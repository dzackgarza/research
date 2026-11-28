# Provenance: the lattice-research corpus (research records)

## Source recovery (2026-11-27)

`source-main-67c244a0.tsv` maps every tracked entry of lattice-research
main at `67c244a011c24c8870a9d84c7f1210add1457e92` to an identical existing
research blob or a preserved source file under `source-main/` (or records
an external Git link). The recovered category specifications, Sage
patches, fixtures and theory notes are historical inputs, not maintained
APIs or trusted assertions. Their source declarations are deliberately
not installed into the live mathematical library. Source symlinks are
preserved as text rather than activated.

The three non-main branch heads are also accounted for under
`historical-branches/`: the frozen July archive (`05bc64e6`), the memory
migration (`af87e631`), and the branch deleting the Lean sources (`fbe36440`).
The per-branch manifests identify the source commit, original path and
preserved Git blob. In particular, the task/spec/decision records from the
memory-migration branch no longer depend on an external vault or old branch.

The latest recoverable deleted-file versions, including the original
Coble computational scripts and stdout transcripts, earlier research proof
notes, and historical decision/specification cards, are preserved under
`deleted-history/` with `manifest.tsv`. Each path records the pre-deletion
revision and original blob. Historical claim statuses and reported successes
are not proofs; the preserved texts must not override subsequent corrections.
The first Task 1.1 parametrization has been independently verified and
forward-ported as [an explicit ten-nodal sextic and its K3 cover](../../../writing/coble/coble-surfaces/rational-sextic-calculations.md#ex-explicit-ten-nodal-sextic).
The [corrected module calculations](../../../writing/category-theory/constructions/Generators-and-Presentations.md#sec-integral-presentation-examples)
replace incompatible expectations in the old module script.

The original fixture witnesses and source-table labels have been
reconciled in [the corrected two-elementary specimens](../../../references/databases/alexeev-engel-two-elementary/README.md).
The fixed-square orbit claim has been corrected and proved in
[the lattice theory chapter](../../../writing/lattice-theory/embeddings-and-overlattices.md#prop-fixed-norm-orbit-finiteness).
The source snapshot establishes preservation, not semantic or execution
parity of the historical category specifications; their assertions must
be judged at the present formalization and acceptance owners.

## Complete published Git history and earlier numbered records (2026-11-28)

The four original published branch tips are preserved as lightweight archival
tags in the research repository itself. Their object IDs were checked against
the source remote refs:

| Original tip | Research tag | Commit |
|---|---|---|
| main | archive/lattice-research/main | 67c244a011c24c8870a9d84c7f1210add1457e92 |
| chore/archive-frozen-category-specifications | archive/lattice-research/archive-frozen-category-specifications | 05bc64e6eacc1a083df0bef6f0f69fc066ca8bab |
| chore/migrate-memories-to-iwe2 | archive/lattice-research/migrate-memories-to-iwe2 | af87e6315f8d260554e46a71b87ffa8fe293ac34 |
| claude/gallant-mccarthy-oglg4j | archive/lattice-research/gallant-mccarthy-oglg4j | fbe36440a96be7dc6b04ca0f6dfc4d362b187e01 |

These are frozen source-history refs, not development branches. Every ancestor
and tracked Git object reachable from these tips can be retrieved from research
without access to the former repository. This retains intermediate revisions
without installing obsolete code or duplicating every revision as files.

[early-records/manifest.tsv](early-records/manifest.tsv) additionally maps 296
previously unmatched historical authored paths to byte-identical files,
including the original numbered tasks (144 paths), earlier proof attempts,
audit and verification records, and the original Nikulin pyramid. There are
210 additional materialized blobs. The remaining downloaded literature and
other historical versions are retained in the archival Git tags. Historical
assertions and task completion statuses are not current proofs or acceptance
evidence.

The literature-specific ten-point fixture of T-1007 and T-3001 is now
[the explicit Desargues sextic](../../../writing/coble/coble-surfaces/rational-sextic-calculations.md#ex-thas-desargues-sextic),
including the ten rational nodes, all ten configuration lines and the
index-16 curve-generated sublattice. Its exact arithmetic is reproduced in
the linked script. [Research #851](https://github.com/dzackgarza/research/issues/851)
owns the remaining classical nine-point completion questions; the earlier
generic sextics alone did not satisfy the literature-specific fixture.

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

Excluded from the August 2026 migration, because they were administration rather than
mathematics: the 323 per-task SPEC cards under each feature, the
`category_specs` mypy-ledger generator scripts, the issue-tracker templates,
and the repository's own QC and packaging configuration. The November source
recovery above supersedes these exclusions for tracked entries of the pinned
source revision.
