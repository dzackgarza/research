# References

Sources for the Sterk reconstruction, its dependency graph, and the
formalization-practice policies (`FRM-*`, `FDC-*`, `FRD-*`, `FSC-*`, `FSV-*` in
the repository `CONTRIBUTING.md`).  Every citation below was read at the stated
locator; none is recalled.  Access dates are 2026-09-09 unless stated.

## The mathematics

**[Ste88a]** H. J. M. Sterk, *Compactifications of the period space of Enriques
surfaces: arithmetic and geometric aspects*.  Proefschrift, Katholieke
Universiteit te Nijmegen, 13 September 1988.  167 pp.
Radboud Repository: <http://hdl.handle.net/2066/113552>.
Zotero key `Ste88a`, item `42VIAWPR`.
*The text this work reads.*  Chap. 2 §§1–3 is the boundary computation:
(2.7)–(2.8) define $\Gamma$; (2.10) characterizes it; (2.16)–(2.18) are the
orbit lemmas and Eichler's criterion; (3.2.1)–(3.2.4) the five zero-dimensional
cusps; (3.3.4)–(3.3.20) the Coxeter diagrams, their maximal parabolic
subdiagrams, and the nine one-dimensional cusps; (3.4) the incidence diagram.
The diagram of $W_e$ is §3.3.7, printed p. 58 (PDF p. 70).

**[Ste91]** H. Sterk, *Compactifications of the period space of Enriques
surfaces. I*.  Math. Z. **207** (1991).  Zotero key `Ste91`, item `SW47ULJ5`.
The published form of the thesis material above, with Chap. 2 §§3.2, 3.3
renumbered §§4.2, 4.3 — so (3.2.3) there is (4.2.3), and the diagram of $W_e$ is
(4.3.5)ff.

**[Ste95a]** H. Sterk, *Compactifications of the period space of Enriques
surfaces. II*.  Math. Z. **220** (1995), 427–444.  DOI
[10.1007/BF02572623](https://doi.org/10.1007/BF02572623).  Zotero key `Ste95a`,
item `VAICKFL6`.
⚠️ **The PDF attached to this Zotero item is the 1988 thesis, not the Math. Z.
paper** — 167 pages, `PROEFSCHRIFT` title page — and its extracted markdown and
notes children are likewise thesis text.  The real Math. Z. 220 PDF is not in
the library.  Section numbers quoted in this work as `3.3.x` are the thesis
numbering, read from that attachment.

**[Vin75]** È. B. Vinberg, *Some arithmetical discrete groups in Lobačevskiĭ
spaces* (1975); cited by Sterk for the fundamental polyhedron of a hyperbolic
reflection group, its Coxeter diagram, and the correspondence between vertices
at infinity and parabolic subdiagrams of rank $n-1$; table 2 is the list of
extended Dynkin diagrams used to label them.  Cited via Sterk (3.3.2)–(3.3.3);
**not read in the original**.

**[Vin83]** È. B. Vinberg, (1.9): the isotropic vector read off a parabolic
subdiagram.  Cited via Sterk (3.3.3); **not read in the original**.

**[Nik80]** V. V. Nikulin, Theorem 1.13.2: an even lattice is determined up to
isometry by its signature and discriminant form; Theorem 1.14.2 cited at Sterk
(2.x).  Cited via Sterk; **not read in the original**.

**[Sca84]** F. Scattone, *On the compactification of moduli spaces for
algebraic K3 surfaces* (1984), 5.6.10, §6, and the list of nine possibilities
for $F^\perp/F$ on p. 100.  Cited via Sterk (3.3.7); **not read in the
original**.

## Formalization practice

**[YS26]** B. Yanahama and A. Sannai, *Lean Atlas: An Integrated Proof
Environment for Scalable Human-AI Collaborative Formalization*.
arXiv:[2604.16347](https://arxiv.org/abs/2604.16347) [cs.HC], 16 March 2026.
Read: abstract, §§1–5, pp. 1–6.
Supplies: **semantic hallucination** (Def. 1) and its five patterns —
definition mismatch, missing or extra assumptions, goal substitution, quantifier
and scope errors, type default semantics shift (§3.1); **type vs value
dependency** (Defs. 2–3) and the 8-kind edge classification with pruning rules
(Table 1); **Lean Compass** (§5) and its soundness argument (Prop. 4);
**aligned Lean code** as a quality standard; review-set reductions of 94–99%
on proof-heavy projects, 59.8% on a six-theorem FLT milestone subset, 69.0% on
PhysLib, 27.3% on definition-heavy XMSS.  Basis of `FSV-*`.

**[Ant26]** Anthropic, *Formalizing Fermat's Last Theorem*, announced
2026-09-04.  <https://www.anthropic.com/research/formalizing-fermats-last-theorem>.
The first end-to-end machine-checked proof of FLT: 11 days largely autonomous,
13 million lines of Lean, 30,300 theorems, ~6 billion output tokens, over five
times the size of Mathlib.  Records that earlier attempts failed because agents
lost track of project state, and that the successful run was carried on
Prove2Me, which maintains a DAG of theorem statements.  Basis of `FSC-00`.

**[AntTR26]** Anthropic, *Formalizing Fermat's Last Theorem in Lean: A timeline
and selected excerpts from Claude's reasoning*, September 2026.
<https://www-cdn.anthropic.com/9e431dff043da6538d99d6c2d231b670aa3da263.pdf>.
Read in full (pp. 1–14).  **The primary process document for the 11-day run**,
and the source for everything in `PROCESS.md` about it: Day 1 = 7 August 2026,
root card Proved 22:00 ET on 17 August; harness built on Prove2Me, developed by
Tianyi Peng's group at Columbia; a *card* is one theorem statement posted as a
node in the shared dependency graph plus its accepted proof; humans "wrote no
mathematics and no Lean beyond the one-line statement of the goal theorem";
agents "wrote the statements, checked one another's statements, and proved
them"; built on Mathlib, on the Imperial College FLT project — whose blueprint
the opening reduction follows, with **106 files adapted with credit** — and on
flt-regular; 29,511 theorems, ~533,000 local supporting lemmas, 13M lines (10.5M
without generated boilerplate), 3 standard axioms, no `sorry`; the Day 7 dip in
the theorem count is "a rewiring of that dependency tree, not lost work"; §4 the
four-stage end-to-end check (recompile outside the platform, single-project
build, Lean FRO comparator, nanoda); §5 Claude's own assessment that
"correctness is not the difference.  The difference is form."

**[AntRepo]** Anthropic, *fermats-last-theorem*.
<https://github.com/anthropics/fermats-last-theorem>.  The released proof, with
a `PROOF-PATH.md` recording how strong each named result is as proved.
**Not yet read.**

**[Xena26]** K. Buzzard, *FLT: Anthropic has beaten me to it*, Xena Project blog,
2026-09-04.  <https://xenaproject.wordpress.com/2026/09/04/flt-anthropic-has-beaten-me-to-it/>.
**Not yet read** — the assessment of the run by the person running the human
project, and the obvious next thing to read.

**[FLT]** Imperial College London, *FLT* — ongoing Lean formalization of Fermat's
Last Theorem.  <https://github.com/ImperialCollegeLondon/FLT>.  Created
2023-11-19, active, 69 contributors, EPSRC grant EP/Y022904/1 to Kevin Buzzard,
first phase to September 2029.  Read at this date: `GENERAL.md` (build from both
ends; state the assumed claims first; PR foundations to Mathlib as you go; route
designed by Richard Taylor), `CONTRIBUTING.md` (the `claim`/`disclaim`/`propose`/
`withdraw`/`awaiting-review` workflow and the dashboard columns), `blog.md`
(Buzzard's project announcement; blueprint software by Patrick Massot, first used
for the sphere eversion project), and the commit history.

**[FLTann]** K. Buzzard, *The Fermat's Last Theorem Project*, Lean community
blog, 2024-03-24.
<https://leanprover-community.github.io/blog/posts/FLT-announcement/>.

**[NS26]** OpenAI, *On the Navier–Stokes Millennium Prize Problem*, 2026-09.
<https://openai.com/index/navier-stokes-solution/>.  Proof reached about 88
hours after launch; Lean formalization and verification a further 17 hours.

**[NSrepo]** OpenAI, *NavierStokesAndEuler* — Lean certificates.
<https://github.com/openai/NavierStokesAndEuler>, published 2026-09-08.  Read:
`README.md`, `formalization.yaml`, `ComparatorChallenges/README.md`.  Supplies
the `formalization.yaml` schema v0.4 usage, with `sorry_count`,
`sorry_in_definitions`, and per-result `axioms`; and the independent-checking
setup.

**[FormalizationYAML]** Mathlib Initiative, *formalization.yaml* schema.
<https://github.com/mathlib-initiative/formalization.yaml> (schema v0.4 as used
by [NSrepo]).

**[Comparator]** *comparator* — independent proof checking for Lean.
<https://github.com/leanprover/comparator>, run with `lean4export`, `nanoda_bin`
and `landrun`.

**[FormalConjectures]** Google DeepMind, *Formal Conjectures* — the Lean
formalization of the Clay Navier–Stokes problem statement, adapted by [NSrepo]
as its Comparator reference statements.
<https://github.com/google-deepmind/formal-conjectures>.

**[Blueprint]** P. Massot, *leanblueprint* (2020): generates dependency graphs
from a LaTeX write-up for tracking formalization progress.  Cited by [YS26] §2
and used by [FLT]; **tool not used here yet**.

**[P2M]** Prove2me, <https://prove2.me>, API `https://prove2.me/api/v1`, skill
version 0.9.8; workspace <https://github.com/prove2me/prove2me_workspace>.
Maintains a DAG of theorem statements; supports reduction (sketch) submissions
whose imported child lemmas become open problems and whose parent auto-resolves
when they are proved.

## Not read

Recorded so the gap is visible rather than implied: Vinberg 1975 and 1983,
Nikulin 1980, and Scattone 1984 are cited here only as Sterk cites them.  Any
node of the dependency graph that rests on them needs its own reading before its
statement is written, per `FRM-02`.
