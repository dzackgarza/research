# Preamble organization assessment

## Current organization work

[TODO-WORKSTREAMS.md](TODO-WORKSTREAMS.md) owns the parallel schedule, shared-file boundaries, active reservations, and current progress.
Consolidation work claims the common owner and its affected consumers through that board.

[TODO-PRIORITIES.md](TODO-PRIORITIES.md#how-much-category-theory-to-implement-here) owns the criteria for work before the `sage-categories` transfer.
Apply the findings below to the module, affine-local algebra, and general scheme constructions first.
Recheck each finding at its live owner; the assessment records an earlier source tree.
The current algebra-to-geometry assessment is [PORT_TODO.md §8.4](PORT_TODO.md#84-commutative-algebra-foundation-required-by-scheme-theory).
Its construction traces identify the immediate consolidation work.

The useful unit of consolidation is one mathematical responsibility and its dependent constructions.
An algebra should obtain module operations from its underlying module; geometric constructions should use the resulting algebra and module maps.
Affine charts, restrictions, and stalks must return objects in that same algebraic subtree.
Local computations dispatch through their categories; restriction and gluing maps assemble the geometric result.
Sheaves of modules and algebras reuse these local operations, with their compatibility data owned at the sheaf level.
Global invariants retain their own hypotheses and algorithms, including the topology needed for singular cohomology.
Fix the shared construction path when this reuse requires initialized inherited state.
The current `owned_category.py` adapter makes implementation classes available through the category inheritance chain.
Treat repairs to that common path according to the consumer they enable and the duplication they remove.

- [ ] Consolidate repeated mathematical operations at the owner used by the active geometry construction.
- [ ] Connect ring quotients and presented algebra quotients through their scalar maps and shared presentation operations.
  Nested subschemes, differential modules, and fibers must consume the same relations.
- [ ] Consolidate localization, quotient, tensor, and presentation calculations across affine schemes, stalks, sheaves, and cover algebras.
  Extend the existing localization functor and transported module presentations with the required exact local algorithms.
- [ ] Unify the existing finite G-set and finitely presented group-module action constructions at the common categorical owner.
  Extend it to schemes and their invariants with the required morphisms and computational regimes.
- [ ] Realize toric character modules, divisor groups, and cohomology pairings through existing module and formed-module categories.
- [ ] Make each required underlying-structure functor explicit on objects and morphisms, with the correct initialized image.
- [ ] Keep framework-specific initialization and class assembly within the existing common runtime boundaries.
- [ ] Use explicit functor application where it gives correct shared implementation before automatic threading is available.
- [ ] Organize the active subsystem around its defining data, mathematical maps, algorithms, and private engine realizations.
- [ ] Transfer the subsystem to framework leaves when its required constructors and inherited operations are available.

Mathematical definitions, algorithm placement, exact engine computations, and coherent dependency organization survive the transfer.
General compiler and functor-classification mechanisms belong to the replacement framework.
Broad package, annotation, and collection sweeps follow the surviving interfaces.

## Earlier assessment

The measurements, source locations, and proposed repairs below describe the tree at the time of assessment.
Use them to locate a responsibility for inspection. Current work selection is defined above and in `TODO-PRIORITIES.md`.

<details>
<summary>Source assessment and mathematical consolidation examples</summary>

The current live tree at `src/dzack_research/preamble` is already a medium-sized mathematical software system, not a “preamble” in the usual sense.

| Metric | Current tree |
|---|---:|
| Python modules | 203 |
| Physical source lines | 65,020 |
| Code lines | 50,334 |
| Source size | ~2.37 MB |
| Directories | 25 |
| Modules under `categories/` | 182 / 203 |
| Lines under `categories/` | 58,810 / 65,020 = 90.4% |
| Functions | 5,609 |
| Classes | 887 |
| Median file size | 201 lines |
| Files ≥500 lines | 38 |
| Files ≥1,000 lines | 15 |
| Largest file | `categories/lattices.py`, 2,297 lines |
| Preamble-related test files | 63 |
| Test functions | 424 |
| Test LOC | 10,322 |
| Approx. `preamble.all` public names | 748 |
| Currently changed source files | 139 / 203 = 68.5% |

The largest domains by physical LOC are:

- `categories/modules/`: 45 files, 15,990 lines
- flat `categories/*.py`: 15 files, 7,929 lines
- `categories/algebras/`: 22 files, 7,020 lines
- `categories/functors/`: 25 files, 5,926 lines
- `categories/group/`: 21 files, 5,792 lines
- `categories/rings/`: 9 files, 4,186 lines
- `categories/sets/`: 15 files, 3,818 lines
- `categories/abstract_categories/`: 10 files, 3,807 lines

So the nominal package decomposition is fairly good. Most files are also not individually pathological: median function length is 4 lines, 90th percentile 19, and the simple cyclomatic-complexity estimate has median 1, 95th percentile 7. Only 29 functions reached complexity ≥20. The difficulty is therefore much more architectural than “everything consists of giant spaghetti functions.”

The current organization score is about **60/100**.

The largest deduction is dependency structure. The repository now explicitly says in `ARC-11` that package `__init__.py` aggregators must be dependency leaves, yet the actual tree has **530 imports through package aggregators in 135 ordinary source files**. The largest offenders are:

- `categories.rings`: 179 import sites across 98 files
- `categories.sets`: 149 across 78
- `categories.modules`: 87 across 39
- `tensors`: 35 across 27
- `abstract_categories`: 29 across 22
- `categories.algebras`: 28 across 17

This is not merely theoretical. The top-level import graph is acyclic, but **1,378 of 2,840 import statements—48.5%—are function/local imports**. Once those latent dependencies are included, the internal graph has roughly 1,200 edges and one SCC containing **133 modules**. Even after completely removing `__init__.py` modules from the graph, the largest SCC still contains **87 modules**.

That is the principal complexity problem: deferred imports are currently acting as a cycle-breaking mechanism. The filesystem looks layered, while the semantic dependency graph is substantially entangled. It also explains why import-order/coherence problems can appear in surprising places.

The second major issue is the unresolved collection/finiteness architecture. This is already recorded explicitly in `TODO.md`, so it is not inference from grep statistics. The remediation queue spans the owned ordered/enumerated-set spine, framings, Cartesian products, biproducts, tensor/Hom, symmetric/exterior/divided powers, algebra generators, connections, forms, submodules, group/lattice orbits, discriminant objects, Coxeter data, tensors, schemes, and Galois constructions. The source currently contains 827 AST-level `tuple(...)` calls and 58 `list(...)` calls. Those counts are not themselves 885 bugs—backend serialization can legitimately account for some—but they show the scale of the required audit. The fact that one representation mistake propagates across that many theories is itself evidence that the collection abstraction sits too low-level or was introduced too late.

Third, several files/classes have become domain monoliths. The notable cases are:

- `categories/lattices.py`: 2,297 lines; `Lattices` class spans 1,918 lines and its `ParentMethods` 1,576.
- `categories/modules/framed/finitely_generated/finitely_presented_modules.py`: 1,576 lines.
- `tensors/tensor.py`: 1,568.
- `categories/rings/rings.py`: 1,450.
- `categories/modules/framed/formed/torsion_form_modules.py`: 1,376.
- `categories/group/groups.py`: 1,332.
- `categories/modules/module_morphisms/module_morphisms.py`: 1,268.
- `categories/_lattice.py`: 1,261.
- `categories/lattice_morphisms.py`: 1,251.
- `categories/rings/commutative_algebra.py`: 1,237.

This is not primarily a function-complexity issue; it is responsibility density. `lattices.py`, for example, contains 105 nested imports alone. A class spanning ~1,900 lines means Sage-style `ParentMethods` organization has effectively become a second module system embedded inside Python classes.

There is also an obvious asymmetry in filesystem organization: the lattice ecosystem is still largely spread across the flat `categories/` root—`_lattice`, `lattices`, `lattice_morphisms`, `lattice_engines`, `lattice_properties`, `definite_lattices`, `rational_lattices`, `root_lattices`, `orthogonal_quotients`, `isotropic_orbits`, `vector_orbits`, `coxeter_diagrams`, etc.—whereas modules, algebras, groups, rings, and sets have dedicated subtrees. The flat root alone is nearly 8,000 lines. A `categories/lattices/` subtree would reflect the actual scale much better.

The huge session namespace is a lesser issue. `all.py` is 817 lines and exposes roughly **748 public names**. That is defensible given the deliberate “closed mathematical universe” model, and importantly ordinary internal source does not appear to import through `preamble.all`. So the size of `all.py` itself is not an architectural failure. The corresponding package aggregators, however, are currently being used internally, contrary to the intended architecture.

On the positive side, the semantic directory decomposition is strong, names generally correspond to actual mathematical theories/constructions, the project has a substantial test suite—424 preamble tests over 63 files—and complexity is not dominated by long procedural algorithms. The architecture documents are also now quite explicit about the intended invariants. The problem is that the implementation has not yet converged to those invariants.

A rough scoring decomposition is:

| Aspect | Score |
|---|---:|
| Mathematical/domain decomposition | 17/20 |
| Dependency architecture | 5/25 |
| Representation/abstraction coherence | 10/20 |
| File/class granularity | 10/15 |
| Public API/discoverability | 8/10 |
| Tests/maintenance structure | 9/10 |
| **Total** | **59/100** |

The tree is therefore **well-conceived but currently strongly coupled**. The highest-value structural remediation is not splitting arbitrary large files. It is first making `ARC-11` true—eliminating aggregator dependencies and exposing the real DAG of defining modules—while completing the owned collection/finiteness spine. Once those two are repaired, the remaining large-file/package boundaries should become substantially easier to determine from actual mathematical dependency boundaries rather than cosmetic LOC thresholds.

Yes. The main problem is not ordinary Python ugliness. The code is comparatively clean at the statement level; the serious slop is architectural duplication and failure to cash out the mathematical abstractions the tree has already built.

I audited the current dirty tree, excluding the collection/finiteness problems already in `TODO.md` except where they expose a separate abstraction failure.

A useful headline is:

| Layer | Assessment |
|---|---:|
| Ordinary Python idiom | ~85/100 |
| DRY / reuse | ~55/100 |
| Use of mathematical abstractions | ~45/100 |
| Separation of mathematics from engineering | ~45/100 |

Ruff finds only 44 ordinary simplification/idiom issues over ~65K source lines. So this is emphatically not a codebase full of trivial Python mistakes. The expensive slop is deeper.

### 1. Generic categorical constructions are implemented as a central switchboard — severe

`categories/abstract_categories/constructions.py:11-194` has generic names such as

`TensorProduct`, `Biproduct`, `Product`, `Coproduct`, `Pushout`, `FiberProduct`, `Kernel`, `Cokernel`

but their implementations explicitly import and branch over modules, algebras, sets, and schemes.

For example, `Product` asks whether the objects are commutative algebras, then modules, then sets. `FiberProduct` explicitly tests for `SchemeMorphism`. `Kernel` explicitly recognizes modules.

`abstract_categories/functors.py:385-443` repeats this problem when constructing product/coproduct morphisms: it explicitly distinguishes modules from sets.

This is backwards. The abstract layer should not know the list of concrete mathematical theories below it. The relevant category/Hom/category-construction should provide its product/kernel/tensor implementation, and the generic operation should delegate.

This is probably the single clearest example of “mathematically sensible API turning into engineering switchboard code.”

### 2. Type-(1,1) tensors still implement a second matrix/linear-map system — severe

The newly added `categories/matrices.py` gets the ontology right:

> a matrix is the existing `Hom_R(F_R(S), F_R(T))`

and `CONTRIBUTING.md` explicitly says that a linear map matrix must not be represented by `tensor.matrix(...)`.

But `tensors/tensor.py` still has a substantial legacy linear-map API on tensors:

- `determinant`
- `rank`
- `solve_right`
- `stack`
- `trace`
- `kernel_tensor`
- `left_kernel_tensor`
- `row`
- `transpose`
- `inverse`
- `inverse_tensor`

Those methods alone occupy roughly 145 lines, before counting the corresponding branches in the 150-line `_CoordinateTensor.__mul__` and surrounding matrix-specialized machinery.

Some of them now literally duplicate methods in `categories/matrices.py`: rows, transpose, trace, determinant, etc.

This is a direct ARC-09/ARC-10/API-02 violation left over from the old representation. A genuine tensor may have type `(1,1)`, but that does not make it the canonical matrix carrier. Linear-system/kernel/matrix-ring operations should be on the Hom object. Tensor operations should remain tensor operations.

This should delete a meaningful chunk of `tensor.py`, not merely reorganize it.

### 3. `forms/forms.py` is explicitly an obsolete workaround — severe

Its module docstring currently says:

> “The active module layer does not materialize a general tensor-product parent yet…”

But it now does: `modules/tensor_products.py` contains `TensorProductModules`, the selected universal bilinear map, and the induced morphism out of a tensor product.

Consequently `forms/forms.py` has retained a parallel homemade Hom hierarchy after its stated reason for existence ceased to be true:

- `_FormSpace`
- `BilinearFormSpace`
- `PairingSpace`
- `BilinearFormMorphism`
- `PairingMorphism`
- three separate global caches
- custom evaluation
- custom extensional equality
- custom pullback
- custom Gram-array representation

Yet the file itself correctly states mathematically that

\[
\operatorname{Pairings}(X,Y;W)
=\operatorname{Hom}_R(X\otimes_RY,W).
\]

For represented tensor products, that should be literal.

Likewise quadratic maps now have `DividedSquare`/`Gamma^2` infrastructure. The quadratic layer should be organized through that universal object rather than maintaining yet another parallel map representation.

There can still be a more general callable pairing abstraction where the tensor product genuinely cannot yet be materialized, but the represented finite cases should no longer have a second Hom carrier.

### 4. `Adjunction` requires four equivalent pieces of mathematical data independently — severe DRY failure

`functors/core.py::Adjunction` requires subclasses to implement all four:

- `unit`
- `counit`
- `hom_set_isomorphism_forward`
- `hom_set_isomorphism_inverse`

Twenty-one adjunction classes implement the entire quartet independently. Those methods currently occupy **899 source lines**. Forward/inverse Hom bijections alone occupy about **615 lines**.

This is unnecessary mathematical duplication.

Given \(F\dashv U\), unit \(\eta\), and counit \(\epsilon\), the Hom bijection is forced:

\[
\Phi(f)=U(f)\circ\eta_A,\qquad
\Phi^{-1}(g)=\epsilon_B\circ F(g).
\]

Indeed,
\[
\Phi^{-1}\Phi(f)
=\epsilon_B\circ FU(f)\circ F\eta_A
=f\circ\epsilon_{FA}\circ F\eta_A=f
\]
by naturality of \(\epsilon\) and the first triangle identity. Similarly
\[
\Phi\Phi^{-1}(g)
=U\epsilon_B\circ UF(g)\circ\eta_A
=U\epsilon_B\circ\eta_{UB}\circ g=g
\]
by naturality of \(\eta\) and the second triangle identity.

So the abstraction should choose one equivalent presentation of an adjunction and derive the rest. Requiring four independently implemented versions creates hundreds of lines whose primary job is to stay mutually coherent.

This is exactly the kind of boilerplate that a mathematically designed API should eliminate.

### 5. Functor provenance is being recorded with arbitrary hidden attributes despite already having a functor-image abstraction

There are **676 `_preamble_*` references**, involving **171 distinct names across 69 files**. There are 260 assignment sites for 139 distinct attributes.

Not all of this is bad—selected mathematical structure has to live somewhere—but a particularly clear bad subset is functor provenance.

Examples include:

- `_preamble_trivial_g_set_source_set`
- `_preamble_free_g_set_source_set`
- `_preamble_cofree_g_set_source_set`
- `_preamble_scalar_extension_source_module`
- `_preamble_localization_source_module`
- `_preamble_scalar_extension_source_group_module`
- `_preamble_restriction_source_group_module`
- `_preamble_induction_source_group_module`
- `_preamble_coinduction_source_group_module`
- `_preamble_scalar_extension_source_algebra`

The functor code then contains bespoke `source_set()`, `source_algebra()`, `original_group_module()`, etc. that recover these attributes.

But `Functor` already has an object-image cache, and the tree already has `ImageOfFunctor` / `FunctorImageObject`, whose entire mathematical purpose is “an image equipped with a chosen preimage.”

So there are currently at least three mechanisms for essentially the same concern:

1. the functor's image cache;
2. the formal `ImageOfFunctor` construction;
3. arbitrary attributes attached to output objects.

That should collapse to one coherent mechanism.

### 6. Runtime refinement has become a second object system

`refine.py` is only ~110 lines, but it is extraordinarily consequential. It:

- walks category superclasses and their MROs;
- manufactures dynamic classes;
- assigns `parent.__class__`;
- rebuilds `parent.element_class`;
- assigns `morphism.__class__`.

There are **128 live `refine(...)` call sites**.

Some centralized workaround is probably unavoidable if Sage's category MRO cannot satisfy the owned graph's semantics. So `refine.py` itself is not automatically bad code.

The problem is how extensively it is being used to manufacture mathematical state incrementally. For example, direct-sum decompositions can refine already-existing objects after asking for a decomposition; rings acquire canonical module/algebra structure through later mutations; scheme category membership is accumulated in hidden fields.

At that point the runtime class of an object is partly a history of which operations have happened to it. That is difficult to reason about mathematically and difficult to debug as Python.

The desired endpoint should be stable implementation classes plus category refinement for genuine properties/structures—not refinement as general-purpose object construction.

### 7. Ring structure is currently import-order-dependent

`categories/rings/rings.py::_refine_canonical_self_module_and_algebra` is especially concerning.

`_own_ring()` attempts to install the canonical \(R\)-module and \(R\)-algebra structures on \(R\). But the installation is guarded by:

- `_preamble_self_structures_done`
- `_preamble_self_structures_in_progress`
- imports of module/algebra packages inside the operation
- `except ImportError: return ring`

The docstring explicitly says refinement may be “deferred until the next lookup”.

So asking for the same mathematical ring at different points during package initialization can mutate its available categorical structure.

The mathematical fact “\(R\) is canonically an \(R\)-module and \(R\)-algebra” should not be a side effect of eventually getting far enough through Python's import graph.

This is a major source of inscrutable engineering.

### 8. Scheme code has accumulated a substantial parallel object/provenance system

`categories/schemes/schemes.py` is one of the clearest engineering thickets.

It contains:

- an identity cache `_SCHEME_MORPHISM_WRAPPERS`;
- a `SchemeMorphism` wrapper around native Sage morphisms;
- separate domain/codomain overrides;
- native unwrap/rewrap logic;
- `_preamble_coordinate_algebra_morphism`;
- `_preamble_scheme_base_ring`;
- `_preamble_scheme_category_types`;
- manually attached identity and structure morphisms;
- special product-projective point behavior;
- affine-coordinate special cases.

In particular, `Spec` is mathematically a contravariant functor, but the implementation is primarily a cached constructor plus side-channel fields attaching the contravariant algebra morphism afterward.

This should converge toward an actual `Spec` functor and ordinary scheme Hom objects whose coordinate-ring pullback is intrinsic data. Products/fiber products should then use the generic cone/product machinery rather than accumulating more scheme-specific object metadata.

I would treat the scheme layer as one of the largest local cleanup targets.

### 9. Abstract morphism equality knows about concrete theories

`abstract_categories/arrow_categories.py::_morphisms_agree` is an abstraction inversion.

The supposedly abstract equality routine contains special cases for:

- commutative squares;
- scheme coordinate pullbacks;
- native Sage scheme identities;
- finite enumerated sets;
- finitely generated groups;
- framed modules.

It even imports groups/modules to decide how two abstract arrows should be compared.

Equality/extensionality belongs to the relevant Hom category. The arrow-category layer should ask whether its component morphisms are equal, not reproduce the theorem “maps from this kind of object are determined by these generators.”

This function should become tiny if Hom objects own equality correctly.

### 10. `PowerAlgebra` reimplements `GradedDirectSumModule`

This is an unusually clean DRY example.

`GradedDirectSumElement` is 83 lines. `PowerAlgebraElement` is 87 lines. They repeat almost verbatim:

- component normalization;
- `homogeneous_components`;
- `homogeneous_component`;
- homogeneity/degree;
- monomial coefficients;
- addition;
- negation;
- scalar multiplication;
- equality;
- display.

The parents also repeat `module_generating_set`, `module_generator`, `linear_combination`, component constructors, zero, and scalar multiplication.

And `power_algebras.py` itself says the algebra is assembled as the direct sum of its graded pieces.

The correct organization seems quite direct: use the existing graded direct sum as the additive/module carrier and refine it with multiplication/unit/free-algebra structure. Do not implement another finite-support graded sum.

This is probably a >100 LOC deletion by itself.

### 11. Group-module code contains multiple conspicuous parallel implementations

Several separate issues occur here.

`GroupModules`, `FinitelyGeneratedFreeGroupModules`, `FinitelyPresentedGroupModules`, and `GroupLattices` all independently implement essentially the same `(base_ring, group)` category canonicalization and storage. There is already `OwnedCategoryOverBaseRing`; what is missing is the analogous common parameterized category base for “over \(R\), acted on by \(G\).”

`GroupModuleHomset` and `GradedModuleHomset` then copy **25 method assignments** directly from `ModuleHomset`, e.g.

`base_ring = ModuleHomset.base_ring`,
`elementwise = ModuleHomset.elementwise`,
`evaluation = ModuleHomset.evaluation`, …

`GroupModuleHomset` even assigns `_element_constructor_` twice. This is manual inheritance disguised as assignment.

There is also a more substantial duplication: `GroupModules.ParentMethods.base_change()` already implements transport of the action under scalar extension, while `GroupModuleScalarExtensionFunctor._apply_object()` independently reconstructs essentially the same action-matrix transport. The functor should call the canonical mathematical operation, as `AlgebraScalarExtensionFunctor` already does.

### 12. Closed-universe code frequently distrusts its own categorical interfaces

There are 52 `hasattr(...)` sites, plus many `try/except AttributeError` capability probes.

Some are reasonable at backend ingress. Others are not.

For example `functors/group_scalar_change.py` defines:

```python id="nzm5vu"
def _unacted_module(group_module):
    try:
        return group_module.unacted_module()
    except AttributeError:
        return group_module
```

and analogous fallbacks for forgetting/equipping the action.

But this functor's domain is explicitly `GroupModules(...)`. If an operation requires chosen unacted-module/equip/forget data, then either that is part of the category's contract or the domain should be the finer category carrying that data. Silently switching semantics on `AttributeError` is a second, duck-typed type system beside the mathematical category graph.

This occurs elsewhere with rank/unrank, presentations, algebra-generation facilities, etc. The strongest cases should be replaced by category dispatch or explicit chosen-data categories.

### 13. Multi-step engine code still lives inside mathematical implementations

The worst example I found is

`modules/framed/finitely_generated/finitely_presented_modules.py::_singular_presentation_kernel`

at about **309 lines**, with estimated cyclomatic complexity **56**.

The mathematics is straightforward: form an augmented presentation, compute syzygies, compute the relations among the resulting kernel generators, and return the owned kernel/inclusion.

The Python implementation, however, handles all of the Singular matrix layout, row/column flattening, ring translation, augmented matrices, repeated syzygy marshaling, and lifting itself.

That is precisely the case covered by the repository's own `ENG-04`: multi-stage engine computations should execute natively in the engine when doing so removes cross-boundary orchestration.

The owned Python layer should state the mathematical input/output and reconstruct the owned kernel. The Singular routine should do the Singular calculation.

Similarly, `torsion_form_modules.py:862-987` directly performs GAP `Orbit` and `Stabilizer` calls and bespoke element conversion even though the tree now has a general G-set/action layer. This indicates the G-set API is missing generic orbit/stabilizer operations that special theories are then forced to reinvent.

### 14. `ContravariantFunctor` and `Bifunctor` duplicate ordinary `Functor`

`functors/core.py` separately implements:

- `Functor`
- `ContravariantFunctor`
- `Bifunctor`

Each has its own domains, codomain, object cache, endpoint validation, morphism validation, and call dispatch.

But the tree already has `OppositeCategory` and `ProductCategory`.

Mathematically,

\[
F:C^{op}\to D
\]

is just a functor, and

\[
F:C\times D\to E
\]

is just a functor.

A two-argument convenience call for a bifunctor is fine. Reimplementing the functor machinery is unnecessary. These should be thin interfaces over ordinary `Functor(OppositeCategory(C),D)` and `Functor(ProductCategory(C,D),E)`.

### 15. Cache policy is reinvented repeatedly

There are at least **15 named module-global dictionary caches**, including separate caches for:

- cohomology;
- divided squares;
- tensor products;
- module powers;
- fixed-size selections;
- three form-space types;
- power algebras;
- restricted graded algebras;
- Kähler differentials;
- de Rham algebras;
- cohomology algebras;
- sparse free algebras;
- underlying modules.

This is in addition to Sage `cached_function` / `cached_method` and the functor caches.

Identity-sensitive caching is genuinely needed in places. The slop is having each theory invent its own id-key/identity-check/lifetime pattern. One correct identity-memoization abstraction would remove boilerplate and make object-lifetime semantics reviewable in one place.

### 16. The enumerated symbolic-function classes are four copies of one class

`FourierCharacters`, `HermitePolynomials`, `LaurentMonomials`, and `SincTranslates` all repeat essentially the same `UniqueRepresentation, Parent` implementation:

- infinite cardinality;
- rank/unrank;
- membership by attempting `rank`;
- infinite `while True` enumeration;
- symbolic indexed element construction.

`function_sets.py` already contains `EnumeratedByNaturals`, `EnumeratedByIntegers`, and the index conversion/symbol helpers, but the abstraction stops one layer before eliminating the duplicated parent implementation.

This is a straightforward generic `IndexedSymbolSet`/indexed-function-set abstraction.

### 17. There is real non-idiomatic Python, but it is secondary

Assertions are **not** themselves a defect in this Sage research preamble.  Mathematical assertions are desirable executable statements of the proof context: finite-rank assumptions, nondegeneracy, category containment, parentage, shape compatibility, and identities should be stated loudly with informative `assert` statements.  Method placement follows **mathematical definability**, not the current algorithmic domain: `cardinality()` belongs to sets even when some represented sets have no current exact cardinality algorithm, and `is_nondegenerate()` belongs to formed modules even when some infinite/callable forms are not presently decidable.  Such general methods may implement the cases currently understood and assertion-gate the unhandled computational remainder.  The concrete defect in `Tensor.tensor_shape()` and `tensor_valence()` is stronger: `assert False` is the entire method body, so there is no implemented case at all.  A genuine abstract implementation contract uses Sage's `@abstract_method`; a method that is not mathematically defined on the broader category should not be visible there.  A final `assert False` (or `typing.assert_never` when the type partition is statically exhaustive) can be reasonable only as the fallback after real implemented cases.  Mathematical code should not use `NotImplementedError` or exception-driven fallback as an alternate output.

There is an important distinction between the mathematical domain of an operation and the domain of the current algorithm.  If an operation itself belongs only to a narrower category, put the method there.  If the operation is mathematically general but the current implementation requires stronger hypotheses, keep it at the correct mathematical owner and assert those hypotheses at the head of the implementation so the remainder is total under an explicit finite set of assumptions.

There are also the 44 Ruff simplification findings and the duplicate `_element_constructor_` assignment noted above. These are worth mechanically cleaning, but they are not where the complexity comes from.

`preamble/utilities.py` is a session-surface case, not dead-code evidence.  `lmap`, `lzip`, `to_var_names`, and `zipsum` may exist specifically as notebook/REPL conveniences and therefore need not have internal callers.  Their value is judged by session ergonomics and deliberate exposure through `preamble.all`, not by `src/` call counts.  Internal-unusedness must be treated cautiously throughout this repository because the preamble itself is a user-facing interactive environment.

### Expected payoff

I would not attack this as “make large files smaller.” The likely high-value order is:

1. make categorical construction dispatch genuinely categorical;
2. eliminate matrix-as-tensor operations;
3. collapse forms onto tensor-product/DividedSquare Hom objects;
4. make `Adjunction` derive redundant data;
5. centralize functor-image provenance;
6. reduce dynamic refinement/state mutation;
7. normalize scheme/Spec architecture;
8. deduplicate graded direct sums, group-category infrastructure, Homsets, and identity caches;
9. push multi-step CAS calculations behind proper engine boundaries;
10. then run the mechanical Python cleanup.

There is comfortably **more than 1,000 LOC of genuine deletion/consolidation available without reducing mathematical functionality**, before counting the potentially much larger scheme/refinement cleanup. The strongest evidence is the 615 lines of independently implemented adjunction transposes, the duplicated graded-direct-sum carriers, obsolete form Hom hierarchy, duplicated tensor/matrix operations, construction switchboards, group-module parallel implementations, and repeated provenance/cache machinery.

So I would characterize the tree as **not Python-sloppy, but abstraction-sloppy**: many individual functions are perfectly reasonable implementations of things that should not need an individual implementation at all. That is the dominant source of both LOC and inscrutability.

No files were changed during this audit.

## Finitary and coordinate overfitting audit

A separate high-value failure mode is **premature semantic lowering**: mathematical code descends to finite enumeration, chosen coordinates, raw matrix rows/columns, or exhaustive carrier checks before the surrounding theorem requires that representation.  This is more serious than a local `tuple(...)` style violation because it makes finiteness contagious: future infinite/lazy/theorem-backed implementations then require rewriting every consumer that learned the coordinate representation.

The static complexity audit currently finds **106 direct `list`/`tuple` materializations of named mathematical collections**, **49 explicit loops over named mathematical collections**, and **98 raw matrix/coordinate representation peeks** (`rows`, `columns`, `row`, `column`, `basis_matrix`, kernel matrices, flattened `list`, etc.).  These are review candidates, not automatic violations: finite CAS serialization is legitimate at a private backend boundary.  The defects are sites where the mathematical consumer itself depends on those representations.

High-confidence current cases:

1. **`categories/abstract_categories/functors.py::DiscreteCategory.objects` exhausts the object set.**  It returns `tuple(self(value) for value in self.object_set())` whenever the set is iterable.  The objects of a discrete category are the owned image of the underlying set and may be infinite.  `objects()` should return that owned/lazy set, not silently strengthen enumerability to finite exhaustibility.

2. **`categories/abstract_categories/direct_sum_objects.py::DirectSumDecomposition` represents the selected family as `tuple(summands)` and validates essentially only finite/binary cases.**  The selected decomposition should be an owned indexed family with its index set retained.  Binary/finite matrix verification is one computational specialization of the biproduct/direct-sum universal property, not the representation of the decomposition itself.

3. **`categories/divisors/divisor_groups.py::FormalDivisorGroup` confuses finite support with a finite prime-divisor set.**  It constructs `FreshFreeModuleOn(ring, finite_ordered_set(prime_divisors))`.  A formal divisor has finite support, but the group of formal divisors may be free on an infinite owned set of prime divisors.  The parent should retain the arbitrary prime-divisor set; each element carries finite support.

4. **`categories/modules/free_resolutions.py::FreeResolution.is_exact` proves exactness by comparing backend row modules.**  Exactness is the semantic statement `im(d_1) = ker(augmentation)` together with the surrounding zero/composition conditions.  `is_exact()` should ask image/kernel subobjects/Homs; their finite-free implementations may use row modules privately.  The current code bakes finite matrix realization into the theorem itself.

5. **`categories/modules/cochain_complexes.py::Cohomology` reconstructs `ker(d_n)/im(d_{n-1})` through raw lift matrices, kernel basis matrices, projected rows, coordinate vectors, and synthesized relation matrices.**  This is one of the strongest coordinate-overfitting sites.  Cohomology should be constructed from the already-owned kernel/image/subobject/quotient operations.  A finite-presentation backend may optimize the complete computation without exposing row orientation or basis choices to the cohomology layer.

6. **`categories/functors/subobject_images.py::_inverse_image_subobject` and `categories/modules/subobjects.py::intersection` state the correct universal property in comments and then implement it through matrix stacking and kernel rows.**  Inverse image and intersection are pullbacks of inclusions (or the corresponding additive kernel construction).  Construct the pullback/kernel subobject semantically and let finite-free Hom/subobject code choose the matrix algorithm.

7. **`categories/modules/group_modules/group_lattices.py::GroupLattice` verifies form preservation by assuming finite rank and finite group generation, materializing lattice generators, and checking every pair of generator images.**  The action should be a morphism `G -> Aut(L,b)` (or be checked in the formed-module automorphism Hom), with preservation of the form/correlation morphism owned there.  A finite Gram check may implement that Hom predicate, but the GroupLattice constructor should not acquire finiteness assumptions merely to validate structure.

8. **`categories/modules/group_modules/group_modules.py::module_invariants` / `module_coinvariants` make existence depend on chosen finite group generators.**  Invariants are the fixed-point/equalizer subobject of the action; coinvariants are the corresponding coequalizer/quotient.  Finite group generators give a finite algorithm, not the mathematical definition.  The action/G-set/module machinery should own the general construction and route to finite-generator computations where available.

9. **`categories/modules/general_modules.py::annihilator` uses exhaustive enumeration of the scalar ring and entire module.**  `Ann_R(M)` is structurally the ideal/kernel of the scalar-action morphism `R -> End(M)` (or the equivalent annihilator construction).  Exhaustive finite enumeration may be a fallback computational case, but it should not be the general architecture.  `_verify_module_laws_when_decidable` similarly performs exhaustive finite carrier/scalar law checking; useful as a diagnostic case, but the durable structure should come from the supplied additive/scalar morphisms and category contracts.

10. **`categories/modules/pure/finitely_generated/finitely_generated_modules.py::fiber_dimension` and `minimal_number_of_generators` manually specialize relation rows and compute backend matrix rank before falling back to the semantic fiber/residue module.**  Reverse the priority: construct `M(p)` / `M/mM` first and ask the resulting vector space for dimension.  Its represented finite implementation can use presentation-matrix rank internally.  This keeps localization, scalar extension, residue fields, and vector-space dimension as the reusable spine.

11. **Matrix-like tensor operations remain a concentrated semantic-lowering hazard.**  `tensors/tensor.py` still exposes stack/kernel/solve/inverse/row-style operations by lowering type-`(1,1)` tensors to engine matrices.  The canonical matrix carrier is the free-module Hom object.  In particular block operations should be expressed as morphisms between biproducts/direct sums from their component Homs, so a future infinite/formal block implementation changes the Hom backend rather than every consumer assembling row arrays.

12. **Many mathematically finite collections are still returned as Python tuples.**  Examples include definite-lattice root sets, lattice orbit representatives/stabilizer generators, Coxeter connected components, genus representatives, and divisor term/component families.  Even where a theorem guarantees finiteness, the result should normally be an owned finite set/ordered set/indexed family or lazy enumeration; finiteness is mathematical metadata, not a reason to replace the collection by a Python sequence.

The corrective architectural rule is: **mathematical consumers ask semantic questions; representation-specific code answers them.**  The intended layering is

```text
cohomology / exactness / action / geometry / subobject consumer
    -> kernel, image, quotient, pullback, Hom, product, dimension, action invariant, ...
        -> category/representation-specific algorithm
            -> finite coordinates / matrix / CAS backend when applicable
```

not

```text
mathematical consumer
    -> rows / columns / coordinate vectors / exhaustive enumeration
        -> reconstruct the semantic object manually
```

This is now also encoded in `CONTRIBUTING.md` policies `ARC-16`, `SET-04`, and `STY-91`–`STY-103`, and measured by `just preamble-complexity`.

## LLM-local-patch amplification: semantic API debt becomes numerical bloat

A recurring failure mode deserves separate treatment from ordinary finitary overfitting: an implementation task starts with a mathematically meaningful owned object, but the local patch immediately lowers it to coordinates because that is the shortest path visible to the agent. For example, a consumer receives `f : M -> N`, calls `f.matrix()`, computes a nullspace, rebuilds a module from basis rows, and manually manufactures an inclusion instead of calling or repairing `f.kernel()`. The local code may be correct in one finite-free case while duplicating the kernel construction, chosen-basis semantics, row/column conventions, backend selection, and subobject reconstruction.

This behavior amplifies when the semantic API is incomplete. An agent that finds `kernel()`, `pullback()`, `image()`, `cokernel()`, `dimension()`, block-Hom construction, or a structural predicate awkward or missing tends to patch around the gap rather than improve it. The first workaround becomes precedent; later consumers copy it; eventually every downstream theory contains its own finite-coordinate fragment. That is a major source of LOC bloat and gives infinite generalization a large blast radius.

The corrective architecture is the reverse. Mathematical consumers compose semantic operations; those semantic owners route among finite-coordinate, sparse/infinite, theorem-backed, or external-engine algorithms. Thus `is_primitive(i)` should read as `i.cokernel().is_torsion_free()`, not as a gcd/minor criterion in a lattice consumer. Exactness should compare `image()` and `kernel()` subobjects, not row modules. Cohomology should be `ker/im`, not an augmented-matrix program. If these semantic calls cannot yet support the requested feature, repairing them is part of the feature task rather than out-of-scope refactoring.

This is especially important for LLM-authored changes: minimizing the geographical size of the diff is not the objective. The review question is whether the new code would mostly disappear if the common semantic API were complete. If yes, strengthen that API first. `CONTRIBUTING.md` policies `ARC-17`, `DEV-13`, and `STY-104`--`STY-111` are authoritative for this failure mode.

</details>
