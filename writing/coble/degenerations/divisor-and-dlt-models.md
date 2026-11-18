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
3. That is the whole of what the sources determine, and it is what the method uses but not what the ledger's question asks: (1) makes the data a function of the Picard--Lefschetz transform and (2) makes their output the *combinatorial type* of the limit, so $B(\lambda)$ computes a candidate whose combinatorial type is the limit's; whether that candidate is the limit is not decided by (1) and (2) and is not asserted here.
4. The point-level reading is open, and the proof of it on this page is withdrawn. It rested on the step "a degeneration at a $1$-cusp has the Picard--Lefschetz transform of the cusp", which is false: the transform is $T = \exp N$ with
$$
N(x) = (x\cdot\lambda)e - (x\cdot e)\lambda,
$$
$e$ primitive isotropic and $\lambda\in e^\perp/e$ the monodromy invariant, and when $\lambda^2 = 0$, $\lambda\neq0$ it is the *plane* $(\ZZ e\oplus\ZZ\lambda)_{\mathrm{sat}}$ that defines the $1$-cusp [@AE22, §6A, arXiv:2208.10383v2, p. 28]. One $1$-cusp therefore carries a cone of monodromy invariants, two limits at it need not share a transform, and the recovery of $j$ from the pair [@AEGS25, proof of Theorem 5.9, printed p. 612] separates limits at a *fixed* $\lambda$ only given an argument that $\lambda$ is fixed on the locus in question. No such argument is in this record, and the claim that the data do not determine the pair goes with it.
5. The point-level reading is therefore open, and it is @qst:ia-data-pair-determinacy.

So the ledger's question is answered in the affirmative at the level of the combinatorial type, which is the level at which the sources prove it and at which the divisor-model method uses it; the point-level reading is neither a theorem nor a refuted conjecture, and it is @qst:ia-data-pair-determinacy.
:::

::: {.question #qst:ia-data-pair-determinacy title="Do the integral-affine data determine the limit itself, and not only its combinatorial type?"}

A pair of divisor models with one Picard--Lefschetz transform, one $(\Gamma(\mcx_0),R_{\IA})$ and non-isomorphic KSBA stable limits would answer no, and so would a locus of $\widetilde{\fentwo}$ on which the transform is constant and which is of positive dimension, which no finite map carries to a point [@AEGS25, proof of Theorem 5.9, printed p. 612].
The literature's own construction is where such a pair belongs: at a fixed transform the models of a combinatorial type are the deformations of the gluings and of the moduli of the components [@AEGS25, §4.1, printed p. 598], and the Type II period takes values in the elliptic curve of the double curve [@AE22, §6A, arXiv:2208.10383v2, p. 29], whose $j$ the pair recovers [@AEGS25, proof of Theorem 5.9, printed p. 612].
What is missing is the pair itself, and with it the definition of the integral-affine polarization on a Type II segment, which is [@ABE22, Definition 5.17] as [@AEGS25, §4.1, printed p. 598] cites it; ABE22 is not in `tmp/sources`, and no computation here builds either model.
:::

::: {.proof}

(1) is the sentence of [@AEGS25, §4.1, printed p. 599] that states the constancy for all degenerations with a fixed Picard--Lefschetz transform and attributes it to [@AE23, Theorem 8.11(5)].

(2) is the two sentences that follow it in the same paragraph, which name the cones as the loci of pairs of a fixed combinatorial type, after [@AE23, Corollary 8.13 and Theorem 9.3]. That a stratum of the compactification is a cone is the construction of the semifan and of the semitoroidal compactification [@AEGS25, §5.2, printed p. 610], and $\widetilde{\fentwo}$ is that compactification [@AEGS25, Theorem 5.9, printed p. 611].

(3) is (1) with (2): the data are a function of the transform, and (2) gives their output a combinatorial type; nothing read here identifies the point of the stratum with them.

(4) is the printed form of the transform. [@AE22, §6A, arXiv:2208.10383v2, p. 28] reads $T = \exp N$ with $N(x) = (x\cdot\lambda)e - (x\cdot e)\lambda$, $e$ primitive isotropic and $\lambda\in e^\perp/e$ the monodromy invariant, and separates the cases: $\lambda^2>0$ is Type III, where $\ZZ e$ defines the $0$-cusp, and $\lambda^2 = 0$, $\lambda\neq0$ is Type II, where $(\ZZ e\oplus\ZZ\lambda)_{\mathrm{sat}}$ defines the $1$-cusp. The monodromy invariant is thus not a function of the $1$-cusp, which is what the withdrawn step assumed.

The K3 setting of the conjecture needs nothing further for (1) and (2): the same two facts are printed for $\overline{\mathcal F}_{(2,2,0)}$, whose normalization is semitoroidal [@AEGS25, §5.2, printed p. 610, from @AE22] and which has two $0$-cusps and eight $1$-cusps [@AEGS25, §3.1, printed p. 589].
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
