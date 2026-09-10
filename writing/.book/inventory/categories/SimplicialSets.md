# SimplicialSets

| field | value |
| --- | --- |
| module | `simplicial_sets` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](../../categories/Category_singleton.md) |
| source | [`src/sage/categories/simplicial_sets.py:27`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L27) |
| loads at 10.10 | yes |

## Local axiom paths

- `Finite`
- `Pointed`
- `Homsets.Endset`
- `Pointed.Finite`

## Local construction paths

- `Homsets`

## Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](../../axioms/Finite.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/simplicial_sets.py:176`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L176) |
| [`Homsets`](../../constructions/Homsets.md) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/simplicial_sets.py:157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L157) |
| [`Endset`](../../axioms/Endset.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/simplicial_sets.py:158`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L158) |
| [`Pointed`](../../axioms/Pointed.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/simplicial_sets.py:201`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L201) |
| [`Pointed`](../../axioms/Pointed.md) | axiom | subcategory interface method | `_with_axiom(Pointed)` | [`src/sage/categories/simplicial_sets.py:186`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L186) |
| [`Finite`](../../axioms/Finite.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/simplicial_sets.py:1117`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/simplicial_sets.py#L1117) |

## Axiom-generated classes at 10.10 (4)

| class | module | axiom |
| --- | --- | --- |
| `SimplicialSets.Finite` | `simplicial_sets` | `Finite` |
| `SimplicialSets.Homsets.Endset` | `simplicial_sets` | `Endset` |
| `SimplicialSets.Pointed` | `simplicial_sets` | `Pointed` |
| `SimplicialSets.Pointed.Finite` | `simplicial_sets` | `Finite` |

## Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `SimplicialSets.Homsets` | `simplicial_sets` | `Homsets` |
