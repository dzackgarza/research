r"""Scalar extension/restriction for algebras and their adjunction.

For a ring morphism ``f : R -> S`` the mathematical adjunction is

``S tensor_R - : Alg_R <-> Alg_S : Res_f``.

Restriction is represented for every live algebra because it changes only the
structure map.  Scalar extension is currently materialized on algebras with a
chosen finite commutative polynomial presentation, exactly the class for which
the algebra layer already knows how to transport relations.  The functors act
on algebra morphisms, and the represented adjunction supplies the actual Hom
bijection, unit, and counit on that executable subdomain.
"""

from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.rings.ring_foundation import OwnedRings as _OwnedRings
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    algebra_homset,
)
from dzack_research.preamble.categories.algebras.finitely_presented_algebras import AlgebrasWithChosenFinitePresentation
from dzack_research.preamble.categories.algebras.restricted_scalars import (
    RestrictedScalarsAlgebras,
    restrict_algebra_scalars,
)
from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


def _engine_ring_map(ring_map):
    r"""Return the same ring morphism with computation-ring endpoints."""
    owned_source = ring_map.domain()
    owned_target = ring_map.codomain()
    source = _engine_ring(owned_source)
    target = _engine_ring(owned_target)

    def image(scalar):
        owned_scalar = owned_source._from_engine_element(source(scalar))
        return _engine_element(owned_target, ring_map(owned_scalar))

    return SetMorphism(source.Hom(target), image)


def _base_change_presented_element(algebra, element, target, ring_map):
    r"""Carry one element through the selected finite presentation."""
    presentation_ring = algebra.presentation_ring()
    presentation = _engine_ring(presentation_ring)
    target_engine = _engine_ring(target)
    presentation_map = presentation.hom(
        [
            _engine_element(target, target.algebra_generator(label))
            for label in algebra.algebra_generating_set()
        ],
        target_engine,
        base_map=_engine_ring_map(ring_map),
    )
    lifted = algebra.lift_to_presentation(element)
    if getattr(lifted, "parent", lambda: None)() is presentation:
        representative = presentation(lifted)
    else:
        representative = _engine_element(presentation_ring, lifted)
    return target._from_engine_element(
        target_engine(presentation_map(representative))
    )


class AlgebraScalarExtensionFunctor(Functor):
    r"""``S tensor_R - : Alg_R -> Alg_S`` along ``f : R -> S``.

    The functor is mathematical on all algebras.  The live object adapter is
    deliberately narrower: it materializes chosen finite polynomial
    presentations and refuses to advertise an unavailable general tensor
    algebra backend as though it had been constructed.
    """

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        self._source_ring = _owned_ring(ring_map.domain())
        self._target_ring = _owned_ring(ring_map.codomain())
        super().__init__(Algebras(self._source_ring), Algebras(self._target_ring))

    def ring_map(self):
        return self._ring_map

    def _apply_object(self, algebra):
        if algebra not in AlgebrasWithChosenFinitePresentation(self._source_ring):
            raise NotImplementedError(
                "algebra scalar extension is currently materialized for algebras "
                "with a chosen finite commutative polynomial presentation"
            )
        extended = algebra.base_change(self.ring_map())
        extended._preamble_scalar_extension_source_algebra = algebra
        extended._preamble_scalar_extension_ring_map = self.ring_map()
        return extended

    def source_algebra(self, extended_algebra):
        r"""Return the algebra recorded by this scalar-extension construction."""
        source = getattr(
            extended_algebra,
            "_preamble_scalar_extension_source_algebra",
            None,
        )
        ring_map = getattr(
            extended_algebra,
            "_preamble_scalar_extension_ring_map",
            None,
        )
        if source is None or ring_map is not self.ring_map():
            raise ValueError(
                f"{extended_algebra} was not constructed by scalar extension along "
                f"{self.ring_map()}"
            )
        return source

    chosen_preimage = source_algebra

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return algebra_homset(source, target)(
            lambda label: _base_change_presented_element(
                morphism.codomain(),
                morphism(morphism.domain().algebra_generator(label)),
                target,
                self.ring_map(),
            )
        )

    def _repr_(self):
        return f"Algebra scalar extension along {self.ring_map()}"


class AlgebraRestrictionOfScalarsFunctor(Functor):
    r"""``Res_f : Alg_S -> Alg_R`` along ``f : R -> S``."""

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        self._source_ring = _owned_ring(ring_map.domain())
        self._target_ring = _owned_ring(ring_map.codomain())
        super().__init__(Algebras(self._target_ring), Algebras(self._source_ring))

    def ring_map(self):
        return self._ring_map

    def _apply_object(self, algebra):
        return restrict_algebra_scalars(algebra, self.ring_map())

    def chosen_preimage(self, image):
        if image in RestrictedScalarsAlgebras(self._source_ring):
            if image.ring_map() is self.ring_map():
                return image.algebra_over_extension()
        return super().chosen_preimage(image)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        # Restriction changes only the scalar structure; the underlying map is
        # the original algebra morphism.  When the restricted source retains a
        # framing, state the map on that framing so its Hom constructor can
        # check the selected relations.
        from dzack_research.preamble.categories.algebras.algebras import FramedAlgebras

        if source in FramedAlgebras(source.base_ring()):
            return algebra_homset(source, target)(
                {
                    label: target(
                        morphism(
                            morphism.domain()(source.algebra_generator(label))
                        )
                    )
                    for label in source.algebra_generating_set()
                }
            )
        return algebra_homset(source, target)(
            SetMorphism(
                Sets().hom(source, target),
                lambda element: target(morphism(morphism.domain()(element))),
            )
        )

    def _repr_(self):
        return f"Algebra restriction of scalars along {self.ring_map()}"


class AlgebraBaseChangeAdjunction(Adjunction):
    r"""The represented algebra adjunction ``S tensor_R - ⊣ Res_f``."""

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        super().__init__(
            AlgebraScalarExtensionFunctor(ring_map),
            AlgebraRestrictionOfScalarsFunctor(ring_map),
        )

    def unit(self, algebra):
        extended = self.left_adjoint()(algebra)
        restricted = self.right_adjoint()(extended)
        return algebra_homset(algebra, restricted)(
            lambda label: restricted(extended.algebra_generator(label))
        )

    def counit(self, algebra):
        restricted = self.right_adjoint()(algebra)
        extended = self.left_adjoint()(restricted)
        return algebra_homset(extended, algebra)(
            lambda label: algebra(restricted.algebra_generator(label))
        )


    def _repr_(self):
        return f"Algebra scalar-extension/restriction adjunction along {self._ring_map}"


@cached_function
def algebra_base_change_adjunction(ring_map) -> AlgebraBaseChangeAdjunction:
    return AlgebraBaseChangeAdjunction(ring_map)


__all__ = [
    "AlgebraBaseChangeAdjunction",
    "AlgebraRestrictionOfScalarsFunctor",
    "AlgebraScalarExtensionFunctor",
    "algebra_base_change_adjunction",
]
