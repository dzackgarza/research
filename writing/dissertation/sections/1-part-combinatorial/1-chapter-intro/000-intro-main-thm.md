

## Introduction  {#sec:chapter-1}

The central object needed to define such a compactification is a **KSBA stable pair**: a pair $(Z, \epsilon R_Z)$ where $Z$ is a connected projective variety and $R_Z$ is an effective $\QQ$-divisor such that the pair $(Z, \epsilon R_Z)$ is semi-log canonical for some $0 < \epsilon \leq 1$, and $K_Z + \epsilon R_Z$ is ample.
We will then define KSBA compactifications as closures of spaces of particular types of surface pairs in the space of stable pairs.
When constructing such compactifications, we will often take the divisor $R_Z$ to be the ramification divisor corresponding to a $2$-divisible ample line bundle coming from a branched double-cover construction, i.e. an involution.
We note, however, that explicitly determining or classifying the boundary strata of a given KSBA compactification and the exact stable pairs that appear is nontrivial.
In @AEGS25, we classify the strata of $\bd\cpt{\fent}$, the KSBA compactification of $\fent$, and find that the irreducible components of stable limits of surface pairs are described by **$ADE+BC$ diagrams**, we which we mean the classical Dynkin diagrams corresponding to the semisimple complex Lie algebras of types $A_n, D_n, E_6, E_7, E_8$, which we refer to as simply-laced, and the diagrams of types $B_n$ and $C_n$.
The latter can be obtained from the former by a classically well-known operation called **folding**.

By the work of @AET23, to each such diagram one can associated a pair $(Y, C)$ where $Y$ is a surface, which in many cases is toric, and $C$ is a reduced boundary divisor such that $(Y, C)$ is an lc pair and $-2(K_Y + C)$ is an ample Cartier divisor providing a natural polarization.
This provides a natural association of a classical $ADE+BC$ diagram (decorated with extra combinatorial parity data) to, in many cases, an explicit projective toric variety.
We refer to such surfaces as **$ADE+BC$ surfaces**.
This thesis details the construction of an isomorphism between the normalization of the KSBA stable pair compactification $\cpt{\fent}$ and a semitoroidal compactification $\semitorcpt{\fent}$ for the moduli space of Enriques surfaces with *numerical polarization* of degree 2. The main theorem establishes an isomorphism $\semitorcpt{\fent} \to \ksbacpt{\fent}$ where $\semifans{F} = \ts{ \semifan{F}_k }_{k=1,2,3,4,5}$ is a collection of semifans determined by the five 0-dimensional boundary components of the Baily-Borel compactification $\bbcpt{\fent}$.
Our goal is to prove the following:


:::{.theorem
    title="[@AEGS25, Thm. 1.1]"
    #thm:intro-main-theorem
}
Let $\fent$ be the moduli space of numerically polarized degree 2 Enriques surfaces, and let $\cpt{\fent}$ be its KSBA compactification.
There is a morphism

\begin{align*}
\semitorcpt{\fent} \iso \normksbacpt{\fent}
,\end{align*}

where $\normalize{(\wait)}$ denotes the normalization, the left-hand side is the semitoroidal compactification corresponding to an explicit collection $\semifans{F} = \ts{\semifan{F}_1, \torfan_2, \semifan{F}_3, \torfan_4, \semifan{F}_5}$ of semifans, one for each $0$-cusp of the Baily-Borel compactification $\bbcpt{\fent}$, and the right-hand side is the KSBA compactification. The semifans $\torfan_2, \torfan_4$ are fans, while $\semifan{F}_1, \semifan{F}_2, \semifan{F}_3$ are strict semifans.
:::

We note that the normalization is a technical condition that is often applied in the setting of KSBA compactifications, since the KSBA compactification is not guaranteed to be normal in general.
Roughly speaking, this is due to the fact that its construction involves taking a Zariski closure, which can introduce non-normal points where degenerations are identified, leading to a non-separated stack.
Since the normalization morphism is finite, birational, and relatively smooth in codimension one, this replacement restricts the worst singularities to lie in high codimension sub-loci and is thus a desirable tradeoff.

A standard construction in the study of del Pezzo and Enriques surfaces involves analyzing the invariant and coinvariant sublattices of a lattice $L$ acted on by an involution $L$.
In this situation, we take $L = \lkt$, consider three involutions $I_\star$, and study the invariant sublattices $T_\star = \lkt^{I_\star = 1}$ -- these are the lattices into which the transcendental lattices $T_Z$ of Enriques surfaces $Z$ primitively embed.
With a transcendental lattice identified, because these lattices have very particular signatures, we are placed in a setting where two combinatorial compactifications are accessible: the Baily Borel compactification of @BB66, and the semitoroidal compactifications of @Loo85, which simultaneously generalize both the Baily Borel and toroidal compactifications.
Their boundaries are stratified by *cusps*, and understanding how maps of moduli spaces induce maps on cusps is the first step toward classifying the boundary strata.
To finally attain a comparison with KSBA compactifiations, we then leverage the main result of @AE23, that the (normalization) of the KSBA compactification of stable K3 pairs $(X, \eps R)$ for a **recognizable** divisor $R$ (see @sec:chapter-4 and @sec:chapter-5) is isomorphic to a semitoroidal compactification.
Then @thm:intro-main-theorem follows from [@AEH24, Thm. 3.26], which shows that certain ramification divisors are recognizable.

The standard approach to understanding boundaries of semitoroidal compactifications (including Baily-Borel and toroidal compactifications as special cases) involves several difficult intermediate computational problems, among which is describing the faces of certain hyperbolic polytopes corresponding to fundamental domains of actions by reflection groups.
Typical methods include the use of Vinberg's algorithm [@Vin72], which although constructive, is computationally intensive for high rank lattices (and quickly becomes intractable) and is not generally known to be a halting procedure.
The approach we take in @AEGS25 largely bypasses many of these computational difficulties, in favor of more easily constructible divisorial log terminal (dlt) models which can be described in the finitary data of an integral affine 2-sphere, which we refer to as an $\IAS^2$ throughout this work.

These folding and involution-based methods recover the work of @Ste91, while the more general theory established in
[@AET23; @AEH24; @AE22; @AE23; @ABE22] has been shown to recover results from e.g. [@Sca87] and others.
The classification data is explicit and combinatorial, making it amenable to computation and reproducibility.
