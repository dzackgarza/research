# SageMath category framework reference

Sage's category framework defines category classes, a global axiom registry, and functorial category constructions.
Parameterized categories, joins, refinements by axioms, and functorial constructions produce further category instances at runtime.
The mathematical categories represented here are defined in [Algebraic categories from operations](../framework/Mathematical-Framework.md), [Modules and base change](../framework/Modules-and-Forms.md), [Bilinear and quadratic forms](../framework/Bilinear-and-Quadratic-Forms.md), [Bilinear forms on the underlying module of an algebra](../framework/Bilinear-Forms-on-Algebra-Modules.md), and [Lattices and discriminant forms](../framework/Lattices-and-Discriminant-Forms.md).

## Categories

The pinned `sage.categories` source defines 222 category classes and wrapper constructors: 1 example-only class, 38 framework helpers, 6 public category-valued wrapper constructors, 173 public named classes, and 4 test-only classes.
At runtime the framework generates further classes from these: 209 axiom-generated and 200 construction-generated classes among the 678 loaded in a full-import session.

The [Sage category classes](Sage-Category-Classes.md) catalogue records each class with its module, role, defining axiom chain, and source permalink.
It also records the runtime classes and the 130 category instances constructed by a full import, including the 84 join categories and their factors.

The chain of declared superclass relations from `Modules(ZZ)` to `Objects()` passes through `Sets()` and `SetsWithPartialMaps()`:

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

The method `C._with_axiom(A)` is Sage's implementation mechanism for adjoining a registered axiom, and the registry is global.
The resulting category is not uniformly a mathematical replete full subcategory: some entries model isomorphism-invariant object properties, `WithBasis` records chosen data, and `Facade` and `Endset` control framework behavior.
The implementation site is the class in which the entry is declared.
Named classes are predefined category classes reached through this mechanism.

| axiom | status | implementation site | named subcategory classes |
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

### Mathematical interpretation

- The `Additive*` family duplicates the multiplicative axiom family across Sage's two operation towers; mathematically there is one magma-axiom family.

- Sage implements the ring refinements `Noetherian`, `Principal`, `UniqueFactorization`, `Euclidean`, `Gcd`, and `Dedekind` as plain category classes outside the axiom registry.

- Finite generation is structure-relative in Sage's own naming (`FinitelyGeneratedAsMagma`, `FinitelyGeneratedAsLambdaBracketAlgebra`).

- `WithBasis` records a chosen basis.
  `Facade` and `Endset` serve framework bookkeeping roles.

## Known discrepancies in Sage 10.9 {#sec-sage-discrepancies}

The pinned source and a running Sage kernel exhibit the following discrepancies between the mathematical hierarchy and Sage's declarations.

1. **Missing theorem inclusions in the subcategory lattice.** `PrincipalIdealDomains().is_subcategory(DedekindDomains())` and `…is_subcategory(NoetherianRings())` are both `False` (kernel-verified), though every PID is a Dedekind domain and noetherian; Sage does know `EuclideanDomains ⊂ PrincipalIdealDomains`. Consequence: `ZZ.category()` is the uncollapsed five-factor join *Dedekind ∧ euclidean ∧ noetherian ∧ infinite enumerated ∧ metric* whose algebraic part is mathematically just euclidean domains.

2. **The topological/metric naming gap.** The `Topological` construction has a declared nested class only at `Groups` (`groups.py:654`, "Category of topological groups"); `Metric` at none.
   All 76 bare joins constructed at import are intersections of a metric or topological Sage category with categories in the algebraic towers.
   The join factors alone do not assert compatibility between the topology or metric and the algebraic operations (join table in [Sage Category Classes](Sage-Category-Classes.md)).

3. **Construction declarations were not duplicated across the towers.** The additive tower received copies of the four magma axioms but not the `Topological` declaration, so `Groups().Topological()` is named while `AdditiveGroups().Topological()` is a bare join.

4. **The registry has no `Countable` or `Uncountable` axiom.** Countability is not expressible through `_with_axiom` in this Sage version.

5. **Doctest fixtures occur in the global registry.** `Blue` and `Flying` are test-only axioms registered in the same `all_axioms` collection as the mathematical axioms.

## Functorial constructions (17)

Constructions lift a category to a category of constructed objects.
Covariant constructions add structure, as in `C.CartesianProducts()`. Regressive constructions change the base category, as in `Graded`, `Filtered`, `Super`, `Metric`, and `Topological`. Both are distinct from refinements by axioms.

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

## Versions and source data

Source analysis and a runtime enumeration were compared on 2026-07-18. Both yielded 51 axioms and 17 functorial constructions:

- **Source axis** — AST audit of the SageMath 10.9 distribution (pinned commit [`686dc1a`](https://github.com/sagemath/sage/commit/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50), dist SHA-256 recorded in the artifacts).
  Raw data and the deterministic generator are tracked in the repository under [`data/sage-source-audit-10.9/`](../data/sage-source-audit-10.9/) ([categories](../data/sage-source-audit-10.9/sagemath-10.9-categories.csv), [axioms](../data/sage-source-audit-10.9/sagemath-10.9-axioms.csv), [constructions](../data/sage-source-audit-10.9/sagemath-10.9-functorial-constructions.csv), [feature declarations](../data/sage-source-audit-10.9/sagemath-10.9-category-feature-declarations.csv), [aliases](../data/sage-source-audit-10.9/sagemath-10.9-category-aliases.csv), [combined JSON](../data/sage-source-audit-10.9/sagemath-10.9-category-inventory.json), [generator](../data/sage-source-audit-10.9/build_sage_category_inventory.py)).

- **Runtime axis** — full class walk, registry dump, and instance enumeration of the running kernel (SageMath 10.10.beta0), scripts tracked under [`data/sage-inventory-scripts/`](../data/sage-inventory-scripts/) ([dump_categories.py](../data/sage-inventory-scripts/dump_categories.py), [dump_classes.py](../data/sage-inventory-scripts/dump_classes.py), [dump_instances.py](../data/sage-inventory-scripts/dump_instances.py)).
