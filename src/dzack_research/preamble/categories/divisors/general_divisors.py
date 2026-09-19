"""General divisor data and divisor-class quotient constructions.

This module keeps Weil-divisor data separate from class presentations.
On a represented normal Noetherian affine integral scheme, the Weil divisor
group is the sparse free abelian group on *all* height-one points.  Principal
divisors have finite support, computed from primary decomposition and local
lengths.  Cartier divisors themselves are global sections of
``K_X^*/O_X^*`` and are owned by :mod:`cartier_divisor_groups`.

Class groups are obtained from explicit principal-divisor presentations
(``PicardGroups().picard_to_class_group_morphism``).  A presentation may be
finite even when the full Weil divisor group is not; the presentation is
retained rather than identified with the full divisor group.
"""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.divisors.class_groups import ClassGroups
from dzack_research.preamble.categories.divisors.picard_groups import PicardGroups
from dzack_research.preamble.categories.divisors.weil_divisor_groups import WeilDivisorGroups
from dzack_research.preamble.categories.rings.commutative_algebra import (
    _engine_ideal,
    _owned_ideal,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedIntegralDomains,
    OwnedNoetherianRings,
    _own_ring,
)


def _integers():
    return _own_ring(SageZZ)


def _affine_normal_weil_divisor_group(scheme):
    r"""``Div(X)`` for a represented normal Noetherian affine integral scheme ``X``.

    The framing is the actual height-one locus of ``Spec(A)``.  It is
    generally infinite; elements remain finite-support sparse sums.
    """
    ring = scheme.coordinate_algebra()
    assert ring in OwnedIntegralDomains(), (
        "Weil divisors in this construction require an integral affine scheme"
    )
    assert ring in OwnedNoetherianRings(), (
        "Weil divisors in this construction require a Noetherian coordinate ring"
    )
    assert ring.is_normal(), "Weil divisors in this construction require a normal coordinate ring"
    return WeilDivisorGroups()(
        scheme,
        ring.spectrum().condition_set(lambda point: point.height() == 1),
    )


def _effective_principal_coefficients(group, function):
    r"""The coefficients of ``div(f)`` for a nonzero regular function ``f``.

    The primes of height one containing ``f`` are the radicals of the primary
    components of ``(f)``; at each, ``f`` has the valuation of the discrete
    valuation ring ``A_p``.  The unit ideal has no primary component, so a
    unit contributes no prime divisor.
    """
    ring = group.affine_divisor_coordinate_ring()
    function = ring(function)
    assert not function.is_zero(), "the divisor of the zero rational function is not a Weil divisor"
    engine_ideal = _engine_ideal(ring, ring.ideal(function))
    coefficients = {}
    for primary in engine_ideal.primary_decomposition():
        prime = group.divisor_scheme().underlying_space()(_owned_ideal(ring, primary.radical()))
        if prime.height() != 1:
            continue
        local_ring = prime.local_ring()
        uniformizers = local_ring.maximal_ideal().minimal_module_generators()
        assert uniformizers.cardinality() == 1, (
            "a height-one local ring of a normal Noetherian domain is a discrete valuation ring"
        )
        uniformizer = next(iter(uniformizers))
        multiplicity = local_ring(function).valuation(uniformizer)
        if multiplicity:
            coefficients[prime] = coefficients.get(prime, _integers().zero()) + multiplicity
    return coefficients


def _principal_weil_divisor(group, rational_function):
    r"""``div(f)`` in a represented affine-normal Weil divisor group."""
    ring = group.affine_divisor_coordinate_ring()
    function = ring.fraction_field()(rational_function)
    coefficients = _effective_principal_coefficients(group, ring(function.numerator()))
    for prime, multiplicity in _effective_principal_coefficients(
        group,
        ring(function.denominator()),
    ).items():
        value = coefficients.get(prime, _integers().zero()) - multiplicity
        if value:
            coefficients[prime] = value
        else:
            coefficients.pop(prime, None)
    framing = group.prime_divisor_locus()
    assert all(prime in framing for prime in coefficients), (
        "div(f) is supported on prime divisors outside the framing of this Weil divisor group"
    )
    return group.linear_combination(coefficients)


def _projective_space_picard_to_class_group_morphism(
    projective_space,
    base_picard_group,
    base_class_group,
    base_picard_to_class,
):
    r"""\(\operatorname{Pic}(\mathbb{P}^n_S) \to \operatorname{Cl}(\mathbb{P}^n_S)\) from the projective-bundle formulas.

    For the represented projective space ``P^n_S`` the supplied base groups
    are transported through

    ``Pic(P^n_S)=Pic(S) + ZZ[O(1)]`` and
    ``Cl(P^n_S)=Cl(S) + ZZ[H]``.

    The comparison is the supplied ``Pic(S)->Cl(S)`` on the base summand and
    the identity on the hyperplane summand.  Requiring the base class group and
    its comparison map prevents this construction from silently replacing a
    nontrivial base contribution by zero.
    """
    assert base_picard_to_class.domain() is base_picard_group, (
        "the base Picard-to-class morphism has the wrong domain"
    )
    assert base_picard_to_class.codomain() is base_class_group, (
        "the base Picard-to-class morphism has the wrong codomain"
    )
    picard = PicardGroups().projective_bundle(projective_space, base_picard_group)
    classes = ClassGroups().projective_bundle(projective_space, base_class_group)
    picard_hyperplane = picard.projective_hyperplane_factor()
    class_hyperplane = classes.biproduct_factor(1)
    class_hyperplane_label = class_hyperplane.module_generating_set()[0]
    hyperplane_map = picard_hyperplane.module_category().Mor(picard_hyperplane, class_hyperplane)(
        {
            picard_hyperplane.module_generating_set()[0]: class_hyperplane.module_generator(
                class_hyperplane_label
            )
        }
    )
    comparison = base_picard_to_class.biproduct_map(
        hyperplane_map,
        source=picard,
        target=classes,
    )
    weil_hyperplane = classes.injection(1)(class_hyperplane.module_generator(class_hyperplane_label))
    assert comparison(picard.hyperplane_class()) == weil_hyperplane, (
        "the hyperplane class did not map to the Weil hyperplane class"
    )
    return comparison


__all__ = []
