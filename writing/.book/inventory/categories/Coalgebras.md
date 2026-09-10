# Coalgebras

| field | value |
| --- | --- |
| module | `coalgebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](../../categories/Category_over_base_ring.md) |
| source | [`src/sage/categories/coalgebras.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L27) |
| loads at 10.10 | yes |

## Local axiom paths

- `Cocommutative`
- `WithBasis`
- `Super.Supercocommutative`

## Local construction paths

- `DualObjects`
- `Filtered`
- `Graded`
- `Realizations`
- `Super`
- `TensorProducts`
- `WithRealizations`

## Declared features (12)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Cocommutative`](../../axioms/Cocommutative.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/coalgebras.py:180`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L180) |
| [`Cocommutative`](../../axioms/Cocommutative.md) | axiom | subcategory interface method | `_with_axiom(Cocommutative)` | [`src/sage/categories/coalgebras.py:150`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L150) |
| [`DualObjects`](../../constructions/DualObjects.md) | functorial construction | nested category class | `DualObjectsCategory` | [`src/sage/categories/coalgebras.py:210`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L210) |
| [`Filtered`](../../constructions/Filtered.md) | functorial construction | nested category class | `FilteredModulesCategory` | [`src/sage/categories/coalgebras.py:288`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L288) |
| [`Graded`](../../constructions/Graded.md) | functorial construction | lazy-import binding | `sage.categories.graded_coalgebras.GradedCoalgebras` | [`src/sage/categories/coalgebras.py:52`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L52) |
| [`Realizations`](../../constructions/Realizations.md) | functorial construction | nested category class | `RealizationsCategory` | [`src/sage/categories/coalgebras.py:343`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L343) |
| [`Super`](../../constructions/Super.md) | functorial construction | nested category class | `SuperModulesCategory` | [`src/sage/categories/coalgebras.py:236`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L236) |
| [`Supercocommutative`](../../axioms/Supercocommutative.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/coalgebras.py:283`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L283) |
| [`Supercocommutative`](../../axioms/Supercocommutative.md) | axiom | subcategory interface method | `_with_axiom(Supercocommutative)` | [`src/sage/categories/coalgebras.py:262`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L262) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/coalgebras.py:185`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L185) |
| [`WithBasis`](../../axioms/WithBasis.md) | axiom | lazy-import binding | `sage.categories.coalgebras_with_basis.CoalgebrasWithBasis` | [`src/sage/categories/coalgebras.py:51`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L51) |
| [`WithRealizations`](../../constructions/WithRealizations.md) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/coalgebras.py:293`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L293) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Coalgebras.Cocommutative` | `coalgebras` | `Cocommutative` |
| `Coalgebras.Super.Supercocommutative` | `coalgebras` | `Supercocommutative` |

## Construction-generated classes at 10.10 (6)

| class | module | construction |
| --- | --- | --- |
| `Coalgebras.DualObjects` | `coalgebras` | `DualObjects` |
| `Coalgebras.Filtered` | `coalgebras` | `Filtered` |
| `Coalgebras.Realizations` | `coalgebras` | `Realizations` |
| `Coalgebras.Super` | `coalgebras` | `Super` |
| `Coalgebras.TensorProducts` | `coalgebras` | `TensorProducts` |
| `Coalgebras.WithRealizations` | `coalgebras` | `WithRealizations` |
