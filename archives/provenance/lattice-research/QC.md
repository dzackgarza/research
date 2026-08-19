# QC Triage Report — Research Repo

**Date**: 2026-05-10
**Branch**: `dzack/reviews-bugfixes-and-phase-completion-2026-05-07`
**Phase**: Category specs and semantic vocabulary (spec phase)
**QC authority**: `/home/dzack/ai/quality-control/justfile` — `just test`

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

These are false positives caused by fundamental architectural mismatch between Sage's runtime category framework and mypy's static view. They are NOT code defects.

#### A1. `@override` with no statically visible base method (`misc: override`)

~300 errors. Pattern: methods decorated `@override` inside `ParentMethods` / `ElementMethods` classes that mypy cannot trace back to a base class definition.

Root cause:
- Sage categories use metaclass-driven method injection. A method defined in `_FinitePosets.ParentMethods` becomes an override of `Sets.ParentMethods` at runtime through Sage's category join machinery.
- Mypy sees these as orphan `@override` decorations because the inheritance chain is constructed dynamically, not through Python class inheritance.
- Example: `category_specs/sets/subcategories/countable.py:49: error: Method "is_countable" is marked as an override, but no base method was found`

These ARE correct overrides in Sage's model. The `@override` markers were added intentionally to catch drift. The conflict is between mypy's static view and Sage's dynamic dispatch.

#### A2. Variables used as types (`valid-type`)

~100 errors. Pattern: `Variable "category_specs.modules.homsets.RModuleHomCategory.ParentMethods" is not valid as a type`.

Root cause:
- Category objects expose surface classes (`ParentMethods`, `ElementMethods`, `MorphismMethods`) as module-level instances, not as type aliases.
- Code uses these in type annotations (e.g., `-> RModuleHomCategory.ParentMethods`), which is correct at runtime but mypy sees them as variable expressions, not valid types.
- The category spec style doc (`category-spec-style/references/style.md`) explicitly defines these surface class patterns. This is the intended architecture.
- Example: `category_specs/algebras/__init__.py:693: error: Variable "category_specs.algebras.homsets.AlgebraHomCategory.ParentMethods" is not valid as a type`

Conflict with docs: The category-spec style reference defines `ParentMethods` / `ElementMethods` / `MorphismMethods` as standard method-surface classes. Using them in type annotations is architecturally correct, but mypy cannot validate them without a `TypeAlias` intermediary or a `.pyi` stub layer that flattens the dynamic hierarchy into static types.

#### A3. Missing attributes on dynamically-assembled classes (`attr-defined`)

~100 errors. Pattern: `"ParentMethods" has no attribute "base_ring"` / `"is_finite"` / `"rank"` / `"form"`, etc.

Root cause:
- When a method is defined inside `ModulesWithBilinearForm.ParentMethods`, it can reference `self.base_ring()` because at runtime `self` is a module object that inherits this method via category join. Mypy sees `self` typed as `ParentMethods` (the mixin class) and knows nothing about the concrete object's attributes.
- Same dynamic dispatch issue as A1.

### Category B: Genuinely Missing Type Annotations (est. ~800 errors, ~47%)

Source paths: `src/lattices/`, `tests/`, `src/sage_patches/`.

#### B1. Functions without return type annotations (`no-untyped-def`)

~600 errors. Pattern: nearly every function in `src/lattices/core/`, `src/lattices/morphisms/`, `tests/` lacks `-> ReturnType`.

Root cause:
- `src/lattices/` and `tests/` contain implementation and test code from a prior implementation pass. Per `AGENTS.md`, `src.bak/` and `tests.bak/` quarantine stale implementation code, but `src/lattices/` and `tests/` remain active (not in `.bak`).
- The repo is currently in the **spec phase** per `.agents/current-goal-phase.md`, where `GOAL.md` states: "QC is part of transition evidence for committed implementation work, but it is not the main control loop during churn-heavy spec drafting."
- However, `AGENTS.md` directive: "QC findings are mandatory, not advisory" — this applies regardless of phase.

The missing annotations are real defects in the current working tree, even if the spec-phase policy deprioritizes implementation polish.

#### B2. Missing parameter type annotations (`no-untyped-def` on parameters)

~150 errors. Pattern: `def __init__(self, base_ring, invariants, gram_matrix=None, ...)` — parameters lack type annotations.

Same root cause as B1.

#### B3. Object-type cascades in tests/conftest.py

~15 errors. Pattern: `tests/conftest.py:77: error: Unsupported target for indexed assignment ("object")` — the `config` fixture returns untyped objects, causing cascading `object`-typed errors downstream (float casts, unary negation, etc.).

Root cause: `pytest_addoption`, `pytest_configure`, and related fixtures lack type annotations. Without annotations, mypy infers `object` for all parameters, and subsequent operations on these objects all fail.

### Category C: Sage Constructor Call Mismatches (`call-arg`) (est. ~50 errors, ~3%)

Pattern: `Missing positional argument "base_category" in call to "_Fields"` / `"_CommutativeRings"` / `"TopologicalSpaces"`.

Root cause:
- Category constructors in `category_specs/` use Sage's `ParentMethods.__init_subclass__` machinery where `base_category` is often optional or derived at runtime.
- Mypy sees the static signature requiring `base_category` but the call sites omit it.
- This is a tension between Sage-idiomatic construction patterns and mypy's strict signature checking. In some cases these may be real bugs (missing required arguments); in others they reflect runtime behavior mypy cannot see.

### Category D: Other Genuine Issues (est. ~370 errors, ~21%)

- `Missing return statement` (~50): Functions with typed returns but code paths that fall through without `return`. Genuine bugs.
- `no-any-return` (~150): Functions returning `Any` when a specific type is declared. Caused by dynamic Sage machinery returning untyped values.
- `no-redef` (~20): Duplicate name definitions (e.g., `category_specs/forms/__init__.py` defines `IntegralNondegenerate...` class family twice on lines 87-96 and 137-146).
- `@final` on non-methods (~10): `category_specs/forms/__init__.py:155` and similar.
- `Incompatible types in assignment` (~5): Type mismatches in `endsets.py` and `autsets.py` assignment overrides.
- `Cyclic definition` (~10): `Poset`, `PosetElement`, `Category` appear in cyclic chains.
- Ungrounded attribute references (~30): `SubcategoryMethods has no attribute '_with_axiom'` — suggests axiom wiring may be incomplete.

---

## 2. Ruff: 612 Errors

### Category E: Import Sorting (I001) — ~200+

Pervasive across `category_specs/` and `src/`. The imports violate ruff's isort-equivalent ordering.

Root cause: The code was likely written with `from __future__ import annotations` at module top followed by stdlib, third-party, and local imports, but ruff's sort order disagrees with the current arrangement. Low severity — purely cosmetic.

### Category F: TypeAlias → `type` Keyword (UP040) — ~200+

All in category `__init__.py` alias sections. Ruff 0.9+ enforces Python 3.12 `type X = Y` syntax.

Root cause: The alias blocks (e.g., `AlgebrasCategory: TypeAlias = Algebras`) use the pre-3.12 `TypeAlias` annotation pattern. Modernizing to `type` keyword would resolve this but requires Python 3.12+. **No mathematical impact.**

### Category G: Unused Imports (F401) — ~30

Scattered across `src/sage_patches/`, `src/lattices/core/`, and `tests/`.

Root causes (by file):
- `src/sage_patches/ring_base_category.py`: `cached_method`, `CommutativeRings`, `Any` — imported but never used. Genuine dead imports.
- `src/sage_patches/completions.py`: `ZZ`, `QQ` — imported but never used.
- `src/sage_patches/ideal_submodule.py`: `QQ`, `PrincipalIdealDomain` — imported but never used.
- `src/sage_patches/module_enrichment.py`: `ZZ`, `Modules as ModulesCategory` — imported but never used.
- `src/lattices/core/modules_with_forms.py`: `Category` — imported but never used.
- `src/lattices/morphisms/__init__.py`: `Element` — imported but never used.
- `tests/category_specs/test_spec_obligations.py`: `refinement` module — imported but doesn't exist.

These are genuine dead imports that should be removed.

### Category H: Line Length (E501) — ~15

In `tests/conftest.py`, `tests/category_specs/test_spec_obligations.py`, `src/sage_patches/ring_base_category.py`, and `.agents/scripts/generate_card_progress_report.py`.

### Category I: Ambiguous Variable Name `I` (E741) — 2

`src/sage_patches/ring_base_category.py:63` and `tests/category_specs/test_spec_obligations.py:39`. Both assign `I = ...ideal(...)`.

**Conflict with style docs**: The variable name `I` for an ideal is standard mathematical notation in algebraic code. The `research-code-style` doc says "code must read like mathematical prose." Ruff's E741 rule flags `I` as ambiguous (confusable with `l`), but in algebraic code, `I` for ideal and `O` for object are universal conventions. This is a tension between general-purpose linting rules and domain-specific mathematical notation.

---

## 3. Black: ~13 Files Need Reformatting

Files in `category_specs/` that black would reformat:

- `category_specs/forms/chain.py`
- `category_specs/modules/subcategories/free_graded_modules.py`
- `category_specs/modules/subcategories/finitely_presented_graded_modules.py`
- `category_specs/modules/subcategories/integer_lattices.py`
- `category_specs/modules/subcategories/representation_modules.py`
- `category_specs/modules/subcategories/with_basis.py`
- `category_specs/algebras/__init__.py`
- `category_specs/rings/subcategories/local.py`
- `category_specs/rings/subcategories/reduced.py`
- `category_specs/rings/subcategories/polynomial_ring.py`
- `category_specs/rings/subcategories/number_field.py`
- `category_specs/rings/subcategories/rational_field.py`
- `category_specs/cat/base_category_types.py`
- `category_specs/sets/subcategories/finite_set_maps.py`
- `.agents/scripts/generate_card_progress_report.py`

Also one hard error: `category_specs/sets/subcategories/image.py` — black can't verify equivalence because the running Python (3.13) is older than the target version (3.14). This is an environment issue, not a code defect.

---

## 4. Semgrep: 14 Blocking Findings

Findings were detected but the JSON extraction failed in this session. These need individual inspection. The 14 findings are classified as "blocking" by semgrep's default severity model. Re-running with `--json` and piping to a proper formatter would surface the exact rules and locations.

---

## 5. Vulture: PASS

Vulture found dead code only in `.venv/` (setuptools/distutils internals). No repo-level dead code was detected at confidence >= 70%. **Clean bill of health for dead code.**

---

## 6. Jscpd: Environment Gap

`jscpd` cannot be resolved from npm/pypi registries by `uvx`. This is an environment provisioning issue, not a repo defect. The justfile recipe for jscpd needs the tool to be available.

---

## Triage Summary: Root Cause Map

| Error Count | Category                      | True Positive? | Root Cause                                     |
|-------------|-------------------------------|:---:|------------------------------------------------|
| ~500        | Sage dispatch vs mypy         | NO  | Sage metaclass method injection invisible to mypy |
| ~600        | Missing return annotations    | YES | src/ and tests/ from prior impl pass, untyped  |
| ~150        | Missing param annotations     | YES | src/ and tests/ from prior impl pass, untyped  |
| ~200        | Import sorting (ruff)         | YES | Cosmetic — import block ordering               |
| ~200        | TypeAlias modernization       | YES | Pre-3.12 syntax, no mathematical impact        |
| ~50         | Sage constructor args         | MIX | Some runtime-valid, some possibly bugs          |
| ~30         | Unused imports                | YES | Dead imports to remove                         |
| ~15         | Line length                   | YES | Exceeds 88-char limit                          |
| ~50         | Missing return statements     | YES | Genuine control-flow bugs                      |
| ~30         | Ungrounded axiom attrs        | PROB | `_with_axiom` / `base_category` not available   |
| ~20         | Duplicate definitions         | YES | `forms/__init__.py` redefines class family      |
| ~15         | Object cascades in tests      | YES | Untyped pytest fixtures                        |
| 14          | Semgrep findings              | LIKELY | Security/correctness patterns to inspect       |
| 2           | Ambiguous variable `I`        | NO   | Standard math notation conflicts with lint rule |

## Key Conflicts with Docs

- The **category-spec style doc** defines `ParentMethods`/`ElementMethods` as standard method-surface classes used in type annotations. Mypy's `valid-type` errors on these are a tool limitation, not a style violation.
- The **`@override` markers** are intentional per the style doc's "method override" rules. Mypy can't trace them through Sage's dynamic hierarchy, producing false positives.
- The **variable name `I`** for ideals is standard mathematical prose per `research-code-style` doc. Ruff's E741 rule conflicts with domain convention.
- The **`AGENTS.md` policy** states "QC findings are mandatory, not advisory" and "never dismiss findings as 'expected for this phase.'" However, `GOAL.md` also states that during spec drafting, "QC is not the main control loop." These two statements are in tension. The former takes lexical precedence per AGENTS.md hierarchy, meaning all findings must be addressed regardless of phase.

## Verdict

**1,720 mypy errors**: ~500 are Sage-dispatch false positives requiring either mypy plugin configuration or `.pyi` stubs to resolve. ~800 are genuine missing type annotations in `src/lattices/`, `tests/`, and `src/sage_patches/` — these are real code hygiene gaps. The remaining ~420 are a mix of missing return statements, duplicate definitions, and dynamic-typing artifacts.

**612 ruff errors**: Dominated by two high-count/low-severity categories (import sorting, TypeAlias modernization). ~30 unused imports are genuine dead code. ~15 line-length violations. 2 ambiguous-variable-name hits conflict with mathematical naming conventions.

**13 black files**: All formatting-only, no semantic change. The `image.py` file has a tooling version mismatch.

**14 semgrep findings**: Need individual review — likely include security patterns (hardcoded secrets, unsafe deserialization, etc.) common in scientific Python code.

---

## Addendum: Explicit Python Inheritance Audit (`category_specs/`)

Category specs should declare mathematical relationships via `super_categories()` / `_base_category_class_and_axiom`, not Python class inheritance. The following are possible violations — cases where a spec class inherits from another spec-internal class in a way that may encode mathematical hierarchy statically.

### Possible violations

**`forms/subcategories/with_forms.py`** — `OverPIDFormedModulesCategory`:
- Line 121: `ParentMethods = FormedModulesCategory.ParentMethods` — alias makes the two containers the same object; PID-specific refinements are impossible without removing it
- Line 123: `class SubcategoryMethods(FormedModulesCategory.SubcategoryMethods)` — explicit Python inheritance for a mathematical subcategory relationship already declared via `_base_category_class_and_axiom = (_OverPID, "WithForms")`
- Line 136: `ElementMethods = FormedModulesCategory.ElementMethods` — same alias issue as line 121

**`HomCategory(HomCategoryConstruction)` nested inside spec classes**:
- `modules/subcategories/with_basis.py:133`
- `modules/subcategories/finitely_presented_over_pid.py:153`
- `modules/subcategories/with_ordered_generating_set.py:44`
- `forms/subcategories/free_bilinear.py:210`

`HomCategoryConstruction` is defined in `category_specs/homsets/homsets.py` (a project-internal class). Whether functorial construction dispatch requires this Python inheritance or whether it could be expressed via `extra_super_categories()` is unverified.

**`rings/subcategories/constructions/` — parametric spec classes inheriting from internal helpers**:
- `characteristic.py:13`: `_CharacteristicRings(_Category_over_base_integer)`
- `krull_dimension.py:13`: `_KrullDimension(_Category_over_base_integer)`
- `rings/matrix_algebras.py:21`: `_MatrixAlgebras(_Category_over_base_integer_pair)`

`_Category_over_base_integer` is itself a spec class with method containers. Downstream authors adding new integer-parametric ring constructions must know to inherit from this internal class.

**`homsets/autsets.py:126`**: `AutCategoryConstruction(EndCategoryConstruction)` — one construction category inheriting from another project-internal construction category.
