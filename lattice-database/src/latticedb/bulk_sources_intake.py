"""Intake of the Brandt–Intrau–Schiemann and Watson source tables."""

from fractions import Fraction
from pathlib import Path

from latticedb import arithmetic, brandt_intrau, bulk_admission, watson


def brandt(root: Path, source_file: str, start_line: int, limit: int) -> tuple[int, int]:
    """Admit a bounded range of one Brandt–Intrau–Schiemann table."""
    assert source_file in ("Brandt_1.html", "Brandt_2.html") and limit > 0
    entries = [entry for entry in brandt_intrau.stored(root / "sources" / "brandt_intrau") if entry.source_file == source_file and entry.source_line >= start_line][:limit]
    pending: list[bulk_admission.Pending] = []
    for entry in entries:
        source_determinant = arithmetic.determinant(entry.gram_tensor)
        expected_ratio = Fraction(1, 4) if entry.odd_form else Fraction(2)
        assert source_determinant == -entry.discriminant * expected_ratio, f"{source_file}:{entry.source_number}"
        scale = int(arithmetic.scale(entry.gram_tensor))
        declared, prose = brandt_intrau.record(entry, scale)
        pending.append(bulk_admission.Pending(f"{entry.source_file}:{entry.source_number}", entry.gram_tensor, scale, declared, prose, "Brandt–Intrau–Schiemann form"))
    return bulk_admission.admit(root, "brandt_intrau", pending)


def watson_rows(root: Path, start_line: int, limit: int) -> tuple[int, int]:
    """Admit a bounded range of Watson's single-class genus representatives."""
    assert limit > 0
    entries = [entry for entry in watson.stored(root / "sources" / "watson" / "watson.txt") if entry.source_line >= start_line][:limit]
    pending: list[bulk_admission.Pending] = []
    for entry in entries:
        scale = int(arithmetic.scale(entry.gram_tensor))
        declared, prose = watson.record(entry, scale)
        pending.append(bulk_admission.Pending(f"{entry.dimension}:{entry.ordinal}", entry.gram_tensor, scale, declared, prose, "Watson's form"))
    return bulk_admission.admit(root, "watson", pending)
