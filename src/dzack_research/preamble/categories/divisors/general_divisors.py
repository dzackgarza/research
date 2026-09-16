"""General divisor data and divisor-class quotient constructions.

This module keeps concrete divisor data separate from class presentations.
On a represented normal Noetherian affine integral scheme, the Weil divisor
group is the sparse free abelian group on *all* height-one points.  Principal
divisors have finite support, computed from primary decomposition and local
lengths.  Cartier data on a finite affine atlas retain their local rational
equations and the unit transition ratios, hence their associated line bundle.

Class groups are obtained from explicit principal-divisor presentations.  A
presentation may be finite even when the full Weil divisor group is not; the
presentation is retained rather than identified with the full divisor group.
"""

from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.divisors.class_groups import ClassGroups
from dzack_research.preamble.categories.divisors.invertible_sheaves import FiniteAtlasInvertibleSheaf
from dzack_research.preamble.categories.divisors.picard_groups import (
    PicardGroups,
    _ProjectivePicardConstruction,
)
from dzack_research.preamble.categories.divisors.weil_divisor_groups import (
    WeilDivisorGroups,
    _AffineNormalWeilDivisorConstruction,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.commutative_algebra import (
    _engine_ideal,
    _owned_ideal,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedIntegralDomains,
    OwnedNoetherianRings,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set



def _integers():
    return _own_ring(SageZZ)


def _affine_normal_weil_divisor_group(scheme):
    r"""Return ``WDiv(X)`` for a represented normal Noetherian affine integral scheme.

    The basis is the actual height-one locus of ``Spec(A)``.  It is generally
    infinite; elements remain finite-support sparse sums.
    """
    ring = scheme.coordinate_algebra()
    if ring not in OwnedIntegralDomains():
        raise TypeError("Weil divisors in this construction require an integral affine scheme")
    if ring not in OwnedNoetherianRings():
        raise TypeError("Weil divisors in this construction require a Noetherian coordinate ring")
    if not ring.is_normal():
        raise TypeError("Weil divisors in this construction require a normal coordinate ring")
    spectrum = ring.spectrum()
    prime_locus = spectrum.condition_set(lambda point: point.height() == 1)
    return _integers()._fresh_free_module_on(
        prime_locus,
        _extra_categories=(WeilDivisorGroups(),),
        _extra_construction_data={
            "_weil_divisor_construction": _AffineNormalWeilDivisorConstruction(scheme),
        },
    )


def _effective_principal_coefficients(group, function):
    ring = group.affine_divisor_coordinate_ring()
    function = ring(function)
    if function.is_zero():
        raise ValueError("the divisor of the zero rational function is not a Weil divisor")
    ideal = ring.ideal(function)
    engine_ideal = _engine_ideal(ring, ideal)
    try:
        if bool(engine_ideal.is_one()):
            return {}
    except (AttributeError, TypeError):
        pass
    coefficients = {}
    for primary in engine_ideal.primary_decomposition():
        radical = primary.radical()
        prime = group.divisor_scheme().underlying_space()(_owned_ideal(ring, radical))
        if prime.height() != 1:
            continue
        local_ring = prime.local_ring()
        local_maximal = local_ring.maximal_ideal()
        uniformizers = local_maximal.minimal_module_generators()
        if uniformizers.cardinality() != 1:
            raise ArithmeticError(
                "a height-one local ring of a normal Noetherian domain must be a DVR"
            )
        uniformizer = next(iter(uniformizers))
        multiplicity = local_ring(function).valuation(uniformizer)
        if multiplicity:
            coefficients[prime] = coefficients.get(prime, _integers().zero()) + multiplicity
    return coefficients


def _principal_weil_divisor(group, rational_function):
    r"""Return ``div(f)`` in a represented affine-normal Weil divisor group."""
    ring = group.affine_divisor_coordinate_ring()
    field = ring.fraction_field()
    function = field(rational_function)
    numerator = ring(function.numerator())
    denominator = ring(function.denominator())
    coefficients = _effective_principal_coefficients(group, numerator)
    for prime, multiplicity in _effective_principal_coefficients(group, denominator).items():
        value = coefficients.get(prime, _integers().zero()) - multiplicity
        if value:
            coefficients[prime] = value
        else:
            coefficients.pop(prime, None)
    return group.linear_combination(coefficients)


def _fraction_pullback(ring_morphism, fraction):
    target_ring = ring_morphism.codomain()
    target_field = target_ring.fraction_field()
    return target_field.fraction(
        ring_morphism(fraction.numerator()),
        ring_morphism(fraction.denominator()),
    )


class FiniteAtlasCartierDivisor(SageObject):
    r"""A Cartier divisor given by local rational equations on a finite affine atlas."""

    def __init__(self, gluing_datum, local_equations) -> None:
        self._gluing_datum = gluing_datum
        supplied = dict(local_equations)
        if set(supplied) != set(gluing_datum.chart_indices()):
            raise ValueError("a Cartier datum requires one local equation on every atlas chart")
        self._local_equations = {}
        for index in gluing_datum.chart_indices():
            ring = gluing_datum.chart(index).coordinate_algebra()
            equation = ring.fraction_field()(supplied[index])
            if equation.is_zero():
                raise ValueError("a Cartier local equation is a nonzero rational function")
            self._local_equations[index] = equation
        self._transition_units = {
            pair: self._compute_transition_unit(*pair)
            for pair in gluing_datum.transition_index_set()
        }

    def gluing_datum(self):
        return self._gluing_datum

    def scheme(self):
        return self.gluing_datum().scheme()

    def local_equation(self, index):
        index = self.gluing_datum().normalize_chart_index(index)
        return self._local_equations[index]

    def _restricted_equation(self, source_index, target_index):
        overlap = self.gluing_datum().overlap(source_index, target_index)
        restriction = overlap.inclusion().coordinate_algebra_morphism()
        return _fraction_pullback(restriction, self.local_equation(source_index))

    def _compute_transition_unit(self, source_index, target_index):
        datum = self.gluing_datum()
        source_equation = self._restricted_equation(source_index, target_index)
        target_equation = self._restricted_equation(target_index, source_index)
        transition = datum.transition_between(source_index, target_index).forward()
        target_on_source = _fraction_pullback(
            transition.coordinate_algebra_morphism(),
            target_equation,
        )
        field = datum.overlap(source_index, target_index).coordinate_algebra().fraction_field()
        ratio = field.fraction(
            source_equation.numerator() * target_on_source.denominator(),
            source_equation.denominator() * target_on_source.numerator(),
        )
        overlap_ring = datum.overlap(source_index, target_index).coordinate_algebra()
        try:
            unit = overlap_ring(ratio)
        except (TypeError, ValueError) as error:
            raise ValueError(
                "Cartier local equations must have a regular transition ratio on every overlap"
            ) from error
        if not unit.is_unit():
            raise ValueError("Cartier local equations must differ by a unit on every overlap")
        return unit

    def transition_unit(self, source_index, target_index):
        datum = self.gluing_datum()
        source_index = datum.normalize_chart_index(source_index)
        target_index = datum.normalize_chart_index(target_index)
        pair = next(
            pair
            for pair in datum.transition_index_set()
            if {pair[0], pair[1]} == {source_index, target_index}
        )
        unit = self._transition_units[pair]
        if pair == (source_index, target_index):
            return unit
        reverse = datum.transition_between(source_index, target_index).forward()
        return reverse.coordinate_algebra_morphism()(unit.inverse_of_unit())

    def associated_invertible_sheaf(self):
        return FiniteAtlasInvertibleSheaf(
            self.gluing_datum(),
            self._transition_units,
            associated_divisor=self,
        )

    line_bundle = associated_invertible_sheaf

    def _repr_(self):
        return f"Cartier divisor on {self.scheme()} from finite-atlas local equations"


class DivisorClassTheory(SageObject):
    r"""The comparison ``Pic(X) -> Cl(X)`` for one represented scheme.

    This is deliberately class-level data, not a replacement for the full
    Cartier and Weil divisor groups.  It retains the two class groups and the
    actual comparison morphism between them, so a locally factorial example
    may have an isomorphism here while a singular normal example need not.
    """

    def __init__(self, scheme, picard_group, class_group, picard_to_class) -> None:
        if picard_group.picard_scheme() is not scheme:
            raise ValueError("the Picard group belongs to a different scheme")
        if class_group.class_group_scheme() is not scheme:
            raise ValueError("the Weil class group belongs to a different scheme")
        if picard_to_class.domain() is not picard_group:
            raise ValueError("the Picard-to-class comparison has the wrong domain")
        if picard_to_class.codomain() is not class_group:
            raise ValueError("the Picard-to-class comparison has the wrong codomain")
        self._scheme = scheme
        self._picard_group = picard_group
        self._class_group = class_group
        self._picard_to_class = picard_to_class

    def scheme(self):
        return self._scheme

    def picard_group(self):
        return self._picard_group

    def class_group(self):
        return self._class_group

    def picard_to_class_group_morphism(self):
        return self._picard_to_class

    def _repr_(self):
        return f"Divisor-class theory of {self.scheme()}"


def _projective_space_divisor_class_theory(
    projective_space,
    base_picard_group,
    base_class_group,
    base_picard_to_class,
):
    r"""Return the projective-bundle formulas for ``Pic`` and ``Cl``.

    For the represented projective space ``P^n_S`` the supplied base groups
    are transported through

    ``Pic(P^n_S)=Pic(S) + ZZ[O(1)]`` and
    ``Cl(P^n_S)=Cl(S) + ZZ[H]``.

    The comparison is the supplied ``Pic(S)->Cl(S)`` on the base summand and
    the identity on the hyperplane summand.  Requiring the base class group and
    its comparison map prevents this construction from silently replacing a
    nontrivial base contribution by zero.
    """
    if base_picard_to_class.domain() is not base_picard_group:
        raise ValueError("the base Picard-to-class morphism has the wrong domain")
    if base_picard_to_class.codomain() is not base_class_group:
        raise ValueError("the base Picard-to-class morphism has the wrong codomain")
    base_scheme = projective_space.base_scheme()
    if base_picard_group.picard_scheme() is not base_scheme:
        raise ValueError("the supplied Picard group is not attached to the projective base")
    if base_class_group.class_group_scheme() is not base_scheme:
        raise ValueError("the supplied class group is not attached to the projective base")

    integers = _integers()
    picard_hyperplane = integers._fresh_free_module_on(
        finite_ordered_set(("O(1)",)),
    )
    class_hyperplane = integers._fresh_free_module_on(
        finite_ordered_set(("H",)),
    )
    modules = Modules(integers)
    picard_biproduct = modules.biproduct((base_picard_group, picard_hyperplane))
    class_biproduct = modules.biproduct((base_class_group, class_hyperplane))
    picard = PicardGroups()(
        picard_biproduct,
        scheme=projective_space,
        construction=_ProjectivePicardConstruction(
            projective_space,
            base_picard_group,
            picard_hyperplane,
            picard_biproduct,
        ),
    )
    classes = ClassGroups()(class_biproduct, scheme=projective_space)
    picard_hyperplane_label = picard_hyperplane.module_generating_set()[0]
    class_hyperplane_label = class_hyperplane.module_generating_set()[0]
    hyperplane_map = picard_hyperplane.module_category().Mor(picard_hyperplane, class_hyperplane)(
        {picard_hyperplane_label: class_hyperplane.module_generator(class_hyperplane_label)}
    )
    raw_comparison = base_picard_to_class.biproduct_map(
        hyperplane_map,
        source=picard_biproduct,
        target=class_biproduct,
    )
    forget_picard_role = picard.module_category().Mor(picard, picard_biproduct)(
        {
            label: picard_biproduct.module_generator(label)
            for label in picard.module_generating_set()
        }
    )
    equip_class_role = class_biproduct.module_category().Mor(class_biproduct, classes)(
        {
            label: classes.module_generator(label)
            for label in class_biproduct.module_generating_set()
        }
    )
    comparison = equip_class_role * raw_comparison * forget_picard_role
    theory = DivisorClassTheory(projective_space, picard, classes, comparison)
    weil_hyperplane = equip_class_role(
        class_biproduct.right_inclusion()(
            class_hyperplane.module_generator(class_hyperplane_label)
        )
    )
    if comparison(picard.hyperplane_class()) != weil_hyperplane:
        raise ArithmeticError("the hyperplane class did not map to the Weil hyperplane class")
    return theory


def _projective_space_picard_group(projective_space, base_picard_group):
    r"""Return ``Pic(P^n_S) = Pic(S) direct_sum ZZ[O(1)]`` from represented ``Pic(S)``.

    The base Picard group is required input.  In particular this construction
    never replaces it by zero merely because the total space is projective.
    """
    integers = _integers()
    if base_picard_group.base_ring() is not integers:
        raise TypeError("a Picard group is an abelian group over ZZ")
    hyperplane = integers._fresh_free_module_on(finite_ordered_set(("O(1)",)))
    decomposition = Modules(integers).biproduct((base_picard_group, hyperplane))
    return PicardGroups()(
        decomposition,
        scheme=projective_space,
        construction=_ProjectivePicardConstruction(
            projective_space,
            base_picard_group,
            hyperplane,
            decomposition,
        ),
    )


class DivisorClassComparison(SageObject):
    r"""The quotient square from principal, Cartier and Weil divisor presentations."""

    def __init__(
        self,
        scheme,
        principal_source,
        cartier_group,
        weil_group,
        principal_to_cartier,
        principal_to_weil,
        cartier_to_weil,
    ) -> None:
        if principal_to_cartier.domain() is not principal_source:
            raise ValueError("the Cartier principal-divisor map has the wrong source")
        if principal_to_weil.domain() is not principal_source:
            raise ValueError("the Weil principal-divisor map has the wrong source")
        if principal_to_cartier.codomain() is not cartier_group:
            raise ValueError("the Cartier principal-divisor map has the wrong target")
        if principal_to_weil.codomain() is not weil_group:
            raise ValueError("the Weil principal-divisor map has the wrong target")
        if cartier_to_weil.domain() is not cartier_group or cartier_to_weil.codomain() is not weil_group:
            raise ValueError("the Cartier-to-Weil comparison has the wrong endpoints")
        for label in principal_source.module_generating_set():
            generator = principal_source.module_generator(label)
            if cartier_to_weil(principal_to_cartier(generator)) != principal_to_weil(generator):
                raise ValueError("the principal/Cartier/Weil comparison square does not commute")
        self._scheme = scheme
        self._principal_source = principal_source
        self._cartier_group = cartier_group
        self._weil_group = weil_group
        self._principal_to_cartier = principal_to_cartier
        self._principal_to_weil = principal_to_weil
        self._cartier_to_weil = cartier_to_weil
        cartier_cokernel = principal_to_cartier.cokernel()
        weil_cokernel = principal_to_weil.cokernel()
        self._picard_group = PicardGroups()(cartier_cokernel, scheme=scheme)
        self._class_group = ClassGroups()(weil_cokernel, scheme=scheme)
        self._cartier_class_projection = self._projection_to_role(
            cartier_cokernel.cokernel_projection(),
            cartier_cokernel,
            self._picard_group,
        )
        self._weil_class_projection = self._projection_to_role(
            weil_cokernel.cokernel_projection(),
            weil_cokernel,
            self._class_group,
        )
        self._picard_to_class = self._picard_group.module_category().Mor(self._picard_group, self._class_group)(
            {
                label: self._weil_class_projection(
                    cartier_to_weil(cartier_group.module_generator(label))
                )
                for label in self._picard_group.module_generating_set()
            }
        )

    @staticmethod
    def _projection_to_role(projection, cokernel, role):
        copy = cokernel.module_category().Mor(cokernel, role)(
            {label: role.module_generator(label) for label in cokernel.module_generating_set()}
        )
        return copy * projection

    def scheme(self):
        return self._scheme

    def cartier_divisor_group(self):
        return self._cartier_group

    def weil_divisor_group(self):
        return self._weil_group

    def principal_divisor_source(self):
        return self._principal_source

    def principal_to_weil_morphism(self):
        return self._principal_to_weil

    def picard_group(self):
        return self._picard_group

    def class_group(self):
        return self._class_group

    def cartier_to_weil_morphism(self):
        return self._cartier_to_weil

    def cartier_class_projection(self):
        return self._cartier_class_projection

    def weil_class_projection(self):
        return self._weil_class_projection

    def picard_to_class_group_morphism(self):
        return self._picard_to_class

    def _repr_(self) -> str:
        return f"Divisor-class comparison on {self.scheme()}: {self.picard_group()} -> {self.class_group()}"



__all__ = [
    "DivisorClassTheory",
    "DivisorClassComparison",
    "FiniteAtlasCartierDivisor",
]
