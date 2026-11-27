---
id: TASK-1777748120529-YQJMY7-SPLIT-MIXED-SET-CONSTRUCTOR-INPUT-SHAPES-INTO-NAMED-ALTERNATIVES
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Split mixed set-constructor input shapes into named alternatives
status: complete
priority: high
complexity: 56
description: Split mixed set-constructor input shapes into named alternatives
successCriteria:
- Split mixed set-constructor input shapes into named alternatives is resolved according
  to the body acceptance criteria.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Split mixed set-constructor input shapes into named alternatives
Source: pasted backlog 2026-05-02.

Task: split the mixed input shapes on set constructors (objects, collection, and single object) into explicit alternatives using @overload.

## Grounding

- Source provenance: recovered variadic sprint source at
  `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` in commit
  `8d1c21c^`; current phase card
  `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT.md`; Sage set inventory
  `category_specs/sets/docs/SAGE_INVENTORY.md`; tracked set mapping spec
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md`.
- Style authority: `.agents/skills/category-spec-style/references/style.md`
  requires non-variadic public constructor surfaces, explicit overloads for finite
  Sage casework, and no software-shaped helper types.
- Sage grounding:
  - `sage.sets.set.Set(X, category=None)` accepts existing Sage category objects,
    finite iterable collections, and other iterable/wrapper cases; it rejects Sage
    elements without a defined underlying set. The project mapping explicitly rejects
    this generic wrapper as a public constructor.
  - `Set(X)` collection behavior is recovered by
    `Sets().Constructors().from_iterable(elements)` and
    `FiniteEnumeratedSet(elements)`.
  - A single element determines the singleton finite set `{x}`; this is a named
    finite-enumerated construction, not the generic Sage wrapper.
  - Existing set objects already lie in `Sets()` and must not be wrapped merely to
    satisfy a constructor call shape.
  - Fixed-base set-partition constructors still expose collapsed base-set shapes:
    a set object, an iterable collection of elements, or an integer cardinality for
    the standard totally ordered finite base `{1, ..., n}`.
- Mathematical owner: `Sets().Constructors()` owns named set-entry constructors;
  `Sets().Partitioned()` owns the fixed-base set-partition result surface.
- Return objects: finite iterable and singleton inputs return finite countable set
  objects; fixed-base partition constructors return `SetPartitionSet`; integer
  fixed-base inputs additionally refine through
  `Sets().Partitioned().FiniteTotallyOrderedBase()`.

## Acceptance Criteria

- [x] Do not admit a catch-all project `Set(X)` constructor.
- [x] Preserve existing finite-collection behavior through
  `from_iterable(elements)` and `FiniteEnumeratedSet(elements)`.
- [x] Add or preserve a named singleton finite-set path for a single element.
- [x] Split fixed-base set-partition constructor signatures into explicit overloads
  for set object, finite iterable collection, and integer cardinality inputs.
- [x] Keep implementations closed over the admitted cases and avoid `*args`,
  `**kwargs`, or duck-typed wrapper admission.
- [x] Add category-obligation example or regression coverage using small finite examples.
- [x] Run syntax/category-obligation example validation, or record the exact phase-local blocker.
- [x] Run and record a spec-weakening review before moving the card to
  `needs-agent-review`.

## Complexity And Ownership

- Owner: category-spec set constructor implementation agent.
- Complexity: 56, Moderate (41-60).
- Complexity band: Moderate (41-60).
- Why this specific score:
  - The task touches multiple constructor overload surfaces for set creation, which is broader than a single method edit but still bounded to API typing. The complexity is moderate because behavior should remain same while call-shape space is decomposed, requiring careful static compatibility checks.
- Item-specific evidence:
  - The source-backed scope is limited to set constructor entry points in
    `category_specs/sets/__init__.py`, set category-obligation example/regression coverage, and this card.
  - The work does not change method ownership or admit a new wrapper category.
  - The main coupling risk is preserving Sage-compatible fixed-base partition
    construction while making the public signatures explicit.

## Work Log

- 2026-05-06: Began execution. Grounded the vague migrated card against Sage `Set`
  source, the set inventory, the tracked set mapping spec, and the category-spec
  style rules. Scoped implementation to named alternatives and fixed-base
  set-partition overloads, not to a generic `Set(X)` wrapper.
- 2026-05-06: Added `Sets().Constructors().SingletonSet(element)` as the named
  singleton finite-set path, documented it in `SPEC-MAPPING-SETS.md`, and added
  category-obligation example coverage with a small integer witness.
- 2026-05-06: Added explicit `@overload` declarations for
  `SetPartitions`, `SetPartitionsWithBlockCount`, and
  `SetPartitionsWithBlockSizes` for set-object, finite-iterable, and integer
  cardinality base inputs. The initial runtime implementation still delegated the
  broad mixed union to Sage; this was corrected by the 2026-05-07 rework below.
- 2026-05-07: Gate 2 review found that the overload declarations were still backed
  by broad mixed-union bodies delegating directly to Sage. Reworked the runtime path
  so fixed-base set-partition constructors first dispatch through a closed helper
  over the three admitted cases: Sage integer cardinality, categorical set object,
  or finite iterable materialized as a tuple.

## Validation

- `python -m py_compile category_specs/sets/__init__.py` passed.
- `git diff --check -- category_specs/sets/__init__.py category_specs/sets/category_obligations.sage plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-1777748120529-YQJMY7-SPLIT-MIXED-SET-CONSTRUCTOR-INPUT-SHAPES-INTO-NAMED-ALTERNATIVES.md` passed.
- `just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage` passed,
  with the pre-existing Sage warning about `Sets.Topological` not subclassing
  `CategoryWithAxiom`.
- 2026-05-07 rework validation:
  - `python -m py_compile category_specs/sets/__init__.py` passed.
  - `git diff --check -- category_specs/sets/__init__.py` passed.
  - `just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage` passed,
    with the same pre-existing Sage warning about `Sets.Topological` not subclassing
    `CategoryWithAxiom`.

## Spec-Weakening Review

- Reviewed the task-local diff for generic `Set(X)` admission, deleted abstract
  methods, removed constructor obligations, narrowed category assertions, and
  Sage-gap-driven interface shrinkage.
- Result: passed. The diff preserves the `Set(X)` rejection, adds the named
  singleton surface, and adds overload declarations without removing obligations.

## Review Log

### Independent Review - 2026-05-07 (fresh-context subagent)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance

**Gates failed:** none

**Outcome:** complete. All six gates pass with concrete falsifiable evidence.

#### Gate 1: Definition Grounding — PASSED

Evidence:
- Card lines 28-36 cite VARIADIC_SIGNATURE_INVENTORY.md (commit 8d1c21c^), phase card, SAGE_INVENTORY.md, SPEC-MAPPING-SETS.md — all confirmed.
- Style authority `.agents/skills/category-spec-style/references/style.md` requires non-variadic surfaces, explicit overloads — confirmed.
- Sage grounding: `sage.sets.set.Set(X)` behavior cited; `Set(X)` rejected as public constructor; named paths enumerated.
- Mathematical owner: `Sets().Constructors()` for named set-entry constructors; `Sets().Partitioned()` for fixed-base partitions. Confirmed in `__init__.py`.
- Return objects: SingletonSet → FiniteSet, SetPartitions → SetPartitionSet, integer → plus FiniteTotallyOrderedBase refinement.

#### Gate 2: Acceptance Criteria — PASSED

- AC1: No catch-all `Set(X)` constructor. All construction through named methods.
- AC2: `from_iterable(elements)` and `FiniteEnumeratedSet(elements)` preserved. Category-obligation example lines 73-116 verify.
- AC3: `SingletonSet(element)` at `__init__.py:541-543`. Category-obligation example lines 118-120 verify.
- AC4: SetPartitions, SetPartitionsWithBlockCount, SetPartitionsWithBlockSizes each have 3 explicit `@overload` declarations.
- AC5: `_set_partitions_base` dispatches over exactly 3 cases: SageInteger, CategoryObject in Sets(), Iterable. Other types raise TypeError. Zero `*args`/`**kwargs`.
- AC6: Category-obligation example lines 490-515 cover all 3 constructors × 3 input shapes.
- AC7: `python -m py_compile` passed. `just category-obligation-file sets/category_obligations.sage` passed.
- AC8: Spec-weakening review section in card confirms passed.

#### Gate 3: Spec-Weakening — PASSED

Examined `git diff 07e7d85^..1599059`. No abstract methods removed. No constructor obligations deleted. Category-obligation example file grew from ~50 to ~100+ statements (positive growth). No Sage-gap-driven interface shrinkage. SPEC-MAPPING-SETS.md gained rows (computable-sets section, singleton constructor), lost none.

#### Gate 4: Gradient — PASSED

All decided decisions checked: `DECISION-01KQN9YGCTP85RXF1F56D8S08X` (reject generic Set(X)) is preserved. No contradiction. No previously passing category-obligation example regressed. Git history shows additive commits only.

#### Gate 5: Mathematical Correctness — PASSED

- `python -m py_compile` passed.
- `just category-obligation-file sets/category_obligations.sage` passed (pre-existing Sets.Topological warning only).
- `git diff --check` passed.
- SingletonSet(element) = `FiniteEnumeratedSet((element,))` — correct for `{x}`.
- `_set_partitions_base` dispatch: SageInteger→{1,...,n}, CategoryObject in Sets→object itself, Iterable→tuple — all correct.
- SetPartitions overloads route through `_set_partitions_base` then SageSetPartitions, refining through Sets().Partitioned().

#### Gate 6: Style and Compliance — PASSED

- No `ConditionSet`, no variadic option bags. `@overload` pattern used correctly.
- No `*args`/`**kwargs`. Types from `types.py` (Set, Integer, SetPartitionSet).
- `@final` on all public Constructors methods.
- Commit messages follow Conventional Commit format.
- No AI-slop patterns.
