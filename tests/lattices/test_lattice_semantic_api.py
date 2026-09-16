from dzack_research.preamble.all import ZZ, Lattices


def test_metric_map_and_linear_dual_are_the_live_correlation_data() -> None:
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()

    assert lattice.linear_dual() is lattice.dual_module()
    assert lattice.metric_map().domain() is lattice
    assert lattice.metric_map().codomain() is lattice.linear_dual()
    assert lattice.metric_map()(e) == e.to_covector()
    assert lattice.metric_map()(f) == f.to_covector()


def test_signature_and_selected_basis_gram_matrix_are_owner_level_operations() -> None:
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()

    assert lattice.signature() == lattice.signature_pair()
    changed = lattice.gram_matrix((e + f, e - f))
    assert changed[0, 0] == 2
    assert changed[0, 1] == 0
    assert changed[1, 0] == 0
    assert changed[1, 1] == -2


def test_primitive_sublattice_rebuilds_the_restricted_lattice_after_saturation() -> None:
    lattice = Lattices(ZZ)("U")
    e, _f = lattice.module_generators()

    nonsaturated = lattice.sublattice_from((2 * e,))
    primitive = lattice.primitive_sublattice_from((2 * e,))

    assert not nonsaturated.is_primitive()
    assert primitive.is_primitive()
    assert primitive.inclusion().codomain() is lattice
    assert primitive.module_rank() == 1
    assert primitive.gram_matrix()[0, 0] == 0


def test_perp_is_the_same_owned_orthogonal_subobject_from_both_endpoints() -> None:
    lattice = Lattices(ZZ)("U")
    e, _f = lattice.module_generators()
    line = lattice.primitive_sublattice_from((e,))

    from_line = line.perp()
    from_ambient = lattice.perp(line)

    assert from_line.inclusion().codomain() is lattice
    assert from_ambient.inclusion().codomain() is lattice
    assert from_line.module_rank() == from_ambient.module_rank() == 1
    assert lattice.b(
        line.inclusion()(line.module_generator(0)),
        from_ambient.inclusion()(from_ambient.module_generator(0)),
    ) == 0


def test_lattice_vector_divisor_and_primitive_discriminant_class_use_live_form_data() -> None:
    lattice = Lattices(ZZ)([[2, 0], [0, -6]])
    e, f = lattice.module_generators()

    assert e.divisor() == 2
    assert f.divisor() == 6
    assert e.discriminant_class() == e.divided_discriminant_class()

    try:
        (2 * e).discriminant_class()
    except ValueError:
        pass
    else:
        raise AssertionError("the primitive discriminant class is not defined on a nonprimitive vector")


def test_sublattice_semantic_accessors_retain_the_actual_embedding_and_form() -> None:
    lattice = Lattices(ZZ)("U")
    e, _f = lattice.module_generators()
    line = lattice.sublattice_from((2 * e,))

    assert line.ambient_lattice() is lattice
    assert line.inclusion().codomain() is lattice
    assert line.rank() == line.module_rank() == 1
    assert line.lattice_basis() == line.module_generators()
    assert not line.is_primitive()

    saturated = line.saturation()
    assert saturated.ambient_lattice() is lattice
    assert saturated.is_primitive()
    assert saturated.rank() == 1


def test_isotropic_reduction_exposes_its_defining_inclusion_and_live_reduction_data() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("U")
    e = lattice.module_generator(0)
    isotropic = lattice.primitive_sublattice_from((e,))
    reduction = isotropic.isotropic_reduction()

    assert reduction.isotropic_sublattice() is isotropic
    assert reduction.inclusion() is reduction.isotropic_inclusion()
    assert reduction.inclusion().domain() is isotropic
    assert reduction.inclusion().codomain() is reduction.orthogonal_complement()
    assert reduction.quotient_lattice() is reduction
    assert reduction.projection().domain() is reduction.orthogonal_complement()
    assert reduction.projection().codomain() is reduction
