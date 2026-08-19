# Provenance: the lattice-research corpus (research records)

Research records migrated 2026-08-20 from `~/gitclones/lattice-research`
(the frozen first-attempt lattice DSL repository), per the corpora-audit
registry sections R1-lattice-research-backends and R2-lattice-research-prose.
These are records, not maintained surfaces: the mathematics they distill has
been re-expressed on the preamble or landed in `notes/` and `references/`.

Contents:

- `session-ses_1914.md` — session record establishing that private method
  containers are never return types; the public type *is* the category's
  ``ParentMethods``.
- `realset_update_session.md` — the RealSet incident: subobject predicates
  are ambient-relative, and the assert-not-raise ruling.
- `GOAL.md`, `AGENTS.md`, `QC.md`, `QC_REPORT.md` — the corpus's staged plan,
  conduct rules, and QC wiring/status at freeze.
- `reports/workstreams/` — workstream reports, including the review that
  established `End(L) = Hom(L, L)` and `Aut = End^*` with lattice-specific
  work confined to the base object, the discriminant bridge, and the
  orthogonal subgroups.
- `agents/memories/` — 154 distilled research records (bilinear-form
  semantics, orthogonal-group conventions, Coble claim boundaries, cusp
  algorithms, monodromy/Hodge tooling, spec-design rulings).
- `agents/TODO.md`, `agents/current-goal-phase.md`, `agents/visuals/` —
  phase marker, outstanding-work list, and plan diagrams at freeze.
- `paper/` — the claim-ledger paper skeleton with typed claim states
  (source-backed / computation-supported / conjectural / disputed / failed
  path) and the LaTeX macros implementing the claim-status margin notes.

Where the mathematics landed:

- Theory corpus → `notes/topics/coble-enriques-lattice-theory/` (this
  migration supersedes the older 2026-07-13 snapshot of the same corpus at
  `archives/lattice-research/`, which the registry records as strictly older
  and smaller; that snapshot awaits its own decommission receipt).
- Literature extractions → `references/literature/lattice-research/`.
- Reflective Lorentzian database →
  `references/databases/scharlau-kirschmer-reflective-lorentzian/`.
- Isometry screens, characters, predicate subgroups, and isotropic-orbit
  machinery → the preamble
  (`lattice_homomorphisms.sage`, `lattice_isometries.sage`, `engines.sage`,
  `isotropic_orbits.sage`, `integral_lattices.sage`, `vector_orbits.sage`).
- The code corpus — backend implementations, the executable specifications,
  and the written design specification →
  `computations/scripts/lattice-research/`, which has its own map.
- The reading of that design, and where the preamble differs from it →
  `notes/category-design/lattice-dsl-prior-attempt.md`.
- The two Lean files →
  `notes/topics/coble-enriques-lattice-theory/lean/`; the proved Hessian rank
  bound is stated there, and the sorry'd isotropic-plane claim is corrected at
  `notes/topics/isotropic-vector-orbits/tco-isotropic-plane-orbit-claim.md`.
- Hodge-theoretic monodromy of a one-parameter hypersurface family →
  `notes/computations/hypersurface-family-monodromy.md` (a note beside a
  stated gap: the preamble has no surface for it).
- The Coble discriminant-orbit computations →
  `computations/scripts/coble-discriminant/`.

Also here, added with this receipt: `agents/agents/` (21 auditor role
definitions, several encoding mathematical review criteria — representation
collapse, missing base categories, the Sage boundary, spec weakening),
`agents/skills/`, `agents/plans/` (the twenty feature cards naming the
research program, plus the plan DAG and its diagrams).

Deliberately not migrated, because they are administration rather than
mathematics: the 323 per-task SPEC cards under each feature, the
`category_specs` mypy-ledger generator scripts, the issue-tracker templates,
and the repository's own QC and packaging configuration.
