# Memory Migration Classification Ledger

Classification of every in-scope memory file for migration into the iwe2 vault
`github.com__dzackgarza__lattice-research`. Built by subagent fan-out over the
manifest. Disposition ∈ {DURABLE, JUNK, DUPLICATE}. Type ∈ {decision, trap, advice,
context, reference}. Scope default = project.

**Status:** COMPLETE. All four groups classified and migrated. 116 memories created in
the iwe2 vault (95 project + 21 global); 46 `.serena` duplicates dropped; JUNK distilled
and trashed; repo rewired to iwe2; originals trashed (Phases 0–5 all done).

## Group A — `.agents/memories/` root discipline/policy/handoff

| path | proposed_title | type | scope | disposition | promotion_candidate | distill_note | rationale |
|------|----------------|------|-------|-------------|---------------------|-------------|-----------|
| analysis-must-be-grounded.md | Analysis Must Be Grounded | advice | project | DURABLE | yes | — | Read real source before classifying; source-of-truth hierarchy. |
| backend-environment-notes.md | Backend Environment Notes | context | project | DURABLE | no | — | Concrete env facts for Indefinite.jl and ore_algebra builds. |
| bilinear-form-category-semantics.md | Bilinear Form Category Semantics | context | project | DURABLE | no | — | Durable lattice/bilinear-form/spec semantic definitions. |
| category-spec-architectural-boundary.md | Category Spec Architectural Boundary | context | project | DURABLE | no | — | Three-layer spec/plugin/stub boundary definition. |
| category-spec-constructor-routes-are-category-owned.md | Category Spec Constructor Routes Are Category Owned | decision | project | DURABLE | no | — | Settled category-owned constructor architecture. |
| category-spec-epistemic-foundation.md | Category Spec Epistemic Foundation | advice | project | DURABLE | yes | — | Core completion discipline: object before artifact. |
| category-spec-graph-minimality.md | Category Spec Graph Minimality | decision | project | DURABLE | no | — | super_categories must list immediate parents only. |
| category-spec-how-work-should-proceed.md | Category Spec How Work Should Proceed | advice | project | DURABLE | no | — | Three-problem-types workflow for spec mypy errors. |
| category-spec-interface-collisions-are-code-problems.md | Category Spec Interface Collisions Are Code Problems | trap | project | DURABLE | no | — | Same-name signature collisions are internal code problems. |
| category-spec-ledger-classification.md | Category Spec Ledger Classification | trap | project | DURABLE | no | — | Never trust bucket name/count/prior classification. |
| category-spec-mathematical-absurdities.md | Category Spec Mathematical Absurdities | trap | project | DURABLE | no | — | Catalog of concrete graph absurdities; still illustrative. |
| category-spec-methods-are-abstract.md | Category Spec Methods Are Abstract | decision | project | DURABLE | no | — | Spec methods are abstract obligations. |
| category-spec-methods-live-at-most-general-owner.md | Category Spec Methods Live At Most General Owner | decision | project | DURABLE | no | — | Methods belong at weakest mathematical owner category. |
| category-spec-no-stub-redeclaration.md | Category Spec No Stub Redeclaration | advice | project | DURABLE | no | — | Delete inherited re-declarations in subcategory specs. |
| category-spec-properties-witnesses-and-equipped-structure.md | Category Spec Properties Witnesses And Equipped Structure | decision | project | DURABLE | no | — | Property vs equipped-witness category distinction. |
| category-spec-refinement-category-declaration.md | Category Spec Refinement Category Declaration | decision | project | DURABLE | no | — | Refinement is declaration, not validation. |
| category-spec-repo-model-corrections.md | Category Spec Repo Model Corrections | context | project | DURABLE | no | — | False-vs-correct repo model table for spec semantics. |
| category-spec-root-bridge-vs-internal.md | Category Spec Root Bridge Vs Internal | decision | project | DURABLE | no | — | Binary boundary: only roots bridge to Sage. |
| category-spec-rotten-core-indicators.md | Category Spec Rotten Core Indicators | trap | project | DURABLE | no | — | Red-flag catalog for laundered/incomprehensible spec artifacts. |
| category-specs-sage-interop-is-a-design-constraint.md | Category Specs Sage Interop Is A Design Constraint | decision | project | DURABLE | no | — | Sage is feasibility witness, not adequacy standard. |
| category-spec-stub-classification-rule.md | Category Spec Stub Classification Rule | trap | project | DURABLE | no | — | Three banned stub-misclassification patterns plus autopsy. |
| category-spec-tests-use-category-api-not-private-classes.md | Category Spec Tests Use Category API Not Private Classes | advice | project | DURABLE | no | — | Tests use public category API, not private classes. |
| coble-and-moduli-claim-boundaries.md | Coble And Moduli Claim Boundaries | context | project | DURABLE | no | — | Stored Coble/K3 task facts and verification policy. |
| corrections-update-the-model-not-the-artifact.md | Corrections Update The Model Not The Artifact | advice | project | DURABLE | yes | — | Correction means model is wrong; fix model first. |
| current-goal-handoff.md | Current Goal Handoff | context | project | JUNK | no | Durable bit (typed Hom/morphism vocabulary need) already in repo-purpose memory. | Status snapshot of in-progress mapping pass. |
| diagnostics-are-navigation.md | Diagnostics Are Navigation | trap | project | DURABLE | yes | — | Diagnostics are pointers to read, not data to classify. |
| enriques-isotropic-gamma-orbits-paper-2302-01679.md | Enriques Isotropic Gamma Orbits Paper 2302 01679 | reference | project | DURABLE | no | — | Paper facts on Enriques cusp/orbit algorithm. |
| foundation-serves-research-not-itself.md | Foundation Serves Research Not Itself | advice | project | DURABLE | no | — | Foundation tasks justified only by mathematical use. |
| hard-problem-artifact-drift.md | Hard Problem Artifact Drift | trap | project | DURABLE | yes | — | Hard math triggers success-shaped artifact avoidance. |
| hermes/MEMORY.md | Hermes Memory | context | project | JUNK | no | Obsidian vault rules belong in vault-steward guidance, not this repo. | Hermes vault session state, foreign to lattice repo. |
| hermes/USER.md | Hermes User | context | project | JUNK | no | User vault prefs belong in user profile, not repo memory. | Hermes vault user-prefs, foreign to lattice repo. |
| index.md | Agent Memories | reference | project | JUNK | no | none — pure nav index, regenerable from vault structure. | Link index; superseded by iwe2 graph. |
| lattice-redesign-rules.md | Lattice Redesign Rules | decision | project | DURABLE | no | — | Redesign policy, dependency order, Sage integration contract. |
| lattice-research-stub-misclassification-following.md | Lattice Research Stub Misclassification Following | trap | project | DURABLE | no | — | Three ownership classes; stub-vs-plugin-vs-spec rule. |
| lattice-testing-and-semantics.md | Lattice Testing And Semantics | advice | project | DURABLE | no | — | Family-based math testing style; dual/discriminant semantics. |
| mathematical-narrative-test.md | Mathematical Narrative Test | advice | project | DURABLE | no | — | Implementation should read as mathematical narrative. |
| mathematical-sanity-check.md | Mathematical Sanity Check | advice | project | DURABLE | no | — | "Is this absurd?" gate before committing math code. |
| mathematical-source-report-memories.md | Mathematical Source Report Memories | advice | project | DURABLE | yes | — | Record external-source research findings durably. |
| mathematics-first-not-engineering-options.md | Mathematics First Not Engineering Options | advice | project | DURABLE | no | — | Name math objects before enumerating engineering fixes. |
| memory-management-discipline.md | Memory-Management Discipline | advice | project | DURABLE | yes | — | Memory is epistemic infrastructure; store invariants. |
| onboarding.md | Onboarding | context | project | DURABLE | no | — | Entry gate: repo purpose, phase, seven failure modes. |
| paperwork-is-a-routing-layer-not-progress.md | Paperwork Is A Routing Layer Not Progress | trap | project | DURABLE | yes | — | Cards/ledgers/plans are routing, not progress. |
| periodic-research-relevance-check.md | Periodic Research Relevance Check | advice | project | DURABLE | yes | — | Periodically recheck work advances mathematics. |
| plannotator-workflow.md | Plannotator Workflow | advice | project | DURABLE | no | — | Plannotator CLI plan-review workflow. |
| plugin-fixture-requirement.md | Plugin Fixture Requirement | advice | project | DURABLE | no | — | Required minimal-fixture form for plugin override red tests. |
| private-method-containers-are-not-return-types.md | Private Method Containers Are Not Return Types | trap | project | DURABLE | no | — | Private _*Methods classes are not public return types. |
| private-stubs-are-not-types.md | Private Stubs Are Not Types | trap | project | DURABLE | no | — | Private Sage stub containers are never valid types. |
| process-before-patches-policy.md | Process Before Patches Policy | advice | project | DURABLE | no | — | Embarrassing bug means fix process/tooling first. |
| provider-satisfaction-goal-contract.md | Provider Satisfaction Goal Contract | advice | project | JUNK | no | Durable model already in repo-model-corrections + refinement-category-declaration. | Legacy one-off goal state-machine contract. |
| provider-satisfaction-goal-state.md | Provider Satisfaction Goal State | context | project | JUNK | no | Corrected model duplicated in repo-model-corrections; rest invalidated task state. | Active task-state ledger for superseded goal. |
| provider-satisfaction-phase-source-reconstruction.md | Provider Satisfaction Phase Source Reconstruction | advice | project | JUNK | no | none — phase scaffolding for one cache-priming task. | One-off goal phase doc. |
| provider-satisfaction-phase-source-repair.md | Provider Satisfaction Phase Source Repair | advice | project | JUNK | no | none — banned-edit-shapes duplicated in repo-model-corrections. | One-off goal phase doc. |
| provider-satisfaction-phase-verification-review.md | Provider Satisfaction Phase Verification Review | advice | project | JUNK | no | none — review gate generic to state-machine skill. | One-off goal phase doc. |
| repo-purpose-mathematical-research-machine.md | Repo Purpose Mathematical Research Machine | context | project | DURABLE | no | — | Core statement: repo advances math research. |
| repo-understanding-is-agent-work.md | Repo Understanding Is Agent Work | trap | project | DURABLE | yes | — | Do not defer to "someone who understands the repo." |
| research-standardness-and-argument-standards.md | Research Standardness And Argument Standards | advice | project | DURABLE | yes | — | Standardness calibration and argument rules. |
| sage-axiom-binding-is-descriptor-binding.md | Sage Axiom Binding Is Descriptor Binding | decision | project | DURABLE | no | — | Axiom binding contract and banned cast patterns. |
| specs-do-not-contain-runtime-notimplemented-gaps.md | Specs Do Not Contain Runtime NotImplemented Gaps | trap | project | DURABLE | no | — | Abstract obligations stay abstractmethod. |
| stub-eligibility-test.md | Stub Eligibility Test | advice | project | DURABLE | no | — | Concrete decision test for sage-stubs eligibility. |
| subobjects-have-ambient-semantics.md | Subobjects Have Ambient Semantics | decision | project | DURABLE | no | — | Subobject self-predicates relative to ambient. |
| what-category-specs-actually-is.md | What Category Specs Actually Is | context | project | DURABLE | no | — | One-sentence purpose and structure of category_specs. |

## Group C — `.agents/memories/theory/**` + root `theory-*.md`

| path | proposed_title | type | scope | disposition | promotion_candidate | distill_note | rationale |
|------|----------------|------|-------|-------------|---------------------|-------------|-----------|
| theory/index.md | Theory Index | reference | project | DURABLE | no | — | Navigation hub for theory subtree. |
| theory/algorithms/index.md | Theory Algorithms Index | reference | project | DURABLE | no | — | Navigation index for algorithm memories. |
| theory/algorithms/buildings.md | Theory Algorithms Buildings | context | project | DURABLE | no | — | Source-backed Dawes building algorithm commentary. |
| theory/algorithms/dawes-nonisotropic-vector-orbits.md | Dawes Nonisotropic Vector Orbits | context | project | DURABLE | no | — | Source-backed Dawes Algorithms 2.1-2.3 with fixtures. |
| theory/algorithms/dawes-orbit-backend.md | Dawes Orbit Backend | advice | project | DURABLE | no | — | Implementation plan for non-isotropic orbit backend. |
| theory/algorithms/graph-automorphisms.md | Theory Graph Automorphisms | reference | project | DURABLE | no | — | GAP GRAPE/Digraphs automorphism method reference. |
| theory/algorithms/isotropic-gamma-orbit-backend.md | Isotropic Gamma Orbit Backend | advice | project | DURABLE | no | — | Implementation plan for isotropic Gamma-orbit backend. |
| theory/algorithms/monodromy-computations.md | Monodromy Computations | context | project | DURABLE | no | — | Source-backed monodromy tooling survey with code. |
| theory/algorithms/subgraph-orbits.md | Subgraph Orbits | reference | project | DURABLE | no | — | GAP subgraph enumeration/orbit method reference. |
| theory/backends/index.md | Theory Backends Index | reference | project | DURABLE | no | — | Navigation index for backend memories. |
| theory/backends/software-capability-map.md | Software Capability Map | reference | project | DURABLE | no | — | Routing map for mathematical software backends. |
| theory/backends/abstract-to-external-mapping.md | Abstract To External Mapping | reference | project | DURABLE | no | — | Repo method-to-external-tool mapping table. |
| theory/backends/oscar-lattices.md | Oscar Lattices | reference | project | DURABLE | no | — | Source-backed Oscar/Hecke lattice capability reference. |
| theory/backends/gap-orbits.md | Gap Orbits | reference | project | DURABLE | no | — | Tested GAP orbit/stabilizer call reference. |
| theory/backends/indefinite-jl.md | Indefinite Jl | reference | project | DURABLE | no | — | Indefinite.jl call reference with examples. |
| theory/backends/indefinite-isometry.md | Indefinite Isometry | reference | project | DURABLE | no | — | Verified upstream isometry routes plus local experiments. |
| theory/backends/carat.md | Carat | reference | project | DURABLE | no | — | CARAT capability audit and limitations. |
| theory/backends/buildings.md | Theory Backends Buildings | reference | project | DURABLE | no | — | buildings.sage class/method capability reference. |
| theory/backends/foliation-lib-reusable-procedures.md | Foliation Lib Reusable Procedures | reference | project | DURABLE | no | — | foliation.lib reusable Hodge procedure inventory. |
| theory/backends/library-integration.md | Library Integration | advice | project | DURABLE | no | — | Maps Coble tasks to existing library functions. |
| theory/backends/comprehensive-tool-docs.md | Comprehensive Tool Docs | reference | project | DURABLE | no | — | Extracted upstream tool docs for Coble project. |
| theory/backends/vinberg-algorithm.md | Theory Backends Vinberg Algorithm | advice | project | DURABLE | no | — | Vinberg algorithm implementation plan and references. |
| theory/foundations/index.md | Theory Foundations Index | reference | project | DURABLE | no | — | Navigation index for foundation memories. |
| theory/foundations/bilinear-forms-duals-morphisms.md | Bilinear Forms Duals Morphisms | context | project | DURABLE | no | — | Categorical bilinear-form/dual/morphism foundations. |
| theory-backend-routing.md | Theory Backend Routing | reference | project | DURABLE | no | — | Compact backend method-ownership routing store. |
| theory-source-routing.md | Theory Source Routing | context | project | DURABLE | no | — | Stored Coble/K3/Enriques claim facts with anchors. |
| theory-orbit-and-building-backends.md | Theory Orbit And Building Backends | reference | project | DURABLE | no | — | Compact orbit/building implementation routing store. |
| theory-graph-monodromy-hodge-methods.md | Theory Graph Monodromy Hodge Methods | reference | project | DURABLE | no | — | Compact graph/monodromy/Hodge method routing store. |
| theory/external/dutsik_polyhedral/.../notes/indefinite_methods.md | Polyhedral Common Indefinite Methods | reference | project | DURABLE | no | — | Repo-specific synthesis: indefinite method decision guide. |
| theory/external/dutsik_polyhedral/** (15 other files) | Polyhedral Common Reference | reference | project | JUNK | no | Fold all 15 vendored upstream docs into ONE polyhedral-common reference memory (method families + tool pointer). | Vendored external repo docs — belong as a single source pointer. |

Note: the 15 dutsik files collapse to one consolidated `reference` memory plus the
preserved `indefinite_methods` synthesis. The per-file `index.md`/`README.md` stems
collide; consolidation avoids the slug-collision problem entirely.

## Group B — `.agents/memories/skills/**`

All DURABLE except `request-triager.md`. Titles path-qualified to avoid slug collisions
on generic body stems (workflow, subtrees, code-style, …). 11 pointer+body pairs MERGE
into one memory each (pointer `skills/NAME.md` + body `skills/NAME/*.md`).

| path | proposed_title | type | scope | disposition | promotion_candidate | distill_note | rationale |
|---|---|---|---|---|---|---|---|
| skills/category-framework-design.md | Category Framework Design | advice | project | DURABLE | no | — | pointer; MERGE with category-framework-design/* bodies |
| skills/category-framework-design/autset-categories-path.md | Category Framework Design Autset Categories Path | reference | project | DURABLE | no | — | Sage endset/autset source map; merge into parent |
| skills/category-framework-design/autset-integration-plan.md | Category Framework Design Autset Integration Plan | decision | project | DURABLE | no | — | settled autset axiom integration; merge into parent |
| skills/category-framework-design/axioms-with-generators-finitely-presented.md | Category Framework Design Axioms With Generators | reference | project | DURABLE | no | — | Sage axiom-hierarchy source map; merge into parent |
| skills/category-framework-design/category-creation-notes.md | Category Framework Design Category Creation Notes | reference | project | DURABLE | no | — | Sage base-ring/module source map; merge into parent |
| skills/category-framework-design/category-refinement-phases.md | Category Framework Design Refinement Phases | advice | project | DURABLE | no | — | phased static-spec-first workflow; merge into parent |
| skills/category-framework-design/homsets-structural-core.md | Category Framework Design Homsets Structural Core | reference | project | DURABLE | no | — | Sage Homsets/dual/rank source map; merge into parent |
| skills/category-spec-audit.md | Category Spec Audit | advice | project | DURABLE | no | — | category-spec review/audit discipline |
| skills/category-spec-complexity-rubric.md | Category Spec Complexity Rubric | advice | project | DURABLE | no | — | complexity scoring rubric for cards |
| skills/category-spec-failed-assertion-classification.md | Category Spec Failed Assertion Classification | advice | project | DURABLE | no | — | classify failed category-obligation assertions |
| skills/category-spec-planning.md | Category Spec Planning | advice | project | DURABLE | no | — | plan/decomposition rules + anti-trigger |
| skills/category-spec-priority-rubric.md | Category Spec Priority Rubric | advice | project | DURABLE | no | — | priority scoring rubric for cards |
| skills/category-spec-retirement.md | Category Spec Retirement | advice | project | DURABLE | no | — | card retirement procedure |
| skills/category-spec-sage-mapping.md | Category Spec Sage Mapping | advice | project | DURABLE | no | — | Sage-name-to-math-owner mapping workflow |
| skills/category-spec-subtrees.md | Category Spec Subtrees | advice | project | DURABLE | no | — | pointer; MERGE with category-spec-subtrees/subtrees |
| skills/category-spec-subtrees/subtrees.md | Category Spec Subtrees Ownership | decision | project | DURABLE | no | — | settled subtree ownership map; merge with pointer |
| skills/category-spec-triage.md | Category Spec Triage | advice | project | DURABLE | no | — | PM triage routing for category-spec cards |
| skills/category-spec-visuals.md | Category Spec Visuals | advice | project | DURABLE | no | — | visual-artifact routing policy |
| skills/category-spec-workflow.md | Category Spec Workflow | advice | project | DURABLE | no | — | pointer; MERGE with category-spec-workflow/workflow |
| skills/category-spec-workflow/workflow.md | Category Spec Workflow Reference | advice | project | DURABLE | no | — | canonical category-spec PM workflow; merge with pointer |
| skills/creating-fixtures.md | Creating Fixtures | advice | project | DURABLE | yes | — | fixtures-as-oracles discipline; reusable |
| skills/lattice-redesign.md | Lattice Redesign | advice | project | DURABLE | no | — | pointer; MERGE with lattice-redesign/* bodies |
| skills/lattice-redesign/category-abc-spec.md | Lattice Redesign Category ABC Spec | decision | project | DURABLE | no | — | ModulesWithForms category contract; merge into parent |
| skills/lattice-redesign/lattice-interface-style-guide.md | Lattice Redesign Interface Style Guide | advice | project | DURABLE | no | — | lattice public-API doctrine; merge into parent |
| skills/lattice-redesign/lattice-redesign-corrections-spec.md | Lattice Redesign Corrections Spec | context | project | DURABLE | no | — | verbatim user corrections artifact; merge into parent |
| skills/opencode-one-shot-workers.md | Opencode One Shot Workers | advice | project | DURABLE | yes | — | reusable cheap-parallel-worker delegation discipline |
| skills/request-triager.md | Request Triager | advice | project | JUNK | no | none | generic PM/RICE/Linear boilerplate, off-domain |
| skills/research-code-style/code-style.md | Research Code Style | advice | project | DURABLE | yes | — | canonical mathematical-prose code-style (body-only) |
| skills/research-co-mathematician-workflow.md | Research Co Mathematician Workflow | advice | project | DURABLE | yes | — | pointer; MERGE with .../architecture |
| skills/research-co-mathematician-workflow/architecture.md | Research Co Mathematician Workflow Architecture | advice | project | DURABLE | yes | — | workspace/workstream model; merge with pointer |
| skills/research-math-boundary.md | Research Math Boundary | advice | project | DURABLE | no | — | pointer; MERGE with .../math-boundary |
| skills/research-math-boundary/math-boundary.md | Research Math Boundary Reference | advice | project | DURABLE | no | — | trusted-vocabulary/backend-routing; merge with pointer |
| skills/research-planning-cleanup.md | Research Planning Cleanup | advice | project | DURABLE | yes | — | meta-review for shallow-work detection |
| skills/research-project-workflow.md | Research Project Workflow | advice | project | DURABLE | yes | — | pointer; MERGE with .../project-workflow |
| skills/research-project-workflow/project-workflow.md | Research Project Workflow Reference | advice | project | DURABLE | yes | — | canonical Nimbalyst PM workflow; merge with pointer |
| skills/research-proof-auditing.md | Research Proof Auditing | advice | project | DURABLE | yes | — | pointer; MERGE with .../proof-auditing |
| skills/research-proof-auditing/proof-auditing.md | Research Proof Auditing Reference | advice | project | DURABLE | yes | — | proof/fraud failure-mode taxonomy; merge with pointer |
| skills/research-repo-structure.md | Research Repo Structure | advice | project | DURABLE | no | — | pointer; MERGE with .../repo-structure |
| skills/research-repo-structure/repo-structure.md | Research Repo Structure Reference | advice | project | DURABLE | no | — | directory-placement authority; merge with pointer |
| skills/research-scheduling.md | Research Scheduling | advice | project | DURABLE | yes | — | pointer; MERGE with .../cadence |
| skills/research-scheduling/cadence.md | Research Scheduling Cadence | advice | project | DURABLE | yes | — | scheduling/wakeup cadence policy; merge with pointer |
| skills/research-source-acquisition.md | Research Source Acquisition | advice | project | DURABLE | yes | — | theory-source acquisition + citation workflow |
| skills/sage-category-source-maps.md | Sage Category Source Maps | reference | project | DURABLE | no | — | pointer; MERGE with sage-category-source-maps/* bodies |
| skills/sage-category-source-maps/ring-integration.md | Sage Category Source Maps Ring Integration | reference | project | DURABLE | no | — | Sage ring-constructor source map; merge into parent |
| skills/sage-category-source-maps/set-spec.md | Sage Category Source Maps Set Spec | reference | project | DURABLE | no | — | Sage set-category source map; merge into parent |
| skills/vinberg-algorithm.md | Vinberg Algorithm | advice | project | DURABLE | no | — | routing/boundaries; points to theory/backends body |

## Group D — `.serena/memories/**` dedup

46 files are pure DUPLICATE (condensed subsets of the `.agents` canonical) → DROP, no
fold-in needed. Only 6 UNIQUE files migrate.

| serena_path | relationship | type | scope | disposition | proposed_title | rationale |
|---|---|---|---|---|---|---|
| category-spec-predicate-policy.md | UNIQUE | advice | project | DURABLE | Category Spec Predicate Policy | is_*/has_* predicates must be @abstractmethod |
| completion_checklist.md | UNIQUE | advice | project | DURABLE | Completion Checklist | planning/spec completion checklist |
| project_overview.md | UNIQUE | context | project | DURABLE | Project Overview | repo orientation: Coble program, durable roots |
| style_and_workflow.md | UNIQUE | advice | project | DURABLE | Style And Workflow | source-ground specs, needs-review gate |
| suggested_commands.md | UNIQUE | reference | project | DURABLE | Suggested Commands | command cheatsheet |
| skills/category-spec-smoke-triage.md | UNIQUE | advice | project | DURABLE | Category Spec Smoke Triage | smoke-frontier triage routing rules |
| (46 others) | DUPLICATE | — | — | DROP | — | condensed subset of .agents canonical |

## Summary & totals

- **DURABLE → migrate:** ~88 memories (Group A 57, Group C 28+1, Group B 45, Group D 6),
  reduced to ~77 distinct iwe2 memories after the 11 skill pointer+body merges.
- **JUNK → distill-then-trash (Phase 2):**
  - `current-goal-handoff.md` — *flagged for user decision* (live cold-start handoff, see below).
  - `provider-satisfaction-*` (5 files) — superseded goal state-machine; durable model already in repo-model-corrections.
  - `hermes/MEMORY.md`, `hermes/USER.md` — foreign Hermes/Obsidian vault state (*flagged*).
  - `index.md` — nav index, regenerable by iwe2.
  - `skills/request-triager.md` — off-domain PM boilerplate.
  - `theory/external/dutsik_polyhedral/**` (15 files) — vendored upstream docs → fold into ONE consolidated `polyhedral-common` reference; keep `notes/indefinite_methods.md`.
- **DUPLICATE → drop:** 46 `.serena` condensed copies.

### Judgment calls — RESOLVED by user
1. **`current-goal-handoff.md`**: **distill-then-trash** (user choice). Durable bit (typed
   Hom/morphism vocabulary need) is already in repo-purpose memory → nothing new to migrate;
   trash the file and drop the AGENTS.md step-2 / GOAL.md:230 handoff reference in Phase 4.
2. **`hermes/MEMORY.md` + `hermes/USER.md`**: **migrate to global scope** (user choice).
   MEMORY → `global/reference` (Obsidian vault facts, NIM API, script inventory);
   USER → `global/advice` (how the user wants agents to work).
3. **Promotions to global** (user choice — promote the genuinely cross-project ones):
   - Group A → global: analysis-must-be-grounded, corrections-update-the-model-not-the-artifact,
     diagnostics-are-navigation, hard-problem-artifact-drift, mathematical-source-report-memories,
     memory-management-discipline, paperwork-is-a-routing-layer-not-progress,
     periodic-research-relevance-check, repo-understanding-is-agent-work,
     research-standardness-and-argument-standards.
   - Group B skills → global: creating-fixtures, opencode-one-shot-workers, research-code-style,
     research-co-mathematician-workflow, research-planning-cleanup, research-project-workflow,
     research-proof-auditing, research-scheduling, research-source-acquisition.
   - **Kept project despite the yes flag:** category-spec-epistemic-foundation
     (category-spec-specific, not cross-project).

### Execution mechanics
- `iwe2 add` writes a vault git commit per call → run adds **sequentially** (deterministic
  script `reports/migrate_memories.py`), not via concurrent subagents (git-race + math
  transcription risk). Strip leading YAML frontmatter from each source before `--content`.
- **11 merge groups** (skill pointer `skills/NAME.md` + body `skills/NAME/*.md`) → one
  memory each, body = concatenated sources under the pointer's title.
- **dutsik consolidation**: 15 vendored upstream docs → one new `polyhedral-common`
  reference (subagent-synthesized); keep `notes/indefinite_methods.md` as its own memory.
- **Link fix**: after all adds, rewrite `mem:<oldkey>` references to new vault keys.

