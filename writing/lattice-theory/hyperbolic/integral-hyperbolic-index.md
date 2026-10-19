# Integral hyperbolic index {#sec:integral-hyperbolic-index}

::: {.definition #def:integral-hyperbolic-index title="Integral hyperbolic index"}

Let $U$ be the unimodular hyperbolic plane.
For an integral lattice $L$, define
$$
h_\bZ(L)
\definedas
\max\theset{
n\geq0
\st
\operatorname{PrimEmb}(U^{\perp n},L)\neq\varnothing
}.
$$
:::

::: {.proposition #prop:integral-hyperbolic-vs-witt title="Comparison with the Witt index"}

Let $i_W(L_\bQ)$ be the Witt index of the rational quadratic space $L_\bQ$.
Then
$$
h_\bZ(L)
\leq
i_W(L_\bQ)
\leq
\min(n_+,n_-).
$$
For every
$$
\iota\in\operatorname{PrimEmb}(U^{\perp n},L),
$$
@prop:unimodular-splits gives
$$
U^{\perp n}\perp(U^{\perp n})^{\perp L}
\isoto
L.
$$
Thus $h_\bZ(L)$ is the integral direct-summand refinement of the rational Witt index [@OM00].
:::
