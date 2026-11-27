# Modules Mapping

This file records the forward target mapping from Sage module surfaces into the local
category-spec hierarchy.

## Constructor Namespace

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| `Modules(R).NamedModules()` | `Modules(R).Constructors()` | Sage constructors create module objects; they are not mathematical subcategories. |
| `FreeModule(R, n)` and `R^n` | `Modules(R).Constructors().FreeModule(n)` refined into `Modules(R).Free()` plus finite-rank and base-ring restrictions | The constructor is concrete; `Free` is an axiomatic restriction attachable to any module subcategory. |
| `CombinatorialFreeModule(R, basis_keys)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys)` refined into `Modules(R).Free()` and `Modules(R).WithOrderedGeneratingSet()` | Combinatorial free modules are a Sage constructor family for free modules with explicit basis keys, not a mathematical subcategory. |
| Plain-set Sage `S.algebra(R)` / `Sets().Algebras(R)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)`, exposed by `S.free_module(R)` | Sage's existing path already constructs the free `R`-module with basis indexed by `S`. The spec routes that Sage source surface here instead of treating it as an algebra constructor. |
| `VectorSpace(K, n)` | `Modules(K).Constructors().VectorSpace(n)` refined into `Modules(K).Free().FiniteRank().OverField()` | Vector spaces are modules over fields with finite-rank structure when the constructor supplies a dimension. |
| Matrix presentations `f: R^m -> R^n` | `Modules(R).from_matrix(M)` delegating to `FinitelyPresentedModulesOverPID.from_matrix` | A matrix presentation defines `coker(f)`. Smith-form and elementary-divisor normalization are specific to finitely presented modules over PIDs, so the constructor namespace delegates to that subcategory owner. |
| `SubmoduleWithBasis`, free-module submodules, vector subspaces | `Modules(R).Subobjects()` / `Submodules` plus ordered-generating-set refinements | In module categories, subobjects are submodules. |
| Quotient modules and FGP modules | `Modules(R).Quotients()` plus finite-presentation/base-ring refinements | Quotients are construction categories attachable to arbitrary module subcategories. |
| Ring objects viewed as modules | `Modules(R).Constructors().RingObjectAsModule(...)` | The ring object supplies the module structure; ring-specific methods remain in `rings`. |

Constructor signatures expose the finite Sage input casework as named methods instead
of mirroring Sage's positional dispatch. The canonical rank constructors stay named
`FreeModule(rank=...)`, `VectorSpace(dimension=...)`, and
`FreeQuadraticModule(rank=..., inner_product_matrix=...)`. The other documented Sage
paths are split into `FreeModuleWithBasisKeys`, `FreeModuleWithoutBasis`,
`FreeModuleWithInnerProductRows`, `FreeModuleWithInnerProductEntries`,
`VectorSpaceWithBasisKeys`, `VectorSpaceWithoutBasis`,
`VectorSpaceWithInnerProductRows`, `VectorSpaceWithInnerProductEntries`,
`FreeQuadraticModuleFromRows`, and `FreeQuadraticModuleFromEntries`. Sage's
`inner_product_ring` path is not public because the installed Sage source immediately
raises `NotImplementedError`.

`FPModule(arg0, ...)` splits into `FPModuleFromPresentation(algebra=...)`,
`FPModuleFromCokernelMap(defining_map=...)`, and
`FPModuleFromFreeGradedModule(module=...)`; `FPModule(algebra, generator_degrees, ...)`
is retained only for the presentation case. `IntegerLattice(basis, ...)` splits into
`IntegerLatticeFromBasisMatrix`, `IntegerLatticeFromBasisRows`, and
`IntegerLatticeFromOrderElement`. `TorsionQuadraticForm(q)` splits into matrix and
row-list routes, with the public Sage-compatible name reserved for the matrix case.
Quotient construction similarly splits Sage's `quotient_module` data shapes into
`quotient_by_submodule`, `quotient_by_generators`,
`quotient_by_relation_matrix`, and `quotient_by_relation_rows`.

Ring-as-module constructors mirror the ring constructor split: polynomial
`var_array` admits only one generator-count integer, power-series construction splits
univariate and multivariate routes, and Laurent/Puiseux series expose explicit
constructors from their underlying power/Laurent series rings. When upstream Sage
implements a surface with `*args` or `**kwds`, the spec does not mirror that plumbing
unless the written Sage documentation proves a genuinely open-ended mathematical input
family.

Integer-valued module data uses `Integer`, not `int | Integer`: ranks, dimensions,
tensor powers, tensor types, start indices, graded generator degrees, polynomial
variable counts, and series precisions. The constructor namespace may pass these values
to Sage factories, but the spec surface records the Sage mathematical type.

Type vocabulary should name mathematical objects, not implementation containers.
Generating sets, coordinate vectors, tensor symmetry data, and element-class hooks are
spelled directly as sequences, module elements, tuples, or element classes unless the
name introduces an independent mathematical noun such as `ModuleBasis` or
`Cardinality`.

Sage's `CombinatorialFreeModule(..., **kwds)` keyword bag is not copied as a project
constructor surface. The admitted constructor data is the basis-key set, optional
element class, optional category refinement, prefix, and names. Remaining Sage
keywords are display/provenance options for `IndexedGenerators` (`bracket`,
`latex_bracket`, `latex_names`, old monomial ordering aliases, `key`, and related
print controls). They are recovered through the Sage parent and its
`print_options(...)` API, not through category constructors; basis/order mathematics is
mapped to the basis and ordered-generating-set surfaces below.

## Tensor Component Duals And Forms

`TensorAlgebraComponents(R).DualObjects()` owns integral forms.  If
`N = T_R(M)[p,q]`, then `N.dual()` is the tensor component `T_R(M)[q,p]`.  The
same object is naturally interpretable as `Hom_R(T_R(M)[p,q], R)`, so the hom
category supplies evaluation behavior rather than a separate form identity.

Use these names consistently:

| Surface | Meaning |
| --- | --- |
| `TensorAlgebraComponents(R).DualObjects()` / `dual()` | The dual-component category, a subcategory of `TensorAlgebraComponents(R)`. |
| `tensor_type()` | The tensor type of the object itself: `(p,q)` on `T_R(M)[p,q]`, `(q,p)` on its dual. |
| `Modules(R).HomCategory().Forms()` | Hom-layer interpretation for evaluation against the original component. |

Thus ordinary linear forms are dual tensor components of type `(0,1)`. Bilinear
forms are dual tensor components of type `(0,2)`.
Multiplication structure tensors are not forms on `T_R(M)[1,2]`; they are tensor
elements of type `(1,2)` constructed in `tensor_algebra_components`.

## Combinatorial Free Module Method Surface

`CombinatorialFreeModule` is not a project category. Its constructor builds a free
module with explicit basis keys, and its methods are evidence for existing or missing
mathematical surfaces. Each inventoried method must map independently.

| Sage method surface | Target surface | Rationale |
| --- | --- | --- |
| `rank()` / `dimension()` | `Modules(R).Free().rank()`; finite cases may also satisfy `Modules(R).Free().FiniteRank().dimension()` | The mathematical invariant is the cardinality of a basis. Sage's `dimension()` is a constructor-family alias for rank, not evidence for a `CombinatorialFreeModules` category. |
| `basis()` and `basis().keys()` | Free module basis data, with key access attached to the ordered/indexed basis surface | A basis is structure on a free module. The basis-key set is part of the chosen basis data, not a separate implementation category. |
| `monomial(i)` / `_monomial(i)` / `term(i, coeff)` | Basis-element and term constructors on a free module with a chosen indexed basis | These construct elements from basis indices and coefficients. They belong to the basis-bearing free-module surface, not to the Sage class name. |
| `_sum_of_monomials(indices)` / `sum_of_terms(terms, distinct=...)` | Finite linear-combination constructors for a basis-bearing free module | These are sparse element constructors from basis terms. They should be exposed only through explicit finite linear-combination vocabulary, not through a constructor-family category. |
| `from_vector(vector, order=..., coerce=...)` | Coordinate conversion for a free module with a chosen ordered basis | The operation depends on an ordered basis and a coordinate vector. It belongs with coordinate-vector conversion, not with the constructor that happened to create the module. |
| `set_order(order)` / `get_order()` / `get_order_key()` / `_order_key(x)` | Ordered-basis or term-order surface refining `Modules(R).WithOrderedGeneratingSet()` | Sage lets the chosen basis order drive coordinate and term operations. The project surface should state this as ordered basis data; private order-key helpers stay interop-local. |
| `change_ring(S)` | `Modules(R)` base-change surface, returning an object in `Modules(S)` with compatible free/basis refinements when valid | Base change is a module operation. The constructor family only supplies one implementation. |
| `zero()` | Additive identity inherited from the module/additive-monoid structure | This is not specific to free modules with basis keys. |
| `sum(iter_of_elements)` / `linear_combination(iter_of_elements_coeff, ...)` | No public category method unless the spec admits finite linear-combination constructors | The module laws already give addition and scalar multiplication. Sage implements parent-side aggregation for speed; that implementation detail is not itself mathematical structure. |
| `_element_constructor_`, `_convert_map_from_`, `_coerce_map_from_`, `_from_dict` | Coercion and element-construction interop | These are Sage parent internals. Public project mappings should expose the mathematical constructors above, not raw dictionary or coercion plumbing. |
| `construction()`, `__classcall_private__`, `__init__`, `element_class`, `_element_class`, representation hooks | Constructor/provenance or Python/Sage implementation internals | These surfaces record how Sage builds and displays the object. They are inventory evidence, but they are not mathematical category methods. |
| `is_exact()` | Exact-arithmetic capability predicate, not a module-category predicate | This belongs to a separate exact-computation policy if admitted. It should not be smuggled into module mathematics. |

Inherited `ModulesWithBasis` methods available on a `CombinatorialFreeModule` follow
the same rule:

| Sage method surface | Target surface | Rationale |
| --- | --- | --- |
| `basis()`, `rank()`, `dimension()`, `cardinality()`, `is_finite()` | Free-module and finite-set/cardinality surfaces | These are invariants of the module and its basis-key set. Finite cardinality belongs to set/enumerated-set structure, not to the Sage constructor family. |
| `gens()`, `gen(i)`, `basis()` iteration | `Modules(R).WithOrderedGeneratingSet()` plus basis-bearing free-module structure | These expose the chosen ordered generators or basis elements. |
| `module_morphism(...)` and hom-on-basis constructors | `Modules(R).HomCategory()` with ordered-basis construction helpers where admitted | A basis-defined map is a module homomorphism construction. The hom category owns the morphism object. |
| `submodule(...)`, `quotient_module(...)`, `intersection(...)` | `Modules(R).Subobjects()`, `Modules(R).Quotients()`, and subobject intersections | These are module subobject and quotient operations. Sage's inheritance from `CombinatorialFreeModule` is only implementation reuse. |
| `tensor(...)` and tensor element helpers | `Modules(R).TensorProducts()` | Tensor products are construction objects, not combinatorial-free-module subcategories. |
| `random_element(...)` | No mathematical category method unless a probability distribution is specified | Random sampling is computational API, not module structure. |
| Element coefficient access: `monomial_coefficients()`, `__getitem__`, `coefficient()`, `items()`, `support()`, `support_of_term()`, `monomials()`, `terms()`, `coefficients()` | Element coordinate/support surface for free modules with a chosen basis | These read the finite support of an element in a basis. They belong to the element surface for basis-bearing free modules. |
| Element predicates and size: `is_zero()`, `__len__()`, `length()` | Module element zero/support-size surfaces where mathematically meaningful | Zero is general module-element structure; support length depends on a chosen basis. |
| Leading/trailing term methods and `map_coefficients`, `map_support`, `map_support_skip_none`, `map_item` | Ordered-basis or term-order element surface; otherwise interop-local | These depend on an order or on implementation-level sparse support traversal. Admit only the mathematically stated ordered-basis cases. |

`CombinatorialFreeModule_Tensor` and `CombinatorialFreeModule_CartesianProduct`
are implementation classes for tensor-product and cartesian-product construction
objects. Their factor accessors and structure maps map to
`Modules(R).TensorProducts()` and `Modules(R).CartesianProducts()`, respectively.
Their representation hooks remain Sage interop.

`SubmoduleWithBasis` and `QuotientModuleWithBasis` inherit from
`CombinatorialFreeModule` in Sage, but their mathematical ownership is subobject and
quotient structure: `Modules(R).Subobjects()` / ordered-generating-set refinements and
`Modules(R).Quotients()` / ordered-generating-set refinements. The inheritance is
implementation evidence only.

Basis-coordinate audit:

| Old or audited surface | Project surface | Rationale |
| --- | --- | --- |
| `Modules(R).WithBasis().linear_combination_of_basis(terms)` | unchanged on `Modules(R).WithBasis().ParentMethods` | A finite sum of indexed basis terms is genuine structure of a module equipped with a specified basis. |
| `Modules(R).WithBasis().cokernel_basis_indices()` | `Modules(R).Quotients().ParentMethods.cokernel_basis_indices()` | These are normal-form basis indices for a quotient/cokernel, not a property of every basis-bearing module. |
| `Modules(R).WithBasis().HomCategory().from_basis_map(f)` | unchanged on `WithBasis().HomCategory().ParentMethods` | A map from basis indices determines a unique module morphism from a basis-bearing domain. The hom object owns the resulting morphism construction. |
| `Modules(R).WithBasis().HomCategory().ElementMethods.on_basis()` | unchanged on `WithBasis().HomCategory().ElementMethods` | This reads the basis-index function determining a basis-defined morphism, so it belongs to the basis-refined hom surface. |

## Sage Wrapper Subcategory Migration Mapping

The old Sage-wrapper files are implementation evidence, not ownership evidence. A
method goes to the weakest mathematical category whose hypotheses make the method
meaningful. Constructor-only Sage families are routed through `Modules(R).Constructors()`
and then refined into those categories.

The mapping below is the phase-one owner table for the wrapper migration.

| Current wrapper | Sage evidence | Constructor owner | Mathematical method owner | Migration result |
| --- | --- | --- | --- | --- |
| `_CombinatorialFreeModules` | `CombinatorialFreeModule` | `Modules(R).Constructors().CombinatorialFreeModule(...)` | `Modules(R).Free()` plus a basis-bearing refinement; ordered APIs refine further to `WithOrderedGeneratingSet()` or an ordered-basis owner | Already deleted. Keep only constructor routing and method mapping. |
| `_FreeModulesWithStandardBasis` | `FreeModule_ambient*` | `FreeModule(R, n)` and `R^n` | finite-rank free modules with a chosen standard ordered basis | Deleted; methods moved to free, ordered-basis, subobject, and quotient owners. |
| `_FiniteRankFreeModules` | tensor-calculus `FiniteRankFreeModule` | `Modules(R).Constructors().FiniteRankFreeModule(...)` | `Modules(R).Free().FiniteRank()` plus tensor, dual, symmetric, exterior, hom, end, and aut construction owners | Deleted; constructor routes directly to `Free().FiniteRank()`. |
| `_FreeModulesOverIntegralDomains` | `FreeModule_generic_domain` | `FreeModule(R, n)` when `R` is an integral domain | `Modules(R).Free().OverIntegralDomain()` and its subobject owner | Deleted; methods moved to integral-domain and subobject owners. |
| `_FreeModulesOverPIDs` | `FreeModule_generic_pid` | `FreeModule(R, n)` when `R` is a PID | `Modules(R).Free().OverPID()`, `Modules(R).Quotients()`, and `FinitelyPresentedModulesOverPID` | Deleted; methods moved to PID and finite-presentation owners. |
| `_VectorSpaces` | `FreeModule_ambient_field` | `VectorSpace(K, n)` and `FreeModule(K, n)` for a field `K` | `Modules(K).OverField().Free().FiniteRank()` plus field-linear subobject and quotient owners | Deleted; methods moved to field/free/subobject/quotient owners. |
| `_RealDoubleVectorSpaces` | `RealDoubleVectorSpace_class` | `VectorSpace(RDF, n)` / `FreeModule(RDF, n)` | the RDF instance of the field-vector-space owner; numeric storage is interop-only | Deleted; coordinates moved to ordered-basis owners. |
| `_ComplexDoubleVectorSpaces` | `ComplexDoubleVectorSpace_class` | `VectorSpace(CDF, n)` / `FreeModule(CDF, n)` | the CDF instance of the field-vector-space owner; numeric storage is interop-only | Deleted; coordinates moved to ordered-basis owners. |
| `_VectorSubspaces` | `FreeModule_submodule_field` | `subspace(...)`, `span(...)`, `V.subspace(...)` | `Modules(K).OverField().Subobjects()` with ambient vector-space structure | Deleted; methods moved to subobject and field-linear owners. |
| `_VectorSubspacesWithOrderedGeneratingSet` | `FreeModule_submodule_with_basis_field` | `subspace_with_basis(...)` | field subobjects with chosen ordered basis/generating set | Deleted; methods moved to ordered-basis subobject owners. |
| `_VectorSpaceQuotients` | `FreeModule_ambient_field_quotient` | `V.quotient_module(W)` for vector spaces | `Modules(K).OverField().Quotients()` | Deleted; methods moved to quotient owners. |
| `_FreeModuleSubmodules` | `FreeModule_submodule_pid` | `M.submodule(...)` for PID free modules | `Modules(R).Free().OverPID().Subobjects()` | Deleted; methods moved to subobject and PID owners. |
| `_FreeModuleSubmodulesWithOrderedGeneratingSet` | `FreeModule_submodule_with_basis_pid` | `M.submodule_with_basis(...)` | PID free subobjects with chosen ordered basis/generating set | Deleted; methods moved to ordered-basis subobject owners. |
| `_SubmodulesWithOrderedGeneratingSet` | `SubmoduleWithBasis` | `M.submodule(...)` for modules with basis | `Modules(R).Subobjects()` refined by basis/ordered-generating-set structure | Deleted; methods moved to subobject and basis owners. |
| `_FreeModuleQuotients` | `QuotientModule_free_ambient` | `M.quotient_module(S)` and `M / S` for free modules | `Modules(R).Free().Quotients()` plus finite-presentation owners when the quotient has PID invariant data | Deleted; methods moved to quotient owners. |
| `_QuotientModulesWithOrderedGeneratingSet` | `QuotientModuleWithBasis` | `M.quotient_module(S)` for modules with basis | `Modules(R).Quotients()` refined by basis/ordered-generating-set structure | Deleted; methods moved to quotient and basis owners. |
| `_FinitelyGeneratedPIDQuotientModules` | `FGP_Module_class` | `FGP_Module(V, W)` and PID quotient syntax | `FinitelyPresentedModulesOverPID`, with torsion and finite refinements as axioms | Deleted; methods moved to `FinitelyPresentedModulesOverPID`. |
| `_FreeQuadraticModules` | `FreeQuadraticModule_*` | `FreeQuadraticModule(R, n, form)` and `QuadraticSpace(K, n, form)` | free modules with bilinear/quadratic form, with PID/field refinements where needed | Deleted; methods moved to forms-owned category surfaces. |
| `_IntegerLattices` | `IntegerLattice` and integral symmetric lattice classes | lattice constructors on `Modules(ZZ).Constructors()` | finite-rank free `ZZ`-modules with symmetric nondegenerate integral bilinear form; algorithmic reduction methods live on the lattice owner | Retained as a real integral-lattice category, not as a Sage-class wrapper. |
| `_TorsionQuadraticModules` | `TorsionQuadraticModule` | `TorsionQuadraticForm(...)` and discriminant-group constructors | finite torsion `ZZ`-modules with bilinear/quadratic form | Moved to `forms`; `Modules(R).TorsionQuadraticModules()` is a compatibility route. |
| `_FreeGradedModules` | `FreeGradedModule` | `FreeGradedModule(algebra, generator_degrees, ...)` | `Modules(A).Graded().Free()` plus basis-bearing refinements | Retained as a real graded-free category surface. |
| `_FinitelyPresentedGradedModules` | `FPModule` | `FPModule(...)` | `Modules(A).Graded().FinitelyPresented()` | Retained as a real graded finitely presented category surface. |
| `_OreModules` | `OreModule`, `OreSubmodule`, `OreQuotientModule` | `OrePolynomialRing(...).quotient_module(P)` and `OreModule(...)` | modules over the relevant Ore-polynomial algebra or a stated semilinear-operator category; coefficient-ring free-module behavior remains inherited | Retained as a real Ore-module category surface. |
| `_RepresentationModules` | `Representation_abstract` and subclasses | semigroup/group representation constructors | modules with an action of a specified semigroup/group/monoid and side | Retained as a real representation-module category surface. |
| `_RingObjectsAsModules` | ring objects exposing module structure | forgetful/constructor bridge from ring or algebra objects | ring methods stay in `rings`; module generators and structure maps live on a forgetful construction or objects-over/under surface | Retained as a real ring-object-as-module category surface. |

### Required Immediate Category Owners

The migration needs these mathematical owners before constructors are fully rewired:

| Owner | Role |
| --- | --- |
| `Modules(R).WithBasis()` | Modules equipped with a specified basis. This is the owner for `basis`, basis-key access, monomial/term constructors, support in a basis, and basis-defined morphisms. |
| `Modules(R).WithOrderedBasis()` | Basis-bearing modules whose basis has a specified order. This refines `WithBasis()` and `WithOrderedGeneratingSet()` and owns coordinate vectors, ordered support, leading/trailing term operations, and basis matrices whose row order is meaningful. |
| `C.WithBasis().Subobjects()` / `C.WithOrderedBasis().Subobjects()` | Subobjects equipped with chosen bases or ordered bases, including `SubmoduleWithBasis`, vector subspaces with basis, and PID free submodules with user bases. The construction order uses Sage's covariant machinery so these categories are automatically subcategories of both `C.Subobjects()` and the corresponding basis-bearing category. |
| `C.WithBasis().Quotients()` / `C.WithOrderedBasis().Quotients()` | Quotients equipped with chosen normal-form bases, including `QuotientModuleWithBasis`. The construction order keeps quotient structure functorial over the basis-bearing parent category. |
| `Modules(R).Free().FiniteRank().OverField()` | The vector-space owner for finite-dimensional vector spaces over a field. |
| `Modules(R).Free().OverIntegralDomain()` | The owner for free-module operations requiring an integral domain, including intersection and saturation. |
| `Modules(R).Free().OverPID()` | The owner for free-module operations requiring a PID, including quotient construction and index computations. |
| `FormedModules(R).Bilinear()` / `Modules(R).WithForms().Bilinear()` | Modules equipped with a bilinear form; the class lives in `forms`. |
| `FormedModules(R).Quadratic()` / `Modules(R).WithForms().Quadratic()` | Modules equipped with a quadratic form; the class lives in `forms`. |
| `C.AutCategory().Of(M)` for a form-bearing module category `C` | The orthogonal group of `(M, form)`: automorphisms of `M` in `C`, equivalently module automorphisms that preserve the form. This owner covers integral lattices, rational formed modules, degenerate formed modules, and finite discriminant forms. |
| `Modules(ZZ).Free().FiniteRank().WithForms().Bilinear().Integral().Nondegenerate()` | The forms-owned ambient chain for integral lattices; `lattices` adds the named `Lattice` endpoint. |
| `FinitelyPresentedModulesOverPID(...).Torsion().WithForms().Quadratic()` | The forms-owned finite quadratic module owner for torsion quadratic modules and discriminant groups. |
| `Modules(A).Graded().Free()` | Free graded modules over a graded algebra `A`. |
| `Modules(A).Graded().FinitelyPresented()` | Finitely presented graded modules over a graded algebra `A`. |
| `Modules(R).WithAction(S, side)` | Representation modules: modules over `R` equipped with a specified action of `S` on the given side. |
| `Modules(R).WithOreOperator(...)` or `Modules(OreAlgebra).FiniteRankFree()` | Ore modules, depending on whether the admitted mathematical owner is semilinear-operator data or modules over the Ore algebra. |

### Method Ownership Rules

The same Sage implementation class can expose methods owned by several mathematical
categories. The migration should use these rules before placing any method:

| Method group | Mathematical owner |
| --- | --- |
| `rank`, `dimension`, basis cardinality | `Modules(R).Free()` for rank as basis cardinality; finite-dimensional aliases belong to finite-rank or field-vector owners. |
| `basis`, `basis().keys()`, `monomial`, `term`, `from_vector`, `linear_combination_of_basis` | `WithBasis()`; ordered coordinate variants belong to `WithOrderedBasis()`. |
| `gens`, `gen`, `ngens` | `WithOrderedGeneratingSet()` unless the methods assert basis coordinates, in which case `WithOrderedBasis()`. |
| element `list`, `vector`, `support`, coefficient lookup, leading/trailing term methods | basis or ordered-basis element surfaces; not generic module elements. |
| `degree`, coordinate-ring bookkeeping, dense/sparse conversion, representation hooks, `_sympy_`, `_magma_init_`, `_macaulay2_` | interop or representation details unless a mathematical invariant is explicitly stated. |
| `linear_combination`, parent `sum`, random elements | generic computational helpers; no public category method unless the spec states finite-linear-combination or probability-distribution structure. |
| `submodule`, `submodule_with_basis`, `span`, `zero_submodule`, submodule comparison | `Subobjects()` refined by free, field, PID, basis, or ordered-basis hypotheses as required. |
| `intersection`, `saturation`, `denominator`, `index_in` | free modules over integral domains/PIDs and their subobject owners. |
| `quotient_module`, `__truediv__`, `quotient_abstract`, quotient matrices | `Quotients()` refined by field, free, PID, finite-presentation, basis, or ordered-basis hypotheses. |
| `cover`, `relations`, `free_cover`, `free_relations`, `quotient_map`, `lift_map`, `lift`, `retract` | quotient or subquotient construction owners; `lift`/`retract` for submodules belong to `Subobjects()`. |
| `cokernel_basis_indices` | quotient owners with basis or PID normal-form hypotheses. |
| Smith-form data, `invariant_factors`, `invariants`, `smith_form_gens`, `free_part`, `torsion_part`, `annihilator`, element order | `FinitelyPresentedModulesOverPID` and its torsion/finite refinements. |
| `hom`, `_Hom_`, `module_morphism`, morphism from basis/images/matrices, `on_basis` | the relevant `HomCategory()`; basis-defined constructors refine through `WithBasis().HomCategory()`. |
| `tensor`, `tensor_module`, tensor constructors, tensor factors | `TensorProducts()` and tensor-power construction owners. |
| `dual`, `linear_form`, `alternating_form`, symmetric and exterior powers | `DualObjects()` or the appropriate symmetric/exterior construction owner over finite-rank free modules. |
| `determinant`, `discriminant`, `gram_matrix`, `inner_product_matrix`, `inner_product`, quadratic product | forms-owned bilinear/quadratic module owners. |
| `is_symmetric`, `is_alternating`, `is_nondegenerate`, `is_integral`, `is_even` | forms-owned axiom owners, not constructor wrappers. |
| lattice reduction and enumeration: `LLL`, `BKZ`, `HKZ`, `shortest_vector`, `voronoi_cell`, `closest_vector`, `babai` | integral-lattice algorithm surface, not generic modules or generic free modules. |
| lattice constructions: `dual_lattice`, `discriminant_group`, `orthogonal_complement`, `overlattice`, `genus` | integral-lattice and finite-quadratic-module owners. |
| `orthogonal_group` / `automorphisms` for a formed module `(M, b)` or `(M, q)` | `C.AutCategory().Of(M)` where `C` is the relevant forms-owned category. The group is `Aut_C(M)`, not a generic Sage group anchor. Lattice and discriminant-form orthogonal groups are specializations of this aut surface; matrix-group, finite-generation, and finite-presentation realizations are later refinements. |
| graded data: `generator_degrees`, homogeneous `basis`, `degree`, `connectivity`, `suspension`, `minimal_presentation`, `resolution` | graded free or graded finitely presented owners. |
| Ore data: `ore_ring`, `twisting_morphism`, `twisting_derivation`, `pseudohom`, Ore matrix, morphism restriction/corestriction/quotient | Ore-algebra or semilinear-operator owner; ordinary free-module operations remain inherited from free finite-rank modules. |
| representation data: `semigroup`, `side`, `representation_matrix`, `character`, invariant/twisted invariant modules, subrepresentation, quotient representation, tensor/exterior/symmetric/Schur functors | parameterized representation-module owner and its subobject, quotient, tensor, exterior, symmetric, and Schur construction owners. |
| ring-as-module data: `structure_ring`, `structure_map`, `module_generators` | forgetful construction from rings/algebras to modules or objects-over/under structure; ring operations remain in `rings`. |

## Axiomatic Restrictions

`Free`, `Torsion`, `Torsionfree`, `Projective`, `FinitelyGenerated`,
`FinitelyPresented`, and base-ring restrictions are axiomatic restrictions. They must be
attachable to any subcategory `C` of `Modules(R)` through `C.<Axiom>()`. More concrete
categories, such as finitely generated free modules over a PID, can be implementation
targets only when the additional hypotheses make a real algorithmic surface possible.

## Construction Layout

| Current source surface | Target file organization |
| --- | --- |
| Former construction aggregator | `subcategories/constructions/subobjects.py`, `subquotients.py`, `quotients.py`, `isomorphic_objects.py`, `tensor_products.py`, `cartesian_products.py`, and `dual_objects.py`. |
| Axiomatic module restrictions | One mathematical file per axiomatic subcategory under `subcategories/`. |
| Sage-backed module family surface | Constructor namespace plus mathematical subcategory files only where the family expresses a genuine category restriction. Constructor-only Sage families refine into existing module categories. |

## Construction-Category Mapping

| Sage surface | Target surface | Rationale |
| --- | --- | --- |
| `Modules(R).Homsets()` | `Modules(R).HomCategory()` in `modules/homsets.py` and top-level `homsets/` | Module hom categories have objects `Hom_R(M, N)`, the sets of `R`-linear maps. Sage makes those hom objects modules over `R` and gives the parent method `zero()`. |
| `Modules(R).Endsets()` / `Modules(R).Homsets().Endset()` | `Modules(R).EndCategory()` plus generic `Modules(R).HomCategory().EndCategory()` | Module end categories have objects `End_R(M) = Hom_R(M, M)`. Sage's `Modules.Homsets.Endset` adds magmatic-algebra structure over `R`, so the project declares `End_R(M)` as an `R`-algebra in addition to the generic end-category structure. |
| Sage/project automorphism surfaces | `Modules(R).AutCategory()` with module specialization | `Aut_R(M)` is the invertible part of `End_R(M)`. The root hom category layer owns the aut-category construction; `modules/homsets.py` declares only module-specific names and extra structure. |
| Orthogonal groups of modules with forms | `C.AutCategory().Of(M)` for `C <= FormedModules(R)` | `O(M,b)` is the automorphism group in the category of modules carrying the form. `Modules(R).WithForms()` remains the Sage-compatible spelling, but `forms` owns the category surface. This definition does not require nondegeneracy or a matrix realization; those hypotheses only refine algorithms and concrete presentations. |
| `Modules(R).CartesianProducts()` | `subcategories/constructions/cartesian_products.py` | Cartesian products of modules are direct products with componentwise module operations and common base-ring bookkeeping. |
| `Modules(R).TensorProducts()` | `subcategories/constructions/tensor_products.py` | Tensor products are functorial constructions with `tensor_factors()` and construction data. |
| `Modules(R).DualObjects()` / `dual()` | `subcategories/constructions/dual_objects.py` | Linear duals are covariant functorial construction objects in Sage; graded duals are not separated by the Sage `DualObjects` category. |
| `Modules(R).Subquotients()` | `subcategories/constructions/subquotients.py` | Constructive module subquotients have an ambient module, lift, and retract. Submodules and quotient modules refine this surface. |
| `Modules(R).Subobjects()` / `Submodules` | `subcategories/constructions/subobjects.py` | Subobjects in module categories are submodules. Method signatures should use `Submodule`, not bare `Module`. |
| `Modules(R).Quotients()` | `subcategories/constructions/quotients.py` | Quotient modules are modules modulo submodules and should refine `Subquotients`. |
| `Modules(R).IsomorphicObjects()` | `subcategories/constructions/isomorphic_objects.py` | Transport of module structure along an isomorphism is simultaneously subobject-like and quotient-like in Sage's construction hierarchy. |
| `Modules(R).Graded()` | `subcategories/graded.py` | A graded module is an attachable restriction/construction on any module subcategory. Concrete FP graded modules remain constructor-family objects, not the definition of all graded modules. |
| `Modules(R).Filtered()` | `subcategories/filtered.py` | Filtered modules are attachable restrictions/constructions on module subcategories. Sage notes interaction with `WithBasis`; the project mapping keeps it as its own mathematical file. |
| `Modules(R).FiniteDimensional()` | `subcategories/finite_dimensional.py` | Finite-dimensionality is an axiomatic restriction. Over finite base rings, Sage adds finite-set structure. |
| `Modules(R).FinitelyPresented()` | `subcategories/finitely_presented.py` | Finitely presented modules are an axiomatic restriction. Concrete finitely presented graded/PID modules are implementation families under the constructor namespace. |

For `Modules(R).ObjectsOver(M)` and `Modules(R).ObjectsUnder(M)`, the module subtree
owns `structure_module()` and the module morphism `structure_map()`. The old local
`structure_domain()` and `structure_codomain()` methods move to the Cat-owned universal
structure-morphism surface via `structure_morphism().domain()` and
`structure_morphism().codomain()`.

## Hom-Category Extra-Structure Decision

`R-Mod` is the first concrete model for hom/end/aut extra structure. The generic layer
declares that `Modules(R).HomCategory()`, `Modules(R).EndCategory()`, and
`Modules(R).AutCategory()` have objects `Hom_R(M, N)`, `End_R(M)`, and `Aut_R(M)`.
The module subtree additionally declares that `Hom_R(M, N)` is an `R`-module and
`End_R(M)` is an object of `Algebras(R)`, retaining Sage's `MagmaticAlgebras(R)`
supercategory for upstream compatibility. Aut-category construction still comes from
the generic layer because `Aut_R(M)` is defined by invertibility inside `End_R(M)` and
dispatched through the module end category.

## Topological Modules

Topological module structure should inherit the topological-space surface from
`topological_spaces`, the module surface from `modules`, and any ring topology from
`rings`. It should not duplicate topological-space methods locally.
