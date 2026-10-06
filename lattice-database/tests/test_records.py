"""The record commands compute Gram-determined fields and certify the values they write."""

import shutil
from fractions import Fraction
from pathlib import Path

import frontmatter
import pytest
import yaml

from latticedb import certificates, checks, corpus, records, root_systems, site
from latticedb.cli import app
from latticedb.model import Lattice, Morphism, Yaml

REPOSITORY = Path(__file__).resolve().parent.parent


def run(*tokens: str) -> None:
    """Run a command of `latticedb` in this process."""
    app(tokens, result_action="return_value")


def declared(name: str, gram_tensor: list[list[int | str]]) -> dict[str, Yaml]:
    """The fields of a record that a person writes."""
    return {
        "tag": "0001",
        "name": name,
        "latex": name,
        "aliases": [],
        "gram_tensor": gram_tensor,
        "families": [],
        "related": [],
        "references": [],
    }


def test_derive_computes_the_invariants_and_the_root_system_of_e8() -> None:
    record = records.derive(declared("E8", [list(row) for row in root_systems.simple_root_gram("E8")]))
    lattice = Lattice.model_validate(record)
    assert (lattice.rank, lattice.signature, lattice.determinant, lattice.definiteness) == (8, (8, 0), 1, "positive_definite")
    assert lattice.integral is not None
    assert (lattice.integral.parity, lattice.integral.discriminant_group) == ("even", ())
    assert lattice.definite is not None
    assert (lattice.definite.minimum, lattice.definite.kissing_number) == (2, 240)
    assert lattice.definite.theta_series == (1, 0, 240, 0, 2160, 0, 6720, 0, 17520)
    assert lattice.definite.root_system == ("E8",)
    assert lattice.definite.roots is not None
    assert [(component.type, component.scale) for component in lattice.definite.roots] == [("E8", 1)]
    assert lattice.is_root_lattice


def test_derive_leaves_exact_overlattice_count_to_enrichment() -> None:
    record = records.derive(
        declared("A3", [[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    )
    lattice = Lattice.model_validate(record)
    assert lattice.integral is not None
    assert lattice.integral.overlattice_count is None


def test_derive_preserves_an_enriched_overlattice_count() -> None:
    source = declared("A3", [[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    source["integral"] = {"overlattice_count": 2}
    lattice = Lattice.model_validate(records.derive(source))
    assert lattice.integral is not None
    assert lattice.integral.overlattice_count == 2


def test_derive_states_the_primes_of_bad_reduction_and_the_character_of_the_discriminant() -> None:
    # A2 has det 3, so D = -3 and Q(sqrt(-3)) has discriminant -3; Q(x) = 2x^2 - 2xy + 2y^2 is 0 modulo 2.
    # Modulo p != 2, 3, Q is a hyperbolic plane exactly when -3 is a square, so the cone has 2q - 1 or 1 points over F_q (theory/zeta.md).
    a2 = Lattice.model_validate(records.derive(declared("A2", [[2, -1], [-1, 2]])))
    assert a2.integral is not None
    assert (a2.integral.bad_reduction_primes, a2.integral.quadratic_character) == ((2, 3), -3)
    assert site.zeta_tex(a2, cone=True) == "\\frac{\\zeta^\\Sigma(s - 1)\\, L^\\Sigma(s - 1, \\chi_{-3})}{L^\\Sigma(s, \\chi_{-3})}"
    # <1> + <1> + <-1> has odd rank 3 and det -1, so D_n = (-1)^1 n (-1) = n.
    odd = Lattice.model_validate(records.derive(declared("I_{2,1}", [[1, 0, 0], [0, 1, 0], [0, 0, -1]])))
    assert odd.integral is not None
    assert (odd.integral.bad_reduction_primes, odd.integral.quadratic_character) == ((2,), None)
    assert site.zeta_tex(odd, cone=False) == "\\zeta^\\Sigma(s - 2)\\, L^\\Sigma(s - 1, \\chi_{n})"


def test_derive_states_the_roots_of_a_definite_lattice_whose_values_are_not_integers() -> None:
    # The dual of A2 has Gram tensor (1/3) [[2, 1], [1, 2]]: every nonzero vector of least norm 2/3 is a root, and they form G2 at scale 1/3.
    record = records.derive(declared("A2 dual", [["2/3", "1/3"], ["1/3", "2/3"]]))
    lattice = Lattice.model_validate(record)
    assert lattice.integral is None
    assert lattice.definite is not None
    assert (lattice.definite.minimum, lattice.definite.kissing_number, lattice.definite.theta_series) == (Fraction(2, 3), 6, None)
    assert lattice.definite.roots is not None
    assert [(component.type, component.scale) for component in lattice.definite.roots] == [("G2", Fraction(1, 3))]


def test_derive_decides_isotropy_and_the_root_sublattice_of_an_indefinite_lattice() -> None:
    # e_1 and e_2 are roots of norms 2 and -2, so L = Z Phi(L); -det(b) = 5 is not a square, so b is anisotropic.
    record = records.derive(declared("Indefinite binary", [[2, 1], [1, -2]]))
    lattice = Lattice.model_validate(record)
    assert lattice.definiteness == "indefinite"
    assert lattice.definite is None
    assert lattice.indefinite is not None
    assert not lattice.indefinite.isotropic
    assert lattice.root_span is not None
    assert lattice.is_root_lattice


def test_derive_leaves_the_root_sublattice_undecided_when_the_roots_it_finds_do_not_generate_the_lattice() -> None:
    # Phi(U) is (1, 1) and (1, -1) up to sign; it generates a sublattice of index 2, and the record proves that by hand.
    record = records.derive(declared("U", [[0, 1], [1, 0]]))
    lattice = Lattice.model_validate(record)
    assert lattice.indefinite is not None
    assert lattice.indefinite.isotropic
    assert lattice.root_span is None


def test_derive_keeps_the_fields_that_a_person_declares() -> None:
    record = declared("I_{1,0}", [[1]])
    record["integral"] = {"parity": "even", "genus_symbol": "I_{1,0}"}
    record["definite"] = {"minimum": 5, "automorphism_group_order": 2}
    derived = records.derive(record)
    lattice = Lattice.model_validate(derived)
    assert lattice.integral is not None
    assert (lattice.integral.parity, lattice.integral.genus_symbol) == ("odd", "I_{1,0}")
    assert lattice.definite is not None
    assert (lattice.definite.minimum, lattice.definite.automorphism_group_order) == (1, 2)


def write_corpus(directory: Path) -> Path:
    lattices = directory / "lattices"
    lattices.mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, directory / corpus.FAMILIES_FILE)
    (directory / corpus.RETIRED_FILE).write_text("{}\n")
    record = records.derive(declared("I_{1,0}", [[1]]))
    (lattices / "0001.md").write_text(records.record_text(record, "The lattice Z with the form b(x, y) = xy."))
    return directory


def test_new_writes_a_sparse_record_and_enrich_fills_derived_fields(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    declared = ("--name", "A2", "--latex", "A_2", "--family", "irreducible-root-lattice", "--alias", "Hexagonal lattice", "--reference", "A citation.")
    run("new", "--gram", "[[2, 1], [1, 2]]", *declared, "--prose", "The root lattice of type A2.", "--root", str(root))
    entries = corpus.load(root).entries
    assert [entry.lattice.tag for entry in entries] == ["0001", "0002"]
    lattice = entries[1].lattice
    assert (lattice.name, lattice.aliases, lattice.families) == ("A2", ("Hexagonal lattice",), ("irreducible-root-lattice",))
    assert [reference.citation for reference in lattice.references] == ["A citation."]
    assert (lattice.rank, lattice.signature, lattice.determinant, lattice.definite) == (None, None, None, None)
    assert entries[1].prose == "The root lattice of type A2."

    run("enrich", "--tag", "0002", "--root", str(root))
    lattice = corpus.load(root).entries[1].lattice
    assert lattice.definite is not None
    assert (lattice.definite.minimum, lattice.definite.kissing_number, lattice.definite.root_system) == (2, 6, ("A2",))


def test_verify_reports_a_new_card_that_is_a_twist(tmp_path: Path) -> None:
    # A1 = <1>(2), and the corpus records <1>.
    root = write_corpus(tmp_path)
    run("new", "--gram", "[[2]]", "--name", "A1", "--latex", "A_1", "--root", str(root))
    run("enrich", "--tag", "0002", "--root", str(root))
    assert any("M(2)" in problem for problem in checks.report(root))


def test_verify_reports_a_definite_card_isometric_to_an_existing_record(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    run("new", "--gram", "[[2, 1], [1, 2]]", "--name", "A2", "--latex", "A_2", "--root", str(root))
    # A2 in the basis e_1, -e_2 has b(e_1, e_2) = -1.
    run("new", "--gram", "[[2, -1], [-1, 2]]", "--name", "A2 in another basis", "--latex", "A_2", "--root", str(root))
    run("enrich", "--tag", "0002", "--tag", "0003", "--root", str(root))
    assert any("isometric to 0002" in problem for problem in checks.report(root))


def test_verify_reports_a_family_that_families_yaml_does_not_list(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    run("new", "--gram", "[[2, 1], [1, 2]]", "--name", "A2", "--latex", "A_2", "--family", "hexagonal", "--root", str(root))
    assert any("family 'hexagonal'" in problem for problem in checks.report(root))


def test_a_derive_certificate_binds_the_computed_values_for_its_gram_tensor(
    tmp_path: Path,
) -> None:
    root = write_corpus(tmp_path)
    path = root / "lattices" / "0001.md"
    run("enrich", "--tag", "0001", "--root", str(root))
    assert Lattice.model_validate(frontmatter.loads(path.read_text()).metadata).signature == (1, 0)
    stored = corpus.front_matter(frontmatter.load(str(path)))
    lattice = Lattice.model_validate(stored)
    cited_hash = certificates.certification_hash(
        "0001 derive", lattice, records.derived_projection(stored)
    )
    stored["certifications"] = {"derive": cited_hash}
    document = frontmatter.load(str(path))
    path.write_text(records.record_text(stored, document.content))
    certificates.save(
        root,
        {"0001 derive": certificates.Certificate(hash=cited_hash, by="test")},
    )
    assert not any("certificate" in problem for problem in checks.report(root))

    changed = frontmatter.loads(path.read_text())
    changed.metadata["signature"] = [0, 1]
    path.write_text(
        "---\n"
        + yaml.safe_dump(changed.metadata, sort_keys=False)
        + "---\n\n"
        + changed.content
        + "\n"
    )
    problems = checks.report(root)
    assert any("contradict their completed computation certificate" in problem for problem in problems)

    run("enrich", "--tag", "0001", "--root", str(root))
    repaired = path.read_text()
    assert Lattice.model_validate(frontmatter.loads(repaired).metadata).signature == (1, 0)
    assert not any("certificate" in problem for problem in checks.report(root))
    run("enrich", "--tag", "0001", "--root", str(root))
    assert path.read_text() == repaired


def test_morphism_authors_maps_and_verify_checks_the_form_equation(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    run("morphism", "0001", "0001", "--name", "identity", "--matrix", "[[1]]", "--prose", "Automorphisms of Z.", "--root", str(root))
    run("morphism", "0001", "0001", "--name", "negation", "--matrix", "[[-1]]", "--root", str(root))
    run("morphism", "0001", "0001", "--name", "doubling", "--matrix", "[[2]]", "--root", str(root))
    assert any(
        "doubling: the matrix does not preserve the forms" in problem
        for problem in checks.report(root)
    )

    scaled = tmp_path / "scaled"
    scaled.mkdir()
    scaled_root = write_corpus(scaled)
    # x -> 2x takes b(x, x) = 1 to b(2x, 2x) = 4: a morphism Z(4) -> Z.
    run("morphism", "0001", "0001", "--name", "doubling", "--matrix", "[[2]]", "--scale", "4", "--root", str(scaled_root))
    (entry,) = corpus.load(scaled_root).morphisms
    found = [(morphism.name, morphism.matrix, morphism.scale) for morphism in entry.morphisms.morphisms]
    assert found == [("doubling", ((2,),), 4)]


def gram(rows: list[list[int]]) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(Fraction(value) for value in row) for row in rows)


@pytest.mark.parametrize(
    ("rows", "expected"),
    [
        ([[0, 1], [2, 0]], ["differs from b(e_j, e_i)"]),
        # <1>(2), <1>(0) and <1>(-1).
        ([[2, 0], [0, 2]], ["M(2)"]),
        ([[0, 0], [0, 0]], ["zero form"]),
        ([[-1, 0], [0, -1]], ["M(-1)"]),
        # U + <2> is the twist by -1 of U + <-2>, whose signature (1, 2) has n_plus <= n_minus.
        ([[0, 1, 0], [1, 0, 0], [0, 0, 2]], ["M(-1)"]),
        ([[0, 1, 0], [1, 0, 0], [0, 0, -2]], []),
    ],
)
def test_a_gram_tensor_is_refused_when_it_is_not_symmetric_or_is_a_twist(rows: list[list[int]], expected: list[str]) -> None:
    found = records.gram_problems(gram(rows), ())
    assert len(found) == len(expected)
    assert all(fragment in problem for fragment, problem in zip(expected, found, strict=True))


@pytest.mark.parametrize(
    ("rows", "expected"),
    [
        # U(2), the row (2, 2, 0) of Nikulin's Table 1, is a record of the family.
        ([[0, 2], [2, 0]], []),
        # <1>(4) is not a twist by 2, and <1>(-2) is a twist by 2 against the sign convention.
        ([[4]], ["M(4)"]),
        ([[-2]], ["M(-1)"]),
    ],
)
def test_the_nikulin_family_admits_exactly_the_twists_by_2(rows: list[list[int]], expected: list[str]) -> None:
    found = records.gram_problems(gram(rows), (records.TWIST_FAMILY,))
    assert len(found) == len(expected)
    assert all(fragment in problem for fragment, problem in zip(expected, found, strict=True))


def admitted(name: str, rows: list[list[int]], **declared: Yaml) -> Lattice:
    return Lattice.model_validate(records.derive(declared_fields(name, rows) | declared))


def declared_fields(name: str, rows: list[list[int]]) -> dict[str, Yaml]:
    return declared(name, [list(row) for row in rows])


A3 = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]
D3 = [[2, 0, -1], [0, 2, -1], [-1, -1, 2]]


def test_a_definite_lattice_isometric_to_a_written_record_in_another_basis_is_refused() -> None:
    # A3 and D3 are isometric: both have determinant 4 and 12 roots of norm 2.
    written = {"0002": admitted("A3", A3).model_copy(update={"tag": "0002"})}
    (problem,) = records.admission_problems(admitted("D3", D3), written)
    assert "isometric to 0002" in problem
    # <1> + <3> and A2 have determinant 3; <1> + <3> has a vector of norm 1 and A2 does not.
    assert records.admission_problems(admitted("<1> + <3>", [[1, 0], [0, 3]]), {"0002": admitted("A2", [[2, 1], [1, 2]])}) == []


def test_an_odd_automorphism_group_order_is_refused() -> None:
    lattice = admitted("A2", [[2, 1], [1, 2]], definite={"automorphism_group_order": 13})
    (problem,) = records.admission_problems(lattice, {})
    assert "order is even" in problem


def u_with_root_span(span: dict[str, Yaml]) -> Lattice:
    return admitted("U", [[0, 1], [1, 0]], root_span=span)


RANK_ONE = {"0001": admitted("<1>", [[1]])}


def test_a_root_span_of_u_is_admitted_when_its_embedding_has_the_gram_tensor_of_the_sum_of_its_summands() -> None:
    span: dict[str, Yaml] = {"roots": [[1, 1], [1, -1]], "summands": [{"tag": "0001", "scale": 2}, {"tag": "0001", "scale": -2}], "embedding": [[1, 1], [1, -1]]}
    assert records.admission_problems(u_with_root_span(span), RANK_ONE) == []


@pytest.mark.parametrize(
    ("span", "expected"),
    [
        # b((1, 0), (1, 0)) = 0 in U, and (2, 2) is not primitive.
        ({"roots": [[1, 0]]}, ["is not a root of L"]),
        ({"roots": [[2, 2]]}, ["is not a root of L"]),
        # e and f generate U, and the roots (1, 1) and (1, -1) generate a sublattice of index 2; U is not <2> + <-2>.
        (
            {"roots": [[1, 1], [1, -1]], "summands": [{"tag": "0001", "scale": 2}, {"tag": "0001", "scale": -2}], "embedding": [[1, 0], [0, 1]]},
            ["not a basis", "orthogonal sum"],
        ),
        # <2> + <2> is positive definite, and the sublattice that (1, 1) and (1, -1) generate is <2> + <-2>.
        ({"roots": [[1, 1], [1, -1]], "summands": [{"tag": "0001", "scale": 2}, {"tag": "0001", "scale": 2}], "embedding": [[1, 1], [1, -1]]}, ["orthogonal sum"]),
        ({"roots": [[1, 1], [1, -1]], "summands": [{"tag": "0001", "scale": 2}, {"tag": "0008", "scale": -2}], "embedding": [[1, 1], [1, -1]]}, ["0008 is not in the corpus"]),
    ],
)
def test_a_root_span_of_u_is_refused_for_its_reasons(span: dict[str, Yaml], expected: list[str]) -> None:
    found = records.admission_problems(u_with_root_span(span), RANK_ONE)
    assert len(found) == len(expected)
    assert all(fragment in problem for fragment, problem in zip(expected, found, strict=True))


U = admitted("U", [[0, 1], [1, 0]])


def morphism(matrix: list[list[int]], row_subdivisions: list[int] | None = None, scale: int = 1) -> Morphism:
    return Morphism.model_validate({"name": "phi", "matrix": matrix, "scale": scale, "row_subdivisions": row_subdivisions or [], "column_subdivisions": []})


@pytest.mark.parametrize(
    ("matrix", "row_subdivisions", "expected"),
    [
        ([[1, 0], [0, 1]], [], []),
        ([[0, 1], [1, 0]], [], []),
        # e -> e, f -> -f is an isometry U(-1) -> U, so it is refused as a morphism U -> U.
        ([[1, 0], [0, -1]], [], ["is not 1 G_source"]),
        # The image of f is 2f, so b(e, f) = 1 goes to b(e, 2f) = 2.
        ([[1, 0], [0, 2]], [], ["does not preserve the forms"]),
        ([[1, 0]], [], ["2 rows and 2 columns"]),
        # e and f are not orthogonal, so the line between them does not cut U into orthogonal summands.
        ([[1, 0], [0, 1]], [1], ["row_subdivisions are not orthogonal summands of the target"]),
    ],
)
def test_a_morphism_of_u_is_refused_when_its_matrix_does_not_preserve_the_forms_or_a_line_cuts_u(
    matrix: list[list[int]], row_subdivisions: list[int], expected: list[str]
) -> None:
    found = records.morphism_problems(morphism(matrix, row_subdivisions), U, U)
    assert len(found) == len(expected)
    assert all(fragment in problem for fragment, problem in zip(expected, found, strict=True))


def test_a_morphism_with_a_scale_is_a_morphism_from_the_twist_of_its_source() -> None:
    # e -> e, f -> -f takes b(e, f) = 1 to b(e, -f) = -1, so it is a morphism U(-1) -> U.
    assert records.morphism_problems(morphism([[1, 0], [0, -1]], scale=-1), U, U) == []


def test_derive_computes_the_dual_gram_tensor() -> None:
    record = records.derive(declared("A2", [[2, -1], [-1, 2]]))
    assert record["dual_gram_tensor"] == [["2/3", "1/3"], ["1/3", "2/3"]]
    Lattice.model_validate(record)
