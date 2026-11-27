# Algebras Triage

## Current Smoke Frontier

On SageMath 10.7, `just smoke-file algebras/smoketest.sage` currently fails before
the smoke statement loop. `Algebras(ZZ)` raises while Sage tries to resolve
`subcategory_class` during category initialization:

- `AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has no attribute '_SageObject__custom_name'`

The same failure occurs from a clean `HEAD` archive, so this is not introduced by the
constructor inventory repair.

The next known non-constructor frontier remains:

- `Algebras(ZZ).DualObjects()` fails while Sage/project axiom inference tries to build
  the nested `category_specs.modules.homsets._Forms` class of `RModuleHomCategory`.
  This is a module hom-category/form-axiom blocker, not an algebra constructor issue.

## Remaining Constructor Blockers

| Blocker | Current status |
| --- | --- |
| Constructor admission | `docs/MAPPING.md` records candidate constructor targets. Free-construction names may appear as abstract spec targets, but callable implementations still require Sage-backed routing and refinement. |
| Additive algebra constructors | Sage uses `S.algebra(R, category=...)` for additive semigroups, additive monoids, and additive groups. The project needs explicit names and input types before adding stubs. |
| General algebra-with-basis constructor | Algebra construction is canonicalized to `from_multiplication_tensor(multiplication=mu)`, with `mu` a `Tensor` in `T_R(M)[1, 2]`. Module-element matrices, Sage tables, and matrix-list shapes must be converted by `TensorAlgebraComponents(R).Constructors()` before they reach `Algebras(R)`. |
| Nonunital and nonassociative table algebras | Sage's `FiniteDimensionalAlgebra(k, table)` defaults to magmatic algebras. These route to the appropriately named axiomatic algebra subcategories once those subtrees are scaffolded. |
| Basis-returning Sage helpers | Sage exposes helpers such as `center_basis()`, `radical_basis()`, and `derivations_basis()`. Project methods should return the algebraic object spanned by that basis, such as `center()`, `radical()`, or `derivations()`, and let basis recovery happen on the returned object when appropriate. |
| Plain-set Sage `S.algebra(R)` | Closed for `Algebras(R)`: this Sage path is routed to `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)` / `S.free_module(R)`. The actual set-to-algebra constructor is `free_algebra_from_set`, backed by Sage `FreeAlgebra`, not by `Sets().Algebras(R)`. |
