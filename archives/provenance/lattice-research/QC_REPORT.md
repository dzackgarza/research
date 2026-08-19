## QC Sprint Standup Report — 2026-05-14

**Pipeline state:** `just test` fails at `_mypy`. Ruff/format passes (no lint/format output). Mypy is the sole blocker.

**Total mypy errors: 1,290 across 173 files**

---

### Error Budget by Error Code

| Code | Count | Classification | Root Cause |
|---|---|---|---|
| `[misc]` | 428 | 359 plugin / 69 code | 359 = `@override` w/ no visible base (Sage dynamic dispatch); 69 = other (type-alias-as-base, overload mismatch, `@final` on non-method, `Cannot assign to final`) |
| `[attr-defined]` | 300 | 98 plugin / 202 code | 98 = `SubcategoryMethods._with_axiom` absent (plugin gap); 202 = `base_ring`, `category`, `rank`, `is_subset`, `parent` etc not declared on stub types |
| `[no-any-return]` | 267 | code | Sage returns `Any` at runtime; declared return types are concrete (rings, modules, posets). Most concentrated in `rings/` (406 errors total) |
| `[valid-type]` | 86 | code | Inner method-container classes (`ParentMethods`, `ElementMethods`) used as type annotations in signatures — tracked by `TASK-QC-GROUND-CATEGORY-SPEC-CALLABLE-TYPES` |
| `[untyped-decorator]` | 75 | plugin | `@cached_method`, `@abstract_method` etc. are Sage decorators with no stubs — makes decorated functions untyped |
| `[call-arg]` | 62 | mixed | 22 plugin (Constructors/FunctorialConstruction/dispatch=False); 40 code (`base_category` positional missing, `*_certificate` keyword) |
| `[assignment]` | 28 | plugin | Covariant `ParentMethods`/`ElementMethods` narrowing in homset specializations |
| `[name-defined]` | 10 | code | Missing `ParentMethods` from axiom subcategories (`SetsCategory.Finite`, `SetsCategory.Countable`, `ModulesCategory.Free`, etc.) |
| `[empty-body]` | 10 | code | Missing return statements in declared-return functions |
| `[no-redef]` | 8 | code | `Constructors` class/method name collision (8 files) — tracked by triage card |
| `[return-value]` | 5 | plugin | Covariant return narrowing |
| `[operator]` / `[arg-type]` | 5 | plugin | `MorphismMethods` not callable, `__gt__`/`__ge__` type width |
| `[attr-defined]` (test) | 1 | code | `category_specs.refinement` missing — `test_spec_obligations.py:70` |

**Rough split: ~496 plugin-gap errors, ~794 code-gap errors**

---

### Error Budget by Module

| Module | Errors | Hottest File |
|---|---|---|
| `rings/` | 406 | `rational_field.py` (16), `integral_domain.py` (multiple clusters) |
| `sets/` | 257 | `countable.py` (10 misc), `facade.py` (6 misc) |
| `modules/` | 196 | `homsets.py`, `with_basis.py`, `with_ordered_generating_set.py` |
| `posets/` | 73 | `finite.py` (9 `[valid-type]` — single-function `list` used as type) |
| `forms/` | 68 | `free_bilinear.py`, `definite.py`, `indefinite.py` |
| `topological_spaces/` | 55 | connected/compact/complete (6 `[call-arg]`) |
| `algebras/` | 51 | `finite_dimensional.py` |
| `lattices/` | 50 | `over_integers.py` |
| `cat/` | 45 | `base_category_types.py` (4 distinct `[misc]` types) |
| `homsets/` | 43 | `homsets.py` (overload mismatch, assignment narrowing) |

---

### Task Tracker State

| Task | Status | Covers |
|---|---|---|
| `TASK-QC-GROUND-CATEGORY-SPEC-CALLABLE-TYPES` | **needs-agent-review** | `[valid-type]` 86 errors — inner classes as type annotations |
| `TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY` | **unstarted** | `[no-any-return]` 267, `[empty-body]` 10, `[name-defined]` 10, `[no-redef]` 8 |
| `TASK-QC-PLUGIN-METHOD-CONTAINER-SELF-SURFACES` | **unstarted** (gated) | `[attr-defined]` `base_ring`/`category`/`parent` surfaces |
| `TASK-QC-PLUGIN-MORPHISMMETHODS-CALLABLE` | **unstarted** (gated) | `[operator]` MorphismMethods not callable |
| `TASK-QC-PLUGIN-FUNCTORIAL-CONSTRUCTION-CONSTRUCTORS` | **unstarted** (gated) | `[call-arg]` FunctorialConstruction 0-arg |
| `TASK-QC-PLUGIN-CLASSCALL-PRIVATE-KWARGS` | **unstarted** (gated) | `[call-arg]` `dispatch=False` |
| `TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW` | **unstarted** (gated) | `[misc]` override (359), `[attr-defined]` `_with_axiom` (98), `[assignment]` (28) |

Gates: all plugin tasks are gated on `PHASE-QC-BASIC-TYPING-HYGIENE` completing first, and `TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW` is also gated on `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`.

---

### Sprint Priorities (Recommended Order)

**Now (unblocked):**
1. **Close `TASK-QC-GROUND-CATEGORY-SPEC-CALLABLE-TYPES`** (needs-agent-review → done). This is the prerequisite before `PHASE-QC-BASIC-TYPING-HYGIENE` can mark complete. Covers 86 `[valid-type]` errors.
2. **Start `TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY`** — largest unblocked code-gap bucket. Priority sub-items:
   - `[no-any-return]` 267 errors: concentrated in `rings/` (integral\_domain, rational\_field, real\_precision). Sage call sites return `Any`; need cast or typed wrapper.
   - `[name-defined]` 10: axiom subcategory `ParentMethods` not wired (Sets, Modules axioms).
   - `[empty-body]` 10: missing return statements.
   - `[no-redef]` 8: `Constructors` collision across 8 `__init__.py` files.
3. **`cat/base_category_types.py` misc cluster** (4 distinct non-override `[misc]` types in one file) — `_make_named_class`, `__classcall__`, invalid base class, `Cannot assign to final`. These are low-count but structurally blocking.

**Open question:** The `category_specs.refinement` attribute missing from category-obligation test (`test_spec_obligations.py:70`) — is this a missing module or a renamed subpackage? Not tracked in any current task card.

**Blocked until plugin work lands:** The 359 `@override` errors and 98 `_with_axiom` errors (combined ~457 errors, 35% of total) cannot be fixed without the Sage mypy plugin.
