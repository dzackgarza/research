r"""The three verification milestones of the indefinite orbit program.

Each milestone fixes a lattice and asks for the orbit data of one Witt index.

Milestone 1, ``h = 1``: ``E10 = U + E8``, the even unimodular Lorentzian
lattice ``II_{1,9}`` (Conway--Sloane, *Sphere Packings, Lattices and Groups*,
ch. 26).  Its single cusp, the reduction ``e^perp/e = E8`` and the Eichler
transvections of the unipotent radical are asserted in
``test_cusp_lattices.py`` and ``test_parabolic_induction.py``; what is added
here is the Levi half of ``1 -> U_I -> P_I -> M_I -> 1``, namely that the
cusp stabilizer acts nontrivially on the reduction.  That action is onto
``O(E8)``, which is a theorem and not something a method body establishes.

Milestone 2, ``h = 2``: ``N = U + U(2) + E8(-2)``, the anti-invariant lattice
of the Enriques involution, whose isotropic lines and planes are the zero- and
one-dimensional boundary components of the Enriques period space
(Dutour Sikiric--Hulek, arXiv:2302.01679, classify the arithmetic subgroups
acting on it).  The incidence between the two ranks is the Tits building.

Milestone 3, equivariant: the K3 lattice ``Lambda = 3U + 2E8(-1)`` with the
Enriques involution.  The invariant and anti-invariant decomposition, the
gluing subgroup and the index ``2^10`` are asserted in
``test_centralizer_gluing.py``; what is added here is the intersection of the
centralizer ``O(Lambda, iota)`` with the stabilizer of a polarization, which
is the group acting on the polarized period domain.
"""

from dzack_research.preamble.all import (
    Involutions,
    NamedLattices,
    centralizer,
    cusps,
    isometry_primitive_extension,
    predicate_subgroup,
    primitive_isotropic,
)


def test_milestone_one_the_E10_cusp_acts_on_its_reduction_lattice() -> None:
    lattice = NamedLattices.E10
    cusp = cusps(lattice)[0]
    line = cusp.representative()
    quotient = line.isotropic_quotient()
    assert quotient.module_rank() == 8

    descents = tuple(
        line.levi_quotient_action(generator)
        for generator in cusp.stabilizer_generators()
    )
    assert descents
    assert all(
        descent.domain() is quotient and descent.codomain() is quotient
        for descent in descents
    )

    # P_I -> O(E8) is onto, so the stabilizer generators cannot all descend to
    # the identity: a group acting trivially on the reduction could not cover
    # a group of order 696729600.
    assert any(
        any(
            descent(generator) != generator
            for generator in quotient.module_generators()
        )
        for descent in descents
    )


def test_milestone_two_a_plane_of_the_enriques_lattice_meets_a_line_cusp() -> None:
    lattice = NamedLattices.TEn
    line_cusps = cusps(lattice, 1)
    plane_cusps = cusps(lattice, 2)

    # Two lines whose reductions are not isometric cannot share a cusp, and
    # both reduction classes occur among the Sterk lines, so there are at
    # least two zero-dimensional cusps.
    assert line_cusps.cardinality() >= 2
    assert all(cusp.reduction_lattice().module_rank() == 10 for cusp in line_cusps)
    assert plane_cusps.cardinality() >= 1
    assert all(cusp.reduction_lattice().module_rank() == 8 for cusp in plane_cusps)

    plane = plane_cusps[0].representative()
    assert plane.module_rank() == 2
    embedded = plane.embedded_module_generators()
    first = embedded[plane.module_generating_set()[0]]
    assert first.q() == 0

    # A basis vector of a saturated plane spans a saturated line, so the
    # incidence of the Tits building is a statement about two cusps.
    line = primitive_isotropic(lattice, (first,))
    assert line.module_rank() == 1
    assert any(line in cusp for cusp in line_cusps)


def test_milestone_three_the_polarized_enriques_group_is_a_proper_subgroup() -> None:
    lattice = NamedLattices.LK3
    involution = Involutions.I_En
    extension = isometry_primitive_extension(involution)

    invariant = extension.invariant
    inclusion = invariant.inclusion()
    labels = invariant.module_generating_set()
    # A polarization is a non-isotropic vector of the invariant lattice; the
    # stabilizer construction is the same for either sign of its square.
    polarization = inclusion(
        invariant.module_generator(labels[0])
    ) + inclusion(invariant.module_generator(labels[1]))
    assert polarization.q() != 0
    assert involution(polarization) == polarization

    equivariant = centralizer(lattice.Aut(), involution)
    polarized = equivariant.intersection(
        predicate_subgroup(
            lattice.Aut(),
            lambda isometry: isometry(polarization) == polarization,
            f"g fixes {polarization}",
        )
    )

    negation = lattice.Aut()(
        {label: -lattice.module_generator(label) for label in lattice.module_generating_set()}
    )
    assert involution in equivariant
    assert negation in equivariant
    assert lattice.Aut().one() in polarized
    assert involution in polarized
    # -1 commutes with every isometry but moves the polarization, so the
    # polarized group is a proper subgroup of the centralizer.
    assert negation not in polarized
