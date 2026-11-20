"""research#788: the monodromy group is never identified with the arithmetic one.

``thm:coble-monodromy-versus-enriques`` proves ``Gamma_{Co,2} <= R_gent cap O^+`` and
refutes the equality ``Gamma_{Co,2} = R_gent``; the reverse inclusion is
``qst:coble-monodromy-equality`` and is open.  A page that writes the equality says
something false about the monodromy group, and a set or a count computed through it is
the arithmetic group's.  The equality is allowed on a line that itself refutes it or
asks it, and nowhere else.

Run: python3 tests/engineering/test_coble_788_arithmetic_group_naming.py
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
WRITING = ROOT / "writing"
PAGE = WRITING / "coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md"

# `Gamma_{Co,2} = <the arithmetic group>`, in the spellings the corpus uses.  The
# lookahead lets through `Gamma_{Co,2} = R_gent cap O^+`, which is the question's object.
IDENTITY = re.compile(
    r"\\Gamma_\{\\Co,2\}\s*=\s*"
    r"(?:\\bar\\rho\^\{-1\}\(P\)|R_\{\\gent\}(?!\\intersect))")

# A line that states the equality in order to refute it or to ask it is allowed.
REFUTING = ("is false", "qst:coble-monodromy-equality", r"\neq", "refut")


def conditional_sites() -> list[str]:
    """Every line of writing/ that asserts the equality outside a refuting context."""
    out = []
    for path in sorted(WRITING.rglob("*.md")):
        if ".book" in path.parts or ".assets" in path.parts:
            continue
        for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if not IDENTITY.search(line):
                continue
            if any(mark in line for mark in REFUTING):
                continue
            out.append(f"{path.relative_to(ROOT)}:{n}")
    return out


def test_no_page_identifies_the_monodromy_group_with_the_arithmetic_one():
    sites = conditional_sites()
    assert not sites, sites


def test_the_page_keeps_the_containment_and_the_question():
    """The corrected form the pages owe: the containment of item (4), and the question."""
    text = PAGE.read_text()
    assert "\\Gamma_{\\Co,2}\\subseteq R_{\\gent}\\intersect\\Orth^+(T_\\Co)" in text
    assert "@qst:coble-monodromy-equality" in text


def _run_all() -> int:
    tests = [(n, f) for n, f in sorted(globals().items())
             if n.startswith("test_") and callable(f)]
    failures = 0
    for name, fn in tests:
        try:
            fn()
        except AssertionError as exc:
            failures += 1
            print(f"FAIL {name}: {exc}")
        else:
            print(f"ok   {name}")
    print(f"\n{len(tests) - failures}/{len(tests)} checks pass")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(_run_all())
