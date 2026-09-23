r"""Parabolic subgroups of primitive isotropic subobjects, and Eichler transvections.

The specimen is the even unimodular Lorentzian lattice ``E10 = U + E8``, for
which ``e^perp/e`` is ``E8`` (Conway--Sloane, *Sphere Packings, Lattices and
Groups*, ch. 26: ``II_{1,9} = U + E8``), so the cusp of the isotropic line
``Z e`` has ``E8`` as its reduction lattice.
"""


from dzack_research.preamble.all import (
    NamedLattices,
    PrimitiveIsotropicSubobjects,
    ZZ,
)


def _lorentzian_line():
    lattice = NamedLattices.E10
    generators = lattice.module_generators()
    return lattice, generators, lattice.primitive_isotropic_subobject(generators[0])


def _acts_as_identity(restriction, module) -> bool:
    return all(
        restriction(generator) == generator for generator in module.module_generators()
    )


def test_the_isotropic_line_of_E10_reduces_to_E8() -> None:
    lattice, _generators, line = _lorentzian_line()

    assert line in PrimitiveIsotropicSubobjects(ZZ)
    assert line.is_totally_isotropic()
    assert line.is_primitive()
    assert line.module_rank() == 1
    assert line.ambient_lattice() is lattice

    assert line.isotropic_perpendicular().module_rank() == 9
    assert line.isotropic_quotient().module_rank() == 8
    reduction = line.isotropic_reduction()
    assert reduction.module_rank() == 8
    assert reduction.is_isometric(NamedLattices.E8)


def test_eichler_transvections_lie_in_the_unipotent_radical() -> None:
    lattice, generators, line = _lorentzian_line()
    isotropic, hyperbolic_partner = generators[0], generators[1]
    root = generators[2]
    assert lattice.b(isotropic, root) == 0
    assert root.q() == -2

    transvection = line.eichler_transvection(root)
    assert transvection.parent() is lattice.Aut()
    assert transvection != lattice.Aut().one()
    assert transvection(isotropic) == isotropic
    assert transvection(hyperbolic_partner) == hyperbolic_partner + isotropic - root
    assert transvection(hyperbolic_partner).q() == hyperbolic_partner.q()

    assert line.stabilizes(transvection)
    assert transvection in line.parabolic_subgroup()
    assert transvection in line.unipotent_radical()
    assert line.acts_trivially_on_isotropic_reduction(transvection)
    assert _acts_as_identity(line.levi_restriction(transvection), line)


def test_the_eichler_transvections_of_a_line_form_an_abelian_group() -> None:
    lattice, generators, line = _lorentzian_line()
    isotropic = generators[0]
    first, second = generators[2], generators[3]

    left = line.eichler_transvection(first)
    right = line.eichler_transvection(second)
    assert left * right == line.eichler_transvection(first + second)
    assert left * right == right * left
    assert ~left == line.eichler_transvection(-first)
    assert line.eichler_transvection(isotropic) == lattice.Aut().one()
    assert line.eichler_transvection(lattice.zero()) == lattice.Aut().one()

    family = line.unipotent_group_generators()
    assert family.index_set() is line.isotropic_perpendicular().module_generating_set()
    assert all(transvection in line.unipotent_radical() for transvection in family)






def test_the_two_isotropic_lines_of_two_hyperbolic_planes_are_one_orbit() -> None:
    lattice = NamedLattices.U + NamedLattices.U
    generators = lattice.module_generators()
    first = lattice.primitive_isotropic_subobject(generators[0])
    second = lattice.primitive_isotropic_subobject(generators[2])

    assert first.isotropic_reduction().is_isometric(NamedLattices.U)
    assert second.isotropic_reduction().is_isometric(NamedLattices.U)

    witness = first.transporter_witness_to(second)
    assert witness is not None
    assert second.inclusion().is_in_image(witness(generators[0]))
    assert first.is_equivalent_to(second)


