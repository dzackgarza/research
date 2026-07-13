---
author:
- D. Zack Garza
bibliography: /home/dzack/gitclones/diss/200-dev/thesis/src/latex_core/Dissertation.bib
keywords:
- Enriques surfaces
- KSBA compactification
- Period domains
- Semitoroidal compactifications
- Integral affine geometry
title: Compact Moduli of Numerically Polarized Degree Two Enriques Surfaces
authors:
- Throughout This Text
- We Work Over $K={\Mathbf{C}}$.
tags:
- paper
- extraction
abstract: |
  
---

<!-- Source: 1-part-combinatorial/000-part-1.md -->

# Foundations and Geometric Setup {#part-1}

Throughout this text, we work over $k={\mathbf{C}}$.
A **K3 surface** is a smooth, projective, geometrically integral surface $X$ such that $\omega_X\cong {\mathcal{O}}_X$ is trivial, and $q(X) \mathrel{\mathop:}= h^{0, 1}(X) \mathrel{\mathop:}= H^0({\mathcal{O}}_X) = 0$.
An **Enriques surface** is a non-rational algebraic surface $Z$ of Kodaira dimension $\kappa(Z) = 0$ for which $h^1({\mathcal{O}}_Z) = h^2({\mathcal{O}}*Z) = 0$ and $K_Z$ is nontrivial $2$-torsion in $\operatorname{Pic}(Z)$.
Equivalently, they are quotients $Z = X/\iota$ of K3 surfaces $X$ by fixed-point-free involutions $\iota$, satisfying $2K_Z \sim 0$ and $q(Z) = 0$.
Enriques surfaces were among the first examples of non-rational surfaces with $p_g = 0$.
They have Kodaira dimension $\kappa(Z) = 0$ and are minimal.
We are interested in the study of moduli spaces of such surfaces, and in particular compactifications of $F*{{\mathrm{En}}, 2}$, the moduli space of degree 2 numerically polarized Enriques surfaces, which we will describe shortly.

For typical moduli spaces ${\mathcal{M}}$, one often has many choices for what a compactification $\overline{{\mathcal{M}}}$ should mean: GIT quotients $\overline{{\mathcal{M}}}^{ \operatorname{GIT} }$, Baily-Borel compactifications $\overline{{\mathcal{M}}}^{ \operatorname{BB} }$, toroidal compactifications $ \overline{{\mathcal{M}}}^{ \Sigma _{\bullet} } $, the semitoroidal compactifications $\overline{{\mathcal{M}}}^{ \mathcal{F} _{\bullet} }$ of (Looijenga 1985) which simultaneously generalize $\overline{{\mathcal{M}}}^{ \operatorname{BB} }$ and $ \overline{{\mathcal{M}}}^{ \Sigma \_{\bullet} } $, KSBA compactifications $ \overline{{\mathcal{M}}} $, quotient stack constructions, derived quotient stacks, and so on.
A disadvantage of many naively constructed compactifications $\overline{{\mathcal{M}}}$ is that they do not a priori have modular interpretations, i.e. $\partial\overline{{\mathcal{M}}}$ may not parameterize singular limits of smooth interior points in any canonically meaningful way.
However, the theory developed by KSBA (see (János Kollár 2023)) provides a functorial, geometrically meaningful compactification which can be defined in a canonical way, provided one can make a natural choice of divisor on the varieties in question (e.g. a polarization or a ramification divisor), and $\partial\overline{{\mathcal{M}}}$ can be understood as stable pairs $(X, R)$: of a variety $X$ with slc singularities and an ample divisor $R$.
Our goal for Part I is thus to establish the setting of the main theorem, along with the lattice-theoretic background and computational tools needed to contextualize and prove it.

<!-- Source: 1-part-combinatorial/1-chapter-intro/000-intro-main-thm.md -->

## Introduction {#chapter-1}

The central object needed to define such a compactification is a **KSBA stable pair**: a pair $(Z, \epsilon R_Z)$ where $Z$ is a connected projective variety and $R_Z$ is an effective ${\mathbf{Q}}$-divisor such that the pair $(Z, \epsilon R_Z)$ is semi-log canonical for some $0 < \epsilon \leq 1$, and $K_Z + \epsilon R_Z$ is ample.
We will then define KSBA compactifications as closures of spaces of particular types of surface pairs in the space of stable pairs.
When constructing such compactifications, we will often take the divisor $R_Z$ to be the ramification divisor corresponding to a $2$-divisible ample line bundle coming from a branched double-cover construction, i.e. an involution.
We note, however, that explicitly determining or classifying the boundary strata of a given KSBA compactification and the exact stable pairs that appear is nontrivial.
In (**AEGS23?**), we classify the strata of $\partial\overline{F_{{\mathrm{En}}, 2}}$, the KSBA compactification of $F_{{\mathrm{En}}, 2}$, and find that the irreducible components of stable limits of surface pairs are described by **$ADE+BC$ diagrams**, we which we mean the classical Dynkin diagrams corresponding to the semisimple complex Lie algebras of types $A_n, D_n, E_6, E_7, E_8$, which we refer to as simply-laced, and the diagrams of types $B_n$ and $C_n$.
The latter can be obtained from the former by a classically well-known operation called **folding**.

By the work of (**AET19?**), to each such diagram one can associated a pair $(Y, C)$ where $Y$ is a surface, which in many cases is toric, and $C$ is a reduced boundary divisor such that $(Y, C)$ is an lc pair and $-2(K_Y + C)$ is an ample Cartier divisor providing a natural polarization.
This provides a natural association of a classical $ADE+BC$ diagram (decorated with extra combinatorial parity data) to, in many cases, an explicit projective toric variety.
We refer to such surfaces as **$ADE+BC$ surfaces**. This thesis details the construction of an isomorphism between the normalization of the KSBA stable pair compactification $\overline{F_{{\mathrm{En}}, 2}}$ and a semitoroidal compactification $\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} *{\bullet} }$ for the moduli space of Enriques surfaces with *numerical polarization* of degree 2. The main theorem establishes an isomorphism $\overline{F*{{\mathrm{En}}, 2}}^{  \mathcal{F} *{\bullet} } \to  \overline{F*{{\mathrm{En}}, 2}} $ where $  \mathcal{F} *{\bullet}  = \left\{{  \mathcal{F} *k }\right\}*{k=1,1,2,3,45}$ is a collection of semifans determined by the five 0-dimensional boundary components of the Baily-Borel compactification $\overline{F*{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$.
Our goal is to prove the following:

:::{#thm:main-identification .theorem title="{[@AEGS23, Thm. 1.1]}
"}
Let $F_{{\mathrm{En}}, 2}$ be the moduli space of numerically polarized degree 2 Enriques surfaces, and let $\overline{F_{{\mathrm{En}}, 2}}$ be its KSBA compactification.
There is a morphism [ \overline{F_{{\mathrm{En}}, 2}}^{ \mathcal{F} _{\bullet} } { \, \xrightarrow{\sim}\, } \overline{F_{{\mathrm{En}}, 2}} ,] where $ {({-})}^{\nu} $ denotes the normalization, the left-hand side is the semitoroidal compactification corresponding to an explicit collection $ \mathcal{F} _{\bullet} = \left\{{ \mathcal{F} \_1, \Sigma \_2, \mathcal{F} \_3, \Sigma \_4, \mathcal{F} \_5}\right\}$ of semifans, one for each $0$-cusp of the Baily-Borel compactification $\overline{F_{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$, and the right-hand side is the KSBA compactification. The semifans $ \Sigma _2,  \Sigma _4$ are fans, while $ \mathcal{F} \_1, \mathcal{F} \_2, \mathcal{F} \_3$ are strict semifans.
:::

We note that the normalization is a technical condition that is often applied in the setting of KSBA compactifications, since the KSBA compactification is not guaranteed to be normal in general.
Roughly speaking, this is due to the fact that its construction involves taking a Zariski closure, which can introduce non-normal points where degenerations are identified, leading to a non-separated stack.
Since the normalization morphism is finite, birational, and relatively smooth in codimension one, this replacement restricts the worst singularities to lie in high codimension sub-loci and is thus a desirable tradeoff.

A standard construction in the study of del Pezzo and Enriques surfaces involves analyzing the invariant and coinvariant sublattices of a lattice $L$ acted on by an involution $L$.
In this situation, we take $L =  {L_{\mathrm{K3}}} $, consider three involutions $I_\star$, and study the invariant sublattices $T_\star =  {L_{\mathrm{K3}}} ^{I_\star = 1}$ -- these are the lattices into which the transcendental lattices $T_Z$ of Enriques surfaces $Z$ primitively embed.
With a transcendental lattice identified, because these lattices have very particular signatures, we are placed in a setting where two combinatorial compactifications are accessible: the Baily Borel compactification of (Baily and Borel 1966), and the semitoroidal compactifications of (Looijenga 1985), which simultaneously generalize both the Baily Borel and toroidal compactifications.
Their boundaries are stratified by *cusps*, and understanding how maps of moduli spaces induce maps on cusps is the first step toward classifying the boundary strata.
To finally attain a comparison with KSBA compactifiations, we then leverage the main result of (Alexeev and Engel 2023), that the (normalization) of the KSBA compactification of stable K3 pairs $(X, \varepsilon R)$ for a **recognizable** divisor $R$ (see \Cref{chapter-cpt} and \Cref{chapter-ias-dlt}) is isomorphic to a semitoroidal compactification.
Then \cref{thm:main-identification} then follows from (Alexeev, Engel, and Han 2022, Thm.
3.26), which shows that certain ramification divisors are recognizable.

The standard approach to understanding boundaries of semitoroidal compactifications (including Baily-Borel and toroidal compactifications as special cases) involves several difficult intermediate computational problems, among which is describing the faces of certain hyperbolic polytopes corresponding to fundamental domains of actions by reflection groups.
Typical methods include the use of Vinberg's algorithm (Vinberg 1972), which although constructive, is computationally intensive for high rank lattices (and quickly becomes intractable) and is not generally known to be a halting procedure.
The approach we take in (**AEGS23?**) largely bypasses many of these computational difficulties, in favor of more easily constructible divisorial log terminal (dlt) models which can be described in the finitary data of an integral affine 2-sphere, which we refer to as an $\mathrm{IAS}^2$ throughout this work.

These folding and involution-based methods recover the work of (Sterk 1991), while the more general theory established in (**AET23a?**; **AEH22?**; **AE23b?**; **AET23a?**; Alexeev and Engel 2023; Alexeev, Brunyate, and Engel 2022) has been shown to recover results from e.g. (Scattone 1987) and others.
The classification data is explicit and combinatorial, making it amenable to computation and reproducibility.

<!-- Source: 1-part-combinatorial/1-chapter-intro/100-historical-context.md -->

### Historical Context and Related Work {#section-1-1}

The systematic study of compactifications of moduli spaces began with the foundational work of Deligne and Mumford (P. Deligne and Mumford 1969), who compactified the moduli space of curves $ \mathcal{M}\_{g}$ by incorporating stable curves, i.e., one allows certain controlled degenerations with prescribed singularities.
For moduli of varieties described as arithmetic quotients of bounded symmetric domains, Baily and Borel (Baily and Borel 1966) developed a different approach, introducing a compactification by adjoining Hodge-theoretic boundary components to the period domain.

Subsequent developments included the work of Artin and Winters (Artin and Winters 1971) on stable reduction and semistable models for families of curves.
Although their results focused on curves, the methods -- particularly the use of semistable models and an emphasis on controlling degenerations -- provided the groundwork for extending these ideas to higher-dimensional varieties, including surfaces.
In particular, the techniques and perspectives developed for understanding degenerations of curves influenced later approaches to constructing and compactifying moduli spaces of surfaces, where the behavior of singular fibers and degenerations is even more complex.
In the 1980s, the development of higher-dimensional minimal model theory (see, for example, (Janos Kollár and Mori 1998)) built directly on these ideas, offering new tools for analyzing the compactification of moduli spaces for surfaces and varieties of general type, especially through the theory of log-canonical pairs.

Enriques surfaces were initially studied by Federigo Enriques at the beginning of the twentieth century as part of his broader classification of algebraic surfaces; see (Enriques 1906). The modern viewpoint that an Enriques surface arises as a quotient of a K3 surface by a fixed-point-free involution was developed much later in the work of Horikawa (**Hor78a?**) and Namikawa (Namikawa 1985). The study of the moduli of Enriques surfaces advanced through the work of Cossec and Dolgachev (**CD89?**), who developed a classification theory for linear systems on Enriques surfaces, laying the groundwork for the study of moduli of polarized Enriques surfaces.
(Sterk 1991) constructed the first complete (Baily--Borel) compactification of the moduli space $F_{{\mathrm{En}}, 2}$ by exploiting the lattice-theoretic structure inherited from the universal K3 cover.

The modern approach to compactifying moduli spaces of surfaces has been dominated by the theory of stable pairs established by Kollár, Shepherd-Barron, and Alexeev (J. Kollár and Shepherd-Barron 1988; Alexeev 1996). This machinery produces projective compactifications by allowing degenerations to semi-log-canonical pairs, and we refer to Kollár's recent book (János Kollár 2023) for details.
KSBA theory has been especially effective for surfaces of general type and for Calabi--Yau surfaces.

For Enriques surfaces, whose canonical class is numerically trivial, there is not always a canonical choice of polarization or divisor.
Recent advances include the classification of ADE surfaces (surfaces with at worst rational double points of type A, D, or E) by Alexeev and Thompson (**AT19?**), which establishes a foundation for describing boundary points corresponding to simply-laced singularities.
More recently, this framework has been extended (**AEGS23?**) to cover the case of non-simply-laced singularities (types B and C), which naturally appear in the boundary of degenerating families of Enriques surfaces.

<!-- Source: 1-part-combinatorial/1-chapter-intro/200-k3-enr-lattices.md -->

### The K3 and Enriques Lattices $ {L*{\mathrm{K3}}} $ and $ {L*{\mathrm{En}}} $ {#section-1-2}

The **K3 lattice** is given by $$ {L_{\mathrm{K3}}}  = U^3 \oplus E_8^2  { \, \xrightarrow{\sim}\, }   {\textrm{II}}*{3, 19} ,$$ where $U$ is the hyperbolic plane (\cref{def:hyperbolic-plane}) and $E_8$ is the negative-definite $E_8$ root lattice (\cref{ex:classical-root-lattices}). It is the unique even unimodular latice of signature $(3, 19)$ up to isometry, which we write as ${\textrm{II}}*{3, 19}$.
For any K3 surface $X$, there exists a **marking** $H^2(X,{\mathbf{Z}})  { \, \xrightarrow{\sim}\, }    {L_{\mathrm{K3}}} $ that identifies the cohomology lattice with this fixed reference lattice.
We refere to a K3 surface with a marking as a **marked** K3 surface.
Moduli spaces of polarized and marked K3 surfaces are typically governed by the following two lattices: $$ S*X \mathrel{\mathop:}= \operatorname{NS}(X) \cong \operatorname{Pic}(X) \hookrightarrow H^2(X; {\mathbf{Z}}), \qquad T_X \mathrel{\mathop:}= S_X^{\perp*{H^2(X; {\mathbf{Z}})}}
,$$ where $\operatorname{NS}(X) \mathrel{\mathop:}= \operatorname{Pic}(X)/\operatorname{Pic}^0(X)$ is the Neron-Severi lattice, and we take the orthogonal complement with respect to the bilinear form induced by the intersection pairing in cohomology.
If the signature of $H^2(X; {\mathbf{Z}})$ is $(p, q)$, then we must have $\operatorname{sig}(S_X) + \operatorname{sig}(T_X) = (p, q)$ since $T_X \oplus S_X \hookrightarrow H^2(X;{\mathbf{Z}})$ embeds as a finite-index submodule.
In particular, if one chooses $S$ such that $\operatorname{sig}(S_X) = (1, \rho(X) - 1)$, this forces $\operatorname{sig}(T_X) = (p-1, q-r-1)$.
When $p=3$ on obtains a lattice $T_X$ of signature $(2, n)$.
For such lattices, there is a well-defined Type ${\textrm{IV}}$ Hermitian symmetric domain $D_{T_X}$, and for any choice of neat arithmetic subgroup $\Gamma \leq \operatorname{O}^*(T_X)$ of the *stable orthogonal group* of $T_X$, there is a well-defined arithmetic quotient $$ F_{\Gamma} \mathrel{\mathop:}=  { D_{T_X} }/{\Gamma} , \qquad \Gamma \leq \operatorname{O}^*(T_X) .$$ The $S$ and $T$ lattices are dual in many senses -- for projective surfaces, $S_X$ contains ample line bundles, and hence the algebraic/projective structure of $X$ (as determined by its polarizations) are governed by $S_X$, while its complemenet $T_X$ governs transcendental data such as periods and variations of Hodge structure, which are typically orthogonal to the polarization.
For K3 surfaces, by the global Torelli theorem, its isomorphism is determined by its polarized weight 2 Hodge structure on $H^2(X;{\mathbf{C}})$, and since period domains of the form $D_{T_X}$ classify such Hodge structures, they can be used to construct coarse moduli spaces of $S_X$-polarized marked K3 surfaces.

#### Unpolarized Enriques Surfaces and $F_{{\mathrm{En}}}$

As quotients of K3 surfaces, Enriques surfaces $Z$ admit similar Hodge-theoretic moduli spaces, and we are thus naturally lead to study the lattice-theoretic techniques used to construct $D_{T_X}$ and the involutions involved in double cover constructions $X\to Z$.
By the classification theory for Enriques surfaces (see (**CD89?**, Cor.
1.2.3)), $\omega_Z$ is a generator of the 2-torsion in $\operatorname{Pic}(Z)$.
The Néron--Severi group satisfies $$ \operatorname{NS}(Z) \cong H^2(Z; {\mathbf{Z}}) \cong {\mathbf{Z}}^{10} \oplus {\mathbf{Z}}_2 .$$ Let $H^2(Z; {\mathbf{Z}})_f$ denote the free part.
The intersection pairing endows $H^2(Z; {\mathbf{Z}})*f$ with the structure of a lattice, i.e. a free ${\mathbf{Z}}$-module with a integral symmetric bilinear form, and there are isometries $$ {L*{\mathrm{En}}}  \mathrel{\mathop:}= H^2(Z; {\mathbf{Z}})*f  { \, \xrightarrow{\sim}\, }   U \oplus E_8  { \, \xrightarrow{\sim}\, }   {\textrm{II}}*{1, 9} ,$$ the unique even unimodular lattice up to isometry(see \cref{def:canonical-lattice-table}), where $U$ and $E_8$ are as above.
We similarly define a **marking** for an Enriques surface $Y$ as an isometry $H^2(Y,{\mathbf{Z}})*f \cong  {L*{\mathrm{En}}} $, and refer to an Enriques surface with a marking as a **marked** Enriques surface.
For any Enriques surface $Z$, since $\omega_Z$ is 2-torsion, there exists an étale double cover $\pi: X \to Z$ such that $X$ is a K3 surface.
This is the universal cover, and the fundamental group $\pi_1(Z) \cong {\mathbf{Z}}_2$ is generated by the covering involution, which acts freely and properly discontinuously on $X$.
The Hodge diamonds of K3 and Enriques surface are well known, and visibly reflect the structure of the double cover:

\begin{tikzcd}
[
row sep=small, column sep=small,
every matrix/.append style={name=m},
execute at end picture={
\scoped[on background layer]{
\draw[gray!20, thick] (m-1-3) -- (m-3-1) -- (m-5-3) -- (m-3-5) -- (m-1-3);
\draw[gray!20, thick] (m-1-9) -- (m-3-7) -- (m-5-9) -- (m-3-11) -- (m-1-9);
}}
]
& & 1 & & & & & & 1 & & \\
& 0 & & 0 \ar[rrrr, bend left, "\iota_{{\mathrm{En}}}\colon X \to Z"]& & & & 0 & & 0 & \\
1 & & 20 & & 1& & 0 & & 10 & & 0 \\
& 0 & & 0 & & & & 0 & & 0 & \\
& & 1 & & & & & & 1 & &
\end{tikzcd}

In particular, $h^{1,1}(Z) = 10$, $h^{2,0}(Z) = h^{0,2}(Z) = 0$, confirming $p_g = 0$, and all other Hodge numbers vanish except $h^{0,0} = h^{2,2} = 1$.
Conversely, any K3 surface $X$ with a fixed-point-free involution $\iota_{{\mathrm{En}}}$ is said to have an *Enriques involution*, gives rise to an Enriques surface $Y \mathrel{\mathop:}= X/\iota_{{\mathrm{En}}}$ as its quotient.
The pullback $\pi^* H^2(Z; {\mathbf{Z}})$ under the covering map can be identified with the lattice $ {L*{\mathrm{En}}} (2)$, i.e., $ {L*{\mathrm{En}}} $ with the intersection form multiplied by 2. There is a unique primitive embedding $ {L*{\mathrm{En}}} (2) \hookrightarrow {L*{\mathrm{K3}}} $ up to isometry, and so we regard it as a primitive sublattice and set $$ S_{{\mathrm{En}}} \mathrel{\mathop:}=  {L_{\mathrm{En}}} (2) = U(2)\oplus E_8(2), \quad T_{{\mathrm{En}}} \cong S_{{\mathrm{En}}}^{\perp  {L_{\mathrm{K3}}} } = U \oplus U(2) \oplus E_8(2) \cong U \oplus S_{{\mathrm{En}}}
,$$ which have satisfy $\operatorname{sig} S_{{\mathrm{En}}} = (1,9)$ and $\operatorname{sig} T_{{\mathrm{En}}} = (2, 10)$ respectively.
The computation of $T_{{\mathrm{En}}}$ can be found, for example, in (Sterk 1991), although it was known earlier.
We note that when $X$ is a K3 surface that admits an Enriques involution $\iota_{{\mathrm{En}}}$, letting $I_{{\mathrm{En}}}$ denote the induced isometry on $H^2(X; {\mathbf{Z}})$, we obtain $$ S_{{\mathrm{En}}} \oplus T_{{\mathrm{En}}}  { \, \xrightarrow{\sim}\, }    {L_{\mathrm{K3}}} ^{I_{{\mathrm{En}}} = 1} \oplus  {L_{\mathrm{K3}}} ^{I_{{\mathrm{En}}}=-1} \hookrightarrow  {L_{\mathrm{K3}}}
,$$ realizing these as the invariant and coinvariant lattices respectively.\footnote{We note that there are mixed conventions in the literature regarding whether $S$ or $T$ should be the invariant sublattice -- we choose here the convention used in [@AEGS23].} This similarly determines a Type ${\textrm{IV}}$ period domain $D_{T_{{\mathrm{En}}}}$, and the quotient $$ F*{{\mathrm{En}}} \mathrel{\mathop:}= { D*{T*{{\mathrm{En}}}}}/{\Gamma*{{\mathrm{En}}} } , \qquad \Gamma*{{\mathrm{En}}} \mathrel{\mathop:}= \operatorname{O}(T*{{\mathrm{En}}})

$$
is a 10-dimensional rational quasi-projective variety.
The global Torelli theorem for Enriques surfaces (**Hor78b?**; Namikawa 1985) states that two Enriques surfaces $Z_1, Z_2$ are isomorphic if and only if there exists an isometry $\phi: H^2(Z_1;{\mathbf{Z}}) \to H^2(Z_2;{\mathbf{Z}})$ preserving the intersection pairing and Hodge structure.
This implies that the natural map from the set ${\mathcal{M}}_{{\mathrm{En}}}$ of isomorphism classes of Enriques surfaces to $F_{{\mathrm{En}}}$ is injective on the open subset parameterizing smooth surfaces.
Thus, $F_{{\mathrm{En}}}$ serves as the coarse moduli space of (unpolarized) Enriques surfaces.

#### Numerically Polarized Enriques Surfaces and $F_{{\mathrm{En}}, 2}$

Let $Z$ be an Enriques surface.
The first Chern class induces an isomorphism
$$

c*1\colon\operatorname{Pic}(Z) { \, \xrightarrow{\sim}\, } H^2(Z; {\mathbf{Z}}) $$ so that the free part $H^2(Z; {\mathbf{Z}})_f$ is identified with the group of numerical divisor classes, $\operatorname{Num}(Z)$.
A **numerical polarization** $[h]$ on $Z$ is the numerical class of $h \mathrel{\mathop:}= c_1({\mathcal{L}})$ for an ample line bundle ${\mathcal{L}} \in \operatorname{Pic}(Z)$, which we often write $[{\mathcal{L}}]$.
For a fixed degree $2d$, one considers the moduli space $F*{{\mathrm{En}},h}$ of numerically polarized Enriques surfaces of degree $2d$.
The set of primitive classes $h$ with $h^2 = 2d$, up to the action of $\operatorname{O}( {L_{\mathrm{En}}} )$, may consist of more than one orbit, except in the case $d = 1$, where the orbit is unique.
Therefore, the moduli space $F_{{\mathrm{En}}, 2}$ of numerically polarized Enriques surfaces of degree 2 is distinguished by this uniqueness property.
The moduli space $F_{{\mathrm{En}}, 2}$ parameterizes pairs $(Z, [{\mathcal{L}}_Z])$, where $Z$ is an Enriques surface, possibly with ADE singularities, and $[{\mathcal{L}}*Z] \in \operatorname{Pic}(Z)/{\mathbf{Z}}*2 \cong \operatorname{Num}(Z)$ is the numerical class of an ample polarization of degree 2. Equivalently, $F*{{\mathrm{En}}, 2}$ may be described as the moduli space of pairs $(Z, {\mathcal{M}})$, where ${\mathcal{M}} = {\mathcal{L}}*Z^{\otimes 2} \in \operatorname{Pic}(Z)$ is a 2-divisible polarization of degree 8. Given an ample line bundle ${\mathcal{L}}$ on $Z$, set ${\mathcal{M}} = {\mathcal{L}}^{\otimes 2}$, which has degree 8. By the classification of big and nef linear systems on Enriques surfaces (see (F. R. Cossec 1983)), the linear system $|{\mathcal{M}}|$ is basepoint-free and defines a morphism $\rho\colon Z \to W$ where $W$ is a quartic del Pezzo surface with singularities of type $4A_1$ or $A_3 + 2A_1$.
The morphism $\rho$ is a double cover of $W$ which is branched along a divisor $B \subset W$ where the corresponding ramification divisor $R_Z = \rho^{-1}(B)$ is ample, ${\mathbf{Q}}$-Cartier, and in the linear system $|{\mathcal{M}}|$.
The pair $(Z, \varepsilon R_Z)$ is log-canonical for sufficiently small $\varepsilon > 0$, and thus $F*{{\mathrm{En}}, 2}$ admits a KSBA compactification by stable pairs, which we will simply denote $\overline{F*{{\mathrm{En}}, 2}}$ throughout this work.

To put us in the setting of the main theorem, fix a basis of $ {L*{\mathrm{K3}}} $ in the decomposition above, so in coordinates we have $(u_1, u_2, u_3, \alpha_1, \alpha_2) \in U^3 \oplus E_8^2$, where each $u_i$ is in a copy of $U$ and each $\alpha_i$ is in a copy of $E_8$.
Consider three morphisms on $ {L*{\mathrm{K3}}} $, acting on vectors $(u_1, u_2, u_3, \alpha_1, \alpha_2) \in U^3 \oplus E_8^2$ in this basis in the following way:

`\begin{align*}\label{three-lattice-involutions} I_{\operatorname{dP}}(u_1, u_2, u_3, \alpha_1, \alpha_2)        &= (-u_1, u_3, u_2, -\alpha_1, -\alpha_2) \\ I_{{\mathrm{En}}}(u_1, u_2, u_3, \alpha_1, \alpha_2)  &= (-u_1, u_3, u_2, \alpha_2, \alpha_1) \\ I_{ {\mathrm{Nik}} }(u_1, u_2, u_3, \alpha_1, \alpha_2) &= (u_1, u_2, u_3, -\alpha_2, -\alpha_1) \end{align*}`{=tex}

These arise as the lattice involutions on $ {L*{\mathrm{K3}}} $ induced by three types of geometric involutions, $\iota*{\operatorname{dP}}, \iota*{{\mathrm{En}}}$, and $\iota*{ {\mathrm{Nik}} }$ respectively, on a K3 surface $X$.
A direct computation shows that the group $\left\langle I_{\operatorname{dP}}, I_{{\mathrm{En}}}, I_{ {\mathrm{Nik}} } \right\rangle$ is isomorphic to ${\mathbf{Z}}*2^2$, and thus these involutions mutually commute.
For each such involution $I*\star$, we write $S_\star \mathrel{\mathop:}=  {L_{\mathrm{K3}}} ^{I_\star = 1}$ and $T_\star =  {L_{\mathrm{K3}}} ^{I_\star = -1}$ for the invariant and co-invariant sublattices under the group actions $\left\langle  I_\star  \right\rangle \curvearrowright  {L_{\mathrm{K3}}} $.
Similarly direct computations yield the invariant and coinvariant sublattices shown in the table below, where the triples $(r, a, \delta)*{n*+}$ are the invariants shown by (Nikulin 1980) to classify 2-elementary lattices $T$ which admit a primitive embedding $T\hookrightarrow  {L_{\mathrm{K3}}} $.
Concretely, $r \mathrel{\mathop:}= \operatorname{rank}*{\mathbf{Z}}(T)$ is the rank, $a$ is the *length* of $L$, which can be expressed as $\dim*{{ \mathbf{F} }*2}(A_T)$ where $A_T\mathrel{\mathop:}= T {}^{ \vee }/T$ is the *discriminant group* of $T$, the integer $\delta\in \left\{{0, 1}\right\}$ is the *coparity*, and the subscript $n$ is used to track the rank of a maximal positive-definite sublattice, which can be used to recover the signature as $(n*+, r-n_+)$.

\begin{table}[htbp] \centering \caption{(Co)Invariant Lattices for the Three Involutions} \begin{tabular}{|c|l|c|c|l|c|} \hline $L$ & Isometry Class & $\operatorname{rank}_{\mathbf{Z}}(L)$ & $\operatorname{sig}(L)$ & $(r,a,\delta)*n$ & $A_L$ \\
\hline $S*{\operatorname{dP}}$ & $U(2)$ & $2$ & $(1,1)$ & $(2,2,0)_1$ & ${\mathbf{Z}}*2^2$ \\
$T*{\operatorname{dP}}$ & $U \oplus U(2) \oplus E_8^2$ & $20$ & $(2,18)$ & $(20,2,0)_2$ & ${\mathbf{Z}}*2^2$ \\
$S*{{\mathrm{En}}}$ & $U(2) \oplus E_8(2)$ & $10$ & $(1,9)$ & $(10,10,0)_1$ & ${\mathbf{Z}}*2^{10}$ \\
$T*{{\mathrm{En}}}$ & $U \oplus U(2) \oplus E_8(2)$ & $12$ & $(2,10)$ & $(12,10,0)_2$ & ${\mathbf{Z}}*2^{10}$ \\
$L*{{\mathrm{Nik}}}^{+}$ & $U^3 \oplus E_8(2)$ & $14$ & $(3,11)$ & $(14,8,0)_3$ & ${\mathbf{Z}}*2^8$ \\
$L*{{\mathrm{Nik}}}^{-}$ & $E_8(2)$ & $8$ & $(0,8)$ & $(8,8,0)_0$ & ${\mathbf{Z}}_2^8$ \\
\hline \end{tabular} \end{table}

<!-- \label{canonical-lattice-table} -->
<!-- Source: 1-part-combinatorial/1-chapter-intro/300-overview.md -->

### Structure and Overview {#section-1-3}

The thesis is organized into three parts, establishing the foundations and proving the main isomorphism theorem:

- \Cref{part-1} develops the combinatorial and lattice-theoretic foundations:

  - \Cref{chapter-1} introduces the main theorem, historical context, and key concepts including KSBA stable pairs and $\mathrm{ADE}+\mathrm{BC}$ surfaces.

  - \Cref{chapter-2} establishes lattice-theoretic foundations, particularly Nikulin's theory of 2-elementary lattices, with applications to the invariant lattices $ {L*{\mathrm{K3}}} $, $\operatorname{len}$, $T*{{\mathrm{En}}}$, and $T_{\operatorname{dP}}$.
    This includes the classification of primitive embeddings and the structure of discriminant groups.

  - \Cref{chapter-3} develops the theory of Enriques surfaces and their K3 covers, analyzing the period domains $F_{{\mathrm{En}}, 2}$ and $F_{(2,2,0)}$, and classifying the five 0-cusps of $\partial\overline{F_{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$ through explicit lattice-theoretic computations.

- \Cref{part-2} constructs the compactifications:

  - \Cref{chapter-4} presents the theory of KSBA, Baily-Borel, toroidal, and semitoroidal compactifications.
    It establishes the framework for stable pairs and recognizable divisors that enables the comparison between algebraic and analytic compactifications.

  - \Cref{chapter-5} develops integral affine geometry and the theory of Kulikov models.
    It describes how Type III degenerations correspond to integral affine spheres with singularities ($\mathrm{IAS}^2$), and how these yield divisorial log terminal (dlt) models through explicit algorithms involving Coxeter polytopes and monodromy invariants.

- \Cref{part-3} proves the main theorem and provides explicit computations:
  - \Cref{chapter-6} establishes the isomorphism $ \overline{F*{{\mathrm{En}}, 2}} \cong \overline{F*{{\mathrm{En}}, 2}}^{ \mathcal{F} \_{\bullet} }$ through:
    1. Embedding $F_{{\mathrm{En}}, 2}$ into the moduli space $F_{(2,2,0)}$ of $(2,2,0)$-polarized K3 surfaces as a Noether-Lefschetz locus
    2. Showing the normalized closure $ {B}^{\nu} $ inherits a semitoroidal structure from $ \overline{F\_{(2,2,0)}} $
    3. Constructing the universal family of Enriques pairs via quotient by the Enriques involution
    4. Proving the classifying map $ {B}^{\nu} \to \overline{F\_{{\mathrm{En}}, 2}} $ is finite using geometric constraints on double curves
    5. Applying Zariski's Main Theorem to conclude the isomorphism
  - \Cref{chapter-7} provides computational examples, constructing explicit dlt models for degenerations at each of the five 0-cusps of $\partial\overline{F_{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$.
    It demonstrates the folding procedure that relates K3 degenerations to Enriques degenerations through the action of commuting involutions on $\mathrm{IAS}^2$ structures.

<!-- Source: 1-part-combinatorial/2-chapter-lattice-theory/000-lattice-theory.md -->

## Lattice Theory {#chapter-2}

Compactifications of $F_{{\mathrm{En}}, 2}$, and more generally moduli spaces of K3 surfaces, rely on the arithmetic and combinatorial structure of even indefinite (and often hyperbolic) lattices.
This chapter discusses the lattice-theoretic techniques used in such problems, emphasizing both theoretical results and explicit computational techniques.

Of particular importance is the structure theory of *2-elementary* lattices: even integral lattices whose discriminant group is an ${ \mathbf{F} }*2$-module.
In the context of $F*{{\mathrm{En}}, 2}$, the sublattice $T_{{\mathrm{En}}}$ associated to the Enriques involution $\iota_{{\mathrm{En}}}$ on a K3 cover $X$ is 2-elementary of signature $(2,10)$.
The invariants $(r, a, \delta)$, recording the rank, length of the discriminant group, and *coparity*, completely determine the isometry classes of such lattices, as well as their embedding properties.
Nikulin's fundamental work in (Nikulin 1979a) yields existence and uniqueness of the relevant period domains $D_{T_{{\mathrm{En}}}}$, their arithmetic quotients $F_{{\mathrm{En}}, 2}$, and the structure of boundary strata in various compactifications.

A major theme is the connection between the geometry of the period domain and the arithmetic of $T_{{\mathrm{En}}}$: the construction of $F_{{\mathrm{En}}, 2}$ relies on an arithmetic subgroup ${\Gamma_{{\mathrm{En}}, 2}} $, and the ${\Gamma_{{\mathrm{En}}, 2}} $-orbits of primitive isotropic vectors $\eta$ and primitive isotropic planes $I$ in $T_{{\mathrm{En}}}$ index the rational boundary components of the Baily-Borel compactification $\overline{F_{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$, called *cusps*. It has has $0$-cusps and $1$-cusps indexed by such $\eta$ and $I$ respectively.
This chapter details the lattice-theoretic methods classically used to find the five $0$-cusps of $F_{{\mathrm{En}}, 2}$.
We begin with definitions and standard constructions:

- Properties of even lattices, dual lattices, discriminant groups, and genus;

- The hyperbolic plane $U$, indefinite root lattices $A_n, D_n, E_8$ and their twists, and particularly their duals and discriminant groups;

- Criteria for primitively embedding one lattice into another, including Nikulin's theorems on extensions, embeddings, and overlattices, as well as his classification of 2-elementary lattices.

Special focus is given Nikulin's work: explicit determination of invariants, criteria for primitive embeddings into even unimodular lattices such as $ {L*{\mathrm{K3}}} $ and $\operatorname{len}$, and explicit discriminant group techniques that can be used to reduce the aforementioned orbit problems to the study of finitary, computable objects.
All lattice-theoretic results in this chapter serve a concrete purpose in the overall study of $F*{{\mathrm{En}}, 2}$ and similar lattice-theoretic moduli spaces.
In later chapters, we will see how the the explicit classification of isotropic sublattices of $T_{{\mathrm{En}}}$ determines the structure of $\partial\overline{F_{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$ and consequently that of semitoroidal compactifications $\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} *{\bullet} }$, and by the main theorem, provide an inroad into studying the boundary $\partial\overline{F*{{\mathrm{En}}, 2}}$ of the KSBA compactification.

<!-- Source: 1-part-combinatorial/2-chapter-lattice-theory/100-foundations.md -->

### Foundations {#section-2-1}

#### Bilinear and Quadratic Forms

##### Pairings

:::{#def:symmetric-bilinear-form .definition title="{Symmetric Bilinear Form}
"}
Let $L$ be a ${\mathbf{Z}}$-module.
A **bilinear form** $\beta$ on $L$ is a morphism $\beta: L \otimes_{{\mathbf{Z}}} L \to {\mathbf{Q}}$.
We often write $v \cdot w$ or $vw$ for $\beta(v,w)$.
A bilinear form $\beta$ is:

- **$\varepsilon$-symmetric** for $\varepsilon \in {\mathbf{Q}}$ if $\beta(a,b) = \varepsilon \cdot \beta(b,a)$.
- **Symmetric** if $\varepsilon = 1$.
- **Skew-symmetric** if $\varepsilon = -1$.
- **Alternating** if $\beta(a,a) = 0$ for all $a \in L$.
- **Integral** if its image $\beta(L,L)$ is contained in ${\mathbf{Z}}$.
- **Nondegenerate** if the map $L\to \operatorname{Hom}_{\mathbf{Z}}(L, {\mathbf{Z}})$ given by $v\mapsto \beta(v, \cdot)$ is injective.
:::

:::{#def:quadratic-form .definition title="{Quadratic Form and Associated Bilinear Form}
"}
A **quadratic form** on a ${\mathbf{Z}}$-module $L$ is a map of sets $q: L \to {\mathbf{Q}}$ such that $q(\lambda v) = \lambda^2 q(v)$ for all $v \in L, \lambda \in {\mathbf{Q}}$, and such that its **polar form** $\beta_q$ is a symmetric bilinear form on $L$: `\begin{align*}
\beta_q: L \otimes_{{\mathbf{Z}}} L &\to {\mathbf{Q}} \\
(v,w) &\mapsto \beta_q(v,w) \mathrel{\mathop:}= q(v+w) - q(v) - q(w)
\end{align*}`{=tex} We say $q$ is **integral** if $q(L) \subseteq {\mathbf{Z}}$.
The pair $(L,q)$ is called a **quadratic ${\mathbf{Z}}$-module**.
:::

:::{#lem:bilinear-quadratic-correspondence .lemma title="{Correspondence between Bilinear and Quadratic Forms}
"}
Every ${\mathbf{Q}}$-valued bilinear module $(L,\beta)$ determines a ${\mathbf{Q}}$-valued quadratic module $(L,q_\beta)$ by $q_\beta(v) \mathrel{\mathop:}= \beta(v,v)$, which depends only on the symmetric part of $\beta$.
Conversely, every ${\mathbf{Q}}$-valued quadratic module $(L,q)$ determines a symmetric bilinear module $(L,\beta_q)$ via the polar form.
:::

:::{#lem:even-lattice-bijection .lemma title="{Bijection for Even Lattices}
"}
There is a bijection between even symmetric integral forms and integral quadratic forms: $$\begin{aligned}
\{\beta \in \operatorname{Sym}_{{\mathbf{Z}}}^2(L {}^{ \vee }) {~\mathrel{\Big\vert}~} \beta \text{ is even}\} &\rightleftharpoons \mathrm{Quad}_{{\mathbf{Z}}}(L) \\
\beta &\mapsto q(v) \mathrel{\mathop:}= {1\over 2}\beta(v,v) \\
\beta_q &\mathrel{\reflectbox{\ensuremath{\mapsto}}} q
\end{aligned}$$ In other words, the polar form of any integral quadratic form is an even symmetric integral form.
Conversely, every even symmetric integral form $\beta$ is the polar form of the integral quadratic form $q(v) \mathrel{\mathop:}= {1\over 2}\beta(v,v)$.
:::

##### Lattices

:::{#def:lattice .definition title="{Lattice}
"}
A **lattice** is a pair $(L,\beta)$ where $L$ is a free ${\mathbf{Z}}$-module of finite rank and $\beta$ is a nondegenerate symmetric bilinear form, which is typically integral but may be ${\mathbf{Q}}$-valued.
A **quadratic lattice** is a pair $(L,q)$ where $q$ is a nondegenerate quadratic form.
A lattice $(L,\beta)$ is **even** if $\beta(v,v) \in 2{\mathbf{Z}}$ for all $v \in L$, and **odd** otherwise.
:::

##### Gram Matrices

:::{#def:gram-matrices .definition title="{Gram Matrix}
"}
Given a basis $B_L = (e_i)_{1 \leq i \leq n}$ for a bilinear module $(L,\beta)$, the **Gram matrix** of $\beta$ is $G_\beta \mathrel{\mathop:}= (\beta(e_i, e_j))_{i,j} \in \operatorname{Mat}_{n \times n}({\mathbf{Q}})$.
For vectors $v = \sum a_j e_j$ and $w = \sum b_j e_j$, we have $\beta(v,w) = v^t G_\beta w$.
Similarly, for a quadratic module $(L,q)$, a **Gram matrix** $G_q$ is any matrix such that $q(v) = v^t G_q v$.
We define the **discriminant** $\operatorname{disc}(L)$ of $L$ as $\operatorname{det}(G_\beta)$ in any choice of basis.
We note that for any sublattice $S \leq L$, we have the formula $$
\operatorname{disc}(S) = [L:S]^2 \operatorname{disc}(L)
,$$ so the discriminant typically _increases_ when passing to a sublattice.
We say $L$ is **unimodular** of $\operatorname{disc}(L) = \pm 1$.
The Gram matrix reflects properties of the form: $\beta$ is symmetric iff $G_\beta^t = G_\beta$, skew-symmetric iff $G_\beta^t = -G_\beta$, and an integral lattice is even iff $G_\beta$ is an integer matrix with diagonal entries in $2{\mathbf{Z}}$.
:::

:::{#prop:divisibility-properties-revised .proposition title="{Primitive Isotropic Vectors, Divisibility, and Hyperbolic Splittings}
"}
Let $S$ be any unimodular lattice admitting a primitive embedding into a nondegenerate lattice $L$.
Then $L \cong S \oplus T$ where $$
T\mathrel{\mathop:}= S^{\perp} = \left\{{v\in L {~\mathrel{\Big\vert}~} \beta(v, S) = 0}\right\}
$$ is the **orthogonal complement** of $S$ in $L$.
Moreover, if $S$ is unimodular, then so is $T$.
:::

:::
proof
This follows from (Peters and Sterk 2024, Lem.
1.3.1): we can write $\operatorname{disc}(S) = [S\oplus T: L]\cdot c_S$ for some $c_S\in {\mathbf{Z}}$.
By unimodularity, $\operatorname{disc}(S) = \pm 1$ forces $c_S = \pm 1$ and $[S\oplus T: L] = 1$, yielding the first claim.
For the second, we note that $\operatorname{disc}(S\oplus T) = \operatorname{disc}(S) \cdot \operatorname{disc}(T)$ by standard properties of determinants, forcing $\operatorname{disc}(T) = \pm 1$.
:::

:::{#def:rank-signature .definition title="{Rank and Signature}
"}
Let $(L, \beta)$ be a nondegenerate lattice.
We say it is:

- **positive definite** if $\beta(v,v) > 0$ for all nonzero $v \in L$.
- **positive semidefinite** if $\beta(v,v) \geq 0$ for all $v \in L$.
- **negative definite** if $\beta(v,v) < 0$ for all nonzero $v \in L$.
- **negative semidefinite** if $\beta(v,v) \leq 0$ for all $v \in L$.
- **indefinite** if it is neither positive nor negative semidefinite.

Letting $(L_{{\mathbf{R}}}, \beta_{{\mathbf{R}}})$ be the extension of $L$ to ${\mathbf{R}}$, the diagonalization of the Gram matrix $p$ positive terms and $q$ negative terms.
We define the following:

- The **rank** of $L$ is $\operatorname{rank}(L) = p + q$.
- The **signature** of $L$ is $\operatorname{sig}(L) = (p,q)$.
- The **index** of $L$ is $\tau(L) = p - q$.

We note that $L$ is positive-definite if $q=0$, negative-definite if $p=0$, and indefinite if both $p,q > 0$.
We say $L$ is **hyperbolic** if its signature is $(1, n-1)$ or $(n-1, 1)$.
:::

:::{#def:scaled-lattices .definition title="{Scaled Lattices}
"}

```meta
corpus-references: ""
depends-on: "#def:lattice"
audited: false
```

For any lattice $(L,\beta)$ and positive integer $m$, the **scaled lattice** $L(m)$ is the same ${\mathbf{Z}}$-module $L$ equipped with the bilinear form $\beta_m(v,w) = m \cdot \beta(v,w)$.
The signature of $L(m)$ is the same as $L$, but the discriminant scales as $\operatorname{disc}(L(m)) = m^{\operatorname{rank}(L)} \cdot \operatorname{disc}(L)$.
If $L$ is unimodular and $m>1$, $L(m)$ is not unimodular.
:::

:::{.example title="{Diagonal and Hyperbolic Lattices}
"}
The **diagonal lattice** $\left\langle a_1, \ldots, a_n \right\rangle$ is ${\mathbf{Z}}^n$ with the bilinear form $\beta(x,y) = \sum a_i x_i y_i$ and diagonal Gram matrix $\operatorname{diag}(a_1, \ldots, a_n)$.
In the special case $a_1,\cdots, a_{p} = 1$ and $a_{m+1}, \cdots, a_n = -1$, we write this lattice as ${\textrm{I}}_{p, q}$, due to its distinguished nature as the unique nondegenerate odd unimodular lattice of signature $p, q$.
The **hyperbolic lattice** $U$ is the free ${\mathbf{Z}}$-module ${\mathbf{Z}}^2$ with basis $e,f$ such that $\beta(e,e) = \beta(f,f) = 0$ and $\beta(e,f) = 1$.
It is an even, integral, rank 2 lattice with Gram matrix $$
G_U = \matt 0110
.$$
:::

#### Sublattices, Embeddings, and Isometries

:::{#def:lattice-morphisms .definition title="{Lattice Morphisms and Embeddings}
"}
A **morphism** between lattices $(L_1, \beta_1)$ and $(L_2, \beta_2)$ is a morphism of ${\mathbf{Z}}$-modules $f: L_1 \to L_2$ that preserves the bilinear form: $\beta_1(v,w) = \beta_2(f(v), f(w))$ for all $v,w \in L_1$.
We write $\operatorname{Lat}$ for the category of integral lattices, and $\operatorname{Hom}_{\operatorname{Lat}}(L_1, L_2)$ for their spaces of morphisms.
An **embedding** is an injective morphism.
An embedding is **primitive** if its cokernel, $\operatorname{coker}(f)$, is a torsion-free ${\mathbf{Z}}$-module.
An **isometry** is a morphism of lattices that is also an isomorphism of ${\mathbf{Z}}$-modules.
Two lattices $L_1, L_2$ are **isometric**, written $L_1  { \, \xrightarrow{\sim}\, }   L_2$, if an isometry exists between them.
The **orthogonal group** of a lattice $L$ is its group of self-isometries $\operatorname{O}(L) \mathrel{\mathop:}= \operatorname{Aut}_{\operatorname{Lat}}(L)$.
In terms of a Gram matrix $G_\beta$, the orthogonal group has the characterization: $$
\operatorname{O}(L) = \{M \in \operatorname{GL}_n({\mathbf{Z}}) {~\mathrel{\Big\vert}~} M G_\beta M^t = G\_\beta\}

$$
:::

:::{#def:primitive-sublattice .definition title="{Primitive and Saturated Sublattices}
"}
A sublattice $S \leq L$ is **primitive** (or **saturated**) if the quotient module $L/S$ is torsion-free. An element $v \in L$ is **primitive** if the sublattice $\left\langle v \right\rangle_{{\mathbf{Z}}}$ is primitive.
:::

:::{#prop:saturation-characterization .proposition title="{Characterization of Primitive Sublattices}
"}
For a sublattice $S \subseteq L$, the following are equivalent:

-   $S$ is a primitive sublattice of $L$.
-   The inclusion $S \hookrightarrow L$ is a primitive embedding.
-   $S$ is saturated in $L$, meaning $S = \operatorname{Sat}_L(S) \mathrel{\mathop:}= \{v \in L {~\mathrel{\Big\vert}~} nv \in S \text{ for some } n \in {\mathbf{Z}} \setminus \{0\}\}$.
-   $S$ is a direct summand of $L$ as a ${\mathbf{Z}}$-module (i.e., $L \cong S \oplus T$ for some submodule $T$).
-   Any ${\mathbf{Z}}$-basis of $S$ can be extended to a ${\mathbf{Z}}$-basis of $L$.
-   $S_{\mathbf{Q}} \cap L = S$.
-   $S = (S^{\perp L})^{\perp L}$.
-   Every integral linear functional on $S$ can be lifted to an integral linear functional on $L$.
:::

:::{#def:embedding-equivalence .definition title="{Equivalence of Embeddings}
"}
Two primitive embeddings $\iota_1{~\mathrel{\Big\vert}~} S \hookrightarrow L_1$ and $\iota_2{~\mathrel{\Big\vert}~} S \hookrightarrow L_2$ are **equivalent** if there exists an isometry $f \in \operatorname{Isom}(L_1, L_2)$ such that $f \circ \iota_1 = \iota_2$, so the following diagram commutes

\begin{tikzcd}
S \arrow[r, "\iota_1"] \arrow[rd, "\iota_2"'] & L_1 \arrow[d, "f", dashed] \\
& L_2
\end{tikzcd}

If $L_1 = L_2 = L$ is a single lattice, two primitive embeddings $\iota_1, \iota_2: S \hookrightarrow L$ are **equivalent** if they are equivalent by an element of $\operatorname{O}(L)$ as above. The set of equivalence classes of primitive embeddings of $S$ into $L$ is denoted $\operatorname{Emb}(S, L)$.
:::

:::{#def:isotropic-submodules .definition title="{Isotropic Submodules and Vectors}
"}
``` meta
corpus-references: ""
depends-on: "#def:lattice"
audited: false
```

For a lattice $(L,\beta)$, a submodule $W \subseteq L$ is **isotropic** if $\beta|_W = 0$ (equivalently, $W \subseteq W^{\perp L}$). An **isotropic vector** is an element $v \in L$ with $\beta(v,v) = 0$. The **Witt index** $\operatorname{WI}(L)$ is the maximal rank of an isotropic sublattice.
:::

:::{#def:divisibility-primitive-elements .definition title="{Divisibility}
"}
Let $L$ be a lattice with form $\beta$, and let $v \in L$. The **divisibility** of $v$ in $L$, denoted $\operatorname{div}_L(v)$, is the positive generator of the ideal $\{\beta(v, w){~\mathrel{\Big\vert}~} w \in L\} \subseteq {\mathbf{Z}}$.
:::

:::{#prop:divisibility-discriminant .proposition title="{Divisibility and Discriminant for Primitive Vectors}
"}
Let $L$ be a nondegenerate lattice, and $v \in L$ an arbitrary (not necessarily isotropic) vector. The element $v^* \mathrel{\mathop:}= v/\operatorname{div}_L(v) \in L {}^{ \vee }$ is primitive in the dual lattice, and its image in the discriminant group $A_L \mathrel{\mathop:}= L {}^{ \vee }/L$ has order $\operatorname{div}_L(v)$. In particular, $\operatorname{div}_L(v)$ divides the order of $A_L$, and hence $|\operatorname{disc}(L)|$.
:::

:::
proof
Since the divisibility $\operatorname{div}_L(v) = d$ is by definition the positive generator of the ideal $\{(v, w){~\mathrel{\Big\vert}~} w \in L\}$, one has $v/d \in L {}^{ \vee }$ and this vector is primitive in $L {}^{ \vee }$. Indeed, if $v/d = m y$ for some $m \in {\mathbf{Z}}$, $y \in L {}^{ \vee }$, then $v = d m y \in L$, and primitivity of $v$ in $L$ implies $m = \pm 1$. The order of $v^*$ in $A_L$ is the minimal positive $n$ such that $n v^* \in L$. This occurs precisely when $n$ is divisible by $d$, so the order is $d = \operatorname{div}_L(v)$. Since $A_L$ is finite of order $|\operatorname{disc}(L)|$, it follows in particular that $\operatorname{div}_L(v)$ divides $|\operatorname{disc}(L)|$.
:::

:::{#lem:isotropic-pairing-unimodular .lemma title="Divisibility of Isotropic Vectors in Unimodular Lattices"}
Let $L$ be a nondegenerate unimodular lattice, and let $v \in L$ be a primitive isotropic vector. Then there exists $w \in L$ such that $(v, w) = 1$. In particular, $\operatorname{div}_L(v) = 1$ for all $v\in L$.
:::

:::
proof
Since $L$ is unimodular, $L  { \, \xrightarrow{\sim}\, }   L {}^{ \vee }$. The linear form $x \mapsto (v, x)$ is a nonzero element of $\operatorname{Hom}(L, {\mathbf{Z}} )$, and is surjective because $v$ is primitive and $L$ is unimodular. Hence there exists $w \in L$ with $(v, w) = 1$.
:::

#### Dual Lattices and Discriminant Forms

:::{#def:dual-lattice-construction .definition title="{Dual Lattice}
"}
For an integral lattice $(L,\beta)$, the **dual lattice** is the ${\mathbf{Z}}$-module of linear functionals $L {}^{ \vee } \mathrel{\mathop:}= \operatorname{Hom}_{{\mathbf{Z}}}(L, {\mathbf{Z}})$.
:::

:::{#thm:geometric-identification-dual .theorem title="{Geometric Identification of the Dual Lattice}
"}
For a nondegenerate integral lattice $(L,\beta)$, the dual lattice can be identified with a sublattice of $L_{{\mathbf{Q}}} \mathrel{\mathop:}= L \otimes_{{\mathbf{Z}}} {\mathbf{Q}}$ via the bijection: `\begin{align*}
L {}^{ \vee } \cong \{ v \in L_{{\mathbf{Q}}} {~\mathrel{\Big\vert}~} \beta_{{\mathbf{Q}}}(v,L) \subseteq {\mathbf{Z}}\}
\end{align*}`{=tex} where a functional $\phi \in L {}^{ \vee }$ corresponds to the unique vector $v_\phi \in L_{\mathbf{Q}}$ such that $\phi(w) = \beta(v_\phi, w)$ for all $w \in L$. Under this identification, we have the inclusions $L \subseteq L {}^{ \vee } \subseteq L_{{\mathbf{Q}}}$.
:::

:::{#rem:dual-lattice-properties .remark title="{Properties of Dual Lattices}
"}
We summarize some standard properties of dual lattices

-   Duality commutes with direct sums, $(L \oplus M)^\vee = L {}^{ \vee } \oplus M^\vee$.
-   If $L$ has Gram matrix $G_\beta$ in a basis $B_L$, then the dual basis satisfies $B_{L {}^{ \vee }} = (B_L^t)^{-1}$, and the Gram matrix of the dual form is $G_{\beta^\vee} = G_\beta^{-1}$.
-   The discriminant of the dual satifies $\operatorname{disc}(L {}^{ \vee }) = 1/\operatorname{disc}(L)$, and the dual of a scaled lattice is $(L(m))^\vee = L {}^{ \vee }(1/m)$.
:::

:::{#def:discriminant-group .definition title="{Discriminant Group and Discriminant}
"}
For a nondegenerate lattice $(L,\beta)$, the **discriminant group** is the finite abelian group $A_L \mathrel{\mathop:}= L {}^{ \vee } / L$. The order of the discriminant group equals the absolute value of the discriminant, i.e. $|A_L| = |\operatorname{disc}(L)| = [L {}^{ \vee }{~\mathrel{\Big\vert}~} L]$, so $L$ is unimodular if and only if $A_L$ is trivial.
:::

:::{#def:discriminant-forms .definition title="{Discriminant Forms [@PS24, Def. 1.6.5] }
"}
For a nondegenerate *even* lattice $(L,\beta)$, the **discriminant bilinear form** is $\beta_{A_L}: A_L \times A_L \to {\mathbf{Q}}/{\mathbf{Z}}$, given by $\beta_{A_L}(\overline{x}, \overline{y}) = \beta(x,y) \bmod {\mathbf{Z}}$ for any lifts $x,y \in L {}^{ \vee }$ and $\beta$ the induced form on $L {}^{ \vee }$. It admits an associated quadratic form $q_{A_L}(\overline{x}) = \beta(x,x)\pmod{{\mathbf{Z}}} \in {\mathbf{Q}}/{\mathbf{Z}}$ for any lift $x$. We note that there are two conventions in the literature, where one sometimes defines $q_{A_L}(\overline{x}) \mathrel{\mathop:}= \beta(x,x)\pmod{2{\mathbf{Z}}}\in {\mathbf{Q}}/2{\mathbf{Z}}$; these agree by the isomorphism ${\mathbf{Q}}/{\mathbf{Z}}  { \, \xrightarrow{\sim}\, }   {\mathbf{Q}}/2{\mathbf{Z}}$ induced by multiplication by $2$. We define its **orthogonal group** $\operatorname{O}(A_L)$ as the automorphisms that preserve $q_{A_L}$. The **length** $\ell(L)$ of $L$ is the minimal number of generators for the abelian group $A_L$.
:::

:::{#prop:discriminant-form-properties .proposition title="{Properties of Discriminant Forms}
"}
The discriminant forms $b_L$ and $q_L$ of a nondegenerate lattice $L$ are themselves nondegenerate. For any $[v], [w] \in A_L$, the bilinear and quadratic forms are related by $\beta_{A_L}([v],[w]) = {1\over 2}(q_{A_L} ([v]+[w]) - q_{A_L} ([v]) - q_{A_L} ([w]))$, where multiplication by ${1\over 2}$ is interpreted as an isomorphism ${\mathbf{Q}}/2{\mathbf{Z}} \to {\mathbf{Q}}/{\mathbf{Z}}$.
:::

:::{#prop:scaled-lattice-sequence .proposition title="{Exact Sequence for Scaled Lattices}
"}
For any lattice $L$ and positive integer $m$, there is a short exact sequence: $$
0 \to L/mL \hookrightarrow A_{L(m)} \to A_L \to 0
$$ If $L$ is unimodular, this implies $A_{L(m)} \cong L/mL$. Similarly, by functoriality, any isometry $f \in \operatorname{O}(L)$ lifts to an isometry of $L {}^{ \vee }$ and thus induces an isometry on the discriminant group $A_L$. This defines a group homomorphism $\psi: \operatorname{O}(L) \to \operatorname{O}(A_L)$, which fits into an exact sequence: $$
0 \to \operatorname{O}^*(L) \to \operatorname{O}(L) \xrightarrow{\psi} \operatorname{O}(A_L) \to \operatorname{O}^*(A_L) \to 0
$$ where $\operatorname{O}^*(L) \mathrel{\mathop:}= \ker(\psi)$ and $\operatorname{O}^*(A_L) \mathrel{\mathop:}= \operatorname{coker}(\psi)$ are the **stable orthogonal groups** of $L$ and $A_L$. The cokernel, $\operatorname{O}^*(A_L) \mathrel{\mathop:}= \operatorname{coker}(\psi)$, measures the obstruction to lifting isometries from the discriminant form $A_L$ to the lattice $L$. We note that $\psi$ is surjective (i.e., $\operatorname{O}^*(A_L) = 0$) when $L$ is indefinite and satisfies $\ell(A_L) + 2 \leq \operatorname{rank}(L)$, where $\ell(A_L)$ is the minimal number of generators of $A_L$. For unimodular lattices like $U$ and $E_8$, the discriminant group is trivial, so $\operatorname{O}^*(L) = \operatorname{O}(L)$.
:::

:::{#ex:hyperbolic-duals .example title="$U$ and $U(2)$"}
The hyperbolic lattice $U$ is unimodular, so $U^\vee = U$ and its discriminant group $A_U$ is trivial. For the scaled lattice $U(2)$, with Gram matrix $\matt 0220$, the dual is $U(2)^\vee = {1\over 2}U = U$ and we have $A_{U(2)} = U/U(2) \cong ({\mathbf{Z}}/2{\mathbf{Z}})^2 \cong U/2U$.
:::

#### Torsion Forms over ${\mathbf{Q}}/{\mathbf{Z}}$

:::{#def:torsion-forms .definition title="{Torsion Bilinear and Quadratic Forms}
"}
A **torsion bilinear form** is a pair $(G,\beta)$ where $G$ is a finitely generated torsion ${\mathbf{Z}}$-module and $\beta: G \otimes_{{\mathbf{Z}}} G \to {\mathbf{Q}}/{\mathbf{Z}}$ is a bilinear form. A **torsion quadratic form** is a pair $(G,q)$ where $G$ is a torsion module and $q: G \to {\mathbf{Q}}/{\mathbf{Z}}$ is a quadratic form.
:::

<!-- Source: 1-part-combinatorial/2-chapter-lattice-theory/200-examples.md -->

### Fundamental Examples

#### The Hyperbolic Plane \$ U \$

The **hyperbolic plane** \$ U \$ is the unique even, unimodular lattice of signature \$ (1,1) \$, with a standard basis given by vectors \$ {e, f} \$ satisfying [ e\^2 = f\^2 = 0, \quad e \cdot f = 1, \qquad G_U = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}

. ] A vector \$ v \in U \$ is called **isotropic** if \$ v\^2 = 0 \$.
We have $\operatorname{disc}(U) = -1$, and thus \$ U \cong U {}^{ \vee } \$, hence \$ U \$ is unimodular and $A_U = 0$.
This can also be computed directly: if $v\in U {}^{ \vee }$, then $v = ae + bf$ where $a,b\in {\mathbf{Q}}$.
We then must have $vw\in {\mathbf{Z}}$ for all $w\in U$, and in particular this must hold for $w=e$ and $w=f$.
We compute $ev = b$ and $fv = a$, so $a,b\in {\mathbf{Z}}$.
Both $e$ and $f$ are primitive -- for examples, the embedding $\operatorname{gen}{e}\hookrightarrow U$ is primitive, since $U/\left\langle e \right\rangle  { \, \xrightarrow{\sim}\, }   \left\langle f \right\rangle$ is free.
The full set of primitive isotropic vectors is $\left\{{\pm e, \pm f}\right\}$.
To see this, let $v=ae + bf$ and compute $v^2 = (a e + b f)^2 = 2ab$.
Thus, \$ v \$ is isotropic if and only if \$ ab = 0 \$, implying \$ v = a e \$ or \$ v = b f \$ for some \$ a,b \in {\mathbf{Z}} \$.
For $v$ to additionally be primitive, we must have \$ a = \pm 1 \$ or \$ b = \pm 1 \$.

The scaled hyperbolic plane \$ U(2) \$ has basis \$ {e' , f'} \$ such that [ (e')\^2 = (f')\^2 = 0, e'\cdot f' = 2, \qquad G\_{U(2)} = \begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix}

. ] We can similarly compute $U(2) {}^{ \vee }$ by writing $v\in ae' + bf'$, then $e'v = 2b$ and $f'v = 2a$ are integral if and only if $a,b\in {1\over 2}{\mathbf{Z}}$ -- thus $U(2) {}^{ \vee } = {1\over 2}U$, and $A_{U(2)} = {1\over 2} U/ U \cong U/2U \cong C_2^2$, as expected from the exact sequence in the previous section.

The orthogonal group of $U$ is $\operatorname{O}(U) = \left\{\pm\mathrm{id}, \pm\begin{bsmallmatrix} 0 & 1 \\ 1 & 0 \end{bsmallmatrix}\right\} \cong C_2^2$, generated by the involutions $(e,f) \mapsto (-e, -f)$ and $(e,f)\mapsto (f, e)$.
Explicitly, we have the following elements, closed under composition, each of order 2, generating a Klein four group:

`\begin{align*} & \sigma_0 = \mathrm{id}: \quad e \mapsto e,\ f \mapsto f; \quad A_0 &= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \\ & \sigma_1: \quad e \mapsto -e,\ f \mapsto -f; \quad A_1 &= \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}, \\ & \sigma_2: \quad e \mapsto f,\ f \mapsto e; \quad A_2 &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \\ & \sigma_3: \quad e \mapsto -f,\ f \mapsto -e; \quad A_3 &= \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}. \end{align*}`{=tex}

To see why this is true, since \$ g \$ must preserve primitive isotropic vectors and \$ ef = 1 \$, the images \$ g(e), g(f) \$ must lie in \$ {\pm e, \pm f} \$ and have the same pairing.
Only four such transformations preserve \$ ef = 1 \$, as listed above.
Direct computation verifies the relation \$ A_i\^T G_U A_i = G_U \$ for each $i$.
Note however that the *rational* orthogonal group \$ \operatorname{O}(U\_{\mathbf{Q}}) \$ is much larger: it contains the one-parameter subgroups: [ i_a = \begin{pmatrix} a & 0 \\ 0 & a^{-1} \end{pmatrix} , \quad j_b = \begin{pmatrix} 0 & b \\ b^{-1} & 0 \end{pmatrix}

\quad  \text{ for }  a,b \in {\mathbf{Q}}\^\times, .] Finally, we note that the lattices $U$ and ${\textrm{I}}*{1,1} \mathrel{\mathop:}= \left\langle 1, -1 \right\rangle$ are not isometric over ${\mathbf{Z}}$, since $U$ is even and ${\textrm{I}}*{1,1}$ is odd.
However, both have signature $(1,1)$ and discriminant $-1$, so they become isometric over ${\mathbf{Q}}$ and ${\mathbf{R}}$.
It is true, however, that $U$ and ${\textrm{II}}_{1, 1}$ are isometric, where the latter is the unique *even* unimodular lattice discussed later in this section.

#### Root Lattices

We present here the classical definitions of the *positive-definite* root lattices of $A,D,E$ types, noting that in applications in later chapters, we will typically choose the negative-definite variations of these lattices, as is the typical convention in algebraic geometry.
We maintain the positive-definite convention until \Cref{sec-folding}, where we give more precise constructions and critically used the positive-definite constructions to carry out folding calculations in Euclidean spaces.
After which we switch to the more negative-definite convention that is typically more convenient for geometry.
We refer to \Cref{section-root-lattice-conventions} for explicit computations, diagram, and labelings.

We summarize below all of the relevant information for the simply-laced $\mathrm{ADE}$ types, as well as the exceptional types $E_6, E_7, E_8, F_4$, and $G_2$.
In all cases, the lattices $L$ can be realized by a primitive embedding $L\hookrightarrow {\mathbf{Q}}^n$ for some $n$, where we identify ${\mathbf{Z}}^n \subseteq {\mathbf{Q}}^n$ with the abstract diagonal lattice $\left\langle 1,1,\cdots, 1 \right\rangle$.
In these Euclidean embeddings, one can explicitly compute the Gram matrices $G_L$, the duals $L {}^{ \vee }$ and discriminant groups $A_L$, and invariants such as $\operatorname{disc}(L)$ using standard linear algebra.
We let $R(L) \subseteq L$ denote the set of *roots* in each lattice (vectors $v\in L$ with $v^2=2$), $\Phi(L)\subseteq R(L)$ its corresponding *simple root system* -- a subset of roots $\alpha_i$ such that, without loss of generality, ${\mathbf{Z}}*{\geq 0} \Phi(L) = R(L)$, i.e. every $v\in R(L)$ can be written as $v=\sum*{\alpha_i \in \Phi(L)} c_i \alpha_i$ with all $c_i \geq 0$ integral.
This defines a sublattice ${\mathbf{Z}}\Phi(L) \hookrightarrow L$, and we say $L$ is a **root lattice** if this is index 1. In any case, one can define a *Weyl group* $W(L) \leq \operatorname{O}(L)$ of reflections generated in by hyperplanes $H_{\alpha_i} \mathrel{\mathop:}= \alpha_i^{\perp L}$ for $\alpha_i\in \Phi(L)$.
For root lattices, we can identify $G_L$ with $G_{{\mathbf{Z}} \Phi(L)}$, the Gram matrix of intersections between the simple roots; these agree up to similarity since $\Phi(L)$ generates $L$.

##### Type $A$

Let ${\mathbf{Z}}^{n}$ denote the standard diagonal lattice $\left\langle 1,1,\cdot, 1 \right\rangle$ with generators $\left\{{e_1,\cdots, e_n}\right\}$.
The root lattice $A_n$ is isometric to a root lattice in $v_{n+1}^{\perp {\mathbf{Z}}^{n+1}}$ where $v_{n+1} \mathrel{\mathop:}= \sum_{i=1}^{n+1} e_i$, and thus concretely identified as a primitively embedded sublattice [ A_n \hookrightarrow \left\{{x\in {\mathbf{Z}}^{n+1} {~~\mathrel{\Big\vert}~~} \sum_{i=1}^{n+1} x_i = 0 }\right\} .] One defines $R(A_n)$ to consist of the roots $r_{i,j} \mathrel{\mathop:}= e_i - e_j$ in $v_{n+1}^\perp$ for $1\leq i \neq j \leq n+1$, and so $|R(A_n)| = n\cdot(n+1)$.
There are $n$ simple roots forming $\Phi(A_n)$, which can be chosen as $\alpha_i \mathrel{\mathop:}= e_i - e_{i+1}$ for $1\leq i \leq n$.

##### Type $D$

For any lattice $L$, one can consider the lattice $dL\mathrel{\mathop:}= \left\{{d\cdot v{~~\mathrel{\Big\vert}~~} v\in L}\right\}$, noting that this differs from the twist $L(d)$.
In particular, $d{\mathbf{Z}}^n$ forms a lattice for any $n$, and one can produce interesting lattices by taking the kernels of *augmentation* morphisms $\varepsilon_d: L\to d{\mathbf{Z}}$ given by $v\mapsto \sum v_i$.
In particular, for $L = {\mathbf{Z}}^n$, we define ${\mathbf{Z}}^n_{\mathrm{ev}} = \ker({\mathbf{Z}}^n\xrightarrow{\varepsilon_2} 2{\mathbf{Z}})$, which can be realized as $$ {\mathbf{Z}}^n_{\mathrm{ev}} \mathrel{\mathop:}= \left\{{ x = (x_1, \ldots, x_n) \in {\mathbf{Z}}^n {~~\mathrel{\Big\vert}~~} \sum_{i=1}^n x_i \equiv 0 \pmod{2{\mathbf{Z}}} }\right\} \hookrightarrow {\mathbf{Z}}^n $$ The $D_n$ root lattice is the root sublattice ${\mathbf{Z}}^n_{\mathrm{ev}}$ whose roots $R(D_n)$ consist of all vectors $r_{i,j} \mathrel{\mathop:}= \pm e_i \pm e_j$ in ${\mathbf{Z}}^n_{\mathrm{ev}}$ for all $1 \leq i < j \leq n$.
There are $n(n-1)/2$ unordered pairs of distinct indices, and for each such pair, four roots corresponding to all sign choices, and thus $$
|R(D_n)| = 4 \cdot \binom{n}{2} = 4 \cdot \frac{n(n-1)}{2} = 2n(n-1)
.$$ A set of simple roots for $\Phi(D_n)$ can be chosen as $\alpha_i \mathrel{\mathop:}= e_i - e_{i+1}$ for $1 \leq i \leq n-1$ and $\alpha_n \mathrel{\mathop:}= e_{n-1} + e_n$.

####### Type $E$

The root lattice $E_8$ is the unique, even, unimodular, positive-definite lattice of rank 8, and admits an isometry $$ E_8  { \, \xrightarrow{\sim}\, }   \left\{{ x \in {\mathbf{Z}}^8 \cup \left( {{\mathbf{Z}}^8 + {1\over 2}v_8} \right) {~~\mathrel{\Big\vert}~~} \sum_{i=1}^8 x_i \equiv 0\pmod{2{\mathbf{Z}}}}\right\} \hookrightarrow {\mathbf{Q}}^8 $$ where $v_8 = (1,\cdots, 1)$.
It contains exactly $2^4\cdot 3\cdot 5 = 240$ roots:

- The difference vectors $r_{i, j}^{\pm, \pm} \mathrel{\mathop:}= \pm e_i \pm e_j$ for $1\leq i\neq j\leq 8$, of which there are $\binom{8}{2}\cdot 4 = 112$, and

- The half-sum vectors $r_{\pm^8} \mathrel{\mathop:}= {1\over 2} \sum_{i=1}^8 \varepsilon_i e_i$ with $\varepsilon_i = \pm 1$ and $\prod \varepsilon_i = 1$, i.e. vectors of the form ${1\over 2}(\pm e_1 \pm e_2 \cdots \pm e_8)$ where the number of minus signs is even, of which there are $2^8/2 = 128$.

Of these, there are 8 simple roots comprising $\Phi(E_8)$, and there is a transitive action $W(E_8)\curvearrowright \Phi(E_8)$.
The root lattice $E_{7}$ can be constructed as $\operatorname{Ann}*{E*{8}}\left(L_{1}\right)$ for any sublattice $L_{1} \leq E_{8}$ isometric to $A_{1}$, usually taken to be generated by a specific vector denoted $v_8$.
Similarly, $E_{6}=\operatorname{Ann}*{E*{8}}\left(L_{2}\right)$ for any sublattice $L_{2}$ isometric to $A_{2}$, usually chosen to be generated by a specific vector $v_7$.

##### Types $B, C, F_4, G_2$.

The root system $R(B_n) \subset \mathbb{Z}^n$ consists of all vectors of the form $r_i \mathrel{\mathop:}= \pm e_i$ for $q\leq i \leq n$ and $r_{ij}\mathrel{\mathop:}= \pm e_i \pm e_j$ for $1\leq i < j \leq n$, of which there are $2n + 2n\cdot(n-1) = 2n^2$; of these, one can choose $\Phi(B_n)$ to consist of roots $\alpha_i \mathrel{\mathop:}= e_i - e_{i+1}$ for $1\leq i \leq n-1$ and $\alpha_n = e_n$.
For type $C$, the root system $R(C_n)$ consists of the roots $2r_i$ and $r_{ij}$ as in type $B$, again yielding $2n^2$, and one can choose all $\alpha_i$ in the same way, only replacing $\alpha_n$ with $2e_n$.
It is worth pointing out the duality here: for $B_n$, there are $2n$ short roots $r_i$ and $2n\cdot(n-1)$ long roots $r_{ij}$; in $C_n$, these switch roles, and there are $2n$ long roots $2r_i$ and $2n\cdot(n-1)$ short roots $r_{ij}$.

The root lattice $F_4$ is realized as a root system in ${\mathbf{Z}}^4$ with $R(F_4)$ consisting of vectors $\pm e_i$ for $1\leq i \leq 4$, $\pm e_i \pm e_j$ for $1\leq i < j \leq 4$, and those of the form ${1\over 2}(\sum \pm e_i)$ where the number of minus signs is even.
A system of simple roots can be taken to be $$
\begin{aligned}
\alpha_1 &= e_2 - e_3, \\
\alpha_2 &= e_3 - e_4, \\
\alpha_3 &= e_4, \\
\alpha_4 &= \tfrac{1}{2} ( e_1 - e_2 - e_3 - e_4 ).
\end{aligned}
$$ Finally, the root lattice $G_2$ embeds into ${\mathbf{Z}}^3_{\Delta}\subseteq {\mathbf{Z}}^3$, i.e. those $x\in {\mathbf{Z}}^3$ with $\sum x_i = 0$.
The root system $R(G_2)$ is generated by roots of the form $\pm(e_i - e_j)$ for $1\leq i < j \leq 3$ and $\pm(2e_i -e_j-e_k)$ for $i,j,k$ a permutation of $\left\{{1,2,3}\right\}$, yielding 12 total roots.
A simple system can be taken to be $$
\begin{aligned}
\alpha_1 &= e_1 - e_2, \\
\alpha_2 &= - e_1 + 2 e_2 - e_3.
\end{aligned}
.
$$

##### The Plus Construction and Remarks

We also briefly note the classical "plus" construction: define two vectors in $\mathbb{Q}^n$ by [ v\_{+} = \frac{1}{2}(1,1,1,\ldots,1), \quad v\_{-} = \frac{1}{2}(-1,1,1,\ldots,1). ] We then define the overlattices [ D_n\^{+} := D_n \cup (v\_+ + D_n), \quad D_n\^{-} := D_n \cup (v\_- + D_n). ] If $n$ is odd, then there are isometries [ D_n\^{+} { \, \xrightarrow{\sim}\, } D_n\^{-} { \, \xrightarrow{\sim}\, } D_n\^\vee, ] the dual lattice of $D_n$.
If $n$ is even, then $D_n^{+} \not { \, \xrightarrow{\sim}\, }   D_n^{-}$, and both contain $D_n$ as an index 2 sublattice.
Both $D_n^{+}$ and $D_n^{-}$ are unimodular lattices, and are even integral lattices if and only if $n \equiv 0 \pmod{8}$.
For $n=8$, we have $D_8^+  { \, \xrightarrow{\sim}\, }   E_8$.

We also recall that if $R \mathrel{\mathop:}= \left\langle  \Phi  \right\rangle_{\mathbf{Z}}$ is a root lattice generate by a root system $\Phi$, the dual lattice $R {}^{ \vee }$ is referred to as the **weight space** of $R$, and the dual basis elements $w_i$ defined by $w_i(\alpha_j) = \delta_{ij}$ are referred to as **coroots**.
For unimodular lattices such as $E_8$, it is often useful to identify $E_8 {}^{ \vee } \cong E_8$ and work in a basis of coroots $w_{1}, \cdots, w_{8}\mathrel{\mathop:}=\alpha_{1}{ }^{\vee}, \cdots, \alpha_{8}{ }^{\vee}$.The coordinates of each $w_i$ in terms of the original roots $\alpha_i$ can be found explicitly; for example, note that
$$
G_{E_{8}}^{-1}=\left[\begin{array}{rrrrrrrr} -4 & -5 & -7 & -10 & -8 & -6 & -4 & -2 \\
-5 & -8 & -10 & -15 & -12 & -9 & -6 & -3 \\
-7 & -10 & -14 & -20 & -16 & -12 & -8 & -4 \\
-10 & -15 & -20 & -30 & -24 & -18 & -12 & -6 \\
-8 & -12 & -16 & -24 & -20 & -15 & -10 & -5 \\
-6 & -9 & -12 & -18 & -15 & -12 & -8 & -4 \\
-4 & -6 & -8 & -12 & -10 & -8 & -6 & -3 \\
-2 & -3 & -4 & -6 & -5 & -4 & -3 & -2 \end{array}\right], $$ and thus one can write each $w_{i}$ in terms of $\alpha_{i}$ basis using its columns: $$
\begin{aligned}
& w_{1}=-4 \alpha_{1}-5 \alpha_{2}-7 \alpha_{3}-10 \alpha_{4}-8 \alpha_{5}-6 \alpha_{6}-4 \alpha_{7}-2 \alpha_{8} \\
& w_{2}=-5 \alpha_{1}-8 \alpha_{2}-10 \alpha_{3}-15 \alpha_{4}-12 \alpha_{5}-9 \alpha_{6}-6 \alpha_{7}-3 \alpha_{8}
\end{aligned}
,$$ and so on.
Finally, the lattice $E_8(2)$ frequently appears in moduli-theoretic applications.A direct determinant computation shows that $\operatorname{disc}(E_8(2)) = 2^8$, and using the exact sequences of the previous chapter, we can write $$ E_8(2) {}^{ \vee }  { \, \xrightarrow{\sim}\, }   {1\over 2}E_8 \implies A_{E_8(2)} \cong E_8/2E_8 \cong {1\over 2}E_8/E_8 \cong {\mathbf{Z}}*2^8 ,$$ and similarly $U(2) {}^{ \vee }  { \, \xrightarrow{\sim}\, }   {1\over 2}U$, facts which were critically employed in (Sterk 1991) to compute $\partial \overline{F*{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$.

#### Unimodular lattices

##### Type ${\textrm{I}}$

For any positive integer $n$ and non-negative integers $0 \leq p, q \leq n$ with $p+q=n$, let $L=\left\langle v_{1}, \cdots, v_{p}, w_{1}, \cdots, w_{p}\right\rangle \cong {\mathbf{Z}}^{n}$ be generated by $p+q$ elements where $$ \beta\left(v_{i}, v_{j}\right)=\delta_{i j}, \quad \beta\left(w_{i}, w_{j}\right)=-\delta_{i j}, \quad \beta\left(v_{i}, w_{j}\right)=0 \,\,\forall i, j .$$ The Gram matrix is diagonal with $p$ copies of +1 and $q$ copies of $-1$: $$ G_{\beta}=\left(\begin{array}{ccccc} 1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & \ddots & 0 & 0 \\
0 & 0 & 0 & -1 & 0 \\
0 & 0 & 0 & 0 & -1 \end{array}\right)=\left[\begin{array}{c|c} \mathrm{id}*{p \times p} & 0 \\
\hline 0 & -\mathrm{id}*{q \times q} \end{array}\right] \in \operatorname{Mat}*{p \times p}({\mathbf{Z}}) \times \operatorname{Mat}*{q \times q}({\mathbf{Z}}) . $$ We write this lattice as $$ {\textrm{I}}*{p, q}\mathrel{\mathop:}=\langle 1,1, \cdots,-1,-1\rangle\mathrel{\mathop:}=\langle 1\rangle^{ p} \oplus\langle-1\rangle^{ q} .$$ This is an integral, odd, unimodular lattice of rank $p+q$ and signature $(p, q)$ with discriminant $(-1)^q$.
By the classification theorem of such lattices, if $L$ is any odd indefinite unimodular lattice with $\operatorname{sig}(L)=$ $(p, q)$, then $L  { \, \xrightarrow{\sim}\, }   I*{p, q}$.

##### Type ${\textrm{II}}$

For $p, q \in {\mathbf{Z}}*{\geq 0}$, define $$ {\textrm{II}}*{p, q} = {\textrm{II}}_{p, q} =
\begin{cases}
  E_{8}^{\frac{p-q}{8}} \oplus U^{q}, & p-q \geq 0  \text{ and }  8|(p-q) \\
  E_{8}^{\frac{q-p}{8}} \oplus U^{p}, & p-q < 0  \text{ and }  8|(q-p)
\end{cases}
$$ where $E_{8}$ is the negative-definite $E_{8}$ lattice defined above and $U$ is the hyperbolic lattice.
This is an integral, even, unimodular lattice of rank $p+q$ and signature $(p, q)$ with discriminant $(-1)^p$.
We note that $G_{\beta}^{-1}$ is generally nontrivial due to the $E_{8}$ factors, making the dual basis somewhat difficult to work with by hand.
The following can be found in (Milnor 1958; Serre 1973): if $L$ is an even indefinite unimodular lattice with $\operatorname{sig}(L) = (p, q)$, then necessarily $\tau \equiv 0\pmod{8{\mathbf{Z}}}$ and $L { \, \xrightarrow{\sim}\, }   {\textrm{II}}_{p, q}$.

We conclude with the major classification theorems:

:::{.theorem title="Classification of indefinite unimodular lattices"}
Any indefinite unimodular lattice is determined up to isometry by its rank, index, and parity.
The same is true for _definite_ unimodular lattices $L$ with $\operatorname{rank} L \leq 8$.
:::

:::{.theorem title="Classification of small unimodular lattices"}
Let $L$ be _any_ unimodular integral lattice, definite or indefinite, with $\operatorname{rank}_{{\mathbf{Z}}} L \leq 4$.
Then either

- $L$ is odd and $L  { \, \xrightarrow{\sim}\, }   I_{p, q}$ for some $p, q$, or

- $L$ is even and either $L  { \, \xrightarrow{\sim}\, }   U$ or $U^{2}$.
:::

#### K3 and Enriques Lattices

The K3 lattice [ {L_{\mathrm{K3}}} \mathrel{\mathop:}= U\^{ 3} \oplus E_8\^{ 2} { \, \xrightarrow{\sim}\, } {\textrm{II}}*{3, 19} ,] is the unique even unimodular lattice of rank $22$ and signature \$ (3,19) \$ modeling $H^2(X; {\mathbf{Z}})$ of a K3 surface $X$.
We define $$ L_{\mathrm{K3}, 2d} ^{(m)} \mathrel{\mathop:}= \langle-2 d\rangle \oplus U^{2} \oplus E_{8}^{ m}, \qquad  L_{\mathrm{K3}, 2d}  \mathrel{\mathop:}=  L_{\mathrm{K3}, 2d} ^{(2)} ,$$ the degree 2d K3 lattices that appear in the study the moduli spaces $F_{2d}$ of K3 surfaces with a polarization of degree $2d$ and similar moduli problems.
The lattice $ L*{\mathrm{K3}, 2d} $, corresponding to the $m=2$ case, models the orthogonal complement in $ {L*{\mathrm{K3}}} $ of a polarization $h$ of degree $2d$.
We also recall that the Enriques lattice is defined as [ {L_{\mathrm{En}}} \mathrel{\mathop:}= U \oplus E_8 { \, \xrightarrow{\sim}\, } {\textrm{II}}*{1, 9} ,] the unique even unimodular lattice of rank $10$ and signature \$ (1,9) \$, modeling (the free part of) \$ H\^2(Z; {\mathbf{Z}}) \$ for an Enriques surface \$ Z \$.

#### Nikulin's Lattices

Let ${\mathbf{Z}}*2$ denote the 2-adic integers.
For $k \geq 0$, define $$ V*{k}\mathrel{\mathop:}= \left({\mathbf{Z}}*{2}^{2},\left[\begin{array}{cc} 2^{k+1} & 2^{k} \\
2^{k} & 2^{k+1} \end{array}\right]\right) $$ For $k=1$, we write $V \mathrel{\mathop:}= V_1$.
This is an even, nondegenerate lattice of 2-adic rank $2$ and signature $(2, 0)$ that we write as $V$.
Similarly, we define $$ U*{k}\mathrel{\mathop:}= \left({\mathbf{Z}}_{2}^{2},\left[\begin{array}{cc} 0 & 2^{k} \\
2^{k} & 0 \end{array}\right]\right) $$ over the 2 -adic integers and write $U \mathrel{\mathop:}= U_1$.
These lattices contribute to the indecomposable factors of general 2-elementary lattices, which we discuss in the next section.

<!-- Source: 1-part-combinatorial/2-chapter-lattice-theory/300-classification.md -->

### Classification Results {#section-2-3}

:::{#def:genus .definition title="{Genus of a Lattice}
"}
Two lattices $L_1, L_2$ belong to the same **genus** if $L_{1, {\mathbf{Z}}_p} \cong L_{2, {\mathbf{Z}}_p}$ for all primes $p$ and $L_{1, {\mathbf{R}}} \cong L_{2, {\mathbf{R}}}$.
Lattices in the same genus have the same rank, signature, and determinant, but may not be isometric over ${\mathbf{Z}}$.
We define the **class group** $\operatorname{cl}(L)$ to be the set of isometry classes within a genus, and the **class number** as the size of $\operatorname{cl}(L)$.
We note that for indefinite even lattices $L$, one typically expects the class number of $L$ to be one.
For definite lattices, the situation is reversed, and having class number one is somewhat rare.
By (Scattone 1987, sec.
3.4), if $\operatorname{rank}(L)>16+\ell(L)$, then $\operatorname{cl}(L) \geq 2$.
:::

#### p-Elementary Lattices

A lattice $(L,\beta)$ is **$p$-elementary** if its discriminant group $A_L$ is a $p$-elementary abelian group, i.e., $A_L \cong ({\mathbf{Z}}/p{\mathbf{Z}})^a$ for some integer $a \geq 0$.
We will be particularly concerned with the case $p=2$.
We call the exponent $a = \operatorname{rank}*{{ \mathbf{F} }*2} A_L$ the **2-rank** of the discriminant group.
For a 2-elementary lattice $L$, let $L^\dagger \mathrel{\mathop:}= L {}^{ \vee }(2)$.
We say $L$ is **co-even** if $L^\dagger$ is even and define the invariant $\delta = 0$, and **co-odd** otherwise and set $\delta = 1$.
Equivalently, `\begin{align} \delta(L) \mathrel{\mathop:}=  \begin{cases} 0 &  \text{ if }  q_{A_L}(x) \in {\mathbf{Z}} \,\,\forall\,\, x \in A_L \\ 1 &  \text{ otherwise }  \end{cases} \end{align}`{=tex} The following lattices are particularly important to the classification of 2-elementary lattices.
We note, however, that Nikulin works over ${ {\mathbf{Z}}*{\widehat{p}} }$ and particularly over ${ {\mathbf{Z}}*{\widehat{2}} }$, and so there are subtleties in choosing integral models that localize correctly.

\noindent `\resizebox{\linewidth}{!}{% \begin{tabular}{>{\raggedright\arraybackslash}m{0.4\linewidth} >{\raggedright\arraybackslash}m{0.45\linewidth} >{\centering\arraybackslash}m{0.15\linewidth}}
\toprule \textbf{$(L, \beta)$} & \textbf{$(A_L, q)$} & \textbf{Co-even/Co-odd} \\
\midrule $\langle 2 \rangle \cong \left( {\mathbf{Z}}, \begin{bmatrix} 2 \end{bmatrix} \right)$ & $p \cong {\mathfrak{q}}_1(2) \cong \left( C_2, \left[ \tfrac{1}{2} \right] \right)$ & Co-odd \\

$\langle -2 \rangle \cong \left( {\mathbf{Z}}, \begin{bmatrix} -2 \end{bmatrix} \right)$ & $q \cong {\mathfrak{q}}_1(-2) \cong \left( C_2, \left[ -\tfrac{1}{2} \right] \right)$ & Co-odd \\

$U(2) \cong \left( {\mathbf{Z}}^2, \begin{bmatrix} 0 & 2 \\ 2 & 0 \end{bmatrix} \right)$ & $u \cong {\mathfrak{u}}(2) \cong \left( C_2^2, \begin{bmatrix} 0 & \tfrac{1}{2} \\ \tfrac{1}{2} & 0 \end{bmatrix} \right)$ & Co-even \\

$V(2) \cong \left( {\mathbf{Z}}^2, \begin{bmatrix} 4 & 2 \\ 2 & 4 \end{bmatrix} \right)$ & $v \cong {\mathfrak{v}}(2) \cong \left( C_2 \times C_6, \begin{bmatrix} 1 & \tfrac{1}{2} \\ \tfrac{1}{2} & \tfrac{1}{3} \end{bmatrix} \right)$ & Co-even \\
\bottomrule \end{tabular} }`{=tex}

Let $L$ be an even, indefinite, 2-elementary lattice with $\operatorname{rank}(L) \geq 4$.
The classification of such lattices is determined by three invariants:

1. the rank $r = \operatorname{rank}_{{\mathbf{Z}}}(L)$,

2. the 2-rank $a = \dim_{{ \mathbf{F} }_2}(A_L)$, or equivalently $\ell(L)$, and

3. the coparity $\delta \in \{0,1\}$ as defined above.

We denote by $(r, a, \delta)*{n*+}$ the 2-elementary lattice with these invariants and signature $(n_+, n_-)$.
For each **admissible** triple (see (Nikulin 1980)) $(r, a, \delta)$ satisfying $r \geq 4$, there exists a unique isometry class of even, indefinite, 2-elementary lattice with these invariants.
Equivanelty, any two such lattices are isometric if and only if they have the same signature and isometric discriminant quadratic forms.

\todo{Check Nik80 citation to make sure this is where the conditions are spelled out.}

#### Decomposability of 2-elementary lattices

By (**AE23b?**) and (Nikulin 1979c, Prop.
1.8.1), if $L$ is an even 2-elementary lattice, then $A_{L}$ can be written as a finite direct sum of discriminant forms $p, q, u$, and $v$ above, subject to the relations

`\begin{align*} u^{ 2} & =v^{ 2} \\ p^{ 4} & =q^{ 4} \\ u \oplus p & =(p \oplus q) \oplus p \\ u \oplus q & =(p \oplus q) \oplus q \\ v \oplus p & =q^{ 3} \\ v \oplus q & =p^{ 3} \end{align*}`{=tex}

It is interesting to note that if one freely imposes these relations on the free group generated by $u,v,p,q$, one obtains the group ${\mathbf{Z}}\times {\mathbf{Z}}/4{\mathbf{Z}}$ with generators $v$ and $q$.
However, it is not immedaitely clear if this coincides with the corresponding Grothendieck group ${\mathsf{K}}_0$ of the category of such quadratic forms.
In any case, the even 2-elementary lattices that admit a primitive embedding into $ {L\_{\mathrm{K3}}} $ are finite direct sums of the following lattices, whose discriminant forms are recorded as well:

\begin{center}
\begin{tabular}{|l|l|l|}
\hline Lattice $L$ & Discriminant Form $A_{L}$ & Co-even/Coodd \\
\hline $A_{1}$ & $q\mathrel{\mathop:}= {\mathfrak{q}}_{1}(-2)$ & Co-odd \\
\hline $D_{4}$ & $v\mathrel{\mathop:}= {\mathfrak{v}}(2)$ & Co-even \\
\hline $D_{6}$ & $p^{ 2}\mathrel{\mathop:}= {\mathfrak{q}}_{1}(2)^{ 2}$ & Co-odd \\
\hline $D_{8}$ & $u\mathrel{\mathop:}= {\mathfrak{u}}(2)$ & Co-even \\
\hline $E_{7}$ & $p\mathrel{\mathop:}= {\mathfrak{q}}_{1}(2)$ & Co-odd \\
\hline $E_{8}$ & $0$ & Co-even \\
\hline $E_{8}(2)$ & $u^{ 4}\mathrel{\mathop:}= {\mathfrak{u}}(2)^{ 4}$ & Co-even \\
\hline $\langle 2\rangle$ & $p\mathrel{\mathop:}= {\mathfrak{q}}_{1}(2)$ & Co-odd \\
\hline $U$ & $0$ & Co-even \\
\hline $U(2)$ & $u\mathrel{\mathop:}= {\mathfrak{u}}(2)$ & Co-even \\
\hline
\end{tabular}
\end{center}

#### Ordinary and Characteristic

For 2-elementary lattices, one always has $\operatorname{div}*{L}(v) \in\{1,2\}$.
We set $v^{*}\mathrel{\mathop:}= v / \operatorname{div}*{L}(v) \in$ $A_{L}$.
Letting $q_{L}: A_{L} \to {1\over 2} {\mathbf{Z}} / {\mathbf{Z}}$ be the induced quadratic form on $A_{L}$, we say $v^{*}$ is **characteristic** if $q_{L}(x)=\beta_{L}\left(v^{*}, x\right) \bmod {\mathbf{Z}}$ for all $x \in A_{L}$, and is **ordinary** otherwise.
We say that a primitive isotropic vector $e \in L$ is

- **odd** if $\operatorname{div}_{L}(v)=1$,

- **even ordinary** if $\operatorname{div}_{L}(v)=2$ and $v^{*}$ is ordinary, or

- **even characteristic** if $\operatorname{div}_{L}(v)=2$ and $v^{*}$ is characteristic.

Such vectors play a role in the mirror move algorithm of \todo{Cite}, which can be used to determine 0-cusps and 1-cusps of K3 compactifications.

<!-- Source: 1-part-combinatorial/2-chapter-lattice-theory/400-group-actions.md -->

### Group Actions and Isometries {#section-2-4}

Define the space of **isometries** between two lattices $(L_1, \beta_1)$ and $(L_2, \beta_2)$ as $$\operatorname{Isom}(L_1, L_2) \mathrel{\mathop:}=  \{f \in \operatorname{Hom}*{\operatorname{Lat}*{{\mathbf{Z}}}}(L_1, L_2) {~~\mathrel{\Big\vert}~~} f \text{ is an isomorphism of } {\mathbf{Z}}\text{-modules}\}$$ Two lattices are **isometric** ($L_1 \cong L_2$) if and only if this set is non-empty.

#### Reflections and Transvections

Let $(L,\beta)$ be a nondegenerate integral lattice.
For an anisotropic vector $\alpha \in L$ satisfying the condition $2\beta(\alpha, L) \subseteq \beta(\alpha,\alpha){\mathbf{Z}}$, the **reflection in $\alpha$** is the isometry: $$s_\alpha(x) \mathrel{\mathop:}=  x - 2\frac{\beta(\alpha,x)}{\beta(\alpha,\alpha)}\alpha$$ Reflections have determinant -1 and act as the identity on the orthogonal complement $\left\langle \alpha \right\rangle^{\perp L}$.
The group generated by all such reflections is the **Weyl group** $W(L) \leq \operatorname{O}(L)$.
Letting $e \in L_{\mathbf{Q}}$ be an isotropic vector and let $a \in \left\langle e \right\rangle^{\perp_{L_{\mathbf{Q}}}}$ be any vector satisfying $a\cdot e=0$.
The **Seigel-Eichler transformation** associated to the pair $(e, a)$ is the isometry $E_{e,a} \in \operatorname{O}(L_{\mathbf{Q}})$ defined by: $$ E*{e,a}(v) = v + \beta(e, v)a - \left( \beta(a, v) + {1\over 2}\beta(a, a)\beta(e, v) \right) e $$ If $a$ is also isotropic, this simplifies to $$ E*{e,a}(v) = v + \beta(e, v)a - \beta(a, v)e .$$ The **Eichler transvection group** $E(L)$ is generated by all such transvections where $e \in L$ is a primitive isotropic vector with $\operatorname{div}_L(e) = 1$, and $a \in \left\langle e \right\rangle^{\perp_L}$.
If $L$ is even, then $E(L) \subseteq \operatorname{O}^*(L)$.

#### Orbits of Isotropic Vectors

For a nondegenerate indefinite lattice $L$ and any integer $k$, the set of $\operatorname{O}(L)$-orbits of primitive vectors of norm $k$, denoted $L[k]/\operatorname{O}(L)$, is finite.
In particular, let $T$ be an even lattice of signature $(2,n)$ and let $\Gamma \subseteq \operatorname{O}(T)$ be an arithmetic subgroup (e.g., a subgroup of finite index like $\operatorname{O}^*(T)$). The 0-cusps of the Baily-Borel compactification of the associated arithmetic quotient $F_\Gamma \mathrel{\mathop:}=  { D_{T} }/{\Gamma} $ are in one-to-one correspondence with $\Gamma$-orbits of primitive rank 1 isotropic sublattices of $T$, i.e. $$ \partial*0\overline{F*\Gamma}^{ \operatorname{BB} }\mathrel{\mathop:}= \partial*0\overline{ { D*{T} }/{ \Gamma } }^{ \operatorname{BB} } \rightleftharpoons L[0]/\Gamma = \left\{{v \in L {~~\mathrel{\Big\vert}~~} v \text{ is primitive and } v^2 = 0}\right\} / \Gamma .$$ For $T \mathrel{\mathop:}= T_{{\mathrm{En}}}$, the appropriate arithmetic group ${\Gamma_{{\mathrm{En}}, 2}} $ has exactly 5 orbits of primitive isotropic vectors, yielding 5 cusps of $\overline{F_{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$.
They are partitioned by divisibility: there is one orbit of divisibility 1 vectors, and 4 orbits of divisibility 2 vectors.
We are thus interested in classifying orbits of primitive isotropic vectors.
For lattices containing a double hyperbolic plane $U^2$, we recount the following useful theorems:

:::{#thm:eichler-siegel-transformations .theorem}
There is an isometry $$
\phi: U \oplus U \to (\operatorname{Mat}_{2 \times 2}({\mathbf{Z}}), 2\cdot \operatorname{det})
.$$ Under $\phi$, the group generated by Eichler-Siegel transformations corresponds to the image of $\operatorname{SL}_2({\mathbf{Z}}) \times \operatorname{SL}_2({\mathbf{Z}})$ acting on a matrix $X$ by $(A, B)\curvearrowright X \mathrel{\mathop:}= A X B^{-1}$.
:::

:::
proof
Write $L = U \oplus U'$ as two distinct copies of $U$.
The map $\phi: L \to \operatorname{Mat}_{2 \times 2}({\mathbf{Z}})$ defined by [ ae + df + be' + cf' \mapsto
\begin{pmatrix} a & b \\ -c & d \end{pmatrix}

] is a ${\mathbf{Z}}$-module isomorphism.
To check that $\phi$ is an isometry for the quadratic form, observe that [ (ae + df + be' + cf')\^2 = 2ad + 2bc. ,] which is precisely twice the determinant of the coresponding matrix.
The group $SL_2({\mathbf{Z}}) \times SL_2({\mathbf{Z}})$ acts on $\operatorname{Mat}_{2 \times 2}({\mathbf{Z}})$ by [ (A, B): X \mapsto A X B\^{-1}, ] which preserves the determinant and thus the bilinear form.
The action of $SL_2({\mathbf{Z}})$ by left multiplication corresponds to elementary row operations (acting on the basis $\{e, f\}$), and the action on the right corresponds to elementary column operations (acting on the basis $\{e', f'\}$).
We conclude using the fact that $SL_2({\mathbf{Z}})$ is generated by elementary matrices.
:::

:::{.theorem title="{[@Sca87, Prop 3.7.3]}
"}
Let $L$ be an even lattice that decomposes as $L  { \, \xrightarrow{\sim}\, }   U^{2} \oplus M$ where $M$ is any lattice, and suppose $v, w \in L[k]$ for some fixed $k$.
Then $$
v \sim*{E(L)} w \Longleftrightarrow\left[v^{*}\right]=\left[w^{*}\right] \in A\*{L} .

$$
:::

:::{.proof title="Sketch"}
Suppose that $\phi(v)=w$ for some $\phi \in E(L)$. Then necessarily $\phi^{*}\left(\left[v^{*}\right]\right)=\left[w^{*}\right]$ in $A_{L}$ by restriction. However, $E(L) \subseteq \operatorname{O}^*(L)$, so $\phi$ must induce the identity on $A_{L}$ and thus $\left[v^{*}\right]=\left[w^{*}\right]$. Conversely, suppose that $\left[v^{*}\right]=\left[w^{*}\right]$ in $A_{L}$. Write $L=U_{1} \oplus U_{2} \oplus M$; then by the above proposition we may assume that $v, w \in L^{\prime}\mathrel{\mathop:}= M \oplus U_{1}$ up to $E\left(U_{1} \oplus U_{2}\right)$. Since $\left[v^{*}\right]=\left[w^{*}\right]$, in particular these elements have the same order in $A_{L}$, and so $\operatorname{div}_{L}(v)=\operatorname{div}_{L}(w)=d$ is a fixed positive integer. Thus there exist $x, y \in L^{\prime}$ such that $\beta(x, v)=d$ and $\beta(y, w)=d$. We now claim that $z\mathrel{\mathop:}= \frac{v}{d}-\frac{w}{d}=\frac{v-w}{d}$ is an element of $M \oplus U_{1}$. This follows from the fact that $v^{*} \equiv w^{*}\left(\bmod L^{\prime}\right)$, so $\frac{v}{d} \equiv \frac{w}{d}$ $\left(\bmod L^{\prime}\right)$. Thus $z\mathrel{\mathop:}= \frac{v}{d}-\frac{w}{d} \equiv 0 \bmod L$ is an element of $L^{\prime}$. Using the fact that $d z^{2}=2 v z$, a direct calculation shows that the following composition maps $v$ to $w$: $$
E_{e, y} \circ E_{f,-z} \circ E_{e,-x}
.
$$
:::

#### Group Actions

For a faithful representation $G \hookrightarrow \operatorname{O}(L)$ realizing a group $G$ acting on $L$ by isometries, the sublattice of **invariants** and **coinvariants** are defined as $$ L^G \mathrel{\mathop:}=  \{v \in L {~~\mathrel{\Big\vert}~~} g.v = v \,\,\forall\,\, g \in G\}, \qquad L_G \mathrel{\mathop:}=  (L^G)^{\perp L} .$$ If $I$ is an involution ($I^2=\mathrm{id}$), these correspond to the eigenspaces for eigenvalues +1 and -1, respectively, for the induced action on $L_{\mathbf{Q}}$.
More generally, if $G \hookrightarrow \operatorname{O}(L)$ is a faithful representation of a finite cyclic group $G$, then $L^G$ and $L_G$ are primitive sublattices, and $L^G \oplus L_G$ has finite index in $L$.
If $I \in \operatorname{O}^*(L)$ is an involution and $L$ is 2-elementary, then both $L^I$ and $L_I$ are again 2-elementary lattices.

#### Applications

:::{#def:overlattices-gluing .definition title="{Overlattices and Gluing Theory}
"}
An **overlattice** $L$ of a lattice $S$ is a lattice containing $S$ as a finite-index sublattice.
Nikulin's theory provides a classification of even overlattices of $S$ in terms of isotropic subgroups of $A_S$ up to $\operatorname{O}(S)$.
:::

<!-- Source: 1-part-combinatorial/2-chapter-lattice-theory/500-nikulin-theory.md -->

### Nikulin's Embedding Theorems {#section-2-5}

Throughout this section, we adopt some simplifying notational conventions: for any lattice $L$, writing $\operatorname{sig}(L) = (p, q)$, we define $\tau(L) = p+q$, $\min \operatorname{sig}(L) = \min\left\{{p, q}\right\}$, and $\max\operatorname{sig}(L)$ similarly.
Let $S \hookrightarrow L$ be an embedding of lattices.
We say $L$ is an **overlattice** of $S$ if $\iota(S)$ is a finite index sublattice.
We will be primarily interested in the case where $S\hookrightarrow L$ is a primitive embedding with $T\mathrel{\mathop:}= S^{\perp L} \hookrightarrow L$ its (primitively embedded) orthogonal complement.
In this situation, $L$ is an overlattice of $S\oplus T$, and we would like to know when it is of index 1. When this happens, we will say that $S$ **splits** $L$.
We first note a basic tool: for any lattice $L$, there is a canonical primitive embedding `\begin{align*} \delta: L(2) &\to L \oplus L \\ v &\mapsto (v, v) \end{align*}`{=tex}

#### Scattone's Methods

:::{#rem:scattone-method-niemeier .remark title="Scattone's Method: Enumerating Boundary Components via Niemeier Lattices"}
To motivate the detailed study of primitive embeddings, we note that the method of (Scattone 1987) provides a concrete arithmetic approach to enumerating $0$-cusps in the Baily--Borel compactification $\overline{F_{2d}}^{ \operatorname{BB} }$ of the moduli space of degree-$2d$ polarized K3 surfaces.

By the classification of boundary components for arithmetic quotients of Hermitian symmetric domains ((Baily and Borel 1966)), $0$-cusps correspond to $\Gamma_{2d}$-orbits of primitive isotropic lines $I \subset L_{2d}$, where $$
 L_{\mathrm{K3}, 2d}  \mathrel{\mathop:}=  \langle -2d \rangle \oplus U^{ 2} \oplus E_8^{ 2}
$$ is the rank-$21$ lattice of signature $(2,19)$ associated to degree-$2d$ polarized K3 surfaces.

Each such cusp corresponds to a degeneration of K3 surfaces with associated lattice $I^\perp / I$, an even lattice of signature $(1,18)$, which encodes the limiting Hodge structure for degenerations to that cusp.
(Scattone 1987) classified boundary components by studying primitive embeddings $U\hookrightarrow L$ where $L$ is one of the $24$ **Niemeier lattices** -- the even, negative-definite, unimodular lattices of rank $24$.
For each such embedding $U \hookrightarrow L$, the orthogonal complement $T \mathrel{\mathop:}=  U^{\perp_L}$ is an even, negative-definite, unimodular lattice of rank $22$.
These are the possible isometry classes of lattices of the form $I^{\perp}/I$ at $0$-cusps of $\overline{F_{2d}}^{ \operatorname{BB} }$.
The enumeration of $0$-cusps is thus reduced to counting the orbits of primitive embeddings $U \hookrightarrow L$ for each Niemeier lattice $L$ up to $\operatorname{O}(L)$, where (Scattone 1987) establishes that each such orbit corresponds to a _distinct_ $0$-cusp, allowing for an explicit enumeration and thus an understanding of the entire cusp diagram for $F_{2d}$ for a wide range of values of $d$.
From this, we find that the class number $\operatorname{cl}(T)$ directly indluences the number of 0-cusps, and representatives of isometry classes can be used to provide an explicit indexing set.
:::

#### Existence and Uniqueness

:::{#thm:nik79-1-14-4 .theorem title="{Nikulin's Analog of Witt's Theorem [@Nik79, Thm.~1.14.4]}
"}
Let $S$ be an even lattice and $L$ an even unimodular lattice.
Then

1.  **The weak case:**\
    If $\operatorname{sig}(L) > \operatorname{sig}(S)$ and $\operatorname{rank}(L) - \operatorname{rank}(S) \geq 2 + \ell(A_S)$, then there exists a primitive embedding $S \hookrightarrow L$ that is unique up to isometry.

2.  **The generic case:**\
    If $\operatorname{sig}(L) > \operatorname{sig}(S)$ and $\operatorname{rank}(L) - \operatorname{rank}(S) \geq 2 + \max_{p \neq 2} \ell(A_{S_p})$, then there exists a primitive embedding $S \hookrightarrow L$ that is unique up to isometry.

3.  **The exceptional 2-adic case:**\
     If $\operatorname{sig}(L) > \operatorname{sig}(S)$ and $\operatorname{rank}(L) - \operatorname{rank}(S) = \ell(A_{S_2})$, then a primitive embedding exists **if and only if** there exists some $q'$ such that $q_S$ satisfies $$
      q_S \cong u_{+}^{(2)}(2) \oplus q' \quad  \text{ or }  \quad q_S \cong v_{+}^{(2)}(2) \oplus q'
      .$$
    :::

We note that this is not how (Nikulin 1979a) originally states the theorem, but rather extracts the case that is more commonly used in applications for clarity.
The generic case is both necessary and sufficient for the existence and uniqueness of a primitive embedding, The weak case, which uses the global invariant $\ell(A_S)$ is easier to check in practice, but only gives a sufficient condition and is thus strictly weaker than the generic case.
This is because if $A$ is any finite abelian group, one can consider the primary decomposition $A = \bigoplus_p A_p$, and there is an inequality $\max_p \ell(A_p) \leq \ell(A) \leq \sum_p \ell(A_p)$.
Thus, using $\ell(A_S)$ in place of $\max_{p \neq 2} \ell(A_{S_p})$ can exclude embeddings that the generic case would allow.

The weak and generic embedding criteria for Nikulin's theorem coincide if and only if the minimal number of generators of the group equals the maximum of the minimal numbers of generators of its $p$-primary parts, i.e., $\ell(A) = \max_p \ell(A_p)$.
When $\ell(A) > \max_p \ell(A_p)$, the weak criterion requires a larger difference in ranks than the generic criterion, and thus gives only a sufficient (not necessary) condition for embedding.
This is best illustrated through concrete examples:

Let $A = {\mathbf{Z}}_6 \cong {\mathbf{Z}}_2 \times {\mathbf{Z}}_3$.
Then $A_2 = {\mathbf{Z}}_2$ with $\ell(A_2) = 1$, and $A_3 = {\mathbf{Z}}_3$ with $\ell(A_3) = 1$.
Since $A$ is cyclic, we have $\ell(A) = 1$, and $\max\{\ell(A_2), \ell(A_3)\} = 1$.
The weak and generic criteria coincide, since $\ell(A) = \max\{\ell(A_2), \ell(A_3)\}$.

Let $A = {\mathbf{Z}}_2 \oplus {\mathbf{Z}}_3$.
Then $A_2 = {\mathbf{Z}}_2$ with $\ell(A_2) = 1$, $A_3 = {\mathbf{Z}}_3$ with $\ell(A_3) = 1$, and $\ell(A) = 2$, since both factors are needed to generate $A$.
We have $\max\{\ell(A_2), \ell(A_3)\} = 1$, and the weak criterion now requires rank difference $d$ to satisfy $d\geq 2 + 2$, while the generic criterion only requires $d \geq 2 + 1$.
Thus, the weak case is strictly weaker and more restrictive: it may exclude embeddings allowed by the generic criterion.

##### Elementary abelian groups:\*\*

Let $A = {\mathbf{Z}}_2 \oplus {\mathbf{Z}}_2$ Then $A_2 = {\mathbf{Z}}_2 \oplus {\mathbf{Z}}_2$ with $\ell(A_2) = 2$, and $\ell(A) = 2$ with $\max\{\ell(A_2)\} = 2$.
Here, the weak and generic criteria again coincide.
Thus the weak criterion is **always** sufficient, but only necessary when $\ell(A) = \max_p \ell(A_p)$, and the actual difference between the two cases depends highly on the structure of the group in question.
When $\ell(A) > \max_p \ell(A_p)$, the weak criterion is strictly more restrictive and does not capture all cases allowed by the generic condition.

#### Finiteness

::: {.proposition title="Finiteness of embeddings for even, unimodular lattices"}
If $S$ and $L$ are even lattices and $L$ is unimodular, then $\operatorname{Emb}(S, L)$ is a finite set.
:::

:::
proof
By (Nikulin 1979c, Prop.
1.6.1), such a primitive embedding $\iota: S \hookrightarrow L$ is determined by an isometry $\gamma: A_{S}  { \, \xrightarrow{\sim}\, }   A_{T}(-1)$, two such primitive embeddings are equivalent if and only if $\gamma_{1}$ is conjugate to $\gamma_{2}$ under $\operatorname{O}\left(A_{T}\right)$, and $\iota_{1}\left(S_{1}\right)  { \, \xrightarrow{\sim}\, }   \iota_{2}\left(S_{2}\right)$ are equivalent primitive sublattices if $\exists(\phi, \psi) \in \operatorname{O}(S) \oplus \operatorname{O}(T)$ such that $\left.\gamma_{1} \circ \phi\right|_{A_{S}}=\left.\psi\right|_{A_{T}} \circ \gamma_{2}$.
Since $A_{S}, A_{T}$ are finite abelian groups, $\operatorname{Isom}\left(A_{S}, A_{T}\right)$ is a finite set, as is $\operatorname{O}\left(A_{T}\right)$.
Moreover, noting that if $S_{1}  { \, \xrightarrow{\sim}\, }   S_{2}$ then $A_{S_{1}}  { \, \xrightarrow{\sim}\, }   A_{S_{2}}$ and thus $\operatorname{Emb}\left(S_{1}, L\right) \cong \operatorname{Emb}\left(S_{2}, L\right)$, so $\operatorname{Emb}(S, L)$ only depends on the isometry class of $S$.
Since gen $(S)$ is a finite set, there are only finitely many isometry classes of $S$, so the class group $\operatorname{cl}(S)$ is finite and thus $\operatorname{Emb}(S, L)$ a finite set.
:::

#### Splitting

:::{.remark title="Discriminant form and anti-isometry"}
The discriminant group $A_S = S^\vee/S$ of $S$ carries a finite quadratic form $q_S$.
The structure of the orthogonal complement $T$ and the existence of an overlattice are governed by the existence of an **anti-isometry** between $(A_S, q_S)$ and $(A_T, -q_T)$.
This anti-isometry encodes the gluing data for constructing $L$ as an overlattice of $S \oplus T$.
The following results collect the relevant facts for this aspect of the theory:
:::

:::{#thm:primitive-embedding-corrected .theorem title="{Primitive Embedding Theorem [@PS24, Prop.~15.1.1]}
"}
Let $S$ be a primitive non-degenerate sublattice of a unimodular lattice $L$, and let $T = S^{\perp L}$ be its orthogonal complement.
Then:

1.  $S \oplus T$ is a sublattice of $L$ of finite index.

2.  $[L\colon S \oplus T] = |A_S| = |A_T|$, where $A_S = S^*/S$ and $A_T = T^*/T$ are the discriminant groups.

3.  There is a canonical isomorphism $\psi: A_S \to A_T$ such that the discriminant forms are related by an **anti-isometry**: $$
    q_{A_T}(\psi(x)) = -q_{A_S}(x) \qquad \forall x\in A_S
    .$$
    :::

#### Gluing and Overlattices

Throughout this section, for a discriminant group $(G, q)$, we write $G(n)$ for the group $G$ with quadratic form $\tilde q \mathrel{\mathop:}= n q$.
In particular, $G_1 { \, \xrightarrow{\sim}\, }   G_2(-1)$ are isometric by a map $f$ if and only if $G_1\cong G_2$ as groups and $q_1(v) = -q_2(f(v))$ for all $v\in G_1$.
Let $L$ be as above; a primitive embedding $S \hookrightarrow L$ with $T\mathrel{\mathop:}= S^{\perp L}$ is uniquely determined by the choice of

1.  A subgroup $H \leq A_{L}$, the _embedding subgroup_, and

2.  An isometry $\gamma: H  { \, \xrightarrow{\sim}\, }   H^{\prime} \subseteq A_{S}$, the _embedding isometry_, where $H'$ is the image of $H$.

Letting $\Gamma$ be the graph of $\gamma$ in $A_{L} \oplus A_{S}(-1)$, one has $A_{T}=\Gamma^{\perp} / \Gamma$ and we note that there is a dicriminant formula $$
|\operatorname{disc} T|=\frac{|\operatorname{disc} L| \cdot|\operatorname{disc} S|}{(\sharp H)^{2}} 
.$$ Now let $\iota: S \hookrightarrow L$ be an embedding of even lattices where $L$ is unimodular, and define $H_{L}\mathrel{\mathop:}= L / \iota(S)$.
Using the chain of embeddings $S \hookrightarrow L \hookrightarrow L^{\vee} \hookrightarrow S^{\vee}$ to produce embeddings $H_{L} \hookrightarrow L^{\vee} / S \hookrightarrow A_{S}$, one can regard $H_L$ as a subgroup of $A_S$.
Conversely, for a subgroup $H \leq A_{S}$, write $\eta: S^{\vee} \to A_{S}$ and define a lattice $S_{H}\mathrel{\mathop:}= \eta^{-1}(H) \subseteq S^{\vee}$.
We note that $S_{H} \supseteq S$, so $S_{H}$ is an overlattice of $S$.

These constructions are mutually inverse and define a bijection: `\begin{align*}
\{\text { Even overlattices } L \text { of } S\} & \rightleftharpoons
\left\{\text { Isotropic subgroups } H \leq A_{S}\right\} \\
L &\mapsto H_{L}\mathrel{\mathop:}= L / S \\
L\mathrel{\mathop:}= S_{H} & \leftarrow H
\end{align*}`{=tex}

We apply this to the following:

::: proposition
Let $L$ be a unimodular lattice and $\iota: S \hookrightarrow L$ be a primitively embedded sublattice.
Then $|\operatorname{disc}(S)|=|\operatorname{disc}(T)|$, and if $S$ is unimodular, then $L \cong$ $S \oplus T$.
:::

:::
proof
We have $$
|\operatorname{disc}(S)|=\sharp A_{S} = \sharp A_{T}=|\operatorname{disc}(T)| .
$$ The isometry follows from Proposition 1.3.7: since $S \oplus T \leq L$ is a full-rank sublattice, $T$ is also unimodular and thus $$
[L: S \oplus T]^{2}=\frac{\operatorname{disc}(S \oplus T)}{\operatorname{disc}(L)}=\frac{\operatorname{disc}(S) \cdot \operatorname{disc}(T)}{\operatorname{disc}(L)}=1 .
$$ Finally, a pair of isometries of $S$ and $T$ lifts to an isometry of $L$ if and only if they preserve $H_{L}$, or equivalently commute with the glue map.
Thus given $S\hookrightarrow L$ as above with $T\mathrel{\mathop:}= S^{\perp L}$, even if $S$ does not split $L$, we still have a way to construct isometries on $L$: one first constructs isometries $f_S\in \operatorname{O}(S)$ and $f_T \in \operatorname{O}(T)$ such that the restricted action of $f_S$ to $A_S$ and that of $f_T$ to $A_T$ agree, using the anti-isometry $A_S { \, \xrightarrow{\sim}\, }   A_T(-1)$, then produces a lift of $f_S \oplus f_T$ to an element of $f\in \operatorname{O}(L)$ that restricts to both $f_S$ and $f_T$.
In particular, $f$ stabilizes both $S$ and $T$, and thus defines isometries in the stabilizers $\operatorname{Stab}_{\operatorname{O}(L)}(S)$ and $\operatorname{Stab}_{\operatorname{O}(L)}(T)$.
:::

#### Applications to $F_{{\mathrm{En}}, 2}$ {#lemma-fent-to-fttz-closed-immersion}

To see some of this theory applied to the moduli problem at hand, we take a small detour to prove that $F_{{\mathrm{En}}, 2}$ is the normalization of a closed subvariety of $F_{(2,2,0)}$ -- an essential ingredient in the main theorem.
The strategy is as follows:

1. Identify a morphism $\Psi: F_{{\mathrm{En}}, 2} \to F_{(2,2,0)}$ arising from a lattice embedding $\tilde \Psi: T_{{\mathrm{En}}} \hookrightarrow T_{\operatorname{dP}}$.

2. Establish a rigidity theorem at the level of lattice embeddings to assert that $\Psi$ is well-defined and canonically determined.

3. Restrict $\Psi$ to its scheme-theoretic image, i.e. the smallest closed subscheme of $F_{(2,2,0)}$ through which $\Psi$ factors, to obtain $\Psi: F_{{\mathrm{En}}, 2} \to X$

4. Since we know $F_{{\mathrm{En}}, 2}$ is normal by the standard theory of (Baily and Borel 1966), so we then appeal to Zariski's main theorem: since $X$ is a closed subscheme of a normal variety, if $\Psi$ is finite and birational, it satisfies the universal property of normalization.

We first claim there is a holomorphic, algebraic morphism of period domains `\begin{align*} \tilde \Psi: D_{T_{{\mathrm{En}}}} \to D_{T_{\operatorname{dP}}} \\ \end{align*}`{=tex}

This follows from defining an embedding of lattices by `\begin{align*} \tilde \Psi: T_{{\mathrm{En}}} \mathrel{\mathop:}= U \oplus U(2) \oplus E_8(2) &\hookrightarrow T_{\operatorname{dP}}\mathrel{\mathop:}=  U \oplus U(2) \oplus E_8^2 \\ (u_1, u_2, v) &\mapsto (u_1, u_2, v, v) \end{align*}`{=tex} which in block form is $(\mathrm{id}, \mathrm{id}, \delta)$ where $\delta$ is the canonical doubling embedding.
To see that this induces a well-defined morphism after passing from lattices to period domains, note that its construction is functorial: it involves tensoring to ${\mathbf{C}}$, projectivizing, restricting to a quadric, and then further restricting to a semialgebraic subset in both the source and the target, cut out by precisely the same conditions.
The map $\tilde \Psi$ is holomorphic because it is the restriction of a linear map to an open set, and algebraic (and hence a morphism) because both varieties are quasiprojective and $\tilde \Psi$ is linear.

We now claim this morphism is well-defined and canonical in the following sense: let $A_i\to B_i \to C_i$ for $i=1,2$ be two sequences of primitive embeddings.
We say two such sequences are **equivalent** if there exist isometries making the following diagram commute:

\begin{tikzcd}
A_1 \arrow[r, "f_1"] \arrow[d, "\phi_A", "\simeq"'] & B_1 \arrow[r, "g_1"] \arrow[d, "\phi_B", "\simeq"'] & C_1 \arrow[d, "\phi_C", "\simeq"'] \\
A_2 \arrow[r, "f_2"] & B_2 \arrow[r, "g_2"] & C_2
\end{tikzcd}

In particular, if $C_1 = C_2 = L$ is a fixed lattice, then $\phi_C\in\operatorname{O}(L)$ and we say the sequences are *equivalent up to $\operatorname{O}(L)$*. If $A_1 = A_2 = A$ and $B_1=B_2 = B$ are also fixed and any two such sequences $A \to B \to L$ are equivalent, we say the sequence is **unique up to isometry** or **unique up to $\operatorname{O}(L)$**. We observe several useful facts:

- $A\hookrightarrow B\hookrightarrow L$ is unique up to $\operatorname{O}(L)$ if and only if $A^{\perp L} \hookrightarrow B^{\perp L}\hookrightarrow L$ is,

- $A\hookrightarrow B\hookrightarrow L$ is unique if $B\hookrightarrow L$ is unique and $A\hookrightarrow B$ is unique,

- $A(n) \hookrightarrow B(n)$ is unique if $A\hookrightarrow B$ is unique

The following is proved as (**AEGS23?**, Lem.
2.4):

:::
proposition
The following sequence of primitive embeddings is unique up to isometry: `\begin{align*}
\tilde \Psi: T_{{\mathrm{En}}} \hookrightarrow T_{\operatorname{dP}} \hookrightarrow  {L_{\mathrm{K3}}}  
.\end{align*}`{=tex}
:::

:::
proof
Passing to orthogonal complements in $ {L*{\mathrm{K3}}} $ yields the sequence $$
\left( {
S*{{\mathrm{En}}} \hookrightarrow S*{\operatorname{dP}} \hookrightarrow L
} \right) =
\left( {
U(2) \hookrightarrow U(2) \oplus E_8(2) \hookrightarrow L
} \right)
.$$ We first claim $U(2) \hookrightarrow U(2) \oplus E_8(2)$ is unique.
By untwisting, it suffices to show that $U\hookrightarrow U\oplus E_8$ is unique.
Write $U = S = {\textrm{II}}*{1,1}$ and $U \oplus E_8 = L = {\textrm{II}}_{1, 9}$, noting that both are the unique even unimodular lattices with those signatures.
The existence of an embedding $S\hookrightarrow L$, is clear, since one can simply take $x\mapsto (x, 0)$ and check that the cokernel is isometric to $E_8$ and thus free.
For uniqueness, let $T\mathrel{\mathop:}= S^{\perp L}$: then $T$ is an even unimodular lattice of signature $(0, 8)$, and thus isometric to $E_8 = {\textrm{II}}_{0, 8}$, which is unique up to isometry.
So if $j_i: S_i \hookrightarrow L$ are any two primitive embeddings, there are decompositions $L \cong S_1 \oplus T_1$ and $L\cong S_2 \oplus T_2$ where $S_1\cong S_2 \cong {\textrm{II}}_{1,1}$ and $T_1\cong T_2 \cong {\textrm{II}}_{0, 8}$ are both unique up to isometry.
So there exist isometries $\phi_S: S_1\to S_2$ and $\phi_T: T_1\to T_2$, and thus an isometry $\phi_S \oplus \phi_T: S_1\oplus T_1\to S_2\oplus T_2$.
Since $S_i, T_i$ are unimodular, $\phi_S$ and $\phi_T$ trivially act identically on the discriminant groups, and thus lift to an isometry $\phi\in \operatorname{O}(L)$.
So $j_1$ is equivalent to $j_2$ as an embedding.

We now claim that the second embedding $U(2)\oplus E_8(2)\hookrightarrow  {L_{\mathrm{K3}}}  = U^2 \oplus E_8^3$ is unique.
This follows from Nikulin's version of Witt's \Cref{thm:nik79-1-14-4}:

1.  $\operatorname{sig}( {L_{\mathrm{K3}}} ) = (3, 19) > \operatorname{sig}(U(2) \oplus E_8(2)) = (1, 9)$,
2.  $\operatorname{rank}( {L_{\mathrm{K3}}} ) - \operatorname{rank}(U(2) \oplus E_8(2)) = 22-10 \geq 2 + \ell(A_S) = 2 + 10$.

We conclude by the observations above.
:::

:::
proposition
The map $\tilde \Psi$ descends to a well-defined algebraic morphism on arithmetic quotients: $$
\Psi: F_{{\mathrm{En}}, 2} = D_{T_{{\mathrm{En}}}}/{\Gamma_{{\mathrm{En}}, 2}}  \to F_{(2,2,0)} = D_{T_{\operatorname{dP}}}/\operatorname{O}(T_{\operatorname{dP}})
.$$
:::

:::
proof
It suffices to show that every isometry of $T_{{\mathrm{En}}}$ extends to an isometry of $T_{\operatorname{dP}}$ preserving $T_{{\mathrm{En}}}$.
This follows from a standard lattice-theoretic argument involving discriminant groups: let $S = T_{{\mathrm{En}}} = U \oplus U(2) \oplus E_8(2)$ and $T = S_{{\mathrm{En}}} = U(2) \oplus E_8(2) = S^{\perp L}$ where $L =  {L_{\mathrm{K3}}} $. We note that $$
A*S = A*{U(2)} \oplus A*{E_8(@)} = C_2^2 \oplus C_2^{8} \cong C_2^{10} \cong A_T
,$$ and that $S$ and $T$ are both even indefinite 2-elementary lattices.
By (Nikulin 1979a, Thm.
3.6.3), the restrictions $\operatorname{O}(S)\to\operatorname{O}(A_S)$ and $\operatorname{O}(T) \to\operatorname{O}(A_T)$ are surjective, and thus of $f\in \operatorname{O}(S)$, using the fact that $A_S\cong A_T$, the restricted isometry $f*{A*S}$ induces an isometry $f*{A*T}$ on $A_T$, which can be be lifted to an isometry $f_T$ on $T$.
By construction, $f*{T}$ and $f_{S}$ act identically on $A_S$ and $A_T$, and so lift to an isometry $f\in \operatorname{O}(L)$ preserving both $S$ and $T$.
:::

:::{.lemma title="{[@AEGS23, Lemma 2.8]}
"}
There exists a closed subscheme $X \subset F_{(2,2,0)}$ such that $F_{{\mathrm{En}}, 2}$ is canonically isomorphic to the normalization of $X$.
:::

:::
proof
The result follows by restricting the period morphism $\Psi$ to its scheme-theoretic image $X$ and replacing it by $\Psi: F_{{\mathrm{En}}, 2} \to X$.
The morphism $\Psi$ is finite and birational.
Birationality is established by the fact that $\Psi$ is an open immersion over the locus of smooth, generic Enriques surfaces, and thus is birational onto its image.
Finiteness holds since $\Psi$ is proper and quasi-finite.
Both $F_{{\mathrm{En}}, 2}$ and $F_{(2,2,0)}$ are normal, as shown in [Borel--Baily, *Ann. of Math.* 84 (1966), 442--528, Theorem 10.11], since they are complex analytic manifolds.
The closed subscheme $X$ inherits normality as a subscheme of a normal variety.

By Zariski's Main Theorem, a finite birational morphism from a normal variety to an integral variety identifies the source with the normalization of the target.
Therefore, $\Psi\colon F_{{\mathrm{En}}, 2} \to X$ exhibits $F_{{\mathrm{En}}, 2}$ as the normalization of $X$.
:::

<!-- Source: 1-part-combinatorial/2-chapter-lattice-theory/600-coxeter-vinberg.md -->

### Coxeter-Vinberg Theory {#section-2-6}

#### Cusp Diagrams

Let $T$ be an even nondegenerate lattice of signature $(2,n)$ and $\Gamma \leq \operatorname{O}^*(T)$ a finite index arithmetic subgroup.
As we have seen and will explore in more detail in \Cref{chapter-4}, the quotient $F_\Gamma \mathrel{\mathop:}=  { D_{T} }/{\Gamma} $ admits a Baily--Borel compactification $\overline{F_\Gamma}^{ \operatorname{BB} }$.
The rational boundary components (or **cusps**) of $\partial\overline{F_\Gamma}^{ \operatorname{BB} }$ are indexed by $\Gamma$-orbits of isotropic sublattices of $L$.
In particular, **0-cusps** correspond to orbits of isotropic lines $\eta \subset L$, and **1-cusps** correspond to orbits of isotropic planes $I \subset L$.
We can thus often combinatorially understand a compactification by first constructing the following:

:::{#def:cusp-diagrams-moduli .definition title="{Cusp Diagrams}
"}
Let $X$ be a complex analytic space equipped with a stratification $\partial X = \bigsqcup_{i \geq 0} \partial_i X$ by boundary strata indexed by codimension.
The **cusp diagram** of $X$ is the directed graph whose vertices index the irreducible components of $\partial_i X$, with a directed edge $e_{i \to j}$ corresponding to components $V_i$ and $V_j$ whenever $V_j$ lies in the Zariski closure of $V_i$.
:::

For a given $0$-cusp defined by $I$, the orthogonal complement modulo $I$, which we refer to as the *boundary lattice* $ \overline{T}*{ I } \mathrel{\mathop:}= I^\perp / I$, is an even lattice of signature $(1, n{-}1)$ and admits the structure of a hyperbolic lattice.
By studying reflective subgroups of $\operatorname{O}(T)$, one can determine $1$-cusps adjacent $[I]$ using the Coxeter diagram associated to $W(M)$.
As explained in e.g. (Scattone 1987) and (Sterk 1991), the 1-cusps adjacent to a given $0$-cusp $[I]$ in the Baily--Borel compactification correspond bijectively to $\Gamma$-orbits of isotropic planes $J$ such that $I \subset J$, or equivalently, to the set of **maximal parabolic subdiagrams** of the Coxeter diagram associated to the reflection group of the hyperbolic lattice $M \mathrel{\mathop:}=  I^\perp / I$.
Each such subdiagram determines a codimension-one face of the Coxeter polytope in $\mathbb{H}*M$, and hence a distinct $\Gamma_I$ orbit of a $1$-cusp, where $\Gamma_I$ is the stabilizer of $[I]$ in $\Gamma$.
We use this description in (**AEGS23?**) to determine the boundary stratification of $\overline{F*{{\mathrm{En}}, 2}}$ using semitoroidal data, which in turn comes from Coxeter-theoretic data ranging over the $0$-cusps of $\overline{F*{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$.
We then reduce the analysis of $\partial\overline{F_{{\mathrm{En}}, 2}}$ to a combinatorial study of the poset of elliptic and parabolic subdiagrams of Coxeter diagrams that are "folded" from those of $F_{(2,2,0)}$.
This yields integral affine structures and ultimately dlt models of stable degenerations of Enriques surfaces.

#### Root Systems and Weyl Groups

:::{#def:root-system-k-roots .definition title="{Root System and k-Roots}
"}
Let $L$ be a nondegenerate integranl lattice and let $v\in L$ be a primitive vector.
We recall that the reflection in $v$ is defined by the formula $$
s_v(x) \mathrel{\mathop:}= x - 2{x\cdot v \over v^2}v, \qquad s_v \in \operatorname{O}(L_{\mathbf{Q}})
,$$ which is generally only a rational isometry and not necessarily integral, and only well-defined if $v$ is not isotropic.
We note that a sufficient condition for integrality is that $2(v, L) \subseteq k {\mathbf{Z}}$.
We note that this is precisely the formula for a reflection about the hyperplane $H_v \mathrel{\mathop:}= v^{\perp L}$, which we refer to as the **mirror** or **wall** associated to $v$.
We define the **$k$-Weyl group** $W^k(L)$ as the group of reflections $s_v$ such that $s_v\in \operatorname{O}(L)$ is integral and $v^2 = -k$.
More generally, we define the **full Weyl group** $W(L)$ as $\bigcup_k W^k(L)$, the group generated by integral reflections in vectors of any norm.
We say $v$ is a **$k$-root** if $s_v\in W^k(L)$, and more generally that $v$ is simply a **root** if $s_v\in W(L)$, so its mirror supports a well-defined integral reflection isometry.
For 2-elementary lattices $L$, roots are precisely those vectors $v\in L$ with either $$
v^2 = -2, \qquad  \text{ or }  \qquad v^2=-4,\, \operatorname{div}_L(v) = 2
$$ In light of this, we call roots of norm $\pm 2$ **short roots**, and roots of norm $\pm 4$ **long roots**.
We say $L$ is a **root lattice** if it is generated by a set of roots.
We call any group generated by roots a **reflection group**.
:::

:::{#def:discriminant-locus-chambers .definition title="{Discriminant Locus and Weyl Chambers}
"}
The **discriminant locus** is the union of all mirrors, $$
\Delta(L) \mathrel{\mathop:}=  \bigcup_{v \in \Phi_2(L)} v^{\perp L}
.$$ When $L \hookrightarrow  {L_{\mathrm{K3}}} $ is a primitively embedded lattice corresponding to a polarization $h$ on a K3 surface $X$, this locus corresponds to points in the corresponding period domain $D_{T}$ where $X$ acquires extra algebraic cycles -- if identifying the holomorphic 2-form $\omega$ on $X$ with its period point in $D_{L}$, the condition that $\omega$ on a mirror $H_\alpha$ is precisely that $\omega\cdot\alpha = 0$, so $\alpha \in \omega^{\perp H^2(X; {\mathbf{C}})}$ and thus $\omega\in H^{1,1,}(X)$, which by the Lefschetz $(1,1)$-theorem for $(-2)$-curves on K3 surfaces makes $\alpha$ a Hodge class.
The **Weyl chambers** are the connected components of $C_L^{\circ} \mathrel{\mathop:}=  C_L \setminus \Delta(L)$ where $C_L$ is the cone of positive-norm vectors in $L$.
A **simple system** is a set of roots $v$ such that the mirrors $H_v$ form the bounding hyperplanes for a fundamental domain for the action of $W(L)$ on $L$.
:::

#### Coxeter Groups and Polytopes

A **Coxeter group** is a group $S$ with presentation $$ S = \left\langle s_1,\cdots, s_n {~~\mathrel{\Big\vert}~~} s_i^2 = (s_i s_j)^{m_{ij}} = e  \right\rangle, \qquad m_{ii} = 1 \,\,\forall i, m_{ij} = m_{ji} \geq 2\,\,\forall i\neq j .$$ The **Coxeter diagram** $G_S$ of $S$ is a labeled graph whose vertices correspond to generators $s_i$, with edges between $s_i$ and $s_j$ for $i < j$ and $m_{ij} \geq 3$.
We label the edges with $m_{ij}$ when $m_{ij} \geq 3$.
A general Coxeter group $S$ encodes a bounding set of hyperplanes for a polytope $P_S$ in a space $X = {\mathbb{E}}^n, S^n$, or $\mathbb{H}^n$, where ${\mathbb{E}}^n$ is the standard Euclidean space, $S^n$ is the sphere, and $\mathbb{H}^n$ is hyperbolic $n$-space.
The elements $s_i\in S$ encode reflections about hyperplanes $H_i$, and the corders $m_{ij}$ encode the dihedral angles between $H_i$ and $H_j$.
The reflections $H_i$ generate a reflection group $W_S$, and $P_S$ is a fundamental domain for the action of $W_S$ on $X$.

Let $P$ be a polytope in a space $X = {\mathbb{E}}^n, S^n$, or $\mathbb{H}^n$ with finitely many faces.
We say $P$ is a **Coxeter polytope** if the following hold:

1. Each face of $P$ lies in a hyperplane $H_i$ that is the orthogonal complement of a vector $\alpha_i$,

2. The dihedral angles between adjacent faces are of the form $\pi/m_{ij}$ for positive integers $m_{ij}\geq 1$, and

3. The reflection group $W = \left\langle s_{\alpha_i} \right\rangle$ generated by reflections about the faces of $P$ acts properly discontinuously on $X$ with fundamental domain $P$.

We often identify a Coxeter polytope $P$ with a a minimal set of bounding hyperplanes $\left\{{H_i}\right\}$ such that $P$ is the intersection of the positive half-spaces of all of the $H_i$.
We say $P$ is **Euclidean**, **spherical**, or **hyperbolic** according to whether $X = {\mathbb{E}}^n, S^n$, or $\mathbb{H}^n$ respectively.

#### Hyperbolic Lattices and Polytopes

Let $C_L$ be the cone of positive norm vectors in $L_{\mathbf{R}}$, i.e. $C_L\mathrel{\mathop:}= \left\{{v\in L_{\mathbf{R}} {~~\mathrel{\Big\vert}~~} v^2 > 0}\right\}$.
There is a decomposition $C_L = C_L^+ \amalg C_L^-$, where $$ C_L^+ \mathrel{\mathop:}=  \{v \in C_L {~~\mathrel{\Big\vert}~~} v_0 > 0\}, \qquad C_L^- \mathrel{\mathop:}=  \{v \in C_L {~~\mathrel{\Big\vert}~~} v_0 < 0\} .$$ Recall that a lattice $L$ is called **hyperbolic** or **Lorentzian** if it is nondegenerate and has signature $(1, n+1)$ for $n \geq 1$, following the standard algebro-geometric convention.
The standard example is the hyperbolic lattice $U$.
The intersection pairing on $L$ induces a hyperbolic metric $\rho(v,w) \mathrel{\mathop:}=  \operatorname{arccosh}(v\cdot w)$ on $L_{\mathbf{R}}$.
The group of orientation-preserving isometries of $\mathbb{H}^n_L$ is: $$ \operatorname{Isom}^+(\mathbb{H}^n_L) \cong \operatorname{O}^*(L_{\mathbf{R}}) \mathrel{\mathop:}=  \operatorname{Stab}*{\operatorname{O}(L*{\mathbf{R}})}(C_L^+), $$ Moreover, the associated hyperbolic space $\mathbb{H}_L^n$ admits several standard models:

- The **unit hyperboloid model**: $$ \mathbb{H}^n_L \mathrel{\mathop:}=  \{ v \in L_{{\mathbf{R}}} {~~\mathrel{\Big\vert}~~} v^2 = 1,\, v \in C_L^+ \}, ,$$

- The **projective or Klein model**: $$ \operatorname{BB}*L^n \mathrel{\mathop:}=  {\mathbf{P}}(C_L ) \subset {\mathbf{P}}(L*{\mathbf{R}}), .$$

For a hyperbolic lattice $L$, consider the Poincaré ball model $\operatorname{BB}_L^n$.
For vectors $v, w \in L$ and their associated hyperplanes $H_v \mathrel{\mathop:}=  v^{\perp}$ and $H_w \mathrel{\mathop:}=  w^{\perp}$, the dihedral angle between these hyperplanes is determined by $vw$.
When $|vw| < 1$, the hyperplanes intersect in the interior of the ball and satisfy $-vw = \cos(\angle(H_v, H_w))$ where $\angle(H_v, H_w)$ denotes the dihedral angle.
When $|vw| = 1$, the hyperplanes are *asymptotically parallel*, meeting at an *ideal point* in $\partial \mathbb{H}^n$.
When $|vw| > 1$, the hyperplanes are *ultra-parallel* and satisfy $-vw = \cosh(\rho(H_v, H_w))$ where $\rho(H_v, H_w)$ denotes the hyperbolic distance between them.

#### Coxeter-Vinberg Diagrams

Let $v \in L$ be a simple root, the the reflection $s_v$ is in $\operatorname{O}(L)$ precisely when $2(v, L)/v^2 \subseteq {\mathbf{Z}}$.
Thus if $L$ is 2-elementary, the roots of $L$ are primitive vectors $v \in L$ such that either $v^2 = -2$, or $v^2 = -4$ and $\operatorname{div}*L(v) = 2$.
The mirrors $H_v \mathrel{\mathop:}=  v^\perp \subset L*{\mathbf{R}}$ for $v \in \Phi(L)$ define a hyperplane arrangement.
The intersection of the positive cone $C_L^+$ with the complement of all mirrors, $$ C_L^\circ \mathrel{\mathop:}=  C_L^+ \setminus \bigcup_{v \in \Phi(L)} H_v, $$ decomposes into connected components called **Weyl chambers**, each of which is a fundamental domain $P$ for the action of the Weyl group $W(L)$ on $C_L^+$.
This is a hyperbolic Coxeter polytope, and thus the Gram matrix corresponding to its walls encodes a Coxeter diagram.
Let $P$ by a hyperbolic Coxeter polytope arising from a root system in $L$ as above.
Its **Coxeter diagram** is the colored undirected graph whose vertices correspond tosimple roots $r_i$ with $r_i^2 < 0$ and whose edges $e_{i,j}$ encode the angle $\angle(H_i, H_j)$ between $H_i \mathrel{\mathop:}= r_i^{\perp}$ and $H_j \mathrel{\mathop:}= r_j^{\perp}$ by the formula $$ g_{i,j} \mathrel{\mathop:}= { r_i \cdot r_j \over \sqrt{ r_i^2 r_j^2} } = \cos\left( {\pi \over m_{ij}} \right) .$$ We let $e_{i. j}$ be

- an omitted edge if $m_{i, j} \leq 2$,
- a multiple edge if $3 \leq m_{i, j} < \infty$, so $H_i \cap H_j$ is in the interior of $\mathbb{H}^n$ and $g_{i,j} < 1$,
- a thick/bold edge if $H_i \cap H_j \in \partial \mathbb{H}^n$ and $g_{i,j} = 1$,
- dotted edge if the $H_i, H_j$ do not intersect in the closure $\overline{\mathbb{H}^n}$ and $g_{i, j} > 1$.

In the 2-elementary setting, we additionally assign white vertices to $\Phi^2$ and black vertices to $\Phi^4$.
We refer to (Vinberg 1972, 1975) for thorough treatments.

#### Elliptic/Parabolic Subdiagrams

Let $G$ be the Coxeter diagram, for example corresponding to a Coxeter group or a Coxeter polytope arising from a reflection group.
A subdiagram $D \subset G$ is called **elliptic** if the Gram matrix $(v_i \cdot v_j)$ is positive definite.
Such a subdiagram defines a finite face of the Coxeter polytope.
A subdiagram is **parabolic** if the Gram matrix is positive semidefinite of corank one, but not contained in any strictly larger elliptic subdiagram.
A parabolic subdiagram $D \subset G$ is **maximal** if it is not properly contained in a larger parabolic subdiagram.
Such diagrams correspond bijectively to rank-$2$ isotropic subspaces $J \subset L$ with $I \subset J$, i.e., to $1$-cusps adjacent to $[I]$, modulo $\Gamma$.
The set of maximal parabolic subdiagrams of $G$ thus indexes the $1$-cusps contained in the closure of the $0$-cusp corresponding to $[I]$.
The incidence relations among boundary strata follow from containments among these diagrams.

#### Computing Cusps

Putting this together, we thus obtain a general, effective method for indexing rational boundary components for both the Baily--Borel and semitoroidal compactifications of modular varieties $ { D }/{ \Gamma } $ of orthogonal type corresponding to lattices $T$ of signature $(2, n)$:

1. Compute the 0-cusps of $ { D }/{ \Gamma } $ by any means possible, yielding (orbits of) primitive isotropic vectors $\eta_i \in T$.

2. For each $i$, compute the lattice $ \overline{T}\_{ \eta } \mathrel{\mathop:}= \eta_i^{\perp T}$, which is of signature $(1, n-1)$ and thus hyperbolic.

3. Compute the "minimal stabilizing" subgroup $\Gamma_{\eta_i}$ of $\eta_i$ in $\Gamma$ determined by the exact sequence $$ 1\to U_{\eta_i} \to \operatorname{Stab}*{\Gamma}(\eta_i) \to \Gamma*{\eta_i} \to 1 ,$$ where $U_{\eta_i}$ is the (maximal) unipotent subgroup acting trivially on $ \overline{T}\_{ \eta } $.

4. Compute the reflection subgroups $W(\Gamma_{\eta_i})$, which are Coxeter groups with Coxeter-Vinberg diagrams $G( \overline{T}_{ \eta  } )$.

5. Enumerate orbits of maximal elliptic and parabolic subdiagrams of $G( \overline{T}*{ \eta  } )$ under diagram automorphisms to determine the the face poset of the Coxeter polytope $P( \overline{T}*{ \eta  } )$, which corresponds bijectively to the incidence poset of $\partial\overline{ { D }/{ \Gamma } }^{ \operatorname{BB} }$.

Toward carring out the program proposed above, let $\Gamma \subset \operatorname{O}(L)$ be an arithmetic reflection subgroup generated by reflections in simple roots.
The following algorithm due to (Vinberg 1975) constructs a fundamental chamber $P \subset \mathbb{H}^n$:

1. **Choice of control vector**:\
   Start with a generic positive-norm rational vector $v_0 \in C_L^+$, the **control vector**. The algorithm will construct the walls of the chamber $P$ of $W(L)$ containing $v_0$.
   Write $\tilde P$ for the cone formed by the intersection of the positive half-spaces of all currently obtained walls.

2. **Enumerating roots**:\
   Enumerate the set of all primitive vectors $v \in L$ such that $v^2 < 0$, $s_v\in \Gamma$, and the hyperplane $H_v$ intersects $\tilde P$, to define a face of $P$ containing $v_0$.
   These vectors will define the simple roots of $L$.

3. **Ordering/pruning**:\
   List the simple roots in order of increasing *height* $h(v) \mathrel{\mathop:}= -2(v_0\cdot v)/v^2$.
   For each candidate simple root $v$, check whether the associated reflection $s_v$ defines a new bounding wall of $P$, i.e., whether $H_v$ intersects $\tilde P$ transversely.

4. **Constructing the diagram**:\
   Whenever $\tilde P$ becomes a convex polytope, the Gram matrix $(v_i \cdot v_j)$ determines the angles between faces and the Coxeter diagram of $P$.

The fundamental polytope $P \subset \mathbb{H}^{n-1}_M$ constructed via Vinberg's algorithm is a rational polyhedral cone, possibly with compact and ideal faces.
The algorithm terminates if and only if $\Gamma$ has finite covolume.
This is not typically easy to determine a priori, and so it is difficult to tell if or when the algorithm terminates.
For lattices of high rank, the search space grows extremely quickly, making this an ineffective strategy if applied naively.
In practice, one often leverages specific properties of a given lattice to more intelligently enumerate the search space.

<!-- Source: 1-part-combinatorial/2-chapter-lattice-theory/700-folding.md -->

### Lattice Folding

#### Examples and Conventions around Dynkin Diagrams

We quickly recall constructions of root systems of small rank, which easily generalize to larger rank but allow for explicit calculations.
For each such lattice $L$, we recall the classical embeddings $L\hookrightarrow {\mathbb{E}}_L$ into Euclidean spaces, describe the simple roots $\Phi(L) = \{\alpha_i\}$ in coordinates in ${\mathbb{E}}_L$ and the Gram matrix $G_L$ for $\Phi(L)$ in terms of the $\alpha_i$ by carrying out computations using Euclidean coordinates within ${\mathbb{E}}_L$.
For this section, we explicitly write root lattices in the **positive-definite** convention, since we are working with roots in ${\mathbb{E}}_L$ directly.
For the remainder of this work, we implicitly take the negative-definite variants; although this can create confusion, but makes the computations easily verifiable using linear algebra and the standard positive-definite Euclidean pairing on ${\mathbf{Z}}^n$.
Thus throughout this section,if $R$ is a root-lattice, it is assumed to be positive-definite, with negative-definite twist $R(-1)$.
For explicit conventions, we refer to \Cref{section-root-lattice-conventions}.

#### Invariant and Coinvariant Sublattices

Let $L$ be an even nondegenerate lattice containing a root system $\Phi \subset L$, and let $G \subset \operatorname{O}(L)$ be a finite group of isometries preserving $\Phi$ and let $L^G, L_G$ be the invariant and coinvariant sublattices respectively.
Both are primitive and orthogonal in $L$.
Suppose $G = \langle I \rangle \cong {\mathbf{Z}}/2{\mathbf{Z}}$ is generated by an involution $I$.
Each $v \in L$ then decomposes orthogonally, up to a factor of 2, as: $$ 2\cdot v = v*+ + v*-, \qquad v*+ = v + I(v) \in L^G,\quad v*- = v - I(v) \in L_G.

$$

#### Folded Root Systems
Given a simple root $\alpha_i \in \Phi \subseteq L$, let $[\alpha_i] \subset \Phi$ denote its $G$-orbit. The associated **folded root** and **folded root system** are defined by
$$
\beta_{[\alpha_i]} \mathrel{\mathop:}= \sum_{\alpha_j \in [\alpha_i]} \alpha_j \in L^G, \quad \Phi^G \mathrel{\mathop:}=  \left\{\beta_{[\alpha_i]} \in L^G\ {~~\mathrel{\Big\vert}~~}\ [\alpha_i] \in \Phi/G \right\}. $$ Each folded root, corresponding to a folded node in the corresponding Dynkin diagram, thus corresponds to a $G$-orbit of roots in the ambient lattice $L$.
For involutions, this simplifies to $$ \beta_{[\alpha_i]} \mathrel{\mathop:}= \alpha_i + I(\alpha_i) \in L^G. $$ If $I$ fixes $\alpha_i$, then $\beta_{[\alpha_i]} = 2\alpha_i$; otherwise, $\beta_{[\alpha_i]}$ has a different norm, thereby affecting the multiplicity of edges in the corresponding Dynkin diagram.

#### Examples of Classical Foldings

The process of folding nontrivial diagram automorphisms produces non-simply-laced root systems from simply-laced diagrams; the key condition is that roots in the same orbit under the folding group must be orthogonal for a valid quotient.
We note that this is easy to check at the level of diagrams -- noting that folding takes place at the level of lattices, i.e. computing $\Phi(L^G)$, such an automorphism group $G$ can arise from any representation $G\to \operatorname{Sym}(G_{\Phi(L)})$ on the Coxeter diagram of $\Phi(L)$.
This uses the fact that for the lattices $T$ that occur in our study, there is a decmoposition $\operatorname{O}(L) \cong W(L) \rtimes P$ where $P\leq \operatorname{Sym}(G_{\Phi(L)})$ is some subgroup of diagram symmetries, which are simply graph isomorphisms that preserve vertex and edge weights.
In good cases, $P$ is the entire automorphism group, and so any representation $G\to \operatorname{Sym}(G_{\Phi(L)})$ can be lifted along the inclusion $P\hookrightarrow\operatorname{O}(L)$ to obtain a representation $G\to \operatorname{O}(L)$, allowing one to apply the folding theory described above.
In particular, this property holds for the classical root lattices, and we can thus construct foldings by selecting subgroups $G$ of automorphisms of their Coxeter-Dynking diagrams.
Classical examples in the context of semisimple Lie algebras include:

Folding              Symmetry Group   Mechanism
* * *
$A_{2n-1} \to C_n$   $S_2$            Horizontal reflection $D_{n+1} \to B_n$    $S_2$            Vertical reflection $D_4 \to G_2$        $S_3$            Rotation by $2\pi /3$ $E_6 \to F_4$        $S_2$            Horizontal reflection

: Foldings of simply-laced Dynkin diagrams

In the study of $F_{{\mathrm{En}}, 2}$, the folding procedure must be carried out more carefully at the level of lattices, explicitly tracking the explicit twists that folding introduces, along with other parity-related data necessary for distinguishing irreducible components of the associated KSBA stable models, which we describe in the section on ADE surfaces.
In order to make this theory concrete, we now show how to explicitly carry out the types of folding calculations that occur for $F_{{\mathrm{En}}, 2}$, as well as for some of the exceptional types that do not occur in this specific case, noting the slightly new features that arise (like tracking twists) arise, causing some slight differences in conventions from the presentations of folding given in classical literature.

\newcommand{\dynkinscale}{4.0} \newcommand{\labeldistance}{8pt}
\begin{center}
\begin{tikzpicture}
  % Grid 1 - Top Left Quadrant
  \begin{scope}[shift={(0,10)}]
    % A3
    \begin{scope}[shift={(0,4)}]
      \dynkin[scale=\dynkinscale, involutions={13}, involution/.style={blue, dashed, stealth-stealth, thick, shorten <=8pt, shorten >=8pt}, mark=o, labels*={1,2,3}, label macro*/.code={\alpha_{#1}}, label distance=\labeldistance, text style/.style={scale=1.1}]A3
      \node at (-0.3,0) {\Large $A_3$};
    \end{scope}

    % D4 (first variant)
    \begin{scope}[shift={(6,4)}]
      \dynkin[scale=\dynkinscale, involutions={43}, involution/.style={blue, dashed, stealth-stealth, thick, shorten <=8pt, shorten >=8pt}, mark=o, labels={\alpha_1,\alpha_2,\alpha_3,\alpha_4}, label directions={above,above left,above right,below right,}, label distance=4pt, text style/.style={scale=1.1}]D4
      \node at (-0.3,0) {\Large $D_4$};
    \end{scope}

    % Arrows
    \draw[-{Stealth[scale=1.5]}, dashed, thick] (1.4,3) -- (1.4,0.5);
    \draw[-{Stealth[scale=1.5]}, dashed, thick] (7.4,3) -- (7.4,0.5);

    % C2
    \begin{scope}[shift={(0,0)}]
      \dynkin[arrows=false, scale=\dynkinscale, mark=*, label, label macro/.code={\beta_{[\alpha_{#1}]}}, label distance=8pt, text style/.style={scale=1.3}] C{o*}
      \node at (-0.3,0) {\Large $C_2$};
    \end{scope}

    % B3
    \begin{scope}[shift={(6,0)}]
      \dynkin[arrows=false, scale=\dynkinscale, mark=*, label, label macro/.code={\beta_{[\alpha_{#1}]}}, label distance=8pt, text style/.style={scale=1.1}] B{oo*}
      \node at (-0.3,0) {\Large $B_3$};
    \end{scope}

    % Grid label
  \end{scope}

  % Grid 2 - Bottom Left Quadrant
  \begin{scope}[shift={(0,0)}]
    % D4 (second variant)
    \begin{scope}[shift={(0,4)}]
      \dynkin[scale=\dynkinscale, involutions={[out=-30,in=-150,relative, -stealth]14;[out=30,in=150,stealth-,relative]13;[out=60, in=120,stealth-,relative]34}, involution/.style={blue, dashed, stealth-, thick, shorten <=8pt, shorten >=8pt}, mark=o, labels={\alpha_1,\alpha_2,\alpha_3,\alpha_4}, label directions={left,above left,above right,below right,}, label distance=8pt, text style/.style={scale=1}]D4
      \node at (-0.3,0) {\Large $D_4$};
    \end{scope}

    % E6
    \begin{scope}[shift={(6,4)}]
      \dynkin[scale=\dynkinscale, involutions={[out=-60,in=-120,relative]16;[out=-70,in=-110,relative]35}, involution/.style={blue, dashed, stealth-stealth, thick, shorten <=8pt, shorten >=8pt}, mark=o, labels={\alpha_1,\alpha_2,\alpha_3,\alpha_4,\alpha_5,\alpha_6}, label directions={above,above,above,below,above,above}, label distance=8pt, text style/.style={scale=1.1}]E6
      \node at (-0.3,0) {\Large $E_6$};
    \end{scope}

    % Arrows
    \draw[-{Stealth[scale=1.5]}, dashed, thick] (1.4,3) -- (1.4,0.5);
    \draw[-{Stealth[scale=1.5]}, dashed, thick] (8.75,3) -- (8.75,0.5);

    % G2
    \begin{scope}[shift={(0,0)}]
      \dynkin[arrows=false, scale=\dynkinscale, mark=*, label, label macro/.code={\beta_{[\alpha_{#1}]}}, label distance=8pt, text style/.style={scale=1.1}] G{*o}
      \node at (-0.3,0) {\Large $G_2$};
    \end{scope}

    % F4
    \begin{scope}[shift={(6,0)}]
      \dynkin[arrows=false, scale=\dynkinscale, mark=*, label, label macro/.code={\beta_{[\alpha_{#1}]}}, label distance=8pt, text style/.style={scale=1.1}] F{oo**}
      \node at (-0.3,0) {\Large $F_4$};
    \end{scope}

    % Grid label
  \end{scope}

\end{tikzpicture}
\end{center}

##### Case 1: $A_5 \to C_3(2)$ (Horizontal Reflection, $G = S_2$)

Let $L = A_5$, where we recall the simple roots and Gram matrix: $$ \Phi(A_5)\colon\,\,
\begin{cases}
\alpha_1 = e_1 - e_2 \\
\alpha_2 = e_2 - e_3 \\
\alpha_3 = e_3 - e_4 \\
\alpha_4 = e_4 - e_5 \\
\alpha_5 = e_5 - e_6
\end{cases}
,\quad G_{A_5} =
\begin{pmatrix}
2 & -1 &  0 &  0 &  0 \\
-1 & 2 & -1 &  0 &  0 \\
0 & -1 & 2 & -1 &  0 \\
0 &  0 & -1 & 2 & -1 \\
0 &  0 &  0 & -1 & 2
\end{pmatrix}
$$

Define $G = \langle I \rangle \cong S_2$ by
$$
I\colon
\begin{cases}
\alpha_1 \mapsto \alpha_5 \\
\alpha_2 \mapsto \alpha_4 \\
\alpha_3 \mapsto \alpha_3 \\
\alpha_4 \mapsto \alpha_2 \\
\alpha_5 \mapsto \alpha_1,
\end{cases}
\implies I =
\begin{pmatrix}
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 0
\end{pmatrix}
$$
The invariant sublattice is
$$
A_5^G \cong \{ (x_1, x_2, x_3, x_3, x_2, x_1) \in {\mathbf{Z}}^6 : x_1 + x_2 + x_3 + x_3 + x_2 + x_1 = 0 \}

$$

with orbits
$$

G \cdot \alpha*i:
\begin{cases}
G \cdot \alpha_1 = \{\alpha_1, \alpha_5\} \\
G \cdot \alpha_2 = \{\alpha_2, \alpha_4\} \\
G \cdot \alpha_3 = \{\alpha_3\}
\end{cases}
\implies \Phi(A_5^G)\colon
\begin{cases}
\beta*{[\alpha_1]} = \alpha*1 + \alpha_5 = e_1 - e_2 + e_5 - e_6 \\
\beta*{[\alpha_2]} = \alpha*2 + \alpha_4 = e_2 - e_3 + e_4 - e_5 \\
\beta*{[\alpha_3]} = \alpha*3 = e_3 - e_4,
\end{cases}
$$ and thus $$ G*{\Phi(A*5^G)} =
\begin{pmatrix}
4 & -2 & 0 \\
-2 & 4 & -2 \\
0 & -2 & 2
\end{pmatrix}
\sim G*{C_3(2)} = 2\cdot
\begin{pmatrix}
2 & -1 & 0 \\
-1 & 2 & -1 \\
0 & -1 & 1
\end{pmatrix}
$$ which is the Gram matrix for $C_3$ up to uniform scaling, so $\Phi(A_5^G) \cong \Phi(C_3)$.
One can see the equivalence of these root systems by noting that the Coxeter diagrams are isomorphic as weighted graphs with weighted nodes:

\begin{center}
\begin{tikzpicture}

% Left half: A5^G
\begin{scope}[shift={(0,0)}]
\node[circle, draw, fill=blue!30, minimum size=8mm] (n0) at (0.00, 0.00) {};
\node at (0.00, 0.80) {$\beta_{ [\alpha_1] }^2 = 4$};
\node[circle, draw, fill=blue!30, minimum size=8mm] (n1) at (2.00, 0.00) {};
\node at (2.00, 0.80) {$\beta_{ [\alpha_2] }^2 = 4$};
\node[circle, draw, fill=white, minimum size=8mm] (n2) at (4.00, 0.00) {};
\node at (4.00, 0.80) {$\beta_{ [\alpha_3] }^2 = 2$};
\draw (n0) -- (n1);
\draw[transform canvas={yshift=1.5pt}] (n0) -- (n1);
\node at ($(n0)!0.5!(n1)$) [above=0.2cm] {4};
\draw (n1) -- (n2);
\draw[transform canvas={yshift=1.5pt}] (n1) -- (n2);
\node at ($(n1)!0.5!(n2)$) [above=0.2cm] {4};
\node at (2.00, 2.0) {\Large \textbf{$A_5^G$}};
\end{scope}

% Right half
\begin{scope}[shift={(8,0)}]
% Top: C3
\begin{scope}[shift={(0,2.5)}]
\node[circle, draw, fill=white, minimum size=8mm] (m0) at (0.00, 0.00) {};
\node at (0.00, 0.80) {$\alpha_{1}^2 = 2$};
\node[circle, draw, fill=white, minimum size=8mm] (m1) at (2.00, 0.00) {};
\node at (2.00, 0.80) {$\alpha_{2}^2 = 2$};
\node[circle, draw, fill=red!30, minimum size=8mm] (m2) at (4.00, 0.00) {};
\node at (4.00, 0.80) {$\alpha_{3}^2 = 1$};
\draw (m0) -- (m1) node[midway, above] {3};
\draw (m1) -- (m2) node[midway, above] {3};
\node at (2.00, 2.0) {\Large \textbf{$C_3$}};
\end{scope}

% Bottom: C3(2)
\begin{scope}[shift={(0,-2.5)}]
\node[circle, draw, fill=blue!30, minimum size=8mm] (p0) at (0.00, 0.00) {};
\node at (0.00, 0.80) {$\alpha_{1}^2 = 4$};
\node[circle, draw, fill=blue!30, minimum size=8mm] (p1) at (2.00, 0.00) {};
\node at (2.00, 0.80) {$\alpha_{2}^2 = 4$};
\node[circle, draw, fill=white, minimum size=8mm] (p2) at (4.00, 0.00) {};
\node at (4.00, 0.80) {$\alpha_{3}^2 = 2$};
\draw (p0) -- (p1);
\draw[transform canvas={yshift=1.5pt}] (p0) -- (p1);
\node at ($(p0)!0.5!(p1)$) [above=0.2cm] {4};
\draw (p1) -- (p2);
\draw[transform canvas={yshift=1.5pt}] (p1) -- (p2);
\node at ($(p1)!0.5!(p2)$) [above=0.2cm] {4};
\node at (2.00, 2.0) {\Large \textbf{$C_3(2)$}};
\end{scope}
\end{scope}

\end{tikzpicture}
\end{center}

##### Case 2: $D_4 \to C_3$ (Vertical Reflection, $G=S_2$)

Let $L = D_4$, with simple roots and Gram matrix: $$ \Phi(D_4) =
\begin{cases}
\alpha_1 &= e_1 - e_2 \\
\alpha_2 &= e_2 - e_3 \\
\alpha_3 &= e_3 - e_4 \\
\alpha_4 &= e_3 + e_4
\end{cases},\quad
G_{D_4} =
\begin{pmatrix}
2 & -1 & 0 & 0 \\
-1 & 2 & -1 & -1 \\
0 & -1 & 2 & 0 \\
0 & -1 & 0 & 2
\end{pmatrix}
$$ and $$
I\colon
\begin{cases}
\alpha_1 \mapsto \alpha_1 \\
\alpha_2 \mapsto \alpha_2 \\
\alpha_3 \mapsto \alpha_4 \\
\alpha_4 \mapsto \alpha_3,
\end{cases}
\implies I = \begin{pmatrix} 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 \end{pmatrix}

$$

The invariant sublattice is
$$

D*4^G \cong \{ (x_1, x_2, x_3, 0) \in {\mathbf{Z}}^4 : x_1 + x_2 + x_3 \in 2{\mathbf{Z}} \} $$ with orbits and folded root system $$ G \cdot \alpha_i:
\begin{cases}
G \cdot \alpha_1 = \{\alpha_1\} \\
G \cdot \alpha_2 = \{\alpha_2\} \\
G \cdot \alpha_3 = \{\alpha_3, \alpha_4\},
\end{cases}
\implies \Phi(D_4^G)\colon
\begin{cases}
\beta*{[\alpha_1]} = \alpha*1 = e_1 - e_2 \\
\beta*{[\alpha_2]} = \alpha*2 = e_2 - e_3 \\
\beta*{[\alpha_3]} = \alpha_3 + \alpha_4 = 2e_3
\end{cases}

$$

The Gram matrix is
$$

G*{\Phi(D_4^G)} =
\begin{pmatrix}
2 & -1 & 0 \\
-1 & 2 & -2 \\
0 & -2 & 4
\end{pmatrix} =
G*{C_3} =
\begin{pmatrix}
2 & -1 & 0 \\
-1 & 2 & -2 \\
0 & -2 & 4
\end{pmatrix}
,$$ which is precisely the Gram matrix for $C_3$, so $\Phi(D_4^G) \cong \Phi(C_3)$.
One can again see the equivalence by noting the isomorphism of Coxeter diagrams:

\begin{center}
\begin{tikzpicture}

% First diagram: D4^G
\begin{scope}[shift={(0,0)}]
\node[circle, draw, fill=white, minimum size=8mm] (n0) at (0.00, 0.00) {};
\node at (0.00, 0.80) {$\beta_{[\alpha_1]}^2=2$};
\node[circle, draw, fill=white, minimum size=8mm] (n1) at (2.00, 0.00) {};
\node at (2.00, 0.80) {$ \beta*{[\alpha_2]}^2 = 2$};
\node[circle, draw, fill=blue!30, minimum size=8mm] (n2) at (4.00, 0.00) {};
\node at (4.00, 0.80) {$\beta*{[\alpha_3]}^2 = 4$};
\draw (n0) -- (n1) node[midway, above] {3};
\draw (n1) -- (n2);
\draw[transform canvas={yshift=1.5pt}] (n1) -- (n2);
\node at ($(n1)!0.5!(n2)$) [above=0.2cm] {4};
\node at (2.00, 2.0) {\Large \textbf{$D_4^G$}};
\end{scope}

% Second diagram: C3
\begin{scope}[shift={(6,0)}]
\node[circle, draw, fill=white, minimum size=8mm] (m0) at (0.00, 0.00) {};
\node at (0.00, 0.80) {$\alpha_{1}^2 = 2$};
\node[circle, draw, fill=white, minimum size=8mm] (m1) at (2.00, 0.00) {};
\node at (2.00, 0.80) {$\alpha_{2}^2 = 2$};
\node[circle, draw, fill=blue!30, minimum size=8mm] (m2) at (4.00, 0.00) {};
\node at (4.00, 0.80) {$\alpha_{3}^2 = 4$};
\draw (m0) -- (m1) node[midway, above] {3};
\draw (m1) -- (m2);
\draw[transform canvas={yshift=1.5pt}] (m1) -- (m2);
\node at ($(m1)!0.5!(m2)$) [above=0.2cm] {4};
\node at (2.00, 2.0) {\Large \textbf{$C_3$}};
\end{scope}

\end{tikzpicture}
\end{center}

##### Case 3: $D_4 \to G_2$ (Rotation by $2\pi/3$, $G = {\mathbf{Z}}/3{\mathbf{Z}}$)

Let $L = D_4$ with $\sigma$ acting by $$ \sigma\colon
\begin{cases}
\alpha_1 \mapsto \alpha_3 \\
\alpha_3 \mapsto \alpha_4 \\
\alpha_4 \mapsto \alpha_1 \\
\alpha_2 \mapsto \alpha_2
\end{cases}
\text{ with orbits } G \cdot \alpha_i :
\begin{cases}
G \cdot \alpha_2 = \{\alpha_2\} \\
G \cdot \alpha_1 = \{\alpha_1, \alpha_3, \alpha_4\}.
\end{cases}
$$ Then $$ \Phi(D_4^G)\colon
\begin{cases}
\beta_{[\alpha_1]} = \alpha_1 + \alpha_3 + \alpha_4 = e_1 - e_2 + 2e_3 \\
\beta_{[\alpha_2]} = \alpha_2 = e_2 - e_3
\end{cases}
\implies G_{\Phi(D_4^G)} =
\begin{pmatrix}
2 & -3 \\
-3 & 6
\end{pmatrix} = G_{\Phi(G_2)},
$$ yielding the isometry $\Phi(D_4^G)\cong \Phi(G_2)$ on the nose.

##### Case 4: $E_6 \to F_4$ (Horizontal Reflection, $G=S_2$)

We take the simple roots [
\begin{cases}
\alpha_1 = e_2 - e_3 \\
\alpha_2 = e_3 - e_4 \\
\alpha_3 = e_4 \\
\alpha_4 = {1\over 2}(e_1 - e_2 - e_3 - e_4),
\end{cases}
\qquad
G\_{F_4} =
\begin{pmatrix}
2 & -1 & 0 & 0 \\
-1 & 2 & -1 & 0 \\
0 & -1 & 1 & -{1\over 2} \\
0 & 0 & -{1\over 2} & 1
\end{pmatrix}

] and for $E_6$, we fix a basis in the Bourbaki convention, $$
\begin{cases}
\alpha_1 = {1\over 2}(e_1 - e_2 - e_3 - e_4 - e_5 - e_6 - e_7 + e_8) \\
\alpha_2 = e_1 + e_2 \\
\alpha_3 = -e_1 + e_2 \\
\alpha_4 = -e_2 + e_3 \\
\alpha_5 = -e_3 + e_4 \\
\alpha_6 = -e_4 + e_5,
\end{cases}
G_{E_6} =
\begin{pmatrix}
  2 &  0 & -1 &  0 &  0 &  0 \\
  0 &  2 &  0 & -1 &  0 &  0 \\
 -1 &  0 &  2 & -1 &  0 &  0 \\
  0 & -1 & -1 &  2 & -1 &  0 \\
  0 &  0 &  0 & -1 &  2 & -1 \\
  0 &  0 &  0 &  0 & -1 &  2
\end{pmatrix}
$$ Writing the folding involution yields $$ I\colon
\begin{cases}
\alpha_1 \leftrightarrow \alpha_6 \\
\alpha_3 \leftrightarrow \alpha_5\\
\alpha_2\mapsto\alpha_2\\
\alpha_4\mapsto\alpha_4
\end{cases} \quad \implies
I =
\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
.$$ Taking orbits, $$
G \cdot \alpha_i :
\begin{cases}
G \cdot \alpha_1 = \{\alpha_1,\alpha_6\} \\
G \cdot \alpha_2 = \{\alpha_2\} \\
G \cdot \alpha_3 = \{\alpha_3, \alpha_5\} \\
G \cdot \alpha_4 = \{\alpha_4\}
\end{cases} \implies
\Phi(E_6^G)\colon
\begin{cases}
\beta_{[\alpha_1]} = \alpha_1 + \alpha_6 \\
\beta_{[\alpha_2]} = \alpha_2 \\
\beta_{[\alpha_3]} = \alpha_3 + \alpha_5 \\
\beta_{[\alpha_4]} = \alpha_4
\end{cases}
$$ and thus $$ G_{\Phi(E_6^G)} =
\begin{pmatrix}
4 & 0 & -2 & 0 \\
0 & 2 & 0 & -1 \\
-2 & 0 & 4 & -2 \\
0 & -1 & -2 & 2
\end{pmatrix}
\sim G_{F_4(2)} =
\begin{pmatrix}
2 & -1 & 0 & 0 \\
-1 & 2 & -1 & 0 \\
0 & -1 & 1 & -{1\over 2} \\
0 & 0 & -{1\over 2} & 1
\end{pmatrix}
,$$ which coincide after applying the permutation $(1,3,4,2)$ to the $\beta_{[\alpha_i]}$, so $\Phi(E_6^G) \cong \Phi(F_4(2))$.
One can also additionally check that the computed Coxeter diagrams are isomorphic, or equivalently that the associated Cartan matrices are similar via a permutation matrix.

### Applications to $F_{{\mathrm{En}}, 2}$ and $F_{(2,2,0)}$

The main geometric application of folded diagrams is the construction of semitoroidal compactifications of moduli spaces $F_\Gamma$ and their quotients via **generalized Coxeter semifans**. Unlike classical toroidal compactifications where all walls of the Coxeter chamber are preserved, semitoroidal compactifications allow certain **irrelevant roots** to be removed.
In the case of interest to us, the semifan $ \mathcal{F} \_{\bullet} $ is constructed by:

1. Identifying the 0-cusps of $F_{(2,2,0)}$ and their corresponding Coxeter diagrams and semifans
2. Folding the semifans and Coxeter diagrams to determine the Coxeter diagrams for the 0-cusps of $F_{{\mathrm{En}}, 2}$
3. Identifying the irrelevant roots for foldings as images of irrelevant roots of the corresponding $F_{(2,2,0)}$ cusp
4. Removing the corresponding walls to create a coarser fan structure for $F_{{\mathrm{En}}, 2}$

This process constructs the compactification $\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} *{\bullet} }$ appearing in the main theorem, and the distinction between toroidal and strictly semitoroidal behavior depends on the order of the irrelevant root subgroup: toroidal cusps are those with finite irrelevant subgroups, while strictly semitoroidal cusps are those with infinite irrelevant subgroups.
The folding procedure operates as follows: Let $W$ be the reflection group generated by $\Phi$ inside $\operatorname{O}(L)$, and $W^G$ the reflection group generated by $\Phi^G$ where $G$ acts as a diagram automorphism.
If $ \mathfrak{C} \subset L*{\mathbf{R}}$ is a $G$-invariant Weyl chamber for $W$, then the restriction $$ \mathfrak{C} ^G \mathrel{\mathop:}= \mathfrak{C} \cap L^G*{\mathbf{R}}
$$ is a fundamental chamber for $W^G$.
The walls are given by hyperplanes orthogonal to the folded roots $\beta*{[\alpha_i]}$, where each folded root is either a fixed root under $G$ or the "average" of an orbit: the sum of roots in a $G$-orbit, satisfying orthogonality conditions.
The relationship between $F_{(2,2,0)}$ (quartic hyperelliptic K3 surfaces) and $F_{{\mathrm{En}}, 2}$ (degree 2 numerically polarized Enriques surfaces) is determined by the lattice involution $I = -I_{{\mathrm{En}}}$ acting on the transcendental lattice $T_{\operatorname{dP}} = U \oplus U(2) \oplus E_8^2$.
The fixed sublattice under this involution is precisely the Enriques transcendental lattice $T_{{\mathrm{En}}} = U \oplus U(2) \oplus E_8(2)$.
At each 0-cusp $\eta$ of $\partial\overline{F_{(2,2,0)}}^{ \operatorname{BB} }$, which are distinguished by primitive isotropic vectors $\eta\in T_{\operatorname{dP}}$ of divisibility 1 or 2, there exists a stable reflection group $\Gamma_\eta$ whose reflection group $W(\Gamma_\eta)$ and associated Coxeter diagram $G(\Gamma\eta)$ encodes the incidence relations of points and curves in $\partial \overline{F_{(2,2,0)}}^{ \operatorname{BB} }$ at $I$.
T The key technical result governing the folding is:

:::{#lem-which-roots-descend .lemma title="Root folding criterion"}
Let $\Phi(T_{\operatorname{dP}})$ be the root syste of $T_{\operatorname{dP}}$ and $I$ be the induced involution.
The folded roots $\beta_{[v]} \in\Phi( T_{\operatorname{dP}}^{\left\langle I \right\rangle} )$ arise in exactly one of the following ways:

1.  $v \in \Phi^2(T_{\operatorname{dP}})$ and $\beta_{[v]}\in \Phi(T_{{\mathrm{En}}})$,
2.  $v \in \Phi^4(T_{\operatorname{dP}})$ and $\beta_{[v]}\in \Phi(T_{{\mathrm{En}}})$, or
3.  $v\in \Phi^2(T_{\operatorname{dP}})\cap I(v)^{\perp T_{\operatorname{dP}}}$, and so $\beta_{[v]} \mathrel{\mathop:}= v + I(v) \in \Phi^4(T_{{\mathrm{En}}})$ is the sum of orthogonal roots in $\Phi^2(T_{\operatorname{dP}})$.
    :::

::: proof
Noting that $T_{{\mathrm{En}}} = T_{\operatorname{dP}}^{I=1}$ is a sublattice, any $v\in \Phi(T_{\operatorname{dP}})$ which is $I$-invariant is also in $\Phi(T_{{\mathrm{En}}})$ by definition, since its norm, primitivity, and divisibility are unchanged, and the folded root is defined by $\beta_{[v]} = v$.

So suppose $I(v) \neq v$, so $\beta_{[v]} \mathrel{\mathop:}= v + I(v)$ is the orbit sum, which is $I$-invariant by construction.
If $v^2 = -2$, noting that $I \in \operatorname{O}(T_{{\mathrm{En}}})$ is an isometry, we have $$
\beta_{[v]}^2 \mathrel{\mathop:}= (v + I(v) )^2 = v^2 + 2 v\cdot I(v) + I(v)^2 =
2v^2 + 2v\cdot I(v)
,$$ and thus if $v\perp I(v)$ then the norm is doubled, and if $v$ is a $(-2)$-root then $\beta_{[v]}$ is a $(-4)$-root.
The remaining cases are when

1.  $I(v)\neq v$ but $v^2=-4$, or
2.  when $v^2 = -2$ but $v$ is not orthogonal to \$I(v)

The first case can be immediately dispensed with, since folding doubles the norm.
Suppose that $v \notin T_{{\mathrm{En}}}$, so $v_I = v + I(v)$.
Write $v \in T_{\operatorname{dP}}$ in the block form as in Definition 2.3. Then one can write

`\begin{align*}
v = (u_1, u_2, u_3, \alpha_1, \alpha_2)
\implies I(v) &= (u_1, u_2, u_3, -\alpha_2, -\alpha_1) \\
&= v - (0,0,0,\alpha_1+\alpha_2,\alpha_1+\alpha_2) \\
\implies v \cdot I(v) &= v^2 - (\alpha_1+\alpha_2)^2, \\
\implies v_I^2 &= (v + I(v))^2 \\
&= 2( v^2 + v \cdot I(v) ) \\
&= 2( 2v^2 - (\alpha_1+\alpha_2)^2) \\
&= 4v^2 - 2(\alpha_1 + \alpha_2)^2 < 0,
\end{align*}`{=tex}

Now since $v\neq I(v)$, we have $0\neq v-I(v) = (0,0,0,\alpha_1+\alpha_2, \alpha_1+\alpha_2)$ and thus $\alpha_1 + \alpha_2\neq 0$ in $E_8$, forcing $(\alpha_1 + \alpha_2)^2 < 0$ since $E_8$ is negative-definite.
But then $v\cdot I(v) = v^2 + c$ where $c := -(\alpha_1+\alpha_2)^2 > 0$, so $v\cdot I(v) > v^2$.
Let $\lambda := (\alpha_1 + \alpha_2)^2$; there are now two cases:

**Case 1: $v^2 = -2$**

In this case, we have $$
v_I^2 = 4(-2) - 2\lambda = -8 - 2\lambda < 0
$$ We want $v_I$ to be a root with the correct divisibility and primitiveness in $T_{{\mathrm{En}}}$.
The only possibility is $v\cdot I(v) = 0$, and we thus have `\begin{align*}
0 = v\cdot I(v)
&= v^2 - \lambda \\
\implies \lambda
&= -2  \\
\implies v_I^2
&= 4v^2 - 2\lambda  \\
&= -8 - 2(-2) \\
&= -4
\end{align*}`{=tex} and since $\operatorname{div}_{T_{En}}(v_I) = 2$, $v_I$ is a well-defined root of $T_{{\mathrm{En}}}$.
However, note that $\operatorname{div}_{T_{dP}}(v_I) \ne 2$ -- otherwise, $\alpha_1 + \alpha_2 \in 2E_8$, which implies that $\lambda = (2(\alpha_1'+\alpha_2'))^2 = 4\lambda'\in 4\mathbb{Z}$ with $\lambda' = (\alpha_1' + \alpha_2')^2 < 0$.
But then $$
v\cdot I(v) = v^2 - \lambda = -2 - 4\lambda' \geq 2
$$ and thus $$
v_I^2 = 4v^2 -2 (\alpha_1+\alpha_2)^2 = -8 -2\cdot (4\lambda') \geq 0
,$$ a contradiction.

**Case 2: $v^2 = -4$**

In this case we have $\operatorname{div}_{T_{dP}}(v) = 2$ and $\alpha_1,\alpha_2,\alpha_1 + \alpha_2 \in 2E_8$.
By similar computations as in the first case, we again obtain $$
-\lambda \geq 8 \implies v \cdot I(v) \geq 4 \implies v_I^2 \geq 0
,$$ a contradiction.
Finally, the converse follows from [Nam85, 2.13 and 2.15], since $T_{{\mathrm{En}}}[k]/\operatorname{O}(T_{{\mathrm{En}}})$ contains one orbit for $k=-2$ and two orbits for $k=-4$.
:::

<!--

**Lemma 3.4** (Folded Roots Characterization): For the involution $I = -I_{{\mathrm{En}}} = I_{\operatorname{dP}} \circ I_{{\mathrm{En}}} = I_{ {\mathrm{Nik}} }$ on $T_{\operatorname{dP}}$, if $\alpha$ is a root with $\alpha_I^2 < 0$, then $\alpha_I$ is a root in $T_{{\mathrm{En}}}$ of one of three types:
1. $\alpha^2 = -2$, $\alpha \in T_{{\mathrm{En}}}$: direct descent
2. $\alpha^2 = -4$, $\alpha \in T_{{\mathrm{En}}}$: direct descent
3. $\alpha^2 = -2$, $\alpha \cdot I(\alpha) = 0$: creates new $(-4)$-root $\alpha_I = \alpha + I(\alpha)$

**Detailed Proof of Lemma 3.4**:
- For $\alpha \notin T_{{\mathrm{En}}}$, write $\alpha = (v, u, -u, e, e')$ in block form.
  Then $I(\alpha) = (v, u, -u, -e', -e)$.
- Direct computation: $\alpha_I^2 = 2\alpha^2 + 2(\alpha \cdot I(\alpha))$ where $\alpha \cdot I(\alpha) = \alpha^2 - (e+e')^2$.
- Since $\alpha \neq I(\alpha)$, we have $e + e' \neq 0 \in E_8$, forcing $(e+e')^2 \leq -2$.
- For $\alpha^2 = -2$: This forces $\alpha \cdot I(\alpha) = 0$ and $\alpha_I^2 = -4$.
- For $\alpha^2 = -4$: Since $\operatorname{div}*{T*{\operatorname{dP}}}(\alpha) = 2$, both $e, e' \in 2E_8$, so $(e+e')^2 \leq -8$, giving $\alpha \cdot I(\alpha) \geq 4$ and $\alpha_I^2 \geq 0$, which contradicts the root condition.

-->

Thus for every 0-cusp $\tilde \eta_i\in T_{\operatorname{dP}}$ for $F_{(2,2,0)}$, we have an explicit understanding of how roots $\alpha$ in boundary lattices $ \overline{T*{\operatorname{dP}}}*{ \tilde\eta*i } $ ($i=1,2$) descend or combine when passing to the $I$-invariant sublattices, which correspond to $ \overline{T*{{\mathrm{En}}}}*{ \eta_j } $ ($j=1,\cdots,5$). The Coxeter diagrams $G( {\Gamma*{\operatorname{dP}}} *{\tilde \eta_i} )$ at 0-cusps $\eta_i$ in $F*{(2,2,0)}$ determine, via their maximal parabolic subdiagrams, the type ${\textrm{II}}$ curves adjacent to $\eta_i$ in $\partial\overline{F_{(2,2,0)}}^{ \operatorname{BB} }$.
Under the folding involution $I$, only those maximal parabolic subdiagrams that are $I$-invariant and whose images remain maximal parabolic correspond to maximal parabolic subdiagrams in the folded diagram $G( G( {\Gamma_{\operatorname{dP}}} *{\tilde \eta_i} ) )^I$, which in turn correspond to maximal parabolic subdiagrams in $G( {\Gamma*{{\mathrm{En}}, 2}} *{\eta_j} )$ and thus boundary curves in $\partial\overline{F*{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$.
The incidences between 0-cusps and 1-cusps is preserved only for these cases, and thus under this correspondence, we can determine the cusp diagram of $F_{{\mathrm{En}}, 2}$ entirely by studying folded diagrams.

<!-- Source: 1-part-combinatorial/3-chapter-enriques-k3/000-k3-enriques.md -->

## Enriques Surfaces and Their K3 Covers {#chapter-3}

Building on the foundational lattice theory established in \Cref{chapter-1} and \Cref{chapter-2}, we focus on the concrete geometric constructions, orbit classifications, and boundary correspondences that distinguish Enriques surface moduli theory from general K3 theory.
Every degree 2 numerically polarized Enriques surface can be realized via a canonical toric construction, which we describe in this chapter.

### Notational Conventions

We establish standard notation to be used throughout the remainder of this work: for lattice theoretic constructions, we write $U$ for the hyperbolic plane, $\left\langle a_1, \ldots, a_n \right\rangle$ for the diagonal lattice with Gram matrix $\operatorname{diag}(a_1, \ldots, a_n)$, $L(m)$ for rescaling of lattice $L$ by factor $m$, $L^{\oplus n}$ for the $n$-fold orthogonal direct sum, and $L {}^{ \vee }$ for the dual lattice $\operatorname{Hom}*{{\mathbf{Z}}}(L, {\mathbf{Z}})$.
We write ${\textrm{I}}*{p,q}$ and ${\textrm{II}}*{p, q}$ for the unique odd (resp.
even) nondegenerate unimodular lattice of signature $(p, q)$ over ${\mathbf{Z}}$.
For root lattices, we use $A_n, D_n, E_6, E_7, E_8$ for the classical root lattices, $\Phi(L)$ for the root system of all roots in $L$, and $W(L)$ for the Weyl group generated by reflections in all roots.
These are typically indexed by vectors of norm $v^2=-2$ or those of norm $v^2=-4$ with divisibility 2. We write $A_L \mathrel{\mathop:}= L {}^{ \vee } / L$ for the discriminant group, $q_L: A_L \to {\mathbf{Q}}/2{\mathbf{Z}}$ for the discriminant quadratic form, and $\ell(L) \mathrel{\mathop:}= \ell(A_L) = \operatorname{rank}*{{ \mathbf{F} }*2} A_L$ for the length of the discriminant group.
For group actions, we denote $\operatorname{O}(L)$ for the orthogonal group of lattice $L$, $\operatorname{O}^*(L) = \ker(\operatorname{O}(L) \to \operatorname{O}(A_L))$ for the stable orthogonal group, $\operatorname{div}_L(v)$ for the divisibility of vector $v$ in $L$, and $L[k] = \{v \in L{~~\mathrel{\Big\vert}~~}  v^2 = k\}$ for vectors of squared length $k$.
In applications to K3 and Enriques surfaces, $ {L*{\mathrm{K3}}} $ denotes the K3 lattice, $(r,a,\delta)$ are the classification invariants for 2-elementary lattices, $\iota*{{\mathrm{En}}}$ is the Enriques involution, and $F*{{\mathrm{En}}, 2}$ is the moduli space of Enriques surfaces with polarization of degree 2.

<!-- Source: 1-part-combinatorial/3-chapter-enriques-k3/100-main-diagram.md -->

### The Main Diagram and Geometric Construction

#### The base surface $Y={\mathbf{P}}^1\times {\mathbf{P}}^1$

##### The Basic Geometry of ${\mathbf{P}}^1\times {\mathbf{P}}^1$

Let $Y = {\mathbf{P}}^1 \times {\mathbf{P}}^1$ over ${\mathbf{C}}$, with coordinates $(x, y)$ on standard affine charts.
Consider the natural projections onto the two factors, [ p_1: Y \to {\mathbf{P}}\^1_1, \qquad p_2: Y \to {\mathbf{P}}\^1_2. ] Let $H_1 \subset {\mathbf{P}}^1_1$ and $H_2 \subset {\mathbf{P}}^1_2$ denote hyperplane classes on the first and second factor, respectively, and write their pullbacks as $\ell_1 \mathrel{\mathop:}=  p_1^* H_1$ and $\ell_2 \mathrel{\mathop:}=  p_2^* H_2$.
The group $\operatorname{Pic}(Y) \cong {\mathbf{Z}}^2$ is freely generated by $\ell_1$ and $\ell_2$, so every divisor (and hence every line bundle) corresponds to a vector $(a, b)$.
The intersection numbers of $\ell_1$ and $\ell_2$ can be readily computed, yielding the following lattice isometry: [ \ell*1\^2 = 0, \qquad \ell*2\^2 = 0, \qquad \ell*1 \cdot \ell*2 = 1 \implies (\operatorname{Pic}(Y), \cdot) { \, \xrightarrow{\sim}\, } `\left( {{\mathbf{Z}}^2, \matt 0110} \right) = U ,] which follows because fibers do not intersect, while a fiber and a section (or a fiber in the other projection) generically intersect in a single point, and we can readily apply Chow's moving lemma to arrange for this.
For any{=tex} $(a, b) \in {\mathbf{Z}}^2$, the line bundle ${\mathcal{O}}_Y(a, b)$ is defined as [ `{\mathcal{O}}*Y(a, b) = p_1^\*\ {\mathcal{O}}*{{\mathbf{P}}\^1}(a)\ \otimes*{{\mathcal{O}}*Y}\ p_2\^\*\ {\mathcal{O}}*{{\mathbf{P}}^1}(b) ] and its associated divisor class is $a \ell_1 + b \ell_2$.
On the standard affine open $U_{00} = \{x_0 \ne 0,\, y_0 \ne 0\}$ with local coordinates $x = x_1 / x_0$, $y = y_1 / y_0$, a section of ${\mathcal{O}}_Y(a, b)$ has the form [ f(x, y) = \sum*{\substack{0 \leq i \leq a \\ 0 \leq j \leq b}} a*{ij}, x\^i y\^j, \qquad a*{ij} \in {\mathbf{C}} .] Globally, a section of ${\mathcal{O}}_Y(a, b)$ corresponds to a bihomogeneous polynomial $F(x_0, x_1, y_0, y_1)$ of "bidegree" $(a, b)$: [ F(x_0, x_1; y_0, y_1) = \sum*{\substack{i + j = a \\ k + \ell = b}} c*{i, j; k, \ell} ; x_0\^{i}, x_1\^{j} \cdot y_0\^{k} , y_1\^{\ell}, \qquad c\_{i, j; k, \ell} \in {\mathbf{C}} .] Thus $H^0( {\mathcal{O}}_Y(a, b) )$ is generated by the monomials $x^i y^j$, where $0 \leq i \leq a$ and $0 \leq j \leq b$.
If $f$ is a section of ${\mathcal{O}}_Y(a, b)$, we thus say it has **bidegree** $(a, b)$.
Recall that a **del Pezzo surface** is a smooth projective surface $Y$ with ample anticanonical divisor $-K_Y$, and the **degree** of a del Pezzo surface is the intersection number $(-K_Y)^2$.
The canonical divisor on $Y$ is $K_Y = -2\ell_1 - 2\ell_2$ and thus corresponds to the vector $(-2, -2$, making the degree easy to compute: [ K_Y\^2 = (-2, -2)\^t \matt 0110 (-2, -2) = 8 .] This of course agrees with the standard calculation, $$ K_Y^2 = (-2\ell_1 - 2\ell_2)^2 = 4(\ell_1^2 + 2(\ell_1 \cdot \ell_2) + \ell_2^2 ) = 4 (0 + 2 \cdot 1 + 0 ) = 8. $$ We thus recover the well-known fact that $Y$ is a del Pezzo surface of degree $8$.
It is also well-known that $Y$ is a toric, and the polytope for the projective toric pair $(Y, {\mathcal{O}}*Y(a, b))$ is the rectangle $Q*{a,b} \mathrel{\mathop:}= [0, a] \times [0, b] \subseteq {\mathbf{Z}}^2$.
In particular, for ${\mathcal{O}}*Y(4, 4)$, the polytope is the square $Q\mathrel{\mathop:}= Q*{4,4} = [0, 4]^2 \subseteq M_Y \mathrel{\mathop:}= {\mathbf{Z}}^2$ with sides of lattice length 4.

##### Involutions in Coordinates

Define the involution $\tau: (x,y) \mapsto (-x, -y)$.
In homogeneous coordinates, this is given by $(x_0:x_1,\, y_0:y_1) \mapsto (x_0:-x_1,\, y_0:-y_1)$.
The involution $\tau$ fixes the four points with coordinates $(x,y)$ equal to either $0$ or $\infty$, that is, those in $\{0,\infty\} \times \{0,\infty\}$.
The action $\tau \curvearrowright H^0( {\mathcal{O}}_Y(4,4) )$ is given on generators $\tau^*(x^i y^j) = (-1)^{i+j} x^i y^j$.
Hence, the $\tau$-invariant monomials are those for which $i+j$ is even.
Let $W = Y/\tau$, and denote by $\phi: Y \to W$ the quotient map.
This map is branched precisely at the four fixed points described above, and the quotient is locally given by $(u,v) \mapsto (u^2, v^2)$, yielding 4 $A_1$ singularities on $W$.

Adjunction for finite covers gives $K_Y = \phi^* K_W + R$, where $R$ is the ramification divisor, here the sum of the four fixed points.
Since any intersection involving $R$ vanishes (as it is $0$-dimensional), it follows that $K_Y^2 = (\phi^* K_W)^2$.
The map $\phi$ has degree two, so $(\phi^* K_W)^2 = 2 K_W^2$, and hence $K_W^2 = K_Y^2 / 2 = 4$.
Thus, $W$ is a (singular) del Pezzo surface of degree $4$.
The ampleness of $-K_W$ follows from the fact that $-K_Y$ is ample and the ramification locus consists only of isolated points.
The surface $W$ is again toric, and yields a projective pair $(W, Q_W)$ where $Q_W \mathrel{\mathop:}= Q \cap {\mathbf{Z}}^2_{\mathrm{ev}}$ where $$ {\mathbf{Z}}^2_{\mathrm{ev}} = \{ (i, j) \in {\mathbf{Z}}^2 {~~\mathrel{\Big\vert}~~} i+j \in 2{\mathbf{Z}} \} ,$$ corresponding to $\tau$-invariant monomials.
Thus $Q$ and $W$ share the same polytope, but for the two distinct lattices $M_Y \mathrel{\mathop:}= {\mathbf{Z}}^2$ and $M_W \mathrel{\mathop:}= {\mathbf{Z}}^2_{\mathrm{ev}}$.
We note that $Q_Z$ has 16 boundary lattice points and 9 interior points, yielding 25 total sections of ${\mathcal{O}}_Y(4,4)$, while $Q_W$ has 8 boundary points and 5 interior points, yielding 13 $\tau$-invariant sections:

\begin{center}
\begin{tikzpicture}[scale=1.2]
% Define colors using a harmonious palette inspired by Material Design
% Base: Cool grays for structure
\definecolor{gridcolor}{RGB}{226, 232, 240} % slate-200
\definecolor{axiscolor}{RGB}{71, 85, 105} % slate-600

    % Lattice points: Dark blue-gray and teal accent
    \definecolor{fulllatticept}{RGB}{100, 116, 139}  % slate-500
    \definecolor{evenlatticept}{RGB}{20, 184, 166}   % teal-500

    % Polytope: Indigo primary with complementary coral edges
    \definecolor{polytopefill}{RGB}{99, 102, 241}    % indigo-500
    \definecolor{polytopeedge}{RGB}{79, 70, 229}     % indigo-600
    \definecolor{polytopevertex}{RGB}{251, 113, 133} % rose-400

    % Set up the viewing window
    \clip(-1.5,-1.5) rectangle (5.5,5.5);

    % Draw background grid
    \draw[gridcolor] (-2,-2) grid (7,7);

    % Draw coordinate axes
    \draw[axiscolor, thick, ->] (-1.2,0) -- (6.2,0);
    \draw[axiscolor, thick, ->] (0,-1.2) -- (0,6.2);

    % Add monomial axis labels for x-axis
    \node[below right, axiscolor, font=\small] at (0,-0.1) {$x_0^4$};
    \node[below, axiscolor, font=\small] at (1,-0.1) {$x_0^3x_1$};
    \node[below, axiscolor, font=\small] at (2,-0.1) {$x_0^2x_1^2$};
    \node[below, axiscolor, font=\small] at (3,-0.1) {$x_0x_1^3$};
    \node[below, axiscolor, font=\small] at (4,-0.1) {$x_1^4$};

    % Add monomial axis labels for y-axis
    \node[above left, axiscolor, font=\small] at (-0.1,0) {$y_0^4$};
    \node[left, axiscolor, font=\small] at (-0.1,1) {$y_0^3y_1$};
    \node[left, axiscolor, font=\small] at (-0.1,2) {$y_0^2y_1^2$};
    \node[left, axiscolor, font=\small] at (-0.1,3) {$y_0y_1^3$};
    \node[left, axiscolor, font=\small] at (-0.1,4) {$y_1^4$};

    % Define the polytope Q as a 4x4 square
    % Vertices: (0,0), (4,0), (4,4), (0,4)
    \coordinate (v1) at (0,0);
    \coordinate (v2) at (4,0);
    \coordinate (v3) at (4,4);
    \coordinate (v4) at (0,4);

    % Fill the polytope with subtle color
    \fill[polytopefill, opacity=0.25] (v1) -- (v2) -- (v3) -- (v4) -- cycle;

    % Draw polytope edges
    \draw[polytopeedge, line width=2pt] (v1) -- (v2) -- (v3) -- (v4) -- cycle;

    % Draw all lattice points in the viewing window
    \foreach \x in {-1,0,1,2,3,4,5,6} {
        \foreach \y in {-1,0,1,2,3,4,5,6} {
            \fill[fulllatticept, opacity=0.3] (\x,\y) circle (0.08);
        }
    }

    % Highlight the even sublattice points (where i+j is even)
    \foreach \x in {-1,0,1,2,3,4,5,6} {
        \foreach \y in {-1,0,1,2,3,4,5,6} {
            \pgfmathparse{int(mod(\x+\y,2))}
            \ifnum\pgfmathresult=0
                \fill[evenlatticept, opacity=0.25] (\x,\y) circle (0.14);
            \fi
        }
    }

    % Highlight polytope vertices with rose accent
    \foreach \v in {v1,v2,v3,v4} {

    }

    % Add labels for the polytope
    \node[polytopeedge, font=\bfseries] at (1.5,4.4) {$Q_Y, Q_W$};

\end{tikzpicture}
\end{center}

##### The K3 Double Cover

We briefly recall the standard construction of a double cover of smooth projective surface $Y$ branched over a reduced divisor $B$ as a method of producing (families of) Calabi-Yau varieties (see e.g.(Pardini 1991)). Select a line bundle $L$ such that $L^{\otimes 2} \cong {\mathcal{O}}_Y(B)$ -- for example, if $B \in |-2K_Y|$, one can take $L = -K_Y$.
We can write $B$ as the zero divisor of zeros of a section $f \in H^0(Y, L^{\otimes 2})$, and define a coherent ${\mathcal{O}}_Y$-algebra ${\mathcal{A}} = {\mathcal{O}}*Y \oplus L^{-1},$ where the algebra structure is locally determined by $$ (o_1 \oplus \ell_1) \cdot (o_2\oplus \ell_2) = (o_1o_2 + { \left.{{f}} \right|*{{U}} } \cdot \ell_1\ell_2) \oplus (o_1\ell_2 + o_2\ell_1)z, \quad o_i \in {\mathcal{O}}_Y(U),\, \ell_i \in L^{-1}(U) $$ where $z\in H^0(L^{-1})$ is a generator of $L^{-1}$ satisfying $z^2 = f$.
The double cover $\pi: X\to Y$ is then constructed as $X = \operatorname{Spec}_Y({\mathcal{A}})$; $\pi$ is a finite morphism, it is etale away from $B$, and is ramified to order 2 precisely over $B$.
The relation $z^2 + f = 0$ is imposed for an ${\mathcal{O}}_Y$-module generator $z$ of $L^{-1}$, and the algebra structure above ensures that global functions on $X$ over an open $U \subseteq Y$ are of the form $s_1 + z s_2$ with $s_i \in {\mathcal{O}}_Y(U)$ and $z^2 = f|_U$, and the covering involution is locally modeled by $z\mapsto -z$.
By the adjunction formula, one has $K_X = \pi^*\left(K_Y + L\right)$, and so for $L = -K_Y$, and $B \in |-2K_Y|$, we have $K_X = \pi^* (K_Y - K_Y) = {\mathcal{O}}_X$ and $X$ is Calabi-Yau.

##### The main family of K3 surfaces

We now let $B \subset Y$ be a smooth $\tau$-invariant curve in the linear system $|-2K_Y| = |{\mathcal{O}}_Y(4,4)|$.
Such a curve is defined by a bihomogeneous polynomial $f(x, y)$ of bidegree $(4,4)$ that is invariant under $\tau$; that is, only monomials $x^i y^j$ with $i + j$ even may have nonzero coefficient in $f$.
In order that $B$ does not pass through any of the four fixed points, it suffices to require that the coefficients of the monomials $1$, $x^4$, $y^4$, and $x^4 y^4$ are nonzero.
We now apply this to $B$ with $L = -K_Y = {\mathcal{O}}_Y(2,2)$ as above.
Since $Y$ is simply connected and $\pi$ is a finite cover, it follows that $X$ is simply connected as well.
Moreover, one can show by the Leray spectral sequence that $h^1({\mathcal{O}}_X) = h^1({\mathcal{O}}_Y) = 0$, and thus $X$ is a K3 surface.
For a toric description, let $P$ denote the polytope in ${\mathbf{R}}^3$ formed by forming the pyramid over $Q$ with apex $(2,2,2)$.
The associated toric threefold $V_P$ then contains $X$ as the affine hypersurface locally defined by the vanishing locus of $z^2 + f$.
By varying $B$, we can thus produce families of K3 surfaces as families of hypersurfaces in the toric threefold $V_P$.
The parameter space for such $B$ corresponds to the space of $\tau$-invariant global sections of ${\mathcal{O}}_Y(4,4)$.
There are exactly 13 monomials $x^i y^j$ of bidegree $(4,4)$ with $i+j$ even, which can be easily seen by counting lattice points in $Q$, and thus each choice of $f$ defines a point in an open subset $U \subseteq {\mathbf{P}}^{12}$.
We thus obtain a 12-dimensional family of such K3 surfaces.
While the full automorphism group of $Y$ is an extensions of $\operatorname{PGL}*2^2$, the relevant symmetries for this family are the scaling actions of the torus factor $({{\mathbf{C}}^{\times} })^2$ on the coordinate axes of $Y$, as well as the symmetries $D_4$ of $Q$.
We thus pass to a 10-dimensional family: $$ {\mathcal{M}}*{{\mathrm{En}}, 2} \mathrel{\mathop:}= U/(D_4 \rtimes ({{\mathbf{C}}^{\times} })^2\
.$$

##### Geometric Involutions

Let $X$ be constructed as above; it carries three distinguished involutions: \\begin `\begin{align*} \iota_{\operatorname{dP}}(x, y, z)   &= (x, y, -z) \\ \iota_{{\mathrm{En}}}(x, y, z)   &= (-x, -y, -z) \\ \iota_{ {\mathrm{Nik}} }(x, y, z)  &= (-x, -y, z) \end{align*}`{=tex}

The involution $\iota_{\operatorname{dP}}$ is the covering involution of the branched double cover $\pi\colon X \to Y$.
The original involution $\tau : (x, y) \mapsto (-x, -y)$ on $Y$ has two lifts to $X$, both $\iota_{{\mathrm{En}}}$ and $\iota_{ {\mathrm{Nik}} }$.
By checking directly in coordinates, o $$ \iota_{\operatorname{dP}}^2 = \iota_{{\mathrm{En}}}^2 = \iota_{ {\mathrm{Nik}} }^2 = \mathrm{id}*X, \quad \iota*{\operatorname{dP}} \circ \iota_{{\mathrm{En}}} = \iota_{{\mathrm{En}}} \circ \iota_{\operatorname{dP}} = \iota_{ {\mathrm{Nik}} } $$ and all three commute pairwise, thus generating a faithful representation of the Klein 4-group $G \mathrel{\mathop:}= \langle \iota_{\operatorname{dP}}, \iota_{{\mathrm{En}}}, \iota_{ {\mathrm{Nik}} } \rangle \cong {\mathbf{Z}}_2^2 \hookrightarrow \operatorname{Aut}(X)$ acting by algebraic automorphisms on $X$.
Moreover, on affine open sets, a generating holomorphic $2$-form for $X$ can be found, where the three involutions act in the following way:

`\begin{align*} \omega_X &= \operatorname{Res}_X \left( \frac{dx \wedge dy \wedge dz}{z^2 + f(x, y)} \right) \implies \iota^\star(\omega_X)\colon\,\,
\begin{cases}
  \iota_{\operatorname{dP}}^*(\omega_X) = -\omega_X, \\
  \iota_{{\mathrm{En}}}^*(\omega_X) = -\omega_X, \\
  \iota_{ {\mathrm{Nik}} }^*(\omega_X) = +\omega_X.
\end{cases}
\end{align*}`{=tex}

Thus, $\iota_{\operatorname{dP}}$ and $\iota_{{\mathrm{En}}}$ are **non-symplectic**, i.e. act as $-\mathrm{id}$ on $H^{2,0}(X)$, while $\iota_{ {\mathrm{Nik}} }$ is symplectic.
Let $Z = X/\iota_{{\mathrm{En}}}$ and $Z' = X/\iota_{ {\mathrm{Nik}} }$, write $\psi:X\to Z$ and $\psi'X:\to Z'$, and consider the singularities of the quotient surfaces.
Note that $Z'$ has at least 8 $A_1$ singularities, induced by the 4 fixed points of $\tau$ on $Y$ under the 2-to-1 cover $\pi:X\to Y$.
However, provided $B$ does not pass through $\operatorname{Fix}(\tau)$, it is a fixed-point-free invollution on $X$ and thus $Z$ is a smooth Enriques surface and $X$ is its universal K3 cover.
We summarize the current situation below:

\begin{longtable}{|c|c|c|c|c|} \hline $\iota_\star$ & $\iota_\star(x,y,z)$ & $\iota_\star^*\omega_X$ & $X/\iota_\star$ & Type \\
\hline \endfirsthead \hline $\iota_\star$ & $\iota_\star(x,y,z)$ & $\iota_\star^*\omega_X$ & $X/\iota_\star$ & Type \\
\hline \endhead \hline \endfoot

$\iota_{\operatorname{dP}}$ & $(x,y,-z)$ & $-\omega_X$ & $\pi: X\to Y$ & $\mathrm{K3}$, smooth \\ \hline $\iota_{{\mathrm{En}}}$ & $({-}x,{-}y,{-}z)$ & $-\omega_X$ & $\psi: X\to Z$ & Enriques, smooth \\ \hline $\iota_{ {\mathrm{Nik}} }$ & $({-}x,{-}y,\,z)$ & $+\omega_X$ & $\psi': X\to Z'$ & $\widetilde{\mathrm{K3}}$, $\ge8A_1$ \\ \hline

\end{longtable}

##### Branch and Ramification Divisors

Let $\tau_{\operatorname{dP}}$ be the involution on $Z$ induced by the deck transformation $\iota_{\operatorname{dP}}$ for the original cover $\pi:X\to Y$, and write $\rho:Z \to Z/\tau_{\operatorname{dP}} = W$ for the corresponding branched cover.
Let $B$ and $R$ denote the branch and ramification divisors of $\pi:X\to Y$, and $B_W$ and $R_Z$ the branch and ramification divisors of $\rho:Z\to W$.
We record the classical formulas $\pi^*(B) = dR$ and $R = {1\over d} \pi^*(R)$ for ramified $d$-to-$1$ covers, and we thus have $$ R = \psi^* R_Z = {1\over 2} \pi^*(B), \qquad R_Z = \frac12 \psi_* R .$$ Since $B$ is ample, $R$ is ample as the pullback of an ample divisor under a finite surjective morphism.
Since $\psi$ is a finite quotient by a group acting freely in codimension 1, the pushfoward $R_Z$ of $R$ is ample as well.
The associated line bundle on $Z$ satisfies ${\mathcal{M}} \mathrel{\mathop:}= {\mathcal{O}}_Z(R_Z) = {\mathcal{L}}_Z^{\otimes 2}$ for a suitable element ${\mathcal{L}}_Z \in \operatorname{Pic}(Z)$, and thus $[{\mathcal{L}}_Z] \in \operatorname{Pic}(Z)/C_2$ is a well-defined numerical polarization on the Enriques surface $Z$.
We can check that its degree is 2, and the degree of ${\mathcal{M}}$ is 8. Conversely, if ${\mathcal{M}}$ is any polarization on an Enriques surface $Z$ with at worst ADE singularities which is 2-divisble, so ${\mathcal{M}} = {\mathcal{L}}_Z^{\otimes 2}$ for some ${\mathcal{L}}*Z\in \operatorname{Pic}(Z)$, then $\abs{{\mathcal{M}}}$ is big and nef and thus by (F. R. Cossec 1983; **CD89?**; C. F. Cossec, Dolgachev, and Liedtke 2024) defines a 2-to-1 branched cover $\rho:Z\to W$ where $W$ is a quartic del Pezzo with $4A_1$ or $A_3 + 2A_1$ singularities with ample ramification divisor $R_Z$.
In this situation, $(Z, \varepsilon R_Z)$ is a log canonical pair for small enough $\varepsilon$, and thus there is a well-defined KSBA moduli space of such pairs which we will refer to as $F*{{\mathrm{En}}, 2}$.
We summarize the overall situation in the following diagram:

\begin{figure}[ht] \centering \begin{minipage}{0.42\textwidth} \centering \begin{tikzcd}[ row sep={3cm,between origins}, column sep={3.2cm,between origins}, cells={nodes={font=\Large}}, every label/.append style = {font=\Large}, arrows={thick} ] X \arrow[d, swap, "\pi"] \arrow[r, "\psi"] \arrow[bend left=30]{rr}{\psi'} & Z \arrow[d, swap, "\rho"] & Z' \arrow[dl, "\rho'"] \\
Y \arrow[r, "\phi"] & W \end{tikzcd} \end{minipage} \hfill \begin{minipage}{0.42\textwidth} \centering \begin{tikzcd}[ row sep={3cm,between origins}, column sep={3.2cm,between origins}, cells={nodes={font=\Large}}, every label/.append style = {font=\Large}, arrows={thick} ] \mathrm{K3} \arrow[d, swap, "/\iota_{\operatorname{dP}}"] \arrow[r, "/\iota_{{\mathrm{En}}}"] \arrow[bend left=30]{rr}{/\iota\_{ {\mathrm{Nik}} }}
& \mathrm{En} \arrow[d, swap, "\rho"] & \widetilde{\mathrm{K3}}
\arrow[dl, "\rho'"] \\
{\mathbf{P}}^1 \times {\mathbf{P}}^1 \arrow[r, "/\tau"] & \mathrm{dP}\_4 \end{tikzcd} \end{minipage} \caption{The main diagram.} \end{figure}

Here,

- $\pi: X \to Y$ is the double cover branched over $B \subset Y$, recalling that $Y = {\mathbf{P}}^1\times {\mathbf{P}}^1$ and $X$ is a K3 surface,

- $\phi: Y \to W$ is the quotient by $\tau$,

- $\psi: X \to Z \mathrel{\mathop:}=  X/\iota_{{\mathrm{En}}}$ is the quotient by the Enriques involution $\iota_{{\mathrm{En}}}$ and $Z$ is a smooth Enriques surface,

- $\rho: Z \to W$ is the further quotient by the involution induced by $\iota_{\operatorname{dP}}$, where $W$ is a singular quartic del Pezzo with $4A_1$ or $A_3 + 2A_1$ singularities,

- $\psi': X \to Z'\mathrel{\mathop:}=  X/\iota_{ {\mathrm{Nik}} }$ is the quotient by the Nikulin involution $\iota_{ {\mathrm{Nik}} }$, where $Z'$ is a singular K3 surface with (at least) $8A_1$ singularities.

This diagram has been well-studied in the literature, see e.g. (F. R. Cossec 1983; **CD89?**; **Hor78a?**; Enriques 1906). The GIT quotient $$ \overline{ {\mathcal{M}}_{{\mathrm{En}}, 2} }^{ \operatorname{GIT} } \mathrel{\mathop:}= {\mathbf{P}}^{12} { \mathbin{/\mkern-6mu/}} D_4 \ltimes ({{\mathbf{C}}^{\times} })^2, $$ was studied in (Shah 1981), where it is determined exactly which forms of $f$ result in stable and unstable quartic K3 surfaces (**Hor78b?**) analyzed the period map and its extension.
In particular, if $f(x, y)$ vanishes at a torus-fixed point, the K3 cover $X$ acquires a node and the quotient by the Enriques involution is a **Coble surface**: a smooth rational projective surface with empty anti-canonical linear system $|-K| = \varnothing$ but non-empty anti-bicanonical system $|-2K| \neq \varnothing$.

<!-- Source: 1-part-combinatorial/3-chapter-enriques-k3/450-scattone.md -->

### Enumerating Cusps

As a starting point to any compactification procedure of lattice polarized K3 surfaces $F_S$, we must first find the cusps of $\overline{F}^{ \operatorname{BB} }_S$.
We give an overview here of various methods in the literature for similar moduli spaces, and how their cusps can be found and studied.

#### \$ F\_{2d} \$: Degree 2d Polarized K3 Surfaces (Scattone's Description)

\todo{Separate the Hodge-theoretic work}

Let $ {L*{\mathrm{K3}}} $ denote the K3 lattice, and let $h \in {L*{\mathrm{K3}}} $ be a primitive vector of square $2d > 0$.
The lattice orthogonal to the polarization is defined as $$ T_{2d} \mathrel{\mathop:}=  h^\perp_{ {L_{\mathrm{K3}}} } \cong \langle -2d \rangle \oplus U^{\oplus 2} \oplus E_8^{\oplus 2}, $$ which is even and of signature $(2,19)$.
The Type ${\textrm{IV}}$ Hermitian symmetric period domain for $T_{2d}$, $$ D_{T_{2d}} = \{ [\omega] \in {\mathbf{P}}(T_{2d, {\mathbf{C}}} ) {~~\mathrel{\Big\vert}~~} (\omega, \omega) = 0,\, (\omega, \overline{\omega}) > 0 \}, $$ admits a natural right action by the arithmetic group $\Gamma_{2d} \subset \operatorname{O}^+(T_{2d})$, the intersection of the original orthogonal group with the subgroup stabilizing $h$ (and, if necessary, a choice of connected component).
The arithmetic quotient $$ F_{2d} \mathrel{\mathop:}=   { D_{T_{2d}} }/{ \Gamma_{2d} } $$ is the coarse moduli space parametrizing degree $2d$ polarized K3 surfaces.

The Baily--Borel compactification $\overline{F_{2d}}^{ \operatorname{BB} }$ is projective, and its boundary strata correspond bijectively to $\Gamma_{2d}$-orbits of primitive isotropic sublattices of $T_{2d}$ of ranks $1$ and $2$.
More precisely, $0$-cusps are in correspondence with orbits of primitive isotropic planes up to the action of $\Gamma_{2d}$.
The incidence relations between cusps are set by lattice inclusions: any $0$-cusp (an isotropic line) is contained in the closure of all $1$-cusps (isotropic planes) in which it lies.

As a concrete and illustrative case, set $d = 1$.
Then $h^2 = 2$ and $$ T_2 = \langle -2 \rangle \oplus U^{\oplus 2} \oplus E_8^{\oplus 2}. $$ Scattone shows that for squarefree $d$ (in particular, $d = 1$), there is exactly one $\Gamma_{2d}$-orbit of primitive isotropic lines in $T_{2d}$, so the Baily--Borel boundary of $F_2$ has a unique $0$-cusp.

The 1-cusps are determined by the negative-definite lattices $ \overline{T}_{ 2d, I } \mathrel{\mathop:}= I^{\perp T}/I$, for $I \subset T$ a primitive isotropic plane.
Scattone showed that, up to isomorphism and the action of the arithmetic group, there are exactly four possible such lattices, each of rank $18$ and discriminant $2$, characterized by their root sublattices: `\begin{align}\label{eq-ft-four-lattices} A_1 \oplus E_8^{\oplus 2}, \qquad E_7 \oplus D_{10}, \qquad A*1 \oplus D*{16}, \qquad A\_{17}. \end{align}`{=tex} These emerge as orthogonal complements to embeddings of $E_7$ into the four Niemeier lattices $U$ of rank $24$ that admit such sublattices.
Each of these possibilities labels a modular curve in the boundary of $\overline{F_2}^{ \operatorname{BB} }$, and the closure of each of these modular curves contains the unique $0$-cusp as every isotropic line is contained in some isotropic plane.

The structure of $\partial \overline{F_{2d}}^{ \operatorname{BB} }$ can be studied through the asymptotic behavior of the period map, governed by limiting mixed Hodge structures and their associated monodromy operators, following the work of FS86. For a one-parameter degeneration ${\mathcal{X}} \to \Delta$ of polarized degree $2d$ K3 surfaces over a punctured disk $\Delta^*$, the unipotent monodromy operator $T \in O(T_{2d})$ determines the degeneration structure.
Its nilpotent logarithm $N = \log T \in \operatorname{End}(T_{2d, {\mathbf{Q}} })$ induces the canonical monodromy weight filtration $ {W}^{\bullet} $ on $T_{2d, {\mathbf{Q}}}$, uniquely characterized by the properties $N(W_k) \subseteq W_{k-2}$ for all $k$, and that for each $j > 0$, the maps $N^j: \operatorname{Gr}^W_{k+j} \to \operatorname{Gr}^W_{k-j}$ are isomorphisms.
Schmid's Nilpotent Orbit Theorem establishes that the period map asymptotically approaches a nilpotent orbit, defining a limiting Hodge filtration $ {F^{\lim}}*{\bullet} $ on $T*{2d, {\mathbf{C}}}$ which, together with $ {W}^{\bullet} $, constitutes the limiting mixed Hodge structure (LMHS). This framework provides the connection between geometric degenerations and arithmetic lattice structures.

The boundary components of $\overline{F_{2d}}^{ \operatorname{BB} }$ are classified by the nilpotency index of $N$.
The Type ${\textrm{II}}$ boundary components (1-cusps) correspond to degenerations where $N \neq 0$ but $N^2 = 0$.
For such degenerations, associated with a primitive isotropic plane $I \subset T_{2d}$, is a three-step monodromy weight filtration: $$ 0 = W_0 \subset W_1 = I_{{\mathbf{Q}}} \subset W_2 = I^{\perp T_{2d}}*{{\mathbf{Q}}} \subset W_3 = T*{2d, {\mathbf{Q}}}
.$$ The LMHS induces a pure polarized Hodge structure of weight 2 on the graded piece $\operatorname{Gr}*2^W = I^{\perp}/I$, which is precisely the boundary lattice $ \overline{T}*{ I } $ arising in Scattone's combinatorial classification.
This identification reveals that $ \overline{T}_{ I } $ is not merely a lattice-theoretic invariant, but rather the natural target of the weight-2 component of the limiting mixed Hodge structure.

For Type ${\textrm{III}}$ degenerations (0-cusps), where $N^2 \neq 0$ but $N^3 = 0$, the weight filtration is of maximal length.
The classifying space of such Hodge structures on $ \overline{T}*{ I } $ is itself a Type ${\textrm{IV}}$ Hermitian symmetric domain $D*{ \overline{T}*{ I } }$ and the boundary component itself is a modular variety $F*{\Gamma*I}$ for an appropriate arithmetic subgroup $\Gamma_I \leq \operatorname{O}^+( \overline{T}*{ I } )$.
These degenerations correspond to normal crossing varieties whose dual complex is a triangulation of $S^2$.
The computational accessibility of these mixed Hodge structures relies on several key tools developed in the work starting in (Friedman and Scattone 1986): the Clemens-Schmid exact sequence relating the cohomology of central and ${\mathcal{X}}*t$s, and the Steenbrink weight spectral sequence, which for K3 surfaces degenerates integrally at the $E_2$-page.
This integral degeneration is a special property of K3 surface degenerations that enables explicit computation of the limiting mixed Hodge structure components.
The vanishing cycle analysis developed by Friedman and Scattone provides detailed control over how cohomology classes behave under degeneration.
Through Mayer-Vietoris techniques and careful analysis of the dual complex structure, they established the precise relationship between the geometric combinatorics of singular fibers and the arithmetic invariants encoded in the limiting mixed Hodge structures.
The stratification $\overline{F*{2d}}^{ \operatorname{BB} }$ is thus realized by the asymptotic behavior of the period map at the various boundary cusps.

#### $F_2$: Scattone's Description

For the specific case $d=1$, (Scattone 1987) yields exactly four possible isometry classes for $ \overline{T}*{ I } $ determined by a 1-cusp $I$ adjacent to the unique 0-cusp $\eta$, distinguished by their root sublattices as defined above.
These correspond to the four distinct Type ${\textrm{II}}$ modular curves in the boundary of $\overline{F_2}^{ \operatorname{BB} }$.
The unique 0-cusp $\eta$ correspond to a Type ${\textrm{III}}$ component, and thus a degeneration where $N^2 \neq 0$ but $N^3=0$, yielding a weight filtration of maximal length.
The geometric inclusion of the 0-cusp in the closure of each 1-cusp reflects the lattice-theoretic fact that any primitive isotropic plane $I$ contains the primitive isotropic line $\eta$, all up to $\Gamma*{T*{2d}}$-invariance.
This incidence structure is encoded combinatorially in the Coxeter diagram of the lattice $ \overline{T}*{ 2d, \eta } $ associated to the 0-cusp, whose maximal parabolic subdiagrams are in bijection with the possible isomorphism classes of the lattices $ \overline{T}\_{ I } $ for the adjacent 1-cusps.

The cusps in $\overline{F_2}^{ \operatorname{BB} }$ are obtained by classifying primitive isotropic sublattices of the lattice\

$$
T_{2} \mathrel{\mathop:}= \langle -2\rangle\oplus U^{\oplus2}\oplus E_{8}^{\oplus2}
$$ using discriminant--form methods, from which Scattone shows:

-   there is a single $\Gamma_{2}$-orbit of primitive isotropic lines $\eta$ in $T_2$, giving one 0-cusp (Type ${\textrm{III}}$);\
-   there are four $\Gamma_{2}$-orbits of primitive isotropic planes $I$ in $T_2$, whose corresponding boundary lattices $ \overline{T}_{ I  } $ are the rank-18, negative-definite lattices given in \Cref{eq-ft-four-lattices}, yielding four Type ${\textrm{II}}$ boundary curves;\
-   these four curves meet transversely at the unique Type ${\textrm{III}}$ point.

We assemble this data into the following **cusp diagram**:

\begin{center}
\begin{tikzpicture}[
    square/.style={rectangle, draw, minimum width=3cm, minimum height=0.8cm},
    circ/.style={circle, draw, minimum size=0.8cm}
]

% Define nodes
\node[circ] (eta) at (0,0) {$\eta$};
\node[square] (A1) at (4,3) {$A_1 \oplus E_8^{\oplus 2}$};
\node[square] (E7) at (4,1) {$E_7 \oplus D_{10}$};
\node[square] (D16) at (4,-1) {$A_1 \oplus D_{16}$};
\node[square] (A17) at (4,-3) {$A_{17}$};

% Draw arrows
\draw[->] (eta.east) -- (A1.west);
\draw[->] (eta.east) -- (E7.west);
\draw[->] (eta.east) -- (D16.west);
\draw[->] (eta.east) -- (A17.west);

\end{tikzpicture}
\end{center}

The general enumeration of $\partial\overline{ F_{2d} }^{ \operatorname{BB} }$ reduces to finite problems in the discriminant group $A_{T_{2d}}$: cusps can be classified by studying isotropic subgroups of the finite discriminant group $A_{T_{2d}} \mathrel{\mathop:}=  (T_{2d})^*/T_{2d}$, and applying Nikulin's theorem that the genus of an even lattice is determined by its signature and the isomorphism class of its discriminant form [Nikulin 1980]. The classification proceeds by associating to a primitive isotropic sublattice $I \subset T_{2d}$ an isotropic subgroup of $A_{T_{2d}}$. The problem of classifying orbits of such sublattices under the infinite group $\Gamma_{2d}$ is thereby reduced to classifying orbits of isotropic subgroups of the finite group $A_{T_{2d}}$ under the action of a subgroup of $\operatorname{O}^*( A_{T_{2d}} )$. For the case $d=1$, he four isomorphism classes of the rank-18 lattice $ \overline{T}_{ I  } $ are constructed by leveraging the classification of the 24 Niemeier lattices: each isometry class of $ \overline{T}_{ I  } $ is realized as the orthogonal complement $E_7^\perp \subset M$, where $M$ is one of the Niemeier lattices that admit a primitive embedding of the $E_7$ root lattice [Scattone 1987]. This reduces the classification to a relatively well-known, finite set of possibilities. For general $d$, cusp enumeration becomes a number-theoretic problem, since structure of $A_{T_{2d}}$ is highly dependent on the arithetic properties of $d$ itself, including various the numbers of solutions to various congruences, as well as the prime factorization of $d$. (Scattone 1987) uses these techniques to explicitly describe cusp diagrams for certain (sparse) families of values of $d$. For further details and the explicit Coxeter diagrams, see (Scattone 1987, 6.2) and (Alexeev, Engel, and Thompson 2023, fig. 2).

<!--
# Separating Scattone's Methods: F₂d Paper vs. Type ${\textrm{III}}$ Degenerations Paper

Based on my research, I can now provide a clear separation between what Scattone accomplished in his two main papers: the 1987 memoir on F₂d compactifications and the 1986 collaboration with Friedman on Type ${\textrm{III}}$ degenerations.

## Scattone's 1987 F₂d Paper: "On the Compactification of Moduli Spaces for Algebraic K3 Surfaces"

### Core Methods and Focus

**Primary Approach: Lattice-Theoretic Classification**
- **Discriminant Form Analysis**: Scattone's main innovation was using discriminant quadratic forms to systematically classify boundary components
- **Isotropic Sublattice Classification**: Established bijective correspondence between boundary components and Γ₂d-orbits of primitive isotropic sublattices of T₂d
- **Arithmetic Group Theory**: Used properties of orthogonal groups O⁺(T₂d) and their action on isotropic sublattices

**Specific Technical Methods**:
1. **Eichler Criterion Application**: Used to classify primitive isotropic vectors and their orbits under arithmetic group action
2. **Discriminant Group Computations**: Exploited the finite discriminant group A_{T₂d} = (T₂d)*/T₂d to reduce infinite classification problems to finite ones
3. **Niemeier Lattice Connections**: For degree 2 case, used embeddings into the 24 Niemeier lattices to classify the four types of rank-18 lattices

**Key Results for F₂d**:
- Complete classification of boundary components for general degree 2d
- Explicit enumeration for d=1: exactly one 0-cusp and four 1-cusps with specific root lattice structures
- **Cusp Counting Formula**: Number of cusps depends on arithmetic properties of d (square-free factorization, congruences)

**Notable Absence**: The 1987 paper does **not** contain extensive Hodge-theoretic machinery - it's primarily combinatorial and arithmetic.

## Friedman-Scattone 1986 Paper: "Type ${\textrm{III}}$ Degenerations of K3 Surfaces"

### Core Methods and Focus

**Primary Approach: Mixed Hodge Structure Analysis**
- **Limiting Mixed Hodge Structures**: Systematic study of Steenbrink-Schmid theory for Type ${\textrm{III}}$ degenerations
- **Monodromy Weight Filtrations**: Detailed analysis of nilpotent monodromy operators N with N³=0 but N²≠0
- **Vanishing Cycle Analysis**: Study of how cohomology classes behave under degeneration

**Specific Technical Methods**:
1. **Clemens-Schmid Exact Sequence**: Used to relate cohomology of smooth and singular fibers
2. **Weight Spectral Sequence**: Proved integral degeneration at E₂ for K3 surface degenerations
3. **Mayer-Vietoris Analysis**: For computing cohomology of normal crossing varieties

**Key Results**:
- **Complete Classification**: All Type ${\textrm{III}}$ degenerations correspond to triangulations of S² with specific combinatorial constraints
- **Cohomological Invariants**: Showed how dual complex structure determines lattice-theoretic invariants
- **Monodromy Structure**: Established precise relationship between geometric degenerations and monodromy representations

## Critical Distinctions

### What Belongs to the F₂d Paper:
```
• Discriminant form techniques for boundary classification
• Isotropic sublattice orbit analysis
• Arithmetic group computations
• Cusp enumeration formulas
• Connection to Niemeier lattices (degree 2 case)
• Lattice genus theory applications
```

### What Belongs to the Friedman-Scattone Type ${\textrm{III}}$ Paper:
```
• Mixed Hodge structure machinery
• Monodromy weight filtrations
• Limiting Hodge filtration analysis
• Clemens-Schmid exact sequences
• Weight spectral sequence degeneration
• Vanishing cycle computations
• Connection to triangulations of S²
```

## The Text Analysis

Looking at the provided text, the **lattice-theoretic portions** (discriminant forms, isotropic sublattices, Niemeier lattice connections, cusp classification) clearly belong to **Scattone's 1987 F₂d work**.

The **Hodge-theoretic portions** (limiting mixed Hodge structures, monodromy weight filtrations, Steenbrink weight spectral sequences) belong to the **1986 Friedman-Scattone collaboration**.

The text appears to conflate methods from both papers, presenting them as if they were unified in a single approach, when in fact they represent distinct but complementary methodologies developed in separate works.
 -->

#### $F_{ \mathrm{ell} } $: Elliptic Surfaces (Brunyate-Alexeev's Description)

The moduli space $F_{ \mathrm{ell} } $ parametrizes elliptic K3 surfaces with a chosen section, a condition that fixes a primitive embedding of a hyperbolic plane $U_1 \subset  {L_{\mathrm{K3}}} $. The relevant period map is thus defined on the orthogonal complement $T_{ \mathrm{ell} }  \mathrel{\mathop:}=  U_1^{\perp_{ {L_{\mathrm{K3}}} }} \cong U^2 \oplus E_8^2$, and the moduli space is the 18-dimensional arithmetic quotient $F_{ \mathrm{ell} } $. A geometric description of the compactifications of $F_{ \mathrm{ell} } $ is given in (**ABE18?**), who construct KSBA compactifications and prove their isomorphism to specific semitoroidal compactifications. There a unique $F_{ \mathrm{ell} } $-orbit of 0-cusps in $T_{ \mathrm{ell} } $, repsented by $\eta = e$, and the analysis falls on $\overline{(T_{ \mathrm{ell} } )}_\eta \cong {\textrm{II}}_{1, 17}$ Semitoroidal compactifications are defined by fans constructed in the rational closure $ \mathfrak{C} _{\eta, {\mathbf{Q}}}$ of the positive cone in ${\textrm{II}}_{1, 17}$. Two separate KSBA compactifications are constructed:

1.  **The Ramification Divisor Compactification ($\overline{F}^{\operatorname{ram}}$):** The polarization is given by the class of the ramification divisor $R$ from the representation of the K3 surface as a double cover of ${\mathbf{P}}(1,1,4)$, so that $[R] = 3(s+2f)$, where $s$ is the section class and $f$ is the fiber class. This defines a KSBA compactification parametrizing pairs $(X, \epsilon R)$ with $X$ an slc K3 surface.

2.  **The Rational Curve Divisor Compactification ($\overline{F}^{\mathrm{rc}}$):** The polarization is taken to be $R = s + m \sum_{i=1}^{24} f_i$, where the $f_i$ are the 24 singular fibers of the elliptic fibration for a generic elliptic K3 surface.

The core result (**ABE19?**) is the identification of these KSBA moduli spaces with semitoroidal compactifications defined by specific fans in $ \mathfrak{C} _{{\mathbf{Q}}}$. The fundamental fan is the **Coxeter fan** $F^{\operatorname{Cox}}$, whose cones are the chambers of the reflection group $W({\textrm{II}}_{1,17})$. The **ramification fan** $F^{\operatorname{ram}}$ is a coarsening of $F^{\operatorname{Cox}}$ whose fundamental chamber is a union of four Coxeter chambers. The **rational curve fan** $F^{\mathrm{rc}}$ is a refinement of $F^{\operatorname{Cox}}$ obtained by subdividing its fundamental chamber into nine sub-chambers. (**ABE19?**) prove that the normalizations of $\overline{F}^{\operatorname{ram}}$ and $\overline{F}^{\mathrm{rc}}$ are isomorphic to the semitoroidal compactifications defined by the fans $F^{\operatorname{ram}}$ and $F^{\mathrm{rc}}$, respectively, laying the groundwork for our main result on $F_{{\mathrm{En}}, 2}$.

The geometric models for the boundary strata are constructed using the theory of **integral-affine spheres with 24 singularities ($\mathrm{IAS}^2$)**. A Type ${\textrm{III}}$ Kulikov degeneration of an elliptic K3 surface corresponds bijectively to a triangulated $\mathrm{IAS}^2$, and the monodromy of a one-parameter degeneration determines a vector $\lambda \in  \mathfrak{C} _{{\mathbf{Q}}}$, the **mondromy invariant**, which determines the combinatorial type of the stable limit $(X_0, \epsilon R)$ and is constant for all $\lambda$ within the interior of a cone of the relevant fan. This provides a description of the boundary strata as unions of rational surfaces with prescribed singularities determined by the $\mathrm{IAS}^2$.

Its Baily--Borel boundary contains a unique 0-cusp and two 1-cusps. The latter correspond to the two $\Gamma^{ \mathrm{ell} } $-orbits of primitive isotropic planes $I \subset T_{ \mathrm{ell} } $, distinguished by the isomorphism class of the negative-definite rank-16 lattice $ \overline{T}_{ I  }  = I^\perp/I$. These two classes are isometric to the root lattices $E_8 \oplus E_8$ and $D_{16}$, respectively, and the cusp diagram is as follows:

\begin{center}
\begin{tikzpicture}[
    square/.style={rectangle, draw, minimum width=3cm, minimum height=0.8cm},
    circ/.style={circle, draw, minimum size=0.8cm}
]

% Define nodes
\node[circ] (eta) at (0,0) {$\eta$};
\node[square] (E8) at (4,1) {$E_8^2$};
\node[square] (D16) at (4,-1) {$D_{16}$};

% Draw arrows
\draw[->] (eta.east) -- (E8.west);
\draw[->] (eta.east) -- (D16.west);

\end{tikzpicture}
\end{center}

#### $F_{{\mathrm{En}}}$: Unpolarized Enriques Surfaces
The moduli space of *unpolarized* Enriques surfaces corresponds to the lattice $T_{{\mathrm{En}}}$ and $\Gamma_{{\mathrm{En}}} \mathrel{\mathop:}= \operatorname{O}^+(T_{{\mathrm{En}}})$, yielding the orthogonal modular variety $F_{{\mathrm{En}}}$. To enumerate the 0-cusps of $\overline{F_{{\mathrm{En}}}}^{ \operatorname{BB} }$, one can replace $T_{{\mathrm{En}}}$ by an auxiliary lattice $K = U \oplus E_8 \oplus {\textrm{I}}_{1,1}$ and utilize a bijection
$$
T_{{\mathrm{En}}}/\operatorname{O}(T_{{\mathrm{En}}}) \cong K/\operatorname{O}(K) ,$$ allowing for a classification in terms of simpler lattices.
A primitive isotropic vector $\eta \in {\textrm{I}}*{1,1}\subset K$ yields a unimodular lattice $ \overline{T}*{ \eta  } $ of signature $(1,9)$.
There are precisely two such lattices up to isometry, ${\textrm{I}}*{1, 9}$ and ${\textrm{II}}*{1, 9}$.
Pulling back, some slightly finer analysis shows there are exactly two $\Gamma_{{\mathrm{En}}}$-orbits of primitive isotropic lines in $T_{{\mathrm{En}}}$, corresponding to two 0-cusps $\eta_1, \eta_2$.
A direct approach for **1-cusps** is analytic: any isotropic plane $P \subset K$ must contain an odd primitive isotropic vector $\eta$, due to the indefinite form ${\textrm{I}}*{1,1}$.
There is only one orbit of such under the full orthogonal group, so $P$ can always be assumed to contain $\eta$.
The remaining problem is to classify the possible isometry classes of primitive isotropic lines in $ \overline{T}*{ \eta  }  \cong {\textrm{I}}*{1,9}$.
By examining the parities of a basis $\{w, w'\}$ for $P$, one finds two inequivalent types: planes where both generators have the same parity (even/even or odd/odd), and planes where the two have different parity (even/odd).
Hence, there are exactly two distinct $\operatorname{O}(T*{{\mathrm{En}}})$-orbits of primitive isotropic planes, corresponding to two 1-cusps.

Explicit representatives can be given as follows.
The 0-cusps correspond to the isotropic lines $\langle e \rangle$ and $\langle e' \rangle$, where $U = \left\langle e,f \right\rangle$ and $U(2) = \left\langle e', f' \right\rangle$ as sublattices of $T_{{\mathrm{En}}}$.
The 1-cusps can be represented by the planes $\langle e, e' \rangle$, and $\langle e', f'+\alpha \rangle$ where $\alpha \in E_8$ is a fixed primitive vector with $\alpha^2=-4$.
We thus obtain the following cusp diagram:

\begin{center}
\begin{tikzpicture}[
    square/.style={rectangle, draw, minimum width=3cm, minimum height=1cm},
    circ/.style={circle, draw, minimum size=1cm}
]

% Define nodes
\node[square] (I1) at (0,0) {$I_1 = \langle e', f' + \alpha \rangle$};
\node[circ] (eta1) at (4,0) {$\eta_1 = e$};
\node[square] (I12) at (8,0) {$I_{1,2} = \langle \eta_1, \eta_2 \rangle$};
\node[circ] (eta2) at (12,0) {$\eta_2 = e'$};

% Draw arrows
\draw[->] (eta1.west) -- (I1.east);
\draw[->] (eta1.east) -- (I12.west);
\draw[->] (eta2.west) -- (I12.east);

% Add the constraint below
\node[below=0.5cm of I1] {$\alpha \in E_8, \alpha^2 = -4$};

\end{tikzpicture}
\end{center}

##### Mirror Moves

All of the above situations involved somewhat ad-hoc analyses, which can be verified by computing the Coxeter-Vinberg diagrams $G(\Gamma_\eta)$ at the 0-cusps $\eta$ associated to the arithmetic subgroup $\Gamma$ and classifying their maximal elliptic and parabolic subdiagrams.
This can be computationally difficult, so we note a algorithm that can unify most of the above situations when $\Gamma$ is the full (stable) orthogonal group.
Let $T$ be a 2-elementary, nondegenerate, even unimodular lattice of signature $(2, n)$ embedding into the K3 lattice $ {L_{\mathrm{K3}}} $, let $\Gamma = O^+(T)$, and consider the corresponding arithmetic quotient $F_\Gamma =  { D_{T} }/{ \Gamma } $.
All such lattices are encoded in Nikulin's pyramid diagram (see (**AE23b?**)) of 2-elementary lattices.
The **cusp diagram** of $\overline{F}*\Gamma$ is a labeled, directed graph whose vertices are boundary points and curves in $\overline{F}*\Gamma$, corresponding (up to $\Gamma$-equivalence) with primitive isotropic vectors $\eta, I$ in $T$ and their associated boundary lattices $ \overline{T}*{ \eta  } $, $ \overline{T}*{ I  } $, with an edge $v_1 \to v_2$ between vertices if the corresponding boundary stratum $F_1$ is contained in the closure of $F_2$.
The cusp diagram is computed as follows.

A **mirror move** is a lattice-theoretic operation governed by the existence of a primitive isotropic vector $\eta \in T$ of a specified type and splitting as proved in (**AE23b?**):

- **Odd/simple:** $\operatorname{div}_T(\eta) = 1$, and $T \cong U \oplus K$
- **Even, ordinary:** $\operatorname{div}_T(\eta) = 2$ and $\eta^*$ is ordinary in $A_T$, and $T \cong U(2) \oplus K$
- **Even, characteristic:** $\operatorname{div}*T(\eta) = 2$ and $\eta^*$ is characteristic, and $T \cong I*{1,1}(2) \oplus K$

The move replaces $T$ with $ \overline{T}_{ \eta  } $, computing the new invariants in each case.
A mirror move is only possible if the resulting lattice is realized (i.e., if the corresponding node exists in Nikulin's pyramid, Fig. 1) and admits the required splitting.

###### Step 1: Find All Orbits of $0$-Cusps $\eta$

1. **Start at the node $(r_0, a_0, \delta_0)$** in Nikulin's pyramid associated to $T$.

2. **For every admissible mirror move,** check for outgoing arrows (*mirror moves*) from this node, corresponding to possible splittings of boundary lattices $T_{\eta_a}$ for isotropic vectors $\eta_a$.
   Each outgoing arrow from $(r_0, a_0, \delta_0)$ will be of one of the following types:

\begin{longtable}{|c|c|c|} \hline Type of $\eta_a \in T$ & Destination $(r_1, a_1, \delta_1)$ & Splitting of $ \overline{T}*{ \eta_a  } $ \\
\hline Odd/simple & $(r_0-2,\, a_0,\, 1)$ & $U \oplus K$ \\
\hline Even, ordinary & $(r_0-2,\, a_0-2,\, 1)$ & $U(2) \oplus K$ \\
\hline Even, characteristic & $(r_0-2,\, a_0-2,\, 0)$ & $I*{1,1}(2) \oplus K$ \\
\hline \end{longtable}

**A $0$-cusp $\eta_a$ exists** if the arrow exists: the destination represents a realizable, hyperbolic, 2-elementary lattice $ \overline{T}*{ \eta_a  } $ in Nikulin's table, and the node at the head of the arrow gives the invariants $(r_1, a_1, \delta_1)$ of the boundary lattice $ \overline{T}*{ \eta_a  } $.

###### Step 2: All $1$-Cusps and Incidence Structure

1. For each $0$-cusp $\eta_a$ determined in Step 1, recursively use $ \overline{T}*{ \eta_a  } $ with invariants $(r_1, a_1, \delta_1)$ as a new starting point and consider all outgoing arrows from $(r_1, a_1, \delta_1)$ to construct $(r_2, a_2, \delta_2)$.
   Each move corresponds to a splitting of $ \overline{T}*{ I  }  \mathrel{\mathop:}=  \overline{(T_{\eta_a})}*{\eta_b}$ for a primitive isotropic vector $\eta_b \in  \overline{T}*{ \eta_a  } $:

\begin{longtable}{@{}llp{7cm}@{}}
\toprule \textbf{Type of $\eta_b \in  \overline{T}*{ \eta_a  } $} & \textbf{Destination $(r_2, a_2, \delta_2)$} & \textbf{Splitting of $ \overline{T}*{ I  }  = \overline{(T_{\eta_a})}_{\eta_b}$} \\
\midrule \endhead

Odd/simple                          & $(r_1 - 2,\, a_1,\, \delta_1)$       & $U \oplus K'$ \\
Even, ordinary                      & $(r_1 - 2,\, a_1 - 2,\, \delta_1)$   & $U(2) \oplus K'$ \\
Even, characteristic               & $(r_1 - 2,\, a_1 - 2,\, 0)$          & $I_{1,1}(2) \oplus K'$ \\

\bottomrule \end{longtable}

2. **A $1$-cusp $I$ of type $(\eta_a, \eta_b)$ exists** if and only if the move $(r_1, a_1, \delta_1) \to (r_2, a_2, \delta_2)$ exists, corresponding to a 2-elementary lattice $ \overline{T}_{ I  } $ with the specified invariants.
   The $1$-cusp $I$ is incident to $\eta_a$ if and only if it arises from such a two-step sequence.

###### Step 3: Diagram Extraction

The **nodes for $0$-cusps** are given by a single admissible mirror move from $(r_0, a_0, \delta_0)$, labeled by $(r_1, a_1, \delta_1)$, the corresponding lattice splitting, and the root system $\Phi( \overline{T}*{ \eta  } )$.
The **nodes for $1$-cusps** are determined by two-step sequences $(r_0, a_0, \delta_0) \to (r_1, a_1, \delta_1) \to (r_2, a_2, \delta_2)$, with associated lattice splitting and root system $\Phi( \overline{T}*{ I  } )$.
Each $1$-cusp is incident to every $0$-cusp $(r_1, a_1, \delta_1)$ that occurs as an intermediate node in such a sequence.
While the boundary lattice $ \overline{T}*{ I  } $ for a $1$-cusp is determined up to isometry by invariants $(r_2, a_2, \delta_2)$, distinct $\Gamma$-orbits of $1$-cusps are distinguished by their root lattices $\Phi( \overline{T}*{ I  } )$, either tabulated in \\cite{AE23b or computed via Vinberg's algorithm.
We conclude by tabulating several useful references to use when carrying out this algorithm:

\begin{longtable}{@{}lll@{}}
\toprule \textbf{Cusp} & \textbf{Invariants} & \textbf{Existence Condition} \\
\midrule \endhead

$0$-cusp $\eta$ & $(r_1, a_1, \delta_1)$ & One-step sequence $(r_0, a_0, \delta_0) \to (r_1, a_1, \delta_1)$ \\
$1$-cusp $I$    & $(r_2, a_2, \delta_2)$, $\Phi( \overline{T}_{ I  } )$ & Two-step sequence $(r_0, a_0, \delta_0) \to (r_1, a_1, \delta_1) \to (r_2, a_2, \delta_2)$ \\

\bottomrule \end{longtable} \section*{Change of Invariants Under Two-Step Mirror Moves} \begin{longtable}{@{}llll@{}}
\toprule \textbf{Step 1 Type, $\eta_a$} & \textbf{Step 2 Type, $\eta_b$} & \textbf{$(r_1, a_1, \delta_1)$} & \textbf{$(r_2, a_2, \delta_2)$} \\
\midrule \endhead

Odd/simple            & Odd/simple            & $(r_0 - 2,\, a_0,\, 1)$     & $(r_0 - 4,\, a_0,\, 1)$     \\
Odd/simple            & Even, ordinary        & $(r_0 - 2,\, a_0,\, 1)$     & $(r_0 - 4,\, a_0 - 2,\, 1)$ \\
Odd/simple            & Even, characteristic  & $(r_0 - 2,\, a_0,\, 1)$     & $(r_0 - 4,\, a_0 - 2,\, 0)$ \\
Even, ordinary        & Odd/simple            & $(r_0 - 2,\, a_0 - 2,\, 1)$ & $(r_0 - 4,\, a_0 - 2,\, 1)$ \\
Even, ordinary        & Even, ordinary        & $(r_0 - 2,\, a_0 - 2,\, 1)$ & $(r_0 - 4,\, a_0 - 4,\, 1)$ \\
Even, ordinary        & Even, characteristic  & $(r_0 - 2,\, a_0 - 2,\, 1)$ & $(r_0 - 4,\, a_0 - 4,\, 0)$ \\
Even, characteristic  & Odd/simple            & $(r_0 - 2,\, a_0 - 2,\, 0)$ & $(r_0 - 4,\, a_0 - 2,\, 0)$ \\
Even, characteristic  & Even, ordinary        & $(r_0 - 2,\, a_0 - 2,\, 0)$ & $(r_0 - 4,\, a_0 - 4,\, 0)$ \\
Even, characteristic  & Even, characteristic  & $(r_0 - 2,\, a_0 - 2,\, 0)$ & $(r_0 - 4,\, a_0 - 4,\, 0)$ \\

\bottomrule \end{longtable}

Carrying out this algorithm for $F_{{\mathrm{En}}}$ shows that there are exactly two 1-cusps and two 0-cusps.
The following diagram encodes the mirror-move procedure, recording a sequence of moves starting from a primitive sublattice $S\hookrightarrow  {L_{\mathrm{K3}}} $, computing $T\mathrel{\mathop:}= S^{\perp  {L_{\mathrm{K3}}} }$, finding $\overline{T}$, the first type of boundary lattice corresponding to a 1-step mirror move (corresponding to \$0\$0-cusps) and finally finding $\overline{\overline{T}}$, the target of a 2-step mirror move.
We find that there are two possibilities for $\overline{T}$, indicated in the $\overline{T}$ column as $(10,10,0)_1$ and $(10, 8, 0)_1$, and two possibilities present in the $\overline{\overline{T}}$ column.
There are three 2-step paths through the diagram, but only two possibilities for $\overline{\overline{T}}$, yielding two $1$-cusps and two $0$-cusps.
We record the resulting cusp diagram below as well.

\begin{tikzpicture}[ scale=1.5, decoration=snake,
> =stealth, every arrow/.append style={line width=1.2pt}, every label/.append style={font=\Large}, white node/.style={ circle, draw=black, fill=white, inner sep=0pt, minimum size=8pt } ]

\node[white node] (p1) at (0, 0) {}; \node[white node] (p2) at (2, 0) {}; \node[white node] (p3) at (4, 2) {}; \node[white node] (p4) at (4, -2) {}; \node[white node] (p5) at (6, 0) {}; \node[white node] (p6) at (6, -2) {};

%\draw[shorten >= 0.2em, decorate] (p1) to (p2.west); \draw[-latex, shorten >= 0.4em] (p2) to (p3.west); \draw[-latex, shorten >= 0.4em, double] (p2) to (p4.west); \draw[-latex, shorten >= 0.4em, double] (p3) to (p5.west); \draw[-latex, shorten >= 0.4em] (p4) to (p5.west); \draw[-latex, shorten >= 0.4em, double] (p4) to (p6.west); \draw[-latex, decorate] (0.2,0) -- (1.8,0);

\node at (3.25, .75) {\Large $U$}; \node at (4.7, 0.75) {\Large $U(2)$}; \node at (3.25, -.75) {\Large $U(2)$}; \node at (4.7, -0.75) {\Large $U$}; \node at (4.7, -2.25) {\Large $U(2)$};

\node at (0, 3) {\Large $S$}; \node at (2, 3) {\Large $T$}; \node at (4, 3) {\Large $\overline{T}$}; \node at (6, 3) {\Large $\overline{\overline{T}}$};

\node at (-0.5, 0.5) {\large $(10, 10, 0)_1$}; \node at (1.5, 0.5) {\large $(12, 10, 0)_2$}; \node at (3.5, 2.5) {\large $(10, 10, 0)_1$}; \node at (3.5, -2.5) {\large $(10, 8, 0)_1$}; \node at (6.5, 0.5) {\large $(8, 8, 0)_0$}; \node at (6.5, -1.5) {\large $(8, 6, 0)_0$};

\end{tikzpicture} \resizebox{0.7\textwidth}{!}{% \begin{tikzpicture}[ square/.style={rectangle, draw, minimum size=1cm}, circ/.style={circle, draw, minimum size=0.8cm} ]

% Define nodes \node[square] (I1) at (0,0) {$I_1$}; \node[circ] (eta1) at (2,0) {$\eta_1$}; \node[square] (I12) at (4,0) {$I_{12}$}; \node[circ] (eta2) at (6,0) {$\eta_2$};

% Draw arrows \draw[->] (eta1) -- (I1); \draw[->] (eta1) -- (I12); \draw[->] (I12) -- (eta2);

\end{tikzpicture}% }
<!-- Source: 1-part-combinatorial/3-chapter-enriques-k3/475-our-cusps.md -->

### Enumeration of Baily--Borel 0-cusps via Diagram Folding

The boundary lattices at 0-cusps $\eta$ have the form $ \overline{T}*{ \eta  }  = \eta^\perp/\langle\eta\rangle$ for each primitive isotropic vector $\eta$.
The typical situation is two have some number $n$ of possible isometry classes for boundary lattices, and some number $m\geq n$ of *actual* boundary lattices, where $m$ depends on $\Gamma$, reflecting isometry classes splitting into further possibilities.
For $F*{(2,2,0)}$, there are two isometry classes, each containing one sub-type of lattice, so the two cusps can be labeled $$ \tilde\eta_1 \mathrel{\mathop:}= (18, 2, 0)*1, \qquad \tilde \eta_2 \mathrel{\mathop:}= (18, 0, 0)*1 .$$ For $F*{{\mathrm{En}}, 2}$, there are two isometry classes, one which does not split into further subclass corresponding to orbits of divisibility one vectors in $T*{{\mathrm{En}}}$, the other splitting into four sub-classes, reflecting an $\operatorname{O}(T_{{\mathrm{En}}})$ orbit of divisibility two vectors that splits into 4 separate orbits.
We label the cusps $\eta_1,\cdots, \eta_5$, and note that the two isometry classes are given by $$ \operatorname{div}*{T*{{\mathrm{En}}}}(\eta) = 1\colon (10, 10, 0)*1, \qquad \operatorname{div}*{T_{{\mathrm{En}}}}(\eta) = 2\colon (10, 8, 0)_1
$$

\begin{longtable}{L{3cm} L{4cm} L{4cm} L{4cm}}
\toprule
\textbf{$F_{{\mathrm{En}}, 2}$ Cusp} & \textbf{Covering $F_{(2,2,0)}$ Cusp} & \textbf{Diagram Involution} & \textbf{Folded Lattice} \\
\midrule
$\eta_1$ ($\operatorname{div}(\eta_1) = 1$) & $\tilde\eta_1 \mathrel{\mathop:}= (18,2,0)_1$ & $180^\circ$ rotation & $(10,10,0)_1$ \\
$\eta_2$ ($\operatorname{div}(\eta_2) = 2$) & $\tilde\eta_2 \mathrel{\mathop:}= (18,0,0)_1$ & Vertical reflection & $(10,8,0)_1$ \\
$\eta_3$ ($\operatorname{div}(\eta_3) = 2$) & $\tilde\eta_1 \mathrel{\mathop:}= (18,2,0)_1$ & Diagonal + root swap & $(10,8,0)_1$ \\
$\eta_4$ ($\operatorname{div}(\eta_4) = 2$) & $\tilde\eta_1 \mathrel{\mathop:}= (18,2,0)_1$ & Horizontal reflection & $(10,8,0)_1$ \\
$\eta_5$ ($\operatorname{div}(\eta_5) = 2$) & $\tilde\eta_1 \mathrel{\mathop:}= (18,2,0)_1$ & 8 commuting reflections & $(10,8,0)_1$ \\
\bottomrule
\end{longtable}
\todo{Check details}

### Cusps by Folding

Following (**AEGS23?**, Lemmas 3.10, 3.19), the five 0-cusps of the Baily--Borel compactification $\overline{F_{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$ correspond to five different involutions on the K3 lattice $T_{\operatorname{dP}}$.
Let \$ T \$ be an even indefinite lattice and let \$ \eta \in T \$ be a primitive isotropic vector.
Define the boundary lattice $ \overline{T}_{ \eta } \mathrel{\mathop:}= \eta^{\perp T} / \operatorname{gen}{\eta}$, which we will often simply write as $\overline{T} \mathrel{\mathop:}= \eta^{\perp}/\eta$ when working with a fixed vector $\eta$.
Write $\Phi(\overline{T})$ for the root system of $ \overline{T}_{ \eta } $. Let $\Gamma\leq \operatorname{O}(T)$ be a fixed arithmetic subgroup acting on $T$.For each such $\eta$, we write $U_\eta$ for the maximal unipotent subgroup of the stabilizer of $\eta$ in $\Gamma$ which acts trivially on $ \overline{T}_{ \eta } $. This group thus fits into an exact sequence
$$
0 \to U_\eta \to \operatorname{Stab}*\Gamma(\eta) \to \Gamma*{\eta} \to 0 .$$ We refer to $\Gamma_\eta$ as the **stable boundary group at $\eta$** and its corresponding reflection subgroup $W(\Gamma_\eta)$ as the **stable reflection group at $\eta$**. When $\Gamma = \operatorname{O}(T)$, we will write this as $W(\overline{T})$.
We write $ \mathfrak{C} ( \Gamma*\eta )$ for the corresponding fundamental chamber of $W(\Gamma*\eta)$, and \$ G( \Gamma\_\eta ) \$ for its Coxeter diagram.
When $ \overline{T}*{ \eta  } $ is hyperbolic, it is known that $\operatorname{O}( \overline{T}*{ \eta  } )$ is an extension of $W( \overline{T}*{ \eta  } )$ by a subgroup of chamber symmetries $\operatorname{Aut}(  \mathfrak{C} ( \Gamma*\eta ))$, and thus any diagram automorphism of $G(\Gamma_\eta)$ induces a chamber symmetry and thus an isometry of $ \overline{T}*{ \eta } $.
Let $J$ be an involution of $ \overline{T}*{ \eta } $, for example induced by an diagram involution on $G(\Gamma_\eta)$.
We then write $G( \Gamma_\eta )^{J}$ for the corresponding folded diagram, $ \mathfrak{C} ( \Gamma\_\eta )^J$ its folded fundamental chamber, and so on.

We recall the definitions $$ T_{{\mathrm{En}}} = U \oplus U(2) \oplus E_8(2) = (12,10,0)*2 \hookrightarrow T*{\operatorname{dP}} = U \oplus U(2) \oplus E_8^2 = (20, 2, 0)*2 ,$$ and write $I*{{\mathrm{En}}}, I_{\operatorname{dP}}$, and $I_{ {\mathrm{Nik}} }$ for the involutions on $ {L*{\mathrm{K3}}} $ induced by the geometric involutions $\iota*{{\mathrm{En}}}, \iota*{\operatorname{dP}}$, and $\iota*{ {\mathrm{Nik}} }$ respectively.
In the decomposition $ {L*{\mathrm{K3}}} = U^3 \oplus E_8^2$, these involutions can be written in block form as follows: $$\label{involution-lattice-block-forms} I*{\operatorname{dP}}:
\begin{pmatrix}
-1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 & 0 \\
0 & 0 & 0 & 0 & -1
\end{pmatrix},
\quad
I*{{\mathrm{En}}}:
\begin{pmatrix}
-1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & 0
\end{pmatrix},
\quad
I*{ {\mathrm{Nik}} }:
\begin{pmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & -1 \\
0 & 0 & 0 & -1 & 0
\end{pmatrix}
,$$ or as in \Cref{three-lattice-involutions}, `\begin{align*} I_{\operatorname{dP}}: (u_1,\ u_2,\ u_3,\ \alpha_1,\ \alpha_2) &\to (-u_1,\ u_3,\ u_2,\ -\alpha_1,\ -\alpha_2) \\ I_{{\mathrm{En}}}:(u_1,\ u_2,\ u_3,\ \alpha_1,\ \alpha_2) &\to (-u_1,\ u_3,\ u_2,\ \alpha_2,\ \alpha_1) \\ I_{ {\mathrm{Nik}} }:(u_1,\ u_2,\ u_3,\ \alpha_1,\ \alpha_2) &\to (u_1,\ u_2,\ u_3,\ -\alpha_2,\ -\alpha_1) \end{align*}{=tex} By (**AEGS23?**, Lem. 3.4), the coinvariant sublattice $T_{\operatorname{dP}}^{I_{{\mathrm{En}}} = -1} { \, \xrightarrow{\sim}\, }   T_{{\mathrm{En}}}$, and so to simplify matters we write $I \mathrel{\mathop:}= - I_{{\mathrm{En}}} = I_{ {\mathrm{Nik}} }$ and thus $T_{\operatorname{dP}}^{I} \mathrel{\mathop:}= T_{\operatorname{dP}}^{I=1} = T_{{\mathrm{En}}}$. Fixing a primitive isotropic vector $\eta \in T_{{\mathrm{En}}}$, we write $ \overline{T_{{\mathrm{En}}}}_{ \eta  }  \mathrel{\mathop:}= \eta^{\perp T_{{\mathrm{En}}}}/\left\langle \eta \right\rangle_{T_{{\mathrm{En}}}}$ and $ \overline{T_{\operatorname{dP}}}_{ \eta  }  \mathrel{\mathop:}= \eta^{\perp T_{\operatorname{dP}}}/\left\langle \eta \right\rangle_{T_{\operatorname{dP}}}$, and so on. Under the primitive embedding $T_{{\mathrm{En}}}\hookrightarrow T_{\operatorname{dP}}$, we can construct two distinct boundary lattices associated to $\eta$, [ ` \overline{T*{{\mathrm{En}}}}*{ \eta } \mathrel{\mathop:}= \eta\^{\perp T*{{\mathrm{En}}}}/\left\langle \eta \right\rangle, \qquad \overline{T*{\operatorname{dP}}}*{ \eta } \mathrel{\mathop:}= \eta\^{\perp T*{\operatorname{dP}}}/\left\langle \eta \right\rangle ,] where we carefully identify $\eta$ with its image in $T_{\operatorname{dP}}$ under the embedding.
There are two possible isometry classses possible for $ \overline{T*{\operatorname{dP}}}*{ \eta } $: $$ \overline{T*{\operatorname{dP}}}*{ \eta } :\quad (18, 2, 0)*1 = U(2) \oplus E_8^2 ,\quad \text{ or } \quad (18,0,0)\_1 = U \oplus E_8^2 ,$$ corresponding to the two 0-cusps of the Baily-Borel compactification $\overline{F*{(2,2,0)}}^{ \operatorname{BB} }$, and distinguished by the divisibility $\operatorname{div}*{T*{\operatorname{dP}}}(\eta)$ of $\eta$ in $T_{\operatorname{dP}}$.
From a similar analysis of $\overline{F_{{\mathrm{En}}}}^{ \operatorname{BB} }$, the moduli space of *unpolarized* Enriques surfaces, one finds that there are similarly two possibilities $$ \overline{T_{{\mathrm{En}}}}*{ \eta  } : \quad (10, 10, 0)*1 = U(2) \oplus E_8(2) ,\quad \text{ or } \quad (10,8,0)*1 = U \oplus E_8(2) .$$ Both possibilities for $ \overline{T*{\operatorname{dP}}}*{ \eta } $ are hyperbolic, 2-elementary lattices with induced involutions $\overline{I}*{{\mathrm{En}}}$ and $\overline{I}*{\operatorname{dP}}$, and if we write $J\mathrel{\mathop:}= -\overline{I}*{{\mathrm{En}}}$ then we recover $ \overline{T*{\operatorname{dP}}}*{ \eta } ^J = \overline{T*{{\mathrm{En}}}}*{ \eta } $ as the invariant sublattice.
We immediately note that the involution $J$ is highly sensitive to the choice of $\eta$, as are the isometry classes of $ \overline{T*{\operatorname{dP}}}*{ \eta } $ and thus $ \overline{T*{{\mathrm{En}}}}*{ \eta } $ -- in our situation, this highly depends on the geometry of the moduli spaces $F*{{\mathrm{En}}, 2}$ and $F*{(2,2,0)}$.
To make this dependence explicit, we define the arithmetic groups used to construct period domains for these spaces.
We define a distinguished polarization $$ h = e + f \in S_{\operatorname{dP}}  { \, \xrightarrow{\sim}\, }   U(2) \hookrightarrow S_{{\mathrm{En}}}  { \, \xrightarrow{\sim}\, }   U(2) \oplus E_8(2) = (10, 10, 0)*1 ,$$ and writing $\Psi: \operatorname{O}( {L*{\mathrm{K3}}} ) \to \operatorname{O}(T_{{\mathrm{En}}})$ for the restriction map, $$ \Gamma_{{\mathrm{En}}, 2} \mathrel{\mathop:}= \Psi\left( {\left\{{ g\in \operatorname{O}( {L_{\mathrm{K3}}} ) {~~\mathrel{\Big\vert}~~} g\circ I_{{\mathrm{En}}} = I_{{\mathrm{En}}}\circ g, \, g(h) = h }\right\}} \right), \qquad \Gamma_{\operatorname{dP}} \mathrel{\mathop:}= \operatorname{O}(T_{\operatorname{dP}}) ,$$ where we form $\Gamma_{{\mathrm{En}}, 2}$ by taking the intersection of the commutator of $I_{{\mathrm{En}}}$ in $\operatorname{O}( {L_{\mathrm{K3}}} )$, intersecting it with the stabilizer of the polarization, and taking the image in $\operatorname{O}(T_{{\mathrm{En}}})$.
This is the correct monodromy group for $F_{{\mathrm{En}}, 2}$; the full details can be found e.g. in (Sterk 1991). For any lattice $T$ of signature $(2, n)$, we define its period domain as $$ D_{T} \mathrel{\mathop:}=\left\{{ [v]\in {\mathbf{P}}(T_{\mathbf{C}}) {~~\mathrel{\Big\vert}~~} v^2 = 0, v\overline{v} > 0 }\right\}^\circ ,$$ where $({-})^\circ$ denotes taking one connected component.
We then define the two moduli spaces $$ F_{{\mathrm{En}}, 2} \mathrel{\mathop:}=  { D_{T} }/{ \Gamma } *{{\mathrm{En}}, 2}, \qquad F*{(2,2,0)} \mathrel{\mathop:}=  { D_{T} }/{ \Gamma } *{\operatorname{dP}} = D*{T}/\operatorname{O}(T_{\operatorname{dP}}) .$$ corresponding to degree 2 numerically polarized Enriques surfaces and quartic hyperelliptic K3 surfaces respectively.
To study the Baily-Borel compactification $\overline{F_{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$, we will be interested in $\Gamma_{{\mathrm{En}}, 2}$-orbits of primitive isotropic vectors $\eta_i$, which correspond to 0-cusps, and the Coxeter diagrams for the stable reflection groups $\Gamma_{{\mathrm{En}}, 2, \eta_i}$ at each $\eta_i$, which can be used to determine the 1-cusps and their adjacencies.
We note that if $\alpha\in \Phi(T_{\operatorname{dP}})$ is a (negative) root of $T_{\operatorname{dP}}$, then the folded root $\alpha_I$ is in $\Phi(T_{\operatorname{dP}}^I) = \Phi(T_{{\mathrm{En}}})$ and is thus a root of $T_{{\mathrm{En}}}$.
We can thus use the known stable reflection groups of $T_{\operatorname{dP}}$ at its known 0-cusps to study those of $T_{{\mathrm{En}}}$ and $\overline{T_{{\mathrm{En}}}}_{\eta_i}$ at each cusp $\eta_i$.
We analyze the structure of reflection groups and invariant lattices associated to each $0$-cusp $\eta_i$ on the moduli space, using the correspondence between the (negative) roots of the covering domain and its foldings.
The results are organized by cusp.

Let $\eta_1,\ldots,\eta_5$ denote the five distinguished $0$-cusps with the invariants, lattices, and automorphism relations as below.
Each case is presented precisely in a separate equation environment, as is standard for complex configurations that cannot be tabulated succinctly.

#### Cusp $\eta_1 = e$ (divisor $1$)

$$
\begin{aligned}
&\text{Transcendental lattice:} && (18,2,0)_1, \qquad U(2)\oplus E_8^2 \\
&\text{Automorphism: rotation by } 180^\circ: &&
\begin{cases}
\alpha_i \leftrightarrow \alpha_{8+i}, & i=0,\ldots,7 \\
\alpha_{16} \leftrightarrow \alpha_{18} \\
\alpha_{17} \leftrightarrow \alpha_{19}
\end{cases} \\
&\text{Invariants:} && (10,10,0)_1, \qquad U(2)\oplus E_8(2)
\end{aligned}
$$

#### Cusp $\eta_2 = e'$ (divisibility $2$)

$$
\begin{aligned}
&\text{Transcendental lattice:} && (18,0,0)_1, \qquad U\oplus E_8^2 \\
&\text{Automorphism: vertical reflection:} &&
\alpha_i \leftrightarrow \alpha_{20-i}, \quad i=1,\ldots,8 \\
&\text{Invariants:} && (10,8,0)_1, \qquad U\oplus E_8(2)
\end{aligned}
$$

#### Cusp $\eta_3 = e'+f'+\omega$, $\omega^2 = -4$ (divisibility $2$)

$$
\begin{aligned}
&\text{Transcendental lattice:} && (18,2,0)_1, \qquad U(2)\oplus E_8^2 \\
&\text{Automorphism: diagonal reflection:} &&
\begin{cases}
\alpha_i \leftrightarrow \alpha_{16-i}, & i=1,\ldots,7 \\
\alpha_{17} \leftrightarrow \alpha_{19} \\
s_{\alpha_{20}} \text{ fixes}
\end{cases} \\
&\text{Invariants:} && (10,8,0)_1, \qquad U\oplus E_8(2)
\end{aligned}
$$

#### Cusp $\eta_4 = e'+2f'+\alpha$, $\alpha^2 = -8$ (divisibility $2$)

$$
\begin{aligned}
&\text{Transcendental lattice:} && (18,2,0)_1, \qquad U(2)\oplus E_8^2 \\
&\text{Automorphism: horizontal reflection:} &&
\begin{cases}
\alpha_{14+i} \leftrightarrow \alpha_{14-i} \bmod 16 \\
\alpha_{19} \leftrightarrow \alpha_{16} \\
\alpha_{17} \leftrightarrow \alpha_{18} \\
\alpha_{20} \leftrightarrow \alpha_{21}
\end{cases} \\
&\text{Invariants:} && (10,8,0)_1, \qquad U\oplus E_8(2)
\end{aligned}
$$

#### Cusp $\eta_5 = 2e + 2f + \alpha$, $\alpha^2 = -8$ (divisibility $2$)

$$
\begin{aligned}
&\text{Transcendental lattice:} && (18,2,0)_1, \qquad U(2)\oplus E_8^2 \\
&\text{Automorphism:}\ 8\ \text{reflections:} && s_{\alpha_{2i+1}},\quad i=0,\ldots,7 \\
&\text{Invariants:} && (10,8,0)_1, \qquad U\oplus E_8(2)
\end{aligned}
$$

#### The main cusp correspondence

In this section, we record the cusp diagrams of the main moduli spaces of interest: $F_{(2,2,0)}$ and $F_{{\mathrm{En}}, 2}$.
The cusp diagram for $F_{(2,2,0)}$ is shown below, which can be found in (Alexeev and Engel 2022) or reconstructed using the mirror move algorithm.
The boundary lattices for $F_{(2,2,0)}$ at its two 0-cusps are $(18,0,0)*1$ and $(18,2,0)*1$.
The cusps, their Coxeter diagrams, and the KSBA compactification $ \overline{F*{(2,2,0)}} $ were analyzed in detail in (Alexeev and Engel 2022, 10). Consider the Enriques transcendental lattice [ T*{{\mathrm{En}}} \mathrel{\mathop:}= U \oplus U(2) \oplus E*8(2) .] The classification of ${\Gamma*{{\mathrm{En}}, 2}} $-orbits of primitive isotropic vectors in $T*{{\mathrm{En}}}$ provides an enumeration of the 0-cusps in the Baily--Borel compactification of $F*{{\mathrm{En}}, 2}$.
we know by (Sterk 1991) what the five 0-cusps $\eta_1,\cdots, \eta_5$ of $\overline{F_{{\mathrm{En}}, 2}}^{ \operatorname{BB} }$ are, as well as their stable reflection groups, Coxeter diagrams, and the associated 1-cusps.
We collect below some of the lattice-theoretic calculations that will be relevant to showing that folding methods can be used to recover this data.
The following shows the cusp diagram for $F_{{\mathrm{En}}, 2}$, where we note that the mirror move algorith does *not* apply, since it only determines cusps when $\Gamma$ is the full stable orthogonal group.
We can instead appeal to (Sterk 1991), who computed these cusps and their incidences in their entirety.
In the diagram below, we recapitulate these incidences, adding new information: recalling if $D$ is a $G$-space and $H\leq G$ is a subgroup, the chain of subgroups $1\hookrightarrow H\hookrightarrow G$ induces a chain of surjective morphisms $D\twoheadrightarrow  {D}/{H} \twoheadrightarrow  {D}/{G} $.
Thus there is a chain of maps $D_{T_{{\mathrm{En}}}}\to F_{{\mathrm{En}}, 2}\to F_{{\mathrm{En}}}$, and we can consider the images of the cusps of $F_{{\mathrm{En}}, 2}$ in $F_{{\mathrm{En}}}$ as well as their images in $F_{(2,2,0)}$.

\begin{figure}[H] \centering \vspace\*{\fill} \begin{tikzpicture}[ square/.style={rectangle, draw, minimum width=2.5cm, minimum height=0.8cm}, highlighted_square/.style={rectangle, draw, minimum width=2.5cm, minimum height=0.8cm, fill=blue!15}, circ/.style={circle, draw, minimum size=0.8cm}, highlighted_circ/.style={circle, draw, minimum size=0.8cm, fill=blue!15} ]

% Define column positions - centered and properly spaced \def\colZero{0} \def\colOne{2.5} \def\colTwo{5.5} \def\colThree{8.5} \def\colFour{11.5}

% === NEW VERTICAL STRUCTURE === % Column 0: Vertical arrangement aligned with colored circle \node[highlighted_square] (I1new) at (\colZero,5.5) {$I_1$}; \node[highlighted_circ] (eta1new) at (\colZero,4) {$\eta_1$}; \node[square] (I12new) at (\colZero,2.5) {$I_{12}$}; \node[circ] (eta2new) at (\colZero,1) {$\eta_2$};

% Arrows for vertical structure \draw[->] (eta1new) -- (I1new); \draw[->] (eta1new) -- (I12new); \draw[->] (I12new) -- (eta2new);

% === UPPER DIAGRAM === % Column 1: Left circle \node[circ] (eta2top) at (\colOne,2) {$\eta_2$}; \node[above=0.3cm of eta2top] {$U \oplus E_8(2)$};

% Column 2: Middle squares (connected to left circle) \node[highlighted_square] (L1top) at (\colTwo,2.5) {$I_{1,2}: E_8^2$}; \node[square] (L2top) at (\colTwo,1.5) {$I_{2,4,5}: D_{16}^+$};

% Column 3: Four circles \node[highlighted_circ] (eta1top) at (\colThree,4) {$\eta_1$}; \node[circ] (eta3top) at (\colThree,2.7) {$\eta_3$}; \node[circ] (eta4top) at (\colThree,1.3) {$\eta_4$}; \node[circ] (eta5top) at (\colThree,0) {$\eta_5$}; \node[above=0.3cm of eta1top] {$U(2) \oplus E_8(2)$};

% Column 4: Seven squares \node[highlighted_square] (R1top) at (\colFour,5) {$I_{1,3}: E_7^2 C_2$}; \node[highlighted_square] (R2top) at (\colFour,4) {$I_{1,4}: D_8^2$}; \node[highlighted_square] (R3top) at (\colFour,3) {$I_{1,5}: A_{15} A_1(2)$}; \node[square] (R4top) at (\colFour,2) {$I_{3,4}: A_{15} A_1(2)$}; \node[square] (R5top) at (\colFour,1) {$I_{3,5}: D_{12} D_4$}; \node[square] (R6top) at (\colFour,0) {$I_{4,5}: D_8^2$}; \node[square] (R7top) at (\colFour,-1) {$I_{5}: E_7^2 C_2$};

% Arrows for upper diagram % From column 1 to column 2 \draw[->] (eta2top.east) -- (L1top.west); \draw[->] (eta2top.east) -- (L2top.west);

% From column 3 to column 2 \draw[->, blue!50, thick] (eta1top.west) -- (L1top.east); \draw[->] (eta4top.west) -- (L2top.east); \draw[->] (eta5top.west) -- (L2top.east);

% From column 3 to column 4 \draw[->, blue!50, thick] (eta1top.east) -- (R1top.west); \draw[->, blue!50, thick] (eta1top.east) -- (R2top.west); \draw[->, blue!50, thick] (eta1top.east) -- (R3top.west); \draw[->] (eta3top.east) -- (R1top.west); \draw[->] (eta3top.east) -- (R4top.west); \draw[->] (eta3top.east) -- (R5top.west); \draw[->] (eta4top.east) -- (R2top.west); \draw[->] (eta4top.east) -- (R4top.west); \draw[->] (eta4top.east) -- (R6top.west); \draw[->] (eta5top.east) -- (R3top.west); \draw[->] (eta5top.east) -- (R5top.west); \draw[->] (eta5top.east) -- (R6top.west); \draw[->] (eta5top.east) -- (R7top.west);

% === LOWER DIAGRAM (shifted down) === \def\lowerShift{-5}

% Column 1: Left circle \node[circ] (eta1bot) at (\colOne,\lowerShift) {$\eta_1$}; \node[below=0.3cm of eta1bot] {$U \oplus E_8^2$};

% Column 2: Middle squares \node[square] (L1bot) at (\colTwo,\lowerShift+0.5) {$I_{1,2}: E_8^2$}; \node[square] (L2bot) at (\colTwo,\lowerShift-0.5) {$I_{1,2}: D_{16}$};

% Column 3: Right circle \node[circ] (eta2bot) at (\colThree,\lowerShift) {$\eta_2$}; \node[below=0.3cm of eta2bot] {$U(2) \oplus E_8^2$};

% Column 4: Six squares \node[square] (R1bot) at (\colFour,\lowerShift+2.5) {$I_2: D_5^2$}; \node[square] (R2bot) at (\colFour,\lowerShift+1.5) {$I_2: E_7^2 C_2$}; \node[square] (R3bot) at (\colFour,\lowerShift+0.5) {$I_2: E_8 D_8$}; \node[square] (R4bot) at (\colFour,\lowerShift-0.5) {$I_2: D_{12} D_4$}; \node[square] (R5bot) at (\colFour,\lowerShift-1.5) {$I_2: D_{16}$}; \node[square] (R6bot) at (\colFour,\lowerShift-2.5) {$I_2: A_{15} A_1(2)$};

% Arrows for lower diagram % From column 1 to column 2 \draw[->] (eta1bot.east) -- (L1bot.west); \draw[->] (eta1bot.east) -- (L2bot.west);

% From column 3 to column 2 \draw[->] (eta2bot.west) -- (L1bot.east); \draw[->] (eta2bot.west) -- (L2bot.east);

% From column 3 to column 4 \draw[->] (eta2bot.east) -- (R1bot.west); \draw[->] (eta2bot.east) -- (R2bot.west); \draw[->] (eta2bot.east) -- (R3bot.west); \draw[->] (eta2bot.east) -- (R4bot.west); \draw[->] (eta2bot.east) -- (R5bot.west); \draw[->] (eta2bot.east) -- (R6bot.west);

% Add horizontal separator line and connecting arrows \draw[gray, dotted, thick] (-1,-1.75) -- (14,-1.75); \draw[gray, dotted, thick] (1.25,7) -- (1.25,-8);

% Blue dashed arrows with proper spacing from nodes \draw[->, dashed, blue, thick, shorten >=0.5em, shorten <=0.5em] (eta5top.south) -- (eta2bot.north); \draw[->, dashed, blue, thick, shorten >=0.5em, shorten <=0.5em] (eta2top.south) -- (eta1bot.north); \draw[->, dashed, blue, thick, shorten >=0.5em, shorten <=0.5em] (eta1top.west) -- (eta1new.east);

% Main labels \node[above=8em of eta2top, xshift=5em] {\Huge $F_{{\mathrm{En}}, 2}$}; \node[below=4em of eta1bot, xshift=5em] {\Huge $F_{(2,2,0)}$}; \node[below=2em of eta2new] {\Huge $F_{{\mathrm{En}}}$};

\end{tikzpicture} \vspace\*{\fill} \end{figure}

We briefly describe the methods that go into finding these cusps, due to (Sterk 1991). The following result appears as (Sterk 1991, Cor.\~3.3), and generalized the Eichler transvection method:

:::{#thm:orbit-classification-sterk .theorem title="{Orbit Classification in $T = U \\oplus \ \overline{T}
_{ \\eta  } $ ([@Ste91, Cor.~3.3]) }"}
Fix an even lattice $T$ with a splitting $T = U \oplus  \overline{T}_{ \eta  } $ with $\overline{T}$ negative--definite and even.\
Let $\eta_1,\;\eta_2\;\in T$ be primitive isotropic vectors satisfying

1.  $\eta_1^2=\eta_2^2=k$;\
2.  $\operatorname{div}_T(\eta_1)=\operatorname{div}_T(\eta_2)=p>0$ (so $(\eta_i,T)=p\Bbb Z$);\
3.  $\eta_1\equiv \eta_2\pmod{pT}$.

Then there exists an isometry $\phi \in \operatorname{O}^*(T)$ such that $\phi(\eta_1) = \eta_2$.
In particular, $\eta_1$ and $\eta_2$ lie in the same $\operatorname{O}^*(T)$-orbit.
:::

:::{.proof title="Sketch"}
The idea is to let $\eta_i = a_i e + b_i e + c_i$ where $c_i\in  \overline{T}_{ \eta  } $, and then put both $\eta_i$ into normal form.
Sterk shows that you can arrange for $\eta_1\cdot e = p$, so $a_1 = 0, b_1 = p$ by some $g\in \operatorname{O}^*(T)$, and that you can arrange for $\eta_2\cdot e =p$ simultaneously, so $a_2=0,v_2=p$.
Thus $$
\eta_1 = pe + c_1, \eta_2 = pe + c_2, \qquad \eta_1 f = \eta_2 f = p
.$$ One then checks that $$\eta_1 \equiv_{p T}\eta_2 \implies \eta_1 - \eta_2 \in pT \implies c_1 - c_2 = pc \in p \overline{T}_{ \eta  } $$ by canceling the now-identical $pf$ components, and writes $$\eta_1 - \eta_2 = pc \implies \eta_1 = \eta_2 + pc, \qquad c\in  \overline{T}_{ \eta  } .$$

Constructing the Siegel-Eichler transvection $$E_{f, c}(x) = x - (x, f)c + \left( (x, c) - {1\over 2}c^2 (x, f)\right)f,$$ one finds that

`\begin{align*}
E_{f, c}(\eta_1) 
&\equiv_{{\mathbf{Z}} f} \eta_1 - (\eta_1, f)c  \\
&\equiv_{{\mathbf{Z}} f} (pe+ c_1) - pc  \\
&\equiv_{{\mathbf{Z}} f} (pe+ c_1) - (c_1 - c_2)  \\
&\equiv_{{\mathbf{Z}} f} pe + c_2  \\
&\equiv_{{\mathbf{Z}} f} \eta_2 \\
.\end{align*}`{=tex} Writing $\eta_1 = \eta_2 + \lambda  f$, one concludes by checking that $$
k = \eta_1^2 = E_{f, c}(\eta_1)^2 = (\eta_2 + \lambda f)^2 = \eta^2 + 2\lambda (\eta_2, f) + \lambda^2 f^2 = k + 2\lambda p
,$$ forcing $\lambda=0$ and $\eta_1 = \eta_2$.
:::

We then find that all divisibility one vectors are in the same orbit:

:::{.proposition title="{ [@Ste91, Lem. 4.2.1] }
"}
If $\operatorname{div}_{T_{{\mathrm{En}}}}(v)=1$, then $v \sim_{{\Gamma_{{\mathrm{En}}, 2}}  } v_{1} \mathrel{\mathop:}= e \in U$.
:::

:::
proof
We apply \Cref{orbit-classification-sterk}: since

- $v^{2}=e^{2}=0$,
- $\operatorname{div}_{T_{{\mathrm{En}}}}(v)=\operatorname{div}_{T_{{\mathrm{En}}}}(e)=1$, and
- $v \equiv e \bmod T_{{\mathrm{En}}}$,

we have $v \sim_{\operatorname{O}^{*}\left(T_{{\mathrm{En}}}\right)} e$ and thus $v \sim_{{\Gamma_{{\mathrm{En}}, 2}} } e$.
:::

The divisibility two vectors require a slightly finer analysis, but this quickly reduces to studying the large (but finite) discriminant group $A_{T_{{\mathrm{En}}}}$: (Sterk 1991, \S. 4.2.2)first uses the fact that there is a decomposition $$A_{T_{{\mathrm{En}}}} = A\oplus B \mathrel{\mathop:}= {1\over 2}U/U \oplus {1\over 2}E_8/E_8$$ and if $\operatorname{div}*{T*{{\mathrm{En}}}}(\eta) = k \geq 2$ then $\eta/k \in T_{{\mathrm{En}}} {}^{ \vee }$ induces a nontrivial class in $A_{T_{{\mathrm{En}}}}$.
Any such class can be written as $g = a + b$ with $a\in A, b\in B$ and $q(g) = q_A(a) + q_B(b)$.
If $q(g) = 0\pmod{2{\mathbf{Z}}}$, there are exactly two possibilities:

1. $q_A(a) = q_B(b) = 0$, or
2. $q_A(a) = q_B(b) = 1$.

In the first case, one checks that the possibilities are $$a = 0, \quad {1\over 2}e', \quad {1\over 2}f', \qquad b = 0, \quad {1\over 2}\alpha, \quad \alpha\in E_8(2), \,\,\alpha^2 = -8,$$ using explicit computations for $U(2)$ and known facts about $E_8(2)$, and one can immediately rule out ${1\over 2}f'$ up to stable isometries.
In the second case, one has $$a = {1\over 2}(e' + f'), \qquad b = {1\over 2}\omega,\quad \omega\in E_8(2),\,\, \omega^2 = -4.$$ This gives five possibilities, only four of which are new, which admit explicit lifts that are shown to be inequivalent under the action of $\Gamma_{{\mathrm{En}}, 2}$: $$ A_T: \begin{cases} 0 &\\
{1\over 2}e' &\\
{1\over 2}\alpha & (\alpha^2 = -8) \\
{1\over 2}e' + {1\over 2}\alpha & (\alpha^2 = -8) \\
{1\over 2}e' + {1\over 2}f' + {1\over 2}\omega & (\omega^2 = -4) \end{cases} \qquad\leadsto\,\, T: \begin{cases} e &\\
e' &\\
2e + 2f + \alpha \quad &(\alpha^2 = -8) \\
e' + 2f' + \alpha \quad &(\alpha^2 = -8) \\
e' + f' + \omega \quad &(\omega^2 = -4) \end{cases}

$$

Sterk then shows that under the full isometry group $\operatorname{O}(T_{{\mathrm{En}}})$, the four divisibility-two orbits collapse to a single orbit, and the divisibility-one orbit remains unique. Therefore, up to $O(T_{{\mathrm{En}}})$, there are exactly two orbits of primitive isotropic vectors, partially affirming the know cusp diagram of $F_{{\mathrm{En}}}$ shown in the previous section.

#### Folded Coxeter Diagrams

We now describe---in precise terms following (**AEGS23?**) -- how the Coxeter diagrams for the 0-cusps of $F_{{\mathrm{En}}, 2}$ are obtained by folding the Coxeter diagrams for the 0-cusps of the related quartic hyperelliptic K3 moduli $F_{(2,2,0)}$ under the involution $I = -I_{{\mathrm{En}}}$. Recall there are two $\operatorname{O}(T_{\operatorname{dP}})$-orbits of primitive isotropic vectors in $T_{\operatorname{dP}}$, associated to the boundary lattices $(18,2,0)_1 = U(2)\oplus E_8^2$ and $(18,0,0)_1 = U\oplus E_8^2$. Each determines a *Coxeter diagram* encoding the walls of the fundamental chamber for the stable reflection group. The five 0-cusps of $F_{{\mathrm{En}}, 2}$ correspond to five distinct orbits of primitive isotropic vectors in $T_{{\mathrm{En}}}$ (Sterk), and each is *realized as a folded image* of one of the K3 diagrams under the involution.
The fundamental fact is that the set of simple roots defining the faces of the Coxeter chamber are determined by \Cref{lem-which-roots-descend} The *folded chamber* for the reflection group in $T_{{\mathrm{En}}}$ is the intersection
$$
\mathfrak{C} ^I =  \mathfrak{C}  \cap \overline{T}*{ \eta, {\mathbf{R}}  } ^{I = 1} $$ where $ \mathfrak{C} $ is the Coxeter chamber for $T*{\operatorname{dP}}$, yielding a fundamental chamber for the reflection group in $T_{{\mathrm{En}}}$ whose faces correspond to the roots described above.
Simple roots fixed by $I$ correspond to cases 1 and 2 above, and pass directly to the folded diagram as roots of the same norm.
Pairs of simple $(-2)$-roots swapped by the involution $I$ and orthogonal to their images, i.e. $I(\alpha) \in \alpha^{\perp}$, are "averaged" into a new $(-4)$-root wall of the folded diagram.
Moreover, every wall of the folded chamber, and hence every boundary divisor at each 0-cusp of $F_{{\mathrm{En}}, 2}$, arises by this procedure.
Maximal *parabolic subdiagrams* of the K3 diagrams invariant under $I$ (i.e., unions of nodes fixed or swapped under $I$ as above) yield, upon folding, the parabolic subdiagrams of the Enriques diagram, which can thus be used to find the 1-cusps and complete the full cusp diagram.

To summarize, the five Coxeter diagrams for the five 0-cusps of $F_{{\mathrm{En}}, 2}$ are obtained by explicit folding of the diagrams $G(18,2,0)$ and $G(18,0,0)$ of $F_{(2,2,0)}$ under $I$.
This process precisely matches Sterk's list: each 0-cusp boundary lattice in $T_{{\mathrm{En}}}$ is the fixed lattice under $I$ of the appropriate K3 boundary lattice for $T_{\operatorname{dP}}$, and the combinatorics of simple roots and walls are gotten by descending them from $T_{\operatorname{dP}}$ under the involution.
Moreover, each Coxeter diagram for each 0-cusp of $F_{{\mathrm{En}}, 2}$ arises from an explicit involution on a Coxeter diagram for $F_{(2,2,0)}$, which we list below.
In each diagram, a folding symmetry is defined by a combination of blue arrows and crossed out red nodes.
Each folding involution is strictly speaking an element of $\operatorname{O}( \Phi(T) )$ for an appropriate lattice $T$, which decmoposes as the semidirect product of a reflection group and a subgroup of diagram symmetries, as described above.
We can thus specify *some* isometries of $\Phi(T)$ by combining elements from each factor.
In these diagrams, the blue decorations indicate isometries taken from the group of diagram symmetries, while red crossed-out nodes indicate elements taken from the Weyl group.
Explicitly, in each case we have:

1. A counter-clockwise rotation by $\pi$,
2. A left-to-right reflection about the center,
3. A reflection about the line $y=x$, supposing the bottom-left node is at $(0, 0)$ in the plane,composed with a reflection in a single root,
4. A top-to-bottom reflection about the center, and
5. A composition of commuting reflections in 8 simple roots.

\resizebox{\linewidth}{!}{% \begin{tikzpicture}[ scale=0.8, % Coxeter-Vinberg diagram styles normal edge/.style={line width=1pt}, thick edge/.style={line width=2pt}, doubled edge/.style={double, line width=0.8pt, double distance=1.5pt}, dotted edge/.style={dotted, line width=1pt}, white node/.style={circle, fill=white, draw=black, line width=1pt, inner sep=2pt}, black node/.style={circle, fill=black, inner sep=2pt}, % Define a doubled white node style for even-numbered exterior nodes doubled node/.style={circle, fill=white, draw=black, line width=1pt, inner sep=3pt, path picture={\draw[black, line width=1pt] (path picture bounding box.center) circle (2pt);}}
]

% Declare layers \pgfdeclarelayer{background} \pgfdeclarelayer{foreground} \pgfsetlayers{background,main,foreground}

% Define macros for each cusp type \newcommand{\cuspone}[2]{ \begin{scope}[shift={(#1,#2)}] % Square perimeter nodes \node[black node] at (0,0) {}; \node[black node] at (2,0) {}; \node[black node] at (4,0) {}; \node[black node] at (4,2) {}; \node[black node] at (4,4) {}; \node[black node] at (2,4) {}; \node[black node] at (0,4) {}; \node[black node] at (0,2) {}; % Diagonal nodes \node[black node] at (1,1) {}; \node[black node] at (2,2) {}; \node[black node] at (3,3) {};

```
\begin{pgfonlayer}{background}
\draw[normal edge] (0,0) -- (2,0) -- (4,0) -- (4,2) -- (4,4) -- (2,4) -- (0,4) -- (0,2) -- (0,0);
\draw[normal edge] (0,0) -- (1,1);
\draw[normal edge] (3,3) -- (4,4);
\draw[thick edge] (1,1) -- (2,2) -- (3,3);
\end{pgfonlayer}
\end{scope}
```
}

\newcommand{\cusptwo}[2]{ \begin{scope}[shift={(#1,#2)}]

```
% Define triangle corners to match cusptwocover precisely
\coordinate (A) at (0,0);    % bottom left
\coordinate (B) at (4,0);    % bottom right
\coordinate (C) at (2,4);    % top

% Calculate positions along edges (same as cusptwocover)
\foreach \i in {0,1,...,5} {
    \pgfmathsetmacro{\t}{\i/5}
    \coordinate (bottom\i) at ($(A)!\t!(B)$);
}

\foreach \i in {0,1,...,6} {
    \pgfmathsetmacro{\t}{\i/6}
    \coordinate (right\i) at ($(B)!\t!(C)$);
}

\foreach \i in {0,1,...,6} {
    \pgfmathsetmacro{\t}{\i/6}
    \coordinate (left\i) at ($(C)!\t!(A)$);
}

% Only keep nodes 10-19 from cusptwocover
% Node 10 at top (white, even -> doubled)
\node[white node] (n10) at (right6) {};

% Nodes 11-15 on left edge (now black)
\node[black node] (n11) at (left1) {};
\node[black node] (n12) at (left2) {};
\node[black node] (n13) at (left3) {};
\node[black node] (n14) at (left4) {};
\node[black node] (n15) at (left5) {};

% Nodes 16-18 on bottom edge (now black)
\node[black node] (n16) at (bottom0) {};
\node[black node] (n17) at (bottom1) {};
\node[black node] (n18) at (bottom2) {};

% Interior node 19 (now black)
\coordinate (interior19) at ($(A)!0.3!(B)!0.2!(C)$);
\node[black node] (n19) at (interior19) {};

\begin{pgfonlayer}{background}
% Edges: path 11-12-13-14-15-16-17-18 and edge 16-19
\draw[normal edge] (n11) -- (n12) -- (n13) -- (n14) -- (n15) -- (n16) -- (n17) -- (n18);
\draw[normal edge] (n16) -- (n19);

% Double edge 10-11 (white to black)
\draw[doubled edge] (n10) -- (n11);
\end{pgfonlayer}

\end{scope}
```
}

\newcommand{\cuspthree}[2]{ \begin{scope}[shift={(#1,#2)}] % White nodes \node[white node] (white_bl) at (0,0) {}; \node[white node] (white_tr) at (4,4) {}; % Black nodes \node[black node] (a1) at (0,1) {}; \node[black node] (a2) at (0,2) {}; \node[black node] (a3) at (0,3) {}; \node[black node] (a4) at (0,4) {}; \node[black node] (b4) at (1,4) {}; \node[black node] (c4) at (2,4) {}; \node[black node] (d4) at (3,4) {}; \node[black node] (b3) at (1,3) {}; \node[black node] (diag1) at (1.33,1.33) {}; \node[black node] (diag2) at (2.67,2.67) {};

```
\begin{pgfonlayer}{background}
\draw[normal edge] (a4) -- (b4) -- (c4) -- (d4);
\draw[normal edge] (a1) -- (a2) -- (a3) -- (a4);
\draw[normal edge] (a4) -- (b3);
\draw[thick edge] (diag1) -- (diag2);
\draw[doubled edge] (d4) -- (white_tr);
\draw[doubled edge] (a1) -- (white_bl);
\draw[doubled edge] (white_bl) -- (diag1);
\draw[doubled edge] (white_bl) -- (diag2);
\draw[doubled edge] (diag2) -- (white_tr);
\end{pgfonlayer}
\end{scope}
```
}

\newcommand{\cuspfour}[2]{ \begin{scope}[shift={(#1,#2)}] % External nodes \node[white node] (w_left) at (0,2) {}; \node[black node] (bl_4) at (0,3) {}; \node[black node] (bl_5) at (0,4) {}; \node[black node] (b1_5) at (1,4) {}; \node[black node] (b2_5) at (2,4) {}; \node[black node] (b3_5) at (3,4) {}; \node[black node] (b4_5) at (4,4) {}; \node[black node] (br_4) at (4,3) {}; \node[white node] (w_right) at (4,2) {}; % Internal arms \node[black node] (arm_left) at (1,3) {}; \node[black node] (arm_right) at (3,3) {};

```
\begin{pgfonlayer}{background}
\draw[normal edge] (bl_5) -- (b1_5) -- (b2_5) -- (b3_5) -- (b4_5);
\draw[normal edge] (bl_4) -- (bl_5);
\draw[normal edge] (b4_5) -- (br_4);
\draw[doubled edge] (bl_4) -- (w_left);
\draw[doubled edge] (br_4) -- (w_right);
\draw[normal edge] (bl_5) -- (arm_left);
\draw[normal edge] (b4_5) -- (arm_right);
\end{pgfonlayer}
\end{scope}
```
}

\newcommand{\cuspfive}[2]{ \begin{scope}[shift={(#1,#2)}] % Outer square \node[black node] (b00) at (0,0) {}; \node[black node] (b20) at (2,0) {}; \node[black node] (b40) at (4,0) {}; \node[black node] (b42) at (4,2) {}; \node[black node] (b44) at (4,4) {}; \node[black node] (b24) at (2,4) {}; \node[black node] (b04) at (0,4) {}; \node[black node] (b02) at (0,2) {}; % White nodes \node[white node] (w11) at (1,1) {}; \node[white node] (w31) at (3,1) {}; \node[white node] (w33) at (3,3) {}; \node[white node] (w13) at (1,3) {}; % Interior black nodes \node[black node] (interior1) at (2,1.6) {}; \node[black node] (interior2) at (2,2.4) {};

```
\begin{pgfonlayer}{background}
\draw[normal edge] (b00) -- (b20) -- (b40) -- (b42) -- (b44) -- (b24) -- (b04) -- (b02) -- (b00);
\draw[doubled edge] (b00) -- (w11);
\draw[doubled edge] (b40) -- (w31);
\draw[doubled edge] (b44) -- (w33);
\draw[doubled edge] (b04) -- (w13);
\draw[thick edge] (interior1) -- (interior2);
\draw[doubled edge] (w11) -- (interior2);
\draw[doubled edge] (w31) -- (interior1);
\draw[doubled edge] (w13) -- (interior1);
\draw[doubled edge] (w33) -- (interior2);
\end{pgfonlayer}
\end{scope}
```
}

\newcommand{\cuspsix}[3][true]{ \begin{scope}[shift={(#2,#3)}] % Outer square - even numbered nodes get double circles \node[doubled node] (b00) at (0,0) {};    % node 0 \node[white node] (b10) at (1,0) {};           % node 1 \node[doubled node] (b20) at (2,0) {};    % node 2 \node[white node] (b30) at (3,0) {};           % node 3 \node[doubled node] (b40) at (4,0) {};    % node 4 \node[white node] (b41) at (4,1) {};           % node 5 \node[doubled node] (b42) at (4,2) {};    % node 6 \node[white node] (b43) at (4,3) {};           % node 7 \node[doubled node] (b44) at (4,4) {};    % node 8 \node[white node] (b34) at (3,4) {};           % node 9 \node[doubled node] (b24) at (2,4) {};    % node 10 \node[white node] (b14) at (1,4) {};           % node 11 \node[doubled node] (b04) at (0,4) {};    % node 12 \node[white node] (b03) at (0,3) {};           % node 13 \node[doubled node] (b02) at (0,2) {};    % node 14 \node[white node] (b01) at (0,1) {};           % node 15 % Interior white nodes (same positions as cusp 5) \node[white node] (w11) at (1,1) {};           % node 16 \node[white node] (w31) at (3,1) {};           % node 17 \node[white node] (w33) at (3,3) {};           % node 18 \node[white node] (w13) at (1,3) {};           % node 19 % Interior black nodes (same as cusp 5) \node[black node] (interior1) at (2,1.6) {};  % node 21 \node[black node] (interior2) at (2,2.4) {};  % node 20

```
\begin{pgfonlayer}{background}
% Outer perimeter with all the new nodes
\draw[normal edge] (b00) -- (b10) -- (b20) -- (b30) -- (b40) -- (b41) -- (b42) -- (b43) -- (b44) -- (b34) -- (b24) -- (b14) -- (b04) -- (b03) -- (b02) -- (b01) -- (b00);
% Connections from corners to interior white nodes (doubled edges since white-to-white)
\draw[doubled edge] (b00) -- (w11);
\draw[doubled edge] (b40) -- (w31);
\draw[doubled edge] (b44) -- (w33);
\draw[doubled edge] (b04) -- (w13);
% The barbell in the middle
\draw[thick edge] (interior1) -- (interior2);
% Connections from interior white nodes to barbell (doubled edges since white-to-black)
\draw[doubled edge] (w11) -- (interior2);
\draw[doubled edge] (w31) -- (interior1);
\draw[doubled edge] (w13) -- (interior1);
\draw[doubled edge] (w33) -- (interior2);
\end{pgfonlayer}

% Add labels - simplified conditional
\def\showlabels{#1}
\ifx\showlabels\undefined
    \cuspsixlabels
\else
    \def\truevalue{true}
    \ifx\showlabels\truevalue
        \cuspsixlabels
    \fi
\fi
\end{scope}
```
}

% Helper macro for cuspsix labels \newcommand{\cuspsixlabels}{ \node[below left] at (0,-0.08) {\tiny 0}; \node[below] at (1,-0.08) {\tiny 1}; \node[below] at (2,-0.08) {\tiny 2}; \node[below] at (3,-0.08) {\tiny 3}; \node[below right] at (4,-0.08) {\tiny 4}; \node[right] at (4.08,1) {\tiny 5}; \node[right] at (4.08,2) {\tiny 6}; \node[right] at (4.08,3) {\tiny 7}; \node[above right] at (4,4.08) {\tiny 8}; \node[above] at (3,4.08) {\tiny 9}; \node[above] at (2,4.08) {\tiny 10}; \node[above] at (1,4.08) {\tiny 11}; \node[above left] at (0,4.08) {\tiny 12}; \node[left] at (-0.08,3) {\tiny 13}; \node[left] at (-0.08,2) {\tiny 14}; \node[left] at (-0.08,1) {\tiny 15}; \node[above] at (0.85,1.15) {\tiny 16}; \node[above] at (3,1.15) {\tiny 17}; \node[below] at (3,2.85) {\tiny 18}; \node[below] at (1,2.85) {\tiny 19}; \node[above] at (2,2.5) {\tiny 20}; \node[below] at (2,1.5) {\tiny 21}; }

\newcommand{\cusptwocover}[2]{ \begin{scope}[shift={(#1,#2)}]

```
% Define triangle corners to match the scale of other diagrams
\coordinate (A) at (0,0);    % bottom left
\coordinate (B) at (4,0);    % bottom right
\coordinate (C) at (2,4);    % top

% Define how many nodes on each edge
\def\bottomnodes{6}  % nodes 16,17,18,2,3,4
\def\rightnodes{7}   % nodes 4,5,6,7,8,9,10
\def\leftnodes{7}    % nodes 10,11,12,13,14,15,16

% Calculate positions along bottom edge A to B
\foreach \i in {0,1,...,5} {
    \pgfmathsetmacro{\t}{\i/5}
    \coordinate (bottom\i) at ($(A)!\t!(B)$);
}

% Calculate positions along right edge B to C
\foreach \i in {0,1,...,6} {
    \pgfmathsetmacro{\t}{\i/6}
    \coordinate (right\i) at ($(B)!\t!(C)$);
}

% Calculate positions along left edge C to A
\foreach \i in {0,1,...,6} {
    \pgfmathsetmacro{\t}{\i/6}
    \coordinate (left\i) at ($(C)!\t!(A)$);
}

% Place perimeter nodes with automatic styling based on node number
% Bottom edge: 16,17,18,2,3,4
\node[doubled node] (n16) at (bottom0) {};
\node[white node] (n17) at (bottom1) {};
\node[doubled node] (n18) at (bottom2) {};
\node[doubled node] (n2) at (bottom3) {};
\node[white node] (n3) at (bottom4) {};
\node[doubled node] (n4) at (bottom5) {};

% Right edge: 5,6,7,8,9,10 (skip 4 as it's already placed)
\node[white node] (n5) at (right1) {};
\node[doubled node] (n6) at (right2) {};
\node[white node] (n7) at (right3) {};
\node[doubled node] (n8) at (right4) {};
\node[white node] (n9) at (right5) {};
\node[doubled node] (n10) at (right6) {};

% Left edge: 11,12,13,14,15 (skip 10 and 16 as already placed)
\node[white node] (n11) at (left1) {};
\node[doubled node] (n12) at (left2) {};
\node[white node] (n13) at (left3) {};
\node[doubled node] (n14) at (left4) {};
\node[white node] (n15) at (left5) {};

% Interior nodes at computed positions
\coordinate (interior1) at ($(A)!0.7!(B)!0.2!(C)$);  % node 1
\coordinate (interior19) at ($(A)!0.3!(B)!0.2!(C)$); % node 19

\node[white node] (n1) at (interior1) {};
\node[white node] (n19) at (interior19) {};

% Labels with consistent spacing using coordinate offsets
\node[below left] at ($(bottom0) + (-0.08,-0.08)$) {\tiny 16};
\node[below] at ($(bottom1) + (0,-0.08)$) {\tiny 17};
\node[below] at ($(bottom2) + (0,-0.08)$) {\tiny 18};
\node[below] at ($(bottom3) + (0,-0.08)$) {\tiny 2};
\node[below] at ($(bottom4) + (0,-0.08)$) {\tiny 3};
\node[below right] at ($(bottom5) + (0.08,-0.08)$) {\tiny 4};
\node[right] at ($(right1) + (0.08,0)$) {\tiny 5};
\node[right] at ($(right2) + (0.08,0)$) {\tiny 6};
\node[right] at ($(right3) + (0.08,0)$) {\tiny 7};
\node[right] at ($(right4) + (0.08,0)$) {\tiny 8};
\node[right] at ($(right5) + (0.08,0)$) {\tiny 9};
\node[above] at ($(right6) + (0,0.08)$) {\tiny 10};
\node[left] at ($(left1) + (-0.08,0)$) {\tiny 11};
\node[left] at ($(left2) + (-0.08,0)$) {\tiny 12};
\node[left] at ($(left3) + (-0.08,0)$) {\tiny 13};
\node[left] at ($(left4) + (-0.08,0)$) {\tiny 14};
\node[left] at ($(left5) + (-0.08,0)$) {\tiny 15};
\node[above] at ($(interior1) + (-0.08,0)$) {\tiny 1};
\node[above] at ($(interior19) + (0.08,0)$) {\tiny 19};

\begin{pgfonlayer}{background}
% Path 2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18
\draw[normal edge] (n2) -- (n3) -- (n4) -- (n5) -- (n6) -- (n7) -- (n8) -- (n9) -- (n10) -- (n11) -- (n12) -- (n13) -- (n14) -- (n15) -- (n16) -- (n17) -- (n18);

% Additional edges
\draw[normal edge] (n16) -- (n19);
\draw[normal edge] (n1) -- (n4);
\end{pgfonlayer}

\end{scope}
```
}

% Draw first row \cuspone{0}{0} \cusptwo{5}{0} \cuspthree{10}{0} \cuspfour{15}{0} \cuspfive{20}{0}

% Cover diagrams with additional visual elements % Cover 1: cuspsix with counterclockwise rotation arrows \cuspsix{0}{6} \begin{scope}[shift={(0,6)}] % Circular arc with arrow indicating 180° counterclockwise rotation \draw[->, blue, line width=0.5pt,dashed] (2,2) ++(-0.9,0) arc[start angle=-180, end angle=-0, radius=0.9]; \draw[->, blue, line width=0.5pt, dashed] (2,2) ++(0.9,0) arc[start angle=0, end angle=180, radius=0.9]; \end{scope}

% Cover 2: cusptwocover with vertical reflection line \cusptwocover{5}{6} \begin{scope}[shift={(5,6)}] % Vertical dotted line through center \draw[dotted, thick, blue] (2,-0.5) -- (2,4.2); % Horizontal double arrow indicating reflection \draw[<->, thick, blue] (1.4,2) -- (2.6,2); \end{scope}

% Cover 3: cuspsix with diagonal reflection and red X on node 20 \cuspsix{10}{6} \begin{scope}[shift={(10,6)}] % Diagonal line from bottom-left to top-right \draw[thick,dashed,blue] (-0.2,-0.2) -- (4.2,4.2); % Diagonal double arrow (northwest to southeast) \draw[<->, thick, blue] (1.5,3.5) -- (3.5,1.5); % Red X over node 20 (interior2 at (2,2.4)) \draw[red, very thick, line width=1pt] (2,2.4) ++(-0.15,-0.15) -- ++(0.3,0.3); \draw[red, very thick, line width=1pt] (2,2.4) ++(-0.15,0.15) -- ++(0.3,-0.3); \end{scope}

% Cover 4: cuspsix with horizontal reflection line \cuspsix{15}{6} \begin{scope}[shift={(15,6)}] % Horizontal line cutting diagram in half \draw[thick, blue, dashed] (0,2) -- (4,2); % Vertical double arrow indicating reflection \draw[<->, thick, blue] (2.5,0.75) -- (2.5,3.25); \end{scope}

% Cover 5: cuspsix with red X over odd-numbered perimeter nodes \cuspsix{20}{6} \begin{scope}[shift={(20,6)}] % Red X over odd-numbered nodes: 1,3,5,7,9,11,13,15 \foreach \x/\y in {1/0,3/0,4/1,4/3,3/4,1/4,0/3,0/1} { \draw[red, very thick, line width=1pt] (\x,\y) ++(-0.15,-0.15) -- ++(0.3,0.3); \draw[red, very thick, line width=1pt] (\x,\y) ++(-0.15,0.15) -- ++(0.3,-0.3); } \end{scope}

% Labels for first row (cusps) and second row (covers) \foreach \i/\name in {0/1,5/2,10/3,15/4,20/5} { \node[below] at (\i+2,-0.5) {Cusp \name}; \node[above] at (\i+2,10.5) {Cover \name}; }

% Labels - only for first row (main/bottom row) \node[below] at (2,-0.5) {Cusp 1}; \node[below] at (7,-0.5) {Cusp 2}; \node[below] at (12,-0.5) {Cusp 3}; \node[below] at (17,-0.5) {Cusp 4}; \node[below] at (22,-0.5) {Cusp 5};

\end{tikzpicture}% }
<!-- Source: 2-part-moduli/000-part-2.md -->

# Compactifications and Integral Affine Structures {#part-2}

Let \$ D \$ be a Hermitian symmetric domain of type IV, such as the domains $D_{T}$ arising from indefinite lattices of signature $(2, n)$, and and \$ \Gamma \$ be an arithmetic subgroup of $\operatorname{Aut}(D)$, e.g. an arithmetic subgroup of $\operatorname{O}(T)$.
The typical compactifications of \$ F_\Gamma = \Gamma \backslash D \$ include the Baily--Borel compactification $\overline{F_\Gamma}^{ \operatorname{BB} }$, toroidal compactifications $ \overline{F_\Gamma}^{  \Sigma *{\bullet} } $, semitoroidal compactifications $\overline{F*\Gamma}^{  \mathcal{F} *{\bullet} }$, and the KSBA compactification $ \overline{F*\Gamma} $.
Discussions of the following material can be found in (Scattone 1987), (Ash et al. 1975), (Baily and Borel 1966), (Farkas and Morrison 2013), (Janos Kollár and Mori 1998).

The Baily Borel compactification \$ \overline{F_\Gamma}^{ \operatorname{BB} } \$ is defined as \$ \operatorname{Proj},A(\Gamma) \$, where \$ A(\Gamma) \$ is the graded \$ {\mathbf{C}} \$-algebra of automorphic forms for \$ \Gamma \$.
It is a projective, normal variety, and is canonical in the sense that it does not depend on any auxiliary choices.
It is the unique *minimal* geometric compactification in the following sense: for any other normal, projective compactification \$ X \$ of \$ F_\Gamma \$ admitting an extension of the period map, there exists a unique, regular, projective morphism \$ X \to \overline{F_\Gamma}^{ \operatorname{BB} } \$ restricting to the identity on \$ F_\Gamma \$.
The boundary \$ \partial\overline{F_\Gamma}^{ \operatorname{BB} } \$ consists of finitely many strata, each itself a quotient of a Hermitian symmetric domain by an arithmetic group, and is described via rational boundary components indexed by maximal rational parabolics subgroups of $\operatorname{Aut}(D)$.
However, the boundary is generally of high codimension and almost never divisorial for Type ${\textrm{IV}}$ domains, for whic it is generically comprised of only points and modular curves.
The analytic structure at the boundary is highly singular and generally not even ${\mathbf{Q}}$-factorial.
Moreover, boundary points typically do not correspond to moduli of degenerate surfaces.
However, $\overline{F_\Gamma}^{ \operatorname{BB} }$ is functorial and canonical, and the representaiton-theoretic nature of the boundary components often reduces their study to combinatorics and lattice theory.

Toroidal compactifications \$  \overline{F_\Gamma}^{  \Sigma *{\bullet} }  \$ are defined by refining the structure near the cusps of $\overline{F*\Gamma}^{ \operatorname{BB} }$.
For each cusp, one chooses an admissible rational polyhedral fan in a particuar cone at that cusp.
The result is a proper algebraic variety with a divisorial boundary which is locally toric.
The construction is highly non-canonical, and depends on the choice of fans, of which there are typically infinitely many.
Different choices give different, though birationally equivalent, compactifications, all mapping to $\overline{F_\Gamma}^{ \operatorname{BB} }$.
The boundary \$ \partial  \overline{F_\Gamma}^{  \Sigma *{\bullet} }  \$, after potentially a refinement of fans and a finite cover, is a snc divisor.
Each boundary component is constructed from tori associated to unipotent radicals $U_P$ of rational parabolic subgroups $P$ of $\Gamma \leq \operatorname{Aut}(D)$.
The fibers of the canonical morphism $ \overline{F*\Gamma}^{  \Sigma *{\bullet} } \to \overline{F*\Gamma}^{ \operatorname{BB} }$ over boundary strata are toric.
The boundary singularities are typically milder than in $\overline{F_\Gamma}^{ \operatorname{BB} }$, and for well-chosen admissible decompositions, is is possible to construct smooth compactifications.
Moreover, toroidal compactifications often allow the extension of period maps and universal families over boundary strata, yielding a much stronger modular interpretation than $\overline{F_\Gamma}^{ \operatorname{BB} }$.

Semitoroidal compactifications, introduced by Looijenga (see (Looijenga 1985)), are useful when $\overline{F_\Gamma}^{ \operatorname{BB} }$ is insufficient, but a full toroidal compactification $ \overline{F_\Gamma}^{  \Sigma *{\bullet} } $ is unnecessary or obstructed, or there are no particularly canonical choice of the necessary toric fan data.
While $\overline{F*\Gamma}^{ \operatorname{BB} }$ has boundary components of codimension typically at least 2 and toroidal compactifications $ \overline{F_\Gamma}^{  \Sigma *{\bullet} } $ *fully* refine all cusps to divisorial components, semitoroidal compactifications only partially "toroidalize" along a subset of boundary strata.
They thus allow individual cusps to be differentiated, some being fully toroidal, and others being only partially toroidal, hence the name *semitoroidal*. Formally, choose a subset \$ {\mathcal{S}} \$ of boundary strata in \$ \overline{F*\Gamma}^{ \operatorname{BB} } \$ and assign, for each \$ F \in {\mathcal{S}} \$, an admissible rational polyhedral decomposition (i.e. a *semifan*) in the relevant cone at that cusp.
One then performs a blowup up only along these loci, glues in toroidal models over \$ {\mathcal{S}} \$, and leave other strata untouched.
The boundary is divisorial along those strata \$ F \in {\mathcal{S}} \$, but retains higher codimension strata elsewhere.
The construction is not canonical, since there are still infinitely many choices of both semitoric data at each cusp.
There are still natural projective morphisms [  \overline{F_\Gamma}^{  \Sigma *{\bullet} }  \longrightarrow \overline{F*\Gamma}^{  \mathcal{F} *{\bullet} } \longrightarrow \overline{F*\Gamma}^{ \operatorname{BB} } ] restricting to the identity on the open locus \$ F_\Gamma \$, yielding a compactification birationally equivalent to all toroidal compactifications.
By (**AE21?**, Thm.
5.14) the semitoroidal compactifications are *precisely* the compactifications fitting into such a tower.
Such compactifications are particularly effective when compactifying Type ${\textrm{IV}}$domains, and often admit extensions of period maps and (partial) universal families over the cusps.

The KSBA compactification $ \overline{F_\Gamma} $ (see (**KSBA?**)) arises from the (log) minimal model program (MMP), for varieties of log general type.
For a moduli problem, e.g., polarized varieties or stable pairs, one seeks a modular compactification where points correspond to geometric degenerations: namely, stable slc pairs $(X,D)$ with prescribed numerical invariants and $K_X + D$ ample.
One defines a functor and forms the moduli stack of such pairs; by properness of the moduli functor (see (J. Kollár and Shepherd-Barron 1988; Alexeev 1996) ), one obtains a proper algebraic space and that compactifies the moduli stack of smooth pairs.
The resulting **KSBA moduli space** $ \overline{F_\Gamma} $ includes boundary divisors corresponding to *all* possible stable degenerations, including those not visible at the level of period domains or other methods for locally symmetric spaces.
The boundary is divisorial, though possibly reducible and singular, and every 1-parameter family over a DVR of smooth surfaces admits, possibly after a base-change, a unique stable limit.
Universal families exist over open subsets, and a coarse moduli interpretation is valid everywhere.
When a period map exists (e.g. when there is an established Torelli theorem), there is a regular but not generally finite morphism $ \overline{F_\Gamma}  \to\overline{F_\Gamma}^{ \operatorname{BB} }$ and $ \overline{F_\Gamma} $ is generally the finest among all of the compactifications discussed.
In general, these maps contract or identify bounday components, and only in very particular cases is even close to an isomorphism over the boundary, making the main theorem particularly surprising.
To summarize, the typical situation is the following:

\begin{tikzcd}
 \overline{F_\Gamma}^{  \Sigma _{\bullet} }  \arrow[d] &  \overline{F_\Gamma}  \arrow[ddl] \\
\overline{F_\Gamma}^{  \mathcal{F} _{\bullet} } \arrow[d] & \\
\overline{F_\Gamma}^{ \operatorname{BB} } &
\end{tikzcd}

However, in situations such as $F_{{\mathrm{En}}, 2}$, the canonical morphism $\overline{F_\Gamma}\to \overline{F_\Gamma}^{ \operatorname{BB} }$ lifts to an isomorphism $ \overline{F_\Gamma}   { \, \xrightarrow{\sim}\, }   \overline{F_\Gamma}^{  \mathcal{F} _{\bullet} }$ for a proper choice of semifans ${\mathcal{F}}$.

<!-- Source: 2-part-moduli/4-chapter-cpt/000-ksba.md -->

## Compactifications {#chapter-5}

### Comparing Compactifications

Given a smooth projective family of varieties ${\mathcal{X}} \rightarrow \Delta$ over the unit disk with ${\mathcal{X}}_0$ ${\mathcal{X}}_0$ a simple normal crossings (SNC) divisor, the Clemens--Schmid exact sequence provides a powerful tool to analyze the limit mixed Hodge structure on the cohomology of the general fiber.
This sequence, however, depends on the presence of semistable (SNC) reduction, and in general, no analogous sequence or description is known when the total space ${\mathcal{X}}$ is itself singular or the ${\mathcal{X}}*0$ has worse singularities.
\todo{Note: Clemens LES FAILS when semistable reduction is not available?} To systematically handle degenerating families of higher-dimensional varieties -- where semistable reduction is either inadequate or inapplicable -- Kollár and Shepherd-Barron introduced the theory of stable slc pairs (J. Kollár and Shepherd-Barron 1988). In this framework, a **stable pair** consists of a projective variety $X$ (possibly reducible and with mild singularities) together with a ${\mathbf{Q}}$-divisor $D$ such that $K_X + D$ is ample and ${\mathbf{Q}}$-Cartier, and the pair $(X, D)$ has semi log canonical (slc) singularities.
This generalizes the definition of stable curves from the classical Deligne--Mumford compactification $\overline{{\mathcal{M}} }*g$ to all dimensions, and stable slc pairs provide a modular, proper, algebraic compactification of moduli spaces of varieties and pairs.
For moduli of K3 surfaces, this leads to the **KSBA compactification**: for a moduli space $F*{2d}$ of degree $2d$ polarized K3 surfaces, and for a suitable **recognizable** divisor $R$ on a generic such surface, one studies the closure of the locus of pairs $(X, \varepsilon R)$ (for sufficiently small $\varepsilon > 0$) in the moduli space of all KSBA stable pairs, sometimes referred to as *slc pairs* in the relevant literature.
For example, for a degree two polarized K3 surface $(X, L)$, the linear system $|L|$ gives a double cover $X \rightarrow {\mathbf{P}}^2$ branched along a sextic, and $R$ can be chosen as the ramification divisor for the covering involution.
When $R$ is recognizable, there exists a semifan $ \mathcal{F} *R$ so that the normalization of the KSBA compactification $ \overline{F*{2d}} $ is isomorphic to the corresponding **semitoroidal compactification** $\overline{F*{2d}}^{ \mathcal{F} _R}$.
The precise construction of such semifans is highly nontrivial and depends on the geometry of the polarization.

Drawing an analogy with the Deligne--Mumford compactification of ${\mathcal{M}}_g$, one obtains the following procedure for families of surfaces: after base change and birational modifications, any family ${\mathcal{X}} \to \Delta$ of surfaces can be replaced by a semistable model, that is, with ${\mathcal{X}}$ smooth and the ${\mathcal{X}}_0$ ${\mathcal{X}}_0$ a reduced snc divisor.
One then contracts $(-1)$-curves in the fibers to obtain a relatively minimal model with smooth total space.
To construct a stable model, one further contracts all $(-2)$-curves in the fibers; this produces a family whose total space is typically singular, but whose ${\mathcal{X}}_0$ is uniquely determined and has at worst nodal singularities.
This uniqueness (up to isomorphism), together with the finiteness of the automorphism group and the ampleness of the dualizing sheaf, are the properties which extend to higher dimensional varieties.
Recall that a divisor $D$ on a normal variety $X$ has simple normal crossings (snc) if, in a Zariski neighborhood of every point, its support is defined by the vanishing of a product of coordinate functions.
A log pair $(X,D)$ is said to be **divisorial log terminal** (dlt) if there exists an open subset $U \subseteq X$ such that $D|_U$ has snc support, and for any divisorial valuation $E$ centered in $X \setminus U$, the log discrepancy $a(E,X,D)>-1$.
A **KSBA-stable pair** is a pair $(X, D=\sum b_j D_j)$ where $X$ is a projective demi-normal variety (that is, $X$ satisfies Serre's condition $S_2$ and has normal crossing singularities in codimension $1$), the divisorial components $D_j$ are effective Weil divisors of $X$ not contained in the singular locus of $X$, and the coefficients $b_j$ are rational numbers with $0 < b_j < 1$, such that:

1. The divisor $K_X + D$ is ample and ${\mathbf{Q}}$-Cartier.
2. The pair $(X, D)$ has semi log canonical (slc) singularities

<!-- see [Kollár, *Singularities of the Minimal Model Program*, Cambridge, 2013, Definition 5.10]). -->

This notion generalizes the stability condition for curves: for $X$ a nodal curve and $D = \sum b_j p_j$ a divisor with $0 < b_j < 1$, the pair $(X, D)$ is KSBA stable if and only if $X$ is stable in the sense of Deligne--Mumford.
The KSBA compactification provides a canonical and proper compactification of the moduli space of varieties and pairs of log general type by allowing stable pairs $(X, D)$ with semi log canonical singularities and ample $K_X + D$.
As a consequence, these moduli spaces are proper and projective, and their construction is compatible with the minimal model program.

<!-- see [Kollár, *Moduli of varieties of general type*, in: *Handbook of Moduli*, vol. II (2013), 131–157, arXiv:1008.0621], [@Alexeev, *Comp. Math.* 112 (1998), 147–182], [Kollár–Shepherd-Barron, *J. Algebraic Geom.* 1 (1992), 429–479]. -->
<!-- see (Kollár–Shepherd-Barron–Alexeev) compactification, as constructed in [Kollár–Shepherd-Barron, *J. Algebraic Geom.* 1 (1992), 429–479], [@Alexeev, *Comp. Math.* 112 (1998), 147–182], and [Kollár, *Moduli of varieties of general type*, Handbook of Moduli, vol. II, 2013 (arXiv:1008.0621)],  -->

### Recognizable Divisors

Let $F_S$ be the moduli space of $S$-polarized K3 surfaces, and let $R$ be a canonical ample divisor on the generic surface in $F_S$.
The divisor $R$ is called **recognizable** (for $F_S$) if for any $S$-quasipolarized Kulikov degeneration ${\mathcal{X}} \to \Delta$, there exists a divisor $R_0 \subset {\mathcal{X}}_0$ such that, for any other smoothing $\tilde{{\mathcal{X}}} \to \Delta$ with ${\mathcal{X}}_0$ $\tilde{{\mathcal{X}}}*0$, the divisor $R_0$ is, up to the connected component of the identity $\operatorname{Aut}^0(\tilde{{\mathcal{X}}}*0)$, the unique flat limit of the divisors $R_t \subset {\mathcal{X}}*t$ as $t \to 0$.This yields a form of uniqueness and "path-independence" for Kulikov models, namely that $R$ extends unambiguously to all boundary components of $F_S$.
For any choice of recognizable divisor, the normalization of the KSBA stable pair compactification $ \overline{F} ^R$ is a semitoroidal compactification of the period domain, with the semifan determined by $R$.
A canonical example of a recognizable divisor comes from (Alexeev and Engel 2023), who compactify the moduli spaces $F*{2d}$ of polarized K3 surfaces $(X, L)$ of degree $2d$.
The **rational curve divisor** is the formal sum $R*\mathrm{rc}$ of all smooth genus zero curves in the linear system $\abs{L}$: [ R\_\mathrm{rc} \mathrel{\mathop:}=  \sum\_{i=1}\^{n_d} R_i \in \|n_d L\| ] where each $R_i$ is an irreducible rational curve and $n_d$ is given by the *Yau--Zaslow* formula, see e.g. (Alexeev and Engel 2023, Thm.
10.2). In loc.cit., this divisor is shown to be recognizable for all $d$, and thus there are semifans such that $\overline{F*{2d}}^{  \mathcal{F} *{\bullet} } \cong  \overline{F*{2d}} $.
The proof uses the Kontsevich moduli space of stable maps, Gromov-Witten invariants, and properties of rational stable maps to surfaces with K-trivial degenerations.

This follows a similar line of work: for $F_2$, see (**AET19?**), and for degree 2 elliptic K3 surfaces $F_{ \mathrm{ell} } $, see (Alexeev, Brunyate, and Engel 2022). These are $S$-polarized K3 surfaces for $S$ a 2-elementary lattice that primitively embeds in $ {L_{\mathrm{K3}}} $, of which there are exactly 75 by (Nikulin 1979b), and (**AE23b?**, Thm.
9.10) handles the remaining cases, including $F_{(2,2,0)}$ corresponding to $S = U(2) = (2,2,0)*1$, using the fact that such surfaces carry a nonsymplectic involution $\iota$ whose ramification divisor $R*\iota$ is recognizable.
For $50$ of these cases, there is a similar theorem as \Cref{main-theorem}: $\overline{F_S}^{  \mathcal{F} *{\bullet} }  { \, \xrightarrow{\sim}\, }    \overline{F_S} $ for a semifan associated to $R*\iota$ -- they are precisely the closures of irreducible components on which monodromy invariants $\lambda$ maintain a fixed *combinatorial type*(**AE21?**).\
By passing to Kulikov models with nonsymplectic involutions, they show that stable limits can be constructed using the fact that the ${\mathcal{X}}_0$ ${\mathcal{X}}*0 = \cup_i V_i$ of Type ${\textrm{II}}$ Kulikov models ${\mathcal{X}}$ of K3 surfaces admit dual complexes $\Gamma({\mathcal{X}}*0)$ homeomorphic to $S^2$, which can naturally be equipped with integral affine structures, yielding an $\iota$-symmetric $\mathrm{IAS}^2$, where $\iota$ typically acts on $S^2$ by $(x,y,z)\mapsto (x,y,-z)$ in the standard coordinates on ${\mathbf{R}}^3$.
Thus one can reverse-engineer this procedure, starting with a model for a hemisphere of $S^2$ which is homeomorphic to $\mathbf{D}^2$, and realizing $S^2 \cong \mathbf{D}^2 \bigsqcup*{\partial \mathbf{D}^2} \mathbf{D}^2$ as the pushout of two discs along their boundaries, naturally enforcing $\iota$-invariance.
The process starts from a *monodromy invariant* $\lambda$ encoding a degeneration, then constructs an integral-affine polygon $P(\lambda)$ in ${\mathbf{R}}^2$ with singularities, performing Symington surgeries on $P(\lambda)$ that encode the degeneration.
Passing to a complete triangulation and taking the pushout $B(\lambda) \mathrel{\mathop:}=  P(\lambda) \bigsqcup*{\partial P(\lambda)} (-P(\lambda))$, where $-P(\lambda)$ denotes reversing the orientation, yields an $\mathrm{IAS}^2$.

From this, one can construct a *$d$-semistable Kulikov surface* such that $B(\lambda) \cong \Gamma({\mathcal{X}}_0(\lambda) )$, which by (Friedman 1983b) smooths to K3 surface ${\mathcal{X}}*t \mathrel{\mathop:}= {\mathcal{X}}*t(\lambda)$ and thus specifies a family ${\mathcal{X}} \mathrel{\mathop:}= {\mathcal{X}}(\lambda)$.
One extends the induced involution $\iota$ on $mcx_0$ to ${\mathcal{X}}$, passes to a carefully chosen divisorial component of the ramification divisor $R*\iota$\$ on ${\mathcal{X}}$ and performs modifications to obtain a pair $(X,\varepsilon R) \mathrel{\mathop:}= (X(\lambda), \varepsilon R(\lambda))$.
One then shows that the limit of $R*\iota$ is big and nef and thus defines a contraction $\pi: (X, \varepsilon R) \to (\overline{X}, \varepsilon \overline{R})$ to a KSBA stable pair There is a decomposition $X = \cup_i ( V_i, D_i)$ into irreducible components indexed by the lattice points in $B(\lambda)$, each of which forms an anticanonical pair, and so we can write $(X, \varepsilon R) = \cup_i ((V_i, D_i), \varepsilon R_i)$, which contracts under $\pi$ to a decomposition $(\overline{X}, \varepsilon \overline{R}) = \cup_i ( (\overline{V}_i, \overline{D}_i ), \varepsilon \overline{R}_i )$ of the stable model.
Tracing this construction backwards, we thus access the irreducible components of the stable model by understanding how the contraction $\pi$ combinatorially acts at the level of $B(\lambda) = \Gamma({\mathcal{X}}_0)$, and in particular how the contraction acts on individual anticanonical pairs $(V_i, D_i)$.
By analogy, we seek a similar method of studying Enriques surfaces.

<!-- Source: 2-part-moduli/4-chapter-cpt/100-baily-borel.md -->

### The Baily-Borel Compactification

#### Hermitian Symmetric Domains and Arithmetic Quotients

Let $G$ be a connected, simple linear algebraic group defined over ${\mathbf{Q}}$ and fix a maximal compact subgroup $K \subset G({\mathbf{R}})$.
The quotient $D = G({\mathbf{R}})/K$ is an irreducible symmetric space.
This data defines a **Riemannian symmetric space** $(G,K)$ with a decomposition of the Lie algebra of $G({\mathbf{R}})$: [ {\mathfrak{g}} = {\mathfrak{k}} \oplus {\mathfrak{p}} ,] where ${\mathfrak{p}}$ is the orthogonal complement to ${\mathfrak{k}}$ for an invariant symmetric bilinear form $\beta$ on ${\mathfrak{g}}$.
These spaces frequently arise in moduli problems: for an arithmetic subgroup $\Gamma \subset G({\mathbf{Q}})$ acting properly discontinuously on $D \mathrel{\mathop:}= G/K$, the quotient $ { D }/{ \Gamma } $ is a locally symmetric space.
It can be expressed as the double coset space $$ F_\Gamma \mathrel{\mathop:}=  { D }/{ \Gamma }  \cong \Gamma \backslash G / K = \left\{{ \Gamma g K {~~\mathrel{\Big\vert}~~} g \in G }\right\} ,$$ which is a typically a non-proper, quasi-projective complex variety parameterizing representation-theoretic data such as Hodge structures of a fixed type.
Such symmetric spaces $(G,K)$ are classified by the restriction of $\beta$:

- **Euclidean type**: $\left.\beta\right|_{{\mathfrak{p}}} = 0$,

- **Compact type**: $\left.\beta\right|_{{\mathfrak{p}}} < 0$ (negative definite),

- **Non-compact type**: $\left.\beta\right|_{{\mathfrak{p}}} > 0$ (positive definite).

For non-compact types, $D$ is a **Hermitian symmetric domain** (HSD): a non-compact, irreducible symmetric space with a $G({\mathbf{R}})$-invariant complex structure and Hermitian metric.
All Hermitian symmetric domains can be realized as bounded domains in ${\mathbf{C}}^n$ via the **Harish-Chandra embedding**. They admit a classification due to Cartan; the non-exceptional types are:

* * *
Type        Standard Description                                Realization as Homogeneous Space
* * *
I$_{p,q}$   Complex Grassmannian of $p$-dimensional subspaces   $\operatorname{SU}(p,q)/S(\operatorname{U}(p)\times\operatorname{U}(q))$

II$_n$      Lagrangian Grassmannian (orthogonal type)           $\operatorname{SO}^*(2n)/\operatorname{U}(n)$

III$_n$     Siegel upper half space (symplectic type)           $\operatorname{Sp}(n,{\mathbf{R}})/\operatorname{U}(n)$

## IV$_n$      Period domain                                       $\operatorname{O}(2,n)/(\operatorname{O}(2)\times\operatorname{O}(n))$

##### Type I

Type ${\textrm{I}}$domains arise as quotients $D_{p,q}^{{\textrm{I}}} = \operatorname{SU}(p,q)/S(\operatorname{U}(p)\times\operatorname{U}(q))$ where $p\leq q$, and consist of $p$-dimensional positive subspaces in ${\mathbf{C}}^{p+q}$ with respect to the Hermitian form [ h(z,w) = z_1 \overline{w}*1 + \cdots + z_p \overline{w}*p - z*{p+1} \overline{w}*{p+1} - \cdots - z\_{p+q} \overline{w}\_{p+q}. ] A fundamental example is the **complex upper half-plane**, $\mathbb{H} = \left\{ \tau \in {\mathbf{C}}: \Im(\tau) > 0 \right\} \cong \operatorname{SL}_2({\mathbf{R}})/\operatorname{SO}(2)$.
The action of $\operatorname{SL}_2({\mathbf{Z}})$ (or congruence subgroups $\Gamma\leq \operatorname{SL}*2({\mathbf{Z}})$) on $\mathbb{H}$ via Möbius transformations [ \gamma \cdot \tau = \frac{a\tau + b}{c\tau + d},\quad \gamma = \matt abcd \in \Gamma ] gives rise to the **modular curves** $Y*\Gamma = \Gamma \backslash \mathbb{H}$, which are coarse moduli spaces for elliptic curves with level structure.

##### Type ${\textrm{III}}$

Type ${\textrm{III}}$ domains take the form $D_g^{{\textrm{III}}} = \operatorname{Sp}*g({\mathbf{C}})/\operatorname{U}*g$ and consist of $g\times g$ symmetric complex matrices $Z$ whose imaginary part is positive definite -- otherwise known as the **Siegel upper half space**, $$ \mathbb{H}*g = \{ Z \in M*{g\times g}({\mathbf{C}}){~~\mathrel{\Big\vert}~~}  Z^t = Z,\, \Im(Z) > 0 \} .$$ The group $\operatorname{Sp}*{2g}({\mathbf{Z}})$ acts by [ \gamma \cdot Z = (AZ + B)(CZ + D)\^{-1},\quad \gamma = \matt ABCD \in \operatorname{Sp}\_{2g}({\mathbf{Z}} ) ,] producing a coarse moduli space for complex principally polarized abelian varieties: $  \mathcal{A}*{g}  = \operatorname{Sp}_{2g}({\mathbf{Z}})\backslash \mathbb{H}*g$.
For genus $g > 1$, via the Torelli map, the moduli space of curves $  \mathcal{M}*{g}$ embeds as an open subset of a suitable arithmetic quotient of a Siegel space.

##### Type IV

Type ${\textrm{IV}}$domains are open subsets of quadric surfaces defined as [ D_{T} \mathrel{\mathop:}=\left\{{ [v]\in {\mathbf{P}}(T_{\mathbf{C}}) {~~\mathrel{\Big\vert}~~} v^2 = 0, v\overline{v} > 0 }\right\}\^\circ ] where $L$ is a lattice of signature $(2,n)$ and $(\cdot,\cdot)$ denotes the complex *bilinear* extension of the intersection pairing to $L_{\mathbf{C}}$.
These domains can be realized as open subsets of quadric hypersurfaces in projective space, $Q = \{ [\omega] \in {\mathbf{P}}^{n+1} {~~\mathrel{\Big\vert}~~} (\omega, \omega) = 0 \}$, and the boundary components of their Baily-Borel compactifications encode possible limiting mixed Hodge structures of varieties.

#### Cusps Parabolic Subgroups

To compactify $F_\Gamma$, one must analyze the boundary of $D$.
This is achieved via the **Borel embedding**, a $G({\mathbf{R}})$-equivariant holomorphic open immersion $D \hookrightarrow D^\vee$, where $D^\vee$ is the **compact dual**. $D^\vee$ can be realized as $\widetilde{G}/K$, where $\widetilde{G}$ is the simply connected complex Lie group with Lie algebra $\widetilde{{\mathfrak{g}}} \mathrel{\mathop:}=  {\mathfrak{k}} + i{\mathfrak{p}} \subset {\mathfrak{g}} \otimes_{{\mathbf{R}}} {\mathbf{C}}$.
The boundary of the closure of $D$ in $D^\vee$, denoted $\partial D$, decomposes as a disjoint union of maximal connected complex-analytic subsets, known as **boundary components** or **cusps**, $\partial D = \bigsqcup F_i$.
For each such component $F$, its stabilizer in $G({\mathbf{R}})$ is the parabolic subgroup $$ N_F \mathrel{\mathop:}=  \{ g \in G({\mathbf{R}}) {~~\mathrel{\Big\vert}~~}  g F = F \} .$$ The maximal parabolic subgroups of $G({\mathbf{R}})$ are precisely those arising as stabilizers $N_F$ of boundary components $F$, and thus there is a bijective correspondence: $\left\{\text{Boundary components}\; F \subseteq \partial D\right\} \longleftrightarrow \left\{\text{Maximal parabolic subgroups}\; P \leq G\right\}$ A boundary component $F$ is **rational** if its stabilizer $N_F$ is defined over ${\mathbf{Q}}$.
Let $B(D)$ be the collection of proper rational boundary components.
The set $B(D)$ is in a natural bijection with the set of proper maximal parabolic ${\mathbf{Q}}$-subgroups of $G$.
The boundary is thus stratified by its rational components: $$ \partial D = \bigsqcup_{F \in B(D)} F \subseteq D^{\vee}
$$

#### The Rational Closure

The Baily--Borel compactification of $F_\Gamma \mathrel{\mathop:}=  { D }/{ \Gamma } $, denoted $\overline{F_\Gamma}^{ \operatorname{BB} }$, is constructed from the **rational closure** of $D$: [ D\^\* \mathrel{\mathop:}= D \cup \partial D \mathrel{\mathop:}= D\cup \bigsqcup\_{F \in B(D)} F ] The arithmetic group $\Gamma$ acts naturally on $D^*$ with only finitely many orbits of boundary strata.
The compactification is the quotient space, which can also be expressed as the quotient of $D$ with its boundary adjoined: [ \overline{F_\Gamma}^{ \operatorname{BB} } \mathrel{\mathop:}= {D^*}/{ \Gamma } = {(D \cup \partial D)}/{ \Gamma } .] By the main theorem of Baily and Borel, $\overline{F_\Gamma}^{ \operatorname{BB} }$ is a compact and Hausdorff space that contains $F_\Gamma$ as a dense open subset whose boundary $\partial \overline{F_\Gamma}^{ \operatorname{BB} } \mathrel{\mathop:}= \overline{F_\Gamma}^{ \operatorname{BB} } \setminus F_\Gamma$ is a finite disjoint union of closed, locally symmetric varieties: $\overline{F_\Gamma}^{ \operatorname{BB} } \setminus F_\Gamma = \bigsqcup{[F] \in  {B(D)}/{\Gamma}  } V_F$ where the indices $[F]$ run over $\Gamma$-orbits rational boundary components.
Each component $F$ is itself a Hermitian symmetric domain (or possibly a point), and the stratum $V_F$ is its arithmetic quotient, and we can write `\begin{align*}
V_F &= F / N_\Gamma(F)  \text{ where } 
N_\Gamma(F) \mathrel{\mathop:}= \operatorname{Stab}_\Gamma(F) / \operatorname{Fix}_\Gamma(F),
\\
\operatorname{Aut}(V_F) &= G_F \mathrel{\mathop:}= \operatorname{Stab}_{G({\mathbf{R}})}(F) / \operatorname{Fix}_{G({\mathbf{R}})}(F)
.\end{align*}`{=tex} Since $F$ is rational, $N_\Gamma(F)$ is a discrete arithmetic subgroup of the Lie group $G_F$.
As $F$ is an HSD, the quotient $V_F$ inherits the structure of a locally symmetric variety.

#### Projectivity via Automorphic Forms

A foundational result of (Baily and Borel 1966) is that $\overline{F_\Gamma}^{ \operatorname{BB} }$ can alternatively be constructed from the space of automorphic forms for $\Gamma$ and a canonical automorphic line bundle, showing it is a normal projective variety.
Letting $D = G({\mathbf{R}})/K$ be a Hermitian symmetric domain associated to a symmetric pair $(G, K)$, and $\Gamma \subset G({\mathbf{Q}})$ be an arithmetic subgroup acting properly discontinuously on $D$ as above, there is a distinguished $G({\mathbf{R}})$-equivariant ample line bundle ${\mathcal{L}} = {\mathcal{L}}_\chi$ on $D$ defined by a particular character $\chi: K\to {{\mathbf{C}}^{\times} }$.
In cases of interest, such as the Siegel and Type ${\textrm{IV}}$ cases $D = \operatorname{Sp}_g({\mathbf{R}})/\operatorname{U}_g$ or $D = \operatorname{O}(2,n)/(\operatorname{O}(2)\times\operatorname{O}(n))$, the bundle ${\mathcal{L}}$ is the determinant of the Hodge bundle or the inverse tautological bundle, respectively, where for a smooth, proper family of $n$-dimensional varieties $\pi: X \to S$, the **Hodge bundle** is the vector bundle ${\mathbb{E}} \mathrel{\mathop:}=  \pi_*\Omega^n_{X/S}$ whose fiber over $s \in S$ is $H^0(\Omega^n_{X_s})$, the space of global holomorphic $n$-forms on the fiber $X_s$.
For $ \mathcal{M}_{g}$, this reduces to the pushforward $\pi_\* \omega*{{\mathcal{C}}/ \mathcal{M}*{g}}$ of the relative dualizing sheaf of the universal curve $\pi: {\mathcal{C}} \to   \mathcal{M}_{g}$, and for $ \mathcal{A}\_{g} $ one often passes to its determinant, the **Hodge line bundle**.

For arithmetic groups $\Gamma$ as above, an **automorphic form of weight $k$ for $\Gamma$** (with _factor of automorphy_ $j$) is a holomorphic section $f \in H^0( {\mathcal{L}}^{\otimes k})$ of the $k$th tensor power of ${\mathcal{L}}$ such that the $\gamma^* f = f$ for all $\gamma \in \Gamma$.Locally, this recovers the familiar automorphy condition
$$
f(\gamma \cdot z) = j(\gamma, z)^k \cdot f(z) \qquad \text{for all } \gamma \in \Gamma, z\in D .$$ We define the space of weight $k$ $\Gamma$-automorphic forms as the invariants sections of ${\mathcal{L}}^{\otimes k}$, which assemble to a graded ring: $$ A_k(\Gamma) \mathrel{\mathop:}=  H^0(D, {\mathcal{L}}^{\otimes k})^\Gamma, \qquad R_\Gamma \mathrel{\mathop:}= \bigoplus_{k \geq 0} A_k(\Gamma) .$$ (Baily and Borel 1966) shows that that $R_\Gamma$ is a finitely generated ${\mathbf{C}}$-algebra, and there is an identification $\overline{F_\Gamma}^{ \operatorname{BB} } \cong \operatorname{Proj}(R_\Gamma)$.
Moreover, ${\mathcal{L}}$ descends to an ample line bundle on $\overline{F_\Gamma}^{ \operatorname{BB} }$ and the sections of ${\mathcal{L}}^{\otimes k}$ satisfy the analytic growth conditions at cusps of $F_\Gamma$ in analogy to classical modular forms for $\operatorname{SL}(2, {\mathbf{Z}})$.
This construction is canonical and functorial: any $(\Gamma_1, \Gamma_2)$-equivariant morphism $F_{\Gamma_1} \to F_{\Gamma_2}$ compatible with ${\mathcal{L}}_1$ and ${\mathcal{L}}*2$ extends uniquely to a morphism between their Baily--Borel compactifications.
However, this typically introduces singularities on $\partial\overline{F*\Gamma}^{ \operatorname{BB} }$, motivating further refinements, e.g., semitoroidal or KSBA compactifications.

#### Cusps and Boundary Strata

Let $T$ be an even lattice of signature $(2, n)$, let $\Gamma\leq \operatorname{O}(L)$ be a (neat) arithmetic subgroup, and let $D \mathrel{\mathop:}= D_{T}$ be the corresponding period domain with arithmetic quotient $F_\Gamma \mathrel{\mathop:}=  { D_{T} }/{ \Gamma } $.
The rational boundary components of $D$ have dimensions $0$ ("Type ${\textrm{III}}$") or $1$ ("Type ${\textrm{II}}$"). There are canonical bijections between $\Gamma$-orbits of the following sets:

- Rational boundary components of $D$,
- Rational parabolic subgroups $P \leq \operatorname{O}(T_{\mathbf{Q}})$, and
- Primitive isotropic subspaces $I \subset T_{\mathbf{Q}}$.

This correspondence is explicitly as follows: to each primitive isotropic subspace $I \subset T_{\mathbf{Q}}$ of rank $k$ (with $1 \leq k \leq 2$), associate the boundary component $F_I$ of dimension $k-1$ described as follows: writing $D$ as $G({\mathbf{R}})/K$, a boundary component $F_I$ corresponds to an isotropic sublattice $I$ if and only if $\operatorname{Stab}*G(I) = \operatorname{Stab}*G(F_I)$.
If $k=1$, then $I$ is a line and $F_I$ is a point, and if $k=2$, the component $F_I$ is a modular curve with level structure.
These bijections are compatible with the natural poset structures: inclusion $I_1 \subset I_2$ induces $F*{I_2}$ contained in the closure of $F*{I_1}$, and parabolic subgroups are partially ordered by inclusion.
We grade isotropic sublattices by rank, boundary components by dimension, and parabolic subgroups by the dimension of their unipotent radical.
The above bijection then extends to an isomorphism of ${\mathbf{Z}}$-graded posets, up to a shift: rank $k$ isotropic sublattices correspond to boundary components of dimension $k-1$.
This is the fundamental bijection which makes $\overline{F_\Gamma}^{ \operatorname{BB} }$ accessible by lattice-theoretic methods.

To conclude, let $\eta \in T$ be a primitive isotropic vector and set $ \overline{T}*{ \eta } \mathrel{\mathop:}= \eta^{\perp T}/\langle\eta\rangle$, which is an even lattice of signature $(1, n-1)$.
Recall that the **stable boundary group** is defined as $\Gamma*\eta \mathrel{\mathop:}= \operatorname{Stab}*\Gamma(\eta)/U*\eta$, where $\operatorname{Stab}*\Gamma(\eta)$ is the stabilizer of $\eta$ in $\Gamma$ and $U*\eta$ is its unipotent radical.
Associated to $\Gamma_\eta$ is its **stable reflection group** $W(\Gamma_\eta) \subseteq \operatorname{O}( \overline{T}*{ \eta  } )$, generated by reflections in roots of $ \overline{T}*{ \eta } $ contained in $\Gamma_\eta$.
Denote by $ \mathfrak{C} (\Gamma_\eta)$ the *fundamental chamber*, which is the convex polyhedral cone in $ \overline{T}*{ \eta, {\mathbf{R}} } $ consisting of those vectors $v$ satisfying $(\alpha, v) \geq 0$ for each simple root $\alpha$ corresponding to the chosen system of reflections.
The local data for a toroidal compactification at the $0$-cusp $F*\eta$ comes from attaching a toric variety constructed from the positive cone and its rational closure, [ \mathfrak{C} *\eta \mathrel{\mathop:}= `\left\{{ v \in \overline{T}_{ \eta, {\mathbf{R}} } {~\mathrel{\Big\vert}~} v^2 > 0 }\right\}{=tex} `\qquad \mathfrak{C} *{\eta,{\mathbf{Q}}} \mathrel{\mathop:}= \bigcup `\left\{{ {\mathbf{R}}_{\geq 0} v {~\mathrel{\Big\vert}~} v \in \overline{T}_{ \eta, {\mathbf{Q}} } , v^2 > 0 }\right\}`{=tex} .] After projectivization, ${\mathbf{P}}( \mathfrak{C} *\eta) \cong  \mathfrak{C} *\eta / {\mathbf{R}}*{>0}$ is identified with $\mathbb{H}^{n-1}$.
The stable reflection group $W(\Gamma*\eta)$ acts discretely on this space by isometries, with fundamental chamber $ \mathfrak{C} (\Gamma*\eta)$ yielding a convex (possibly non-compact) hyperbolic polytope bounded by the reflection hyperplanes in the roots of $ \overline{T}*{ \eta } $.

One must choose a $\Gamma_\eta$-invariant rational polyhedral fan $\Sigma(\eta)$ supported on $ \mathfrak{C} *{\eta, {\mathbf{Q}}}$.
A particularly canonical choice, when $W(\Gamma*\eta)$ is sufficiently large enough and defines a locally finite arrangement, is the **Coxeter fan**: the rational polyhedral decomposition of $ \mathfrak{C} *{\eta, {\mathbf{Q}}}$ whose cones are in bijection with the $W(\Gamma*\eta)$-translates of $ \mathfrak{C} (\Gamma_\eta)$.
This yields a tiling of $\mathbb{H}^{n-1}$ by Coxeter polytopes, where each chamber is in bijection with a fan in $ \mathfrak{C} *{\eta, {\mathbf{Q}}}$ and their gluing data is determined by the combinatorics of $W(\Gamma*\eta)$.
In general, other $\Gamma_\eta$-invariant fans $\Sigma(\eta)$ may be chosen; however, when the Coxeter fan is well-defined and locally finite, it provides a natural, symmetric choice . Globally, the collection of all such fans $\{\Sigma(\eta)\}$ ranging over all $k$-cusps $\eta$ produces a **toroidal compactification** $ \overline{F*\Gamma}^{ \Sigma *{\bullet} } $.
Locally, analytic neighborhoods of cusps $\eta$ are described via open subsets in the respective toric varieties $X_{\Sigma(\eta)}$, which assemble to form a normal, complex algebraic space $ \overline{F*\Gamma}^{ \Sigma *{\bullet} } $ that naturally maps to $\overline{F_\Gamma}^{ \operatorname{BB} }$.

<!-- Source: 2-part-moduli/4-chapter-cpt/200-toroidal.md -->

### Toroidal Compactifications

Let $F_\Gamma \mathrel{\mathop:}=  { D }/{ \Gamma } $ be a Hermitian symmetric domain of Type ${\textrm{IV}}$ associated to an indefinite lattice $T$ of signature $(2, n)$, as in the previous section, and let $\overline{F_\Gamma}^{ \operatorname{BB} }$ be its Baily-Borel compactification.
We make an additional technical assumption that $\Gamma$ is *neat*, which ensures that $F_\Gamma$ is smooth.
The Baily--Borel compactification $\overline{F_\Gamma}^{ \operatorname{BB} }$ is projective but is typically highly singular along its cusps.
To obtain a compactification with better local and algebro-geometric properties, one constructs a **toroidal compactification**. This requires, for each cusp $\eta$ of $\overline{F_\Gamma}^{ \operatorname{BB} }$, the choice of a $\Gamma$-admissible rational polyhedral decomposition $\Sigma_\eta$ of the rational closure of the positive cone, i.e. a fan . Locally, a neighborhood of $\eta$ is described by a toric variety $X_{\Sigma(\eta)}$ associated to these fans.
The global compactification $ \overline{F*\Gamma}^{ \Sigma *{\bullet} } $ is patched from these local models and contains $F_\Gamma$ as a dense open subset, with a proper, $\Gamma$-equivariant morphism $ \overline{F*\Gamma}^{ \Sigma *{\bullet} } \longrightarrow \overline{F*\Gamma}^{ \operatorname{BB} }$.
Unlike the Baily--Borel compactification, $\partial \overline{F*\Gamma}^{ \Sigma \_{\bullet} } $ can be made smooth for suitable choices of fans.
We now describe the construction in more detail.

#### Admissible Fans

Let $T$ be an even indefinite lattice of signature $(2,n)$ and let $\Gamma \leq \operatorname{O}(T)$ be an arithmetic subgroup.
Fix a primitive isotropic sublattice $I \subset T$ of rank $k$ and set the boundary lattice $\overline{T}*I \mathrel{\mathop:}= I^{\perp T} / I$, which is an even lattice of signature $(2-k, n-k)$ and rank $\operatorname{rank}(T) - 2k$.
Denote by $ \mathfrak{C} *I \subset \overline{T}*{ I, {\mathbf{R}} } $ the positive cone, with $ \mathfrak{C} *{I, {\mathbf{Q}}}\subset \overline{T}*{ I, {\mathbf{R}} } $ its rational closure: $$ \mathfrak{C} *{I, {\mathbf{Q}}} \mathrel{\mathop:}= \left\{ {\mathbf{R}}*{\geq 0} v {~~\mathrel{\Big\vert}~~} v \in  \overline{T}*{ {\mathbf{Q}}  } ,\ v^2 > 0 \right\} .$$ A **rational polyhedral fan** $\Sigma_I$ in $ \overline{T}\_{ I, {\mathbf{R}} } $ is a collection of strongly convex, rational polyhedral cones $\sigma \subset V$ with the following properties:

- For every face $\tau$ of every $\sigma \in \Sigma_I$, we have $\tau \in \Sigma_I$.
- For all $\sigma_1, \sigma_2 \in \Sigma_I$, the intersection $\sigma_1 \cap \sigma_2$ is a common face of both.
- $\Sigma_I$ is **locally finite**: every compact subset of $ \overline{T}\_{ I, {\mathbf{R}} } $ meets only finitely many cones of $\Sigma_I$.
- Each cone $\sigma$ is **rational**: it is generated by finitely many elements of $\overline{T} \cap (T \otimes_{\mathbf{Q}})$.
- Each cone $\sigma$ is **strongly convex**: it contains no nontrivial linear subspace.

### Admissible Fans at Boundary Cusps

Let $T$ be an integral lattice and $\Gamma \leq O(T)$ an arithmetic subgroup.
For a primitive isotropic sublattice $I \subset T$, consider a fan $\Sigma_I$ in the associated real vector space $ \overline{T}*{ I, {\mathbf{R}} } $.
The **support** of $\Sigma_I$ is defined as $$
|\Sigma_I| \mathrel{\mathop:}= \bigcup*{\sigma \in \Sigma_I} \sigma.

$$

Let $\operatorname{Stab}_{\Gamma}(I) \leq \Gamma$ denote the stabilizer of $I$ in $\Gamma$. The fan $\Sigma_I$ is said to be **$\Gamma$-admissible at the cusp determined by $I$** if the following conditions are satisfied:

-   **(i) Invariance:** $\Sigma_I$ is invariant under the action of $\operatorname{Stab}_{\Gamma}(I)$;

-   **(ii) Local finiteness:** $\Sigma_I$ is locally finite in $ \overline{T}_{ I, {\mathbf{R}}  } $;

-   **(iii) Finiteness of orbits:** There are only finitely many $\operatorname{Stab}_{\Gamma}(I)$-orbits of cones in $\Sigma_I$;

-   **(iv) Full support:** $|\Sigma_I| =  \mathfrak{C} _{I, {\mathbf{Q}}}$, where $ \mathfrak{C} _{I, {\mathbf{Q}}}$ is the rational closure of the relevant positive cone associated to $I$;
-   **(v) Compatibility under projection:** For every inclusion of primitive isotropic sublattices $I \subset J \subset T$, let $W \mathrel{\mathop:}= (J^\perp/J) \otimes_{\mathbf{Z}} {\mathbf{R}}$ and denote by $\pi_{IJ}\colon T_{{\mathbf{R}}} \to W$ the canonical projection. Then the fan at $J$ is given by
$$
```
\Sigma_J = \left\{{
\pi_{IJ}(\sigma) {~\mathrel{\Big\vert}~} \sigma \in \Sigma_I,\ \pi_{IJ}(\sigma)\ \text{is a cone of positive dimension}
}\right\}
$$ that is, $\Sigma_J$ is the image of $\Sigma_I$ under the projection $\pi_{IJ}$, omitting cones of dimension zero.
```

A **compatible system of $\Gamma$-admissible fans** is a family $\{\Sigma_I\}$, indexed by all primitive isotropic sublattices $I \subset T$, such that for every inclusion $I \subset J$, the compatibility condition above (v) is satisfied.

Given such a system, the local model of the toroidal compactification at the cusp associated to $I$ is the toric variety $X_{\Sigma_I}$ determined by $\Sigma_I$, and $ \overline{F_\Gamma}^{  \Sigma *{\bullet} } $ is then constructed by gluing these toric varieties to neighborhoods of the cusps in $\overline{F*\Gamma}^{ \operatorname{BB} }$ according to the configuration of cones $\Sigma_\bullet \mathrel{\mathop:}= \left\{{ \Sigma_I}\right\}$.
If $\{\Sigma_I\}$ is sufficiently fine and regular, $\partial  \overline{F_\Gamma}^{  \Sigma *{\bullet} } $ is divisorial and locally a union of snc toric varieties.
It is a normal, projective algebraic variety containing $F*\Gamma$ as a dense open subset and is equipped with a proper morphism $ \overline{F_\Gamma}^{  \Sigma *{\bullet} }  \to \overline{F*\Gamma}^{ \operatorname{BB} }$ extending the identity on $F_\Gamma$ and resolving the singularities at the boundary of the Baily--Borel compactification.

The compactification $ \overline{F_\Gamma}^{  \Sigma *{\bullet} } $ is canonical up to the choice of admissible fan.
For each $0$-cusp $\eta$ of the Baily--Borel compactification, corresponding to a primitive isotropic sublattice $I \subset T$, the local structure of the toroidal compactification near $\eta$ is modeled on a toroidal embedding; that is, a formal (or analytic) neighborhood is locally isomorphic to an open subset of a finite quotient of a toric variety $X(\Sigma*\eta)$, where $\Sigma_\eta$ is a $\Gamma_\eta$-invariant rational polyhedral fan as above.
For higher-dimensional boundary strata, the local model is a finite quotient of a toric fibration over the corresponding stratum of $\overline{F_\Gamma}^{ \operatorname{BB} }$.

Globally, there is a proper, $\Gamma$-equivariant morphism $\sigma\colon  \overline{F_\Gamma}^{  \Sigma *{\bullet} }  \to \overline{F*\Gamma}^{ \operatorname{BB} }$ which is an isomorphism over $F_\Gamma$.
Over a $0$-cusp $\eta$, the preimage $\sigma^{-1}(\eta)$ is a finite quotient of the union of toric boundary strata in $X(\Sigma_\eta)$.
For higher-dimensional boundary strata $S$, the preimage $\sigma^{-1}(S)$ is locally a finite quotient of a toric fibration over $S$, whose fibers are unions of toric strata as above.
The contraction induced by $\sigma$ contracts each such fiber to the corresponding cusp, and is an isomorphism on the interior $F_\Gamma$.
Since the entire construction is compatible with $\Gamma$, the resulting space is generally a normal, proper algebraic variety when $\Gamma$ is neat.

#### Example: $  \mathcal{A}_{g} $ and Voronoi Fans

The Siegel modular variety $  \mathcal{A}*{g}  = \operatorname{Sp}*{2g}({\mathbf{Z}}) \backslash \mathbb{H}*g$ parametrizes principally polarized abelian varieties (ppavs) of dimension $g$, where $\mathbb{H}*g$ is the Siegel upper half-space of $g \times g$ complex symmetric matrices with $\Im(\tau) > 0$.
A toroidal compactification $ \overline{  \mathcal{A}*{g} }^{  \Sigma *{\bullet} } $ is specified by a collection of admissible, rational polyhedral fans $\Sigma_I$ in the cone $C_g$ of real, symmetric, positive-definite $g \times g$ matrices at each cusp, invariant under a finite index subgroup of $\operatorname{Stab}*\Gamma(I)$.
Each cone $\sigma \in \Sigma$ determines a boundary stratum $D*\sigma$, and locally the boundary is modeled by toric varieties $U_\sigma/\Gamma_\sigma$ glued along shared faces, as described above.
For $Q \in C_g$ and $$ M(Q) \mathrel{\mathop:}= \{ v \in {\mathbf{Z}}^g \setminus \{0\} {~~\mathrel{\Big\vert}~~} Q[v] = \min_{w \neq 0} Q[w] \}. ,$$ define the **perfect cone** generated by $Q$ as $$ \sigma(Q) = {\mathbf{R}}*{\geq 0} \langle v v^{\intercal} {~~\mathrel{\Big\vert}~~} v \in M(Q) \rangle.
$$ A form $Q$ is **perfect** if it is determined by $M(Q)$ up to scaling.
The **first Voronoi** fan $\Sigma^{\operatorname{perf}}$, is the union of all such cones as $Q$ varies over all such forms, and determines a compactification $\overline{  \mathcal{A}*{g} }^{\,\operatorname{perf}}$.
Each form $Q \in C_g$ induces a Delaunay decomposition: a tiling of ${\mathbf{R}}^g$ into convex polytopes determined by minima of $Q$, and two forms are Delaunay-equivalent if their tilings are $\operatorname{GL}*g({\mathbf{Z}})$-equivalent.
The **second Voronoi fan** $\Sigma^{\operatorname{Vor}}$ consists of cones dual to faces of the secondary polytope parameterizing all possible Delaunay decompositions, which determines a dual compactification $\overline{  \mathcal{A}*{g} }^{\,\operatorname{Vor}}$ Each boundary stratum in $\overline{  \mathcal{A}*{g} }^{\operatorname{Vor}}$ corresponds to a stable *semiabelic pair* $(G,\Theta)$, where $G$ is a semiabelian scheme, i.e. an extension $0 \to {\mathbf{G}}*m^r \to G \to A' \to 0$, where $\Theta$ is a stable limit of a theta divisor.
The face poset of $\Sigma^{\operatorname{Vor}}$ encodes the combinatorics of $\Theta$, and there is an identification $\overline{  \mathcal{A}*{g} }^{\operatorname{Vor}} \cong  \overline{  \mathcal{A}*{g} } $ where $ \overline{  \mathcal{A}*{g} } $ is the KSBA compactification by stable semiabelic pairs due to (**Ale03?**). This mirrors $\overline{  \mathcal{M}*{g}}$, where dual graphs index boundary points of the Deligne-Mumford compactfication by stable curves (P. Deligne and Mumford 1969); here, cones in $\Sigma^{\operatorname{Vor}}$ play an analogous role.
For each $\sigma \in \Sigma$, neighborhoods of $D_\sigma$ are modeled analytically on toric varieties $U_\sigma/\Gamma_\sigma$, where face inclusions determine the gluing data.

#### Toward semitoroidal compactifications

The theory of toroidal compactifications guarantees that local models around boundary cusps have at worst finite quotient singularities if $\Gamma$ is not neat, and that the resulting compactification $ \overline{F_\Gamma}^{  \Sigma *{\bullet} } $ is a normal, projective algebraic space.
However, in many cases, the requirement that $\Sigma_I$ is globally polyhedral and locally finite at every cusp is too restrictive, making $\overline{F*\Gamma}^{ \operatorname{BB} }$ too coarse and singular for many applications.
To address this, semitoroidal compactifications allow, at each cusp, the use of a semifan: a collection of convex rational cones which need not be polyhedral or locally finite, which may thus contain infinitely generated cones or infinitely many cones accumulating at the boundary.
The combinatorial data $  \mathcal{F} *{\bullet}  = { \mathcal{F} *I}$ indexed by cusps $I$ is still required to be $\Gamma$-admissible, i.e. invariant with only finitely many orbits under the stabilizer, and satisfy similar compatibility conditions.
While the local boundary models in semitoroidal compactifications $\overline{F*\Gamma}^{  \mathcal{F} *{\bullet} }$ are no longer strictly toric varieties, the resulting compactification still admits a proper, $\Gamma$-equivariant morphism $\overline{F*\Gamma}^{  \mathcal{F} *{\bullet} } \to \overline{F*\Gamma}^{ \operatorname{BB} }$ and contains $F*\Gamma$ as a dense open subset.
In the next section, we review the formal definitions of semifans and the construction of semitoroidal compactifications, following (Looijenga 1985) and related work.

<!-- Source: 2-part-moduli/4-chapter-cpt/300-semitoroidal.md -->

### Semitoroidal Compactifications {#setion-5-3}

Throughout this section, let $T$ be an even lattice of signature $(2, n)$, $ \overline{T}*{ \eta  }  \mathrel{\mathop:}=   \overline{T}*{ \eta  }  = \eta^{\perp T} / \langle \eta \rangle$ be the boundary lattice of signature $(1, n-1)$ at a $0$-cusp $\eta \in T$, and let $\Gamma\leq \operatorname{O}(T)$ be a neat arithmetic subgroup, and let $\eta \in T$ denote a primitive isotropic line in $T$ and $I\subseteq T$ a primitive isotropic plane, corresponding to a 0-cusp of $\overline{F_\Gamma}^{ \operatorname{BB} }$ and a 1-cusp respectively.
Let $W \mathrel{\mathop:}=  W(\Gamma_\eta)$ denote the stable reflection group acting on $ \overline{T}*{ \eta  } $.
Let $ \mathfrak{C}  =  \mathfrak{C} (\Gamma*\eta)$ be a fixed fundamental chamber for $W$ defined by the inequalities $(v, \alpha) \ge 0$ for all $\alpha \in \Phi(\Gamma\eta)$.
Let $G(\Gamma_\eta)$ be the associated Coxeter diagram and $\Phi(\Gamma_\eta)$ be the set of simple roots for $W(\Gamma_\eta)$.
**Semitoroidal compactifications** ((Looijenga 1985, 2003)) $\overline{F_\Gamma}^{  \mathcal{F} *{\bullet} }$ generalize the construction of toroidal compactifications $ \overline{F*\Gamma}^{  \Sigma *{\bullet} } $ by replacing each polyhedral fan $\Sigma_I$ with a $\Gamma$-admissible **semifan**. The local models are toroidal embeddings attached to semifans, compatibly glued over all cusps.
This section formalizes semifans and semitoroidal compactifications, describes admissibility and compatibility, and relates semitoroidal, toroidal, and Baily--Borel compactifications via a tower of birational morphisms: $$ \overline{F*\Gamma}^{ \operatorname{BB} } \longleftarrow \overline{F_\Gamma}^{  \mathcal{F} *{\bullet} } \longleftarrow  \overline{F*\Gamma}^{  \Sigma _{\bullet} } .$$ More precisely,

:::{.definition
    title="{ Semifans [@???] }
    title="{ Semifans [@???] }
    title="{ Semifans [@???] }

} let $V$ be a real finite-dimensional vector space, and let $C \subset V$ be an open, nondegenerate convex cone. A **semifan** ${\mathcal{F}}$ in $C$ is a collection of closed, convex, rational polyhedral cones $\sigma \subset  \mathfrak{C} _{{\mathbf{Q}}}$ such that:

-   every face of every $\sigma \in {\mathcal{F}}$ belongs to ${\mathcal{F}}$;
-   for any $\sigma, \tau \in {\mathcal{F}}$, the intersection $\sigma \cap \tau$ is a face of both $\sigma$ and $\tau$;
-   the interiors of the cones in ${\mathcal{F}}$ are pairwise disjoint.

Unlike a fan, ${\mathcal{F}}$ is not required to be locally finite, nor to cover all of $C$. In particular, ${\mathcal{F}}$ may be infinite and its support $\bigcup_{\sigma \in {\mathcal{F}}} \sigma$ may be a proper subset of $ \mathfrak{C} _{{\mathbf{Q}}}$. This generalization allows, for example, arrangements arising from infinite or non-polyhedral wall structures, as well as dual complexes of degenerations; it thus extends the toroidal theory to situations where global polyhedrality or local finiteness fails.
:::

:::
remark
Recall that the positive cone associated to a primitive isotropic sublattice and its rational closure are defined by
$$

\mathfrak{C} _{I} \mathrel{\mathop:}= \left\{{ v \in \overline{T}_{ I, {\mathbf{R}} } {~\mathrel{\Big\vert}~} (v, v) > 0}\right\}, \quad
\mathfrak{C} _{I, {\mathbf{Q}}} \mathrel{\mathop:}= \bigcup \left\{{
{\mathbf{R}}_{\geq 0} \cdot v {~\mathrel{\Big\vert}~} v \in \overline{T}_{ I, {\mathbf{Q}} } , v^2 \geq 0
}\right\}
,$$ \todo{Duplicated.
Also, should include isotropic rays...?} which defines a real hyperbolic space by projectivization: $$
\mathbb{H}\_I \mathrel{\mathop:}= {\mathbf{P}}( \mathfrak{C} _{I}) \mathrel{\mathop:}= \left\{{
\left\langle v \right\rangle*{{\mathbf{R}}*{>0}} \subset \overline{T}_{ I, {\mathbf{R}} } {~\mathrel{\Big\vert}~} v^2 > 0
}\right\}
.$$ A **tiling** $\mathcal{T}_I$ of $\mathbb{H}_I$ is a locally finite collection of convex polyhedral subsets $\{\tau_\alpha\}_{\alpha \in A}$ such that $\mathbb{H}\_I = \bigcup_\alpha \tau*\alpha^\circ$ is disjoint union of the relative interiors of the tiles, and for each $\alpha$, there is a cone $\sigma \in {\mathcal{F}}_I$ with $\tau*\alpha = {\mathbf{P}}(\sigma)$ where ${\mathcal{F}}_I$ is a semifan in $ \mathfrak{C} _{I, {\mathbf{Q}}}$. If for every cone $\sigma \in {\mathcal{F}}_I$ there is a decomposition $\sigma = P \times H_{I, {\mathbf{R}}}$ where $P \subset  \overline{T}_{ I, {\mathbf{R}}  } $ is a convex polytope and $H_{I, {\mathbf{R}}} \subset  \overline{T}_{ I, {\mathbf{R}}  } $ is a fixed real linear subspace, then we say the lattice $H_I \mathrel{\mathop:}=  H_{I, {\mathbf{R}}} \cap  \overline{T}_{ I  } $ is the **coning direction**, and the semifan (or equivalently the tiling) is **coned in the direction of $H_I$\*\*.
:::

:::{.definition title="$\\Gamma$-admissible semifans"}
Let $T$ be an even lattice of signature $(2, n)$ and $\Gamma \leq \operatorname{O}(T)$ a neat arithmetic group.
Let $F_\Gamma$ be the arithmetic quotient, and $\overline{F_\Gamma}^{ \operatorname{BB} }$ its Baily--Borel compactification.
Each cusp of $\overline{F_\Gamma}^{ \operatorname{BB} }$ corresponds to a primitive isotropic subspace $I \subset T$.
Let $ \overline{T}_{ I } = I^\perp / I$ be the associated boundary lattice and $ \mathfrak{C} _{I, {\mathbf{Q}}}$ the rational closure of the positive cone in $ \overline{T}_{ I, {\mathbf{R}} } $. A **$\Gamma$-admissible semifan at the cusp determined by $I$\*\* is a semifan ${\mathcal{F}}_I$ in $ \mathfrak{C} _{I, {\mathbf{Q}}}$, invariant under $\operatorname{Stab}_\Gamma(I)$ with finitely many $\operatorname{Stab}_\Gamma(I)$-orbits of cones.
The support of ${\mathcal{F}}_I$ need not cover all of $ \mathfrak{C} _{I, {\mathbf{Q}}}$ nor be locally finite.
A **compatible system of $\Gamma$-admissible semifans** is a collection $ \mathcal{F} _{\bullet} $, one for each cusp $I$, such that for every inclusion of cusps $I \subset J$ (that is, for inclusions of the underlying isotropic subspaces), the natural projection $\pi_{IJ} \colon  \overline{T}_{ I, {\mathbf{R}}  }  \to  \overline{T}_{ J, {\mathbf{R}}  } $ satisfies $$
{\mathcal{F}}_J = \left\{ \pi_{IJ}(\sigma) {~\mathrel{\Big\vert}~} \sigma \in {\mathcal{F}}_I,\, \pi_{IJ}(\sigma) \text{ a cone of positive dimension} \right\}
.$$
:::

\todo{Redundancy with fan definitions?}

As an example, any fan is a semifan, and if a semifan is not a fan, we say it is a **strict semifan**. In particular, the classical toroidal case is recovered by choosing for each $I$ a rational polyhedral fan $\Sigma_I$ supported on $ \mathfrak{C} *{I, {\mathbf{Q}}}$ and requiring $\Sigma_I$ to be invariant under $\operatorname{Stab}*\Gamma(I)$ with finitely many orbits.
The corresponding compactification is the toroidal compactification $ \overline{F*\Gamma}^{ \Sigma *{\bullet} } $.
The "trivial" semifan consists of, for each $I$, the full positive cone $ \mathfrak{C} *{I, {\mathbf{Q}}}$ in $ \overline{T}*{ I, {\mathbf{R}} } $, which yields $\overline{F_\Gamma}^{ \operatorname{BB} }$, and thus we will refer to this as the **Baily-Borel semifan** ${\mathcal{F}}^{\operatorname{BB}}$.
In this case each local model is essentially the "one-point" (or "one-orbit") compactification, and ${\mathcal{F}}^{\operatorname{BB}}$ is a fan in the toroidal sense.
Generalized Coxeter semifans, defined below, provide intermediate examples of strict semifans.
For instance, partial wall data associated to a set of relevant roots yields a semifan that is a coarsening of the Coxeter fan.
These may fail to be locally finite -- the boundary decomposition then glues together chambers along the omitted (irrelevant) walls.

* * *

#### Construction

:::{.theorem title="{ Existence of semitoroidal compactifications [@Loo03] }
"}
Let $T$ be an even lattice of signature $(2, n)$, $\Gamma \leq \operatorname{O}^*(T)$ a neat arithmetic group, and $F_\Gamma$ the associated locally symmetric modular variety.
Let $ \mathcal{F} _{\bullet} $ be a compatible system of $\Gamma$-admissible semifans ranging over Baily-Borel cusps $I$ of $\partial\overline{F_\Gamma}^{ \operatorname{BB} }$, as defined above. Then there exists a normal compactification $\overline{F_\Gamma}^{  \mathcal{F} _{\bullet} }$ containing $F_\Gamma$ as an open dense subset, called the **semitoroidal compactification** associated to $ \mathcal{F} \_{\bullet} $, with the following properties:

1.  The boundary strata are in bijection with the set of $\Gamma$-orbits of pairs $(I, \sigma)$, where $I$ is a cusp and $\sigma$ is the class of a cone in ${\mathcal{F}}_I$, modulo the stabilizer in $\Gamma$.

2.  If $\sigma \subset {\mathcal{F}}_\eta$ is a cone with $\eta$ an isotropic line corresonding to a Type ${\textrm{III}}$ cusp, let $L_{\eta, \sigma} = \eta^{\perp T}/\left\langle \eta, \sigma \right\rangle$.
    Then the corresponding stratum is a finite quotient of $L_{\eta, \sigma, {{\mathbf{C}}^{\times} }}$.
    \todo{Check}

3.  If $\sigma \subset {\mathcal{F}}_I$ with $I$ an isotropic plane corresponding to a a Type ${\textrm{II}}$ cusp, there is a subspace $H_I$ depending on $\sigma$ and an algebraic group ${\mathcal{E}}$ defined in (Looijenga 2003).
    Let $L_{I, \sigma} \mathrel{\mathop:}= I^{\perp}/\left\langle I, H_I \right\rangle$, then the corresponding stratum is a finite quotient of $L_{I, \sigma, {\mathcal{E}}}$.
    \todo{Check}

4.  For any compatible system of semifans $ \mathcal{G} _{\bullet} $ refining $ \mathcal{F} _{\bullet} $, there is a natural morphism $\overline{F_\Gamma}^{  \mathcal{G} _{\bullet} } \to \overline{F_\Gamma}^{  \mathcal{F} _{\bullet} }$ which maps strata to strata according to inclusion of cones: for $\tau \subset \sigma$, the stratum indexed by $(I,\tau)$ maps to the startum indexed by $(I,\sigma)$.

\todo{Revise}

Note that unlike for fans, strata corresponding to Type ${\textrm{III}}$ cones of a semifan may have infinite stabilizer in $\operatorname{Stab}_\Gamma(\eta)$ -- however, the stratum is still a finite quotient of $L_{\eta, \sigma, {{\mathbf{C}}^{\times} }}$.
:::

\todo{Citations}

:::{.definition title="{ Semitoroidal compactifications}
"}
Given a compatible system $ \mathcal{F} _{\bullet} $ of $\Gamma$-admissible semifans, the local model of the semitoroidal compactification near the cusp associated to $I$ is a toroidal embedding constructed from ${\mathcal{F}}_I$, typically a finite quotient of a toric embedding $X( \mathcal{F} _{\bullet} )$ associated with the semifan.
For $0$-cusps, the local neighborhood is modeled on such a quotient of a torus fibration, and the boundary strata correspond to cones of $ \mathcal{F} _{\bullet} $. For higher rank cusps ($\operatorname{rank}(I) > 1$), the local model is, locally in the analytic or formal topology, a toric fibration over the boundary stratum corresponding to $I$, whose fibers are toroidal embeddings associated to semifans.
The boundary of $\overline{F_\Gamma}^{ \mathcal{F} _{\bullet} }$ is stratified by the cones and faces of all semifans $ \mathcal{F} _{\bullet} $, with strata glued compatibly respecting the combinatorial morphisms given by face projections. This local-to-global structure enables interpolation between the $\overline{F_\Gamma}^{ \operatorname{BB} }$ and the maximal $ \overline{F*\Gamma}^{ \Sigma *{\bullet} } $ by allowing the semifans to vary from trivial to polyhedral and locally finite.
:::

:::{.theorem title="{Birational tower characterization [@AE23, Theorem 5.14]}
"}
Let $F_\Gamma$ be a Type ${\textrm{IV}}$ arithmetic quotient, and let $\overline{F_\Gamma}$ be any normal compactification of $F_\Gamma$.
The following are equivalent:

1.  There exist proper morphisms of normal compactifications $$
     \overline{F_\Gamma}^{  \Sigma _{\bullet} }  \longrightarrow \overline{F_\Gamma} \longrightarrow \overline{F_\Gamma}^{ \operatorname{BB} }
    $$ where $ \overline{F*\Gamma}^{ \Sigma *{\bullet} } $ is a toroidal compactification and $\overline{F_\Gamma}^{ \operatorname{BB} }$ is the Baily--Borel compactification.

2.  There exists a collection of $\Gamma$-admissible semifans $ \mathcal{F} _{\bullet} $ such that $\overline{F_\Gamma}^{ \mathcal{F} _{\bullet} } { \, \xrightarrow{\sim}\, } \overline{F_\Gamma}$.
    :::

\todo{Check morphism direction.}

::: {.theorem title="{Recognition theorem for KSBA compactifications [@AE23, Theorem 9.1]}"}
Let $R$ be a recognizable divisor in the moduli space of $S$-polarized K3 surfaces (in the sense of (Alexeev and Engel 2023)) corresponding to the moduli space $F_{\Gamma}$, where $\Gamma$ is the appropriate arithmetic subgroup of $\operatorname{O}(T)$ and $T\mathrel{\mathop:}= S^{\perp  {L_{\mathrm{K3}}} }$.
Then there exists a unique semifan ${\mathcal{F}}_R$ such that the normalization morphism $\overline{F_\Gamma}^{{\mathcal{F}}_R} \to  \overline{F_\Gamma} ^R$ identifies $\overline{F_M}^{{\mathcal{F}}_R}$ as the normalization of the KSBA compactification $ \overline{F\_\Gamma} ^R$ associated to $R$.
The cones of ${\mathcal{F}}_R$ are precisely the maximal subsets in which the combinatorial type of slc stable pairs is constant as a function of the _monodromy invariant_ $\lambda$.
:::

:::
remark
For any recognizable divisor $R$ on $F_S$, the normalization of the KSBA compactification $\overline{F}^R$ is a semitoroidal compactification, with the associated semifan ${\mathcal{F}}_R$ determined by $R$.
A fundamental example of a recognizable divisor is the **rational curves divisor** $R_{\mathrm{rc}}$ for moduli of degree $2d$ K3 surfaces: [ R\_{\mathrm{rc}} \mathrel{\mathop:}= \sum\_{i=1}\^{n_d} R_i \in \|n_d L\| ] where $R_i$ runs over all irreducible rational curves in the linear system $|L|$ of the polarization and $n_d$ is given by the Yau--Zaslow formula ((Alexeev and Engel 2023, Thm.\~10.2)).
In (Alexeev and Engel 2023), $R_{\mathrm{rc}}$ is shown to be recognizable for all $d$, so there exists a canonical semifan ${\mathcal{F}}^{\mathrm{rc}}$ with [ \overline{F_{2d}}^{ \mathcal{F} _{\bullet} } \cong \overline{F_{2d}} .] In degree $2$, ${\mathcal{F}}_{\mathrm{rc}}$ is a semifan but not a fan, and coarsens the Coxeter fan.
For elliptic K3 surfaces with divisor $s + \sum_{i=1}^{24} f_i$, the semifan is in fact a fan, which further refines the maximal cone of the Coxeter fan.
It is currently a widely open problem to describe the semifan ${\mathcal{F}}_R$ for a recognizable divisor in full generality, and is still open in the case of $R = R^{\mathrm{rc}}$ -- these are currently only characterized only as the coarsest subdivision such that the combinatorial type of stable pairs is constant on its cones.
Our work in (**AEGS23?**) relies on the fact that recognizability was proved for ramification loci of non-symplectic automorphisms in (Alexeev and Engel 2022), and explicit constructions of the corresponding semifans are provided.
:::

#### Generalized Coxeter Semifans and Relevant Roots

:::{#def:relevant-irrelevant .definition title="Relevant and irrelevant roots"}
Let $ \overline{T}_{ \eta } $ be the boundary lattice of signature $(1, n-1)$ for a $0$-cusp $\eta$, with stable reflection group $W = W(\Gamma_\eta)$, simple root system $\Phi = \Phi(\Gamma_\eta)$, and fundamental chamber $ \mathfrak{C} = \mathfrak{C} _\eta$.
The Coxeter diagram is $G = G(\Gamma_\eta)$. A partition $\Phi = \Phi^{\mathrm{rel}} \sqcup \Phi^{\mathrm{irr}}$ into **relevant** and **irrelevant** simple roots is defined as follows:

- The roots in $\Phi^{\mathrm{irr}}$ (the **irrelevant roots**) are those for which, in every Kulikov model over the cusp $\eta$, the faces of $ \mathfrak{C} $ defined using only mirrors from $\Phi^{\mathrm{irr}}$ correspond to strata that are contracted in the KSBA stable model over $\eta$.

- The **relevant roots** are those in $\Phi^{\mathrm{rel}} = \Phi \setminus \Phi^{\mathrm{irr}}$.
:::

:::{.definition title="Generalized Coxeter Semifan {[@AET19a, Def.~4.16]}
"}
Fix a partition $\Phi = \Phi^{\mathrm{irr}} \sqcup \Phi^{\mathrm{rel}}$.
Let $W^{\mathrm{irr}} = \langle w_\alpha {~\mathrel{\Big\vert}~} \alpha \in \Phi^{\mathrm{irr}} \rangle \subset W$ denote the reflection subgroup generated by reflections in the irrelevant roots.
The corresponding generalized chamber is $$
 \mathfrak{L}  = \bigcup_{h \in W^{\mathrm{irr}}} h( \mathfrak{C} )
$$ The corresponding **generalized Coxeter semifan** ${\mathcal{F}}_{\mathrm{gen}}$ is the semifan whose maximal cones are $g( \mathfrak{C} _{\mathrm{gen}} )$ for $g \in W$, with faces given by all intersections of maximal cones not contained in any wall $\alpha^\perp$ for $\alpha \in \Phi^{\mathrm{rel}}$.
:::

:::
remark
Passing from the Coxeter fan to the generalized Coxeter semifan corresponds to deleting nodes of $G(\Gamma_\eta)$ representing the irrelevant roots: walls $\alpha^\perp$ for $\alpha \in \Phi^{\mathrm{irr}}$ are omitted, so maximal cones become unions of Weyl chambers glued along these "inactive mirrors".
If $\Phi^{\mathrm{irr}} = \varnothing$, this recovers the Coxeter fan, while if $\Phi^{\mathrm{rel}} = \varnothing$, there is a single chamber and this recovers the Baily--Borel fan.
Moreover, if $|W^{\mathrm{irr}}| = \infty$, the resulting semifan is not locally finite, and the compactification is strictly semitoroidal.
Crossing a relevant wall $\alpha^\perp$ corresponds to a birational transformation -- such as a flip, flop, or divisorial contraction -- between KSBA stable models.
The chambers cut out by relevant walls in $ \mathfrak{C} $ correspond to regions where the combinatorial type of Kulikov (and hence stable) models remains constant.
:::

#### Generalized Coxeter compactifications

We thus obtain a natural, purely combinatorial way to interpolate between the maximal and minimal compactifications of $F_\Gamma$, which can be encoded in a single combinatorial object that we now describe.

:::{#def:semifanposet .definition title="{The semifan poset of a cone}
"}
Let $V$ be a real finite-dimensional vector space and $ \mathfrak{C} \subset V$ an open convex cone.
The **semifan poset** $\mathrm{SFan}( \mathfrak{C} )$ is the set of all semifans in $ \mathfrak{C} $, partially ordered by refinement: ${\mathcal{F}} \leq {\mathcal{F}}'$ if every cone of ${\mathcal{F}}$ is contained in a cone of ${\mathcal{F}}'$.
The maximal (finest) and minimal (coarsest) elements correspond to the finest locally polyhedral subdivision and the single full cone, respectively.
:::

:::{#def:semitoroidalposet .definition title="{The semitoroidal compactification poset}
"}
The **semitoroidal compactification poset** $ \mathcal{S} _\Gamma$ of $F_\Gamma$ is the set of isomorphism classes of semitoroidal compactifications $\overline{F_\Gamma,   \mathcal{F} _{\bullet} }^{  \mathcal{F} _{\bullet} }$ constructed from compatible systems of $\Gamma$-admissible semifans $ \mathcal{F} _{\bullet} $ ranging over the cusps $I$ of $\overline{F_\Gamma}^{ \operatorname{BB} }$. $ \mathcal{S} _\Gamma$ is partially ordered: $\overline{F_\Gamma}^{   \mathcal{F} _{\bullet}  } \leq \overline{F_\Gamma}^{   \mathcal{G} _{\bullet}  }$ if $ \mathcal{F} \_I$ refines $ \mathcal{G} \_I$ for all $I$.
This order is reversed under induced morphisms, i.e., coarser semifans yield "smaller" compactifications.
\todo{F and G} The maximal element corresponds to the maximal toroidal compactification; the minimal to the Baily--Borel compactification.
:::

\todo{Repeated}

:::{#def:coxetersemiposet .definition title="{The Coxeter semitoroidal compactification poset}
"}
For each $0$-cusp $\eta$ of $\overline{F_\Gamma}^{ \operatorname{BB} }$, let $G(\Gamma_\eta)$ be the stable Coxeter diagram, and $ \mathcal{P} _{G(\Gamma_\eta)}$ the poset of subdiagrams under inclusion.
Define the **Coxeter semitoroidal compactification poset** of $F_\Gamma$ as the coproduct poset $$
 \mathcal{P} _\Gamma \mathrel{\mathop:}=  \coprod_{\eta \in \partial\overline{F_\Gamma}^{ \operatorname{BB} }}  \mathcal{P} _{G(\Gamma_\eta)}
.$$ An element $(D_\eta) \in  \mathcal{P} _\Gamma$ specifies, for each $0$-cusp, a subdiagram $D_\eta \subset G(\Gamma_\eta)$ and thus a set of irrelevant roots at each cusp.
:::

:::{#prop:coxsemiposetmap .proposition title="{Coxeter semifan system and main identification}
"}
There is a canonical poset morphism $\Psi\colon  \mathcal{P} _\Gamma \longrightarrow  \mathcal{S} _\Gamma$ which sends a tuple $(D_\eta)$ of subdiagrams, one for each $0$-cusp $\eta$, to the induced semitoroidal compactification, constructed by gluing together maximal cones of generalized Coxeter semifans (as in \Cref{def:coxetersemiposet}) along all omitted walls, corresponding to the nodes omitted in $D_\eta$.
The maximal element of $ \mathcal{P} _\Gamma$, where no nodes are omitted, corresponds to the Coxeter fan and thus the toroidal compactification. The minimal element, where all nodes are omitted at each cusp, corresponds to the Baily--Borel fan $\Sigma^{\operatorname{BB}}$ and thus $\overline{F_\Gamma}^{ \operatorname{BB} }$. Morphisms in $ \mathcal{P} _\Gamma$ corresponding to deleting more nodes correspond to coarsenings of the semifans and thus to proper birational morphisms between the corresponding semitoroidal compactifications.
:::

:::
remark
The poset $ \mathcal{S} _\Gamma$ of semitoroidal compactifications organizes all normal compactifications arising from systems of $\Gamma$-admissible semifans over the boundary strata of $F_\Gamma$. The Coxeter semitoroidal subposet $ \mathcal{P} _\Gamma$ parameterizes those compactifications obtained as Coxeter-type (generalized Coxeter semifan) coarsenings of local reflection decompositions, and is canonically identified with the product of subdiagram posets at all $0$-cusps.
The product $ \mathcal{P} _\Gamma$ thus parametrizes exactly the semitoroidal compactifications of $F_\Gamma$ arising from generalized Coxeter semifans, distinguished in the full semitoroidal poset $ \mathcal{S} _\Gamma$.
Note that the latter may contain other compactifications, and the author is not aware of any choices of $F_\Gamma$ for which $\Psi$ is known to be surjective or bijective.
:::

<!-- Source: 2-part-moduli/4-chapter-cpt/400-ksba-functor.md -->

### KSBA Compactifications {#setion-5-3}

#### Introduction {#introduction}

For higher-dimensional varieties, GIT, toroidal, and semitoroidal compactifcations are often inadequate, producing boundary points that lack modular interpretations and possibly corresponding to degenerations with excessively severe singularities.
For instance, GIT compactification $F_2$ result in boundary strata containing highly singular, non-separated, or even non-reduced curves.
Such limiting surfaces may not be uniquely determined by one-parameter degenerations, violating the valuative criterion for properness and separatedness.
Moreover, GIT boundaries often allow non-slc singularities, which are more severe than those typically permitted by the MMP (see e.g., (**Shah80?**), (**Looijenga86?**)). In contrast, for curves of genus $g \geq 2$, Deligne and Mumford compactify $ \mathcal{M}*{g}$ using **stable curves**: a (connected, reduced, projective) curve $C$ over an algebraically closed field is **stable** if all singularities of $C$ are nodes and every rational component of $C$ meets the rest of $C$ (including the marked points) in at least $3$ points.
The moduli functor $ \mathcal{M}*{g}^{\operatorname{DM}}$ assigning to each connected base $S$ the groupoid of flat, proper families ${\mathcal{C}} \to S$ whose fibers are stable curves, is represented by a proper Deligne--Mumford stack.
The boundary $\partial  \mathcal{M}*{g}$ parameterizes connected, nodal curves with finite automorphism groups, and every family $C^\circ$ over $S^\circ = S \setminus \left\{{0}\right\}$ admits, after a ramified base change, a unique stable limit by semistable reduction and relative abundance of $\omega*{C/S}$ (see (P. Deligne and Mumford 1969), (**Kollár96?**)). The **boundary strata** of $\partial  \mathcal{M}_{g}$ are indexed by **dual graphs** recording the incidence data of components and their intersections -- each stable degeneration's combinatorial "type" corresponds to the dual graph of its ${\mathcal{X}}_0$, and each such graph describes a distinct boundary stratum (see (P. Deligne and Mumford 1969), (**Kollár96?**)).

To generalize this to higher dimension, one introduces **stable pairs** $(X, B)$, following (**KSB88?**), (**Alexeev96?**). Such a pair is **KSBA stable** if:

- $X$ is a projective, reduced, equidimensional, *demi-normal* variety of dimension $d \geq 2$,
- $B = \sum b_i B_i$ is an effective ${\mathbf{Q}}$-divisor, $0 < b_i \leq 1$,
- The pair $(X, B)$ has **semi-log-canonical (slc) singularities**,
- $K_X + B$ is ample.

KSBA stability ensures:

- (**Properness**) Any flat family $({\mathcal{X}}^*, {\mathcal{B}}^*) \to \Delta^*$ over the punctured disk extends, after finite base change, to a family $({\mathcal{X}}, {\mathcal{B}}) \to \Delta$ of stable pairs with ${\mathcal{X}}*0$ $(X_0, B_0)$ slc and $K*{X_0} + B_0$ ample.

- (**Separatedness**) Any isomorphism over $\Delta^*$ extends uniquely over $\Delta$.

- (**Modularity**) Every point of the boundary parameterizes a geometric, unique, slc limit.

For curves, setting $d=1$ and $B$ the be the sum of markings, this recovers the notion of stable curves as $\omega_C(\sum_i p_i)$ ample and only nodes allowed.
However, unlike the case of curves, where all stable curves are smoothable, not every stable variety is a limit of smooth ones.
Thus, boundary components can include non-smoothable varieties, yielding compactifications that potentially have multiple irreducible components.
Fixing discrete invariants -- the dimension $d$, a Hilbert polynomial $h$, boundary coefficients $\{b_i\}$, and the **volume** $(K_X + B)^d$ --, the **KSBA moduli functor** $\overline{{\mathcal{M}}}_{d, \vec{b}, v}: \operatorname{Sch}^{\mathrm{op}} \to \operatorname{\mathsf{Sets}}$ assigns to $S$ the set of isomorphism classes of flat families $({\mathcal{X}}, {\mathcal{B}}) \to S$ of KSBA stable pairs with these invariants.
This functor is represented by a proper, separated Deligne--Mumford stack ${\mathcal{M}}$, whose coarse moduli space $M$ is a projective scheme [KSB88, Thm 1.1]. The closure of the locus of smooth pairs in ${\mathcal{M}}$ provides a geometrically meaningful compactification by stable pairs.

For K3 or Enriques surfaces, $K_X \equiv 0$ is numerically trivial, so to ensure ampleness one considers **pairs** $(X, \varepsilon R)$ for $0 < \varepsilon \ll 1$, $R$ ample divisor, and studies the stable pair locus for these data.
The divisor $R$ is typically chosen to be the ramification divisor of an automorphism, and the compactification is independent of $\varepsilon$ for $\varepsilon$ sufficiently small ((**KSB88?**), (**Alexeev96?**), (János Kollár 2023, Lemma VI.1.1), (**AET19?**)). For $K3$ surfaces with polarization of degree $2d$, a **divisor model** refers to the representation of a $K3$ surface $X$ together with an ample Cartier divisor $L$ of degree $2d$ -- concretely, for $d = 1$, this is a double cover of ${\mathbf{P}}^2$ branched along a sextic.
The stability condition requires $(X, L)$ to be log canonical with $K_X + L$ ample.
The KSBA compactification $ \overline{F} \_{2d}$ for such pairs compactifies the moduli space of smooth pairs $(X, L)$ by adding K3 surface pairs with at worst ADE/slc singularities.
These are parameterized by **integral affine spheres** $\mathrm{IAS}^2$ with 24 singularities.
For Enriques surfaces the boundary of the KSBA compactification naturally includes **half-divisor models**: pairs $(Z, \Delta)$, where $Z$ is an Enriques surface and $\Delta$ is an effective Weil divisor determined by the universal K3 cover $X\to Z$, often defined only up to numerical equivalence or descent $X$.
These are in turn parametrized by $\mathrm{IAS}^2$ with involutions.

#### Singularities

\todo{Copy in all of the comments/remarks from notes.}

:::{#sing-deminormal .definition title="Demi-normal Variety"}
A variety $X$ is **demi-normal** if $X$ is reduced, \$ X \$ is \$ S_2 \$ and normal crossing in codimension one (every codimension one singularity is analytically isomorphic to a normal crossing or ordinary node).
:::

:::{#sing-s2 .definition title="Serre’s $S_2$ Condition"}
A Noetherian scheme $X$ satisfies **Serre's $S_2$ condition** if, for every $x\in X$, $\operatorname{depth}\, {\mathcal{O}}_{X,x} \geq \min\{2, \dim {\mathcal{O}}_{X,x}\}.$ For surfaces, $S_2$ implies $X$ is Cohen--Macaulay in codimension one.
:::

:::{#sing-snc .definition title="Simple Normal Crossings (snc)"}
A variety $X$ has **simple normal crossings (snc)** singularities if, at each point $x \in X$, there exists an analytic or étale neighborhood isomorphic to $(x_1 x_2 \cdots x_k = 0)\subset {\mathbf{A}}^n$ for some $k \leq n$, i.e., $X$ locally looks like $k$ coordinate hyperplanes.
:::

:::{#sing-gor-qgor .definition title="Gorenstein and $\{\mathbf{Q}
}$-Gorenstein Varieties"}
A scheme $X$ of pure dimension is **Gorenstein** if it is Cohen--Macaulay and its dualizing sheaf $\omega_X$ is invertible.
$X$ is **${\mathbf{Q}}$-Gorenstein** if $\omega_X$ is ${\mathbf{Q}}$-Cartier, i.e., some positive tensor power $\omega_X^{\otimes m}$ is invertible for $m > 0$.
:::

:::{#pairs-ade .definition title="ADE Singularities (Du Val, Rational Double Points)"}
An **ADE singularity** (Du Val or rational double point) is a normal surface singularity whose minimal resolution has exceptional curves intersecting according to an ADE Dynkin diagram with analytic forms:

`\begin{align*}
A_n &\colon x^2 + y^2 + z^{n+1} = 0 \\
D_n &\colon x^2 + y^{n-1} + y z^2 = 0 \\
E_6 &\colon x^2 + y^3 + z^4 = 0 \\
E_7 &\colon x^2 + y^3 + y z^3 = 0 \\
E_8 &\colon x^2 + y^3 + z^5 = 0
\end{align*}`{=tex}
:::

:::{#sing-normalization .definition title="Normalization and Double Locus"}
Let \$ X \$ be a reduced, demi-normal scheme, as defined above.
The **normalization** of $X$ is a finite birational morphism [ \nu\colon \overline{X} \to X ] with $ {X}^{\nu} $ normal, universal among morphisms from normal schemes to $X$.
\### Definition: The Conductor Subscheme and Double Locus

Let \$ X \$ be a reduced scheme and let \$ \nu: \widetilde{X} \to X \$ denote its normalization.
The **conductor ideal sheaf** is defined as [ \mathcal{C}*X := \operatorname{Ann}*{{\mathcal{O}}*X}\big( \nu*\* {\mathcal{O}}\_{\widetilde{X}} / {\mathcal{O}}\_X \big). ]

This ideal sheaf gives rise to two closed subschemes:

- The **conductor subscheme** (or **conductor locus**) on \$ X \$, defined by \$ \mathcal{C}\_X \subseteq {\mathcal{O}}\_X \$.
  This locus coincides with the points where \$ \nu \$ is not an isomorphism, i.e., where \$ X \$ is not normal.
- The **conductor divisor** on \$ \widetilde{X} \$, which is the closed subscheme cut out by pulling back the conductor ideal via \$ \nu \$.

The **double locus** of \$ X \$ is the support of the conductor subscheme on \$ X \$.
Equivalently, it is the locus where \$ X \$ fails to be normal---typically, the set of points where two or more local analytic branches of the normalization are identified in \$ X \$.
:::

For algebraic surfaces, the double locus is a (possibly reducible) disjoint union of curves (i.e., it is of pure codimension one).
In higher dimensions, the conductor always has pure codimension one in \$ X \$.
The preimage of the conductor divisor in \$ \widetilde{X} \$ records the precise locations where the gluing occurs in the normalization, thus encoding the identification data required to reconstruct \$ X \$ from its normalization.
Normalization replaces a reduced scheme $X$ with a normal scheme $ {X}^{\nu} $ up to birational equivalence, and the fibers of $ {X}^{\nu} \to X$ encode the branching behavior of the singularity at that point.
Its practical implications by dimension are as follows:

- $\dim(X) = 1:$ The normalization of a reduced curve $C$ is a smooth curve $\widetilde{C}$.

- $\dim(X) = 2:$ Normalization resolves all non-normal singularities, such as double curves and cusps, and more generally all 1-dimensional singularities, leaving only singularities at isolated points (which are typically ADE or quotient singularities).

- $\dim(X) \geq 3:$ The singular locus of $ {X}^{\nu} $ is of codimension at least 2, and consists of *normal singularities* -- these can generally be complicated.

:::{.theorem title="Zariski's Main Theorem (Recognition Theorem for Normalizations)"}
Let $X$ be a reduced, separated, Noetherian scheme, and let $f \colon Y \to X$ be a morphism.
Then $f$ is (up to unique isomorphism) the normalization of $X$ if and only if:

1.  $Y$ is normal,
2.  $f$ is finite and birational,
3.  $f$ restricts to an isomorphism over the open subset of $X$ where $X$ is normal (i.e., over the normal locus of $X$).

In other words, any morphism with these three properties realizes $Y$ as the normalization of $X$.
In particular, if $X$ is an irreducible, reduced, separated variety over ${\mathbf{C}}$ such that

1.  $Y$ is normal and irreducible, and
2.  $f$ is finite and birational,

then $Y$ is the normalization of $X$ and $f$ is the normalization morphism.
In this case, $f$ is an isomorphism over the smooth locus of $X$.
:::

#### Pairs

:::{#pairs-logpair .definition title="Log Pair $(X, D)$"}
A **log pair** is a pair $(X, D)$, where $X$ is a normal variety over ${\mathbf{C}}$ and $D = \sum d_i D_i$ is an effective ${\mathbf{Q}}$-divisor on $X$ with coefficients $0 \leq d_i \leq 1$.
:::

:::{#pairs-lc .definition title="Log Canonical (lc) Singularities"}
Let \$ X \$ be a normal variety over \$ {\mathbf{C}} \$, and let \$ R = \sum r_i R_i \$ be an effective \$ {\mathbf{Q}} \$-divisor with \$ 0 \leq r_i \leq 1 \$.
For any log resolution \$ f\colon Y \to X \$, and for each prime divisor \$ E \$ on \$ Y \$, the **discrepancy** \$ a(E, X, R) \$ is defined by [ K_Y = f\^\*(K_X + R) + \sum\_E a(E, X, R), E. ] Let \$ (X, D) \$ be a log pair, where \$ X \$ is a normal variety and \$ D \$ is a $\mathbb{Q}$-divisor.
The pair is said to be **log canonical** (lc) if \$ K_X + D \$ is $\mathbb{Q}$-Cartier and, for every log resolution \$ f: Y \to X \$ and every prime divisor \$ E \$ on \$ Y \$, the discrepancy satisfies \$ a(E, X, D) \geq -1 \$.
A **log canonical center** of \$ (X, D) \$ is the image \$ f(E) \subseteq X \$ of a prime divisor \$ E \$ on some log resolution \$ f: Y \to X \$ with discrepancy \$ a(E, X, D) = -1 \$; this locus is precisely where the singularities of the pair are exactly log canonical.
:::

The minimal model program (MMP) distinguishes four main classes of singularities for pairs, ordered by the values their discrepancies may attain.
Let \$ f: Y \to X \$ be any log resolution and \$ E \$ a prime divisor on \$ Y \$:

Here is a revised version of the passage, rewritten for clarity, precision, and stylistic consistency with a research monograph such as the *Annals of Mathematics*. Technical terms are used with care, and informal phrasing has been eliminated:

* * *

### Classes of Singularities for Pairs $(X, D)$

Let $(X, D)$ be a normal pair with $K_X + D$ $\mathbb{Q}$-Cartier.
For a birational morphism $f : Y \to X$, and a prime divisor $E \subset Y$, the discrepancy $a(E, X, D)$ is defined via the relation $$ K_Y + D_Y = f^*(K_X + D) + \sum_E a(E, X, D) \cdot E, $$ where $D_Y$ is the strict transform of $D$.
The classification of singularities according to the discrepancy function is given below.

* * *

Class Discrepancy Condition Typical Applications

* * *

Terminal $a(E, X, D) > 0$ Minimal models in dimension $\geq 3$

Canonical $a(E, X, D) \geq 0$ Canonical models; moduli of varieties of general type

Kawamata log terminal (klt) $a(E, X, D) > -1$ Singularities allowed in the Minimal Model Program

Log canonical (lc) $a(E, X, D) \geq -1$ Stable pairs; compactifications of moduli spaces

* * *

- **Terminal:** All discrepancies are strictly positive.
  Such singularities are the mildest allowed in the context of minimal models in dimension at least three, ensuring $\mathbb{Q}$-factoriality and smoothness in codimension two.

- **Canonical:** Discrepancies are nonnegative.
  Canonical singularities permit discrepancies to vanish but exclude boundary contributions with coefficient one.
  They are characteristic of canonical models and appear naturally in the classification of varieties of general type.

- **Kawamata log terminal (klt):** All discrepancies satisfy $a(E, X, D) > -1$.
  These include quotient singularities and allow boundary divisors with coefficients in $(0,1)$.
  klt pairs form the primary class of singularities admissible in the Minimal Model Program.

- **Log canonical (lc):** Discrepancies satisfy $a(E, X, D) \geq -1$.
  This is the broadest class considered in the birational classification of pairs, accommodating boundary components with coefficient one.
  lc singularities are essential in the theory of stable pairs and in the construction of compactified moduli spaces.

Let me know if you'd like to add references (e.g., [Kollár--Mori, *Birational Geometry of Algebraic Varieties*]) or extend this table to include dlt or plt singularities.

When the condition \$ a(E, X, D) \geq -1 \$ is enforced, the essential steps of the MMP---flips, divisorial contractions, and the extraction of minimal and canonical models---can be performed, and the canonical ring remains finitely generated.
If one allows singularities with discrepancies less than $-1$, these procedures can fail, and fundamental theorems such as the existence of minimal models or the finiteness of the canonical ring may break down.
Thus, log canonical singularities constitute the maximal class for which the program is expected to be valid.
Canonical and log canonical singularities appear naturally on canonical models of varieties of general type, and this inclusion ensures that the canonical ring has the necessary finiteness properties.
The MMP is specifically designed so that, under finite generation, canonical models admit at worst lc singularities, which are thus the natural endpoint for varieties of general type constructed via the MMP.

:::{#pairs-dlt .definition title="Divisorial Log Terminal (dlt) Singularities"}
A pair \$ (X, D) \$, where \$ X \$ is normal and \$ D \$ is an effective \$ {\mathbf{Q}} \$-divisor, is said to be **divisorial log terminal (dlt)** if \$ K_X + D \$ is \$ {\mathbf{Q}} \$-Cartier, and there exists a log resolution \$ f \colon Y \to X \$ such that:

- for every \$ f \$-exceptional divisor \$ E \$, the discrepancy \$ a(E, X, D) \> -1 \$,
- the union of the strict transform of \$ D \$ with the \$ f \$-exceptional divisors is a simple normal crossings (snc) divisor,
- all log canonical centers are contained in the support of the strict transform of \$ D \$.
:::

:::{#pairs-slc .definition title="Semi-Log Canonical (slc) Pairs"}
Let \$ X \$ be a demi-normal scheme and \$ R = \sum r_i R_i \$ an effective \$ {\mathbf{Q}} \$-divisor on \$ X \$ with \$ 0 \leq r_i \leq 1 \$.
The pair \$ (X, R) \$ is called **semi-log canonical (slc)** if:

1.  \$ K_X + R \$ is \$ {\mathbf{Q}} \$-Cartier.

2.  \$ ( {X}^{\nu} , R\^\nu) \$ is log canonical, wher e\$ \nu\colon {X}^{\nu} \to X \$ is the normalization of \$ X \$ and [ R\^\nu \mathrel{\mathop:}= D + \sum r_i, \nu\^\*(R_i). ] where \$ D \$ be the conductor divisor on \$ {X}^{\nu} \$.
    :::

Semi-log canonical singularities generalize lc singularities to possibly non-normal varieties.
In this setting, \$ X \$ is allowed to have certain mild singularities, notably double crossings in codimension one.
The normalization \$ \nu: \widetilde{X} \to X \$ separates these non-normal loci, and the conductor divisor \$ D \subset \widetilde{X} \$ records the preimage of the non-normal (double) locus of \$ X \$.
The pair \$ (\widetilde{X}, R\^\nu) \$ combines the pullback of \$ R \$ and the conductor divisor, and being lc in this setting captures the requirement that singularities of the normalization and the identifications along the conductor divisor are at worst log canonical; that is, all discrepancies for the pair \$ (\widetilde{X}, R\^\nu) \$ are at least $-1$, both on the components of \$ \widetilde{X} \$ and along the loci where the components are glued together via the conductor.
This allows the extension of the MMP and moduli of pairs to schemes that are not necessarily normal or irreducible.
In particular, slc pairs arise naturally as stable limits of pairs in families where the total space acquires non-normal singularities, making them central objects in the compactification of moduli spaces of pairs.

::: {#pairs-qp-minimalres .definition title="Quasi-polarized Minimal Resolutions and Deformation Types"}
Given a pair \$ (X, R) \$, where \$ X \$ is a surface with at worst ADE or quotient singularities and \$ R \$ is a nef (or ample) divisor, the **quasi-polarized minimal resolution** is the pair \$ (\tilde{X}, f\^\* R) \$, where \$ f \colon \tilde{X} \to X \$ is the minimal crepant resolution of \$ X \$.
The **deformation type** of a (possibly singular) surface with an ample line bundle (or quasi-polarization) is the isomorphism class (up to analytic or algebraic equivalence) of its quasi-polarized minimal resolution.
:::

#### Numerical Conditions and Models

:::{#div-big-nef .definition title="Big and Nef Divisors"}
Let $D$ be a ${\mathbf{Q}}$-Cartier divisor on a projective variety $X$:

- $D$ is **nef** (numerically effective) if $D \cdot C \geq 0$ for every irreducible curve $C \subset X$.
- $D$ is **big** if its volume is positive, $\operatorname{vol}_X(D) \mathrel{\mathop:}=  \limsup_{m \to \infty} \frac{h^0(X, {\mathcal{O}}_X(mD))}{m^{\dim X}/\dim X!} > 0.$
:::

:::{#div-polarization .definition title="Polarizing, Primitive, and Quasi-Polarizing Divisors"}
Let $X$ be a projective variety.
A **polarizing divisor** is an ample Cartier divisor $R$ on $X$.
We say $R$ is a **quasi-polarizing divisor** if it is only big and nef, but not necessarily ample.
It is **primitive** if its class in $\operatorname{Pic}(X)$ cannot be written as $kL'$ for any integer $k > 1$ and any divisor $L'$.
:::

Ample divisors guarantee that $X$ is projective.
making polarizations especially common in moduli problems, where it ensures that the moduli stack is proper and separated.
Nefness provides a numerical positivity condition that yields well-defined numerical invariants, and since it is preserved under birational equivalence, it ensures that the singularities of degenerations are mild enough to be controlled by the MMP. Bigness is a maximality condition, selecting divisors whose sections grow like ample divisors.
Quasi-polarizations arise naturally as limits of polarizations: degenerations of polarized KSBA pairs can induce a loss of ampleness, while bigness and nefness persist.
Finally, primitivity imposes a minimality and uniqueness condition (up to isomorphism) on the divisor class, ensuring that each isomorphism class is represented exactly once in the corresponding moduli problem, avoiding redundancies due to rescaling.

:::{#hdm-nefmodel .definition title="Nef Model"}
Let ${\mathcal{X}}^* \to \Delta^*$ be a flat family over a punctured disk, and let ${\mathcal{L}}^*$ be a relatively big and nef line bundle on ${\mathcal{X}}^*$.
A **nef model** for $({\mathcal{X}}^*, {\mathcal{L}}^*)$ is a pair $({\mathcal{X}}, {\mathcal{L}})$ where:

- ${\mathcal{X}} \to \Delta$ is a flat extension of ${\mathcal{X}}^* \to \Delta^*$ (often a Kulikov or semistable model),
- ${\mathcal{L}}$ is a line bundle on ${\mathcal{X}}$ extending ${\mathcal{L}}^*$,
- ${\mathcal{L}}$ is relatively nef and big over $\Delta$.
:::

Given a family \$ \mathcal{X}^\*\ \to \Delta^\* \$ of smooth varieties over a punctured disk and a relatively big and nef line bundle \$ \mathcal{L}\^\* \$ or an effective divisor \$ {\mathcal{R}}^\*\ \subset \mathcal{X}^\* \$, the problem is to construct canonical extensions of this data over the whole disk \$ \Delta \$, especially over the ${\mathcal{X}}_0$ \$ \mathcal{X}\_0 \$.

Such extensions must satisfy several requirements dictated by the geometry of degenerations and the construction of compactified moduli spaces:

- The extension \$ (\mathcal{X}, \mathcal{L}) \$ or \$ (\mathcal{X}, {\mathcal{R}}) \$ must be flat over \$ \Delta \$, so that the fibers capture the correct limit structure as the family degenerates.
  Note that flatness of a family ensures that the fibers vary in a "continuous" manner from a scheme-theoretic perspective, yielding equidimensionality and consistent Hilbert polynomial across the family.

- The positivity properties of the line bundle or divisor---such as nefness and ampleness---must be preserved on the total space to ensure that the relevant moduli functor remains separated and proper.

- In the case of divisors, compatibility with the stratification of the ${\mathcal{X}}_0$ is essential: the ${\mathcal{X}}_0$ of the divisor should avoid all strata of the possibly singular ${\mathcal{X}}_0$, so as not to introduce unwanted components or increase the complexity of the limit.

Precisely formulating these extensions is essential for defining and constructing stable limits.
They form the starting point for constructing stable limits, which are stable pairs arising as canonical limits of smooth pairs in families.
The following definition captures the precise requirements for extending divisors across degenerations:

:::{#hdm-divmodel .definition title="Divisor Model"}
Let ${\mathcal{X}}^* \to \Delta^*$ be a family of varieties over a punctured disk and let ${\mathcal{R}}^* \subset {\mathcal{X}}^*$ be an effective divisor (usually a section of a relatively nef and big line bundle).
A **divisor model** for $({\mathcal{X}}^*, {\mathcal{R}}^*)$ is a pair $({\mathcal{X}}, {\mathcal{R}})$, where:

- ${\mathcal{X}} \to \Delta$ is a flat family extending ${\mathcal{X}}^* \to \Delta^*$,
- ${\mathcal{R}}$ is an effective divisor on ${\mathcal{X}}$ restricting to ${\mathcal{R}}^*$ on ${\mathcal{X}}^*$,
- ${\mathcal{R}}$ is relatively nef over $\Delta$,
- The ${\mathcal{X}}_0$ ${\mathcal{R}}_0$ does **not contain any stratum** of the ${\mathcal{X}}_0$ ${\mathcal{X}}_0$; that is, ${\mathcal{R}}_0$ does not contain any irreducible component or singular locus (double curves, triple points, etc.) of ${\mathcal{X}}_0$.
:::

:::{#hdm-exuniq-prop .proposition title="Existence and Uniqueness of Stable Limits via Divisor Models"}
Let $({\mathcal{X}}^*, {\mathcal{R}}^*)$ be a flat family of smooth pairs over $\Delta^*$.
After finite base change, there exists a divisor model $({\mathcal{X}}, {\mathcal{R}})$ as above.
The associated **stable model** is the pair $(\overline{{\mathcal{X}}}, \overline{{\mathcal{R}}} )$, where $$
(\overline{{\mathcal{X}}}, \overline{{\mathcal{R}}}) \mathrel{\mathop:}=  \operatorname{Proj}_\Delta \left(\bigoplus_{n \geq 0} H^0({\mathcal{X}}, {\mathcal{O}}_{{\mathcal{X}}}(n {\mathcal{R}}))\right)
.$$ For $0 < \varepsilon \ll 1$, the pair $(\overline{{\mathcal{X}}}, \varepsilon \overline{{\mathcal{R}}})$ is KSBA-stable: $\overline{{\mathcal{X}}}$ has slc singularities and $K_{\overline{{\mathcal{X}}}} + \varepsilon \overline{{\mathcal{R}}}$ is ample.

This stable limit is unique up to isomorphism (after base change), and the construction is functorial in families.
It provides a canonical procedure for extending any family of smooth pairs to a stable pair in the boundary of the KSBA moduli space, ensuring the properness of the compactification.
:::

:::{#hdm-halfdivisor .definition title="Half-Divisor Model"}
A **half-divisor model** is a pair $({\mathcal{Z}}, {\mathcal{R}}_{{\mathcal{Z}}})$ consisting of a flat family ${\mathcal{Z}} \to C$ over a base curve $C$, together with a divisor ${\mathcal{R}}_{{\mathcal{Z}}} \subset {\mathcal{Z}}$, such that the pair arises as the quotient of a divisor model $({\mathcal{X}}, {\mathcal{R}}) \to C$ by a fixed-point-free involution $\tau$ with ${\mathcal{R}}$ anti-invariant (i.e., ${\mathcal{R}}$ does not descend as a Cartier divisor, but $2{\mathcal{R}}$ does).
Equivalently, $({\mathcal{Z}}, {\mathcal{R}}_{{\mathcal{Z}}})$ is locally modeled as $({\mathcal{X}}/\tau, {\mathcal{R}}/\tau)$ where ${\mathcal{R}}$ is a "half" of a Weil divisor that becomes Cartier only after passing to the double cover.
:::

Let \$ \mathcal{X} \to C \$ be a flat family of K3 surfaces over a smooth curve, equipped with a fixed-point-free involution \$ \tau \$, and let \$ {\mathcal{R}} \subset \mathcal{X} \$ be an effective Cartier divisor that is anti-invariant under \$ \tau \$ (i.e., \$ \tau\^\* {\mathcal{R}} = -{\mathcal{R}} \$). The quotient family [ \pi \colon (\mathcal{X}, {\mathcal{R}}) \to ({\mathcal{Z}}, {\mathcal{R}}*{{\mathcal{Z}}}) ] with \$ {\mathcal{Z}} = \mathcal{X} / \langle \tau \rangle \$, yields a family of Enriques surfaces together with a divisor \$ {\mathcal{R}}*{{\mathcal{Z}}}\$ defined as the scheme-theoretic image of \$ {\mathcal{R}} \$.
In general, \$ {\mathcal{R}}*{{\mathcal{Z}}}\$ is a Weil divisor on \$ {\mathcal{Z}} \$ that is not Cartier, but its double \$ 2{\mathcal{R}}*{{\mathcal{Z}}}\$ is always Cartier.
This reflects a fundamental feature of Enriques surfaces: the divisor defining the marking or polarization typically does not descend to a Cartier divisor through a degree two étale cover with empty branch locus.
Instead, the presence of the involution ensures there is global 2-torsion in the divisor class group, leading to the condition $2{\mathcal{R}}*{{\mathcal{Z}}}\in \operatorname{CaDiv}({\mathcal{Z}}) \quad \text{but} \quad {\mathcal{R}}*{{\mathcal{Z}}}\notin \operatorname{CaDiv}({\mathcal{Z}}).$ This half-divisibility characterizes polarized Enriques surfaces and persists in their degenerations.
When the ${\mathcal{X}}*0$ degenerates (\$ (\mathcal{X}\_0, {\mathcal{R}}\_0) \$), it may become reducible, and the involution specializes to \$ \tau_0 \$ on \$ \mathcal{X}\_0 \$.
The quotient \$ {\mathcal{Z}}\_0 = \mathcal{X}\_0 / \langle \tau*0 \rangle \$ is then a demi-normal surface, and the induced divisor \$ {\mathcal{R}}*{{\mathcal{Z}}*0} \$ remains a Weil divisor with \$ 2{\mathcal{R}}*{{\mathcal{Z}}\_0} \$ Cartier.
In the context of the KSBA compactification, every boundary stratum corresponding to a stable limit of Enriques surfaces is thus naturally modeled by half-divisor pairs \$ ({\mathcal{Z}}*0, \frac{1}{2} {\mathcal{R}}\*{{\mathcal{Z}}\_0}) \$, with log-canonical polarization $K*{{\mathcal{Z}}*0} + \frac{1}{2} {\mathcal{R}}*{{\mathcal{Z}}_0}$ ample, and with semi-log-canonical singularities that may arise both from the quotient construction and from singularities already present in the K3 ${\mathcal{X}}_0$.
As discussed in (**AEGS23?**), the structure of degenerations of Enriques surfaces are thus governed by half-divisor models in this way.

#### The KSBA Moduli Stack

:::{.definition title="KSBA Stable Pair"}
Let $X$ be a projective, demi-normal (in particular, $S_2$ and normal crossing in codimension one) variety over an algebraically closed field of characteristic $0$, and let $D = \sum_j a_j D_j$ be an effective ${\mathbf{Q}}$-divisor with $0 < a_j < 1$ and each component $D_j$ a Weil divisor whose support does not contain any component of the double locus of $X$.
The pair $(X, D)$ is called a **(KSBA) stable pair** if:

- $(X, D)$ is semi-log-canonical (slc): $X$ is $S_2$; $(X, D)$ is slc in the sense of Section I, i.e., the normalization with the conductor plus pullbacks of $D$ is log canonical, and $K_X + D$ is ${\mathbf{Q}}$-Cartier,
- $K_X + D$ is ample,
- $\operatorname{Aut}(X, D)$ is finite (which follows from ampleness and $X$ reduced).
:::

:::{.definition title="Dual Complex of a Stable Degeneration"}
Let $\overline{X}$ be a reduced, finite-type, possibly reducible variety arising as the ${\mathcal{X}}_0$ of a degeneration of KSBA stable pairs.
The **dual complex** $\Gamma(\overline{X})$ is the simplicial complex defined by:

- **Vertices:** Each irreducible component $\overline{V}_i$ of $\overline{X}$ corresponds to a vertex.

- **$k$-Simplices:** For every connected component of the intersection of $k+1$ distinct irre0ducible components $\overline{V}_{i_0} \cap \overline{V}_{i_1} \cap \cdots \cap \overline{V}_{i_k}$ (with nonempty intersection), include a $k$-simplex whose vertices correspond to the involved components.

- **Faces and Gluing:** The simplices are glued according to inclusions of the corresponding strata.

The dual complex $\Gamma(\overline{X})$ thus encodes precisely the combinatorics of how the irreducible components of the degeneration $\overline{X}$ meet along their strata of higher codimension.
:::

:::{#moduli-functor .definition title="KSBA Moduli Functor"}
Fix numerical invariants (such as dimension $d$, Hilbert polynomial $h$, coefficients $\{a_j\}$, and volume $v = (K_X+D)^d$).
The **KSBA moduli functor** is $$
{\mathcal{M}}^{\mathrm{KSBA}}_{d,\vec{a},v} \colon (\operatorname{Sch}/k)^{\mathrm{op}} \to \operatorname{\mathsf{Sets}}
$$ assigning to each $S$ the set of isomorphism classes of families of KSBA stable pairs $({\mathcal{X}}, {\mathcal{D}} ) \to S$ with the fixed invariants.
:::

:::{#moduli-dmstack .definition title="KSBA Moduli Stack and Coarse Moduli Space"}
There exists a Deligne--Mumford stack ${\mathcal{M}}^{\mathrm{KSBA}}_{d, \vec{a}, v}$ of finite type over $k$, whose geometric points parametrize KSBA stable pairs with the chosen invariants.
The associated **coarse moduli space** $M^{\mathrm{KSBA}}_{d, \vec{a}, v}$ is an algebraic space, which is a projective scheme in many important cases.
:::

:::{#moduli-properness .theorem title="Properness and Projectivity of the KSBA Moduli Space"}
The stack ${\mathcal{M}}^{\mathrm{KSBA}}_{d, \vec{a},v}$ is separated and proper, and its coarse moduli space $M^{\mathrm{KSBA}}_{d, \vec{a}, v}$ is projective.
Any family of smooth (or slc) stable pairs over a punctured disk extends (after finite base change) to a family over the disk with a unique stable pair as ${\mathcal{X}}_0$; any isomorphism over the ${\mathcal{X}}_t$ extends uniquely.
Thus, $M^{\mathrm{KSBA}}_{d, \vec{a}, v}$ is a modular compactification of the moduli of smooth pairs.
:::

#### The KSBA Stack of $K$-Trivial Pairs

<!-- [AET19, Prop. 3.8] -->

Varieties with $K_X\sim 0$ numerically trivial, such as $K3$ and Enriques surfaces, are said to be **$K$-trivial**. They require special treatment in the theory of KSBA stable pairs and compactifications because the stability condition (ampleness of $K_X + R$) can not hold when $R=0$.
So one must *always* choose a nontrivial divisor $R$ for such varieties, and the positivity must be entirely supplied by $R$ in order to achieve any kind of stability.
We are thus lead, as a first approximation, to consider pairs $(X, R)$.
However, the MMP and KSBA compactification require pairs $(X, D)$ where each component $D_i$ of $D$ appears with coefficient $a_i < 1$, noting that this must be a *strict* inequality.
This ensures that limits have only slc singularities and that stability is preserved in families, and avoids the complications that arise in the $a_i = 1$ case -- infinite stabilizers leading to Artin stacks instead of Deligne-Mumford stacks, more severe non-slc singularities in degenerations, a potential loss of separatedness, and so on.
Thus, in the $K$-trivial setting, one "perturbs" the canonical class by achieve the necessary positivity, by considering pairs $(X, \varepsilon R)$ with a small rational coefficient $0 < \varepsilon \ll 1$.
For sufficiently small $\varepsilon$, the sum $K_X + \varepsilon R$ becomes ample and thus $(X, \varepsilon R)$ is KSBA stable.
With this setup, the moduli of stable $K$-trivial pairs is realized as a special locus in the general KSBA moduli stack described above, and all the foundational results (properness, separatedness, projectivity, etc.) apply directly.

:::{.definition title="Stable $K$-Trivial Pair"}
Let $X$ be a projective, Gorenstein, connected, reduced variety with $K_X \cong {\mathcal{O}}_X$ (that is, $K_X$ is trivial; for example, a $K3$ or Enriques surface).
Fix a discrete invariant $e > 0$ (e.g., $e = R^2$ for surfaces), and let $0 < \varepsilon \ll 1$ be a (sufficiently small) rational number.
A **stable $K$-trivial pair of type $(e, \varepsilon)$** is a KSBA stable pair $(X, \varepsilon R)$ such that: - $R$ is an effective Cartier divisor on $X$ with $R^2 = e$, - $(X, \varepsilon R)$ is semi-log-canonical, - $K_X + \varepsilon R$ is ample, - $\operatorname{Aut}(X, \varepsilon R)$ is finite (which follows from ampleness and $X$ reduced).
:::

:::{#ktriv-moduli-functor .definition title="Family and Moduli Functor for Stable $K$-Trivial Pairs"}
Let $e > 0$ and $0 < \varepsilon \ll 1$.
A **family of stable $K$-trivial pairs** over a scheme $S$ is a flat, projective morphism $f\colon ({\mathcal{X}}, \varepsilon {\mathcal{R}}) \to S$ such that every geometric fiber $({\mathcal{X}}_s, \varepsilon{\mathcal{R}}_s)$ is a stable $K$-trivial pair of type $(e, \varepsilon)$ as above.
The corresponding moduli functor ${\mathcal{M}}_e^{K-\mathrm{triv}}(\varepsilon)$ assigns to $S$ the set of isomorphism classes of such families over $S$.
:::

The moduli functor for stable $K$-trivial pairs ${\mathcal{M}}_e^{K-\mathrm{triv}}(\varepsilon)$ arises as a subfunctor of the previously discussed KSBA functor for stable pairs.
Specifically, ${\mathcal{M}}_e^{K-\mathrm{triv}}(\varepsilon)$ parametrizes those families where each fiber $(X, \varepsilon R)$ satisfies $K_X \cong {\mathcal{O}}*X$, the $K$-trivial condition, and $R$ is an effective divisor of fixed primitive numerical class $e$ appearing in the boundary with weight $\varepsilon \ll 1$.
This is a closed locus in the moduli stack ${\mathcal{M}}^{\mathrm{KSBA}}*{d, \vec{a}, v}$, where $d = \dim X$, the polarization type $e$ is fixed for the divisor $R$, the boundary coefficients $\vec{a}$ have $a_j = \varepsilon$ at $R$ and zero otherwise, and $K_X$ is trivial as a line bundle or divisor.
The relevance of this construction is that the general results of KSBA theory---separatedness, properness, finite automorphism group property, and the existence of projective coarse moduli spaces---are inherited by this subfunctor.
Thus:

- Every family of stable $K$-trivial pairs admits unique stable limits in one-parameter degenerations, guaranteeing the moduli stack is proper.
- The moduli stack is of finite type, separated, and Deligne--Mumford, with a projective coarse moduli space $M_e^{K-\mathrm{triv}}(\varepsilon)$.
- Extension and uniqueness of isomorphisms in families follow directly from the established machinery for stable pairs.

Thus by construction, the functor ${\mathcal{M}}_e^{K-\mathrm{triv}}(\varepsilon)$ ensures that the moduli problem for stable $K$-trivial pairs is embedded as a closed substack in the general KSBA stack, inheriting all of the necessary geometric properties.
The existence of universal stable limits in families, the finiteness and separatedness of isomorphism classes, and the projectivity of the coarse moduli space are immediate consequences of this embedding.

:::{#ktriv-eps-independence .lemma title="Independence from Small Boundary $\\varepsilon$"}
Given $e>0$, there exists $\varepsilon_0(e) > 0$ such that for all $0 < \varepsilon \leq \varepsilon_0$, the stacks and spaces $$
{\mathcal{M}}\_e^{K-\mathrm{triv}}(\varepsilon) \cong {\mathcal{M}}\_e^{K-\mathrm{triv}}(\varepsilon_0),\qquad
M_e^{K-\mathrm{triv}}(\varepsilon) \cong M_e^{K-\mathrm{triv}}(\varepsilon_0)

$$
are canonically isomorphic; that is, passing to small boundary does not affect the structure of the moduli problem or its compactification.
:::

Thus ${\mathcal{M}}_e^{K-\mathrm{triv}}(\varepsilon)$ is a locus in a general KSBA moduli stack cut out by the condition $K_X \cong {\mathcal{O}}_X$ and a the specification of a single boundary divisor $R$ of degree $e$ with small coefficient $\varepsilon$.

#### Boundaries of KSBA compactifications

:::{#boundary-organization-remark .remark title="Combinatorial Organization of the Boundary"}
For moduli spaces such as $F_S$ of $S$-polarized K3 surfaces, and thus for spaces like $F_{(2,2,0)}$ and $F_{{\mathrm{En}}, 2}$, the boundary of the KSBA compactification is stratified by SLC combinatorial type. Each stratum corresponds to a distinct type of geometric degeneration, classified via monodromy and combinatorial invariants which are encoded in dual complexes, fans, or semifans in related semitoroidal compactifications.
:::

:::{#boundary-stratum .definition title="Boundary Strata and Combinatorial Types"}
A **boundary stratum** in a KSBA compactification $\overline{X}$ of $X$ is a locally closed subset parameterizing stable pairs $(X, R)$ that are not smoot, i.e., those lying in the boundary $\partial\overline{X} \mathrel{\mathop:}= \overline{X} \setminus X$, where $X$ is the locus of smooth KSBA stable pairs. The **slc combinatorial type** of a stable KSBA limit $(\overline{X}, \varepsilon \overline{R})$ is the discrete data given by the simplicial complex $\Gamma(\overline{X})$, along with the deformation type of the quasi-polarized minimal resolution $(V_i, D_i, L_i)$ of each irreducible component $\overline{V}_i$ of $\overline{X}$, where $L_i = {\mathcal{O}}_{V_i}(R_i)$ is the line bundle associated to the pullback $R_i$ of the boundary divisor to the resolution. An **slc stratum** is a boundary stratum of $\overline{X}$ consisting of all stable pairs $(X, R)$ with the same slc combinatorial type.
:::

Given a nonzero vector $\lambda$ in a lattice $T$, its **projective class** is $[\lambda] \mathrel{\mathop:}= \left\{{ a\lambda {~~\mathrel{\Big\vert}~~} a\in {\mathbf{R}}*{>0}}\right\}$, i.e. the ray it generates in $T*{\mathbf{R}}$.
Letting $T$ be the polarization lattice for a polarized moduli problem $F_\Gamma$ of K3 surfaces, we consider degenerations at a cusp $I$ in $\partial\overline{F_\Gamma}^{ \operatorname{BB} }$.
The logarithmic mondromy $N$ at $I$ determines, up to the monodromy group and scaling, elements $\eta\in T$ and $\lambda\in \eta^{\perp T}$ by the explicit formula (see [Friedman--Scattone86, Thm 7.25]), [Engel--Alexeev21, Def. 2.15] $$ N(\gamma) = (\gamma \cdot \eta)\lambda - (\gamma \cdot \lambda)\eta, \qquad \eta^2 = 0,\,\, \lambda^2 =
\begin{cases}
t > 0 & \text{if $I$ is a type ${\textrm{III}}$ $0$-cusp  } \\
t = 0 & \text{if $I$ is a type ${\textrm{II}}$ $1$-cusp }
\end{cases}
,$$ where $t$ is the number of triple points in ${\mathcal{X}}*0$ in the type ${\textrm{III}}$ case.
Arcs in $\overline{F*\Gamma}^{ \operatorname{BB} }$ approaching a 0-cusp $\eta$ are asymptotic to translates of co-characters determined by the class of $\lambda \in  \overline{T}*{ \eta  }  = \eta^{\perp T}/\eta$, and thus $\lambda$ called the "monodromy invariant" of the degeneration.
We finally arrive at the key results that make our combinatorial analysis of $F*{{\mathrm{En}}, 2}$ possible:

:::{#boundary-monodromy-dependence .theorem title="{Dependence of boundary strata on monodromy invariants [@AE23, Cor. 8.13]}
"}
Suppose $R$ is a recognizable divisor for $F_S$. Let $(\overline{X}^*, \varepsilon \overline{R}^*) \to C^*$ be a family of stable pairs over a punctured curve with monodromy invariant $\lambda$. Then the slc combinatorial type of the unique KSBA stable limit $(\overline{X}_0, \varepsilon \overline{R}_0)$ depends only on the projective class $[\lambda]$. Thus there is a well-defined **stratum function** $$
{\mathbb{S}}\colon \{\text{monodromy invariants } \lambda\} \longrightarrow \{\text{slc boundary strata in } \overline{X}\}
,$$ which assigns to each projective monodromy class the corresponding slc boundary stratum.
:::

:::{#normalization-semitoroidal .proposition title="{Normalization and Semitoroidal Strata [@AE23, Thm. 9.1, Cor. 9.2, Thm. 9.3]}
"}
Let $F_S$ denote the moduli space of $S$-polarized K3 surfaces, and suppose $R$ is a recognizable divisor for $F_S$. Then there exists a KSBA compactification $F_S^R$ by stable pairs associated to $R$, a unique semifan $ \mathcal{F} _R$ with a morphism $$
\Psi_R\colon \overline{F_S}^{F_R} \to \overline{F}_S^R
$$ from a semitoroidal compactification realizing it as the normalization of $\overline{F}_S^R$. For each cusp $I\in \overline{F_S}^{ \operatorname{BB} }$, writing $ \overline{T}_{ I  } $ for the corresponding stable boundary lattice and $ \mathfrak{C} _I$ for the corresponding positive cone, let [  \mathfrak{C} *S\^{\operatorname{BB}} \mathrel{\mathop:}= \coprod*{I\in \partial\overline{F_S}^{ \operatorname{BB} } }`\left( {  \mathfrak{C} _I \cap  \overline{T}_{ I  }  } \right)
]
and let`{=tex} $D$ be the polyhedral decomposition of $ \mathfrak{C} _S^{\operatorname{BB}}$ induced by the level sets of ${\mathbb{S}}$, i.e. whose tiles are the loci of all monodromy invariants $\lambda$ on which ${\mathbb{S}}(\lambda)$ is constant. Then the *maximal* cones of $D$ and $ \mathcal{F} _R$ are in bijection, and $\Psi_R$ sends each stratumm in $\partial \overline{F}_S^{ \mathcal{F} _R}$ to the corresponding slc stratum of $\partial \overline{F}_S^R$.
:::

#### Conclusion

The main takeaway of this section is that the boundary of the KSBA compactifications of moduli spaces such as $F_S$ of $S$-polarized K3 surfaces and related spaces like $F_{(2,2,0)}$ and $F_{{\mathrm{En}}, 2}$ admit a precise, combinatorial description:

- The boundary $\overline{F}_S^R$ is stratified according by slc combinatorial type, which encodes both the deformation type of the minimal resolution (with its corresponding divisor) of a stable pair $(X, R)$ and its simplicial dual complex,

- Each stratum corresponds to degenerations sharing the same monodromy data up to scaling, which is captured by the projective classes $[\lambda]$ of monodromy invariants in the stable boundary lattices $ \overline{T}_{ I  } $ . There is thus a well-defined stratum function ${\mathbb{S}}$ assigning to every monodromy class $\lambda$ the associated slc boundary stratum in $\overline{F}_S$.

The stratification of $\overline{F}_S^R$ is thus canonically organized by combinatorial data: dual complexes, semifans, and monodromy invariants.
In geometric terms:

- There exists a semitoroidal compactification $\overline{F}_S^{ \mathcal{F} _R}$ whose normalization maps onto the KSBA compactification $\overline{F}_S^{R}$,

- Polyhedral decompositions and maximal cones of the semifan $ \mathcal{F} _R$ correspond bijectively to the maximal slc strata of the KSBA boundary, and

- The normalization morphism sends each combinatorial stratum of the semitoroidal model to the corresponding slc stratum on the KSBA side.

Thus the boundary of $\overline{F}_S^R$ (and similar KSBA compactifications) is controlled by combinatorial invariants and is indexed purely in terms of discrete monodromy and combinatorial data.

The KSBA approach has a range of pros and cons.
On the one hand, it yields a proper, separated, and projective moduli space and captures all stable degenerations (slc pairs).
It is compatible with the MMP, and the corresponding coarse moduli space structure is always available.
However, the approach is often abstract: explicit descriptions of the boundary and singularities are rare, and few algorithmic tools exist.
The geometry of the boundary strata can be highly complicated, non-smoothable components and pathologies are generic in higher dimensions, and there is virtually no uniform combinatorial structure in those settings.

KSBA compactifications extend to surfaces of general type ($\kappa=2$), but for $\kappa = 0$ surfaces in full generality, i.e. K3, Enriques, abelian, and bielliptic surfaces, as well as for $\kappa=-\infty$ (ruled and rational surfaces), these require significant modification.
Moving to higher dimensions, compactifications for general $K$-trivial varieties like Calabi--Yau threefolds remains a major open problem.
While the KSBA theory guarantees the existence of a good compact moduli space for varieties of log general type, the construction of projective and separated moduli spaces for $K$-trivial threefolds or Calabi--Yau varieties remains largely conjectural.
The core technical obstacles here include the lack smoothability results, the failure of Torelli-type theorems, and much more complex limiting varieties which may be non-reduced or have infinite automorphism groups.
For varieties $X$ of general type with $\dim(X) \geq 3$, many results for surfaces generalize via the MMP -- however, explicit combinatorial classifications of the boundary are almost entirely missing.

Several parts of the KSBA theory have broad applicability.
Universally valid points include the projectivity and properness of the moduli functor for slc varieties of (log) general type, yielding finite automorphism groups for stable pairs and thus a separated proper Deligne-Mumford stack.
However, in higher dimensions, these stacks are generally expected to be non-irreducible and highly singular, and even the deformation spaces of smooth objects can possess arbitrarily bad singularities -- a phenomenon encapsulated in Vakil's "Murphy's law."
Unlike curves, where every stable limit is smoothable, smoothability fails in general: not every slc variety arises as a limit of smooth varieties.
Combinatorial invariants such as dual complexes rapidly become complicated and lose the inductive or graph-like simplicity seen in the curve or surface cases as the dimension increases.
For K3 and Enriques surfaces, the boundary components of $\overline{F}_S$ reflect geometric degenerations that align with period domain descriptions and semitoroidal constructions.

There is also an increasing interest in the relationship between $K$-stability and KSBA stability, particularly in the Fano and $K$-trivial settings.
Heuristically, $K$-stability is a the link between GIT and KSBA stability -- for instance, any (GIT) $K$-semistable polarized variety has slc singularities (Odaka), and any slc variety polarized by an ample canonical divisor is $K$-stable.
Similarly, $K$-trivial, slc polarized pairs are $K$-semistable.
In the Fano and Calabi-Yau cases, $K$-stability is necessary for establishing moduli that carry the expected differential-geometric invariants, namely, Kähler--Einstein metrics.
However, $K$-stability is not an open or constructible condition in general, and so explicit construction of moduli stacks via $K$-stability remains conjectural for many classes.
Recent work by Xu, Li, Wang, and others have constructed projective moduli spaces for Fano varieties using the $K$-stability criterion.

Some key open directions for future research include:

- Extending the success of explicit boundary classifications, as seen in K3 and Enriques surfaces, to Calabi--Yau threefolds and higher-dimensional Fano varieties;

- Exploiting deeper connections with period maps and Hodge theory to construct and better understand compactification in higher dimensions;

- Clarifying the exact relationships between KSBA and $K$-stability, and developing effective, algorithmic, or combinatorial tools for KSBA (or related) compactifications beyond the few well-understood special cases.

<!-- Source: 2-part-moduli/5-chapter-ias-dlt/000-intro.md -->

## Integral Affine Geometry and Comparing Compactifications {#chapter-6}

Sources for this chapter include (Friedman and Scattone 1986; Kulikov 1977; **Persson81?**; **Pinkham81?**; **Scattone87?**; Miranda and Morrison 1983; **Friedman84?**; **Fr83b?**) Let $T$ be an even lattice of signature $(2, n)$, and let $\Gamma \subset \operatorname{O}(T)$ be an arithmetic subgroup.
The period domain $D_{T}$ parametrizes weight-two Hodge structures on $T$, and the modular varieties $F_\Gamma =  { D_{T} }/{ \Gamma } $ serve as coarse moduli spaces for (markedIntegral Affine Geometry and) polarized K3 surfaces.
Given a one-parameter degeneration of K3 or Enriques surfaces, a **Kulikov model** \*arises after a ramified base change, and the possible types for the ${\mathcal{X}}_0$ ${\mathcal{X}}_0$ are:

- **Type I:** ${\mathcal{X}}_0$ is a smooth K3 surface.

- **Type ${\textrm{II}}$:**${\mathcal{X}}_0 = V_0 \cup \ldots \cup V_k$ is a chain of surfaces, where

  - $V_0$ and $V_k$ are rational and $V_1,\cdots, V_{k-1}$ are birational to $E\times {\mathbf{P}}^1$ and thus elliptically ruled,

  - The chain consists of components $V_0,\ldots,V_k$ glued along elliptic curves $E_i = V_{i-1} \cap V_i$ $(1 \leq i \leq k)$, all isomorphic to the same elliptic curve $E$, satisfying a compatibility condition on normal bundles, ${\mathcal{N}}*{E/V_i} \otimes {\mathcal{N}}*{E/V_{i+1}} \cong {\mathcal{O}}_E$

  - The dual complex $\Gamma({\mathcal{X}}_0)$ is a simplicial$\mathbf{D}^1$, corresponding to a partition of the closed unit interval $[0, 1]$.

- **Type ${\textrm{III}}$:** ${\mathcal{X}}*0 = \bigcup*{i=0}^r V_i$ is a union of rational surfaces glued along rational curves such the dual intersection complex $\Gamma({\mathcal{X}}*0)$ is a simplicial $S^2$.
  The union of the double curves on each component $V_i$ forms an anticanonical divisor -- that is, a (possibly reducible) cycle of smooth rational curves in $|-K*{V_i}|$

The dual intersection complex $\Delta$ of a Type ${\textrm{III}}$ model is a triangulation of $S^2$ admitting the structure of a 2-dimensional **integral affine sphere with singularities** ($\mathrm{IAS}^2$) which correspond to a distinguished subset of vertices in $\Delta$, after passing to a suitably complete triangulation.
Away from this singular locus, the charts are locally modeled on open subsets of ${\mathbf{R}}^2$ with transition functions in the orientation-preserving affine linear group $\operatorname{SL}_2({\mathbf{Z}}) \ltimes {\mathbf{R}}^2$.
The possible singularities are modeled on the local structure of the quotient of ${\mathbf{R}}^2$ by the shearing matrices $\begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$ for some integer $n \geq 0$; these are called $I_n$ singularities, where ${\textrm{I}}_1$ are generic and $I_0$ is the trivial (toric) case.
More general singularities arise as products of such shears, corresponding to collisions of the corresponding ${\textrm{I}}_n$ singularities, see (Alexeev and Engel 2022; Symington 2002)

By taking the star to obtain a fan, each vertex $v$ in $\Delta$ yields an **anticanonical pair** $(V, D)$, where $V$ is a rational surface and $D = \sum_{j} D_j \in |-K_V|$ is a cycle of rational curves in the anticanonical linear system.
The dual polytope of this fan encodes a *semitoric* variety: varieties which arise from toric varieties via sequences of blowups and blowdowns.
The data of these blowups is encoded in the following way: the **charge** at a vertex $v$, for the anticanonical pair $(V, D)$, is defined by $Q(V, D) \mathrel{\mathop:}=  {1\over 2}\sum_j D_j^2 + 3$, where $D = \sum_j D_j$ is the (possibly reducible) anticanonical cycle, and $D_j^2$ is the self-intersection of component $D_j$ in $V$.
The charge is precisely designed to measures the defect from being toric: $Q(V, D) = 0$ precisely when $(V, D)$ is toric.
More fundamentally, (Friedman and Scattone 1986, Prop.
2.11) asserts that $\sum_{v \in \Delta} Q(V_v, D_v) = 24$ for any Type ${\textrm{III}}$ Kulikov model of a K3 surface, see (Friedman and Miranda 1983; **Friedman-Scattone?**).

**Symington surgeries** are local modifications of $\mathrm{IAS}^2$ structures that manipulate the placement and type of singularities, and there are two main types: performing a *toric blowup* corresponds to the standard blowup in toric geometry attained by inserting rays into a fan or deleting triangles from its dual polytope.
It increases the number of vertices in $\Delta$, but preserves the total charge.
A *non-toric* (interior) blowup is a surgery that increases the charge at an interior vertex and modifies the integral-affine structure locally by adding the data of a distinguished *monodromy ray*, where the transition functions across the ray are generically described by monodromy matrices as described above.
A toric blowup is thus a blowup at a node of the cycle, corresponding to a torus-invariant point in a toric model, while a nontoric/interior blowup is a blowup at a smooth point of the surface, either on or off the anticanonical cycle.
Such moves are necessary to build arbitrary $\mathrm{IAS}^2$ with prescribed collections of $I_n$ singularities and total charge 24 from a standard simplicial sphere.

Symington's theory explicitly produces $\mathrm{IAS}^2$ by sequences of such surgeries, along with *cuts* and *nodal slides*. Thus, the charge, and the combinatorial data of surgeries, encode all allowable dual complexes for Type ${\textrm{III}}$ degenerations.
Arbitrary $\mathrm{IAS}^2$s with prescribed ($I_{n_1},\ldots,I_{n_k}$) of total charge 24 are built by sequences of toric and nontoric starting from a convex polygon.
This defines the base of a Lagrangian torus fibration, and we refer to the total space as a *semitoric variety* -- a variety that is birationally equivalent to a toric variety, differing by only finitely many nontoric blowups.
Whenever the data $(B(\lambda),\text{charge})$ arise from such construction, there exists a corresponding Kulikov model ${\mathcal{X}}_0$ with $\Gamma({\mathcal{X}}_0) = B(\lambda)$.

(**EF?**) showed that any such $\mathrm{IAS}^2$ satisfying a $d$-semistability condition $\mathcal{Ext}^1_{{\mathcal{O}}_{{\mathcal{X}}*0 }}(\Omega*{{\mathcal{X}}*0}, {\mathcal{O}}*{{\mathcal{X}}*0} ) \cong {\mathcal{O}}*{{\mathcal{X}}_0^{\mathrm{sing} } }$ such that the obstruction theory for deformations is supported only on the singular locus, and thus is locally unobstructred, admits a smoothing ${\mathcal{X}} \to \Delta$ to a (possibly singular) K3 surface.
The $d$-semistability condition is necessary and sufficient for (local) smoothability; for global smoothings to K3 surfaces, the ${\mathcal{X}}_0$ must also satisfy the additional conditions of a Kulikov model.
(**GHK?**) relate this to the existence of Lagrangian torus fibrations on the nearby fibers, mirroring the affine geometry of $B(\lambda)$.

Every Type ${\textrm{III}}$ Kulikov degeneration carries a *projective monodromy invariant* $[\lambda]$ in (projectivized) boundary lattice ${\mathbf{P}}(  \overline{T}_{ \eta  } ) ={\mathbf{P}}( \eta^{\perp}/\eta)$.
This invariant records the monodromy around the ${\mathcal{X}}_0$ and, crucially, determines the gluing data for reconstructing the degeneration from the $\mathrm{IAS}^2$ and its singularities.
The "transvection formula" relates $[\lambda]$, the vanishing cycle.
The local system $H^2$carries a monodromy operator$T$, computed via a primitive isotropic vector $\delta$, the *vanishing cycle*, and the monodromy invariant $\lambda$: $$ T(x) = x + (x, \delta) \lambda - (\lambda, x) \delta, \qquad x\in H^2({\mathcal{X}}_t; {\mathbf{Z}}) $$ where $\lambda^2$ counts the number of triple points.
(**Persson81?**; **Scattone87?**)

Recall that a divisor $R$ is **recognizable** (**AE21?**; Alexeev, Engel, and Han 2022) for $F_\Gamma$ if, for any K3 surface $X = {\mathcal{X}}*0$ and any smooth ${\mathcal{X}}$ to a Kulikov model, the flat limit $R_0$ on ${\mathcal{X}}*0$ is uniquely determined up to automorphism.
Given a recognizable divisor $R$, the KSBA compactification $\overline{F}*\Gamma^R$ can be formed, as well as a the corresponding normalizing semitoroidal compactification $\overline{F*\Gamma}^{ \mathcal{F} _R}$.
By way of the strata functions ${\mathbb{S}}(\lambda)$ from \Cref{chapter-4-cpt} for decorated intersection complexes $B(\lambda)$ constructed from monodromy invariants $\lambda$, boundary strata on both sides correspond to possible $\mathrm{IAS}^2$ spheres with singularities.

Mirror symmetry supplies a *Lagrangian torus fibration* over $B(\lambda)$, and the intersection complex $\Gamma({\mathcal{X}}_0)$ of a Kulikov model coincides with the $\mathrm{IAS}^2$ sphere $B(\lambda)$ constructed from the monodromy data.
The smoothability of the singularities (Engel--Friedman smoothing) then produces a family ${\mathcal{X}} \to \Delta$, whose ${\mathcal{X}}_t$ is smooth, and an explicit contraction algorithm (mirroring the MMP) yields the KSBA stable model.
For K3 surfaces with a nonsymplectic involution, the construction of $\mathrm{IAS}^2$s is mirrored by gluing a polygon $P$ to its opposite $P^{\mathrm{op}}$, forming an $\mathrm{IAS}^2$, $B(\lambda)$, with an induced involution.

Given a degeneration at a 0-cusp $\eta$, the cusp is classified by the boundary lattice $ \overline{T}*{ \eta  } $and the group$\Gamma*\eta$.
The associated Coxeter polytope $P(\Gamma_\eta)$ specifies a Coxeter-Vinberg diagram $G(\Gamma_\eta)$.
To build the intersection complex $\Gamma({\mathcal{X}}_0)$(for a degeneration with monodromy invariant$[\lambda]$),

- Compute $[\lambda] \in  \mathfrak{C} _\eta$,
- Write barycentric coordinates $\ell_i = (\lambda,\alpha_i)$,
- Form the convex (planar) polygon $B_1(\lambda) = \operatorname{Conv} {v_i} \subset {\mathbf{R}}^2$ where $v_i$ are specified by the Coxeter diagram and$\ell_i$ govern their lengths,
- Obtain the full integral affine sphere by gluing $B_1(\lambda)$ to its opposite:$B(\lambda) = B_1(\lambda) \cup -B_1(\lambda)$, yielding a rigid $\mathrm{IAS}^2$.

We summarize this process in the following algorithm to construct all Type ${\textrm{III}}$ degenerations for $F_\Gamma$, which we in turn specialize to $F_{(2,2,0)}$ and $F_{{\mathrm{En}}, 2}$ to construct all dlt models for their KSBA compactifications:

1. **Build the Coxeter polygon $P(\Gamma_\eta)$** from the Coxeter--Vinberg diagram (using the configuration of simple roots $\alpha_i$).
2. **Compute barycentric coordinates** $\ell_i = (\lambda, \alpha_i)$ from the monodromy invariant$[\lambda]$.
3. **Construct the monodromy polytope** $B_1(\lambda)$in${\mathbf{R}}^2$using vertices$v_i$and these lengths.
4. **Form the$\mathrm{IAS}^2$sphere** $B(\lambda) = B_1(\lambda) \cup -B_1(\lambda)$, with $I_n$singularities at prescribed locations, total charge 24.
5. **Produce the corresponding Kulikov model**${\mathcal{X}}_0$(intersection complex matching$B(\lambda)$), and smooth to a family ${\mathcal{X}}\to\Delta$.
6. Contract to the KSBA stable model.

For Enriques surfaces, as shown in \todo{CITE}, the above theory must be quotiented by a fixed-point-free involution on $\mathrm{IAS}^2$, reflecting the covering $K3$ surface structure.
This mandates working with "half-divisor" models (\Cref{half-divisor-model}) and searching for $\mathrm{IAS}^2$ spheres invariant under a group generated by two commuting involutions, one corresponding to $\iota_{\operatorname{dP}}$, corresponding to K3 surfaces $X$ in $F_{(2,2,0)}$, and another fixed-point-free involution corresponding to $\iota_{{\mathrm{En}}}$, coming from the embedded locus $F_{{\mathrm{En}}, 2}$, those $X$ arising as K3 covers $X\to Z$ of Enriques surfaces.
We impose the condition that the periods and dual complex of $(X_0, R_0)$ are involution invariant -- then the Torelli theorem for anticanonical pairs shows that $(V_i, D_i, R_i)$ admits an involution $\iota_{{\mathrm{En}}, i}$ and the quotient $(V_i, D_i, R_i)/\iota_{{\mathrm{En}},i}$ is a log Calabi--Yau pair.
We note that $\iota_{{\mathrm{En}}}$ is only a birational involution in general, and so we obtain half-divisor models for generic degenerations with a given monodromy invariant $\lambda$.

<!--  [@Ale02], [@MZ08], [@AMRT75] -->
<!-- Source: 2-part-moduli/5-chapter-ias-dlt/200-Kulikov.md -->

### Kulikov Models

#### Degenerations

Let $\pi\colon {\mathcal{X}} \to C$ be a flat, proper morphism, with $C$ a germ of a smooth complex curve (typically taken as a disk $\Delta = \{ t \in {\mathbf{C}} \colon |t| < \epsilon\}$). The **${\mathcal{X}}_0$** ${\mathcal{X}}_0 = \pi^{-1}(0)$ encodes the limiting geometry of the family as $t \to 0$.
For $t \neq 0$, the fibers ${\mathcal{X}}_t$ are assumed smooth, often K3 or Enriques surfaces.
The **punctured disk** $\Delta^* = \Delta \setminus \{0\}$ and the corresponding smooth locus ${\mathcal{X}}^* = \pi^{-1}(\Delta^*)$ are natural analytic settings for studying the variation of complex and Hodge-theoretic structures across the family.
Over $\Delta^*$, the fibers ${\mathcal{X}}*t$ are smooth and give rise to a variation of Hodge structure on the local system $R^2 \pi** {\mathbf{Z}}$.
The behavior of ${\mathcal{X}}_0$ reflects the limiting geometry and possible singularities, providing key topological and moduli-theoretic invariants that determine both the topological degeneration type and the locus in the compactified moduli space.

###### Dual Complexes

If ${\mathcal{X}}_0$ is a simple normal crossings (snc) divisor, its **dual complex** $\Gamma({\mathcal{X}}_0)$ is the finite simplicial complex constructed as follows:

- vertices correspond to irreducible components of ${\mathcal{X}}_0$;
- $k$-simplices correspond to connected components of nonempty intersections of $k+1$ distinct components.

This combinatorial invariant is stable under blowups and birational modifications that preserve the snc structure.
For degenerations with semi log canonical (slc) singularities, $\Gamma({\mathcal{X}}_0)$ is defined up to homeomorphism and remains a meaningful measure of combinatorial complexity of the ${\mathcal{X}}_0$.

For degenerations of Enriques surfaces constructed as quotients by a biregular, fiberwise involution (the **Enriques involution**), the dual complex comes in one of two types:

- a topological closed disk $\mathbf{D}^2$ (when the quotient preserves orientation), or
- a real projective plane ${\mathbf{RP}}^2$ (when antipodal identification occurs).

This distinction can be read off from the intersection pairing on the lattice $ \overline{T}_{ I  } $ attached to the relevant cusp $I$ and the structure of ${\mathcal{X}}_0$.

###### Kulikov Models

A **Kulikov model** is a degeneration ${\mathcal{X}} \to C$ in which:

1. The total space ${\mathcal{X}}$ is regular (smooth as a threefold);
2. The ${\mathcal{X}}_0$ ${\mathcal{X}}_0$ is a reduced snc divisor;
3. The relative dualizing sheaf is trivial: $\omega_{{\mathcal{X}}/C} \cong {\mathcal{O}}_{{\mathcal{X}}}$.

This Calabi--Yau condition ensures that ${\mathcal{X}}$ is a Calabi--Yau threefold over $C$ and provides precise control over the limiting variation of Hodge structure, situating the degeneration as minimally complicated with respect to semistable reduction (Kulikov 1977; Persson and Pinkham 1981). The condition ensures that the limits of periods and Hodge structures are controlled, and the ${\mathcal{X}}_0$ is as geometrically simple as feasible under semistable reduction.

###### Monodromy and Classification

The variation of Hodge structure on the local system $R^2 \pi_* {\mathbf{Z}}$ equips the family with a locally constant sheaf whose fibers are $H^2({\mathcal{X}}_t; {\mathbf{Z}})$ for $t \neq 0$.
The monodromy transformation about $t = 0$ is given by the Picard-Lefschetz operator $T \colon H^2({\mathcal{X}}_t; {\mathbf{Z}}) \to H^2({\mathcal{X}}_t; {\mathbf{Z}}).$

After a finite cover of $\Delta$, one reduces to the case where $T$ is unipotent and defines the nilpotent logarithm $N = \log T = (T - I) - {1\over 2}(T - I)^2 + \frac{1}{3}(T - I)^3 - \cdots,$ which is nilpotent of order at most three.
The index of nilpotency of $N$ determines both the geometry of the ${\mathcal{X}}_0$ ${\mathcal{X}}_0$ and the combinatorial type of the degeneration.

**Type I.** If $N = 0$, then ${\mathcal{X}}_0$ is a smooth K3 surface.
The degeneration is locally analytically trivial, and the dual complex is a single point.

**Type ${\textrm{II}}$.** If $N \neq 0$ and $N^2 = 0$, then ${\mathcal{X}}_0 = V_1 \cup \cdots \cup V_n$, with:

- $V_1, V_n$ are rational surfaces;
- Each intermediate $V_i$ ($2 \leq i \leq n-1$) is birational to $E \times {\mathbf{P}}^1$ for a fixed elliptic curve $E$;
- The double locus $D_{i,i+1} = V_i \cap V_{i+1}$ is isomorphic to $E$;
- The self-intersection numbers satisfy $D_{i,i+1}|*{V_i}^2 + D*{i,i+1}|*{V*{i+1}}^2 = 0.$ The dual complex is a closed interval $\text{IAD}^1$.

**Type ${\textrm{III}}$.** If $N^3 = 0$ with $N^2 \neq 0$, then ${\mathcal{X}}_0$ is a union of smooth rational surfaces, with irreducible components meeting along rational curves, such that:

- On each $V_i$ the sum of the double curves forms an anticanonical cycle:
- $\sum_{j \neq i} D_{ij} \sim -K_{V_i};$
- The intersection numbers satisfy
$$

    d_{ij} + d_{ji} = -2, \qquad d_{ij} = -2p_a(D_{ij}) - (D_{ij})^2,
    $$ where $p_a(D_{ij})$ is the arithmetic genus of $D_{ij}$.

The dual complex of ${\mathcal{X}}_0$ is a triangulation of the 2-sphere $\mathrm{IAS}^2$ (Friedman and Scattone 1986; Friedman 1983a).

\todo{Redundant}

###### Lattice-Theoretic Interpretation

These types are naturally stratified by the rank of isotropic subspaces in the boundary lattice $ \overline{T}_{ I } $ and correspond to geometric locations in the closure of the fundamental chamber $ \mathfrak{C} \_I$ in $ \overline{T}_{ I, {\mathbf{R}} } $.
The degeneration is situated in the rational closure of the positive cone:

- Type ${\textrm{I}}$corresponds to interior points of $ \mathfrak{C} \_I$;
- Type ${\textrm{II}}$ corresponds to rational boundary rays;
- Type ${\textrm{III}}$ corresponds to two-dimensional face strata.

The position in the positive cone encodes both the monodromy and the moduli-theoretic stratum to which the degeneration belongs.
This lattice-theoretic perspective connects the local analytic classification with the global structure of the compactified moduli space.

\begin{longtable}{|l|p{4.5cm}|p{3cm}|c|p{4cm}|p{3.5cm}|}
\hline
Type & ${\mathcal{X}}_0$ & $\Gamma({\mathcal{X}}_0)$ & $\operatorname{rank}(I)$ & Diagram(s) & Locus in $ \mathfrak{C} _I$ \\
\hline
\endfirsthead
\hline
Type & Structure of ${\mathcal{X}}_0$ & Dual Complex $\Gamma({\mathcal{X}}_0)$ & Rank of Isotropic Subspace $I$ & Diagram Type Governing Degeneration(s) & Locus in $ \mathfrak{C} \_I$ \\
\hline
\endhead
\hline
\endfoot
\hline
\endlastfoot
${\textrm{I}}$ & Smooth K3 & ${\operatorname{pt}}$ & $0$ & Full Coxeter diagram is elliptic (finite ADE) & Interior \\
\hline
${\textrm{II}}$ & $V_1{\amalg}\_E W_2 {\amalg}\_E \cdots {\amalg}\_E W_{n-1} {\amalg}_E V_n$ & $\text{IAD}^1$ & $1$ & Parabolic/$\widetilde{ \mathrm{ADE} } $ $^\ast$ & Ray $\eta$ \\
\hline
${\textrm{III}}$ & $V_1 {\amalg}\_R V_2 {\amalg}\_R \cdots {\amalg}\_R V_{n-1} {\amalg}\_R V_1$ & $\mathrm{IAS}^2$ & $2$ & Elliptic/$\mathrm{ADE}$ & Plane $I$ \\
\hline
\end{longtable}

where $V_1, V_n$ are ....
and $W_i$ are ..., with $E$ an elliptic double curve.
here $V_i$ in Type ${\textrm{III}}$ are rational and glued in an anticanonical cycle.

\todo{Double check}

The **Elliptic/Parabolic Subdiagram(s)** column records the nature of the Coxeter/Dynkin subdiagram associated with the corresponding degeneration.
For Type I, the entire graph is negative definite (elliptic).
For Type ${\textrm{II}}$, maximal rank 1 isotropic sublattices (parabolic) arise as the relevant subdiagram.
Type ${\textrm{III}}$ corresponds to the appearance of maximal rank 2 elliptic subdiagrams associated with the boundary face.

#### Picard-Lefschetz Theory

###### Picard--Lefschetz Transformations

::: {#def:picard-lefschetz-transformation .definition title="Picard–Lefschetz Transformation"}
Let $p\colon {\mathcal{X}} \to \Delta$ be a Kulikov model (or a semistable degeneration) with ${\mathcal{X}}_0$ ${\mathcal{X}}_0$.
The sheaf ${\mathbf{R}}^2 p_*\underline{{\mathbf{Z}}}_{\Delta}$ restricts to a locally constant system over the punctured disk $\Delta^*$, whose fiber over $t \in \Delta^*$ is $H^2({\mathcal{X}}_t; {\mathbf{Z}})$.After trivializing the pullback of this local system to the universal cover $\widetilde{\Delta^*}$, the fundamental group $\pi_1(\Delta^*, t)$ acts via monodromy $\pi_1(\Delta^*, t) \longrightarrow \operatorname{Aut}(H^2({\mathcal{X}}_t; {\mathbf{Z}})).$ The image of a simple closed loop $\gamma$ generating $\pi_1(\Delta^*, t)$ is the **Picard--Lefschetz transformation**:
$$
T_\gamma \colon H^2({\mathcal{X}}_t; {\mathbf{Z}}) \to H^2({\mathcal{X}}_t; {\mathbf{Z}}) ,$$ represented by the **monodromy matrix** $T \in \operatorname{GL}_n({\mathbf{Z}})$ where $n = \operatorname{Pic}\ H^2({\mathcal{X}}_t; {\mathbf{Z}})$ (Kulikov 1977), (Friedman and Scattone 1986).
:::

###### Quasi-Unipotency and Logarithmic Monodromy

::: {#thm:quasi-unipotent-monodromy .theorem title="Quasi-Unipotency and Log Monodromy"}
If ${\mathcal{X}}_0$ is a simple normal crossings (semistable) degeneration, the monodromy $T$ is **quasi-unipotent**: that is, there exist positive integers $k, n$ such that $(T^k - \mathrm{id})^n = 0$.
For semistable degenerations, one can take $k = 1$.
The logarithm of the unipotent part of $T$ defines the **log monodromy operator**: $$
N = \log(T) = (T-\mathrm{id}) - {1\over 2}(T-\mathrm{id})^2 + \frac{1}{3}(T-\mathrm{id})^3 - \cdots + \frac{(-1)^{n+1}}{n}(T-\mathrm{id})^n
,$$ where $n$ is the index of nilpotency (Kulikov 1977), (Persson and Pinkham 1981).
:::

\todo{Repeated somewhere else.}

:::{#def:monodromy-singularities .definition title="Monodromy Around Singularities"}
Let $B$ be an integral affine manifold with singularities.
The **monodromy** of $B$ around a singularity $p$ is the element of $\operatorname{Aff}({\mathbf{Z}}^n)$ defined by parallel transport around a loop encircling $p$.

For an $I_1$ singularity in dimension $2$, the monodromy matrix is $T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$ This affine monodromy encodes the classical Picard--Lefschetz transformation for such degenerations (Kontsevich and Soibelman 2006), (Symington 2002).
:::

:::{#rem:monodromy-invariant-parameter .remark title="Monodromy Invariant as Structural Parameter"}
For a Type ${\textrm{III}}$ Kulikov degeneration with ${\mathcal{X}}_0$ ${\mathcal{X}}_0$, the **monodromy invariant** $\lambda \in \overline{T}_\eta = \eta^\perp / \eta$ determines:

1.  The number of triple points of ${\mathcal{X}}_0$, with $\lambda^2 = \#\{\text{triple points}\}$;

2.  The _barycentric coordinates_ $\lambda = (\ell_i)$,which determine $B(\lambda)$, an explicit $\mathrm{IAS}^2$.

See (**AEGS23?**), (**GHK15a?**), (**Eng18?**).
:::

###### Weight Filtrations

:::{#def:weight-filtration-cohomology .definition title="Weight Filtration on Cohomology"}
Let $N = \log(T)$ be the logarithm of the unipotent monodromy operator.
The **weight filtration** $ {W }^{\bullet} $ on $H^2({\mathcal{X}}_t; {\mathbf{C}})$ is defined by: $$
W_k H^2 = \{ v \in H^2 {~\mathrel{\Big\vert}~} N^{j} v = 0 \text{ for } j > k \}
,$$ yielding a canonical increasing filtration $$
0 = W_{-1} \subset W_0 \subset W_1 \subset W_2 \subset W_3 \subset W_4 = H^2({\mathcal{X}}_t; {\mathbf{C}})
.$$ The **graded pieces** are $\operatorname{Gr}_k^W H^2 \mathrel{\mathop:}=  W_k / W_{k-1}$, and carry the limiting mixed Hodge structure (Pierre Deligne 1971), (**SZ85?**).
:::

\todo{Repeated}

:::{#thm:weight-filtration-kulikov-types .theorem title="Weight Filtration and Kulikov Type"}
Let $N$ be the logarithm of the monodromy in a degeneration of K3 (or analogous) surfaces.
Then:

- **Type I** (trivial monodromy, $N = 0$): $W_2 = H^2$, and all higher pieces vanish.
- **Type ${\textrm{II}}$** ($N^2 = 0,\ N \neq 0$): $W_0 = \ker(N)$; $W_2 = H^2$; $W_4 = 0$.
- **Type ${\textrm{III}}$** ($N^3 = 0,\ N^2 \neq 0$): all steps in the filtration are nontrivial.

The geometric interpretations are as follows:

- $\operatorname{Gr}_0^W$ encodes contributions from singular or reducible components;
- $\operatorname{Gr}_2^W$ corresponds to the part of the cohomology preserved in the degeneration;
- $\operatorname{Gr}_4^W$ arises from new cycles present in Type ${\textrm{III}}$ degenerations.

This filtration packages the mixed Hodge structure obtained from the Clemens--Schmid exact sequence and classifies degenerations according to their limit behavior (Kulikov 1977), (**CKS86?**).
:::

Degenerations with unipotent monodromy give rise to monodromy invariants:

:::{.definition title="Monodromy Invariant and Barycentric Coordinates"}
Let $\lambda \in \overline{T}_\eta \mathrel{\mathop:}= \eta^\perp / \eta$ denote the monodromy invariant associated to a degenerating family of K3 surfaces.
Let $\{ \alpha_i \} \subset L$ be a set of simple roots defining a rational polyhedral chamber $ \mathfrak{C} \subset L\_{{\mathbf{R}}}$, with wall hyperplanes $\alpha_i^\perp$.
We define the **barycentric coordinates** of $\lambda$ by: $$
\ell_i \mathrel{\mathop:}=  \lambda \cdot \alpha_i
.$$ The vector $\ell = (\ell_i)$ determines the affine geometry of the dual complex and the positions of singularities under the integral-affine structure.
:::

Let $\pi \colon {\mathcal{X}} \to C$ be a flat projective family of K3 surfaces over a smooth curve $C$, endowed with a biregular involution $\iota_{{\mathrm{En}}}$ acting on ${\mathcal{X}}$ such that for every $t \ne 0$, the restriction $\iota_{{\mathrm{En}}} |_{{\mathcal{X}}_t}$ is a fixed-point-free involution.
Thus, for $t \ne 0$, the fibers ${\mathcal{X}}*t$ are K3 surfaces and the quotients ${\mathcal{X}}*t/\iota*{{\mathrm{En}}}$ are nonsingular Enriques surfaces.
The specialization of $\iota*{{\mathrm{En}}}$ to the ${\mathcal{X}}*0$, denoted $\iota*{{\mathrm{En}}, 0}$, may acquire fixed points even if it acts freely on the ${\mathcal{X}}_t$.
This can result in additional singularities in the ${\mathcal{X}}_0$, and consequently, in the quotient $$ {\mathcal{Z}}_0 \mathrel{\mathop:}=  {\mathcal{X}}*0/\iota*{{\mathrm{En}}, 0}. $$ Here, ${\mathcal{X}}_0$ denotes the ${\mathcal{X}}_0$ of the degeneration, and ${\mathcal{Z}}_0$ is its quotient by the specialized involution.
The dual complex $\Gamma({\mathcal{Z}}_0)$ of the ${\mathcal{X}}_0$ ${\mathcal{Z}}*0$ is topologically determined by the action of $\iota*{{\mathrm{En}}, 0}$ on the dual complex $\Gamma({\mathcal{X}}_0)$ of the original Kulikov fiber.
Specifically, if $\Gamma({\mathcal{X}}*0)$ is a triangulated $2$-sphere, then if $\iota*{{\mathrm{En}}, 0}$ is free on $\Gamma({\mathcal{X}}_0)$, the quotient dual complex $\Gamma({\mathcal{Z}}*0)$ is homeomorphic to the real projective plane ${\mathbf{RP}}^2$, as occurs when the involution acts antipodally on the sphere.
If $\iota*{{\mathrm{En}}, 0}$ has fixed points on $\Gamma({\mathcal{X}}_0)$ or preserves a region, then the quotient dual complex $\Gamma({\mathcal{Z}}_0)$ is a disk $\mathbf{D}^2$, corresponding to a boundary stratum where the involution admits fixed locus or acts with boundary preserves.

<!-- Source: 2-part-moduli/5-chapter-ias-dlt/400-acp-charge.md -->

### Anticanonical Pairs and Kulikov Models

#### Charge

The components of certain singular fibers in degenerations are naturally described as log Calabi--Yau surfaces, also known as anticanonical pairs.

:::{#def:anticanonical-pairs .definition title="Anticanonical Pairs"}
Let $V$ be a smooth projective rational surface, and let $D = \sum_j D_j$ be a reduced divisor on $V$ with simple normal crossings.
The pair $(V, D)$ is called an **anticanonical pair** if the log canonical divisor is ${\mathbf{Q}}$-linearly trivial: [ K_V + D \sim\_{{\mathbf{Q}}} 0. ] Such pairs are also called **log Calabi-Yau surfaces**.
If $V$ is a toric surface and $D = \partial V$ is its toric boundary divisor, $(V, D)$ is called a **toric anticanonical pair**.
Common examples include pairs where $D$ is a smooth elliptic curve, a cycle of $n \ge 2$ smooth rational curves, or an irreducible rational nodal curve.
For a classification of exceptional cases, see (**GHK15?**).
The following is a numerical invariant that measures the deviation of an anticanonical pair from being toric.
:::

:::{#def:charge-anticanonical-pair .definition title="Charge of an Anticanonical Pair"}
Let $(V, D = \sum_j D_j)$ be an anticanonical pair.
The **charge** of the pair is defined as [ Q(V, D) \mathrel{\mathop:}= 12 - \sum\_j (D_j\^2 + 3). ] This quantity is a non-negative integer for all anticanonical pairs and is zero if and only if the pair $(V, D)$ is toric.
:::

The definition of charge can be restated using the adjunction formula, depending on the geometry of the boundary divisor $D$.

:::{#def:charge-alt-formulas .definition title="Alternative Formulas for Charge"}
Let $(V, D)$ be an anticanonical pair.

- If $D = \sum_j D_j$ is a nodal cycle of $n \ge 2$ rational components, the charge is $Q(V, D) = 12 + \sum_j (-D_j^2 - 3)$.
- If $D$ is an irreducible nodal curve, the charge is $Q(V, D) = 11 - D^2$.
:::

#### Toric Models and Blowups

Rational anticanonical pairs can be constructed from toric pairs via a sequence of two fundamental types of birational modifications.

:::{#def:corner-interior-blowups .definition title="Corner and Interior Blowups"}
Let $(V, D)$ be an anticanonical pair.

- A **corner blowup** is the blowup of $V$ at a node of $D$.
  If $\pi: V' \to V$ is such a blowup and $D'$ is the reduced total transform of $D$, then $(V', D')$ is an anticanonical pair with its charge preserved: $Q(V', D') = Q(V, D)$.

- An **interior blowup** is the blowup of $V$ at a smooth point of a component of $D$.
  If $D''$ is the union of the proper transform of $D$ and the exceptional divisor, then $(V'', D'')$ is an anticanonical pair whose charge increases by one: $Q(V'', D'') = Q(V, D) + 1$.

Any rational anticanonical pair can be obtained from a toric pair (which has charge 0) by a sequence of corner blowups followed by a sequence of interior blowups (**GHK15?**).
:::

In the context of K3 surface degenerations, these local invariants are subject to a global conservation law discovered by Friedman and Morrison.

:::{#thm:friedman-morrison-charge .theorem title="Friedman–Morrison Charge Theorem for Type $\{\textrm{III}
}$ Degenerations"}
Let ${\mathcal{X}} \to \Delta$ be a Type ${\textrm{III}}$ Kulikov degeneration of K3 surfaces, with ${\mathcal{X}}_0$ ${\mathcal{X}}_0 = \bigcup_{i=1}^n V_i$.
For each component $V_i$, let $D_i = V_i \cap \overline{({\mathcal{X}}_0 \setminus V_i)}$ be its boundary divisor, so that $(V_i, D_i)$ is an anticanonical pair.
Then the sum of the charges of these pairs is constant: [ \sum\_{i=1}\^n Q(V_i, D_i) = 24. ] This imposes the constraint that at most 24 of the components $V_i$ can be non-toric, as toric pairs contribute zero to the sum.
This result provides a rigidity condition on the combinatorics of K3 degenerations (Friedman and Miranda 1983, Thm.\~2.2), (Friedman 2015).
:::

:::
remark
The conservation property constrains the possible combinatorial types of ${\mathcal{X}}_0$s and ensures that the total complexity of a degeneration, as measured by the charge, remains constant across the moduli space.
This invariance establishes the relationship between the KSBA and Baily-Borel compactifications of the moduli space.
:::

<!-- Source: 2-part-moduli/5-chapter-ias-dlt/500-ias.md -->

### Integral Affine Structures

:::{.definition title="Integral-Affine Structure"}
Let \$ B \$ be a topological manifold.\
An **integral-affine structure** on \$ B \$ is specified by an atlas of charts [ { \phi\_i\colon U_i \to {\mathbf{R}}\^n } ] such that for each nonempty overlap \$ U_i \cap U_j \$, the transition maps [ \phi\_j \circ \phi\_i\^{-1} {~\mathrel{\Big\vert}~} \phi\_i(U_i \cap U_j) \to \phi\_j(U_i \cap U_j) ] are elements of the group [ \operatorname{Aff}({\mathbf{Z}}\^n) \mathrel{\mathop:}= \operatorname{GL}\_n({\mathbf{Z}}) \ltimes {\mathbf{R}}\^n. ] That is, each transition function is of the form \$ x \mapsto Ax + b \$, where \$ A \in \operatorname{GL}\_n({\mathbf{Z}}) \$ and \$ b \in {\mathbf{R}}\^n \$, i.e., it is an affine transformation preserving the standard lattice \$ {\mathbf{Z}}\^n \subset {\mathbf{R}}\^n \$.
This defines a local system \$ \Lambda_B \subset {\mathcal{T}}\_B \$ of integral sections of the tangent sheaf on \$ B \$: a subsheaf locally trivialized by those coordinate vector fields which whose transition maps act by the linear part \$ A \$.
The global monodromy of $\Lambda_B$ records the obstruction to a global trivialization.

The integral-affine structure is said to be **singular** if there exists a discrete (or more generally, closed of codimension at least two) subset in \$ B \$ such that the charts cannot be completed, or equivalently, the monodromy of \$ \Lambda_B \$ is nontrivial around loops enclosing these points.
These singularities model local monodromy defects of the affine structure and their presence is intimately related to topological data, encoding, for example, the global Euler characteristic or "total curvature" of the integral-affine manifold.
In the context of degenerations, such singularities mirror the loci in the total space responsible for nontrivial monodromy or the failure of smooth toric models.
:::

:::{.proposition title="Integral-Affine Structures on Kulikov Models"}
Let \$ \pi \colon {\mathcal{X}} \to \Delta \$ be a one-parameter degeneration of K3 surfaces over a disc, with reduced normal crossings ${\mathcal{X}}_0$ [ {\mathcal{X}}*0 = \bigcup*{i \in I} V_i ] and denote by \$ \Gamma({\mathcal{X}}\_0) \$ the dual complex of \$ {\mathcal{X}}\_0 \$.

If \$ {\mathcal{X}} \$ is a Type ${\textrm{III}}$ Kulikov degeneration of K3 surfaces, then \$ \Gamma({\mathcal{X}}\_0) \$ is canonically a triangulated 2-sphere.
There exists a canonical singular integral-affine structure on \$ \Gamma({\mathcal{X}}\_0) \$, defined as follows:

Each irreducible component is an anticanonical pair, which we recall admits a pseudofan.
The pseudo-fans are glued along their boundaries via primitive integral-affine identifications determined by the cyclic order and intersection numbers of the components of \$ D_i \$ as they appear in \$ {\mathcal{X}}\_0 \$.
This construction defines an integral-affine structure on \$ \Gamma({\mathcal{X}}\_0) \$.

The points of \$ \Gamma({\mathcal{X}}\_0) \$ corresponding to non-toric anticanonical pairs, i.e. those of positive charge, become singularities for the integral-affine structure.
The monodromy about these points records the nontriviality of the local structure.
As shown in (Friedman and Miranda 1983), the total number of such singularities equals: $\sum_{i \in I} Q(V_i, D_i) = 24,$ where $Q(V_i, D_i)$ denotes the charge of the pair $(V_i, D_i)$.
:::

:::{.definition title="The Symington polytope $B(\\lambda)$"}
Given a vector $\ell$, define $P(\lambda)$ to be the **Symington polytope**, an integral-affine polygon uniquely determined by the entries of $\ell$, constructed as specified in (Symington 2002).
The edge lengths and directions of $P(\lambda)$ are determined by the barycentric coordinates $\ell_i$ with respect to the roots $\alpha_i$.
Define the corresponding $\mathrm{IAS}^2$ $B(\lambda)$ by $B(\lambda) \mathrel{\mathop:}=  P(\lambda) \cup P(\lambda)^{\mathrm{op}},$ where $P(\lambda)^{\mathrm{op}}$ is a copy of $P(\lambda)$ with reversed orientation.
The polytopes $P(\lambda)$ and $P(\lambda)^{\mathrm{op}}$ are glued along their boundaries, which jointly form the equator of $B(\lambda)$.
:::

:::{.definition title="Integral affine polarizations"}
Let $R_{\mathrm{IA}}$ denote the **integral-affine polarization** on $B(\lambda)$, which is a distinguished equator in the integral-affine sphere $B(\lambda)$.
This equator corresponds to the flat limit divisor ${\mathcal{R}}_0$ in the degeneration.
For the cusp $(18,2,0)_1$, $R_{\mathrm{IA}}$ consists of edges along the equator with weights alternating between $2$ and $1$.\
For the cusp $(18,0,0)_1$, $R_{\mathrm{IA}}$ has no support on the bottom edge of $P(\lambda)$, and the associated components of ${\mathcal{R}}_0$ in ${\mathcal{X}}_0$ are empty.
:::

:::
remark
The construction of $P(\lambda)$ and $B(\lambda)$ may require certain coordinates of $\ell$ to be even, depending on the configuration of the singularities and the structure of the underlying lattice.
These divisibility conditions ensure, for example, that an $I_2$-type singularity may be split into two $I_1$-type singularities in the integral-affine structure.
Coordinates such as $\ell_{20}$ and $\ell_{21}$ for cusps \todo{???} correspond to twice the lattice distance between pairs of integral-affine singularities that are introduced via surgery or gluing operations in the polytope.
These entries record the geometric distances between ingularities or their collisions in integral affine structure.
:::

Type ${\textrm{III}}$ degenerations of Enriques surfaces inherit involutions from their K3 covers, which in turn act on the dual complexes of Kulikov models and hence on the $IAS^2$s $B(\lambda)$, giving rise to an $\mathrm{IAS}^2$ with commuting involutions $\iota_{{\mathrm{En}}}, \iota_{\operatorname{dP}}$.
In the standard Euclidean embedding of $S^2$ into ${\mathbf{R}}^3$, these involutions act either by $(x,y,z)\mapsto (-x,-y,-z)$, the antipodal map with quotient ${\mathbf{RP}}^2$, or by $(x,y,z)\mapsto (x,y,-z)$, the "flip" whose quotient is a disc $\mathbf{D}^2$.
These cases are distinguished by the fixed loci, and the quotients if the $\mathrm{IAS}^2$s $B(\lambda)$ correspond precisely to the dual complexes of Enriques stable degenerations, and thus determine the strata of the $\overline{F_{{\mathrm{En}}, 2}}$.
We refer to these as $\text{IAD}^2$ and $\text{IARP}^2$ respectively.

<!-- Source: 2-part-moduli/5-chapter-ias-dlt/600-dlt-models.md -->

### dlt Models

Let $T$ be an even lattice of signature $(2, n)$, and let $\eta \in T$ be a primitive isotropic vector.
The boundary lattice associated to $\eta$ is $$ \overline{T}*{ \eta  }  \mathrel{\mathop:}=  \eta^{\perp_T} / \left\langle \eta \right\rangle $$ which has signature $(1, n-1)$ and admits a root system $\Phi( \overline{T}*{ \eta  } )$.
For an arithmetic subgroup $\Gamma \leq \operatorname{O}(T)$, the stable boundary group at $\eta$ is $$ \Gamma_\eta \mathrel{\mathop:}=  \operatorname{Stab}*\Gamma(\eta)/U*\eta $$ where $U_\eta$ is the maximal unipotent normal subgroup of $\operatorname{Stab}*\Gamma(\eta)$ that acts trivially on $ \overline{T}*{ \eta } $.
The group $W(\Gamma_\eta) \leq \operatorname{O}( \overline{T}*{ \eta } )$ generated by reflections in roots stabilized by $\Gamma*\eta$ defines the stable reflection group, and the associated Coxeter chamber $ \mathfrak{C} (\Gamma*\eta) \subset \overline{T}*{ \eta, {\mathbf{R}} } $ is determined by the set of simple roots for $W(\Gamma_\eta)$ (**AEGS23?**).

Let $ \mathfrak{C} *\eta \mathrel{\mathop:}= \{ v \in \overline{T}*{ \eta, {\mathbf{R}} } {~~\mathrel{\Big\vert}~~} v^2 > 0 \}$.
Any rational polyhedral fan $\Sigma(\eta)$ supported on the rational closure $ \mathfrak{C} *{\eta, {\mathbf{Q}}}$ that is $\Gamma*\eta$-invariant determines the structure of the toroidal compactification of $F_\Gamma =  { D_{T} }/{ \Gamma } $, with the Coxeter fan subdividing $ \mathfrak{C} *{\eta, {\mathbf{Q}}}$ into chambers indexed by $W(\Gamma*\eta)$ (**AEGS23?**).

#### Boundary Models: Stable Involution Pairs and Quotients

:::{.definition title="(K+D)-Trivial Polarized Involution Pairs"}
A $(K+D)$-trivial polarized involution pair is a triple $(X, D, \iota)$, where $X$ is a normal surface, $D \subset X$ a reduced effective divisor, and $\iota: X \to X$ is an involution satisfying $\iota(D) = D$.
The canonical class and divisor are related by $K_X + D \sim 0$, and the fixed locus of $\iota$ consists of an ample Cartier divisor $R$, possibly with isolated fixed points.
For all $0 < \varepsilon \ll 1$, the pair $(X, D + \varepsilon R)$ is log canonical.
Each irreducible component occurring in stable degenerations of K3 surfaces with nonsymplectic involution is locally modeled by such a triple [Alexeev--Engel--Thompson 2023, Thm. 1.3].
:::

Given such a pair, the finite quotient $\pi: X \to Y = X/\iota$ has image divisor $C = \pi(D)$ and branch divisor $B = \pi(R) \in |-2(K_Y + C)|$.
The pair $(Y, C)$ is a log del Pezzo surface of index at most 2, and $(Y, C + \frac{1+\varepsilon}{2} B)$ is log canonical for $\varepsilon > 0$.
There is an exact relation $$ K_X + D + \varepsilon R = \pi^*\left( K_Y + C + \frac{1+\varepsilon}{2}B \right).
$$ This induces a bijection between $(K+D)$-trivial involution pairs and such log del Pezzo pairs with branch data [Alexeev--Engel 2022, Prop. 2.2.1]. For instance, in the boundary analysis of $F_{{\mathrm{En}}, 2}$, the image pairs $(Y, C)$ arising in this way include the rational log del Pezzo surfaces of type $A_n$, $D_n$, $E_n$, and their foldings, as classified by the corresponding diagrams in (**AEGS23?**).

#### Degenerations and Dual Complex Topology

Let $\{ (Y_t, [{\mathcal{L}}*t]) \}*{t \in \Delta^*}$ be a family of polarized Enriques surfaces degenerating, after base change and birational modification, to a KSBA-stable pair $(Y_0, [{\mathcal{L}}_0])$.
The associated family of K3 double covers $({\mathcal{X}}_t \to Y_t)$ admits a Kulikov model degeneration ${\mathcal{X}}_0$, and the involution $\iota$ extends to ${\mathcal{X}}_0$ over the ${\mathcal{X}}_0$.
The quotient $Y_0' \mathrel{\mathop:}=  {\mathcal{X}}_0/\iota$ is a dlt model of the ${\mathcal{X}}_0$ in the KSBA compactification (**AEGS23?**, Thm.
1.1).

The topological type of the dual complex $\Gamma(Y_0')$ is determined by the boundary chamber (or cusp) type, which is classified by the Coxeter diagram appearing in the stable boundary reflection group at the given primitive isotropic vector.
The correspondence is as follows:

- For the generic Type ${\textrm{III}}$ boundary stratum, corresponding to the chamber of Coxeter type $\widetilde{E}_8 + \widetilde{E}_8$, the dual complex $\Gamma(Y_0')$ is a simplicial triangulation of ${\mathbf{RP}}^2$.
  This reflects the quotient, under the covering involution, of the $S^2$-dual complex for the corresponding K3 Kulikov model.
  The configuration of irreducible components and their intersections is prescribed by the maximal parabolic subdiagrams of type $\widetilde{E}_8 + \widetilde{E}_8$ in the Coxeter diagram; see [(**AEGS23?**), §6.3; Example 6.13].

- For Type ${\textrm{II}}$ and for Type ${\textrm{III}}$ degenerations associated to other boundary chambers -- such as those with Coxeter diagrams of types $\widetilde{E}*8 + \widetilde{D}*{10}$, $\widetilde{D}_{16}$, etc. -- the dual complex $\Gamma(Y_0')$ is homeomorphic to a 2-disk.
  The number and configuration of components reflect the combinatorics of the chamber, with vertices given by maximal parabolic subdiagrams that contain the corresponding cusp [(**AEGS23?**), Prop. 6.6; Table 6.1; Table 6.2].

- In certain special (non-generic) degenerations, especially for Type ${\textrm{II}}$, the dual complex reduces further to a segment.
  Such cases are realized when the normalization of the ${\mathcal{X}}_0$ consists of two irreducible components meeting transversely, as in (**AEGS23?**, Example 8.18).

The combinatorial structure of the degeneration is dictated by the Coxeter chamber associated to the boundary cusp $\eta$ and the arrangement of root hyperplanes in the boundary lattice $ \overline{T}\_{ \eta } $.
The induced dual complex encodes the precise gluing pattern and intersection properties of irreducible components in the normalization, as detailed in (**AEGS23?**, Prop.
6.6, Table 6.1, Table 6.2).

#### Construction of Boundary Models from Combinatorial Data

Given $\eta \in T$ and the associated boundary lattice $ \overline{T}*{ \eta } $, the Coxeter diagram $G(\Gamma*\eta)$, or a suitable refinement or folding, determines the boundary combinatorics.
Each Coxeter chamber corresponds to a polyhedral complex in ${\mathbf{R}}^2$, naturally interpreted as the dual complex of the ${\mathcal{X}}_0$ of a stable degeneration.
Vertices of this complex are indexed by maximal parabolic subdiagrams in the Coxeter diagram, and edges correspond to adjacent subdiagrams; see [(**AEGS23?**), §5; §7.2].

Given a choice of monodromy vector (integral-affine data, for example, a vector $\ell$ as in (**AEGS23?**, Example 5.12)), one constructs a triangulated sphere or disk whose combinatorial type is determined by the Coxeter chamber.
To each vertex there is assigned a log del Pezzo surface (often toric, but not always: "flowerpot" and Coble surfaces are realized at certain cusps; cf.
(**AEGS23?** Example 7.10, Table 4.1)), and the explicit gluing is determined by the adjacency in the polyhedral complex.
The polarization and branching data are prescribed by the structure of adjacent faces and dual monodromy invariants.

A central result is that, up to automorphisms, every stable pair in the boundary of the KSBA compactification arises via this combinatorial construction, and each configuration classified by the Coxeter data is geometrically realized [(**AEGS23?**), Thm. 7.2, Table 7.1; §8.4].

#### Explicit Example: Cusp 3 Degeneration

Consider $T = U \oplus E_8(2)$ and let $\eta$ correspond to a primitive isotropic vector associated to a boundary component whose root diagram is the fold of $E_8 \oplus D_{10}$.
The corresponding Coxeter fan determines a dual complex with a disk topology comprising twelve vertices, corresponding to surface components indexed by the maximal parabolic subdiagrams of the folded diagram.
The monodromy vector $$ \ell = (2,0^{15},2,4,6,4,0,4)

$$
determines the precise affine structure on the disk; each vertex star prescribes a (possibly non-toric) log del Pezzo surface, and the full gluing is determined by the adjacency in the Coxeter graph in(**AEGS23?**). For Cusp 3 in the Enriques compactification, this construction yields a dlt model whose normalization is described in [CDL24, §3.2] and whose explicit geometric data is tabulated in (**AEGS23?**).

<!-- Source: 2-part-moduli/5-chapter-ias-dlt/900-ade-surfaces.md -->

### ADE Surfaces

This section presents the theory of ADE surfaces (**AT19?**), which provides a classification of log canonical log del Pezzo surfaces of index two with ADE boundary configurations. All definitions, constructions, and results in this section are from (**AT19?**) unless otherwise noted.

#### $\mathrm{ADE}$ and $\widetilde{ \mathrm{ADE} } $ Surfaces: Combinatorics and Constructions

Let $Y$ be a normal projective surface defined over an algebraically closed field of characteristic zero, and let $C = \sum_i C_i$ be a reduced, effective Cartier divisor on $Y$, with irreducible components $C_i$. The pair $(Y, C)$ is called an ADE surface if the dual intersection graph of the $C_i$ is isomorphic, as an abstract graph, to the Dynkin diagram of type $A_n$, $D_n$, or $E_n$ in its simply-laced incarnation. This graph records the incidence structure of the boundary: each vertex corresponds to a component $C_i$, and an edge reflects a simple transverse intersection between $C_i$ and $C_j$. These are log canonical log del Pezzo surfaces of index two: pairs $(Y, C)$ such that $2K_Y + C$ is Cartier, $-(K_Y + C)$ is ample, and $(Y, C)$ admits strictly log canonical singularities in the sense of the MMP. ADE configurations as boundary graphs result from surface birational geometry and log canonical threshold constraints, which restrict admissible degenerations and underlie the KSBA compactification for surfaces of general type (**AT19?**).

Pure ADE surfaces admit canonical toric models. For each simply-laced root system $\Phi$, there exists a toric surface $Y_\Phi$ whose Coxeter fan reflects the arrangement of simple roots. The boundary divisor $C$ is supported on certain torus-invariant irreducible divisors such that the dual intersection graph of $C$ coincides with the diagram of $\Phi$. The geometry of $(Y_\Phi, C)$ is encoded by the class of a convex lattice polytope $P \subset {\mathbf{Z}}^2$, with vertices explicitly given according to type: for instance, for type $A_{2n-1}$, the polytope is the triangle with vertices at $(0,2), (0,0), (2n,0)$, and $C$ equals the sum of the divisors supported on the two edges meeting at $(0,2)$. For type $D_{2n}$, the polytope is a quadrilateral with vertices $(2,2), (0,2), (0,0), (2n-2,0)$; the configuration of toric divisors reflects the fork of the $D$-type diagram. The exceptional types $E_6$, $E_7$, and $E_8$ correspond to quadrilaterals whose rightmost vertex differentiates the respective diagram (**AT19?**, Table 1). The polytope $P$ has sides of length one or two as measured in the lattice $N \cong {\mathbf{Z}}^2$. An edge of length two is a long side (white node); an edge of length one is a short side (black node). Long and short sides determine which priming operations are allowed. Priming (**AT19?**) blows up (potentially with weight) a smooth point on a boundary component $C_j$. A blowup at an edge of length two decreases this length to one and is marked by a prime at the corresponding node. Multiple sequential blowups (primings) are encoded by repeated primes or node-circling conventions, and a minus sign denotes a side that has become short. Allowed primings are classified in (**AT19?**, Table 4), with only certain operations preserving normality, log canonicity, and toric structure. Pure shapes have simple undecorated boundary divisors; primed shapes arise from permissible priming sequences. Affine ADE surfaces have boundary graphs $\widetilde{A}_n$ (cycle of $n+1$ curves), $\widetilde{D}_{2n}$, or $\widetilde{E}_{7,8}$. Toric realizations: $\widetilde{A}_n$ via $(n+1)$-gon, others via polytopes with cyclic/branching structure extending the finite ADE patterns. Let \$ \Gamma \$ be a (dual) Coxeter--Dynkin diagram associated to a lattice \$ L \$, equipped with a finite group of automorphisms \$ \mathrm{Aut}(\Gamma) \$. The set of nodes (vertices) is \$ \mathcal{N} \$, and edges \$ \mathcal{E} \$. The decorated diagram \$ (\Gamma, \mathcal{C}, \mathcal{A}, \mathcal{M}, \mathcal{S}) \$ is specified by the data:

-   \$ \mathcal{C} \subseteq \mathcal{N} \$: set of circled nodes, with each \$ v \in \mathcal{C} \$ signifying a simple root (or wall) where an additional priming operation is admissible---that is, \$ \mathcal{C} \$ parameterizes loci permitting further wall-crossings in the sense of primed polyhedral decompositions or lattice extensions.
-   \$ \mathcal{A} \subseteq \mathcal{E} \$: set of arrows, with each \$ (i \to j) \in \mathcal{A} \$ representing a directed edge; such orientation encodes folding via a nontrivial automorphism \$ \varphi \in \mathrm{Aut}(\Gamma) \$ such that the orbit \$ O_i = O_j \$ is identified under \$ \varphi \$, collapsing \$ \Gamma \$ to a quotient diagram \$ \Gamma' = \Gamma/\langle \varphi \rangle \$.
-   \$ \mathcal{M}: \mathcal{E} \rightarrow \mathbb{N}*{\geq 1} \$: edge multiplicity function, where \$ \mathcal{M}(e) \> 1 \$ signals the presence of multiple bonds between nodes, corresponding to non-simply-laced types---the bond of order \$ m \$ between \$ i \$ and \$ j \$ indicates a Cartan matrix entry \$ a*{ij} = -m \$ (with the usual convention \$ a\_{ii}=2 \$).
-   \$ \mathcal{S}: \mathcal{N} \rightarrow \Xi \$: a coloring map, partitioning nodes into orbits under an automorphism group \$ H \leq \mathrm{Aut}(\Gamma) \$, so that \$ \mathcal{S}\^{-1}(\xi) \$ records equivalence classes of roots or gluing data under \$ H \$. The canonical assignment of decorated strata \$ (\Gamma, \mathcal{C}, \mathcal{A}, \mathcal{M}, \mathcal{S}) \$ to boundary strata \$ \Delta \subset \overline{\mathcal{M}} \$ in the KSBA or toroidal/semitoric compactification is as follows: each circled node \$ v \in \mathcal{C} \$ corresponds to an irreducible component of the boundary divisor \$ D_v \subset \overline{\mathcal{M}} \$ that admits further priming, while each folding (arrow or multi-bond) encodes the isomorphism type of the stratum as a stack quotient or root stack \$ [Z/G] \$, with possible ramifications \$ \mathbb{Q}\text{-divisor} \$ coefficients \$ \frac{1}{m} \$, where \$ m \$ is the folding order or ramification index. The coloring function \$ \mathcal{S} \$ tracks the multiplicity and stacking structure arising from the automorphism or gluing data implicit in the global period mapping and determines the ramification behavior of the boundary. All such data are formalized in the decorated diagram, which parameterizes a unique (stack-theoretic) boundary stratum or birational modification, as constructed in explicit form in (**AEGS23?**).

\todo{Check}

Explicit models assign boundary configurations to toric (or stacky or nontoric) surfaces according to Coxeter fan data, combinatorial encodings of birational modifications, and MMP constraints. These underlie boundary phenomena, dual complexes, and moduli stratification in higher-dimensional and singular surface theory (**AT19?**, Tables 1 and 4, Lemmas 3.4 and 3.25, Theorem 4.2).

#### Surface Geometry and Divisor Formulae
Let $Y$ be a normal projective surface as in Section 1, and $C$ a reduced effective divisor whose dual intersection graph is of ADE type. These surfaces admit a canonical double cover encoding the relationship between boundary and branch data in stable pairs and moduli of surfaces of general type. Suppose $(Y, C)$ is as above and admits additional data consisting of an effective divisor $B$, called the branch divisor, satisfying the numerical equivalence $B \sim 2K_Y + C$ in the Picard group $\operatorname{Pic}(Y)$. The normalization of the double covering $\pi: X \to Y$ branched over $B$ gives a normal surface $X$ with $D = \pi^{-1}_*C$ the reduced preimage of $C$. The involution on $X$ induced by the double cover is nontrivial and fixed by a ramification divisor $R \subset X$, equal to the reduced preimage of $B$. The canonical divisor satisfies
$$
K_X + D + R = \pi^*\left(K_Y + C + \tfrac{1}{2}B\right) ,$$ When $B$ is effective, Cartier, and disjoint from $C$, this gives a semi-log canonical surface pair of index two in the sense of classification theory (**AT19?**, Lemma 4.1).

The conditions on $Y$, $C$, and $B$ are: The pair $(Y, C)$ must be log canonical, with $B$ an effective, reduced Cartier divisor whose support does not contain any component of $C$, and all singularities of $Y$ lying along $B$ must be Du Val singularities (rational double points).
This determines the singularities of $X$ and the positivity of canonical bundles.

Let \$ f: X \to Y \$ be a double cover of a normal surface \$ Y \$, branched over a reduced effective divisor \$ C \subset Y \$, with \$ D \subset X \$ the reduced branch divisor, i.e., the reduced preimage \$ D = f\^{-1}(C)\_{\text{red}} \$.
The classification of such double covers can be organized according to the possible configurations of the boundary divisor \$ D \$:

- **Case I:** \$ D = \varnothing \$ (empty boundary).
  Here \$ C = \varnothing \$, so \$ f \$ is étale and \$ X \$ is an étale double cover of \$ Y \$.
  If \$ Y \$ is canonical (e.g., a log Enriques surface or a K3 surface with isolated singularities), then \$ X \$ is canonical as well.
  In particular, when the étale cover is nontrivial (i.e., \$ Y \$ is an Enriques surface and \$ X \$ is its K3 canonical cover), the involution on \$ X \$ acts freely outside finitely many points; the fixed locus is empty, and the singularities of \$ Y \$ lift to corresponding canonical singularities on \$ X \$.

- **Case II:** \$ D = f\^{-1}(C)\_{\text{red}} \$ is a union of one or two smooth (not necessarily connected) elliptic curves.
  Here, \$ C \subset Y \$ is a union of smooth elliptic curves, and the ramification is transverse and reduced.
  The pair \$ (X, D) \$ is strictly log canonical: at generic points of \$ D \$, the pair is log smooth, and at intersection points, at worst strictly log canonical but not log terminal.
  The boundary reflects elliptic phenomena: both the covering \$ X \$ and the base \$ Y \$ can have log canonical singularities along \$ D \$ and \$ C \$ (respectively), but no worse.
  This case corresponds to degenerations where the branch locus acquires smooth elliptic components.

- **Case III:** \$ D = f^{-1}(C)*{\text{red}}\ \$\ is\ a\ cycle\ of\ smooth\ rational\ curves,\ i.e.,\ \$\ D\ =\ \cup*{i=1}^r D_i \$ with \$ D_i \simeq \mathbb{P}\^1 \$, and the dual graph of \$ D \$ is a cycle or a fork (a configuration star-shaped at a node with three branches).
  These configurations arise from branch curves \$ C \$ with normal crossings whose preimages under \$ f \$ arrange as such.
  The pair \$ (X, D) \$ is strictly log canonical: the discrepancies at components of \$ D \$ are zero and at singularities of \$ D \$ (nodes), the log canonical threshold is one.
  Such arrangements correspond to semi-stable or boundary components in KSBA moduli, and the dual graphs of \$ D \$ reflect the intersection types classified in stable surface degenerations (**AEGS23?**, Prop.
  5.9) (**nonsymplectic-involutions?**).

\todo{Check}

In all cases, the log canonical pair \$ (X, D) \$ is uniquely determined (up to isomorphism) by the branch data \$ (Y, C) \$, and the configuration of \$ D \$ (empty, elliptic, or rational cycle/fork) determines both the geometric and singularity-theoretic type of the double cover and its place in the compactified moduli space.

These are boundary strata in the KSBA or generalized stable pair compactification, determined by admissibility of $(Y, C, B)$ (**AT19?**, Theorem 4.2).

The local geometry and singularity structure depends on the interaction between the branch divisor $B$ and the boundary divisor $C$, particularly at points of intersection or ramification.
At a general point of $B$, if $Y$ is smooth, the covering $\pi$ yields ordinary double points (type $A_1$) on the ramified locus of $X$.
More generally, at points of transverse intersection $p \in B \cap C$, the local equation near $p$ can be written as $u^2 = f(x, y)$ where $f$ defines the local analytic germ of $B$, and the preimage in $X$ typically acquires a singularity of type $A_n$, reflecting the connection with the minimal resolution data of Du Val singularities.

Along the boundary, the intersection behavior is controlled by the combinatorics of the dual graph.
Each component of $C$ meets its neighbors transversely; self-intersection numbers are determined by the toric or decorated polytope but do not introduce further singularities in the normal crossing setting.
Ramification along $C$ is precluded by requiring that $B$ does not contain any component of $C$, so the preimage in $X$ is unramified away from the finite set of intersection points $B \cap C$.

Singularities on $Y$ (and correspondingly on $X$ after normalization) for quadruples $(Y, C, B, X)$ are restricted to ADE (Du Val) types, as local analytic models near the branch locus must yield rational double points.
At each singularity of $Y$ on $B$, the pair $(Y, C + {1\over 2}B)$ is log canonical if and only if the singularity of $Y$ is Du Val and the point does not lie on $C$ (**AT19?**, Lemma 4.1). All stable limit surfaces in the boundary strata of the KSBA or toroidal compactifications admit uniform description via double cover and divisor data, with explicit local models and combinatorial invariants from the arrangement of $(Y, C, B)$.
These exhaust all arrangements under log canonicity and divisor positivity constraints, determining degenerations, dual complexes, and automorphism groups (**AT19?**).

#### Folding to $BC$ Surfaces: Combinatorics and Construction

Let $\Phi$ be a simply-laced root system of ADE type.
Folding passes from $\Phi$ to a non-simply-laced root system by quotienting the Dynkin diagram by a nontrivial automorphism.
When the diagram admits a symmetry of order two, the invariants of the automorphism define a new root system: for example, the outer automorphism of $A_{2n-1}$ induces the root system $C_n$, and a similar involution on $D_{n+1}$ yields $B_n$.
The resulting diagrams are those of $B_n$, $C_n$, and $BC_n$, characterized by double bonds and merged nodes indicating multiple edge multiplicities in the root lattice.

Folding is depicted diagrammatically by arrows or symmetrization marks, where distinct nodes of the original ADE diagram are identified under the involution.
The quotient diagram thus acquires double bonds (for example, linking the unique short root in $B_n$ or $C_n$ to the adjacent node), and repeated nodes are merged.
The rank is preserved, but the resulting root systems become non-simply-laced, with root lengths and intersection structures encoded by the folding data.
This yields $BC$-type boundaries from ADE models (**AT19?**).

Given an ADE or affine ADE surface $(Y, C)$, folding forms the quotient $Y' = Y/\tau$ by a finite group of automorphisms $\tau$ preserving the boundary divisor $C$.
In the simplest cases, $\tau$ is the involution corresponding to the automorphism of the Dynkin diagram that exchanges symmetric nodes, and the geometric realization may require passing to a stacky (orbifold) quotient in the presence of fixed points.

Folding affects the toric polytope associated to $Y$: the involution acts as a lattice symmetry, identifying pairs of vertices and edges in a manner determined by the automorphism.
The quotient polytope has fewer vertices and may possess edges of length one or two, mirroring the root length distinction in $BC$-type systems.
In the divisor data, the new boundary $C'$ is the quotient of the original $C$, and its components may now carry multiplicities, non-reduced structure, or even half-integral coefficients due to the branching behavior of the cover.

The boundary $C'$ may consist of components of multiplicity two (resulting from merging distinct branches) or of non-reduced components.
In the most general constructions, the quotient may possess reduced, non-reduced, or fractional boundary divisors, with the latter arising whenever the branch locus of the involution is ramified over the original boundary or when the quotient fails to be Cartier in codimension one.
Such half-integral divisorial data play a crucial role in moduli and are absorbed into the theory of stable pairs by considering pairs with boundary coefficients in ${1\over 2}{\mathbf{Z}}$, as required by the ${\mathbf{Q}}$-Gorenstein property of the singularities and divisor configuration.

If $\pi: Y \to Y'$ is the quotient morphism and $C$ is the boundary on $Y$, then the pushforward $C' = \pi_*C$ may fail to be reduced, and the canonical divisor formula reflects half-divisors.
Specifically, the boundary on the quotient is typically expressible in the form $C' = \sum m_i C_i'$, where $m_i \in \{1, 2, {1\over 2}\}$ depending on the local ramification.
The canonical double cover inevitably restores the ADE type: the pullback $\pi^* C\prime$ decomposes into integral divisors on the cover, and the map is branched exactly along the non-reduced or half-integral components.
The divisor relation under folding is $$ K_X + D + R = \pi^*(K_Y + C + \tfrac{1}{2}B) ,$$ where $K_X$ and $K_Y$ denote the canonical class on the cover and base, $D$ is the pullback of the boundary, $R$ is the ramification divisor, and $B$ is the branch divisor (**AT19?**). In various degenerations---such as those of Enriques surfaces, realized via K3 surfaces with involution, or of log del Pezzo surfaces of index two---the boundary components are constructed to reflect the geometry of surfaces associated with ADE or folded $BC$-type Dynkin diagrams.
Folding operations introduce non-Cartier behavior and multiplicities in the boundary, often giving rise to divisors with coefficients $\frac{1}{2}$.
These arise naturally from quotient constructions involving stacky or singular surfaces.
Passing to the canonical double cover eliminates these fractional phenomena: it yields a normalization of the associated quotient surface in which the boundary becomes reduced and Cartier.
The resulting surface admits an ADE configuration, and its boundary stratification, dual complex, and period data are completely governed by the structure of the corresponding folded or unfolded Dynkin diagram.

#### Toric Polytope Data for Pure and Primed ADE (and Affine ADE) Shapes

ADE surfaces have toric realizations via lattice polygons encoding the intersection configuration of the boundary divisor and its dual graph.
Canonical polytopes (in $N \cong {\mathbf{Z}}^2$), boundary assignment data, and minimal marking conventions for the main ADE and affine ADE pure types, together with representative primed cases:

* * *
Type                   Polytope Vertices (in ${\mathbf{Z}}^2$)       Distinguished Vertex $p_*$   Boundary Assignment
* * *
$A_{2n-1}$             $(0,2),\ (0,0),\ (2n,0)$             $(0,2)$                      Two sides through $(0,2)$, corresponding to chain ends

$A_{2n-2}$             $(0,2),\ (0,0),\ (2n-1,0)$           $(0,2)$                      Left long, right short (minus at right end)

$-A_{2n-3}$            $(0,2),\ (1,0),\ (2n-1,0)$           $(0,2)$                      Left short (minus at left end), right long

$D_{2n}$               $(2,2),\ (0,2),\ (0,0),\ (2n-2,0)$   $(2,2)$                      Fork with both long ends

$D_{2n-1}$             $(2,2),\ (0,2),\ (0,0),\ (2n-3,0)$   $(2,2)$                      Fork with one short end (minus at lower end)

$-E_6$                 $(2,2),\ (0,3),\ (0,0),\ (3,0)$      $(2,2)$                      Double fork, all long

$-E_7$                 $(2,2),\ (0,3),\ (0,0),\ (4,0)$      $(2,2)$                      Double fork, all long

$-E_8$                 $(2,2),\ (0,3),\ (0,0),\ (5,0)$      $(2,2)$                      Double fork, all long

$\widetilde{A}_n$      Regular $(n+1)$-gon vertices         (arbitrary)                  All sides in a cycle

$\widetilde{D}_{2n}$   $(0,2),\ (0,0),\ (2n-4,0),\ (4,2)$   (convex hull, see )          Cycle with two additional branches

$\widetilde{E}_7$      $(0,4),\ (0,0),\ (4,0)$              (special, see )              Extended exceptional configuration

## $\widetilde{E}_8$      $(0,3),\ (0,0),\ (6,0)$              (special, see )              Extended exceptional configuration

Primed shapes truncate vertices along one or more edges.
Each priming at a long edge reduces its lattice length (marked by prime/circled node).
Toricity is lost beyond certain limits (**AT19?**, Table 4).

\todo{Swap diagram back in.}

#### Priming and Folding Table

Permissible operations depend on polytope combinatorics and long/short side configuration.
Priming at a lattice edge of length two is always allowed and indicated in the diagram as a prime at the corresponding node.
Priming at a short side (length one) is not allowed if it would violate ampleness, Cartier, or normality conditions.

Representative priming and folding possibilities and their notation (see (**AT19?**, Table 4) for full enumerations):

* * *
Surface Type                               Max Primings per Side        Toric When?
Decoration After Priming or Folding
* * *
$A_{2n-1}$ pure                            $\leq 1$ at ends             Always toric after one priming at each end   Prime ($'$) or minus ($^{-}$) at node

$D_{2n}$ pure                              $\leq 2$ at fork ends        Toric under certain limits                   Primes at arms; minus at short arms

$E_k$ pure ($k=6,7,8$)                     $\leq 1$ at ends             Toric for single priming                     Prime or circled node in diagram

General primed (multi)                     Prescribed in , Table 4      Only for bounded sequences                   Multiple primes or circled nodes

Folded ($BC_n$)                            N/A (folding, not priming)   Toric under symmetry conditions              Arrow, double bond, or merged node

## Affine types ($\widetilde{A}_n, \cdots$)   At special nodes, per        Certain cases only                           Circle or multi-prime on diagram

Folding is marked by diagram automorphism data: nodes are identified, and double bonds or arrows are drawn in the Coxeter/Dynkin diagram.
The resulting combinatorics record non-simply-laced root data, the origin of half-divisor structures, and signal possible quotient or stacky geometry.

\todo{May not need here, or put in appendix}

#### Sample Divisor Schemata

For a pair $(Y, C)$ where $Y$ is a surface of ADE or folded $BC$ type, consider the double cover $\pi: X \to Y$ branched along an effective divisor $B$, with $B \sim 2K_Y + C$, and let $D = \pi^{-1}**C$ denote the scheme-theoretic pullback of $C$.
The canonical divisor formula reads [ K_X + D + R = \pi\^*\left(K_Y + C + \tfrac{1}{2}B\right), ] where $R$ is the reduced ramification divisor of $\pi$.
In the case of a folded $C_n$ configuration arising from the quotient of the $A*{2n-1}$ Dynkin diagram by an involution exchanging its endpoints, the image of the boundary divisor can be decomposed as [ C' = C_1' + C_2' + \cdots + 2D\_*, ] where $D_*$ is the unique component resulting from folding two nodes of the original diagram, carrying multiplicity two.
Boundary divisors acquire coefficients $\frac{1}{2}$ when the quotient surface features stacky points or when the cover has nontrivial stabilizer groups, so that [ K_Y + C + \frac{1}{2}B ] is $\mathbb{Q}$-Cartier, but may fail to be Cartier.
Upon passage to the canonical double cover, the preimages of these boundary divisors regain integral coefficients, and the ADE-type combinatorics and properties are restored.
Priming, as defined in the context of ADE or folded $BC$ surface pairs, refers to a weighted blowup centered at a boundary node---typically a singularity or marked point of the boundary divisor $C$ on a normal (often orbifold or quotient) surface $Y$.
The weights are determined by the local intersection type: for nodes or singularities arising from folding (such as cyclic or stacky points), the process uses weights matching the local quotient or stack structure.
After priming, the new boundary is $C' = \widetilde{C} + E$, where $E$ is the exceptional divisor, and the canonical class becomes $K_{Y'} = f^* K_Y + a E$, with $a$ the discrepancy prescribed by the weights and local geometry.
In folded or quotient models (e.g., $D_{n+1}/\langle \iota \rangle$ to $B_n$), priming may be performed at stacky or orbifold nodes, with the resulting divisor structure capturing the essential combinatorial and intersection-theoretic changes to the polytope or Dynkin diagram.
This process ensures the moduli-theoretic and intersection data remain compatible with the KSBA compactification; see (**AT19?**) for full details.

<!-- [@AT19], especially Sections 3–4, 6, Tables 1 and 4, and Figures 1–3. -->

#### Moduli, Degenerations, and Dual Complexes

In the KSBA compactification of moduli spaces of stable pairs of index two, folding determines boundary strata corresponding to $BC$-type surface components.
When an ADE or affine ADE surface $(Y, C)$ with simply-laced Dynkin diagram admits a diagram automorphism---such as the involution on $A_{2n-1}$ or $D_{n+1}$---the quotient produces a pair $(Y', C')$ whose boundary is modeled on a non-simply-laced diagram of type $C_n$, $B_n$, or $BC_n$.

These folded or $BC$-type surface components appear as irreducible components in the boundary of the KSBA moduli space.
Each combinatorial class of folded diagram determines a corresponding boundary stratum, with the normalization of a degenerate fiber comprising unions of ADE and folded components, glued along divisors that may be non-reduced or have half-integral coefficients.
The moduli boundary stratification follows the enriched combinatorics induced by folding and the birational geometry of the possible degenerations.
The boundary strata encode degenerations from smooth surfaces to stable unions of ADE and folded $BC$ pairs, and each irreducible component of the moduli boundary corresponds to a distinct decorated or folded Dynkin diagram (**AT19?**).

#### Dual Complexes and Topology

Dual complexes encode the topological and combinatorial invariants of boundary strata.
The dual complex records incidence relations of irreducible components, encoding both the combinatorics of the boundary divisor and the gluing data along their intersections.
When folding is present, the dual complex of the ${\mathcal{X}}_0$ is a quotient of the dual complex associated to the simply-laced configuration by the automorphism group acting on the diagram.

If ${\mathcal{D}}_Y$ is the dual complex associated to the ${\mathcal{X}}*0$ of a degeneration with boundary configuration of affine ADE type, then after folding by an involutive automorphism, the complex ${\mathcal{D}}*{Y'} = {\mathcal{D}}_Y/\tau$ reflects the topological type of the folded configuration.
For example, folding a cycle corresponding to $\widetilde{A}_n$ yields an interval or disk, while folding the disk corresponding to $\widetilde{D}_n$ produces a real projective plane.
The quotient topology thus records the reduction in symmetry and the identification of strata arising from automorphism-invariant gluings.

Coxeter fans formalize these via arithmetic quotients $\overline{T}$ of the relevant lattice, and the reflection group $W(\Gamma_\eta)$ generated by reflections in roots preserved under the action of the arithmetic group.
The corresponding tiling of hyperbolic space, and the boundary complex of the toroidal compactification, realize the wall-and-chamber structures of the moduli problem reflecting the combinatorics of folded/unfolded diagrams and the action of the reflection group on the rational closure of the positive cone (**AT19?**).

#### Moduli Formulas and Compactifications

Folded and half-divisor strata are placed via toroidal and semi-toric compactifications associated to the Coxeter fan and its foldings.
In toroidal compactifications $ \overline{F_\Gamma}^{  \Sigma *{\bullet} } $ constructed from fans subdividing the positive cone of $\overline{T}*{\mathbf{R}}$, the boundary strata and their dual complexes are indexed by the faces and orbits of the tiling under the stable reflection group $W(\Gamma_\eta)$.
Folding induces identifications of chambers, faces, and cones, so that non-simply-laced (folded) types correspond to quotient strata in the compactification.
For quotients $q: (Y, C) \to (Y', C')$ realizing the folding: $$ K_{Y'} + C' + {1\over 2} B' = q_*(K_Y + C), \qquad 2K_{Y'} + C' \sim B', $$ where $B'$ is the branch divisor of the quotient.
Each moduli boundary component's normalization follows from this divisor data, and the dual complex structure is induced by the quotient of the Coxeter tiling and the associated fan.

Folded and half-divisor surfaces occupy explicit boundary strata of the toroidal compactification $ \overline{F_\Gamma}^{  \Sigma _{\bullet} } $, and correspond to stratified boundary data in the Baily--Borel and non-toroidal models via the interplay of Coxeter fans, reflection groups, and combinatorial folding.
The equations governing their period images, gluing, and degenerations are canonical functions of the geometry of the folded Coxeter diagram and the arithmetic subgroup data, following the compactification theory for lattice-polarized K3 and log del Pezzo moduli (**AT19?**).

<!-- Source: 3-part-main-theorem/000-part-3.md -->

# The Main Theorem {#part-3}

## Statement and Outline

This chapter is devoted to establishing the isomorphism $\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} *{\bullet} } { \, \xrightarrow{\sim}\, }    \overline{F*{{\mathrm{En}}, 2}} $:

:::{#thm:main-theorem .theorem title="{Main Theorem [@AEGS23, Theorem 1.1, Thm. 5.9]}
"}
Let $ \overline{F_{{\mathrm{En}}, 2}} $ denote the KSBA compactification of the moduli space $F_{{\mathrm{En}}, 2}$ of numerically polarized Enriques surfaces of degree $2$, and let $  \mathcal{F} _{\bullet}  = \left\{{  \mathcal{F} _k }\right\}_{k=1,2,3,4,5}$ be the explicit collection of semifans, one for each $0$-cusp as classified in \cref{thm:complete-classification-0-cusps-fen2}.

Then:

1.  The normalization $ \overline{F_{{\mathrm{En}}, 2}} $ is isomorphic to the semitoroidal compactification $\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} _{\bullet} }$ for these semifans,

2.  This compactification is toroidal over the $0$-cusps $2$ and $4$, their adjacent $1$-cusps, and cusp $35$, and strictly semitoroidal over all other cusps as described in \cref{lem:fent-semitoroidal-semifans-at-cusps}.

3.  There exists a toroidal compactification $\overline{F_{{\mathrm{En}}, 2}}^{ \Sigma _{\bullet}^{\operatorname{Cox}}}$ associated to the collection of Coxeter fans $ \Sigma ^{\operatorname{Cox}} = \left\{{  \Sigma ^{\operatorname{Cox}}_k }\right\}_{k=1,2,3,4,5}$, such that there is a chain of morphisms $$
    \overline{F_{{\mathrm{En}}, 2}}^{ \Sigma _{\bullet}^{\operatorname{Cox}}}
    \to
    \overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} _{\bullet} }
    \to
     \overline{F_{{\mathrm{En}}, 2}}
    $$ where the first morphism contracts cones corresponding to faces defined by irrelevant roots (see (**AEGS23?**)), and the second morphism is the normalization.
:::

We summarize this entire situation in the following diagram:

\begin{tikzcd}
\overline{F_{{\mathrm{En}}, 2}}^{ \Sigma _{\bullet}^{\operatorname{Cox}}} \arrow[d] &   & \overline{F_{(2,2,0)}}^{ \Sigma _{\bullet}^{\operatorname{Cox}}} \arrow[d] \\
\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} _{\bullet} } \arrow[equal, "\therefore"']{d} \ar[d] &
\overline{B}^{  \mathcal{F} _{\bullet} }
\ar[equal]{d} \ar[r, hook]   \ar[equal, ":="']{l}
& \overline{F_{(2,2,0)}}^{  \mathcal{F} _{\bullet} } \ar[equal]{d} \ar[d] \\
  { \overline{F_{{\mathrm{En}}, 2}} }^{\nu}   \arrow[d, "\nu"'] &
 {B}^{\nu}  \ar[d, "\nu"]
\ar[equal, dashed,"\exists \tilde \Phi"']{l}
\ar[dl, "\Phi"']
\ar[r, hook]
&   { \overline{F_{(2,2,0)}} }^{\nu}   \arrow[d, "\nu"] \\
 \overline{F_{{\mathrm{En}}, 2}}  \arrow[d] &
B := \overline{ j(F_{{\mathrm{En}}, 2}) } \ar[r, hook]
&  \overline{F_{(2,2,0)}}  \arrow[d] \\
F_{{\mathrm{En}}, 2} \arrow[rr, "j", hook] \arrow[rd, ->>] & \phantom{B} & F_{(2,2,0)} \\
\phantom{X} & j(F_{{\mathrm{En}}, 2}) \ar[ru, hook] \ar[uu, hook, bend right] & x
\end{tikzcd}

We define the embedding $j$, restrict to its image, take the Zariski closure, and then normalize to produce $B^\eta$.
Functoriality of normalization and the KSBA compactification gives am embedding of $B^\eta$ into $  { \overline{F_{(2,2,0)}} }^{\nu}  $, which is identified with a specific semitoroidal compactification $\overline{F_{(2,2,0)}}^{  \mathcal{F} *{\bullet} }$ for the ramification divisor.
We pull back that semifan data to obtain an identification of $B^\nu$ with a semitoroidal compactification $\overline{B}^{  \mathcal{F} *{\bullet} }$ by restriction, which we define to be $\overline{F*{{\mathrm{En}}, 2}}^{  \mathcal{F} *{\bullet} }$.
We then construct a morphism $\Phi:  {B}^{\nu} \to  \overline{F*{{\mathrm{En}}, 2}} $ by constructing a universal family, lifting it to an isomorphism to $  { \overline{F*{{\mathrm{En}}, 2}} }^{\nu}  $ using the universal property of normalization, and obtain an isomorphism $B^\nu \cong   { \overline{F_{{\mathrm{En}}, 2}} }^{\nu}  $ by Zariski's main theorem.
Thus $ {B}^{\nu} $ is used as an intermediate space which is isomorphic to both $\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} *{\bullet} }$ and $  { \overline{F*{{\mathrm{En}}, 2}} }^{\nu}  $.
The proof proceeds in the following steps:

1. Defining $F_{{\mathrm{En}}, 2}$ and $ \overline{F_{{\mathrm{En}}, 2}} $:

   The moduli stack $F_{{\mathrm{En}}, 2}$ is defined to parametrize numerically polarized Enriques surfaces of degree two and their KSBA stable limits.
   The compactification $ \overline{F_{{\mathrm{En}}, 2}} $ is constructed using the theory of stable surface pairs with boundary divisor weighted by $\varepsilon \ll 1$.
   Each point corresponds to a pair $(Z, \varepsilon R_Z)$ where $K_Z + \varepsilon R_Z$ is ample and the total pair is semi-log-canonical.

2. Realization of $F_{{\mathrm{En}}, 2}$ as a Noether--Lefschetz locus inside $F_{(2,2,0)}$:

   By \cref{lemma-fent-to-fttz-closed-immersion}, there is an immersion of $F_{{\mathrm{En}}, 2}$ into the moduli stack $F_{(2,2,0)}$ of K3 surfaces with a del Pezzo involution $\iota_{\operatorname{dP}}$ of type $(2,2,0)$.
   The image consists of K3 surfaces admitting an additional fixed-point-free involution $\iota_{{\mathrm{En}}}$, and is cut out by period-theoretic conditions.
   Its Zariski closure $B \subset  \overline{F_{(2,2,0)}} $ in the KSBA compactification is the Noether--Lefschetz locus parameterizing K3 surfaces $X$ whose quotients $Z \mathrel{\mathop:}= X/\iota_{{\mathrm{En}}}$ define Enriques surfaces.

3. Extension of $\iota_{{\mathrm{En}}}$ to the universal family of K3 surfaces over $B$ inherited from $F_{(2,2,0)}$:

   The moduli stack $ \overline{F_{(2,2,0)}} $ admits a universal family $({\mathcal{X}}, \varepsilon {\mathcal{R}})$, where ${\mathcal{R}}$ is the normalized ramification divisor of $\iota_{\operatorname{dP}}$.
   This family pulls back to a family over $B$ whose general fiber admits an Enriques involution $\iota_{{\mathrm{En}}}$ commuting with $\iota_{\operatorname{dP}}$.
   By the uniqueness of KSBA limits, $\iota_{{\mathrm{En}}}$ extends over the total space.

4. Quotient to produce a family of stable Enriques pairs over $B$:

   After extending $\iota_{{\mathrm{En}}}$, the quotient $({\mathcal{X}}_B, \varepsilon {\mathcal{R}}*B)/\iota*{{\mathrm{En}}}$ defines a family of stable Enriques pairs $({\mathcal{Z}}, \varepsilon {\mathcal{R}}_Z) \to B$, extending the universal family over the interior.
   The quotient preserves KSBA stability and compatible degeneration data.

5. Pass to $ {B}^{\nu} $ and descend the semifans from $ \overline{F_{(2,2,0)}} $:

   The normalization $ {B}^{\nu}  \to B$ is a proper, normal stack supporting the pullback of the universal family.
   The semifans associated to $ \overline{F_{{\mathrm{En}}, 2}} $, governed by the ramification semifan, restricts to induce a semifan on $ {B}^{\nu} $.
   The resulting combinatorics define a collection of folded semifans ${\mathcal{F}} = \{ {\mathcal{F}}_k \}$ determining the boundary stratification.

6. Show finiteness of the classifying map using the geometry of Kulikov models of K3 surfaces:

   The classifying morphism $\phi:  {B}^{\nu}  \to  \overline{F_{{\mathrm{En}}, 2}} $ is birational.
   To prove finiteness, one must exclude the existence of distinct K3 pairs giving the same Enriques quotient.
   This is achieved via explicit analysis of degenerations (see Sections 4 and 5): the Enriques quotient of a K3 degeneration cannot have a more singular ${\mathcal{X}}_0$ than its cover.
   Any strict coarsening of the semifans would contradict this.

7. Zariski's Main Theorem and identification of compactifications:

   Since $\phi$ is finite and birational, it is an isomorphism.
   The normalization $ \overline{F_{{\mathrm{En}}, 2}} $ is thus identified with the semitoroidal compactification $\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} *{\bullet} }$, as constructed via the restricted and folded ramification semifans for $F*{(2,2,0)}$.

<!-- Source: 3-part-main-theorem/6-chapter/100-defining-fen2.md -->

### Defining $F_{{\mathrm{En}}, 2}$ and $\overline{F_{{\mathrm{En}}, 2}}$ {#section-7-1}

:::{#def:fent .definition title="{Moduli Stack $\F_{{\mathrm{En}
}, 2}$ of Numerically Polarized Enriques Surfaces of Degree Two}"}
Let $F_{{\mathrm{En}}, 2}$ be the Deligne--Mumford stack over $\mathbb{C}$ parameterizing isomorphism classes of pairs $(Z, L)$, where

-   $Z$ is a smooth Enriques surface,
-   $L \in \mathrm{Pic}(Z)$ is a nef and big divisor class satisfying [ L\^2 = 2, \qquad L \cdot C \> 0 \text{ for every } (-2)\text{-curve } C \subset Z. ] Two pairs $(Z, L)$ and $(Z', L')$ are isomorphic if there exists an isomorphism $\varphi : Z \xrightarrow{\sim} Z'$ such that $\varphi^* L' \equiv L$. The numerical equivalence represents the action of the automorphism group of $Z$ and preserves the polarization class up to numerical type.
:::

:::{#def:cpt-fent .definition title="{KSBA Compactification $\\overline{\F_{{\mathrm{En}
}, 2}}$ of $\F_{{\mathrm{En}}, 2}$}"}
Fix a rational $0 < \varepsilon \ll 1$. The KSBA compactification $\overline{F_{{\mathrm{En}}, 2}}$ is defined as the Deligne--Mumford stack whose objects over $\mathbb{C}$-schemes are isomorphism classes of pairs $(Z, \varepsilon R_Z)$, satisfying:

-   $Z$ is a projective surface with numerically trivial canonical divisor, $K_Z \equiv 0$,
-   $R_Z$ is an effective $\mathbb{Q}$-Cartier divisor such that the pair $(Z, \varepsilon R_Z)$ is semi-log-canonical (slc),
-   The divisor $K_Z + \varepsilon R_Z$ is ample,
-   On the open locus where $Z$ is smooth, $R_Z$ is numerically equivalent to $2L$ for some $(Z, L) \in F_{{\mathrm{En}}, 2}$.

The open substack consisting of pairs with smooth $Z$ and $R_Z$ the branch divisor of the associated K3 double cover is canonically isomorphic to $F_{{\mathrm{En}}, 2}$.
:::

:::{#thm:basic-fent .theorem title="{Basic Properties of $\\overline{\F_{{\mathrm{En}
}, 2}}$}"}
The stack $\overline{F_{{\mathrm{En}}, 2}}$ is a proper, separated, normal Deligne--Mumford stack of finite type over $\mathbb{C}$ . The inclusion $F_{{\mathrm{En}}, 2} \hookrightarrow \overline{F_{{\mathrm{En}}, 2}}$ realizes $F_{{\mathrm{En}}, 2}$ as the maximal open substack whose geometric points correspond to smooth numerically polarized Enriques surfaces of degree two. Each one-parameter family in $F_{{\mathrm{En}}, 2}$ admits a unique extension, up to unique isomorphism, to $\overline{F_{{\mathrm{En}}, 2}}$. That is, the KSBA compactification provides unique stable limits for degenerating families.
:::

#### Discussion

Pairs $(Z, L)$ as above parametrize the interior of the moduli problem, encoding the data of smooth numerically polarized Enriques surfaces of degree two.
The KSBA compactification $\overline{F_{{\mathrm{En}}, 2}}$ systematically includes stable degenerations: objects $(Z, \varepsilon R_Z)$ where $Z$ may acquire slc singularities and $R_Z$ encodes the limiting polarization data through its intersection and ramification structure.

This compactification captures limiting behavior for degenerations in a manner compatible with the log minimal model program (MMP). The identification and extension of the period lattice structure and polarization data across the boundary provide the stack $\overline{F_{{\mathrm{En}}, 2}}$ with a precise modular interpretation necessary for arithmetic and geometric applications.
Further refinements of this construction---such as the explicit realization of $F_{{\mathrm{En}}, 2}$ and its compactification as a Noether--Lefschetz locus in the KSBA compactified moduli of polarized K3 surfaces, and the construction of the polyhedral semitoroidal boundary---are systematically developed in subsequent sections.

<!-- Source: 3-part-main-theorem/6-chapter/200-noether-lefschetz.md -->

### Realization of $F_{{\mathrm{En}}, 2}$ as a Noether--Lefschetz Locus in $F_{(2,2,0)}$ {#section-7-2}

In this section, we establish that the moduli space $F_{{\mathrm{En}}, 2}$ of degree-2 polarized Enriques surfaces is realized as a locally closed, irreducible sublocus of a Noether--Lefschetz locus inside $F_{(2,2,0)}$, the moduli space of degree-4 polarized K3 surfaces with a nonsymplectic involution of fixed type.

:::{#def:canonical-cover-involution .definition title="{Canonical Cover and Involution Structure}
"}
Let $(Z, L)$ be a smooth Enriques surface equipped with an ample line bundle $L$ having self-intersection $L^2=2$. The canonical étale double cover [ \pi: X \longrightarrow Z ] is uniquely determined by $K_Z$. The deck transformation of $\pi$ is a fixed-point-free involution $\iota_{{\mathrm{En}}}: X \to X$---the **Enriques involution**. The class $H \mathrel{\mathop:}= \pi^*L$ is a nef and big divisor on $X$ with $H^2 = 4$. There is a unique involution $\iota_{\operatorname{dP}}: X \to X$ distinct from $\iota_{{\mathrm{En}}}$, commuting with $\iota_{{\mathrm{En}}}$ and fixing $H$, arising as the base change of the degree-2 linear system on $Z$. According to Nikulin's classification, $\iota_{\operatorname{dP}}$ is a nonsymplectic involution of type $(2,2,0)$.
:::

:::{#def:canonical-map-j .definition title="{The Canonical Map $j$}
"}
The association [ (Z, L) \mapsto (X, H = \pi\^\*L, \iota_{\operatorname{dP}}) ] defines a functorial morphism [ j: F_{{\mathrm{En}}, 2} \to F_{(2,2,0)}, ] where $F_{{\mathrm{En}}, 2}$ is the moduli of degree-2 polarized Enriques surfaces and $F_{(2,2,0)}$ the moduli of degree-4 polarized K3 surfaces with a nonsymplectic involution of type $(2,2,0)$. This construction is compatible with base change and extends to families.
:::

:::{#def:noether-lefschetz-locus .definition title="{Noether–Lefschetz Locus $\\mathrm{NL}
_{{\mathbf{T}}_{{\mathrm{En}}}}$}"}
Let $\Lambda = H^2(X, \mathbb{Z}) \cong \mathrm{II}_{3,19}$, and let $T_{{\mathrm{En}}} = U(2) \oplus E_8(-2)$ denote the anti-invariant lattice under the Enriques involution, reflecting both the required polarization and involution structure. Define the **Noether--Lefschetz locus** [ \mathrm{NL}\_{T_{{\mathrm{En}}}} = \left{ [X] \in F_{(2,2,0)} {~\mathrel{\Big\vert}~} T_{{\mathrm{En}}} \hookrightarrow \operatorname{Pic}(X) \text{primitively}, [\iota_{\operatorname{dP}},\iota_{{\mathrm{En}}}] = 0 \text{ for some } \iota_{{\mathrm{En}}} \right}. ,] whose points parameterize polarized quartic hyperelliptic K3 surfaces $(X, H)$ with involutions so that $(X, H, \iota_{\operatorname{dP}}, \iota_{{\mathrm{En}}})$ descends to data of a (possibly degenerate) degree-2 polarized Enriques surface.
:::

\todo{Drop in comments about NL locus, possibly many irreducible components, might have to justify that the image is \textbf{equal} to the NL locus?}

:::{#prop:lattice-theoretic-image-j .proposition title="{Lattice-Theoretic Description of the Image of $j$}
"}
The image $j(F_{{\mathrm{En}}, 2})$ consists precisely of those $(X, H, \iota_{\operatorname{dP}}) \in F_{(2,2,0)}$ for which:

-   $X$ admits a commuting involution $\iota_{{\mathrm{En}}}$,
-   $\iota_{{\mathrm{En}}}$ is fixed-point-free,
-   The anti-invariant lattice is $\operatorname{Pic}(X)^{\iota_{{\mathrm{En}}}} = T_{{\mathrm{En}}}$.

Equivalently, [ j(F_{{\mathrm{En}}, 2}) = \left{ (X, H, \iota_{\operatorname{dP}}) \in F_{(2,2,0)} : \exists \iota_{{\mathrm{En}}}, [\iota_{{\mathrm{En}}},\iota_{\operatorname{dP}}]=0, \text{ and } \operatorname{Pic}(X)\^{I_{{\mathrm{En}}} = -1} = T_{{\mathrm{En}}} \right}. ]
:::

:::
proof
For $X = \pi^{-1}(Z)$ as above, the involution $\iota_{{\mathrm{En}}}$ is fixed-point-free, $\iota_{\operatorname{dP}}$ arises canonically from the polarization, and the anti-invariant lattice is explicitly computed as $T_{{\mathrm{En}}}$ using the cohomology of double covers and the configuration of the involutions. The presence of these two commuting involutions together with the polarization forces the Picard lattice to contain $T_{{\mathrm{En}}}$ primitively. Conversely, any $(X, H, \iota_{\operatorname{dP}})$ with such a primitive embedding and compatible involutions arises as the canonical cover of some Enriques surface with polarization of degree $2$.
:::

:::{#prop:period-compatibility .proposition title="{Period Compatibility and Linear Subdomain}
"}
Let $S_{\operatorname{dP}}$ be the invariant lattice of $\iota_{\operatorname{dP}}$ and $S_{{\mathrm{En}}}$ that of $\iota_{{\mathrm{En}}}$. Then [ T_{\operatorname{dP}} \oplus S_{\operatorname{dP}} = T\_{\mathrm{en}} \oplus S_{{\mathrm{En}}} \hookrightarrow H\^2(X, \mathbb{Z}), ] with $T_{\operatorname{dP}} \cong U(2)$ and $T_{\mathrm{en}} \cong U(2) \oplus E_8(-2)$. For any $(Z,L) \in F_{{\mathrm{En}}, 2}$, the period point for $X$ lies in the orthogonal complement of $T_{{\mathrm{En}}}$ in the K3 period domain. Thus, the image $j(F_{{\mathrm{En}}, 2})$ is described as the subset of the moduli space where the periods are orthogonal to the fixed lattice $T_{{\mathrm{En}}}$.
:::

:::
proof
This follows directly from the construction: the double cover, involutions, and polarization together prescribe the lattice embedding, forcing the period to be on the locus cut out by the orthogonality to $T_{{\mathrm{En}}}$.
:::

:::{#def:zariski-closure-b .definition title="{Zariski Closure $B$}
"}
Define [ B := \overline{j(F_{{\mathrm{En}}, 2})} \subset  \overline{F_{(2,2,0)}}  ] as the Zariski closure of $j(F_{{\mathrm{En}}, 2})$ in the KSBA compactification. This $B$ forms a closed Noether--Lefschetz locus, parametrizing all limits (in the KSBA sense) of K3 surfaces that are double covers of Enriques surfaces, possibly with semi-log canonical singularities and compatible involution structure.
:::

:::{#prop:realization-dimension .proposition title="{Realization and Dimension}
"}
$F_{{\mathrm{En}}, 2}$ is realized as a locally closed, irreducible component of the Noether--Lefschetz locus $\mathrm{NL}_{T_{{\mathrm{En}}}} \subset F_{(2,2,0)}$. The Zariski closure $B$ in $ \overline{F_{(2,2,0)}} $ parametrizes exactly all (possibly degenerate) degree-4 K3 surfaces $(X, H)$ with a compatible pair of involutions $(\iota_{{\mathrm{En}}}, \iota_{\operatorname{dP}})$ arising from a numerically polarized Enriques surface (or its stable degeneration).
:::

:::
proof
By the arguments above, the construction $j$ embeds $F_{{\mathrm{En}}, 2}$ into $\mathrm{NL}_{T_{{\mathrm{En}}}}$ defined by the period and lattice conditions. Local closedness follows because the period subdomain is defined by a linear orthogonality condition. The irreducibility and dimension count come from the identification of the period domain for Enriques surfaces as a 10-dimensional linear section inside the ambient 20-dimensional K3 period domain by the global Torelli theorem.
:::

: Both $B$ and $F_{{\mathrm{En}}, 2}$ are 10-dimensional: this dimension is determined by period theory.
The period domain for numerically degree-2 polarized Enriques surfaces is a linear subdomain (cut out by the orthogonality to $T_{{\mathrm{En}}}$) of the 20-dimensional period domain for degree-4 K3s with involution, and its dimension is 10 by classical results.
Every Enriques surface in $F_{{\mathrm{En}}, 2}$ and every KSBA degeneration thereof in $B$ is canonically covered by a K3 surface $X$ (possibly degenerate).
The full modular datum of the point, including degenerations, is encoded by the triple $(X, \iota_{\operatorname{dP}}, \iota_{{\mathrm{En}}})$: the surface and two commuting involutions, precisely reflecting the structure of the double cover and the polarization.

:::{#prop:compatibility-period-map .proposition title="{Compatibility of Period Map}
"}
For any $(Z, L) \in F_{{\mathrm{En}}, 2}$, the Hodge structure on its canonical K3 cover $X$ lies in the orthogonal complement of $T_{{\mathrm{En}}}$ in the K3 period domain. The period map for $F_{{\mathrm{En}}, 2}$ factors through the period map for $F_{(2,2,0)}$ as a linear subspace cut out by the linear condition of being orthogonal to $T_{{\mathrm{En}}}$.
:::

:::
proof
The characterization of the period domain for Enriques surfaces (with fixed degree-2 polarization) as a linear section of the K3 period domain follows immediately from the splitting of the full lattice into invariant and anti-invariant parts for the involutions, and the polarization data forces a unique class in the orthogonal complement.
:::

<!-- Source: 3-part-main-theorem/6-chapter/300-extend-univ-family.md -->

### Extension of $\iota_{{\mathrm{En}}}$ to the Universal Family over $B$ {#section-7-3}

In this section, we construct and analyze the global extension of the Enriques involution $\iota_{{\mathrm{En}}}$ to the universal KSBA family of K3 surfaces over the Noether--Lefschetz locus $B \subset \overline{F_{(2,2,0)}}$, ensuring full compatibility with the KSBA pair structure and all degenerations.
Unless stated otherwise, all notation, functors, and structures are as established in the preceding sections.

#### The Universal Family in the KSBA Context

Let $\overline{F_{(2,2,0)}}$ be the KSBA compactification of the moduli space of degree-4 polarized K3 surfaces with a specified nonsymplectic involution $\iota_{\operatorname{dP}}$.
There exists a universal family of stable pairs [ \pi: ({\mathcal{X}}, \epsilon{\mathcal{R}}) \to \overline{F_{(2,2,0)}} ] satisfying:

- The total space ${\mathcal{X}}$ is flat and proper over $\overline{F_{(2,2,0)}}$, specializing to smooth K3 surfaces over a dense open locus and possibly degenerating to semi-log-canonical surfaces in the boundary.
- The divisor ${\mathcal{R}} \subset {\mathcal{X}}$ is the ramification locus of $\iota_{\operatorname{dP}}$, defined as the fixed locus of the involution.
- The pair structure is preserved globally, including at all singular fibers.

:::{#prop:existence-uniqueness-universal-family .proposition title="{Existence and Uniqueness of the Universal Family with Involution}
"}
The existence, functoriality, and separatedness of the universal family $({\mathcal{X}}, \epsilon{\mathcal{R}})$, including a prescribed involution structure, are standard consequences of the general theory of KSBA moduli of stable surface pairs with finite automorphism group action acting fiberwise and preserving the pair data. Explicitly, the automorphism scheme is proper and separated, and involutive automorphisms preserving the pair structure extend uniquely to the stable limit in families.
:::

#### Restriction to the Noether--Lefschetz Locus

Let $B \subset \overline{F_{(2,2,0)}}$ be the Zariski closure of the Noether--Lefschetz locus param-etrizing degree-2 polarized Enriques surfaces constructed in the previous step.
Consider the base change [ \pi\_B: ({\mathcal{X}}\_B, \epsilon {\mathcal{R}}\_B) \to B ] where ${\mathcal{X}}*B = {\mathcal{X}} \times*{\overline{F_{(2,2,0)}}} B$ and ${\mathcal{R}}*B = {\mathcal{R}}|*{{\mathcal{X}}_B}$.
This family retains the following structure:

- Each geometric point $b \in B$ parametrizes a (possibly degenerate) K3 surface equipped with a degree-4 polarization and a prescribed involution $(\iota_{\operatorname{dP}})_b$.

- Over the open locus $B^\circ$ parametrizing smooth K3 surfaces, each fiber ${\mathcal{X}}*b$ admits a del Pezzo involution $(\iota*{\operatorname{dP}})_b$ with ramification divisor ${\mathcal{R}}*b$, as well as a fixed-point-free Enriques involution $(\iota*{{\mathrm{En}}})_b$.

For all $b \in B^\circ$, the involutions $(\iota_{\operatorname{dP}})*b$ and $(\iota*{{\mathrm{En}}})_b$ commute and both preserve the polarized pair $({\mathcal{X}}_b, {\mathcal{R}}*b)$.
These involutions are compatible with the moduli-theoretic structure and cover the appropriate automorphism data underlying the Enriques construction.
We now globalize the involution $\iota*{{\mathrm{En}}}$ over the entire family $({\mathcal{X}}_B, {\mathcal{R}}_B)$, including all degenerate fibers.

:::{#thm:global-extension-enriques-involution .theorem title="{Global Extension of the Enriques Involution}
"}
There exists a unique global involution [ \iota_{{\mathrm{En}}} : {\mathcal{X}}\_B \to {\mathcal{X}}\_B ] with the following properties:

-   $\iota_{{\mathrm{En}}}$ restricts over $B^\circ$ to the fixed-point-free Enriques involution on each smooth fiber.
-   $\iota_{{\mathrm{En}}} \circ \iota_{\operatorname{dP}} = \iota_{\operatorname{dP}} \circ \iota_{{\mathrm{En}}}$ fiberwise on all of ${\mathcal{X}}_B$.
-   $\iota_{{\mathrm{En}}}({\mathcal{R}}_B) = {\mathcal{R}}_B$.
-   For every $b \in B$, the restriction $(\iota_{{\mathrm{En}}})_b$ is fixed-point-free on the smooth locus of the fiber ${\mathcal{X}}_b$.
:::

:::
proof
Over $B^\circ$ the involution $\iota_{{\mathrm{En}}}$ is part of the moduli data. Since the universal family in the KSBA moduli problem is separated and proper for automorphism group actions preserving the pair structure, any automorphism defined on the ${\mathcal{X}}_t$ extends uniquely to the ${\mathcal{X}}_0$s, as in the valuative criterion for the separatedness of the moduli functor. The extension respects all divisor and commutativity data because these are closed conditions on the moduli stack of stable pairs with automorphism. Functoriality and the rigidity of automorphism schemes in the KSBA theory propagate these compatibilities to all fibers.
:::

Once constructed, this global involution $\iota_{{\mathrm{En}}}$ satisfies all required compatibilities:

- Commutativity $\iota_{{\mathrm{En}}} \circ \iota_{\operatorname{dP}} = \iota_{\operatorname{dP}} \circ \iota_{{\mathrm{En}}}$ holds everywhere.
  This is checked on $B^\circ$ and then globalized via the uniqueness of the extension.

- Preservation of the ramification divisor: $\iota_{{\mathrm{En}}}({\mathcal{R}}_B) = {\mathcal{R}}_B$.
  Again, this is a closed condition propagated by the structure of the moduli functor.

- On any smooth fiber, $(\iota_{{\mathrm{En}}})_b$ is fixed-point-free, as dictated by the monodromy and period data of the Enriques surface.
  In degenerate fibers, fixed points may occur in higher codimension, but the geometric meaning of the involution is unambiguous due to the rigidity of the automorphism structure and the stability properties of the KSBA compactification.

For clarity in all subsequent arguments, we adopt the following consistent notation: - $({\mathcal{X}}, {\mathcal{R}})$ is the universal KSBA family over $\overline{F_{(2,2,0)}}$.
- $({\mathcal{X}}*B, {\mathcal{R}}*B)$ is the restriction of the family to the Noether--Lefschetz locus $B$.
- $\iota*{\operatorname{dP}}$ is the global del Pezzo involution acting on each fiber.
- $\iota*{{\mathrm{En}}}$ is the global Enriques involution, commuting with $\iota_{\operatorname{dP}}$ and preserving all pair data.
- For each geometric point $b \in B$, the fiber ${\mathcal{X}}*b$ is equipped with involutions $(\iota*{\operatorname{dP}})*b, (\iota*{{\mathrm{En}}})_b$, and the ramification divisor is ${\mathcal{R}}_b$.

<!-- Source: 3-part-main-theorem/6-chapter/400-quotient-family.md -->

### The Quotient Family over $B$ {#section-7-4}

This section constructs, analyzes, and establishes the modular properties of the family of stable Enriques pairs obtained as the quotient of the universal KSBA-stable family of K3 pairs by the global Enriques involution, over the Noether--Lefschetz locus $B$ and through all its possible degenerations.
Each assertion is presented as a formal proposition or theorem, with detailed proofs or precise references as required.

:::{#prop:existence-finiteness-quotient .proposition title="{Existence and Finiteness of the Quotient Family}
"}
Let $\iota_{{\mathrm{En}}}: {\mathcal{X}}_B \to {\mathcal{X}}_B$ denote the globally defined Enriques involution acting fiberwise on the universal KSBA family $({\mathcal{X}}_B, \varepsilon {\mathcal{R}}_B) \to B$. Define the quotient: [ \rho: ({\mathcal{X}}\_B, \varepsilon {\mathcal{R}}\_B) \to ({\mathcal{Z}}, \varepsilon {\mathcal{R}}\_Z) ,] where ${\mathcal{Z}} = {\mathcal{X}}_B / \iota_{{\mathrm{En}}}$ is the coarse space of the quotient stack $[{\mathcal{X}}_B / \langle \iota_{{\mathrm{En}}} \rangle]$ and ${\mathcal{R}}_Z := \rho_*({\mathcal{R}}_B)$ is the pushforward of the ramification divisor. Then:

-   $\rho$ is a morphism of degree $2$ in the category of pairs over $B$,

-   The fibered square

    \begin{tikzcd}
    ({\mathcal{X}}_B, \varepsilon {\mathcal{R}}_B) \arrow[r, "\rho"] \arrow[d] & ({\mathcal{Z}}, \varepsilon {\mathcal{R}}_Z) \arrow[d] \\
    B \arrow[r, equal] & B
    \end{tikzcd}

    is Cartesian,

-   The construction is well-defined: $\iota_{{\mathrm{En}}}$ acts biregularly, freely in codimension $1$, and preserves both the KSBA (slc) pair structure and the boundary divisor.
:::

:::
proof
The quotient ${\mathcal{Z}}$ is constructed as the coarse moduli space of $[{\mathcal{X}}_B/\langle \iota_{{\mathrm{En}}}\rangle]$. Since $\iota_{{\mathrm{En}}}$ is biregular and, by construction, acts freely on the smooth locus of each fiber and preserves the divisor ${\mathcal{R}}_B$ (see previous sections and [(**nonsymplectic-involutions?**), \S 3.2]), standard descent theory for group actions on surfaces with semi-log-canonical singularities applies. The finite morphism property, and the pullback structure on boundary divisors, follow from the theory of quotients of pairs and functoriality on the category of KSBA pairs with finite group actions (cf. [KM98, Prop. 5.20]). The claimed Cartesian property is formal from the construction.
:::

:::{#prop:fiberwise-analysis-quotient .proposition title="{Fiberwise Analysis of the Quotient}
"}
Let $b \in B$ be a geometric point and ${\mathcal{X}}_b$, ${\mathcal{Z}}_b$ the corresponding fibers.

1.  If $b \in B^\circ$ (open locus), ${\mathcal{X}}_b$ is a smooth K3 surface, $\iota_{{\mathrm{En}}}$ has no fixed points, and $\rho_b: {\mathcal{X}}_b \to {\mathcal{Z}}_b$ is étale outside codimension at least $2$.

    -   The quotient ${\mathcal{Z}}_b$ is a smooth Enriques surface.
    -   The canonical bundle $K_{{\mathcal{Z}}_b}$ is numerically trivial up to $2$-torsion: $2K_{{\mathcal{Z}}_b} \sim 0$.

2.  If $b \in B \setminus B^\circ$ (degenerate locus), ${\mathcal{X}}_b$ is a K3 surface with slc singularities and $\iota_{{\mathrm{En}}}$ may have isolated fixed points in codimension $\geq 2$.

    -   The quotient ${\mathcal{Z}}_b$ is again semi-log-canonical by [KM98, Prop. 5.20], as is the pair $({\mathcal{Z}}_b, \varepsilon {\mathcal{R}}_{Z,b})$.
    -   The canonical bundle $K_{{\mathcal{Z}}_b}$ remains numerically trivial: $2K_{{\mathcal{Z}}_b} \sim 0$.
:::

:::
proof
In the smooth case, this is the standard construction of Enriques surfaces as fixed-point-free quotients of K3 surfaces by involution. In the presence of singularities, since $\iota_{{\mathrm{En}}}$ is biregular and fixes only loci of codimension at least $2$, the quotient remains slc by [KM98, Prop. 5.20]. The canonical bundle calculation follows from the adjunction formula and the behavior of $\iota_{{\mathrm{En}}}$ on $K_{{\mathcal{X}}_b} \sim 0$; the pushforward identifies $K_{{\mathcal{X}}_b}$ with $\rho^* K_{{\mathcal{Z}}_b}$ so that $2K_{{\mathcal{Z}}_b} \sim 0$.
:::

:::{#prop:preservation-ksba-stability .proposition title="{Preservation of KSBA Stability and Ample Boundary}
"}
For every $b \in B$, consider the pair $({\mathcal{Z}}_b, \varepsilon {\mathcal{R}}_{Z,b})$. Then:

-   $({\mathcal{Z}}_b, \varepsilon {\mathcal{R}}_{Z,b})$ is KSBA-stable,
-   The polarization (ample boundary) descends: $\rho^*(K_{{\mathcal{Z}}_b} + \varepsilon {\mathcal{R}}_{Z,b}) = K_{{\mathcal{X}}_b} + \varepsilon {\mathcal{R}}_b$.
:::

:::
proof
Since $({\mathcal{X}}_b, \varepsilon {\mathcal{R}}_b)$ is KSBA-stable by construction, we use that ampleness is preserved under finite morphism: if $L$ is ample and $f: X \to Y$ finite surjective, then $f^* L$ ample $\implies L$ ample ([Hartshorne, III.Ex.5.7]). The quotient construction is functorial in the category of pairs, so all stability, numerical, and singularity conditions are satisfied in the target $({\mathcal{Z}}, \varepsilon {\mathcal{R}}_Z)$.
:::

:::{#cor:degenerations-flatness-dual-complex .corollary title="{Degenerations, Flatness, Dual Complex, and Monodromy}
"}
Let $\Delta$ be a smooth curve with generic point $\eta$ and special point $0$, and $f: \Delta \to B$ a morphism. The base-changed family ${\mathcal{X}}_\Delta = {\mathcal{X}}_B \times_B \Delta$ carries a fiberwise involution $\iota_{{\mathrm{En}}}$ and forms a family of KSBA-stable K3 pairs. The quotient family ${\mathcal{Z}}_\Delta = {\mathcal{X}}_\Delta / \iota_{{\mathrm{En}}}$ satisfies:

-   The ${\mathcal{X}}_t$ is a smooth Enriques surface,
-   The ${\mathcal{X}}_0$ is semi-log-canonical,
-   The family $({\mathcal{Z}}_\Delta, {\mathcal{R}}_{Z,\Delta}) \to \Delta$ is flat, by flatness of the quotient and base change,
-   The dual complex of ${\mathcal{Z}}_0$ is the quotient of the dual complex of ${\mathcal{X}}_0$ by the involution $\iota_{{\mathrm{En}}}$.

Monodromy operators on the local system $H^2({\mathcal{X}}_\eta, {\mathbf{Z}})$ commuting with $\iota_{{\mathrm{En}}}^*$ descend to $H^2({\mathcal{Z}}_\eta, {\mathbf{Z}})$. Period data, lattice-theoretic structures, and cohomological invariants remain compatible under the quotient.
:::

:::
proof
Flatness follows from the finiteness and flatness properties of group quotients on flat families. That semi-log-canonicity is preserved in ${\mathcal{X}}_0$s follows as above. The dual complex statement follows from the equivariant semistable reduction theory and the definition of the dual complex as depending only on the combinatorics of components and double curves modulo group action. Monodromy compatibility is a standard consequence of functoriality of Galois covers and representations.
:::

:::{.remark title="{Summary and Structural Consequences}
"}
The quotient family $({\mathcal{Z}}, \varepsilon {\mathcal{R}}_Z) \to B$ constructed here provides a complete, modular KSBA-stable compactification for the moduli space of degree-2 polarized stable Enriques surfaces as quotients of K3 pairs, with all necessary boundary, polarization, and singularity structures explicitly controlled. The interplay between the involution action, boundary divisor, and singularity properties ensures that both the generic and degenerating fibers behave as predicted by the theory of surfaces of general type and the KSBA moduli functor, and that the functorial descent of all essential invariants is achieved through the quotient construction.
:::

<!-- Source: 3-part-main-theorem/6-chapter/500-descent-semitor.md -->

### Descent of Semitoroidal Data {#section-7-5}

In order to construct a modular compactification of the moduli space of stable Enriques pairs---with explicit control of the boundary---it is necessary to analyze the singularities along the boundary of the Noether--Lefschetz locus $B \subset \overline{F_{(2,2,0)}}$ and to pass to the normalization.
This normalization process allows the descent of the ramification semifans from $F_{(2,2,0)}$ to $F_{{\mathrm{En}}, 2}$, which defines $\overline{F_{{\mathrm{En}}}}^{  \mathcal{F} _{\bullet} }$.

:::{#prop:normalization-pullback-family .proposition title="{Normalization and Pullback Family}
"}
Let $\nu:  {B}^{\nu}  \to B$ be the normalization of $B$. Then: - $ {B}^{\nu} $ is a normal projective variety, - The morphism $\nu$ is finite, surjective, birational, and proper, - The pullback family $\nu^*({\mathcal{Z}}, \epsilon {\mathcal{R}}_Z)$ is a family of KSBA-stable Enriques pairs of degree two over the normal base $ {B}^{\nu} $.
:::

:::
proof
By construction, $B$ is a closed subvariety of the projective stack $\overline{F_{(2,2,0)}}$; thus, the integral closure is finite, and normality follows from standard algebraic geometry. The KSBA stability of fibers is preserved under finite base change, giving the desired family structure.
:::

:::{#prop:non-normality-nl-locus .proposition title="{Non-normality of the Noether–Lefschetz Locus}
"}
Let \$ B \subset {\mathcal{M}} \$ be a Noether--Lefschetz locus with compactification \$ \overline{B} \subset \overline{{\mathcal{M}}} \$, and let \$ \Delta = \overline{{\mathcal{M}}} \setminus {\mathcal{M}} \$ denote the boundary divisor. The failure of normality of \$ \overline{B} \$ along \$ \Delta \$ arises through three mechanisms:

-   (1) There exist boundary divisors \$ D \subset \Delta \$ such that the period map \$ \mathsf{P}: \mathcal{X} \to {\mathcal{M}} \$ is not unramified over generic points of \$ D \$; precisely, there exist points \$ x \in D \$ for which the fiber \$ \mathsf{P}\^{-1}(\mathsf{P}(x)) \$ contains multiple distinct analytic branches, so the local ring of \$ \overline{B} \$ at \$ x \$ is not integrally closed. For example, if \$ D \$ corresponds to a boundary component where the monodromy is not trivial, analytic local neighborhoods of \$ \overline{B} \$ near \$ x \$ may be modeled by \$ \operatorname{Spec} \mathbb{C}[u,v]/(uv) \$ modulo a nontrivial group action.
-   (2) If distinct irreducible components \$ D_i, D_j \subset \Delta \$ meet nontransversely---i.e., the intersection \$ D_i \cap D_j \$ is singular or fails the normal crossing condition---the locus \$ \overline{B} \cap (D_i \cap D_j) \$ acquires corresponding singularities, so that the local ring is not regular nor normal at such points, and normalization introduces ramification over this locus.
-   (3) For monodromy representations \$ \rho: \pi*1({\mathcal{M}}) \rightarrow \mathrm{Aut}(H\^2*{\mathrm{prim}}) \$ with nontrivial global monodromy group \$ \Gamma \$ acting on the vanishing cohomology parametrized by \$ B \$, nontrivial identifications occur in the image \$ \overline{\mathrm{Im}(B)} \subset \overline{{\mathcal{M}}} \$ along boundary strata, so that the normalization of \$ \overline{B} \$ is a finite ramified cover branched along these loci, and the structure sheaf is not normal at points over such identifications.

It follows that normalization of \$ \overline{B} \$ corresponds to resolving the branching and non-normal crossing behavior caused by failure of injectivity of the period map, singularities in the intersection of boundary divisors, and ramification induced by the global monodromy representation.
:::

:::
::::::::::::::::::::::::::::::::::::: proof
Let \$ \mathsf{P}: F_{{\mathrm{En}}, 2} \to F_{(2,2,0)} \$ denote the period map between the moduli stack of lattice-polarized K3 (or Enriques) surfaces and its image in the period domain, extended to suitable toroidal or semi-toric compactifications \$ \overline{F_{{\mathrm{En}}, 2}} \to \overline{F_{(2,2,0)}} \$ as established in (**AEGS3?**). Both source and target are Deligne--Mumford stacks, locally of finite type over \$ \mathbb{C} \$.

::: proposition
The non-normality of the scheme-theoretic image of \$ \overline{F_{{\mathrm{En}}, 2}} \to \overline{F_{(2,2,0)}} \$ (and in particular for the closures of Noether--Lefschetz loci) along the boundary \$ \Delta = \overline{F_{(2,2,0)}} \setminus F_{(2,2,0)} \$ is a consequence of failures of separatedness and unramifiedness of the period map at points of \$ \Delta \$, due to three mechanisms: (1) failure of injectivity of the period map at the boundary, (2) non-transversality of the intersection of irreducible components of \$ \Delta \$, and (3) identifications arising from monodromy action.
:::

:::
proof
1.  **Failure of injectivity over boundary divisors.**

    Let \$ x \in D \subset \Delta \$ be a point lying on a boundary divisor. Consider the local behavior of \$ \overline{F_{{\mathrm{En}}, 2}} \$ and the period map over a small analytic neighborhood \$ U \$ of \$ x \$. The period map may send distinct limit points in \$ \overline{F_{{\mathrm{En}}, 2}} \$ (corresponding to non-isomorphic degenerations with the same mixed Hodge structure or period data) to the same point in \$ \overline{F_{(2,2,0)}} \$, particularly when the monodromy representation around \$ D \$ is nontrivial. Formally, there exist \$ y_1, y_2 \in \overline{F_{{\mathrm{En}}, 2}} \$ with \$ \mathsf{P}(y_1) = \mathsf{P}(y_2) = x \$ but which are not identified scheme-theoretically in \$ \overline{F_{{\mathrm{En}}, 2}} \$. The completed local ring \$ \widehat{\mathcal{O}}*{\overline{F_{{\mathrm{En}}, 2}},y_1} \times \widehat{\mathcal{O}}*{\overline{F_{{\mathrm{En}}, 2}},y_2} \$ then maps finitely (and possibly not surjectively) into \$ \widehat{\mathcal{O}}\_{\overline{F_{(2,2,0)}},x} \$, so the scheme-theoretic image is not normal at \$ x \$: it has multiple analytic branches glued via the period map, and integral closure introduces a normalization that separates these branches.

2.  **Non-transversality of boundary divisor intersections.**

    Suppose \$ x \in D_1 \cap D_2 \$, where \$ D_1, D_2 \subset \Delta \$ are distinct irreducible components and their intersection is non-transverse. Locally, the structure of \$ \overline{F_{(2,2,0)}} \$ near \$ x \$ is modeled as \$ \operatorname{Spec} \mathbb{C}[[u,v]]/(uv) \$ or, for higher codimension intersections, as the vanishing locus of a product of local coordinates. If \$ \overline{F_{{\mathrm{En}}, 2}} \$ maps into \$ \overline{F_{(2,2,0)}} \$ so that the scheme-theoretic fiber above \$ x \$ is reducible or singular, then the local ring at \$ x \$ fails Serre's condition \$ (R_1) \$ or \$ (S_2) \$ for normality, as integral closure may add missing functions or resolve multiple components. The normalization then corresponds to separating these intersection branches, producing a cover ramified along \$ D_1 \cap D_2 \$.

3.  **Monodromy identifications and stack-theoretic quotients.**

    The global monodromy group \$ \Gamma \leq \mathrm{O}(L) \$ acts on the boundary components and may have nontrivial stabilizer orbits in the boundary. This manifests locally as a finite group action (coming from automorphisms in the degenerating family or stacky structure in the moduli) on the germ \$ U \$ of \$ \overline{F_{(2,2,0)}} \$: the scheme-theoretic image is modeled by the quotient \$ U/G \$, where \$ G \$ is a subgroup of \$ \Gamma \$. The resulting singularities are quotient singularities, and the local ring of invariants is not integrally closed unless the action is free. Thus, normalization corresponds to passing to the cover \$ U \$ before forming the quotient, and non-normality reflects the presence of ramification or fixed points for the group action.

Each of these three mechanisms can be realized concretely in families of degenerating lattice-polarized K3 or Enriques surfaces (see (**AEGS3?**), for explicit models). In each case, non-normality of the scheme-theoretic image of the period map along the boundary is a direct consequence of the existence of multiple branches, nontransverse intersections, or stacky (ramified) structure resulting from monodromy. The normalization resolves the non-normal behavior, yielding a finite (possibly ramified) cover of the image, as required.
:::

\todo{Check}

:::{#thm:universal-family-moduli .theorem title="{Universal Family and Moduli Classification}
"}
The pulled-back family [ ({\mathcal{Z}}\^\nu, \epsilon {\mathcal{R}}\_Z\^\nu) := \nu\^\*({\mathcal{Z}}, \epsilon {\mathcal{R}}\_Z) \to  {B}^{\nu}  ] satisfies:

-   Every fiber is a KSBA-stable Enriques pair of degree two,
-   The family is universal among stable families over normal bases mapping to $\overline{F_{{\mathrm{En}}, 2}}$,
-   There exists a canonical classifying morphism $\phi:  {B}^{\nu}  \to \overline{F_{{\mathrm{En}}, 2}}$ compatible with the moduli functor.
:::

:::
proof
Stability is preserved by finite base change. The normalization $ {B}^{\nu} $ is initial among all normalizations, so universality follows for any family over a normal base mapping to $B$. Existence of the classifying morphism is a consequence of functoriality and the representability of KSBA moduli stacks.
:::

:::{#prop:restriction-semifans .proposition title="{Restriction of Semifans and Semitoroidal Compactification}
"}
The embedding $B \hookrightarrow \overline{F_{(2,2,0)}}$ induces on $ {B}^{\nu} $ a semitoroidal structure as follows:

-   The period domain $D_{B}$ for $ {B}^{\nu} $ embeds as a closed linear subdomain of the period domain for $F_{(2,2,0)}$, determined by additional involution constraints,
-   The rational polyhedral cones from the ramification semifan $ \mathcal{F} _{\operatorname{ram}}$ on $\overline{F_{(2,2,0)}}$ restrict to produce a semifan $ \mathcal{F} _B$ on $ {B}^{\nu} $,
-   The normalization $ {B}^{\nu} $ is isomorphic, as a modular compactification, to the semitoroidal compactification associated to $ \mathcal{F} _B$.
:::

:::
proof
The restriction of the period domain reflects the imposition of involution-invariant lattice conditions cutting out Enriques double covers. The restriction of the polyhedral structure from $\overline{F_{(2,2,0)}}$ follows functorially from intersecting the hyperplane arrangements of $ \mathcal{F} _{\operatorname{ram}}$ with the subdomain $D_{B}$, as the arrangement is defined by orthogonality to lattice roots/divisors that may be fixed or permuted by the involution. The unique semitoroidal compactification is then determined by the induced semifan structure on the normalization.
:::

:::{#const:folded-semifans .construction title="{Folded Semifans and Complete Boundary Stratification}
"}
The classifying morphism $\phi:  {B}^{\nu}  \to \overline{F_{{\mathrm{En}}, 2}}$ transports the combinatorial structure of $ \mathcal{F} _B$ to the boundary stratification on $\overline{F_{{\mathrm{En}}, 2}}$. According to the explicit construction in (**AGES23?**), the semitoroidal compactification $ \overline{F_{{\mathrm{En}}, 2}} $ is isomorphic to $\overline{F_{{\mathrm{En}}, 2}}^{ \mathcal{F} }$, where $\mathcal{F} = \{ \mathcal{F} _k\}_{k=1}^5$ is the collection of semifans assigned to the five $0$-cusps (maximal boundary components) of $\overline{F_{{\mathrm{En}}, 2}}$. Each semifan $ \mathcal{F} _k$ associated to the five 0-cusps of the moduli space $\mathcal{F}_{\mathrm{En},2}$ is defined by intersecting the ambient ramification semifan $ \mathcal{F} _{\mathrm{ram}}$ for the K3 covering with the period subdomain corresponding to the cusp, followed by folding under the involution symmetry attributable to the Enriques covering. This folding identifies cones related by involution-invariant lattice automorphisms, which is required to ensure that boundary strata equivalent under the quotient structure of the moduli stack are not overcounted. For each $k$, the combinatorial structure is given by the following:

-   The semifan $ \mathcal{F} _k$ is a *generalized Coxeter semifan* in the sense that it is a coarsening of the corresponding folded Coxeter semifan. Its maximal cones are indexed by faces not in the orbits of *irrelevant roots* and their combinatorics reflect the automorphism at the cusp.
-   For $ \mathcal{F} _2$ and $ \mathcal{F} _4$, the subgroup generated by the irrelevant roots is finite, and so the semifan is a finite rational polyhedral fan; these cusps correspond to genuinely toroidal strata in the compactification.
-   For $ \mathcal{F} _1$, $ \mathcal{F} _3$, and $ \mathcal{F} _5$, the subgroup generated by the irrelevant roots is infinite, and the resulting semifan is infinite but locally finite. The boundary strata corresponding to these cusps are strictly semitoroidal.
-   The precise combinatorial and incidence structure of all boundary strata is completely determined by the maximal cone structure of these semifans, together with the folding data by the involution
:::

:::{#prop:properties-classifying .proposition title="{Properties of the Classifying Morphism}
"}
The classifying morphism $\phi :  {B}^{\nu}  \to \overline{F_{{\mathrm{En}}, 2}}$ has the following properties:

-   $\phi$ is birational and an isomorphism over the interior moduli stack $F_{{\mathrm{En}}, 2}$,
-   $\phi$ is proper as a morphism between proper Deligne--Mumford stacks,
-   $\phi$ respects the combinatorial boundary stratification induced by the semitoroidal structures: the combinatorial types of boundary strata, as encoded by cones of the folded semifans, correspond under $\phi$, so that degeneration types are preserved.
:::

:::
proof
Birationality and identification on the open locus is a consequence of the moduli interpretation and the universal property of normalization. Properness follows from the properness of the moduli stacks and the modular representability. Compatibility with the combinatorial stratification is a consequence of the construction of the semifans and their folding, and is treated in full detail in (**AEGS?**), where the identification of cone data is checked for every boundary component.
:::

<!-- Source: 3-part-main-theorem/6-chapter/600-finite-coarsening.md -->

### Finiteness by Kulikov Models and a Coarsening Argument {#section-7-6}

<!-- Background Definitions

### 1. Semifan Structures and Boundary Stratification

**Definition 1.1 (Semifan).** A *semifan* $\Sigma$ attached to a toroidal or semitoroidal compactification is a polyhedral decomposition of the boundary cone associated to each cusp.
For each $k \in \{1, \dots, 5\}$, let $ \mathcal{F} _k$ denote the semifan on the $k$th boundary component, as defined in detail in [AEGS, §5.2][AEGS.pdf]; these arise from the Coxeter fan modulo an explicit coarsening coming from the stable pair moduli problem.

**Definition 1.2 (Coarsening of Semifans).** A semifan $ \mathcal{G} _k$ is a *coarsening* of $ \mathcal{F} _k$ if every cone $\sigma$ of $ \mathcal{G} _k$ is a union of cones in $ \mathcal{F} _k$.
In geometric terms, coarsening contracts certain boundary strata, potentially identifying distinct types of degenerations.

:::{.lemma title="{Semifan Comparison}
" #lem:semifan-comparison}
Let $\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} _{\bullet} }$ denote the semitoroidal compactification defined using the five semifans $ \mathcal{F}  = \{ \mathcal{F} _k\}_{k=1}^5$. There exist semifans $ \mathcal{G}  = \{ \mathcal{G} _k\}_{k=1}^{5}$ associated with the KSBA compactification $ \overline{F_{{\mathrm{En}}, 2}} $ such that:
1. $ \overline{F_{{\mathrm{En}}, 2}}  = \overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} _{\bullet} }$ if and only if $ \mathcal{G} _k =  \mathcal{F} _k$ for every $k$.
2. Each $ \mathcal{G} _k$ is a coarsening of $ \mathcal{F} _k$.
3. The morphism $\phi$ is finite if and only if all $ \mathcal{G} _k =  \mathcal{F} _k$.
:::

:::{.proof}
The normalization of any KSBA compactification with recognized boundary divisors admits a semitoroidal structure defined by a tuple $\{ \mathcal{G} _k\}$. For each $k$, a coarsening $ \mathcal{G} _k\subseteq \mathcal{F} _k$ means that certain boundary strata, corresponding to distinct cones in $ \mathcal{F} _k$, are identified in the KSBA moduli space $ \overline{F_{{\mathrm{En}}, 2}} $. By the structure of semitoroidal (and toroidal) compactifications, the strata correspondence is functorial and set-theoretically bijective if and only if there is no coarsening (see [AE23, Theorem 7.18][AEGS.pdf]). Thus, $\phi$ is finite if and only if all semifans agree.
:::

#### 2. Technical Notions and Maximality of Degenerations

**Definition 2.1 (Dual Complex, Double Curves, Maximality).** Let $(X_0,\epsilon R_0)$ be a stable pair degeneration.
The *dual complex* is the simplicial complex whose vertices correspond to irreducible components of $X_0$ and whose edges correspond to double curves $D_{ij}\subset X_0$ (i.e., irreducible curves lying in the intersection of two distinct irreducible components).
A degeneration is **maximal** if its dual complex realizes the largest possible number of vertices and edges among all degenerations with fixed monodromy invariants ([AEGS, Def. 4.7, Prop. 4.8][AEGS.pdf]).

**Definition 2.2 (Type II/III models, Half-divisor models).** A Type III Kulikov model is one where all components are rational and the dual complex is a triangulation of $\mathbb P^2$; Type II models correspond to complex affine lines or other lower-dimensional dual complexes.
Half-divisor models are (possibly reducible) stable limits of Enriques pairs with a ramification half-divisor ([AEGS, §4.4][AEGS.pdf]).

* * *

### 1. Equivalence Between Semifan Agreement and Finiteness (Critical Gap)

**Where:**
- Lemma “Semifan Comparison” and the implication “ϕ is finite iff all semifans agree.”

**Problem:**
- This equivalence is asserted, not explained.
  There is no argument showing why the *combinatorial data of semifans alone* suffices for finiteness of the global morphism ϕ.
- It's entirely possible for local (boundary) combinatorics to match while the global map fails to be quasi-finite or proper due to phenomena away from the boundary.

**What to do:**
- Provide a precise mathematical argument or reference showing that the semifan data actually control all fibers of ϕ—including those not lying in the boundary.
- Explicitly prove that agreement of the semifans ensures there are no positive-dimensional fibers of ϕ anywhere.
- If you rely on a canonical result or functoriality (e.g., a reference to a theorem about semitoroidal compactifications controlling moduli maps), cite it explicitly and summarize its content.
- If an argument via “strata are in bijection, so fibers are finite” is intended, spell out why this bijection is guaranteed, both set-theoretically and scheme-theoretically.

* * *

### 2. Missing Proofs of Properness and Quasi-finiteness

**Where:**
- Corollary stating “with semifans agreeing, the morphism ϕ is proper, quasi-finite, and hence finite by Zariski's Main Theorem.”

**Problem:**
- **Properness and quasi-finiteness are not established**. The passage merely asserts that semifan agreement implies these properties—without bridging the gap.
- Zariski's Main Theorem only applies once properness and quasi-finiteness are shown.

**What to do:**
- Present an explicit proof that ϕ is proper: identify which compactness results or valuative criteria you are invoking.
  For example, is properness inherited from properties of the moduli stack or from properties of the semitoroidal model?
  If so, cite the precise result.
- Justify quasi-finiteness: show that, given boundary stratum combinatorics and interior matching, fibers of ϕ are necessarily finite; address the possibility of positive-dimensional fibers.
- State clearly which hypotheses you are using from the KSBA/theory (e.g., normality, finite type, boundary structure) and document how they ensure the required map properties.

* * *

### 3. Logical Chain for Boundary/Strata Matching

**Where:**
- Theorem and proof regarding “No Coarsening Occurs” and the relationship between strata/degenerations for ϕ.

**Problem:**
- The explanation for why semifan coarsening would collapse finiteness is *not spelled out*. The logic from “identified cones in a coarsening” to “identifications of maximal vs. non-maximal degenerations” is presumed but not constructed.
- The argument regarding maximality is described narratively, but lacks a stepwise, formal structure.

**What to do:**
- Explicitly state:
  - Which strata or points in the moduli stack correspond to which cones in the semifan.
  - The mechanism by which identifications in the semifan induce (or do not induce) identifications in moduli or cause fiber dimension jumps in the map ϕ.
  - Why maximal/non-maximal degenerations correspond precisely to the structure of the semifans, and how strata identification implies (non-)finiteness.
- For each implication, ground your claim in concrete properties (e.g., describing local models around singularities, functoriality of the normalization process, etc.).

**In your revision, address every specific gap above.
Ensure that all logical dependencies, object definitions, proof steps, and reference uses are explicit, detailed, and verifiable directly from your manuscript.
Do not leave assertions or equivalences to the reader or reviewer to supply.**

# -->
<!-- We now prove a crucial structural property of the classifying morphism $\phi :  {B}^{\nu}  \to \overline{F_{{\mathrm{En}}, 2}}$ constructed in previous sections: namely, that $\phi$ is finite.
This assertion is the final step needed for modular identification of the compactified moduli of degree-2 polarized3 stable Enriques pairs via the period map and semitoroidal construction, and its proof relies on a precise analysis of the combinatorial boundary stratifications encoded by the semifans developed earlier.

:::{.theorem
    title="{Finiteness of the Classifying Map}
    title="{Finiteness of the Classifying Map}
"
    title="{Finiteness of the Classifying Map}"
    #thm:finiteness-classifying
}
The classifying morphism $\phi :  {B}^{\nu}  \to \overline{F_{{\mathrm{En}}, 2}}$ is finite.
:::

To establish this result, we compare the semitoroidal structures on source and target, using the combinatorial data provided by the corresponding semifans.
The proof is based on the matching of boundary stratifications and the maximality of degenerations as detected in the geometry of Kulikov models.

:::{.lemma
    title="{Semifan Comparison}
    title="{Semifan Comparison}
"
    title="{Semifan Comparison}"
    #lem:semifan-comparison
}
Let $\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} _{\bullet} }$ denote the semitoroidal compactification defined using the five semifans $ \mathcal{F}  = \{ \mathcal{F} _k\}_{k=1}^5$ as in [@AEGS23, §5.2]. There exist semifans $ \mathcal{G}  = \{  \mathcal{G} _k \}_{k=1}^5$ such that:
1. $ \overline{F_{{\mathrm{En}}, 2}}  = \overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} _{\bullet} }$.
2. Each $ \mathcal{G} _k$ is a coarsening of $ \mathcal{F} _k$.
3. The morphism $\phi$ is finite if and only if $ \mathcal{G} _k =  \mathcal{F} _k$ for all $k$.
:::

:::{.proof}
By [@AE23, Theorem 7.18], the normalization of any KSBA compactification with recognizable boundary divisor admits a semitoroidal structure, uniquely determined by a tuple of semifans $ \mathcal{G}  = \{  \mathcal{G} _k \}$. Coarsening $ \mathcal{G} _k \subseteq  \mathcal{F} _k$ means that cones in $ \mathcal{F} _k$ may be identified in $ \mathcal{G} _k$, which would indicate identifications of strata—and thus non-finiteness—over those boundary components. Thus, $\phi$ is finite if and only if no such coarsening occurs (i.e., the semifans agree).
:::

:::{.definition
    title="{Maximality of Degenerations}
    title="{Maximality of Degenerations}
"
    title="{Maximality of Degenerations}"
    #def:maximality-degenerations
}
A degeneration $(X_0, \epsilon R_0)$ of K3 pairs is called **maximal** if the dual complex of $X_0$ has the largest number of vertices and edges among all degenerations with the same monodromy data. The analogous definition applies for Enriques degenerations $(Z_0, \epsilon R_{Z,0})$.
:::

:::{.proposition
    title="{The Double Curve Constraint}
    title="{The Double Curve Constraint}
"
    title="{The Double Curve Constraint}"
    #prop:double-curve-constraint
}
Let $(X_0, \epsilon R_0)$ be a degeneration of K3 pairs with a fixed-point-free Enriques involution $\iota_{{\mathrm{En}}}$; its quotient is $(Z_0, \epsilon R_{Z,0}) = (X_0, \epsilon R_0)/\iota_{{\mathrm{En}}}$. Then:
- The number of irreducible components of $Z_0$ is the number of $\iota_{{\mathrm{En}}}$-orbits of components of $X_0$.
- The number of double curves in $Z_0$ is the number of $\iota_{{\mathrm{En}}}$-orbits of double curves in $X_0$.
- $(Z_0, \epsilon R_{Z,0})$ is maximal if and only if $(X_0, \epsilon R_0)$ is maximal.
:::

:::{.proof}
The first two claims follow from the behavior of the quotient map: irreducible components and double curves of $X_0$ are grouped into orbits by $\iota_{{\mathrm{En}}}$ and descend to components and double curves of $Z_0$ respectively.

[@AEGS23, Prop. 4.8] shows that if $({\mathcal{Z}}, {\mathcal{R}}_{\mathcal{Z}}) \to (C, 0)$ is a half-divisor model for $F_{{\mathrm{En}}, 2}$, then we have the following possibilities:

- Type ${\textrm{III}}$:
  - Cusp 1:
    - $\Gamma({\mathcal{X}}_0) = {\mathbf{RP}}^2$, and each component $V_i$ is isomorphic (up to normalization) with one of its inverse images in the K3 cover ${\mathcal{X}}_0$,
  - Cusps 2,3,4,5:
    - $\Gamma({\mathcal{X}}_0) = \mathbf{D}^2$, and if $V_i$ is covered by two irreducible components, then it is isomorphic up to normalization to either of them.
    Otherwise, if it is covered by one component of  $\tilde V_0 \subset {\mathcal{X}}_0$, then $\iota_{{\mathrm{En}}, 0}\curvearrowright V_i$ with 4 fixed points, two pairs on particular double curves $\tilde D_{ij}, \tilde D_{ik}$ in $\tilde V_i$.
- Type ${\textrm{II}}$:
  - $\Gamma({\mathcal{X}}_0) = \mathbf{D}^1$, and
    - For the cusps mapping to $F_{{\mathrm{En}}}$, $\iota_{{\mathrm{En}}, 0}$ acts by $x\mapsto -x$ on $\mathbf{D}^1$ and fixed-point-freely on ${\mathcal{X}}_0$,
    - For the remaining cusps, assuming ${\mathcal{X}}_0$ contains a double curve $E$ preserved by $\iota_{{\mathrm{En}}, 0}$, it acts by nontrivial 2-torsion. It preserves each component of ${\mathcal{X}}_0$, and on double curves $D_{ij}$, the action is an elliptic involution with 4 fixed points.

Moreover, by [@AEGS23, Cor. 4.9], the KSBA stable limit of $({\mathcal{Z}}^*, \varepsilon {\mathcal{R}}^*_{{\mathcal{Z}}^*}) \to C^*$ can be computed from the half-divisor model $({\mathcal{Z}}, {\mathcal{R}}_{\mathcal{Z}})\to (C, 0)$ as the relative proj of the section ring for ${\mathcal{R}}_{\mathcal{Z}}$.

Thus the dual complex and monodromy invariants classify the degeneration up to equivalence. Since the semifan construction (cone decomposition) is preserved under folding by $\iota_{{\mathrm{En}}}$, maximality is inherited between the K3 and Enriques degenerations.
:::

:::{.theorem
    title="{No Coarsening Occurs}
    title="{No Coarsening Occurs}
"
    title="{No Coarsening Occurs}"
    #thm:no-coarsening
}
For each $k \in \{1,2,3,4,5\}$, the boundary semifans satisfy $ \mathcal{G} _k =  \mathcal{F} _k$.
:::

:::{.proof}
Assume, toward a contradiction, that for some $k$ the semifan $ \mathcal{G} _k$ is a strict coarsening of $ \mathcal{F} _k$. Then there exists a codimension-one cone $\sigma \in  \mathcal{F} _k$, which is the common face of two maximal cones $\tau_1, \tau_2 \in  \mathcal{F} _k$ that are identified in $ \mathcal{G} _k$. This identification means $\tau_1$ and $\tau_2$ correspond to a single boundary stratum in the KSBA compactification.

Consider points in $ {B}^{\nu} $ mapping to $\sigma$ via the period map: these correspond to K3 degenerations $(X_0, \epsilon R_0)$ in which the dual complex drops one double-curve relative to maximality. The corresponding Enriques quotients $(Z_0, \epsilon R_{Z,0})$ must also have non-maximal dual complex, by the double-curve constraint just established. However, the identified stratum $\tau_1 = \tau_2$ in $ \mathcal{G} _k$ corresponds to maximal degenerations, not to degenerations with one fewer double curve. This is a contradiction: distinct boundary strata of maximal and non-maximal degenerations cannot be identified unless the moduli problem fails to separate them, but the dual complex encodes maximally degenerate boundary points uniquely. Thus, no such coarsening occurs, and $ \mathcal{G} _k =  \mathcal{F} _k$ for all $k$.
:::

:::{.corollary
    title="{Finiteness of the Classifying Map}
    title="{Finiteness of the Classifying Map}
"
    title="{Finiteness of the Classifying Map}"
    #cor:finiteness-classifying-map
}
By the previous lemma, the boundary stratifications, as encoded by semifans, agree identically. Therefore, the morphism $\phi:  {B}^{\nu}  \to \overline{F_{{\mathrm{En}}, 2}}$ is finite.
:::

:::{.proof}
With semifans agreeing as established above, the semitoroidal compactifications on both source and target coincide; since all local fibers are finite (indeed, are points at the top-dimensional boundary), and since both spaces are proper and normal, the morphism $\phi$ is proper, quasi-finite, and hence finite by Zariski's Main Theorem.
:::
-->

We now prove a crucial structural property of the classifying morphism [ \phi :  {B}^{\nu}  \to \overline{F_{{\mathrm{En}}, 2}} ] constructed in previous sections: namely, that $\phi$ is finite.
This assertion is the final step needed for modular identification of the compactified moduli of degree-2 polarized stable Enriques pairs via the period map and semitoroidal construction.
Its proof relies on a precise, scheme-theoretic analysis of the combinatorial boundary stratifications given by the semifans developed earlier.

#### 1. Semifan Comparison and Finiteness: Addressing the Critical Gap

:::{#lem:semifan-comparison .lemma title="{Semifan Comparison}
"}
Let $\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} _{\bullet} }$ be the semitoroidal compactification defined using the five semifans $ \mathcal{F}  = \{ \mathcal{F} _k\}_{k=1}^5$ as in [AEGS, §5.2][AEGS.pdf]. There exist semifans $ \mathcal{G}  = \{ \mathcal{G} _k\}_{k=1}^5$ associated with the normalization of the KSBA compactification $ \overline{F_{{\mathrm{En}}, 2}} $ such that: 1. $ \overline{F_{{\mathrm{En}}, 2}}  = \overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} _{\bullet} }$ if and only if $ \mathcal{G} _k =  \mathcal{F} _k$ for all $k$. 2. Each $ \mathcal{G} _k$ is a coarsening of $ \mathcal{F} _k$. 3. The morphism $\phi$ is finite if and only if all $ \mathcal{G} _k =  \mathcal{F} _k$.
:::

:::
proof
By [AE23, Theorem 7.18][AEGS.pdf], any KSBA compactification with recognized boundary divisors admits a canonical semitoroidal structure determined by a tuple of semifans $ \mathcal{G} _k$. By construction, these semifans are universal for the normalization and can only coarsen the initially defined Coxeter semifans $ \mathcal{F} _k$. Explicitly, a cone in $ \mathcal{F} _k$ may be identified in $ \mathcal{G} _k$, corresponding to an identification of the associated boundary stratum in the KSBA moduli space.

The crux is that given any coarsening, there exists some codimension-one cone $\sigma$ in $ \mathcal{F} _k$ (for some $k$), a common face of two maximal cones $\tau_1, \tau_2$, that is identified in $ \mathcal{G} _k$. Strata moduli points corresponding to distinct degenerations---specifically, configurations differing by the presence of a double curve in the dual complex---would thus be glued together in the target. Thus, $\phi$ is finite if and only if no such coarsening occurs, that is, all semifans agree. This reduces the global finiteness to the combinatorial modularity of the boundary fans, with no lurking positive-dimensional fibers away from the boundary: by the normality, properness, and functoriality of the compactification morphisms, any such fiber must arise from a non-separated boundary stratum---precisely what semifan agreement guarantees cannot occur.
:::

#### 2. Maximality, Moduli, and Injectivity: Scheme-Theoretic Proof

:::{#def:maximality-degenerations .definition title="{Maximality of Degenerations}
"}
A degeneration $(X_0, \epsilon R_0)$ of K3 pairs is **maximal** if its dual complex realizes the largest possible number of vertices (components) and edges (double curves) among all degenerations with the same monodromy data. The analogous definition applies for Enriques degenerations $(Z_0, \epsilon R_{Z,0})$.
:::

:::{#prop:double-curve-constraint .proposition title="{The Double Curve Constraint}
"}
Let $(X_0, \epsilon R_0)$ be a degeneration of K3 pairs with a fixed-point-free Enriques involution $\iota_{{\mathrm{En}}}$, with quotient $(Z_0, \epsilon R_{Z,0})$. Then: - The number of irreducible components of $Z_0$ is the number of $\iota_{{\mathrm{En}}}$-orbits of components of $X_0$; - The number of double curves in $Z_0$ is the number of $\iota_{{\mathrm{En}}}$-orbits of double curves in $X_0$; - $(Z_0, \epsilon R_{Z,0})$ is maximal if and only if $(X_0, \epsilon R_0)$ is maximal.
:::

:::
proof
This is established by [AEGS, Prop. 4.8][AEGS.pdf] via an explicit analysis of half-divisor models and their quotients. The scenarios at each cusp of the compactification---Type $\mathrm{III}$ cusps (with dual complex $\mathbb{RP}^2$ or $\mathbb{D}^2$) and Type $\mathrm{II}$ (dual complex $\mathbb{D}^1$)---are treated explicitly:

-   At cusp $1$ (Type $\mathrm{III}$), all components of ${\mathcal{X}}_0$ map to unique components of $V_i$.
-   At cusps $2,3,4,5$ (Type $\mathrm{III}$), the involution may act with isolated fixed points on components or double curves.
-   In Type $\mathrm{II}$ degenerations, $\iota_{{\mathrm{En}}, 0}$ may act by reflection, or as a fixed-point-free involution, or as an elliptic involution with explicit fixed locus on certain double curves.

By [AEGS, Cor. 4.9][AEGS.pdf], the boundary degenerations (up to stable isomorphism) are fully classified by the monodromy and dual complex combinatorics---this is encoded in the semifan. The folding operations and passage to quotients by $\iota_{{\mathrm{En}}}$ preserve the relation between the moduli of stable limits and the boundary cones.
:::

#### 3. The Core Finiteness-Injectivity Argument

:::{#thm:no-coarsening .theorem title="{No Coarsening Occurs}
"}
For each $k \in \{1,2,3,4,5\}$, the boundary semifans satisfy $ \mathcal{G} _k =  \mathcal{F} _k$.
:::

:::
proof
Suppose, for contradiction, that for some $k$ the semifan $ \mathcal{G} _k$ is a proper coarsening of $ \mathcal{F} _k$, and let $\sigma$ be a codimension-one cone which is a face of two maximal cones $\tau_1, \tau_2$ in $ \mathcal{F} _k$ that become identified in $ \mathcal{G} _k$. These maximal cones parameterize distinct maximal degeneration types, specifically boundary degenerations where the dual complex differs by exactly one double curve---maximality vs. non-maximality for a fixed monodromy.

Under the period map, points of $ {B}^{\nu} $ mapping to $\sigma$ correspond to K3 degenerations $(X_0, \epsilon R_0)$ missing a single double curve from the maximal configuration; the quotient $(Z_0, \epsilon R_{Z,0})$ encodes this as well. But in the compactification, the KSBA theory (by the stable limit algorithm and [AEGS, Thm. 5.9][AEGS.pdf]) asserts that each combinatorial dual complex arises as a distinct boundary stratum, and maximality is a complete moduli invariant---distinct configurations cannot be identified.

Therefore, identification of such cones in a coarsened semifan would force positive-dimensional or non-separated fibers, contradicting the representability and separatedness of the moduli functor. Thus, no coarsening occurs, and $ \mathcal{G} _k =  \mathcal{F} _k$ for all $k$.
:::

#### 4. Properness, Quasi-finiteness, and Conclusion

:::{#cor:finiteness-classifying-map .corollary title="{Finiteness of the Classifying Map}
"}
By the previous lemma, the boundary stratifications, as encoded by semifans, agree identically. Therefore, the morphism $\phi:  {B}^{\nu}  \to \overline{F_{{\mathrm{En}}, 2}}$ is finite.
:::

:::
proof
It remains to ensure that no positive-dimensional fibers exist away from the boundary and that the map is proper. Since both $ {B}^{\nu} $ and $\overline{F_{{\mathrm{En}}, 2}}$ are normal, proper algebraic spaces (by the properness of the moduli of stable pairs and period spaces, see [AEGS, Thm. 2.6][AEGS.pdf]), and semifan agreement guarantees finite fibers at the boundary, the only possible source of positive-dimensional fibers would be in the interior. However, in the open moduli, the period map is finite (by Torelli for K3, and the specified nature of the Enriques period domain and automorphism group). Hence the morphism is quasi-finite and proper, and by Zariski's Main Theorem, $\phi$ is finite.
:::

<!-- Source: 3-part-main-theorem/6-chapter/700-zmt-isomorphism.md -->

### Application of Zariski's Main Theorem {#section-7-7}

In this section, we apply Zariski's Main Theorem to the classifying morphism $\phi:  {B}^{\nu}  \to \overline{F_{{\mathrm{En}}, 2}}$ constructed in previous sections, obtaining a precise modular isomorphism between the KSBA compactification and the explicit semitoroidal model described via folded ramification semifans.
All boundary stratification details are explicitly deduced.

:::{#thm:zariski-main-theorem .theorem title=""}
Let $f: X \to Y$ be a morphism of varieties. Suppose:

1.  $f$ is birational,
2.  $f$ is finite,
3.  $X$ and $Y$ are normal,
4.  $Y$ is proper.

Then $f$ is an isomorphism.
:::

:::
proof
This is standard; see, for example, Hartshorne[\text{Corollary III.11.4}] or Liu[\text{Theorem 8.12}].
:::

:::{#lem:verification-hypotheses .lemma title="{Verification of Hypotheses for the Classifying Map}
"}
The morphism $\phi:  {B}^{\nu}  \to \overline{F_{{\mathrm{En}}, 2}}$ constructed above satisfies all hypotheses of Zariski's Main Theorem:

1.  Birationality: By Proposition 5.6, $\phi$ restricts to an isomorphism over the dense open subset $F_{{\mathrm{En}}, 2}$.
2.  Finiteness: By Corollary 7.6.6, $\phi$ is finite.
3.  Normality: $ {B}^{\nu} $ is normal by definition as normalization; $ \overline{F_{{\mathrm{En}}, 2}} $ is normal as the normalization of the proper algebraic stack $\overline{F_{{\mathrm{En}}, 2}}$.
4.  Properness: $\overline{F_{{\mathrm{En}}, 2}}$ is proper by the general theory of KSBA compactification for surfaces with numerically trivial canonical class (see Kollár[\text{Theorem 1.2}]).
:::

:::
proof
Each item follows from the explicit construction and previous cited results in this monograph. In particular, items (1) and (2) are established in Sections 7.5 and 7.6, and items (3)-(4) are standard in the theory of moduli stacks of stable pairs.
:::

:::{#thm:main-isomorphism .theorem title="{Main Isomorphism: KSBA and Semitoroidal Compactifications}
"}
The classifying morphism induces canonical isomorphisms: [ \phi:  {B}^{\nu}  \xrightarrow{\sim}  \overline{F_{{\mathrm{En}}, 2}}  ] and hence, [  \overline{F_{{\mathrm{En}}, 2}}  \cong \overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} _{\bullet} } ] where $\mathcal{F} = \{\mathcal{F}_k\}_{k=1}^5$ denotes the system of folded semifans constructed in Section 5.2.
:::

:::
proof
By Lemma 7.7.2 and Theorem 7.7.1, $\phi$ is an isomorphism of normal proper spaces. Surjectivity onto $ \overline{F_{{\mathrm{En}}, 2}} $ is built into the modular construction of $\phi$. From Section 7.5, $ {B}^{\nu} $ is canonically identified, as a semitoroidal compactification via $\mathcal{F}$, with $\overline{F_{{\mathrm{En}}, 2}}^{  \mathcal{F} _{\bullet} }$. The identification is functorial with respect to the delineated semifan combinatorics.
:::

:::{#rem:toroidal-vs-semitoroidal .remark title="{Toroidal vs. Semitoroidal Structure}
"}
By Lemma 5.7 of AEGS, the resulting compactification exhibits hybrid structure: - It is toroidal over the 0-cusps 2 and 4 (where $\mathcal{F}_2$ and $\mathcal{F}_4$ are honest fans), - It is toroidal over the 1-cusps adjacent to the 0-cusps 2 and 4, - It is toroidal over the 1-cusp labeled $35$, - It is strictly semitoroidal (i.e., not toroidal but modeled on an infinite semifan) over the remaining cusps ($\mathcal{F}_1$, $\mathcal{F}_3$, $\mathcal{F}_5$).
:::

:::{#cor:explicit-stratification .corollary title="{Explicit Stratification of the Boundary}
"}
The boundary $\partial  \overline{F_{{\mathrm{En}}, 2}}  =  \overline{F_{{\mathrm{En}}, 2}}  \setminus F_{{\mathrm{En}}, 2}$ decomposes as follows:

-   $0$-dimensional strata correspond to the five $0$-cusps, i.e., the maximally degenerate Enriques surfaces,

-   $1$-dimensional strata correspond to the $1$-cusps, i.e., one-parameter families of degenerations,

-   Higher-dimensional strata correspond to intermediate forms of degeneration.

Each boundary stratum is locally analytically modeled on the cone corresponding to that degeneration in the appropriate folded semifan $\mathcal{F}_k$.
:::

This completes the identification of the KSBA compactification with the explicit semitoroidal model given by folding and restricting the ambient K3 ramification semifans.
All boundary and degeneration structures in $ \overline{F_{{\mathrm{En}}, 2}} $ are thus characterized in terms of the degeneration polyhedral data laid out in Sections 5 and 6.

<!-- Source: 3-part-main-theorem/7-chapter/000-intro.md -->

## Computational Examples {#chapter-6}

<!-- Source: 3-part-main-theorem/7-chapter/800-divisor-models.md -->

### DLT Models

This section gives a precise structural and combinatorial description of divisor models (for degenerations of K3 pairs) and half-divisor models (for Enriques quotients), connecting KSBA limits explicitly to integral-affine data on dual complexes.
Let $\pi: {\mathcal{X}} \to C$ be a degeneration of complex surfaces with ${\mathcal{X}}_0$ ${\mathcal{X}}_0$.
The **dual complex** $\Gamma({\mathcal{X}}_0)$ encodes the topology of ${\mathcal{X}}_0$: each vertex of $\Gamma({\mathcal{X}}*0)$ corresponds to an irreducible component $V_i$, each edge to a double curve $D*{ij} = V_i \cap V_j$.
When ${\mathcal{X}}_0$ has normal crossings, $\Gamma({\mathcal{X}}_0)$ is a finite graph.
Given a Cartier divisor ${\mathcal{R}} \subset {\mathcal{X}}$ disjoint from the singular strata of ${\mathcal{X}}_0$ (i.e., ${\mathcal{R}}$ does not meet points where two or more components meet), the combinatorial geometry of $({\mathcal{X}}_0, {\mathcal{R}}*0)$ is encoded by an **integral-affine divisor** $R*{\mathrm{IA}} \subset \Gamma({\mathcal{X}}_0)$.
This means:

- Each edge of $\Gamma({\mathcal{X}}*0)$ (corresponding to a double curve $D*{ij}$) is assigned an integer weight $n_{ij}$, expressing the degree of intersection of ${\mathcal{R}}*0$ with $D*{ij}$.

- To each vertex $v_i$ (component $V_i$) one assigns a line bundle $L_i \in \operatorname{Pic}(V_i)$ so that, for any edge $v_{ij}$, $\deg(L_i|*{D*{ij}}) = n_{ij}$.
  The weighting must be compatible on edges and satisfy global compatibility conditions.

These weights obey a **balancing condition** at every vertex $v_i$.
For a toric vertex, resp.
a non-toric vertex arising from an internal blowup in the direction $\vec{e}$, we have

[ \sum*j n*{ij} \vec{e}*{ij} = 0, \qquad  \sum*j n*{ij} \vec{e}*{ij} \in {\mathbf{Z}},\vec{e} ] where $\vec{e}_{ij}$ is the primitive integral direction associated to the corresponding edge.
These constraints ensure that the line bundles patch together along double curves and that the data collectively define a global Cartier divisor structure in the smoothing.

:::{#def:divisor-model .definition title="{Divisor Model}
"}
A **divisor model** for a degeneration $\pi: {\mathcal{X}} \to C$ of K3 (or Enriques) surfaces is a degeneration of pairs $({\mathcal{X}}, {\mathcal{R}}) \to C$ such that:

-   ${\mathcal{R}}$ is a Cartier divisor, with ${\mathcal{R}}_t = {\mathcal{R}} \cap {\mathcal{X}}_t$ effective for all $t \in C$,
-   For $t \neq 0$, ${\mathcal{R}}_t$ is semiample,
-   ${\mathcal{R}}$ does not meet the singular strata of ${\mathcal{X}}_0$ (i.e., is disjoint from double/triple intersections).
:::

Given a divisor model, the isomorphism class of ${\mathcal{O}}_{{\mathcal{X}}_0}({\mathcal{R}}*0)$ is encoded by its corresponding integral-affine divisor $R*{\mathrm{IA}}$ on $\Gamma({\mathcal{X}}*0)$.
The dual complex, together with $R*{\mathrm{IA}}$, captures all line bundle glueing data and allows for explicit calculation of limit objects.

:::{#prop:classification-ia-data .proposition title="{Classification via Integral-Affine Data}
"}
Given a fixed Picard--Lefschetz monodromy invariant $\lambda$, the combinatorial type $(\Gamma({\mathcal{X}}_0), R_{\mathrm{IA}})$---that is, the dual complex with its weighted, balanced subgraph---uniquely determines the KSBA stable limit $(\overline{{\mathcal{X}}}_0, \epsilon \overline{{\mathcal{R}}}_0)$. Furthermore, this combinatorial type is locally constant in families with fixed Picard--Lefschetz form.
:::

:::{#prop:semitoroidal-recognizable .proposition title="{Semitoroidal Compactification via Recognizable Divisors}
"}
If $R$ is a recognizable divisor (such as the fixed locus of a nonsymplectic involution), then there exists a unique semifan $ \mathcal{F} _R$ whose semitoroidal compactification normalizes the KSBA compactification of the relevant moduli space $F_{{\mathrm{En}}, 2}$[6, Sec. 5C].
:::

:::{#thm:explicit-construction .theorem title="{Explicit Construction and Type Determination}
"}
Given a polarized integral-affine structure $(B(\ell), R_{\mathrm{IA}})$ (with $\ell = (\lambda \cdot \alpha_i)_{i \in G}$), and an appropriate triangulation, one obtains [ (B(\ell), R\_{\mathrm{IA}}) = (\Gamma({\mathcal{X}}\_0), \Gamma({\mathcal{R}}\_0)) ] as the dual complex of the ${\mathcal{X}}_0$ of a divisor model with monodromy invariant $\lambda$.
:::

:::{#def:half-divisor-model .definition title="{Half-Divisor Model}
"}
Suppose $({\mathcal{X}}, {\mathcal{R}}) \to (C,0)$ is a divisor model for a family of K3 surfaces admitting an involution $\iota_{{\mathrm{En}}}$ that preserves ${\mathcal{R}}$. The **half-divisor model** is the quotient [ ({\mathcal{Z}}, {\mathcal{R}}\_{\mathcal{Z}}) := ({\mathcal{X}}, {\mathcal{R}})/\iota_{{\mathrm{En}}}. ] These models realize degenerations of Enriques pairs as quotients of K3 divisor models, and in generic settings, the quotient inherits slc singularities, and the divisor structure matches the normalization of the image of ${\mathcal{R}}$[2, Prop. 4.5].
:::

:::{#prop:geometric-types .proposition title="{Geometric Types and Boundary Strata}
"}
Let $({\mathcal{Z}}, {\mathcal{R}}_{{\mathcal{Z}}}) \to (C,0)$ be a half-divisor model for $F_{{\mathrm{En}}, 2}$ as constructed above. Then the following properties hold:

-   The fibers of ${\mathcal{Z}}$ have semi-log canonical (slc) singularities.

-   The divisor $K_{{\mathcal{Z}}} + \epsilon {\mathcal{R}}_{{\mathcal{Z}}}$ is relatively big and nef over $C$.

-   The divisor ${\mathcal{R}}_{{\mathcal{Z}}}$ contains no log canonical centers.

More precisely:

-   In the case of Type ${\textrm{III}}$ degenerations at cusp $1$, the dual complex $\Gamma({\mathcal{Z}}_0)$ is homeomorphic to $\mathbb{R}\mathbb{P}^2$; each irreducible component $V_i$ of the ${\mathcal{X}}_0$ ${\mathcal{Z}}_0$ is, after normalization, isomorphic to one of the preimage components of ${\mathcal{X}}_0$.

-   For Type ${\textrm{III}}$ degenerations at cusps $2$--$5$, the dual complex $\Gamma({\mathcal{Z}}_0)$ is homeomorphic to $\mathbb{D}^2$. If a component $V_i$ lifts to two distinct components of ${\mathcal{X}}_0$, the normalized copies are isomorphic; if it arises from a single irreducible component, the involution $\iota_{{\mathrm{En}}, 0}$ acts on $V_i$ with precisely four fixed points.

-   In the case of Type $\mathrm{II}$ degenerations, $\Gamma({\mathcal{Z}}_0)$ is a segment, and the quotient is described by the action of $\iota_{{\mathrm{En}}, 0}$ as detailed in [2, Proposition 4.5].
:::

:::
proof
See detailed analyses in (**AEGS23?**, Prop. 4.5), which classify Enriques degenerations by their dual complex and describe the induced slc structure and divisor support in every case.
:::

:::{#cor:ksba-stable-limit .corollary title="{Computability of the KSBA Stable Limit}
"}
Given a degeneration $({\mathcal{Z}}^*, \epsilon {\mathcal{R}}_{{\mathcal{Z}}}^*) \to C^*$, the KSBA-stable limit is [ \operatorname{Proj}*C \bigoplus*{n \geq 0} H\^0({\mathcal{Z}}, n {\mathcal{R}}\_{{\mathcal{Z}}}), ] where the right-hand side is computed from the data of the half-divisor model $({\mathcal{Z}}, {\mathcal{R}}_{{\mathcal{Z}}}) \to (C, 0)$.
:::

:::
remark
The quotient $\Gamma({\mathcal{Z}}_0) = \Gamma({\mathcal{X}}_0) / \iota_{{\mathrm{En}}, \mathrm{IA}}$ always inherits a natural integral-affine structure, encoding both the combinatorics and divisor data of the degeneration[2, Prop. 4.5]. In Type ${\textrm{III}}$, certain boundary components are the images of the "Enriques equator" and are characterized by four $A_1$ singularities.
:::

:::
remark
For general monodromy invariant $\lambda$, half-divisor models exist only generically: the involution $\iota_{{\mathrm{En}}}$ may be only birational on ${\mathcal{X}}_0$s. After contracting exceptional loci to resolve indeterminacies, one obtains only a dlt pair. This supports the broader philosophy (see , ) that dlt models, rather than strictly semistable ones, are the correct analogues of Kulikov models for $K$-trivial surface degenerations.
:::

<!-- Source: 3-part-main-theorem/7-chapter/900- five-cusps.md -->

#### The Five Cusps

\todo{Insert sagecode output for maximal parabolics + elliptics}

This section provides an explicit, case-by-case analysis of the five 0-cusps of $F_{{\mathrm{En}}, 2}$, describing the structure of the corresponding semifans, dual complexes, integral-affine data, and involution symmetries arising in the boundary of the KSBA compactification, as described in (**AEGS23?**). The semifans $ \mathcal{F} *k$ are defined by intersecting the ambient ramification semifan $ \mathcal{F} *{\operatorname{ram}}(T*{\operatorname{dP}})$ with the Enriques lattice subspace $T*{{\mathrm{En}}}$, for each lattice polarization $T_{\operatorname{dP}}$ occurring at a cusp.
By \cref{thm:five-semifans}, the resulting collection $  \mathcal{F} _{\bullet}  = \{ \mathcal{F} *k\}*{k=1}^{5}$ consists of generalized Coxeter semifans governing the semitoroidal structure at each cusp.
Each semifan encodes the stratified boundary behavior of the compactification via its rays (corresponding to degenerations of Types ${\textrm{II}}$ and ${\textrm{III}}$) and the folding symmetries inherited from involutions on the integral-affine structures.

#### 8.2. Structure of Half-Divisor Models

Let $({\mathcal{Z}}, {\mathcal{R}}*{{\mathcal{Z}}}) \to (C,0)$ be a half-divisor model for $F*{{\mathrm{En}},2}$ as in Proposition 4.5. The following facts hold for each such degeneration:

- The fibers of ${\mathcal{Z}}$ have semi-log-canonical (slc) singularities.
- $K_{{\mathcal{Z}}} + \epsilon {\mathcal{R}}_{{\mathcal{Z}}}$ is relatively big and nef over $C$.
- The boundary ${\mathcal{R}}_{{\mathcal{Z}}}$ contains no log canonical centers.

These conditions ensure that all ${\mathcal{X}}_0$s belong to the class of degenerations permitted by the KSBA theory and are appropriate for the log minimal model program (MMP).

#### 8.3. Involutions and Symmetries

#### Definition 8.3.1 (Enriques Involutions)

- $\iota_{{\mathrm{En}}}$: the fixed-point-free Enriques involution of the total space ${\mathcal{X}}$ in a K3 surface degeneration, as in [AE23, Def. 6.2].
- $\iota_{{\mathrm{En}}, 0}$: the restriction to the ${\mathcal{X}}*0$; when $\iota*{{\mathrm{En}}, 0}$ acts freely, ${\mathcal{Z}}_0 = {\mathcal{X}}*0/\iota*{{\mathrm{En}}, 0}$ is an Enriques surface [AE23, Prop. 4.5].
- $\iota_{{\mathrm{En}},\mathrm{IA}}$: the involution acting on the integral-affine sphere $\mathrm{IAS}^2$ $B(\ell)$ or the dual complex $\Gamma({\mathcal{X}}_0)$ by folding, see [AE23, Prop. 4.5, Thm. 1].

A dual complex $\Gamma({\mathcal{X}}*0)$ or sphere $B(\ell)$ is said to be of Enriques type if and only if it admits such an involution $\iota*{{\mathrm{En}}, \mathrm{IA}}$.

#### Lemma 8.3.2 (Normalization and Component Structure in Half-Divisor Models)

Let $({\mathcal{Z}}, {\mathcal{R}}_{{\mathcal{Z}}})$ be a half-divisor model as in [AE23, Prop. 4.5, Prop. 4.8].

- If a component $V_i \subset {\mathcal{Z}}_0$ is covered by two irreducible components of ${\mathcal{X}}_0$, then (up to normalization) $V_i$ is isomorphic to either.
- If $V_i$ is covered by a single irreducible component $\widetilde{V}*i \subset {\mathcal{X}}*0$, then $\iota*{{\mathrm{En}}, 0}$ acts on $\widetilde{V}*i$ with exactly four fixed points, occurring as two pairs on double curves $\widetilde{D}*{ij}$, $\widetilde{D}*{ik}$.

:::
proof
See [AE23, Prop. 4.8].
:::

#### Remark 8.3.3 (Topology of Dual Complexes by Degeneration Type)

- Type $\mathrm{III}$, cusp (1): $\Gamma({\mathcal{Z}}_0) = \mathbb{R}\mathbb{P}^2$.
- Type $\mathrm{III}$, cusps (2--5): $\Gamma({\mathcal{Z}}_0) = \mathbb{D}^2$.
- Type $\mathrm{II}$: $\Gamma({\mathcal{Z}}_0)$ is a segment.

See [AE23, Prop. 4.8] for explicit models.

#### Lemma 8.3.4 (Involution Actions in Types $\mathrm{II}$ and $\mathrm{III}$)

For Type $\mathrm{II}$ degenerations [AE23, Prop. 4.8]: - In "double rectangle" cases, $\iota_{{\mathrm{En}}, 0}$ exchanges the two components of $\Gamma({\mathcal{X}}*0)$ without fixed points.
- For a preserved double curve $E$, $\iota*{{\mathrm{En}}, 0}$ acts via a nontrivial $2$-torsion translation.
- In "single rectangle" cases, $\iota_{{\mathrm{En}}, 0}$ preserves each component; on any double curve, its action is an elliptic involution with four fixed points.

#### 8.5. Explicit Summary of Boundary Data by Cusp

##### Cusp 1

- **Coxeter Diagram:** See \Cref{fig:fen2-coxeter-1}.
- **Boundary Type:** Maps to cusp $(10,10,0)*1$ of $F*{{\mathrm{En}}}$, and $\Gamma({\mathcal{Z}}_0) = \mathbb{R}\mathbb{P}^2$.
- **Lattice Data:** $\overline{T_{\operatorname{dP}}} = (18,2,0)*1 = U(2)\oplus E_8^2$, with symmetry $J$ given by $180^\circ$ rotation; invariant sublattice $\overline{T*{\operatorname{dP}}}^{J=1} = U(2) \oplus E_8(2)$.
- **Semifan Structure:** The irrelevant subgroup is infinite, so ${\mathcal{F}}_1$ is an infinite semifan and the compactification is semitoroidal.
- **Degeneration Rays:** 2 type $\mathrm{II}$ rays (elliptic subdiagrams); 0 type $\mathrm{III}$ rays; 2 total.
- **IAS Symmetry:** $\lambda \in  \mathfrak{C} ^J$ if and only if $\ell_i = \ell_{8+i}$ ($i=0,\ldots,7$), $\ell_{16} = \ell_{18}$, $\ell_{17} = \ell_{19}$; involution acts as $180^\circ$ rotation on each hemisphere, swapping $P$ and $P^{\mathrm{op}}$.

##### Cusp 2

- **Coxeter Diagram:** See \Cref{fig:fen2-coxeter-2}.
- **Boundary Type:** Maps to cusp $(10,8,0)*1$ of $F*{{\mathrm{En}}}$; $\Gamma({\mathcal{Z}}_0) = \mathbb{D}^2$.
- **Lattice Data:** $\overline{T_{\operatorname{dP}}} = (18,0,0)_1 = U \oplus E_8^2$, $J$ is vertical reflection; invariant sublattice $U \oplus E_8(2)$.
- **Semifan Structure:** Irrelevant subgroup is $S_2$; ${\mathcal{F}}_2$ is a finite fan, giving a toroidal compactification.
- **Degeneration Rays:** 2 type $\mathrm{II}$, 7 type $\mathrm{III}$; 9 total.
- **IAS Symmetry:** $\lambda$ in $ \mathfrak{C} ^J$ iff $\ell_i = \ell_{20-i}$ $(i=1,\ldots,9)$; involution flips both hemispheres about the vertical axis.

##### Cusp 3

- **Coxeter Diagram:** See \Cref{fig:fen2-coxeter-3}.
- **Boundary Type:** Maps to cusp $(10,8,0)_1$; $\Gamma({\mathcal{Z}}_0) = \mathbb{D}^2$.
- **Lattice Data:** $\overline{T_{\operatorname{dP}}} = (18,2,0)*1 = U(2)\oplus E_8^2$, $J$ is diagonal reflection followed by $\alpha*{20}$ reflection; $\overline{T_{\operatorname{dP}}}^{J=1} = U(2)\oplus E_8(2)$.
- **Semifan Structure:** Irrelevant subgroup is infinite; ${\mathcal{F}}_3$ is semitoroidal.
- **Degeneration Rays:** 2 type $\mathrm{II}$, 7 type $\mathrm{III}$; 9 total.
- **IAS Symmetry:** $\lambda$ in $ \mathfrak{C} ^J$ iff $\ell_i = \ell_{16-i}$ $(i=1,\ldots,7)$, $\ell_{17}=\ell_{19}$, $\ell_{20}=0$ (folding symmetry requires $\ell_{20}=0$); the involution acts as diagonal flip.

##### Cusp 4

- **Coxeter Diagram:** See \Cref{fig:fen2-coxeter-4}.
- **Boundary Type:** Maps to cusp $(10,8,0)_1$; $\Gamma({\mathcal{Z}}_0) = \mathbb{D}^2$.
- **Lattice Data:** $\overline{T_{\operatorname{dP}}} = (18,2,0)*1 = U(2)\oplus E_8^2$, $J$ is horizontal reflection; $\overline{T*{\operatorname{dP}}}^{J=1} = U(2)\oplus E_8(2)$.
- **Semifan Structure:** Irrelevant subgroup is $S_2^2$; ${\mathcal{F}}_4$ is a finite fan (toroidal).
- **Degeneration Rays:** 4 type $\mathrm{II}$, 7 type $\mathrm{III}$; 11 total.
- **IAS Symmetry:** $\lambda$ in $ \mathfrak{C} ^J$ iff each hemisphere of $B(\ell)$ is symmetric under a horizontal flip; the involution reflects across this axis.

##### Cusp 5

- **Coxeter Diagram:** See \Cref{fig:fen2-coxeter-5}.
- **Boundary Type:** Maps to cusp $(10,8,0)_1$; $\Gamma({\mathcal{Z}}_0) = \mathbb{D}^2$.
- **Lattice Data:** $\overline{T_{\operatorname{dP}}} = (18,2,0)*1 = U(2)\oplus E_8^2$, $J$ is composition of eight commuting reflections $\alpha_1,\ldots,\alpha*{15}$; $\overline{T_{\operatorname{dP}}}^{J=1} = U(2)\oplus E_8(2)$.
- **Semifan Structure:** Irrelevant subgroup infinite; ${\mathcal{F}}_5$ is semitoroidal.
- **Degeneration Rays:** 3 type $\mathrm{II}$, 0 type $\mathrm{III}$; 3 total.
- **IAS Symmetry:** $\lambda \in  \mathfrak{C} ^J$ iff $\ell_{2i+1}=0$ for $i=0,\ldots,7$; involution flips hemispheres as in the cover.

* * *
Cusp   Dual Complex $\Gamma({\mathcal{Z}}*0)$   Coxeter Diagram      Irrelevant Subgroup   Semifan Type   \# Type $\mathrm{II}$   \# Type $\mathrm{III}$   Total Rays   $\iota*{{\mathrm{En}},\mathrm{IA}}$ Action (IAS)
* * *
1      $\mathbb{R}\mathbb{P}^2$        fig:fen2-coxeter-1   Infinite              Semitoroidal   2                       0                        2            $180^\circ$ rotate $+$ flip hemispheres

2      $\mathbb{D}^2$                  fig:fen2-coxeter-2   $S_2$                 Toroidal       2                       7                        9            Vertical flip of both hemispheres

3      $\mathbb{D}^2$                  fig:fen2-coxeter-3   Infinite              Semitoroidal   2                       7                        9            Diagonal flip

4      $\mathbb{D}^2$                  fig:fen2-coxeter-4   $S_2^2$               Toroidal       4                       7                        11           Horizontal flip

## 5      $\mathbb{D}^2$                  fig:fen2-coxeter-5   Infinite              Semitoroidal   3                       0                        3            Flip hemispheres (cover symmetry)

* * *

Overall, the boundary stratification is determined by:

- 6 type $\mathrm{II}$ rays (elliptic subdiagrams),
- 21 type $\mathrm{III}$ rays (maximal or nearly maximal degenerations),
- 27 rays in total across the five cusps.

The involution symmetries on the integral-affine sphere and dual complex precisely encode the gluing data for the half-divisor models and fold the boundary stratification according to Enriques automorphisms.
Full geometric and combinatorial information, including explicit diagrams and integral-affine gluing data, is referenced in [AE23, Figs. 4, 5, 11, 12, 17].

<!-- CUSP DATA

#### # Cusp 1

- Coxeter diagram \Cref{fig:fen2-coxeter-1}
- Relation to $F_{{\mathrm{En}}}$: maps to cusp $(10,10, 0)*1$ in $F*{{\mathrm{En}}}$
  - $\implies \Gamma({\mathcal{Z}}_0) = {\mathbf{RP}}^2$.
- $\overline{T_{\operatorname{dP}}} = (18, 2, 0)_1 = U(2) \oplus E_8^2$
  - $J$: rotation by $180^\circ$
  - $\overline{T_{\operatorname{dP}}}^{J=1} = U(2) \oplus E_8(2)$
- Semifan data:
  - The irrelevant subgroup is infinite.
  - ${\mathcal{F}}_1$ is a semifan, the compactification is semitoroidal.
- Diagram data
  - 2 type ${\textrm{II}}$ rays, corresponding to elliptic subdiagrams in \Cref{fig:fen2-coxeter-parabolic-1}
  - 0 type ${\textrm{III}}$ rays, corresponding to elliptic subdiagrams in \Cref{fig:fen2-coxeter-ell-1}
  - 2 total rays.
- IAS data
  - $\lambda \in  \mathfrak{C} ^J \iff$
    - $\lambda \in  \mathfrak{C} ^J$ if and only if
    - $\ell_i = \ell_{8+i}$ for all $i=0, \ldots, 7$,
    - $\ell_{16} = \ell_{18}$,
    - $\ell_{17} = \ell_{19}$.
  - $\iota_{{\mathrm{En}}, \mathrm{IA}} \curvearrowright B(\lambda):$
    - Rotate each hemisphere by $180^\circ$,
    - Then flip the two hemispheres $P$ and $P^{\mathrm{op}}$.
  - $\iota_{{\mathrm{En}}, 0} \curvearrowright \Gamma({\mathcal{Z}}_0)$:
    - ?

#### # Cusp 2

- Coxeter diagram \Cref{fig:fen2-coxeter-2}
- Relation to $F_{{\mathrm{En}}}$: maps to cusp $(10,8, 0)*1$ in $F*{{\mathrm{En}}}$
  - $\implies \Gamma({\mathcal{Z}}_0) = \mathbf{D}^2$ (closed 2-disk).
- $\overline{T_{\operatorname{dP}}}= (18, 0, 0)_1 = U \oplus E_8^2$
  - $J$: vertical reflection.
  - $\overline{T_{\operatorname{dP}}}^{J=1} = U\oplus E_8(2)$
- Semifan data:
  - The irrelevant subgroup is $S_2$.
  - ${\mathcal{F}}_2$ is a fan, the compactification is strictly toroidal.
- Diagram data
  - 2 type ${\textrm{II}}$ rays, corresponding to elliptic subdiagrams in \Cref{fig:fen2-coxeter-parabolic-2}
  - 7 type ${\textrm{III}}$ rays, corresponding to elliptic subdiagrams in \Cref{fig:fen2-coxeter-ell-2}
  - 9 total rays.
- IAS data
  - $\lambda \in  \mathfrak{C} ^J \iff$
    - $\lambda \in  \mathfrak{C} ^J$ if and only if $\ell_i = \ell_{20-i}$ for all $i=1, \ldots, 9$.
  - $\iota_{{\mathrm{En}}, \mathrm{IA}} \curvearrowright B(\lambda):$
    - Flip both the hemisphere $P$ and its opposite $P^{\mathrm{op}}$ across the vertical line bisecting the bottom and top edges.
  - $\iota_{{\mathrm{En}}, 0} \curvearrowright \Gamma({\mathcal{Z}}_0)$:
    - ?

#### # Cusp 3

- Coxeter diagram \Cref{fig:fen2-coxeter-3}
- Relation to $F_{{\mathrm{En}}}$: maps to cusp $(10,8, 0)*1$ in $F*{{\mathrm{En}}}$
  - $\implies \Gamma({\mathcal{Z}}_0) = \mathbf{D}^2$.
- $\overline{T_{\operatorname{dP}}} = (18, 2, 0)_1 = U(2) \oplus E_8^2$
  - $J$: diagonal reflection composed with a reflection in the root $\alpha_{20}$
  - $\overline{T_{\operatorname{dP}}}^{J=1} = U(2) \oplus E_8(2)$
- Semifan data:
  - The irrelevant subgroup is infinite.
  - ${\mathcal{F}}_3$ is a semifan, the compactification is semitoroidal.
- Diagram data
  - 2 type ${\textrm{II}}$ rays, corresponding to elliptic subdiagrams in \Cref{fig:fen2-coxeter-parabolic-3}
  - 7 type ${\textrm{III}}$ rays, corresponding to elliptic subdiagrams in \Cref{fig:fen2-coxeter-ell-3}
  - 9 total rays.
- IAS data
- $\lambda \in  \mathfrak{C} ^J \iff$
  - $\lambda \in  \mathfrak{C} ^J$ if and only if
  - $\ell_i = \ell_{16-i}$ for all $i=1,\ldots,7$,
  - $\ell_{17} = \ell_{19}$,
  - $\ell_{20} = 0$.
    - This is because the folding symmetry reflecting in the root $\alpha_{20}$, since $w_{\alpha_{20}}(\lambda) = \lambda$ implies $\ell_{20} = \lambda \cdot \alpha_{20} = 0$.
    - $\ell_{20}$ measures the signed lattice distance between the two singularities from Symington surgeries on the edges parallel to $(1,-1)$ and $(-1,1)$.
      $B(\ell)$ is constructed so these two singularities coincide.
- $\iota_{{\mathrm{En}}, \mathrm{IA}} \curvearrowright B(\lambda):$
  - The involution $\iota_{{\mathrm{En}}, \mathrm{IA}}$ acts by flipping each hemisphere $P$ and $P^{\mathrm{op}}$ diagonally.
- $\iota_{{\mathrm{En}}, 0} \curvearrowright \Gamma({\mathcal{Z}}_0)$:
  - ?

#### # Cusp 4

- Coxeter diagram \Cref{fig:fen2-coxeter-4}
- Relation to $F_{{\mathrm{En}}}$: maps to cusp $(10,8, 0)*1$ in $F*{{\mathrm{En}}}$
  - $\implies \Gamma({\mathcal{Z}}_0) = \mathbf{D}^2$.
- $\overline{T_{\operatorname{dP}}} = (18, 2, 0)_1 = U(2) \oplus E_8^2$
  - $J$: horizontal reflection
  - $\overline{T_{\operatorname{dP}}}^{J=1} = U(2) \oplus E_8(2)$
- Semifan data:
  - The irrelevant subgroup is $S_2^2$.
  - ${\mathcal{F}}_4$ is a fan, the compactification is strictly toroidal.
- Diagram data
  - 4 type ${\textrm{II}}$ rays, corresponding to elliptic subdiagrams in \Cref{fig:fen2-coxeter-parabolic-4}
  - 7 type ${\textrm{III}}$ rays, corresponding to elliptic subdiagrams in \Cref{fig:fen2-coxeter-ell-4}
  - 11 total rays.
- IAS data
- $\lambda \in  \mathfrak{C} ^J \iff$
  - $\lambda \in  \mathfrak{C} ^J$ if and only if
  - Each hemisphere of $B(\ell)$ is symmetric under a flip along the horizontal line bisecting the edges $\ell_6(0,1)$ and $\ell_{14}(0,-1)$.
  - TODO MAKE PRECISE
- $\iota_{{\mathrm{En}}, \mathrm{IA}} \curvearrowright B(\lambda):$
  - The involution is reflection across this horizontal axis of the hemisphere.
- $\iota_{{\mathrm{En}}, 0} \curvearrowright \Gamma({\mathcal{Z}}_0)$:
  - ?

#### # Cusp 5

- Coxeter diagram \Cref{fig:fen2-coxeter-5}
- Relation to $F_{{\mathrm{En}}}$: maps to cusp $(10,8, 0)*1$ in $F*{{\mathrm{En}}}$
  - $\implies \Gamma({\mathcal{Z}}_0) = \mathbf{D}^2$.
- $\overline{T_{\operatorname{dP}}} = (18, 2, 0)_1 = U(2) \oplus E_8^2$
  - $J$: composition of 8 commuting reflections in the roots $\alpha_1, \cdots, \alpha_{15}$
  - $\overline{T_{\operatorname{dP}}}^{J=1} = U(2) \oplus E_8(2)$
- Semifan data:
  - The irrelevant subgroup is infinite.
  - ${\mathcal{F}}_5$ is a semifan, the compactification is semitoroidal.
- Diagram data
  - 3 type ${\textrm{II}}$ rays, corresponding to elliptic subdiagrams in \Cref{fig:fen2-coxeter-parabolic-5}
  - 0 type ${\textrm{III}}$ rays, corresponding to elliptic subdiagrams in \Cref{fig:fen2-coxeter-ell-5}
  - 3 total rays.
- IAS data
- $\lambda \in  \mathfrak{C} ^J \iff$
  - $\ell_{2i+1} = 0$ for $i = 0, \ldots, 7$.
  - The eight $\times$-marked nodes correspond to eight collisions of pairs of $I_1$ singularities along the equator of $B(\ell)$.
- $\iota_{{\mathrm{En}}, \mathrm{IA}} \curvearrowright B(\lambda):$
  - The involution $\iota_{{\mathrm{En}}, \mathrm{IA}}$ acts by flipping the two hemispheres $P$ and $P^{\mathrm{op}}$ mirroring the extension of $\iota_{\operatorname{dP}}$ to ${\mathcal{X}}_0$.
- $\iota_{{\mathrm{En}}, 0} \curvearrowright \Gamma({\mathcal{Z}}_0)$:
  - ?

#### # Conclusion

- Semifan data:
  - 6 Type ${\textrm{II}}$ rays,
  - 21 Type ${\textrm{III}}$ rays,
  - 27 total rays,

\todo{Example No explicit worked example of a Type III degeneration and its associated $\mathrm{IAS}^2$ is provided.
Including at least one fully annotated example (e.g., standard toric, or a non-toric case) would clarify constructions.
}

-->
<!-- Source: 3-part-main-theorem/7-chapter/999-appendix.md -->

### Appendix

#### Root Systems

##### $A_4$

The relevant Euclidean space is ${\mathbb{E}}_{A_4} = \{ x \in {\mathbf{R}}^5 : x_1+x_2+x_3+x_4+x_5=0 \}$ with $$ \Phi(A_4)\colon
\begin{cases}
\alpha_1= e_1 - e_2 \\
\alpha_2= e_2 - e_3 \\
\alpha_3= e_3 - e_4 \\
\alpha_4= e_4 - e_5
\end{cases}
\qquad G_{A_4(-1)} =
\begin{pmatrix}
-2 & 1 & 0 & 0 \\
1 & -2 & 1 & 0 \\
0 & 1 & -2 & 1 \\
0 & 0 & 1 & -2
\end{pmatrix}
$$ By convention, we take $A_n$ to mean $A_n(-1)$.
This has Coxeter diagram [ A_4:\quad \dynkin[mark=o,scale=3]{A}{4} ]

##### $B_4$

Roots live in ${\mathbb{E}}_{B_4} = {\mathbf{R}}^4$, and $$ \Phi(B_4)\colon
\begin{cases}
\alpha_1 = e_1 - e_2 \\
\alpha_2 = e_2 - e_3 \\
\alpha_3 = e_3 - e_4 \\
\alpha_4 = e_4
\end{cases}
\qquad G_{B_4(-1)} =
\begin{pmatrix}
-2 & 1 & 0 & 0 \\
1 & -2 & 1 & 0 \\
0 & 1 & -2 & 1 \\
0 & 0 & 1 & -1
\end{pmatrix}
$$ Because we typically work with roots with $v^2 = -2$ or $-4$, we often replace $B_n$ with $B_n(2)$, where for example $$ G_{B_4(-2)} =
\begin{pmatrix}
-4 & 2 & 0 & 0 \\
2 & -4 & 2 & 0 \\
0 & 2 & -4 & 2 \\
0 & 0 & 2 & -2
\end{pmatrix}
$$ By convention, we thus take $B_n$ to mean $B_n(-2)$, and identify the following Coxeter diagram: [ B_4: \quad  \dynkin[arrows=false,scale=3]{B}{***o} ]

##### $C_4$

Set ${\mathbb{E}}_{C_4} = {\mathbf{R}}^4$, then $$ \Phi(C_4)\colon
\begin{cases}
\alpha_1 = e_1 - e_2 \\
\alpha_2 = e_2 - e_3 \\
\alpha_3 = e_3 - e_4 \\
\alpha_4 = 2e_4
\end{cases}
\qquad G_{C_4(-1)} =
\begin{pmatrix}
-2 & 1 & 0 & 0 \\
1 & -2 & 1 & 0 \\
0 & 1 & -2 & 2 \\
0 & 0 & 2 & -4
\end{pmatrix}
$$ We again take $C_n$ to mean $C_n(-1)$ by convention, with Coxeter diagram [ C_4:\quad \dynkin[arrows=false,scale=3]{C}{ooo*} ]

##### $D_4$

Roots live in ${\mathbb{E}}_{D_4} = {\mathbf{R}}^4$ and $$ \Phi(D_4)\colon
\begin{cases}
\alpha_1 = e_1 - e_2 \\
\alpha_2 = e_2 - e_3 \\
\alpha_3 = e_3 - e_4 \\
\alpha_4 = e_3 + e_4
\end{cases}
\qquad G_{D_4(-1)} =
\begin{pmatrix}
-2 & 1 & 0 & 0 \\
1 & -2 & 1 & 1 \\
0 & 1 & -2 & 0 \\
0 & 1 & 0 & -2
\end{pmatrix}
$$ We take $D_n$ to mean $D_n(-1)$, and identify th

##### $E_6$

Roots live in ${\mathbb{E}}_{E_6} = \{ x \in {\mathbf{R}}^8 : x_1+\cdots+x_8=0 \}$ with $$ \Phi(E_6)\colon\,\,
\begin{cases}
\alpha_1 = e_1 - e_2 \[6pt]
\alpha_2 = e_2 - e_3 \[6pt]
\alpha_3 = e_3 - e_4 \[6pt]
\alpha_4 = e_4 - e_5 \[6pt]
\alpha_5 = e_5 - e_6 \[6pt]
\alpha_6 = \tfrac{1}{2}(e_1 + e_2 + e_3 + e_4 - e_5 - e_6 - e_7 - e_8)
\end{cases}\hspace{2em}
G_{E_6(-1)} =
\begin{pmatrix}
-2 & 1  & 0  & 0  & 0  & 0 \\
1  & -2 & 1  & 0  & 0  & 0 \\
0  & 1  & -2 & 1  & 0  & 0 \\
0  & 0  & 1  & -2 & 1  & -1 \\
0  & 0  & 0  & 1  & -2 & 0 \\
0  & 0  & 0  & -1 & 0  & -2
\end{pmatrix}
$$ We take $E_n$ to mean $E_n(-1)$, and identify [ E_6: \dynkin[mark=o,scale=2.5]{E}{6} ]

##### $F_4$

We take the simple roots [
\begin{cases}
\alpha_1 = e_2 - e_3 \\
\alpha_2 = e_3 - e_4 \\
\alpha_3 = e_4 \\
\alpha_4 = {1\over 2}(e_1 - e_2 - e_3 - e_4)
\end{cases}
] with the standard Gram matrix
$$

G\_{F_4} =
\begin{pmatrix}
2 & -1 & 0 & 0 \\
-1 & 2 & -1 & 0 \\
0 & -1 & 1 & -{1\over 2} \\
0 & 0 & -{1\over 2} & 1
\end{pmatrix}
$$ To work integrally, we rescale by $-2$: [ G\_{F_4(-2)} =
\begin{pmatrix}
-4 & 2 & 0 & 0 \\
2 & -4 & 2 & 0 \\
0 & 2 & -2 & 1 \\
0 & 0 & 1 & -2
\end{pmatrix}

] and thus take $F_4$ to mean $F_4(-2)$, with Coxeter diagram [ F_4: \quad \dynkin[arrows=false,scale=3]{F}{ooo\*} ]

##### $G_2$
Roots live in ${\mathbb{E}}_{G_2} = \{ x \in {\mathbf{R}}^3 {~\mathrel{\Big\vert}~} x_1 + x_2 + x_3 = 0 \}$ with simple roots and Gram matrix
$$
\Phi(G_2)\colon
\begin{cases}
\alpha_1 = e_1 - e_2 \\
\alpha_2 = -e_1 + 2e_2 - e_3
\end{cases}
\qquad G_{G_2(-1)} =
\begin{pmatrix}
-2 & 3 \\
3 & -6
\end{pmatrix}
.$$ We thus take $G_2$ to mean $G_2(-1)$, and identify [ G_2:\quad \dynkin[arrows=false,label,labels={,-6},scale=4,text style/.style={scale=1.2}]{G}{o\*} ]

### Root Lattice Conventions {#section-root-lattice-conventions}

To fix conventions, we record here Bourbaki's conventions for these Dynkin diagrams and the corresponding simple roots.

The Euclidean embeddings can be used to compute the following invariants in all types:

\begin{center}
\captionof{table}{Simply Laced Root Lattices (A, D, E types)}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{|l|c|c|c|c|c|}
\hline
& $A_n$ & $D_n$ & $E_6$ & $E_7$ & $E_8$ \\
\hline
$\operatorname{rank}(L) = |\Phi(L)|$ & $n$ & $n$ & $2 \cdot 3$ & $7$ & $2^3$ \\
\hline
$|R(L)|$ & $n(n+1)$ & $2n(n-1)$ & $2^3 \cdot 3^2$ & $2 \cdot 3^2 \cdot 7$ & $2^4 \cdot 3 \cdot 5$ \\
\hline
$W(L)$ & $S_{n+1}$ & $({\mathbf{Z}}_2)^{n-1} \rtimes S_n$ & $W(E_6)$ & $W(E_7)$ & $W(E_8)$ \\
\hline
$|W(L)|$ & $(n+1)!$ & $2^{n-1}\cdot n!$ & $2^7 \cdot 3^4 \cdot 5$ & $2^{10} \cdot 3^4 \cdot 5 \cdot 7$ & $2^{14} \cdot 3^5 \cdot 5^2 \cdot 7$ \\
\hline
$A_L$ & ${\mathbf{Z}}_{n+1}$ & ${\mathbf{Z}}_{2^2}$ or ${\mathbf{Z}}_2^2$\footnote{For $D_n$, $A_L = {\mathbf{Z}}_{2^2}$ when $n$ is odd, and $A_L = ({\mathbf{Z}}_2)^2$ when $n$ is even.} & ${\mathbf{Z}}_3$ & ${\mathbf{Z}}_2$ & $\{0\}$ \\
\hline
$\operatorname{disc}(L)$ & $n+1$ & $2^2$ & $3$ & $2$ & $1$ \\
\hline
\end{tabular}\vspace{2em}

\captionof{table}{Non-Simply Laced Root Lattices (B, C, F, G types)}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{|l|c|c|c|c|}
\hline
& $B_n$ & $C_n$ & $F_4$ & $G_2$ \\
\hline
$\operatorname{rank}(L) = |\Phi(L)|$ & $n$ & $n$ & $2^2$ & $2$ \\
\hline
$|R(L)|$ & $2n^2$ & $2n^2$ & $2^4 \cdot 3$ & $2^2 \cdot 3$ \\
\hline
$W(L)$ & ${\mathbf{Z}}_2^n \rtimes S_n$ & ${\mathbf{Z}}_2^n \rtimes S_n$ & $W(F_4)$ & $W(G_2)$ \\
\hline
$|W(L)|$ & $2^n \cdot n!$ & $2^n n!$ & $2^7 \cdot 3^2$ & $2^2 \cdot 3$ \\
\hline
$A_L$ & ${\mathbf{Z}}_2$ & ${\mathbf{Z}}_2$ & $\{0\}$ & ${\mathbf{Z}}_3$ \\
\hline
$\operatorname{disc}(L)$ & $2$ & $2$ & $1$ & $3$ \\
\hline
\end{tabular}
\end{center}

We now record explicit representatives for the simple roots of each lattice, their Gram matrix, and the associated Coxeter diagrams:

#### Types A,B,C, D

`\begin{align*} A_n:\,\,
\begin{cases}
\alpha_1 &= e_1 - e_2 \\
\alpha_2 &= e_2-e_3 \\
\vdots & \vdots \\
\alpha_n &= e_n - e_{n+1},
\end{cases}
\quad G_{A_n} &=
\begin{pmatrix}
2 & -1 & \cdot & \cdots & \cdot \\
-1 & 2 & \ddots & \cdots & \cdot \\
\cdot & \ddots & \ddots & \ddots & \vdots \\
\vdots & \cdots & \ddots & 2 & -1 \\
\cdot & \cdots & \cdot & -1 & 2
\end{pmatrix} \\
& \hspace{-8em}
\raisebox{0.75em}{$A_n$:\,\,} \dynkin[mark=o, labels={\alpha_1,\alpha_2,,\alpha_n}, label directions={above,above,,above}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] A{} \[1em]
B_n:\,\,
\begin{cases}
\alpha_1 &= e_1 - e_2 \\
\alpha_2 &= e_2 - e_3 \\
\vdots & \vdots \\
\alpha_{n-1} &= e_{n-1} - e_n \\
\alpha_n &= e_n
\end{cases},
\quad
G_{B_n} &=
\begin{pmatrix}
2 & -1 & \cdot & \cdot & \cdots & \cdot & \cdot \\
-1 & 2 & \ddots & \cdot & \cdots & \cdot & \cdot \\
\cdot & \ddots & \ddots & \ddots & \cdots & \cdot & \cdot \\
\vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\
\cdot & \cdot & \cdots & \ddots & 2 & -1 \\
\cdot & \cdot & \cdots & \cdot & -1 & 1
\end{pmatrix} \\
& \hspace{-8em} 
\raisebox{0.75em}{$B_n(2)$:\,\,}\dynkin[arrows=false, labels={\alpha_1,\alpha_2,\alpha_{n-1}, \alpha_n}, label directions={above,above,above, above}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] B{**.*o} \[1em]
C_n:\,\,
\begin{cases}
\alpha_1 &= e_1 - e_2 \\
\alpha_2 &= e_2 - e_3 \\
\vdots & \vdots \\
\alpha_{n-1} &= e_{n-1} - e_n \\
\alpha_n &= 2e_n,
\end{cases}
\quad
G_{C_n} &=
\begin{pmatrix}
2 & -1 & \cdot & \cdot & \cdots & \cdot \\
-1 & 2 & \ddots & \cdot & \cdots & \cdot  \\
\cdot & \ddots & \ddots & \ddots & \cdots & \cdot \\
\vdots & \vdots & \ddots & 2 & -1 & \vdots  \\
\cdot & \cdot & \cdots & -1 & 2 & -2 \\
\cdot & \cdot & \cdots & \cdot & -2 & 4
\end{pmatrix} \\
& \hspace{-8em} 
\raisebox{0.75em}{$C_n$:\,\,}\dynkin[arrows=false, labels={\alpha_1,\alpha_2,\alpha_{n-1}, \alpha_n}, label directions={above,above,above, above}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] C{oo.o*} \[1em]
\end{align*}`{=tex}

`\begin{align*}
D_n:\,\,\begin{cases}
\alpha_1 &= e_1 - e_2 \\
\alpha_2 &= e_2 - e_3 \\
\vdots & \vdots \\
\alpha_{n-2} &= e_{n-2} - e_{n-1} \\
\alpha_{n-1} &= e_{n-1} - e_n \\
\alpha_n &= e_{n-1} + e_n
\end{cases},
\quad
G_{D_n} &=
\begin{pmatrix}
2 & -1 & \cdot & \cdot & \cdots & \cdot & \cdot & \cdot \\
-1 & 2 & \ddots & \cdot & \cdots & \cdot & \cdot & \cdot \\
\cdot & \ddots & \ddots & \ddots & \cdots & \cdot & \cdot & \cdot \\
\vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots & \vdots \\
\cdot & \cdot & \cdots & \ddots & 2 & -1 & -1 \\
\cdot & \cdot & \cdots & \cdot & -1 & 2 & \cdot \\
\cdot & \cdot & \cdots & \cdot & -1 & \cdot & 2
\end{pmatrix} \\
& \hspace{-8em}
\raisebox{0.75em}{$D_n$:\,\,}
\dynkin[labels={\alpha_1,\alpha_2,\alpha_{n-2},\alpha_{n-1}, \alpha_{n}}, label directions={above,above,above left,above right,below right}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] D{oo.ooo} \[1em]
%
\hline \\
E_6:\,\,
\begin{cases}
\alpha_1 &= \tfrac{1}{2}(e_1 - e_2 - e_3 - e_4 - e_5 - e_6 - e_7 + e_8) \\
\alpha_2 &= e_1 + e_2 \\
\alpha_3 &= -e_1 + e_2 \\
\alpha_4 &= -e_2 + e_3 \\
\alpha_5 &= -e_3 + e_4 \\
\alpha_6 &= -e_4 + e_5,
\end{cases}
\quad
G_{E_6} &=
\begin{pmatrix}
2 & \cdot & -1 & \cdot & \cdot & \cdot \\
\cdot & 2 & \cdot & -1 & \cdot & \cdot \\
-1 & \cdot & 2 & -1 & \cdot & \cdot \\
\cdot & -1 & -1 & 2 & \ddots & \cdot \\
\cdot & \cdot & \cdot & \ddots & \ddots & -1 \\
\cdot & \cdot & \cdot & \cdot & -1 & 2
\end{pmatrix} \\
& \hspace{-16em}
\raisebox{0.75em}{$E_6$:\,\,}
\dynkin[mark=o, labels={\alpha_1,\alpha_2,\alpha_3,\alpha_4,\alpha_5,\alpha_6}, label directions={below,above,below,below,below,below}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] E6 & \[1em]
\end{align*}`{=tex}

#### Type E

`\begin{align*}
E_7:\,\,
\begin{cases}
\alpha_1 &= \tfrac{1}{2}(e_1 - e_2 - e_3 - e_4 - e_5 - e_6 - e_7 + e_8) \\
\alpha_2 &= e_1 + e_2 \\
\alpha_3 &= -e_1 + e_2 \\
\alpha_4 &= -e_2 + e_3 \\
\alpha_5 &= -e_3 + e_4 \\
\alpha_6 &= -e_4 + e_5 \\
\alpha_7 &= -e_5 + e_6
\end{cases},
\quad
G_{E_7} &=
\begin{pmatrix}
2 & \cdot & -1 & \cdot & \cdot & \cdots & \cdot \\
\cdot & 2 & \cdot & -1 & \cdot & \cdots & \cdot \\
-1 & \cdot & 2 & -1 & \cdot & \cdots & \cdot \\
\cdot & -1 & -1 & 2 & -1 & \cdots & \cdot \\
\cdot & \cdot & \cdot & -1 & 2 & \ddots & \vdots \\
\vdots & \vdots & \vdots & \vdots & \ddots & \ddots & -1 \\
\cdot & \cdot & \cdot & \cdot & \cdots & -1 & 2
\end{pmatrix} \\
& \hspace{-16em}
\raisebox{0.75em}{$E_7$:\,\,}
\dynkin[mark=o, labels={\alpha_1,\alpha_2,\alpha_3,\alpha_4,\alpha_5,\alpha_6,\alpha_7}, label directions={below,above,below,below,below,below,below}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] E7 &\[1em]
%
\hline \\
E_8:\,\,
\begin{cases}
\alpha_1 &= \tfrac{1}{2}(e_1 - e_2 - e_3 - e_4 - e_5 - e_6 - e_7 + e_8) \\
\alpha_2 &= e_1 + e_2 \\
\alpha_3 &= -e_1 + e_2 \\
\alpha_4 &= -e_2 + e_3 \\
\alpha_5 &= -e_3 + e_4 \\
\alpha_6 &= -e_4 + e_5 \\
\alpha_7 &= -e_5 + e_6 \\
\alpha_8 &= -e_6 + e_7
\end{cases},
\quad
G_{E_8} &=
\begin{pmatrix}
2 & \cdot & -1 & \cdot & \cdot & \cdots & \cdot \\
\cdot & 2 & \cdot & -1 & \cdot & \cdots & \cdot \\
-1 & \cdot & 2 & -1 & \cdot & \cdots & \cdot \\
\cdot & -1 & -1 & 2 & -1 & \cdots & \cdot \\
\cdot & \cdot & \cdot & -1 & 2 & \ddots & \vdots \\
\vdots & \vdots & \vdots & \vdots & \ddots & \ddots & -1 \\
\cdot & \cdot & \cdot & \cdot & \cdots & -1 & 2
\end{pmatrix} \\
& \hspace{-16em}
\raisebox{0.75em}{$E_8$:\,\,}
\dynkin[mark=o, labels={\alpha_1,\alpha_2,\alpha_3,\alpha_4,\alpha_5,\alpha_6,\alpha_7,\alpha_8}, label directions={below,above,below,below,below,below,below,below}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] E8 
\end{align*}`{=tex}

#### Types F and G

`\begin{align*}
F_4:\,\,
\begin{cases}
\alpha_1 &= e_2 - e_3 \\
\alpha_2 &= e_3 - e_4 \\
\alpha_3 &= e_4 \\
\alpha_4 &= \frac{1}{2}(e_1 - e_2 - e_3 - e_4),
\end{cases}
\quad
G_{F_4} &=\begin{pmatrix}
2 & -1 & \cdot & \cdot \\
-1 & 2 & -1 & \cdot \\
\cdot & -1 & 1 & -\frac{1}{2} \\
\cdot & \cdot & -\frac{1}{2} & 1
\end{pmatrix} \\
& \hspace{-8em}
\raisebox{0.75em}{$F_4(2)$:\,\,}
\dynkin[arrows=false, labels={\alpha_1,\alpha_2,\alpha_3,\alpha_4}, label directions={above,above,above,above}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] F{**oo} \[1em]
%
\hline \\
G_2:\,\,
\begin{cases}
\alpha_1 &= e_2 - e_3 \\
\alpha_2 &= e_1 - 2e_2 + e_3,
\end{cases}
\quad
G_{G_2} &=\begin{pmatrix}
2 & -3 \\
-3 & 6
\end{pmatrix} \\
& \hspace{-8em}
\raisebox{0.75em}{$G_2$:\,\,}\dynkin[arrows=false, labels={\alpha_1,\alpha_2}, label directions={above,above}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] G{*o}
\end{align*}`{=tex}
::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::: {#refs .references .csl-bib-body .hanging-indent entry-spacing="0"}
::: {#ref-Ale96a .csl-entry}
Alexeev, Valery.
1996. "Moduli Spaces m~g,n~(W) for Surfaces." In _Higher-Dimensional Complex Varieties (Trento, 1994)_, 1--22.
Berlin: de Gruyter.
:::

::: {#ref-ABE22 .csl-entry}
Alexeev, Valery, Adrian Brunyate, and Philip Engel.
2022. "Compactifications of Moduli of Elliptic K3 Surfaces: Stable Pair and Toroidal." _Geometry & Topology_ 26 (8): 3525--88.
<https://doi.org/10.2140/gt.2022.26.3525>.
:::

::: {#ref-AE22 .csl-entry}
Alexeev, Valery, and Philip Engel.
2022. "Compactifications of Moduli Spaces of K3 Surfaces with a Nonsymplectic Involution." <https://arxiv.org/abs/2208.10383>.
:::

::: {#ref-AE23 .csl-entry}
---------.
2023. "Compact Moduli of K3 Surfaces." _Annals of Mathematics_ 198 (2): 727--89.
<https://doi.org/10.4007/annals.2023.198.2.5>.
:::

::: {#ref-AEH21 .csl-entry}
Alexeev, Valery, Philip Engel, and Changho Han.
2022. "Compact Moduli of K3 Surfaces with a Nonsymplectic Automorphism." arXiv.
<https://doi.org/10.48550/arXiv.2110.13834>.
:::

::: {#ref-AET23 .csl-entry}
Alexeev, Valery, Philip Engel, and Alan Thompson.
2023. "Stable Pair Compactification of Moduli of K3 Surfaces of Degree 2." _Journal Fur Die Reine Und Angewandte Mathematik_ 799: 1--56.
<https://doi.org/10.1515/crelle-2023-0011>.
:::

::: {#ref-AW71 .csl-entry}
Artin, M., and G.
Winters.
1971. "Degenerate Fibers and Stable Reduction of Curves." _Topology_ 10: 373--83.
<https://doi.org/10.1016/0040-9383(71)90028-0>.
:::

::: {#ref-AMRT75 .csl-entry}
Ash, A., D.
Mumford, M.
Rapoport, and Y.
Tai.
1975. _Smooth Compactification of Locally Symmetric Varieties_.
Lie Groups: History, Frontiers and Applications, Vol.
IV.
Math Sci Press, Brookline, Mass.
:::

::: {#ref-BB66 .csl-entry}
Baily, W.
L., Jr., and A.
Borel.
1966. "Compactification of Arithmetic Quotients of Bounded Symmetric Domains." _Annals of Mathematics_ 84 (3): 442--528.
<https://doi.org/10.2307/1970457>.
:::

::: {#ref-CDL24 .csl-entry}
Cossec, Cdl20]cdl20 F., I.
Dolgachev, and C.
Liedtke.
2024. "Enriques Surfaces I." <https://doi.org/NA>.
:::

::: {#ref-Cos83 .csl-entry}
Cossec, Francois R.
1983. "Projective Models of Enriques Surfaces." _Mathematische Annalen_ 265 (3): 283--334.
<https://doi.org/10.1007/BF01456021>.
:::

::: {#ref-Del71 .csl-entry}
Deligne, Pierre.
1971. "Théorie De Hodge.
II." _Inst.
Hautes Études Sci.
Publ.
Math._, no.
40: 5--57.
<https://doi.org/10.1007/BF02684692>.
:::

::: {#ref-DM69 .csl-entry}
Deligne, P., and D.
Mumford.
1969. "The Irreducibility of the Space of Curves of Given Genus." _Inst.
Hautes Études Sci.
Publ.
Math._, no.
36: 75--109.
:::

::: {#ref-Enr06 .csl-entry}
Enriques, Federigo.
1906. _Sopra Le Superficie Algebriche Di Bigenere Uno Memoria_.
Roma: Salviucci.
:::

::: {#ref-FM13 .csl-entry}
Farkas, Gavril, and Ian Morrison.
2013. _Handbook of Moduli_.
Somerville, MA, Beijing, China: International Press ; Higher Education Press of China.
:::

::: {#ref-Fri83 .csl-entry}
Friedman, Robert.
1983a.
"Base Change, Automorphisms, and Stable Reduction for Type III K3 Surfaces." In _The Birational Geometry of Degenerations (Cambridge, Mass., 1981)_, 29:277--98.
Progr.
Math.
Birkhäuser, Boston, Mass.
:::

::: {#ref-Fri83a .csl-entry}
---------.
1983b.
"Global Smoothings of Varieties with Normal Crossings." _Annals of Mathematics_ 118 (1): 75--114.
<https://doi.org/10.2307/2006955>.
:::

::: {#ref-Fri15 .csl-entry}
---------.
2015. "On the Geometry of Anticanonical Pairs." _Preprint_.
<https://doi.org/10.48550/arXiv.1502.02560>.
:::

::: {#ref-FM83 .csl-entry}
Friedman, Robert, and Rick Miranda.
1983. "Smoothing Cusp Singularities of Small Length." _Mathematische Annalen_ 263 (2): 185--212.
<https://doi.org/10.1007/BF01456880>.
:::

::: {#ref-FS86 .csl-entry}
Friedman, Robert, and Francesco Scattone.
1986. "Type III Degenerations of K3 Surfaces." _Inventiones Mathematicae_ 83 (1): 1--39.
<https://doi.org/10.1007/BF01388751>.
:::

::: {#ref-Kol23 .csl-entry}
Kollár, János.
2023. "Arthur Byron Coble, 1878--1966." arXiv.
<https://doi.org/10.48550/arXiv.2306.05940>.
:::

::: {#ref-KM98 .csl-entry}
Kollár, Janos, and Shigefumi Mori.
1998. _Birational Geometry of Algebraic Varieties_.
Cambridge Tracts in Mathematics.
Cambridge: Cambridge University Press.
<https://doi.org/10.1017/CBO9780511662560>.
:::

::: {#ref-KS88 .csl-entry}
Kollár, J., and N.
I.
Shepherd-Barron.
1988. "Threefolds and Deformations of Surface Singularities." _Inventiones Mathematicae_ 91 (2): 299--338.
<https://doi.org/10.1007/BF01389370>.
:::

::: {#ref-KS06 .csl-entry}
Kontsevich, Maxim, and Yan Soibelman.
2006. "Affine Structures and Non-Archimedean Analytic Spaces." In _The Unity of Mathematics_, 244:321--85.
Progr.
Math.
Boston, MA: Birkhäuser Boston.
:::

::: {#ref-Kul77 .csl-entry}
Kulikov, Vik.
S.
1977. "Degenerations of K3 Surfaces and Enriques Surfaces." _Izv.
Akad.
Nauk SSSR Ser.
Mat._ 41 (5): 1008--42, 1199. <https://doi.org/10.1070/IM1977v011n05ABEH001753>.
:::

::: {#ref-Loo85 .csl-entry}
Looijenga, Eduard.
1985. "Semi-Toric Partial Compactifications I." _Nijmegen Preprint Series_, 1--76.
:::

::: {#ref-Loo03 .csl-entry}
---------.
2003. "Compactifications Defined by Arrangements.
I.
The Ball Quotient Case." _Duke Mathematical Journal_ 118 (1): 151--87.
<https://doi.org/10.1215/S0012-7094-03-11816-5>.
:::

::: {#ref-Mil58 .csl-entry}
Milnor, John W.
1958. "On Simply-Connected 4-Manifolds." In _Symp.
Int.
De Top.
Alg.
Mexico_, 122--28.
<https://doi.org/NA>.
:::

::: {#ref-MM83 .csl-entry}
Miranda, Rick, and David R.
Morrison.
1983. "The Minus One Theorem." In _The Birational Geometry of Degenerations (Cambridge, Mass., 1981)_, 29:173--259.
Progr.
Math.
Birkhäuser Boston, Boston, MA.
<https://mathscinet-ams-org.proxy-remote.galib.uga.edu/mathscinet-getitem?mr=690266>.
:::

::: {#ref-Nam85 .csl-entry}
Namikawa, Yukihiko.
1985. "Periods of Enriques Surfaces." _Mathematische Annalen_ 270 (2): 201--22.
<https://doi.org/10.1007/BF01456182>.
:::

::: {#ref-Nik79 .csl-entry}
Nikulin, V.
V.
1979a.
"Finite Groups of Automorphisms of Kählerian K3 Surfaces." _Trudy Moskov.
Mat.
Obshch._ 38: 75--137.
:::

::: {#ref-Nik79a .csl-entry}
---------.
1979b.
"Integer Symmetric Bilinear Forms and Some of Their Geometric Applications." _Izv.
Akad.
Nauk SSSR Ser.
Mat._ 43 (1): 111--77, 238.
:::

::: {#ref-Nik79b .csl-entry}
---------.
1979c.
"Quotient-Groups of Groups of Automorphisms of Hyperbolic Forms of Subgroups Generated by 2-Reflections." _Doklady Akademii Nauk SSSR_ 248 (6): 1307--9.
:::

::: {#ref-Nik80 .csl-entry}
---------.
1980. "Integral Symmetric Bilinear Forms and Some of Their Applications." _Mathematics of the USSR-Izvestiya_ 14 (1): 103. <https://doi.org/10.1070/IM1980v014n01ABEH001060>.
:::

::: {#ref-Par91 .csl-entry}
Pardini, Rita.
1991. "Abelian Covers of Algebraic Varieties." _Journal Fur Die Reine Und Angewandte Mathematik_ 417: 191--213.
<https://doi.org/10.1515/crll.1991.417.191>.
:::

::: {#ref-PP81 .csl-entry}
Persson, Ulf, and Henry Pinkham.
1981. "Degeneration of Surfaces with Trivial Canonical Bundle." _Annals of Mathematics_ 113 (1): 45--66.
<https://doi.org/10.2307/1971133>.
:::

::: {#ref-PS24 .csl-entry}
Peters, Chris A.
M., and Hans J.
M.
Sterk.
2024. "Symmetric and Quadratic Forms, with Applications to Coding Theory, Algebraic Geometry and Topology." _Symmetric and Quadratic Forms, with Applications to Coding Theory, Algebraic Geometry and Topology_.
:::

::: {#ref-Sca87 .csl-entry}
Scattone, Francesco.
1987. "On the Compactification of Moduli Spaces for Algebraic K3 Surfaces." _Memoirs of the American Mathematical Society_ 70 (374): x+86.
<https://doi.org/10.1090/memo/0374>.
:::

::: {#ref-Ser73 .csl-entry}
Serre, Jean-Pierre.
1973. _A Course in Arithmetic_.
Vol.
7. Graduate Texts in Mathematics.
New York, NY: Springer.
<https://doi.org/10.1007/978-1-4684-9884-4>.
:::

::: {#ref-Sha81 .csl-entry}
Shah, Jayant.
1981. "Degenerations of K3 Surfaces of Degree 4." _Transactions of the American Mathematical Society_ 263 (2): 271--308.
<https://doi.org/10.2307/1998352>.
:::

::: {#ref-Ste91 .csl-entry}
Sterk, Hans.
1991. "Compactifications of the Period Space of Enriques Surfaces.
I." _Mathematische Zeitschrift_ 207 (1): 1--36.
<https://doi.org/10.1007/BF02571372>.
:::

::: {#ref-Sym03 .csl-entry}
Symington, Margaret.
2002. "Four Dimensions from Two in Symplectic Topology." arXiv.
<https://doi.org/10.48550/arXiv.math/0210033>.
:::

::: {#ref-Vin72 .csl-entry}
Vinberg, È.
B.
1972. "The Groups of Units of Certain Quadratic Forms." _Mat.
Sb.
(N.S.)_ 87(129): 18--36.
<https://doi.org/10.1070/sm1972v016n01abeh001346>.
:::

::: {#ref-Vin75 .csl-entry}
---------.
1975. "Some Arithmetical Discrete Groups in Lobacevski Spaces." In _Discrete Subgroups of Lie Groups and Applications to Moduli (Internat.
Colloq., Bombay, 1973)_, No.
7:323--48.
Tata Inst.
Fundam.
Res.
Stud.
Math.
Published for the Tata Institute of Fundamental Research, Bombay by Oxford University Press, Bombay.
:::
:::::::::::::::::::::::::::::::::::::::::::::::
\end{pmatrix}
