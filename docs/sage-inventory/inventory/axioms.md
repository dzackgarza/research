# Sage axioms

## AdditiveAssociative {#ax-additiveassociative}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `additive_semigroups.AdditiveSemigroups` |
| interface declarations | `additive_magmas.AdditiveMagmas:AdditiveAssociative` |
| implementation or binding | `additive_magmas.AdditiveMagmas:AdditiveAssociative [lazy-import binding]; distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas:AdditiveAssociative [nested category class]` |
| method expansions | `additive_magmas.AdditiveMagmas:AdditiveAssociative -> _with_axiom(AdditiveAssociative)` |

### Declared in (3)

| category | declaration | source |
| --- | --- | --- |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | lazy-import binding | [`src/sage/categories/additive_magmas.py:167`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L167) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | subcategory interface method | [`src/sage/categories/additive_magmas.py:78`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L78) |
| [`DistributiveMagmasAndAdditiveMagmas`](categories.md#cat-distributivemagmasandadditivemagmas) | nested category class | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:41`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L41) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative` | `distributive_magmas_and_additive_magmas` |

## AdditiveCommutative {#ax-additivecommutative}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `commutative_additive_groups.CommutativeAdditiveGroups`, `commutative_additive_monoids.CommutativeAdditiveMonoids`, `commutative_additive_semigroups.CommutativeAdditiveSemigroups` |
| interface declarations | `additive_magmas.AdditiveMagmas:AdditiveCommutative` |
| implementation or binding | `additive_groups.AdditiveGroups:AdditiveCommutative [lazy-import binding]; additive_magmas.AdditiveMagmas:AdditiveCommutative [nested category class]; additive_monoids.AdditiveMonoids:AdditiveCommutative [lazy-import binding]; additive_semigroups.AdditiveSemigroups:AdditiveCommutative [lazy-import binding]; distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas:AdditiveAssociative.AdditiveCommutative [nested category class]` |
| method expansions | `additive_magmas.AdditiveMagmas:AdditiveCommutative -> _with_axiom(AdditiveCommutative)` |

### Declared in (6)

| category | declaration | source |
| --- | --- | --- |
| [`AdditiveGroups`](categories.md#cat-additivegroups) | lazy-import binding | [`src/sage/categories/additive_groups.py:69`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L69) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:563`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L563) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | subcategory interface method | [`src/sage/categories/additive_magmas.py:104`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L104) |
| [`AdditiveMonoids`](categories.md#cat-additivemonoids) | lazy-import binding | [`src/sage/categories/additive_monoids.py:47`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L47) |
| [`AdditiveSemigroups`](categories.md#cat-additivesemigroups) | lazy-import binding | [`src/sage/categories/additive_semigroups.py:53`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L53) |
| [`DistributiveMagmasAndAdditiveMagmas`](categories.md#cat-distributivemagmasandadditivemagmas) | nested category class | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:42`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L42) |

### Classes the framework generates at 10.10 (2)

| class | module |
| --- | --- |
| `AdditiveMagmas.AdditiveCommutative` | `additive_magmas` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative` | `distributive_magmas_and_additive_magmas` |

## AdditiveInverse {#ax-additiveinverse}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `additive_groups.AdditiveGroups`, `rngs.Rngs` |
| interface declarations | `additive_magmas.AdditiveMagmas:AdditiveUnital.AdditiveInverse` |
| implementation or binding | `additive_magmas.AdditiveMagmas:AdditiveUnital.AdditiveInverse [nested category class]; additive_monoids.AdditiveMonoids:AdditiveInverse [lazy-import binding]; distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas:AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative.AdditiveInverse [lazy-import binding]` |
| method expansions | `additive_magmas.AdditiveMagmas:AdditiveUnital.AdditiveInverse -> _with_axiom(AdditiveInverse)` |

### Declared in (4)

| category | declaration | source |
| --- | --- | --- |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:898`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L898) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | subcategory interface method | [`src/sage/categories/additive_magmas.py:621`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L621) |
| [`AdditiveMonoids`](categories.md#cat-additivemonoids) | lazy-import binding | [`src/sage/categories/additive_monoids.py:48`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L48) |
| [`DistributiveMagmasAndAdditiveMagmas`](categories.md#cat-distributivemagmasandadditivemagmas) | lazy-import binding | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:45`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L45) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `AdditiveMagmas.AdditiveUnital.AdditiveInverse` | `additive_magmas` |

## AdditiveUnital {#ax-additiveunital}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `additive_monoids.AdditiveMonoids` |
| interface declarations | `additive_magmas.AdditiveMagmas:AdditiveUnital` |
| implementation or binding | `additive_magmas.AdditiveMagmas:AdditiveUnital [nested category class]; additive_semigroups.AdditiveSemigroups:AdditiveUnital [lazy-import binding]; distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas:AdditiveAssociative.AdditiveCommutative.AdditiveUnital [nested category class]` |
| method expansions | `additive_magmas.AdditiveMagmas:AdditiveUnital -> _with_axiom(AdditiveUnital)` |

### Declared in (4)

| category | declaration | source |
| --- | --- | --- |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | nested category class | [`src/sage/categories/additive_magmas.py:599`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L599) |
| [`AdditiveMagmas`](categories.md#cat-additivemagmas) | subcategory interface method | [`src/sage/categories/additive_magmas.py:134`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L134) |
| [`AdditiveSemigroups`](categories.md#cat-additivesemigroups) | lazy-import binding | [`src/sage/categories/additive_semigroups.py:54`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L54) |
| [`DistributiveMagmasAndAdditiveMagmas`](categories.md#cat-distributivemagmasandadditivemagmas) | nested category class | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:43`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L43) |

### Classes the framework generates at 10.10 (2)

| class | module |
| --- | --- |
| `AdditiveMagmas.AdditiveUnital` | `additive_magmas` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital` | `distributive_magmas_and_additive_magmas` |

## AlmostComplex {#ax-almostcomplex}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `manifolds.Manifolds:AlmostComplex` |
| implementation or binding | `manifolds.Manifolds:AlmostComplex [nested category class]` |
| method expansions | `manifolds.Manifolds:AlmostComplex -> _with_axiom(AlmostComplex)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Manifolds`](categories.md#cat-manifolds) | nested category class | [`src/sage/categories/manifolds.py:288`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L288) |
| [`Manifolds`](categories.md#cat-manifolds) | subcategory interface method | [`src/sage/categories/manifolds.py:199`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L199) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Manifolds.AlmostComplex` | `manifolds` |

## Analytic {#ax-analytic}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `manifolds.Manifolds:Analytic` |
| implementation or binding | `manifolds.Manifolds:Analytic [nested category class]` |
| method expansions | `manifolds.Manifolds:Analytic -> _with_axiom(Analytic)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Manifolds`](categories.md#cat-manifolds) | nested category class | [`src/sage/categories/manifolds.py:267`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L267) |
| [`Manifolds`](categories.md#cat-manifolds) | subcategory interface method | [`src/sage/categories/manifolds.py:179`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L179) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Manifolds.Analytic` | `manifolds` |

## Aperiodic {#ax-aperiodic}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/semigroups.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L27) |
| defining categories | `aperiodic_semigroups.AperiodicSemigroups` |
| interface declarations | `semigroups.Semigroups:Aperiodic` |
| implementation or binding | `semigroups.Semigroups:Aperiodic [lazy-import binding]` |
| method expansions | `semigroups.Semigroups:Aperiodic -> _with_axiom(Aperiodic)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Semigroups`](categories.md#cat-semigroups) | lazy-import binding | [`src/sage/categories/semigroups.py:783`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L783) |
| [`Semigroups`](categories.md#cat-semigroups) | subcategory interface method | [`src/sage/categories/semigroups.py:729`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L729) |

## Associative {#ax-associative}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `associative_algebras.AssociativeAlgebras`, `semigroups.Semigroups` |
| interface declarations | `magmas.Magmas:Associative` |
| implementation or binding | `distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas:AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative [nested category class]; magmas.Magmas:Associative [lazy-import binding]; magmatic_algebras.MagmaticAlgebras:Associative [lazy-import binding]` |
| method expansions | `magmas.Magmas:Associative -> _with_axiom(Associative)` |

### Declared in (4)

| category | declaration | source |
| --- | --- | --- |
| [`DistributiveMagmasAndAdditiveMagmas`](categories.md#cat-distributivemagmasandadditivemagmas) | nested category class | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:44`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L44) |
| [`Magmas`](categories.md#cat-magmas) | lazy-import binding | [`src/sage/categories/magmas.py:342`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L342) |
| [`Magmas`](categories.md#cat-magmas) | subcategory interface method | [`src/sage/categories/magmas.py:75`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L75) |
| [`MagmaticAlgebras`](categories.md#cat-magmaticalgebras) | lazy-import binding | [`src/sage/categories/magmatic_algebras.py:100`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L100) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative` | `distributive_magmas_and_additive_magmas` |

## Blue {#ax-blue}

| field | value |
| --- | --- |
| status | test-only placeholder |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `category_with_axiom.Blahs:Blue` |
| implementation or binding | `category_with_axiom.Blahs:Unital.Blue [nested category class]` |
| method expansions | `category_with_axiom.Blahs:Blue -> _with_axiom(Blue)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Blahs`](categories.md#cat-blahs) | subcategory interface method | [`src/sage/categories/category_with_axiom.py:2630`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2630) |
| [`Blahs`](categories.md#cat-blahs) | nested category class | [`src/sage/categories/category_with_axiom.py:2642`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2642) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Blahs.Unital.Blue` | `category_with_axiom` |

## Bounded {#ax-bounded}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `posets.Posets:Bounded` |
| implementation or binding | `posets.Posets:Bounded [nested category class]` |
| method expansions | `posets.Posets:Bounded -> _with_axiom(Bounded)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Posets`](categories.md#cat-posets) | nested category class | [`src/sage/categories/posets.py:736`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L736) |
| [`Posets`](categories.md#cat-posets) | subcategory interface method | [`src/sage/categories/posets.py:723`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L723) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Posets.Bounded` | `posets` |

## Cellular {#ax-cellular}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis:Cellular` |
| implementation or binding | `finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis:Cellular [nested category class]` |
| method expansions | `finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis:Cellular -> _with_axiom(Cellular)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`FiniteDimensionalAlgebrasWithBasis`](categories.md#cat-finitedimensionalalgebraswithbasis) | nested category class | [`src/sage/categories/finite_dimensional_algebras_with_basis.py:1571`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L1571) |
| [`FiniteDimensionalAlgebrasWithBasis`](categories.md#cat-finitedimensionalalgebraswithbasis) | subcategory interface method | [`src/sage/categories/finite_dimensional_algebras_with_basis.py:2020`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L2020) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `FiniteDimensionalAlgebrasWithBasis.Cellular` | `finite_dimensional_algebras_with_basis` |

## ChainGraded {#ax-chaingraded}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `lattice_posets.DistributiveLattices` |
| interface declarations | `lattice_posets.LatticePosets:ChainGraded` |
| implementation or binding | `lattice_posets.LatticePosets:ChainGraded [nested category class]; lattice_posets.LatticePosets:Trim.ChainGraded [module-level binding]` |
| method expansions | `lattice_posets.LatticePosets:ChainGraded -> _with_axiom(ChainGraded)` |

### Declared in (3)

| category | declaration | source |
| --- | --- | --- |
| [`LatticePosets`](categories.md#cat-latticeposets) | nested category class | [`src/sage/categories/lattice_posets.py:536`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L536) |
| [`LatticePosets`](categories.md#cat-latticeposets) | subcategory interface method | [`src/sage/categories/lattice_posets.py:93`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L93) |
| [`LatticePosets`](categories.md#cat-latticeposets) | module-level binding | [`src/sage/categories/lattice_posets.py:619`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L619) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `LatticePosets.ChainGraded` | `lattice_posets` |

## Cocommutative {#ax-cocommutative}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `coalgebras.Coalgebras:Cocommutative` |
| implementation or binding | `coalgebras.Coalgebras:Cocommutative [nested category class]` |
| method expansions | `coalgebras.Coalgebras:Cocommutative -> _with_axiom(Cocommutative)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Coalgebras`](categories.md#cat-coalgebras) | nested category class | [`src/sage/categories/coalgebras.py:180`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L180) |
| [`Coalgebras`](categories.md#cat-coalgebras) | subcategory interface method | [`src/sage/categories/coalgebras.py:150`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L150) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Coalgebras.Cocommutative` | `coalgebras` |

## Commutative {#ax-commutative}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `commutative_algebras.CommutativeAlgebras`, `commutative_rings.CommutativeRings`, `fields.Fields`, `integral_domains.IntegralDomains` |
| interface declarations | `category_with_axiom.Blahs:Commutative; magmas.Magmas:Commutative` |
| implementation or binding | `algebras.Algebras:Commutative [lazy-import binding]; category_with_axiom.Blahs:Commutative [nested category class]; category_with_axiom.DummyObjectsOverBaseRing:Commutative [nested category class]; category_with_axiom.DummyObjectsOverBaseRing:FiniteDimensional.Unital.Commutative [nested category class]; category_with_axiom.TestObjects:Commutative [nested category class]; category_with_axiom.TestObjects:FiniteDimensional.Unital.Commutative [nested category class]; division_rings.DivisionRings:Commutative [lazy-import binding]; domains.Domains:Commutative [lazy-import binding]; finite_dimensional_semisimple_algebras_with_basis.FiniteDimensionalSemisimpleAlgebrasWithBasis:Commutative [nested category class]; groups.Groups:Commutative [nested category class]; magmas.Magmas:Commutative [nested category class]; monoids.Monoids:Commutative [nested category class]; rings.Rings:Commutative [lazy-import binding]` |
| method expansions | `category_with_axiom.Blahs:Commutative -> _with_axiom(Commutative); magmas.Magmas:Commutative -> _with_axiom(Commutative)` |

### Declared in (15)

| category | declaration | source |
| --- | --- | --- |
| [`Algebras`](categories.md#cat-algebras) | lazy-import binding | [`src/sage/categories/algebras.py:129`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L129) |
| [`Blahs`](categories.md#cat-blahs) | nested category class | [`src/sage/categories/category_with_axiom.py:2635`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2635) |
| [`Blahs`](categories.md#cat-blahs) | subcategory interface method | [`src/sage/categories/category_with_axiom.py:2626`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2626) |
| [`DummyObjectsOverBaseRing`](categories.md#cat-dummyobjectsoverbasering) | nested category class | [`src/sage/categories/category_with_axiom.py:2824`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2824) |
| [`DummyObjectsOverBaseRing`](categories.md#cat-dummyobjectsoverbasering) | nested category class | [`src/sage/categories/category_with_axiom.py:2821`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2821) |
| [`TestObjects`](categories.md#cat-testobjects) | nested category class | [`src/sage/categories/category_with_axiom.py:2779`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2779) |
| [`TestObjects`](categories.md#cat-testobjects) | nested category class | [`src/sage/categories/category_with_axiom.py:2776`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2776) |
| [`DivisionRings`](categories.md#cat-divisionrings) | lazy-import binding | [`src/sage/categories/division_rings.py:63`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/division_rings.py#L63) |
| [`Domains`](categories.md#cat-domains) | lazy-import binding | [`src/sage/categories/domains.py:49`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/domains.py#L49) |
| [`FiniteDimensionalSemisimpleAlgebrasWithBasis`](categories.md#cat-finitedimensionalsemisimplealgebraswithbasis) | nested category class | [`src/sage/categories/finite_dimensional_semisimple_algebras_with_basis.py:116`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_semisimple_algebras_with_basis.py#L116) |
| [`Groups`](categories.md#cat-groups) | nested category class | [`src/sage/categories/groups.py:495`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L495) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:401`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L401) |
| [`Magmas`](categories.md#cat-magmas) | subcategory interface method | [`src/sage/categories/magmas.py:101`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L101) |
| [`Monoids`](categories.md#cat-monoids) | nested category class | [`src/sage/categories/monoids.py:391`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L391) |
| [`Rings`](categories.md#cat-rings) | lazy-import binding | [`src/sage/categories/rings.py:311`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L311) |

### Classes the framework generates at 10.10 (9)

| class | module |
| --- | --- |
| `Blahs.Commutative` | `category_with_axiom` |
| `DummyObjectsOverBaseRing.Commutative` | `category_with_axiom` |
| `DummyObjectsOverBaseRing.FiniteDimensional.Unital.Commutative` | `category_with_axiom` |
| `TestObjects.Commutative` | `category_with_axiom` |
| `TestObjects.FiniteDimensional.Unital.Commutative` | `category_with_axiom` |
| `FiniteDimensionalSemisimpleAlgebrasWithBasis.Commutative` | `finite_dimensional_semisimple_algebras_with_basis` |
| `Groups.Commutative` | `groups` |
| `Magmas.Commutative` | `magmas` |
| `Monoids.Commutative` | `monoids` |

## Compact {#ax-compact}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `topological_spaces.TopologicalSpaces:Compact` |
| implementation or binding | `topological_spaces.TopologicalSpaces:Compact [nested category class]` |
| method expansions | `topological_spaces.TopologicalSpaces:Compact -> _with_axiom(Compact)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`TopologicalSpaces`](categories.md#cat-topologicalspaces) | nested category class | [`src/sage/categories/topological_spaces.py:146`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L146) |
| [`TopologicalSpaces`](categories.md#cat-topologicalspaces) | subcategory interface method | [`src/sage/categories/topological_spaces.py:104`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L104) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `TopologicalSpaces.Compact` | `topological_spaces` |

## Complete {#ax-complete}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `metric_spaces.MetricSpaces:Complete` |
| implementation or binding | `metric_spaces.MetricSpaces:Complete [nested category class]` |
| method expansions | `metric_spaces.MetricSpaces:Complete -> _with_axiom(Complete)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`MetricSpaces`](categories.md#cat-metricspaces) | nested category class | [`src/sage/categories/metric_spaces.py:347`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L347) |
| [`MetricSpaces`](categories.md#cat-metricspaces) | subcategory interface method | [`src/sage/categories/metric_spaces.py:330`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L330) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `MetricSpaces.Complete` | `metric_spaces` |

## CongruenceUniform {#ax-congruenceuniform}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `lattice_posets.LatticePosets:CongruenceUniform` |
| implementation or binding | `lattice_posets.LatticePosets:CongruenceUniform [nested category class]` |
| method expansions | `lattice_posets.LatticePosets:CongruenceUniform -> _with_axiom(CongruenceUniform)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`LatticePosets`](categories.md#cat-latticeposets) | nested category class | [`src/sage/categories/lattice_posets.py:457`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L457) |
| [`LatticePosets`](categories.md#cat-latticeposets) | subcategory interface method | [`src/sage/categories/lattice_posets.py:144`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L144) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `LatticePosets.CongruenceUniform` | `lattice_posets` |

## Connected {#ax-connected}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `category_with_axiom.Blahs:Connected; cw_complexes.CWComplexes:Connected; filtered_modules.FilteredModules:Connected; manifolds.Manifolds:Connected; simplicial_complexes.SimplicialComplexes:Connected; topological_spaces.TopologicalSpaces:Connected` |
| implementation or binding | `category_with_axiom.Blahs:Connected [nested category class]; cw_complexes.CWComplexes:Connected [nested category class]; filtered_hopf_algebras_with_basis.FilteredHopfAlgebrasWithBasis:Connected [nested category class]; filtered_modules.FilteredModules:Connected [nested category class]; graded_hopf_algebras_with_basis.GradedHopfAlgebrasWithBasis:Connected [nested category class]; graphs.Graphs:Connected [nested category class]; manifolds.Manifolds:Connected [nested category class]; simplicial_complexes.SimplicialComplexes:Connected [nested category class]; topological_spaces.TopologicalSpaces:Connected [nested category class]` |
| method expansions | `category_with_axiom.Blahs:Connected -> _with_axiom(Connected); cw_complexes.CWComplexes:Connected -> _with_axiom(Connected); filtered_modules.FilteredModules:Connected -> _with_axiom(Connected); manifolds.Manifolds:Connected -> _with_axiom(Connected); simplicial_complexes.SimplicialComplexes:Connected -> _with_axiom(Connected); topological_spaces.TopologicalSpaces:Connected -> _with_axiom(Connected)` |

### Declared in (15)

| category | declaration | source |
| --- | --- | --- |
| [`Blahs`](categories.md#cat-blahs) | nested category class | [`src/sage/categories/category_with_axiom.py:2638`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2638) |
| [`Blahs`](categories.md#cat-blahs) | subcategory interface method | [`src/sage/categories/category_with_axiom.py:2628`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2628) |
| [`CWComplexes`](categories.md#cat-cwcomplexes) | nested category class | [`src/sage/categories/cw_complexes.py:105`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L105) |
| [`CWComplexes`](categories.md#cat-cwcomplexes) | subcategory interface method | [`src/sage/categories/cw_complexes.py:65`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L65) |
| [`FilteredHopfAlgebrasWithBasis`](categories.md#cat-filteredhopfalgebraswithbasis) | nested category class | [`src/sage/categories/filtered_hopf_algebras_with_basis.py:68`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_hopf_algebras_with_basis.py#L68) |
| [`FilteredModules`](categories.md#cat-filteredmodules) | nested category class | [`src/sage/categories/filtered_modules.py:207`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules.py#L207) |
| [`FilteredModules`](categories.md#cat-filteredmodules) | subcategory interface method | [`src/sage/categories/filtered_modules.py:181`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules.py#L181) |
| [`GradedHopfAlgebrasWithBasis`](categories.md#cat-gradedhopfalgebraswithbasis) | nested category class | [`src/sage/categories/graded_hopf_algebras_with_basis.py:79`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_hopf_algebras_with_basis.py#L79) |
| [`Graphs`](categories.md#cat-graphs) | nested category class | [`src/sage/categories/graphs.py:112`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graphs.py#L112) |
| [`Manifolds`](categories.md#cat-manifolds) | nested category class | [`src/sage/categories/manifolds.py:323`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L323) |
| [`Manifolds`](categories.md#cat-manifolds) | subcategory interface method | [`src/sage/categories/manifolds.py:98`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L98) |
| [`SimplicialComplexes`](categories.md#cat-simplicialcomplexes) | nested category class | [`src/sage/categories/simplicial_complexes.py:124`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_complexes.py#L124) |
| [`SimplicialComplexes`](categories.md#cat-simplicialcomplexes) | subcategory interface method | [`src/sage/categories/simplicial_complexes.py:107`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_complexes.py#L107) |
| [`TopologicalSpaces`](categories.md#cat-topologicalspaces) | nested category class | [`src/sage/categories/topological_spaces.py:121`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L121) |
| [`TopologicalSpaces`](categories.md#cat-topologicalspaces) | subcategory interface method | [`src/sage/categories/topological_spaces.py:86`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L86) |

### Classes the framework generates at 10.10 (9)

| class | module |
| --- | --- |
| `Blahs.Connected` | `category_with_axiom` |
| `CWComplexes.Connected` | `cw_complexes` |
| `FilteredHopfAlgebrasWithBasis.Connected` | `filtered_hopf_algebras_with_basis` |
| `FilteredModules.Connected` | `filtered_modules` |
| `GradedHopfAlgebrasWithBasis.Connected` | `graded_hopf_algebras_with_basis` |
| `Graphs.Connected` | `graphs` |
| `Manifolds.Connected` | `manifolds` |
| `SimplicialComplexes.Connected` | `simplicial_complexes` |
| `TopologicalSpaces.Connected` | `topological_spaces` |

## Differentiable {#ax-differentiable}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `manifolds.Manifolds:Differentiable; vector_bundles.VectorBundles:Differentiable` |
| implementation or binding | `manifolds.Manifolds:Differentiable [nested category class]; vector_bundles.VectorBundles:Differentiable [nested category class]` |
| method expansions | `manifolds.Manifolds:Differentiable -> _with_axiom(Differentiable); vector_bundles.VectorBundles:Differentiable -> _with_axiom(Differentiable)` |

### Declared in (4)

| category | declaration | source |
| --- | --- | --- |
| [`Manifolds`](categories.md#cat-manifolds) | nested category class | [`src/sage/categories/manifolds.py:239`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L239) |
| [`Manifolds`](categories.md#cat-manifolds) | subcategory interface method | [`src/sage/categories/manifolds.py:138`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L138) |
| [`VectorBundles`](categories.md#cat-vectorbundles) | nested category class | [`src/sage/categories/vector_bundles.py:144`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_bundles.py#L144) |
| [`VectorBundles`](categories.md#cat-vectorbundles) | subcategory interface method | [`src/sage/categories/vector_bundles.py:100`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_bundles.py#L100) |

### Classes the framework generates at 10.10 (2)

| class | module |
| --- | --- |
| `Manifolds.Differentiable` | `manifolds` |
| `VectorBundles.Differentiable` | `vector_bundles` |

## Distributive {#ax-distributive}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas` |
| interface declarations | `lattice_posets.LatticePosets:Distributive; magmas.Magmas:Distributive; magmas_and_additive_magmas.MagmasAndAdditiveMagmas:Distributive` |
| implementation or binding | `magmas_and_additive_magmas.MagmasAndAdditiveMagmas:Distributive [lazy-import binding]` |
| method expansions | `lattice_posets.LatticePosets:Distributive -> _with_axiom(ChainGraded) then _with_axiom(Trim); magmas.Magmas:Distributive -> calls AdditiveMagmas(), MagmasAndAdditiveMagmas(); magmas_and_additive_magmas.MagmasAndAdditiveMagmas:Distributive -> _with_axiom(Distributive)` |

### Declared in (4)

| category | declaration | source |
| --- | --- | --- |
| [`LatticePosets`](categories.md#cat-latticeposets) | subcategory interface method | [`src/sage/categories/lattice_posets.py:123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L123) |
| [`Magmas`](categories.md#cat-magmas) | subcategory interface method | [`src/sage/categories/magmas.py:265`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L265) |
| [`MagmasAndAdditiveMagmas`](categories.md#cat-magmasandadditivemagmas) | lazy-import binding | [`src/sage/categories/magmas_and_additive_magmas.py:134`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L134) |
| [`MagmasAndAdditiveMagmas`](categories.md#cat-magmasandadditivemagmas) | subcategory interface method | [`src/sage/categories/magmas_and_additive_magmas.py:59`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L59) |

## Division {#ax-division}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `division_rings.DivisionRings` |
| interface declarations | `rings.Rings:Division` |
| implementation or binding | `rings.Rings:Division [lazy-import binding]` |
| method expansions | `rings.Rings:Division -> _with_axiom(Division)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Rings`](categories.md#cat-rings) | lazy-import binding | [`src/sage/categories/rings.py:310`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L310) |
| [`Rings`](categories.md#cat-rings) | subcategory interface method | [`src/sage/categories/rings.py:287`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L287) |

## Endset {#ax-endset}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `homsets.Homsets:Endset` |
| implementation or binding | `finite_dimensional_modules_with_basis.FiniteDimensionalModulesWithBasis:Homsets.Endset [nested category class]; homsets.Homsets:Endset [nested category class]; modular_abelian_varieties.ModularAbelianVarieties:Homsets.Endset [nested category class]; modules.Modules:Homsets.Endset [nested category class]; schemes.AbelianVarieties:Homsets.Endset [nested category class]; simplicial_sets.SimplicialSets:Homsets.Endset [nested category class]` |
| method expansions | `homsets.Homsets:Endset -> _with_axiom(Endset)` |

### Declared in (7)

| category | declaration | source |
| --- | --- | --- |
| [`FiniteDimensionalModulesWithBasis`](categories.md#cat-finitedimensionalmoduleswithbasis) | nested category class | [`src/sage/categories/finite_dimensional_modules_with_basis.py:892`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L892) |
| [`Homsets`](categories.md#cat-homsets) | nested category class | [`src/sage/categories/homsets.py:296`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/homsets.py#L296) |
| [`Homsets`](categories.md#cat-homsets) | subcategory interface method | [`src/sage/categories/homsets.py:282`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/homsets.py#L282) |
| [`ModularAbelianVarieties`](categories.md#cat-modularabelianvarieties) | nested category class | [`src/sage/categories/modular_abelian_varieties.py:67`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modular_abelian_varieties.py#L67) |
| [`Modules`](categories.md#cat-modules) | nested category class | [`src/sage/categories/modules.py:810`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L810) |
| [`AbelianVarieties`](categories.md#cat-abelianvarieties) | nested category class | [`src/sage/categories/schemes.py:288`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L288) |
| [`SimplicialSets`](categories.md#cat-simplicialsets) | nested category class | [`src/sage/categories/simplicial_sets.py:158`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L158) |

### Classes the framework generates at 10.10 (6)

| class | module |
| --- | --- |
| `FiniteDimensionalModulesWithBasis.Homsets.Endset` | `finite_dimensional_modules_with_basis` |
| `Homsets.Endset` | `homsets` |
| `ModularAbelianVarieties.Homsets.Endset` | `modular_abelian_varieties` |
| `Modules.Homsets.Endset` | `modules` |
| `AbelianVarieties.Homsets.Endset` | `schemes` |
| `SimplicialSets.Homsets.Endset` | `simplicial_sets` |

## Enumerated {#ax-enumerated}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `enumerated_sets.EnumeratedSets` |
| interface declarations | `sets_cat.Sets:Enumerated` |
| implementation or binding | `sets_cat.Sets:Enumerated [lazy-import binding]` |
| method expansions | `sets_cat.Sets:Enumerated -> _with_axiom(Enumerated)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Sets`](categories.md#cat-sets) | lazy-import binding | [`src/sage/categories/sets_cat.py:1879`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1879) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:776`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L776) |

## Extremal {#ax-extremal}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `lattice_posets.LatticePosets:Extremal` |
| implementation or binding | `lattice_posets.LatticePosets:Extremal [nested category class]` |
| method expansions | `lattice_posets.LatticePosets:Extremal -> _with_axiom(Extremal)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`LatticePosets`](categories.md#cat-latticeposets) | nested category class | [`src/sage/categories/lattice_posets.py:214`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L214) |
| [`LatticePosets`](categories.md#cat-latticeposets) | subcategory interface method | [`src/sage/categories/lattice_posets.py:195`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L195) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `LatticePosets.Extremal` | `lattice_posets` |

## Facade {#ax-facade}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `facade_sets.FacadeSets` |
| interface declarations | `sets_cat.Sets:Facade` |
| implementation or binding | `category_with_axiom.DummyObjectsOverBaseRing:Commutative.Facade [nested category class]; category_with_axiom.TestObjects:Commutative.Facade [nested category class]` |
| method expansions | `sets_cat.Sets:Facade -> _with_axiom(Facade)` |

### Declared in (3)

| category | declaration | source |
| --- | --- | --- |
| [`DummyObjectsOverBaseRing`](categories.md#cat-dummyobjectsoverbasering) | nested category class | [`src/sage/categories/category_with_axiom.py:2825`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2825) |
| [`TestObjects`](categories.md#cat-testobjects) | nested category class | [`src/sage/categories/category_with_axiom.py:2780`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2780) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:799`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L799) |

### Classes the framework generates at 10.10 (2)

| class | module |
| --- | --- |
| `DummyObjectsOverBaseRing.Commutative.Facade` | `category_with_axiom` |
| `TestObjects.Commutative.Facade` | `category_with_axiom` |

## Finite {#ax-finite}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `finite_complex_reflection_groups.FiniteComplexReflectionGroups`, `finite_coxeter_groups.FiniteCoxeterGroups`, `finite_crystals.FiniteCrystals`, `finite_enumerated_sets.FiniteEnumeratedSets`, `finite_fields.FiniteFields`, `finite_groups.FiniteGroups`, `finite_lattice_posets.FiniteLatticePosets`, `finite_monoids.FiniteMonoids`, `finite_permutation_groups.FinitePermutationGroups`, `finite_posets.FinitePosets`, `finite_semigroups.FiniteSemigroups`, `finite_sets.FiniteSets`, `finite_weyl_groups.FiniteWeylGroups` |
| interface declarations | `sets_cat.Sets:Finite; sets_cat.Sets:Infinite.Finite` |
| implementation or binding | `additive_groups.AdditiveGroups:Finite [nested category class]; category_with_axiom.DummyObjectsOverBaseRing:Commutative.Finite [nested category class]; category_with_axiom.DummyObjectsOverBaseRing:FiniteDimensional.Finite [nested category class]; category_with_axiom.TestObjects:Commutative.Finite [nested category class]; category_with_axiom.TestObjects:FiniteDimensional.Finite [nested category class]; commutative_rings.CommutativeRings:Finite [nested category class]; complex_reflection_groups.ComplexReflectionGroups:Finite [lazy-import binding]; coxeter_groups.CoxeterGroups:Finite [lazy-import binding]; crystals.Crystals:Finite [lazy-import binding]; cw_complexes.CWComplexes:Finite [nested category class]; enumerated_sets.EnumeratedSets:Finite [lazy-import binding]; fields.Fields:Finite [lazy-import binding]; finitely_generated_semigroups.FinitelyGeneratedSemigroups:Finite [nested category class]; generalized_coxeter_groups.GeneralizedCoxeterGroups:Finite [nested category class]; groups.Groups:Finite [lazy-import binding]; lattice_posets.DistributiveLattices:Finite [nested category class]; lattice_posets.LatticePosets:Finite [lazy-import binding]; monoids.Monoids:Finite [lazy-import binding]; permutation_groups.PermutationGroups:Finite [lazy-import binding]; posets.Posets:Finite [lazy-import binding]; semigroups.Semigroups:Finite [lazy-import binding]; sets_cat.Sets:Finite [lazy-import binding]; simplicial_complexes.SimplicialComplexes:Finite [nested category class]; simplicial_sets.SimplicialSets:Finite [nested category class]; simplicial_sets.SimplicialSets:Pointed.Finite [nested category class]; supercrystals.SuperCrystals:Finite [nested category class]; weyl_groups.WeylGroups:Finite [lazy-import binding]` |
| method expansions | `sets_cat.Sets:Finite -> _with_axiom(Finite)` |

### Declared in (29)

| category | declaration | source |
| --- | --- | --- |
| [`AdditiveGroups`](categories.md#cat-additivegroups) | nested category class | [`src/sage/categories/additive_groups.py:62`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L62) |
| [`DummyObjectsOverBaseRing`](categories.md#cat-dummyobjectsoverbasering) | nested category class | [`src/sage/categories/category_with_axiom.py:2831`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2831) |
| [`DummyObjectsOverBaseRing`](categories.md#cat-dummyobjectsoverbasering) | nested category class | [`src/sage/categories/category_with_axiom.py:2817`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2817) |
| [`TestObjects`](categories.md#cat-testobjects) | nested category class | [`src/sage/categories/category_with_axiom.py:2786`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2786) |
| [`TestObjects`](categories.md#cat-testobjects) | nested category class | [`src/sage/categories/category_with_axiom.py:2772`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2772) |
| [`CommutativeRings`](categories.md#cat-commutativerings) | nested category class | [`src/sage/categories/commutative_rings.py:830`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_rings.py#L830) |
| [`ComplexReflectionGroups`](categories.md#cat-complexreflectiongroups) | lazy-import binding | [`src/sage/categories/complex_reflection_groups.py:143`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complex_reflection_groups.py#L143) |
| [`CoxeterGroups`](categories.md#cat-coxetergroups) | lazy-import binding | [`src/sage/categories/coxeter_groups.py:129`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coxeter_groups.py#L129) |
| [`Crystals`](categories.md#cat-crystals) | lazy-import binding | [`src/sage/categories/crystals.py:1822`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L1822) |
| [`CWComplexes`](categories.md#cat-cwcomplexes) | nested category class | [`src/sage/categories/cw_complexes.py:115`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L115) |
| [`EnumeratedSets`](categories.md#cat-enumeratedsets) | lazy-import binding | [`src/sage/categories/enumerated_sets.py:1123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L1123) |
| [`Fields`](categories.md#cat-fields) | lazy-import binding | [`src/sage/categories/fields.py:192`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/fields.py#L192) |
| [`FinitelyGeneratedSemigroups`](categories.md#cat-finitelygeneratedsemigroups) | nested category class | [`src/sage/categories/finitely_generated_semigroups.py:192`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_semigroups.py#L192) |
| [`GeneralizedCoxeterGroups`](categories.md#cat-generalizedcoxetergroups) | nested category class | [`src/sage/categories/generalized_coxeter_groups.py:72`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/generalized_coxeter_groups.py#L72) |
| [`Groups`](categories.md#cat-groups) | lazy-import binding | [`src/sage/categories/groups.py:491`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L491) |
| [`DistributiveLattices`](categories.md#cat-distributivelattices) | nested category class | [`src/sage/categories/lattice_posets.py:602`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L602) |
| [`LatticePosets`](categories.md#cat-latticeposets) | lazy-import binding | [`src/sage/categories/lattice_posets.py:211`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L211) |
| [`Monoids`](categories.md#cat-monoids) | lazy-import binding | [`src/sage/categories/monoids.py:77`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L77) |
| [`PermutationGroups`](categories.md#cat-permutationgroups) | lazy-import binding | [`src/sage/categories/permutation_groups.py:62`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/permutation_groups.py#L62) |
| [`Posets`](categories.md#cat-posets) | lazy-import binding | [`src/sage/categories/posets.py:155`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L155) |
| [`Semigroups`](categories.md#cat-semigroups) | lazy-import binding | [`src/sage/categories/semigroups.py:776`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L776) |
| [`Sets`](categories.md#cat-sets) | lazy-import binding | [`src/sage/categories/sets_cat.py:1880`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1880) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:736`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L736) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:1890`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1890) |
| [`SimplicialComplexes`](categories.md#cat-simplicialcomplexes) | nested category class | [`src/sage/categories/simplicial_complexes.py:59`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_complexes.py#L59) |
| [`SimplicialSets`](categories.md#cat-simplicialsets) | nested category class | [`src/sage/categories/simplicial_sets.py:176`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L176) |
| [`SimplicialSets`](categories.md#cat-simplicialsets) | nested category class | [`src/sage/categories/simplicial_sets.py:1117`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L1117) |
| [`SuperCrystals`](categories.md#cat-supercrystals) | nested category class | [`src/sage/categories/supercrystals.py:69`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercrystals.py#L69) |
| [`WeylGroups`](categories.md#cat-weylgroups) | lazy-import binding | [`src/sage/categories/weyl_groups.py:77`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/weyl_groups.py#L77) |

### Classes the framework generates at 10.10 (14)

| class | module |
| --- | --- |
| `AdditiveGroups.Finite` | `additive_groups` |
| `DummyObjectsOverBaseRing.Commutative.Finite` | `category_with_axiom` |
| `DummyObjectsOverBaseRing.FiniteDimensional.Finite` | `category_with_axiom` |
| `TestObjects.Commutative.Finite` | `category_with_axiom` |
| `TestObjects.FiniteDimensional.Finite` | `category_with_axiom` |
| `CommutativeRings.Finite` | `commutative_rings` |
| `CWComplexes.Finite` | `cw_complexes` |
| `FinitelyGeneratedSemigroups.Finite` | `finitely_generated_semigroups` |
| `GeneralizedCoxeterGroups.Finite` | `generalized_coxeter_groups` |
| `DistributiveLattices.Finite` | `lattice_posets` |
| `SimplicialComplexes.Finite` | `simplicial_complexes` |
| `SimplicialSets.Finite` | `simplicial_sets` |
| `SimplicialSets.Pointed.Finite` | `simplicial_sets` |
| `SuperCrystals.Finite` | `supercrystals` |

## FiniteDimensional {#ax-finitedimensional}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis`, `finite_dimensional_bialgebras_with_basis.FiniteDimensionalBialgebrasWithBasis`, `finite_dimensional_coalgebras_with_basis.FiniteDimensionalCoalgebrasWithBasis`, `finite_dimensional_graded_lie_algebras_with_basis.FiniteDimensionalGradedLieAlgebrasWithBasis`, `finite_dimensional_hopf_algebras_with_basis.FiniteDimensionalHopfAlgebrasWithBasis`, `finite_dimensional_modules_with_basis.FiniteDimensionalModulesWithBasis` |
| interface declarations | `category_with_axiom.Blahs:FiniteDimensional; cw_complexes.CWComplexes:FiniteDimensional; manifolds.Manifolds:FiniteDimensional; modules.Modules:FiniteDimensional` |
| implementation or binding | `algebras_with_basis.AlgebrasWithBasis:FiniteDimensional [lazy-import binding]; category_with_axiom.Blahs:FiniteDimensional [nested category class]; category_with_axiom.DummyObjectsOverBaseRing:Commutative.FiniteDimensional [nested category class]; category_with_axiom.DummyObjectsOverBaseRing:FiniteDimensional [nested category class]; category_with_axiom.TestObjects:Commutative.FiniteDimensional [nested category class]; category_with_axiom.TestObjects:FiniteDimensional [nested category class]; cw_complexes.CWComplexes:FiniteDimensional [nested category class]; filtered_modules_with_basis.FilteredModulesWithBasis:FiniteDimensional [nested category class]; graded_algebras_with_basis.GradedAlgebrasWithBasis:FiniteDimensional [nested category class]; graded_lie_algebras.GradedLieAlgebras:Stratified.FiniteDimensional [nested category class]; graded_lie_algebras_with_basis.GradedLieAlgebrasWithBasis:FiniteDimensional [lazy-import binding]; hopf_algebras_with_basis.HopfAlgebrasWithBasis:FiniteDimensional [lazy-import binding]; lie_algebras.LieAlgebras:FiniteDimensional [nested category class]; magmatic_algebras.MagmaticAlgebras:WithBasis.FiniteDimensional [nested category class]; manifolds.Manifolds:FiniteDimensional [nested category class]; modules.Modules:FiniteDimensional [nested category class]; modules_with_basis.ModulesWithBasis:FiniteDimensional [lazy-import binding]; semisimple_algebras.SemisimpleAlgebras:FiniteDimensional [nested category class]; triangular_kac_moody_algebras.TriangularKacMoodyAlgebras:FiniteDimensional [nested category class]; vector_spaces.VectorSpaces:FiniteDimensional [nested category class]; vector_spaces.VectorSpaces:WithBasis.FiniteDimensional [nested category class]` |
| method expansions | `category_with_axiom.Blahs:FiniteDimensional -> _with_axiom(FiniteDimensional); cw_complexes.CWComplexes:FiniteDimensional -> _with_axiom(FiniteDimensional); manifolds.Manifolds:FiniteDimensional -> _with_axiom(FiniteDimensional); modules.Modules:FiniteDimensional -> _with_axiom(FiniteDimensional)` |

### Declared in (25)

| category | declaration | source |
| --- | --- | --- |
| [`AlgebrasWithBasis`](categories.md#cat-algebraswithbasis) | lazy-import binding | [`src/sage/categories/algebras_with_basis.py:125`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L125) |
| [`Blahs`](categories.md#cat-blahs) | nested category class | [`src/sage/categories/category_with_axiom.py:2632`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2632) |
| [`Blahs`](categories.md#cat-blahs) | subcategory interface method | [`src/sage/categories/category_with_axiom.py:2625`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2625) |
| [`DummyObjectsOverBaseRing`](categories.md#cat-dummyobjectsoverbasering) | nested category class | [`src/sage/categories/category_with_axiom.py:2828`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2828) |
| [`DummyObjectsOverBaseRing`](categories.md#cat-dummyobjectsoverbasering) | nested category class | [`src/sage/categories/category_with_axiom.py:2816`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2816) |
| [`TestObjects`](categories.md#cat-testobjects) | nested category class | [`src/sage/categories/category_with_axiom.py:2783`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2783) |
| [`TestObjects`](categories.md#cat-testobjects) | nested category class | [`src/sage/categories/category_with_axiom.py:2771`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2771) |
| [`CWComplexes`](categories.md#cat-cwcomplexes) | nested category class | [`src/sage/categories/cw_complexes.py:110`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L110) |
| [`CWComplexes`](categories.md#cat-cwcomplexes) | subcategory interface method | [`src/sage/categories/cw_complexes.py:84`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L84) |
| [`FilteredModulesWithBasis`](categories.md#cat-filteredmoduleswithbasis) | nested category class | [`src/sage/categories/filtered_modules_with_basis.py:1161`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules_with_basis.py#L1161) |
| [`GradedAlgebrasWithBasis`](categories.md#cat-gradedalgebraswithbasis) | nested category class | [`src/sage/categories/graded_algebras_with_basis.py:157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras_with_basis.py#L157) |
| [`GradedLieAlgebras`](categories.md#cat-gradedliealgebras) | nested category class | [`src/sage/categories/graded_lie_algebras.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras.py#L60) |
| [`GradedLieAlgebrasWithBasis`](categories.md#cat-gradedliealgebraswithbasis) | lazy-import binding | [`src/sage/categories/graded_lie_algebras_with_basis.py:41`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras_with_basis.py#L41) |
| [`HopfAlgebrasWithBasis`](categories.md#cat-hopfalgebraswithbasis) | lazy-import binding | [`src/sage/categories/hopf_algebras_with_basis.py:157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L157) |
| [`LieAlgebras`](categories.md#cat-liealgebras) | nested category class | [`src/sage/categories/lie_algebras.py:174`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L174) |
| [`MagmaticAlgebras`](categories.md#cat-magmaticalgebras) | nested category class | [`src/sage/categories/magmatic_algebras.py:224`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L224) |
| [`Manifolds`](categories.md#cat-manifolds) | nested category class | [`src/sage/categories/manifolds.py:312`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L312) |
| [`Manifolds`](categories.md#cat-manifolds) | subcategory interface method | [`src/sage/categories/manifolds.py:117`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L117) |
| [`Modules`](categories.md#cat-modules) | nested category class | [`src/sage/categories/modules.py:514`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L514) |
| [`Modules`](categories.md#cat-modules) | subcategory interface method | [`src/sage/categories/modules.py:341`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L341) |
| [`ModulesWithBasis`](categories.md#cat-moduleswithbasis) | lazy-import binding | [`src/sage/categories/modules_with_basis.py:195`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L195) |
| [`SemisimpleAlgebras`](categories.md#cat-semisimplealgebras) | nested category class | [`src/sage/categories/semisimple_algebras.py:111`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semisimple_algebras.py#L111) |
| [`TriangularKacMoodyAlgebras`](categories.md#cat-triangularkacmoodyalgebras) | nested category class | [`src/sage/categories/triangular_kac_moody_algebras.py:341`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/triangular_kac_moody_algebras.py#L341) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:285`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L285) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:225`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L225) |

### Classes the framework generates at 10.10 (17)

| class | module |
| --- | --- |
| `Blahs.FiniteDimensional` | `category_with_axiom` |
| `DummyObjectsOverBaseRing.Commutative.FiniteDimensional` | `category_with_axiom` |
| `DummyObjectsOverBaseRing.FiniteDimensional` | `category_with_axiom` |
| `TestObjects.Commutative.FiniteDimensional` | `category_with_axiom` |
| `TestObjects.FiniteDimensional` | `category_with_axiom` |
| `CWComplexes.FiniteDimensional` | `cw_complexes` |
| `FilteredModulesWithBasis.FiniteDimensional` | `filtered_modules_with_basis` |
| `GradedAlgebrasWithBasis.FiniteDimensional` | `graded_algebras_with_basis` |
| `GradedLieAlgebras.Stratified.FiniteDimensional` | `graded_lie_algebras` |
| `LieAlgebras.FiniteDimensional` | `lie_algebras` |
| `MagmaticAlgebras.WithBasis.FiniteDimensional` | `magmatic_algebras` |
| `Manifolds.FiniteDimensional` | `manifolds` |
| `Modules.FiniteDimensional` | `modules` |
| `SemisimpleAlgebras.FiniteDimensional` | `semisimple_algebras` |
| `TriangularKacMoodyAlgebras.FiniteDimensional` | `triangular_kac_moody_algebras` |
| `VectorSpaces.FiniteDimensional` | `vector_spaces` |
| `VectorSpaces.WithBasis.FiniteDimensional` | `vector_spaces` |

## FinitelyGeneratedAsLambdaBracketAlgebra {#ax-finitelygeneratedaslambdabracketalgebra}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `finitely_generated_lambda_bracket_algebras.FinitelyGeneratedLambdaBracketAlgebras`, `finitely_generated_lie_conformal_algebras.FinitelyGeneratedLieConformalAlgebras` |
| interface declarations | `lambda_bracket_algebras.LambdaBracketAlgebras:FinitelyGeneratedAsLambdaBracketAlgebra` |
| implementation or binding | `lambda_bracket_algebras.LambdaBracketAlgebras:FinitelyGeneratedAsLambdaBracketAlgebra [lazy-import binding]; lambda_bracket_algebras_with_basis.LambdaBracketAlgebrasWithBasis:FinitelyGeneratedAsLambdaBracketAlgebra [nested category class]; lie_conformal_algebras.LieConformalAlgebras:FinitelyGeneratedAsLambdaBracketAlgebra [lazy-import binding]; lie_conformal_algebras_with_basis.LieConformalAlgebrasWithBasis:FinitelyGeneratedAsLambdaBracketAlgebra [nested category class]` |
| method expansions | `lambda_bracket_algebras.LambdaBracketAlgebras:FinitelyGeneratedAsLambdaBracketAlgebra -> _with_axiom(FinitelyGeneratedAsLambdaBracketAlgebra)` |

### Declared in (5)

| category | declaration | source |
| --- | --- | --- |
| [`LambdaBracketAlgebras`](categories.md#cat-lambdabracketalgebras) | lazy-import binding | [`src/sage/categories/lambda_bracket_algebras.py:276`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras.py#L276) |
| [`LambdaBracketAlgebras`](categories.md#cat-lambdabracketalgebras) | subcategory interface method | [`src/sage/categories/lambda_bracket_algebras.py:87`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras.py#L87) |
| [`LambdaBracketAlgebrasWithBasis`](categories.md#cat-lambdabracketalgebraswithbasis) | nested category class | [`src/sage/categories/lambda_bracket_algebras_with_basis.py:61`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras_with_basis.py#L61) |
| [`LieConformalAlgebras`](categories.md#cat-lieconformalalgebras) | lazy-import binding | [`src/sage/categories/lie_conformal_algebras.py:347`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras.py#L347) |
| [`LieConformalAlgebrasWithBasis`](categories.md#cat-lieconformalalgebraswithbasis) | nested category class | [`src/sage/categories/lie_conformal_algebras_with_basis.py:85`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L85) |

### Classes the framework generates at 10.10 (2)

| class | module |
| --- | --- |
| `LambdaBracketAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra` | `lambda_bracket_algebras_with_basis` |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra` | `lie_conformal_algebras_with_basis` |

## FinitelyGeneratedAsMagma {#ax-finitelygeneratedasmagma}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `finitely_generated_magmas.FinitelyGeneratedMagmas`, `finitely_generated_semigroups.FinitelyGeneratedSemigroups` |
| interface declarations | `magmas.Magmas:FinitelyGeneratedAsMagma` |
| implementation or binding | `magmas.Magmas:FinitelyGeneratedAsMagma [lazy-import binding]; semigroups.Semigroups:FinitelyGeneratedAsMagma [lazy-import binding]` |
| method expansions | `magmas.Magmas:FinitelyGeneratedAsMagma -> _with_axiom(FinitelyGeneratedAsMagma)` |

### Declared in (3)

| category | declaration | source |
| --- | --- | --- |
| [`Magmas`](categories.md#cat-magmas) | lazy-import binding | [`src/sage/categories/magmas.py:343`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L343) |
| [`Magmas`](categories.md#cat-magmas) | subcategory interface method | [`src/sage/categories/magmas.py:165`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L165) |
| [`Semigroups`](categories.md#cat-semigroups) | lazy-import binding | [`src/sage/categories/semigroups.py:777`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L777) |

## FinitelyPresented {#ax-finitelypresented}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `modules.Modules:FinitelyPresented` |
| implementation or binding | `modules.Modules:FinitelyPresented [nested category class]` |
| method expansions | `modules.Modules:FinitelyPresented -> _with_axiom(FinitelyPresented)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Modules`](categories.md#cat-modules) | nested category class | [`src/sage/categories/modules.py:562`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L562) |
| [`Modules`](categories.md#cat-modules) | subcategory interface method | [`src/sage/categories/modules.py:363`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L363) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Modules.FinitelyPresented` | `modules` |

## Flying {#ax-flying}

| field | value |
| --- | --- |
| status | test-only placeholder |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `category_with_axiom.Blahs:Flying` |
| implementation or binding | `category_with_axiom.Blahs:Flying [nested category class]` |
| method expansions | `category_with_axiom.Blahs:Flying -> _with_axiom(Flying)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Blahs`](categories.md#cat-blahs) | nested category class | [`src/sage/categories/category_with_axiom.py:2645`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2645) |
| [`Blahs`](categories.md#cat-blahs) | subcategory interface method | [`src/sage/categories/category_with_axiom.py:2629`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2629) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Blahs.Flying` | `category_with_axiom` |

## HTrivial {#ax-htrivial}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/semigroups.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L27) |
| defining categories | `h_trivial_semigroups.HTrivialSemigroups` |
| interface declarations | `semigroups.Semigroups:HTrivial` |
| implementation or binding | `semigroups.Semigroups:HTrivial [lazy-import binding]` |
| method expansions | `semigroups.Semigroups:HTrivial -> _with_axiom(HTrivial)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Semigroups`](categories.md#cat-semigroups) | lazy-import binding | [`src/sage/categories/semigroups.py:782`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L782) |
| [`Semigroups`](categories.md#cat-semigroups) | subcategory interface method | [`src/sage/categories/semigroups.py:692`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L692) |

## Infinite {#ax-infinite}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `infinite_enumerated_sets.InfiniteEnumeratedSets` |
| interface declarations | `finite_sets.FiniteSets:Infinite; sets_cat.Sets:Infinite` |
| implementation or binding | `enumerated_sets.EnumeratedSets:Infinite [lazy-import binding]; sets_cat.Sets:Infinite [nested category class]` |
| method expansions | `sets_cat.Sets:Infinite -> _with_axiom(Infinite)` |

### Declared in (4)

| category | declaration | source |
| --- | --- | --- |
| [`EnumeratedSets`](categories.md#cat-enumeratedsets) | lazy-import binding | [`src/sage/categories/enumerated_sets.py:1124`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L1124) |
| [`FiniteSets`](categories.md#cat-finitesets) | subcategory interface method | [`src/sage/categories/finite_sets.py:42`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L42) |
| [`Sets`](categories.md#cat-sets) | nested category class | [`src/sage/categories/sets_cat.py:1887`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1887) |
| [`Sets`](categories.md#cat-sets) | subcategory interface method | [`src/sage/categories/sets_cat.py:756`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L756) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Sets.Infinite` | `sets_cat` |

## Inverse {#ax-inverse}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `groups.Groups` |
| interface declarations | `magmas.Magmas:Unital.Inverse` |
| implementation or binding | `magmas.Magmas:Unital.Inverse [nested category class]; monoids.Monoids:Inverse [lazy-import binding]` |
| method expansions | `magmas.Magmas:Unital.Inverse -> _with_axiom(Inverse)` |

### Declared in (3)

| category | declaration | source |
| --- | --- | --- |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:598`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L598) |
| [`Magmas`](categories.md#cat-magmas) | subcategory interface method | [`src/sage/categories/magmas.py:570`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L570) |
| [`Monoids`](categories.md#cat-monoids) | lazy-import binding | [`src/sage/categories/monoids.py:78`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L78) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Magmas.Unital.Inverse` | `magmas` |

## Irreducible {#ax-irreducible}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `complex_reflection_or_generalized_coxeter_groups.ComplexReflectionOrGeneralizedCoxeterGroups:Irreducible` |
| implementation or binding | `complex_reflection_or_generalized_coxeter_groups.ComplexReflectionOrGeneralizedCoxeterGroups:Irreducible [nested category class]; finite_complex_reflection_groups.FiniteComplexReflectionGroups:Irreducible [nested category class]; finite_complex_reflection_groups.FiniteComplexReflectionGroups:WellGenerated.Irreducible [nested category class]` |
| method expansions | `complex_reflection_or_generalized_coxeter_groups.ComplexReflectionOrGeneralizedCoxeterGroups:Irreducible -> _with_axiom(Irreducible)` |

### Declared in (4)

| category | declaration | source |
| --- | --- | --- |
| [`ComplexReflectionOrGeneralizedCoxeterGroups`](categories.md#cat-complexreflectionorgeneralizedcoxetergroups) | nested category class | [`src/sage/categories/complex_reflection_or_generalized_coxeter_groups.py:1233`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complex_reflection_or_generalized_coxeter_groups.py#L1233) |
| [`ComplexReflectionOrGeneralizedCoxeterGroups`](categories.md#cat-complexreflectionorgeneralizedcoxetergroups) | subcategory interface method | [`src/sage/categories/complex_reflection_or_generalized_coxeter_groups.py:116`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complex_reflection_or_generalized_coxeter_groups.py#L116) |
| [`FiniteComplexReflectionGroups`](categories.md#cat-finitecomplexreflectiongroups) | nested category class | [`src/sage/categories/finite_complex_reflection_groups.py:763`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_complex_reflection_groups.py#L763) |
| [`FiniteComplexReflectionGroups`](categories.md#cat-finitecomplexreflectiongroups) | nested category class | [`src/sage/categories/finite_complex_reflection_groups.py:1237`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_complex_reflection_groups.py#L1237) |

### Classes the framework generates at 10.10 (3)

| class | module |
| --- | --- |
| `ComplexReflectionOrGeneralizedCoxeterGroups.Irreducible` | `complex_reflection_or_generalized_coxeter_groups` |
| `FiniteComplexReflectionGroups.Irreducible` | `finite_complex_reflection_groups` |
| `FiniteComplexReflectionGroups.WellGenerated.Irreducible` | `finite_complex_reflection_groups` |

## JTrivial {#ax-jtrivial}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/semigroups.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L27) |
| defining categories | `j_trivial_semigroups.JTrivialSemigroups` |
| interface declarations | `magmas.Magmas:JTrivial; semigroups.Semigroups:JTrivial` |
| implementation or binding | `magmas.Magmas:JTrivial [nested category class]; semigroups.Semigroups:JTrivial [lazy-import binding]` |
| method expansions | `magmas.Magmas:JTrivial -> _with_axiom(JTrivial); semigroups.Semigroups:JTrivial -> _with_axiom(JTrivial)` |

### Declared in (4)

| category | declaration | source |
| --- | --- | --- |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:345`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L345) |
| [`Magmas`](categories.md#cat-magmas) | subcategory interface method | [`src/sage/categories/magmas.py:320`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L320) |
| [`Semigroups`](categories.md#cat-semigroups) | lazy-import binding | [`src/sage/categories/semigroups.py:781`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L781) |
| [`Semigroups`](categories.md#cat-semigroups) | subcategory interface method | [`src/sage/categories/semigroups.py:636`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L636) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Magmas.JTrivial` | `magmas` |

## LTrivial {#ax-ltrivial}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/semigroups.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L27) |
| defining categories | `l_trivial_semigroups.LTrivialSemigroups` |
| interface declarations | `semigroups.Semigroups:LTrivial` |
| implementation or binding | `semigroups.Semigroups:LTrivial [lazy-import binding]` |
| method expansions | `semigroups.Semigroups:LTrivial -> _with_axiom(LTrivial)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Semigroups`](categories.md#cat-semigroups) | lazy-import binding | [`src/sage/categories/semigroups.py:779`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L779) |
| [`Semigroups`](categories.md#cat-semigroups) | subcategory interface method | [`src/sage/categories/semigroups.py:546`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L546) |

## Nilpotent {#ax-nilpotent}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `finite_dimensional_nilpotent_lie_algebras_with_basis.FiniteDimensionalNilpotentLieAlgebrasWithBasis` |
| interface declarations | `lie_algebras.LieAlgebras:Nilpotent` |
| implementation or binding | `finite_dimensional_lie_algebras_with_basis.FiniteDimensionalLieAlgebrasWithBasis:Nilpotent [lazy-import binding]; lie_algebras.LieAlgebras:Nilpotent [nested category class]` |
| method expansions | `lie_algebras.LieAlgebras:Nilpotent -> _with_axiom(Nilpotent)` |

### Declared in (3)

| category | declaration | source |
| --- | --- | --- |
| [`FiniteDimensionalLieAlgebrasWithBasis`](categories.md#cat-finitedimensionalliealgebraswithbasis) | lazy-import binding | [`src/sage/categories/finite_dimensional_lie_algebras_with_basis.py:87`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_lie_algebras_with_basis.py#L87) |
| [`LieAlgebras`](categories.md#cat-liealgebras) | nested category class | [`src/sage/categories/lie_algebras.py:203`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L203) |
| [`LieAlgebras`](categories.md#cat-liealgebras) | subcategory interface method | [`src/sage/categories/lie_algebras.py:94`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L94) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `LieAlgebras.Nilpotent` | `lie_algebras` |

## NoZeroDivisors {#ax-nozerodivisors}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `domains.Domains` |
| interface declarations | `rings.Rings:NoZeroDivisors` |
| implementation or binding | `rings.Rings:NoZeroDivisors [lazy-import binding]` |
| method expansions | `rings.Rings:NoZeroDivisors -> _with_axiom(NoZeroDivisors)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Rings`](categories.md#cat-rings) | lazy-import binding | [`src/sage/categories/rings.py:309`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L309) |
| [`Rings`](categories.md#cat-rings) | subcategory interface method | [`src/sage/categories/rings.py:264`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L264) |

## Pointed {#ax-pointed}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `simplicial_sets.SimplicialSets:Pointed` |
| implementation or binding | `simplicial_sets.SimplicialSets:Pointed [nested category class]` |
| method expansions | `simplicial_sets.SimplicialSets:Pointed -> _with_axiom(Pointed)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`SimplicialSets`](categories.md#cat-simplicialsets) | nested category class | [`src/sage/categories/simplicial_sets.py:201`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L201) |
| [`SimplicialSets`](categories.md#cat-simplicialsets) | subcategory interface method | [`src/sage/categories/simplicial_sets.py:186`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L186) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `SimplicialSets.Pointed` | `simplicial_sets` |

## RTrivial {#ax-rtrivial}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/semigroups.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L27) |
| defining categories | `r_trivial_semigroups.RTrivialSemigroups` |
| interface declarations | `semigroups.Semigroups:RTrivial` |
| implementation or binding | `semigroups.Semigroups:RTrivial [lazy-import binding]` |
| method expansions | `semigroups.Semigroups:RTrivial -> _with_axiom(RTrivial)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Semigroups`](categories.md#cat-semigroups) | lazy-import binding | [`src/sage/categories/semigroups.py:780`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L780) |
| [`Semigroups`](categories.md#cat-semigroups) | subcategory interface method | [`src/sage/categories/semigroups.py:591`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L591) |

## Semidistributive {#ax-semidistributive}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `lattice_posets.LatticePosets:Semidistributive` |
| implementation or binding | `lattice_posets.LatticePosets:Semidistributive [nested category class]` |
| method expansions | `lattice_posets.LatticePosets:Semidistributive -> _with_axiom(Semidistributive)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`LatticePosets`](categories.md#cat-latticeposets) | nested category class | [`src/sage/categories/lattice_posets.py:278`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L278) |
| [`LatticePosets`](categories.md#cat-latticeposets) | subcategory interface method | [`src/sage/categories/lattice_posets.py:158`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L158) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `LatticePosets.Semidistributive` | `lattice_posets` |

## Smooth {#ax-smooth}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `manifolds.Manifolds:Smooth; vector_bundles.VectorBundles:Smooth` |
| implementation or binding | `manifolds.Manifolds:Smooth [nested category class]; vector_bundles.VectorBundles:Smooth [nested category class]` |
| method expansions | `manifolds.Manifolds:Smooth -> _with_axiom(Smooth); vector_bundles.VectorBundles:Smooth -> _with_axiom(Smooth)` |

### Declared in (4)

| category | declaration | source |
| --- | --- | --- |
| [`Manifolds`](categories.md#cat-manifolds) | nested category class | [`src/sage/categories/manifolds.py:246`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L246) |
| [`Manifolds`](categories.md#cat-manifolds) | subcategory interface method | [`src/sage/categories/manifolds.py:159`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L159) |
| [`VectorBundles`](categories.md#cat-vectorbundles) | nested category class | [`src/sage/categories/vector_bundles.py:152`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_bundles.py#L152) |
| [`VectorBundles`](categories.md#cat-vectorbundles) | subcategory interface method | [`src/sage/categories/vector_bundles.py:123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_bundles.py#L123) |

### Classes the framework generates at 10.10 (2)

| class | module |
| --- | --- |
| `Manifolds.Smooth` | `manifolds` |
| `VectorBundles.Smooth` | `vector_bundles` |

## Stone {#ax-stone}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `lattice_posets.LatticePosets:Stone` |
| implementation or binding | `lattice_posets.LatticePosets:Stone [nested category class]` |
| method expansions | `lattice_posets.LatticePosets:Stone -> _with_axiom(Stone)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`LatticePosets`](categories.md#cat-latticeposets) | nested category class | [`src/sage/categories/lattice_posets.py:496`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L496) |
| [`LatticePosets`](categories.md#cat-latticeposets) | subcategory interface method | [`src/sage/categories/lattice_posets.py:108`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L108) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `LatticePosets.Stone` | `lattice_posets` |

## Stratified {#ax-stratified}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `graded_lie_algebras.GradedLieAlgebras:Stratified` |
| implementation or binding | `finite_dimensional_graded_lie_algebras_with_basis.FiniteDimensionalGradedLieAlgebrasWithBasis:Stratified [nested category class]; graded_lie_algebras.GradedLieAlgebras:Stratified [nested category class]` |
| method expansions | `graded_lie_algebras.GradedLieAlgebras:Stratified -> _with_axiom(Stratified)` |

### Declared in (3)

| category | declaration | source |
| --- | --- | --- |
| [`FiniteDimensionalGradedLieAlgebrasWithBasis`](categories.md#cat-finitedimensionalgradedliealgebraswithbasis) | nested category class | [`src/sage/categories/finite_dimensional_graded_lie_algebras_with_basis.py:112`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_graded_lie_algebras_with_basis.py#L112) |
| [`GradedLieAlgebras`](categories.md#cat-gradedliealgebras) | nested category class | [`src/sage/categories/graded_lie_algebras.py:47`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras.py#L47) |
| [`GradedLieAlgebras`](categories.md#cat-gradedliealgebras) | subcategory interface method | [`src/sage/categories/graded_lie_algebras.py:33`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras.py#L33) |

### Classes the framework generates at 10.10 (2)

| class | module |
| --- | --- |
| `FiniteDimensionalGradedLieAlgebrasWithBasis.Stratified` | `finite_dimensional_graded_lie_algebras_with_basis` |
| `GradedLieAlgebras.Stratified` | `graded_lie_algebras` |

## Supercocommutative {#ax-supercocommutative}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `coalgebras.Coalgebras:Super.Supercocommutative` |
| implementation or binding | `coalgebras.Coalgebras:Super.Supercocommutative [nested category class]` |
| method expansions | `coalgebras.Coalgebras:Super.Supercocommutative -> _with_axiom(Supercocommutative)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`Coalgebras`](categories.md#cat-coalgebras) | nested category class | [`src/sage/categories/coalgebras.py:283`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L283) |
| [`Coalgebras`](categories.md#cat-coalgebras) | subcategory interface method | [`src/sage/categories/coalgebras.py:262`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L262) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `Coalgebras.Super.Supercocommutative` | `coalgebras` |

## Supercommutative {#ax-supercommutative}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `supercommutative_algebras.SupercommutativeAlgebras` |
| interface declarations | `algebras.Algebras:Supercommutative; super_algebras.SuperAlgebras:Supercommutative` |
| implementation or binding | `super_algebras.SuperAlgebras:Supercommutative [lazy-import binding]` |
| method expansions | `algebras.Algebras:Supercommutative -> calls Super(); super_algebras.SuperAlgebras:Supercommutative -> _with_axiom(Supercommutative)` |

### Declared in (3)

| category | declaration | source |
| --- | --- | --- |
| [`Algebras`](categories.md#cat-algebras) | subcategory interface method | [`src/sage/categories/algebras.py:109`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L109) |
| [`SuperAlgebras`](categories.md#cat-superalgebras) | lazy-import binding | [`src/sage/categories/super_algebras.py:53`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L53) |
| [`SuperAlgebras`](categories.md#cat-superalgebras) | subcategory interface method | [`src/sage/categories/super_algebras.py:110`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L110) |

## Trim {#ax-trim}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `lattice_posets.LatticePosets:Trim` |
| implementation or binding | `lattice_posets.LatticePosets:Trim [nested category class]` |
| method expansions | `lattice_posets.LatticePosets:Trim -> _with_axiom(Trim)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`LatticePosets`](categories.md#cat-latticeposets) | nested category class | [`src/sage/categories/lattice_posets.py:239`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L239) |
| [`LatticePosets`](categories.md#cat-latticeposets) | subcategory interface method | [`src/sage/categories/lattice_posets.py:180`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L180) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `LatticePosets.Trim` | `lattice_posets` |

## Unital {#ax-unital}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `algebras.Algebras`, `monoids.Monoids`, `rings.Rings`, `semirings.Semirings`, `unital_algebras.UnitalAlgebras` |
| interface declarations | `category_with_axiom.Blahs:Unital; magmas.Magmas:Unital` |
| implementation or binding | `associative_algebras.AssociativeAlgebras:Unital [lazy-import binding]; category_with_axiom.Blahs:Unital [nested category class]; category_with_axiom.DummyObjectsOverBaseRing:FiniteDimensional.Unital [nested category class]; category_with_axiom.DummyObjectsOverBaseRing:Unital [nested category class]; category_with_axiom.TestObjects:FiniteDimensional.Unital [nested category class]; category_with_axiom.TestObjects:Unital [nested category class]; distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas:AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative.Unital [lazy-import binding]; magmas.Magmas:Unital [nested category class]; magmatic_algebras.MagmaticAlgebras:Unital [lazy-import binding]; rngs.Rngs:Unital [lazy-import binding]; semigroups.Semigroups:Unital [lazy-import binding]` |
| method expansions | `category_with_axiom.Blahs:Unital -> _with_axiom(Unital); magmas.Magmas:Unital -> _with_axiom(Unital)` |

### Declared in (13)

| category | declaration | source |
| --- | --- | --- |
| [`AssociativeAlgebras`](categories.md#cat-associativealgebras) | lazy-import binding | [`src/sage/categories/associative_algebras.py:46`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/associative_algebras.py#L46) |
| [`Blahs`](categories.md#cat-blahs) | nested category class | [`src/sage/categories/category_with_axiom.py:2641`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2641) |
| [`Blahs`](categories.md#cat-blahs) | subcategory interface method | [`src/sage/categories/category_with_axiom.py:2627`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2627) |
| [`DummyObjectsOverBaseRing`](categories.md#cat-dummyobjectsoverbasering) | nested category class | [`src/sage/categories/category_with_axiom.py:2820`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2820) |
| [`DummyObjectsOverBaseRing`](categories.md#cat-dummyobjectsoverbasering) | nested category class | [`src/sage/categories/category_with_axiom.py:2834`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2834) |
| [`TestObjects`](categories.md#cat-testobjects) | nested category class | [`src/sage/categories/category_with_axiom.py:2775`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2775) |
| [`TestObjects`](categories.md#cat-testobjects) | nested category class | [`src/sage/categories/category_with_axiom.py:2789`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2789) |
| [`DistributiveMagmasAndAdditiveMagmas`](categories.md#cat-distributivemagmasandadditivemagmas) | lazy-import binding | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:46`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L46) |
| [`Magmas`](categories.md#cat-magmas) | nested category class | [`src/sage/categories/magmas.py:457`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L457) |
| [`Magmas`](categories.md#cat-magmas) | subcategory interface method | [`src/sage/categories/magmas.py:129`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L129) |
| [`MagmaticAlgebras`](categories.md#cat-magmaticalgebras) | lazy-import binding | [`src/sage/categories/magmatic_algebras.py:101`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L101) |
| [`Rngs`](categories.md#cat-rngs) | lazy-import binding | [`src/sage/categories/rngs.py:51`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rngs.py#L51) |
| [`Semigroups`](categories.md#cat-semigroups) | lazy-import binding | [`src/sage/categories/semigroups.py:778`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L778) |

### Classes the framework generates at 10.10 (6)

| class | module |
| --- | --- |
| `Blahs.Unital` | `category_with_axiom` |
| `DummyObjectsOverBaseRing.FiniteDimensional.Unital` | `category_with_axiom` |
| `DummyObjectsOverBaseRing.Unital` | `category_with_axiom` |
| `TestObjects.FiniteDimensional.Unital` | `category_with_axiom` |
| `TestObjects.Unital` | `category_with_axiom` |
| `Magmas.Unital` | `magmas` |

## WellGenerated {#ax-wellgenerated}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| interface declarations | `finite_complex_reflection_groups.FiniteComplexReflectionGroups:WellGenerated` |
| implementation or binding | `finite_complex_reflection_groups.FiniteComplexReflectionGroups:WellGenerated [nested category class]` |
| method expansions | `finite_complex_reflection_groups.FiniteComplexReflectionGroups:WellGenerated -> _with_axiom(WellGenerated)` |

### Declared in (2)

| category | declaration | source |
| --- | --- | --- |
| [`FiniteComplexReflectionGroups`](categories.md#cat-finitecomplexreflectiongroups) | nested category class | [`src/sage/categories/finite_complex_reflection_groups.py:1108`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_complex_reflection_groups.py#L1108) |
| [`FiniteComplexReflectionGroups`](categories.md#cat-finitecomplexreflectiongroups) | subcategory interface method | [`src/sage/categories/finite_complex_reflection_groups.py:87`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_complex_reflection_groups.py#L87) |

### Classes the framework generates at 10.10 (1)

| class | module |
| --- | --- |
| `FiniteComplexReflectionGroups.WellGenerated` | `finite_complex_reflection_groups` |

## WithBasis {#ax-withbasis}

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `algebras_with_basis.AlgebrasWithBasis`, `bialgebras_with_basis.BialgebrasWithBasis`, `coalgebras_with_basis.CoalgebrasWithBasis`, `finite_dimensional_lie_algebras_with_basis.FiniteDimensionalLieAlgebrasWithBasis`, `finite_dimensional_semisimple_algebras_with_basis.FiniteDimensionalSemisimpleAlgebrasWithBasis`, `hopf_algebras_with_basis.HopfAlgebrasWithBasis`, `lambda_bracket_algebras_with_basis.LambdaBracketAlgebrasWithBasis`, `lie_algebras_with_basis.LieAlgebrasWithBasis`, `lie_conformal_algebras_with_basis.LieConformalAlgebrasWithBasis`, `modules_with_basis.ModulesWithBasis` |
| interface declarations | `modules.Modules:WithBasis` |
| implementation or binding | `algebras.Algebras:WithBasis [lazy-import binding]; bialgebras.Bialgebras:WithBasis [lazy-import binding]; coalgebras.Coalgebras:WithBasis [lazy-import binding]; hopf_algebras.HopfAlgebras:WithBasis [lazy-import binding]; lambda_bracket_algebras.LambdaBracketAlgebras:WithBasis [lazy-import binding]; lie_algebras.LieAlgebras:FiniteDimensional.WithBasis [lazy-import binding]; lie_algebras.LieAlgebras:WithBasis [lazy-import binding]; lie_conformal_algebras.LieConformalAlgebras:WithBasis [lazy-import binding]; magmatic_algebras.MagmaticAlgebras:WithBasis [nested category class]; modules.Modules:WithBasis [lazy-import binding]; quantum_group_representations.QuantumGroupRepresentations:WithBasis [nested category class]; semisimple_algebras.SemisimpleAlgebras:FiniteDimensional.WithBasis [lazy-import binding]; supercommutative_algebras.SupercommutativeAlgebras:WithBasis [nested category class]; unital_algebras.UnitalAlgebras:WithBasis [nested category class]; vector_spaces.VectorSpaces:WithBasis [nested category class]` |
| method expansions | `modules.Modules:WithBasis -> _with_axiom(WithBasis)` |

### Declared in (16)

| category | declaration | source |
| --- | --- | --- |
| [`Algebras`](categories.md#cat-algebras) | lazy-import binding | [`src/sage/categories/algebras.py:138`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L138) |
| [`Bialgebras`](categories.md#cat-bialgebras) | lazy-import binding | [`src/sage/categories/bialgebras.py:100`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/bialgebras.py#L100) |
| [`Coalgebras`](categories.md#cat-coalgebras) | lazy-import binding | [`src/sage/categories/coalgebras.py:51`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L51) |
| [`HopfAlgebras`](categories.md#cat-hopfalgebras) | lazy-import binding | [`src/sage/categories/hopf_algebras.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L60) |
| [`LambdaBracketAlgebras`](categories.md#cat-lambdabracketalgebras) | lazy-import binding | [`src/sage/categories/lambda_bracket_algebras.py:273`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras.py#L273) |
| [`LieAlgebras`](categories.md#cat-liealgebras) | lazy-import binding | [`src/sage/categories/lie_algebras.py:175`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L175) |
| [`LieAlgebras`](categories.md#cat-liealgebras) | lazy-import binding | [`src/sage/categories/lie_algebras.py:171`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L171) |
| [`LieConformalAlgebras`](categories.md#cat-lieconformalalgebras) | lazy-import binding | [`src/sage/categories/lie_conformal_algebras.py:344`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras.py#L344) |
| [`MagmaticAlgebras`](categories.md#cat-magmaticalgebras) | nested category class | [`src/sage/categories/magmatic_algebras.py:119`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L119) |
| [`Modules`](categories.md#cat-modules) | lazy-import binding | [`src/sage/categories/modules.py:597`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L597) |
| [`Modules`](categories.md#cat-modules) | subcategory interface method | [`src/sage/categories/modules.py:492`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L492) |
| [`QuantumGroupRepresentations`](categories.md#cat-quantumgrouprepresentations) | nested category class | [`src/sage/categories/quantum_group_representations.py:63`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quantum_group_representations.py#L63) |
| [`SemisimpleAlgebras`](categories.md#cat-semisimplealgebras) | lazy-import binding | [`src/sage/categories/semisimple_algebras.py:113`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semisimple_algebras.py#L113) |
| [`SupercommutativeAlgebras`](categories.md#cat-supercommutativealgebras) | nested category class | [`src/sage/categories/supercommutative_algebras.py:61`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercommutative_algebras.py#L61) |
| [`UnitalAlgebras`](categories.md#cat-unitalalgebras) | nested category class | [`src/sage/categories/unital_algebras.py:252`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/unital_algebras.py#L252) |
| [`VectorSpaces`](categories.md#cat-vectorspaces) | nested category class | [`src/sage/categories/vector_spaces.py:182`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L182) |

### Classes the framework generates at 10.10 (5)

| class | module |
| --- | --- |
| `MagmaticAlgebras.WithBasis` | `magmatic_algebras` |
| `QuantumGroupRepresentations.WithBasis` | `quantum_group_representations` |
| `SupercommutativeAlgebras.WithBasis` | `supercommutative_algebras` |
| `UnitalAlgebras.WithBasis` | `unital_algebras` |
| `VectorSpaces.WithBasis` | `vector_spaces` |
