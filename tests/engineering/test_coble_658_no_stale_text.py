"""Phrasings that were wrong on this issue, and the statements that replaced them.

Every entry below is a sentence that was on main at some point and is now withdrawn.  They are kept
here so that a later edit cannot restore one of them silently, and the replacements are named beside
it so a reader sees what to use instead.

  1. "the question is invisible to the discriminant representation ... exactly as every w_delta is"
     (coble-heegner-research-report.md) -- false for the nodal-pair products, which move A_{T_Co}.
     Replacement: the parity statement in prop:gamma-co-reflective-set(3).
  2. "every wall reflection already lies in the stable group" (in the record smwo_direct-period.md)
     -- true for (-2)-walls, false for mixed walls.
     Replacement: the dated correction block appended to that record.
  3. "which divisibility-2 classes these are is open" (the register) -- stale: the classes are
     exactly the 527 nonzero isotropic classes (prop:cusp-map-surjective-on-classes).
     Replacement: the orbit count of prop:cusp-map-onto-criterion.
  4. the equality Gamma_Co = O~^+(T_Co) asserted as a fact (it was briefly a theorem here) -- it is
     the open conjecture conj:gamma-co-stable.
     Replacement: conj:gamma-co-stable plus rmk:gamma-co-nodal-pair-proposal.

Run standalone (``python3 tests/engineering/test_coble_658_no_stale_text.py``) or under pytest.
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
WRITING = ROOT / "writing"

WITHDRAWN = [
    "invisible to the discriminant representation",
    "every wall reflection already lies in the stable group",
    "which divisibility-$2$ classes these are open",
    "This statement is false (@thm:gamma-co-not-stable)",
]

REPLACEMENTS = {
    "prop:gamma-co-reflective-set": "writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md",
    "prop:cusp-map-onto-criterion": "writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md",
    "prop:ten-no-second-plane": "writing/coble/lattices-and-moduli/discriminant-orbits-of-the-coble-lattice.md",
    "prop:tco-no-hyperbolic-plane": "writing/coble/lattices-and-moduli/discriminant-orbits-of-the-coble-lattice.md",
    "rmk:gamma-co-nodal-pair-proposal": "writing/coble/lattices-and-moduli/lattices.md",
}


def test_no_withdrawn_phrasing_survives():
    offenders = []
    for path in sorted(WRITING.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for phrase in WITHDRAWN:
            if phrase in text:
                offenders.append("%s: %s" % (path.relative_to(ROOT), phrase))
    assert not offenders, offenders


def test_the_replacements_are_present():
    missing = []
    for label, rel in REPLACEMENTS.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        if "#" + label not in text:
            missing.append("%s in %s" % (label, rel))
    assert not missing, missing


def test_the_record_keeps_the_dated_correction():
    record = (ROOT / "computations/reports/smwo_direct-period.md").read_text(encoding="utf-8")
    assert "## Correction, 2026-11-19" in record
    assert "every `(-2)`-wall reflection already lies in the stable group" in record


def _run_all() -> int:
    items = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]
    failures = 0
    for name, fn in items:
        try:
            fn()
        except AssertionError as exc:
            failures += 1
            print(f"FAIL {name}: {exc}")
        else:
            print(f"ok   {name}")
    print(f"\n{len(items) - failures}/{len(items)} checks pass")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)
