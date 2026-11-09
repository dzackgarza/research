# Orthogonal complements of lattice embeddings {#sec-lattice-orthogonal-complements}

The left and right orthogonal-complement kernels are defined in @def:orthogonal-complement.
For $\iota_v\colon\generators{v}_{\bZ}\injects L$, write $\kappa_v\colon v^{\perp_L}\injects L$ for its right orthogonal-complement kernel.
When $v$ is isotropic, $v^{\perp_L}$ is degenerate with nondegenerate reduction $\qty{v^{\perp_L}}^{\mathrm{nd}}$.

::: {.proposition #prop:primitive-isotropic-complement title="Primitive isotropic complements"}

Let $L$ be a nondegenerate integral lattice and let $v\in L^{\mathrm{prim}}[0]$.
Isotropy gives a unique monomorphism $\lambda_v\colon\generators{v}_{\bZ}\injects v^{\perp_L}$ with $\kappa_v\circ\lambda_v=\iota_v$.
For the radical monomorphism $\rho_v\colon\radic(v^{\perp_L})\injects v^{\perp_L}$, there is a unique isomorphism
$\bar{\lambda}_v\colon\generators{v}_{\bZ}\isoto\radic(v^{\perp_L})$ with $\rho_v\circ\bar{\lambda}_v=\lambda_v$.
Consequently
$$
0
\too
\generators{v}_{\bZ}
\xrightarrow{\lambda_v}
v^{\perp_L}
\xrightarrow{p_v}
\qty{v^{\perp_L}}^{\mathrm{nd}}
\too
0
$$
is exact in $\mathbf{BilMod}_{\bZ}$.
:::

::: {.proof}
Flat base change along $\bZ\to\bQ$ sends the kernel defining $v^{\perp_L}$ to the kernel defining $v^{\perp_{L_\bQ}}$.
Nondegeneracy of $L_\bQ$ and isotropy of $v$ give $\radic\qty{v^{\perp_{L_\bQ}}}=\bQ v$.
Primitivity of $\iota_v$ gives the Cartesian square

```tikzcd
\generators{v}_{\bZ} \arrow[r,hook,"\iota_v"] \arrow[d,hook] &
L \arrow[d,hook] \\
\bQ v \arrow[r,hook] &
L_\bQ .
```

Hence $\radic(v^{\perp_L})$ is the pullback of $\bQ v\injects v^{\perp_{L_\bQ}}$ along $v^{\perp_L}\injects v^{\perp_{L_\bQ}}$, so $\bar{\lambda}_v$ is an isomorphism.
The displayed sequence is the defining cokernel sequence of the nondegenerate reduction.
:::

::: {.proposition #prop:isotropic-complement-embedding title="Splitting an isotropic orthogonal complement"}

Under the hypotheses of @prop:primitive-isotropic-complement, applying $U\colon\mathbf{BilMod}_{\bZ}\too\bZ\text{-}\mathbf{Mod}$ to its exact sequence gives a split exact sequence, and $\qty{v^{\perp_L}}^{\mathrm{nd}}$ admits an embedding into $L$ in $\mathbf{Lat}_{\bZ}$.
:::

::: {.proof}
By @prop:primitive-characterization choose $\epsilon\in\Hom_{\bZ\text{-}\mathbf{Mod}}(L,\bZ)$ with $\epsilon(v)=1$.
Set $\epsilon_v\definedas\epsilon\circ\kappa_v$.
Then $\epsilon_v(v)=1$. Define $r_v\colon U(v^{\perp_L})\too U(\generators{v}_{\bZ})$ by $r_v(x)=\epsilon_v(x)v$; then $r_v\circ U(\lambda_v)=\id$.
Define
$$
s_{\epsilon_v}\colon
\qty{v^{\perp_L}}^{\mathrm{nd}}
\too
v^{\perp_L},
\qquad
s_{\epsilon_v}([x])=x-\epsilon_v(x)v.
$$
If $x'=x+nv$, then $x'-\epsilon_v(x')v=x-\epsilon_v(x)v$, so $s_{\epsilon_v}$ is well defined and $p_v\circ s_{\epsilon_v}=\id$.
For $x,y\in v^{\perp_L}$,
$$
\beta_L\qty{x-\epsilon_v(x)v,\,y-\epsilon_v(y)v}=\beta_L(x,y),
$$
because $v$ lies in $\radic(v^{\perp_L})$.
Thus $s_{\epsilon_v}$ preserves the induced bilinear form, and
$$
j_{\epsilon_v}\definedas
\kappa_v\circ s_{\epsilon_v}\colon
\qty{v^{\perp_L}}^{\mathrm{nd}}
\injects
L
$$
is an embedding in $\mathbf{Lat}_{\bZ}$.
:::

::: {.proposition #prop:discriminant-orthogonal-sum title="Discriminants of orthogonal sums"}

Let $L_1,\dots,L_n$ be integral lattices with $n\geq1$, and set $L\definedas L_1\perp\cdots\perp L_n$.
Let $N_b$ denote the bilinear denominator of @def:discriminant, and set
$$
N\definedas\operatorname{lcm}_{1\leq i\leq n}N_b(L_i),
\qquad
W\definedas\tfrac1N\bZ/\bZ.
$$
Then $N_b(L)=N$.
For the canonical value-module monomorphisms
$u_i\colon\tfrac1{N_b(L_i)}\bZ/\bZ\injects W$,
$$
A_L
\isoto
(u_1)_*A_{L_1}
\perp\cdots\perp
(u_n)_*A_{L_n}
$$
in $\mathcal B_{\bZ,W}$.

If every $L_i$ is even, let $N_q$ denote the quadratic level of @def:lattice-level and set
$$
N_q'\definedas\operatorname{lcm}_{1\leq i\leq n}N_q(L_i),
\qquad
W_q\definedas\tfrac2{N_q'}\bZ/2\bZ.
$$
For the canonical monomorphisms
$u_{q,i}\colon\tfrac2{N_q(L_i)}\bZ/2\bZ\injects W_q$,
$$
N_q(L)=N_q',
\qquad
A_{L,q}
\isoto
(u_{q,1})_*A_{L_1,q}
\perp\cdots\perp
(u_{q,n})_*A_{L_n,q}.
$$
:::

::: {.proof}
The metric dual is additive under finite orthogonal sums,
$$
L^\#
\isoto
L_1^\#\oplus\cdots\oplus L_n^\#,
$$
and additivity of cokernels gives
$$
A_L^\sharp
\isoto
\bigoplus_{i=1}^n A_{L_i}^\sharp.
$$
Therefore $N_b(L)=\operatorname{lcm}_{1\leq i\leq n}N_b(L_i)$.
For $x_i\in L_i^\#$ and $x_j\in L_j^\#$ with $i\ne j$, orthogonality gives $\beta_{L_\bQ}(x_i,x_j)=0$, while the form on the $i$th summand is $u_i\circ\bar{\beta}_{L_i}$.
This gives the displayed isometry in $\mathcal B_{\bZ,W}$.

If every $L_i$ is even, then for $x_i\in L_i^\#$,
$$
q_L\qty{\sum_i x_i}=\sum_i q_{L_i}(x_i)
$$
because $\beta_{L_\bQ}(x_i,x_j)=0$ for $i\ne j$.
Hence $N_q(L)=\operatorname{lcm}_{1\leq i\leq n}N_q(L_i)$, and the quadratic discriminant isometry follows.
:::

## Isotropic reduction and the cusp quotient {#sec-isotropic-reduction}

A primitive totally isotropic sublattice $P\leq L$ determines the cusp lattice $Q=P^{\perp_L}/P$.
The finite subgroup of $A_L$ cut out by $P$ is the isotropic subgroup $D(P)$ of @not:isotropic-reduction-setup, and $A_Q\isoto D(P)^{\perp}/D(P)$ by @thm:isotropic-reduction-discriminant.

::: {.notation #not:isotropic-reduction-setup title="The data of an isotropic reduction"}

Let $L\in\mathbf{Lat}_{\bZ}^{\mathrm{nd}}$ be integral and let $P\leq L$ be a primitive totally isotropic sublattice of rank $r\geq1$.
Put
$$
V\definedas P_{\bQ},
\qquad
W\definedas V^{\perp_{L_{\bQ}}},
\qquad
M\definedas P^{\perp_L}=L\cap W,
\qquad
Q\definedas M/P .
$$
Because $V$ is totally isotropic one has $V\subseteq W$, and because both are $\bQ$-subspaces of $L_{\bQ}$ the sublattices $P=L\cap V$ and $M=L\cap W$ are saturated in $L$.
Primitivity of $P$ is exactly the statement $L\cap V=P$, so $P\subseteq M$ and $Q$ is a lattice.
Write $N\definedas L^{\#}$ for the metric dual of @def:metric-dual and set
$$
N_V\definedas N\cap V,
\qquad
D(P)\definedas\im\qty(N_V\too A_L),
\qquad
H\definedas\theset{x\in N\st\beta_{L_{\bQ}}(x,N_V)\subseteq\bZ}.
$$
Since $N$ is the metric dual of @def:metric-dual one has $\beta_{L_{\bQ}}(L,N)\subseteq\bZ$, and $N_V\subseteq N$, so $L\subseteq H$;
and $x\in N$ represents a class of $D(P)^{\perp}$ exactly when $\beta_{L_{\bQ}}(x,N_V)\subseteq\bZ$.
Hence
$$
D(P)^{\perp}/D(P)=H/(L+N_V).
$$

The subgroup $D(P)$ is the image of $N_V$ in the ambient group $A_L=N/L$, so it is the subquotient
$$
D(P)=\frac{N_V+L}{L}\cong\frac{N_V}{N_V\cap L}=\frac{N_V}{P},
\qquad
\cardinality{D(P)}=[N_V:P],
$$
the middle isomorphism being Noether's, with $N_V\cap L=N\cap V\cap L=P$ because $L\cap V=P$.
The subgroup is determined by $V$ alone, and it is totally isotropic: every class of $D(P)$ has a representative in the totally isotropic subspace $V$, so $\beta_{L_{\bQ}}$ vanishes on $V\times V$ and, when $L$ is even, $q_{A_L}$ vanishes there as well.
This is the isotropy that makes $D(P)^{\perp}/D(P)$ a quadratic subquotient, and it is a property of $P$ alone.

:::

The first lemma is the only place where the metric dual of the quotient is compared with the metric dual of $L$; it is what an element of $Q^{\#}$ uses to obtain a representative in $N$.

::: {.lemma #lem:isotropic-reduction-pairing title="The pairing of the isotropic subspace with $L/M$, and the metric dual it computes"}

With the data of @not:isotropic-reduction-setup, the pairing with $L$ induces an isomorphism of $\bQ$-vector spaces
$$
\theta\colon
V\isoto\Hom_{\bZ\text{-}\mathbf{Mod}}(L/M,\bQ),
\qquad
\theta(v)(\bar\ell)=\beta_{L_{\bQ}}(v,\ell),
$$
and the composite $V\too\Hom_{\bZ\text{-}\mathbf{Mod}}(L/M,\bQ)\too\Hom_{\bZ\text{-}\mathbf{Mod}}(L/M,\bQ/\bZ)$ is surjective with kernel $N_V$.
:::

::: {.proof}

For $v\in V\subseteq W$ one has $\beta_{L_{\bQ}}(v,M)=0$, so $\theta(v)$ is defined on classes and $\theta$ is $\bQ$-linear.
If $\theta(v)=0$ then $v$ pairs trivially with $L$, hence with $L_{\bQ}$, so $v=0$ by nondegeneracy of $L_{\bQ}$; thus $\theta$ is injective.
Both sides have rank $r$, so $\theta$ is an isomorphism.

The coefficient morphism $\bQ\too\bQ/\bZ$ is surjective and $L/M$ is free of rank $r$ by @prop:primitive-characterization, so a functional $L/M\too\bQ/\bZ$ lifts along a basis of $L/M$ to a functional $L/M\too\bQ$; the composite is therefore surjective.
Its kernel consists of those $v\in V$ with $\beta_{L_{\bQ}}(v,L)\subseteq\bZ$, that is of $N\cap V=N_V$.
:::

::: {.lemma #lem:isotropic-reduction-extension title="Dual extension along the isotropic subspace, and choice independence"}

With the data of @not:isotropic-reduction-setup let $y\in Q^{\#}$ and let $\tilde y\in W$ lift $y$.
Then:

1. $\beta_{L_{\bQ}}(\tilde y,M)\subseteq\bZ$;
2. there exists $u\in V$ with $\tilde y+u\in N$, and the set of such $u$ is a coset of $N_V$;
3. $\beta_{L_{\bQ}}(\tilde y,N_V)=0$, and consequently $\tilde y+u\in H$ for every $u$ as in item 2;
4. the class of $\tilde y+u$ in $H/(L+N_V)$ depends only on $y$, not on the lift $\tilde y$ nor on the correction $u$.
:::

::: {.proof}

*Item 1.* For $m\in M$ the value $\beta_{Q_{\bQ}}(y,\bar m)$ is $\beta_{L_{\bQ}}(\tilde y,m)$, because $\tilde y$ represents $y\in W/V$ with $m\in M\subseteq W$, and on the restricted form of $W$ the subspace $V$ satisfies $\beta_{L_{\bQ}}(V,V)=0$ and $\beta_{L_{\bQ}}(W,V)=0$, so replacing $\tilde y$ by another lift in $W$ changes it by an element of $V$ and does not change the value; the hypothesis $y\in Q^{\#}$ therefore gives $\beta_{L_{\bQ}}(\tilde y,M)\subseteq\bZ$.

*Item 2.* By item 1 the functional $\ell\mapsto\beta_{L_{\bQ}}(\tilde y,\ell)$ is integral on $M$, so its reduction modulo $\bZ$ vanishes on $M$ and it descends to a functional $\bar\lambda\colon L/M\too\bQ/\bZ$.
By @lem:isotropic-reduction-pairing choose $u\in V$ with $\theta(u)\equiv-\bar\lambda$, that is $\beta_{L_{\bQ}}(u,\ell)\equiv-\beta_{L_{\bQ}}(\tilde y,\ell)\pmod{\bZ}$ for all $\ell\in L$; then $\tilde y+u\in N$.
If $u,u'$ both have this property, then $\beta_{L_{\bQ}}(u-u',L)\subseteq\bZ$, so $u-u'\in N\cap V=N_V$; conversely adding an element of $N_V$ preserves the property because $\beta_{L_{\bQ}}(N_V,L)\subseteq\bZ$.

*Item 3.* Since $\tilde y\in W=V^{\perp}$ and $N_V\subseteq V$ one has $\beta_{L_{\bQ}}(\tilde y,N_V)=0$, and since $V$ is totally isotropic one has $\beta_{L_{\bQ}}(u,N_V)=0$.
Together with $\tilde y+u\in N$ this states $\tilde y+u\in H$.

*Item 4.* Lifts of $y$ differ by an element of $V$, and representatives of $y$ modulo $Q$ — that is, changes of $\tilde y$ by an element of $M$ — are changes by an element of $L$. Two lifts in $W$ therefore differ by some $v\in V$.
Let $u,u'$ be the corrections of item 2 for $\tilde y,\tilde y+v$.
Then $(\tilde y+u)-(\tilde y+v+u')\in V$, and it is a difference of two elements of $N$, so it lies in $N\cap V=N_V\subseteq L+N_V$.
A change $\tilde y\mapsto\tilde y+m$ with $m\in M$ changes $\hat y=\tilde y+u$ by $m\in L$; the sum remains in $H$ because $\beta_{L_{\bQ}}(M,N_V)\subseteq\beta_{L_{\bQ}}(W,V)=0$, and its class moves by an element of $L$.
Both changes therefore leave the class in $H/(L+N_V)$ fixed.
:::

The two lemmas give the comparison map. Its injectivity is formal; its surjectivity is where an index identity is needed, and @lem:isotropic-reduction-index supplies one rather than a matching of invariant factors. That identity is proved first, since the theorem's surjectivity is read off from it.

::: {.lemma #lem:isotropic-reduction-index title="The index identity of an isotropic reduction"}

With the data of @not:isotropic-reduction-setup,
$$
\cardinality{A_L}=\cardinality{A_Q}\cdot[N_V:P]^2,
\qquad\text{equivalently}\qquad
\abs{\disc L}=\abs{\disc Q}\cdot[N_V:P]^2 .
$$
:::

::: {.proof}

By @prop:primitive-characterization the quotient $L/P$ is free, and $M/P$ is saturated in it because $M$ is saturated in $L$; choose a $\bZ$-basis $v_1,\dots,v_r$ of $P$, a $\bZ$-basis $\bar u_1,\dots,\bar u_s$ of $M/P$ with lifts $u_1,\dots,u_s\in M$, and lifts $w_1,\dots,w_r\in L$ completing to a basis of $L/P$.
Then $(v,u,w)$ is a $\bZ$-basis of $L$, the pair $(v,u)$ is a $\bZ$-basis of $M$, and $s=\rank Q=\rank L-2r$.
In this basis the Gram matrix of $L$ is
$$
G=\begin{pmatrix}
0 & 0 & B\\
0 & G_Q & C\\
B^{\mathsf T} & C^{\mathsf T} & E
\end{pmatrix},
\qquad
B_{ij}=\beta_{L_{\bQ}}(v_i,w_j),
$$
where the $v$–$v$ block vanishes by isotropy, the $v$–$u$ block vanishes because $u\subseteq M=P^{\perp_L}$, and $G_Q$ is the Gram matrix of the basis $\bar u$ of $Q$.
Since $\det G\neq0$, an element $x=\sum_i\lambda_i v_i$ with $B^{\mathsf T}\lambda=0$ satisfies $\beta_{L_{\bQ}}(x,w_j)=0$ for every $j$, while $\beta_{L_{\bQ}}(x,u)=0$ because $u\subseteq M=P^{\perp_L}$ and $\beta_{L_{\bQ}}(x,v)=0$ by isotropy; then $x$ is orthogonal to $L_{\bQ}$ and is zero by nondegeneracy, so $\lambda=0$ and $B$ is invertible.

Over $\bQ$, first replace $w_j$ by $w_j-\sum_\ell\qty(G_Q^{-1}C_{\cdot j})_\ell u_\ell$, which is legitimate because $\det G_Q=\pm\disc Q\neq0$. Indeed, on the subspace $W$ the radical of the restricted form is $W\cap W^{\perp_{L_{\bQ}}}=W\cap V=V$, since $V\subseteq W$ is totally isotropic, so the radical of the quotient $Q_{\bQ}=W/V$ is $V/V=0$ and the induced form on $Q_{\bQ}$ is nondegenerate. This kills the $u$–$w$ block while preserving the $v$–$u$ and $v$–$v$ blocks.
Then replace the new $w_j$ by $w_j-\tfrac12\sum_k\qty(B^{-\mathsf T}E'_{\cdot j})_k v_k$, where $E'$ is the resulting $w$–$w$ block; this is legitimate because $B$ is invertible, it kills $E'$ because $E'$ is symmetric, and it does not disturb the other blocks since $V$ is totally isotropic and $\beta_{L_{\bQ}}(u,v)=0$.
In the resulting $\bQ$-basis $(v,u,w'')$ the Gram matrix is $\begin{pmatrix}0&B&0\\B^{\mathsf T}&0&0\\0&0&G_Q\end{pmatrix}$ after reordering, so
$$
\abs{\det G}=\det(B)^2\,\abs{\det G_Q}.
$$

It remains to identify $\det(B)$ with $[N_V:P]$. An element $x=\sum_i\lambda_i v_i$ of $V$ lies in $N$ exactly when $\beta_{L_{\bQ}}(x,L)\subseteq\bZ$, and since $\beta_{L_{\bQ}}(x,M)=0$ this is the single condition $B^{\mathsf T}\lambda\in\bZ^r$.
Hence $N_V=(B^{\mathsf T})^{-1}\bZ^r$, whose covolume in $V$ is $\abs{\det B}^{-1}$ times that of $P=\sum_i\bZ v_i$; therefore $[N_V:P]=\abs{\det B}$.
With $\cardinality{A_L}=\abs{\det G}$ and $\cardinality{A_Q}=\abs{\det G_Q}=\abs{\disc Q}$, the displayed identity follows.
:::

The count of $\cardinality{D(P)^{\perp}/D(P)}$ is a separate statement about the finite form, and it must not be read off from the map whose bijectivity is being proved.
It is duality for an isotropic subgroup of a nondegenerate finite form, and it uses the nondegeneracy of $A_L$ of @prop:discriminant-nondegenerate together with the isotropy recorded in @not:isotropic-reduction-setup.

::: {.lemma #lem:isotropic-subgroup-quotient-order title="The order of the orthogonal subquotient of an isotropic subgroup"}

Let $A$ be a finite abelian group with a nondegenerate pairing $\beta\colon A\times A\too\bQ/\bZ$, and let $D\leq A$ satisfy $D\subseteq D^{\perp}$ for $D^{\perp}=\theset{a\in A\st\beta(a,d)=0 \text{ for all } d\in D}$.
Then the pairing induces an isomorphism $A/D^{\perp}\isoto\Hom_{\bZ\text{-}\mathbf{Mod}}(D,\bQ/\bZ)$, and
$$
\cardinality{D^{\perp}/D}=\frac{\cardinality{A}}{\cardinality{D}^2}.
$$
:::

::: {.proof}

The prescription
$$
\Psi\colon A\longrightarrow\Hom_{\bZ\text{-}\mathbf{Mod}}(D,\bQ/\bZ),
\qquad
\Psi(a)=\beta(a,\cdot)|_D,
$$
is additive, and its kernel is $D^{\perp}$ by the definition of $D^{\perp}$; write $\Phi\colon A/D^{\perp}\to\Hom(D,\bQ/\bZ)$ for the induced map on the quotient, which is therefore well defined and injective.
For surjectivity, let $\lambda\colon D\too\bQ/\bZ$ be a homomorphism; since $\bQ/\bZ$ is a divisible group, $\lambda$ extends to a homomorphism $\Lambda\colon A\too\bQ/\bZ$, and nondegeneracy of $\beta$ on the finite group $A$ provides $a\in A$ with $\Lambda=\beta(a,\cdot)$, that is $\Phi(\bar a)=\lambda$.
Hence $\Phi$ is an isomorphism and $\cardinality{A/D^{\perp}}=\cardinality{D^{\vee}}=\cardinality{D}$.

Since $D\subseteq D^{\perp}$, the quotient $D^{\perp}/D$ is defined and
$$
\cardinality{D^{\perp}/D}
=\frac{\cardinality{D^{\perp}}}{\cardinality{D}}
=\frac{\cardinality{A}/\cardinality{D}}{\cardinality{D}}
=\frac{\cardinality{A}}{\cardinality{D}^2}.
$$
:::

::: {.theorem #thm:isotropic-reduction-discriminant title="The discriminant form of an isotropic reduction: $A_Q\isoto D(P)^{\perp}/D(P)$"}

Let $L\in\mathbf{Lat}_{\bZ}^{\mathrm{nd}}$ be integral, let $P\leq L$ be primitive totally isotropic of rank $r\geq1$, and adopt @not:isotropic-reduction-setup.
By @lem:isotropic-reduction-extension the prescription
$$
\varphi_P\colon
A_Q\longrightarrow D(P)^{\perp}/D(P),
\qquad
[y]\longmapsto[\tilde y+u]+D(P),
$$
with $\tilde y\in W$ any lift of $y$ and $u\in V$ the correction of @lem:isotropic-reduction-extension, is well defined and additive, hence a morphism of finite abelian groups.
It is an isomorphism, and it preserves both forms:
$$
\beta_{A_Q}(y,y')=\beta_{A_L}\qty(\varphi_P(y),\varphi_P(y'))
\qquad\text{for all } y,y'\in A_Q,
$$
and when $L$ is even, so that $Q$ is even,
$$
q_{A_Q}(y)=q_{A_L}\qty(\varphi_P(y))
\qquad\text{for all } y\in A_Q .
$$
The subgroup has order $\cardinality{D(P)}=[N_V:P]$, and
$$
\cardinality{A_Q}=\frac{\cardinality{A_L}}{[N_V:P]^2},
\qquad
D(P)^{\perp}/D(P)\cong A_Q .
$$
Finally $\varphi_P$ is natural in the pair $(L,P)$: for $g\in\Orth(L)$ the isometry $\bar g=\rho_L(g)$ of $A_L$ carries $D(P)$ to $D(gP)$, and the square
$$
\begin{aligned}
A_Q &\xrightarrow{\ \varphi_P\ } & D(P)^{\perp}/D(P)\\
\downarrow{\bar g_Q} & & \downarrow{\bar g_D}\\
A_{gQ} &\xrightarrow{\ \varphi_{gP}\ } & D(gP)^{\perp}/D(gP)
\end{aligned}
$$
commutes, where $\bar g_Q$ is the isometry of $Q$ induced by $g$ and $\bar g_D$ is the map of subquotients
$$
\bar g_D\colon D(P)^{\perp}/D(P)\longrightarrow D(gP)^{\perp}/D(gP),
\qquad
\bar g_D\qty(c+D(P))=\rho_L(g)(c)+D(gP),
$$
which is well defined because $\rho_L(g)$ preserves $\beta_{A_L}$ and carries $D(P)$ onto $D(gP)$; for $g\in\Stab_{\Orth(L)}(P)$ it is an automorphism of $D(P)^{\perp}/D(P)$.
Setting $Q_0\definedas\rho_L(\Orth(L))$, naturality gives the containment
$$
\rho_L\qty(\Stab_{\Orth(L)}(P))\subseteq\Stab_{Q_0}\qty(D(P)),
$$
and the action of $\Stab_{\Orth(L)}(P)$ on $A_Q$ is transported by $\varphi_P$ to its action on $D(P)^{\perp}/D(P)$ through $\rho_L$.
Nothing more is asserted: the exact image is $\rho_L(\Stab_{\Orth(L)}(P))$, and equality with the full finite stabilizer is a lifting statement of @cor:isotropic-reduction-stabilizer.
:::

::: {.proof}

*Well defined and additive.* @lem:isotropic-reduction-extension gives the existence of $u$, the independence of the class in $H/(L+N_V)$, and $\tilde y+u\in H$; and $D(P)^{\perp}/D(P)=H/(L+N_V)$ by @not:isotropic-reduction-setup.
For additivity, let $y,y'$ have representatives $\hat y=\tilde y+u$ and $\hat y'=\tilde y'+u'$ as above and let $u''$ correct $\tilde y+\tilde y'$.
Then $(\tilde y+\tilde y'+u'')-\hat y-\hat y'=u''-u-u'\in V$ is a difference of two elements of $N$, hence lies in $N\cap V=N_V$, so the classes add.

*Injectivity.* Let $\varphi_P(y)=0$. Then $\hat y\in L+N_V$, say $\hat y=\ell+n_V$ with $\ell\in L$ and $n_V\in N_V$.
Since $u\in V$ and $n_V\in V$ we get $\tilde y-\ell=\hat y-u-\ell=n_V-u\in V$, so $\tilde y\equiv\ell\pmod{V}$, and then
$$
\beta_{L_{\bQ}}(\ell,P)=\beta_{L_{\bQ}}(\tilde y,P)-\beta_{L_{\bQ}}(n_V-u,P)=0
$$
because $\tilde y\in W=V^{\perp}$ and $V$ is totally isotropic.
Hence $\ell\in P^{\perp_L}=M$, and $y=[\tilde y]=[\ell]\in M/P=Q$, that is $y=0$ in $A_Q$.

*Surjectivity.* The target has $\cardinality{D(P)^{\perp}/D(P)}=\cardinality{A_L}/\cardinality{D(P)}^2$ by @lem:isotropic-subgroup-quotient-order, applied to the nondegenerate form of $A_L$ of @prop:discriminant-nondegenerate and the isotropic subgroup $D(P)$ of @not:isotropic-reduction-setup; that count is a statement about the finite form and does not use $\varphi_P$.
With $\cardinality{D(P)}=[N_V:P]$ and @lem:isotropic-reduction-index this equals $\cardinality{A_Q}$.
An injective morphism between finite groups of the same order is bijective.

*The bilinear form.* Write $\hat y=\tilde y+u$ and $\hat y'=\tilde y'+u'$ as above, so $\hat y-\tilde y\in V$ and $\hat y'-\tilde y'\in V$.
Here $u,u'\in V=W^{\perp_{L_{\bQ}}}$, so $\beta_{L_{\bQ}}(\tilde y,u')=0$ and $\beta_{L_{\bQ}}(u,\tilde y')=0$; and $V$ is totally isotropic, so $\beta_{L_{\bQ}}(u,u')=0$.
Hence
$$
\beta_{L_{\bQ}}(\hat y,\hat y')=\beta_{L_{\bQ}}(\tilde y,\tilde y')=\beta_{Q_{\bQ}}(y,y'),
$$
the last equality because $\tilde y,\tilde y'$ represent $y,y'$ in $W/V\supseteq Q_{\bQ}$ and $\beta_{L_{\bQ}}$ vanishes on $V\times V$ and on $W\times V$.
Passing to $\bQ/\bZ$ gives the displayed identity of discriminant forms.

*The quadratic form.* Let $L$ be even; then $Q=M/P$ is even because the norms of $M$ are norms of $L$.
Since $\hat y-\tilde y\in V$ is isotropic and orthogonal to $\tilde y$, one has $\hat y^2=\tilde y^2$, and $\tilde y^2=y^2$ in $\bQ/2\bZ$ because a change of lift by $V$ leaves the square unchanged.
Hence $q_{A_L}(\varphi_P(y))=\hat y^2\bmod2\bZ=y^2\bmod2\bZ=q_{A_Q}(y)$.

*Naturality.* Let $g\in\Orth(L)$ and let $\hat y\in H$ represent $\varphi_P(y)$. Then $g\hat y\in L^{\#}$, and $g\hat y-g\tilde y=gu\in gV$, while $g\tilde y\in gW$ lifts $\bar g_Q y$; by the choice independence of @lem:isotropic-reduction-extension the class of $g\hat y$ is $\varphi_{gP}(\bar g_Qy)$.
Its image modulo $D(gP)$ is $\rho_L(g)\qty(\hat y+D(P))$, because $g$ preserves $N$ and carries $V=P_{\bQ}$ to $(gP)_{\bQ}$, so $g(N_V)=L^{\#}\cap(gP)_{\bQ}$ and $\rho_L(g)D(P)=D(gP)$.
The commutativity of the square follows, and restricting to $g\in\Stab_{\Orth(L)}(P)$ gives the stabilizer statement.
:::

::: {.corollary #cor:isotropic-reduction-stabilizer title="The exact image of the parabolic stabilizer, and the action on the subquotient"}

Let the data and hypotheses be those of @thm:isotropic-reduction-discriminant, put $Q_0=\rho_L(\Orth(L))$ for the discriminant representation $\rho_L$ of @def:discriminant-rep, and let
$$
C\definedas\ker\qty(\Stab_{Q_0}\qty(D(P))\too\Aut\qty(D(P)^{\perp}/D(P))).
$$
Then:

1. the image of $\Stab_{\Orth(L)}(P)$ in $\Orth(A_L)$ is exactly $\rho_L(\Stab_{\Orth(L)}(P))$, and it is contained in $\Stab_{Q_0}(D(P))$; it consists of those elements of the finite stabilizer that are realised by an integral isometry preserving $P$;
2. for $g\in\Stab_{\Orth(L)}(P)$ let $\bar g_D$ be the automorphism of $D(P)^{\perp}/D(P)$ induced by $\rho_L(g)$ through the representative action
   $$
   \bar g_D\qty(c+D(P))=\rho_L(g)(c)+D(P),
   $$
   which is well defined because $\rho_L(g)$ carries $D(P)$ to $D(gP)=D(P)$ and preserves $\beta_{A_L}$, hence preserves $D(P)^{\perp}$; then the isometry of $A\definedas A_Q$ induced by $g$ is
   $$
   \bar g_Q=\varphi_P^{-1}\circ\bar g_D\circ\varphi_P,
   $$
   so $\Stab_{\Orth(L)}(P)\too\Orth(A_Q)$ has the same kernel as $\Stab_{\Orth(L)}(P)\too\Aut(D(P)^{\perp}/D(P))$, namely $\Stab_{\Orth(L)}(P)\cap\rho_L^{-1}(C)$;
3. equality $\rho_L(\Stab_{\Orth(L)}(P))=\Stab_{Q_0}(D(P))$ is a lifting statement about the integral stabilizer and is **not** proved here; neither is injectivity of the map in item 2.
:::

::: {.proof}

Item 1 is the containment of @thm:isotropic-reduction-discriminant read as a statement about the image, together with the description of $\rho_L$ as the map that records the action on $A_L$.
For item 2, the commuting square of @thm:isotropic-reduction-discriminant states $\bar g_D\circ\varphi_P=\varphi_{gP}\circ\bar g_Q$; when $g\in\Stab_{\Orth(L)}(P)$ one has $gP=P$ and $gQ=Q$, so it reads $\bar g_D\circ\varphi_P=\varphi_P\circ\bar g_Q$, that is the displayed formula, and composing with $\varphi_P$ identifies the two kernels.
For item 3, the kernel of $\Stab_{\Orth(L)}(P)\too\Orth(A_Q)$ is $\Stab_{\Orth(L)}(P)\cap\rho_L^{-1}(C)$ by item 2, and it contains $\Stab_{\Orth(L)}(P)\cap\widetilde\Orth(L)$, where $\widetilde\Orth(L)=\ker\rho_L$ is the discriminant kernel of @def:discriminant-rep: those isometries act trivially on $A_L$, hence on every subgroup and subquotient of it, and hence on $A_Q$ by item 2.
So the action in item 2 is faithful exactly when $\Stab_{\Orth(L)}(P)\cap\rho_L^{-1}(C)=1$, and in particular it fails to be faithful whenever $\Stab_{\Orth(L)}(P)\cap\widetilde\Orth(L)\neq1$.
Equality in item 3 is a different statement again: it would require an integral isometry preserving $P$ for each element of the finite stabilizer of $D(P)$ in $Q_0$, whereas the commuting square constrains only those elements that already have an integral lift.
So the square neither implies equality in item 3 nor is implied by it, and the isometry $\varphi_P$ of @thm:isotropic-reduction-discriminant is not a substitute for the computation of the integral stabilizer's image.
:::

Two specializations are worth recording, since both are easy to get wrong.

*An integral representative needs the correction.*
An element $\tilde y\in W$ that already lies in $L$ lies in $L\cap W=M$, and its class in $A_L$ is the zero class; the map $[y]\mapsto[\tilde y]$ on such representatives therefore carries all of $A_Q$ to the single class $D(P)$ and is not the comparison of @thm:isotropic-reduction-discriminant.
What makes the comparison work is the correction along $V$ of @lem:isotropic-reduction-extension: it moves the representative into $N$ while leaving its pairing with $M$ and its square unchanged, and it is exactly that movement which records the position of $y$ in $A_Q$.
Equivalently, $\varphi_P(y)$ is the class modulo $L+N_V$ of the unique element of $N$ in the coset $\tilde y+V$, so no choice of basis of $Q$ and no listing of $Q^{\#}$ enters.

*The rank-one case.*
For $r=1$ and $P=\generators{v}$ primitive isotropic, $N_V$ is the cyclic module generated by $v/\div_L(v)$, so $[N_V:P]=\div_L(v)$ and $D(P)=\generators{[v/\div_L(v)]}$; the theorem then identifies $A_{v^{\perp_L}/v}$ with the orthogonal complement of that class modulo itself,
$$
A_{v^{\perp_L}/v}\isoto\generators{c}^{\perp}/\generators{c},
\qquad
c=[v/\div_L(v)]\in A_L .
$$
This is the general form of the cyclic statement, and it holds for every divisibility: the factor $\div_L(v)$ enters only through $\cardinality{D(P)}$.
