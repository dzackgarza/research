"""Red test first: the class-surjectivity of Phi is not on any page.

LEMMA.  The orbit map Phi of sec-enriques-coble-correspondence is onto the divisibility-2 classes: its
image is exactly the set of 527 nonzero isotropic classes of A_{T_En}, and the class of eta(v)/2 is a
complete invariant of the orbit.

PROOF (chain, each step cited or computed).
  (a) every class in the image is a nonzero isotropic class of A_{T_En}     [prop:cusp-map-not-onto]
  (b) Phi is injective, and the source has 527 orbits                       [prop:cusp-map-injective;
                                                                            thm:coble-zero-cusp-count(2)]
      hence the image has exactly 527 elements
  (c) the class map is injective on the image: if [eta(v)/2] = [eta(v')/2] then v = v' mod 2T_Co
      [prop:cusp-map-separates-mod-two], so the classes v*, v'* agree, and thm:coble-zero-cusp-count(1)
      puts v, v' in one stable orbit, hence in one Gamma_En-orbit
  (d) A_{T_En} has exactly 527 nonzero isotropic classes                      [computed:
                                                                            coble_658-image-census-probe]
  So the image has 527 distinct classes inside a set of 527, and they are equal.

This test is RED because no page states the conclusion.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_class_surjectivity_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1f: Phi is onto the 527 nonzero isotropic classes of A_{T_En}, by "
               "prop:cusp-map-injective and thm:coble-zero-cusp-count(2) against the computed count in "
               "coble_658-image-census-probe-run.txt. No page states it. Remove this marker when one does.",
    )(fn)


@_red
def test_the_class_surjectivity_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "527" in line and ("image" in line or "onto" in line or "surject" in line):
                if "A_{T_\\\\En}" in line or "\\\\ten" in line:
                    return
    raise AssertionError(
        "no page states that the image of Phi is exactly the 527 nonzero isotropic classes of A_{T_En}"
    )


def test_the_two_counts_agree_with_the_book():
    """The lemma's arithmetic: |A_{T_En}| = 2^10 with 527 isotropic classes, and the same 527 for T_Co,
    which is what thm:coble-zero-cusp-count(2) counts as the stable 0-cusps."""
    probe = ROOT / "computations/reports/coble_658-class-surjectivity-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-class-surjectivity-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "T_En: rank 12, |A| = 1024, nonzero isotropic classes = 527" in transcript
    assert "T_Co: rank 11, |A| = 2048, nonzero isotropic classes = 527" in transcript
    assert "verdict: the lemma holds" in transcript


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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the class surjectivity)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)
