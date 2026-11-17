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
    identity = [[int(i == j) for j in range(11)] for i in range(11)]

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

    # An edge must use the *indexed integral plane*, not merely a different
    # primitive isotropic plane with the same mod-two discriminant subgroup.
    # Negate the E8 coordinates but retain the positive coordinate.
    # This is another isotropic vector with identical parity.
    p_other = p[:3] + tuple(-a for a in p[3:])
    assert audit.pairing(p_other, p_other) == audit.pairing(p_other, q) == 0
    assert audit.mod2_span(p_other, q) == audit.mod2_span(p, q)
    assert audit.plane_plucker_key(p_other, q) != audit.plane_plucker_key(p, q)
    mismatched_plane = tmp_path / "mismatched-plane.log"
    mismatched_plane.write_text(
        f"[Otilde] line cusp 0: ({q},)\n"
        f"[Otilde] plane cusp 0: ({p}, {q})\n"
        f"[Otilde] edge 0: L0 < P0; line=({q},); plane=({p_other}, {q}); "
        f"transporter={identity}\n"
    )
    with pytest.raises(AssertionError, match="edge plane differs from indexed integral plane"):
        audit.audit(mismatched_plane)

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

    strict_valid = tmp_path / "strict-valid.log"
    strict_valid.write_text(
        f"[Otilde] line cusp 0: ({q},)\n"
        f"[Otilde] plane cusp 0: ({p}, {q})\n"
        f"[Otilde] edge 0: L0 < P0; line=({q},); plane=({p}, {q}); "
        f"transporter={identity}\n"
    )
    with pytest.raises(AssertionError, match="final successful two-row summary"):
        audit.audit(strict_valid)

    missing_transporter = tmp_path / "missing-transporter.log"
    missing_transporter.write_text(
        f"[Otilde] line cusp 0: ({q},)\n"
        f"[Otilde] plane cusp 0: ({p}, {q})\n"
        f"[Otilde] edge 0: L0 < P0; line=({q},); plane=({p}, {q})\n"
    )
    with pytest.raises(AssertionError, match="unparsed public row"):
        audit.audit(missing_transporter)

    negative_spinor = [row[:] for row in identity]
    negative_spinor[0][0] = -1  # positive-norm reflection, kernel modulo 2
    wrong_spinor = tmp_path / "wrong-spinor.log"
    wrong_spinor.write_text(
        f"[Otilde+] line cusp 0: ({q},)\n"
        f"[Otilde+] plane cusp 0: ({p}, {q})\n"
        f"[Otilde+] edge 0: L0 < P0; line=({q},); plane=({p}, {q}); "
        f"transporter={negative_spinor}\n"
    )
    with pytest.raises(AssertionError, match="positive real spinor orientation"):
        audit.audit(wrong_spinor)

    wrong_gram = [row[:] for row in identity]
    wrong_gram[3][3] = -1  # does not preserve E8(-2) off-diagonal pairings
    wrong_gram_log = tmp_path / "wrong-gram.log"
    wrong_gram_log.write_text(
        f"[Otilde] line cusp 0: ({q},)\n"
        f"[Otilde] plane cusp 0: ({p}, {q})\n"
        f"[Otilde] edge 0: L0 < P0; line=({q},); plane=({p}, {q}); "
        f"transporter={wrong_gram}\n"
    )
    with pytest.raises(AssertionError, match="transporter integral Gram"):
        audit.audit(wrong_gram_log)
