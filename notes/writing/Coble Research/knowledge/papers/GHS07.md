---
title: The Kodaira dimension of the moduli of K3 surfaces
authors:
- Gritsenko
- K.
year: ''
bibkey: GHS07
tags:
- paper
- extraction
abstract: |
  The global Torelli theorem for projective K3 surfaces was first proved by Piatetskii-Shapiro and Shafarevich 35 years ago, opening the way to treat moduli problems for K3 surfaces.
  The moduli space of polarised K3 surfaces of degree $2d$ is a quasi-projective variety of dimension 19. For general $d$ very little has been known about the Kodaira dimension of these varieties.
  In this paper we present an almost complete solution to this problem.
  Our main result says that this moduli space is of general type for $d>61$ and for $d=46$, 50, 54, 58, 60.
---

# The Kodaira dimension of the moduli of K3 surfaces

V.
Gritsenko, K.
Hulek and G.K.
Sankaran

###### Abstract

The global Torelli theorem for projective K3 surfaces was first proved by Piatetskii-Shapiro and Shafarevich 35 years ago, opening the way to treat moduli problems for K3 surfaces.
The moduli space of polarised K3 surfaces of degree $2d$ is a quasi-projective variety of dimension 19. For general $d$ very little has been known about the Kodaira dimension of these varieties.
In this paper we present an almost complete solution to this problem.
Our main result says that this moduli space is of general type for $d>61$ and for $d=46$, 50, 54, 58, 60.

## 0 Introduction

Moduli spaces of polarised K3 surfaces can be identified with the quotient of a classical hermitian domain of type $IV$ and dimension 19 by an arithmetic group.
The general set-up for the problem is the following.
Let $L$ be an integral lattice with a quadratic form of signature $(2,n)$ and let

${\cal D}_{L}=\{[{\bf w}]\in{\mathbb{P}}(L\otimes{\mathbb{C}})\mid({\bf w},{\bf w})=0,\;({\bf w},{\overline{\bf w}})>0\}^{+}$ (1)

be the associated $n$-dimensional Hermitian domain (here $+$ denotes one of its two connected components).
We denote by ${\rm O}(L)^{+}$ the index 2 subgroup of the integral orthogonal group ${\rm O}(L)$ preserving ${\cal D}_{L}$.
We are, in general, interested in the birational type of the $n$-dimensional variety

${\cal F}_{L}(\Gamma)=\Gamma\backslash{\cal D}_{L}$ (2)

where $\Gamma$ is a subgroup of ${\rm O}^{+}(L)$ of finite index. Clearly, the answer will depend strongly on the lattice $L$ and the chosen subgroup $\Gamma$.

A compact complex surface $S$ is a K3 surface if $S$ is simply connected and there exists a holomorphic 2-form $\omega_{S}\in H(S,\Omega^{2})$ without zeros.
For example, a smooth quartic in ${\mathbb{P}}^{3}({\mathbb{C}})$ is a K3 surface and all quartics (modulo projective equivalence) form a (unirational) space of dimension 19.

The second cohomology group $H^{2}(S,{\mathbb{Z}})$ with the intersection pairing is an even unimodular lattice of signature $(3,19)$, more precisely,

$H^{2}(S,{\mathbb{Z}})\cong L_{{\rm K}3}=3U\oplus 2E_{8}(-1)$ (3)

$U$ is the hyperbolic plane and $E_{8}(-1)$ is the negative definite even lattice associated to the root system $E_{8}$.
The 2-form $\omega_{S}$, considered as a point of $\mathbb{P}(L_{\mathrm{K}3}\otimes\mathbb{C})$, is the period of $S$.
By the Torelli theorem the period of a K3 surface determines its isomorphism class.
The moduli space of all K3 surfaces is not Hausdorff.
Therefore it is better to restrict to moduli spaces of polarised K3 surfaces.
The moduli of all algebraic K3 surfaces are parametrised by a countable union of 19-dimensional irreducible algebraic varieties.
To choose a component we have to fix a polarisation.
A polarised K3 surface of degree $2d$ is a pair $(S,H)$ consisting of a K3 surface $S$ and a primitive pseudo-ample divisor $H$ on $S$ of degree $H^{2}=2d>0$.
If $h$ is the corresponding vector in the lattice $L_{\mathrm{K}3}$ then its orthogonal complement

$h^{\perp}_{L_{\mathrm{K}3}}\cong L_{2d}=2U\oplus 2E_{8}(-1)\oplus\langle-2d\rangle$ (4)

is a lattice of signature $(2,19)$.

The 2-form $\omega_{S}$ determines a point of $\mathcal{D}_{L_{2d}}$ modulo the group

$\widetilde{\mathrm{O}}^{+}(L_{2d})=\{g\in\mathrm{O}^{+}(L_{\mathrm{K}3})\mid g(h)=h\}.$

By the global Torelli theorem (_[x11]_) and the surjectivity of the period map

$\mathcal{F}_{2d}=\widetilde{\mathrm{O}}^{+}(L_{2d})\setminus\mathcal{D}_{L_{2d}}$ (5)

is the coarse moduli space of polarised K3 surfaces of degree $2d$.
By a result of Baily and Borel _[x1]_, $\mathcal{F}_{2d}$ is a quasi-projective variety.
One of the fundamental problems is to determine its birational type.

For $d=2$, $3$ and $4$ the polarised K3 surfaces of degree $2d$ are complete intersections in $\mathbb{P}^{d+1}(\mathbb{C})$ and the moduli spaces $\mathcal{F}_{2d}$ for such $d$ are classically known.
Mukai has extended these results in his papers _[x14]_, _[x15]_ and _[x16]_ to $1\leq d\leq 10$ and $d=17$, $19$, showing that these moduli spaces are also unirational.

In the other direction there are two results of Kondo and of Gritsenko.
Kondo _[x10]_ considered the moduli spaces $\mathcal{F}_{2p^{2}}$ where $p$ is a prime number.
(The reason for this choice is that all these spaces are covers of $\mathcal{F}_{2}$.) He proved that these spaces are of general type for $p$ sufficiently large.
His result, however, is not effective.
Gritsenko _[x7]_ showed a result for level structures: let $\widetilde{\mathrm{O}}^{+}(L_{2d})(q)$ be the principal congruence subgroup of $\widetilde{\mathrm{O}}^{+}(L_{2d})$ of level $q$.
Then $\widetilde{\mathrm{O}}^{+}(L_{2d})(q)\setminus\mathcal{D}_{L_{2d}}$ is of general type for any $d$ if $q\geq 3$.
In this paper we determine the Kodaira dimension of $\mathcal{F}_{2d}$ without imposing any a priori restriction on $d$.

###### Theorem 1

The moduli space $\mathcal{F}_{2d}$ of K3 surfaces with a polarisation of degree $2d$ is of general type for any $d>61$ and for $d=46$, $50$, $54$, $57$, $58$ and $60$.

If $d\geq 40$ and $d\neq 41$, $44$, $45$ or $47$ then the Kodaira dimension of $\mathcal{F}_{2d}$ is non-negative.

The description of the moduli space ${\cal F}_{2d}$ as a quotient of the symmetric space ${\cal D}_{L_{2d}}$ by a subgroup of the orthogonal group leads us to study, more generally, quotients of the form ${\cal F}_{L}(\Gamma)=\Gamma\backslash{\cal D}_{L}$.
One of the main tools in our proof of the main theorem is the following general result (for a more precise formulation see Theorem 2.1).

###### Theorem 2

Let $L$ be a lattice of signature $(2,n)$ with $n\geq 9$, and let $\Gamma<{\rm O}^{+}(L)$ be a subgroup of finite index. Then there exists a toroidal compactification $\overline{\cal F}_{L}(\Gamma)$ of ${\cal F}_{L}(\Gamma)=\Gamma\backslash{\cal D}_{L}$ such that $\overline{\cal F}_{L}(\Gamma)$ has canonical singularities.

We hope that this result will also be important for other applications.

The plan of the paper is as follows.
In Section 1 we give the basic definitions that we shall need and explain what the obstructions are to showing that ${\cal F}_{L}(\Gamma)$ is of general type.
These obstructions may be called elliptic, cusp and reflective.
The elliptic obstructions come from singularities of ${\cal F}_{L}(\Gamma)$ and its compactifications.
The cusp obstructions come from infinity, i.e. from the fact that ${\cal F}_{L}(\Gamma)$ is only quasi-projective.
The reflective obstructions come from divisors fixed by $\Gamma$ in its action on the symmetric space ${\cal D}_{L}$.

In Section 2 we deal with the elliptic obstructions and we show, by an analysis of the toroidal compactifications, that they disappear if $n\geq 9$, and also that there are no fixed divisors at infinity.

In Section 3 we examine the reflective obstructions by describing the fixed divisors.
We do this first for arbitrary $L$ and then in greater detail for $L_{2d}$.

In Section 4 we turn to the cusp obstructions.
We describe the structure of the cusps for a lattice $L$ having only cyclic isotropic subgroups in its discriminant group.

In Section 5 we study the moduli space ${\cal SF}_{2d}$ of K3 surfaces with a spin structure.
In this case there are few reflective obstructions, and the cusp forms constructed by Jacobi lifting already have the properties we need.

In Section 6 we show how to construct forms with the properties needed for ${\cal F}_{2d}$ by pulling back the Borcherds form.
This requires us to find a suitable embedding of $L_{2d}$ in $L_{2,26}$, which in turn requires a vector in $E_{8}$ with square $2d$ that is orthogonal to at most $12$ and at least $2$ roots.
We show directly that such a vector exists for large $d$ and use a small amount of computer help to show that it exists for smaller $d$.
For some values of $d$ we can find only a vector of square $2d$ orthogonal to $14$ roots.
In these cases we can deduce that ${\cal F}_{2d}$ has non-negative Kodaira dimension.

Acknowledgements: We have learned much from conversations with many people, but from S.
Kondo and N.I.
Shepherd-Barron especially.
We are grateful for financial support from the Royal Society and the DFG Schwerpunktprogramm SPP 1094 “Globale Methoden in der komplexen Geometrie”, Grant Hu 337/5-3.
We are also grateful for the hospitality and good

working conditions provided by several places where one or more of us did substantial work on this project: the Max-Planck-Institut für Mathematik in Bonn; DPMMS in Cambridge and Trinity College, Cambridge; Nagoya University; KIAS in Seoul; Tokyo University; and the Fields Institute in Toronto.

## 1 Orthogonal groups and modular forms

Let $L$ be a lattice of signature $(2,n)$, with $n>1$.
For any lattice $M$ and field $K$ we write $M_{K}$ for $M\otimes K$.
Then $\mathcal{D}_{L}$ is one of the two connected components of

$\{[{\bf w}]\in\mathbb{P}(L_{\mathbb{C}})\mid({\bf w},{\bf w})=0,\;({\bf w},\overline{{\bf w}})>0\}.$

We denote by $\mathrm{O}^{+}(L)$ the subgroup of $\mathrm{O}(L)$ that preserves $\mathcal{D}_{L}$.
If $\Gamma<\mathrm{O}^{+}(L)$ is of finite index we denote by $\mathcal{F}_{L}(\Gamma)$ the quotient $\Gamma\backslash\mathcal{D}_{L}$, which is a quasi-projective variety by _[x1]_.

For every non-degenerate integral lattice we denote by $L^{\vee}=\mathrm{Hom}(L,\mathbb{Z})$ its dual lattice.
The finite group $A_{L}=L^{\vee}/L$ carries a discriminant quadratic form $q_{L}$ (if $L$ is even) and a discriminant bilinear form $b_{L}$, with values in $\mathbb{Q}/2\mathbb{Z}$ and $\mathbb{Q}/\mathbb{Z}$ respectively (see _[x21, §1.3]_).
We define

$\widetilde{\mathrm{O}}(L)$ $=$ $\{g\in\mathrm{O}(L)\mid g|_{A_{L}}=\mathrm{id}\},\;\mbox{ and}$
$\widetilde{\mathrm{O}}^{+}(L)$ $=$ $\widetilde{\mathrm{O}}(L)\cap\mathrm{O}^{+}(L).$

The K3 lattice is

$L_{\mathrm{K3}}=3U\oplus 2E_{8}(-1)$

where $U$ is the hyperbolic plane and $E_{8}$ is the (positive definite) $E_{8}$-lattice.
If $h\in L_{\mathrm{K3}}$ is a primitive vector with $h^{2}=2d>0$ then its orthogonal complement $h^{\perp}_{L_{\mathrm{K3}}}$ is isometric to

$L_{2d}=\langle-2d\rangle\oplus 2U\oplus 2E_{8}(-1).$

By _[x21, Proposition 1.5.1]_

$\widetilde{\mathrm{O}}(L_{2d})\cong\{g\in\mathrm{O}(L_{\mathrm{K3}})\mid g(h)=h\},$

and the moduli space $\mathcal{F}_{2d}$ is given by

$\mathcal{F}_{2d}=\widetilde{\mathrm{O}}^{+}(L_{2d})\backslash\mathcal{D}_{L_{2d}}.$

A modular form of weight $k$ and character $\chi\colon\Gamma\to\mathbb{C}^{*}$ for a subgroup $\Gamma<\mathrm{O}^{+}(L)$ is a holomorphic function $F\colon\mathcal{D}_{L}^{\bullet}\to\mathbb{C}$ on the affine cone $\mathcal{D}_{L}^{\bullet}$ over $\mathcal{D}_{L}$ such that

$F(tZ)=t^{-k}F(Z)\;\forall\,t\in\mathbb{C}^{*},\;\mbox{ and }\;F(gZ)=\chi(g)F(Z)\;\forall\,g\in\Gamma.$ (6)

A modular form is a cusp form if it vanishes at every cusp.
We denote the linear spaces of modular and cusp forms of weight $k$ and character $\chi$ for $\Gamma$ by $M_{k}(\Gamma,\chi)$ and $S_{k}(\Gamma,\chi)$ respectively.

###### Theorem 1.1

Let $L$ be an integral lattice of signature $(2,n)$, $n\geq 9$, and let $\Gamma$ be a subgroup of finite index of $\mathrm{O}^{+}(L)$.
The modular variety $\mathcal{F}_{L}(\Gamma)$ is of general type if there exists a character $\chi$ of finite order and a non-zero cusp form $F_{a}\in S_{a}(\Gamma,\chi)$ of weight $a<n$ that vanishes along the branch divisor of the projection $\pi\colon\mathcal{D}_{L}\to\mathcal{F}_{L}(\Gamma)$.

If $S_{n}(\Gamma,\det)\neq 0$ then the Kodaira dimension of $\mathcal{F}_{L}(\Gamma)$ is non-negative.

Proof.
We let $\overline{\mathcal{F}}_{L}(\Gamma)$ be a toroidal compactification of $\mathcal{F}_{L}(\Gamma)$ with canonical singularities and no branch divisors at infinity, which exists by Theorem 2.1. We take a smooth projective model $\widehat{\mathcal{F}}_{L}(\Gamma)$ by taking a resolution of singularities of $\overline{\mathcal{F}}_{L}(\Gamma)$.

Suppose that $F_{nk}\in M_{nk}(\Gamma,\det^{k})$.
Then, if $dZ$ is a holomorphic volume element on $\mathcal{D}_{L}$, the differential form $\Omega(F_{nk})=F_{nk}\,(dZ)^{k}$ is $\Gamma$-invariant and therefore determines a section of the pluricanonical bundle $kK=kK_{\widehat{\mathcal{F}}_{L}(\Gamma)}$ away from the branch locus of $\pi\colon\mathcal{D}_{L}\to\mathcal{F}_{L}(\Gamma)$ and the cusps.

In general $\Omega(F_{nk})$ will not extend to a global section of $kK$.
We distinguish three kinds of obstruction to its doing so.
There are elliptic obstructions, arising because of singularities given by elliptic fixed points of the action of $\Gamma$; reflective obstructions, arising from the branch divisors in $\mathcal{D}_{L}$ (divisors fixed pointwise by an element of $\Gamma$ acting locally as a quasi-reflection); and cusp obstructions, arising from divisors at infinity.

In this situation the elliptic obstruction vanishes (and there are no elliptic or reflective obstructions at infinity either) because of the choice of $\overline{\mathcal{F}}_{L}(\Gamma)$.
So $\Omega(F_{nk})$ will extend to a section of $kK$ provided it extends to a general point of each branch divisor and each boundary divisor.

We apply the low-weight cusp form trick, used for example in _[x10]_, _[x12]_, _[x13]_ to show that the cusp obstruction for continuation of the pluricanonical forms on a smooth compactification is small compared with the dimension of $S_{nk}(\Gamma,\det^{k})$.
Let $N$ be the order of $\chi$ and put $k=2Nl$.
Then we consider special elements $F_{nk}^{0}\in S_{nk}(\Gamma)$ of the form

$F_{nk}^{0}=F_{a}^{k}F_{(n-a)k}$ (7)

where $F_{(n-a)k}\in M_{(n-a)k}(\Gamma)$ is a modular form of weight $(n-a)k\geq k$.
The corresponding differential form $\Omega(F_{nk}^{0})$ vanishes to order at least $k$ on the boundary of the toroidal compactification $\overline{\mathcal{F}}_{L}(\Gamma)$.
It follows by the results of _[x2]_ that $\Omega(F_{nk}^{0})$ extends as a $k$-fold pluricanonical form to the generic point of any boundary divisor of $\overline{\mathcal{F}}_{L}(\Gamma)$.
The reason is that the anticanonical divisor of a toric variety is the sum of the torus-invariant divisors, so $dZ$ has simple poles at all boundary divisors in a toroidal compactification.

Since $F_{a}$ vanishes at the branch divisors, which are the fixed divisors of reflections by Theorem 2.12, $\Omega(F^{0}_{nk})$ vanishes there to order $k$, and hence it extends to give a section of $kK$ over $\widehat{\mathcal{F}}_{L}(\Gamma)$.

Finally, we observe that this gives us an injective map

$M_{(n-a)k}(\Gamma)\hookrightarrow H^{0}(\widehat{\mathcal{F}}_{L}(\Gamma)).$

But $\dim M_{(n-a)k}(\Gamma)\sim k^{n}$, as can be seen from _[x1]_: a more precise estimate, using the results of _[x14]_, can be found in _[x7]_.
Hence it follows that $\mathcal{F}_{L}(\Gamma)$ is of general type.

Even if we can only find a cusp form of weight $n$ we still get some information, because of the well-known result of Freitag that if $F_{n}\in S_{n}(\Gamma,\det)$ then $\Omega(F_{n})$ defines an element of $H^{0}(K_{\widehat{\mathcal{F}}_{L}(\Gamma)})$.
Therefore the plurigenera do not all vanish: indeed $p_{g}\geq 1$.
∎

## 2 Singularities of locally symmetric varieties

In this section, we consider the singularities of compactified locally symmetric varieties associated with the orthogonal group of a lattice of signature $(2,n)$.
Our main theorem is that for all but small $n$, the compactification may be chosen to have canonical singularities.

###### Theorem 2.1

Let $L$ be a lattice of signature $(2,n)$ with $n\geq 9$, and let $\Gamma<\mathrm{O}^{+}(L)$ be a subgroup of finite index. Then there exists a toroidal compactification $\overline{\mathcal{F}}_{L}(\Gamma)$ of $\mathcal{F}_{L}(\Gamma)=\Gamma\backslash\mathcal{D}_{L}$ such that $\overline{\mathcal{F}}_{L}(\Gamma)$ has canonical singularities and there are no branch divisors in the boundary.
The branch divisors in $\mathcal{F}_{L}(\Gamma)$ arise from the fixed divisors of reflections.

###### Proof.

Immediate from Corollaries 2.16, 2.21 and 2.31. The last part is a summary of Theorem 2.12 (an element that fixes a divisor in $\mathcal{D}_{L}$ has order $2$ on the tangent space) and Corollary 2.13 (such elements, up to sign, are given by reflections by vectors in $L$).
∎

In fact we prove more than this: for example, $\mathcal{F}_{L}(\Gamma)$ has canonical singularities if $n\geq 7$ (Corollary 2.16), and our method (which uses ideas from _[x17]_) gives some information about what non-canonical singularities can occur for small $n$.
In order to choose $\overline{\mathcal{F}}_{L}(\Gamma)$ as in Theorem 2.1 it is enough to take all the fans defining the toroidal compactification to be basic.

### 2.1 The interior

For $[\mathbf{w}]\in\mathcal{D}_{L}$ we define $\mathbb{W}=\mathbb{C}.\mathbf{w}$.
We put $S=(\mathbb{W}\oplus\overline{\mathbb{W}})^{\perp}\cap L$, noting that $S$ could be $\{0\}$, and take $T=S^{\perp}\subset L$.

In the case of polarised K3 surfaces, $S$ is the primitive part of the Picard lattice and $T$ is the transcendental lattice of the surface corresponding to the period point $\mathbf{w}$.

###### Lemma 2.2

$S_{\mathbb{C}}\cap T_{\mathbb{C}}=\{0\}$.

Proof.
$S_{\mathbb{C}}$ and $T_{\mathbb{C}}$ are real (i.e. preserved by complex conjugation) so it is enough to show that $S_{\mathbb{R}}\cap T_{\mathbb{R}}=\{0\}$.
If $\mathbf{x}\in T_{\mathbb{R}}\cap S_{\mathbb{R}}$ then $(\mathbf{x},\mathbf{x})=0$ from the definition of $T$, so it is enough to prove that $S_{\mathbb{R}}$ is negative definite.
The subspace $\mathbb{U}=\mathbb{W}\oplus\overline{\mathbb{W}}\subset L_{\mathbb{C}}$ is also real, so we may write $\mathbb{U}=U_{\mathbb{R}}\otimes\mathbb{C}$, taking $U_{\mathbb{R}}$ to be the real vector subspace of $\mathbb{U}$ fixed pointwise by complex conjugation.
An $\mathbb{R}$-basis for $U_{\mathbb{R}}$ is given by $\{\mathbf{w}+\bar{\mathbf{w}},i(\mathbf{w}-\bar{\mathbf{w}})\}$.
But $(\mathbf{w}+\bar{\mathbf{w}},\mathbf{w}+\bar{\mathbf{w}})>0$ and $(i(\mathbf{w}-\bar{\mathbf{w}}),i(\mathbf{w}-\bar{\mathbf{w}}))>0$, so $U_{\mathbb{R}}$ has signature $(2,0)$.
Hence $U_{\mathbb{R}}^{\perp}$ has signature $(0,n)$, but $S_{\mathbb{R}}\subset U_{\mathbb{R}}^{\perp}$ so $S_{\mathbb{R}}$ is negative definite.
$\Box$

We are interested first in the singularities that arise at fixed points of the action of $\Gamma$ on $\mathcal{D}_{L}$.
Suppose then that $\mathbf{w}\in L_{\mathbb{C}}$ and let $G$ be the stabiliser of $[\mathbf{w}]$ in $\Gamma$.
Then $G$ acts on $\mathbb{W}$ and we let $G_{0}$ be the kernel of this action: thus for $g\in G$ we have $g(\mathbf{w})=\alpha(g)\mathbf{w}$ for some homomorphism $\alpha\colon G\to\mathbb{C}^{*}$, and $G_{0}=\ker\alpha$.

###### Lemma 2.3

$G$ acts on $S$ and on $T$.

Proof.
$G$ acts on $\mathbb{W}$ and on $L$, hence also on $S=(\mathbb{W}\oplus\overline{\mathbb{W}})^{\perp}\cap L$ and on $T=S^{\perp}\cap L$.
$\Box$

###### Lemma 2.4

$G_{0}$ acts trivially on $T_{\mathbb{Q}}$.

Proof.
If $\mathbf{x}\in T_{\mathbb{Q}}$ and $g\in G_{0}$ then

$(\mathbf{w},\mathbf{x})=(g(\mathbf{w}),g(\mathbf{x}))=(\mathbf{w},g(\mathbf{x})).$

Hence $T_{\mathbb{Q}}\ni\mathbf{x}-g(\mathbf{x})\in L_{\mathbb{Q}}\cap(\mathbb{W}\oplus\overline{\mathbb{W}})=S_{\mathbb{Q}}$, so by Lemma 2.2 we have $g(\mathbf{x})=\mathbf{x}$.
$\Box$

The quotient $G/G_{0}$ is a subgroup of $\mathrm{Aut}\,\mathbb{W}\cong\mathbb{C}^{*}$ and is thus cyclic of some order, which we call $r_{\mathbf{w}}$.
So by the above, $\mu_{r_{\mathbf{w}}}\cong G/G_{0}$ acts on $T_{\mathbb{Q}}$.
(By $\mu_{r}$ we mean the group of $r$th roots of unity in $\mathbb{C}$.)

For any $r\in\mathbb{N}$ there is a unique faithful irreducible representation of $\mu_{r}$ over $\mathbb{Q}$, which we call $\mathcal{V}_{r}$.
The dimension of $\mathcal{V}_{r}$ is $\varphi(r)$, where $\varphi$ is the Euler $\varphi$ function and, by convention, $\varphi(1)=\varphi(2)=1$.
The eigenvalues of a generator of $\mu_{r}$ in this representation are precisely the primitive $r$th roots of unity: $\mathcal{V}_{1}$ is the 1-dimensional trivial representation.
Note that $-\mathcal{V}_{d}=\mathcal{V}_{d}$ if $d$ is even and $-\mathcal{V}_{d}=\mathcal{V}_{2d}$ if $d$ is odd.

Proof.

###### Lemma 2.5

As a $G/G_{0}$-module, $T_{\mathbb{Q}}$ splits as a direct sum of irreducible representations $\mathcal{V}_{r_{\mathbf{w}}}$.
In particular, $\varphi(r_{\mathbf{w}})|\dim T_{\mathbb{Q}}$.

Proof.
We must show that no nontrivial element of $G/G_{0}$ has $1$ as an eigenvalue on $T_{\mathbb{C}}$.
Suppose that $g\in G\setminus G_{0}$ (so $\alpha(g)\neq 1$) and that $g(\mathbf{x})=\mathbf{x}$ for some $\mathbf{x}\in T_{\mathbb{C}}$.
Then

$(\mathbf{w},\mathbf{x})=(g(\mathbf{w}),g(\mathbf{x}))=\alpha(g)(\mathbf{w},\mathbf{x}),$

so $(\mathbf{w},\mathbf{x})=0$, so $\mathbf{x}\in S_{\mathbb{C}}\cap T_{\mathbb{C}}=0$.
$\Box$

###### Corollary 2.6

If $g\in G$ and $\alpha(g)$ is of order $r$ (so $r|r_{\mathbf{w}}$), then $T_{\mathbb{Q}}$ splits as a $g$-module into a direct sum of irreducible representations $\mathcal{V}_{r}$ of dimension $\varphi(r)$.

Proof.
Identical to the proof of Lemma 2.5. $\Box$

We are interested in the action of $G$ on the tangent space to $\mathcal{D}_{L}$.
We have a natural isomorphism

$T_{[\mathbf{w}]}\mathcal{D}_{L}\cong\operatorname{Hom}(\mathbb{W},\mathbb{W}^{\perp}/\mathbb{W})=:V.$

We choose $g\in G$ of order $m$ and put $\zeta=e^{2\pi i/m}$ for convenience: as $g$ is arbitrary there is no loss of generality.
Let $r$ be the order of $\alpha(g)$, as in Corollary 2.6 (this is called $m$ in _[x12]_ but we want to keep the notation of _[x10]_).
In particular $r|m$.
The eigenvalues of $g$ on $V$ are powers of $\zeta$, say $\zeta^{a_{1}},\ldots,\zeta^{a_{n}}$, with $0\leq a_{i}<m$.
We define

$\Sigma(g):=\sum_{i=1}^{n}a_{i}/m.$ (8)

Recall that an element of finite order in $\operatorname{GL}_{n}(\mathbb{C})$ (for any $n$) is called a quasi-reflection if all but one of its eigenvalues are equal to $1$.
It is called a reflection if the remaining eigenvalue is equal to $-1$.
The branch divisors of $\mathcal{D}_{L}\to\mathcal{F}_{L}(\Gamma)$ are precisely the fixed loci of elements of $\Gamma$ acting as quasi-reflections.

###### Proposition 2.7

Assume that $g\in G$ does not act as a quasi-reflection on $V$ and that $\varphi(r)>4$.
Then $\Sigma(g)\geq 1$.

Proof.
As $\xi$ runs through the $m$th roots of unity, $\xi^{m/r}$ runs through the $r$th roots of unity.
We denote by $k_{1},\ldots,k_{\varphi(r)}$ the integers such that $0<k_{i}<r$ and $(k_{i},r)=1$, in no preferred order.
Without loss of generality, we assume $\alpha(g)=\zeta^{mk_{2}/r}$ and $\overline{\alpha(g)}=\alpha(g)^{-1}=\zeta^{mk_{1}/r}$, with $k_{1}\equiv-k_{2}\bmod r$.

One of the $\mathbb{Q}$-irreducible subrepresentations of $g$ on $L_{\mathbb{C}}$ contains the eigenvector $\mathbf{w}$: we call this $\mathbb{V}_{r}^{\mathbf{w}}$ (it is the smallest $g$-invariant complex subspace

of $L_{\mathbb{C}}$ that is defined over $\mathbb{Q}$ and contains $\mathbf{w})$.
It is a copy of $\mathcal{V}_r \otimes \mathbb{C}$: to distinguish it from other irreducible subrepresentations of the same type we write $\mathbb{V}_r^{\mathbf{w}} = \mathcal{V}_r^{\mathbf{w}} \otimes \mathbb{C}$.

If $\mathbf{v}$ is an eigenvector for $g$ with eigenvalue $\zeta^{mk_i / r}$, $i \neq 1$ (in particular $\mathbf{v} \notin \overline{\mathbb{W}}$), then $\mathbf{v} \in \mathbb{W}^{\perp}$ since $(\mathbf{v}, \mathbf{w}) = (g(\mathbf{v}), g(\mathbf{w})) = \zeta^{mk_i / r} \alpha(g)(\mathbf{v}, \mathbf{w})$.
Therefore the eigenvalues of $g$ on $\mathbb{V}_r^{\mathbf{w}} \cap \mathbb{W}^{\perp} / \mathbb{W}$ include $\zeta^{mk_i / r}$ for $i \geq 3$, so the eigenvalues on $\mathrm{Hom}(\mathbb{W}, \mathbb{V}_r^{\mathbf{w}} \cap \mathbb{W}^{\perp} / \mathbb{W}) \subset V$ include $\zeta^{mk_1 / r} \zeta^{mk_i / r}$ for $i \geq 3$.
So, writing $\{a\}$ for the fractional part of $a$, we have

$$
\begin{array}{l}
\Sigma (g) \geq \sum_ {i = 3} ^ {\varphi (r)} \frac {1}{m} \left\{\frac {m k _ {1}}{r} + \frac {m k _ {i}}{r} \right\} \\
= \sum_ {i = 3} ^ {\varphi (r)} \left\{\frac {k _ {1} + k _ {i}}{r} \right\}. \tag {9}
\end{array}
$$

Now the proposition follows from the elementary Lemma 2.8 below.

Lemma 2.8 Suppose $k_{1}, \ldots, k_{\varphi(r)}$ are the integers between 0 and $r$ coprime to $r$, in some order, and that $k_{2} = r - k_{1}$.
If $\varphi(r) \geq 6$ then

$$
\sum_ {i = 3} ^ {\varphi (r)} \left\{\frac {k _ {1}}{r} + \frac {k _ {i}}{r} \right\} \geq 1.
$$

Proof.
If $k_{1} &lt; k_{3} &lt; r / 2$ then $\left\{\frac{k_1 + k_3}{r}\right\} = \frac{k_1 + k_3}{r}$, and $k_{4} = r - k_{3}$ so $\left\{\frac{k_1 + k_4}{r}\right\} = \frac{k_1 + r - k_3}{r}$.
Thus

$$
\left\{\frac {k _ {1} + k _ {3}}{r} \right\} + \left\{\frac {k _ {1} + k _ {4}}{r} \right\} = \frac {2 k _ {1} + r}{r} &gt; 1.
$$

If $r / 2 &gt; k_{1} &gt; r / 4$ or $r &gt; k_{1} &gt; 3r / 4$ then $(k_{1} + k_{3}) + (k_{1} + k_{4}) \equiv 2k_{1} \bmod r$, so

$$
\left\{\frac {k _ {1} + k _ {3}}{r} \right\} + \left\{\frac {k _ {1} + k _ {4}}{r} \right\} \equiv \frac {2 k _ {1}}{r} \bmod 1.
$$

Therefore $\left\{\frac{k_1 + k_3}{r}\right\} + \left\{\frac{k_1 + k_4}{r}\right\} &gt; \frac{1}{2}$, and similarly for $\left\{\frac{k_1 + k_5}{r}\right\} + \left\{\frac{k_1 + k_6}{r}\right\}$, so the sum is at least 1.

If $r/2 &lt; k_1 &lt; 3r/4$ then we may take $k_3 = 1$ and $k_4 = r - 1$, and then $\left\{\frac{k_1 + k_3}{r}\right\} + \left\{\frac{k_1 + k_4}{r}\right\} = 1 + \frac{2k_1}{r} &gt; 1$.

The remaining possibility is that $k_{1} &lt; r / 4$ but $k_{1} &gt; k_{j}$ if $k_{j} &lt; r / 2$.
But then there is no integer coprime to $r$ between $r / 4$ and $3r / 4$.
As long as $2\lceil r / 4\rceil &lt; \lfloor 3r / 4\rfloor$, which is true if $r &gt; 9$, we may choose a prime $q$ such that $r / 4 &lt; q &lt; 3r / 4$, by Bertrand's Postulate [HW, Theorem 418], and $\gcd (q,r)\neq 1$ so $r = 2q$ or $r = 3q$.
In the first case one of $q\pm 2$ lies in

9

$(r/4,3r/4)$ and is prime to $r$, and in the second case one of $q \pm 1$ or $q \pm 2$ does, unless $r &lt; 8$; so this possibility does not occur.
The cases $r = 7$ and $r = 9$, which are not covered by this argument, are readily checked: $2 \in (7/4,21/4)$ and $4 \in (9/4,27/4)$ are coprime to $r$.

**Proposition 2.9** Assume that $g \in G$ does not act as a quasi-reflection on $V$ and that $r = 1$ or $r = 2$.
Then $\Sigma(g) \geq 1$.

**Proof.** We note first that we may assume $g$ is not of order 2, because if $g^2$ acts trivially on $V$ but $g$ is not a quasi-reflection then at least two of the eigenvalues of $g$ on $V$ are $-1$, and hence $\sum_{i=1}^{n} a_i / m \geq 1$.
However, $g^2$ does act trivially on $T_{\mathbb{C}}$, by Corollary 2.6. Therefore $g^2$ does not act trivially on $S_{\mathbb{C}}$.
The representation of $g$ on $S_{\mathbb{C}}$ therefore splits over $\mathbb{Q}$ into a direct sum of irreducible subrepresentations $\mathcal{V}_d$, and at least one such piece has $d &gt; 2$.
So on the subspace $\mathrm{Hom}(\mathbb{W}, \mathcal{V}_d \otimes \mathbb{C}) = \mathrm{Hom}(\mathbb{W}, (\mathcal{V}_d \otimes \mathbb{C} \oplus \mathbb{W}) / \mathbb{W}) \subset V$, the representation of $g$ is $\pm \mathcal{V}_d$ (the sign depending on whether $r = 1$ or $r = 2$), and choosing two conjugate eigenvalues $\pm \zeta^a$ and $\pm \zeta^{m - a}$ we have $\sum a_i / m \geq 1$.

**Theorem 2.10** Assume that $g \in G$ does not act as a quasi-reflection on $V$ and that $n \geq 6$.
Then $\Sigma(g) \geq 1$.

**Proof.** In view of Proposition 2.9 and Proposition 2.7, we need only consider $r = 3, 4, 5, 6, 8, 10$ or 12. We suppose, as before, that $g$ has order $m$, and we put $k = m / r$.

Consider first a $\mathbb{Q}$-irreducible subrepresentation $\mathcal{V}_d \subset S_{\mathbb{C}}$, and the action of $g$ on $\mathrm{Hom}(\mathbb{W}, \mathcal{V}_d \otimes \mathbb{C}) \subset V$.
This is $\zeta^{kc} \mathcal{V}_d$, where $\zeta$ is a primitive $m$th root of unity, and $c$ is some integer with $0 &lt; c &lt; r$ and $(c, r) = 1$ (the eigenvalue of $g$ on $\mathbb{W}$ is $\zeta^{-kc}$).
So the eigenvalues are of the form $\zeta^{b_i / m}$ for $1 \leq i \leq \varphi(d)$, with $0 \leq b_i &lt; m$ and the $b_i$ all different mod $m$ but all equivalent mod $l$, where $l = m / d$.
Clearly

$$
\sum_{i=1}^{\varphi(d)} \frac{b_i}{m} \geq \frac{1}{2m} l(\varphi(d) - 1)\varphi(d) = \frac{1}{2d}(\varphi(d) - 1)\varphi(d)
$$

and it is easy to see that this is $\geq 1$ unless $d \in \{1, \ldots, 6, 8, 10, 12, 18, 30\}$.

By a slightly less crude estimate we can reduce further.
For $d &gt; 2$ we write $c_{\min}(d)$ for a lower bound for the contribution to the sum $\Sigma(g)$ from $\mathcal{V}_d$ as a subrepresentation of $g$ on $S_{\mathbb{C}}$, i.e.

$$
c_{\min}(d) = \min_{0 \leq a &lt; d} \sum_{0 &lt; b &lt; d, (d, b) = 1} \left\{ \frac{b + a}{d} \right\}.
$$

Note that this is a lower bound independently of $r$.
For fixed $r$ one has a contribution to $\Sigma(g)$ from $\mathcal{V}_d$ of at most

$$
\begin{array}{l}
\min_{0 &lt; c &lt; r} \sum_{0 &lt; b &lt; d, (d, b) = 1} \left\{ \frac{bl + kc}{m} \right\} = \min_{0 &lt; c &lt; r} \sum_{0 &lt; b &lt; d, (d, b) = 1} \left\{ \frac{b}{d} + \frac{kc}{m} \right\} \\
\geq \min_{0 &lt; c &lt; r} \sum_{0 &lt; b &lt; d, (d, b) = 1} \left\{ \frac{b}{d} + \frac{|kc / l|}{d} \right\} \\
\geq c_{\min}(d).
\end{array}
$$

It is easy to calculate that $c_{\mathrm{min}}(30) = 92 / 30$ (attained when $a = 19$), $c_{\mathrm{min}}(18) = 42 / 18$, $c_{\mathrm{min}}(12) = 16 / 12$, $c_{\mathrm{min}}(10) = 12 / 10$, $c_{\mathrm{min}}(8) = 12 / 8$ and $c_{\mathrm{min}}(5) = 6 / 5$.
But

$$
c_{\min}(3) = c_{\min}(6) = 1 / 3, \quad c_{\min}(4) = 1 / 2. \tag{10}
$$

Hence we may assume that $r \in \{3, 4, 5, 6, 8, 12\}$ and $d \in \{1, 2, 3, 4, 6\}$ for every subrepresentation $\mathcal{V} \otimes \mathbb{C} \subset S_{\mathbb{C}}$.
The summands of $T_{\mathbb{C}}$ are all $\mathcal{V}_r \otimes \mathbb{C}$.
We let $\nu_d$ be the multiplicity of $\mathcal{V}_d$ in $S_{\mathbb{C}}$ as a $g$-module, and $\lambda$ be the multiplicity of $\mathcal{V}_r$ in $T_{\mathbb{C}}$.
Counting dimensions gives

$$
\lambda \varphi(r) + \nu_1 + \nu_2 + 2\nu_3 + 2\nu_4 + 2\nu_6 = n + 2. \tag{11}
$$

We split into two cases, depending on whether $\varphi(r) = 4$ or $\varphi(r) = 2$.

Case I.
Suppose $\varphi(r) = 4$, so $r \in \{5, 8, 10, 12\}$.

If $\lambda &gt; 1$ then there will be a $\mathcal{V}_r \otimes \mathbb{C}$ not containing $\mathbb{W}$ and this will contribute at least $c_{\min}(r)$ to $\Sigma(g)$, just as if it were contained in $S_{\mathbb{C}}$ instead of $T_{\mathbb{C}}$.
For $r = 5, 8, 10$ or 12 we have $c_{\min}(r) \geq 1$, so we may assume that $\lambda = 1$.
Moreover in these cases $\varphi(r) = 4$, so equation (11) becomes

$$
\nu_1 + \nu_2 + 2\nu_3 + 2\nu_4 + 2\nu_6 = n - 2. \tag{12}
$$

We may assume that $\nu_4 \leq 1$ and $\nu_3 + \nu_6 \leq 2$, as otherwise those summands contribute at least 1 to $\Sigma(g)$, by equation (10).
The contribution from $\mathcal{V}_r^{\mathbf{w}}$ was computed in equation (9) above: for $\varphi(r) = 4$ it is $\frac{k_1 + k_3}{r} + \frac{k_1 + k_4}{r}$.
The contribution from a $\mathcal{V}_1$ (an invariant) is $\frac{k_1}{r}$ and from $\mathcal{V}_2$ (an anti-invariant) it is $\left\{\frac{k_1}{r} + \frac{1}{2}\right\}$.

Now we can compute all cases.
The contribution from a copy of $\mathcal{V}_d$ is

$$
\sum_{(a, d) = 1} \left\{ \frac{a}{d} + \frac{k_1}{r} \right\} \tag{13}
$$

or $\frac{k_1}{r}$ if $d = 1$.
Half the time ($k_1$ first or third in order of size) the contribution $c^{\mathbf{w}}$ from $\mathcal{V}_r^{\mathbf{w}}$ is already at least 1. In all cases it is at least $\frac{1}{2}$, so we may also assume that $\nu_4 = 0$.
In six of the remaining eight cases we get $\Sigma(g) \geq 1$

$L_{\mathbb{C}}=\mathbb{V}_{r}^{\mathbf{w}}$ and hence $n=2$: all other possible contributions are greater than $1-c^{\mathbf{w}}$.
The exceptions are $r=5$, $k_{1}=4$ and $r=10$, $k_{1}=3$.

For $r=5$, $k_{1}=4$, contributions from $\mathcal{V}_{r}^{\mathbf{w}}$, $\mathcal{V}_{1}$, $\mathcal{V}_{2}$, $\mathcal{V}_{3}$ and $\mathcal{V}_{6}$ are $\frac{3}{5}$, $\frac{4}{5}$, $\frac{3}{10}$, $\frac{3}{5}$ and $\frac{8}{5}$ respectively.
So $\Sigma(g)\geq 1$ unless $\nu_{1}=\nu_{3}=\nu_{6}=0$ and $\nu_{2}\leq 1$, and in particular $n\leq 3$.

For $r=10$, $k_{1}=3$, contributions from $\mathcal{V}_{r}^{\mathbf{w}}$, $\mathcal{V}_{1}$, $\mathcal{V}_{2}$, $\mathcal{V}_{3}$ and $\mathcal{V}_{6}$ are $\frac{3}{5}$, $\frac{3}{10}$, $\frac{8}{10}$, $\frac{6}{10}$ and $\frac{6}{10}$ respectively.
So $\Sigma(g)\geq 1$ unless $\nu_{2}=\nu_{3}=\nu_{6}=0$ and $\nu_{1}\leq 1$, and in particular $n\leq 3$.

Case II.
Suppose $\varphi(r)=2$, so $r\in\{3,4,6\}$.

In this case one summand of $L_{\mathbb{C}}$ as a $g$-module is the space $\mathbb{W}\oplus\overline{\mathbb{W}}$, which is $\mathbb{V}_{r}^{\mathbf{w}}$, a copy of $\mathcal{V}_{r}\otimes\mathbb{C}$.
We denote by $\nu_{d}$ the multiplicity of $\mathcal{V}_{d}$ in $L_{\mathbb{C}}/(\mathbb{W}\oplus\overline{\mathbb{W}})$ as a $g$-module.
Thus $\nu_{r}$ is the number of copies of $\mathcal{V}_{r}\otimes\mathbb{C}$ in $L_{\mathbb{C}}$ that are different from $\mathbb{V}_{r}^{\mathbf{w}}$.
Equation (11) becomes

$\nu_{1}+\nu_{2}+2\nu_{3}+2\nu_{4}+2\nu_{6}=n.$ (14)

There are six cases (three values of $r$, and $k_{1}=1$ or $k_{1}=r-1$) and we simply compute all contributions in each case using the expression (13).
For $1$-dimensional summands ($d=1$ or $2$) the lowest contribution is $\frac{1}{6}$ (for $r=3$, $k_{1}=2$, $d=2$ and for $r=6$, $k_{1}=1$ and $d=1$).
For $2$-dimensional summands the lowest contribution is $\frac{1}{3}$ (for $r=3$, $k_{1}=2$, $d=3$ and for $r=6$, $k_{1}=1$, $d=6$).
So $\Sigma(g)\geq 1$ unless $n\leq 5$.
$\Box$

###### Corollary 2.11

If $n\geq 6$, then the space $\mathcal{F}_{L}(\Gamma)$ has canonical singularities away from the branch divisors of $\mathcal{D}_{L}\to\mathcal{F}_{L}(\Gamma)$.

Proof.
This follows at once from the Reid–Shepherd-Barron–Tai criterion (RST criterion for short) for canonical singularities: see _[x13]_ or _[x16]_.
$\Box$

Remark.
It is easy to classify the types of canonical singularities that can occur for small $n$, by examining the calculations above.

So far we have not considered quasi-reflections.
We need to analyse not only quasi-relections themselves but also all elements some power of which acts as a quasi-reflection on $V$: note, however, that Theorem 2.10 does apply to such elements.

###### Theorem 2.12

Suppose $n>2$.
Let $g\in G$ and suppose that $h=g^{k}$ acts as a quasi-reflection on $V$.
Then, as a $g$-module, $L_{\mathbb{Q}}$ is either $\mathcal{V}_{k}\oplus\bigoplus_{j}\mathcal{V}_{2k}$ or $\mathcal{V}_{2k}\oplus\bigoplus_{j}\mathcal{V}_{k}$ (that is, one copy of $\mathcal{V}_{k}$ and some copies of $\mathcal{V}_{2k}$ or vice versa).
In particular, $h$ has order $2$.

Proof.
Suppose that $L_{\mathbb{Q}}$ decomposes as a $g$-module as $\mathcal{V}_{r}^{\mathbf{w}}\oplus\bigoplus_{i}\mathcal{V}_{d_{i}}$ for some sequence $d_{i}\in\mathbb{N}$.
The eigenvalues of $h$ on $V$ are all equal to $1$, with exactly one exception.
On the other hand, if $\zeta_{r}$ and $\zeta_{d_{i}}$ denote primitive

$d_{i}$th roots of unity, the eigenvalues of $h$ are certain powers of $\zeta_{r}$ (on $\mathrm{Hom}(\mathbb{W},\mathbb{V}_{r}^{\mathbf{w}}\cap\mathbb{W}^{\perp}/\mathbb{W})$) and all numbers of the form $\alpha(h)^{-1}\zeta_{d_{i}}^{ka}$ for $(a,d_{i})=1$.

Consider a $\mathcal{V}_{d}=\mathcal{V}_{d_{i}}$ and put $d^{\prime}=d/(k,d)$.
The eigenvalues of $h$ on $\mathcal{V}_{d}$ are primitive $d^{\prime}$th roots of unity: each one occurs with multiplicity exactly $\varphi(d)/\varphi(d^{\prime})$.
However, only two eigenvalues of $h$ may occur in any $\mathcal{V}_{d}$, and only one (namely $\alpha(h)$) may occur with multiplicity greater than $1$, since if $\xi$ is an eigenvalue of $h$ on $\mathcal{V}_{d}$, the eigenvalue $\alpha(h)^{-1}\xi$ occurs with the same multiplicity on $V$.
Hence $\varphi(d^{\prime})\leq 2$, and if $\varphi(d^{\prime})=2$ then $\varphi(d)=2$: this last can occur at most once.

Let us consider first the case where for some $d$ we have $\varphi(d)=\varphi(d^{\prime})=2$.
We claim that in this case $n=2$.
We must have $d=6$ and $(k,d)=2$, and therefore $\alpha(h)=\omega$, a primitive cube root of unity.
There can be no other $\mathcal{V}_{d}$ summands (i.e. summands not containing $\mathbb{W}$), because such a $\mathcal{V}_{d}$ would have $\varphi(d)=1$ and hence give rise to an eigenvalue $\pm\omega^{2}$ for $h$ on $V$; but the $\mathcal{V}_{6}$ already gives rise to an eigenvalue for $h$ on $V$ different from $1$.
So $L_{\mathbb{Q}}=\mathcal{V}_{r}^{\mathbf{w}}\oplus\mathcal{V}_{6}$.
The eigenvalues of $h$ on $\mathcal{V}_{r}^{\mathbf{w}}$ are $\omega$ and $\omega^{2}$, each with multiplicity $\varphi(r)/2$: so $\varphi(r)=2$, otherwise $h$ has the eigenvalue $\omega$ with multiplicity $>1$ on $V$.
Hence $\mathrm{rank}\,L=4$ and $n=2$.

Since we are assuming that $n\geq 6$, we have $\varphi(d^{\prime})=1$ for all $d$: that is, the eigenvalues of $h$ on the $\mathcal{V}_{d}$ part are all $\pm 1$.
Put $r^{\prime}=r/(k,r)$.
We claim that $\varphi(r^{\prime})=1$.

Suppose instead that $\varphi(r^{\prime})\geq 2$, so $\alpha(h)\neq\pm 1$.
Then $\varphi(r)/\varphi(r^{\prime})\leq 2$, since the multiplicity of $\alpha(h)^{-2}\neq 1$ as an eigenvalue of $h$ on $V$ is at least $\varphi(r)/\varphi(r^{\prime})-1$.
But the eigenvalues of $h$ on $\mathcal{V}_{r}^{\mathbf{w}}$ are the primitive $r^{\prime}$th roots of unity.
If $\varphi(r^{\prime})>2$ then these include $\alpha(h)$, $\alpha(h)^{-1}$, $\xi$ and $\xi^{-1}$ for some $\xi$, these being distinct.
But then the eigenvalues of $h$ on $V$ include $\alpha(h)^{-1}\xi$ and $\alpha(h)^{-1}\xi^{-1}$, neither of which is equal to $1$.
So $\varphi(r^{\prime})\leq 2$

Moreover, if $\varphi(r)/\varphi(r^{\prime})=2$ then $h$ has the eigenvalue $\alpha(h)^{-2}\neq 1$ on $V$, and any $\mathcal{V}_{d}$ will give rise to the eigenvalue $\pm\alpha(h)^{-1}\neq 1$; so no such components occur, and $L_{\mathbb{Q}}=\mathcal{V}_{r}^{\mathbf{w}}$.
Moreover, $\varphi(r)\leq 4$ so $n\leq 2$.

This shows that if $h$ is a quasi-reflection and $\varphi(r^{\prime})>1$ then $\varphi(r^{\prime})=2$; moreover if $n>2$ then $\varphi(r)=\varphi(r^{\prime})=2$.
Hence, if $\varphi(r^{\prime})>1$, we have $r=6$ and $(r,k)=2$, so again $\alpha(h)=\omega$, a primitive cube root of unity.
This time $\mathbb{W}\oplus\overline{\mathbb{W}}=\mathbb{V}_{r}^{\mathbf{w}}$, so the eigenvalues of $h$ on $V$ all arise from $\mathcal{V}_{d}$ and since $\varphi(d^{\prime})=1$ they are equal to $\pm\omega^{2}\neq 1$.
So there is only one of them, that is, $n=1$.

Since we suppose $n>2$, it follows that $\varphi(r^{\prime})=1$.
The theorem follows immediately from this.
$\Box$

###### Corollary 2.13

The quasi-reflections on $V$, and hence the branch divisors of $\mathcal{D}_{L}\to\mathcal{D}_{F}(\Gamma)$, are induced by elements $h\in\mathrm{O}(L)$ such that $\pm h$ is a reflection with respect to a vector in $L$.

Proof.
The two cases are distinguished by whether $\alpha(h)=\pm 1$.
If $\alpha(h)=1$

then the eigenvalues of $h$ on $L_{\mathbb{C}}$ are $+1$ with multiplicity $1$ and $-1$ with multiplicity $n+1$, so $-h$ is a reflection; if $\alpha(h)=-1$, they are the other way round.
$\Box$

Now suppose that $g\in G$ and that $g^{k}=h$ is a quasi-reflection, $k>1$.
By Theorem 2.12, $h$ has order $2$ so $g$ has order $2k$.
We may suppose that the eigenvalues of $g$ on $V$ are $\zeta^{a_{1}},\ldots,\zeta^{a_{n}}$, where $\zeta$ is a primitive $2k$th root of unity, $0\leq a_{i}<2k$, $a_{n}$ is odd and $a_{i}$ is even for $i<n$.

We need to look at the action of the group $\langle g\rangle/\langle h\rangle$ on $V^{\prime}:=V/\langle h\rangle$.
The eigenvalues of $g^{l}\langle h\rangle$ on $V^{\prime}$ are $\zeta^{la_{1}},\ldots,\zeta^{la_{n-1}},\zeta^{2la_{n}}$, and we define

$\Sigma^{\prime}(g^{l}):=\left\{\frac{la_{n}}{k}\right\}+\sum_{i=1}^{n-1}\left\{\frac{la_{i}}{2k}\right\}.$ (15)

###### Lemma 2.14

$\mathcal{F}_{L}(\Gamma)$ has canonical singularities if $\Sigma(g)\geq 1$ for every $g\in\Gamma$ no power of which is a quasi-reflection, and $\Sigma^{\prime}(g^{l})\geq 1$ if $g^{k}=h$ is a quasi-reflection and $1\leq l<k$.

Proof.
It is easy to see that if $V/\langle g\rangle$ has canonical singularities for every $g\in G$ then $V/G$ has canonical singularities (the converse is false).
This follows from the fact that a $G$-invariant form extends to a resolution of $V/G$ if and only if it extends to a resolution of every $V/\langle g\rangle$, which is [T, Proposition 3.1].

If no power of $g$ is a quasi-reflection on $V$ we simply apply the RST criterion.
Otherwise, consider $g$ with $g^{k}=h$ a quasi-reflection as above.
By Corollary 2.13, $V^{\prime}$ is smooth, and $V/\langle g\rangle\cong V^{\prime}/(\langle g\rangle/\langle h\rangle)$.
So the result follows by applying the RST criterion to the elements $g^{l}\langle h\rangle$ acting on $V^{\prime}$.
$\Box$

###### Proposition 2.15

If $g^{k}=h$ is a quasi-reflection and $n\geq 7$ then $\Sigma^{\prime}(g^{l})\geq 1$ for every $1\leq l<k$.

Proof.
In fact we shall show that $\sum_{i=1}^{n-1}\{\frac{la_{i}}{2k}\}\geq 1$.
As in Corollary 2.13 we have $\alpha(h)=\pm 1$ and this is a primitive $r^{\prime}$th root of unity; so all the eigenvalues of $h$ on $\mathcal{V}_{r}^{\mathbf{w}}$ are equal to $\alpha(h)$.
Here, as usual, $\mathbb{W}\oplus\overline{\mathbb{W}}\subset\mathbb{V}_{r}^{\mathbf{w}}$ (two copies of $\mathcal{V}_{r}\otimes\mathbb{C}$ if $r|2$) and we have decomposed $L_{\mathbb{C}}$ as a $g$-module into $\mathbb{Q}$-irreducible pieces.
But exactly one eigenvalue of $h$ on $L_{\mathbb{C}}$ is $-\alpha(h)=\mp 1$, and this must occur on some summand $\mathcal{V}_{d}$.

The eigenvalues of $g$ on $\mathcal{V}_{d}$ are primitive $d$th roots of unity, and in particular they all have the same order.
Therefore the eigenvalues of $h$ are either all equal to $1$ (if $\alpha(h)=-1$ and $d|k$) or all equal to $-1$ (if $\alpha(h)=1$ and $d|2k$ but $d$ does not divide $k$).
Since the eigenvalue $-\alpha(h)$ on $L_{\mathbb{C}}$ has multiplicity $1$, it follows that $\varphi(d)=1$, i.e. $d=1$ or $d=2$.

The eigenvector in $V$ corresponding to $\zeta^{a_{n}}$ comes from $\mathcal{V}_{d}$, i.e. its span is the space $\mathrm{Hom}(\mathbb{W},\mathcal{V}_{d}\otimes\mathbb{C})\subset V$.
If we choose a primitive generator $\delta$ of

$\mathcal{V}_{d}\cap L$ we have $\delta^{2}<0$ since $\mathcal{V}_{d}\subset U_{\mathbb{Q}}^{\perp}$ as in Lemma 2.2, so $L^{\prime}=\delta^{\perp}$ is of signature $(2,n-1)$ and $\langle g\rangle/\langle h\rangle$ acts on $L^{\prime}$ as a subgroup of $\mathrm{O}^{+}(L^{\prime})$.
But then $\Sigma^{\prime}(g^{l})=\{\frac{la_{n}}{k}\}+\Sigma(g^{l}\langle h\rangle)$ where $g^{l}\langle h\rangle\in\mathrm{O}^{+}(L^{\prime})$.
It is clear that $g^{l}\langle h\rangle$ cannot be a quasi-reflection on $L^{\prime}$: if it were, then by Corollary 2.13 the eigenvalues of $g^{l}$ on $L^{\prime}$ are all $\pm 1$, and so is its eigenvalue on $\mathcal{V}_{d}$, so it has order dividing $2$; so $g^{l}\in\langle h\rangle$.

Now we apply Theorem 2.10 to $L^{\prime}$, using $n-1\geq 6$.
$\Box$

###### Corollary 2.16

If $n\geq 7$ then $\mathcal{F}_{L}(\Gamma)$ has canonical singularities.

### 2.2 Dimension $0$ cusps

We now consider the boundary $\overline{\mathcal{F}}_{L}(\Gamma)\setminus\mathcal{F}_{L}(\Gamma)$.
Boundary components in the Baily-Borel compactification correspond to totally isotropic subspaces $E\subset L_{\mathbb{Q}}$.
Since $L$ has signature $(2,n)$, the dimension of $E$ is $1$ or $2$, corresponding to dimension $0$ and dimension $1$ boundary components respectively.
In this section we consider the case $\dim E=1$, that is, isotropic vectors in $L$.

For a cusp $F$ (of any dimension) we denote by $U(F)$ the unipotent radical of the stabiliser subgroup $N(F)\subset\Gamma_{\mathbb{R}}$ and by $W(F)$ its centre.
We let $N(F)_{\mathbb{C}}$ and $U(F)_{\mathbb{C}}$ be the complexifications and put $N(F)_{\mathbb{Z}}=N(F)\cap\Gamma$ and $U(F)_{\mathbb{Z}}=U(F)\cap\Gamma$.

A toroidal compactification over a $0$-dimensional cusp $F$ coming from a $1$-dimensional isotropic subspace $E$ corresponds to an admissible fan $\Sigma$ in some cone $C(F)\subset U(F)$.
We have, as in _[x1]_

$\mathcal{D}_{L}(F)=U(F)_{\mathbb{C}}\mathcal{D}_{L}\subset\dot{\mathcal{D}}_{L}$

and in this case

$\mathcal{D}_{L}(F)\cong F\times U(F)_{\mathbb{C}}=U(F)_{\mathbb{C}}.$

Put $M(F)=U(F)_{\mathbb{Z}}$ and define the torus $\mathbf{T}(F)=U(F)_{\mathbb{C}}/M(F)$.
In general $(\mathcal{D}_{L}/M(F))_{\Sigma}$ is by definition the interior of the closure of $\mathcal{D}_{L}/M(F)$ in $\mathcal{D}_{L}(F)/M(F)\times_{\mathbf{T}(F)}X_{\Sigma}(F)$, i.e. in $X_{\Sigma}(F)$ in this case, where $X_{\Sigma}(F)$ is the torus embedding corresponding to the torus $\mathbf{T}(F)$ and the fan $\Sigma$.
We may choose $\Sigma$ so that $X_{\Sigma}(F)$ is smooth and $G(F):=N(F)_{\mathbb{Z}}/U(F)_{\mathbb{Z}}$ acts on $(\mathcal{D}_{L}/M(F))_{\Sigma}$.
The toroidal compactification is locally isomorphic to $X_{\Sigma}(F)/G(F)$.
Thus the problem of determining the singularities is reduced to a question about toric varieties.
The result we want will follow from Theorem 2.17, below.
We also need to consider possible fixed divisors in the boundary.

We take a lattice $M$ of dimension $n$ and denote its dual lattice by $N$.
A fan $\Sigma$ in $N\otimes\mathbb{R}$ determines a toric variety $X_{\Sigma}$ with torus $\mathbf{T}=\mathrm{Hom}(M,\mathbb{C}^{*})=N\otimes\mathbb{C}^{*}$.

###

###### Theorem 2.17

Let $X_{\Sigma}$ be a smooth toric variety and suppose that a finite group $G<\mathrm{Aut}(\mathbf{T})=\mathrm{GL}(M)$ of torus automorphisms acts on $X_{\Sigma}$.
Then $X_{\Sigma}/G$ has canonical singularities.

###### Proof.

It is enough to show that for each $x\in X_{\Sigma}$ and for each $g\in\mathrm{Stab}_{G}(x)$, the quotient $X_{\Sigma}/\langle g\rangle$ has canonical singularities at $x$.

We consider the subtorus $\mathbf{T}_{0}=\mathrm{Stab}_{\mathbf{T}}(x)$ of $\mathbf{T}$, which is given by $\mathbf{T}_{0}=N_{0}\otimes\mathbb{C}^{*}$ for some sublattice $N_{0}\subset N$, and the quotient torus $\mathbf{T}_{1}=\mathbf{T}/\mathbf{T}_{0}$.
The orbit $\mathrm{orb}(x)=\mathbf{T}.x$ of $x$ is isomorphic to $\mathbf{T}_{1}$: it corresponds to a cone $\sigma\in\Sigma$ of dimension

$s=\dim\sigma=\dim\mathbf{T}_{1}=\mathrm{codim}\,\mathrm{orb}(x),$

and $N_{0}$ is the lattice generated by $\sigma\cap N$.
More explicitly, $\mathrm{orb}(x)$ is given locally near $x$ by the equations $\xi_{i}=0$, where $\xi_{i}$ are coordinates on $\mathbf{T}_{0}$.
The quotient torus $\mathbf{T}_{1}$ is naturally isomorphic to $N_{1}\otimes\mathbb{C}^{*}$, where $N_{1}=N/N_{0}$ which is a lattice because $X_{\Sigma}$ is smooth.

Certainly $x$ determines $\mathrm{orb}(x)$ and therefore $\sigma$, so $g$ stabilises $\sigma$.
If $U_{\sigma}=\mathrm{Hom}(M\cap\hat{\sigma},\mathbb{C}^{*})$ (semigroup homomorphisms) is the corresponding $\mathbf{T}$-invariant open set, then $U_{\sigma}$ is $g$-invariant and the tangent spaces to $U_{\sigma}$ and to $X_{\Sigma}$ at $x$ are the same: we denote this tangent space by $V$.
Choosing a basis for $N_{0}$ and extending it to a basis for $N$ gives an isomorphism of $U_{\sigma}$ with $\mathbb{C}^{s}\times(\mathbb{C}^{*})^{n-s}$ (compare _[x18, Theorem 1.1.10]_).
Since $g$ preserves $N_{0}$ it acts on both factors, by permuting the coordinates and by torus automorphisms respectively.
Thus

$V=(N_{0}\otimes\mathbb{C})\oplus\mathrm{Lie}(\mathbf{T}_{1})=(N_{0}\otimes\mathbb{C})\oplus(N_{1}\otimes\mathbb{C})=V_{0}\oplus V_{1}$

as a $g$-module, which is thus defined over $\mathbb{Q}$.

Since $V$ is defined over $\mathbb{Q}$, we may decompose it as a direct sum of $\mathcal{V}_{d}$s as a $g$-module, with each $d$ dividing $m$, the order of $g$.

Note that if $g$ acts as a quasi-reflection, with eigenvalues $(1,\ldots,1,\zeta)$ then since $g\in\mathrm{GL}(N)=\mathrm{GL}_{n}(\mathbb{Z})$ we have $\mathrm{tr}(g)=\zeta+n-1\in\mathbb{Z}$, and therefore $\zeta=-1$ and $g$ is a reflection.

We define $\Sigma(g)$ as we did in equation (8) above, and in the event that some power of $g$, say $h=g^{k}$, acts as a quasi-reflection we define $V^{\prime}=V/\langle h\rangle$ and $\Sigma^{\prime}(g^{l})$ as we did in equation (15).
Now the theorem follows from Proposition 2.18 and Proposition 2.19, below.
∎

Note that we only needed to choose $\Sigma$ smooth: no further subdivision is necessary.

A version of Theorem 2.17 is stated in _[x20]_ and proved in _[x21]_.
There the variety $X_{\Sigma}$ is itself allowed to have canonical singularities, but $G$ is assumed to act freely in codimension 1.

###### Proposition 2.18

If $g\in G$ is not the identity, then unless $g$ acts as a reflection, $\Sigma(g)\geq 1$.

Proof.
If $V$ contains a $\mathcal{V}_{d}$ with $\varphi(d)>1$ then $g$ has a conjugate pair of eigenvalues and they contribute $1$ to $\Sigma(g)$.
The same is true if $V$ contains two copies of $\mathcal{V}_{2}$.
If neither of these is true, then $V=\mathcal{V}_{2}\oplus(n-1)\mathcal{V}_{1}$ and $g$ is a reflection.
$\Box$

###### Lemma 2.19

If $g^{k}=h$ acts as a reflection, and $g$ has order $m=2k>2$, then $\Sigma^{\prime}(g^{l})\geq 1$ for $1\leq l<k$.

Proof.
Since $m>2$, certainly $V$ contains a $\mathcal{V}_{d}$ with $\varphi(d)\geq 2$.
In such a summand, the eigenvalues of any power of $g$ come in conjugate pairs: in particular, this is true for the eigenvalues of $h$.
Therefore the eigenvalues of $h$ on $\mathcal{V}_{d}$ are equal to $1$ if $\varphi(d)\geq 2$, since the eigenvalue $-1$ occurs with multiplicity $1$.
Therefore a pair of conjugate eigenvalues of $g^{l}$ on $\mathcal{V}_{d}$ contribute $1$ to $\Sigma^{\prime}(g^{l})$.
$\Box$

###### Lemma 2.20

Let $X_{\Sigma}$ and $g$ be as above.
Then there is no divisor in the boundary $X\setminus\mathbf{T}$ that is fixed pointwise by a non-trivial element of $\langle g\rangle$.

Proof.
Suppose $D$ were such a divisor, fixed pointwise by some element $h\in G$.
Then $D$ corresponds to a $1$-parameter subgroup $\lambda\colon\mathbb{C}^{*}\to\mathbf{T}$.
Moreover, $D$ is a toric divisor and is itself a toric variety with dense torus $\mathbf{T}/\lambda(\mathbb{C}^{*})$.
Thus $h\in\mathrm{GL}(M)\cong\mathrm{GL}_{n}(\mathbb{Z})$ acts trivially on $\mathbf{T}/\lambda(\mathbb{C}^{*})$; but the only such element is $\lambda(t)\mapsto\lambda(t^{-1})$, which does not preserve $D$.
$\Box$

###### Corollary 2.21

The toroidal compactification $\overline{\mathcal{F}}_{L}(\Gamma)$ may be chosen so that on a boundary component over a dimension $0$ cusp, $\overline{\mathcal{F}}_{L}(\Gamma)$ has canonical singularities, and there are no fixed divisors in the boundary.

Proof.
Since $\Sigma$ is $G(F)$-invariant, the result follows immediately from Theorem 2.17 and Lemma 2.20 $\Box$

###### Corollary 2.22

There are no divisors at the boundary over a dimension $0$ cusp $F$ that are fixed by a nontrivial element of $G(F)$.

Note that in this subsection we needed no restriction on $n$.

### 2.3 Dimension $1$ cusps

It remains to consider the dimension $1$ cusps.
Here we have to be more explicit: we consider a rank $2$ totally isotropic subspace $E_{\mathbb{Q}}\subset L_{\mathbb{Q}}$, corresponding to a dimension $1$ boundary component $F$ of $\mathcal{D}_{L}$.
We want to choose standard bases for $L_{\mathbb{Q}}$ so as to be able to identify $U(F)$, $U(F)_{\mathbb{Z}}$ and $N(F)_{\mathbb{Z}}$ explicitly, as is done in _[x17]_ for maximal K3 lattices, where $n=19$.

But we shall not be able to choose suitable bases of $L$ itself, as in [Sc].
The first steps, however, can be done over $\mathbb{Z}$.
We define $E = E_{\mathbb{Q}} \cap L$ and $E^{\perp} = E_{\mathbb{Q}}^{\perp} \cap L$, primitive sublattices of $L$.

**Lemma 2.23** There exists a basis $\mathbf{e}_1', \ldots, \mathbf{e}_{n+2}'$ for $L$ over $\mathbb{Z}$ such that $\mathbf{e}_1', \mathbf{e}_2'$ is a basis for $E$ and $\mathbf{e}_1', \ldots, \mathbf{e}_n'$ is a basis for $E^{\perp}$.
Furthermore we can choose $\mathbf{e}_1', \ldots, \mathbf{e}_{n+2}'$ so that

$$
A = \left( \begin{array}{cc} \delta &amp; 0 \\ 0 &amp; \delta e \end{array} \right)
$$

for some integers $\delta$ and $e$, where $A$ is defined by

$$
Q' := (\mathbf{e}_i', \mathbf{e}_j') = \left( \begin{array}{ccc} 0 &amp; 0 &amp; A \\ 0 &amp; B &amp; C \\ {}^t A &amp; {}^t C &amp; D \end{array} \right).
$$

**Proof.** We can find a basis with all the properties except for the special form of $A$ by choosing any bases for the primitive sublattices $E$ and $E^{\perp}$ of $L$.
Then the matrix $A$ may be chosen to have the special form given by choosing $\mathbf{e}_1'$, $\mathbf{e}_2'$, $\mathbf{e}_{n+1}'$ and $\mathbf{e}_{n+2}'$ suitably: the numbers $\delta$ and $\delta e$ are the elementary divisors of $A \in \mathrm{Mat}_{2 \times 2}(\mathbb{Z})$.

If we are willing to allow two of the basis vectors to be in $L_{\mathbb{Q}}$ we can achieve much more.

**Lemma 2.24** There is a basis $\mathbf{e}_1, \ldots, \mathbf{e}_{n+2}$ for $L_{\mathbb{Q}}$ such that $\mathbf{e}_1$ and $\mathbf{e}_2$ form a $\mathbb{Z}$-basis for $E$, and $\mathbf{e}_1, \ldots, \mathbf{e}_n$ form a $\mathbb{Z}$-basis for $E^{\perp}$, for which

$$
Q := (\mathbf{e}_i, \mathbf{e}_j) = \left( \begin{array}{ccc} 0 &amp; 0 &amp; A \\ 0 &amp; B &amp; 0 \\ A &amp; 0 &amp; 0 \end{array} \right)
$$

with $A$ and $B$ as before.

**Proof.** We start with the basis $\mathbf{e}_1', \ldots, \mathbf{e}_{n+2}'$ from Lemma 2.23. Note that $B \in \mathrm{Mat}_{n-2 \times n-2}$ has non-zero determinant, because it represents the quadratic form of $L$ on $E_{\mathbb{Q}}^{\perp} / E_{\mathbb{Q}}$.
So we put $R = -B^{-1}C \in \mathrm{Mat}_{n-2 \times 2}(\mathbb{Q})$ and we take $\mathbf{e}_i$ consisting of the columns of

$$
N := \left( \begin{array}{ccc} I &amp; 0 &amp; R' \\ 0 &amp; I &amp; R \\ 0 &amp; 0 &amp; I \end{array} \right),
$$

where $R'$ is chosen to satisfy

$$
D - {}^t C B^{-1} C + {}^t R' A + {}^t A R' = 0.
$$

Then $\mathbf{e}_i$ is a $\mathbb{Q}$-basis for $L_{\mathbb{Q}}$ including $\mathbb{Z}$-bases for $E$ and $E^{\perp}$, as we want, and ${}^t N Q' N = Q$ as required.

18

Lemma 2.25 The subgroups $N(F)$, $W(F)$ and $U(F)$ are given by

$$
N (F) = \left\{\left( \begin{array}{c c c} U &amp; V &amp; W \\ 0 &amp; X &amp; Y \\ 0 &amp; 0 &amp; Z \end{array} \right) \mid {} ^ {t} U A Z = A, {} ^ {t} X B X = B, {} ^ {t} X B Y + {} ^ {t} V A Z = 0, \right.
$$

$$
W (F) = \left\{\left( \begin{array}{c c c} I &amp; V &amp; W \\ 0 &amp; I &amp; Y \\ 0 &amp; 0 &amp; I \end{array} \right) \mid B Y + {} ^ {t} V A = 0, {} ^ {t} Y B Y + A W + {} ^ {t} W A = 0 \right\},
$$

and

$$
U (F) = \left\{\left( \begin{array}{c c c} I &amp; 0 &amp; \left( \begin{array}{c c} 0 &amp; e x \\ - x &amp; 0 \end{array} \right) \\ 0 &amp; I &amp; 0 \\ 0 &amp; 0 &amp; I \end{array} \right) \mid x \in \mathbb {R} \right\}.
$$

Proof.
This is a straightforward calculation.

As in [Ko1] we realise $\mathcal{D}_L$ as a Siegel domain and $\mathcal{D}_L(F) = U(F)_{\mathbb{C}}\mathcal{D}_L(F)$ is identified with $\mathbb{C}\times \mathbb{C}^{n - 2}\times \mathbb{H}$.
The identification is by choosing homogeneous coordinates $(t_1\colon \ldots \colon t_{n + 2})$ on $\mathbb{P}(L_{\mathbb{C}})$ so that $t_{n + 2} = 1$ and mapping $t_1\mapsto z\in \mathbb{C}$, $t_{n + 1}\mapsto \tau \in \mathbb{H}$ and $t_i\mapsto w_{i - 2}\in \mathbb{C}$ for $3\leq i\leq n$: the value of $t_2$ is determined by the equation

$$
2 \delta e t _ {2} = - 2 \delta z \tau - {} ^ {t} \underline {{w}} B \underline {{w}} \tag {16}
$$

where $\underline{w}\in \mathbb{C}^{n - 2}$ is a column vector.

We are interested in the action of $N(F)_{\mathbb{Z}} = N(F) \cap \Gamma$ on $\mathcal{D}_L(F)$.
We denote by $\underline{V}_i$ the $i$th row of the matrix $V$ in Lemma 2.25.

Proposition 2.26 If $g \in N(F)$ is given by

$$
\left( \begin{array}{c c c} U &amp; V &amp; W \\ 0 &amp; X &amp; Y \\ 0 &amp; 0 &amp; Z \end{array} \right), \qquad Z = \left( \begin{array}{c c} a &amp; b \\ c &amp; d \end{array} \right)
$$

then $g$ acts on $\mathcal{D}_L(F)$ by

$$
z \quad \longmapsto \quad \frac {z}{\det  Z} + (c \tau + d) ^ {- 1} \left(\frac {c}{2 \delta \det  Z} ^ {t} \underline {{w}} B \underline {{w}} + \underline {{V}} _ {1} \underline {{w}} + W _ {1 1} \tau + W _ {1 2}\right)
$$

$$
\underline {{w}} \quad \longmapsto \quad (c \tau + d) ^ {- 1} \left(X \underline {{w}} + Y \left( \begin{array}{c} \tau \\ 1 \end{array} \right)\right)
$$

$$
\tau \quad \longmapsto \quad (a \tau + b) / (c \tau + d).
$$

Proof.
This is also a straightforward calculation.
One need only take into account that

$$
U = \frac {1}{\det  Z} \left( \begin{array}{c c} d &amp; - c e \\ b / e &amp; a \end{array} \right)
$$

We must now describe $N(F)_{\mathbb{Z}}$ and $U(F)_{\mathbb{Z}}$ .

Proposition 2.27 If $g \in N(F)_{\mathbb{Z}}$ then $Z \in \mathrm{SL}_2(\mathbb{Z})$ , and if $g \in U(F)_{\mathbb{Z}}$ then $x \in \mathbb{Z}$ .

Proof.
For $Z$ , it is enough to show that $Z \in \mathrm{Mat}_{2 \times 2}(\mathbb{Z})$ , since it acts on $\mathbb{H}$ .
The condition that $g \in N(F)_{\mathbb{Z}}$ or $g \in U(F)_{\mathbb{Z}}$ is that $N^{-1}gN \in \Gamma$ and in particular $N'^{-1}gN \in \mathrm{GL}_{n+2}(\mathbb{Z})$ .
We calculate this directly:

$$
N ^ {- 1} g N = \left( \begin{array}{c c c} U &amp; V &amp; V B ^ {- 1} C + W - U T + T Z \\ 0 &amp; X &amp; Y + X B ^ {- 1} C - B ^ {- 1} C Z \\ 0 &amp; 0 &amp; Z \end{array} \right),
$$

so $Z$ is integral.
In fact, because of ${}^t UAZ = A$ we even have $Z \in \Gamma_0(e)$ .

If $g \in U(F)_{\mathbb{C}}$ we have in addition $V = 0$ , $Y = 0$ , $U = Z = I_2$ and $X = I_{n-2}$ , so $VB^{-1}C + W - UT + TZ = W$ and therefore $W$ is integral.

Now we can calculate the action on the tangent space at a point in the boundary.
Suppose $g \in G(F) = N(F)_{\mathbb{Z}} / U(F)_{\mathbb{Z}}$ has finite order $m &gt; 1$ .
We abuse notation by also using $g$ to denote a corresponding element of $N(F)_{\mathbb{Z}}$ .
We choose a coordinate $u = \exp_e(z) \coloneqq e^{2\pi iz / e}$ on $U(F)_{\mathbb{C}} / U(F)_{\mathbb{Z}} \cong \mathbb{C}^*$ , where $e$ is as in Lemma 2.23, because $g \in U(F)_{\mathbb{Z}}$ acts by $z \mapsto z + ex$ .
The compactification is given by allowing $u = 0$ .
We suppose that $g$ fixes the point $(0, \underline{w}_0, \tau_0)$ .
We define $\Sigma(g)$ as we did before, in equation (8), as $\sum \left\{\frac{a_i}{m}\right\}$ if the eigenvalues are $\zeta^{a_i}$ for $\zeta = e^{2\pi i / m}$ .

Proposition 2.28 If $n \geq 8$ and no power of $g$ acts as a quasi-reflection at $(0, \underline{w}_0, \tau_0)$ then $\Sigma(g) \geq 1$ .

Proof.
This closely follows [Ko1, (8.2)].
The action of $g$ on the tangent space is given by

$$
\left( \begin{array}{c c c} \exp_ {e} (t) &amp; 0 &amp; 0 \\ * &amp; (c \tau_ {0} + d) ^ {- 1} X &amp; 0 \\ * &amp; * &amp; (c \tau_ {0} + d) ^ {- 2} \end{array} \right)
$$

where $t = (c\tau_0 + d)^{-1}(c^t\underline{w}_0B\underline{w}_0 / 2 + \underline{V}_1\underline{w}_0 + W_{11}\tau_0 + W_{12}) / e$ , by Lemma 2.26. Observe that $c\tau_0 + d = \xi$ is a (not necessarily primitive) fourth or sixth root of unity, because of the well-known fixed points of $\mathrm{SL}_2(\mathbb{Z})$ on $\mathbb{H}$ .

Suppose $X$ is of order $m_X$ .
We consider the decomposition of the representation $X$ , i.e. of $E_{\mathbb{Q}}^{\perp} / E_{\mathbb{Q}}$ as a $g$ -module.
It decomposes as a direct sum of $\mathcal{V}_d$ .
If $\xi \neq \pm 1$ the situation is exactly as in the case $\varphi(r) = 2$ at the end of the proof of Theorem 2.10, except that the right-hand side of equation (14) is now equal to $n - 2$ (that is, $\operatorname{rank} X$ ) instead of $n$ .
Any $\mathcal{V}_d$ contributes at least $c_{\min}(d)$ to $\Sigma(g)$ , so we may assume that $\varphi(d) \leq 2$ ; but then the

1-dimensional summands contribute at least $\frac{1}{6}$ and the 2-dimensional ones at least $\frac{1}{3}$.
Moreover, if $m_X &gt; 2$ then $X$ has a pair of conjugate eigenvalues and in the case $\xi = \pm 1$ they contribute 1 to $\Sigma(g)$.

So we may assume that $m_X = 1$ or $m_X = 2$, and $\xi = \pm 1$.
Since $-1 \in \Gamma$ acts trivially on $\mathcal{D}_L$ we may replace $g$ by $-g$ if we prefer, and assume that $\xi = 1$.
Since $g$ fixes $(0, \underline{w}_0, \tau_0)$ that implies $Z = I$.
If also $m_X = 1$, so $X = I$, then by Proposition 2.26 we have

$$
Y \left( \begin{array}{c} \tau_ {0} \\ 1 \end{array} \right) = \underline {{0}}
$$

and since $\tau_0 \notin \mathbb{Z}$ this implies $Y = 0$.
But then ${}^t VA = 0$ by Lemma 2.25, so $g \in U(F)_{\mathbb{Z}}$.

So the remaining possibility is that $Z = I$ and $m_X = 2$: thus $U = I$ since ${}^t UAZ = A$, and $c = 0$.
But then $t$ is a half-integer, because

$$
\underline {{w}} _ {0} = X \underline {{w}} _ {0} + Y \left( \begin{array}{c} \tau_ {0} \\ 1 \end{array} \right)
$$

and the condition $g^2 \in U(F)_{\mathbb{Z}}$ implies that $VX = -V$, that $XY = -Y$ and that

$$
2 W \equiv - V Y \bmod \left( \begin{array}{cc} 0 &amp; e \\ - 1 &amp; 0 \end{array} \right).
$$

So, modulo $e\mathbb{Z}$, we have

$$
\begin{array}{l}
2 t = 2 \underline {{V}} _ {1} \underline {{w}} _ {0} + 2 W _ {1 1} \tau_ {0} + 2 W _ {1 2} \\
\equiv \quad 2 \underline {{V}} _ {1} \underline {{w}} _ {0} - \underline {{V}} _ {1} Y \left( \begin{array}{c} \tau_ {0} \\ 1 \end{array} \right) \\
\equiv \underline {{V}} _ {1} (I + X) \underline {{w}} _ {0} \\
\equiv \quad 0.
\end{array}
$$

Thus the eigenvalue $\exp_e(t)$ is $\pm 1$, so in this case all eigenvalues on the tangent space are $\pm 1$ and either $\Sigma(g) \geq 1$ or $g$ acts as a reflection.
In particular any quasi-reflections have order 2.

Corollary 2.29 There are no divisors at the boundary over a dimension 1 cusp $F$ that are fixed by a nontrivial element of $G(F)$.

Proof.
From the proof of Proposition 2.28, any quasi-reflection $g$ has $m_X = 2$, and hence fixes a divisor different from $u = 0$.

Finally we check the analogue of Proposition 2.15. We define $\Sigma'(g)$ for $g \in G(F)$ exactly as in equation (15).

Proposition 2.30 If $g \in G(F)$ is such that $g^k = h$ is a reflection and $n \geq 9$ then $\Sigma'(g^l) \geq 1$ for every $1 \leq l &lt; k$.

21

Proof.

If the unique eigenvalue of $h$ that is different from $1$ (hence equal to $-1$) is $\exp_{e}(t)$ then the contribution from $X^{l}$ to $\Sigma^{\prime}(g)$ is at least $1$.
Otherwise, consider the $\mathcal{V}_{d}$ (in the decomposition as a $g$-module) in which the exceptional eigenvector $\mathbf{e}_{0}$ occurs, satisfying $h(\mathbf{e}_{0})=-\mathbf{e}_{0}$.
We must have $d=1$ or $d=2$, since if $\varphi(d)>1$ the eigenvalue $-1$ for $h$ would occur more than once.
But the rest of $X$ (i.e. the $(n-3)$-dimensional $g$-module $E^{\perp}_{\mathbb{Q}}/(E+\mathbb{Q}\,\mathbf{e}_{0})$) contributes at least $1$ to $\Sigma(g)$ and hence to $\Sigma^{\prime}(g)$, as long as $n-3\geq 6$, as was shown in Proposition 2.28. ∎

###### Corollary 2.31

If $n\geq 9$, the toroidal compactification $\overline{\mathcal{F}}_{L}(\Gamma)$ may be chosen so that on a boundary component over a dimension $1$ cusp, $\overline{\mathcal{F}}_{L}(\Gamma)$ has canonical singularities, and there are no fixed divisors in the boundary.

###### Proof.

This is immediate from Corollary 2.29, Proposition 2.28 and Proposition 2.30. In fact there are no choices to be made in this part of the boundary.
∎

## 3 Special reflections in $\widetilde{\mathrm{O}}(L)$

Let $L$ be an arbitrary nondegenerate integral lattice, and write $D$ for the exponent of the finite group $A_{L}=L^{\vee}/L$.
The reflection with respect to the hyperplane defined by a vector $r$ is given by

$\sigma_{r}\colon l\longmapsto l-\frac{2(l,r)}{(r,r)}r.$

For any $l\in L$ its _divisor_ $\mathrm{div}(l)$ in $L$ is the positive generator of the ideal $(l,L)$.
In other words $l^{*}=l/\operatorname{div}(l)$ is a primitive element of the dual lattice $L^{\vee}$.
If $r$ is primitive and the reflection $\sigma_{r}$ fixes $L$, i.e. $\sigma_{r}\in\mathrm{O}(L)$, then we say that $r$ is a reflective vector.
In this case

$\operatorname{div}(r)\mid r^{2}\mid 2\operatorname{div}(r).$ (17)

###### Proposition 3.1

Let $L$ be a nondegenerate even integral lattice.
Let $r\in L$ be primitive.
Then $\sigma_{r}\in\widetilde{\mathrm{O}}(L)$ if and only if $r^{2}=\pm 2$.

###### Proof.

For $r^{*}=r/\operatorname{div}(r)\in L^{\vee}$ and $\sigma_{r}\in\widetilde{\mathrm{O}}(L)$ we get

$\sigma_{r}(r^{*})=-r^{*}\equiv r^{*}\mod L.$

Therefore $2r^{*}\in L$, $\operatorname{div}(r)=1$ or $2$ (because $r$ is primitive) and $r^{2}=\pm 2$ or $\pm 4$, because $L$ is even.
If $r^{2}=\pm 2$ then $\sigma_{r}\in\widetilde{\mathrm{O}}(L)$.
If $r^{2}=\pm 4$, then

$\mathrm{div}(r)=2$ by condition (17).
For such $r$ the reflection $\sigma_{r}$ is in $\widetilde{\mathrm{O}}(L)$ if and only if

$l^{\vee}-\sigma_{r}(l^{\vee})=\frac{(r,l^{\vee})}{2}r=(r^{*},l^{\vee})r\in L$

for any $l^{\vee}\in L^{\vee}$.
Therefore $r^{*}=r/2\in(L^{\vee})^{\vee}=L$.
We obtain a contradiction because $r$ is primitive.
$\Box$

###### Proposition 3.2

Let $L$ be as in Proposition 3.1 and let $r\in L$ be primitive.
If $-\sigma_{r}\in\widetilde{\mathrm{O}}(L)$, i.e. $\sigma_{r}|_{A_{L}}=-\,\mathrm{id}$, then

- $r^{2}=\pm 2D$ and $\mathrm{div}(r)=D\equiv 1\mod 2$, or $r^{2}=\pm D$ and $\mathrm{div}(r)=D$ or $D/2$;
- $A_{L}\cong(\mathbb{Z}/2\mathbb{Z})^{m}\times(\mathbb{Z}/D\mathbb{Z})$.

In the opposite direction we have

- If $r^{2}=\pm D$ and either $\mathrm{div}(r)=D$ or $\mathrm{div}(r)=D/2\equiv 1\mod 2$, then $-\sigma_{r}\in\widetilde{\mathrm{O}}(L)$;
- If $r^{2}=\pm 2D$ and $\mathrm{div}(r)=D\equiv 1\mod 2$, then $-\sigma_{r}\in\widetilde{\mathrm{O}}(L)$.

Proof.
(i) $\sigma_{r}|_{A_{L}}=-\,\mathrm{id}$ is equivalent to the following condition:

$2l^{\vee}\equiv\frac{2(r,l^{\vee})}{r^{2}}r\mod L\qquad\forall\ l^{\vee}\in L^{\vee}.$ (18)

It follows that if $r^{2}=2e$, then $(2L^{\vee})/L$ is a subgroup of the cyclic group $\langle(r/e)+L\rangle$.
Thus $D$ divides $2e$.
But by definition of the divisor of the vector $e\mid\mathrm{div}(r)\mid D$, therefore

$e\mid\mathrm{div}(r)\mid 2e\quad\text{and}\quad e\mid D\mid 2e.$

From this it follows that $(2L^{\vee})/L$ is a subgroup of the cyclic group generated by $(r/D)+L$ or $(2r/D)+L$.
This implies (ii).

Let us assume that $r^{2}=\pm 2D$ and $\mathrm{div}(r)=D\equiv 0\mod 2$.
We have $2l^{\vee}\equiv\pm\frac{(r,l^{\vee})}{D}r\mod L$.
If the order of $l^{\vee}$ in the discriminant group is odd, then $(r,l^{\vee})$ is even, since $D$ is even.
If the order of $l^{\vee}$ is even, then $(r,l^{\vee})$ is again even, because the order of $2l^{\vee}$ is $D/2$.
Therefore $(r/2,l^{\vee})\in\mathbb{Z}$ for all $l^{\vee}\in L^{\vee}$.
This contradicts the assumption that $r$ is primitive.
Thus (i) is proved.

(iii) Let assume that $\mathrm{div}(r)=D$.
In this case $r^{*}=r/D$ and $2r^{*}+L$ is a generator of $(2L^{\vee})/L$.
According to (ii) we have that for any $l^{\vee}\in L^{\vee}$, $2l^{\vee}=2xr^{*}+l^{\prime}$, where $x\in\mathbb{Z}$, $l^{\prime}\in L$.
Therefore

$\frac{(2l^{\vee},r)}{r^{2}}r=2xr^{*}\pm\frac{(l^{\prime},r)}{D}r\equiv 2xr^{*}\equiv 2l^{\vee}\mod L$ (19)

and $-\sigma_{r}\in\widetilde{\mathrm{O}}(L)$ according to condition (18).

Let assume that $\mathrm{div}(r)=D/2\equiv 1\mod 2$.
We have to check condition (18) for all elements of order $2$ or $D$ in $A_{L}$.
If $\mathrm{ord}(l^{\vee})=2$, then $(2l^{\vee},r)\equiv 0\mod D/2$, and also $(l^{\vee},r)\equiv 0\mod D/2$, because $D/2$ is odd.
It follows that $2(l^{\vee},r)/r^{2}\in\mathbb{Z}$.
If $l^{\vee}$ is an element of order $D$, we have $2l^{\vee}=2xr^{*}+l^{\prime}$ as above with $r^{*}=(2r)/D$ and $l^{\prime}\in L$.
Thus $(l^{\prime},r)$ is even.
But $(l^{\prime},r)$ is also divisible by the odd number $D/2$.
Therefore $(l^{\prime},r)\equiv 0\mod D$ and equation (19) is also true.

(iv) is similar to (iii).
$D$ is odd and the group $A_{L}$ is cyclic with generator $r^{*}=r/D$.
Therefore $l^{\vee}=xr^{*}+l^{\prime}$ for any $l^{\vee}\in L^{\vee}$ and

$\frac{(2l^{\vee},r)}{r^{2}}r=\frac{2(xr^{*}+l^{\prime},r)}{r^{2}}r=2xr^{*}\pm\frac{2(l^{\prime},r)}{2D}\equiv 2l^{\vee}\mod L.$

$\Box$

###### Corollary 3.3

Let $L$ be an even integral lattice and $|A_{L}|=|\det L|$ be odd.
Then

- $\sigma_{r}\in\widetilde{\mathrm{O}}(L)$ if and only if $r^{2}=\pm 2$;
- $-\sigma_{r}\in\widetilde{\mathrm{O}}(L)$ if and only if $r^{2}=\pm 2D$ and $\mathrm{div}(r)=D$.

With K3 surfaces in mind, we consider in more detail the lattice $L_{2d}=2U\oplus 2E_{8}(-1)\oplus\langle-2d\rangle$.

###### Corollary 3.4

Let $\sigma_{r}$ be a reflection in $\mathrm{O}(L_{2d})$ defined by a primitive vector $r\in L_{2d}$.
$\sigma_{r}$ induces $\pm\,\mathrm{id}$ on the discriminant form $L_{2d}^{\vee}/L_{2d}$ if and only if $r^{2}=\pm 2$ or $r^{2}=\pm 2d$ and $\mathrm{div}(r)=d$ or $2d$.

Proof.
Any $r\in L_{2d}$ can be written as $r=m+xh$, where $m\in L_{0}=2U\oplus 2E_{8}(-1)$ and $h^{2}=-2d$ ($h$ is primitive).

If $r^{2}=\pm 2d$ and $\mathrm{div}(r)=2d$, then $-\sigma_{r}\in\widetilde{\mathrm{O}}(L_{2d})$ by Proposition 3.2.

If $r^{2}=\pm 2d$ and $\mathrm{div}(r)=d$, then $r=dm_{0}+xh$, where $x^{2}=1-d(m_{0}^{2}/2)$.
We see that

$\sigma_{r}\left(\frac{h}{2d}\right)=\frac{h}{2d}(1-2x^{2})-xm_{0}\equiv-\frac{h}{2d}\mod L_{2d}.$

$\Box$

The types of reflections in the full orthogonal group $\mathrm{O}^{+}(L)$ for $L=L_{2d}^{(0)}=2U\oplus\langle-2d\rangle$ were classified in _[x10]_ (for square-free $d$).
The result for $L_{2d}=2U\oplus 2E_{8}(-1)\oplus\langle-2d\rangle$ is exactly the same, because the unimodular part $2E_{8}(-1)$ plays no role in the classification.

The reflection $\sigma_{r}$ is an element of $\mathrm{O}^{+}(L_{\mathbb{R}})$ (where $L$ has signature $(2,n)$) if and only if $r^{2}<0$: see _[x11]_.

##

The $(-2)$-vectors of $L_{2d}$ form one or two (if $d\equiv 1\mod 4$) orbits with respect to the group $\widetilde{\mathrm{O}}^{+}(L_{2d})$.
We can also compute the number of $\widetilde{\mathrm{O}}^{+}(L_{2d})$-orbits of the $(-2d)$-reflective vectors in Corollary 3.4. However, in this paper we only need to know the orthogonal complements of $(-2d)$-vectors, which we compute in Proposition 3.6. (For the case of $(-2)$-vectors see _[x10, §3.6]_).

The following lemma, which we use in the proof of Proposition 3.6, is well-known, but we state it and give a general proof here for the convenience of the reader.
Recall that an integral lattice $T$ is called $2$-elementary if $A_{T}=T^{\vee}/T\cong(\mathbb{Z}/2\mathbb{Z})^{m}$.

###### Lemma 3.5

Let $T$ be a primitive sublattice of an unimodular even lattice $M$, and let $S$ be the orthogonal complement of $T$ in $M$.
Suppose that there is an involution $\sigma\in\mathrm{O}(M)$ such that $\sigma|_{T}=\mathrm{id}_{T}$ and $\sigma|_{S}=-\,\mathrm{id}_{S}$.
Then $T$ and $S$ are $2$-elementary lattices.

Proof.
Let us consider the inclusions $T\oplus S\subset M\subset T^{\vee}\oplus S^{\vee}$.
We have that $(A_{S},\;q_{S})\cong(A_{T},\;-q_{T})$ because $M$ is unimodular (see _[x23]_).
In particular $[M:T\oplus S]=[T^{\vee}:T]=[S^{\vee}:S]$.
It follows that

$H=M/(T\oplus S)\cong\phi(M)/S=S^{\vee}/S=A_{S}.$

Here $\phi\colon M\to S^{\vee}$ is defined by $\phi(m)(s)=(m,s)$ where $s\in S$.
The natural projections of the subgroup $H<A_{T}\oplus A_{S}$ onto $A_{T}$ and $A_{S}$ are injective, therefore the action of $\sigma$ on $A_{S}$ is completely determined by the action of $\sigma$ on $A_{T}$.
Thus $\sigma$ acts trivially on $A_{S}$ since it acts trivially on $A_{T}$.
But we assumed that $\sigma(s^{\vee})=-s^{\vee}$ for any $s^{\vee}\in S^{\vee}$.
It follows that $A_{S}$ is an abelian $2$-group.
$\Box$

###### Proposition 3.6

Let $r$ be a primitive vector of $L_{2d}$.
If $\mathrm{div}(r)=2d$ then

$r^{\perp}_{L_{2d}}\cong 2U\oplus 2E_{8}(-1).$

If $\mathrm{div}(r)=d$ then either

$r^{\perp}_{L_{2d}}\cong U\oplus 2E_{8}(-1)\oplus\langle 2\rangle\oplus\langle-2\rangle$

or

$r^{\perp}_{L_{2d}}\cong U\oplus 2E_{8}(-1)\oplus U(2).$

Proof.
The lattice $L_{2d}$ is the orthogonal complement of a primitive vector $h$, with $h^{2}=2d$ in the unimodular K3 lattice $L_{\mathrm{K3}}=3U\oplus 2E_{8}(-1)$.
We put $L_{r}=r^{\perp}_{L_{2d}}$ and $S_{r}=(L_{r})_{L_{\mathrm{K3}}}^{\perp}$.

We note that $L_{r}$ and $S_{r}$ have the same determinant: in fact

\[ \det L*{r}=\det S*{r}=4d^{2}/\,\mathrm{div}(r)^{2}=\begin{cases}1&\quad\text{if }\;\mathrm{div}(r)=2d,\\
4&\quad\text{if }\;\mathrm{div}(r)=d.\end{cases} \]

######

To see this, consider a more general situation.
Let $N$ be a primitive even nondegenerate sublattice of any even integral lattice $L$ and let $N^{\perp}$ be its orthogonal complement in $L$.
Then we have

$N\oplus N^{\perp}\subset L\subset L^{\vee}\subset N^{\vee}\oplus(N^{\perp})^{\vee},$

where $L/(N\oplus N^{\perp})\cong L^{\vee}/(N^{\vee}\oplus(N^{\perp})^{\vee})$.
As before we have $\phi\colon L\to N^{\vee}$, and $\ker(\phi)=N^{\perp}$.
Since $L/(N\oplus N^{\perp})\cong\phi(L)/N$ we obtain

$|L/(N\oplus N^{\perp})|=|\phi(L)/N|=|\det N|/[N^{\vee}:\phi(L)],$

as $|\det N|=[N^{\vee}:N]$.
From the inclusions above

$|\det N|\cdot|\det N^{\perp}|=(|\det L|)[\phi(M):N]^{2}=|\det L|\cdot|\det N|^{2}/[N^{\vee}:\phi(L)]^{2}.$

In our particular case $L=L_{2d}$, $N=\mathbb{Z}r$ and $L_{r}=N^{\perp}$.
We have $[N^{\vee}:\phi(L)]=\operatorname{div}(r)$, where $\operatorname{div}(r)\mathbb{Z}=(r,L)$, and this gives us the formula for the determinant of $L_{r}$.

If $\operatorname{div}(r)=2d$ then $L_{r}$ and $S_{r}$ are are isomorphic to the unique unimodular lattices of signatures $(2,18)$ and $(1,1)$ respectively: that is, $L_{r}\cong 2U\oplus 2E_{8}(-1)$ and $S_{r}\cong U$.

If $\operatorname{div}(r)=d$ then the reflection $\sigma_{r}$ acts as $-\operatorname{id}$ on the discriminant group (see Corollary 3.4). Therefore we can extend $-\sigma_{r}\in\widetilde{\operatorname{O}}(L_{2d})$ to an element of $\operatorname{O}(L_{\operatorname{K}3})$ by putting $(-\sigma_{r})|_{\mathbb{Z}h}=\operatorname{id}$.
So $\sigma_{r}$ has an extension $\tilde{\sigma}_{r}\in\operatorname{O}(L_{\operatorname{K}3})$ such that $\tilde{\sigma}_{r}|_{L_{r}}=\operatorname{id}_{L_{r}}$ and $\tilde{\sigma}_{r}|_{S_{r}}=-\operatorname{id}_{S_{r}}$.
It follows from Lemma 3.5 that $L_{r}$ and $S_{r}$ are $2$-elementary lattices.

The finite discriminant forms of $2$-elementary lattices were classified by Nikulin in _[x21]_.
The genus of $M$ (and the class of $M$ if $M$ is indefinite) is determined by the signature of $M$, the number of generators $m$ of $A_{M}$ and the parity $\delta_{M}$ of the finite quadratic form $q_{M}\colon A_{M}\to\mathbb{Q}/2\mathbb{Z}$, which is given by $\delta_{M}=0$ if $l^{2}\in\mathbb{Z}$ for all $l\in M^{\vee}$ and $\delta_{M}=1$ otherwise: (see _[x21, §3]_).
In particular, for an indefinite lattice $S_{r}$ of rank $2$ and determinant $4$ we have

\[ S*{r}\cong\left\{\begin{array}[]{ll}U(2)&\quad\text{if}\quad\delta*{S*{r}}=0,\\
\langle 2\rangle\oplus\langle-2\rangle&\quad\text{if}\quad\delta*{S\_{r}}=1.\end{array}\right.
\]

The class of the indefinite lattice $L_{r}$ is uniquely defined by its discriminant form.
Proposition 3.6 is proved.
$\Box$

Geometrically the three cases in Proposition 3.6 correspond to the Néron-Severi group being (generically) $U$, $U(2)$ or $\langle 2\rangle\oplus\langle-2\rangle$ respectively.
The K3 surfaces (without polarisation) themselves are, respectively, a double cover of the Hirzebruch surface $F_{4}$, a double cover of a quadric, and the desingularisation of a double cover of $\mathbb{P}^{2}$ branched along a nodal sexti

4 Special cusp forms.

Let $L=2U\oplus L_{0}$ be an even lattice of signature $(2,n)$ ($n\geq 3$) containing two hyperbolic planes.
We write ${\cal F}_{L}={\cal F}_{L}(\widetilde{\rm O}^{+}(L))$ for brevity.
A 0-dimensional cusp of ${\cal F}_{L}$ is defined by a primitive isotropic vector $v$.
Any two primitive isotropic vectors of divisor 1 lie in the same $\widetilde{\rm O}^{+}(L)$-orbit, according to the well-known criterion of Eichler (see _[x10, §10]_).
We call the corresponding cusp the standard 0-dimensional cusp of the Baily–Borel compactification ${\cal F}^{*}_{L}$.

Each 1-dimensional boundary component $F$ of ${\cal D}_{L}$ is isomorphic to the upper half plane $\mathbb{H}$ and in the Baily–Borel compactification this corresponds to adding an (open) curve $\Lambda\backslash\mathbb{H}$, where $\Lambda\subset{\rm SL}_{2}(\mathbb{Q})$ is an arithmetic group which depends on the component $F$.
Details of this can be found in _[x2]_ and _[x25]_.
For our purpose we need one general result not contained there.

###### Lemma 4.1

Suppose that $L$ is even, and that any isotropic subgroup of the discriminant group $(A_{L},q_{L})$ is cyclic.
Then the closure of every $1$-dimensional cusp in ${\cal F}^{*}_{L}$ contains the standard $0$-dimensional cusp.

Proof.
Let $E$ be a primitive totally isotropic rank 2 sublattice of $L$ and define the lattice $\widetilde{E}=E_{L^{\vee}}^{\perp\perp}$ (both orthogonal complements are taken in the dual lattice $L^{\vee}$).
We remark that $E\subset\widetilde{E}$ and that $E=\widetilde{E}\cap L$ because $E$ is isotropic and primitive.
Thus the finite group

$H_{E}=E_{L^{\vee}}^{\perp\perp}/E<A_{L}$

is an isotropic subgroup of the discriminant group of $L$.
Let us take a basis of $L$ as in Lemma 2.23. It is easy to see that

$H_{E}\cong A^{-1}\mathbb{Z}^{2}/\mathbb{Z}^{2}.$

In the case we are considering, $H_{E}$ is a cyclic subgroup ($|H_{E}|^{2}$ divides $\det L$).
Therefore $A=\mathrm{diag}(1,e)$.
Thus $E$ contains primitive isotropic vectors with divisors $1$ and $e$, and the first vector defines the standard $0$-dimensional cusp.
$\Box$

Remark.
If the discriminant group of $L$ contains a non-cyclic isotropic subgroup then there is a totally isotropic sublattice $E$ of $L$ such that the finite abelian group $H_{E}$ has elementary divisors $(\delta,\delta e)$ with $\delta>1$.
Thus $\det L$ is divisible by $\delta^{4}e^{2}$.

Let $L=2U\oplus L_{0}$ be of signature $(2,n)$ and $u$ be a primitive isotropic vector of divisor 1. The tube realisation ${\cal H}_{u}$ of the homogeneous domain ${\cal D}_{L}$ at the standard $0$-dimensional cusp is defined by the sublattice $L_{1}=u^{\perp}/\mathbb{Z}u\cong U\oplus L_{0}$:

${\cal H}_{u}={\cal H}(L_{1})=\{Z\in L_{1}\otimes\mathbb{C}\ |\ (\mathrm{Im}\,Z,\mathrm{Im}\,Z)>0\}^{+},$ (20)

where

$F_{L}(L)=\frac{1}{2}\sum_{l\in L_{1}^{\vee}}(l,l)\geq 0a(l)\exp(2\pi i(l,L))$ (20)

where ^{+} denotes a connected component of the domain (see [G] for details).
The modular group $\widetilde{\mathrm{O}}^{+}(L)$ acting on $\mathcal{H}(L_{1})$ contains all translations $Z\to Z+l$ $(l\in L_{1})$.
Therefore the Fourier expansion of a $\widetilde{\mathrm{O}}^{+}(L)$-modular form $F$ at the standard cusp is

$F(Z)=\sum_{l\in L_{1}^{\vee},\ (l,l)\geq 0}a(l)\exp(2\pi i(l,Z)).$ (21)

###### Theorem 4.2

Let $L$ be an even lattice with two hyperbolic planes such that any isotropic subgroup of the discriminant group of $L$ is cyclic.
Let $F$ be a modular form with respect to $\widetilde{\mathrm{O}}^{+}(L)$.
If its Fourier coefficients $a(l)$ at the standard cusp satisfy $a(l)=0$ if $(l,l)=0$, then $F$ is a cusp form.

Proof.
A standard $1$-dimensional cusp is defined by a primitive totally isotropic sublattice $E_{1}=\langle u,v\rangle$ with $\mathrm{div}(u)=\mathrm{div}(v)=1$.
We can choose $(u,v)$ in such a way that they generate the maximal totally isotropic sublattice in $U\oplus U$.
Let $E$ be an arbitrary primitive totally isotropic sublattice of rank $2$ of $L$ defining a $1$-dimensional cusp of $\mathcal{F}_{L}$.
We can assume that $E=\langle u,v^{\prime}\rangle_{\mathbb{Z}}$ where $u$ defines the standard $0$-dimensional cusp (see Lemma 4.1 above).
According to the Witt theorem for the rational hyperbolic quadratic space $L_{1}\otimes\mathbb{Q}$ there exists $\sigma\in\mathrm{O}(L_{1}\otimes\mathbb{Q})$ such that $\sigma(v^{\prime})=v$.
We can extend $\sigma$ to an element of $\mathrm{O}^{+}(L\otimes\mathbb{Q})$ by putting $\sigma(u)=\pm u$.
The Siegel operator $\Phi_{E}$ for the boundary component defined by $E$ has the property $\Phi_{E}(F\circ\sigma)=\Phi_{\sigma(E)}(F)\circ\sigma$ (see [BB]).
Therefore

$\Phi_{E}(F)=\Phi_{\sigma^{-1}E_{1}}(F)=\Phi_{E_{1}}(F\circ\sigma^{-1})\circ\sigma.$

We can calculate the Fourier expansion of the function under the Siegel operator $\Phi_{E_{1}}$:

$F\circ\sigma^{-1}$ $=$ $\pm\sum_{l\in L_{1}^{\vee},\ (l,l)>0}a(l)\exp(2\pi i(l,\sigma^{-1}Z))$ (22)
$=$ $\pm\sum_{l_{1}\in\sigma L_{1}^{\vee},\ (l_{1},l_{1})>0}a(\sigma^{-1}l_{1})\exp(2\pi i(l_{1},Z)).$

Thus $\Phi_{E}(F)=\Phi_{E_{1}}(F\circ\sigma^{-1})\circ\sigma\equiv 0$ and $F$ is a cusp form.
$\Box$

In [G, Theorem 3.1] modular forms for $\widetilde{\mathrm{SO}}^{+}(L)$ are constructed using the arithmetic lifting of a Jacobi form $\phi$.
The modular form $\mathrm{Lift}(\phi)$ is defined by its first Fourier-Jacobi coefficient at a fixed standard $1$-dimensional cusp.
In particular, we know the Fourier expansion at the standard $0$-dimensional cusp.
Therefore we obtain the following improvement of the result proved in [G] for square-free $d$

###### Corollary 4.3

Let $L=L_{2d}=2U\oplus 2E_{8}(-1)\oplus\langle-2d\rangle$.
Then the arithmetic lifting $\mathrm{Lift}(\phi)$ of a Jacobi cusp form $\phi\in J_{k,1}^{\mathrm{cusp}}(L_{2d})$ of weight $k$ and index $1$ is a cusp form of weight $k$ for $\widetilde{\mathrm{SO}}^{+}(L_{2d})$ for any $d\geq 1$.

## 5 Application: K3 surfaces with a spin structure

Instead of $\widetilde{\mathrm{O}}^{+}(L_{2d})$ and $\mathcal{F}_{2d}$, we may consider the subgroup $\widetilde{\mathrm{SO}}^{+}(L_{2d})$ of $\widetilde{\mathrm{O}}^{+}(L_{2d})$ of index $2$ and the corresponding quotient

$\mathcal{SF}_{2d}=\widetilde{\mathrm{SO}}^{+}(L_{2d})\backslash\mathcal{D}_{L_{2d}}.$

If $d>1$ then $\mathcal{SF}_{2d}$ is a double covering of $\mathcal{F}_{2d}$.
(For $d=1$ the two spaces coincide since $\widetilde{\mathrm{SO}}^{+}(L_{2})\cong\widetilde{\mathrm{O}}^{+}(L_{2})/\pm I$.) This double covering has the following geometric interpretation: the domain $\mathcal{D}_{L_{2d}}$ is the parameter space of marked K3 surfaces of degree $2d$, and dividing out by the group $\widetilde{\mathrm{O}}^{+}(L_{2d})$ identifies all the different markings on a given K3 surface.
Two markings will be identified under the group $\widetilde{\mathrm{SO}}^{+}(L_{2d})$ if and only if they have the same orientation.
Hence $\mathcal{SF}_{2d}$ parametrises polarised K3 surfaces $(S,h)$ together with an orientation of the lattice $L_{h}=h^{\perp}$.
We shall refer to these as _oriented_ K3 surfaces.
An orientation on a surface $S$ is also sometimes called a _spin structure_ on $S$.

We have seen in Corollary 3.4 that the branch divisor of the map $\mathcal{D}_{L_{2d}}\to\mathcal{F}_{2d}$ is given by the divisors associated to reflections $\sigma_{r}$ defined by a primitive vector $r$ of length either $r^{2}=-2$ or $r^{2}=-2d$.
Note that in the first case $\sigma_{r}$ acts trivially on the discriminant group whereas it acts as $-\,\mathrm{id}$ in the second case.
Hence $\pm\sigma_{r}\notin\widetilde{\mathrm{SO}}^{+}(L_{2d})$ if $r^{2}=-2$, but $-\sigma_{r}\in\widetilde{\mathrm{SO}}^{+}(L_{2d})$ if $r^{2}=-2d$.
It follows that the quotient map $\mathcal{D}_{L_{2d}}\to\mathcal{SF}_{2d}$ is branched along the $(-2d)$-divisors whereas the double cover $\mathcal{SF}_{2d}\to\mathcal{F}_{2d}$ is branched along the $(-2)$-divisors.
In this way the group $\widetilde{\mathrm{SO}}^{+}(L_{2d})$ separates the two types of contributions to our reflective obstructions.
The reflective obstructions coming from the $(-2d)$ divisors are less problematic, as we shall see in the next theorem.
The $(-2d)$-divisors have a geometric interpretation.
The general point on such a divisor is associated to a K3 surface $S$ whose transcendental lattice $T_{S}$ has rank $20$ and which admits an involution acting as $-\,\mathrm{id}$ on $T_{S}$.
For $d=p^{2}$ this was shown in (_[x14, Prop. 7.4]_), and for general $d$ it follows from Corollary 3.4 and the proof of Proposition 3.6 above.

In _[x10]_ it was proved that the modular variety $\widetilde{\mathrm{SO}}^{+}(L_{2d})(q)\backslash\mathcal{D}_{L_{2d}}$, where $\widetilde{\mathrm{SO}}^{+}(L_{2d}(q))$ is the principal congruence subgroup of $\widetilde{\mathrm{SO}}^{+}(L_{2d})$ of level $q\geq 3$, is of general type for any $d\geq 1$.
Here we obtain a much stronger result.

###### Theorem 5.1

The moduli space $\mathcal{SF}_{2d}=\widetilde{\mathrm{SO}}^{+}(L_{2d})\backslash\mathcal{D}_{L_{2d}}$ of oriented K3 surfaces of degree $2d$ is of general type if $d\geq 3$.

###### Proof.

For $L_{2d}=2U\oplus 2E_{8}(-1)\oplus\langle-2d\rangle$ the corresponding space of Jacobi cusp forms in 18 variables is isomorphic (as a linear space) to the space of Jacobi cusp forms of Eichler-Zagier type (see _[x11, lemma 2.4]_)

$J_{k,1}^{\mathrm{cusp}}(L_{2d})\cong J_{k-8,d}^{\mathrm{cusp}}(EZ).$

For $k=17$, this space is non-trivial for any $d\geq 3$.
Therefore for any $d\geq 3$ there is a cusp form $F_{17}$ of weight 17 with respect to $\widetilde{\mathrm{SO}}^{+}(L_{2d})$.

The ramification divisor of the projection $\pi_{\mathrm{SO}}\colon\mathcal{D}_{L_{2d}}\to\widetilde{\mathrm{SO}}^{+}(L_{2d})\backslash\mathcal{D}_{L_{2d}}$ is defined by $(-2d)$-reflections of $L_{2d}$.
In Lemma 5.2 below we show that the cusp form $F_{17}$ vanishes on the ramification divisors of $\pi_{\mathrm{SO}}$.

Hence $\mathcal{SF}_{2d}$ is of general type for $d\geq 3$ by Theorem 1.1. ∎

###### Lemma 5.2

Any modular form $F\in M_{2k+1}(\widetilde{\mathrm{SO}}^{+}(L_{2d}))$ of odd weight vanishes along the divisors defined by $(-2d)$-reflective vectors.

###### Proof.

Let $\sigma_{r}\in\mathrm{O}^{+}(L_{2d})$ be a reflection with respect to a $(-2d)$-vector.
Then $-\sigma_{r}\in\widetilde{\mathrm{SO}}^{+}(L_{2d})$ (see Corollary 3.4). For any $z\in\mathcal{D}_{L_{2d}}$ with $(z,r)=0$ and a modular form $F\in M_{2k+1}(\widetilde{\mathrm{SO}}^{+}(L_{2d}))$ we have

$F(z)=F((-\sigma_{r})(z))=F(-z)=(-1)^{2k+1}F(z),$

so $F(z)\equiv 0$.
∎

We note that $\mathcal{SF}_{2}=\mathcal{F}_{2}$ is unirational.

The geometric interpretation of the $(-2)$-divisors, which form the ramification of the covering $\mathcal{SF}_{2d}\to\mathcal{F}_{2d}$, is that they parametrise those polarised K3 surfaces whose polarisation is only semi-ample, but not ample.
This is due the presence of rational curves on which the polarisation has degree 0. Thus in the case $d=2$ the map $\mathcal{SF}_{4}\to\mathcal{F}_{4}$ is a double cover of the moduli space of quartic surfaces branched along the discriminant divisor of singular quartics.
The variety $\mathcal{F}_{4}$ is unirational but $\mathcal{SF}_{4}$ is not, since there exists a canonical differential form on it (see _[x11]_).
There is also a cusp form of weight 18 with respect to $\widetilde{\mathrm{SO}}^{+}(L_{4})$ which vanishes on one of the two irreducible components of the ramification divisors for $d=2$.
We shall return to this question in a more general context in _[x10]_.

## 6 Pull-back of the Borcherds function $\Phi_{12}$.

To construct pluricanonical differential forms on a smooth model of $\mathcal{F}_{2d}$ we shall use the pull-back of the Borcherds automorphic product $\Phi_{12}$.

Let $L_{2,26}=2U\oplus 3E_{8}(-1)$ be the unimodular lattice of signature $(2,26)$.
For later use, we note the following simple lemma.

###### Lemma 6.1

Let $r$ be a primitive reflective vector in $L_{2d}$ with $r^{2}=-2d$ and let $L_{r}=r_{L_{2d}}^{\perp}$ be its orthogonal complement considered as a primitive sublattice of the unimodular lattice $L_{2,26}$.
Then

$(L_{r})^{\perp}_{L_{2,26}}\cong E_{8}(-1),\ E_{7}(-1)\oplus\langle-2\rangle\ \ \text{or}\ \ D_{8}(-1).$

Proof.
In the proof of Proposition 3.6 we found $L_{r}$ and its orthogonal complement $S_{r}$ in the unimodular lattice $L_{\mathrm{K}3}=3U+2E_{8}(-1)$.
The discriminant forms of $S_{r}$ and $K_{r}=(L_{r})^{\perp}_{L_{2,26}}$ coincide, but $K_{r}$ is of signature $(0,8)$.
The three possible genera of $K_{r}$ are represented by $E_{8}(-1)$, $E_{7}(-1)\oplus\langle-2\rangle$ and $D_{8}(-1)$.
The genera of such lattices contain only one class: one can can prove this well-known fact by analysing sublattices of order 2 in $E_{8}$ or simply check it using MAGMA.
$\Box$

The Borcherds function $\Phi_{12}\in M_{12}(\mathrm{O}^{+}(L_{2,26}),\det)$ is the unique modular form of weight 12 and character det with respect to $\mathrm{O}^{+}(L_{2,26})$ (see [B]).

$\Phi_{12}$ is the denominator function of the fake Monster Lie algebra and it has a lot of remarkable properties.
In particular, the zeros of $\Phi_{12}(Z)$ lie on rational quadratic divisors defined by $(-2)$-vectors in $L_{2,26}$, i.e., $\Phi_{12}(Z)=0$ if and only if there exists $r\in L_{2,26}$ with $r^{2}=-2$ such that $(r,Z)=0$ and the multiplicity of the rational quadratic divisor in the divisor of zeros of $\Phi_{12}$ is 1.

Pulling back this function gives us many interesting automorphic forms (see [B, pp. 200-201], [GN, pp. 257-258]).
In the context of the moduli of K3 surfaces this function was used in [BKPS] and [Ko2].
We summarise their results in a suitable form.

Let $l\in E_{8}(-1)$ satisfy $l^{2}=-2d$.
The choice of $l$ determines an embedding of $L_{2d}$ into $L_{2,26}$ as well as an embedding of the domain $\mathcal{D}_{L_{2d}}$ into $\mathcal{D}_{L_{2,26}}$.
We put $R_{l}=\{r\in E_{8}(-1)\mid r^{2}=-2,\ (r,l)=0\}$, and $N_{l}=\#R_{l}$.
(It is clear that $N_{l}$ is even.) Then by [BKPS] the function

$F_{l}=\frac{\Phi_{12}(Z)}{\prod_{\{\pm r\}\in R_{l}}(Z,r)}\ \Bigg{|}_{\mathcal{D}_{L_{2d}}}\in M_{12+\frac{N_{l}}{2}}(\widetilde{\mathrm{O}}^{+}(L_{2d}),\det)$ (23)

is a non-trivial modular form of weight $12+\frac{N_{l}}{2}$ vanishing on all $(-2)$-divisors of $\mathcal{D}_{L_{2d}}$.
(As we did in Section 4, we think of a modular form as a function on $\mathcal{D}_{L}$ rather than $\mathcal{D}_{L}^{\bullet}$, by identifying $\mathcal{D}_{L}$ with a tube domain realisation as in equation (20) above.) Moreover it is shown in [Ko2] that $F_{l}$ is a cusp form if $d$ is square-free and the weight is odd.

In fact much more is true.

###### Theorem 6.2

The function $F_{l}$ has the following properties:

- $F_{l}\in M_{12+\frac{N_{l}}{2}}(\widetilde{\mathrm{O}}^{+}(L_{2d}),\det)$ and $F_{l}$ vanishes on all $(-2)$-divisors.
-

$F_{l}$ is a cusp form for any $d$ if $N_{l}>0$.
3. If the weight of $F_{l}(Z)$ is smaller than $68$ (i.e., if $N_{l}<112$) then $F_{l}(Z)$ is zero along the branch divisor of the projection

$\pi\colon\mathcal{D}_{L_{2d}}\longrightarrow\Gamma_{2d}\backslash\mathcal{D}_{L_{2d}}=\mathcal{F}_{2d}.$

###### Proof.

(i) was proved in _[x1]_, but we repeat some details here for convenience.
First, $F_{l}(Z)$ is holomorphic because of the properties of the divisor of $\Phi_{12}$.
Then $F_{l}(tZ)=t^{-(12+N_{l}/2)}F_{l}(Z)$ for any $Z\in\mathcal{D}_{L_{2d}}$.
Any $g\in\widetilde{\mathrm{O}}^{+}(L_{2d})$ can be extended (by the identity on the orthogonal complement of $L_{2d}$ in $L_{2,26}$) to an element $\tilde{g}$ of $\mathrm{O}^{+}(L_{2,26})$.
Therefore $F_{l}(gZ)=\det(g)F_{l}(Z)$ since $\tilde{g}(r)=r$ for all roots in $R_{l}$.
This modular form is evidently not identically zero.
On the other hand, because it has character det it vanishes on all divisors of $\mathcal{D}_{L_{2d}}$ which are invariant with respect to $\sigma_{r}$ with $r^{2}=-2$, because then $\sigma_{r}\in\widetilde{\mathrm{O}}^{+}(L_{2d})$.

(ii) The Fourier expansion of $\Phi_{12}$ at the standard $0$-dimensional cusp is defined by the hyperbolic unimodular lattice $L_{1,25}=U\oplus 3E_{8}(-1)$ (see (20) and (21)):

$\Phi_{12}(Z)=\sum_{u\in L_{1,25},\,(u,u)=0}\,a(u)\exp(2\pi i(u,Z)).$

The weight $12$ is singular, therefore the hyperbolic norm of the index of any non-zero Fourier coefficient is zero.

Let us fix a root $r\in R_{l}\subset L_{1,25}$ (any root is equivalent to such a root).
We denote by $L_{r}$ the orthogonal complement of $r$ in $L_{1,25}$.
We have $Z=Z_{r}+zr$, where $Z_{r}\in\mathcal{H}(L_{r})$ and $z\in\mathbb{C}$.
We note that $\Phi_{12}(Z_{r})\equiv 0$.
The function

$\Phi_{r}(Z_{r})=\left.\frac{\Phi_{12}(Z)}{(Z,r)}\right|_{\mathcal{H}(L_{r})}$

is the first coefficient of the Taylor expansion of the function $\Phi_{12}(Z_{r}+zr)$ in $z$.

The summation in the Fourier expansion of $\Phi_{r}(Z_{r})$ is taken over the dual lattice $L_{r}^{\vee}$.
We note that

$L_{r}\oplus\mathbb{Z}r\subset L_{1,25}\subset L_{r}^{\vee}\oplus\mathbb{Z}(r/2).$

Let us calculate

$\left.\frac{\partial\Phi_{12}(Z_{r}+zr)}{\partial z}\right|_{z=0}.$

We get non-zero Fourier coefficient only for indices $u=u_{r}+m(r/2)$, where $u_{r}\in L_{r}^{\vee}$ and $0\neq m\in\mathbb{Z}$.
In this case $(u_{r},u_{r})=m^{2}/2>0$.
Thus the first derivative has non-zero Fourier coefficient only for indices $u_{r}$ with positive square.
Doing this for every $r$ we see that the Fourier expansion of $F_{l}$ at the

canonical cusp contains only indices with positive hyperbolic norm.
Thus $F_{l}$ is a cusp form.

The components of the branch divisor are divisors

$\mathcal{F}_{2d}(r)=\pi(\{Z\in\mathcal{D}_{L_{2d}}\mid(Z,r)=0\})$

defined by reflective vectors $r\in L_{2d}$, by Corollary 3.4. For a $(-2)$-vector $r\in L_{2d}$, the form $F_{l}(Z)$ has a zero along $\mathcal{F}_{2d}(r)$ (see (i)).

Now we can finish the proof using Lemma 6.1. If $r$ is a $(-2d)$-reflective vector and $L_{r}=r_{L_{2d}}^{\perp}$, then the divisor $\mathcal{F}_{2d}(r)$ coincides with the modular projection $\pi(\mathcal{D}_{L_{r}})$ of the homogeneous domain of the lattice $L_{r}$ of signature $(2,18)$.
According to Lemma 6.1, $(L_{r})_{L_{2,26}}^{\perp}$ is a root lattice with $N\geq 112$ roots ($E_{8}$ has $240$ roots, $E_{7}$ has $126$ and $D_{8}$ has $112$).
Therefore the Borcherds form $\Phi_{12}$ has a zero of order $N\geq 112>N_{l}$ along the subdomain $\mathcal{D}_{L_{r}}$.
Thus $F_{l}$ is zero along the corresponding divisor $\mathcal{F}_{2d}(r)$.
$\Box$

According to Theorem 6.2 and Theorem 1.1 the main point for us is the following.
We want to know for which $2d>0$ there exists a vector

$l\in E_{8},\ l^{2}=2d,\ l\ \ \text{is orthogonal to at least 2 and at most 12 roots.}$ (24)

###### Theorem 6.3

Such a vector $l$ in $E_{8}$ does exist if one of two inequalities

$4N_{E_{7}}(2d)>28N_{E_{6}}(2d)+63N_{D_{6}}(2d)$ (25)

or

$5N_{E_{7}}(2d)>28N_{E_{6}}(2d)+63N_{D_{6}}(2d)+378N_{D_{5}}(2d)$ (26)

is valid, where $N_{L}(2d)$ denotes the number of representations of $2d$ by the lattice $L$.

Proof.
Let us fix a root $a\in E_{8}$.
This choice gives us a realisation of the lattice $E_{7}$ as a sublattice of $E_{8}$:

$E_{7}\cong E_{7}^{(a)}=a_{E_{8}}^{\perp}.$

We have the following decomposition of the set of roots $R(E_{8})$:

$R(E_{8})=R(E_{7})\sqcup X_{114}\qquad\text{where }X_{114}=\{c\in R(E_{8})\mid c\cdot a\neq 0\}$

and $|X_{114}|=|R(E_{8})|-|R(E_{7})|=240-126=114$.

###### Lemma 6.4

The roots have the following properties:

1. $X_{114}$ is the union of $28$ root systems of type $A_{2}$ such that $R(A_{2}^{(i)})\cap R(A_{2}^{(j)})=\{\pm a\}$ for any $i\neq j$.
2.

3. Let $A_{2}(a,c)\neq A_{2}(a,d)$ be two $A_{2}$-lattices generated by roots $a$, $c$ and $a$, $d$.
   Then

$A_{3}(a,c,d)=A_{2}(a,c)+A_{2}(a,d)$

is a lattice of type $A_{3}$ containing one and only one copy of $A_{1}$ from $E_{7}^{(a)}$.
3. Let us take three different $A_{2}(a,c_{i})$ ($i=1,2,3$).
Then their sum

$S=\sum_{i=1}^{3}A_{2}(a,c_{i})$

is a lattice of type $A_{4}$ or $D_{4}$.
The first one contains $20$ roots, the second contains $24$ roots.
In both cases exactly six roots of $S$ are in $E_{7}^{(a)}$.

###### Proof.

(i) Recall that $|b\cdot c|\leq 2$ for any roots $b$, $c\in R(E_{8})$.
If $b\cdot c=\pm 2$ then $b=\pm c$.
We can assume that $a\cdot c=-1$ (if not we replace $c$ by $-c$).
The lattice $A_{2}(a,c)=\mathbb{Z}a+\mathbb{Z}c$ is a lattice of $A_{2}$-type.
Any $A_{2}$-lattice contains six roots

$R(A_{2}(a,c))=\{\,\pm a,\,\,\pm c,\,\,\pm(a+c)\,\}.$

$A_{2}(a,c)$ is generated by any pair of linearly independent roots.
Therefore

$A_{2}(a,c_{1})\cap A_{2}(a,c_{2})=\{\pm a\}$

if the root lattices are distinct.

(ii) $c\neq\pm d$ implies that $c\cdot d=0$ or $\pm 1$.
Suppose that $c\cdot d=0$.
Then the sum of the lattices is of type $A_{3}$ ($a\cdot c=a\cdot d=-1$ and $c\cdot d=0$).
This lattice contains $12$ roots

$R(A_{3}(a,c,d))=\pm(a,\ c,\ d,\ a+c,\ a+d;\ a+c+d).$

The first five roots are elements of $X_{114}$ and $a+c+d\in E_{7}^{(a)}$.

If $c\cdot d=1$ then $(a+d)\cdot c=0$ and we come back to the first case.
If $c\cdot d=-1$ then $(a+d)\cdot c=-2$, $c=-(a+d)$ and $A_{2}(a,c)=A_{2}(a,d)$.

(iii) As in the proof of 2) we can suppose that $c_{1}\cdot c_{2}=c_{2}\cdot c_{3}=0$ and $c_{1}\cdot c_{3}=0$ or $1$.

If $c_{1}\cdot c_{3}=1$, then we see that $S$ has a root basis of type $A_{4}$.

$A_{4}$ has $20$ roots.
They are

$\pm(a,\ c_{i},\ a+c_{i},\ a+c_{1}+c_{2},\ a+c_{2}+c_{3},\ c_{1}-c_{3})\quad\text{where }i=1,2,3.$

Only the last three roots belong to $E_{7}^{(a)}$.

If $c_{1}\cdot c_{3}=0$ then the roots $c_{1}$, $a$, $c_{2}$, $c_{3}$ form a basis of $S$.
In this case $S$ has type $D_{4}$ ($a\cdot c_{i}=-1$ for all $i$ and the other scalar products are zero).
This root system contains all roots of $A_{4}$ except $\pm(c_{1}-c_{3})$ and the roots

$\pm(a+c_{1}+c_{3},\ a+c_{1}+c_{2}+c_{3},\ 2a+c_{1}+c_{2}+c_{3}).$

The six roots from $E_{7}^{(a)}$ are $\pm(a+c_{i}+c_{j})$.
$\Box$

Now we can finish the proof of Theorem 6.3. Let us assume that every $l\in E_{7}^{(a)}$ with $l^{2}=2d>0$ is orthogonal to at least 14 roots in $E_{8}$ including $\pm a$.
The others are some roots in $E_{7}^{(a)}$ (126 roots), or in $X_{114}\setminus\{\pm a\}$ (112 roots).
If $l$ is orthogonal to $b\in X_{114}\setminus\{\pm a\}$ then $l$ is orthogonal to the lattice $A_{2}(a,b)$.
Therefore using Lemma 6.4 we have

$l\in\bigcup_{i=1}^{28}(A_{2}^{(i)})^{\perp}_{E_{8}}\cup\bigcup_{j=1}^{63}(A_{1}^{(j)})^{\perp}_{E_{7}}.$ (27)

We recall that $(A_{2})^{\perp}_{E_{8}}\cong E_{6}$, $(A_{1})^{\perp}_{E_{7}}\cong D_{6}$ and $(A_{1}\oplus A_{1})^{\perp}_{E_{8}}\cong D_{6}$.
Let denote by $n(l)$ the number of components in (27) containing the vector $l$.
We have calculated this vector exactly $n(l)$ times in the sum

$28N_{E_{6}}(2d)+63N_{D_{6}}(2d).$

We shall consider several cases.

(a).
Suppose that $l\cdot c\neq 0$ for any $c\in X_{114}\setminus\{\pm a\}$.
Then $l$ is orthogonal to at least 6 copies of $A_{1}$ in $E_{7}^{(a)}$ and $n(l)\geq 6$.

Now we suppose that there exist $c\in X_{114}\setminus\{\pm a\}$ such that $l\cdot c=0$.
Then $l$ is orthogonal to $A_{2}(a,c)$ which is one of the 28 subsystems of the bouquet $X_{114}$.

(b).
If $l$ is orthogonal to only one $A_{2}^{(i)}$ (6 roots) then $l$ is orthogonal to at least 4 copies of $A_{1}$ (8 roots) in $E_{7}^{(a)}$.
Thus $n(l)\geq 5$.

(c).
If $l$ is orthogonal to exactly two $A_{2}^{(i)}$ and $A_{2}^{(j)}$ in $X_{114}$ then $l$ is orthogonal to $A_{3}=A_{2}^{(i)}+A_{2}^{(j)}$ having 12 roots and containing only one $A_{1}$ from $E_{7}^{(a)}$.
Thus $l$ is orthogonal to another $A_{1}$ in $E_{7}^{(a)}$.
Therefore $n(l)\geq 4$.

(d).
If $l$ is orthogonal to three or more $A_{2}^{(i)}$ then their sum contains three $A_{1}\subset E_{7}^{(a)}$ and $n(l)\geq 6$.

We see that under our assumption $n(l)\geq 4$ for any $l\in E_{7}^{(a)}$.
Therefore we have proved that if every $l\in E_{7}^{(a)}$ with $l^{2}=2d$ is orthogonal to at least 14 roots then

$28N_{E_{6}}(2d)+63N_{D_{6}}(2d)\geq 4N_{E_{7}}(2d).$

Moreover $n(l)$ can be equal to 4 only in case (c).
In this case $l\in(A_{3})^{\perp}_{E_{8}}\cong D_{5}$ and there are $\binom{28}{2}=378$ pairs of $A_{2}$-subsystems in $X_{114}$.
This gives us the second inequality

$28N_{E_{6}}(2d)+63N_{D_{6}}(2d)\geq 5N_{E_{7}}(2d)-378N_{D_{5}}(2d).$

$\Box$

The inequalities (25) and (26) fail only for a finite number of $d$ because their left- and right-hand sides have the asymptotics $O(d^{5/2})$ and $O(d^{2})$.

###### Proposition 6.5

A vector $l\in E_{8}$ satisfying the condition (24) does exist if $d\not\in P_{ex}$, where

$P_{ex}=\{\,1\leq m\leq 100\,\,(m\neq 96);\quad 101\leq m\leq 127\,\,(m\mbox{ is }odd);$
$m=110,\,\,131,137,\,\,143\,\}.$

Proof.
The Jacobi theta-series of the lattice $E_{8}$ coincides with the Jacobi-Eisenstein series $E_{4,1}(\tau,z)$ of weight 4 and index 1. Let us fix a root $a\in E_{8}$.
We have

$E_{4,1}(\tau,z)=\sum_{l\in E_{8}}\exp(\pi i\,l^{2}\tau+2\pi i\,l\cdot az)=1+\sum_{m\geq 1}e_{4,1}(m,n)\exp(2\pi m\tau+nz).$

$N_{E_{7}}(2m)=e_{4,1}(m,0)$, since the orthogonal complement of $a$ in $E_{8}$ is $E_{7}$.

The Fourier coefficients $e_{4,1}(m,n)$ were calculated in _[x10]_.
In particular

$N_{E_{7}}(2m)=\frac{2^{6}\pi^{3}}{15}\frac{L_{4m}^{Z}(3)}{\zeta(3)}\,m^{5/2}$

where

$L_{D}^{Z}(s)=\sum_{t\geq 1}\frac{\#\{\,x\mod 2t\mid x^{2}\equiv D\mod 4t\,\}\,}{t^{s}}.$

It is evident that $L_{4m}^{Z}(3)>9/8$ (one has to take only two terms for $t=1$ and $t=2$).
Thus

$N_{E_{7}}(2m)>\frac{24\pi^{3}}{5\zeta(3)}\,m^{5/2}>c(E_{7})m^{5/2},$ (28)

where $c(E_{7})=123.8$.
In fact this estimate is quite good: a computation with PARI shows that $N_{E_{7}}(314)\approx 124.73\times(157)^{5/2}$

We can find simple exact formulae for $N_{E_{6}}(2m)$ and $N_{D_{6}}(2m)$.
Let $\chi_{3}$ and $\chi_{4}$ be the unique non-trivial Dirichlet characters modulo 3 and 4 respectively.
For a Dirichlet character $\chi$ we put

$\sigma_{k}(m,\chi)=\sum_{d|m}\chi(d)d^{k},\qquad\tilde{\sigma}_{k}(m,\chi)=\sum_{d|m}\chi\left(\frac{m}{d}\right)d^{k}.$

###### Lemma 6.6

The number of representations of $2m$ by the quadratic forms $E_{6}$ and $D_{6}$ are

$N_{E_{6}}(2m)$ $=81\tilde{\sigma}_{2}(m,\chi_{3})-9\sigma_{2}(m,\chi_{3}),$
$N_{D_{6}}(2m)$ $=64\tilde{\sigma}_{2}(m,\chi_{4})-4\sigma_{2}(m,\chi_{4}).$

Proof.
The second identity is well-known.
This is the number of representations of $2m$ by six squares.
To prove the first identity we consider the theta-series of $E_{6}$:

$\theta_{E_{6}}(\tau)=\sum_{l\in E_{6}}e^{\pi i(l\cdot l)}\in M_{3}(\Gamma_{0}(3),\chi_{3})=M_{3}(\Gamma_{1}(3)).$

The dimension of $M_{3}(\Gamma_{1}(3))$ is equal to $2$.
We can construct a basis with the help of Eisenstein series $G_{k}^{\alpha}$, where $\alpha=(a,b)\in(\mathbb{Z}/N\mathbb{Z})^{2}$,

$G_{k}^{\alpha}(\tau)=\sum_{(n,m)\equiv(a,b)\mod N}(n\tau+m)^{-k}.$

Using the relation $G_{k}^{\alpha}|_{k}\gamma=G_{k}^{\alpha\gamma}$ (where $\gamma\in\mathrm{SL}_{2}(\mathbb{Z})$) for $k=3$ and $N=3$ we obtain two modular forms in $M_{3}(\Gamma_{1}(3))$, namely $G_{3}^{(0,1)}$ and $G_{3}^{(1,0)}+G_{3}^{(1,1)}+G_{3}^{(1,2)}$.
The Fourier expansion of $G_{k}^{\alpha}$ was found by Hecke (see _[x11]_).
Normalising both series we obtain a basis of $M_{3}(\Gamma_{0}(3),\chi_{3})$ consisting of

$E_{3}^{(\infty)}(\tau,\chi_{3})$ $=1-9\sum_{m\geq 1}\sigma_{2}(m,\chi_{3})q^{m},$
$E_{3}^{(0)}(\tau,\chi_{3})$ $=\sum_{m\geq 1}\tilde{\sigma}_{2}(m,\chi_{3})q^{m}\qquad\qquad(q=e^{2\pi i\tau}).$

We note that the first series is proportional to $(\eta^{3}(\tau)/\eta(3\tau))^{3}$ and it vanishes at the cusp $0$.
The second series vanishes at $i\infty$.
The lattice $E_{6}$ has $72$ roots.
Therefore

$\theta_{E_{6}}(\tau)=81E_{3}^{(0)}(\tau,\chi_{3})+E_{3}^{(\infty)}(\tau,\chi_{3}).$ (29)

This gives us the formula for $N_{E_{6}}(2m)$.
Applying the same method to the theta-series $\theta_{D_{6}}\in M_{3}(\Gamma_{0}(4),\chi_{4})$ we obtain that

$\theta_{D_{6}}(\tau)=64E_{3}^{(0)}(\tau,\chi_{4})+E_{3}^{(\infty)}(\tau,\chi_{4}),$ (30)

where

$E_{3}^{(\infty)}(\tau,\chi_{4})$ $=1-4\sum_{m\geq 1}\sigma_{2}(m,\chi_{4})q^{m},$
$E_{3}^{(0)}(\tau,\chi_{4})$ $=\sum_{m\geq 1}\tilde{\sigma}_{2}(m,\chi_{4})q^{m}.$

$\Box$

##

Using these representations we can get an upper bound for $N_{E_{6}}(2m)$ and $N_{D_{6}}(2m)$.
It is clear that

$\sigma_{2}(m,\chi_{3})=\chi_{3}(m)\tilde{\sigma}_{2}(m,\chi_{3})\qquad\text{if}\ \ m\not\equiv 0\mod 3.$

For any $C\equiv 1\mod 3$ we have the following bound

$\frac{\tilde{\sigma}_{2}(m,\chi_{3})}{m^{2}}=\sum_{d|m}\frac{\chi_{3}(d)}{d^{2}}<\sum_{1\leq l\leq C,\ l\equiv 1\mod 3}l^{-2}+\bigg{(}\zeta(2)-\sum_{1\leq n\leq C+2,}n^{-2}\bigg{)}.$

Taking $C=19$ we get that for any $m$ not divisible by $3$

$N_{E_{6}}(2m)=\tilde{\sigma}_{2}(m,\chi_{3})(81-9\chi_{3}(m))<c(E_{6})m^{2},$ (31)

where $c(E_{6})=103.69$.

If $m=3^{k}m_{1}$ then $\sigma_{2}(m,\chi_{3})=\sigma_{2}(m_{1},\chi_{3})$, so the last inequality is valid for any $m$.
For $D_{6}$ one can take $C=21$ in a similar sum.
As a result we get

$N_{D_{6}}(2m)<c(D_{6})m^{2},$ (32)

where $c(D_{6})=75.13$.

Using the estimates (28), (31) and (32) for $N_{L}(2m)$, where $L=E_{7}$, $E_{6}$ and $D_{6}$, we obtain that the main inequality (25) of Theorem 6.3 is valid if

$m\geq 238>\bigg{(}\frac{28c(E_{6})+63c(D_{6})}{4c(E_{7})}\bigg{)}^{2}.$

For smaller $m$ we can use another formula for the theta-series of $E_{7}$ (see _[x10]_)

$\theta_{E_{7}}(\tau)=\theta_{3}(2\tau)^{7}+7\theta_{3}(2\tau)^{3}\theta_{2}(2\tau)^{4},$ (33)

where

$\theta_{3}(2\tau)=\sum_{n=-\infty}^{\infty}q^{n^{2}},\qquad\theta_{2}(2\tau)=\sum_{n=-\infty}^{\infty}q^{(n+\frac{1}{2})^{2}}.$

Moreover (see _[x10]_)

$\theta_{D_{n}}(\tau)=\frac{1}{2}(\theta_{3}(\tau)^{n}+\theta_{3}(\tau+1)^{n}).$ (34)

Using (33) and (34) together with (29) we can compute (using PARI) the first $240$ Fourier coefficients of the function

$5\theta_{E_{7}}-28\theta_{E_{6}}-63\theta_{D_{6}}-378\theta_{D_{5}}.$

The indices of the negative coefficients form the set $P_{ex}$ of $d$ for which the inequality (26) of Theorem 6.3 fails.
$\Box$

Now we are going to analyse the main condition (24) for some $d \in P_{ex}$ from Proposition 6.5. Moreover we are also looking for vectors with $d \leq 61$ orthogonal to exactly 14 roots.
Such vectors produce cusp forms $F_{l}$ of weight 19 due to Theorem 6.2.

Let $e_i$ ( $1 \leq i \leq 8$ ) be a euclidean basis of the lattice $\mathbb{Z}^8$ ( $(e_i, e_j) = \delta_{ij}$ ).
We consider the Coxeter basis of simple roots in $E_8$ (see [Bou])

![img-0.jpeg](img-0.jpeg)

where

$$
\alpha_ {1} = \frac {1}{2} (e _ {1} + e _ {8}) - \frac {1}{2} (e _ {2} + e _ {3} + e _ {4} + e _ {5} + e _ {6} + e _ {7}),
$$

$$
\alpha_ {2} = e _ {1} + e _ {2}, \quad \alpha_ {k} = e _ {k - 1} - e _ {k - 2} \quad (3 \leq k \leq 8)
$$

and $E_8 = \langle \alpha_1,\ldots \alpha_8\rangle_{\mathbb{Z}}$

Let $L_{S} = \langle \alpha_{i} \mid i \in S \rangle_{\mathbb{Z}} \subset E_{8}$ be a sublattice of $E_{8}$ generated by some simple roots $(S \subset \{1, \ldots, 8\})$ .
We assume that $\# R(L_{S}) \leq 12$ , where $R(L_{S})$ is the set of roots of $L_{S}$ .
We can find the orthogonal complement of $L_{S}$ in $E_{8}$ using fundamental weights $\omega_{j}$ , i.e. the basis of $E_{8}$ dual to the basis $\{\alpha_{i}\}_{i=1}^{8}$ .
We have

$$
L _ {S} ^ {\perp} = (L _ {S}) _ {E _ {8}} ^ {\perp} = \langle \omega_ {j} \mid j \notin S \rangle_ {\mathbb {Z}}.
$$

Any vector of $L_S^\perp$ is orthogonal to all roots of $L_S$ .
If $l \in L_S^\perp$ is orthogonal to an additional root $r$ of $E_8$ ( $r \notin R(L_S)$ ) then we obtain a linear relation on the coordinates of $l$ in the basis $\omega_j$ ( $j \notin S$ ).
Considering all roots of $E_8$ we can formulate a condition on the coordinates of $l \in L_S^\perp$ to be orthogonal to at most 12 roots (or to exactly 14 roots).
We shall analyse four different lattices $L_S$ .

I.
$L_{1} = 4A_{1}$ ， $\# R(4A_1) = 8$ and $L_{1}^{\perp} = 4A_{1}$

We put

$$
L _ {1} = \langle \alpha_ {2}, \alpha_ {3}, \alpha_ {5}, \alpha_ {7} \rangle_ {\mathbb {Z}} = \langle e _ {2} + e _ {1}, e _ {2} - e _ {1}, e _ {4} - e _ {3}, e _ {6} - e _ {5} \rangle_ {\mathbb {Z}} \cong 4 A _ {1}.
$$

This root lattice $L_{1}$ gives us vectors of norm $2d$ for most $d \in P_{ex}$ .
$L_{1}$ is a primitive sublattice of $E_{8}$ .
Therefore $L_{1}^{\perp}$ is a lattice with the same discriminant form and $L_{1}^{\perp} \cong 4A_{1}$ .
More exactly,

$$
L _ {1} ^ {\perp} = \langle \omega_ {1}, \omega_ {4}, \omega_ {6}, \omega_ {8} \rangle_ {\mathbb {Z}} = \langle e _ {3} + e _ {4}, e _ {5} + e _ {6}, e _ {7} + e _ {8}, e _ {7} - e _ {8} \rangle_ {\mathbb {Z}}.
$$

This representation follows easily from the formulae for the fundamental weights of $E_8$ (see [Bou, Plat VII]):

$$
\omega_ {2} = \frac {1}{2} (e _ {1} + \dots + e _ {7} + 5 e _ {8}), \quad \omega_ {3} = \frac {1}{2} (- e _ {1} + e _ {2} + \dots + e _ {7} + 7 e _ {8}),
$$

$$
\omega_ {k} = e _ {k - 1} + \dots + e _ {7} + (9 - k) e _ {8} \quad (4 \leq k \leq 8), \quad \omega_ {1} = 2 e _ {8}.
$$

Any vector

$l=m_{3}(e_{3}+e_{4})+m_{5}(e_{5}+e_{6})+m_{7}(e_{7}+e_{8})+m_{8}(e_{7}-e_{8})\in L_{1}^{\perp}$ (35)

is orthogonal to 8 roots of $L_{1}$.
The root system of $E_{8}$ contains 112 integral and 128 half-integral roots:

$\pm e_{i}\pm e_{j}\quad(i<j),\quad\frac{1}{2}\sum_{i=1}^{8}(-1)^{\nu_{i}}e_{i}\quad\text{with}\ \ \sum_{i=1}^{8}\nu_{i}\equiv 0\mod 2.$

If $l$ is orthogonal to a half-integral root $r$ then

\[ 2(l\cdot r)=m*{7}((-1)^{\nu*{7}}+(-1)^{\nu*{8}})+m*{8}((-1)^{\nu*{7}}-(-1)^{\nu*{8}})+\\
m*{3}((-1)^{\nu*{3}}+(-1)^{\nu*{4}})+m*{5}((-1)^{\nu*{5}}+(-1)^{\nu*{6}})=0.
\] (36)

We note that only one of $m_{7}$ or $m_{8}$ appears.
Let us assume that this identity contains three non-zero terms: $m_{7,8}\pm m_{3}\pm m_{5}=0$ (by $m_{7,8}$ we mean $m_{7}$ or $m_{8}$).
Then $l$ is orthogonal to 4 additional half-integral roots.
There are two choices for $(\nu_{1},\nu_{2})$ and one can change the sign of the root.
A similar result, i.e. a relation $m_{7}\pm m_{8}\pm m_{3,5}=0$ and 4 additional integral roots, is obtained if $l$ is orthogonal to the integral roots $e_{7,8}\pm e_{3,4}$ or $e_{7,8}\pm e_{5,6}$.

If (36) contains only two non-zero terms then we have a relation of type $m_{7,8}\pm m_{3,5}=0$.
In this case $l$ is orthogonal to 8 additional half-integral roots: there are two choices for $(\nu_{3},\nu_{4})$ (or $(\nu_{5},\nu_{6})$), for $(\nu_{1},\nu_{2})$ and the change of the sign.
We can also have $m_{7,8}=0$, and then the number of half-integral roots orthogonal to $l$ is equal to 16.

If $l$ is orthogonal to an integral root $r\not\in L_{1}$, which has not been considered above, then we get a relation $m_{3}=\pm m_{5}$ or $m_{7}=\pm m_{8}$ with 8 additional roots or $m_{3,5}=0$ with 16 additional integral roots.
For example, if $m_{7}=m_{8}$ then $l$ is orthogonal to $\pm(e_{8}\pm e_{1,2})$; if $m_{3}=0$ then $l$ is orthogonal to $\pm(e_{3,4}\pm e_{1,2})$.
Therefore we have proved the following

###### Proposition 6.7

$l\in L_{1}^{\perp}$ (see (35)) is orthogonal to at least $8$ and at most $12$ roots of $E_{8}$ if and only if

- $m_{j}\neq 0$ for any $j$ and $m_{i}\neq m_{j}$ for any $i\neq j$;
- There is at most one relation of type $m_{k}=\pm m_{i}\pm m_{j}$ for $i<j<k$.

This lemma gives us a set of vectors $l\in L_{1}^{\perp}$ with

$l^{2}=2(m_{3}^{2}+m_{5}^{2}+m_{7}^{2}+m_{8}^{2})=2d\in P_{ex}$

such that $l$ is orthogonal to 8 or to 12 roots of $E_{8}$.
We list these vectors in table I-8,12.

| I-8,12.
L1=4A1, l=(m3,m5,m7,m8)∈L1↓ | | | | | |
| ---------------------------------- | --------- | --- | --------- | --- | ---------- |
| d | l | d | l | d | l |
| 46 | (1,2,4,5) | 84 | (1,3,5,7) | 110 | (1,3,6,8) |
| 50 | (1,2,3,6) | 85 | (1,2,4,8) | 111 | (1,2,5,9) |
| 54 | (2,3,4,5) | 86 | (3,4,5,6) | 113 | (2,3,6,8) |
| 57 | (1,2,4,6) | 90 | (1,2,6,7) | 117 | (1,4,6,8) |
| 62 | (1,3,4,6) | 91 | (1,4,5,7) | 119 | (2,3,5,9) |
| 63 | (1,2,3,7) | 93 | (2,3,4,8) | 121 | (1,2,4,10) |
| 65 | (2,3,4,6) | 94 | (1,2,5,8) | 123 | (1,3,7,8) |
| 66 | (1,2,5,6) | 95 | (1,3,6,7) | 125 | (3,4,6,8) |
| 70 | (1,2,4,7) | 98 | (2,3,6,7) | 127 | (1,3,6,9) |
| 71 | (1,3,5,6) | 99 | (3,4,5,7) | 131 | (3,4,5,9) |
| 74 | (2,3,5,6) | 102 | (1,2,4,9) | 137 | (2,4,6,9) |
| 78 | (1,2,3,8) | 105 | (1,2,6,8) | 143 | (1,5,6,9) |
| 79 | (1,2,5,7) | 107 | (1,3,4,9) | | |
| 81 | (2,4,5,6) | 109 | (2,4,5,8) | | |

II.
$L_{2} = 2A_{1}\oplus A_{2},\# R(2A_{1}\oplus A_{2}) = 10.$

Our second example is the sublattice

$$
L _ {2} = \langle \alpha_ {2}, \alpha_ {3}, \alpha_ {5}, \alpha_ {6} \rangle_ {\mathbb {Z}} = \langle e _ {2} + e _ {1}, e _ {2} - e _ {1}, e _ {4} - e _ {3}, e _ {5} - e _ {4} \rangle_ {\mathbb {Z}} \cong 2 A _ {1} \oplus A _ {2}.
$$

Then using the dual basis $\omega_{j}$ we obtain that

$$
\begin{array}{l} L _ {2} ^ {\perp} = \left\langle \omega_ {1}, \omega_ {4}, \omega_ {7}, \omega_ {8} \right\rangle = \left\langle e _ {3} + e _ {4} + e _ {5} + e _ {6}, e _ {6} + e _ {7}, e _ {7} - e _ {8}, e _ {7} + e _ {8} \right\rangle \\ = \left\{l = m _ {5} \left(e _ {3} + e _ {4} + e _ {5}\right) + \sum_ {i = 6} ^ {8} m _ {i} e _ {i} \mid m _ {5} + m _ {6} + m _ {7} + m _ {8} \text {i s e v e n} \right\}. \tag {37} \\ \end{array}
$$

We note that $L_2^\perp$ is not a root lattice.

The vector $l$ is orthogonal to a half-integral root $r$ if

$$
2 (l \cdot r) = m _ {5} ((- 1) ^ {\nu_ {3}} + (- 1) ^ {\nu_ {4}} + (- 1) ^ {\nu_ {5}}) + m _ {6} (- 1) ^ {\nu_ {6}} + m _ {7} (- 1) ^ {\nu_ {7}} + m _ {8} (- 1) ^ {\nu_ {8}} = 0.
$$

There are two different cases:

- if $3m_{5} = \pm m_{6} \pm m_{7} \pm m_{8}$ then there are 4 half-integral roots orthogonal to $l$ , since there are two choices for $(\nu_{1}, \nu_{2})$ and for the sign of $r$ ;
- if $m_5 = \pm m_6 \pm m_7 \pm m_8$ then there are 12 half-integral roots orthogonal to $l$ , since there are three choices for $(\nu_3, \nu_4, \nu_5)$ .

Let us find integral roots of $E_8$ (not in $L_2$ ) orthogonal to $l$ :

- if $m_i = 0$ ( $i = 6, 7$ or 8) then there are 8 roots $\pm (e_{1,2} \pm e_i)$ ;

- if $m_5 = 0$ then there are 24 roots $\pm (e_{1,2} \pm e_{3,4,5})$ ;
- if $m_i = \pm m_5$ ( $i = 6, 7$ or 8) then there are 6 roots $\pm (e_i \mp e_{3,4,5})$ ;
- if $m_i = \pm m_j$ ( $6 \leq i &lt; j \leq 8$ ) then there are 2 roots $\pm (e_i \mp e_j)$ .

Therefore we obtain

Proposition 6.8 $l \in L_2^\perp$ (see (37)) is orthogonal to exactly 10 roots of $E_8$ if and only if

(i) $m_j \neq 0$ for any $j$ and $m_i \neq \pm m_j$ for any $i &lt; j$ ;
(ii) $km_{5}\neq \pm m_{6}\pm m_{7}\pm m_{8}$ , where $k = 1$ or 3.

Moreover $l \in L_2^\perp$ is orthogonal to exactly 14 roots of $E_8$ if (i) and (ii) for $k = 1$ are valid and there is exactly one relation of type $3m_5 = \pm m_6 \pm m_7 \pm m_8$ .

Some $l \in L_2^\perp$ orthogonal to 10 roots in $E_8$ and having norm $l^2 = 3m_5^2 + m_6^2 + m_7^2 + m_8^2 = 2d \in P_{ex}$ are given in table II-10.

| II-10.
L2=2A1 ⊕ A2, l=(m5; m6, m7, m8)∈L2⊥ | | | | | |
| ----------------------------------------- | ------------- | --- | ------------- | --- | ------------- |
| d | l | d | l | d | l |
| 58 | (1; 2, 3, 10) | 75 | (6; 1, 4, 5) | 89 | (2; 6, 7, 9) |
| 60 | (3; 2, 5, 8) | 80 | (3; 4, 6, 9) | 97 | (4; 1, 8, 9) |
| 64 | (5; 1, 4, 6) | 82 | (5; 3, 4, 8) | 100 | (7; 1, 4, 6) |
| 67 | (2; 4, 5, 9) | 83 | (2; 1, 3, 12) | 101 | (4; 1, 3, 12) |
| 72 | (3; 1, 4, 10) | 87 | (6; 1, 4, 7) | 103 | (8; 1, 2, 3) |
| 73 | (4; 3, 5, 8) | 88 | (1; 2, 5, 12) | 115 | (4; 1, 9, 10) |

The vectors from the tables I-8,12 and II-10 produce cusp forms $F_{l}(Z)$ of weights 16, 18 (table I-8,12) or 17 (table II-10) for all $d &gt; 61$ in the set $P_{ex}$ except $d = 68$ , 69, 77, 92.

The vectors from $L_2^\perp$ with $l^2 = 2d$ and $d \leq 61$ that are orthogonal to exactly 14 roots of $E_8$ are given in table II-14.

| II-14.
L2=2A1 ⊕ A2, l=(m5; m6, m7, m8)∈L2⊥ | | | | | |
| ----------------------------------------- | ------------ | --- | ------------ | --- | ------------- |
| d | l | d | l | d | l |
| 40 | (1; 2, 3, 8) | 48 | (3; 1, 2, 8) | 55 | (4; 1, 5, 6) |
| 43 | (2; 1, 3, 8) | 52 | (1; 2, 4, 9) | 61 | (2; 1, 3, 10) |

III.
$L_{3} = A_{3}$ $\# R(A_3) = 12$

The root lattice $A_{3}$ is maximal.
Therefore any sublattice of type $A_{3}$ in $E_{8}$ is primitive.
Analysing the discriminant form of the orthogonal complement of $A_{3}$ we obtain that it is isomorphic to $D_{5}$ .
We put

$$
L _ {3} = \langle \alpha_ {2}, \alpha_ {4}, \alpha_ {3} \rangle_ {\mathbb {Z}} = \langle e _ {2} + e _ {1}, e _ {3} - e _ {2}, e _ {2} - e _ {1} \rangle_ {\mathbb {Z}} \cong A _ {3}.
$$

Then

$$
L _ {3} ^ {\perp} = \left\{l = \sum_ {i = 4} ^ {8} m _ {i} e _ {i} \mid \sum_ {i = 4} ^ {8} m _ {i} \equiv 0 \mod 2 \right\} \cong D _ {5}.
$$

As above we obtain

Proposition 6.9 $l \in L_3^\perp$ is orthogonal to exactly 12 roots of $E_8$ if and only if

(i) $m_j \neq 0$ for any $j$ ;
(ii) $m_{i}\neq \pm m_{j}$ for any $i &lt;   j$
(iii) $\sum_{i=4}^{8} \pm m_i \neq 0$ for any choice of the signs.

Moreover $l \in L_3^\perp$ is orthogonal to exactly 14 roots of $E_8$ if (i) and (iii) are valid and there is only one relation of type $m_i = \pm m_j$ for $4 \leq i &lt; j \leq 8$ .

See table III for several vectors $l \in L_3^\perp$ orthogonal to $N_l$ roots ( $N_l = 12$ or 14) in $E_8$ and having norm $l^2 = \sum_{i=4}^{8} m_i^2 = 2d$ .

| III.
L3 = A3, l = (m4, m5, m6, m7, m8) ∈ L3⊥ | | | | | |
| ------------------------------------------- | ----------- | --- | --- | ------------ | --- |
| d | l | Nl | d | l | Nl |
| 69 | (2,3,5,6,8) | 12 | 53 | (1,4,4,3,8) | 14 |
| 42 | (1,3,3,4,7) | 14 | 54 | (1,3,3,5,8) | 14 |
| 48 | (1,1,2,3,9) | 14 | 56 | (1,1,5,6,7) | 14 |
| 49 | (2,2,4,5,7) | 14 | 59 | (1,2,2,3,10) | 14 |
| 51 | (1,6,6,2,5) | 14 | 63 | (3,4,4,6,7) | 14 |

IV.
$L_{4} = A_{1}\oplus A_{2},\# R(A_{1}\oplus A_{2}) = 8.$

For any sublattice $A_1 \oplus A_2$ in $E_8$ we see that its orthogonal complement is isomorphic to $A_5$ , since $(A_2)_{E_8}^{\perp} = E_6$ and $(A_1)_{E_6}^{\perp} = A_5$ .
We put $L_4 = \langle \alpha_1, \alpha_2, \alpha_3 \rangle_{\mathbb{Z}} \cong A_1 \oplus A_2$ .
Then

$$
L _ {4} ^ {\perp} = \left\{l = \sum_ {i = 3} ^ {8} m _ {i} e _ {i} \mid m _ {8} = \sum_ {i = 3} ^ {7} m _ {i} \right\}.
$$

If $l$ is orthogonal to a half-integral root distinct from $\alpha_{1}$ , $\alpha_{1} + \alpha_{3} \in L_{4}$ then we get a relation of the form

$$
m _ {i _ {1}} + \dots + m _ {i _ {k}} = 0, \quad \text {w h e r e} \quad 3 \leq i _ {1} &lt;   \dots i _ {k} \leq 7, \quad 1 \leq k \leq 5.
$$

If any relation of this type is valid then $l$ is orthogonal to 4 additional half-integral roots.
Considering the scalar products with integral roots we see that

- if $m_i = 0$ ( $3 \leq i \leq 8$ ) then $l$ is orthogonal to 8 roots $\pm (e_{1,2} \pm e_i)$ ;

- if $m_i = \pm m_j$ ( $3 \leq i &lt; j \leq 8$ ) then $l$ is orthogonal to 2 roots $\pm (e_i \mp e_j)$ .

We list some cases of these results in table IV.

| IV.
L4 = A1 ⊕ A2, l = (m3, m4, m5, m6, m7; m8) ∈ L4+ | | | | | |
| --------------------------------------------------- | --------------- | --- | --- | ---------------- | --- |
| d | l | Nl | d | l | Nl |
| 68 | (1,3,4,5,-7; 8) | 12 | 92 | (1,1,2,3,5; 12) | 10 |
| 77 | (2,3,4,5,-8; 6) | 12 | 40 | (1,1,2,3,-8; -1) | 14 |

It is possible to formulate a result for this case analogous to Propositions 6.7, 6.8 and 6.9, but we do not need it.

An extensive computer search for vectors $l$ orthogonal to at least 2 and at most 14 roots for other $d \in P_{ex}$ has not found any.

Now we have everything we need to prove our main theorem, Theorem 1. For $d &gt; 61$ and for $d = 46, 50, 54, 57, 58, 60$ there exists a vector $l$ satisfying condition (24), either by Proposition 6.5 or listed in one of the tables.
Hence Theorem 6.2 provides us with a suitable cusp form of low weight.
Since the dimension of $\mathcal{F}_{2d}$ is 19, Theorem 2.1 guarantees the existence of a compactification with only canonical singularities and hence Theorem 1 follows by using the low weight cusp form trick, according to Theorem 1.1.

If $d$ is not as above but $d \geq 40$ and $d \neq 41, 44, 45, 47$ then we have a cusp form of weight 19 arising from a vector $l$ orthogonal to 14 roots, listed in one of the tables.
This gives rise to a canonical form and hence, by Freitag's result, the Kodaira dimension of $\mathcal{F}_{2d}$ is non-negative, as stated in Theorem 1.1.

# References

[AMRT] A.
Ash, D.
Mumford, M.
Rapoport, Y.
Tai, Smooth compactification of locally symmetric varieties.
Lie Groups: History, Frontiers and Applications, Vol.
IV.
Math.
Sci.
Press, Brookline, Mass., 1975.
[BB] W.L.
Baily Jr., A.
Borel, Compactification of arithmetic quotients of bounded symmetric domains.
Ann.
of Math.
(2) 84 (1966), 442-528.
[B] R.E.
Borcherds, Automorphic forms on $\mathrm{O}_{s+2,2}(\mathbb{R})$ and infinite products.
Invent.
Math.
120 (1995), 161-213.
[BKPS] R.E.
Borcherds, L.
Katzarkov, T.
Pantev, N.I.
Shepherd-Barron, Families of K3 surfaces.
J.
Algebraic Geom.
7 (1998), 183-193.
[Bou] N.
Bourbaki, Groupes et algèbres de Lie. Chapitre IV: Groupes de Coxeter et systèmes de Tits.
Chapitre V: Groupes engendrés par des réflexions.
Chapitre VI: systèmes de racines.
Éléments de mathématique.
Fasc.
XXXIV.
Actualités Scientifiques et Industrielles, No.
1337 Hermann, Paris, 1968.

[CS] J.H.
Conway, N.J.A.
Sloane, Sphere packings, lattices and groups.
Grundlehren der mathematischen Wissenschaften 290. Springer-Verlag, New York, 1988.

- [E] M.
  Eichler, Quadratische Formen und orthogonale Gruppen.
  Grundlehren der mathematischen Wissenschaften 63. Springer-Verlag, Berlin–Göttingen–Heidelberg, 1952.
- [EZ] M.
  Eichler, D.
  Zagier, The theory of Jacobi forms.
  Progress in Mathematics 55. Birkhäuser, Boston, Mass., 1985.
- [G] V.
  Gritsenko, Modular forms and moduli spaces of abelian and K3 surfaces.
  Algebra i Analiz 6 (1994), 65–102; English translation in St.
  Petersburg Math.
  J.
  6 (1995), 1179–1208.
- [GH1] V.
  Gritsenko, K.
  Hulek, Appendix to the paper “Irrationality of the moduli spaces of polarized abelian surfaces”.
  Abelian varieties.
  Proceedings of the international conference held in Egloffstein, 83–84.
  Walter de Gruyter Berlin, 1995.
- [GH2] V.
  Gritsenko, K.
  Hulek, Minimal Siegel modular threefolds.
  Math.
  Proc.
  Cambridge Philos.
  Soc.
  123 (1998), 461–485.
- [GHS1] V.
  Gritsenko, K.
  Hulek, G.K.
  Sankaran, The Hirzebruch-Mumford volume for the orthogonal group and applications.
  Preprint 2005 (math.NT/0512595, 27 pp.)
- [GHS2] V.
  Gritsenko, K.
  Hulek, G.K.
  Sankaran, The orthogonal modular varieties of K3 types (in preparation).
- [GN] V.
  Gritsenko, V.V.
  Nikulin, Automorphic forms and Lorentzian Kac-Moody algebras.
  II.
  Internat.
  J.
  Math.
  9 (1998), 201–275.
- [GS] V.
  Gritsenko, G.K.
  Sankaran, Moduli of abelian surfaces with a $(1,p^{2})$ polarisation.
  Izv.
  Ross.
  Akad.
  Nauk Ser.
  Mat.
  60 (1996), 19–26; reprinted in Izv.
  Math.
  60 (1996), 893–900.
- [HW] G.H.
  Hardy, E.M.
  Wright, An introduction to the theory of numbers.
  Fifth edition.
  Oxford University Press, Oxford, 1979.
- [Kob] N.
  Koblitz Introduction to elliptic curves and modular forms.
  Graduate Texts in Mathematics 97. Springer-Verlag, New York, 1984.
- [Ko1] S.
  Kondo, On the Kodaira dimension of the moduli space of K3 surfaces.
  Compositio Math.
  89 (1993), 251–299.
- [Ko2] S.
  Kondo, On the Kodaira dimension of the moduli space of K3 surfaces.
  II.
  Compositio Math.
  116 (1999), 111–117.

[Mu1] S.
Mukai, Curves, K3 surfaces and Fano $3$-folds of genus $\leq 10$.
Algebraic geometry and commutative algebra, Vol.
I, 357–377, Kinokuniya, Tokyo, 1988.

- [Mu2] S.
  Mukai, Polarized K3 surfaces of genus $18$ and $20$.
  Complex projective geometry (Trieste, 1989/Bergen, 1989), 264–276, London Math.
  Soc.
  Lecture Note Ser., 179, Cambridge Univ.
  Press, Cambridge, 1992.
- [Mu3] S.
  Mukai, Curves and K3 surfaces of genus eleven.
  Moduli of vector bundles (Sanda, 1994; Kyoto, 1994), 189–197, Lecture Notes in Pure and Appl.
  Math., 179, Dekker, New York, 1996.
- [Mum] D.
  Mumford, Hirzebruch’s proportionality theorem in the noncompact case.
  Invent.
  Math.
  42 (1977), 239–272.
- [Nik1] V.V.
  Nikulin, Finite automorphism groups of Kähler K3 surfaces.
  Trudy Moskov.
  Mat.
  Obshch.
  38 (1979), 75–137.
  English translation in Trans.
  Mosc.
  Math.
  Soc.
  2, 71-135 (1980).
- [Nik2] V.V.
  Nikulin, Integral symmetric bilinear forms and some of their applications.
  Izv.
  Akad.
  Nauk SSSR Ser.
  Mat.
  43 (1979), 111–177.
  English translation in Math.
  USSR, Izvestiia 14 (1980), 103–167.
- [Nik3] V.
  Nikulin, Factor groups of automorphisms of hyperbolic forms with respect to subgroups generated by $2$-reflections.
  Algebro-geometric applications.
  Itogi Nauki Tekh., Ser.
  Sovrem.
  Probl.
  Mat.
  18 (1981), 3–114.
  English translation in J.
  Sov.
  Math.
  22 (1983), 1401–1475.
- [Od] T.
  Oda, Convex bodies and algebraic geometry.
  Ergebnisse der Mathematik und ihrer Grenzgebiete (3) 15. Springer-Verlag, Berlin, 1988.
- [P-SS] I.
  Piatetskii-Shapiro, I.
  Shafarevich, A Torelli theorem for algebraic surfaces of type K3.
  Izv.
  Akad.
  Nauk SSSR, Ser.
  Mat.
  35, 530-572 (1971).
  English translation in Math.
  USSR, Izv.
  5 (1971), 547-588 (1972).
- [Re] M.
  Reid, Canonical $3$-folds.
  Journées de Géometrie Algébrique d’Angers 1979, 273–310.
  Sijthoff &amp; Noordhoff, Alphen aan den Rijn, 1980.
- [Sc] F.
  Scattone, On the compactification of moduli spaces of algebraic K3 surfaces., Mem.
  Amer.
  Math.
  Soc.
  70, no.
  374, (1987)
- [S-B] N.I.
  Shepherd-Barron, Perfect forms and the moduli space of abelian varieties.
  Invent.
  Math.
  163 (2006), 25–45.

[Sn] V.
Snurnikov, Quotients of canonical toric singularities.
Ph.D.
thesis, Cambridge 2002.

- [T] Y.
  Tai, On the Kodaira dimension of the moduli space of abelian varieties.
  Invent.
  Math.
  68 (1982), 425–439.

V.A.
Gritsenko
Université Lille 1
Laboratoire Paul Painlevé
F-59655 Villeneuve d’Ascq, Cedex
France
valery.gritsenko@math.univ-lille1.fr

K.
Hulek
Institut für Algebraische Geometrie
Leibniz Universität Hannover
D-30060 Hannover
Germany
hulek@math.uni-hannover.de

G.K.
Sankaran
Department of Mathematical Sciences
University of Bath
Bath BA2 7AY
England
gks@maths.bath.ac.uk