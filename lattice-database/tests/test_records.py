"""The record commands compute every field that the Gram tensor determines, once, when they write a record, and refuse a record whose declared values are false."""

import shutil
from fractions import Fraction
from pathlib import Path

import frontmatter
import pytest
import yaml

from latticedb import corpus, nebe_sloane, records, root_systems, site
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


def test_derive_states_the_number_of_integral_overlattices_of_a3() -> None:
    # The discriminant group of A3 is Z/4 with a generator g, b(g, g) = 3/4: the form vanishes on 0 and on <2g>, and the lattices are A3 and I_3.
    record = records.derive(declared("A3", [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]))
    lattice = Lattice.model_validate(record)
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


def test_a_record_does_not_state_the_overlattice_count_above_the_subgroup_bound() -> None:
    # I_{1,0} + <-2>^8 has the discriminant group (Z/2)^8, which has more subgroups than the bound of the enumeration.
    record = records.derive(declared("<1> + <-2>^8", [[(1 if i == 0 else -2) if i == j else 0 for j in range(9)] for i in range(9)]))
    lattice = Lattice.model_validate(record)
    assert lattice.integral is not None
    assert lattice.integral.overlattice_count is None


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


def test_new_writes_a_valid_record_under_the_next_tag(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    declared = ("--name", "A2", "--latex", "A_2", "--family", "irreducible-root-lattice", "--alias", "Hexagonal lattice", "--reference", "A citation.")
    run("new", "--gram", "[[2, 1], [1, 2]]", *declared, "--prose", "The root lattice of type A2.", "--root", str(root))
    entries = corpus.load(root).entries
    assert [entry.lattice.tag for entry in entries] == ["0001", "0002"]
    lattice = entries[1].lattice
    assert (lattice.name, lattice.aliases, lattice.families) == ("A2", ("Hexagonal lattice",), ("irreducible-root-lattice",))
    assert [reference.citation for reference in lattice.references] == ["A citation."]
    assert lattice.definite is not None
    assert (lattice.definite.minimum, lattice.definite.kissing_number, lattice.definite.root_system) == (2, 6, ("A2",))
    assert entries[1].prose == "The root lattice of type A2."


def test_new_refuses_a_lattice_whose_components_are_those_of_a_record_of_the_corpus(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    with pytest.raises(SystemExit):
        run("new", "--gram", "[[1]]", "--name", "I_{1,0} again", "--latex", r"\mathrm{I}_{1,0}", "--root", str(root))
    assert [path.name for path in sorted((root / "lattices").glob("*.md"))] == ["0001.md"]


def test_new_refuses_a_twist_of_a_lattice(tmp_path: Path) -> None:
    # A1 = <1>(2), and the corpus records <1>.
    root = write_corpus(tmp_path)
    with pytest.raises(SystemExit):
        run("new", "--gram", "[[2]]", "--name", "A1", "--latex", "A_1", "--root", str(root))
    assert [path.name for path in sorted((root / "lattices").glob("*.md"))] == ["0001.md"]


def test_new_refuses_a_definite_lattice_that_is_isometric_to_a_record_of_the_corpus(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    run("new", "--gram", "[[2, 1], [1, 2]]", "--name", "A2", "--latex", "A_2", "--root", str(root))
    # A2 in the basis e_1, -e_2 has b(e_1, e_2) = -1.
    with pytest.raises(SystemExit):
        run("new", "--gram", "[[2, -1], [-1, 2]]", "--name", "A2 in another basis", "--latex", "A_2", "--root", str(root))
    assert [path.name for path in sorted((root / "lattices").glob("*.md"))] == ["0001.md", "0002.md"]


def test_new_refuses_a_family_that_families_yaml_does_not_list(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    with pytest.raises(SystemExit):
        run("new", "--gram", "[[2, 1], [1, 2]]", "--name", "A2", "--latex", "A_2", "--family", "hexagonal", "--root", str(root))
    assert [path.name for path in sorted((root / "lattices").glob("*.md"))] == ["0001.md"]


def test_nebe_sloane_writes_the_record_of_a_stored_entry_with_its_reference(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    (root / "sources" / "nebe_sloane").mkdir(parents=True)
    shutil.copy(REPOSITORY / "sources" / "nebe_sloane" / "K12.json", root / "sources" / "nebe_sloane" / "K12.json")
    run("nebe-sloane", "K12", "--name", "K12", "--latex", "K_{12}", "--alias", "Coxeter-Todd lattice", "--root", str(root))
    lattice = corpus.load(root).entries[1].lattice
    assert (lattice.name, lattice.aliases, lattice.families) == ("K12", ("K12", "Coxeter-Todd lattice"), ("nebe-sloane-catalogue",))
    assert (lattice.rank, lattice.determinant) == (12, 729)
    assert lattice.definite is not None
    assert (lattice.definite.minimum, lattice.definite.kissing_number) == (4, 756)
    assert [reference.url for reference in lattice.references] == ["https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/K12.html"]


def test_nebe_sloane_intakes_a_named_entry_from_the_union_archive(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    source = root / "sources" / "nebe_sloane"
    source.mkdir(parents=True)
    shutil.copy(REPOSITORY / "sources" / "nebe_sloane" / "union.gz", source / "union.gz")
    run("nebe-sloane", "BGF.2.2112", "--name", "BGF.2.2112", "--latex", r"\mathrm{BGF.2.2112}", "--root", str(root))
    lattice = corpus.load(root).entries[1].lattice
    assert (lattice.gram_tensor, lattice.determinant) == (((2, 1), (1, 12)), 23)
    assert lattice.definite is not None
    assert (lattice.definite.minimum, lattice.definite.kissing_number) == (2, 2)
    assert lattice.references[0].url == "https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz"
    assert nebe_sloane.stored_problems(root, corpus.load(root)) == []


def test_certify_derives_a_record_once_for_its_gram_tensor(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    path = root / "lattices" / "0001.md"
    document = frontmatter.loads(path.read_text())
    stale = dict(document.metadata)
    stale["signature"] = [0, 1]
    stale_text = "---\n" + yaml.safe_dump(stale, sort_keys=False) + "---\n\n" + document.content + "\n"
    path.write_text(stale_text)
    run("certify", "--tag", "0001", "--root", str(root))
    assert Lattice.model_validate(frontmatter.loads(path.read_text()).metadata).signature == (1, 0)
    # The certificate of the derived values names the Gram tensor, which has not changed: they are not computed again.
    path.write_text(stale_text)
    run("certify", "--tag", "0001", "--root", str(root))
    assert path.read_text() == stale_text


def test_morphism_appends_each_morphism_that_preserves_the_forms_up_to_its_scale_and_refuses_one_that_does_not(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    run("morphism", "0001", "0001", "--name", "identity", "--matrix", "[[1]]", "--prose", "Automorphisms of Z.", "--root", str(root))
    run("morphism", "0001", "0001", "--name", "negation", "--matrix", "[[-1]]", "--root", str(root))
    with pytest.raises(SystemExit):
        run("morphism", "0001", "0001", "--name", "doubling", "--matrix", "[[2]]", "--root", str(root))
    # x -> 2x takes b(x, x) = 1 to b(2x, 2x) = 4: a morphism Z(4) -> Z.
    run("morphism", "0001", "0001", "--name", "doubling", "--matrix", "[[2]]", "--scale", "4", "--root", str(root))
    (entry,) = corpus.load(root).morphisms
    found = [(morphism.name, morphism.matrix, morphism.scale) for morphism in entry.morphisms.morphisms]
    assert found == [("identity", ((1,),), 1), ("negation", ((-1,),), 1), ("doubling", ((2,),), 4)]
    assert entry.prose.strip() == "Automorphisms of Z."


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
