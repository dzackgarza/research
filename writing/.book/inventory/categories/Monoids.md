# Monoids

| field | value |
| --- | --- |
| module | `monoids` |
| role | public named category class |
| implementation | Python class |
| defined by | Semigroups + axiom Unital |
| direct defining axiom | [`Unital`](../../axioms/Unital.md) |
| syntactic axiom chain | [`Associative`](../../axioms/Associative.md), [`Unital`](../../axioms/Unital.md) |
| bound as | `Semigroups.Unital` |
| bases | [`CategoryWithAxiom`](../../categories/CategoryWithAxiom.md) |
| source | [`src/sage/categories/monoids.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L27) |
| loads at 10.10 | yes |

## Local axiom paths

- `Commutative`
- `Finite`
- `Inverse`

## Local construction paths

- `Algebras`
- `CartesianProducts`
- `Subquotients`
- `WithRealizations`

## Declared features (7)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/monoids.py:484`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L484) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/monoids.py:626`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L626) |
| [`Commutative`](../../axioms/Commutative.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/monoids.py:391`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L391) |
| [`Finite`](../../axioms/Finite.md) | axiom | lazy-import binding | `sage.categories.finite_monoids.FiniteMonoids` | [`src/sage/categories/monoids.py:77`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L77) |
| [`Inverse`](../../axioms/Inverse.md) | axiom | lazy-import binding | `sage.categories.groups.Groups` | [`src/sage/categories/monoids.py:78`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L78) |
| [`Subquotients`](../../constructions/Subquotients.md) | functorial construction | nested category class | `SubquotientsCategory` | [`src/sage/categories/monoids.py:468`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L468) |
| [`WithRealizations`](../../constructions/WithRealizations.md) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/monoids.py:439`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/monoids.py#L439) |

## Axiom-generated classes at 10.10 (4)

| class | module | axiom |
| --- | --- | --- |
| `Monoids` | `monoids` | `(framework base)` |
| `Monoids.Commutative` | `monoids` | `Commutative` |
| `Monoids.Commutative_with_category` | `monoids` | `Commutative_with_category` |
| `Monoids_with_category` | `monoids` | `(framework base)` |

## Construction-generated classes at 10.10 (5)

| class | module | construction |
| --- | --- | --- |
| `Monoids.Algebras` | `monoids` | `Algebras` |
| `Monoids.CartesianProducts` | `monoids` | `CartesianProducts` |
| `Monoids.Subquotients` | `monoids` | `Subquotients` |
| `Monoids.Subquotients_with_category` | `monoids` | `Subquotients_with_category` |
| `Monoids.WithRealizations` | `monoids` | `WithRealizations` |
