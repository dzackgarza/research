r"""Non-unimodular cusp gluing can restrict the Levi image."""

from dzack_research.preamble.all import ZZ, Lattices, finite_ordered_set


def _glued_divisibility_two_cusp():
    r"""Return the cusp obtained from ``U(2) + A1^4`` by diagonal order-two glue."""
    lattice = Lattices(ZZ)(
        [
            [-2, 1, -1, -1, -1, -1],
            [1, 0, 0, 0, 0, 0],
            [-1, 0, -2, 0, 0, 0],
            [-1, 0, 0, -2, 0, 0],
            [-1, 0, 0, 0, -2, 0],
            [-1, 0, 0, 0, 0, -2],
        ]
    )
    g, _f, r1, r2, r3, r4 = lattice.module_generators()
    isotropic = 2 * g - r1 - r2 - r3 - r4
    line = lattice.primitive_isotropic_subobject(isotropic)
    return lattice, isotropic, line


def test_glued_cusp_has_divisibility_two_and_D4_type_reduction() -> None:
    lattice, isotropic, line = _glued_divisibility_two_cusp()
    reduction = line.isotropic_reduction()

    assert isotropic.q() == 0
    assert isotropic.is_primitive()
    assert isotropic.div() == 2
    assert lattice.determinant().abs() == 16
    assert reduction.module_rank() == 4
    assert reduction.is_even()
    assert reduction.determinant().abs() == 4


def test_nonunimodular_gluing_restricts_the_definite_Levi_image() -> None:
    _lattice, _isotropic, line = _glued_divisibility_two_cusp()
    reduction = line.isotropic_reduction()
    image = reduction.levi_image()

    assert image.supergroup() is reduction.O()
    assert image.cardinality() < reduction.O().cardinality()
    assert image.cardinality() > 1
    assert all(generator in image for generator in reduction.levi_image_generators())


def test_every_reported_Levi_generator_is_the_descent_of_a_parabolic_generator() -> None:
    lattice, _isotropic, line = _glued_divisibility_two_cusp()
    reduction = line.isotropic_reduction()
    levi = reduction.levi_action()
    parabolic_generators = lattice.O().isotropic_stabilizer_generators(line)
    descended = finite_ordered_set(
        [levi(generator) for generator in parabolic_generators]
    )

    assert reduction.levi_image_generators() == descended
    assert all(generator in reduction.O() for generator in descended)


def test_every_element_of_the_Levi_image_retains_an_actual_parabolic_lift() -> None:
    _lattice, _isotropic, line = _glued_divisibility_two_cusp()
    reduction = line.isotropic_reduction()
    levi = reduction.levi_action()

    for isometry in reduction.levi_image():
        lifted = reduction.levi_lift(isometry)
        assert lifted is not None
        assert lifted in reduction.parabolic_subgroup()
        assert levi(lifted) == isometry


def test_gluing_obstruction_is_an_actual_missing_Levi_lift() -> None:
    _lattice, _isotropic, line = _glued_divisibility_two_cusp()
    reduction = line.isotropic_reduction()
    image = reduction.levi_image()
    excluded = next(isometry for isometry in reduction.O() if isometry not in image)

    assert reduction.levi_lift(excluded) is None


def test_divisibility_two_cusp_retains_its_rational_Witt_decomposition() -> None:
    lattice, isotropic, line = _glued_divisibility_two_cusp()
    reduction = line.isotropic_reduction()
    witt = reduction.rational_witt_decomposition()

    assert witt.integral_line() is line
    assert witt.integral_reduction() is reduction
    assert witt.integral_perpendicular() is reduction.orthogonal_complement()
    assert witt.divisibility() == 2
    assert lattice.b(isotropic, witt.bezout_partner()) == 2

    rational = witt.rational_lattice()
    e = witt.isotropic_vector()
    f = witt.dual_isotropic_vector()
    assert rational.q(e) == 0
    assert rational.q(f) == 0
    assert rational.b(e, f) == 1
    assert witt.hyperbolic_plane().module_rank() == 2
    assert witt.orthogonal_summand().module_rank() == reduction.module_rank()


def test_pointwise_parabolic_sequence_has_the_unipotent_kernel_and_actual_Levi_image() -> None:
    _lattice, _isotropic, line = _glued_divisibility_two_cusp()
    reduction = line.isotropic_reduction()
    sequence = reduction.parabolic_levi_exact_sequence()

    assert sequence.source() is reduction.pointwise_parabolic_subgroup()
    assert sequence.kernel() is reduction.unipotent_kernel()
    assert sequence.target() is reduction.pointwise_levi_image()
    assert sequence.kernel().supergroup() is sequence.source()

    projection = sequence.projection()
    for target in sequence.target():
        lifted = sequence.lift(target)
        assert lifted is not None
        assert lifted in sequence.source()
        assert projection(lifted) == target


def test_pointwise_Levi_kernel_is_exactly_the_unipotent_kernel() -> None:
    _lattice, _isotropic, line = _glued_divisibility_two_cusp()
    reduction = line.isotropic_reduction()
    sequence = reduction.parabolic_levi_exact_sequence()
    identity = sequence.target().one()

    for generator in reduction.isotropic_embedding().codomain().O().isotropic_stabilizer_generators(line):
        if generator in sequence.source():
            assert (generator in sequence.kernel()) == (sequence.projection()(generator) == identity)
