# Divisor models and dlt degenerations

## dlt models and involution pairs

::: {.definition #def:dlt-model title="dlt models and half-divisor models"}

Let $\mcx \to (C,0)$, resp. $(\mcx,\mcr)\to(C,0)$, be a Kulikov model, resp. a divisor model (@def:coble-divisor-model), of Enriques K3 surfaces on which the Enriques involution $\iota_\En$ is a regular involution of $\mcx$, resp. a regular involution that preserves $\mcr$.
The **dlt model**, resp. the **half-divisor model**, is the quotient by the Enriques involution:
$$
\mcz \definedas \mcx/\iota_\En,
\qquad\text{resp.}\qquad
(\mcz, \mcr_{\mcz}) \definedas (\mcx, \mcr)/\iota_\En
$$
[@AEGS25, Def. 4.7].
:::

::: {.definition #def:dlt-involution-pair title="dlt models and involution pairs"}

For Enriques surface degenerations we study *involution pairs* $(X, D, \iota)$, where $X$ is the K3 cover limit, $D$ is the boundary, and $\iota$ is the involution.
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

::: {.proposition #prop:enriques-quotient-dual-complex title="Dual complexes of Enriques quotients"}

Let $\mcx \to (C,0)$ be a Kulikov model of Enriques K3 surfaces, and assume that the Enriques involution of the general fiber extends to an involution $\iota_{\En,0}$ of the central fiber.

1. If $0\in C$ maps to a $0$-cusp of $\overline{F}^{BB}_{(10,10,0)}$, then $\Gamma(\mcx_0)$ is a $2$-sphere.
   At the $0$-cusp $(10,10,0)_1$ the action of $\iota_{\En,0}$ on $\Gamma(\mcx_0)$ is an antipodal involution, and the quotient is $\RP^2$.
   At the $0$-cusp $(10,8,0)_1$ the action is a hemispherical involution, and the quotient is a disc $\Dc^2$.

2. In Type $\latII$, $\Gamma(\mcx_0)$ is a segment.
   At the cusp $(8,8,0)_0$ the involution flips the segment, and at the cusp $(8,6,0)_0$ it fixes the segment

[@AEGS25, Sec. 3.2].

Let $(\mcz,\mcr_\mcz)\to(C,0)$ be a half-divisor model for $\fentwo$ for the divisor models of [@AEGS25, Prop. 4.5].
In Type $\mathrm{III}$, $\Gamma(\mcz_0) = \RP^2$ at cusp $1$ and $\Gamma(\mcz_0) = \Dc^2$ at cusps $2$ to $5$.
In Type $\latII$, $\Gamma(\mcz_0)$ is a segment [@AEGS25, Prop. 4.8].
:::

## Divisor models

::: {.definition #def:coble-divisor-model title="Divisor model"}

A *divisor model* for a degeneration $\pi\colon \mcx \to C$ of K3 (or Enriques) surfaces is a degeneration of pairs $(\mcx, \mcr) \to C$ where:

1. $\mcr$ is a Cartier divisor, effective on all fibers.

2. For $t \neq 0$, $\mcr_t$ is semiample.

3. $\mcr$ is disjoint from the singular strata of the central fiber $\mcx_0$.

The geometry is encoded by an *integral-affine divisor* $R_{\IA} \subset \Gamma(\mcx_0)$, which assigns weights to the double curves reflecting the intersection with $\mcr_0$, satisfying a balancing condition at every vertex.
:::

::: {.conjecture #conj:classification-ia-data title="Integral-affine data determine the stable limit"}

Among divisor models $(\mcx,\mcr)\to C$ with a fixed Picard--Lefschetz monodromy, the pair $(\Gamma(\mcx_0),R_{\IA})$ determines the KSBA stable limit of $(\mcx_t,\epsilon\mcr_t)$.
:::

## Half-divisor models

::: {.proposition #prop:half-divisor-stable-limit title="Stable limits from half-divisor models"}

Let $(\mcz,\mcr_\mcz)\to(C,0)$ be a half-divisor model (@def:dlt-model) for $\fentwo$ for the divisor models of [@AEGS25, Prop. 4.5].
Then the fibers of $\mcz$ have slc singularities, $K_\mcz + \eps\mcr_\mcz$ is relatively big and nef over $C$, and $\mcr_\mcz$ contains no log canonical centers [@AEGS25, Prop. 4.8].
The KSBA stable limit of the degeneration $(\mcz^*, \eps\mcr_\mcz^*)\to C^*$ is
$$
\Proj_C \bigoplus_{n\geq0} H^0(\mcz, n\mcr_\mcz)
$$
[@AEGS25, Cor. 4.9].
This stable limit is a point of $\ksbacpt{\fentwo}$, whose points are the pairs $(Z, \eps R_Z)$ and their KSBA stable limits [@AEGS25, Sec. 5.3].
These are pairs $(Z, \eps R_Z)$ with slc singularities and $K_Z\equiv 0$, in which $R_Z$ is an ample $\QQ$-Cartier divisor [@AEGS25, Sec. 1].
:::
