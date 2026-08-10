# Preamble: replacing the load list with imports

> **Done, 2026-08-10** (`e2ad547`, `4aa41a8`). `install.sage` imports its files
> instead of loading them, registration happens in the module body that owns it,
> and the two `sys.modules` shims are gone. 65 of 69 files import standalone; the
> import graph has no cycles. The per-file tables below are the record of that
> work and are now history, not a plan — the counts predate it.
>
> Open work lives under **Open** at the end of this file.

`install.sage` carries 55 ordered `load()` calls. That list is the
preamble's dependency graph, written by hand because `.sage` files could not be
modules. They can now. This file records what changed upstream, what the
conversion costs, and the exact per-file work.

Generated against `tree-sitter-sage` at `8807fd4`. Regenerate the tables after
any substantial preamble edit — the counts below are a snapshot, not a contract.

## What changed upstream

`tree-sitter-sage` ships `sageparse`, a complete replacement for Sage's
preparser built on a real grammar. It now has two frontends over that compiler:

- `sageparse.preparser.importer` — a meta-path finder and loader that make
  `.sage` an importable source format.
- `sageparse.build` — the same lowering ahead of time, `.sage` → `.py`, for
  distribution.

Sage itself treats `.sage` as a script language: `sage foo.sage` writes a
`foo.sage.py` beside it, and `load()` executes a file into an existing
namespace. Neither produces a module. That is why this directory loads instead
of imports, and it is the constraint that has been lifted.

## How to use it

One import installs the finder for the process:

```python
import sageparse.preparser.importer

import dzack_research.preamble.categories.forms.forms as forms
from dzack_research.preamble.categories.forms.forms import FormModules
```

Then everything is ordinary Python: `__spec__`, `sys.modules`, `importlib.reload`,
relative imports, and `__pycache__` all behave as they do for `.py`. A directory
becomes a package with an `__init__.sage`. Tracebacks name the `.sage` file and
the author's line, because the lowering preserves line geometry.

Two properties worth knowing:

- **A `.py` beside a `.sage` wins.** The finder declines wherever Python can
  already import the module, so a generated artifact shadows its source.
  During conversion this means a half-migrated tree behaves predictably.
- **Importing `sageparse` alone changes nothing.** Only importing
  `sageparse.preparser.importer` installs the finder.

The lowered module gets the compiler's runtime prelude — `Integer`,
`RealNumber`, `ellipsis_range`, `Set`, and the rest of what the lowering emits —
and nothing else. It does **not** get `sage.all`. That is the whole point of a
library module, and it is the source of most of the work below: names this
directory currently receives from the shared namespace have to be imported.

## What imports replace, and what they do not

Replaced: the ordering. Python computes it from the import graph, and the graph
of names needed *at import time* is acyclic (26 edges, no cycles), so the order
is derivable. Also replaced: the `_preamble_namespace` double-load cache, which
`sys.modules` provides for free.

**Not replaced:** the initialization sequence. `refine`/`hook_post_init` patch
Sage classes process-wide and must run exactly once, and the `install_*()` calls
must run after the catalogue exists. No import graph expresses that. It stays an
explicit step in `install.sage` — a much shorter one.

## The shape of the work

57 real `.sage` files (the other 47 under this directory are
`.ipynb_checkpoints` copies). All 57 lower to valid Python today; none needs a
compiler fix.

| | |
|---|---:|
| files importable unchanged | 8 |
| files needing added imports | 49 |
| cross-file references currently supplied by the shared namespace | 188 |
| …of those, evaluated at import time | 26 |
| import-time cycles | **0** |
| cycles if every reference is hoisted to a top-level import | 2 (26 files, 2 files) |
| distinct names from outside the preamble | 34 |

The last two rows are the trap. A reference inside a method body is resolved at
call time and is harmless as a *use*, but writing `from .other import Foo` at
module top promotes it to import time. Hoisting all 188 would close two cycles.
The fix is ordinary Python: import those specific names inside the function that
uses them. The tables below mark exactly which ones.

## Suggested order

1. **The 8 clean files** (✅ in the catalogue). They import unchanged; convert
   and delete their `load()` lines to prove the path end to end.
2. **Outside names.** Mechanical, and independent of the cycles — add the
   verified import lines from the table below. `ZZ` alone is 57 uses.

   One row there is not mechanical: `load` (59 uses) is Sage's loader being
   called from inside preamble files. Those calls are the problem, not a name
   to import — each becomes an import of the module it was loading. The table
   lists `from sage.misc.persist import load` because that is what the name
   resolves to today; do not add it.
3. **Acyclic sibling edges.** Top-level imports, ordered by the catalogue.
4. **The two cyclic groups.** Function-local imports for the marked edges, or
   restructure. This is a category-layer design question, not a tooling one, and
   worth deciding deliberately rather than mechanically.
5. **Reduce `install.sage`** to the post-init sequence and the `install_*()`
   calls.

## Caveats on this analysis

- Name ownership was computed from top-level definitions in this directory's
  `.sage` and `.py` files. A name defined elsewhere shows as "outside".
- It measures what the AST evaluates. A `getattr`, a string-keyed lookup, or a
  name introduced by `exec` will not appear.
- Ten "outside" names resolve to nothing in `sage.all`: `value`, `indexed`,
  `ring`, `scalar`, `first`, `Element`, `UnderlyingSet`, `SetMorphism`,
  `MorphismMatrix`, `get_ipython`. Some come from the vendored
  `sage_lattice_category_spike`; the lowercase ones look like analysis artifacts
  or genuine free variables. Check them individually before trusting either
  reading.
- Verified import lines were resolved by finding a module that binds the name to
  the *same object* `sage.all` exposes, not by reading `__module__`. Several
  Sage globals are not the class of the same name — `RealNumber` is
  `create_RealNumber`, `ComplexNumber` is `create_ComplexNumber` — so guessing
  the path produces something that imports and then fails at first use.
## Catalogue: every `.sage` file and what it must import

`needs` is names used but not bound in the file. `sibling` are owned by another
preamble file; `outside` by Sage or the vendored spike. `deferred` counts sibling
names whose top-level import would close a cycle -- import those inside the
function that uses them. `at import` counts names evaluated while the module
executes (class bases, decorators, module-level code); those must be top-level.

| file | needs | sibling | outside | deferred | at import |
|---|---:|---:|---:|---:|---:|
| `catalogue.sage` | 5 | 5 | 0 | 0 | 3 |
| `categories/abstract_categories/arrow_categories.sage` | 3 | 2 | 1 | 1 | 0 |
| `categories/abstract_categories/products.sage` | 2 | 1 | 1 | 0 | 0 |
| `categories/abstract_categories/slice_categories.sage` | 4 | 2 | 2 | 1 | 0 |
| `categories/algebras/algebras.sage` | 2 | 2 | 0 | 2 | 0 |
| `categories/algebras/finitely_presented_algebras.sage` | 2 | 2 | 0 | 0 | 0 |
| `categories/algebras/framed_free_algebras.sage` | 12 | 9 | 3 | 7 | 4 |
| `categories/algebras/free_algebras.sage` | 3 | 3 | 0 | 2 | 0 |
| `categories/divisors/cartier_divisor_groups.sage` | 3 | 1 | 2 | 0 | 0 |
| `categories/divisors/class_groups.sage` | 3 | 1 | 2 | 0 | 0 |
| `categories/divisors/divisor_groups.sage` | 3 | 2 | 1 | 0 | 0 |
| `categories/divisors/picard_groups.sage` | 3 | 1 | 2 | 0 | 0 |
| `categories/divisors/weil_divisor_groups.sage` | 4 | 3 | 1 | 0 | 0 |
| `categories/forms/forms.sage` | 6 | 4 | 2 | 4 | 0 |
| `categories/forms/gram_matrices.sage` ✅ | 0 | 0 | 0 | 0 | 0 |
| `categories/group/finitely_presented_groups.sage` | 3 | 2 | 1 | 0 | 0 |
| `categories/group/groups.sage` | 5 | 2 | 3 | 0 | 0 |
| `categories/group/predicate_subgroups.sage` ✅ | 0 | 0 | 0 | 0 | 0 |
| `categories/modules/direct_sum_objects.sage` | 2 | 2 | 0 | 1 | 0 |
| `categories/modules/fractional_ideals.sage` | 2 | 1 | 1 | 0 | 0 |
| `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` | 13 | 11 | 2 | 8 | 1 |
| `categories/modules/framed/finitely_generated/finitely_presented_modules.sage` | 13 | 12 | 1 | 9 | 0 |
| `categories/modules/framed/finitely_generated/finitely_presented_torsion_modules.sage` | 10 | 8 | 2 | 4 | 0 |
| `categories/modules/framed/formed/form_modules.sage` | 32 | 27 | 5 | 21 | 0 |
| `categories/modules/framed/formed/integrallattice/coxeter_diagrams.sage` | 4 | 4 | 0 | 0 | 0 |
| `categories/modules/framed/formed/integrallattice/hyperbolic_lattices.sage` | 2 | 2 | 0 | 1 | 0 |
| `categories/modules/framed/formed/integrallattice/integral_lattices.sage` | 30 | 23 | 7 | 19 | 0 |
| `categories/modules/framed/formed/integrallattice/lattice_homomorphisms.sage` | 6 | 6 | 0 | 5 | 0 |
| `categories/modules/framed/formed/integrallattice/lattice_isometries.sage` | 10 | 7 | 3 | 4 | 2 |
| `categories/modules/framed/formed/integrallattice/subobjects.sage` | 8 | 7 | 1 | 4 | 0 |
| `categories/modules/framed/formed/torsionform/discriminant_bilinear_modules.sage` | 14 | 13 | 1 | 11 | 0 |
| `categories/modules/framed/formed/torsionform/discriminant_quadratic_modules.sage` | 15 | 14 | 1 | 12 | 0 |
| `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` | 13 | 8 | 5 | 4 | 1 |
| `categories/modules/framed/framed_free_modules.sage` | 6 | 5 | 1 | 2 | 0 |
| `categories/modules/framed/framed_modules.sage` | 5 | 3 | 2 | 3 | 0 |
| `categories/modules/functors/base_change_adjunction.sage` | 5 | 4 | 1 | 3 | 1 |
| `categories/modules/functors/free_forgetful_adjunction.sage` | 2 | 1 | 1 | 1 | 0 |
| `categories/modules/functors/trivial_action.sage` | 6 | 4 | 2 | 0 | 1 |
| `categories/modules/group_modules/group_lattices.sage` | 14 | 11 | 3 | 11 | 1 |
| `categories/modules/group_modules/group_modules.sage` | 23 | 19 | 4 | 16 | 1 |
| `categories/modules/module_morphisms/module_morphisms.sage` | 17 | 14 | 3 | 11 | 0 |
| `categories/modules/pure/finitely_generated/finitely_generated_modules.sage` ✅ | 0 | 0 | 0 | 0 | 0 |
| `categories/modules/pure/free_modules.sage` ✅ | 0 | 0 | 0 | 0 | 0 |
| `categories/modules/pure/torsion_modules.sage` ✅ | 0 | 0 | 0 | 0 | 0 |
| `categories/modules/scalar_actions.sage` ✅ | 0 | 0 | 0 | 0 | 0 |
| `categories/schemes/ambient_spaces.sage` | 3 | 3 | 0 | 0 | 0 |
| `categories/schemes/ringed_spaces.sage` | 3 | 1 | 2 | 0 | 2 |
| `categories/schemes/scheme_morphisms.sage` ✅ | 0 | 0 | 0 | 0 | 0 |
| `categories/schemes/scheme_points.sage` | 1 | 1 | 0 | 0 | 1 |
| `categories/schemes/schemes.sage` | 9 | 8 | 1 | 2 | 2 |
| `categories/schemes/subschemes.sage` | 4 | 4 | 0 | 3 | 1 |
| `categories/schemes/varieties.sage` | 4 | 4 | 0 | 0 | 1 |
| `categories/sets/sets.sage` | 3 | 1 | 2 | 0 | 0 |
| `init.sage` | 9 | 1 | 8 | 0 | 8 |
| `install.sage` | 12 | 10 | 2 | 0 | 12 |
| `refine.sage` ✅ | 0 | 0 | 0 | 0 | 0 |
| `sterk.sage` | 4 | 3 | 1 | 0 | 0 |

### Per-file name map

<details><summary>Which sibling owns each name (expand)</summary>


**`catalogue.sage`**

- `_integral_lattice_with_names` (52x) — from `categories/modules/framed/formed/integrallattice/integral_lattices.sage` — top-level, required at import
- `zipsum` (44x) — from `utilities.py` — top-level, required at import
- `register_indecomposable` (6x) — from `categories/modules/framed/formed/integrallattice/integral_lattices.sage` — top-level, required at import
- `IntegralLattices` (2x) — from `categories/modules/framed/formed/integrallattice/integral_lattices.sage` — top-level
- `_apply_names` (1x) — from `categories/modules/framed/formed/integrallattice/integral_lattices.sage` — top-level

**`categories/abstract_categories/arrow_categories.sage`**

- `sole_structure_generators` (3x) — from `categories/abstract_categories/slice_categories.sage` — defer (cycle)
- `refine` (2x) — from `refine.sage` — top-level

**`categories/abstract_categories/products.sage`**

- `refine` (5x) — from `refine.sage` — top-level

**`categories/abstract_categories/slice_categories.sage`**

- `refine` (6x) — from `refine.sage` — top-level
- `Algebras` (1x) — from `categories/algebras/algebras.sage` — defer (cycle)

**`categories/algebras/algebras.sage`**

- `FreeAlgebras` (1x) — from `categories/algebras/free_algebras.sage` — defer (cycle)
- `FramedModules` (1x) — from `categories/modules/framed/framed_modules.sage` — defer (cycle)

**`categories/algebras/finitely_presented_algebras.sage`**

- `FreeAlgebraOn` (2x) — from `categories/algebras/framed_free_algebras.sage` — top-level
- `FreeAlgebras` (1x) — from `categories/algebras/free_algebras.sage` — top-level

**`categories/algebras/framed_free_algebras.sage`**

- `FreeModuleOnSetElement` (2x) — from `categories/modules/framed/framed_free_modules.sage` — defer (cycle)
- `FreeModuleOnSet` (2x) — from `categories/modules/framed/framed_free_modules.sage` — defer (cycle)
- `_as_set` (2x) — from `categories/sets/sets.sage` — top-level
- `FramedFreeModules` (2x) — from `categories/modules/framed/framed_free_modules.sage` — defer (cycle)
- `module_homset` (2x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `ModuleMorphism` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FreeAlgebras` (1x) — from `categories/algebras/free_algebras.sage` — defer (cycle)
- `FramedAlgebras` (1x) — from `categories/algebras/algebras.sage` — defer (cycle)
- `finite_ordered_set` (1x) — from `categories/sets/sets.sage` — top-level

**`categories/algebras/free_algebras.sage`**

- `FreeModules` (1x) — from `categories/modules/pure/free_modules.sage` — top-level
- `FreeAlgebraOn` (1x) — from `categories/algebras/framed_free_algebras.sage` — defer (cycle)
- `Algebras` (1x) — from `categories/algebras/algebras.sage` — defer (cycle)

**`categories/divisors/cartier_divisor_groups.sage`**

- `refine` (1x) — from `refine.sage` — top-level

**`categories/divisors/class_groups.sage`**

- `refine` (1x) — from `refine.sage` — top-level

**`categories/divisors/divisor_groups.sage`**

- `FramedFreeModules` (2x) — from `categories/modules/framed/framed_free_modules.sage` — top-level
- `refine` (1x) — from `refine.sage` — top-level

**`categories/divisors/picard_groups.sage`**

- `refine` (1x) — from `refine.sage` — top-level

**`categories/divisors/weil_divisor_groups.sage`**

- `refine` (1x) — from `refine.sage` — top-level
- `FramedFreeModules` (1x) — from `categories/modules/framed/framed_free_modules.sage` — top-level
- `DivisorGroups` (1x) — from `categories/divisors/divisor_groups.sage` — top-level

**`categories/forms/forms.sage`**

- `_coordinate_vector` (3x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FormModule` (2x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `_underlying_module` (2x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FormModuleElement` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)

**`categories/group/finitely_presented_groups.sage`**

- `hook_post_init` (1x) — from `refine.sage` — top-level
- `OwnedGroups` (1x) — from `categories/group/groups.sage` — top-level

**`categories/group/groups.sage`**

- `finite_ordered_set` (2x) — from `categories/sets/sets.sage` — top-level
- `module_over_ring` (1x) — from `categories/modules/scalar_actions.sage` — top-level

**`categories/modules/direct_sum_objects.sage`**

- `Subobjects` (1x) — from `categories/modules/framed/formed/integrallattice/subobjects.sage` — defer (cycle)
- `finite_ordered_set` (1x) — from `categories/sets/sets.sage` — top-level

**`categories/modules/fractional_ideals.sage`**

- `finite_ordered_set` (2x) — from `categories/sets/sets.sage` — top-level

**`categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage`**

- `FreeModuleOnSet` (3x) — from `categories/modules/framed/framed_free_modules.sage` — defer (cycle)
- `_as_set` (2x) — from `categories/sets/sets.sage` — top-level
- `FreeModuleOn` (1x) — from `categories/modules/framed/framed_free_modules.sage` — defer (cycle)
- `FramedFreeModules` (1x) — from `categories/modules/framed/framed_free_modules.sage` — defer (cycle)
- `FinitelyGeneratedModules` (1x) — from `categories/modules/pure/finitely_generated/finitely_generated_modules.sage` — top-level
- `_independent_module_generators` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `Subobject` (1x) — from `categories/modules/framed/formed/integrallattice/subobjects.sage` — defer (cycle)
- `finite_ordered_set` (1x) — from `categories/sets/sets.sage` — top-level
- `ModuleAutomorphismGroup` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `module_homset` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `_finite_module_generator_assignment` (1x) — from `categories/modules/framed/framed_modules.sage` — defer (cycle)

**`categories/modules/framed/finitely_generated/finitely_presented_modules.sage`**

- `BasedFreeModule` (3x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — defer (cycle)
- `refine` (2x) — from `refine.sage` — top-level
- `Isomorphism` (2x) — from `categories/abstract_categories/arrow_categories.sage` — defer (cycle)
- `_module_morphism` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `module_homset` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `_underlying_module` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FinitelyGeneratedModules` (1x) — from `categories/modules/pure/finitely_generated/finitely_generated_modules.sage` — top-level
- `ModuleMorphism` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FormMorphism` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `FinitelyPresentedTorsionModules` (1x) — from `categories/modules/framed/finitely_generated/finitely_presented_torsion_modules.sage` — defer (cycle)
- `zipsum` (1x) — from `utilities.py` — top-level
- `_coordinate_vector` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)

**`categories/modules/framed/finitely_generated/finitely_presented_torsion_modules.sage`**

- `finite_ordered_set` (3x) — from `categories/sets/sets.sage` — top-level
- `own_group` (3x) — from `categories/group/groups.sage` — top-level
- `FinitelyPresentedModule` (2x) — from `categories/modules/framed/finitely_generated/finitely_presented_modules.sage` — defer (cycle)
- `BasedFreeModule` (2x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — defer (cycle)
- `TorsionModules` (1x) — from `categories/modules/pure/torsion_modules.sage` — top-level
- `FinitelyPresentedModules` (1x) — from `categories/modules/framed/finitely_generated/finitely_presented_modules.sage` — defer (cycle)
- `_module_morphism` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `zipsum` (1x) — from `utilities.py` — top-level

**`categories/modules/framed/formed/form_modules.sage`**

- `refine` (14x) — from `refine.sage` — top-level
- `TorsionModulesWithForm` (4x) — from `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` — defer (cycle)
- `ModuleMorphism` (3x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `_forget_form_element` (3x) — from `categories/forms/forms.sage` — defer (cycle)
- `BilinearFormMorphism` (2x) — from `categories/forms/forms.sage` — defer (cycle)
- `QuadraticFormMorphism` (2x) — from `categories/forms/forms.sage` — defer (cycle)
- `zipsum` (2x) — from `utilities.py` — top-level
- `FinitelyGeneratedModules` (2x) — from `categories/modules/pure/finitely_generated/finitely_generated_modules.sage` — top-level
- `FinitelyGeneratedFreeModules` (2x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — defer (cycle)
- `TorsionModules` (2x) — from `categories/modules/pure/torsion_modules.sage` — top-level
- `FramingMorphism` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `module_homset` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `_coordinate_vector` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FramedFreeModules` (1x) — from `categories/modules/framed/framed_free_modules.sage` — defer (cycle)
- `_independent_module_generators` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `finite_ordered_set` (1x) — from `categories/sets/sets.sage` — top-level
- `Subobject` (1x) — from `categories/modules/framed/formed/integrallattice/subobjects.sage` — defer (cycle)
- `BasedFreeModule` (1x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — defer (cycle)
- `BilinearForm` (1x) — from `categories/forms/forms.sage` — defer (cycle)
- `FreeModules` (1x) — from `categories/modules/pure/free_modules.sage` — top-level
- `refine_one_lattice` (1x) — from `categories/modules/framed/formed/integrallattice/integral_lattices.sage` — defer (cycle)
- `_decompose_lattice` (1x) — from `categories/modules/framed/formed/integrallattice/integral_lattices.sage` — defer (cycle)
- `GroupModule` (1x) — from `categories/modules/group_modules/group_modules.sage` — defer (cycle)
- `_action_preserves_form` (1x) — from `categories/modules/group_modules/group_lattices.sage` — defer (cycle)
- `_install_group_lattice_structure` (1x) — from `categories/modules/group_modules/group_lattices.sage` — defer (cycle)
- `_finite_module_generator_assignment` (1x) — from `categories/modules/framed/framed_modules.sage` — defer (cycle)
- `GroupLattices` (1x) — from `categories/modules/group_modules/group_lattices.sage` — defer (cycle)

**`categories/modules/framed/formed/integrallattice/coxeter_diagrams.sage`**

- `_integral_lattice_with_names` (6x) — from `categories/modules/framed/formed/integrallattice/integral_lattices.sage` — top-level
- `finite_ordered_set` (5x) — from `categories/sets/sets.sage` — top-level
- `FormMorphism` (2x) — from `categories/modules/framed/formed/form_modules.sage` — top-level
- `own_group` (1x) — from `categories/group/groups.sage` — top-level

**`categories/modules/framed/formed/integrallattice/hyperbolic_lattices.sage`**

- `IntegralLattices` (1x) — from `categories/modules/framed/formed/integrallattice/integral_lattices.sage` — defer (cycle)
- `zipsum` (1x) — from `utilities.py` — top-level

**`categories/modules/framed/formed/integrallattice/integral_lattices.sage`**

- `finite_ordered_set` (6x) — from `categories/sets/sets.sage` — top-level
- `refine` (4x) — from `refine.sage` — top-level
- `BilinearForm` (3x) — from `categories/forms/forms.sage` — defer (cycle)
- `BasedFreeModule` (3x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — defer (cycle)
- `zipsum` (3x) — from `utilities.py` — top-level
- `Subobject` (2x) — from `categories/modules/framed/formed/integrallattice/subobjects.sage` — defer (cycle)
- `FormModuleElement` (2x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `DiscriminantQuadraticModules` (2x) — from `categories/modules/framed/formed/torsionform/discriminant_quadratic_modules.sage` — defer (cycle)
- `DiscriminantBilinearModules` (2x) — from `categories/modules/framed/formed/torsionform/discriminant_bilinear_modules.sage` — defer (cycle)
- `_matrix_connected_component_cuts` (1x) — from `categories/forms/gram_matrices.sage` — top-level
- `DirectSumDecomposition` (1x) — from `categories/modules/direct_sum_objects.sage` — defer (cycle)
- `FinitelyGeneratedFreeFormModules` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `SymmetricBilinearFormModules` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `module_homset` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `correlation_of` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `group_lattice` (1x) — from `categories/modules/group_modules/group_lattices.sage` — defer (cycle)
- `HyperbolicLattices` (1x) — from `categories/modules/framed/formed/integrallattice/hyperbolic_lattices.sage` — defer (cycle)
- `FormModules` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `lattice_homset` (1x) — from `categories/modules/framed/formed/integrallattice/lattice_homomorphisms.sage` — defer (cycle)
- `FormAutomorphismGroup` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `GroupAction` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `LatticeHomomorphisms` (1x) — from `categories/modules/framed/formed/integrallattice/lattice_homomorphisms.sage` — defer (cycle)
- `LatticeIsometries` (1x) — from `categories/modules/framed/formed/integrallattice/lattice_isometries.sage` — defer (cycle)

**`categories/modules/framed/formed/integrallattice/lattice_homomorphisms.sage`**

- `FormHomset` (2x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `refine` (1x) — from `refine.sage` — top-level
- `FormModules` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `FormMorphism` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `_expand_direct_sum_hom_dict` (1x) — from `categories/modules/direct_sum_objects.sage` — defer (cycle)
- `Subobjects` (1x) — from `categories/modules/framed/formed/integrallattice/subobjects.sage` — defer (cycle)

**`categories/modules/framed/formed/integrallattice/lattice_isometries.sage`**

- `LatticeHomomorphisms` (3x) — from `categories/modules/framed/formed/integrallattice/lattice_homomorphisms.sage` — defer (cycle)
- `FormMorphism` (3x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `FormAutomorphismGroup` (2x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `refine` (2x) — from `refine.sage` — top-level
- `zipsum` (2x) — from `utilities.py` — top-level
- `FiniteAutomorphismSubgroup` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `finite_ordered_set` (1x) — from `categories/sets/sets.sage` — top-level

**`categories/modules/framed/formed/integrallattice/subobjects.sage`**

- `finite_ordered_set` (2x) — from `categories/sets/sets.sage` — top-level
- `Slice` (1x) — from `categories/abstract_categories/slice_categories.sage` — defer (cycle)
- `refine` (1x) — from `refine.sage` — top-level
- `ModuleMorphism` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FormMorphism` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `_coordinate_vector` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `zipsum` (1x) — from `utilities.py` — top-level

**`categories/modules/framed/formed/torsionform/discriminant_bilinear_modules.sage`**

- `FinitelyPresentedTorsionModules` (3x) — from `categories/modules/framed/finitely_generated/finitely_presented_torsion_modules.sage` — defer (cycle)
- `BilinearForm` (2x) — from `categories/forms/forms.sage` — defer (cycle)
- `refine` (2x) — from `refine.sage` — top-level
- `subdivide_form_gram_matrix` (2x) — from `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` — defer (cycle)
- `FormMorphism` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `TorsionModule` (1x) — from `categories/modules/framed/finitely_generated/finitely_presented_torsion_modules.sage` — defer (cycle)
- `TorsionModulesWithForm` (1x) — from `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` — defer (cycle)
- `SymmetricBilinearFormModules` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `regenerating_data` (1x) — from `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` — defer (cycle)
- `cokernel_categories` (1x) — from `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` — defer (cycle)
- `finite_ordered_set` (1x) — from `categories/sets/sets.sage` — top-level
- `p_adic_jordan_module_generators` (1x) — from `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` — defer (cycle)
- `DiscriminantQuadraticModules` (1x) — from `categories/modules/framed/formed/torsionform/discriminant_quadratic_modules.sage` — defer (cycle)

**`categories/modules/framed/formed/torsionform/discriminant_quadratic_modules.sage`**

- `FinitelyPresentedTorsionModules` (3x) — from `categories/modules/framed/finitely_generated/finitely_presented_torsion_modules.sage` — defer (cycle)
- `QuadraticForm` (2x) — from `categories/forms/forms.sage` — defer (cycle)
- `refine` (2x) — from `refine.sage` — top-level
- `subdivide_form_gram_matrix` (2x) — from `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` — defer (cycle)
- `FormMorphism` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `TorsionModule` (1x) — from `categories/modules/framed/finitely_generated/finitely_presented_torsion_modules.sage` — defer (cycle)
- `TorsionModulesWithForm` (1x) — from `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` — defer (cycle)
- `QuadraticFormModules` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `QuadraticForms` (1x) — from `categories/forms/forms.sage` — defer (cycle)
- `regenerating_data` (1x) — from `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` — defer (cycle)
- `cokernel_categories` (1x) — from `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` — defer (cycle)
- `finite_ordered_set` (1x) — from `categories/sets/sets.sage` — top-level
- `p_adic_jordan_module_generators` (1x) — from `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage` — defer (cycle)
- `DiscriminantBilinearModules` (1x) — from `categories/modules/framed/formed/torsionform/discriminant_bilinear_modules.sage` — defer (cycle)

**`categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage`**

- `Subobject` (2x) — from `categories/modules/framed/formed/integrallattice/subobjects.sage` — defer (cycle)
- `_matrix_connected_component_cuts` (1x) — from `categories/forms/gram_matrices.sage` — top-level
- `IntegralLattices` (1x) — from `categories/modules/framed/formed/integrallattice/integral_lattices.sage` — defer (cycle)
- `FinitelyGeneratedFormModules` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `TorsionModules` (1x) — from `categories/modules/pure/torsion_modules.sage` — top-level
- `finite_ordered_set` (1x) — from `categories/sets/sets.sage` — top-level
- `_module_morphism` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `zipsum` (1x) — from `utilities.py` — top-level

**`categories/modules/framed/framed_free_modules.sage`**

- `_as_set` (2x) — from `categories/sets/sets.sage` — top-level
- `refine` (2x) — from `refine.sage` — top-level
- `FreeModules` (1x) — from `categories/modules/pure/free_modules.sage` — top-level
- `BasedFreeModule` (1x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — defer (cycle)
- `FinitelyGeneratedFreeModules` (1x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — defer (cycle)

**`categories/modules/framed/framed_modules.sage`**

- `module_homset` (2x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FramingMorphism` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FramedFreeModules` (1x) — from `categories/modules/framed/framed_free_modules.sage` — defer (cycle)

**`categories/modules/functors/base_change_adjunction.sage`**

- `module_homset` (3x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `Adjunction` (2x) — from `categories/modules/functors/free_forgetful_adjunction.sage` — defer (cycle)
- `BasedFreeModule` (2x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — defer (cycle)
- `zipsum` (1x) — from `utilities.py` — top-level

**`categories/modules/functors/free_forgetful_adjunction.sage`**

- `FreeModuleOnSet` (1x) — from `categories/modules/framed/framed_free_modules.sage` — defer (cycle)

**`categories/modules/functors/trivial_action.sage`**

- `group_lattice` (1x) — from `categories/modules/group_modules/group_lattices.sage` — top-level
- `IntegralLattices` (1x) — from `categories/modules/framed/formed/integrallattice/integral_lattices.sage` — top-level
- `GroupLattices` (1x) — from `categories/modules/group_modules/group_lattices.sage` — top-level
- `group_action_homset` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — top-level

**`categories/modules/group_modules/group_lattices.sage`**

- `FormHomset` (4x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `FormModule` (4x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `FormMorphism` (3x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `GroupAction` (3x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `group_action_homset` (3x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `IntegralLattices` (2x) — from `categories/modules/framed/formed/integrallattice/integral_lattices.sage` — defer (cycle)
- `GroupModules` (2x) — from `categories/modules/group_modules/group_modules.sage` — defer (cycle)
- `Subobject` (1x) — from `categories/modules/framed/formed/integrallattice/subobjects.sage` — defer (cycle)
- `GroupModule` (1x) — from `categories/modules/group_modules/group_modules.sage` — defer (cycle)
- `ModuleMorphism` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FinitelyGeneratedFormModules` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)

**`categories/modules/group_modules/group_modules.sage`**

- `zipsum` (4x) — from `utilities.py` — top-level
- `ModuleMorphism` (3x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `GroupAction` (3x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `finite_ordered_set` (3x) — from `categories/sets/sets.sage` — top-level
- `_coordinate_vector` (3x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `ModuleHomset` (2x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `_independent_module_generators` (2x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `BasedFreeModule` (2x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — defer (cycle)
- `refine` (2x) — from `refine.sage` — top-level
- `group_action_homset` (2x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FinitelyGeneratedFreeModules` (2x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — defer (cycle)
- `FramingMorphism` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `ModuleAutomorphism` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `FinitelyPresentedModule` (1x) — from `categories/modules/framed/finitely_generated/finitely_presented_modules.sage` — defer (cycle)
- `Subobject` (1x) — from `categories/modules/framed/formed/integrallattice/subobjects.sage` — defer (cycle)
- `_coefficients` (1x) — from `categories/modules/module_morphisms/module_morphisms.sage` — defer (cycle)
- `BaseChangeFunctor` (1x) — from `categories/modules/functors/base_change_adjunction.sage` — defer (cycle)
- `DirectSumObjects` (1x) — from `categories/modules/direct_sum_objects.sage` — defer (cycle)
- `_finite_module_generator_assignment` (1x) — from `categories/modules/framed/framed_modules.sage` — defer (cycle)

**`categories/modules/module_morphisms/module_morphisms.sage`**

- `zipsum` (6x) — from `utilities.py` — top-level
- `FinitelyPresentedModule` (5x) — from `categories/modules/framed/finitely_generated/finitely_presented_modules.sage` — defer (cycle)
- `FormModuleElement` (2x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `GroupModuleElement` (2x) — from `categories/modules/group_modules/group_modules.sage` — defer (cycle)
- `BasedFreeModuleElement` (2x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — defer (cycle)
- `FinitelyPresentedModuleElement` (2x) — from `categories/modules/framed/finitely_generated/finitely_presented_modules.sage` — defer (cycle)
- `FramedFreeModules` (2x) — from `categories/modules/framed/framed_free_modules.sage` — defer (cycle)
- `finite_ordered_set` (2x) — from `categories/sets/sets.sage` — top-level
- `FramedModules` (2x) — from `categories/modules/framed/framed_modules.sage` — defer (cycle)
- `refine` (1x) — from `refine.sage` — top-level
- `FormModule` (1x) — from `categories/modules/framed/formed/form_modules.sage` — defer (cycle)
- `FreeModuleOnSetElement` (1x) — from `categories/modules/framed/framed_free_modules.sage` — defer (cycle)
- `FinitelyPresentedModules` (1x) — from `categories/modules/framed/finitely_generated/finitely_presented_modules.sage` — defer (cycle)
- `Subobjects` (1x) — from `categories/modules/framed/formed/integrallattice/subobjects.sage` — defer (cycle)

**`categories/schemes/ambient_spaces.sage`**

- `refine` (2x) — from `refine.sage` — top-level
- `AffineSpaces` (1x) — from `categories/schemes/schemes.sage` — top-level
- `ProjectiveSpaces` (1x) — from `categories/schemes/schemes.sage` — top-level

**`categories/schemes/ringed_spaces.sage`**

- `refine` (2x) — from `refine.sage` — top-level

**`categories/schemes/scheme_points.sage`**

- `SchemeMorphism` (1x) — from `categories/schemes/scheme_morphisms.sage` — top-level, required at import

**`categories/schemes/schemes.sage`**

- `refine` (6x) — from `refine.sage` — top-level
- `Free_ZZ` (4x) — from `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage` — top-level
- `ClosedSubschemes` (3x) — from `categories/schemes/subschemes.sage` — defer (cycle)
- `LocallyRingedSpace` (2x) — from `categories/schemes/ringed_spaces.sage` — top-level, required at import
- `PicardGroup` (2x) — from `categories/divisors/picard_groups.sage` — top-level
- `ClassGroup` (2x) — from `categories/divisors/class_groups.sage` — top-level
- `OpenSubschemes` (2x) — from `categories/schemes/subschemes.sage` — defer (cycle)
- `LocallyRingedSpaces` (1x) — from `categories/schemes/ringed_spaces.sage` — top-level

**`categories/schemes/subschemes.sage`**

- `Scheme` (4x) — from `categories/schemes/schemes.sage` — defer (cycle)
- `SchemeElement` (4x) — from `categories/schemes/schemes.sage` — defer (cycle)
- `refine` (2x) — from `refine.sage` — top-level
- `Schemes` (2x) — from `categories/schemes/schemes.sage` — defer (cycle)

**`categories/schemes/varieties.sage`**

- `refine` (4x) — from `refine.sage` — top-level
- `Scheme` (2x) — from `categories/schemes/schemes.sage` — top-level, required at import
- `SchemeElement` (2x) — from `categories/schemes/schemes.sage` — top-level
- `Schemes` (1x) — from `categories/schemes/schemes.sage` — top-level

**`categories/sets/sets.sage`**

- `refine` (7x) — from `refine.sage` — top-level

**`init.sage`**

- `Lattices` (1x) — from `catalogue.sage` — top-level, required at import

**`install.sage`**

- `install_finitely_presented_groups` (1x) — from `categories/group/finitely_presented_groups.sage` — top-level, required at import
- `install_finitely_presented_algebras` (1x) — from `categories/algebras/finitely_presented_algebras.sage` — top-level, required at import
- `install_algebras` (1x) — from `categories/algebras/algebras.sage` — top-level, required at import
- `install_ringed_spaces` (1x) — from `categories/schemes/ringed_spaces.sage` — top-level, required at import
- `install_schemes` (1x) — from `categories/schemes/schemes.sage` — top-level, required at import
- `install_scheme_morphisms` (1x) — from `categories/schemes/scheme_morphisms.sage` — top-level, required at import
- `install_scheme_points` (1x) — from `categories/schemes/scheme_points.sage` — top-level, required at import
- `install_ambient_spaces` (1x) — from `categories/schemes/ambient_spaces.sage` — top-level, required at import
- `install_subschemes` (1x) — from `categories/schemes/subschemes.sage` — top-level, required at import
- `install_varieties` (1x) — from `categories/schemes/varieties.sage` — top-level, required at import

**`sterk.sage`**

- `Lattices` (8x) — from `catalogue.sage` — top-level
- `Embeddings` (1x) — from `catalogue.sage` — top-level
- `FiniteCoxeterDiagram` (1x) — from `categories/modules/framed/formed/integrallattice/coxeter_diagrams.sage` — top-level

</details>


## Names from outside the preamble

Import lines below were verified in this Sage: the module named actually binds
that name to the same object `sage.all` exposes. Do not guess these -- several
Sage globals are not the class of the same name.

| name | uses | import |
|---|---:|---|
| `load` | 59 | `from sage.misc.persist import load` |
| `ZZ` | 57 | `from sage.rings.all import ZZ` |
| `Modules` | 16 | `from sage.categories.modules import Modules` |
| `cached_method` | 16 | `from sage.misc.cachefunc import cached_method` |
| `Parent` | 6 | `from sage.structure.parent import Parent` |
| `QQ` | 5 | `from sage.rings.rational_field import QQ` |
| `Groups` | 4 | `from sage.categories.groups import Groups` |
| `value` | 4 | — *not a Sage global* |
| `Sets` | 3 | `from sage.categories.sets_cat import Sets` |
| `indexed` | 3 | — *not a Sage global* |
| `cached_function` | 2 | `from sage.misc.cachefunc import cached_function` |
| `Element` | 2 | — *not a Sage global* |
| `UnderlyingSet` | 2 | — *not a Sage global* |
| `ring` | 2 | — *not a Sage global* |
| `Matrix` | 2 | `from sage.matrix.constructor import Matrix` |
| `scalar` | 2 | — *not a Sage global* |
| `Category` | 2 | `from sage.categories.category import Category` |
| `identity_matrix` | 2 | `from sage.matrix.special import identity_matrix` |
| `Morphism` | 2 | `from sage.categories.morphism import Morphism` |
| `NN` | 2 | `from sage.rings.semirings.non_negative_integer_semiring import NN` |
| `RR` | 2 | `from sage.rings.all import RR` |
| `PolynomialRing` | 1 | `from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing` |
| `Infinity` | 1 | `from sage.rings.infinity import Infinity` |
| `vector` | 1 | `from sage.modules.free_module_element import vector` |
| `SetMorphism` | 1 | — *not a Sage global* |
| `block_diagonal_matrix` | 1 | `from sage.matrix.special import block_diagonal_matrix` |
| `MorphismMatrix` | 1 | — *not a Sage global* |
| `first` | 1 | — *not a Sage global* |
| `lcm` | 1 | `from sage.arith.functions import lcm` |
| `CyclotomicField` | 1 | `from sage.rings.number_field.number_field import CyclotomicField` |
| `prod` | 1 | `from sage.misc.misc_c import prod` |
| `CC` | 1 | `from sage.rings.cc import CC` |
| `latex` | 1 | `from sage.misc.latex import latex` |
| `get_ipython` | 1 | — *not a Sage global* |

## Cycles


**Group 1 — 26 files.** Hoisting every cross-reference in this group to
a top-level import would deadlock. The names marked `defer` above are the edges to
move inside functions.

- `categories/abstract_categories/arrow_categories.sage`
- `categories/abstract_categories/slice_categories.sage`
- `categories/algebras/algebras.sage`
- `categories/algebras/framed_free_algebras.sage`
- `categories/algebras/free_algebras.sage`
- `categories/forms/forms.sage`
- `categories/modules/direct_sum_objects.sage`
- `categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage`
- `categories/modules/framed/finitely_generated/finitely_presented_modules.sage`
- `categories/modules/framed/finitely_generated/finitely_presented_torsion_modules.sage`
- `categories/modules/framed/formed/form_modules.sage`
- `categories/modules/framed/formed/integrallattice/hyperbolic_lattices.sage`
- `categories/modules/framed/formed/integrallattice/integral_lattices.sage`
- `categories/modules/framed/formed/integrallattice/lattice_homomorphisms.sage`
- `categories/modules/framed/formed/integrallattice/lattice_isometries.sage`
- `categories/modules/framed/formed/integrallattice/subobjects.sage`
- `categories/modules/framed/formed/torsionform/discriminant_bilinear_modules.sage`
- `categories/modules/framed/formed/torsionform/discriminant_quadratic_modules.sage`
- `categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage`
- `categories/modules/framed/framed_free_modules.sage`
- `categories/modules/framed/framed_modules.sage`
- `categories/modules/functors/base_change_adjunction.sage`
- `categories/modules/functors/free_forgetful_adjunction.sage`
- `categories/modules/group_modules/group_lattices.sage`
- `categories/modules/group_modules/group_modules.sage`
- `categories/modules/module_morphisms/module_morphisms.sage`

**Group 2 — 2 files.** Hoisting every cross-reference in this group to
a top-level import would deadlock. The names marked `defer` above are the edges to
move inside functions.

- `categories/schemes/schemes.sage`
- `categories/schemes/subschemes.sage`

* * *

# Open

## The discriminant form has no general target

`discriminant_group()` builds its form over `QmodnZ(1)` and `QmodnZ(2)`. The
mathematics is more general: for an $R$-lattice $L$ with fraction field $K$, the
discriminant group $A_L=L^\vee/L$ carries an induced $K/R$-valued bilinear form,
and a $K/2R$-valued quadratic form when $L$ is even.

The gap is not that the general case is unimplemented. It is that **the preamble
has no object for $K/R$**, so the theorem it implements cannot be stated in its
own vocabulary. Every method downstream of `discriminant_group` therefore
specializes to $\ZZ$ silently — there is no name whose absence is felt.

Decide before implementing: what is the general target object, and does it belong
to the forms layer (a value module built from a base ring and its fraction field)
or to the rings layer (a quotient the ring itself can name)? `QmodnZ(n)` becomes
the $R=\ZZ$ instance of whatever that is.

## Equivariance is checked by enumerating a group

`group_lattices.sage:171-184` ranges over every element of the acting group. That
is what forces `assert group.is_finite()` at `group_lattices.sage:18` and
`group_modules.sage:27`, which excludes infinite-order isometries — the generic
case for indefinite lattices.

The design was settled in an earlier session and never implemented: probe
predicates answering `True | False | Unknown` (`is_finitely_generated`,
`generators_are_computable`, `has_computed_generators`), the check run **on
generators** where they are available, a flag on morphism construction that forces
the computation, and a recorded flag saying whether equivariance was actually
checked rather than pretending it was.

The same defect in `descends_along` is fixed (`ace125f`); this one is the original.

## Form evaluation re-derives coordinates

Each form evaluation re-enters Sage's coordinate machinery
(`free_module.coordinate_ring`) instead of multiplying by a presentation the form
already holds, so evaluation cost grows with the rank of the module rather than
staying flat in it. Measure it that way before changing anything: wall time of a
fixed number of evaluations at ranks 2, 8, 22, and check whether the curve is
flat. This is the suspected floor under the remaining slow tests, including the
90s `test_catalogue_latex_fits_mathjax_and_has_balanced_environments`.
