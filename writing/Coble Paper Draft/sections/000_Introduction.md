# Introduction 

:::{.remark}
A Coble surface is a smooth projective rational surface $S$ with $\abs{-K_S} = \emptyset$ but $\abs{-2K_S}\neq \emptyset$.
Such surfaces arise from the work of \cite{Cob19} and \cite{Cob29} on Cremona transformations of $\PP^2$ preserving an irreducible rational sextic $C$ with ten nodes -- the blowup $S$ along these nodes yields a Coble surface. \cite{Cob19} shows that the Cremona class of such a curve $C$ can be written as a union of finitely many projective equivalence classes, and that if $C$ is sufficiently general then $\Aut(S) \cong W(E_{10})$, the Weyl group of an infinite root system of type $E_{10}$.
 Moreover, he shows that that modulo $\Aut(S)$, there are only finitely many smooth rational negative curves on $S$.

Coble surfaces occur as degenerations of Enriques surfaces and were ultimately classified in \cite{DZ99}.
As such, they are intimately tied to the theory of algebraic K3 surfaces equipped with a nonsymplectic involution, which were classified by \cite{nikulin1979quotient-groups}. For a reduced plane sextic $C$, the double cover of $S$ branched along the proper transform of $C$ is a K3 surface $X$ which can be realized as a degeneration of the universal double cover of an Enriques surface, where $X$ acquires an $A_1$ singularity fixed by the Enriques involution. The resulting quotient has a quartic singularity whose resolution is an irreducible smooth rational curve $\tilde C$ satisfying $\tilde C^2 = -4$, and thus by \cite[\S 3]{Nue16} is a Coble surface.

We will be interested in Coble surfaces in the strong sense, where $\abs{-2K_S} = \ts{C_1 + \cdots + C_n}$ is a single reduced divisor comprised of $n$ disjoint smooth rational curves referred to as *boundary components* of $S$.
It is known that $1\leq n\leq 10$, and for each such $n$, there is a moduli space $F_{\Co, n}$ of Coble surfaces with $n$ boundary components.
When $n=1$, the moduli space $F_{\Co} \da F_{\Co, 1}$ of Coble surfaces can be described as a boundary divisor $\cH_{-2}$ in the 10-dimensional moduli space $F_{\En}$ of unpolarized Enriques surfaces, and thus $F_{\Co}$ is 9-dimensional.
Moreover, $F_{\Co}$ was shown to be rational in \cite{DK13} via a comparison to a moduli space of cuspidal plane quintics.
A natural question is whether or not $F_{\Co}$ admits a geometrically meaningful, modular compactification $\overline{F_{\Co}}$, and if so, if the boundary $\partial \overline{F_{\Co}}$ can be described and classified.
Toward this end, we turn to the stable pair compactifications of Kollár, Shepherd-Barron, and Alexeev \cite{kollar1988threefolds-and-deformations,alexeev1996moduli-spaces,Kol23}.
:::

:::{.remark}
The search for modular compactifications of moduli spaces is a central problem in algebraic geometry. 
The prototypical example stems from the work of \cite{deligne1969the-irreducibility-of-the-space, knudsen1976the-projectivity-of-the-moduli,knudsen1983the-projectivity-of-the-moduli23} on the Deligne-Mumford-Knudsen compactification $\overline{\Mgn}$ of the moduli space of stable pointed curves $\Mgn$. 
By \cite{mumford1965git, namikawa1976a-new-compactification-of-the-siegel1, alexeev1999on-mumfords-construction, alexeev2002complete-moduli}, a similarly modular compactification $\overline{\Ag}$ of the moduli space $\Ag$ of principally polarized abelian varieties via stable pairs exists, the normalization of which coincides with a particular choice of toroidal \cite{AMRT75} compactification by the work of \cite{kollar1988threefolds-and-deformations} and \cite{alexeev1996moduli-spaces}.
By \cite{PSS71}, the coarse moduli space $F_{2d}$ of primitively polarized K3 surfaces of degree $2d$ is isomorphic to an arithmetic quotient $D_{L_{2d}}/\Gamma_{L_{2d}}$ of a Type IV Hermitian symmetric domain associated to a lattice $L_{2d}$, where $D_{L_{2d}}$ is a period domain classifying Hodge structures of K3 type and $\Gamma_{L_{2d}}$ is an arithmetic subgroup of the orthogonal group $\Orth(L_{2d})$.
By \cite{BB66}, such domains admit a Baily-Borel compactification which is a projective variety. For $F_{2d}$ and related lattice-polarized moduli spaces $F_S$ of K3 surfaces, the boundary of the compactification consists of a configuration of 0-cusps (points) and 1-cusps (curves), see \cite{scattone1987on-the-compactification-of-moduli}.
By \cite{AMRT75}, there additionally exist infinitely many toroidal compactifications described by a choice of fans at each cuspidal point of the Baily-Borel compactification.
The work of \cite{looijenga1985semi-toric} on semitoroidal compactifications simultaneously generalizes the Baily-Borel and toroidal compactifications, retaining the advantage that the boundary can be understood in terms of semifans and studied using toric geometry.

Semitoroidal compactifications are advantageous due to their explicit and combinatorial nature, but do not a priori carry a clear modular interpretation along the boundary strata. 
Alternatively, letting $(S, R)$ be a pair consisting of a surface and a suitably chosen divisor, the work of \cite{kollar1988threefolds-and-deformations,alexeev1996moduli-spaces,Kol23} yields a compactification obtained by taking the closure of pairs $(S, \varepsilon R)$ in the space of KSBA stable pairs. Although KSBA compactifications admit strong modular interpretations, their boundary strata are generally quite difficult to describe. A recent strategy employed in \cite{alexeevCompactificationsModuliElliptic2023,AET23,AE22,AEGS23} is to simultaneously leverage the advantages of both semitoric and KSBA compactifications by finding comparison morphisms between them. This allows the modular boundary of the KSBA compactification to be studied and classified using the combinatorics of toric geometry, lattice theory, and critically, advances in integral affine geometry and mirror symmetry.

The moduli space $F_\Co$ of Coble surfaces with $n=1$ boundary components admits a Hodge-theoretic period domain description of the form $D(T_\Co)/\Gamma_\Co$ where $T_\Co$ is a fixed lattice and $\Gamma_\Co \da \Orth(T_\Co)$ is its orthogonal group. Its Baily-Borel compactification $\overline{F_{\Co}}^{\bb}$ contains only one 0-cusp $p_0$, and thus the combinatorial data of a semitoroidal compactification is determined by a single $\Gamma_\Co\dash$invariant semifan associated to a lattice at $p_0$. A canonical choice one can take is the Coxeter fan, formed by a fundamental domain of the action of the lattice's Weyl group, along with its reflections.
Perhaps more naturally, one can also search for a semifan $\cF$ such that the resulting compactification $\overline{F_\Co}^{\cF}$ is isomorphic to the KSBA compactification $\overline{F_\Co}$ for a suitably chosen divisor, and indeed this is what we do in this paper.
To this end, we prove the following:
:::

:::{.theorem}
There is a semifan $\cF$ such that there exists a morphism
\[
\Psi: (\overline{F_\Co})^{\nu} \to \overline{F_\Co}^{\cF}
\]
from the normalization of the KSBA compactification to the semitoroidal compactification associated with $\cF$.
The Coxeter fan of $T_{\Co}$ is a refinement of $\cF$, and stable Coble surfaces in the boundary of $\overline{F_\Co}$ admit explicit descriptions in terms of surfaces associated to sub-Dynkin diagrams of Coxeter diagrams.
:::

:::{.remark}
This result is made possible by recent advances in \cite{AE22,alexeev2021nonsymplectic} on compactifications of K3 surfaces with nonsymplectic automorphisms, along with the theory of recognizable divisors developed in \cite{alexeev2023compact}.
We also critically leverage the related stable pair compactification of the moduli spaces of Enriques surfaces studied in \cite{AEGS23}. In particular, we use the folding theory of Coxeter diagrams, their associated integral affine structures, and the theory of $ADE+BC$ surfaces in order to explicitly describe stable degenerations of Coble surfaces.
:::

**Acknowledgements**. I would like to thank my advisor Valery Alexeev for his guidance and support throughout this project. I thank Luca Schaffler and Philip Engel for many useful discussions. I would also like to gratefully acknowledge financial support from the Office of the Graduate School of the University of Georgia and the Research and Training Group in Algebra, Algebraic Geometry, and Number Theory at the University of Georgia.
