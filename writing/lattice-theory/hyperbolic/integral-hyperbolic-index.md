# Integral hyperbolic index {#sec-integral-hyperbolic-index}

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

Let $L$ be a *nondegenerate* integral lattice, let $i_W(L_\bQ)$ be the Witt index of @def:witt-index of the rational quadratic space $L_\bQ$, and let $(n_+,n_-)$ be its signature in the sense of @def:signature.
Then
$$
h_\bZ(L)
\leq
i_W(L_\bQ)
\leq
\min(n_+,n_-),
$$
so $h_\bZ(L)$ is the integral, direct-summand refinement of the rational Witt index [@OM00].
Nondegeneracy is a hypothesis and not a convenience: over a nonzero radical every subspace of the radical is totally isotropic, so $i_W$ counts vectors that contribute nothing to the signature, and the second inequality fails where $L$ is degenerate.
:::

::: {.proof}

An embedding of $U^{\perp n}$ into $L$ is an embedding of the rational space $U^{\perp n}\otimes_\bZ\bQ$, which is split of dimension $2n$; a split form has a totally isotropic subspace of dimension $n$, so $n\leq i_W(L_\bQ)$ and hence $h_\bZ(L)\leq i_W(L_\bQ)$.

That such an embedding cuts off an orthogonal summand is @prop:unimodular-splits, applied to the perfect summand $U^{\perp n}$: for $\iota\in\operatorname{PrimEmb}(U^{\perp n},L)$ it gives
$$
U^{\perp n}\perp(U^{\perp n})^{\perp L}
\isoto
L.
$$
That is what distinguishes $h_\bZ$ from $i_W$: the rational index counts isotropic subspaces, the integral one counts orthogonal summands isomorphic to $U^{\perp n}$.

For the second inequality, let $W\subseteq L_\bQ$ be totally isotropic and let $L_\bQ=V^{+}\perp V^{-}$ be a decomposition as in @thm:sylvester, with $\dim V^{\pm}=n_{\pm}$ and $V^{-}$ negative definite.
If $w\in W$ has zero component in $V^{+}$ then $w\in V^{-}$, and $0=b(w,w)=b(w^{-},w^{-})$ forces $w=0$.
So the projection to $V^{+}$ is injective on $W$ and $\dim W\leq n_+$; exchanging the roles of $V^{+}$ and $V^{-}$ gives $\dim W\leq n_-$.
Hence $i_W(L_\bQ)\leq\min(n_+,n_-)$.
:::
