# AdditiveCommutative

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `commutative_additive_groups.CommutativeAdditiveGroups`, `commutative_additive_monoids.CommutativeAdditiveMonoids`, `commutative_additive_semigroups.CommutativeAdditiveSemigroups` |
| interface declarations | `additive_magmas.AdditiveMagmas:AdditiveCommutative` |
| implementation or binding | `additive_groups.AdditiveGroups:AdditiveCommutative [lazy-import binding]; additive_magmas.AdditiveMagmas:AdditiveCommutative [nested category class]; additive_monoids.AdditiveMonoids:AdditiveCommutative [lazy-import binding]; additive_semigroups.AdditiveSemigroups:AdditiveCommutative [lazy-import binding]; distributive_magmas_and_additive_magmas.DistributiveMagmasAndAdditiveMagmas:AdditiveAssociative.AdditiveCommutative [nested category class]` |
| method expansions | `additive_magmas.AdditiveMagmas:AdditiveCommutative -> _with_axiom(AdditiveCommutative)` |

## Declared in (6)

| category | declaration | source |
| --- | --- | --- |
| [`AdditiveGroups`](../../categories/AdditiveGroups.md) | lazy-import binding | [`src/sage/categories/additive_groups.py:69`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L69) |
| [`AdditiveMagmas`](../../categories/AdditiveMagmas.md) | nested category class | [`src/sage/categories/additive_magmas.py:563`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L563) |
| [`AdditiveMagmas`](../../categories/AdditiveMagmas.md) | subcategory interface method | [`src/sage/categories/additive_magmas.py:104`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L104) |
| [`AdditiveMonoids`](../../categories/AdditiveMonoids.md) | lazy-import binding | [`src/sage/categories/additive_monoids.py:47`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L47) |
| [`AdditiveSemigroups`](../../categories/AdditiveSemigroups.md) | lazy-import binding | [`src/sage/categories/additive_semigroups.py:53`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L53) |
| [`DistributiveMagmasAndAdditiveMagmas`](../../categories/DistributiveMagmasAndAdditiveMagmas.md) | nested category class | [`src/sage/categories/distributive_magmas_and_additive_magmas.py:42`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/distributive_magmas_and_additive_magmas.py#L42) |

## Classes the framework generates at 10.10 (2)

| class | module |
| --- | --- |
| `AdditiveMagmas.AdditiveCommutative` | `additive_magmas` |
| `DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative` | `distributive_magmas_and_additive_magmas` |
