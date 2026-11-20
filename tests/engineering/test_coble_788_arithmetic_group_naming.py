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


KSBA = WRITING / "coble/stable-limits/ksba.md"


def test_no_prose_says_the_monodromy_group_is_the_restricted_stabilizer():
    """`Gamma_{Co,2} is the restricted stabilizer R_gent` is the refuted identity in prose."""
    for path in (PAGE, KSBA):
        text = path.read_text()
        assert "$\\Gamma_{\\Co,2}$ is the restricted stabilizer" not in text, path.name
        assert "\\Gamma_{\\Co,2} is the restricted stabilizer" not in text, path.name
    assert "$R_{\\gent} = \\bar\\rho^{-1}(P)$ is the restricted stabilizer" in PAGE.read_text()


def test_no_page_infers_membership_in_the_monodromy_group():
    """A lattice computation places an element in R_gent, not in Gamma_{Co,2}.

    The witnesses at cusp 5 are isometries fixing delta and preserving the discriminant
    decomposition, that is elements of Gent, and thm:coble-monodromy-versus-enriques(3),(4)
    refute the equality with Gamma_{Co,2} and prove only the containment; the reverse
    inclusion is qst:coble-monodromy-equality.  So a page may not read membership in R_gent
    as membership in Gamma_{Co,2}; the only remaining use is the definitional action.
    """
    text = KSBA.read_text()
    for phrase in ("form-preserving, in $\\Gamma_{\\Co,2}$",
                   "places in $\\Gamma_{\\Co,2}$",
                   "returns an element of $\\Gamma_{\\Co,2}$",
                   "The membership test in $\\Gamma_{\\Co,2}$",
                   "lies in $\\Gamma_{\\Co,2}$"):
        assert phrase not in text, phrase
    assert "$\\Gamma_{\\Co,2}$ acts on $T_\\Co$" in text


def test_the_cusp_five_orbits_are_the_arithmetic_groups():
    """The cusp-5 witnesses lie in R_gent; a positive R-relation does not descend to Gamma_{Co,2}.

    thm:coble-monodromy-versus-enriques(4) gives Gamma_{Co,2} <= R_gent cap O^+ and (3)
    refutes the equality, so R_gent-equivalence of roots 13 and 14 says nothing about
    their Gamma_{Co,2}-orbits.  The negative pair (12,13) is decided in the larger group
    and hence in the smaller, which is what makes thm:no-moduli-loss's hypothesis met.
    """
    text = KSBA.read_text()
    forbidden = ("$13$ and $14$ lie in one $\\Gamma_{\\Co,2}$-orbit",
                 "$13$ and $14$ are $\\Gamma_{\\Co,2}$-equivalent",
                 "two $\\Gamma_{\\Co,2}$-orbits, $\\{13,14\\}$",
                 "form one $\\Gamma_{\\Co,2}$-orbit")
    hits = [f for f in forbidden if f in text]
    assert not hits, hits
    assert "$R_{\\gent}$-equivalent" in text
    assert "$R_{\\gent}$-orbits" in text


def test_no_page_infers_r_gent_from_the_full_stabilizer():
    """R_gent is the image of Stab_{Gent}(delta), not of Stab_{O(T_En)}(delta).

    Gent = rho^{-1}(M) is the summand-preserving subgroup of O(T_En)
    (prop:sterk-group-identification(2)), so an isometry that fixes delta but is not
    checked to preserve the two summands of A_{T_En} lies only in the image of the full
    stabilizer, which strictly contains R_gent (prop:gamma-co-images(3)).  Two valid
    criteria remain: membership in Gent, and membership in ker(rho_{T_En}), the second
    because a reflection in a vector of the lattice is discriminant-trivial.
    """
    text = KSBA.read_text()
    for phrase in ("so its restriction to $T_\\Co$ lies in $R_{\\gent}$ (@prop:gamma-co-images(3))",
                   "that is in $R_{\\gent}$",
                   "and preserving both summands, so its restriction"):
        assert phrase not in text, phrase
    # the replacement names the criterion that decides it
    assert "\\ker\\rho_{T_\\En}\\subseteq\\gent" in text or "\\ker\\rho\\subseteq\\gent" in text


def test_no_page_reads_discriminant_triviality_as_monodromy_membership():
    """ker(rho-bar) <= R_gent is proved (prop:gamma-co-images(3)); Gamma_{Co,2} >= ker is not.

    The reverse inclusion is qst:coble-monodromy-equality, so a page may not infer that an
    isometry acting trivially on A_{T_Co} lies in Gamma_{Co,2}.  What it may infer is
    membership in R_gent, and then membership in Gamma_{Co,2} only by the containment of
    thm:coble-monodromy-versus-enriques(4), which runs the other way.
    """
    text = KSBA.read_text()
    assert "so $s_m\\in\\Gamma_{\\Co,2}$" not in text
    assert "$s_m\\in\\ker\\bar\\rho\\subseteq R_{\\gent}$" in text


def test_the_shear_is_placed_in_the_arithmetic_group_corpus_wide():
    """The same inference outside ksba.md: the shear is discriminant-trivial, hence in R_gent."""
    sites = []
    for path in sorted(WRITING.rglob("*.md")):
        if ".book" in path.parts or ".assets" in path.parts:
            continue
        for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if "\\Gamma_{\\Co,2}" not in line:
                continue
            if "not in $\\Gamma_{\\Co,2}$" in line:
                continue  # a sentence that denies the membership is the corrected form
            if re.search(r"(shear|reflection in a vector|trivially on .?A_|ker\\bar\\rho)"
                         r"[^.;]{0,160}\\Gamma_{\\Co,2}", line):
                sites.append(f"{path.relative_to(ROOT)}:{n}")
    assert not sites, sites


def test_root_reflections_are_split_by_the_square_at_552():
    """A lattice reflection is discriminant-trivial only for w^2 = -2.

    The coefficient 2(x*,w)/(w,w) is integral when w^2 = -2 and a half-integer in general
    when w^2 = -4, so only the (-2)-roots lie in ker(rho_{T_En}) by integrality; the
    (-4)-roots are placed in Gent by a summand test, and the page must say which is which.
    """
    text = KSBA.read_text()
    assert "moves every dual vector by an integral multiple of that vector" not in text
    assert "$w^2=-2$" in text and "$w^2=-4$" in text


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
