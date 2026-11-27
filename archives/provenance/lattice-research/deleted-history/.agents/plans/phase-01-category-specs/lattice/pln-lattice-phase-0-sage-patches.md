---
trackerStatus:
  type: plan
title: 'Phase 0 Sage patch prerequisites for ModulesWithForms'
status: approved
planId: PLN-LAT-010
planType: implementation-phase
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
parentPlan: PLN-LAT-000
tasks:
  - TASK-LAT-PHASE0-MODULE-BASE-RINGS
  - TASK-LAT-PHASE0-IDEAL-QUOTIENT-MODULES
  - TASK-LAT-PHASE0-FRACTION-QUOTIENT-CODOMAINS
  - TASK-LAT-PHASE0-COMPLETIONS-LOCALIZATIONS
  - TASK-LAT-PHASE0-MODULE-ENRICHMENT
  - TASK-LAT-PHASE0-MODULE-OPERATIONS
  - TASK-LAT-PHASE0-HOM-ENRICHMENT
tags:
  - category-specs
  - plan
  - lattices
  - theme-modules-tensors
---

Migrated source: this plan contains the full content formerly stored at `plans/PHASE_0_SAGE_PATCHES.md`. The old `plans/` copy was removed so this tracked plan is the active planning document.

# Phase 0: Sage Patches

## Grounded Implementation Contract

### Canonical source set
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/homsets/docs/MAPPING.md`
- `category_specs/forms/docs/MAPPING.md`
- `theory/backends/software-capability-map.md`
- `theory/foundations/bilinear-forms-duals-morphisms.md`

### Target public surface
- Install `ModuleBaseRings` on target PID bases and route Sage ring/module behavior into
  redesigned categories under `src/sage_patches/`.
- Make ideal-submodule, fraction-quotient, completion/localization, module enrichment,
  module operations, and hom enrichment changes concrete and testable at file-level targets:
  - `ring_base_category.py`
  - `ideal_submodule.py`
  - `fraction_quotients.py`
  - `completions.py`
  - `module_enrichment.py`
  - `module_operations.py`
  - `hom_enrichment.py`

### Contract obligations (plan-level)
- Every child TASK card in `PLN-LAT-010` must include an explicit implementation contract
  for:
  1) exact noun ownership (`Modules`, `Forms`, hom sets),
  2) method semantics (`quotient`, `tensor`, `base_change`, `dual`, `cokernel`, etc.),
  3) codomain/return categories,
  4) acceptance checks from `tests/sage_spec/misc.sage`.
- Child cards should not introduce non-document source gates; all work is directly grounded
  in the listed canonical sources and then expressed as code-level API obligations.
- `_install.py` remains the single dependency-order entry point and must call each child
  module `install()` after prerequisites.

### Acceptance criteria (phase gate)
- `[ ]` `tests/sage_spec/misc.sage` is executable after all module installs, including
  discriminant-form codomain checks.
- `[ ]` Phase 1 prerequisites are available: `FormCodomain.torsion_bilinear(ZZ)`,
  `FormCodomain.torsion_quadratic(ZZ)`, and form evaluation into `QQ/ZZ`, `QQ/2ZZ`.
- `[ ]` No method contracts in this phase depend on ad hoc helper methods outside mapped
  category owners in the canonical sources.

## Admitted Definitions

Phase 0 child work may rely on these definitions:

- `ModuleBaseRings` targets commutative PIDs used as base rings for finitely presented
  module structure. Current target families are `ZZ`, `Zp(p)`, `QQ`, `RR`, `CC`,
  `QQbar`, and finite fields `GF(p^n)`. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- `R^n` is an enriched free `R`-module object, not a raw vector object. It should land
  in the redesigned `Modules(R)` surface after `ModuleBaseRings` refinement. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- `r * R` and `R * r` mean the principal ideal as an ideal-submodule of `R`; for
  `A = R` as an `R`-module, `n * A` is the submodule `{n*v : v in A}`. Sources:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md` and
  `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`.
- `R / I` is a finitely presented `R`-module quotient object in the enriched module
  surface. Quotient objects must retain module semantics even when Sage returns a ring
  parent such as `ZZ/(n)`. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- Localizations, completions, and fraction fields returned from target base rings must
  be refined back into `ModuleBaseRings` when the returned ring remains in scope, so
  downstream module/form expressions preserve the same category vocabulary. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.

Standalone monkeypatch modules that make existing Sage objects support the
syntax and semantics required by `tests/sage_spec/misc.sage`. These patches
are **prerequisites** for Phase 1: the BilinearModule category cannot work
over general R without them, and discriminant form descent requires QQ/ZZ and
QQ/2ZZ as working codomains.

Phase 0 does NOT touch the existing `src/lattices/` hierarchy. It creates
new files under `src/sage_patches/` that can be imported independently.

Canonical spec: `tests/sage_spec/misc.sage`.

Implementation model: define a new Sage category `ModuleBaseRings`, a
subcategory of `Rings().PrincipalIdealDomains().Commutative()`, and install it
into the target ring parents via `_refine_category_`.  No new Python class is
created for each ring family; the ring object's `__class__` does not change;
native Sage coercions, arithmetic, and completions are fully preserved.

The `ParentMethods` of `ModuleBaseRings` define the selected overrides:
`__pow__` to return enriched free modules, `ideal()` / `__mul__` / `__rmul__`
to return *ideal-submodule* objects (Sage ideals whose categories are refined
to also carry `R`-module structure), and `quotient()` to return finitely
presented `R`-module objects.  Each override calls `super()` to obtain the
native Sage result and then calls `result._refine_category_(...)` on it.

The front-door entry point is `install()` in `ring_base_category.py`, which
iterates over the target rings and calls
`ring._refine_category_(ModuleBaseRings())` on each.  After that call, Sage's
dynamic dispatch automatically serves the `ParentMethods` overrides for
that ring instance without any monkeypatching.

The base-ring enrichment targets commutative base rings whose finitely
presented module categories have a usable structure theorem. Phase 0 keeps
that scope at PIDs, specifically `ZZ`, `Zp(p)`, `QQ`, `RR`, `CC`, `QQbar`,
and finite fields `GF(p^n)`. Later phases may widen the same interface to
Dedekind domains, including rings of integers of number fields with class
number greater than one, once ideal-class and projective-module data are part
of the module layer.

There is no implementation-class split by ring family.  All target rings are
enriched by the single `ModuleBaseRings` category via `_refine_category_`.


## File Structure

```
src/sage_patches/
    __init__.py              # imports install(); calls it on module import
    ring_base_category.py    # ModuleBaseRings category + install()
    ideal_submodule.py       # IdealSubmodule category; _refine_category_ target for ideals
    fraction_quotients.py    # QQ/ZZ, QQ/nZZ quotient modules
    module_enrichment.py     # Enriched Modules(R) surface; _refine_category_ for free/FGP modules
    module_operations.py     # free_part, torsion_part, generator assignment
    hom_enrichment.py        # Hom spaces: from_*, cokernel().projection()
    completions.py           # ZZ.complete(p) and ZZ.localize(p) convenience aliases
    _install.py              # Single entry point that calls each module's install()
```

## Dependency Order

```
ring_base_category      (no internal deps — defines ModuleBaseRings, calls _refine_category_ on target rings)
ideal_submodule         (depends on ring_base_category — category injected into Sage ideal objects)
fraction_quotients      (depends on ideal_submodule — QQ/ZZ refined as module)
completions             (depends on ring_base_category — localization/completion refinement)
module_enrichment       (depends on ring_base_category, ideal_submodule, fraction_quotients)
module_operations       (depends on module_enrichment)
hom_enrichment          (depends on module_enrichment, module_operations)
_install                (imports and applies all of the above)
```


## Module-by-Module Design


### `ring_base_category.py` -- ModuleBaseRings category and installation

#### What Sage provides natively

- `ZZ.quotient(2*ZZ)` returns `IntegerModRing(2)`.
- `ZZ / 2` raises `TypeError` -- `Rings.ParentMethods.__truediv__` blocks it.
- `IntegerModRing(p).is_field()` returns True for primes.
- `IntegerModRing(n) in Modules(ZZ)` returns False.

#### What to build

Define the `ModuleBaseRings` category (see `category_specs/rings.py`) with
`ParentMethods.quotient()` interpreting `R / n` as `R.quotient(n * R)` when
`n` is an element, and as `R.quotient(I)` when `n` is an `R`-ideal.  The
`__truediv__` final method on `ParentMethods` delegates to `quotient()`, so
`ZZ / 2` and `ZZ / (2*ZZ)` both route through the single override.

The `quotient()` override calls Sage's native `quotient()` via `super()`, then
refines the returned ring via `result._refine_category_(...)` so
`IntegerModRing(n)` becomes a finitely presented `ZZ`-module object.  No
direct monkeypatch of `IntegerRing_class.__truediv__` is needed.

The `install()` function calls `ZZ._refine_category_(ModuleBaseRings())` (and
similarly for `QQ`, `Zp(p)`, etc.), after which `ZZ.quotient`, `ZZ.__pow__`,
and `ZZ.ideal` all dispatch through `ModuleBaseRings.ParentMethods`.

Category containment (`IntegerModRing(n) in Modules(ZZ)`) is handled by
patching `Modules(ZZ).__contains__` to also accept any parent whose category
is a join including `ModuleBaseRings()` or whose `base_ring()` is `ZZ` and
whose `_refine_category_` has already been called.  This avoids deep surgery
on Sage's category caching infrastructure.

#### Spec assertions covered

```python
Z2 = ZZ / (2*ZZ)
Z4 = ZZ / (4*ZZ)
R = 2*ZZ
assert Z2 == ZZ/2
assert Z4 == ZZ/4
assert ZZ in Modules(ZZ)
assert R in Modules(ZZ)
assert Z2 in Modules(ZZ)
assert Z2 in Modules(Z2)
assert Z2.is_field() and not Z4.is_field()
```


### `fraction_quotients.py` -- QQ/ZZ, QQ/nZZ quotient modules

#### What Sage provides natively

- `QQ / ZZ` might not work natively. Sage has `QmodnZ(1)` for Q/Z, accessed
  via `QQ.quotient_ring(ZZ)` or similar -- needs investigation at
  implementation time.
- `QmodnZ(n)` elements have `.lift()` returning canonical representative.
- `QmodnZ(1)(1/2) == QmodnZ(1)(3/2)` should work.
- `QmodnZ(n)` is in "infinite commutative additive groups" -- NOT in
  `Modules(ZZ)`.

#### What to build

Ensure `QQ / ZZ` and `QQ / (n*ZZ)` produce `QmodnZ(1)` and `QmodnZ(n)`
respectively. This may require patching `QQ.__truediv__` or
`RationalField.__truediv__` to detect when the divisor is ZZ or a ZZ-ideal.

Patch `QmodnZ` to be recognized as a ZZ-module (same category containment
approach as ring_quotients).

Ensure `QmodnZ(n)` has `base_ring()` returning ZZ (likely needs
monkeypatching).

**Critical for Phase 1:** QQ/ZZ is the codomain for discriminant bilinear
forms, QQ/2ZZ for discriminant quadratic forms. These must work as targets
for form evaluation.

#### Spec assertions covered

```python
R = QQ/ZZ
assert R in Modules(ZZ)
assert R(1/2) == R(3/2)
assert R(3/2).lift() == QQ(1/2)
```

#### Investigation needed at implementation time

- Exact Sage class hierarchy for `QmodnZ`.
- Whether `QQ.__truediv__` already dispatches to `QmodnZ`.
- Whether `QmodnZ` has arithmetic operations (+, *, coercion from QQ)
  sufficient for form evaluation.


### `completions.py` -- ZZ.complete(p), ZZ.localize(p)

#### What Sage provides natively

- `ZZ.completion(5, 20)` returns `Zp(5, prec=20)`.
- `Localization(ZZ, (5,))` returns the localization.
- `Zp(5).fraction_field()` returns `Qp(5)`.
- `ZZ.fraction_field()` returns `QQ`.
- ZZ has NO `.complete()` or `.localize()` method.

#### What to build

`ModuleBaseRings.ParentMethods` already provides `complete` and `localize` as
`@final` aliases for `completion` and `localization` respectively.  The
`completion` override in `ParentMethods` calls Sage's native `completion()`
via `super()` and then refines the returned ring with `_refine_category_`.
The `localization` override does the same.

The `completions.py` module therefore only needs to ensure that the
`ModuleBaseRings` category is installed (i.e., `ring_base_category.install()`
has been called) before any `complete`/`localize` call is made.  No
additional attribute assignments on `IntegerRing_class` are needed.

These are mathematically unambiguous and require no design decisions beyond
the `_refine_category_` pattern.

#### Spec assertions covered

```python
S = ZZ.complete(5)
assert S == Zp(5)
assert (ZZ^3).base_change(S) == S^3
assert ZZ.fraction_field() == QQ
assert Zp(5).fraction_field() == Qp(5)

ZZ_L5 = ZZ.localize(5)
assert ZZ_L5 == Localization(ZZ, [5])
assert 1/5 in ZZ_L5 and 1/3 not in ZZ_L5
```


### `module_enrichment.py` -- ZZ^n as enriched FGP module

This is the most substantial patch module.

#### What Sage provides natively

- `ZZ^3` returns `FreeModule_ambient_pid` with `.gens()`, `.rank()`,
  `.Hom()`, `.direct_sum()`.
- Missing: `.dual()`, `.tensor()`, `.base_change()`, `.is_free()`,
  `.is_torsionfree()`, `.is_torsion()`.
- `M + M` means "span inside ambient" for free modules -- NOT direct sum.
- `FGP_Module` (quotient modules) lacks `.direct_sum()`.

#### What to build

Monkeypatch onto `FreeModule_ambient_pid` and/or `FGP_Module_class`:

**Predicate methods:**
- `is_free()`: True for free modules, check invariants for FGP.
- `is_torsionfree()`: True for free modules, check invariants for FGP.
- `is_torsion()`: False for free modules, check invariants for FGP.

**Dual:**
- `dual()` = `self.Hom(ZZ)` (the rank-1 free module as target). For ZZ^n
  this is isomorphic to ZZ^n. The returned object should be a proper
  ZZ-module (hom set in `Modules(ZZ)`).

**Tensor product:**
- `tensor(other)` and `__mul__` on parents: `ZZ^m * ZZ^n` gives
  `ZZ^(m*n)`. For mixed: `(ZZ^n).tensor(ZZ/p)` gives `(ZZ/p)^n`. Use FGP
  module construction with appropriate relations.
- **Parent `*` = tensor, element `*` = bilinear product.** Phase 1 handles
  element `*` via ElementWrapper; this module only patches parent `__mul__`.

**Base change:**
- `base_change(S)` = `self.tensor(S)` where S is a ring viewed as a
  ZZ-module via the structure map.

**Ring-power hook:**
- patch the relevant ring-parent `__pow__` / `free_module` path so `ZZ^n`
  and more generally `R^n` return enriched module objects rather than raw
  Sage `FreeModule` parents.

**Direct sum as `+`:**
- Redefine `__add__` on our enriched modules to mean direct sum, NOT span.
  The spec explicitly rejects the "ambient module" paradigm where `+` means
  span-in-ambient.
- `__pow__` for direct sum powers: `ZZ^3 == ZZ + ZZ + ZZ`.

**Module quotient:**
- `__truediv__` on modules: `M / (n*M)` produces the FGP quotient. Use
  Sage's existing `FGP_Module(M, n*M)` construction.

**Canonical isomorphisms as equalities:**
- `M/(2*M) == M.tensor(Z2)` -- this requires `__eq__` to recognize
  canonically isomorphic FGP modules. This may be the hardest part. One
  approach: define equality as isomorphism of the underlying FGP presentations
  (same invariants in the same order). Another: defer to Sage's `==` on
  FGP modules and verify it already does the right thing.

#### Spec assertions covered

```python
M = ZZ^3
assert M.base_ring() == ZZ
assert M in Modules(ZZ)
assert M.is_free() and M.is_torsionfree()
assert not M.is_torsion()
assert M.rank() == 3
assert M == ZZ + ZZ + ZZ
assert M.dual() == M.Hom(ZZ)
assert M * M == M.tensor(M)
assert M.tensor(Z2) in Modules(Z2)
assert M/(2*M) == M.tensor(Z2)
assert M.base_change(Z2) == M.tensor(Z2)
```

#### Key design decisions

- **Where to patch:** Monkeypatch methods directly onto
  `FreeModule_ambient_pid` and `FGP_Module_class`. Avoid category-level
  method injection which interacts with Sage's aggressive category caching.
- **`+` redefinition risk:** Redefining `+` on free modules breaks Sage's
  native "span" semantics. Since this codebase explicitly rejects the ambient
  module paradigm and controls all call sites, this is acceptable. If
  isolation is needed, scope the patch to only affect objects that have been
  through our enrichment (e.g. via a marker attribute).


### `module_operations.py` -- free_part, torsion_part, generator assignment

#### What to build

Monkeypatch `FGP_Module_class`:
- `free_part()`: Extract the free summand from Smith normal form
  decomposition. If M has invariants `(0, 0, 3, 5)`, then `free_part()` is
  the sub-module corresponding to invariant-0 generators.
- `torsion_part()`: Extract the torsion summand.

Generator assignment `M.<x,y,z> = ZZ^3`:
- Sage's preparser transforms this to `M = expr; (x,y,z) = M._first_ngens(3)`.
- `ZZ^3` already has `._first_ngens(3)` returning the standard basis.
- Verify this works natively and document. If not, patch `_first_ngens`.

#### Spec assertions covered

```python
F1, F2 = ZZ^2, ZZ^3
T1, T2 = ZZ/5, ZZ/7
M1 = F1 + T1
M2 = F2 + T2
assert M1.free_part() == F1 and M1.torsion_part() == T1
assert M2.free_part() == F2 and M2.torsion_part() == T2

M.<x,y,z> = ZZ^3  # generator assignment
```


### `hom_enrichment.py` -- Hom spaces as modules, morphism construction

#### What Sage provides natively

- `(ZZ^2).Hom(ZZ^2)` returns `FreeModuleHomspace`, already in `Modules(ZZ)`.
- `FGP_Homset_class` for FGP module hom sets.
- Morphisms can be constructed from matrices via `__call__`.
- FGP morphisms have `.kernel()` and some `.cokernel()` support.

#### What to build

**On hom spaces (`FreeModuleHomspace` / `FGP_Homset_class`):**
- `from_dict(mapping)`: Given `{gen_i: image_i}`, construct the
  morphism. This resolves the dict to a matrix and delegates to the native
  constructor.
- `from_images(images)`: Given a list of images for each generator,
  construct. Sugar for `from_dict(dict(zip(domain.gens(), images)))`.
- `from_matrix(M)`: Named constructor delegating to the existing
  `__call__` dispatch.
- `element_from_function(f)`: Apply f to each generator, check it defines a
  morphism.
- `natural_map()`: For `Hom(ZZ^m, ZZ^n)` where m >= n, the natural map
  sends e_i to e_i for i <= n and e_i to 0 for i > n.
- `identity()`: The identity morphism (when domain == codomain).

**On morphisms (`FreeModuleMorphism` / `FGP_Morphism`):**
- `to_matrix()`: Alias for `.matrix()` (already exists on free module
  morphisms).
- `to_dict()`: Convert to `{gen_i: image_i}`.
- `is_primitive()`: `self.cokernel().is_torsionfree()`.
- `base_change(S)`: Tensor the morphism with a ring.
- Ensure `cokernel()` returns an FGP module object, and that the cokernel
  object has a `.projection()` method returning the natural surjection.
  Sage's `FGP_Morphism` may already support this -- investigate at
  implementation time.

**On endomorphism/automorphism:**
- `M.End()` = `M.Hom(M)` -- trivial alias.
- `M.Aut()` -- the group of invertible endomorphisms. For free modules,
  `Aut(ZZ^n)` = `GL(n, ZZ)`. Return a `ConditionSet` or proper group.

#### Spec assertions covered

```python
M1.<g1,g2> = ZZ^2
M2.<h1, h2> = ZZ^2
H = M1.Hom(M2)
assert H in Modules(ZZ)
f = H.from_matrix(matrix(ZZ, 2, [0,1,1,0]))
assert f in H
assert f(g1) == h2 and f(g2) == h1
assert f.to_matrix() == matrix(ZZ, 2, [0,1,1,0])
assert f.is_injective() and f.kernel() == Modules(ZZ).zero()
assert f.is_surjective() and f.cokernel() == Modules(ZZ).zero()

g = H.from_images([2*h1, 3*h2])
assert g.cokernel() == ZZ/2 + ZZ/3
pi = g.cokernel().projection()
assert pi.is_surjective()

assert M1.End() == M1.Hom(M1)
assert M1.End().identity() in M1.Aut()
assert M1.End() in Monoids
assert M1.Aut() in Groups
```


### `_install.py` -- Single entry point

Each module defines an `install()` function. `_install.py` calls all of them
in dependency order. Calling `import src.sage_patches` installs all patches.

Every `install()` call must:
- Check `ring.category()` before calling `_refine_category_` to be idempotent.
- Log which ring parents were refined (via standard logging).

Because `_refine_category_` is the mechanism for ring enrichment (not class
creation or method assignment), there is no "original method" to save for ring
parents.  The Sage category dispatch stack handles fallthrough automatically.
Module-level patches (direct attribute assignments on `FreeModule_ambient_pid`
etc.) that are still required must follow the save-original / idempotent
pattern as before.


## Explicitly Out of Scope

- **Tor/Ext functors.** The `Tor` and `Ext` assertions in `misc.sage` are
  labeled TODO and require substantial homological algebra. Defer to a later
  phase.
- **Viewing ZZ/p as multiple algebraic structures simultaneously** (cyclic
  group, abelian group, finitely presented group, FGP module). This requires
  Sage's `Facade` or category-join machinery and is not needed for Phase 1.
- **Number field extensions.** The plan mentions "hopefully extensible to
  number fields", but Phase 0 targets R = ZZ exclusively. The patches should
  not PREVENT generalization (i.e. don't hard-code ZZ where R would work),
  but active support for number fields is deferred.


## Risks

| Risk | Mitigation |
|------|-----------|
| Patching `__truediv__` on ZZ breaks other Sage code | Only intercept integer/ideal arguments; fall through to original for all else |
| Redefining `+` to mean direct sum breaks Sage module arithmetic | This codebase never uses Sage's "span" `+`. If isolation needed, use marker attribute to scope the patch |
| Category containment patches interact with Sage's caching | Patch `__contains__` which is called dynamically, not cached |
| `M/(2*M) == M.tensor(Z2)` requires canonical-isomorphism equality | Investigate Sage's FGP `__eq__` semantics first; may need custom `__eq__` |
| `QmodnZ` arithmetic may be incomplete for form evaluation | Test early; may need additional monkeypatches on `QmodnZ` element arithmetic |


## Verification Strategy

Run `tests/sage_spec/misc.sage` line by line in a Sage session with
`src.sage_patches` imported. Each assertion in that file is a required
behavior. The file is the acceptance test.

Additionally, verify Phase 1 prerequisites:
- `FormCodomain.torsion_bilinear(ZZ)` constructs `QQ/ZZ` successfully.
- `FormCodomain.torsion_quadratic(ZZ)` constructs `QQ/2ZZ` successfully.
- Form evaluation `beta(v, w) mod ZZ` lands in `QQ/ZZ` correctly.
- Cokernel of a free-module morphism produces a torsion FGP module with
  working `invariants()`, `gens()`, and `projection()`.
