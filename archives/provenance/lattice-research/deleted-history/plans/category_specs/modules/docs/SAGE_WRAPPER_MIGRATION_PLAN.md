# Sage Wrapper Subcategory Migration Plan

## Goal

The module subtree currently contains subcategories whose main purpose is to wrap Sage
implementation classes. That is the wrong abstraction when the Sage class names a
constructor family or a concrete implementation strategy rather than a mathematical
category.

The target state is:

- every module method from the Sage inventory is mapped to a real mathematical owner;
- constructor entry points route Sage objects into those owners by explicit construction
  case and precise Sage implementation-class matches at the boundary;
- chained axiom subcategories have their immediate supercategories declared before
  constructors depend on them;
- no category spec keeps a Sage-wrapper subcategory solely to expose methods from a Sage
  implementation class;
- `modules/smoketest.sage` asserts mathematical category membership and method behavior,
  not wrapper membership.

## Non-Negotiables

- Do not add explicit provider subclassing inside nested `ParentMethods`,
  `ElementMethods`, `MorphismMethods`, or `SubcategoryMethods`.
- Do not use `hasattr` or broad `try/except` to infer category membership.
- Do not route by generic duck-typing. Constructor routing may use exact Sage classes at
  the interop boundary; ordinary code should use mathematical categories.
- Do not keep a project subcategory unless it names a genuine mathematical category.
- Do not move a method just because a Sage wrapper used to provide it. Each method must
  be mapped from its mathematical meaning.
- Do not delete a wrapper until its methods are either represented on real categories,
  marked interop-only in `modules/docs/MAPPING.md`, or rejected with a documented
  mathematical reason.

## Prerequisites

- Use `modules/docs/SAGE_INVENTORY.md`, `modules/docs/MAPPING.md`, and
  `modules/docs/TRIAGE.md` as the starting sources.
- Read the Sage source and written Sage docs for each class before deciding its mapping.
- Use a commit checkpoint before each pass. Category-spec work uses the repository's
  no-verification commit path because the repo-wide hook is not scoped to this spec
  subtree.

## Efficient Order

The efficient order is mapping first, category graph second, constructors third,
method coverage fourth, deletion last. Doing this in any other order invites the same
failure mode: constructors and smokes depending on wrapper categories before the real
method owners exist.

## Current Execution State

Completed in the current branch:

- The wrapper inventory and mapping table have been created from the Sage inventory.
- `_CombinatorialFreeModules` has been deleted as a project subcategory. Construction
  now routes through `Modules(R).Constructors().CombinatorialFreeModule(...)` and
  refines into the real module categories `Free()`, `WithBasis()`, and
  `WithOrderedGeneratingSet()`.
- `WithBasis()` and `WithOrderedBasis()` are module axioms rather than Sage-wrapper
  categories. `WithOrderedBasis()` is a direct `Modules` axiom with immediate
  supercategories `WithBasis()` and `WithOrderedGeneratingSet()`.
- Standard free-module and basis subobject/quotient routing uses functorial
  construction categories such as `C.Free().FiniteRank().WithOrderedBasis()`,
  `C.WithOrderedBasis().Subobjects()`, and `C.WithOrderedBasis().Quotients()`.
- `FreeQuadraticModule` construction routes to a free finite-rank ordered-basis module
  with forms-owned bilinear/quadratic structure rather than to a wrapper category.
- Generic basis-owned methods are now represented on `WithBasis()` and
  `WithBasis().HomCategory()`.
- Generic subobject and quotient construction-owner surfaces are represented on the
  module construction categories.
- PID presentation invariant surfaces are represented on
  `FinitelyPresentedModulesOverPID`.

Smoke validation frontier:

- `just smoke-file modules/smoketest.sage` reaches the real module constructor
  assertions and reports missing category surfaces such as `algebra`, `_sympy_`, and
  `__richcmp__`, plus the representation/lattice key errors and graded-module base
  category mismatch recorded in `modules/docs/TRIAGE.md`.
- These failures are not evidence that constructor-only Sage wrapper categories should
  be restored.

## Phase: Freeze The Wrapper Inventory

Location: `modules/subcategories/`, `modules/__init__.py`,
`modules/docs/SAGE_INVENTORY.md`, `modules/docs/TRIAGE.md`.

Work:

- Build the authoritative candidate list from subcategory classes that either match Sage
  implementation classes in `__contains__` or exist only as constructor-family surfaces.
- Classify each candidate as constructor-only, real mathematical category, or mixed.
- For mixed candidates, split the implementation class evidence from the mathematical
  category name before any code edit.

Acceptance:

- `modules/docs/MAPPING.md` has a migration table covering every candidate in the todo
  list at the end of this file.
- Each row states the mathematical owner, constructor owner, and deletion condition.

Validation:

- `rg "_CombinatorialFreeModules|_FreeModulesWithStandardBasis|_VectorSpaces|_RepresentationModules" modules` finds only expected mapping/todo references until the
  later deletion phase.
- `git diff --check` passes.

Commit boundary:

- Commit only inventory and mapping documentation for this phase.

## Phase: Define The Mathematical Category Graph

Location: existing mathematical subcategories such as `free.py`,
`finitely_generated.py`, `finitely_presented.py`, `over_field.py`,
`over_integral_domain.py`, `over_pid.py`, `with_ordered_generating_set.py`,
construction-category files under `modules/subcategories/constructions/`,
forms-owned files under `forms/`, and hom/end/aut files where needed.

Work:

- Define missing immediate supercategories before any constructor depends on them.
- Express chains such as free finite-rank modules over fields through axiom/category
  composition, not by a wrapper class around `FreeModule_ambient_field`.
- Ensure subobject and quotient refinements are construction categories over the ambient
  module category, with ordered-generating-set refinements attached only where that
  structure is stated.
- Ensure bilinear, quadratic, lattice, and torsion-quadratic surfaces are stated as
  forms-owned categories, not as wrappers around Sage form implementations.
- If a Sage method requires a chained axiom subcategory that does not yet exist, define
  the immediate missing owner first rather than installing the method on a narrower
  implementation wrapper.

Acceptance:

- Every category method owner in `modules/docs/MAPPING.md` resolves to an existing
  category object or to a clearly named missing category entry.
- No nested provider class subclasses another provider class to simulate method
  inheritance.
- For every declared `C <= D` relation, `C.HomCategory() <= D.HomCategory()` follows
  from the category construction rather than from manual class manipulation.
- For every category `C`, `C.EndCategory() <= C.HomCategory()` follows from the generic
  end construction.

Validation:

- Probe or ripgrep confirms no explicit nested provider subclassing was introduced.
- The relevant smoke section reaches category construction without C3 or dynamic-key
  failures for the newly defined surfaces.
- `git diff --check` passes.

Commit boundary:

- Commit by coherent graph cluster: ambient/free/vector, subobjects/quotients,
  form-bearing modules, graded/Ore/representation.

## Phase: Rewrite Constructor Routing

Location: `modules/__init__.py`, constructor-specific helpers, and
`modules/smoketest.sage`.

Work:

- For each Sage constructor, call the Sage constructor once and refine the returned
  parent into the real categories identified in the mapping phase.
- Keep exact Sage implementation-class matches localized to the constructor-routing
  boundary.
- Route by construction case first, class match second, and declared mathematical
  refinements last.
- Remove routing to project wrapper categories as soon as the target mathematical
  categories exist.
- Preserve previously supported call shapes with smoke cases that exercise the old call
  paths through the new explicit routes.

Acceptance:

- Constructor methods return Sage objects refined into real project mathematical
  categories.
- Constructor smokes assert membership in mathematical categories such as
  `Modules(R).Free()`, `Modules(R).WithOrderedGeneratingSet()`,
  `Modules(R).Subobjects()`, `Modules(R).Quotients()`, and form-bearing refinements.
- No constructor helper uses `hasattr`, broad catch-and-retry logic, or membership in a
  soon-to-be-deleted wrapper category.

Validation:

- `just smoke-file modules/smoketest.sage` is the main check.
- If the smoke still fails, the failure must expose a real missing category graph edge
  or mapped method owner, not a hidden wrapper dependency.
- `git diff --check` passes.

Commit boundary:

- Commit constructor routing separately from method-surface moves.

## Phase: Move Method Surfaces To Real Owners

Location: category owners named in `modules/docs/MAPPING.md`; element and morphism
providers under those same owners; hom/end/aut files for morphism-specific methods.

Work:

- For every method available on a wrapper candidate, decide one of:
  - it is a parent method on a real module category;
  - it is an element method on a real element surface;
  - it is a morphism method on the relevant hom/end/aut category;
  - it is a constructor helper;
  - it is Sage interop-only and remains unexposed;
  - it is rejected because it has no mathematical meaning without extra structure.
- Add missing immediate categories before placing methods that require those hypotheses.
- Keep support/order/coordinate methods on basis-bearing or ordered-basis surfaces, not
  on all free modules.
- Keep submodule, quotient, tensor, product, dual, hom, end, and aut methods on their
  construction categories.

Acceptance:

- `modules/docs/MAPPING.md` has no unmapped methods for any class in the final todo
  list.
- Deleted wrapper files do not remove the only representation of any mapped method.
- Methods that require ordered bases, forms, finite rank, PID hypotheses, or field
  hypotheses are not installed on broader categories.

Validation:

- For each migrated class, add or update a smoke statement using a real Sage object and
  the final category owner.
- `just smoke-file modules/smoketest.sage` passes or stops at a documented blocker that
  is not a deleted-wrapper dependency.
- `git diff --check` passes.

Commit boundary:

- Commit one method-owner cluster at a time, after the corresponding smoke statements
  are updated.

## Phase: Delete Wrapper Subcategories

Location: `modules/subcategories/`, `modules/__init__.py`,
`modules/docs/MAPPING.md`, and imports in adjacent files.

Work:

- Delete constructor-only wrapper files after all of their methods have moved or been
  rejected.
- Remove lazy imports, constructor accessors, and smoke references to deleted wrappers.
- Keep only subcategories that name real mathematical categories, even if Sage currently
  implements them with a concrete class.
- For mixed candidates, delete only the implementation-wrapper surface and keep the
  mathematical category under a corrected name and graph.

Acceptance:

- `rg` finds no references to deleted wrapper class names outside migration docs.
- The remaining `modules/subcategories/*.py` files correspond to mathematical
  categories, construction categories, or axiomatic restrictions.
- `modules/smoketest.sage` does not assert membership in wrapper categories.

Validation:

- `just smoke-file modules/smoketest.sage`.
- `rg "CombinatorialFreeModules|FreeModulesWithStandardBasis|VectorSubspacesWithOrderedGeneratingSet|QuotientModulesWithOrderedGeneratingSet" modules` returns only intentional documentation entries after deletion.
- `git diff --check`.

Commit boundary:

- Commit wrapper deletion last, after method coverage is complete.

## Stop Rules

- Stop if a class cannot be classified as constructor-only, real category, or mixed
  from the Sage source and docs.
- Stop if a method needs a mathematical owner that has not been defined yet.
- Stop if a smoke failure is caused by a category graph mismatch. Fix the graph before
  changing constructors.
- Stop if the required next step is production code outside `plans/category_specs`; the
  no-verification path here applies only to this category-spec migration.

## Class Migration Todo

Status marker:

- `[x]` migrated: the Sage-wrapper layer is deleted, or the file is retained only as a
  real mathematical category surface with no exact Sage implementation-class
  containment definition.

| Status | Class | First mapping target | Migration result |
| --- | --- | --- | --- |
| [x] | `_CombinatorialFreeModules` | Constructor on `Modules(R)` refined to `Free()`, `WithBasis()`, and `WithOrderedGeneratingSet()` | Deleted. |
| [x] | `_FreeModulesWithStandardBasis` | Free finite-rank modules with ordered basis | Deleted; methods moved to free, ordered-basis, subobject, and quotient owners. |
| [x] | `_FiniteRankFreeModules` | `Modules(R).Free().FiniteRank()` | Deleted; tensor-calculus constructor routes to finite-rank free modules without a wrapper. |
| [x] | `_FreeModulesOverIntegralDomains` | `Modules(R).Free().OverIntegralDomain()` | Deleted; domain-specific methods live on integral-domain module owners. |
| [x] | `_FreeModulesOverPIDs` | `Modules(R).Free().OverPID()` | Deleted; PID-specific methods live on PID and finite-presentation owners. |
| [x] | `_VectorSpaces` | `Modules(K).Free().FiniteRank().OverField()` | Deleted; vector-space methods live on finite-rank free modules over fields. |
| [x] | `_RealDoubleVectorSpaces` | Finite-rank free modules over `RDF` | Deleted; numeric storage is interop-only and coordinate methods live on ordered-basis owners. |
| [x] | `_ComplexDoubleVectorSpaces` | Finite-rank free modules over `CDF` | Deleted; numeric storage is interop-only and coordinate methods live on ordered-basis owners. |
| [x] | `_VectorSubspaces` | `Modules(K).Subobjects()` over the vector-space refinement | Deleted; subspace methods live on subobject and field-linear owners. |
| [x] | `_VectorSubspacesWithOrderedGeneratingSet` | Field subobjects with ordered basis | Deleted; basis and coordinate methods live on ordered-basis subobject owners. |
| [x] | `_VectorSpaceQuotients` | `Modules(K).Quotients()` over the vector-space refinement | Deleted; quotient methods live on quotient owners. |
| [x] | `_FreeModuleSubmodules` | `Modules(R).Subobjects()` over free/PID module refinements | Deleted; submodule methods live on subobject owners with PID or basis hypotheses. |
| [x] | `_FreeModuleSubmodulesWithOrderedGeneratingSet` | Free-module subobjects with ordered basis | Deleted; user-basis methods live on ordered-basis owners. |
| [x] | `_SubmodulesWithOrderedGeneratingSet` | Subobjects of modules with bases | Deleted; implementation evidence is separated from subobject and basis owners. |
| [x] | `_FreeModuleQuotients` | `Modules(R).Quotients()` over free module refinements | Deleted; quotient cover and relation methods live on quotient owners. |
| [x] | `_QuotientModulesWithOrderedGeneratingSet` | Quotients of modules with bases | Deleted; quotient/basis methods live on quotient and basis owners. |
| [x] | `_FinitelyGeneratedPIDQuotientModules` | Finitely presented modules over PIDs | Deleted; invariant and Smith-generator methods live on `FinitelyPresentedModulesOverPID`. |
| [x] | `_FreeQuadraticModules` | Free modules with bilinear or quadratic form | Deleted; form methods live on forms-owned categories. |
| [x] | `_IntegerLattices` | Integral lattices as finite-rank free `ZZ`-modules with integral bilinear form | Retained as a real lattice/form category, not a Sage class wrapper. |
| [x] | `_TorsionQuadraticModules` | Finite torsion modules with quadratic form | Moved to `forms`; module path remains a compatibility route. |
| [x] | `_FreeGradedModules` | Free graded modules | Retained as a real graded-free category surface. |
| [x] | `_FinitelyPresentedGradedModules` | Finitely presented graded modules | Retained as a real graded finitely presented category surface. |
| [x] | `_OreModules` | Modules over Ore-polynomial quotient data | Retained as a real Ore-module category surface. |
| [x] | `_RepresentationModules` | Modules with a semigroup/group action | Retained as a real representation-module category surface. |
| [x] | `_RingObjectsAsModules` | Forgetful surface from ring objects to modules | Retained as a real ring-object-as-module category surface. |

## Per-Class Completion Rule

A class row can move to `[x]` only after all of the following are true:

- every inventoried method is mapped in `modules/docs/MAPPING.md` to a real owner or to
  an explicit interop-only or rejected non-mapping;
- every needed narrow category owner exists before the method is moved;
- constructor routing and smokes use real mathematical categories, not wrapper
  membership;
- the wrapper file, lazy import, constructor accessor, and membership smoke are deleted
  if the wrapper was constructor-only;
- `rg` finds the deleted wrapper name only in migration documentation.

All rows above satisfy the migration criterion for the Sage-wrapper layer.

## Migrated Method Clusters

- Ordered finite-rank coordinate surfaces: `basis_matrix`, `coordinate_vector`,
  `coordinates`, `from_vector`, and `echelonized_basis` live on ordered-basis owners.
- Field subobject and quotient surfaces: `linear_dependence`, subspace comparison,
  complement, and lift maps live on field-linear subobject or quotient owners.
- PID free and subobject surfaces: `index_in`, invariant data, Smith generators,
  basis-matrix, saturation, and echelon surfaces live on PID-refined owners.
- Quotient normal-form and basis surfaces: `free_cover`, `free_relations`, `lift_map`,
  `retract`, quotient-of-quotient structure, and `cokernel_basis_indices` live on
  quotient owners with the right basis or PID hypotheses.
- Form and lattice surfaces: Gram data and inner products live on forms-owned owners;
  lattice reduction lives on lattice owners.
- Graded, Ore, representation, and ring-object bridges are retained only as real
  mathematical category surfaces.
