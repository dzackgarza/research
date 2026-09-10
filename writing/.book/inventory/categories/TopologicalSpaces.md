# TopologicalSpaces

| field | value |
| --- | --- |
| module | `topological_spaces` |
| role | public named category class |
| implementation | Python class |
| defined by | Sets.Topological() |
| defining construction | [`Topological`](../../constructions/Topological.md) |
| bound as | `Sets.Topological` |
| bases | [`TopologicalSpacesCategory`](../../categories/TopologicalSpacesCategory.md) |
| source | [`src/sage/categories/topological_spaces.py:32`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L32) |
| loads at 10.10 | yes |

## Local axiom paths

- `Compact`
- `Connected`

## Local construction paths

- `CartesianProducts`
- `Compact.CartesianProducts`
- `Connected.CartesianProducts`

## Declared features (7)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/topological_spaces.py:65`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L65) |
| [`Compact`](../../axioms/Compact.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/topological_spaces.py:146`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L146) |
| [`Compact`](../../axioms/Compact.md) | axiom | subcategory interface method | `_with_axiom(Compact)` | [`src/sage/categories/topological_spaces.py:104`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L104) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/topological_spaces.py:151`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L151) |
| [`Connected`](../../axioms/Connected.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/topological_spaces.py:121`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L121) |
| [`Connected`](../../axioms/Connected.md) | axiom | subcategory interface method | `_with_axiom(Connected)` | [`src/sage/categories/topological_spaces.py:86`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L86) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/topological_spaces.py:126`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/topological_spaces.py#L126) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `TopologicalSpaces.Compact` | `topological_spaces` | `Compact` |
| `TopologicalSpaces.Connected` | `topological_spaces` | `Connected` |

## Construction-generated classes at 10.10 (5)

| class | module | construction |
| --- | --- | --- |
| `TopologicalSpaces` | `topological_spaces` | `(framework base)` |
| `TopologicalSpaces.CartesianProducts` | `topological_spaces` | `CartesianProducts` |
| `TopologicalSpaces.Compact.CartesianProducts` | `topological_spaces` | `CartesianProducts` |
| `TopologicalSpaces.Connected.CartesianProducts` | `topological_spaces` | `CartesianProducts` |
| `TopologicalSpaces_with_category` | `topological_spaces` | `(framework base)` |
