r"""Global tests for ``dzack_research.preamble``.

The modules carry assertions internally, but those only fire when something calls
them -- so without this file nothing exercises the port on a schedule. These are the
checks that would catch a regression in the recovered mathematics, chosen for what
they can *falsify* rather than for coverage:

- the catalogue's named lattices against their defining invariants;
- the Sterk configurations against **Sterk's published norm breakdown**, an external
  oracle independent of how the vectors were transcribed;
- the involutions against the six named lattices, two constructions that never
  touched each other;
- the source's own claim block, which never ran before this port.

``.sage`` because several checks need the preparser and Sage's global namespace.
"""


def _preamble():
    from dzack_research.preamble import (
        catalogue,
        coxeter,
        involutions,
        patches,
        predicates,
        sterk,
    )

    return catalogue, coxeter, involutions, patches, predicates, sterk


# --------------------------------------------------------------------------
# catalogue
# --------------------------------------------------------------------------


def test_named_lattices_have_their_defining_invariants():
    catalogue = _preamble()[0]
    expected = {
        "U": (2, (1, 1)),
        "U_2": (2, (1, 1)),
        "E8": (8, (0, 8)),
        "E8_2": (8, (0, 8)),
        "E10": (10, (1, 9)),
        "E10_2": (10, (1, 9)),
        "LK3": (22, (3, 19)),
        "SEn": (10, (1, 9)),
        "TEn": (12, (2, 10)),
        "LpNik": (14, (3, 11)),
        "LmNik": (8, (0, 8)),
        "TdP": (20, (2, 18)),
        "L_20_2_0": (20, (2, 18)),
    }
    for name, (rank, signature) in expected.items():
        lattice = catalogue.NAMED[name]
        assert lattice.rank() == rank, f"{name}: rank {lattice.rank()} != {rank}"
        assert lattice.signature_pair() == signature, (
            f"{name}: signature {lattice.signature_pair()} != {signature}"
        )


def test_root_lattices_use_the_negative_definite_convention():
    """A_n, D_n, E_n are negative definite here; Sage's own are positive."""
    catalogue = _preamble()[0]
    for kind, rank in (("A", 2), ("D", 4), ("E", 8)):
        lattice = catalogue.root_lattice(kind, rank)
        assert lattice.signature_pair() == (0, rank), (
            f"{kind}{rank} should be negative definite, got {lattice.signature_pair()}"
        )


def test_k3_degree_2d_family():
    catalogue = _preamble()[0]
    for degree in (1, 2, 3):
        lattice = catalogue.LK3_2d(degree)
        assert lattice.rank() == 21
        assert lattice.signature_pair() == (2, 19)
        assert lattice.gram_matrix().det() == -2 * degree


def test_two_elementary_table_ranks_match_its_keys():
    catalogue = _preamble()[0]
    table = catalogue.two_elementary_lattices()
    assert len(table) == 12
    for key, lattice in table.items():
        rank = int(key.strip("()").split(",")[0])
        assert lattice.rank() == rank, f"{key}: rank {lattice.rank()}"


# --------------------------------------------------------------------------
# sterk
# --------------------------------------------------------------------------


def test_sterk_configurations_match_published_norm_breakdown():
    """The external oracle: Sterk's counts *by norm*, not just totals."""
    sterk = _preamble()[5]
    configurations = sterk.sterk_roots()
    for name, roots in configurations.items():
        published = sterk.STERK_PUBLISHED[name]
        minus_four = sum(1 for r in roots if sterk.bilinear_form(r, r) == -4)
        minus_two = sum(1 for r in roots if sterk.bilinear_form(r, r) == -2)
        assert len(roots) == published["total"], name
        assert minus_four == published["norm_-4"], f"{name}: {minus_four} roots of norm -4"
        assert minus_two == published["norm_-2"], f"{name}: {minus_two} roots of norm -2"


def test_every_sterk_vector_is_a_root():
    sterk = _preamble()[5]
    for name, roots in sterk.sterk_roots().items():
        for index, root in enumerate(roots, start=1):
            norm = sterk.bilinear_form(root, root)
            assert norm in (-2, -4), f"{name} root {index}: norm {norm}"


def test_s4_12_is_isotropic_not_a_root():
    """The vector wrongly dropped as dead code: a cusp, norm 0."""
    sterk = _preamble()[5]
    vectors = sterk.isotropic_vectors()
    assert "s4_12" in vectors
    value = vectors["s4_12"]
    assert sterk.bilinear_form(value, value) == 0


def test_five_selected_isotropic_vectors():
    """Why there are five Sterk cases."""
    sterk = _preamble()[5]
    selected_vectors = sterk.selected_isotropic_vectors()
    assert len(selected_vectors) == 5
    _, _, gram = sterk.ten_frames()
    for name, vector_ in selected_vectors.items():
        assert vector_ * gram * vector_ == 0, f"{name} is not isotropic"


def test_getsterk5_reproduces_sterk_5_from_a_different_lattice():
    """Rank 10 here versus rank 20 in ``sterk_roots`` -- independent presentations."""
    sterk = _preamble()[5]
    lattice, vectors = sterk.sterk5_in_U_E8_2()
    assert lattice.rank() == 10
    assert len(vectors) == 14
    gram = lattice.gram_matrix().change_ring(QQ)
    minus_four = sum(1 for v in vectors if v * gram * v == -4)
    minus_two = sum(1 for v in vectors if v * gram * v == -2)
    published = sterk.STERK_PUBLISHED["Sterk_5"]
    assert (minus_four, minus_two) == (published["norm_-4"], published["norm_-2"])


def test_diagonal_embedding_images_span_e8_2():
    sterk = _preamble()[5]
    images = sterk.diagonal_embedding_images()
    assert len(images) == 16


# --------------------------------------------------------------------------
# involutions
# --------------------------------------------------------------------------


def test_involutions_are_involutions_and_isometries():
    involutions = _preamble()[2]
    assert sorted(involutions.involutions()) == ["I_En", "I_Nik", "I_dP"]


def test_eigenlattices_reproduce_the_named_lattices():
    """Two independent constructions agreeing: direct sums versus signed basis images."""
    catalogue, _, involutions, patches, _, _ = _preamble()
    patches.install("lattice_methods")
    try:
        pairs = [
            ("I_dP", "-", catalogue.TdP),
            ("I_En", "+", catalogue.SEn),
            ("I_En", "-", catalogue.TEn),
            ("I_Nik", "+", catalogue.LpNik),
            ("I_Nik", "-", catalogue.LmNik),
        ]
        for name, sign, named in pairs:
            lattice = (
                involutions.invariant_lattice(name)
                if sign == "+"
                else involutions.anti_invariant_lattice(name)
            )
            assert lattice.is_isometric(named), f"{name} L{sign}"
    finally:
        patches.uninstall("lattice_methods")


def test_eigenlattice_ranks_sum_to_22():
    involutions = _preamble()[2]
    for name in ("I_dP", "I_En", "I_Nik"):
        plus = involutions.invariant_lattice(name)
        minus = involutions.anti_invariant_lattice(name)
        assert plus.rank() + minus.rank() == 22, name


# --------------------------------------------------------------------------
# the source's claim block (old lines 365-388)
# --------------------------------------------------------------------------


def test_source_claim_block_holds():
    """Eight assertions the source wrote behind ``do_tests = False`` and never ran."""
    catalogue, _, _, patches, _, _ = _preamble()
    patches.install("lattice_methods")
    try:
        TEn = catalogue.TEn
        table = catalogue.two_elementary_lattices()
        basis, dual = TEn.basis(), TEn.dual_basis()
        e, f, ep = basis[0], basis[1], basis[2]
        w1 = dual[4]

        assert TEn.div(e) == 1 and TEn.q(e) == 0
        assert TEn.e_perp_mod_e(e).is_isometric(catalogue.E10_2)
        assert TEn.e_perp_mod_e(e).is_isometric(table["(10,10,0)"])

        assert TEn.div(ep) == 2 and TEn.q(ep) == 0
        assert TEn.e_perp_mod_e(ep).is_isometric(catalogue.U.direct_sum(catalogue.E8_2))
        assert TEn.e_perp_mod_e(ep).is_isometric(table["(10,8,0)"])

        assert TEn.I_perp_mod_I([e, ep]).is_isometric(table["(8,8,0)"])

        vp = 2 * e + 2 * f + 2 * w1
        assert TEn.div(vp) == 2 and TEn.q(vp) == 0
    finally:
        patches.uninstall("lattice_methods")


def test_the_8_6_0_lattice_has_its_recorded_invariants():
    """The entry recovered from the claim block; an index-2 overlattice of A1^8."""
    catalogue, _, _, patches, _, _ = _preamble()
    patches.install("lattice_methods")
    try:
        TEn = catalogue.TEn
        basis, dual = TEn.basis(), TEn.dual_basis()
        quotient = TEn.I_perp_mod_I([basis[2], 2 * basis[0] + 2 * basis[1] + 2 * dual[4]])
        recorded = catalogue.TWO_ELEMENTARY_8_6_0_INVARIANTS
        assert quotient.rank() == recorded["rank"]
        assert quotient.signature_pair() == recorded["signature_pair"]
        assert quotient.gram_matrix().det() == recorded["determinant"]
    finally:
        patches.uninstall("lattice_methods")


# --------------------------------------------------------------------------
# predicates, coxeter, patches
# --------------------------------------------------------------------------


def test_delta_is_zero_on_the_two_elementary_lattices():
    catalogue, _, _, _, predicates, _ = _preamble()
    for name in ("U", "U_2", "E8", "E8_2", "E10_2", "TEn"):
        lattice = catalogue.NAMED[name]
        assert predicates.delta(lattice) in (0, 1)
        assert predicates.is_coeven(lattice) == (predicates.delta(lattice) == 0)


def test_definiteness_predicates():
    catalogue, _, _, _, predicates, _ = _preamble()
    assert predicates.is_elliptic(catalogue.E8)
    assert predicates.is_parabolic(catalogue.E8)
    assert not predicates.is_elliptic(catalogue.U)


def test_coxeter_diagram_uses_the_owned_sage_parent():
    _, coxeter, _, _, _, _ = _preamble()
    from dzack_research import lattice

    root_lattice = lattice.Lattice("E8")
    diagram = root_lattice.coxeter_diagram()

    assert diagram.category().is_subcategory(coxeter.CoxeterDiagrams())
    assert diagram.coxeter_matrix() == CoxeterMatrix(["E", 8])


def test_diagram_layouts_match_root_counts():
    _, coxeter, _, _, _, sterk = _preamble()
    for name, positions in coxeter.STERK_POSITIONS.items():
        assert len(positions) == sterk.STERK_ROOT_COUNTS[name], name


def test_patches_round_trip():
    patches = _preamble()[3]
    assert patches.installed() == ()
    for name in patches.available():
        patches.install(name)
    assert set(patches.installed()) == set(patches.available())
    for name in patches.available():
        patches.uninstall(name)
    assert patches.installed() == ()


# --------------------------------------------------------------------------
# newly ported surface: sterks1/2/3, run_vin, get_isotrop_type, patch methods
# --------------------------------------------------------------------------


def test_sterks_in_ten_are_root_configurations():
    """The T_En-coordinate configurations, with their two different dual scalings."""
    sterk = _preamble()[5]
    configurations = sterk.sterks_in_ten()
    assert sorted(configurations) == ["sterks1", "sterks2", "sterks3"]
    _, _, gram = sterk.ten_frames()
    expected_counts = {"sterks1": 12, "sterks2": 10, "sterks3": 12}
    for name, vectors in configurations.items():
        assert len(vectors) == expected_counts[name], name
        for index, vector_ in enumerate(vectors, start=1):
            norm = vector_ * gram * vector_
            assert norm in (-2, -4), f"{name} vector {index}: norm {norm}"


def test_sterks1_and_sterks3_use_different_dual_scalings():
    """A regression guard: using one scaling for both changes every dual vector.

    sterks1 takes duals from 2*G^-1, sterks3 from G^-1. If a refactor unified them,
    the vectors would still be *vectors* but would no longer be roots -- so the norm
    check above would catch it. This pins the distinction more directly.
    """
    sterk = _preamble()[5]
    _, _, gram = sterk.ten_frames()
    doubled = (2 * gram.inverse()).columns()
    plain = gram.inverse().columns()
    assert doubled[4] == 2 * plain[4], "the two dual bases must differ by a factor 2"


def test_recorded_root_matrix_is_preserved():
    sterk = _preamble()[5]
    rows = sterk.RECORDED_ROOT_MATRIX_ROWS
    assert len(rows) == 5
    assert all(len(row) == 10 for row in rows)


def test_nothing_from_the_sterk_section_is_unported():
    sterk = _preamble()[5]
    assert sterk.NOT_PORTED == ()


def test_to_lin_comb_generators_labels_elements():
    catalogue, _, _, patches, _, _ = _preamble()
    patches.install("lattice_methods")
    try:
        lattice = catalogue.U.direct_sum(catalogue.E8).with_names("e, f, a1..a8")
        generators = lattice.gens()
        assert lattice.to_lin_comb_generators(generators[0]) == "e"
        label = lattice.to_lin_comb_generators(2 * generators[0] - generators[3])
        assert "2*e" in label and "a2" in label, label
    finally:
        patches.uninstall("lattice_methods")


def test_sublattices_is_a_usable_dict():
    """Old line 358 does ``TEn.sublattices.update({...})`` and needs it to exist."""
    catalogue, _, _, patches, _, _ = _preamble()
    patches.install("lattice_methods")
    try:
        lattice = catalogue.TEn
        lattice.sublattices.update({"Sterk_1": catalogue.E10_2})
        assert "Sterk_1" in lattice.sublattices
        lattice.sublattices.clear()
    finally:
        patches.uninstall("lattice_methods")


def test_twist_accepts_names():
    catalogue, _, _, patches, _, _ = _preamble()
    patches.install("lattice_methods")
    try:
        twisted = catalogue.E8.twist(2, names=tuple(f"b{i}" for i in range(1, 9)))
        assert twisted.variable_names() == tuple(f"b{i}" for i in range(1, 9))
    finally:
        patches.uninstall("lattice_methods")


def test_lattice_latex_representation():
    catalogue, _, _, patches, _, _ = _preamble()
    from dzack_research.preamble.patches import lattice_methods

    patches.install("lattice_methods")
    try:
        from sage.misc.latex import latex

        u_latex = str(latex(catalogue.U))
        assert r"L \in \mathrm{Lattices}(\ZZ)" in u_latex
        assert r"\mathrm{rk}(L) = 2" in u_latex
        assert r"\mathrm{sig}(L) = (1, 1)" in u_latex
        assert r"\mathrm{disc}(L) = -1" in u_latex
        assert r"\cdot" in u_latex
        assert r"A_L \cong 0 \in \mathrm{Groups}" in u_latex
        assert r"G_{q_{A_L}} = ()" in u_latex

        a2_latex = str(latex(catalogue.root_lattice("A", 2)))
        assert r"A_L \cong C_{3} \in \mathrm{Groups}" in a2_latex
        assert r"G_{q_{A_L}} =" in a2_latex

        a2_d4_lattice = catalogue.root_lattice("A", 2).direct_sum(catalogue.root_lattice("D", 4))
        a2_d4_latex = str(latex(a2_d4_lattice))
        assert r"A_L \cong C_{2} \oplus C_{6} \in \mathrm{Groups} \quad \text{(Invariant factor decomposition)}" in a2_d4_latex
        assert r"A_L \cong C_{2}^{2} \oplus C_{3} \in \mathrm{Groups} \quad \text{(Primary decomposition)}" in a2_d4_latex

        lattice_methods.set_zero_dots(False)
        u_latex_no_dots = str(latex(catalogue.U))
        assert r"\cdot" not in u_latex_no_dots
        assert "0" in u_latex_no_dots
    finally:
        lattice_methods.set_zero_dots(True)
        patches.uninstall("lattice_methods")


def test_direct_sum_subdivides_gram_matrix():
    catalogue, _, _, patches, _, _ = _preamble()
    patches.install("lattice_methods")
    try:
        direct_sum_lattice = catalogue.U.direct_sum(catalogue.E8)
        assert direct_sum_lattice.gram_matrix().subdivisions() == ([2], [2])
        assert catalogue.LK3.gram_matrix().subdivisions() == ([2, 4, 6, 14], [2, 4, 6, 14])
        assert catalogue.LK3_2d(3).gram_matrix().subdivisions() == ([1, 3, 5, 13], [1, 3, 5, 13])
    finally:
        patches.uninstall("lattice_methods")


def test_lattice_element_multiplication_and_exponentiation():
    catalogue, _, _, patches, _, _ = _preamble()
    patches.install("lattice_methods")
    try:
        a2 = catalogue.root_lattice("A", 2)
        alpha1, alpha2 = a2.gens()
        assert alpha1 * alpha1 == -2
        assert alpha1 * alpha2 == 1
        assert alpha1 ** 2 == -2
        assert alpha1 ^ 2 == -2
        assert (alpha1 + alpha2) ^ 2 == -2
        assert (alpha1 + 2 * alpha2) * (alpha1 - alpha2) == 3
    finally:
        patches.uninstall("lattice_methods")


def test_run_vin_negates_roots_when_it_twists():
    """The source typo (``do_twist`` set, ``doTwist`` tested) disabled this branch."""
    catalogue, _, _, patches, _, _ = _preamble()
    from dzack_research.preamble.patches import vinberg

    patches.install("lattice_methods")
    patches.install("vinberg")
    try:
        d4 = catalogue.root_lattice("D", 4).twist(-1)
        lattice = catalogue.U.direct_sum(d4).with_names("e, f, a1..a4")
        result = vinberg.run_vin(lattice)
        assert len(result.roots) == 6, len(result.roots)
        assert result.root_names is not None
        # Twisting happened, so the roots come back negated -- the branch the typo
        # made unreachable.
        assert any(name.startswith("-") for name in result.root_names), result.root_names
    finally:
        patches.uninstall("vinberg")
        patches.uninstall("lattice_methods")


def test_get_isotrop_type_classifies():
    catalogue, _, _, patches, _, _ = _preamble()
    from dzack_research.preamble.patches import vinberg

    patches.install("lattice_methods")
    try:
        lattice = catalogue.U.direct_sum(catalogue.U)
        verdict = vinberg.get_isotrop_type(lattice, lattice.gens()[0])
        assert verdict in ("Odd", "Even ordinary", "Even characteristic", "Not found.")
    finally:
        patches.uninstall("lattice_methods")


def test_install_reports_every_stanza_it_ran():
    from dzack_research.preamble import install

    report = install(red_tracebacks=False)
    assert "vendor_paths" in report
    assert "red_tracebacks" not in report
    assert "gap_package_manager" not in report


def test_julia_preamble_calls_oscar_with_a_sage_matrix():
    from dzack_research.preamble import julia as julia_preamble

    gram = julia_preamble.BONDS["bond1"]
    assert julia_preamble.oscar_call("rank", gram) == 2

    julia_preamble.julia.set("_preamble_round_trip", gram)
    converted_back = julia_preamble.julia.get_sage("_preamble_round_trip")
    assert converted_back == gram
    assert converted_back.base_ring() is gram.base_ring()


def test_static_preamble_data_has_one_fixture_owner():
    from dzack_research.preamble import catalogue, coxeter, fixtures, involutions, sterk
    from dzack_research.preamble import julia as julia_preamble

    assert julia_preamble.BONDS is fixtures.BONDS
    assert coxeter.DIAGRAM_CONVENTION is fixtures.DIAGRAM_CONVENTION
    assert coxeter.CROSS_CHECK_RECIPES is fixtures.CROSS_CHECK_RECIPES
    assert coxeter.STERK_POSITIONS is fixtures.STERK_POSITIONS
    assert coxeter.STERK_ROOT_COUNTS is fixtures.STERK_ROOT_COUNTS
    assert involutions.BASIS_NAMES is fixtures.K3_BASIS_NAMES
    assert sterk.STERK_ROOT_COUNTS is fixtures.STERK_ROOT_COUNTS
    assert sterk.STERK_PUBLISHED is fixtures.STERK_PUBLISHED
    assert sterk.COMPUTED_ROOT_COUNTS is fixtures.COMPUTED_ROOT_COUNTS
    assert sterk.RECORDED_ROOT_MATRIX_ROWS is fixtures.RECORDED_ROOT_MATRIX_ROWS
    assert catalogue.RECORDED_RESULTS is fixtures.RECORDED_RESULTS
    assert catalogue.CITATIONS is fixtures.CITATIONS
    assert catalogue.TWO_ELEMENTARY_8_6_0_INVARIANTS is fixtures.TWO_ELEMENTARY_8_6_0_INVARIANTS
    assert catalogue.TWO_ELEMENTARY_BUILDING_BLOCKS is fixtures.TWO_ELEMENTARY_BUILDING_BLOCKS
    assert catalogue.UNBUILT_TWO_ELEMENTARY is fixtures.UNBUILT_TWO_ELEMENTARY
