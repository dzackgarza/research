"""Integrity index of the research#658 chain: every probe and its verdict, checked on main.

The session that produced this index left, on #658, one proved or refuted lemma per turn.  Each is a script
under computations/reports/ with its committed transcript; this module asserts that each transcript is
present and carries the verdict its script prints, so a later reader (or a later session) can rely on the
chain without re-deriving it.  It is an index, not a new mathematical claim.

The twelve entries, by subject:

  item 1 (the Gamma_Co lifting)
    coble_658-gamma-co-discriminant-probe        the deciding probe for Gamma_Co <= ker(rho); verdict
                                                 "undecided" until generators exist
    coble_658-nodal-pair-refutation-probe        REFUTED: the nodal-pair monodromy acts on T_Co as the
                                                 reflection in a (-4)-class, outside the kernel
    coble_658-meridian-lemma-probe                reflections and Eichler transvections lie in the kernel
    coble_658-reflective-generation-probe         2668 reflections, 200 transvections, 100 products, all in
    coble_658-cusp-parabolic-probe                16 cusp meridians, in the kernel
    coble_658-kernel-exceeds-short-roots-probe    the <2>-summand reflection is in the kernel, out of O^+
    coble_658-isotropic-separates-probe           an isometry is trivial iff it fixes the 527 classes
    coble_658-index-narrowing-probe               the index divides 696,729,600
    coble_658-equivalent-forms-probe              the four equivalent forms
    coble_658-dichotomy-probe                     rho = G_Co would falsify the item
    coble_658-forward-half-probe                  the item is the forward half of conj:gamma-co-stable
    coble_658-conditional-corollary-probe         under conj:gamma-co-stable the lifting holds for Gamma_Co
    coble_658-polarized-containment-probe         Gamma_{Co,2} <= Gamma_Co would falsify the item
    coble_658-polarized-not-kernel-probe          the polarized monodromy is NOT in the kernel
    coble_658-meridians-do-not-generate-probe     "the meridians generate the monodromy" is false for it
    coble_658-pushoff-fails-probe                 the removed locus is not closed, so no push-off
    coble_658-enriques-monodromy-gap-probe        the Enriques monodromy identification is unsourced
    coble_658-induces-tension-probe               the "induces" clause vs rmk:gamma-co-status
    coble_658-strong-reading-false-probe          the clause cannot be a map of bases

  item 1f (the image of Phi)
    coble_658-image-witness-probe                 the witness's cheap test, verified
    coble_658-stabilizer-image-probe              the witness IS in the image (explicit transporter)
    coble_658-class-orbit-probe                   a second transporter through e~'
    coble_658-image-census-probe                  527 of 527 classes pass the necessary test
    coble_658-class-surjectivity-probe            Phi is onto the 527 classes

The RED item: the book carries no such index, and this one lives only in the test tree.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
REPORTS = ROOT / "computations/reports"
RED_NAME = "test_the_chain_index_is_in_the_book"

# (transcript, a line the script prints that states its verdict)
CHAIN = [
    ("coble_658-gamma-co-discriminant-probe-run.txt", "verdict: undecided"),
    ("coble_658-nodal-pair-refutation-probe-run.txt", "verdict: item 1e is FALSE."),
    ("coble_658-pointwise-criterion-probe-run.txt", "An isometry fixing S_Co pointwise acts trivially on A_{T_Co}"),
    ("coble_658-source-census-probe-run.txt", "verdict: no source held in tmp/sources states the monodromy group"),
    ("coble_658-meridian-lemma-probe-run.txt", "verdict: the meridian lemma is PROVED"),
    ("coble_658-reflective-generation-probe-run.txt", "verdict: item 1e holds for every subgroup"),
    ("coble_658-cusp-parabolic-probe-run.txt", "verdict: every kind of monodromy element"),
    ("coble_658-kernel-exceeds-short-roots-probe-run.txt", "consequence: ker(rho_{T_Co}) strictly contains"),
    ("coble_658-isotropic-separates-probe-run.txt", "verdict: the lemma holds"),
    ("coble_658-index-narrowing-probe-run.txt", "verdict: the lemma holds"),
    ("coble_658-equivalent-forms-probe-run.txt", "verdict: the lemma holds"),
    ("coble_658-dichotomy-probe-run.txt", "verdict: the dichotomy holds"),
    ("coble_658-forward-half-probe-run.txt", "verdict: the lemma holds"),
    ("coble_658-conditional-corollary-probe-run.txt", "verdict: the corollary holds"),
    ("coble_658-polarized-containment-probe-run.txt", "verdict: the lemma holds"),
    ("coble_658-polarized-not-kernel-probe-run.txt", "verdict: the discriminant kernel is strictly smaller"),
    ("coble_658-meridians-do-not-generate-probe-run.txt", "verdict: REFUTED"),
    ("coble_658-pushoff-fails-probe-run.txt", "verdict: the lemma holds"),
    ("coble_658-enriques-monodromy-gap-probe-run.txt", "verdict: REFUTED"),
    ("coble_658-induces-tension-probe-run.txt", "verdict: RESOLVED."),
    ("coble_658-strong-reading-false-probe-run.txt", "verdict: REFUTED"),
    ("coble_658-image-witness-probe-run.txt", "the (-2)-vectors of T_En are infinite in number"),
    ("coble_658-stabilizer-image-probe-run.txt", "verdict: the class of w = 2e~ + e~' IS in the image of Phi."),
    ("coble_658-class-orbit-probe-run.txt", "verdict: the class of w = 2e~ + e~' IS in the image of Phi."),
    ("coble_658-two-step-transporter-probe-run.txt", "verdict: undecided -- no certificate"),
    ("coble_658-image-census-probe-run.txt", "527 of 527"),
    ("coble_658-class-surjectivity-probe-run.txt", "verdict: the lemma holds"),
]


def test_every_transcript_is_present_with_its_verdict():
    missing = []
    for name, needle in CHAIN:
        path = REPORTS / name
        if not path.is_file():
            missing.append("%s: absent" % name)
            continue
        if needle not in path.read_text(encoding="utf-8"):
            missing.append("%s: verdict line absent" % name)
        if not (REPORTS / name.replace("-run.txt", ".py")).is_file():
            missing.append("%s: script absent" % name)
    assert not missing, missing


def test_the_index_covers_every_probe_on_main():
    scripts = {p.name for p in REPORTS.glob("coble_658-*.py")}
    indexed = {name.replace("-run.txt", ".py") for name, _ in CHAIN}
    assert not (scripts - indexed), "unindexed probes: %s" % sorted(scripts - indexed)


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658: the chain of lemmas lives only in computations/reports and the test tree; no "
               "page of writing/ indexes it. Remove this marker when one does.",
    )(fn)


@_red
def test_the_chain_index_is_in_the_book():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        if "coble_658-meridian-lemma-probe" in text and "coble_658-dichotomy-probe" in text:
            return
    raise AssertionError(
        "no page of writing/ indexes the #658 chain: the meridian lemma, the isotropy, index, dichotomy, "
        "forward-half, conditional-corollary, containment and gap results, and the image decisions"
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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the book has no index)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)
