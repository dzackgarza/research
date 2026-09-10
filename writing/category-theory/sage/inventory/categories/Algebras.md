# Algebras

| field | value |
| --- | --- |
| module | `algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | AssociativeAlgebras + axiom Unital |
| direct defining axiom | [`Unital`](../../axioms/Unital.md) |
| syntactic axiom chain | [`Associative`](../../axioms/Associative.md), [`Unital`](../../axioms/Unital.md) |
| bound as | `AssociativeAlgebras.Unital` |
| bases | [`CategoryWithAxiom_over_base_ring`](../../categories/CategoryWithAxiom_over_base_ring.md) |
| source | [`src/sage/categories/algebras.py:29`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L29) |
| loads at 10.10 | yes |

## Local axiom paths

- `Commutative`
- `Supercommutative`
- `WithBasis`

## Local construction paths

- `CartesianProducts`
- `DualObjects`
- `Filtered`
- `Graded`
- `Quotients`
- `Super`
- `TensorProducts`

## Other local category paths

- `Semisimple`

## Declared features (12)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/algebras.py:273`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L273) |
| [`Commutative`](../../axioms/Commutative.md) | axiom | lazy-import binding | `sage.categories.commutative_algebras.CommutativeAlgebras` | [`src/sage/categories/algebras.py:129`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L129) |
| [`DualObjects`](../../constructions/DualObjects.md) | functorial construction | nested category class | `DualObjectsCategory` | [`src/sage/categories/algebras.py:325`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L325) |
| [`Filtered`](../../constructions/Filtered.md) | functorial construction | lazy-import binding | `sage.categories.filtered_algebras.FilteredAlgebras` | [`src/sage/categories/algebras.py:131`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L131) |
| [`Graded`](../../constructions/Graded.md) | functorial construction | lazy-import binding | `sage.categories.graded_algebras.GradedAlgebras` | [`src/sage/categories/algebras.py:133`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L133) |
| [`Quotients`](../../constructions/Quotients.md) | functorial construction | nested category class | `QuotientsCategory` | [`src/sage/categories/algebras.py:247`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L247) |
| `Semisimple` | derived category shorthand | subcategory interface method | `calls SemisimpleAlgebras()` | [`src/sage/categories/algebras.py:89`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L89) |
| `Semisimple` | other category | lazy-import binding | `sage.categories.semisimple_algebras.SemisimpleAlgebras` | [`src/sage/categories/algebras.py:141`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L141) |
| [`Super`](../../constructions/Super.md) | functorial construction | lazy-import binding | `sage.categories.super_algebras.SuperAlgebras` | [`src/sage/categories/algebras.py:135`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L135) |
| [`Supercommutative`](../../axioms/Supercommutative.md) | axiom | subcategory interface method | `calls Super()` | [`src/sage/categories/algebras.py:109`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L109) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/algebras.py:300`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L300) |
| [`WithBasis`](../../axioms/WithBasis.md) | axiom | lazy-import binding | `sage.categories.algebras_with_basis.AlgebrasWithBasis` | [`src/sage/categories/algebras.py:138`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L138) |

## Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `Algebras` | `algebras` | `(framework base)` |

## Construction-generated classes at 10.10 (4)

| class | module | construction |
| --- | --- | --- |
| `Algebras.CartesianProducts` | `algebras` | `CartesianProducts` |
| `Algebras.DualObjects` | `algebras` | `DualObjects` |
| `Algebras.Quotients` | `algebras` | `Quotients` |
| `Algebras.TensorProducts` | `algebras` | `TensorProducts` |
