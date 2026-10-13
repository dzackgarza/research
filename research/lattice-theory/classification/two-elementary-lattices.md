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

For $v$ with $\div_L(v)=2$, its discriminant class $[v^*]\in A_L^\sharp$ from @def:lattice-discriminant-class is **characteristic** when
$$
r_L\qty{q_L(x)}
=
j_L\qty{\bar{\beta}_L([v^*],x)}
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
Let $j_{q,L}\colon W_q(L)\injects\bQ/2\bZ$ be the coefficient inclusion of @def:discriminant. Define $\delta(L)=0$ when the image of the composite $j_{q,L}\circ q_L$ lies in the canonical submodule $\bZ/2\bZ\injects\bQ/2\bZ$, and define $\delta(L)=1$ otherwise.
Equivalently, $\delta(L)=0$ when the value submodule $\operatorname{Val}(q_L)$ of @def:form-axioms factors through $\bZ/2\bZ\injects\bQ/2\bZ$.

The integral isometry class of $L$ is determined by its signature $(p,q)$, generator length $a$, and coparity $\delta(L)$. Conversely, for integers $p,q\ge1$, $a\ge0$, and $\delta\in\{0,1\}$, an indefinite even $2$-elementary lattice with these invariants exists exactly when
$$
\begin{aligned}
&a\le p+q,\qquad p+q+a\equiv0\pmod2,\\
&\delta=0\ \Longrightarrow\ p-q\equiv0\pmod4,\\
&a=0\ \Longrightarrow\ \delta=0,\ p-q\equiv0\pmod8,\\
&a=1\ \Longrightarrow\ p-q\equiv\pm1\pmod8,\\
&a=2,\ p-q\equiv4\pmod8\ \Longrightarrow\ \delta=0,\\
&\delta=0,\ a=p+q\ \Longrightarrow\ p-q\equiv0\pmod8.
\end{aligned}
$$
This is the existence and uniqueness classification [@Nik80, Thm. 3.6.2].
:::

::: {.theorem #thm:two-elementary-surjectivity title="Nikulin's surjectivity theorem"}
Let $L$ be an even indefinite nondegenerate $2$-elementary lattice. Its quadratic discriminant representation is surjective; thus its discriminant kernel fits into the exact sequence of groups
$$
1\too\widetilde\Orth(L)\too\Orth(L)
\xrightarrow{\rho_{L,q}}\Orth(A_{L,q})\too1.
$$
This is [@Nik80, Thm. 3.6.3].
:::

::: {.corollary #cor:twoelementary-complement-lifting title="Extension of isometries across a $2$-elementary complement"}
Let $L$ be even unimodular, let $\iota_S\colon S\injects L$ be a primitive embedding of nondegenerate lattices, and let $T=S^{\perp_L}$ be indefinite and $2$-elementary. Every $\varphi\in\Orth(S)$ extends to an isometry of $L$ preserving the embedded sublattice $S$.

Writing $\Stab_{\Orth(L)}(S)$ for the stabilizer of $\iota_S(S)$, the restriction and extension morphisms give the exact group sequence
$$
1\too\widetilde\Orth(T)
\longrightarrow\Stab_{\Orth(L)}(S)
\xrightarrow{\operatorname{res}_S}\Orth(S)\too1.
$$
:::

::: {.proof}
Let $\gamma_q\colon A_{S,q}\xrightarrow{\sim}A_{T,q}(-1)$ be the discriminant anti-isometry of @thm:nikulin-gluing. For $\varphi\in\Orth(S)$, the discriminant isometry $\gamma_q\circ\rho_{S,q}(\varphi)\circ\gamma_q^{-1}$ is realized by some $\psi\in\Orth(T)$, by surjectivity in @thm:two-elementary-surjectivity. The compatibility equation of @cor:lifting-unimodular then extends $\varphi\perp\psi$ to $L$. The kernel of the restriction consists of those $\psi\in\Orth(T)$ inducing the identity on $A_{T,q}$, namely $\widetilde\Orth(T)$; its extension to $L$ fixes $S$ pointwise.
:::

::: {.corollary #cor:twoelementary-mm-obstructions title="Vanishing of the Miranda–Morrison obstruction"}
For an even indefinite $2$-elementary lattice $L$ of rank at least $3$, the Miranda–Morrison obstruction and genus groups of @def:mm-obstruction-group and @def:mm-genus-group are trivial:
$$
\operatorname{MM}(L)=0,\qquad g(L)=1.
$$
:::

::: {.proof}
Nikulin's indefinite classification @thm:two-elementary-classification makes the genus of $L$ a single integral isometry class, so $g(L)=1$. By @thm:two-elementary-surjectivity, the discriminant representation is onto. Exactness of the full Miranda–Morrison sequence of @thm:miranda-morrison then gives $\operatorname{MM}(L)=0$.
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
