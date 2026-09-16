r"""Archive reconciliation for ADE base log-pair vocabulary."""

from dzack_research.preamble.all import ADELogPairs, QQ

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/schemes/ade_surfaces.sage",
    "live_owner": "src/dzack_research/preamble/categories/schemes/ade_surfaces.py",
    "owner_overrides": {
        "LogPairs": "src/dzack_research/preamble/categories/schemes/log_pairs.py",
        "LogPairs.super_categories": "src/dzack_research/preamble/categories/schemes/log_pairs.py",
        "LogPairs.ParentMethods": "src/dzack_research/preamble/categories/schemes/log_pairs.py",
        "LogPairs.ParentMethods.is_log_pair": "src/dzack_research/preamble/categories/schemes/log_pairs.py",
        "ToricLogPairs": "src/dzack_research/preamble/categories/schemes/log_pairs.py",
        "ToricLogPairs.super_categories": "src/dzack_research/preamble/categories/schemes/log_pairs.py",
        "ToricLogPairs.ParentMethods": "src/dzack_research/preamble/categories/schemes/log_pairs.py",
        "ToricLogPairs.ParentMethods.scheme": "src/dzack_research/preamble/categories/schemes/log_pairs.py",
        "ToricLogPairs.ParentMethods.boundary_divisor": "src/dzack_research/preamble/categories/schemes/log_pairs.py",
        "ToricLogPair": "src/dzack_research/preamble/categories/schemes/toric/toric_schemes.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_archived_ade_type_names_read_the_same_retained_family_data() -> None:
    pair = ADELogPairs(QQ)("A", 3, variant=("long", "short"))

    assert pair.letter() == pair.dynkin_letter() == "A"
    assert pair.rank() == pair.dynkin_rank() == 3
    assert tuple(pair.variant()) == tuple(pair.dynkin_variant())
    assert not pair.is_affine()
    assert pair.is_affine() is pair.is_affine_type()


def test_archived_polygon_and_blue_divisor_names_are_the_live_owned_objects() -> None:
    pair = ADELogPairs(QQ)("D", 4)

    assert pair.p_star() is pair.distinguished_point()
    assert pair.polarizing_polytope() is pair.polygon()
    assert pair.vertices() is pair.vertices()
    assert pair.vertices() == pair.polygon().vertices()
    assert pair.vertices().cardinality() == pair.polygon().vertices().cardinality()
    assert all(vertex.parent() is pair.polygon().ambient_lattice() for vertex in pair.vertices())
    assert pair.blue_line_divisor() == pair.blue_divisor()
    assert pair.log_scheme().polarizing_polytope() is pair.polarizing_polytope()


def test_archived_affine_predicate_keeps_the_affine_family_distinct() -> None:
    affine = ADELogPairs(QQ)("A", 3, affine=True)
    finite = ADELogPairs(QQ)("A", 3)

    assert affine.is_affine()
    assert not finite.is_affine()
    assert affine.p_star() != finite.p_star()


def test_archived_base_role_names_identify_the_actual_toric_base_pair() -> None:
    pair = ADELogPairs(QQ)("E", 6)

    assert pair.scheme() is pair.log_scheme()
    assert pair.toric_scheme() is pair.log_scheme()
    assert pair.base() is pair
    assert pair.is_base()
    assert not pair.is_cover()
    assert pair.codimension_in_toric_scheme() == 0


def test_archived_dynkin_diagram_is_the_owned_finite_coxeter_diagram() -> None:
    pair = ADELogPairs(QQ)("E", 6)

    assert pair.dynkin_diagram() is pair.coxeter_diagram()
    assert pair.dynkin_diagram().cardinality() == 6
    assert pair.dynkin_diagram().is_elliptic()


def test_archived_affine_dynkin_diagram_uses_the_affine_cartan_type() -> None:
    pair = ADELogPairs(QQ)("A", 3, affine=True)
    diagram = pair.dynkin_diagram()

    assert diagram is pair.coxeter_diagram()
    assert diagram.cardinality() == 4
    assert diagram.is_parabolic()


def test_archived_integral_polygon_invariants_are_an_owned_labelled_family() -> None:
    pair = ADELogPairs(QQ)("D", 4)
    invariants = pair.integral_invariants()

    assert invariants is pair.integral_invariants()
    assert tuple(invariants.index_set()) == (
        "dimension",
        "volume",
        "normalized_volume",
        "n_integral_points",
        "n_interior_points",
        "n_boundary_points",
    )
    assert invariants["dimension"].parent() is pair.dynkin_rank().parent()
    assert invariants["volume"].parent() is QQ
    assert invariants["normalized_volume"].parent() is pair.dynkin_rank().parent()
    assert (
        invariants["n_boundary_points"] + invariants["n_interior_points"]
        == invariants["n_integral_points"]
    )
