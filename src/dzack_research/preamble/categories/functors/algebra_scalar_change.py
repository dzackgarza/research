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

from sage.categories.homset import Hom as _SageHom
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.misc.cachefunc import cached_function
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    FramedAlgebras,
)
from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
    AlgebrasWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedOrders,
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

    return SetMorphism(_SageHom(source, target, SageRings()), image)


def _base_change_presented_element(algebra, element, target, ring_map):
    r"""Carry one element through the selected finite presentation.

    Declared polynomial-engine adapter (``OWN-06``): the selected presentation
    may return either its native polynomial representative or an owned element
    that must be lowered once at this boundary.
    """
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


def _base_change_symmetric_element(algebra, element, target, ring_map):
    r"""Carry one element of a finitely framed symmetric algebra through scalar extension.

    Declared polynomial-engine adapter (``OWN-06``): native monomial keys have
    the univariate and multivariate shapes supplied by the maintained algebra
    engines, and their representation is decoded only here.
    """

    labels = algebra.algebra_generating_set()
    assert labels.cardinality().is_finite(), (
        "scalar extension of a symmetric-algebra morphism requires a finite algebra framing"
    )
    labels = tuple(labels)
    backend = _engine_element(algebra, algebra(element))
    result = target.zero()
    source_base = algebra.base_ring()
    source_base_engine = _engine_ring(source_base)
    for exponent, coefficient in backend.monomial_coefficients().items():
        try:
            powers = tuple(int(value) for value in exponent)
        except TypeError:
            if hasattr(exponent, "exponents"):
                powers = tuple(int(value) for value in exponent.exponents()[0])
            else:
                powers = (int(exponent),)
        if len(powers) != len(labels):
            raise ArithmeticError(
                "the symmetric-algebra engine returned a monomial with the wrong arity"
            )
        scalar = ring_map(
            source_base._from_engine_element(source_base_engine(coefficient))
        )
        term = target.scalar_multiple(scalar, target.one())
        for label, power in zip(labels, powers, strict=True):
            if power:
                term *= target.algebra_generator(label) ** power
        result += term
    return target(result)


class _AlgebraScalarExtensionFunctor(Functor):
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
        super().__init__(
            Algebras(self._source_ring).Associative().Unital(),
            Algebras(self._target_ring).Associative().Unital(),
        )

    def ring_map(self):
        return self._ring_map

    def _apply_object(self, algebra):
        from dzack_research.preamble.categories.algebras.free_algebras import (
            SymmetricAlgebras,
        )

        if algebra in SymmetricAlgebras(self._source_ring):
            from dzack_research.preamble.categories.modules.pure.modules import Modules

            source_module = algebra.generating_module()
            extended_module = Modules(self._source_ring).scalar_extension(self.ring_map())(
                source_module
            )
            return Modules(self._target_ring).symmetric_algebra()(extended_module)

        match algebra in AlgebrasWithChosenFinitePresentation(self._source_ring):
            case True:
                return algebra.base_change(self.ring_map())
            case False:
                from dzack_research.preamble.categories.rings.number_fields import (
                    OrdersWithChosenIntegralBasis,
                )

                assert algebra in OrdersWithChosenIntegralBasis(), (
                    "algebra scalar extension is materialized for algebras with a chosen "
                    "finite commutative polynomial presentation or a number-field order "
                    "with a chosen integral basis"
                )
                return algebra.base_change(self.ring_map())

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        from dzack_research.preamble.categories.algebras.free_algebras import (
            SymmetricAlgebras,
        )
        match (
            morphism.domain() in OwnedOrders()
            and morphism.codomain() in OwnedOrders()
        ):
            case True:
                source_field = morphism.domain().fraction_field()
                target_field = morphism.codomain().fraction_field()
                match _engine_ring(source_field) is SageQQ:
                    case True:
                        return Algebras(source.base_ring()).Associative().Unital().Mor(source, target).identity()
                    case False:
                        pass
                assert _engine_ring(source_field).is_absolute(), (
                    "order-morphism scalar extension uses the selected absolute "
                    "primitive-element presentation"
                )
                primitive_image = morphism.field_embedding()(
                    source_field.primitive_element()
                )
                target_image = target._from_engine_element(
                    _engine_element(target_field, primitive_image)
                )
                return Algebras(source.base_ring()).Associative().Unital().Mor(source, target)(
                    {
                        label: target_image
                        for label in source.algebra_generating_set()
                    }
                )
            case False:
                pass

        if morphism.codomain() in SymmetricAlgebras(self._source_ring):
            return Algebras(source.base_ring()).Associative().Unital().Mor(source, target)(
                lambda label: _base_change_symmetric_element(
                    morphism.codomain(),
                    morphism(morphism.domain().algebra_generator(label)),
                    target,
                    self.ring_map(),
                )
            )

        return Algebras(source.base_ring()).Associative().Unital().Mor(source, target)(
            lambda label: _base_change_presented_element(
                morphism.codomain(),
                morphism(morphism.domain().algebra_generator(label)),
                target,
                self.ring_map(),
            )
        )

    def _repr_(self):
        return f"Algebra scalar extension along {self.ring_map()}"


class _AlgebraRestrictionOfScalarsFunctor(Functor):
    r"""``Res_f : Alg_S -> Alg_R`` along ``f : R -> S``."""

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        self._source_ring = _owned_ring(ring_map.domain())
        self._target_ring = _owned_ring(ring_map.codomain())
        super().__init__(
            Algebras(self._target_ring).Associative().Unital(),
            Algebras(self._source_ring).Associative().Unital(),
        )

    def ring_map(self):
        return self._ring_map

    def _apply_object(self, algebra):
        return algebra.restrict_scalars(self.ring_map())

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        # Restriction changes only the scalar structure; the underlying map is
        # the original algebra morphism.  When the restricted source retains a
        # framing, state the map on that framing so its Hom constructor can
        # check the selected relations.

        if source in FramedAlgebras(source.base_ring()):
            return Algebras(source.base_ring()).Associative().Unital().Mor(source, target)(
                {
                    label: target(
                        morphism(
                            morphism.domain()(source.algebra_generator(label))
                        )
                    )
                    for label in source.algebra_generating_set()
                }
            )
        return Algebras(source.base_ring()).Associative().Unital().Mor(source, target)(
            SetMorphism(
                Sets().Mor(source, target),
                lambda element: target(morphism(morphism.domain()(element))),
            )
        )

    def _repr_(self):
        return f"Algebra restriction of scalars along {self.ring_map()}"


class _AlgebraBaseChangeAdjunction(Adjunction):
    r"""The represented algebra adjunction ``S tensor_R - ⊣ Res_f``."""

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        super().__init__(
            _AlgebraScalarExtensionFunctor(ring_map),
            _AlgebraRestrictionOfScalarsFunctor(ring_map),
        )

    def unit(self, algebra):
        extended = self.left_adjoint()(algebra)
        restricted = self.right_adjoint()(extended)
        return Algebras(algebra.base_ring()).Associative().Unital().Mor(algebra, restricted)(
            lambda label: restricted(extended.algebra_generator(label))
        )

    def counit(self, algebra):
        restricted = self.right_adjoint()(algebra)
        extended = self.left_adjoint()(restricted)
        return Algebras(extended.base_ring()).Associative().Unital().Mor(extended, algebra)(
            lambda label: algebra(restricted.algebra_generator(label))
        )


    def _repr_(self):
        return f"Algebra scalar-extension/restriction adjunction along {self._ring_map}"


@cached_function(key=lambda ring_map: id(ring_map))
def _algebra_base_change_adjunction(ring_map) -> _AlgebraBaseChangeAdjunction:
    return _AlgebraBaseChangeAdjunction(ring_map)


__all__ = []
