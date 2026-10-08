# Indefinite even $2$-elementary lattices {#sec:indefinite-two-elementary-lattices}

::: {.definition #def:two-elementary-isotropic-types title="Primitive isotropic-vector types"}

Let $L$ be an even $2$-elementary lattice.
For every primitive vector, $\div_L(v)\in\theset{1,2}$.
Since multiplication by $2$ annihilates $A_L^\sharp$, one has $N_b(L)\mid2$.
Hence the bilinear value module admits the canonical monomorphism
$$
j_L\colon
\tfrac1{N_b(L)}\bZ/\bZ
\injects
\tfrac12\bZ/\bZ.
$$
Let
$$
r_L\colon
\tfrac2{N_q(L)}\bZ/2\bZ
\too
\tfrac12\bZ/\bZ
$$
be the restriction of the canonical quotient $\bQ/2\bZ\to\bQ/\bZ$.

For $v$ with $\div_L(v)=2$, its discriminant class $v^*\in A_L^\sharp$ from @def:lattice-basic-invariants is **characteristic** when
$$
r_L\qty{q_L(x)}
=
j_L\qty{\bar{\beta}_L(v^*,x)}
\qquad
\text{for every }x\in A_L^\sharp.
$$
Otherwise $v^*$ is **ordinary**.

For $e\in L^{\mathrm{prim}}[0]$, define its type by

1. **odd** when $\div_L(e)=1$;

2. **even ordinary** when $\div_L(e)=2$ and $e^*$ is ordinary;

3. **even characteristic** when $\div_L(e)=2$ and $e^*$ is characteristic.
:::

::: {.theorem #thm:two-elementary-classification title="Nikulin's classification of indefinite even $2$-elementary lattices"}

Let $L$ be an indefinite even $2$-elementary lattice.
Set $r\definedas\rank_\bZ L$ and $a\definedas\dim_{\bF_2}(A_L^\sharp)$.
Let $i_{2,L}\colon\bZ/2\bZ\injects\tfrac2{N_q(L)}\bZ/2\bZ$ be the canonical monomorphism.
Define $\delta(L)=0$ when there exists a quadratic morphism
$q_L^{(2)}\colon A_L^\sharp\too\bZ/2\bZ$ for which
```tikzcd
A_L^\sharp \arrow[r,"q_L^{(2)}"] \arrow[dr,"q_L"'] &
\bZ/2\bZ \arrow[d,"i_{2,L}"] \\
& \tfrac2{N_q(L)}\bZ/2\bZ
```
commutes, and set $\delta(L)=1$ otherwise.

Then the integral isometry class of $L$ is determined by its signature and $(r,a,\delta(L))$, subject to the admissibility conditions of [@Nik80, Thm. 3.6.2].
:::

::: {.theorem #thm:isotropic-trichotomy title="Primitive isotropic vectors in a hyperbolic $2$-elementary lattice"}

Let $S$ be an even hyperbolic $2$-elementary lattice with invariants $(r,a,\delta)$, and let $v\in S^{\mathrm{prim}}[0]$.
Let $\kappa_v\colon v^{\perp_S}\injects S$ be the right orthogonal-complement kernel of $\iota_v\colon\generators{v}_{\bZ}\injects S$ from @def:orthogonal-complement. By @prop:primitive-isotropic-complement its nondegenerate reduction is $\qty{v^{\perp_S}}^{\mathrm{nd}}$.

Then exactly one of the following holds [@AE22, Prop. 5.5]:

1. If $v$ is odd, $S\isoto U\perp\qty{v^{\perp_S}}^{\mathrm{nd}}$, and $\qty{v^{\perp_S}}^{\mathrm{nd}}$ has invariants $(r-2,a,\delta)$.

2. If $v$ is even ordinary, $S\isoto U(2)\perp\qty{v^{\perp_S}}^{\mathrm{nd}}$, and $\qty{v^{\perp_S}}^{\mathrm{nd}}$ has invariants $(r-2,a-2,\delta)$.

3. If $v$ is even characteristic, $S\isoto\latI_{1,1}(2)\perp\qty{v^{\perp_S}}^{\mathrm{nd}}$, necessarily $\delta=1$, and $\qty{v^{\perp_S}}^{\mathrm{nd}}$ has invariants $(r-2,a-2,0)$.

In every case $\qty{v^{\perp_S}}^{\mathrm{nd}}$ is even negative definite of rank $r-2$.
:::
