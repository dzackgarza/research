"""The record commands serialize preamble-owned values and certificate metadata."""

import shutil
from fractions import Fraction
from pathlib import Path

import frontmatter
import yaml

from latticedb import certificates, checks, corpus, records, site
from latticedb.cli import app
from latticedb.model import Lattice, Yaml

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


def test_derive_serializes_preamble_owned_root_and_theta_data() -> None:
    e8_source = frontmatter.load(str(REPOSITORY / "lattices" / "0094.md")).metadata
    record = records.derive(declared("E8", e8_source["gram_tensor"]))
    lattice = Lattice.model_validate(record)
    assert all(
        value is not None
        for value in (lattice.rank, lattice.signature, lattice.determinant, lattice.definiteness)
    )
    assert lattice.integral is not None
    assert lattice.definite is not None
    assert lattice.definite.minimum is not None
    assert lattice.definite.kissing_number is not None
    assert lattice.definite.theta_series is not None
    assert lattice.definite.root_system == ("E8",)
    assert lattice.definite.roots is not None
    assert lattice.root_sublattice is not None


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


def test_derive_serializes_preamble_reduction_fields_when_available() -> None:
    lattice = Lattice.model_validate(
        records.derive(declared("A2", [[2, -1], [-1, 2]]))
    )
    assert lattice.integral is not None
    assert lattice.integral.bad_reduction_primes is not None
    assert lattice.integral.quadratic_character is not None
    assert site.zeta_tex(lattice, cone=True) == "\\frac{\\zeta^\\Sigma(s - 1)\\, L^\\Sigma(s - 1, \\chi_{-3})}{L^\\Sigma(s, \\chi_{-3})}"


def test_derive_computes_rational_definite_invariants_through_the_integral_reflection_model() -> None:
    record = records.derive(declared("A2 dual", [["2/3", "1/3"], ["1/3", "2/3"]]))
    lattice = Lattice.model_validate(record)
    assert lattice.integral is None
    assert lattice.definite is not None
    assert lattice.definite.minimum == Fraction(2, 3)
    assert lattice.definite.kissing_number == 6
    assert lattice.definite.theta_series is None
    assert lattice.definite.roots is not None


def test_derive_serializes_indefinite_root_data_through_the_preamble() -> None:
    authored = declared("Indefinite binary", [[2, 1], [1, -2]])
    authored["root_span"] = {"roots": [[1, 0], [0, 1]]}
    record = records.derive(authored)
    lattice = Lattice.model_validate(record)
    assert lattice.definite is None
    assert lattice.indefinite is not None
    assert lattice.root_span is not None
    assert lattice.root_sublattice is not None
    assert lattice.root_sublattice.invariant_factors == (1, 1)
    assert lattice.root_sublattice.norms == (Fraction(-2), Fraction(2))


def test_derive_leaves_root_data_absent_for_an_indefinite_lattice_without_authored_root_data() -> None:
    record = records.derive(declared("U", [[0, 1], [1, 0]]))
    lattice = Lattice.model_validate(record)
    assert lattice.indefinite is not None
    assert lattice.root_span is None
    assert lattice.root_sublattice is None


def test_derive_keeps_the_fields_that_a_person_declares() -> None:
    record = declared("I_{1,0}", [[1]])
    record["integral"] = {"parity": "even", "genus_symbol": "I_{1,0}"}
    record["definite"] = {"minimum": 5, "automorphism_group_order": 2}
    derived = records.derive(record)
    lattice = Lattice.model_validate(derived)
    assert lattice.integral is not None
    assert lattice.integral.genus_symbol == "I_{1,0}"
    assert lattice.definite is not None
    assert lattice.definite.automorphism_group_order == 2


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
    assert lattice.definite.minimum is not None
    assert lattice.definite.kissing_number is not None
    assert lattice.definite.root_system == ("A2",)


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
    original_signature = Lattice.model_validate(
        frontmatter.loads(path.read_text()).metadata
    ).signature
    assert original_signature is not None
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
    assert Lattice.model_validate(frontmatter.loads(repaired).metadata).signature == original_signature
    assert not any("certificate" in problem for problem in checks.report(root))
    run("enrich", "--tag", "0001", "--root", str(root))
    assert path.read_text() == repaired


def test_morphism_authors_stored_map_data(tmp_path: Path) -> None:
    root = write_corpus(tmp_path)
    run("morphism", "0001", "0001", "--name", "identity", "--matrix", "[[1]]", "--root", str(root))
    run("morphism", "0001", "0001", "--name", "negation", "--matrix", "[[-1]]", "--root", str(root))
    run("morphism", "0001", "0001", "--name", "doubling", "--matrix", "[[2]]", "--root", str(root))
    (entry,) = corpus.load(root).entries
    assert [(morphism.name, morphism.matrix, morphism.scale) for morphism in entry.lattice.morphisms] == [
        ("identity", ((1,),), 1),
        ("negation", ((-1,),), 1),
        ("doubling", ((2,),), 1),
    ]

    scaled = tmp_path / "scaled"
    scaled.mkdir()
    scaled_root = write_corpus(scaled)
    # x -> 2x takes b(x, x) = 1 to b(2x, 2x) = 4: a morphism Z(4) -> Z.
    run("morphism", "0001", "0001", "--name", "doubling", "--matrix", "[[2]]", "--scale", "4", "--root", str(scaled_root))
    (entry,) = corpus.load(scaled_root).entries
    found = [(morphism.name, morphism.matrix, morphism.scale) for morphism in entry.lattice.morphisms]
    assert found == [("doubling", ((2,),), 4)]


def test_derive_computes_the_dual_gram_tensor() -> None:
    record = records.derive(declared("A2", [[2, -1], [-1, 2]]))
    assert record.get("dual_gram_tensor") is not None
    Lattice.model_validate(record)


def test_admission_recomputes_authored_reduction_invariants_through_the_preamble() -> None:
    record = records.derive(declared("A2", [[2, -1], [-1, 2]]))
    integral = dict(record["integral"])
    integral["level"] = 17
    integral["bad_reduction_primes"] = [17]
    integral["quadratic_character"] = 17
    lattice = Lattice.model_validate(record | {"integral": integral})
    problems = records.local_admission_problems(lattice)
    assert any("integral.level" in problem for problem in problems)
    assert any("integral.bad_reduction_primes" in problem for problem in problems)
    assert any("integral.quadratic_character" in problem for problem in problems)


def test_admission_recomputes_authored_perfectness_through_the_preamble() -> None:
    record = records.derive(declared("A2", [[2, -1], [-1, 2]]))
    definite = dict(record["definite"])
    definite["minimal_vectors"] = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
        [1, 1],
        [-1, -1],
    ]
    definite["perfect"] = False
    lattice = Lattice.model_validate(record | {"definite": definite})
    assert any(
        "definite.perfect" in problem
        for problem in records.local_admission_problems(lattice)
    )


def test_admission_detects_a_definite_duplicate_in_another_basis() -> None:
    first_source = declared("A2 first basis", [[2, -1], [-1, 2]])
    first_source["tag"] = "0001"
    second_source = declared("A2 second basis", [[2, 1], [1, 2]])
    second_source["tag"] = "0002"
    first = Lattice.model_validate(records.derive(first_source))
    second = Lattice.model_validate(records.derive(second_source))
    problems = records.definite_isometry_problems((first, second))
    assert list(problems) == ["0002"]
    assert any("isometric to 0001" in problem for problem in problems["0002"])


def test_isometric_twists_of_different_scales_are_not_duplicates() -> None:
    sources = []
    for tag, gram_tensor in (
        ("0001", [[2, -1], [-1, 2]]),
        ("0002", [[2, 1], [1, 2]]),
        ("0003", [["1/2"]]),
        ("0004", [["1/3"]]),
    ):
        source = declared(f"card {tag}", gram_tensor)
        source["tag"] = tag
        sources.append(Lattice.model_validate(records.derive(source)))
    problems = records.definite_isometry_problems(tuple(sources))
    assert list(problems) == ["0002"]
