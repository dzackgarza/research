# DistributiveMagmasAndAdditiveMagmas

| field | value |
| --- | --- |
| module | `distributive_magmas_and_additive_magmas` |
| role | public named category class |
| implementation | Python class |
| defined by | MagmasAndAdditiveMagmas + axiom Distributive |
| direct defining axiom | [`Distributive`](../../axioms/Distributive.md) |
| syntactic axiom chain | [`Distributive`](../../axioms/Distributive.md) |
| bound as | `MagmasAndAdditiveMagmas.Distributive` |
| bases | [`CategoryWithAxiom`](../../categories/CategoryWithAxiom.md) |
| source | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L16) |
| loads at 10.10 | yes |

## Local axiom paths

- `AdditiveAssociative`
- `AdditiveAssociative.AdditiveCommutative`
- `AdditiveAssociative.AdditiveCommutative.AdditiveUnital`
- `AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative`
- `AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative.AdditiveInverse`
- `AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative.Unital`

## Local construction paths

- `CartesianProducts`

## Declared features (7)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AdditiveAssociative`](../../axioms/AdditiveAssociative.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:41`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L41) |
| [`AdditiveCommutative`](../../axioms/AdditiveCommutative.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:42`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L42) |
| [`AdditiveUnital`](../../axioms/AdditiveUnital.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:43`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L43) |
| [`Associative`](../../axioms/Associative.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:44`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L44) |
| [`AdditiveInverse`](../../axioms/AdditiveInverse.md) | axiom | lazy-import binding | `sage.categories.rngs.Rngs` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:45`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L45) |
| [`Unital`](../../axioms/Unital.md) | axiom | lazy-import binding | `sage.categories.semirings.Semirings` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:46`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L46) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:84`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L84) |

## Axiom-generated classes at 10.10 (10)

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

## Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `DistributiveMagmasAndAdditiveMagmas.CartesianProducts` | `distributive_magmas_and_additive_magmas` | `CartesianProducts` |
