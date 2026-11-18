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

The conjecture was that, among divisor models $(\mcx,\mcr)\to C$ with a *fixed* Picard--Lefschetz monodromy, the pair $(\Gamma(\mcx_0),R_{\IA})$ determines the KSBA stable limit of $(\mcx_t,\epsilon\mcr_t)$.
Write $\widetilde{\fentwo}$ for the semitoroidal compactification of $\fentwo$ for the five semifans of [@AEGS25, Theorem 5.9, printed p. 611].

1. The half that holds is constancy at fixed monodromy: $(\Gamma(\mcx_0),R_{\IA})$ can be chosen to be the same for all degenerations with a fixed Picard--Lefschetz transform [@AEGS25, §4.1, printed p. 599, after @AE23, Theorem 8.11(5)].
2. What the data determine is the *combinatorial type* of the limit, and with it the stratum. The cones of a semifan are, by construction, the collections of Picard--Lefschetz transformations for which $(\Gamma(\mcx_0),R_{\IA})$ determines a KSBA-stable pair of a fixed combinatorial type [@AEGS25, §4.1, printed p. 599, after @AE23, Corollary 8.13 and Theorem 9.3], and a stratum of $\widetilde{\fentwo}$ is a cone. So the data name the stratum in which the limit lies, and not the point of it.
3. The other half fails. At a Type II degeneration $\Gamma(\mcx_0)$ is a segment [@AEGS25, §4.1, printed p. 598], so every Type II degeneration at one $1$-cusp carries one $(\Gamma(\mcx_0),R_{\IA})$ by (1); a $1$-cusp is a modular curve [@AEGS25, Definition 2.9, printed p. 588], on which $j$ is not constant. The limit carries that $j$ as an invariant of the pair: its double curve is elliptic with that $j$, or is a $\PP^1$ whose four distinguished $A_1$ points give the double cover with that $j$ [@AEGS25, proof of Theorem 5.9, printed p. 612]. Two Type II degenerations at one $1$-cusp whose $j$ differ therefore have the same $(\Gamma(\mcx_0),R_{\IA})$ and non-isomorphic KSBA stable limits.
4. The freedom is Hodge-theoretic and not combinatorial: the limit is read off the dlt model, that is, off Hodge-theoretic data [@AEGS25, §1, printed p. 583], and the data of (2) do not supply the $j$ of (3).
5. Consequently computing $B(\lambda)$ computes the stratum of the limit and a candidate of the right combinatorial type, and not the limit. The hinge of the divisor-model method is (1) with (2), which is a published theorem, and the forward direction in the form (3) refutes is false.

So the conjecture is false as stated, and what replaces it is the pair (1) and (2): the data determine the stratum, and the point inside the stratum is the period.
:::

::: {.proof}

(1) is the sentence of [@AEGS25, §4.1, printed p. 599] that states the constancy for all degenerations with a fixed Picard--Lefschetz transform and attributes it to [@AE23, Theorem 8.11(5)].

(2) is the two sentences that follow it in the same paragraph, which name the cones as the loci of pairs of a fixed combinatorial type, after [@AE23, Corollary 8.13 and Theorem 9.3]. That a stratum of the compactification is a cone is the construction of the semifan and of the semitoroidal compactification [@AEGS25, §5.2, printed p. 610], and $\widetilde{\fentwo}$ is that compactification [@AEGS25, Theorem 5.9, printed p. 611].

(3) has three steps, each printed. The first is that a Type II degeneration has $\Gamma(\mcx_0)$ a segment [@AEGS25, §4.1, printed p. 598]. The second is that $R_{\IA}$ does not change with the degeneration: the Picard--Lefschetz transform of a degeneration at a $1$-cusp is that of the cusp, so (1) applies and the data are one value on the cusp. The third is that $j$ is an invariant of the limit and moves with the cusp: a $1$-cusp is a modular curve [@AEGS25, Definition 2.9, printed p. 588], where the $j$-invariant of its points is not constant, and the $j$-invariant of a Type II boundary point is recovered from the slc stable pair, through the elliptic double curve or through the double cover of $\PP^1$ branched at the four distinguished $A_1$ points [@AEGS25, proof of Theorem 5.9, printed p. 612]. The double curve is a closed subscheme of the pair, so two limits with different $j$ are non-isomorphic, which with the first two steps is (3).

(4) is [@AEGS25, §1, printed p. 583]: the stable limit of a degeneration in $\fentwo$ is extracted from its dlt model, and that extraction is described there as one from Hodge-theoretic data. The $j$ of (3) is the part of that passage that the dual complex does not see.

(5) collects (1)--(4): the monodromy $\lambda$ and the polarization are what $B(\lambda)$ is computed from, (2) makes their output a stratum together with a combinatorial type, and (3) is the failure of the further step to the point.

The K3 form of the conjecture fails by the same three citations, the two analogous facts being printed for $\overline{\mathcal F}_{(2,2,0)}$: its normalization is semitoroidal [@AEGS25, §5.2, printed p. 610, from @AE22], and it has eight $1$-cusps and two $0$-cusps [@AEGS25, §3.1, printed p. 589], each $1$-cusp a modular curve [@AEGS25, Definition 2.9, printed p. 588]; the segment and the constancy are [@AEGS25, §4.1, printed pp. 598--599] as above, and the double curve of the limit is again part of the pair.
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
