r"""Base change of schemes, and the slice adjunction along a base morphism.

For a ring morphism ``g: R -> R'`` the base-change functor is

``- x_{Spec R} Spec R' : Sch/R -> Sch/R'``.

On an affine scheme ``Spec A`` it is ``Spec(A tensor_R R')``, computed by
scalar extension of the coordinate algebra, and the result is equipped as the
fibre product of the cospan ``Spec A -> Spec R <- Spec R'`` with its two
projections and the universal factorization.

For a morphism of schemes ``g: S' -> S`` over one ring, pullback along ``g``
is the functor ``g^*: Sch/S -> Sch/S'``, ``(X -> S) |-> (X x_S S' -> S')``,
and composition with ``g`` is ``Sigma_g: Sch/S' -> Sch/S``,
``(X -> S') |-> (X -> S' -> S)``.  These form the adjunction
``Sigma_g ⊣ g^*`` whose unit at ``X -> S'`` is the cone map
``X -> X x_S S'`` and whose counit at ``Y -> S`` is the projection
``Y x_S S' -> Y`` (Stacks, Tag 01JO for the fibre product; the adjunction is
the universal property of the fibre product read in the two slices).
"""

from sage.misc.cachefunc import cached_function, cached_method

from dzack_research.preamble.categories.abstract_categories.arrow_categories import SliceOver
from dzack_research.preamble.categories.algebras.algebras import FramedAlgebras
from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
    AlgebrasWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    SymmetricAlgebraOn,
    SymmetricAlgebras,
)
from dzack_research.preamble.categories.functors.algebra_scalar_change import (
    _base_change_presented_element,
    _engine_ring_map,
)
from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    _engine_element,
    _engine_ring,
    _owned_ring,
    ring_morphism,
)
from dzack_research.preamble.categories.schemes.schemes import (
    AffineSchemes,
    AffineSpace,
    AffineSpaces,
    FiberProductSchemes,
    ProjectiveSpace,
    ProjectiveSpaces,
    Schemes,
    Spec,
    _affine_morphism_from_pullback,
    refine_scheme,
    scheme_fiber_product,
)


def _base_changed_algebra(algebra, ring_map):
    r"""``A tensor_R R'`` for the coordinate algebras the scheme layer builds.

    Presented algebras carry their own scalar extension.  A polynomial
    algebra is ``Sym`` of a free module, and ``Sym`` commutes with base
    change, so ``R[S] tensor_R R' = R'[S]``; the ring itself extends to
    ``R'``.  The polynomial and scalar cases are stated here because the
    algebra layer's scalar extension is materialized only on chosen finite
    presentations.
    """
    source = _owned_ring(ring_map.domain())
    target = _owned_ring(ring_map.codomain())
    match algebra:
        case _ if algebra is source:
            return target
        case _ if algebra in AlgebrasWithChosenFinitePresentation(source):
            return algebra.base_change(ring_map)
        case _ if algebra in SymmetricAlgebras(source) and algebra in FramedAlgebras(source):
            return SymmetricAlgebraOn(target, algebra.algebra_generating_set())
        case _:
            assert False, (
                f"base change of {algebra} along {ring_map} is not represented: it needs a "
                "chosen finite presentation, a polynomial framing, or the scalar ring itself"
            )


def _base_changed_element(algebra, element, changed_algebra, ring_map):
    r"""The image of ``a`` under the canonical ``A -> A tensor_R R'``."""
    source = _owned_ring(ring_map.domain())
    match algebra:
        case _ if algebra is source:
            return ring_map(element)
        case _ if algebra in AlgebrasWithChosenFinitePresentation(source):
            return _base_change_presented_element(algebra, element, changed_algebra, ring_map)
        case _:
            engine_image = _engine_element(algebra, element).map_coefficients(
                _engine_ring_map(ring_map),
                new_base_ring=_engine_ring(_owned_ring(ring_map.codomain())),
            )
            return changed_algebra._from_engine_element(_engine_ring(changed_algebra)(engine_image))


def _base_change_unit(algebra, changed_algebra, ring_map):
    r"""The ring morphism ``A -> A tensor_R R'`` with its engine realization."""
    source = _owned_ring(ring_map.domain())
    changed_engine = _engine_ring(changed_algebra)
    match algebra:
        case _ if algebra is source:
            engine = ring_map._engine_morphism_crossing()
        case _:
            engine = _engine_ring(algebra).hom(
                [
                    changed_engine(_engine_element(changed_algebra, changed_algebra.algebra_generator(label)))
                    for label in algebra.algebra_generating_set()
                ],
                changed_engine,
                base_map=_engine_ring_map(ring_map),
            )
    return ring_morphism(
        algebra,
        changed_algebra,
        lambda element: _base_changed_element(algebra, element, changed_algebra, ring_map),
        engine_morphism=engine,
    )


class SchemeBaseChangeFunctor(Functor):
    r"""``- x_{Spec R} Spec R' : Sch/R -> Sch/R'`` along ``g: R -> R'``."""

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        self._source_ring = _owned_ring(ring_map.domain())
        self._target_ring = _owned_ring(ring_map.codomain())
        super().__init__(Schemes(self._source_ring), Schemes(self._target_ring))

    def ring_map(self):
        return self._ring_map

    @cached_method
    def base_morphism(self):
        r"""``Spec g: Spec R' -> Spec R``, the affine morphism induced by the ring map."""
        return _affine_morphism_from_pullback(
            Spec(self._target_ring, base_ring=self._target_ring),
            Spec(self._source_ring, base_ring=self._source_ring),
            self.ring_map(),
        )

    def projection(self, scheme):
        r"""The projection ``X x_{Spec R} Spec R' -> X``."""
        return self(scheme).left_projection()

    def _apply_object(self, scheme):
        source, target = self._source_ring, self._target_ring
        match scheme:
            case _ if scheme in AffineSpaces(source):
                changed = AffineSpace(
                    scheme.relative_dimension(),
                    target,
                    names=tuple(str(label) for label in scheme.coordinate_algebra().algebra_generating_set()),
                )
            case _ if scheme in ProjectiveSpaces(source):
                return ProjectiveSpace(scheme.relative_dimension(), target, names=scheme.variable_names())
            case _ if scheme in AffineSchemes(source):
                changed = Spec(_base_changed_algebra(scheme.coordinate_algebra(), self.ring_map()), base_ring=target)
            case _:
                assert False, f"base change of {scheme} is represented for affine schemes and projective spaces"
        algebra = scheme.coordinate_algebra()
        changed_algebra = changed.coordinate_algebra()
        unit = _base_change_unit(algebra, changed_algebra, self.ring_map())
        projection = _affine_morphism_from_pullback(changed, scheme, unit)

        def factor(to_scheme, to_base):
            r"""``A tensor_R R' -> C`` from ``A -> C`` and ``R' -> C`` agreeing on ``R``."""
            assert to_scheme.codomain() is to_base.codomain(), "a pushout cocone has one codomain"
            cocone_algebra = to_scheme.codomain()
            match algebra:
                case _ if algebra is source:
                    return to_base
                case _:
                    return changed_algebra.Mor(cocone_algebra)(
                        {label: to_scheme(algebra.algebra_generator(label)) for label in algebra.algebra_generating_set()}
                    )

        changed._preamble_fiber_product_cospan = (scheme.structure_morphism(), self.base_morphism())
        changed._preamble_fiber_product_projections = (projection, changed.structure_morphism())
        changed._preamble_fiber_product_cocone_factorization = factor
        return refine_scheme(changed, target, [FiberProductSchemes(target)])

    def _apply_morphism(self, morphism):
        source_scheme = self(morphism.domain())
        target_scheme = self(morphism.codomain())
        pullback = morphism.coordinate_algebra_morphism()
        codomain_algebra = morphism.codomain().coordinate_algebra()
        domain_algebra = morphism.domain().coordinate_algebra()
        changed_codomain_algebra = target_scheme.coordinate_algebra()
        changed_domain_algebra = source_scheme.coordinate_algebra()
        match codomain_algebra:
            case _ if codomain_algebra is self._source_ring:
                changed_pullback = changed_domain_algebra.algebra_structure_morphism()
            case _:
                changed_pullback = changed_codomain_algebra.Mor(changed_domain_algebra)(
                    {
                        label: _base_changed_element(
                            domain_algebra,
                            pullback(codomain_algebra.algebra_generator(label)),
                            changed_domain_algebra,
                            self.ring_map(),
                        )
                        for label in codomain_algebra.algebra_generating_set()
                    }
                )
        changed = _affine_morphism_from_pullback(source_scheme, target_scheme, changed_pullback)
        assert self.projection(morphism.codomain()) * changed == morphism * self.projection(morphism.domain()), (
            "the base-changed morphism does not commute with the projections"
        )
        return changed

    def _repr_(self):
        return f"Base change of schemes along {self.ring_map()}"


@cached_function
def scheme_base_change_functor(ring_map) -> SchemeBaseChangeFunctor:
    return SchemeBaseChangeFunctor(ring_map)


class SlicePullbackFunctor(Functor):
    r"""``g^*: Sch/S -> Sch/S'``, ``(X -> S) |-> (X x_S S' -> S')``."""

    def __init__(self, base_morphism) -> None:
        self._base_morphism = base_morphism
        schemes = Schemes(base_morphism.codomain().scheme_base_ring())
        super().__init__(
            SliceOver(schemes, base_morphism.codomain()),
            SliceOver(schemes, base_morphism.domain()),
        )

    def base_morphism(self):
        return self._base_morphism

    def _apply_object(self, family):
        pulled_back = scheme_fiber_product(family.arrow(), self.base_morphism())
        return self.codomain()(pulled_back.right_projection())

    def _apply_morphism(self, triangle):
        source = self(triangle.domain()).arrow().domain()
        target = self(triangle.codomain()).arrow().domain()
        induced = target.from_pullback_cone(
            triangle.left() * source.left_projection(),
            source.right_projection(),
        )
        return self.codomain().Mor(self(triangle.domain()), self(triangle.codomain()))(induced)

    def _repr_(self):
        return f"Pullback of families along {self.base_morphism()}"


class SliceCompositionFunctor(Functor):
    r"""``Sigma_g: Sch/S' -> Sch/S``, ``(X -> S') |-> (X -> S' -> S)``."""

    def __init__(self, base_morphism) -> None:
        self._base_morphism = base_morphism
        schemes = Schemes(base_morphism.codomain().scheme_base_ring())
        super().__init__(
            SliceOver(schemes, base_morphism.domain()),
            SliceOver(schemes, base_morphism.codomain()),
        )

    def base_morphism(self):
        return self._base_morphism

    def _apply_object(self, family):
        return self.codomain()(self.base_morphism() * family.arrow())

    def _apply_morphism(self, triangle):
        return self.codomain().Mor(self(triangle.domain()), self(triangle.codomain()))(triangle.left())

    def _repr_(self):
        return f"Composition of families with {self.base_morphism()}"


class SliceBaseChangeAdjunction(Adjunction):
    r"""``Sigma_g ⊣ g^*`` for a base morphism ``g: S' -> S``."""

    def __init__(self, base_morphism) -> None:
        self._base_morphism = base_morphism
        super().__init__(SliceCompositionFunctor(base_morphism), SlicePullbackFunctor(base_morphism))

    def base_morphism(self):
        return self._base_morphism

    def unit(self, family):
        r"""``X -> X x_S S'`` over ``S'``, the cone with legs ``id_X`` and ``X -> S'``."""
        composed = self.left_adjoint()(family)
        pulled_back = self.right_adjoint()(composed)
        scheme = family.arrow().domain()
        cone = pulled_back.arrow().domain().from_pullback_cone(
            scheme.categorical_identity_morphism(),
            family.arrow(),
        )
        return self.left_adjoint().domain().Mor(family, pulled_back)(cone)

    def counit(self, family):
        r"""``Y x_S S' -> Y`` over ``S``, the projection to the family."""
        pulled_back = self.right_adjoint()(family)
        composed = self.left_adjoint()(pulled_back)
        projection = pulled_back.arrow().domain().left_projection()
        return self.right_adjoint().domain().Mor(composed, family)(projection)

    def _repr_(self):
        return f"Composition/pullback adjunction along {self.base_morphism()}"


@cached_function
def slice_base_change_adjunction(base_morphism) -> SliceBaseChangeAdjunction:
    return SliceBaseChangeAdjunction(base_morphism)


__all__ = [
    "SchemeBaseChangeFunctor",
    "SliceBaseChangeAdjunction",
    "SliceCompositionFunctor",
    "SlicePullbackFunctor",
    "scheme_base_change_functor",
    "slice_base_change_adjunction",
]
