# Anticanonical pairs, charge, and MMP singularities

## Anticanonical pairs and their charge

::: {.definition #def:anticanonical-pair defines="anticanonical pair; length; labeled anticanonical pair"}

An **anticanonical pair** $(V, D)$ consists of a smooth rational surface $V$ and a divisor $D\in\abs{-K_V}$ that is a reduced cycle of rational curves $D = \sum_{i=1}^r D_i$, with $i$ taken mod $r$, together with an orientation (@def:free-module-orientation) of $D$.
For $r\geq 2$, each $D_i$ is a smooth rational curve, and $D_i$ meets (@def:replete-full-meet) $D_{i\pm1}$ transversally.
For $r = 1$, $D = D_1$ is an irreducible nodal (@def:nodal-enriques-surface) curve.
The integer $r = r(D)$ is the **length** of $D$.
The pair is **labeled** if the components of $D$ are indexed as above [@Fri15, Sec. 1].
:::

::: {.definition #def:charge defines="charge; $Q(V,D)$"}

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

Let $(V, D)$ be an anticanonical pair (@def:anticanonical-pair) whose divisor $D$ is a cycle of rational curves.

- **Corner blowups**, at nodes of $D$ (points where two components of $D$ meet (@def:replete-full-meet)), preserve the charge (@def:charge).

- **Interior blowups**, at smooth points of $D$ (points lying on a single component of $D$), increase the charge by $1$

[@Fri15, Lem. 2.2(iii)].
Moreover, $Q(V, D)\geq0$, and $Q(V, D) = 0$ if and only if $(V, D)$ is toric [@Fri15, Lem. 2.7].
:::

::: {.definition #def:toric-model-anticanonical title="Toric models of anticanonical pairs" defines="toric model"}

A *toric model* of an anticanonical pair (@def:anticanonical-pair) $(V,D)$ is a diagram of pairs
$$
(V,D) \longleftarrow (V',D') \longrightarrow (\bar V,\bar D),
$$
where $(\bar V,\bar D)$ is a smooth toric surface with its toric boundary, $V'\to V$ is a sequence of corner blowups at nodes of $D$, and $V'\to\bar V$ is the contraction of the exceptional curves of a sequence of interior blowups at smooth points of the boundary. The boundary on the corner blowup is the reduced inverse image; on an interior blowup it is the strict (@def:monoidal-category) transform [@AE22, §6.1].

The diagram gives a birational map $V\dashrightarrow\bar V$ through their common model $V'$. The intermediate $V'$ need not be toric: its map to the toric surface contracts curves created by interior blowups. Thus “toric model” names the toric target (@def:globular-boundary) of the diagram, rather than every surface in it [@AE22, §6.1].
:::

::: {.theorem #thm:anticanonical-toric-model title="Existence of toric models"}

Every anticanonical pair (@def:anticanonical-pair) admits a toric model as in @def:toric-model-anticanonical [@AE22, §6.1].
:::

::: {.proof}

This is [@AE22, Lem. 6.3], which is [@GHK15, Prop. 1.3].
:::

::: {#fig-anticanonical-interior-blowups .figure}
\input{tikz/dissertation/NontoricBlowups.tikz}

Nine interior blowups of the toric boundary of $\PP^1\times\PP^1$; the exceptional curves are drawn on the right.
:::

::: {.proposition #prop:charge-counts-interior-blowups title="Charge counts interior blowups"}

For any toric model (@def:toric-model-anticanonical) of $(V,D)$, the number of interior blowups is $Q(V,D)$.
:::

::: {.proof}

The toric pair $(\bar V,\bar D)$ has charge (@def:charge) $0$ by @prop:charge-under-blowup. Each interior blowup raises charge by $1$, and each corner blowup preserves it. Thus the charge of $(V',D')$ is the number of interior blowups and equals the charge of $(V,D)$ [@AE22, §6.1].
:::

::: {.example #ex:nine-interior-blowups title="Nine interior blowups of $\PP^1\times\PP^1$"}

Let $D$ be the four toric boundary curves on $\PP^1\times\PP^1$. Blow up nine distinct smooth points of $D$, away from its nodes, and let $D'$ be its strict transform. The pair $(V',D')$ is anticanonical and has charge $9$ by @prop:charge-counts-interior-blowups. @fig-anticanonical-interior-blowups shows the blowup centers and exceptional curves.
:::

::: {.theorem #thm:friedman-miranda-charge title="Friedman--Miranda charge theorem"}

Let $\mcx \to (C, 0)$ be a Type III Kulikov degeneration of $K3$ surfaces with central fiber (@def:fiber-cofiber)
$$
\mcx_0 = \Union_{i=1}^n V_i
.
$$
Let $\tilde V_i$ be the normalization of $V_i$, and let $\tilde D_i$ be the inverse image in $\tilde V_i$ of the double curve of $\mcx_0$ on $V_i$, so that each $(\tilde V_i, \tilde D_i)$ is an anticanonical pair (@def:anticanonical-pair).
Then the sum of the charges (@def:charge) of all components is exactly $24$:
$$
\Sum_{i=1}^n Q(\tilde V_i, \tilde D_i) = 24
$$
[@FM83, Prop. 3.7].
:::

## Singularities in the minimal model program

::: {.definition #def:discrepancy defines="discrepancy; $a(E, X, D)$; $\operatorname{discrep}(X, D)$"}

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

::: {.definition #def:mmp-singularities defines="terminal pair; canonical pair; Kawamata log terminal (klt) pair; purely log terminal (plt) pair; log canonical (lc) pair"}

With discrepancies as in @def:discrepancy, write $D = \Sum_i a_i D_i$ with distinct prime divisors $D_i$.
The pair $(X, D)$ is

- **terminal (@def:terminal-coble-surface)** if $\operatorname{discrep}(X, D) > 0$;

- **canonical** if $\operatorname{discrep}(X, D) \geq 0$;

- **Kawamata log terminal (klt)** if $\operatorname{discrep}(X, D) > -1$ and $\lfloor D\rfloor\leq0$;

- **purely log terminal (plt)** if $\operatorname{discrep}(X, D) > -1$;

- **log canonical (lc)** if $\operatorname{discrep}(X, D) \geq -1$

[@KM98, Def. 2.34].
:::

::: {.definition #def:divisorial-log-terminal title="Divisorial log terminal pairs" defines="divisorial log terminal (dlt) pair"}

Let $X$ be a normal variety and let $D = \Sum_i a_i D_i$ be a sum of distinct prime divisors with $0\leq a_i\leq1$, such that $m(K_X + D)$ is Cartier for some $m > 0$.
The pair $(X, D)$ is **divisorial log terminal (@def:terminal-coble-surface) (dlt)** if there is a closed (@def:closed-monoidal) subset $Z\subset X$ such that:

1. $X\sm Z$ is smooth and $D|_{X\sm Z}$ is an snc divisor;

2. if $f\colon Y\to X$ is birational and $E\subset Y$ is an irreducible divisor with $\operatorname{center}_X E\subset Z$, then $a(E, X, D) > -1$

[@KM98, Def. 2.37].
:::

::: {.definition #def:demi-normal-slc defines="demi-normal scheme; semi-log canonical (slc) pair"}

- A scheme (@def:scheme-as-lrs) $X$ is **demi-normal** if it satisfies Serre's condition $S_2$ and each of its codimension-$1$ points is a regular (@def:regular-ternary-lattice) point or a node [@Kol23a, Def. 11.10].

- Let $X$ be demi-normal, with normalization $\pi\colon\bar X\to X$ and conductors $\Sigma\subset X$ and $\bar\Sigma\subset\bar X$.
  Let $D$ be an effective $\RR$-divisor on $X$ whose support contains no irreducible component of $\Sigma$, and let $\bar D$ be the divisorial part of $\pi^{-1}(D)$.
  The pair $(X, D)$ is **semi-log canonical (slc)** if $K_X + D$ is $\RR$-Cartier and $(\bar X, \bar\Sigma + \bar D)$ is log canonical [@Kol23a, Def. 11.11].
:::
