# MagmasAndAdditiveMagmas

| field | value |
| --- | --- |
| module | `magmas_and_additive_magmas` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](../../categories/Category_singleton.md) |
| source | [`src/sage/categories/magmas_and_additive_magmas.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L19) |
| loads at 10.10 | yes |

## Local axiom paths

- `Distributive`

## Local construction paths

- `CartesianProducts`

## Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/magmas_and_additive_magmas.py:136`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L136) |
| [`Distributive`](../../axioms/Distributive.md) | axiom | lazy-import binding | `sage.categories.distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas` | [`src/sage/categories/magmas_and_additive_magmas.py:134`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L134) |
| [`Distributive`](../../axioms/Distributive.md) | axiom | subcategory interface method | `_with_axiom(Distributive)` | [`src/sage/categories/magmas_and_additive_magmas.py:59`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L59) |

## Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `MagmasAndAdditiveMagmas.CartesianProducts` | `magmas_and_additive_magmas` | `CartesianProducts` |
