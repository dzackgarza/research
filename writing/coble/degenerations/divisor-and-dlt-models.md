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

For a fixed Picard–Lefschetz transform $\lambda$, the construction of
[@AEGS25, Remark 4.11] establishes half-divisor models for generic
degenerations. On a nongeneric Kulikov model the Enriques involution may
extend only birationally; this can happen already in Type I when the
central fiber acquires a $(-2)$-curve. Contracting the $ADE$
configurations that form its indeterminacy locus makes the involution
regular on the resulting model. Its quotient is generally dlt rather
than a Kulikov-type normal crossings model. Thus @def:dlt-model applies
after the regular action has been obtained; it does not assert that
every chosen Kulikov model carries one.

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

::: {.theorem #thm:ia-data-verdict title="Verdict on the integral-affine-data conjecture"}

The conjecture was that, among divisor models $(\mcx,\mcr)\to C$ with a *fixed* Picard--Lefschetz monodromy, the pair $(\Gamma(\mcx_0),R_{\IA})$ determines the KSBA stable limit of $(\mcx_t,\eps\mcr_t)$.

1. The constancy half is a theorem: $(\Gamma(\mcx_0),R_{\IA})$ can be chosen to be the same for all degenerations with a fixed Picard--Lefschetz transform [@AEGS25, §4.1, printed p. 599, after @AE23, Theorem 8.11(5)].
2. What those data determine is the *combinatorial type* of the limit, and with it the stratum. The cones of a semifan are, by construction, the collections of Picard--Lefschetz transformations for which $(\Gamma(\mcx_0),R_{\IA})$ determines a KSBA-stable pair of a fixed combinatorial type [@AEGS25, §4.1, printed p. 599, after @AE23, Corollary 8.13 and Theorem 9.3], and a stratum of the compactification is a cone.
3. The determination of the limit itself fails, and at a $1$-cusp the reason is a count. The limits over a $1$-cusp $J$ carry the $j$-invariant of a modular curve, uncountably many values, while a monodromy invariant at a fixed cusp ranges over $J/\ZZ e$, a lattice of rank one, and is therefore countable; and all of its values are admissible, since $J$ is totally isotropic and $\lambda^2 = 0$ excludes none of them. Were each $\lambda$ attached to a single $j$, the $j$ realised over $J$ would be at most countable. So one $\lambda$ occurs at two different $j$; the two limits have the same $(\Gamma(\mcx_0),R_{\IA})$ by (1) and are non-isomorphic, since a limit carries the $j$ of its double curve as an invariant of the pair [@AEGS25, proof of Theorem 5.9, printed p. 612]. The count is `computations/reports/coble_678-lambda-versus-j-run.txt`, with its script.
4. So the data determine the stratum and not the point, and computing $B(\lambda)$ computes a candidate of the limit's combinatorial type. The hinge of the divisor-model method is (1) with (2), which is a theorem; the forward direction to the limit is false, and (3) is why.

So the conjecture is false as stated, and what replaces it is the pair (1) and (2): the data determine the stratum, and the point inside the stratum is the period.
:::

::: {.proof}

(1) is the sentence of [@AEGS25, §4.1, printed p. 599] that states the constancy for all degenerations with a fixed Picard--Lefschetz transform and attributes it to [@AE23, Theorem 8.11(5)].

(2) is the two sentences that follow it in the same paragraph, which name the cones as the loci of pairs of a fixed combinatorial type, after [@AE23, Corollary 8.13 and Theorem 9.3]. That a stratum of the compactification is a cone is the construction of the semifan and of the semitoroidal compactification [@AEGS25, §5.2, printed p. 610].

(3) has four steps, and each is either printed or computed.

- *Uncountably many $j$ over the cusp.* The boundary component of a $1$-cusp is a modular curve [@AEGS25, Definition 2.9, printed p. 588], a quotient of the upper half plane by a finite-index group, on which $j$ is a non-constant holomorphic function; the parallel case of $F_{2d}$ is printed with its finite morphism to the $j$-line [@AET23, §3B, printed p. 16]. The points over the cusp are KSBA stable limits of degenerations [@AEGS25, §5.3, printed p. 611], and the preimage of the component in the compactification is a family over it, a fibration in quotients of $J^\perp/J\otimes E$ with $E$ the universal elliptic curve [@AET23, §3C, printed p. 17].

- *Countably many $\lambda$ at the cusp.* The transform is $T = \exp N$ with $N(x) = (x\cdot\lambda)e - (x\cdot e)\lambda$ and the $1$-cusp is the plane $(\ZZ e\oplus\ZZ\lambda)_{\mathrm{sat}}$ [@AE22, §6A, arXiv:2208.10383v2, p. 28], so $\lambda$ and $\lambda + ce$ give one transform and a $\lambda$ at the fixed cusp $J$ is a class in $J/\ZZ e$, of rank one. The script enumerates them and recomputes that rank: the coordinate $b$ of $\lambda$ in $J/\ZZ e$ is unbounded, so the set is countably infinite.

- *Admissibility excludes nothing.* $J$ is totally isotropic — the script verifies $\lambda\cdot\lambda' = 0$ for all $\lambda,\lambda'$ in $J$ — so $\lambda^2 = 0$, the Type II value of $\lambda^2$ [@AE22, §6A, p. 28], holds for every $\lambda$ at this cusp. The computation is one explicit primitive isotropic plane in $T_\En = U\oplus U(2)\oplus E_8(2)$, checked to be primitive and totally isotropic, and the rank-one lattice $J^\perp/J$.

- *The count.* The $j$ over $J$ are uncountable, the $\lambda$ countable; so one $\lambda$ carries two limits at different $j$, and those two are the pair (3) exhibits. This is a count of the two sets and needs no elliptic curve to be built.

The K3 setting of the conjecture falls to the same argument: for $\overline{\mathcal F}_{(2,2,0)}$ the same two facts are printed [@AEGS25, §5.2, printed p. 610, from @AE22; @AEGS25, §3.1, printed p. 589] with the $1$-cusps modular curves as in (3).
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
