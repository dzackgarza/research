# STATUS decisions review plan

Review target: the replacement state for `STATUS.md`.

The current repo state treats the `STATUS.md` items as workflow classification, not
as a questionnaire. Source-forced facts and routine tracker cleanup are agent work.
Human input is reserved for owner-level conventions or phase overrides that remain
after source review, repo policy, and the dependency graph have been checked.

## Current Policy State

Human-facing Plannotator reports are now forward-facing artifacts. They should state
the current classification, source basis, consequence, and next action. They should
not back-explain prior agent failures, list bare source paths without explaining their
content, or tell the user what answer shape to provide.

`needs-human-input` is now reserved for real human judgment. The controlling policy is
that source-forced mathematical facts, fixable plan/card debris, and ordinary planned
dependency order are not user decisions. If a card cannot start because vocabulary,
source grounding, implementation surface, or theory prerequisites are incomplete, the
card stays `unstarted` with `dependsOn`; it is not marked as waiting for human input.

Constructor-placement reports now separate three layers. The mathematical owner is
the category or object whose structure defines the constructor. The human convention
is where users should expect a named object when several structures apply. The
code-maintenance owner is where implementation should live for readability,
aggregation, and duplicate avoidance. Aggregate entry points such as
`Cat().Constructors()` can be the canonical user-facing surface even when concrete
implementations live on more specific owners.

The active phase gate remains strict. `GOAL.md` and `.agents/current-goal-phase.md`
make the current work category-spec and semantic-vocabulary work. Downstream Coble
orbit/lifting work waits until the category, lattice, discriminant-form, and geometry
vocabulary can express it without ad hoc raw computations.

## Current Tracker State

| Surface | Classification | Current state | Next action |
| --- | --- | --- | --- |
| Tensor-product lifting | Source-forced tensor-product vocabulary. The pure-product-to-tensor element map is a tensor-product parent operation inherited by tensor algebra components; component storage is not a separate mathematical owner. | `TASK-1777748120751-VP7D5V-FIX-TENSOR-COMPONENT-PLACEHOLDER-METHODS-AND-TYPE-LEAKS` is `needs-review`. | Review the completed cleanup evidence for placeholder removal and raw Sage type-leak avoidance. |
| Algebra constructor boundary | Source-forced constructor routing plus scoped audit cleanup. Rings/fields such as `Zmod`, cyclotomic fields, and number fields are not public algebra constructors merely because they may carry algebra structure. | `TASK-1777748120716-ZUYAHM-MOVE-NONTRIVIAL-ALGEBRA-CONSTRUCTION-OUT-OF-CATEGORY-CONSTRUCTORS` is `needs-review`. | Review the owner boundary; create a separate cross-subtree audit only if review finds a concrete leak outside this card. |
| Static category refinement order | Agent-owned source-grounding work. `super_categories()` edges must be true mathematical/category edges with source basis; dead links, partial citation rows, and contradictory rows are maintenance defects. | `PLAN-STATIC-CATEGORY-REFINEMENT-ORDER` is `in-progress`. | Audit current `super_categories()` returns and record source basis or file exact ambiguity cards. |
| Smoke/audit stabilization | Agent-owned plan maintenance. Dead links, inventory mismatch, and circular self-dependency are not owner decisions. | `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION` is `in-progress`. | Repair the concrete plan/card inconsistencies, then surface only any remaining audit-governance convention. |
| Varieties category | Source-forced geometry vocabulary. `Varieties(k)` follows the scheme-theoretic convention: integral, separated, finite type over a field. Backend adapters must verify hypotheses rather than trust broad backend names. | `TASK-INTEGRATE-VARIETIES-CATEGORY` is `needs-review`. | Review the source-admitted geometry vocabulary and backend naming warning. |
| Coble isotropic orbit enumeration | Real downstream research, not a current-phase human deferral. It requires discriminant-form, TCO, category, module-with-form/lattice, and geometry prerequisites. | `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` is `unstarted` with explicit `dependsOn`. | Do not run Coble orbit computations in the current category-spec phase. |
| Coble lifting theorem verification | Real downstream research, not a current-phase human deferral. It depends on orbit enumeration plus the same vocabulary and theory prerequisites. | `SPEC-COBLE-LIFTING-THEOREM-VERIFICATION` is `unstarted` with explicit `dependsOn`. | Do not attempt theorem verification until prerequisite vocabulary and source-backed lattice surfaces exist. |

## Validation State

`just plan-validate` now validates 251 root planning cards.

`just plan-progress-report` regenerated `plans/card-progress-report.md` after the
state changes.

`STATUS.md` has been retired. The active source of truth is now the policy surface,
the tracker cards, the dependency graph, and the generated planning report.

## Review Question

The default next action is to continue agent-owned cleanup and review through the
cards above while keeping downstream Coble work phase-gated.

The only owner-level override still visible here is whether to intentionally pull
Coble theory preparation forward despite the active category-spec phase gate. Without
that override, the repo should proceed from the current tracker state.
