# Divisor models and dlt degenerations

## dlt models and involution pairs

::: {.definition #def:dlt-model title="dlt models and half-divisor models"}

Let $\mcx \to (C,0)$, resp. $(\mcx,\mcr)\to(C,0)$, be a Kulikov model, resp. a divisor model (@def:coble-divisor-model), of Enriques K3 surfaces on which the Enriques involution (@def:enriques-surface) $\iota_\En$ is a regular involution of $\mcx$, resp. a regular involution that preserves $\mcr$.
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

For Enriques surface (@def:enriques-surface) degenerations we study *involution pairs* $(X, D, \iota)$, where $X$ is the K3 cover limit, $D$ is the boundary, and $\iota$ is the involution.
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

Let $\mcx \to (C,0)$ be a Kulikov model of Enriques K3 surfaces, and assume that the Enriques involution (@def:enriques-surface) of the general fiber extends to an involution $\iota_{\En,0}$ of the central fiber.

1. If $0\in C$ maps to a $0$-cusp of $\overline{F}^{BB}_{(10,10,0)}$, then $\Gamma(\mcx_0)$ is a $2$-sphere.
   At the $0$-cusp $(10,10,0)_1$ the action of $\iota_{\En,0}$ on $\Gamma(\mcx_0)$ is an antipodal involution, and the quotient is $\RP^2$.
   At the $0$-cusp $(10,8,0)_1$ the action is a hemispherical involution, and the quotient is a disc $\Dc^2$.

2. In Type $\latII$, $\Gamma(\mcx_0)$ is a segment.
   At the cusp $(8,8,0)_0$ the involution flips the segment, and at the cusp $(8,6,0)_0$ it fixes the segment

[@AEGS25, Sec. 3.2].

Let $(\mcz,\mcr_\mcz)\to(C,0)$ be a half-divisor model (@def:dlt-model) for $\fentwo$ for the divisor models of [@AEGS25, Prop. 4.5].
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
3. The determination of the limit itself fails, and at a $1$-cusp the reason is a count. The boundary component of a $1$-cusp of $\overline{\mathcal F}^{BB}_{\En,2}$ is a half-plane [@Ste91, §4.1, printed p. 15], computed as $H/\Gamma^1(2)$ and, in the remaining cases, as $H/\Gamma'$ with $\Gamma'$ containing the level $2$ subgroup of $SL_2(\mathbb{Z})$ [@Ste91, §4.3.16 and §4.3.17, printed p. 27]; uncountably many values of the classical $j$ therefore occur over one cusp, and each is a KSBA stable limit [@AEGS25, §5.3, printed p. 611] whose $j$ the limit itself carries [@AEGS25, proof of Theorem 5.9, printed p. 612]. Against that, a monodromy invariant at a fixed cusp is a class in $J/\ZZ e$, of rank one, hence countably many, and every one of them is admissible because $J$ is totally isotropic. Were each $\lambda$ attached to a single $j$, the $j$ realised over the cusp would be countable. So one $\lambda$ occurs at two different $j$; the two limits have the same $(\Gamma(\mcx_0),R_{\IA})$ by (1) and are non-isomorphic. The lattice premises of the count are `computations/reports/coble_678-lambda-versus-j-run.txt`, with its script.
4. So the data determine the stratum and not the point, and computing $B(\lambda)$ computes a candidate of the limit's combinatorial type. The hinge of the divisor-model method is (1) with (2), which is a theorem; the forward direction to the limit is false, and (3) is why.

So the conjecture is false as stated, and what replaces it is the pair (1) and (2): the data determine the stratum, and the point inside the stratum is the period.
:::

::: {.proof}

(1) is the sentence of [@AEGS25, §4.1, printed p. 599] that states the constancy for all degenerations with a fixed Picard--Lefschetz transform and attributes it to [@AE23, Theorem 8.11(5)].

(2) is the two sentences that follow it in the same paragraph, which name the cones as the loci of pairs of a fixed combinatorial type, after [@AE23, Corollary 8.13 and Theorem 9.3]. That a stratum of the compactification is a cone is the construction of the semifan and of the semitoroidal compactification [@AEGS25, §5.2, printed p. 610].

(3) has four steps: two from the printed record, two computed.

- *Uncountably many $j$ over the cusp.* A rational boundary component of the period domain $\Omega_-$ with $\operatorname{sgn}L_- = (2,10)$ is a singleton for a rank $1$ isotropic $I$ and a half-plane for a rank $2$ one [@Ste91, §4.1, printed p. 15]; the one-dimensional components are computed as $H/\Gamma^1(2)$ with $\Gamma^1(2)$ a congruence subgroup of $SL_2(\mathbb{Z})$ [@Ste91, §4.3.16, printed p. 27], and in the remaining cases $\Gamma'$ contains the level $2$ subgroup $\Gamma(2)$ [@Ste91, §4.3.17, printed p. 27]. A quotient $H/\Gamma'$ of the upper half plane by a congruence subgroup is uncountable and the classical $j$ is non-constant on it, so its values there are uncountable. The points over the cusp are the KSBA stable limits of degenerations in $\fentwo$ [@AEGS25, §5.3, printed p. 611], and a Type II boundary point's $j$ is recovered from its stable pair [@AEGS25, proof of Theorem 5.9, printed p. 612].

- *Countably many $\lambda$ at the cusp.* The transform is $T = \exp N$ with $N(x) = (x\cdot\lambda)e - (x\cdot e)\lambda$ and the $1$-cusp is the plane $(\ZZ e\oplus\ZZ\lambda)_{\mathrm{sat}}$ [@AE22, §6A, arXiv:2208.10383v2, p. 28], so $\lambda$ and $\lambda + ce$ give one transform, and a $\lambda$ at the fixed cusp $J$ is a class in $J/\ZZ e$. The script builds $T_\En = U\oplus U(2)\oplus E_8(2)$, computes $\operatorname{rank}J = 2$ and $\operatorname{rank}\ZZ e = 1$, hence $\operatorname{rank}J/\ZZ e = 1$, and enumerates the classes by the coordinate $b$ of $\lambda$ in that lattice, which is unbounded: countably infinite.

- *Admissibility excludes nothing.* On one explicit primitive isotropic plane $J$ the script verifies $\lambda\cdot\lambda' = 0$ for all $\lambda,\lambda'$ in $J$, so $\lambda^2 = 0$ — the Type II value of $\lambda^2$ [@AE22, §6A, p. 28] — holds for every $\lambda$ at this cusp; it also computes $\operatorname{rank}J^\perp/J = 8$, the fibre lattice that the Type II boundary carries [@AET23, §3C, printed p. 17].

- *The count, and what it is not.* The $j$ over the cusp are uncountable and the $\lambda$ countable, so one $\lambda$ carries two limits at different $j$. This is a count of two sets. The record computes its lattice premises and contains no construction of a limit, because no operation available here constructs one: the pair of limits is produced by the count and is not exhibited.

The K3 setting of the conjecture falls to the same count with its own pages: for $\overline{\mathcal F}_{(2,2,0)}$ the normalization is semitoroidal [@AEGS25, §5.2, printed p. 610, from @AE22], the $1$-cusps are printed with their finite morphism to the $j$-line [@AET23, §3B, printed p. 16] — that is the $F_{2d}$ case itself, not a parallel one — and the preimage of a $1$-cusp is the fibration in quotients of $J^\perp/J\otimes E$ [@AET23, §3C, printed p. 17].
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
