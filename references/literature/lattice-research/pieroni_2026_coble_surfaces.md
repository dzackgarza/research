#

Roma Tre

CORSO DI DOTTORATO DI RICERCA IN MATEMATICA

XXXVII CICLO DEL CORSO DI DOTTORATO

# Coble surfaces: projective models and automorphisms with related topics

Relatore:

Prof. Alessandro Verra

Dottorando:

Federico Pieroni

Coordinatore:

Prof. Alessandro Giuliani

19 Novembre 2025

Contents

Abstract 2

Introduction 5

1 Generalities on surfaces 13
1.1 Line bundles, divisors and intersection theory on surfaces 13
1.2 Projective models via line bundles 14
1.3 Rational surfaces 16
1.3.1 Hirzebruch surfaces 17
1.3.2 Blow ups of $\mathbb{P}^2$ 17
1.4 Del Pezzo surfaces 18
1.4.1 Del Pezzo surfaces of degree in $\{3,\ldots,8\}$ 18
1.4.2 Del Pezzo surfaces of degree 2, and the Geiser involution 19
1.4.3 Del Pezzo surfaces of degree 1, and the Bertini involution 20
1.4.4 The De-Jonquieres involution 21
1.5 Some Lattice theory 22
1.6 Enriques surfaces 23

2 Coble surfaces 26
2.1 First properties and examples 26
2.2 An extension result 33
2.3 Moduli space of Coble surfaces 45

3 Projective models of Coble surfaces 47
3.1 The Bordiga model 47
3.2 Quintic Coble surfaces 49
3.3 Nodal Coble cubic surfaces 56
3.4 A quartic Coble in $\mathbb{P}^3$ 57

4 Coble conjecture 59
4.1 Pompilj's method 59

5 Involutions on Coble surfaces 67
5.1 Classifying involutions 67
5.2 Families of Coble surfaces 87

6 Appendix 91
6.1 An application of Reider Theorem 100
6.2 The tangent behaviour 108

7 Acknowledgements 111

References 112

# Abstract

Our goal will be the study of complex Coble surfaces. Originally, they were introduced by A.B. Coble in *[6]* in 1919, in the following way. Consider the complex projective plane $\mathbb{P}^{2}$, which we will define more precisely in the next Introduction. Inside $\mathbb{P}^{2}$, an irreducible curve of degree $d$ is the zero locus of an irreducible homogeneous polynomial $F=F(X_{0},X_{1},X_{2})$ of degree $d$ in three complex variables. A singular point for such a curve is a point where all the partial derivatives $\frac{\partial F}{\partial X_{0}},\frac{\partial F}{\partial X_{1}},\frac{\partial F}{\partial X_{2}}$ simultaneously vanish. In the original definition, a Coble surface is obtained picking an irreducible curve $\overline{C}\subset\mathbb{P}^{2}$ of degree $6$ with $10$ singular points $p_{1},\ldots,p_{10}$, and by performing what is called the blow - up of $\mathbb{P}^{2}$ at these points. The result is a smooth surface $X$, originally called a Coble surface. By construction, this surface possesses a holomorphic map $p:X\to\mathbb{P}^{2}$, which is almost everywhere an isomorphism. Indeed, the restriction on the open subsets $p:X\setminus p^{-1}\{p_{1},\ldots,p_{10}\}\to\mathbb{P}^{2}\setminus\{p_{1},\ldots,p_{10}\}$ is invertible, so that we can think of $p^{-1}$ as a meromorphic inverse to $p$. This surface $X$ has a nice property, that is, the automorphism group $\mathrm{Aut}(\mathrm{X})$ of holomorphic invertible transformations of $X$ in itself is infinite, see for example *[3]*, *[6]*. For each of these transformations $f:X\to X$, one can consider the composition $p\circ f\circ p^{-1}$, which is a meromorphic map of $\mathbb{P}^{2}$ in itself, undefined at $p_{1},\ldots,p_{10}$. Coble surfaces were introduced precisely with the aim to study subgroups of meromorphic transformations of $\mathbb{P}^{2}$ in itself, which was a classical topic in Algebraic Geometry in the early 20-th century. Moreover, the fact that $\mathrm{Aut}(\mathrm{X})$ is infinite is remarkable, since a conjecture of Coble himself, later proved by Hirschowitz in *[19]*, stated that, if one starts with a set of $n\geq 9$ points $p_{1},\ldots,p_{n}$ in $\mathbb{P}^{2}$, which do not satisfy any non-trivial algebraic constraint, then the blow up of $\mathbb{P}^{2}$ at these points admits only the identity automorphism. However, Coble surfaces do not contradict Hirschowitz theorem. Indeed, fixed a $10$-ple $(p_{1},\ldots,p_{10})$, we are asking that there exists a homogeneous polynomial $F(X_{0},X_{1},X_{2})$ of degree $6$ with $\frac{\partial F}{\partial X_{i}}(p_{j})=0$. One can easily show that this is actually a non trivial algebraic condition, which is not automatically satisfied by all the $10$-ples $p_{1},\ldots,p_{10}$. Those which actually satisfy this condition can be used to give rise to a Coble surface.

Nowadays, the definition of a Coble surface has been modified in the following way. To any surface $X$, one can associate an abelian group, called the Picard group $\mathrm{Pic}(\mathrm{X})$ of $X$. By definition, a divisor $D$ on $X$ is a formal linear combination $D=n_{1}C_{1}+\cdots+n_{r}C_{r}$, where $C_{i}\subset X$ are curves, and the coefficients $n_{i}\in\mathbb{Z}$ are integers. The set of divisors is an abelian group, with the addition operation. A divisor is said effective if $n_{i}\geq 0$ for all indices $i$. We want to be able to deform divisors, so we consider equivalent two

divisors $D_{1},D_{2}$ if there exists a 1-parameter deformation family $X_{\lambda}\subset X$, with $\lambda\in\mathbb{P}^{1}=\mathbb{C}\cup\{\infty\}$ which starts with $X_{0}=D_{1}$ and it terminates with $X_{\infty}=D_{2}$. This equivalence relation is called rational equivalence, and the Picard group $\mathrm{Pic(X)}$ is the group of divisors modulo rational equivalence. A crucial role in the Picard group is played by canonical divisors. A divisor $D=\sum n_{i}C_{i}-\sum_{j}m_{j}C^{\prime}_{j}$ is canonical if there exists a meromorphic differential form $\omega$ of degree 2, with zeroes of order $n_{i}$ along $C_{i}$ and poles of order $m_{j}$ along $C^{\prime}_{j}$. All canonical divisors lie in the same class of rational equivalence, denoted by $K_{X}$, the canonical class of $X$. This class contains effective divisors if and only if $X$ admits holomorphic 2-differential forms.

The modern definition for a Coble surface is stated purely in terms of the canonical divisor class $K_{X}$. Indeed, we require three conditions to a Coble surface $X$:

i) $X$ must be rational, that is, there must exist open subsets $U\subset X,V\subset\mathbb{P}^{2}$ which are isomorphic.

ii) The anti - canonical divisor class $-K_{X}$ does not contain any effective divisor.

iii) The anti - bicanonical divisor class $-2K_{X}$ contains a unique effective divisor $C=C_{1}+\cdots+C_{n}$, called the Coble curve of $X$.

The reason of this definition is that it closely resembles the definition of Enriques surfaces. This is a very well known family of surfaces, first introduced in the late 19-th century by Enriques. For an Enriques surface, the requirement $i)$ on rationality is dropped, while conditions $ii),iii)$ are required respectively for the divisors $K_{X},2K_{X}$, rather than their opposites.

Going back on Coble surfaces, the original definition given by Coble corresponds exactly to the irreducibility of the curve $C$ introduced in point iii).

In the first part of this work, we will discuss general properties of Coble surfaces, with a special focus on the case when $C$ is irreducible. We will underline many analogies between the behaviour of these surfaces and of Enriques surfaces. As an example, a very useful tool to study Enriques surfaces are isotropic sequences, see for example Knutsen *[21]*. By definition, these are sequences of isolated elliptic curves $\mathcal{E}_{1},\ldots,\mathcal{E}_{r}$ with intersection product $\mathcal{E}_{i}\mathcal{E}_{j}=1-\delta_{i,j}$. On a Coble surface, we will show that any isotropic sequence $\mathcal{E}_{1},\ldots,\mathcal{E}_{r}$ of length $r\leq 8$ can be extended to a maximal sequence $\mathcal{E}_{1},\ldots,\mathcal{E}_{10}$. Going on, we can study lots of models for projective Coble surfaces. Among these, we cite the Bordiga - Coble model, which will be a special Bordiga surface which is also a Coble surface. Another interesting model, which underlines the link between Enriques surfaces and Coble surfaces, will be the case of Coble quintics in $\mathbb{P}^{3}$. These will be quintic surfaces containing a tetrahedron, and they will be nodal along three concurrent edges. We will show that the desingularization of such a surface is actually a Coble surface in the

classical sense, and vice versa, any Coble surface admits such a polarization $|H|$. The similarities will become heavier once we will pass to the anti - adjoint linear system $|H-K_{X}|$. Using this we will come back to the classical construction of an Enriques sextic, which is nodal along all the six edges, with the extra condition that one of the vertices will be a $4th$-ple point.
The following sections will be dedicated to study of automorphisms on Coble surface, with a detailed attention to those with irreducible Coble curve $C$. For those surfaces, indeed, there exist a well - defined restriction homomorphism $\rho:\mathrm{Aut(X)}\to\mathrm{Aut(C)}\simeq\mathrm{PGL(2)}$, and there exists an open conjecture about who $ker(\rho),Im(\rho)$ might be. We will show the construction made by Pompilj in 1937, in an attempt to prove $ker(\rho)\neq 1$, and we will follow Coble counter - proof, which proved how this happens only for some families of Coble surfaces. Going on, we will focus on the case of involutions, proving that on an unnodal Coble surface $X$ with irreducible boundary $C$, any involution $i:X\to X$ is the lift of a Bertini involution. We will conclude this work by defining the coincidence loci for families of involutions, showing that they are always 2-codimensional inside the Severi variety of 10-nodal plane sextics.

##

Introduction

General setup: The main topic of Algebraic Geometry is the study of algebraic varieties. By definition, one considers the complex projective space $\mathbb{P}^{n}(\mathbb{C})=\mathbb{P}^{n}$, which is the quotient

$\mathbb{P}^{n}:=(\mathbb{C}^{n+1}\setminus\{0\})/\simeq$

where the equivalence relation $\simeq$ between nonzero vectors $v,w\in\mathbb{C}^{n+1}\setminus\{0\}$ is given by

$v\simeq w\quad\text{ if and only if }\quad w=\lambda v$

for some scalar $\lambda\neq 0$. If $(X_{0},\ldots,X_{n})\in\mathbb{C}^{n+1}$ is any vector different from zero, its equivalence class with respect to $\simeq$ will be denoted as $[X_{0},\ldots,X_{n}]$. Over the space $\mathbb{P}^{n}$, one puts the Zariski topology, where the closed subsets have the form

$V(F_{1},\ldots,F_{r}):=\{x\in\mathbb{P}^{n}\quad\text{such that }\quad F_{1}(x)=\cdots=F_{r}(x)=0\}\subset\mathbb{P}^{n}$

for a finite collection of homogeneous polynomials $F_{1},\ldots,F_{r}\in\mathbb{C}[X_{0},\ldots,X_{n}]$. The Zariski - closed subsets of $\mathbb{P}^{n}$ are called algebraic varieties. If $X\subset\mathbb{P}^{n},Y\subset\mathbb{P}^{m}$ are varieties, a regular morphism $f:X\to Y$ will be a holomorphic function which locally has a polynomial structure, that is, it can be written as

$f(x):=[H_{0}(x),\ldots,H_{m}(x)]$

for a $(m+1)$-ple of homogeneous polynomials $H_{0},\ldots,H_{m}\in\mathbb{C}[X_{0},\ldots,X_{n}]$ with the same degree and with no common zeroes. We will consider mainly curves and surfaces, which are varieties of dimension $1$ and $2$ respectively. The simplest examples are given respectively by the projective line $\mathbb{P}^{1}$ and the projective plane $\mathbb{P}^{2}$.

The closest examples are given by rational varieties. An $n$-dimensional variety $X$ is said rational if there exist open subsets $U\subset X,V\subset\mathbb{P}^{n}$ which are isomorphic via regular functions $f:U\to V,g:V\to U$. Roughly speaking, this means that $X$ admits a meromorphic polynomial parametrization from $\mathbb{P}^{n}$, which is almost everywhere an isomorphism. In dimension $1$, one can show that the only rational smooth curve is actually $\mathbb{P}^{1}$ itself, see for example *[32]*. In dimension $2$, this is no longer true: there are smooth rational surfaces which are not isomorphic to $\mathbb{P}^{2}$. During the $20$-th century, Castelnuovo, Enriques and later Kodaira provided a classification of all families of complex surfaces. A key ingredient for their work is the notion of vector bundle. The idea is the following: given a smooth complex variety $X$, one can attach to any point $x\in X$ a $\mathbb{C}$-vector space $V_{x}$, whose rank $r$ does not vary as $x$ moves

in $X$. The union $V:=\bigcup_{x\in X}V_{x}$ is still a variety, equipped with a natural surjective morphism $p:V\to X$, $p(v):=x$ if $v\in V_{x}$. As an example, one can simply consider $X\times\mathbb{C}^{r}$, which attaches to any $x\in X$ the “constant” vector space $\mathbb{C}^{r}$. Other natural constructions are given by the tangent vector bundle $\mathcal{T}_{X}\to X$, which is given by the glueing of the tangent spaces $T_{x}X,x\in X$, or its dual cotangent bundle $\Omega^{1}_{X}:=(\mathcal{T}_{X})^{*}$, or its external $p$-th power $\Omega^{p}_{X}:=\bigwedge^{p}\Omega^{1}_{X}$, for $1\leq p\leq\,\dim X$. For any vector bundle $p:V\to X$, one can look for its sections, that is, regular functions $\sigma:X\to V$ such that $\sigma(x)\in V_{x}$ for any $x\in X$. The set of such sections is a vector space itself, denoted by $H^{0}(X,V)$. In the examples above, a section of $X\times\mathbb{C}^{r}\to X$ is just a $r$-ple of regular functions $X\to\mathbb{C}$, and by a compactness argument, each of these must be a constant, so that $H^{0}(X,\mathbb{C}^{r})=\mathbb{C}^{r}$. Sections of the tangent bundle $\mathcal{T}_{X}$ are regular vector fields on $X$, and they may exist or not. A section of $\Omega^{p}_{X}$ is a holomorphic differential form of degree $p$.

A special role is played by line bundles, which are vector bundles of rank 1. The reason is the following: given two line bundles $p_{1}:L_{1}\to X,p_{2}:L_{2}\to X$, one can construct the tensor line bundle $L_{1}\otimes L_{2}$, which attaches to any point $x\in X$ the space $(L_{1}\otimes L_{2})_{x}:=(L_{1})_{x}\otimes(L_{2})_{x}$, which has still rank 1. The trivial line bundle $X\times\mathbb{C}$ plays the role of zero element with respect to this operation, and any line bundle $L\to X$ satisfies admits an inverse element, namely the dual bundle $L^{*}\to X$, which satisfies $L\otimes L^{*}\simeq X\times\mathbb{C}$. Hence the set of line bundles over a fixed variety $X$, equipped with the tensor product, has a structure of an abelian group. From now on, a line bundle $L\to X$ will be denoted by $\mathcal{O}_{X}(L)$, so that the tensor product between $\mathcal{O}_{X}(L_{1}),\mathcal{O}_{X}(L_{2})$ will become simply $\mathcal{O}_{X}(L_{1}+L_{2})$, using the additive notation which comes from the commutativity of tensor product. The dual of $\mathcal{O}_{X}(L)$ will be $\mathcal{O}_{X}(-L)$, and the trivial line bundle $X\times\mathbb{C}$ will be just $\mathcal{O}_{X}$. For any variety $X$, the top wedge power $\Omega_{X}^{\dim X}$ is called the canonical line bundle, and it is denoted as $\mathcal{O}_{X}(K_{X})$. The abelian group of line bundles on any variety $X$ is called the Picard group, and it is denoted as Pic(X).

In the Castelnuovo - Enriques - Kodaira classification of surfaces, the canonical bundle $\mathcal{O}_{X}(K_{X})=\Omega^{2}_{X}$ of a smooth surface $X$ plays a central role. As an example, Castelnuovo showed that the rationality of $X$ can be stated just in terms of $\mathcal{O}_{X},\Omega^{2}_{X}$.

The aim of this Ph.D. Thesis is the study of linear systems on Coble surfaces. Historically, they were introduced for the following reason: a classical problem in Algebraic Geometry in the early 20-th century was the study of birational transformations of the plane $\mathbb{P}^{2}$, which are meromorphic transformations of $\mathbb{P}^{2}$ in itself, with meromorphic inverse. The group of such transformations is denoted by $Cr(2)$ or $Cr(\mathbb{P}^{2})$, the Cremona group in dimension 2. Since this is a very large group, an idea was to look at some

of its subgroups, in the following way. Starting from a finite set of points $p_{1},\ldots,p_{n}$ in the plane $\mathbb{P}^{2}$, one can always build the blow up of $\mathbb{P}^{2}$ centered at $p_{1},\ldots,p_{n}$. By construction, this will be a smooth algebraic surface $X=Bl_{p_{1},\ldots,p_{n}}\mathbb{P}^{2}$, with a regular morphism $p:X\to\mathbb{P}^{2}$, with the property that $p^{-1}(p_{i})\simeq\mathbb{P}^{1}$ for all the points $p_{i}$’s, and the restriction on the complementary open subsets $p:X\setminus p^{-1}\{p_{1},\ldots,p_{n}\}\to\mathbb{P}^{2}\setminus\{p_{1},\ldots,p_{n}\}$ is invertible. Once we have our blow up $X$, any regular invertible automorphism $f:X\to X$ will induce a meromorphic transformation on $\mathbb{P}^{2}$, by considering the composition $\phi:=p\circ f\circ p^{-1}:\mathbb{P}^{2}\dashrightarrow\mathbb{P}^{2}$. The discontinuous arrow in this notation underlines that the composition is defined only as a meromorphic function, since the involved function $p^{-1}:\mathbb{P}^{2}\dashrightarrow X$ exists only over the open subset $\mathbb{P}^{2}\setminus\{p_{1},\ldots,p_{n}\}$. In this way, the group $\mathrm{Aut(X)}$ of regular transformation of $X$ in itself is identified with the subgroup of $Cr(\mathbb{P}^{2})$ of meromorphic transformation which have indeterminacies at most at prescribed points $p_{1},\ldots,p_{n}\in\mathbb{P}^{2}$. There is not too much restriction in this, since one can show that the indeterminacy locus of a meromorphic transformation $\phi:\mathbb{P}^{2}\dashrightarrow\mathbb{P}^{2}$ is always a finite set, see for example *[32]*, so you can always consider its blow up to resolve the indeterminacies of $\phi$. As the finite set $\{p_{1},\ldots p_{n}\}$ changes, the blown up surface $X$ changes too, so it has different automorphism group $\mathrm{Aut(X)}$, and we will be able to describe different subgroups of $Cr(\mathbb{P}^{2})$.

However, this strategy has some limits: if one picks too many points $p_{1},\ldots,p_{n}$, the surface $X$ may admit just the identity $\mathbbm{1}_{X}$ as automorphism into itself, so the induced subgroup in $Cr(\mathbb{P}^{2})$ would be trivial. In the early 20-th century this was just a conjecture, but Hirschowitz actually showed in *[19]* that for almost every choice of $n\geq 9$ points in the plane, the blow up $X=Bl_{p_{1},\ldots,p_{n}}\mathbb{P}^{2}$ does not admit any automorphism. Coble surfaces proved to be an exception to this fact. Indeed, they were originally defined by A. B. Coble in *[6]* as a blow up of $\mathbb{P}^{2}$ in 10 points, which must be singular points for a curve $\overline{C}\subset\mathbb{P}^{2}$ of degree 6, and nonetheless they admit nontrivial automorphisms.

Nowadays, there is another definition for Coble surfaces, purely expressed in terms of the previously mentioned line bundle $\mathcal{O}_{X}(K_{X})$, and it extends the original one given by Coble. The new definition, which we will se later, underlines how Coble surface provide a bridge between the world of rational surfaces, where they belong, and the world of Enriques surfaces. This is a class of non - rational surfaces known since the late 19-th century, and it is object of an extremely rich literature, see for example *[1]*, *[4]*, *[7]*, *[8]*, *[9]*, *[10]*, *[13]*, *[14]*, *[15]*, *[21]*, *[24]*, *[26]*, *[31]*, *[33]*, *[34]*.

##

#### Overview on the work:

The main results we will show are the following: in an unnodal Coble surface $X$ with irreducible boundary $C$, any isotropic sequence $\mathcal{E}_{1},\ldots,\mathcal{E}_{r}$ with $r\leq 8$ can be extended to a maximal isotropic sequence $\mathcal{E}_{1},\ldots,\mathcal{E}_{10}$ (Theorem 46, page 45). Under the same assumption, there are no involutions $i:X\to X$ which fix the curve $C$ (Proposition 71, page 69), and all the involutions of $\mathrm{Aut}(\mathrm{X})$ are lifts of Bertini involutions (Theorem 72, page 70).
In Section 1, we will give a brief introduction on the general setting, showing the tools we will use in all the work. A deep attention will be put upon the theory of divisors, remembering the construction of the Picard group $\mathrm{Pic}(\mathrm{X})$ for any smooth surface $X$. This group comes together a bilinear symmetric pairing $\mathrm{Pic}(\mathrm{X})\times\mathrm{Pic}(\mathrm{X})\to\mathbb{Z}$, which is just an application to surfaces of the much larger intersection theory on any kind of smooth variety. A very heavy role will be played by the canonical class divisor $K_{X}$. We will give remarks on some classical Theorems, which use this intersection product to establish some criteria for divisors to be effective, such as Riemann - Roch Theorem, or ample divisors, like the Mukai - Moishezon Criterion or Reider Theorem. Following this way, we will briefly remember some concrete application of the study of $\mathrm{Pic}(\mathrm{X})$ to rational surfaces. Among rational surfaces, a special attention will be dedicated to Del Pezzo surfaces, and the definition of some automorphisms on them, like those induced by De - Jonquieres, Geiser or Bertini involutions of $\mathbb{P}^{2}$. We will also give some basic information on the construction of the Hirzebruch surfaces $\mathbb{F}_{n}$, since they will be needed in some parts of this Thesis.
Next part will be dedicated to giving some pre-requisites on Enriques surfaces. These were first introduced during the birational classification work by Enriques and Castelnuovo, as a negative example to the following question: is the rationality of a surface $X$ an equivalent condition to the cohomological properties $h^{1}(\mathcal{O}_{X})=h^{0}(\mathcal{O}_{X}(K_{X}))=0$ ? It is well - known that this question has negative answer, since these cohomological conditions are satisfied by Enriques surfaces, which yet fail to be rational. We will briefly remember their birational model, which were originally discovered by Enriques. Namely he proved that sextic surfaces in $\mathbb{P}^{3}$ with double points along the six edges of a tetrahedron are birational models of what we call nowadays as Enriques surfaces. Other needed tools will be the Picard group $\mathrm{Pic}(\mathrm{X})$ and the numerical class group $\mathrm{Num}(\mathrm{X})$ of a general Enriques surface $X$. This will involve the definition of the lattice $\mathbb{E}_{10}$, which will show some analogies with main object of the thesis, the Coble surfaces.

In Section 2 we will finally give the definition of a Coble surface: it is a complex smooth rational surface $X$ which satisfies $h^{0}(\mathcal{O}_{X}(-K_{X}))=0$ and

$h^{0}(\mathcal{O}_{X}(-2K_{X}))=1$. For us, the Coble curve, or boundary curve, of a Coble surface $X$ will be the unique effective divisor $C\in|-2K_{X}|$, with irreducible decomposition $C=C_{1}+\cdots+C_{n}$, with $C_{i}\cap C_{j}=\emptyset$ for any $i\neq j$. It is well known that each of these surfaces comes from blowing up the projective plane $\mathbb{P}^{2}$ at a suitable number of points, placed in non-general position. We will provide examples of Coble surfaces with reducible boundary, and it was proved by Cossec, Dolgachev and Liedtke in *[9]* that $n\leq 10$ always.

Most of the work of this Thesis will be carried over Coble surfaces $X$ with irreducible boundary, that is, $n=1$. In this case, the birational description of $X$ becomes much easier, since every such surface is obtained via the blow up of $10$ points in $\mathbb{P}^{2}$ which are nodes for a reduced irreducible plane sextic curve $\overline{C}$, and conversely, every such blow up is a Coble surface. In this case, the strict transform of $\overline{C}$ becomes the Coble curve $C$. We will underline some analogies between Enriques surfaces and Coble surfaces with irreducible boundary. As an example, at a level of Picard group, the former satisfy $\mathrm{Pic(X)}=\mathbb{E}_{10}\oplus\mathbb{Z}_{2}\mathrm{K_{X}}$, while the latter satisfy $\mathrm{Pic(X)}=\mathbb{E}_{10}\oplus\mathbb{Z}\mathrm{K_{X}}$.

Another nice analogy we will find is the following: it is well known that, for an Enriques surface $X$, you can build an isotropic sequence, that is, a sequence $\mathcal{E}_{1},\ldots,\mathcal{E}_{r}$, where $\mathcal{E}_{i}\in\mathrm{Pic(X)}$ are the classes of isolated elliptic curves with intersection products $\mathcal{E}_{i}\mathcal{E}_{j}=1-\delta_{i,j}$, and that the maximum achievable value for the length $r$ is $r\leq 10$. On a Coble surface $X$ we will show that this upper bound is always achieved, namely, any isotropic sequence $\mathcal{E}_{1},\ldots,\mathcal{E}_{r}$ with $r\leq 8$ can be extended to an isotropic sequence $\mathcal{E}_{1},\ldots,\mathcal{E}_{10}$. A fundamental help in the proof will come from the fact that Coble curves always admit $(-1)$-curves, which is absolutely forbidden in Enriques surface.

We will conclude Section 2 with a brief glimpse on why it it reasonable to think that the moduli space of Coble curves with irreducible boundary has dimension $9$. To do this, we will observe that the rationality of the sextic Coble curve $\overline{C}$ provides a morphism $\mathbb{P}^{1}\to\mathbb{P}^{2}$ defined by a net in $H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))$, and hence a suitable parameter space for Coble curves is given by the Grassmannian $G=Gr(3,H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6)))$, which is $12$-dimensional. Then we will use the GIT-quotient $G//PGL(2)$.

Section 3 will be dedicated to the study of projective models of Coble surfaces with irreducible boundary curve $C\in|-2K_{X}|$. The first one will be the Bordiga-Coble model, since it is a Bordiga surface, which is also a Coble surface, since its anti - bicanonical class contains a smooth rational curve, of degree $4$ and self intersection $-4$. Actually, Bordiga-Coble surfaces are special Bordiga surfaces. Indeed, a general Coble surface is embedded in $\mathbb{P}^{4}$ via the linear system of quartic curves passing through the $10$ base points, and the image is a Bordiga surface, as mentioned.

Another interesting case is given by case of quintic Coble surfaces: by definition, these surfaces are the normalization of a quintic surface $\overline{X}\subset\mathbb{P}^{3}$ of the form

$\overline{X}$ $:=$ $\{[X_{0},X_{1},X_{2},X_{3}]\in\mathbb{P}^{3}\quad\text{such\,that}$
$\alpha X_{0}X_{2}^{2}X_{3}^{2}+\beta X_{0}X_{1}^{2}X_{3}^{2}+\gamma X_{0}X_{1}^{2}X_{2}^{2}+X_{1}X_{2}X_{3}q=0\}$

where $\alpha,\beta,\gamma$ are nonzero constants, and $q$ is a quadric in $\mathbb{P}^{3}$. The similarities with the Enriques sextic are evident. We will prove that on any Coble surface there is always a big polarization $H$ with $H^{2}=5$ which realizes such a representation, and conversely, the normalization of any such quintic surface is actually a Coble surface. The similarities with the Enriques case become even stronger if we pass to the anti - adjoint linear system $|H-K_{X}|$, which realizes $X$ as an actual Enriques sextic in $\mathbb{P}^{3}$, with the additive condition that it has a 4-ple singular point at a vertex of the coordinate tetrahedron.
We go on, introducing two other models for Coble surfaces, both in $\mathbb{P}^{3}$. The first one has degree 3, and it will be interesting since it will be the first concrete example of a nodal Coble surface, that is, a Coble surface containing a $(-2)$-curve. The second one has degree 4 and contains a double line, and we consider it as a $K3$-Coble surface, since it can be thought as a limit of smooth quartics in $\mathbb{P}^{3}$, which are special cases of $K3$ surfaces.

From Section 4 on, we start to consider biregular automorphisms of Coble surfaces. The reason why we do this is the following: any automorphism $f:X\to X$ from a Coble surface $X$ to itself must preserve the canonical divisor $K_{X}$, that is, $f_{\star}(K_{X})=K_{X}$ at a level of divisors on $X$. Multiplying by $-2$, the consequence is that $f(C)=C$, that is, $C$ is set - theoretically preserved by $f$. When $C$ is irreducible, this fact becomes strongly relevant, since it provides a restriction morphism between groups $\rho:\mathrm{Aut(X)}\to\mathrm{Aut(C)}\simeq\mathrm{PGL(2)}$. Coble posed the question about which subgroups $Ker(\rho),Im(\rho)$ can be, and in particular, he conjectured that $\ker(\rho)=\mathbb{1}_{X}$ for a general Coble surface $X$.
We will reconstruct the attempt given by G. Pompilj in 1937 in his article “Sulle trasformazioni cremoniane del piano che posseggono una curva di punti uniti” (see *[29]*). His aim was to provide a counter - example to Coble conjecture, and to do so, he proceeded in the following way. He started with an irreducible curve $\overline{C}\subset\mathbb{P}^{2}$ of degree 6, with 10 nodes in points $p_{1},\ldots,p_{7},A,B,C\in Sing(\overline{C})$. Then he considered the plane birational Bertini involution $i_{A}:\mathbb{P}^{2}\dashrightarrow\mathbb{P}^{2}$, associated to the 8-ple $p_{1},\ldots,p_{7},A$, and he observed that $i_{A}$ becomes regular when you pass to the blow - up $X$, which is our Coble surface. The same holds by symmetry for the Bertini involutions

$i_{B},i_{C}$. He then considered a triple of automorphisms $T_{A},T_{B},T_{C}:X\to X$, defined as $T_{A}:=i_{B}\circ i_{C}$, $T_{B}:=i_{C}\circ i_{A}$, $T_{C}:=i_{A}\circ i_{B}$. The automorphism $T_{A}$ can also be defined by looking at the elliptic pencil $\pi_{A}:X\to\mathbb{P}^{1}$, whose fibers are the strict transforms of sextic curves with nodes at $p_{1},\ldots,p_{7},A$. Indeed, $T_{A}$ preserves each fiber of $\pi_{A}$, as it acts simply as the addition of a divisor of degree $0$ on each smooth fiber of geometric genus $1$. Again, the same holds for $T_{B},T_{C}$ with respect to the elliptic fibrations $\pi_{B},\pi_{C}$ similarly defined. Pompilj claimed that the composition $R:=T_{C}\circ T_{B}\circ T_{A}=(i_{A}\circ i_{B}\circ i_{C})^{2}$ acts as the identity on the curve $C\in|-2K_{X}|$. We will show the path followed by Coble in *[5]*, where he proved that the condition $(i_{A}\circ i_{B}\circ i_{C})^{2}|_{C}=\mathbb{1}_{C}$ is not automatically true, as Pompilj claimed, but it is a divisorial condition in a suitable parameter space.

In the final Section 5, we will focus our attention on the biregular involutions defined on a Coble $X$, still under the assumption that $C\in|-2K_{X}|$ is irreducible. We start by a very simple observation: no involution $i$ on such a Coble surface $X$ can satisfy the Coble conjecture $i|_{C}=\mathbb{1}_{C}$. To prove this, we will use a result from Bayle - Beauville in *[2]*, which explicitly enlists all possible minimal pairs $(X,i)$, with $X$ a smooth rational surface and $i:X\to X$ a minimal involution, that is, an involution which is not induced by another pair $(X^{\prime},i^{\prime})$ by blowing up an $i^{\prime}$-symmetric finite set. It will be a straight - forward proof to show that none of the minimal models $(X,i)$ admits $X$ to be a Coble surface. Together with the hypothesis that $i|_{C}=\mathbb{1}_{C}$, this will lead us to the existence of a $(-1)$-curve $E\subset X$ such that $i(E)=E$. But then we will invoke Castelnuovo’s Contractibility Criterion, and a result from Dolgachev - Zhang in *[36]* on smoothness of fixed loci to find a contradiction.
As we already mentioned, we will also prove that any involution $i:X\to X$ is a lift of a Bertini involution, under the assumption that the Coble curve $C$ is irreducible and the surface is unnodal. Again, we will invoke the same result from *[2]*, to We will do this by a straight - forward procedure, excluding one by one all the cases provided by *[2]*. To do this, a crucial help will come from the quintic model in $\mathbb{P}^{3}$ we talked about in Section 3. In all the steps of the proof, we will show that the hypothesis of irreducibility for $|-2K_{X}|$ cannot be removed, providing examples of how all the cases actually happens when $|-2K_{X}|$ is reducible. We will also point out that the converse is not true, showing that the Bertini involution admits lifts also on Coble surfaces with reducible boundary.
The final part of this Section will be dedicated to repeating the same reasoning, but for families. We will build a suitable quasi - projective parameter space $\tilde{V}$ of triples $\tilde{V}:=\{(X,E,H)\}$, where $X$ is a Coble surface, $E\subset X$

is a $(-1)$-curve, and $|H|:X\to\mathbb{P}^{2}$ is a polarization of degree 1 which contracts $E$. In other words, $|H|$ realizes $X$ as a blow up of $\mathbb{P}^{2}$ in 10 points, and $E$ is a marked choice of one of the 10 exceptional divisors. This space will come together with a family $\pi:\mathcal{Y}\to\tilde{V}$, a divisor $\mathcal{E}\subset\mathcal{Y}$, and a line bundle $\mathcal{H}\in\mathrm{Pic}(\mathcal{Y})$, such that the pre - image of a point $\pi^{-1}(X,E,H)$ is $X$ itself, the restriction $\mathcal{E}|_{\pi^{-1}(X,E,H)}=E$ and the polarization $\mathcal{H}|_{\pi^{-1}(X,E,H)}$ is equal to $H$. On the family $\mathcal{Y}$ we will talk about rationally determined automorphism $\mathcal{G}:\mathcal{Y}\to\mathcal{Y}$, to denote biregular tranformations which live in every $\mathrm{Aut(X)}$, while $X$ moves in a family of Coble surfaces. The aim is to construct, for a rationally determined involution $\mathcal{I}:\mathcal{Y}\to\mathcal{Y}$, what is the coincidence locus of $\mathcal{I}$. By definition, this will be the set of triples $(X,E,H)$ such that $i_{C\cap E}=\mathbb{1}_{C\cap E}$, with $i:=\mathcal{I}|_{X}$. The aim of this part will be to study the geometry of this loci; invoking the classification result from Section 4, we will show that the coincidence loci are always 2-codimensional in $\tilde{V}$.

The final Appendix contains some un - finished computations, showing an alternative strategy to classify involutions on unnodal Coble surfaces with irreducible Coble curve. These calculations were made before the proof of the Proposition 71 and Theorem 72 in Section 3. The idea was to take any involution $i:X\to X$ such that $i|_{C}=\mathbb{1}_{C}$, an exceptional curve $E\subset X$, and look at the behaviour of the linear system $E+i(E)$. However, none of the proof of Section 3 requires these computations, which until now remain suspended.

##

1 Generalities on surfaces

We work on the complex field $\mathbb{C}$. A surface (respectively, a curve) will be a Zariski - closed subvariety of some projective space $\mathbb{P}^{N}$, of dimension $2$ (respectively $1$). Unless otherwise specified, we will assume that surfaces and curves are smooth and irreducible.
For any smooth irreducible variety $X$, we will denote by $\mathrm{Pic(X)}$ the Picard group of $X$, that is, the abelian group of line bundles on $X$, with group operation given by the tensor product.

### 1.1 Line bundles, divisors and intersection theory on surfaces

We refer to *[18]* for the contents of this subsection.
If $X$ is smooth and irreducible, the group $\mathrm{Div(X)}$ of divisors on $X$ is the free abelian group generated by closed subvarieties of $X$ of codimension $1$. The subgroup $\mathrm{Rat(X)}\subset\mathrm{Div(X)}$ is the group of divisors of rational functions on $X$. The Chow group of $X$ in codimension $1$ is the quotient $CH^{1}(X)=\mathrm{Div(X)}/\mathrm{Rat(X)}$.
We will repeatedly use the existence of an isomorphism

$CH^{1}(X)\simeq\mathrm{Pic(X)}.$

With some ambiguity, a divisor $D$ will be both an element in $\mathrm{Div(X)}$ and its class in $CH^{1}(X)$. The corresponding line bundle in $\mathrm{Pic(X)}$ will be denoted by $\mathcal{O}_{X}(D)$. The $i$-th cohomology space of the line bundle $\mathcal{O}_{X}(D)$ will be denoted by $H^{i}(\mathcal{O}_{X}(D))$, with the space $H^{0}(\mathcal{O}_{X}(D))$ consisting of global regular sections (provided they exist) of $\mathcal{O}_{X}(D)$. The dimension $\dim_{\mathbb{C}}H^{i}(\mathcal{O}_{X}(D))$ will be denoted by $h^{i}(\mathcal{O}_{X}(D))$.
We will denote by $K_{X}\in\mathrm{Pic(X)}$ the (isomorphism class of) the line bundle $\Omega_{X}^{dim\,X}$.

###### Theorem 1 (Serre duality)

If $D$ is any divisor on a smooth variety $X$ of dimension $n$, then for any $k\in\{0,\ldots,n\}$ we have

$h^{k}(\mathcal{O}_{X}(D))=h^{n-k}(\mathcal{O}_{X}(K_{X}-D)).$

We will denote by $K_{X}\in\mathrm{Pic(X)}$ the (isomorphism class of) the line bundle $\Omega_{X}^{dim\,X}$.
If $X$ is a surface, intersection theory provides a bilinear symmetric pairing $CH^{1}(X)\times CH^{1}(X)\to\mathbb{Z}$, which automatically induces a bilinear pairing

$\mathrm{Pic(X)}\times\mathrm{Pic(X)}\to\mathbb{Z}$. For any pair of different irreducible curves $C_{1},C_{2}$, the product $C_{1}C_{2}$ is a non-negative integer number, as it counts the cardinality of $C_{1}\cap C_{2}$ with the appropriate multiplicities. Conversely, the self-intersection $C^{2}$ of a curve $C$ can be any integer number.

The construction of $CH^{1}(X)$ is functorial: if $f:X\to Y$ is a regular morphism between smooth irreducible surface, then it induces a pull-back

$f^{*}:CH^{1}(Y)\to CH^{1}(X)$

and a push-forward

$f_{*}:CH^{1}(X)\to CH^{1}(Y).$

The pull-back $f^{*}$ of a curve $C\in CH^{1}(Y)$ is defined passing through the pull-back of the corresponding line bundle $\mathcal{O}_{Y}(C)$, while the push-forward $f_{*}$ of an effective irreducible curve $C\subset X$ is given as $f_{*}(C)=mC^{\prime}$ if $C^{\prime}\subset Y$ is the image of $C$, and $\deg{(f:C\to C^{\prime})}=m$, with the convention that $m=0$ if $f(C)$ is a point. This constructions respect the relation of linear equivalence, and satisfy

$f^{*}(C_{1})C_{2}=C_{1}f_{*}(C_{2})$

for all $C_{1}\in CH^{1}(Y),C_{2}\in CH^{1}(X)$. Moreover, if $f$ is generically finite of degree $d$, then

$f^{*}(C_{1})f^{*}(C_{2})=dC_{1}C_{2}$

for any $C_{1},C_{2}\in CH^{1}(Y)$.

### 1.2 Projective models via line bundles

For any divisor $D$, the set of effective divisors rationally equivalent to $X$ will be denoted by $|D|$. If $V\subset H^{0}(\mathcal{O}_{X}(D))$ is a linear subspace of sections, it induces a rational map $f_{|V|}:X\dashrightarrow\mathbb{P}(V^{*})\simeq\mathbb{P}^{dim\,V-1}$ in the following way. The projective dual $\mathbb{P}(V^{*})$ parametrizes hyperplanes of $V$. For any $x\in X$ define

$f_{|V|}(x):=\{\sigma\in V\,\mathrm{s.t.}\,\sigma(x)=0\}\subset V.$

This map is undefined at the base locus of $V$, which is made of common zeroes for all sections in $V$. Thus $f_{|V|}$ is a morphism if and only if $V$ is basepoint-free. If $\sigma_{0},\ldots,\sigma_{n}$ is a base for $V$, the map $f_{|V|}:X\dashrightarrow\mathbb{P}^{n}$ is given by

$f_{|V|}(x)=[\sigma_{0}(x),\ldots,\sigma_{n}(x)],$

where the evaluations $\sigma_{i}(x)$ are computed with respect to a common local trivialization of $\mathcal{O}_{X}(D)$ around $x$. Two trivializations differ by the multiplication for a nowhere zero factor around $x$, hence the projective point $f_{|V|}(x)$

is well defined, and it depends only on the choice of the basis $\sigma_{0},\ldots,\sigma_{n}$. This determines a family of different maps $f_{|V|}$, but all of them differ by the post-composition with an element in $\mathbb{P}GL(n+1)$, which acts transitively on the set of basis of $V$. This writing also makes clear that the indeterminacy locus for $f_{|V|}$ is exactly the set of common zeroes of $V$, given by $\sigma_{0}(x)=\cdots=\sigma_{n}(x)=0$.
We denote by $f_{|D|}$ the map induced choosing $V$ as the complete linear system $V=H^{0}(\mathcal{O}_{X}(D))$.

###### Definition 2

Let $X$ be any variety.
A line bundle $\mathcal{O}_{X}(D)$ is very ample if $f_{|D|}$ is a regular embedding.
A line bundle $\mathcal{O}_{X}(D)$ is ample if there exists a natural $n\geq 1$ such that $nD$ is very ample.
A line bundle $\mathcal{O}_{X}(D)$ is big if there exists a natural $n\geq 1$ such that the rational morphism $f_{|nD|}$ is birational on its image.
A divisor $D$ is nef (numerically effective) if $DC\geq 0$ for any curve $C\subset X$. A divisor $D$ is numerically equivalent to $0$ if it is orthogonal to all $\mathrm{Pic(X)}$. In this case we write $D\simeq_{num}0$.
We denote by $\mathrm{Num(X)}$ the quotient $\mathrm{Num(X)}:=\mathrm{Pic(X)}/\simeq_{\mathrm{num}}$.

 there exist a natural surjective homomorphism $\mathrm{Pic(X)}\to\mathrm{Num(X)}$, which is an isomorphism if and only if there are no nontrivial divisors $D\simeq_{num}0$. Moreover, $\mathrm{Num(X)}$ is always torsion-free, since a divisor $D$ is orthogonal to all $\mathrm{Pic(X)}$ if and only if all its multiples $mD$ are. We will use repeatedly the following facts:

###### Theorem 3 (Nakai-Moishezon Criterion)

On a surface $X$, a line bundle $\mathcal{O}_{X}(D)$ is ample if and only if $D^{2}>0$ and $DC>0$ for any curve $C\subset X$.

###### Theorem 4 (Hodge Index Theorem)

*[23]* If $\mathcal{O}_{X}(D)$ is a big line bundle on a smooth surface $X$, and $C\subset X$ is any divisor such that $DC=0$, then $C^{2}\leq 0$ and equality holds if and only if $C\simeq_{num}0$.

###### Theorem 5 (Riemann-Roch Theorem on surfaces)

If $C$ is any divisor on a smooth surface $X$, then

$h^{0}(\mathcal{O}_{X}(D))-h^{1}(\mathcal{O}_{X}(D))+h^{2}(\mathcal{O}_{X}(D))=h^{0}(\mathcal{O}_{X})-h^{1}(\mathcal{O}_{X})+h^{2}(\mathcal{O}_{X})+\frac{C(C-K_{X})}{2}$

###### Theorem 6 (Reider’s Theorem)

*[30]* Let $X$ be a smooth surface, and let $H\in\mathrm{Pic(X)}$ be a nef divisor.
Part I): If $H^{2}>4$, and the adjoint linear system $H+K_{X}$ has a base point

$p\in X$, then there exists an effective divisor $D$ containing $p$, such that one of the following statements is true:
i) $HD=0$ and $D^{2}=-1$.
ii) $HD=1$ and $D^{2}=0$.
Part II) If $H^{2}>8$ and the adjoint linear system $H+K_{X}$ does not separate two points $p,q\in X$, then there exists an effective divisor $D$ containing both $p,q$, such that one of the following statements is true:
i) $HD=0$ and $D^{2}\in\{-1,-2\}$.
ii) $HD=1$ and $D^{2}\in\{0,-1\}$.
iii) $HD=2$ and $D^{2}=0$.
iv) $H=3D$ and $D^{2}=1$.

###### Proposition 7

If $D\in\operatorname{Pic}(\mathrm{X})$ is an effective divisor, and $V\subset H^{0}(\mathcal{O}_{X}(D))$ is a subsystem with no base locus, then the map $f:=f_{|V|}:X\to\mathbb{P}^{\dim V-1}$ is a regular morphism. In this case we have

$D^{2}=(\deg f|_{X}:X\to f(X))(\deg f(X))$

and for any irreducible, reduced, effective divisor $R$, we will use

$DR=(\deg f|_{R}:R\to f(R))(\deg f(R)).$

These two formulas remain true even when $\dim f(R)<R$, adopting the convention that $\deg f(R)=0$ in this case.

###### Definition 8

For any $k>0$, a $(-k)$-curve on $X$ will be an irreducible smooth curve $C\subset X$ such that $C^{2}=-k$.
We say that a smooth surface $X$ is nodal if it contains a $(-2)$-curve.

The following fact is due to Castelnuovo, and we will use it repeatedly:

###### Theorem 9

A $(-1)$-curve on a smooth surface $X$ can be contracted. In other words, there exists a smooth surface $X^{\prime}$, a regular birational morphism $\pi:X\to X^{\prime}$, and a point $x^{\prime}\in X^{\prime}$ such that $\pi(C)=x^{\prime}$ and $\pi:X-C\to X^{\prime}-\{x^{\prime}\}$ is an isomorphism.

### 1.3 Rational surfaces

A key role will be played by rational surfaces.

###### Definition 10

A surface $X$ is rational if there exists an open subset $U\subset X$ and an open subset $V\subset\mathbb{P}^{2}$ such that $U\simeq V$.

This geometric property has a purely cohomological description, thanks to the following Criterion:

###### Theorem 11 (Castelnuovo Criterion)

A surface $X$ is rational if and only if $H^{1}(\mathcal{O}_{X})=H^{0}(\mathcal{O}_{X}(K_{X}))=H^{0}(\mathcal{O}_{X}(2K_{X}))=0$.

There are two types of rational surfaces: those which do not contain $(-1)$-curves, and those which do. A rational surface without $(-1)$-curves is a minimal rational surface.
The simplest example is the projective plane $\mathbb{P}^{2}$. The Picard group is $\mathrm{Pic(X)}=\mathbb{Z}\mathrm{L}$, where $L$ is the class of any line. The intersection product is defined by $L^{2}=1$, and the canonical class divisor is $K_{\mathbb{P}^{2}}=-3L$. For any $d>0$, the class of a curve of degree $d$ is $dL$.
Another example of minimal rational surface is the product $\mathbb{P}^{1}\times\mathbb{P}^{1}$. The fibers $F_{1},F_{2}$ of the two fibrations generate the Picard group $\mathrm{Pic}(\mathbb{P}^{1}\times\mathbb{P}^{1})=\mathbb{Z}\mathrm{F}_{1}\oplus\mathbb{Z}\mathrm{F}_{2}$, and the intersection product is given by $F_{1}^{2}=F_{2}^{2}=0$, $F_{1}F_{2}=1$. The canonical class divisor is $K_{\mathbb{P}^{1}\times\mathbb{P}^{1}}=-2F_{1}-2F_{2}$. For any pair of naturals $a,b\geq 0$, a curve of type $(a,b)$ will be a divisor in the linear system $\mathcal{O}_{\mathbb{P}^{1}\times\mathbb{P}^{1}}(a,b)$, defined by a bi-homogeneous equation of bi-degree $(a,b)$.

#### 1.3.1 Hirzebruch surfaces

The remaining minimal rational surfaces are the Hirzebruch surfaces, $\mathbb{F}_{n}$. They are defined for any $n\geq 0$ as the projectified rank-2 vector bundle $\mathcal{O}_{\mathbb{P}^{1}}\oplus\mathcal{O}_{\mathbb{P}^{1}}(-n)$ over $\mathbb{P}^{1}$. We will denote by $F$ the class of a fiber, and by $C_{-n}$ the unique negative section, given by the projectified sub-bundle $\mathbb{P}(\mathcal{O}_{\mathbb{P}^{1}})\subset\mathbb{F}_{n}$. The classes $C_{-n},F$ generate the Picard group of the surface, and the intersection product is determined by $C_{-n}^{2}=-n$, $F^{2}=0$ and $C_{-n}F=1$. The canonical class is given by $K_{\mathbb{F}_{n}}=-2C_{-n}-(n+2)F$.
For $n=0$, $\mathbb{F}_{0}$ is just $\mathbb{P}^{1}\times\mathbb{P}^{1}$, while $\mathbb{F}_{1}$ is the unique non-minimal Hirzebruch surface, because of the presence of the curve $C_{-1}$.

#### 1.3.2 Blow ups of $\mathbb{P}^{2}$

All the others rational surfaces are blow-ups of $\mathbb{P}^{2}$ or $\mathbb{F}_{n}$, with $n\neq 1$. We will deal a lot with blow-ups of $\mathbb{P}^{2}$ at $N$ points $p_{1},\ldots,p_{N}$. If $X$ is such a blow-up, then $\mathrm{Pic(X)}$ is a free abelian group, of rank $N+1$, generated by the class $L$ of a line not containing any of the $p_{i}$’s, and the exceptional curves $E_{1},\ldots,E_{N}$ over the base points. The intersection rules are $L^{2}=1,LE_{i}=0$ and $E_{i}E_{j}=-\delta_{i,j}$. Let $\pi:X\to\mathbb{P}^{2}$ be the blow-down morphism. The class of any irreducible (smooth or not) curve in $C\subset X$, different from the $E_{i}$’s, can be decomposed in this basis as $C=dL-m_{1}E_{1}\cdots-m_{N}E_{N}$, where $d>0$

is the degree of the plane curve $\pi(C)\subset\mathbb{P}^{2}$, and $m_{i}\geq 0$ is the multiplicity of $\pi(C)$ at $p_{i}$.
Conversely, any linear system of the form $|dL-m_{1}E_{1}\cdots-m_{N}E_{N}|$ contains the strict transforms of curves of degree $d$, and multiplicity at least $m_{i}$ at $p_{i}$. We will specify in any situation wether we are allowing infinitely near blow-ups, since they produce curves of self intersection lesser or equal than $(-2)$.

### 1.4 Del Pezzo surfaces

###### Definition 12

A smooth surface $X$ is a Del Pezzo surface if is rational and the anti - canonical linear system $-K_{X}$ is ample.
The self intersection $(-K_{X})^{2}$ is called the degree of the Del Pezzo surface $X$.

###### Proposition 13

Assume $X$ is a blow up of $\mathbb{P}^{2}$ at $N$ points. Then $X$ is a Del Pezzo surface if and only if $N\leq 8$, and in this case its degree is $9-N$.

The projective plane $\mathbb{P}^{2}$ and the product $\mathbb{P}^{1}\times\mathbb{P}^{1}$ are the only cases of Del Pezzo surfaces with divisible anti-canonical bundle, that is, the anti canonical is a positive multiple of another very ample line bundle.
For $\mathbb{P}^{2}$ we have

$-K_{\mathbb{P}^{2}}=3L$

which defines the Veronese embedding of $\mathbb{P}^{2}$ as a surface of degree $9$ in $\mathbb{P}^{9}$, but of course we can just pick $L$ itself as a very ample line bundle.
For $\mathbb{P}^{1}\times\mathbb{P}^{1}$ we have

$-K_{\mathbb{P}^{1}\times\mathbb{P}^{1}}=2(F_{1}+F_{2})$

which realizes $\mathbb{P}^{1}\times\mathbb{P}^{1}$ as a surface of degree $8$ inside $\mathbb{P}^{8}$. Again, we can just pick $F_{1}+F_{2}$ as a very ample line bundle, which identifies $\mathbb{P}^{1}\times\mathbb{P}^{1}$ with a smooth quadric $Q\subset\mathbb{P}^{3}$, and the embedding defined by $-K_{\mathbb{P}^{1}\times\mathbb{P}^{1}}$ is just the composition of this Segre embedding with the Veronese embedding $\mathbb{P}^{3}\to\mathbb{P}^{9}$ defined by the complete linear system of quadrics. Since $Q$ itself is one of the quadrics of the Veronese embedding, the image of the composition

$\mathbb{P}^{1}\times\mathbb{P}^{1}\to\mathbb{P}^{3}\to\mathbb{P}^{9}$

is actually contained in a hyperplane $\mathbb{P}^{8}\subset\mathbb{P}^{9}$.

#### 1.4.1 Del Pezzo surfaces of degree in $\{3,\ldots,8\}$

Each of these surfaces is obtained as a blow up of $\mathbb{P}^{2}$ in a set of $N$ points, with $N\in\{1,\ldots,6\}$. If $X$ is such a surface, with the notation we adopted we have

$\mathrm{Pic(X)}=\mathbb{Z}\mathrm{L}\oplus\mathbb{Z}\mathrm{E}_{1}\cdots\oplus\mathbb{Z}\mathrm{E}_{\mathrm{N}}$

where

and

$-K_{X}=3L-E_{1}\cdots-E_{N}$

which corresponds to the strict transforms of plane cubics passing through the $N$ base points. If the base points are in general position, the anti canonical linear system induces an embedding

$X\subset\mathbb{P}^{d}$

as a surface of degree $d$, with

$d=9-N=(-K_{X})^{2}$

An important role in this representation is played by $(-1)$-curves, thanks to the following fact:

###### Proposition 14

The $(-1)$-curves in $X$ are in $1:1$ correspondence with the straight lines of $\mathbb{P}^{d}$ contained in $X$.
Moreover, each of this surfaces contains a finite number of lines.

It is also easy to list the $(-1)$-curves in each of these surfaces, still under the assumption that the $N$ base points are in general position:
N = 1: There is only one line, the exceptional divisor of the base point.
N = 2: There are 3 lines, which live in the classes $E_{1},E_{2},L-E_{1}-E_{2}$. These curves are displaced in a chain of length 3.
N = 3: There are 6 lines, which live in the classes $E_{1},E_{2},E_{3},L-E_{1}-E_{2},L-E_{1}-E_{3},L-E_{2}-E_{3}$. They are displaced in an hexagon.
N = 4: There are 10 lines, which live in the classes $E_{1},\cdots E_{4}$ and $L-E_{i}-E_{j}$ for all pairs $i<j$.
N = 5: There are 16 lines, which live in the classes $E_{1},\cdots E_{5}$, plus all the $L-E_{i}-E_{j}$ for all pairs $i<j$, and the class $2L-E_{1}\cdots-E_{5}$.
N = 6: There are 27 lines, which live in the classes $E_{1},\cdots E_{6}$, plus all the $L-E_{i}-E_{j}$ for all pairs $i<j$, and the classes $2L-E_{1}\cdots-\hat{E}_{i}\cdots-E_{5}$.

#### 1.4.2 Del Pezzo surfaces of degree $2$, and the Geiser involution

A Del Pezzo surface of degree 2 is a blow - up of $\mathbb{P}^{2}$ at $N=7$ points $p_{1},\ldots,p_{7}$. Let $X$ be such a surface. With the notation we adopted, the linear system $-K_{X}$ is given by $-K_{X}=3L-E_{1}\cdots-E_{7}$, which consists of strict transforms of cubics through the base points $p_{1},\ldots,p_{7}$. We have

$\dim|-\mathrm{K_{X}}|=2$

thus we have the induced morphism $f_{|-K_{X}|}:X\to\mathbb{P}^{2}$. The degree of $f$ is simply given by

$\deg f=(-K_{X})^{2}=2$

This is the first case when $|-K_{X}|$ is not very ample, but just ample. The branch locus of $f$ is a smooth curve $B\subset\mathbb{P}^{2}$ of degree 4, which is a non - hyperelliptic curve of genus 3. The $(-1)$-curves in $X$ are still a finite number, namely 56, and they are in $2:1$ correspondence with the set of bitangent lines of $B$, which are 28.
Conversely, any double cover of $\mathbb{P}^{2}$ branched along such a curve $B$ is a Del Pezzo surface of degree 2. The deck involution $i$ with respect to this double cover is called Geiser involution. For any point $x\in X$, the point $i(x)$ is the ninth base point for the pencil of cubics defined by $p_{1},\ldots,p_{7},x$.
The linear system $|-2K_{X}|$ is very ample, since it induces an embedding $|-2K_{X}|:X\to\mathbb{P}^{6}$, which identifies $X$ as a surface of degree 8.

#### 1.4.3 Del Pezzo surfaces of degree $1$, and the Bertini involution

A Del Pezzo surface $X$ of degree 1 is the blow up of $\mathbb{P}^{2}$ at 8 points $p_{1},\ldots,p_{8}$. The anti - canonical divisor $-K_{X}$ has the form

$-K_{X}=3L-E_{1}\cdots-E_{8}$

so it consists of strict transforms of cubics through $p_{1},\ldots,p_{8}$. Such cubic curves form a pencil, with a ninth base point $p_{9}$, which we do not blow up. The system $-2K_{X}=6L-2E_{1}-\cdots-2E_{8}$ is made up of sextics with 8 nodes, and

$h^{0}(\mathcal{O}_{X}(-2K_{X}))=4$

Let $F,G$ be generators for $H^{0}(\mathcal{O}_{X}(-K_{X}))$, then the three forms $F^{2},FG,G^{2}$ generate $Sym^{2}H^{0}(\mathcal{O}_{X}(-K_{X}))\subset H^{0}(\mathcal{O}_{X}(-2K_{X}))$, so we can pick a fourth generator $H$ to have

$H^{0}(\mathcal{O}_{X}(-2K_{X}))=Span(F^{2},FG,G^{2},H)$

and the corresponding map

$f:=f_{|-2K_{X}|}:X\to\mathbb{P}^{3}$

takes the form

$[F^{2},FG,G^{2},H]:X\to\mathbb{P}^{3}$

If we put coordinates $[X_{0},X_{1},X_{2},X_{3}]$ on $\mathbb{P}^{3}$ we see then that the image of $X$ is the cone

$S:=\{X_{1}^{2}=X_{0}X_{2}\}$

which has the vertex $v$ in the point $v=[0,0,0,1]$. The point $p_{9}$ is defined by equations

$p_{9}=\{F=G=0\}$

on $X$, hence it is sent by $f$ on the vertex $v$:

$f(p_{9})=v$

Moreover

$\deg f=\frac{(-2K_{X})^{2}}{(\deg f(X))}=2$

so that $f$ is a double cover of the cone. The restriction of $f$ to any elliptic curve $\mathcal{E}$ in $|-K_{X}|$ is a double cover of a generatrix line of $S$, so $\mathcal{E}$ contains 4 ramification points of $f$. One of them is of course $p_{9}$, while the other 3 move with $\mathcal{E}$, hence they describe a curve $R$ in $X$. The union $R\cup p_{9}$ is the ramificarion locus of $f$, and it corresponds to the fixed locus of the deck involution, called the Bertini involution on $X$.
The $(-1)$-curves of $X$ are 240, and they are in $2:1$ correspondence with the set of plane sections of the cone which are totally tangent to the branch locus $B:=f(R)$.
Conversely, any double cover of $S$ branched on the vertex and a non - hyper-elliptic curve of genus 4 is a Del Pezzo surface of degree 1.

#### 1.4.4 The De-Jonquieres involution

We recall here the construction of the De-Jonquieres involution of degree $d$. Let $C_{d}$ be a curve of degree $d\geq 3$ in $\mathbb{P}^{2}$, with a unique singular point $p_{0}\in Sing\,C_{d}$, of multiplicity $d-2$. Consider the plane birational involution $i$ given as follows: for any line $L$ through $p_{0}$, write the divisor $C_{d}|_{L}$ as

$C_{d}|_{L}=(d-2)p_{0}+a+b$

Let $i|_{L}$ be the involution on $L$ with $a,b$ as fixed points, and let $i$ be the glueing of all the $i|_{L}$’s. Of course $i$ is undefined at $p_{0}$. Moreover, there are finitely many lines $L_{i}$ such that the restricted divisor $C_{d}|_{L_{i}}$ takes the form

$C_{d}|_{L_{i}}=(d-2)p_{0}+2p_{i}$

The points $p_{i}$ correspond to the ramification points of the double cover induced by the projection from $p_{0}$ $\pi_{p_{0}}:C_{d}\dashrightarrow\mathbb{P}^{1}$. Since $C_{d}$ has geometric genus $d-2$, the number of $p_{i}$’s is $2d-2$. Clearly $i$ is undefined along $L_{i}$ too. Let write it in coordinates: $C_{d}$ has a unhomogeneous local equation

$F_{d-2}(x,y)+F_{d-1}(x,y)+F_{d}(x,y)=0$

$F_{k}$ an homogeneous polynomial of degree $k$. The discriminant equation

$F_{d-1}^{2}-4F_{d-2}F_{d}=0$

describes the union of the lines $L_{1},\ldots,L_{2d-2}$. The involution $i$ has the form

$i(x,y)=(-x\cdot\frac{F_{d-1}+2F_{d-2}}{2F_{d}+F_{d-1}},-y\cdot\frac{F_{d-1}+2F_{d-2}}{2F_{d}+F_{d-1}}).$

The three polynomials $x(F_{d-1}+2F_{d-2}),y(F_{d-1}+2F_{d-2}),2F_{d}+F_{d-1}$ generate the net of curves of degree $d$, passing through $p_{1},\cdots,p_{2d-2}$ and having multiplicity $d-1$ at $p_{0}$.
Let $X$ be the blow up of $\mathbb{P}^{2}$ at $p_{0},\ldots,p_{2d-2}$. The surface $X$ has a fibration $|F|$ in rational curves, namely the strict transforms of lines through $p_{0}$. On $X$ the involution $i$ becomes biregular, and it preserves each fiber of $|F|$. There are exactly $2d-2$ singular fibers, given by the union of the exceptional divisor associated to $p_{i}$, and the strict transform of the line $L_{i}$. The involution $i$ switches the component of each singular fiber, fixing the unique singular point. The fixed locus is given by construction by the strict transform of $C_{d}$, which is a bisection of $|F|$.

### 1.5 Some Lattice theory

We will keep this subsection to give some preliminaries about lattice theory.

###### Definition 15

A lattice $\Lambda$ is a free abelian group of finite rank, endowed with a bilinear symmetric product $<\cdot,\cdot>:\Lambda\times\Lambda\to\mathbb{Z}$.
For $a,b\in\Lambda$, we will denote by $ab$ the product $<a,b>$.
If $\Lambda_{1},\Lambda_{2}$ are lattices, we denote by $\Lambda_{1}\oplus\Lambda_{2}$ the lattice equipped with the product $(a_{1},b_{1})(a_{2},b_{2}):=a_{1}a_{2}+b_{1}b_{2}$.
An isometry of lattices $f:\Lambda_{1}\to\Lambda_{2}$ is a $\mathbb{Z}$-isomorphism $f$ such that $f(a)f(b)=ab$ for all $a,b\in\Lambda_{1}$.

We will denote by $\mathbb{Z}^{1,10}$ the lattice of rank 11 with signature $(1,10)$, given as follows: it is generated by a list of elements $e_{0},\ldots,e_{10}$, with the products $e_{i}e_{j}=0$ for $i\neq j$, $e_{0}^{2}=1$, $e_{1}^{2}=\cdots=e_{10}^{2}=-1$. Let $k:=-3e_{0}+e_{1}+\cdots+e_{10}\in\mathbb{Z}^{1,10}$, and let its orthogonal

$k^{\perp}:=\{v\in\mathbb{Z}^{1,10}\,\mathrm{s.\,t.\,}v\cdot k=0\}.$

Since $k^{2}=-1$, it is possible to perform the Gram-Schmidt algorithm in $\mathbb{Z}^{1,10}$ to write any vector $v\in\mathbb{Z}^{1,10}$ as $v=(v+(v\cdot k)k)-(v\cdot k)k$ to show that

$\mathbb{Z}^{1,10}=k^{\perp}\oplus\mathbb{Z}k$

###### Definition 16

We denote by $\mathbb{E}_{10}$ the sublattice $\mathbb{E}_{10}:=k^{\perp}\subset\mathbb{Z}^{1,10}$.

A useful basis to deal with $\mathbb{E}_{10}$ is defined by the following elements: $\alpha_{0}:=e_{0}-e_{1}-e_{2}-e_{3},\alpha_{1}:=e_{1}-e_{2},\cdots,\alpha_{9}:=e_{9}-e_{10}$. The intersection product of this base are given by:
i) $\alpha_{i}^{2}=-2$ for all $i=0,\cdots,9$.
ii) $\alpha_{i}\alpha_{i+1}=1$ for all $i=1,\cdots,8$.
iii) $\alpha_{0}\alpha_{3}=1$.
iv) $\alpha_{i}\alpha_{j}=0$ for all other cases.

###### Definition 17

For any $\alpha\in\mathbb{E}_{10}$ with $\alpha^{2}=-2$, consider the map $\rho_{\alpha}:\mathbb{E}_{10}\rightarrow\mathbb{E}_{10}$,

$\rho_{\alpha}(x):=x+(x\cdot\alpha)\alpha$

The map $\rho_{\alpha}$ is an isometric involution of $\mathbb{E}_{10}$, meaning that $\rho_{\alpha}^{2}=\mathbb{1}$.

###### Definition 18

Let $O(\mathbb{E}_{10})$ be the orthogonal group of isometries of $\mathbb{E}_{10}$ in itself. The Weyl group $W(\mathbb{E}_{10})\subset O(\mathbb{E}_{10})$ is the subgroup generated by all the $\rho_{\alpha}$’s, with $\alpha^{2}=-2$.

 $W(E_{10})$ is a normal subgroup, since for any isometry $g\in O(\mathbb{E}_{10})$ we have $g\rho_{\alpha}g^{-1}=\rho_{g(\alpha)}$. In *[15]*, Dolgachev showed that

$O(\mathbb{E}_{10})=W(\mathbb{E}_{10})\times\pm\mathbb{1}$

### 1.6 Enriques surfaces

An important example of non-rational surfaces we will deal with are Enriques surfaces.

###### Definition 19

An Enriques surface is a smooth surface $X$ satisfying

$h^{1}(\mathcal{O}_{X})=h^{0}(\mathcal{O}_{X}(K_{X}))=0$

and

$h^{0}(\mathcal{O}_{X}(2K_{X}))=1.$

###### Proposition 20

On an Enriques surface $X$, the canonical divisor is a $2$-torsion element in $\mathrm{Pic(X)}$, that is,

$2K_{X}=0.$

The classical example of an Enriques surface is the following:

###### Proposition 21

Let $T\subset\mathbb{P}^{3}$ be the tetrahedron

$T:=\bigcup_{0\leq i<j\leq 3}\{X_{i}=X_{j}=0\}$

and let $\overline{X}\subset\mathbb{P}^{3}$ be a surface of degree $6$ with double points along all lines in $T$. If $\overline{X}$ is generic, then the normalization $\nu:X\to\overline{X}$ is a smooth Enriques surface.

Enriques surfaces are the best known example of surfaces with $\mathrm{Pic(X)}\neq\mathrm{Num(X)}$. Indeed, since $K_{X}$ is a torsion divisor, we have $K_{X}D=0$ for any $D\in\mathrm{Pic(X)}$.

###### Proposition 22

For an Enriques surface $X$, the subgroup in $\mathrm{Pic(X)}$ of divisors numerically equivalent to $0$ coincides with the subgroup $\mathbb{Z}_{2}$ generated by $K_{X}$. As a consequence,

$\mathrm{Pic(X)}=\mathrm{Num(X)}\oplus\mathbb{Z}_{2}\mathrm{K_{X}}$

###### Theorem 23

*[8]* For an Enriques surface $X$, the lattice $\mathrm{Num(X)}$ is isometric to $\mathbb{E}_{10}$.

One of the most known invariants to classify polarized Enriques $(X,H)$ surfaces is the following:

###### Definition 24

A polarized Enriques surface is a pair $(X,H)$, with $H\in\mathrm{Pic(X)}$ the class of a big and nef divisor.
The $\phi$-invariant of the polarized pair $(X,H)$ is by definition:

$\phi(H):=\,\min\,\{H\mathcal{E},\,\mathrm{with}\,\mathcal{E}\,\mathrm{a}\,\mathrm{rigid}\,\mathrm{elliptic}\,\mathrm{curve}\,\mathrm{in}\,X\}$

The previous definition is always well defined, as any Enriques surface contains rigid elliptic curves $\mathcal{E}$. These are also known as half - fibers, as the double $|2\mathcal{E}|$ can always move in a basepoint - free pencil of elliptic curves, which has exactly two double fibers, namely $\mathcal{E}$ and $\mathcal{E}+K_{X}$.
Moreover, it was shown in *[9]* that the equality $\phi(H)=1$ corresponds to a polarization $H$ with base points, since otherwise we the polarization $H$ would induce an isomorphism between a smooth elliptic curve $\mathcal{E}$ and $\mathbb{P}^{1}$. Moreover, the authors also classify which classes $H\in\mathbb{E}_{10}$ actually correspond to big and nef polarizations which achieve $\phi(H)=1$.
The next value $\phi(H)=2$ is achieved for example by Enriques surfaces $(X,H)$ which arise from Proposition 21, with $H$ the natural polarization induced from $\mathcal{O}_{\mathbb{P}^{3}}(1)$. Indeed, the normalizations of all the $6$ edges of the tetrahedron $T$ are rigid elliptic curves, and they are double covers over the corresponding lines.
The next value $\phi(H)=3$ plays a special role:

###### Definition 25

We call $(X,H)$ a Fano polarization if $H^{2}=10$ and $\phi(H)=3$.
One immediately sees that a Fano polarization provides a map $|H|:X\to\mathbb{P}^{5}$.
A Fano polarization $(X,H)$ is called a Fano - Reye polarization if the image of $X$ is contained in a smooth quadric hypersurface of $\mathbb{P}^{5}$.

The reason of the previous definition is the following: we know that $\mathrm{Num}(\mathrm{X})=\mathbb{E}_{10}$ has rank $10$. Assume for a moment that we able to find a sequence $\mathcal{E}_{1},\ldots,\mathcal{E}_{10}$ of half - fibers, with intersection products $\mathcal{E}_{i}\mathcal{E}_{j}=1-\delta_{i,j}$. Such a sequence is known in literature as a maximal isotropic sequence. By a purely lattice - theoretical argument, the $\mathbb{Q}$-divisor $H:=\frac{1}{3}(\mathcal{E}_{1}+\cdots+\mathcal{E}_{10})\in\mathbb{E}_{10}\otimes\mathbb{Q}$ is integer, that is, it actually belongs to $\mathbb{E}_{10}$, and it satifies $H^{2}=10$ and $\phi(H)=3$. The minimum product $H\mathcal{E}=3$ is achieved for example on all the $\mathcal{E}_{i}$’s.
Of course this works provided a maximal isotropic sequence of half - fibers, which not always exists. Moreover, it is a very hard work to find the maximal lengths for such sequences, see for example *[4]*, *[21]*, *[26]*.
The definition of a Fano - Reye polarization in 25 is due to the following construction:

###### Definition 26

*[10]* *[31]* Let $W\subset H^{0}(\mathcal{O}_{\mathbb{P}^{3}}(2))$ be a vector space of dimension $4$ of quardrics of $\mathbb{P}^{3}$. The surface

$Reye(W):=\{l\in Gr(1,\mathbb{P}^{3})\,\mathrm{s.\,t.\,}l\subset Bs(|P|)\,\mathrm{for\,a\,pencil\,}|P|\subset|W|\}\subset$
$\subset Gr(1,\mathbb{P}^{3})\subset\mathbb{P}^{5}$

is called a classical Reye congruence.

The following fact is very well - known:

###### Theorem 27

*[7]* If $W\subset H^{0}(\mathcal{O}_{\mathbb{P}^{3}}(2))$ is a general $4$-dimensional $\mathbb{C}$-vector subspace, then $Reye(W)$ is a smooth nodal Enriques surface, of degree $10$ in $\mathbb{P}^{5}$.

It is also a very recent result that also the converse is true:

###### Theorem 28

*[24]* A smooth nodal Enriques surface always admits a Fano - Reye polarization, although it need not be a classical Reye congruence.

##

2 Coble surfaces

Now we introduce the main object of this work:

###### Definition 29

A Coble surface is a smooth rational projective surface $X$ whose canonical divisor $K_{X}$ satisfies two properties:
1. $h^{0}(\mathcal{O}_{X}(-K_{X}))=0$,
2. $h^{0}(\mathcal{O}_{X}(-2K_{X}))=1$.

We refer to *[16]* for the above definition. The definition clearly points out some analogy between Coble surfaces and Enriques surfaces, to be especially reconsidered in this thesis. Note also that $-2K_{X}$ is a non zero effective divisor. Otherwise $-K_{X}$ would be a non trivial 2-torsion element of $\operatorname{Pic}(X)$: against the rationality of $X$.

###### Definition 30

The unique effective curve $C\in|-2K_{X}|$ is often called Coble curve, or boundary curve of the surface $X$.
The irreducible decomposition of $C$ is the equality

$C=C_{1}+\cdots+C_{n},$ (1)

whose summands are irreducible curves with two by two distinct supports.

### 2.1 First properties and examples

Definition 29 above differs from the one given by Dolgachev and Zhang in *[36]*, where the condition $h^{0}(\mathcal{O}_{X}(-2K_{X}))=1$ is weakened to $h^{0}(\mathcal{O}_{X}(-2K_{X}))\geq 1$. However, the authors showed the following fact:

###### Proposition 31

Let $X$ be a smooth rational surface with $h^{0}(\mathcal{O}_{X}(-K_{X}))=0$ and $h^{0}(\mathcal{O}_{X}(-2K_{X}))\geq 1$. Then every divisor in $|-2K_{X}|$ is simple normal crossing.

Proposition 31 has quite remarkable consequences. Indeed, let $D$ be any divisor in $|-2K_{X}|$. Since $D$ is simple normal crossing, it does not admit multiple components. Moreover, for any singular point $p\in Sing(D)$ there are two cases:
$i)$ either $p$ belongs to a unique irreducible component of $D$, and it is a simple node for that component;
$ii)$ or $p$ belongs to exactly two irreducible components of $D$, it is a smooth point for both of them, and the intersection is transverse.
Consequently, let $p_{1},\ldots,p_{n}$ be the collection of all singularities of $D$, and let $\bar{X}:=Bl_{p_{1},\ldots,p_{n}}X$ be the blow up of $X$ at $p_{1},\ldots,p_{n}$, with exceptional

components $E_{1},\ldots,E_{n}\subset\tilde{X}$. Let $\tilde{D}\subset\tilde{X}$ be the strict transform of $D$. We claim that $\tilde{X}$ is a Coble surface with respect to Definition 29. Indeed, let $p:\tilde{X}\to X$ be the blow down of the exceptional curves $E_{1},\ldots,E_{n}$ onto $p_{1},\ldots,p_{n}$. Then

$K_{\tilde{X}}=p^{*}K_{X}+E_{1}+\cdots+E_{n}.$

If $|-K_{\tilde{X}}|$ was effective, its members would be sent via $p$ on effective members of $|-K_{X}|$, but this is empty. Hence $|-K_{\tilde{X}}|=\emptyset$. Moreover, since the points $p_{1},\ldots,p_{n}$ are ordinary double points for $D$, the divisor $\tilde{D}$ is smooth, and it belongs to the class:

$\tilde{D}=p^{*}D-2E_{1}-\cdots-2E_{n}=-2(p^{*}K_{X}+E_{1}+\cdots+E_{n})=-2K_{\tilde{X}}$

To prove the claim, we only need to show that $\tilde{D}$ cannot move in $\tilde{X}$. To do so, we will use the following Proposition, which was proved by Dolgachev and Zhang in *[36]*.

###### Proposition 32

Let $\{C\}=|-2K_{X}|$ be the Coble curve in a Coble surface $X$, with irreducible decomposition $C=C_{1}+\cdots+C_{n}$.
If the divisor $C$ is smooth, then:
i) the $C_{i}$’s are smooth rational curves,
ii) $C_{i}^{2}=-4$,
iii) $K_{X}^{2}=-n$.

Before proving Proposition 32, we will use it to show that the divisor $\tilde{D}$ can not move, so that $h^{0}(\mathcal{O}_{\tilde{X}}(-2K_{\tilde{X}}))=1$. It suffices to consider the short exact sequence

$0\to\mathcal{O}_{\tilde{X}}\to\mathcal{O}_{\tilde{X}}(\tilde{D})\to\mathcal{O}_{\tilde{D}}(\tilde{D})\to 0$

By Proposition 32, the divisor $\tilde{D}$ has the form $\tilde{D}=C_{1}+\cdots+C_{n}$, with $C_{i}\simeq\mathbb{P}^{1}$ and $C_{i}C_{j}=-4\delta_{i,j}$, so the right - hand term equals $\bigoplus_{i=1}^{n}\mathcal{O}_{\mathbb{P}^{1}}(-4)$. As a consequence, the associated long exact sequence establishes an isomorphism $H^{0}(\mathcal{O}_{\tilde{X}})\simeq H^{0}(\mathcal{O}_{\tilde{X}}(\tilde{D}))$. Thus we showed that any Coble surface in the weak sense can be blown up to a Coble surface with respect to Definition 29, and that the divisor $\{C\}=|-2K_{X}|$ can be taken smooth. From now on, we will always assume this to be true for any Coble surface we will consider.

Proof of Proposition 32: i) We use the short exact sequence

$0\to\mathcal{O}_{X}(-C_{1}-\cdots-C_{n})\to\mathcal{O}_{X}\to\bigoplus_{i=1}^{n}\mathcal{O}_{C_{i}}\to 0$

Since $X$ is rational, the long exact sequence gives:

$0\to\bigoplus_{i=1}^{n}H^{1}(\mathcal{O}_{C_{i}})\to H^{2}(\mathcal{O}_{X}(-C_{1}-\cdots-C_{n}))\to\cdots$

But by Serre’s duality

$H^{2}(\mathcal{O}_{X}(-C_{1}-\cdots-C_{n}))=H^{2}(\mathcal{O}_{X}(2K_{X}))=H^{0}(\mathcal{O}_{X}(-K_{X}))=0$

which forces

$H^{1}(\mathcal{O}_{C_{i}})=0.$

ii) From one side, part $i)$ gives

$C_{i}^{2}+C_{i}K_{X}=-2$

But from the other side,

$C_{i}^{2}+C_{i}K_{X}=C_{i}^{2}-\frac{1}{2}C_{i}(C_{1}+\cdots+C_{n})=\frac{1}{2}C_{i}^{2}$

hence we have the thesis.
iii) We start from the equality

$-2K_{X}=C_{1}+\cdots+C_{n}$

and taking the square of both sides, by part $ii)$, we have

$4K_{X}^{2}=-4n.\quad\square$

The following Proposition states which are the negative curves inside a Coble surface. The reader is referred to *[14]* for a proof.

###### Proposition 33

Let $X$ be a Coble surface, with Coble curve $C=\{C_{1}+\cdots+C_{n}\}$. If $D\subset X$ is an irreducible curve with $D^{2}<0$, then $D$ is a smooth rational curve with

$D^{2}\in\{-1,-2,-4\}$

and

$D^{2}=-4\,\text{iff}\,D\in\{C_{1},\ldots,C_{n}\}$

Proof: Assume $D$ is not one of the $C_{i}$’s, and let $p_{a}(D),p_{g}(D)$ be its algebraic and geometric genus respectively. By the adjunction formula $D^{2}+DK_{X}=2p_{a}(D)-2$. Since $C\in|-2K_{X}|$ is effective, we have then

$DK_{X}\leq 0$

so

$2p_{a}(D)-2\leq D^{2}<0$

This forces

$p_{a}(D)=0$

and

$D^{2}\in\{-1,-2\}$

The equality $p_{a}(D)=0$ also forces $p_{g}(D)=0$, which means that $D$ is both rational and smooth. $\square$

###### Proposition 34

*[14]* *[28]* Every Coble surface $X$ can be constructed as the blow-up $X\to\mathbb{P}^{2}$ in a finite set $\Sigma\subset\mathbb{P}^{2}$, which can possibly contain infinitely near points.
The image $\overline{C}\subset\mathbb{P}^{2}$ of the anti - bicanonical curve $C\in|-2K_{X}|$ has degree $6$, and all its components are rational curves.
There exists an upper bound for the number $n$ of components of $C=C_{1}+\cdots+C_{n}$, and it is $n\leq 10$.

We briefly remark that, when a smooth surface is blown up at a point, the self - intersection of the canonical divisor drops by $1$. As a consequence, for a Coble surface $X\simeq Bl_{\Sigma}\mathbb{P}^{2}$ we find $K_{X}^{2}=K_{\mathbb{P}^{2}}^{2}-|\Sigma|=9-|\Sigma|$. This fact implies that $|\Sigma|=n+9$ and hence the following property:

###### Proposition 35

Let $X$ be a smooth Coble surface such that $\{C\}=|-2K_{X}|$ is smooth and irreducible, then $X$ is the blow up of $\mathbb{P}^{2}$ at $10$ distinct point.

Historically speaking, that is exactly how Coble surfaces came out for the first time. In 1917 Coble himself posed the following question: if $\Sigma$ is a finite set of points in $\mathbb{P}^{2}$, how can we describe the automorphism group $\mathrm{Aut}(\mathrm{Bl}_{\Sigma}\mathbb{P}^{2})$ ? The answer depended on the cardinality $|\Sigma|$ of the chosen set. For $|\Sigma|\leq 8$ it was already well - known that the study of $\mathrm{Aut}(\mathrm{Bl}_{\Sigma}\mathbb{P}^{2})$ was linked to the study of the Del Pezzo surfaces, which are by definition surfaces whose anti - canonical divisor is ample.
On the other hand, for $|\Sigma|\geq 9$, the answer was given later by the following theorem:

###### Theorem 36 (Hirschowitz)

*[19]* A general set $\Sigma$ of points in $\mathbb{P}^{2}$ with $|\Sigma|\geq 9$ satisfies

$\mathrm{Aut}(\mathrm{Bl}_{\Sigma}\mathbb{P}^{2})=\mathbb{1}$

Coble was looking for non general configurations $\Sigma$ such that $|\Sigma|\geq 9$ and the group $\mathrm{Aut}(\mathrm{Bl}_{\Sigma}\mathbb{P}^{2})$ is nontrivial. Finite subsets of $\mathbb{P}^{2}$ with this property are known as Cremona - special subsets, and are deeply described by Cantat - Dolgachev, see for example *[3]*.

###### Lemma 37

*[3]* If $\overline{C}\subset\mathbb{P}^{2}$ is an irreducible sextic curve with nodes at ten points $p_{1},\ldots,p_{10}$, then

$X:=Bl_{p_{1},\ldots,p_{10}}\mathbb{P}^{2}$

is a Coble surface, and $\mathrm{Aut(X)}$ is an infinite discrete group.

This was actually the original definition for a Coble surface, given by Coble himself in *[6]*, and it was later generalized to Definition 29, so to include also reducible sextics, with more than 10 nodes.
 for a generic finite subset $\Sigma\subset\mathbb{P}^{2},|\Sigma|=10$, there is no sextic $\overline{C}$ nodal at $\Sigma$, because 10 nodes correspond to 30 generally indipendent linear conditions over the $\mathbb{C}$-vector space $H^{0}(\mathcal{O}_{\mathbb{P}^{2}}(6L))$, which has dimension 28. When $\overline{C}$ actually does exist, the surface $X:=Bl_{\Sigma}\mathbb{P}^{2}$ satisfies the requirements of Definition 29. In this case, the Coble curve $C$ is the proper transform of $\overline{C}$ in $X$.
Vice versa, if $X$ is a Coble surface (with respect to Definition 29), and $\pi:X\to\mathbb{P}^{2}$ is a blow-down map, then

$K_{X}=-3L+E$

where $L$ is the hyperplane section of $\mathbb{P}^{2}$, and the support of $E$ is contracted by $\pi$. If we put ourselves in the simplest situation, where we have no infinitely near points, then $E$ is a smooth divisor, and the requirement

$h^{0}(\mathcal{O}_{X}(-2K_{X}))=h^{0}(\mathcal{O}_{X}(6L-2E))=1$

correspond exactly to the existence of a sextic curve with nodes at the points in $\pi(E)$.
Meanwhile, the condition

$h^{0}(\mathcal{O}_{X}(-K_{X}))=h^{0}(\mathcal{O}_{X}(3L-E))=0$

requires that no plane cubic curve contains all the points in $\pi(E)$.

###### Example 38

We will show in this example how to build a Coble surface $X$ whose Coble curve $\{C\}=|-2K_{X}|$ has $n=2$ irreducible components. We know that we need to start with a sextic curve $\overline{C}\subset\mathbb{P}^{2}$ whose irreducible components are all rational. Moreover, the number of these components must necessarily be equal to $2$. Thus there are only three possibilities:
i) $\overline{C}=\overline{C}_{5}+L$, where $\overline{C}_{5}$ is a rational quintic curve and $L$ is a line.
ii) $\overline{C}=\overline{C}_{4}+C_{2}$, where $\overline{C}_{4}$ is a rational quartic, and $C_{2}$ is a smooth conic.
iii) $\overline{C}=\overline{C}_{3}^{(1)}+\overline{C}_{3}^{(2)}$, where $C_{3}^{(i)}$ are two rational cubics.
If we assume that the singularities of $\overline{C}_{5},\overline{C}_{4},\overline{C}_{3}^{(i)}$ are just simple nodes, the

rationality forces $6$ nodes for $\overline{C}_{5}$, $3$ nodes for $\overline{C}_{4}$ and $1$ node for each $\overline{C}_{3}^{(i)}$. In total, each of these models has $11$ nodes. The blow up $X=Bl_{11}\mathbb{P}^{2}$ gives a Coble surface, where the strict transforms of the two components of $\overline{C}$ become the disjoint components of the Coble curve $C\in|-2K_{X}|$. The condition $|-K_{X}|=\emptyset$ corresponds to asking that no cubic curve passes through all the $11$ base points, and this is assured by counting the intersection multiplicities with the components of $\overline{C}$.

###### Remark 39

The three cases in this example do not exhaust all the possible constructions for a Coble surface with two boundary components: there is another remaining case. Let $p_{1},\ldots,p_{8}\in\mathbb{P}^{2}$ be eight points in general position, and let $\overline{X}$ be their blow up

$\overline{X}:=Bl_{p_{1},\ldots,p_{8}}\mathbb{P}^{2}.$

With the usual notation for the lattice $\mathrm{Pic(X)}$, a dimensional count shows that

$h^{0}(\mathcal{O}_{\overline{X}}(6L-2E_{1}-\cdots-2E_{7}-3E_{8}))=1$

This divisor class contains the strict transform of the unique plane sextic curve with nodes at $p_{1},\ldots,p_{7}$ and a triple point at $p_{8}$. Let $D\subset\overline{X}$ be this divisor. Then the sum $D+E_{8}$ equals

$D+E_{8}=6L-2E_{1}\cdots-2E_{8}=-2K_{\overline{X}}$

and the two components meet at $DE_{8}=3$ points. $D$ is a $(-1)$-curve too. Let $X$ be the blow up of the three intersection points of $D,E_{8}$, and let $\tilde{D},\tilde{E}_{8}\subset X$ be their strict transforms. Then

$\tilde{D}+\tilde{E}_{8}=-2K_{X}$

and the two components are disjoint $(-4)$-curves, so that $X$ is again a Coble surface. the total number of points we blew up is still $11$.

###### Example 40

We now describe the costruction of a Coble surface $X$ with $n=6$ irreducible components in the anti - bicanonical divisor $|-2K_{X}|$. We already know we need to start with a plane sextic curve $\overline{C}\subset\mathbb{P}^{2}$, but now we choose it in a very peculiar way, that is $\overline{C}=L_{1}\cup\cdots\cup L_{6}$ is the union of six plane lines in general position. If the lines $L_{i}$ are general enough, the reducible curve $\overline{C}$ will have $\binom{6}{2}=15$ singular points, namely the intersections of different components. Then let $X:=Bl_{15}\mathbb{P}^{2}$ be the blow up of the plane at these points. The strict transform $C_{i}\subset X$ of each $L_{i}$ is a curve of self - intersection $-4$, since we blew $5$ points on $L_{i}$, and of course $C_{i}\cap C_{j}=\emptyset$.

##

It is also easy to show that Coble surfaces of this type are degenerations of Coble surfaces with irreducible anti - bicanonical divisor. Indeed, let $V\subset\mathbb{P}^{6}$ be the Del Pezzo surface of degree $6$, and let $V^{*}\subset\mathbb{P}^{6^{*}}$ the dual variety, that is

$V^{*}:=\{H\subset\mathbb{P}^{6}\mathop{\rm such\,that}H\mathop{\rm is\,tangent}\nolimits\rm to\,V\}$

Pick two disjoint linear subspaces $\Lambda,\Gamma\subset\mathbb{P}^{6}$ with $\dim\Lambda=2,\dim\Gamma=3$, and $\Gamma\cap V=\emptyset$ and consider the projection from $\Gamma$,

$\pi_{\Gamma}:\mathbb{P}^{6}\setminus\Gamma\to\Lambda\simeq\mathbb{P}^{2}$

The embedding $V\subset\mathbb{P}^{6}$ is determined by the anti canonical divisor of $V$, hence the generic hyperplane sections of $V$ is a smooth elliptic curve. If $H\in V^{*}$, then the intersection $V\cap H$ is a curve of degree $6$ and geometric genus $0$. Then $\pi_{\Gamma}(V\cap H)$ has the same degree and geometric genus, hence $\pi_{\Gamma}(V\cap H)$ is an irreducible rational sextic plane curve, for a generic $H\in V^{*}$. But now we recall that $V$ contains a very peculiar section $H_{0}$, consisting of an hexagon of lines

$V\cap H_{0}=L^{\prime}_{1}+\cdots+L^{\prime}_{6}$

with

$L_{i}\cap L_{j}=1\mathop{\rm if}|i-j|=1\mathop{\rm mod}6$

and

$L^{\prime}_{i}\cap L^{\prime}_{j}=0\mathop{\rm if}|i-j|\geq 2\mathop{\rm mod}6$

The projection $\pi_{\Gamma}$ is linear, hence $\pi_{\Gamma}(L^{\prime}_{1}+\cdots+L^{\prime}_{6})$ consists of $6$ plane lines. Thus, we can fix a quasi-projective curve $R\subset V^{*}$ passing through the point corresponding to $H_{0}$, and we get an induced family of plane sextics, with a central element which is totally reducible.

###### Example 41

It is easy to show an example of a Coble surface with a maximal number $n=10$ of irreducible components in the anti - bicanonical divisor. Let $S$ be the Del Pezzo surface of degree $5$ obtained blowing up $4$ points $p_{1},p_{2},p_{3},p_{4}$ of $\mathbb{P}^{2}$, with no three of them collinear. It is well known that the linear system $-K_{S}$ defines a regular map $j:S\to\mathbb{P}^{5}$, which identifies $S$ as a quintic surface inside $\mathbb{P}^{5}$. We denote by $E_{1},E_{2},E_{3},E_{4}\subset S$ the exceptional curves associated to the $4$ base points; for each couple $(i,j)$ with $1\leq i<j\leq 4$ let $L_{i,j}\subset S$ be the strict transform of the line through $p_{i},p_{j}$. The curves $E_{i},L_{i,j}$ are smooth rational $(-1)$-curves in $S$, and hence the linear system $|-K_{S}|$ embeds them as lines in $\mathbb{P}^{5}$. In total we have $10$ lines, and each of them touches $3$ of the others, leading to $15$ total intersection points. Let

$\pi:S^{\prime}\to S$

be the blow up of these $15$ points. Then $S^{\prime}$ is a Coble surface. Indeed, let us denote by $F_{1},\ldots,F_{15}\subset S^{\prime}$ the new exceptional curves. We have

$-K_{S^{\prime}}=\pi^{*}(-K_{S})-F_{1}-\cdots-F_{15}=\pi^{*}\mathcal{O}_{S}(1)-F_{1}-\cdots-F_{15}$

Since no hyperplane of $\mathbb{P}^{5}$ contains all the $15$ intersection points, we have $|-K_{S^{\prime}}|=\emptyset$. On the other hand, the relation

$\sum_{i}E_{i}+\sum_{i,j}L_{i,j}=-2K_{S}$

holds in $\mathrm{Pic(S)}$, and the divisor on the left hand side is nodal at the $15$ points. If $\overline{E}_{i},\overline{L}_{i,j}\subset S^{\prime}$ are the strict transforms of the $10$ lines, then

$\sum_{i}\overline{E}_{i}+\sum_{i<j}\overline{L}_{i,j}=\pi^{*}(\sum_{i}E_{i}+\sum_{i,j}L_{i,j})-2F_{1}-\cdots-2F_{15}=-2K_{S^{\prime}}$

so that

$|-2K_{S^{\prime}}|\neq\emptyset$

The $K3$ double cover $V\to S^{\prime}$ branched over the smooth divisor $\sum_{i}\overline{E}_{i}+\sum_{i<j}\overline{L}_{i,j}$ is called the Vinberg “most algebraic” $K3$ surface, see for example *[14]*,*[34]*, and it is a “rigid” surface. Indeed, its moduli are determined only by the choice of the first $4$ points $p_{1},p_{2},p_{3},p_{4}\in\mathbb{P}^{2}$, but you can always move a $4$-ple of $\mathbb{P}^{2}$ to another one by an element of $PGL(3)$.

### 2.2 An extension result

The following is a nice property of $(-1)$-curves on a Coble surfaces.

###### Proposition 42

Let $X$ be an unnodal Coble surface with irreducible Coble curve $\{C\}=|-2K_{X}|$, and let $E_{1},\ldots,E_{s}\subset X$ be a set of disjoint $(-1)$-curves, with $s\leq 8$. Then it can be completed to a $10$-ple $E_{1},\ldots,E_{10}$ of pairwise disjoint $(-1)$-curves, such that the blowing down of $E_{1},\ldots,E_{10}$ is $\mathbb{P}^{2}$.

Proof: Let’s extend $E_{1},\ldots,E_{s}$ to a family $E_{1},\ldots,E_{r}$ satisfying $E_{i}E_{j}=-\delta_{i,j}$ of maximal length $r$, with $r\geq s$. Let

$\pi:X\to\overline{X}$

be the contraction of all the $E_{i}$’s. Since $X$ is unnodal, the smooth rational surface $\overline{X}$ is minimal, which forces either

$\overline{X}=\mathbb{P}^{2}$

$\overline{X}=\mathbb{F}_{m},m\neq 1$

where $\mathbb{F}_{m}$ denotes the $m$-th Hirzebruch surface.
The first step is to exclude $\mathbb{F}_{m}$ for $m\geq 2$. This $\mathbb{F}_{m}$ contains a $(-m)$-curve, which would force $X$ to contain a curve $D$ with $D^{2}\leq-2$. Since $X$ is unnodal, $D$ should be the anti-bicanonical curve. But then the curve $\pi(D)$ is nodal, a contradiction since the $(-m)$-curve in $\mathbb{F}_{m}$ is smooth.
Then we are left with only two cases:

$\overline{X}=\mathbb{P}^{2}$

or

$\overline{X}=\mathbb{F}_{0}=\mathbb{P}^{1}\times\mathbb{P}^{1}$

Of course

$K_{X}=\pi^{*}K_{\overline{X}}+E_{1}+\cdots+E_{r}$

and taking squares one finds:

$-1=K_{X}^{2}=K_{\overline{X}}^{2}-r$

which gives

$\overline{X}=\mathbb{P}^{2}\operatorname{iff}r=10$

and

$\overline{X}=\mathbb{P}^{1}\times\mathbb{P}^{1}\operatorname{iff}r=9$

In the first case we are done.
In the second case we extended $E_{1},\ldots,E_{s}$ to a collection $E_{1},\ldots,E_{9}\subset X$ of disjoint $(-1)$-curves, and the blowing down of $E_{1},\ldots,E_{9}$ is $\mathbb{P}^{1}\times\mathbb{P}^{1}$. Let

$\pi:X\to\mathbb{P}^{1}\times\mathbb{P}^{1}$

be the blow down map, with

$p_{1},\ldots,p_{9}\in\mathbb{P}^{1}\times\mathbb{P}^{1}$

the points

$p_{i}:=\pi(E_{i})$

 a fiber $F$ of one of the two rulings of $\mathbb{P}^{1}\times\mathbb{P}^{1}$ cannot contain two distinct $p_{i},p_{j}$, otherwise the strict transform of $F$ in $X$ is a $(-2)$-curve, which is forbidden by hypothesis.
Using this, and the fact that $s\leq 8$, we can blow up $p_{9}$ on $\mathbb{P}^{1}\times\mathbb{P}^{1}$ and

low down the fibers $F_{1},F_{2}$ of the two rulings through $p_{9}$. This substitutes $\mathbb{P}^{1}\times\mathbb{P}^{1}$ with the required $\mathbb{P}^{2}$. The final family of $(-1)$-curves will be $E_{1},\ldots,E_{8},F_{1},F_{2}$. $\square$

 $s<9$ is a sharp condition. Indeed, given a curve $\overline{C}\subset\mathbb{P}^{1}\times\mathbb{P}^{1}$ of type $(4,4)$ with nodes in $9$ points $p_{1},\ldots,p_{9}\in\mathbb{P}^{1}\times\mathbb{P}^{1}$, we can consider the blow up $X:=Bl_{p_{1},\ldots,p_{9}}\mathbb{P}^{1}\times\mathbb{P}^{1}$. Then $X$ is a Coble surface, but the family $E_{1},\ldots,E_{9}$ of exceptional curves associated to $p_{1},\ldots,p_{9}$ cannot be extended to a $10$-ple with the desired properties. $\square$

 it is hard to hope that the extension of $E_{1},\ldots,E_{s}$ to $E_{1},\ldots,E_{10}$ is unique. For example, if $s=7$, a family

$E_{1},\ldots,E_{7}$

can be extended to

$E_{1},\ldots,E_{10}$

But we can also consider the lines joining two of the last three nodes

$\hat{E_{8}}\in|L-E_{9}-E_{10}|,\hat{E_{9}}\in|L-E_{8}-E_{10}|,\hat{E}_{10}\in|L-E_{8}-E_{9}|$

and the family $E_{1},\ldots,E_{7},\hat{E_{8}},\hat{E_{9}},\hat{E}_{10}$ still works as well. For $s\geq 2$, counting how many the completions of $E_{1},\ldots,E_{s}$ are is the same as counting how many sets of $10-s$ disjoint $(-1)$-curves are contained in a Del Pezzo surface of degree $s-1$.

Here we generalize the result of Proposition 42 to possibly nodal Coble surface with irreducible boundary $\{C\}=|-2K_{X}|$.

###### Definition 43

Let $X$ be any smooth surface. A connected $(-1)$-chain in $X$ is an effective divisor $E=F_{1}+\cdots+F_{r}$, with

$F_{i}\simeq\mathbb{P}^{1}$
$F_{1}^{2}=\cdots=F_{r-1}^{2}=-2$
$F_{r}^{2}=-1$
$F_{i}F_{i+1}=1,F_{i}F_{j}=0\text{ for }|i-j|\geq 2$

If $E$ is irreducible, we simply require that $E$ is a smooth rational curve of self intersection $-1$. Given a chain $E=F_{1}+\cdots+F_{m}$, the length $l(E)$ is the number $m$ of its irreducible components.

If $E_{1},\ldots,E_{n}$ is a set of disjoint $(-1)$ chains, we set the length $l(E_{1}+\cdots+E_{n}):=l(E_{1})+\cdots+l(E_{n})$ as the number of all irreducible components.

An extension of $E_{1},\ldots,E_{n}$ is a set of disjoint $(-1)$-chains $E_{1}^{\prime},\ldots,E_{m}^{\prime}$, such that $m\geq n$ and $E_{i}^{\prime}\geq E_{i}$ for $i=1,\ldots,n$.

######

![img-0.jpeg](img-0.jpeg)
Figure 1: A $(-1)$-chain with length 4. The blue component $F_{4}$ is a $(-1)$-curve, the red components are $(-2)$-curves.

![img-1.jpeg](img-1.jpeg)
Figure 2: With the same colors as above, the set $E_1', E_2', E_3', E_4'$ is an extension of $E_1, E_2$. The extra components are dashed.

By the Castelnuovo Criterion, any set of disjoint $(-1)$-chains $E_1, \ldots, E_n$ on a surface $X$ can be contracted to a set of points $p_1, \ldots, p_n$ on a smooth surface $Y$, with

$$
K _ {Y} ^ {2} - K _ {X} ^ {2} = l \left(E _ {1}\right) + \dots + l \left(E _ {n}\right), \tag {2}
$$

see Figure 3. Also, given a smooth curve $D \subset Y$, with strict transform $\tilde{D} \subset X$, for any point $p_i$ which lies inside $D$, we can take the corresponding chain $E_i = F_1 + \dots + F_{r_i}$. There exists a unique $F_{s_i}$ touching $\tilde{D}$, for some $1 \leq s_i \leq r_i$ and these numbers satisfy

$$
\sum_ {p _ {i} \in D} s _ {i} = D ^ {2} - \tilde {D} ^ {2}, \tag {3}
$$

see Figure 3.

36

![img-2.jpeg](img-2.jpeg)
Figure 3: We can imagine to contract the  $(-1)$ -chain  $F_{1} + \dots + F_{r}$  on the point  $p$  starting from the  $(-1)$ -curve  $F_{r}$ . This turns  $F_{r-1}$  into a  $(-1)$ -curve, so it can be contracted as well, and we proceed backwards to  $F_{1}$ . Each step makes the self-intersection  $K_{X}^{2}$  jump by 1, hence we get formula 2. Meanwhile, the self-intersection  $\tilde{D}^{2}$  is affected only by  $F_{s}, F_{s-1}, \ldots, F_{1}$ , and each of these produces a jump by 1. The sum of the contributions of all  $(-1)$ -chains involved gives formula 3.

Proposition 44 Let  $X$  be a smooth Coble surface with irreducible Coble curve  $C$ . Then any set  $E_1, \ldots, E_n$  of disjoint  $(-1)$ -chains with length  $l(E_1 + \dots + E_n) \leq 8$  can be extended to a set  $E_1', \dots, E_m'$  with length 10, such that the contraction of  $E_1', \ldots, E_m'$  is  $\mathbb{P}^2$ .

Proof: The proof will be very similar to the proof of Proposition 42.

Let  $E_1', \dots, E_m' \subset X$  be an extension of  $E_1, \ldots, E_n$  of maximal length, and let  $Y$  be the surface obtained via the contraction of  $E_1', \ldots, E_m'$ , with base points  $p_1, \ldots, p_m \in Y$ . We claim that  $Y$  does not contain any  $(-1)$  curve.

On the country, assume  $E \subset Y$  to be a  $(-1)$  curve, and let  $\tilde{E} \subset X$  be its strict transform. If  $E$  does not contain any of the  $p_i$ , then  $\tilde{E}$  is still a  $(-1)$  curve, so we can build a greater set  $E_1', \ldots, E_m', E$ , which contradicts the maximality of the length. Then  $E$  must contain some of the  $p_i$ 's, so

$$
\tilde {E} ^ {2} \leq - 2
$$

By Proposition 33, the equality

$\tilde{E}^{2}=-2$

must hold. The relation (3) applied to $E,\tilde{E}$ gives

$\sum_{p_{i}\in E}s_{i}=1$

This means that $E$ contains exactly one base point, say $p_{1}\in E$ while $p_{2},\ldots,p_{m}\not\in E$, and the chain $E_{1}^{\prime}$ has the shape $E_{1}^{\prime}=F_{1}+\cdots+F_{r_{1}}$, with $\tilde{E}$ touching $F_{1}$ at exactly one point, and disjoint from the other components. Hence we can build another extension, namely $\tilde{E}+E_{1}^{\prime},E_{2}^{\prime},\ldots,E_{m}^{\prime}$, which again is impossible by maximality.
Thus $Y$ does not contain any $(-1)$-curve, so it is a smooth minimal rational surface, that is

$Y=\mathbb{P}^{2}$

or

$Y=\mathbb{F}_{m}$

for some $m\neq 1$. We want to examine all the possibilities.
First of all, remember that $\mathbb{F}_{m}$ contains a curve of self intersection $-m$. Hence, if $m\geq 3$, then $X$ contains a curve of self intersection smaller or equal than $-3$, which is forbidden by Proposition 33.
So we are left with 3 cases: $Y=\mathbb{P}^{2},\mathbb{P}^{1}\times\mathbb{P}^{1}$ or $\mathbb{F}_{2}$. By (2), we can now compute the length

$l(E_{1}^{\prime}+\cdots+E_{m}^{\prime})=K_{Y}^{2}-K_{X}^{2}=K_{Y}^{2}+1$

which gives

$l(E_{1}^{\prime}+\cdots+E_{m}^{\prime})=10\ \ \text{if}\ \ Y=\mathbb{P}^{2}$

and

$l(E_{1}^{\prime}+\cdots+E_{m}^{\prime})=9\ \ \text{if}\ \ Y=\mathbb{P}^{1}\times\mathbb{P}^{1}\ \ \text{or}\ \ \mathbb{F}_{2}$

If $Y=\mathbb{P}^{2}$ the proof is complete.
If $Y=\mathbb{P}^{1}\times\mathbb{P}^{1}$ we act as in the proof of Proposition 42, blowing up a base point, and blowing down the strict transforms of the fibers passing through it, and we get a family of $(-1)$-chains of strictly higher length, which is absurd. Finally, if $Y=\mathbb{F}_{2}$, none of the points $p_{1},\ldots,p_{m}$ can lie on the $(-2)$-section $C_{-2}\subset\mathbb{F}_{2}$, otherwise the strict transform $\tilde{C}_{-2}\subset X$ would have

$\tilde{C}_{-2}\leq-3$

which is impossible.
By definition, the original set $E_{1},\ldots,E_{n}$ satisfies $n\leq m$ and $E_{i}\leq E_{i}^{\prime}$ for $i=1,\ldots,n$. By hypothesis, $l(E_{1})+\cdots+l(E_{n})\leq 8$, while $l(E_{1}^{\prime})+\cdots+l(E_{m}^{\prime})=9$. So we can write the last extended $(-1)$-chain $E_{m}^{\prime}$ as

$E_{m}^{\prime}=F_{1}+\cdots+F_{r^{\prime}}$

with $F_{1}$ not appearing in the original $E_{1},\ldots,E_{n}$. Consider the corresponding base point $p_{m}\in Y$, and let $F$ be the fiber in $\mathbb{F}_{2}$ passing through $p_{m}$. Let $\tilde{F}\subset X$ be its strict transform. Proposition 33 gives

$\tilde{F}^{2}\in\{-1,-2\}$

If $\tilde{F}^{2}=-1$, relation 3 states that $p_{m}$ is the only base point lying in $F$, and $\tilde{F}$ touches the first component $F_{1}$. So we can substitute the $(-1)$-chain $E_{m}^{\prime}$ of length $r^{\prime}$ with two disjoint $(-1)$-chains, namely $(E_{m}^{\prime}-F_{1})$ and $\tilde{C}_{-2}+\tilde{F}$, with length $r^{\prime}+1$. This is impossible by maximality.
Similarly, if $\tilde{F}^{2}=-2$ we have

$\sum_{p_{i}\in F}s_{i}=2$

which means that $F$ can contain at most two base points. If $F$ contains only $p_{m}$ as base point, then $\tilde{F}$ touches $F_{2}$ at one point, so we can throw away $F_{1}$ to build a longer chain $\tilde{C}_{-2}+\tilde{F}+(E_{m}^{\prime}-F_{1})$, which is a connected $(-1)$-chain of length $r+1$. Again, this is forbidden by maximality.
If another base point, say $p_{m-1}$, lies inside $F$ together with $p_{m}$, we need to write down its corresponding $(-1)$-chain. So

$E_{m-1}^{\prime}=F_{1}^{(m-1)}+\cdots+F_{s}^{(m-1)}$

where $F_{s}^{(m-1)}$ is a $(-1)$-curve, while the other components have self-intersection $-2$. Moreover, $\tilde{F}$ touches at one point both $F_{1}$ and $F_{1}^{(m-1)}$, which gives the possibility to build two disjoint chains, that are $\tilde{C}_{-2}+\tilde{F}+E_{m-1}^{\prime}$ and $E_{m}^{\prime}-F_{1}$. Since their complexive length is $r+s+1$, this contradicts the maximality of $E_{1}^{\prime},\ldots,E_{m}^{\prime}$.
This exhausts all the possibilities, so the proof is complete. $\square$

Exceptional curves inside Coble surfaces are closely related to elliptic curves. Indeed we first claim that a Coble surface $X$ with irreducible Coble curve $C$ satisfies:

$h^{1}(\mathcal{O}_{X}(-K_{X}))=0.$ (4)

This comes from the application of the Riemann - Roch Theorem to the divisor $-K_{X}$, so that:

$h^{0}(\mathcal{O}_{X}(-K_{X}))-h^{1}(\mathcal{O}_{X}(-K_{X}))+h^{2}(\mathcal{O}_{X}(-K_{X}))=1+\frac{(-K_{X})(-2K_{X})}{2}=1+K_{X}^{2}=0.$

But $h^{0}(\mathcal{O}_{X}(-K_{X}))=0$ by Definition 29, and $h^{2}(\mathcal{O}_{X}(-K_{X}))=h^{0}(\mathcal{O}_{X}(2K_{X}))=0$, because of Serre’s duality and the rationality of $X$. This proves equality (4).
Now for any $(-1)$-curve $E\subset X$ inside a Coble surface $X$ with irreducible Coble curve $C$, we have a short exact sequence:

$0\to\mathcal{O}_{X}(-K_{X})\to\mathcal{O}_{X}(E-K_{X})\to\mathcal{O}_{E}(E-K_{X})\to 0$

Together with the relations (4) and

$\mathcal{O}_{E}(E-K_{X})=\mathcal{O}_{\mathbb{P}^{1}}(E(E-K_{X}))=\mathcal{O}_{\mathbb{P}^{1}},$

this induces an isomorphism

$H^{0}(\mathcal{O}_{X}(E-K_{X}))\simeq\mathbb{C}.$

Hence the divisor $\mathcal{E}:=E-K_{X}$ is effective and rigid, that is, it cannot move. The adjunction formula immediately proves that $\mathcal{E}$ is an elliptic curve. The following proposition shows also that also the converse is true:

###### Proposition 45

Let $\mathcal{E}$ be an elliptic curve on a Coble surface $X$, with $C\in|-2K_{X}|$ irreducible anti - bicanonical divisor. If $\mathcal{E}$ is rigid, then the divisor $2\mathcal{E}$ moves in a basepoint - free pencil of elliptic curves.
Conversely, every base point-free pencil of elliptic curves $\mathcal{E}^{\prime}$ has the form $\mathcal{E}^{\prime}=2\mathcal{E}$, with $\mathcal{E}$ an isolated elliptic curve.

Proof: We start from the short exact sequence

$0\to\mathcal{O}_{X}\to\mathcal{O}_{X}(\mathcal{E})\to\mathcal{O}_{\mathcal{E}}(\mathcal{E})\to 0$ (5)

which remains exact on global sections:

$0\to H^{0}(\mathcal{O}_{X})\to H^{0}(\mathcal{O}_{X}(\mathcal{E}))\to H^{0}(\mathcal{O}_{\mathcal{E}}(\mathcal{E}))\to 0.$

Since $\mathcal{E}$ is rigid, we deduce

$H^{0}(\mathcal{O}_{\mathcal{E}}(\mathcal{E}))=0.$

The adjunction formula gives

$\mathcal{O}_{\mathcal{E}}(\mathcal{E}+K_{X})=\mathcal{O}_{\mathcal{E}}$

$\mathcal{O}_{\mathcal{E}}(\mathcal{E})=\mathcal{O}_{\mathcal{E}}(-K_{X}).$

In particular,

$\deg\mathcal{O}_{\mathcal{E}}(\mathcal{E})=\frac{1}{2}\mathcal{E}\mathrm{C}\geq 0.$

If the inequality was sharp, then Riemann-Roch Theorem would imply $h^{0}(\mathcal{O}_{\mathcal{E}}(\mathcal{E}))>0$ which is false, hence

$\deg\mathcal{O}_{\mathcal{E}}(\mathcal{E})=0$

Consequently,

$\mathcal{O}_{\mathcal{E}}(2\mathcal{E})=\mathcal{O}_{\mathcal{E}}(-2K_{X})=\mathcal{O}_{\mathcal{E}}(C)$

is an effective line bundle of degree $0$, thus $\mathcal{O}_{\mathcal{E}}(2\mathcal{E})=\mathcal{O}_{\mathcal{E}}$. In other words, $\mathcal{O}_{\mathcal{E}}(\mathcal{E})$ is a $2$-torsion divisor, and by Serre duality:

$h^{1}(\mathcal{O}_{\mathcal{E}}(\mathcal{E}))=h^{0}(\mathcal{O}_{\mathcal{E}}(\mathcal{E}))=0$

The long exact sequence induced by (5) now implies that

$h^{1}(\mathcal{O}_{X}(\mathcal{E}))=0.$

Finally we look at the sequence

$0\to\mathcal{O}_{X}(\mathcal{E})\to\mathcal{O}_{X}(2\mathcal{E})\to\mathcal{O}_{\mathcal{E}}(2\mathcal{E})=\mathcal{O}_{\mathcal{E}}\to 0,$

which gives

$h^{0}(\mathcal{O}_{X}(2\mathcal{E}))=2.$

It is easy to show that the pencil $|2\mathcal{E}|$ has no base points or base components: indeed, a base component of $2\mathcal{E}$ can only be $\mathcal{E}$ itself. But if $\mathcal{E}$ was a base component, then we would have $h^{0}(\mathcal{O}_{X}(2\mathcal{E}-\mathcal{E}))=h^{0}(\mathcal{O}_{X}(2\mathcal{E}))=2$, which is a contradiction with the rigidity of $\mathcal{E}$. Finally, if the pencil $|2\mathcal{E}|$ had a base point, this should lie on the reduced curve $\mathcal{E}$. Since $|2\mathcal{E}|$ has no base components, the intersection product $\mathcal{E}(2\mathcal{E})=2\deg\mathcal{O}_{\mathcal{E}}(\mathcal{E})=0$ shows that the generic element of $|2\mathcal{E}|$ does not touch $\mathcal{E}$, and hence this pencil has no base points.
Conversely, assume $\mathcal{E}^{\prime}$ is a base point free pencil of elliptic curves: necessarily we have

$\mathcal{O}_{\mathcal{E}^{\prime}}(\mathcal{E}^{\prime})=\mathcal{O}_{\mathcal{E}^{\prime}}$

and by adjunction formula also

$\mathcal{O}_{\mathcal{E}^{\prime}}(K_{X})=\mathcal{O}_{\mathcal{E}^{\prime}}$

Consider the divisor

$D:=\mathcal{E}^{\prime}+K_{X}.$

We first show that it is effective. With this purpose, we consider the sequence

$0\to\mathcal{O}_{X}(K_{X})\to\mathcal{O}_{X}(\mathcal{E}^{\prime}+K_{X})\to\mathcal{O}_{\mathcal{E}^{\prime}}(\mathcal{E}^{\prime}+K_{X})\to 0$

which induces an isomorphism

$H^{0}(\mathcal{O}_{X}(\mathcal{E}^{\prime}+K_{X}))\simeq H^{0}(\mathcal{O}_{\mathcal{E}^{\prime}}(\mathcal{E}^{\prime}+K_{X}))=H^{0}(\mathcal{O}_{\mathcal{E}^{\prime}})\simeq\mathbb{C}.$

Hence $D$ is effective, and the relation

$\mathcal{E}^{\prime}D=\mathcal{E}^{\prime}(\mathcal{E}^{\prime}+K_{X})=0$

yields that every component of $D$ is contained in a fiber of $\mathcal{E}^{\prime}$. Nonetheless, we also have

$H^{0}(\mathcal{O}_{X}(\mathcal{E}^{\prime}-D))=H^{0}(\mathcal{O}_{X}(-K_{X}))=0$

so one fiber of $|\mathcal{E}^{\prime}|$ is not sufficient to contain all of $D$. On the other side,

$H^{0}(\mathcal{O}_{X}(2\mathcal{E}^{\prime}-D))=H^{0}(\mathcal{O}_{X}(\mathcal{E}^{\prime}-K_{X}))$ (6)

This quantity can be computed via the short exact sequence

$0\to\mathcal{O}_{X}(-K_{X})\to\mathcal{O}_{X}(\mathcal{E}^{\prime}-K_{X})\to\mathcal{O}_{\mathcal{E}^{\prime}}(\mathcal{E}^{\prime}-K_{X})\to 0$

which induces an isomorphism

$H^{0}(\mathcal{O}_{X}(\mathcal{E}^{\prime}-K_{X}))\simeq H^{0}(\mathcal{O}_{\mathcal{E}^{\prime}}(\mathcal{E}^{\prime}-K_{X}))=H^{0}(\mathcal{O}_{\mathcal{E}^{\prime}})=\mathbb{C}$ (7)

Of course, the vanishing (4) was used to derive this isomorphism. Putting together the relations (6) and (7) we find that two fibers of $\mathcal{E}^{\prime}$ are sufficient to contain all of $D$, so we have a disjoint decomposition

$D=E+\mathcal{E}$

Moreover, the product

$DC=(\mathcal{E}^{\prime}+K_{X})(-2K_{X})=2$

forces, up to the order,

$EC=2\,\text{ and }\,\mathcal{E}C=0$

Let $p_{a}(E)$ denote the algebraic genus of $E$. Since $C$ and $E$ touch each other, they belong to the same fiber of $\mathcal{E}^{\prime}$, so that $C+E\leq\mathcal{E}^{\prime}$. This forces

$p_{a}(C+E)\leq 1$, but we also know that $p_{a}(C+E)=p_{a}(C)+p_{a}(E)+1=p_{a}(E)+1$. The only possibility is that

$p_{a}(E)=0$

and by adjunction formula

$E^{2}=2p_{a}(E)-2-EK_{X}=-2+\frac{EC}{2}=-1,$

so that $E$ is a smooth $(-1)$-curve. Now we compute the intersection product between $E$ and the effective divisor $\mathcal{E}^{\prime}-C-E$, and we find

$(\mathcal{E}^{\prime}-C-E)E=-1$

Hence $E$ is necessarily a component of $\mathcal{E}^{\prime}-C-E$. So we showed that

$C+2E\leq\mathcal{E}^{\prime}$

and since both these two divisors generate base point-free pencils, we have

$C+2E=\mathcal{E}^{\prime}$

and thus

$\mathcal{E}^{\prime}-2\mathcal{E}=\mathcal{E}^{\prime}-2(\mathcal{E}^{\prime}+K_{X}-E)=-\mathcal{E}^{\prime}+C+2E=0$

that is

$\mathcal{E}^{\prime}=2\mathcal{E}\ \ \square$

The previous Proposition is a glimpse on a very large theory, about Halphen pencils. By definition, a Halphen pencil of index $m$ is a rational surface $Y$ such that the divisor $|-mK_{Y}|$ defines a relatively minimal and basepoint - free pencil of curves, with exactly one multiple fiber, of multiplicity $m$. The blow - down of the curve $E$ in Proposition 45 defines a Halphen pencil of index $2$, with $2\mathcal{E}$ as the unique double fiber. For a wider overview on Halphen pencils, see *[25]*, *[35]*.
Note also that Proposition (45) also showed that $\mathcal{E}+K_{X}$ is the class of a $(-1)$-curve in $X$, for any isolated elliptic curve $\mathcal{E}$. We also remark that if we start with two isolated elliptic curves $\mathcal{E}_{1}=E_{1}-K_{X},\mathcal{E}_{2}=E_{2}-K_{X}$, then $\mathcal{E}_{1}\mathcal{E}_{2}=E_{1}E_{2}+1$. Combining this fact with the results from Propositions 42 and 45, we finally get to the main result of this subsection:

###### Theorem 46

Let $X$ be an unnodal Coble surface, with irreducible boundary curve $C$. Then any sequence $\mathcal{E}_{1},\ldots,\mathcal{E}_{r}$ of isolated elliptic curves satisfying $\mathcal{E}_{i}\mathcal{E}_{j}=1-\delta_{i,j}$ and $r\leq 8$ can be extended to a sequence $\mathcal{E}_{1},\ldots,\mathcal{E}_{10}$ with the same property.

In the classical literature of Enriques surfaces, a sequence $\mathcal{E}_{1},\ldots,\mathcal{E}_{r}$ of isolated elliptic curves with intersection products $\mathcal{E}_{i}\mathcal{E}_{j}=1-\delta_{i,j}$ is known as an isotropic sequence. Cossec proved in *[8]* that Theorem 46 is true also on unnodal Enriques surfaces. For the study of this problem on Enriques surfaces, including nodal ones, we refer to *[4]*, *[21]*, *[26]*.

##

2.3 Moduli space of Coble surfaces

Nowadays, Coble surfaces are studied also for other reasons: the two conditions of Definition 29 imply that for every Coble surface $X$ there exists a map $\pi:\tilde{X}\to X$, where $\tilde{X}$ is a smooth $K3$ surface and $\pi$ is a double cover, ramified over the Coble curve. As a consequence, Coble surfaces are closely related to Enriques surfaces, which are quotients of $K3$ surfaces by a fixed point - free involution. More precisely, we refer to *[13]*, where the authors proved the following result:

###### Theorem 47

*[13]* The coarse moduli space of nodal Enriques surfaces $\mathcal{M}_{En,nod}$ and of Coble surfaces $\mathcal{M}_{Co}$ are both rational varieties of dimension $9$.

Our goal is to give an idea about why it is reasonable that $\mathcal{M}_{Co}$ has dimension $9$: a rational sextic curve $\overline{C}\subset\mathbb{P}^{2}$ is the image of a regular map $\gamma$:

$\gamma:\mathbb{P}^{1}\to\mathbb{P}^{2}$
$\gamma(u,v)=[F_{0}(u,v),F_{1}(u,v),F_{2}(u,v)]$ (8)

where the $F_{i}$’s are three linearly independent homogeneous polynomials of degree $6$ over $\mathbb{P}^{1}$, without common zeroes. These three forms span a subspace $V\subset H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))$. Clearly, another base of $V$ made by $G_{0},G_{1},G_{2}$ defines a different map

$\gamma^{\prime}:\mathbb{P}^{1}\to\mathbb{P}^{2}$
$\gamma^{\prime}(u,v)=[G_{0}(u,v),G_{1}(u,v),G_{2}(u,v)]$

with image a curve $C^{\prime}$. Of course there is an element $M\in\mathbb{P}GL(2)$ which moves $C$ onto $C^{\prime}$, which lifts to an isomorphism of the corresponding Coble surfaces. Thus the isomorphism class of a Coble surface $X$ depends only on the choice of an element $V\in\mathrm{Gr}(3,\mathrm{H}^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6)))$.

Viceversa, “almost every” subspace $V\subset H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))$ of dimension $3$ is good to build a Coble surface.

Indeed, if $V$ is basepoint-free one can define the regular map

$\gamma_{|V|}:\mathbb{P}^{1}\to\mathbb{P}(V^{*})\simeq\mathbb{P}^{2}$
$\gamma(p):=\{\sigma\in V\,\mathrm{such}\,\mathrm{that}\,\sigma(p)=0\}$

When we look at the projective coordinates, the map $\gamma_{|V|}$ has exactly the shape $8$. We can give a geometric interpretation of this map as the composite

$\mathbb{P}^{1}\to\mathbb{P}(H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))^{*})\dashrightarrow\mathbb{P}(V^{*})$ (9)

where

The first map in (9) is the standard Veronese embedding

$\mathbb{P}^{1}\to\mathbb{P}(H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))^{*})\simeq\mathbb{P}^{6}$
$p\to\{\sigma\in H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))\operatorname{such}\operatorname{that}\sigma(p)=0\}$

The rational function on the right side of (9) is induced by the linear map $H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))^{*}\to V^{*}$, dual to the inclusion $V\subset H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))$, and consists precisely to the projection with center the projectified annihilator $\mathbb{P}(\operatorname{Ann}\left(\mathrm{V}\right))\subset\mathbb{P}(\mathrm{H}^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))^{*})$. Thus the image of

$C_{V}:=\gamma_{|V|}(\mathbb{P}^{1})$

will be the projection of a rational normal curve from some subspace.

Since

$\gamma_{|V|}^{*}\mathcal{O}_{\mathbb{P}^{2}}(1)=\mathcal{O}_{\mathbb{P}^{1}}(6)$

one finds

$(\deg\gamma_{|\mathrm{V}|})(\deg\mathrm{C}_{|\mathrm{V}|})=6$

Then the space of semi - stable nets, in the sense of *[27]*

$U:=\{V\in\operatorname{Gr}(3,\mathrm{H}^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6)))\operatorname{such}\operatorname{that}\operatorname{Bs}|\mathrm{V}|=\emptyset$
$\text{ and }\operatorname{Im}\left(\gamma_{|V|}\right)\operatorname{is}\operatorname{a}10-\operatorname{nodal}\operatorname{sextic}\}$

is an open subset of the Grassmannian $\operatorname{Gr}(3,\mathrm{H}^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6)))\simeq\operatorname{Gr}(3,7)$. In the complementary closed subset, there are subspaces $V$ such that $\gamma_{|V|}$ is a double cover of a nodal cubic curve, or a triple cover of a smooth conic, or the image has worse singularities.

Moreover, we have to take in account the reparametrizations of $\mathbb{P}^{1}$, that are elements of $\mathbb{P}GL(2,\mathbb{C})$. Thus, the GIT-quotient

$\mathcal{M}_{Co}:=U//PGL(2,\mathbb{C})$

constructed again as in *[27]*, is a suitable moduli space for rational plane sextics. 

$\dim\mathrm{U}=\dim\operatorname{Gr}(3,\mathrm{H}^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6)))=12,$

so that

$\dim\mathcal{M}_{\mathrm{Co}}=9.$

3 Projective models of Coble surfaces

### 3.1 The Bordiga model

There is another model for Coble surfaces, which also underlines their parenthood with Enriques surfaces: the Bordiga model. This subsection is inspired by the construction of a Reye - Enriques model in *[33]*.
One looks at the family of quadrics in $\mathbb{P}^{3}$, that is, the family

$\mathbb{P}^{9}\simeq\mathbb{P}(H^{0}(\mathbb{P}^{3},\mathcal{O}(2)))$

We identify each quadric polynomial $Q\in H^{0}(\mathbb{P}^{3},\mathcal{O}(2))$ with a symmetric matrix $M$. Thus $\mathbb{P}^{9}$ can be stratified by the rank of matrices: for $k=1,\ldots,4$, let us denote by

$\mathcal{Q}_{k}:=\{M\operatorname{such}\operatorname{that}rk\,M\leq k\}$

the family of quadrics of rank less or equal than $k$.
We have a chain of closed inclusions

$\mathcal{Q}_{1}\subset\mathcal{Q}_{2}\subset\mathcal{Q}_{3}\subset\mathcal{Q}_{4}=\mathbb{P}^{9}$

The generic element of every $\mathcal{Q}_{k}$, more precisely the ones in $\mathcal{Q}_{k}\setminus\mathcal{Q}_{k-1}$, has rank exactly $k$. In particular, the space $\mathcal{Q}_{3}$ is defined by the annihilation of the determinant, which is a section of $H^{0}(\mathbb{P}^{9},\mathcal{O}(4))$. Hence $\mathcal{Q}_{3}$ is an 8-dimensional hypersurface of degree 4 in $\mathbb{P}^{9}$.
The inner space $\mathcal{Q}_{2}$ consists of quadrics which are made up of two hyperplanes, counted with multiplicities. Hence we have a parametrization

$\pi:(\mathbb{P}^{3})^{*}\times(\mathbb{P}^{3})^{*}\to\mathcal{Q}_{2}\subset\mathbb{P}^{9}$
$\pi([F],[G]):=[FG]$

The map $\pi$ is a double cover over its image, which is exactly $\mathcal{Q}_{2}$. Thus $\mathcal{Q}_{2}$ is a variety of dimension 6, of degree equal to

$\deg\mathcal{Q}_{2}=\frac{1}{2}\pi^{*}\mathrm{H}^{6}=10$

where $H$ is an hyperplane section of $\mathbb{P}^{9}$. The space $\mathcal{Q}_{1}$ is the branch locus of $\pi$, while the diagonal in $(\mathbb{P}^{3})^{*}\times(\mathbb{P}^{3})^{*}$ is the ramification locus.
This locus is a threefold of degree 8 in $\mathbb{P}^{9}$, and it corresponds to the Veronese embedding of $(\mathbb{P}^{3})^{*}$ through quadric forms, and it is the singular locus of the six-fold $\mathcal{Q}_{2}$.
To get a Coble surface, we choose a 5-dimensional linear subspace $\Lambda\subset\mathbb{P}^{9}$,

$\Lambda=V(L_{1},L_{2},L_{3},L_{4})\simeq\mathbb{P}^{5}$

where the $L_{i}$’s are linear forms on $\mathbb{P}^{9}$. We consider the intersection surface

$S:=\Lambda\cap\mathcal{Q}_{2}$

and its pre-image

$\tilde{S}:=\pi^{-1}(S)=\pi^{-1}(\Lambda).$

The surface $\tilde{S}\subset(\mathbb{P}^{3})^{*}\times(\mathbb{P}^{3})^{*}$ is defined by the system of bilinear symmetric equations

$\tilde{S}=\{([F],[G])\text{ such that }L_{i}(FG)=0\text{ for }i=1,2,3,4\}$ (10)

If $\Lambda$ is general enough, we have $\Lambda\cap\mathcal{Q}_{1}=\emptyset$. In this case, the system (10) has no solutions along the diagonal $\Delta$ of $(\mathbb{P}^{3})^{*}\times(\mathbb{P}^{3})^{*}$, both $\tilde{S}$ and $S$ are smooth, and the 2:1 cover $\pi:\tilde{S}\to S$ is unramified. The automorphism group of this cover is $\mathbb{Z}_{2}$, generated by the involution $i$ of $(\mathbb{P}^{3})^{*}\times(\mathbb{P}^{3})^{*}$ which switches the factors. In $(\mathbb{P}^{3})^{*}\times(\mathbb{P}^{3})^{*}$, the surface $\tilde{S}$ is defined by the four bilinear equations of (10), which are four sections of $\mathcal{O}(1,1)$. Hence, the canonical bundle of $\tilde{S}$ is

$K_{\tilde{S}}=(4\,\mathcal{O}(1,1)+K_{(\mathbb{P}^{3})^{*}\times(\mathbb{P}^{3})^{*}})|_{\tilde{S}}=\mathcal{O}_{\tilde{S}}$

Together with the fact that $\tilde{S}$ is simply connected, this says that $\tilde{S}$ is a $K3$ surface, and $S=\pi(\tilde{S})=\tilde{S}/i$ is an Enriques surface.

Now, suppose we are in the pathological case when $\Lambda\cap\mathcal{Q}_{1}\neq\emptyset$. In this case, the surfaces $S$ inherits the singularities coming from $\mathcal{Q}_{1}$, and so $S$ becomes a singular surface, with a quartic point $p\in S\cap\mathcal{Q}_{1}$. Now let us choose a hyperplane

$H\subset\Lambda$
$H\simeq\mathbb{P}^{4}$

such that $p\notin H$, and consider the projection with center $p$,

$\pi_{p}:S\setminus\{p\}\subset\Lambda\setminus\{p\}\to H$

We denote by

$\tilde{\pi}_{p}:=\mathrm{Bl}_{p}S\to H$

the resolution of the indeterminacy of $\pi$ at $p$.

###### Definition 48

The image surface $X:=\operatorname{Im}\pi_{p}\subset\mathbb{P}^{4}$ is called Bordiga surface.

###### Proposition 49

The linear system $|H+K_{X}|$ has projective dimension $2$, and it contracts $10$ smooth rational $(-1)$-curves. Thus, the Bordiga surface $X\subset\mathbb{P}^{4}$ is isomorphic to the blow-up of $\mathbb{P}^{2}$ in 10 base-points.
If $E\subset Bl_{p}S$ is the exceptional curve over the singular point $p$, then its image

$C:=\tilde{\pi}(E)\subset X$

is the proper transform of a sextic curve $C\subset\mathbb{P}^{2}$, having multiplicity $2$ at all the $10$ base points. As a consequence, the class $C\in\operatorname{Pic}(X)$ is given by

$[\hat{C}]=6L-2E_{1}-\cdots-2E_{10}=-2K_{X}$

Conversely, if we start with a Coble surface $X^{\prime}=Bl_{10}\mathbb{P}^{2}$, then the linear system

$|H|:=|4L-E_{1}-\cdots-E_{10}|$

of quartics passing through all the base points determines an embedding

$X^{\prime}\to\mathbb{P}^{4}$

whose image is a Bordiga surface.

### 3.2 Quintic Coble surfaces

Another way to see a Coble surface is using the linear system

$H:=|6L-2E_{1}-\cdots-2E_{7}-E_{8}-E_{9}-E_{10}|$

We have

$h^{0}(X,H)=4$

and

$H^{2}=5$

so that the pair $(X,H)$ determines a birational map $\phi:X\to\mathbb{P}^{3}$ onto a quintic hypersurface $\overline{X}$. For each permutation $(i,j,k)$ of the indices $(8,9,10)$, the exceptional divisor $E_{i}$ is sent biregularly onto a line $l_{i}$, because

$HE_{i}=1.$

Moreover the cubic curve through $p_{1},\ldots,p_{7},p_{i},p_{j}$ lives in the linear system $-K_{X}+E_{k}$, and covers with degree $2$ a line $\hat{l}_{k}\subset X^{\prime}$, because

$H(-K_{X}+E_{k})=2$

$\hat{l}_{k}$ meets both $l_{i},l_{j}$ at the same point. The three lines $\hat{l}_{8},\hat{l}_{9},\hat{l}_{10}$ are double lines for $\overline{X}$, and they are concurrent at a point. Indeed, the decomposition

$H=-2K_{X}+E_{8}+E_{9}+E_{10}=(-K_{X}+E_{i})+(-K_{K}+E_{j})+E_{k}$

implies that $\hat{l}_{i},\hat{l}_{j},l_{k}$ are coplanar for every $i,j$. Hence $\overline{X}$ contains a tetrahedron $T\subset\mathbb{P}^{3}$ consisting of 6 lines, and passes doubly through three of them. The three double lines share a common vertex of $T$, which is a triple point for $\overline{X}$. In a suitable choice of coordinates, the equation of such a quintic $\overline{X}$ is:

$\alpha X_{0}X_{2}^{2}X_{3}^{2}+\beta X_{0}X_{1}^{2}X_{3}^{2}+\gamma X_{0}X_{1}^{2}X_{2}^{2}+X_{1}X_{2}X_{3}q=0$ (11)

with $\alpha,\beta,\gamma\in\mathbb{C}$, and $q=q(X_{0},X_{1},X_{2},X_{3})$ is a quadratic form on $\mathbb{P}^{3}$.
We write $L_{i,j}$ to denote the line $X_{i}=X_{j}=0$. The three lines $l_{0,1},l_{0,2},l_{0,3}$ are double lines, and they meet at the triple point $[1,0,0,0]$. The plane $X_{0}=0$ cuts the three simple edges $l_{1,2},l_{2,3},l_{1,3}$, plus the plane quadric defined by $q=0,X_{0}=0$, which is the image of $C$.
Now we want to prove the opposite, that is, the normalization of a generic quintic surface $\overline{X}$ defined as in (11) is actually a Coble surface.
First we can assume

$\alpha,\beta,\gamma\neq 0$

and hence we can perform the diagonal change of variables

$X_{1}$ $=\sqrt{\alpha}X_{1}^{\prime}$
$X_{2}$ $=\sqrt{\beta}X_{2}^{\prime}$
$X_{3}$ $=\sqrt{\gamma}X_{3}^{\prime}$

which turns Equation (11) in

$X_{0}X_{2}^{2}X_{3}^{2}+X_{0}X_{1}^{2}X_{3}^{2}+X_{0}X_{1}^{2}X_{2}^{2}+X_{1}X_{2}X_{3}q=0$ (12)

Now let $\nu:X\to\overline{X}$ be its normalization, and assume $X$ is smooth.

###### Definition 50

Let $\overline{X}$ be a quintic surface inside $\mathbb{P}^{3}$ defined as in (12). We denote by $L_{i,j}$ the line

$L_{i,j}:=\{X_{i}=X_{j}=0\}$

and by $E_{i,j}$ the corresponding divisorial pre-image in $X$.
Moreover, let $\overline{C}\subset\overline{X}$ the plane conic defined by

$\overline{C}:=\{X_{0}=0,q(0,X_{1},X_{2},X_{3})=0\}$

and let $C$ be its pre-image in $X$.

, if $X$ is generic, then the unique singular points of $\overline{X}$ in $L_{0,1},L_{0,2},$ $L_{0,3}$ are the three vertices $[0,1,0,0],[0,0,1,0],[0,0,0,1]$. Consequently, also $E_{0,1},E_{0,2},E_{0,3}$ are still smooth rational curves. For the same reason, also $C$ is a smooth rational curve in $X$.
On the converse, a local computation, in complete analogy with the case of Enriques surfaces, shows that the three lines $L_{1,2},L_{1,3},L_{2,3}$ consist of double points of $\overline{X}$, and each of them contains 4 pinch points. Hence, the three curves $E_{1,2},E_{1,3},E_{2,3}$ are smooth genus 1 curves.

###### Proposition 51

The divisor $4L_{1,2}+4L_{1,3}+4L_{2,3}-\overline{C}$ lies in the linear system $\mathcal{O}_{\overline{X}}(2)$, so it is a Cartier divisor. Its pull-back on $X$ equals $\nu^{*}(4L_{1,2}+4L_{1,3}+4L_{2,3}-\overline{C})=2E_{1,2}+2E_{1,3}+2E_{2,3}-C$

Proof: Let

$H_{i}\subset\mathbb{P}^{3}$

be the coordinate hyperplanes defined by

$H_{i}=\{X_{i}=0\}$

for $i=0,1,2,3$. The $H_{i}$’s are Cartier divisor on $\mathbb{P}^{3}$, and so are their restrictions on $\overline{X}$. But clearly

$(H_{0})|_{\overline{X}}=L_{0,1}+L_{0,2}+L_{0,3}+\overline{C}$
$(H_{1})|_{\overline{X}}=L_{0,1}+2L_{1,2}+2L_{1,3}$
$(H_{2})|_{\overline{X}}=L_{0,2}+2L_{1,2}+2L_{2,3}$
$(H_{3})|_{\overline{X}}=L_{0,3}+2L_{1,3}+2L_{2,3}$

Let $D$ be the following divisor on $\overline{X}$:

$D:=4L_{1,2}+4L_{1,3}+4L_{2,3}-\overline{C},$

so that we have

$D=(H_{1}+H_{2}+H_{3}-H_{0})|_{\overline{X}}$

and the right-hand term lives in $|\mathcal{O}_{\overline{X}}(2)|$. The pull-back $\nu^{*}D$ clearly takes the form $\nu^{*}D=m(E_{1,2}+E_{1,3}+E_{2,3})-C$ for some $m>0$. The equality $m=2$ follows since $\nu_{*}E_{i,j}=2L_{i,j}$. $\square$

###### Corollary 52

The surface $X$ satisfies $h^{0}(\mathcal{O}_{X}(K_{X}))=h^{0}(\mathcal{O}_{X}(2K_{X}))=h^{0}(\mathcal{O}_{X}(-K_{X}))=0$, and $C\in|-2K_{X}|$.

##

Proof: We apply the formula

$K_{X}=\nu^{*}K_{\overline{X}}-(E_{1,2}+E_{1,3}+E_{2,3})$

By the adjunction formula

$K_{\overline{X}}=\mathcal{O}_{\overline{X}}(1),$

so by Proposition 3.2

$\mathcal{O}_{X}(2K_{X})=\nu^{*}\mathcal{O}_{\overline{X}}(2)-2(E_{1,2}+E_{1,3}+E_{2,3})=\mathcal{O}_{X}(-C).$

This immediately proves that $2K_{X}$ (and so $K_{X}$) is noneffective, while $-2K_{X}$ is.
It only remains to show that $h^{0}(-K_{X})=0$, but by Serre duality we know that

$h^{0}(\mathcal{O}_{X}(-K_{X}))=h^{2}(\mathcal{O}_{X}(2K_{X}))=h^{2}(\mathcal{O}_{X}(-C)).$

The short exact sequence

$0\to\mathcal{O}_{X}(-C)\to\mathcal{O}_{X}\to\mathcal{O}_{C}\to 0$

gives a long exact sequence

$0\to H^{2}(\mathcal{O}_{X}(-C))\to H^{2}(\mathcal{O}_{X}).$

Using again Serre duality and the first part of this statement,

$h^{2}(\mathcal{O}_{X})=h^{0}(\mathcal{O}_{X}(K_{X}))=0.$

$\square$
The next step is to compute some intersection products in $X$.

###### Proposition 53

The intersection products are $C^{2}=-4,E_{0,i}E_{0,j}=-\delta_{i,j},CE_{0,i}=2$. In particular, the Picard rank $rk$Pic(X) and the second Betti number $b_{2}(X)$ are greater than or equal to $4$.

Proof: The curves $\overline{C},L_{0,i}$ are smooth rational curves in $\overline{X}$, and so are their pull-backs $C,E_{0,i}$ in $X$. In particular,

$C^{2}+CK_{X}=-2$

and by Corollary 52 we find

$C^{2}+CK_{X}=\frac{1}{2}C^{2}$

which gives

$C^{2}=-4.$

The line $L_{0,i}$ meets the conic $\overline{C}$ at two smooth points of $\overline{X}$, so $CE_{0,i}=2$. Again, the adjunction formula and Corollary 52 give

$E_{0,i}^{2}=-1.$

Finally, if $\overline{X}$ is generic enough, none of the intersection points $L_{0,i}\cap L_{0,j}$ is a pinch point. Indeed, look for example at

$L_{0,1}\cap L_{0,2}=[0,0,0,1],$

which lies on the double line $L_{1,2}=\{X_{1}=X_{2}=0\}$. We consider the equation 12, putting in evidence the terms of minimal degree in the variables $X_{1},X_{2}$. Such terms are:

$(X_{0}X_{3}^{2})X_{1}^{2}+(X_{0}X_{3}^{2})X_{2}^{2}+(X_{3}\hat{q}(X_{0},X_{3}))X_{1}X_{2},$ (13)

where

$\hat{q}(X_{0},X_{3}):=q(X_{0},0,0,X_{3})$

is the part of $q$ which is independent from $X_{1},X_{2}$. The discriminant $\Delta$ of Equation 13 is

$\Delta(X_{0},X_{3})=(X_{3}^{2})(\hat{q}^{2}-4X_{0}^{2}X_{3}^{2}).$

The external factor $X_{3}^{2}$ corresponds to the intersection of $L_{1,2}$ with the plane $H_{3}$, which is the triple point $[1,0,0,0]$. The four solutions of

$\hat{q}^{2}-4X_{0}^{2}X_{3}^{2}=0$

are the four pinch points along $L_{1,2}$. In particular, the point $[0,0,0,1]$ is a pinch point if and only if $\hat{q}(0,1)=q(0,0,0,1)=0$. For a generic equation in the form 12, this equality does not hold, so the double point $[0,0,0,1]$ has two distinct pre-images in $E_{0,1},E_{0,2}$, hence these are two disjoint curves. An analogous argument holds of course for $[0,0,1,0],[0,1,0,0]$.
Since the matrix of these intersection products in non-degenerate, this states the linear independence of $C,E_{0,1},E_{0,2},E_{0,3}$ in Pic(X) and $H^{2}(X,\mathbb{C})$. $\square$

###### Lemma 54

The surface $X$ is a Coble surface.

Proof: We already know from Proposition 52 that $h^{0}(\mathcal{O}_{X}(K_{X}))=h^{0}(\mathcal{O}_{X}(2K_{X}))=0$ and $h^{0}(\mathcal{O}_{X}(-2K_{X}))=1$.
Let $q=h^{1}(\mathcal{O}_{X})$ be the irregularity of $X$. We apply the Noether formula, see for example *[20]*:

$\chi(\mathcal{O}_{X})=\frac{\chi_{top}(X)+K_{X}^{2}}{12}$

Applying together Poincare duality and the Corollary 52, the left-hand term equals

$\chi(\mathcal{O}_{X})=1-q+h^{0}(\mathcal{O}_{X}(K_{X}))=1-q$

Meanwhile, the right-hand term is

$\frac{\chi_{top}(X)+K_{X}^{2}}{12}=\frac{b_{0}-b_{1}+b_{2}-b_{3}+b_{4}-1}{12}$

where the $b_{i}$’s are the Betti numbers of $X$. We used the equality $K_{X}^{2}=-1$ which comes from Proposition 53. By Serre duality $b_{4}=b_{0}=1$ and $b_{1}=b_{3}$. The Hodge decomposition

$H^{1}(X,\mathbb{C})=H^{1,0}(X)\oplus H^{0,1}(X)$

gives $b_{1}=2q$. Putting all together, we find

$1-q=\frac{1-4q+b_{2}}{12}$

that is

$11-8q=b_{2}$

But Proposition 53 states

$b_{2}\geq 4$

which is equivalent to saying

$q=0$

and

$b_{2}=11.$

$\square$

 the subspace $V\subset H^{0}(\mathcal{O}_{\mathbb{P}^{3}}(5))$ of forms as in (11) has dimension 13. Meanwhile, the subgroup $G\subset GL(4)$ preserving $V$ consists of invertible matrices, which fix the triple point $[1,0,0,0]$ and permute the vertices $[0,1,0,0],[0,0,1,0],[0,0,0,1]$. The dimension of $G$ is 4, since it fits in a short exact sequence of groups

$\mathbb{1}\to D\to G\to\mathcal{S}_{3}\to\mathbb{1}$

Here $D$ consists of all $4\times 4$ invertible diagonal matrices, and the discrete symmetric group $\mathcal{S}_{3}$ acts by permutation on $[0,1,0,0],[0,0,1,0],[0,0,0,1]$. Thus the quotient $V/G$ has still dimension $13-4=9$, the same of the moduli space of Coble.

Suppose we start with a quintic surface $X\subset\mathbb{P}^{3}$ given by the equation:

$\alpha X_{0}X_{2}^{2}X_{3}^{2}+\beta X_{0}X_{1}^{2}X_{3}^{2}+\gamma X_{0}X_{1}^{2}X_{2}^{2}+X_{1}X_{2}X_{3}q(X_{0},X_{1},X_{2},X_{3})=0$

with

$q=\sum_{0\leq i\leq j\leq 3}\lambda_{i,j}X_{i}X_{j}$

Now consider the birational involution of $\mathbb{P}^{3}$ given by:

$i[X_{0},X_{1},X_{2},X_{3}]=[\frac{1}{X_{0}},\frac{1}{X_{1}},\frac{1}{X_{2}},\frac{1}{X_{3}}]=[X_{1}X_{2}X_{3},X_{0}X_{2}X_{3},X_{0}X_{1}X_{3},X_{0}X_{1}X_{2}]$

Under this transformation the equation of $X$ becomes:

$(X_{0}^{3}X_{1}^{2}X_{2}^{2}X_{3}^{2})*(\lambda_{0,0}(X_{1}X_{2}X_{3})^{2}+\lambda_{1,1}(X_{0}X_{2}X_{3})^{2}+\lambda_{2,2}(X_{0}X_{1}X_{3})^{2}+$
$+\lambda_{3,3}(X_{0}X_{1}X_{2})^{2}+X_{0}X_{1}X_{2}X_{3}(\alpha X_{1}^{2}+\beta X_{2}^{2}+\gamma X_{3}^{2}+\sum_{0\leq i<j\leq 3}\hat{\lambda}_{i,j}X_{i}X_{j}))=0$

where the coefficients $\hat{\lambda}_{i,j}$ are defined as

$\hat{\lambda}i,j=\lambda_{b,k}\,\text{if}\,\{i,j\}\cup\{h,k\}=\{0,1,2,3\}$

If we cut out the initial factor $X_{0}^{3}X_{1}^{2}X_{2}^{2}X_{3}^{2}$ we finally arrive at an expression of the form

$\lambda_{0,0}(X_{1}X_{2}X_{3})^{2}+\lambda_{1,1}(X_{0}X_{2}X_{3})^{2}+\lambda_{2,2}(X_{0}X_{1}X_{3})^{2}+\lambda_{3,3}(X_{0}X_{1}X_{2})^{2}+$
$+X_{0}X_{1}X_{2}X_{3}\hat{q}(X_{0},X_{1},X_{2},X_{3})=0$

which is the expression of an Enriques sextic, with the additive 1-codimensional condition that

$\hat{q}(1,0,0,0)=0.$

###### Proposition 55

The linear system on the Coble surface $X$ which realizes the birational map $X\to\mathbb{P}^{3}$ onto an Enriques sextic with a quartic point is $|H^{\prime}|=|9L-3E_{1}-\cdots-3E_{7}-2E_{8}-2E_{9}-2E_{10}|$.

Proof: By definition, we have

$|H|=|6L-2E_{1}-\cdots-2E_{7}-E_{8}-E_{9}-E_{10}|$

The cubo - cubic involution of $\mathbb{P}^{3}$ is defined by the system of cubics containing the tetrahedron $T$, hence

$H^{\prime}=3H-D$

where $D$ is the preimage in $X$ of $T$. But we saw that $D$ is given by the union of $E_{8},E_{9},E_{10}$ and the three plane cubics $-K_{X}+E_{8},-K_{X}+E_{9},-K_{X}+E_{10}$, thus

$D=9L-3E_{1}-\dots-3E_{7}-E_{8}-E_{9}-E_{10}$

Finally, we find

$H^{\prime}=9L-3E_{1}-\dots-3E_{7}-2E_{8}-2E_{9}-2E_{10}$

$\square$

Note that

$H=H^{\prime}+K_{X}$

that is, $H$ is the adjoint linear system of $H^{\prime}$.

### 3.3 Nodal Coble cubic surfaces

Let’s consider three points $p_{1},p_{2},p_{3}\in\mathbb{P}^{2}$, and three lines $l_{1},l_{2},l_{3}\subset\mathbb{P}^{2}$ such that

$p_{i}\in l_{i},\quad p_{i}\notin l_{j}\quad\text{for}\quad i\neq j\in\{1,2,3\}$

If we look at the cubics in $\mathbb{P}^{2}$ passing through $p_{i}$ and tangent to $l_{i}$, we get a subspace $W\subset H^{0}(\mathcal{O}_{\mathbb{P}^{2}}(3))$ with $\dim|\mathrm{W}|=3$. The corresponding rational map $|W|:\mathbb{P}^{2}\dashrightarrow\mathbb{P}^{3}$ has three base points at the $p_{i}$’s. The blow up $\tilde{\mathbb{P}}^{2}$ of $\mathbb{P}^{2}$ at these points does not resolve the indeterminacy of the map, since we have still three base points $p_{i}^{\prime}$ on the exceptional divisors $E_{i}$, for $i=1,2,3$. If one performs a second blow - up on the $p_{i}^{\prime}$’s, the result is a surface $\tilde{\tilde{\mathbb{P}}}^{2}$, with a regular map $\tau:\tilde{\tilde{\mathbb{P}}}^{2}\to\mathbb{P}^{3}$.

If we denote by $\overline{E}_{i}$ the proper transform of $E_{i}$ in $\tilde{\tilde{\mathbb{P}}}^{2}$, and by $F_{i}$ the new exceptional divisors of the second blow - up, then

$\tau^{*}\mathcal{O}_{\mathbb{P}^{3}}(1)=-K_{\tilde{\tilde{\mathbb{P}}}^{2}}=3L-\sum_{i=1}^{3}\overline{E}_{i}-2\sum_{i=1}^{3}F_{i}$

We have the relations

$L^{2}=1,L\overline{E}_{i}=LF_{i}=0,\overline{E}_{i}^{2}=-2,E_{i}F_{i}=1,F_{i}^{2}=-1$

so that

$(\tau^{*}\mathcal{O}_{\mathbb{P}^{3}}(1))^{2}=3$

and

$\overline{E}_{i}\tau^{*}\mathcal{O}_{\mathbb{P}^{3}}(1)=0$

this means that the image of $\tau$ is a cubic surface $S\subset\mathbb{P}^{3}$, and the $\overline{E}_{i}$’s are three smooth rational $(-2)$-curves, which are contracted by $\tau$ to three nodes of $S$.
If $q=[q_{0},q_{1},q_{2},q_{3}]\in S$ is a smooth point, and $H\subset\mathbb{P}^{3}$ is a plane not containing $q$, then we have a projection $\pi_{q}:S\setminus q\to H$, which is a map of degree two. The ramification locus is the curve $R$ made up of points $p$ such that the line $\overline{q,p}$ is tangent to $S$ at $p$. If $F\in H^{0}(\mathcal{O}_{\mathbb{P}^{3}}(3))$ is the equation of $S$, then $R$ is given geometrically by

$F=0,$
$\sum_{i=0}^{3}q_{i}\frac{\partial F}{\partial z_{i}}=0$

This is a curve of degree 6, described as the complete intersection of a cubic and a quadric surface in $\mathbb{P}^{3}$. By construction $R$ has a node at $q$, so its projection $\pi_{q}(R)$ on $H$ is a curve of degree $6-2=4$. Moreover, $R$ of course contains the three nodes of $S$, where the partial derivatives simultaneously vanish. So $\pi_{q}(R)$ is a three - nodal quartic curve, and hence it is rational.

### 3.4 A quartic Coble in $\mathbb{P}^{3}$

Suppose $X$ is a Coble surface, realized as a blow up of ten points $p_{1},\ldots,p_{10}\in\mathbb{P}^{2}$, with exceptional curves $E_{1},\ldots,E_{10}\subset X$. Let $|H|$ be the following linear system:

$|H|:=|4L-E_{1}-\cdots-E_{8}-2E_{10}|$

the linear system of quartics passing through $p_{1},\ldots,p_{8}$ and nodal at $p_{10}$. We have

$\dim|\mathrm{H}|=3$

and

$H^{2}=4$

so that $|H|$ defines a map $f:X\to\mathbb{P}^{3}$ over a quartic surface $Y\subset\mathbb{P}^{3}$. The cubic curve $\hat{F}_{9}$ passing through $p_{1},\ldots,p_{8},p_{10}$ lives in the class $F_{9}\in|3L-E_{1}-\cdots-E_{8}-E_{10}|$ so it satisfies

$H\hat{F}_{9}=2.$

Moreover, we have

$h^{0}(X,H-\hat{F}_{9})=h^{0}(X,L-E_{10})=2,$

so that there are two independent planes in $\mathbb{P}^{3}$ containing the curve

$\hat{l}:=f(\hat{F}_{9}).$

So $\hat{l}$ is a line, and the restricted map $f:\hat{F}_{9}\to\hat{l}$ has degree 2. This means that $\hat{l}$ is a double line for the surface $Y$. Hence, given a general plane $\Gamma\subset\mathbb{P}^{3}$, the intersection $X\cap\Gamma$ is a curve of degree 4 with a double point in $\hat{l}\cap H$. Thus $X\cap\Gamma$ has algebraic genus 2, as well as the general member of $|H|$.

4 Coble conjecture

Coming back to Coble’s original construction, from now on we will assume that the number $n$ of Proposition 32 equals $1$, so that the Coble curve $C\subset X$ is a copy of $\mathbb{P}^{1}$. every automorphism $\phi\in\mathrm{Aut}(\mathrm{X})$ must satisfy

$\phi_{*}(K_{X})=K_{X}\in\mathrm{Pic}(\mathrm{X})$

and consequently,

$\phi(C)=C$

Thus, there exists a well - defined restriction map

$\rho:\mathrm{Aut}(\mathrm{X})\to\mathrm{Aut}(\mathrm{C})\simeq\mathbb{P}\mathrm{GL}(2,\mathbb{C})$

###### Conjecture 56 (Coble, *[6]*)

Is $\mathrm{Ker}\,\rho$ trivial for a general Coble surface $X$ ? What is the image $\mathrm{Im}\ \rho\subset\mathbb{P}GL(2)$?

### 4.1 Pompilj’s method

We refer to *[5]*, *[12]*, *[29]* for the content of this Section.
Let $X$ be a Coble surface with one irreducible boundary component $C\in|-2K_{X}|$. In this chapter, we will reconstruct the path made by Pompilj in an article of 1938 in an attempt to provide a non - trivial element in the kernel of the restriction map $\rho:\mathrm{Aut}(\mathrm{X})\to\mathrm{Aut}(\mathrm{C})\simeq\mathrm{PGL}(2,\mathbb{C})$. The idea was the following: we represent $X$ as a blow-up of ten points $p_{1},\ldots,p_{10}\in\mathbb{P}^{2}$. Let $E_{i}\subset X$ be the exceptional divisor associated to the point $p_{i}$. For every $i=1,\ldots,10$, we consider the linear system $|6L-2E_{1}-\cdots-2E_{i-1}-2E_{i+1}-\cdots-2E_{10}|$. Its sections consist of the strict transforms of sextics with nodes at all $p_{j}$’s but $p_{i}$. One can prove that

$h^{0}(\mathcal{O}_{X}(6L-2E_{1}-\cdots-2E_{i-1}-2E_{i+1}-\cdots-2E_{10}))=2$

and it is easy to show two generators. One of them has the form $2C_{i}$, where $C_{i}$ is the unique cubic curve through $p_{1},\ldots,p_{i-1},p_{i+1},\ldots,p_{10}$, while the other one has the form $C+2E_{i}$. It is also immediate to show that the self intersection of a curve in $|6L-2E_{1}-\cdots-2E_{i-1}-2E_{i+1}-\cdots-2E_{10}|$ is $0$, and the arithmetic genus is $1$. Hence, we have just defined $10$ elliptic fibrations $\pi_{i}:X\to\mathbb{P}^{1}$, and each of them admits a unique double fiber $2C_{i}$.
We need to specialize our attention to three of these points, so we set

$A:=p_{8},B:=p_{9},C:=p_{10}$

and let

$E_{A},E_{B},E_{C}\subset X$

be the corresponding exceptional divisors, and consequently

$\pi_{A}:=\pi_{8}:X\to\mathbb{P}^{1},\pi_{B}:=\pi_{9}:X\to\mathbb{P}^{1},\pi_{C}:=\pi_{10}:X\to\mathbb{P}^{1}$

the associated fibrations.

###### Definition 57

Let $F_{A}$ be a smooth fiber of the fibration $\pi_{A}$, which is an elliptic curve. On $F_{A}$ the divisor $(E_{B}-E_{C})|_{F_{A}}$ has degree zero, so for every point $p\in F_{A}$ there is a unique point $T_{A}(p)\in F_{A}$ satisfying

$T_{A}(p)-p=(E_{B}-E_{C})|_{F_{A}}\text{ in }\mathrm{Pic}(\mathrm{F_{A}})$

Letting $F_{A}$ vary among the smooth fibers of $\pi_{A}$, this defines a birational morphism $T_{A}:X\dashrightarrow X$. In a similar way, we define two morphisms $T_{B},T_{C}:X\dashrightarrow X$ as

$T_{B}(p)-p=(E_{C}-E_{A})|_{F_{B}}\text{ in }\mathrm{Pic}(\mathrm{F_{B}})$

and

$T_{C}(p)-p=(E_{A}-E_{B})|_{F_{C}}\text{ in }\mathrm{Pic}(\mathrm{F_{C}})$

where $F_{B},F_{C}$ are, respectively, smooth fibers of $\pi_{B},\pi_{C}:X\to\mathbb{P}^{1}$, and (respectively) $p\in F_{B},F_{C}$.

Up to now, these are just birational transformations, which fail to be well - defined on the singular, or nonreduced, fibers of $\pi_{A},\pi_{B},\pi_{C}$. Nonetheless, this can be adjusted:

###### Proposition 58

*[5]* The birational morphisms $T_{A},T_{B},T_{C}$ extend to biregular automorphisms of $X$.

Now we need a very simple observation:

###### Proposition 59

If $p_{1},\dots,p_{10}$ are points in $\mathbb{P}^{2}$ such that there exists a reduced sextic curve $\overline{C}$ nodal at the $p_{i}$’s, then the Bertini involution $\sigma$ associated to any eight of these points fixes the remaining two.
In particular, $\sigma$ lifts to a biregular involution on the Coble surface $X:=Bl_{p_{1},\dots,p_{10}}\mathbb{P}^{2}$.

##

Proof: Let $Y$ be the blow up of $\mathbb{P}^2$ at $p_1, \ldots, p_8$. The Bertini involution $\sigma: Y \to Y$ preserves the curves in the linear systems $|-K_Y|, |-2K_Y|$. In particular, let $D_1 \in |-K_Y|$ be the proper transform of the unique plane cubic passing also through $p_9$, and let $D_2 \in |-2K_Y|$ be the strict transform of the sextic $\overline{C}$ having the additional node at $p_9$. The divisor $D_1$ is smooth at $p_9$, while $D_2$ has a node, and these divisors have no common components, because otherwise $D_2 = 2D_1$, which cannot happen because $\overline{C}$ is reduced. As a consequence

$$
D_1 D_2 = (-K_Y)(-2K_Y) = 2
$$

which implies that $D_1, D_2$ intersect at $p_9$ with multiplicity 2, and they have no further points in common. Since both these curves are preserved by $\sigma$, it follows that $\sigma(p_9) = p_9$, and similarly $\sigma(p_{10}) = p_{10}$.

As a consequence, $\sigma$ lifts to a biregular involution of the Coble surface $X = Bl_{p_9,p_{10}}Y = Bl_{p_1,\ldots,p_{10}}\mathbb{P}^2$, which switches the direction of $D_2$ at both $p_9,p_{10}$. $\square$

**Proposition 60** [5] [12] Let $i_A, i_B, i_C$ be the Bertini involutions associated to the points $p_1, \ldots, p_7$, and choosing $A, B, C$ as the eighth point. Then the three automorphisms $T_A, T_B, T_C$ satisfy:

$$
T_A = i_B \circ i_C, T_B = i_C \circ i_A, T_C = i_A \circ i_B
$$

Pompilj claimed the following fact:

$$
(T_C \circ T_B \circ T_A)|_C = \mathbb{1}_C \tag{14}
$$

This equality can be restated in terms of Proposition 60 claiming that

$$
(i_A \circ i_B \circ i_C)|_C^2 = \mathbb{1}
$$

However, Coble proved the following result:

**Theorem 61** [12] For the generic Coble surface $X \in \mathcal{M}_{Co}$ equality (14) is false. The family of Coble $X$ such that (14) actually holds is a divisor in $\mathcal{M}_{Co}$.

Now we will prove the previous Theorem, but it needs a number of technical results.

**Proposition 62** Let $F, G \in H^0(\mathcal{O}_{\mathbb{P}^1}(2))$ two linearly independent quadric forms, and let $\sigma$ be the involution associated to the $g_2^1$ generated by $F, G$. Then the solution of the quadric form $J(F, G) := \frac{\partial F}{\partial u} \frac{\partial G}{\partial v} - \frac{\partial F}{\partial v} \frac{\partial G}{\partial u}$ are the two fixed points of $\sigma$.

61

Proof: The polynomials $F, G$ cannot share a common root $a \in \mathbb{P}^1$, otherwise by hypothesis they would also share its image $\sigma(a)$, contradicting the linear independence of these forms. As a consequence, the map

$$
h: \mathbb{P}^1 \to \mathbb{P}^1, h(u, v) := (F(u, v), G(u, v))
$$

is a well defined regular double cover. The corresponding deck involution is $\sigma$ itself by construction. The fixed locus of $\sigma$ is the ramification locus, where $h$ fails to be a local isomorphism, and hence is given by the annihilation of the Jacobian determinant

$$
J(F, G) = \det \left( \begin{array}{cc} \frac{\partial F}{\partial u} &amp; \frac{\partial F}{\partial v} \\ \frac{\partial G}{\partial u} &amp; \frac{\partial G}{\partial v} \end{array} \right) = 0.
$$

☐

Definition 63 Let $X \subset \mathbb{P}^m$ be a hypersurface, defined by a homogeneous equation $F(Z_0, \ldots, Z_m) = 0$ in the projective coordinates $[Z_0, \ldots, Z_m]$. If $p = [p_0, \ldots, p_m]$ is any point in $\mathbb{P}^m$, the hypersurface given by

$$
P := \{ [z] \in \mathbb{P}^m \text{ such that } \sum_{i=0}^m p_i \frac{\partial F}{\partial Z_i}([z]) = 0 \}
$$

is called polar hypersurface to $X$, with centre $p$.

Remark 64, despite the name, the polar hypersurface $P$ with centre $p$ does not necessarily contain $p$. Indeed, by Euler's formula, $p \in P$ if and only if $p \in X$.

In particular, if $Q \subset \mathbb{P}^2$ is a smooth quadric, its polar hypersurfaces are lines. If the centre $p$ lies in $Q$, then the polar line is exactly the tangent at $Q$ in $p$. If $p \notin Q$, then there are two points $q_1, q_2$ such that the lines $\overline{q_i, p}$ are tangent to $Q$ at $q_i$. In this case, the polar line is exactly $\overline{q_1, q_2}$.

The following theorem is a standard result in plane geometry, due to Pascal.

Theorem 65 (Pascal) [32] Let consider six points $p_1, \ldots, p_6$ lying on a smooth conic $Q \subset \mathbb{P}^2$. Let consider an hexagon inscribed in $Q$ with vertices the $p_i$'s, with edges $l_1, l_2, l_3, m_1, m_2, m_3$, labeled so that every vertex $p_i$ belongs to exactly one of the $l_i$'s, and one of the $m_i$'s. Then the three points $l_1 \cap m_1, l_2 \cap m_2, l_3 \cap m_3$ are collinear.

62

Let identify the conic $Q$ with $\mathbb{P}^{1}$. Consider the restriction map

$H^{0}(\mathcal{O}_{\mathbb{P}^{2}}(3L))\to H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))$

and let $V\subset H^{0}(\mathcal{O}_{\mathbb{P}^{2}}(3L))$ be the pencil generated by the cubic forms $l_{1}l_{2}l_{3}$ and $m_{1}m_{2}m_{3}$. It has 9 base points, namely the 6 vertices, and the three points $l_{i}\cap m_{i}$. The image of $V$ in $H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))$ has rank 1, because both the two generators of $V$ restrict to the divisor $p_{1}+\cdots+p_{6}$. Hence there exist $[\lambda,\mu]\in\mathbb{P}^{1}$ such that the section $\lambda l_{1}l_{2}l_{3}+\mu m_{1}m_{2}m_{3}$ restricts to the zero section in $H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))$, so the corresponding cubic splits as $Q+L$, where $L$ is a line which must necessarily contain the points $l_{i}\cap m_{i}$. $\square$

###### Proposition 66

*[12]* Let $\sigma_{1},\sigma_{2},\sigma_{3}$ three involutions of $\mathbb{P}^{1}$, and let

$G_{1},G_{2},G_{3}\in H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(2))$

the three quadric forms vanishing respectively on the pairs of fixed points of $\sigma_{1},\sigma_{2},\sigma_{3}$. If the composition $\sigma_{1}\circ\sigma_{2}\circ\sigma_{3}$ is still an involution, then $G_{1},G_{2},G_{3}$ are linearly dependent.

Proof: Let consider the Veronese embedding $v:\mathbb{P}^{1}\to\mathbb{P}^{2}$, which identifies $\mathbb{P}^{1}$ as a smooth conic $Q\subset\mathbb{P}^{2}$. Then there are three points $p_{1},p_{2},p_{3}\notin Q$, and a line $l\subset\mathbb{P}^{2}$ not containing any of the $p_{i}$’s, such that the induced involutions through $v$ on $Q$ correspond to the deck involutions of the double covers $\pi_{p_{i}}:Q\to l$, where $\pi_{p_{i}}$ is the projection with center $p_{i}$. Let $P_{i}$ be the polar lines to $Q$ with center $p_{i}$. The crucial point is that the $p_{i}$’s are collinear. This follows from Pascal’s Theorem 65, choosing a random point $x\in Q$ and considering the hexagon with edges

$l_{1}$ $=$ $\overline{x,\sigma_{1}(x)}\,,\,\,m_{2}=\overline{\sigma_{1}(x),\sigma_{2}\sigma_{1}(x)}\,,\,\,l_{3}=\overline{\sigma_{2}\sigma_{1}(x),\sigma_{3}\sigma_{2}\sigma_{1}(x)}$
$m_{1}$ $=$ $\overline{\sigma_{3}\sigma_{2}\sigma_{1}(x),\sigma_{1}\sigma_{3}\sigma_{2}\sigma_{1}(x)}\,,\,\,l_{2}=\overline{\sigma_{1}\sigma_{3}\sigma_{2}\sigma_{1}(x),\sigma_{2}\sigma_{1}\sigma_{3}\sigma_{2}\sigma_{1}(x)}\,,$
$m_{3}$ $=$ $\overline{\sigma_{2}\sigma_{1}\sigma_{3}\sigma_{2}\sigma_{1}(x),x}\,.$

Indeed, by construction, the point $p_{i}$ is exactly the intersection

$p_{i}=l_{i}\cap m_{i}$

By Definition 63, the $P_{i}$’s are linear combinations of the partials $\frac{\partial Q}{\partial Z_{j}}$, with coefficients the projective coordinates of $p_{i}$’s. Since the centers lie on the same line, the $P_{i}$ are linearly dependent, and so $G_{i}=v^{*}P_{i}$ are linearly dependent too. $\square$

Now we have all the ingredients we need to prove Theorem 61:

Proof of Theorem 61: A $10$-nodal sextic plane curve $\overline{C}\subset\mathbb{P}^{2}$ is rational, hence there exists a regular birational parametrization

$\gamma:\mathbb{P}^{1}\to\overline{C}\subset\mathbb{P}^{2}$

We write

$\gamma(u,v)=[F_{0}(u,v),F_{1}(u,v),F_{2}(u,v)]$

where $F_{0},F_{1},F_{2}$ are linearly independent forms of degree $6$. Up to an automorphism of $\mathbb{P}^{2}$, we can assume that three nodes of $\overline{C}$ are placed at the points $[1,0,0],[0,1,0],[0,0,1]$. The curve $\overline{C}$ passes twice over $[0,0,1]$, so $F_{0},F_{1}$ must share two common roots. The same holds for the pairs $(F_{0},F_{2})$ and $(F_{1},F_{2})$. Thus, it is not a restriction to assume that there exist

$A,B,C,G_{0},G_{1},G_{2}\in H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(2))$

such that the $F_{i}$’s factor as:

$F_{0}=BCG_{0},F_{1}=ACG_{1},F_{2}=ABG_{2}$

The polynomials $B,C$ are invariant under the Bertini involution $(i_{A})|_{C}$, and the same is true for the pairs $(A,C),(A,B)$ with respect to $(i_{B})|_{C},(i_{C})|_{C}$. Proposition 62 implies that the three quadric Jacobian forms

$J(A,B)$ $=\frac{\partial A}{\partial u}\frac{\partial B}{\partial v}-\frac{\partial A}{\partial v}\frac{\partial B}{\partial u}$
$J(A,C)$ $=\frac{\partial A}{\partial u}\frac{\partial C}{\partial v}-\frac{\partial A}{\partial v}\frac{\partial C}{\partial u}$
$J(B,C)$ $=\frac{\partial B}{\partial u}\frac{\partial B}{\partial v}-\frac{\partial C}{\partial v}\frac{\partial B}{\partial u}$

vanish on the pairs of fixed points of $(i_{C})|_{C},(i_{B})|_{C},(i_{A})|_{C}$ respectively, and Proposition 66 forces these Jacobians to be linearly dependent. But this defines a determinantal equation over the coefficients of $A,B,C$. $\square$

If we write down explicitly $A,B,C\in H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(2))$, say

$A=a_{0}u^{2}+a_{1}uv+a_{2}v^{2}$
$B=b_{0}u^{2}+b_{1}uv+b_{2}v^{2}$
$C=c_{0}u^{2}+c_{1}uv+c_{2}v^{2},$

then

$J(B,C)=(b_{0}c_{1}-b_{1}c_{0})u^{2}+2(b_{0}c_{2}-b_{2}c_{0})uv+(b_{1}c_{2}-b_{2}c_{1})v^{2}$

$J(A,C)$ $=(a_{0}c_{1}-a_{1}c_{0})u^{2}+2(a_{0}c_{2}-a_{2}c_{0})uv+(a_{1}c_{2}-a_{2}c_{1})v^{2}$

$J(A,B)$ $=(a_{0}b_{1}-a_{1}b_{0})u^{2}+2(a_{0}b_{2}-a_{2}b_{0})uv+(a_{1}b_{2}-a_{2}b_{1})v^{2}$

Let $M,N$ be the matrices

$M:=\left(\matrix{a_{0}&a_{1}&a_{2}\cr b_{0}&b_{1}&b_{2}\cr c_{0}&c_{1}&c_{2}}\right)$

$N:=\left(\matrix{b_{0}c_{1}-b_{1}c_{0}&b_{0}c_{2}-b_{2}c_{0}&b_{1}c_{2}-b_{2}c_{1}\cr a_{0}c_{1}-a_{1}c_{0}&a_{0}c_{2}-a_{2}c_{0}&a_{1}c_{2}-a_{2}c_{1}\cr a_{0}b_{1}-a_{1}b_{0}&a_{0}b_{2}-a_{2}b_{0}&a_{1}b_{2}-a_{2}b_{1}}\right)$

Up to a permutation of columns, and a factor 2, we have

$N=(\det{\rm M}){\rm M}^{-1}$

and hence

$\det{\rm N}=(\det{\rm M})^{2}$

Thus the linear dependence of the three Jacobian forms $J(A,B),J(A,C),J(B,C)$ is equivalent to the one of $A,B,C$. We now consider the product space ${\mathbb{P}}^{2}\times{\mathbb{P}}^{2}$, where we put projective coordinates $[X_{0},X_{1},X_{2}],[Y_{0},Y_{1},Y_{2}]$. We denote $\pi_{1}$ the projection on the $X$-coordinates, and $\pi_{2}$ the projection on the $Y$-coordinates. Let $\lambda$ be the morphism $\lambda:{\mathbb{P}}^{1}\to{\mathbb{P}}^{2}\times{\mathbb{P}}^{2}$,

$\gamma(u,v):=([BC(u,v),AC(u,v),AB(u,v)],[G_{0}(u,v),G_{1}(u,v),G_{2}(u,v)]).$

For a generic choice of $A,B,C$, the morphism $\pi_{1}\circ\lambda=[BC,AC,AB]$ is the normalization of a 3-nodal quartic. The special case when the image of $\pi_{1}\circ\lambda$ is a conic corresponds to a polynomial $H(X_{0},X_{1},X_{2})\in H^{0}({\cal O}_{{\mathbb{P}}^{2}}(2))$ such that $H\circ\pi_{1}\circ\lambda=0$. Since the points $[1,0,0],[0,1,0],[0,0,1]$ must belong to $V(H)$, $H$ must have the form $H=\alpha X_{1}X_{2}+\beta X_{0}X_{2}+\gamma X_{0}X_{1}$, so the relation

$H\circ\pi_{1}\circ\lambda=0$

becomes

$ABC(\alpha A+\beta B+\gamma C)=0.$

Thus the image of $\pi_{1}\circ\lambda$ is a quartic if and only if $A,B,C$ are linearly independent. Meanwhile, the composition $\pi_{2}\circ\lambda$ is an isomorphism on a smooth plane conic.
Remember that there exists a natural Segre embedding ${\mathbb{P}}^{2}\times{\mathbb{P}}^{2}\subset{\mathbb{P}}^{8}$, defined by the complete linear system $|{\cal O}_{{\mathbb{P}}^{2}\times{\mathbb{P}}^{2}}(1,1)|$. With respect to this embedding,

the image $\lambda(\mathbb{P}^{1})$ has degree 6, since the two factors $\pi_{1}\circ\lambda$ and $\pi_{2}\circ\lambda$ have degree 4 and 2 respectively. Thus there exist a linear subspace $\mathbb{P}^{6}\subset\mathbb{P}^{8}$ containing $\lambda(\mathbb{P}^{1})$. The intersection

$S:=\mathbb{P}^{6}\cap(\mathbb{P}^{2}\times\mathbb{P}^{2})$

is a surface. It projects birationally on both the factors, hence $S$ is a rational surface. Let $\rho:\mathbb{P}^{2}\times\mathbb{P}^{2}\dashrightarrow\mathbb{P}^{2}$ be the map

$\rho([X_{0},X_{1},X_{2}],[Y_{0},Y_{1},Y_{2}]):=[X_{0}Y_{0},X_{1}Y_{1},X_{2}Y_{2}]$

Then the original morphism $\mathbb{P}^{1}\to\mathbb{P}^{2}$ given by $[BCG_{0},ACG_{1},ABG_{2}]$ factors as the composition

$\gamma=\rho\circ\lambda$

If $A,B,C$ are linearly dependent, then we know that the morphism

$\pi_{1}\circ\lambda,\pi_{2}\circ\lambda:\mathbb{P}^{1}\to\mathbb{P}^{2}$

have degree $2,1$ respectively on smooth plane conics. Thus we can think of $\lambda(\mathbb{P}^{1})$ as a curve of type $(2,1)$ inside $\mathbb{P}^{1}\times\mathbb{P}^{1}$. In this case, the inclusion map $\mathbb{P}^{1}\times\mathbb{P}^{1}\to\mathbb{P}^{2}\times\mathbb{P}^{2}$ is given by the cartesian product of two Veronese embeddings of degree 2, hence the composite morphism

$\mathbb{P}^{1}\times\mathbb{P}^{1}\to\mathbb{P}^{2}\times\mathbb{P}^{2}\xrightarrow{\rho}\mathbb{P}^{2}$

is induced by a net in the linear system $|\mathcal{O}_{\mathbb{P}^{1}\times\mathbb{P}^{1}}(2,2)|$.

##

5 Involutions on Coble surfaces

We focus our attention to the case of the biregular involutions of $X$, so let $i\neq id_{X}$ satisfy

$i^{2}=\mathbb{1}_{X}$

The main results of this Section are two: if $X$ is a Coble surface with irreducible boundary curve $\{C\}=|-2K_{X}|$, then there are no involutions which pointwise fix $C$.
Moreover, if $X$ is also unnodal, then any involution is the lift of a Bertini involution.
We will need the following lemma:

###### Lemma 67 (Dolgachev, Zhang)

*[36]* Suppose $X$ is a smooth rational algebraic surface, and $\psi:X\to X$ a non trivial automorphism of finite prime order $p$. Then the fixed locus $\operatorname{Fix}(\psi)$ is a disjoint union of smooth curves and isolated fixed points, that is, it is smooth.

### 5.1 Classifying involutions

We follow the definition given by Bayle-Beauville in *[2]* and Dolgachev - Zhang in *[36]* :

###### Definition 68

Consider the set of all possible pairs $(X,i)$, where $X$ is a smooth rational projective surface, and $i$ is a non-trivial involution.
An equivariant morphism $\phi:(X,i)\to(X^{\prime},i^{\prime})$ is a (regular) birational morphism $\phi:X\to X^{\prime}$ such that $i^{\prime}\circ\phi=\phi\circ i$.
We say that a pair $(X,i)$ is minimal if every equivariant morphism $(X,i)\to(X^{\prime},i^{\prime})$ to any other pair $(X^{\prime},i^{\prime})$ is an isomorphism.

###### Proposition 69

*[2]* A pair $(X,i)$ is minimal if and only if for every smooth rational $(-1)$-curve $E\subset X$, both relations

$i(E)\neq E$

and

$i(E)\cap E\neq\emptyset$

are true.

###### Lemma 70

*[2]* Assume $(X,i)$ is a minimal pair. Then one of the following cases is necessarily true:

i) There exists a smooth $\mathbb{P}^{1}$-fibration $f:X\to\mathbb{P}^{1}$, stable under $i$. In other words, there exists a non-trivial involution $\tau$ on $\mathbb{P}^{1}$, such that:

$\tau\circ f=f\circ i.$

ii) There exist a conic fibration $f:X\to\mathbb{P}^{1}$ such that

$f\circ i=f$

In other words, $i$ preserves the fibers of $f$. The smooth fibers are rational curves. Each singular fiber is a linear chain of two $(-1)$-curves attached at one point, and exchanged by $i$. The fixed locus $\mathrm{Fix(i)}$ is smooth and it has pure dimension $1$, and it is a bisection of $f$, ramified exactly at the singular points of the singular fibers. Moreover, $\mathrm{Fix(i)}$ splits as a union of two disjoint sections of $f$ if and only if $f$ has no singular fibers.
iii) $X=\mathbb{P}^{2}$, and $i$ is a projective linear involution.
iv) $X=\mathbb{P}^{1}\times\mathbb{P}^{1}$, and $i(x,y)=(y,x)$ is the involution switching the two factors.
v) $X$ is a Del Pezzo surface of degree $2$, and $i$ is the Geiser involution.
vi) $X$ is a Del Pezzo surface of degree $1$, and $i$ is the Bertini involution.
Viceversa, a pair $(X,i)$ built as in case $i),\ldots,vi)$ is actually minimal, except the following ones:
Case i), when $X=\mathbb{F}_{1}$ is the first Hirzebruch surface, or
Case ii), when $X=\mathbb{F}_{1}$, or $X=BI_{p_{1},p_{2},p_{3}}\mathbb{P}^{2}$, with $p_{i}$’s non collinear points, and $i$ is the De - Jonquieres involution of degree $2$ (the quadro-quadric involution centered at $p_{1},p_{2},p_{3}$).

Lemma 70 allows us to exclude any involution $i\in\mathrm{Aut(X)}$ to satisfy $i|_{C}=C$, if $C$ is irreducible:

###### Proposition 71

On a Coble surface $X$ with irreducible curve $C\in|-2K_{X}|$ there is no involution $i$ such that $i|_{C}=\mathbbm{1}_{C}$.

Proof: Assume such an involution $i$ actually exists: we first show that the pair $(X,i)$ must necessarily be minimal, using Proposition 69 and Lemma 67.
Indeed, if $E\subset X$ is any $(-1)$-curve such that $i(E)=E$, then we can execute the blow down $\pi:X\to X^{\prime}$, which comes together with an involution $i^{\prime}:X^{\prime}\to X^{\prime}$. But the relation

$EK_{X}=-1$

implies

$EC=2,$

so the curve $\pi(C)$ is singular and lies inside the fixed locus of $i^{\prime}$, a contradiction. This forces $i(E)\neq E$, and the relation $i(E)\cap E\neq\emptyset$ is obvious, since $E,i(E)$ at least share the two points in $E\cap C$.
So the pair $(X,i)$ is minimal, and hence we lie inside one of the cases $i),\ldots,vi)$ of Lemma 70. Of course $X$ is not isomorphic to $\mathbb{P}^{2},\mathbb{P}^{1}\times\mathbb{P}^{1}$, nor to a Del Pezzo or Hirzebruch surface, so the unique admissible case is ii). Thus we find a fibration $f:X\to\mathbb{P}^{1}$, whose fibers are rational curves preserved by $i$.
Let $F\in\mathrm{Pic(X)}$ be the class of a fiber: the rationality of $F$ gives

$FK_{X}=-2$

and hence

$FC=4,$

so $C$ is a $4$-section of $f$. This is a contradiction, since Lemma 70 states that $\mathrm{Fix(i)}$ must be a bi-section. The contradiction follows from the initial assumption on the existence of such an involution $i$. $\square$

We saw in Remark 4.1 that on a Coble surface $X$ with irreducible boundary, it is always possible to construct involutions whose minimal model is the Bertini involution. Actually, we can show more:

###### Theorem 72

On an unnodal Coble surface $X$ with irreducible Coble curve $C$, any involution is the lift of a Bertini involution.

Before starting the proof, we point out that the vice versa is false: you can build Coble surfaces with reducible boundary, equipped with involutions which are lifts of a Bertini, as in the following example.

###### Example 73

Consider the construction of Remark 39, where we considered a rational sextic $\overline{C}\subset\mathbb{P}^{2}$ with $7$ nodes at points $p_{1},\ldots,p_{7}$, and a triple point $p_{8}$. The surface $X^{\prime}=Bl_{8}\mathbb{P}^{2}$ of these eight points is a Del Pezzo surface, equipped with the Bertini involution $i^{\prime}:X^{\prime}\to X^{\prime}$, which switches the strict transform $D\subset X^{\prime}$ of $\overline{C}$ with the exceptional divisor $E_{8}$. When we blow - up the three intersection points in $D\cap E_{8}$, we get a Coble surface $X$ with $2$ boundary components, still equipped with an involution $i:X\to X$ induced by $i^{\prime}$.

The following construction is remarkable, since it provides a Coble surface with $2$ boundary components, both preserved by a lift of the Bertini involution:

###### Example 74

Let $X^{\prime}:=Bl_{p_{1},\ldots,p_{8}}\mathbb{P}^{2}$ be a Del Pezzo surface of degree $1$, with its Bertini involution $i^{\prime}:X^{\prime}\to X^{\prime}$. Consider the anti canonical pencil $|-K_{X^{\prime}}|$: we know that it consists of curves of genus $1$, each preserved by $i^{\prime}$. Moreover, $|-K_{X^{\prime}}|$ has a base point $p_{9}$, which is an isolated fixed point for $i^{\prime}$. Let $\overline{C}_{1},\overline{C}_{2}\in|-K_{X^{\prime}}|$ be two irreducible singular members, with nodes at two points $q_{1},q_{2}$. Then both $q_{1},q_{2}$ must be fixed by $i^{\prime}$, so we can blow - up again $X:=Bl_{p_{9},q_{1},q_{2}}X^{\prime}$ to obtain a Coble surface $X$. This is a Coble surface, since its anti - bicanonical class contains the divisor $C_{1}+C_{2}$, where $C_{i}\subset X$ is the strict transform of $\overline{C}_{i}$. Moreover, by construction, $X$ is equipped with a lifted Bertini involution which preserves both $C_{1},C_{2}$.

We refer to *[22]* for the construction of a Coble surface with three boundary components, equipped with a Bertini involution.
We also, on a given unnodal Coble surface $X$ with irreducible Coble curve $C$, there is not only “one” lift of a Bertini involution: indeed, given any two disjoint $(-1)$-curves $E_{1},E_{2}\subset X$, we can think of them as the start of a sequence $E_{1},\ldots,E_{10}$ of disjoint $(-1)$-curves, whose blow - down is $\mathbb{P}^{2}$, thanks to Proposition 42. But then, the blow - down $p:X\to X^{\prime}$ of just $E_{1},E_{2}$ is a Del Pezzo surface $X^{\prime}$ of degree $1$, and this is equipped with its Bertini involution $i^{\prime}:X^{\prime}\to X^{\prime}$. Moreover, the base points $p(E_{1}),p(E_{2})\in X^{\prime}$ are nodes for the curve $p(C)$, because $CE_{1}=CE_{2}=2$, and these two points are fixed by $i^{\prime}$ by Remark 4.1. But then $i^{\prime}$ lifts to a non - minimal involution $i:X\to X$, which preserves both $E_{1},E_{2}$. Hence any pair of disjoint $(-1)$-curves on $X$ determines a different lift of a Bertini involution.
The proof of Theorem 72 needs the following trick, which we will use repeatedly in the following:

###### Remark 75

We showed in Proposition 42 that, if $X$ has irreducible anti - bicanonical curve $C\in|-2K_{X}|$ and it does not contain $(-2)$-curves, then any set of three disjoint $(-1)$-curves $E_{1},E_{2},E_{3}\subset X$ can be extended to a maximal sequence $E_{1},\ldots,E_{10}$, such that their contraction transforms $X$ in $\mathbb{P}^{2}$. In this case the class of $C$ becomes $C=6L-2E_{1}-\cdots-2E_{10}$. Now look at the system

$H:=C+E_{1}+E_{2}+E_{3}=6L-E_{1}-E_{2}-E_{3}-2E_{4}-\cdots-2E_{10}.$

We saw in Subsection 3.2 that $|H|$ induces a birational map on a quintic surface in $\mathbb{P}^{3}$, and we described its singularities. Note then that an involution $i$ on $X$ which preserves each of $E_{1},E_{2},E_{3}$ must act as the identity on one of them. Indeed, $i$ preserves the linear system $H=C+E_{1}+E_{2}+E_{3}$, so it

induces a commutative diagram:

![img-3.jpeg](img-3.jpeg)

The plane  $\Pi \subset \mathbb{P}^3$  corresponding to the section  $C + E_1 + E_2 + E_3$  is preserved by  $I$  by construction. Let  $L_i$  be the image of  $E_i$  inside  $\Pi$ . Since  $i$  preserves all the  $E_i$ 's, the involution  $I$  must preserve all the  $L_i$ . But then  $I$  fixes the three intersection points  $L_i \cap L_j$ , and hence one of the  $L_i$ , say  $L_1$ , must be a fixed line.

We point out that we used the hypothesis that  $X$  is unnodal in Remark 75, and we will show later in a couter - example that it can not be dropped. This Remark will be used to exclude case  $v$ ) of Lemma 70.

Corollary 76 Given a degree 2 Del Pezzo surface  $X'$  equipped with its Geiser involution  $i': X' \to X'$ , and an unnodal Coble surface  $X$  with irreducible boundary, it is impossible to build a commutative diagram:

![img-4.jpeg](img-4.jpeg)

Proof: We should blow up three points on  $X'$  in a smart way to get a well defined involution on  $X$ . Remember that, for any  $p \in X'$  such that  $i'(p) \neq p$ , there exist a pencil of sections of  $|-K_{X'}|$  containing both  $p, i'(p)$ . We should pick

$$
p _ {1}, p _ {2}, p _ {3} \in X ^ {\prime}
$$

preserved by  $i'$ . Assume

$$
i ^ {\prime} (p _ {1}) = p _ {2}, i ^ {\prime} (p _ {2}) = p _ {1}, i ^ {\prime} (p _ {3}) = p _ {3}.
$$

Then there exists a divisor in  $| - K_{X'}|$  containing all the three points, so we would have  $| - K_X| \neq \emptyset$ .

Hence we are forced to pick

$$
p _ {1}, p _ {2}, p _ {3} \in \operatorname {F i x} (i ^ {\prime})
$$

If we assume by contradiction that the surface  $X \coloneqq Bl_{p_1,p_2,p_3}X'$  is an unnodal Coble surface, with a irreducible divisor  $C \in | - 2K_X|$ , then we end up

exactly in the situation forbidden by the previous Remark 75. $\square$

 the following example nonetheless provides a Coble surface with reducible anti - bicanonical divisor equipped with a Geiser involution.

###### Example 77

Let $Q\subset\mathbb{P}^{2}$ be a smooth quartic, that is, a curve of genus $3$, canonically embedded in $\mathbb{P}^{2}$. It is well-known that there exist $63$ families of plane quadrics which are totally tangent to $Q$. Indeed, this corresponds to choosing $p_{1},p_{2},p_{3},p_{4}\in Q$ such that $2p_{1}+2p_{2}+2p_{3}+2p_{4}\in|2K_{Q}|$. Hence

$p_{1}+p_{2}+p_{3}+p_{4}\in|K_{Q}+\eta|$

where $\eta$ is a nontrivial $2$-torsion divisor on $Q$. There are exactly $63$ such divisors, and each of them satisfies (by Riemann - Roch):

$h^{0}(\mathcal{O}_{Q}(p_{1}+p_{2}+p_{3}+p_{4}+\eta))=2$

Let then $C\subset\mathbb{P}^{2}$ be one of these smooth conics, and let $\pi:X^{\prime}\to\mathbb{P}^{2}$ be the double cover branched over $Q$. Then $X^{\prime}$ is a smooth Del Pezzo surface of degree $2$. The pre - image $\pi^{-1}(C)$ is a section of $|-2K_{X^{\prime}}|$, of the form

$\pi^{-1}(C)=C_{1}+C_{2},$

where $C_{1},C_{2}$ are smooth rational curves, which meet at $4$ points $p^{\prime}_{1},p^{\prime}_{2},p^{\prime}_{3},p^{\prime}_{4}$ on the ramification locus of $\pi$. Then $X:=Bl_{p^{\prime}_{1},p^{\prime}_{2},p^{\prime}_{3},p^{\prime}_{4}}X^{\prime}$ is a Coble surface, with $2$ boundary components, equipped with a biregular involution, which is induced by the Geiser involution.

The following example is more tricky, since it provides the construction of a Coble surface $X$, equipped with an involution $i$ induced by a Geiser involution, which preserves all the components of the anti - bicanonical divisor $|-2K_{X}|$.

###### Example 78

Let $Q\subset\mathbb{P}^{2}$ be an irreducible rational quartic curve with three nodes, and let $p:Y\to\mathbb{P}^{2}$ be the blow up of the plane at the singular points of $Q$. Consider the double cover

$q:X^{\prime}\to Y$

branched over the strict transform of $Q$, and let $i^{\prime}:X^{\prime}\to X^{\prime}$ be the deck involution. As usual, let $L,E_{1},E_{2},E_{3}$ be the generators of $\mathrm{Pic}(\mathrm{Y})$. Then

$K_{Y}=-3L+E_{1}+E_{2}+E_{3}$

and

$K_{X^{\prime}}=-q^{*}L$

which means that the composite map $pq:X^{\prime}\to\mathbb{P}^{2}$ is induced by the anti canonical linear system. Moreover, $(-K_{X^{\prime}})^{2}=(pq)^{*}L^{2}=2$, which states that $X$ is a Del Pezzo surface of degree $2$. Each curve $E_{1},E_{2},E_{3}$ in $Y$ cuts in two points the branch locus, hence the preimages $q^{*}E_{1},q^{*}E_{2},q^{*}E_{3}$ are three $(-2)$-curves in $X^{\prime}$. Let $B\subset Y$ be the branch locus of $q$, and let $R\subset X^{\prime}$ be the ramification locus. The class of $R$ is

$R=\frac{1}{2}q^{*}(4L-2E_{1}-2E_{2}-2E_{3})=q^{*}(2L-E_{1}-E_{2}-E_{3}),$

so the divisor $R+q^{*}E_{1}+q^{*}E_{2}+q^{*}E_{3}$ belongs to the class

$R+q^{*}E_{1}+q^{*}E_{2}+q^{*}E_{3}\in|q^{*}(2L)|=|-2K_{X^{\prime}}|.$

All the four components are smooth rational curves, which meet at $R(q^{*}E_{1}+q^{*}E_{2}+q^{*}E_{3})=6$ points, all fixed by $i^{\prime}$. Thus we can blow up these points on $X^{\prime}$ to get a Coble surface $X$ with $4$ boundary components, together with an involution $i:X\to X$ which preserves all of them.

In Remark 75 we used the linear system $H=C+E_{1}+E_{2}+E_{3}$ under the hypothesis that $X$ is unnodal, $C$ is irreducible and the $E_{i}$’s are disjoint. We now show that the unnodality of $X$ can not be dropped. We start showing that $H$ has still almost all its good properties.

###### Proposition 79

Let $X$ be a Coble surface, with irreducible anti - bicanonical curve $C\in|-2K_{X}|$, and let $E_{1},E_{2},E_{3}$ three disjoint $(-1)$-curves in $X$. Then $H:=C+E_{1}+E_{2}+E_{3}$ has no base points or base components, and it has dimension $h^{0}(\mathcal{O}_{X}(H))=4$. The images of the $E_{i}$ under the map $f_{|H|}:X\to\mathbb{P}^{3}$ are three pairwise distinct lines lying in the same plane of $\mathbb{P}^{3}$.

Proof: For any sequence of disjoint $(-1)$-curves $E_{1},\ldots,E_{r}$ in $X$ one has

$h^{0}(\mathcal{O}_{X}(E_{1}+\cdots+E_{r}))=1$

and

$h^{1}(\mathcal{O}_{X}(E_{1}+\cdots+E_{r}))=0$

Indeed, the short exact sequence

$0\to\mathcal{O}_{X}(E_{1}+\cdots+E_{r-1})\to\mathcal{O}_{X}(E_{1}+\cdots+E_{r})\to\mathcal{O}_{E_{r}}(E_{1}+\cdots E_{r})\to 0$

induces isomorphisms

$H^{0}(\mathcal{O}_{X}(E_{1}+\cdots+E_{r-1}))\simeq H^{0}(\mathcal{O}_{X}(E_{1}+\cdots+E_{r}))$

and

$H^{1}(\mathcal{O}_{X}(E_{1}+\cdots+E_{r-1}))\simeq H^{1}(\mathcal{O}_{X}(E_{1}+\cdots+E_{r}))$

so by induction we find

$h^{0}(\mathcal{O}_{X}(E_{1}+\cdots+E_{r}))=h^{0}(\mathcal{O}_{X})=1$ (15)

and

$h^{1}(\mathcal{O}_{X}(E_{1}+\cdots+E_{r}))=h^{1}(\mathcal{O}_{X})=0.$ (16)

Now we look at the short exact sequence:

$0\to\mathcal{O}_{X}(-C)\to\mathcal{O}_{X}\to\mathcal{O}_{C}\to 0.$ (17)

Taking the tensor with $\mathcal{O}_{X}(H)$ we find:

$0\to\mathcal{O}_{X}(E_{1}+E_{2}+E_{3})\to\mathcal{O}_{X}(H)\to\mathcal{O}_{C}(H)\to 0$

Now we it remains exact on global sections, due to equality 16, so we find an exact sequence

$0\to H^{0}(\mathcal{O}_{X}(E_{1}+E_{2}+E_{3}))\to H^{0}(\mathcal{O}_{X}(H))\to H^{0}(\mathcal{O}_{C}(H))\to 0.$

Note that

$\mathcal{O}_{C}(H)\simeq\mathcal{O}_{\mathbb{P}^{1}}(CH)=\mathcal{O}_{\mathbb{P}^{1}}(2).$

Together with equality 15, this shows that $h^{0}(\mathcal{O}_{X}(H))=4$ and that $C$ is not a base component of $H$, since $h^{0}(\mathcal{O}_{X}(H-C))=h^{0}(\mathcal{O}_{X}(E_{1}+E_{2}+E_{3}))=1<4$. Moreover, the surjectivity of $H^{0}(\mathcal{O}_{X}(H))\to H^{0}(\mathcal{O}_{C}(H))$ proves that $H$ has not base points on the curve $C$.
Now we tensor the short exact sequence in 17 with $\mathcal{O}_{X}(C+E_{1}+E_{2})$, and applying equalities 15 and 16 we find

$h^{0}(\mathcal{O}_{X}(C+E_{1}+E_{2}))=2$ (18)

and

$h^{1}(\mathcal{O}_{X}(C+E_{1}+E_{2}))=0.$ (19)

Finally, we consider

$0\to\mathcal{O}_{X}(C+E_{1}+E_{2})\to\mathcal{O}_{X}(H)\to\mathcal{O}_{E_{3}}(H)\to 0$

Equalities 18 and 19 state that the induced sequence on global sections

$0\to H^{0}(\mathcal{O}_{X}(C+E_{1}+E_{2}))\to H^{0}(\mathcal{O}_{X}(H))\to H^{0}(\mathcal{O}_{E_{3}}(H))\to 0$

is still exact. The surjectivity of $H^{0}(\mathcal{O}_{X}(H))\to H^{0}(\mathcal{O}_{E_{3}}(H))$ shows that $H$ has no base points on $E_{3}$, and the exactness proves that

$h^{0}(\mathcal{O}_{X}(H-E_{3}))=h^{0}(\mathcal{O}_{X}(C+E_{1}+E_{2}))=2<4$

shows that $E_{3}$ is not a base component of $H$. By a symmetric argument, the same is true for $E_{1},E_{2}$. Since all the base locus of $H$ must be contained in the curve $C+E_{1}+E_{2}+E_{3}$, this proves that $H$ has no base points or base components. The equality $HE_{i}=1$ proves that the image of each $E_{i}$ under the map $f_{|H|}:X\to\mathbb{P}^{3}$ is a line.
Finally, the long exact sequence induced by

$0\to\mathcal{O}_{X}(E_{3})\to\mathcal{O}_{X}(C+E_{3})\to\mathcal{O}_{C}(C+E_{3})\to 0$

proves that $h^{0}(\mathcal{O}_{X}(C+E_{3}))=1$. But this is the same to say $H^{0}(\mathcal{O}_{X}(H-E_{1}-E_{2}))=1$, so there exists a unique plane containing the images of both $E_{1},E_{2}$, which means that these are different lines. $\square$

The next step is to consider the following definition:

###### Definition 80

We denote by $\mathbb{P}^{8}=|\mathcal{O}_{\mathbb{P}^{1}}(8)|$ the set of all effective divisors of degree $8$ on $\mathbb{P}^{1}$. Inside $\mathbb{P}^{8}$ let $\mathcal{V}^{\circ}$ the set of all divisors of the form $2p_{1}+2p_{2}+2p_{3}+p_{4}+p_{5}$, with $p_{i}$ distinct points, and let $\mathcal{V}$ be its closure.
Similarly, let $\mathcal{W}^{\circ}$ be the locus of all divisors of the form $2p_{1}+2p_{2}+2p_{3}+2p_{4}$, with $p_{i}$ distinct points, and let $\mathcal{W}$ be its closure.

###### Proposition 81

Both $\mathcal{V},\mathcal{W}\subset\mathbb{P}^{8}$ are irreducible, and $\mathcal{W}\subset\mathcal{V}$. Moreover $\mathcal{V}^{\circ}$ is an open subset inside $\mathcal{V}$.

Proof: Let denote by $\mathbb{P}^{2}:=|\mathcal{O}_{\mathbb{P}^{1}}(2)|,\mathbb{P}^{3}:=|\mathcal{O}_{\mathbb{P}^{1}}(3)|$, and consider the map $\tau:\mathbb{P}^{2}\times\mathbb{P}^{3}\to\mathbb{P}^{8}$,

$\tau(F,G):=FG^{2}$

Let $\overline{\Delta}_{2}\subset\mathbb{P}^{2}$ be the locus of polynomials which are squares of a linear polynomial, $\overline{\Delta}_{3}\subset\mathbb{P}^{3}$ be the locus of polynomials with a double root, and $R\subset\mathbb{P}^{2}\times\mathbb{P}^{3}$ the resultant locus of pairs of polynomials $(F,G)$ with at least a common root. Set

$\Delta_{2}:=\overline{\Delta}_{2}\times\mathbb{P}^{3}\subset\mathbb{P}^{2}\times\mathbb{P}^{3},$
$\Delta_{3}:=\mathbb{P}^{2}\times\overline{\Delta}_{3}\subset\mathbb{P}^{2}\times\mathbb{P}^{3},$

so that

$\mathcal{V}^{\circ}=\tau(\mathbb{P}^{2}\times\mathbb{P}^{3}\setminus\Delta_{2}\setminus\Delta_{3}\setminus R).$

This proves that $\mathcal{V}^{\circ}$ (and thus $\mathcal{V}$) is irreducible, and also that

$\tau^{-1}(\mathcal{V})=\mathbb{P}^{2}\times\mathbb{P}^{3},$

that is

$\mathcal{V}=\tau(\mathbb{P}^{2}\times\mathbb{P}^{3}).$

It follows then that

$\mathcal{V}^{\circ}=\mathcal{V}\setminus\tau(\Delta_{2})\setminus\tau(\Delta_{3})\setminus\tau(R)$

is open inside $\mathcal{V}$.
Finally, the equality

$\mathcal{W}^{\circ}=\tau(\Delta_{2}\setminus\Delta_{3}\setminus R)$

proves the irreducibility of $\mathcal{W}^{\circ}$ (and consequently of $\mathcal{W}$), and also that $\mathcal{W}^{\circ}\subset\mathcal{V}$. $\square$

The previous proposition has the following Corollary:

###### Corollary 82

There exist infinitely many pairs $(Q,C)$ where $Q\subset\mathbb{P}^{2}$ is a smooth quartic, and $C\subset\mathbb{P}^{2}$ is a smooth conic, whose intersection takes the form $Q\cap C=2q_{1}+2q_{2}+2q_{3}+q_{4}+q_{5}$, with $q_{i}$ pairwise distinct points.

Proof: Let $Q\subset\mathbb{P}^{2}$ be any ausiliary smooth quartic curve, and let $C\subset\mathbb{P}^{2}$ be any of the smooth conics given by Example 77. Look at the short exact sequence

$0\to\mathcal{O}_{\mathbb{P}^{2}}(2)\to\mathcal{O}_{\mathbb{P}^{2}}(4)\to\mathcal{O}_{C}(4)\to 0$

It induces an exact sequence

$0\to H^{0}(\mathcal{O}_{\mathbb{P}^{2}}(2))\to H^{0}(\mathcal{O}_{\mathbb{P}^{2}}(4))\to H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(8))\to 0.$

Let $\rho:H^{0}(\mathcal{O}_{\mathbb{P}^{2}}(4))\to H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(8))$ be the restriction map, and look at its projectification $\rho:\mathbb{P}^{14}\setminus\mathbb{P}^{5}\to\mathbb{P}^{8}$, which is an $\mathbb{A}^{6}$-bundle. Let $U^{sm}\subset\mathbb{P}^{14}$ be the open subset corresponding to smooth plane quartics. $U\subset\mathbb{P}^{14}\setminus\mathbb{P}^{5}$, since all quartics containing $C$ are clearly singular. Now let $\mathcal{W}\subset\mathcal{V}\subset\mathbb{P}^{8}$ be the loci defined previously. We denote by $[Q]\in\mathbb{P}^{14}$ the point corresponding to the quartic $Q$. Its restriction to $C$ has the form $2(p_{1}+p_{2}+p_{3}+p_{4})$, hence it belongs to $\rho^{-1}(\mathcal{W})$, and consequently to $\rho^{-1}(\mathcal{V})$ by Proposition 81. Since $Q$ is smooth, this proves that $U^{sm}\cap\rho^{-1}(\mathcal{V})$ is nonempty. Using again Proposition 81, we have that $\mathcal{V}^{\circ}$ is open inside $\mathcal{V}$, and hence $\rho^{-1}(\mathcal{V}^{\circ})$ is open inside

in $\rho^{-1}(\mathcal{V})$. Since $\rho$ is an $\mathbb{A}^{6}$-bundle, the space $\rho^{-1}(\mathcal{V})$ is irreducible, and hence the intersection $(U^{sm}\cap\rho^{-1}(\mathcal{V}))\cap\rho^{-1}(\mathcal{V}^{\circ})$ is nonempty. Any quartic in this intersection is smooth and it restricts to a divisor of the required form. $\square$

Now we are finally able to show that, without the assumption of unnodality for a Coble surface $X$, Remark 75 and Corollary 76 can be false.

###### Example 83

By Corollary 82, we can pick a smooth quartic $Q\subset\mathbb{P}^{2}$ and a smooth conic $C\subset\mathbb{P}^{2}$ with $Q\cap C=2q_{1}+2q_{2}+2q_{3}+q_{4}+q_{5}$, where the $q_{i}$’s are pairwise distinct points. Let

$q:Y\to\mathbb{P}^{2}$

be the double cover branched over $Q$. The surface $Y$ is a Del Pezzo surface of degree $2$, equipped with the deck involution $i_{Y}:Y\to Y$, which is a Geiser involution. Its canonical divisor is

$K_{Y}=q^{*}(-L),$

where $L$ is any line in the plane. Let $\tilde{C}\subset Y$ be the preimage of $C$. Since $q_{4}\neq q_{5}$, the curve $\tilde{C}$ is irreducible, and it belongs to the linear system

$\tilde{C}\in|q^{*}(2L)|=|-2K_{Y}|.$

Its algebraic genus equals

$p_{a}(\tilde{C})=1+\frac{1}{2}(\tilde{C}^{2}+\tilde{C}K_{Y})=1+K_{Y}^{2}=3.$

However, $\tilde{C}$ has three double points $p_{1},p_{2},p_{3}$, with $q(p_{i})=q_{i}$, so $\tilde{C}$ has geometric genus $0$. Let $X\to Y$ be the blow up of these $3$ points, with exceptional divisors $E_{1},E_{2},E_{3}$. Let $C\subset X$ be the strict transform of $\tilde{C}$. Then $C$ is smooth, and its class in $\mathrm{Pic(X)}=\mathrm{Pic(Y)}\oplus\mathbb{Z}\mathrm{E}_{1}\oplus\mathbb{Z}\mathrm{E}_{2}\oplus\mathbb{Z}\mathrm{E}_{3}$ equals $C=\tilde{C}-2E_{1}-2E_{2}-2E_{3}=-2(K_{Y}+E_{1}+E_{2}+E_{3})=-2K_{X}$. This shows that $X$ is a Coble surface, equipped with an involution $i_{X}:X\to X$, which is well - defined since the points $p_{i}$ are fixed by $i_{Y}$. The equivariant morphism $(X,i_{X})\to(Y,i_{Y})$ contradicts Corollary 76, and since $p_{i}$ are non - isolated fixed points for $i_{Y}$, the action of $i_{X}$ on $E_{1},E_{2},E_{3}$ is different from the identity, which contradicts Remark 75. Nonetheless, we know from Proposition 5.1 that the linear system $H=C+E_{1}+E_{2}+E_{3}$ induces a well - defined morphism $f_{|H|}:X\to\mathbb{P}^{3}$. The problem is that we are not able to state that the projective involution $I:\mathbb{P}^{3}\to\mathbb{P}^{3}$ induced by $i_{X}$ acts as the identity on one of the three image lines $L_{i}=f_{|H|}(E_{i})$, since they are concurrent at a

point. Indeed, let $\tilde{R}\subset Y$ be the ramification curve for $q$, and let $R\subset X$ be its strict transform. We claim that $\tilde{C},\tilde{R}$ are equivalent in $\mathrm{Pic}(Y)$. Indeed, we already know that

$\tilde{C}=q^{*}(2L),$

and we have

$2\tilde{R}=q^{*}(Q)=q^{*}(4L).$

The rationality of $Y$ allows us to simplify and get

$\tilde{R}\simeq q^{*}(2L)\simeq\tilde{C}.$

But then in $\mathrm{Pic}(X)$ we have

$H=C+E_{1}+E_{2}+E_{3}=$
$=(\tilde{C}-2E_{1}-2E_{2}-2E_{3})+E_{1}+E_{2}+E_{3}=$
$=\tilde{C}-E_{1}-E_{2}-E_{3}=\tilde{R}-E_{1}-E_{2}-E_{3}=R.$

This shows that the curve $R$ is a member of $|H|$, hence there exists exactly one hyperplane $\Pi_{0}\subset\mathbb{P}^{3}$ containing the image $f_{|H|}(R)$. Since $i_{X}$ fixes $R$, the projective involution $I$ fixes $\Pi_{0}$. Then the fixed locus of $I$ has the shape $\mathrm{Fix}(I)=\Pi_{0}\cup\mathrm{p}_{0}$, where $\mathrm{p}_{0}$ is an isolated fixed point. But each $E_{1},E_{2},E_{3}$ contains isolated fixed points $x_{1},x_{2},x_{3}$ with respect to $i_{X}$, as they correspond to the $(-1)$-eigenvectors under the action of $i_{Y}$ in the tangent planes of $Y$ at $p_{1},p_{2},p_{3}$ respectively. Since $I\circ f_{|H|}=f_{|H|}\circ i_{X}$, this implies that $f_{|H|}(x_{1})=f_{|H|}(x_{2})=f_{|H|}(x_{3})=p_{0}$, and thus $L_{1},L_{2},L_{3}$ are all concurrent at $p_{0}$.
The reason for this failure is that $X$ contains $(-2)$-curves. Indeed, look at the tangent lines $\overline{L}_{i}\subset\mathbb{P}^{2}$ at $Q$ at $p_{i}$ for $i=1,2,3$. The pull - back $q^{*}(\overline{L}_{i})$ is a singular curve with algebraic genus $1$, and it has a double point at $p_{i}$ and self - intersection $q^{*}(\overline{L}_{i})^{2}=2$. Hence the strict transforms are smooth rational curves in $X$, and their class is $q^{*}(\overline{L}_{i})-2E_{i}$, so the self - intersection equals $(q^{*}(\overline{L}_{i})-2E_{i})^{2}=2-4=-2$.

In the following part, we will use repeatedly the following fact:

###### Remark 84

Assume we have a birational morphism $p:X\to Y$, where $X$ is an unnodal Coble surface with irreducible anti - bicanonical curve $C\in|-2K_{X}|$, and $Y$ is a smooth rational surface. Then the curve $p(C)$ can have only nodes or cusps as singularities. Indeed, let $H\in\mathrm{Pic}(Y)$ be the class of a big divisor. Since $p$ is birational, the pull - back $p^{*}H$ is still big on $X$, and it satisfies

$E(p^{*}H)=0$

for any irreducible curve  $E$  contracted by  $p$ . By Hodge Index Theorem 4 we find

$E^2 &lt; 0$

so we can apply Proposition 33 to deduce

$E^2\in \{-1, - 2, - 4\} .$

But  $X$  has no  $(-2)$ -curves, and the unique  $(-4)$ -curve is  $C$  itself, and hence

$E^2 = -1$

Thus all the curves contracted by  $p$  are  $(-1)$ -curves, and each of these intersects  $C$  with multiplicity 2. If the two intersection points are distinct we find a node for  $p(C)$ , if they coincide we get an ordinary cusp.

Now we eliminate case  $iv$ ) of Lemma 70.

Proposition 85 Assume  $X$  is a Coble surface with irreducible anti-bi-canonical divisor  $C \in | - 2K_X|$ . Then it is impossible to build an involution  $i: X \to X$  together with a regular birational morphism  $p: X \to \mathbb{P}^1 \times \mathbb{P}^1$  which makes the following diagram commute:

![img-5.jpeg](img-5.jpeg)

Proof: Since  $p$  is birational, the image curve  $C' := p(C)$  belongs to

$C^{\prime}\in | - 2K_{\mathbb{P}^{1}\times \mathbb{P}^{1}}| = |\mathcal{O}_{\mathbb{P}^{1}\times \mathbb{P}^{1}}(4,4)|$

Since  $C$  is irreducible, also  $C'$  is irreducible of arithmetic genus 9, and it must be preserved by the involution which switches the two factors. Moreover, its singularities can be only nodes or cusps, by Remark 84. Each node or cusp makes the geometric genus drop by 1, hence their total number must be equal to 9. Thus the singularities of  $C'$  are divided in  $s$  pairs outside of the diagonal  $\Delta$ , plus  $t$  singular points along  $\Delta$ , with  $2s + t = 9$ . Let  $q: \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^2$  be the quotient map, defined by the subsystem of symmetric sections of  $\mathcal{O}_{\mathbb{P}^1 \times \mathbb{P}^1}(1,1)$ . The branch locus of  $q$  is a smooth plane conic  $B \subset \mathbb{P}^2$ . By degree reasons,

$\deg \mathrm{q}(\mathrm{C}^{\prime}) = 4$

Each pair of singular points of  $C'$  outside  $\Delta$  corresponds to a singularity of  $q(C')$ , while a singularity in  $\Delta$  corresponds to a tangency point between  $B$

and $q(C^{\prime})$. Since $q(C^{\prime})$ has degree 4, it can have at most 3 ordinary double points and 4 tangency points with the conic $B$, so

$s\leq 3\quad\text{and}\quad t\leq 4$

This forces

$s=t=3$

The three singularities of $C^{\prime}$ along $\Delta$ correspond to three disjoint exceptional divisors in $X$, each of them preserved by $i$, a contradiction with Remark 75. $\square$

Again, the hypothesis of irreducibility of the Coble curve $C$ is crucial, as the following example shows:

###### Example 86

Let $F_{1}+F_{2}+F_{3}+F_{4}\in|\mathcal{O}_{\mathbb{P}^{1}\times\mathbb{P}^{1}}(4,0)|$ be the union of $4$ lines in one ruling, and let $G_{1}+G_{2}+G_{3}+G_{4}$ in $|\mathcal{O}_{\mathbb{P}^{1}\times\mathbb{P}^{1}}(0,4)|$ be their images in the other ruling under the involution $(p,q)\to(q,p)$. The divisor $\sum_{i}F_{i}+\sum_{i}G_{i}$ lives in the anti - bicanonical class $|-2K_{\mathbb{P}^{1}\times\mathbb{P}^{1}}|=|\mathcal{O}_{\mathbb{P}^{1}\times\mathbb{P}^{1}}(4,4)|$, and it is invariant under the involution. The blow up of its $16$ nodes produces a Coble surface with $8$ boundary components, equipped with a biregular involution with $\mathbb{P}^{1}\times\mathbb{P}^{1}$ as minimal model.

Next step is to show that case $ii)$ of Lemma 70 is impossible, still preserving the assumption that the Coble curve is irreducible.

###### Proposition 87

If $X$ is an unnodal Coble surface with irreducible Coble curve $C\in|-2K_{X}|$, and $i:X\to X$ is an involution, then the pair $(X,i)$ does not admit a minimal model as in case $ii)$ of Lemma 70.

Proof: Assume the countrary: then we find an equivariant morphism

$p:X\to Y$

with $Y$ a smooth rational surface equipped with an involution

$i_{Y}:Y\to Y$

such that

$p\circ i=i_{Y}\circ p$

Moreover, $Y$ admits a conic fibration $\pi_{Y}:Y\to\mathbb{P}^{1}$, whose fibers are all preserved by $i_{Y}$. such an involution $i_{Y}$ arises as the deck involution of a double cover $q:Y\to\mathbb{F}_{n}$ on a Hirzebruch surface $\mathbb{F}_{n}$, branched over a smooth bisection $B\subset\mathbb{F}_{n}$. The singular fibers of $\pi_{Y}:Y\to\mathbb{P}^{1}$ correspond

to the ramification locus of the restriction  $B \to \mathbb{P}^1$ . Putting all together, we have a diagram:

![img-6.jpeg](img-6.jpeg)

We first want to exclude the case  $n &gt; 0$ . Assume this actually happens, and consider the negative section  $C_{-n} \subset \mathbb{F}_n$ . If the pullback  $q^{*}(C_{-n}) \subset Y$  is irreducible, then it is a curve of self intersection

$$
q ^ {*} (C _ {- n}) ^ {2} = - 2 n \leq - 2
$$

By Proposition 33 and the unnodality assumption, the strict transform of  $q^{*}(C_{-n})$  in  $X$  must necessarily coincide with a component of the Coble curve  $C$ . Since  $C$  is irreducible, we have

$$
p (C) = q ^ {*} (C _ {- n})
$$

But by definition,  $Y$  is obtained by  $X$  as a blow - down of  $i$ -equivariant  $(-1)$ -curves. Each  $(-1)$ -curve of  $X$  intersects  $C$  in two points, hence its contraction makes the self-intersection of  $C$  jump by 4, that is,

$$
p (C) ^ {2} \geq C ^ {2} + 4 = 0,
$$

which is a contradiction.

Another contradiction arises if we assume that  $q^{*}(C_{-n})$  actually splits as

$$
q ^ {*} (C _ {- n}) = A + B
$$

with  $A, B$  curves switched by  $i_{Y}$ . In this case, we find the same self-intersection

$$
- 2 n = q ^ {*} (C _ {- n}) ^ {2} = A ^ {2} + B ^ {2} + 2 A B = 2 A ^ {2} + 2 A B
$$

This shows that  $A, B$  are two distinct curves with negative self-intersection, hence

$$
A ^ {2} = B ^ {2} = - 1
$$

by Proposition 33. So the previous equality becomes

$$
- 2 n = 2 A B - 2
$$

which is possible only if $AB=0$ and $n=1$. This again is a contradiction, since $i_{Y}$ should exchange two disjoint $(-1)$-curves, against the hypothesis of minimality.
The last case to exclude is that $C_{-n}$ might be a component of the branch locus $B\subset{\mathbb{F}}_{n}$ of $q$. Since $B$ is a bisection of ${\mathbb{F}}_{n}$, the other component $B-C_{-n}$ must be another section, disjoint from $C_{-n}$ (otherwise $Y$ would be a singular surface). The only curves with this property live in the linear system $C_{-n}+nF$, where $F$ is a fiber of the ${\mathbb{P}}^{1}$-bundle $|F|:{\mathbb{F}}_{n}\to{\mathbb{P}}^{1}$. Thus we find

$B=2C_{-n}+nF,$

which forces $n$ to be even. Let $R\subset Y$ be the ramification component corresponding to $C_{-n}$, so that

$q^{*}(C_{-n})=2R.$

Taking squares, we have

$-2n=4R^{2},$

that is

$R^{2}=-\frac{n}{2}$

Now we can argue as before: if $n\geq 4$, then $R^{2}\leq-2$ and we still find $R=p(C)$, which is a contradiction, since $p(C)^{2}\geq 0$. But if $n=2$, we still have a contradiction, since $R^{2}=-\frac{n}{2}=-1$ would give a $(-1)$-curve fixed by $i_{Y}$, against the assumption of minimality.
Finally, we have proved that $n=0$, that is

${\mathbb{F}}_{n}={\mathbb{F}}_{0}={\mathbb{P}}^{1}\times{\mathbb{P}}^{1}.$

To avoid confusion, we denote by $F_{1}\in{\rm Pic}({\mathbb{P}}^{1}\times{\mathbb{P}}^{1})$ the ruling induced from $Y$, so that $q^{*}(F_{1})$ is the conic bundle on $Y$ given by Lemma 70. Let $F_{2}$ be the other ruling. In this notation, the branch curve $B$ of $q$ lives in the linear system

$B\in|aF_{1}+2F_{2}|$ (20)

for some even number $a\geq 0$.
If $a=0$ then $B$ is the disjoint union of two horizontal lines in $F_{2}$. This means that $Y={\mathbb{P}}^{1}\times{\mathbb{P}}^{1}$ too, with the involution $i_{Y}:{\mathbb{P}}^{1}\times{\mathbb{P}}^{1}\to{\mathbb{P}}^{1}\times{\mathbb{P}}^{1}$ acting as the identity on the first component. In a suitable choice of coordinates $([X_{0},X_{1}],[Y_{0},Y_{1}])$ on $Y$, we have

$i_{Y}([X_{0},X_{1}],[Y_{0},Y_{1}])=([X_{0},X_{1}],[Y_{0},-Y_{1}])$

$q([X_{0},X_{1}],[Y_{0},Y_{1}])=([X_{0},X_{1}],[Y_{0}^{2},Y_{1}^{2}])$ (21)

Since $p:X\to Y$ is birational, the image $p(C)=p(-2K_{X})$ must live in the linear system

$p(C)\in|-2K_{\mathbb{P}^{1}\times\mathbb{P}^{1}}|=|\mathcal{O}_{\mathbb{P}^{1}\times\mathbb{P}^{1}}(4,4)|$

An irreducible member of this system has algebraic genus 9, as it is confirmed by the difference

$K_{Y}^{2}-K_{X}^{2}=9$

Hence $Y$ comes from the contraction via $p$ of 9 $(-1)$-curves of $X$ over 9 nodes of $p(C)$, and these points must be set - theoretically preserved by $i_{Y}$. Denote by $s$ the number of pairs of nodes which are switched by $i_{Y}$, and by $t$ the number of nodes fixed by $i_{Y}$, with

$2s+t=9$

By Remark 75, we must have $t<3$, so that $s=4$ and $t=1$ is the only possible solution. Now let:

$D:=q(p(C))\subset\mathbb{P}^{1}\times\mathbb{P}^{1}$

be the set - theoretic image of $p(C)$ in the final $\mathbb{P}^{1}\times\mathbb{P}^{1}$, with the reduced scheme structure. Since $q:p(C)\to D$ has degree 2, as divisors we have

$q_{*}(p_{*}(C))=2D$

But the expression 21 shows that the induced push - forward $q_{*}$ acts as $F_{1}\to 2F_{1},F_{2}\to F_{2}$, so that

$2D=q_{*}(p(C))=q_{*}(4F_{1}+4F_{2})=8F_{1}+4F_{2}$

and hence

$D\in|4F_{1}+2F_{2}|$

The unique fixed node of $p(C)$ corresponds to a tangency point between $D$ and the branch locus $B$, while the 4 pairs correspond to 4 actual nodes of $D$. But an irreducible curve $D\in|4F_{1}+2F_{2}|$ has algebraic genus 3, hence it cannot admit 4 nodes.
We now show that the number $a$ in 20 can only assume the values 2 or 4. Indeed, consider the pencil $F_{2}$ and the pull-back $q^{*}(F_{2})$ on $Y$. It is a pencil of

hyperelliptic curves, which cover $2:1$ the lines in $|F_{2}|$ with $a$ branch points, so they have arithmetic genus

$p_{a}(q^{*}(F_{2}))=\frac{a-2}{2}$

 $|-2K_{Y}|$ is effective, since it contains the curve $p(C)$, so the product

$q^{*}(F_{2})(-2K_{Y})\geq 0$

must be non - negative. Putting this inside adjunction formula, we have

$2p_{a}(q^{*}(F_{2}))-2=q^{*}(F_{2})^{2}+q^{*}(F_{2})K_{Y}\leq 0$

This leaves only $p_{a}(q^{*}(F_{2}))=0,1$ as possibilities, and they correspond respectively to $a=2,4$.
If $a=2$, then $q:Y\to\mathbb{P}^{1}\times\mathbb{P}^{1}$ is branched over a curve of type $B\in|2F_{1}+2F_{2}|$, and we can compute $K_{Y}$ as

$K_{Y}=q^{*}(K_{\mathbb{P}^{1}\times\mathbb{P}^{1}})+\frac{1}{2}q^{*}(B)=q^{*}(-F_{1}-F_{2})$

Note that

$K_{Y}^{2}=4$

so $Y$ is obtained from $X$ via the contraction of $K_{Y}^{2}-K_{X}^{2}=5$ equivariant $(-1)$-curves, which correspond to $5$ nodes of $p(C)$. As before, assume that $s$ pairs are switched by $i_{Y}$, while $t$ nodes are fixed, with $2s+t=5$. Since there are not isolated fixed points in $Y$, Proposition 75 gives again $t<3$, that is

$s=2,\ t=1$

necessarily. Again, this means that $q(p(C))$ has $2$ nodes. As divisors, we have $q_{*}(p_{*}(C))=2D$ for some effective irreducible divisor $D\subset\mathbb{P}^{1}\times\mathbb{P}^{1}$, and

$q^{*}(D)=p(C)=-2K_{Y}=q^{*}(2F_{1}+2F_{2})$

so that

$D\in|2F_{1}+2F_{2}|$

But an irreducible curve in this linear system has algebraic genus $1$, so it can have at most one node, contradicting $s=2$.
There is only one case left, that is the number $a$ in 20 equals $4$, so that $B=4F_{1}+2F_{2}$. Again, we compute can compute $K_{Y}$ as

$K_{Y}=q^{*}(K_{\mathbb{P}^{1}\times\mathbb{P}^{1}})+\frac{1}{2}q^{*}(B)=q^{*}(-F_{2})$

Hence the canonical has square

$K_{Y}^{2}=0$

and hence $Y$ is obtained from $X$ via the contraction of only $K_{Y}^{2}-K_{X}^{2}=1$ $(-1)$-curve $E$ to a point $p\in Y$. But $F_{2}$ can move in $\mathbb{P}^{1}\times\mathbb{P}^{1}$, and hence $|-K_{Y}|=|q^{*}(F_{2})|$ can move in $Y$. But then one member of $-K_{Y}$ passes through $p$, which means that $|-p^{*}K_{Y}-E|$ is non empty. This contradicts the very Coble assumption $|-K_{X}|=\emptyset$. $\square$

###### Proposition 88

For an unnodal Coble surface, with irreducible boundary $\{C\}=|-2K_{X}|$, cases i) and iii) of Theorem 70 cannot happen.

Proof: Assume that we are in case $i)$ of Theorem 70: then there exists a commutative diagram:

where $\mathbb{F}_{n}$ is a Hirzebruch surface, with its $\mathbb{P}^{1}$-bundle $f:\mathbb{F}_{n}\to\mathbb{P}^{1}$, $p$ is an equivariant morphism, and $\tau$ is a nontrivial involution on $\mathbb{P}^{1}$.

Again, we start excluding the case $n>0$: $n=1$ is impossible, since $(\mathbb{F}_{1},i^{\prime})$ is not a minimal pair. Hence $n\geq 2$, but then the negative curve $C_{-n}\subset\mathbb{F}_{n}$ has a strict transform in $X$ with self intersection lesser or equal than $-2$. Again, by Proposition 33, this strict tranform must coincide with the anti - bicanonical curve $C$, so that $p(C)=C_{-n}$. But this is impossible, since $p:X\to\mathbb{F}_{n}$ contracts $(-1)$-curves, and hence $C_{-n}$ should be singular, which is false.

This gives $n=0$, so we have

$i^{\prime}:\mathbb{P}^{1}\times\mathbb{P}^{1}\to\mathbb{P}^{1}\times\mathbb{P}^{1}$

By Theorem 70, the involution $i^{\prime}$ preserves the linear system given by the first ruling $|F_{1}|$, and it acts on it as the involution $\tau$ of the previous diagram. But then $i^{\prime}$ must preserve also the second ruling $|F_{2}|$, so let denote by $\sigma$ the action of $i^{\prime}:\mathbb{P}^{1}\to\mathbb{P}^{1}$ on the second coordinate of the product. We already

saw during the proof of 87 how to deal with the case $\sigma = \mathbb{1}_{\mathbb{P}^1}$, so we can assume $\sigma \neq \mathbb{1}_{\mathbb{P}^1}$. In a suitable choice of coordinates, we can write

$$
i'([X_0, X_1], [Y_0, Y_1]) = ([X_0, -X_1], [Y_0, -Y_1]) \tag{22}
$$

It has four fixed points, namely $([1,0],[1,0]),([1,0],[0,1]),([0,1],[1,0]),([0,1],[0,1])$. Moreover, since $p$ is birational, the image $p(C)$ is an irreducible member of the linear system

$$
p(C) \in |\mathcal{O}_{\mathbb{P}^1 \times \mathbb{P}^1}(4, 4)| \tag{23}
$$

and hence it must have 9 nodes. This set of nodes is preserved by $i'$, hence at least one of them must coincide with one of the four fixed points. Assume for example that this node is $p = ([1,0],[1,0])$. Then the map $p: X \to \mathbb{P}^1 \times \mathbb{P}^1$ factors through the blow-up $X \to Bl_p(\mathbb{P}^1 \times \mathbb{P}^1) \to \mathbb{P}^1 \times \mathbb{P}^1$. The involution induced by $i'$ on this blow-up acts trivially on the exceptional divisor over $p$, and it preserves both the strict transforms of the two fibers $\{X_1 = 0\}, \{Y_1 = 0\}$ containing $p$. Hence we can contract these $(-1)$-curves, and this produces another minimal model:

$$
\begin{array}{c c c}
X &amp; \xrightarrow{i} &amp; X \\
\downarrow &amp; &amp; \downarrow^p \\
\mathbb{P}^2 &amp; \xrightarrow{I} &amp; \mathbb{P}^2
\end{array}
$$

where $I$ is a projective involution. This is the unique left possibility, corresponding to case iii) of Theorem 70. In a suitable choice of coordinates, we can write

$$
I[X_0, X_1, X_2] = [-X_0, X_1, X_2]
$$

and the fixed locus is the disjoint union $\operatorname{Fix}(\mathrm{I}) = \{\mathrm{p}_0\} \cup \mathrm{L}_0$, where $p_0 = [1,0,0]$ and $L_0 = \{X_0 = 0\}$. There are three possibilities: $p_0$ could be a node of the 10-nodal sextic $\overline{C} := p(C) \subset \mathbb{P}^2$, or a smooth point of $\overline{C}$, or it could not lie in $\overline{C}$ at all.

In all these situations, it is impossible that all nodes are fixed by $I$, otherwise at least 9 of them (all but at most $p_0$) should lie on $L_0$. This would provide an intersection product $\overline{C}L_0 = 18$, which is way too large. Hence there exists at least one pair of nodes $p, q \in \operatorname{Sing}(\overline{C})$ switched by $I$. As before, the map $p: X \to \mathbb{P}^2$ factors through the blow-up $X \to Bl_{p,q}\mathbb{P}^2 \to \mathbb{P}^2$. This blow up is equipped with a well-defined involution, induced by $I$, which preserves the $(-1)$-curve consisting on the strict transform of the line $\overline{p,q}$. The contraction of this curve leads us to a minimal model of $(X,i)$ consisting of $\mathbb{P}^1 \times \mathbb{P}^1$, equipped with the involution which exchanges the two factors.

86

This is forbidden by Proposition 85. $\square$

This concludes the proof of Theorem 72.

###### Example 89

Again, we the irreducibility hypothesis for the curve $C$ cannot be dropped. Indeed, consider a plane cubic $\overline{C}_{3}$ whose components are all rational, and whose singularities are all double points: the curve $\overline{C}_{3}$ could be the union of three non - concurrent lines, or a line and a smooth conic, or an irreducible cubic with a node, or a cusp. Pick a point $p_{0}\in\mathbb{P}^{2}$ outside $\overline{C}_{3}$, and a line $L_{0}$ not containing $p_{0}$ nor any of the singular points of $\overline{C}_{3}$, and not tangent to any of its components. If $\overline{C}_{3}$ splits as a smooth conic $C_{2}$ plus a line, assume also that $L_{0}$ is not the polar to $C_{2}$ with center $p_{0}$. Let $I:\mathbb{P}^{2}\to\mathbb{P}^{2}$ be the involution with fixed locus $p_{0}\cup L_{0}$, and let $X$ be the blow up of all the singularities of the reducible sextic $C_{3}+\overline{C}_{3}$. Then $X$ is a Coble surface, equipped with a non - minimal involution induced by a projective one, with $2,4$ or $6$ boundary components.

Note also that the expressions 22 and 23 closely remember the construction of Horikawa models for Enriques surfaces in *[1]*. The difference is that the construction in the cited article starts with an $i^{\prime}$ invariant divisor of type $|\mathcal{O}_{\mathbb{P}^{1}\times\mathbb{P}^{1}}(4,4)|$ which in general needs not to be irreducible or rational, differently from our case. Moreover, the construction in *[1]* needs this divisor to not contain any of the $4$ fixed points, which is something we could not avoid in our proof.

### 5.2 Families of Coble surfaces

The goal of this section is to construct a suitable space to parametrize triples $(X,H,E)$, where $X$ is a Coble surface, $H\in\mathrm{Pic(X)}$ is a polarization, and $E\subset X$ is a $(-1)$-curve contracted by the morphism induced by $|H|$. We will proceed in the following way: let

$\mathbb{P}^{27}\simeq\mathbb{P}(H^{0}(\mathcal{O}_{\mathbb{P}^{2}}(6)))$

the space of plane curves of degree $6$. Consider the Severi variety $V\subset\mathbb{P}^{27}$ given by

$V:=\{[F]\operatorname{s.t.}V(F)\operatorname{is reduced, irreducible, with 10 nodes}\}\subset\mathbb{P}^{27}$

It is a locally closed subset of $\mathbb{P}^{27}$ of dimension $17$.
Now we need to specify a choice for a $(-1)$-curve. Take $\tilde{V}\subset V\times\mathbb{P}^{2}$,

$\tilde{V}:=\{(F,p)\operatorname{such that}p\in Sing(V(F))\}$

The variety $\tilde{V}$ is a $10:1$ cover of $V$, and up to restricting $V$, we can assume it is unramified. Now we take the trivial $\mathbb{P}^{2}$-bundle $\tilde{V}\times\mathbb{P}^{2}$, and the fibre product

$\tilde{V}\times_{V}\tilde{V}=\{(F,p,q)\operatorname{such}\operatorname{that}p,q\in Sing(V(F))\}$

lives inside $\tilde{V}\times\mathbb{P}^{2}$. The subspace $\tilde{V}\times_{V}\tilde{V}$ has codimension $2$ inside $\tilde{V}\times\mathbb{P}^{2}$, and it consists of a disjoint union of $10$ copies of $\tilde{V}$. $\tilde{V}\times_{V}\tilde{V}$ contains a distinguished component, namely the diagonal $\Delta_{\tilde{V}}$,

$\Delta_{\tilde{V}}=\{(F,p,p),p\in Sing(V(F))\}\subset\tilde{V}\times_{V}\tilde{V}$

Finally, we construct the universal Coble surface

$\mathcal{X}:=Bl_{\tilde{V}\times_{V}\tilde{V}}\tilde{V}\times\mathbb{P}^{2}$

Let $\overline{\mathcal{C}}\subset\tilde{V}\times\mathbb{P}^{2}$ the universal nodal sextic

$\overline{\mathcal{C}}:=\{((F,p),x)\operatorname{such}\operatorname{that}F(x)=0\}$

and let $\mathcal{C}\subset\mathcal{X}$ be its strict transform.
Let $\mathcal{E}\subset\mathcal{X}$ be the universal $(-1)$-curve, that is, the exceptional divisor associated to $\Delta_{\tilde{V}}$.
Let $\mathcal{H}\in\operatorname{Pic}(\mathcal{X})$ be the line bundle given by the pull-back of $\mathcal{O}_{\mathbb{P}^{2}}(1)$ via the composite map

$\mathcal{X}\to\tilde{V}\times\mathbb{P}^{2}\to\mathbb{P}^{2}$

For every $x=(F,p)\in\tilde{V}$, the fiber $\mathcal{X}_{x}$ is the Coble surface obtained by the blow up of the singularities of $F$. The Coble curve of $\mathcal{X}_{x}$ is just the normalization of $V(F)$, that is, the intersection $\mathcal{C}_{x}:=\mathcal{C}\cap\mathcal{X}_{x}$. The divisor $\mathcal{E}$ cuts in $\mathcal{X}_{x}$ the exceptional divisor associated to $p$, and the restriction $\mathcal{H}|_{\mathcal{X}_{x}}$ is a polarization on $\mathcal{X}_{x}$ which contracts $\mathcal{E}_{x}$.
Informally, we can think of this space as the set of quadruples $(X,C,E,H)$, where $(X,H)$ is a polarized Coble surface, with $C$ its Coble curve, and $E$ is one of the $10$ divisors contracted by $H$. Since $C$ is uniquely determined by the relation $|-2K_{X}|=\{C\}$, it can be omitted. Hence we will talk about triples $(X,E,H)$ with the properties we said above.
 we could achieve the same construction first by considering

$\mathcal{Y}:=Bl_{\tilde{V}}V\times\mathbb{P}^{2}$

to build the universal Coble surface over $V$, and then defining $\mathcal{X}=f^{*}\mathcal{Y}$ as the pull-back via the $10:1$ cover $f:\tilde{V}\to V$.

Definition 90 A rationally determined automorphism of Coble surfaces is an automorphism  $\mathcal{G}:\mathcal{Y}\to \mathcal{Y}$  which fits in a commutative diagram:

![img-7.jpeg](img-7.jpeg)

 $\mathcal{G}$ induces via pull-back an automorphism $f^{*}\mathcal{G}:\mathcal{X}\to \mathcal{X}$. The coincidence locus $\Gamma (\mathcal{G})$ of $\mathcal{G}$ is the set of pairs

$\Gamma (\mathcal{G}):= \{(X,E)\in \tilde{V}\mathrm{such~that}f^{*}\mathcal{G}|_{E\cap C} = \mathbb{1}\}$

Example 91 Let  $A, B, C \in H^0(\mathcal{O}_{\mathbb{P}^1}(2))$  three linearly independent forms of degree 2 in 2 homogeneous variables  $u, v$ . Assume that none of them is a square of a linear form, and no two of them have share a common root. Let

$$
\Lambda = (\lambda_ {i, j}) _ {i, j = 0} ^ {2}
$$

a generic  $3 \times 3$  invertible matrix with complex coefficients, and define

$$
G _ {0} := \lambda_ {0, 0} A + \lambda_ {0, 1} B + \lambda_ {0, 2} C
$$

$$
G _ {1} := \lambda_ {1, 0} A + \lambda_ {1, 1} B + \lambda_ {1, 2} C
$$

$$
G _ {2} := \lambda_ {2, 0} A + \lambda_ {2, 1} B + \lambda_ {2, 2} C
$$

Consider the three polynomials of degree 6:  $BCG_0, ACG_1, ABG_2$ . If the matrix  $\Lambda$  is generic, these polynomials are linearly independent, with no common roots, and they define a regular map

$$
\gamma : \mathbb {P} ^ {1} \to \mathbb {P} ^ {2}
$$

$$
\gamma (u, v) := \left[ B C G _ {0} (u, v), A C G _ {1} (u, v), A B G _ {2} (u, v) \right]
$$

which is birational over a rational plane sextic with 10 nodes. Its singularities are located at the points  $[1,0,0],[0,1,0],[0,0,1]$  and other seven points  $p_1,\ldots ,p_7$ . Consider the set of triples  $(X,E,H)$ , where:

i)  $X$  is the blow up of all the nodes;
ii)  $E\subset X$  is the strict transform of the line  $Z = 0$
iii)  $H \in \operatorname{Pic}(\mathrm{X})$  is the polarization defined by  $YZ, XZ, XY$ , that is the system of plane conics through  $[1,0,0], [0,1,0], [0,0,1]$ . Its exceptional curves are the divisors associated to  $p_1, \ldots, p_7$ , plus the transforms of the lines  $X = 0, Y = 0, Z = 0$ . In particular,  $E$  is one of them.

Consider the Bertini involution  $\mathcal{G}:X\to X$  with base points  $[0,0,1],p_1,\ldots ,p_7$

It is well defined for every $\Lambda$, so we are in the case described by Definition 90. Its restriction to the curve acts as the deck involution associated to the $g_{2}^{1}$ spanned by $A,B$. Hence its pair of fixed points is given by the zeroes of

$\frac{\partial A}{\partial u}\frac{\partial B}{\partial v}-\frac{\partial A}{\partial v}\frac{\partial B}{\partial u}=0$

Meanwhile, the intersection $E\cap C$ is given by $G_{2}=0$. Hence the coincidence loci of $\mathcal{G}$ is the set of matrices $\Lambda$ such that $G_{2},\frac{\partial A}{\partial u}\frac{\partial B}{\partial V}-\frac{\partial A}{\partial v}\frac{\partial B}{\partial u}$ are linearly independent in $H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(2))$. this is a $2$-codimensional condition over the set of all matrices $\Lambda$.

Thanks to Theorem 72, we are able to state that this is the general case:

###### Lemma 92

The coincidence loci of a rationally defined involution has codimension $2$ inside $\tilde{V}$.

##

6 Appendix

This Appendix contains some un - finished computations, which were made in attempt to classify involutions on unnodal Coble surfaces with irreducible Coble curve. These calculations were made before the proof of the Proposition 71 and Theorem 72 in Section 3. The idea was to take any involution $i:X\to X$ such that $i|_{C}=\mathbb{1}_{C}$, an exceptional curve $E\subset X$, and look at the behaviour of the linear system $E+i(E)$. However, none of the proof of Section 3 requires these computations, which until now remain suspended.
The previous lemma has a very nice consequence:

###### Corollary 93

Suppose $X$ is a Coble surface, $C\subset X$ the Coble curve, $i:X\to X$ an involution acting identically on $C$, and $E\subset X$ a rational normal curve of self intersection $-1$. Then $i(E)\neq E$.

Proof: Let $X^{\prime}$ be the surface obtained from $X$ via the blow-down of $E$ to a point $p\in X^{\prime}$. Then $X^{\prime}$ is still a smooth rational surface. If $i(E)=E$ the involution $i$ descends to an involution $i^{\prime}:X^{\prime}\to X^{\prime}$. Since $E$ is a $(-1)$-curve, we have

$EK_{X}=-1$

so

$EC=-2EK_{X}=2$

Thus the image of $C$ inside $X^{\prime}$ is fixed by $i^{\prime}$ but it has a node at $p$, which contradicts the previous Lemma. $\square$

In particular, the intersection product $Ei(E)$ is a non negative number. Moreover, since $i$ fixes the two intersection points in $E\cap C$, this intersection counts at least these two points. This leads to the next definition.

###### Definition 94

We will denote by $\overline{E}$ the curve

$\overline{E}:=i(E)$

and by $k\geq 0$ the natural number given by

$E\overline{E}=k+2$

In other words, $k$ is the number of non trivial intersection points between $E$ and $\overline{E}$.

Of course this number $k$ depends on the choice of the $(-1)$-curve $E$ and the involution $i$. We want to compute the dimension of the linear system $|E+\overline{E}|$.

We look at the normalization of the divisor $E+\overline{E}$, $\nu:E\sqcup\overline{E}\to E+\overline{E}$, where the symbol $\sqcup$ denotes the disjoint union. It defines a short exact sequence

$0\to\mathcal{O}_{E+\overline{E}}\xrightarrow{\nu^{*}}\mathcal{O}_{E\sqcup\overline{E}}=\mathcal{O}_{E}\oplus\mathcal{O}_{\overline{E}}\xrightarrow{(f,g)\to f|_{E\cap\overline{E}}-g|_{E\cap\overline{E}}}\mathcal{O}_{E\cap\overline{E}}\to 0$

Tensoring by $\mathcal{O}_{X}(E+\overline{E})$, and taking cohomology, we find

$0\to H^{0}(\mathcal{O}_{E+\overline{E}}(E+\overline{E}))\to H^{0}(\mathcal{O}_{E}(E+\overline{E}))\oplus H^{0}(\mathcal{O}_{\overline{E}}(E+\overline{E}))\to H^{0}(\mathcal{O}_{E\cap\overline{E}}(E+\overline{E}))\to\cdots$

###### Remark 95

The map

$ev:H^{0}(\mathcal{O}_{E}(E+\overline{E}))\oplus H^{0}(\mathcal{O}_{\overline{E}}(E+\overline{E}))\to H^{0}(\mathcal{O}_{E\cap\overline{E}}(E+\overline{E}))$
$(\sigma,\tau)\to\sigma|_{E\cap\overline{E}}-\tau|_{E\cap\overline{E}}$

is surjective.
Indeed, we have

$E(E+\overline{E})=\overline{E}(E+\overline{E})=k+1$

so the domain vector space can be thought as the direct sum of homogeneous polynomials in two variables of degree $k+1$ over $E,\overline{E}$ respectively. On the other hand, the codomain is a sum of $k+2$ copies of $\mathbb{C}$, one for each intersection point in $E\cap\overline{E}$.
The restriction of this evaluation map to each of the two summands is of course an isomorphism, because the only homogeneous polynomial of degree $k+1$ in two variables admitting $k+2$ zeroes is $0$. The surjectivity of $ev$ follows.

This fact has several consequences.

###### Corollary 96

We have $h^{0}(\mathcal{O}_{E+\overline{E}}(E+\overline{E}))=k+2$, and $h^{0}(\mathcal{O}_{X}(E+\overline{E}))=k+3$.

Proof: The first equality follows immediately from the short exact sequence

$0\to H^{0}(\mathcal{O}_{E+\overline{E}}(E+\overline{E}))\to H^{0}(\mathcal{O}_{E}(E+\overline{E}))\oplus H^{0}(\mathcal{O}_{\overline{E}}(E+\overline{E}))\to H^{0}(\mathcal{O}_{E\cap\overline{E}}(E+\overline{E}))\to 0$

For the second equality, we look at the standard short exact sequence:

$0\to\mathcal{O}_{X}\to\mathcal{O}_{X}(E+\overline{E})\to\mathcal{O}_{E+\overline{E}}(E+\overline{E})\to 0$

The first cohomology group $H^{1}(\mathcal{O}_{X})$ vanishes since $X$ is rational, so the previous sequence remains exact at levels of global sections:

$0\to H^{0}(\mathcal{O}_{X})\to H^{0}(\mathcal{O}_{X}(E+\overline{E}))\to H^{0}(\mathcal{O}_{E+\overline{E}}(E+\overline{E}))\to 0$

In particular,

$h^{0}(\mathcal{O}_{X}(E+\overline{E}))=k+3$

$\square$

##

Corollary 97

The linear system $\mathcal{O}_{X}(E+\overline{E})$ has not fixed components or base points.

Proof: The only possible fixed components of $\mathcal{O}_{X}(E+\overline{E})$ can be $E$ or $\overline{E}$. But if one of these two curves is a fixed component, then the other one must move in a net, which is forbidden by $E^{2}=\overline{E}^{2}=-1$.

For the fixed points, the argument is similar: a fixed point of $\mathcal{O}_{X}(E+\overline{E})$ must necessarily lie on the divisor $E+\overline{E}$. The restriction map $H^{0}(\mathcal{O}_{X}(E+\overline{E}))\to H^{0}(\mathcal{O}_{E+\overline{E}}(E+\overline{E}))$ is surjective by the previous corollary, so it suffices to show that $\mathcal{O}_{E+\overline{E}}(E+\overline{E})$ is base point - free.

Suppose $p\in E$, $\sigma\in H^{0}(\mathcal{O}_{E}(E+\overline{E}))$ such that $\sigma(p)\neq 0$. By the previous remark, there exist a unique section $\tau\in H^{0}(\mathcal{O}_{\overline{E}}(E+\overline{E}))$ which agrees with $\sigma$ in the intersection $E\cap\overline{E}$, so the couple $(\sigma,\tau)$ defines an element of $H^{0}(\mathcal{O}_{E+\overline{E}}(E+\overline{E}))$ which is nonzero at $p$. $\square$

###### Corollary 98

If $E\neq\overline{E}$, the linear system $|E+\overline{E}|$ defines a regular map $f:X\to\mathbb{P}^{k+2}$.

###### Definition 99

We denote by $Y:=f(X)\subset\mathbb{P}^{k+2}$ the image of $X$ under the regular function $f$.

The surface $Y$ satisfies

$(\deg{\rm f})(\deg{\rm Y})={\rm D}^{2}=2{\rm k}+2$

and, since it is non-degenerate,

$\deg{\rm Y}\geq{\rm k}+1$

which leaves only two possibilities:

Case 1: $f:X\to Y$ has degree two, and $Y\subset\mathbb{P}^{k+2}$ is a surface of minimal degree, or

Case 2: $f:X\to Y$ is a birational morphism, and $Y$ has degree $\deg{\rm Y}=2{\rm k}+2$.

###### Remark 100

We briefly underline the fact that, if $f:C\to\mathbb{P}^{1}$ is a double cover branched over a divisor $B=p+q+2r$, with $p,q,r$ distinct points in $\mathbb{P}^{1}$, then $C$ is a rational curve. Indeed, we can locally write

$C=\{(x,y)\in\mathbb{C}^{2}\text{ such}\mathop{\rm that}\nolimits y^{2}=x^{2}(x^{2}-1)\}$

for

nd $f$ corresponds to the projection on the $x$ axis. Then we can give the rational parametrization

$x=\frac{t^{2}+1}{t^{2}-1},\quad y=2t\frac{t^{2}+1}{(t^{2}-1)^{2}}$

More geometrically, the unique singularity of $C$ is a node $\overline{r}$, with $f(\overline{r})=r$. In the normalization $\tilde{C}\to C$ there are two points over $\overline{r}$, so the composite map $\tilde{C}\to C\to\mathbb{P}^{1}$ is ramified only over $p,q$.
This remains true even if $p=r$, so that the branch divisor $B$ in $\mathbb{P}^{1}$ has the shape $B=3p+q$. In this case, $C$ has locally the form

$C=\{(x,y)\in\mathbb{C}^{2}\text{ such}\mathop{\mathrm{that}}y^{2}=x^{3}(x-1)\}$

which has a cusp in the origin. Such a curve admits the rational parametrization

$x=\frac{t^{2}}{t^{2}-1},\quad y=\frac{t^{3}}{(t^{2}-1)^{2}}$

Again, the geometric interpretation is that the normalization $\tilde{C}$ of $C$ has only one points lying over the cusp of $C$, so the composite map $\tilde{C}\to C\to\mathbb{P}^{1}$ is ramified over the two points $p,q$ without multiplicity.

The previous theorem gives us a precious result:

###### Remark 101

Suppose $D$ is an irreducible curve contracted by the map $f:X\to\mathbb{P}^{k+2}$ induced by the linear system $|E+\overline{E}|$. Since $H:=E+\overline{E}$ is big and nef, and $HD=0$, Hodge Index Theorem *[23]* forces

$D^{2}<0$

Thus, by Proposition 33 we find

$D^{2}\in\{-1,-2\}$

If $D$ is a $(-1)$-curve contracted by $f$, then

$D^{2}=-1,HD=0$

Since $i$ is an isomorphism and $H$ is $i$-invariant, we also have

$i(D)^{2}=-1,Hi(D)=0$

So we can apply Hodge Index Theorem to the divisor $D+i(D)$ to deduce that

$(D+i(D))^{2}<0$

This translates to

$Di(D)<1$

a contradiction to Corollary 93. Thus $D^{2}=-1$ cannot happen.

##

Proposition 102 The case $k = 0$ is impossible.

Proof: For $k = 0$ the linear system induces a map $f: X \to \mathbb{P}^2$, with $f^* \mathcal{O}_{\mathbb{P}^2}(1) = E + \overline{E}$. The degree of $f$ can be computed by

$$
\deg f = (E + \overline{E})^2 = 2
$$

By construction

$$
i^*(E + \overline{E}) = E + \overline{E}
$$

hence there exists an projective involution $I$ of $\mathbb{P}^2$ which fits into a commutative diagram:

$$
\begin{array}{c}
X \xrightarrow{f} \mathbb{P}^2 \\
i \Big{\downarrow} \qquad \qquad \Big{\downarrow} I \\
X \xrightarrow{f} \mathbb{P}^2
\end{array}
$$

The involution $I$ acts trivially on the non-degenerate curve $f(C)$, so

$$
I = \mathbb{1}_{\mathbb{P}^2}
$$

So $i$ corresponds to the deck involution of the double cover $f$.

By a theorem of Stein, the map $f$ factors through a (possibly singular) surface $\overline{X}$ in two regular maps

$$
\tau : X \to \overline{X}, \quad \overline{f} : \overline{X} \to \mathbb{P}^2, \quad f = \overline{f} \circ \tau
$$

where $\tau$ is a birational map with connected fibers, while $\overline{f}$ is a finite map of degree $\deg \overline{\mathbf{f}} = \deg \mathbf{f} = 2$, branched over a curve $B \subset \mathbb{P}^2$.

It is easy to compute $\deg \mathrm{B}$: if $l \subset \mathbb{P}^2$ is a generic line, the restriction

$$
f : f^{-1}(l) \to l
$$

is a double cover from the smooth elliptic curve $f^{-1}(l) \in |E + \overline{E}|$ to the rational normal curve $l$. This forces $l$ to contain exactly 4 branch points, so that

$$
\deg \mathrm{B} = 4
$$

By hypothesis

$$
i|_C = \mathbb{1}_C
$$

so $\tau(C)$ is a component of the ramification locus of the double cover $\overline{f}$. Thus the restriction $f: C \to f(C)$ is a birational map, and

$$
\deg \mathrm{f}(C) = C(E + \overline{E}) = 4
$$

This forces

$f(C)=B$

by degree reasons.
Thus $B$ is a rational plane quartic curve, and hence $B$ must have singular points. But this forces also the branch locus $\tau(C)\subset\overline{X}$ to be singular. On the other hand, by remark 101, $\tau$ can only contract some $(-2)$-curves of $X$, which are disjoint from $C$, so $\tau(C)$ should be smooth, a contradiction. $\square$

So let us assume $k>0$, and suppose we are in Case 1 as above: the function $f:X\to\mathbb{P}^{k+2}$ is a map of degree $2$ over a surface $Y:=f(X)\subset\mathbb{P}^{k+2}$ of minimal degree $k+1$.

###### Remark 103

We remember the definition of Hirzebruch surfaces $\mathbb{F}_{n},n\geq 0$ as follows: we consider the rank $2$ vector bundle $\mathcal{E}$ over $\mathbb{P}^{1}$,

$\mathcal{E}:=\mathcal{O}_{\mathbb{P}^{1}}\oplus\mathcal{O}_{\mathbb{P}^{1}}(-n)$

and $\mathbb{F}_{n}:=\mathbb{P}(\mathcal{E})$. The surface $\mathbb{F}_{n}$ has a $\mathbb{P}^{1}$-fibration

$\pi:\mathbb{F}_{n}\to\mathbb{P}^{1}$

For $n>0$, this fibration admits a unique section $C_{n}$ with negative self intersection; more precisely,

$C_{n}^{2}=-n$

and

$\mathrm{Pic}(\mathbb{F}_{\mathrm{n}})=\mathbb{Z}\mathrm{C}_{\mathrm{n}}\oplus\mathbb{Z}\mathrm{F}$

where $F$ is the class of a fiber of $\pi$. The linear system $|C_{n}+nF|$ defines a map $g:\mathbb{F}_{n}\to\mathbb{P}^{n+1}$. The image of $g$ is a cone over a Veronese model of $\mathbb{P}^{1}$ of degree $n$ in $\mathbb{P}^{n+1}$. The map $g$ is an isomorphism outside of $C_{n}$, and it contracts $C_{n}$ to the vertex of the cone.

Surfaces of minimal degree $r$ in $\mathbb{P}^{r+1}$ are completely classified, see for example *[11]*, *[17]* and they are the following:
Case 1.1: A smooth rational normal scroll, i.e., a surface obtained as $\mathbb{P}(\mathcal{E})$, with $\mathcal{E}=\mathcal{O}_{\mathbb{P}^{1}}(-a)\oplus\mathcal{O}_{\mathbb{P}^{1}}(-b),a,b>0$, embedded as a smooth surface of degree $a+b$ in $\mathbb{P}^{a+b+1}$ by the hyperplane linear system $\mathcal{O}_{\mathbb{P}(\mathcal{E})}(1)$. such a surface is isomorphic to the Hirzebruch surface $\mathbb{F}_{|a-b|}$, but this is a “better” embedding, which avoids the cone singularity.
Case 1.2: A cone representation of a Hirzebruch surface, as in the previous remark. this is the degeneration of Case 1 when we let $a$ or $b$ to be $0$.
Case 1.3: The Veronese embedding of $\mathbb{P}^{2}$ in $\mathbb{P}^{5}$

Proposition 104

The Case 1.1 is impossible.

Proof: In Case 1.1 the surface $Y\subset\mathbb{P}^{k+2}$ is isomorphic

$Y\simeq\mathbb{P}(\mathcal{O}_{\mathbb{P}^{1}}(-a)\oplus\mathcal{O}_{\mathbb{P}^{1}}(-b))$

where

$a+b=k+1$

We denote by $F$ a fiber of the $\mathbb{P}^{1}$-fibration $Y\to\mathbb{P}^{1}$, and by $H\in\mathrm{Pic}(\mathrm{Y})$ the hyperplane section giving the embedding $Y\hookrightarrow\mathbb{P}^{k+2}$. Then

$\mathrm{Pic}(\mathrm{Y})=\mathbb{Z}\mathrm{H}\oplus\mathbb{Z}\mathrm{F}$

where the product law is given by

$H^{2}=a+b=k+1,\quad HF=1,\quad F^{2}=0$

Moreover, it is a straightforward computation that

$K_{Y}=-2H+(k-1)F$

If we decompose

$f_{*}C=c_{1}H+c_{2}F,\quad c_{1},c_{2}\in\mathbb{Z},c_{1}\geq 0$

the equality

$Cf^{*}H=C(E+\overline{E})=4$

gives

$c_{1}(k+1)+c_{2}=4$

On the other hand, the divisor $f_{*}C$ has the form $f_{*}C=d\overline{C}$, with $d\in\{1,2\}$, and $\overline{C}$ a reduced irreducible divisor. Hence we can not allow $c_{1}=0,c_{2}=4$, because the linear system $|4F|$ does not contain divisors of such type. Thus the inequality

$c_{1}>0$

is sharp.
Let $\tilde{F}:=f^{*}F\subset X$ be the pre-image of a line $F$. 

$\tilde{F}K_{X}=Ff_{*}K_{X}=-\frac{1}{2}Ff_{*}C=-\frac{1}{2}c_{1}$

Hence, the curve $\tilde{F}$ has genus

$\tilde{g}:=g(\tilde{F})$

such that

$2\tilde{g}-2=\tilde{F}(\tilde{F}+K_{X})=-\frac{1}{2}c_{1}$

so that $c_{1}=4-4\tilde{g}$. This forces

$\tilde{g}=0$

and

$f_{*}C=4H-4kF$

Here we find a contradiction: the linear system $|4H-4kF|$ does not contain any irreducible reduced divisor $\overline{C}$. On the countrary, the genus of such a curve $\overline{C}$ would be equal to:

$g(\overline{C})=1+\frac{1}{2}\overline{C}(\overline{C}+K_{Y})-m_{\rm
sing}$

where $m_{\rm sing}\geq 0$ is the contribution given by the singularities of $\overline{C}$. But this leads to

$g(\overline{C})=3-6k-m_{\rm sing}<0$

which is impossible. The only remaining chance is that the restriction $f|_{C}$ is a double cover of an irreducible reduced divisor $\overline{C}\in|2H-2kF|$, but again, its genus $g(\overline{C})$ would be given by the same formula:

$g(\overline{C})=1+\frac{1}{2}\overline{C}(\overline{C}+K_{Y})-m_{\rm
sing}=-k-m_{\rm
sing}<0$

Again, we found a contradiction. $\Box$

###### Corollary 105

If $k=1$, then $f(C)$ is a non degenerate curve of degree $4$ in $\mathbb{P}^{3}$.

Proof: We already know that

$dim\,|H|=k+2=3$

so we have $f:X\to\mathbb{P}^{3}$. Suppose $f(C)$ is a plane curve: then the linear system $|H-C|$ is non empty, so there exist an effective divisor $D$,

$D\in|H-C|$

Of course $H\neq C\in{\rm Pic(X)}$, so $D$ cannot be the zero divisor. Moreover,

$HD=H^{2}-HC=(2k+2)-4=0$

so $f$ contracts all the irreducible components of $D$. By Remark 101 the only possibility is that all the irreducible components of $D$ are smooth rational $(-2)$-curves, which are necessarily disjoint from $C$. Thus $|H|$ would contain the disconnected section

$C+D\in|H|$

which is forbidden by Bertini’s Theorem. So $f(C)$ is non-degenerate. $\square$

###### Corollary 106

If $k=1$, then $|H|$ induces a map of degree $2$ on a cone in $\mathbb{P}^{3}$.

Proof: Since $H$ is an $i$-invariant linear system, there exists a projective involution

$I:\mathbb{P}^{3}\to\mathbb{P}^{3}$

which fits into the following commutative diagram:

In particular, $I$ acts as the identity over the curve $f(C)$, which is non degenerate by the previous corollary 105. Thus

$I=\mathbb{1}_{\mathbb{P}^{3}}$

everywhere, and hence $i$ preserves the fibers of $f$, which forces

$\deg{\rm f}=2$

and

$\deg{\rm f(X)}=\frac{{\rm H}^{2}}{\deg{\rm f}}=2$

So $f(X)$ is a quadric surface in $\mathbb{P}^{3}$, which must be a singular cone by Proposition 104. $\square$

###### Proposition 107

The Case 1.3 is also impossible.

Proof: This case can only happen if $k=3$, so that the linear system $|E+\overline{E}|$ is made up of curves of genus $4$. The image $Y$ of the associated map $f:X\to\mathbb{P}^{5}$ is the Veronese embedding of $\mathbb{P}^{2}$ through the linear system of plane quadrics. Let $v:\mathbb{P}^{2}\simeq Y\subset\mathbb{P}^{5}$ be this embedding. A general hyperplane section $H_{Y}\subset Y$ is a smooth rational curve, covered $2:1$ by a curve of genus $4$. Thus $H_{Y}$ contains $10$ branch points. This means that the composite map $v^{-1}\circ f:X\to\mathbb{P}^{2}$ is a double cover branched over a quintic curve, and this can not happen. $\square$

6.1 An application of Reider Theorem

Assume

$E\cap\overline{E}=\{p_{1},\ldots,p_{n}\}$

with $n\geq 3$, and let label these points such that

$\{p_{1},p_{2}\}=E\cap C=\overline{E}\cap C$

This forces $i(p_{1})=p_{1},i(p_{2})=p_{2}$. Assume also that

$i(p_{3})=p_{3}$

then for all $k\geq 4$ the Von Staudt Theorem gives the equality of cross ratios

$(p_{1},p_{2},p_{3},p_{k})=(p_{1},p_{2},p_{3},i(p_{k}))$

in $E$ (or in $\overline{E}$). This forces

$i(p_{k})=p_{k}$

for all the common points $p_{k}$’s, and hence

$\frac{E+\overline{E}}{i}\simeq\mathbb{P}^{1}$

In other words, $E+\overline{E}$ is an hyper-elliptic curve. Consequently, the canonical linear system $K_{E+\overline{E}}$ does not separate the point $p\in E$ from the point $i(p)\in\overline{E}$. the short exact sequence

$0\to\mathcal{O}_{X}(K_{X})\to\mathcal{O}_{X}(E+\overline{E}+K_{X})\to\mathcal{O}_{E+\overline{E}}(E+\overline{E}+K_{X})=\mathcal{O}_{E+\overline{E}}(K_{E+\overline{E}})\to 0$

induces an isomorphism

$H^{0}(X,E+\overline{E}+K_{X})\simeq H^{0}(E+\overline{E},K_{E+\overline{E}})$ (24)

For every $H\in|E+\overline{E}|$ there exists the same isomorphism

$H^{0}(X,E+\overline{E})\simeq H^{0}(H,K_{H})$ (25)

In particular, a pair of conjugate point $p\in E,i(p)\in\overline{E}$ is not separated by the canonical system $|K_{E+\overline{E}}|$. Relation 24 implies that $p,i(p)$ are not separated by the linear system $|E+\overline{E}|$, and relation 25 implies this pair is not separated by any canonical system $|K_{H}|$, for any $H\in|E+\overline{E}|$ containing both of them. This forces $H$ to be an hyperelliptic curve, for any $H\in|E+\overline{E}|$

containing a pair $p,i(p)$ for some $p\in E$.
Let’s count how many these curves are: a curve $H$ containing $p,i(p)$ lives in

$H\in|\mathcal{I}_{p,i(p)}(E+\overline{E})|$

where $\mathcal{I}_{p,i(p)}\subset\mathcal{O}_{X}$ is the ideal sheaf of the pair of points. The passage through both of them imposes two linear conditions on the space $H^{0}(\mathcal{O}_{X}(E+\overline{E}))$, so we find a 2-codimensional subspace in $|E+\overline{E}|$. As $p$ moves in $E$, this subspace moves inside $|E+\overline{E}|$, sweeping a divisor inside $|E+\overline{E}|$.

###### Theorem 108

Suppose $H$ is a nef linear system on a smooth projective surface $X$, with $H^{2}\geq 9$, and that there exist two points $p,q\in X$ which are not separated by the adjoint linear system $|H+K_{X}|$. Then there exists an effective divisor $D$ containing $p,q$, which satisfies one of the following cases:
$\cdot HD=0,D^{2}=-1$ or $-2$;
$\cdot HD=1,D^{2}=0$ or $-1$;
$\cdot HD=2,D^{2}=0$;
$\cdot H=3D,D^{2}=1$.

We now remember that $X$ can contain at most countably many rigid curves $D$, which are curves with $h^{0}(\mathcal{O}_{X}(D))=1$. Hence, without loss of generality we can assume that:

$p,q\mathop{\rm do\,not\,belong\,to\,any\,rigid\,curve}$ (26)

We will use this particular choice of points $p,i(p)$ to exclude most of these cases, but before we go on, we need the following technical result.

###### Proposition 109

We cannot have an effective linear system $|M|$ without base components such that $HM=1$.

Proof: Suppose the existence of such an $|M|$. Let

$f:X\to\mathbb{P}^{k+2}$

be the map induced by $|H|$.The equality

$HM=1$

means the generic element in $|M|$ is birational to (hence, isomorphic to) a line $l\in\mathbb{P}^{k+2}$. Thus the generic member of $|M|$ is a smooth rational curve. The vanishing $H^{1}(\mathcal{O}_{X})$ gives a short exact sequence:

$0\to H^{0}(\mathcal{O}_{X})\to H^{0}(\mathcal{O}_{X}(M))\to H^{0}(\mathcal{O}_{M}(M))\to 0$ (27)

with

$H^{0}(\mathcal{O}_{M}(M))\simeq H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(M^{2}))$

Since $|M|$ has no base components, we have

$M^{2}\geq 0$

We want to prove that both the cases $M^{2}=0$ and $M^{2}\geq 1$ are impossible.
Suppose

$M^{2}=0$

then by 27 we have that $|M|$ is a base point-free pencil, so there exists a regular map

$\pi:X\to\mathbb{P}^{1}$

whose fibers are elements of $|M|$. Since $HM=1$ and $H=E+\overline{E}$, we must have $EM=1,\overline{E}M=0$ or vice versa. Thus $\overline{E}$ is contained in a fiber of $\pi$, while $E$ is a section of $\pi$. But then $E,\overline{E}$ could meet in at most one point, contradicting $E\overline{E}\geq 2$.
Suppose now that

$M^{2}\geq 1$

By 27, this corresponds to

$h^{0}(\mathcal{O}_{X}(M))\geq 3$

Now choose a curve $M_{0}\in|M|$ and a point $x_{0}\in X$ such that its $f(x_{0})$ does not belong to the line $l_{0}:=f(M_{0})$. Since $h^{0}(\mathcal{O}_{X}(M))\geq 3$, for any $y\in M_{0}$ there exists a curve $M_{y}\in|M|$ containing both $y,x_{0}$. Hence the line $f(M_{y})$ lies inside $f(X)$, for every $y\in M_{0}$. This is possible only if $f(X)$ is equal to the plane spanned by $l_{0},f(x_{0})$, which is equivalent to $E\overline{E}=2$, and this is forbidden by 102. $\square$

The last case would imply $H^{2}=9$, which contradicts the parity of $H^{2}$.

Suppose we are in case 1: let decompose

$D=F+M$

where $F=Bs(D)$ is the fixed part of $D$, while $M$ is the mobile part of $D$. The relation $HD=0$ forces also

$HF=0$
$HM=0$

so both $F,M$ are contracted by $|H|$. Hence $|M|$ cannot move, otherwise the image of $|H|$ would not be $2$-dimensional.

Suppose then that $p,p^{\prime}$ belong to an effective divisor $D$ such that $HD=1$ and $D^{2}=0$ or $-1$. The same decomposition $D=F+M$ now leaves two possibilities:

$HF=1,HM=0$

or

$HF=0,HM=1$

Since $M$ can move, it cannot be contracted by $|H|$ unless $M=0$. Thus $D=F$ is a rigid divisor, and since $HD=1$, the image of $D$ is a smooth line $l\subset\mathbb{P}^{k+2}$, so $D$ has the form $D=D_{1}+D_{2}$, where $D_{1}$ is a rational normal curve, isomorphically mapped onto $l$, while $D_{2}$ is contracted. Again, this implies that the irreducible components of $D_{2}$ are $(-2)$-curves, which cannot contain $p,i(p)$ by assumption. Of course $D_{1}$ cannot move, otherwise $D$ could move as well. the short exact sequence

$0\to\mathcal{O}_{X}\to\mathcal{O}_{X}(D_{1})\to\mathcal{O}_{D_{1}}(D_{1})\to 0$

remains exact in cohomology, so

$H^{0}(\mathcal{O}_{D_{1}}(D_{1}))=0$

which is the same as

$D_{1}^{2}<0$

But this only happen if

$D_{1}^{2}=-1\,\mathrm{or}\,-2$

which again contradicts the initial assumption 26.
The opposite case

$HF=0,HM=1$

is forbidden by Proposition 109.
The unique remaining case in that

$HD=2,D^{2}=0$

which leaves three possibilities:

$HF=0,HM=2$

or

$HF=1,HM=1$

or

$HF=2,HM=0$

Assume we have the first case, so that

$HF=0,HM=2$

We first show that the generic element in $|M|$ must be irreducible. If this does not happen, by Bertini’s Theorem $M$ must be composite with a pencil $\hat{M}$, and the relation $HM=2$ forces

$M=2\hat{M}$

and

$H\hat{M}=1$

which is forbidden by 109.
Now that we have the irreducibility of $|M|$, its general member is either mapped birationally (and hence isomorphically) on smooth plane curves of degree 2, or it is a double cover of a line in $\mathbb{P}^{k+2}$. In the first situation the generic $M$ is such that $f(M)$ spans a plane inside $\mathbb{P}^{k+2}$, that is:

$h^{0}(\mathcal{O}_{X}(H))-h^{0}(\mathcal{O}_{X}(H-M))=3$ (28)

The second case happens if $f(M)$ spans a line in $\mathbb{P}^{k+2}$, that is:

$h^{0}(\mathcal{O}_{X}(H))-h^{0}(\mathcal{O}_{X}(H-M))=2$ (29)

In both cases, we must have

$h^{0}(\mathcal{O}_{X}(M))=2$

Indeed, since $M$ can move the inequality $h^{0}(\mathcal{O}_{X}(M))\geq 2$ is guaranteed. Assume that $h^{0}(\mathcal{O}_{X}(M))\geq 3$. Then we can argue similarly to Proposition 109: any two points $x_{1},x_{2}\in X$ can be joined by an element of $|M|$. Consequently, if 28 (respectively, 29) holds, then any two points $y_{1},y_{2}\in f(X)$ can be joined by a plane conic curve (respectively, a line) which is entirely contained in $f(X)$. This cases can happen respectively if $f(X)$ has degree 2 or 1, but by hypothesis we have $H^{2}\geq 10$, which means $\deg{\rm f(X)}\geq 5$.
So until now we proved that

$h^{0}(\mathcal{O}_{X}(M))=2$

and the generic element in $|M|$ is irreducible.
Now we no element of $|M|$ can entirely contain $C$. If this happens, then

$M=C+R$

for some effective divisor $R$. But multiplying by $H$ we find

$2=4+HR$

a contradiction, since $HR$ must be non-negative.
We now show that 28 is impossible: as we stated, this corresponds to say that the generic element of $|M|$ is birational via $f$ to a smooth plane conic. In particular, the generic element in $|M|$ is a smooth rational curve. Hence, we find a short exact sequence

$0\to H^{0}(\mathcal{O}_{X})\to H^{0}(\mathcal{O}_{X}(M))\to H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(M^{2}))\to 0$

and hence

$M^{2}=0$

Thus $|M|$ is a base-point free pencil of rational curves, so its elements are fibers of a regular map $\pi:X\to\mathbb{P}^{1}$. The adjunction formula

$M^{2}+MK_{X}=-2$

becomes $MK_{X}=-2$ so

$MC=4$

Thus $C$ is a 4-section of $\pi$. Consider again the map $f:X\to\mathbb{P}^{k+2}$ induced by $|H|$. Since $f(C)$ has degree at most 4, we can write

$f(C)\subset\Gamma$

for some 4-dimensional linear subspace $\mathbb{P}^{4}\simeq\Gamma\subset\mathbb{P}^{k+2}$. But now a generic $X_{\lambda}\in|M|$ intersects $C$ at 4 points, so the plane conic $f(X_{\lambda})$ touches $\Gamma$ in 4 different points. This happens only if $f(X_{\lambda})\subset\Gamma$ for the generic $\lambda\in\mathbb{P}^{1}$, which forces $f(X)\subset\Gamma$. This is a contradiction, because the initial hypothesis $H^{2}\geq 10$ corresponds to $dim\,|H|\geq 6$.
So we are in the case where the generic element of $|M|$ covers a line in $\mathbb{P}^{k+2}$ with degree 2. Again, an inequality $h^{0}(\mathcal{O}_{X}(M))\geq 3$ would imply that every couple of points in $X$ can be joint by an element of $|M|$, so $f(X)$ would be a plane, which is absurd. Hence,

$h^{0}(\mathcal{O}_{X}(M))=2$

Putting this data in Riemann - Roch Theorem we get

$2-h^{1}(\mathcal{O}_{X}(M))=1+\frac{1}{2}(M^{2}-MK_{X})$

The effectiveness of $|-2K_{X}|$ gives $MK_{X}\leq 0$. Moreover, for the same reason as before, no member of $|M|$ can contain $C$, so inequality

$MK_{X}<0$

must be sharp. This leads to

$1-h^{1}({\cal O}_{X}(M))=\frac{1}{2}(M^{2}-MK_{X})>0$

So we have

$h^{1}({\cal O}_{X}(M))=0$

and

$M^{2}-MK_{X}=2$

which separates in two cases

$M^{2}=0,MK_{X}=-2$

or

$M^{2}=1,MK_{X}=-1$

In the first case $|M|$ is a basepoint-free pencil of smooth rational curves, in the second it’s a pencil of elliptic curves with one base point.
In the elliptic case, 

${\cal O}_{M}(M+K_{X})={\cal O}_{M}(K_{M})={\cal O}_{M}$

so the short exact sequence

$0\to{\cal O}_{X}(K_{X})\to{\cal O}_{X}(M+K_{X})\to{\cal O}_{M}(M+K_{X})$

induces an isomorphism

$H^{0}({\cal O}_{X}(M+K_{X}))\simeq H^{0}({\cal O}_{M})\simeq{\mathbb{C}}$

Thus $M+K_{X}$ is a rigid effective divisor, and the equality

$H(M+K_{X})=2-2=0$

states that it is contracted via $f$. But we know that such a divisor is supported on a $(-1)$-curves. Moreover, the self intersection

$(M+K_{X})^{2}=-2$

gives

$M+K_{X}=F_{1}+F_{2}$

with $F_{1},F_{2}$ disjoint $(-1)$-curves. But now $E,F_{1},F_{2}$ can be extended to a set of 10 disjoint $(-1)$-curves

$E_{1},\ldots,E_{8},F_{1},F_{2}$

with

$E=E_{1}$

. Since also $\overline{E}$ is disjoint from $F_{1},F_{2}$, its class in Pic(X) takes the form

$\overline{E}=dL-k_{1}E_{1}\cdots-k_{8}E_{8}$

with

$k_{1}=k+2$

. Since $\overline{E}$ is a $(-1)$-curve, the coefficients have to satisfy the system

\[ \left\{\begin{array}[]{l}d^{2}-\sum_{i}k_{i}^{2}=-1\\
\\
-3d+\sum_{i}k_{i}=-1\end{array}\right. \]

This corresponds to look for $(-1)$-curves in a Del Pezzo surface of degree 1, but they are finite and well known, and satisfy $k_{1}\leq 3$. But then $H^{2}=2E\overline{E}-2\leq 4$, contradicting Reider hypothesis.
Hence the unique possible answer is that $|M|$ is a base point free pencil of rational curves. But such a pencil must have 9 singular fibers, and each of them consists of a linear chain of two $(-1)$-curves, attached at one point.
Remember that

$(E+\overline{E})M=2$

and that leaves only

$EM=\overline{E}M=1$ (30)

Indeed, if we assume

$EM=2,\overline{E}M=0$

then $\overline{E}$ must be contained in a fiber of $|M|$, while $E$ is a bisection of $|M|$. This would force

$E\overline{E}\leq 2$

which contradicts the hypothesis.
By reason of the Picard number, $|M|$ must have 9 singular fibers. Relation 30 implies that each of these contains a $(-1)$-curve not touched by

$E$. Let $F_{1},\cdots,E_{9}$ be these $(-1)$-curves. The simoultaneous contraction of $E,F_{1},\ldots,F_{9}$ transforms $X$ in $\mathbb{P}^{2}$, so we can use $L,E,F_{1},\ldots,F_{9}$ as base for Pic(X). In this basis we must have

$|M|=|L-E|$

since $M$ is orthogonal to $F_{1},\ldots,F_{9}$. Moreover, we write

$\overline{E}=dL-(k+2)E-a_{1}F_{1}\cdots-a_{9}F_{9}$

But now we use again 30 to deduce that

$d=k+3$

Since $k+2$ is the maximum possible multiplicity for an irreducible curve of degree $k+3$, this forces

$a_{1},\ldots,a_{9}\in\{0,1\}$

Let $b$ the number of $a_{i}$’s which are equal to 1. Since

$\overline{E}^{2}=-1$

we also have

$b=2k+6$

which combined with $b\leq 9$ gives

$k=0,1$

Both of these two values contradict the Reider assumption $H^{2}\geq 9$. Note nonetheless that we producted two expressions for $\overline{E}$ and $H$, which up to permutations are

$\overline{E}=3L-2E-E_{1}\cdots-E_{6},H=3L-E-E_{1}\cdots-E_{6}\,\text{if}\,k=0$

and

$\overline{E}=4L-3E-E_{1}\cdots-E_{8},H=4L-2E-E_{1}\cdots-E_{8}\,\text{if}\,k=1$

### 6.2 The tangent behaviour

On the curve $C\subset X$ we have the short normal exact sequence

$0\to T_{C}\to T_{X}|_{C}\to N_{C/X}\to 0$

We identify $C\simeq\mathbb{P}^{1}$, so that the tangent bundle $T_{C}$ on $C$ can be identified with

$T_{C}=T_{\mathbb{P}^{1}}=\mathcal{O}_{\mathbb{P}^{1}}(2)$

and clearly

$N_{C/X}=\mathcal{O}_{C}(C)\simeq\mathcal{O}_{\mathbb{P}^{1}}(C^{2})=\mathcal{O}_{\mathbb{P}^{1}}(-4)$

Since

$Ext^{1}(\mathcal{O}_{\mathbb{P}^{1}}(-4),\mathcal{O}_{\mathbb{P}^{1}}(2))=0$

we have

$T_{X}|_{C}=\mathcal{O}_{\mathbb{P}^{1}}(2)\oplus\mathcal{O}_{\mathbb{P}^{1}}(-4)$

Let $\mathcal{E}$ denote the rank 2 vector bundle

$\mathcal{E}=TX|_{C}\otimes\mathcal{O}_{\mathbb{P}^{1}}(-2)=\mathcal{O}_{\mathbb{P}^{1}}\oplus\mathcal{O}_{\mathbb{P}^{1}}(-6)$

Then the space $P=\mathbb{P}(\mathcal{E})$ is a $\mathbb{P}^{1}$-fibration over $\mathbb{P}^{1}$, corresponding to the sixth Hirzebruch surface $P=\mathbb{F}_{6}$. The standard hyperplane bundle $\mathcal{O}_{P}(1)$ defines an isomorphism

$H^{0}(P,\mathcal{O}_{P}(1))\simeq H^{0}(\mathbb{P}^{1},\mathcal{E}^{*})=H^{0}(\mathbb{P}^{1},\mathcal{O})\oplus H^{0}(\mathcal{O}_{\mathbb{P}^{1}}(6))$

The last space has dimension 8 over $\mathbb{C}$, so the linear system $|\mathcal{O}_{P}(1)|$ defines a map $P\to\mathbb{P}^{7}$. The section

Suppose $\alpha:X\to X$ is an automorphism such that $\alpha|_{C}=\mathbb{1}_{C}$, and suppose also that $\alpha$ is an involution,

$\alpha^{2}=\mathbb{1}$

For each point $p\in C$, the differential operator $d_{p}\alpha$ acts on the tangent space $T_{p}X$, so the operator $d\alpha$ defines a linear endomorphism of the vector bundle

$d\alpha:TX|_{C}\to TX|_{C}$

The line subbundle $\mathcal{O}_{\mathbb{P}^{1}}(2)\subset\mathcal{O}_{\mathbb{P}^{1}}(2)\oplus\mathcal{O}_{\mathbb{P}^{1}}(-4)$ corresponds to the tangent space of $C$, so it is composed of $(+1)$-eigenvectors of $d\alpha$. Since $\alpha^{2}=\mathbb{1}_{X}$, the other eigenvector on the points of $C$ is $-1$. Let $\mathcal{L}\subset TX|_{C}$ denote the line subbundle generated by these $(-1)$-eigenvectors at all points of $C$. Then $\mathcal{L}$ corresponds to a complementar subspace for $TC$ inside $TX|_{C}$, so

$\mathcal{L}\simeq\mathcal{O}_{\mathbb{P}^{1}}(-4)$

We remember now that the Coble surface $X$ is nothing but a blow up of $\mathbb{P}^{2}$ at the nodes of a rational sextic curve $\overline{C}$. Let

$\pi:X\to\mathbb{P}^{2}$

the blow-down map,

Let $F\in H^{0}(\mathcal{O}_{\mathbb{P}^{2}}(6))$ be the equation of $\overline{C}$. We consider the dual curve

$\overline{C}^{*}\subset\mathbb{P}^{2^{*}}$

which is the image of $\overline{C}$ under the map

$\overline{C}\to\mathbb{P}^{2^{*}}$

$p\to T_{p}\overline{C}$

In projective coordinates, this map has the form

$x\to[\frac{\partial F}{\partial Z_{0}}(x),\frac{\partial F}{\partial Z_{1}}(x),\frac{\partial F}{\partial Z_{2}}(x)]$

The partial derivatives $\frac{\partial F}{\partial Z_{i}}$ form a net of quintic forms with $10$ base points, if $F$ is generic enough. Thus, these form cut over $\overline{C}$ a divisor $D$ of degree $5\deg\overline{C}=30$, with a base locus of degree $2$ at each node of $\overline{C}$. Thus the mobile part of $D$ has degree $30-2\cdot 10=10$, which means that

$\deg\overline{C}^{*}=10$

Now we look at the following rational map:

$\psi:\mathbb{P}(TX|_{C})\dashrightarrow\mathbb{P}^{2^{*}}$

$(x,[v])\to\{\,\text{the unique line through}\;\pi(x)\;\text{tangent to}\;d\;\pi_{x}(v)\}$

This map possesses $20$ indeterminacy points: if $E_{1},\cdots,E_{10}$ are the exceptional curves of $\pi$, and

$\{x_{i},y_{i}\}=C\cap E_{i}$

then $\,\ker d_{x_{i}}\,\pi:T_{x_{i}}X\;toT_{\pi(x_{i})}\mathbb{P}^{2}\neq 0$. Indeed,

$\,\ker d_{x_{i}}=T_{x_{i}}E_{i}$

and the same holds for $y_{i}$ too. By construction, the map $\psi$ is undefined at the points $(x_{i},T_{x_{i}}E_{i}),(y_{i},T_{y_{i}}E_{i})$. Away from these points, $\psi$ is well defined. Then we blow up $\mathbb{F}_{6}=\mathbb{P}(TX|_{C})$ in these $20$ points, and we get another surface $\tilde{\mathbb{F}_{\mathsf{\mathbf{\in}}}}$, with a resolution of indeterminacies

$\tilde{\psi}:\tilde{\mathbb{F}_{\mathsf{\mathbf{\in}}}}\to\mathbb{P}^{2^{*}}$

and

7 Acknowledgements

I would like to express my warmest gratitude to my Advisor, Professor Alessandro Verra. This work would have never been possible without his precious support. During these three years, he provided irreplaceable contributions with his comments, inputs, and ability to show links between totally apparently different fields of Algebraic Geometry. His deepest knowledge of the topics we treated were very inspirational to me. Especially when I felt blocked, his human presence and fantasy to find new perspectives provided an incredible support.

##

References

- [1] Valery Alexeev, Philip Milton Engel, D. Zack Garza, and Luca Schaffler. Compact moduli of Enriques surfaces with a numerical polarization of degree 2. Preprint, arXiv:2312.03638 [math.AG] (2023), 2023.
- [2] Lionel Bayle and Arnaud Beauville. Birational involutions of $\mathbb{P}^{2}$. Asian J. Math., 4(1):11–17, 2000.
- [3] Serge Cantat and Igor Dolgachev. Rational surfaces with a large group of automorphisms. J. Am. Math. Soc., 25(3):863–905, 2012.
- [4] Ciro Ciliberto, Thomas Dedieu, Concettina Galati, and Andreas Leopold Knutsen. Nonemptiness of Severi varieties on Enriques surfaces. Forum Math. Sigma, 11:32, 2023. Id/No e52.
- [5] A. B. Coble. Cremona transformations with an invariant rational sextic. Bull. Am. Math. Soc., 45:285–288, 1939.
- [6] Arthur B. Coble. The Ten Nodes of the Rational Sextic and of the Cayley Symmetroid. Amer. J. Math., 41(4):243–265, 1919.
- [7] A. Conte and A. Verra. Reye constructions for nodal Enriques surfaces. Trans. Amer. Math. Soc., 336(1):79–100, 1993.
- [8] François R. Cossec. On the Picard group of Enriques surfaces. Math. Ann., 271(4):577–600, 1985.
- [9] François Cossec, Igor Dolgachev, and Christian Liedtke. Enriques surfaces I (to appear). Singapore: Springer, 2nd edition edition, 2025.
- [10] Francois R. Cossec. Reye congruences. Trans. Am. Math. Soc., 280:737–751, 1983.
- [11] P. del Pezzo. On surfaces of order $n$ in an $n+1$-dimensional space. über flächen $n$-ter ordnung im $n+1$-dimensionalen Raum. Nap. Rend., 24:212–216, 1885.
- [12] I. Dolgachev. Invariant sextic (after A. Coble). Unpublished Notes, 2019.
- [13] I. Dolgachev and S. Kond$\overline{\text{o}}$. The rationality of the moduli spaces of Coble surfaces and of nodal Enriques surfaces. Izv. Ross. Akad. Nauk Ser. Mat., 77(3):77–92, 2013.
- [14] Igor Dolgachev and Shigeyuki Kond$\overline{\text{o}}$. Enriques surfaces II. Singapore: Springer, 2025.
-

[15] Igor V. Dolgachev. A brief introduction to Enriques surfaces. In *Development of moduli theory – Kyoto 2013. Proceedings of the 6th Mathematical Society of Japan-Seasonal Institute, MSJ-SI, Kyoto, Japan, June 11–21, 2013*, pages 1–32. Tokyo: Mathematical Society of Japan (MSJ), 2016.
- [16] Igor V. Dolgachev and De-Qi Zhang. Coble rational surfaces. *Am. J. Math.*, 123(1):79–114, 2001.
- [17] David Eisenbud and Joe Harris. On varieties of minimal degree. (A centennial account). Algebraic geometry, Proc. Summer Res. Inst., Brunswick/Maine 1985, part 1, Proc. Symp. Pure Math. 46, 3-13 (1987)., 1987.
- [18] David Eisenbud and Joe Harris. *3264 and all that. A second course in algebraic geometry*. Cambridge: Cambridge University Press, 2016.
- [19] A. Hirschowitz. Symétries des surfaces rationnelles génériques. *Math. Ann.*, 281(2):255–261, 1988.
- [20] Daniel Huybrechts. *Complex geometry. An introduction*. Universitext. Berlin: Springer, 2005.
- [21] Andreas Leopold Knutsen. On moduli spaces of polarized Enriques surfaces. *J. Math. Pures Appl. (9)*, 144:106–136, 2020.
- [22] John Lesieutre. Tri-Coble surfaces and their automorphisms. *J. Mod. Dyn.*, 17:267–284, 2021.
- [23] Tie Luo. A note on the Hodge index theorem. *Manuscr. Math.*, 67(1):17–20, 1990.
- [24] Gebhard Martin, Giacomo Mezzedimi, and Davide Cesare Veniani. Nodal Enriques surfaces are Reye congruences. *J. Reine Angew. Math.*, 808:49–65, 2024.
- [25] Rick Miranda and Aline Zanardini. The moduli space of rational elliptic surfaces of index two. *Indag. Math., New Ser.*, 33(5):919–935, 2022.
- [26] Riccardo Moschetti, Franco Rota, and Luca Schaffler. A computational view on the non-degeneracy invariant for Enriques surfaces. *Exp. Math.*, 33(3):400–421, 2024.
- [27] D. Mumford, J. Fogarty, and F. Kirwan. *Geometric invariant theory.*, volume 34 of *Ergeb. Math. Grenzgeb.* Berlin: Springer-Verlag, 3rd enl. ed. edition, 1994.

[28] V. V. Nikulin. Quotient-groups of groups of automorphisms of hyperbolic forms of subgroups generated by 2-reflections. Dokl. Akad. Nauk SSSR, 248(6):1307–1309, 1979.
- [29] Giuseppe Pompilj. Sulle transformazioni Cremoniane che posseggono per curva di punti uniti una sestica con dieci punti doppi. Bull. Amer. Math. Soc., 46:684–686, 1940.
- [30] Igor Reider. Vector bundles of rank 2 and linear systems on algebraic surfaces. Ann. Math. (2), 127(2):309–316, 1988.
- [31] Th. Reye. The problem of the configurations. Acta Math., 1:93–96, 1882.
- [32] Igor R. Shafarevich. Basic algebraic geometry 1. Varieties in projective space. Translated from the Russian by Miles Reid. Berlin: Springer, 3rd ed. edition, 2013.
- [33] Alessandro Verra. From Enriques surface to Artin-Mumford counterexample. In Algebraic geometry between tradition and future. An Italian perspective. Proceedings of the INdAM workshop, Rome, Italy, December 6–8, 2021, pages 191–217. Singapore: Springer, 2023.
- [34] È.B̀. Vinberg. The two most algebraic $K3$ surfaces. Math. Ann., 265(1):1–21, 1983.
- [35] Aline Zanardini. Explicit constructions of Halphen pencils of index two. Rocky Mt. J. Math., 52(4):1485–1522, 2022.
- [36] D.-Q. Zhang. Automorphisms of finite order on rational surfaces. With an appendix by I. Dolgachev. J. Algebra, 238(2):560–589, 2001.
