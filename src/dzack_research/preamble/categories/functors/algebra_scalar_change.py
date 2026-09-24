r"""Scalar extension/restriction for algebras and their adjunction.

For a ring morphism ``f : R -> S`` the mathematical adjunction is

``S tensor_R - : Alg_R <-> Alg_S : Res_f``.

Restriction is represented for every live algebra because it changes only the
structure map.  Scalar extension is materialized on tensor/symmetric free
constructions through scalar change of their exact generating module, and on
chosen finite commutative polynomial presentations through their selected
relations.  The functors act on algebra morphisms, and the represented
adjunction supplies the actual Mor bijection, unit, and counit on that
executable subdomain.
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
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
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
        owned_scalar = _owned_engine_element(owned_source, source(scalar))
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
    return _owned_engine_element(target,
        target_engine(presentation_map(representative))
    )


def _base_change_free_algebra_element(algebra, element, target, ring_map):
    r"""Carry one tensor/symmetric-algebra element through its full module factor.

    The free construction already owns a framing by all words/monomials.  A
    coefficient change therefore acts on that actual underlying module; the
    consumer does not decode a second native monomial representation or reduce
    the algebra to its degree-one generating module.
    """
    source_labels = algebra.module_generating_set()
    target_labels = target.module_generating_set()
    result = target.zero()
    for label, coefficient in algebra.framing_coefficients(algebra(element)).items():
        source_label = source_labels(label)
        target_label = target_labels(source_label)
        result += target.scalar_multiple(
            ring_map(coefficient),
            target.module_generator(target_label),
        )
    return result


class _AlgebraScalarExtensionFunctor(Functor):
    r"""``S tensor_R - : Alg_R -> Alg_S`` along ``f : R -> S``.

    The functor is mathematical on all algebras.  The live object adapter is
    deliberately narrower: it materializes tensor/symmetric free algebras from
    the scalar-changed generating module, chosen finite commutative polynomial
    presentations from their relations, and the selected number-field order
    cases.  It does not advertise an unavailable general algebra tensor backend
    as though it had been constructed.
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
            TensorAlgebras,
        )
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        match (
            algebra in TensorAlgebras(self._source_ring),
            algebra in SymmetricAlgebras(self._source_ring),
        ):
            case (True, False):
                source_module = algebra.generating_module()
                extended_module = Modules(self._source_ring).scalar_extension(
                    self.ring_map()
                )(source_module)
                return Modules(self._target_ring).tensor_algebra()(extended_module)
            case (False, True):
                source_module = algebra.generating_module()
                extended_module = Modules(self._source_ring).scalar_extension(
                    self.ring_map()
                )(source_module)
                return Modules(self._target_ring).symmetric_algebra()(extended_module)
            case _:
                pass

        match algebra in AlgebrasWithChosenFinitePresentation(self._source_ring):
            case True:
                return algebra.base_change(self.ring_map())
            case False:
                from dzack_research.preamble.categories.rings.number_fields import (
                    OrdersWithChosenIntegralBasis,
                )

                assert algebra in OrdersWithChosenIntegralBasis(), (
                    f"scalar extension of the algebra {algebra} is computed only for a commutative algebra given "
                    "by finitely many generators and relations, or an order in a number field with an integral basis"
                )
                return algebra.base_change(self.ring_map())

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        from dzack_research.preamble.categories.algebras.free_algebras import (
            SymmetricAlgebras,
            TensorAlgebras,
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
                    f"scalar extension of the order morphism {morphism} is computed only over an absolute number "
                    f"field, but {source_field} is a relative extension"
                )
                primitive_image = morphism.field_embedding()(
                    source_field.primitive_element()
                )
                target_image = _owned_engine_element(target,
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

        match (
            morphism.codomain() in TensorAlgebras(self._source_ring),
            morphism.codomain() in SymmetricAlgebras(self._source_ring),
        ):
            case (True, _) | (_, True):
                return Algebras(source.base_ring()).Associative().Unital().Mor(source, target)(
                    lambda label: _base_change_free_algebra_element(
                        morphism.codomain(),
                        morphism(morphism.domain().algebra_generator(label)),
                        target,
                        self.ring_map(),
                    )
                )
            case _:
                pass

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
        # framing, state the map on that framing so its Mor constructor can
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

    def _unit_component(self, algebra):
        extended = self.left_adjoint()(algebra)
        restricted = self.right_adjoint()(extended)
        return Algebras(algebra.base_ring()).Associative().Unital().Mor(algebra, restricted)(
            lambda label: restricted(extended.algebra_generator(label))
        )

    def _counit_component(self, algebra):
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
