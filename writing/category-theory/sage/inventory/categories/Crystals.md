# Crystals

| field | value |
| --- | --- |
| module | `crystals` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](../../categories/Category_singleton.md) |
| source | [`src/sage/categories/crystals.py:35`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L35) |
| loads at 10.10 | yes |

## Local axiom paths

- `Finite`

## Local construction paths

- `TensorProducts`

## Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](../../axioms/Finite.md) | axiom | lazy-import binding | `sage.categories.finite_crystals.FiniteCrystals` | [`src/sage/categories/crystals.py:1822`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L1822) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/crystals.py:1808`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L1808) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | subcategory interface method | `TensorProductsCategory.category_of(...)` | [`src/sage/categories/crystals.py:1791`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/crystals.py#L1791) |

## Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `Crystals.TensorProducts` | `crystals` | `TensorProducts` |
