# Sage categories

## AbelianCategory {#cat-abeliancategory}

| field | value |
| --- | --- |
| module | `category_types` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/category_types.py:334`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L334) |
| loads at 10.10 | yes |

## AbelianVarieties {#cat-abelianvarieties}

| field | value |
| --- | --- |
| module | `schemes` |
| role | public named category class |
| implementation | Python class |
| bases | [`Schemes_over_base`](categories.md#cat-schemes-over-base) |
| source | [`src/sage/categories/schemes.py:205`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L205) |
| loads at 10.10 | yes |

### Local axiom paths

- `Homsets.Endset`

### Local construction paths

- `Homsets`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/schemes.py:267`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L267) |
| [`Endset`](axioms.md#ax-endset) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/schemes.py:288`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L288) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `AbelianVarieties.Homsets.Endset` | `schemes` | `Endset` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `AbelianVarieties.Homsets` | `schemes` | `Homsets` |

## AdditiveGroups {#cat-additivegroups}

| field | value |
| --- | --- |
| module | `additive_groups` |
| role | public named category class |
| implementation | Python class |
| defined by | AdditiveMonoids + axiom AdditiveInverse |
| direct defining axiom | [`AdditiveInverse`](axioms.md#ax-additiveinverse) |
| syntactic axiom chain | [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`AdditiveInverse`](axioms.md#ax-additiveinverse) |
| bound as | `AdditiveMonoids.AdditiveInverse` |
| bases | [`CategoryWithAxiom_singleton`](categories.md#cat-categorywithaxiom-singleton) |
| source | [`src/sage/categories/additive_groups.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L19) |
| loads at 10.10 | yes |

### Local axiom paths

- `AdditiveCommutative`
- `Finite`

### Local construction paths

- `Algebras`
- `Finite.Algebras`

### Declared features (4)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AdditiveCommutative`](axioms.md#ax-additivecommutative) | axiom | lazy-import binding | `sage.categories.commutative_additive_groups.CommutativeAdditiveGroups` | [`src/sage/categories/additive_groups.py:69`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L69) |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_groups.py:58`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L58) |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/additive_groups.py:62`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L62) |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_groups.py:63`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L63) |

### Axiom-generated classes at 10.10 (3)

| class | module | axiom |
| --- | --- | --- |
| `AdditiveGroups` | `additive_groups` | `(framework base)` |
| `AdditiveGroups.Finite` | `additive_groups` | `Finite` |
| `AdditiveGroups_with_category` | `additive_groups` | `(framework base)` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `AdditiveGroups.Algebras` | `additive_groups` | `Algebras` |
| `AdditiveGroups.Finite.Algebras` | `additive_groups` | `Algebras` |

## AdditiveMagmas {#cat-additivemagmas}

| field | value |
| --- | --- |
| module | `additive_magmas` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/additive_magmas.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L25) |
| loads at 10.10 | yes |

### Local axiom paths

- `AdditiveAssociative`
- `AdditiveCommutative`
- `AdditiveUnital`
- `AdditiveUnital.AdditiveInverse`

### Local construction paths

- `Algebras`
- `CartesianProducts`
- `Homsets`
- `AdditiveCommutative.Algebras`
- `AdditiveCommutative.CartesianProducts`
- `AdditiveUnital.Algebras`
- `AdditiveUnital.CartesianProducts`
- `AdditiveUnital.Homsets`
- `AdditiveUnital.WithRealizations`
- `AdditiveUnital.AdditiveInverse.CartesianProducts`

### Declared features (18)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AdditiveAssociative`](axioms.md#ax-additiveassociative) | axiom | lazy-import binding | `sage.categories.additive_semigroups.AdditiveSemigroups` | [`src/sage/categories/additive_magmas.py:167`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L167) |
| [`AdditiveAssociative`](axioms.md#ax-additiveassociative) | axiom | subcategory interface method | `_with_axiom(AdditiveAssociative)` | [`src/sage/categories/additive_magmas.py:78`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L78) |
| [`AdditiveCommutative`](axioms.md#ax-additivecommutative) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/additive_magmas.py:563`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L563) |
| [`AdditiveCommutative`](axioms.md#ax-additivecommutative) | axiom | subcategory interface method | `_with_axiom(AdditiveCommutative)` | [`src/sage/categories/additive_magmas.py:104`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L104) |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_magmas.py:580`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L580) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/additive_magmas.py:564`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L564) |
| [`AdditiveUnital`](axioms.md#ax-additiveunital) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/additive_magmas.py:599`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L599) |
| [`AdditiveUnital`](axioms.md#ax-additiveunital) | axiom | subcategory interface method | `_with_axiom(AdditiveUnital)` | [`src/sage/categories/additive_magmas.py:134`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L134) |
| [`AdditiveInverse`](axioms.md#ax-additiveinverse) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/additive_magmas.py:898`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L898) |
| [`AdditiveInverse`](axioms.md#ax-additiveinverse) | axiom | subcategory interface method | `_with_axiom(AdditiveInverse)` | [`src/sage/categories/additive_magmas.py:621`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L621) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/additive_magmas.py:899`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L899) |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_magmas.py:965`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L965) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/additive_magmas.py:936`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L936) |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/additive_magmas.py:857`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L857) |
| [`WithRealizations`](constructions.md#con-withrealizations) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/additive_magmas.py:1008`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L1008) |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_magmas.py:492`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L492) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/additive_magmas.py:452`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L452) |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/additive_magmas.py:438`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L438) |

### Axiom-generated classes at 10.10 (6)

| class | module | axiom |
| --- | --- | --- |
| `AdditiveMagmas.AdditiveCommutative` | `additive_magmas` | `AdditiveCommutative` |
| `AdditiveMagmas.AdditiveCommutative_with_category` | `additive_magmas` | `AdditiveCommutative_with_category` |
| `AdditiveMagmas.AdditiveUnital` | `additive_magmas` | `AdditiveUnital` |
| `AdditiveMagmas.AdditiveUnital.AdditiveInverse` | `additive_magmas` | `AdditiveInverse` |
| `AdditiveMagmas.AdditiveUnital.AdditiveInverse_with_category` | `additive_magmas` | `AdditiveInverse_with_category` |
| `AdditiveMagmas.AdditiveUnital_with_category` | `additive_magmas` | `AdditiveUnital_with_category` |

### Construction-generated classes at 10.10 (10)

| class | module | construction |
| --- | --- | --- |
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

## AdditiveMonoids {#cat-additivemonoids}

| field | value |
| --- | --- |
| module | `additive_monoids` |
| role | public named category class |
| implementation | Python class |
| defined by | AdditiveSemigroups + axiom AdditiveUnital |
| direct defining axiom | [`AdditiveUnital`](axioms.md#ax-additiveunital) |
| syntactic axiom chain | [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveUnital`](axioms.md#ax-additiveunital) |
| bound as | `AdditiveSemigroups.AdditiveUnital` |
| bases | [`CategoryWithAxiom_singleton`](categories.md#cat-categorywithaxiom-singleton) |
| source | [`src/sage/categories/additive_monoids.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L17) |
| loads at 10.10 | yes |

### Local axiom paths

- `AdditiveCommutative`
- `AdditiveInverse`

### Local construction paths

- `Homsets`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AdditiveCommutative`](axioms.md#ax-additivecommutative) | axiom | lazy-import binding | `sage.categories.commutative_additive_monoids.CommutativeAdditiveMonoids` | [`src/sage/categories/additive_monoids.py:47`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L47) |
| [`AdditiveInverse`](axioms.md#ax-additiveinverse) | axiom | lazy-import binding | `sage.categories.additive_groups.AdditiveGroups` | [`src/sage/categories/additive_monoids.py:48`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L48) |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/additive_monoids.py:89`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L89) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `AdditiveMonoids` | `additive_monoids` | `(framework base)` |
| `AdditiveMonoids_with_category` | `additive_monoids` | `(framework base)` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `AdditiveMonoids.Homsets` | `additive_monoids` | `Homsets` |

## AdditiveSemigroups {#cat-additivesemigroups}

| field | value |
| --- | --- |
| module | `additive_semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | AdditiveMagmas + axiom AdditiveAssociative |
| direct defining axiom | [`AdditiveAssociative`](axioms.md#ax-additiveassociative) |
| syntactic axiom chain | [`AdditiveAssociative`](axioms.md#ax-additiveassociative) |
| bound as | `AdditiveMagmas.AdditiveAssociative` |
| bases | [`CategoryWithAxiom_singleton`](categories.md#cat-categorywithaxiom-singleton) |
| source | [`src/sage/categories/additive_semigroups.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L20) |
| loads at 10.10 | yes |

### Local axiom paths

- `AdditiveCommutative`
- `AdditiveUnital`

### Local construction paths

- `Algebras`
- `CartesianProducts`
- `Homsets`

### Declared features (5)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AdditiveCommutative`](axioms.md#ax-additivecommutative) | axiom | lazy-import binding | `sage.categories.commutative_additive_semigroups.CommutativeAdditiveSemigroups` | [`src/sage/categories/additive_semigroups.py:53`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L53) |
| [`AdditiveUnital`](axioms.md#ax-additiveunital) | axiom | lazy-import binding | `sage.categories.additive_monoids.AdditiveMonoids` | [`src/sage/categories/additive_semigroups.py:54`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L54) |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_semigroups.py:123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L123) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/additive_semigroups.py:105`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L105) |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/additive_semigroups.py:88`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L88) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `AdditiveSemigroups` | `additive_semigroups` | `(framework base)` |
| `AdditiveSemigroups_with_category` | `additive_semigroups` | `(framework base)` |

### Construction-generated classes at 10.10 (3)

| class | module | construction |
| --- | --- | --- |
| `AdditiveSemigroups.Algebras` | `additive_semigroups` | `Algebras` |
| `AdditiveSemigroups.CartesianProducts` | `additive_semigroups` | `CartesianProducts` |
| `AdditiveSemigroups.Homsets` | `additive_semigroups` | `Homsets` |

## AffineWeylGroups {#cat-affineweylgroups}

| field | value |
| --- | --- |
| module | `affine_weyl_groups` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/affine_weyl_groups.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/affine_weyl_groups.py#L17) |
| loads at 10.10 | yes |

## AlgebraIdeals {#cat-algebraideals}

| field | value |
| --- | --- |
| module | `algebra_ideals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_ideal`](categories.md#cat-category-ideal) |
| source | [`src/sage/categories/algebra_ideals.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebra_ideals.py#L19) |
| loads at 10.10 | yes |

## AlgebraModules {#cat-algebramodules}

| field | value |
| --- | --- |
| module | `algebra_modules` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_module`](categories.md#cat-category-module) |
| source | [`src/sage/categories/algebra_modules.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebra_modules.py#L19) |
| loads at 10.10 | yes |

## Algebras {#cat-algebras}

| field | value |
| --- | --- |
| module | `algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | AssociativeAlgebras + axiom Unital |
| direct defining axiom | [`Unital`](axioms.md#ax-unital) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`Unital`](axioms.md#ax-unital) |
| bound as | `AssociativeAlgebras.Unital` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/algebras.py:29`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L29) |
| loads at 10.10 | yes |

### Local axiom paths

- `Commutative`
- `Supercommutative`
- `WithBasis`

### Local construction paths

- `CartesianProducts`
- `DualObjects`
- `Filtered`
- `Graded`
- `Quotients`
- `Super`
- `TensorProducts`

### Other local category paths

- `Semisimple`

### Declared features (12)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/algebras.py:273`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L273) |
| [`Commutative`](axioms.md#ax-commutative) | axiom | lazy-import binding | `sage.categories.commutative_algebras.CommutativeAlgebras` | [`src/sage/categories/algebras.py:129`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L129) |
| [`DualObjects`](constructions.md#con-dualobjects) | functorial construction | nested category class | `DualObjectsCategory` | [`src/sage/categories/algebras.py:325`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L325) |
| [`Filtered`](constructions.md#con-filtered) | functorial construction | lazy-import binding | `sage.categories.filtered_algebras.FilteredAlgebras` | [`src/sage/categories/algebras.py:131`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L131) |
| [`Graded`](constructions.md#con-graded) | functorial construction | lazy-import binding | `sage.categories.graded_algebras.GradedAlgebras` | [`src/sage/categories/algebras.py:133`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L133) |
| [`Quotients`](constructions.md#con-quotients) | functorial construction | nested category class | `QuotientsCategory` | [`src/sage/categories/algebras.py:247`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L247) |
| `Semisimple` | derived category shorthand | subcategory interface method | `calls SemisimpleAlgebras()` | [`src/sage/categories/algebras.py:89`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L89) |
| `Semisimple` | other category | lazy-import binding | `sage.categories.semisimple_algebras.SemisimpleAlgebras` | [`src/sage/categories/algebras.py:141`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L141) |
| [`Super`](constructions.md#con-super) | functorial construction | lazy-import binding | `sage.categories.super_algebras.SuperAlgebras` | [`src/sage/categories/algebras.py:135`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L135) |
| [`Supercommutative`](axioms.md#ax-supercommutative) | axiom | subcategory interface method | `calls Super()` | [`src/sage/categories/algebras.py:109`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L109) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/algebras.py:300`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L300) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | lazy-import binding | `sage.categories.algebras_with_basis.AlgebrasWithBasis` | [`src/sage/categories/algebras.py:138`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L138) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `Algebras` | `algebras` | `(framework base)` |

### Construction-generated classes at 10.10 (4)

| class | module | construction |
| --- | --- | --- |
| `Algebras.CartesianProducts` | `algebras` | `CartesianProducts` |
| `Algebras.DualObjects` | `algebras` | `DualObjects` |
| `Algebras.Quotients` | `algebras` | `Quotients` |
| `Algebras.TensorProducts` | `algebras` | `TensorProducts` |

## AlgebrasCategory {#cat-algebrascategory}

| field | value |
| --- | --- |
| module | `algebra_functor` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`CovariantConstructionCategory`](categories.md#cat-covariantconstructioncategory), [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/algebra_functor.py:640`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebra_functor.py#L640) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `AlgebrasCategory` | `algebra_functor` | `(framework base)` |

## AlgebrasWithBasis {#cat-algebraswithbasis}

| field | value |
| --- | --- |
| module | `algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | Algebras + axiom WithBasis |
| direct defining axiom | [`WithBasis`](axioms.md#ax-withbasis) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`Unital`](axioms.md#ax-unital), [`WithBasis`](axioms.md#ax-withbasis) |
| bound as | `Algebras.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/algebras_with_basis.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L21) |
| loads at 10.10 | yes |

### Local axiom paths

- `FiniteDimensional`

### Local construction paths

- `CartesianProducts`
- `Filtered`
- `Graded`
- `Super`
- `TensorProducts`

### Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/algebras_with_basis.py:200`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L200) |
| [`Filtered`](constructions.md#con-filtered) | functorial construction | lazy-import binding | `sage.categories.filtered_algebras_with_basis.FilteredAlgebrasWithBasis` | [`src/sage/categories/algebras_with_basis.py:124`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L124) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | lazy-import binding | `sage.categories.finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis` | [`src/sage/categories/algebras_with_basis.py:125`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L125) |
| [`Graded`](constructions.md#con-graded) | functorial construction | lazy-import binding | `sage.categories.graded_algebras_with_basis.GradedAlgebrasWithBasis` | [`src/sage/categories/algebras_with_basis.py:126`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L126) |
| [`Super`](constructions.md#con-super) | functorial construction | lazy-import binding | `sage.categories.super_algebras_with_basis.SuperAlgebrasWithBasis` | [`src/sage/categories/algebras_with_basis.py:127`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L127) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/algebras_with_basis.py:283`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L283) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `AlgebrasWithBasis` | `algebras_with_basis` | `(framework base)` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `AlgebrasWithBasis.CartesianProducts` | `algebras_with_basis` | `CartesianProducts` |
| `AlgebrasWithBasis.TensorProducts` | `algebras_with_basis` | `TensorProducts` |

## AperiodicSemigroups {#cat-aperiodicsemigroups}

| field | value |
| --- | --- |
| module | `aperiodic_semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | Semigroups + axiom Aperiodic |
| direct defining axiom | [`Aperiodic`](axioms.md#ax-aperiodic) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`Aperiodic`](axioms.md#ax-aperiodic) |
| bound as | `Semigroups.Aperiodic` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/aperiodic_semigroups.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/aperiodic_semigroups.py#L18) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `AperiodicSemigroups` | `aperiodic_semigroups` | `(framework base)` |

## AssociativeAlgebras {#cat-associativealgebras}

| field | value |
| --- | --- |
| module | `associative_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | MagmaticAlgebras + axiom Associative |
| direct defining axiom | [`Associative`](axioms.md#ax-associative) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative) |
| bound as | `MagmaticAlgebras.Associative` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/associative_algebras.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/associative_algebras.py#L16) |
| loads at 10.10 | yes |

### Local axiom paths

- `Unital`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Unital`](axioms.md#ax-unital) | axiom | lazy-import binding | `sage.categories.algebras.Algebras` | [`src/sage/categories/associative_algebras.py:46`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/associative_algebras.py#L46) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `AssociativeAlgebras` | `associative_algebras` | `(framework base)` |

## Bars {#cat-bars}

| field | value |
| --- | --- |
| module | `category_with_axiom` |
| role | test-only category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/category_with_axiom.py:2707`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2707) |
| loads at 10.10 | yes |

## Bialgebras {#cat-bialgebras}

| field | value |
| --- | --- |
| module | `bialgebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/bialgebras.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/bialgebras.py#L20) |
| loads at 10.10 | yes |

### Local axiom paths

- `WithBasis`

### Local construction paths

- `Super`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Super`](constructions.md#con-super) | functorial construction | nested category class | `SuperModulesCategory` | [`src/sage/categories/bialgebras.py:97`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/bialgebras.py#L97) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | lazy-import binding | `sage.categories.bialgebras_with_basis.BialgebrasWithBasis` | [`src/sage/categories/bialgebras.py:100`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/bialgebras.py#L100) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `Bialgebras.Super` | `bialgebras` | `Super` |

## BialgebrasWithBasis {#cat-bialgebraswithbasis}

| field | value |
| --- | --- |
| module | `bialgebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | Bialgebras + axiom WithBasis |
| direct defining axiom | [`WithBasis`](axioms.md#ax-withbasis) |
| syntactic axiom chain | [`WithBasis`](axioms.md#ax-withbasis) |
| bound as | `Bialgebras.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/bialgebras_with_basis.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/bialgebras_with_basis.py#L16) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `BialgebrasWithBasis` | `bialgebras_with_basis` | `(framework base)` |

## Bimodules {#cat-bimodules}

| field | value |
| --- | --- |
| module | `bimodules` |
| role | public named category class |
| implementation | Python class |
| bases | [`CategoryWithParameters`](categories.md#cat-categorywithparameters) |
| source | [`src/sage/categories/bimodules.py:24`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/bimodules.py#L24) |
| loads at 10.10 | yes |

## Blahs {#cat-blahs}

| field | value |
| --- | --- |
| module | `category_with_axiom` |
| role | test-only category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/category_with_axiom.py:2600`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2600) |
| loads at 10.10 | yes |

### Local axiom paths

- `Blue`
- `Commutative`
- `Connected`
- `FiniteDimensional`
- `Flying`
- `Unital`
- `Unital.Blue`

### Declared features (12)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Blue`](axioms.md#ax-blue) | axiom | subcategory interface method | `_with_axiom(Blue)` | [`src/sage/categories/category_with_axiom.py:2630`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2630) |
| [`Commutative`](axioms.md#ax-commutative) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2635`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2635) |
| [`Commutative`](axioms.md#ax-commutative) | axiom | subcategory interface method | `_with_axiom(Commutative)` | [`src/sage/categories/category_with_axiom.py:2626`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2626) |
| [`Connected`](axioms.md#ax-connected) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2638`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2638) |
| [`Connected`](axioms.md#ax-connected) | axiom | subcategory interface method | `_with_axiom(Connected)` | [`src/sage/categories/category_with_axiom.py:2628`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2628) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2632`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2632) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | subcategory interface method | `_with_axiom(FiniteDimensional)` | [`src/sage/categories/category_with_axiom.py:2625`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2625) |
| [`Flying`](axioms.md#ax-flying) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2645`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2645) |
| [`Flying`](axioms.md#ax-flying) | axiom | subcategory interface method | `_with_axiom(Flying)` | [`src/sage/categories/category_with_axiom.py:2629`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2629) |
| [`Unital`](axioms.md#ax-unital) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2641`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2641) |
| [`Unital`](axioms.md#ax-unital) | axiom | subcategory interface method | `_with_axiom(Unital)` | [`src/sage/categories/category_with_axiom.py:2627`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2627) |
| [`Blue`](axioms.md#ax-blue) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2642`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2642) |

### Axiom-generated classes at 10.10 (6)

| class | module | axiom |
| --- | --- | --- |
| `Blahs.Commutative` | `category_with_axiom` | `Commutative` |
| `Blahs.Connected` | `category_with_axiom` | `Connected` |
| `Blahs.FiniteDimensional` | `category_with_axiom` | `FiniteDimensional` |
| `Blahs.Flying` | `category_with_axiom` | `Flying` |
| `Blahs.Unital` | `category_with_axiom` | `Unital` |
| `Blahs.Unital.Blue` | `category_with_axiom` | `Blue` |

## CWComplexes {#cat-cwcomplexes}

| field | value |
| --- | --- |
| module | `cw_complexes` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/cw_complexes.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L18) |
| loads at 10.10 | yes |

### Local axiom paths

- `Connected`
- `Finite`
- `FiniteDimensional`

### Declared features (5)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Connected`](axioms.md#ax-connected) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/cw_complexes.py:105`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L105) |
| [`Connected`](axioms.md#ax-connected) | axiom | subcategory interface method | `_with_axiom(Connected)` | [`src/sage/categories/cw_complexes.py:65`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L65) |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/cw_complexes.py:115`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L115) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/cw_complexes.py:110`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L110) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | subcategory interface method | `_with_axiom(FiniteDimensional)` | [`src/sage/categories/cw_complexes.py:84`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L84) |

### Axiom-generated classes at 10.10 (3)

| class | module | axiom |
| --- | --- | --- |
| `CWComplexes.Connected` | `cw_complexes` | `Connected` |
| `CWComplexes.Finite` | `cw_complexes` | `Finite` |
| `CWComplexes.FiniteDimensional` | `cw_complexes` | `FiniteDimensional` |

## CartesianProductsCategory {#cat-cartesianproductscategory}

| field | value |
| --- | --- |
| module | `cartesian_product` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`CovariantConstructionCategory`](categories.md#cat-covariantconstructioncategory) |
| source | [`src/sage/categories/cartesian_product.py:225`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cartesian_product.py#L225) |
| loads at 10.10 | yes |

### Local construction paths

- `CartesianProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | category method | — | [`src/sage/categories/cartesian_product.py:252`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cartesian_product.py#L252) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `CartesianProductsCategory` | `cartesian_product` | `(framework base)` |

## Category {#cat-category}

| field | value |
| --- | --- |
| module | `category` |
| role | framework/helper category class |
| implementation | Python class |
| bases | `UniqueRepresentation`, `SageObject` |
| source | [`src/sage/categories/category.py:131`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category.py#L131) |
| loads at 10.10 | no |

### Local construction paths

- `Realizations`
- `WithRealizations`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Realizations`](constructions.md#con-realizations) | functorial construction | module-level binding | `Realizations` | [`src/sage/categories/realizations.py:107`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/realizations.py#L107) |
| [`WithRealizations`](constructions.md#con-withrealizations) | functorial construction | module-level binding | `WithRealizations` | [`src/sage/categories/with_realizations.py:284`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/with_realizations.py#L284) |

## CategoryWithAxiom {#cat-categorywithaxiom}

| field | value |
| --- | --- |
| module | `category_with_axiom` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/category_with_axiom.py:1864`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1864) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `CategoryWithAxiom` | `category_with_axiom` | `(framework base)` |

## CategoryWithAxiom_over_base_ring {#cat-categorywithaxiom-over-base-ring}

| field | value |
| --- | --- |
| module | `category_with_axiom` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom), [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/category_with_axiom.py:2506`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2506) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `CategoryWithAxiom_over_base_ring` | `category_with_axiom` | `(framework base)` |

## CategoryWithAxiom_singleton {#cat-categorywithaxiom-singleton}

| field | value |
| --- | --- |
| module | `category_with_axiom` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton), [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/category_with_axiom.py:2530`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2530) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `CategoryWithAxiom_singleton` | `category_with_axiom` | `(framework base)` |

## CategoryWithParameters {#cat-categorywithparameters}

| field | value |
| --- | --- |
| module | `category` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/category.py:2691`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category.py#L2691) |
| loads at 10.10 | yes |

## Category_ideal {#cat-category-ideal}

| field | value |
| --- | --- |
| module | `category_types` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`Category_in_ambient`](categories.md#cat-category-in-ambient) |
| source | [`src/sage/categories/category_types.py:579`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L579) |
| loads at 10.10 | yes |

## Category_in_ambient {#cat-category-in-ambient}

| field | value |
| --- | --- |
| module | `category_types` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/category_types.py:534`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L534) |
| loads at 10.10 | yes |

## Category_module {#cat-category-module}

| field | value |
| --- | --- |
| module | `category_types` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`AbelianCategory`](categories.md#cat-abeliancategory), [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/category_types.py:575`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L575) |
| loads at 10.10 | yes |

## Category_over_base {#cat-category-over-base}

| field | value |
| --- | --- |
| module | `category_types` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`CategoryWithParameters`](categories.md#cat-categorywithparameters) |
| source | [`src/sage/categories/category_types.py:147`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L147) |
| loads at 10.10 | yes |

## Category_over_base_ring {#cat-category-over-base-ring}

| field | value |
| --- | --- |
| module | `category_types` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`Category_over_base`](categories.md#cat-category-over-base) |
| source | [`src/sage/categories/category_types.py:347`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L347) |
| loads at 10.10 | yes |

## Category_realization_of_parent {#cat-category-realization-of-parent}

| field | value |
| --- | --- |
| module | `realizations` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`Category_over_base`](categories.md#cat-category-over-base), `BindableClass` |
| source | [`src/sage/categories/realizations.py:110`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/realizations.py#L110) |
| loads at 10.10 | yes |

## Category_singleton {#cat-category-singleton}

| field | value |
| --- | --- |
| module | `category_singleton` |
| role | framework/helper category class |
| implementation | Cython class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/category_singleton.pyx:83`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_singleton.pyx#L83) |
| loads at 10.10 | yes |
| notes | Technical singleton-category base class defined in category_singleton.pyx. |

## ChainComplexes {#cat-chaincomplexes}

| field | value |
| --- | --- |
| module | `chain_complexes` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_module`](categories.md#cat-category-module) |
| source | [`src/sage/categories/chain_complexes.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/chain_complexes.py#L25) |
| loads at 10.10 | yes |

## ClassicalCrystals {#cat-classicalcrystals}

| field | value |
| --- | --- |
| module | `classical_crystals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/classical_crystals.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/classical_crystals.py#L21) |
| loads at 10.10 | yes |

### Local construction paths

- `TensorProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/classical_crystals.py:473`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/classical_crystals.py#L473) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `ClassicalCrystals.TensorProducts` | `classical_crystals` | `TensorProducts` |

## Coalgebras {#cat-coalgebras}

| field | value |
| --- | --- |
| module | `coalgebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/coalgebras.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L27) |
| loads at 10.10 | yes |

### Local axiom paths

- `Cocommutative`
- `WithBasis`
- `Super.Supercocommutative`

### Local construction paths

- `DualObjects`
- `Filtered`
- `Graded`
- `Realizations`
- `Super`
- `TensorProducts`
- `WithRealizations`

### Declared features (12)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Cocommutative`](axioms.md#ax-cocommutative) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/coalgebras.py:180`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L180) |
| [`Cocommutative`](axioms.md#ax-cocommutative) | axiom | subcategory interface method | `_with_axiom(Cocommutative)` | [`src/sage/categories/coalgebras.py:150`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L150) |
| [`DualObjects`](constructions.md#con-dualobjects) | functorial construction | nested category class | `DualObjectsCategory` | [`src/sage/categories/coalgebras.py:210`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L210) |
| [`Filtered`](constructions.md#con-filtered) | functorial construction | nested category class | `FilteredModulesCategory` | [`src/sage/categories/coalgebras.py:288`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L288) |
| [`Graded`](constructions.md#con-graded) | functorial construction | lazy-import binding | `sage.categories.graded_coalgebras.GradedCoalgebras` | [`src/sage/categories/coalgebras.py:52`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L52) |
| [`Realizations`](constructions.md#con-realizations) | functorial construction | nested category class | `RealizationsCategory` | [`src/sage/categories/coalgebras.py:343`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L343) |
| [`Super`](constructions.md#con-super) | functorial construction | nested category class | `SuperModulesCategory` | [`src/sage/categories/coalgebras.py:236`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L236) |
| [`Supercocommutative`](axioms.md#ax-supercocommutative) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/coalgebras.py:283`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L283) |
| [`Supercocommutative`](axioms.md#ax-supercocommutative) | axiom | subcategory interface method | `_with_axiom(Supercocommutative)` | [`src/sage/categories/coalgebras.py:262`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L262) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/coalgebras.py:185`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L185) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | lazy-import binding | `sage.categories.coalgebras_with_basis.CoalgebrasWithBasis` | [`src/sage/categories/coalgebras.py:51`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L51) |
| [`WithRealizations`](constructions.md#con-withrealizations) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/coalgebras.py:293`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L293) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Coalgebras.Cocommutative` | `coalgebras` | `Cocommutative` |
| `Coalgebras.Super.Supercocommutative` | `coalgebras` | `Supercocommutative` |

### Construction-generated classes at 10.10 (6)

| class | module | construction |
| --- | --- | --- |
| `Coalgebras.DualObjects` | `coalgebras` | `DualObjects` |
| `Coalgebras.Filtered` | `coalgebras` | `Filtered` |
| `Coalgebras.Realizations` | `coalgebras` | `Realizations` |
| `Coalgebras.Super` | `coalgebras` | `Super` |
| `Coalgebras.TensorProducts` | `coalgebras` | `TensorProducts` |
| `Coalgebras.WithRealizations` | `coalgebras` | `WithRealizations` |

## CoalgebrasWithBasis {#cat-coalgebraswithbasis}

| field | value |
| --- | --- |
| module | `coalgebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | Coalgebras + axiom WithBasis |
| direct defining axiom | [`WithBasis`](axioms.md#ax-withbasis) |
| syntactic axiom chain | [`WithBasis`](axioms.md#ax-withbasis) |
| bound as | `Coalgebras.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/coalgebras_with_basis.py:23`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras_with_basis.py#L23) |
| loads at 10.10 | yes |

### Local construction paths

- `Filtered`
- `Graded`
- `Super`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Filtered`](constructions.md#con-filtered) | functorial construction | nested category class | `FilteredModulesCategory` | [`src/sage/categories/coalgebras_with_basis.py:42`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras_with_basis.py#L42) |
| [`Graded`](constructions.md#con-graded) | functorial construction | lazy-import binding | `sage.categories.graded_coalgebras_with_basis.GradedCoalgebrasWithBasis` | [`src/sage/categories/coalgebras_with_basis.py:39`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras_with_basis.py#L39) |
| [`Super`](constructions.md#con-super) | functorial construction | nested category class | `SuperModulesCategory` | [`src/sage/categories/coalgebras_with_basis.py:220`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras_with_basis.py#L220) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `CoalgebrasWithBasis` | `coalgebras_with_basis` | `(framework base)` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `CoalgebrasWithBasis.Filtered` | `coalgebras_with_basis` | `Filtered` |
| `CoalgebrasWithBasis.Super` | `coalgebras_with_basis` | `Super` |

## CommutativeAdditiveGroups {#cat-commutativeadditivegroups}

| field | value |
| --- | --- |
| module | `commutative_additive_groups` |
| role | public named category class |
| implementation | Python class |
| defined by | AdditiveGroups + axiom AdditiveCommutative |
| direct defining axiom | [`AdditiveCommutative`](axioms.md#ax-additivecommutative) |
| syntactic axiom chain | [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`AdditiveInverse`](axioms.md#ax-additiveinverse), [`AdditiveCommutative`](axioms.md#ax-additivecommutative) |
| bound as | `AdditiveGroups.AdditiveCommutative` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom), [`AbelianCategory`](categories.md#cat-abeliancategory) |
| source | [`src/sage/categories/commutative_additive_groups.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_additive_groups.py#L18) |
| loads at 10.10 | yes |

### Local construction paths

- `Algebras`
- `CartesianProducts`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/commutative_additive_groups.py:98`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_additive_groups.py#L98) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/commutative_additive_groups.py:61`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_additive_groups.py#L61) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `CommutativeAdditiveGroups` | `commutative_additive_groups` | `(framework base)` |
| `CommutativeAdditiveGroups_with_category` | `commutative_additive_groups` | `(framework base)` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `CommutativeAdditiveGroups.Algebras` | `commutative_additive_groups` | `Algebras` |
| `CommutativeAdditiveGroups.CartesianProducts` | `commutative_additive_groups` | `CartesianProducts` |

## CommutativeAdditiveMonoids {#cat-commutativeadditivemonoids}

| field | value |
| --- | --- |
| module | `commutative_additive_monoids` |
| role | public named category class |
| implementation | Python class |
| defined by | AdditiveMonoids + axiom AdditiveCommutative |
| direct defining axiom | [`AdditiveCommutative`](axioms.md#ax-additivecommutative) |
| syntactic axiom chain | [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`AdditiveCommutative`](axioms.md#ax-additivecommutative) |
| bound as | `AdditiveMonoids.AdditiveCommutative` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/commutative_additive_monoids.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_additive_monoids.py#L16) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `CommutativeAdditiveMonoids` | `commutative_additive_monoids` | `(framework base)` |
| `CommutativeAdditiveMonoids_with_category` | `commutative_additive_monoids` | `(framework base)` |

## CommutativeAdditiveSemigroups {#cat-commutativeadditivesemigroups}

| field | value |
| --- | --- |
| module | `commutative_additive_semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | AdditiveSemigroups + axiom AdditiveCommutative |
| direct defining axiom | [`AdditiveCommutative`](axioms.md#ax-additivecommutative) |
| syntactic axiom chain | [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveCommutative`](axioms.md#ax-additivecommutative) |
| bound as | `AdditiveSemigroups.AdditiveCommutative` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/commutative_additive_semigroups.py:15`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_additive_semigroups.py#L15) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `CommutativeAdditiveSemigroups` | `commutative_additive_semigroups` | `(framework base)` |
| `CommutativeAdditiveSemigroups_with_category` | `commutative_additive_semigroups` | `(framework base)` |

## CommutativeAlgebraIdeals {#cat-commutativealgebraideals}

| field | value |
| --- | --- |
| module | `commutative_algebra_ideals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_ideal`](categories.md#cat-category-ideal) |
| source | [`src/sage/categories/commutative_algebra_ideals.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_algebra_ideals.py#L19) |
| loads at 10.10 | yes |

## CommutativeAlgebras {#cat-commutativealgebras}

| field | value |
| --- | --- |
| module | `commutative_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | Algebras + axiom Commutative |
| direct defining axiom | [`Commutative`](axioms.md#ax-commutative) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`Unital`](axioms.md#ax-unital), [`Commutative`](axioms.md#ax-commutative) |
| bound as | `Algebras.Commutative` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/commutative_algebras.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_algebras.py#L20) |
| loads at 10.10 | yes |

### Local construction paths

- `TensorProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/commutative_algebras.py:66`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_algebras.py#L66) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `CommutativeAlgebras` | `commutative_algebras` | `(framework base)` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `CommutativeAlgebras.TensorProducts` | `commutative_algebras` | `TensorProducts` |

## CommutativeRingIdeals {#cat-commutativeringideals}

| field | value |
| --- | --- |
| module | `commutative_ring_ideals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_ideal`](categories.md#cat-category-ideal) |
| source | [`src/sage/categories/commutative_ring_ideals.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_ring_ideals.py#L18) |
| loads at 10.10 | yes |

## CommutativeRings {#cat-commutativerings}

| field | value |
| --- | --- |
| module | `commutative_rings` |
| role | public named category class |
| implementation | Python class |
| defined by | Rings + axiom Commutative |
| direct defining axiom | [`Commutative`](axioms.md#ax-commutative) |
| syntactic axiom chain | [`Distributive`](axioms.md#ax-distributive), [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveCommutative`](axioms.md#ax-additivecommutative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`Associative`](axioms.md#ax-associative), [`AdditiveInverse`](axioms.md#ax-additiveinverse), [`Unital`](axioms.md#ax-unital), [`Commutative`](axioms.md#ax-commutative) |
| bound as | `Rings.Commutative` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/commutative_rings.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_rings.py#L20) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`

### Local construction paths

- `CartesianProducts`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/commutative_rings.py:992`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_rings.py#L992) |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/commutative_rings.py:830`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/commutative_rings.py#L830) |

### Axiom-generated classes at 10.10 (3)

| class | module | axiom |
| --- | --- | --- |
| `CommutativeRings` | `commutative_rings` | `(framework base)` |
| `CommutativeRings.Finite` | `commutative_rings` | `Finite` |
| `CommutativeRings_with_category` | `commutative_rings` | `(framework base)` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `CommutativeRings.CartesianProducts` | `commutative_rings` | `CartesianProducts` |

## CompleteDiscreteValuationFields {#cat-completediscretevaluationfields}

| field | value |
| --- | --- |
| module | `complete_discrete_valuation` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/complete_discrete_valuation.py:175`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complete_discrete_valuation.py#L175) |
| loads at 10.10 | yes |

## CompleteDiscreteValuationRings {#cat-completediscretevaluationrings}

| field | value |
| --- | --- |
| module | `complete_discrete_valuation` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/complete_discrete_valuation.py:24`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complete_discrete_valuation.py#L24) |
| loads at 10.10 | yes |

## ComplexManifolds {#cat-complexmanifolds}

| field | value |
| --- | --- |
| module | `manifolds` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/manifolds.py:335`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L335) |
| loads at 10.10 | yes |

## ComplexReflectionGroups {#cat-complexreflectiongroups}

| field | value |
| --- | --- |
| module | `complex_reflection_groups` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/complex_reflection_groups.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complex_reflection_groups.py#L20) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_complex_reflection_groups.FiniteComplexReflectionGroups` | [`src/sage/categories/complex_reflection_groups.py:143`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complex_reflection_groups.py#L143) |

## ComplexReflectionOrGeneralizedCoxeterGroups {#cat-complexreflectionorgeneralizedcoxetergroups}

| field | value |
| --- | --- |
| module | `complex_reflection_or_generalized_coxeter_groups` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/complex_reflection_or_generalized_coxeter_groups.py:23`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complex_reflection_or_generalized_coxeter_groups.py#L23) |
| loads at 10.10 | yes |

### Local axiom paths

- `Irreducible`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Irreducible`](axioms.md#ax-irreducible) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/complex_reflection_or_generalized_coxeter_groups.py:1233`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complex_reflection_or_generalized_coxeter_groups.py#L1233) |
| [`Irreducible`](axioms.md#ax-irreducible) | axiom | subcategory interface method | `_with_axiom(Irreducible)` | [`src/sage/categories/complex_reflection_or_generalized_coxeter_groups.py:116`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/complex_reflection_or_generalized_coxeter_groups.py#L116) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `ComplexReflectionOrGeneralizedCoxeterGroups.Irreducible` | `complex_reflection_or_generalized_coxeter_groups` | `Irreducible` |

## CovariantConstructionCategory {#cat-covariantconstructioncategory}

| field | value |
| --- | --- |
| module | `covariant_functorial_construction` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`FunctorialConstructionCategory`](categories.md#cat-functorialconstructioncategory) |
| source | [`src/sage/categories/covariant_functorial_construction.py:513`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/covariant_functorial_construction.py#L513) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `CovariantConstructionCategory` | `covariant_functorial_construction` | `(framework base)` |

## CoxeterGroupAlgebras {#cat-coxetergroupalgebras}

| field | value |
| --- | --- |
| module | `coxeter_group_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | CoxeterGroups.Algebras() |
| defining construction | [`Algebras`](constructions.md#con-algebras) |
| bound as | `CoxeterGroups.Algebras` |
| bases | [`AlgebrasCategory`](categories.md#cat-algebrascategory) |
| source | [`src/sage/categories/coxeter_group_algebras.py:10`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coxeter_group_algebras.py#L10) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `CoxeterGroupAlgebras` | `coxeter_group_algebras` | `(framework base)` |

## CoxeterGroups {#cat-coxetergroups}

| field | value |
| --- | --- |
| module | `coxeter_groups` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/coxeter_groups.py:30`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coxeter_groups.py#L30) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`

### Local construction paths

- `Algebras`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | lazy-import binding | `sage.categories.coxeter_group_algebras.CoxeterGroupAlgebras` | [`src/sage/categories/coxeter_groups.py:130`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coxeter_groups.py#L130) |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_coxeter_groups.FiniteCoxeterGroups` | [`src/sage/categories/coxeter_groups.py:129`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coxeter_groups.py#L129) |

## Crystals {#cat-crystals}

| field | value |
| --- | --- |
| module | `crystals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/crystals.py:35`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L35) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`

### Local construction paths

- `TensorProducts`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_crystals.FiniteCrystals` | [`src/sage/categories/crystals.py:1822`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L1822) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/crystals.py:1808`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L1808) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | subcategory interface method | `TensorProductsCategory.category_of(...)` | [`src/sage/categories/crystals.py:1791`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L1791) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `Crystals.TensorProducts` | `crystals` | `TensorProducts` |

## DedekindDomains {#cat-dedekinddomains}

| field | value |
| --- | --- |
| module | `dedekind_domains` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/dedekind_domains.py:14`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/dedekind_domains.py#L14) |
| loads at 10.10 | yes |

## DiscreteValuationFields {#cat-discretevaluationfields}

| field | value |
| --- | --- |
| module | `discrete_valuation` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/discrete_valuation.py:222`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/discrete_valuation.py#L222) |
| loads at 10.10 | yes |

## DiscreteValuationRings {#cat-discretevaluationrings}

| field | value |
| --- | --- |
| module | `discrete_valuation` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/discrete_valuation.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/discrete_valuation.py#L18) |
| loads at 10.10 | yes |

## DistributiveLattices {#cat-distributivelattices}

| field | value |
| --- | --- |
| module | `lattice_posets` |
| role | public named category class |
| implementation | Python class |
| defined by | LatticePosets.Trim + axiom ChainGraded |
| direct defining axiom | [`ChainGraded`](axioms.md#ax-chaingraded) |
| syntactic axiom chain | [`Trim`](axioms.md#ax-trim), [`ChainGraded`](axioms.md#ax-chaingraded) |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/lattice_posets.py:564`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L564) |
| loads at 10.10 | yes |
| notes | The public shorthand LatticePosets().Distributive() expands to Trim then ChainGraded; the implementation class is bound at LatticePosets.Trim.ChainGraded. |

### Local axiom paths

- `Finite`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:602`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L602) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `DistributiveLattices` | `lattice_posets` | `(framework base)` |
| `DistributiveLattices.Finite` | `lattice_posets` | `Finite` |

## DistributiveMagmasAndAdditiveMagmas {#cat-distributivemagmasandadditivemagmas}

| field | value |
| --- | --- |
| module | `distributive_magmas_and_additive_magmas` |
| role | public named category class |
| implementation | Python class |
| defined by | MagmasAndAdditiveMagmas + axiom Distributive |
| direct defining axiom | [`Distributive`](axioms.md#ax-distributive) |
| syntactic axiom chain | [`Distributive`](axioms.md#ax-distributive) |
| bound as | `MagmasAndAdditiveMagmas.Distributive` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L16) |
| loads at 10.10 | yes |

### Local axiom paths

- `AdditiveAssociative`
- `AdditiveAssociative.AdditiveCommutative`
- `AdditiveAssociative.AdditiveCommutative.AdditiveUnital`
- `AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative`
- `AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative.AdditiveInverse`
- `AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative.Unital`

### Local construction paths

- `CartesianProducts`

### Declared features (7)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AdditiveAssociative`](axioms.md#ax-additiveassociative) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:41`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L41) |
| [`AdditiveCommutative`](axioms.md#ax-additivecommutative) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:42`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L42) |
| [`AdditiveUnital`](axioms.md#ax-additiveunital) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:43`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L43) |
| [`Associative`](axioms.md#ax-associative) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:44`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L44) |
| [`AdditiveInverse`](axioms.md#ax-additiveinverse) | axiom | lazy-import binding | `sage.categories.rngs.Rngs` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:45`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L45) |
| [`Unital`](axioms.md#ax-unital) | axiom | lazy-import binding | `sage.categories.semirings.Semirings` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:46`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L46) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:84`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L84) |

### Axiom-generated classes at 10.10 (10)

| class | module | axiom |
| --- | --- | --- |
| `DistributiveMagmasAndAdditiveMagmas` | `distributive_magmas_and_additive_magmas` | `(framework base)` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative` | `distributive_magmas_and_additive_magmas` | `AdditiveAssociative` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative` | `distributive_magmas_and_additive_magmas` | `AdditiveCommutative` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital` | `distributive_magmas_and_additive_magmas` | `AdditiveUnital` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative` | `distributive_magmas_and_additive_magmas` | `Associative` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative_with_category` | `distributive_magmas_and_additive_magmas` | `Associative_with_category` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital_with_category` | `distributive_magmas_and_additive_magmas` | `AdditiveUnital_with_category` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative_with_category` | `distributive_magmas_and_additive_magmas` | `AdditiveCommutative_with_category` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative_with_category` | `distributive_magmas_and_additive_magmas` | `AdditiveAssociative_with_category` |
| `DistributiveMagmasAndAdditiveMagmas_with_category` | `distributive_magmas_and_additive_magmas` | `(framework base)` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `DistributiveMagmasAndAdditiveMagmas.CartesianProducts` | `distributive_magmas_and_additive_magmas` | `CartesianProducts` |

## DivisionRings {#cat-divisionrings}

| field | value |
| --- | --- |
| module | `division_rings` |
| role | public named category class |
| implementation | Python class |
| defined by | Rings + axiom Division |
| direct defining axiom | [`Division`](axioms.md#ax-division) |
| syntactic axiom chain | [`Distributive`](axioms.md#ax-distributive), [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveCommutative`](axioms.md#ax-additivecommutative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`Associative`](axioms.md#ax-associative), [`AdditiveInverse`](axioms.md#ax-additiveinverse), [`Unital`](axioms.md#ax-unital), [`Division`](axioms.md#ax-division) |
| bound as | `Rings.Division` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/division_rings.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/division_rings.py#L16) |
| loads at 10.10 | yes |

### Local axiom paths

- `Commutative`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Commutative`](axioms.md#ax-commutative) | axiom | lazy-import binding | `sage.categories.fields.Fields` | [`src/sage/categories/division_rings.py:63`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/division_rings.py#L63) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `DivisionRings` | `division_rings` | `(framework base)` |
| `DivisionRings_with_category` | `division_rings` | `(framework base)` |

## Domains {#cat-domains}

| field | value |
| --- | --- |
| module | `domains` |
| role | public named category class |
| implementation | Python class |
| defined by | Rings + axiom NoZeroDivisors |
| direct defining axiom | [`NoZeroDivisors`](axioms.md#ax-nozerodivisors) |
| syntactic axiom chain | [`Distributive`](axioms.md#ax-distributive), [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveCommutative`](axioms.md#ax-additivecommutative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`Associative`](axioms.md#ax-associative), [`AdditiveInverse`](axioms.md#ax-additiveinverse), [`Unital`](axioms.md#ax-unital), [`NoZeroDivisors`](axioms.md#ax-nozerodivisors) |
| bound as | `Rings.NoZeroDivisors` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/domains.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/domains.py#L17) |
| loads at 10.10 | yes |

### Local axiom paths

- `Commutative`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Commutative`](axioms.md#ax-commutative) | axiom | lazy-import binding | `sage.categories.integral_domains.IntegralDomains` | [`src/sage/categories/domains.py:49`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/domains.py#L49) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Domains` | `domains` | `(framework base)` |
| `Domains_with_category` | `domains` | `(framework base)` |

## DrinfeldModules {#cat-drinfeldmodules}

| field | value |
| --- | --- |
| module | `drinfeld_modules` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/drinfeld_modules.py:35`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/drinfeld_modules.py#L35) |
| loads at 10.10 | yes |

### Local construction paths

- `Homsets`

### Other local category paths

- `Endsets`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| `Endsets` | derived category shorthand | category method | `calls Homsets()` | [`src/sage/categories/drinfeld_modules.py:332`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/drinfeld_modules.py#L332) |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | category method | — | [`src/sage/categories/drinfeld_modules.py:313`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/drinfeld_modules.py#L313) |

## DualObjectsCategory {#cat-dualobjectscategory}

| field | value |
| --- | --- |
| module | `dual` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`CovariantConstructionCategory`](categories.md#cat-covariantconstructioncategory) |
| source | [`src/sage/categories/dual.py:29`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/dual.py#L29) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `DualObjectsCategory` | `dual` | `(framework base)` |

## DummyObjectsOverBaseRing {#cat-dummyobjectsoverbasering}

| field | value |
| --- | --- |
| module | `category_with_axiom` |
| role | test-only category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/category_with_axiom.py:2793`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2793) |
| loads at 10.10 | yes |

### Local axiom paths

- `Commutative`
- `FiniteDimensional`
- `Unital`
- `Commutative.Facade`
- `Commutative.Finite`
- `Commutative.FiniteDimensional`
- `FiniteDimensional.Finite`
- `FiniteDimensional.Unital`
- `FiniteDimensional.Unital.Commutative`

### Declared features (9)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Commutative`](axioms.md#ax-commutative) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/category_with_axiom.py:2824`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2824) |
| [`Facade`](axioms.md#ax-facade) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/category_with_axiom.py:2825`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2825) |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/category_with_axiom.py:2831`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2831) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/category_with_axiom.py:2828`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2828) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/category_with_axiom.py:2816`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2816) |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/category_with_axiom.py:2817`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2817) |
| [`Unital`](axioms.md#ax-unital) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/category_with_axiom.py:2820`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2820) |
| [`Commutative`](axioms.md#ax-commutative) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/category_with_axiom.py:2821`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2821) |
| [`Unital`](axioms.md#ax-unital) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/category_with_axiom.py:2834`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2834) |

### Axiom-generated classes at 10.10 (9)

| class | module | axiom |
| --- | --- | --- |
| `DummyObjectsOverBaseRing.Commutative` | `category_with_axiom` | `Commutative` |
| `DummyObjectsOverBaseRing.Commutative.Facade` | `category_with_axiom` | `Facade` |
| `DummyObjectsOverBaseRing.Commutative.Finite` | `category_with_axiom` | `Finite` |
| `DummyObjectsOverBaseRing.Commutative.FiniteDimensional` | `category_with_axiom` | `FiniteDimensional` |
| `DummyObjectsOverBaseRing.FiniteDimensional` | `category_with_axiom` | `FiniteDimensional` |
| `DummyObjectsOverBaseRing.FiniteDimensional.Finite` | `category_with_axiom` | `Finite` |
| `DummyObjectsOverBaseRing.FiniteDimensional.Unital` | `category_with_axiom` | `Unital` |
| `DummyObjectsOverBaseRing.FiniteDimensional.Unital.Commutative` | `category_with_axiom` | `Commutative` |
| `DummyObjectsOverBaseRing.Unital` | `category_with_axiom` | `Unital` |

## Elements {#cat-elements}

| field | value |
| --- | --- |
| module | `category_types` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/category_types.py:36`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_types.py#L36) |
| loads at 10.10 | yes |

## EnumeratedSets {#cat-enumeratedsets}

| field | value |
| --- | --- |
| module | `enumerated_sets` |
| role | public named category class |
| implementation | Python class |
| defined by | Sets + axiom Enumerated |
| direct defining axiom | [`Enumerated`](axioms.md#ax-enumerated) |
| syntactic axiom chain | [`Enumerated`](axioms.md#ax-enumerated) |
| bound as | `Sets.Enumerated` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/enumerated_sets.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L21) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`
- `Infinite`

### Local construction paths

- `CartesianProducts`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/enumerated_sets.py:1126`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L1126) |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_enumerated_sets.FiniteEnumeratedSets` | [`src/sage/categories/enumerated_sets.py:1123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L1123) |
| [`Infinite`](axioms.md#ax-infinite) | axiom | lazy-import binding | `sage.categories.infinite_enumerated_sets.InfiniteEnumeratedSets` | [`src/sage/categories/enumerated_sets.py:1124`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L1124) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `EnumeratedSets` | `enumerated_sets` | `(framework base)` |
| `EnumeratedSets_with_category` | `enumerated_sets` | `(framework base)` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `EnumeratedSets.CartesianProducts` | `enumerated_sets` | `CartesianProducts` |

## EuclideanDomains {#cat-euclideandomains}

| field | value |
| --- | --- |
| module | `euclidean_domains` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/euclidean_domains.py:26`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/euclidean_domains.py#L26) |
| loads at 10.10 | yes |

## FacadeSets {#cat-facadesets}

| field | value |
| --- | --- |
| module | `facade_sets` |
| role | public named category class |
| implementation | Python class |
| defined by | Sets + axiom Facade |
| direct defining axiom | [`Facade`](axioms.md#ax-facade) |
| syntactic axiom chain | [`Facade`](axioms.md#ax-facade) |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/facade_sets.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/facade_sets.py#L16) |
| loads at 10.10 | yes |
| notes | The base/axiom relation is inferred by Sage's documented category-name heuristic. Listed under Technical Categories in Sage's reference index, but callable as Sets().Facade(). |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FacadeSets` | `facade_sets` | `(framework base)` |

## Fields {#cat-fields}

| field | value |
| --- | --- |
| module | `fields` |
| role | public named category class |
| implementation | Python class |
| defined by | DivisionRings + axiom Commutative |
| direct defining axiom | [`Commutative`](axioms.md#ax-commutative) |
| syntactic axiom chain | [`Distributive`](axioms.md#ax-distributive), [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveCommutative`](axioms.md#ax-additivecommutative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`Associative`](axioms.md#ax-associative), [`AdditiveInverse`](axioms.md#ax-additiveinverse), [`Unital`](axioms.md#ax-unital), [`Division`](axioms.md#ax-division), [`Commutative`](axioms.md#ax-commutative) |
| bound as | `DivisionRings.Commutative` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/fields.py:26`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/fields.py#L26) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_fields.FiniteFields` | [`src/sage/categories/fields.py:192`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/fields.py#L192) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Fields` | `fields` | `(framework base)` |
| `Fields_with_category` | `fields` | `(framework base)` |

## FilteredAlgebras {#cat-filteredalgebras}

| field | value |
| --- | --- |
| module | `filtered_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | Algebras.Filtered() |
| defining construction | [`Filtered`](constructions.md#con-filtered) |
| bound as | `Algebras.Filtered` |
| bases | [`FilteredModulesCategory`](categories.md#cat-filteredmodulescategory) |
| source | [`src/sage/categories/filtered_algebras.py:15`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_algebras.py#L15) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `FilteredAlgebras` | `filtered_algebras` | `(framework base)` |

## FilteredAlgebrasWithBasis {#cat-filteredalgebraswithbasis}

| field | value |
| --- | --- |
| module | `filtered_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | AlgebrasWithBasis.Filtered() |
| defining construction | [`Filtered`](constructions.md#con-filtered) |
| bound as | `AlgebrasWithBasis.Filtered` |
| bases | [`FilteredModulesCategory`](categories.md#cat-filteredmodulescategory) |
| source | [`src/sage/categories/filtered_algebras_with_basis.py:22`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_algebras_with_basis.py#L22) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `FilteredAlgebrasWithBasis` | `filtered_algebras_with_basis` | `(framework base)` |

## FilteredHopfAlgebrasWithBasis {#cat-filteredhopfalgebraswithbasis}

| field | value |
| --- | --- |
| module | `filtered_hopf_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | HopfAlgebrasWithBasis.Filtered() |
| defining construction | [`Filtered`](constructions.md#con-filtered) |
| bound as | `HopfAlgebrasWithBasis.Filtered` |
| bases | [`FilteredModulesCategory`](categories.md#cat-filteredmodulescategory) |
| source | [`src/sage/categories/filtered_hopf_algebras_with_basis.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_hopf_algebras_with_basis.py#L18) |
| loads at 10.10 | yes |

### Local axiom paths

- `Connected`

### Local construction paths

- `WithRealizations`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Connected`](axioms.md#ax-connected) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/filtered_hopf_algebras_with_basis.py:68`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_hopf_algebras_with_basis.py#L68) |
| [`WithRealizations`](constructions.md#con-withrealizations) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/filtered_hopf_algebras_with_basis.py:49`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_hopf_algebras_with_basis.py#L49) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FilteredHopfAlgebrasWithBasis.Connected` | `filtered_hopf_algebras_with_basis` | `Connected` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `FilteredHopfAlgebrasWithBasis` | `filtered_hopf_algebras_with_basis` | `(framework base)` |
| `FilteredHopfAlgebrasWithBasis.WithRealizations` | `filtered_hopf_algebras_with_basis` | `WithRealizations` |

## FilteredModules {#cat-filteredmodules}

| field | value |
| --- | --- |
| module | `filtered_modules` |
| role | public named category class |
| implementation | Python class |
| defined by | Modules.Filtered() |
| defining construction | [`Filtered`](constructions.md#con-filtered) |
| bound as | `Modules.Filtered` |
| bases | [`FilteredModulesCategory`](categories.md#cat-filteredmodulescategory) |
| source | [`src/sage/categories/filtered_modules.py:118`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules.py#L118) |
| loads at 10.10 | yes |

### Local axiom paths

- `Connected`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Connected`](axioms.md#ax-connected) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/filtered_modules.py:207`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules.py#L207) |
| [`Connected`](axioms.md#ax-connected) | axiom | subcategory interface method | `_with_axiom(Connected)` | [`src/sage/categories/filtered_modules.py:181`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules.py#L181) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FilteredModules.Connected` | `filtered_modules` | `Connected` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `FilteredModules` | `filtered_modules` | `(framework base)` |

## FilteredModulesCategory {#cat-filteredmodulescategory}

| field | value |
| --- | --- |
| module | `filtered_modules` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`RegressiveCovariantConstructionCategory`](categories.md#cat-regressivecovariantconstructioncategory), [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/filtered_modules.py:37`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules.py#L37) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `FilteredModulesCategory` | `filtered_modules` | `(framework base)` |

## FilteredModulesWithBasis {#cat-filteredmoduleswithbasis}

| field | value |
| --- | --- |
| module | `filtered_modules_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | ModulesWithBasis.Filtered() |
| defining construction | [`Filtered`](constructions.md#con-filtered) |
| bound as | `ModulesWithBasis.Filtered` |
| bases | [`FilteredModulesCategory`](categories.md#cat-filteredmodulescategory) |
| source | [`src/sage/categories/filtered_modules_with_basis.py:38`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules_with_basis.py#L38) |
| loads at 10.10 | yes |

### Local axiom paths

- `FiniteDimensional`

### Local construction paths

- `Subobjects`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/filtered_modules_with_basis.py:1161`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules_with_basis.py#L1161) |
| [`Subobjects`](constructions.md#con-subobjects) | functorial construction | nested category class | `SubobjectsCategory` | [`src/sage/categories/filtered_modules_with_basis.py:1076`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules_with_basis.py#L1076) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FilteredModulesWithBasis.FiniteDimensional` | `filtered_modules_with_basis` | `FiniteDimensional` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `FilteredModulesWithBasis` | `filtered_modules_with_basis` | `(framework base)` |
| `FilteredModulesWithBasis.Subobjects` | `filtered_modules_with_basis` | `Subobjects` |

## FiniteComplexReflectionGroups {#cat-finitecomplexreflectiongroups}

| field | value |
| --- | --- |
| module | `finite_complex_reflection_groups` |
| role | public named category class |
| implementation | Python class |
| defined by | ComplexReflectionGroups + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Finite`](axioms.md#ax-finite) |
| bound as | `ComplexReflectionGroups.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_complex_reflection_groups.py:22`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_complex_reflection_groups.py#L22) |
| loads at 10.10 | yes |

### Local axiom paths

- `Irreducible`
- `WellGenerated`
- `WellGenerated.Irreducible`

### Declared features (4)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Irreducible`](axioms.md#ax-irreducible) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/finite_complex_reflection_groups.py:763`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_complex_reflection_groups.py#L763) |
| [`WellGenerated`](axioms.md#ax-wellgenerated) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/finite_complex_reflection_groups.py:1108`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_complex_reflection_groups.py#L1108) |
| [`WellGenerated`](axioms.md#ax-wellgenerated) | axiom | subcategory interface method | `_with_axiom(WellGenerated)` | [`src/sage/categories/finite_complex_reflection_groups.py:87`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_complex_reflection_groups.py#L87) |
| [`Irreducible`](axioms.md#ax-irreducible) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/finite_complex_reflection_groups.py:1237`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_complex_reflection_groups.py#L1237) |

### Axiom-generated classes at 10.10 (4)

| class | module | axiom |
| --- | --- | --- |
| `FiniteComplexReflectionGroups` | `finite_complex_reflection_groups` | `(framework base)` |
| `FiniteComplexReflectionGroups.Irreducible` | `finite_complex_reflection_groups` | `Irreducible` |
| `FiniteComplexReflectionGroups.WellGenerated` | `finite_complex_reflection_groups` | `WellGenerated` |
| `FiniteComplexReflectionGroups.WellGenerated.Irreducible` | `finite_complex_reflection_groups` | `Irreducible` |

## FiniteCoxeterGroups {#cat-finitecoxetergroups}

| field | value |
| --- | --- |
| module | `finite_coxeter_groups` |
| role | public named category class |
| implementation | Python class |
| defined by | CoxeterGroups + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Finite`](axioms.md#ax-finite) |
| bound as | `CoxeterGroups.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_coxeter_groups.py:22`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_coxeter_groups.py#L22) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FiniteCoxeterGroups` | `finite_coxeter_groups` | `(framework base)` |

## FiniteCrystals {#cat-finitecrystals}

| field | value |
| --- | --- |
| module | `finite_crystals` |
| role | public named category class |
| implementation | Python class |
| defined by | Crystals + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Finite`](axioms.md#ax-finite) |
| bound as | `Crystals.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_crystals.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_crystals.py#L18) |
| loads at 10.10 | yes |

### Local construction paths

- `TensorProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/finite_crystals.py:91`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_crystals.py#L91) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FiniteCrystals` | `finite_crystals` | `(framework base)` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `FiniteCrystals.TensorProducts` | `finite_crystals` | `TensorProducts` |

## FiniteDimensionalAlgebrasWithBasis {#cat-finitedimensionalalgebraswithbasis}

| field | value |
| --- | --- |
| module | `finite_dimensional_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | AlgebrasWithBasis + axiom FiniteDimensional |
| direct defining axiom | [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`Unital`](axioms.md#ax-unital), [`WithBasis`](axioms.md#ax-withbasis), [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| bound as | `AlgebrasWithBasis.FiniteDimensional` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/finite_dimensional_algebras_with_basis.py:36`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L36) |
| loads at 10.10 | yes |

### Local axiom paths

- `Cellular`

### Local construction paths

- `Cellular.TensorProducts`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Cellular`](axioms.md#ax-cellular) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/finite_dimensional_algebras_with_basis.py:1571`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L1571) |
| [`Cellular`](axioms.md#ax-cellular) | axiom | subcategory interface method | `_with_axiom(Cellular)` | [`src/sage/categories/finite_dimensional_algebras_with_basis.py:2020`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L2020) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/finite_dimensional_algebras_with_basis.py:1846`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L1846) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `FiniteDimensionalAlgebrasWithBasis` | `finite_dimensional_algebras_with_basis` | `(framework base)` |
| `FiniteDimensionalAlgebrasWithBasis.Cellular` | `finite_dimensional_algebras_with_basis` | `Cellular` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `FiniteDimensionalAlgebrasWithBasis.Cellular.TensorProducts` | `finite_dimensional_algebras_with_basis` | `TensorProducts` |

## FiniteDimensionalBialgebrasWithBasis(base_ring) {#cat-finitedimensionalbialgebraswithbasis-base-ring}

| field | value |
| --- | --- |
| module | `finite_dimensional_bialgebras_with_basis` |
| role | public category-valued wrapper constructor |
| implementation | Python function |
| defined by | BialgebrasWithBasis(base_ring).FiniteDimensional() |
| direct defining axiom | [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| syntactic axiom chain | [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| source | [`src/sage/categories/finite_dimensional_bialgebras_with_basis.py:13`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_bialgebras_with_basis.py#L13) |
| loads at 10.10 | no |
| notes | Returns a dynamically constructed category rather than an instance of a dedicated class. |

## FiniteDimensionalCoalgebrasWithBasis(base_ring) {#cat-finitedimensionalcoalgebraswithbasis-base-ring}

| field | value |
| --- | --- |
| module | `finite_dimensional_coalgebras_with_basis` |
| role | public category-valued wrapper constructor |
| implementation | Python function |
| defined by | CoalgebrasWithBasis(base_ring).FiniteDimensional() |
| direct defining axiom | [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| syntactic axiom chain | [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| source | [`src/sage/categories/finite_dimensional_coalgebras_with_basis.py:13`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_coalgebras_with_basis.py#L13) |
| loads at 10.10 | no |
| notes | Returns a dynamically constructed category rather than an instance of a dedicated class. |

## FiniteDimensionalGradedLieAlgebrasWithBasis {#cat-finitedimensionalgradedliealgebraswithbasis}

| field | value |
| --- | --- |
| module | `finite_dimensional_graded_lie_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | GradedLieAlgebrasWithBasis + axiom FiniteDimensional |
| direct defining axiom | [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| syntactic axiom chain | [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| bound as | `GradedLieAlgebrasWithBasis.FiniteDimensional` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/finite_dimensional_graded_lie_algebras_with_basis.py:23`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_graded_lie_algebras_with_basis.py#L23) |
| loads at 10.10 | yes |

### Local axiom paths

- `Stratified`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Stratified`](axioms.md#ax-stratified) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/finite_dimensional_graded_lie_algebras_with_basis.py:112`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_graded_lie_algebras_with_basis.py#L112) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `FiniteDimensionalGradedLieAlgebrasWithBasis` | `finite_dimensional_graded_lie_algebras_with_basis` | `(framework base)` |
| `FiniteDimensionalGradedLieAlgebrasWithBasis.Stratified` | `finite_dimensional_graded_lie_algebras_with_basis` | `Stratified` |

## FiniteDimensionalHopfAlgebrasWithBasis {#cat-finitedimensionalhopfalgebraswithbasis}

| field | value |
| --- | --- |
| module | `finite_dimensional_hopf_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | HopfAlgebrasWithBasis + axiom FiniteDimensional |
| direct defining axiom | [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| syntactic axiom chain | [`WithBasis`](axioms.md#ax-withbasis), [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| bound as | `HopfAlgebrasWithBasis.FiniteDimensional` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/finite_dimensional_hopf_algebras_with_basis.py:15`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_hopf_algebras_with_basis.py#L15) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FiniteDimensionalHopfAlgebrasWithBasis` | `finite_dimensional_hopf_algebras_with_basis` | `(framework base)` |

## FiniteDimensionalLieAlgebrasWithBasis {#cat-finitedimensionalliealgebraswithbasis}

| field | value |
| --- | --- |
| module | `finite_dimensional_lie_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | LieAlgebras.FiniteDimensional + axiom WithBasis |
| direct defining axiom | [`WithBasis`](axioms.md#ax-withbasis) |
| syntactic axiom chain | [`FiniteDimensional`](axioms.md#ax-finitedimensional), [`WithBasis`](axioms.md#ax-withbasis) |
| bound as | `LieAlgebras.FiniteDimensional.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/finite_dimensional_lie_algebras_with_basis.py:55`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_lie_algebras_with_basis.py#L55) |
| loads at 10.10 | yes |

### Local axiom paths

- `Nilpotent`

### Local construction paths

- `Subobjects`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Nilpotent`](axioms.md#ax-nilpotent) | axiom | lazy-import binding | `sage.categories.finite_dimensional_nilpotent_lie_algebras_with_basis.FiniteDimensionalNilpotentLieAlgebrasWithBasis` | [`src/sage/categories/finite_dimensional_lie_algebras_with_basis.py:87`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_lie_algebras_with_basis.py#L87) |
| [`Subobjects`](constructions.md#con-subobjects) | functorial construction | nested category class | `SubobjectsCategory` | [`src/sage/categories/finite_dimensional_lie_algebras_with_basis.py:2609`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_lie_algebras_with_basis.py#L2609) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FiniteDimensionalLieAlgebrasWithBasis` | `finite_dimensional_lie_algebras_with_basis` | `(framework base)` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `FiniteDimensionalLieAlgebrasWithBasis.Subobjects` | `finite_dimensional_lie_algebras_with_basis` | `Subobjects` |

## FiniteDimensionalModulesWithBasis {#cat-finitedimensionalmoduleswithbasis}

| field | value |
| --- | --- |
| module | `finite_dimensional_modules_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | ModulesWithBasis + axiom FiniteDimensional |
| direct defining axiom | [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| syntactic axiom chain | [`WithBasis`](axioms.md#ax-withbasis), [`FiniteDimensional`](axioms.md#ax-finitedimensional) |
| bound as | `ModulesWithBasis.FiniteDimensional` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/finite_dimensional_modules_with_basis.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L21) |
| loads at 10.10 | yes |

### Local axiom paths

- `Homsets.Endset`

### Local construction paths

- `Homsets`
- `TensorProducts`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/finite_dimensional_modules_with_basis.py:890`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L890) |
| [`Endset`](axioms.md#ax-endset) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/finite_dimensional_modules_with_basis.py:892`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L892) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/finite_dimensional_modules_with_basis.py:1050`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L1050) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `FiniteDimensionalModulesWithBasis` | `finite_dimensional_modules_with_basis` | `(framework base)` |
| `FiniteDimensionalModulesWithBasis.Homsets.Endset` | `finite_dimensional_modules_with_basis` | `Endset` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `FiniteDimensionalModulesWithBasis.Homsets` | `finite_dimensional_modules_with_basis` | `Homsets` |
| `FiniteDimensionalModulesWithBasis.TensorProducts` | `finite_dimensional_modules_with_basis` | `TensorProducts` |

## FiniteDimensionalNilpotentLieAlgebrasWithBasis {#cat-finitedimensionalnilpotentliealgebraswithbasis}

| field | value |
| --- | --- |
| module | `finite_dimensional_nilpotent_lie_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | LieAlgebras.FiniteDimensional.WithBasis + axiom Nilpotent |
| direct defining axiom | [`Nilpotent`](axioms.md#ax-nilpotent) |
| syntactic axiom chain | [`FiniteDimensional`](axioms.md#ax-finitedimensional), [`WithBasis`](axioms.md#ax-withbasis), [`Nilpotent`](axioms.md#ax-nilpotent) |
| bound as | `FiniteDimensionalLieAlgebrasWithBasis.Nilpotent` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/finite_dimensional_nilpotent_lie_algebras_with_basis.py:24`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_nilpotent_lie_algebras_with_basis.py#L24) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FiniteDimensionalNilpotentLieAlgebrasWithBasis` | `finite_dimensional_nilpotent_lie_algebras_with_basis` | `(framework base)` |

## FiniteDimensionalSemisimpleAlgebrasWithBasis {#cat-finitedimensionalsemisimplealgebraswithbasis}

| field | value |
| --- | --- |
| module | `finite_dimensional_semisimple_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | SemisimpleAlgebras.FiniteDimensional + axiom WithBasis |
| direct defining axiom | [`WithBasis`](axioms.md#ax-withbasis) |
| syntactic axiom chain | [`FiniteDimensional`](axioms.md#ax-finitedimensional), [`WithBasis`](axioms.md#ax-withbasis) |
| bound as | `SemisimpleAlgebras.FiniteDimensional.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/finite_dimensional_semisimple_algebras_with_basis.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_semisimple_algebras_with_basis.py#L18) |
| loads at 10.10 | yes |

### Local axiom paths

- `Commutative`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Commutative`](axioms.md#ax-commutative) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/finite_dimensional_semisimple_algebras_with_basis.py:116`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_semisimple_algebras_with_basis.py#L116) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `FiniteDimensionalSemisimpleAlgebrasWithBasis` | `finite_dimensional_semisimple_algebras_with_basis` | `(framework base)` |
| `FiniteDimensionalSemisimpleAlgebrasWithBasis.Commutative` | `finite_dimensional_semisimple_algebras_with_basis` | `Commutative` |

## FiniteEnumeratedSets {#cat-finiteenumeratedsets}

| field | value |
| --- | --- |
| module | `finite_enumerated_sets` |
| role | public named category class |
| implementation | Python class |
| defined by | EnumeratedSets + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Enumerated`](axioms.md#ax-enumerated), [`Finite`](axioms.md#ax-finite) |
| bound as | `EnumeratedSets.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_enumerated_sets.py:22`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_enumerated_sets.py#L22) |
| loads at 10.10 | yes |

### Local construction paths

- `CartesianProducts`
- `IsomorphicObjects`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/finite_enumerated_sets.py:662`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_enumerated_sets.py#L662) |
| [`IsomorphicObjects`](constructions.md#con-isomorphicobjects) | functorial construction | nested category class | `IsomorphicObjectsCategory` | [`src/sage/categories/finite_enumerated_sets.py:820`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_enumerated_sets.py#L820) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `FiniteEnumeratedSets` | `finite_enumerated_sets` | `(framework base)` |
| `FiniteEnumeratedSets_with_category` | `finite_enumerated_sets` | `(framework base)` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `FiniteEnumeratedSets.CartesianProducts` | `finite_enumerated_sets` | `CartesianProducts` |
| `FiniteEnumeratedSets.IsomorphicObjects` | `finite_enumerated_sets` | `IsomorphicObjects` |

## FiniteFields {#cat-finitefields}

| field | value |
| --- | --- |
| module | `finite_fields` |
| role | public named category class |
| implementation | Python class |
| defined by | Fields + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Distributive`](axioms.md#ax-distributive), [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveCommutative`](axioms.md#ax-additivecommutative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`Associative`](axioms.md#ax-associative), [`AdditiveInverse`](axioms.md#ax-additiveinverse), [`Unital`](axioms.md#ax-unital), [`Division`](axioms.md#ax-division), [`Commutative`](axioms.md#ax-commutative), [`Finite`](axioms.md#ax-finite) |
| bound as | `Fields.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_fields.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_fields.py#L21) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FiniteFields` | `finite_fields` | `(framework base)` |

## FiniteGroups {#cat-finitegroups}

| field | value |
| --- | --- |
| module | `finite_groups` |
| role | public named category class |
| implementation | Python class |
| defined by | Groups + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`Unital`](axioms.md#ax-unital), [`Inverse`](axioms.md#ax-inverse), [`Finite`](axioms.md#ax-finite) |
| bound as | `Groups.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_groups.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_groups.py#L16) |
| loads at 10.10 | yes |

### Local construction paths

- `Algebras`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/finite_groups.py:183`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_groups.py#L183) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FiniteGroups` | `finite_groups` | `(framework base)` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `FiniteGroups.Algebras` | `finite_groups` | `Algebras` |

## FiniteLatticePosets {#cat-finitelatticeposets}

| field | value |
| --- | --- |
| module | `finite_lattice_posets` |
| role | public named category class |
| implementation | Python class |
| defined by | LatticePosets + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Finite`](axioms.md#ax-finite) |
| bound as | `LatticePosets.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_lattice_posets.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_lattice_posets.py#L16) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FiniteLatticePosets` | `finite_lattice_posets` | `(framework base)` |

## FiniteMonoids {#cat-finitemonoids}

| field | value |
| --- | --- |
| module | `finite_monoids` |
| role | public named category class |
| implementation | Python class |
| defined by | Monoids + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`Unital`](axioms.md#ax-unital), [`Finite`](axioms.md#ax-finite) |
| bound as | `Monoids.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_monoids.py:14`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_monoids.py#L14) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FiniteMonoids` | `finite_monoids` | `(framework base)` |

## FinitePermutationGroups {#cat-finitepermutationgroups}

| field | value |
| --- | --- |
| module | `finite_permutation_groups` |
| role | public named category class |
| implementation | Python class |
| defined by | PermutationGroups + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Finite`](axioms.md#ax-finite) |
| bound as | `PermutationGroups.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_permutation_groups.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_permutation_groups.py#L18) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FinitePermutationGroups` | `finite_permutation_groups` | `(framework base)` |

## FinitePosets {#cat-finiteposets}

| field | value |
| --- | --- |
| module | `finite_posets` |
| role | public named category class |
| implementation | Python class |
| defined by | Posets + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Finite`](axioms.md#ax-finite) |
| bound as | `Posets.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_posets.py:24`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_posets.py#L24) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FinitePosets` | `finite_posets` | `(framework base)` |

## FiniteSemigroups {#cat-finitesemigroups}

| field | value |
| --- | --- |
| module | `finite_semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | Semigroups + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`Finite`](axioms.md#ax-finite) |
| bound as | `Semigroups.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_semigroups.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_semigroups.py#L18) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FiniteSemigroups` | `finite_semigroups` | `(framework base)` |

## FiniteSets {#cat-finitesets}

| field | value |
| --- | --- |
| module | `finite_sets` |
| role | public named category class |
| implementation | Python class |
| defined by | Sets + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Finite`](axioms.md#ax-finite) |
| bound as | `Sets.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_sets.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L16) |
| loads at 10.10 | yes |

### Local axiom paths

- `Infinite`

### Local construction paths

- `Algebras`
- `Subquotients`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/finite_sets.py:91`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L91) |
| [`Infinite`](axioms.md#ax-infinite) | axiom | subcategory interface method | — | [`src/sage/categories/finite_sets.py:42`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L42) |
| [`Subquotients`](constructions.md#con-subquotients) | functorial construction | nested category class | `SubquotientsCategory` | [`src/sage/categories/finite_sets.py:70`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L70) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `FiniteSets` | `finite_sets` | `(framework base)` |
| `FiniteSets_with_category` | `finite_sets` | `(framework base)` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `FiniteSets.Algebras` | `finite_sets` | `Algebras` |
| `FiniteSets.Subquotients` | `finite_sets` | `Subquotients` |

## FiniteWeylGroups {#cat-finiteweylgroups}

| field | value |
| --- | --- |
| module | `finite_weyl_groups` |
| role | public named category class |
| implementation | Python class |
| defined by | WeylGroups + axiom Finite |
| direct defining axiom | [`Finite`](axioms.md#ax-finite) |
| syntactic axiom chain | [`Finite`](axioms.md#ax-finite) |
| bound as | `WeylGroups.Finite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finite_weyl_groups.py:14`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_weyl_groups.py#L14) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FiniteWeylGroups` | `finite_weyl_groups` | `(framework base)` |

## FinitelyGeneratedLambdaBracketAlgebras {#cat-finitelygeneratedlambdabracketalgebras}

| field | value |
| --- | --- |
| module | `finitely_generated_lambda_bracket_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | LambdaBracketAlgebras + axiom FinitelyGeneratedAsLambdaBracketAlgebra |
| direct defining axiom | [`FinitelyGeneratedAsLambdaBracketAlgebra`](axioms.md#ax-finitelygeneratedaslambdabracketalgebra) |
| syntactic axiom chain | [`FinitelyGeneratedAsLambdaBracketAlgebra`](axioms.md#ax-finitelygeneratedaslambdabracketalgebra) |
| bound as | `LambdaBracketAlgebras.FinitelyGeneratedAsLambdaBracketAlgebra` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/finitely_generated_lambda_bracket_algebras.py:24`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lambda_bracket_algebras.py#L24) |
| loads at 10.10 | yes |

### Local construction paths

- `Graded`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Graded`](constructions.md#con-graded) | functorial construction | nested category class | `GradedModulesCategory` | [`src/sage/categories/finitely_generated_lambda_bracket_algebras.py:92`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lambda_bracket_algebras.py#L92) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FinitelyGeneratedLambdaBracketAlgebras` | `finitely_generated_lambda_bracket_algebras` | `(framework base)` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `FinitelyGeneratedLambdaBracketAlgebras.Graded` | `finitely_generated_lambda_bracket_algebras` | `Graded` |

## FinitelyGeneratedLieConformalAlgebras {#cat-finitelygeneratedlieconformalalgebras}

| field | value |
| --- | --- |
| module | `finitely_generated_lie_conformal_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | LieConformalAlgebras + axiom FinitelyGeneratedAsLambdaBracketAlgebra |
| direct defining axiom | [`FinitelyGeneratedAsLambdaBracketAlgebra`](axioms.md#ax-finitelygeneratedaslambdabracketalgebra) |
| syntactic axiom chain | [`FinitelyGeneratedAsLambdaBracketAlgebra`](axioms.md#ax-finitelygeneratedaslambdabracketalgebra) |
| bound as | `LieConformalAlgebras.FinitelyGeneratedAsLambdaBracketAlgebra` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/finitely_generated_lie_conformal_algebras.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lie_conformal_algebras.py#L25) |
| loads at 10.10 | yes |

### Local construction paths

- `Graded`
- `Super`
- `Super.Graded`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Graded`](constructions.md#con-graded) | functorial construction | nested category class | `GradedModulesCategory` | [`src/sage/categories/finitely_generated_lie_conformal_algebras.py:93`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lie_conformal_algebras.py#L93) |
| [`Super`](constructions.md#con-super) | functorial construction | nested category class | `SuperModulesCategory` | [`src/sage/categories/finitely_generated_lie_conformal_algebras.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lie_conformal_algebras.py#L60) |
| [`Graded`](constructions.md#con-graded) | functorial construction | nested category class | `GradedModulesCategory` | [`src/sage/categories/finitely_generated_lie_conformal_algebras.py:70`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_lie_conformal_algebras.py#L70) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FinitelyGeneratedLieConformalAlgebras` | `finitely_generated_lie_conformal_algebras` | `(framework base)` |

### Construction-generated classes at 10.10 (3)

| class | module | construction |
| --- | --- | --- |
| `FinitelyGeneratedLieConformalAlgebras.Graded` | `finitely_generated_lie_conformal_algebras` | `Graded` |
| `FinitelyGeneratedLieConformalAlgebras.Super` | `finitely_generated_lie_conformal_algebras` | `Super` |
| `FinitelyGeneratedLieConformalAlgebras.Super.Graded` | `finitely_generated_lie_conformal_algebras` | `Graded` |

## FinitelyGeneratedMagmas {#cat-finitelygeneratedmagmas}

| field | value |
| --- | --- |
| module | `finitely_generated_magmas` |
| role | public named category class |
| implementation | Python class |
| defined by | Magmas + axiom FinitelyGeneratedAsMagma |
| direct defining axiom | [`FinitelyGeneratedAsMagma`](axioms.md#ax-finitelygeneratedasmagma) |
| syntactic axiom chain | [`FinitelyGeneratedAsMagma`](axioms.md#ax-finitelygeneratedasmagma) |
| bound as | `Magmas.FinitelyGeneratedAsMagma` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finitely_generated_magmas.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_magmas.py#L16) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `FinitelyGeneratedMagmas` | `finitely_generated_magmas` | `(framework base)` |

## FinitelyGeneratedSemigroups {#cat-finitelygeneratedsemigroups}

| field | value |
| --- | --- |
| module | `finitely_generated_semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | Semigroups + axiom FinitelyGeneratedAsMagma |
| direct defining axiom | [`FinitelyGeneratedAsMagma`](axioms.md#ax-finitelygeneratedasmagma) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`FinitelyGeneratedAsMagma`](axioms.md#ax-finitelygeneratedasmagma) |
| bound as | `Semigroups.FinitelyGeneratedAsMagma` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/finitely_generated_semigroups.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_semigroups.py#L19) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/finitely_generated_semigroups.py:192`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finitely_generated_semigroups.py#L192) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `FinitelyGeneratedSemigroups` | `finitely_generated_semigroups` | `(framework base)` |
| `FinitelyGeneratedSemigroups.Finite` | `finitely_generated_semigroups` | `Finite` |

## FunctionFields {#cat-functionfields}

| field | value |
| --- | --- |
| module | `function_fields` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/function_fields.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/function_fields.py#L19) |
| loads at 10.10 | yes |

## FunctorialConstructionCategory {#cat-functorialconstructioncategory}

| field | value |
| --- | --- |
| module | `covariant_functorial_construction` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/covariant_functorial_construction.py:230`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/covariant_functorial_construction.py#L230) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `FunctorialConstructionCategory` | `covariant_functorial_construction` | `(framework base)` |

## GSets {#cat-gsets}

| field | value |
| --- | --- |
| module | `g_sets` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/g_sets.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/g_sets.py#L21) |
| loads at 10.10 | yes |

## GcdDomains {#cat-gcddomains}

| field | value |
| --- | --- |
| module | `gcd_domains` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/gcd_domains.py:15`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/gcd_domains.py#L15) |
| loads at 10.10 | yes |

## GeneralizedCoxeterGroups {#cat-generalizedcoxetergroups}

| field | value |
| --- | --- |
| module | `generalized_coxeter_groups` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/generalized_coxeter_groups.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/generalized_coxeter_groups.py#L20) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/generalized_coxeter_groups.py:72`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/generalized_coxeter_groups.py#L72) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `GeneralizedCoxeterGroups.Finite` | `generalized_coxeter_groups` | `Finite` |

## GradedAlgebras {#cat-gradedalgebras}

| field | value |
| --- | --- |
| module | `graded_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | Algebras.Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| bound as | `Algebras.Graded` |
| bases | [`GradedModulesCategory`](categories.md#cat-gradedmodulescategory) |
| source | [`src/sage/categories/graded_algebras.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras.py#L17) |
| loads at 10.10 | yes |

### Local construction paths

- `SignedTensorProducts`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`SignedTensorProducts`](constructions.md#con-signedtensorproducts) | functorial construction | nested category class | `SignedTensorProductsCategory` | [`src/sage/categories/graded_algebras.py:71`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras.py#L71) |
| [`SignedTensorProducts`](constructions.md#con-signedtensorproducts) | functorial construction | subcategory interface method | `SignedTensorProductsCategory.category_of(...)` | [`src/sage/categories/graded_algebras.py:53`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras.py#L53) |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `GradedAlgebras` | `graded_algebras` | `(framework base)` |
| `GradedAlgebras.SignedTensorProducts` | `graded_algebras` | `SignedTensorProducts` |

## GradedAlgebrasWithBasis {#cat-gradedalgebraswithbasis}

| field | value |
| --- | --- |
| module | `graded_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | AlgebrasWithBasis.Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| bound as | `AlgebrasWithBasis.Graded` |
| bases | [`GradedModulesCategory`](categories.md#cat-gradedmodulescategory) |
| source | [`src/sage/categories/graded_algebras_with_basis.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras_with_basis.py#L18) |
| loads at 10.10 | yes |

### Local axiom paths

- `FiniteDimensional`

### Local construction paths

- `SignedTensorProducts`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/graded_algebras_with_basis.py:157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras_with_basis.py#L157) |
| [`SignedTensorProducts`](constructions.md#con-signedtensorproducts) | functorial construction | nested category class | `SignedTensorProductsCategory` | [`src/sage/categories/graded_algebras_with_basis.py:175`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras_with_basis.py#L175) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `GradedAlgebrasWithBasis.FiniteDimensional` | `graded_algebras_with_basis` | `FiniteDimensional` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `GradedAlgebrasWithBasis` | `graded_algebras_with_basis` | `(framework base)` |
| `GradedAlgebrasWithBasis.SignedTensorProducts` | `graded_algebras_with_basis` | `SignedTensorProducts` |

## GradedBialgebras(base_ring) {#cat-gradedbialgebras-base-ring}

| field | value |
| --- | --- |
| module | `graded_bialgebras` |
| role | public category-valued wrapper constructor |
| implementation | Python function |
| defined by | Bialgebras(base_ring).Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| source | [`src/sage/categories/graded_bialgebras.py:13`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_bialgebras.py#L13) |
| loads at 10.10 | no |
| notes | Returns a dynamically constructed category rather than an instance of a dedicated class. |

## GradedBialgebrasWithBasis(base_ring) {#cat-gradedbialgebraswithbasis-base-ring}

| field | value |
| --- | --- |
| module | `graded_bialgebras_with_basis` |
| role | public category-valued wrapper constructor |
| implementation | Python function |
| defined by | BialgebrasWithBasis(base_ring).Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| source | [`src/sage/categories/graded_bialgebras_with_basis.py:13`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_bialgebras_with_basis.py#L13) |
| loads at 10.10 | no |
| notes | Returns a dynamically constructed category rather than an instance of a dedicated class. |

## GradedCoalgebras {#cat-gradedcoalgebras}

| field | value |
| --- | --- |
| module | `graded_coalgebras` |
| role | public named category class |
| implementation | Python class |
| defined by | Coalgebras.Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| bound as | `Coalgebras.Graded` |
| bases | [`GradedModulesCategory`](categories.md#cat-gradedmodulescategory) |
| source | [`src/sage/categories/graded_coalgebras.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_coalgebras.py#L17) |
| loads at 10.10 | yes |

### Local construction paths

- `SignedTensorProducts`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`SignedTensorProducts`](constructions.md#con-signedtensorproducts) | functorial construction | nested category class | `SignedTensorProductsCategory` | [`src/sage/categories/graded_coalgebras.py:51`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_coalgebras.py#L51) |
| [`SignedTensorProducts`](constructions.md#con-signedtensorproducts) | functorial construction | subcategory interface method | `SignedTensorProductsCategory.category_of(...)` | [`src/sage/categories/graded_coalgebras.py:33`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_coalgebras.py#L33) |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `GradedCoalgebras` | `graded_coalgebras` | `(framework base)` |
| `GradedCoalgebras.SignedTensorProducts` | `graded_coalgebras` | `SignedTensorProducts` |

## GradedCoalgebrasWithBasis {#cat-gradedcoalgebraswithbasis}

| field | value |
| --- | --- |
| module | `graded_coalgebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | CoalgebrasWithBasis.Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| bound as | `CoalgebrasWithBasis.Graded` |
| bases | [`GradedModulesCategory`](categories.md#cat-gradedmodulescategory) |
| source | [`src/sage/categories/graded_coalgebras_with_basis.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_coalgebras_with_basis.py#L18) |
| loads at 10.10 | yes |

### Local construction paths

- `SignedTensorProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`SignedTensorProducts`](constructions.md#con-signedtensorproducts) | functorial construction | nested category class | `SignedTensorProductsCategory` | [`src/sage/categories/graded_coalgebras_with_basis.py:33`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_coalgebras_with_basis.py#L33) |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `GradedCoalgebrasWithBasis` | `graded_coalgebras_with_basis` | `(framework base)` |
| `GradedCoalgebrasWithBasis.SignedTensorProducts` | `graded_coalgebras_with_basis` | `SignedTensorProducts` |

## GradedHopfAlgebras(base_ring) {#cat-gradedhopfalgebras-base-ring}

| field | value |
| --- | --- |
| module | `graded_hopf_algebras` |
| role | public category-valued wrapper constructor |
| implementation | Python function |
| defined by | HopfAlgebras(base_ring).Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| source | [`src/sage/categories/graded_hopf_algebras.py:13`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_hopf_algebras.py#L13) |
| loads at 10.10 | no |
| notes | Returns a dynamically constructed category rather than an instance of a dedicated class. |

## GradedHopfAlgebrasWithBasis {#cat-gradedhopfalgebraswithbasis}

| field | value |
| --- | --- |
| module | `graded_hopf_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | HopfAlgebrasWithBasis.Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| bound as | `HopfAlgebrasWithBasis.Graded` |
| bases | [`GradedModulesCategory`](categories.md#cat-gradedmodulescategory) |
| source | [`src/sage/categories/graded_hopf_algebras_with_basis.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_hopf_algebras_with_basis.py#L18) |
| loads at 10.10 | yes |

### Local axiom paths

- `Connected`

### Local construction paths

- `WithRealizations`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Connected`](axioms.md#ax-connected) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/graded_hopf_algebras_with_basis.py:79`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_hopf_algebras_with_basis.py#L79) |
| [`WithRealizations`](constructions.md#con-withrealizations) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/graded_hopf_algebras_with_basis.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_hopf_algebras_with_basis.py#L60) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `GradedHopfAlgebrasWithBasis.Connected` | `graded_hopf_algebras_with_basis` | `Connected` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `GradedHopfAlgebrasWithBasis` | `graded_hopf_algebras_with_basis` | `(framework base)` |
| `GradedHopfAlgebrasWithBasis.WithRealizations` | `graded_hopf_algebras_with_basis` | `WithRealizations` |

## GradedLieAlgebras {#cat-gradedliealgebras}

| field | value |
| --- | --- |
| module | `graded_lie_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | LieAlgebras.Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| bound as | `LieAlgebras.Graded` |
| bases | [`GradedModulesCategory`](categories.md#cat-gradedmodulescategory) |
| source | [`src/sage/categories/graded_lie_algebras.py:23`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras.py#L23) |
| loads at 10.10 | yes |

### Local axiom paths

- `Stratified`
- `Stratified.FiniteDimensional`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Stratified`](axioms.md#ax-stratified) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/graded_lie_algebras.py:47`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras.py#L47) |
| [`Stratified`](axioms.md#ax-stratified) | axiom | subcategory interface method | `_with_axiom(Stratified)` | [`src/sage/categories/graded_lie_algebras.py:33`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras.py#L33) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/graded_lie_algebras.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras.py#L60) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `GradedLieAlgebras.Stratified` | `graded_lie_algebras` | `Stratified` |
| `GradedLieAlgebras.Stratified.FiniteDimensional` | `graded_lie_algebras` | `FiniteDimensional` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `GradedLieAlgebras` | `graded_lie_algebras` | `(framework base)` |

## GradedLieAlgebrasWithBasis {#cat-gradedliealgebraswithbasis}

| field | value |
| --- | --- |
| module | `graded_lie_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | LieAlgebrasWithBasis.Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| bound as | `LieAlgebrasWithBasis.Graded` |
| bases | [`GradedModulesCategory`](categories.md#cat-gradedmodulescategory) |
| source | [`src/sage/categories/graded_lie_algebras_with_basis.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras_with_basis.py#L19) |
| loads at 10.10 | yes |

### Local axiom paths

- `FiniteDimensional`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | lazy-import binding | `sage.categories.finite_dimensional_graded_lie_algebras_with_basis.FiniteDimensionalGradedLieAlgebrasWithBasis` | [`src/sage/categories/graded_lie_algebras_with_basis.py:41`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras_with_basis.py#L41) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `GradedLieAlgebrasWithBasis` | `graded_lie_algebras_with_basis` | `(framework base)` |

## GradedLieConformalAlgebras {#cat-gradedlieconformalalgebras}

| field | value |
| --- | --- |
| module | `graded_lie_conformal_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | LieConformalAlgebras.Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| bound as | `LieConformalAlgebras.Graded` |
| bases | [`GradedLieConformalAlgebrasCategory`](categories.md#cat-gradedlieconformalalgebrascategory) |
| source | [`src/sage/categories/graded_lie_conformal_algebras.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_conformal_algebras.py#L60) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `GradedLieConformalAlgebras` | `graded_lie_conformal_algebras` | `(framework base)` |

## GradedLieConformalAlgebrasCategory {#cat-gradedlieconformalalgebrascategory}

| field | value |
| --- | --- |
| module | `graded_lie_conformal_algebras` |
| role | framework/helper category class |
| implementation | Python class |
| defined by | generic base category.Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| bases | [`GradedModulesCategory`](categories.md#cat-gradedmodulescategory) |
| source | [`src/sage/categories/graded_lie_conformal_algebras.py:23`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_conformal_algebras.py#L23) |
| loads at 10.10 | yes |

### Local construction paths

- `Super`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Super`](constructions.md#con-super) | functorial construction | category method | `calls Graded()` | [`src/sage/categories/graded_lie_conformal_algebras.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_conformal_algebras.py#L25) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `GradedLieConformalAlgebrasCategory` | `graded_lie_conformal_algebras` | `(framework base)` |

## GradedModules {#cat-gradedmodules}

| field | value |
| --- | --- |
| module | `graded_modules` |
| role | public named category class |
| implementation | Python class |
| defined by | Modules.Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| bound as | `Modules.Graded` |
| bases | [`GradedModulesCategory`](categories.md#cat-gradedmodulescategory) |
| source | [`src/sage/categories/graded_modules.py:100`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_modules.py#L100) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `GradedModules` | `graded_modules` | `(framework base)` |

## GradedModulesCategory {#cat-gradedmodulescategory}

| field | value |
| --- | --- |
| module | `graded_modules` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`RegressiveCovariantConstructionCategory`](categories.md#cat-regressivecovariantconstructioncategory), [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/graded_modules.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_modules.py#L17) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `GradedModulesCategory` | `graded_modules` | `(framework base)` |

## GradedModulesWithBasis {#cat-gradedmoduleswithbasis}

| field | value |
| --- | --- |
| module | `graded_modules_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | ModulesWithBasis.Graded() |
| defining construction | [`Graded`](constructions.md#con-graded) |
| bound as | `ModulesWithBasis.Graded` |
| bases | [`GradedModulesCategory`](categories.md#cat-gradedmodulescategory) |
| source | [`src/sage/categories/graded_modules_with_basis.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_modules_with_basis.py#L16) |
| loads at 10.10 | yes |

### Local construction paths

- `Quotients`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Quotients`](constructions.md#con-quotients) | functorial construction | nested category class | `QuotientsCategory` | [`src/sage/categories/graded_modules_with_basis.py:290`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_modules_with_basis.py#L290) |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `GradedModulesWithBasis` | `graded_modules_with_basis` | `(framework base)` |
| `GradedModulesWithBasis.Quotients` | `graded_modules_with_basis` | `Quotients` |

## Graphs {#cat-graphs}

| field | value |
| --- | --- |
| module | `graphs` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/graphs.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graphs.py#L19) |
| loads at 10.10 | yes |

### Local axiom paths

- `Connected`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Connected`](axioms.md#ax-connected) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/graphs.py:112`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graphs.py#L112) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `Graphs.Connected` | `graphs` | `Connected` |

## GroupAlgebras {#cat-groupalgebras}

| field | value |
| --- | --- |
| module | `group_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | Groups.Algebras() |
| defining construction | [`Algebras`](constructions.md#con-algebras) |
| bound as | `Groups.Algebras` |
| bases | [`AlgebrasCategory`](categories.md#cat-algebrascategory) |
| source | [`src/sage/categories/group_algebras.py:34`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/group_algebras.py#L34) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `GroupAlgebras` | `group_algebras` | `(framework base)` |

## Groupoid {#cat-groupoid}

| field | value |
| --- | --- |
| module | `groupoid` |
| role | public named category class |
| implementation | Python class |
| bases | [`CategoryWithParameters`](categories.md#cat-categorywithparameters) |
| source | [`src/sage/categories/groupoid.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groupoid.py#L18) |
| loads at 10.10 | yes |

## Groups {#cat-groups}

| field | value |
| --- | --- |
| module | `groups` |
| role | public named category class |
| implementation | Python class |
| defined by | Monoids + axiom Inverse |
| direct defining axiom | [`Inverse`](axioms.md#ax-inverse) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`Unital`](axioms.md#ax-unital), [`Inverse`](axioms.md#ax-inverse) |
| bound as | `Monoids.Inverse` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/groups.py:23`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L23) |
| loads at 10.10 | yes |

### Local axiom paths

- `Commutative`
- `Finite`

### Local construction paths

- `Algebras`
- `CartesianProducts`
- `Topological`

### Other local category paths

- `Lie`

### Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | lazy-import binding | `sage.categories.group_algebras.GroupAlgebras` | [`src/sage/categories/groups.py:493`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L493) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/groups.py:547`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L547) |
| [`Commutative`](axioms.md#ax-commutative) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/groups.py:495`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L495) |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_groups.FiniteGroups` | [`src/sage/categories/groups.py:491`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L491) |
| `Lie` | other category | lazy-import binding | `sage.categories.lie_groups.LieGroups` | [`src/sage/categories/groups.py:492`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L492) |
| [`Topological`](constructions.md#con-topological) | functorial construction | nested category class | `TopologicalSpacesCategory` | [`src/sage/categories/groups.py:654`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L654) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Groups` | `groups` | `(framework base)` |
| `Groups.Commutative` | `groups` | `Commutative` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `Groups.CartesianProducts` | `groups` | `CartesianProducts` |
| `Groups.Topological` | `groups` | `Topological` |

## HTrivialSemigroups {#cat-htrivialsemigroups}

| field | value |
| --- | --- |
| module | `h_trivial_semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | Semigroups + axiom HTrivial |
| direct defining axiom | [`HTrivial`](axioms.md#ax-htrivial) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`HTrivial`](axioms.md#ax-htrivial) |
| bound as | `Semigroups.HTrivial` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/h_trivial_semigroups.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/h_trivial_semigroups.py#L18) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `HTrivialSemigroups` | `h_trivial_semigroups` | `(framework base)` |

## HeckeModules {#cat-heckemodules}

| field | value |
| --- | --- |
| module | `hecke_modules` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_module`](categories.md#cat-category-module) |
| source | [`src/sage/categories/hecke_modules.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hecke_modules.py#L18) |
| loads at 10.10 | yes |

### Local construction paths

- `Homsets`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/hecke_modules.py:158`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hecke_modules.py#L158) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `HeckeModules.Homsets` | `hecke_modules` | `Homsets` |

## HighestWeightCrystals {#cat-highestweightcrystals}

| field | value |
| --- | --- |
| module | `highest_weight_crystals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/highest_weight_crystals.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/highest_weight_crystals.py#L19) |
| loads at 10.10 | yes |

### Local construction paths

- `TensorProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/highest_weight_crystals.py:655`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/highest_weight_crystals.py#L655) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `HighestWeightCrystals.TensorProducts` | `highest_weight_crystals` | `TensorProducts` |

## Homsets {#cat-homsets}

| field | value |
| --- | --- |
| module | `homsets` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/homsets.py:236`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/homsets.py#L236) |
| loads at 10.10 | yes |

### Local axiom paths

- `Endset`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Endset`](axioms.md#ax-endset) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/homsets.py:296`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/homsets.py#L296) |
| [`Endset`](axioms.md#ax-endset) | axiom | subcategory interface method | `_with_axiom(Endset)` | [`src/sage/categories/homsets.py:282`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/homsets.py#L282) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `Homsets.Endset` | `homsets` | `Endset` |

## HomsetsCategory {#cat-homsetscategory}

| field | value |
| --- | --- |
| module | `homsets` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`FunctorialConstructionCategory`](categories.md#cat-functorialconstructioncategory), [`CategoryWithParameters`](categories.md#cat-categorywithparameters) |
| source | [`src/sage/categories/homsets.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/homsets.py#L18) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `HomsetsCategory` | `homsets` | `(framework base)` |

## HomsetsOf {#cat-homsetsof}

| field | value |
| --- | --- |
| module | `homsets` |
| role | framework/helper category class |
| implementation | Python class |
| defined by | generic base category.Homsets() |
| defining construction | [`Homsets`](constructions.md#con-homsets) |
| bases | [`HomsetsCategory`](categories.md#cat-homsetscategory) |
| source | [`src/sage/categories/homsets.py:172`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/homsets.py#L172) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (3)

| class | module | construction |
| --- | --- | --- |
| `HomsetsOf` | `homsets` | `(framework base)` |
| `HomsetsOf_with_category` | `homsets` | `(framework base)` |
| `HomsetsOf_with_category` | `homsets` | `(framework base)` |

## HopfAlgebras {#cat-hopfalgebras}

| field | value |
| --- | --- |
| module | `hopf_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/hopf_algebras.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L21) |
| loads at 10.10 | yes |

### Local axiom paths

- `WithBasis`

### Local construction paths

- `Realizations`
- `Super`
- `TensorProducts`

### Other local category paths

- `DualCategory`
- `Morphism`

### Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| `DualCategory` | other category | nested category class | `Category_over_base_ring` | [`src/sage/categories/hopf_algebras.py:176`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L176) |
| `Morphism` | other category | nested category class | `Category` | [`src/sage/categories/hopf_algebras.py:103`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L103) |
| [`Realizations`](constructions.md#con-realizations) | functorial construction | nested category class | `RealizationsCategory` | [`src/sage/categories/hopf_algebras.py:187`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L187) |
| [`Super`](constructions.md#con-super) | functorial construction | nested category class | `SuperModulesCategory` | [`src/sage/categories/hopf_algebras.py:109`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L109) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/hopf_algebras.py:147`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L147) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | lazy-import binding | `sage.categories.hopf_algebras_with_basis.HopfAlgebrasWithBasis` | [`src/sage/categories/hopf_algebras.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L60) |

### Construction-generated classes at 10.10 (3)

| class | module | construction |
| --- | --- | --- |
| `HopfAlgebras.Realizations` | `hopf_algebras` | `Realizations` |
| `HopfAlgebras.Super` | `hopf_algebras` | `Super` |
| `HopfAlgebras.TensorProducts` | `hopf_algebras` | `TensorProducts` |

## HopfAlgebrasWithBasis {#cat-hopfalgebraswithbasis}

| field | value |
| --- | --- |
| module | `hopf_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | HopfAlgebras + axiom WithBasis |
| direct defining axiom | [`WithBasis`](axioms.md#ax-withbasis) |
| syntactic axiom chain | [`WithBasis`](axioms.md#ax-withbasis) |
| bound as | `HopfAlgebras.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/hopf_algebras_with_basis.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L20) |
| loads at 10.10 | yes |

### Local axiom paths

- `FiniteDimensional`

### Local construction paths

- `Filtered`
- `Graded`
- `Super`
- `TensorProducts`

### Declared features (5)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Filtered`](constructions.md#con-filtered) | functorial construction | lazy-import binding | `sage.categories.filtered_hopf_algebras_with_basis.FilteredHopfAlgebrasWithBasis` | [`src/sage/categories/hopf_algebras_with_basis.py:159`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L159) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | lazy-import binding | `sage.categories.finite_dimensional_hopf_algebras_with_basis.FiniteDimensionalHopfAlgebrasWithBasis` | [`src/sage/categories/hopf_algebras_with_basis.py:157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L157) |
| [`Graded`](constructions.md#con-graded) | functorial construction | lazy-import binding | `sage.categories.graded_hopf_algebras_with_basis.GradedHopfAlgebrasWithBasis` | [`src/sage/categories/hopf_algebras_with_basis.py:161`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L161) |
| [`Super`](constructions.md#con-super) | functorial construction | lazy-import binding | `sage.categories.super_hopf_algebras_with_basis.SuperHopfAlgebrasWithBasis` | [`src/sage/categories/hopf_algebras_with_basis.py:163`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L163) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/hopf_algebras_with_basis.py:284`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L284) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `HopfAlgebrasWithBasis` | `hopf_algebras_with_basis` | `(framework base)` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `HopfAlgebrasWithBasis.TensorProducts` | `hopf_algebras_with_basis` | `TensorProducts` |

## IdempotentSemigroups {#cat-idempotentsemigroups}

| field | value |
| --- | --- |
| module | `examples/semigroups_cython` |
| role | example-only category class |
| implementation | Cython class |
| defined by | supercategory Semigroups() |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/examples/semigroups_cython.pyx:13`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/examples/semigroups_cython.pyx#L13) |
| loads at 10.10 | no |
| notes | Demonstration category used by the Cython semigroup example. |

## InfiniteEnumeratedSets {#cat-infiniteenumeratedsets}

| field | value |
| --- | --- |
| module | `infinite_enumerated_sets` |
| role | public named category class |
| implementation | Python class |
| defined by | EnumeratedSets + axiom Infinite |
| direct defining axiom | [`Infinite`](axioms.md#ax-infinite) |
| syntactic axiom chain | [`Enumerated`](axioms.md#ax-enumerated), [`Infinite`](axioms.md#ax-infinite) |
| bound as | `EnumeratedSets.Infinite` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/infinite_enumerated_sets.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/infinite_enumerated_sets.py#L19) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `InfiniteEnumeratedSets` | `infinite_enumerated_sets` | `(framework base)` |
| `InfiniteEnumeratedSets_with_category` | `infinite_enumerated_sets` | `(framework base)` |

## IntegralDomains {#cat-integraldomains}

| field | value |
| --- | --- |
| module | `integral_domains` |
| role | public named category class |
| implementation | Python class |
| defined by | Domains + axiom Commutative |
| direct defining axiom | [`Commutative`](axioms.md#ax-commutative) |
| syntactic axiom chain | [`Distributive`](axioms.md#ax-distributive), [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveCommutative`](axioms.md#ax-additivecommutative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`Associative`](axioms.md#ax-associative), [`AdditiveInverse`](axioms.md#ax-additiveinverse), [`Unital`](axioms.md#ax-unital), [`NoZeroDivisors`](axioms.md#ax-nozerodivisors), [`Commutative`](axioms.md#ax-commutative) |
| bound as | `Domains.Commutative` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/integral_domains.py:41`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/integral_domains.py#L41) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `IntegralDomains` | `integral_domains` | `(framework base)` |
| `IntegralDomains_with_category` | `integral_domains` | `(framework base)` |

## IsomorphicObjectsCategory {#cat-isomorphicobjectscategory}

| field | value |
| --- | --- |
| module | `isomorphic_objects` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`RegressiveCovariantConstructionCategory`](categories.md#cat-regressivecovariantconstructioncategory) |
| source | [`src/sage/categories/isomorphic_objects.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/isomorphic_objects.py#L19) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `IsomorphicObjectsCategory` | `isomorphic_objects` | `(framework base)` |

## JTrivialSemigroups {#cat-jtrivialsemigroups}

| field | value |
| --- | --- |
| module | `j_trivial_semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | Semigroups + axiom JTrivial |
| direct defining axiom | [`JTrivial`](axioms.md#ax-jtrivial) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`JTrivial`](axioms.md#ax-jtrivial) |
| bound as | `Semigroups.JTrivial` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/j_trivial_semigroups.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/j_trivial_semigroups.py#L18) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `JTrivialSemigroups` | `j_trivial_semigroups` | `(framework base)` |

## Jacobians {#cat-jacobians}

| field | value |
| --- | --- |
| module | `schemes` |
| role | public named category class |
| implementation | Python class |
| bases | [`Schemes_over_base`](categories.md#cat-schemes-over-base) |
| source | [`src/sage/categories/schemes.py:308`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L308) |
| loads at 10.10 | yes |

## JoinCategory {#cat-joincategory}

| field | value |
| --- | --- |
| module | `category` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`CategoryWithParameters`](categories.md#cat-categorywithparameters) |
| source | [`src/sage/categories/category.py:2978`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category.py#L2978) |
| loads at 10.10 | yes |

## KacMoodyAlgebras {#cat-kacmoodyalgebras}

| field | value |
| --- | --- |
| module | `kac_moody_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/kac_moody_algebras.py:23`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/kac_moody_algebras.py#L23) |
| loads at 10.10 | yes |

## KahlerAlgebras {#cat-kahleralgebras}

| field | value |
| --- | --- |
| module | `kahler_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/kahler_algebras.py:24`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/kahler_algebras.py#L24) |
| loads at 10.10 | yes |

## KirillovReshetikhinCrystals {#cat-kirillovreshetikhincrystals}

| field | value |
| --- | --- |
| module | `loop_crystals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/loop_crystals.py:170`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/loop_crystals.py#L170) |
| loads at 10.10 | yes |

### Local construction paths

- `TensorProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/loop_crystals.py:715`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/loop_crystals.py#L715) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `KirillovReshetikhinCrystals.TensorProducts` | `loop_crystals` | `TensorProducts` |

## LTrivialSemigroups {#cat-ltrivialsemigroups}

| field | value |
| --- | --- |
| module | `l_trivial_semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | Semigroups + axiom LTrivial |
| direct defining axiom | [`LTrivial`](axioms.md#ax-ltrivial) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`LTrivial`](axioms.md#ax-ltrivial) |
| bound as | `Semigroups.LTrivial` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/l_trivial_semigroups.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/l_trivial_semigroups.py#L19) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `LTrivialSemigroups` | `l_trivial_semigroups` | `(framework base)` |

## LambdaBracketAlgebras {#cat-lambdabracketalgebras}

| field | value |
| --- | --- |
| module | `lambda_bracket_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/lambda_bracket_algebras.py:30`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras.py#L30) |
| loads at 10.10 | yes |

### Local axiom paths

- `FinitelyGeneratedAsLambdaBracketAlgebra`
- `WithBasis`

### Other local category paths

- `FinitelyGenerated`

### Declared features (4)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| `FinitelyGenerated` | derived category shorthand | subcategory interface method | `_with_axiom(FinitelyGeneratedAsLambdaBracketAlgebra)` | [`src/sage/categories/lambda_bracket_algebras.py:98`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras.py#L98) |
| [`FinitelyGeneratedAsLambdaBracketAlgebra`](axioms.md#ax-finitelygeneratedaslambdabracketalgebra) | axiom | lazy-import binding | `sage.categories.finitely_generated_lambda_bracket_algebras.FinitelyGeneratedLambdaBracketAlgebras` | [`src/sage/categories/lambda_bracket_algebras.py:276`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras.py#L276) |
| [`FinitelyGeneratedAsLambdaBracketAlgebra`](axioms.md#ax-finitelygeneratedaslambdabracketalgebra) | axiom | subcategory interface method | `_with_axiom(FinitelyGeneratedAsLambdaBracketAlgebra)` | [`src/sage/categories/lambda_bracket_algebras.py:87`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras.py#L87) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | lazy-import binding | `sage.categories.lambda_bracket_algebras_with_basis.LambdaBracketAlgebrasWithBasis` | [`src/sage/categories/lambda_bracket_algebras.py:273`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras.py#L273) |

## LambdaBracketAlgebrasWithBasis {#cat-lambdabracketalgebraswithbasis}

| field | value |
| --- | --- |
| module | `lambda_bracket_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | LambdaBracketAlgebras + axiom WithBasis |
| direct defining axiom | [`WithBasis`](axioms.md#ax-withbasis) |
| syntactic axiom chain | [`WithBasis`](axioms.md#ax-withbasis) |
| bound as | `LambdaBracketAlgebras.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/lambda_bracket_algebras_with_basis.py:23`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras_with_basis.py#L23) |
| loads at 10.10 | yes |

### Local axiom paths

- `FinitelyGeneratedAsLambdaBracketAlgebra`

### Local construction paths

- `FinitelyGeneratedAsLambdaBracketAlgebra.Graded`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`FinitelyGeneratedAsLambdaBracketAlgebra`](axioms.md#ax-finitelygeneratedaslambdabracketalgebra) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/lambda_bracket_algebras_with_basis.py:61`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras_with_basis.py#L61) |
| [`Graded`](constructions.md#con-graded) | functorial construction | nested category class | `GradedModulesCategory` | [`src/sage/categories/lambda_bracket_algebras_with_basis.py:79`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras_with_basis.py#L79) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `LambdaBracketAlgebrasWithBasis` | `lambda_bracket_algebras_with_basis` | `(framework base)` |
| `LambdaBracketAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra` | `lambda_bracket_algebras_with_basis` | `FinitelyGeneratedAsLambdaBracketAlgebra` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `LambdaBracketAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Graded` | `lambda_bracket_algebras_with_basis` | `Graded` |

## LatticePosets {#cat-latticeposets}

| field | value |
| --- | --- |
| module | `lattice_posets` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/lattice_posets.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L19) |
| loads at 10.10 | yes |

### Local axiom paths

- `ChainGraded`
- `CongruenceUniform`
- `Distributive`
- `Extremal`
- `Finite`
- `Semidistributive`
- `Stone`
- `Trim`
- `Trim.ChainGraded`

### Declared features (15)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`ChainGraded`](axioms.md#ax-chaingraded) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:536`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L536) |
| [`ChainGraded`](axioms.md#ax-chaingraded) | axiom | subcategory interface method | `_with_axiom(ChainGraded)` | [`src/sage/categories/lattice_posets.py:93`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L93) |
| [`CongruenceUniform`](axioms.md#ax-congruenceuniform) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:457`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L457) |
| [`CongruenceUniform`](axioms.md#ax-congruenceuniform) | axiom | subcategory interface method | `_with_axiom(CongruenceUniform)` | [`src/sage/categories/lattice_posets.py:144`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L144) |
| [`Distributive`](axioms.md#ax-distributive) | axiom | subcategory interface method | `_with_axiom(ChainGraded) then _with_axiom(Trim)` | [`src/sage/categories/lattice_posets.py:123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L123) |
| [`Extremal`](axioms.md#ax-extremal) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:214`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L214) |
| [`Extremal`](axioms.md#ax-extremal) | axiom | subcategory interface method | `_with_axiom(Extremal)` | [`src/sage/categories/lattice_posets.py:195`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L195) |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_lattice_posets.FiniteLatticePosets` | [`src/sage/categories/lattice_posets.py:211`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L211) |
| [`Semidistributive`](axioms.md#ax-semidistributive) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:278`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L278) |
| [`Semidistributive`](axioms.md#ax-semidistributive) | axiom | subcategory interface method | `_with_axiom(Semidistributive)` | [`src/sage/categories/lattice_posets.py:158`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L158) |
| [`Stone`](axioms.md#ax-stone) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:496`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L496) |
| [`Stone`](axioms.md#ax-stone) | axiom | subcategory interface method | `_with_axiom(Stone)` | [`src/sage/categories/lattice_posets.py:108`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L108) |
| [`Trim`](axioms.md#ax-trim) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:239`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L239) |
| [`Trim`](axioms.md#ax-trim) | axiom | subcategory interface method | `_with_axiom(Trim)` | [`src/sage/categories/lattice_posets.py:180`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L180) |
| [`ChainGraded`](axioms.md#ax-chaingraded) | axiom | module-level binding | `DistributiveLattices` | [`src/sage/categories/lattice_posets.py:619`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L619) |

### Axiom-generated classes at 10.10 (6)

| class | module | axiom |
| --- | --- | --- |
| `LatticePosets.ChainGraded` | `lattice_posets` | `ChainGraded` |
| `LatticePosets.CongruenceUniform` | `lattice_posets` | `CongruenceUniform` |
| `LatticePosets.Extremal` | `lattice_posets` | `Extremal` |
| `LatticePosets.Semidistributive` | `lattice_posets` | `Semidistributive` |
| `LatticePosets.Stone` | `lattice_posets` | `Stone` |
| `LatticePosets.Trim` | `lattice_posets` | `Trim` |

## LeftModules {#cat-leftmodules}

| field | value |
| --- | --- |
| module | `left_modules` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/left_modules.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/left_modules.py#L16) |
| loads at 10.10 | yes |

## LieAlgebras {#cat-liealgebras}

| field | value |
| --- | --- |
| module | `lie_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/lie_algebras.py:34`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L34) |
| loads at 10.10 | yes |

### Local axiom paths

- `FiniteDimensional`
- `Nilpotent`
- `WithBasis`
- `FiniteDimensional.WithBasis`

### Local construction paths

- `Graded`

### Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/lie_algebras.py:174`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L174) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | lazy-import binding | `sage.categories.finite_dimensional_lie_algebras_with_basis.FiniteDimensionalLieAlgebrasWithBasis` | [`src/sage/categories/lie_algebras.py:175`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L175) |
| [`Graded`](constructions.md#con-graded) | functorial construction | lazy-import binding | `sage.categories.graded_lie_algebras.GradedLieAlgebras` | [`src/sage/categories/lie_algebras.py:112`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L112) |
| [`Nilpotent`](axioms.md#ax-nilpotent) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/lie_algebras.py:203`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L203) |
| [`Nilpotent`](axioms.md#ax-nilpotent) | axiom | subcategory interface method | `_with_axiom(Nilpotent)` | [`src/sage/categories/lie_algebras.py:94`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L94) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | lazy-import binding | `sage.categories.lie_algebras_with_basis.LieAlgebrasWithBasis` | [`src/sage/categories/lie_algebras.py:171`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L171) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `LieAlgebras.FiniteDimensional` | `lie_algebras` | `FiniteDimensional` |
| `LieAlgebras.Nilpotent` | `lie_algebras` | `Nilpotent` |

## LieAlgebrasWithBasis {#cat-liealgebraswithbasis}

| field | value |
| --- | --- |
| module | `lie_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | LieAlgebras + axiom WithBasis |
| direct defining axiom | [`WithBasis`](axioms.md#ax-withbasis) |
| syntactic axiom chain | [`WithBasis`](axioms.md#ax-withbasis) |
| bound as | `LieAlgebras.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/lie_algebras_with_basis.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras_with_basis.py#L25) |
| loads at 10.10 | yes |

### Local construction paths

- `Graded`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Graded`](constructions.md#con-graded) | functorial construction | lazy-import binding | `sage.categories.graded_lie_algebras_with_basis.GradedLieAlgebrasWithBasis` | [`src/sage/categories/lie_algebras_with_basis.py:55`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras_with_basis.py#L55) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `LieAlgebrasWithBasis` | `lie_algebras_with_basis` | `(framework base)` |

## LieConformalAlgebras {#cat-lieconformalalgebras}

| field | value |
| --- | --- |
| module | `lie_conformal_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/lie_conformal_algebras.py:133`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras.py#L133) |
| loads at 10.10 | yes |

### Local axiom paths

- `FinitelyGeneratedAsLambdaBracketAlgebra`
- `WithBasis`

### Local construction paths

- `Graded`
- `Super`

### Declared features (4)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`FinitelyGeneratedAsLambdaBracketAlgebra`](axioms.md#ax-finitelygeneratedaslambdabracketalgebra) | axiom | lazy-import binding | `sage.categories.finitely_generated_lie_conformal_algebras.FinitelyGeneratedLieConformalAlgebras` | [`src/sage/categories/lie_conformal_algebras.py:347`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras.py#L347) |
| [`Graded`](constructions.md#con-graded) | functorial construction | lazy-import binding | `sage.categories.graded_lie_conformal_algebras.GradedLieConformalAlgebras` | [`src/sage/categories/lie_conformal_algebras.py:338`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras.py#L338) |
| [`Super`](constructions.md#con-super) | functorial construction | lazy-import binding | `sage.categories.super_lie_conformal_algebras.SuperLieConformalAlgebras` | [`src/sage/categories/lie_conformal_algebras.py:341`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras.py#L341) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | lazy-import binding | `sage.categories.lie_conformal_algebras_with_basis.LieConformalAlgebrasWithBasis` | [`src/sage/categories/lie_conformal_algebras.py:344`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras.py#L344) |

## LieConformalAlgebrasWithBasis {#cat-lieconformalalgebraswithbasis}

| field | value |
| --- | --- |
| module | `lie_conformal_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | LieConformalAlgebras + axiom WithBasis |
| direct defining axiom | [`WithBasis`](axioms.md#ax-withbasis) |
| syntactic axiom chain | [`WithBasis`](axioms.md#ax-withbasis) |
| bound as | `LieConformalAlgebras.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/lie_conformal_algebras_with_basis.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L25) |
| loads at 10.10 | yes |

### Local axiom paths

- `FinitelyGeneratedAsLambdaBracketAlgebra`

### Local construction paths

- `Graded`
- `Super`
- `FinitelyGeneratedAsLambdaBracketAlgebra.Graded`
- `FinitelyGeneratedAsLambdaBracketAlgebra.Super`
- `Super.Graded`
- `FinitelyGeneratedAsLambdaBracketAlgebra.Super.Graded`

### Declared features (7)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`FinitelyGeneratedAsLambdaBracketAlgebra`](axioms.md#ax-finitelygeneratedaslambdabracketalgebra) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/lie_conformal_algebras_with_basis.py:85`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L85) |
| [`Graded`](constructions.md#con-graded) | functorial construction | nested category class | `GradedLieConformalAlgebrasCategory` | [`src/sage/categories/lie_conformal_algebras_with_basis.py:136`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L136) |
| [`Super`](constructions.md#con-super) | functorial construction | nested category class | `SuperModulesCategory` | [`src/sage/categories/lie_conformal_algebras_with_basis.py:99`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L99) |
| [`Graded`](constructions.md#con-graded) | functorial construction | nested category class | `GradedModulesCategory` | [`src/sage/categories/lie_conformal_algebras_with_basis.py:110`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L110) |
| [`Graded`](constructions.md#con-graded) | functorial construction | nested category class | `GradedLieConformalAlgebrasCategory` | [`src/sage/categories/lie_conformal_algebras_with_basis.py:75`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L75) |
| [`Super`](constructions.md#con-super) | functorial construction | nested category class | `SuperModulesCategory` | [`src/sage/categories/lie_conformal_algebras_with_basis.py:34`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L34) |
| [`Graded`](constructions.md#con-graded) | functorial construction | nested category class | `GradedLieConformalAlgebrasCategory` | [`src/sage/categories/lie_conformal_algebras_with_basis.py:64`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras_with_basis.py#L64) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `LieConformalAlgebrasWithBasis` | `lie_conformal_algebras_with_basis` | `(framework base)` |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra` | `lie_conformal_algebras_with_basis` | `FinitelyGeneratedAsLambdaBracketAlgebra` |

### Construction-generated classes at 10.10 (6)

| class | module | construction |
| --- | --- | --- |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Graded` | `lie_conformal_algebras_with_basis` | `Graded` |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Super` | `lie_conformal_algebras_with_basis` | `Super` |
| `LieConformalAlgebrasWithBasis.FinitelyGeneratedAsLambdaBracketAlgebra.Super.Graded` | `lie_conformal_algebras_with_basis` | `Graded` |
| `LieConformalAlgebrasWithBasis.Graded` | `lie_conformal_algebras_with_basis` | `Graded` |
| `LieConformalAlgebrasWithBasis.Super` | `lie_conformal_algebras_with_basis` | `Super` |
| `LieConformalAlgebrasWithBasis.Super.Graded` | `lie_conformal_algebras_with_basis` | `Graded` |

## LieGroups {#cat-liegroups}

| field | value |
| --- | --- |
| module | `lie_groups` |
| role | public named category class |
| implementation | Python class |
| defined by | bound from Groups |
| bound as | `Groups.Lie` |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/lie_groups.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_groups.py#L18) |
| loads at 10.10 | yes |

## LoopCrystals {#cat-loopcrystals}

| field | value |
| --- | --- |
| module | `loop_crystals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/loop_crystals.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/loop_crystals.py#L25) |
| loads at 10.10 | yes |

## Magmas {#cat-magmas}

| field | value |
| --- | --- |
| module | `magmas` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/magmas.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L25) |
| loads at 10.10 | yes |

### Local axiom paths

- `Associative`
- `Commutative`
- `Distributive`
- `FinitelyGeneratedAsMagma`
- `JTrivial`
- `Unital`
- `Unital.Inverse`

### Local construction paths

- `Algebras`
- `CartesianProducts`
- `Realizations`
- `Subquotients`
- `Commutative.Algebras`
- `Commutative.CartesianProducts`
- `Unital.Algebras`
- `Unital.CartesianProducts`
- `Unital.Realizations`
- `Unital.Inverse.CartesianProducts`

### Other local category paths

- `FinitelyGenerated`

### Declared features (24)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/magmas.py:349`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L349) |
| [`Associative`](axioms.md#ax-associative) | axiom | lazy-import binding | `sage.categories.semigroups.Semigroups` | [`src/sage/categories/magmas.py:342`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L342) |
| [`Associative`](axioms.md#ax-associative) | axiom | subcategory interface method | `_with_axiom(Associative)` | [`src/sage/categories/magmas.py:75`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L75) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/magmas.py:1038`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L1038) |
| [`Commutative`](axioms.md#ax-commutative) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/magmas.py:401`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L401) |
| [`Commutative`](axioms.md#ax-commutative) | axiom | subcategory interface method | `_with_axiom(Commutative)` | [`src/sage/categories/magmas.py:101`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L101) |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/magmas.py:415`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L415) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/magmas.py:441`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L441) |
| [`Distributive`](axioms.md#ax-distributive) | axiom | subcategory interface method | `calls AdditiveMagmas(), MagmasAndAdditiveMagmas()` | [`src/sage/categories/magmas.py:265`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L265) |
| `FinitelyGenerated` | derived category shorthand | subcategory interface method | `calls FinitelyGeneratedAsMagma(), AdditiveMagmas()` | [`src/sage/categories/magmas.py:222`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L222) |
| [`FinitelyGeneratedAsMagma`](axioms.md#ax-finitelygeneratedasmagma) | axiom | lazy-import binding | `sage.categories.finitely_generated_magmas.FinitelyGeneratedMagmas` | [`src/sage/categories/magmas.py:343`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L343) |
| [`FinitelyGeneratedAsMagma`](axioms.md#ax-finitelygeneratedasmagma) | axiom | subcategory interface method | `_with_axiom(FinitelyGeneratedAsMagma)` | [`src/sage/categories/magmas.py:165`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L165) |
| [`JTrivial`](axioms.md#ax-jtrivial) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/magmas.py:345`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L345) |
| [`JTrivial`](axioms.md#ax-jtrivial) | axiom | subcategory interface method | `_with_axiom(JTrivial)` | [`src/sage/categories/magmas.py:320`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L320) |
| [`Realizations`](constructions.md#con-realizations) | functorial construction | nested category class | `RealizationsCategory` | [`src/sage/categories/magmas.py:1154`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L1154) |
| [`Subquotients`](constructions.md#con-subquotients) | functorial construction | nested category class | `SubquotientsCategory` | [`src/sage/categories/magmas.py:1103`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L1103) |
| [`Unital`](axioms.md#ax-unital) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/magmas.py:457`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L457) |
| [`Unital`](axioms.md#ax-unital) | axiom | subcategory interface method | `_with_axiom(Unital)` | [`src/sage/categories/magmas.py:129`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L129) |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/magmas.py:694`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L694) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/magmas.py:615`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L615) |
| [`Inverse`](axioms.md#ax-inverse) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/magmas.py:598`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L598) |
| [`Inverse`](axioms.md#ax-inverse) | axiom | subcategory interface method | `_with_axiom(Inverse)` | [`src/sage/categories/magmas.py:570`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L570) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/magmas.py:599`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L599) |
| [`Realizations`](constructions.md#con-realizations) | functorial construction | nested category class | `RealizationsCategory` | [`src/sage/categories/magmas.py:720`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L720) |

### Axiom-generated classes at 10.10 (6)

| class | module | axiom |
| --- | --- | --- |
| `Magmas.Commutative` | `magmas` | `Commutative` |
| `Magmas.Commutative_with_category` | `magmas` | `Commutative_with_category` |
| `Magmas.JTrivial` | `magmas` | `JTrivial` |
| `Magmas.Unital` | `magmas` | `Unital` |
| `Magmas.Unital.Inverse` | `magmas` | `Inverse` |
| `Magmas.Unital_with_category` | `magmas` | `Unital_with_category` |

### Construction-generated classes at 10.10 (11)

| class | module | construction |
| --- | --- | --- |
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

## MagmasAndAdditiveMagmas {#cat-magmasandadditivemagmas}

| field | value |
| --- | --- |
| module | `magmas_and_additive_magmas` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/magmas_and_additive_magmas.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L19) |
| loads at 10.10 | yes |

### Local axiom paths

- `Distributive`

### Local construction paths

- `CartesianProducts`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/magmas_and_additive_magmas.py:136`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L136) |
| [`Distributive`](axioms.md#ax-distributive) | axiom | lazy-import binding | `sage.categories.distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas` | [`src/sage/categories/magmas_and_additive_magmas.py:134`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L134) |
| [`Distributive`](axioms.md#ax-distributive) | axiom | subcategory interface method | `_with_axiom(Distributive)` | [`src/sage/categories/magmas_and_additive_magmas.py:59`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L59) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `MagmasAndAdditiveMagmas.CartesianProducts` | `magmas_and_additive_magmas` | `CartesianProducts` |

## MagmaticAlgebras {#cat-magmaticalgebras}

| field | value |
| --- | --- |
| module | `magmatic_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/magmatic_algebras.py:23`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L23) |
| loads at 10.10 | yes |

### Local axiom paths

- `Associative`
- `Unital`
- `WithBasis`
- `WithBasis.FiniteDimensional`

### Declared features (4)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Associative`](axioms.md#ax-associative) | axiom | lazy-import binding | `sage.categories.associative_algebras.AssociativeAlgebras` | [`src/sage/categories/magmatic_algebras.py:100`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L100) |
| [`Unital`](axioms.md#ax-unital) | axiom | lazy-import binding | `sage.categories.unital_algebras.UnitalAlgebras` | [`src/sage/categories/magmatic_algebras.py:101`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L101) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/magmatic_algebras.py:119`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L119) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/magmatic_algebras.py:224`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L224) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `MagmaticAlgebras.WithBasis` | `magmatic_algebras` | `WithBasis` |
| `MagmaticAlgebras.WithBasis.FiniteDimensional` | `magmatic_algebras` | `FiniteDimensional` |

## Manifolds {#cat-manifolds}

| field | value |
| --- | --- |
| module | `manifolds` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/manifolds.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L19) |
| loads at 10.10 | yes |

### Local axiom paths

- `AlmostComplex`
- `Analytic`
- `Connected`
- `Differentiable`
- `FiniteDimensional`
- `Smooth`

### Other local category paths

- `Complex`

### Declared features (13)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AlmostComplex`](axioms.md#ax-almostcomplex) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:288`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L288) |
| [`AlmostComplex`](axioms.md#ax-almostcomplex) | axiom | subcategory interface method | `_with_axiom(AlmostComplex)` | [`src/sage/categories/manifolds.py:199`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L199) |
| [`Analytic`](axioms.md#ax-analytic) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:267`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L267) |
| [`Analytic`](axioms.md#ax-analytic) | axiom | subcategory interface method | `_with_axiom(Analytic)` | [`src/sage/categories/manifolds.py:179`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L179) |
| `Complex` | derived category shorthand | subcategory interface method | `ComplexManifolds(self.base())._with_axioms(...); calls ComplexManifolds()` | [`src/sage/categories/manifolds.py:220`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L220) |
| [`Connected`](axioms.md#ax-connected) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:323`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L323) |
| [`Connected`](axioms.md#ax-connected) | axiom | subcategory interface method | `_with_axiom(Connected)` | [`src/sage/categories/manifolds.py:98`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L98) |
| [`Differentiable`](axioms.md#ax-differentiable) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:239`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L239) |
| [`Differentiable`](axioms.md#ax-differentiable) | axiom | subcategory interface method | `_with_axiom(Differentiable)` | [`src/sage/categories/manifolds.py:138`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L138) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:312`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L312) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | subcategory interface method | `_with_axiom(FiniteDimensional)` | [`src/sage/categories/manifolds.py:117`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L117) |
| [`Smooth`](axioms.md#ax-smooth) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:246`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L246) |
| [`Smooth`](axioms.md#ax-smooth) | axiom | subcategory interface method | `_with_axiom(Smooth)` | [`src/sage/categories/manifolds.py:159`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L159) |

### Axiom-generated classes at 10.10 (6)

| class | module | axiom |
| --- | --- | --- |
| `Manifolds.AlmostComplex` | `manifolds` | `AlmostComplex` |
| `Manifolds.Analytic` | `manifolds` | `Analytic` |
| `Manifolds.Connected` | `manifolds` | `Connected` |
| `Manifolds.Differentiable` | `manifolds` | `Differentiable` |
| `Manifolds.FiniteDimensional` | `manifolds` | `FiniteDimensional` |
| `Manifolds.Smooth` | `manifolds` | `Smooth` |

## MatrixAlgebras {#cat-matrixalgebras}

| field | value |
| --- | --- |
| module | `matrix_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/matrix_algebras.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/matrix_algebras.py#L17) |
| loads at 10.10 | yes |

## MetricSpaces {#cat-metricspaces}

| field | value |
| --- | --- |
| module | `metric_spaces` |
| role | public named category class |
| implementation | Python class |
| defined by | Sets.Metric() |
| defining construction | [`Metric`](constructions.md#con-metric) |
| bound as | `Sets.Metric` |
| bases | [`MetricSpacesCategory`](categories.md#cat-metricspacescategory) |
| source | [`src/sage/categories/metric_spaces.py:76`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L76) |
| loads at 10.10 | yes |

### Local axiom paths

- `Complete`

### Local construction paths

- `CartesianProducts`
- `Homsets`
- `WithRealizations`
- `Complete.CartesianProducts`

### Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/metric_spaces.py:283`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L283) |
| [`Complete`](axioms.md#ax-complete) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/metric_spaces.py:347`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L347) |
| [`Complete`](axioms.md#ax-complete) | axiom | subcategory interface method | `_with_axiom(Complete)` | [`src/sage/categories/metric_spaces.py:330`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L330) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/metric_spaces.py:352`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L352) |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/metric_spaces.py:224`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L224) |
| [`WithRealizations`](constructions.md#con-withrealizations) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/metric_spaces.py:263`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L263) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `MetricSpaces.Complete` | `metric_spaces` | `Complete` |
| `MetricSpaces.Complete_with_category` | `metric_spaces` | `Complete_with_category` |

### Construction-generated classes at 10.10 (6)

| class | module | construction |
| --- | --- | --- |
| `MetricSpaces` | `metric_spaces` | `(framework base)` |
| `MetricSpaces.CartesianProducts` | `metric_spaces` | `CartesianProducts` |
| `MetricSpaces.Complete.CartesianProducts` | `metric_spaces` | `CartesianProducts` |
| `MetricSpaces.Homsets` | `metric_spaces` | `Homsets` |
| `MetricSpaces.WithRealizations` | `metric_spaces` | `WithRealizations` |
| `MetricSpaces_with_category` | `metric_spaces` | `(framework base)` |

## MetricSpacesCategory {#cat-metricspacescategory}

| field | value |
| --- | --- |
| module | `metric_spaces` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`RegressiveCovariantConstructionCategory`](categories.md#cat-regressivecovariantconstructioncategory) |
| source | [`src/sage/categories/metric_spaces.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L20) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `MetricSpacesCategory` | `metric_spaces` | `(framework base)` |

## ModularAbelianVarieties {#cat-modularabelianvarieties}

| field | value |
| --- | --- |
| module | `modular_abelian_varieties` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base`](categories.md#cat-category-over-base) |
| source | [`src/sage/categories/modular_abelian_varieties.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modular_abelian_varieties.py#L20) |
| loads at 10.10 | yes |

### Local axiom paths

- `Homsets.Endset`

### Local construction paths

- `Homsets`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/modular_abelian_varieties.py:65`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modular_abelian_varieties.py#L65) |
| [`Endset`](axioms.md#ax-endset) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/modular_abelian_varieties.py:67`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modular_abelian_varieties.py#L67) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `ModularAbelianVarieties.Homsets.Endset` | `modular_abelian_varieties` | `Endset` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `ModularAbelianVarieties.Homsets` | `modular_abelian_varieties` | `Homsets` |

## Modules {#cat-modules}

| field | value |
| --- | --- |
| module | `modules` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_module`](categories.md#cat-category-module) |
| source | [`src/sage/categories/modules.py:33`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L33) |
| loads at 10.10 | yes |

### Local axiom paths

- `FiniteDimensional`
- `FinitelyPresented`
- `WithBasis`
- `Homsets.Endset`

### Local construction paths

- `CartesianProducts`
- `dual`
- `DualObjects`
- `Filtered`
- `Graded`
- `Homsets`
- `Super`
- `TensorProducts`
- `FiniteDimensional.TensorProducts`

### Declared features (20)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/modules.py:832`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L832) |
| [`DualObjects`](constructions.md#con-dualobjects) | functorial construction | subcategory interface method | `DualObjectsCategory.category_of(...)` | [`src/sage/categories/modules.py:263`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L263) |
| [`Filtered`](constructions.md#con-filtered) | functorial construction | lazy-import binding | `sage.categories.filtered_modules.FilteredModules` | [`src/sage/categories/modules.py:593`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L593) |
| [`Filtered`](constructions.md#con-filtered) | functorial construction | subcategory interface method | `FilteredModulesCategory.category_of(...)` | [`src/sage/categories/modules.py:384`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L384) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/modules.py:514`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L514) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | subcategory interface method | `_with_axiom(FiniteDimensional)` | [`src/sage/categories/modules.py:341`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L341) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/modules.py:545`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L545) |
| [`FinitelyPresented`](axioms.md#ax-finitelypresented) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/modules.py:562`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L562) |
| [`FinitelyPresented`](axioms.md#ax-finitelypresented) | axiom | subcategory interface method | `_with_axiom(FinitelyPresented)` | [`src/sage/categories/modules.py:363`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L363) |
| [`Graded`](constructions.md#con-graded) | functorial construction | lazy-import binding | `sage.categories.graded_modules.GradedModules` | [`src/sage/categories/modules.py:594`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L594) |
| [`Graded`](constructions.md#con-graded) | functorial construction | subcategory interface method | `GradedModulesCategory.category_of(...)` | [`src/sage/categories/modules.py:420`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L420) |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/modules.py:720`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L720) |
| [`Endset`](axioms.md#ax-endset) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/modules.py:810`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L810) |
| [`Super`](constructions.md#con-super) | functorial construction | lazy-import binding | `sage.categories.super_modules.SuperModules` | [`src/sage/categories/modules.py:595`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L595) |
| [`Super`](constructions.md#con-super) | functorial construction | subcategory interface method | `SuperModulesCategory.category_of(...)` | [`src/sage/categories/modules.py:456`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L456) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/modules.py:932`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L932) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | subcategory interface method | `TensorProductsCategory.category_of(...)` | [`src/sage/categories/modules.py:245`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L245) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | lazy-import binding | `sage.categories.modules_with_basis.ModulesWithBasis` | [`src/sage/categories/modules.py:597`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L597) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | subcategory interface method | `_with_axiom(WithBasis)` | [`src/sage/categories/modules.py:492`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L492) |
| [`DualObjects`](constructions.md#con-dualobjects) | functorial construction | subcategory API alias | `DualObjects` | [`src/sage/categories/modules.py:338`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L338) |

### Axiom-generated classes at 10.10 (3)

| class | module | axiom |
| --- | --- | --- |
| `Modules.FiniteDimensional` | `modules` | `FiniteDimensional` |
| `Modules.FinitelyPresented` | `modules` | `FinitelyPresented` |
| `Modules.Homsets.Endset` | `modules` | `Endset` |

### Construction-generated classes at 10.10 (4)

| class | module | construction |
| --- | --- | --- |
| `Modules.CartesianProducts` | `modules` | `CartesianProducts` |
| `Modules.FiniteDimensional.TensorProducts` | `modules` | `TensorProducts` |
| `Modules.Homsets` | `modules` | `Homsets` |
| `Modules.TensorProducts` | `modules` | `TensorProducts` |

## ModulesWithBasis {#cat-moduleswithbasis}

| field | value |
| --- | --- |
| module | `modules_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | Modules + axiom WithBasis |
| direct defining axiom | [`WithBasis`](axioms.md#ax-withbasis) |
| syntactic axiom chain | [`WithBasis`](axioms.md#ax-withbasis) |
| bound as | `Modules.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/modules_with_basis.py:44`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L44) |
| loads at 10.10 | yes |

### Local axiom paths

- `FiniteDimensional`

### Local construction paths

- `CartesianProducts`
- `DualObjects`
- `Filtered`
- `Graded`
- `Homsets`
- `Super`
- `TensorProducts`

### Declared features (8)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/modules_with_basis.py:2576`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L2576) |
| [`DualObjects`](constructions.md#con-dualobjects) | functorial construction | nested category class | `DualObjectsCategory` | [`src/sage/categories/modules_with_basis.py:2781`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L2781) |
| [`Filtered`](constructions.md#con-filtered) | functorial construction | lazy-import binding | `sage.categories.filtered_modules_with_basis.FilteredModulesWithBasis` | [`src/sage/categories/modules_with_basis.py:196`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L196) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | lazy-import binding | `sage.categories.finite_dimensional_modules_with_basis.FiniteDimensionalModulesWithBasis` | [`src/sage/categories/modules_with_basis.py:195`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L195) |
| [`Graded`](constructions.md#con-graded) | functorial construction | lazy-import binding | `sage.categories.graded_modules_with_basis.GradedModulesWithBasis` | [`src/sage/categories/modules_with_basis.py:197`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L197) |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/modules_with_basis.py:2458`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L2458) |
| [`Super`](constructions.md#con-super) | functorial construction | lazy-import binding | `sage.categories.super_modules_with_basis.SuperModulesWithBasis` | [`src/sage/categories/modules_with_basis.py:198`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L198) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/modules_with_basis.py:2621`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L2621) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `ModulesWithBasis` | `modules_with_basis` | `(framework base)` |

### Construction-generated classes at 10.10 (4)

| class | module | construction |
| --- | --- | --- |
| `ModulesWithBasis.CartesianProducts` | `modules_with_basis` | `CartesianProducts` |
| `ModulesWithBasis.DualObjects` | `modules_with_basis` | `DualObjects` |
| `ModulesWithBasis.Homsets` | `modules_with_basis` | `Homsets` |
| `ModulesWithBasis.TensorProducts` | `modules_with_basis` | `TensorProducts` |

## MonoidAlgebras(base_ring) {#cat-monoidalgebras-base-ring}

| field | value |
| --- | --- |
| module | `monoid_algebras` |
| role | public category-valued wrapper constructor |
| implementation | Python function |
| defined by | Monoids().Algebras(base_ring) |
| source | [`src/sage/categories/monoid_algebras.py:14`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoid_algebras.py#L14) |
| loads at 10.10 | no |
| notes | Returns a dynamically constructed category rather than an instance of a dedicated class. |

## Monoids {#cat-monoids}

| field | value |
| --- | --- |
| module | `monoids` |
| role | public named category class |
| implementation | Python class |
| defined by | Semigroups + axiom Unital |
| direct defining axiom | [`Unital`](axioms.md#ax-unital) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`Unital`](axioms.md#ax-unital) |
| bound as | `Semigroups.Unital` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/monoids.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L27) |
| loads at 10.10 | yes |

### Local axiom paths

- `Commutative`
- `Finite`
- `Inverse`

### Local construction paths

- `Algebras`
- `CartesianProducts`
- `Subquotients`
- `WithRealizations`

### Declared features (7)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/monoids.py:484`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L484) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/monoids.py:626`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L626) |
| [`Commutative`](axioms.md#ax-commutative) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/monoids.py:391`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L391) |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_monoids.FiniteMonoids` | [`src/sage/categories/monoids.py:77`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L77) |
| [`Inverse`](axioms.md#ax-inverse) | axiom | lazy-import binding | `sage.categories.groups.Groups` | [`src/sage/categories/monoids.py:78`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L78) |
| [`Subquotients`](constructions.md#con-subquotients) | functorial construction | nested category class | `SubquotientsCategory` | [`src/sage/categories/monoids.py:468`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L468) |
| [`WithRealizations`](constructions.md#con-withrealizations) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/monoids.py:439`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L439) |

### Axiom-generated classes at 10.10 (4)

| class | module | axiom |
| --- | --- | --- |
| `Monoids` | `monoids` | `(framework base)` |
| `Monoids.Commutative` | `monoids` | `Commutative` |
| `Monoids.Commutative_with_category` | `monoids` | `Commutative_with_category` |
| `Monoids_with_category` | `monoids` | `(framework base)` |

### Construction-generated classes at 10.10 (5)

| class | module | construction |
| --- | --- | --- |
| `Monoids.Algebras` | `monoids` | `Algebras` |
| `Monoids.CartesianProducts` | `monoids` | `CartesianProducts` |
| `Monoids.Subquotients` | `monoids` | `Subquotients` |
| `Monoids.Subquotients_with_category` | `monoids` | `Subquotients_with_category` |
| `Monoids.WithRealizations` | `monoids` | `WithRealizations` |

## NoetherianRings {#cat-noetherianrings}

| field | value |
| --- | --- |
| module | `noetherian_rings` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/noetherian_rings.py:30`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/noetherian_rings.py#L30) |
| loads at 10.10 | yes |

## NumberFields {#cat-numberfields}

| field | value |
| --- | --- |
| module | `number_fields` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/number_fields.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/number_fields.py#L18) |
| loads at 10.10 | yes |

## Objects {#cat-objects}

| field | value |
| --- | --- |
| module | `objects` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/objects.py:24`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/objects.py#L24) |
| loads at 10.10 | yes |

### Local construction paths

- `Homsets`

### Other local category paths

- `Endsets`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| `Endsets` | derived category shorthand | subcategory interface method | `_with_axiom(Endset); calls Homsets()` | [`src/sage/categories/objects.py:145`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/objects.py#L145) |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | subcategory interface method | `HomsetsCategory.category_of(...)` | [`src/sage/categories/objects.py:82`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/objects.py#L82) |

## OreModules {#cat-oremodules}

| field | value |
| --- | --- |
| module | `ore_modules` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/ore_modules.py:26`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/ore_modules.py#L26) |
| loads at 10.10 | yes |

## PartiallyOrderedMonoids {#cat-partiallyorderedmonoids}

| field | value |
| --- | --- |
| module | `partially_ordered_monoids` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/partially_ordered_monoids.py:15`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/partially_ordered_monoids.py#L15) |
| loads at 10.10 | yes |

## PermutationGroups {#cat-permutationgroups}

| field | value |
| --- | --- |
| module | `permutation_groups` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/permutation_groups.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/permutation_groups.py#L17) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_permutation_groups.FinitePermutationGroups` | [`src/sage/categories/permutation_groups.py:62`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/permutation_groups.py#L62) |

## PointedSets {#cat-pointedsets}

| field | value |
| --- | --- |
| module | `pointed_sets` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/pointed_sets.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/pointed_sets.py#L17) |
| loads at 10.10 | yes |

## PolyhedralSets {#cat-polyhedralsets}

| field | value |
| --- | --- |
| module | `polyhedra` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/polyhedra.py:15`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/polyhedra.py#L15) |
| loads at 10.10 | yes |

## Posets {#cat-posets}

| field | value |
| --- | --- |
| module | `posets` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/posets.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L19) |
| loads at 10.10 | yes |

### Local axiom paths

- `Bounded`
- `Finite`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Bounded`](axioms.md#ax-bounded) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/posets.py:736`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L736) |
| [`Bounded`](axioms.md#ax-bounded) | axiom | subcategory interface method | `_with_axiom(Bounded)` | [`src/sage/categories/posets.py:723`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L723) |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_posets.FinitePosets` | [`src/sage/categories/posets.py:155`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L155) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `Posets.Bounded` | `posets` | `Bounded` |

## PrincipalIdealDomains {#cat-principalidealdomains}

| field | value |
| --- | --- |
| module | `principal_ideal_domains` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/principal_ideal_domains.py:15`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/principal_ideal_domains.py#L15) |
| loads at 10.10 | yes |

## QuantumGroupRepresentations {#cat-quantumgrouprepresentations}

| field | value |
| --- | --- |
| module | `quantum_group_representations` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_module`](categories.md#cat-category-module) |
| source | [`src/sage/categories/quantum_group_representations.py:28`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quantum_group_representations.py#L28) |
| loads at 10.10 | yes |

### Local axiom paths

- `WithBasis`

### Local construction paths

- `TensorProducts`
- `WithBasis.TensorProducts`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/quantum_group_representations.py:369`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quantum_group_representations.py#L369) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/quantum_group_representations.py:63`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quantum_group_representations.py#L63) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/quantum_group_representations.py:68`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quantum_group_representations.py#L68) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `QuantumGroupRepresentations.WithBasis` | `quantum_group_representations` | `WithBasis` |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `QuantumGroupRepresentations.TensorProducts` | `quantum_group_representations` | `TensorProducts` |
| `QuantumGroupRepresentations.WithBasis.TensorProducts` | `quantum_group_representations` | `TensorProducts` |

## QuotientFields {#cat-quotientfields}

| field | value |
| --- | --- |
| module | `quotient_fields` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/quotient_fields.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quotient_fields.py#L18) |
| loads at 10.10 | yes |

## QuotientsCategory {#cat-quotientscategory}

| field | value |
| --- | --- |
| module | `quotients` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`RegressiveCovariantConstructionCategory`](categories.md#cat-regressivecovariantconstructioncategory) |
| source | [`src/sage/categories/quotients.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quotients.py#L19) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `QuotientsCategory` | `quotients` | `(framework base)` |

## RTrivialSemigroups {#cat-rtrivialsemigroups}

| field | value |
| --- | --- |
| module | `r_trivial_semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | Semigroups + axiom RTrivial |
| direct defining axiom | [`RTrivial`](axioms.md#ax-rtrivial) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative), [`RTrivial`](axioms.md#ax-rtrivial) |
| bound as | `Semigroups.RTrivial` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/r_trivial_semigroups.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/r_trivial_semigroups.py#L18) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `RTrivialSemigroups` | `r_trivial_semigroups` | `(framework base)` |

## RealizationsCategory {#cat-realizationscategory}

| field | value |
| --- | --- |
| module | `realizations` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`RegressiveCovariantConstructionCategory`](categories.md#cat-regressivecovariantconstructioncategory) |
| source | [`src/sage/categories/realizations.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/realizations.py#L25) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `RealizationsCategory` | `realizations` | `(framework base)` |

## RegressiveCovariantConstructionCategory {#cat-regressivecovariantconstructioncategory}

| field | value |
| --- | --- |
| module | `covariant_functorial_construction` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`CovariantConstructionCategory`](categories.md#cat-covariantconstructioncategory) |
| source | [`src/sage/categories/covariant_functorial_construction.py:658`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/covariant_functorial_construction.py#L658) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `RegressiveCovariantConstructionCategory` | `covariant_functorial_construction` | `(framework base)` |

## RegularCrystals {#cat-regularcrystals}

| field | value |
| --- | --- |
| module | `regular_crystals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/regular_crystals.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/regular_crystals.py#L27) |
| loads at 10.10 | yes |

### Local construction paths

- `TensorProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/regular_crystals.py:880`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/regular_crystals.py#L880) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `RegularCrystals.TensorProducts` | `regular_crystals` | `TensorProducts` |

## RegularLoopCrystals {#cat-regularloopcrystals}

| field | value |
| --- | --- |
| module | `loop_crystals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/loop_crystals.py:132`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/loop_crystals.py#L132) |
| loads at 10.10 | yes |

## RegularSuperCrystals {#cat-regularsupercrystals}

| field | value |
| --- | --- |
| module | `regular_supercrystals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/regular_supercrystals.py:24`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/regular_supercrystals.py#L24) |
| loads at 10.10 | yes |

### Local construction paths

- `TensorProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/regular_supercrystals.py:155`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/regular_supercrystals.py#L155) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `RegularSuperCrystals.TensorProducts` | `regular_supercrystals` | `TensorProducts` |

## RightModules {#cat-rightmodules}

| field | value |
| --- | --- |
| module | `right_modules` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/right_modules.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/right_modules.py#L16) |
| loads at 10.10 | yes |

## RingIdeals {#cat-ringideals}

| field | value |
| --- | --- |
| module | `ring_ideals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_ideal`](categories.md#cat-category-ideal) |
| source | [`src/sage/categories/ring_ideals.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/ring_ideals.py#L20) |
| loads at 10.10 | yes |

## Rings {#cat-rings}

| field | value |
| --- | --- |
| module | `rings` |
| role | public named category class |
| implementation | Python class |
| defined by | Rngs + axiom Unital |
| direct defining axiom | [`Unital`](axioms.md#ax-unital) |
| syntactic axiom chain | [`Distributive`](axioms.md#ax-distributive), [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveCommutative`](axioms.md#ax-additivecommutative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`Associative`](axioms.md#ax-associative), [`AdditiveInverse`](axioms.md#ax-additiveinverse), [`Unital`](axioms.md#ax-unital) |
| bound as | `Rngs.Unital` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/rings.py:24`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L24) |
| loads at 10.10 | yes |

### Local axiom paths

- `Commutative`
- `Division`
- `NoZeroDivisors`

### Declared features (5)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Commutative`](axioms.md#ax-commutative) | axiom | lazy-import binding | `sage.categories.commutative_rings.CommutativeRings` | [`src/sage/categories/rings.py:311`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L311) |
| [`Division`](axioms.md#ax-division) | axiom | lazy-import binding | `sage.categories.division_rings.DivisionRings` | [`src/sage/categories/rings.py:310`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L310) |
| [`Division`](axioms.md#ax-division) | axiom | subcategory interface method | `_with_axiom(Division)` | [`src/sage/categories/rings.py:287`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L287) |
| [`NoZeroDivisors`](axioms.md#ax-nozerodivisors) | axiom | lazy-import binding | `sage.categories.domains.Domains` | [`src/sage/categories/rings.py:309`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L309) |
| [`NoZeroDivisors`](axioms.md#ax-nozerodivisors) | axiom | subcategory interface method | `_with_axiom(NoZeroDivisors)` | [`src/sage/categories/rings.py:264`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L264) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Rings` | `rings` | `(framework base)` |
| `Rings_with_category` | `rings` | `(framework base)` |

## Rngs {#cat-rngs}

| field | value |
| --- | --- |
| module | `rngs` |
| role | public named category class |
| implementation | Python class |
| defined by | MagmasAndAdditiveMagmas.Distributive.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative + axiom AdditiveInverse |
| direct defining axiom | [`AdditiveInverse`](axioms.md#ax-additiveinverse) |
| syntactic axiom chain | [`Distributive`](axioms.md#ax-distributive), [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveCommutative`](axioms.md#ax-additivecommutative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`Associative`](axioms.md#ax-associative), [`AdditiveInverse`](axioms.md#ax-additiveinverse) |
| bound as | `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative.AdditiveInverse` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/rngs.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rngs.py#L18) |
| loads at 10.10 | yes |

### Local axiom paths

- `Unital`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Unital`](axioms.md#ax-unital) | axiom | lazy-import binding | `sage.categories.rings.Rings` | [`src/sage/categories/rngs.py:51`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rngs.py#L51) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Rngs` | `rngs` | `(framework base)` |
| `Rngs_with_category` | `rngs` | `(framework base)` |

## Schemes {#cat-schemes}

| field | value |
| --- | --- |
| module | `schemes` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/schemes.py:33`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L33) |
| loads at 10.10 | yes |

## Schemes_over_base {#cat-schemes-over-base}

| field | value |
| --- | --- |
| module | `schemes` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`Category_over_base`](categories.md#cat-category-over-base) |
| source | [`src/sage/categories/schemes.py:159`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/schemes.py#L159) |
| loads at 10.10 | yes |

## Semigroups {#cat-semigroups}

| field | value |
| --- | --- |
| module | `semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | Magmas + axiom Associative |
| direct defining axiom | [`Associative`](axioms.md#ax-associative) |
| syntactic axiom chain | [`Associative`](axioms.md#ax-associative) |
| bound as | `Magmas.Associative` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/semigroups.py:30`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L30) |
| loads at 10.10 | yes |

### Local axiom paths

- `Aperiodic`
- `Finite`
- `FinitelyGeneratedAsMagma`
- `HTrivial`
- `JTrivial`
- `LTrivial`
- `RTrivial`
- `Unital`

### Local construction paths

- `Algebras`
- `CartesianProducts`
- `Quotients`
- `Subquotients`

### Declared features (17)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/semigroups.py:872`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L872) |
| [`Aperiodic`](axioms.md#ax-aperiodic) | axiom | lazy-import binding | `sage.categories.aperiodic_semigroups.AperiodicSemigroups` | [`src/sage/categories/semigroups.py:783`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L783) |
| [`Aperiodic`](axioms.md#ax-aperiodic) | axiom | subcategory interface method | `_with_axiom(Aperiodic)` | [`src/sage/categories/semigroups.py:729`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L729) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/semigroups.py:856`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L856) |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_semigroups.FiniteSemigroups` | [`src/sage/categories/semigroups.py:776`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L776) |
| [`FinitelyGeneratedAsMagma`](axioms.md#ax-finitelygeneratedasmagma) | axiom | lazy-import binding | `sage.categories.finitely_generated_semigroups.FinitelyGeneratedSemigroups` | [`src/sage/categories/semigroups.py:777`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L777) |
| [`HTrivial`](axioms.md#ax-htrivial) | axiom | lazy-import binding | `sage.categories.h_trivial_semigroups.HTrivialSemigroups` | [`src/sage/categories/semigroups.py:782`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L782) |
| [`HTrivial`](axioms.md#ax-htrivial) | axiom | subcategory interface method | `_with_axiom(HTrivial)` | [`src/sage/categories/semigroups.py:692`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L692) |
| [`JTrivial`](axioms.md#ax-jtrivial) | axiom | lazy-import binding | `sage.categories.j_trivial_semigroups.JTrivialSemigroups` | [`src/sage/categories/semigroups.py:781`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L781) |
| [`JTrivial`](axioms.md#ax-jtrivial) | axiom | subcategory interface method | `_with_axiom(JTrivial)` | [`src/sage/categories/semigroups.py:636`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L636) |
| [`LTrivial`](axioms.md#ax-ltrivial) | axiom | lazy-import binding | `sage.categories.l_trivial_semigroups.LTrivialSemigroups` | [`src/sage/categories/semigroups.py:779`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L779) |
| [`LTrivial`](axioms.md#ax-ltrivial) | axiom | subcategory interface method | `_with_axiom(LTrivial)` | [`src/sage/categories/semigroups.py:546`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L546) |
| [`Quotients`](constructions.md#con-quotients) | functorial construction | nested category class | `QuotientsCategory` | [`src/sage/categories/semigroups.py:826`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L826) |
| [`RTrivial`](axioms.md#ax-rtrivial) | axiom | lazy-import binding | `sage.categories.r_trivial_semigroups.RTrivialSemigroups` | [`src/sage/categories/semigroups.py:780`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L780) |
| [`RTrivial`](axioms.md#ax-rtrivial) | axiom | subcategory interface method | `_with_axiom(RTrivial)` | [`src/sage/categories/semigroups.py:591`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L591) |
| [`Subquotients`](constructions.md#con-subquotients) | functorial construction | nested category class | `SubquotientsCategory` | [`src/sage/categories/semigroups.py:786`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L786) |
| [`Unital`](axioms.md#ax-unital) | axiom | lazy-import binding | `sage.categories.monoids.Monoids` | [`src/sage/categories/semigroups.py:778`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L778) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Semigroups` | `semigroups` | `(framework base)` |
| `Semigroups_with_category` | `semigroups` | `(framework base)` |

### Construction-generated classes at 10.10 (6)

| class | module | construction |
| --- | --- | --- |
| `Semigroups.Algebras` | `semigroups` | `Algebras` |
| `Semigroups.CartesianProducts` | `semigroups` | `CartesianProducts` |
| `Semigroups.Quotients` | `semigroups` | `Quotients` |
| `Semigroups.Quotients_with_category` | `semigroups` | `Quotients_with_category` |
| `Semigroups.Subquotients` | `semigroups` | `Subquotients` |
| `Semigroups.Subquotients_with_category` | `semigroups` | `Subquotients_with_category` |

## Semirings {#cat-semirings}

| field | value |
| --- | --- |
| module | `semirings` |
| role | public named category class |
| implementation | Python class |
| defined by | MagmasAndAdditiveMagmas.Distributive.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative + axiom Unital |
| direct defining axiom | [`Unital`](axioms.md#ax-unital) |
| syntactic axiom chain | [`Distributive`](axioms.md#ax-distributive), [`AdditiveAssociative`](axioms.md#ax-additiveassociative), [`AdditiveCommutative`](axioms.md#ax-additivecommutative), [`AdditiveUnital`](axioms.md#ax-additiveunital), [`Associative`](axioms.md#ax-associative), [`Unital`](axioms.md#ax-unital) |
| bound as | `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative.Unital` |
| bases | [`CategoryWithAxiom`](categories.md#cat-categorywithaxiom) |
| source | [`src/sage/categories/semirings.py:15`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semirings.py#L15) |
| loads at 10.10 | yes |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Semirings` | `semirings` | `(framework base)` |
| `Semirings_with_category` | `semirings` | `(framework base)` |

## SemisimpleAlgebras {#cat-semisimplealgebras}

| field | value |
| --- | --- |
| module | `semisimple_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | bound from Algebras |
| bound as | `Algebras.Semisimple` |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/semisimple_algebras.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semisimple_algebras.py#L19) |
| loads at 10.10 | yes |

### Local axiom paths

- `FiniteDimensional`
- `FiniteDimensional.WithBasis`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/semisimple_algebras.py:111`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semisimple_algebras.py#L111) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | lazy-import binding | `sage.categories.finite_dimensional_semisimple_algebras_with_basis.FiniteDimensionalSemisimpleAlgebrasWithBasis` | [`src/sage/categories/semisimple_algebras.py:113`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semisimple_algebras.py#L113) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `SemisimpleAlgebras.FiniteDimensional` | `semisimple_algebras` | `FiniteDimensional` |

## Sets {#cat-sets}

| field | value |
| --- | --- |
| module | `sets_cat` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/sets_cat.py:98`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L98) |
| loads at 10.10 | yes |

### Local axiom paths

- `Enumerated`
- `Facade`
- `Finite`
- `Infinite`
- `Infinite.Finite`

### Local construction paths

- `Algebras`
- `CartesianProducts`
- `IsomorphicObjects`
- `Metric`
- `Quotients`
- `Realizations`
- `Subobjects`
- `Subquotients`
- `Topological`
- `WithRealizations`

### Declared features (26)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/sets_cat.py:2721`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2721) |
| [`Algebras`](constructions.md#con-algebras) | functorial construction | subcategory interface method | `AlgebrasCategory.category_of(...); calls Rings()` | [`src/sage/categories/sets_cat.py:695`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L695) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/sets_cat.py:2185`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2185) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | subcategory interface method | `CartesianProductsCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:303`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L303) |
| [`Enumerated`](axioms.md#ax-enumerated) | axiom | lazy-import binding | `sage.categories.enumerated_sets.EnumeratedSets` | [`src/sage/categories/sets_cat.py:1879`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1879) |
| [`Enumerated`](axioms.md#ax-enumerated) | axiom | subcategory interface method | `_with_axiom(Enumerated)` | [`src/sage/categories/sets_cat.py:776`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L776) |
| [`Facade`](axioms.md#ax-facade) | axiom | subcategory interface method | `_with_axiom(Facade)` | [`src/sage/categories/sets_cat.py:799`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L799) |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_sets.FiniteSets` | [`src/sage/categories/sets_cat.py:1880`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1880) |
| [`Finite`](axioms.md#ax-finite) | axiom | subcategory interface method | `_with_axiom(Finite)` | [`src/sage/categories/sets_cat.py:736`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L736) |
| [`Infinite`](axioms.md#ax-infinite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/sets_cat.py:1887`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1887) |
| [`Infinite`](axioms.md#ax-infinite) | axiom | subcategory interface method | `_with_axiom(Infinite)` | [`src/sage/categories/sets_cat.py:756`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L756) |
| [`Finite`](axioms.md#ax-finite) | axiom | subcategory interface method | — | [`src/sage/categories/sets_cat.py:1890`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1890) |
| [`IsomorphicObjects`](constructions.md#con-isomorphicobjects) | functorial construction | nested category class | `IsomorphicObjectsCategory` | [`src/sage/categories/sets_cat.py:2156`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2156) |
| [`IsomorphicObjects`](constructions.md#con-isomorphicobjects) | functorial construction | subcategory interface method | `IsomorphicObjectsCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:575`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L575) |
| [`Metric`](constructions.md#con-metric) | functorial construction | lazy-import binding | `sage.categories.metric_spaces.MetricSpaces` | [`src/sage/categories/sets_cat.py:1883`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1883) |
| [`Metric`](constructions.md#con-metric) | functorial construction | subcategory interface method | `MetricSpacesCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:683`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L683) |
| [`Quotients`](constructions.md#con-quotients) | functorial construction | nested category class | `QuotientsCategory` | [`src/sage/categories/sets_cat.py:2081`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2081) |
| [`Quotients`](constructions.md#con-quotients) | functorial construction | subcategory interface method | `QuotientsCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:462`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L462) |
| [`Realizations`](constructions.md#con-realizations) | functorial construction | nested category class | `RealizationsCategory` | [`src/sage/categories/sets_cat.py:3157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L3157) |
| [`Subobjects`](constructions.md#con-subobjects) | functorial construction | nested category class | `SubobjectsCategory` | [`src/sage/categories/sets_cat.py:2125`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2125) |
| [`Subobjects`](constructions.md#con-subobjects) | functorial construction | subcategory interface method | `SubobjectsCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:517`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L517) |
| [`Subquotients`](constructions.md#con-subquotients) | functorial construction | nested category class | `SubquotientsCategory` | [`src/sage/categories/sets_cat.py:1952`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1952) |
| [`Subquotients`](constructions.md#con-subquotients) | functorial construction | subcategory interface method | `SubquotientsCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:325`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L325) |
| [`Topological`](constructions.md#con-topological) | functorial construction | lazy-import binding | `sage.categories.topological_spaces.TopologicalSpaces` | [`src/sage/categories/sets_cat.py:1881`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1881) |
| [`Topological`](constructions.md#con-topological) | functorial construction | subcategory interface method | `TopologicalSpacesCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:671`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L671) |
| [`WithRealizations`](constructions.md#con-withrealizations) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/sets_cat.py:2797`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2797) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Sets.Infinite` | `sets_cat` | `Infinite` |
| `Sets.Infinite_with_category` | `sets_cat` | `Infinite_with_category` |

### Construction-generated classes at 10.10 (10)

| class | module | construction |
| --- | --- | --- |
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

## SetsWithGrading {#cat-setswithgrading}

| field | value |
| --- | --- |
| module | `sets_with_grading` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category`](categories.md#cat-category) |
| source | [`src/sage/categories/sets_with_grading.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_with_grading.py#L18) |
| loads at 10.10 | yes |

## SetsWithPartialMaps {#cat-setswithpartialmaps}

| field | value |
| --- | --- |
| module | `sets_with_partial_maps` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/sets_with_partial_maps.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_with_partial_maps.py#L17) |
| loads at 10.10 | yes |

## ShephardGroups {#cat-shephardgroups}

| field | value |
| --- | --- |
| module | `shephard_groups` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/shephard_groups.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/shephard_groups.py#L19) |
| loads at 10.10 | yes |

## SignedTensorProductsCategory {#cat-signedtensorproductscategory}

| field | value |
| --- | --- |
| module | `signed_tensor` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`CovariantConstructionCategory`](categories.md#cat-covariantconstructioncategory) |
| source | [`src/sage/categories/signed_tensor.py:76`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/signed_tensor.py#L76) |
| loads at 10.10 | yes |

### Local construction paths

- `SignedTensorProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`SignedTensorProducts`](constructions.md#con-signedtensorproducts) | functorial construction | category method | — | [`src/sage/categories/signed_tensor.py:93`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/signed_tensor.py#L93) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `SignedTensorProductsCategory` | `signed_tensor` | `(framework base)` |

## SimplicialComplexes {#cat-simplicialcomplexes}

| field | value |
| --- | --- |
| module | `simplicial_complexes` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/simplicial_complexes.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_complexes.py#L19) |
| loads at 10.10 | yes |

### Local axiom paths

- `Connected`
- `Finite`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Connected`](axioms.md#ax-connected) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/simplicial_complexes.py:124`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_complexes.py#L124) |
| [`Connected`](axioms.md#ax-connected) | axiom | subcategory interface method | `_with_axiom(Connected)` | [`src/sage/categories/simplicial_complexes.py:107`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_complexes.py#L107) |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/simplicial_complexes.py:59`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_complexes.py#L59) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `SimplicialComplexes.Connected` | `simplicial_complexes` | `Connected` |
| `SimplicialComplexes.Finite` | `simplicial_complexes` | `Finite` |

## SimplicialSets {#cat-simplicialsets}

| field | value |
| --- | --- |
| module | `simplicial_sets` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/simplicial_sets.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L27) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`
- `Pointed`
- `Homsets.Endset`
- `Pointed.Finite`

### Local construction paths

- `Homsets`

### Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/simplicial_sets.py:176`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L176) |
| [`Homsets`](constructions.md#con-homsets) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/simplicial_sets.py:157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L157) |
| [`Endset`](axioms.md#ax-endset) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/simplicial_sets.py:158`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L158) |
| [`Pointed`](axioms.md#ax-pointed) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/simplicial_sets.py:201`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L201) |
| [`Pointed`](axioms.md#ax-pointed) | axiom | subcategory interface method | `_with_axiom(Pointed)` | [`src/sage/categories/simplicial_sets.py:186`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L186) |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/simplicial_sets.py:1117`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L1117) |

### Axiom-generated classes at 10.10 (4)

| class | module | axiom |
| --- | --- | --- |
| `SimplicialSets.Finite` | `simplicial_sets` | `Finite` |
| `SimplicialSets.Homsets.Endset` | `simplicial_sets` | `Endset` |
| `SimplicialSets.Pointed` | `simplicial_sets` | `Pointed` |
| `SimplicialSets.Pointed.Finite` | `simplicial_sets` | `Finite` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `SimplicialSets.Homsets` | `simplicial_sets` | `Homsets` |

## SubobjectsCategory {#cat-subobjectscategory}

| field | value |
| --- | --- |
| module | `subobjects` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`RegressiveCovariantConstructionCategory`](categories.md#cat-regressivecovariantconstructioncategory) |
| source | [`src/sage/categories/subobjects.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/subobjects.py#L19) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `SubobjectsCategory` | `subobjects` | `(framework base)` |

## SubquotientsCategory {#cat-subquotientscategory}

| field | value |
| --- | --- |
| module | `subquotients` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`RegressiveCovariantConstructionCategory`](categories.md#cat-regressivecovariantconstructioncategory) |
| source | [`src/sage/categories/subquotients.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/subquotients.py#L18) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `SubquotientsCategory` | `subquotients` | `(framework base)` |

## SuperAlgebras {#cat-superalgebras}

| field | value |
| --- | --- |
| module | `super_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | Algebras.Super() |
| defining construction | [`Super`](constructions.md#con-super) |
| bound as | `Algebras.Super` |
| bases | [`SuperModulesCategory`](categories.md#cat-supermodulescategory) |
| source | [`src/sage/categories/super_algebras.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L18) |
| loads at 10.10 | yes |

### Local axiom paths

- `Supercommutative`

### Local construction paths

- `SignedTensorProducts`

### Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`SignedTensorProducts`](constructions.md#con-signedtensorproducts) | functorial construction | nested category class | `SignedTensorProductsCategory` | [`src/sage/categories/super_algebras.py:135`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L135) |
| [`Supercommutative`](axioms.md#ax-supercommutative) | axiom | lazy-import binding | `sage.categories.supercommutative_algebras.SupercommutativeAlgebras` | [`src/sage/categories/super_algebras.py:53`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L53) |
| [`Supercommutative`](axioms.md#ax-supercommutative) | axiom | subcategory interface method | `_with_axiom(Supercommutative)` | [`src/sage/categories/super_algebras.py:110`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L110) |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `SuperAlgebras` | `super_algebras` | `(framework base)` |
| `SuperAlgebras.SignedTensorProducts` | `super_algebras` | `SignedTensorProducts` |

## SuperAlgebrasWithBasis {#cat-superalgebraswithbasis}

| field | value |
| --- | --- |
| module | `super_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | AlgebrasWithBasis.Super() |
| defining construction | [`Super`](constructions.md#con-super) |
| bound as | `AlgebrasWithBasis.Super` |
| bases | [`SuperModulesCategory`](categories.md#cat-supermodulescategory) |
| source | [`src/sage/categories/super_algebras_with_basis.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras_with_basis.py#L16) |
| loads at 10.10 | yes |

### Local construction paths

- `SignedTensorProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`SignedTensorProducts`](constructions.md#con-signedtensorproducts) | functorial construction | nested category class | `SignedTensorProductsCategory` | [`src/sage/categories/super_algebras_with_basis.py:125`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras_with_basis.py#L125) |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `SuperAlgebrasWithBasis` | `super_algebras_with_basis` | `(framework base)` |
| `SuperAlgebrasWithBasis.SignedTensorProducts` | `super_algebras_with_basis` | `SignedTensorProducts` |

## SuperCrystals {#cat-supercrystals}

| field | value |
| --- | --- |
| module | `supercrystals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/supercrystals.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercrystals.py#L25) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`

### Local construction paths

- `TensorProducts`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/supercrystals.py:69`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercrystals.py#L69) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/supercrystals.py:388`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercrystals.py#L388) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `SuperCrystals.Finite` | `supercrystals` | `Finite` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `SuperCrystals.TensorProducts` | `supercrystals` | `TensorProducts` |

## SuperHopfAlgebrasWithBasis {#cat-superhopfalgebraswithbasis}

| field | value |
| --- | --- |
| module | `super_hopf_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | HopfAlgebrasWithBasis.Super() |
| defining construction | [`Super`](constructions.md#con-super) |
| bound as | `HopfAlgebrasWithBasis.Super` |
| bases | [`SuperModulesCategory`](categories.md#cat-supermodulescategory) |
| source | [`src/sage/categories/super_hopf_algebras_with_basis.py:14`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_hopf_algebras_with_basis.py#L14) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `SuperHopfAlgebrasWithBasis` | `super_hopf_algebras_with_basis` | `(framework base)` |

## SuperLieConformalAlgebras {#cat-superlieconformalalgebras}

| field | value |
| --- | --- |
| module | `super_lie_conformal_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | LieConformalAlgebras.Super() |
| defining construction | [`Super`](constructions.md#con-super) |
| bound as | `LieConformalAlgebras.Super` |
| bases | [`SuperModulesCategory`](categories.md#cat-supermodulescategory) |
| source | [`src/sage/categories/super_lie_conformal_algebras.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_lie_conformal_algebras.py#L25) |
| loads at 10.10 | yes |

### Local construction paths

- `Graded`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Graded`](constructions.md#con-graded) | functorial construction | nested category class | `GradedModulesCategory` | [`src/sage/categories/super_lie_conformal_algebras.py:174`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_lie_conformal_algebras.py#L174) |

### Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `SuperLieConformalAlgebras` | `super_lie_conformal_algebras` | `(framework base)` |
| `SuperLieConformalAlgebras.Graded` | `super_lie_conformal_algebras` | `Graded` |

## SuperModules {#cat-supermodules}

| field | value |
| --- | --- |
| module | `super_modules` |
| role | public named category class |
| implementation | Python class |
| defined by | Modules.Super() |
| defining construction | [`Super`](constructions.md#con-super) |
| bound as | `Modules.Super` |
| bases | [`SuperModulesCategory`](categories.md#cat-supermodulescategory) |
| source | [`src/sage/categories/super_modules.py:86`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_modules.py#L86) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `SuperModules` | `super_modules` | `(framework base)` |

## SuperModulesCategory {#cat-supermodulescategory}

| field | value |
| --- | --- |
| module | `super_modules` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`CovariantConstructionCategory`](categories.md#cat-covariantconstructioncategory), [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/super_modules.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_modules.py#L27) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `SuperModulesCategory` | `super_modules` | `(framework base)` |

## SuperModulesWithBasis {#cat-supermoduleswithbasis}

| field | value |
| --- | --- |
| module | `super_modules_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | ModulesWithBasis.Super() |
| defining construction | [`Super`](constructions.md#con-super) |
| bound as | `ModulesWithBasis.Super` |
| bases | [`SuperModulesCategory`](categories.md#cat-supermodulescategory) |
| source | [`src/sage/categories/super_modules_with_basis.py:14`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_modules_with_basis.py#L14) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `SuperModulesWithBasis` | `super_modules_with_basis` | `(framework base)` |

## SupercommutativeAlgebras {#cat-supercommutativealgebras}

| field | value |
| --- | --- |
| module | `supercommutative_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | SuperAlgebras + axiom Supercommutative |
| direct defining axiom | [`Supercommutative`](axioms.md#ax-supercommutative) |
| syntactic axiom chain | [`Supercommutative`](axioms.md#ax-supercommutative) |
| bound as | `SuperAlgebras.Supercommutative` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/supercommutative_algebras.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercommutative_algebras.py#L17) |
| loads at 10.10 | yes |

### Local axiom paths

- `WithBasis`

### Local construction paths

- `SignedTensorProducts`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`SignedTensorProducts`](constructions.md#con-signedtensorproducts) | functorial construction | nested category class | `SignedTensorProductsCategory` | [`src/sage/categories/supercommutative_algebras.py:44`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercommutative_algebras.py#L44) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/supercommutative_algebras.py:61`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercommutative_algebras.py#L61) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `SupercommutativeAlgebras` | `supercommutative_algebras` | `(framework base)` |
| `SupercommutativeAlgebras.WithBasis` | `supercommutative_algebras` | `WithBasis` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `SupercommutativeAlgebras.SignedTensorProducts` | `supercommutative_algebras` | `SignedTensorProducts` |

## TensorProductsCategory {#cat-tensorproductscategory}

| field | value |
| --- | --- |
| module | `tensor` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`CovariantConstructionCategory`](categories.md#cat-covariantconstructioncategory) |
| source | [`src/sage/categories/tensor.py:69`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/tensor.py#L69) |
| loads at 10.10 | yes |

### Local construction paths

- `TensorProducts`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | category method | — | [`src/sage/categories/tensor.py:86`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/tensor.py#L86) |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `TensorProductsCategory` | `tensor` | `(framework base)` |

## TestObjects {#cat-testobjects}

| field | value |
| --- | --- |
| module | `category_with_axiom` |
| role | test-only category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/category_with_axiom.py:2753`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2753) |
| loads at 10.10 | yes |

### Local axiom paths

- `Commutative`
- `FiniteDimensional`
- `Unital`
- `Commutative.Facade`
- `Commutative.Finite`
- `Commutative.FiniteDimensional`
- `FiniteDimensional.Finite`
- `FiniteDimensional.Unital`
- `FiniteDimensional.Unital.Commutative`

### Declared features (9)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Commutative`](axioms.md#ax-commutative) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2779`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2779) |
| [`Facade`](axioms.md#ax-facade) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2780`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2780) |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2786`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2786) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2783`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2783) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2771`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2771) |
| [`Finite`](axioms.md#ax-finite) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2772`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2772) |
| [`Unital`](axioms.md#ax-unital) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2775`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2775) |
| [`Commutative`](axioms.md#ax-commutative) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2776`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2776) |
| [`Unital`](axioms.md#ax-unital) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/category_with_axiom.py:2789`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2789) |

### Axiom-generated classes at 10.10 (9)

| class | module | axiom |
| --- | --- | --- |
| `TestObjects.Commutative` | `category_with_axiom` | `Commutative` |
| `TestObjects.Commutative.Facade` | `category_with_axiom` | `Facade` |
| `TestObjects.Commutative.Finite` | `category_with_axiom` | `Finite` |
| `TestObjects.Commutative.FiniteDimensional` | `category_with_axiom` | `FiniteDimensional` |
| `TestObjects.FiniteDimensional` | `category_with_axiom` | `FiniteDimensional` |
| `TestObjects.FiniteDimensional.Finite` | `category_with_axiom` | `Finite` |
| `TestObjects.FiniteDimensional.Unital` | `category_with_axiom` | `Unital` |
| `TestObjects.FiniteDimensional.Unital.Commutative` | `category_with_axiom` | `Commutative` |
| `TestObjects.Unital` | `category_with_axiom` | `Unital` |

## TopologicalSpaces {#cat-topologicalspaces}

| field | value |
| --- | --- |
| module | `topological_spaces` |
| role | public named category class |
| implementation | Python class |
| defined by | Sets.Topological() |
| defining construction | [`Topological`](constructions.md#con-topological) |
| bound as | `Sets.Topological` |
| bases | [`TopologicalSpacesCategory`](categories.md#cat-topologicalspacescategory) |
| source | [`src/sage/categories/topological_spaces.py:32`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L32) |
| loads at 10.10 | yes |

### Local axiom paths

- `Compact`
- `Connected`

### Local construction paths

- `CartesianProducts`
- `Compact.CartesianProducts`
- `Connected.CartesianProducts`

### Declared features (7)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/topological_spaces.py:65`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L65) |
| [`Compact`](axioms.md#ax-compact) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/topological_spaces.py:146`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L146) |
| [`Compact`](axioms.md#ax-compact) | axiom | subcategory interface method | `_with_axiom(Compact)` | [`src/sage/categories/topological_spaces.py:104`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L104) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/topological_spaces.py:151`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L151) |
| [`Connected`](axioms.md#ax-connected) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/topological_spaces.py:121`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L121) |
| [`Connected`](axioms.md#ax-connected) | axiom | subcategory interface method | `_with_axiom(Connected)` | [`src/sage/categories/topological_spaces.py:86`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L86) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/topological_spaces.py:126`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L126) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `TopologicalSpaces.Compact` | `topological_spaces` | `Compact` |
| `TopologicalSpaces.Connected` | `topological_spaces` | `Connected` |

### Construction-generated classes at 10.10 (5)

| class | module | construction |
| --- | --- | --- |
| `TopologicalSpaces` | `topological_spaces` | `(framework base)` |
| `TopologicalSpaces.CartesianProducts` | `topological_spaces` | `CartesianProducts` |
| `TopologicalSpaces.Compact.CartesianProducts` | `topological_spaces` | `CartesianProducts` |
| `TopologicalSpaces.Connected.CartesianProducts` | `topological_spaces` | `CartesianProducts` |
| `TopologicalSpaces_with_category` | `topological_spaces` | `(framework base)` |

## TopologicalSpacesCategory {#cat-topologicalspacescategory}

| field | value |
| --- | --- |
| module | `topological_spaces` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`RegressiveCovariantConstructionCategory`](categories.md#cat-regressivecovariantconstructioncategory) |
| source | [`src/sage/categories/topological_spaces.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L18) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `TopologicalSpacesCategory` | `topological_spaces` | `(framework base)` |

## TriangularKacMoodyAlgebras {#cat-triangularkacmoodyalgebras}

| field | value |
| --- | --- |
| module | `triangular_kac_moody_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/triangular_kac_moody_algebras.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/triangular_kac_moody_algebras.py#L27) |
| loads at 10.10 | yes |

### Local axiom paths

- `FiniteDimensional`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/triangular_kac_moody_algebras.py:341`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/triangular_kac_moody_algebras.py#L341) |

### Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `TriangularKacMoodyAlgebras.FiniteDimensional` | `triangular_kac_moody_algebras` | `FiniteDimensional` |

## UniqueFactorizationDomains {#cat-uniquefactorizationdomains}

| field | value |
| --- | --- |
| module | `unique_factorization_domains` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/unique_factorization_domains.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/unique_factorization_domains.py#L18) |
| loads at 10.10 | yes |

## UnitalAlgebras {#cat-unitalalgebras}

| field | value |
| --- | --- |
| module | `unital_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | MagmaticAlgebras + axiom Unital |
| direct defining axiom | [`Unital`](axioms.md#ax-unital) |
| syntactic axiom chain | [`Unital`](axioms.md#ax-unital) |
| bound as | `MagmaticAlgebras.Unital` |
| bases | [`CategoryWithAxiom_over_base_ring`](categories.md#cat-categorywithaxiom-over-base-ring) |
| source | [`src/sage/categories/unital_algebras.py:24`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/unital_algebras.py#L24) |
| loads at 10.10 | yes |

### Local axiom paths

- `WithBasis`

### Local construction paths

- `CartesianProducts`

### Declared features (2)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/unital_algebras.py:373`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/unital_algebras.py#L373) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/unital_algebras.py:252`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/unital_algebras.py#L252) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `UnitalAlgebras` | `unital_algebras` | `(framework base)` |
| `UnitalAlgebras.WithBasis` | `unital_algebras` | `WithBasis` |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `UnitalAlgebras.CartesianProducts` | `unital_algebras` | `CartesianProducts` |

## VectorBundles {#cat-vectorbundles}

| field | value |
| --- | --- |
| module | `vector_bundles` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](categories.md#cat-category-over-base-ring) |
| source | [`src/sage/categories/vector_bundles.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_bundles.py#L19) |
| loads at 10.10 | yes |

### Local axiom paths

- `Differentiable`
- `Smooth`

### Declared features (4)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Differentiable`](axioms.md#ax-differentiable) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/vector_bundles.py:144`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_bundles.py#L144) |
| [`Differentiable`](axioms.md#ax-differentiable) | axiom | subcategory interface method | `_with_axiom(Differentiable)` | [`src/sage/categories/vector_bundles.py:100`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_bundles.py#L100) |
| [`Smooth`](axioms.md#ax-smooth) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/vector_bundles.py:152`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_bundles.py#L152) |
| [`Smooth`](axioms.md#ax-smooth) | axiom | subcategory interface method | `_with_axiom(Smooth)` | [`src/sage/categories/vector_bundles.py:123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_bundles.py#L123) |

### Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `VectorBundles.Differentiable` | `vector_bundles` | `Differentiable` |
| `VectorBundles.Smooth` | `vector_bundles` | `Smooth` |

## VectorSpaces {#cat-vectorspaces}

| field | value |
| --- | --- |
| module | `vector_spaces` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_module`](categories.md#cat-category-module) |
| source | [`src/sage/categories/vector_spaces.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L27) |
| loads at 10.10 | yes |

### Local axiom paths

- `FiniteDimensional`
- `WithBasis`
- `WithBasis.FiniteDimensional`

### Local construction paths

- `CartesianProducts`
- `DualObjects`
- `Filtered`
- `Graded`
- `TensorProducts`
- `FiniteDimensional.TensorProducts`
- `WithBasis.CartesianProducts`
- `WithBasis.Filtered`
- `WithBasis.Graded`
- `WithBasis.TensorProducts`
- `WithBasis.FiniteDimensional.TensorProducts`

### Declared features (14)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/vector_spaces.py:322`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L322) |
| [`DualObjects`](constructions.md#con-dualobjects) | functorial construction | nested category class | `DualObjectsCategory` | [`src/sage/categories/vector_spaces.py:303`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L303) |
| [`Filtered`](constructions.md#con-filtered) | functorial construction | nested category class | `FilteredModulesCategory` | [`src/sage/categories/vector_spaces.py:348`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L348) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/vector_spaces.py:285`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L285) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/vector_spaces.py:287`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L287) |
| [`Graded`](constructions.md#con-graded) | functorial construction | nested category class | `GradedModulesCategory` | [`src/sage/categories/vector_spaces.py:353`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L353) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/vector_spaces.py:335`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L335) |
| [`WithBasis`](axioms.md#ax-withbasis) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/vector_spaces.py:182`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L182) |
| [`CartesianProducts`](constructions.md#con-cartesianproducts) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/vector_spaces.py:199`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L199) |
| [`Filtered`](constructions.md#con-filtered) | functorial construction | nested category class | `FilteredModulesCategory` | [`src/sage/categories/vector_spaces.py:264`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L264) |
| [`FiniteDimensional`](axioms.md#ax-finitedimensional) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/vector_spaces.py:225`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L225) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/vector_spaces.py:227`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L227) |
| [`Graded`](constructions.md#con-graded) | functorial construction | nested category class | `GradedModulesCategory` | [`src/sage/categories/vector_spaces.py:243`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L243) |
| [`TensorProducts`](constructions.md#con-tensorproducts) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/vector_spaces.py:212`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L212) |

### Axiom-generated classes at 10.10 (3)

| class | module | axiom |
| --- | --- | --- |
| `VectorSpaces.FiniteDimensional` | `vector_spaces` | `FiniteDimensional` |
| `VectorSpaces.WithBasis` | `vector_spaces` | `WithBasis` |
| `VectorSpaces.WithBasis.FiniteDimensional` | `vector_spaces` | `FiniteDimensional` |

### Construction-generated classes at 10.10 (11)

| class | module | construction |
| --- | --- | --- |
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

## WeylGroups {#cat-weylgroups}

| field | value |
| --- | --- |
| module | `weyl_groups` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](categories.md#cat-category-singleton) |
| source | [`src/sage/categories/weyl_groups.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/weyl_groups.py#L18) |
| loads at 10.10 | yes |

### Local axiom paths

- `Finite`

### Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](axioms.md#ax-finite) | axiom | lazy-import binding | `sage.categories.finite_weyl_groups.FiniteWeylGroups` | [`src/sage/categories/weyl_groups.py:77`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/weyl_groups.py#L77) |

## WithRealizationsCategory {#cat-withrealizationscategory}

| field | value |
| --- | --- |
| module | `with_realizations` |
| role | framework/helper category class |
| implementation | Python class |
| bases | [`RegressiveCovariantConstructionCategory`](categories.md#cat-regressivecovariantconstructioncategory) |
| source | [`src/sage/categories/with_realizations.py:287`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/with_realizations.py#L287) |
| loads at 10.10 | yes |

### Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `WithRealizationsCategory` | `with_realizations` | `(framework base)` |
