# Miranda–Morrison obstructions {#sec-miranda-morrison}

Let $L$ be a nondegenerate indefinite even integral lattice of rank at least $3$, with quadratic discriminant form $A_{L,q}$ from @def:discriminant. Put $V\definedas L_\bQ$, $\widehat{\bZ}\definedas\prod_p\bZ_p$, and $\widehat L\definedas L\tensor_\bZ\widehat{\bZ}$.

## Adelic determinant and spinor data

::: {.definition #def:mm-adelic-det-spinor title="Adelic determinant–spinor character"}

For each prime $p$, write
$$
\Gamma_p\definedas\theset{\pm1}\times
\qty{\bQ_p^\times/(\bQ_p^\times)^2},
\qquad
\Gamma_{p,0}\definedas\theset{\pm1}\times
\qty{\bZ_p^\times/(\bZ_p^\times)^2}.
$$
The **adelic determinant–spinor group** is the restricted product
$$
\Gamma_{\mathbb A_f}\definedas
\prod_p^{\prime}(\Gamma_p,\Gamma_{p,0}).
$$
The determinant and the spinor norm of @def:spinor-norm give
$$
\sigma_{\mathbb A_f}\colon\Orth(V_{\mathbb A_f})
\longrightarrow\Gamma_{\mathbb A_f}.
$$
Write $\Gamma_\bQ\hookrightarrow\Gamma_{\mathbb A_f}$ for the diagonal image of
$\Gamma_\bQ:=\theset{\pm1}\times\bQ^\times/(\bQ^\times)^2$.
:::

::: {.definition #def:mm-integral-spinor-data title="Integral determinant–spinor images"}

The action of $\Orth(\widehat L)$ on the quadratic discriminant form defines the discriminant kernel
$$
\widetilde\Orth(\widehat L)\definedas
\ker\qty{\Orth(\widehat L)\longrightarrow\Orth(A_{L,q})}.
$$
Define the two subgroups of $\Gamma_{\mathbb A_f}$ by the image factorizations
$$
\Sigma(L)\hookrightarrow\Gamma_{\mathbb A_f},
\qquad
\Sigma(L)=\operatorname{im}\qty{\sigma_{\mathbb A_f}\big|_{\Orth(\widehat L)}},
$$
and
$$
\Sigma^\sharp(L)\hookrightarrow\Sigma(L),
\qquad
\Sigma^\sharp(L)=\operatorname{im}\qty{\sigma_{\mathbb A_f}\big|_{\widetilde\Orth(\widehat L)}}.
$$
The subgroup $K_L\hookrightarrow\Sigma(L)$ is the pullback in $\mathbf{Ab}$
```tikzcd
K_L \arrow[r] \arrow[d] & \Sigma(L) \arrow[d,hook] \\
\Gamma_\bQ \arrow[r,hook] & \Gamma_{\mathbb A_f}.
```
In particular, $K_L=\Gamma_\bQ\cap\Sigma(L)$ inside $\Gamma_{\mathbb A_f}$ [@MM09, Ch. VIII, §§2–5].
:::

## The obstruction and genus groups

::: {.definition #def:mm-obstruction-group title="Miranda–Morrison group"}

Define the **Miranda–Morrison obstruction group** $\operatorname{MM}(L)$ by the cokernel sequence in $\mathbf{Ab}$
$$
\Gamma_\bQ\times\Sigma^\sharp(L)
\xrightarrow{(q,s)\mapsto qs}
\Gamma_{\mathbb A_f}
\twoheadrightarrow\operatorname{MM}(L)
\too0.
$$
Thus $\operatorname{MM}(L)$ retains the adelic determinant–spinor obstruction after rational and discriminant-trivial integral isometries are accounted for.
:::

::: {.definition #def:mm-genus-group title="Genus group"}

Define the **genus group** $g(L)$ by the cokernel sequence in $\mathbf{Ab}$
$$
\Gamma_\bQ\times\Sigma(L)
\xrightarrow{(q,s)\mapsto qs}
\Gamma_{\mathbb A_f}
\twoheadrightarrow g(L)
\too0.
$$
Strong approximation identifies its distinguished pointed set with the class set $\Cl(L)=\pi_0\operatorname{Gen}(L)$ of @def:genus [@MM09, Ch. VIII, Cor. 3.2].
:::

::: {.theorem #thm:miranda-morrison title="The Miranda–Morrison exact sequence"}

There is a homomorphism $\delta_L\colon\Orth(A_{L,q})\to\operatorname{MM}(L)$ and an exact sequence in $\mathbf{Grp}$
$$
1\too\widetilde\Orth(L)
\too\Orth(L)
\xrightarrow{\rho_{L,q}}\Orth(A_{L,q})
\xrightarrow{\delta_L}\operatorname{MM}(L)
\too g(L)\too1.
$$
For $\varphi\in\Orth(A_{L,q})$, choose $h\in\Orth(\widehat L)$ inducing $\varphi$ on $A_{L,q}$. Then
$$
\delta_L(\varphi)
=
\pi_{\operatorname{MM}(L)}\qty{\sigma_{\mathbb A_f}(h)},
$$
where $\pi_{\operatorname{MM}(L)}$ is the cokernel morphism of @def:mm-obstruction-group. The value is independent of the choice of $h$.

Moreover, the subgroup $K_L\Sigma^\sharp(L)\hookrightarrow\Sigma(L)$ gives the exact sequence
$$
1\too K_L\Sigma^\sharp(L)\too\Sigma(L)
\twoheadrightarrow\ker\qty{\operatorname{MM}(L)\to g(L)}
\too1.
$$
In particular, the final quotient here is the **kernel of the genus morphism**, not $\operatorname{MM}(L)$ in general [@MM09, Ch. VIII, Thm. 5.1].
:::

::: {.proof}
The local lifting theorem and strong approximation for the spin group give the displayed sequence by [@MM09, Ch. VIII, Thms. 2.3 and 5.1]. Two adelic lifts of $\varphi$ differ by an element of $\widetilde\Orth(\widehat L)$, whose determinant–spinor image belongs to $\Sigma^\sharp(L)$, proving independence of the lift.

For the final sequence, the kernel of the canonical epimorphism $\operatorname{MM}(L)\to g(L)$ is the image of $\Sigma(L)$ under the cokernel projection. Its kernel on $\Sigma(L)$ is
$$
\Sigma(L)\cap\bigl(\Gamma_\bQ\Sigma^\sharp(L)\bigr)
=
\qty{\Sigma(L)\cap\Gamma_\bQ}\Sigma^\sharp(L)
=K_L\Sigma^\sharp(L).
$$
The first isomorphism theorem gives the asserted short exact sequence.
:::

::: {.corollary #cor:nikulin-mm-vanishing title="Nikulin's criterion for vanishing obstructions"}

Let $L$ be an even indefinite integral lattice of rank at least $3$. Write $\ell_p(A_L)$ for the length of its $p$-primary discriminant module and $q_{L,2}$ for its $2$-primary quadratic discriminant form. Assume
1. $\rank L\geq\ell_p(A_L)+2$ for every odd prime $p$;
2. if $\rank L=\ell_2(A_L)$, then $q_{L,2}$ has an orthogonal summand isometric to the rank-two form $u$ or $v$ of @thm:2elementary-decomposition.

Then the discriminant representation $\rho_{L,q}$ is surjective, $L$ is unique in its genus, and
$$
\operatorname{MM}(L)=0,\qquad g(L)=1.
$$
:::

::: {.proof}
Nikulin's surjectivity and uniqueness theorem [@Nik80, Thm. 1.14.2] gives the first two assertions. Exactness of @thm:miranda-morrison then gives the vanishing of both obstruction groups.
:::
