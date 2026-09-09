r"""Archive reconciliation for ADE base log-pair vocabulary."""

from dzack_research.preamble.all import ADELogPair, QQ


def test_archived_ade_type_names_read_the_same_retained_family_data() -> None:
    pair = ADELogPair("A", 3, QQ, variant=("long", "short"))

    assert pair.letter() == pair.dynkin_letter() == "A"
    assert pair.rank() == pair.dynkin_rank() == 3
    assert tuple(pair.variant()) == tuple(pair.dynkin_variant())
    assert not pair.is_affine()
    assert pair.is_affine() is pair.is_affine_type()


def test_archived_polygon_and_blue_divisor_names_are_the_live_owned_objects() -> None:
    pair = ADELogPair("D", 4, QQ)

    assert pair.p_star() is pair.distinguished_point()
    assert pair.polarizing_polytope() is pair.polygon()
    assert pair.blue_line_divisor() == pair.blue_divisor()
    assert pair.log_scheme().polarizing_polytope() is pair.polarizing_polytope()


def test_archived_affine_predicate_keeps_the_affine_family_distinct() -> None:
    affine = ADELogPair("A", 3, QQ, affine=True)
    finite = ADELogPair("A", 3, QQ)

    assert affine.is_affine()
    assert not finite.is_affine()
    assert affine.p_star() != finite.p_star()


def test_archived_base_role_names_identify_the_actual_toric_base_pair() -> None:
    pair = ADELogPair("E", 6, QQ)

    assert pair.scheme() is pair.log_scheme()
    assert pair.toric_scheme() is pair.log_scheme()
    assert pair.base() is pair
    assert pair.is_base()
    assert not pair.is_cover()
    assert pair.codimension_in_toric_scheme() == 0
