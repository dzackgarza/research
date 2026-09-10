# Magmas

| field | value |
| --- | --- |
| module | `magmas` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](../../categories/Category_singleton.md) |
| source | [`src/sage/categories/magmas.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L25) |
| loads at 10.10 | yes |

## Local axiom paths

- `Associative`
- `Commutative`
- `Distributive`
- `FinitelyGeneratedAsMagma`
- `JTrivial`
- `Unital`
- `Unital.Inverse`

## Local construction paths

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

## Other local category paths

- `FinitelyGenerated`

## Declared features (24)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/magmas.py:349`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L349) |
| [`Associative`](../../axioms/Associative.md) | axiom | lazy-import binding | `sage.categories.semigroups.Semigroups` | [`src/sage/categories/magmas.py:342`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L342) |
| [`Associative`](../../axioms/Associative.md) | axiom | subcategory interface method | `_with_axiom(Associative)` | [`src/sage/categories/magmas.py:75`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L75) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/magmas.py:1038`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L1038) |
| [`Commutative`](../../axioms/Commutative.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/magmas.py:401`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L401) |
| [`Commutative`](../../axioms/Commutative.md) | axiom | subcategory interface method | `_with_axiom(Commutative)` | [`src/sage/categories/magmas.py:101`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L101) |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/magmas.py:415`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L415) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/magmas.py:441`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L441) |
| [`Distributive`](../../axioms/Distributive.md) | axiom | subcategory interface method | `calls AdditiveMagmas(), MagmasAndAdditiveMagmas()` | [`src/sage/categories/magmas.py:265`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L265) |
| `FinitelyGenerated` | derived category shorthand | subcategory interface method | `calls FinitelyGeneratedAsMagma(), AdditiveMagmas()` | [`src/sage/categories/magmas.py:222`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L222) |
| [`FinitelyGeneratedAsMagma`](../../axioms/FinitelyGeneratedAsMagma.md) | axiom | lazy-import binding | `sage.categories.finitely_generated_magmas.FinitelyGeneratedMagmas` | [`src/sage/categories/magmas.py:343`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L343) |
| [`FinitelyGeneratedAsMagma`](../../axioms/FinitelyGeneratedAsMagma.md) | axiom | subcategory interface method | `_with_axiom(FinitelyGeneratedAsMagma)` | [`src/sage/categories/magmas.py:165`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L165) |
| [`JTrivial`](../../axioms/JTrivial.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/magmas.py:345`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L345) |
| [`JTrivial`](../../axioms/JTrivial.md) | axiom | subcategory interface method | `_with_axiom(JTrivial)` | [`src/sage/categories/magmas.py:320`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L320) |
| [`Realizations`](../../constructions/Realizations.md) | functorial construction | nested category class | `RealizationsCategory` | [`src/sage/categories/magmas.py:1154`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L1154) |
| [`Subquotients`](../../constructions/Subquotients.md) | functorial construction | nested category class | `SubquotientsCategory` | [`src/sage/categories/magmas.py:1103`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L1103) |
| [`Unital`](../../axioms/Unital.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/magmas.py:457`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L457) |
| [`Unital`](../../axioms/Unital.md) | axiom | subcategory interface method | `_with_axiom(Unital)` | [`src/sage/categories/magmas.py:129`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L129) |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/magmas.py:694`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L694) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/magmas.py:615`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L615) |
| [`Inverse`](../../axioms/Inverse.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/magmas.py:598`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L598) |
| [`Inverse`](../../axioms/Inverse.md) | axiom | subcategory interface method | `_with_axiom(Inverse)` | [`src/sage/categories/magmas.py:570`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L570) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/magmas.py:599`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L599) |
| [`Realizations`](../../constructions/Realizations.md) | functorial construction | nested category class | `RealizationsCategory` | [`src/sage/categories/magmas.py:720`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L720) |

## Axiom-generated classes at 10.10 (6)

| class | module | axiom |
| --- | --- | --- |
| `Magmas.Commutative` | `magmas` | `Commutative` |
| `Magmas.Commutative_with_category` | `magmas` | `Commutative_with_category` |
| `Magmas.JTrivial` | `magmas` | `JTrivial` |
| `Magmas.Unital` | `magmas` | `Unital` |
| `Magmas.Unital.Inverse` | `magmas` | `Inverse` |
| `Magmas.Unital_with_category` | `magmas` | `Unital_with_category` |

## Construction-generated classes at 10.10 (11)

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
