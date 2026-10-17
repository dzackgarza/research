# Divisor models and dlt degenerations

::: {.remark}

This section collects three models used to describe degenerations of K3 and Enriques surfaces and their KSBA stable limits: the *dlt* (divisorially log terminal) models of stable involution pairs, the *divisor models* of a degeneration of pairs, and the *half-divisor models* obtained by an involution quotient.
The three are related: a half-divisor model is the quotient of a divisor model by an involution, and the dlt models supply the birational models on whose strata the associated combinatorial data live.
:::

::: {.question}
The source notes describe the relationship of these models to the KSBA program (below); they do not discuss the relationship to Kulikov models explicitly.
If a Kulikov comparison is intended here, supply it.
:::

::: {.remark}
The dlt, divisor and half-divisor models here are those of the Alexeev--Engel--Garza--Schaffler degree-$2$ Enriques program [@AEGS25], used in the Morrison degenerations section in the same form.
:::

## dlt models and involution pairs

Here a *dlt model* refers to a relative divisorially-log-terminal model of the degeneration supplying these boundary strata; the definition below is of the associated *stable involution pair* $(X, D, \iota)$.

::: {.definition #def:dlt-involution-pair title="dlt models and involution pairs"}

For Enriques surface degenerations we study *stable involution pairs* $(X, D, \iota)$, where $X$ is the K3 cover limit, $D$ is the boundary, and $\iota$ is the involution.
The canonical condition
$$
K_X + D \sim 0
$$
holds.

The quotient $Y = X/\iota$ has branch divisor $B$ and image boundary $C = \pi(D)$, where $\pi\colon X \to Y$ is the quotient map.
The pair $(Y, C)$ is a log del Pezzo surface of index at most $2$, satisfying
$$
K_X + D + \eps R = \pi^*\left( K_Y + C + \frac{1+\eps}{2}B \right)
,
$$
where $R$ is the ramification divisor of $\pi$.
:::

::: {.remark title="Dual complex topology"}

The topology of the dual complex of the central fiber $Y_0'$ distinguishes the degeneration types:

- Generic Type III (e.g. Coxeter type $\widetilde{E}_8 + \widetilde{E}_8$): the dual complex of $Y_0'$ is a projective plane $\RP^2$, with the involution acting antipodally on $S^2$.

- Other Type III / Type II (e.g. $\widetilde{E}_8 + \widetilde{D}_{10}$): the dual complex is a $2$-disk $\Dc^2$, with the involution acting as a reflection on $S^2$.

- Special Type II cases: the dual complex reduces to a segment.
:::

## Divisor models

::: {.definition #def:coble-divisor-model title="Divisor model"}

A *divisor model* for a degeneration $\pi\colon \mcx \to C$ of K3 (or Enriques) surfaces is a degeneration of pairs $(\mcx, \mcr) \to C$ where:

1. $\mcr$ is a Cartier divisor, effective on all fibers.

2. For $t \neq 0$, $\mcr_t$ is semiample.

3. $\mcr$ is disjoint from the singular strata of the central fiber $\mcx_0$.

The geometry is encoded by an *integral-affine divisor* $R_{\IA} \subset \Gamma(\mcx_0)$, which assigns weights to the double curves reflecting the intersection with $\mcr_0$, satisfying a balancing condition at every vertex.
:::

## Half-divisor models

::: {.definition #def:coble-half-divisor-model title="Half-divisor model"}

A *half-divisor model* is a pair $(\mcz, \mcr_{\mcz})$ over a base curve $C$ that arises as the quotient of a divisor model $(\mcx, \mcr) \to C$ by a fixed-point-free involution $\tau$ under which $\mcr$ is $\tau$-invariant, $\tau^*\mcr = \mcr$.
The class $\mcr$ descends to $\mcz$ only up to the $2$-torsion twist $K_{\mcz}$ (the two $\ZZ/2$-linearizations of the invariant $\mcr$ differ by the sign character of $\tau$); this is why $\mcr_{\mcz}$ is Weil but not Cartier, while $2\mcr_{\mcz}$ is Cartier.

This naturally models limits of polarized Enriques surfaces, where the polarization does not descend to a Cartier divisor on the Enriques quotient.

Boundary strata for Enriques stable limits are modeled by pairs $(\mcz_0, \tfrac{1}{2}\mcr_{\mcz_0})$ with $K_{\mcz_0} + \tfrac{1}{2}\mcr_{\mcz_0}$ ample and slc singularities.
:::

::: {.remark title="Half-divisor models from the Enriques involution"}

Equivalently, a half-divisor model arises when a divisor model $(\mcx, \mcr)$ admits an Enriques involution $\iota_\En$ preserving $\mcr$; the quotient is
$$
(\mcz, \mcr_{\mcz})
= (\mcx, \mcr) / \iota_\En
.
$$
Its KSBA stable limit can be computed directly from the relative $\Proj$ of its section ring.
:::
