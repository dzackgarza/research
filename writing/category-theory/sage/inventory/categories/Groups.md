# Groups

| field | value |
| --- | --- |
| module | `groups` |
| role | public named category class |
| implementation | Python class |
| defined by | Monoids + axiom Inverse |
| direct defining axiom | [`Inverse`](../../axioms/Inverse.md) |
| syntactic axiom chain | [`Associative`](../../axioms/Associative.md), [`Unital`](../../axioms/Unital.md), [`Inverse`](../../axioms/Inverse.md) |
| bound as | `Monoids.Inverse` |
| bases | [`CategoryWithAxiom`](../../categories/CategoryWithAxiom.md) |
| source | [`src/sage/categories/groups.py:23`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L23) |
| loads at 10.10 | yes |

## Local axiom paths

- `Commutative`
- `Finite`

## Local construction paths

- `Algebras`
- `CartesianProducts`
- `Topological`

## Other local category paths

- `Lie`

## Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | lazy-import binding | `sage.categories.group_algebras.GroupAlgebras` | [`src/sage/categories/groups.py:493`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L493) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/groups.py:547`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L547) |
| [`Commutative`](../../axioms/Commutative.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/groups.py:495`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L495) |
| [`Finite`](../../axioms/Finite.md) | axiom | lazy-import binding | `sage.categories.finite_groups.FiniteGroups` | [`src/sage/categories/groups.py:491`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L491) |
| `Lie` | other category | lazy-import binding | `sage.categories.lie_groups.LieGroups` | [`src/sage/categories/groups.py:492`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L492) |
| [`Topological`](../../constructions/Topological.md) | functorial construction | nested category class | `TopologicalSpacesCategory` | [`src/sage/categories/groups.py:654`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/groups.py#L654) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Groups` | `groups` | `(framework base)` |
| `Groups.Commutative` | `groups` | `Commutative` |

## Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `Groups.CartesianProducts` | `groups` | `CartesianProducts` |
| `Groups.Topological` | `groups` | `Topological` |
