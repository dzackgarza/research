"""The published bulk tables present exact lattice forms in distinct conventions."""

from fractions import Fraction
from pathlib import Path

from flint import fmpz_mat

from latticedb import brandt_intrau, nebe_sloane, nipp, records, watson
from latticedb.model import Lattice

SOURCES = Path(__file__).resolve().parent.parent / "sources"


def test_nipp_tables_preserve_the_source_discriminants_and_group_orders() -> None:
    quaternary = nipp.quaternary(SOURCES / "nipp" / "d4to457.html")[0]
    quinary = nipp.quinary(SOURCES / "nipp" / "tbl.256.html")[0]
    assert (quaternary.discriminant, int(fmpz_mat(quaternary.gram_tensor).det())) == (4, 4)
    assert (quaternary.automorphism_group_order, quaternary.mass) == (1152, Fraction(1, 1152))
    assert (quinary.discriminant, int(fmpz_mat(quinary.gram_tensor).det())) == (2, 4)
    assert (quinary.automorphism_group_order, quinary.mass) == (3840, Fraction(1, 3840))


def test_brandt_intrau_tables_apply_their_distinct_parity_conventions() -> None:
    odd = brandt_intrau.table(SOURCES / "brandt_intrau" / "Brandt_1.html", odd_form=True)[0]
    even = brandt_intrau.table(SOURCES / "brandt_intrau" / "Brandt_2.html", odd_form=False)[0]
    assert (odd.discriminant, odd.gram_tensor) == (-4, ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    assert (even.discriminant, even.gram_tensor) == (-2, ((2, 1, 1), (1, 2, 1), (1, 1, 2)))


def test_watson_table_reads_lower_triangular_gram_components() -> None:
    entries = watson.stored(SOURCES / "watson" / "watson.txt")
    assert (entries[0].dimension, entries[0].gram_tensor) == (1, ((1,),))
    assert (entries[1].dimension, entries[1].gram_tensor) == (2, ((5, 1), (1, 23)))


def test_union_archive_retains_repeated_names_at_distinct_positions() -> None:
    entries = nebe_sloane.archive_rows(SOURCES / "nebe_sloane" / "union.gz")
    assert len(entries) == 823
    assert [entry.ordinal for entry in entries] == list(range(1, 824))
    assert len({entry.name for entry in entries}) < len(entries)


def test_brandt_and_watson_source_forms_seed_valid_lattice_records() -> None:
    odd = brandt_intrau.table(SOURCES / "brandt_intrau" / "Brandt_1.html", odd_form=True)[0]
    even = brandt_intrau.table(SOURCES / "brandt_intrau" / "Brandt_2.html", odd_form=False)[0]
    watson_entry = watson.stored(SOURCES / "watson" / "watson.txt")[0]
    for entry, declared in (
        (odd, brandt_intrau.record(odd)[0]),
        (even, brandt_intrau.record(even)[0]),
        (watson_entry, watson.record(watson_entry)[0]),
    ):
        lattice = Lattice.model_validate(records.derive({"tag": "ZZZZ", **declared}))
        assert lattice.gram_tensor == entry.gram_tensor
