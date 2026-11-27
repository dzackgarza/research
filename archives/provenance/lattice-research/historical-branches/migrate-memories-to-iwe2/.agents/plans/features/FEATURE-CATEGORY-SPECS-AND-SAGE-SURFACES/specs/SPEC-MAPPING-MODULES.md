---
id: SPEC-MAPPING-MODULES
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track modules mapping spec
status: complete
priority: critical
requirement: Convert category_specs/modules/docs/MAPPING.md into a tracked spec surface and
  audit it for Sage-source completeness, mathematical correctness, and well-typed module,
  subobject, quotient, tensor, dual, basis, and constructor signatures.
acceptanceCriteria:
- Source paths category_specs/modules/docs/MAPPING.md and category_specs/modules/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return object,
  and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 90
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
constructorNameInventories:
- owner: category_specs.modules.Modules._Constructors
  sageConstructorNames:
  - CombinatorialFreeModule
  - FiniteRankFreeModule
  - FPModule
  - FreeGradedModule
  - FreeModule
  - FreeQuadraticModule
  - IntegerLattice
  - OreQuotientModule
  - span
  - TorsionQuadraticForm
  - VectorSpace
  projectOwnedConstructionNames:
  - ideal_as_submodule
  - invertible_ideal_as_projective_submodule
  - laurent_series_ring_as_module
  - matrix_ring_as_module
  - multivariate_power_series_ring_as_module
  - multivariate_power_series_ring_with_generator_prefix_as_module
  - polynomial_ring_as_module
  - power_series_ring_as_module
  - puiseux_series_ring_as_module
  - quotient_module
  - quotient_of_free_modules
  - rank_one_module_with_ring_isomorphisms
  - ring_as_rank_one_module
---
# Modules Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/modules/docs/MAPPING.md`.

Source inventory: `category_specs/modules/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and category-obligation example-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/modules/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage`
  - `sage/modules/free_module.py`
  - `sage/modules/free_quadratic_module.py`
  - `sage/combinat/free_module.py`
  - `sage/modules/with_basis/subquotient.py`
  - `sage/modules/with_basis/representation.py`
  - `sage/categories/semigroups.py`
  - `sage/modules/fg_pid/fgp_module.py`
  - `sage/modules/free_module_integer.py`
  - `sage/modules/free_quadratic_module_integer_symmetric.py`
  - `sage/modules/torsion_quadratic_module.py`
  - `sage/tensor/modules/finite_rank_free_module.py`
  - `sage/modules/fp_graded/free_module.py`
  - `sage/modules/fp_graded/module.py`
  - `sage/rings/polynomial/ore_polynomial_ring.py`
  - `sage/modules/ore_module.py`
  - `sage/categories/rings.py`
  - `sage/categories/modules.py`
  - `sage/categories/modules_with_basis.py`
  - `sage/modules/free_module_homspace.py`
  - `sage/modules/free_module_morphism.py`
  - `sage/modules/matrix_morphism.py`
  - `sage/modules/fg_pid/fgp_morphism.py`
  - `sage/tensor/modules/free_module_homset.py`
  - `sage/tensor/modules/free_module_morphism.py`
  - `sage/modules/fp_graded/free_homspace.py`
  - `sage/modules/fp_graded/homspace.py`
  - `sage/modules/fp_graded/morphism.py`
  - `sage/modules/ore_module_homspace.py`
  - `sage/modules/ore_module_morphism.py`
  - `sage/geometry/toric_lattice.py`
  - `sage/geometry/toric_lattice_element.pyx`
  - additional installed source paths listed in `category_specs/modules/docs/SAGE_INVENTORY.md` beyond this ledger limit: 21
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the Modules
  source reconciliation is recorded below, with remaining gaps routed through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Source Reconciliation Against Installed Sage 10.7

This reconciliation compares the local inventory with installed Sage source under
`/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage`. It records
surfaces that were missing, inherited, or easy to mis-own in the converted mapping.
Ownership follows the caller object/category. The category of an output object is
codomain data and does not by itself own the method.

### Reconciled Category And Constructor Surfaces

| Sage surface checked | Source evidence | Mapping outcome |
| --- | --- | --- |
| `Modules(R).__classcall_private__(base_ring)` dispatching fields to vector spaces | `categories/modules.py:120-152` | Runtime dispatch. The project owner remains `Modules(R)`; vector-space output for field bases is a refinement/codomain consequence. |
| `Modules(R).FiniteDimensional()`, `.FinitelyPresented()`, `.Filtered()`, `.Graded()`, `.WithBasis()` | `categories/modules.py:342-493` | Axiomatic or construction restrictions on `Modules(R)`. They are inherited owners for module methods satisfying their hypotheses, not constructor families. |
| `Modules(R).TensorProducts()`, `.DualObjects()`, `.CartesianProducts()`, `.Subquotients()`, `.Subobjects()`, `.Quotients()`, `.IsomorphicObjects()` | `categories/modules.py:246-264`, `:836-980`, inherited construction-category machinery | Construction categories. Methods called on a module, subobject, quotient, tensor product, or dual object stay on that caller surface; the constructed object's category is codomain data. |
| `Modules(R).Homsets()` and `Modules(R).Endsets()` | `categories/modules.py:724-820` | `Modules(R).HomCategory()` and `Modules(R).EndCategory()`. The hom object owns `base_ring()` and `zero()`; module end objects additionally carry algebra structure over `R`. |
| `FreeModule(R, ...)`, `VectorSpace(K, ...)`, `span(...)`, `FreeQuadraticModule(R, ...)`, `QuadraticSpace(K, ...)` | `modules/free_module.py:311-804`, `modules/free_quadratic_module.py:86-220` | Constructor namespace entries on `Modules(R).Constructors()` or the relevant forms-owned constructor route. Positional Sage dispatch remains split into named non-variadic project constructors. |
| `R^n`, `R^(m,n)`, and `R.free_module(...)` | `categories/rings.py:885-906`, `:1622-1686` | Ring-side bridge into module constructors. The ring method is source evidence for preserving Sage syntax; module structure is owned by `Modules(R).Free().FiniteRank()` or by matrix-space module-with-basis structure. |
| `OrePolynomialRing(...).quotient_module(P)` and `OreModule.__classcall_private__` | `rings/polynomial/ore_polynomial_ring.py:1255`, `modules/ore_module.py:322-357`, `categories/ore_modules.py:9-174` | Constructor route into Sage's `OreModules(base, twist)` category. Project ownership remains deferred between a semilinear-operator module owner and a module-over-Ore-algebra owner until the Ore decision is recorded. |
| `FiniteDimensionalAlgebrasWithBasis.ParentMethods.cell_module(mu, **kwds)` | `categories/finite_dimensional_algebras_with_basis.py:1499-1653`, `modules/with_basis/cell_module.py:23-393` | Algebra-side constructor for a cell module. The module object maps to representation/cellular-module owners; the constructor is not owned by generic `Modules(R)`. |

### Modules Homset Mirroring Audit

The module subtree does not inherit Sage's generic homset surface as an
unexamined contract. Sage homset and concrete homspace methods are retained only
where the method belongs to a module hom object, module morphism element,
endomorphism object, or automorphism object in the project-owned Hom/End/Aut
vocabulary.

| Sage source surface | Source evidence | Project owner and outcome |
| --- | --- | --- |
| `Modules(R).Homsets().base_ring()` and homset parent `base_ring()` | `sage/categories/modules.py:724-785` | Retained on `Modules(R).HomCategory()` objects. The base ring is part of the `R`-linear hom object structure, not a separate constructor family. |
| `Modules(R).Homsets().ParentMethods.zero()` | `sage/categories/modules.py:786-818`; `sage/modules/free_module_homspace.py:230-275` | Retained on `Modules(R).HomCategory().ParentMethods.zero()`. The result is the zero `R`-linear morphism `M -> N`; concrete free homspaces may realize it by a zero matrix or constant-zero function. |
| Concrete homspace `__call__` from matrices, generator images, or callables | `sage/modules/free_module_homspace.py:132-229`; inventory `category_specs/modules/docs/SAGE_INVENTORY.md` homspaces section | Retained as hom-object constructors under `Modules(R).HomCategory()`, with basis-defined cases refined through `Modules(R).WithBasis().HomCategory()`. Coercion convenience is backend interop unless the source data states an `R`-linear map under the required base-ring/coercion hypotheses. |
| Concrete homspace `_matrix_space()` and `basis()` | `sage/modules/free_module_homspace.py:276-341`; finite/free homspace inventory rows | Retained only under finite-rank free or basis-bearing hom objects. They are not generic `Modules(R).HomCategory()` methods unless a finite presented basis or matrix-space hypothesis is part of the object. |
| Concrete homspace `identity()` and generic homset `identity()` / `one()` | `sage/modules/free_module_homspace.py:342-368`; `sage/categories/homset.py:1161-1204` | Routed through endomorphism ownership: `Modules(R).EndCategory().ParentMethods` for identity of `End_R(M)`, with generic Hom identity/one inherited only through the project root Hom/End vocabulary. For non-end hom objects, Sage's `natural_map()` remains generic homset interop, not a module-specific method. |
| Generic homset `domain()`, `codomain()`, `reversed()`, `natural_map()` and homset-category `is_endomorphism_set()` | `sage/categories/homset.py:1136-1249`; `sage/categories/homsets.py:330-355` | Routed to the generic project homset semantic base and the generic endset predicate. The Modules mapping relies on these only as Hom/End infrastructure, not as evidence for module-specific methods. |
| `Modules(R).Homsets().Endset.extra_super_categories()` | `sage/categories/modules.py:819-848` | Retained on `Modules(R).EndCategory()`: `End_R(M)` is an `R`-algebra, with Sage's magmatic-algebra supercategory preserved as implementation compatibility evidence. |
| Morphism matrix/rank/kernel/image/inverse/restriction and injective/surjective/bijective predicates | `sage/modules/matrix_morphism.py:312-339`, `:863-1076`, `:1322-1677`; `sage/modules/free_module_morphism.py:247-693` | Retained on `Modules(R).HomCategory().ElementMethods` or end/aut refinements under the source hypotheses. Kernel, image, and inverse-image outputs are subobjects/codomain data; they do not own the caller method. |
| Automorphism construction and recognition through invertible endomorphisms, `general_linear_group()`, and form/lattice `orthogonal_group()` methods | `category_specs/modules/docs/SAGE_INVENTORY.md`; negative finding below for absent `Modules(R).Autsets()` | Routed to `Modules(R).AutCategory().Of(M)` or `C.AutCategory().Of(M)` for form-preserving categories `C`. Sage automorphism classes and groups are implementation witnesses; they are not a separate module-category construction surface. |

### Reconciled Method Ownership

| Sage method or inherited surface | Highest correct owner | Classification and notes |
| --- | --- | --- |
| `base_ring`, `zero`, additive/scalar operations, `linear_combination` | `Modules(R)` or the relevant `Modules(R).HomCategory()` object when called on a homset | Admitted only as module or hom-object structure. Parent aggregation is not a separate constructor surface. |
| `tensor_square`, `tensor`, `tensor_module`, `tensor_factors`, tensor element `apply_multilinear_morphism` | `Modules(R).TensorProducts()` with `WithBasis()` refinements when basis tensor APIs are used | Tensor-product construction and tensor-product object methods. Representation tensor products refine through representation-module owners. |
| `dual`, `linear_form`, `alternating_form`, `dual_symmetric_power`, `dual_exterior_power` | `Modules(R).DualObjects()` and `Modules(R).HomCategory()` for `Hom_R(M, R)` content; exterior/symmetric owners require finite-rank/free/projective hypotheses | The caller is the module whose dual or tensor construction is being formed. Ordinary linear duals are not forms-owned shortcuts. |
| `basis`, `bases`, `default_basis`, `set_default_basis`, `basis_matrix`, `coordinate_vector`, `coordinates`, `from_vector`, `element_from_coordinates` | `Modules(R).WithBasis()` and `Modules(R).WithOrderedBasis()` where row/order data is meaningful | Basis and coordinate surfaces. Sage state mutation such as `set_default_basis` is interop unless represented as a new presented object plus change-of-basis morphism. |
| `gens`, `gen`, `ngens`, `generator`, `generators`, `generator_degrees` | `WithOrderedGeneratingSet()` or graded-free/finitely-presented graded owners when degrees are part of the structure | Generator access is not evidence for a constructor-family category. Graded degree data stays on graded module surfaces. |
| `monomial`, `term`, `sum_of_monomials`, `sum_of_terms`, `_from_dict`, coefficient/support element methods | `Modules(R).WithBasis().ElementMethods`; ordered leading/trailing methods refine to ordered-basis or term-order owners | Public element construction/readback only when stated as basis-coordinate mathematics. Raw dictionary and private helpers are interop/private. |
| `submodule`, `submodule_with_basis`, `span`, `zero_submodule`, subspace constructors, `ambient`, `lift`, `retract`, `reduce` | `Modules(R).Subobjects()` with `WithBasis()`, `WithOrderedBasis()`, field, PID, or Ore refinements as required | The caller is the ambient module or subobject. Output submodule category is codomain data. |
| `intersection`, `saturation`, `denominator`, `index_in`, `index_in_saturation`, `ambient_vector_space`, `vector_space_span` | Common-ambient subobject owners with integral-domain, PID, or field hypotheses | Admitted only under the algebraic hypotheses in Sage source. Ambient/vector-space conversion is interop unless expressed as scalar extension or subobject data. |
| `quotient`, `quotient_module`, `quotient_abstract`, `__truediv__`, `cover`, `relations`, `free_cover`, `free_relations`, `quotient_map`, `lift_map`, `cokernel_basis_indices` | `Modules(R).Quotients()` and `Modules(R).Subquotients()`, with finite-presentation, PID, field, or basis refinements | The caller is the ambient module, quotient object, or quotient morphism. Quotient normal forms belong to quotient owners, not general basis-bearing modules. |
| `hom`, `_Hom_`, `module_morphism`, `homspace.__call__`, homspace `basis`, `identity`, `zero`, basis-map `on_basis` | `Modules(R).HomCategory()`; `WithBasis().HomCategory()` owns basis-defined constructors | Matrix/image/function constructors are hom-object constructors. Endomorphism specializations refine through `EndCategory()`. |
| Morphism `matrix`, `rank`, `nullity`, `kernel`, `image`, `inverse_image`, `lift`, `restrict_domain`, `restrict_codomain`, `restrict`, injective/surjective/bijective predicates | `Modules(R).HomCategory().ElementMethods`, with field/PID/Ore/graded hypotheses where Sage algorithms require them | These are methods on morphisms. Kernel and image output subobjects are codomain data, not method owners. |
| `inverse`, `side`, `side_switch`, hom arithmetic, `is_identity`, `is_zero`, `is_equal_function` | Hom/end/aut element surfaces | Invertibility promotes membership in the aut surface but does not move the caller-owned method off the morphism/end object. |
| `general_linear_group`, `automorphism`, finite-rank `FreeModuleAutomorphism`, tensor-calculus endomorphism determinant/trace/characteristic polynomial | `Modules(R).AutCategory().Of(M)` and `Modules(R).EndCategory().Of(M)` with finite-rank/free hypotheses | Sage tensor-calculus automorphism classes are implementation witnesses for `Aut_R(M)`, not a separate module family owner. |
| `orthogonal_group` and `automorphisms` on integral lattices or torsion quadratic modules | `C.AutCategory().Of(M)` for the relevant forms-owned category `C` | Orthogonal groups are automorphism objects in a form-preserving category. Lattice/discriminant-form presentations refine the implementation. |
| `determinant`, `discriminant`, `gram_matrix`, `inner_product_matrix`, `_inner_product_is_dot_product`, `_inner_product_is_diagonal`, `inner_product`, `quadratic_product`, `brown_invariant`, `value_module`, `value_module_qf` | Forms-owned bilinear/quadratic module owners | `inner_product_matrix` is Sage wording; public project spelling should be form/Gram/codomain vocabulary. Private diagonal/dot-product helpers stay interop. |
| `dual_lattice`, `discriminant_group`, `signature`, `signature_pair`, `is_even`, `is_primitive`, `orthogonal_complement`, `sublattice`, `overlattice`, `maximal_overlattice`, `genus`, `twist` | Integral-lattice and finite quadratic module owners under forms | Lattice-specific surfaces. They must not be generalized to all modules merely because Sage classes subclass free modules. |
| `LLL`, `BKZ`, `HKZ`, `reduced_basis`, `shortest_vector`, `short_vectors`, `enumerate_short_vectors`, `enumerate_close_vectors`, `voronoi_cell`, `closest_vector`, `babai`, `minimum`, `maximum` | Integral-lattice algorithm surfaces | Algorithmic lattice surfaces. Definite/optional-package limits are implementation caveats, not reasons to weaken the lattice spec. |
| `invariants`, `smith_form_gens`, `gens_to_smith`, `smith_to_gens`, `annihilator`, `additive_order`, finite iteration/list/cardinality | `FinitelyPresentedModulesOverPID` with torsion/finite refinements where applicable | Smith normal form and finite enumeration are PID finite-presentation structure. Element order belongs to torsion/finite PID-module element surfaces. |
| `connectivity`, `suspension`, `minimal_presentation`, `resolution`, `submodule_inclusion`, graded morphism `solve`, `split`, `homology` | `Modules(A).Graded().Free()` or `Modules(A).Graded().FinitelyPresented()` and their hom/subobject/quotient owners | Graded algorithms stay graded; morphism-level algorithms stay on graded hom elements. |
| `semigroup`, `side`, `representation_matrix`, `character`, `brauer_character`, invariant/twisted invariant modules, composition series/factors, Schur/exterior/symmetric representation functors | `Modules(R).WithAction(S, side)` and its representation subobject, quotient, tensor, exterior, symmetric, and Schur construction owners | Representation structure is a module with action. Semigroup/group caller constructors are source evidence for constructor routing only. |
| `cellular_algebra`, `bilinear_form`, `bilinear_form_matrix`, `radical`, `simple_module` on `CellModule` | Deferred cellular-module owner under finite-dimensional algebras with basis, with forms and quotient-module refinements for the bilinear/radical/simple-module surfaces | Not generic module ownership. The caller is a cell module; the constructing caller is the cellular algebra. |
| `ore_ring`, `twisting_morphism`, `twisting_derivation`, `pseudohom`, `multiplication_map`, Ore submodule/quotient morphism restriction/corestriction/quotient/modulo | Deferred Ore owner, plus ordinary inherited free-module, hom, subobject, and quotient surfaces | `categories/ore_modules.py` is present in installed Sage; project naming still needs a decision between semilinear-operator and Ore-algebra ownership. |
| `is_sparse`, `is_dense`, `is_exact`, `some_elements`, `random_element`, `dense_module`, `sparse_module`, `element_class`, display hooks, `_sympy_`, `_magma_init_`, `_macaulay2_`, `_repr_`, `_latex_` | Private/runtime/display/interop | Not public mathematical category surfaces unless a later spec introduces exact-computation or probability-distribution structure with explicit hypotheses. |

### Toric Character-Lattice Corrective Mapping

Sage's `sage.geometry.toric_lattice.ToricLattice` is implementation evidence for
presented coordinate-character and cocharacter lattices, not evidence for a separate
toric-lattice owner. `ToricLattice_generic` subclasses Sage PID free-module classes,
and its distinctive behavior is parent identity, naming, conversion barriers between
distinct lattices, and convenient toric notation for a lattice and its dual. For a
presented coordinate torus, the coordinate characters give a selected basis; with the
identity Gram matrix this is a unimodular formed lattice. The mathematical methods
exposed there must be mapped to the highest ordinary module, basis, or formed-lattice
owner:

| Sage toric surface | Project owner | Mapping consequence |
| --- | --- | --- |
| `ToricLattice(rank, name, dual_name, ...)` | `Modules(ZZ).Constructors().FreeModule(rank)` plus selected-basis and identity-formed-lattice surfaces when the coordinate-character presentation is part of the object | The toric constructor witnesses that named finite-rank free abelian lattices must be expressible without collapsing distinct parents into `ZZ^n`. For coordinate characters, the selected basis supplies the identity Gram form, so the object also lies in the unimodular lattice surface. The names `M` and `N` are notation/provenance, not a subcategory. |
| `ToricLattice.dual()` | `Modules(ZZ).DualObjects()` plus the metric `dual_lattice()` compatibility path for the identity-formed presentation | The module dual `Hom_ZZ(L, ZZ)` and the metric dual `L^#` identify canonically for the standard unimodular identity form. Sage's dual parent is implementation evidence for the module-dual construction and for the metric-dual compatibility path. For arbitrary formed lattices this identification and any transported form on `Hom_R(L,R)` must be stated separately. |
| element multiplication between elements of dual toric lattices | dual evaluation pairing, identified with the identity-form pairing after the unimodular presentation is fixed | The public surface is evaluation of a dual element on a module element; through the identity Gram form this is the associated lattice bilinear pairing. |
| `direct_sum`, `intersection`, `saturation`, `submodule`, `span`, `span_of_basis`, `quotient` | ordinary free-module direct-sum, subobject, saturation, basis, and quotient owners | Sage returns toric-flavored parents to preserve labels and prevent accidental mixing, but the mathematical operations are the standard module operations. |
| parent `__call__`, `_coerce_map_from_`, containment, display, plotting | constructor/interop/display surfaces | Conversion barriers and labels protect parent identity. Plotting is geometry display interop, not module structure. |

### Formal Negative And Corrective Findings

Sage module autset category surface:

- Searched: `category_specs/modules/docs/SAGE_INVENTORY.md`; `sage/categories/modules.py`; recursive source search under installed `sage/modules` and `sage/tensor/modules` for `Autsets`, `AutCategory`, `automorphism`, `general_linear_group`, and `orthogonal_group`.
- Found: no installed `Modules(R).Autsets()` category in the inspected module category source. Sage exposes automorphism behavior through tensor finite-rank `general_linear_group()`/`automorphism()`, matrix-morphism invertibility predicates, and form/lattice `orthogonal_group()` methods.
- Conclusion: inference - the project should own the generic module automorphism surface through `Modules(R).AutCategory()`, with Sage automorphism classes treated as implementation witnesses and specialization evidence.
- Confidence: High.
- Gaps: generated documentation pages and import-resolution aliases outside the inspected installed source tree were not exhausted.

Legacy `NamedModules` surface:

- Searched: `category_specs/modules/docs/SAGE_INVENTORY.md`; `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-MODULES.md`; recursive source search under installed `sage/categories` and `sage/modules` for `NamedModules`, `class NamedModules`, and `def NamedModules`.
- Found: the mapping spec contains the legacy row `Modules(R).NamedModules()`, but the inspected installed Sage source did not expose a `NamedModules` category or method.
- Conclusion: inference - `NamedModules` is a legacy local/wrapper vocabulary item, not a Sage 10.7 source surface; the replacement owner remains `Modules(R).Constructors()`.
- Confidence: High.
- Gaps: historical local deleted files and upstream Sage versions before 10.7 were not inspected in this reconciliation pass.

Cell-module factory ownership:

- Searched: `category_specs/modules/docs/SAGE_INVENTORY.md`; `sage/modules/with_basis/cell_module.py`; installed Sage categories and algebras for `def cell_module` and `cell_module(`.
- Found: `CellModule` is a module class, and `FiniteDimensionalAlgebrasWithBasis.ParentMethods.cell_module(mu, **kwds)` is the visible public factory. No generic module-category `cell_module` constructor was found.
- Conclusion: inference - cell-module construction is algebra-side, while the resulting cell module's module, form, radical, and simple-module methods map to cellular representation/form/quotient owners.
- Confidence: High.
- Gaps: cellular-algebra subclasses outside the searched installed categories/algebras may add specialized wrappers.

Ore module category source:

- Searched: `category_specs/modules/docs/SAGE_INVENTORY.md`; `sage/modules/ore_module.py`; installed `sage/categories/ore_modules.py`; recursive installed-source search for `class OreModules` and `OreModules(`.
- Found: contrary to the local inventory's negative finding, installed Sage 10.7 includes `sage/categories/ore_modules.py` with `class OreModules(Category_over_base_ring)`, and `OreModule.__classcall_private__` references `OreModules(base, twist)`.
- Conclusion: inference - the source-visible Sage category surface is present and must be included in future inventory updates; project ownership is still deferred because the mathematical owner name has not been chosen.
- Confidence: High.
- Gaps: the written Sage manual pages for Ore modules were not separately crawled in this pass.

Free-module element source visibility:

- Searched: Python import location for `sage.modules.free_module_element`; installed `sage/modules/free_module.py` element dispatcher; structural searches for dense vector class names recorded in the local inventory.
- Found: the installed tree exposes `sage/modules/free_module_element.cpython-312-x86_64-linux-gnu.so`, while readable Python source for the base element implementation and several dense vector classes is not present in this environment.
- Conclusion: inference - element-level reconciliation for dense vector internals must rely on visible dispatcher evidence, category element methods, and upstream Cython source acquisition if exact internal behavior is required.
- Confidence: High.
- Gaps: upstream `.pyx` source and generated Cython/C sources were not inspected.

## Converted Mapping Content

This file records the forward target mapping from Sage module surfaces into the local
category-spec hierarchy.

## Constructor Namespace

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| `Modules(R).NamedModules()` | `Modules(R).Constructors()` | Sage constructors create module objects; they are not mathematical subcategories. |
| `FreeModule(R, n)` and `R^n` | `Modules(R).Constructors().FreeModule(rank=n)` refined into `Modules(R).Free()` plus finite-rank and base-ring restrictions | The constructor is concrete; `Free` is an axiomatic restriction attachable to any module subcategory. |
| `CombinatorialFreeModule(R, basis_keys)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys)` refined into `Modules(R).Free()` and `Modules(R).WithOrderedGeneratingSet()` | Combinatorial free modules are a Sage constructor family for free modules with explicit basis keys, not a mathematical subcategory. |
| Plain-set Sage `S.algebra(R)` / `Sets().Algebras(R)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)`, exposed by `S.free_module(R)` | Sage's existing path already constructs the free `R`-module with basis indexed by `S`. The spec routes that Sage source surface here instead of treating it as an algebra constructor. |
| `VectorSpace(K, n)` | `Modules(K).Constructors().VectorSpace(n)` refined into `Modules(K).Free().FiniteRank().OverField()` | Vector spaces are modules over fields with finite-rank structure when the constructor supplies a dimension. |
| Matrix presentations `f: R^m -> R^n` | `Modules(R).from_matrix(M)` delegating to `FinitelyPresentedModulesOverPID.from_matrix` | A matrix presentation defines `coker(f)`. Smith-form and elementary-divisor normalization are specific to finitely presented modules over PIDs, so the constructor namespace delegates to that subcategory owner. |
| `SubmoduleWithBasis`, free-module submodules, vector subspaces | `Modules(R).Subobjects()` / `Submodules` plus ordered-generating-set refinements | In module categories, subobjects are submodules. |
| Quotient modules and FGP modules | `Modules(R).Quotients()` plus finite-presentation/base-ring refinements | Quotients are construction categories attachable to arbitrary module subcategories. |
| Ring objects viewed as modules | `Modules(R).Constructors().RingObjectAsModule(...)` | The ring object supplies the module structure; ring-specific methods remain in `rings`. |
| Ring `R` with a selected unit basis viewed as a rank-one free module, plus inverse `BaseIsomorphism1D` witnesses | `Modules(R).Constructors().rank_one_module_with_ring_isomorphisms(basis=u)` and its module-only projection `ring_as_rank_one_module()` | Sage's ring-side `free_module` source constructs the free rank-one module together with inverse isomorphisms between `R` and that module. The project-owned constructor name exposes the module object and witness morphisms under the explicit unit-basis hypothesis recorded by Sage source; it is not a generic canonical identification for arbitrary rank-one modules. |
| Square `MatrixRing(R, n)` / `MatrixSpace(R, n, n)` viewed over `R` | The same parent refined into `Modules(R).Free().FiniteRank()` | A square matrix parent is a free finite-rank `R`-module on the matrix-unit basis. This is module structure on the same parent, not a second constructor family. |

Constructor signatures expose the finite Sage input casework as named-only overload
shapes under the original Sage constructor names instead of mirroring Sage's positional
dispatch or inventing new public constructor names. `FreeModule(...)` has overloads
for `rank=...`, `basis_keys=...`, `rank=..., with_basis=None`,
`rank=..., inner_product_matrix=...`, `rank=..., inner_product_rows=...`, and
`rank=..., inner_product_entries=...`. `VectorSpace(...)` has the corresponding
`dimension=...`, `basis_keys=...`, `dimension=..., with_basis=None`,
`dimension=..., inner_product_matrix=...`, `dimension=..., inner_product_rows=...`,
and `dimension=..., inner_product_entries=...` shapes. `FreeQuadraticModule(...)`
uses `rank=...` together with exactly one of `inner_product_matrix=...`,
`inner_product_rows=...`, or `inner_product_entries=...`. Sage's
`inner_product_ring` path is not public because the installed Sage source immediately
raises `NotImplementedError`.

`FPModule(...)` keeps Sage's original constructor name and exposes the three source
shapes as `algebra=..., generator_degrees=..., relations=...`,
`defining_map=...`, or `module=...`. `IntegerLattice(...)` keeps the original name
and exposes `basis=...` for the matrix, row-list, and order-element Sage shapes.
`TorsionQuadraticForm(...)` keeps the original name and exposes `q=...` for either
matrix or row-list data. Quotient construction similarly splits Sage's
`quotient_module` data shapes into `quotient_by_submodule`,
`quotient_by_generators`, `quotient_by_relation_matrix`, and
`quotient_by_relation_rows`.

Ring-as-module constructors mirror the ring constructor split: polynomial
`var_array` admits only one generator-count integer, power-series construction splits
univariate and multivariate routes, and Laurent/Puiseux series expose explicit
named-only overloads from their underlying power/Laurent series rings under the same
constructor names. When upstream Sage
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

## Square Matrix Parent Recovery

Sage's documented split is that rectangular matrix spaces lie in module-with-basis
categories, while square matrix spaces refine further to algebra-with-basis categories.
That algebra refinement does not remove the underlying free finite-rank `R`-module
structure on the square parent.

The project module owner rule is therefore:

| Module surface on a square matrix parent over `R` | Owner | Codomain consequence |
| --- | --- | --- |
| Rank, basis, basis order, coordinate vectors, `from_vector`, submodule and quotient-module structure, module homs | `Modules(R).Free().FiniteRank()` with the usual basis-bearing refinements | The codomain stays the same square matrix parent viewed as an `R`-module. |
| `row_space()` and `column_space()` | Ordinary free-module outputs over `R`, distinct from the square matrix parent itself | These remain separate free modules derived from the matrix parent; they do not replace the parent-as-module surface. |
| Ring multiplication, units, ring ideals | Not owned here | These remain in `rings` and `algebras`. |

Migration consequence: keep matrix-space linear methods in `modules`, including the
square case, and keep the category-obligation example expectation that the square matrix parent refines into
`Modules(R).Free().FiniteRank()` simultaneously with its ring and algebra structure.

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

## Rank, Primitive Elements, And Divisibility Boundary

`rank()` is a parent method on `Modules(R).Free()`. Finite-rank free modules may also
expose `dimension()` as a basis-cardinality convention.

Do not admit a free-module element method named `divisibility()` from coordinate gcds,
chosen generators, or a putative divisor relation `v = a*w`. That premise is not a
source-grounded module definition here, and it must not be conflated with lattice/form
divisibility.

The generic module-element predicate `v.is_primitive()` is already routed through the
cyclic submodule inclusion `v.span().inclusion().is_primitive()`, i.e. through the
primitive morphism/submodule notion. It is not a unit-divisibility predicate unless a
later source-grounded proof establishes that equivalence under explicit hypotheses.

The sourced divisibility surface for formed elements belongs in the symmetric bilinear
forms subtree: for `b: M x M -> S`, `divisibility(v)` is the submodule
`<b(v, M)> <= S`; when `S = R`, this is an ideal of `R`.

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

### Wrapper Candidate Classification

The recovered wrapper plan at
`plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` requires every
Sage-wrapper candidate to be classified before deletion. This mapping pass fixes the
classification as follows.

| Classification | Wrapper candidates | Migration consequence |
| --- | --- | --- |
| Constructor-only interop shell | `_CombinatorialFreeModules`, `_FreeModulesWithStandardBasis`, `_FiniteRankFreeModules`, `_FreeModulesOverIntegralDomains`, `_FreeModulesOverPIDs`, `_VectorSpaces`, `_RealDoubleVectorSpaces`, `_ComplexDoubleVectorSpaces`, `_VectorSubspaces`, `_VectorSubspacesWithOrderedGeneratingSet`, `_VectorSpaceQuotients`, `_FreeModuleSubmodules`, `_FreeModuleSubmodulesWithOrderedGeneratingSet`, `_SubmodulesWithOrderedGeneratingSet`, `_FreeModuleQuotients`, `_QuotientModulesWithOrderedGeneratingSet`, `_FinitelyGeneratedPIDQuotientModules` | These wrapper categories are deleted. Exact Sage implementation classes may still be matched at constructor interop boundaries, but public methods route through the constructor, subobject, quotient, basis, ordered-basis, PID, field, hom, tensor, and finite-presentation owners listed above. |
| Forms-owned owner | `_FreeQuadraticModules`, `_TorsionQuadraticModules` | Free quadratic modules and torsion quadratic modules are not module-wrapper categories. Their Gram, bilinear, quadratic, evenness, genus, and orthogonal-group surfaces route through formed-module owners and their aut categories; module paths remain only constructor or compatibility routes. |
| Lattice-owned owner | `_IntegerLattices` | The retained surface is a real integral-lattice/form category: finite-rank free `ZZ`-modules with integral symmetric nondegenerate bilinear form. Reduction, enumeration, gluing, dual, discriminant, and genus methods are lattice-specific surfaces, not generic module methods. |
| Real module-category owner | `_FreeGradedModules`, `_FinitelyPresentedGradedModules`, `_OreModules`, `_RepresentationModules`, `_RingObjectsAsModules` | These retained names describe mathematical module categories or forgetful module surfaces. They are not deletion targets, and their methods stay on graded, Ore, representation, or ring-object-as-module owners with inherited ordinary module behavior. |

Unresolved-owner check:

- Searched: the recovered wrapper plan's class todo list, the current wrapper mapping
  table above, `category_specs/modules/docs/SAGE_INVENTORY.md`, and exact wrapper-name
  matches in `category_specs/modules`.
- Found: no active wrapper candidate is assigned to an unresolved-owner bucket in this
  mapping; deleted wrapper names remain in mapping/provenance docs, while retained code
  names are exactly the real-category rows listed above.
- Conclusion: inference - the wrapper migration mapping has no known unresolved
  candidate classification left for this leaf.
- Confidence: Medium.
- Gaps: this is a documentation and source-map audit, not a fresh exhaustive Sage
  source re-inventory or implementation category-obligation example run.

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

### Method Mapping Rules

The same Sage implementation class can expose methods owned by several mathematical
categories. The migration should map each Sage method to a project method signature:
where the project method is defined, its inputs, its hypotheses, and its return type.
Construction categories describe output structure or extra methods on constructed
objects; they do not by themselves determine where an operation is called.

For root module construction signatures, use the tracked spec
`[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]`.

| Method group | Project mapping |
| --- | --- |
| `rank`, `dimension`, basis cardinality | `Modules(R).Free()` for rank as basis cardinality; finite-dimensional aliases belong to finite-rank or field-vector owners. |
| `basis`, `basis().keys()`, `monomial`, `term`, `from_vector`, `linear_combination_of_basis` | `WithBasis()`; ordered coordinate variants belong to `WithOrderedBasis()`. |
| `gens`, `gen`, `ngens` | `WithOrderedGeneratingSet()` unless the methods assert basis coordinates, in which case `WithOrderedBasis()`. |
| element `list`, `vector`, `support`, coefficient lookup, leading/trailing term methods | basis or ordered-basis element surfaces; not generic module elements. |
| `degree`, coordinate-ring bookkeeping, dense/sparse conversion, representation hooks, `_sympy_`, `_magma_init_`, `_macaulay2_` | interop or representation details unless a mathematical invariant is explicitly stated. |
| `linear_combination`, parent `sum`, random elements | generic computational helpers; no public category method unless the spec states finite-linear-combination or probability-distribution structure. |
| `submodule`, `submodule_with_basis`, `span`, `zero_submodule` | Construction methods called on an ambient module `M`; they return submodules of `M`. Basis/order/PID/field hypotheses refine the signature and output subobject structure. |
| Submodule comparison and ambient/lift/retract methods | Methods on subobject or ambient-bearing module objects. They require a specified inclusion or ambient relation, not just an abstract module isomorphism. |
| `intersection`, `saturation`, `denominator`, `index_in` | Methods on submodules of a common ambient module, with free/integral-domain/PID hypotheses where the operation or algorithm requires them. |
| `quotient_module`, `__truediv__`, `quotient_abstract`, quotient matrices | Construction methods called on an ambient module `M` with submodule data `N <= M`; they return `M/N`. Field/free/PID/finite-presentation/basis hypotheses refine the signature and output quotient structure. |
| `cover`, `relations`, `free_cover`, `free_relations`, `quotient_map`, `lift_map`, `lift`, `retract` | quotient or subquotient construction owners; `lift`/`retract` for submodules belong to `Subobjects()`. |
| `cokernel_basis_indices` | quotient owners with basis or PID normal-form hypotheses. |
| Smith-form data, `invariant_factors`, `invariants`, `smith_form_gens`, `free_part`, `torsion_part`, `annihilator`, element order | `FinitelyPresentedModulesOverPID` and its torsion/finite refinements. |
| `hom`, `_Hom_`, `module_morphism`, morphism from basis/images/matrices, `on_basis` | the relevant `HomCategory()`; basis-defined constructors refine through `WithBasis().HomCategory()`. |
| `tensor`, `tensor_module`, tensor constructors, tensor factors | Tensor construction methods are called on modules with compatible base/sidedness data and return tensor-product modules; tensor-product objects may have additional factor/construction methods. |
| `dual`, `linear_form`, `alternating_form`, symmetric and exterior powers | `dual()` is called on the module whose dual is being constructed. Linear-form, symmetric, and exterior surfaces require explicit finite-rank/free/projective and sidedness hypotheses before placement. |
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

For `C <= FormedModules(R)`, preservation of form data is not a separate module-local
boolean predicate. The object `C.HomCategory().Of(M, N)` owns the containment check for
candidate module morphisms, and isometry is isomorphism inside that formed-module Hom
object. In the endomorphism case, `C.AutCategory().Of(M)` is the orthogonal group.
Matrix criteria are implementation witnesses only after a presentation has been fixed.

## Dual Objects As Hom Objects

`Modules(R).DualObjects()` owns linear dual modules. For an object `M in Modules(R)`,
the mathematical meaning is

```text
M^* = Hom_R(M, R).
```

The public construction surface is therefore `M.dual()` as an object lying in
`Modules(R).DualObjects()`, but the category-theoretic content must route through the
module hom layer. The dual object is simultaneously:

- a dual object in `Modules(R).DualObjects()`;
- a hom object in `Modules(R).HomCategory()` with codomain the rank-one module `R`;
- an `R`-module, through the module-hom extra structure.

The implementation target in `subcategories/constructions/dual_objects.py` is to keep
the extra-supercategory chain routed through `Modules(R).HomCategory()`, specifically
the linear integral form surface, instead of shortcutting directly to `Modules(R)`.
This preserves the fact that elements of `M^*` are both module elements and morphisms
`M -> R`.

The docstring for `M.dual()` must identify this Hom-dual meaning. If a subclass or
interop path also has a metric-dual convention, the docstring must point to that
separate construction and say when the global category diagnostic flag should warn
that `dual()` is returning an evaluation-bearing Hom object rather than a metric dual.
That flag is the disabled-by-default framework diagnostic switch specified by
`[[SPEC-MAPPING-CAT]]`; diagnostics are logging-only and must not weaken the Hom-dual
contract.

Migration consequences:

- `RModule.dual()` is a named construction into `Modules(R).DualObjects()`, not a
  separate forms-local helper.
- the dual of a morphism `f: A -> B` belongs to
  `Modules(R).HomCategory().ElementMethods` as `f.dual(): B^* -> A^*`;
- public type aliases for `DualModule` and dual elements must point to the
  `DualObjects` method surfaces, not to plain `RModule` aliases;
- tensor-component duals and semilinear form data may refine the form object attached
  to a module, but they do not replace the module-level linear dual owner. No separate
  `TwistedForms` category is admitted unless the forms mapping records a concrete
  public surface that cannot be expressed through `FormedModules(R)`,
  tensor-component duals, and Hom-category structure.

## Topological Modules

Topological module structure should inherit the topological-space surface from
`topological_spaces`, the module surface from `modules`, and any ring topology from
`rings`. It should not duplicate topological-space methods locally.

## 6-Gate Protocol Review Log

### GATE 1: Source Grounding — PASS (with caveats)

Every mapping row cites proper Sage source paths. All 31 explicitly listed installed
Sage source files under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/`
were verified present on disk by direct filesystem probe. Spot-checked line ranges
against Sage source content:

- `categories/modules.py:120-152` (`__classcall_private__` dispatching fields to
  `VectorSpaces`): confirmed; the method signature, dispatch logic, and examples in
  the spec row match the source at lines 125-152.
- `categories/modules.py:342-493` (FiniteDimensional, FinitelyPresented, Filtered,
  Graded): confirmed; `with_axiom` calls and `FilteredModulesCategory.category_of`
  routing are present at the cited locations.
- `categories/modules.py:246-264` (TensorProducts, DualObjects): confirmed; both
  construction-category accessors use `TensorProductsCategory.category_of(self)`
  and `DualObjectsCategory.category_of(self)`.
- `modules/ore_module.py:322-357` (`__classcall_private__`): confirmed; the
  normalization logic and `OreModules(base, twist)` category dispatch are present.
- `rings/polynomial/ore_polynomial_ring.py:1255` (`quotient_module`): confirmed;
  the method signature exists at that line.
- `categories/finite_dimensional_algebras_with_basis.py:1499-1653` (`cell_module`):
  confirmed; both `cell_module_indices` (line 1499) and `cell_module` (line 1599)
  factory methods exist.
- `categories/ore_modules.py` (`class OreModules`): confirmed present at line 9,
  contrary to the local inventory negative finding; the spec correctly corrects
  this in its Formal Negative And Corrective Findings (line 180-186).

The Source Coverage Ledger notes "21 additional installed source paths listed in
`category_specs/modules/docs/SAGE_INVENTORY.md` beyond this ledger limit" (line 79).
The local inventory (`category_specs/modules/docs/SAGE_INVENTORY.md`) exists at 811
lines and covers constructors, categories, free/vector/quadratic/graded/Ore/tensor/
representation/ring-bridge surfaces. Cross-reference completeness is therefore
reasonable but not exhaustive.

Caveat: The spec references `plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`
(line 422) as a source document, but this file does not exist in the repository.
No file matching `*wrapper*migration*plan*` was found by recursive filesystem search.
This is a broken reference — the spec's wrapper classification work (lines 419-445)
is self-contained enough to proceed, but the missing reference is a documentation
gap.

Caveat: line number ranges in the mapping rows are approximate (e.g., `categories/modules.py:836-980`
for Subquotients/CartesianProducts, which spans multiple construction accessors).
The Sage source at these locations does contain the claimed surfaces, but the
ranges are coarser than the spec suggests. This is acceptable for a mapping spec
but should be refined in implementation cards.

### GATE 2: Sage Surface Completeness — PASS (with gaps acknowledged)

The spec's "Reconciled Category And Constructor Surfaces" table (lines 95-104) accounts
for: `__classcall_private__` field dispatch; FiniteDimensional/FinitelyPresented/
Filtered/Graded/WithBasis axiomatic restrictions; TensorProducts/DualObjects/
CartesianProducts/Subquotients/Subobjects/Quotients/IsomorphicObjects construction
categories; Homsets/Endsets; constructor namespace entries (FreeModule, VectorSpace,
span, FreeQuadraticModule, QuadraticSpace); ring-side bridges (R^n, R^(m,n),
R.free_module); Ore module factory; and cell-module factory.

The "Reconciled Method Ownership" table (lines 108-132) accounts for 24 method groups:
base_ring/zero/linear_combination; tensor products; duals/forms; basis/coordinates;
generators; monomial/term elements; submodule/subspace constructors; submodule
intersection/saturation; quotient constructors; homs and morphisms; morphism
arithmetic and predicates; automorphism/GL; orthogonal groups; determinant/
discriminant/gram forms; integral lattice methods; reduction/enumeration algorithms;
Smith/PID invariants; graded algorithms; representation structure; cell-module
structure; Ore structure; and interop/private rejections.

The "Toric Character-Lattice Corrective Mapping" (lines 136-152) provides an
additional 7-row mapping for `sage.geometry.toric_lattice`, properly routing its
surfaces to free-module, dual-object, and formed-lattice owners rather than a
separate toric owner.

The "Sage Wrapper Subcategory Migration Mapping" (lines 389-417) provides a 26-row
table mapping each deleted/retained wrapper class to its constructor and mathematical
method owners.

The "Formal Negative And Corrective Findings" section (lines 156-194) records five
negative/finding items: autset absence (correct — Sage 10.7 has no `Modules(R).Autsets()`
category), NamedModules legacy vocabulary (correct — not present in Sage 10.7),
cell-module factory ownership (correct — algebra-side constructor), Ore module
category source (corrective — confirms presence contrary to inventory negative
finding), and free-module element source visibility (correct — Cython .so only).

The Sage inventory file (`category_specs/modules/docs/SAGE_INVENTORY.md`, 811 lines)
was inspected. It covers: constructor entry points (17 rows, lines 31-60); Sage
category interop for Modules, ModulesWithBasis, and construction categories (lines
62-127); standard free modules and vector spaces (6 class families + core methods +
caveats, lines 128-193); homsets and morphisms for free-module, FGP, finite-rank,
FP-graded, and Ore families (lines 195-273); quadratic free modules and integral
lattices (lines 275-337); combinatorial modules, subquotients, and representations
(lines 339-451); FGP modules, torsion quadratic modules, and FQF orthogonal groups
(lines 453-531); finite-rank tensor modules (lines 533-561); finitely presented
graded modules (lines 562-616); Ore modules (lines 618-657); ring-side module bridges,
ideals, and polynomial/series/matrix rings (lines 659-755); and negative findings
(lines 757-811).

Gaps acknowledged in the spec:
- "21 additional installed source paths ... beyond this ledger limit" (line 79)
- Sage categories not covered by either spec or inventory: `sage/categories/algebra_modules.py`,
  `sage/categories/bimodules.py`, `sage/categories/drinfeld_modules.py`,
  `sage/categories/left_modules.py`, `sage/categories/right_modules.py`,
  `sage/categories/super_modules.py`, `sage/categories/super_modules_with_basis.py`,
  `sage/categories/hecke_modules.py` — these are module-related Sage category files
  present on disk but absent from the local inventory and spec. Their surfaces
  (left/right/bimodule sidedness, super-module parity, Hecke modules, Drinfeld
  modules) are not yet inventoried.
- Sage module files on disk not in the source ledger: `sage/modules/complex_double_vector.py`,
  `sage/modules/diamond_cutting.py`, `sage/modules/filtered_vector_space.py`,
  `sage/modules/free_module_pseudohomspace.py`, `sage/modules/free_module_pseudomorphism.py`,
  `sage/modules/misc.py`, `sage/modules/module_functors.py`,
  `sage/modules/multi_filtered_vector_space.py`, `sage/modules/ore_module_element.py`.
  Some of these (pseudohomspace, pseudomorphism, ore_module_element, filtered_vector_space,
  multi_filtered_vector_space) are semantically meaningful for module mathematics;
  diamond_cutting is geometry-specific; misc and module_functors are likely utility
  code. The spec's completeness status line (81-83) routes these through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

### GATE 3: Constructor Route Justification — PASS

Each constructor and method route is mathematically justified:

- `FreeModule(R, n)` → `Modules(R).Free().FiniteRank()`: Correct. A free module of
  finite rank carries the free-module axiom plus finite-rank structure. The
  constructor is a named factory, not a subcategory.
- `VectorSpace(K, n)` → `Modules(K).Free().FiniteRank().OverField()`: Correct.
  Vector spaces are free finite-rank modules over a field.
- `CombinatorialFreeModule(R, basis_keys)` → `Modules(R).Free()` + `WithBasis()`:
  Correct. A combinatorial free module mathematically is a free module with an
  explicit specified basis indexed by the key set.
- Tensor products: `Modules(R).TensorProducts()` owns tensor-product object methods;
  the caller-side `M.tensor(N)` lives on `Modules(R).ParentMethods`. Correct
  separation of construction-call surface from result-category surface.
- Dual objects: `M.dual()` returns an object in `Modules(R).DualObjects()`, routed
  through `HomCategory()` because `M^* = Hom_R(M, R)`. The spec's "Dual Objects As
  Hom Objects" section (lines 568-611) correctly identifies the dual as simultaneously
  a dual-construction object and a hom object. The extra-supercategory chaining
  through `HomCategory()` is mathematically sound.
- Subobjects: `Modules(R).Subobjects()` owns submodule methods. The caller is the
  ambient module. Output submodule category is codomain data. Correct.
- Quotients: same pattern as subobjects. `Modules(R).Quotients()` owns quotient
  methods. Correct.
- HomCategory / EndCategory / AutCategory: `Modules(R).HomCategory()` owns hom-object
  and morphism methods. `End_R(M)` is an R-algebra via the module-end extra structure.
  `Aut_R(M)` is the invertible part. Correct mathematical layering.
- Subquotients: `Modules(R).Subquotients()` is the construction category for
  subquotient objects with ambient, lift, retract. Subobjects and Quotients refine
  this. Correct per Sage's covariant construction hierarchy.
- Graded: `Modules(R).Graded()` is an attachable restriction. Concrete FP graded
  modules are constructor-family objects. Correct.
- Filtered: same attachable-restriction pattern. Correct.
- FiniteDimensional / FinitelyPresented: axiomatic restrictions attachable to any
  module subcategory. Correct.

Method ownership follows the "highest category where well-defined" rule (lines 36-38):
`base_ring`, `zero`, additive/scalar operations are on `Modules(R)` directly.
`basis`, `monomial`, `term` are on `WithBasis()`. `submodule`, `span` are
construction methods on `Modules(R)` with result in `Subobjects()`. This is
mathematically consistent.

The Ore module constructor route is deferred (lines 103-104) pending a decision
between semilinear-operator and Ore-algebra ownership. This is explicitly documented
as deferred, not incorrectly routed.

### GATE 4: Nonmathematical Rejection — PASS

The spec explicitly rejects nonmathematical surfaces with concrete justifications:

- Lines 131-132: `is_sparse`, `is_dense`, `is_exact`, `some_elements`, `random_element`,
  `dense_module`, `sparse_module`, `element_class`, display hooks, `_sympy_`,
  `_magma_init_`, `_macaulay2_`, `_repr_`, `_latex_` → "Not public mathematical
  category surfaces unless a later spec introduces exact-computation or
  probability-distribution structure with explicit hypotheses."
- Lines 258-265: Sage's `CombinatorialFreeModule(..., **kwds)` keyword bag
  (`bracket`, `latex_bracket`, `latex_names`, old monomial ordering aliases, `key`,
  print controls) → rejected as constructor surface; recovered through `print_options()`
  API, not category constructors.
- Lines 322-323: `sum(iter_of_elements)` and `linear_combination(iter_of_elements_coeff, ...)`
  → "The module laws already give addition and scalar multiplication. Sage implements
  parent-side aggregation for speed; that implementation detail is not itself
  mathematical structure."
- Lines 323-324: `_element_constructor_`, `_convert_map_from_`, `_coerce_map_from_`,
  `_from_dict` → "Sage parent internals. Public project mappings should expose the
  mathematical constructors above, not raw dictionary or coercion plumbing."
- Line 325: `is_exact()` → "Exact-arithmetic capability predicate, not a module-category
  predicate. This belongs to a separate exact-computation policy if admitted."
- Lines 225-226: `inner_product_ring` path → "not public because the installed Sage
  source immediately raises `NotImplementedError`."
- Line 347-350: Free-module element `divisibility()` → explicitly rejected: "That
  premise is not a source-grounded module definition here, and it must not be
  conflated with lattice/form divisibility."
- Line 85: `__mul__` for modules → rejected in the dependent spec
  `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]` (row line 85).

Each rejection states the mathematical reason and routes the corresponding Sage
surface to an alternative owner (forms, lattice, interop, or explicit construction
names) where appropriate, satisfying the "no weakening without grounded replacement"
obligation from GATE 6.

### GATE 5: Ambiguity Routing — PASS (with deferred items tracked)

Unresolved issues are explicitly routed to decision cards or tasks:

- Ore module ownership: "Project ownership remains deferred between a semilinear-operator
  module owner and a module-over-Ore-algebra owner until the Ore decision is recorded"
  (line 104). Also: "project ownership is still deferred because the mathematical
  owner name has not been chosen" (line 184). The "Required Immediate Category Owners"
  table (line 468) lists `Modules(R).WithOreOperator(...)` or
  `Modules(OreAlgebra).FiniteRankFree()` as the pending owner. Status: decision needed
  but no `DECISION-ORE-*` card found in the repository. This is a legitimate ambiguity
  with an explicit placeholder, but the absence of a decision card file is a tracking
  gap.

- Sidedness: explicitly deferred to `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]`,
  which exists at `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES.md`.
  The spec's `annihilator`, `tensor_algebra`, `module_structure`, `dual`, `tensor`,
  and `natural_pairing` surfaces all defer to this decision for noncommutative
  sidedness choices.

- Missing Sage surfaces or mathematical ambiguities → routed through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]` (line 83), which exists at
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION/PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT/tasks/TASK-MAPPING-DOC-COMPLETENESS-RESEARCH.md`.

- Root module method ownership → `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]` (line 479),
  which exists and is in `needs-agent-review` status.

- Diagnostic flag for dual-vs-metric-dual convention → `[[SPEC-MAPPING-CAT]]` (line 596),
  which exists at `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-CAT.md`
  and is in `needs-agent-review` status.

- Parent phase → `[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]` (line 8),
  which exists.

- The "Unresolved-owner check" (lines 433-445) concludes: "the wrapper migration
  mapping has no known unresolved candidate classification left for this leaf"
  (confidence: Medium). The medium confidence and acknowledged gap ("this is a
  documentation and source-map audit, not a fresh exhaustive Sage source re-inventory
  or implementation category-obligation example run") are appropriate for a spec at this stage.

### GATE 6: Obligation Preservation — PASS

The spec preserves mathematical obligations consistently:

- The review gates (lines 36-40) explicitly state the preservation principle: "Preserve
  every inventoried Sage surface by mapping it to a project mathematical surface, a
  named constructor path, a mathematically justified non-mapping, or a tracked decision."
  "Place every method at the highest category where the operation is mathematically
  well-defined; subcategories inherit methods from supercategories."

- The CombinatorialFreeModule section (lines 306-340) carefully maps every Sage method
  to a mathematical surface rather than dropping it: `rank`/`dimension` → `Modules(R).Free()`;
  `basis`/`monomial`/`term` → `WithBasis()`; `from_vector` → `WithOrderedBasis()`;
  `submodule`/`quotient_module` → `Subobjects()`/`Quotients()`; `tensor` → `TensorProducts()`.
  No Sage method is silently dropped; each either gets a mathematical owner or is
  explicitly rejected as interop.

- The Sage Wrapper Subcategory Migration Mapping (lines 389-417) maps 26 wrapper
  classes. Of these, 17 are classified as "Constructor-only interop shell" and deleted,
  but their methods are redistributed to proper mathematical owners (constructor,
  subobject, quotient, basis, ordered-basis, PID, field, hom, tensor, finite-presentation).
  2 are classified as "Forms-owned owner" (FreeQuadraticModules, TorsionQuadraticModules).
  1 is "Lattice-owned owner" (IntegerLattices). 5 are "Real module-category owner"
  (FreeGradedModules, FinitelyPresentedGradedModules, OreModules, RepresentationModules,
  RingObjectsAsModules). No wrapper surface is deleted without a grounded replacement
  owner.

- The Wrapper Candidate Classification table (lines 426-431) confirms this classification.

- The "Method Mapping Rules" section (lines 470-507) systematically assigns every
  method group to its highest mathematical owner: rank → `Free()`; basis → `WithBasis()`;
  gens → `WithOrderedGeneratingSet()`; submodule → `Subobjects()`; quotient →
  `Quotients()`; hom → `HomCategory()`; tensor → `TensorProducts()`; dual →
  `DualObjects()`; forms → forms-owned owners; reduction → integral-lattice owners;
  graded → graded owners; Ore → Ore-algebra/semilinear-operator owner; representation →
  representation-module owner; ring-as-module → forgetful construction.

- The dependent spec `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]` explicitly
  requires (line 26): "No root abstract method is deleted, weakened, or moved before
  the replacement project method signature is admitted here or in a linked decision."
  The parent spec respects this by not weakening any root obligation.

- The "Rank, Primitive Elements, And Divisibility Boundary" section (lines 342-365)
  explicitly protects against weakening: "Do not admit a free-module element method
  named `divisibility()` from coordinate gcds" and routes primitive-element semantics
  through cyclic submodule inclusion, not unit-divisibility. Sourced divisibility for
  formed elements is explicitly placed in the symmetric bilinear forms subtree.

No weakening without grounded replacement was detected.

### Cross-Gate Findings

1. **Broken reference**: `plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`
   (line 422) does not exist. The spec's wrapper classification tables are self-contained
   and the missing file is not load-bearing, but this reference should be corrected or
   the file should be created.

2. **Ore decision card missing**: The Ore module mathematical owner is deferred but
   no `DECISION-ORE-*` card exists. This should be tracked as a prerequisite before
   Ore module implementation proceeds.

3. **Inventory gap**: Sage module-related category files (`algebra_modules.py`,
   `bimodules.py`, `drinfeld_modules.py`, `left_modules.py`, `right_modules.py`,
   `super_modules.py`, `super_modules_with_basis.py`, `hecke_modules.py`) and module
   files (`complex_double_vector.py`, `filtered_vector_space.py`, `free_module_pseudohomspace.py`,
   `free_module_pseudomorphism.py`, `multi_filtered_vector_space.py`, `ore_module_element.py`,
   `diamond_cutting.py`, `misc.py`, `module_functors.py`) are present on disk but not
   accounted for in either the spec's source ledger or the local inventory. These are
   routed through `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]` but should be
   explicitly listed in that task.

4. **Approximate line ranges**: Many Sage source line references are approximate
   (spanning entire method groups rather than precise locations). This is acceptable
   for a spec-level document but implementation cards should use more precise
   references.

5. **Wrapper migration plan reference**: The spec references a wrapper migration
   plan that doesn't exist under the cited path. The wrapper classification work
   in the spec is substantial and self-contained, but the reference should be fixed.

### Gate Summary

| Gate | Status | Evidence |
|------|--------|----------|
| GATE 1: Source grounding | PASS | All 31 + 4 additional Sage source files verified on disk. Line ranges spot-checked and confirmed. Local inventory exists at 811 lines. One broken doc reference (wrapper migration plan). |
| GATE 2: Sage surface completeness | PASS | 24 method groups, 26 wrapper classes, 7 toric rows, 5 negative findings accounted for. ~15 Sage module/category files not yet inventoried, routed to completeness task. |
| GATE 3: Constructor route justification | PASS | Constructor namespace, construction categories, method ownership, hom/end/aut layering all mathematically justified. Ore route deferred with explicit placeholder. |
| GATE 4: Nonmathematical rejection | PASS | ~12 explicit rejections with mathematical rationales and grounded alternative owners. No silent dropping. |
| GATE 5: Ambiguity routing | PASS | Ore ownership deferred, sidedness routed to existing decision card, completeness gaps to task, root methods to spec. Ore decision card file missing (tracking gap). |
| GATE 6: Obligation preservation | PASS | ~40 method groups preserved with proper mathematical owners. No weakening without replacement. Wrapper migration maps all methods before deletion. |

### Status Recommendation

**Recommended: admit with tracked follow-up cards.**

The spec is substantively sound across all six gates. Source references are verified,
mathematical routes are correct, nonmathematical surfaces are rejected with grounded
alternatives, ambiguities are routed to tracked cards, and obligations are preserved.

Before this spec advances beyond `needs-agent-review`, create or confirm existence of:
- A decision card for the Ore module mathematical owner (`DECISION-ORE-MODULE-OWNER`
  or similar).
- Either fix the broken reference to `SAGE_WRAPPER_MIGRATION_PLAN.md` or create
  that file.
- Ensure `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]` explicitly lists the ~15
  uninventoried Sage module/category files found in this review.
