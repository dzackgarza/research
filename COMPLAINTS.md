# Foundational Gaps and Papercuts

Record unresolved issues observed anywhere in research or contribution work.
The primary subject is general mathematical machinery that should be available but is missing, incomplete, or bypassed in the owned language.
Concrete workflow papercuts also belong here.
This is neither a retrospective work log nor a list of hypothetical defects.

Use the [mathematical tracing method](CONTRIBUTING.md#mathematical-dependency-tracing) and the capture/lifecycle rule [`DEV-59`](CONTRIBUTING.md#dev-59-record-observed-foundational-gaps-and-papercuts).
State the mathematics before its implementation symptoms.
Extend an existing entry when another consumer exposes the same foundation.
Link execution details in [TODO.md](TODO.md); keep implementation ordering and active reservations there.
Remove resolved entries with evidence in the commit, retaining only unfinished needs and any required terminal verification.
Durable definitions and decisions belong at their mathematical declarations or in CONTRIBUTING, not solely here.

## Foundational Mathematics


I audited the current clean `main` at `1cc95d7b3e59` against the normative `CONTRIBUTING.md`, covering `src/dzack_research/preamble/**`, `preamble.all`, the canonical notebook, and the test harness.
I did not run Sage/tests because the current `TODO.md` explicitly pauses execution; this is a source-level architecture audit.
The generated megadoc is older than several current source files, so I did not treat its diagnostics as authoritative where the source had moved.

The preamble is still substantially nonconforming.
The violations I found are below.
For very large systematic families, I give exact occurrence counts and representative/source-defining sites rather than printing hundreds of essentially identical lines.

| Violation | Policies | Current evidence |
| --- | --- | --- |
| **2. Framing is still constructed backwards.** | `CON-11`, `OWN-03`, `ARC-20`, `STY-152` | `modules/pure/modules.py:2170–2185` defines a framed module by storing `module_generating_set` plus `module_generator_function`. Only later, `2207–2228`, does it manufacture the generator map and reconstruct `Free_R(S)` to obtain `framing_morphism()`. The required primary datum is instead the selected epi `Free_R(S) → M`. |
| **3. Descendants duplicate the framing/generator machinery instead of inheriting the one framing object.** | `OWN-14`, `STY-154`, `DEV-10` | There are **9 separate `module_generators()` definitions**: `lattices.py:1486`, `fractional_ideals.py:228`, presented modules `:819`, framed free modules `:398`, group modules `:555`, generic framed modules `:2199`, restricted-scalars `:2492`, matrix modules `:3264`, number fields `:663`. Presented modules similarly reconstruct their framing at `finitely_presented_modules.py:818–831`. |
| **4. Internal representation vocabulary leaks into the public mathematical view.** | `LEX-01`, `LEX-04` | Public generator displays are literally named `"Module-generator family"` (`modules.py:2204`), `"Free-module generator family"` (`framed_free_modules.py:403`), `"Presented-module generator family"` (`finitely_presented_modules.py:825`), `"Lattice-generator family"` (`lattices.py:1491`), `"Fractional-ideal generator family"` (`fractional_ideals.py:233`), etc. This is exactly the type-theoretic implementation leakage you identified: the user asked for module generators, not an `IndexedFamily` implementation concept. |
| **7. Runtime refinement remains a second object-construction mechanism.** | `ARC-13`, `STY-08`, `OWN-02`–`03` | There are **49 `refine(...)` call sites in 25 files**. Not every mathematically proved property refinement is forbidden, but construction still depends on mutable post-allocation placement. Concrete architectural examples include ring construction calling `refine(self, placements)` in `ring_foundation.py:1374–1405`, and `refine_scheme()` mutating `_preamble_scheme_*` state and calling `_refine_category_` at `schemes.py:908–926`. |
| **8. `NotImplementedError` is still a normal mathematical control path.** | `CAT-01`, `DEF-06`, `STY-48`, `DEV-11` | There are **449 direct `raise NotImplementedError` statements**; AST classification finds **212 public callables containing one**. `CAT-01` explicitly says "`NotImplementedError` is not a mathematical implementation strategy"; unsupported computational cases must end at the declared assertion-gated frontier. Major concentrations include `schemes.py` (45 direct raises), `algebras.py` (37), `commutative_algebra.py` (29), `modules.py` (20), `lattice_morphisms.py` (16), `groups.py` (15), `lattices.py` (14). |
| **9. Visible mathematical placeholder stubs remain.** | `STY-48`, `STY-160` | `tensor.py:312–315` implements `_index_ranks()` as unconditional `assert False`; `tensor.py:343–345` does the same for `tensor_valence()`. `profinite_groups.py:33–35` has an `@abstract_method(optional=True)` body containing `pass`, where `STY-160` explicitly requires the Sage abstract contract with `...`. |
| **10. Equivalent categorical data are still independently implemented.** | `ARC-14`, `STY-51`, `STY-54` | `abstract_categories/functors.py:47–93` maintains `ContravariantFunctor` machinery atop `Functor(C^op,D)`; `:96–169` does the same for `Bifunctor` atop a product category. `functors/core.py:421–480` makes `Adjunction` expose unit, counit, and both Hom transposes as independently implemented interfaces. These are exactly named as prohibited current-tree patterns in `CONTRIBUTING.md`. |
| **11. Group-module scalar extension has duplicate method/functor authority.** | `STY-54`, `OWN-09`, `OWN-14` | `group_modules.py:902–914` implements object-level `base_change` by transporting the action. `functors/group_scalar_change.py:42–79` separately implements `GroupModuleScalarExtensionFunctor`, whose object action calls that method but whose morphism transport has its own parallel machinery. The architecture still has two places understanding the construction. |
| **13. A substantial Singular algorithm is still orchestrated locally in Python.** | `ENG-01`–`03`, `STY-57`–`59`, `OWN-08` | `_singular_presentation_kernel` in `finitely_presented_modules.py:2240ff` performs a long sequence of matrix construction, coefficient lifting, Singular `modulo`, relation reconstruction, and lift recovery through roughly lines 2270–2415. This is the exact current-tree exemplar named by `CONTRIBUTING.md`: the maintained engine should own the coherent kernel computation behind one crossing. |
| **14. Torsion-form orbit/stabilizer computation bypasses the general action/G-set owner.** | `ENG-01`, `STY-40`–`42`, `BND-01`–`02` | `torsion_form_modules.py:540–584` hand-rolls subobject orbit traversal; `:1319–1381` directly invokes `libgap.Orbit`/`libgap.Stabilizer`. The guideline explicitly names this subtree as a current violation: orbit/stabilizer semantics belong to the owned action infrastructure, with GAP private beneath it. |
| **15. Generic imperative algorithms catalogued by the guide remain live.** | various `STY-*` | Examples still present include the nested bilinear accumulation in `forms.py:245–250`; multiplicative `_multiply_in_target` loops in both `free_algebras.py:1464–1468` and `sparse_free_algebras.py:634–638`; `_divided_product_coefficient` in `powers.py:584ff`, including the algebraically inert second `*=1` loop; the append/filter loop in `absolute_galois_group.py:697–708`; `setdefault(...).append(...)` in `finitely_presented_algebras.py:119`; and numerous `frontier`/`seen` bespoke traversals in torsion forms, orthogonal quotients, lattices and lattice morphisms. |
| **16. Public mathematical products are still returned as Python tuples.** | `CON-15`, `SET-01`, `CAT-08` | `CommutativeSquare.components()` returns `(left,right)` at `arrow_categories.py:68–69`; `NaturalTransformation.naturality_square()` returns a two-morphism tuple at `functors/core.py:414–418`; `TensorModule.index_modules()` returns a pair of families at `tensor.py:1548`, and `tensor_indices()` another pair at `1561`. `CON-15` expressly says a bare tuple never appears as a public mathematical return. |
| **17. The type surface systematically uses implementation-universal types instead of mathematical codomains.** | `LEX-12`–`LEX-15` | Current source contains **238 `-> Parent`**, **16 `-> Element`**, **1 `-> CategoryObject`**, and **6 `-> Any`** return annotations: **261 framework-universal return annotations**. `LEX-13` explicitly names `Parent`, `Element`, `SageObject`, and `CategoryObject` as empty types that assert nothing. Examples include `Functor.object_image -> Parent`, set `cardinality() -> Parent`, arbitrary `an_object() -> Parent`, and scheme methods returning `Any`. |
| **18. Public coordinate/storage escape hatches remain and are actively taught.** | `ARC-18`, `API-02`, `DEV-40` | Lattice elements expose `to_list`, `to_tuple`, `to_vector` at `lattices.py:3057–3077`; tensor elements expose raw `components()`/`list()` at `tensor.py:381–404`; ordinary `ModuleMorphism.matrix()` remains a public coordinate view at `module_morphisms.py:655ff`. Explicit coordinate views can be legitimate at a narrow framing boundary, but the notebook actively uses them as ordinary mathematical interaction, so the semantic firewall is not functioning. |
| **19. The canonical notebook violates the notebook/session rules.** | `NB-01`, `NB-03`, `NB-04`, `ARC-07`, `LEX-10`, `DEV-40` | Of 51 code cells, **30 are currently unexecuted**. A committed cell retains a `NotImplementedError` traceback at `preamble.ipynb:802–822`. Markdown at `:1214–1216` says the algebra “should look like” a polynomial ring instead of asserting the claim. `:1254` states the exact substitution behavior only in prose. Session code uses `.generators()` (`1227`, `1269`), `A.Hom(P)` (`1239`), positional `P.gen(i)` (`1241`), bare global `Hom(...)` (`1267`, `1290`), low-level `module_homset`/`TensorAlgebraOf`/`DividedPowerAlgebraOf` around `977–980`, and `.hom(...)` for Coxeter diagrams around `1097`. The heading “Coxeter diagrams as Sage parents and their morphisms” (`1080`) is also implementation-centered rather than a mathematical question (`NB-03`). |

Two additional points are worth separating from those violations.

First, some older catalogue examples in `CONTRIBUTING.md` have been repaired and should not be charged against the current tree.
In particular, the previous `PowerAlgebraElement`/`GradedDirectSumElement` duplication is no longer present in that old form, and the manual `GroupModuleHomset`/`GradedModuleHomset` method-grafting example has been replaced by a shared `_ModuleHomsetCommonMethods` implementation.
I excluded those.

Second, the generated `docs/preamble-megadoc.md` contains 92 `LEX-12` “not placed” entries, but the megadoc predates several current source edits.
Those 92 need regeneration before they can be counted as additional current violations; I did not inflate the audit with stale generated diagnostics.

The highest-priority architectural defects are therefore: **(1) remove the global operation language; (2) reconstruct framing around the selected epi itself rather than post-hoc generator metadata; (3) eliminate hidden provenance/refinement state; (4) replace the `NotImplementedError` computational model; (5) restore one categorical representation for functors/adjunctions/universal structures; and (6) repair the test/notebook surfaces so they actually enforce rather than conceal those decisions.**


### Categories declared into `Sets()` whose objects are not sets

`super_categories()` states that every object of the category is an object of those.
The `Sets()` group is the largest in the tree; `just category-graph by-supercategory` lists it, and `just category-graph audit` reports what is mechanically checkable about the graph (no name is declared as a supercategory without being defined, and there are no cycles among distinct categories).
Reading each member against the definition in its own docstring separates the group in two.

**Correct: sets with structure.**
`Magmas`, `AdditiveMagmas`, `EnumeratedSets`, `CountableSets`, `PartiallyOrderedSets`, `PowerSets`, `FinitePowerSets`, `FixedCardinalitySubsetSets`, `FunctionSets`, `FinitelySupportedFunctionSets`, `CartesianProductsOfSets`, `CoproductsOfSets`, `Homsets` ("Hom objects, which are sets").

**Incorrect: the object is not a set, and the category it belongs to is named by its own docstring.**

| Category | Its own definition | The category that should be declared | Source |
| --- | --- | --- | --- |
| `TopologicalManifolds` | "finite-dimensional topological manifolds" | topological spaces | `manifolds.py:151` |
| `LogPairs` | "pairs ``(X, Delta)`` of a variety and a chosen boundary divisor" | a scheme with a divisor | `schemes/log_pairs.py:22` |
| `HyperbolicSpaces` | "projectivizations of chosen positive-cone components" | the projectivization of a cone component | `hyperbolic_geometry.py:111` |
| `HyperbolicPolyhedra` | "projectivized rational polyhedral cones in a chosen hyperbolic space" | projectivized cones | `hyperbolic_geometry.py:161` |
| `PositiveConeComponents` | "chosen components of ``{x : q(x)>0}``" | a subspace of `L (x) RR` | `hyperbolic_geometry.py:26` |
| `ConvexPolytopes` | "rational convex polytopes in a chosen coordinate lattice" | convex bodies in `L (x) QQ` | `schemes/polytopes.py:117` |
| `RationalPolyhedralCones` | "rational polyhedral cones in a selected integral coordinate lattice" | convex cones in `L (x) QQ` | `polyhedral_cones.py:38` |
| `RegularPolytopes` | "finite spherical regular abstract polytopes named by Schlaefli symbols" | graded posets -- an abstract polytope is a poset, and `PartiallyOrderedSets` exists | `schemes/polytopes.py:37` |
| `CoxeterDiagrams` | "a symmetric matrix of vertex angles" | labelled graphs | `coxeter_diagrams.py:162` |
| `ProjectiveWeightedGraphs` | "finite graphs or digraphs with exact projective vertex and edge weights" | graphs and digraphs | `vinberg_invariants.py:62` |
| `VinbergInvariantMatrices` | "symmetric matrices of Vinberg invariants on a finite set of mirrors" | a matrix space over the coefficient ring | `vinberg_invariants.py:359` |
| `WeylChamberComplexes` | "locally finite chamber systems generated by simple reflections" | chamber systems | `chamber_complexes.py:50` |
| `CharacterSets` | "the owned sets ``Char(G)`` of ordinary characters of finite ``G``" | undecided: `Char(G)` carries a ring structure, and whether this category is of the sets or of the rings is a decision, not an oversight | `group/characters.py:32` |

**Categories the table asks for and the tree does not have.**
Topological spaces.
Graphs, digraphs, and labelled graphs.
Chamber systems.
Convex bodies and convex cones in a module over an ordered field.
The functor category and the opposite category both exist and are what the presheaf construction is built from, so that one is placement rather than new theory.

**Required end state.**
No category declares a supercategory its own definition contradicts.
Where the honest category is missing it is built; where it is not yet decided, `super_categories()` is left abstract so the category refuses to construct.
Scheduled as `geometric-space-placement` and `combinatorial-object-placement` in [TODO.md](TODO.md).

**Coverage boundary.**
Read from source: the declared graph, and each listed category's own class docstring.
No session was run.
The right-hand column states the category each docstring names; where building it requires a choice between several honest formulations, that choice is not made here.
Whether any consumer additionally depends on the false declaration, rather than merely carrying it, was not determined.

### Algebras are not constructed from their structure morphism

**Missing general mathematics.**
An \(R\)-algebra is an additive group \(A\) with a biadditive multiplication together with a ring morphism \(\rho\colon R\to Z(A)\) into its centroid, the additive endomorphisms commuting with left and right multiplication (Mathlib `CentroidHom`); for unital associative \(A\) the centroid is the centre.
Nothing else is assumed: unit, associativity and commutativity are axioms, and a Lie bracket is the multiplication of its algebra.
\(\rho\) constructs the underlying \(R\)-module, \(r\cdot a=\rho(r)(a)\), so the forgetful functor \(\mathbf{Alg}_R\to\mathbf{Mod}_R\) is the identity on that object; from an \(R\)-module \(M\) with bilinear \(m\), \(\rho\) is the scalar action of \(M\), which lands in the centroid because \(m\) is bilinear.

**Dependency path.**
One canonical constructor consumes \((A, \rho)\); every other route -- \((M, m)\), a group algebra, a centre, a quotient, a commutator Lie algebra, an engine-adopted ring, a free functor -- computes \(\rho\) from its own data and feeds it (CONTRIBUTING `CON-02`, `CON-06`; vault plan `PLAN-r-algebras-math-syntax-20260803`).

**Observed evidence.**
`Algebras(R)(M, m)` builds a second module and retains \(M\) with an identification map (`_ChosenAlgebraMultiplicationDatum`, `multiplication_source_module`, `from_multiplication_source`, `AlgebrasWithChosenMultiplication`; `algebras/algebras.py`), a parallel constructor with names that have no mathematical referent.
`_own_algebra` and `AlgebraStructureConstruction` hold a structure map as a side attribute of an engine ring, only for unital associative algebras.
`_OwnedAlgebraParent` and the engine free-algebra realization (`algebras/sparse_free_algebras.py`) are placed in `Modules(R)` by the `Algebras(R)` declaration without constructing a module; the realization hand-writes the module operations, and `FramedAlgebras.ParentMethods.cardinality` restates a set-level operation.
The algebra Hom asserts a finite module framing to decide multiplicativity instead of asking the module Hom and recording `Unknown` as the hypothesis on non-finitary data.
The same copy-and-identify shape stands at three more sites -- group modules (`forget_action_morphism`, `equip_action_morphism`), formed modules (`forget_form_morphism`, `equip_form_morphism`, `_form_module_construction`) and lattices (a stored `_module`, `forget_form_morphism`) -- and six `*_source_module` accessors name functor preimages by an implementation word.
How it entered: the algebra copy arrived in the bulk commit `4b1786db` of 2026-09-05, which adopted other workers' in-flight edits unchanged, and was extended by `0f4d809c` and `41712e5f`, neither with a body; the form-module copy arrived in `351f8c38`, body empty.  The data-subcategory pattern (`XWithChosenY`) was applied to the defining datum of the category, which manufactured two kinds of algebra object and the membership routing between them.
The private construction-datum classes (`_*Construction`, `_*Datum`; fifty-five in the tree) were not surveyed for the same shape; that survey is owed, and the count is not a verdict on any of them.
Filed as `CON-16` in CONTRIBUTING and as `structured-module-constructors-route-through-the-datum` in [TODO.md](TODO.md).

**Existing partial capability.**
`Modules(R)` constructs framed and presented modules; `Algebras(R)` and its axioms exist; the history of `functors/algebra_modules.py` before `83c80ce4` records how words and monomials index the homogeneous pieces of a free algebra.

**Affected consumers.**
Every algebra constructor and every algebra Hom; the tensor- and symmetric-algebra adjunctions; Kaehler differentials and de Rham algebras of polynomial rings; group algebras and their regular representations.

**Coverage boundary.**
Read from source; no session was run.
Which engine-backed algebras answer `module_generating_set` today, and with what, was not determined.
Scheduled as `algebra-structure-morphism-constructor` and `engine-algebras-through-the-structure-constructor` in [TODO.md](TODO.md).

## Workflow Papercuts

Add concrete observed workflow friction here under a descriptive heading, with the user action, expected behavior, actual result, owning boundary and example.
Use `DEV-59` for capture and resolution.
Foundational mathematical gaps belong above even when first noticed as an inconvenient method or notebook interaction.

### Tracked research Sage path resolves to a non-runnable stub source tree

- **User action:** run the repository's mandatory commit gate or regenerate the live preamble megadoc using the `SAGE_BIN` exported by the tracked `.envrc`.

- **Expected:** `/home/dzack/gitclones/sage-dev-allopts/sage` is the executable research-Sage runtime named by the repository environment.

- **Observed:** `/home/dzack/gitclones/sage-dev-allopts` currently resolves to `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src`; invoking its `sage`/`sage-preparse` fails with `ModuleNotFoundError: No module named 'sage'`. The host also has no `docker`, `podman`, `apptainer`, or `singularity` executable with which to provision the fork's documented `ghcr.io/dzackgarza/sage:develop` non-relocatable runtime. A separate Miniforge Sage 10.7 exists, but it is not the configured research-Sage owner and is not interchangeable semantic acceptance.

- **Owner:** research-Sage runtime/environment provisioning and the tracked `.envrc` contract.

- **Example:** observed when banking the resumed architecture-remediation DAG on 2026-09-15; the commit gate reached `_sage-syntax` and then failed inside the stub-tree `sage-preparse`.
