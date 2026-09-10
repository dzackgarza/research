# SuperAlgebras

| field | value |
| --- | --- |
| module | `super_algebras` |
| role | public named category class |
| implementation | Python class |
| defined by | Algebras.Super() |
| defining construction | [`Super`](../../constructions/Super.md) |
| bound as | `Algebras.Super` |
| bases | [`SuperModulesCategory`](../../categories/SuperModulesCategory.md) |
| source | [`src/sage/categories/super_algebras.py:18`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L18) |
| loads at 10.10 | yes |

## Local axiom paths

- `Supercommutative`

## Local construction paths

- `SignedTensorProducts`

## Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`SignedTensorProducts`](../../constructions/SignedTensorProducts.md) | functorial construction | nested category class | `SignedTensorProductsCategory` | [`src/sage/categories/super_algebras.py:135`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L135) |
| [`Supercommutative`](../../axioms/Supercommutative.md) | axiom | lazy-import binding | `sage.categories.supercommutative_algebras.SupercommutativeAlgebras` | [`src/sage/categories/super_algebras.py:53`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L53) |
| [`Supercommutative`](../../axioms/Supercommutative.md) | axiom | subcategory interface method | `_with_axiom(Supercommutative)` | [`src/sage/categories/super_algebras.py:110`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/super_algebras.py#L110) |

## Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `SuperAlgebras` | `super_algebras` | `(framework base)` |
| `SuperAlgebras.SignedTensorProducts` | `super_algebras` | `SignedTensorProducts` |
