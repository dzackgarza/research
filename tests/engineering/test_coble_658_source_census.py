"""Red test first: the source census for the monodromy groups is on no page.

CLAIM (recorded by computation).  None of the sources held in tmp/sources states the monodromy group of the
moduli of Coble surfaces, or of unpolarized Enriques surfaces.  The book's identification of the Enriques
monodromy with O~+(T_En) (def:gamma-co-groups item 1) and conj:gamma-co-stable for Coble are therefore not
derivable from the material at hand, and item 1e's remaining input is external.

The probe scans every text and PDF of tmp/sources for the phrases that would carry such a statement -- a
monodromy group acting on a period domain, for the Coble or the Enriques family -- and prints, file by file,
what it finds.  It is a negative census, not a proof of absence in the literature: a source that is not in
tmp/sources is not covered, and the census says so.

This test is RED because no page records the census.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_census_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: no source in tmp/sources states the monodromy group of the Coble or "
               "of the unpolarized Enriques moduli; the item's remaining input is external. No page records "
               "the census. Remove this marker when one does.",
    )(fn)


def test_the_probe_and_its_transcript_are_present():
    probe = ROOT / "computations/reports/coble_658-source-census-probe.py"
    transcript = ROOT / "computations/reports/coble_658-source-census-probe-run.txt"
    assert probe.is_file() and transcript.is_file()
    text = transcript.read_text(encoding="utf-8")
    assert "sources scanned" in text
    assert "verdict:" in text


@_red
def test_the_census_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "tmp/sources" in line and ("monodromy" in line or "census" in line):
                if "no source" in line.lower() or "none" in line.lower():
                    return
    raise AssertionError(
        "no page records that no source in tmp/sources states the monodromy group of the Coble or of the "
        "unpolarized Enriques moduli"
    )


def _run_all() -> int:
    items = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]
    failures = 0
    for name, fn in items:
        try:
            fn()
        except AssertionError as exc:
            if name == RED_NAME:
                print(f"RED  {name}: {exc}")
                continue
            failures += 1
            print(f"FAIL {name}: {exc}")
        else:
            print(f"ok   {name}")
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the census)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)
