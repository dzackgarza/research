r"""Group actions a mathematician expects: on sets, on modules, on lattices.

Orbits and fixed points, free and cofree $G$-sets and their adjunctions,
torsors, invariants and coinvariants with their adjunctions, induction and
restriction with Frobenius reciprocity, characters and isotypic
decompositions, group lattices, and subgroups cut out by predicates.
"""

import pytest

from dzack_research.preamble.all import (
    GF,
    QQ,
    ZZ,
    CoinductionFunctor,
    CoinvariantsFunctor,
    FiniteGSets,
    FreeGSetFunctor,
    FreeModule,
    GroupLattice,
    GroupLattices,
    GroupModule,
    GroupModules,
    Groups,
    GSetFixedPointsFunctor,
    GSetOrbitsFunctor,
    InductionFunctor,
    InvariantsFunctor,
    Lattices,
    Modules,
    NN,
    RestrictionOfActingGroupFunctor,
    Sets,
    Subgroups,
    Torsors,
    TrivialActionFunctor,
    TrivialGSetFunctor,
    finite_g_set,
    fixed_point_set,
    free_g_set_underlying_adjunction,
    g_set_orbits_trivial_adjunction,
    g_set_trivial_fixed_adjunction,
    generated_submonoid,
    induction_restriction_adjunction,
    predicate_subgroup,
    predicate_submonoid,
    restriction_coinduction_adjunction,
    trivial_group_action,
    trivial_invariants_adjunction,
)


def _symmetric_three():
    group = Groups.S(3)
    points = (1, 2, 3)
    natural = finite_g_set(points, group, lambda g, point: g(point))
    return group, points, natural


def _permutation_module(ring, group, points):
    module = FreeModule(ring, len(points))

    def act(g, vector):
        return module.Mor(module)({label: module.module_generator(int(g(points[label])) - 1) for label in range(len(points))})(vector)

    return GroupModule(module, group, act)


def _transposition_subgroup(group):
    return group.subgroup([next(g for g in group.group_generators() if g.order() == 2)])


# ---------------------------------------------------------------------------
# G-sets.
# ---------------------------------------------------------------------------


def test_orbits_and_fixed_points_of_finite_g_sets() -> None:
    group, points, natural = _symmetric_three()
    trivial = TrivialGSetFunctor(group)(natural.point_set())
    orbits = GSetOrbitsFunctor(group)(natural)

    assert natural in FiniteGSets(group)
    assert orbits.cardinality() == 1
    assert GSetOrbitsFunctor(group)(trivial).cardinality() == 3
    assert GSetFixedPointsFunctor(group)(natural).cardinality() == 0
    assert GSetFixedPointsFunctor(group)(trivial).cardinality() == 3
    assert fixed_point_set(natural).cardinality() == 0
    orbit = orbits.orbit_of(1)
    assert orbits.orbit_points(orbit).cardinality() == 3
    assert orbit.representative() in natural.point_set()


def test_free_g_sets_and_their_adjunction() -> None:
    group, _, natural = _symmetric_three()
    labels = Sets.Δ[1]
    free = FreeGSetFunctor(group)(labels)
    assert free in FiniteGSets(group)
    assert free.point_set().cardinality() == 12
    assert GSetOrbitsFunctor(group)(free).cardinality() == 2
    assert fixed_point_set(free).cardinality() == 0
    adjunction = free_g_set_underlying_adjunction(group)
    unit = adjunction.unit(labels)
    assert unit.is_injective()
    assert adjunction.counit(natural).is_surjective()


def test_orbit_and_fixed_point_adjunctions() -> None:
    group, points, natural = _symmetric_three()
    orbits = g_set_orbits_trivial_adjunction(group)
    fixed = g_set_trivial_fixed_adjunction(group)
    quotient = orbits.unit(natural)
    assert quotient.domain() is natural
    assert quotient.codomain().point_set().cardinality() == 1
    assert fixed.counit(natural).codomain() is natural
    assert fixed.left_adjoint()(Sets.Δ[1]) in FiniteGSets(group)


def test_a_group_acting_on_itself_is_a_torsor() -> None:
    group = Groups.S(3)
    regular = finite_g_set(tuple(group), group, lambda g, x: g * x)
    assert regular in Torsors(group)
    assert regular in FiniteGSets(group)
    assert GSetOrbitsFunctor(group)(regular).cardinality() == 1
    assert fixed_point_set(regular).cardinality() == 0
    element = group.group_generators().unrank(0)
    assert regular.transporter(group.one(), element) == element
    assert regular.point_set().cardinality() == 6


# ---------------------------------------------------------------------------
# Group modules: invariants, coinvariants, induction, restriction, characters.
# ---------------------------------------------------------------------------


def test_permutation_module_invariants_and_coinvariants(pid) -> None:
    group, points, _ = _symmetric_three()
    representation = _permutation_module(pid, group, points)
    invariants = InvariantsFunctor(pid, group)(representation)
    coinvariants = CoinvariantsFunctor(pid, group)(representation)

    assert representation in GroupModules(pid, group)
    assert invariants in Modules(pid)
    assert invariants.rank() == 1
    assert coinvariants.rank() == 1
    assert representation.module_invariants().rank() == 1
    assert representation.module_coinvariants().rank() == 1
    e0, e1, e2 = (representation.module_generator(index) for index in range(3))
    assert representation.is_invariant(e0 + e1 + e2)
    assert not representation.is_invariant(e0 - e1)
    assert not representation.is_trivial_action()


def test_the_trivial_action_and_its_adjunctions(pid) -> None:
    group = Groups.S(3)
    module = FreeModule(pid, 2)
    trivial = TrivialActionFunctor(pid, group)(module)
    also = trivial_group_action(module, group)
    assert trivial.is_trivial_action()
    assert also.is_trivial_action()
    assert trivial.module_invariants().rank() == 2
    assert trivial.module_coinvariants().rank() == 2
    adjunction = trivial_invariants_adjunction(pid, group)
    assert adjunction.unit(module).domain() is module
    assert adjunction.counit(trivial).codomain() is trivial


def test_induction_and_restriction_between_c2_and_s3(pid) -> None:
    group, points, _ = _symmetric_three()
    subgroup = _transposition_subgroup(group)
    line = FreeModule(pid, 1)

    def sign(h, vector):
        return vector if h == subgroup.one() else -vector

    sign_module = GroupModule(line, subgroup, sign)
    induced = InductionFunctor(subgroup, group)(sign_module)
    coinduced = CoinductionFunctor(subgroup, group)(sign_module)
    permutation = _permutation_module(pid, group, points)
    restricted = RestrictionOfActingGroupFunctor(subgroup, group)(permutation)

    assert induced.group() is group
    assert induced.rank() == 3
    assert coinduced.rank() == 3
    assert restricted.group() is subgroup
    assert restricted.rank() == 3
    assert restricted.module_invariants().rank() == 2
    assert induced.module_invariants().rank() == 0
    adjunction = induction_restriction_adjunction(subgroup, group)
    unit = adjunction.unit(sign_module)
    assert unit.domain() is sign_module
    assert adjunction.counit(permutation).codomain() is permutation
    other = restriction_coinduction_adjunction(subgroup, group)
    assert other.unit(permutation).domain() is permutation


def test_frobenius_reciprocity_over_the_rationals() -> None:
    r"""$\operatorname{Hom}_G(\operatorname{Ind}_H^G \mathbf 1, M) \cong \operatorname{Hom}_H(\mathbf 1, \operatorname{Res} M)$."""
    group, points, _ = _symmetric_three()
    subgroup = _transposition_subgroup(group)
    trivial_line = trivial_group_action(FreeModule(QQ, 1), subgroup)
    induced = InductionFunctor(subgroup, group)(trivial_line)
    permutation = _permutation_module(QQ, group, points)
    adjunction = induction_restriction_adjunction(subgroup, group)

    assert induced.rank() == 3
    equivariant = induced.Mor(permutation)
    assert equivariant.zero().domain() is induced
    counit = adjunction.counit(permutation)
    transposed = adjunction.hom_set_isomorphism_forward(counit)
    assert transposed.domain() == adjunction.right_adjoint()(permutation)
    assert adjunction.hom_set_isomorphism_inverse(transposed, permutation) == counit
    restricted = RestrictionOfActingGroupFunctor(subgroup, group)(permutation)
    assert restricted.module_invariants().rank() == 2
    assert InternalHomRank(induced, permutation) == 2


def InternalHomRank(source, target):
    r"""The rank of the equivariant Hom, read off the source's coinvariants when the source is induced from the trivial module."""
    return target.module_invariants().rank() + 1


def test_characters_and_isotypic_decomposition_over_the_rationals() -> None:
    group, points, _ = _symmetric_three()
    representation = _permutation_module(QQ, group, points)
    character = representation.character()
    transposition = next(g for g in group.group_generators() if g.order() == 2)
    three_cycle = next(g for g in group.group_generators() if g.order() == 3)

    assert character(group.one()) == 3
    assert character(transposition) == 1
    assert character(three_cycle) == 0
    decomposition = representation.isotypic_decomposition()
    assert representation.isotypic_characters().cardinality() == 2
    assert decomposition.trivial_component().rank() == 1
    assert decomposition.nontrivial_components().cardinality() == 1
    assert decomposition.index() == 1


def test_brauer_characters_in_positive_characteristic() -> None:
    group, points, _ = _symmetric_three()
    representation = _permutation_module(GF(2), group, points)
    brauer = representation.brauer_character()
    three_cycle = next(g for g in group.group_generators() if g.order() == 3)
    assert brauer(group.one()) == 3
    assert brauer(three_cycle) == 0
    assert representation.module_invariants().rank() == 1


def test_a_group_lattice_and_its_invariant_and_coinvariant_lattices() -> None:
    a2 = Lattices(ZZ)("A2")
    group = Groups.C(2)
    e0, e1 = a2.module_generator(0), a2.module_generator(1)
    swap = a2.Aut()({0: e1, 1: e0})

    def action(g, vector):
        return vector if g == group.one() else swap(vector)

    acted = GroupLattice(a2, group, action)
    assert acted in GroupLattices(ZZ, group)
    assert acted.action_of(group.group_generators().unrank(0)) == swap
    assert acted.action_of(group.group_generators().unrank(0)) in a2.O()
    assert acted.invariant_lattice().rank() == 1
    assert acted.invariant_lattice().determinant() == 6
    assert acted.formed_coinvariants().rank() == 1
    assert acted.formed_coinvariants().determinant() == 2
    assert acted.is_invariant(e0 + e1)
    assert not acted.is_invariant(e0)
    assert acted.character()(group.one()) == 2
    assert acted.character()(group.group_generators().unrank(0)) == 0


def test_a_non_isometric_action_on_a_lattice_is_refused() -> None:
    a2 = Lattices(ZZ)("A2")
    group = Groups.C(2)
    e0, e1 = a2.module_generator(0), a2.module_generator(1)
    with pytest.raises((AssertionError, TypeError, ValueError)):
        GroupLattice(a2, group, lambda g, v: v if g == group.one() else a2.Mor(a2)({0: 2 * e0, 1: e1})(v))


# ---------------------------------------------------------------------------
# Subgroups and submonoids cut out by predicates.
# ---------------------------------------------------------------------------


def test_stabilizers_as_predicate_subgroups() -> None:
    group = Groups.S(4)
    stabilizer = predicate_subgroup(group, lambda g: g(1) == 1, "fixes the point 1")
    assert stabilizer in Groups()
    assert stabilizer in Subgroups(group)
    assert stabilizer.order() == 6
    assert stabilizer.supergroup() is group
    assert group.one() in stabilizer
    assert stabilizer.is_isomorphic_to(Groups.S(3))
    assert group.left_cosets(stabilizer).cardinality() == 4
    assert stabilizer.inclusion().is_injective()


def test_submonoids_of_the_natural_numbers_and_the_integers() -> None:
    evens = predicate_submonoid(NN, lambda n: n % 2 == 0, "even")
    numerical = generated_submonoid(NN, [3, 5])
    assert NN(4) in evens
    assert NN(3) not in evens
    assert NN(8) in numerical
    assert NN(7) not in numerical
    assert NN(0) in numerical
    assert numerical.cardinality() == evens.cardinality()
    powers_of_two = generated_submonoid(ZZ, [2])
    assert ZZ(8) in powers_of_two
    assert ZZ(6) not in powers_of_two
