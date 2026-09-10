# WithBasis

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `algebras_with_basis.AlgebrasWithBasis`, `bialgebras_with_basis.BialgebrasWithBasis`, `coalgebras_with_basis.CoalgebrasWithBasis`, `finite_dimensional_lie_algebras_with_basis.FiniteDimensionalLieAlgebrasWithBasis`, `finite_dimensional_semisimple_algebras_with_basis.FiniteDimensionalSemisimpleAlgebrasWithBasis`, `hopf_algebras_with_basis.HopfAlgebrasWithBasis`, `lambda_bracket_algebras_with_basis.LambdaBracketAlgebrasWithBasis`, `lie_algebras_with_basis.LieAlgebrasWithBasis`, `lie_conformal_algebras_with_basis.LieConformalAlgebrasWithBasis`, `modules_with_basis.ModulesWithBasis` |
| interface declarations | `modules.Modules:WithBasis` |
| implementation or binding | `algebras.Algebras:WithBasis [lazy-import binding]; bialgebras.Bialgebras:WithBasis [lazy-import binding]; coalgebras.Coalgebras:WithBasis [lazy-import binding]; hopf_algebras.HopfAlgebras:WithBasis [lazy-import binding]; lambda_bracket_algebras.LambdaBracketAlgebras:WithBasis [lazy-import binding]; lie_algebras.LieAlgebras:FiniteDimensional.WithBasis [lazy-import binding]; lie_algebras.LieAlgebras:WithBasis [lazy-import binding]; lie_conformal_algebras.LieConformalAlgebras:WithBasis [lazy-import binding]; magmatic_algebras.MagmaticAlgebras:WithBasis [nested category class]; modules.Modules:WithBasis [lazy-import binding]; quantum_group_representations.QuantumGroupRepresentations:WithBasis [nested category class]; semisimple_algebras.SemisimpleAlgebras:FiniteDimensional.WithBasis [lazy-import binding]; supercommutative_algebras.SupercommutativeAlgebras:WithBasis [nested category class]; unital_algebras.UnitalAlgebras:WithBasis [nested category class]; vector_spaces.VectorSpaces:WithBasis [nested category class]` |
| method expansions | `modules.Modules:WithBasis -> _with_axiom(WithBasis)` |

## Declared in (16)

| category | declaration | source |
| --- | --- | --- |
| [`Algebras`](../../categories/Algebras.md) | lazy-import binding | [`src/sage/categories/algebras.py:138`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras.py#L138) |
| [`Bialgebras`](../../categories/Bialgebras.md) | lazy-import binding | [`src/sage/categories/bialgebras.py:100`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/bialgebras.py#L100) |
| [`Coalgebras`](../../categories/Coalgebras.md) | lazy-import binding | [`src/sage/categories/coalgebras.py:51`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/coalgebras.py#L51) |
| [`HopfAlgebras`](../../categories/HopfAlgebras.md) | lazy-import binding | [`src/sage/categories/hopf_algebras.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L60) |
| [`LambdaBracketAlgebras`](../../categories/LambdaBracketAlgebras.md) | lazy-import binding | [`src/sage/categories/lambda_bracket_algebras.py:273`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lambda_bracket_algebras.py#L273) |
| [`LieAlgebras`](../../categories/LieAlgebras.md) | lazy-import binding | [`src/sage/categories/lie_algebras.py:175`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L175) |
| [`LieAlgebras`](../../categories/LieAlgebras.md) | lazy-import binding | [`src/sage/categories/lie_algebras.py:171`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L171) |
| [`LieConformalAlgebras`](../../categories/LieConformalAlgebras.md) | lazy-import binding | [`src/sage/categories/lie_conformal_algebras.py:344`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_conformal_algebras.py#L344) |
| [`MagmaticAlgebras`](../../categories/MagmaticAlgebras.md) | nested category class | [`src/sage/categories/magmatic_algebras.py:119`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L119) |
| [`Modules`](../../categories/Modules.md) | lazy-import binding | [`src/sage/categories/modules.py:597`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L597) |
| [`Modules`](../../categories/Modules.md) | subcategory interface method | [`src/sage/categories/modules.py:492`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L492) |
| [`QuantumGroupRepresentations`](../../categories/QuantumGroupRepresentations.md) | nested category class | [`src/sage/categories/quantum_group_representations.py:63`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/quantum_group_representations.py#L63) |
| [`SemisimpleAlgebras`](../../categories/SemisimpleAlgebras.md) | lazy-import binding | [`src/sage/categories/semisimple_algebras.py:113`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semisimple_algebras.py#L113) |
| [`SupercommutativeAlgebras`](../../categories/SupercommutativeAlgebras.md) | nested category class | [`src/sage/categories/supercommutative_algebras.py:61`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/supercommutative_algebras.py#L61) |
| [`UnitalAlgebras`](../../categories/UnitalAlgebras.md) | nested category class | [`src/sage/categories/unital_algebras.py:252`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/unital_algebras.py#L252) |
| [`VectorSpaces`](../../categories/VectorSpaces.md) | nested category class | [`src/sage/categories/vector_spaces.py:182`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L182) |

## Classes the framework generates at 10.10 (5)

| class | module |
| --- | --- |
| `MagmaticAlgebras.WithBasis` | `magmatic_algebras` |
| `QuantumGroupRepresentations.WithBasis` | `quantum_group_representations` |
| `SupercommutativeAlgebras.WithBasis` | `supercommutative_algebras` |
| `UnitalAlgebras.WithBasis` | `unital_algebras` |
| `VectorSpaces.WithBasis` | `vector_spaces` |
