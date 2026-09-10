# VectorSpaces

| field | value |
| --- | --- |
| module | `vector_spaces` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_module`](../../categories/Category_module.md) |
| source | [`src/sage/categories/vector_spaces.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L27) |
| loads at 10.10 | yes |

## Local axiom paths

- `FiniteDimensional`
- `WithBasis`
- `WithBasis.FiniteDimensional`

## Local construction paths

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

## Declared features (14)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/vector_spaces.py:322`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L322) |
| [`DualObjects`](../../constructions/DualObjects.md) | functorial construction | nested category class | `DualObjectsCategory` | [`src/sage/categories/vector_spaces.py:303`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L303) |
| [`Filtered`](../../constructions/Filtered.md) | functorial construction | nested category class | `FilteredModulesCategory` | [`src/sage/categories/vector_spaces.py:348`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L348) |
| [`FiniteDimensional`](../../axioms/FiniteDimensional.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/vector_spaces.py:285`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L285) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/vector_spaces.py:287`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L287) |
| [`Graded`](../../constructions/Graded.md) | functorial construction | nested category class | `GradedModulesCategory` | [`src/sage/categories/vector_spaces.py:353`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L353) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/vector_spaces.py:335`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L335) |
| [`WithBasis`](../../axioms/WithBasis.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/vector_spaces.py:182`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L182) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/vector_spaces.py:199`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L199) |
| [`Filtered`](../../constructions/Filtered.md) | functorial construction | nested category class | `FilteredModulesCategory` | [`src/sage/categories/vector_spaces.py:264`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L264) |
| [`FiniteDimensional`](../../axioms/FiniteDimensional.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/vector_spaces.py:225`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L225) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/vector_spaces.py:227`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L227) |
| [`Graded`](../../constructions/Graded.md) | functorial construction | nested category class | `GradedModulesCategory` | [`src/sage/categories/vector_spaces.py:243`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L243) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/vector_spaces.py:212`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L212) |

## Axiom-generated classes at 10.10 (3)

| class | module | axiom |
| --- | --- | --- |
| `VectorSpaces.FiniteDimensional` | `vector_spaces` | `FiniteDimensional` |
| `VectorSpaces.WithBasis` | `vector_spaces` | `WithBasis` |
| `VectorSpaces.WithBasis.FiniteDimensional` | `vector_spaces` | `FiniteDimensional` |

## Construction-generated classes at 10.10 (11)

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
