---
title: "Complete moduli spaces of Coble surfaces"
abstract: "We describe a modular KSBA stable pair compactification of the moduli space of Coble surfaces and compare it to a semitoroidal compactification of the corresponding period domain. We further describe KSBA stable limits in terms of integral affine structures."
---


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

# Coble surfaces 

## The geometry of Coble surfaces

:::{.remark}
For the general theory of Coble surfaces, we refer to \cite{EnriquesOne,EnriquesTwo}, along with \cite{DM19, DZ99, dolgachev2013the-rationality, CD89, CD12, Dol17}.
Following \cite[\S 5.1]{DM19}, a \textbf{Coble surface} is a smooth projective rational surface $S$ with $\abs{-K_S} = \emptyset$ but $\abs{-2K_S} \neq \emptyset$. 
We say $S$ is of **K3 type** if $\abs{-2K_S}$ consists of a single smooth divisor $C = C_1 + \cdots + C_n$, the union of $n$ disjoint smooth rational curves satisfying $C_i\cdot C_j = -4\delta_{ij}$. For Coble surfaces obtained as the blowup along ten nodes of a nodal plane sextic, this calculation follows from adjunction and the genus formula.
We refer to $C$ as the *anti-bicanonical curve* of $S$, and note that $K_S\cdot C_i = -2$.
The $C_i$ are referred to as the **boundary components** of $S$.

By \cite[\S 5.1]{Dol17}, such a Coble surface is known to be a *basic rational surface*, i.e. there is a birational morphism $\pi: S\to \PP^2$. Writing $-K_S^2 = n$, one can decompose $\pi$ as a blowup of $N = 9+n$ points in $\PP^2$. 
It is known that $n\leq 10$, c.f. \cite[Prop.\,9.1.5]{EnriquesTwo}.
The image of $C$ is contained in $\abs{-2K_{\PP^2}} = \abs{\OO_{\PP^2}(6)}$ and is thus generically a nodal plane sextic where the images of $C_i$ are its irreducible components.

We will primarily be interested in the case $n=1$, whence $S$ is obtained as the blowup of a plane sextic along $N=10$ ordinary double points, some of which may be infinitely near to each other.
Such Coble surfaces are not the image of any birational but not biregular morphism from another Coble surface and are said to be \textbf{terminal}. We say $S$ is \textbf{minimal} if the blowdown of any $(-1)$-curve on $S$ is no longer a Coble surface, or equivalently if $S$ does not admit a birational but not biregular morphism onto another Coble surface.
:::

:::{.remark}
Let $\cL \da \OO_S(-K_S) \in \Pic(S)$; By \cite[Prop. 9.1.1]{EnriquesTwo}, taking a section $s\in H^0(\cL ^{\otimes 2})$ with $Z(s) = C$ yields a double branched double cover $f: X\to S$ where $X$ is a smooth K3 surface. By \cite[Def. 5.4.3]{EnriquesOne}, the preimages $f^{-1}(C_i)$ are disjoint $(-2)$-curves and $\Pic(X)$ is a 2-elementary lattice with invariants of the form 
\[
(r,a,\delta)_1 = (10+n, 12-n, \delta)_1
.\] 
By \cite[Def. 5.4.3, Eqn. 5.3.1]{EnriquesOne}, the ramification divisor $R$ is explicitly of one of the following forms:

- $R=\emptyset$ if $(r,a,\delta) = (10, 10, 0)$,
- $R$ is a sum of two elliptic curves if $(r,a,\delta) = (10, 8, 0)$,
- $R$ is the sum of a single rational curve and $n-1$ other disjoint $(-2)$-curves otherwise.

It is also known that $\delta=1$ unless $n=8$, c.f. \cite[Table\, 5.1]{EnriquesOne}.
Thus if $S$ is a terminal Coble surface of K3 type with $n=1$, the ramification locus of the K3 cover is a single smooth rational curve, and we obtain a lattice with invariants 
\[
S_{\Co} \da (11, 11, 1)_1 \cong \gens{-2} \oplus E_{10}(2)
\]
with orthogonal complement 
\[
T_{\Co} \da S_{\Co}^{\perp \lkthree} = (11, 11, 1)_2 \cong \rm{I}_{2, 9}(2) \cong \gens{2} \oplus E_{10}(2)
.\]

Explicitly, $S_{\Co}$ is generated by the preimages $E_i$ for $1\leq i \leq 10$ under $f$ of the ten exceptional divisors of the blowup, along with the preimage $E_0$ under $f$ of the pullback of a hyperplane class of $\PP^2$ under $\pi$.
One can show that $E_0^2=2$ and $E_i^2 = -2$ for $i\geq 1$, and thus these divisors form a lattice of the form 
\[
S_{\Co} \cong \gens{2} \oplus \gens{-2}^{\oplus 10} \cong \rm{I}_{1, 10}(2) \cong (11, 11, 1)_1
,\]
and the identification $S_{\Co} \cong \gens{-2} \oplus E_{10}(2)$ follows from the fact that both definitions of $S_{\Co}$ are 2-elementary lattices of signature $(1, 10)$ with discriminant group $(\bZ/2\bZ)^{11}$, which are classified uniquely up to isometry by their invariants $(r,a,\delta)_{n_+}$.
Similarly, the identification of $T_{\Co}$ follows from the fact that it is again a 2-elementary lattice of signature $(2, 9)$ satisfying $q_{T_{\Co}} \cong -q_{S_{\Co}}$, and the isomorphism class of $q_{T_{\Co}}$ determines $T_{\Co}$ up to isometry.
Alternatively, this can be seen directly using the mirror move $S\leadsto T$ of \cite[Thm. 5.10]{AE22nonsympinv} applied to $S_\Co =(11, 11, 1)_1$ in \cite[Fig.\,1]{AE22nonsympinv}, immediately yielding $T_{\Co} = (11, 11, 1)_2$.


The lattices $S_{\Co}$ and $T_{\Co}$ will be of fundamental importance in constructing the Hodge-theoretic period domain for Coble surfaces, yielding a coarse space for the corresponding moduli space.
:::

:::{.remark}
Following \cite{CD12}, we note that this computation is a special case of a general construction. Let $S$ be any basic rational surface and write $S$ as the blowup of $\PP^2$ at $N$ points $p_1,\cdots, p_N$ with $N\geq 9$.
It is a fact that $\Pic(S) \cong \rm{I}_{1, N}$, since one can construct a **geometric basis** in the following way: let $e_0$ be the class of the total transform of a hyperplane class in $\PP^2$ and for $1\leq i\leq N$, let $e_i$ be the class of the total transform of the exceptional divisor over $p_i$.
Then $\Pic(S) = \gens{e_0,e_1,\cdots, e_N}$ and $\rho(X) = N+1$; one verifies that $e_0^2 = 1$, and for $i\geq 1$, that $e_i^2 = -1$. Moreover $e_ie_j = 0$ for $i\neq j$, making this an orthogonal basis with respect to the intersection pairing, yielding $\rm{I}_{1, N}$.
In the case of Coble surfaces, the effect of taking the K3 double cover is to twist this lattice by 2, yielding $\Pic(X) = \rm{I}_{1, N}(2)$, generated by preimages of the $e_i$.
We remark that
\[
K_S = -3e_0 + e_1 + \cdots + e_N
.\]
:::




# Lattice Theory

:::{.remark}
We refer to:

- \cite{vinberg1985hyperbolic-groups}
- \cite{Vin75}

:::

## Basic Theory

:::{.remark}
The study of semitoroidal compactifications of moduli spaces of Coble surfaces largely reduces to lattice theory, of which we will now recall the essential notions.

:::

:::{.remark title="Basic invariants"}
By a **lattice**, we mean a free $\ZZ$-module $L$ of finite rank equipped with a nondegenerate[^1] symmetric integral bilinear form $\beta_L: L \otimes_\ZZ L \to \ZZ$. 
We abbreviate $vw \da \beta_L(v, w)$ and $v^2 \da \beta_L(v, v)$ and refer to the latter as the \textbf{norm} of $v$. 
We write $L_R \da L\otimes_{\ZZ} R$  and $\beta_{L_R}$ for $R = \QQ, \RR, \CC$ for the $\ZZ$-linear extensions of $(L, \beta_L)$ to the rational, real, and complex numbers respectively. 

A submodule $M\subseteq L$ is a **sublattice** if the restricted bilinear form $\ro{\beta_L}{M}$ endows $M$ with the structure of a lattice. 
A vector $v\in L$ is **isotropic** if $v^2 = 0$, i.e. it is norm zero, and more generally a sublattice $M \subseteq L$ is isotropic if $\ro{\beta_L}{M} \equiv 0$. 
A lattice is said to be **even** if $x^2\in 2\ZZ$ for all $x\in L$, and \textbf{odd} otherwise. 
A nondegenerate symmetric bilinear form can be linearly extended to $L_\RR$ and by Sylvester's theorem, diagonalized with only $1$ or $-1$ on the diagonal. 
We write $n_+$ and $n_-$ respectively for the number of $\pm 1$ entries on the diagonal. 
The **signature** of $L$ is the pair $(n_+, n_-)$, and the **index** is $n_+ - n_-$. 
We say $L$ is **definite** if either $n_+$ or $n_-$ is zero, and **indefinite** otherwise. 
More precisely, if $n_- = 0$ we say $L$ is **positive definite**, and similarly if $n_+ = 0$, we say $L$ is **negative definite**. 
A negative definite lattice generated by elements of norm $-2$ is said to be a **root lattice**, and such elements are referred to as **roots**.

The **rank** $r$ of a lattice is its rank as a free $\ZZ$-module and is given by $r=n_+ + n_- = \dim_\QQ L_\QQ$. 
An indefinite lattice of signature $(1, r-1)$ is said to be **hyperbolic**. 
Fixing a generating set $e_i$ of $L$, we define the **Gram matrix** of $L$ as the matrix $G_L \da (\beta_L(e_i, e_j))_{ij}$, and the **discriminant** as $\operatorname{disc} L \da \det G_L$. 
The discriminant is independent of the choice of generating set.

:::

:::{.remark title="Discriminant forms"}

The **dual lattice** to $L$ is denoted $L\dual \da \Hom_\ZZ(L, \ZZ)$,
and there is an morphism 
$$\begin{aligned}
\iota: L &\injects L\dual \\
x &\mapsto \beta_L(x, \cdot)
\end{aligned}$$ which, if $L$ is nondegenerate, is an injection with
finite index image. The **discriminant group** is
$A_L \da \coker \iota \cong L\dual/L$; this is a finite order group of
order $\abs{\operatorname{disc} L}$. We say $L$ is **unimodular** if any
of the following equivalent conditions hold:

1.  $A_L$ is the trivial group,

2.  $\iota$ is an isomorphism and $L\cong L\dual$,

3.  $\abs{ \operatorname{disc} L} = 1$.

If $A_L \cong (\ZZ/p\ZZ)^a$ for some $a$, we say $L$ is
**$p$-elementary**; in our applications we will often have $p=2$. For
even lattices, the form $\beta_L$ descends to a well-defined quadratic
form $$\begin{aligned}
q_L: A_L &\to \QQ/2\ZZ \\
x + L &\mapsto \beta_{L_\QQ}(x, x) \mod 2\ZZ
\end{aligned}$$ We call the pair $(A_L, q_L)$ the **discriminant
quadratic form** of $L$. A **morphism** between two lattices is a
morphism of $\ZZ$-modules $\eta: L\to L'$ respecting the bilinear forms
in the sense that $\beta_L(x, y) = \beta_{L'}(\eta(x), \eta(y))$, and is
a **primitive embedding** if $\eta$ is injective and $\coker \eta$ is
torsionfree. An **isometry** of lattices is an isomorphism, defined in
the obvious way. We write $\Orth(L)$ for the group of lattice
automorphisms of $L$, denoted the **orthogonal group** of $L$, and
similarly $\Orth(q_L)$ for the $\ZZ$-module automorphisms of of the discriminant form $A_L$ which
preserve the quadratic form. There is a natural group homomorphism
$\Orth(L)\to\Orth(q_L)$, the kernel is denoted $\tilde \Orth(L)$.
:::

:::{.remark title="Orthogonal complements"}

Given two lattices $L_1, L_2$ we write $L_1\oplus L_2$ for the
**orthogonal direct sum**, which is the direct sum of the underlying
modules with bilinear form defined by
$$\beta_{L_1\oplus L_2}(v_1 + v_2, w_1 + w_2)\da \beta_{L_1}(v_1, w_1) + \beta_{L_2}(v_2, w_2) 
.$$ We write $L^{\oplus n}$ for the direct sum of $n$ copies of $L$. Let
$\eta: M \injects L$ be a primitive embedding of lattices, for example
the inclusion of a sublattice. We write
$$M^{\perp L} \da \ts{x\in L \mid \beta_L(x, M) = 0}
.$$ If the ambient lattice $L$ is understood, we often abuse notation
and simply write $M^{\perp}$ without reference to $L$. Note that
$M^{\perp L}\oplus M \subseteq L$ may not be saturated, and is generally a finite index sublattice of $L$.
We note that $M^{\perp L}\intersect M \neq \ts{0}$ in general.[^2]
We also note that for any lattices $L_i$,
\[
A_{L_1 \oplus \cdots \oplus L_n} = A_{L_1} \oplus \cdots \oplus A_{L_n}
\]

:::

:::{.remark title="2-elementary lattices"}
Let $L$ be a 2-elementary lattice. The **divisibility** of a vector
$v\in L$, denoted $\operatorname{div}_L(v)$, is defined by
$\beta_L(v, L) = \operatorname{div}_L(v)\ZZ$, i.e. the positive
integral generator of the image of the map $\beta_L(v, \cdot): L\to \ZZ$. For
2-elementary lattices, one always has
$\operatorname{div}_L(v) \in \ts{1, 2}$. We set
$v^* \da v/\operatorname{div}_L(v)\in A_L$. Letting
$q_L:A_L \to {1\over 2}\ZZ/\ZZ$ be the induced quadratic form on $A_L$,
we say $v^*$ is **characteristic** if $q_L(x) = \beta_L(v^*, x)\mod \ZZ$
for all $x\in A_L$, and is **ordinary** otherwise. We say that a
primitive isotropic vector $e\in L$ is

1.  **odd** if $\operatorname{div}_L(e) = 1$,

2.  **even ordinary** if $\operatorname{div}_L(e) = 2$ and $e^*$ is
    ordinary, or

3.  **even characteristic** if $\operatorname{div}_L(e) = 2$ and $e^*$
    is characteristic.

The 2-elementary hyperbolic lattices admitting a primitive embedding
into $\lkt$ were classified by Nikulin in \cite[\S 3.6.2]{nikulin1979integer-symmetric}. 
An indefinite 2-elementary lattice is determined up to isometry by a triple of invariants $(r,a,\delta)$. Here, $r\da \operatorname{rank}_\ZZ(L)$ is the rank, $a = \operatorname{rank}_{\bF_2}A_L$ is the exponent appearing in $A_L = (\ZZ/2\ZZ)^a$, and $\delta \in \ts{0, 1}$ is the **coparity**:
we set $\delta = 0$ if $q_L(A_L) \subseteq \ZZ$, so
$q_L(x) \equiv 0 \mod \ZZ$ for all $x\in A_L$, and $\delta=1$ otherwise.
We accordingly specify such lattices using the notation
$(r,a,\delta)_{n_+}$.
:::

:::{.remark title="Twists of a lattice"}
If $L$ is a lattice with bilinear for $\beta_L$, define $L(n)$ to be the twist of $L$ by $n$, which has the same underlying $\ZZ$-module but is equipped with the scaled bilinear form 
\[\beta_{L(n)}(v,w) \da n\cdot \beta_L(v, w).\]
:::

:::{.remark title="The lattice $\gens{n}$"}
The lattice $\gens{n}$ is defined as the rank 1 lattice $\ZZ$ with one generator $v$ satisfying $\beta_{\gens{n}}(v,v) = n$. The Gram matrix is the $1\times 1$ matrix $G_{\gens n} = [n]$, and the associated quadratic form is $q_{\gens{n}}(x) = nx^2$. 
:::

:::{.remark title="The hyperbolic lattice"}
In rank 2, there are two unimodular hyperbolic lattices: the odd $\rm{I}_{1, 1} \da \gens{1} \oplus \gens{-1}$, and the even $U\da \rm{II}_{1, 1}$.
We refer to the latter as the \textbf{hyperbolic lattice}, which can be realized as $U \da \ZZ e \oplus \ZZ f$ with $e^2=f^2 = 0$ and $ef = 1$, and thus the following Gram matrix:
\[ 
G_U = \begin{bmatrix}0&1\\1&0\end{bmatrix}
.\]

:::

:::{.remark title="ADE lattices"}
Any Dynkin diagram of type $A_n, D_n, E_6, E_7, E_8$ corresponds to a root lattice of the respective type. By convention, we take the negative definite twists of these lattices. Of particular importance to us is the $E_8$ lattice associated to the following Dynkin diagram:


<!--![](figures/2024-07-24_12-12-27.png)-->

\begin{figure}[H]
\centering
\input{tikz/e8_coxeter_diagram.tikz}
\caption{The Dynkin diagram $E_{8}$}
\label{fig:e8-coxeter-diagram}
\end{figure}

:::

:::{.remark title="The lattice ${{\rm{I} }_{p, q}}$."}
For any pair of non-negative integers $(p, q)$, there exists an odd indefinite unimodular lattice determined up to isomorphism by its rank and signature:
\[
\mathrm{I}_{p, q} \da \gens{1}^{\oplus p}\oplus \gens{-1}^{\oplus q}
.\]

:::

:::{.remark title="The lattice ${\rm{II}}_{p, q}$"}
Let $L$ be an even indefinite unimodular lattice of signature $(p, q)$. Then $p-q\equiv 0 \pmod 8$, and $L$ is uniquely determined up to isomorphism by its rank and signature:
\[ 
{\rm{II}}_{p, q} \da 
\begin{cases}
    U ^{\oplus p}\oplus E_8^{\oplus {q-p\over 8}}, & p < q \\
    U^{\oplus q} \oplus E_8(-1)^{\oplus {p-q\over 8}}, & p > q
.\end{cases}
\]
:::


[^1]: A bilinear form is *nondegenerate* if for any $x$, $\beta_L(x, L) = 0$ implies $x=0$.
[^2]: For example, let $L = U = \gens{e,f}$ and $M = \gens{e}$. Then $M^{\perp L} = M$.



## Summary

:::{.remark}
We summarize the lattices that will be relevant to our discussion:

$$\begin{aligned}
    \lkthree &= (22, 0, 0)_3 = U^3 \oplus E_8^2 = \rm{II}_{3, 19} &
    E_{10} &= (10, 0, 0)_1 = U \oplus E_8 = \mathrm{I}_{1, 9} \\
    S_{\En} &= (10, 10, 0)_1    = E_{10}(2) & 
    T_{\En} &= (12, 10, 0)_2    = U \oplus E_{10}(2) \\
    S_{\Co} &= (11, 11, 1)_1    = \gens{-2} \oplus E_{10}(2) & 
    T_{\Co} &= (11,11,1)_2      = \gens{2} \oplus E_{10}(2) \\
    S_{\dP} &= (2,2,0)_1        = U(2) &
    T_{\dP} &= (20, 2, 0)_2     = U \oplus U(2) \oplus E_8^2
\end{aligned}$$

:::

:::{.lemma}
\label{lem:embedding_eta}
Writing
\begin{align*}
T_{\Co} = \gens{2} \oplus E_{10}(2) &= \langle h, e', f',\alpha_1,\cdots, \alpha_8 \rangle \\
T_{\En} = U \oplus E_{10}(2) &= \langle \tilde e,\tilde f,\tilde e',\tilde f',\tilde \alpha_1,\cdots,\tilde \alpha_8\rangle,
\end{align*}
there is an embedding of lattices $T_{\Co} \injects T_{\En}$:
\begin{align*}
    \eta: \gens{2} \oplus E_{10}(2) &\to U \oplus E_{10}(2) \\
    (h, x) &\mapsto (\tilde e + \tilde f, x)
\end{align*}
which sends the generator $h$ of $\gens{2}$ to $\tilde e+\tilde f\in U$ and is the identity on the $E_{10}(2)$ summand. Since $\coker \eta$ is torsionfree, $\eta$ is a primitive embedding.
:::

:::{.lemma}
There is a sequence of primitive embeddings
\[
T_{\Co} \injects T_{\En} \injects T_{\dP} \injects \lkthree
\]  
which is unique up to $\Orth(\lkthree)$. In particular, this yields an embedding $T_{\Co}\injects T_{\dP}$ given by
\begin{align*}
    \gens{2} \oplus U(2) \oplus E_8(2) &\injects U \oplus U(2) \oplus E_8^2 \\
    (h,x,y) & \mapsto (\tilde e + \tilde f, x, y, y)
\end{align*}
and thus an embedding $F_{\Co} \injects F_{(2,2,0)}$.
:::

:::{.proof}
By \cite[Lem.\,2.4]{AEGS23}, it suffices to show uniqueness of $S_{\En} \injects S_{\Co}$, i.e.
\[
E_{10}(2) \injects \gens{-2}\oplus E_{10}(2)
,\]
or equivalently by untwisting,
\[
E_{10} \injects \gens{-1}\oplus E_{10}
.\]
This embedding is unique since one can write the codomain as $E_{10}^\perp \oplus E_{10}$. Similarly, by \cite[Cor.\,1.5.2, Thm.\,3.6.3]{nikulin1979integer-symmetric}, the homomorphism $\Orth(L)\to \Orth(T_{\Co})$ is surjective.
:::

:::{.lemma}
\label{lem:lattice-embeddings-induce-morphisms}
The embeddings of lattices $\eta: T_{\Co}\injects T_{\En}$ (resp. $T_{\Co} \injects T_{\dP}$) induce locally closed embedding $F_{\Co} \injects F_{\En}$ (resp. $F_{\Co} \injects F_{(2,2,0)}$) which extend to morphisms on the Baily-Borel compactifications.
:::

:::{.proof}
This follows from \cite[\S 5, Thm.\,2]{kiernan1972satake-compactification}.
:::

:::{.theorem}
$F_{\Co}$ is the normalization of a closed subvariety of $F_{\En}$.
:::

:::{.proof}
It suffices to show that $D(T_{\Co})/\Orth(T_{\Co}) \to D(T_{\En})/\Orth(T_{\En})$ is a finite morphism which is generically injective. 
The lattice embedding $T_{\Co}\injects T_{\En}$ induces an injective morphism $D(T_{\Co}) \injects D(T_{\En})$.
It remains to show that the stabilizer of $T_{\Co}$ in $\Orth(T_{\En})$ is precisely $\Orth(T_{\Co})$ and the morphism is finite.

This morphism is finite because...

The stabilizer statement follows from...


:::

\todo[inline]{I don't know how to prove this. Maybe one should embed into $T_{\dP}$ instead to get the stabilizer statement? Finiteness is still unclear. Maybe one can use finite $\iff$ proper and finite fibers, using Stacks tag 02LS. This can be checked Zariski locally?}

\todo[inline]{Maybe this can be proved using Zariski's main theorem: a birational morphism to a normal variety with finite fibers is an isomorphism onto an open subset. Is this morphism birational? What are the fibers, and how can we tell if they are finite?}





## Moduli of Coble Surfaces

:::{.remark}
We begin with a naive parameter space for Coble surfaces.
Following \cite{DK13}, by varying the coefficients of $p_i$ in the planar blowup construction, one can construct $F_\Co$ as a locally closed subvariety of $(\PP^2)^{10}/\PGL_3$, which is of dimension
\[
\dim (\PP^2)^{10}/\PGL_3 = \dim (\PP^2)^{10} - \dim \PGL_3 = 2\cdot 10 - (3^2-1) = 12
.\]
A posteriori, the number of moduli for a Coble surface is 9, which means that there should be 3 conditions imposed upon the configuration of 10 points. These 3 conditions are precisely the *discriminant conditions* described in \cite[\S 2,\,Prop. (10)]{Cob19}.
Letting $D$ be the corresponding discriminant locus, we can identify $F_{\Co}$ as an open subset of $\qty{ (\PP^2)^{10} \sm D }/\PGL_3$ at the level of coarse moduli spaces.
We note that \cite{DK13} shows that $F_\Co$ is rational by relating it to a codimension one subvariety of a moduli space of certain cuspidal quintics in $\PP^2$.
:::

:::{.remark}
Alternatively, Horikawa \cite{Hor78b} and more recently \cite{AEGS23} consider the following: let $Y\da \PP^1\times \PP^1$ and define an involution $\tau(x,y) \da (-x,-y)$. Let $B\in\abs{-2K_{Y}}^\tau$ be a $\tau$-invariant anti-bicanonical curve in $Y$. If $B$ passes through a $\tau$-fixed point $x,y\in \ts{0, \pm \infty}$, then the corresponding double branched cover branched over $B$ is a nodal K3 surface $X$ with covering involution $\iota_{\dP}$ such that $Y = X/\gens{\iota_{\dP}}$. Letting $\iota_{\En}$ be a lift of $\tau$, the quotient $Z\da X/\gens{\iota_{\En}}$ is a Coble surface. The case in which $B$ does not pass through a $\tau$-invariant point yields an Enriques surface $Z$, and an analysis of the corresponding moduli space is carried out in \cite{AEGS23}.
In this way, one realizes the moduli space $F_{\Co}$ of unpolarized Coble surfaces as a boundary divisor in $F_{\En}$, the 10-dimensional moduli space of unpolarized Enriques surfaces.
:::

:::{.remark}
By passing to the K3 cover, one can embed $F_\Co$ into an arithmetic quotient of a 9-dimensional Hermitian symmetric domain of type $\rm{IV}$. Let $\lkt = U^3 \oplus E_8^2$ be the canonical K3 lattice. We recall that for any primitively embedded lattice $S\injects \lkt$, letting $T \da S^{\perp \lkt}$, there is a Hodge-theoretic description of the coarse moduli space $F_S$ of $S$-polarized K3 surfaces given by
\[
F_S \da D_T/\tilde\Orth(T)
\]
where $\tilde \Orth(T) \da \ker\qty{\Orth(T) \to \Orth(q_T)}$ and $D_T$ is a connected component of
\[
\Omega_T \da \ts{[v]\in \PP(T_\CC) \st v^2=0,\, v\bar v > 0}
.\]
Letting $E_{10} \da U \oplus E_8$, one can consider the Enriques lattices $S_{\En} := E_{10}(2)$ with $T_{\En} \da U \oplus E_{10}(2)$. Letting
\[
\cH_{-2d} = \Union_{\delta^2 = -2d} \delta^{\perp D_T}
.\]
We note, as in \cite{DK13}, that $T_{\Co} \cong v^{\perp T_{\En}}$ for some $v^2=-2$, which implies that there is a birational isomorphism $F_{\Co} \birational \cH_{-2}/\Orth(T_{\En})$.
Thus up to birational isomorphism, one can present
\begin{align*}
F_{\En} &= \qty{D_{T_{\En}} \setminus \cH_{-2}} / \tilde \Orth(T_{\En}) \\
F_{\Co} &= \cH_{-2} / \tilde \Orth(T_{\En}) \\
\end{align*}
where surfaces along the divisor $\cH_{-2}$ in $F_{\En}$ correspond precisely to Coble surfaces. We note that surfaces along $\cH_{-4}\setminus \cH_{-2}$ correspond to nodal Enriques surfaces, an interesting divisor in its own right.
:::

:::{.remark}
We summarize the relevant moduli spaces:
\begin{align*}
F_{\En} &= D_{T_{\En}}/\tilde \Orth(T_{\En}) & 
F_{\En, 2} &= D_{T_{\En}}/\Gamma_{\En, 2} \\
F_\Co &= D_{T_{\Co}} / \tilde \Orth(T_{\Co}) & 
F_{\Co, 2} &= D_{T_{\Co}}/\Gamma_{\Co, 2} 
\end{align*}
where
\begin{align*}
\Gamma_{\En, 2} &= \Orth(T_{\En}) \intersect \Orth(T_\dP) \subseteq \Orth(\lkt) \\
\Gamma_{\Co, 2} &= \mathrm{Stab}_{\Orth(T_{\En})}(T_{\Co}) \subseteq \Orth(T_{\En})
\end{align*}
where $T_{\dP}$ is described in \cite{AEGS23}.
Note that we implicitly use the embedding $\eta: T_{\Co} \injects T_{\En}$ of \cref{lem:embedding_eta}.
:::

:::{.remark}
By \cref{lem:lattice-embeddings-induce-morphisms}, there are morphisms $\overline{F_{\Co}}^{\bb} \to \overline{F_{\En}}^{\bb}$ and $\overline{F_{\Co}}^{\bb} \to \overline{F_{(2,2,0)}}^{\bb}$ which induce correspondences between the boundary cusps.
:::

:::{.remark}
We set up the moduli space of KSBA stable pairs for Coble surfaces, possibly using the ramification divisor of the K3 involution (which is in this case not fixed-point free).
The above embeddings should allow us to take closures of stable pairs in already existing moduli spaces.
:::


# Cusp Correspondence

## Coble Cusps

:::{.remark}
We recall the mirror move algorithm from \cite{AE22nonsympinv}.
We have Nikulin's 2-elementary diagram:

\begin{figure}[H]
\centering
\input{tikz/nikulin_table.tikz}
\caption{White nodes are $\delta=0$, black are $\delta=1$, double circled are $\delta = 1,2$.}
\label{fig:nikulin_table}
\end{figure}

:::


:::{.remark}
Having identified the 2-elementary lattice $S_\Co = (11, 11, 0)_1$, one can apply the mirror move algorithm of \cite[Thm. 5.10]{AE22nonsympinv} to determine the 0-cusps and 1-cusps of $F_\Co$.
The outcome of the algorithm is summarized by the following tree:

\begin{figure}[H]
\centering
\input{tikz/mirror-moves-coble.tikz}
\caption{Blue (resp. red) indicate lattices which are valid (resp. invalid) targets of mirror moves.}
\label{fig:unlabeledtwo}
\end{figure}

Thus $F_{\Co}$ has one 0-cusp corresponding to an isotropic vector $v$ with 
\[
v_0^{\perp T_{\Co}}/\gens{v_0} \cong (9,9,1)_1 \cong \gens{2} \oplus E_{8}(2)
.\] 
Moreover, this 0-cusp $v_0$ is incident to one 1-cusp $C_0$ corresponding to an isotropic plane $J = \gens{v_0, v_1}$ with 
\[
J^{\perp T_{\Co}}/\gens{J} \cong (7,7,1)_0 \cong A_1^{\oplus 7}
.\]
where $v_1 \in v_0^{\perp T_{\Co}}/\gens{v_0}$.
In the diagrammatic language of \cite[Fig.\, 1, Thm.\,5.10]{AE22nonsympinv}, this corresponds to a $U^2$ move and can be summarized in the following mirror move diagram as a composition of two even ordinary $U(2)$-type moves:

\begin{figure}[H]
\centering
\input{tikz/mirror-moves-coble-simplified.tikz}
\caption{}
\label{fig:unlabeledthree}
\end{figure}


Note that $v_0$ corresponds to a Type $\rm{III}$ boundary, while $C_0$ corresponds to a type $\rm{II}$ boundary. It is easily verified that the Coxeter diagram $G_{(9,9,1)_1}$ at $v_0$ has precisely one maximal parabolic subdiagram, corresponding to a finite-index root lattice of type $A_7$.
We note that by \cite[\S 5]{AE22nonsympinv}, such isotropic vectors are unique up to $\Orth(T_\Co)$, and so we can choose representatives:

- $v_0 = e'$,
- $v_1 = 2h + \alpha_1 + \alpha_2$.

Calculations verify that $v_0^2 = v_1^2 = 0$, that $v_1 \in v_0^{T_{\Co}}/\gens{v_0}$, and that $v_0v_1 = 0$, and thus $J \da \gens{v_0, v_1}$ is an admissible choice of an isotropic plane.
We further note that $\div_{T_{\Co}}(v_0) = \div_{T_{\Co}}(v_1) = 2$, which will be an important invariant for establishing a correspondence to cusps of other moduli spaces.
For an isotropic plane $J$, we denote the divisibilities of the constituent generating vectors as a tuple $(d_1, d_2)$, and in this convention we have $\div_{T_{\Co}}(v_0, v_1) = (2, 2)$. We summarize this in the following boundary cusp diagram:

% Cusp diagram F_Co
\begin{figure}[H]
\centering
\input{tikz/coble-cusp-diagram-detailed.tikz}
\caption{Cusp diagram for $F_\Co = F_{(11, 11, 1)}$ where $T_\Co = \gens{2} \oplus E_{10}(2)$.}
\label{fig:coble-cusp-diagram}
\end{figure}

:::


:::{.remark}
As further proof that this cusp diagram is correct, we can use the theory of Coxeter diagrams.
Given an isotropic vector $e\in L$ a lattice of signature $(2, n)$, the lattice $e^{\perp L}/\gens{e}$ is a hyperbolic lattice equipped with a root system $R_e$ with a Coxeter diagram $G_e$. Generally, when $e$ corresponds to a 0-cusp in a Baily-Borel compactification, the adjacent 1-cusps correspond precisely to maximal parabolic subdiagrams of $G_e$. The cusp diagram above suggests that the 0-cusp $v_0$ should have a Coxeter diagram $G_{v_0}$ with precisely one maximal parabolic subdiagram. One can run Vinberg's algorithm to determine the Coxeter diagram for $v_0$, and it is a straightforward check to determine that there is indeed a unique maximal parabolic subdiagram of the form $\tilde B_7(2)$:

\begin{figure}[H]
\centering
\input{tikz/coble-coxeter-diagram-maximal-parabolic.tikz}
\caption{The unique maximal parabolic subdiagram $\tilde B_7(2)$ of $(9,9,1)_1$, corresponding to single one-cusp $(7,7,1)_0$ in $F_\Co$.}
\label{fig:coble-cusp-9-9-1-parabolics}
\end{figure}

:::

:::{.remark}
\begin{align*}
\div_{T_{\dP}}(v_0) = 2 &&
\div_{T_{\dP}}(v_1) = 1 
.\end{align*}

The former is clear, since the image of $v_0$ in $T_{\dP}$ is $e'\in U(2)$ and $e'f' = 2$.
The latter follows from the fact that $v_1\alpha_3 = 1$.
:::


:::{.remark}
We note the divisibilities of $v_i$ under various lattice embeddings:

\begin{table}[H]
\centering
\begin{tabular}{|l|l|l|l|l|}
\hline
Coble Vector & Representative & $\mathrm{div}_{T_{\Co}}$ & $\mathrm{div}_{T_{\En}}$ & $\mathrm{div}_{T_{\dP}}$ \\ \hline
$v_0$        & $e'$   & 2                        & 2                        & 2                        \\ \hline
$v_1$        & $2h + \alpha_1 + \alpha_2$   & 2                        & 2                        & 1                        \\ \hline
\end{tabular}
\caption{Isotropic vectors in $F_{\En, 2}$ and their divisibilities.}
\label{tab:sterk-cusps-two}
\end{table}

More concisely:

\begin{table}[H]
\centering
\begin{tabular}{|l|l|l|l|}
\hline
Lattice   & Image of $v_0$ & Image of $v_1$                  & Divisibility \\ \hline
$T_{\Co}$ & $e'$           & $2h + \alpha_1 + \alpha_2$      & $(2, 2)$     \\ \hline
$T_{\En}$ & $e'$           & $2e + 2f + \alpha_1 + \alpha_2$ & $(2, 2)$     \\ \hline
$T_{\dP}$ & $e'$ & $2e + 2f + \alpha_1 + \tilde\alpha_1 + \alpha_2 + \tilde \alpha_2$ & $(2, 1)$ \\ \hline
\end{tabular}
\caption{Isotropic vectors in $F_{\En, 2}$ and their divisibilities.}
\label{tab:coble-cusp-divisibilities}
\end{table}

:::

## Enriques Cusps

:::{.remark}
We recall the cusp diagram of $F_{\En}$:

% Cusp diagram F_En
\begin{figure}[H]
\centering
\input{tikz/enriques-cusp-diagram-detailed.tikz}
\caption{Cusp diagram for $F_{\En} = F_{(10, 10, 0)}$ corresponding to $T_{\En} = U \oplus E_{10}(2)$.}
\label{fig:enriques-cusp-diagram}
\end{figure}

This can be recovered using the mirror move algorithm:

\begin{figure}[H]
\centering
\input{tikz/mirror-moves-enriques-simplified.tikz}
\caption{}
\label{fig:mirror-moves-enriques-simplified}
\end{figure}


:::

:::{.remark}
We recall the Coxeter diagrams and their maximal parabolic subdiagrams at the 0-cusps of $F_{\En}$:

\begin{figure}[H]
\centering
\caption{}
\input{tikz/enriques-cusp-coxeter-diagrams-maximal-parabolics.tikz}
\label{fig:enriques-maximal-parabolics-10-10-0}
\end{figure}

:::

## Sterk Cusps

:::{.remark}
We recall Sterk's cusp diagram for $F_{\En, 2}$:

\begin{figure}[H]
\centering
\input{tikz/sterk-cusp-diagram.tikz}
\caption{Sterk's cusp diagram}
\label{fig:sterk-cusp-diagram}
\end{figure}

We have the following divisibilities in various lattices:

\begin{table}[]
\centering
\begin{tabular}{llll}
\hline
Sterk Cusp & Vector                           & $\mathrm{div}_{T_{\En}}$ & $\mathrm{div}_{T_{\mathrm{K3} } }$ \\ \hline
1          & $e$                              & 1                      & 1                                  \\
2          & $e'$                             & 2                      & 2                                  \\
3          & $e' + f' + \overline{\alpha}_8$  & 2                      & 1                                  \\
4          & $2e' + f' + \overline{\alpha}_1$ & 2                      & 1                                  \\
5          & $2e + 2f + \overline{\alpha}_1$  & 2                      & 1                                  \\ \hline
\end{tabular}
\caption{Isotropic vectors in $F_{\En, 2}$ and their divisibilities.}
\label{tab:sterk-cusp-divisibilities}
\end{table}

:::




## K3 Cusps

:::{.remark}
We recall the cusp diagram for $F_{(2,2,0)}$:

\begin{figure}[H]
\centering
\input{tikz/220-cusp-diagram.tikz}
\caption{}
\label{fig:220-cusp-diagram}
\end{figure}




:::


## Coble to Enriques Cusp Correspondence

:::{.theorem}
The embedding $\eta: F_{\Co}\to F_{\En}$ induces the correspondence on boundary cusps of the Baily-Borel compactifications shown in \cref{fig:enriques-coble-correspondence}.

\begin{figure}[H]
\centering
\input{tikz/coble-enriques-cusp-correspondence.tikz}
\caption{Cusp correspondence $F_{\Co} \to F_{\En}$.}
\label{fig:enriques-coble-correspondence}
\end{figure}
:::

:::{.remark}
We prove this correspondence by considering divisibilities at the corresponding 0-cusps and 1-cusps in both moduli spaces.
We first note that since $T_{\Co}$ can be written as $L(2)$ where $L = \gens{1} \oplus E_8$, every $v\in T_{\Co}$ satisfies $\div_{T_{\Co}}(v) = 2$.
:::

:::{.lemma}
\label{lem:divisibility_Tco_one}
Fixing notation,
\begin{align*}
    v_1 &\da e' & w_1 &\da \eta(v_1) = \tilde e' \\
    v_2 &\da 2h + \alpha_1 + \alpha_2 & w_2 &\da \eta(v_2) = 2\tilde e + 2\tilde f + \tilde\alpha_1 + \tilde\alpha_2 \\
    J &\da \gens{v_1, v_2} & \tilde J &\da \gens{w_1, w_2}
\end{align*}
We then have $\mathrm{div}_{T_{\En} }(w_1) = 2$.
:::

:::{.proof}
This follows from the fact that $\tilde e\in U(2)$ where 
$T_{\En} = U \oplus U(2) \oplus E_8(2)$ 
Noting that
$\tilde e' \tilde f' = 2$, and $\tilde e'$ is orthogonal to the remaining generators of in the $U$ and $E_8(2)$ summands, we thus have
\[
\mathrm{div}_{T_{\En} }(w_1) \da \mathrm{div}_{T_{\En} }(\eta(e'))  
 = \mathrm{div}_{T_{\En} }(\tilde e') = 2
.\]
Explicitly, one can check the pairing of $\tilde e'$ against an arbitrary vector. 
Write $x+y+z\in U \oplus U(2)\oplus E_8(2)$, then 
\[
\tilde e'\cdot(x+y+z) = \tilde e'\cdot y\in \ts{0, 2}
\]
since $y\in U(2)$ and $\tilde e'\in (U\oplus E_8(2))^{\perp T_{\En}}$.
Thus $\beta_{T_{\En}}(\tilde e', T_{\En}) = \beta_{T_{\En}}(\tilde e', U(2)) = 2\bZ$ since $\tilde e'\cdot\tilde f' = 2$.
:::


:::{.lemma}
\label{lem:w1_perp_calculation}
The 0-cusp $(9,9,1)_1$ in $F_{\Co}$ maps to the zero-cusp $(10, 8, 0)_1$ in $F_{\En}$.
:::

:::{.proof}
The cusp correspondence follows from computing the lattice $w_1^{\perp T_{\En}}/\gens{w_1}$ under the primitive embedding $\eta$, since $\eta(v_1) = w_1$ and $v_1$ is the isotropic vector corresponding to $(9,9,1)_1$ in $F_{\Co}$.
This particular case follows from a direct computation:
\begin{align*}
{
(\tilde e')^{\perp T_{\En}} \over \gens{\tilde e'}
}
&= {
\gens{\tilde e,\tilde f} \oplus \gens{\tilde e'} \oplus \gens{\tilde \alpha_1, \cdots, \tilde \alpha_8} \over \gens{\tilde e'}
} \\
&\cong \gens{\tilde e, \tilde f} \oplus \gens{\tilde \alpha_1, \cdots, \tilde \alpha_8} \\
&\cong U \oplus E_{8}(2) 
\cong (10,8,0)_1
.\end{align*}

Alternatively, by \cite[Prop. 5.5]{AE22nonsympinv}, the isomorphism type of $w_1^{\perp T_{\En}}/w_1$ is determined by $\mathrm{div}_{T_{\En}}(w_1)$; by \cref{lem:divisibility_Tco_one} $\mathrm{div}_{T_{\En}}(w_1) = 2$. 
Since the divisibility of the isotropic vector at the Enriques 0-cusp $(10, 8, 0)_1$ is also 2 and the two Enriques 0-cusps are distinguished by divisibility, the correspondence follows.
:::

:::{.lemma}
\label{lem:1_cusp_correspondence}
Cusp $(7,7,1)_0$ in $F_{\Co}$ maps to cusp $(8, 6, 0)_0$ in $F_{\En}$.
:::

:::{.proof}
The results follows from verifying that the unique orbit $J$ of a primitive isotropic plane in $T_{\Co}$ satisfies $J^{\perp T_{\Co}}/J \cong (7,7,1)$, and identifying the isomorphism type of its image $\tilde J^{\perp T_{\En}}/\tilde J$ in $T_{\En}$.
One checks that both $v_2$ and $w_2$ are isotropic, and $v_2 \in v_1^{\perp T_{\Co}}/v_1$, and so $J$ and $\tilde J$ define isotropic planes in $T_{\Co}$ and $T_{\En}$ respectively. By \cite[Prop. 5.5, Lem. 5.9]{AE22nonsympinv}, it suffices to show
\[
\mathrm{div}_{w_1^{\perp T_{\En}} /w_1}(w_2)  \da \mathrm{div}_{U \oplus E_8(2)}(2\tilde e + 2\tilde f + \tilde \alpha_1 + \tilde \alpha_2)= 2
,\]
since the isomorphism type of $\tilde J^\perp/\tilde J$ is uniquely determined by the isomorphism type of $w_2^{\perp T_{\En}}/w_2$ in $w_1^{\perp T_{\En}}/w_1$, which is in turn uniquely determined by the characterization of $w_2$ as odd, even ordinary, or even characteristic in $w_1^{\perp T_{\En}}/w_1$, which by \cref{lem:w1_perp_calculation} is isomorphic to $U \oplus E_8(2)$. One checks directly in coordinates: let $x+y\in U \oplus E_8(2)$ and consider its pairing with $w_2$:
\begin{align*}
(x+y)\cdot w_2 
= (x+y)\cdot (2\tilde e + 2\tilde f + \tilde \alpha_1 + \tilde \alpha_2 )
= 2x\cdot (\tilde e + \tilde f) + y\cdot (\tilde \alpha_1 + \tilde \alpha_2)
,\end{align*}
where we've used orthogonality relations. We note that the first term is evidently even, while the second term is even because all pairings are either zero or divisible by two in the $E_8(2)$ summand of $U \oplus E_8(2)$.
:::


# Degenerations of stable Coble surfaces

:::{.remark}
We describe the KSBA stable limits of Coble surfaces.
:::

:::{.remark}
We give an example of an integral affine structure for a degeneration of Coble surfaces.
:::



# Appendix




:::{.remark}
Following \cite{AEGS23}, a **Kulikov model** is a $K$-trivial semistable model $\cX \to (C, 0)$ of a degeneration of K3 surfaces over a pointed curve $C$. 
For each such degeneration, one can define the dual complex of the central fiber $\Gamma(\cX_0)$. For Type II degenerations of K3 surfaces, this yields an integral affine $S^2$ with singularities of total charge $24$, and for Type III the dual complex is an interval $\bD^1$.
The additional data of an integral affine polarization $R_{\IA} \subset \Gamma(\cX_0)$ describes the KSBA stable limit of a degeneration $(\cX^*, \varepsilon \cR^*)$.
For Enriques (and hence Coble) surfaces, we take the corresponding dlt models $\cZ \da \cX/\iota_{\En}$ and half-divisor models $(\cZ, \cR_{\cZ}) \da (\cX, \cR)/\iota_{\En}$ where $\cX \to (C, 0)$ and $(\cX, \cR)$ are Kulikov and divisor models of their K3 covers.


:::

:::{.remark}
The following is a representation of a Type II degeneration -- it is a chain of surfaces whose dual complex is an interval $\bD^1$, where the ends $V_1$ and $V_n$ are rational and the remaining $V_i$ are isomorphic to $E\times \PP^1$ for a fixed elliptic curve $E$.
The intersections $V_i \intersect V_{i+1}$ are double curves isomorphic to $E$.

\begin{figure}[H]
\centering
\includesvg[width=\textwidth]{inkscape/type-ii-kulikov-degeneration}
\caption{}
\label{fig:typeiikdg}
\end{figure}

A Type III degeneration can be represented by a triangulation of $S^2$ with singularities, depicted as follows:


\begin{figure}[H]
\centering
\includesvg[width=\textwidth]{inkscape/triangulated-sphere-fan.svg}
\caption{}
\label{fig:triangulated-sphere-fan}
\end{figure}

:::

:::{.remark}
The following is a combinatorial representation of a Kulikov model for Sterk 2.

\begin{figure}[H]
\centering
\includesvg[width=\textwidth]{inkscape/ias-sterk2-kulikov-model.svg}
\caption{}
\label{fig:ias-sterk2-kulikov-model}
\end{figure}

:::

