# Orthogonal complements of lattice embeddings {#sec:lattice-orthogonal-complements}

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
