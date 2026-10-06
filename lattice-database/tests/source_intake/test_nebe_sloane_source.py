"""Source-intake checks for the Nebe--Sloane catalogue and union archive.

These tests exercise archived-source parsing and source-to-card transcription.
They are provenance/importer checks, not mathematical certification.
"""

import shutil
from pathlib import Path

from latticedb import corpus, nebe_sloane, records
from latticedb.model import Lattice, Yaml

REPOSITORY = Path(__file__).resolve().parent.parent.parent


def _declared(name: str, gram_tensor: list[list[int | str]]) -> dict[str, Yaml]:
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


def _corpus(directory: Path) -> Path:
    lattices = directory / "lattices"
    lattices.mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, directory / corpus.FAMILIES_FILE)
    (directory / corpus.RETIRED_FILE).write_text("{}\n")
    record = _declared("I_{1,0}", [[1]]) | {"rank": 1}
    (lattices / "0001.md").write_text(records.record_text(record, ""))
    return directory


def test_nebe_sloane_writes_the_record_of_a_stored_entry_with_its_reference(
    tmp_path: Path,
) -> None:
    root = _corpus(tmp_path)
    source = root / "sources" / "nebe_sloane"
    source.mkdir(parents=True)
    shutil.copy(REPOSITORY / "sources" / "nebe_sloane" / "K12.json", source / "K12.json")
    entry = nebe_sloane.stored(source, "K12")
    declared, prose = nebe_sloane.record(
        entry, "K12", "K_{12}", ("Coxeter-Todd lattice",), ()
    )
    lattice = Lattice.model_validate(declared | {"tag": "0002"})
    assert (lattice.name, lattice.aliases, lattice.families) == (
        "K12",
        ("K12", "Coxeter-Todd lattice"),
        ("nebe-sloane-catalogue",),
    )
    assert (lattice.rank, lattice.determinant) == (12, 729)
    assert lattice.definite is not None
    assert (lattice.definite.minimum, lattice.definite.kissing_number) == (4, 756)
    assert [reference.url for reference in lattice.references] == [
        "https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/K12.html"
    ]
    assert "GRAM" in prose


def test_nebe_sloane_intakes_a_named_entry_from_the_union_archive(
    tmp_path: Path,
) -> None:
    root = _corpus(tmp_path)
    source = root / "sources" / "nebe_sloane"
    source.mkdir(parents=True)
    shutil.copy(REPOSITORY / "sources" / "nebe_sloane" / "union.gz", source / "union.gz")
    entry = nebe_sloane.archive_entry(source / "union.gz", "BGF.2.2112")
    (source / "BGF.2.2112.json").write_text(entry.model_dump_json() + "\n")
    declared, prose = nebe_sloane.record(
        entry, "BGF.2.2112", r"\mathrm{BGF.2.2112}", (), ()
    )
    authored = declared | {"tag": "0002"}
    (root / "lattices" / "0002.md").write_text(records.record_text(authored, prose))
    lattice = corpus.load(root).entries[1].lattice
    assert (lattice.gram_tensor, lattice.determinant) == (((2, 1), (1, 12)), 23)
    assert lattice.definite is not None
    assert (lattice.definite.minimum, lattice.definite.kissing_number) == (2, 2)
    assert (
        lattice.references[0].url
        == "https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz"
    )
    assert nebe_sloane.stored_problems(root, corpus.load(root)) == []


def test_nebe_sloane_accepts_an_indefinite_entry_without_definite_invariants() -> None:
    entry = nebe_sloane.Entry(
        name="IndefiniteSpecimen",
        title="IndefiniteSpecimen",
        url="https://example.org/IndefiniteSpecimen",
        dimension=2,
        determinant=-5,
        minimal_norm=None,
        kissing_number=None,
        references=(),
        gram_tensor=((2, 1), (1, -2)),
    )
    declared, _ = nebe_sloane.record(entry, "IndefiniteSpecimen", "S", (), ())
    lattice = Lattice.model_validate(declared | {"tag": "0002"})
    assert (lattice.rank, lattice.determinant, lattice.definite) == (2, -5, None)


def test_nebe_sloane_reads_the_full_matrix_of_shimada_86() -> None:
    entry = nebe_sloane.archive_entry(
        REPOSITORY / "sources" / "nebe_sloane" / "union.gz", "Shimada_86"
    )
    assert (
        entry.dimension,
        entry.determinant,
        entry.minimal_norm,
        entry.kissing_number,
    ) == (86, 196608, 8, 109421928)
    rings = session_ring_objects()
    formed = rings["ZZ"].free_module(entry.dimension).equip_bilinear_form(
        rings["QQ"], entry.gram_tensor
    )
    signature = formed.signature_pair()
    assert (int(signature.first()), int(signature.second()), 0) == (86, 0, 0)
    assert int(formed.determinant()) == entry.determinant
