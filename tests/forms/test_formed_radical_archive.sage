r"""The radical of a degenerate lattice and the nondegenerate quotient."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_affine_A1_lattice_modulo_its_radical_is_the_A1_root_lattice() -> None:
    r"""``[[2, -2], [-2, 2]]`` has radical ``Z(e1 + e2)``, and the quotient is ``<2> = A1``.

    ``b(e1 + e2, e_i) = 0``; in the quotient the class of ``e1`` has norm 2.
    """
    affine = Lattices(ZZ)([[2, -2], [-2, 2]])
    e1, e2 = affine.basis()
    radical = affine.radical()
    (r,) = radical.basis()
    quotient = affine.radical_quotient()

    assert not affine.is_nondegenerate()
    assert radical.module_rank() == 1
    assert radical.inclusion()(r) in (e1 + e2, -e1 - e2)
    assert radical.inclusion().is_primitive()
    assert quotient.module_rank() == 1
    assert quotient.is_nondegenerate()
    assert quotient.is_isometric_to(Lattices(ZZ)([[2]]))


def test_nondegenerate_hyperbolic_plane_has_zero_radical() -> None:
    r"""``U`` is unimodular, so its radical is 0 and ``U / rad U = U``."""
    u = Lattices(ZZ)("U")

    assert u.radical().module_rank() == 0
    assert u.radical_quotient().is_isometric_to(u)


def test_rational_radical_quotient_retains_its_projection() -> None:
    r"""The quotient of the rank-three form with a one-dimensional radical has rank two."""
    lattice = Lattices(QQ)([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    quotient = lattice.radical_quotient()
    projection = lattice.radical_quotient_projection()

    assert lattice.radical().module_rank() == 1
    assert quotient.module_rank() == 2
    assert projection.domain() is lattice
    assert projection.codomain() is quotient
    assert projection.module_morphism().domain() is lattice.unformed_module()
    assert projection.module_morphism().codomain() is quotient.unformed_module()
    assert projection.preserves_forms() is True
    assert projection(lattice.module_generator(1)) != quotient.zero()
    assert quotient.b(
        projection(lattice.module_generator(1)),
        projection(lattice.module_generator(2)),
    ) == lattice.b(lattice.module_generator(1), lattice.module_generator(2)) == 1
    radical = lattice.radical()
    for label in radical.module_generating_set():
        assert projection(radical.inclusion()(radical.module_generator(label))) == quotient.zero()


def test_rational_formed_module_radical_quotient_retains_its_projection() -> None:
    r"""The generic formed-module quotient retains its map after basis re-presentation."""
    module = QQ ^ 3
    form = module.bilinear_forms(QQ)([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    formed = FormModules(QQ)(form)
    quotient = formed.radical_quotient()
    projection = formed.radical_quotient_projection()

    assert formed.radical().module_rank() == 1
    assert quotient.module_rank() == 2
    assert quotient.unformed_module().module_rank() == 2
    assert quotient.unformed_module() in FramedFreeModules(QQ)
    assert quotient.form().module() is quotient.unformed_module()
    assert quotient.gram_tensor().tensor_shape() == (2, 2)
    assert projection.domain() is formed
    assert projection.codomain() is quotient
    assert projection.preserves_forms() is True
    basis_map = quotient._preamble_radical_quotient_basis_map
    canonical_projection = quotient._preamble_radical_quotient_projection
    source_module = formed.unformed_module()
    for label in source_module.module_generating_set():
        generator = source_module.module_generator(label)
        assert basis_map(projection.module_morphism()(generator)) == canonical_projection(generator)
    assert quotient.b(
        projection(formed.module_generator(1)),
        projection(formed.module_generator(2)),
    ) == formed.b(formed.module_generator(1), formed.module_generator(2)) == 1
    for label in formed.radical().module_generating_set():
        assert projection(formed.radical().inclusion()(formed.radical().module_generator(label))) == quotient.zero()
    lattice_quotient = Lattices(QQ)(quotient)
    assert lattice_quotient.module_rank() == 2
    assert lattice_quotient.unformed_module().module_rank() == 2
    assert lattice_quotient.unformed_module() is quotient.unformed_module()
    assert lattice_quotient.gram_tensor().tensor_shape() == (2, 2)
    assert lattice_quotient.is_isometric_to(Lattices(QQ)([[0, 1], [1, 0]]))
