r"""Restriction of scalar constants for represented graded power algebras."""

import operator

from sage.categories.action import Action
from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.algebras import FramedAlgebras
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumElement,
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _owned_ring,
)
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets


class _DegreeZeroAlgebraMultiplication(Action):
    r"""Multiplication of a graded algebra by its canonical degree-zero subalgebra."""

    def __init__(self, degree_zero_algebra, graded_algebra, *, actor_on_left: bool):
        self._graded_algebra = graded_algebra
        self._actor_on_left = actor_on_left
        super().__init__(
            degree_zero_algebra,
            graded_algebra,
            is_left=actor_on_left,
            op=operator.mul,
        )

    def _act_(self, actor, element):
        embedded = self._graded_algebra.from_degree_zero(actor)
        if self._actor_on_left:
            return self._graded_algebra.multiply(embedded, element)
        return self._graded_algebra.multiply(element, embedded)


class RestrictedGradedAlgebraElement(GradedDirectSumElement):
    def _mul_(self, other):
        return self.parent().multiply(self, other)

    def _acted_upon_(self, actor, self_on_left):
        r"""Let the canonical degree-zero subalgebra multiply this element."""
        parent = self.parent()
        actor_parent = actor.parent() if hasattr(actor, "parent") else None
        if actor_parent is parent.degree_zero_algebra():
            actor = parent.from_degree_zero(actor)
            return (
                parent.multiply(self, actor)
                if self_on_left
                else parent.multiply(actor, self)
            )
        return super()._acted_upon_(actor, self_on_left)


class RestrictedGradedAlgebra(GradedDirectSumModule):
    r"""The same graded ring read over the constants of its degree-zero algebra."""

    Element = RestrictedGradedAlgebraElement

    def is_commutative(self):
        r"""The same multiplication read over fewer scalars commutes exactly when it did."""
        return self._extension_algebra.is_commutative()

    def __init__(self, extension_algebra, ring_map, *, extra_categories=()) -> None:
        self._extension_algebra = extension_algebra
        self._ring_map = ring_map
        self._degree_zero_algebra = extension_algebra.base_ring()
        base = _owned_ring(ring_map.domain())
        self._preamble_algebra_base_ring = base
        self._restricted_pieces = {}

        def piece(degree):
            degree = int(degree)
            cached = self._restricted_pieces.get(degree)
            if cached is not None:
                return cached
            extension_piece = extension_algebra.graded_piece(degree)
            result = extension_piece.restrict_scalars(ring_map)
            self._restricted_pieces[degree] = result
            return result

        def realize_generator(degree, label):
            restricted_piece = piece(degree)
            underlying = restricted_piece.module_generator(label).underlying_element()
            return extension_algebra._from_component(degree, underlying)

        def from_realization(element):
            element = extension_algebra(element)
            return self.from_components({degree: piece(degree)(component) for degree, component in element.homogeneous_components().items()})

        categories = [
            GradedAlgebras(base),
            GradedAlgebras(base).Supercommutative().Alternating(),
            *tuple(extra_categories),
        ]
        try:
            degree_zero_labels = self.degree_zero_algebra().algebra_generating_set()
            degree_one_labels = extension_algebra.free_source_module().module_generating_set()
        except (AttributeError, TypeError):
            self._preamble_algebra_generating_set = None
        else:
            framing = Sets().coproduct(
                indexed_family(
                    Sets.Δ[1],
                    lambda index: (
                        degree_zero_labels if int(index) == 0 else degree_one_labels
                    ),
                )
            )
            self._preamble_algebra_generating_set = framing

            def generator_value(tagged):
                if int(tagged.summand_index()) == 0:
                    return self.from_degree_zero(self.degree_zero_algebra().algebra_generator(tagged.summand_element()))
                return self.from_realization(self.extension_algebra().algebra_generator(tagged.summand_element()))

            self._preamble_algebra_generator_values = indexed_family(
                framing,
                generator_value,
                name="Restricted graded-algebra generators",
            )
            categories.append(FramedAlgebras(base))
        GradedDirectSumModule.__init__(
            self,
            base,
            piece,
            name=f"{extension_algebra} over {base}",
            realize_generator=realize_generator,
            realized_object=extension_algebra,
            from_realization=from_realization,
            extra_categories=tuple(categories),
        )
        for actor_on_left in (True, False):
            self.degree_zero_algebra().register_action(
                _DegreeZeroAlgebraMultiplication(
                    self.degree_zero_algebra(),
                    self,
                    actor_on_left=actor_on_left,
                )
            )

    def extension_algebra(self):
        return self._extension_algebra

    def degree_zero_algebra(self):
        return self._degree_zero_algebra

    def ring_map(self):
        return self._ring_map

    def algebra_base_ring(self):
        return self.base_ring()

    def _element_constructor_(self, value):
        r"""Include the degree-zero algebra into the restricted graded algebra.

        The degree-zero algebra is part of this algebra's defining graded
        structure, not an unrelated scalar parent.  Its canonical inclusion
        is therefore valid ordinary element ingress in addition to the sparse
        graded-direct-sum representation.
        """
        parent = value.parent() if hasattr(value, "parent") else None
        if parent is self.degree_zero_algebra():
            return self.from_degree_zero(value)
        return super()._element_constructor_(value)

    def _coerce_map_from_(self, source):
        if source is self.degree_zero_algebra():
            return True
        return super()._coerce_map_from_(source)

    def _get_action_(self, source, op, self_on_left):
        if op is operator.mul and source is self.degree_zero_algebra():
            return _DegreeZeroAlgebraMultiplication(
                source,
                self,
                actor_on_left=not self_on_left,
            )
        return super()._get_action_(source, op, self_on_left)

    def multiply(self, left, right):
        return self.from_realization(self.realize(left) * self.realize(right))

    def realize(self, element):
        r"""Return the same finite homogeneous sum in the extension algebra.

        The restricted homogeneous pieces need not themselves carry a finite
        framing over the smaller constants ring.  Realization therefore uses
        the stored underlying element of each restricted piece directly,
        rather than expanding it in an artificial restricted-scalar basis.
        """
        element = self(element)
        result = self.extension_algebra().zero()
        for degree, component in element.homogeneous_components().items():
            underlying = component.underlying_element() if hasattr(component, "underlying_element") else component
            result += self.extension_algebra()._from_component(degree, underlying)
        return result

    def one(self):
        return self.from_realization(self.extension_algebra().one())

    def _an_element_(self):
        r"""Return the unit as a canonical live specimen of this algebra."""
        return self.one()

    def algebra_generating_set(self):
        assert self._preamble_algebra_generating_set is not None, (
            "algebra_generating_set requires a selected finite algebra framing on this restricted graded algebra"
        )
        return self._preamble_algebra_generating_set

    def algebra_generator(self, label):
        r"""Return the generator at a point of the coproduct framing.

        The framing is the coproduct of the degree-zero algebra's generating
        set with the extension module's, so a label carries which summand it
        came from and its point there.
        """
        labels = self.algebra_generating_set()
        if label not in labels:
            raise ValueError(f"{label!r} is not an algebra-generator label")
        return self._preamble_algebra_generator_values[label]

    def algebra_structure_morphism(self):
        return self.base_ring().Mor(self)(
            lambda scalar: self.from_degree_zero(self.degree_zero_algebra()(self.ring_map()(scalar))),
        )

    def from_degree_zero(self, element):
        return self.from_realization(self.extension_algebra()(element))

    def degree_zero_element(self, element):
        realized = self.realize(element)
        component = realized.homogeneous_component(0)
        coefficients = realized.parent().graded_piece(0).framing_coefficients(component)
        scalar = coefficients.get(0, self.degree_zero_algebra().zero())
        return self.degree_zero_algebra()(scalar)


@cached_function(key=lambda algebra, ring_map: (id(algebra), id(ring_map)))
def _restrict_graded_algebra_scalars(algebra, ring_map):
    result = RestrictedGradedAlgebra(algebra, ring_map)
    return result


__all__ = [
    "RestrictedGradedAlgebra",
    "RestrictedGradedAlgebraElement",
]
