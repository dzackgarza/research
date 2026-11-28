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

The former snapshot submodule at `archives/lattice-research/` was pinned
to exactly `05bc64e6eacc1a083df0bef6f0f69fc066ca8bab`, now preserved by the
second archival tag above. The redundant gitlink and live submodule
references are removed ([research #726](https://github.com/dzackgarza/research/issues/726)).
The original `NodeCriteria.lean` and `IsotropicPlanes.lean` are byte-identical
in `formalization/coble-enriques/`; its README identifies the other Lean
files and the obsolete project infrastructure. The paper scaffold is retained
in the provenance tree and superseded as explained below. No original
tracked object needs the old submodule to remain reachable.

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

## Live mathematical owners (2026-11-28)

The old CAS prototype is archived. Its successor is
[cas-dsl](https://github.com/dzackgarza/cas-dsl); the original consumer
requirements are now explicitly owned by its roadmap children
[#7: sets, modules and morphisms](https://github.com/dzackgarza/cas-dsl/issues/7),
[#8: lattices, isometries and cusps](https://github.com/dzackgarza/cas-dsl/issues/8),
and [#9: geometry and families](https://github.com/dzackgarza/cas-dsl/issues/9).
These supplement the successor's immutable baseline; they do not claim
the original assertions have been discharged. In particular the source
of these requirements includes the frozen category specifications,
written design specifications and mathematical regression tests.

The old monodromy requirements are also linked to
[sage-extensions #129](https://github.com/dzackgarza/sage-extensions/issues/129);
the rank-two cone question to
[#265](https://github.com/dzackgarza/sage-extensions/issues/265);
tensor universal maps and fraction/global-field questions to
[lean-categories #108](https://github.com/dzackgarza/lean-categories/issues/108)
and [#102](https://github.com/dzackgarza/lean-categories/issues/102).
The older dyadic isometry witness is now a
[manuscript example](../../../writing/lattice-theory/embeddings-and-overlattices.md#ex-dyadic-jordan-symbol-isometry).

The further source audit included the six original issue records, five
merged pull requests, their conversation comments and inline review comments.
All five PR head commits are reachable from the archived refs.
The complete original issue bodies, conversation comments, PR reviews and
inline review threads are also retained in
[github-conversations.json](github-conversations.json), including original
URLs, authors, timestamps, and reviewed commit and source coordinates.
The record contains all eleven source threads and does not depend on the
continued availability of the original GitHub repository. The source
repository has its wiki flag enabled, but the wiki Git endpoint was not
available and the web wiki URL redirected to the repository; no accessible
wiki pages were found. Discussions are disabled and no project boards were
listed. The inspected source checkout and archive had no additional authored
untracked files; the one local-only source commit changed agent guidance,
not mathematics.

The separate agent-memory project was also checked at the pre-deletion tree
of the vault commit `49e8a748a4202cef405791377b972333d89136e2`. Its 605
entries were compared with the transferred research vault and corpus.
Six paths with no same-basename match were four upstream polyhedral-common
documentation files and two obsolete diagnostic scripts, not original
mathematical results. The retained vault and Git source archive preserve
the historical plans. A completed mapping card is not evidence that its
mapped functionality was implemented.

Specific previously omitted contracts from those sources now have active
owners:

- [lean-categories #228](https://github.com/dzackgarza/lean-categories/issues/228):
  fixed-base set partitions, refinement/coarsening, ordered coarsening and
  crossing/nesting operations; the original mathematical constructions
  are in [Joins, meets, and closure](../../../writing/category-theory/constructions/Joins-Meets-and-Closure.md).
- [lean-categories #229](https://github.com/dzackgarza/lean-categories/issues/229):
  the deferred finite-poset graph, polyhedral, algebraic and polynomial
  operations, including the already existing order-complex route.
- [lean-categories #230](https://github.com/dzackgarza/lean-categories/issues/230):
  real subsets, relative topology, interval components and measure, including
  the explicit user corrections in both recorded conversations.
  See [the real-subset example](../../../writing/category-theory/foundations/Elements-and-Containment.md#ex-real-subsets-ambient-and-components).
- [sage-extensions #628](https://github.com/dzackgarza/sage-extensions/issues/628):
  Sirocco and Zariski--van Kampen plane-curve complement groups.
- [sage-extensions #629](https://github.com/dzackgarza/sage-extensions/issues/629):
  analytic curve period lattices, Jacobians, Abel--Jacobi maps, and the
  distinction between numerical candidates and proved morphisms.
  The original backend results and limitations for both geometry threads
  now appear in [Periods, Picard--Fuchs operators, and local monodromy](../../../writing/coble/computations/periods-and-local-monodromy.md).

The consumer requirements are linked to cas-dsl #7--9, including the original
lattice-expression parser's mathematical constructors without requiring its
old regex implementation. Genuine external Sage stub obligations remain
under [sage-stubs #5](https://github.com/dzackgarza/sage-stubs/issues/5).
The previously missing note `Spec Enforcement in Sage.md` was located in
the separate historical vault (`research/spec-enforcement-in-sage.md`, private
repository `agent-memory-vault`, revision
`4e0bf48fa0f01770b97e51306836ff08c6a3c95f`, blob
`dc483f1ed4fa63b0faedfe4b503eb8e242955595`). Its user requirement was
to inspect the inherited mathematical obligations of actual objects, discover
constructors and reuse constructions through composition. This survives as
[CAS DSL #10](https://github.com/dzackgarza/cas-dsl/issues/10) and in
[the architecture-inspection documentation](../../../docs/architecture-inspection.md);
the original private discussion remains in its vault, not copied into public
research. Four adjacent May 22–27 work-forward and stub-ownership notes at that
revision were also read. They concern the already transferred checker and
stub requirements and the superseded local category-provider architecture;
they do not supply additional mathematical theorems.

The original concrete Zq and Qq unramified p-adic extension constructors
and precision contracts were not found in the current owned library.
[Sage-extensions #630](https://github.com/dzackgarza/sage-extensions/issues/630)
now owns those constructions with the original ring regression and category
obligation specimens. The unfinished source comments in
`tests/sage_spec/coxeter.sage` (embedded subdiagram posets, angles, folding,
fixed and orthogonal coinvariant lattices, and enumeration) and
`category_specs/modules/tests/new_spec/surface_gaps.sage` (actual quotient
presentation, coordinate maps and polynomial-ring module) have been
transferred to the existing CAS DSL #8 and #7 respectively. The original
stable-model surgery and slc obligation is retained in
[research #669](https://github.com/dzackgarza/research/issues/669), not treated
as solved by the old diagonal-model calculation.

The remaining concrete category and consumer requirements identified in the
source declarations and regression examples are assigned to the following
active mathematical issues, with the original source links, hypotheses,
maps, and acceptance specimens in the issue bodies:

| Original mathematical construction | Current owner |
|---|---|
| Left/right/two-sided algebra ideals, radical, Peirce components and idempotent lifts | [lean-categories #231](https://github.com/dzackgarza/lean-categories/issues/231) |
| Ore quotient modules and pseudolinear action | [#232](https://github.com/dzackgarza/lean-categories/issues/232) |
| Recursive enumeration, successor graphs, finite-depth and graded families | [#233](https://github.com/dzackgarza/lean-categories/issues/233) |
| Laurent and Puiseux series, inclusions, coefficient maps and valuation | [#234](https://github.com/dzackgarza/lean-categories/issues/234) |
| Number-field class groups, unit groups, regulator, different and local integral bases | [#235](https://github.com/dzackgarza/lean-categories/issues/235) |
| Real and complex interval, ball and rounded arithmetic with approximation data | [#236](https://github.com/dzackgarza/lean-categories/issues/236) |
| Shifted free graded modules, homogeneous finite presentations and resolutions | [#237](https://github.com/dzackgarza/lean-categories/issues/237) |
| Indexed families, paired maps, selected subfamilies and inverse on image | [#238](https://github.com/dzackgarza/lean-categories/issues/238) |
| Polynomial-family enumeration and finite-field trace-dual bases | [#239](https://github.com/dzackgarza/lean-categories/issues/239) |
| Hochschild chain complexes with bimodule coefficients | [#240](https://github.com/dzackgarza/lean-categories/issues/240) |
| Hecke cell modules and their descended actions | [#241](https://github.com/dzackgarza/lean-categories/issues/241) |
| Tor with the rational torsion quotient and arbitrary-module resolutions | [#242](https://github.com/dzackgarza/lean-categories/issues/242) |

These are not requests to reproduce the old Sage wrapper classes. For
example, the source's cyclic Tor/Ext cases already have maintained
specimens in sage-extensions' `test_tor_and_ext_of_finite_cyclic_groups.sage`
and `test_derived_functors.sage`; #242 retains the additional non-finitely
generated Q/Z case and corrects the degree conventions. The Hecke
cell-module and Hochschild requests extend the existing named Lean
construction owners, not new definitions. Existing lattice isometry,
centralizer and discriminant operations are retained through the
sage-extensions and sage-indefinite-port owners.

The original rook-placement bijections, finite-lattice congruences and
certificates, metric examples, tensor symmetry data and cyclic/submodule
coordinate maps are attached to #228–230, #108 and sage-extensions #109.
The [set/module acceptance owner](https://github.com/dzackgarza/cas-dsl/issues/7#issuecomment-7238518089)
links the new requirements; the
[lattice acceptance owner](https://github.com/dzackgarza/cas-dsl/issues/8#issuecomment-7238518364)
also retains the remaining historical saturation, gluing, radical-signature,
stabilizer and flag questions. Failed searches and incorrect old assertions
are not positive acceptance evidence. The original monodromy tool note additionally specifies the global Legendre
representation and the Hesse pencil; the corrected loop matrices, group
distinction, and four type $I_3$ fibers of the Hesse pencil are retained in
[sage-extensions #129](https://github.com/dzackgarza/sage-extensions/issues/129)
and [cas-dsl #9](https://github.com/dzackgarza/cas-dsl/issues/9).
The original specialized Hodge-cycle, Fermat period, and Hodge-locus
procedure mapping is retained in
[lean-categories #243](https://github.com/dzackgarza/lean-categories/issues/243).
The original weighted Coxeter subdiagram orbits and their orbit posets
are represented by the existing `coxeter_diagrams.py` operations in
sage-extensions, including `subdiagram_orbit_poset`.

The historical local-only commit
`e4ded1c41bd875858c8f906e434e4e965d6120ad` was agent container guidance,
not an additional mathematical branch; the original local reflogs contain
no other commits outside the four published source histories.

This source audit does not establish declaration-by-declaration semantic
equivalence for all historical revisions. [Research #727](https://github.com/dzackgarza/research/issues/727)
and the current consumer requirements remain open.

The original Lean mathematical files have their research owner in
[formalization/coble-enriques](../../../formalization/coble-enriques/README.md).
The earlier paper is preserved in `paper/` and the full Git history.
Its `main.tex`, `macros/research-notes.tex`, five sections
(`claims.tex`, `current-program.tex`, `failed-explorations.tex`,
`uncertainty.tex`, `workstreams.tex`), README and ignore file constitute
a paper scaffold, claim-status machinery, and research-policy/workstream
templates, not an additional mathematical manuscript. The current
dissertation and mathematical writing, together with the issue tree,
supersede that scaffold. No mathematical claim from the paper requires
another copy in the writing tree.

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
  and smaller; that duplicate snapshot has been retired).
- Literature extractions → `references/literature/lattice-research/`.
- Reflective Lorentzian database →
  `references/databases/scharlau-kirschmer-reflective-lorentzian/`.
- Isometry screens, characters, predicate subgroups, and isotropic-orbit
  machinery → the preamble
  (`lattice_homomorphisms.sage`, `lattice_isometries.sage`, `engines.sage`,
  `isotropic_orbits.sage`, `integral_lattices.sage`, `vector_orbits.sage`).
- The former code corpus (93 tracked files) is preserved at its
  [immutable pre-retirement revision](https://github.com/dzackgarza/research/tree/889f214f54198fb4e46fce69be1d80a84b062230/computations/scripts/lattice-research).
  The current operation owners and specific open implementation obligations are
  recorded at [sage-extensions #60](https://github.com/dzackgarza/sage-extensions/issues/60#issuecomment-7239055418),
  [cas-dsl #8](https://github.com/dzackgarza/cas-dsl/issues/8#issuecomment-7239055676),
  [sage-extensions #124](https://github.com/dzackgarza/sage-extensions/issues/124#issuecomment-7239055875),
  [#129](https://github.com/dzackgarza/sage-extensions/issues/129#issuecomment-7239056048),
  and [sage-indefinite-port #64](https://github.com/dzackgarza/sage-indefinite-port/issues/64#issuecomment-7239056249).
  The historical binary same-genus/nonisometry example is now proved in
  [Discriminant forms and genus](../../../writing/lattice-theory/discriminant-forms-and-genus.md#ex-binary-same-genus-not-isometric).
  The obsolete reference code does not remain a second implementation under
  `computations/scripts/`; the exact original tree is reachable from research's
  published history. This is the lattice-research disposition of
  [research #727](https://github.com/dzackgarza/research/issues/727).
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
