r"""A session in representation theory of finite groups over several coefficient rings.

Permutation representations, characters and their inner products, isotypic
decompositions, restriction and induction, Frobenius reciprocity, and the
same objects over the integers and over a field of positive characteristic.
"""

import pytest
from sage.misc.latex import latex

from dzack_research.preamble.all import (
    GF,
    QQ,
    ZZ,
    CoinductionFunctor,
    FreeModule,
    GroupModule,
    GroupModules,
    Groups,
    InductionFunctor,
    Modules,
    RestrictionOfActingGroupFunctor,
    induction_restriction_adjunction,
    trivial_group_action,
)


def rendered(obj) -> str:
    text = repr(obj)
    assert "object at 0x" not in text
    assert "object at 0x" not in latex(obj)
    return text


SESSIONS = {
    # name: (group, degree of natural action, number of orbits on pairs, |Hom_G(perm, perm)|-rank)
    "S3": (lambda: Groups.S(3), 3, 2),
    "S4": (lambda: Groups.S(4), 4, 2),
    "A4": (lambda: Groups.A(4), 4, 2),
    "D4": (lambda: Groups.D(4), 4, 3),
}
COEFFICIENTS = {"QQ": lambda: QQ, "ZZ": lambda: ZZ, "GF(2)": lambda: GF(2), "GF(3)": lambda: GF(3)}


def _permutation_module(ring, group, degree):
    points = tuple(range(1, degree + 1))
    module = FreeModule(ring, degree)

    def act(g, vector):
        return module.Mor(module)({label: module.module_generator(int(g(points[label])) - 1) for label in range(degree)})(vector)

    return GroupModule(module, group, act)


@pytest.mark.parametrize("name", sorted(SESSIONS))
@pytest.mark.parametrize("coefficients", sorted(COEFFICIENTS))
def test_a_representation_theory_session(name, coefficients) -> None:
    build, degree, endomorphism_rank = SESSIONS[name]
    ring = COEFFICIENTS[coefficients]()
    group = build()
    rendered(group)

    # The permutation representation and its invariants.
    permutation = _permutation_module(ring, group, degree)
    rendered(permutation)
    assert permutation in GroupModules(ring, group)
    assert permutation in Modules(ring)
    assert permutation.rank() == degree
    assert permutation.group() is group
    generator = group.group_generators().unrank(0)
    assert permutation.action_of(generator) * permutation.action_of(generator.inverse()) == permutation.action_of(group.one())
    invariants = permutation.module_invariants()
    coinvariants = permutation.module_coinvariants()
    rendered(invariants)
    rendered(coinvariants)
    assert invariants.rank() == 1
    assert coinvariants.rank() == 1
    total = sum((permutation.module_generator(label) for label in range(degree)), permutation.zero())
    assert permutation.is_invariant(total)
    assert invariants.inclusion().is_in_image(total)

    # Equivariant endomorphisms: their rank counts orbits on pairs.
    endomorphisms = permutation.Mor(permutation)
    rendered(endomorphisms)
    assert endomorphisms.identity()(total) == total
    assert permutation.equivariant_endomorphism_module().rank() == endomorphism_rank

    # Characters over the rationals; Brauer characters in positive characteristic.
    if coefficients == "QQ":
        character = permutation.character()
        rendered(character)
        assert character(group.one()) == degree
        assert character(generator) == sum(1 for point in range(1, degree + 1) if generator(point) == point)
        decomposition = permutation.isotypic_decomposition()
        rendered(decomposition)
        assert decomposition.trivial_component().rank() == 1
        assert decomposition.index() == 1
        assert permutation.isotypic_characters().cardinality() == endomorphism_rank
        components = decomposition.nontrivial_components()
        assert sum(component.rank() for component in components) + 1 == degree
    if coefficients.startswith("GF"):
        brauer = permutation.brauer_character()
        rendered(brauer)
        assert brauer(group.one()) == degree

    # Restriction to a cyclic subgroup, induction back, Frobenius reciprocity.
    subgroup = group.subgroup([generator])
    rendered(subgroup)
    restricted = RestrictionOfActingGroupFunctor(subgroup, group)(permutation)
    rendered(restricted)
    assert restricted.group() is subgroup
    assert restricted.rank() == degree
    assert restricted.module_invariants().rank() >= 1
    trivial = trivial_group_action(FreeModule(ring, 1), subgroup)
    induced = InductionFunctor(subgroup, group)(trivial)
    coinduced = CoinductionFunctor(subgroup, group)(trivial)
    rendered(induced)
    assert induced.rank() == group.order() // subgroup.order()
    assert coinduced.rank() == induced.rank()
    assert induced.module_invariants().rank() == 1
    adjunction = induction_restriction_adjunction(subgroup, group)
    unit = adjunction.unit(trivial)
    counit = adjunction.counit(permutation)
    rendered(unit)
    assert unit.domain() is trivial
    assert counit.codomain() is permutation
    transposed = adjunction.hom_set_isomorphism_forward(counit)
    assert adjunction.hom_set_isomorphism_inverse(transposed, permutation) == counit
    if coefficients == "QQ":
        assert induced.character()(group.one()) == induced.rank()
        assert induced.isotypic_decomposition().trivial_component().rank() == 1
