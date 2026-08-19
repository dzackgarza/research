---
id: FEATURE-QC-WARNINGS-ZERO
trackerStatus:
  type: feature
parents: []
dependsOn: []
plans:
- '[[PLAN-QC-MYPY-FOUNDATION-ORDER]]'
title: Zero QC warnings — repo-wide QC gate
status: in-progress
priority: critical
description: 'Eliminate all blocking QC findings across the repo so that `just test`
  from the global QC authority passes cleanly. This is a mandatory gate: no further
  feature work (spec, implementation, research, Coble) proceeds until QC is clean. The
  mypy cleanup order is basic typing hygiene first, dynamic-inheritance plugin review
  second, stub generation third, and downstream type cleanup last.

  '
---
# Feature: Zero QC Warnings

## Summary

The global QC stack (`just test` from `/home/dzack/ai/quality-control/justfile`)
currently reports 4 blocking failures across the research repo: mypy (1,720
errors), ruff (612 errors), black (13 files), and semgrep (14 findings). Per
`AGENTS.md` policy, QC findings are mandatory and not advisory — they are
defects in the repo.

This feature gates all further work (spec, implementation, research, Coble) until
`just test` passes with zero findings. Its mypy work is ordered by
`PLAN-QC-MYPY-FOUNDATION-ORDER`; do not treat aggregate mypy output as one queue.
The first selectable work is basic annotation, `Any`, fixture, and ordinary code
hygiene. The Sage mypy plugin is a later dynamic-inheritance lane, and stub
generation is later still.

## Source Provenance

- `AGENTS.md`: "QC findings are mandatory, not advisory."
- `GOAL.md`: Phase-transition QC policy.
- `QC.md` (root): Full QC triage report from 2026-05-10 session.
- `~/ai/quality-control/planning/override-sage-categories.md`: Plugin design and
  technical addendum.

## Acceptance Criteria

- [ ] `just test` exits 0 with no blocking findings
- [ ] mypy: 0 errors (after plugin resolves Sage dispatch false positives, remaining
  genuine issues fixed)
- [ ] ruff: 0 errors (after E741 global disable; import sorting, TypeAlias
  modernization, unused imports, line length fixed)
- [ ] black: 0 would-be-reformatted files (black exits clean)
- [ ] semgrep: 0 findings (14 findings individually addressed)
- [ ] jscpd: available and passing, or explicitly excluded from gate with
  documented justification

## Dependencies And Boundaries

The mypy queue is not a flat list. Its declared order is:

- `PHASE-QC-BASIC-TYPING-HYGIENE`: first frontier. Missing annotations,
  `Any` leakage, untyped fixtures, and ordinary local code hygiene are real
  current-tree defects. Nothing downstream in the mypy cleanup queue is
  selectable until this phase is complete.
- `PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW`: second frontier. This is the
  narrow plugin lane for Sage dynamic method-container inheritance: `@override`,
  `@final`, `@abstractmethod`, and related MRO/base-injection behavior.
- `PHASE-QC-STUB-GENERATION`: third frontier. Sage, pytest, `.pyi`,
  `TypeAlias`, and generated static surface issues belong here and strictly
  depend on the dynamic-inheritance plugin lane.
- `PHASE-QC-DOWNSTREAM-TYPE-CLEANUP`: final mypy frontier. Only after the
  preceding phases are complete should remaining incompatible signatures,
  constructor calls, `attr-defined`, and category-specific typing defects be
  classified as ordinary downstream fixes.

The remaining 612 ruff errors, 13 black files, and 14 semgrep findings are also
part of this QC feature, but they do not license skipping the mypy dependency
order above.

Every non-complete feature in the repo depends on this gate. No spec,
implementation, research, or Coble work proceeds until QC is clean.

## Governance: No Suppression, No Bypass

**No task under this feature may silence, suppress, ignore, or bypass any global
QC finding.** Every finding is a defect and must be resolved against the repo's
style docs and audit criteria through independent analysis. Permitted resolution
paths are, in order of preference:

1. **Fix the code** — the finding is correct and the code is wrong.

2. **Fix the global QC config** — the code is correct per the repo's own style
   docs and audit criteria, and the QC tool's rule should be adjusted globally
   with a documented justification (as was done for E741).

3. **Route through a decision card** — the correct resolution is an architectural
   change, a new tool integration (e.g., teaching mypy about Sage categories), a
   structural refactor, or any nontrivial choice where more than one reasonable
   path exists. The decision card must record the options, the recommendation,
   and wait for human approval before implementation.

**Not permitted**: per-file `# noqa`, per-file `# type: ignore`, repo-local QC
config overrides, relaxed validators, warning-only paths, or any mechanism that
makes a finding invisible without addressing its root cause.

This feature is expected to require several decision cards. The triage report
identifies multiple categories where the resolution path is not a simple bug fix:

- `valid-type` errors (~100): using ParentMethods/ElementMethods as types is
  architecturally correct per the category-spec style doc, but mypy can't see
  them. Resolution may be `TypeAlias` intermediaries, plugin extension, or
  `.pyi` stubs — all of which need a decision card.

- `attr-defined` on dynamically-assembled classes (~100): `self.base_ring()`
  etc. inside ParentMethods methods. Plugin can partially resolve; remaining
  cases may need structural changes. Decision card required.

- Sage constructor call mismatches (~50): `base_category` arguments. Each is a
  case-by-case analysis; patterns that recur need a decision card.

- `no-any-return` (~150): Sage dynamic machinery returns untyped values. The
  systemic fix is plugin-side `self` typing improvement, not per-method casts.
  Decision card required.

- Ungrounded axiom attrs (~30): `_with_axiom` / `base_category` not available.
  May indicate incomplete spec coverage or wiring gaps. Decision card required.

- Semgrep findings (14): each needs individual triage. False positives that
  conflict with scientific Python conventions may need global semgrep config
  changes — decision card required.

- jscpd environment gap: install globally, exclude from gate with justification,
  or replace with an alternative. Decision card required.

Decisions live under this feature's `decisions/` directory.

---

# QC Triage Report

> Migrated from `QC.md` (root), 2026-05-10 session.
> Branch: `dzack/reviews-bugfixes-and-phase-completion-2026-05-07`
> QC authority: `/home/dzack/ai/quality-control/justfile` — `just test`

## Executive Summary

| Tool      | Status | Count         | Blocking? |
|-----------|--------|---------------|-----------|
| syntax    | PASS   | 0             | no        |
| sage-syn  | PASS   | 0             | no        |
| mypy      | FAIL   | 1,720 errors  | **YES**   |
| ruff      | FAIL   | 612 errors    | **YES**   |
| black     | FAIL   | ~13 files     | **YES**   |
| vulture   | PASS   | 0 (all .venv) | no        |
| semgrep   | FAIL   | 14 findings   | **YES**   |
| jscpd     | SKIP   | not installed | env       |

**Overall: FAIL** — 4 blocking failures.

---

## 1. Mypy: 1,720 Errors in 203 Files

### Category A: Sage Dynamic Dispatch vs. Mypy Static Analysis (est. ~500 errors, ~29%)

Most of these are false positives caused by fundamental architectural mismatch
between Sage's runtime category framework and mypy's static view. However, the
Hom/End/Aut QC audit found a mixed residual set: some remaining override errors are
real owner-map defects in `category_specs/homsets/*`, not plugin misses.

#### A1. `@override` with no statically visible base method (`misc: override`)

~300 errors. Pattern: methods decorated `@override` inside `ParentMethods` /
`ElementMethods` classes that mypy cannot trace back to a base class definition.

Root cause:
- Sage categories use metaclass-driven method injection. A method defined in
  `_FinitePosets.ParentMethods` becomes an override of `Sets.ParentMethods` at
  runtime through Sage's category join machinery.
- Mypy sees these as orphan `@override` decorations because the inheritance
  chain is constructed dynamically, not through Python class inheritance.
- Example: `category_specs/sets/subcategories/countable.py:49: error: Method
  "is_countable" is marked as an override, but no base method was found`

These are often correct overrides in Sage's model. The `@override` markers were
added intentionally to catch drift, and the main conflict is between mypy's static
view and Sage's dynamic dispatch.

Update 2026-05-10: the generic Hom/End/Aut audit proved this category is not
uniform. `category_specs.homsets.homsets.HomCategory.parent_class` currently has
MRO

- `category_specs.homsets.homsets.HomCategory.parent_class`
- `sage.categories.sets_cat.Sets.parent_class`
- `sage.categories.sets_with_partial_maps.SetsWithPartialMaps.parent_class`
- `sage.categories.objects.Objects.parent_class`

and therefore does not inherit Sage's concrete `sage.categories.homset.Homset`
parent methods. Under the current wiring,
`HomCategory.ParentMethods.is_endomorphism_set` and the corresponding generic hom
element predicates are not real runtime overrides, while the End/Aut refinements
still do inherit from real runtime ancestors. Those owner-mismatch cases are tracked
by `[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]` and
`[[TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME]]`.

Update 2026-05-17: the generic Hom/End/Aut owner split is a source issue only where a
method surface claims Sage inheritance or an `@override` that the project runtime
owner chain does not actually provide. Backend reuse of Sage `Hom(...)`,
`HomsetsCategory`, concrete homset containers, or `Homsets().Endset()` does not make the
generic project Hom layer a Sage `Homset` method-container subclass. Plugin work still
owns dynamic Sage/category inheritance failures in ordinary subcategory method
containers, but generic Hom/End/Aut owner mismatches must be fixed in the project
Hom/End/Aut source or docs instead of recorded as plugin false positives.

**Resolution**: Mostly blocked on `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`, with
the generic Hom/End/Aut owner-mismatch cases routed through
`[[TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME]]`.

#### A2. Variables used as types (`valid-type`)

~100 errors. Pattern: `Variable "category_specs.modules.homsets.RModuleHomCategory.ParentMethods"
is not valid as a type`.

Root cause:
- Category objects expose surface classes (`ParentMethods`, `ElementMethods`,
  Hom-category `ElementMethods`) as module-level instances, not as type aliases.
- Code uses these in type annotations (e.g., `-> RModuleHomCategory.ParentMethods`),
  which is correct at runtime but mypy sees them as variable expressions, not
  valid types.
- The category spec style doc (`category-spec-style/references/style.md`)
  explicitly defines these surface class patterns. This is the intended
  architecture.

Conflict with docs: The category-spec style reference defines `ParentMethods`,
`ElementMethods`, and Hom-category `ElementMethods` as standard method-surface
classes. Using them in type annotations is architecturally correct, but mypy
cannot validate them without a `TypeAlias` intermediary or a `.pyi` stub layer
that flattens the dynamic hierarchy into static types.

**Resolution**: Route through `PHASE-QC-STUB-GENERATION` after the basic hygiene
and dynamic-inheritance plugin frontiers are complete. Do not fold this into the
plugin lane unless the failure is first proven to be a base-injection/MRO problem.

#### A3. Missing attributes on dynamically-assembled classes (`attr-defined`)

~100 errors. Pattern: `"ParentMethods" has no attribute "base_ring"` /
`"is_finite"` / `"rank"` / `"form"`, etc.

Root cause: When a method is defined inside `ModulesWithBilinearForm.ParentMethods`,
it can reference `self.base_ring()` because at runtime `self` is a module object
that inherits this method via category join. Mypy sees `self` typed as
`ParentMethods` (the mixin class) and knows nothing about the concrete object's
attributes.

**Resolution**: Not a single bucket. If the missing attribute is caused by
method-container MRO/base injection, route it through
`PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW`. If it requires a static `.pyi`,
`TypeAlias`, or generated surface, route it through
`PHASE-QC-STUB-GENERATION`. Otherwise defer it to
`PHASE-QC-DOWNSTREAM-TYPE-CLEANUP`.

### Category B: Genuinely Missing Type Annotations (est. ~800 errors, ~47%)

Source paths: `src/lattices/`, `tests/`, `src/sage_patches/`.

#### B1. Functions without return type annotations (`no-untyped-def`)

~600 errors. Pattern: nearly every function in `src/lattices/core/`,
`src/lattices/morphisms/`, `tests/` lacks `-> ReturnType`.

Root cause:
- `src/lattices/` and `tests/` contain implementation and test code from a prior
  implementation pass. Per `AGENTS.md`, `src.bak/` and `tests.bak/` quarantine
  stale implementation code, but `src/lattices/` and `tests/` remain active (not
  in `.bak`).
- The repo is currently in the **spec phase** per `.agents/current-goal-phase.md`,
  where `GOAL.md` states: "QC is part of transition evidence for committed
  implementation work, but it is not the main control loop during churn-heavy
  spec drafting."
- However, `AGENTS.md` directive: "QC findings are mandatory, not advisory" —
  this applies regardless of phase.

The missing annotations are real defects in the current working tree.

**Resolution**: Add `-> ReturnType` to every function in `src/lattices/`,
`tests/`, and `src/sage_patches/`. Estimate: ~600 locations across ~50 files.
Mechanical work suitable for delegation.

#### B2. Missing parameter type annotations (`no-untyped-def` on parameters)

~150 errors. Pattern: `def __init__(self, base_ring, invariants, gram_matrix=None, ...)`
— parameters lack type annotations.

**Resolution**: Same scope as B1. Add parameter type annotations. Estimate: ~150
locations.

#### B3. Object-type cascades in tests/conftest.py

~15 errors. Pattern: `tests/conftest.py:77: error: Unsupported target for indexed
assignment ("object")` — the `config` fixture returns untyped objects, causing
cascading `object`-typed errors downstream.

Root cause: `pytest_addoption`, `pytest_configure`, and related fixtures lack
type annotations. Without annotations, mypy infers `object` for all parameters.

**Resolution**: Add type annotations to all pytest fixtures in `tests/conftest.py`.
Estimate: ~10 fixture functions.

### Category C: Sage Constructor Call Mismatches (`call-arg`) (est. ~50 errors, ~3%)

Pattern: `Missing positional argument "base_category" in call to "_Fields"` /
`"_CommutativeRings"` / `"TopologicalSpaces"`.

Root cause: Category constructors in `category_specs/` use Sage's
`ParentMethods.__init_subclass__` machinery where `base_category` is often
optional or derived at runtime. Mypy sees the static signature requiring
`base_category` but the call sites omit it.

**Resolution**: Case-by-case analysis needed. Some may be real bugs; others may
be runtime-valid patterns that need `# type: ignore` with justification. Not
blocked on plugin.

### Category D: Other Genuine Issues (est. ~370 errors, ~21%)

| Subcategory | Count | Description |
|-------------|-------|-------------|
| `Missing return statement` | ~50 | Genuine control-flow bugs |
| `no-any-return` | ~150 | Return `Any` when specific type declared (Sage dynamic machinery) |
| `no-redef` | ~20 | Duplicate definitions in `forms/__init__.py` (lines 87-96 and 137-146) |
| `@final` on non-methods | ~10 | `forms/__init__.py:155` and similar |
| `Incompatible types` | ~5 | `endsets.py` / `autsets.py` assignment overrides |
| `Cyclic definition` | ~10 | `Poset`, `PosetElement`, `Category` cyclic chains |
| Ungrounded axiom attrs | ~30 | `_with_axiom` / `base_category` not available |

---

## 2. Ruff: 612 Errors

| Category | Code | Count | Severity | Resolution |
|----------|------|-------|----------|------------|
| Import sorting | I001 | ~200 | Cosmetic | `ruff --fix` |
| TypeAlias modernization | UP040 | ~200 | Cosmetic | Mechanical `TypeAlias` → `type` |
| Unused imports | F401 | ~30 | Genuine dead | Remove dead imports |
| Line length | E501 | ~15 | Style | Wrap long lines |
| Ambiguous variable `I` | E741 | 2 | Suppressed | Globally disabled in `ruff-global.toml`; see `~/ai/quality-control/planning/README.md` |

E741 resolution note: The variable name `I` for an ideal is standard
mathematical notation. `research-code-style` mandates "code must read like
mathematical prose." Globally disabled with justification.

---

## 3. Black: ~13 Files Need Reformatting

Files in `category_specs/` that black would reformat. Purely formatting — no
semantic change. Also `category_specs/sets/subcategories/image.py` has a tooling
version mismatch (Python 3.13 < target 3.14). Resolve by running black with
Python 3.14 or setting `--target-version py313`.

---

## 4. Semgrep: 14 Blocking Findings

Findings detected but not individually inspected in the 2026-05-10 session.
Need `semgrep --json` extraction and per-finding triage. Likely categories:
hardcoded secrets, unsafe deserialization, subprocess injection patterns common
in scientific Python.

---

## 5. Vulture: PASS

Clean. Dead code only in `.venv/`.

---

## 6. Jscpd: Environment Gap

`jscpd` not resolvable by `uvx`. Environment provisioning issue. Either install
jscpd globally or document as excluded from QC gate.

---

## Triage Summary: Root Cause Map

| Error Count | Category | True Positive? | Root Cause |
|-------------|----------|:---:|------------|
| ~500 | Sage dispatch vs mypy | NO | Sage metaclass method injection invisible to mypy |
| ~600 | Missing return annotations | YES | `src/` and `tests/` untyped |
| ~150 | Missing param annotations | YES | `src/` and `tests/` untyped |
| ~200 | Import sorting (ruff) | YES | Cosmetic |
| ~200 | TypeAlias modernization | YES | Pre-3.12 syntax |
| ~50 | Sage constructor args | MIX | Some runtime-valid, some possibly bugs |
| ~30 | Unused imports | YES | Dead imports to remove |
| ~15 | Line length | YES | Exceeds 88-char limit |
| ~50 | Missing return statements | YES | Control-flow bugs |
| ~30 | Ungrounded axiom attrs | PROB | `_with_axiom` / `base_category` not available |
| ~20 | Duplicate definitions | YES | `forms/__init__.py` redefines class family |
| ~15 | Object cascades in tests | YES | Untyped pytest fixtures |
| 14 | Semgrep findings | LIKELY | Security/correctness patterns |
| 2 | Ambiguous variable `I` | NO | Standard math notation, globally disabled |

## Key Conflicts with Docs

- The **category-spec style doc** defines `ParentMethods`/`ElementMethods` as
  standard method-surface classes. Mypy `valid-type` errors are a tool
  limitation, not a style violation.
- The **`@override` markers** are intentional per the style doc. Mypy can't
  trace them through Sage's dynamic hierarchy.
- The **variable name `I`** is standard mathematical prose per `research-code-style`.
  Ruff E741 conflicts with domain convention. Globally resolved.
- **`AGENTS.md`** states "QC findings are mandatory, not advisory." **`GOAL.md`**
  states that during spec drafting, "QC is not the main control loop." These are
  in tension. `AGENTS.md` takes lexical precedence: all findings must be
  addressed.

## Verdict

**1,720 mypy errors**: ~500 Sage-dispatch false positives → blocked on plugin.
~800 genuine missing annotations → mechanical fix. ~420 mixed bugs/artifacts →
case-by-case.

**612 ruff errors**: ~400 cosmetic (import sort, TypeAlias) → `ruff --fix`.
~30 dead imports → remove. ~15 line length → wrap. 2 E741 → globally disabled.

**13 black files**: `black .` reformat.

**14 semgrep findings**: Individual triage needed.
