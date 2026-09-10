# Distributive

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas` |
| interface declarations | `lattice_posets.LatticePosets:Distributive; magmas.Magmas:Distributive; magmas_and_additive_magmas.MagmasAndAdditiveMagmas:Distributive` |
| implementation or binding | `magmas_and_additive_magmas.MagmasAndAdditiveMagmas:Distributive [lazy-import binding]` |
| method expansions | `lattice_posets.LatticePosets:Distributive -> _with_axiom(ChainGraded) then _with_axiom(Trim); magmas.Magmas:Distributive -> calls AdditiveMagmas(), MagmasAndAdditiveMagmas(); magmas_and_additive_magmas.MagmasAndAdditiveMagmas:Distributive -> _with_axiom(Distributive)` |

## Declared in (4)

| category | declaration | source |
| --- | --- | --- |
| [`LatticePosets`](../../categories/LatticePosets.md) | subcategory interface method | [`src/sage/categories/lattice_posets.py:123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L123) |
| [`Magmas`](../../categories/Magmas.md) | subcategory interface method | [`src/sage/categories/magmas.py:265`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas.py#L265) |
| [`MagmasAndAdditiveMagmas`](../../categories/MagmasAndAdditiveMagmas.md) | lazy-import binding | [`src/sage/categories/magmas_and_additive_magmas.py:134`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L134) |
| [`MagmasAndAdditiveMagmas`](../../categories/MagmasAndAdditiveMagmas.md) | subcategory interface method | [`src/sage/categories/magmas_and_additive_magmas.py:59`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmas_and_additive_magmas.py#L59) |
