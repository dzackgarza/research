"""The record commands compute every field that the Gram tensor determines, and the corpus is their output."""

import shutil
from fractions import Fraction
from pathlib import Path

import frontmatter
import pytest
import yaml
from latticedb import corpus, records, root_systems
from latticedb.cli import app
from latticedb.model import Lattice, Yaml
from pydantic import ValidationError

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
        "provenance": {"source": "Test record."},
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


def test_a_record_does_not_state_the_overlattice_count_above_the_subgroup_bound() -> None:
    # I_{1,0} + <-2>^8 has the discriminant group (Z/2)^8, which has more subgroups than the bound of the enumeration.
    record = records.derive(declared("<1> + <-2>^8", [[(1 if i == 0 else -2) if i == j else 0 for j in range(9)] for i in range(9)]))
    lattice = Lattice.model_validate(record)
    assert lattice.integral is not None
    assert lattice.integral.overlattice_count is None
    integral = record["integral"]
    assert isinstance(integral, dict)
    with pytest.raises(ValidationError) as raised:
        Lattice.model_validate(record | {"integral": integral | {"overlattice_count": 2981}})
    assert {error["type"] for error in raised.value.errors()} == {"overlattice_count_not_decided"}


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
    record["provenance"] = {"source": "Test record.", "computed_with": "by hand"}
    derived = records.derive(record)
    lattice = Lattice.model_validate(derived)
    assert lattice.integral is not None
    assert (lattice.integral.parity, lattice.integral.genus_symbol) == ("odd", "I_{1,0}")
    assert lattice.definite is not None
    assert (lattice.definite.minimum, lattice.definite.automorphism_group_order) == (1, 2)
    assert lattice.provenance.computed_with == "by hand"


def test_derive_reproduces_every_record_of_the_corpus() -> None:
    for path in sorted((REPOSITORY / "lattices").glob("*.md")):
        text = path.read_text()
        document = frontmatter.loads(text)
        assert records.record_text(records.derive(document.metadata), document.content) == text, path


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
    declared = ("--name", "A2", "--latex", "A_2", "--source", "Test record.", "--family", "root-lattice", "--alias", "Hexagonal lattice", "--reference", "A citation.")
    run("new", "--gram", "[[2, 1], [1, 2]]", *declared, "--prose", "The root lattice of type A2.", "--root", str(root))
    entries = corpus.load(root).entries
    assert [entry.lattice.tag for entry in entries] == ["0001", "0002"]
    lattice = entries[1].lattice
    assert (lattice.name, lattice.aliases, lattice.families) == ("A2", ("Hexagonal lattice",), ("root-lattice",))
    assert [reference.citation for reference in lattice.references] == ["A citation."]
    assert lattice.definite is not None
    assert (lattice.definite.minimum, lattice.definite.kissing_number, lattice.definite.root_system) == (2, 6, ("A2",))
    assert entries[1].prose == "The root lattice of type A2."


def test_new_refuses_a_lattice_whose_components_are_those_of_a_record_of_the_corpus(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    with pytest.raises(SystemExit):
        run("new", "--gram", "[[1]]", "--name", "I_{1,0} again", "--latex", r"\mathrm{I}_{1,0}", "--source", "Test record.", "--root", str(root))
    assert [path.name for path in sorted((root / "lattices").glob("*.md"))] == ["0001.md"]


def test_new_refuses_a_twist_of_a_lattice(tmp_path: Path) -> None:
    # A1 = <1>(2), and the corpus records <1>.
    root = write_corpus(tmp_path)
    with pytest.raises(SystemExit):
        run("new", "--gram", "[[2]]", "--name", "A1", "--latex", "A_1", "--source", "Test record.", "--root", str(root))
    assert [path.name for path in sorted((root / "lattices").glob("*.md"))] == ["0001.md"]


def test_new_refuses_a_definite_lattice_that_is_isometric_to_a_record_of_the_corpus(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    run("new", "--gram", "[[2, 1], [1, 2]]", "--name", "A2", "--latex", "A_2", "--source", "Test record.", "--root", str(root))
    # A2 in the basis e_1, -e_2 has b(e_1, e_2) = -1.
    with pytest.raises(SystemExit):
        run("new", "--gram", "[[2, -1], [-1, 2]]", "--name", "A2 in another basis", "--latex", "A_2", "--source", "Test record.", "--root", str(root))
    assert [path.name for path in sorted((root / "lattices").glob("*.md"))] == ["0001.md", "0002.md"]


def test_new_refuses_a_family_that_families_yaml_does_not_list(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    with pytest.raises(SystemExit):
        run("new", "--gram", "[[2, 1], [1, 2]]", "--name", "A2", "--latex", "A_2", "--source", "Test record.", "--family", "hexagonal", "--root", str(root))
    assert [path.name for path in sorted((root / "lattices").glob("*.md"))] == ["0001.md"]


def test_nebe_sloane_writes_the_record_of_a_stored_entry_with_its_reference_and_provenance(tmp_path: Path) -> None:
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
    assert lattice.provenance.url == "https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/K12.html"


def test_derive_rewrites_exactly_the_records_whose_computed_fields_changed(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    path = root / "lattices" / "0001.md"
    document = frontmatter.loads(path.read_text())
    stale = dict(document.metadata)
    stale["signature"] = [0, 1]
    path.write_text("---\n" + yaml.safe_dump(stale, sort_keys=False) + "---\n\n" + document.content + "\n")
    run("derive", "--root", str(root))
    assert Lattice.model_validate(frontmatter.loads(path.read_text()).metadata).signature == (1, 0)
    text = path.read_text()
    run("derive", "--root", str(root))
    assert path.read_text() == text
