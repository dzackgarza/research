"""Pure-integer regression gates for the public T_Co kernel-incidence audit."""

import importlib.util
from pathlib import Path

import pytest


def test_coble_kernel_audit_rejects_false_integral_incidence(tmp_path):
    source = (Path(__file__).resolve().parents[2] / "computations" / "reports"
              / "coble_kernel_public_incidence_audit.py")
    spec = importlib.util.spec_from_file_location("coble_kernel_audit", source)
    assert spec is not None and spec.loader is not None
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)

    p = (2, 0, 0, 0, -1, -1, -2, -2, -2, -2, -2)
    q = (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    outside = (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
    assert audit.pairing(p, p) == audit.pairing(q, q) == audit.pairing(p, q) == 0
    assert audit.primitive_plane_pivot(p, q)
    assert audit.plane_plucker_key(p, q) == audit.plane_plucker_key(q, p)
    assert audit.plane_plucker_key(p, q) == audit.plane_plucker_key(
        p, tuple(a + b for a, b in zip(p, q))
    )
    assert audit.plane_plucker_key(p, q) != audit.plane_plucker_key(p, outside)

    duplicate = tmp_path / "duplicate.log"
    duplicate.write_text(
        f"[Otilde] plane cusp 0: ({p}, {q})\n"
        f"[Otilde] plane cusp 1: ({q}, {p})\n"
    )
    with pytest.raises(AssertionError, match="repeated integral plane span"):
        audit.audit(duplicate, class_only=True)

    wrong_class = tmp_path / "wrong-class.log"
    wrong_class.write_text(
        f"[Otilde] line cusp 0: ({outside},)\n"
        f"[Otilde] plane cusp 0: ({p}, {q})\n"
        "[Otilde] edge 0: L0 < P0\n"
    )
    with pytest.raises(AssertionError, match="divided-class incidence"):
        audit.audit(wrong_class, class_only=True)

    valid_edge = tmp_path / "valid-edge.log"
    valid_edge.write_text(
        f"[Otilde] line cusp 0: ({q},)\n"
        f"[Otilde] plane cusp 0: ({p}, {q})\n"
        "[Otilde] edge 0: L0 < P0\n"
    )
    # This is a valid *class* edge, but the strict integral-witness mode must
    # refuse the record because it contains no integral flag/transport datum.
    with pytest.raises(AssertionError, match="unparsed public row"):
        audit.audit(valid_edge)
    # Class mode passes the edge's local checks; the intentionally incomplete
    # one-edge fixture must still fail the full two-row completion criterion.
    with pytest.raises(AssertionError, match="final successful two-row summary"):
        audit.audit(valid_edge, class_only=True)
