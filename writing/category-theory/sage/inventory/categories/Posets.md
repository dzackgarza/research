# Posets

| field | value |
| --- | --- |
| module | `posets` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category`](../../categories/Category.md) |
| source | [`src/sage/categories/posets.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L19) |
| loads at 10.10 | yes |

## Local axiom paths

- `Bounded`
- `Finite`

## Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Bounded`](../../axioms/Bounded.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/posets.py:736`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L736) |
| [`Bounded`](../../axioms/Bounded.md) | axiom | subcategory interface method | `_with_axiom(Bounded)` | [`src/sage/categories/posets.py:723`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L723) |
| [`Finite`](../../axioms/Finite.md) | axiom | lazy-import binding | `sage.categories.finite_posets.FinitePosets` | [`src/sage/categories/posets.py:155`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/posets.py#L155) |

## Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `Posets.Bounded` | `posets` | `Bounded` |
