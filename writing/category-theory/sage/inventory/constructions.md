# Sage functorial constructions

## Algebras {#con-algebras}

| field | value |
| --- | --- |
| flavor | covariant |
| implementation class | `algebra_functor.AlgebrasCategory` |
| implementation | [`src/sage/categories/algebra_functor.py:668`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebra_functor.py#L668) |
| other classes with the same functor tag | `algebra_functor.AlgebraFunctor` |
| interface declarations | `sets_cat.Sets:Algebras` |
| specialized implementations | `additive_groups.AdditiveGroups:Algebras [nested category class]; additive_groups.AdditiveGroups:Finite.Algebras [nested category class]; additive_magmas.AdditiveMagmas:AdditiveCommutative.Algebras [nested category class]; additive_magmas.AdditiveMagmas:AdditiveUnital.Algebras [nested category class]; additive_magmas.AdditiveMagmas:Algebras [nested category class]; additive_semigroups.AdditiveSemigroups:Algebras [nested category class]; commutative_additive_groups.CommutativeAdditiveGroups:Algebras [nested category class]; coxeter_groups.CoxeterGroups:Algebras [lazy-import binding]; finite_groups.FiniteGroups:Algebras [nested category class]; finite_sets.FiniteSets:Algebras [nested category class]; groups.Groups:Algebras [lazy-import binding]; magmas.Magmas:Algebras [nested category class]; magmas.Magmas:Commutative.Algebras [nested category class]; magmas.Magmas:Unital.Algebras [nested category class]; monoids.Monoids:Algebras [nested category class]; semigroups.Semigroups:Algebras [nested category class]; sets_cat.Sets:Algebras [nested category class]` |
| named result categories | `coxeter_group_algebras.CoxeterGroupAlgebras; group_algebras.GroupAlgebras` |

### Declared in (18)

| category | declaration | source |
| --- | --- | --- |
| [`AdditiveGroups`](categories.md#cat-additivegroups) | nested category class | [`src/sage/categories/additive_groups.py:58`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L58) |
| [`AdditiveGroups`](categories.md#cat-additivegroups) | nested category class | [`src/sage/categories/additive_groups.py:63`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L63) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:580`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L580) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:965`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L965) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:492`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L492) |
| [`AdditiveSemigroups`](categories.md#cat-additivesemigroups) | nested category class | [`src/sage/categories/additive_semigroups.py:123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L123) |
| [`CommutativeAdditiveGroups`](categories.md#cat-commutativeadditivegroups) | nested category class | [`src/sage/categories/commutative_additive_groups.py:98`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_additive_groups.py#L98) |
| [`CoxeterGroups`](categories.md#cat-coxetergroups) | lazy-import binding | [`src/sage/categories/coxeter_groups.py:130`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coxeter_groups.py#L130) |
| [`FiniteGroups`](categories.md#cat-finitegroups) | nested category class | [`src/sage/categories/finite_groups.py:183`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_groups.py#L183) |
| [`FiniteSets`](categories.md#cat-finitesets) | nested category class | [`src/sage/categories/finite_sets.py:91`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L91) |
| [`Groups`](categories.md#cat-groups) | lazy-import binding | [`src/sage/categories/groups.py:493`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L493) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:349`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L349) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:415`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L415) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:694`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L694) |
| [`Monoids`](categories.md#cat-monoids) | nested category class | [`src/sage/categories/monoids.py:484`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L484) |
| [`Semigroups`](categories.md#cat-semigroups) | nested category class | [`src/sage/categories/semigroups.py:872`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L872) |
| [`Sets`](categories.md#cat-sets) | nested category class | [`src/sage/categories/sets_cat.py:2721`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2721) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:695`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L695) |

### Classes the framework generates at 10.10 (15)

| class | module |
| --- | --- |
| `AdditiveGroups.Algebras` | `additive_groups` |
| `AdditiveGroups.Finite.Algebras` | `additive_groups` |
| `AdditiveMagmas.AdditiveCommutative.Algebras` | `additive_magmas` |
| `AdditiveMagmas.AdditiveUnital.Algebras` | `additive_magmas` |
| `AdditiveMagmas.Algebras` | `additive_magmas` |
| `AdditiveSemigroups.Algebras` | `additive_semigroups` |
| `CommutativeAdditiveGroups.Algebras` | `commutative_additive_groups` |
| `FiniteGroups.Algebras` | `finite_groups` |
| `FiniteSets.Algebras` | `finite_sets` |
| `Magmas.Algebras` | `magmas` |
| `Magmas.Commutative.Algebras` | `magmas` |
| `Magmas.Unital.Algebras` | `magmas` |
| `Monoids.Algebras` | `monoids` |
| `Semigroups.Algebras` | `semigroups` |
| `Sets.Algebras` | `sets_cat` |

## CartesianProducts {#con-cartesianproducts}

| field | value |
| --- | --- |
| flavor | covariant |
| implementation class | `cartesian_product.CartesianProductsCategory` |
| implementation | [`src/sage/categories/cartesian_product.py:240`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cartesian_product.py#L240) |
| other classes with the same functor tag | `cartesian_product.CartesianProductFunctor` |
| interface declarations | `sets_cat.Sets:CartesianProducts` |
| specialized implementations | `additive_magmas.AdditiveMagmas:AdditiveCommutative.CartesianProducts [nested category class]; additive_magmas.AdditiveMagmas:AdditiveUnital.AdditiveInverse.CartesianProducts [nested category class]; additive_magmas.AdditiveMagmas:AdditiveUnital.CartesianProducts [nested category class]; additive_magmas.AdditiveMagmas:CartesianProducts [nested category class]; additive_semigroups.AdditiveSemigroups:CartesianProducts [nested category class]; algebras.Algebras:CartesianProducts [nested category class]; algebras_with_basis.AlgebrasWithBasis:CartesianProducts [nested category class]; cartesian_product.CartesianProductsCategory:CartesianProducts [category method]; commutative_additive_groups.CommutativeAdditiveGroups:CartesianProducts [nested category class]; commutative_rings.CommutativeRings:CartesianProducts [nested category class]; distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas:CartesianProducts [nested category class]; enumerated_sets.EnumeratedSets:CartesianProducts [nested category class]; finite_enumerated_sets.FiniteEnumeratedSets:CartesianProducts [nested category class]; groups.Groups:CartesianProducts [nested category class]; magmas.Magmas:CartesianProducts [nested category class]; magmas.Magmas:Commutative.CartesianProducts [nested category class]; magmas.Magmas:Unital.CartesianProducts [nested category class]; magmas.Magmas:Unital.Inverse.CartesianProducts [nested category class]; magmas_and_additive_magmas.MagmasAndAdditiveMagmas:CartesianProducts [nested category class]; metric_spaces.MetricSpaces:CartesianProducts [nested category class]; metric_spaces.MetricSpaces:Complete.CartesianProducts [nested category class]; modules.Modules:CartesianProducts [nested category class]; modules_with_basis.ModulesWithBasis:CartesianProducts [nested category class]; monoids.Monoids:CartesianProducts [nested category class]; semigroups.Semigroups:CartesianProducts [nested category class]; sets_cat.Sets:CartesianProducts [nested category class]; topological_spaces.TopologicalSpaces:CartesianProducts [nested category class]; topological_spaces.TopologicalSpaces:Compact.CartesianProducts [nested category class]; topological_spaces.TopologicalSpaces:Connected.CartesianProducts [nested category class]; unital_algebras.UnitalAlgebras:CartesianProducts [nested category class]; vector_spaces.VectorSpaces:CartesianProducts [nested category class]; vector_spaces.VectorSpaces:WithBasis.CartesianProducts [nested category class]` |

### Declared in (33)

| category | declaration | source |
| --- | --- | --- |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:564`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L564) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:899`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L899) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:936`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L936) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:452`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L452) |
| [`AdditiveSemigroups`](categories.md#cat-additivesemigroups) | nested category class | [`src/sage/categories/additive_semigroups.py:105`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L105) |
| [`Algebras`](categories.md#cat-algebras) | nested category class | [`src/sage/categories/algebras.py:273`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L273) |
| [`AlgebrasWithBasis`](categories.md#cat-algebraswithbasis) | nested category class | [`src/sage/categories/algebras_with_basis.py:200`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L200) |
| [`CartesianProductsCategory`](categories.md#cat-cartesianproductscategory) | category method | [`src/sage/categories/cartesian_product.py:252`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cartesian_product.py#L252) |
| [`CommutativeAdditiveGroups`](categories.md#cat-commutativeadditivegroups) | nested category class | [`src/sage/categories/commutative_additive_groups.py:61`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_additive_groups.py#L61) |
| [`CommutativeRings`](categories.md#cat-commutativerings) | nested category class | [`src/sage/categories/commutative_rings.py:992`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_rings.py#L992) |
| [`DistributiveMagmasAndAdditiveMagmas`](categories.md#cat-distributivemagmasandadditivemagmas) | nested category class | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:84`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L84) |
| [`EnumeratedSets`](categories.md#cat-enumeratedsets) | nested category class | [`src/sage/categories/enumerated_sets.py:1126`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L1126) |
| [`FiniteEnumeratedSets`](categories.md#cat-finiteenumeratedsets) | nested category class | [`src/sage/categories/finite_enumerated_sets.py:662`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_enumerated_sets.py#L662) |
| [`Groups`](categories.md#cat-groups) | nested category class | [`src/sage/categories/groups.py:547`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L547) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:1038`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L1038) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:441`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L441) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:615`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L615) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:599`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L599) |
| [`MagmasAndAdditiveMagmas`](categories.md#cat-magmasandadditivemagmas) | nested category class | [`src/sage/categories/magmas_and_additive_magmas.py:136`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L136) |
| [`MetricSpaces`](categories.md#cat-metricspaces) | nested category class | [`src/sage/categories/metric_spaces.py:283`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L283) |
| [`MetricSpaces`](categories.md#cat-metricspaces) | nested category class | [`src/sage/categories/metric_spaces.py:352`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L352) |
| [`Modules`](categories.md#cat-modules) | nested category class | [`src/sage/categories/modules.py:832`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L832) |
| [`ModulesWithBasis`](categories.md#cat-moduleswithbasis) | nested category class | [`src/sage/categories/modules_with_basis.py:2576`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L2576) |
| [`Monoids`](categories.md#cat-monoids) | nested category class | [`src/sage/categories/monoids.py:626`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L626) |
| [`Semigroups`](categories.md#cat-semigroups) | nested category class | [`src/sage/categories/semigroups.py:856`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L856) |
| [`Sets`](categories.md#cat-sets) | nested category class | [`src/sage/categories/sets_cat.py:2185`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2185) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:303`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L303) |
| [`TopologicalSpaces`](categories.md#cat-topologicalspaces) | nested category class | [`src/sage/categories/topological_spaces.py:65`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L65) |
| [`TopologicalSpaces`](categories.md#cat-topologicalspaces) | nested category class | [`src/sage/categories/topological_spaces.py:151`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L151) |
| [`TopologicalSpaces`](categories.md#cat-topologicalspaces) | nested category class | [`src/sage/categories/topological_spaces.py:126`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L126) |
| [`UnitalAlgebras`](categories.md#cat-unitalalgebras) | nested category class | [`src/sage/categories/unital_algebras.py:373`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/unital_algebras.py#L373) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:322`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L322) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:199`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L199) |

### Classes the framework generates at 10.10 (31)

| class | module |
| --- | --- |
| `AdditiveMagmas.AdditiveCommutative.CartesianProducts` | `additive_magmas` |
| `AdditiveMagmas.AdditiveUnital.AdditiveInverse.CartesianProducts` | `additive_magmas` |
| `AdditiveMagmas.AdditiveUnital.CartesianProducts` | `additive_magmas` |
| `AdditiveMagmas.CartesianProducts` | `additive_magmas` |
| `AdditiveSemigroups.CartesianProducts` | `additive_semigroups` |
| `Algebras.CartesianProducts` | `algebras` |
| `AlgebrasWithBasis.CartesianProducts` | `algebras_with_basis` |
| `CommutativeAdditiveGroups.CartesianProducts` | `commutative_additive_groups` |
| `CommutativeRings.CartesianProducts` | `commutative_rings` |
| `DistributiveMagmasAndAdditiveMagmas.CartesianProducts` | `distributive_magmas_and_additive_magmas` |
| `EnumeratedSets.CartesianProducts` | `enumerated_sets` |
| `FiniteEnumeratedSets.CartesianProducts` | `finite_enumerated_sets` |
| `Groups.CartesianProducts` | `groups` |
| `Magmas.CartesianProducts` | `magmas` |
| `Magmas.Commutative.CartesianProducts` | `magmas` |
| `Magmas.Unital.CartesianProducts` | `magmas` |
| `Magmas.Unital.Inverse.CartesianProducts` | `magmas` |
| `MagmasAndAdditiveMagmas.CartesianProducts` | `magmas_and_additive_magmas` |
| `MetricSpaces.CartesianProducts` | `metric_spaces` |
| `MetricSpaces.Complete.CartesianProducts` | `metric_spaces` |
| `Modules.CartesianProducts` | `modules` |
| `ModulesWithBasis.CartesianProducts` | `modules_with_basis` |
| `Monoids.CartesianProducts` | `monoids` |
| `Semigroups.CartesianProducts` | `semigroups` |
| `Sets.CartesianProducts` | `sets_cat` |
| `TopologicalSpaces.CartesianProducts` | `topological_spaces` |
| `TopologicalSpaces.Compact.CartesianProducts` | `topological_spaces` |
| `TopologicalSpaces.Connected.CartesianProducts` | `topological_spaces` |
| `UnitalAlgebras.CartesianProducts` | `unital_algebras` |
| `VectorSpaces.CartesianProducts` | `vector_spaces` |
| `VectorSpaces.WithBasis.CartesianProducts` | `vector_spaces` |

## DualObjects {#con-dualobjects}

| field | value |
| --- | --- |
| flavor | covariant |
| implementation class | `dual.DualObjectsCategory` |
| implementation | [`src/sage/categories/dual.py:31`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/dual.py#L31) |
| other classes with the same functor tag | `dual.DualFunctor` |
| interface declarations | `modules.Modules:DualObjects; modules.Modules:dual` |
| specialized implementations | `algebras.Algebras:DualObjects [nested category class]; coalgebras.Coalgebras:DualObjects [nested category class]; modules_with_basis.ModulesWithBasis:DualObjects [nested category class]; vector_spaces.VectorSpaces:DualObjects [nested category class]` |

### Declared in (6)

| category | declaration | source |
| --- | --- | --- |
| [`Algebras`](categories.md#cat-algebras) | nested category class | [`src/sage/categories/algebras.py:325`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L325) |
| [`Coalgebras`](categories.md#cat-coalgebras) | nested category class | [`src/sage/categories/coalgebras.py:210`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L210) |
| [`Modules`](categories.md#cat-modules) | subcategory interface method | [`src/sage/categories/modules.py:263`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L263) |
| [`Modules`](categories.md#cat-modules) | subcategory API alias | [`src/sage/categories/modules.py:338`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L338) |
| [`ModulesWithBasis`](categories.md#cat-moduleswithbasis) | nested category class | [`src/sage/categories/modules_with_basis.py:2781`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L2781) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:303`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L303) |

### Classes the framework generates at 10.10 (4)

| class | module |
| --- | --- |
| `Algebras.DualObjects` | `algebras` |
| `Coalgebras.DualObjects` | `coalgebras` |
| `ModulesWithBasis.DualObjects` | `modules_with_basis` |
| `VectorSpaces.DualObjects` | `vector_spaces` |

## Filtered {#con-filtered}

| field | value |
| --- | --- |
| flavor | regressive covariant |
| implementation class | `filtered_modules.FilteredModulesCategory` |
| implementation | [`src/sage/categories/filtered_modules.py:58`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules.py#L58) |
| interface declarations | `modules.Modules:Filtered` |
| specialized implementations | `algebras.Algebras:Filtered [lazy-import binding]; algebras_with_basis.AlgebrasWithBasis:Filtered [lazy-import binding]; coalgebras.Coalgebras:Filtered [nested category class]; coalgebras_with_basis.CoalgebrasWithBasis:Filtered [nested category class]; hopf_algebras_with_basis.HopfAlgebrasWithBasis:Filtered [lazy-import binding]; modules.Modules:Filtered [lazy-import binding]; modules_with_basis.ModulesWithBasis:Filtered [lazy-import binding]; vector_spaces.VectorSpaces:Filtered [nested category class]; vector_spaces.VectorSpaces:WithBasis.Filtered [nested category class]` |
| named result categories | `filtered_algebras.FilteredAlgebras; filtered_algebras_with_basis.FilteredAlgebrasWithBasis; filtered_hopf_algebras_with_basis.FilteredHopfAlgebrasWithBasis; filtered_modules.FilteredModules; filtered_modules_with_basis.FilteredModulesWithBasis` |

### Declared in (10)

| category | declaration | source |
| --- | --- | --- |
| [`Algebras`](categories.md#cat-algebras) | lazy-import binding | [`src/sage/categories/algebras.py:131`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L131) |
| [`AlgebrasWithBasis`](categories.md#cat-algebraswithbasis) | lazy-import binding | [`src/sage/categories/algebras_with_basis.py:124`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L124) |
| [`Coalgebras`](categories.md#cat-coalgebras) | nested category class | [`src/sage/categories/coalgebras.py:288`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L288) |
| [`CoalgebrasWithBasis`](categories.md#cat-coalgebraswithbasis) | nested category class | [`src/sage/categories/coalgebras_with_basis.py:42`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras_with_basis.py#L42) |
| [`HopfAlgebrasWithBasis`](categories.md#cat-hopfalgebraswithbasis) | lazy-import binding | [`src/sage/categories/hopf_algebras_with_basis.py:159`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L159) |
| [`Modules`](categories.md#cat-modules) | lazy-import binding | [`src/sage/categories/modules.py:593`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L593) |
| [`Modules`](categories.md#cat-modules) | subcategory interface method | [`src/sage/categories/modules.py:384`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L384) |
| [`ModulesWithBasis`](categories.md#cat-moduleswithbasis) | lazy-import binding | [`src/sage/categories/modules_with_basis.py:196`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L196) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:348`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L348) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:264`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L264) |

### Classes the framework generates at 10.10 (4)

| class | module |
| --- | --- |
| `Coalgebras.Filtered` | `coalgebras` |
| `CoalgebrasWithBasis.Filtered` | `coalgebras_with_basis` |
| `VectorSpaces.Filtered` | `vector_spaces` |
| `VectorSpaces.WithBasis.Filtered` | `vector_spaces` |

## Graded {#con-graded}

| field | value |
| --- | --- |
| flavor | regressive covariant |
| implementation class | `graded_modules.GradedModulesCategory` |
| implementation | [`src/sage/categories/graded_modules.py:47`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_modules.py#L47) |
| interface declarations | `modules.Modules:Graded` |
| specialized implementations | `algebras.Algebras:Graded [lazy-import binding]; algebras_with_basis.AlgebrasWithBasis:Graded [lazy-import binding]; coalgebras.Coalgebras:Graded [lazy-import binding]; coalgebras_with_basis.CoalgebrasWithBasis:Graded [lazy-import binding]; finitely_generated_lambda_bracket_algebras.FinitelyGeneratedLambdaBracketAlgebras:Graded [nested category class]; finitely_generated_lie_conformal_algebras.FinitelyGeneratedLieConformalAlgebras:Graded [nested category class]; finitely_generated_lie_conformal_algebras.FinitelyGeneratedLieConformalAlgebras:Super.Graded [nested category class]; hopf_algebras_with_basis.HopfAlgebrasWithBasis:Graded [lazy-import binding]; lambda_bracket_algebras_with_basis.LambdaBracketAlgebrasWithBasis:FinitelyGeneratedAsLambdaBracketAlgebra.Graded [nested category class]; lie_algebras.LieAlgebras:Graded [lazy-import binding]; lie_algebras_with_basis.LieAlgebrasWithBasis:Graded [lazy-import binding]; lie_conformal_algebras.LieConformalAlgebras:Graded [lazy-import binding]; lie_conformal_algebras_with_basis.LieConformalAlgebrasWithBasis:FinitelyGeneratedAsLambdaBracketAlgebra.Graded [nested category class]; lie_conformal_algebras_with_basis.LieConformalAlgebrasWithBasis:FinitelyGeneratedAsLambdaBracketAlgebra.Super.Graded [nested category class]; lie_conformal_algebras_with_basis.LieConformalAlgebrasWithBasis:Graded [nested category class]; lie_conformal_algebras_with_basis.LieConformalAlgebrasWithBasis:Super.Graded [nested category class]; modules.Modules:Graded [lazy-import binding]; modules_with_basis.ModulesWithBasis:Graded [lazy-import binding]; super_lie_conformal_algebras.SuperLieConformalAlgebras:Graded [nested category class]; vector_spaces.VectorSpaces:Graded [nested category class]; vector_spaces.VectorSpaces:WithBasis.Graded [nested category class]` |
| named result categories | `graded_algebras.GradedAlgebras; graded_algebras_with_basis.GradedAlgebrasWithBasis; graded_bialgebras.GradedBialgebras; graded_bialgebras_with_basis.GradedBialgebrasWithBasis; graded_coalgebras.GradedCoalgebras; graded_coalgebras_with_basis.GradedCoalgebrasWithBasis; graded_hopf_algebras.GradedHopfAlgebras; graded_hopf_algebras_with_basis.GradedHopfAlgebrasWithBasis; graded_lie_algebras.GradedLieAlgebras; graded_lie_algebras_with_basis.GradedLieAlgebrasWithBasis; graded_lie_conformal_algebras.GradedLieConformalAlgebras; graded_lie_conformal_algebras.GradedLieConformalAlgebrasCategory; graded_modules.GradedModules; graded_modules_with_basis.GradedModulesWithBasis` |

### Declared in (22)

| category | declaration | source |
| --- | --- | --- |
| [`Algebras`](categories.md#cat-algebras) | lazy-import binding | [`src/sage/categories/algebras.py:133`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L133) |
| [`AlgebrasWithBasis`](categories.md#cat-algebraswithbasis) | lazy-import binding | [`src/sage/categories/algebras_with_basis.py:126`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L126) |
| [`Coalgebras`](categories.md#cat-coalgebras) | lazy-import binding | [`src/sage/categories/coalgebras.py:52`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L52) |
| [`CoalgebrasWithBasis`](categories.md#cat-coalgebraswithbasis) | lazy-import binding | [`src/sage/categories/coalgebras_with_basis.py:39`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras_with_basis.py#L39) |
| [`FinitelyGeneratedLambdaBracketAlgebras`](categories.md#cat-finitelygeneratedlambdabracketalgebras) | nested category class | [`src/sage/categories/finitely_generated_lambda_bracket_algebras.py:92`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lambda_bracket_algebras.py#L92) |
| [`FinitelyGeneratedLieConformalAlgebras`](categories.md#cat-finitelygeneratedlieconformalalgebras) | nested category class | [`src/sage/categories/finitely_generated_lie_conformal_algebras.py:93`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lie_conformal_algebras.py#L93) |
| [`FinitelyGeneratedLieConformalAlgebras`](categories.md#cat-finitelygeneratedlieconformalalgebras) | nested category class | [`src/sage/categories/finitely_generated_lie_conformal_algebras.py:70`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lie_conformal_algebras.py#L70) |
| [`HopfAlgebrasWithBasis`](categories.md#cat-hopfalgebraswithbasis) | lazy-import binding | [`src/sage/categories/hopf_algebras_with_basis.py:161`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L161) |
| [`LambdaBracketAlgebrasWithBasis`](categories.md#cat-lambdabracketalgebraswithbasis) | nested category class | [`src/sage/categories/lambda_bracket_algebras_with_basis.py:79`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras_with_basis.py#L79) |
| [`LieAlgebras`](categories.md#cat-liealgebras) | lazy-import binding | [`src/sage/categories/lie_algebras.py:112`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L112) |
| [`LieAlgebrasWithBasis`](categories.md#cat-liealgebraswithbasis) | lazy-import binding | [`src/sage/categories/lie_algebras_with_basis.py:55`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras_with_basis.py#L55) |
| [`LieConformalAlgebras`](categories.md#cat-lieconformalalgebras) | lazy-import binding | [`src/sage/categories/lie_conformal_algebras.py:338`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras.py#L338) |
| [`LieConformalAlgebrasWithBasis`](categories.md#cat-lieconformalalgebraswithbasis) | nested category class | [`src/sage/categories/lie_conformal_algebras_with_basis.py:136`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L136) |
| [`LieConformalAlgebrasWithBasis`](categories.md#cat-lieconformalalgebraswithbasis) | nested category class | [`src/sage/categories/lie_conformal_algebras_with_basis.py:110`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L110) |
| [`LieConformalAlgebrasWithBasis`](categories.md#cat-lieconformalalgebraswithbasis) | nested category class | [`src/sage/categories/lie_conformal_algebras_with_basis.py:75`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L75) |
| [`LieConformalAlgebrasWithBasis`](categories.md#cat-lieconformalalgebraswithbasis) | nested category class | [`src/sage/categories/lie_conformal_algebras_with_basis.py:64`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L64) |
| [`Modules`](categories.md#cat-modules) | lazy-import binding | [`src/sage/categories/modules.py:594`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L594) |
| [`Modules`](categories.md#cat-modules) | subcategory interface method | [`src/sage/categories/modules.py:420`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L420) |
| [`ModulesWithBasis`](categories.md#cat-moduleswithbasis) | lazy-import binding | [`src/sage/categories/modules_with_basis.py:197`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L197) |
| [`SuperLieConformalAlgebras`](categories.md#cat-superlieconformalalgebras) | nested category class | [`src/sage/categories/super_lie_conformal_algebras.py:174`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_lie_conformal_algebras.py#L174) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:353`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L353) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:243`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L243) |

### Classes the framework generates at 10.10 (11)

| class | module |
| --- | --- |
| `FinitelyGeneratedLambdaBracketAlgebras.Graded` | `finitely_generated_lambda_bracket_algebras` |
| `FinitelyGeneratedLieConformalAlgebras.Graded` | `finitely_generated_lie_conformal_algebras` |
| `FinitelyGeneratedLieConformalAlgebras.Super.Graded` | `finitely_generated_lie_conformal_algebras` |
| `LambdaBracketAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Graded` | `lambda_bracket_algebras_with_basis` |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Graded` | `lie_conformal_algebras_with_basis` |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Super.Graded` | `lie_conformal_algebras_with_basis` |
| `LieConformalAlgebrasWithBasis.Graded` | `lie_conformal_algebras_with_basis` |
| `LieConformalAlgebrasWithBasis.Super.Graded` | `lie_conformal_algebras_with_basis` |
| `SuperLieConformalAlgebras.Graded` | `super_lie_conformal_algebras` |
| `VectorSpaces.Graded` | `vector_spaces` |
| `VectorSpaces.WithBasis.Graded` | `vector_spaces` |

## Homsets {#con-homsets}

| field | value |
| --- | --- |
| flavor | general/specialized functorial |
| implementation class | `homsets.HomsetsCategory` |
| implementation | [`src/sage/categories/homsets.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/homsets.py#L20) |
| interface declarations | `objects.Objects:Homsets` |
| specialized implementations | `additive_magmas.AdditiveMagmas:AdditiveUnital.Homsets [nested category class]; additive_magmas.AdditiveMagmas:Homsets [nested category class]; additive_monoids.AdditiveMonoids:Homsets [nested category class]; additive_semigroups.AdditiveSemigroups:Homsets [nested category class]; drinfeld_modules.DrinfeldModules:Homsets [category method]; finite_dimensional_modules_with_basis.FiniteDimensionalModulesWithBasis:Homsets [nested category class]; hecke_modules.HeckeModules:Homsets [nested category class]; metric_spaces.MetricSpaces:Homsets [nested category class]; modular_abelian_varieties.ModularAbelianVarieties:Homsets [nested category class]; modules.Modules:Homsets [nested category class]; modules_with_basis.ModulesWithBasis:Homsets [nested category class]; schemes.AbelianVarieties:Homsets [nested category class]; simplicial_sets.SimplicialSets:Homsets [nested category class]` |
| named result categories | `homsets.HomsetsOf` |

### Declared in (14)

| category | declaration | source |
| --- | --- | --- |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:857`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L857) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:438`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L438) |
| [`AdditiveMonoids`](categories.md#cat-additivemonoids) | nested category class | [`src/sage/categories/additive_monoids.py:89`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L89) |
| [`AdditiveSemigroups`](categories.md#cat-additivesemigroups) | nested category class | [`src/sage/categories/additive_semigroups.py:88`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L88) |
| [`DrinfeldModules`](categories.md#cat-drinfeldmodules) | category method | [`src/sage/categories/drinfeld_modules.py:313`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/drinfeld_modules.py#L313) |
| [`FiniteDimensionalModulesWithBasis`](categories.md#cat-finitedimensionalmoduleswithbasis) | nested category class | [`src/sage/categories/finite_dimensional_modules_with_basis.py:890`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L890) |
| [`HeckeModules`](categories.md#cat-heckemodules) | nested category class | [`src/sage/categories/hecke_modules.py:158`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hecke_modules.py#L158) |
| [`MetricSpaces`](categories.md#cat-metricspaces) | nested category class | [`src/sage/categories/metric_spaces.py:224`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L224) |
| [`ModularAbelianVarieties`](categories.md#cat-modularabelianvarieties) | nested category class | [`src/sage/categories/modular_abelian_varieties.py:65`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modular_abelian_varieties.py#L65) |
| [`Modules`](categories.md#cat-modules) | nested category class | [`src/sage/categories/modules.py:720`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L720) |
| [`ModulesWithBasis`](categories.md#cat-moduleswithbasis) | nested category class | [`src/sage/categories/modules_with_basis.py:2458`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L2458) |
| [`Objects`](categories.md#cat-objects) | subcategory interface method | [`src/sage/categories/objects.py:82`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/objects.py#L82) |
| [`AbelianVarieties`](categories.md#cat-abelianvarieties) | nested category class | [`src/sage/categories/schemes.py:267`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L267) |
| [`SimplicialSets`](categories.md#cat-simplicialsets) | nested category class | [`src/sage/categories/simplicial_sets.py:157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L157) |

### Classes the framework generates at 10.10 (12)

| class | module |
| --- | --- |
| `AdditiveMagmas.AdditiveUnital.Homsets` | `additive_magmas` |
| `AdditiveMagmas.Homsets` | `additive_magmas` |
| `AdditiveMonoids.Homsets` | `additive_monoids` |
| `AdditiveSemigroups.Homsets` | `additive_semigroups` |
| `FiniteDimensionalModulesWithBasis.Homsets` | `finite_dimensional_modules_with_basis` |
| `HeckeModules.Homsets` | `hecke_modules` |
| `MetricSpaces.Homsets` | `metric_spaces` |
| `ModularAbelianVarieties.Homsets` | `modular_abelian_varieties` |
| `Modules.Homsets` | `modules` |
| `ModulesWithBasis.Homsets` | `modules_with_basis` |
| `AbelianVarieties.Homsets` | `schemes` |
| `SimplicialSets.Homsets` | `simplicial_sets` |

## IsomorphicObjects {#con-isomorphicobjects}

| field | value |
| --- | --- |
| flavor | regressive covariant |
| implementation class | `isomorphic_objects.IsomorphicObjectsCategory` |
| implementation | [`src/sage/categories/isomorphic_objects.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/isomorphic_objects.py#L21) |
| interface declarations | `sets_cat.Sets:IsomorphicObjects` |
| specialized implementations | `finite_enumerated_sets.FiniteEnumeratedSets:IsomorphicObjects [nested category class]; sets_cat.Sets:IsomorphicObjects [nested category class]` |

### Declared in (3)

| category | declaration | source |
| --- | --- | --- |
| [`FiniteEnumeratedSets`](categories.md#cat-finiteenumeratedsets) | nested category class | [`src/sage/categories/finite_enumerated_sets.py:820`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_enumerated_sets.py#L820) |
| [`Sets`](categories.md#cat-sets) | nested category class | [`src/sage/categories/sets_cat.py:2156`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2156) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:575`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L575) |

### Classes the framework generates at 10.10 (2)

| class | module |
| --- | --- |
| `FiniteEnumeratedSets.IsomorphicObjects` | `finite_enumerated_sets` |
| `Sets.IsomorphicObjects` | `sets_cat` |

## Metric {#con-metric}

| field | value |
| --- | --- |
| flavor | regressive covariant |
| implementation class | `metric_spaces.MetricSpacesCategory` |
| implementation | [`src/sage/categories/metric_spaces.py:22`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L22) |
| interface declarations | `sets_cat.Sets:Metric` |
| specialized implementations | `sets_cat.Sets:Metric [lazy-import binding]` |
| named result categories | `metric_spaces.MetricSpaces` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Sets`](categories.md#cat-sets) | lazy-import binding | [`src/sage/categories/sets_cat.py:1883`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1883) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:683`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L683) |

## Quotients {#con-quotients}

| field | value |
| --- | --- |
| flavor | regressive covariant |
| implementation class | `quotients.QuotientsCategory` |
| implementation | [`src/sage/categories/quotients.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quotients.py#L21) |
| interface declarations | `sets_cat.Sets:Quotients` |
| specialized implementations | `algebras.Algebras:Quotients [nested category class]; graded_modules_with_basis.GradedModulesWithBasis:Quotients [nested category class]; semigroups.Semigroups:Quotients [nested category class]; sets_cat.Sets:Quotients [nested category class]` |

### Declared in (5)

| category | declaration | source |
| --- | --- | --- |
| [`Algebras`](categories.md#cat-algebras) | nested category class | [`src/sage/categories/algebras.py:247`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L247) |
| [`GradedModulesWithBasis`](categories.md#cat-gradedmoduleswithbasis) | nested category class | [`src/sage/categories/graded_modules_with_basis.py:290`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_modules_with_basis.py#L290) |
| [`Semigroups`](categories.md#cat-semigroups) | nested category class | [`src/sage/categories/semigroups.py:826`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L826) |
| [`Sets`](categories.md#cat-sets) | nested category class | [`src/sage/categories/sets_cat.py:2081`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2081) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:462`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L462) |

### Classes the framework generates at 10.10 (4)

| class | module |
| --- | --- |
| `Algebras.Quotients` | `algebras` |
| `GradedModulesWithBasis.Quotients` | `graded_modules_with_basis` |
| `Semigroups.Quotients` | `semigroups` |
| `Sets.Quotients` | `sets_cat` |

## Realizations {#con-realizations}

| field | value |
| --- | --- |
| flavor | regressive covariant |
| implementation class | `realizations.RealizationsCategory` |
| implementation | [`src/sage/categories/realizations.py:49`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/realizations.py#L49) |
| interface declarations | `category.Category:Realizations` |
| specialized implementations | `coalgebras.Coalgebras:Realizations [nested category class]; hopf_algebras.HopfAlgebras:Realizations [nested category class]; magmas.Magmas:Realizations [nested category class]; magmas.Magmas:Unital.Realizations [nested category class]; sets_cat.Sets:Realizations [nested category class]` |

### Declared in (6)

| category | declaration | source |
| --- | --- | --- |
| [`Category`](categories.md#cat-category) | module-level binding | [`src/sage/categories/realizations.py:107`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/realizations.py#L107) |
| [`Coalgebras`](categories.md#cat-coalgebras) | nested category class | [`src/sage/categories/coalgebras.py:343`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L343) |
| [`HopfAlgebras`](categories.md#cat-hopfalgebras) | nested category class | [`src/sage/categories/hopf_algebras.py:187`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L187) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:1154`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L1154) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:720`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L720) |
| [`Sets`](categories.md#cat-sets) | nested category class | [`src/sage/categories/sets_cat.py:3157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L3157) |

### Classes the framework generates at 10.10 (5)

| class | module |
| --- | --- |
| `Coalgebras.Realizations` | `coalgebras` |
| `HopfAlgebras.Realizations` | `hopf_algebras` |
| `Magmas.Realizations` | `magmas` |
| `Magmas.Unital.Realizations` | `magmas` |
| `Sets.Realizations` | `sets_cat` |

## SignedTensorProducts {#con-signedtensorproducts}

| field | value |
| --- | --- |
| flavor | covariant |
| implementation class | `signed_tensor.SignedTensorProductsCategory` |
| implementation | [`src/sage/categories/signed_tensor.py:91`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/signed_tensor.py#L91) |
| other classes with the same functor tag | `signed_tensor.SignedTensorProductFunctor` |
| interface declarations | `graded_algebras.GradedAlgebras:SignedTensorProducts; graded_coalgebras.GradedCoalgebras:SignedTensorProducts` |
| specialized implementations | `graded_algebras.GradedAlgebras:SignedTensorProducts [nested category class]; graded_algebras_with_basis.GradedAlgebrasWithBasis:SignedTensorProducts [nested category class]; graded_coalgebras.GradedCoalgebras:SignedTensorProducts [nested category class]; graded_coalgebras_with_basis.GradedCoalgebrasWithBasis:SignedTensorProducts [nested category class]; signed_tensor.SignedTensorProductsCategory:SignedTensorProducts [category method]; super_algebras.SuperAlgebras:SignedTensorProducts [nested category class]; super_algebras_with_basis.SuperAlgebrasWithBasis:SignedTensorProducts [nested category class]; supercommutative_algebras.SupercommutativeAlgebras:SignedTensorProducts [nested category class]` |

### Declared in (10)

| category | declaration | source |
| --- | --- | --- |
| [`GradedAlgebras`](categories.md#cat-gradedalgebras) | nested category class | [`src/sage/categories/graded_algebras.py:71`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras.py#L71) |
| [`GradedAlgebras`](categories.md#cat-gradedalgebras) | subcategory interface method | [`src/sage/categories/graded_algebras.py:53`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras.py#L53) |
| [`GradedAlgebrasWithBasis`](categories.md#cat-gradedalgebraswithbasis) | nested category class | [`src/sage/categories/graded_algebras_with_basis.py:175`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras_with_basis.py#L175) |
| [`GradedCoalgebras`](categories.md#cat-gradedcoalgebras) | nested category class | [`src/sage/categories/graded_coalgebras.py:51`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_coalgebras.py#L51) |
| [`GradedCoalgebras`](categories.md#cat-gradedcoalgebras) | subcategory interface method | [`src/sage/categories/graded_coalgebras.py:33`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_coalgebras.py#L33) |
| [`GradedCoalgebrasWithBasis`](categories.md#cat-gradedcoalgebraswithbasis) | nested category class | [`src/sage/categories/graded_coalgebras_with_basis.py:33`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_coalgebras_with_basis.py#L33) |
| [`SignedTensorProductsCategory`](categories.md#cat-signedtensorproductscategory) | category method | [`src/sage/categories/signed_tensor.py:93`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/signed_tensor.py#L93) |
| [`SuperAlgebras`](categories.md#cat-superalgebras) | nested category class | [`src/sage/categories/super_algebras.py:135`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L135) |
| [`SuperAlgebrasWithBasis`](categories.md#cat-superalgebraswithbasis) | nested category class | [`src/sage/categories/super_algebras_with_basis.py:125`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras_with_basis.py#L125) |
| [`SupercommutativeAlgebras`](categories.md#cat-supercommutativealgebras) | nested category class | [`src/sage/categories/supercommutative_algebras.py:44`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercommutative_algebras.py#L44) |

### Classes the framework generates at 10.10 (7)

| class | module |
| --- | --- |
| `GradedAlgebras.SignedTensorProducts` | `graded_algebras` |
| `GradedAlgebrasWithBasis.SignedTensorProducts` | `graded_algebras_with_basis` |
| `GradedCoalgebras.SignedTensorProducts` | `graded_coalgebras` |
| `GradedCoalgebrasWithBasis.SignedTensorProducts` | `graded_coalgebras_with_basis` |
| `SuperAlgebras.SignedTensorProducts` | `super_algebras` |
| `SuperAlgebrasWithBasis.SignedTensorProducts` | `super_algebras_with_basis` |
| `SupercommutativeAlgebras.SignedTensorProducts` | `supercommutative_algebras` |

## Subobjects {#con-subobjects}

| field | value |
| --- | --- |
| flavor | regressive covariant |
| implementation class | `subobjects.SubobjectsCategory` |
| implementation | [`src/sage/categories/subobjects.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/subobjects.py#L21) |
| interface declarations | `sets_cat.Sets:Subobjects` |
| specialized implementations | `filtered_modules_with_basis.FilteredModulesWithBasis:Subobjects [nested category class]; finite_dimensional_lie_algebras_with_basis.FiniteDimensionalLieAlgebrasWithBasis:Subobjects [nested category class]; sets_cat.Sets:Subobjects [nested category class]` |

### Declared in (4)

| category | declaration | source |
| --- | --- | --- |
| [`FilteredModulesWithBasis`](categories.md#cat-filteredmoduleswithbasis) | nested category class | [`src/sage/categories/filtered_modules_with_basis.py:1076`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules_with_basis.py#L1076) |
| [`FiniteDimensionalLieAlgebrasWithBasis`](categories.md#cat-finitedimensionalliealgebraswithbasis) | nested category class | [`src/sage/categories/finite_dimensional_lie_algebras_with_basis.py:2609`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_lie_algebras_with_basis.py#L2609) |
| [`Sets`](categories.md#cat-sets) | nested category class | [`src/sage/categories/sets_cat.py:2125`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2125) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:517`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L517) |

### Classes the framework generates at 10.10 (3)

| class | module |
| --- | --- |
| `FilteredModulesWithBasis.Subobjects` | `filtered_modules_with_basis` |
| `FiniteDimensionalLieAlgebrasWithBasis.Subobjects` | `finite_dimensional_lie_algebras_with_basis` |
| `Sets.Subobjects` | `sets_cat` |

## Subquotients {#con-subquotients}

| field | value |
| --- | --- |
| flavor | regressive covariant |
| implementation class | `subquotients.SubquotientsCategory` |
| implementation | [`src/sage/categories/subquotients.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/subquotients.py#L20) |
| interface declarations | `sets_cat.Sets:Subquotients` |
| specialized implementations | `finite_sets.FiniteSets:Subquotients [nested category class]; magmas.Magmas:Subquotients [nested category class]; monoids.Monoids:Subquotients [nested category class]; semigroups.Semigroups:Subquotients [nested category class]; sets_cat.Sets:Subquotients [nested category class]` |

### Declared in (6)

| category | declaration | source |
| --- | --- | --- |
| [`FiniteSets`](categories.md#cat-finitesets) | nested category class | [`src/sage/categories/finite_sets.py:70`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L70) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:1103`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L1103) |
| [`Monoids`](categories.md#cat-monoids) | nested category class | [`src/sage/categories/monoids.py:468`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L468) |
| [`Semigroups`](categories.md#cat-semigroups) | nested category class | [`src/sage/categories/semigroups.py:786`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L786) |
| [`Sets`](categories.md#cat-sets) | nested category class | [`src/sage/categories/sets_cat.py:1952`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1952) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:325`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L325) |

### Classes the framework generates at 10.10 (5)

| class | module |
| --- | --- |
| `FiniteSets.Subquotients` | `finite_sets` |
| `Magmas.Subquotients` | `magmas` |
| `Monoids.Subquotients` | `monoids` |
| `Semigroups.Subquotients` | `semigroups` |
| `Sets.Subquotients` | `sets_cat` |

## Super {#con-super}

| field | value |
| --- | --- |
| flavor | covariant |
| implementation class | `super_modules.SuperModulesCategory` |
| implementation | [`src/sage/categories/super_modules.py:74`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_modules.py#L74) |
| interface declarations | `modules.Modules:Super` |
| specialized implementations | `algebras.Algebras:Super [lazy-import binding]; algebras_with_basis.AlgebrasWithBasis:Super [lazy-import binding]; bialgebras.Bialgebras:Super [nested category class]; coalgebras.Coalgebras:Super [nested category class]; coalgebras_with_basis.CoalgebrasWithBasis:Super [nested category class]; finitely_generated_lie_conformal_algebras.FinitelyGeneratedLieConformalAlgebras:Super [nested category class]; graded_lie_conformal_algebras.GradedLieConformalAlgebrasCategory:Super [category method]; hopf_algebras.HopfAlgebras:Super [nested category class]; hopf_algebras_with_basis.HopfAlgebrasWithBasis:Super [lazy-import binding]; lie_conformal_algebras.LieConformalAlgebras:Super [lazy-import binding]; lie_conformal_algebras_with_basis.LieConformalAlgebrasWithBasis:FinitelyGeneratedAsLambdaBracketAlgebra.Super [nested category class]; lie_conformal_algebras_with_basis.LieConformalAlgebrasWithBasis:Super [nested category class]; modules.Modules:Super [lazy-import binding]; modules_with_basis.ModulesWithBasis:Super [lazy-import binding]` |
| named result categories | `super_algebras.SuperAlgebras; super_algebras_with_basis.SuperAlgebrasWithBasis; super_hopf_algebras_with_basis.SuperHopfAlgebrasWithBasis; super_lie_conformal_algebras.SuperLieConformalAlgebras; super_modules.SuperModules; super_modules_with_basis.SuperModulesWithBasis` |

### Declared in (15)

| category | declaration | source |
| --- | --- | --- |
| [`Algebras`](categories.md#cat-algebras) | lazy-import binding | [`src/sage/categories/algebras.py:135`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L135) |
| [`AlgebrasWithBasis`](categories.md#cat-algebraswithbasis) | lazy-import binding | [`src/sage/categories/algebras_with_basis.py:127`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L127) |
| [`Bialgebras`](categories.md#cat-bialgebras) | nested category class | [`src/sage/categories/bialgebras.py:97`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/bialgebras.py#L97) |
| [`Coalgebras`](categories.md#cat-coalgebras) | nested category class | [`src/sage/categories/coalgebras.py:236`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L236) |
| [`CoalgebrasWithBasis`](categories.md#cat-coalgebraswithbasis) | nested category class | [`src/sage/categories/coalgebras_with_basis.py:220`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras_with_basis.py#L220) |
| [`FinitelyGeneratedLieConformalAlgebras`](categories.md#cat-finitelygeneratedlieconformalalgebras) | nested category class | [`src/sage/categories/finitely_generated_lie_conformal_algebras.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lie_conformal_algebras.py#L60) |
| [`GradedLieConformalAlgebrasCategory`](categories.md#cat-gradedlieconformalalgebrascategory) | category method | [`src/sage/categories/graded_lie_conformal_algebras.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_conformal_algebras.py#L25) |
| [`HopfAlgebras`](categories.md#cat-hopfalgebras) | nested category class | [`src/sage/categories/hopf_algebras.py:109`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L109) |
| [`HopfAlgebrasWithBasis`](categories.md#cat-hopfalgebraswithbasis) | lazy-import binding | [`src/sage/categories/hopf_algebras_with_basis.py:163`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L163) |
| [`LieConformalAlgebras`](categories.md#cat-lieconformalalgebras) | lazy-import binding | [`src/sage/categories/lie_conformal_algebras.py:341`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras.py#L341) |
| [`LieConformalAlgebrasWithBasis`](categories.md#cat-lieconformalalgebraswithbasis) | nested category class | [`src/sage/categories/lie_conformal_algebras_with_basis.py:99`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L99) |
| [`LieConformalAlgebrasWithBasis`](categories.md#cat-lieconformalalgebraswithbasis) | nested category class | [`src/sage/categories/lie_conformal_algebras_with_basis.py:34`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L34) |
| [`Modules`](categories.md#cat-modules) | lazy-import binding | [`src/sage/categories/modules.py:595`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L595) |
| [`Modules`](categories.md#cat-modules) | subcategory interface method | [`src/sage/categories/modules.py:456`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L456) |
| [`ModulesWithBasis`](categories.md#cat-moduleswithbasis) | lazy-import binding | [`src/sage/categories/modules_with_basis.py:198`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L198) |

### Classes the framework generates at 10.10 (7)

| class | module |
| --- | --- |
| `Bialgebras.Super` | `bialgebras` |
| `Coalgebras.Super` | `coalgebras` |
| `CoalgebrasWithBasis.Super` | `coalgebras_with_basis` |
| `FinitelyGeneratedLieConformalAlgebras.Super` | `finitely_generated_lie_conformal_algebras` |
| `HopfAlgebras.Super` | `hopf_algebras` |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Super` | `lie_conformal_algebras_with_basis` |
| `LieConformalAlgebrasWithBasis.Super` | `lie_conformal_algebras_with_basis` |

## TensorProducts {#con-tensorproducts}

| field | value |
| --- | --- |
| flavor | covariant |
| implementation class | `tensor.TensorProductsCategory` |
| implementation | [`src/sage/categories/tensor.py:84`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/tensor.py#L84) |
| other classes with the same functor tag | `tensor.TensorProductFunctor` |
| interface declarations | `crystals.Crystals:TensorProducts; modules.Modules:TensorProducts` |
| specialized implementations | `algebras.Algebras:TensorProducts [nested category class]; algebras_with_basis.AlgebrasWithBasis:TensorProducts [nested category class]; classical_crystals.ClassicalCrystals:TensorProducts [nested category class]; coalgebras.Coalgebras:TensorProducts [nested category class]; commutative_algebras.CommutativeAlgebras:TensorProducts [nested category class]; crystals.Crystals:TensorProducts [nested category class]; finite_crystals.FiniteCrystals:TensorProducts [nested category class]; finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis:Cellular.TensorProducts [nested category class]; finite_dimensional_modules_with_basis.FiniteDimensionalModulesWithBasis:TensorProducts [nested category class]; highest_weight_crystals.HighestWeightCrystals:TensorProducts [nested category class]; hopf_algebras.HopfAlgebras:TensorProducts [nested category class]; hopf_algebras_with_basis.HopfAlgebrasWithBasis:TensorProducts [nested category class]; loop_crystals.KirillovReshetikhinCrystals:TensorProducts [nested category class]; modules.Modules:FiniteDimensional.TensorProducts [nested category class]; modules.Modules:TensorProducts [nested category class]; modules_with_basis.ModulesWithBasis:TensorProducts [nested category class]; quantum_group_representations.QuantumGroupRepresentations:TensorProducts [nested category class]; quantum_group_representations.QuantumGroupRepresentations:WithBasis.TensorProducts [nested category class]; regular_crystals.RegularCrystals:TensorProducts [nested category class]; regular_supercrystals.RegularSuperCrystals:TensorProducts [nested category class]; supercrystals.SuperCrystals:TensorProducts [nested category class]; tensor.TensorProductsCategory:TensorProducts [category method]; vector_spaces.VectorSpaces:FiniteDimensional.TensorProducts [nested category class]; vector_spaces.VectorSpaces:TensorProducts [nested category class]; vector_spaces.VectorSpaces:WithBasis.FiniteDimensional.TensorProducts [nested category class]; vector_spaces.VectorSpaces:WithBasis.TensorProducts [nested category class]` |

### Declared in (28)

| category | declaration | source |
| --- | --- | --- |
| [`Algebras`](categories.md#cat-algebras) | nested category class | [`src/sage/categories/algebras.py:300`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L300) |
| [`AlgebrasWithBasis`](categories.md#cat-algebraswithbasis) | nested category class | [`src/sage/categories/algebras_with_basis.py:283`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L283) |
| [`ClassicalCrystals`](categories.md#cat-classicalcrystals) | nested category class | [`src/sage/categories/classical_crystals.py:473`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/classical_crystals.py#L473) |
| [`Coalgebras`](categories.md#cat-coalgebras) | nested category class | [`src/sage/categories/coalgebras.py:185`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L185) |
| [`CommutativeAlgebras`](categories.md#cat-commutativealgebras) | nested category class | [`src/sage/categories/commutative_algebras.py:66`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_algebras.py#L66) |
| [`Crystals`](categories.md#cat-crystals) | nested category class | [`src/sage/categories/crystals.py:1808`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L1808) |
| [`Crystals`](categories.md#cat-crystals) | subcategory interface method | [`src/sage/categories/crystals.py:1791`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L1791) |
| [`FiniteCrystals`](categories.md#cat-finitecrystals) | nested category class | [`src/sage/categories/finite_crystals.py:91`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_crystals.py#L91) |
| [`FiniteDimensionalAlgebrasWithBasis`](categories.md#cat-finitedimensionalalgebraswithbasis) | nested category class | [`src/sage/categories/finite_dimensional_algebras_with_basis.py:1846`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L1846) |
| [`FiniteDimensionalModulesWithBasis`](categories.md#cat-finitedimensionalmoduleswithbasis) | nested category class | [`src/sage/categories/finite_dimensional_modules_with_basis.py:1050`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L1050) |
| [`HighestWeightCrystals`](categories.md#cat-highestweightcrystals) | nested category class | [`src/sage/categories/highest_weight_crystals.py:655`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/highest_weight_crystals.py#L655) |
| [`HopfAlgebras`](categories.md#cat-hopfalgebras) | nested category class | [`src/sage/categories/hopf_algebras.py:147`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L147) |
| [`HopfAlgebrasWithBasis`](categories.md#cat-hopfalgebraswithbasis) | nested category class | [`src/sage/categories/hopf_algebras_with_basis.py:284`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L284) |
| [`KirillovReshetikhinCrystals`](categories.md#cat-kirillovreshetikhincrystals) | nested category class | [`src/sage/categories/loop_crystals.py:715`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/loop_crystals.py#L715) |
| [`Modules`](categories.md#cat-modules) | nested category class | [`src/sage/categories/modules.py:545`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L545) |
| [`Modules`](categories.md#cat-modules) | nested category class | [`src/sage/categories/modules.py:932`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L932) |
| [`Modules`](categories.md#cat-modules) | subcategory interface method | [`src/sage/categories/modules.py:245`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L245) |
| [`ModulesWithBasis`](categories.md#cat-moduleswithbasis) | nested category class | [`src/sage/categories/modules_with_basis.py:2621`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L2621) |
| [`QuantumGroupRepresentations`](categories.md#cat-quantumgrouprepresentations) | nested category class | [`src/sage/categories/quantum_group_representations.py:369`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quantum_group_representations.py#L369) |
| [`QuantumGroupRepresentations`](categories.md#cat-quantumgrouprepresentations) | nested category class | [`src/sage/categories/quantum_group_representations.py:68`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quantum_group_representations.py#L68) |
| [`RegularCrystals`](categories.md#cat-regularcrystals) | nested category class | [`src/sage/categories/regular_crystals.py:880`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/regular_crystals.py#L880) |
| [`RegularSuperCrystals`](categories.md#cat-regularsupercrystals) | nested category class | [`src/sage/categories/regular_supercrystals.py:155`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/regular_supercrystals.py#L155) |
| [`SuperCrystals`](categories.md#cat-supercrystals) | nested category class | [`src/sage/categories/supercrystals.py:388`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercrystals.py#L388) |
| [`TensorProductsCategory`](categories.md#cat-tensorproductscategory) | category method | [`src/sage/categories/tensor.py:86`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/tensor.py#L86) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:287`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L287) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:335`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L335) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:227`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L227) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:212`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L212) |

### Classes the framework generates at 10.10 (25)

| class | module |
| --- | --- |
| `Algebras.TensorProducts` | `algebras` |
| `AlgebrasWithBasis.TensorProducts` | `algebras_with_basis` |
| `ClassicalCrystals.TensorProducts` | `classical_crystals` |
| `Coalgebras.TensorProducts` | `coalgebras` |
| `CommutativeAlgebras.TensorProducts` | `commutative_algebras` |
| `Crystals.TensorProducts` | `crystals` |
| `FiniteCrystals.TensorProducts` | `finite_crystals` |
| `FiniteDimensionalAlgebrasWithBasis.Cellular.TensorProducts` | `finite_dimensional_algebras_with_basis` |
| `FiniteDimensionalModulesWithBasis.TensorProducts` | `finite_dimensional_modules_with_basis` |
| `HighestWeightCrystals.TensorProducts` | `highest_weight_crystals` |
| `HopfAlgebras.TensorProducts` | `hopf_algebras` |
| `HopfAlgebrasWithBasis.TensorProducts` | `hopf_algebras_with_basis` |
| `KirillovReshetikhinCrystals.TensorProducts` | `loop_crystals` |
| `Modules.FiniteDimensional.TensorProducts` | `modules` |
| `Modules.TensorProducts` | `modules` |
| `ModulesWithBasis.TensorProducts` | `modules_with_basis` |
| `QuantumGroupRepresentations.TensorProducts` | `quantum_group_representations` |
| `QuantumGroupRepresentations.WithBasis.TensorProducts` | `quantum_group_representations` |
| `RegularCrystals.TensorProducts` | `regular_crystals` |
| `RegularSuperCrystals.TensorProducts` | `regular_supercrystals` |
| `SuperCrystals.TensorProducts` | `supercrystals` |
| `VectorSpaces.FiniteDimensional.TensorProducts` | `vector_spaces` |
| `VectorSpaces.TensorProducts` | `vector_spaces` |
| `VectorSpaces.WithBasis.FiniteDimensional.TensorProducts` | `vector_spaces` |
| `VectorSpaces.WithBasis.TensorProducts` | `vector_spaces` |

## Topological {#con-topological}

| field | value |
| --- | --- |
| flavor | regressive covariant |
| implementation class | `topological_spaces.TopologicalSpacesCategory` |
| implementation | [`src/sage/categories/topological_spaces.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L20) |
| interface declarations | `sets_cat.Sets:Topological` |
| specialized implementations | `groups.Groups:Topological [nested category class]; sets_cat.Sets:Topological [lazy-import binding]` |
| named result categories | `topological_spaces.TopologicalSpaces` |

### Declared in (3)

| category | declaration | source |
| --- | --- | --- |
| [`Groups`](categories.md#cat-groups) | nested category class | [`src/sage/categories/groups.py:654`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L654) |
| [`Sets`](categories.md#cat-sets) | lazy-import binding | [`src/sage/categories/sets_cat.py:1881`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1881) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:671`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L671) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Groups.Topological` | `groups` |

## WithRealizations {#con-withrealizations}

| field | value |
| --- | --- |
| flavor | regressive covariant |
| implementation class | `with_realizations.WithRealizationsCategory` |
| implementation | [`src/sage/categories/with_realizations.py:298`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/with_realizations.py#L298) |
| interface declarations | `category.Category:WithRealizations` |
| specialized implementations | `additive_magmas.AdditiveMagmas:AdditiveUnital.WithRealizations [nested category class]; coalgebras.Coalgebras:WithRealizations [nested category class]; filtered_hopf_algebras_with_basis.FilteredHopfAlgebrasWithBasis:WithRealizations [nested category class]; graded_hopf_algebras_with_basis.GradedHopfAlgebrasWithBasis:WithRealizations [nested category class]; metric_spaces.MetricSpaces:WithRealizations [nested category class]; monoids.Monoids:WithRealizations [nested category class]; sets_cat.Sets:WithRealizations [nested category class]` |

### Declared in (8)

| category | declaration | source |
| --- | --- | --- |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:1008`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L1008) |
| [`Category`](categories.md#cat-category) | module-level binding | [`src/sage/categories/with_realizations.py:284`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/with_realizations.py#L284) |
| [`Coalgebras`](categories.md#cat-coalgebras) | nested category class | [`src/sage/categories/coalgebras.py:293`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L293) |
| [`FilteredHopfAlgebrasWithBasis`](categories.md#cat-filteredhopfalgebraswithbasis) | nested category class | [`src/sage/categories/filtered_hopf_algebras_with_basis.py:49`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_hopf_algebras_with_basis.py#L49) |
| [`GradedHopfAlgebrasWithBasis`](categories.md#cat-gradedhopfalgebraswithbasis) | nested category class | [`src/sage/categories/graded_hopf_algebras_with_basis.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_hopf_algebras_with_basis.py#L60) |
| [`MetricSpaces`](categories.md#cat-metricspaces) | nested category class | [`src/sage/categories/metric_spaces.py:263`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L263) |
| [`Monoids`](categories.md#cat-monoids) | nested category class | [`src/sage/categories/monoids.py:439`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L439) |
| [`Sets`](categories.md#cat-sets) | nested category class | [`src/sage/categories/sets_cat.py:2797`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2797) |

### Classes the framework generates at 10.10 (7)

| class | module |
| --- | --- |
| `AdditiveMagmas.AdditiveUnital.WithRealizations` | `additive_magmas` |
| `Coalgebras.WithRealizations` | `coalgebras` |
| `FilteredHopfAlgebrasWithBasis.WithRealizations` | `filtered_hopf_algebras_with_basis` |
| `GradedHopfAlgebrasWithBasis.WithRealizations` | `graded_hopf_algebras_with_basis` |
| `MetricSpaces.WithRealizations` | `metric_spaces` |
| `Monoids.WithRealizations` | `monoids` |
| `Sets.WithRealizations` | `sets_cat` |
