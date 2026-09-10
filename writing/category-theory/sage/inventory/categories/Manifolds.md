# Manifolds

| field | value |
| --- | --- |
| module | `manifolds` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](../../categories/Category_over_base_ring.md) |
| source | [`src/sage/categories/manifolds.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L19) |
| loads at 10.10 | yes |

## Local axiom paths

- `AlmostComplex`
- `Analytic`
- `Connected`
- `Differentiable`
- `FiniteDimensional`
- `Smooth`

## Other local category paths

- `Complex`

## Declared features (13)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AlmostComplex`](../../axioms/AlmostComplex.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:288`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L288) |
| [`AlmostComplex`](../../axioms/AlmostComplex.md) | axiom | subcategory interface method | `_with_axiom(AlmostComplex)` | [`src/sage/categories/manifolds.py:199`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L199) |
| [`Analytic`](../../axioms/Analytic.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:267`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L267) |
| [`Analytic`](../../axioms/Analytic.md) | axiom | subcategory interface method | `_with_axiom(Analytic)` | [`src/sage/categories/manifolds.py:179`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L179) |
| `Complex` | derived category shorthand | subcategory interface method | `ComplexManifolds(self.base())._with_axioms(...); calls ComplexManifolds()` | [`src/sage/categories/manifolds.py:220`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L220) |
| [`Connected`](../../axioms/Connected.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:323`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L323) |
| [`Connected`](../../axioms/Connected.md) | axiom | subcategory interface method | `_with_axiom(Connected)` | [`src/sage/categories/manifolds.py:98`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L98) |
| [`Differentiable`](../../axioms/Differentiable.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:239`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L239) |
| [`Differentiable`](../../axioms/Differentiable.md) | axiom | subcategory interface method | `_with_axiom(Differentiable)` | [`src/sage/categories/manifolds.py:138`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L138) |
| [`FiniteDimensional`](../../axioms/FiniteDimensional.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:312`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L312) |
| [`FiniteDimensional`](../../axioms/FiniteDimensional.md) | axiom | subcategory interface method | `_with_axiom(FiniteDimensional)` | [`src/sage/categories/manifolds.py:117`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L117) |
| [`Smooth`](../../axioms/Smooth.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/manifolds.py:246`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L246) |
| [`Smooth`](../../axioms/Smooth.md) | axiom | subcategory interface method | `_with_axiom(Smooth)` | [`src/sage/categories/manifolds.py:159`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L159) |

## Axiom-generated classes at 10.10 (6)

| class | module | axiom |
| --- | --- | --- |
| `Manifolds.AlmostComplex` | `manifolds` | `AlmostComplex` |
| `Manifolds.Analytic` | `manifolds` | `Analytic` |
| `Manifolds.Connected` | `manifolds` | `Connected` |
| `Manifolds.Differentiable` | `manifolds` | `Differentiable` |
| `Manifolds.FiniteDimensional` | `manifolds` | `FiniteDimensional` |
| `Manifolds.Smooth` | `manifolds` | `Smooth` |
