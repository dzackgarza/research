# Sage Module Inventory

This is a source-backed inventory of upstream Sage module-related constructors,
classes, categories, and method surfaces. It is organized around the category-spec
coverage questions for this subtree, but it records Sage facts only.

This file does not describe downstream implementation status, constructor-hook
status, or mappings from Sage objects into another hierarchy.

## Source Root And Scope

Sage paths below refer to the installed Sage tree at:

`/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage`

The inventory covers:

- Standard free modules, vector spaces, submodules, quotients, homspaces, and
  matrix morphisms.
- Quadratic free modules, integral quadratic lattices, integer lattice
  submodules, torsion quadratic modules, and finite quadratic form isometry
  groups.
- Combinatorial free modules, modules with basis, subquotients,
  representations, invariant modules, and cell modules.
- Finite-rank tensor-calculus modules, finitely presented graded modules, and
  Ore modules.
- Ring-side constructors and methods that create or expose module structure:
  `R^n`, `free_module`, ideals, matrix spaces, number-field order modules,
  polynomial and series ring constructors.

## Constructor Entry Points

| Source | Entry point | Sage behavior |
|---|---|---|
| `modules/free_module.py:248-305` | `FreeModuleFactory.create_object` | Dispatches free-module construction by base ring and `inner_product_matrix`; returns double vector spaces, field/PID/domain/general ambient free modules, or `FreeQuadraticModule`. |
| `modules/free_module.py:311-580` | `FreeModule(R, rank_or_basis_keys, ...)` | Main free-module constructor. `with_basis=None` returns `FiniteRankFreeModule`; non-integer `basis_keys` with standard basis return `CombinatorialFreeModule`; otherwise delegates to `FreeModuleFactory`. |
| `modules/free_module.py:583-613` | `VectorSpace(K, dimension_or_basis_keys, ...)` | Field-checking wrapper around `FreeModule`; raises `TypeError` when `K` is not a field or `sparse` is not boolean. |
| `modules/free_module.py:616-804` | `span(gens, base_ring=None, ...)` | Builds a module or vector subspace from generators; requires a PID base ring when supplied. |
| `modules/free_quadratic_module.py:86-187` | `FreeQuadraticModule(R, rank, inner_product_matrix, ...)` | Constructs a free quadratic module and dispatches by field/PID/domain/general base ring. |
| `modules/free_quadratic_module.py:190-220` | `QuadraticSpace(K, dimension, ...)` | Field-only wrapper around `FreeQuadraticModule`. |
| `combinat/free_module.py:36-1261` | `CombinatorialFreeModule(R, basis_keys, ...)` | Free module with arbitrary basis keys, defaulting to `ModulesWithBasis(R)`. |
| `modules/with_basis/subquotient.py:165-682` | `SubmoduleWithBasis(...)` | Submodule of a module with basis, normally constructed by `M.submodule(gens)`. |
| `modules/with_basis/subquotient.py:17-162` | `QuotientModuleWithBasis(...)` | Quotient of a module with basis by a submodule admitting unitriangular echelon reduction, normally constructed by `M.quotient_module(sub)`. |
| `modules/with_basis/representation.py:1036-1320` | `Representation(G, M, on_basis, side, ...)` | General semigroup representation on a module with basis. |
| `categories/semigroups.py:441-513` | `trivial_representation`, `regular_representation`, `representation` | Semigroup parent methods constructing representation modules. |
| `groups/matrix_gps/matrix_group.py:348-421` | `sign_representation`, `natural_representation` | Matrix-group entry points for sign and natural representations. |
| `modules/fg_pid/fgp_module.py:233-266` | `FGP_Module(V, W, check=True)` | Finitely generated module over a PID represented as `V/W`; quotient syntax on free modules also reaches this implementation. |
| `modules/free_module_integer.py:29-190` | `IntegerLattice(basis, lll_reduce=True)` | Constructs an integer lattice as `FreeModule_submodule_with_basis_integer`. |
| `modules/free_quadratic_module_integer_symmetric.py:73-259` | `IntegralLattice(data, basis=None)` | Constructs an integral symmetric lattice from a matrix, rank, Cartan datum, or `"U"`/`"H"`. |
| `modules/free_quadratic_module_integer_symmetric.py:263-616` | `IntegralLatticeDirectSum`, `IntegralLatticeGluing` | Integral lattice direct-sum and gluing constructors. |
| `modules/torsion_quadratic_module.py:35-87` | `TorsionQuadraticForm(q)` | Constructs a finite quadratic module from a rational symmetric matrix. |
| `modules/torsion_quadratic_module.py:188-1289` | `TorsionQuadraticModule(V, W, ...)` | Finite `ZZ`-module with bilinear/quadratic form; subclasses the finitely generated PID quotient module implementation. |
| `tensor/modules/finite_rank_free_module.py:1020-3329` | `FiniteRankFreeModule(R, rank, ...)` | Basis-free finite-rank free module used by tensor calculus and differential geometry. |
| `modules/fp_graded/free_module.py:296-1059` | `FreeGradedModule(algebra, generator_degrees, ...)` | Free graded module over a connected graded algebra. |
| `modules/fp_graded/module.py:70-1338` | `FPModule(arg0, generator_degrees=None, relations=(), ...)` | Finitely presented graded module, either as a cokernel or from generators and relations. |
| `rings/polynomial/ore_polynomial_ring.py:73-1334` | `OrePolynomialRing(...)` and `.quotient_module(P)` | Ore polynomial ring and quotient-module constructor for Ore modules. |
| `modules/ore_module.py:316-2206` | `OreModule`, `OreSubmodule`, `OreQuotientModule` | Finite free modules over the coefficient ring equipped with an Ore pseudomorphism. |
| `categories/rings.py:885-906` | `R^n`, `R^(m,n)` | `R^n` returns `FreeModule(R, n)`; `R^(m,n)` returns `MatrixSpace(R, m, n)`. |
| `categories/rings.py:1622-1686` | `R.free_module(base=None, basis=None, ...)` | Default ring method returning a free module over the ring itself; non-self bases raise `NotImplementedError`. |
| `matrix/matrix_space.py:677-924` | `MatrixSpace(R, m, n, ...)` | Matrix-space constructor; rectangular spaces are modules with basis, square spaces are algebras with basis. |

## Sage Category Interop

### `Modules`

Source: `categories/modules.py:34-180`, `:603-980`.

- `Modules.__classcall_private__(base_ring)` dispatches `Modules(field)` to
  `VectorSpaces(field)`.
- `Modules.super_categories()` returns `Bimodules(R, R)`.
- `Modules.ParentMethods` supplies `linear_combination`, `tensor_square`,
  `module_morphism`, and `quotient`.
- `Modules.Homsets.ParentMethods` supplies `base_ring` and `zero`.
- `Modules.CartesianProducts.ParentMethods.__init_extra__` records a common base
  ring when all factors share one.
- `Modules.TensorProducts.ParentMethods` supplies `construction` and
  `tensor_factors`.

### `ModulesWithBasis`

Source: `categories/modules_with_basis.py:45-179`, `:207-360`, `:2453-2790`.

- `ModulesWithBasis._call_` coerces objects exposing `free_module()` and changes
  ring if needed.
- `ModulesWithBasis.is_abelian()` is `True` exactly when the base ring is a
  field.
- `ParentMethods` includes `basis`, `module_morphism`, `submodule`,
  `quotient_module`, `tensor`, `intersection`, `cardinality`, `is_finite`,
  `dimension`, `rank`, and `random_element`.
- `ElementMethods` includes coefficient, support, leading/trailing term,
  mapping, and tensor helpers: `monomial_coefficients`, `__getitem__`,
  `coefficient`, `items`, `is_zero`, `__len__`, `length`, `support`,
  `monomials`, `terms`, `coefficients`, `support_of_term`, leading/trailing
  variants, `map_coefficients`, `map_support`, `map_support_skip_none`,
  `map_item`, and `tensor`.
- `Homsets.ParentMethods.__call_on_basis__` constructs morphisms from basis
  maps by forwarding to `module_morphism`.
- `MorphismMethods.on_basis` and `_on_basis` expose the basis-map view of a
  morphism.
- `TensorProducts.ElementMethods.apply_multilinear_morphism` applies
  multilinear maps to tensor elements.
- `DualObjects.extra_super_categories` links dual objects back to
  `Modules(base_ring)`.

## Standard Free Modules And Vector Spaces

### Class Families

Source: `modules/free_module.py`.

- `Module_free_ambient` (`:864-1941`) is the base class for ambient free modules.
  Its initializer builds a finite-dimensional `ModulesWithBasis` category,
  refines finite objects to `Enumerated().Finite()` when possible, and joins any
  supplied category. Method surface includes element construction, degree,
  sparsity, exactness, zero, relations, ambient-submodule comparison, span,
  submodule construction, quotient construction, and free-resolution helpers.
- `FreeModule_generic` (`:1944-3770`) adds rank and coordinate-ring
  bookkeeping, dense/sparse conversion, basis and coordinate extraction, direct
  sums, scalar scaling, iteration, cardinality, random elements, and interop
  hooks such as `_magma_init_`, `_macaulay2_`, and `_sympy_`.
- `FreeModule_generic_domain`, `FreeModule_generic_pid`,
  `FreeModule_generic_field` (`:3773-5461`) specialize ambient comparison and
  linear algebra. Domain/PID surfaces include `intersection`, `saturation`,
  `denominator`, `index_in`, Smith/Hermite form operations, `span_of_basis`,
  `vector_space_span`, `vector_space_span_of_basis`, and quotient behavior.
  Field surfaces include `linear_dependence`, `subspace`, `subspaces`,
  `subspace_with_basis`, `zero_subspace`, `complement`, `quotient_module`,
  `quotient_abstract`, and quotient matrix construction.
- `FreeModule_ambient`, `FreeModule_ambient_domain`,
  `FreeModule_ambient_pid`, `FreeModule_ambient_field` (`:5470-6544`) are the
  standard-basis ambient implementations. They supply representation, generator
  methods, basis caching, coercions, `change_ring`, `coordinate_vector`,
  `random_element`, `_repr_`, and `_latex_`; domain and field versions add
  fraction-field and base-field behavior.
- `FreeModule_submodule_with_basis_pid`, `FreeModule_submodule_pid`,
  `FreeModule_submodule_with_basis_field`, and `FreeModule_submodule_field`
  (`:6569-8287`) implement row-echelon submodules and subspaces. Method surface
  includes echelonization, basis matrices, coordinate transforms, lift, retract,
  change of ring, ambient/ambient-vector-space access, and user-basis tracking.

### Core Method Surface

- Ambient/free-module methods: `degree`, `rank`, `basis`, `gens`,
  `basis_matrix`, `coordinate_vector`, `coordinates`, `gen`, `random_element`,
  `scale`, `direct_sum`, `intersection`, `submodule`, `submodule_with_basis`,
  `quotient_module`, `__truediv__`, `change_ring`, `ambient_module`,
  `zero_submodule`, `relations`, `free_resolution`, `graded_free_resolution`.
- Submodule methods: `construction`, `lift`, `retract`, `ambient`,
  `ambient_vector_space`, `change_ring`, `coordinate_vector`,
  `echelon_coordinate_vector`, `echelonized_basis`,
  `echelonized_basis_matrix`, `has_user_basis`.
- Quotient methods: `cover`/`V`, `relations`/`W`, `free_cover`,
  `free_relations`, `quotient_map`, `lift_map`, `lift`, coercion maps, element
  construction, representation, and hashing.
- Element dispatch: `element_class` (`modules/free_module.py:8295-8376`) selects
  dense or sparse vector element classes by base ring and sparsity, including
  integer, rational, modular, real double, complex double, callable symbolic,
  symbolic, and generic free-module element classes.

### Standard Caveats

- `FreeModuleFactory` warns but still constructs modules over noncommutative
  base rings; the source warns that left/right behavior is not guaranteed.
- `FreeModule(..., with_basis=None)` rejects `inner_product_matrix`.
- Unsupported `with_basis` values raise `NotImplementedError`.
- `span(gens, base_ring)` requires a PID.
- `FreeModule_generic.quotient_module` is fully implemented for fields and
  `ZZ`; other rings can raise `NotImplementedError`.
- `FreeModuleMorphism.inverse_image` and `lift` require a field or a ring with
  Hermite form support.

## Homsets, Morphisms, And Matrix Morphisms

### Free-Module Homspaces

Sources:

- `modules/free_module_homspace.py:132-368`
- `modules/free_module_morphism.py:74-822`
- `modules/matrix_morphism.py:84-1744`

`FreeModuleHomspace` subclasses `HomsetWithBase` and constructs morphisms from
matrices, generator images, or callables. It supplies `__call__`, `zero`,
`_matrix_space`, `basis`, and `identity`.

`FreeModuleMorphism` subclasses `MatrixMorphism` and adds `pushforward`,
`change_ring`, `inverse_image`, `lift`/`preimage_representative`,
`eigenvalues`, `eigenvectors`, `eigenspaces`, and representation methods.

`BaseIsomorphism1D`, `BaseIsomorphism1D_to_FM`, and
`BaseIsomorphism1D_from_FM` implement rank-1 isomorphisms between a base ring and
its one-dimensional free module.

`MatrixMorphism_abstract` supplies comparison, evaluation, inversion, side
switching, arithmetic, rank, nullity, kernel, image, restriction, identity
tests, zero tests, injectivity, surjectivity, and bijectivity checks.
`MatrixMorphism` stores the matrix and adds matrix access plus shape/side
validation.

### Finitely Generated PID Homspaces

Sources:

- `modules/fg_pid/fgp_morphism.py:31-548`

`FGP_Morphism` subclasses `Morphism`. Its method surface includes `im_gens`,
comparison, addition, subtraction, negation, call/evaluation, `kernel`,
`inverse_image`, `image`, and `lift`.

`FGP_Homset_class` subclasses `Homset` with `Element = FGP_Morphism`. It chooses
`ModulesWithBasis(R)` when both ends are free, otherwise `Modules(R)`, and
supplies coercion and element construction.

### Finite-Rank Homsets

Sources:

- `tensor/modules/free_module_homset.py:37-349`
- `tensor/modules/free_module_morphism.py:38-198`, `:1262-1419`

`FreeModuleHomset` and `FreeModuleEndset` construct morphisms and endomorphisms
between finite-rank free modules. `FiniteRankFreeModuleMorphism` and
`FiniteRankFreeModuleEndomorphism` supply `matrix`, `display`, `_call_`,
`is_injective`, `is_surjective`, `is_identity`, and common-basis helpers.

### FP-Graded Homspaces

Sources:

- `modules/fp_graded/free_homspace.py:48-52`
- `modules/fp_graded/homspace.py:55-562`
- `modules/fp_graded/morphism.py:420-761`, `:1617-1987`

`FreeGradedModuleHomspace` is a thin subclass of `FPModuleHomspace`.
`FPModuleHomspace` supplies element construction, `zero`, `identity`,
`an_element`, `basis_elements`, internal basis computation, and `matrix_space`.
`FPModuleMorphism` supplies evaluation, representation-definition helpers,
surjectivity, image/kernel/cokernel/coimage machinery, and resolution helpers.

### Ore Homspaces

Sources:

- `modules/ore_module_homspace.py:27-145`
- `modules/ore_module_morphism.py:272-380`, `:512-942`

`OreModule_homspace` supplies `matrix_space`, `identity`, `zero`, and element
construction. `OreModuleMorphism` supplies matrix construction, representation
type, evaluation, arithmetic, equality, injectivity, surjectivity,
bijectivity, inverse, kernel, image, cokernel, and coimage.

## Quadratic Free Modules And Integral Lattices

### Free Quadratic Modules

Source: `modules/free_quadratic_module.py`.

- `FreeQuadraticModule_generic` (`:258-585`) subclasses `FreeModule_generic`,
  stores an inner-product matrix, and supplies `determinant`, `discriminant`,
  `gram_matrix`, `inner_product_matrix`, and dot-product/diagonal predicates.
- `FreeQuadraticModule_generic_pid` and `FreeQuadraticModule_generic_field`
  (`:588-813`) add PID- and field-specific `span`, `span_of_basis`, and
  `zero_submodule`.
- `FreeQuadraticModule_ambient`, `_domain`, `_pid`, and `_field`
  (`:822-1200`) mirror free-module ambient classes while preserving the
  inner-product matrix through ambient/vector-space/dense/sparse conversions
  and representations.
- `FreeQuadraticModule_submodule_with_basis_pid`,
  `FreeQuadraticModule_submodule_pid`,
  `FreeQuadraticModule_submodule_with_basis_field`, and
  `FreeQuadraticModule_submodule_field` (`:1210-1717`) preserve inner products
  through change of basis, change of ring, and comparison operations.

### Integer Lattice Submodules

Sources:

- `modules/free_module_integer.py:29-894`

`IntegerLattice(basis, lll_reduce=True)` constructs a
`FreeModule_submodule_with_basis_integer`, which subclasses
`FreeModule_submodule_with_basis_pid`. Its method surface includes
`reduced_basis`, `LLL`, `BKZ`, `HKZ`, `volume`, `discriminant`,
`is_unimodular`, `shortest_vector`, `update_reduced_basis`, `voronoi_cell`,
`voronoi_relevant_vectors`, `closest_vector`, `approximate_closest_vector`, and
`babai`.

### Integral Symmetric Lattices

Source: `modules/free_quadratic_module_integer_symmetric.py:73-1705`.

`FreeQuadraticModule_integer_symmetric` subclasses
`FreeQuadraticModule_submodule_with_basis_pid`. Its construction enforces
symmetry, integrality, and nondegeneracy. Its method surface includes
`is_even`, `dual_lattice`, `discriminant_group`, `signature`,
`signature_pair`, `direct_sum`, `is_primitive`, `orthogonal_complement`,
`sublattice`, `overlattice`, `maximal_overlattice`, `tensor_product`, `twist`,
`orthogonal_group`, `automorphisms`, `genus`, `quadratic_form`, `minimum`,
`maximum`, `LLL`, `short_vectors`, `enumerate_short_vectors`, and
`enumerate_close_vectors`.

Caveats:

- `IntegralLattice`, `IntegralLatticeDirectSum`, and `IntegralLatticeGluing`
  validate symmetry, integrality, nondegeneracy, and discriminant-group
  constraints.
- `orthogonal_group` computes generators only for definite lattices.
- Several methods depend on optional packages such as fpylll, PARI, GAP,
  graph/combinatorics components, and p-adic functionality.

## Combinatorial Modules, Subquotients, And Representations

### Combinatorial Free Modules

Source: `combinat/free_module.py:36-1975`.

`CombinatorialFreeModule` subclasses `UniqueRepresentation`, `Module`, and
`IndexedGenerators`. It defaults to `ModulesWithBasis(R)` and upgrades to a
finite-dimensional category when the basis key set is finite.

Methods defined directly on `CombinatorialFreeModule` include
`__classcall_private__`, `element_class`, `__init__`, `construction`,
`change_ring`, `_element_constructor_`, `_convert_map_from_`,
`_coerce_map_from_`, `dimension`, `is_exact`, `set_order`, `get_order`,
`get_order_key`, `_order_key`, `from_vector`, `sum`, `linear_combination`,
`term`, `monomial`, `_sum_of_monomials`, `sum_of_terms`, `zero`, and
`_from_dict`.

`CombinatorialFreeModule_Tensor` subclasses `CombinatorialFreeModule` and is
the tensor-product implementation behind tensor constructors. Its methods
include `tensor_factors`, `tensor_constructor`, `_tensor_of_elements`,
`_coerce_map_from_`, `_repr_`, `_ascii_art_`, `_unicode_art_`, `_latex_`,
`_repr_term`, and `_latex_term`.

`CombinatorialFreeModule_CartesianProduct` subclasses
`CombinatorialFreeModule` and supplies `cartesian_embedding`,
`cartesian_projection`, `_cartesian_product_of_elements`, `cartesian_factors`,
`_sets_keys`, and representation helpers.

### Submodules And Quotients With Basis

Source: `modules/with_basis/subquotient.py:17-682`.

`SubmoduleWithBasis` subclasses `CombinatorialFreeModule`. It represents a
submodule spanned by an echelon or triangular basis. Its methods include
`ambient`, `_support_key`, `lift`, `reduce`, `retract`, `is_submodule`,
`_common_submodules`, `is_equal_subspace`, `__add__`, `__and__`, and
`subspace`.

`QuotientModuleWithBasis` subclasses `CombinatorialFreeModule`. It represents a
quotient by a free submodule admitting unitriangular echelon form. Its methods
include `ambient`, `lift`, and `retract`.

Caveats:

- `SubmoduleWithBasis` construction depends on echelon form, `unitriangular`
  lifts, and support order.
- `QuotientModuleWithBasis` expects a submodule whose lift supports
  `cokernel_basis_indices` and whose parent can reduce elements modulo the
  submodule.

### Representation Modules

Sources:

- `modules/with_basis/representation.py:29-2937`
- `modules/with_basis/invariant.py:27-1073`
- `modules/with_basis/cell_module.py:22-393`

`Representation_abstract` supplies `semigroup`, `semigroup_algebra`, `side`,
`invariant_module`, `twisted_invariant_module`, `representation_matrix`,
`character`, `brauer_character`, `exterior_power`, `symmetric_power`,
`schur_functor`, `_semigroup_action`, `is_irreducible`,
`find_subrepresentation`, `subrepresentation`, `quotient_representation`,
`_composition_series_data`, `composition_series`, and `composition_factors`.

Concrete representation classes:

- `Representation`: general semigroup representation on a module with basis;
  adds `_test_representation`, `_element_constructor_`, `product_by_coercion`,
  `_semigroup_action`, and an element `_acted_upon_`.
- `Subrepresentation`: representation submodule; adds representation-specific
  initialization and representation text.
- `QuotientRepresentation`: quotient representation.
- `Representation_Tensor`: tensor-product representation; flattens nested
  tensor products and preserves finite-dimensional categories when all factors
  are finite-dimensional.
- `Representation_Exterior` and `Representation_ExteriorAlgebra`: exterior
  powers and exterior algebra; add action-on-basis, term formatting,
  `one_basis`, and `product_on_basis`.
- `Representation_Symmetric`: symmetric-power representation; adds
  symmetric-term conversion and action-on-basis.
- `RegularRepresentation`: semigroup regular representation with left and
  right basis actions.
- `TrivialRepresentation`: one-dimensional trivial representation.
- `SignRepresentation_abstract` and permgroup/matrix-group/Coxeter
  specializations: sign representations with `_default_sign`.
- `ReflectionRepresentation`: reflection representation.
- `NaturalMatrixRepresentation`: natural matrix-group representation.
- `SchurFunctorRepresentation`: Schur functor representation.

`FiniteDimensionalInvariantModule` subclasses `SubmoduleWithBasis` and supplies
`construction`, `_test_invariant`, `semigroup`, representation helpers, and
element action/multiplication behavior.

`FiniteDimensionalTwistedInvariantModule` subclasses `SubmoduleWithBasis` and
supplies `project`, `project_ambient`, and `projection_matrix`.

`CellModule` subclasses `CombinatorialFreeModule` and supplies
`cellular_algebra`, `_action_basis`, `_bilinear_form_on_basis`,
`bilinear_form`, `bilinear_form_matrix`, `nonzero_bilinear_form`,
`radical_basis`, `radical`, `simple_module`, and element action.

Caveats:

- `Semigroups.ParentMethods.trivial_representation` ignores `side`.
- `regular_representation` is explicitly left/right.
- `twisted_invariant_module` assumes the base ring contains character values
  and `1/|G|`.
- `exterior_power(None)` and `exterior_power(0)` use the exterior-algebra
  specialization.
- Matrix-group sign representation falls back to the trivial representation in
  characteristic 2.

## Finitely Generated PID Quotients And Torsion Quadratic Modules

### Finitely Generated PID Modules

Sources:

- `modules/fg_pid/fgp_module.py:1-1970`
- `modules/fg_pid/fgp_element.py:27-454`
- `modules/fg_pid/fgp_morphism.py:31-548`

`FGP_Module_class` subclasses `Module` and represents a module as `V/W`, with
noncanonical element lifts in `V` and Smith-form data for invariants.

Parent methods include:

- presentation/accessors: `V`, `W`, `cover`, `relations`, `base_ring`.
- quotient/coercion: `_module_constructor`, `_coerce_map_from_`,
  `has_canonical_map_to`, `is_submodule`, `__contains__`, `__truediv__`,
  `_element_constructor_`.
- Smith/coordinate methods: `_relative_matrix`, `_smith_form`,
  `smith_form_gens`, `invariants`, `gen`, `smith_form_gen`, `optimized`,
  `linear_combination_of_smith_form_gens`.
- hom methods: `hom`, `_hom_general`, `_hom_from_smith`, `_Hom_`,
  `quotient_map`.
- arithmetic/enumeration: `_mul_`, `random_element`, `cardinality`,
  `is_finite`, `annihilator`, `list`, `__iter__`.
- comparison/hash: `__eq__`, `__ne__`, `__lt__`, `__gt__`, `__ge__`,
  `__hash__`.

`FGP_Element` subclasses `ModuleElement` and supplies `lift`, `__neg__`,
`_add_`, `_sub_`, `_rmul_`, `_lmul_`, `_repr_`, `__getitem__`, `vector`,
`_vector_`, `_richcmp_`, `__hash__`, and `additive_order`.

Caveats:

- The module documentation states that the implementation is currently enabled
  and tested mainly over `ZZ`, although many algorithms make sense over more
  general PIDs with Hermite form.
- `FGP_Module_class.__iter__` is only for finite quotients over `ZZ`.

### Torsion Quadratic Modules

Sources:

- `modules/torsion_quadratic_module.py:35-1289`
- `groups/fqf_orthogonal.py:59-382`

`TorsionQuadraticModuleElement` subclasses `FGP_Element` and supplies bilinear
and quadratic product methods: `_mul_`/`inner_product`/`b` and
`quadratic_product`/`q`.

`TorsionQuadraticModule` subclasses `FGP_Module_class` and
`CachedRepresentation`. Construction paths include `TorsionQuadraticForm(q)`
and `IntegralLattice.discriminant_group(s=0)`. Parent methods include
`all_submodules`, `brown_invariant`, `gram_matrix_bilinear`,
`gram_matrix_quadratic`, `gens`, `genus`, `is_genus`, `orthogonal_group`,
`orthogonal_submodule_to`, `normal_form`, `primary_part`,
`submodule_with_gens`, `twist`, `value_module`, and `value_module_qf`.

`FqfIsometry` subclasses `AbelianGroupAutomorphism` and supplies `_repr_` and
`__call__`. `FqfOrthogonalGroup` subclasses
`AbelianGroupAutomorphismGroup_subgroup` and supplies `invariant_form`,
element construction, `_preserves_form`, `_get_action_`,
`_subgroup_constructor`, and representation.

Caveats:

- `TorsionQuadraticModule.__classcall__` only supports `ZZ`, requires equal
  ranks, and checks symmetry on the cover.
- `all_submodules` materializes all submodules.
- `brown_invariant` requires values in `QQ/2ZZ`.
- `is_genus` implements the even-lattice case; odd genera raise
  `NotImplementedError`.

## Finite-Rank Tensor Modules

Sources:

- `tensor/modules/finite_rank_free_module.py:1020-3329`
- `tensor/modules/free_module_element.py:1-283`
- `tensor/modules/free_module_morphism.py:38-198`, `:1262-1419`
- `tensor/modules/free_module_homset.py:37-349`

`FiniteRankFreeModule` subclasses `ReflexiveModule_base` and
`FiniteRankFreeModule_abstract`. Its `__classcall_private__` requires a
commutative base ring, defaults to `Modules(ring).FiniteDimensional()`, and
refines field bases to vector spaces.

Parent methods include `basis`, `bases`, `default_basis`, `set_default_basis`,
`print_bases`, `irange`, `change_of_basis`, `set_change_of_basis`,
`tensor_module`, `symmetric_power`, `dual_symmetric_power`, `dual`,
`linear_form`, `alternating_form`, `hom`, `endomorphism`, `identity_map`,
`automorphism`, and `general_linear_group`.

`FiniteRankFreeModuleElement` subclasses `AlternatingContrTensor` and supplies
`_new_comp`, `_new_instance`, and representation helpers.

Caveats:

- The base ring must be commutative.
- Some morphism predicates are only fully implemented for special cases such as
  identity maps.

## Finitely Presented Graded Modules

### Free Graded Modules

Sources:

- `modules/fp_graded/free_module.py:296-1059`
- `modules/fp_graded/free_element.py:1-291`
- `modules/fp_graded/free_morphism.py:27-215`

`FreeGradedModule` subclasses `CombinatorialFreeModule`. Its category is
`GradedModules(algebra).WithBasis().FiniteDimensional()`, and construction
requires the algebra base ring to be a PID.

Parent methods include `generator_degrees`, `generator`, `generators`, `gens`,
`connectivity`, `is_trivial`, `has_relations`, `relations`, `suspension`,
`_element_constructor_`, `an_element`, `basis_elements`,
`element_from_coordinates`, `vector_presentation`, `__getitem__`, and `_Hom_`.

`FreeGradedModuleElement` supplies `dense_coefficient_list`, `degree`,
`lift_to_free`, `_lmul_`, and `vector_presentation`.

`FreeGradedModuleMorphism` supplies `degree`, `__call__`, and `fp_module`.

### Finitely Presented Modules

Sources:

- `modules/fp_graded/module.py:70-1338`
- `modules/fp_graded/element.py:29-345`
- `modules/fp_graded/homspace.py:55-562`
- `modules/fp_graded/morphism.py:420-761`, `:1617-1987`
- `modules/fp_graded/steenrod/module.py`
- `modules/fp_graded/steenrod/morphism.py`

`FPModule` subclasses `UniqueRepresentation`, `IndexedGenerators`, and
`Module`. Its category is `GradedModules(algebra).FinitelyPresented()`.

Parent methods include `defining_homomorphism`, `_free_module`, `relations`,
`relation`, `generator_degrees`, `generators`, `generator`, `_from_dict`,
`_monomial`, `monomial`, `zero`, `_element_constructor_`, `an_element`,
`element_from_coordinates`, `basis_elements`, `vector_presentation`,
`connectivity`, `is_trivial`, `has_relations`, `minimal_presentation`,
`suspension`, `submodule_inclusion`, `resolution`, and `change_ring`.

`FPElement` supplies `lift_to_free`, `degree`, `dense_coefficient_list`,
`_lmul_`, `vector_presentation`, `__bool__`, `__eq__`, and `normalize`.

Caveats:

- The algebra is expected to be connected graded with a graded basis.
- `submodule_inclusion` is implemented for finite-dimensional algebras because
  it relies on `top_class`.
- `resolution` and `minimal_presentation` may need `top_dim` for
  infinite-dimensional algebras.

## Ore Modules

Sources:

- `modules/ore_module.py:316-2206`
- `modules/ore_module_element.py:23-120`
- `modules/ore_module_morphism.py:272-380`, `:512-942`
- `modules/ore_module_homspace.py:27-145`
- `rings/polynomial/ore_polynomial_ring.py:73-1334`

`OrePolynomialRing` subclasses `UniqueRepresentation` and `Parent`. It supplies
`gen`, `gens`, `fraction_field`, `change_var`, `quotient_module`,
`twisting_morphism`, `twisting_derivation`, `random_element`, and
`random_irreducible`. Its `quotient_module(P, names=None)` builds an
`OreModule`.

`OreModule` subclasses `UniqueRepresentation` and `FreeModule_ambient`. Its
`__classcall_private__` normalizes the matrix, twist, and names. Its method
surface includes `_repr_`, `_latex_`, `basis`, `gens`, `gen`, `rename_basis`,
`is_zero`, `module`, `ore_ring`, `twisting_morphism`,
`twisting_derivation`, `matrix`, `pseudohom`, `span`, `quotient`, `quo`,
`_span`, `_Hom_`, `hom`, `multiplication_map`, `identity_morphism`,
`injection_morphism`, `projection_morphism`, `morphism_restriction`,
`morphism_corestriction`, `morphism_quotient`, and `morphism_modulo`.

`OreModuleElement` subclasses `FreeModuleElement_generic_dense` and supplies
representation, LaTeX representation, immutability guards, and hashing.

`OreSubmodule` and `OreQuotientModule` supply inclusion/projection,
relations/cover, and morphism restriction/corestriction behavior.

Caveats:

- `OrePolynomialRing` is univariate.
- Sparse Ore polynomial rings are not implemented.
- With trivial twist, Sage may fall back to an ordinary polynomial ring unless
  `polcast=False`.
- Ore submodule and quotient operations are implemented over fields.
- `OreModule_homspace` requires domain and codomain Ore modules over the same
  Ore ring/twist.

## Ring-Side Module Bridges

### Ring Category Methods

Source: `categories/rings.py:885-1686`.

- `Rings.ParentMethods.__pow__` returns `FreeModule(self, n)` for `R^n` and
  `MatrixSpace(self, m, n)` for `R^(m,n)`.
- `Rings.ParentMethods.free_module` returns a free module over the ring itself;
  the default implementation raises `NotImplementedError` for other bases.
- `Rings.ParentMethods.ideal` constructs ideals using `_ideal_class_`.
- `Rings.ParentMethods.quotient`, `quo`, and `quotient_ring` construct quotient
  rings by two-sided ideals.
- `Rings.ParentMethods.__truediv__` rejects quotient syntax and directs callers
  to `quotient(I)`.
- `Rings.ParentMethods.__getitem__` is the syntax bridge for polynomial rings,
  power series rings, Laurent series, Ore polynomial rings, number fields, and
  orders.

### Ideals As Module-Like Objects

Sources:

- `rings/ideal.py:251-1254`
- `rings/polynomial/laurent_polynomial_ideal.py:30-357`
- `rings/number_field/order_ideal.py:74-157`, `:212`, `:242`, `:740-741`
- `rings/number_field/number_field_ideal.py:302-355`, `:599-729`

`Ideal_generic` supplies `gens`, `gen`, `ngens`, `gens_reduced`, `ring`,
`base_ring`, `apply_morphism`, `reduce`, `category`, `__add__`, `__mul__`,
`__rmul__`, `norm`, `absolute_norm`, `free_resolution`, and
`graded_free_resolution`. Its `category()` returns `Ideals(self.__ring)`.

`LaurentPolynomialIdeal` represents ideals via saturation in the associated
polynomial ring and supplies `hint`, `set_hint`, `_richcmp_`, `__contains__`,
`gens_reduced`, `change_ring`, `base_extend`, `apply_map`, `apply_coeff_map`,
and `toric_coordinate_change`.

`NumberFieldOrderIdeal_generic` constructs a `ZZ`-module by
`O.free_module().submodule(span)` and stores it as `_module`; `free_module()`
returns that module. Its `norm` computes the index in the ambient order module.

`NumberFieldIdeal` and `NumberFieldFractionalIdeal` expose `coordinates`,
`basis`, and `free_module`; `coordinates` uses
`self.free_module().coordinate_vector(...)`.

Caveats:

- `Ideal_generic._contains_`, `primary_decomposition`, `associated_primes`,
  `minimal_associated_primes`, and `absolute_norm` are not implemented in the
  generic class.
- `Ideal_generic.free_resolution` and `graded_free_resolution` only work for
  principal ideals in the generic implementation.
- Number-field order ideals and number-field ideals expose `ZZ`-module
  constructions tied to their order/field representation, not generic
  ring-ideal module constructors.

### Polynomial, Series, And Matrix Rings

Sources:

- `rings/polynomial/polynomial_ring.py:240-860`
- `rings/polynomial/laurent_polynomial_ring_base.py:33-403`
- `rings/power_series_ring.py:493-915`
- `matrix/matrix_space.py:677-924`, `:2333-2414`
- `rings/number_field/order.py:749-850`, `:2024-2043`
- `rings/number_field/number_field.py:9044-9123`

`PolynomialRing_generic` supplies coercion and completion behavior. Its
`_element_constructor_` accepts lists/tuples, power series, Laurent series,
fraction-field elements, PARI elements, strings, and finite-ring elements.
`_coerce_map_from_` and `_coerce_map_from_base_ring` manage compatibility with
base rings and related polynomial rings. `flattening_morphism` flattens
iterated polynomial rings.

`LaurentPolynomialRing_generic` supplies `ngens`, `gens`, `gen`,
`construction`, `completion`, `_coerce_map_from_`, `_is_valid_homomorphism_`,
and `ideal`. Its `completion` returns Laurent-series or lazy Laurent-series
rings.

`PowerSeriesRing_generic` supplies initialization, coercion, element
construction, and construction metadata; it is a complete local/valuation-style
ring rather than a direct module constructor.

`MatrixSpace.__classcall__` returns `Hom(FreeModule(...), FreeModule(...))`
when row/column keys are supplied. `MatrixSpace.__init__` places square matrix
spaces in `Algebras(base_ring.category())`, rectangular matrix spaces in
`Modules(base_ring.category())`, and then adds `WithBasis().FiniteDimensional()`.
`row_space` and `column_space` return free modules over the matrix base ring.
`from_vector` converts vectors into matrix elements.

`Order.free_module` returns the underlying free `ZZ`-module for a number-field
order, and `Order.module` returns the stored module representation. `Order.basis`
and `Order.coordinates` provide integral-basis and coordinate-vector access.

`NumberField.free_module` and `absolute_vector_space` expose number-field vector
or module presentations.

## Negative And Source-Visibility Findings

### Cell-Module Factory

- Searched: `sage/` for `def cell_module` and `cell_module(` in the
  modules-with-basis and representation scope.
- Found: no separate public `cell_module` factory in the searched Sage source;
  the visible entry point is the `CellModule` class in
  `modules/with_basis/cell_module.py`.
- Conclusion: I believe the scoped cell-module entry point is the class
  constructor rather than a standalone factory.
- Confidence: Medium.
- Gaps: Cellular-algebra callers outside the scoped module files were not
  exhaustively inspected.

### Multivariate Polynomial Ring Free-Module Method

- Searched: `rg -n "def (free_module|vector_space|basis_matrix|coordinate_vector|module_morphism|tensor|__pow__)"` under the Sage polynomial-ring sources.
- Found: hits in `multi_polynomial_ideal.py`, `laurent_polynomial.pyx`,
  `infinite_polynomial_ring.py`, and matrix-related polynomial code; no direct
  `free_module` or `vector_space` method on the inspected multivariate
  polynomial ring parents.
- Conclusion: I believe the inspected multivariate polynomial ring parents do
  not themselves advertise a direct free-module constructor.
- Confidence: Medium.
- Gaps: Generated symbols, documentation-only aliases, and every caller outside
  the searched source files were not exhausted.

### Free-Module Element Source Visibility

- Searched: Python import location for `sage.modules.free_module_element`, plus
  structural searches for `class FreeModuleElement`, `class Vector_integer_dense`,
  `class Vector_rational_dense`, `class Vector_modn_dense`, and
  `class Vector_mod2_dense`.
- Found: `sage/modules/free_module_element.cpython-312-x86_64-linux-gnu.so`;
  dense vector classes were visible as dispatcher targets in `free_module.py`
  but not as readable Python source in this install.
- Conclusion: I believe the base free-module element implementation and dense
  vector classes are not source-visible in the installed Python tree.
- Confidence: High.
- Gaps: Upstream Sage `.pyx` sources and generated Cython source were not
  inspected.

### Ore Module Category Source

- Searched: Sage source for `sage/categories/ore_modules.py` and
  `class OreModules` while inspecting `OreModule.__classcall_private__`.
- Found: no source-visible category file or class in the searched installed
  tree, although `OreModule` references an `OreModules(base, twist)` category.
- Conclusion: I believe the category hook is not source-visible in this
  installed tree, or is reached through alias/import indirection not covered by
  the search.
- Confidence: Medium.
- Gaps: Import-resolution tracing and generated/package metadata were not
  exhaustively inspected.
