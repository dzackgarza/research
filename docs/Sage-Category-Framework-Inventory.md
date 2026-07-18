# SageMath Category Framework Reference

The reference for Sage's category framework: the categories, the axiom registry, and the functorial constructions.
Sage constructs infinitely many category *instances* (parameterized, joined, axiom-refined, construction-lifted); the finite content below is the source-level vocabulary those instances are generated from.
Consumers: the mapping work on [research#260](https://github.com/dzackgarza/research/issues/260) and the generating-graph record on [research#251](https://github.com/dzackgarza/research/issues/251); the project-side counterpart of this page is [Mathematical Definitions](Mathematical-Definitions.md).

## Categories

222 category classes and wrapper constructors are defined in `sage.categories` (1 example-only; 38 framework/helper; 6 public category-valued wrapper constructor; 173 public named; 4 test-only).
At runtime the framework generates further classes from these: 209 axiom-generated and 200 construction-generated classes among the 678 loaded in a full-import session.

The full catalogue is **[Sage Category Classes](Sage-Category-Classes.md)**: every named category with its module, role, defining axiom chain, and source permalink, followed by the complete runtime population — every axiom-generated, construction-generated, and framework class with its generating axiom or construction, and the semantic instance layer: the 130 category instances a full import constructs, including all 84 join categories (meets in the category lattice) with their factors.

The hierarchy bottoms out at `Objects()` through `SetsWithPartialMaps()`, not at `Sets()`. Reference chain from `Modules(ZZ)` (complete `super_categories()` edge set):

```
    Category of additive commutative additive magmas  →  Category of additive magmas
    Category of additive groups  →  Category of additive inverse additive unital additive magmas
    Category of additive groups  →  Category of additive monoids
    Category of additive inverse additive unital additive magmas  →  Category of additive unital additive magmas
    Category of additive magmas  →  Category of sets
    Category of additive monoids  →  Category of additive semigroups
    Category of additive monoids  →  Category of additive unital additive magmas
    Category of additive semigroups  →  Category of additive magmas
    Category of additive unital additive magmas  →  Category of additive magmas
    Category of bimodules over Integer Ring on the left and Integer Ring on the right  →  Category of left modules over Integer Ring
    Category of bimodules over Integer Ring on the left and Integer Ring on the right  →  Category of right modules over Integer Ring
    Category of commutative additive groups  →  Category of additive groups
    Category of commutative additive groups  →  Category of commutative additive monoids
    Category of commutative additive monoids  →  Category of additive monoids
    Category of commutative additive monoids  →  Category of commutative additive semigroups
    Category of commutative additive semigroups  →  Category of additive commutative additive magmas
    Category of commutative additive semigroups  →  Category of additive semigroups
    Category of left modules over Integer Ring  →  Category of commutative additive groups
    Category of modules over Integer Ring  →  Category of bimodules over Integer Ring on the left and Integer Ring on the right
    Category of right modules over Integer Ring  →  Category of commutative additive groups
    Category of sets  →  Category of sets with partial maps
    Category of sets with partial maps  →  Category of objects
```

## Axiom registry (51)

Axioms refine a category into a full subcategory (`C._with_axiom(A)`); the registry is global and closed.
"Declared at" is the interface site — the category owning the axiom's meaning; named classes are premade subcategory classes reached by that axiom.

| axiom | status | declared at | named subcategory classes |
| --- | --- | --- | --- |
| `AdditiveAssociative` | production | `additive_magmas.AdditiveMagmas:AdditiveAssociative` | `AdditiveSemigroups` |
| `AdditiveCommutative` | production | `additive_magmas.AdditiveMagmas:AdditiveCommutative` | `CommutativeAdditiveGroups`, `CommutativeAdditiveMonoids`, `CommutativeAdditiveSemigroups` |
| `AdditiveInverse` | production | `additive_magmas.AdditiveMagmas:AdditiveUnital.AdditiveInverse` | `AdditiveGroups`, `Rngs` |
| `AdditiveUnital` | production | `additive_magmas.AdditiveMagmas:AdditiveUnital` | `AdditiveMonoids` |
| `AlmostComplex` | production | `manifolds.Manifolds:AlmostComplex` | — |
| `Analytic` | production | `manifolds.Manifolds:Analytic` | — |
| `Aperiodic` | production | `semigroups.Semigroups:Aperiodic` | `AperiodicSemigroups` |
| `Associative` | production | `magmas.Magmas:Associative` | `AssociativeAlgebras`, `Semigroups` |
| `Bounded` | production | `posets.Posets:Bounded` | — |
| `Cellular` | production | `finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis:Cellular` | — |
| `ChainGraded` | production | `lattice_posets.LatticePosets:ChainGraded` | `DistributiveLattices` |
| `Cocommutative` | production | `coalgebras.Coalgebras:Cocommutative` | — |
| `Commutative` | production | `category_with_axiom.Blahs:Commutative` | `CommutativeAlgebras`, `CommutativeRings`, `Fields`, … (4) |
| `Compact` | production | `topological_spaces.TopologicalSpaces:Compact` | — |
| `Complete` | production | `metric_spaces.MetricSpaces:Complete` | — |
| `CongruenceUniform` | production | `lattice_posets.LatticePosets:CongruenceUniform` | — |
| `Connected` | production | `category_with_axiom.Blahs:Connected` | — |
| `Differentiable` | production | `manifolds.Manifolds:Differentiable` | — |
| `Distributive` | production | `lattice_posets.LatticePosets:Distributive` | `DistributiveMagmasAndAdditiveMagmas` |
| `Division` | production | `rings.Rings:Division` | `DivisionRings` |
| `Endset` | production | `homsets.Homsets:Endset` | — |
| `Enumerated` | production | `sets_cat.Sets:Enumerated` | `EnumeratedSets` |
| `Extremal` | production | `lattice_posets.LatticePosets:Extremal` | — |
| `Facade` | production | `sets_cat.Sets:Facade` | `FacadeSets` |
| `Finite` | production | `sets_cat.Sets:Finite` | `FiniteComplexReflectionGroups`, `FiniteCoxeterGroups`, `FiniteCrystals`, … (13) |
| `FiniteDimensional` | production | `category_with_axiom.Blahs:FiniteDimensional` | `FiniteDimensionalAlgebrasWithBasis`, `FiniteDimensionalBialgebrasWithBasis`, `FiniteDimensionalCoalgebrasWithBasis`, … (6) |
| `FinitelyGeneratedAsLambdaBracketAlgebra` | production | `lambda_bracket_algebras.LambdaBracketAlgebras:FinitelyGeneratedAsLambdaBracketAlgebra` | `FinitelyGeneratedLambdaBracketAlgebras`, `FinitelyGeneratedLieConformalAlgebras` |
| `FinitelyGeneratedAsMagma` | production | `magmas.Magmas:FinitelyGeneratedAsMagma` | `FinitelyGeneratedMagmas`, `FinitelyGeneratedSemigroups` |
| `FinitelyPresented` | production | `modules.Modules:FinitelyPresented` | — |
| `HTrivial` | production | `semigroups.Semigroups:HTrivial` | `HTrivialSemigroups` |
| `Infinite` | production | `finite_sets.FiniteSets:Infinite` | `InfiniteEnumeratedSets` |
| `Inverse` | production | `magmas.Magmas:Unital.Inverse` | `Groups` |
| `Irreducible` | production | `complex_reflection_or_generalized_coxeter_groups.ComplexReflectionOrGeneralizedCoxeterGroups:Irreducible` | — |
| `JTrivial` | production | `magmas.Magmas:JTrivial` | `JTrivialSemigroups` |
| `LTrivial` | production | `semigroups.Semigroups:LTrivial` | `LTrivialSemigroups` |
| `Nilpotent` | production | `lie_algebras.LieAlgebras:Nilpotent` | `FiniteDimensionalNilpotentLieAlgebrasWithBasis` |
| `NoZeroDivisors` | production | `rings.Rings:NoZeroDivisors` | `Domains` |
| `Pointed` | production | `simplicial_sets.SimplicialSets:Pointed` | — |
| `RTrivial` | production | `semigroups.Semigroups:RTrivial` | `RTrivialSemigroups` |
| `Semidistributive` | production | `lattice_posets.LatticePosets:Semidistributive` | — |
| `Smooth` | production | `manifolds.Manifolds:Smooth` | — |
| `Stone` | production | `lattice_posets.LatticePosets:Stone` | — |
| `Stratified` | production | `graded_lie_algebras.GradedLieAlgebras:Stratified` | — |
| `Supercocommutative` | production | `coalgebras.Coalgebras:Super.Supercocommutative` | — |
| `Supercommutative` | production | `algebras.Algebras:Supercommutative` | `SupercommutativeAlgebras` |
| `Trim` | production | `lattice_posets.LatticePosets:Trim` | — |
| `Unital` | production | `category_with_axiom.Blahs:Unital` | `Algebras`, `Monoids`, `Rings`, … (5) |
| `WellGenerated` | production | `finite_complex_reflection_groups.FiniteComplexReflectionGroups:WellGenerated` | — |
| `WithBasis` | production | `modules.Modules:WithBasis` | `AlgebrasWithBasis`, `BialgebrasWithBasis`, `CoalgebrasWithBasis`, … (10) |
| `Blue` | test-only placeholder | `category_with_axiom.Blahs:Blue` | — |
| `Flying` | test-only placeholder | `category_with_axiom.Blahs:Flying` | — |

Reading notes (design facts):

- The `Additive*` family duplicates the multiplicative axiom family across Sage's two operation towers; mathematically there is one magma-axiom family.

- Ring refinements (`Noetherian`, `Principal`, `UniqueFactorization`, `Euclidean`, `Gcd`, `Dedekind`) are **not** axioms — Sage implements them as plain category classes.

- Finite generation is structure-relative in Sage's own naming (`FinitelyGeneratedAsMagma`, `FinitelyGeneratedAsLambdaBracketAlgebra`).

- `WithBasis` is presentation-witness data, not a mathematical property; `Facade` and `Endset` are framework bookkeeping.

## Defects and gaps (kernel-verified)

Findings about the upstream framework discovered while building this reference, each verified against the running kernel or the pinned source.
Candidate upstream reports; recorded here so the mapping work on [research#260](https://github.com/dzackgarza/research/issues/260) treats them as "mathematics present, declaration absent," never as missing mathematics.

1. **Missing theorem edges in the subcategory lattice.** `PrincipalIdealDomains().is_subcategory(DedekindDomains())` and `…is_subcategory(NoetherianRings())` are both `False` (kernel-verified), though every PID is a Dedekind domain and noetherian; Sage does know `EuclideanDomains ⊂ PrincipalIdealDomains`. Consequence: `ZZ.category()` is the uncollapsed five-factor join *Dedekind ∧ euclidean ∧ noetherian ∧ infinite enumerated ∧ metric* whose algebraic part is mathematically just euclidean domains.
   (The project's generating graph gains the missing `PID ⊂ Dedekind` theorem-witness inclusion as a pending delta on [research#251](https://github.com/dzackgarza/research/issues/251).)

2. **The topological/metric naming gap.** The `Topological` construction has a declared nested class only at `Groups` (`groups.py:654`, "Category of topological groups"); `Metric` at none.
   All 76 bare joins constructed at import are Metric/Topological meets with the algebraic towers — topological additive groups, metric monoids, topological semirings, … — standard objects Sage builds but cannot name (join table in [Sage Category Classes](Sage-Category-Classes.md)).

3. **Construction declarations were not duplicated across the towers.** The additive tower received copies of the four magma axioms but not the `Topological` declaration, so `Groups().Topological()` is named while `AdditiveGroups().Topological()` is a bare join.

4. **No `Countable`/`Uncountable` axiom exists upstream** — countability is not expressible in the registry; [research#65](https://github.com/dzackgarza/research/issues/65) owns these axioms project-side.

5. **Doctest fixtures live in the production registry.** `Blue` and `Flying` are test-only axioms registered in the same global `all_axioms` as the mathematical ones — enumeration must disposition, never copy.

## Functorial constructions (17)

Constructions lift a category to a category of constructed objects.
Covariant constructions add structure ( `C.CartesianProducts()` ); regressive ones change the base category (`Graded`, `Filtered`, `Super`, `Metric`, `Topological`) — the same species as the project's constructors (El, Core, π₀), never axioms.

| construction | flavor | implementation class | named result categories |
| --- | --- | --- | --- |
| `Algebras` | covariant | `AlgebrasCategory` | `CoxeterGroupAlgebras`, `GroupAlgebras` |
| `CartesianProducts` | covariant | `CartesianProductsCategory` | — |
| `DualObjects` | covariant | `DualObjectsCategory` | — |
| `Filtered` | regressive covariant | `FilteredModulesCategory` | `FilteredAlgebras`, `FilteredAlgebrasWithBasis`, `FilteredHopfAlgebrasWithBasis`, … (5) |
| `Graded` | regressive covariant | `GradedModulesCategory` | `GradedAlgebras`, `GradedAlgebrasWithBasis`, `GradedBialgebras`, … (14) |
| `Homsets` | general/specialized functorial | `HomsetsCategory` | `HomsetsOf` |
| `IsomorphicObjects` | regressive covariant | `IsomorphicObjectsCategory` | — |
| `Metric` | regressive covariant | `MetricSpacesCategory` | `MetricSpaces` |
| `Quotients` | regressive covariant | `QuotientsCategory` | — |
| `Realizations` | regressive covariant | `RealizationsCategory` | — |
| `SignedTensorProducts` | covariant | `SignedTensorProductsCategory` | — |
| `Subobjects` | regressive covariant | `SubobjectsCategory` | — |
| `Subquotients` | regressive covariant | `SubquotientsCategory` | — |
| `Super` | covariant | `SuperModulesCategory` | `SuperAlgebras`, `SuperAlgebrasWithBasis`, `SuperHopfAlgebrasWithBasis`, … (6) |
| `TensorProducts` | covariant | `TensorProductsCategory` | — |
| `Topological` | regressive covariant | `TopologicalSpacesCategory` | `TopologicalSpaces` |
| `WithRealizations` | regressive covariant | `WithRealizationsCategory` | — |

## Provenance

Two independent enumeration axes, cross-checked 2026-07-18; their 51-axiom and 17-construction registries are **identical**:

- **Source axis** — AST audit of the SageMath 10.9 distribution (pinned commit [`686dc1a`](https://github.com/sagemath/sage/commit/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50), dist SHA-256 recorded in the artifacts).
  Raw data and the deterministic generator are tracked in the repository under [`data/sage-source-audit-10.9/`](data/sage-source-audit-10.9/) ([categories](data/sage-source-audit-10.9/sagemath-10.9-categories.csv), [axioms](data/sage-source-audit-10.9/sagemath-10.9-axioms.csv), [constructions](data/sage-source-audit-10.9/sagemath-10.9-functorial-constructions.csv), [feature declarations](data/sage-source-audit-10.9/sagemath-10.9-category-feature-declarations.csv), [aliases](data/sage-source-audit-10.9/sagemath-10.9-category-aliases.csv), [combined JSON](data/sage-source-audit-10.9/sagemath-10.9-category-inventory.json), [generator](data/sage-source-audit-10.9/build_sage_category_inventory.py)).

- **Runtime axis** — full class walk, registry dump, and instance enumeration of the running kernel (SageMath 10.10.beta0), scripts tracked under [`data/sage-inventory-scripts/`](data/sage-inventory-scripts/) ([dump_categories.py](data/sage-inventory-scripts/dump_categories.py), [dump_classes.py](data/sage-inventory-scripts/dump_classes.py), [dump_instances.py](data/sage-inventory-scripts/dump_instances.py)).

To refresh after a kernel upgrade: rerun the runtime scripts, diff, update the tables here and in [Sage Category Classes](Sage-Category-Classes.md), and note the new version in this section.
