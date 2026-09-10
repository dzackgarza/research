# FiniteSets

| field | value |
| --- | --- |
| module | `finite_sets` |
| role | public named category class |
| implementation | Python class |
| defined by | Sets + axiom Finite |
| direct defining axiom | [`Finite`](../../axioms/Finite.md) |
| syntactic axiom chain | [`Finite`](../../axioms/Finite.md) |
| bound as | `Sets.Finite` |
| bases | [`CategoryWithAxiom`](../../categories/CategoryWithAxiom.md) |
| source | [`src/sage/categories/finite_sets.py:16`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L16) |
| loads at 10.10 | yes |

## Local axiom paths

- `Infinite`

## Local construction paths

- `Algebras`
- `Subquotients`

## Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/finite_sets.py:91`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L91) |
| [`Infinite`](../../axioms/Infinite.md) | axiom | subcategory interface method | — | [`src/sage/categories/finite_sets.py:42`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L42) |
| [`Subquotients`](../../constructions/Subquotients.md) | functorial construction | nested category class | `SubquotientsCategory` | [`src/sage/categories/finite_sets.py:70`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_sets.py#L70) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `FiniteSets` | `finite_sets` | `(framework base)` |
| `FiniteSets_with_category` | `finite_sets` | `(framework base)` |

## Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `FiniteSets.Algebras` | `finite_sets` | `Algebras` |
| `FiniteSets.Subquotients` | `finite_sets` | `Subquotients` |
