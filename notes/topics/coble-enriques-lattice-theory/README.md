# Coble–Enriques lattice theory (migrated corpus)

The theory corpus of `~/gitclones/lattice-research`, migrated 2026-08-20 per
the corpora-audit registry (R2-lattice-research-prose). This landing
**supersedes the older 2026-07-13 snapshot** of the same corpus at
`archives/lattice-research/theory/`, which the registry records as strictly
older and smaller; that snapshot awaits its own decommission receipt and is
not maintained.

Contents:

- `reflective-two-elementary-lattices.md` — the 1368-line sourced glossary:
  conventions, ~60 definitions, and 12 results on two-elementary lattices,
  K3 moduli, and compactifications. Its WARNING section (Arf, Brown–Kervaire,
  and Milgram do **not** classify integral lattices) is the correction
  authority two of the migration corrections below cite.
- `coble-task-background.md` — the Coble research program's mathematical
  spine (tasks 1.1–6.1). Two corrections applied on landing, marked in
  place: the Nikulin citation for the (r, a, δ) classification (Thm 3.6.2,
  not 1.14.2 — verified against the Nikulin extraction), and the
  Brown-invariant congruence demoted from "verification" of q_T = −q_S to a
  necessary consequence of it.
- `coble-standard-target-discriminant-form.md` — the N = 2B computation for
  the standard Coble target: 528 isotropic classes, |O(A_N, q_N)|, orbit
  lengths [1, 527], and the primitive-isotropic transitivity argument.
- `computable-sets.md` — the design decision that Sets means computable
  sets, with the EnumeratedSets ↔ Sets().Countable() identifications the
  preamble's placements realize.
- `finiteness-orbits-indefinite-lattices.md` — finiteness of O(L)-orbits of
  fixed-norm vectors in indefinite lattices (Siegel/Kitaoka; quantitative
  counting references). The theorem that makes vector-orbit enumeration
  well-posed.
- `moduli-dimension-claim.md` — type IV period-domain dimension r − 2;
  M-polarized K3 moduli dimension 20 − rank(M); the Coble K3 double cover
  and I_{1,10}(2).
- `reference-map.md` — the canonical reference map per claim family
  (deduplicated opening, see its header note).
- `claim-map.md` — claim-to-source map for the Coble sextic, the K3 cover
  lattice, the degree-2 polarization, the period-domain dimension, and the
  Torelli step.
- `references.bib` — the corpus's central BibTeX.
- `theory-tree-index.md` — the source tree's own routing rules, kept as
  context for the file names above.

Related landings:

- Literature extractions: `references/literature/lattice-research/`.
- The two discriminant computations:
  `computations/scripts/coble-discriminant/`.
- The open T_Co isotropic-plane claim, with its recorded errors corrected:
  `notes/topics/isotropic-vector-orbits/tco-isotropic-plane-orbit-claim.md`.
- The corpus's two Lean files, and the proved Hessian rank bound at a node of
  a plane sextic: `lean/` in this directory.
- The corpus's code — backend implementations, executable specifications, the
  written design specification: `computations/scripts/lattice-research/`.
