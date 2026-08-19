# Current Goal Phase

Current phase: category-spec and semantic-vocabulary phase.

This file is the repo-local phase marker for the staged plan in `GOAL.md`. Agents use
it to avoid drifting into downstream work before the prerequisite mathematical language
exists.

The operative staged-program source is `GOAL.md`. Do not mirror the staged program as a
tracker feature; active tracker cards start at concrete deliverable features under
`.agents/plans/features/`.

## Active phase

The repo is currently in the spec phase.

Frame the spec phase as: define the mathematically natural category/refinement
structure needed by the Coble/K3 lattice research, grounded by Sage/source inventories.
The phase is not "only specify what Sage already implements" and not "write an ideal
API detached from realization."

Current phase plan:

The plan paths below are tracker addresses, not mathematical descriptions of the work.
Several historical IDs still contain terms such as "surface" or "admission"; those
names must not determine routing. The live object is the source-backed mathematical
operation claim: Sage behavior is read first, then translated into an operation under
hypotheses, the weakest category/refinement where it is defined, required witnesses,
codomain or return object, and source evidence. The operation-map document records
those claims; it is not itself the mathematical object of progress.

- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SPEC-CORE-VERTICAL-SLICE/PLAN-SPEC-CORE-VERTICAL-SLICE.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-SPEC-PROGRAM/PLAN-CATEGORY-SPEC-PROGRAM.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-FOUNDATION-KERNEL/PLAN-CATEGORY-FOUNDATION-KERNEL.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-STATIC-CATEGORY-REFINEMENT-ORDER/PLAN-STATIC-CATEGORY-REFINEMENT-ORDER.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION/PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-OBLIGATION-EXAMPLES/PLAN-CATEGORY-OBLIGATION-EXAMPLES.md`
- `.agents/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/FEATURE-MODULES-WITH-FORMS-AND-LATTICES.md`
- `.agents/plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/FEATURE-GEOMETRY-CATEGORY-INTERFACES.md`

Primary work:

- Recover the mathematically natural interface from the later pipeline: free modules,
  formed modules, lattices, Hom/End/Aut, lattice isometry groups `O(L)`, discriminant
  forms, orthogonal complements, embeddings, typed pullbacks, stabilizers,
  centralizers, and orbit sets.
- Discover Sage constructors, methods, classes, categories, coercions, canonical maps,
  return objects, and documented or runtime-observed limitations for each mathematical
  family under consideration.
- Translate Sage behavior into category/refinement membership and witness data. An
  object of `Groups` has group structure; an object of `FinitelyGeneratedGroups` has
  finite-generation structure and a generating-set witness; an object of
  `FinitelyPresentedGroups` has finite-presentation structure; an explicitly generated
  subgroup carries its generators as construction data.
- Decide category ownership for each operation at the highest mathematically valid
  layer. For example, deterministic enumeration belongs first to countable
  sets/products/free modules before becoming lattice-local bounded-vector search, and
  form-preserving maps belong to modules with forms or lattices rather than arbitrary
  modules.
- Produce specs sufficient for the lattice-theoretic layer: discriminant forms,
  primitive embeddings, orthogonal complements, local invariants, base change,
  Nikulin-style criteria, isometry groups, stabilizers, centralizers, and orbit objects,
  with stronger algorithmic methods placed only on stronger categories or constructions.
- Advance by vertical examples:
  mathematical need -> Sage inventory -> category/refinement claim -> required witness
  or proof obligation -> check/report.
- Continue the handoff's concrete source-backed mapping target unless the latest user
  directive names a broader correction. The lattice Hom/morphism block has split
  theorem-shaped rows; the next ordinary lattice mapping target is the remaining
  non-Hom method clusters after that block.
- Create and audit category specs extending Sage's category layer.
- Establish uniform semantic vocabulary for sets, modules, Hom/End/Aut objects, modules
  with forms, lattices, and later scheme/variety interfaces without falsely refining
  canonical objects into finite-generation, finite-presentation, finite, or enumerable
  categories.
- Research Sage and open-source backend capabilities needed to support those specs.
- Create plans and cards for implementation gaps discovered during spec work.
- Preserve mathematical intent in docs that can be reviewed by mathematicians.
- Treat broad category expansion, global QC cleanup, and broad category-obligation repair as
  non-goals unless they directly change source-backed mathematical operation claims or
  correct a false steering claim in an entrypoint.

Blocked by default:

- Downstream Coble experimental research.
- Ad hoc lattice, matrix, polynomial, orbit, or group computations.
- Attempts to prove Coble claims before the lattice/category vocabulary exists.
- Complete redesigns of Sage, full algebraic-geometry library work, arbitrary
  concrete-method catalogs, or general Sage ergonomics unrelated to the Coble/K3
  lattice pipeline.
- False refinements, such as treating `Aut(L)` or `O(L)` as a finitely generated,
  finitely presented, finite, explicitly generated, or fully enumerable group without
  the required proof, construction, Sage support, backend support, or witness data.
- Generator, presentation, orbit-enumeration, Vinberg-chamber, Coxeter-parabolic, or
  hyperbolic-lattice group algorithms when no category/refinement claim justifies those
  obligations.
- QC-driven code cleanup unrelated to an approved phase transition or implementation card.
- Rolling back formatter, linter, or hook auto-fixes.

These defaults block only attempts to do that downstream or unrelated work. They do not
block phase-01 spec execution, source mining, audit drafting, decision capture, or
decomposition under approved phase-01 plans.

## Phase dependency

Each stage in `GOAL.md` blocks the next. It is pointless to attempt Coble research before
there is a lattice spec capable of semantically expressing objects such as
`Pic(S)`, lattice isometry types, discriminant forms, Hom spaces, and pullback/pushforward
maps.

Raw computations do not satisfy the project goal. A 21-by-21 matrix calculation that is
not expressed through reviewed mathematical objects, typed morphisms, vetted algorithms,
and source-backed semantics is not a result for this project. It is exploratory scratch
at best and should not be promoted as evidence.

The practical success condition for this phase is source-grounded sufficiency for the
research pipeline: an implementation agent can build the category/spec layer without
inventing the mathematics or claiming false refinements, because the objects,
morphisms, ownership boundaries, category memberships, witness data, hypotheses, Sage
bridge points, backend evidence, and known gaps are already stated at the
mathematical level.

## QC policy

QC is required for phase transitions and commit-integrated implementation work so
quality debt cannot be forgotten indefinitely.

QC is not the controlling activity during churn-heavy spec work. Specs undergo human/LLM
planning, audit, review, and rewrite before settling. During the spec phase, agents
should not chase incidental QC failures or hook noise unless the user explicitly asks
for QC work or the repo is being prepared for a phase transition.

If QC, implementation validation, or a downstream research guard fails during ordinary
spec work, record the finding in the appropriate card/TODO/decision only when durable
tracking is needed, then continue another approved active spec leaf.

When a phase transition is proposed, QC becomes mandatory for the affected committed
implementation under review. Passing QC is evidence for moving between phases; it is not a
substitute for mathematical review.

## Auto-fix policy

Auto-fixes produced by hooks, formatters, linters, or other tooling are carried forward.
Do not roll them back, undo them, or "restore" pre-fix formatting. If auto-fixes touch
unexpected files, report the tool and paths and let the user decide the follow-up.
