# Overview

My research is in algebraic geometry, particularly in explicit combinatorial techniques for compactifying moduli spaces of algebraic surfaces over $\CC$ and classifying their boundaries.
For a given moduli space, there are often many choices of compactifications, leading to a need to study comparisons between them and their relative advantages and disadvantages.
In particular, a natural question to ask is whether or not the boundaries have geometric and modular meanings, exhibited as degenerating limits of smooth surfaces.
Toward this end, we turn to the **stable pair compactifications** of Kollár, Shepherd-Barron, and Alexeev \cite{kollar1988threefolds-and-deformations,alexeev1996moduli-spaces,Kol23}.

The KSBA compactification generalizes the Deligne-Mumford compactification $\overline{\Mgn}$ \cite{deligne1969the-irreducibility-of-the-space} of $\Mgn$, the moduli space of genus $g$ curves with $n$ marked points, to higher-dimensional varieties.
By \cite{mumford1965git, namikawa1976a-new-compactification-of-the-siegel1, alexeev1999on-mumfords-construction, alexeev2002complete-moduli}, a similarly modular compactification $\overline{\Ag}$ of the moduli space $\Ag$ of principally polarized abelian varieties via stable pairs exists.
The normalization of $\overline{\Ag}$ coincides with a particular choice of toroidal \cite{AMRT75} compactification by the work of \cite{kollar1988threefolds-and-deformations} and \cite{alexeev1996moduli-spaces}.

More recently, similar compactifications have been constructed for moduli spaces of K3 surfaces.
\cite{alexeev2023stable-pair} addresses $F_2$, the moduli space of degree 2 primitively polarized K3 surfaces, and \cite{ABE22} studies $F_{\mathrm{ell}}$, the moduli space of elliptic K3 surfaces, which embeds into $F_2$.
\cite{alexeevCompactModuliK32023} addresses $F_{2d}$, polarized K3 surfaces of degree $2d$ for $d\geq 1$, developing the theory of *recognizable divisors*, which gives comparison morphisms between KSBA and semitoroidal compactifications.
\cite{AEH21, AE22} extend the theory further to K3 surfaces with nonsymplectic automorphisms and nonsymplectic involutions respectively.

In \cite{AEGS23}, we built upon these ideas to describe the stable pair compactification of $F_{\En, 2}$, the moduli space of degree 2 numerically polarized Enriques surfaces, leveraging the theory of ADE surfaces developed in \cite{AT21}. In my current project, I extend these ideas to $F_{\Co}$, the moduli space of Coble surfaces, regarded as a divisor in $F_{\En}$, the moduli space of unpolarized Enriques surfaces.

# Compactifications

My work builds on the theory of compactifications of K3 surfaces.
In compactification problems, one allows smooth surfaces to degenerate into surfaces with controllable and well-understood singularities.
Our primary choices of compactifications include the following:

- The Baily-Borel compactification \cite{BB66}, which is amenable to lattice theory.
  However, surfaces on the boundary lack clear interpretations as limits of smooth surfaces.
  These compactifications are generally "small", since they involve adjoining finitely many components of dimension at most two, and thus the boundary is comprised of points and modular curves with various level structures.
  In favorable cases, the number of boundary cusps and their incidence relations can be concretely computed, and thus the boundary can be encoded in an incidence diagram.

- Toroidal compactifications, which can be studied using toric geometry.
  These are determined by the data of a collection of fans ranging over the Baily-Borel cusps.
  However, there are infinitely many choices of such data, and it is often unclear which choices (if any) lead to modular compactifications.
  Again in favorable cases, these fans can be described explicitly.

- The semitoroidal compactifications of \cite{Loo03} which simultaneously generalize both of the above.
  They are similarly specified by a collection of infinite-type "semifans", of which there is not an *a priori* distinguished choice.
  However, the boundary strata can be studied using tools from Hodge theory, Picard-Lefschetz theory, lattice-theoretic techniques, and the rich combinatorial structures of Coxeter groups and integral affine geometry.

- The KSBA stable pair compactifications.
  An alternative from the log minimal model program, this yields a moduli space whose boundary strata admit strong geometric interpretations as limiting surfaces with controlled singularities.
  However, this comes at a cost -- it is generally very difficult to classify or describe the boundary.

A central theme in my research is to construct KSBA compactifications and classify their boundary strata by relating them to particular choices of semitoroidal compactifications.
In this way, one can construct compactifications that are simultaneously modular and amenable to explicit computations.
In \cite{AEGS23}, we prove the following:

::: {.theorem title="\cite{AEGS23}, Thm. 1.1"}
\label{thm:aegs-normalization-comparison-morphism}
There is an isomorphism
\[
\qty{ \overline{F_{\En, 2}} }^\nu \cong \overline{F_{\En, 2}}^{\cF}
\]
between the normalization of the KSBA compactification of $F_{\En, 2}$, the moduli space of degree two numerically polarized Enriques surfaces, and a semitoroidal compactification associated to an explicit collection of semifans $\cF$. 

The semifan data $\cF$ can be combinatorially described in terms of tilings of hyperbolic spaces by polytopes, Coxeter diagrams, and integral affine spheres with involutions.
There is a complete classification of KSBA stable limits of such Enriques surfaces in terms of ADE+BC surfaces.
Furthermore, the structure of $\partial \overline{F_{\mathrm{En}, 2}}$ can be read off of Coxeter diagrams in a straightforward manner.
:::

# Past Work

## Compact moduli spaces of Enriques surfaces

An **Enriques surface** is a non-rational minimal algebraic surface $Y$ of Kodaira dimension $\kappa(Y) = 0$ for which $h^1(\OO_Y) = h^2(\OO_Y) = 0$ and $K_Y$ is nontrivial 2-torsion.
\cite{Enr06} originally constructed such surfaces, motivated by relating the rationality of a surface to its irregularity $q_Y \da h^1(\OO_Y)$.
There has been a resurgence of interest in moduli spaces of Enriques surfaces, c.f. \cite{viehweg1995quasi-projective-moduli,Lie13,GH16,CDGK18,knutsen2020moduli,EnriquesOne,fortuna2020cohomology}.

Away from characteristic 2, deformations of (numerically polarized) Enriques surfaces are unobstructed by \cite{Il79,La83}, yielding a quasi-separated 10-dimensional Artin stack of finite type over $\CC$ by \cite[Thm.\, 5.11.6]{EnriquesOne}. By \cite{kondo1994the-rationality}, the coarse moduli space is known to be rational.
As for K3 surfaces, Enriques surfaces admit a global Torelli theorem and thus a coarse space $F_{\En}$ of unpolarized surfaces birational to a Shimura variety $D/\Gamma$ of orthogonal type, yielding a type IV Hermitian symmetric domain.
Fixing a numerical polarization of degree $2d$ yields a quasiprojective, non-proper moduli space $F_{\En, 2d}$.

Every Enriques surface can be obtained as a quotient $X/\iota$ of a K3 surface $X$ by a nonsymplectic fixed-point-free involution $\iota$.
Thus the moduli space of Enriques surfaces can be related to moduli of K3 surfaces with nonsymplectic involutions, allowing us to leverage the theory of \cite{AE22} to describe compactifications $\overline{F_{\En}}$ and $\overline{F_{\En, 2}}$ and arrive at \cref{thm:aegs-normalization-comparison-morphism}. A key insight in this paper is that the Coxeter diagrams for $F_{\En, 2}$ can be obtained as quotients by involutions of the diagrams for K3 surfaces.
Leveraging and extending the theory of ADE surfaces in \cite{AT21} to Dynkin diagrams of types $B$ and $C$, we arrive at a description of the irreducible components of KSBA degenerations which is largely in terms of explicit toric varieties.

# Current Work

## Compact moduli spaces of Coble surfaces

::: {.remark}
A Coble surface is a smooth projective rational surface $S$ with $\abs{-K_S} = \emptyset$ but $\abs{-2K_X}\neq \emptyset$.
Such surfaces arise from the work of \cite{Cob19} and \cite{Cob29} on Cremona transformations of $\PP^2$ preserving an irreducible rational sextic $C$ with ten nodal singularities. The blowup $S$ of these nodes yields a Coble surface.
Coble surfaces occur as degenerations of Enriques surfaces and were ultimately classified in \cite{DZ99}.
As such, they are closely tied to the theory of algebraic K3 surfaces with nonsymplectic involutions, which were classified by \cite{nikulin1979quotient-groups}. For a reduced sextic $C$, the double cover of $S$ branched along the proper transform of $C$ is a K3 surface $X$ which can be realized as a degeneration of the universal double cover of an Enriques surface, where $X$ is allowed to acquire an $A_1$ singularity fixed by the Enriques involution.

Denote by $F_{\Co, n}$ the moduli space of Coble surfaces with $n$ boundary components.
It is well-known that $1\leq n\leq 10$, and the case $n=1$ corresponds to the surfaces originally studied by Coble.
By \cite{DK13}, the moduli space $F_{\Co} \da F_{\Co, 1}$ is known to be rational, but very little else is known about these moduli spaces.
In particular, compactifications of $F_{\Co, n}$ have not yet appeared in the literature, despite their close relation to Enriques surfaces.
:::

::: {.remark}
\label{rmk:divisors-for-coble-compactification}
Towards constructing such a KSBA compactification, one can form a period domain for $F_{\Co}$ and study (semi)toroidal compactifications as an intermediate step. Note that the blowup of a rational plane sextic $C$ along its ten nodes yields a Coble surface $S$ with $n=1$ boundary components.
The double cover of $S$ branched along $C$ is a K3 surface $X$ containing divisors $e_0,\cdots, e_{10}$ where $e_0$ is the preimage of the pullback of a hyperplane class in $\PP^2$ and $e_1,\cdots, e_{10}$ are preimages of the exceptional divisors over the nodes of $C$.

These divisors in $X$ generate a sublattice $S_{\Co}$ of $\Pic(X)$ with orthogonal complement $T_{\Co}$, which can be shown to be isometric to the following:
\begin{align*}
S_{\Co} ={\rm{I}}_{1, 10}(2) \cong \gens{-2} \oplus E_{10}(2), \qquad T_{\Co}\cong \gens{2} \oplus E_{10}(2)
\end{align*}
where $E_{10} \da U \oplus E_8$ with $U$ the hyperbolic lattice and $E_8$ the lattice associated to the $E_8$ Dynkin diagram.
I construct the period domain 
\[
F_{\Co} \da D_{T_\Co}/\Orth(T_\Co),\qquad D_{T_\Co} \subseteq \ts{ [\sigma] \in \PP\qty{T_{\Co}\tensor_{\ZZ} \CC} \st \sigma^2 = 0,\, \sigma\bar\sigma >0 }
,\]
which is birational to the moduli space of Coble surfaces with $n=1$ boundary component constructed as a GIT quotient $(\PP^2)^{10}\modmod\PGL_3$.
The moduli space $F_{\Co}$ is an arithmetic quotient of a Hermitian symmetric domain of Type IV, and thus admits semitoroidal compactifications, including the canonically defined Baily-Borel compactification $\bbcpt{F_{\Co}}$.
:::

::: {.remark}
In my current single-author project, I have studied the boundary $\partial \bbcpt{F_{\Co}}$ of the Baily-Borel compactification of the moduli space of Coble surfaces and constructed an embedding $F_{\Co}\injects F_{\En}$ into the moduli space of unpolarized Enriques surfaces. Furthermore, I extend this to a morphism 
\[
\eta: \bbcpt{F_{\Co}} \to \bbcpt{F_{\En}}
\]
on their Baily-Borel compactifications.
To determine the stratification of $\bbcpt{F_{\Co}}$, I apply the *mirror moves* of \cite{AE22}, which are encoded in \cref{fig:mirror-moves-coble-simplified-tikz}. 

\begin{figure}[H]
\centering
\input{tikz/mirror-moves-coble-simplified.tikz}
\caption{Application of the mirror move algorithm to $S_{\Co} = (11, 11, 1)_1$.}
\label{fig:mirror-moves-coble-simplified-tikz}
\end{figure}


Using this, I have constructed the incidence diagram that represents $\partial \bbcpt{F_{\Co}}$, which is shown in \cref{fig:coble-cusp-diagram-detailed}.
Using lattice theoretic techniques, and in particular an invariant called the *divisibility*, I have determined that $\eta$ induces the correspondence $\partial \bbcpt{F_{\Co}}\to \partial \bbcpt{F_{\En}}$ depicted in \cref{fig:enriques-coble-correspondence}, which has allowed me to determine that Coble degenerations are *$\DD^2$-type*, as opposed to *$\RP^2$-type*, an essential ingredient for later constructing the correct divisorial log terminal (dlt) models of KSBA degenerations.


\begin{figure}[H]
\centering
\input{tikz/coble-cusp-diagram-detailed.tikz}
\caption{The boundary of the Baily-Borel compactification of $F_{\Co}$. Rounded nodes indicate points added in the boundary of the compactification $\bbcpt{F_{\Co}}$, and rectangles indicate modular curves. Solid arrows $A\to B$ indicate that a point $A$ is contained in the closure of a curve $B$.}
\label{fig:coble-cusp-diagram-detailed}
\end{figure}

\begin{figure}[H]
\centering
\input{tikz/coble-enriques-cusp-correspondence.tikz}
\caption{The cusp correspondence $\eta: \bbcpt{ F_{\Co}} \to \bbcpt{ F_{\En} }$. Dotted arrows indicate the boundary correspondence under $\eta$.}
\label{fig:enriques-coble-correspondence}
\end{figure}
:::

::: {.remark}
I have extended $\eta$ to a morphism $\tilde \eta: \bbcpt{ F_{\Co}} \to \bbcpt{ F_{(2,2,0)} }$, a moduli space of quartic hyperelliptic K3 surfaces used in \cite{AEGS23}. I determined that that the Coble cusps correspond to $U\oplus E_8^2$, the lattice with invariants $(18, 0, 0)_1$ in \cref{fig:220-cusps-diagram}.
Using our previous work in \cite{AEGS23}, I am working on a correspondence between $F_{\Co}$ and $F_{\En, 2}$ in order to construct KSBA degenerations. The cusp diagram for $F_{\En, 2}$ was first given by \cite{Ste91}, and I have computed that the Coble 0-cusp corresponds with cusp 2 of \cref{fig:sterk-cusp-diagram}. This correspondence requires studying a separate period domain $D_{\Co}/\Gamma$ for a certain subgroup $\Gamma_{\Co} \leq \Orth(T_{\Co})$ and classifying orbits of isotropic vectors under this subgroup.

Toward this end, I have been working on adapting the techniques of \cite{Ste91} and \cite{scattone1987on-the-compactification-of-moduli} to new lattices. This has involved a careful study of the discriminant groups $A_{T_{\Co}}$ and $A_{T_{\En}}$ of the Coble and Enriques lattices, and finding techniques to reduce classification of orbits of isotropic vectors in $T_{\Co}$ to finite, computable problems in $A_{T_{\Co}}$. This has also involved explicit constructions of *Eichler transformations* which prove that vectors satisfying certain numerical properties are in the same $\Gamma_{\Co}$-orbit. Conjecturally, this will suffice to produce a complete cusp diagram for $D_{\Co}/\Gamma_{\Co}$, which I can then put in correspondence with the cusps of $F_{\En, 2}$.

Ultimately, this chain of correspondences will allow me to leverage \cite{AEGS23}, \cite{AT21}, and \cite{AE22} to construct integral affine structures and dlt models of KSBA-stable Coble surfaces in terms of those for K3 and Enriques surfaces.
From these data, in an in-progress paper which will comprise the majority of my dissertation, I am working on constructing the KSBA stable limits of Coble surfaces as special cases of limits of Enriques surfaces satisfying a certain linear relation, yielding a geometrically meaningful, explicit, combinatorial description of the KSBA stable pair compactification $\overline{F_{\Co}}$ and its boundary $\partial \overline{F_{\Co}}$.

\begin{figure}[H]
\centering
\input{tikz/220-cusp-diagram.tikz}
\caption{The boundary cusp diagram of $F_{(2,2,0)}$, the moduli space of quartic hyperelliptic K3 surfaces.}
\label{fig:220-cusps-diagram}
\end{figure}

\begin{figure}[H]
\centering
\input{tikz/sterk-cusp-diagram.tikz}
\caption{The boundary cusp diagram of $F_{\En, 2}$, the moduli space of degree 2 numerically polarized Enriques surfaces.}
\label{fig:sterk-cusp-diagram}
\end{figure}
:::

# Future Work

## Coble surfaces with $1\leq n\leq 10$ boundary components

::: {.remark}
For $S$ a Coble surface of *K3 type*, one can write 
$\abs{-2K_S} = \ts{C}$ where $C = C_1 + \cdots + C_n$, with each $C_i$ an irreducible curve on $S$.
The $C_i$ are referred to as *boundary components*, and it is known that $1\leq n \leq 10$.
The moduli spaces $F_{\Co, n}$ for $n\geq 2$ have not yet appeared in the literature, but are amenable to a similar study as the $n=1$ case.
Let $\Sigma$ be a general *Coble set* of points in $\PP^2$, so that the blowup $S$ of $\PP^2$ along the points of $\Sigma$ is a Coble surface double covered by a K3 surface $X$ branched along $C$.
Following a similar construction as that described in \cref{rmk:divisors-for-coble-compactification} yields a collection of primitively embedded sublattices $L_1,\cdots, L_{10}$ in $\Pic(X)$. These are 2-elementary lattices with invariants $(r=10+n, a=12-n,\delta)$, described in 
\cite[Table 5.1, p.553]{EnriquesOne}
 and reproduced in \cref{fig:coble-boundary-components-table}.

\begin{figure}[H]
\centering
\begin{tabular}{|c|c|c|c|c|c|}
\hline$n$ & $\abs\Sigma$ & $K_{\mathrm{V}}^{2}$ & $M = (r, a, \delta)$ & 2-elementary lattice $M$ & $N=M^{\perp}$ \\
\hline 1 & 10 & -1 & $(11,11,1)$ & $\mathrm{E}_{10}(2) \oplus \gens{-2}$ & $\mathrm{I}^{2,9}(2)$ \\
2 & 11 & -2 & $(12,10,1)$ & $\mathrm{E}_{8}(2) \oplus \mathrm{U} \oplus \gens{-2}^{\oplus 2}$ & $\mathrm{I}^{2,8}(2)$ \\
3 & 12 & -3 & $(13,9,1)$ & $\mathrm{D}_{4}^{\oplus 2} \oplus \gens{-2}^{\oplus 3} \oplus \mathrm{U}(2)$ & $\mathrm{I}^{2,7}(2)$ \\
4 & 13 & -4 & $(14,8,1)$ & $\mathrm{D}_{4}^{\oplus 2} \oplus \gens{-2}^{\oplus 4} \oplus \mathrm{U}(2)$ & $\mathrm{I}^{2,6}(2)$ \\
5 & 14 & -5 & $(15,7,1)$ & $\mathrm{E}_{8} \oplus \gens{-2}^{\oplus 5} \oplus \mathrm{U}$ & $\mathrm{I}^{2,5}(2)$ \\
6 & 15 & -6 & $(16,6,1)$ & $\mathrm{E}_{10} \oplus \gens{-2}^{\oplus 6}$ & $\mathrm{I}^{2,4}(2)$ \\
7 & 16 & -7 & $(17,5,1)$ & $\mathrm{E}_{8} \oplus \mathrm{D}_{6} \oplus \gens{-2} \oplus \mathrm{U}(2)$ & $\mathrm{I}^{2,3}(2)$ \\
8 & 17 & -8 & $(18,4,0)$ & $\mathrm{E}_{8} \oplus \mathrm{D}_{8} \oplus \mathrm{U}(2)$ & $\mathrm{U}(2)^{\oplus 2}$ \\
8 & 17 & -8 & $(18,4,1)$ & $\mathrm{E}_{10} \oplus \mathrm{D}_{6} \oplus \gens{-2}^{\oplus 2}$ & $\mathrm{I}^{2,2}(2)$ \\
9 & 18 & -9 & $(19,3,1)$ & $\mathrm{E}_{10} \oplus \mathrm{D}_{8} \oplus \gens{-2}$ & $\mathrm{I}^{2,1}(2)$ \\
10 & 19 & -10 & $(20,2,1)$ & $\mathrm{E}_{10} \oplus \mathrm{D}_{10}$ & $\langle 2\rangle^{\oplus 2}$ \\
\hline
\end{tabular}
\caption{10 irreducible families of K3 surfaces corresponding to Coble surfaces with $1\leq n\leq 10$ boundary components.}
\label{fig:coble-boundary-components-table}
\end{figure}
:::

::: {.remark}
This collection coincides precisely with the $g=0$ line of Nikulin's triangular table of 2-elementary lattices \cite[Fig.\,1]{AE22}, 
and applying the period domain construction to these lattices yields ten moduli spaces $F_{\Co, n}$ for $1\leq n \leq 10$.
The $n=1$ case is the subject of my current work.

I conjecture that the moduli spaces and the boundaries of their compactifications for the cases $2\leq n \leq 10$ can be described using similar techniques, which would be the first explicit study of their boundaries in the literature.
Most immediately, I have computed several of the boundary incidence diagrams of their Baily-Borel compactifications using algorithms described in \cite{AE22nonsympinv}, and the remaining ones are similarly computable.
:::

::: {.remark}
The ramification locus of the K3 cover of $S$ is described in \cite[Eqn. 5.3.1]{EnriquesOne} --
I conjecture that the corresponding involutions are nonsymplectic and that a component of the ramification locus forms a **recognizable divisor** c.f. \cite{alexeevCompactModuliK32023,AEH21}.
Under this assumption, \cite[Thm.\,3.24]{AEH21} can be applied to identify the KSBA compactification with a semitoroidal compactification for a specific choice of semifans.
I conjecture that these semifans are either refinements or coarsenings of the canonical Coxeter fans at the Baily-Borel cusps, and can be described in an explicit way, using an extension of the theory of ADE surfaces developed in \cite{AT21}.

Moreover, from this data one can extract a classification of dlt models for KSBA stable limits of such surfaces, giving a first description of $\partial \overline{F_{\Co, n}}$, as our previous paper \cite{AEGS23} did for numerically polarized Enriques surfaces.
Finally, by \cite[Prop.\,5.4.6]{EnriquesOne}, for each lattice of rank $10+n$ in \cref{fig:coble-boundary-components-table}, there is an embedding $F_{\Co, n}\injects F_{\En}$ the moduli space of Enriques surfaces as constructed from $E_{10}(2)$-polarized K3 surfaces. 
Thus the data of integral affine structures, and hence dlt and stable models, can be understood by studying restrictions of the K3 boundary data described in \cite{AE22}.
:::

## Nodal Enriques surfaces

An Enriques surface $Y$ is called **nodal** if $Y$ contains a rational $(-2)$-curve, and **unnodal** otherwise.
Let $F_{\En, \Nod}$ be the moduli space of nodal Enriques surfaces.
Such surfaces have received a great deal of attention in recent years, c.f.

- \cite{cossecAutomorphismsNodalEnriques1985} describes the automorphism group of a generic point of $F_{\En, \Nod}$ using non-transcendental methods, showing it is equal to a normal subgroup of the Weyl group $W(T_{2,4,6})$ containing its 2-congruence subgroup.
  They further show that up to $\Aut(S)$, there is a unique smooth rational curve on such a surface.
  Combined with the work of \cite{barthAutomorphismsEnriquesSurfaces1983} on unnodal surfaces, this gives a description of the automorphism group at a generic point of $F_{\En}$.

- \cite{ingallsNodalEnriquesSurfaces2015} studies semiorthogonal decompositions of the derived categories $D^b(Y)$ of nodal Enriques surfaces, as progress toward answering similar questions for general Enriques surfaces.

- \cite{martinNodalEnriquesSurfaces2024} shows that an arbitrary (not just generic) nodal Enriques surface $Y$ is a *Reye congruence*: letting $F_{i}^{\pm}$ be the multiple fibers of the 10 elliptic pencils on $Y$, the image of the Fano model of $Y$ defined by $\abs{{1\over 3} \sum F_i^+}$ is contained in a quadric.

- \cite{DK13} shows that $F_{\En, \Nod}$ is rational.

By \cite[\S.\,5.6]{EnriquesOne}, the moduli space $F_{\Nod}$ can be constructed using the period domain $F_S$ of lattice-polarized K3 surfaces where
\[
S_{\Nod} = \gens{-4} \oplus U \oplus E_8(2)
\]
is the generic Picard lattice of the K3 cover $X$ of $Y$ and
\[
T_{\Nod} \da S^{\perp} \cong \gens{4} \oplus U \oplus E_8(2)
\]
is its transcendental lattice.
It is known that $F_{\En, \Nod}$ forms an irreducible hypersurface in $F_{\En}$, and that a generic Enriques surface is unnodal.
Similar to the case of Coble surfaces, $F_{\Nod}$ can also be realized as a divisor $\cH_{-4}/\Orth(T_{\En})$, yielding an 9-dimensional irreducible quasiprojective variety.
By \cite[Def.\,5.6.3]{EnriquesOne}, there is a primitive embedding of lattices
\begin{align*}
S_{\En} \da E_{10}(2) \da U(2) \oplus E_8(2) &\to S_{\Nod} \da \gens{-4} \oplus U \oplus E_8(2) \\
((e_1, f_1), x) &\mapsto (f_2, 2e_2 + f_2 + h , x) 
\end{align*}
(where $h$ is a generator of $\gens{-4}$) which exhibits $F_{\Nod}\injects F_{\En}$ as a divisor in the moduli space of unpolarized Enriques surfaces.

This yields a similar setup to $F_{\Co}$, and I conjecture that the Baily-Borel compactification can be studied using similar techniques.
In particular, I conjecture that orbits under $\Orth(T_{\Nod})$ of isotropic vectors and planes can be classified, yielding a boundary incidence diagram, and that the above lattice embedding will allow leveraging \cite{AEGS23} to construct the KSBA compactification.
I similarly conjecture that the work in \cite{AEGS23} can be used to construct dlt models and integral affine structures that classify KSBA stable limits of nodal Enriques surfaces.
However, new techniques will have to be developed, since $T_{\Nod}$ is not a 2-elementary lattice.

## Halphen and rational elliptic surfaces

Following \cite{mirandaModuliSpaceRational2021}, a **rational elliptic surface** is a smooth, projective, rational surface $Y$ which admits a relatively minimal fibration $\pi: Y\to \PP^1$ where the generic fiber is a smooth elliptic curve.
Given a rational elliptic surface, the **index** of $Y$ is the minimal $m$ such that $\pi$ corresponds to the anti-pluricanonical linear system $\abs{-mK_Y}$.
A **Halphen pencil of index $m$** is a pencil of curves of degree $3m$ in $\PP^2$ with 9 basepoints.
A rational surface obtained by minimally resolving the base points of a Halphen pencil of index $m$ is called a **Halphen surface of index $m$**. Equivalently, by \cite[Def.\,3.18]{grivauxInfinitesimalDeformationsRational2018} they are rational surfaces $Y$ such that $\abs{-mK_Y}$ is of dimension 1, has no fixed part, and defines a basepoint-free pencil.

By \cite[Rmk.\,4.9.4]{EnriquesOne}, the set of Halphen pencils in $\PP^2$ up to Cremona equivalence is in bijection with the set of rational surfaces with genus 1 fibrations.
Indeed,  and by \cite[Rmk.\,2.4]{DZ99} and \cite[\S 3.3.3]{grivauxInfinitesimalDeformationsRational2018}, any relatively minimal rational elliptic surface $Y$ is a Halphen surface of some index $m$, realized as the blowup of $\PP^2$ along the 9 basepoints of a Halphen pencil,

By \cite[Rmk.\,2.8]{CD12}, Halphen surfaces of index 1 are parameterized by an open subset of the Grassmannian $\Gr_2(10)$ of pencils of plane cubic curves, and their moduli space $M_{H, 1}$ is an irreducible variety of dimension 8. Moreover, there are moduli spaces $M_{H, m}$ of Halphen surfaces of index $m$ for $m\geq 2$ which are fibrations over $M_{H, 1}$ with 1-dimensional fibers, and are conjectured to be irreducible varieties of dimension 9. Equivalently, these are moduli spaces of rational elliptic surfaces of index $m$.

By \cite[Prop.\,9.1.4]{EnriquesTwo}, any terminal Coble surface of K3 type is isomorphic to a blowup of a Halphen surface of index 1 or 2 at either 2 or 1 simple reduced fibers.
In particular, \cite{DZ99} shows that blowing down any $(-1)$-curve on an unnodal Coble surface $S$ yields a Halphen surface $Y$ of index 2. Conversely, by \cite{DM19}, any such Coble surface $S$ is obtained by blowing up the singular point of a non-multiple irreducible fiber of a Halphen surface $Y$.
Due to this close geometric relationship between Coble surfaces and Halphen surfaces of index 1 and 2, I conjecture that there is a relationship between $F_{\Co}$ and the moduli spaces $M_{H, 1}$ and $M_{H, 2}$.

Open subsets of these moduli spaces are referenced in the literature, e.g. in \cite[Rmk.\,5.4]{dolgachevChileanConfigurationConics2020} and \cite[\S. 3.3.3]{grivauxInfinitesimalDeformationsRational2018}. \cite{mirandaModuliWeierstrassFibrations1981} constructs a projective compactification of $M_{H, 1}$ via GIT applied to the Weierstrass models of such surfaces.
\cite{mirandaModuliSpaceRational2021} constructs $M_{H, 2}$, showing it is a toric variety of dimension 9, and \cite{zanardiniStabilityPencilsPlane2023} studies the GIT stability of index 2 Halphen pencils in $\PP^2$, toward a GIT compactification of $M_{H, 2}$.

Halphen surfaces of index 2 are special classes of elliptic surfaces without a global section, and are double-covered by K3 surfaces cf.
\cite{kimura2018k3-surfaces}. \cite{ABE22} and \cite{AT21} introduce stable pair compactifications for special classes of elliptic fibrations.
In particular, there is a starting point for this study provided by \cite{AE22}, for which the case $S = (10, 10, 1)$ corresponds to K3 surfaces $X$ with nonsymplectic involution $\iota$ such that $Y \da X/\iota$ is an index 2 Halphen pencil.
More generally, by \cite[\S 4C]{AE22}, the lattices $S = (10+n, 12-n, \delta)$ for $1\leq n\leq 9$ yield index 2 Halphen K3 surfaces $X$ with $I_{2k}$ fiber, and the surfaces $\bar Y$ obtained from contracting the $(-1)$-curves in the special fiber are index 2 Halphen pencils with an $I_k$ fiber.

In particular, these are precisely the lattices that appear in \cref{fig:coble-boundary-components-table}. I conjecture that these lattices can be used to construct period domains of such pencils, yielding moduli spaces $M_{H, 2, k}$ of Halphen surfaces of index 2 with an $I_{2k}$ fiber, and that the matching of these lattices arises from a geometric comparison to Coble surfaces.
Consequently, their KSBA compactifications can be studied, much as was done for $F_{\En, 2}$ and $F_{\Co}$ in our previous and current work, and I conjecture that the boundary strata of $M_{H, 2, k}$ can be classified in a similar way.
In particular, I conjecture that the normalizations of the stable pair compactifications $\overline{M_{H, 2, k}}^R$ are isomorphic to semitoroidal compactifications of the corresponding period domains, where $R$ is a suitably canonical choice of divisor.
In particular, a Halphen surface of index $m\geq 2$ has a unique multiple fiber of multiplicity $m$, and I conjecture that such a fiber can be used to construct a recognizable divisor $R$.

As a starting point, the Coxeter diagram for $S \da (10, 10, 1)$ is well-known, and the moduli theory for the corresponding K3 surfaces is well-developed.
Further study would include

- Constructing the period domain $F_{S}$,

- Constructing Baily-Borel compactification $\overline{F_{S}}^{\bb}$,

- Studying $\Orth(S)$-orbits of isotropic vectors $e_i$ in $S$,

- Using lattice-theoretic techniques to determine the cusp diagram of $\partial \overline{ F_{S}}^{\bb}$,

- Computing $e_i^\perp/\gens{e_i}$ and the Coxeter diagrams at the corresponding 0-cusps,

- Finding an appropriate recognizable divisor $R$ and constructing the stable pair compactification $\overline{F_S}^R$, and

- Leveraging \cite{AE22nonsympinv} to construct dlt models and integral affine structures classifying $\partial\overline{F_S}^R$.

This would open an avenue of research comparing GIT compactifications to KSBA compactifications, and generalizing these techniques to compactifications $\overline{M_{H, m}}^R$ for $m > 2$ to construct new moduli spaces of general rational elliptic surfaces (with no restrictions on the fiber type).
