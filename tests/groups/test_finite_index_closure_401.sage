r"""Issue 401 finite-index and subgroup-image closure specimens."""

from dzack_research.preamble.all import *  # noqa: F401,F403
from dzack_research.preamble.categories.group.groups import _matrix_group_element_matrix


def test_mod_two_kernel_of_sl2z_has_index_six_and_schreier_generators():
    group = Groups.SL(2, ZZ)
    target = Groups.SL(2, GF(2))
    engine = target._engine_group()
    reduction = group.Mor(target)(
        lambda g: target._from_engine(engine([
            [engine.base_ring()(int(entry)) for entry in row]
            for row in _matrix_group_element_matrix(group, g).rows()
        ]))
    )
    kernel = reduction.kernel()
    generators = kernel.schreier_generators()
    assert kernel.index() == 6
    assert target.cardinality() == 6
    assert all(reduction(g) == target.one() for g in generators)
    # Schreier's lemma asserts that this returned family generates the kernel.
    assert len(generators) == 12


def test_indefinite_stable_orthogonal_kernel_with_supplied_generators():
    lattice = Lattices(ZZ)([[0, 2], [2, 0]])
    group = lattice.Aut()
    exchange = group([[0, 1], [1, 0]])
    minus_id = group([[-1, 0], [0, -1]])
    stable = lattice.stable_orthogonal_group()
    rho = lattice.discriminant_representation()
    generators = stable.schreier_generators(generators=(exchange, minus_id))
    assert generators
    assert all(rho(g) == rho.codomain().one() for g in generators)
    assert stable.image_under(rho, ambient_generators=(exchange, minus_id)).cardinality() == 1


def test_a2_discriminant_image_from_orthogonal_generators():
    lattice = Lattices(ZZ)("A2")
    rho = lattice.discriminant_representation()
    group = lattice.Aut().select_group_resolution()
    image = group.subgroup(tuple(group.group_generators())).image_under(rho)
    assert image.cardinality() == rho.codomain().cardinality() == 2


def test_unresolved_predicate_image_names_missing_inverse_algorithm():
    subset = Sets().condition_set(ZZ, lambda x: x*x == ZZ(4))
    square = Sets().Mor(ZZ, ZZ)(lambda x: x*x)
    image = Sets().image_set(square, subset)
    try:
        ZZ(4) in image
    except AssertionError as error:
        assert "source is infinite and no inverse on the image was given" in str(error)
    else:
        raise AssertionError("membership in a predicate image was decided without an algorithm")
