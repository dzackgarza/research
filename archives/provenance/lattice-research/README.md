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
  `isotropic_orbits.sage`, `integral_lattices.sage`).
