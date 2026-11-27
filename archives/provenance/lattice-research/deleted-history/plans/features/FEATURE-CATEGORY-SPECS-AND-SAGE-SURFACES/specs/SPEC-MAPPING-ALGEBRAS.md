---
id: SPEC-MAPPING-ALGEBRAS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
- '[[DECISION-CELLULAR-ALGEBRA-OWNER]]'
title: Track algebras mapping spec
status: complete
priority: critical
requirement: Convert category_specs/algebras/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  public method and constructor signatures.
acceptanceCriteria:
- Source paths category_specs/algebras/docs/MAPPING.md and category_specs/algebras/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 70
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Algebras Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/algebras/docs/MAPPING.md`.

Source inventory: `category_specs/algebras/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/algebras/docs/SAGE_INVENTORY.md`.
- Sage written documentation pages named by the local inventory:
  - `reference/categories/sage/categories/algebras.html`
  - `reference/categories/sage/categories/algebras_with_basis.html`
  - `reference/categories/sage/categories/finite_dimensional_algebras_with_basis.html`
  - `reference/categories/sage/categories/commutative_algebras.html`
  - `reference/categories/sage/categories/semisimple_algebras.html`
  - `reference/categories/sage/categories/algebra_functor.html`
  - `reference/algebras/sage/algebras/free_algebra.html`
- Installed Sage source files checked or named by the local inventory:
  - `sage/categories/magmatic_algebras.py`
  - `sage/categories/associative_algebras.py`
  - `sage/categories/algebras.py`
  - `sage/categories/algebras_with_basis.py`
  - `sage/categories/finite_dimensional_algebras_with_basis.py`
  - `sage/categories/algebra_functor.py`
  - `sage/categories/algebra_modules.py`
  - `sage/categories/sets_cat.py`
  - `sage/algebras/free_algebra.py`
  - `sage/combinat/free_module.py`
  - `sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra.py`
  - `sage/categories/commutative_algebras.py`
  - `sage/categories/semisimple_algebras.py`
- Extra source-only surfaces found during reconciliation:
  - `sage/categories/algebras.py`: `ElementMethods._div_()` and `DualObjects.extra_super_categories()`.
  - `sage/categories/magmatic_algebras.py`: `ParentMethods.algebra_generators()`,
    `WithBasis.ParentMethods.product_on_basis()`, `product()`,
    `_product_from_product_on_basis_multiply()`,
    `WithBasis.FiniteDimensional.ParentMethods.to_finite_dimensional_algebra()`,
    and `derivations_basis()`.
  - `sage/categories/finite_dimensional_algebras_with_basis.py`:
    `ElementMethods.__invert__()` and the nested `Cellular` axiom surface.
  - `sage/categories/algebra_functor.py`: `AlgebrasCategory.ParentMethods.coproduct_on_basis()`
    and `GroupAlgebraFunctor._apply_functor_to_morphism()`.
  - `sage/categories/algebra_modules.py`: `AlgebraModules(A)` for modules over a
    commutative algebra `A`.
  - `sage/algebras/free_algebra.py`: free-algebra display, coercion, quotient,
    PBW-basis, monoid, and letterplace implementation helpers.
  - `sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra.py`:
    table, left-table, base-extension, ideal, homset, finite/cardinality, and
    structural predicates on the concrete table-based parent.
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this spec now records the checked source corpus and the
  method-by-method reconciliation below. Remaining missing surfaces are listed in
  formal negative-finding format because the current write scope excludes creating
  new follow-up cards.

## Source Reconciliation

| Sage surface | Reconciled target | Highest mathematical owner and consequence |
| --- | --- | --- |
| `Algebras.ParentMethods.characteristic()` | Inherited ring/base-ring characteristic, not an algebra-specific method | The value is `base_ring().characteristic()`. The algebra mapping preserves Sage behavior through `base_ring().characteristic()` and any ring-level `characteristic()` surface; `Algebras(R)` does not own a new method. |
| `Algebras.ParentMethods.has_standard_involution()` | Rejected public project method for now; compatibility evidence only | Sage's implementation is explicitly quaternion-specific and basis-dependent. Do not admit this as a generally grounded `Algebras(R)` method. Future admission must go through a source-grounded algebra-with-involution category or quaternion-algebra refinement, preferably exposing the actual involution/conjugation structure rather than a generic compatibility boolean. Decision: `[[DECISION-ALGEBRA-STANDARD-INVOLUTION-OWNER]]`. |
| `Algebras.ElementMethods._div_(y)` | Runtime interop helper | The public mathematical operation is division by an invertible element in the appropriate multiplicative/ring owner. The underscored Sage helper is not a public algebra method. |
| `Algebras.Quotients.ParentMethods.algebra_generators()` | `algebra_generators() -> AlgebraElementFamily` on algebra quotients | The quotient owner may retract generators from the ambient algebra; the returned family remains algebra elements, not a raw Sage family. |
| `Algebras.CartesianProducts`, `TensorProducts`, `DualObjects` | `Algebras(R).CartesianProducts()`, `TensorProducts()`, `DualObjects()` | These are construction categories on algebra subcategories. Product/tensor algebra structure belongs here; generic construction mechanics stay in Cat/universal construction surfaces. |
| `MagmaticAlgebras.ParentMethods.algebra_generators()` | `algebra_generators() -> AlgebraElementFamily` on `MagmaticAlgebras(R)` | The notion of algebra generators only requires bilinear multiplication over `R`; associative and unital endpoints inherit it. |
| `MagmaticAlgebras.WithBasis.ParentMethods.product_on_basis(i, j)` | Interop backing for the multiplication tensor and element multiplication | The public surface is element multiplication plus construction data. Basis-index multiplication is allowed as a Sage compatibility implementation hook for `WithBasis`, not as the canonical public constructor input. |
| `MagmaticAlgebras.WithBasis.ParentMethods.product()` and `_product_from_product_on_basis_multiply()` | Runtime implementation helper | These implement bilinear extension from basis-index multiplication. The method is not a separate mathematical obligation beyond the multiplication operation and the chosen basis data. |
| `MagmaticAlgebras.WithBasis.FiniteDimensional.ParentMethods.to_finite_dimensional_algebra()` | Interop conversion from a with-basis algebra to Sage's table parent | The mathematical owner is finite-dimensional algebras with basis; the project constructor still goes through `from_multiplication_tensor(multiplication=mu)`. The table parent is a Sage interop target, not the canonical source of algebra data. |
| `MagmaticAlgebras.WithBasis.FiniteDimensional.ParentMethods.derivations_basis()` | `derivations() -> Der(A)` | A derivation is an `R`-linear endomorphism `D: A -> A` satisfying `D(ab)=D(a)b+aD(b)`, not an algebra endomorphism. The basis-returning Sage method maps to the derivation submodule of `End_R(A)`, with its commutator Lie bracket when Lie-algebra vocabulary is present; a basis is recoverable only when basis data is present. |
| `AlgebrasWithBasis.ParentMethods.hochschild_complex(M)` | `hochschild_complex(coefficients=M) -> HochschildChainComplex` | Hochschild chains require algebra structure and coefficients. The with-basis implementation is Sage evidence, but the mathematical operation belongs at the algebra level when coefficients are grounded. |
| `AlgebrasWithBasis.ElementMethods.__invert__()` | Inherited multiplicative inverse, with with-basis implementation evidence | Invertibility is multiplicative/ring structure. The Sage basis-unit shortcut is implementation evidence, not a new with-basis algebra operation. |
| `AlgebrasWithBasis.CartesianProducts.ParentMethods.one_from_cartesian_product_of_one_basis()` | Interop helper for Cartesian-product units | Public unit data remains `one() -> AlgebraElement`; the basis index of the unit is compatibility data. |
| `AlgebrasWithBasis.TensorProducts.ParentMethods.one_basis()` and `product_on_basis(t1, t2)` | Tensor-product interop helpers for with-basis multiplication | Public tensor product ownership stays with `Algebras(R).TensorProducts()` and `WithBasis` basis data. Basis-index helpers remain implementation hooks. |
| `FiniteDimensionalAlgebrasWithBasis.ParentMethods.radical_basis()` | `radical() -> AlgebraIdeal` | Public surface returns the Jacobson radical ideal. Basis output is implementation evidence and must not replace the ideal interface. |
| `FiniteDimensionalAlgebrasWithBasis.ParentMethods.center_basis()` | `center() -> Algebra` | Public surface returns the center algebra; basis output is recoverable from the returned object when it has basis data. |
| `FiniteDimensionalAlgebrasWithBasis.ParentMethods.subalgebra(gens, category=None, *args, **opts)` | `subalgebra(generators) -> Algebra` | The generated subalgebra is algebra structure. Sage's category and option bag are implementation routing and are not exposed. |
| `FiniteDimensionalAlgebrasWithBasis.ParentMethods.ideal_submodule()` and `principal_ideal()` | Named left/right/two-sided ideal methods and principal variants | Preserve ideal-interface obligations: ideals are `Algebras(R).Ideals(A)` objects, module subobjects with left/right/two-sided predicates, ambient module, ambient algebra, and inclusion data. No side string or option bag is public API. |
| `FiniteDimensionalAlgebrasWithBasis.ParentMethods.orthogonal_idempotents_central_mod_radical()`, `idempotent_lift()`, `cartan_invariants_matrix()`, `isotypic_projective_modules()`, `peirce_summand()`, `peirce_decomposition()`, `is_identity_decomposition_into_orthogonal_idempotents()` | finite-dimensional associative unital algebra over a field, with basis-backed algorithms | Split the public surfaces by mathematical output and hypotheses: central idempotent lifting returns pairwise orthogonal idempotent elements of `A`; `idempotent_lift(x)` lifts an idempotent through the radical or named quotient; `cartan_invariants_matrix()` returns the integer Cartan matrix; `isotypic_projective_modules()` returns module summands; `peirce_summand(e_i,e_j)` returns the `e_i A e_j` module subobject; `peirce_decomposition(...)` returns the matrix/list of Peirce summands; the identity-decomposition predicate checks a finite family of orthogonal idempotents summing to `1_A`. These are not one broad finite-dimensional method blob and do not inherit to nonunital or nonassociative magmatic algebras. |
| `FiniteDimensionalAlgebrasWithBasis.ParentMethods.is_commutative()` | `Algebras(R).Commutative()` predicate/refinement evidence | Commutativity is a shared axiom; this Sage method is a detection implementation, not an algebra-only public method. |
| `FiniteDimensionalAlgebrasWithBasis.ElementMethods.to_matrix()`, `on_left_matrix()` | Representation/interoperability helpers | These are finite-dimensional regular-representation matrices. Public algebra methods should return morphisms/endormorphisms or module maps; raw matrices are interop/display data. |
| `FiniteDimensionalAlgebrasWithBasis.ElementMethods.__invert__()` | Multiplicative inverse with finite-dimensional implementation evidence | Public ownership remains multiplicative/ring structure; the finite-dimensional matrix solve is an implementation strategy. |
| `FiniteDimensionalAlgebrasWithBasis.Cellular` | Missing project cellular-algebra subcategory surface | Sage defines cellular algebras by a cell datum. This is a genuine mathematical subcategory of finite-dimensional algebras with basis and should become `Algebras(R).FiniteDimensional().WithBasis().Cellular()` after a tracked source-grounding decision/task. |
| `AlgebraFunctor(base_ring).__call__(G, category=None)` and `Sets.ParentMethods.algebra(base_ring, category=None, **kwds)` | Source-category-owned `S.free_algebra(R)` methods and named `Algebras(R).Constructors().free_algebra_from_*` targets | The Sage `category=` disambiguator is not public API. The selected source category chooses the named project constructor. |
| `AlgebrasCategory.ParentMethods.coproduct_on_basis()` for group/monoid algebra categories | Hopf/coalgebra refinement evidence | The coproduct is not owned by `Algebras(R)`. It belongs to a future Hopf/coalgebra category refinement for group-algebra essential images. |
| `GroupAlgebraFunctor._apply_functor_to_morphism(f)` | Functorial base-change interop | This is a construction-functor runtime morphism over base-ring maps. Public algebra mapping records the group-algebra constructor; functorial base change belongs to constructor/functor interop until project functor categories are grounded. |
| `AlgebraModules(A)` | `Modules(A)` for commutative algebra `A` | This is module-category structure over a fixed commutative algebra, not an algebra object or algebra constructor. Route it to the modules subtree; do not admit it as an Algebras method. |
| `FreeAlgebraFactory.create_key/create_object`, `FreeAlgebra_generic._repr_/_latex_`, `_element_constructor_`, `_coerce_map_from_`, `construction()`, `AssociativeFunctor` | Constructor/runtime/display/private interop | Public constructor remains `free_algebra_from_set(generators=S)`. Generator-name parsing, unique-factory keys, letterplace backend choice, display, coercion, quotient implementation, PBW basis, and construction functor internals are compatibility evidence, not public algebra-spec methods. |
| `FreeAlgebra_generic.gen(i)`, `gens()`, `ngens()`, `monoid()`, `degree_on_basis()`, `product_on_basis()` | With-basis/free-constructor evidence | Public generator surface is `algebra_generators() -> AlgebraElementFamily`; basis word degree is graded-algebra evidence; underlying free monoid and basis-index product are interop data. |
| `FiniteDimensionalAlgebra.table()`, `left_table()`, `base_extend()`, `ideal()`, `_Hom_()`, `is_associative()`, `is_commutative()`, `is_unitary()`, `one()` | Concrete table-parent interop and predicate evidence | Public construction uses multiplication tensors; table matrices are an interop input to tensor constructors. Ideals route through named ideal methods. Associativity, commutativity, and unitality refine to project axiom categories rather than staying as ordinary option flags. |

## Formal Negative Findings

- Searched: local inventory `category_specs/algebras/docs/SAGE_INVENTORY.md`; installed Sage files under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories` matching `finite_dimensional_algebras*`; `sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra.py`.
- Found: `sage/categories/finite_dimensional_algebras_with_basis.py` exists and defines the finite-dimensional category surface; no `sage/categories/finite_dimensional_algebras.py` file exists in the installed Sage 10.7 tree.
- Conclusion: inference based on the installed file tree: Sage has no separate category source file for finite-dimensional algebras without basis in this installation; the concrete table parent and with-basis category are the available Sage evidence.
- Confidence: High.
- Gaps: Sage online development branches were not checked because the task scope is installed Sage 10.7.

- Searched: local inventory source-visibility token `sage/tensor/cartesian`; installed Sage category sources `sage/categories/tensor.py`, `sage/categories/cartesian_product.py`, `sage/categories/algebras.py`, and `sage/categories/algebras_with_basis.py`.
- Found: tensor and Cartesian-product construction category files exist under their separate Sage category modules; no installed path or module named `sage/tensor/cartesian` was found in the checked Sage source tree.
- Conclusion: inference based on installed Sage 10.7 source: `sage/tensor/cartesian` is not a concrete source path for the Algebras mapping; tensor and Cartesian-product evidence should cite `sage/categories/tensor.py`, `sage/categories/cartesian_product.py`, and the algebra category files that specialize them.
- Confidence: High.
- Gaps: No web or Sage repository branch search was performed because the local task requested the installed source tree.

- Searched: Sage sources `sage/categories/algebras.py`, `sage/categories/algebras_with_basis.py`, `sage/categories/finite_dimensional_algebras_with_basis.py`, `sage/categories/semisimple_algebras.py`, `sage/algebras/free_algebra.py`, and installed quaternion-algebra sources under `sage/algebras/quatalg/`.
- Found: Sage implements `has_standard_involution()` on `Algebras.ParentMethods`, but its source comment says the algorithm is specific to quaternion algebras and should belong there. The checked quaternion sources expose quaternion conjugation and reduced trace/norm surfaces, not a project-level algebra-with-involution owner.
- Conclusion: inference based on installed Sage 10.7 source: reject `has_standard_involution()` as a public project method for now. Future admission requires a source-grounded algebra-with-involution category or quaternion-algebra refinement.
- Confidence: High for rejection from general `Algebras(R)`; medium for the future owner because the project has not yet grounded quaternion or algebra-with-involution categories.
- Gaps: Literature/source work for a durable algebra-with-involution or quaternion-algebra project category remains future work.

- Searched: Sage sources named above plus `sage/categories/algebra_functor.py` for Hopf/coalgebra methods on group-algebra constructions.
- Found: `coproduct_on_basis()` and documented antipode/counit behavior appear in the group-algebra functor discussion, but no Hopf-algebra project mapping surface exists in this Algebras spec.
- Conclusion: inference based on the checked sources: Hopf structure is real Sage evidence for group algebras, but it is not an `Algebras(R)` method and requires a separate Hopf/coalgebra category mapping before admission.
- Confidence: Medium.
- Gaps: Sage `hopf_algebras*` sources and local Hopf category specs were not checked because the assigned file is the Algebras mapping spec.

## Converted Mapping Content

`MagmaticAlgebras(R)` is the category of `R`-modules with bilinear multiplication.
`AssociativeAlgebras(R)` adds associativity without requiring a unit.
`Algebras(R)` is the associative unital endpoint. Algebra-specific methods belong in
this subtree. Ring and module methods are inherited from `rings` and `modules`.

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| Matrix-ring algebra methods | `Algebras(R)` plus matrix-algebra subcategories | A square matrix parent over `R` is the same object returned by `Rings().Constructors().MatrixRing(...)`, refined into `Algebras(R)`. Algebra methods stay here even though the constructor owner stays in `rings`. |
| `FreeAlgebra(R, n, names)` and `algebras.Free(R, n, names)` | `Algebras(R).Constructors().free_algebra_from_set(generators=S)` | This is the true free associative unital `R`-algebra on a set of symbols. Sage's `Sets().example().algebra(R)` is not this construction. |
| Plain-set Sage `S.algebra(R)` and `Sets().Algebras(R)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)`, exposed by `S.free_module(R)` | Sage already constructs the free `R`-module with basis indexed by `S` on this path. The spec routes that Sage source surface to `Modules(R)` and rejects it as evidence for an `Algebras(R)` constructor. |
| `S.algebra(R)` where the selected source category is `Magmas()` | `MagmaticAlgebras(R).Constructors().free_algebra_from_magma(magma=S)` | This names the free functor from magmas to `R`-modules with bilinear multiplication. It is not necessarily associative or unital, so both owner and codomain live in the magmatic algebra category rather than the current unital-associative `Algebras(R)` endpoint. |
| `S.algebra(R)` where the selected source category is `Semigroups()` | `AssociativeAlgebras(R).Constructors().free_algebra_from_semigroup(semigroup=S)` | This names the free functor from semigroups to associative, not necessarily unital, `R`-algebra objects. The method owner is the associative-algebra constructor namespace, not `Algebras(R)`. |
| `S.algebra(R)` for a Sage monoid `S` | `Algebras(R).Constructors().free_algebra_from_monoid(monoid=S)` | This is the monoid algebra `R[S]`, the free construction relative to the multiplicative-monoid forgetful functor. |
| `G.algebra(R)` for a Sage group `G`; `GroupAlgebra(G, R)` | `Algebras(R).Constructors().free_algebra_from_group(group=G)` | The essential image of the group free functor lands in Hopf algebras over `R`; as an `R`-algebra it is the group algebra `R[G]`. |
| `S.algebra(R, category=AdditiveSemigroups())` | `AssociativeAlgebras(R).Constructors().free_algebra_from_additive_semigroup(semigroup=S)` | This is the semigroup algebra using the additively written operation as multiplication of basis elements. The owner and target are associative and not necessarily unital. |
| `S.algebra(R, category=AdditiveMonoids())` | `Algebras(R).Constructors().free_algebra_from_additive_monoid(monoid=S)` | This is the monoid algebra using the additively written operation and zero element as multiplicative unit data. |
| `S.algebra(R, category=AdditiveGroups())` | `Algebras(R).Constructors().free_algebra_from_additive_group(group=S)` | This is the group algebra using the additively written group law. |
| `FiniteDimensionalAlgebra(k, table, assume_associative=True, assume_unital=True)` | First construct `mu: Tensor` through `TensorAlgebraComponents(k).Constructors().from_module_element_matrix(frame=e, ...)` or another tensor interop constructor, then call `Algebras(k).Constructors().from_multiplication_tensor(multiplication=mu)`. | Bespoke table/list/matrix shapes are tensor interop inputs, not algebra constructor inputs. The algebra constructor has one canonical product input: a tensor in `T_R(M)[1, 2]`. The tensor's parent determines the base module and base ring; coordinate extraction requires an explicit ordered frame. |
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
| `derivations_basis()` | `derivations() -> Der(A)` | The public surface returns the `R`-module of derivations, equivalently the Leibniz-rule subobject of `End_R(A)`, with Lie bracket structure when that category surface is available. A basis is recovered from that object when a basis has been chosen. |
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

## Square Matrix Parent Recovery

For a square matrix parent over a base ring `R`, the algebra owner recovers the
`R`-algebra structure on the same parent returned by the ring constructor. The public
surface consequences are:

| Algebra surface on the square matrix parent | Owner consequence |
| --- | --- |
| Multiplication as an `R`-bilinear product, unit, algebra generators, center, radical, finite-dimensional algebra-with-basis methods | Owned in `Algebras(R)` and matrix-algebra refinements below it. |
| Constructor spelling `MatrixRing(...)` or `MatrixSpace(R, n, n)` | Not reintroduced in `algebras`; constructor admission remains a `rings` responsibility. |
| Module-only structure such as rank, basis order, coordinate vectors, and linear submodule/quotient operations | Inherited from `modules`, not duplicated here. |

Migration consequence: algebra docs may rely on the square matrix parent as an
`R`-algebra, but they must not absorb the constructor namespace or the free-module
surface to make the matrix smoke easier.

## Free-Construction Routing

For source categories admitted in this subtree, the public method on a source object is
`S.free_algebra(R)`. The source category, not a runtime `category=` keyword, chooses
the constructor. The `Sets()` row below is carried out by
`Sets.ParentMethods.free_algebra`, backed by Sage `FreeAlgebra`; it is not Sage's
plain-set `S.algebra(R)` path. The `Magmas()`, `Semigroups()`, `Monoids()`, and
`Groups()` rows record target constructor stubs in the weakest algebra constructor
namespace whose objects actually satisfy the requested laws; matching source-method
stubs belong to those source-category subtrees when this project admits them.

| Source category for `S` | Public source method | Constructor target |
| --- | --- | --- |
| `Sets()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_set(S)` |
| `Magmas()` | `S.free_algebra(R)` | `MagmaticAlgebras(R).Constructors().free_algebra_from_magma(S)` |
| `Semigroups()` | `S.free_algebra(R)` | `AssociativeAlgebras(R).Constructors().free_algebra_from_semigroup(S)` |
| `Monoids()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_monoid(S)` |
| `Groups()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_group(S)` |
| `AdditiveSemigroups()` | `S.free_algebra(R)` | `AssociativeAlgebras(R).Constructors().free_algebra_from_additive_semigroup(S)` |
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
| `free_algebra_from_set(S)` | Sage `FreeAlgebra(R, |S|, names)`, refined to `Algebras(R).WithBasis()`, with a recorded finite generator presentation `tuple(S) -> algebra.gens()`. This is the true free associative unital algebra on generators. The current Sage-backed implementation requires `S` to be finite and iterable; the chosen enumeration is presentation data for the returned object, not a claim that cardinality alone canonically determines the free algebra on `S`. |
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
`mu.structure_constants(frame=e)` against `mu.base_module().rank()`, converts those
constants to Sage's right-multiplication table convention, and calls Sage
`FiniteDimensionalAlgebra(R, table, category=MagmaticAlgebras(R).FiniteDimensional().WithBasis())`.
Sage's documented constructor surface is finite-dimensional algebra over a field. If
If the implementation also wires finite-rank table algebras over a commutative base ring
through the same Sage classcall, that is a separate finite-rank-over-ring owner and may
not inherit field-only algorithms such as radical, Cartan, Peirce, or idempotent-lift
surfaces without their own hypotheses. The result is refined to project
`MagmaticAlgebras(R)` and to `AssociativeAlgebras(R)` or
`Algebras(R).FiniteDimensional().WithBasis()` only when the constructed table satisfies
the corresponding laws and the base hypotheses for that category are met.

## 6-Gate Protocol Review Log

*Review conducted 2026-05-07. Evidence from installed Sage 10.7 source files at
`/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/` and local
inventory at `category_specs/algebras/docs/SAGE_INVENTORY.md`.*

### Gate 1: Source Grounding — PARTIAL PASS

**Status: PARTIAL PASS (1 deficiency)**

**Positive findings (all verified by filesystem check):**

- All 13 claimed Sage source files exist and parse:
  `sage/categories/magmatic_algebras.py`, `associative_algebras.py`, `algebras.py`,
  `algebras_with_basis.py`, `finite_dimensional_algebras_with_basis.py`,
  `algebra_functor.py`, `algebra_modules.py`, `sets_cat.py`, `commutative_algebras.py`,
  `semisimple_algebras.py`, `sage/algebras/free_algebra.py`,
  `sage/combinat/free_module.py`,
  `sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra.py`.
- Local inventory `category_specs/algebras/docs/SAGE_INVENTORY.md` exists.
- Local source MAPPING.md exists.
- All key Sage method surfaces claimed in the Source Reconciliation table were
  verified in their respective source files: `has_standard_involution` (algebras.py
  L162), `product_on_basis` (algebras_with_basis.py L341, magmatic_algebras.py L192),
  `algebra_generators` (magmatic_algebras.py L107/L124), `hochschild_complex`
  (algebras_with_basis.py L135), `radical_basis` (finite_dimensional_algebras_with_basis.py
  L69), `center_basis` (L349), `center` (L372), `subalgebra` (L422), `Cellular` class
  (L1398), `coproduct_on_basis` (algebra_functor.py L719), `AlgebraFunctor.__call__`
  (algebra_functor.py L510).
- Negative findings confirmed: no `sage/categories/finite_dimensional_algebras.py`
  exists (only `_with_basis` variant); no `sage/tensor/cartesian` path exists in
  installed source tree.
- Sage `has_standard_involution` source (algebras.py L162-221) confirms it is
  quaternion-specific (uses `conjugate` attribute, QuaternionAlgebra examples),
  supporting the spec's rejection from general `Algebras(R)`.

**Deficiency:**

- **7 Sage HTML documentation paths claimed in Source Coverage Ledger are MISSING.**
  The spec states these paths exist under the "Sage written documentation pages named
  by the local inventory" heading (lines 47-53):
  `reference/categories/sage/categories/algebras.html`,
  `reference/categories/sage/categories/algebras_with_basis.html`,
  `reference/categories/sage/categories/finite_dimensional_algebras_with_basis.html`,
  `reference/categories/sage/categories/commutative_algebras.html`,
  `reference/categories/sage/categories/semisimple_algebras.html`,
  `reference/categories/sage/categories/algebra_functor.html`,
  `reference/algebras/sage/algebras/free_algebra.html`.
  None of these files exist under
  `/home/dzack/miniforge3/envs/sage/share/doc/sage/`. The only `algebras.html` found
  under the Sage share directory is an unrelated Pari/Giac doc at
  `share/giac/doc/pari/Associative_and_central_simple_algebras.html`.
  **Evidence:** `find /home/dzack/miniforge3/envs/sage/share -name 'algebras.html'`
  returns only the giac file; `-name 'free_algebra.html'` returns nothing.
  **Severity:** Low-medium. The Sage Python source files provide definitive
  documentation for method signatures. The HTML docs may simply not be built in this
  installation. However, the spec should not claim these paths exist without
  qualification. **Remedy:** Either remove the specific HTML path claims (retaining
  only source-file references that are verified), or add a note that HTML docs were
  not found in the installation and source files serve as the verified evidence.

### Gate 2: Sage Surface Completeness — FAIL

**Status: FAIL (3 unaccounted inventoried surfaces)**

**Accounting confirmed:**

- All 24 rows in the Source Reconciliation table map to inventoried Sage surfaces.
- The Converted Mapping Content table (rows 160-194) addresses all constructor and
  category surfaces from the inventory.
- The Free-Construction Routing table (rows 230-239) covers all 8 source-category
  free-algebra paths inventoried.

**Gaps — surfaces in Sage inventory NOT reconciled:**

1. **`FiniteDimensionalAlgebrasWithBasis.ParentMethods.semisimple_quotient()`**
   (Sage source: `finite_dimensional_algebras_with_basis.py` L295). Returns the
   quotient of the algebra by its Jacobson radical. This is a distinct mathematical
   operation from `radical()` and is listed in the local inventory (row 55:
   "semisimple_quotient()"). The spec's reconciliation table has no row for
   `semisimple_quotient`. The word "semisimple" appears in row 114 only as a
   descriptive note ("semisimple quotients") without a dedicated reconciliation
   entry.
   **Evidence:** `grep -c 'semisimple_quotient' SPEC-MAPPING-ALGEBRAS.md` returns 0.
   **Severity:** Medium. The semisimple quotient is a mathematically significant
   operation that should be mapped to a project surface, e.g.,
   `semisimple_quotient() -> Algebras(R).Semisimple()`.

2. **`Algebras.SubcategoryMethods.Supercommutative()`**
   (Sage source: `algebras.py` L110). Returns the full subcategory of
   supercommutative objects. Listed in local inventory row 47. The spec covers
   `Semisimple()` and `Commutative()` but does not mention `Supercommutative()`.
   **Evidence:** `grep -c 'Supercommutative' SPEC-MAPPING-ALGEBRAS.md` returns 0.
   **Severity:** Low. Supercommutative is a super-algebra concept that may require a
   separate super-algebra category mapping. However, since it is inventoried here, it
   needs at minimum a routing note (e.g., "routed to super-algebras subtree" or
   "deferred to [[DECISION-SUPERCOMMUTATIVE-ALGEBRA-OWNER]]").

3. **`FiniteDimensionalAlgebrasWithBasis.ParentMethods.radical()`** —
   NOTE: this is arguably covered by row 110 which maps `radical_basis()` →
   `radical() -> AlgebraIdeal`. However, Sage has BOTH `radical_basis()` and
   `radical()` as separate, independently callable methods. The spec row only
   explicitly names `radical_basis()` as the Sage surface being reconciled. The
   Sage `radical()` method (L233) returns a submodule with `ambient()` and
   `basis()`, and its docstring says "This uses radical_basis." The spec's
   mapping is mathematically correct (the public surface should be `radical()` not
   `radical_basis()`), but the reconciliation should record that BOTH Sage methods
   exist and are handled.
   **Evidence:** Sage source `finite_dimensional_algebras_with_basis.py` L69
   (`radical_basis`) and L233 (`radical`). The inventory lists both on row 55.
   **Severity:** Low. The mathematical content is preserved; this is a
   documentation completeness issue in the reconciliation row.

### Gate 3: Constructor Route Justification — PASS

**Status: PASS**

**Category hierarchy verified mathematically correct:**

- `MagmaticAlgebras(R)` = R-modules with bilinear multiplication (no associativity
  or unit required). Verified in Sage source
  `sage/categories/magmatic_algebras.py` as "modules over R with a bilinear
  multiplication."
- `AssociativeAlgebras(R)` = magmatic algebras with associative multiplication,
  not necessarily unital. Verified in Sage source
  `sage/categories/associative_algebras.py` as
  `MagmaticAlgebras(R).Associative()`.
- `Algebras(R)` = associative unital endpoint. Verified in Sage source
  `sage/categories/algebras.py`.
- The subcategory chain `Magmatic → Associative → Algebras(Unital)` preserves
  mathematical inclusion. Methods placed at the highest well-defined category
  follow the spec's own placement rule.

**Free construction routing mathematically sound:**

- `Sets() → Algebras(R).Constructors().free_algebra_from_set(S)` — the free
  associative unital algebra on generators. Correct: the free R-algebra on a set
  has no pre-existing algebraic relations, so the result is associative and unital.
- `Magmas() → MagmaticAlgebras(R).Constructors().free_algebra_from_magma(S)` —
  bilinear extension of a magma operation yields a non-associative, non-unital
  algebra. Correct routing to weakest category whose objects satisfy the laws.
- `Semigroups() → AssociativeAlgebras(R).Constructors().free_algebra_from_semigroup(S)` —
  semigroup algebra is associative but not necessarily unital. Correct.
- `Monoids()/Groups() → Algebras(R).Constructors().free_algebra_from_monoid/group(S)` —
  monoid/group algebras include the unit element. Correct.
- Additive variants follow the same pattern with additively written operations.

**Multiplication tensor constructor:**

- `from_multiplication_tensor(multiplication=mu)` where `mu` is a tensor in
  `T_R(M)[1, 2]`. A bilinear map M×M→M corresponds to structure constants
  c^k_{i,j} with one upper index (output) and two lower indices (inputs). The
  tensor type (1,2) correctly represents this data. The constructor delegates
  coordinate-to-tensor conversion to `TensorAlgebraComponents(R).Constructors()`,
  which is the correct separation of concerns.
- The implementation note (rows 290-302) accurately records that Sage's
  `FiniteDimensionalAlgebra` constructor is field-only and that ring-valued table
  algebras require separate hypotheses. This is correct: Sage's finite-dimensional
  algebra algorithms (radical, Cartan, Peirce) assume base field properties.

**Plain-set Sage algebra correctly routed:**

- Sage's `S.algebra(R)` for plain `Sets()` is correctly identified as a free
  module construction (`CombinatorialFreeModule`), not an algebra construction.
  The spec routes this to `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)`,
  preserving Sage functionality without admitting the Sage name as algebra
  vocabulary.

### Gate 4: Nonmathematical Rejection — PASS

**Status: PASS**

**Correct rejections with evidence:**

- `has_standard_involution()` — rejected from general `Algebras(R)`. Sage source
  confirms it is quaternion-specific (uses `conjugate` attribute, only
  QuaternionAlgebra examples work; FreeAlgebra raises NotImplementedError).
  Rejection grounded, decision card `[[DECISION-ALGEBRA-STANDARD-INVOLUTION-OWNER]]`
  created.
- `ElementMethods._div_()` (underscored helper) — correctly classified as runtime
  interop, not a public method.
- `product_on_basis(i, j)` — correctly classified as implementation hook for
  element multiplication; public surface is MagmaticAlgebraElement.__mul__.
- `_product_from_product_on_basis_multiply()` — correctly classified as
  bilinear extension implementation detail.
- `to_matrix()` / `on_left_matrix()` — raw matrices classified as
  representation/interop data; public surface should return morphisms or module
  maps.
- Sage `category=` keyword and option bags (`*args, **opts`) — correctly excluded
  from public API in `subalgebra()`, `ideal_submodule()`, `principal_ideal()`.
- `AlgebraModules(A)` — correctly routed to modules subtree, not admitted as
  algebra method.
- FreeAlgebra factory internals (`create_key`, `_repr_`, `_coerce_map_from_`,
  `construction()`, `AssociativeFunctor`) — correctly classified as
  constructor/runtime/display/private interop.
- Concrete table parent surface (`table()`, `left_table()`, `base_extend()`,
  `_Hom_()`, `is_associative()`, `is_commutative()`, `is_unitary()`) — correctly
  classified as interop and predicate evidence, with public construction routed
  through multiplication tensors.
- `one_basis()` / `one_from_cartesian_product_of_one_basis()` — correctly
  classified as interop data; public unit surface is `one() -> AlgebraElement`.

### Gate 5: Ambiguity Routing — PARTIAL PASS

**Status: PARTIAL PASS (1 deficiency)**

**Resolved ambiguity routing:**

- `has_standard_involution` — explicitly routed to decision card
  `[[DECISION-ALGEBRA-STANDARD-INVOLUTION-OWNER]]`. Resolution: reject from general
  Algebras; future admission requires algebra-with-involution or quaternion-algebra
  refinement. Adequate.
- Hopf/coalgebra structure (`coproduct_on_basis`, antipode, counit) — explicitly
  routed to "future Hopf/coalgebra category refinement." Adequate for current spec
  scope.
- `AlgebraModules(A)` — explicitly routed to modules subtree. Adequate.

**Deficiency — missing decision/task card reference:**

- `FiniteDimensionalAlgebrasWithBasis.Cellular` — the spec states this "should
  become `Algebras(R).FiniteDimensional().WithBasis().Cellular()` after a tracked
  source-grounding decision/task" (row 118), but no `[[DECISION-...]]` or
  `[[TASK-...]]` card ID is provided. This is an unresolved ambiguity without
  explicit routing.
  **Evidence:** No `[[DECISION-CELLULAR-...]]` or `[[TASK-CELLULAR-...]]` appears
  anywhere in the spec body.
  **Severity:** Medium. The Cellular algebra subcategory is a genuine mathematical
  refinement requiring explicit tracking.

### Gate 6: Obligation Preservation — PASS

**Status: PASS**

**No weakening without grounded replacement:**

- `center_basis()` → `center() -> Algebra` — obligation preserved at higher
  mathematical level. The center algebra carries its own basis when basis data is
  present. No weakening.
- `radical_basis()` → `radical() -> AlgebraIdeal` — obligation elevated from
  bare basis list to ideal structure. The ideal interface preserves `ambient()`,
  `ambient_module()`, `inclusion()`. No weakening.
- `derivations_basis()` → `derivations() -> Der(A)` — obligation elevated to
  the derivation module with Lie bracket structure. Basis recoverable when basis
  data present. No weakening.
- `ideal_submodule(gens, side='left', ...)` → `left_ideal(generators)`,
  `right_ideal(generators)`, `two_sided_ideal(generators)` — obligation preserved
  with cleaner, type-safe naming. No weakening.
- `subalgebra(gens, category=None, *args, **opts)` → `subalgebra(generators)` —
  obligation preserved with option bag removed. No weakening.
- `principal_ideal(a, side='left', ...)` → `principal_left_ideal(generator)`,
  etc. — obligation preserved. No weakening.
- Plain-set Sage `S.algebra(R)` → `S.free_module(R)` — Sage functionality
  preserved through correct routing to module constructor. The true free algebra
  on a set is provided by `S.free_algebra(R)`. No loss of capability.
- `annihilator_basis(...)` → `annihilator(...) -> AlgebraIdeal` — obligation
  preserved at ideal level with side predicates. No weakening.
- Construction categories (Quotients, Subobjects, CartesianProducts,
  TensorProducts, DualObjects) — all preserved at `Algebras(R).<Construction>()`.
  No weakening.

### Overall Recommendation: REVISE

The spec has strong mathematical grounding and correct category hierarchy, but
requires revision before advancing to implementation:

1. **REQUIRED (Gate 2):** Add reconciliation rows for `semisimple_quotient()` and
   `Supercommutative()`, or add explicit routing notes explaining why they are out
   of scope.
2. **REQUIRED (Gate 5):** Add an explicit `[[DECISION-...]]` or `[[TASK-...]]`
   reference for the Cellular algebra subcategory surface.
3. **RECOMMENDED (Gate 1):** Correct the Source Coverage Ledger's HTML doc path
   claims — either remove them or qualify them as "named by inventory, not filesystem-verified."
4. **RECOMMENDED (Gate 2):** Update the `radical_basis()` reconciliation row to
   explicitly note that Sage also has a separate `radical()` method, and that both
   are handled by the `radical() -> AlgebraIdeal` project surface.
