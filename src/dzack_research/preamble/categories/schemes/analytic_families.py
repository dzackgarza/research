r"""Analytic-disc families and a supported affine analytification bridge.

The analytic objects here are genuine complex manifolds with the topology of
open subsets of ``C^n``.  The comparison is deliberately narrow: an affine
space over ``QQ`` is first read through the selected embedding ``QQ -> CC`` and
then sent to its complex analytic affine space; polynomial morphisms are sent
to the same polynomial coordinate formulas.  Restricting the analytified
projection ``A^2 -> A^1`` to the unit disc gives the first analytic family.

No formal power series is used to construct the disc.  Coherent GAGA is also
not asserted for this affine example: transport of coherent sheaf cohomology
requires the usual proper complex-algebraic hypotheses, which this family does
not satisfy.
"""

from sage.all import CC as SageCC
from sage.all import QQ as SageQQ
from sage.misc.cachefunc import cached_function, cached_method

from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.manifolds import ComplexManifolds
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    AffineSpaces,
    Schemes,
    _polynomial_exponents,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


def _polynomial_chart_expression(algebra, polynomial, chart, scalar_embedding):
    r"""Raise one algebra polynomial to the corresponding complex chart formula.

    Engine adapter (``OWN-06``): read the private Sage polynomial of an owned
    algebra element and write the Sage symbolic chart expression.
    """
    backend = _engine_element(algebra, algebra(polynomial))
    source_ring = algebra.base_ring()
    target_ring = scalar_embedding.codomain()
    engine_source = _engine_ring(source_ring)
    engine_target = _engine_ring(target_ring)
    variables = tuple(chart.coordinates())
    result = 0
    for exponent, coefficient in backend.monomial_coefficients().items():
        powers = _polynomial_exponents(exponent, len(variables))
        owned_coefficient = _owned_engine_element(source_ring, engine_source(coefficient))
        term = engine_target(_engine_element(target_ring, scalar_embedding(owned_coefficient)))
        for variable, power in zip(variables, powers, strict=True):
            if power:
                term *= variable**power
        result += term
    return result


class _AffineSpaceAnalytificationFunctor(Functor):
    r"""Supported analytification of affine spaces and polynomial maps."""

    def __init__(self, scalar_embedding) -> None:
        self._scalar_embedding = scalar_embedding
        source = _own_ring(scalar_embedding.domain())
        target = _own_ring(scalar_embedding.codomain())
        assert _engine_ring(target) is SageCC, (
            "the represented affine analytification uses the selected embedding into Sage CC"
        )
        super().__init__(AffineSpaces(source), ComplexManifolds())

    def scalar_embedding(self):
        return self._scalar_embedding

    @cached_method
    def _apply_object(self, affine_space):
        labels = tuple(affine_space.coordinate_algebra().algebra_generating_set())
        return ComplexManifolds().affine_space(
            int(affine_space.relative_dimension()),
            name=f"{affine_space}^an",
            coordinate_names=tuple(str(label) for label in labels),
        )

    @cached_method
    def _apply_morphism(self, morphism):
        assert morphism.domain() in self.domain() and morphism.codomain() in self.domain(), (
            "affine analytification maps morphisms between affine spaces over the embedding source"
        )
        analytic_source = self.object_image(morphism.domain())
        analytic_target = self.object_image(morphism.codomain())
        source_chart = analytic_source.atlas()["standard"]
        pullback = morphism.coordinate_algebra_morphism()
        target_algebra = morphism.codomain().coordinate_algebra()
        expressions = tuple(
            _polynomial_chart_expression(
                morphism.domain().coordinate_algebra(),
                pullback(target_algebra.algebra_generator(label)),
                source_chart,
                self.scalar_embedding(),
            )
            for label in target_algebra.algebra_generating_set()
        )
        return analytic_source.holomorphic_polynomial_map(
            analytic_target,
            expressions,
        )

    def _repr_(self):
        return f"Affine analytification along {self.scalar_embedding()}"


@cached_function
def _affine_space_analytification_functor(scalar_embedding):
    return _AffineSpaceAnalytificationFunctor(scalar_embedding)


class _AnalyticDiscFamilyEngine:
    r"""Private realization of one selected object of ``ComplexManifolds()/Delta``.

    The slice object itself retains the analytic family morphism.  This engine
    adds only the chosen algebraic family, analytification, and comparison
    morphism used to exhibit the analytic family as a restriction.
    """

    def __init__(
        self,
        *,
        scalar_embedding,
        algebraic_family,
        analytification,
        analytified_family,
        **rest,
    ) -> None:
        self._scalar_embedding = scalar_embedding
        self._algebraic_family = algebraic_family
        self._analytification = analytification
        self._analytified_family = analytified_family
        super().__init__(**rest)

    def scalar_embedding(self):
        return self._scalar_embedding

    def algebraic_family_morphism(self):
        return self._algebraic_family

    def analytification_functor(self):
        return self._analytification

    def analytified_family_morphism(self):
        return self._analytified_family

    def analytic_base(self):
        return self.target_object()

    def analytic_total_space(self):
        return self.source_object()

    def analytic_family_morphism(self):
        return self.arrow()

    def analytic_family_object(self):
        return self

    def comparison_maps(self):
        total_inclusion = self.analytic_total_space().open_inclusion()
        base_inclusion = self.analytic_base().open_inclusion()
        product = Sets().product((total_inclusion.parent(), base_inclusion.parent()))
        return product((total_inclusion, base_inclusion))

    def comparison_square_commutes(self) -> bool:
        total_inclusion, base_inclusion = self.comparison_maps()
        return (
            base_inclusion * self.analytic_family_morphism()
            == self.analytified_family_morphism() * total_inclusion
        )

    def coherent_gaga_applies(self) -> bool:
        r"""Whether the selected algebraic family satisfies the proper GAGA hypothesis."""
        algebraic_total = self.algebraic_family_morphism().domain()
        return algebraic_total in Schemes(
            algebraic_total.scheme_base_ring()
        ).Projective()

    def _repr_(self) -> str:
        return f"Analytic family {self.analytic_total_space()} -> {self.analytic_base()}"


def AnalyticDiscFamily(radius=1):
    r"""Return the selected holomorphic family as an object of ``ComplexManifolds()/Delta``.

    The algebraic source is ``A^2_QQ -> A^1_QQ``, ``(x,t) |-> t``.  Under the
    selected embedding ``QQ -> CC`` its analytification is ``C^2 -> C``.
    Restricting the base to ``Delta={|t|<r}`` and the total space to its inverse
    image gives the represented slice object.
    """
    qq = _own_ring(SageQQ)
    cc = _own_ring(SageCC)
    embedding = qq.Mor(cc)(lambda scalar: cc(scalar))
    algebraic_total = AffineSpaces(qq)(2, names=("x", "t"))
    algebraic_base = AffineSpaces(qq)(1, names=("t",))
    total_algebra = algebraic_total.coordinate_algebra()
    base_algebra = algebraic_base.coordinate_algebra()
    projection_pullback = base_algebra.Mor(total_algebra)(
        {"t": total_algebra.algebra_generator("t")}
    )
    algebraic_family = algebraic_total.Mor(algebraic_base)(projection_pullback)

    analytification = AffineSpaces(qq).analytification(embedding)
    analytic_total_ambient = analytification(algebraic_total)
    analytic_base_ambient = analytification(algebraic_base)
    analytified_family = analytification(algebraic_family)

    analytic_base = ComplexManifolds().disc(
        radius, "Delta", containing_manifold=analytic_base_ambient,
    )
    total_chart = analytic_total_ambient.atlas()["standard"]
    total_parameter = total_chart.coordinate(1)
    analytic_total = ComplexManifolds().open_submanifold(
        analytic_total_ambient,
        "X_Delta",
        abs(total_parameter) < float(radius),
    )
    restricted_parameter = analytic_total.atlas()["standard"].coordinate(1)
    analytic_family = analytic_total.holomorphic_polynomial_map(
        analytic_base,
        (restricted_parameter,),
    )

    assert analytic_base.open_inclusion() * analytic_family == analytified_family * analytic_total.open_inclusion(), (
        "the analytic disc family does not commute with its algebraic analytification square"
    )

    return ComplexManifolds().SliceOver(analytic_base).object(
        analytic_family,
        _engine=_AnalyticDiscFamilyEngine,
        construction_data={
            "scalar_embedding": embedding,
            "algebraic_family": algebraic_family,
            "analytification": analytification,
            "analytified_family": analytified_family,
        },
    )



__all__ = [
    "AnalyticDiscFamily",
]
