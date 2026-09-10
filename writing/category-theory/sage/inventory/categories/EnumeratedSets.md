# EnumeratedSets

| field | value |
| --- | --- |
| module | `enumerated_sets` |
| role | public named category class |
| implementation | Python class |
| defined by | Sets + axiom Enumerated |
| direct defining axiom | [`Enumerated`](../../axioms/Enumerated.md) |
| syntactic axiom chain | [`Enumerated`](../../axioms/Enumerated.md) |
| bound as | `Sets.Enumerated` |
| bases | [`CategoryWithAxiom`](../../categories/CategoryWithAxiom.md) |
| source | [`src/sage/categories/enumerated_sets.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L21) |
| loads at 10.10 | yes |

## Local axiom paths

- `Finite`
- `Infinite`

## Local construction paths

- `CartesianProducts`

## Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/enumerated_sets.py:1126`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L1126) |
| [`Finite`](../../axioms/Finite.md) | axiom | lazy-import binding | `sage.categories.finite_enumerated_sets.FiniteEnumeratedSets` | [`src/sage/categories/enumerated_sets.py:1123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L1123) |
| [`Infinite`](../../axioms/Infinite.md) | axiom | lazy-import binding | `sage.categories.infinite_enumerated_sets.InfiniteEnumeratedSets` | [`src/sage/categories/enumerated_sets.py:1124`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/enumerated_sets.py#L1124) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `EnumeratedSets` | `enumerated_sets` | `(framework base)` |
| `EnumeratedSets_with_category` | `enumerated_sets` | `(framework base)` |

## Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `EnumeratedSets.CartesianProducts` | `enumerated_sets` | `CartesianProducts` |
