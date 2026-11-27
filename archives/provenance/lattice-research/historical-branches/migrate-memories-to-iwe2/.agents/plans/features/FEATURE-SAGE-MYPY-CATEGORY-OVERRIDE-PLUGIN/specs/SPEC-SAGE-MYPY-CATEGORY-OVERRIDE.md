---
id: SPEC-SAGE-MYPY-CATEGORY-OVERRIDE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN]]'
dependsOn: []
title: Acceptance criteria for Sage mypy category override plugin
status: needs-agent-review
priority: high
complexity: 80
acceptanceCriteria:
- 1. A method in C.ParentMethods marked @override is accepted by mypy iff the corresponding
  method name exists in a Sage semantic ancestor method container derived from C.parent_class.mro().
- 2. Same holds for ElementMethods via C.element_class.mro().
- 3. Same holds for MorphismMethods via C.morphism_class.mro().
- 4. No category source file needs to add literal Python bases to ParentMethods, ElementMethods,
  or MorphismMethods.
- 5. No per-category protocol or inherited-method stub inventory is generated.
- 6. New singleton categories automatically participate if Sage's category machinery can instantiate
  them and expose the runtime method-class MRO.
- 7. Parameterized categories are either explicitly configured or explicitly left unresolved;
  no parameter guesses.
- "8. Admission is namespace-agnostic: source fullnames outside `sage.categories.*` are eligible if they resolve to Sage category method containers; the plugin MUST NOT require a `sage.categories.` prefix."
- "9. Third-party or repo-local subtree fixtures under a non-Sage namespace exhibit the same pass/fail override behavior as equivalent fixtures under `sage.categories.*`."
- 10. A debug mode can print the injected static base list for a method container.
- 11. Plugin behavior is deterministic under mypy incremental mode.
- 12. Removing or renaming an ancestor method causes @override failures in semantic descendants
  after rechecking.
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
---
# Acceptance Criteria: Sage Mypy Category Override Plugin

## Source

This spec is derived from the greenfield design document in
`~/ai/quality-control/planning/override-sage-categories.md`, the
user-provided design spec (2026-05-10 session), and the 2026-05-10 follow-up
clarification that this plugin is for any package hand-rolling a Sage category
subtree, not only code filed under upstream `sage.categories.*`.

## Requirements

### Error-Bucket Boundary

This spec covers only Sage dynamic method-container inheritance as seen by mypy:
`@override`, `@final`, `@abstractmethod`, method-container MRO projection, static
base injection, and plugin-loaded QC config behavior.

It does not cover missing annotations, `Any` leakage, untyped pytest fixtures,
Sage/pytest stub generation, `.pyi` material, `TypeAlias` surfacing, constructor
call cleanup, or downstream category-specific typing repairs. Those belong to
`PLAN-QC-MYPY-FOUNDATION-ORDER` phases outside this plugin spec.

### Core Override Semantics

A method in `C.ParentMethods` decorated with `@override` (standard
`typing.override`) must pass mypy type-checking if and only if the method
name exists in at least one ancestor method container derived from
`C.parent_class.mro()`.

The same applies to `ElementMethods` via `C.element_class.mro()` and
`MorphismMethods` via `C.morphism_class.mro()`.

This is the central invariant: mypy's static `@override` check must align with
Sage's runtime method resolution.

Focused Hom/End/Aut reproducer seeds from
`scratch/qc-reset-patches-20260515/validation/hom-end-aut-focused-mypy-after-finality-and-call-source-fixes.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/homsets/endsets.py:28` `UniversalEndObjectMethods.is_endomorphism_set` | `@override` has no visible base method | PASS because `EndCategory.ParentMethods` refines `HomCategory.ParentMethods`, where `is_endomorphism_set` is defined | FAIL if an end-object method claims to override a name absent from the Hom/End object MRO |
| `category_specs/homsets/endsets.py:45` `UniversalEndElementMethods.is_endomorphism` | `@override` has no visible base method | PASS because `EndCategory.ElementMethods` refines `HomCategory.ElementMethods`, where `is_endomorphism` is defined | FAIL if an end-element method claims to override a name absent from the Hom/End element MRO |
| `category_specs/homsets/autsets.py:64` `UniversalAutObjectMethods.domain` | `@override` has no visible base method | PASS because `AutCategory.ParentMethods` refines End/Hom object methods and may specialize the object-domain surface | FAIL if an aut-object method claims to override a name absent from the Aut/End/Hom object MRO |
| `category_specs/homsets/autsets.py:86` `UniversalAutElementMethods.is_invertible` | `@override` has no visible base method | PASS because `AutCategory.ElementMethods` refines End/Hom element methods and strengthens invertibility | FAIL if an aut-element method claims to override a name absent from the Aut/End/Hom element MRO |
| `category_specs/modules/subcategories/with_ordered_generating_set.py:32` `_WithOrderedGeneratingSet.ParentMethods.has_ordered_generating_set` | `@override` has no visible base method | PASS because `Modules(R).WithOrderedGeneratingSet().ParentMethods` refines `Modules(R).ParentMethods`, whose object surface defines `has_ordered_generating_set()` | FAIL if a refined module method claims to override a predicate absent from the resolved base module method-container MRO |
| `category_specs/modules/subcategories/with_basis.py:56` `_WithBasis.ParentMethods.has_basis` | `@override` has no visible base method | PASS because `Modules(R).WithBasis().ParentMethods` refines `Modules(R).ParentMethods`, whose object surface defines `has_basis()` | FAIL if a refined module method claims to override a predicate absent from the resolved base module method-container MRO |
| `category_specs/modules/subcategories/with_basis.py:179` `_WithOrderedBasis.ParentMethods.has_ordered_basis` | `@override` has no visible base method | PASS because `Modules(R).WithOrderedBasis().ParentMethods` refines `Modules(R).ParentMethods`, whose object surface defines `has_ordered_basis()` | FAIL if a refined module method claims to override a predicate absent from the resolved base module method-container MRO |
| `category_specs/rings/subcategories/rational_field.py:75`, `:80`, `:105`, `:148`, and `:327` representative `_QQ.ParentMethods` overrides | `@override` has no visible base method across field, number-field, and global-field methods | PASS because `_QQ.super_categories()` includes `_Fields()`, `_NumberFields()`, and `_GlobalFields()`, so the rational field object may specialize inherited field and number-field method surfaces | FAIL if `_QQ` does not refine the owner category that declares the overridden method, or if the ancestor surface lacks that method |

### No Source-Level Inheritance

No category source file must be required to add literal Python bases to
`ParentMethods`, `ElementMethods`, or `MorphismMethods`. The containment classes
remain "merely containers of operations" as documented by Sage. The plugin
injects ancestry at type-checking time without modifying source trees.

### No Generated Artifacts

No per-category protocol, inherited-method stub inventory, `.pyi`, or
intermediate representation is generated. The plugin operates during semantic
analysis of the original source, not by pre-generating type stubs.

### Singleton Category Participation

Any singleton category (parameter-free, canonical instance — `Groups()`,
`Sets()`, `Rings()`, `Fields()`, etc.) must automatically participate. If
`SageCategory.super_categories()` returns ancestors and the corresponding
`parent_class` / `element_class` / `morphism_class` can be constructed, the
plugin resolves and injects static bases without per-category configuration.

### Parameterized Category Policy

Parameterized categories (`Modules(R)`, `Algebras(R)`, `VectorSpaces(K)`) are
NOT resolved by guessing parameters.

- **Default mode**: singleton-only. Parameterized categories without
  configuration produce no injected bases. Optionally emit a plugin diagnostic.
- **Configured mode**: the plugin accepts a configuration mapping
  parameterized category classes to representative instances, e.g.:
  `Algebras: QQ`. Only bases common across all configured representatives
  (intersection mode) are injected, or a single canonical representative
   per configuration key.

### Namespace-Agnostic Admission

The source module path is NOT part of the semantic contract. A category method
container defined in `my_project.categories.*`, `category_specs.*`, or any
other importable package path must be admissible if the plugin can parse the
method-container fullname, instantiate the corresponding Sage category object,
and project its runtime method-class bases back to source containers.

Prefix checks such as `fullname.startswith("sage.categories.")` are forbidden as
the decisive admission rule. Namespace may be used only as a cheap heuristic if
there is a semantic fallback path that still admits valid third-party Sage
category subtrees.

Minimal non-Sage valid-override seed:

```python
from typing import override

from sage.categories.category import Category


class A(Category):
    def super_categories(self) -> list[Category]:
        return []

    class ParentMethods:
        def f(self) -> int:
            return 1


class B(Category):
    def super_categories(self) -> list[Category]:
        return [A()]

    class ParentMethods:
        @override
        def f(self) -> int:
            return 2
```

Current plain mypy behavior reports the `B.ParentMethods.f` override as missing
a statically visible base method when this seed is checked without the Sage
category plugin model. Expected plugin behavior is PASS, because Sage's runtime
category parent-class MRO supplies `A.ParentMethods.f`. The negative control is
the same seed with `A.ParentMethods.f` removed or renamed, which must FAIL.

### Debug Mode

A debug mode (flag or configuration key) enables printing the injected static
base list for any method container. Output format:

```
C.ParentMethods static bases (from Sage):
  A.ParentMethods
  B.ParentMethods
```

This gives independent verification that the plugin is doing what Sage says.

### Incremental Mode Determinism

Plugin behavior must be deterministic under mypy's incremental/daemon mode.
Hook results may be cached; the plugin must not hold global mutable state
across different category classes.

`report_config_data()` must return JSON-encodable data including Sage version,
plugin version, and configured parameterized-category representatives so
mypy can invalidate caches when configuration changes.

### Reactivity to Ancestor Changes

When a method is removed or renamed in an ancestor method container, mypy must
report `@override` failures in all semantic descendant method containers that
declare an override of that method, after rechecking (incremental or fresh).

This is enforced by the `get_additional_deps()` hook: if `C.ParentMethods`
semantically depends on `A.ParentMethods` and `B.ParentMethods`, changing `A`
must invalidate or recheck `C`.

### Homset Categories (Secondary)

For a homset category `C.Homsets`, the plugin must resolve
`C.Homsets().ParentMethods` against `C.Homsets().parent_class.mro()`
and `C.Homsets().ElementMethods` against `C.Homsets().element_class.mro()`.

### Method-Container Assignment Specialization

The static model must accept subtree Hom/End/Aut method-container assignments that
specialize a generic method-container slot through the category graph, without forcing
explicit Python inheritance between provider classes. Sage treats nested method
providers as flat declarations and builds the generated runtime inheritance from
`super_categories()` and construction/axiom relations; making every subtree provider
explicitly subclass the generic provider would splice the checker model into the
mathematical surface.

This is a checker-model gap when the assigned class is the declared provider for the
subtree Hom/End/Aut category and the category graph supplies the corresponding generic
Hom/End/Aut surface. It is a source defect when a subtree assigns an unrelated class,
uses the wrong slot, or claims an End/Aut provider without the required Hom/End
category ancestry.

Current reproducer seeds from
`scratch/qc-reset-patches-20260515/validation/method-container-assignment-current-filter.txt`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/sets/homsets.py:91` `ParentMethods = _SetHomCategoryObjectMethods` on `SetHomCategory(HomCategoryOf)` | incompatible assignment against generic `HomCategoryOf.ParentMethods` | PASS because `Sets().HomCategory()` specializes the generic Hom object surface through `extra_super_categories()` | FAIL if the assigned provider is not a Hom object method surface for sets |
| `category_specs/sets/homsets.py:92` `ElementMethods = _SetMorphisms` on `SetHomCategory(HomCategoryOf)` | incompatible assignment against generic `HomCategoryOf.ElementMethods` | PASS because set morphisms add set-map predicates while inheriting generic Hom element methods dynamically | FAIL if the provider omits the generic Hom ancestry and the category graph does not supply it |
| `category_specs/sets/homsets.py:110` `ElementMethods = _SetEndomorphisms` on `SetEndCategory(GenericEndCategory)` | incompatible assignment against generic End element methods | PASS because `Sets().EndCategory()` specializes endomorphisms inside the set Hom surface | FAIL if an End provider is assigned on a category that is not an End refinement |
| `category_specs/rings/homsets.py:62` / `:63` `RingHomCategory` provider assignments | incompatible assignment against generic Hom provider slots | PASS because ring hom categories specialize Hom providers through the ring Hom category graph | FAIL for a provider from an unrelated subtree |
| `category_specs/modules/homsets.py:390` `ElementMethods = _RModEndomorphisms` on the module End category | incompatible assignment against generic End element methods | PASS because module endomorphisms refine generic endomorphisms and add module-linear structure through the module Hom graph | FAIL if the category does not refine the corresponding module Hom category |
| `category_specs/cat/homsets.py:124` / `:125` `CatHomCategory` provider assignments | incompatible assignment against generic Hom provider slots | PASS because functors are Cat morphisms and `Cat().HomCategory()` specializes the generic Hom category through the Cat category graph | FAIL if the provider does not model functor object/element methods |
| `category_specs/cat/endsets.py:26` / `:33` and `category_specs/cat/autsets.py:31` Cat End/Aut provider assignments | incompatible assignment against generic End/Aut provider slots | PASS because endofunctors and autofunctors refine Cat hom functors through End/Aut category structure | FAIL if the End/Aut category is not tied to the corresponding Cat Hom category |
| `category_specs/posets/homsets.py:56` / `:57`, `:77`, and `:88` Poset Hom/End/Aut provider assignments | incompatible assignment against generic Hom/End/Aut provider slots | PASS because order-preserving maps, endomorphisms, and automorphisms specialize generic Hom/End/Aut providers through the poset category graph | FAIL if an order-map provider is assigned outside a poset Hom/End/Aut refinement |
| `category_specs/topological_spaces/homsets.py:57` / `:58`, `:85`, and `:127` TopologicalSpace Hom/Aut provider assignments | incompatible assignment against generic Hom/Aut provider slots | PASS because continuous maps, homeomorphisms, and isometries specialize generic Hom/Aut providers through topological and metric category refinements | FAIL if an isometry provider is accepted without the metric/aut category ancestry |
| `category_specs/algebras/homsets.py:40` / `:41` Algebra Hom provider assignments | incompatible assignment against generic Hom provider slots | PASS because algebra homomorphisms specialize generic Hom providers through the algebra category graph | FAIL if an algebra-hom provider is assigned to a non-algebra Hom category |
| `category_specs/lattices/homsets.py:54` / `:55`, `:74`, and `:129` Lattice Hom/End/Aut provider assignments | incompatible assignment against generic Hom/End/Aut provider slots | PASS because lattice morphisms, endomorphisms, and automorphisms specialize generic Hom/End/Aut providers through the lattice category graph | FAIL if the provider is accepted without the lattice Hom/End/Aut ancestry |

### Method-Container Self Surfaces

The static model must type `self` inside `ParentMethods`, `ElementMethods`,
`SubcategoryMethods`, and Hom/End/Aut method containers as the runtime object
that receives the method, not merely as the nested method-container class. This
is the same Sage mechanism that makes a method defined in `ParentMethods`
available on a concrete parent object after category refinement.

This is a checker-model gap when the accessed method or attribute is supplied by
the runtime parent, element, category, or inherited method-container surface that
Sage can resolve. It is a source defect when the accessed surface is not present
on the resolved runtime receiver or belongs to an unrelated owner.

Current reproducer seeds from
`scratch/qc-reset-patches-20260515/validation/matrix-algebra-object-focused-mypy-after-typed-factory.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/rings/matrix_algebras.py:79` `self.base_ring()` inside `_MatrixAlgebras.ParentMethods.is_commutative_ring` | `ParentMethods` has no attribute `base_ring` | PASS because the method runs on the square `MatrixSpace(R, n, n)` parent, whose ring/matrix parent surface includes `base_ring()` | FAIL if a method-container references a parent method absent from the resolved receiver |
| `category_specs/rings/matrix_algebras.py:87` `self.nrows()` inside `_MatrixAlgebras.ParentMethods.is_integral_domain` | checker sees only the nested method-container class | PASS because `nrows()` is a same-container parent method on the refined matrix parent | FAIL if the same-container method has an incompatible signature or wrong return surface |
| `category_specs/rings/matrix_algebras.py:186` `self.base_ring().one()` inside `identity_matrix` | `ParentMethods` has no attribute `base_ring` | PASS when the receiver is the grounded square matrix parent over a ring | FAIL if the receiver is a non-ring parent with no base ring |
| `category_specs/rings/subcategories/constructions/rings_under.py:43` `self.base_ring()` inside `structure_ring()` | checker sees only `_RingsUnder.ParentMethods` and reports missing `base_ring` / `Any` return | PASS because methods in `Rings().RingsUnder(R).ParentMethods` run on ring parents under `R`, whose construction category receiver supplies `base_ring()` | FAIL if the receiver is not a ring-under construction object with a base ring |
| `category_specs/rings/subcategories/constructions/rings_under.py:47` `self.coerce_map_from(self.structure_ring())` inside `structure_map()` | checker sees only `_RingsUnder.ParentMethods` and reports missing `coerce_map_from` / `Any` return | PASS because the runtime receiver is a ring parent and the structure map from the fixed source ring is a ring coercion map | FAIL if the receiver is a category object or non-ring parent without a coercion surface |
| `category_specs/rings/subcategories/constructions/rings_over.py:48` `self.base_ring()` inside `structure_ring()` | checker sees only `_RingsOver.ParentMethods` and reports missing `base_ring` / `Any` return | PASS because methods in `Rings().RingsOver(R).ParentMethods` run on ring parents over the ambient ring `R`, whose construction category receiver supplies `base_ring()` | FAIL if the receiver is not a ring-over construction object with a base ring |
| `category_specs/rings/subcategories/constructions/rings_over.py:59` `self.structure_ring().coerce_map_from(self)` inside `structure_map()` | checker sees `self` only as `_RingsOver.ParentMethods` and rejects it as the `coerce_map_from(...)` ring argument | PASS because the over-object receiver is itself a ring parent over the ambient structure ring, so the structure map is the coercion from that ring parent to the ambient ring | FAIL if the over-object receiver is not a ring parent or the resolved structure ring lacks `coerce_map_from()` |
| `category_specs/lattices/__init__.py:150`, `:157`, `:166`, and `:175`, filtered in `validation/lattice-subcategory-receiver-plugin-seed-filter.txt` | checker sees `Lattices.SubcategoryMethods` without the parameterized lattice-category receiver and reports missing `base_ring()` | PASS because `Lattices(R).SubcategoryMethods` runs on the parameterized lattice category over `R`, whose category-module surface exposes `base_ring()` for construction selectors such as dual lattices, overlattices, orthogonal direct sums, and discriminant groups | FAIL if the receiver is not a parameterized lattice category or lacks a base-ring surface |
| `category_specs/rings/subcategories/field.py:137` `self.zero()` and `:140` `self.one()` inside `_Fields.ParentMethods.gcd` | checker sees only `_Fields.ParentMethods` and reports missing `zero` / `one` plus `no-any-return` | PASS because field parent methods run on field parent objects, and the inherited ring parent surface supplies canonical zero and one elements | FAIL if the receiver is not a ring parent with zero/one element constructors |
| `category_specs/rings/subcategories/principal_ideal_domain.py:60` `self.ideal([r, s])` inside `_PrincipalIdealDomains.ParentMethods.gcd` | checker sees only `_PrincipalIdealDomains.ParentMethods` and reports missing `ideal` | PASS because PID parent methods run on ring parents, and the root ring parent surface declares `ideal(generators)` | FAIL if the receiver is not a ring parent or if the resolved ring parent surface lacks `ideal(...)` |
| Ring subcategory inheritance rows filtered in `validation/ring-subcategory-inheritance-plugin-seed-filter.txt` | checker sees each ring subcategory provider in isolation and reports no visible override base or inherited parent surface for predicates, completions, precision changes, extension/base-ring methods, and idempotent self-returns | PASS because these subcategories refine root ring, field, number-field, valuation, series, finite, local, topological, and precision-bearing ring parent surfaces through Sage/project category ancestry | FAIL if the receiver is not a ring parent in the claimed refinement chain, or if the claimed method is absent from the resolved ring method-container graph |
| `category_specs/modules/homsets.py:88` `self.codomain().zero()` inside `_RModHomCategoryObjectMethods.zero` | checker sees `codomain()` as `Modules.ParentMethods?` and reports missing `zero` | PASS because module Hom objects have module codomains, and `zero()` is an admitted `Modules(R)` parent surface returning a module element | FAIL if the codomain receiver is not a module parent or if the module parent surface lacks `zero()` |
| `category_specs/modules/homsets.py:331` `v.tensor(w)` for `v: RModuleElement` inside `_Bilinear.ElementMethods.b` | checker sees `v` as `Modules.ElementMethods?` but does not expose the declared module-element `tensor(...)` surface | PASS because `RModuleElement` resolves to `Modules.ElementMethods`, whose source surface declares tensoring module elements to build the tensor input for a bilinear form | FAIL if the element alias does not resolve to the module-element method container or if that container lacks `tensor(...)` |
| `category_specs/modules/__init__.py:1520` `torsion_summands[0].direct_sum(torsion_summands[1:])` inside `from_ring_elements` | checker sees `torsion_summands[0]` as `Modules.ParentMethods?` and reports missing `direct_sum` | PASS because each torsion summand is an `RModule`, and the root module parent surface declares `direct_sum(...)` for finite module sums | FAIL if a summand is not an `RModule` or the root module parent surface lacks `direct_sum(...)` |
| `category_specs/modules/__init__.py:969` / `:978` `V.quotient_module(W)` and `module.quotient_module(submodule, check=check)` in module constructors | checker sees `FreeModule` / `RModule` receivers as method containers without visible `quotient_module` | PASS because free modules and root modules expose the declared quotient-module constructor surface, and these constructors refine the resulting quotient module into the project category graph | FAIL if the receiver is not a module parent or if the quotient constructor is absent from the resolved module surface |
| `category_specs/modules/subcategories/torsionfree.py:34` `self.base_ring()` inside `_Torsionfree.ParentMethods.annihilator` | checker sees only `_Torsionfree.ParentMethods` and reports missing `base_ring` | PASS because `Modules(R).Torsionfree().ParentMethods` refines `Modules(R).ParentMethods`, whose root module parent surface declares `base_ring()` | FAIL if the receiver is not a module parent over a base ring or the resolved root module surface lacks `base_ring()` |
| `category_specs/modules/subcategories/free.py:99`, `:107`, `:115`, `:128`, `:137`, `:150`, `:160`, `:165`, `:174`, `:184`, `:196`, `:210`, and `:225` in `_FreeFiniteRank.ParentMethods` | checker sees only the local finite-rank free-module provider and reports missing override bases or inherited receiver methods such as `rank`, `base_ring`, and `change_ring` | PASS because `Modules(R).Free().FiniteRank().ParentMethods` refines both `_Free.ParentMethods` and `Modules(R).ParentMethods`: finite-rank free modules inherit the free-module `rank`/basis surface and the root module `base_ring`, dual, tensor, and base-change surfaces | FAIL if the finite-rank free category does not refine the free-module/root-module parent method graph, or if a claimed override name is absent from that graph |
| Module predicate override rows filtered in `validation/module-predicate-inheritance-plugin-seed-filter.txt` | checker sees each module subcategory provider in isolation and reports no visible override base for predicates such as `is_projective`, `is_over_pid`, `is_finitely_generated`, `is_graded`, and `is_ideal` | PASS because these module subcategories refine `Modules(R).ParentMethods` or an earlier module axiom surface where the predicate is declared as module structure | FAIL if the receiver is not a module parent in the claimed refinement chain, or if the predicate is absent from the resolved module method-container graph |
| `category_specs/modules/subcategories/integer_lattices.py:42` `is_lattice()`, filtered in `validation/module-integer-lattice-predicate-plugin-seed-filter.txt` | checker sees only the integer-lattice provider and reports no visible override base for the lattice predicate | PASS because integer lattices refine the module/lattice category surface whose parent method graph declares lattice membership as semantic structure | FAIL if the receiver is not an integer-lattice module parent or the lattice predicate is absent from the resolved method graph |
| `category_specs/algebras/__init__.py:279` `self.category().Ideals(self)` inside `_AlgebraParentMethods.ideals` | checker sees only `_AlgebraParentMethods` and reports missing `category` | PASS because algebra parent methods run on algebra parent objects, whose Sage parent surface exposes `category()`, and the resolved algebra category owns the `Ideals(self)` construction selector | FAIL if the receiver is not an algebra parent object or the resolved category has no algebra-ideal construction |
| `category_specs/algebras/__init__.py:385` `algebra in self` inside `Algebras(R).SubcategoryMethods.Ideals` | checker sees only `SubcategoryMethods` and rejects it as the right operand of `in` | PASS because subcategory-method receivers are category objects, and membership testing against the current algebra category is the guard that the ideal construction is over an algebra in that category | FAIL if the receiver is not a category object or does not define category membership |
| `category_specs/algebras/subcategories/finite_dimensional.py:45`, `:51`, and `:57` finite-dimensional algebra parent methods | checker sees only `_FiniteDimensionalAlgebras.ParentMethods` and reports no visible override base for `radical`, `semisimple_quotient`, or `idempotent_lift` | PASS because finite-dimensional algebras refine `Algebras(R).ParentMethods`, whose root algebra surface declares those algebra-structure methods | FAIL if the receiver is not an algebra parent or the root algebra method surface lacks the claimed method |
| Algebra method-container inheritance rows filtered in `validation/algebra-method-container-inheritance-plugin-seed-filter.txt` | checker sees algebra construction or with-basis providers in isolation and reports missing inherited receiver methods or override bases for `base_ring`, `algebra_generators`, and `hochschild_complex` | PASS because algebra ideals and algebras-with-basis refine algebra/module parent surfaces whose method-container graph supplies the base ring and algebra-structure methods | FAIL if the receiver is not an algebra parent in the claimed refinement chain or the claimed method is absent from the resolved algebra method graph |
| `category_specs/topological_spaces/subcategories/metric.py:32` `is_metric()` on metric-space parent methods, filtered in `validation/topological-metric-predicate-plugin-seed-filter.txt` | checker sees only `_MetricSpaceObjectMethods` and reports no visible override base for the metric predicate | PASS because `TopologicalSpaces().Metric().ParentMethods` refines the topological-space parent surface that declares metric-space membership as an axiom predicate | FAIL if the receiver is not a metric topological-space parent or the topological-space method graph lacks the metric predicate surface |
| `category_specs/sets/homsets.py:99` / `:100`, `posets/homsets.py:64` / `:65`, and analogous specialized `HomCategoryOf` assignments | checker treats assigning a specialized `ParentMethods` / `ElementMethods` method-container class as an incompatible class-variable override | PASS when the assigned method-container is a subclass of the corresponding universal Hom method surface and the category refines `HomCategoryOf(self.base_category())` | FAIL if the assigned container is not a method-container class, is not a universal Hom parent/element surface, or belongs to an unrelated category construction |
| `category_specs/modules/subcategories/constructions/quotients.py:80` `@override quotient_module(...)` inside quotient module parents | checker sees no visible base method for the override | PASS because quotient module parents refine `Modules(R).ParentMethods`, whose root module parent surface declares `quotient_module(submodule, check=True)` | FAIL if the quotient construction receiver does not resolve to a module parent surface with `quotient_module(...)` |
| `category_specs/modules/subcategories/constructions/quotients.py:100` `self.submodule(...)` inside `quotient_by_generators` | checker sees only the quotient construction method container and reports missing `submodule` | PASS because quotient construction parent methods run on module parents, and the inherited root module parent surface supplies final `submodule(...)` as a wrapper over `span(...)` | FAIL if the receiver is not a module parent or the module parent surface lacks `submodule(...)` |
| `category_specs/modules/subcategories/constructions/quotients.py:115` / `:132` `self.submodule(...)` inside relation-matrix and relation-row quotient helpers | same hidden inherited module-parent surface failure | PASS for the same inherited root module parent `submodule(...)` surface, with relation data accepted by the underlying `span(...)`/Sage module implementation | FAIL if the receiver is not a module parent or relation input is routed to a non-module surface |
| `category_specs/sets/subcategories/enumerated_from_iterator.py:45`, `:69`, and `:81`; `category_specs/sets/subcategories/recursively_enumerated.py:68` and `:86`; `category_specs/sets/subcategories/countable.py:76` and `:94` | checker sees only each nested `ParentMethods` provider and reports missing `category`, `_an_element_`, or inherited `is_finite` | PASS because these providers run on concrete Sage/set parents refined through `Sets().Countable()`, so the runtime receiver has the Sage parent `category()` / `_an_element_()` compatibility surface plus the inherited root/countable set predicates | FAIL if the receiver is not a set parent, is not in the countable/enumerated category chain, or the accessed compatibility method is absent from the resolved concrete parent |
| `category_specs/sets/subcategories/finite_set_maps.py:43`, `:47`, `:51`, `:55`, and `:60` finite map-set parent methods | checker sees only `_FiniteSetMapsSets.ParentMethods` and reports no visible override base for finite/countable set methods | PASS because finite map-set parents refine `Sets().Countable().Finite()`, whose parent surface supplies cardinality, membership, sample element, iteration, and element-constructor methods | FAIL if the receiver is not a finite/countable set parent or if the declared method is absent from the resolved set parent graph |
| `category_specs/sets/subcategories/{disjoint_union,non_negative_integers,finite_enumerated_set,image,family,integer_range,primes,totally_ordered_finite,real_set,cartesian_product,positive_integers}.py`, filtered in `validation/concrete-set-parent-surface-plugin-seed-filter.txt` | checker sees each concrete set provider in isolation and reports missing override bases or inherited receiver methods such as `is_finite`, `_an_element_`, and concrete set operations | PASS because these providers run on Sage set parents refined through root, countable, finite, totally ordered, image, cartesian-product, or topological set categories, so the runtime receiver inherits the corresponding set parent compatibility surface | FAIL if the receiver is not a set parent in the claimed refinement chain, or if a method is not present on the resolved concrete parent surface |
| Set axiom/facade inheritance rows filtered in `validation/set-axiom-facade-inheritance-plugin-seed-filter.txt` | checker sees countable, finite, infinite, uncountable, and facade providers in isolation and reports no visible override base or inherited predicate/receiver methods | PASS because these providers refine the root set parent surface and the relevant set axiom graph, including countability, finiteness, facade parentage, sampling, iteration, rank, and membership operations | FAIL if the receiver is not a set parent in the claimed refinement chain or the method is absent from the resolved set method graph |
| `category_specs/posets/__init__.py:82` through `:208`, filtered in `validation/root-poset-parent-surface-plugin-seed-filter.txt` | checker sees `_PosetParentMethods` without Sage/category supercategory ancestry and reports no visible override base for order and order-ideal methods | PASS because `Posets.super_categories()` includes Sage `Posets()`, and project root poset parents expose the Sage/order-theoretic parent surface for comparison, cover, order-ideal, order-filter, chain, and antichain operations | FAIL if the receiver is not a poset parent or the claimed method is absent from the Sage/project root poset surface |
| `category_specs/modules/subcategories/constructions/cartesian_products.py:37` `@override __init_extra__` inside cartesian-product module parents | checker sees no visible base hook for the override | PASS because cartesian-product parents are Sage parent objects and `__init_extra__` is Sage's post-initialization hook used by category parent method containers | FAIL if the hook appears on a non-parent method container or has an incompatible no-argument signature |
| `category_specs/modules/subcategories/constructions/cartesian_products.py:53` `@override _lmul_` inside cartesian-product module elements | checker sees only the cartesian-product element container and reports no visible base method | PASS because cartesian products of `Modules(R)` are again `Modules(R)`, and module elements inherit the root `_lmul_(r)` scalar-action surface | FAIL if the cartesian product is not known to refine a module category or the inherited element surface lacks `_lmul_` |
| `category_specs/sets/subcategories/partitioned.py:61` `self.an_element()` inside `PartitionedSetsCategory.ParentMethods.partition` | checker sees only `PartitionedSetsCategory.ParentMethods` and reports missing `an_element` | PASS because partitioned-set parents inherit the root `Sets().ParentMethods` surface, whose `an_element()` returns a set element used here as the partition witness | FAIL if the receiver is not a set parent or the inherited set parent surface lacks `an_element()` |
| `category_specs/sets/subcategories/partitioned.py:118` `self.base_set().subsets().subsets()` inside `PartitionsCategory.ParentMethods.ambient` | checker sees `base_set()` as `Sets.ParentMethods?` and reports missing `subsets` | PASS because the fixed-base partition parent returns a set object, and the root set parent surface defines `subsets()` as the powerset constructor used to build the powerset-of-powerset ambient | FAIL if `base_set()` does not resolve to a set parent or if the set surface lacks `subsets()` |
| `category_specs/posets/subcategories/finite_join_semilattice.py:62` `self.join(element, generator)` inside `subjoinsemilattice` | checker sees only `_FiniteJoinSemilatticePosets.ParentMethods` and reports missing `join` | PASS because finite join-semilattice parents inherit the join-semilattice parent surface, whose primitive binary operation is `join(x, y)` | FAIL if the receiver is not a join-semilattice parent or the ancestor surface lacks binary `join` |
| `category_specs/posets/subcategories/finite_join_semilattice.py:65` `self.subposet(closure)` inside `subjoinsemilattice` | checker sees only `_FiniteJoinSemilatticePosets.ParentMethods` and reports missing `subposet` | PASS because finite join-semilattice parents also inherit finite-poset parent methods, including induced `subposet(...)` | FAIL if the receiver is not a finite-poset parent or `subposet` is absent from the finite-poset surface |
| `category_specs/posets/subcategories/finite_meet_semilattice.py:67` `self.meet(element, generator)` inside `submeetsemilattice` | checker sees only `_FiniteMeetSemilatticePosets.ParentMethods` and reports missing `meet` | PASS because finite meet-semilattice parents inherit the meet-semilattice parent surface, whose primitive binary operation is `meet(x, y)` | FAIL if the receiver is not a meet-semilattice parent or the ancestor surface lacks binary `meet` |
| `category_specs/posets/subcategories/finite_meet_semilattice.py:70` `self.subposet(closure)` inside `submeetsemilattice` | checker sees only `_FiniteMeetSemilatticePosets.ParentMethods` and reports missing `subposet` | PASS because finite meet-semilattice parents also inherit finite-poset parent methods, including induced `subposet(...)` | FAIL if the receiver is not a finite-poset parent or `subposet` is absent from the finite-poset surface |
| `category_specs/posets/subcategories/join_semilattice.py:61` and `meet_semilattice.py:61` `@foldable_operation` binary implementation under binary-plus-sequence overloads | overloaded implementation does not accept the sequence overload | PASS because `@foldable_operation` supplies the sequence fold over the primitive binary operation without widening the mathematical implementation signature | FAIL if the decorated method is not binary, lacks the matching sequence overload, or the fold result has a different codomain |

Additional ring-element seed from
`scratch/qc-reset-patches-20260515/validation/finitely-presented-pid-free-rank-focused-mypy-after-bool-sum.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/modules/subcategories/finitely_presented_over_pid.py:117` `r.is_zero()` for `r: RingElement` inside `free_rank` | `Rings.ElementMethods? has no attribute "is_zero"` | PASS because `RingElement` is the canonical type alias for `Rings.ElementMethods`, whose source method surface defines `is_zero() -> bool` | FAIL if an element alias targets a method container that does not define or inherit the accessed method |
| `category_specs/algebras/__init__.py:616`, `:620`, and `:625` `multiplication.tensor_type()`, `multiplication.base_module()`, and `multiplication.structure_constants()` for `multiplication: Tensor` | checker sees `TensorAlgebraComponents.ElementMethods?` and reports missing tensor element methods | PASS because `Tensor` resolves to the public `TensorAlgebraComponents.ElementMethods` surface, whose concrete provider declares `tensor_type()`, `base_module()`, and `structure_constants()` for tensor elements | FAIL if the alias does not resolve to the tensor element method-container surface or if that surface lacks the accessed tensor methods |

Additional ring-ideal receiver seeds from
`scratch/qc-reset-patches-20260515/validation/real-precision-field-change-precision-source-fix-just-test.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/rings/subcategories/principal_ideal_domain.py:55` `ideal.is_principal()` and `:56` `ideal.gen()` for `ideal: Ideal` inside `ideal_generator` | `_RingIdeals.ParentMethods?` has no attribute `is_principal` / `gen`, plus `no-any-return` from `gen()` | PASS because `Ideal` is the canonical alias for `_RingIdeals.ParentMethods`, whose source method surface defines both `is_principal() -> bool` and `gen(...) -> RingElement` | FAIL if the alias does not resolve to a ring-ideal parent method container or if the method is absent from that container |
| `category_specs/rings/subcategories/polynomial_ring.py:84` / `:87` `ideal.is_principal()` and `ideal.gen()` inside polynomial-ring completion | same `_RingIdeals.ParentMethods?` receiver-surface failure | PASS for the same canonical ring-ideal parent receiver; polynomial completion is using ideal methods, not declaring a new ideal surface | FAIL if a non-ideal object is accepted as having ring-ideal methods |
| `category_specs/rings/subcategories/polynomial_ring.py:92` `super().completion(p, prec=oo)` after `p: Polynomial = ideal.gen()` | `completion` undefined in superclass | PASS because polynomial-ring parent methods refine the upstream ring completion method surface, and the method-container `super()` call must resolve against the dynamic Sage/category provider chain | FAIL if the active receiver is not a polynomial-ring parent or the upstream completion surface is absent |
| `category_specs/rings/subcategories/field.py:149` / `:151` and `p_adic_integer_ring.py:51`, `:53`, `:55` `ideal.is_zero()` / `ideal.is_one()` inside completion methods | `_RingIdeals.ParentMethods?` has no attribute `is_zero` / `is_one` | PASS because `Ideal` resolves to `_RingIdeals.ParentMethods`, whose source method surface declares `is_zero() -> bool` and `is_one() -> bool` | FAIL if the alias does not resolve to a ring-ideal parent method container or if the method is absent from that container |

Additional algebraic-number receiver seeds from
`scratch/qc-reset-patches-20260515/validation/aa-object-source-fix-just-test.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/rings/subcategories/algebraic_closure_of_rational_field.py:53` and `real_algebraic_field.py:52` `polynomial_root(...)` overrides | `@override` has no visible base method | PASS because `QQbar` and `AA` refine `_AlgebraicFields`, whose parent method surface declares `polynomial_root(...)` with the corresponding interval inputs | FAIL if a field does not refine `_AlgebraicFields` or the ancestor surface lacks `polynomial_root` |
| `category_specs/rings/subcategories/algebraic_closure_of_rational_field.py:61` and `real_algebraic_field.py:57` element `nth_root(...)` overrides | `@override` has no visible base method | PASS because these element methods are Sage-backed algebraic-number surfaces verified in `SPEC-MAPPING-RINGS`; the receiver is a QQbar/AA element, not a generic ring element | FAIL if the element receiver is not one of the admitted algebraic-number parents or Sage does not expose the compatibility method |

Additional finite-ambient subobject seed from
`scratch/qc-reset-patches-20260515/validation/set-subobject-cardinality-just-test-after-bool-sum.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/sets/subcategories/constructions/subobjects.py:112` `for x in self.ambient()` inside `cardinality`, after the branch `if self.ambient().is_finite()` | `Sets.ParentMethods? has no attribute "__iter__" (not iterable)` | PASS because project `Sets().Finite()` has `Sets().Countable()` as a supercategory, matching Sage `FiniteEnumeratedSets`; inside the finite-ambient branch, the ambient set has the countable/finite enumeration surface needed to count subset elements | FAIL if the ambient is only a root `Set` with no finite/countable evidence, or if the method attempts to iterate outside a proven finite/countable branch |
| Formed-module method-container inheritance rows filtered in `validation/forms-method-container-inheritance-plugin-seed-filter.txt` | checker sees only the local formed-module provider and reports no visible base method for predicates such as `is_bilinear`, `is_integral`, `is_indefinite`, or inherited element methods such as `is_zero` | PASS because each formed-module axiom refines `Modules(R).ParentMethods`, `Modules(R).ElementMethods`, or an earlier formed-module surface that declares the predicate/element method as semantic structure | FAIL if the formed-module category does not refine the owner that declares the method or if the method is absent from the ancestor method-container graph |
| `category_specs/forms/subcategories/with_forms.py:55` `self.category().AutCategory().Of(self)` inside `orthogonal_group` | checker sees only `FormedModulesCategory.ParentMethods` and reports missing `category` | PASS because method-container methods run on Sage parent objects, whose runtime parent surface includes `category()`, and the category is the formed-module category whose `AutCategory().Of(self)` owns the orthogonal group | FAIL if the receiver is not a Sage parent object or the category lacks an Aut construction |
| `category_specs/forms/subcategories/free_bilinear.py:77`, `:82`, and `:98` free bilinear formed-module methods | checker sees only the local free-bilinear provider and reports no visible override base for `is_free`, `gram_matrix`, or `inner_product_matrix` | PASS because free bilinear formed modules refine the formed-module/free-module surface whose parent graph supplies the free predicate and bilinear Gram/inner-product method surfaces | FAIL if the receiver is not a free bilinear formed-module parent or if the resolved ancestor graph lacks the claimed method surface |

Additional set-partition compatibility seed from
`scratch/qc-reset-patches-20260515/validation/partitioned-refinement-set-plugin-seed-filter.txt`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/sets/subcategories/partitioned.py:218` `self.refinements()` inside `refinement_set()` | `ElementMethods` had no attribute `refinements` before the source surface was declared | PASS because the receiver is a Sage `SetPartition` element refined into `Sets().Partitioned()`, and the decided source contract keeps Sage's concrete list-returning `refinements()` method as compatibility behavior while exposing project `refinement_set()` as the finite-set surface | FAIL if a project method calls a Sage compatibility method not present on the resolved element class, or if the compatibility method is used as the public project finite-set name |

This case is not a request to add abstract `refinements()` / `coarsenings()` methods
back to the project element surface. The source-grounded decision in
`DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING` deliberately separates Sage's
list-returning compatibility names from project finite-set method names. The checker
model must therefore see raw Sage element-class methods when they are used as
implementation witnesses inside a refined method container, while still rejecting
attempts to make those Sage names the project finite-set surface.

Additional focused Hom/End/Aut seeds from
`scratch/qc-reset-patches-20260515/validation/hom-end-aut-focused-mypy-after-finality-and-call-source-fixes.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/homsets/homsets.py:51` `self.parent().domain()` inside `UniversalHomElementMethods.domain` | `UniversalHomElementMethods` has no attribute `parent` | PASS because the element method runs on a morphism element whose parent is `Hom_C(A, B)` | FAIL if the resolved element receiver has no parent surface or the parent lacks `domain()` |
| `category_specs/homsets/autsets.py:60` `self.ambient()` inside `UniversalAutObjectMethods.end_category` | `UniversalAutObjectMethods` has no attribute `ambient` | PASS because the aut object is backed by a Sage condition subset whose runtime parent surface includes `ambient()` | FAIL if a non-condition-set receiver lacks an ambient end object |
| `category_specs/homsets/autsets.py:66` `self.end_category().domain()` inside `UniversalAutObjectMethods.domain` | `EndCategory.ParentMethods?` has no attribute `domain` | PASS because `End_C(A)` is a hom object and inherits `domain()` from the Hom object surface | FAIL if the resolved end object does not inherit the Hom object domain/codomain surface |

Additional module-basis seeds from
`scratch/qc-reset-patches-20260515/validation/with-basis-index-set-source-fix-just-test.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/modules/subcategories/with_basis.py:51` `self.base_category().WithOrderedBasis()` inside `_WithBasis.SubcategoryMethods.WithOrderedBasis` | `_WithBasis.SubcategoryMethods` has no attribute `base_category` | PASS because `SubcategoryMethods` runs on the category object, and `_WithBasis` is a category-over-base-ring object with `base_category()` and a base module category exposing `WithOrderedBasis()` | FAIL if the resolved category receiver has no base category or the base category lacks the requested axiom selector |
| `category_specs/modules/subcategories/with_basis.py:184` `self.basis().keys()` inside `_WithOrderedBasis.ParentMethods.basis_order` | `_WithOrderedBasis.ParentMethods` has no attribute `basis` | PASS because `Modules(R).WithOrderedBasis()` includes `Modules(R).WithBasis()` in `extra_super_categories()`, and the inherited parent method surface defines `basis()` | FAIL if the ordered-basis category does not refine `WithBasis()` or the inherited basis surface is absent |
| `category_specs/modules/subcategories/with_basis.py:188` `self.basis()` inside `_WithOrderedBasis.ParentMethods.user_basis` | `_WithOrderedBasis.ParentMethods` has no attribute `basis` | PASS for the same inherited `WithBasis.ParentMethods.basis()` surface | FAIL if the inherited basis surface resolves to an unrelated owner or incompatible return type |

Additional idempotent ring self-return seeds from
`scratch/qc-reset-patches-20260515/validation/zero-ring-completion-source-fix-just-test.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/rings/subcategories/field.py:150` `return self` inside the zero-ideal branch of `_Fields.ParentMethods.completion` | `_Fields.ParentMethods` is not accepted as `_CompleteRings.ParentMethods` | PASS because `self` is the runtime field parent and the zero-ideal completion of a field is the field itself | FAIL if the branch is the unit ideal, whose completion must route to `Rings().Constructors().ZeroRing()` |
| `category_specs/rings/subcategories/algebraically_closed_field.py:44` `return self` inside `_AlgebraicallyClosedFields.ParentMethods.algebraic_closure` | `_AlgebraicallyClosedFields.ParentMethods` is not accepted as `_Fields.ParentMethods` | PASS because an algebraically closed field is already a field and is its own algebraic closure | FAIL if the receiver is not a field or is not algebraically closed |
| `category_specs/rings/subcategories/p_adic_integer_ring.py:54` and `:56` `return self` inside `_Zp.ParentMethods.completion` | `_Zp.ParentMethods` is not accepted as `_CompleteRings.ParentMethods` | PASS because `self` is the runtime p-adic integer-ring parent; the zero ideal and nonzero proper ideals preserve the complete p-adic topology | FAIL if the branch is the unit ideal, whose completion must route to `Rings().Constructors().ZeroRing()` |

### Category Promotion And Selector Returns

The static model must also cover the category-promotion surfaces that ordinary
mypy currently reports as `no-any-return`, `attr-defined`, `arg-type`, or
callability errors even when the source is the direct Sage/category expression.
This includes:

- `_with_axiom(...)` selectors on `SubcategoryMethods`;
- `SomeConstruction.category_of(category, ...)` selectors;
- `refine_category(object, categories, ...)` constructor/refinement returns;
- construction collectors such as `Constructors()`;
- Hom/End/Aut category selectors;
- inherited parent/element method-container projections, including callable
  parent construction such as `Set.__call__(x)`.

The acceptance condition is not merely that mypy becomes quiet. For each pattern,
the plugin or companion static model must distinguish a real source defect from
a checker-model gap. Correct direct category expressions must not require local
`cast(...)`, trivial wrapper methods, explicit provider subclassing, or source
surface weakening. A focused reproducer must fail before the model change and pass
after it, while an intentionally wrong owner/codomain/call surface must still fail.

Current reproducer seeds from
`scratch/qc-reset-patches-20260515/validation/research-current-mypy-live.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/algebras/__init__.py:350` `_with_axiom("Commutative")` | `no-any-return` plus missing `_with_axiom` on `SubcategoryMethods` | PASS as the declared category selector without a local cast | FAIL if the method returns an unrelated category owner |
| `category_specs/rings/__init__.py:1819` `_with_axiom(...)` family | missing `_with_axiom` on `SubcategoryMethods` | PASS for admitted ring axiom selectors without provider subclassing | FAIL when the requested axiom is not admitted by the category |
| `category_specs/cat/universal_subcategory_methods.py:57` `category_of(...)` construction selector | `no-any-return` on direct construction-category expression | PASS as the construction category returned by Sage's category graph | FAIL when the construction receives an incompatible base category |
| `category_specs/homsets/endsets.py:19` `category.EndCategory()` in `_end_categories_of` | `no-any-return` on direct Hom/End selector expression | PASS as the end-category selector returned by the category graph | FAIL when the receiver is not a category exposing an EndCategory selector |
| `category_specs/homsets/homsets.py:161` `Category.join(hom_supercategories)` | `no-any-return` on Sage category join | PASS as the joined Hom-category supercategory returned by Sage's category lattice | FAIL if the joined expression contains non-category inputs |
| `category_specs/homsets/autsets.py:159` `Category.join([..._aut_categories_of(...)])` | `no-any-return` on Sage category join | PASS as the joined Aut-category supercategory returned by Sage's category lattice | FAIL if an aut-category selector is unavailable on the resolved receiver |
| `category_specs/rings/__init__.py:452` principal-ideal parent projection | `no-any-return` plus missing parent method projection | PASS only when the source owner/codomain matches the ring ideal surface | FAIL for a projected method missing from the semantic owner |
| `category_specs/rings/__init__.py:610` `refine_category(Integers(1), [Rings(), _IntegerModRings(), _CompleteRings()])` inside `ZeroRing()` | `no-any-return` on direct category refinement expression | PASS as the zero-ring constructor refined into the complete ring surface | FAIL if the constructor omits the complete-ring refinement or returns an unrelated object |
| `category_specs/sets/subcategories/constructions/subobjects.py:76` subset parent call | `Sets.ParentMethods? not callable` | PASS when a grounded `__call__(x)` parent surface exists | FAIL when the source lacks the callable surface |
| `category_specs/sets/subcategories/partitioned.py:218`, `:223`, and `:293` `Sets().Constructors().from_iterable(...)` inside partition finite-set wrappers | missing `category` argument because mypy sees the nested `Constructors` class constructor instead of the cached collector method result | PASS as the public named set-constructor collector returned by `Sets().Constructors()` | FAIL if code calls the nested `Constructors` class directly without passing the owning category |

### Constructor Collector Static Surfaces

The static model or companion stub generator must preserve the style-required
constructor collector shape: a nested `Constructors` class that declares the
collector methods, and a public `Constructors()` method that returns the
collector instance. This is not an ordinary class/method redefinition in the
mathematical surface; it is the project convention for discoverable constructor
namespaces such as `Sets().Constructors()` and `Modules(R).Constructors()`.

This is a checker-model gap when both declarations are the canonical collector
class and public collector accessor on a category. It is a source defect when an
unrelated class and method collide under the same name, or when a category
renames the collector only to appease static analysis.

Current focused seed from
`scratch/qc-reset-patches-20260515/validation/with-basis-index-set-source-fix-just-test.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/sets/__init__.py:1288` `class Constructors` plus `def Constructors(self) -> Constructors` on `Sets` | `Name "Constructors" already defined` | PASS because the nested class is the constructor collector declaration and the method is the public collector accessor required by category-spec style | FAIL for unrelated duplicate names that are not a category constructor collector class plus accessor pair |

### Sage Classcall Constructor Surfaces

The static model must also account for Sage classcall bridges where the public
constructor surface differs from `__init__`. In particular,
`CategoryWithAxiom_singleton` subclasses may be called without an explicit
`base_category`; `_SingletonAxiomClasscallMixin.__classcall__` redirects that
case through Sage's axiom-category constructor using the class's declared base
category and axiom.

This is a checker-model gap when a no-argument singleton axiom category call is
backed by a declared `_base_category_class_and_axiom` and the runtime classcall
bridge. It is a source defect when the class lacks that declaration, lacks the
singleton-axiom bridge, or the call supplies arguments not admitted by the
classcall surface.

Current reproducer seeds from
`scratch/qc-reset-patches-20260515/validation/matrix-algebra-finality-focused-mypy-after-parameterized-supercategories.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/rings/matrix_algebras.py:70` `_CommutativeRings()` | missing `base_category` because mypy checks `__init__` | PASS as a singleton axiom category constructor using `_base_category_class_and_axiom = (Rings, "Commutative")` | FAIL for a `CategoryWithAxiom_singleton` subclass without a declared base-category/axiom pair |
| `category_specs/rings/subcategories/field.py:58` `_CommutativeRings()` | missing `base_category` because mypy checks `__init__` | PASS for the same singleton axiom category constructor inside another ring subcategory | FAIL if the call targets a non-singleton or parameterized category requiring explicit constructor data |
| `category_specs/rings/subcategories/number_field.py:47` `_Fields()` | missing `base_category` because mypy checks `__init__` | PASS as a singleton axiom category constructor using `_base_category_class_and_axiom = (_CommutativeRings, "Field")` | FAIL if the field category class does not declare the base-category/axiom pair |
| `category_specs/rings/subcategories/dedekind_domain.py:37` `_IntegralDomains()` | missing `base_category` because mypy checks `__init__` | PASS as a singleton axiom category constructor using `_base_category_class_and_axiom = (_CommutativeRings, "IntegralDomains")` | FAIL if the integral-domain category class does not declare the base-category/axiom pair |
| `category_specs/rings/subcategories/quadratic_number_field.py:35` `_NumberFields()` | missing `base_category` because mypy checks `__init__` | PASS as a singleton axiom category constructor using `_base_category_class_and_axiom = (_Fields, "NumberFields")` | FAIL if the number-field category class does not declare the base-category/axiom pair |
| `category_specs/rings/subcategories/nonarchimedean_global_field.py:30` `_GlobalFields()` | missing `base_category` because mypy checks `__init__` | PASS as a singleton axiom category constructor using `_base_category_class_and_axiom = (_Fields, "GlobalFields")` | FAIL if the global-field category class does not declare the base-category/axiom pair |
| `category_specs/rings/subcategories/discrete_valuation_ring.py:37` `_ValuedRings()` | missing `base_category` because mypy checks `__init__` | PASS as a singleton axiom category constructor using `_base_category_class_and_axiom = (Rings, "WithValuation")` | FAIL if the valued-ring category class does not declare the base-category/axiom pair |
| `category_specs/rings/subcategories/complete.py:28` `_TopologicalRings()` | missing `base_category` because mypy checks `__init__` | PASS as a singleton axiom category constructor using `_base_category_class_and_axiom = (Rings, "Topological")` | FAIL if the topological-ring category class does not declare the base-category/axiom pair |
| `category_specs/homsets/endsets.py:95` `EndCategory()` | missing `base_category` because mypy checks `__init__` | PASS as a singleton axiom category constructor using `_base_category_class_and_axiom = (HomCategory, "Endset")` | FAIL for an end-category-like class without the singleton axiom declaration |
| `category_specs/homsets/autsets.py:155` `AutCategory()` | missing `base_category` because mypy checks `__init__` | PASS as a singleton axiom category constructor using `_base_category_class_and_axiom = (EndCategory, "Autset")` | FAIL for an aut-category-like class without the singleton axiom declaration |

### Functorial Construction Constructors

The static model must also account for Sage public construction-category calls
routed through `FunctorialConstructionCategory.__classcall__`. For construction
categories such as `Subobjects`, `Quotients`, `CartesianProducts`,
`TensorProducts`, and Hom-category construction classes, the public call surface
is the Sage selector/constructor expression, not the raw Python `__init__`
signature that mypy sees.

This is a checker-model gap when the call is a direct category-construction
surface admitted by the category graph. It is a source defect when code calls a
construction class with a non-category receiver, bypasses the owning selector
without required constructor data, or asks for a construction unavailable on the
resolved category.

Current focused seed from
`scratch/qc-reset-patches-20260515/validation/with-basis-index-set-source-fix-just-test.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/modules/subcategories/integer_lattices.py:31` `Modules(R).Subobjects()` inside `_IntegerLattices.super_categories` | `Too few arguments` because mypy checks the construction class initializer instead of Sage's public construction selector | PASS because `Subobjects()` is the category-construction selector on `Modules(R)` and Sage routes it through `FunctorialConstructionCategory.__classcall__` | FAIL if the receiver category does not expose `Subobjects()` or the construction is called as an unrelated raw class without the owning category data |
| `category_specs/rings/homsets.py:61` `HomCategoryOf(self.base_category())` inside `RingHomCategory.extra_super_categories` | `Too few arguments` because mypy checks the raw construction-category initializer instead of Sage's public category-construction call surface | PASS because `HomCategoryOf(C)` is the public construction category for hom objects over the resolved base category `C`, routed through Sage category construction machinery | FAIL if `C` is not a category or the call targets a raw construction class unrelated to the resolved category graph |
| `category_specs/sets/__init__.py:646` `Sets().Topological()` inside real-subset category refinement | `Too few arguments` because mypy checks the raw axiom-category initializer instead of Sage's public selector on `Sets()` | PASS because `Topological()` is the documented set-category navigation selector and Sage routes it through the category axiom/construction machinery | FAIL if the receiver is not `Sets()` or a compatible set category exposing the topological-set axiom |
| `category_specs/modules/__init__.py:606`, `:615`, and `:671` `C.Subobjects()` / `C.Quotients()` inside module constructor category helpers | `Too few arguments` because mypy checks raw construction-category initializers instead of the public selectors on `Modules(R)` or its refinements | PASS because `C` is the owning module category and these are Sage/project construction selectors for module subobjects and quotients | FAIL if `C` is not a module category or the requested construction is absent from the resolved category graph |
| `category_specs/algebras/subcategories/constructions/ideals.py:41` `Modules(self.base_ring()).Subobjects()` and `category_specs/lattices/subcategories/constructions/orthogonal_direct_sums.py:30` `Lattices(self.base_ring()).CartesianProducts()` | `Too few arguments` because mypy checks raw construction-category initializers instead of selectors on the resolved algebra/module/lattice category | PASS because these are construction selectors on the owning mathematical category: algebra ideals refine module subobjects, and orthogonal direct sums refine lattice cartesian products | FAIL if the receiver category is not the stated owner or the requested construction is absent from the resolved category graph |
| `category_specs/forms/__init__.py:147` and `category_specs/lattices/__init__.py:229` `Modules(base_ring, dispatch=False)` | checker reports unexpected keyword `dispatch` because it checks `Category_module.__init__` instead of `Modules.__classcall_private__` | PASS because `dispatch` is part of the public `Modules` classcall bridge used to opt out of automatic base-ring refinement while selecting the base module category | FAIL if the target class lacks a matching classcall surface or if the keyword is passed to an ordinary category constructor with no classcall bridge |

### Sage Axiom Hook Overrides

Sage still names axiom interop hooks such as `Endset` and `Autset` on category
classes so `_with_axiom(...)` can route through the correct axiom category. The
static model must allow a project wrapper to rebind such a hook to the
project-owned category class when the hook is backed by a matching
`_base_category_class_and_axiom` declaration. This is a checker-model gap when
the rebinding is a Sage axiom-hook bridge; it is a source defect when an
ordinary final class attribute is replaced with an unrelated object.

Current focused seed from
`scratch/qc-reset-patches-20260515/validation/hom-end-aut-focused-mypy-after-finality-and-call-source-fixes.log`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/homsets/homsets.py:120` `Endset = LazyImport(..., "EndCategory")` | cannot override final attribute `Endset` from Sage `Homsets` | PASS because the hook preserves Sage's `Endset` axiom name while routing to the project `EndCategory` | FAIL for rebinding a non-axiom final attribute or an axiom hook whose target lacks the matching base-category/axiom pair |

### Method-Container Type Surfaces

The static model must also make the public type-surface aliases for Sage method
containers usable as type expressions when the right-hand side is a real
category method container. Current mypy reports these as `valid-type` failures
because it sees nested method-container attributes as variables instead of
static class/type surfaces.

This is a checker-model gap when the alias names a canonical category,
object-method, element-method, Hom, End, or Aut method container that Sage can
resolve. It is a source defect when the alias points at a non-container value,
an unresolved `LazyImport`, a function, or the wrong owner/codomain surface.

Current reproducer seeds from
`scratch/qc-reset-patches-20260515/validation/method-container-type-alias-valid-type-seeds.txt`:

| Seed | Current checker failure | Expected model behavior | Negative control |
|------|-------------------------|-------------------------|------------------|
| `category_specs/sets/__init__.py:1358` `type SetsObject = Sets.ParentMethods` | `Sets.ParentMethods` is not valid as a type | PASS as the source-visible parent method-container type surface for `Sets()` | FAIL if the alias targets a non-method-container attribute |
| `category_specs/homsets/__init__.py:69` `type HomCategoriesObject = HomCategory.ParentMethods` | `HomCategory.ParentMethods` is not valid as a type | PASS as the public object-method type surface for the Hom category | FAIL if the alias targets a non-method-container attribute |
| `category_specs/homsets/__init__.py:74` `type EndCategoriesObject = EndCategory.ParentMethods` | `EndCategory.ParentMethods` is not valid as a type | PASS as the public object-method type surface for the End category | FAIL if the End category cannot resolve a parent method container |
| `category_specs/homsets/__init__.py:79` `type AutCategoriesObject = AutCategory.ParentMethods` | `AutCategory.ParentMethods` is not valid as a type | PASS as the public object-method type surface for the Aut category | FAIL if the Aut category cannot resolve a parent method container |
| `category_specs/rings/__init__.py:2007` `type RingsMorphism = RingHomCategory.ElementMethods` | `RingHomCategory.ElementMethods` is not valid as a type | PASS as the morphism element method-container surface for ring homsets | FAIL if the Hom category does not expose that element container |
| `category_specs/types.py:532` `type PartitionedSetMorphism = PartitionedSetsMorphism` after `PartitionedSetsMorphism = SetHomCategory.ElementMethods` | imported standard-package aliases to Hom/End/Aut method containers are not valid as types | PASS when the imported alias resolves to a canonical category method-container surface owned by the source module | FAIL if the imported alias is unresolved, targets a non-container value, or names a Hom/End/Aut surface from an unrelated owner |
| `category_specs/types.py:405` `type Ideal = _RingIdeals.ParentMethods` | `_RingIdeals.ParentMethods` is not valid as a type | PASS as the source-visible parent method-container surface for the ring-ideal construction category | FAIL if the construction category cannot expose a parent method container |
| `category_specs/modules/__init__.py:1858` `type ModulesObject = Modules.ParentMethods` | `Modules.ParentMethods` is not valid as a type | PASS for singleton category method containers and configured parameterized representatives | FAIL in singleton-only mode for unconfigured parameter-dependent containers |
| `category_specs/forms/__init__.py:153` `type FormsHom = RModuleHomCategory.ParentMethods` | inherited module Hom method container is not valid as a type | PASS when the forms surface reuses an already grounded module Hom container | FAIL if the reused Hom surface is not a semantic ancestor or admitted bridge |

### Axiom Categories (Secondary)

For axiom-generated categories such as `C.Finite.ParentMethods`, the plugin
must resolve against the axiom category's `parent_class.mro()` without
hardcoding axiom names. Detection: parse nested category classes and ask
Sage whether the nested class participates in the category-with-axiom system.

### Failure Modes

- **Not a Sage method container**: Return None (normal mypy behavior).
- **Wrong namespace but valid Sage category subtree**: Continue semantic
  resolution; do not reject solely because the fullname is outside
  `sage.categories.*`.
- **Sage cannot resolve the category**: Do not inject bases. Emit optional
  plugin note under a Sage-specific error code.
- **Runtime MRO resolves but source container can't be mapped to mypy
  TypeInfo**: Omit that base only if it contributes no source-level method
  container. Otherwise emit diagnostic — override checks may be unsoundly
  incomplete.
- **Parameterized category without configured representative**: No injection.
  Optional diagnostic.
- **Mypy rejects injected MRO**: Report the method-container fullname and the
  Sage-computed source-container bases.

### Sage-Side Integration API

The Sage-side API (`sage.categories.mypy_support`) must expose:

- `method_container_bases(category_cls_fullname, method_path) -> list[str]`:
  returns source-level fullnames of ancestor method containers
- `is_category_method_container(fullname) -> bool`
- `parse_method_container_fullname(fullname) -> CategoryMethodContainer | None`

The mapping must handle: `Groups.parent_class` → `Groups.ParentMethods`,
`Monoids.parent_class` → `Monoids.ParentMethods`, and analogous for
`element_class` ← `ElementMethods`, `morphism_class` ← `MorphismMethods`.

Runtime dynamic classes with no source-level method container are omitted from
the static base list.

## Test Matrix

Minimal tests required:

| Test | Category | Expected |
|------|----------|----------|
| Valid override | B.ParentMethods.@override f, B.super_categories → [A()], A.ParentMethods defines f | PASS |
| Invalid override | B.ParentMethods.@override g, g absent from all ancestors | FAIL |
| Diamond | B→A, C→A, D→[B,C]; B.ParentMethods.f, C.ParentMethods.f, D.ParentMethods.@override f | PASS (Sage-computed order) |
| ElementMethods | B.ElementMethods.@override f, A.ElementMethods defines f | PASS |
| MorphismMethods | B.MorphismMethods.@override f, A.MorphismMethods defines f | PASS |
| Homset | B.Homsets.ParentMethods.@override f | PASS |
| `_with_axiom` selector | C.SubcategoryMethods.Finite returns C._with_axiom("Finite") | PASS without local cast |
| `category_of` selector | C.SubcategoryMethods.Subobjects returns SubobjectsCategory.category_of(C) | PASS without local cast |
| `refine_category` return | Constructor returns refine_category(x, [C]) as the declared category object | PASS without local cast |
| Functorial construction constructor | `C.Subobjects()`, `HomCategoryOf(C)`, and analogous construction-category calls | PASS through Sage public construction dispatch |
| Constructor collector class/accessor | category nested `Constructors` class plus public `Constructors()` accessor | PASS without renaming the collector |
| Callable parent projection | Subobject parent calls ambient set or self through `__call__(x)` | PASS when source method surface exists |
| Method-container type alias | `type SetsObject = Sets.ParentMethods` and Hom/End/Aut analogues | PASS when RHS is a resolvable category method container |
| Invalid method-container alias | Alias points at a function, non-container value, wrong owner, or unconfigured parameterized surface | FAIL |
| Real source defect | Selector returns category/object with wrong owner or missing callable surface | FAIL |
| Parameterized no-config | Algebras(QQ).ParentMethods.@override | no injection |
| Parameterized configured | Algebras via configured rep | bases from rep |
| Third-party subtree | `third_party_pkg.demo.C.ParentMethods.@override f` with valid Sage semantic ancestor | PASS |
| Signature mismatch | @override with incompatible signature | FAIL |
| Renamed ancestor | remove f from A.ParentMethods | B.@override f → FAIL |
| Cache invalidation | change A.ParentMethods | B rechecked |
| Config path loads plugin | mypy invocation through repo/QC-style config path | plugin actually active |

## Current Status

Needs agent review. The 2026-05-10 rewrite removes namespace as the decisive admission
criterion, adds non-Sage fixture coverage alongside the Sage-prefixed matrix,
and wires `sage_mypy_category_plugin.plugin` into the global QC mypy config
path. The spec is back to review-ready pending independent verification of the
new evidence.
