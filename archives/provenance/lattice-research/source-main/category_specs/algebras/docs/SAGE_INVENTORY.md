# Algebras Sage Inventory

This inventory records Sage algebra surfaces only. The source baseline is local
SageMath 10.7 (`sage --version`: `SageMath version 10.7, Release Date:
2025-08-09`) plus Sage's written reference pages.

## Sources Checked

| Source | Evidence used |
| --- | --- |
| Sage docs: `reference/categories/sage/categories/algebras.html` | Definition of `Algebras`, supercategories, `Semisimple`, `Supercommutative`, `TensorProducts`, and `WithBasis`. |
| Sage source: `sage/categories/magmatic_algebras.py` | `MagmaticAlgebras(R)` as modules over `R` with bilinear multiplication, with `Associative` and `Unital` axiom endpoints. |
| Sage source: `sage/categories/associative_algebras.py` | `AssociativeAlgebras(R)` as not-necessarily-unital associative algebras and an axiom subcategory of `MagmaticAlgebras(R)`. |
| Sage docs: `reference/categories/sage/categories/algebras_with_basis.html` | Definition of `AlgebrasWithBasis`, example parent, `basis`, `one_basis`, `algebra_generators`, `hochschild_complex`, tensor/cartesian products, and `example`. |
| Sage docs: `reference/categories/sage/categories/finite_dimensional_algebras_with_basis.html` | Definition of finite-dimensional algebras with basis and the radical, center, subalgebra, ideal, idempotent, Peirce, Cartan, and semisimple quotient methods. |
| Sage docs: `reference/categories/sage/categories/commutative_algebras.html` | `CommutativeAlgebras(R)` as `Algebras(R).Commutative()` and tensor-product consequences. |
| Sage docs: `reference/categories/sage/categories/semisimple_algebras.html` | `SemisimpleAlgebras` and its radical behavior. |
| Sage docs: `reference/categories/sage/categories/algebra_functor.html` | The `S.algebra(K, category=...)` construction, group/monoid/additive algebra examples, and the documented ambiguity for objects with both additive and multiplicative semigroup structure. |
| Sage docs: `reference/algebras/sage/algebras/free_algebra.html` | `FreeAlgebra(R, n, names)` and `algebras.Free(R, n, names)` as constructors for free associative unital algebras on symbols. |
| Sage source: `sage/categories/algebras.py` | `Algebras(base_category)`, `ParentMethods.characteristic`, `ParentMethods.has_standard_involution`, construction categories, and lazy subcategory names. |
| Sage source: `sage/categories/algebras_with_basis.py` | `AlgebrasWithBasis(base_category)`, `ParentMethods.hochschild_complex`, `example(alphabet=('a', 'b', 'c'))`, and tensor/cartesian product methods. |
| Sage source: `sage/categories/finite_dimensional_algebras_with_basis.py` | `FiniteDimensionalAlgebrasWithBasis(base_category)` and its finite-dimensional parent/element method surface. |
| Sage source: `sage/categories/algebra_functor.py` | `AlgebraFunctor(base_ring)`, `AlgebraFunctor.__call__(G, category=None)`, and `GroupAlgebraFunctor(group)`. |
| Sage source: `sage/categories/sets_cat.py` | `Sets.SubcategoryMethods.Algebras(base_ring)` and `Sets.ParentMethods.algebra(base_ring, category=None, **kwds)`. |
| Sage source: `sage/algebras/free_algebra.py` | `FreeAlgebraFactory`, `FreeAlgebra_generic`, and the optional letterplace implementation for free associative unital algebras. |
| Sage source: `sage/combinat/free_module.py` | `CombinatorialFreeModule(R, basis_keys=None, element_class=None, category=None, prefix=None, names=None, **kwds)`. |
| Sage source: `sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra.py` | `FiniteDimensionalAlgebra(k, table, names='e', assume_associative=False, assume_unital=False, category=None)`. |

## Category Surfaces

| Sage surface | Source | Sage method surface |
| --- | --- | --- |
| `sage.categories.magmatic_algebras.MagmaticAlgebras(base_ring)` | `sage/categories/magmatic_algebras.py` | Category of `R`-modules equipped with a bilinear multiplication; Sage documents that it is neither necessarily associative nor necessarily unital. |
| `sage.categories.associative_algebras.AssociativeAlgebras(base_ring)` | `sage/categories/associative_algebras.py` | Category of associative, not necessarily unital, algebras; Sage makes it `MagmaticAlgebras(R).Associative()` and explicitly not a subcategory of current Sage `Algebras(R)`. |
| `sage.categories.algebras.Algebras(base_category)` | `sage/categories/algebras.py` | Category of associative unital algebras over a base ring. Lazy subcategories include `Commutative`, `WithBasis`, `Semisimple`, `Super`, `Filtered`, and `Graded`. |
| `sage.categories.algebras_with_basis.AlgebrasWithBasis(base_category)` | `sage/categories/algebras_with_basis.py` | Algebras with a distinguished basis. Sage gives `example(alphabet=('a', 'b', 'c'))` and inherits unital-algebra-with-basis methods such as `one`, `one_basis`, and `product_on_basis`. |
| `sage.categories.finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis(base_category)` | `sage/categories/finite_dimensional_algebras_with_basis.py` | Finite-dimensional associative unital algebras with basis. This is the method-rich finite-dimensional surface for radical, center, idempotents, Peirce decomposition, Cartan invariants, and semisimple quotient. |
| `sage.categories.commutative_algebras.CommutativeAlgebras(base_category)` | `sage/categories/commutative_algebras.py` | Category of commutative algebras with unit; Sage documents it as the same shortcut as `Algebras(R).Commutative()`. |
| `sage.categories.semisimple_algebras.SemisimpleAlgebras(base, name=None)` | `sage/categories/semisimple_algebras.py` | Semisimple algebra restriction. Sage supplies `ParentMethods.radical_basis` as the zero radical basis. |
| `sage.categories.algebra_functor.AlgebrasCategory(category, *args)` | `sage/categories/algebra_functor.py` | Functorial category for algebras of objects in a source category, e.g. group algebras and monoid algebras. |

## Method Surfaces

| Sage owner | Methods recorded from Sage |
| --- | --- |
| `Algebras.ParentMethods` | `characteristic()`, `has_standard_involution()`. |
| `Algebras.SubcategoryMethods` | `Semisimple()`, `Supercommutative()`. |
| `Algebras.CartesianProducts` | `extra_super_categories()`. |
| `Algebras.TensorProducts` | `extra_super_categories()`, nested `ParentMethods`, nested `ElementMethods`. |
| `Algebras.Quotients.ParentMethods` | `algebra_generators()`. |
| `AlgebrasWithBasis.ParentMethods` | `hochschild_complex(M)`. The docs also exercise inherited `basis()`, `one_basis()`, `one()`, `algebra_generators()`, and multiplication through `product_on_basis`. |
| `AlgebrasWithBasis.ElementMethods` | `__invert__()` for elements that are scalar multiples of the basis unit. |
| `AlgebrasWithBasis.CartesianProducts.ParentMethods` | `one_from_cartesian_product_of_one_basis()`. |
| `AlgebrasWithBasis.TensorProducts.ParentMethods` | `one_basis()`, `product_on_basis(t1, t2)`. |
| `FiniteDimensionalAlgebrasWithBasis.ParentMethods` | `radical_basis()`, `radical()`, `semisimple_quotient()`, `center_basis()`, `center()`, `subalgebra(gens, category=None, *args, **opts)`, `ideal_submodule(gens, side='left', category=None, *args, **opts)`, `principal_ideal(a, side='left', *args, **opts)`, `orthogonal_idempotents_central_mod_radical()`, `idempotent_lift(x)`, `cartan_invariants_matrix()`, `isotypic_projective_modules(side='left')`, `peirce_summand(ei, ej)`, `peirce_decomposition(idempotents=None, check=True)`, `is_identity_decomposition_into_orthogonal_idempotents(idempotents)`, `is_commutative()`. |
| `FiniteDimensionalAlgebrasWithBasis.ElementMethods` | `to_matrix()`, `on_left_matrix()`. |

## Constructor Surfaces

| Sage constructor surface | Source-backed signature or behavior |
| --- | --- |
| `Sets.ParentMethods.algebra(base_ring, category=None, **kwds)` | Builds the algebra of a parent `S` over `base_ring`, using `category` to select which structure on `S` induces multiplication. It rejects objects that are both additive and multiplicative semigroups unless `category` disambiguates. |
| `AlgebraFunctor(base_ring).__call__(G, category=None)` | Calls `G.algebra(base_ring, category=category)`. Sage documents examples for groups and monoids. |
| `Sets.SubcategoryMethods.Algebras(base_ring)` | Returns the category of objects constructed as algebras of objects in the source category over `base_ring`, e.g. `Groups().Algebras(QQ)` or `Monoids().Algebras(QQ)`. |
| `GroupAlgebraFunctor(group)` | Construction functor from base rings to group algebras of a fixed group. Sage documents `GroupAlgebra(G, R) is G.algebra(R)`. |
| `FreeAlgebra(R, n, names)` / `algebras.Free(R, n, names)` | Builds the free associative unital algebra over `R` on the named generators. Sage also has a Singular letterplace implementation selected by `implementation='letterplace'`. |
| `CombinatorialFreeModule(R, basis_keys=None, element_class=None, category=None, prefix=None, names=None, **kwds)` | A free module with named basis. If `category=AlgebrasWithBasis(R)` and the object supplies algebra multiplication methods, Sage categorizes it as an algebra with basis; finite basis keys refine to finite-dimensional. |
| `FiniteDimensionalAlgebra(k, table, names='e', assume_associative=False, assume_unital=False, category=None)` | Builds a finite-dimensional `k`-algebra from a table of right-multiplication matrices. With both `assume_associative=True` and `assume_unital=True`, Sage places the result in `Algebras(k).FiniteDimensional().WithBasis()`. |

## Constructor Facts From Sage Examples

| Sage example | Observed fact |
| --- | --- |
| `FreeAlgebra(R, n, names)` | Produces a free associative unital algebra on the named symbols, with basis words in those symbols. |
| `G.algebra(R)` for a group `G` | Produces a group algebra in `Algebras(R)`; `GroupAlgebra(G, R)` is documented as strictly equivalent. |
| `S.algebra(R)` for a monoid `S` | Produces a monoid algebra in `Algebras(R)`. |
| `S.algebra(R, category=CommutativeAdditiveGroups())` | Produces an additive group algebra by extending the selected additive structure. |
| `Sets().example().algebra(QQ)` | Produces a Sage set-algebra category object backed by `GroupAlgebra_class` / `CombinatorialFreeModule`; Sage documents that it is not in `Algebras(QQ)`. |
| `CombinatorialFreeModule(F, basis_keys, category=Algebras(F).FiniteDimensional().WithBasis())` | Sage's finite-dimensional radical example wraps `K[x]/(x^p-1)` this way to obtain the finite-dimensional algebra-with-basis method surface. |
| `FiniteDimensionalAlgebra(k, table, assume_associative=True, assume_unital=True)` | Produces an associative unital finite-dimensional algebra with basis over the field `k`. |
