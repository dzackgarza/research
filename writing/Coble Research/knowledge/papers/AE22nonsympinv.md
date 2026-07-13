---
title: Compactifications of moduli spaces of K3 surfaces with a nonsymplectic involution
authors:
- Valery Alexeev
- Philip Engel
year: 2022
bibkey: AE22nonsympinv
tags:
- paper
- extraction
abstract: |
  There are 75 moduli spaces $F _ { S }$ of K3 surfaces with a nonsymplectic involution.
  We give detailed descriptions of Kulikov models for oneparameter degenerations in $F _ { S }$ .
  In the 50 cases where the fixed locus of the involution has a component $C _ { g }$ of genus $g \ \geq 2$ , we identify normalizations of the KSBA compactifications of $F _ { S }$ via stable pairs $( X , \epsilon C _ { g } )$ , with explicit semitoroidal compactifications of $F _ { S }$ .
---

# COMPACTIFICATIONS OF MODULI SPACES OF K3 SURFACES WITH A NONSYMPLECTIC INVOLUTION

VALERY ALEXEEV AND PHILIP ENGEL

Abstract.
There are 75 moduli spaces $F _ { S }$ of K3 surfaces with a nonsymplectic involution.
We give detailed descriptions of Kulikov models for oneparameter degenerations in $F _ { S }$ . In the 50 cases where the fixed locus of the involution has a component $C _ { g }$ of genus $g \ \geq 2$ , we identify normalizations of the KSBA compactifications of $F _ { S }$ via stable pairs $( X , \epsilon C _ { g } )$ , with explicit semitoroidal compactifications of $F _ { S }$ .

# Contents

1. Introduction

2A. K3 surfaces with a nonsymplectic involution 4\
2B. 2-elementary lattices 6\
2C. Moduli of K3 surfaces with an involution 7\
2D. Baily-Borel, toroidal, and semitoroidal compactifications 8\
2E. Stable pair compactifications 8

3. Reflection groups

3A. Vinberg’s theory 8\
3B. Coxeter, or reflection semifan 10\
3C. Coxeter diagrams for lattices with $g \geq 2$ , excluding $( 1 0 , 8 , 0 )$ 11\
3D. Coxeter diagrams for lattices with $g = 1$ and for $( 1 0 , 8 , 0 )$ 11\
3E. Coxeter diagrams for $( 1 8 , 2 , 1 )$ and $( 1 7 , 3 , 1$ ) 14\
3F. Lattices on the $g = 0$ line 15

4. K3 surfaces, their quotients, and the nef cones 15

4A. Surfaces for $S$ with $g \geq 2$ , excluding $( 1 0 , 8 , 0 )$ 151616\
4B. Surfaces for $S$ on the $g = 1$ line and $( 1 0 , 8 , 0 )$\
4C. Surfaces for $S$ on the $g = 0$ line\
4D. Nef cones and exceptional curves on $X$ and $Y$ 17\
$\mathrm { 4 E }$ . Surfaces $Y$ with the smallest nef cone 1719\
4F. The Heegner divisor hierarchy

5. The cusps of $\mathbb { D } _ { S } / O ( T )$

5A. Isotropic vectors in 2-elementary discriminant groups\
5B. Isotropic vectors in 2-elementary lattices\
5C. The 0-cusps\
5D. The 1-cusps\
5E. 0-cusps and involutions of $L _ { \mathrm { I A S } } = \mathrm { I I } _ { 2 , 1 8 }$

6. Degenerations and integral affine spheres 2727 6A. Kulikov models

6B. Nef, divisor, and stable models 33\
6C. IAS $^ 2$ from Kulikov surfaces\
6D. IAS $^ 2$ from symplectic geometry\
6E. Nodal slides and scaling IAS $^ 2$\
6F. The Mirror Theorem\
6G. Visible curves on IAS2 34

7. Mirror symmetry for K3 surfaces with a nonsymplectic involution 3

7A. A special degeneration 34\
7B. Lagrangian torus fibration for the mirror K3 surfaces 36\
7C. Mirror symmetry and involutions 40

8. Kulikov models of K3 surfaces with a nonsymplectic involution

8A. The main construction 41\
8B. Edge behavior in the gluing of $P$ and $P ^ { \mathrm { o p p } }$\
8C. Models for $\overline { { T } } = ( 1 0 + \bar { k } , 1 0 - \bar { k } , \delta )$ , $1 \leq k \leq 9$\
8D. Models for $\overline { T }$ with $\bar { g } \geq 2$ , excluding $( 1 0 , 8 , 0 )$\
8E. Monodromy invariants for $\overline { { T } } = ( 1 0 , 1 0 , 0 )$\
8F. Models for $\overline { { T } } = ( 1 0 , 8 , 0 )$ , $( 1 0 , 1 0 , 0 )$ , $( 1 0 , 1 0 , 1 )$\
8G. Colliding singularities and non-generic type III models 50\
8H. Type II models 52

9. Compact moduli

9A. The ramification semifan 5354\
9B. Stable models\
9C. The Main Theorem 56

10. Example.
    $S = ( 2 , 2 , 0 )$ : hyperelliptic K3 surfaces of degree 4 5759 References List of Figures 61 List of Tables 61

# 1. Introduction

Let $X$ be a smooth projective K3 surface.
An involution $\iota$ of $X$ is called nonsymplectic if it acts as $\iota ^ { * } \omega _ { X } = - \omega _ { X }$ on a generator of $H ^ { 2 , 0 } ( X )$ . The (+1)-eigenspace of the induced involution on $H ^ { 2 } ( X , \mathbb { Z } )$ is a hyperbolic lattice $S$ . All the possibilities for $S$ were found in a classical work [Nik79a] of Nikulin, who proved that there are 75 cases, given in Fig.

1. The lattices $S$ are uniquely determined by a triple of invariants $( r , a , \delta )$ , or an equivalent set of invariants, $( g , k , \delta )$ .

For a given lattice $S$ , there is a moduli space $F _ { S }$ of K3 surfaces with an involution and generic Picard lattice $S$ . It is an open subset of $\mathbb { D } _ { S } / \Gamma$ , the quotient of a type IV domain of dimension $2 0 - \operatorname { r a n k } S$ by an arithmetic group.

The K3 surfaces that appear include many interesting ones, for example the double covers of: Enriques surfaces, smooth del Pezzo surfaces, log del Pezzo surfaces of index 2, index 2 Halphen pencils, and rational elliptic surfaces.
They have been the subject of a great deal of research.
Here, we are interested in geometric compactifications of the moduli spaces $F _ { S }$ .

In 50 of the 75 cases, the fixed locus $R$ of the involution contains a smooth curve $C _ { g }$ of genus $g \geq 2$ . The divisor $C _ { g }$ is semiample and defines a contraction $X  { \overline { { X } } }$ to a K3 surface with $A D E$ singularities and an ample Cartier divisor $\overline { { C } } _ { g }$ .

It follows that for $0 < \epsilon \ll 1$ the pair $( \overline { { \boldsymbol { X } } } , \epsilon \overline { { \boldsymbol { C } } } _ { g } )$ is a KSBA stable pair, see [Kol23] for their general theory.
Stable pairs have complete, projective moduli spaces.
One thus obtains a geometrically meaningful KSBA compactification $\overline { { F } } _ { S }$ .

Problem 1.1. Describe the compactification $\overline { { F } } _ { S }$ explicitly.

In previous collaborations, we solved this problem in two cases: for the degree 2 K3 surfaces [AET19] and for the elliptic degree 2 K3 surfaces [ABE22], which is a Heegner divisor in the previous case.
In this paper, we solve it for all the remaining cases:

Theorem 1.2. The normalization of $\overline { { F } } _ { S }$ is a semitoroidal compactification of $\mathbb { D } _ { S } / \Gamma$ for an explicit semifan $\mathfrak { F } _ { \mathrm { r a m } }$ . In 48 of the 50 cases it is dominated by a toroidal compactification for a Coxeter reflection fan.

The precise statement is given in Theorem 9.10. We reduce Problem 1.1 to the following problem which we solve for all 75 cases:

Problem 1.3. For each cusp of the Baily-Borel compactification BB $\overline { { F } } _ { S } ^ { \mathrm { B B } }$ and each one-parameter degeneration $C \setminus { 0 \to F _ { S } }$ approaching that cusp, describe explicitly a Kulikov model $X \to ( C , 0 )$ adapted to the ramification divisor $R$ .

A Kulikov model is a $K$ -trivial SNC model $X \to ( C , 0 )$ with smooth total space, and it is adapted to $R$ if $R _ { t } \ \subset \ X _ { t }$ for $t \in C \setminus { 0 }$ extends to $X _ { 0 }$ as a divisor not containing singular strata, and the limit of any component of positive genus is nef.

The answer to the last problem can be read off directly from the Coxeter diagrams of the reflection groups of the hyperbolic lattices $\overline { T }$ appearing at the $0$ -cusps of $F _ { S }$ . The reason for this is quite simple.
The main tool we use is the mirror symmetry between degenerations in the $S$ -family and nef line bundles on mirror K3 surfaces $\widehat { X }$ with Picard lattice ${ \widehat { S } } = { \overline { { T } } }$ . The nef cone of a K3 surface depends on, and is described by the reflection group of its Picard lattice.

The structure of the paper is as follows.
In Section 2 we recall the theory of K3 surfaces with a nonsymplectic involution, of 2-elementary lattices, and the general facts about the moduli spaces $F _ { S }$ of $\mathrm { K 3 }$ surfaces with group action.
We also recall basic facts about the combinatorial (Baily-Borel, toroidal, semitoroidal) and functorial (KSBA) compactifications of these moduli spaces.

In Section 3 we recall Vinberg’s theory of reflection groups in hyperbolic spaces and the Coxeter-Vinberg diagrams.
We don’t need the Coxeter groups for all the 75 of the 2-elementary lattices but only for those that appear at the 0-cusps of $F _ { S }$ for some $S$ . These are the lattices with $g \geq 1$ , excluding $( r , a , \delta ) = ( 1 4 , 6 , 0 )$ . For the lattices with $g \geq 2$ the Coxeter diagrams were computed by Nikulin in [AN06]. A few cases on the $g = 1$ line were previously known.
We complete the job for the remaining lattices, the answer is given in Figs.
3 and 4.

In Section 4 we describe K3 surfaces appearing in the 75 families, their quotients by the involution, and their nef cones.
The 75 families are woven together in a web by certain “Heegner divisor moves,” corresponding to when one moduli space $F _ { S ^ { \prime } }$ is a Heegner divisor in or at the boundary of $F _ { S }$ . We describe these moves and their properties.

In Section 5 we completely describe the 0- and 1-cusps of $F _ { S }$ together with the incidence relations between them.
In particular, the 0-cusps of $F _ { S }$ are described by three kinds of “mirror moves” on the nodes of Fig. 1, making it into a directed graph in which every vertex has in- and out-degrees equal to 0, $1$ , 2, or 3.

In Section 6 we discuss the theory of integral-affine spheres (IAS $^ 2$ ) in relation to Kulikov models.
It is well known that the dual graph $\Gamma ( X _ { 0 } )$ of a Type III Kulikov central fiber $X _ { 0 } = \cup V _ { i }$ is a triangulation of $S ^ { 2 }$ . In simple terms, the integral affine sphere $B = \Gamma ( X _ { 0 } )$ is an economical description for $X _ { 0 }$ . The singularities of the IAS $^ 2$ describe the nontoric components $V _ { i }$ . The same integral-affine structures describe a Lagrangian torus fibration $\mu \colon { \widehat { X } } \to B$ on a mirror K3 surface $\widehat { X }$ with a symplectic form, e.g. given by an ample line bundle.

In Section 7 we study this mirror correspondence specifically for K3 surfaces with a nonsymplectic involution.
To understand the K¨ahler geometry of $X$ , encoded by the divisor $R$ , we must understand the complex geometry of $\widehat { X }$ . The key is a special degeneration of $\widehat { X }$ into two copies ${ \widehat { X } } _ { 0 } = { \widehat { Y } } \cup { \widehat { Y } }$ of the surface $\widehat { Y } = \widehat { X } / \widehat { \iota }$ , the quotient of $\widehat { X }$ by the mirror involution.
This applies to all the cases except for the Enriques case, where the answer is even more interesting: $\hat { Y }$ is an Halphen pencil, and the gluing is by a 2-torsion twist on the multiple fiber.

The resulting IAS $^ 2$ is of a particularly simple kind: $B = P \cup P ^ { \mathrm { o p p } }$ , the union of two isomorphic “hemispheres”, Symington polytopes for $\widehat { Y }$ glued along a circular equator representing an anticanonical boundary of $\hat { Y }$ . We prove that the mirror correspondence exchanges the ( $\pm$ 1)-eigenspaces on the lattices $H ^ { 2 } ( X , \mathbb { Z } )$ , $H ^ { 2 } ( { \hat { X } } , \mathbb { Z } )$ modulo the vanishing cycle, resp.
the fiber class of the Lagrangian torus fibration.

In Section 8, for each lattice $T$ appearing at a $0$ -cusp of $F _ { S }$ , and each monodromy invariant $\lambda \in { \overline { { T } } }$ encoding the Picard-Lefschetz transform of a one-parameter degeneration, we construct explicitly the families of Kulikov surfaces with involution that appear, up to taking some multiple of $\lambda$ .

In Section 9 we first define the semifans appearing in Theorem 1.2. Next, we compute the stable models for the Kulikov surfaces of Section 8. Finally, we prove Theorem 1.2 by applying the general theory of [AE21] and [AEH21].

Acknowledgements.
The authors were partially supported by the NSF grants DMS-2201222 and DMS-2201221 respectively.

# 2. K3 surfaces with involution and 2-elementary lattices

2A. K3 surfaces with a nonsymplectic involution.
Let $X$ be a smooth projective complex K3 surface.
An involution $\iota$ of $X$ is called nonsymplectic if it acts as $\iota ^ { * } \omega _ { X } = - \omega _ { X }$ on a non-vanishing holomorphic two-form $\omega _ { X } \in H ^ { 2 , 0 } ( X )$ . It is well known that the quotient $Y = X / \iota$ is either a rational or Enriques surface and that $X$ is algebraic.

The main invariant of the involution is the (+1) eigenspace $S = H ^ { 2 } ( X , \mathbb { Z } ) ^ { + }$ , a hyperbolic lattice of some rank $r$ . Its orthogonal complement $T = S ^ { \perp } = H ^ { 2 } ( X , \mathbb { Z } ) ^ { - }$ in $H ^ { 2 } ( X , \mathbb { Z } )$ is a lattice of signature $( 2 , 2 0 - r )$ . There is a canonical isomorphism $A _ { S } = A _ { T }$ between the discriminant lattices $A _ { S } = S ^ { * } / S$ and $A _ { T } = T ^ { * } / T$ . The involution acts by multiplication by $\pm 1$ on $A _ { S }$ and $A _ { T }$ respectively.
This implies that $A _ { S } = \mathbb { Z } _ { 2 } ^ { a }$ for some $a \geq 0$ . Such lattices are called 2-elementary.

Conversely, if $S \subset L _ { \mathrm { K 3 } } = \mathrm { I I } _ { 3 , 1 9 } = U ^ { \oplus 3 } \oplus E _ { 8 } ^ { \oplus 2 }$ is a primitive 2-elementary lattice and $T = S ^ { \perp }$ then the involution $\rho$ of $L _ { \mathrm { K 3 } } \otimes \mathbb { Q }$ acting as $\pm 1$ on $S$ and $T = S ^ { \perp }$ respectively is an involution of $L _ { \mathrm { { K 3 } } }$ . If $X$ is a $\mathrm { K 3 }$ surface whose Picard lattice $S _ { X }$ equals $S$ via some marking $H ^ { 2 } ( X , \mathbb { Z } ) \to L _ { \mathrm { K 3 } }$ then by the Torelli theorem, there exists a unique involution $\iota$ of $X$ such that $\iota ^ { * } = \rho$ .

An indefinite even 2-elementary lattice is uniquely determined by its signature and the triple $( r , a , \delta ) = ( \mathrm { r k _ { \mathbb { Z } } } S , \mathrm { r k _ { \mathbb { Z } _ { 2 } } } A _ { S } , \delta )$ , where $\delta \in \{ 0 , 1 \}$ is an additional invariant explained in the next section.
The 2-elementary hyperbolic lattices admitting a primitive embedding into $L _ { \mathrm { { K 3 } } }$ were classified by Nikulin in [Nik79a, 3.6.2]. There are 75 lattices and for each of them, an embedding into $L _ { \mathrm { { K 3 } } }$ is unique up to ${ \cal O } ( L _ { \mathrm { K 3 } } )$ . The result is given in Fig.

![](images/b37234f61719d5c86b6151dd7b80110453fdecdad73e2f9e2fea6644ac4ba2d1.jpg)\
Figure 1. Hyperbolic 2-elementary K3 lattices $( r , a , \delta )$

The fixed locus $R = X ^ { \iota }$ of the involution and the quotient surface $Y = X / \iota$ are smooth.
Denote by $k + 1$ the number of the irreducible components of $R$ and by $g$ the sum of their genera (excluding the special Enriques case).
Then

$$
g = 1 1 - { \frac { 1 } { 2 } } ( r + a ) { \mathrm { ~ a n d ~ } } k = { \frac { 1 } { 2 } } ( r - a )
$$

and the triple $( g , k , \delta )$ is an alternative set of invariants of $S$ . There are three cases:

(1) $R$ is a union of a curve $C _ { 0 }$ of genus $g \geq 0$ and $k$ additional curves $C _ { 1 } , \ldots , C _ { k }$ each isomorphic to $\mathbb { P } ^ { 1 }$ . The surface $Y$ is rational.\
(2) ${ \cal R } = C _ { 0 } \sqcup C _ { 1 }$ is the union of two elliptic curves.
Then $( r , a , \delta ) = ( 1 0 , 8 , 0 )$ and $( g , k , \delta ) = ( 2 , 1 , 0 )$ . The surface $Y$ is rational elliptic.\
(3) $R = \emptyset$ . Then $( r , a , \delta ) = ( 1 0 , 1 0 , 0 )$ and $( g , k , \delta ) = ( 1 , 0 , 0 )$ . The surface $Y$ is Enriques.

Remark 2.1. The case $( 1 0 , 8 , 0 )$ in many ways is more similar to those on the $g = 1$ line than to those with $g \geq 2$ . For example, the automorphism group of a K3 surface with this Picard lattice is infinite.
Its Coxeter diagram, given in Fig. 3, is the same as for $( 1 0 , 1 0 , 1 )$ . See also Theorem 4.1.

In the next sections, we briefly recall the theory of 2-elementary lattices and two ways of constructing the moduli spaces of K3 surfaces with a nonsymplectic involution.

2B. 2-elementary lattices.
A lattice $H$ is a free finite rank $\mathbb { Z }$ -module together with a nondegenerate $\mathbb { Z }$ -valued bilinear form.
It is called even if $x ^ { 2 } \equiv 0$ (mod $2 \mathbb { Z }$ ) for all $x \in H$ and odd otherwise.
The discriminant lattice is $A _ { H } = H ^ { * } / H$ , where $H ^ { \ast } \subset H _ { \mathbb { Q } }$ is the dual lattice.
It comes with the discriminant form $q _ { H } \colon A _ { H } \to \mathbb { Q } / \mathbb { Z }$ , $q ( x ) = x ^ { 2 }$ . Moreover, if $H$ is even then $q _ { H }$ takes well-defined values in $\mathbb { Q } / 2 \mathbb { Z }$ . One also has the associated bilinear form $b _ { H } \colon A _ { H } \times A _ { H } \to \mathbb { Q } / \mathbb { Z }$ .

If $L$ is a unimodular lattice, $S \subset L$ a primitive (i.e. saturated) sublattice and $T = S ^ { \perp }$ then $( A _ { S } , q _ { S } ) = ( A _ { T } , - q _ { T } )$ in a canonical way.

2.2. If $S$ and $T$ are, respectively, the $( \pm 1 )$ -eigenspaces of an involution $\iota$ on $L$ then $\iota$ acts as identity on $A _ { S }$ and as $( - 1 )$ on $A _ { T }$ . Therefore, $A _ { S } \simeq \mathbb { Z } _ { 2 } ^ { a }$ for some $a$ . Lattices $H$ with $A _ { H } \simeq \mathbb { Z } _ { 2 } ^ { a }$ are called 2-elementary.
Thus, $S$ and $T$ are 2-elementary in this case.

Definition 2.3. We define an additional invariant, coparity $\delta _ { H }$ as follows: $\delta = 0$ if for all $x \in A _ { H }$ one has $q _ { H } ( x ) \equiv 0$ (mod $\mathbb { Z }$ ) and $\delta = 1$ otherwise.
We will call lattices with $\delta _ { H } = 0$ co-even and lattices with $\delta _ { H } = 1$ co-odd.

This notation is explained by the following.
Recall that for any lattice $K$ , $K ( n )$ denotes the lattice with the bilinear product scaled by $n$ , i.e. $( x , y ) _ { K ( n ) } = n { \cdot } ( x , y ) _ { K }$ .

Definition 2.4. For a 2-elementary (not necessarily even) lattice $H$ , the doubled dual is $H ^ { \dagger } = H ^ { \ast } ( 2 )$ . The assignment $H  H ^ { \dagger }$ is an involution since

$$
\begin{array} { r } { ( H ^ { \dagger } ) ^ { \dagger } = \left( H ^ { * } ( 2 ) \right) ^ { * } ( 2 ) = H ( \frac { 1 } { 2 } ) ( 2 ) = H . } \end{array}
$$

The doubled dual operation interchanges the parity and co-parity:

Lemma 2.5. Let $H$ be a 2-elementary lattice with invariants $( r , a , \delta )$ . Then $H ^ { \dagger }$ is $a$ 2-elementary lattice of the same signature with invariants $( r , r - a , \delta ^ { \dagger } )$ and the discriminant group is

$$
\begin{array} { r } { A _ { H ^ { \dagger } } = ( H ^ { \dagger } ) ^ { * } / H ^ { \dagger } = H ( \frac { 1 } { 2 } ) / H ^ { * } ( 2 ) . } \end{array}
$$

Moreover, $\delta = 0$ (resp.
$\delta = 1$ ) $i f H ^ { \dagger }$ is even (resp.
odd), and $H$ is even (resp.
odd) iff $\delta ^ { \dagger } = 0$ (resp.
$\delta ^ { \dagger } = 1$ ).

Proof.
For $x , y \in H ^ { * }$ one has $2 x \in H$ so $( x , y ) _ { H ^ { \prime } } = 2 ( x , y ) = ( 2 x , y ) \in \mathbb { Z }$ . So $H ^ { \dagger }$ is indeed a $\mathbb { Z }$ -lattice.
The equation for the discriminant group is immediate.
Since $H$ is 2-elementary, one has

$$
\begin{array} { r } { H \subset 2 H ^ { * } \subset \frac 1 2 H \implies 2 H ^ { \dag } = 2 H ^ { * } ( 2 ) \subset \frac 1 2 H ( 2 ) = H ( \frac 1 2 ) , } \end{array}
$$

so $H ^ { \dagger }$ is 2-elementary of the same rank $r$ , and the $\mathbb { Z } _ { 2 }$ -rank of the discriminant group is $2 r - ( r + a ) = r - a$ . For $x \in H ^ { * }$ one has $( x , x ) _ { H ^ { * } } = \textstyle { \frac { 1 } { 2 } } ( x , x ) _ { H ^ { \dagger } }$ , so $\delta _ { H } = 0$ iff $H ^ { \dagger }$ is even.
The last part holds by symmetry.
$\boxed { \begin{array} { r l } \end{array} }$

We recall the following facts about 2-elementary lattices proved in [Nik79a]. Any indefinite even 2-elementary lattice $H$ is uniquely defined by its signature $( n _ { + } , n _ { - } )$ and the invariants $( r , a , \delta )$ , where $r = n _ { + } + n _ { - }$ is its rank, $a = \operatorname { r k } _ { \mathbb { Z } _ { 2 } } A _ { H }$ is the $\mathbb { Z } _ { 2 }$ -rank of the discriminant lattice, and $\delta$ is the coparity.
Moreover, the homomorphism ${ \cal O } ( H ) \to { \cal O } ( q _ { H } )$ from the isometry group to the isometry group of $\left( A _ { H } , q _ { H } \right)$ is surjective.
For definite 2-elementary lattices, the genus of the lattice is uniquely defined but there may be several isomorphism classes, cf.
Section 5D.

Notation 2.6. Instead of writing “a lattice $H$ of signature $( n _ { + } , n _ { - } )$ with invariants $( r , a , \delta )$ ” we will simply write $H = ( r , a , \delta ) _ { n _ { + } }$ . Moreover, for hyperbolic lattices, which are the majority of lattices in this paper, we will frequently omit the subscript $n _ { + } = 1$ and write simply $( r , a , \delta )$ .

The discriminant forms of even lattices were classified in [Nik79a]. For the even 2-elementary lattices they are direct sums of $p : = q _ { 1 } ( 2 )$ , $q : = q _ { - 1 } ( 2 )$ , $u : = u ( 2 )$ and $v : = v ( 2 )$ , which are the discriminant forms of the lattices $\langle 2 \rangle$ , $\langle - 2 \rangle$ , $U ( 2 )$ , $V ( 2 )$ :

$$
( 2 ) , \quad ( - 2 ) , \quad { \binom { 0 } { 2 } } \ 0 \not { p } , \quad { \binom { 4 } { 2 } } \ 2 \not { p }
$$

considered as lattices over the 2-adic numbers.
Among them $u$ and $\boldsymbol { v }$ are co-even, and $p$ and $q$ are co-odd.
The values of $q$ in $\mathbb { Q } / 2 \mathbb { Z }$ , on $\mathbb { Z } _ { 2 } e ^ { * }$ and $\mathbb { Z } _ { 2 } e ^ { * } \oplus \mathbb { Z } _ { 2 } f ^ { * }$ , are

$$
\begin{array} { l l l } { { p ( e ^ { * } ) = \frac { 1 } { 2 } , } } & { { } } & { { q ( e ^ { * } ) = - \frac { 1 } { 2 } , } } \\ { { u ( e ^ { * } ) = u ( f ^ { * } ) = 0 , u ( e ^ { * } + f ^ { * } ) = 1 \quad } } & { { } } & { { v ( e ^ { * } ) = v ( f ^ { * } ) = v ( e ^ { * } + f ^ { * } ) = 1 . } } \end{array}
$$

We write the discriminant form for a direct sum of lattices multiplicatively.
The relations between the generators $p , q , u , v$ are generated by the identities

$$
u ^ { 2 } = v ^ { 2 } , \quad p ^ { 4 } = q ^ { 4 } , \quad u p = ( p q ) p , \quad u q = ( p q ) q , \quad v p = q ^ { 3 } , \quad v q = p ^ { 3 } .
$$

The signature of a discriminant form is well defined mod 8. For $p$ , $q$ , $u$ , $\boldsymbol { v }$ it is 1, $^ { - 1 }$ , $0$ , 4 respectively.
This makes it easy to compute the discriminant forms for all the cases.
We show some of them in Fig. 1, enough to see the pattern.

All of the lattices in Fig. 1 can be written as direct sums of the negative definite lattices $A _ { 1 }$ , $D _ { 4 }$ , $D _ { 6 }$ , $D _ { 8 }$ , $E _ { 7 }$ , $E _ { 8 }$ , $E _ { 8 } ( 2 )$ , and hyperbolic lattices $\langle 2 \rangle$ , $U = \mathrm { { I I } _ { 1 , 1 } }$ , $U ( 2 )$ . Their discriminant forms are as follows.
For the co-even ones $q ( U ) = q ( E _ { 8 } ) = 1$ , $q ( U ( 2 ) ) = q ( D _ { 8 } ) = u$ , $q ( D _ { 4 } ) = v$ , $q ( E _ { 8 } ( 2 ) ) = u ^ { 4 }$ ; for the co-odd ones $q ( A _ { 1 } ) = q$ , $q ( E _ { 7 } ) = q ( \langle 2 \rangle ) = p$ , $q ( D _ { 6 } ) = p ^ { 2 }$ .

2C. Moduli of $\mathbf { K 3 }$ surfaces with an involution.
The K3 surfaces with a nonsymplectic involution corresponding to a given 2-elementary lattice $S$ come with a natural moduli space.
One way to approach it is using the moduli of $S$ -polarized K3 surfaces following [Dol96], as in [DK07]. The construction is a little delicate.
Another, more direct approach applies to K3 surfaces with any finite automorphism group that is not totally symplectic, see [AEH21, Sec. 2A].

Fix an involution $\rho$ of $L _ { \mathrm { { K 3 } } }$ with the $( \pm 1 )$ eigenspaces $S$ and $T$ . A $\rho$ -marking of a K3 surface with an involution $\iota$ is an isometry $\phi \colon H ^ { \cdot 2 } ( X , \mathbb { Z } ) \to L _ { \mathrm { K 3 } }$ such that $\iota ^ { * } = \phi ^ { - 1 } \circ \rho \circ \phi$ . Let $\mathbb { D } _ { S } : = \mathbb { P } \{ x \in T \otimes \mathbb { C } \mid x \cdot x = 0 , \ x \cdot { \bar { x } } > 0 \}$ be the period domain.
Then $\rho$ -marked K3 surfaces with involution have a period $\phi ( \mathbb { C } \omega _ { X } ) \in \mathbb { D } _ { S }$ .

One defines the discriminant locus $\Delta = ( \cup _ { \delta } \delta ^ { \bot } ) \cap \mathbb { D } _ { S }$ , with $\delta$ ranging over the $\left( - 2 \right)$ -vectors in $S$ . The $\rho$ -markings of a K3 surface with involution are a torsor over

$$
\Gamma _ { \rho } : = \{ \gamma \in O ( L _ { \mathrm { K 3 } } ) \mid \gamma \circ \rho = \rho \circ \gamma \} .
$$

Then $F _ { S } = ( \mathbb { D } _ { S } \setminus \Delta ) / \Gamma _ { \rho }$ is the coarse space of K3 surfaces that admit a $\rho$ -marking

Recall that for the 2-elementary indefinite lattices $S$ and $T$ the homomorphisms ${ \cal O } ( S )  { \cal O } ( A _ { S } , q _ { S } )$ and ${ \cal O } ( T )  { \cal O } ( A _ { T } , q _ { T } )$ are surjective and one of course has $O ( A _ { S } , q _ { S } ) = O ( A _ { T } , q _ { T } )$ . Thus, $\mathbb { D } _ { S } / \Gamma _ { \rho } = \mathbb { D } _ { S } / O ( T )$ is the quotient by the full group of isometries of $T$ , and $F _ { S }$ is the complement of finitely many divisors in it.

Note that for the surfaces parameterized by $F _ { S }$ the Picard lattice $S _ { X }$ could be bigger than $S$ but the (+1)-eigenspace $S _ { X } ^ { + }$ can be identified with $S$ .

2D. Baily-Borel, toroidal, and semitoroidal compactifications.
This material is well known, so we refer to [AMRT75, Loo03] for details.
Let $\mathbb { D } = \mathbb { D } _ { S }$ as above, and let $\Gamma \subset O ( T )$ be a finite index subgroup.
The Baily-Borel compactification

$$
\mathbb { D } / \Gamma \hookrightarrow \overline { { \mathbb { D } / \Gamma } } ^ { \mathrm { B B } }
$$

is a projective variety whose boundary consists of finitely many points (0-cusps) and modular curves (1-cusps).
The “Type III” 0-cusps (resp.
“Type II” 1-cusps) are in a bijection with $\Gamma$ -orbits of primitive isotropic lines $I \subset T$ (resp.
primitive isotropic planes $J \subset T$ ). The “Type” terminology arises from the Kulikov-Persson-Pinkham classification of K3 degenerations [Kul77, PP81].

A toroidal compactification $\overline { { \mathbb { D } / \Gamma } } ^ { \mathfrak { F } }$ is a combinatorially defined normal variety specified by the data $\Im \mathrm { ~ = ~ } \{ \Im I \}$ of a compatible system of admissible fans for each cusp.
For a Type IV domain, the data for the 1-cusps is trivial, so the only important fans are for the 0-cusps and they are always compatible.
The fan $\mathfrak { F } _ { I }$ is a rational polyhedral decomposition of the rational closure $\overline { { \mathcal { C } } } _ { I , \mathbb { Q } }$ of the positive cone $\mathcal { C } _ { I } \subset I ^ { \perp } / I \otimes \mathbb { R }$ . It is required to satisfy the usual fan axioms, and additionally be $\Gamma$ -invariant with only finitely many orbits of cones.

A semitoroidal (or semitoric) compactification $\overline { { \mathbb { D } / \Gamma } } ^ { \mathfrak { F } }$ of Looijenga is a generalization in which the cones of $\mathfrak { F } _ { I }$ are locally polyhedral, but not necessarily finitely generated.
The data for the 1-cusps and the compatibility condition may be nontrivial.
By [AE21, Thm. 5.14], a semitoroidal compactification is the same as a normal compactification which may be sandwiched between the Baily-Borel and a toroidal compactification.

2E. Stable pair compactifications.
We refer the reader to [Kol23] for the definition of slc singularities and the existence of the KSBA compactifications of moduli spaces via KSBA stable pairs.

In the case at hand, a stable pair $( X , \epsilon R )$ consists of a seminormal surface $X$ with only slc singularities (in particular, double normal crossing in codimension 1) with a trivial dualizing sheaf and an ample Cartier divisor $R$ which does not contain any log canonical centers of $X$ . For $0 < \epsilon \ll 1$ this pair is a KSBA stable pair, for all small enough $\epsilon$ bounded in terms $R ^ { 2 }$ . For fixed $R ^ { 2 }$ there exists a projective moduli space for such pairs.
For full details, see [AET19] and [ABE22].

When $g \geq 2$ , we denote by $\overline { { F } } _ { S }$ the closure of the pairs $F _ { S } = \{ ( \overline { { X } } , \epsilon \overline { { C } } _ { g } ) \}$ in the space of KSBA stable pairs.
One of the main goals of this paper is to prove that

$$
( \overline { { F } } _ { S } ) ^ { \nu } = \overline { { F } } _ { S } ^ { \mathfrak { F } }
$$

for a particular semitoroidal compactification for an explicit semifan $\mathfrak { F } = \{ \mathfrak { F } _ { I } \}$ Here $\nu$ denotes the normalization.

# 3. Reflection groups

One of the main tools in the study of K3 surfaces is reflection groups.
In this paper we apply it in two ways: to determine the nef cones in Section 4D and to describe certain toroidal compactifications of Section 2D.

3A. Vinberg’s theory.
We refer to [Vin75, Vin72] for Vinberg’s theory of reflection groups of hyperbolic lattices.
We briefly describe it below.

Let $H$ be a hyperbolic lattice.
Let $\boldsymbol { \mathscr { C } }$ the component of the set $\{ v \in H _ { \mathbb { R } } \mid v ^ { 2 } > 0 \}$ , containing a fixed class $h$ with ${ h ^ { 2 } > 0 }$ . Let $\mathcal { H } = \mathbb { P } \mathcal { C }$ be the corresponding hyperbolic space.
A vector $v \neq 0$ with $v ^ { 2 } = 0$ in the closure of $\boldsymbol { \mathscr { C } }$ is a point on the sphere at infinity of $\mathcal { H }$ .

There are two kinds of closures of $\boldsymbol { \mathscr { C } }$ , and it is always clear from the context which one we have in mind.
When $H = \operatorname { P i c } X$ for some surface $X$ , the nef cone $\operatorname { N e f } ( X )$ is naturally a subset of the round cone $\mathcal { C } = \{ v \in H _ { \mathbb { R } } \ | \ v ^ { 2 } \geq 0 \}$ , so here we add all infinite points of $\mathcal { H }$ . When $c$ is used to define a (semi)fan $\tilde { s }$ for some (semi)toroidal compactification, one considers the rational closure $\overline { { \mathcal { C } } } _ { \mathbb { Q } }$ instead, with only the rays $\mathbb { R } _ { \geq 0 } v$ spanned by rational vectors $\boldsymbol { v }$ added.

A reflection in a root $\alpha \in H$ is the isometry $\begin{array} { r } { w _ { \alpha } ( v ) = v - \frac { 2 ( \alpha , v ) } { ( \alpha , \alpha ) } \alpha } \end{array}$ . One must have $2 \mathrm { d i v } ( \alpha ) \in ( \alpha , \alpha ) \mathbb { Z }$ for it to be well defined.
Let $W \subset O ( H )$ be a group generated by some subset of reflections.
The most interesting cases are the groups

(1) $W _ { \mathrm { r } }$ generated by all reflections, and (2) $W _ { 2 }$ generated by the $\left( - 2 \right)$ -reflections, in roots with $\alpha ^ { 2 } = - 2$ .

Definition 3.1. We denote by $\mathfrak { C }$ the fundamental chamber for $W$ . Equivalently, one can treat it as the (possibly infinite) polyhedron $\| ^ { \mathrm { p } } \mathfrak { C } \subset \mathcal { H }$ . One has

${ \mathfrak { C } } = \{ v \in { \overline { { \mathcal { C } } } }$ o $\cdot { \overline { { \mathcal { C } } } } _ { \mathbb { Q } } \mid ( \alpha _ { i } , v ) \geq 0 { \mathrm { ~ f o r ~ s i m p l e ~ r o o t s ~ } } \alpha _ { i } { \big \} } , \quad O ( H ) = W \ltimes \operatorname { S y m } ( \mathfrak { C } ) .$

The fundamental chamber is encoded in a Coxeter-Vinberg diagram $\Gamma$ . The vertices correspond to the simple roots $\alpha _ { i }$ and the edges show the angles between them as follows.
Let $g _ { i j } = ( \alpha _ { i } , \alpha _ { j } ) / \surd ( \alpha _ { i } , \alpha _ { i } ) ( \alpha _ { j } , \alpha _ { j } )$ . One connects $i$ and $j$ by

• an $m$ -tuple line if $\begin{array} { r } { g _ { i j } = \cos \frac { \pi } { m + 2 } } \end{array}$ . The hyperplanes $\alpha _ { i } ^ { \perp }$ , $\alpha _ { j } ^ { \perp }$ intersect in $\mathcal { H }$ .\
• a thick line if $g _ { i j } = 1$ . $\alpha _ { i } ^ { \perp }$ , $\alpha _ { j } ^ { \perp }$ are parallel, meet at an infinite point of $\mathcal { H }$ .\
• a dotted line if $g _ { i j } > 1$ . $\alpha _ { i } ^ { \perp }$ , $\alpha _ { j } ^ { \perp }$ do not meet in $\mathcal { H }$ or its closure.

We identify a subset $V ^ { \prime } \subset V ( \Gamma )$ of vertices of $\Gamma$ with the induced subgraph $\Gamma ^ { \prime }$ . The faces of $\mathfrak { C }$ are of the form

$$
F = \cap _ { i \in \Gamma ^ { \prime } } \alpha _ { i } ^ { \perp } \cap \mathfrak { C }
$$

for the $\Gamma ^ { \prime }$ which are elliptic or parabolic, i.e. corresponding to a negative definite or negative semi-definite matrix.
This correspondence is bijective for elliptic subdiagrams.
But disjoint parabolic subdiagrams define the same ray of $\mathfrak { C }$ .

The subgroup $W \subset O ( H )$ has finite index iff the polyhedron $\mathbb { P } \mathbb { C }$ has finite volume.
One says $W$ has finite covolume.
In that case, rational vectors at infinity correspond to maximal parabolic subdiagrams, of rank $\dim H - 1$ . Otherwise, there may exist some $\boldsymbol { v }$ for which the maximal parabolic subdiagram has lower rank; for example it could be empty.

In a 2-elementary even hyperbolic lattice, the roots are the $\left( - 2 \right)$ -vectors and the $( - 4 )$ -vectors of divisibility 2. In the Coxeter diagram we denote the $\left( - 2 \right)$ -vectors by transparent, white vertices and the $( - 4 )$ -vectors by filled, black vertices.
In addition, when the hyperbolic lattice is interpreted as the Picard lattice $S$ of a $\mathrm { K 3 }$ surface with an involution, and the white vertices as $\left( - 2 \right)$ -curves on it, the doublecircled vertices denote the $\left( - 2 \right)$ -curves which are fixed pointwise by the involution.
See Fig. 3 for some examples.

For a K3 surface $X$ with $H \ = \ \operatorname { P i c } X$ , its nef cone $\operatorname { N e f } ( X )$ is identified with $\mathfrak { C } _ { 2 } ~ \subset ~ \overline { { \mathcal { C } } }$ , described by the Coxeter diagram $\Gamma _ { 2 }$ . This is the main object of our interest because it appears in the Mirror Theorem 6.19.

But in the most important case, when $H = S$ is a 2-elementary lattice lying on the $g = 1$ line, the group $W _ { 2 } \subset O ( S )$ has infinite index, unless $\boldsymbol { S } = ( 1 9 , 1 , 1 )$ . Indeed, this is equivalent to $| \operatorname { A u t } X | = \infty$ , which holds by [Nik79b]. The Coxeter diagram $\Gamma _ { 2 }$ in these cases is infinite.
Working with the smaller, usually finite, diagram $\Gamma _ { r }$ instead is much more convenient.

For the 50 lattices $S \neq ( 1 0 , 8 , 0 )$ with $g \geq 2$ , $\operatorname { A u t } X$ is finite, and $W _ { 2 }$ has finite covolume, see Section 3C below.
But usually $\Gamma _ { 2 }$ is enormous and $\Gamma _ { \mathrm { r } }$ is relatively small.
In Section 3D we compute Coxeter diagrams for the lattices $S$ on the $g = 1$ line and prove that for most of them $W _ { \mathrm { r } }$ has finite covolume and $\Gamma _ { \mathrm { r } }$ is finite.

In fact, there are many intermediate reflection groups between $W _ { 2 }$ and $W _ { \mathrm { r } }$ :

Definition 3.2. Let $V ( \Gamma _ { \mathrm { r } } ) = V _ { 2 } \sqcup V _ { 4 }$ be the decomposition of the vertices of $\Gamma _ { \mathrm { r } }$ into the $\left( - 2 \right)$ -roots (white) and the $( - 4 )$ -roots (black).
Consider a subset $\mathbb { B } \subset V _ { 4 }$ and let $\mathbb { B } ^ { c }$ be the complement in $V ( \Gamma _ { \mathrm { r } } )$ , which therefore includes all of $V _ { 2 }$ . We define two reflection subgroups of $W _ { \mathrm { r } }$ :

$$
W ( \mathbb { B } ) = \langle w _ { \alpha } \mid \alpha \in \mathbb { B } \rangle \qquad W _ { \mathrm { n o r } } ( \mathbb { B } ^ { c } ) = \langle w _ { g ( \alpha ) } \mid g \in W _ { \mathbf { r } } , \ \alpha \in \mathbb { B } ^ { c } \rangle
$$

The latter is the minimal normal subgroup of $W _ { \mathrm { r } }$ generated by $W ( { \mathbb { B } } ^ { c } )$ . Let ${ \mathfrak { C } } _ { W _ { \mathrm { n o r } } \left( \mathbb { B } ^ { c } \right) }$ be the fundamental chamber for the action of $W _ { \mathrm { n o r } } ( \mathbb { B } ^ { c } )$ on $\mathcal { C }$ .

Two special cases are: $W ( \emptyset ) = W _ { \mathrm { r } }$ and $W ( V _ { 4 } ) = W _ { 2 }$ .

Lemma 3.3. One has $W _ { \mathrm { r } } = W ( { \mathbb { B } } ) \ltimes W _ { \mathrm { n o r } } ( { \mathbb { B } } ^ { c } )$ .

Proof.
This follows by Proposition on p.2 of [Vin83], which applies because roots in $V _ { 4 }$ have divisibility 2. See also [AN06, Prop. 2.4.1] for the case $\mathbb { B } = V _ { 4 }$ . $\boxed { \begin{array} { r l } \end{array} }$

Corollary 3.4. $W ( { \mathbb { B } } )$ acts on ${ \mathfrak { C } } _ { W _ { \mathrm { n o r } } \left( \mathbb { B } ^ { c } \right) }$ with the fundamental chamber $\mathfrak { C } _ { \mathrm { r } }$ . In particular, $W ( V _ { 4 } )$ acts on $\mathfrak { C } _ { 2 }$ with the fundamental chamber $\mathfrak { C } _ { \mathrm { r } }$ .

Any $\lambda \ \in \ \mathfrak { C } _ { \mathrm { r } }$ is also a vector in ${ \mathfrak { C } } _ { 2 }$ , so any elliptic subdiagram of $\Gamma _ { \mathrm { r } }$ can be translated into an elliptic subdiagram of $\Gamma _ { 2 }$ . We note the following useful conversion rules, see Fig. 2.

$$
B _ { n } ( 2 )  A _ { 1 } ^ { n } \quad C _ { 3 }  A _ { 3 } \quad C _ { n }  D _ { n } \quad F _ { 4 }  D _ { 4 }
$$

The reverse direction is possible up to “irrelevant” walls formed by connected diagrams consisting entirely of the $( - 4 )$ -roots.

![](images/2d2e7c97fc4c0ad1b40f1453f247cc06a597e491a84a67762d123a705f1e9b26.jpg)\
Figure 2. Conversion: $B _ { n } ( 2 ) \to A _ { 1 } ^ { n }$ $n = 2 , 3$ ), $C _ { 3 }  A _ { 3 }$ , $F _ { 4 } \to D _ { 4 }$

3B. Coxeter, or reflection semifan.
With the above notations:

Definition 3.5. A Coxeter, or reflection semifan $\mathfrak { F }$ is a semifan with support on ${ \overline { { \mathcal { C } } } } _ { \mathbb { Q } }$ with the following cones: the fundamental chamber $\mathfrak { C }$ , its faces, and their $W$ - translates.
It is a fan iff $W$ has finite covolume.

In particular, we have the semifan ${ \mathfrak { F } } _ { 2 }$ for the Weyl group $W _ { 2 }$ and its refinement, the semifan ${ \mathfrak { F } } _ { \mathrm { r } }$ for the full reflection group $W _ { \mathrm { r } }$ .

For a semitoroidal compactification defined by $\tilde { \vartheta }$ , the Type III cones correspond to elliptic subdiagrams of the Coxeter diagram.
If $\tilde { s }$ is a fan then the Type II cones are the rays on the boundary, corresponding to maximal parabolic subdiagrams of rank $\dim H - 1$ .

3C. Coxeter diagrams for lattices with $g \geq 2$ , excluding $( 1 0 , 8 , 0 )$ . For 50 of the 75 Picard lattices of Fig. 1, namely those with $g \geq 2$ excluding $( 1 0 , 8 , 0 )$ , the Coxeter diagrams $\Gamma _ { \mathrm { r } }$ were computed by Nikulin in [AN06, Table 1]. We recomputed and confirmed them for this paper.

These are exactly the cases when the fixed locus $R$ of the involution contains a curve of genus $g \geq 2$ . Another interpretation is that these are the 2-elementary Picard lattices $S _ { X }$ for which a K3 surface has finite automorphism group, excluding the lattice $( 1 9 , 1 , 1 )$ with $g = 1$ for which the automorphism group is also finite.

3D. Coxeter diagrams for lattices with $g = 1$ and for $( 1 0 , 8 , 0 )$ . These are the 2-elementary lattices corresponding to K3 surfaces with an elliptic pencil that is preserved by an infinite automorphism group $\operatorname { A u t } X$ , see Section 4B. For several of them the Coxeter diagrams are known, e.g. $( 1 0 , 1 0 , 0 )$ in [Vin75], $( 1 8 , 2 , 0 )$ in [VK78], $( 1 9 , 1 , 1 )$ in [Kon89]. We complete the computation in the remaining cases.

Theorem 3.6. $W _ { \mathrm { r } }$ has finite covolume for all the lattices on the $g = 1$ line except for $( 1 8 , 2 , 1 )$ and $( 1 7 , 3 , 1 )$ . The finite Coxeter diagrams are as given in Figures 3, 4. For $( 1 8 , 2 , 1 )$ and $( 1 7 , 3 , 1 )$ , the Coxeter diagrams are infinite and are described in Section $\cdot$ .

Note that in the lattice $( 1 0 , 8 , 0 )$ the roots generate the index 2 sublattice equal $( 1 0 , 1 0 , 1 )$ , so the two lattices have the same Coxeter diagrams.
In all other cases, the roots generate the full lattice.

Proof.
The proof is a direct computation using Vinberg’s algorithm [Vin72, Vin75] which is computationally involved but straightforward.
In all the cases except for $( 1 8 , 2 , 1 )$ and $( 1 7 , 3 , 1 )$ the algorithm satisfies Vinberg’s stopping condition after finitely many steps.

In the $( 1 8 , 2 , 1 )$ case, there are no $( - 4 )$ -vectors of divisibility 2, so $W _ { \mathrm { r } } = W _ { 2 }$ . By [Nik79b, Nik81] a K3 surface with this Picard lattice $S _ { X }$ has an infinite automorphism group.
By the Torelli theorem, this is equivalent to $W _ { 2 } ( S _ { X } ) \subset O ( S _ { X } )$ being of infinite index.
Another proof, which also works for $( 1 7 , 3 , 1 )$ is that in both cases there exists a negative definite lattice $K$ such that $S \simeq U \oplus K$ and the root sublattice $R \subset K$ is of infinite index.
These are the lattices $A _ { 1 5 } * *$ and $A _ { 1 3 } A _ { 1 } ( 2 ) * *$ respectively of Theorem 5.11. As explained in Section 3B, if $W _ { \mathrm { r } } \subset O ( S )$ is of finite index then the rays on the boundary of $\mathcal { H }$ , giving the 1-cusps, correspond to maximal parabolic subdiagrams and their root sublattices have finite index.


Remark 3.7. The $( 1 2 , 8 , 1 )$ diagram contains the subdiagram ${ \widetilde { B } } _ { 3 }$ which generates the same lattice as ${ \widetilde { A } } _ { 3 }$ . As in Lemma 3.3, let $\mathbb { B }$ consist of the isolated $( - 4 )$ -vector, so that $W ( \mathbb { B } ) = S _ { 2 }$ . Reflecting the attached $\left( - 2 \right)$ -vectors gives two other $( - 2 ) \AA$ -vectors.
One of them forms the ${ \tilde { A } } _ { 3 }$ diagram with the others.
This gives the Coxeter diagram for an index 2 reflection subgroup $W ^ { \prime } \subset W _ { \mathrm { { r } } }$ , also shown in Fig. 3. The righthand diagram is of greater relevance for later constructions.

The diagrams for $( 1 5 , 5 , 1 )$ and $( 1 6 , 4 , 1 )$ are quite large so drawn in two parts.

Remark 3.8. The overarching reason for the two exceptional cases is that the lattices on the $g = 1$ line are mirrors of the double covers of del Pezzo surfaces.
The del Pezzo surfaces of Picard rank $n + 1$ correspond to the $E _ { n }$ lattices.
For $n \geq 3$ they are root lattices: $A _ { 2 } A _ { 1 }$ , $A _ { 4 }$ , $D _ { 5 }$ , $E _ { 6 }$ , $E _ { 7 }$ , $E _ { 8 }$ . But the $E _ { 2 }$ lattice of degree 7 is not a root lattice, its root sublattice has corank 1. And for $n = 1$ there are two types $E _ { 1 }$ , $E _ { 1 } ^ { \prime }$ corresponding to $\mathbb { F } _ { 1 }$ and $\mathbb { F } _ { 0 }$ . The lattice $E _ { 1 } ^ { \prime }$ corresponding to $\mathbb { F } _ { 0 }$ has a finite index root sublattice $A _ { 1 }$ . But the lattice $E _ { 1 }$ corresponding to $\mathbb { F } _ { 1 }$ has an empty root lattice.
See more about these in [ABE22].

![](images/149f7ab8432b7235ff89eb2bbd8f71221c36ab983d77b2142f91abc48aefb6ce.jpg)\
Figure 3. Coxeter diagrams for lattices on the $g = 1$ line, part 1

![](images/8893de4c2e52078bd50d181d80f733ad6e630bd2b930da1fb86e498b03724f81.jpg)\
Figure 4. Coxeter diagrams for lattices on the $g = 1$ line, part 2

3E. Coxeter diagrams for $( 1 8 , 2 , 1 )$ and $( 1 7 , 3 , 1 )$ . Here we treat the two exceptional cases which do not have finite covolume.
The following is the result of applying Vinberg’s algorithm.

$( 1 8 , 2 , 1 )$ . There are no $( - 4 )$ -vectors of divisibility 2 in this lattice $S$ , and since the automorphism group of a K3 surface with this Picard lattice is infinite, there are infinitely many $\left( - 2 \right)$ -vectors, so the Coxeter diagram is infinite.
Rather than attempting to draw it, we describe it in words.

There is a wheel $\stackrel { \sim } { A } _ { 1 5 }$ of 16 $\left( - 2 \right)$ -curves forming a singular fiber of an elliptic fibration.
In addition to them there are 8 sections $a _ { 0 } , a _ { 2 } , \dotsc , a _ { 1 4 }$ attached to $e _ { 0 } , e _ { 2 } , \dots u _ { 1 4 }$ singly, i.e. with $( a _ { i } , e _ { j } ) = \delta _ { i j }$ ; and bisections $b _ { 1 } , b _ { 3 } , \dotsc , b _ { 1 5 }$ with $( b _ { i } , e _ { j } ) = 2 \delta _ { i j }$ . The bisections have divisibility 2.

Let $\bar { A } _ { 1 5 } ^ { \perp } = \langle c , v \rangle$ with $c$ the class of the fiber.
The Eichler transformation $E =$ $E _ { c , v }$ [Sca87, 3.7] is an isometry $S$ which fixes the vertices of $\tilde { A } _ { 1 5 }$ . The orbits $a _ { i } ^ { n } : = E ^ { n } ( a _ { i } )$ and $b _ { i } ^ { n } : = E ^ { n } ( b _ { i } )$ are the remaining $\left( - 2 \right)$ -vectors.
Each orbit is isomorphic to $\mathbb { Z }$ .

For the typical representatives $a _ { 0 } = a _ { 0 } ^ { 0 }$ and $b _ { 1 } = b _ { 1 } ^ { 0 }$ we list the vectors with intersections $0 , 2$ . All the other $a _ { i } ^ { n }$ and $b _ { i } ^ { n }$ have intersections $> 2$ and give dashed edges in the Coxeter diagram.

For $a _ { 0 }$ the $( - 2 )$ -vectors outside of the $\tilde { A } _ { 1 5 }$ cycle with intersections $0 , 2$ are:

(0) $a _ { 2 } ^ { 0 }$ , $a _ { 4 } ^ { 1 }$ , $a _ { 6 } ^ { 1 }$ , $a _ { 1 0 } ^ { 2 }$ , $a _ { 1 2 } ^ { 2 }$ , $a _ { 1 4 } ^ { 3 }$ and $b _ { 1 } ^ { 0 }$ , $b _ { 3 } ^ { 0 }$ , $b _ { 1 3 } ^ { 2 }$ , $b _ { 1 5 } ^ { 2 }$ .\
(2) $a _ { 2 } ^ { 1 }$ , $a _ { 8 } ^ { 1 }$ , $a _ { 8 } ^ { 2 }$ , $a _ { 1 4 } ^ { 2 }$ and $b _ { 7 } ^ { 1 }$ , $b _ { 9 } ^ { 1 }$ .

For $b _ { 1 }$ the $\left( - 2 \right)$ -vectors outside of the $\tilde { A } _ { 1 5 }$ cycle with intersections $0 , 2$ are:

(0) $a _ { 0 } ^ { 0 }$ , $a _ { 2 } ^ { 1 }$ , $a _ { 4 } ^ { 1 }$ , $a _ { 1 4 } ^ { 3 }$ (2) $a _ { 8 } ^ { 2 }$ , $a _ { 1 0 } ^ { 2 }$ .

The other intersection numbers are recovered by the fact that $E$ is an isometry, indices stay in the cyclic symmetry $\{ 0 , \ldots 1 5 \}$ $( u _ { i } , v _ { j } ) \ : = \ : ( u _ { i - k } , v _ { j - k } )$ − − ∈ { }. Going around the circle the shift is $( u , v \in \{ a , b \} )$ for as long as all the $u _ { i + 1 6 } ^ { n } = u _ { i } ^ { n - 3 }$ . For example,

$$
\begin{array} { r l } & { ( b _ { 1 5 } , a _ { 6 } ^ { - 1 } ) = ( b _ { 9 } , a _ { 0 } ^ { - 1 } ) = ( b _ { 9 } ^ { 1 } , a _ { 0 } ^ { 0 } ) = 2 , } \\ & { ( a _ { 1 4 } ^ { 3 } , a _ { 2 } ^ { 1 } ) = ( a _ { 1 2 } ^ { 3 } , a _ { 0 } ^ { 1 } ) = ( a _ { 1 2 } ^ { 2 } , a _ { 0 } ^ { 0 } ) = 0 , } \\ & { ( b _ { 1 5 } , a _ { 1 6 } ^ { 1 } ) = ( b _ { 1 5 } , a _ { 0 } ^ { - 2 } ) = ( b _ { 1 5 } ^ { 2 } , a _ { 0 } ^ { 0 } ) = 0 . } \end{array}
$$

Example 3.9. $b _ { 1 }$ is a $\left( - 2 \right)$ -vector of divisibility 2 which does not lie on the $\tilde { A } _ { 1 5 }$ - cycle.
The vectors which have intersection 0 with $b _ { 1 }$ are $e _ { i }$ for $i \neq 1$ and $a _ { 1 4 } ^ { 3 }$ , $a _ { 0 } ^ { 0 }$ , $a _ { 2 } ^ { 1 }$ , $a _ { 4 } ^ { 1 }$ . The last four vectors are mutually orthogonal with the exception of $( a _ { 0 } ^ { 0 } , a _ { 2 } ^ { 1 } ) = 2$ . We conclude that these $1 5 + 4$ vectors form the Coxeter diagram for the lattice $( 1 7 , 1 , 1 )$ that was given in [AN06, Table 1]. This agrees with Lemma 4.15.

$\underline { { ( 1 7 , 3 , 1 ) } }$ . Both the diagrams for the full reflection group $W _ { \mathrm { r } }$ and the reflection group $W _ { 2 }$ in $\left( - 2 \right)$ -vectors are infinite.
We compute the latter one.

There is a wheel $\tilde { A } _ { 1 3 }$ of 14 $\left( - 2 \right)$ -curves forming a singular fiber of an elliptic fibration.
In addition to them there are 7 sections $a _ { 0 } , a _ { 2 } , \ldots , a _ { 1 2 }$ attached to $e _ { 0 } , e _ { 2 } , \ldots a _ { 1 2 }$ singly, i.e. with $( a _ { i } , e _ { j } ) = \delta _ { i j }$ ; and bisections $b _ { 1 } , b _ { 3 } , \dots , b _ { 1 3 }$ with $( b _ { i } , e _ { j } ) = 2 \delta _ { i j }$ . The bisections have divisibility 2.

Let $\tilde { A } _ { 1 3 } ^ { \perp } = \langle c , v _ { 1 } , v _ { 2 } \rangle$ with $c$ the class of the fiber.
For $v \in \ \widetilde { A } _ { 1 3 } ^ { \perp }$ the Eichler transformation $v _ { 1 } , v _ { 2 }$ so that their intersection form is is an isometry $\left( \begin{array} { c c } { { - 4 } } & { { 2 } } \\ { { 2 } } & { { - 8 } } \end{array} \right) .$ $S$ which fixes the vertices of The orbits $\tilde { A } _ { 1 5 }$ . We pick

$$
a _ { i } ^ { n _ { 1 } , n _ { 2 } } : = E _ { c , n _ { 1 } v _ { 1 } + n _ { 2 } v _ { 2 } } ( a _ { i } ) , \quad b _ { i } ^ { n _ { 1 } , n _ { 2 } } : = E _ { c , n _ { 1 } v _ { 1 } + n _ { 2 } v _ { 2 } } ( b _ { i } )
$$

are the remaining $\left( - 2 \right)$ -vectors.
Each orbit is isomorphic to $\mathbb { Z } ^ { 2 }$ . Note that $E _ { c , n _ { 1 } v _ { 1 } }$ is contained in the Weyl group $W ( \tilde { A } _ { 1 } )$ generated by the reflections in the $( - 4 )$ -vectors $v _ { 1 }$ and $c - v _ { 1 }$ .

For the typical representatives a0 = a0 0, 0 and b1 = b0,01 we list the vectors with intersections $0 , 2$ . All the other $a _ { i } ^ { \scriptscriptstyle { n + 1 } , \scriptscriptstyle { n + 2 } }$ and $b _ { i } ^ { n 1 , n 2 }$ have intersections $> 2$ and give dashed edges in the Coxeter diagram.

For $a _ { 0 }$ the $\left( - 2 \right)$ -vectors outside of the $\tilde { A } _ { 1 3 }$ cycle with intersections $0 , 2$ are:

$$
\begin{array} { r l } & { a _ { 0 } ^ { - 1 , 0 } , \ a _ { 0 } ^ { 1 , 0 } , \ a _ { 2 } ^ { 0 , 0 } , \ a _ { 2 } ^ { 0 , 1 } , \ a _ { 2 } ^ { 1 , 1 } , \ a _ { 2 } ^ { 0 , 1 } , \ a _ { 4 } ^ { 1 , 1 } , \ a _ { 6 } ^ { 1 , 2 } , \ a _ { 6 } ^ { 1 , 2 } , \ a _ { 8 } ^ { 1 , 2 } , \ a _ { 1 0 } ^ { 1 , 3 } , \ a _ { 1 0 } ^ { 2 , 3 } , } \\ & { a _ { 1 2 } ^ { 1 , 3 } , \ a _ { 1 2 } ^ { 2 , 3 } , \ a _ { 1 2 } ^ { 2 , 4 } ; } \\ & { a _ { 0 } ^ { - 1 , - 1 } , \ a _ { 0 } ^ { 0 , - 1 } , \ a _ { 0 } ^ { 0 , 1 } , \ a _ { 0 } ^ { 1 , 1 } , \ a _ { 2 } ^ { - 1 , 0 } , \ a _ { 2 } ^ { 1 , 0 } , \ a _ { 4 } ^ { 1 , 2 } , \ a _ { 6 } ^ { 2 , 4 } , \ a _ { 6 } ^ { 0 , 1 } , \ a _ { 6 } ^ { 0 , 2 } , \ a _ { 6 } ^ { 1 , 1 } , \ a _ { 6 } ^ { 2 , 2 } , } \\ & { a _ { 8 } ^ { 0 , 2 } , \ a _ { 8 } ^ { 1 , 3 } , \ a _ { 8 } ^ { 2 , 2 } , \ a _ { 8 } ^ { 2 , 3 } , \ a _ { 1 0 } ^ { 1 , 2 } , \ a _ { 1 2 } ^ { 1 , 4 } , \ a _ { 1 2 } ^ { 3 , 4 } ; } \end{array}
$$

For $b _ { 1 }$ the $\left( - 2 \right)$ -vectors outside of the $\tilde { A } _ { 1 3 }$ cycle with intersections $0 , 2$ are:

$$
\begin{array} { l l } { { a _ { 0 } ^ { - 1 , 0 } , a _ { 0 } ^ { 0 , 0 } , a _ { 2 } ^ { - 1 , 0 } , a _ { 2 } ^ { 0 , 0 } , a _ { 4 } ^ { 0 , 1 } , a _ { 4 } ^ { 1 , 3 } . } } \\ { { a _ { 0 } ^ { - 1 , - 1 } , a _ { 2 } ^ { 0 , 1 } , a _ { 6 } ^ { 0 , 1 } , a _ { 8 } ^ { 0 , 2 } , a _ { 8 } ^ { 1 , 2 } , a _ { 1 0 } ^ { 1 , 3 } . } } \end{array}
$$

The other intersection numbers are recovered by the fact that Eichler transformations are isometries, the symmetries $( u _ { i } , v _ { j } ) = ( u _ { i - k } , v _ { j - k } )$ $( u , v \in \{ a , b \} )$ for as long as all the indices stay in $\{ 0 , \ldots 1 3 \}$ . Going around the circle the shift is $u _ { i + 1 4 } ^ { n _ { 1 } , n _ { 2 } } = u _ { i } ^ { n _ { 1 } - 2 , n _ { 2 } - 4 }$

Example 3.10. $b _ { 1 }$ is a $\left( - 2 \right)$ -vector of divisibility 2 which does not lie on the $\tilde { A } _ { 1 3 }$ - cycle.
The vectors which have intersection 0 with $b _ { 1 }$ are $e _ { i }$ for $i \neq 1$ and $a _ { 0 } ^ { - 1 , 0 }$ , ， $a _ { 0 } ^ { 0 , 0 }$ , $a _ { 2 } ^ { - 1 , 0 }$ , $a _ { 2 } ^ { 0 , 0 }$ , $a _ { 4 } ^ { 0 , 1 }$ , $a _ { 1 2 } ^ { 1 , 3 }$ . Using the rules above, we obtain that $( a _ { 0 } ^ { 0 , 0 } , a _ { 2 } ^ { - 1 , 0 } ) =$ $( a _ { 0 } ^ { - 1 , 0 } , a _ { 2 } ^ { 0 , 0 } ) = 2$ and all the other intersection numbers among these six vectors are zero.
This is the same diagram of $\left( - 2 \right)$ -curves as the one for the $( 1 6 , 2 , 1 )$ lattice obtained from the Coxeter diagram given in [AN06, Table 1] by applying the Weyl group $W ( A _ { 1 } ) = S _ { 2 }$ for the unique black vertex.
This agrees with Lemma 4.15.

3F. Lattices on the $g = 0$ line.
Several of the lattices on the $g = 0$ line have finite Coxeter diagrams.
They are quite large and complicated.
We don’t need them for the present paper since they don’t appear as targets of the mirror moves 5.6, see Remark 5.7. So we don’t include them here; they will appear elsewhere.

4. K3 surfaces, their quotients, and the nef cones

We give a brief description for the K3 surfaces $X$ and their quotients $Y$ that appear in the 75 families of Fig.

4A. Surfaces for $S$ with $g \geq 2$ , excluding $( 1 0 , 8 , 0 )$ . For the 50 lattices with $g \geq 2$ , excluding $( 1 0 , 8 , 0 )$ , a satisfactory description for the quotients $Y$ is given in [AN06]. Indeed, all the possibilities for the exceptional curves on the surfaces $Y$ appearing in these families were found.
From the graph of exceptional curves one can realize $Y$ as an explicit blowup of $\mathbb { P } ^ { 2 }$ or $\mathbb { F } _ { n }$ . The K3 surfaces $X$ are double covers of $Y$ branched in some divisor $B$ lying in the linear system $\mid - 2 K _ { Y } \mid$ .

For the most basic lattices $( r , r , \delta )$ with $r \leq 9$ , the surfaces $Y$ are weak del Pezzo surfaces with big and nef $- K _ { Y }$ and with $A D E$ singularities.
Thus, $Y = \mathrm { B l } _ { r - 1 } \mathbb { P } ^ { 2 }$ for $( r , r , 1 )$ and $Y = \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ or $\mathbb { F } _ { 2 }$ for $( 2 , 2 , 0 )$ .

4B. Surfaces for $S$ on the $g = 1$ line and $( 1 0 , 8 , 0 )$ . This case is especially important for us since it serves as the base case for the mirror symmetry constructions and all the other cases are derived from it.

Theorem 4.1 (Nikulin).
Let $X$ be a $K \mathcal { 3 }$ surface with a nonsymplectic involution ι and 2-elementary Picard lattice $S = \operatorname* { P i c } X$ . Denote $\pi \colon X \to Y = X / \iota$ . Then the automorphism group $\operatorname { A u t } X$ is infinite and preserves $a$ (necessarily unique) elliptic pencil $f \colon X \to \mathbb { P } ^ { 1 }$ if and only if $S$ is one of the following lattices:

(1) $I _ { 2 k } I _ { 0 }$ : $( 1 0 + k , 1 0 - k , \delta ) \neq ( 1 4 , 6 , 0 )$ and $k > 0$ . $Y$ is a rational elliptic surface with a section and the ramification divisor $R = X ^ { \iota } = F _ { 0 } \cup \cup _ { i = 0 } ^ { k - 1 } E _ { 2 i } ,$ where $F _ { 0 }$ is a smooth elliptic fiber, and $E _ { i }$ are disjoint $\mathbb { P } ^ { 1 } { \boldsymbol { s } }$ which are the alternating curves in the $I _ { 2 k }$ fiber $F$ of Kodaira type $I _ { 2 k }$ (a wheel of $2 k$ rational curves).\
(2) $I _ { 0 } ^ { 2 }$ : $( 1 0 , 8 , 0 )$ . $R = F _ { 0 } \cup F$ is a union of two smooth fibers of $f$ .\
(3) Halphen: $( 1 0 , 1 0 , 1 )$ . $Y$ is an index 2 Halphen pencil and $R = F _ { 0 }$ is a smooth elliptic fiber which does not ramify over the unique multiple fiber $G = 2 D$ on $Y$ .\
(4) Enriques: $( 1 0 , 1 0 , 0 )$ . $Y$ is an Enriques surface and $R = \emptyset$ .\
(5) ${ \widetilde { E } } _ { 6 }$ : $( 1 4 , 6 , 0 )$ : $R$ is the sum of a smooth elliptic fiber $F _ { 0 }$ and 4 disjoint $\mathbb { P } ^ { 1 } { \boldsymbol { s } }$ , alternating curves in a $I V ^ { * }$ fiber.

In the $I _ { 0 } ^ { 2 }$ case one has $g = 2$ , in the other cases one has $g = 1$ .

Proof.
[Nik81, Sec. 4] and [Nik20].

We will call (1,2,3) the ordinary cases.
The case (5) does not appear on the mirror side in our constructions.

4C. Surfaces for $S$ on the $g = 0$ line.
The lattices $( 1 0 + k , 1 2 - k , \delta )$ for $1 \leq k \leq 9$ are in a bijection with the lattices $( 1 0 + k , 1 0 - k , \delta )$ on the line below in Fig. 1, excluding $( 1 4 , 6 , 0 )$ , which is the $( \widetilde { E } _ { 6 } )$ case of Theorem 4.1.

Consider one of the lattices $S ^ { \prime } = ( 1 0 + k , 1 0 - k , \delta )$ , $1 \leq k \leq 9$ on the $g = 1$ line.
This is the case (1) of Theorem 4.1. The quotient $Y ^ { \prime }$ is a rational elliptic surface with a section and $\pi \colon X ^ { \prime } \to Y ^ { \prime }$ is ramified in a smooth elliptic fiber $F _ { 0 }$ and ramified in the $n$ alternating curves $( - 4 )$ -curves $E _ { 2 i }$ . It follows that $S ^ { \prime } = U \oplus K$ for some negative definite lattice $K$ . (Indeed, these are the lattices $A _ { 2 k - 1 } E _ { 9 - k } ( 2 )$ of Table 2.)

Now let $S = U ( 2 ) \oplus K$ . Then $S = ( 1 0 + k , 1 2 - k , \delta )$ is the corresponding lattice on the $g = 0$ line.
The line bundle corresponding to an isotropic vector in $U ( 2 )$ defines an elliptic fibration $f \colon X \to \mathbb { P } ^ { 1 }$ without a section whose jacobian fibration is $f ^ { \prime } \colon X ^ { \prime } \to \mathbb { P } ^ { 1 }$ . The fiber corresponding to $F$ is a double fiber of $f$ and the ramification divisor of $\pi \colon X \to Y$ is the union of the $n$ curves $E _ { 2 i }$ . The surface $X$ can be obtained from $X ^ { \prime }$ directly by a logarithmic transformation at $F ^ { \prime }$ using [CD89, Cor. 5.4.7].

So these K3 surfaces $X$ are the index 2 Halphen K3 surfaces with an $I _ { 2 k }$ fiber.
The surfaces $Y$ obtained by contracting the $( - 1 )$ -curves in the special fiber are the rational index 2 Halphen pencils with an $I _ { k }$ fiber.
Some explicit constructions for such pencils were given in [Kim18, Kim20, Zan20].

Finally, the moduli space for the lattice $( 2 0 , 2 , 1 )$ is a point.
It is the unique “most algebraic” 2-elementary K3 surface of [Vin83]. It admits no Halphen pencils but we computed that up to automorphisms, it has 13 elliptic pencils with a section.

4D. Nef cones and exceptional curves on $X$ and $Y$ . It is well known that the nef cone of a K3 surface $X$ is defined by linear inequalities in the positive cone $\mathcal { C } = \left\{ v \in S _ { X } \otimes \mathbb { R } \vert x ^ { 2 } \geq 0 \right.$ , $x \cdot h \geq 0 \}$ , where $h$ is a K¨ahler class, with facets $x \cdot E _ { i } \geq 0$ for the smooth rational curves $E _ { i }$ with $E _ { i } ^ { 2 } = - 2$ , which we call the $\left( - 2 \right)$ -curves.
Their classes in $\operatorname { N S } ( X )$ are the positive roots for the Weyl group $W _ { 2 } ( S _ { X } )$ . For any $\left( - 2 \right)$ -vector $v \in \operatorname { N S } ( X )$ , exactly one of $\pm v$ is effective and is a sum of $\left( - 2 \right)$ -curves.

Since a $\left( - 2 \right)$ -curve is uniquely determined by its class in $\operatorname { N S } ( X )$ , any involution preserving its class preserves the $\left( - 2 \right)$ -curve, but may not fix it pointwise.

We call a curve exceptional if it is irreducible and has negative self-intersection.
$R = X ^ { \iota }$ will denote the ramification divisor of $\pi \colon X \to Y$ and $B \subset Y$ the branch divisor.

Lemma 4.2. Exceptional curves $F$ on $Y$ are of three types:

(1) $F ^ { 2 } = - 4$ , $\pi ^ { * } ( F ) = 2 E$ , and the $\left( - 2 \right)$ -curve $E \subset X ^ { \iota }$ is fixed pointwise by the involution.\
(2a) $F ^ { 2 } = - 1$ , $\pi ^ { * } ( F ) = E$ , $| F \cap B | = | E \cap R | = 2$ .\
(2b) $F ^ { 2 } = - 1$ , $\pi ^ { * } ( F ) = E _ { 1 } + E _ { 2 }$ , $F$ is tangent to $B$ , the curves $E _ { 1 }$ , $E _ { 2 }$ are exchanged by the involution and $E _ { 1 } \cdot E _ { 2 } = 1$ .\
(3) $F ^ { 2 } = - 2$ , $\pi ^ { * } ( F ) = E _ { 1 } + E _ { 2 }$ , $F \cap B = E _ { i } \cap R = \emptyset$ , the curves $E _ { 1 }$ , $E _ { 2 }$ are disjoint and are exchanged by the involution.

Proof.
[AN06, Sec. 2.4].

Lemma 4.3. Nef $Y = ( \operatorname { N e f } X ) \cap S _ { \mathbb { R } }$ , where $S = S _ { X } ^ { + }$

Proof.
This follows from the identities $\iota ^ { * } \circ \iota _ { * } = 1 + \iota$ and $\iota _ { * } \circ \iota ^ { * } = 2$ .

Definition 4.4. Let $\mathrm { C u r } _ { 2 } = \{ F _ { i } \}$ be the set of the $\left( - 2 \right)$ -curves on $Y$ , i.e. of type (3) in Lemma 4.2. Let $\pi ^ { * } ( F ) = E _ { 1 } + E _ { 2 }$ be the corresponding $( - 4 )$ -vectors in $S$ . It is obvious that for any $v \in S$ one has $\pi ^ { * } ( F ) \cdot v \ : = \ : 2 E _ { 1 } \cdot v \in 2 \mathbb { Z }$ . They are also primitive since $( \pi ^ { * } ( F ) / 2 ) ^ { 2 } = - 1$ and $S$ is an even lattice.
So they are simple roots for the full reflection group $W _ { \mathrm { r } } ( S )$ and they correspond to a subset $\mathbb { B }$ of black vertices in the Coxeter diagram of $S$ as in Definition 3.2.

Lemma 4.5. Nef $Y = W ( \mathbb { B } ) . \mathfrak { C } _ { \mathrm { r } }$ , where $\mathfrak { C } _ { \mathrm { r } }$ is a fundamental chamber for $W _ { \mathrm { r } } ( S )$ . The set of exceptional curves on $Y$ is identified with the union of $W ( { \mathbb { B } } )$ -orbits of white vertices in the Coxeter diagram of $S$ .

Proof.
This follows by Corollary 3.4 and the description of $\mathrm { N e f } \ X$ above.

4E. Surfaces $Y$ with the smallest nef cone.

Proposition 4.6. For each lattice $S \ne ( 1 0 , 1 0 , 0 )$ , with $g \geq 1$ of Fig. 1 there exists a $K \mathcal { 3 }$ surface with $S _ { X } ^ { + } = S$ such that ${ \mathrm { N e f ~ } } Y$ can be identified with the Coxeter chamber for the full reflection group $W _ { \mathrm { r } }$ if $S \neq ( 1 2 , 8 , 1 )$ , and the Coxeter chamber for an index 2 subgroup $W ^ { \prime } \subset W _ { \mathrm { { r } } }$ if $S = ( 1 2 , 8 , 1 )$ .

Proof.
In view of Lemma 4.5 we need to find a quotient surface $Y$ on which the $\left( - 2 \right)$ curves form the entire black subdiagram of the Coxeter diagram, for $S \neq ( 1 2 , 8 , 1 )$

In the $( 1 2 , 8 , 1 )$ case we consider the fundamental chamber ${ \mathfrak { C } } _ { \mathrm { r } } ^ { \prime }$ for the index 2 subgroup of $W ^ { \prime } \subset W _ { \mathrm { r } }$ , a union of two fundamental chambers $\mathfrak { C } _ { \mathrm { r } }$ and $w { \mathfrak { C } } _ { \mathrm { r } }$ where $w$ is the reflection in the isolated $( - 4 )$ -root.
This modified chamber is also pictured in Fig. 3. The corresponding surface has an $I _ { 2 }$ fiber.

For the 50 lattices with $g \geq 2$ and different from $( 1 0 , 8 , 0 )$ existence of such $Y$ is a small part of [AN06] where all possibilities for the sets of exceptional curves were classified.
The surfaces we need here are “the most degenerate”, they all appear in [AN06, Table 3].

For the surfaces with an elliptic pencil with a section we take for $Y$ one of the surfaces of Table 1. They exist by [Per90]; see also [MP86, OS91].

Table 1. Special rational elliptic surfaces $Y$\
![](images/9a2fc5c31f9201188b5edbf95b1b5cbca628a00dd2113b44a432bafc667591e3.jpg)

In the $( 1 0 , 1 0 , 1 )$ Halphen case, the surface with a double ${ } _ { 2 } I _ { 0 }$ fiber can be obtained from a $( 1 0 , 8 , 0 )$ surface by a logarithmic transformation along a smooth $I _ { 0 }$ fiber using [CD89, Cor. 5.4.7]. 

Remark 4.7. Most of the surfaces of Table 1 are the maximally degenerate ones in their families but some are not: For $( 1 2 , 8 , 1 )$ the most degenerate surface has $I I I ^ { * } I I I$ fibers, and for $( 1 0 , 1 0 , 1 )$ the ${ _ 2 I _ { 1 } I I ^ { * } I _ { 1 } }$ fibers.

We use a logical notation $A _ { k - 1 } E _ { 9 - k }$ to denote the cases $( 1 0 + k , 1 0 - k , \delta )$ for $1 \leq k \leq 9$ . Here, $E _ { k }$ is the lattice $K ^ { \perp }$ in the Picard lattice for a a del Pezzo surface of degree $K ^ { 2 } = 9 - k$ . For $k = 1$ there are two cases, $E _ { 1 }$ for $\mathbb { F } _ { 1 }$ and $E _ { 1 } ^ { \prime }$ for $\mathbb { F } _ { 0 }$ .

Corollary 4.8. For the surfaces $Y$ of Proposition 4.6, the Coxeter diagram of $S$ also serves as the dual graph of exceptional curves, with the following modifications:

(1) Vertices: the double circled white, single white circles, and black vertices respectively correspond to $\mathbb { P } ^ { 1 }$ with $F ^ { 2 } = - 4$ , $^ { - 1 }$ , $- 2$ respectively.\
(2) Edges: $F _ { i } \cdot F _ { j } = 1$ for a white vertex $F _ { i }$ and a black vertex $F _ { j }$ or for two single circled white vertices.
The other intersection numbers are: $F _ { i } \cdot F _ { j } = 1$ for a single edge, and 2 for a bold edge in the diagram.

# 4F.

The Heegner divisor hierarchy.

Definition 4.9 (Heegner moves).
The $( - 1 , - 1 )$ -move goes from a node $( r , a , 1 )$ of Fig. 1 to the node $( r - 1 , a - 1 , \delta )$ . We call it ordinary if $\delta = 1$ and characteristic if $\delta = 0$ . The opposite $( + 1 , + 1 )$ -move goes from $( r , a , \delta )$ to $( r + 1 , a + 1 , 1 )$ . The $( + 1 , - 1 )$ -move is from $( r , a )$ to $( r + 1 , a - 1 )$ and the opposite $( - 1 , + 1 )$ -move is from $( r , a )$ to $( r - 1 , a + 1 )$ .

For the rest of this section, we exclude the lattice $S = ( 1 0 , 8 , 0 )$ which is in many ways exceptional, cf.
Remark 2.1.

Lemma 4.10. Let $S = ( r , a , \delta )$ and $\mathbb { D } _ { S }$ be its period domain, $S \longmapsto S ^ { \prime } = ( r ^ { \prime } , a ^ { \prime } , \delta ^ { \prime } )$ be $a \left( + 1 , + 1 \right)$ or $( + 1 , - 1 )$ -move.
Then $S ^ { \prime }$ defines a Heegner divisor $\mathbb { D } _ { S ^ { \prime } } \subset \mathbb { D } _ { S }$ on which the $K \mathcal { 3 }$ surfaces acquire an additional $\left( - 2 \right)$ -curve $E$ , preserved by the involution on $K \mathcal { 3 }$ surfaces over $S ^ { \prime }$ . For the $( + 1 , + 1 )$ -move, this involution preserves but does not $\mathit { f i x } \mathit { E }$ and for the $( + 1 , - 1 )$ -move, it fixes $E$ pointwise.

Proof.
Let $X \to ( C , 0 )$ be a smooth family of K3 surfaces with $[ X _ { 0 } ]$ generic in $\mathbb { D } _ { S ^ { \prime } }$ , i.e. $H ^ { 2 } ( X _ { 0 } , \mathbb { Z } ) ^ { + } = S ^ { \prime }$ and with $[ X _ { t } ] \in \mathbb { D } _ { S } \backslash \mathbb { D } _ { S ^ { \prime } }$ for $t \neq 0$ . Let $R _ { t }$ be the ramification divisor on $X _ { t }$ , $t \neq 0$ , $\overline { { R } } _ { 0 }$ be its flat limit, and $R _ { 0 }$ be the ramification divisor of the involution of $X _ { 0 }$ determined by $S ^ { \prime }$ . Then for a

This is proven by considering the small contraction $X  { \overline { { X } } }$ which contracts $E$ to a point.
The birational involution on $X$ equaling $\iota _ { t }$ on the general fiber extends to a regular involution of $\overline { { X } }$ and the two cases are distinguished simply by whether the contraction of $E$ lies on the limit of $R _ { t }$ (necessarily a node of the limiting curve) or is disjoint from the limit.
In the former $( + 1 , + 1 )$ case, the involution on the minimal resolution $X _ { 0 }  \overline { { X } } _ { 0 }$ preserves $E$ but only fixes the two branches of the node.
In the latter $( + 1 , - 1 )$ case, the involution on $X _ { 0 }$ fixes $E$ pointwise, because the contraction of $E$ is isolated in the fixed locus of the involution on $\overline { { X } } _ { 0 }$ . 

Lemma 4.11. Any 2-elementary lattice with $g \geq 1$ has the form

$$
S = ( 1 0 + k - ( g - 1 ) , 1 0 - k - ( g - 1 ) , \delta )
$$

and it can be reached from one of the lattices of Section 4B with $g = 1$ by $g - 1$ total $( - 1 , - 1 )$ -moves.

Proof.
One look at Fig. 1 confirms this.

Next, we want to understand how Coxeter diagrams change.

Lemma 4.12. For the lattices related by $a$ $( - 1 , - 1 )$ -move one has $S = S ^ { \prime } \oplus A _ { 1 }$ and a generator $r$ of $A _ { 1 }$ is $a$ $\left( - 2 \right)$ -root of divisibility 2. For any hyperbolic lattice $S =$ $( r , a , 1 )$ there exists exactly one or two $O ( S )$ -orbits of $\left( - 2 \right)$ -roots of divisibility 2, and these vectors are in a bijection with the $( - 1 , - 1 )$ -moves down from $S$ .

In terms of the Coxeter diagram $\Gamma$ , for any $S \neq ( 1 0 , 8 , 0 )$ they are in bijection with the Aut Γ-orbits of white vertices in $\Gamma$ which are not connected to some neighbor by a single (i.e. weight 1) edge.

Proof.
One has

$$
S ^ { \prime } \oplus A _ { 1 } = ( r - 1 , a - 1 , \delta ) _ { 1 } + ( 1 , 1 , 1 ) _ { 0 } = ( r , a , 1 ) _ { 1 } \simeq S .
$$

For $S = S ^ { \prime } \oplus A _ { 1 } = S ^ { \prime \prime } \oplus A _ { 1 }$ with $S ^ { \prime } , S ^ { \prime \prime }$ of the same type, an isometry $S ^ { \prime }  S ^ { \prime \prime }$ defines an isometry $S  S$ , so there is exactly one $O ( S )$ -orbit.
The generator of $A _ { 1 }$ is a $\left( - 2 \right)$ -root and it clearly has divisibility 2. By Prop.
on p.2 of [Vin83] such roots lie in different $W _ { \mathrm { r } }$ -orbits.
One has $O ( S ) = \mathrm { A u t } \Gamma \ltimes W _ { \mathrm { r } }$ , so two such roots in the same orbit must differ by a diagram symmetry.
Finally, for all the lattices in Fig. 1 with the exception of $( 1 0 , 8 , 0 )$ the roots generate the lattice, so $\mathrm { d i v } ( r ) = 2$ iff $r \cdot r _ { i }$ is even for the other roots, which is read off directly from the diagram.


Corollary 4.13. Any lattice in Fig. 1 with $g \geq 1$ is of the form

$$
S = { \big ( } 1 0 + k - ( g - 1 ) , 1 0 - k - ( g - 1 ) , \delta { \big ) } .
$$

It can be reached from the “base” lattice $S _ { 1 } = ( 1 0 + k , 1 0 - k , 1 ) = S \oplus A _ { 1 } ^ { g - 1 }$ by $a$ sequence of $( - 1 , - 1 )$ -moves which corresponding to a chain of vertices $\alpha _ { 1 } , \ldots , \alpha _ { g - 1 }$ with colors white-black-. . . -black, in the Coxeter diagram $\Gamma _ { \mathrm { r } } ( S )$ , with $\alpha _ { 1 }$ an even $\left( - 2 \right)$ -root.
This chain is unique up to $\mathrm { A u t } \Gamma$ .

Remark 4.14. The $( + 1 , - 1 )$ moves play a particularly important role from the perspective of moduli, because of Lemma 4.10. Recall that $F _ { S } = ( { \mathbb D } _ { S } \setminus \Delta ) / O ( T )$ . The divisors in $\Delta / O ( T )$ correspond to Heegner divisor moves of either $( + 1 , - 1 )$ type or $( + 1 , + 1 )$ -type.
For a Heegner divisor of $( + 1 , - 1 )$ -type, the involution on the limiting of K3 surface has an extra $\left( - 2 \right)$ -curve, fixed pointwise by the involution, but the flat limit of a positive genus fixed component $C _ { g }$ equals the positive genus fixed component.
Thus from the perspective of the KSBA compactification $F _ { S } \hookrightarrow { \overline { { F } } } _ { S }$ for pairs $( \overline { { \boldsymbol { X } } } , \epsilon \overline { { \boldsymbol { C } } } _ { g } )$ , the $( + 1 , - 1 )$ -move plays essentially no role, except to restrict to a Noether-Lefschetz subdomain of $\overline { { F } } _ { S }$ .

Thus, it suffices to compactify the moduli space $F _ { S }$ for lattices $S$ on the $k = 0$ line, and the other cases follow by induction.
For the hyperbolic 2-elementary lattices $T = I ^ { \perp } / I$ associated to Type III cusps of $F _ { S }$ (cf.
Sec.
5), the action of a $( + 1 , - 1 )$ Heegner move on $S$ is a $( - 1 , - 1 )$ move on $\overline { T }$ . This is why Corollary 4.13 is relevant: We can reach all necessary hyperbolic lattices for semitoroidal compactifications from those on the $g = 1$ line.

Lemma 4.15. The Coxeter diagram $\Gamma ^ { \prime }$ of $S ^ { \prime }$ is obtained from the diagram $\Gamma$ of $S = S ^ { \prime } \oplus A _ { 1 }$ by removing the vertex $r$ , removing the adjacent white vertices, turning black adjacent vertices to white and, if there exist $( - 4 )$ -roots $\alpha _ { 1 } , \alpha _ { 2 }$ with $\alpha \cdot \alpha _ { 1 } =$ $\alpha \cdot \alpha _ { 2 } = 2$ , connecting their images in $\Gamma _ { 1 }$ by a double line.

Proof.
The fundamental chamber for $S ^ { \prime }$ is the face $\alpha ^ { \perp }$ of the fundamental chamber for $S ^ { \prime } \oplus A _ { 1 }$ . The facets of this chamber are of the form $p ( \alpha _ { i } ) ^ { \perp }$ where $p ( \alpha _ { i } )$ are the orthogonal projections of the roots defining the facets for $S$ for which $p ( \alpha _ { i } ) ^ { 2 } < 0$ . The formula $p ( \alpha _ { 1 } ) \cdot p ( \alpha _ { 2 } ) = \alpha _ { 1 } \cdot \alpha _ { 2 } + \frac { 1 } { 2 } ( \alpha \cdot \alpha _ { 1 } ) ( \alpha \cdot \alpha _ { 2 } )$ implies the rest: For the $\left( - 2 \right)$ -neighbors $\alpha _ { 1 }$ of $\alpha$ with $\alpha \cdot \alpha _ { 1 } = 2$ one gets $p ( \alpha _ { 1 } ) ^ { 2 } = 0$ , so they are not faces of $\alpha ^ { \perp }$ , and for $( - 4 )$ -neighbors with $\alpha \cdot \alpha _ { 1 } = 2$ one gets $p ( \alpha _ { 1 } ) ^ { 2 } = - 2$ , so they change their color.


Lemma 4.16. Let $S , S _ { 1 }$ and $\alpha _ { 1 } , \ldots , \alpha _ { g - 1 }$ be as in Corollary 4.13. Let $G \subset \Gamma ( S )$ and $G _ { 1 } \subset \Gamma ( S _ { 1 } )$ be the subdiagrams such that for the vertices one has $V ( S _ { 1 } ) =$ $V ( S ) \cup \{ \alpha _ { 1 } , . . . , \alpha _ { g } \}$ . Then

(1) $G _ { 1 }$ is elliptic iff $G$ is too, and no vertex of $G$ is a neighbor of $\alpha _ { 1 } , \ldots , \alpha _ { g - 1 }$ (2) $G _ { 1 }$ is maximal parabolic if $G$ contains a parabolic subdiagram and either no vertex of $G$ is a neighbor of $\alpha _ { 1 } , \ldots , \alpha _ { g - 1 }$ or $g - 1 = 1$ and $\alpha _ { 1 }$ neighbors one isolated vertex of $G$ .

Proof.
If $\beta$ is a vertex of $G$ attached to $\alpha _ { 1 }$ then $\beta ^ { 2 } ~ = ~ - 2$ and $\beta \cdot \alpha _ { 1 } = 2$ , so $\langle \beta , \alpha _ { 1 } \rangle = \widetilde { A } _ { 1 }$ is already parabolic.
(1) immediately follows.
In the parabolic case, maximal parabolic subgraphs have rank $\operatorname { r k } S - 1$ , so the remaining part is nonempty and contains a nonempty maximal parabolic subdiagram.
For the exceptional cases $S _ { 1 } ~ = ~ ( 1 8 , 2 , 1 )$ and $( 1 7 , 3 , 1 )$ the diagrams for the lattice $S _ { 2 } ~ = ~ ( 1 7 , 1 , 1 )$ , resp.
$( 1 6 , 2 , 1 )$ contain parabolic subdiagrams $\widetilde { D } _ { 1 4 }$ , resp.
$\widetilde { D } _ { 1 2 }$ disjoint from $\stackrel { \sim } { A } _ { 1 }$ . 

Lemma 4.17. For the surfaces of Corollary 4.8 for which the Coxeter diagram is the dual graph of the exceptional curves on the quotients, the surface $Y _ { 1 }$ is obtained from $Y$ by contracting a $( - 1 )$ -curve $F ^ { \prime }$ not contained in the branch divisor $B$ . The surface $X _ { 1 }$ is obtained from $X$ by contracting $a$ $\left( - 2 \right)$ -curve not contained in the ramification divisor $R$ , and then smoothing the singular $K \mathcal { 3 }$ surface together with an involution.

Remark 4.18. The $( + 1 , - 1 )$ and $( - 1 , + 1 )$ moves in Fig. 1 do not admit such an easy description.
In those cases $S$ corresponds to an index 2 overlattice of $S ^ { \prime } \oplus A _ { 1 }$ . The $( r , a , \delta _ { 1 } ) \longmapsto ( r - 1 , a + 1 , \delta )$ move can be understood as contracting a $( - 4 )$ - curve on $Y ^ { \prime }$ and then smoothing.
For example, $( 2 , 0 , 0 ) \longmapsto ( 1 , 1 , 1 )$ is a smoothing of $\mathbb { F } _ { 4 } ^ { 0 } = \mathbb { P } ( 1 , 1 , 2 )$ to $\mathbb { P } ^ { 2 }$ . But that is a far trickier operation than contracting a $( - 1 )$ -curve.
There is also no obvious relation between the Coxeter diagrams.
For example, in the sequence $( 1 9 , 1 , 1 ) \mapsto ( 1 8 , 2 , 1 ) \mapsto ( 1 7 , 3 , 1 ) \mapsto ( 1 6 , 4 , 1 )$ the diagrams go from being finite to infinite to finite again, see Sections 3D and $\mathrm { 3 E }$ .

# 5. The cusps of $\mathbb { D } _ { S } / O ( T )$

Let $\boldsymbol { S } = ( r , a , \delta )$ be one of the 2-elementary hyperbolic lattices of Fig. 1, $T =$ $S ^ { \perp } = ( 2 2 - r , a , \delta ) _ { 2 }$ , and $\rho$ the corresponding involution of $L _ { \mathrm { K 3 } }$ for which $S$ and $T$ are the $( \pm 1 )$ -eigenspaces.
By Section 2C we have a moduli space $F _ { S } = ( \mathbb { D } _ { S } \backslash \Delta ) / O ( T )$ . As in Section 2D, the boundary of the Baily-Borel compactification consists of

(1) points, called 0-cusps, in bijection with the $O ( T )$ -orbits of isotropic lines $I = \mathbb { Z } e \subset T$ , $e ^ { 2 } = 0$ ,\
(2) modular curves, called 1-cusps, in bijection with the $O ( T )$ -orbits of isotropic planes $J \subset T$ .

A 0-cusp appearing in the compactification of a modular curve 1-cusp corresponds to an inclusion $I \subset J$ . In this section we find all cusps, together with their incidence relations.

5A. Isotropic vectors in 2-elementary discriminant groups.
For a nonzero vector $T$ its divisibility $\mathrm { d i v } ( v ) \in \mathbb { N }$ is defined by $v \cdot T = \operatorname { d i v } ( v ) \mathbb { Z }$ . Since $T$ is 2- elementary, $\mathrm { d i v } ( v ) = 1$ or 2. Define $v ^ { * } = v / \operatorname { d i v } ( v ) \in A _ { T }$ ; one has $v ^ { * } = 0$ iff $\mathrm { d i v } ( v ) = 1$ . If $e$ is a primitive isotropic vector then one certainly has $q _ { T } ( e ^ { * } ) = 0$ . Thus, the first step in classifying the 0-cusps is to understand the isotropic vectors in the finite discriminant group $A _ { T }$ . For this, one has the following result of Nikulin.

Definition 5.1. For an 2-elementary lattice $H$ the form $q$ $( \mathrm { m o d } \ \mathbb { Z } ) \colon A _ { H }  \frac { 1 } { 2 } \mathbb { Z } / \mathbb { Z }$ is linear.
A nonzero vector $v ^ { * } \in A _ { H }$ is called characteristic if $q ( x ) = ( x , v ^ { * } )$ (mod $\mathbb { Z }$ ) for all $x \in A _ { T }$ . It is called ordinary otherwise.
Note that if the lattice $H$ is co-even then $q$ (mod $\mathbb { Z } ) \equiv 0$ and there are no characteristic vectors.

Lemma 5.2 ([Nik79a], Lemma 3.9.1). Let $\left( A _ { T } , q _ { T } \right)$ be the discriminant group of an even 2-elementary lattice.
Then there are at most two orbits of nonzero isotropic vectors in $A _ { T }$ : ordinary and characteristic (thus, at most three including $e ^ { * } = 0$ ).

Definition 5.3. Let $H$ be a 2-elementary lattice and $e \in T$ be a primitive isotropic vector.
We say that $e$ is odd or simple if $\mathrm { d i v } ( e ) = 1$ ; $e$ is even ordinary if $\mathrm { d i v } ( e ) = 2$ and $e ^ { * }$ is ordinary; and $e$ is even characteristic if $\mathrm { d i v } ( e ) = 2$ and $e ^ { * }$ is characteristic.

# 5B.

Isotropic vectors in 2-elementary lattices.

Lemma 5.4. Let $K \subset T$ be a primitive sublattice.
If $K$ and $T$ are $p$ -elementary for some prime $p$ then so is $K ^ { \perp }$ .

Proof.
By [Nik79a, 1.15.1] the discriminant group of $K ^ { \perp }$ is $G ^ { \perp } / G$ for a certain subgroup $G \subset A _ { T } \oplus A _ { K }$ . If $A _ { T }$ , $A _ { K }$ are vector spaces over $\mathbb { F } _ { p }$ then so is $A _ { K ^ { \perp } }$ . $\boxed { \begin{array} { r l } \end{array} }$

Proposition 5.5. Let $T$ be an even indefinite 2-elementary lattice of signature $( n _ { + } , n _ { - } )$ , $e \in T$ a nonzero primitive isotropic vector, and let $\overline { { T } } = e ^ { \perp } / e$ . Then there exist sublattices $H , K \subset T$ such that ${ \cal T } = { \cal H } \oplus { \cal K }$ , $K \simeq \overline { { T } }$ , $e \in H$ , and exactly one of the following holds.
If $\delta _ { T } = \delta _ { \overline { { { T } } } }$ :

(1) $H = U$ , $a _ { T } = a _ { T }$ and e is odd (Def.
5.3).\
(2) $H = U ( 2 )$ , $\begin{array} { r } { a _ { \overline { { T } } } = a _ { T } - 2 } \end{array}$ and $e$ is even ordinary.

If $\delta _ { T } = 1$ and $\delta _ { \overline { { { T } } } } = 0$ :

(3) $H = I _ { 1 , 1 } ( 2 )$ , $\begin{array} { r } { a _ { \overline { { T } } } = a _ { T } - \cdot 2 } \end{array}$ and $e$ is even characteristic.

An isotropic vector of type (1–3) exists iff there exists a 2-elementary lattice $\overline { T }$ of signature $( n _ { + } - 1 , n _ { - } - 1 )$ with the invariants ( $r _ { \overline { { { T } } } } = r _ { T } - 2 , a _ { \overline { { { T } } } } , \delta _ { \overline { { { T } } } } )$ , and then it is unique up to $O ( T )$ -action.

Here, $I _ { 1 , 1 } = \langle 1 \rangle \oplus \langle - 1 \rangle$ is the odd hyperbolic unimodular hyperbolic rank-2 lattice; recall that $I I _ { 1 , 1 } = U$ is the even one.

Proof.
Let $T = ( r _ { T } , a _ { T } , \delta _ { T } ) _ { n _ { + } }$ and $e ^ { * } = e / \mathrm { d i v } ( e ) \in A _ { T }$ . The lattice $\overline { { T } } = e ^ { \perp } / e$ has signature $( n _ { + } - 1 , n _ { - } - 1 )$ and its discriminant group is $A _ { \overline { { T } } } = ( e ^ { * } ) ^ { \perp } / e ^ { * }$ . If $\mathrm { d i v } ( e ) = 1$ then there exists an isotropic vector $f$ such that $\langle e , f \rangle = U$ , $T = U \oplus U ^ { \perp }$ and we are done.
This is case (1).

So suppose that $\mathrm { d i v } ( e ) = 2$ . Then $\begin{array} { r } { a _ { \overline { { T } } } = a _ { T } - 2 } \end{array}$ . Pick any lift $T \to K \subset e ^ { \bot }$ of the projection $e ^ { \perp } \to T$ . It exists and it is automatically an isometry.
So we got a primitive sublattice $K \simeq \overline { { T } }$ of $T$ . Let $H = K ^ { \perp } \subset T$ . One has $e \in H$ . By Lemma 5.4, $H$ is 2-elementary.
It is also hyperbolic.
So $H = U$ , $U ( 2 )$ or $I _ { 1 , 1 } ( 2 )$ .

The case $H = U$ is impossible since $\mathrm { d i v } ( e ) = 2$ . In the other two cases $H \oplus K \subset T$ have the same $u _ { H \oplus K } = u _ { T }$ , so they are equal.
If $H = U ( 2 )$ or if $H = I _ { 1 , 1 } ( 2 )$ , $\delta _ { T } = 1$ and $\delta _ { \overline { { { T } } } } = 0$ then we are done.
So suppose that $H = I _ { 1 , 1 } ( 2 )$ and $\delta _ { T } = \delta _ { \overline { { { T } } } } = 1$ .

Write $I _ { 1 , 1 } ( 2 ) = \langle e _ { 1 } , e _ { 2 } \rangle$ , $e _ { 1 } ^ { 2 } = 2$ , $e _ { 2 } ^ { 2 } = - 2$ and $e = e _ { 1 } + e _ { 2 }$ . One has $e \cdot e _ { 1 } = 2$ . Since $K$ is co-odd, there exists $x \in K$ of divisibility 2 such that $x ^ { 2 } \equiv 2$ (mod 4). Then $f = e _ { 1 } + x$ has divisibility 2 and satisfies $e \cdot f = 2$ , $f ^ { 2 } = 4 n$ . Then $( f - n e ) ^ { 2 } = 0$ and $\langle e , f - n e \rangle$ splits off a copy of $U ( 2 )$ so that $T = U ( 2 ) \oplus K ^ { \prime }$ as well, as in case (2).

Vice versa, if a lattice $\overline { T }$ with the invariants as in cases (1–3) exists then $T$ and $H \oplus { \overline { { T } } }$ are 2-elementary, even, indefinite and have the same $( r , a , \delta )$ . So they are isomorphic.
The statement about the types of $e ^ { * } \in A _ { T }$ is immediate.

If there are two vectors $e _ { 1 } , e _ { 2 }$ of the same type with isomorphic $T _ { i }$ then the isomorphisms $H _ { 1 }  H _ { 2 }$ , $K _ { 1 }  K _ { 2 }$ define an isometry $T  T$ . Noting that the primitive isotropic vectors in each $H _ { i }$ , $i = 1 , 2$ , are in the same $O ( H _ { i } )$ -orbit, this shows that $e _ { 1 } , e _ { 2 }$ and the splittings ${ \cal T } = H _ { i } \oplus K _ { i }$ are in the same $O ( T )$ -orbit.


# 5C.

The 0-cusps.

Definition 5.6 (Mirror moves).
We define three “mirror moves” from a node $( r , a , \delta )$ to a node $( \bar { r } , \bar { a } , \delta )$ of Fig.

$$
S = ( r , a , \delta ) _ { 1 }  S ^ { \perp } = T = ( 2 2 - r , a , \delta ) _ { 2 }  \overline { { { T } } } = ( \bar { r } , \bar { a } , \bar { \delta } ) _ { 1 } .
$$

where the move $T \sim T$ is one of the following:

(1) odd or simple: $( 2 2 - r , a , \delta ) _ { 2 }  ( 2 0 - r , a , \delta ) _ { 1 }$ , (2) even ordinary: $( 2 2 - r , a , \delta ) _ { 2 } \Rightarrow ( 2 0 - r , a - 2 , \delta ) _ { 1 }$ , (3) even characteristic: $( 2 2 - r , a , 1 ) _ { 2 } \Rightarrow ( 2 0 - r , a - 2 , 0 ) _ { 1 }$ .

$$
U ( 2 ) { \scriptstyle \longmapsto } \infty \quad \longmapsto \quad \bullet \quad \quad I _ { 1 , 1 } ( 2 ) { \scriptstyle \bullet - \quad \mapsto } \circ
$$

This makes Fig. 1 into a directed graph in which every vertex has in- and outdegrees equal to $0$ , $1$ , $2$ or 3.

Remark 5.7. The only nodes which are not targets of any mirror move are those on the line $g = 0$ and the point $( 1 4 , 6 , 0 )$ . In Fig. 1 they are marked in red.

Theorem 5.8. Let $S$ be one of the 2-elementary lattices of Fig. 1 and $e \in T$ $a$ primitive isotropic vector with $\overline { { T } } = e ^ { \perp } / e$ . Then the move $S  T$ is one of the mirror moves of Def.
5.6. Moreover, if Fig. 1 allows for a particular move then there exists a unique 0-cusp of $\mathbb { D } _ { S } / O ( T )$ of that type.

Proof.
This follows immediately from Proposition 5.5 applied to $T = S ^ { \perp }$ . Indeed, in this case $T$ is again hyperbolic and it admits a primitive embedding into $L _ { \mathrm { { K 3 } } }$ . So it corresponds to a node in Fig.

1. 

# 5D.

The 1-cusps.

Lemma 5.9. Let $T$ be an even indefinite 2-elementary lattice of signature $( n _ { + } , n _ { - } )$ , $J \subset T$ a primitive isotropic plane, and let $\overline { { \overline { { T } } } } = J ^ { \perp } / J$ . Then there exist sublattices $P , N \subset T$ such that $T = P \oplus N$ , $N \simeq \overline { { \overline { { T } } } }$ , $J \subset P$ , and exactly one of the following holds.
If $\delta _ { T } = \delta _ { \overline { { { T } } } }$ :

(1) $P = U ^ { 2 }$ and $a _ { \overline { { \overline { { T } } } } } = a _ { T }$ .\
(2) $P = U \oplus U ( 2 )$ and $a _ { \overline { { T } } } = a _ { T } - 2$ .\
(3) $P = U ( 2 ) ^ { 2 }$ and $a _ { \overline { { T } } } = a _ { T } - 4$ .

If $\delta _ { T } = 1$ and $\delta _ { \overline { { \overline { { T } } } } } = 0$

(4) $H = U \oplus I _ { 1 , 1 } ( 2 )$ and $\begin{array} { r } { a _ { \overline { { T } } } = a _ { T } - 2 } \end{array}$ .\
(5) $H = U ( 2 ) \oplus I _ { 1 , 1 } ( 2 )$ and $a _ { T } = a _ { T } - 4$ .

An isotropic plane of type $( 1 - 5 )$ exists iff there exists a 2-elementary lattice $\overline { { \overline { { T } } } }$ of signature $( n _ { + } - 2 , n _ { - } - 2 )$ with the invariants $( r _ { \overline { { \overline { { T } } } } } = r _ { T } - 4 , a _ { \overline { { \overline { { T } } } } } , \delta _ { \overline { { \overline { { T } } } } } )$ , and then it is unique up to $O ( T )$ -action.

Proof.
We apply Proposition 5.5 twice.

Theorem 5.10. On the diagram Fig. 1 the move $S  T  \overline { { \overline { { T } } } }  \overline { { \overline { { T } } } }$ can be seen by (1) making one of the three mirror moves $( r , a , \delta )  ( \bar { r } , \bar { a } , \delta )$ of Def.
5.6, (2) and then doing one of the following three moves:

![](images/fe524a88f2a17a0a97f8400c83b4df34f33978e16bdd1a34fddfcebbe69a446e.jpg) Table 2. 2-elementary negative definite lattices appearing at 1-cusps

(a) odd or simple: staying at the same vertex; we set $\bar { \bar { a } } = \bar { a }$ , $\bar { \bar { \delta } } = \bar { \delta }$ .\
(b) even ordinary: dropping down by 2 and keeping the color; here, we set $\bar { \bar { a } } = \bar { a } - 2$ , $\bar { \bar { \delta } } = \bar { \delta }$ .\
(c) even characteristic: dropping down by 2 and changing the color from black $\delta = 1$ to white $\bar { \bar { \delta } } = 0$ ; we set $\bar { \bar { a } } = \bar { a } - 2$ .

The final vertex of Fig. 1 is interpreted as a negative definite lattice $\overline { { \overline { { T } } } }$ with the invariants $( \bar { \bar { r } } , \bar { \bar { a } } , \bar { \bar { \delta } } )$ , where $\bar { \bar { r } } = \bar { r } - 2 = 1 8 - r$ , and $\bar { a }$ , $\bar { \bar { \delta } }$ are as set above.

![](images/35df0bbaef8bfd5fbe3412c6d3d5df36be26639adfb2389f51c1eb145b743bbe.jpg)

A 1-cusp of this form exists iff Fig. 1 allows the two-move combination.
For each isomorphism class of $\overline { { \overline { { T } } } }$ there is a unique $O ( T )$ -orbit of the 1-cusps.

A 0-cusp corresponding to a mirror move $S \sim T$ contains the cusps $\overline { { \overline { { T } } } }$ above iff $\overline { { \overline { { T } } } }$ can be reached by going through $S  T$ as the first step.

Proof.
This follows by applying Lemma 5.9 and using the fact that by [Nik79a, Thm. 3.6.2] the allowed invariants of even 2-elementary hyperbolic lattices and of negative definite lattices are in a bijection with a shift $\bar { r } = \bar { r } - 2$ , so we can reuse Fig. 1 instead of making a new figure for the invariants of $\overline { T }$ that occur.


Theorem 5.11. For the 2-elementary lattices $S$ of Fig. 1, the isomorphism classes of the even negative definite 2-elementary lattices $\overline { { \overline { { T } } } }$ appearing for the 1-cusps of $\mathbb { D } _ { S } / O ( T )$ are uniquely determined by their invariants $( r , a , \delta )$ and the root sublattices $R$ , as listed in Table 2.

Notations of Table 2 are as follows: $R$ means that $\overline { { \overline { { T } } } }$ is the root lattice $R$ ; $R *$ that the root sublattice $R \subset { \overline { { \overline { { T } } } } }$ is a finite index sublattice and $\overline { { \overline { { T } } } }$ is obtained from $R *$ by adding a glue.
$R * *$ means that $R$ has infinite index in $\overline { { \overline { { T } } } }$ . The root lattices are given for the entire reflection group $W _ { \mathrm { r } }$ as explained in Section 3.

Proof.
Most of these lattices are found by listing the maximal parabolic subdiagrams of Coxeter diagrams of hyperbolic lattices, as described in Section 3. The two exceptional cases are $( 1 6 , 2 , 1 )$ and $( 1 5 , 3 , 1 )$ where Vinberg’s method does not apply.
For these cases we applied Kneser’s gluing method [CS99, 15.10.2]. 

Corollary 5.12. $\mathbb { D } _ { S } / O ( T )$ can have a maximum three of 0-cusps and a maximum 14 of 1-cusps, the latter happening only for $S = ( 4 , 4 , 1 )$ .

Proposition 5.13. The modular curve in $\overline { { \mathbb { D } / O ( T ) } }$ BB corresponding to a cusp $\overline { T }$ is isomorphic to $\mathbb { H } / \operatorname { S L } ( 2 , \mathbb { Z } )$ , resp.
$\mathbb { H } / \Gamma _ { 0 } ( 2 )$ if it is incident to a single 0-cusp, resp.
to two 0-cusps.

Here, $\mathbb { H }$ is the upper half plane and $\Gamma _ { 0 } ( 2 ) \subset \mathrm { S L } ( 2 , \mathbb { Z } )$ is the standard level-2 modular subgroup of index 3.

Proof.
Let $J \subset T$ be an isotropic plane corresponding to the 1-cusp.
Then the corresponding modular curve is $\mathbb { H } / \Gamma$ , where $\Gamma$ is the image of the stabilizer of $J$ in $\operatorname { S L } ( T )$ in $\operatorname { S L } ( J ) \simeq \operatorname { S L } ( 2 , \mathbb { Z } )$ . By Theorem 5.10, $T = P \oplus { \overline { { \overline { { T } } } } }$ , with $P$ one of the five signature $( 2 , 2 )$ lattices listed there.
Then $J$ is an isotropic plane in $P$ . So the statement is reduced for the five cases $T = P$ for which the check is immediate.
$\boxed { \begin{array} { r l } \end{array} }$

5E. 0-cusps and involutions of $L _ { \mathrm { I A S } } = \mathrm { I l } _ { 2 , 1 8 }$ . As before, let $\rho _ { \mathrm { K 3 } }$ be an involution on $L _ { \mathrm { K 3 } }$ , the lattices $S , T = L _ { \mathrm { K 3 } } ^ { \pm }$ , and an isotropic vector $e \in T$ . We have $e _ { T } ^ { \perp } \subset e _ { L _ { \mathrm { K 3 } } } ^ { \perp }$ , where the perps are taken in $T$ , resp.
in $L _ { \mathrm { K 3 } }$ , and

$$
\overline { { T } } = e _ { T } ^ { \perp } / e \subset e _ { L _ { \mathrm { K } 3 } } ^ { \perp } / e \simeq \mathrm { I I } _ { 2 , 1 8 } = U ^ { 2 } \oplus E _ { 8 } ^ { 2 } .
$$

Let us denote the last lattice by $L _ { \mathrm { { I A S } } }$ . It comes with an induced involution $\rho _ { \mathrm { I A S } }$ and aSince need rthog and primi attices , the publattic $L _ { \mathrm { I A S } } ^ { \pm }$ , boion ly it $( - 1 )$ ce is . But $\overline { T }$ $S \subset e _ { L _ { \mathrm { K 3 } } } ^ { \perp }$ $e \not \in S$ $e _ { L _ { \mathrm { K 3 } } } ^ { \perp } \to L _ { \mathrm { I A S } }$ $S$ $L _ { \mathrm { I A S } } ^ { + }$ $S ^ { \mathrm { s a t } } = L _ { \mathrm { I A S } } ^ { + }$

In this sectof the lattices termine exactly which sublattices of . $L _ { \mathrm { I A S } } ^ { + }$ appear as images $S = L _ { \mathrm { K 3 } } ^ { + }$

Lemma 5.14. The inclusion $S  L _ { \mathrm { I A S } } ^ { + }$ identifies $S$ with $L _ { \mathrm { I A S } } ^ { + }$ for an odd $0$ -cusp, or an index 2 sublattice of $L _ { \mathrm { I A S } } ^ { + }$ that contains $( 1 + \rho _ { \mathrm { I A S } } ) L _ { \mathrm { I A S } } = 2 ( L _ { \mathrm { I A S } } ^ { + } ) ^ { * }$ for an even 0-cusp.

Proof.
The identity $( 1 + \rho _ { \mathrm { I A S } } ) L _ { \mathrm { I A S } } = 2 ( L _ { \mathrm { I A S } } ^ { + } ) ^ { * }$ follows because $L _ { \mathrm { { I A S } } }$ is unimodular.
Let Thu $\vert L _ { \mathrm { I A S } } ^ { + } / S \vert = n$ $| A _ { S } | : | A _ { L _ { \mathrm { I A S } } ^ { + } } | = n ^ { 2 }$ .e $| A _ { L _ { \mathrm { I A S } } ^ { + } } | = | A _ { L _ { \mathrm { I A S } } ^ { - } } | = | A _ { \overline { { T } } } |$ .. $n ^ { 2 } = | A _ { S } | : | A _ { \overline { { { T } } } } | = 2 ^ { a _ { s } } : 2 ^ { a _ { \overline { { { T } } } } }$ $\begin{array} { r } { a _ { S } = \ a _ { \overline { { T } } } } \end{array}$ $\begin{array} { r } { a _ { S } = a _ { \overline { { T } } } + 2 } \end{array}$ for an even cusp, it follows that $n = 1$ , resp.
$n = 2$ . 

Lemma 5.15. Let $K$ be an even 2-elementary lattice.
Then any index 2 sublattice $S \subset K$ that contains $2 K ^ { * }$ is 2-elementary.
Such sublattices are in a bijection with nonzero elements $x \in A _ { K ^ { \dagger } }$ . Moreover,

(1) If $\delta _ { K } = 1$ then there exists a unique $O ( q _ { K ^ { \dagger } } )$ -orbit of $x$ ’s.\
(2) If $\delta _ { K } = 0$ then there exist at most two $O ( q _ { K ^ { \dagger } } )$ -orbit of $x$ ’s: for $x$ with $q _ { K ^ { \dagger } } ( x ) \equiv 0$ (mod $2 \mathbb { Z }$ ) and $q _ { K ^ { \dagger } } ( x ) \equiv 1$ (mod $2 \mathbb { Z }$ ). In the first case one has $\delta _ { S } = 0$ and in the second case $\delta _ { S } = 1$ .

If $K$ is indefinite, then the $O ( q _ { K ^ { \dagger } } )$ -orbits are $O ( K )$ -orbits.

Proof.
Any index 2 subgroup of $K$ is of the form

$$
K _ { x } = \{ v \in K \mid v \cdot x \in \mathbb { Z } \} \quad { \mathrm { f o r ~ s o m e ~ } } x \in { \frac { 1 } { 2 } } K ^ { * }
$$

and the condition that $2 K ^ { * } \subset K _ { x }$ means that moreover $x \in ( 2 K ^ { * } ) ^ { * } = \textstyle { \frac { 1 } { 2 } } K \subset \textstyle { \frac { 1 } { 2 } } K ^ { * }$ For the dual lattices we have $K _ { x } ^ { * } = K ^ { * } + x$ .

The lattice $K _ { x }$ is 2-elementary $\iff 2 K _ { x } ^ { * } \subset K _ { x } \iff 2 K ^ { * } + 2 x \subset K _ { x }$ . Since $K$ is 2-elementary, we have $2 K ^ { * } \subset K$ . And $2 K ^ { \ast } \cdot x = K ^ { \ast } \cdot ( 2 x ) \in \mathbb { Z }$ , so $2 K ^ { * } \subset K _ { x }$ as well.
One has $2 x \in K$ , and $2 x \in K _ { x }$ iff $2 x \cdot x = ( 2 x ) ^ { 2 } / 2 \in \mathbb { Z }$ . This is true because $K$ is an even lattice.
This proves that the lattice $K _ { x }$ is indeed 2-elementary.

Two elements $x _ { 1 } , x _ { 2 } \in { \textstyle { \frac { 1 } { 2 } } } K$ define the same sublattice iff $x _ { 1 } - x _ { 2 } \in K ^ { * }$ . So the set of the distinct sublattices $K _ { x }$ is in a bijection with

$$
{ \textstyle \frac { 1 } { 2 } } K / K ^ { * } = K ( { \textstyle \frac { 1 } { 4 } } ) / K ^ { * } \simeq K ( { \textstyle \frac { 1 } { 2 } } ) / K ^ { * } ( 2 ) = A _ { K ^ { \dagger } } ,
$$

see Lemma 2.5. Since $K$ is even, $K ^ { \dagger }$ is co-even, so $q _ { K ^ { \dagger } } ( x ) \in \mathbb { Z }$ for any $x \in A _ { K ^ { \dagger } }$ .

If $\delta _ { K } = 1$ then $K ^ { \dagger }$ is odd and $q _ { K ^ { \dagger } }$ is well defined only mod $\mathbb { Z }$ , so $q _ { K ^ { \dagger } } ( x ) \equiv 0$ (mod $\mathbb { Z }$ ) for any $x \in A _ { K ^ { \dagger } }$ . If $\delta _ { K } = 0$ then $K ^ { \dagger }$ is even and $q _ { K ^ { \dagger } }$ is well defined mod $2 \mathbb { Z }$ , and $q _ { K ^ { \dagger } } ( x ) \equiv 0$ or $1$ (mod $\mathbb { Z }$ ). Then $\delta _ { K _ { x } } = 1$ iff $K _ { x } ^ { \dagger }$ is odd $\iff q _ { K ^ { \dagger } } ( x ) \equiv 1$ .

The statement about the $O ( q _ { K ^ { \dagger } } )$ -orbits follows by [Nik79a, 3.9.1]. We have ${ \cal O } ( q _ { K ^ { \dagger } } ) = { \cal O } ( q _ { K } )$ , and if $K$ is indefinite then $O ( K ) \to O ( q _ { K } )$ is surjective.


Theorem 5.16. Let $\rho _ { \mathrm { I A S } } \colon L _ { \mathrm { I A S } } \to L _ { \mathrm { I A S } }$ be an involution.
Then any sublattice $S \subset K$ of index 1 or 2 containing $2 K ^ { * }$ is 2-elementary, and the $O ( q _ { K ^ { \dagger } } )$ -orbits of such sublattices are in a bijection with the sources of mirror moves $S  T$ with $\overline { { T } } \simeq L _ { \mathrm { I A S } } ^ { - }$ . The lattice $L _ { \mathrm { I A S } } ^ { + }$ itself corresponds to the simple mirror of $\overline { T }$ and the sublattices of index 2 correspond to the even, non-simple mirror moves.

Proof.
We apply the previous lemma to $K = L _ { \mathrm { I A S } } ^ { + }$ and check that the index 2 sublattices corresponding to $0 \neq x \in A _ { K ^ { \dagger } }$ are indeed in a bijection with those that are allowed by Fig.

1. There are two special cases to consider:

(1) The lattices $S$ on the $r = a$ line, where according to Fig. 1 there should be no index 2 sublattices.
Indeed, in this case $S = L ( 2 )$ with a unimodular $L$ , so $S ^ { \dagger } = L$ and $A _ { S ^ { \dagger } } = 0$ has no nonzero elements.\
(2) $( 6 , 4 , 0 )$ where all the index 2 sublattices must be characteristic.
In this case $S = U ( 2 ) \oplus D _ { 4 }$ . So $\delta _ { S } = 0$ and $S ^ { \dagger } = U \oplus D _ { 4 }$ . Then the discriminant form is $q ( A _ { S ^ { \dagger } } ) = v$ and every nonzero element $x \in A _ { S ^ { \dagger } }$ satisfies $q ( x ) \equiv 1$ (mod $2 \mathbb { Z }$ ). So this is consistent with Fig.

As we noted at the end of Section 2B, all lattices in Fig. 1 can be written as direct sums of the standard ones.
Computing the doubled duals for them one checks that in the remaining, non special cases one has $A _ { S ^ { \dagger } } \neq 0$ , and if $\delta _ { S ^ { \dagger } } = 0$ then there are elements both with $q ( x ) \equiv 0$ (mod $2 \mathbb { Z }$ ) and $q ( x ) \equiv 1$ (mod $2 \mathbb { Z }$ ) corresponding to both even ordinary and even characteristic moves.
The answer given by Fig. 1 is the same in all of these cases.


# 6. Degenerations and integral affine spheres

The material of this section is well explained in [Eng18, EF21, AET19, AE21]. So we give a brief summary and fix notations.

6A. Kulikov models.
We discuss one parameter degenerations of K3 surfaces.\
[FS86] is a useful reference.

Definition 6.1. Let $X ^ { * } \to C ^ { * }$ be a family of smooth complex K3 surfaces over a punctured curve or disk $C ^ { * } = C \backslash 0$ . A Kulikov, or Kulikov-Persson-Pinkham, model is a proper extension $X  C$ such that $X  C$ is semistable, i.e. $X$ is nonsingular and the central fiber $X _ { 0 } = \cup V _ { i }$ is a reduced normal crossing union of divisors, and additionally, one has $K _ { X } \sim _ { C } 0$ . The central fiber $X _ { 0 }$ is called a Kulikov surface.

A Kulikov model exists after a finite base change $C ^ { \prime } \to C$ by [Kul77, PP81].

There are three types of Kulikov models, depending on the image of $0 \in C$ under the extended period morphism

$$
f \colon C \to { \overline { { \mathbb { D } / \Gamma } } } ^ { \mathrm { B B } }
$$

to the Baily-Borel compactification:

(I) $f ( 0 )$ lies in the interior $\mathbb { D } / \Gamma$ : $X _ { 0 }$ is smooth.

(II) $f ( 0 )$ lies in a 1-cusp.
The dual complex of $X _ { 0 }$ is an interval of length $n$ , $D _ { 0 , 1 } = \cdot \cdot \cdot = D _ { n - 1 , n } = E$ is the same elliptic curve, $V _ { 0 }$ and $V _ { n }$ are rational, and for $0 < i < n$ the surfaces $V _ { i }  E$ are generically ruled.
The double locus is an anticanonical divisor on each component $V _ { i }$ .\
(III) $f ( 0 )$ lies in a 0-cusp.
The dual complex $\Gamma ( X _ { 0 } )$ is a triangulation of the sphere $S ^ { 2 }$ . Each $( V _ { i } , D _ { i } )$ is an anticanonical pair, i.e. $K _ { V _ { i } } + D _ { i } \sim 0$ , where the part of the double locus $D _ { i }$ contained in $V _ { i }$ is a wheel of rational curves.

In Type III, all components $V _ { i }$ are necessarily rational.
The central fibers $X _ { 0 }$ of Kulikov models are called Type I, II, III Kulikov surfaces, respectively.
Denote $D _ { i j } = V _ { i } \cap V _ { j }$ so that $\begin{array} { r } { D _ { i } = \sum _ { j } D _ { i j } } \end{array}$ . Then the dual complex $\Gamma ( X _ { 0 } )$ of a Type III Kulikov surface consists of vertices $v _ { i }$ corresponding to components $V _ { i }$ , edges $e _ { i j }$ corresponding to double curves $D _ { i j }$ , and triangles $t _ { i j k }$ corresponding to triple points $T _ { i j k } = V _ { i } \cap V _ { j } \cap V _ { k }$ .

The Picard-Lefschetz transform $T \colon H ^ { 2 } ( X _ { t } , \mathbb { Z } ) \to H ^ { 2 } ( X _ { t } , \mathbb { Z } )$ takes the form $T =$ $\exp ( N )$ where

$$
N ( x ) = ( x \cdot \lambda ) e - ( x \cdot e ) \lambda
$$

for $e \in H ^ { 2 } ( X , \mathbb { Z } )$ primitive isotropic and $\lambda \in e ^ { \perp } / e$ a vector satisfying $\lambda ^ { 2 } = \mathrm { t h e }$ number of triple points of $X _ { 0 }$ . We call $\lambda$ the monodromy invariant.
When $\lambda ^ { 2 } > 0$ (so $X _ { 0 }$ is of Type III), $I = \mathbb { Z } e$ defines the 0-cusp $f ( 0 )$ , and when $\lambda ^ { 2 } = 0$ , $\lambda \neq 0$ (so $X _ { 0 }$ is of Type II), $J = ( \mathbb { Z } e \oplus \mathbb { Z } \lambda ) ^ { \mathrm { { s a t } } }$ defines the 1-cusp containing $f ( 0 )$ .

Two Kulikov models $X$ of the same degeneration $X ^ { * } \to C ^ { * }$ differ by a sequence of flops in curves $E \subset X _ { 0 }$ . The central fiber $X _ { 0 }$ is then changed by a sequence of elementary modifications of the following types:

(M0) $E \subset V _ { i }$ , $E \cap D _ { i } = \emptyset$ is an interior $\left( - 2 \right)$ -curve.
The flop is a nontrivial birational transformation $X \mathrm { ~ - ~ } \pmb { X } ^ { \prime }$ but $X _ { 0 } ^ { \prime } = X _ { 0 }$ are canonically identified.\
(M1) $E \subset V _ { i }$ , $E ^ { 2 } = - 1$ , $E \cap D _ { i } = p \in D _ { i j }$ is a smooth point of $D _ { i }$ . The flop contracts $E$ on $V _ { i }$ to $p$ and blows up $p \in V _ { j }$ to create a $( - 1 )$ -curve $E ^ { \prime } \subset V _ { j }$ .\
(M2) The flop contracts $E = D _ { i j }$ which is a $( - 1 )$ -curve on both $V _ { i }$ and $V _ { j }$ and inserts a curve $D _ { k l }$ between their neighbors $V _ { k } , V _ { l }$ .

Definition 6.2. Let ( $V , D = \sum D _ { j } ,$ ) be an anticanonical pair.
A corner blowup is a blowup $f \colon V ^ { \prime } \to V$ at a node of $D$ . The anticanonical divisor of $V ^ { \prime }$ is $D ^ { \prime } = f ^ { - 1 } ( D )$ .

An interior, or almost toric blowup $V ^ { \prime \prime }  V$ is a blowup at an interior point of a curve $D _ { j }$ , i.e. at a point $p \in D _ { j } \setminus \cup _ { k \neq j } D _ { k }$ . The anticanonical divisor $D ^ { \prime \prime } \subset V ^ { \prime \prime }$ is the strict preimage of $D$ .

Lemma 6.3 ([GHK15]). For any anticanonical pair $( V , D )$ there exists a diagram $V \left.
V ^ { \prime } \right.
\overline { { V } }$ , called $a$ toric model, such that $V ^ { \prime }  V$ is a sequence of corner blowups and $V ^ { \prime }  \overline { { V } }$ is a sequence of interior blowups.

We order the blowups and call $V \left.
V ^ { \prime } \right.
\overline { { V } }$ the ordered toric model of $V$ . We also fix the origin $1 \in ( \mathbb { C } ^ { * } ) ^ { 2 } \subset \overline { { V } }$ . This defines a choice of origin on every boundary curve $D _ { j }$ of $V$ .

Definition 6.4. The charge $Q ( V , D )$ of an anticanonical pair is the number of the interior blowups in a toric model.
Equivalently, one has

$$
Q ( V , D ) = { \left\{ \begin{array} { l l } { 1 2 + \sum ( - D _ { j } ^ { 2 } - 3 ) } & { { \mathrm { ~ i f ~ } } D { \mathrm { ~ i s ~ n o d a l ~ w i t h ~ } } \geq 2 { \mathrm { ~ c o m p o n e n t s , } } } \\ { 1 1 - D ^ { 2 } } & { { \mathrm { ~ i f ~ } } D { \mathrm { ~ i s ~ i r r e d u c i b l e ~ n o d a l . } } } \end{array} \right. }
$$

Type III surfaces are in a sense 24 steps away from being toric:

Theorem 6.5 (Friedman-Miranda [FM83]). For a Type III Kulikov surface, one has $\sum Q ( V _ { i } , D _ { i } ) = 2 4 $ .

Conversely, suppose we have a collection of anticanonical pairs $( V _ { i } , D _ { i } )$ and identifications $D _ { i j } \to D _ { j i }$ whose dual complex forms a 2-sphere, such that $D _ { i j } ^ { 2 } + D _ { j i } ^ { 2 } =$ $- 2$ . Then a $d$ -semistable (in the sense of Friedman [Fri83]) gluing gives a Type III surface which admits a smoothing to a K3 surface.
We refer to [AE21] for details.

If we fix the numerical type and the ordered toric models for each $( V _ { i } , D _ { i } )$ , then we can construct the standard Type III surface as follows: the interior blowups $V ^ { \prime }  \overline { { V } }$ are all done at the point $^ { - 1 }$ on each boundary component $D _ { i j } \simeq \mathbb { P } ^ { 1 }$ , with respect to the chosen origins.
Each identification $D _ { i j } \to D _ { j i }$ is chosen to be the unique isomorphism matching the origins and the triple points.
The standard surface is always $d$ -semistable.

All the other gluings are defined by varying the points of nontoric blowups and the differences between the origins in $D _ { i j }$ and $D _ { j i }$ , modulo the changes of the origins in each ${ \overline { { V } } } _ { i }$ . This defines a gluing complex [AE21, Def. 5.10]. The final result is that the $d$ -semistable Type III surfaces of a fixed numerical/combinatorial type are parameterized by the 19-dimensional torus $\mathrm { H o m } ( \Lambda , \mathbb { C } ^ { * } )$ , where $\Lambda \simeq \mathbb { Z } ^ { 1 9 }$ can be defined from the gluing complex or, equivalently, from the Picard complex:

$$
\widetilde { \Lambda } = \ker \left( \oplus _ { i } \operatorname { P i c } V _ { i } \to \oplus _ { i < j } \operatorname { P i c } D _ { i j } \right) , \quad \Lambda = \widetilde { \Lambda } / \Xi ,
$$

where $\Xi = \langle \xi _ { i } \rangle / ( \sum \xi _ { i } )$ and $\begin{array} { r } { \xi _ { i } = \sum _ { j } ( D _ { i j } - D _ { j i } ) \in \bigoplus _ { i } \operatorname { P i c } V _ { i } } \end{array}$ . For a given smoothing with a $0$ -cusp $e$ and monodromy vector $\lambda \in e ^ { \perp } / e$ one has $\Lambda = \lambda ^ { \perp }$ in $e ^ { \perp } / e \simeq \mathrm { I I } _ { 2 , 1 8 }$ . See [AE21], Sec.
5B and Prop.
3.29.

The lattice $\widetilde { \Lambda }$ is of numerical Cartier divisors, which are the numerical possibilities for the restrictions of a line bundle on $X _ { 0 }$ to $V _ { i }$ and $D _ { i j }$ . The elements $\xi _ { i }$ represent the line bundles $\mathcal { O } _ { X _ { 0 } } ( - V _ { i } )$ which are defined on any Kulikov model $X$ containing $X _ { 0 }$ as the central fiber.
The homomorphism

$$
\psi \colon \Lambda \to \mathbb { C } ^ { * } , \ \mathrm { r e s p . } \ E \quad \mathrm { f o r } \ X _ { 0 } \ \mathrm { o f } \ \mathrm { t y p e } \ \mathrm { I I I } , \ \mathrm { r e s p . } \ \mathrm { I I }
$$

is the period of $X _ { 0 }$ . For a Type II surface $X _ { 0 }$ , $E = \mathrm { P i c } ^ { 0 } D _ { i }$ is the elliptic curve for any of the isomorphic double curves $D _ { i }$ .

The Picard group of $X _ { 0 }$ is $\ker \tilde { \psi }$ , where $\widetilde { \psi }$ is the composition $\widetilde { \Lambda } \to \Lambda \stackrel { \psi } { \to } \mathbb { C } ^ { * }$ or $E$

Definition 6.6. The reduced Picard group is ${ \overline { { \operatorname { P i c } } } } ( X _ { 0 } ) = \ker \psi = \operatorname { P i c } ( X _ { 0 } ) / \Xi$ . If $X _ { 0 }$ is the central fiber of a smoothing, it is the quotient of $\mathrm { P i c } ( X _ { 0 } )$ by $\xi _ { i } = \mathcal { O } _ { X _ { 0 } } ( - V _ { i } )$ .

For a standard surface one has $\psi \equiv 1$ , so ${ \overline { { \operatorname { P i c } } } } ( X _ { 0 } ) = \Lambda$ .

6B. Nef, divisor, and stable models.

Definition 6.7. Let $L ^ { * }$ be a line bundle on $X ^ { * }$ , relatively nef and big over $C ^ { * }$ . A relatively nef extension $L$ to a Kulikov model $X  C$ is called a nef model.

Definition 6.8. Let $R ^ { * } \subset X ^ { * }$ be the vanishing locus of a section of $L ^ { * }$ as above, containing no vertical components.
A divisor model is an extension $R \subset X$ to a relatively nef divisor $R \in | L |$ for which $R _ { 0 }$ contains no strata of $X _ { 0 }$ .

Definition 6.9. The (KSBA-)stable model $( { \overline { { X } } } , \epsilon { \overline { { R } } } )$ is ProjC $\bigoplus _ { n \geq 0 } \pi _ { * } ( n R )$ for some divisor model $\pi \colon ( X , R ) \to ( C , 0 )$ . It is unique, depending only on the family $( \overline { { { X } } } ^ { * } , \overline { { { R } } } ^ { * } )  C ^ { * }$ , and stable under base change.
We call $\left( \overline { { X } } _ { 0 } , \epsilon \overline { { R } } _ { 0 } \right)$ the stable limit.

Definition 6.10. For an arbitrary, not necessarily nef effective divisor $R ^ { * }$ on $X ^ { * }$ , we say that a Kulikov model $X  C$ is compatible with a divisor if its closure $R$ does not contain any strata of the central fiber $X _ { 0 }$ .

If $X  C$ is a family with an involution $\iota$ and $R = X ^ { \iota }$ is the fixed locus then $( X , R )$ is usually not a nef model, since $R _ { t }$ contain $\left( - 2 \right)$ curves $\mathit { E } _ { i , t }$ . Only the part of $R$ which is the family $C _ { g }$ of curves of genus $g \geq 2$ may give a divisor or stable model.

6C. IAS $^ 2$ from Kulikov surfaces.
More details of the constructions in the following three sections, with pictures, are given in [Eng18, EF21, AET19].

For a Type III Kulikov surface $X _ { 0 } = \cup V _ { i }$ the dual graph is a triangulation of a sphere.
This is a very rough, partial description.
To describe the combinatorial type of $X _ { 0 }$ precisely, one has to specify the deformation types of each pair $( V _ { i } , D _ { i } )$ . There is an economical way to do so, using the language of integral affine structures $B$ on the complement of finitely many points in a sphere $S ^ { 2 }$ .

Definition 6.11. An integral affine structure on a real oriented surface $S$ is a collection of charts to open subsets of $\mathbb { R } ^ { 2 }$ , with transition functions in $\mathrm { S L } ( 2 , \mathbb { Z } ) \ltimes \mathbb { R } ^ { 2 }$ .

For a Type III Kulikov model, we endow $\Gamma ( X _ { 0 } ) \setminus \{ v _ { i } \ : | \ : Q ( V _ { i } , D _ { i } ) > 0 \}$ with an integral-affine structure as follows.
Each triangle is declared equivalent to a lattice triangle of the smallest possible lattice volume 1. Any two such are equivalent up to $\mathrm { S L _ { 2 } ( Z ) } \ltimes \mathbb { Z } ^ { 2 }$ . Cyclically order the directed edges $\vec { e } _ { i j }$ emanating from a vertex $v _ { i }$ so that $j$ is increasing by 1 on successively counterclockwise edges.
Then, to extend the integral-affine structure to the interiors of edges, we glue two lattice triangles together according to the formula

$$
\begin{array} { r } { \vec { e } _ { i , j - 1 } + \vec { e } _ { i , j + 1 } = d _ { i j } \vec { e } _ { i j } , \quad \mathrm { w h e r e ~ } d _ { i j } = \left\{ \begin{array} { l l } { - D _ { i j } ^ { 2 } } & { \mathrm { ~ i f ~ } D _ { i j } \mathrm { ~ i s ~ s m o o t h } , } \\ { - D _ { i j } ^ { 2 } + 2 } & { \mathrm { ~ i f ~ } D _ { i j } \mathrm { ~ i s ~ r a t i o n a l ~ n o d a l } . } \end{array} \right. } \end{array}
$$

Let $\operatorname { s t a r } ( v _ { i } )$ denote the union of the triangles containing $v _ { i }$ . The integral-affine structure on $\Gamma ( X _ { 0 } ) \backslash \{ v _ { i } \}$ extends to the vertices $v _ { i }$ for which $Q ( V _ { i } , D _ { i } ) = 0$ , i.e. when $( V _ { i } , D _ { i } )$ is toric.
By a well-known formula in toric geometry, $\operatorname { s t a r } ( v _ { i } )$ admits a chart to a polygon in $\mathbb { R } ^ { 2 }$ whose vertices are the endpoints of the primitive integral vectors in the fan of $( V _ { i } , D _ { i } )$ . Thus, in analogy with the toric case, we define (dropping the index $_ i$ for notational convenience):

Definition 6.12. The pseudofan of $( V , D )$ is the integral-affine surface $\operatorname { s t a r } ( v )$ constructed from gluing lattice triangles as above, one for each node of $D$ .

It is an integral-affine surface with boundary, PL isomorphic to the cone over the dual complex of $D$ with (up to) one singularity at the cone point.

An alternative description is in terms of a toric model $V \left.
V ^ { \prime } \right.
\overline { { V } }$ of in Definition 6.3. In the fan of $\overline { V }$ , let $\vec { e } _ { j }$ denote the primitive integral generators of the rays, in the counterclockwise order.
The morphism $V ^ { \prime }  \overline { { V } }$ is a sequence of interior blowups, say $n _ { j }$ times on the side $\overline { { D } } _ { j }$ . Then the pseudofan $\mathfrak { F } ( V ^ { \prime } , D ^ { \prime } )$ is obtained from $\mathfrak { F } ( \overline { { V } } , \overline { { D } } )$ by regluing along each edge $\vec { e } _ { j }$ with a shearing transformation $I _ { n _ { j } } ( \vec { e } _ { j } ) = I ( \vec { e } _ { j } ) ^ { n _ { j } }$ , see [Eng18, Prop. 3.13]. Here,

$$
I ( \vec { e } _ { j } ) \sim \binom { 1 } { 0 } 1 \biggr )
$$

is the unique linear transformation in $\operatorname { S L _ { 2 } } ( \mathbb { Z } )$ conjugate to a unit shear which has $\vec { e } _ { j }$ as an eigenvector.
The pairs $( V , D )$ and $( V ^ { \prime } , D ^ { \prime } )$ differ by corner blowups and the neighborhoods of the origins in ${ \mathfrak { F } } ( V , D )$ and $\mathfrak { F } ( V ^ { \prime } , D ^ { \prime } )$ are isomorphic.
Only the polyhedral subdivision changes.
So they define the same integral-affine singularity.

Definition 6.13. Two pseudofans belong to the same corner blowup equivalence class (cbec) if they correspond to different toric models of the same anticanonical pair, possibly after some corner blowups and topologically trivial deformations.

Definition 6.14. An IAS $^ 2$ is an integral-affine structure on $S ^ { 2 } \setminus \{ p _ { 1 } , \ldots , p _ { k } \}$ , together with the data of a cbec for which ${ \mathfrak { F } } ( V , D )$ models a neighborhood of $p _ { i }$ .

Construction 6.15. Each $d$ -semistable Type III surface $X _ { 0 } = \cup V _ { i }$ defines a triangulated (by unit lattice triangles) IAS $^ 2$ $( B , \tau )$ as follows: $B = \cup _ { i } \mathfrak { F } ( V _ { i } , D _ { i } )$ , and $\tau$ is the dual complex $\Gamma ( X _ { 0 } )$ . By [Eng18, Prop. 2.2], the consistency of the integralaffine structure on the union of adjacent pseudofans is equivalent to the triple point formula $D _ { i j } ^ { 2 } + D _ { j i } ^ { 2 } = - 2$ which holds on any Kulikov surface.

Vice versa, from any triangulated IAS $^ 2$ , one can construct a Type III surface by interpreting the star of each vertex as an anticanonical pair $( V _ { i } , D _ { i } )$ and gluing them along identifications $D _ { i j } \to D _ { j i }$ . As explained in Section 6A, this way one obtains a family of type III surfaces parameterized by the torus $\operatorname { H o m } ( \Lambda , \mathbb { C } ^ { * } ) \simeq ( \mathbb { C } ^ { * } ) ^ { 1 9 }$ .

By Theorem 6.5, the sum of charges of singularities in 24. An IAS $^ 2$ is called generic if there are 24 distinct $I _ { 1 }$ singularities.

6D. IAS $^ 2$ from symplectic geometry.
A second source of integral-affine structures is symplectic geometry.
Let $( \widehat { X } , \omega ) \to B$ be a smooth symplectic 4-manifold with a Lagrangian torus fibration such that the singular fibers are necklaces of spheres.
Then it defines a natural integral-affine structure on the base minus finitely many points and with the $I _ { n }$ singularity $b \in B$ at a point where the fiber $\widehat { X } _ { b }$ is a necklace of $n$ spheres.
Vice versa, any integral affine structure $B$ on a sphere of total charge 24 with only $I _ { n }$ singularities defines a unique symplectic manifold $( \widehat { X } , \omega ) \to B$ with $\widehat { X }$ diffeomorphic to a K3 surface.
See [EF21], [AET19, Sec. 8E] for more details.

The easiest examples of integral-affine structures coming from symplectic geometry are those from the following construction due to Symington [Sym03]:

Construction 6.16. Let $( \hat { V } , \hat { D } )$ be an anticanonical pair with a toric model

$$
\widehat { V } \stackrel { f } { \longleftarrow } \widehat { V } ^ { \prime } \stackrel { g } { \longrightarrow } \overline { { \widehat { V } } } .
$$

Choose a big and nef line bundle $L$ on $\hat { V }$ and let $L ^ { \prime } = f ^ { * } L$ and $\overline { { L } } = g _ { * } L ^ { \prime }$ ; they are big and nef as well.
The line bundle $\overline { { L } }$ defines the moment map

$$
\bar { \mu } \colon \overline { { \widehat { V } } }  \overline { { P } }
$$

to the moment polytope.
It is a Lagrangian torus fibration, with circle and point fibers over the edges and vertices of $\overline { { P } }$ , respectively.

Suppose that $g \colon \widehat { V } ^ { \prime } \to \widehat { V }$ contains $n$ internal blowups on the side $\overline { { D } } _ { j }$ and that $L ^ { \prime } = g ^ { * } ( L ) - \sum a _ { j k } E _ { j k }$ , where $E _ { j k }$ are the exceptional divisors.
Then, as described in [Sym03], one can define a Symington polytope $P$ , obtained from $\overline { { P } }$ by cutting $n _ { j }$ triangles $t _ { j k }$ of sizes $a _ { j k } = L ^ { \prime } { \cdot } E _ { j k }$ resting on the edge of $\overline { { P } }$ over which $\overline { { D } } _ { j }$ fibers, and then gluing the remaining two edges by a unit shear.
The resulting integral affine structure has $n _ { j } \ J _ { 1 }$ singularities of integral-affine structure at interior points, with monodromy-invariant direction parallel to the edge on which the triangles rested.

Assuming all the introduced singularities are distinct, there is a fibration

$$
\mu ^ { \prime } \colon  { \widehat { V } } ^ { \prime } \to V
$$

whose fiber over an $I _ { 1 }$ singularity is an irreducible nodal sphere.
It then descends to a Lagrangian torus fibration

$$
\mu \colon ( \widehat { V } , \omega ) \to P
$$

because $L ^ { \prime } \cdot \widehat { D } _ { j } ^ { \prime } = 0$ for the components of ${ \widehat { D } } ^ { \prime }$ introduced by the corner blow-ups $f$

This construction is only possible if there exists a toric model for which the triangles can be fit into $\overline { { P } }$ without intersections.
By [EF21, Thm. 5.3] such a toric model always exists because $L$ is big and nef.

An important generalization of this construction is to the case of an anticanonical pair $( \hat { V } , \hat { D } )$ with a smooth boundary and a big and nef line bundle $L$ on it.
If $( \hat { V } , \hat { D } )$ is a deformation of a Looijenga pair $( \hat { V } , \hat { D } ^ { \prime } )$ with a singular boundary ${ \widehat { D } } ^ { \prime }$ , one can define a Symington polytope $P$ by a node smoothing surgery from a Symington polytope $P ^ { \prime }$ of $( \hat { V } , \hat { D } ^ { \prime } )$ and a Lagrangian torus fibration $\mu \colon { \widehat { V } } \to P$ .

For K3 surfaces, the basic example of IAS $^ 2$ from symplectic geometry comes from the following construction:

Proposition 6.17. Let $( \widehat { X } , L ) \to ( C , 0 )$ be a nef model with a central fiber $\hat { X } _ { 0 } =$ $\cup V _ { i }$ and $L | _ { \widehat { V _ { i } } }$ big.
Then there is a Lagrangian torus fibration

$$
\mu \colon ( \widehat { X } _ { t } , \omega _ { t } )  B = \cup _ { i } P _ { i }
$$

from a smooth fiber $\widehat { X } _ { t }$ for which $[ { \omega } _ { t } ] = L$ , defined as a composition of two maps:

(1) the Clemens collapse $c _ { t } \colon { \widehat { X } } _ { t } \to { \widehat { X } } _ { 0 }$ and\
(2) the union of moment maps $\mu _ { i } \colon \widehat { V } _ { i } \to P _ { i }$ from Construction 6.16, associated to the big and nef line bundle $L _ { i }$ .

Proof.
The Lagrangian torus fibrations $\mu _ { i }$ undergo symplectic boundary reduction, collapsing to circles over the edges of $P _ { i }$ and to points over vertices of $P _ { i }$ . The Clemens collapse $c _ { t } \colon { \widehat { X } } _ { t } \to { \widehat { X } } _ { 0 }$ is the restriction of a retraction of $\widehat { X } \to \widehat { X } _ { 0 }$ . The fibers of $c _ { t }$ over the double locus are circles, and the fibers over the triple points are 2-tori.
Thus, the composition $( \mu _ { i } ) \circ c _ { t }$ has 2-torus fibers, even over the edges and vertices of $P _ { i }$ .

The general fiber $\widehat { X } _ { t }$ can be constructed as a fiber connect-sum of Lagrangian torus fibrations over $P _ { i }$ which undergo no boundary reduction.
Since we additionally have ${ \cal L } \cdot \widehat { D } _ { i j } = { \cal L } \cdot \widehat { D } _ { j i }$ , this fiber connect-sum can be performed as a symplectic fiber connect-sum of Lagrangian torus fibrations, by slightly enlarging the bases of the Lagrangian torus fibrations, and then gluing over the neighborhood of a glued edge $P _ { i } \cap P _ { j }$ .

Thus $\widehat { X } _ { t }$ is endowed with a symplectic form $\omega _ { t }$ for which the composition $( \mu _ { i } ) \circ c _ { t }$ is a Lagrangian torus fibration over $S ^ { 2 }$ with $I _ { 1 }$ singular fibers over the singular points of the Symington polytopes $P _ { i }$ . The arguments in [EF21, Prop. 3.14], [AET19, Thm. 2.43] show that $[ \omega _ { t } ] = c _ { 1 } ( L ) \in \hat { e } ^ { \perp } / \hat { e }$ , where $\hat { e } \in H ^ { 2 } ( \widehat { X } , \mathbb { Z } )$ denotes the Lagrangian fiber class of $\mu$ . 

6E. Nodal slides and scaling IAS2. A nodal slide on an IAS $^ 2$ $B$ is an operation $B \  \ B ^ { \prime }$ which moves some $I _ { n }$ singularity by a specified lattice length, in the direction of its monodromy ray.
The integral-affine structure the same on the complement of the segment along which the singularity moves, and is only modified along the segment.
It has an interpretation both on the algebraic side for the dual complex $B = \Gamma ( X _ { 0 } )$ , and on the symplectic side for the base $\widehat X  B$ .

The symplectic 4-manifolds $( \widehat { X } , \omega ) \to B$ and $( \widehat { X } ^ { \prime } , \omega ^ { \prime } )$ are symplectomorphic with only the Lagrangian fibration deforming.
On the algebraic side a unit length nodal slide $B \ {  } \ B ^ { \prime }$ corresponds to applying an M1 modification $X _ { 0 } \ \mathrm { ~ -- \to ~ } X _ { 0 } ^ { \prime }$ . It moves the location of the singularity by a length 1 nodal slide, in the direction of the monodromy ray corresponding to the exceptional curve $E$ which was flopped.

The scaling operation on $B$ corresponds to post-composing the charts with multiplication by $n > 0$ . The area of $B$ is multiplied by $n ^ { 2 }$ .

On the symplectic side, it corresponds to replacing $\omega \mapsto n \omega$ or $L \mapsto n L$ , while leaving the Lagrangian torus fibration the same.
On the algebraic side, it corresponds to a ramified base change $( C ^ { \prime } , 0 )  ( C , 0 )$ of degree $n$ , and resolving $X \times _ { C } C ^ { \prime }$ in a standard way to a Kulikov model.
Each triangle in the triangulation $\tau$ is replaced by the standard subdivision into $n ^ { 2 }$ triangles.

A node smoothing, called a nodal trade in [Sym03, Sec. 6], trades a corner of the Symington polytope $P$ for a singularity inside $P$ , smoothing the corner.
It occurs when a nodal slide hits a wall of $P$ .

Remark 6.18. By nodal slides, any integral affine structure with a given decomposition of singularities into $\prod I ( \vec { e } _ { j } ) ^ { n _ { j } }$ can be replaced by an affine structure with only $I _ { n }$ singularities or, by further nodal slides with 24 distinct $I _ { 1 }$ singularities.
On the algebraic side, in our Definition 6.14, each singularity comes with a decomposition $\prod I ( \vec { e } _ { j } ) ^ { n _ { j } }$ . So after a base change any Kulikov model can be replaced, after a sequence of M2 modifications (retriangulation) and M1 modifications (nodal slides), with a generic Kulikov model with exactly 24 non-toric components $V _ { i }$ defining 24 distinct $I _ { 1 }$ singularities of an IAS2.

6F. The Mirror Theorem.
A key to our ability to understand Kulikov models is the mirror symmetry between algebraic geometry of degenerations (the A-model) and symplectic geometry (B-model) which is well-studied in the literature.
For example, it appears in [GS03, KS06]. We use it in the following form:

Theorem 6.19 ([EF21], Prop.
3.14). Let $B$ be a generic IAS $^ 2$ and let (1) $X \to ( C , 0 )$ be a type III Kulikov model for which $\Gamma ( X _ { 0 } ) = B$ . (2) $\mu \colon ( \widehat { X } , \omega )  B$ be a Lagrangian torus fibration defining the same $B$

Then there exists a diffeomorphism $\phi \colon { \widehat { X } }  X _ { t }$ to a nearby fiber $t \neq 0$ such that

(a) $\phi _ { * } \hat { e } = e$ , where $\hat { e }$ is a fiber of $\mu$ and $e \in T _ { X _ { t } }$ the isotropic vanishing cycle.\
(b) $\phi _ { * } [ \omega ] = \lambda$ , where $\lambda \in e ^ { \perp } / e$ is the monodromy invariant.

This theorem reduced study of Kulikov models with a monodromy invariant $\lambda$ to that of a mirror, symplectic K3 surface $\widehat { X }$ and a symplectic form on it.
If $\widehat { X }$ is algebraic, then we can use a nef line bundle $L$ instead of the form $\omega$ . One deals with the non-generic $\mathrm { I A S ^ { 2 } }$ by Remark 6.18.

6G. Visible curves on IAS2. In this paper we use visible curves mostly for motivation, so we only give a brief sketch.
See more details in [AET19].

Let $B$ be a generic $\mathrm { I A S ^ { 2 } }$ . The integral tangent sheaf $T _ { B , \mathbb { Z } }$ is a constructible sheaf whose fiber is $\mathbb { Z } ^ { 2 }$ at a smooth point and $\mathbb { Z }$ at an $I _ { 1 }$ singularity.
The Leray spectral sequence for $\mu \colon { \widehat { X } }  B$ and the sheaf $\mathbb { Z } _ { \widehat { X } }$ shows that $H ^ { 1 } ( B , T _ { B , \mathbb { Z } } ^ { * } )$ has a natural bilinear product and is isomorphic to $\hat { e } ^ { \perp } / \hat { e } \simeq L _ { \mathrm { I A S } } = \mathrm { I I } _ { 2 , 1 8 }$ . By a Poincar´e duality, $H ^ { 1 } ( B , T _ { B , \mathbb { Z } } ^ { * } )$ can be identified with $H _ { 1 } ( B , T _ { B , \mathbb { Z } } )$ . The elements of the latter group are cycles $\sum ( \gamma _ { i } , v _ { i } )$ valued in the integral tangent bundle $T _ { B , \mathbb { Z } }$ which satisfy balancing conditions at the boundaries of the 1-chains $\gamma _ { i }$ from the cycle.
These are called visible curves, see [AET19, Con. 2.39].

Let $p _ { 1 } , p _ { 2 }$ be two $I _ { 1 }$ singularities connected by a path.
Let $v _ { 1 } , v _ { 2 }$ be the monodromy directions at these points and suppose that there is a path $\gamma$ from $p _ { 1 }$ to $p _ { 2 }$ with a constant vector field $\boldsymbol { v }$ along it which at the ends equals $v _ { 1 }$ and $v _ { 2 }$ . Then $( \gamma , v )$ is a visible curve.
Its square is $\left( - 2 \right)$ , and if there are three such $I _ { 1 }$ singularities with the same monodromy rays then $( \gamma ( p _ { 1 } , p _ { 2 } ) , v ) \cdot ( \gamma ( p _ { 2 } , p _ { 3 } ) , v ) = 1$ . Frequently, for a collection of several $I _ { 1 }$ singularities with some monodromy rays in common one can form a collection of visible curves whose intersection matrix is an $A D E$ matrix, giving the dual $A D E$ graph.
We give an example of this in Section 8G.

7. Mirror symmetry for K3 surfaces with a nonsymplectic involution

The Mirror Theorem 6.19 establishes a dictionary between algebraic geometry of degenerations of surfaces in the $S$ -family and symplectic geometry of surfaces in the $\widehat S$ -family, where $\widehat S = \overline { T } = e ^ { \perp } / e$ . One special feature of the present case is that the lattice $\widehat { S }$ is again 2-elementary, so we can exploit algebraic geometry of degenerations of surfaces in the $\widehat { S }$ -family as well.
We do it in this section.

We begin with a hyperbolic lattice $S$ from Fig. 1 and the period domain $\mathbb { D } _ { S }$ as in Section 2C parameterizing K3 surfaces with involution whose generic Picard lattice is $S$ and generic transcendental lattice is $T$ . As in Section 5C, let $e \in T$ , $e ^ { 2 } = 0$ be a 0-cusp of $\mathbb { D } _ { S }$ and $\overline { { T } } = e ^ { \perp } / e$ the hyperbolic lattice corresponding to it.

On the mirror side, we now consider the family of K3 surfaces with involution whose generic Picard lattice is ${ \widehat { S } } = { \overline { { T } } }$ . Note that by Remark 5.7 not every node of Fig. 1 can appear as $T$ . If $( \widehat { X } , \widehat { \iota } )$ is one of these surfaces then we get the quotient surface $\widehat { Y } = \widehat { X } / \widehat { \iota }$ , which is a rational surface for $\widehat { S } \neq ( 1 0 , 1 0 , 0 )$ and an Enriques surface for $\widehat { \cal S } = ( 1 0 , 1 0 , 0 )$ .

7A. A special degeneration.
In this subsection we restrict ourselves to the elliptic surfaces of Section 4B, which we denote by $\widehat { X }$ since this is the mirror side.

Lemma 7.1. In each of the cases (1,2,3) of Theorem 4.1, there exists a oneparameter degeneration ${ \widehat { X } } \  \ ( C , 0 )$ with the central fiber $\widehat { X } _ { 0 } \ = \ \widehat { Y } \cup _ { D } \widehat { Y }$ . The 3-fold $\widehat { X }$ can be chosen to be a smooth Kulikov degeneration in the cases (2,3); it is singular in the case (1).

In the Enriques case (4) there exists such a degeneration with smooth $\widehat { X }$ and the central fiber ${ \widehat { X } } _ { 0 } = { \widehat { Y } } \cup _ { D } { \widehat { Y } }$ such that $\hat { Y }$ is the surface from the Halphen case (3) but the involution on $\widehat { X } _ { 0 }$ is base-point-free.

Proof.
$\left( I _ { 2 k } I _ { 0 } \right)$ . This Type III degeneration is achieved by a family in which the branch divisor $G _ { 0 }$ on $\widehat { Y } _ { 0 }$ collides with the special fiber $G$ . One has $G _ { 0 } + G \sim 2 D$ .

In local coordinates $( x , y , s )$ on $\hat { Y }$ and $s$ on $\mathbb { P } ^ { 1 }$ the fibration $f ^ { \prime } \colon  { \widehat { Y } } \to  { \mathbb { P } } ^ { 1 }$ can be written as $x y ^ { 2 } = s$ , a $( - 4 )$ branch curve $E _ { i }$ is $x = 0$ and the fiber $F _ { 0 }$ is $x y = t$ . Then the double cover is locally given by the equation $z ^ { 2 } = x ( x y - t )$ .

$\left( I _ { 0 } ^ { 2 } \right)$ . Collide $F$ and $F _ { 0 }$ . In local coordinates $\widehat { Y } \to \mathbb { P } ^ { 1 }$ is $( x , y ) \to s = x$ , the branch divisor is $s ^ { 2 } = t$ and $\widehat { X }$ is $z ^ { 2 } = x ^ { 2 } - t$ . Since $F \sim F _ { 0 }$ , the branch divisor $F + F _ { 0 }$ is a pullback of 2 points on $\mathbb { P } ^ { 1 }$ , so this is just $\hat { Y } \times _ { \mathbb { P } ^ { 1 } } S$ , where $S \to \mathbb { P } ^ { 1 } \times C$ is the family of double covers of $\mathbb { P } ^ { 1 }$ .

(Halphen).
Degenerate the branch locus into the multiple fiber $G = 2 D$ . Locally $\widehat { Y }  \mathbb { P } ^ { 1 }$ is $( x , y ) \to s = x ^ { 2 }$ and the branch divisor is $s \mathit { \Theta } = \mathit { t }$ . Thus, $\widehat { X }$ locally is $z ^ { 2 } = x ^ { 2 } - t$ . The fiber $G = 2 D \sim - 2 K _ { \widehat { Y } }$ is divisible by 2 in $\operatorname { P i c } \widehat { Y }$ , so the construction works globally.

(Enriques).
We construct this degeneration “by hand,” by smoothing a central fiber to an Enriques K3 surface.
Let $\widehat { Y } \ \to \ \mathbb { P } ^ { 1 }$ be an index 2 Halphen pencil.
Consider the surface

$$
\widehat { X } _ { 0 } ^ { \prime } = \widehat { Y } \cup _ { D } \widehat { Y }
$$

from the Halphen case with multiple fiber $G = 2 D$ , $D \sim - K _ { \widehat { Y } }$ . It is two copies of $\widehat { Y }$ glued by the identity map along the elliptic curve $D$ b, and the involution $\iota$ exchanges the two copies of $\widehat { Y }$ and fixes $D$ pointwise.

Let $E = \mathrm { P i c } ^ { 0 } ( D )$ . This is an elliptic curve and $D$ is a torsor over $E$ . Then ${ \mathcal { F } } : = { \mathcal { O } } _ { \widehat { Y } } ( D ) | _ { D } = a \in E [ 2 ]$ is nontrivial 2-torsion because the pencil is Halphen.
Now build a new surface ${ \widehat { X } } _ { 0 } = { \widehat { Y } } \cup _ { D } { \widehat { Y } }$ in which the two copies of $\hat { Y }$ are glued with a twist, a translation of $D$ by the element $a \in E$ [2]. There is still an involution which exchanges the $\widehat { Y }$ s, but it now acts as translation by $a$ on $D$ and thus is fixed point free on $\widehat { X } _ { 0 }$ .

Since $T _ { a } ^ { * } { \mathcal { F } } \simeq { \mathcal { F } }$ and ${ \mathcal { F } } ^ { \otimes 2 } \simeq { \mathcal { O } } _ { D }$ , $\widehat { X } _ { 0 }$ is $d$ -semistable.
We will pick a generic smoothing of $\widehat { X } _ { 0 }$ preserving the (+1)-eigenspace of the reduced Picard group of $\widehat { X } _ { 0 }$ modulo of the components of $\widehat { X } _ { 0 }$ defined in 6.6. The lattice of numerical Cartier divisors is

$$
\widetilde { \Lambda } = \ker \big ( H ^ { 2 } ( \widehat { Y } ) \oplus H ^ { 2 } ( \widehat { Y } ) \to H ^ { 2 } ( D ) \big ) ,
$$

$\Xi = \mathbb { Z } \xi$ , where ${ \boldsymbol { \xi } } = ( D , - D )$ , and $\Lambda = { \widetilde \Lambda } / { \Xi }$ is the reduced lattice of numerical Cartier divisors.
The surface $\hat { Y }$ is a blowup of 9 points lying on a cubic, so $\mathrm { P i c } \hat { Y } $ $\mathrm { P i c } D$ can be identified with the homomorphism

$$
I _ { 1 , 9 } \to \mathbb { Z } , \ L \mapsto L \cdot D , \quad { \mathrm { w h e r e } } \ D = ( - 3 , 1 , \dots , 1 ) = - 3 e _ { 0 } + \sum _ { i = 1 } ^ { 9 } e _ { i } .
$$

Choose $\hat { Y }$ to be the $( 1 0 , 1 0 , 1 )$ surface from Table 1. If $e _ { 9 }$ is the last blowup of $\hat { Y } \to { \mathbb P } ^ { 2 }$ then in $\langle e _ { 9 } , D \rangle ^ { \perp }$ in $H ^ { 2 } ( { \widehat { Y } } )$ is the $E _ { 8 }$ lattice with a basis given by 8 of the 9 components of the $I I ^ { * }$ fiber.

Denote by $d$ and $v$ the vectors $( D , 0 )$ and $( e _ { 9 } , e _ { 9 } )$ . One has $v ^ { 2 } = - 2$ , $d ^ { 2 } = 0$ and $v \cdot d = 1$ . Then $\boldsymbol { v }$ and $d$ span a copy of $U$ , and

$$
\Lambda ^ { + } = \mathrm { d i a g } E _ { 8 } \oplus \langle v , d \rangle = E _ { 8 } ( 2 ) \oplus U .
$$

Let $\psi \colon \Lambda \to E$ be the period of $\widehat { X } _ { 0 }$ as in Eq. (5), and $\psi ^ { + }$ be its restriction to $\Lambda ^ { + }$ . We have ${ \overline { { \operatorname { P i c } } } } { \widehat { X } } _ { 0 } = \ker \psi$ and $( \overline { { \mathrm { P i c } } } \ : \widehat { X } _ { 0 } ) ^ { + } = \ker \psi ^ { + }$ . For our surface, $\psi ( E _ { 8 } ( 2 ) ) = 1$

(since the $I I ^ { * }$ fiber is disjoint from $D$ ), $\psi ( v ) = a$ and $\psi ( d ) = { \mathcal { F } }$ . Thus, when $a = \mathcal { F } \in E [ 2 ]$ , we have

$$
\ker ( U  E ) = \langle v + d , 2 d \rangle \simeq U ( 2 ) , \quad ( \overline { { \mathrm { P i c } } } \ \widehat { X } _ { 0 } ) ^ { + } \simeq E _ { 8 } ( 2 ) \oplus U ( 2 ) = ( 1 0 , 1 0 , 0 ) .
$$

So a generic smoothing of $\widehat { X } _ { 0 }$ preserving $( \overline { { \mathrm { P i c } } } \hat { X } _ { 0 } ) ^ { + }$ is a family of K3 surfaces with generic Picard lattice $( 1 0 , 1 0 , 0 )$ , i.e. a family of Enriques K3 surfaces.
It comes with Enriques involution reducing to the involution on $\widehat { X } _ { 0 }$ . 

Remark 7.2. The last construction builds a degeneration of Enriques surfaces to a nonnormal surface obtained by gluing an index 2 Halphen pencil to itself along the double fiber $2 D$ by translating $D$ by $a = \mathcal { O } _ { D } ( D ) \in ( \mathrm { P i c } ^ { 0 } D )$ [2]. This is an interesting degeneration which we have not seen in the literature.

Remark 7.3. There are two more ways to produce a $d$ -semistable Type $\amalg$ surface ${ \widehat { X } } _ { 0 } = V \cup _ { D } V$ with a base-point-free involution: We can glue two Halphen pencils by a nontrivial 2-torsion $a \neq \mathcal { O } _ { D } ( D )$ . We can also glue by 2-torsion two copies of a rational elliptic surface with a section.
In the first case $\ker ( U  E ) = 2 U \simeq U ( 4 )$ . In the second case $\ker ( U  E ) = \langle 2 v , d \rangle$ . Both of these are not 2-elementary lattices, so the base-point-free involution on $\widehat { X } _ { 0 }$ can not be extended to a smoothing.

# 7B.

Lagrangian torus fibration for the mirror $\mathbf { K 3 }$ surfaces.

Theorem 7.4. Let $\widehat { S } = ( r , a , \delta ) = ( 1 0 + k - ( g - 1 ) , 1 0 - k - ( g - 1 ) , \delta )$ be a lattice appearing as a target of one of the mirror moves $S  \overline { { T } } = \widehat { S }$ of Definition 5.6, $\widehat { X } _ { t }$ a surface with $\widehat { S } = ( \operatorname { P i c } \widehat { X } _ { t } ) ^ { + }$ , and $L \in { \widehat { S } } \otimes \mathbb { Q }$ an ample $\mathbb { Q }$ -line bundle on $\widehat { X } _ { t }$ . Then there exists an involution-equivariant Lagrangian torus fibration $\mu \colon ( \widehat { X } _ { t } , \omega )  B$ with $\omega = [ L ]$ , where $B = P \cup P ^ { \mathrm { o p p } }$ is a union of two Symington polytopes for the pairs $( \hat { Y } , D )$ of Lemma 7.1, glued along their common boundary $\partial P = \partial P ^ { \mathrm { o p p } }$ , to form an equator of the sphere.

If $\widehat { S } \neq ( 1 0 , 1 0 , 0 )$ then $\partial P$ and $\partial P ^ { \mathrm { o p p } }$ are glued by the identity map, and if $\widehat { S } = ( 1 0 , 1 0 , 0 )$ , then $B = P \cup _ { \mathrm { t w i s t } } P ^ { \mathrm { o p p } }$ results from gluing the Symington polytope by a half-twist along its equator, so that $B / \iota \simeq \mathbb { R P } ^ { 2 }$ .

If $\widehat { S } \neq ( 1 0 , 8 , 0 )$ then the fibration can be chosen so that $B$ has $2 k \ I _ { 1 }$ singularities on the equator at the vertices of $P$ , with the monodromy rays transverse to the equator, an $I _ { 2 ( g - 1 ) }$ singularity with the monodromy ray parallel to the equator, and $1 2 - k - ( g - 1 )$ total $I _ { 1 }$ singularities in each of the hemispheres.
For $\widehat { S } = ( 1 0 , 8 , 0 )$ , there are 12 $I _ { 1 }$ singularities in each of the hemispheres.

In particular, there no singularities on the equator when $\widehat { S } = ( 1 0 , 1 0 , 0 )$ , $( 1 0 , 1 0 , 1 )$ $( 1 0 , 8 , 0 )$ , and the equator is an embedded integral-affine circle.

Proof.
The base case.
We begin with the base case when $\widehat { S }$ is a lattice in Section 4B. The map $\mu$ is given by Construction 6.17 for the special degeneration of Section 7A. In the $I _ { 0 } ^ { 2 }$ , Halphen, and Enriques cases the degeneration of Lemma 7.1 is already Kulikov and immediately gives the required Lagrangian torus fibration $\mu$ . It is, notably, a Type II degeneration.

We now consider the $I _ { 2 k } I _ { 0 }$ case.
In local coordinates the family ${ \widehat { X } } \to ( C , 0 )$ is

$$
\widehat { X } = \{ z ^ { 2 } = x ( x y ^ { 2 } - t ) \} \subset \mathbb { A } _ { x , y , z , t } ^ { 4 } \quad \mathrm { o r } \quad ( z + x y ) ( z - x y ) = t x .
$$

This 3-fold is singular along the line $\ell = \{ x = z = 0 \}$ . The central fiber $\widehat { X } _ { 0 }$ is a union of two A2s glued along $x y = 0$ . Let $\tilde { X }$ be the blowup of $\widehat { X }$ along $\ell$ . It is covered by two charts:

Chart 1 $z = x z _ { 1 }$ , $( z _ { 1 } + y ) ( z _ { 1 } - y ) x = t$ . This is a smooth 3-fold and the central fiber is a normal crossing divisor with a single triple point.

Chart 2 $x = z x _ { 1 }$ , $z ( 1 + x _ { 1 } y ) ( 1 - x _ { 1 } y ) = t x _ { 1 }$ . If $g$ is the difference of the two sides, then = −x1, ∂g∂z $\begin{array} { r } { \frac { \partial g } { \partial z } = ( 1 + x _ { 1 } y ) ( 1 - x _ { 1 } y ) } \end{array}$ which have no common zeros.
Thus, this 3-fold is smooth as well.
The central fiber consists of three irreducible components, two of which do not intersect: $1 + x _ { 1 } y = 0$ and $1 - x _ { 1 } y = 0$ .

We conclude that $\tilde { X }$ is a Kulikov model of ${ \hat { X } } \to C$ . Globally, the blowup ${ \widetilde { X } } \to { \widehat { X } }$ has $n$ exceptional divisors $Z _ { i }$ , one for each $( - 4 )$ curve $E _ { i }$ in the special fiber $F$ of $\widehat { Y }$ . Each $Z _ { i }$ is an anticanonical pair with two boundary divisors $D _ { 1 }$ , $D _ { 2 }$ , $D _ { 1 } \cdot D _ { 2 } = 2$ and $D _ { i } ^ { 2 } = 2$ . The surface $Z _ { i }$ is geometrically ruled and $D _ { 1 } , D _ { 2 }$ are sections.
It follows that $Z _ { i } \simeq \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ and $D _ { 1 } , D _ { 2 } \in | \mathcal { O } ( 1 , 1 ) |$ , or $\mathbb { F } _ { 2 }$ and $D _ { 1 } \sim D _ { 2 } \sim s _ { \infty }$ . The latter is in the same deformation type, so for the construction of the Lagrangian fibration $\mu$ we can assume $Z _ { i } = \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ . The central fiber $\tilde { X } _ { 0 }$ of this Kulikov model is pictured in Fig. 5.

![](images/ec35e54f2960470ecf95046eebea82a54e343c5db49193c5929153cf329f1067.jpg)\
Figure 5. The local behavior along the equator of the Kulikov model for a degeneration of $( 1 0 + k , 1 0 - k , \delta )$ .

The central fiber $\tilde { X } _ { 0 }$ has $2 + k$ irreducible components $V _ { i }$ . The two hemispherical components are isomorphic to $\widehat { Y }$ with the Symington polytope $P$ and $k$ are isomorphic to $( \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 } , D _ { 1 } + D _ { 2 } )$ . The Clemens collapse $\widehat { X } _ { t } \to \widetilde { X } _ { 0 }$ composed with the moment maps $V _ { i }  P _ { i }$ for appropriately chosen polarizations on $V _ { i }$ gives a Lagrangian torus fibration ${ \widetilde { \mu } } \colon { \widehat { X } } \to { \widetilde { B } } = \cup P _ { i }$ . We construct the claimed Lagrangian torus fibration $\mu \colon { \hat { X } } \to B$ from it by nodal slides defined in Section 6E.

by considering an ample As in Prop.
4.6, let $L = \pi ^ { * } L _ { \widehat { Y } }$ $\mathbb { Q }$ Yb -line bundle for some ample $\begin{array} { r } { L _ { \widehat { Y } } ^ { \prime } = L _ { \widehat { Y } } - \sum _ { i = 1 } ^ { k } c _ { i } E _ { i } } \end{array}$ $\mathbb { Q }$ -line bundle on b Yb for some small positive $\hat { Y }$ . We modify rational numbers $0 < c _ { i } \ll 1$ . Here, $E _ { i }$ bare the $k$ $( - 4 )$ -curves.
Below, we consider the case of a single $( - 4 )$ -curve $E _ { i }$ , with obvious modifications for the general case.
Let $\ell _ { i } = L _ { \widehat { Y } } \cdot E _ { i }$ and $\ell _ { i } ^ { \prime } = L _ { \widehat { Y } } ^ { \prime } \cdot E _ { i }$ . Then $\ell _ { i } = \ell _ { i } ^ { \prime } - 4 c _ { i }$ and $\ell _ { i \pm 1 } = \ell _ { i \pm 1 } ^ { \prime } + c _ { i }$ .

b bWe consider the polarization $\mathcal { O } ( \ell _ { i } , c _ { i } )$ on $Z _ { i } = \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ . The Symington polytope is obtained from a parallelogram with sides of lattice length $\ell _ { i } ^ { \prime }$ and $c _ { i }$ by cutting two triangles of side $c _ { i }$ erasing two of the four sides, as in the first picture of Fig. 6. This produces an IAS $^ 2$ as in the second picture (going clockwise) with two $I _ { 1 }$ singularities off the equator.
Node sliding each of them by lattice distance $c _ { i }$ gives the IAS $^ 2$ $B = P \cup P ^ { \mathrm { o p p } }$ with sides $\ell _ { i }$ and $2 k \ I _ { 1 }$ singularities on the equator.
The effect of this nodal slide on the lengths is $( \ell _ { i - 1 } ^ { \prime } , \ell _ { i } ^ { \prime } , \ell _ { i + 1 } ^ { \prime } ) \to ( \ell _ { i - 1 } ^ { \prime } + c _ { i } , \ell _ { i } ^ { \prime } - 4 c _ { i } , \ell _ { i + 1 } ^ { \prime } + c _ { i } )$ , and gives the symplectic form corresponding to $L _ { \widehat { Y } }$ .

![](images/0565ec946b31f8533b7c08c3cd72a952582e27b508b92052fd5083886571e4e8.jpg)\
Figure 6. Surgery to make IAS $^ 2$ into $P \cup P ^ { \mathrm { o p p } }$ : $( \ell _ { i - 1 } ^ { \prime } , \ell _ { i } ^ { \prime } , \ell _ { i + 1 } ^ { \prime } ) =$ $( 1 , 5 , 1 )  ( \ell _ { i - 1 } , \ell _ { i } , \ell _ { i + 1 } ) = ( 2 , 1 , 2 )$

General case.
We use the reduction given in Corollary 4.13 and Lemma 4.17. Let $\widehat { X }$ , $\widehat { X } _ { 1 }$ be K3 surfaces as in Lemma 4.17. Vary the $\mathbb { Q }$ -line bundle $L$ on $\widehat { X }$ continuously until it becomes zero on the $\left( - 2 \right)$ -curve $E$ and gives a contraction ${ \widehat { X } } \ \to \ { \widehat { X } } ^ { \prime }$ to a K3 surface with a node.
This produces a continuous family of integral affine structures.
In the limiting integral-affine structure on $B$ , two $I _ { 1 }$ singularities with monodromy rays parallel to the equatorial edge collide to give an $I _ { 2 }$ singularity with the monodromy ray in the same direction.
Smoothing ${ \widehat { X } } ^ { \prime }$ to a surface $\widehat { X } _ { 1 }$ in the $\widehat { S } _ { 1 }$ family gives a Lagrangian torus fibration $\mu \colon \widehat { X } _ { 1 } \to B$ with same $B$ . We repeat this procedure $( g - 1 )$ times to complete the proof.

One can produce either $2 ( g - 1 )$ $I _ { 1 }$ singularities in this way, or a single $I _ { 2 ( g - 1 ) }$ singularity, they are equivalent up to nodal slides along the equator.
$\boxed { \begin{array} { r l } \end{array} }$

Example 7.5 (An IAS $^ 2$ for $\widehat { S } = ( 1 2 , 6 , 1 ) )$ . Let $( \overline { { \overline { { V } } } } , \overline { { \overline { { D } } } } ) = ( \mathbb { P } ^ { 2 } , L _ { 1 } + L _ { 2 } + L _ { 3 } )$ be a toric anticanonical pair with the $\boldsymbol { L } _ { i }$ lines forming a triangle.
Let $( \overline { { V } } , \overline { { D } } )  ( \overline { { \overline { { V } } } } , \overline { { \overline { { D } } } } )$ be the blow up at the three corners of the triangle, introducing three exceptional classes $e _ { 1 }$ , $e _ { 2 }$ , $e _ { 3 }$ to get a Cremona surface.
Then, let $( V ^ { \prime } , D ^ { \prime } )  ( \overline { { { V } } } , \overline { { { D } } } )$ be the blow up of 9 total points, 3 on each strict transform of $L _ { i }$ , with exceptional classes $e _ { 4 }$ , . . . , $e _ { 1 2 }$ .

The pair $( V ^ { \prime } , D ^ { \prime } )$ arises as an $I _ { 6 } I _ { 0 }$ type quotient of an elliptic K3 surface, as in Theorem 4.1, with the length 6 cycle $D ^ { \prime }$ of alternating $( - 1 )$ - and $( - 4 )$ -curves representing the quotient of the $I _ { 6 }$ cycle.
Hence $( V ^ { \prime } , D ^ { \prime } )$ is the quotient of an elliptic K3 surface with involution, with generic Picard group $( 1 3 , 7 , 1 )$ .

Consider the ample class $1 2 h$ on $\overline { { \overline { { V } } } } = { \mathbb { P } } ^ { 2 }$ . After the three corner blow-ups, we have an ample class $1 2 h - 6 e _ { 1 } - e _ { 2 } - e _ { 3 }$ on $\overline { V }$ . Their moment polytopes are depicted in the left and center of Figure 7. After the next nine interior blow-ups, we have an ample class

$$
L _ { \epsilon } : = 1 2 h - 6 e _ { 1 } - ( 6 - \epsilon ) e _ { 8 } - \sum _ { i \geq 2 , i \neq 6 } e _ { i }
$$

on $( V ^ { \prime } , D ^ { \prime } )$ whose corresponding Symington polytope $P$ is shown on the right of Figure 7. As $\epsilon  0$ , this class becomes only big and nef, because $L _ { \epsilon } \cdot ( h - e _ { 1 } - e _ { 8 } ) = \epsilon$ and $\boldsymbol { h } - \boldsymbol { e } _ { 1 } - \boldsymbol { e } _ { 8 }$ represents the class of an exceptional curve.
Thus, $L _ { 0 }$ represents an ample class on the pair $( V , D )  ( V ^ { \prime } , D ^ { \prime } )$ resulting from the blow-down of

![](images/a1e951235c34d2551b7d112302d422a9b89aec11614e18ee9a376cf9a26a6587.jpg)

Figure 7. Left: the moment polytope for $( \mathbb { P } ^ { 2 } , 1 2 h )$ . Center: the moment polytope for $( B l _ { p _ { 1 } , p _ { 2 } , p _ { 3 } } \mathbb { P } ^ { 2 } , 1 2 h - 6 e _ { 1 } - e _ { 2 } - e _ { 3 } )$ . Right: the Symington polytope for $\left( B l _ { p _ { 1 } , \cdots , p _ { 1 2 } } \mathbb { P } ^ { 2 } , L _ { \epsilon } \right)$ .

![](images/92fe5a560e3916511d7fcdbbe5c04b2aa73393dc0a1f0eb53eee15d881ef4300.jpg)\
Figure 8. An integral-affine sphere associated to an ample class in $\widehat { S } = ( 1 2 , 6 , 1 )$ . There are 22 $I _ { 1 }$ singularities and 1 $I _ { 2 }$ singularity.

$h - e _ { 1 } - e _ { 8 }$ . Set $( \widehat { Y } , D ) = ( V , D )$ . Then $\widehat { Y }$ is the quotient of a K3 surface $\widehat { X }$ with generic Picard group $( 1 2 , 6 , 1 )$ , or alternatively $k = 3$ , $g = 2$ .

We glue two copies $B = P \cup P ^ { \mathrm { o p p } }$ together along their common boundary to form a sphere, and let $\epsilon  0$ . At $\epsilon = 0$ , the two $I _ { 1 }$ singularities in $P$ and $P ^ { \mathrm { o p p } }$ collide to form an $I _ { 2 }$ singularity on the equator.
See Figure 8.

As in Lemma 7.1, we have a degeneration $( \widehat { X } ^ { \prime } , L ) \to ( C , 0 )$ of $\mathrm { K 3 }$ surface with involution, where $\widehat { X } _ { 0 } ^ { \prime } = V ^ { \prime } \cup _ { D ^ { \prime } } V ^ { \prime }$ and the generic Picard lattice is $\widehat { S } ^ { \prime } = ( 1 3 , 7 , 1 )$ , and with $L | _ { \widehat { X } _ { 0 } ^ { \prime } } = ( L _ { \epsilon } , L _ { \epsilon } )$ . At $\epsilon = 0$ , the class $L$ is only big and nef on the general fiber, contracting the $\left( - 2 \right)$ -curve which results from smoothing the union of $\boldsymbol { h } - \boldsymbol { e } _ { 1 } - \boldsymbol { e } _ { 8 }$ and its opposite.
But instead smoothing $\widehat { X } _ { 0 } ^ { \prime }$ into the larger moduli space $( 1 2 , 6 , 1 )$ , we get a degeneration $\widehat { X }$ for which the class $L$ is ample on the general fiber.
By Theorem 7.4, we have a Lagrangian torus fibration $\widehat { X } _ { t } \ \to \ B$ , and as predicted, there $2 k = 6$ $I _ { 1 }$ singularities on the equator with monodromies transverse to the equator, and there is one $I _ { 2 ( g - 1 ) } = I _ { 2 }$ singularity on the equator, with monodromy parallel to it.
As in Corollary 4.13, the $( 1 2 , 6 , 1 )$ lattice was reached by a single $( - 1 , - 1 )$ Heegner move $( 1 3 , 7 , 1 ) \longmapsto ( 1 2 , 6 , 1 )$ , corresponding a white vertex of the $( 1 3 , 7 , 1 )$ Coxeter diagram attached to the outer 6-cycle by a bolded edge (see Fig. 3).

7C. Mirror symmetry and involutions.
Let $\mu \colon { \widehat { X } } \to B = P \cup P ^ { \mathrm { o p p } }$ be the Lagrangian torus fibration of Theorem 7.4, associated to some 2-elementary lattice $\widehat { S }$ . Suppose that the same $B = \Gamma ( X _ { 0 } )$ is the $\mathrm { I A S ^ { 2 } }$ obtained as in Construction 6.15, from the dual complex of a Kulikov surface $X _ { 0 }$ . We may smooth $X _ { 0 }$ to a Kulikov model $X \  \ ( C , 0 )$ . By the results of the following section, whenever ${ \widehat { S } } = { \overline { { T } } } =$ $e ^ { \bot } / e$ is the target of a mirror move from $S$ , we may choosing the gluings of $X _ { 0 }$ appropriately so that $X \to ( C , 0 )$ admits an involution acting on $\Gamma ( X _ { 0 } ) = B$ by the specified one, exchanging $P$ and $P ^ { \mathrm { o p p } }$ , with generic Picard group $S$ .

By the Mirror Theorem 6.19 there is a diffeomorphism $\phi \colon { \widehat { X } }  X _ { t }$ inducing an identification between a nef class $L \in \hat { e } ^ { \perp } / \hat { e }$ on $\widehat { X }$ and the monodromy vector $\lambda \in \overline { { T } } = e ^ { \perp } / e$ . Now on $\widehat { X }$ there are two involutions: $\hat { \iota }$ and $\iota _ { \phi } : = \phi ^ { - 1 } \circ \iota \circ \phi$ .

Theorem 7.6. The two involutions $\hat { \iota }$ and differ by negation (with respect to some $\iota _ { \phi }$\
section) $z  - z$ in the generic fiber $\hat { e } \simeq ( S ^ { 1 } ) ^ { 2 }$ of $\mu$ , composed with a translation\
in the fibers.
The diffeomorphism $\phi$ identifies $( e ^ { \perp } / e ) ^ { + }$ with $( \hat { e } ^ { \perp } / \hat { e } ) ^ { - }$ and $( e ^ { \perp } / e ) ^ { - }$\
with $( \hat { e } ^ { \perp } / \hat { e } ) ^ { + }$ .

Proof.
The Mirror Theorem [EF21, Prop. 3.14] proceeds by identifying $\widehat { X }$ and $X _ { t }$ as isomorphic torus bundles over the same base $B$ (this is essentially topological SYZ mirror symmetry).
The torus bundle on $\widehat { X }$ is the Lagrangian torus fibration $\mu$ , and Proposition 6.17 serves to construct the Lagrangian torus fibration on $X _ { t }$ as the composition of a Clemens collapse, and almost toric fibrations of components $V _ { i } ~ \subset ~ X _ { 0 }$ (note that our fibration $\mu$ was also constructed this way, but from $a$ different Kulikov model ${ \widehat { X } } _ { 0 } = { \widehat { Y } } \cup _ { D } { \widehat { Y } }$ ). Since the smoothing $X  ( C , 0 )$ extends an involution on $X _ { 0 }$ , we can make the Clemens collapse and almost toric fibrations involution equivariant, and so can ensure both $\iota$ and the diffeomorphism $\phi$ respect the torus bundle structure over $B$ .

Thus, $\hat { \iota }$ and $\iota _ { \phi }$ respect the torus bundle structure, and define the same involution on the base $B$ , exchanging $P$ and $P ^ { \mathrm { o p p } }$ . So the composition $\boldsymbol { \iota } _ { \phi } \circ \boldsymbol { \hat { \iota } } ^ { - 1 }$ is a fiber-preserving diffeomorphism of the torus bundle, and defines an element of the mapping class group ${ \mathrm { G L } } ( 2 , \mathbb { Z } )$ of the general fiber.
Since not all of the monodromy rays of the singularities of $B$ are parallel, the only element centralizing the monodromy on $S ^ { 2 } \setminus \{ p _ { i } \}$ is $\pm$ id.

So $\boldsymbol { \iota } _ { \phi } \circ \boldsymbol { \hat { \iota } }$ must give $\pm$ id in the mapping class group of the general fiber.
By the Mirror Theorem, $\phi$ exchanges the class $L \in S$ of an ample line bundle in the $( + 1 )$ -eigenspace of $\iota$ with the monodromy invariant $\lambda \in \widehat { S } = \overline { { T } }$ , which is in the $( - 1 )$ -eigenspace of $\hat { \iota }$ . Thus, $\iota _ { \phi } \circ \hat { \iota } = - \mathrm { i }$ d composed with a translation.
The negation $z  - z$ in the torus fibers acts by multiplication by $( - 1 )$ on $\hat { e } ^ { \perp } / \hat { e }$ , as can be seen e.g. from the Leray spectral sequence $H ^ { p } ( B , R ^ { q } \mu _ { * } \mathbb { Z } ) \implies H ^ { p + q } ( \widehat { X } , \mathbb { Z } )$ . The eigenspaces of $\hat { \iota }$ and $- \hat { \iota }$ are opposite of each other.
A translation in the fibers acts on $\hat { e } ^ { \perp } / \hat { e }$ as identity.
The theorem follows.


# 8. Kulikov models of K3 surfaces with a nonsymplectic involution

In this section for each of the 75 lattices of Fig. 1 we construct a family of models $( X , R )$ adapted to the ramification divisor of the involution.
Moreover, for the 50 cases when $R$ contains a curve $C _ { g }$ with $g \geq 2$ , we construct the divisor models $( X , C _ { g } )$ . We do it first for a generic $\lambda$ in the interior of the fundamental domain ${ \mathfrak { C } } _ { 2 }$ , and then in Sections 8G, $\mathrm { 8 H }$ for $\lambda$ on a face of $\mathfrak { C } _ { 2 }$ .

8A. The main construction.
Let $S$ be a lattice from Fig. 1, $e \in T$ a $0$ -cusp, and $\overline { { T } } = e ^ { \perp } / e$ . Let $\lambda \in { \overline { { T } } } \cap { \mathcal { C } }$ be a monodromy invariant.
Recall that $\boldsymbol { \mathscr { C } }$ is the positive cone.
Our goal now is to explicitly construct a Type III $d$ -semistable Kulikov surface $X _ { 0 }$ with the monodromy invariant $\lambda$ , admitting an involution $\iota _ { 0 }$ which extends to an involution on a Kulikov model $X \to ( C , 0 )$ for which $X _ { t } \in F _ { S }$ .

Proposition 8.1. For $g \geq 2$ , $S \neq ( 1 0 , 8 , 0 )$ , and for all 0-cusps of $F _ { S }$ , there is a well-defined stratum function

$$
{ \mathbb S } \colon \{ \lambda \colon { \overline { T } } \cap { \mathcal C } \} \to \{ c o m b i n a t o r i a l ~ t y p e s ~ o f ~ K S B A \ – s t a b l e ~ s u r f a c e s \}
$$

which assigns to each monodromy invariant $\lambda$ of a Type III degeneration, the combinatorial type of the stable limit of a degeneration $( \overline { { \boldsymbol { X } } } , \epsilon \overline { { \boldsymbol { C } } } _ { g } )$ , whose monodromy is $\lambda$ $\tilde { s }$ . Furthermore, the loci on which for which $( \overline { { F } } _ { S } ) ^ { \nu } = \overline { { F } } _ { S } ^ { \mathfrak { F } }$ . $\mathbb { S }$ is locally constant form the cones of a semifan

Dropping the condition on $g$ , we have that any degeneration with monodromy invariant $\lambda$ admits a Kulikov model of fixed combinatorial type, adapted to $R$ .

Recall, the Kulikov model is adapted to $R$ if the flat limit contains no strata, and any components of positive genus have a nef limit.

Proof.
It is already a consequence of the general theory, see [AE21, Thm. 1], [AEH21, Thm. 3.24], that when $g \geq 2$ , the KSBA compactification $F _ { S }$ is normalized by a semitoroidal compactification associated to some semifan $\tilde { \vartheta }$ . This is because the fixed locus of an involution is a so-called “recognizable divisor.”

The main tool to find the associated semifan is [AE21, Thm. 9.3]. It states that the cones $\sigma$ of the semifan $\mathfrak { F }$ are determined as the (closures of) collections of monodromy invariants $\lambda \ \in \ \sigma$ for which the KSBA-stable model of a degeneration with monodromy invariant $\lambda$ has a fixed combinatorial type, see [AE21, Def. 8.12]. Furthermore, recognizability ensures that any degeneration with a given monodromy invariant in the projective class of $\lambda$ has the same combinatorial type [AE21, Cor. 8.13]. The first statement follows.

Even when $R$ contains no components of genus $g \geq 2$ , many of the same properties of recognizability hold, in particular, the existence of a combinatorially constant Kulikov model adapted to $R$ for all divisors with a fixed monodromy invariant $\lambda$ . Specifically, the second statement follows from [AE21, Prop. 8.16] and the arguments in [AEH21, Thm. 3.24]. 

With these results in mind, we need only construct some generic divisor model with monodromy invariant $m \lambda$ , for all $\lambda \in { \overline { { T } } } \cap { \mathcal { C } }$ , and identify when the combinatorial type of the stable model changes (as a function of $\lambda$ ).

It is sufficient to consider $\lambda$ up to the isometry group $O ( \overline { { T } } )$ . Thus, we can take $\lambda$ in a fundamental chamber $\mathfrak { C } _ { 2 }$ for the reflection group $W _ { 2 }$ or, more economically, in a fundamental chamber $\mathfrak { C } _ { \mathrm { r } }$ for the full reflection group $W _ { \mathrm { r } }$ . We only care about a generic $X _ { 0 }$ within its combinatorial type.
This is quite useful, as even a smooth, non-generic K3 surface $X _ { 0 } \in \Delta \subset \mathbb { D } _ { S }$ does not smooth with its involution into $F _ { S }$ .

Now we set $\widehat S = \overline { T }$ and consider the family of K3 surfaces with the generic Picard lattice $\widehat { S }$ . Let $\widehat { X }$ be one such surface with an involution $\hat { \iota }$ . We have $( \operatorname { P i c } \widehat { X } ) ^ { + } = \widehat { S }$ . By Theorem 7.4, for an ample line bundle $L$ on $\widehat { X }$ there exists a Lagrangian torus fibration $\mu \colon ( \widehat { X } , \omega )  B$ with $B$ an IAS $^ 2$ of a special type: $B = P \cup P ^ { \mathrm { o p p } }$ , a union of two Symington polytopes interchanged by the involution $\hat { \iota }$ , and $[ \omega ] = L$ .

By Lemma 4.3 and Proposition 4.6, assuming $S \neq ( 1 0 , 1 0 , 0 )$ , $\mathfrak { C } _ { \mathrm { r } }$ can be identified with $( \operatorname { N e f } \hat { X } ) \cap \widehat { S } _ { \mathbb { R } } = \operatorname { N e f } \widehat { Y }$ for a particular quite degenerate rational surface $\hat { Y }$ , so that $L = \pi ^ { * } L _ { \widehat { Y } }$ . Replacing $L$ by $2 L$ we can assume $L _ { \widehat { Y } }$ to be integral.
Alternatively, we can work with a generic K3 surface in the $\widehat { S }$ -family and identify ${ \mathfrak { C } } _ { 2 } \simeq ( \mathrm { N e f } \ { \widehat { X } } ) \cap$ $\widehat { S } _ { \mathbb { R } } = \operatorname { N e f } \widehat { Y }$ . Working with ${ \mathfrak { C } } _ { 2 }$ or $\mathfrak { C } _ { \mathrm { r } }$ is purely a matter a convenience, except for $S = ( 1 7 , 3 , 1 )$ where we only computed ${ \mathfrak { C } } _ { 2 }$ and not $\mathfrak { C } _ { \mathrm { r } }$ in Section $\cdot$ .

Next, pick a triangulation $\tau$ of $B$ into unit lattice volume triangles, in such a way that: the vertices are lattice points, $\tau$ is involution-invariant, and the edges contain the equator.
For instance, such a triangulation arises from triangulating $P$ entirely.
Now interpret $( B , \tau )$ as an $\mathrm { I A S ^ { 2 } }$ coming from a Type III surface $X _ { 0 }$ via Construction 6.15. That is, $B = \Gamma ( X _ { 0 } )$ and for each vertex of $\tau$ , we have an anticanonical pair $( V _ { i } , D _ { i } )$ whose pseudofan $\mathfrak { F } ( V _ { i } , D _ { i } )$ models the star of the vertex.
Then, we glue $X _ { 0 } = \cup V _ { i }$ along $D _ { i }$ according to the triangulation.

For a fixed such $B$ with triangulation, the family of $d$ -semistable Type III surfaces $X _ { 0 }$ satisfying $\Gamma ( X _ { 0 } ) ~ = ~ B$ is $( \mathbb { C } ^ { * } ) ^ { 1 9 } = \operatorname { H o m } ( \Lambda , \mathbb { C } ^ { * } )$ . Here, $\Lambda$ can be computed directly from $X _ { 0 }$ by Eq. (4). We have $\Lambda = \lambda ^ { \perp }$ in $e ^ { \perp } / e \simeq L _ { \mathrm { I A S } } = \mathrm { I I } _ { 2 , 1 8 }$ , where $e$ corresponds to the 0-cusp into which $0 \in C$ maps via the extension of the period map, and $\lambda$ is the monodromy invariant.

Example 8.2. Taking $B = P \cup P ^ { \mathrm { o p p } }$ from Figure 8, we may triangulate it in an involution-invariant manner, and realize it as the dual complex of a Type III Kulikov surface.
See Figure 9. Then 22 components $( V _ { i } , D _ { i } )$ have charge $Q ( V _ { i } , D _ { i } ) = 1$ , one component has $Q = 2$ , and the remaining components, with $Q = 0$ , are toric.

Theorem 8.3. Let $S \  \ \overline { { T } } \ \simeq \ \widehat { S }$ be a mirror move let $L \in { \widehat { S } }$ be an ample line bundle on ${ \hat { X } } \in { \hat { S } }$ . Let $\lambda \ = \ L$ under the identification $\overline { { T } } \simeq \widehat { S }$ . Let $P$ be the Symington polytope of $\widehat { Y } = \widehat { X } / \widehat { \iota }$ associated to the image $L _ { \widehat { Y } }$ and let $B = P \cup P ^ { \mathrm { o p p } }$ bbe the integral-affine sphere built from gluing two copies of $P$ (see Section $\cdot$ for further details on these gluings).
Let $\tau$ be an involution-invariant triangulation of $B$ containing the equator.

Then $B = \Gamma ( X _ { 0 } )$ for a Type III Kulikov surface $X _ { 0 }$ admitting an involution $\iota _ { 0 }$ inducing the involution on $B$ . Furthermore, by choosing the period of $X _ { 0 }$ appropriately, there is a smoothing $X \to ( C , 0 )$ with involution ι whose general fiber $X _ { t }$ lies in $F _ { S }$ and whose monodromy invariant is $\lambda \in T$ .

It is worth remarking that the combinatorial type of $X _ { 0 }$ is completely determined by the vector $\lambda \in { \overline { { T } } }$ and has nothing to do with the source $S$ of the mirror move.
This source $S$ is determined by choosing the period $\psi _ { X _ { 0 } }$ appropriately.

![](images/dfb410e5ac7dcddf051dd493fd68feee90cdb13dac871dd5a4c50fcc391da6e8.jpg)\
Figure 9. A Kulikov surface $X _ { 0 }$ for $\widehat { S } = ( 1 2 , 6 , 1 )$ with $\Gamma ( X _ { 0 } ) =$ $B$ , with triple points shown in yellow and double curves in black.

Proof.
We observe that the gluings of the standard surface $X _ { 0 }$ (satisfying $\psi _ { X _ { 0 } } = 1$ ) are unique, hence invariant under the involution on $B$ . So $X _ { 0 }$ admits an involution $\iota _ { 0 }$ acting on $B$ by the involution $\iota _ { \mathrm { I A S } }$ switching $P$ and $P ^ { \mathrm { o p p } }$ .

We analyze the deformations $X _ { 0 }  X _ { 0 } ^ { \prime }$ for which $X _ { 0 } ^ { \prime }$ retains an involution $\iota _ { 0 } ^ { \prime }$ . For there to be an involution on $X _ { 0 } ^ { \prime }$ the period point $\psi _ { X _ { 0 } ^ { \prime } } \in \mathrm { H o m } ( \Lambda , \mathbb { C } ^ { * } )$ must be anti-invariant with respect to $\iota _ { 0 } ^ { * }$ , under identification $\Lambda ( X _ { 0 } ^ { \prime } ) \simeq \Lambda ( X _ { 0 } )$ . This is because the target $\mathbb { C } ^ { * }$ depends on a choice of orientation on $B$ , which is reversed by $\iota _ { \mathrm { I A S } }$ , see [AET19, Sec. 6G]. We conclude that a generic involutive $X _ { 0 } ^ { \prime }$ deforming $X _ { 0 }$ is one for which $\ker ( \psi _ { X _ { 0 } ^ { \prime } } ) \supset \Lambda ^ { + }$ where $\Lambda ^ { + }$ is the (+1)-eigenspace of $\iota _ { 0 } ^ { * }$ acting on $\Lambda ( X _ { 0 } )$ . The period torus for these involutive Kulikov surfaces is $\mathrm { H o m } ( \Lambda / \Lambda ^ { + } , \mathbb { C } ^ { * } )$ . These deformations of the standard surface $X _ { 0 }$ will become the Kulikov surfaces corresponding to a simple mirror move $S  { \widehat { S } }$ .

The involution $\iota _ { \mathrm { I A S } }$ on $B$ has an induced action $\iota _ { \mathrm { I A S } } ^ { * }$ on $H ^ { 1 } ( B , T _ { \mathbb { Z } } ^ { * } ) \simeq \operatorname { I I } _ { 2 , 1 8 } =$ $L _ { \mathrm { { I A S } } }$ which is easily seen to be an isometry with respect to the intersection form [ABE22, Ex. 7.27] on visible curves, see Section 6G. The induced involution on $\Lambda = \lambda ^ { \perp }$ agrees with the action of $\iota _ { 0 } ^ { * }$ on $\Lambda ( X _ { 0 } )$ for the standard surface $X _ { 0 }$ . Here $\lambda$ , too, can be interpreted purely in integral-affine terms as the so-called radiance obstruction in $H ^ { 1 } ( B , T _ { \mathbb { Z } } ^ { * } )$ of the integral-affine structure.
So it is automatically preserved by $\iota _ { \mathrm { I A S } }$ . We define $\rho _ { \mathrm { I A S } } : = - \iota _ { \mathrm { I A S } } ^ { \ast } \in O ( L _ { \mathrm { I A S } } )$ . The motivation for this definition is Theorem 7.6 (which notably relies on this theorem).

Let $L _ { \mathrm { I A S } } ^ { \pm }$ denote the eigenspaces of $\rho _ { \mathrm { I A S } }$ . We claim that $L _ { \mathrm { I A S } } ^ { - } = \widehat { S }$ or equivalently $( \iota _ { \mathrm { I A S } } ^ { * } ) ^ { + } = \widehat { S }$ . This can be verified purely on the symplectic side, by observing that we have an isomorphism $\hat { e } ^ { \perp } / \hat { e } \cong L _ { \mathrm { I A S } }$ where $\hat { e }$ is the Lagrangian fiber class of $\mu \colon { \widehat { X } } \to B$ . The involution $\hat { \iota }$ quotients this fibration of $\widehat { X }$ to the Lagrangian torus bfibration ${ \hat { Y } }  P$ . Thus, $L _ { \mathrm { I A S } } ^ { - } \otimes \mathbb { Q } \simeq H ^ { 2 } ( Y , \mathbb { Q } )$ and so $\widehat { S } \subset \widehat { e } ^ { \perp } / \widehat { e }$ must equal $L _ { \mathrm { I A S } } ^ { - }$ .

Denote $L _ { \mathrm { I A S } } ^ { + } : = S ^ { \mathrm { s a t } }$ (this choice of notation will be made reasonable soon).
It is a 2-elementary lattice in $L _ { \mathrm { I A S } } \simeq \mathrm { I l } _ { 2 , 1 8 }$ perpendicular to $\widehat { S }$ and so $S ^ { \mathrm { s a t } }$ is the source of a simple mirror move with target $\widehat { S }$ . Smoothing $X _ { 0 } ^ { \prime }$ (a deformation of the standard surface $X _ { 0 }$ as above), keeping the classes in $S ^ { \mathrm { s a t } }$ Cartier, we produce the claimed degeneration of the theorem, in the case of a simple mirror move.
The smoothings that keep $S ^ { \mathrm { s a t } }$ Cartier (at least for $X _ { 0 } ^ { \prime }$ period-generic) are identified with the deformations extending the involution $\iota _ { 0 }$ by [AET19, Thm. 6.35].

For the non-simple mirrors, we observe that an involutive $X _ { 0 }$ need not be a deformation of the standard surface: There may be other connected components in $\mathrm { H o m } ( \Lambda , \mathbb { C } ^ { * } )$ of the space of anti-invariant periods.
These connected components also admit an involution, because

(1) $\rho _ { \mathrm { I A S } }$ acts on the (re)gluing complex of [AE21, Sec. 7A] and an involution anti-invariant regluing of an involutive $X _ { 0 }$ will be involutive, and (2) the period and gluing complexes are quasi-isomorphic [AE21, Thm. 7.9].

The connected components of the anti-invariant periods are determined by a lattice $S = ( \ker \psi ) ^ { + }$ which has index at most 2 in $S ^ { \mathrm { s a t } } = L _ { \mathrm { I A S } } ^ { + }$ and furthermore contains $( 1 + \rho _ { \mathrm { I A S } } ) L _ { \mathrm { I A S } } ^ { + }$ . Up to isometry, these are in bijection with the sources $S$ of mirror moves with target $\widehat { S }$ , by Theorem 5.16.

So these components of anti-invariant periods also parameterize involutive Kulikov surfaces, and the same argument as in the previous paragraph applies to prove that such an $X _ { 0 } ^ { \prime }$ smooths, with its involution, into moduli of $S$ -polarized K3 surfaces.

Finally, we must verify that the monodromy invariant $\lambda$ is as stated.
This is follows from the Monodromy Theorem 6.19, which identifies $[ \omega ] = L \in \hat { e } ^ { \perp } / \hat { e }$ on $\widehat { X }$ with $\lambda \in e ^ { \perp } / e$ on the smoothing $X _ { t } ^ { \prime }$ of $X _ { 0 } ^ { \prime }$ . $\boxed { \begin{array} { r l } \end{array} }$

By Proposition 8.1, we must understand the stable models associated to each $\lambda \in \mathfrak { C } _ { 2 }$ (including for $\lambda$ only big and nef, on faces of $\mathfrak { C } _ { 2 }$ ). For this, it will suffice to show that the Kulikov models of Theorem 8.3 are, after some appropriate M1 modifications (Section 8D), adapted to $R$ . Then, by passing to the stable model (6.9), we can explicitly determine the combinatorial types of stable models on each face of ${ \mathfrak { C } } _ { 2 }$ in terms of the ADE surfaces of [AT21] to find the semifan $\tilde { s }$ .

This requires understanding in some detail how the singularities on the IAS2 collide.
When $\lambda = L$ is ample, in the interior of $\mathfrak { C } _ { 2 }$ , the parameters $\ell _ { i } : = \lambda \cdot \alpha _ { i }$ are all positive, where $\alpha _ { i }$ are the simple roots.
Then, no singularities $B ( \lambda )$ have collided, except the $I _ { 2 g - 2 }$ singularity which forms on an edge of the equator.

For a non-general $\lambda$ with $\lambda ^ { 2 } ~ > ~ 0$ lying on a face of ${ \mathfrak { C } } _ { 2 }$ , some $\ell _ { i } = 0$ . The corresponding IAS $^ 2$ $B ( \lambda )$ is obtained from a generic IAS $^ 2$ $B ( \lambda + t \lambda _ { 0 } )$ for some $\lambda _ { 0 } \in ( \mathfrak { C } _ { 2 } ) ^ { \mathrm { i n t } }$ in the interior, by letting $t  0$ . Then, the $I _ { 1 }$ and $I _ { 2 g - 2 }$ singularities on $B ( \lambda + t \lambda _ { 0 } )$ collide as $t \to 0$ to give more complicated singularities associated to higher charge anticanonical pairs $( V _ { i } , D _ { i } )$ . We discuss this in Section 8G.

Ultimately, only the facets of $\mathfrak { C } _ { \mathrm { r } }$ which are also facets of $\mathfrak { C } _ { 2 }$ matter; for the other facets, the singularity collision can be avoided, and the stable models will not change.
For the (highly non-generic) $\lambda \in \mathfrak { C } _ { \mathrm { r } }$ satisfying $\lambda ^ { 2 } = 0$ , the IAS $^ 2$ collapses to an interval, the dual graph of a Type II degeneration.
These are discussed in Section 8H.

8B. Edge behavior in the gluing of $P$ and $P ^ { \mathrm { o p p } }$ . Consider an IAS $^ 2$ $B =$ $P \cup P ^ { \mathrm { o p p } }$ with a set of integral points and an involution $\iota$ exchanging $P$ and $P ^ { \mathrm { o p p } }$ . Let $C$ be a side of $P$ . The gluing along $C$ could be of two types.
We say that it is even if for any lattice point $u \in P$ the lattice distance between $u$ and $\iota ( u )$ is always even, and odd if it is odd for some $u$ . This is illustrated in Fig. 10.

![](images/9ca8b906856b21af82c78a4952e1ad6ba84c2692bb94fda8608a3333344b24b2.jpg)\
Figure 10. Equatorial behavior: even vs odd

Lemma 8.4. In the $I _ { 2 \bar { k } } I _ { 0 }$ case, when $B$ has $2 k > 0$ $I _ { 1 }$ singularities on the equator at the vertices of $P$ , gluing along the side corresponding to a curve $E _ { i }$ on $\hat { Y }$ with $E _ { i } ^ { 2 } = - 4$ (resp.
$E _ { i } ^ { 2 } = - 1$ ) is even (resp.
odd).

Proof.
The statement is obvious from Fig. 6.

Note: when there are no singularities on the equator, there are no such restrictions and below we will give examples of both even and odd behaviors.

Next, we find anticanonical pairs $( V , D )$ corresponding to the nonsingular lattice points of $B$ on the equator.
Nonsingularity implies means that these are toric pairs.
We say that an involution on a toric pair is nonsymplectic if the action on the cocharacter lattice $\mathbb { Z } ^ { 2 }$ has determinant $^ { - 1 }$ . Equivalently, it acts by multiplying a generator of $H ^ { 0 } ( V , \omega _ { V } ( D ) )$ by $^ { - 1 }$ .

Lemma 8.5. Let ι be a nonsymplectic involution on a toric pair $( V , D )$ such that the fixed locus $V ^ { \iota }$ does not contain any torus-fixed points of $V$ . Then $V$ admits a generic ruling $\pi \colon V \to \mathbb { P } ^ { 1 }$ with two sections $s _ { 1 }$ , $s _ { 2 }$ . The map commutes with $a$ nontrivial involution on the base $\mathbb { P } ^ { 1 }$ and there are three cases:

(E0) $V ^ { \iota }$ consists of four points, two on each $s _ { i }$ (E1) $V ^ { \iota }$ is a fiber of $\pi$ plus two points, one on each $s _ { i }$ (E2) $V ^ { \iota }$ is two fibers of $\pi$ .

The cases E0 and $E 2$ give the even equatorial behavior, and E1 the odd equatorial behavior.
The fan of $V$ is an involution-invariant subdivision of the fan for $\mathbb { F } _ { n }$ with $n$ even for E0, $E 2$ , resp.
with $n$ odd for $E 1$ .

Proof.
Consider the fan $\mathfrak { F }$ of $V$ . The involution acting on the cocharacter lattice $N = \mathbb { Z } ^ { 2 }$ has a fixed line and it does not intersect the interior of a two-dimensional cone in $\mathfrak { F }$ by the condition on $V ^ { \iota }$ . So in $\mathfrak { F }$ there are two rays $\pm e _ { 1 }$ , fixed by the involution.
Let $\langle e _ { 1 } , e _ { 2 } \rangle$ be a basis.
Then $e _ { 2 }  - e _ { 2 } + k e _ { 1 }$ with $k$ either even or odd, and we can assume that $k = 0$ or $^ { 1 }$ . Any nonsingular involution-invariant fan is a symmetric subdivision of the fan with the rays $\pm e _ { 1 }$ , $e _ { 2 } + m e _ { 1 }$ , $- e _ { 2 } + ( k + m ) e _ { 1 }$ which is the fan of $\mathbb { F } _ { n }$ for $n = | k + 2 m |$ . This defines the action on monomials up to constants: $x ^ { m } \to c ( m ) x ^ { \iota m }$ . It is easy to see that up to rescaling there are the following three possibilities, giving the three cases above: (E0) $( x , y ) \to ( - x , y ^ { - 1 } )$ , or (E1) $( x , y ) \to ( x , x y ^ { - 1 } )$ , or (E2) $( x , y )  ( x , y ^ { - 1 } )$ . 

We begin by describing Kulikov models for the lattices $\overline { T }$ on the $\bar { g } = 1$ line.
Note that these only appear as the targets of simple mirror moves.

8C. Models for $\overline { { T } } = ( 1 0 + \bar { k } , 1 0 - \bar { k } , \delta )$ , $1 \leq k \leq 9$ . By Theorem 7.4, for an ample line bundle $L$ , i.e. a generic monodromy vector $\lambda$ , the IAS $^ 2$ $B$ has 24 distinct $I _ { 1 }$ singularities.
Consider the Type III surface $X _ { 0 }$ of Theorem 8.3 with its involution $\iota _ { 0 }$ and involution-equivariant smoothing $( X , \iota )$ . The flat limit of $R _ { t } = \operatorname { F i x } ( \iota _ { t } )$ is the divisorial locus $R _ { 0 }$ in $\mathrm { F i x } ( \iota _ { 0 } )$ . Note that since $X$ is smooth, $\operatorname { F i x } ( \iota )$ as a set consists of relative curves $R \subset X$ and isolated points in $X _ { 0 }$ .

Let us first deal with the pairs $( V _ { j } , D _ { j } )$ corresponding to the lattice points in the interior of either hemisphere.
They fall into disjoint pairs $V _ { j }$ , $V _ { j } ^ { \mathrm { o p p } }$ exchanged by $\iota _ { 0 }$ . Most of the pairs are toric, entirely determined by the triangulation $\tau$ . There are also $1 2 - \bar { k }$ pairs of $I _ { 1 }$ singularities of charge $Q = 1$ . These are almost toric pairs, with a single internal blowup at the side determined by the monodromy ray.
The divisor $R _ { 0 }$ is empty on these components.

![](images/1bfde7dfa40a3134aa8877d3c6af38b47a258ddbf746f3fcd750094d599a8c07.jpg)\
Figure 11. Kulikov models for the $\bar { g } = 1$ case

Next are the pairs corresponding to the nonsingular lattice points on the equator.
These are of types $\mathrm { E 1 }$ or $\mathrm { E 2 }$ of Lemma 8.5 respectively for the sides of $\hat { Y }$ with $E _ { i } ^ { 2 } = - 1$ and $E _ { i } ^ { 2 } = - 4$ .

Finally, we need to determine the cbec, together with the involution, of an $I _ { 1 }$ singularity at a vertex of the polytope $P$ . From either Fig. 6 or 10 we see that the minimal pseudofan for this singularity consists of two rays $v _ { 1 } = \left( - 2 , 1 \right)$ on the side with $E _ { 1 } ^ { 2 } = - 1$ , $v _ { 2 } = ( 1 , 0 )$ on the side with $E _ { 2 } ^ { 2 } = - 4$ , and the monodromy ray $v _ { \mathrm { m o n } } = ( 0 , - 1 )$ . The balancing condition for these vectors is $v _ { 1 } + 2 v _ { 2 } = - v _ { \mathrm { m o n } }$ . This is the pseudofan of $\left( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } \right)$ with $D _ { 1 }$ a line (so $D _ { 1 } ^ { 2 } = 1$ ), $D _ { 2 }$ a conic (so $D _ { 2 } ^ { 2 } = 4$ ), and an involution whose fixed locus is a line $R$ and an isolated point.
The balancing condition [AET19, Sec. 2E] reads $\textstyle \sum _ { i = 1 } ^ { 2 } ( R \cdot D _ { i } ) v _ { i } \in \mathbb { Z } v _ { \mathrm { m o n } }$ .

Therefore, $B$ is the IAS $^ 2$ given by Construction 6.15 for the surfaces $X _ { 0 }$ glued from $2 k$ pairs in the cbec of $\left( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } \right)$ , $k$ chains of lengths $\ell _ { i } = L \cdot E _ { i }$ of type E1 for odd $i$ , $\bar { k }$ chains of lengths $\ell _ { i } = L \cdot E _ { i }$ of type $\mathrm { E 2 }$ for even $i$ , $1 2 - k$ pairs of almost toric surfaces with a single blowup, and the rest toric pairs.
The triangulation $\tau$ specifies the combinatorial type of each pair precisely.

This surface can be read of directly from the Coxeter diagram for the lattice $T$ given in Figs.
3, 4. The most relevant part is the cycle of $2 k$ white vertices, alternating between double circled and single circled.
Each edge on this cycle corresponds to a $\mathbb { P } ^ { 2 }$ . A single circled vertex, with odd $_ i$ corresponds to a line, and a double circled vertex, with even $_ i$ corresponds to a conic on $\mathbb { P } ^ { 2 }$ .

Each integral vector $\lambda \in \mathfrak { C } _ { \mathrm { r } }$ defines the nonnegative integers $\ell _ { i } = \lambda \cdot \alpha _ { i }$ . The numbers $\ell _ { i }$ for these $2 \bar { k }$ simple roots $\alpha _ { i }$ on the $2 k$ -cycle specify the lengths of chains as above.
In addition, the other $\ell _ { i }$ define the locations of the nontoric surfaces in the hemispheres.
On the mirror side, if ${ \widehat { Y } } \to { \overline { { Y } } }$ is a toric model with exceptional curves $E _ { i }$ , $i > 2 \bar { k }$ , then $E _ { i }$ correspond to some of the vertices in the Coxeter diagram and the lattice distance of a singularity from the equator is determined in terms of $\ell _ { i } = L \cdot C _ { i }$ . We give a cartoon picture for the equator of $X _ { 0 }$ in Fig. 11, with the fixed locus shown in red.
The divisorial part $R _ { 0 }$ of $\mathrm { F i x } ( \iota _ { 0 } )$ is a degeneration of genus 3 curves $\operatorname { F i x } ( \iota _ { t } )$ .

A detailed example of this construction was given in [AET19] for $\overline { { T } } = ( 1 9 , 1 , 1 )$ . In that case, there are 18 $I _ { 1 }$ singularities on the equator, and 3 pairs of $I _ { 1 }$ singularities in the hemispheres.
The lengths $\ell _ { 0 } , \ldots , \ell _ { 1 7 }$ give the lengths of the chains of toric surfaces on the equator.
On the mirror side, the morphism to the toric model ${ \widehat { Y } } \to { \overline { { Y } } }$ consists of three disjoint blowups, and the distances of the nontoric surfaces $V _ { j }$ from the equator are $L \cdot E _ { i }$ for $i = 1 8 , 1 9 , 2 0$ .

Each of the lattices $\overline { T }$ on the $\bar { g } = 1$ line is the target of a unique mirror move $S  T  \overline { { T } }$ as in Definition 5.6, which is simple.
So $S \subset L _ { \mathrm { I A S } }$ is saturated and the set of symmetric periods is the torus $\mathbb { T } _ { \Lambda / S }$ and the family of Type III surfaces contains the standard surface corresponding to the period $\psi = 1$ .

8D. Models for $\overline { T }$ with $\bar { g } \geq 2$ , excluding $( 1 0 , 8 , 0 )$ . We use the reduction from the $\bar { g } = 1$ case given in Section 4F. The lattice

$$
\overline { { { T } } } = \widehat { S } = ( 1 0 + \bar { k } - ( \bar { g } - 1 ) , 1 0 - \bar { k } - ( \bar { g } - 1 ) , \bar { \delta } )
$$

is obtained from the lattice $\overline { { { T } } } ^ { \prime } = \widehat { S } ^ { \prime } = ( 1 0 + \bar { k } , 1 0 - \bar { k } , 1 )$ by a chain of $\bar { g } \mathrm { ~ - ~ } 1$ Heegner $( - 1 , - 1 )$ moves.
The set of possible monodromy invariants $\lambda \in { \overline { { T } } }$ lie in the fundamental chamber for $\overline { T }$ which is a face of the fundamental chamber for $\overline { { T } } ^ { \prime }$ , obtained by setting some of the lengths $\ell _ { i }$ with $i > 2 k$ to zero.

By Theorem 7.4 the IAS $^ 2$ for $\overline { T }$ is obtained from the IAS $^ 2$ for $\overline { { T } } ^ { \prime }$ by descending $( \bar { g } - 1 )$ pairs of $I _ { 1 }$ singularities in the interiors of the hemispheres symmetrically to the equator, to a side of type E1 of Lemma 8.5 with odd equatorial behavior, to get an $I _ { 2 ( \bar { g } - 1 ) }$ singularity with monodromy rays parallel to the equator.

What remains to see is an involution on an actual surface $X _ { 0 }$ and specifically the surfaces $V _ { i }$ with involution on the equator.
To describe them we introduce two moves, illustrated in Fig. 12.

![](images/67a40daba63d9b26ff5303156b75371493d4b017c8cad18ffa75c26c21e8eabf.jpg)\
Figure 12. A- and B-moves

A-move: Let $V ^ { \prime } \to { \mathbb { P } } ^ { 1 }$ be a toric surface of type $\mathrm { E 1 }$ of Lemma 8.5. The A-move is blowing up one of the fixed points on a section, say $s _ { 1 }$ twice.
In the corresponding fiber of $V \to \mathbb { P } ^ { 1 }$ this creates the fiber $\begin{array} { r } { E _ { 1 } + 2 E _ { 2 } + E _ { 3 } } \end{array}$ with $E _ { 1 } ^ { 2 } = E _ { 3 } ^ { 2 } = - 1$ and $E _ { 2 } ^ { 2 } = - 2$ , the the interior $( - 2 )$ -curve $E _ { 2 }$ is fixed by the induced involution of $V$ .

Let $( g , k )$ be the invariants of the K3 surfaces in the $S ^ { \prime }$ family, so that $\overline { { T } } ^ { \prime }$ wa s reached by the simple mirror move $S ^ { \prime }  T$ . Then the Type III surface we obtained belongs to the $S$ -family with the invariants $( g , k + 1 )$ .

The point we have blown up twice in the toric model ${ \overline { { V } } } ^ { \prime }$ of $V ^ { \prime }$ corresponds to $^ { - 1 }$ with respect to the origin of the blown up side.
Therefore, we can for example take $X _ { 0 }$ of this type to be the standard surface, with $\psi = 1$ . In particular, the A-move keeps a simple mirror move $S  { \widehat { S } }$ simple, in the sense that $S$ changes by a $( + 1 , - 1 )$ Heegner move, while $\widehat S$ changes by a $( - 1 , - 1 )$ Heegner move.

B-move: For the B-move we instead blow up twice the other fixed point, the one that lies on a fiber fixed by the involution pointwise.
On the surface $\mathrm { B l } _ { 2 } \ V$ the fixed locus of the involution consists of two $( - 1 )$ -curves $E _ { 1 }$ , $E _ { 3 }$ in the fiber $\begin{array} { r } { E _ { 1 } + 2 E _ { 2 } + E _ { 3 } } \end{array}$ . The divisor $V ^ { \iota }$ fixed by the induced involution is not nef since it contains $E _ { 1 }$ and $E _ { 3 }$ and not $E _ { 2 }$ .

We flop $E _ { 1 }$ to a neighboring surface $V _ { 1 }$ by the M1 modification.
In $V _ { 1 }$ this creates a fiber $E _ { 1 } ^ { \prime } + E _ { 2 } ^ { \prime }$ with $E _ { 1 } ^ { \prime 2 } = E _ { 2 } ^ { \prime 2 } = - 1$ , where $E _ { 1 } ^ { \prime }$ is not in $V _ { 1 } ^ { \iota }$ and $E _ { 2 } ^ { \prime }$ is.
The ramification divisor is not nef again.
We proceed by flopping in $E _ { 2 } ^ { \prime }$ etc, until we reach a component in the cbec of $\left( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } \right)$ corresponding to the $I _ { 1 }$ singularity of the IAS2. This is where the sequence of flops stops, making $\left( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } \right)$ with $D _ { 1 } ^ { 2 } = 1$ , $D _ { 2 } ^ { 2 } = 4$ into $( \mathbb { F } _ { 1 } , D _ { 1 } + D _ { 2 } )$ with $D _ { 1 } ^ { 2 } = 0$ , $D _ { 2 } ^ { 2 } = 4$ and the ramification into a fiber of $\mathbb { F } _ { 1 } \to \mathbb { P } ^ { 1 }$ .

We do the same with the other $( - 1 )$ -curve $E _ { 3 }$ on $V$ , flopping it all the way to the surface in the cbec of $( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } )$ on the equator in the other direction.
The end result is that the entire chain of surfaces between the two $\left( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } \right)$ -components, which in $X _ { 0 } ^ { \prime }$ was a chain of toric surfaces of equatorial type E1 is now a chain of toric surfaces of equatorial type $\mathrm { E 0 }$ , with no divisorial part in the fixed locus.

If $( g , k )$ are the invariants of the K3 surfaces in the $S ^ { \prime }$ family then the Type III surface $X _ { 0 }$ obtained by the B-move has invariants $( g - 1 , k )$ and thus must be the result of a non-simple mirror move.

Now repeat this procedure $( \bar { g } - 1 )$ times doing either the A-move every time, or $( \bar { g } - 2 )$ -times the A-move and once the B-move.
Let $X _ { 0 }$ be either of the surfaces obtained this way.
There is an entire 19-dimensional family $\mathrm { H o m } ( \Lambda , \mathbb { C } ^ { * } )$ of $d$ - semistable surfaces $X _ { 0 } ( \psi )$ of the same deformation type.

As in Theorem 8.3, the subset of anti-symmetric periods is a union of torus translates of $\mathbb { T } _ { \Lambda / \Lambda ^ { + } } : = \mathrm { H o m } ( \Lambda / \Lambda ^ { + } , \mathbb { C } ^ { * } )$ . As before, $\Lambda = \lambda ^ { \perp }$ in $L _ { \mathrm { { I A S } } }$ , $\overline { { T } } = L _ { \mathrm { I A S } } ^ { - }$ , and $\Lambda ^ { + } = L _ { \mathrm { I A S } } ^ { + } = ( \overline { { T } } ) ^ { \perp } = S ^ { \mathrm { s a t } }$ in $L _ { \mathrm { { I A S } } }$ . The coset of $\mathbb { T } _ { \Lambda / \Lambda ^ { + } }$ containing the standard surface is of the A...A type, and all other involution anti-invariant cosets of $\mathbb { T } _ { \Lambda / \Lambda ^ { + } }$ are of the A...AB type.

8E. Monodromy invariants for $\overline { { T } } = ( 1 0 , 1 0 , 0 )$ . In this case, the source of the mirror move must be $S = ( 1 0 , 1 0 , 0 )$ , so $\overline { T }$ corresponds to the self-mirror cusp of Enriques K3 moduli.

By Theorem 7.4 and Lemma 7.1, the IAS $2$ $B = P \cup P ^ { \mathrm { o p p } }$ in this case is obtained from the IAS $^ 2$ $B ^ { \prime } = P \cup P ^ { \mathrm { o p p } }$ of the $( 1 0 , 1 0 , 1 )$ case by gluing $P ^ { \mathrm { o p p } }$ to $P$ by twisting halfway along the circular boundary.
This is possible, so long as the affine length of the equator is even, which can always be achieved by replacing $\lambda$ by $2 \lambda$ . So the Type III surface is obtained from a Type III surface of the $( 1 0 , 1 0 , 1 )$ case by this rotation.
The involution $\iota _ { 0 }$ on $X _ { 0 }$ is base point free.

$( 1 0 , 1 0 , 0 )$ is the only case when the fundamental chambers ${ \mathfrak { C } } _ { 2 }$ and $\mathfrak { C } _ { \mathrm { r } }$ are not the nef cones of quotient surfaces $\hat { Y }$ . Indeed, for a general Enriques surface $\widehat { Y }$ the nef cone is the round cone $\bar { \mathcal { C } }$ . On the other hand, in the IAS2 $B$ , we used the Symington polytope $P$ from the Halphen $( 1 0 , 1 0 , 1 )$ case, which certainly has polyhedral walls, and so is not the entire round cone.

On the other hand, $\mathfrak { C } _ { \mathrm { r } } ( 1 0 , 1 0 , 0 )$ is a subset of $\mathfrak { C } _ { \mathrm { r } } ( 1 0 , 1 0 , 1 )$ . Indeed, the Coxeter diagrams for both lattices are given in Fig. 3 and they are nearly identical.
Denote the simple root vectors in $E _ { 8 } ( 2 )$ by $\alpha _ { 1 } , \ldots , \alpha _ { 8 }$ , so that $\alpha _ { i } ^ { 2 } = - 4$ and $\alpha _ { i } \cdot \alpha _ { j } \in \{ 0 , 2 \}$ for $i \neq j$ . Let $U = \langle e , f \rangle$ with $e ^ { 2 } = f ^ { 2 } = 0$ , $e \cdot f = 1$ . One has $( 1 0 , 1 0 , 0 ) = E _ { 8 } ( 2 ) \oplus$ $U ( 2 )$ and $( 1 0 , 1 0 , 1 ) = E _ { 8 } ( 2 ) \oplus I _ { 1 , 1 } ( 2 )$ , where $U ( 2 ) = \langle 2 e , f \rangle$ and $I _ { 1 , 1 } = \langle 2 e , e + f \rangle$ are two different index 2 sublattices of $U$ .

Then the first 9 vectors of the two Coxeter diagrams are exactly the same: $\alpha _ { 1 } , \ldots , \alpha _ { 8 } , \alpha _ { 9 } = 2 e - \alpha _ { 0 }$ , where $- \alpha _ { 0 }$ is the longest root of $E _ { 8 }$ . It is only the last, 10th roots that are different.
For $( 1 0 , 1 0 , 0 )$ it is $\alpha _ { 1 0 } = - 2 e + f$ , and for $( 1 0 , 1 0 , 1 )$ it is $\alpha _ { 1 0 } ^ { \prime } = - e + f$ . Thus, $\alpha _ { 1 0 } ^ { \prime } = \alpha _ { 1 0 } + e$ . Since $e$ is a positive linear combination of , if $\lambda$ is a vector in $\mathfrak { C } _ { \mathrm { r } } ( 1 0 , 1 0 , 0 )$ , i.e. a vector satisfying $\lambda \cdot \alpha _ { i } \geq 0$ for $\alpha _ { 1 } , \ldots , \alpha _ { 9 }$ $i = 1 , \ldots , 1 0$ then one moreover has $\lambda \cdot \alpha _ { 1 0 } ^ { \prime } \geq 0$ .

So for any $\lambda \in \mathfrak { C } _ { \mathrm { r } } ( 1 0 , 1 0 , 0 ) \subset \mathfrak { C } _ { \mathrm { r } } ( 1 0 , 1 0 , 1 )$ we interpret $\lambda$ as a vector defining the Symington polytope for $( 1 0 , 1 0 , 1 )$ by the previous construction, and take $B$ to be $P \cup P ^ { \mathrm { o p p } }$ glued with a half-circle rotation in the equator.

8F. Models for $T = ( 1 0 , 8 , 0 )$ , $( 1 0 , 1 0 , 0 )$ , $( 1 0 , 1 0 , 1 )$ . There are five mirror moves $S \sim T$ for which the integral affine structure $B = P \cup P ^ { \mathrm { o p p } }$ has a circular equator with no singularities on it.
They are:

![](images/b590597a5c144f201a9b670a2837de104c99a334e6c99054ba555961c2d509bc.jpg)\
Figure 13. The fixed loci in circular equators, shown in red, and the corresponding edge behavior.

$$
\begin{array} { r l } & { ( 1 0 , 1 0 , 0 ) \to ( 1 0 , 1 0 , 0 ) , \quad ( 1 0 , 1 0 , 1 ) \to ( 1 0 , 1 0 , 1 ) , } \\ & { ( 1 0 , 8 , 0 ) \to ( 1 0 , 8 , 0 ) , \qquad ( 1 0 , 1 0 , 0 ) \Rightarrow ( 1 0 , 8 , 0 ) , \quad ( 1 0 , 1 0 , 1 ) \Rightarrow ( 1 0 , 8 , 0 ) . } \end{array}
$$

In particular, the lattice $\overline { { T } } = ( 1 0 , 8 , 0 )$ is the target of three mirror moves.
Respectively, there are three families of Type III surfaces with anti-symmetric periods.
All of them share the same IAS $^ 2$ $B = P \cup P ^ { \mathrm { o p p } }$ , glued from two copies of a Symington polytope $P$ for the anticanonical pair $( \hat { Y } , \hat { D } )$ with $\widehat { Y } = B l _ { p 1 , \ldots , p 9 } \mathbb { P } ^ { 2 }$ and $\widehat { D }$ the strict transform of a cubic through the nine points $p _ { i }$ . The gluing as in Section 8B is with the even equatorial behavior.
The only difference is in the periods.

For the $( 1 0 , 1 0 , 1 )  ( 1 0 , 1 0 , 1 )$ mirror move, the target $\mathrm { I A S ^ { 2 } }$ determined by $T$ is $P \cup P ^ { \mathrm { o p p } }$ with $P$ as in the previous paragraph, but with the odd equatorial behavior.

The $( 1 0 , 1 0 , 0 )  ( 1 0 , 1 0 , 0 )$ mirror move is the only one for which the target IAS $^ 2$ satisfy $B / \iota \simeq \mathbb { R P } ^ { 2 }$ . There is no well-defined equatorial edge behavior since the edge is not fixed, and the sphere $B$ is built from Symington polytopes for $( \widehat { Y } , \widehat { D } )$ with a half-twist, as in Section $\mathrm { 8 E }$ .

The shape of the equator, and the fixed locus of $\iota _ { 0 }$ inside it, is depicted in Figure 13, in the respective positions of the mirror moves in Equation 6. In all cases, the equatorial behavior of $R _ { 0 }$ depicted is uniquely determined by the fact that the divisorial part of $R _ { 0 }$ must be the flat limit of $R _ { t }$ .

8G. Colliding singularities and non-generic type III models.
In the previous sections, we defined Kulikov models for the generic $\lambda$ . With the exception of Section 8D, the IAS $^ 2$ had 24 distinct $I _ { 1 }$ singularities: $2 \hat { k }$ of them lie on the equator, and $1 2 - k$ in the interior of each of the hemispheres $P$ , $P ^ { \mathrm { o p p } }$ in pairs, so that the whole collection is preserved by the involution $P  P ^ { \mathrm { o p p } }$ .

For a non-generic $\lambda$ and for the lattices with $\bar { g } \geq 2$ , some of these singularities collide to form integral-affine singularities of higher charge.

Each of the $I _ { 1 }$ singularities on the equator corresponds to a surface in the cbec of $( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } )$ and the ramification divisor is a line $L$ of volume $L ^ { 2 } = 1$ . Also, after a B-move, the M1 modifications convert each end $( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } )$ into $( \mathbb { F } _ { 1 } , D _ { 1 } + D _ { 2 } )$ with the ramification divisor a fiber, of volume $L ^ { 2 } = 0$ .

On the other hand, the off-equator $I _ { 1 }$ singularities correspond to surfaces with an empty ramification divisor, of volume 0. When singularities collide, the volumes add.
The anticanonical pairs of volume 0 get contracted on the stable models, which are described in Section 9B. This leads to three types of collisions:

(1) Collisions in the interiors of the hemispheres $P$ , $P ^ { \mathrm { o p p } }$ . These are completely irrelevant and can be avoided by nodal slides, replacing them by isolated $I _ { 1 }$ . The corresponding anticanonical pairs $( V _ { i } , D _ { i } )$ are disjoint from the $C _ { g }$ component of the ramification divisor $R$ , so on the stable model $V _ { i }$ will be contracted to points.

(2) Collisions obtained by descending pairs of $I _ { 1 }$ singularities to the equator.
These are only partly relevant: without further collisions, the curve $C _ { g }$ has numerical dimension 1 or $0$ on the corresponding pair $( V _ { i } , D _ { i } )$ . So on the stable model, $V _ { i }$ is contracted to $\mathbb { P } ^ { 1 }$ or a point and the collision is not detected by the stable model.

(3) The singularities obtained by colliding some of the $2 k$ $I _ { 1 }$ singularities on the equator, between themselves, or with some of the pairs of $I _ { 1 }$ singularities from case (2). These are truly relevant.
Each isolated $I _ { 1 }$ singularity on the equator corresponds to a pair $( V _ { i } , D _ { i } )$ in the cbec of $\left( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } \right)$ with a line and a conic, and the curve $C _ { g }$ restricts to this $\mathbb { P } ^ { 2 }$ as a line.
On the stable model, this $V _ { i }$ will not be contracted, mapping to a surface whose normalization is $\mathbb { P } ^ { 2 }$ . Further collisions lead to more complicated nontoric anticanonical pairs $( V _ { i } , D _ { i } )$ with big and nef $C _ { g }$ , and to more complicated irreducible components of the stable model.

Below, we work with the chamber $\mathfrak { C } _ { 2 }$ and its Coxeter diagram $\Gamma _ { 2 }$ . The translation between ${ \mathfrak { C } } _ { 2 }$ and $\mathfrak { C } _ { \mathrm { r } }$ and the elliptic subgraphs of $\Gamma _ { 2 }$ and $\Gamma _ { \mathrm { r } }$ is given by Eq. (3) and Fig. 2.

Definition 8.6. For any $\lambda \in \mathfrak { C } _ { 2 }$ define the subdiagram $\Gamma _ { 2 } ( \lambda ) \subset \Gamma _ { 2 }$ with the vertices

$$
V { \mathrm { 2 } } ( \lambda ) = \{ i \mid \ell _ { i } = 0 \} , \quad \mathrm { w h e r e } ~ \ell _ { i } = \lambda \cdot \alpha _ { i }
$$

Recall that for any . specifies the face of C2 to W belongs.
Further, by Section 4F, for a lattice $\overline { T }$ of genus $g$ the chamber ${ \mathfrak { C } } _ { 2 } ( T )$ is a face of the chamber ${ \mathfrak { C } } _ { 2 } ( { \overline { { T } } } _ { 1 } )$ for the “parent” lattice $\overline { { T } } _ { 1 } = \overline { { T } } \oplus A _ { 1 } ^ { \bar { g } - 1 }$ . Let $\Gamma _ { 2 } ^ { \mathrm { p a r } } ( \lambda ) \subset \Gamma _ { 2 } ( \overline { { T } } _ { 1 } )$ be the diagram of $\lambda$ considered as a vector in $\overline { { T } } _ { 1 }$ . With notations of Corollary 4.13 one has $\Gamma _ { 2 } ^ { \mathrm { p a r } } ( \lambda ) = \Gamma ( \lambda ) + A _ { 1 } ^ { g - 1 }$ , see Lemma 4.16.

By Eq. (2) in Section 3, if $\lambda ^ { 2 } > 0$ then $\Gamma _ { 2 } ^ { \mathrm { p a r } } ( \lambda )$ is elliptic, i.e. a disjoint union of $A D E$ diagrams.
As in Section 6G, these $A D E$ diagrams correspond to collections of visible curves connecting the $I _ { 1 }$ singularities.
We illustrate this in Fig. 14 showing a collision of type (2) that gives an $I _ { 2 }$ of charge $Q = 2$ and a collision of type (3) that gives $D _ { 5 }$ of charge $Q = 8$ .

The visible curves $( \gamma _ { i } , \alpha _ { i } )$ connecting the pairs of $I _ { 1 }$ singularities with the same monodromy directions are in a bijection with some of the simple roots $\alpha _ { i }$ of $\Gamma _ { 2 } ^ { \mathrm { p a r } }$ The corresponding lengths $\ell _ { i } = \lambda \cdot \alpha _ { i }$ measure the lattice distances between these $I _ { 1 }$ singularities.
A collision occurs when all of these distances become zero.

For each singularity of type (3) the divisor $C _ { g }$ on the corresponding anticanonical pair $( V , D )$ is big and nef, so $K _ { V } + D + \epsilon C _ { g }$ is big and nef.
Its canonical model $( \overline { { V } } , \overline { { D } } + \epsilon \overline { { C } } _ { g } )$ is one of the $A D E$ stable involution pairs which were completely classified in [AT21, Table 2]. The cbec of $( V , D )$ is the cbec of the minimal resolution of singularities of $( \overline { { V } } , \overline { { D } } )$ .

![](images/e7eea734d1c59fb6bea7cabdf0b307848affd35f673024c4a0e7a404e40143de.jpg)\
Figure 14. Colliding $I _ { 1 }$ singularities: $D _ { 5 }$ (charge = 8, volume $= 4$ ) and $A _ { 1 }$ (charge $= 2$ , volume $= 0$ )

[AT21] devised an elaborate system for denoting the $A D E$ surfaces using decorated Dynkin symbols.
For example the $D _ { 5 }$ singularity of Fig. 14 corresponds to ${ \mathit { \Delta } } ^ { \prime } { \mathit { D } } _ { 5 } ^ { - }$ of [AT21, Table 1]. Perhaps the easiest way to understand them is to look at the $A D E$ subgraphs of the Coxeter diagrams in Figs.
3, 4, while remembering the conversion rules of Eq. (3) and Fig. 2. Such a subgraph $G$ contains more information that just its $A D E$ type.
For example, an $A _ { n }$ subgraph can sit in $\Gamma _ { 2 }$ in many different ways: it may lie entirely in the equatorial $2 k$ -cycle, or one or two of its vertices may venture off-equator.
It may begin at a single-circled or a double-circled white vertex.
All of these possibilities correspond to different cbecs of anticanonical pairs with an involution.
But the decorated $A D E$ symbols specify them uniquely.

The most useful way to think of an $A D E$ subgraph $G \subset \Gamma _ { 2 }$ is as a chain in the equatorial $2 k$ cycle, plus some off-equator vertices each attached to an evennumbered equatorial, double-circled white vertex $\alpha _ { i }$ . For a given $\alpha _ { i }$ , the off-equator vertices $\beta _ { j }$ connected to it are disjoint from each other, cf.
Fig. 2.

With the singularities of $B = \Gamma ( X _ { 0 } )$ modeled by the cbecs of the corresponding $A D E$ surfaces of [AT21], the proof of Theorem 8.3 goes through, essentially unchanged.

8H. Type II models.
Type II degenerations correspond to monodromy vectors $\lambda \in \mathfrak { C } _ { 2 }$ with $\lambda ^ { 2 } = 0$ . On the mirror side, the line bundle $L \in { \widehat { S } }$ is nef but not big, $L ^ { 2 } = 0$ . Since the lattice area of $\mathrm { I A S ^ { 2 } }$ is $\lambda ^ { 2 } = L ^ { 2 }$ , the sphere degenerates to an interval, the dual complex of a Type II Kulikov model.
The limit of an IAS $^ 2$ $B = P \cup P ^ { \mathrm { o p p } }$ with an involution itself has an involution, so the interval is either vertical, going from one pole of the sphere to another, or horizontal.

The subgraph $\Gamma _ { 2 } ( \lambda )$ in this case is parabolic, a disjoint union of finitely many ${ \widetilde { A } } _ { n }$ , ${ \widetilde { D } } _ { n }$ , ${ \widetilde { E } } _ { n }$ extended Dynkin diagrams.
Just as in the previous section, the collisions are of types (1) irrelevant, (2) partly relevant but not changing the stable model, and (3) those that include some vertices on the $2 \hat { k }$ -cycle, which do affect the stable models.
The stable models for $( V _ { i } , D _ { i } , \epsilon C _ { g } )$ in this case are the $\widetilde A D E$ surfaces classified in [AT21] and $( V _ { i } , D _ { i } )$ are their resolutions to nonsingular pairs.

# 9. Compact moduli

We now restrict ourselves to the moduli spaces $F _ { S }$ for the 50 lattices $S$ of Fig. 1 for which $g \geq 2$ , excluding $( 1 0 , 8 , 0 )$ . In these cases the ramification divisor $R = X ^ { \iota }$ has a unique component $C _ { g }$ of genus $g \geq 2$ . If $X  { \overline { { X } } }$ is the contraction given by a linear system $| m C _ { g } |$ then the image $\overline { { C } } _ { g }$ of $C _ { g }$ is an ample Cartier divisor on $\overline { { X } }$ and the pair $( \overline { { X } } , \epsilon \overline { { C } } _ { g } )$ is a stable KSBA pair for $0 ~ < ~ \epsilon \ll 1$ , so one has the KSBA compactification as in Section $\mathrm { 2 E }$ . Recall that we denoted the main component $\overline { { F } } _ { S }$ and its normalization was the semitoric compactification $\overline { { \boldsymbol { F } } } ^ { \mathfrak { F } } =$ $( \overline { { F } } _ { S } ) ^ { \nu }$ by Proposition 8.1.

The goal of this section is to prove the Main Theorem 9.10. The proof is given in Section 9C. We begin by defining the semifans ${ \mathfrak { F } } _ { I } = { \mathfrak { F } } _ { \mathrm { r a m } } ( T )$ forming $\mathfrak { F }$ as one ranges over the 0-cusps $I = e ^ { \perp } / e$ . Then, we discuss stable models.

9A. The ramification semifan.
We use the same notations as in Section 3A. Let $H = \overline { { T } } = e _ { T } ^ { \perp } / e$ be the hyperbolic lattice corresponding to a 0-cusp of $F _ { S }$ . Let $\Gamma$ be its Coxeter diagram.

Recall that we defined the Coxeter semifan in Section 3B. We now define a generalized Coxeter semifan by the “Wythoff’s construction” of [Cox35]. We refer to [AET19, Sec. 10C] for details.

Divide the vertex set $V ( \Gamma )$ of the Coxeter diagram into two sets $V _ { \mathrm { r e l } } \sqcup V _ { \mathrm { i r r } }$ of relevant and irrelevant roots.
(It is important to understand that the “irrelevant” vertices are irrelevant only when in isolation.
They become relevant if they are connected to the relevant ones.)

Definition 9.1. Modulo $W$ , the fan $\mathfrak { F } _ { \mathrm { g e n } }$ has a unique maximal dimensional cone

$$
{ \mathfrak { C } } _ { \mathrm { g e n } } = \cup _ { w \in W _ { \mathrm { i r r } } } w . { \mathfrak { C } } , \quad { \mathrm { w h e r e ~ } } W _ { \mathrm { i r r } } = \langle w _ { i } \mid i \in V _ { \mathrm { i r r } } \rangle .
$$

All the other cones in $\mathfrak { F } _ { \mathrm { g e n } }$ are the faces of $\mathfrak { C }$ and their $W$ -translates.

Example 9.2. Consider the Coxeter fan for $W ( A _ { 2 } ) = S _ { 3 }$ in $\mathbb { R } ^ { 2 }$ , consisting of 6 two-dimensional cones and their faces.
If we take for $V _ { \mathrm { i r r } }$ one of the vertices of the $A _ { 2 }$ diagram then $\mathfrak { F } _ { \mathrm { g e n } }$ will be a fan with 3 two-dimensional cones and it is not a reflection fan.

$\mathfrak { F } _ { \mathrm { g e n } }$ has fewer cones than $\mathfrak { F }$ in the following sense:

Definition 9.3. Let $V ^ { \prime } \subset V ( \Gamma )$ be a subset of vertices and $\Gamma ^ { \prime } \subset \Gamma$ the induced subdiagram which is either elliptic or parabolic.
We divide $V ^ { \prime }$ into the relevant and irrelevant parts $\operatorname { r e l } ( V ^ { \prime } ) { \sqcup } \operatorname { i r r } ( V ^ { \prime } )$ as follows: the vertices of the connected components of $\Gamma ^ { \prime }$ that consist entirely of irrelevant vertices form $\mathrm { i r r } ( V ^ { \prime } )$ , and the rest is $\mathrm { r e l } ( V ^ { \prime } )$ . We say that $\mathrm { r e l } ( V ^ { \prime } )$ is the relevant content of $V ^ { \prime }$ .

Then the cone $F ^ { \prime }$ of $\mathfrak { F } _ { \mathrm { g e n } }$ defined by $V ^ { \prime }$ is the same as the one defined by its relevant content, and $F \cap \mathfrak { C }$ is the cone $F ( \mathrm { r e l } ( V ^ { \prime } ) )$ of $\mathfrak { F }$ . In particular, if $\operatorname { r e l } ( V ^ { \prime } ) = \emptyset$ then $V ^ { \prime }$ does not define any cone in ${ \mathfrak { F } } _ { \mathrm { g e n } }$ at all.

Remark 9.4. Let $W = W _ { \mathrm { r } }$ . If $V _ { \mathrm { i r r } } = \mathbb { B }$ is a subset of $V _ { 4 }$ as in Definition 3.2 then by Lemma 3.3 $\mathfrak { F } _ { \mathrm { g e n } }$ is simply the Coxeter semifan for the Weyl group $W _ { \mathrm { n o r } } ( \mathbb { B } ^ { c } )$ . But in our case the set $V _ { \mathrm { i r r } }$ is bigger than $V _ { 4 }$ , and $\mathfrak { F } _ { \mathrm { g e n } }$ is not a Coxeter semifan for any Weyl group.

Definition 9.5. Let $\overline { { T } } _ { 1 } = ( 1 0 + \bar { k } , 1 0 - \bar { k } , \bar { \delta } )$ , $1 \leq \bar { k } \leq 9$ be a lattice on the $\bar { g } = 1$ line and $\Gamma ( T _ { 1 } )$ be its Coxeter diagram as in Sections 3D, 3E. We declare the only relevant vertices $V _ { \mathrm { r e l } }$ to be the $2 \bar { k }$ vertices on the $I _ { 2 \bar { k } }$ cycle, and all the other vertices to be irrelevant.
In particular, all the black vertices are irrelevant.

Any other lattice $\overline { T }$ appearing as the target of a mirror move $S  T$ for $S$ with $g \geq 2$ is of the form $\overline { { { T } } } _ { \bar { g } } = ( 1 0 + \bar { k } - ( \bar { g } - 1 ) , 1 0 - \bar { k } - ( \bar { g } - 1 ) , \bar { \delta } )$ . By Corollary 4.13, it can be reached from $\overline { { T } } _ { 1 } = ( 1 0 + \bar { k } , 1 0 - \bar { k } , 1 )$ by a chain of $\bar { g } - 1$ standard operations described in Lemma 4.15, and the set of vertices of $\Gamma ( \overline { { T } } _ { \bar { g } } )$ is a subset of the vertices of $\Gamma ( \overline { { T } } _ { 1 } )$ We declare the vertices of $\Gamma ( \overline { { T } } _ { \bar { g } } )$ to be relevant if they were also relevant in $\Gamma ( \overline { { T } } _ { 1 } )$ . For $\bar { g } \geq 2$ there are $2 k - 1$ of them.

We define the semifan $\mathfrak { F } _ { \mathrm { r a m } } ( \overline { { T } } )$ to be the generalized Coxeter fan for this set $V _ { \mathrm { i r r } }$ of relevant vertices.
It is a coarsening of the reflection fan $\mathfrak { F } _ { 2 }$ for the $\left( - 2 \right)$ -roots: Walls of $\mathfrak { F } _ { 2 }$ get erased exactly when they are the perpendicular to an entirely irrelevant diagram.

9B. Stable models.
Let $X _ { 0 }$ be one of the Type III surfaces with an involution $\iota$ defined in Section 8A, $R$ the divisorial part of the fixed locus $X ^ { \iota }$ , and $C _ { g }$ the connected component of $R$ that has arithmetic genus $g \geq 2$ . In each case, we constructed a family $X _ { 0 }$ of such surfaces with an involution, parameterized by a translate of a torus.
After any necessary M1 modifications resulting from a B-move, see Section 8D, the limit of $C _ { g }$ is a big and nef divisor, and a large multiple $| m C _ { g } |$ defines a contraction $f \colon X _ { 0 } \to X _ { 0 }$ . Denote by $\overline { { C } } _ { g }$ the image of $C _ { g }$ , it is a Cartier divisor.
The pair $( \overline { { \boldsymbol { X } } } _ { 0 } , \epsilon \overline { { \boldsymbol { C } } } _ { g } )$ is a KSBA stable pair, see Section 2E.

Lemma 9.6. Let $X _ { 0 } ~ = ~ \cup V _ { i }$ with $V _ { i }$ corresponding to the lattice points of $B =$ $P \cup P ^ { \mathrm { o p p } }$ . Assume $\bar { g } = 1$ . Then under the morphism $f \colon X _ { 0 } \to X _ { 0 }$

(1) if i is in the interior of $P$ or $P ^ { \mathrm { o p p } }$ then $V _ { i }$ is contracted to a point, (2) if i is on the equator but not at a vertex of $P$ then $V _ { i }$ is contracted to $\mathbb { P } ^ { 1 }$ , (3) if i is a vertex of $P$ on the equator then $V _ { i }  \overline { { V } } _ { i }$ is birational.

Proof.
Indeed, by construction, these are the irreducible components of $X _ { 0 }$ on which $C _ { g }$ has numerical dimension 0, $1$ , 2, compare the description of the pairs $( V _ { i } , D _ { i } )$ of types (1), (2), (3) in Section 8G. $\boxed { \begin{array} { r l } \end{array} }$

Recall that a lattice $\overline { { { T } } } _ { \bar { g } } = ( 1 0 + \bar { k } - ( \bar { g } - 1 ) , 1 0 - \bar { k } - ( \bar { g } - 1 ) , \bar { \delta } )$ of genus $\bar { g } > 1$ is reached from $\overline { { T } } _ { 1 } = ( 1 0 + \bar { k } , 1 0 - \bar { k } , 1 )$ by a chain of $\bar { g } - 1$ standard operations described in Lemma 4.15. By the construction of Section 8D, if the mirror move $S  T$ is odd then the Kulikov surface for $\overline { { T } } _ { \bar { g } }$ is obtained from that of $\overline { { T } } _ { 1 }$ by a sequence of moves A. . . AA, and if $S \Rightarrow { \overline { { T } } }$ is even then it is by a sequence of moves A. . . AB. In either case, if $\bar { g } \geq 2$ then the $I _ { 2 \bar { k } }$ -cycle on the equator is broken and becomes a chain of length $2 k - 1$ .

Definition 9.7. Let ( $V , D = \sum D _ { j }$ ) be an anticanonical pair and $L$ be a big and nef divisor on $V$ . We say that an irreducible component $D _ { j }$ of $D$ is a short side if $L D _ { j } = 1$ , a long side if $L \cdot D _ { j } = 2$ , and a zero side if $L \cdot D _ { j } = 0$ . If $f \colon V \to { \overline { { V } } }$ is the contraction defined by $L$ and $L = f ^ { * } { \overline { { L } } }$ , then we say that the images $\overline { { D } } _ { j }$ of $D _ { j }$ are short or long sides of $\overline { V }$ if $\overline { { L } } \cdot \overline { { D } } _ { j } = 1$ or 2 respectively.

Definition 9.8. We define two types of stable models $X _ { 0 } = \cup _ { i } ( \overline { { V } } _ { i } , \overline { { D } } _ { i } , \epsilon \overline { { C } } _ { g , i } )$ , illustrated in Fig. 15.

(1) Pumpkin.
Each surface ${ \overline { { V } } } _ { i }$ has two sides $\overline { { D } } _ { i } = \overline { { D } } _ { i , \mathrm { l e f t } } + \overline { { D } } _ { i , \mathrm { r i g h t } }$ , they are glued in a circle, all of $D _ { i }$ meeting at the north and south poles.

![](images/d303ecb89e06377e3bd5edb245a1d234e9b1ea6521ef4c0a4a0dac28f71cf288.jpg)\
Figure 15. Pumpkin and smashed pumpkin type stable models

(2) Smashed pumpkin.
Starting with a surface of the pumpkin type, one short side is contracted to a point, so that the north and south poles are identified.

If the surface $V _ { i }$ , say to the left, is $\left( \mathbb { F } _ { 1 } , D _ { 1 } + D _ { 2 } \right)$ , where $D _ { 1 } \sim f$ is the short side being contracted, $D _ { 2 } \sim 2 s _ { 1 } + 2 f$ is the other side, and $C _ { g , i } \sim f$ on $V$ contract $V _ { i }$ by the $\mathbb { P } ^ { 1 }$ -fibration $V _ { i } \to { \mathbb { P } } ^ { 1 }$ . Then on the next surface $V _ { i - 1 }$ to the left the long side will fold $2 : 1$ to itself, creating a nonnormal singularity along that side.

If on $V _ { i }$ the divisor $C _ { g , i }$ has degree $C _ { g , i } ^ { 2 } \geq 2$ then only the short side is contracted and the resulting surface ${ \overline { { V } } } _ { i }$ is normal in codimension 1, with only two points in the normalization glued together (the poles).

Theorem 9.9. Let ( $\overline { { { X } } } _ { 0 } = \cup _ { i } \overline { { { V } } } _ { i } , \epsilon \overline { { { C } } } _ { g }$ ) be the stable model of a pair $X _ { 0 } = \cup _ { i } V _ { i } , \epsilon C _  g _  \it$ ), where $X _ { 0 }$ is a Type III Kulikov surface $X _ { 0 } = \cup V _ { i }$ and $C _ { g }$ is the component of genus $g \geq 2$ in the ramification divisor $R$ . Then the normalization of each ${ \overline { { V } } } _ { i }$ is an $A D E$ surface with an involution from [AT21, Table 2]. Moreover,

(1) If $\overline { T }$ is an odd 0-cusp of $F _ { S }$ then $\overline { { X } } _ { 0 }$ is of pumpkin type.\
(2) If $\overline { T }$ is an even 0-cusp of $F _ { S }$ then $\overline { { X } } _ { 0 }$ is of smashed pumpkin type.
The surfaces $V _ { i }$ of the last type in Definition 9.8, on which $V _ { i }  \overline { { V } } _ { i }$ contracts one side are the surfaces of [AT21, Table 2] for which one of the sides has length 0, i.e. those with a double prime or a “+”.

Proof.
By observation, these are the surfaces obtained by contracting the Kulikov models we constructed, defined by the big and nef divisor $C _ { g , i }$ on $V _ { i }$ . 

Figure 15 shows the maximally degenerate stable model $\overline { { X } } _ { 0 }$ and a less degenerate one.
The maximally degenerate surface corresponds to the empty subdiagram $V _ { 2 } ( \lambda ) = \emptyset$ .

In the pumpkin type it is a union of $2 k$ $\left( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } \right)$ with a short side (a line) and a long side (a conic).
Long, (resp.
short) sides correspond to the even-numbered, doubly circled (resp.
odd-numbered, singly circled) white vertices on the $2 k$ cycle in $\Gamma _ { 2 }$ .

In the smashed pumpkin type, $X _ { 0 }$ is a union of $2 k - 2$ components, $2 k - 4$ of them are isomorphic to $\left( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } \right)$ and the remaining two to $\left( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } \right)$ with a conic doubly folded on itself.

For nongeneric $\lambda$ , for each vertex on the equator that is included in $V _ { 2 } ( \lambda )$ , the corresponding side is smoothed out and removed from the picture.
For each offequator vertex in $V _ { 2 } ( \lambda )$ which is connected to some equatorial vertex in $V _ { 2 } ( \lambda )$ , the combinatorial type of the component ${ \overline { { V } } } _ { i }$ changes, since the charge of its minimal resolution increases.

9C. The Main Theorem.
We recall that in 50 of the 75 lattices of Fig. 1 for a generic surface $( X , \iota )$ in the moduli space $F _ { S }$ , the fixed locus $R = X ^ { \iota }$ has a component $C _ { g }$ of genus $g \geq 2$ . These are the lattices with $g \geq 2$ excluding $( 1 0 , 8 , 0 )$ .

Then $C _ { g }$ is big, nef, and semiample, and defines a contraction $X  { \overline { { X } } }$ to a K3 surface with $A D E$ singularities and an ample Cartier divisor $\overline { { C } } _ { g }$ . The KSBA theory (Section 2E) then provides a geometric compactification of $F _ { S }$ by adding stable pairs $( \overline { { X } } , \epsilon \overline { { C } } _ { g } )$ on the boundary.
We denoted by $\overline { { F } } _ { S }$ this closure.

Theorem 9.10. In the 50 cases of interest, the normalization of $\overline { { F } } _ { S }$ is semitoroidal, given by the collection of the semifans $\mathfrak { F } = \{ \mathfrak { F } _ { \mathrm { r a m } } ( \overline { { T } } ) \}$ defined in Section 9A, one for each 0-cusp $\overline { T }$ of $F _ { S }$ . It is dominated by the semitoroidal compactifications $\overline { { F } } _ { S } ^ { \mathfrak { F } _ { \mathrm { r } } }$ and $\overline { { F } } _ { S } ^ { \tilde { s } _ { 2 } }$ for the Coxeter semifans $\mathfrak { F } _ { \mathrm { r } } = \{ \mathfrak { F } _ { \mathrm { r } } ( T ) \}$ and $\mathfrak { F } _ { 2 } = \{ \mathfrak { F } _ { 2 } ( T ) \}$ .

For $S \neq ( 2 , 2 , 1 )$ or $( 3 , 3 , 1 )$ , $\overline { { F } } _ { S } ^ { \mathfrak { F } _ { \mathrm { r } } }$ is toroidal.
For $S$ with $k \geq 1$ , both $\overline { { F } } _ { S } ^ { \tilde { s } _ { 2 } }$ and F FrS a re toroidal.

Proof.
The first part follows from Proposition 8.1 and the description of the combinatorial type of the KSBA-stable limit, for each $\lambda \in \mathfrak { C } _ { 2 }$ described in Theorem 9.9: The combinatorial type changes whenever $\lambda$ degenerates into a cone with larger relevant content, since the number of double curves of the stable limit $\overline { { \boldsymbol X } } _ { 0 }$ decreases.
The semifan thus obtained is the semifan defined in Section 9A.

By Theorem 5.8, the 0-cusps of $F _ { S }$ correspond to the mirror moves $S \sim T$ . For each $\overline { T }$ , the semifan $\mathfrak { F } _ { \mathrm { r a m } } ( \overline { { T } } )$ is a coarsening of the Coxeter fan for the Weyl group $W _ { 2 }$ generated by the $\left( - 2 \right)$ -vectors, which is in turn a coarsening of the Coxeter fan for the full reflection group $W _ { \mathrm { r } }$ .

For the lattices $S$ with $g \geq 2$ , their mirrors $T$ are the 2-elementary lattices with $\bar { g } \geq 1$ and $k \geq 1$ , excluding $( 1 4 , 6 , 0 )$ . In all of these cases except for $\overline { { T } } = ( 1 8 , 2 , 1 )$ $( 1 7 , 3 , 1 )$ , n $\mathfrak { F } _ { \mathrm { r } }$ is a fan,ese cases these is tor $\overline { T }$ appear as mirror only for dal.
$S = ( 2 , 2 , 1 )$ and $( 3 , 3 , 1 )$ $\overline { { F } } _ { S } ^ { \mathfrak { F } _ { \mathrm { r } } }$

Similarly, for the lattices $S$ with $g \geq 1$ , the mirrors satisfy $\bar { g } \geq 2$ . Excluding the case $S = \overline { { T } } = ( 1 0 , 8 , 0 )$ , the Weyl group $W _ { 2 }$ has finite covolume (see Section 3C), so the Coxeter semifan for $W _ { 2 }$ is a fan.


Remark 9.11. From Definition 9.1, $\mathfrak { F } _ { \mathrm { r a m } } ( T )$ is a fan iff $W _ { \mathrm { r } }$ has finite covolume and the Weyl group generated by the irrelevant roots is finite, i.e. the complement of the relevant vertices forms an elliptic diagram.
(Indeed, this is equivalent to the polyhedron $P _ { \mathrm { r a m } } \subset \mathcal { H }$ for the cone $\mathfrak { C } _ { \mathrm { r a m } }$ having finite volume.)
One can go through the Coxeter diagrams in [AN06, Fig. 1] and Figs.
3, 4 to verify that this happens in rather few cases.
Heuristically, it is because there are many irrelevant nodes, as these are the complement of the $2 k$ -cycle in Figs.
3, 4.

# 10. Example.

$S = ( 2 , 2 , 0 )$ : hyperelliptic K3 surfaces of degree 4

Consider the moduli space $F _ { S }$ of K3 surfaces with the generic Picard lattice $S = ( 2 , 2 , 0 ) _ { 1 } = U ( 2 )$ . The K3 surfaces in this family are double covers of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ branched in a divisor $B \in | O ( 4 , 4 ) |$ . The pullback $L = \pi ^ { * } \mathcal { O } _ { \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 } } ( 1 , 1 )$ has degree $L ^ { 2 } = 4$ . These surfaces are known as hyperelliptic K3 surfaces of degree 4.

![](images/2c2d7486035646261cafa8a895391269f3c61076761943c2335af36f2cb5cf2a.jpg)\
Figure 16. Cusps for $T = ( 2 0 , 2 , 0 ) _ { 2 } = U \oplus U ( 2 ) \oplus E _ { 8 } ^ { 2 } = U ^ { 2 } \oplus D _ { 1 6 }$

The generic transcendental lattice is $T = S ^ { \perp } = ( 2 0 , 2 , 0 ) _ { 2 }$ . Explicitly, one has $T \simeq U \oplus U ( 2 ) \oplus E _ { 8 } ^ { 2 } \simeq U ^ { 2 } \oplus D _ { 1 6 }$ . The $0$ -cusps of $F _ { S }$ are found by Theorem 5.8. In Fig. 1 there are two mirror moves: the odd $S = ( 2 , 2 , 0 )  \overline { { { T } } } = ( 1 8 , 2 , 0 ) \simeq$ $U ( 2 ) \oplus E _ { 8 } ^ { 2 } \simeq U \oplus D _ { 1 6 }$ and the even ordinary $S = ( 2 , 2 , 0 ) \Rightarrow T = ( 1 8 , 0 , 0 ) \simeq U \oplus E _ { 8 } ^ { \prime }$ . The 1-cusps are given by Theorem 5.10. They correspond to the negative definite lattices $\overline { { \overline { { T } } } }$ with the invariants $( 1 6 , 0 , 0 ) _ { 0 }$ (i.e. unimodular) and $( 1 6 , 2 , 0 ) _ { 0 }$ . These are listed in Table 2. We give the complete cusp diagram in Fig. 16. (It can also be found in [LO21].) By Proposition 5.13, the 1-cusps for the $\overline { { \overline { { T } } } } ( 1 6 , 2 , 0 )$ lattices are isomorphic to $\mathbb { H } / \operatorname { S L } ( 2 , \mathbb { Z } )$ , and those for the $\overline { { \overline { { T } } } } ( 1 6 , 0 , 0 )$ lattices to $\mathbb { H } / \Gamma _ { 0 } ( 2 )$ .

Vinberg diagrams for $T = ( 1 8 , 2 , 0 )$ and $T = ( 1 9 , 1 , 1 )$ are given in Fig. 4. The diagram for $\overline { { T } } = ( 1 8 , 0 , 0 )$ is obtained from that of $( 1 9 , 1 , 1 )$ by the procedure given in Lemma 4.15; the result is the diagram of Fig. 18 (without the highlighting).
The 1-cusps containing a given 0-cusp correspond to the maximal parabolic subdiagrams in the Vinberg diagram.
They are highlighted in Figs.
17 and 18; the order of appearance is the same as in Fig. 16.

The Kulikov models are as described in Section 8: for $\overline { { T } } = ( 1 8 , 2 , 0 )$ in Section 8C and for $\overline { { T } } = ( 1 8 , 0 , 0 )$ in Section 8D. The stable models are given by Theorem 9.9.

![](images/b97e74e8b1db6cb247f42489b8dceaccd1a3e68e91509fc0828b3b942174b86d.jpg)\
Figure 17. Maximal parabolic subdiagrams in $\Gamma _ { r }$ for $T = ( 1 8 , 2 , 0 )$

![](images/270ab702b58294c4bf9154bfa47fd77f0a12e8dfdb3a568e75c17b1fe72f02bc.jpg)\
Figure 18. Maximal parabolic subdiagrams in $\Gamma _ { r }$ for $\overline { { T } } = ( 1 8 , 0 , 0 )$

At the $( 1 8 , 2 , 0 )$ odd 0-cusp the Type III stable models are of pumpkin type of Fig. 15. They correspond to the elliptic subdiagrams, i.e. disjoint unions of $A D E$ graphs in Fig. 17. The maximal degeneration corresponds to the empty subdiagram, or $( A _ { 0 } ^ { - } \bar { A } _ { 0 } ) ^ { 8 }$ . It is a union of 16 pairs $\left( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } \right)$ with a line $D _ { 1 }$ and a conic $D _ { 2 }$ , as in Fig. 15. The list of irreducible components that appear, in notations of [AT21, Table 2], is as follows.
We list them according to the number of the off-equator vertices.
For brevity, $m$ denotes an even index and $n$ an odd index.

$$
\begin{array} { r l } & { \mathrm {  ~ \lambda ~ } _ { n } \left( 1 \leq n \leq 1 5 \right) \quad A _ { m } ^ { - } \left( 0 \leq m \leq 1 4 \right) \quad \mathrm {  ~ \lambda ~ } _ { n } ^ { - } \left( 1 \leq n \leq 1 5 \right) } \\ & { \mathrm {  ~ \lambda ~ } _ { m } ^ { - } \left( 2 \leq m \leq 1 6 \right) \quad \mathrm {  ~ \lambda ~ } _ { M _ { n } } ^ { - } \left( 3 \leq n \leq 1 5 \right) \quad D _ { m } \left( 4 \leq m \leq 1 6 \right) } \\ & { D _ { n } ^ { - } \left( 5 \leq n \leq 1 5 \right) \quad - E _ { 6 } ^ { - } \quad - E _ { 7 } ^ { - } \quad - E _ { 8 } ^ { - } } \\ & { \mathrm {  ~ \lambda ~ } _ { n } ^ { \prime } \left( n = 7 , 1 1 , 1 5 \right) \quad D _ { n } ^ { \prime } \left( n = 9 , 1 3 , 1 7 \right) } \\ & { \mathrm {  ~ \lambda ~ } _ { 3 } ^ { \prime } \quad _ { D _ { m } } ^ { \prime } \left( 4 \leq m \leq 1 6 \right) \quad ^ { \prime } D _ { n } ^ { - } \left( 5 \leq n \leq 1 5 \right) } \\ & { \mathrm {  ~ \lambda ~ } _ { D _ { m } ^ { \prime } } ^ { \prime } \left( m = 8 , 1 2 , 1 6 \right) } \\ & { \mathrm {  ~ \lambda ~ } _ { 4 } ^ { \prime } } \end{array}
$$

At the $( 1 8 , 0 , 0 )$ even ordinary 0-cusp the Type III stable models are of smashed pumpkin type of Fig 15. They correspond to the elliptic subdiagrams in Fig. 18. In this case some of the irreducible components ${ \overline { { V } } } _ { i }$ are non-normal, with a long side folded $2 : 1$ . As in [AT21, Def. 6.9], we denote these by adding the letter $f$ to the

Dynkin symbol.
The maximal degeneration corresponds to the empty subdiagram, or $f _ { A _ { 0 } ^ { - } } ( \ ^ { - } A _ { 0 } A _ { 0 } ^ { - } ) ^ { 7 } \ ^ { - } A _ { 0 } ^ { f }$ . It is a union of 16 pairs $\left( \mathbb { P } ^ { 2 } , D _ { 1 } + D _ { 2 } \right)$ but in the end two of these pairs the $\mathbb { P } ^ { 2 }$ is glued to itself along the conic $D _ { 2 }$ which is folded $2 : 1$ . The list of irreducible components is as follows:

$$
\begin{array} { r l } &  \begin{array} { c c c c c c c } { + _ { A _ { n } ^ { - } } ( 1 \leq n \leq 1 5 ) } & { + _ { A _ { 1 7 } ^ { + } } } & { + _ { A _ { m } } ( 2 \leq m \leq 1 4 ) ) } & { \begin{array} { c c c c c } { f _ { A _ { 1 6 } ^ { + } } } & & & { } & & \\ { f _ { A _ { n } } ( 1 \leq n \leq 1 3 ) } & { f _ { A _ { 1 5 } ^ { + } } } & { f _ { A _ { m } ^ { - } } ( 0 \leq m \leq 1 4 ) } & & & \\ { - _ { A _ { n } ^ { - } } ( 1 \leq n \leq 1 3 ) } & { - A _ { m } ( 0 \leq m \leq 1 2 ) } & { A _ { n } ( 1 \leq n \leq 1 1 ) . } & & \\ { A _ { 4 } ^ { + } } & { \prime _ { A _ { 1 6 } ^ { + } } ^ { + } } & { f _ { A _ { 3 } ^ { \prime } } } & { f _ { A _ { 1 5 } ^ { \prime } } } & { \prime _ { A _ { m } } ( 2 \leq m \leq 1 4 ) } & { \prime A _ { n } ( 3 \leq n \leq 1 3 ) } & & \\ { D _ { 5 } ^ { + } } & { f _ { D _ { 1 7 } ^ { + } } } & { f _ { D _ { m } } ( 4 \leq m \leq 1 4 ) } & { f _ { D _ { n } } ( 5 \leq n \leq 1 5 ) } & { + _ { E _ { 6 } ^ { - } } } & { + _ { E _ { 7 } } } & { + _ { E _ { 8 } ^ { - } } } \end{array} } \end{array} \end{array}
$$

The Type II stable models are described by the maximal parabolic subdiagrams of Figs.
17, 18. The irreducible components correspond to the relevant connected components.

The normalization of $\overline { { F } } _ { S }$ is semitoroidal.
At the $( 1 8 , 2 , 0 )$ 0-cusp, the semifan $\mathfrak { F } _ { \mathrm { r a m } } ( 1 8 , 2 , 0 )$ is a coarsening of the Coxeter semifan $\mathfrak { F } _ { \mathrm { r } } ( 1 8 , 2 , 0 )$ and neither of them is a fan.
At the $( 1 8 , 0 , 0 )$ 0-cusp, a maximal-dimensional cone of the semifan $\mathfrak { F } _ { \mathrm { r a m } } ( 1 8 , 0 , 0 )$ is a union of 4 maximal-dimensional cones of $\mathfrak { F } _ { \mathrm { r } } ( 1 8 , 0 , 0 ) = \mathfrak { F } _ { 2 } ( 1 8 , 0 , 0 )$ , and both of them are fans, so near this cusp the normalization of $\overline { { F } } _ { S }$ is toroidal.

# References

[ABE22] Valery Alexeev, Adrian Brunyate, and Philip Engel, Compactifications of moduli of elliptic K3 surfaces: stable pair and toroidal, Geom.
and Topology 26 (2022), no. 8, 3525–3588, arXiv:2002.07127.\
[AE21] Valery Alexeev and Philip Engel, Compact moduli of K3 surfaces, Annals of Math., to appear (2021), arXiv:2101.12186.\
[AEH21] Valery Alexeev, Philip Engel, and Changho Han, Complete moduli of K3 surfaces with a nonsymplectic automorphism, Trans.
Amer.
Math.
Soc., to appear (2021), arXiv:2110.13834.\
[AET19] Valery Alexeev, Philip Engel, and Alan Thompson, Stable pair compactification of moduli of K3 surfaces of degree 2, J. Reine Angew.
Math., to appear (2019), arXiv:1903.09742.\
[AMRT75] A. Ash, D. Mumford, M. Rapoport, and Y. Tai, Smooth compactification of locally symmetric varieties, Math.
Sci.
Press, Brookline, Mass., 1975, Lie Groups: History, Frontiers and Applications, Vol. IV.\
[AN06] Valery Alexeev and Viacheslav V. Nikulin, Del Pezzo and K3 surfaces, MSJ Memoirs, vol. 15, Mathematical Society of Japan, Tokyo, 2006, arXiv:math/0406536.\
[AT21] Valery Alexeev and Alan Thompson, ADE surfaces and their moduli, J. Algebraic Geometry 30 (2021), 331–405, arXiv:1712.07932.\
[CD89] Fran¸cois R. Cossec and Igor V. Dolgachev, Enriques surfaces.
I, Progress in Mathematics, vol. 76, Birkh¨auser Boston, Inc., Boston, MA, 1989.\
[Cox35] H. S. M. Coxeter, Wythoff ’s Construction for Uniform Polytopes, Proc.
London Math.
Soc.
(2) 38 (1935), 327–339.\
[CS99] J. H. Conway and N. J. A. Sloane, Sphere packings, lattices and groups, third ed., Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 290, Springer-Verlag, New York, 1999, With additional contributions by E. Bannai, R. E. Borcherds, J. Leech, S. P. Norton, A. M. Odlyzko, R. A. Parker, L. Queen and B. B. Venkov.\
[DK07] Igor V. Dolgachev and Shigeyuki Kond¯o, Moduli of $_ { K 3 }$ surfaces and complex ball quotients, Arithmetic and geometry around hypergeometric functions, Progr.
Math., vol. 260, Birkh¨auser, Basel, 2007, pp. 43–100.\
[Dol96] I. V. Dolgachev, Mirror symmetry for lattice polarized K3 surfaces, J. Math.
Sci.
81 (1996), no. 3, 2599–2630, Algebraic geometry, 4.\
[EF21] Philip Engel and Robert Friedman, Smoothings and rational double point adjacencies for cusp singularities, J. Differential Geom.
118 (2021), no.

1. [Eng18] Philip Engel, Looijenga’s conjecture via integral-affine geometry, J. Differential Geom.
   109 (2018), no. 3, 467–495.\
   [FM83] Robert Friedman and Rick Miranda, Smoothing cusp singularities of small length, Math.
   Ann.
   263 (1983), no. 2, 185–212.\
   [Fri83] Robert Friedman, Global smoothings of varieties with normal crossings, Ann.
   of Math.
   (2) 118 (1983), no. 1, 75–114.\
   [FS86] Robert Friedman and Francesco Scattone, Type III degenerations of K3 surfaces, Invent.
   Math.
   83 (1986), no. 1, 1–39.\
   [GHK15] Mark Gross, Paul Hacking, and Sean Keel, Moduli of surfaces with an anti-canonical cycle, Compos.
   Math.
   151 (2015), no. 2, 265–291.\
   [GS03] Mark Gross and Bernd Siebert, Affine manifolds, log structures, and mirror symmetry, Turkish J. Math.
   27 (2003), no. 1, 33–60.\
   [Kim18] Yusuke Kimura, K3 surfaces without section as double covers of Halphen surfaces, and $F ^ { \prime }$ -theory compactifications, PTEP. Prog.
   Theor.
   Exp.
   Phys.
   (2018), no. 4, 043B06, 13.\
   [Kim20] $S U ( n ) \times \mathbb { Z } _ { 2 }$ in $F ^ { \prime }$ -theory on K3 surfaces without section as double covers of Halphen surfaces, Adv.
   Theor.
   Math.
   Phys.
   24 (2020), no. 2, 459–490.\
   [Kol23] J´anos Koll´ar, Families of varieties of general type, Cambridge Tracts in Mathematics, vol. 231, Cambridge University Press, Cambridge, 2023.\
   [Kon89] Shigeyuki Kond¯o, Algebraic K3 surfaces with finite automorphism groups, Nagoya Math.
   J. 116 (1989), 1–15.\
   [KS06] Maxim Kontsevich and Yan Soibelman, Affine structures and non-Archimedean analytic spaces, The unity of mathematics, Progr.
   Math., vol. 244, Birkh¨auser Boston, Boston, MA, 2006, arXiv: math.AG/0406564, pp. 321–385.\
   [Kul77] Vik.
   S. Kulikov, Degenerations of $_ { K 3 }$ surfaces and Enriques surfaces, Izv.
   Akad.
   Nauk SSSR Ser.
   Mat.
   41 (1977), no. 5, 1008–1042, 1199.\
   [LO21] Radu Laza and Kieran O’Grady, GIT versus Baily-Borel compactification for K3’s which are double covers of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ , Adv.
   Math.
   383 (2021), Paper No. 107680, 63.\
   [Loo03] Eduard Looijenga, Compactifications defined by arrangements.
   II. Locally symmetric varieties of type IV, Duke Math.
   J. 119 (2003), no. 3, 527–588.\
   [MP86] Rick Miranda and Ulf Persson, On extremal rational elliptic surfaces, Math.
   Z. 193 (1986), no. 4, 537–558.\
   [Nik79a] V. V. Nikulin, Integer symmetric bilinear forms and some of their geometric applications, Izv.
   Akad.
   Nauk SSSR Ser.
   Mat.
   43 (1979), no. 1, 111–177, 238.\
   [Nik79b] Quotient-groups of groups of automorphisms of hyperbolic forms of subgroups generated by 2-reflections, Dokl.
   Akad.
   Nauk SSSR 248 (1979), no. 6, 1307–1309.\
   [Nik81] Quotient-groups of groups of automorphisms of hyperbolic forms by subgroups generated by 2-reflections.
   Algebro-geometric applications, Current problems in mathematics, Vol. 18, Akad.
   Nauk SSSR, Vsesoyuz.
   Inst.
   Nauchn.
   i Tekhn.
   Informatsii, Moscow, 1981, pp. 3–114.\
   [Nik20] Viacheslav V. Nikulin, Some examples of K3 surfaces with infinite automorphism group which preserves an elliptic pencil, Math.
   Notes 108 (2020), no. 3-4, 542–549.\
   [OS91] Keiji Oguiso and Tetsuji Shioda, The Mordell-Weil lattice of a rational elliptic surface, Comment.
   Math.
   Univ. St. Paul.
   40 (1991), no. 1, 83–99.\
   [Per90] Ulf Persson, Configurations of Kodaira fibers on rational elliptic surfaces, Math.
   Z. 205 (1990), no. 1, 1–47.\
   [PP81] Ulf Persson and Henry Pinkham, Degeneration of surfaces with trivial canonical bundle, Ann.
   of Math.
   (2) 113 (1981), no. 1, 45–66.\
   [Sca87] Francesco Scattone, On the compactification of moduli spaces for algebraic K3 surfaces, Mem.
   Amer.
   Math.
   Soc.
   70 (1987), no. 374, x+86.\
   [Sym03] Margaret Symington, Four dimensions from two in symplectic topology, Topology and geometry of manifolds (Athens, GA, 2001), Proc.
   Sympos.
   Pure Math., vol. 71, Amer.
   Math.
   Soc., Providence, RI, 2003, pp. 153–208.\
   [Vin72] E. B. Vinberg, \` The groups of units of certain quadratic forms, Mat.
   Sb.
   (N.S.) 87(129) (1972), 18–36.\
   [Vin75] E. B. Vinberg, \` Some arithmetical discrete groups in Lobaˇcevski˘ı spaces, Discrete subgroups of Lie groups and applications to moduli (Internat.
   Colloq., Bombay, 1973), Oxford Univ. Press, Bombay, 1975, pp. 323–348.\
   [Vin83] E. B. Vinberg, \` The two most algebraic K3 surfaces, Math.
   Ann.
   265 (1983), no. 1, 1–21.\
   [VK78] E. B. Vinberg and I. M. Kaplinskaja, \` The groups ${ \cal O } _ { 1 8 , 1 } ( Z )$ and $O _ { 1 9 , 1 } ( Z )$ , Dokl.
   Akad.
   Nauk SSSR 238 (1978), no. 6, 1273–1275.\
   [Zan20] Aline Zanardini, Explicit constructions of Halphen pencils, Preprint (2020), arXiv:2008.08128.

# List of Figures

1 Hyperbolic 2-elementary K3 lattices $( r , a , \delta )$ 5

2 Conversion: $B _ { n } ( 2 ) \to A _ { 1 } ^ { n }$ $n = 2 , 3$ ), $C _ { 3 }  A _ { 3 }$ , $F _ { 4 } \to D _ { 4 }$ 10

3 Coxeter diagrams for lattices on the $g = 1$ line, part 1 12

4 Coxeter diagrams for lattices on the $g = 1$ line, part 2 13

5 The local behavior along the equator of the Kulikov model for a degeneration of $( 1 0 + k , 1 0 - k , \delta )$ . 37

6 Surgery to make IAS $^ 2$ into $P \cup P ^ { \mathrm { o p p } }$ 38

7 Moment polytopes for $\widehat { S } = ( 1 2 , 6 , 1 )$ 39

8 An integral-affine sphere associated to an ample class in $\widehat { S } = ( 1 2 , 6 , 1 )$ 39

9 A Kulikov surface $X _ { 0 }$ for $\widehat { S } = ( 1 2 , 6 , 1 )$ 43

10 Equatorial behavior: even vs odd 45

11 Kulikov models for the $\bar { g } = 1$ case 46

12 A- and B-moves 48

13 The fixed loci in circular equators, shown in red, and the corresponding edge behavior.
50

14 Colliding $I _ { 1 }$ singularities 52

15 Pumpkin and smashed pumpkin type stable models 55

16 Cusps for $T = ( 2 0 , 2 , 0 ) _ { 2 } = U \oplus U ( 2 ) \oplus E _ { 8 } ^ { 2 } = U ^ { 2 } \oplus D _ { 1 6 }$ 57

17 Maximal parabolic subdiagrams in $\Gamma _ { r }$ for $\overline { { T } } = ( 1 8 , 2 , 0 )$ 58

18 Maximal parabolic subdiagrams in $\Gamma _ { r }$ for $\overline { { T } } = ( 1 8 , 0 , 0 )$ 58

# List of Tables

Special rational elliptic surfaces $Y$ 1

2 Negative definite 2-elementary lattices 24

Email address: mailto:valery@uga.edu\
Department of Mathematics, University of Georgia, Athens GA 30602, USA Email address: mailto:philip.engel@uga.edu\
Department of Mathematics, University of Georgia, Athens GA 30602, USA
