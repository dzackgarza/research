# Sage Category Classes

The full catalogue of named categories and wrapper constructors in `sage.categories` (SageMath 10.9 source, pinned commit `686dc1a`), one row per class: source-linked name, module, role, and the syntactic defining axiom chain or construction where the class is axiom- or construction-defined.
The last column marks classes confirmed loaded in the runtime walk at 10.10.beta0. Entrypoint: [Sage Category Framework Inventory](Sage-Category-Framework-Inventory.md).

| category | module | role | defined by | loaded at 10.10 |
| --- | --- | --- | --- | --- |
| [`IdempotentSemigroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/examples/semigroups_cython.pyx#L13) | `examples.semigroups_cython` | example-only | — | – |
| [`AlgebrasCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebra_functor.py#L640) | `algebra_functor` | framework/helper | — | ✓ |
| [`CartesianProductsCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cartesian_product.py#L225) | `cartesian_product` | framework/helper | — | ✓ |
| [`Category`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category.py#L131) | `category` | framework/helper | — | – |
| [`CategoryWithParameters`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category.py#L2691) | `category` | framework/helper | — | ✓ |
| [`JoinCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category.py#L2978) | `category` | framework/helper | — | ✓ |
| [`Category_singleton`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_singleton.pyx#L83) | `category_singleton` | framework/helper | — | ✓ |
| [`AbelianCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L334) | `category_types` | framework/helper | — | ✓ |
| [`Category_ideal`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L579) | `category_types` | framework/helper | — | ✓ |
| [`Category_in_ambient`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L534) | `category_types` | framework/helper | — | ✓ |
| [`Category_module`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L575) | `category_types` | framework/helper | — | ✓ |
| [`Category_over_base`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L147) | `category_types` | framework/helper | — | ✓ |
| [`Category_over_base_ring`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L347) | `category_types` | framework/helper | — | ✓ |
| [`Elements`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L36) | `category_types` | framework/helper | — | ✓ |
| [`CategoryWithAxiom`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1864) | `category_with_axiom` | framework/helper | — | ✓ |
| [`CategoryWithAxiom_over_base_ring`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2506) | `category_with_axiom` | framework/helper | — | ✓ |
| [`CategoryWithAxiom_singleton`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2530) | `category_with_axiom` | framework/helper | — | ✓ |
| [`CovariantConstructionCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/covariant_functorial_construction.py#L513) | `covariant_functorial_construction` | framework/helper | — | ✓ |
| [`FunctorialConstructionCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/covariant_functorial_construction.py#L230) | `covariant_functorial_construction` | framework/helper | — | ✓ |
| [`RegressiveCovariantConstructionCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/covariant_functorial_construction.py#L658) | `covariant_functorial_construction` | framework/helper | — | ✓ |
| [`DualObjectsCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/dual.py#L29) | `dual` | framework/helper | — | ✓ |
| [`FilteredModulesCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules.py#L37) | `filtered_modules` | framework/helper | — | ✓ |
| [`GradedLieConformalAlgebrasCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_conformal_algebras.py#L23) | `graded_lie_conformal_algebras` | framework/helper | `Graded` | ✓ |
| [`GradedModulesCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_modules.py#L17) | `graded_modules` | framework/helper | — | ✓ |
| [`HomsetsCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/homsets.py#L18) | `homsets` | framework/helper | — | ✓ |
| [`HomsetsOf`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/homsets.py#L172) | `homsets` | framework/helper | `Homsets` | ✓ |
| [`IsomorphicObjectsCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/isomorphic_objects.py#L19) | `isomorphic_objects` | framework/helper | — | ✓ |
| [`MetricSpacesCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L20) | `metric_spaces` | framework/helper | — | ✓ |
| [`QuotientsCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quotients.py#L19) | `quotients` | framework/helper | — | ✓ |
| [`Category_realization_of_parent`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/realizations.py#L110) | `realizations` | framework/helper | — | ✓ |
| [`RealizationsCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/realizations.py#L25) | `realizations` | framework/helper | — | ✓ |
| [`Schemes_over_base`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L159) | `schemes` | framework/helper | — | ✓ |
| [`SignedTensorProductsCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/signed_tensor.py#L76) | `signed_tensor` | framework/helper | — | ✓ |
| [`SubobjectsCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/subobjects.py#L19) | `subobjects` | framework/helper | — | ✓ |
| [`SubquotientsCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/subquotients.py#L18) | `subquotients` | framework/helper | — | ✓ |
| [`SuperModulesCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_modules.py#L27) | `super_modules` | framework/helper | — | ✓ |
| [`TensorProductsCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/tensor.py#L69) | `tensor` | framework/helper | — | ✓ |
| [`TopologicalSpacesCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L18) | `topological_spaces` | framework/helper | — | ✓ |
| [`WithRealizationsCategory`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/with_realizations.py#L287) | `with_realizations` | framework/helper | — | ✓ |
| [`FiniteDimensionalBialgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_bialgebras_with_basis.py#L13) | `finite_dimensional_bialgebras_with_basis` | public category-valued wrapper constructor | `FiniteDimensional` | – |
| [`FiniteDimensionalCoalgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_coalgebras_with_basis.py#L13) | `finite_dimensional_coalgebras_with_basis` | public category-valued wrapper constructor | `FiniteDimensional` | – |
| [`GradedBialgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_bialgebras.py#L13) | `graded_bialgebras` | public category-valued wrapper constructor | `Graded` | – |
| [`GradedBialgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_bialgebras_with_basis.py#L13) | `graded_bialgebras_with_basis` | public category-valued wrapper constructor | `Graded` | – |
| [`GradedHopfAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_hopf_algebras.py#L13) | `graded_hopf_algebras` | public category-valued wrapper constructor | `Graded` | – |
| [`MonoidAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoid_algebras.py#L14) | `monoid_algebras` | public category-valued wrapper constructor | — | – |
| [`AdditiveGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L19) | `additive_groups` | named | `AdditiveAssociative; AdditiveUnital; AdditiveInverse` | ✓ |
| [`AdditiveMagmas`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L25) | `additive_magmas` | named | — | ✓ |
| [`AdditiveMonoids`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L17) | `additive_monoids` | named | `AdditiveAssociative; AdditiveUnital` | ✓ |
| [`AdditiveSemigroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L20) | `additive_semigroups` | named | `AdditiveAssociative` | ✓ |
| [`AffineWeylGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/affine_weyl_groups.py#L17) | `affine_weyl_groups` | named | — | ✓ |
| [`AlgebraIdeals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebra_ideals.py#L19) | `algebra_ideals` | named | — | ✓ |
| [`AlgebraModules`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebra_modules.py#L19) | `algebra_modules` | named | — | ✓ |
| [`Algebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L29) | `algebras` | named | `Associative; Unital` | ✓ |
| [`AlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L21) | `algebras_with_basis` | named | `Associative; Unital; WithBasis` | ✓ |
| [`AperiodicSemigroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/aperiodic_semigroups.py#L18) | `aperiodic_semigroups` | named | `Associative; Aperiodic` | ✓ |
| [`AssociativeAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/associative_algebras.py#L16) | `associative_algebras` | named | `Associative` | ✓ |
| [`Bialgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/bialgebras.py#L20) | `bialgebras` | named | — | ✓ |
| [`BialgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/bialgebras_with_basis.py#L16) | `bialgebras_with_basis` | named | `WithBasis` | ✓ |
| [`Bimodules`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/bimodules.py#L24) | `bimodules` | named | — | ✓ |
| [`ChainComplexes`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/chain_complexes.py#L25) | `chain_complexes` | named | — | ✓ |
| [`ClassicalCrystals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/classical_crystals.py#L21) | `classical_crystals` | named | — | ✓ |
| [`Coalgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L27) | `coalgebras` | named | — | ✓ |
| [`CoalgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras_with_basis.py#L23) | `coalgebras_with_basis` | named | `WithBasis` | ✓ |
| [`CommutativeAdditiveGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_additive_groups.py#L18) | `commutative_additive_groups` | named | `AdditiveAssociative; AdditiveUnital; AdditiveInverse; AdditiveCommutative` | ✓ |
| [`CommutativeAdditiveMonoids`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_additive_monoids.py#L16) | `commutative_additive_monoids` | named | `AdditiveAssociative; AdditiveUnital; AdditiveCommutative` | ✓ |
| [`CommutativeAdditiveSemigroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_additive_semigroups.py#L15) | `commutative_additive_semigroups` | named | `AdditiveAssociative; AdditiveCommutative` | ✓ |
| [`CommutativeAlgebraIdeals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_algebra_ideals.py#L19) | `commutative_algebra_ideals` | named | — | ✓ |
| [`CommutativeAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_algebras.py#L20) | `commutative_algebras` | named | `Associative; Unital; Commutative` | ✓ |
| [`CommutativeRingIdeals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_ring_ideals.py#L18) | `commutative_ring_ideals` | named | — | ✓ |
| [`CommutativeRings`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_rings.py#L20) | `commutative_rings` | named | `Distributive; AdditiveAssociative; AdditiveCommutative; AdditiveUnital; Associative; AdditiveInverse; Unital; Commutative` | ✓ |
| [`CompleteDiscreteValuationFields`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complete_discrete_valuation.py#L175) | `complete_discrete_valuation` | named | — | ✓ |
| [`CompleteDiscreteValuationRings`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complete_discrete_valuation.py#L24) | `complete_discrete_valuation` | named | — | ✓ |
| [`ComplexReflectionGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complex_reflection_groups.py#L20) | `complex_reflection_groups` | named | — | ✓ |
| [`ComplexReflectionOrGeneralizedCoxeterGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complex_reflection_or_generalized_coxeter_groups.py#L23) | `complex_reflection_or_generalized_coxeter_groups` | named | — | ✓ |
| [`CoxeterGroupAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coxeter_group_algebras.py#L10) | `coxeter_group_algebras` | named | `Algebras` | ✓ |
| [`CoxeterGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coxeter_groups.py#L30) | `coxeter_groups` | named | — | ✓ |
| [`Crystals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L35) | `crystals` | named | — | ✓ |
| [`CWComplexes`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L18) | `cw_complexes` | named | — | ✓ |
| [`DedekindDomains`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/dedekind_domains.py#L14) | `dedekind_domains` | named | — | ✓ |
| [`DiscreteValuationFields`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/discrete_valuation.py#L222) | `discrete_valuation` | named | — | ✓ |
| [`DiscreteValuationRings`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/discrete_valuation.py#L18) | `discrete_valuation` | named | — | ✓ |
| [`DistributiveMagmasAndAdditiveMagmas`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L16) | `distributive_magmas_and_additive_magmas` | named | `Distributive` | ✓ |
| [`DivisionRings`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/division_rings.py#L16) | `division_rings` | named | `Distributive; AdditiveAssociative; AdditiveCommutative; AdditiveUnital; Associative; AdditiveInverse; Unital; Division` | ✓ |
| [`Domains`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/domains.py#L17) | `domains` | named | `Distributive; AdditiveAssociative; AdditiveCommutative; AdditiveUnital; Associative; AdditiveInverse; Unital; NoZeroDivisors` | ✓ |
| [`DrinfeldModules`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/drinfeld_modules.py#L35) | `drinfeld_modules` | named | — | ✓ |
| [`EnumeratedSets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L21) | `enumerated_sets` | named | `Enumerated` | ✓ |
| [`EuclideanDomains`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/euclidean_domains.py#L26) | `euclidean_domains` | named | — | ✓ |
| [`FacadeSets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/facade_sets.py#L16) | `facade_sets` | named | `Facade` | ✓ |
| [`Fields`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/fields.py#L26) | `fields` | named | `Distributive; AdditiveAssociative; AdditiveCommutative; AdditiveUnital; Associative; AdditiveInverse; Unital; Division; Commutative` | ✓ |
| [`FilteredAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_algebras.py#L15) | `filtered_algebras` | named | `Filtered` | ✓ |
| [`FilteredAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_algebras_with_basis.py#L22) | `filtered_algebras_with_basis` | named | `Filtered` | ✓ |
| [`FilteredHopfAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_hopf_algebras_with_basis.py#L18) | `filtered_hopf_algebras_with_basis` | named | `Filtered` | ✓ |
| [`FilteredModules`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules.py#L118) | `filtered_modules` | named | `Filtered` | ✓ |
| [`FilteredModulesWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules_with_basis.py#L38) | `filtered_modules_with_basis` | named | `Filtered` | ✓ |
| [`FiniteComplexReflectionGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_complex_reflection_groups.py#L22) | `finite_complex_reflection_groups` | named | `Finite` | ✓ |
| [`FiniteCoxeterGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_coxeter_groups.py#L22) | `finite_coxeter_groups` | named | `Finite` | ✓ |
| [`FiniteCrystals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_crystals.py#L18) | `finite_crystals` | named | `Finite` | ✓ |
| [`FiniteDimensionalAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L36) | `finite_dimensional_algebras_with_basis` | named | `Associative; Unital; WithBasis; FiniteDimensional` | ✓ |
| [`FiniteDimensionalGradedLieAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_graded_lie_algebras_with_basis.py#L23) | `finite_dimensional_graded_lie_algebras_with_basis` | named | `FiniteDimensional` | ✓ |
| [`FiniteDimensionalHopfAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_hopf_algebras_with_basis.py#L15) | `finite_dimensional_hopf_algebras_with_basis` | named | `WithBasis; FiniteDimensional` | ✓ |
| [`FiniteDimensionalLieAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_lie_algebras_with_basis.py#L55) | `finite_dimensional_lie_algebras_with_basis` | named | `FiniteDimensional; WithBasis` | ✓ |
| [`FiniteDimensionalModulesWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L21) | `finite_dimensional_modules_with_basis` | named | `WithBasis; FiniteDimensional` | ✓ |
| [`FiniteDimensionalNilpotentLieAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_nilpotent_lie_algebras_with_basis.py#L24) | `finite_dimensional_nilpotent_lie_algebras_with_basis` | named | `FiniteDimensional; WithBasis; Nilpotent` | ✓ |
| [`FiniteDimensionalSemisimpleAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_semisimple_algebras_with_basis.py#L18) | `finite_dimensional_semisimple_algebras_with_basis` | named | `FiniteDimensional; WithBasis` | ✓ |
| [`FiniteEnumeratedSets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_enumerated_sets.py#L22) | `finite_enumerated_sets` | named | `Enumerated; Finite` | ✓ |
| [`FiniteFields`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_fields.py#L21) | `finite_fields` | named | `Distributive; AdditiveAssociative; AdditiveCommutative; AdditiveUnital; Associative; AdditiveInverse; Unital; Division; Commutative; Finite` | ✓ |
| [`FiniteGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_groups.py#L16) | `finite_groups` | named | `Associative; Unital; Inverse; Finite` | ✓ |
| [`FiniteLatticePosets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_lattice_posets.py#L16) | `finite_lattice_posets` | named | `Finite` | ✓ |
| [`FiniteMonoids`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_monoids.py#L14) | `finite_monoids` | named | `Associative; Unital; Finite` | ✓ |
| [`FinitePermutationGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_permutation_groups.py#L18) | `finite_permutation_groups` | named | `Finite` | ✓ |
| [`FinitePosets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_posets.py#L24) | `finite_posets` | named | `Finite` | ✓ |
| [`FiniteSemigroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_semigroups.py#L18) | `finite_semigroups` | named | `Associative; Finite` | ✓ |
| [`FiniteSets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L16) | `finite_sets` | named | `Finite` | ✓ |
| [`FiniteWeylGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_weyl_groups.py#L14) | `finite_weyl_groups` | named | `Finite` | ✓ |
| [`FinitelyGeneratedLambdaBracketAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lambda_bracket_algebras.py#L24) | `finitely_generated_lambda_bracket_algebras` | named | `FinitelyGeneratedAsLambdaBracketAlgebra` | ✓ |
| [`FinitelyGeneratedLieConformalAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lie_conformal_algebras.py#L25) | `finitely_generated_lie_conformal_algebras` | named | `FinitelyGeneratedAsLambdaBracketAlgebra` | ✓ |
| [`FinitelyGeneratedMagmas`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_magmas.py#L16) | `finitely_generated_magmas` | named | `FinitelyGeneratedAsMagma` | ✓ |
| [`FinitelyGeneratedSemigroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_semigroups.py#L19) | `finitely_generated_semigroups` | named | `Associative; FinitelyGeneratedAsMagma` | ✓ |
| [`FunctionFields`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/function_fields.py#L19) | `function_fields` | named | — | ✓ |
| [`GSets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/g_sets.py#L21) | `g_sets` | named | — | ✓ |
| [`GcdDomains`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/gcd_domains.py#L15) | `gcd_domains` | named | — | ✓ |
| [`GeneralizedCoxeterGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/generalized_coxeter_groups.py#L20) | `generalized_coxeter_groups` | named | — | ✓ |
| [`GradedAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras.py#L17) | `graded_algebras` | named | `Graded` | ✓ |
| [`GradedAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras_with_basis.py#L18) | `graded_algebras_with_basis` | named | `Graded` | ✓ |
| [`GradedCoalgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_coalgebras.py#L17) | `graded_coalgebras` | named | `Graded` | ✓ |
| [`GradedCoalgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_coalgebras_with_basis.py#L18) | `graded_coalgebras_with_basis` | named | `Graded` | ✓ |
| [`GradedHopfAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_hopf_algebras_with_basis.py#L18) | `graded_hopf_algebras_with_basis` | named | `Graded` | ✓ |
| [`GradedLieAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras.py#L23) | `graded_lie_algebras` | named | `Graded` | ✓ |
| [`GradedLieAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras_with_basis.py#L19) | `graded_lie_algebras_with_basis` | named | `Graded` | ✓ |
| [`GradedLieConformalAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_conformal_algebras.py#L60) | `graded_lie_conformal_algebras` | named | `Graded` | ✓ |
| [`GradedModules`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_modules.py#L100) | `graded_modules` | named | `Graded` | ✓ |
| [`GradedModulesWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_modules_with_basis.py#L16) | `graded_modules_with_basis` | named | `Graded` | ✓ |
| [`Graphs`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graphs.py#L19) | `graphs` | named | — | ✓ |
| [`GroupAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/group_algebras.py#L34) | `group_algebras` | named | `Algebras` | ✓ |
| [`Groupoid`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groupoid.py#L18) | `groupoid` | named | — | ✓ |
| [`Groups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L23) | `groups` | named | `Associative; Unital; Inverse` | ✓ |
| [`HTrivialSemigroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/h_trivial_semigroups.py#L18) | `h_trivial_semigroups` | named | `Associative; HTrivial` | ✓ |
| [`HeckeModules`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hecke_modules.py#L18) | `hecke_modules` | named | — | ✓ |
| [`HighestWeightCrystals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/highest_weight_crystals.py#L19) | `highest_weight_crystals` | named | — | ✓ |
| [`Homsets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/homsets.py#L236) | `homsets` | named | — | ✓ |
| [`HopfAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L21) | `hopf_algebras` | named | — | ✓ |
| [`HopfAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L20) | `hopf_algebras_with_basis` | named | `WithBasis` | ✓ |
| [`InfiniteEnumeratedSets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/infinite_enumerated_sets.py#L19) | `infinite_enumerated_sets` | named | `Enumerated; Infinite` | ✓ |
| [`IntegralDomains`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/integral_domains.py#L41) | `integral_domains` | named | `Distributive; AdditiveAssociative; AdditiveCommutative; AdditiveUnital; Associative; AdditiveInverse; Unital; NoZeroDivisors; Commutative` | ✓ |
| [`JTrivialSemigroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/j_trivial_semigroups.py#L18) | `j_trivial_semigroups` | named | `Associative; JTrivial` | ✓ |
| [`KacMoodyAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/kac_moody_algebras.py#L23) | `kac_moody_algebras` | named | — | ✓ |
| [`KahlerAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/kahler_algebras.py#L24) | `kahler_algebras` | named | — | ✓ |
| [`LTrivialSemigroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/l_trivial_semigroups.py#L19) | `l_trivial_semigroups` | named | `Associative; LTrivial` | ✓ |
| [`LambdaBracketAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras.py#L30) | `lambda_bracket_algebras` | named | — | ✓ |
| [`LambdaBracketAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras_with_basis.py#L23) | `lambda_bracket_algebras_with_basis` | named | `WithBasis` | ✓ |
| [`DistributiveLattices`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L564) | `lattice_posets` | named | `Trim; ChainGraded` | ✓ |
| [`LatticePosets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L19) | `lattice_posets` | named | — | ✓ |
| [`LeftModules`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/left_modules.py#L16) | `left_modules` | named | — | ✓ |
| [`LieAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L34) | `lie_algebras` | named | — | ✓ |
| [`LieAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras_with_basis.py#L25) | `lie_algebras_with_basis` | named | `WithBasis` | ✓ |
| [`LieConformalAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras.py#L133) | `lie_conformal_algebras` | named | — | ✓ |
| [`LieConformalAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L25) | `lie_conformal_algebras_with_basis` | named | `WithBasis` | ✓ |
| [`LieGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_groups.py#L18) | `lie_groups` | named | — | ✓ |
| [`KirillovReshetikhinCrystals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/loop_crystals.py#L170) | `loop_crystals` | named | — | ✓ |
| [`LoopCrystals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/loop_crystals.py#L25) | `loop_crystals` | named | — | ✓ |
| [`RegularLoopCrystals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/loop_crystals.py#L132) | `loop_crystals` | named | — | ✓ |
| [`Magmas`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L25) | `magmas` | named | — | ✓ |
| [`MagmasAndAdditiveMagmas`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L19) | `magmas_and_additive_magmas` | named | — | ✓ |
| [`MagmaticAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L23) | `magmatic_algebras` | named | — | ✓ |
| [`ComplexManifolds`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L335) | `manifolds` | named | — | ✓ |
| [`Manifolds`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L19) | `manifolds` | named | — | ✓ |
| [`MatrixAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/matrix_algebras.py#L17) | `matrix_algebras` | named | — | ✓ |
| [`MetricSpaces`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L76) | `metric_spaces` | named | `Metric` | ✓ |
| [`ModularAbelianVarieties`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modular_abelian_varieties.py#L20) | `modular_abelian_varieties` | named | — | ✓ |
| [`Modules`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L33) | `modules` | named | — | ✓ |
| [`ModulesWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L44) | `modules_with_basis` | named | `WithBasis` | ✓ |
| [`Monoids`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L27) | `monoids` | named | `Associative; Unital` | ✓ |
| [`NoetherianRings`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/noetherian_rings.py#L30) | `noetherian_rings` | named | — | ✓ |
| [`NumberFields`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/number_fields.py#L18) | `number_fields` | named | — | ✓ |
| [`Objects`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/objects.py#L24) | `objects` | named | — | ✓ |
| [`OreModules`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/ore_modules.py#L26) | `ore_modules` | named | — | ✓ |
| [`PartiallyOrderedMonoids`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/partially_ordered_monoids.py#L15) | `partially_ordered_monoids` | named | — | ✓ |
| [`PermutationGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/permutation_groups.py#L17) | `permutation_groups` | named | — | ✓ |
| [`PointedSets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/pointed_sets.py#L17) | `pointed_sets` | named | — | ✓ |
| [`PolyhedralSets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/polyhedra.py#L15) | `polyhedra` | named | — | ✓ |
| [`Posets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L19) | `posets` | named | — | ✓ |
| [`PrincipalIdealDomains`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/principal_ideal_domains.py#L15) | `principal_ideal_domains` | named | — | ✓ |
| [`QuantumGroupRepresentations`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quantum_group_representations.py#L28) | `quantum_group_representations` | named | — | ✓ |
| [`QuotientFields`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quotient_fields.py#L18) | `quotient_fields` | named | — | ✓ |
| [`RTrivialSemigroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/r_trivial_semigroups.py#L18) | `r_trivial_semigroups` | named | `Associative; RTrivial` | ✓ |
| [`RegularCrystals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/regular_crystals.py#L27) | `regular_crystals` | named | — | ✓ |
| [`RegularSuperCrystals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/regular_supercrystals.py#L24) | `regular_supercrystals` | named | — | ✓ |
| [`RightModules`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/right_modules.py#L16) | `right_modules` | named | — | ✓ |
| [`RingIdeals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/ring_ideals.py#L20) | `ring_ideals` | named | — | ✓ |
| [`Rings`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L24) | `rings` | named | `Distributive; AdditiveAssociative; AdditiveCommutative; AdditiveUnital; Associative; AdditiveInverse; Unital` | ✓ |
| [`Rngs`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rngs.py#L18) | `rngs` | named | `Distributive; AdditiveAssociative; AdditiveCommutative; AdditiveUnital; Associative; AdditiveInverse` | ✓ |
| [`AbelianVarieties`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L205) | `schemes` | named | — | ✓ |
| [`Jacobians`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L308) | `schemes` | named | — | ✓ |
| [`Schemes`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L33) | `schemes` | named | — | ✓ |
| [`Semigroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L30) | `semigroups` | named | `Associative` | ✓ |
| [`Semirings`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semirings.py#L15) | `semirings` | named | `Distributive; AdditiveAssociative; AdditiveCommutative; AdditiveUnital; Associative; Unital` | ✓ |
| [`SemisimpleAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semisimple_algebras.py#L19) | `semisimple_algebras` | named | — | ✓ |
| [`Sets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L98) | `sets_cat` | named | — | ✓ |
| [`SetsWithGrading`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_with_grading.py#L18) | `sets_with_grading` | named | — | ✓ |
| [`SetsWithPartialMaps`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_with_partial_maps.py#L17) | `sets_with_partial_maps` | named | — | ✓ |
| [`ShephardGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/shephard_groups.py#L19) | `shephard_groups` | named | — | ✓ |
| [`SimplicialComplexes`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_complexes.py#L19) | `simplicial_complexes` | named | — | ✓ |
| [`SimplicialSets`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L27) | `simplicial_sets` | named | — | ✓ |
| [`SuperAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L18) | `super_algebras` | named | `Super` | ✓ |
| [`SuperAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras_with_basis.py#L16) | `super_algebras_with_basis` | named | `Super` | ✓ |
| [`SuperHopfAlgebrasWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_hopf_algebras_with_basis.py#L14) | `super_hopf_algebras_with_basis` | named | `Super` | ✓ |
| [`SuperLieConformalAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_lie_conformal_algebras.py#L25) | `super_lie_conformal_algebras` | named | `Super` | ✓ |
| [`SuperModules`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_modules.py#L86) | `super_modules` | named | `Super` | ✓ |
| [`SuperModulesWithBasis`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_modules_with_basis.py#L14) | `super_modules_with_basis` | named | `Super` | ✓ |
| [`SupercommutativeAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercommutative_algebras.py#L17) | `supercommutative_algebras` | named | `Supercommutative` | ✓ |
| [`SuperCrystals`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercrystals.py#L25) | `supercrystals` | named | — | ✓ |
| [`TopologicalSpaces`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L32) | `topological_spaces` | named | `Topological` | ✓ |
| [`TriangularKacMoodyAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/triangular_kac_moody_algebras.py#L27) | `triangular_kac_moody_algebras` | named | — | ✓ |
| [`UniqueFactorizationDomains`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/unique_factorization_domains.py#L18) | `unique_factorization_domains` | named | — | ✓ |
| [`UnitalAlgebras`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/unital_algebras.py#L24) | `unital_algebras` | named | `Unital` | ✓ |
| [`VectorBundles`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_bundles.py#L19) | `vector_bundles` | named | — | ✓ |
| [`VectorSpaces`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L27) | `vector_spaces` | named | — | ✓ |
| [`WeylGroups`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/weyl_groups.py#L18) | `weyl_groups` | named | — | ✓ |
| [`Bars`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2707) | `category_with_axiom` | test-only | — | ✓ |
| [`Blahs`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2600) | `category_with_axiom` | test-only | — | ✓ |
| [`DummyObjectsOverBaseRing`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2793) | `category_with_axiom` | test-only | — | ✓ |
| [`TestObjects`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2753) | `category_with_axiom` | test-only | — | ✓ |

The runtime walk (full-import session, SageMath 10.10.beta0) loads 678 category classes in total.
The named classes above account for the source-declared vocabulary; the remaining classes are enumerated in full below.

## Axiom-generated classes (209)

Nested `CategoryWithAxiom` classes — the premade implementations reached by `C._with_axiom(A)`. The axiom column is the generating axiom (see the registry table on the entrypoint page).

| class (qualname) | module | axiom |
| --- | --- | --- |
| `AdditiveGroups` | `additive_groups` | (framework base) |
| `AdditiveGroups.Finite` | `additive_groups` | `Finite` |
| `AdditiveGroups_with_category` | `additive_groups` | (framework base) |
| `AdditiveMagmas.AdditiveCommutative` | `additive_magmas` | `AdditiveCommutative` |
| `AdditiveMagmas.AdditiveCommutative_with_category` | `additive_magmas` | `AdditiveCommutative_with_category` |
| `AdditiveMagmas.AdditiveUnital` | `additive_magmas` | `AdditiveUnital` |
| `AdditiveMagmas.AdditiveUnital.AdditiveInverse` | `additive_magmas` | `AdditiveInverse` |
| `AdditiveMagmas.AdditiveUnital.AdditiveInverse_with_category` | `additive_magmas` | `AdditiveInverse_with_category` |
| `AdditiveMagmas.AdditiveUnital_with_category` | `additive_magmas` | `AdditiveUnital_with_category` |
| `AdditiveMonoids` | `additive_monoids` | (framework base) |
| `AdditiveMonoids_with_category` | `additive_monoids` | (framework base) |
| `AdditiveSemigroups` | `additive_semigroups` | (framework base) |
| `AdditiveSemigroups_with_category` | `additive_semigroups` | (framework base) |
| `Algebras` | `algebras` | (framework base) |
| `AlgebrasWithBasis` | `algebras_with_basis` | (framework base) |
| `AperiodicSemigroups` | `aperiodic_semigroups` | (framework base) |
| `AssociativeAlgebras` | `associative_algebras` | (framework base) |
| `BialgebrasWithBasis` | `bialgebras_with_basis` | (framework base) |
| `Blahs.Commutative` | `category_with_axiom` | `Commutative` |
| `Blahs.Connected` | `category_with_axiom` | `Connected` |
| `Blahs.FiniteDimensional` | `category_with_axiom` | `FiniteDimensional` |
| `Blahs.Flying` | `category_with_axiom` | `Flying` |
| `Blahs.Unital` | `category_with_axiom` | `Unital` |
| `Blahs.Unital.Blue` | `category_with_axiom` | `Blue` |
| `CategoryWithAxiom` | `category_with_axiom` | (framework base) |
| `CategoryWithAxiom_over_base_ring` | `category_with_axiom` | (framework base) |
| `CategoryWithAxiom_singleton` | `category_with_axiom` | (framework base) |
| `DummyObjectsOverBaseRing.Commutative` | `category_with_axiom` | `Commutative` |
| `DummyObjectsOverBaseRing.Commutative.Facade` | `category_with_axiom` | `Facade` |
| `DummyObjectsOverBaseRing.Commutative.Finite` | `category_with_axiom` | `Finite` |
| `DummyObjectsOverBaseRing.Commutative.FiniteDimensional` | `category_with_axiom` | `FiniteDimensional` |
| `DummyObjectsOverBaseRing.FiniteDimensional` | `category_with_axiom` | `FiniteDimensional` |
| `DummyObjectsOverBaseRing.FiniteDimensional.Finite` | `category_with_axiom` | `Finite` |
| `DummyObjectsOverBaseRing.FiniteDimensional.Unital` | `category_with_axiom` | `Unital` |
| `DummyObjectsOverBaseRing.FiniteDimensional.Unital.Commutative` | `category_with_axiom` | `Commutative` |
| `DummyObjectsOverBaseRing.Unital` | `category_with_axiom` | `Unital` |
| `TestObjects.Commutative` | `category_with_axiom` | `Commutative` |
| `TestObjects.Commutative.Facade` | `category_with_axiom` | `Facade` |
| `TestObjects.Commutative.Finite` | `category_with_axiom` | `Finite` |
| `TestObjects.Commutative.FiniteDimensional` | `category_with_axiom` | `FiniteDimensional` |
| `TestObjects.FiniteDimensional` | `category_with_axiom` | `FiniteDimensional` |
| `TestObjects.FiniteDimensional.Finite` | `category_with_axiom` | `Finite` |
| `TestObjects.FiniteDimensional.Unital` | `category_with_axiom` | `Unital` |
| `TestObjects.FiniteDimensional.Unital.Commutative` | `category_with_axiom` | `Commutative` |
| `TestObjects.Unital` | `category_with_axiom` | `Unital` |
| `Coalgebras.Cocommutative` | `coalgebras` | `Cocommutative` |
| `Coalgebras.Super.Supercocommutative` | `coalgebras` | `Supercocommutative` |
| `CoalgebrasWithBasis` | `coalgebras_with_basis` | (framework base) |
| `CommutativeAdditiveGroups` | `commutative_additive_groups` | (framework base) |
| `CommutativeAdditiveGroups_with_category` | `commutative_additive_groups` | (framework base) |
| `CommutativeAdditiveMonoids` | `commutative_additive_monoids` | (framework base) |
| `CommutativeAdditiveMonoids_with_category` | `commutative_additive_monoids` | (framework base) |
| `CommutativeAdditiveSemigroups` | `commutative_additive_semigroups` | (framework base) |
| `CommutativeAdditiveSemigroups_with_category` | `commutative_additive_semigroups` | (framework base) |
| `CommutativeAlgebras` | `commutative_algebras` | (framework base) |
| `CommutativeRings` | `commutative_rings` | (framework base) |
| `CommutativeRings.Finite` | `commutative_rings` | `Finite` |
| `CommutativeRings_with_category` | `commutative_rings` | (framework base) |
| `ComplexReflectionOrGeneralizedCoxeterGroups.Irreducible` | `complex_reflection_or_generalized_coxeter_groups` | `Irreducible` |
| `CWComplexes.Connected` | `cw_complexes` | `Connected` |
| `CWComplexes.Finite` | `cw_complexes` | `Finite` |
| `CWComplexes.FiniteDimensional` | `cw_complexes` | `FiniteDimensional` |
| `DistributiveMagmasAndAdditiveMagmas` | `distributive_magmas_and_additive_magmas` | (framework base) |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative` | `distributive_magmas_and_additive_magmas` | `AdditiveAssociative` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative` | `distributive_magmas_and_additive_magmas` | `AdditiveCommutative` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital` | `distributive_magmas_and_additive_magmas` | `AdditiveUnital` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative` | `distributive_magmas_and_additive_magmas` | `Associative` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative_with_category` | `distributive_magmas_and_additive_magmas` | `Associative_with_category` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital_with_category` | `distributive_magmas_and_additive_magmas` | `AdditiveUnital_with_category` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative_with_category` | `distributive_magmas_and_additive_magmas` | `AdditiveCommutative_with_category` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative_with_category` | `distributive_magmas_and_additive_magmas` | `AdditiveAssociative_with_category` |
| `DistributiveMagmasAndAdditiveMagmas_with_category` | `distributive_magmas_and_additive_magmas` | (framework base) |
| `DivisionRings` | `division_rings` | (framework base) |
| `DivisionRings_with_category` | `division_rings` | (framework base) |
| `Domains` | `domains` | (framework base) |
| `Domains_with_category` | `domains` | (framework base) |
| `EnumeratedSets` | `enumerated_sets` | (framework base) |
| `EnumeratedSets_with_category` | `enumerated_sets` | (framework base) |
| `FacadeSets` | `facade_sets` | (framework base) |
| `Fields` | `fields` | (framework base) |
| `Fields_with_category` | `fields` | (framework base) |
| `FilteredHopfAlgebrasWithBasis.Connected` | `filtered_hopf_algebras_with_basis` | `Connected` |
| `FilteredModules.Connected` | `filtered_modules` | `Connected` |
| `FilteredModulesWithBasis.FiniteDimensional` | `filtered_modules_with_basis` | `FiniteDimensional` |
| `FiniteComplexReflectionGroups` | `finite_complex_reflection_groups` | (framework base) |
| `FiniteComplexReflectionGroups.Irreducible` | `finite_complex_reflection_groups` | `Irreducible` |
| `FiniteComplexReflectionGroups.WellGenerated` | `finite_complex_reflection_groups` | `WellGenerated` |
| `FiniteComplexReflectionGroups.WellGenerated.Irreducible` | `finite_complex_reflection_groups` | `Irreducible` |
| `FiniteCoxeterGroups` | `finite_coxeter_groups` | (framework base) |
| `FiniteCrystals` | `finite_crystals` | (framework base) |
| `FiniteDimensionalAlgebrasWithBasis` | `finite_dimensional_algebras_with_basis` | (framework base) |
| `FiniteDimensionalAlgebrasWithBasis.Cellular` | `finite_dimensional_algebras_with_basis` | `Cellular` |
| `FiniteDimensionalGradedLieAlgebrasWithBasis` | `finite_dimensional_graded_lie_algebras_with_basis` | (framework base) |
| `FiniteDimensionalGradedLieAlgebrasWithBasis.Stratified` | `finite_dimensional_graded_lie_algebras_with_basis` | `Stratified` |
| `FiniteDimensionalHopfAlgebrasWithBasis` | `finite_dimensional_hopf_algebras_with_basis` | (framework base) |
| `FiniteDimensionalLieAlgebrasWithBasis` | `finite_dimensional_lie_algebras_with_basis` | (framework base) |
| `FiniteDimensionalModulesWithBasis` | `finite_dimensional_modules_with_basis` | (framework base) |
| `FiniteDimensionalModulesWithBasis.Homsets.Endset` | `finite_dimensional_modules_with_basis` | `Endset` |
| `FiniteDimensionalNilpotentLieAlgebrasWithBasis` | `finite_dimensional_nilpotent_lie_algebras_with_basis` | (framework base) |
| `FiniteDimensionalSemisimpleAlgebrasWithBasis` | `finite_dimensional_semisimple_algebras_with_basis` | (framework base) |
| `FiniteDimensionalSemisimpleAlgebrasWithBasis.Commutative` | `finite_dimensional_semisimple_algebras_with_basis` | `Commutative` |
| `FiniteEnumeratedSets` | `finite_enumerated_sets` | (framework base) |
| `FiniteEnumeratedSets_with_category` | `finite_enumerated_sets` | (framework base) |
| `FiniteFields` | `finite_fields` | (framework base) |
| `FiniteGroups` | `finite_groups` | (framework base) |
| `FiniteLatticePosets` | `finite_lattice_posets` | (framework base) |
| `FiniteMonoids` | `finite_monoids` | (framework base) |
| `FinitePermutationGroups` | `finite_permutation_groups` | (framework base) |
| `FinitePosets` | `finite_posets` | (framework base) |
| `FiniteSemigroups` | `finite_semigroups` | (framework base) |
| `FiniteSets` | `finite_sets` | (framework base) |
| `FiniteSets_with_category` | `finite_sets` | (framework base) |
| `FiniteWeylGroups` | `finite_weyl_groups` | (framework base) |
| `FinitelyGeneratedLambdaBracketAlgebras` | `finitely_generated_lambda_bracket_algebras` | (framework base) |
| `FinitelyGeneratedLieConformalAlgebras` | `finitely_generated_lie_conformal_algebras` | (framework base) |
| `FinitelyGeneratedMagmas` | `finitely_generated_magmas` | (framework base) |
| `FinitelyGeneratedSemigroups` | `finitely_generated_semigroups` | (framework base) |
| `FinitelyGeneratedSemigroups.Finite` | `finitely_generated_semigroups` | `Finite` |
| `GeneralizedCoxeterGroups.Finite` | `generalized_coxeter_groups` | `Finite` |
| `GradedAlgebrasWithBasis.FiniteDimensional` | `graded_algebras_with_basis` | `FiniteDimensional` |
| `GradedHopfAlgebrasWithBasis.Connected` | `graded_hopf_algebras_with_basis` | `Connected` |
| `GradedLieAlgebras.Stratified` | `graded_lie_algebras` | `Stratified` |
| `GradedLieAlgebras.Stratified.FiniteDimensional` | `graded_lie_algebras` | `FiniteDimensional` |
| `Graphs.Connected` | `graphs` | `Connected` |
| `Groups` | `groups` | (framework base) |
| `Groups.Commutative` | `groups` | `Commutative` |
| `HTrivialSemigroups` | `h_trivial_semigroups` | (framework base) |
| `Homsets.Endset` | `homsets` | `Endset` |
| `HopfAlgebrasWithBasis` | `hopf_algebras_with_basis` | (framework base) |
| `InfiniteEnumeratedSets` | `infinite_enumerated_sets` | (framework base) |
| `InfiniteEnumeratedSets_with_category` | `infinite_enumerated_sets` | (framework base) |
| `IntegralDomains` | `integral_domains` | (framework base) |
| `IntegralDomains_with_category` | `integral_domains` | (framework base) |
| `JTrivialSemigroups` | `j_trivial_semigroups` | (framework base) |
| `LTrivialSemigroups` | `l_trivial_semigroups` | (framework base) |
| `LambdaBracketAlgebrasWithBasis` | `lambda_bracket_algebras_with_basis` | (framework base) |
| `LambdaBracketAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra` | `lambda_bracket_algebras_with_basis` | `FinitelyGeneratedAsLambdaBracketAlgebra` |
| `DistributiveLattices` | `lattice_posets` | (framework base) |
| `DistributiveLattices.Finite` | `lattice_posets` | `Finite` |
| `LatticePosets.ChainGraded` | `lattice_posets` | `ChainGraded` |
| `LatticePosets.CongruenceUniform` | `lattice_posets` | `CongruenceUniform` |
| `LatticePosets.Extremal` | `lattice_posets` | `Extremal` |
| `LatticePosets.Semidistributive` | `lattice_posets` | `Semidistributive` |
| `LatticePosets.Stone` | `lattice_posets` | `Stone` |
| `LatticePosets.Trim` | `lattice_posets` | `Trim` |
| `LieAlgebras.FiniteDimensional` | `lie_algebras` | `FiniteDimensional` |
| `LieAlgebras.Nilpotent` | `lie_algebras` | `Nilpotent` |
| `LieAlgebrasWithBasis` | `lie_algebras_with_basis` | (framework base) |
| `LieConformalAlgebrasWithBasis` | `lie_conformal_algebras_with_basis` | (framework base) |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra` | `lie_conformal_algebras_with_basis` | `FinitelyGeneratedAsLambdaBracketAlgebra` |
| `Magmas.Commutative` | `magmas` | `Commutative` |
| `Magmas.Commutative_with_category` | `magmas` | `Commutative_with_category` |
| `Magmas.JTrivial` | `magmas` | `JTrivial` |
| `Magmas.Unital` | `magmas` | `Unital` |
| `Magmas.Unital.Inverse` | `magmas` | `Inverse` |
| `Magmas.Unital_with_category` | `magmas` | `Unital_with_category` |
| `MagmaticAlgebras.WithBasis` | `magmatic_algebras` | `WithBasis` |
| `MagmaticAlgebras.WithBasis.FiniteDimensional` | `magmatic_algebras` | `FiniteDimensional` |
| `Manifolds.AlmostComplex` | `manifolds` | `AlmostComplex` |
| `Manifolds.Analytic` | `manifolds` | `Analytic` |
| `Manifolds.Connected` | `manifolds` | `Connected` |
| `Manifolds.Differentiable` | `manifolds` | `Differentiable` |
| `Manifolds.FiniteDimensional` | `manifolds` | `FiniteDimensional` |
| `Manifolds.Smooth` | `manifolds` | `Smooth` |
| `MetricSpaces.Complete` | `metric_spaces` | `Complete` |
| `MetricSpaces.Complete_with_category` | `metric_spaces` | `Complete_with_category` |
| `ModularAbelianVarieties.Homsets.Endset` | `modular_abelian_varieties` | `Endset` |
| `Modules.FiniteDimensional` | `modules` | `FiniteDimensional` |
| `Modules.FinitelyPresented` | `modules` | `FinitelyPresented` |
| `Modules.Homsets.Endset` | `modules` | `Endset` |
| `ModulesWithBasis` | `modules_with_basis` | (framework base) |
| `Monoids` | `monoids` | (framework base) |
| `Monoids.Commutative` | `monoids` | `Commutative` |
| `Monoids.Commutative_with_category` | `monoids` | `Commutative_with_category` |
| `Monoids_with_category` | `monoids` | (framework base) |
| `Posets.Bounded` | `posets` | `Bounded` |
| `QuantumGroupRepresentations.WithBasis` | `quantum_group_representations` | `WithBasis` |
| `RTrivialSemigroups` | `r_trivial_semigroups` | (framework base) |
| `Rings` | `rings` | (framework base) |
| `Rings_with_category` | `rings` | (framework base) |
| `Rngs` | `rngs` | (framework base) |
| `Rngs_with_category` | `rngs` | (framework base) |
| `AbelianVarieties.Homsets.Endset` | `schemes` | `Endset` |
| `Semigroups` | `semigroups` | (framework base) |
| `Semigroups_with_category` | `semigroups` | (framework base) |
| `Semirings` | `semirings` | (framework base) |
| `Semirings_with_category` | `semirings` | (framework base) |
| `SemisimpleAlgebras.FiniteDimensional` | `semisimple_algebras` | `FiniteDimensional` |
| `Sets.Infinite` | `sets_cat` | `Infinite` |
| `Sets.Infinite_with_category` | `sets_cat` | `Infinite_with_category` |
| `SimplicialComplexes.Connected` | `simplicial_complexes` | `Connected` |
| `SimplicialComplexes.Finite` | `simplicial_complexes` | `Finite` |
| `SimplicialSets.Finite` | `simplicial_sets` | `Finite` |
| `SimplicialSets.Homsets.Endset` | `simplicial_sets` | `Endset` |
| `SimplicialSets.Pointed` | `simplicial_sets` | `Pointed` |
| `SimplicialSets.Pointed.Finite` | `simplicial_sets` | `Finite` |
| `SupercommutativeAlgebras` | `supercommutative_algebras` | (framework base) |
| `SupercommutativeAlgebras.WithBasis` | `supercommutative_algebras` | `WithBasis` |
| `SuperCrystals.Finite` | `supercrystals` | `Finite` |
| `TopologicalSpaces.Compact` | `topological_spaces` | `Compact` |
| `TopologicalSpaces.Connected` | `topological_spaces` | `Connected` |
| `TriangularKacMoodyAlgebras.FiniteDimensional` | `triangular_kac_moody_algebras` | `FiniteDimensional` |
| `UnitalAlgebras` | `unital_algebras` | (framework base) |
| `UnitalAlgebras.WithBasis` | `unital_algebras` | `WithBasis` |
| `VectorBundles.Differentiable` | `vector_bundles` | `Differentiable` |
| `VectorBundles.Smooth` | `vector_bundles` | `Smooth` |
| `VectorSpaces.FiniteDimensional` | `vector_spaces` | `FiniteDimensional` |
| `VectorSpaces.WithBasis` | `vector_spaces` | `WithBasis` |
| `VectorSpaces.WithBasis.FiniteDimensional` | `vector_spaces` | `FiniteDimensional` |

## Construction-generated classes (200)

Nested `FunctorialConstructionCategory` classes — per-category implementations of the 17 functorial constructions, plus the framework base classes.

| class (qualname) | module | construction |
| --- | --- | --- |
| `AdditiveGroups.Algebras` | `additive_groups` | `Algebras` |
| `AdditiveGroups.Finite.Algebras` | `additive_groups` | `Algebras` |
| `AdditiveMagmas.AdditiveCommutative.Algebras` | `additive_magmas` | `Algebras` |
| `AdditiveMagmas.AdditiveCommutative.CartesianProducts` | `additive_magmas` | `CartesianProducts` |
| `AdditiveMagmas.AdditiveUnital.AdditiveInverse.CartesianProducts` | `additive_magmas` | `CartesianProducts` |
| `AdditiveMagmas.AdditiveUnital.Algebras` | `additive_magmas` | `Algebras` |
| `AdditiveMagmas.AdditiveUnital.CartesianProducts` | `additive_magmas` | `CartesianProducts` |
| `AdditiveMagmas.AdditiveUnital.Homsets` | `additive_magmas` | `Homsets` |
| `AdditiveMagmas.AdditiveUnital.WithRealizations` | `additive_magmas` | `WithRealizations` |
| `AdditiveMagmas.Algebras` | `additive_magmas` | `Algebras` |
| `AdditiveMagmas.CartesianProducts` | `additive_magmas` | `CartesianProducts` |
| `AdditiveMagmas.Homsets` | `additive_magmas` | `Homsets` |
| `AdditiveMonoids.Homsets` | `additive_monoids` | `Homsets` |
| `AdditiveSemigroups.Algebras` | `additive_semigroups` | `Algebras` |
| `AdditiveSemigroups.CartesianProducts` | `additive_semigroups` | `CartesianProducts` |
| `AdditiveSemigroups.Homsets` | `additive_semigroups` | `Homsets` |
| `AlgebrasCategory` | `algebra_functor` | (framework base) |
| `Algebras.CartesianProducts` | `algebras` | `CartesianProducts` |
| `Algebras.DualObjects` | `algebras` | `DualObjects` |
| `Algebras.Quotients` | `algebras` | `Quotients` |
| `Algebras.TensorProducts` | `algebras` | `TensorProducts` |
| `AlgebrasWithBasis.CartesianProducts` | `algebras_with_basis` | `CartesianProducts` |
| `AlgebrasWithBasis.TensorProducts` | `algebras_with_basis` | `TensorProducts` |
| `Bialgebras.Super` | `bialgebras` | `Super` |
| `CartesianProductsCategory` | `cartesian_product` | (framework base) |
| `ClassicalCrystals.TensorProducts` | `classical_crystals` | `TensorProducts` |
| `Coalgebras.DualObjects` | `coalgebras` | `DualObjects` |
| `Coalgebras.Filtered` | `coalgebras` | `Filtered` |
| `Coalgebras.Realizations` | `coalgebras` | `Realizations` |
| `Coalgebras.Super` | `coalgebras` | `Super` |
| `Coalgebras.TensorProducts` | `coalgebras` | `TensorProducts` |
| `Coalgebras.WithRealizations` | `coalgebras` | `WithRealizations` |
| `CoalgebrasWithBasis.Filtered` | `coalgebras_with_basis` | `Filtered` |
| `CoalgebrasWithBasis.Super` | `coalgebras_with_basis` | `Super` |
| `CommutativeAdditiveGroups.Algebras` | `commutative_additive_groups` | `Algebras` |
| `CommutativeAdditiveGroups.CartesianProducts` | `commutative_additive_groups` | `CartesianProducts` |
| `CommutativeAlgebras.TensorProducts` | `commutative_algebras` | `TensorProducts` |
| `CommutativeRings.CartesianProducts` | `commutative_rings` | `CartesianProducts` |
| `CovariantConstructionCategory` | `covariant_functorial_construction` | (framework base) |
| `FunctorialConstructionCategory` | `covariant_functorial_construction` | (framework base) |
| `RegressiveCovariantConstructionCategory` | `covariant_functorial_construction` | (framework base) |
| `CoxeterGroupAlgebras` | `coxeter_group_algebras` | (framework base) |
| `Crystals.TensorProducts` | `crystals` | `TensorProducts` |
| `DistributiveMagmasAndAdditiveMagmas.CartesianProducts` | `distributive_magmas_and_additive_magmas` | `CartesianProducts` |
| `DualObjectsCategory` | `dual` | (framework base) |
| `EnumeratedSets.CartesianProducts` | `enumerated_sets` | `CartesianProducts` |
| `FilteredAlgebras` | `filtered_algebras` | (framework base) |
| `FilteredAlgebrasWithBasis` | `filtered_algebras_with_basis` | (framework base) |
| `FilteredHopfAlgebrasWithBasis` | `filtered_hopf_algebras_with_basis` | (framework base) |
| `FilteredHopfAlgebrasWithBasis.WithRealizations` | `filtered_hopf_algebras_with_basis` | `WithRealizations` |
| `FilteredModules` | `filtered_modules` | (framework base) |
| `FilteredModulesCategory` | `filtered_modules` | (framework base) |
| `FilteredModulesWithBasis` | `filtered_modules_with_basis` | (framework base) |
| `FilteredModulesWithBasis.Subobjects` | `filtered_modules_with_basis` | `Subobjects` |
| `FiniteCrystals.TensorProducts` | `finite_crystals` | `TensorProducts` |
| `FiniteDimensionalAlgebrasWithBasis.Cellular.TensorProducts` | `finite_dimensional_algebras_with_basis` | `TensorProducts` |
| `FiniteDimensionalLieAlgebrasWithBasis.Subobjects` | `finite_dimensional_lie_algebras_with_basis` | `Subobjects` |
| `FiniteDimensionalModulesWithBasis.Homsets` | `finite_dimensional_modules_with_basis` | `Homsets` |
| `FiniteDimensionalModulesWithBasis.TensorProducts` | `finite_dimensional_modules_with_basis` | `TensorProducts` |
| `FiniteEnumeratedSets.CartesianProducts` | `finite_enumerated_sets` | `CartesianProducts` |
| `FiniteEnumeratedSets.IsomorphicObjects` | `finite_enumerated_sets` | `IsomorphicObjects` |
| `FiniteGroups.Algebras` | `finite_groups` | `Algebras` |
| `FiniteSets.Algebras` | `finite_sets` | `Algebras` |
| `FiniteSets.Subquotients` | `finite_sets` | `Subquotients` |
| `FinitelyGeneratedLambdaBracketAlgebras.Graded` | `finitely_generated_lambda_bracket_algebras` | `Graded` |
| `FinitelyGeneratedLieConformalAlgebras.Graded` | `finitely_generated_lie_conformal_algebras` | `Graded` |
| `FinitelyGeneratedLieConformalAlgebras.Super` | `finitely_generated_lie_conformal_algebras` | `Super` |
| `FinitelyGeneratedLieConformalAlgebras.Super.Graded` | `finitely_generated_lie_conformal_algebras` | `Graded` |
| `GradedAlgebras` | `graded_algebras` | (framework base) |
| `GradedAlgebras.SignedTensorProducts` | `graded_algebras` | `SignedTensorProducts` |
| `GradedAlgebrasWithBasis` | `graded_algebras_with_basis` | (framework base) |
| `GradedAlgebrasWithBasis.SignedTensorProducts` | `graded_algebras_with_basis` | `SignedTensorProducts` |
| `GradedCoalgebras` | `graded_coalgebras` | (framework base) |
| `GradedCoalgebras.SignedTensorProducts` | `graded_coalgebras` | `SignedTensorProducts` |
| `GradedCoalgebrasWithBasis` | `graded_coalgebras_with_basis` | (framework base) |
| `GradedCoalgebrasWithBasis.SignedTensorProducts` | `graded_coalgebras_with_basis` | `SignedTensorProducts` |
| `GradedHopfAlgebrasWithBasis` | `graded_hopf_algebras_with_basis` | (framework base) |
| `GradedHopfAlgebrasWithBasis.WithRealizations` | `graded_hopf_algebras_with_basis` | `WithRealizations` |
| `GradedLieAlgebras` | `graded_lie_algebras` | (framework base) |
| `GradedLieAlgebrasWithBasis` | `graded_lie_algebras_with_basis` | (framework base) |
| `GradedLieConformalAlgebras` | `graded_lie_conformal_algebras` | (framework base) |
| `GradedLieConformalAlgebrasCategory` | `graded_lie_conformal_algebras` | (framework base) |
| `GradedModules` | `graded_modules` | (framework base) |
| `GradedModulesCategory` | `graded_modules` | (framework base) |
| `GradedModulesWithBasis` | `graded_modules_with_basis` | (framework base) |
| `GradedModulesWithBasis.Quotients` | `graded_modules_with_basis` | `Quotients` |
| `GroupAlgebras` | `group_algebras` | (framework base) |
| `Groups.CartesianProducts` | `groups` | `CartesianProducts` |
| `Groups.Topological` | `groups` | `Topological` |
| `HeckeModules.Homsets` | `hecke_modules` | `Homsets` |
| `HighestWeightCrystals.TensorProducts` | `highest_weight_crystals` | `TensorProducts` |
| `HomsetsCategory` | `homsets` | (framework base) |
| `HomsetsOf` | `homsets` | (framework base) |
| `HomsetsOf_with_category` | `homsets` | (framework base) |
| `HomsetsOf_with_category` | `homsets` | (framework base) |
| `HopfAlgebras.Realizations` | `hopf_algebras` | `Realizations` |
| `HopfAlgebras.Super` | `hopf_algebras` | `Super` |
| `HopfAlgebras.TensorProducts` | `hopf_algebras` | `TensorProducts` |
| `HopfAlgebrasWithBasis.TensorProducts` | `hopf_algebras_with_basis` | `TensorProducts` |
| `IsomorphicObjectsCategory` | `isomorphic_objects` | (framework base) |
| `LambdaBracketAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Graded` | `lambda_bracket_algebras_with_basis` | `Graded` |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Graded` | `lie_conformal_algebras_with_basis` | `Graded` |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Super` | `lie_conformal_algebras_with_basis` | `Super` |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Super.Graded` | `lie_conformal_algebras_with_basis` | `Graded` |
| `LieConformalAlgebrasWithBasis.Graded` | `lie_conformal_algebras_with_basis` | `Graded` |
| `LieConformalAlgebrasWithBasis.Super` | `lie_conformal_algebras_with_basis` | `Super` |
| `LieConformalAlgebrasWithBasis.Super.Graded` | `lie_conformal_algebras_with_basis` | `Graded` |
| `KirillovReshetikhinCrystals.TensorProducts` | `loop_crystals` | `TensorProducts` |
| `Magmas.Algebras` | `magmas` | `Algebras` |
| `Magmas.CartesianProducts` | `magmas` | `CartesianProducts` |
| `Magmas.Commutative.Algebras` | `magmas` | `Algebras` |
| `Magmas.Commutative.CartesianProducts` | `magmas` | `CartesianProducts` |
| `Magmas.Realizations` | `magmas` | `Realizations` |
| `Magmas.Subquotients` | `magmas` | `Subquotients` |
| `Magmas.Subquotients_with_category` | `magmas` | `Subquotients_with_category` |
| `Magmas.Unital.Algebras` | `magmas` | `Algebras` |
| `Magmas.Unital.CartesianProducts` | `magmas` | `CartesianProducts` |
| `Magmas.Unital.Inverse.CartesianProducts` | `magmas` | `CartesianProducts` |
| `Magmas.Unital.Realizations` | `magmas` | `Realizations` |
| `MagmasAndAdditiveMagmas.CartesianProducts` | `magmas_and_additive_magmas` | `CartesianProducts` |
| `MetricSpaces` | `metric_spaces` | (framework base) |
| `MetricSpaces.CartesianProducts` | `metric_spaces` | `CartesianProducts` |
| `MetricSpaces.Complete.CartesianProducts` | `metric_spaces` | `CartesianProducts` |
| `MetricSpaces.Homsets` | `metric_spaces` | `Homsets` |
| `MetricSpaces.WithRealizations` | `metric_spaces` | `WithRealizations` |
| `MetricSpacesCategory` | `metric_spaces` | (framework base) |
| `MetricSpaces_with_category` | `metric_spaces` | (framework base) |
| `ModularAbelianVarieties.Homsets` | `modular_abelian_varieties` | `Homsets` |
| `Modules.CartesianProducts` | `modules` | `CartesianProducts` |
| `Modules.FiniteDimensional.TensorProducts` | `modules` | `TensorProducts` |
| `Modules.Homsets` | `modules` | `Homsets` |
| `Modules.TensorProducts` | `modules` | `TensorProducts` |
| `ModulesWithBasis.CartesianProducts` | `modules_with_basis` | `CartesianProducts` |
| `ModulesWithBasis.DualObjects` | `modules_with_basis` | `DualObjects` |
| `ModulesWithBasis.Homsets` | `modules_with_basis` | `Homsets` |
| `ModulesWithBasis.TensorProducts` | `modules_with_basis` | `TensorProducts` |
| `Monoids.Algebras` | `monoids` | `Algebras` |
| `Monoids.CartesianProducts` | `monoids` | `CartesianProducts` |
| `Monoids.Subquotients` | `monoids` | `Subquotients` |
| `Monoids.Subquotients_with_category` | `monoids` | `Subquotients_with_category` |
| `Monoids.WithRealizations` | `monoids` | `WithRealizations` |
| `QuantumGroupRepresentations.TensorProducts` | `quantum_group_representations` | `TensorProducts` |
| `QuantumGroupRepresentations.WithBasis.TensorProducts` | `quantum_group_representations` | `TensorProducts` |
| `QuotientsCategory` | `quotients` | (framework base) |
| `RealizationsCategory` | `realizations` | (framework base) |
| `RegularCrystals.TensorProducts` | `regular_crystals` | `TensorProducts` |
| `RegularSuperCrystals.TensorProducts` | `regular_supercrystals` | `TensorProducts` |
| `AbelianVarieties.Homsets` | `schemes` | `Homsets` |
| `Semigroups.Algebras` | `semigroups` | `Algebras` |
| `Semigroups.CartesianProducts` | `semigroups` | `CartesianProducts` |
| `Semigroups.Quotients` | `semigroups` | `Quotients` |
| `Semigroups.Quotients_with_category` | `semigroups` | `Quotients_with_category` |
| `Semigroups.Subquotients` | `semigroups` | `Subquotients` |
| `Semigroups.Subquotients_with_category` | `semigroups` | `Subquotients_with_category` |
| `Sets.Algebras` | `sets_cat` | `Algebras` |
| `Sets.CartesianProducts` | `sets_cat` | `CartesianProducts` |
| `Sets.IsomorphicObjects` | `sets_cat` | `IsomorphicObjects` |
| `Sets.Quotients` | `sets_cat` | `Quotients` |
| `Sets.Quotients_with_category` | `sets_cat` | `Quotients_with_category` |
| `Sets.Realizations` | `sets_cat` | `Realizations` |
| `Sets.Subobjects` | `sets_cat` | `Subobjects` |
| `Sets.Subquotients` | `sets_cat` | `Subquotients` |
| `Sets.Subquotients_with_category` | `sets_cat` | `Subquotients_with_category` |
| `Sets.WithRealizations` | `sets_cat` | `WithRealizations` |
| `SignedTensorProductsCategory` | `signed_tensor` | (framework base) |
| `SimplicialSets.Homsets` | `simplicial_sets` | `Homsets` |
| `SubobjectsCategory` | `subobjects` | (framework base) |
| `SubquotientsCategory` | `subquotients` | (framework base) |
| `SuperAlgebras` | `super_algebras` | (framework base) |
| `SuperAlgebras.SignedTensorProducts` | `super_algebras` | `SignedTensorProducts` |
| `SuperAlgebrasWithBasis` | `super_algebras_with_basis` | (framework base) |
| `SuperAlgebrasWithBasis.SignedTensorProducts` | `super_algebras_with_basis` | `SignedTensorProducts` |
| `SuperHopfAlgebrasWithBasis` | `super_hopf_algebras_with_basis` | (framework base) |
| `SuperLieConformalAlgebras` | `super_lie_conformal_algebras` | (framework base) |
| `SuperLieConformalAlgebras.Graded` | `super_lie_conformal_algebras` | `Graded` |
| `SuperModules` | `super_modules` | (framework base) |
| `SuperModulesCategory` | `super_modules` | (framework base) |
| `SuperModulesWithBasis` | `super_modules_with_basis` | (framework base) |
| `SupercommutativeAlgebras.SignedTensorProducts` | `supercommutative_algebras` | `SignedTensorProducts` |
| `SuperCrystals.TensorProducts` | `supercrystals` | `TensorProducts` |
| `TensorProductsCategory` | `tensor` | (framework base) |
| `TopologicalSpaces` | `topological_spaces` | (framework base) |
| `TopologicalSpaces.CartesianProducts` | `topological_spaces` | `CartesianProducts` |
| `TopologicalSpaces.Compact.CartesianProducts` | `topological_spaces` | `CartesianProducts` |
| `TopologicalSpaces.Connected.CartesianProducts` | `topological_spaces` | `CartesianProducts` |
| `TopologicalSpacesCategory` | `topological_spaces` | (framework base) |
| `TopologicalSpaces_with_category` | `topological_spaces` | (framework base) |
| `UnitalAlgebras.CartesianProducts` | `unital_algebras` | `CartesianProducts` |
| `VectorSpaces.CartesianProducts` | `vector_spaces` | `CartesianProducts` |
| `VectorSpaces.DualObjects` | `vector_spaces` | `DualObjects` |
| `VectorSpaces.Filtered` | `vector_spaces` | `Filtered` |
| `VectorSpaces.FiniteDimensional.TensorProducts` | `vector_spaces` | `TensorProducts` |
| `VectorSpaces.Graded` | `vector_spaces` | `Graded` |
| `VectorSpaces.TensorProducts` | `vector_spaces` | `TensorProducts` |
| `VectorSpaces.WithBasis.CartesianProducts` | `vector_spaces` | `CartesianProducts` |
| `VectorSpaces.WithBasis.Filtered` | `vector_spaces` | `Filtered` |
| `VectorSpaces.WithBasis.FiniteDimensional.TensorProducts` | `vector_spaces` | `TensorProducts` |
| `VectorSpaces.WithBasis.Graded` | `vector_spaces` | `Graded` |
| `VectorSpaces.WithBasis.TensorProducts` | `vector_spaces` | `TensorProducts` |
| `WithRealizationsCategory` | `with_realizations` | (framework base) |

## Category instances constructed at import (130)

The classes above are vocabulary; Sage's working objects are category *instances*. A full import constructs 130 distinct instances (14 plain, 30 axiom-refined, 2 construction, 84 joins).
Each instance also synthesizes a dynamic `<Base>_with_category` class — 166 such classes load at import; they are machinery shadows of the instances below, not category vocabulary, and are excluded from the tables above on that ground.

### Join categories (84)

Joins are real meets in the category lattice — the intersection of their factors.
These are the ones the framework itself forms at import (∧ = meet).
**8 of the 84 print under a computed standard name** (axiom-joins: commutative semirings, infinite fields, the enumerated/infinite metric and topological spaces); **all 76 bare "Join of …" rows are Metric or Topological meets with the algebraic towers** (39 metric, 37 topological) — topological additive groups, metric monoids, topological semirings, and so on.
The entire unnamed layer is one declaration-gap surface: the `Topological`/`Metric` constructions have a declared nested class only at `Groups`.

A join can also expose missing theorem edges in Sage's subcategory lattice: `ZZ.category()` is the five-factor join of Dedekind domains ∧ euclidean domains ∧ noetherian rings ∧ infinite enumerated sets ∧ metric spaces because Sage knows `EuclideanDomains ⊂ PrincipalIdealDomains` but **not** `PID ⊂ DedekindDomains` or `PID ⊂ NoetherianRings` (both kernel-verified `is_subcategory` = False); mathematically the algebraic part collapses to euclidean domains.
These and related findings are collected under "Defects and gaps" on [Sage Category Framework Inventory](Sage-Category-Framework-Inventory.md).

Whether a meet prints under its standard mathematical name depends on two declaration mechanisms.
Axiom-joins auto-name: a join obtained by adjoining axioms to a single base renders as "finite commutative groups" (`JoinCategory._repr_object_names`, `category.py:3275`, via `_without_axioms` + the axiom set); a join of structurally unrelated categories raises there and falls back to the bare "Join of …" — the source's own failure example is the cross-tower `Category.join((Groups(), CommutativeAdditiveMonoids()))`. Separately, a category can declare a nested construction class: `Groups.Topological` (`groups.py:654`) makes `Groups().Topological()` print "Category of topological groups" as a real declared class, not a join.
`Groups` is the **only** category declaring a nested `Topological`, and none declares a nested `Metric` — so `AdditiveGroups().Topological()` (mathematically: topological additive groups) and `Groups().Metric()` (metric groups) remain bare joins below.
The unnamed rows are standard mathematical objects Sage constructs but has no declared name for.

The third column assigns each meet its **standard mathematical name**. These names are **project-assigned, not Sage's** — Sage prints the bare join — and exist so every instance is auditable against standard parlance.
Two conventions make this honest: naming the meet by the intended compatible notion (topological groups have continuous operations) follows Sage's own declared case (`Groups.Topological`, `groups.py:654`), and is exactly as declarative as every Sage category membership — no Sage category enforces its axioms.
Names marked ᴰ are systematic-descriptive, for tower-scaffolding stages with no established literature name; unmarked names are standard or standard-compositional (e.g. nonunital semirings).

| join category (Sage) | factors | standard name (project-assigned) |
| --- | --- | --- |
| Join of Category of Dedekind domains and Category of euclidean domains and Category of noetherian rings and Category of infinite enumerated sets and Category of metric spaces | Dedekind domains ∧ euclidean domains ∧ infinite enumerated sets ∧ metric spaces ∧ noetherian rings | infinite enumerated metric euclidean domains *(Dedekind/noetherian factors redundant — defect 1)* |
| Join of Category of additive associative distributive magmas and additive magmas and Category of metric spaces | additive associative distributive magmas and additive magmas ∧ metric spaces | metric distributive (·,+)-magmas with associative +ᴰ |
| Join of Category of additive associative distributive magmas and additive magmas and Category of topological spaces | additive associative distributive magmas and additive magmas ∧ topological spaces | topological distributive (·,+)-magmas with associative +ᴰ |
| Join of Category of additive commutative additive associative additive unital distributive magmas and additive magmas and Category of metric spaces | additive commutative additive associative additive unital distributive magmas and additive magmas ∧ metric spaces | metric distributive (·,+)-magmas with commutative monoid +ᴰ |
| Join of Category of additive commutative additive associative additive unital distributive magmas and additive magmas and Category of topological spaces | additive commutative additive associative additive unital distributive magmas and additive magmas ∧ topological spaces | topological distributive (·,+)-magmas with commutative monoid +ᴰ |
| Join of Category of additive commutative additive associative distributive magmas and additive magmas and Category of metric spaces | additive commutative additive associative distributive magmas and additive magmas ∧ metric spaces | metric distributive (·,+)-magmas with commutative associative +ᴰ |
| Join of Category of additive commutative additive associative distributive magmas and additive magmas and Category of topological spaces | additive commutative additive associative distributive magmas and additive magmas ∧ topological spaces | topological distributive (·,+)-magmas with commutative associative +ᴰ |
| Join of Category of additive commutative additive magmas and Category of metric spaces | additive commutative additive magmas ∧ metric spaces | metric commutative additive magmas |
| Join of Category of additive commutative additive magmas and Category of topological spaces | additive commutative additive magmas ∧ topological spaces | topological commutative additive magmas |
| Join of Category of additive groups and Category of metric spaces | additive groups ∧ metric spaces | metric additive groups |
| Join of Category of additive groups and Category of topological spaces | additive groups ∧ topological spaces | topological additive groups |
| Join of Category of additive inverse additive unital additive magmas and Category of metric spaces | additive inverse additive unital additive magmas ∧ metric spaces | metric additive magmas with zero and negationᴰ |
| Join of Category of additive inverse additive unital additive magmas and Category of topological spaces | additive inverse additive unital additive magmas ∧ topological spaces | topological additive magmas with zero and negationᴰ |
| Join of Category of additive magmas and Category of metric spaces | additive magmas ∧ metric spaces | metric additive magmas |
| Join of Category of additive magmas and Category of topological spaces | additive magmas ∧ topological spaces | topological additive magmas |
| Join of Category of additive monoids and Category of metric spaces | additive monoids ∧ metric spaces | metric additive monoids |
| Join of Category of additive monoids and Category of topological spaces | additive monoids ∧ topological spaces | topological additive monoids |
| Join of Category of additive semigroups and Category of metric spaces | additive semigroups ∧ metric spaces | metric additive semigroups |
| Join of Category of additive semigroups and Category of topological spaces | additive semigroups ∧ topological spaces | topological additive semigroups |
| Join of Category of additive unital additive magmas and Category of metric spaces | additive unital additive magmas ∧ metric spaces | metric additive magmas with zeroᴰ |
| Join of Category of additive unital additive magmas and Category of topological spaces | additive unital additive magmas ∧ topological spaces | topological additive magmas with zeroᴰ |
| Join of Category of associative additive commutative additive associative additive unital distributive magmas and additive magmas and Category of metric spaces | associative additive commutative additive associative additive unital distributive magmas and additive magmas ∧ metric spaces | metric nonunital semirings |
| Join of Category of associative additive commutative additive associative additive unital distributive magmas and additive magmas and Category of topological spaces | associative additive commutative additive associative additive unital distributive magmas and additive magmas ∧ topological spaces | topological nonunital semirings |
| Join of Category of commutative additive groups and Category of metric spaces | commutative additive groups ∧ metric spaces | metric abelian groups (additive) |
| Join of Category of commutative additive groups and Category of topological spaces | commutative additive groups ∧ topological spaces | topological abelian groups (additive) |
| Join of Category of commutative additive monoids and Category of metric spaces | commutative additive monoids ∧ metric spaces | metric commutative additive monoids |
| Join of Category of commutative additive monoids and Category of topological spaces | commutative additive monoids ∧ topological spaces | topological commutative additive monoids |
| Join of Category of commutative additive semigroups and Category of metric spaces | commutative additive semigroups ∧ metric spaces | metric commutative additive semigroups |
| Join of Category of commutative additive semigroups and Category of topological spaces | commutative additive semigroups ∧ topological spaces | topological commutative additive semigroups |
| Join of Category of commutative magmas and Category of metric spaces | commutative magmas ∧ metric spaces | metric commutative magmas |
| Join of Category of commutative magmas and Category of topological spaces | commutative magmas ∧ topological spaces | topological commutative magmas |
| Join of Category of commutative monoids and Category of metric spaces | commutative monoids ∧ metric spaces | metric commutative monoids |
| Join of Category of commutative monoids and Category of topological spaces | commutative monoids ∧ topological spaces | topological commutative monoids |
| Join of Category of commutative rings and Category of metric spaces | commutative rings ∧ metric spaces | metric commutative rings |
| Join of Category of commutative rings and Category of topological spaces | commutative rings ∧ topological spaces | topological commutative rings |
| Join of Category of distributive magmas and additive magmas and Category of metric spaces | distributive magmas and additive magmas ∧ metric spaces | metric distributive (·,+)-magmasᴰ |
| Join of Category of distributive magmas and additive magmas and Category of topological spaces | distributive magmas and additive magmas ∧ topological spaces | topological distributive (·,+)-magmasᴰ |
| Join of Category of division rings and Category of metric spaces | division rings ∧ metric spaces | metric division rings |
| Join of Category of division rings and Category of topological spaces | division rings ∧ topological spaces | topological division rings |
| Join of Category of domains and Category of metric spaces | domains ∧ metric spaces | metric domains |
| Join of Category of domains and Category of topological spaces | domains ∧ topological spaces | topological domains |
| Join of Category of euclidean domains and Category of metric spaces | euclidean domains ∧ metric spaces | metric euclidean domains |
| Join of Category of euclidean domains and Category of topological spaces | euclidean domains ∧ topological spaces | topological euclidean domains |
| Join of Category of fields and Category of metric spaces | fields ∧ metric spaces | metric fields |
| Join of Category of fields and Category of topological spaces | fields ∧ topological spaces | topological fields |
| Join of Category of gcd domains and Category of metric spaces | gcd domains ∧ metric spaces | metric GCD domains |
| Join of Category of gcd domains and Category of topological spaces | gcd domains ∧ topological spaces | topological GCD domains |
| Join of Category of integral domains and Category of metric spaces | integral domains ∧ metric spaces | metric integral domains |
| Join of Category of integral domains and Category of topological spaces | integral domains ∧ topological spaces | topological integral domains |
| Join of Category of magmas and Category of additive magmas and Category of metric spaces | additive magmas ∧ magmas ∧ metric spaces | metric (·,+)-magmasᴰ *(same content as the named class MagmasAndAdditiveMagmas)* |
| Join of Category of magmas and Category of additive magmas and Category of topological spaces | additive magmas ∧ magmas ∧ topological spaces | topological (·,+)-magmasᴰ *(same content as the named class MagmasAndAdditiveMagmas)* |
| Join of Category of magmas and Category of metric spaces | magmas ∧ metric spaces | metric magmas |
| Join of Category of magmas and Category of topological spaces | magmas ∧ topological spaces | topological magmas |
| Join of Category of magmas and additive magmas and Category of metric spaces | magmas and additive magmas ∧ metric spaces | metric (·,+)-magmasᴰ |
| Join of Category of magmas and additive magmas and Category of topological spaces | magmas and additive magmas ∧ topological spaces | topological (·,+)-magmasᴰ |
| Join of Category of monoids and Category of metric spaces | metric spaces ∧ monoids | metric monoids |
| Join of Category of monoids and Category of topological spaces | monoids ∧ topological spaces | topological monoids |
| Join of Category of noetherian rings and Category of metric spaces | metric spaces ∧ noetherian rings | metric noetherian rings |
| Join of Category of noetherian rings and Category of topological spaces | noetherian rings ∧ topological spaces | topological noetherian rings |
| Join of Category of number fields and Category of quotient fields and Category of metric spaces | metric spaces ∧ number fields ∧ quotient fields | metric number fields *(realized as fraction fields)* |
| Join of Category of principal ideal domains and Category of metric spaces | metric spaces ∧ principal ideal domains | metric principal ideal domains |
| Join of Category of principal ideal domains and Category of topological spaces | principal ideal domains ∧ topological spaces | topological principal ideal domains |
| Join of Category of quotient fields and Category of metric spaces | metric spaces ∧ quotient fields | metric fields realized as fraction fieldsᴰ *(Sage-specific category)* |
| Join of Category of quotient fields and Category of topological spaces | quotient fields ∧ topological spaces | topological fields realized as fraction fieldsᴰ *(Sage-specific category)* |
| Join of Category of rings and Category of metric spaces | metric spaces ∧ rings | metric rings |
| Join of Category of rings and Category of topological spaces | rings ∧ topological spaces | topological rings |
| Join of Category of rngs and Category of metric spaces | metric spaces ∧ rngs | metric rngs |
| Join of Category of rngs and Category of topological spaces | rngs ∧ topological spaces | topological rngs |
| Join of Category of semigroups and Category of metric spaces | metric spaces ∧ semigroups | metric semigroups |
| Join of Category of semigroups and Category of topological spaces | semigroups ∧ topological spaces | topological semigroups |
| Join of Category of semirings and Category of metric spaces | metric spaces ∧ semirings | metric semirings |
| Join of Category of semirings and Category of topological spaces | semirings ∧ topological spaces | topological semirings |
| Join of Category of unique factorization domains and Category of metric spaces | metric spaces ∧ unique factorization domains | metric unique factorization domains |
| Join of Category of unique factorization domains and Category of topological spaces | topological spaces ∧ unique factorization domains | topological unique factorization domains |
| Join of Category of unital magmas and Category of metric spaces | metric spaces ∧ unital magmas | metric unital magmas |
| Join of Category of unital magmas and Category of topological spaces | topological spaces ∧ unital magmas | topological unital magmas |
| commutative semirings | commutative monoids ∧ semirings | — (named by Sage) |
| enumerated metric spaces | enumerated sets ∧ metric spaces | — (named by Sage) |
| enumerated topological spaces | enumerated sets ∧ topological spaces | — (named by Sage) |
| infinite enumerated metric spaces | infinite enumerated sets ∧ metric spaces | — (named by Sage) |
| infinite enumerated topological spaces | infinite enumerated sets ∧ topological spaces | — (named by Sage) |
| infinite fields | fields ∧ infinite sets | — (named by Sage) |
| infinite metric spaces | infinite sets ∧ metric spaces | — (named by Sage) |
| infinite topological spaces | infinite sets ∧ topological spaces | — (named by Sage) |

## Remaining framework classes (3)

Genuine framework machinery and category classes defined outside `sage.categories` that load in a full-import session.

| class (qualname) | module | note |
| --- | --- | --- |
| `HopfAlgebras.DualCategory` | `hopf_algebras` | framework |
| `HopfAlgebras.Morphism` | `hopf_algebras` | framework |
| `Sets.WithRealizations.ParentMethods.Realizations` | `sets_cat` | framework |
