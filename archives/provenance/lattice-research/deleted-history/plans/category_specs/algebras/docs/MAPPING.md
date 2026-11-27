# Algebras Mapping

`MagmaticAlgebras(R)` is the category of `R`-modules with bilinear multiplication.
`AssociativeAlgebras(R)` adds associativity without requiring a unit.
`Algebras(R)` is the associative unital endpoint. Algebra-specific methods belong in
this subtree. Ring and module methods are inherited from `rings` and `modules`.

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| Matrix-ring algebra methods | `Algebras(R)` plus matrix-algebra subcategories | A matrix ring is also an algebra over its base ring; algebra methods should not be redeclared in the ring subtree. |
| `FreeAlgebra(R, n, names)` and `algebras.Free(R, n, names)` | `Algebras(R).Constructors().free_algebra_from_set(generators=S)` | This is the true free associative unital `R`-algebra on a set of symbols. Sage's `Sets().example().algebra(R)` is not this construction. |
| Plain-set Sage `S.algebra(R)` and `Sets().Algebras(R)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)`, exposed by `S.free_module(R)` | Sage already constructs the free `R`-module with basis indexed by `S` on this path. The spec routes that Sage source surface to `Modules(R)` and rejects it as evidence for an `Algebras(R)` constructor. |
| `S.algebra(R)` where the selected source category is `Magmas()` | `Algebras(R).Constructors().free_algebra_from_magma(magma=S)` returning an object in `MagmaticAlgebras(R)` | This names the free functor from magmas to `R`-modules with bilinear multiplication. It is not necessarily associative or unital, so the target is the magmatic algebra category rather than the current unital-associative `Algebras(R)` endpoint. |
| `S.algebra(R)` where the selected source category is `Semigroups()` | `Algebras(R).Constructors().free_algebra_from_semigroup(semigroup=S)` returning an object in `AssociativeAlgebras(R)` | This names the free functor from semigroups to associative, not necessarily unital, `R`-algebra objects. |
| `S.algebra(R)` for a Sage monoid `S` | `Algebras(R).Constructors().free_algebra_from_monoid(monoid=S)` | This is the monoid algebra `R[S]`, the free construction relative to the multiplicative-monoid forgetful functor. |
| `G.algebra(R)` for a Sage group `G`; `GroupAlgebra(G, R)` | `Algebras(R).Constructors().free_algebra_from_group(group=G)` | The essential image of the group free functor lands in Hopf algebras over `R`; as an `R`-algebra it is the group algebra `R[G]`. |
| `S.algebra(R, category=AdditiveSemigroups())` | `Algebras(R).Constructors().free_algebra_from_additive_semigroup(semigroup=S)` returning an object in `AssociativeAlgebras(R)` | This is the semigroup algebra using the additively written operation as multiplication of basis elements. The target is associative and not necessarily unital. |
| `S.algebra(R, category=AdditiveMonoids())` | `Algebras(R).Constructors().free_algebra_from_additive_monoid(monoid=S)` | This is the monoid algebra using the additively written operation and zero element as multiplicative unit data. |
| `S.algebra(R, category=AdditiveGroups())` | `Algebras(R).Constructors().free_algebra_from_additive_group(group=S)` | This is the group algebra using the additively written group law. |
| `FiniteDimensionalAlgebra(k, table, assume_associative=True, assume_unital=True)` | First construct `mu: Tensor` through `TensorAlgebraComponents(k).Constructors().from_module_element_matrix(...)` or another tensor interop constructor, then call `Algebras(k).Constructors().from_multiplication_tensor(multiplication=mu)`. | Bespoke table/list/matrix shapes are tensor interop inputs, not algebra constructor inputs. The algebra constructor has one canonical product input: a tensor in `T_R(M)[1, 2]`. The tensor's parent determines the base module, the base ring, and the preferred generating set. |
| `FiniteDimensionalAlgebra(k, table)` without both associative and unital assumptions | `MagmaticAlgebras(k)` by default, with `AssociativeAlgebras(k)` when associativity is part of the category data | Sage says the default object is a magmatic algebra, not necessarily associative or unital. Associative but nonunital table data is not a current `Algebras(k)` object. |
| `AlgebrasWithBasis(R)` | `Algebras(R).WithBasis()` | `WithBasis` is shared module/vector-space vocabulary. The distinguished basis is structure on the algebra; multiplication remains element multiplication. |
| `CombinatorialFreeModule(R, basis_keys, category=AlgebrasWithBasis(R))` | `Algebras(R).Constructors().from_multiplication_tensor(multiplication=mu)` after constructing `mu` in `TensorAlgebraComponents(R)` | Sage uses this as infrastructure for algebras with basis, but the constructor alone supplies only the module with basis. The project constructor must specify the multiplication tensor mathematically; Sage `product_on_basis` is only an interop hook derived from that tensor. |
| `basis()` on an algebra with a distinguished basis | `AlgebraBasis` | The chosen basis is part of the structure of `WithBasis`; basis-returning helpers for derived subobjects are not separate public surfaces. |
| `one_basis()` | `one() -> AlgebraElement` plus constructor unit data when the unit is supplied by coordinates | Sage exposes the basis index of the unit when the unit is a basis vector. The project surface exposes the unit as an algebra element; a basis index is interop data only. |
| `product_on_basis(i, j)` | `MagmaticAlgebraElement.__mul__` on basis elements, inherited by associative and unital algebra endpoints | Sage exposes multiplication through basis indices. The project surface is element multiplication; construction supplies the multiplication tensor that makes `e_i * e_j` evaluate. |
| `algebra_generators()` | `AlgebraElementFamily` | Algebra generators form a family of algebra elements, not a generic set family. |
| `FiniteDimensionalAlgebrasWithBasis(R)` | `Algebras(R).FiniteDimensional().WithBasis()` | `FiniteDimensional` is shared vector-space vocabulary. This intersection is where Sage implements radical, center, idempotent lifting, Peirce decomposition, and semisimple quotients for algebras with basis. |
| `SemisimpleAlgebras(R)` | `Algebras(R).Semisimple()` | Semisimplicity uses the shared `Semisimple` axiom; algebra subcategories supply the algebra-specific method surface. |
| `CommutativeAlgebras(R)` | `Algebras(R).Commutative()` | Commutativity uses the shared `Commutative` axiom; this algebra surface records algebra-specific consequences without redefining the axiom. |
| `WithBasis`, `FiniteDimensional`, `Commutative`, `Semisimple` | shared axiom names from `axioms.py` | The algebra subtree contributes algebra-specific method surfaces for these restrictions instead of defining separate algebra-only axiom names. |
| `subalgebra(gens, category=None, *args, **opts)` | `subalgebra(generators)` | The generated subalgebra is algebra structure. Sage's `category` and option bag are implementation routing for the resulting submodule, not public algebra data. |
| `ideal_submodule(gens, side='left', category=None, *args, **opts)` | `left_ideal(generators)`, `right_ideal(generators)`, `two_sided_ideal(generators)` | The finite Sage side string is split into named ideal methods. Algebra ideals are module subobjects with left/right/two-sided predicates, so no side flag or category option is exposed. |
| `principal_ideal(a, side='left', *args, **opts)` | `principal_left_ideal(generator)`, `principal_right_ideal(generator)`, `principal_two_sided_ideal(generator)` | Principal ideal construction is the one-generator case of the corresponding named ideal operation. Sage's `coerce` option is compatibility plumbing and is not a category obligation. |
| `center`, `radical`, derivation and Hochschild methods | Algebra parent method surface | These methods depend on algebra structure, not merely ring or module structure. |
| `center_basis()` | `center() -> Algebra` | The public surface returns the center as the algebra spanned by that basis. The basis itself is implementation/inventory data recoverable from the returned object when it lies in `WithBasis`. |
| `radical_basis()` | `radical() -> AlgebraIdeal` | The public surface returns the radical as the ideal spanned by that basis, not a bare basis list. `AlgebraIdeal` is an `R`-module subobject in `Algebras(R).Ideals(A)`, not a ring ideal and not an algebra subobject. |
| `derivations_basis()` | `derivations() -> RModule` | The public surface returns the module or Lie algebra of derivations. A basis is recovered from that object when a basis has been chosen. |
| `annihilator_basis(...)` | `annihilator(...) -> AlgebraIdeal` | The public surface returns the annihilator ideal spanned by Sage's basis output. `AlgebraIdeal` carries `is_left_ideal()`, `is_right_ideal()`, and `is_two_sided_ideal()` predicates. |
| Quotients, subobjects, Cartesian products, tensor products, duals | `Algebras(R).<Construction>()` | These are construction categories attachable to arbitrary algebra subcategories by `category_of(self)`. Algebra subobjects are subalgebras; algebra ideals live in `Algebras(R).Ideals(A)` and inherit `ambient()`, `ambient_module()`, and `inclusion()` from `Modules(R).Subobjects()`. By construction, that ambient module is the algebra `A` viewed as an `R`-module. |
| Topological algebras | `Algebras(R)` plus `topological_spaces` | Topological-space methods belong to the topological-space subtree and should be inherited. |

Slice and coslice algebra objects keep the algebra-specific names
`structure_algebra()` and `structure_map()`. The old local
`Algebras(R).ObjectsOver(A).ParentMethods.structure_domain()` /
`structure_codomain()` and `Algebras(R).ObjectsUnder(A)` versions now map through the
Cat-owned universal `structure_morphism().domain()` and
`structure_morphism().codomain()` surface. This preserves the old behavior while
placing domain and codomain on the generic structure-morphism owner.

## Free-Construction Routing

For source categories admitted in this subtree, the public method on a source object is
`S.free_algebra(R)`. The source category, not a runtime `category=` keyword, chooses
the constructor. The `Sets()` row below is carried out by
`Sets.ParentMethods.free_algebra`, backed by Sage `FreeAlgebra`; it is not Sage's
plain-set `S.algebra(R)` path. The `Magmas()`, `Semigroups()`, `Monoids()`, and
`Groups()` rows record target constructor stubs in `Algebras(R).Constructors()`;
matching source-method stubs belong to those source-category subtrees when this project
admits them.

| Source category for `S` | Public source method | Constructor target |
| --- | --- | --- |
| `Sets()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_set(S)` |
| `Magmas()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_magma(S)` |
| `Semigroups()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_semigroup(S)` |
| `Monoids()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_monoid(S)` |
| `Groups()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_group(S)` |
| `AdditiveSemigroups()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_additive_semigroup(S)` |
| `AdditiveMonoids()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_additive_monoid(S)` |
| `AdditiveGroups()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_additive_group(S)` |

`Groups()` are not an unrelated constructor family: the group construction refines the
monoid construction, and its essential image lies in Hopf algebras over `R`.

The commutative additive source categories refine the corresponding additive rows. The
selected operation must be represented by the source category method, and the target
constructor name must say which source category is being used. Do not expose Sage's
generic `category=` disambiguation as project API.

Concrete constructor status:

| Constructor | Current route |
| --- | --- |
| `free_algebra_from_set(S)` | Sage `FreeAlgebra(R, |S|, names)`, refined to `Algebras(R).WithBasis()`. This is the true free associative unital algebra on generators. |
| `free_algebra_from_monoid(M)` | Sage `M.algebra(R, category=Monoids())`, refined to `Algebras(R).WithBasis()`. The monoid unit supplies the algebra unit. |
| `free_algebra_from_group(G)` | Sage `G.algebra(R, category=Groups())`, refined to `Algebras(R).WithBasis()`. Group-specific Hopf structure remains a later refinement, not a separate constructor path. |
| `free_algebra_from_additive_monoid(M)` | Sage `M.algebra(R, category=AdditiveMonoids())`, refined to `Algebras(R).WithBasis()`. The additive zero supplies the algebra unit. |
| `free_algebra_from_additive_group(G)` | Sage `G.algebra(R, category=AdditiveGroups())`, refined to `Algebras(R).WithBasis()`. |
| `free_algebra_from_magma(M)` | Sage `M.algebra(R, category=Magmas())` is executed, verified in `sage.categories.magmatic_algebras.MagmaticAlgebras(R).WithBasis()`, and refined to project `MagmaticAlgebras(R)`. |
| `free_algebra_from_semigroup(S)` | Sage `S.algebra(R, category=Semigroups())` is executed, verified in `sage.categories.associative_algebras.AssociativeAlgebras(R).WithBasis()`, and refined to project `AssociativeAlgebras(R)`. |
| `free_algebra_from_additive_semigroup(S)` | Sage `S.algebra(R, category=AdditiveSemigroups())` is executed, verified in `sage.categories.associative_algebras.AssociativeAlgebras(R).WithBasis()`, and refined to project `AssociativeAlgebras(R)`. |

## Plain-Set Sage Algebra Route

Sage's plain-set `S.algebra(R)` path is a module construction in the project spec:

| Sage source path | Project source spelling | Target constructor |
| --- | --- | --- |
| `S.algebra(R)` for `S in Sets()` with no selected multiplicative/additive structure | `S.free_module(R)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)` |

This routing preserves the old Sage functionality without admitting the Sage name as
algebra vocabulary. The true free associative algebra on a set of generators uses
`S.free_algebra(R)` and routes to `free_algebra_from_set`.

## Multiplication Tensor Constructor

The canonical finite-rank algebra constructor is:

```python
Algebras(R).Constructors().from_multiplication_tensor(multiplication=mu)
```

Here `mu` is a `Tensor` in `T_R(M)[1, 2]`. The constructor validates that tensor type and
uses `mu.base_module()` and `mu.parent()` to recover the underlying module and tensor
component. Callers do not pass a separate basis, table, module-element matrix, list of
matrices, or right-multiplication data to `Algebras(R)`. Those shapes belong to
`TensorAlgebraComponents(R).Constructors()`, whose job is to turn coordinate or
module-valued product data into the canonical tensor before algebra construction
begins.

Current implementation status: `from_multiplication_tensor(multiplication=mu)`
validates `mu.tensor_type() == (1, 2)`, checks the tensor base ring, reads
`mu.structure_constants()` against `mu.base_module().rank()`, converts those constants
to Sage's right-multiplication table convention, and calls Sage
`FiniteDimensionalAlgebra(R, table, category=MagmaticAlgebras(R).FiniteDimensional().WithBasis())`.
Sage's constructor prose names a field input, but the classcall has no field guard and
Sage's magmatic-algebra category method converts algebras with basis by passing
`R = self.base_ring()` to the same constructor. The result is refined to project
`MagmaticAlgebras(R)` and to `AssociativeAlgebras(R)` or
`Algebras(R).FiniteDimensional().WithBasis()` when the constructed table satisfies the
corresponding laws. Field-only algorithms on those parents remain method-level
frontiers, not constructor gaps.
