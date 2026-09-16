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
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.manifolds import ComplexManifolds
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    AffineSpaces,
    Schemes,
)


def _polynomial_chart_expression(algebra, polynomial, chart, scalar_embedding):
    r"""Raise one algebra polynomial to the corresponding complex chart formula."""
    backend = _engine_element(algebra, algebra(polynomial))
    source_ring = algebra.base_ring()
    target_ring = scalar_embedding.codomain()
    engine_source = _engine_ring(source_ring)
    engine_target = _engine_ring(target_ring)
    variables = tuple(chart.coordinates())
    result = 0
    for exponent, coefficient in backend.monomial_coefficients().items():
        try:
            powers = tuple(int(value) for value in exponent)
        except TypeError:
            powers = (int(exponent),)
        owned_coefficient = source_ring._from_engine_element(engine_source(coefficient))
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
        if morphism.domain() not in self.domain() or morphism.codomain() not in self.domain():
            raise TypeError("affine analytification currently maps polynomial morphisms of affine spaces")
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


class AnalyticDiscFamily(SageObject):
    r"""The analytic family ``Delta x C -> Delta`` from algebraic projection.

    The algebraic source is ``A^2_QQ -> A^1_QQ``, ``(x,t) |-> t``.  Under the
    selected embedding ``QQ -> CC`` its analytification is ``C^2 -> C``.
    Restricting the base to ``Delta={|t|<r}`` and the total space to its inverse
    image gives a holomorphic family over an actual analytic disc.
    """

    def __init__(self, radius=1) -> None:
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

        base_chart = analytic_base_ambient.atlas()["standard"]
        base_coordinate = base_chart.coordinate(0)
        analytic_base = ComplexManifolds().open_submanifold(
            analytic_base_ambient,
            "Delta",
            abs(base_coordinate) < float(radius),
        )
        analytic_base._preamble_disc_radius = float(radius)

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

        if analytic_base.open_inclusion() * analytic_family != analytified_family * analytic_total.open_inclusion():
            raise ArithmeticError("the analytic disc family does not commute with its algebraic analytification square")

        self._scalar_embedding = embedding
        self._algebraic_total = algebraic_total
        self._algebraic_base = algebraic_base
        self._algebraic_family = algebraic_family
        self._analytification = analytification
        self._analytic_total_ambient = analytic_total_ambient
        self._analytic_base_ambient = analytic_base_ambient
        self._analytified_family = analytified_family
        self._analytic_total = analytic_total
        self._analytic_base = analytic_base
        self._analytic_family = analytic_family
        self._slice_object = ComplexManifolds().SliceOver(analytic_base)(analytic_family)

    def scalar_embedding(self):
        return self._scalar_embedding

    def algebraic_family_morphism(self):
        return self._algebraic_family

    def analytification_functor(self):
        return self._analytification

    def analytified_family_morphism(self):
        return self._analytified_family

    def analytic_base(self):
        return self._analytic_base

    def analytic_total_space(self):
        return self._analytic_total

    def analytic_family_morphism(self):
        return self._analytic_family

    def analytic_family_object(self):
        return self._slice_object

    def comparison_maps(self):
        return (
            self.analytic_total_space().open_inclusion(),
            self.analytic_base().open_inclusion(),
        )

    def comparison_square_commutes(self) -> bool:
        total_inclusion, base_inclusion = self.comparison_maps()
        return (
            base_inclusion * self.analytic_family_morphism()
            == self.analytified_family_morphism() * total_inclusion
        )

    def coherent_gaga_applies(self) -> bool:
        r"""Return whether this selected family satisfies the proper GAGA hypothesis."""
        return self._algebraic_total in Schemes(
            self._algebraic_total.scheme_base_ring()
        ).Projective()

    def _repr_(self) -> str:
        return f"Analytic family {self.analytic_total_space()} -> {self.analytic_base()}"



__all__ = [
    "AnalyticDiscFamily",
]
