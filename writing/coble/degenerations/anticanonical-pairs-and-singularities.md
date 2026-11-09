# Anticanonical pairs, charge, and MMP singularities

## Anticanonical pairs and their charge

::: {.definition #def:anticanonical-pair}

An **anticanonical pair** $(V, D)$ consists of a smooth projective rational surface $V$ together with a reduced effective snc divisor $D$ such that
$$
K_V + D \sim_{\QQ} 0
.
$$
Anticanonical pairs are also known as **log Calabi--Yau surfaces**.
:::

::: {.definition #def:charge}

Let $V$ be a smooth surface and let $D$ be a reduced effective cycle of rational curves on $V$, with $r(D)$ irreducible components.
The **charge** of $(V, D)$ is
$$
Q(V, D) \definedas 12 - D^2 - r(D)
$$
[@FM83, Def. 3.1; @Fri15, Def. 1.1].
If $D = \Sum_{j=1}^{r} D_j$ is a cycle of $r\geq2$ smooth rational curves meeting transversally, then $D^2 = \Sum_j D_j^2 + 2r$, and so
$$
Q(V, D) = 12 - \Sum_j \left( D_j^2 + 3 \right)
.
$$
:::

::: {.proposition #prop:charge-under-blowup title="Charge under blowup"}

Let $(V, D)$ be an anticanonical pair whose divisor $D$ is a cycle of rational curves.

- **Corner blowups**, at nodes of $D$ (points where two components of $D$ meet), preserve the charge.

- **Interior blowups**, at smooth points of $D$ (points lying on a single component of $D$), increase the charge by $1$

[@Fri15, Lem. 2.2(iii)].
Moreover, $Q(V, D)\geq0$, and $Q(V, D) = 0$ if and only if $(V, D)$ is toric [@Fri15, Lem. 2.7].
:::

::: {.theorem #thm:friedman-miranda-charge title="Friedman--Miranda charge theorem"}

Let $\mcx \to (C, 0)$ be a Type III Kulikov degeneration of $K3$ surfaces with central fiber
$$
\mcx_0 = \Union_{i=1}^n V_i
.
$$
Let $\tilde V_i$ be the normalization of $V_i$, and let $\tilde D_i$ be the inverse image in $\tilde V_i$ of the double curve of $\mcx_0$ on $V_i$, so that each $(\tilde V_i, \tilde D_i)$ is an anticanonical pair.
Then the sum of the charges of all components is exactly $24$:
$$
\Sum_{i=1}^n Q(\tilde V_i, \tilde D_i) = 24
$$
[@FM83, Prop. 3.7].
:::

## Singularities in the minimal model program

::: {.definition #def:discrepancy}

Let $(X, D)$ be a normal pair with $K_X + D$ $\QQ$-Cartier, and let $f\colon Y \to X$ be a birational morphism from a normal variety $Y$.
The **discrepancy** $a(E, X, D)$ of an $f$-exceptional prime divisor $E$ is defined by
$$
K_Y + D_Y = f^*(K_X + D) + \Sum_E a(E, X, D)\, E
,
$$
where $D_Y = f_*^{-1}D$ is the birational transform of $D$ [@KM98, Def. 2.25].
The **discrepancy** of $(X, D)$ is
$$
\operatorname{discrep}(X, D) \definedas \inf_E \theset{a(E, X, D) \mid E \text{ is an exceptional divisor over } X}
$$
[@KM98, Def. 2.28].
:::

::: {.definition #def:mmp-singularities}

With discrepancies as in @def:discrepancy, write $D = \Sum_i a_i D_i$ with distinct prime divisors $D_i$.
The pair $(X, D)$ is

- **terminal** if $\operatorname{discrep}(X, D) > 0$;

- **canonical** if $\operatorname{discrep}(X, D) \geq 0$;

- **Kawamata log terminal (klt)** if $\operatorname{discrep}(X, D) > -1$ and $\lfloor D\rfloor\leq0$;

- **purely log terminal (plt)** if $\operatorname{discrep}(X, D) > -1$;

- **log canonical (lc)** if $\operatorname{discrep}(X, D) \geq -1$

[@KM98, Def. 2.34].
:::

::: {.definition #def:divisorial-log-terminal title="Divisorial log terminal pairs"}

Let $X$ be a normal variety and let $D = \Sum_i a_i D_i$ be a sum of distinct prime divisors with $0\leq a_i\leq1$, such that $m(K_X + D)$ is Cartier for some $m > 0$.
The pair $(X, D)$ is **divisorial log terminal (dlt)** if there is a closed subset $Z\subset X$ such that:

1. $X\sm Z$ is smooth and $D|_{X\sm Z}$ is an snc divisor;

2. if $f\colon Y\to X$ is birational and $E\subset Y$ is an irreducible divisor with $\operatorname{center}_X E\subset Z$, then $a(E, X, D) > -1$

[@KM98, Def. 2.37].
:::

::: {.definition #def:demi-normal-slc}

- A variety $X$ is **demi-normal** if it is reduced, satisfies Serre's condition $S_2$, and has at worst normal crossings in codimension $1$.

- A pair $(X, D)$ is **semi-log canonical (slc)** if $X$ is demi-normal and the normalization, taken with the conductor divisor, $(X^\nu, D^\nu)$ is log canonical.
:::
