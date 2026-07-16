---
title: Moduli of K3 surfaces and irreducible symplectic manifolds
authors:
- Gritsenko
- K.
year: 2013
bibkey: GHS10
tags:
- paper
- extraction
abstract: |
  The name “K3 surfaces” was coined by A.
  Weil in 1957 when he formulated a research programme for these surfaces and their moduli.
  Since then, irreducible holomorphic symplectic manifolds have been introduced as a higher dimensional analogue of K3 surfaces.
  In this paper we present a review of this theory starting from the definition of K3 surfaces and going as far as the global Torelli theorem for irreducible holomorphic symplectic manifolds as recently proved by M.
  Verbitsky.
  
  For many years the last open question of Weil’s programme was that of the geometric type of the moduli spaces of polarised K3 surfaces.
  We explain how this problem has been solved.
  Our method uses algebraic geometry, modular forms and Borcherds automorphic products.
  We collect and discuss the relevant facts from the theory of modular forms with respect to the orthogonal group $\mathrm { O } ( 2 , n )$ .
  We also give a detailed description of quasi pull-back of automorphic Borcherds products.
  This part contains previously unpublished results.
---

# Moduli of K3 Surfaces and Irreducible Symplectic Manifolds

V. Gritsenko, K. Hulek and G.K. Sankaran

# Abstract

The name “K3 surfaces” was coined by A. Weil in 1957 when he formulated a research programme for these surfaces and their moduli.
Since then, irreducible holomorphic symplectic manifolds have been introduced as a higher dimensional analogue of K3 surfaces.
In this paper we present a review of this theory starting from the definition of K3 surfaces and going as far as the global Torelli theorem for irreducible holomorphic symplectic manifolds as recently proved by M. Verbitsky.

For many years the last open question of Weil’s programme was that of the geometric type of the moduli spaces of polarised K3 surfaces.
We explain how this problem has been solved.
Our method uses algebraic geometry, modular forms and Borcherds automorphic products.
We collect and discuss the relevant facts from the theory of modular forms with respect to the orthogonal group $\mathrm { O } ( 2 , n )$ . We also give a detailed description of quasi pull-back of automorphic Borcherds products.
This part contains previously unpublished results.

# Contents

1 Introduction 2

2 Periods of K3 surfaces and the Torelli theorem 4

3 Irreducible symplectic manifolds 15

4 Projective models 24

5 Compactifications 26

6 Modular forms and Kodaira dimension 39

7 Orthogonal groups and reflections 46

8 The quasi pull-back of modular forms 51

9 Arithmetic of root systems 59

# 1 Introduction

The history of K3 surfaces goes back to classical algebraic geometry.
In modern complex algebraic geometry a $K \mathcal { 3 }$ surface is a compact complex surface $S$ whose canonical bundle is trivial, i.e. $K _ { S } \cong \mathcal { O } _ { S }$ , and whose irregularity $q ( S ) = h ^ { 1 } ( S , { \mathcal { O } } _ { S } ) = 0$ . These two facts immediately imply that $H ^ { 0 } ( { \cal S } , \Omega _ { \cal S } ^ { 1 } ) = H ^ { 0 } ( { \cal S } , T _ { \cal S } ) = H ^ { 2 } ( { \cal S } , T _ { \cal S } ) = 0$ .

The easiest examples of algebraic K3 surfaces are smooth quartic surfaces in $\mathbb { P } ^ { 3 }$ . Further examples are complete intersections of type $( 2 , 3 )$ in $\mathbb { P } ^ { 4 }$ and of type $( 2 , 2 , 2 )$ in $\mathbb { P } ^ { 5 }$ . Another classical example is the Kummer surfaces, i.e. the (desingularised) quotient of a 2-dimensional torus $A$ by the involution $\iota \colon x \mapsto - x$ .

The modern name “K3 surface” was coined by A. Weil in his famous “Final report on research contract AF 18(603)-57” [Wei, Vol II, pp 390– 395]. In his comments on this report [Wei, Vol II, p 546] Weil writes: “Dans la seconde partie de mon rapport, il s’agit des vari´et´es k¨ahl´eriennes dites K3, ainsi nomm´ees en l’honneur de Kummer, Kodaira, K¨ahler et de la belle montagne K2 au Cachemire.”

In that report the following conjectures, due to Andreotti and Weil, were stated:

(i) K3 surfaces form one family;\
(ii) all K3 surfaces are K¨ahler;\
(iii) the period map is surjective;\
(iv) a form of global Torelli theorem holds.

Weil also remarked that the structure of the moduli space of (polarised) K3 surfaces must be closely related to the theory of automorphic forms.

By now all of these questions have been answered positively and much progress has been made in understanding the moduli spaces of K3 surfaces.
Conjecture (i) was proved by Kodaira [Kod, Part I, theorem 19]. Conjecture (ii) was first shown by Siu [Siu, Section 14]. Nowadays it can be derived from the more general theorem, due to Buchdahl and Lamari, that a compact complex surface is K¨ahler if and only if its first Betti number is even ([BHPV, Theorem IV.3.1], [Bu],[La]). Surjectivity of the period map (conjecture (iii)) was proved for special K3 surfaces in various papers by Shah [Sha1], [Sha2], [Sha3] and by Horikawa [Hor1]. Kulikov [Kul] gave a proof for projective K3 surfaces, with some points clarified by Persson and Pinkham [PP]. The general result for K¨ahler K3 surfaces was proved by Todorov [Tod] and Looijenga [Lo]. The strong Torelli theorem (i.e. conjecture (iv)) for algebraic K3 surfaces was first proved by Piatetskii-Shapiro and Shafarevich [P-SS] with amendments by Rapoport and Shioda.
It was proved for K¨ahler K3 surfaces (and hence for all) by Burns and Rapoport [BR]. A detailed and supplemented account of the original proof was written by Looijenga and Peters [LP]. Finally, Friedman [Fr] gave a proof using degenerations.

It should be noted, though, that Weil’s definition of K3 surface was different from the standard definition used nowadays.
For him a surface was K3 if its underlying differentiable structure was that of a quartic surface in $\mathbb { P } ^ { 3 }$ . Using results from Seiberg-Witten theory one can indeed show that any compact complex surface diffeomorphic to a quartic is a K3 surface.

The crucial ingredient is the fact that the plurigenera of a compact complex surface are invariant under orientation preserving diffeomorphism: see [BHPV, Theorem IX.9.4 and Theorem IX.9.5]. This was formulated as a question in [OV, p. 244] and became known as the Van de Ven conjecture.
A first (partial) proof of this was published by Brussee [Br] (see also [FM]), and an elegant argument using Seiberg-Witten invariants can be found in D¨urr’s thesis [D¨u]. It follows that the only surfaces which admit an orientation preserving diffeomorphism to a quartic are K3 surfaces or possibly tori, but the latter are excluded because they are not simply connected.
If a surface is diffeomorphic to a quartic surface, but with an orientation changing diffeomorphism, then its signature is $^ { - 1 6 }$ and its Euler number equals $c _ { 2 } ( S ) = 2 4 $ . By the Thom-Hirzebruch index theorem $c _ { 1 } ^ { 2 } ( S ) = 9 6$ , but that contradicts the Miyaoka-Yau inequality, so such a surface cannot exist.

Moduli spaces of polarised K3 surfaces are a historically old subject, studied by the classical Italian geometers (starting with the spaces of double sextics and plane quartics in $\mathbb { P } ^ { 3 }$ ). Mukai extended the classical constructions and unirationality results for the moduli spaces ${ \mathcal { F } } _ { 2 d }$ parametrising polarised K3 surfaces of degree $2 d$ to many more cases, going as high as $d = 1 9$ . See [Mu1], [Mu2], [Mu3], [Mu4] and [Mu5] for details.
Kondo [Ko1] proved that the moduli spaces ${ \mathcal { F } } _ { 2 p ^ { 2 } }$ are of general type for sufficiently large prime numbers $p$ , but without giving an effective bound.
Finally, it was shown in [GHS1] that the moduli spaces $\mathcal { F } _ { 2 d }$ are of general type for $d > 6 1$ and $d = 4 6 , 5 0 , 5 4 , 5 7 , 5 8 , 6 0$ , and later it was noticed by A. Peterson [PeSa] that this proof also works for $d = 5 2$ : see Theorem 6.1 below.
For an account of these results see also Voisin’s Bourbaki expos´e [Vo1].

In higher dimension K3 surfaces can be generalised in two ways, namely to Calabi-Yau varieties or to irreducible symplectic manifolds (or hyperk¨ahler manifolds).
In fact, together with tori, these three classes of manifolds are the building blocks of all compact K¨ahler manifolds with trivial first Chern class (over $\mathbb { R }$ ), also called Ricci flat manifolds: every such manifold admits a finite ´etale cover which is a product of tori, Calabi-Yau manifolds and irreducible symplectic manifolds (see [Be], [Bog2]). The first examples of irreducible symplectic manifolds, by now regarded as classical, were studied by Beauville in [Be], namely the Hilbert schemes of points on K3 surfaces and generalised Kummer varieties (and their deformations).
Two further classes of examples were later found by O’Grady [OG1], [OG2]. The theory of irreducible symplectic manifolds, which started from work of Bogomolov,

Beauville and Fujiki, was significantly advanced by Huybrechts [Huy1] who, among other results, proved surjectivity of the period map.
It was noticed early on by Debarre [Deb] and Namikawa [Nam] that the obvious generalisations of the Torelli theorem are false.
Nevertheless, one can use the period map to exhibit moduli spaces of polarised irreducible symplectic manifolds as dominant finite to one covers of quotients of type IV domains by arithmetic groups.
This was used in [GHS5] and [GHS6] to obtain general type results for many of these moduli spaces (Theorem 6.2 and Theorem 6.3 below).

Very recently Verbitsky [Ver] has announced a Torelli theorem for irreducible symplectic manifolds.
The consequences of Verbitsky’s result for the moduli problem of polarised irreducible symplectic manifolds were worked out in detail by Markman [Mar4]. We also refer the reader to Huybrecht’s forthcoming Bourbaki talk [Huy2].

The theory of K3 surfaces and irreducible symplectic manifolds is a fascinating and vast subject.
We have started this introduction by giving the definition of K3 surfaces in complex geometry (which also allows for nonalgebraic surfaces).
The notion of K3 surface also makes perfect sense in algebraic geometry over arbitrary fields: a K3 surface is an irreducible smooth algebraic surface $S$ defined over a field $k$ with trivial canonical bundle and irregularity $q = h ^ { 1 } ( S , { \mathcal { O } } _ { S } ) = 0$ . In this article we shall, however, concentrate on the theory over the complex numbers, and especially on moduli problems.
We are fully aware that we thus exclude a large area of interesting questions.
Concerning K3 surfaces in positive characteristic we refer the reader to the papers by Artin [Ar], Ogus [Ogu] and Nygaard [Nyg] for a first introduction.
Another aspect, which we will not touch upon, is the arithmetic of K3 surfaces.
An introduction to this field can be found in Sch¨utt’s survey paper [Sch].

In this article we mainly survey known results.
Theorem 8.11 is new, however (special cases occur in the literature) and so is Proposition 9.2.

# 2 Periods of K3 surfaces and the Torelli theorem

In this section we will discuss the period domain and the period map for K3 surfaces, and the local and global Torelli theorems.
The case of K3 surfaces presents several special features and the existence of a straightforward global Torelli theorem is one of them.

# 2.1 Lattices

Let $S$ be a K3 surface.
By Noether’s formula $b _ { 2 } ( S ) = 2 2$ , and since $S$ is simply connected (being diffeomorphic to a quartic hypersurface), $H ^ { 2 } ( S , \mathbb { Z } )$ is a free $\mathbb { Z }$ -module of rank 22. The intersection form defines a non-degenerate symmetric bilinear form on $H ^ { 2 } ( S , \mathbb { Z } )$ , giving it the structure of a lattice, which has signature $( 3 , 1 9 )$ by the Hodge index theorem.
As the intersection form is even and unimodular, this lattice is, independently of the surface $S$ the $K \mathcal { 3 }$ lattice

$$
L _ { \mathrm { K 3 } } : = 3 U \oplus 2 E _ { 8 } ( - 1 )
$$

where $U$ is the hyperbolic plane (the unique even unimodular lattice of signature $( 1 , 1 )$ ) and $E _ { 8 }$ is the unique even unimodular positive definite rank 8 lattice.
For any lattice $L$ and $m \in \mathbb { Z }$ , the notation $L ( m )$ indicates that the quadratic form is multiplied by $m$ , so $E _ { 8 } ( - 1 )$ is negative definite.

It was proven by Siu [Siu] that every K3 surface is K¨ahler.
Today, it is known that a compact complex surface is K¨ahler if and only if its first Betti number is even [BHPV, Theorem IV.3.1], which immediately implies Siu’s result.
Hence $H ^ { 2 } ( S , \mathbb { C } )$ has a Hodge decomposition

$$
H ^ { 2 } ( S , \mathbb { C } ) = H ^ { 2 , 0 } ( S ) \oplus H ^ { 1 , 1 } ( S ) \oplus H ^ { 0 , 2 } ( S ) .
$$

Since $K _ { S } \cong \mathcal { O } _ { S }$ it follows that $H ^ { 2 , 0 } ( S ) = H ^ { 0 } ( S , K _ { S } )$ is 1-dimensional and thus $H ^ { 1 , 1 } ( S )$ has dimension 20.

Since the second cohomology has no torsion we can, via the universal coefficient theorem, consider $H ^ { 2 } ( S , \mathbb { Z } )$ as a lattice in $H ^ { 2 } ( S , \mathbb { C } )$ . The N´eronSeveri group is the intersection $\mathrm { N S } ( S ) = H ^ { 2 } ( S , \mathbb { Z } ) \cap H ^ { 1 , 1 } ( S )$ , which, in this case, coincides with the Picard group $\mathrm { P i c } ( S )$ . The transcendental lattice is defined as the smallest lattice whose complexification contains a generator $\omega$ of $H ^ { 0 } ( S , K _ { S } )$ . If the intersection pairing on $\mathrm { N S } ( S )$ is nondegenerate, e.g. if $S$ is projective, then $T ( S )$ is the orthogonal complement in $H ^ { 2 } ( S , \mathbb { Z } )$ of the N´eron-Severi group.

Note that for a general K3 surface $S$ we have no algebraic classes, i.e. $T ( S ) = H ^ { 2 } ( S , \mathbb { Z } )$ . The Picard number $\rho ( S )$ of $S$ is the rank of the N´eronSeveri group $\mathrm { N S } ( S )$ .

For future use we also need the K¨ahler cone of a K3 surface, which is the cone of classes of K¨ahler $( 1 , 1 )$ -forms.
This lives in $H ^ { 1 , 1 } ( S , \mathbb { R } ) \ =$ $H ^ { 1 , 1 } ( S ) \cap H ^ { 2 } ( S , \mathbb { R } )$ . The restriction of the intersection product to $H ^ { 1 , 1 } ( S , \mathbb { R } )$ has signature $( 1 , 1 9 )$ . Let

$$
\mathcal { C } _ { S } \subset \{ x \in H ^ { 1 , 1 } ( S , \mathbb { R } ) \mid ( x , x ) > 0 \}
$$

be the connected component that contains one (and hence all) K¨ahler classes.\
This is called the positive cone of $S$ .

A class in $H ^ { 2 } ( S , \mathbb { Z } )$ is called effective if it is represented by an effective divisor.
By a nodal class we mean the class $\delta$ of an effective divisor $D$ of self-intersection $D ^ { 2 } = - 2$ . We denote by $\Delta$ the set of all nodal classes.
Every nodal class $\delta \in \Delta$ defines a reflection

$$
s _ { \delta } \colon H ^ { 2 } ( S , \mathbb { Z } ) \to H ^ { 2 } ( S , \mathbb { Z } )
$$

given by $s _ { \delta } ( x ) = x + ( x , \delta ) \delta$ and called the Picard-Lefschetz reflection defined by $\delta$ . We shall denote the $\mathbb { R }$ - and $\mathbb { C }$ -linear extensions of $s \delta$ by the same symbol.
Clearly $s \delta$ is the reflection in the hyperplane $H _ { \delta }$ orthogonal to $\delta$ . The set of effective classes on $S$ is the semi-group generated by the integral points in the closure of $\mathit { \mathcal { C } } _ { S }$ and the nodal classes.
The connected components of the set $\mathcal { C } _ { S } \setminus \bigcup _ { \delta \in \Delta } H _ { \delta }$ are called the chambers of $\mathit { \mathcal { C } } _ { S }$ . The chamber

$$
{ \mathcal { C } } _ { S } ^ { + } = \{ x \in { \mathcal { C } } _ { S } \mid ( x , \delta ) > 0 { \mathrm { ~ f o r ~ a l l ~ e f f e c t i v e ~ } } \delta \in \Delta \}
$$

is equal to the K¨ahler cone of $S$ according to [BHPV, Corollary VIII.3.9].

# 2.2 Markings and the period map

A marking of a K3 surface is an isometry $\phi \colon H ^ { \cdot 2 } ( S , \mathbb { Z } ) \to L _ { \mathrm { K 3 } }$ and we refer to a pair $( S , \phi )$ as a marked K3 surface.
An isomorphism between marked K3 surfaces is an isomorphism between the surfaces that commutes with the markings.
If $\omega$ is a non-zero 2-form on $S$ then $\mathbb { C } \phi ( \omega ) = \phi ( H ^ { 2 , 0 } ( S ) )$ is a line in the complex vector space $L _ { \mathrm { K 3 } } \otimes \mathbb { C }$ .

For any indefinite lattice $L$ we define

$$
\Omega _ { L } = \{ [ x ] \in \mathbb { P } ( L _ { \mathrm { K 3 } } \otimes \mathbb { C } ) \mid ( x , x ) = 0 , ( x , \bar { x } ) > 0 \} .
$$

In the case of the K3 lattice, $\Omega = \Omega _ { L _ { \mathrm { K 3 } } }$ is a connected complex manifold of dimension 20, called the period domain of $K \mathcal { 3 }$ surfaces.
Since $( \omega , \omega ) = 0$ and $( \omega , \bar { \omega } ) > 0$ it follows that $[ \phi ( \omega ) ] \in \Omega$ . This is the period point of the marked K3 surface $( S , \phi )$ .

Let $p \colon S  U$ be a flat family of K3 surfaces over some sufficiently small contractible open set $U$ . If $\phi _ { 0 } \colon H ^ { 2 } ( S _ { 0 } , \mathbb { Z } ) \to L _ { \mathrm { K 3 } }$ is a marking then this can be extended to a marking $\phi _ { U } \colon R ^ { 2 } p _ { * } \mathbb { Z } _ { U } \ \to \ ( L _ { \mathrm { K 3 } } ) _ { U }$ where $( L _ { \mathrm { K 3 } } ) _ { U }$ is the constant sheaf with fibre $L _ { \mathrm { K 3 } }$ on $U$ . This defines a holomorphic map $\pi _ { U } \colon U \to \{ 2$ , called the period map defined by the family $p \colon S  U$ .

# 2.3 The Torelli theorem

The Torelli problem asks how much information about an algebraic variety can be reconstructed from its Hodge structure.
In the case of K3 surfaces this means whether one can recover a K3 surface $S$ from a period point.
This question can be made precise in different ways.
As we shall see, one can prove a very strong form of the Torelli theorem in the case of K3 surfaces.

We start by discussing the local Torelli theorem.
For this let $p \colon S  U$ be a representative of the Kuranishi family (or versal deformation) of $S$ . Since $H ^ { 0 } ( S , T _ { S } ) = H ^ { 2 } ( S , T _ { S } ) = 0$ the base space of the Kuranshi family is smooth of dimension $h ^ { 1 } ( S , T _ { S } ) = h ^ { 1 , 1 } ( S ) = 2 0$ . Choosing any marking of the central fibre of the Kuranishi family defines a marking for the entire family (we shall choose $U$ sufficiently small and contractible) and hence a period map $\pi \colon U  \Omega$ .

Theorem 2.1 (Local Torelli) The base space of the Kuranishi family is smooth of dimension 20. It is universal for all points in a sufficiently small neighbourhood of the origin.
The differential of the period map is an isomorphism and thus the period map is a local isomorphism.

Proof.
See [BHPV, Theorem VIII.7.3].

In order to discuss the global Torelli theorem we need the notion of Hodge isometry.
Let $S$ and $S ^ { \prime }$ be K3 surfaces.
An isomorphism of $\mathbb { Z }$ -modules $\Phi \colon H ^ { \cdot 2 } ( S , \mathbb { Z } ) \to H ^ { \cdot 2 } ( S ^ { \prime } , \mathbb { Z } )$ is called a Hodge isometry if it is an isometry and if its $\mathbb { C }$ -linear extension $\Phi _ { \mathbb { C } } \colon H ^ { 2 } ( S , \mathbb { C } ) \to H ^ { 2 } ( S ^ { \prime } , \mathbb { C } )$ preserves the Hodge decomposition.
It is moreover called effective if it maps $\mathit { \Delta } \mathit { \mathcal { C } } _ { S }$ to $\mathcal { C } _ { S } ^ { \prime }$ and maps effective classes to effective classes.

Proposition 2.2 Let $S$ and $S ^ { \prime }$ be K3 surfaces.
Then the following are equivalent for a Hodge isometry $\Phi \colon H ^ { \cdot 2 } ( S , \mathbb { Z } ) \to H ^ { \cdot 2 } ( S ^ { \prime } , \mathbb { Z } )$ :

(i) $\Phi$ is effective,\
(ii) $\Phi ( { \mathcal { C } } _ { S } ^ { + } ) \subset { \mathcal { C } } _ { S ^ { \prime } } ^ { + }$ , i.e. $\Phi$ maps the K¨ahler cone of $S$ into that of $S ^ { \prime }$ .\
(iii) $\Phi$ maps one element of the K¨ahler cone of $S$ into the K¨ahler cone of the surface $S ^ { \prime }$ .

Proof.
See [BHPV, Proposition VIII.3.11].

The crucial result for the theory of moduli of K3 surfaces is the following.

Theorem 2.3 (Strong Torelli) Let $S$ and $S ^ { \prime }$ be two K3 surfaces and suppose $\Phi \colon H ^ { \cdot 2 } ( S ^ { \prime } , \mathbb { Z } ) \to H ^ { \cdot 2 } ( S , \mathbb { Z } )$ is an effective Hodge isometry.
Then there is a unique isomorphism $f \colon S  S ^ { \prime }$ that induces $\Phi$ , i.e. such that $\Phi = f ^ { * }$ .

A proof of this theorem can be found in [BHPV, Sections VIII.7–VIII.11]. Very roughly speaking the idea is to prove the Torelli theorem for projective Kummer surfaces first.
The second step then consists of showing that the period points of marked Kummer surfaces are dense (in the complex topology) in the period domain $\Omega$ . The final step is then to prove the Torelli theorem for all K3 surfaces by approximating them by Kummer surfaces and taking suitable limits in the Barlet topology.

The following weaker form of the Torelli theorem is still useful.

Theorem 2.4 (Weak Torelli theorem) Two K3 surfaces $S$ and $S ^ { \prime }$ are isomorphic if and only if there is a Hodge isometry $H ^ { 2 } ( S ^ { \prime } , \mathbb { Z } ) \to H ^ { 2 } ( S , \mathbb { Z } )$ .

Proof.
Assume that $\Phi \colon H ^ { 2 } ( S ^ { \prime } , \mathbb { Z } ) \to H ^ { 2 } ( S , \mathbb { Z } )$ is a Hodge isometry.
Let $W _ { S }$ be the group of isometries of $H ^ { 2 } ( S , \mathbb { Z } )$ generated by the Picard-Lefschetz reflections.
This group acts on the positive cone $\mathcal { C } _ { S }$ properly discontinuously.

The closure of the K¨ahler cone in the positive cone is a fundamental domain for this action (cf.
[BHPV, Proposition VIII.3.10]). Hence we can choose an element $w \in W _ { S }$ such that for a suitable choice of sign $\pm w \circ \Phi$ is an effective Hodge isometry by Proposition 2.2 and thus is induced by an isomorphism $f \colon S  S ^ { \prime }$ by Theorem 2.3. ✷

# 2.4 The universal family of marked K3 surfaces

For each K3 surface $S$ we choose a representative $p \colon S  U$ of the Kuranishi family with $U$ contractible and sufficiently small such that the following hold:

(i) $p \colon S  U$ is the Kuranishi family for each point $s \in U$ . (ii) If $\phi \colon R ^ { 2 } p _ { * } \mathbb { Z } _ { S }  ( L _ { \mathrm { K 3 } } ) _ { U }$ is a marking, then the associated period map $\pi \colon U  \Omega$ is injective.

We consider all marked Kuranishi families, i.e. pairs $( p \colon S \to U , \phi )$ ), having the above properties.
We can glue the various copies of $U$ by identifying those points where the marked K3 surfaces are isomorphic.
This defines a space $M _ { 1 }$ all of whose points have neighbourhoods isomorphic to some $U$ . Hence $M _ { 1 }$ is a 20-dimensional analytic manifold, but possibly not Hausdorff.
It is also possible to show (cf.
[BHPV, Theorem VIII.10.6]) that one can glue the Kuranishi families to obtain a global family of K3 surfaces over $M _ { 1 }$ .

It turns out that the space $M _ { 1 }$ is indeed not Hausdorff.
This follows from an example due to Atiyah, also referred to as Atiyah’s flop and nowadays crucial in higher-dimensional birational geometry.
Consider, for example, the following 1-parameter family $S _ { t }$ of quartic (and hence K3) surfaces in $\mathbb { P } ^ { 3 }$ , which is given in affine coordinates by

$$
x ^ { 2 } ( x ^ { 2 } - 2 ) + y ^ { 2 } ( y ^ { 2 } - 2 ) + z ^ { 2 } ( z ^ { 2 } - 2 ) = 2 t ^ { 2 } .
$$

Let the parameter $t$ vary in a small neighbourhood $B$ of the origin.
For $t \neq 0$ these surfaces are smooth, whereas the surface $S _ { 0 }$ has an ordinary double point at $( 0 , 0 , 0 )$ . This is also the only singularity, again an ordinary double point, of the total space $\boldsymbol { S }$ . Blowing up this node one obtains a smooth 3-fold $\tilde { s }$ which contains a quadric $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ as exceptional divisor $E$ . The proper transform $\hat { S } _ { 0 }$ of $S _ { 0 }$ is a smooth K3 surface intersecting the exceptional divisor $E$ in a rational curve of bidegree $( 1 , 1 )$ . This is a nodal curve on $\hat { S } _ { 0 }$ . The two rulings on $E$ can each be contracted giving rise to smooth 3-dimensional spaces $p _ { 1 } \colon S _ { 1 } \to B$ and $p _ { 2 } \colon S _ { 2 } \to B$ . These families are by construction identical over $B \backslash 0$ . They are, however, not identical over all of $B$ , since the identity on ${ \cal S } \backslash { \cal S } _ { 0 }$ would, otherwise, have to extend to an automorphism of the total space acting non-trivially on the tangent cone of the double point, which is clearly impossible.
Now choose a marking for $p _ { 1 }$ . This also defines a marking for $p _ { 2 }$ . Since the families coincide outside the origin, the period maps $\pi _ { 1 }$ and $\pi _ { 2 }$ also coincide away from 0. However, the markings differ for the central fibre (namely by the Picard-Lefschetz reflection defined by the nodal curve on $\hat { S } _ { 0 }$ ). This shows that $M _ { 1 }$ cannot be Hausdorff.
In fact all non-Hausdorff behaviour comes from the existence of different resolutions of double points in families: see [BR, Theorem $1 ^ { \prime }$ and Section 7].

There is another formulation of the Torelli theorem, which we will now describe.
For this we consider

$$
\begin{array} { r } { K \Omega = \left\{ \left( \kappa , \left[ \omega \right] \right) \in \left( L _ { \mathrm { K 3 } } \otimes \mathbb { R } \right) \times \Omega \mid \left( \kappa , \mathrm { R e } ( \omega ) \right) = \left( \kappa , \mathrm { I m } ( \omega ) \right) = 0 , \left( \kappa , \kappa \right) > 0 \right\} } \end{array}
$$

and define $E ( \kappa , \omega )$ as the oriented 3-dimensional space spanned by the ordered basis $\{ \kappa , \operatorname { R e } ( \omega ) , \operatorname { I m } ( \omega ) \}$ . By mapping each point $\left( \kappa , [ \omega ] \right)$ to the space $E ( \kappa , \omega )$ we obtain a fibration

$$
\Pi \colon K \Omega  \operatorname { G r } ^ { + } ( 3 , L _ { \mathrm { K 3 } } \otimes \mathbb { R } )
$$

over the Grassmannian $\mathrm { G r } ^ { + } ( 3 , L _ { \mathrm { K 3 } } \otimes \mathbb { R } )$ of oriented 3-planes in $L _ { \mathrm { K 3 } } \otimes \mathbb { R }$ on which the form $\left( \begin{array} { l l l } { \mathbf { \epsilon } } & { \mathbf { \gamma } , } & { \mathbf { \gamma } } \end{array} \right)$ is positive definite.
This is an ${ \mathrm { S O } } ( 3 , \mathbb { R } )$ -fibre bundle and the projection $\Pi$ is equivariant with respect to the action of the orthogonal group $\operatorname { A u t } ( L _ { \mathrm { K 3 } } \otimes \mathbb { R } ) \cong \operatorname { O } ( 3 , 1 9 )$ . We define

$$
( K \Omega ) ^ { \cup } : = \{ ( \kappa , [ \omega ] ) \in K \Omega \mid ( \kappa , d ) \neq 0 \mathrm { ~ f o r ~ } d \in L _ { \mathrm { K } 3 } , ( d , d ) = - 2 , ( \omega , d ) = 0 \}
$$

This is an open subset of $K \Omega$ .

For every point $\omega \in \Omega$ we consider the cone

$$
C _ { \omega } = \{ x \in L _ { \mathrm { K 3 } } \otimes \mathbb { R } \mid ( x , \omega ) = 0 , ( x , x ) > 0 \} .
$$

This has two connected components and varies differentiably with $\omega$ . Since $\Omega$ is connected and simply connected, we can globally choose one of these components, say $C _ { \omega } ^ { + }$ . Let $( S , \phi )$ be a marked K3 surface and let $\kappa \in H ^ { 1 , 1 } ( S , \mathbb { R } )$ be a K¨ahler class.
Then we say that $( S , \kappa )$ , or more precisely $( ( S , \phi ) , \kappa )$ , is a marked pair if $\phi _ { \mathbb { C } } ( \kappa ) \in C _ { \omega } ^ { + }$ , where $\omega$ is the period point defined by $( S , \phi )$ .

Let $M _ { 2 } ^ { \prime }$ be the real analytic vector bundle with fibre $H ^ { 1 , 1 } ( S _ { t } )$ over the base $M _ { 1 }$ of the universal family of marked K3 surfaces and let $M _ { 2 } \subset M _ { 2 } ^ { \prime }$ be the subset of K¨ahler classes.
This is open by [KS, Theorem 15]. In particular, $M _ { 2 }$ is real analytic of dimension $6 0 = 4 0 + 2 0$ , where 40 is the real dimension of the base $M _ { 1 }$ and 20 is the dimension of the fibre.
We can now define a real-analytic map

$$
\pi _ { 2 } \colon M _ { 2 } \to ( K \Omega ) ^ { 0 }
$$

by mapping $\kappa \in H ^ { 1 , 1 } ( S _ { t } ) , t \in M _ { 1 }$ to $\pi _ { 2 } ( \kappa ) = ( \phi _ { \mathbb { C } } ( \kappa ) , \pi ( t ) )$ . This is called the refined period map.
In this way we obtain the obvious commutative diagram

$$
\begin{array} { l c c } { { M _ { 2 } } } & { { \xrightarrow { \pi _ { 2 } } } } & { { ( K \Omega ) ^ { 0 } } } \\ { { \Big \downarrow } } & { { } } & { { \Big \downarrow } } \\ { { M _ { 1 } } } & { { \pi _ { 1 } } } & { { \Big \downarrow } } \end{array}
$$

The Torelli theorem can now be reformulated as follows.

Theorem 2.5 The map $\pi _ { 2 }$ is injective (and thus $M _ { 2 }$ is Hausdorff).

Using this one can finally prove that the period map is surjective.

Theorem 2.6 (Surjectivity of the period map) The refined period map $\pi _ { 2 }$ is surjective.
In particular, every point of $\Omega$ appears as the period point of some marked K3 surface.

Proof.
This is proven in [BHPV, Section VIII.14].

The surjectivity of the period map was one of the major questions in the theory of K3 surfaces.
A. Todorov [Tod] was the first to give a proof; the argument given in [BHPV] is due to Looijenga.

In view of Theorem 2.4 and Theorem 2.6 we now have

Theorem 2.7 The set $\mathrm { O } ( L _ { \mathrm { K 3 } } ) \backslash \Omega$ is in $1 : 1$ correspondence with the set of isomorphism classes of K3 surfaces.

We can thus think of $\mathrm { O } ( L _ { \mathrm { K 3 } } ) \backslash \Omega$ as the “moduli space of K3 surfaces”.
It must be pointed out, however, that the action of the group O( $L _ { \mathrm { K 3 } }$ ) is not well behaved.
In particular, it is not properly discontinuous.
We shall now turn to the case of polarised K3 surfaces where we shall see that the situation is much better.

# 2.5 Moduli spaces of polarised K3 surfaces

A polarisation on a K3 surface is an ample line bundle $\mathcal { L }$ . Since the irregularity of K3 surfaces is 0 and the Picard group has no torsion we can identify a line bundle $\mathcal { L }$ with its first Chern class $h = c _ { 1 } ( \mathcal { L } ) \in H ^ { 2 } ( S , \mathbb { Z } )$ . An ample line bundle $\mathcal { L }$ is nef and big, and conversely a nef and big line bundle on a K3 surface is ample if there are no $\left( - 2 \right)$ -curves $C$ with $h . C = 0$ . This can be seen from the description of the K¨ahler cone (2) and Nakai’s criterion, or from Reider’s theorem [BHPV, Theorem IV.11.4] or from [S-D]. Throughout, we shall only consider primitive polarisations, i.e. we shall assume that the class $h$ is non-divisible in the K3 lattice.
The degree of a polarisation is $\deg ( \mathcal { L } ) = h ^ { 2 } = 2 d$ . Note that the degree is always even.

We denote by $\langle - 2 d \rangle$ the rank 1 lattice whose generator has square $- 2 d$

K3 the orthogonal complement Lh = h⊥LK3 Lemma 2.8 Suppose is a primitive vector with of $h$ is isometric to $h ^ { 2 } = 2 d > 0$ $L _ { 2 d }$ , where . Then $L _ { 2 d }$ , the lattice $L _ { 2 d }$ associated with K3 surfaces with a polarisation of degree $2 d$ , is defined by

$$
L _ { 2 d } = 2 U \oplus 2 E _ { 8 } ( - 1 ) \oplus \langle - 2 d \rangle .
$$

Proof.
It follows from Eichler’s criterion (see Lemma 7.5 and Example 7.6 below) that there is a unique $\mathrm { O } ( L _ { \mathrm { K 3 } } )$ -orbit of primitive vectors $h$ of given degree in the K3 lattice $L _ { \mathrm { K 3 } } = 3 U \oplus 2 E _ { 8 } ( - 1 )$ . Hence we can assume that $h$ is in one of the copies of the hyperbolic plane and that $h = e + d f$ where $e$ , $f$ are a basis of a copy of $U$ with $e ^ { 2 } = f ^ { 2 } = 0$ and $( e , f ) = 1$ . The structure of $L _ { h }$ is clear in this case.
✷

The lattice $L _ { 2 d }$ is an even lattice of signature $( 2 , 1 9 )$ . The period domain $\Omega _ { 2 d } = \Omega _ { L _ { 2 d } }$ has two connected components, $\mathcal { D } _ { 2 d }$ and $\mathcal { D } _ { 2 d } ^ { \prime }$ , interchanged by complex conjugation.
The domain $\mathcal { D } _ { 2 d }$ is a 19-dimensional symmetric homogeneous domain of type IV: see [Sat, Appendix 6]. One can also describe $\Omega _ { 2 d }$ as the intersection of the domain $\Omega$ with the hyperplane $h _ { L _ { \mathrm { K 3 } } } ^ { \perp }$ .

We shall fix $\textit { h } \in \ . \boldsymbol { L } _ { \mathrm { K 3 } }$ once and for all.
For each polarised K3 surface $( S , { \mathcal { L } } )$ of degree $2 d$ we can consider polarised markings, i.e. markings $\phi \colon H ^ { 2 } ( S , \mathbb { Z } ) \to L _ { \mathrm { K 3 } }$ with $\phi ( c _ { 1 } ( \mathcal { L } ) ) = h$ . Any two such markings differ by an element in the group

$$
\operatorname { O } ( L _ { \mathrm { K 3 } } , h ) = \{ g \in \operatorname { O } ( L _ { \mathrm { K 3 } } ) \mid g ( h ) = h \} .
$$

This group leaves the orthogonal complement $L _ { 2 d }$ of $h$ invariant and hence is a subgroup of $\mathrm { O } ( L _ { 2 d } )$ .

For any lattice $L$ we denote by $L ^ { \vee } = \operatorname { H o m } ( L , \mathbb { Z } )$ its dual lattice.
The discriminant group $D ( L ) = L ^ { \vee } / L$ is a finite abelian group of order $| \operatorname* { d e t } L |$ and carries a discriminant quadratic form $q L$ (if $L$ is even) and a discriminant bilinear form $b _ { L }$ , with values in $\mathbb { Q } / 2 \mathbb { Z }$ and $\mathbb { Q } / \mathbb { Z }$ respectively (see [Nik2, Section 1.3]). The stable orthogonal group of an even lattice $L$ is defined as the kernel

$$
\widetilde { \mathrm { O } } ( L ) = \ker ( \mathrm { O } ( L ) \to \mathrm { O } ( D ( L ) ) .
$$

If $L$ is indefinite, the subgroup $\mathrm { O } ^ { + } ( L )$ is defined to be the group of elements of real spinor norm 1 (see [GHS4] for a definition of the real spinor norm).
We define

$$
\widetilde { \boldsymbol { 0 } } ^ { + } ( L ) = \widetilde { \boldsymbol { 0 } } ( L ) \cap \boldsymbol { 0 } ^ { + } ( L )
$$

and generally, for any subgroup $G < \mathrm { O } ( L )$ , we use $G ^ { + }$ to denote the kernel of the real spinor norm and $\widetilde { G }$ to denote the stable subgroup, the kernel of $G \to \operatorname { O } ( D ( L ) )$ .

For $h \in L _ { \mathrm { K 3 } }$ with $h ^ { 2 } = 2 d$ , it follows from Nikulin’s theory [Nik2, Corollary 1.5.2] that

$$
\mathrm { O } ( L _ { \mathrm { K 3 } } , h ) = \widetilde { \mathrm { O } } ( L _ { 2 d } )
$$

considered as subgroups of $\mathrm { O } ( L _ { 2 d } )$ . The two connected components $\mathcal { D } _ { 2 d }$ and $\mathcal { D } _ { 2 d } ^ { \prime }$ are interchanged by the group $\mathrm { O } ( L _ { 2 d } )$ . The index 2 subgroup that fixes the components is $\mathrm { O } ^ { + } ( L _ { 2 d } )$ . Finally we define

$$
\mathcal { F } _ { 2 d } = \widetilde { \mathrm { O } } ( L _ { 2 d } ) \backslash \Omega _ { 2 d } = \widetilde { \mathrm { O } } ^ { + } ( L _ { 2 d } ) \backslash \mathcal { D } _ { 2 d } .
$$

It is important to note that the situation is much better here than in the non-polarised case.
The reason lies in the change of signature which is now $( 2 , 1 9 )$ rather than $( 3 , 1 9 )$ . We are thus dealing with locally symmetric hermitian domains and, as a result, the action of the group O( $L _ { 2 d }$ ) on $\Omega _ { 2 d }$ is properly discontinuous.
Hence the quotient space of $\Omega _ { 2 d }$ by any subgroup of $\mathrm { O } ( L _ { 2 d } )$ of finite index (i.e. an arithmetic subgroup) is a complex space with only finite quotient singularities (also sometimes called a $V$ -manifold).
By a famous result of Baily and Borel [BB] these quotients are quasi-projective and thus carry a natural structure of an algebraic variety.
We shall discuss various compactifications of these quasi-projective varieties below in Section 5.

In order to describe the moduli space of polarised K3 surfaces we need one more ingredient.
For $h \in L _ { \mathrm { K 3 } }$ we define

$$
\Delta _ { h } = \{ \delta \in L _ { \mathrm { K 3 } } \mid \delta ^ { 2 } = - 2 , ( \delta , h ) = 0 \} .
$$

For each $\delta \in \Delta _ { h }$ we define the hyperplane $H _ { \delta } = \delta _ { L _ { \mathrm { K 3 } } } ^ { \perp }$ , i.e. the hyperplane fixed by the Picard-Lefschetz reflection defined by $\delta$ . We set

$$
\Omega _ { 2 d } ^ { 0 } = \Omega _ { 2 d } \backslash \bigcup _ { \delta \in \Delta _ { h } } \left( H _ { \delta } \cap \Omega _ { 2 d } \right) .
$$

There are only finitely many $\widetilde { \mathrm { O } } ( L _ { 2 d } )$ -orbits in $\Delta _ { h }$ . This follows immediately from Lemma 7.5, below: in fact there are at most two orbits by [GHS3, Proposition 2.4(ii)]. Since the group acts properly discontinuously on $\Omega$ , the hyperplanes $H _ { \delta }$ for $\delta \in \Delta _ { h }$ form a locally finite collection.
Clearly, the action of the group $\widetilde { \mathrm { O } } ( L _ { 2 d } )$ on $\Omega _ { 2 d }$ restricts to an action on $\Omega _ { 2 d } ^ { 0 }$ . We define

$$
\mathcal { F } _ { 2 d } ^ { 0 } = \widetilde { \mathrm { O } } ( L _ { 2 d } ) \backslash \Omega _ { 2 d } ^ { 0 } .
$$

Note that this is again a quasi-projective variety (it arises from ${ \mathcal { F } } _ { 2 d }$ by removing finitely many divisors) with only finite quotient singularities.

Theorem 2.9 The variety $\mathcal { F } _ { 2 d } ^ { 0 }$ is the moduli space of polarised K3 surfaces of degree $2 d$ , i.e. its points are in $1 : 1$ correspondence with polarised K3 surfaces of degree $2 d$ .

Proof.
Let $( S , { \mathcal { L } } )$ be a polarised K3 surface with $\deg ( \mathcal { L } ) = 2 d$ . We consider polarised markings $\phi \colon H ^ { \cdot 2 } ( S , \mathbb { Z } )  L _ { \mathrm { K 3 } }$ with $\phi ( c _ { 1 } ( \mathcal { L } ) ) \ = \ h$ . Since $( \omega _ { S } , c _ { 1 } ( \mathcal { L } ) ) = 0$ we find that $\phi ( \omega _ { S } ) \in \Omega _ { 2 d }$ . In fact, since $\mathcal { L }$ is ample it has positive degree on all $\left( - 2 \right)$ -curves and hence $\phi ( \omega _ { S } )$ lies in $\Omega _ { 2 d } ^ { 0 }$ . Any two polarised markings differ by an element in $\mathrm { O } ( L _ { \mathrm { K 3 } } , h ) = \widetilde { \mathrm { O } } ( L _ { 2 d } )$ and hence we obtain a well-defined map which associates to an isomorphism class $( S , { \mathcal { L } } )$ a point in $\mathcal { F } _ { 2 d } ^ { 0 }$ . This map is injective: assume that a point in $\mathcal { F } _ { 2 d } ^ { 0 }$ arises from two polarised surfaces $( S , { \mathcal { L } } )$ and $( S ^ { \prime } , { \mathcal { L } } ^ { \prime } )$ . Then there exists a Hodge isometry $H ^ { 2 } ( S ^ { \prime } , \mathbb { Z } ) \to H ^ { 2 } ( S , \mathbb { Z } )$ mapping the ample class $c _ { 1 } ( \mathcal { L } ^ { \prime } )$ to $c _ { 1 } ( \mathcal { L } )$ . It then follows from the strong Torelli Theorem (Theorem 2.3) that this map is induced by an isomorphism $( S , \mathcal { L } ) \cong ( S ^ { \prime } , \mathcal { L } ^ { \prime } )$ . Thus we get an injective map from the set of isomorphism classes of degree $2 d$ polarised K3 surfaces into $\mathcal { F } _ { 2 d } ^ { 0 }$ . Finally, the surjectivity of this map follows from the surjectivity of the period map, Theorem 2.6. ✷

In the literature one often finds references to $\mathcal { F } _ { 2 d }$ as the moduli space of polarised K3 surfaces.
One can interpret the points in the complement of $\mathcal { F } _ { 2 d } ^ { 0 }$ as weakly- or semi-polarised K3 surfaces, i.e. $\mathcal { L }$ has positive degree and is nef, but not ample, as it has degree 0 on some nodal class(es).
Alternatively, one can consider ample line bundles on K3 surfaces with rational double points.
There is still a version of the strong Torelli theorem for weakly polarised K3 surfaces due to D. Morrison [Mo], but the precise formulation is subtle.
For purposes of the birational geommatter whether one works with ${ \mathcal { F } } _ { 2 d }$ of these spaces,or its open part $\mathcal { F } _ { 2 d } ^ { 0 }$ obviously does not.

The notion of polarised K3 surfaces was generalised by Nikulin [Nik1] to that of lattice-polarised K3 surfaces: see also Dolgachev’s paper [Do] for a concise account, in particular in connection with mirror symmetry.
To describe this, we fix a lattice $M$ of signature $( 1 , t )$ , which we assume can be embedded primitively into the K3-lattice $L _ { \mathrm { { K 3 } } }$ . The cone $V _ { M } = \{ x \in M _ { \mathbb { R } } \ \vert$ $( x , x ) > 0 \}$ has two connected components: we fix one and denote it by $\mathcal { C } _ { M }$ . Let

$$
\Delta _ { M } = \{ d \in M \mid ( d , d ) = - 2 \}
$$

and choose a decomposition $\Delta _ { M } = \Delta _ { M } ^ { + } \cup ( - \Delta _ { M } ^ { + } )$ . Moreover let

$$
\mathcal { C } _ { M } ^ { + } = \{ h \in V ( M ) ^ { + } \cap M \mid ( h , d ) > 0 \mathrm { ~ f o r ~ a l l ~ } d \in \Delta _ { M } ^ { + } \} .
$$

An $M$ -polarised K3 surface is then a pair $( S , j )$ where $S$ is a K3 surface and $j \colon M \hookrightarrow \operatorname { P i c } ( S )$ is a primitive embedding.
An isomorphism between $M$ - polarised K3 surfaces is an isomorphism between the surfaces that commutes with the primitive embeddings.
If $\omega$ is a non-zero 2-form on We call $( S , j )$ ample (or pseudo-ample), if $j ( \mathcal { C } _ { M } ^ { + } )$ contains an ample (or pseudo-ample) class.
The classical case of polarised K3 surfaces is the case where $t = 0$ and $M = \langle 2 d \rangle$ .

The theory of moduli of polarised K3 surfaces carries over naturally to lattice polarised K3 surfaces.
For this, one has to consider the domain $\Omega _ { M } = \{ \omega \in \Omega \mid ( w , M ) = 0 \}$ and the group ${ \mathrm { O } } ( L _ { \mathrm { K 3 } } , M )$ of orthogonal transformations of the K3 lattice which fixes $M$ . The role of the variety ${ \mathcal { F } } _ { 2 d }$ is then taken by the quotient

$$
\mathcal { F } _ { M } = \mathrm { O } ( L _ { \mathrm { K 3 } } , M ) \backslash \Omega _ { M } .
$$

Lattice polarised K3 surfaces play a role in mirror symmetry.
For this we consider admissible lattices, i.e. lattices $M$ which admit an embedding

$j \colon M \hookrightarrow L _ { \mathrm { K 3 } }$ such that

$$
M _ { L _ { \mathrm { K 3 } } } ^ { \perp } \cong U ( m ) \oplus { \widetilde { M } } .
$$

The choice of such a splitting determines a primitive embedding $\widetilde { \jmath } \colon \widetilde { M } \hookrightarrow$ $L _ { \mathrm { { K 3 } } }$ . The lattice $\widetilde { M }$ is hyperbolic: more precisely, its signature is $( 1 , 1 8 - t )$ . The variety ${ \mathcal { F } } _ { \widetilde { M } }$ is then a mirror family to ${ \mathcal { F } } _ { M }$ . There are more ingredients to the concept of mirror symmetry which we will not describe here, such as the Yukawa coupling and the mirror map.
For details we refer to [Do]: see also [GN4], [GN5].

Finally, we want to comment on the relationship between the construction of moduli spaces of K3 surfaces as quotients of homogeneous domains and GIT constructions.
By Viehweg’s results [Vi] moduli spaces of polarised varieties with trivial canonical bundle exist and can be constructed as GIT quotients.
For this we first fix a Hilbert polynomial $P ( m )$ of a line bundle on a K3 surface.
This is of the form $P ( m ) = m ^ { 2 } d + 2$ where the degree of the line bundle is $2 d$ . Let $\mathcal { M } _ { 2 d }$ be the GIT moduli space of degree $2 d$ polarised K3 surfaces.
We want to relate this to ${ \mathcal { F } } _ { 2 d }$ .

We first note that for any ample line bundle $\mathcal { L }$ on a K3 surface $S$ its third power $\mathcal { L } ^ { \otimes 3 }$ is very ample.
For this, see [S-D], but in general one can use Matsusaka’s big theorem ([Mat], [LM]) to show that there is a positive integer $m _ { 0 }$ such that $\mathcal { L } ^ { \otimes m _ { 0 } }$ is very ample for all polarised varieties $( X , { \mathcal { L } } )$ with fixed Hilbert polynomial.
Now let $m _ { 0 } \geq 3$ be sufficiently big.
Then we have embeddings $f _ { | \mathcal { L } ^ { \otimes m _ { 0 } } | } \colon S \to \mathbb { P } ^ { N - 1 }$ where $N = h ^ { 0 } ( S , \mathcal { L } ^ { \otimes m _ { 0 } } ) = P ( m _ { 0 } )$ . Such an embedding depends on the choice of a basis of $H ^ { 0 } ( S , { \mathcal { L } } ^ { \otimes m _ { 0 } } )$ . Let $H$ be an irreducible component of the Hilbert scheme $\mathrm { H i l b } _ { P } ( { \mathbb P } ^ { N - 1 } )$ containing at least one point corresponding to a smooth K3 surface $S$ . Let $H _ { \mathrm { s m } }$ be the open part of $H$ parametrising smooth surfaces.
Then it is easy to prove that $H _ { \mathrm { s m } }$ is smooth and that every point in $H _ { \mathrm { s m } }$ parametrises a K3 surface.
There exists a universal family $S _ { \mathrm { s m } }  H _ { \mathrm { s m } }$ . The group $\mathrm { S L } ( N , \mathbb { C } )$ acts on $H _ { \mathrm { s m } }$ and every irreducible component of the GIT moduli space of degree $2 d$ polarised K3 surfaces is of the form $\mathrm { S L } ( N , \mathbb { C } ) \backslash H _ { \mathrm { s m } }$ . Let $\mathcal { M } _ { 2 d } ^ { \prime }$ be such a component.
Choosing local polarised markings for the universal family one can construct a map $H _ { \mathrm { s m } }  \mathcal { F } _ { 2 d } ^ { 0 }$ , which clearly factors through the action of $\mathrm { S L } ( N , \mathbb { C } )$ , i.e. gives rise to a map $\pi \colon \mathcal { M } _ { 2 d } ^ { \prime } \to \mathcal { F } _ { 2 d } ^ { 0 }$ . By construction this is a holomorphic map.
On the other hand both $\mathcal { M } _ { 2 d } ^ { \prime }$ and ${ \mathcal { F } } _ { 2 d }$ are quasiprojective varieties.
It then follows from a theorem of Borel [Bl] that $\pi$ is a morphism of quasi-projective varieties.

We claim that $\pi$ is an isomorphism and that $\mathcal { M } _ { 2 d }$ has only one component.
First of all we note that one can, as in the proof of [GHS5, Theorem 1.5], take a finite ´etale cover $H _ { \mathrm { s m } } ^ { \prime }  H _ { \mathrm { s m } }$ such that the action of S $\mathrm { L } ( N + 1 , \mathbb { C } )$ lifts to a free action on $H _ { \mathrm { s m } } ^ { \prime }$ as well as on the pullback $S _ { \mathrm { s m } } ^ { \prime }  \ H _ { \mathrm { s m } } ^ { \prime }$ of the universal family.
This gives a quotient family over $Z _ { \mathrm { s m } } = \mathrm { S L } ( N + 1 , \mathbb { Z } ) \backslash H _ { \mathrm { s m } } ^ { \prime }$ which is smooth and maps finite-to-one to $\mathcal { M } _ { 2 d }$ .

By the local Torelli theorem the natural map $Z _ { \mathrm { s m } }  \mathcal { F } _ { 2 d } ^ { 0 }$ has discrete fibres and hence the same is true for $\pi$ . But then $\pi$ must be dominant.
Now we can use Theorem 2.9 to conclude that $\mathcal { M } _ { 2 d }$ is irreducible and that $\pi$ is a bijection.
Since $\mathcal { F } _ { 2 d } ^ { 0 }$ is a normal variety, it also follows that $\pi$ is an isomorphism.
We can thus summarise our discussion as follows.

Theospace 2.10 There is an isomorphism is isomorphic to the modular v $\mathcal { M } _ { 2 d } \cong \mathcal { F } _ { 2 d } ^ { 0 }$ , i.e. the GIT moduli $\mathcal { M } _ { 2 d }$ $\mathcal { F } _ { 2 d } ^ { 0 }$

# 3 Irreducible symplectic manifolds

In this section we recall the main properties of irreducible symplectic manifolds, discuss the Torelli theorem and give basic facts about moduli spaces of polarised symplectic manifolds.

# 3.1 Basic theory of irreducible symplectic manifolds

The theory of irreducible symplectic manifolds is less developed than that of K3 surfaces.
Nevertheless, several results have been proved over the last 30 years.

Definition 3.1 A complex manifold $X$ is called an irreducible symplectic manifold or hyperk¨ahler manifold if the following conditions are fulfilled:

(i) $X$ is a compact K¨ahler manifold;\
(ii) $X$ is simply-connected;\
(iii) $H ^ { 0 } ( X , \Omega _ { X } ^ { 2 } ) \cong \mathbb { C } \omega$ where $\omega$ is an everywhere nondegenerate holomorphic 2-form.

According to the Bogomolov decomposition theorem [Bog2], irreducible symplectic manifolds are one of the building blocks for compact K¨ahler manifolds with trivial canonical bundle: see also [Be, Th´eor\`eme 2]. The others are abelian varieties and Calabi-Yau varieties (here we mean Calabi-Yau in its strictest sense, i.e. a compact K¨ahler manifold $X$ such that $\pi _ { 1 } ( X ) = 1$ and $H ^ { 0 } ( X , \Omega _ { X } ^ { i } ) = 0$ for $0 < i < \dim X$ ).

In dimension two the only irreducible symplectic manifolds are K3 surfaces.
Although irreducible symplectic manifolds have now been studied for nearly 30 years, only four classes of such manifolds have so far been discovered and it is a wide open problem whether other types exist or not.
The known examples are:

(i) The length $n$ Hilbert scheme $S ^ { [ n ] } = \operatorname { H i l b } ^ { n } ( S )$ for a K3 surface $S$ and its deformations.
Note that the deformation space of such a variety has dimension 21 if $n \geq 2$ and that, since K3 surfaces only depend on 20 parameters, a general deformation will not itself be of the form $S ^ { [ n ] }$ . We shall refer to these varieties as irreducible symplectic manifolds of deformation $\mathrm { K 3 } ^ { [ n ] }$ type or deformation $\mathrm { K 3 } ^ { [ n ] }$ manifolds.

(ii) Let $A$ be a 2-dimensional complex torus and consider the length$( n + 1 )$ Hilbert scheme $A ^ { [ n + 1 ] } = \operatorname { H i l b } ^ { n + 1 } ( A )$ together with the morphism $p \colon A ^ { \lfloor n + 1 \rfloor } \to A$ given by addition.
Then $X = p ^ { - 1 } ( 0 )$ is an irreducible symplectic manifold, called a generalised Kummer variety (even though it is not necessarily algebraic).
The deformation space of these manifolds has dimension 5 if $n \geq 2$ , again one more than for 2-dimensional complex tori.

(iii) O’Grady’s irreducible symplectic manifolds of dimension 6, described in [OG2]. These are deformations of (desingularised) moduli spaces of sheaves on an abelian surface and depend on 6 parameters.
(iv) O’Grady’s irreducible symplectic manifolds of dimension 10, described in [OG1]. These are deformations of (desingularised) moduli spaces of sheaves on a K3 surface and depend on 22 parameters.

Other moduli spaces of sheaves, apart from those considered in [OG1] and [OG2], cannot be desingularised symplectically: see [KLS] and also [Zo].

In many ways irreducible symplectic manifolds behave like K3 surfaces, but there are also important differences, as we shall see later.
We first notice that it follows immediately from the definition that $X$ must have even dimension $2 n$ over $\mathbb { C }$ and that its canonical bundle $\omega _ { X }$ is trivial (an $n$ -fold exterior power of a generator $\omega$ of $H ^ { 0 } ( X , \Omega _ { X } ^ { 2 } )$ will define a trivialisation of the canonical bundle).
Clearly $h ^ { 2 , 0 } ( X ) \ = \ h ^ { 0 , 2 } ( X ) \ = \ 1$ and $h ^ { 1 , 0 } ( X ) = h ^ { 0 , 1 } ( X ) = 0$ . By a result of Bogomolov [Bog1], the deformation space of $X$ is unobstructed.
This result was generalised to Ricci-flat manifolds by Tian [Ti] and Todorov [Tod], and algebraic proofs were given by Kawamata [Kaw] and Ran $\left[ \mathrm { R a n } \right]$ (see also [Fuj]). Since

$$
T _ { [ 0 ] } \mathrm { D e f } ( X ) \cong H ^ { 1 } ( X , T _ { X } ) \cong H ^ { 1 } ( X , \Omega _ { X } ^ { 1 } )
$$

the dimension of the deformation space is $b _ { 2 } ( X ) - 2$ .

As in the $\mathrm { K 3 }$ case we have a Hodge decomposition $H ^ { 2 } ( X , \mathbb { C } ) = H ^ { 2 , 0 } \oplus$ $H ^ { 1 , 1 } \oplus H ^ { 0 , 2 }$ with $H ^ { 2 , 0 }$ and $H ^ { 0 , 2 }$ both 1-dimensional.
Unlike the K3 case the intersection form does not immediately provide $H ^ { 2 } ( S , \mathbb { Z } )$ with the structure of a lattice.
It was, however, shown by Beauville [Be] that $H ^ { 2 } ( X , \mathbb { Z } )$ does carry a natural structure as a lattice.
To define this, let $\omega \in H ^ { 2 , 0 } ( X )$ be such that $\begin{array} { r } { \int _ { X } ( \omega \overline { { \omega } } ) ^ { n } = 1 } \end{array}$ and define

$$
q _ { X } ^ { \prime } ( \alpha ) = \frac { n } { 2 } \int _ { X } \alpha ^ { 2 } ( \omega \overline { { { \omega } } } ) ^ { n - 1 } + ( 1 - n ) \left( \int _ { X } \alpha \omega ^ { n - 1 } \overline { { { \omega } } } ^ { n } \right) \left( \int _ { X } \overline { { { \alpha } } } \omega ^ { n } \overline { { { \omega } } } ^ { n - 1 } \right) .
$$

After multiplication by a positive constant $\gamma$ the quadratic form $q _ { X } ~ =$ $\gamma q _ { X } ^ { \prime }$ defines an indivisible integral symmetric bilinear form $( \quad , \quad ) _ { X }$ on $H ^ { 2 } ( X , \mathbb { Z } )$ : this is the Beauville form.
Clearly $( \omega , \omega ) _ { X } = 0$ and $( \omega , { \overline { { \omega } } } ) _ { X } > 0$ .

There is another way to introduce the Beauville form.
For this let $v ( \alpha ) =$ $\alpha ^ { 2 n }$ be given by the cup product.
Then, by a result of Fujiki [Fuj, Theorem 4.7], there is a positive rational number $c$ , the Fujiki invariant, such that

$$
v ( \alpha ) = c q _ { X } ( \alpha ) ^ { n }
$$

for all $\alpha \in H ^ { 2 } ( X , \mathbb { Z } )$ . In this sense the Beauville form can be derived from the cup product of the cohomology.

Proposition 3.2 The Beauville lattices and Fujiki invariants for the known examples of irreducible symplectic manifolds are as follows:

(i) The Beauville lattice of a deformation $\mathrm { K 3 } ^ { [ n ] }$ manifold is $L _ { \mathrm { K 3 , 2 n - 2 } } =$ $3 U \oplus 2 E _ { 8 } ( - 1 ) \oplus \langle - 2 ( n - 1 ) \rangle$ . It has rank 23, one more than the K3 lattice, to which it is closely related.
If $X = S ^ { [ n ] }$ for a K3 surface $S$ , then $3 U \oplus 2 E _ { 8 } ( - 1 )$ comes from $H ^ { 2 } ( S , \mathbb { Z } )$ and the summand $\langle - 2 ( n - 1 ) \rangle$ is generated (over $\mathbb { Q }$ ) by the exceptional divisor $E$ , which is the blow-up of the diagonal in the symmetric product $S ^ { ( n ) }$ . As an element in the Picard group the divisor $E$ is 2-divisible.
The Beauville lattice remains constant under deformations.
The Fujiki invariant is $c = ( 2 n ) ! / ( n ! 2 ^ { n } )$ .

(ii) The Beauville lattice of a generalised Kummer variety (or deformation thereof) is $3 U \oplus \langle - 2 ( n + 1 ) \rangle$ and the Fujiki invariant is $c = ( n +$ $1 ) ( 2 n ) ! / ( n ! 2 ^ { n } )$ . (iii) The Beauville lattice of the 6-dimensional example of $O$ ’Grady is $3 U \oplus \langle - 2 \rangle \oplus \langle - 2 \rangle$ and the Fujiki invariant is $c = 6 0$ . (iv) The Beauville lattice of the 10-dimensional example of O’Grady is $3 U \oplus 2 E _ { 8 } ( - 1 ) \oplus A _ { 2 } ( - 1 )$ and the Fujiki invariant is $c = 9 4 5$ .

For proofs, see [Be], [Rap1] and [Rap2]. Note that all these lattices are even.
It is, however, not known whether this is a general fact for irreducible symplectic manifolds.

Let $L$ be an abstract lattice which is isomorphic to $( H ^ { 2 } ( X , \mathbb { Z } ) , q _ { X } )$ for some irreducible symplectic manifold $X$ . A marking is an isomorphism of lattices $\phi \colon H ^ { 2 } ( X , \mathbb { Z } ) \ { \stackrel { \sim } { \to } } \ L$ . Let $p \colon \mathcal { X }  U$ be a representative of the Kuranishi family of deformations of $X$ with sufficiently small and contractible base.
Note that by unobstructedness the base space of the Kuranishi family is smooth and of dimension $b _ { 2 } ( X ) - 2$ . The marking $\phi$ for $X$ defines a marking for $\mathcal { X }$ and we obtain a period map $\pi _ { U } \colon U \to \Omega _ { L }$ to the period domain defined by (3). As in the K3 case we have a local Torelli theorem.

Theorem 3.3 (Beauville) The differential of the period map defined by the Kuranishi family is an isomorphism and thus the period map is a local isomorphism.

Proof.
See [Bog2], [Be].

As in the K3 case one can define a moduli space of marked irreducible symplectic manifolds (of a given type).
Again, this will not be Hausdorff.
Another result which carries over from the K3 case is surjectivity of the period map.

Theorem 3.4 (Huybrechts) Let $L$ be a lattice of an irreducible symplectic manifold and let $\Omega _ { L }$ be the associated period domain.
If $\mathcal { M } _ { L } ^ { \prime }$ is a non-empty component of the moduli space $\mathcal { M } _ { L }$ of irreducible symplectic manifolds with Beauville lattice $L$ , then the period map $\pi \colon { \mathcal { M } } _ { L } ^ { \prime } \to \Omega _ { L }$ is surjective.

Proof.
A proof can be found in [Huy1, Section 8].

# 3.2 Hodge theoretic Torelli theorem

So far, many results from K3 surfaces have carried over to other irreducible symplectic manifolds.
The situation changes when it comes to the global Torelli theorem.
The first counterexample to this is due to Debarre [Deb]. He showed the following: let $S$ be a K3 surface containing only one curve, which is a smooth rational curve $C$ , and consider the Hilbert scheme $X = S ^ { [ n ] }$ with $n \geq 2$ . Then $X$ contains $S ^ { n } ( C ) \cong \mathbb { P } ^ { n }$ . One can perform an elementary transformation on $X$ by first blowing up $S ^ { n } ( C )$ and then contracting the exceptional divisor in another direction.
This gives another compact complex manifold $X ^ { \prime }$ which is bimeromorphic but not isomorphic to $X$ . In general $X ^ { \prime }$ need not be K¨ahler, but Debarre produced an example where $X ^ { \prime }$ does have a K¨ahler structure and thus is an irreducible symplectic manifold.

Since the natural bimeromorphic transformation $f \colon X ^ { \prime } \to X$ defines a Hodge isometry $f ^ { * } \colon H ^ { 2 } ( X , \mathbb { Z } ) \to H ^ { 2 } ( X ^ { \prime } , \mathbb { Z } )$ this gives a counterexample to the global Torelli theorem.
It should be noted, though, that neither the surface $S$ nor the varieties $X$ and $X ^ { \prime }$ are projective.
Moreover, the existence of $\left( - 2 \right)$ -curves on a K3 surface $S$ is exactly the cause for the failure of the Hausdorff property for the base of the universal family.

Debarre’s counterexample would still allow for a version of the Torelli theorem where the existence of a Hodge isometry only implies birational equivalence, not an isomorphism (for K3 surfaces the two notions coincide).
However, this is also ruled out by the following counterexample which is due to Y. Namikawa [Nam]. For this one starts with a generic abelian surface $A$ with a polarisation of type $( 1 , 3 )$ . Then the dual abelian surface $\hat { A }$ also carries a $( 1 , 3 )$ -polarisation.
Let $X = \mathrm { K m } ^ { [ 2 ] } A$ and $\widehat { X } = \mathrm { K m } ^ { [ 2 ] } ( \widehat { A } )$ be the associated generalised Kummer varieties of dimension 4. Then $X$ and $\widehat { X }$ are birationally equivalent if and only if $A$ and $\widehat { A }$ are isomorphic abelian surfaces.
The reason for this is the following: every birational isomomorphism must send the exceptional divisor $E$ on $X$ to the exceptional divisor $\hat { E }$ on $\hat { X }$ . Since the Albanese of $E$ and $\widehat { E }$ are $A$ and $\widehat { A }$ respectively, this implies that $A$ and $\widehat { A }$ are isomorphic.
This is not the case for general $A$ . This shows that

Namikawa’s example gives a counterexample even to the birational global Torelli theorem.
Moreover, one can easily make this into a counterexample to the polarised Torelli theorem.
This can be done by choosing polarisations of the form $m L - \delta$ and $m { \widehat { L } } - { \widehat { \delta } }$ , where $m$ is sufficiently large, $L$ and $\widehat { L }$ are induced from the polarisation on $A$ and $\widehat { A }$ respectively, $\delta = 2 E$ and $\widehat { \delta } = 2 \widehat { \cal E }$ (the exceptional divisors are 2-divisible in the Picard group).
The Hodge isomorphism respects these polarisations.

At first, these counterexamples seem to indicate that there is no chance of proving a version of the global Torelli theorem for irreducible symplectic manifolds.
However, the above example is not as surprising as it seems at a first glance.
It is well known, and also well understood in terms of period domains and arithmetic groups, that $A$ and $\widehat { A }$ are not isomorphic as polarised abelian surfaces (their period points in the Siegel space are inequivalent under the paramodular group), but that the associated Kummer surfaces $\operatorname { K m } ( A )$ and $\operatorname { K m } ( { \widehat { A } } )$ are isomorphic (and their period points in the corresponding type IV domain are equivalent under the orthogonal group).
Details can be found in [GH2]. An analysis of this situation suggests that a version of the Torelli theorem could hold if one considers Hodge isometries with extra conditions.

Verbitsky [Ver] has announced a global Torelli theorem for irreducible symplectic manifolds (see also Huybrecht’s Bourbaki talk [Huy2]). His results were further elucidated by Markman [Mar4]. The crucial idea here is to use monodromy operators and parallel transport operators.
Markman first noticed the importance of these operators for the study of irreducible symplectic manifolds, developing his ideas in a series of papers [Mar1], [Mar2], [Mar3]. To define them, let $X _ { 1 } , X _ { 2 }$ be irreducible symplectic manifolds.
We say that $f \colon H ^ { * } ( X _ { 1 } , \mathbb { Z } ) \to H ^ { * } ( X _ { 2 } , \mathbb { Z } )$ is a parallel transport operator if there exists a smooth, proper flat family $\pi \colon \mathcal { X } \  \ B$ of irreducible symplectic manifolds together with points $b _ { 1 }$ , $b _ { 2 } \in B$ such that there are isomorphisms $\alpha _ { i } \colon X _ { i } \ \stackrel { \sim } { \to } \ x _ { b _ { i } }$ and a continuous path $\gamma \colon [ 0 , 1 ] \  \ B$ with $\gamma ( 0 ) = b _ { 1 }$ and $\gamma ( 1 ) = b _ { 2 }$ , such that the parallel transport in the local system $R \pi _ { * } \mathbb { Z }$ along $\gamma$ induces the isomorphism $( \alpha _ { 2 } ^ { - 1 } ) ^ { * } \circ f \circ \alpha _ { 1 } ^ { * } \colon H ^ { * } ( \mathcal { X } _ { b _ { 1 } } , \mathbb { Z } )  H ^ { * } ( \mathcal { X } _ { b _ { 2 } } , \mathbb { Z } )$ .

For a single irreducible symplectic manifold $X$ , we call an automorphism $f \colon H ^ { * } ( X , \mathbb { Z } ) \to H ^ { * } ( X , \mathbb { Z } )$ a monodromy operator if it is a parallel transport operator (with $X _ { 1 } = X _ { 2 } = X$ ). The monodromy group $\operatorname { M o n } ( X )$ is defined as the subgroup of $\operatorname { G L } ( H ^ { * } ( X , \mathbb { Z } ) )$ generated by monodromy operators.
Restricting the group action to the second cohomology group we obtain a subgroup $\mathrm { M o n } ^ { 2 } ( X )$ of $\operatorname { G L } ( H ^ { 2 } ( X , \mathbb { Z } ) )$ . Since monodromy operators preserve the Beauville form we obtain a subgroup $\operatorname { M o n } ^ { 2 } ( X ) \subset \operatorname { O } ( H ^ { 2 } ( X , \mathbb { Z } ) )$ .

Based on Verbitsky’s results $[ \mathrm { V e r } ]$ , Markman [Mar4] has formulated the following Hodge theoretic global Torelli theorem.

Theorem 3.5 (Hodge theoretic Torelli) Suppose that $X$ and $Y$ are irreducible symplectic manifolds.

(i) I $f f \colon H ^ { 2 } ( Y , \mathbb { Z } ) \to H ^ { 2 } ( X , \mathbb { Z } )$ is an isomorphism of integral Hodge structures which is a parallel transport operator, then $X$ and $Y$ are bimeromorphic.

(ii) If, moreover, $f$ maps a K¨ahler class of $Y$ to a K¨ahler class of $X$ , then $X$ and $Y$ are isomorphic.

Proof.
The first part of the theorem follows easily from Verbitsky’s results.
The second part uses in addition results on the K¨ahler cone of irreducible symplectic manifolds.
For a more detailed discussion see [Mar4, Theorem 1.3] and [Mar4, Section 3.2]. ✷

# 3.3 Moduli spaces of polarised irreducible symplectic manifolds

We shall now turn to the case of polarised irreducible symplectic manifolds.
In the K3 case we saw that the degree is the only invariant of a polarisation, or, equivalently, that there is only one $\mathrm { O } ( L _ { \mathrm { K 3 } } )$ -orbit of primitive vectors of given length.
This is no longer true in general, as can already be seen in the case of $S ^ { [ 2 ] }$ . Recall that the Beauville lattice in this case is isomorphic to $L _ { \mathrm { K 3 , 2 } } = 3 U \oplus 2 E _ { 8 } ( - 1 ) \oplus \langle - 2 \rangle$ . If $h$ is a primitive vector the number $\mathrm { d i v } ( h )$ (the divisor of $h$ : see Equation (37) below) is the positive generator of the ideal $( h , L _ { \mathrm { K 3 } , 2 } )$ , which is the biggest positive integer by which one can divide $h$ as a vector in the dual lattice $L _ { \mathrm { K 3 , 2 } } ^ { \vee }$ . Since $L _ { \mathrm { K 3 , 2 } }$ is not unimodular, but has determinant 2, the divisor $\mathrm { d i v } ( h )$ can be 1 or 2. Indeed, both of these happen when $d \equiv - 1$ mod 4 and accordingly we have one ${ \mathrm { O } } ( L _ { \mathrm { K 3 , 2 } } )$ -orbit if $d \not \equiv - 1$ mod 4 and two if $d \equiv - 1 \mod 4$ . Details of this can be found in [GHS5]. These two cases are referred to as the split case ( $\dim ( h ) = 1$ ) and the non-split case $\operatorname { d i v } ( h ) = 2$ ). The reason for this terminology is the behaviour of the orthogonal lattice: if h2 = 2d the possibilities for Lh = h⊥LK3,2 are (see Example 7.7 below)

$$
L _ { h } = 2 U \oplus 2 E _ { 8 } ( - 1 ) \oplus \langle - 2 \rangle \oplus \langle - 2 d \rangle { \mathrm { ~ f o r ~ } } \mathrm { d i v } ( h ) = 1
$$

and

$$
L _ { h } = 2 U \oplus 2 E _ { 8 } ( - 1 ) \oplus \left( \begin{array} { c c } { { - 2 } } & { { 1 } } \\ { { 1 } } & { { - \frac { d + 1 } { 2 } \Big ) \mathrm { \ f o r \ d i v } ( h ) = 2 . } } \end{array} \right.
$$

For the higher dimensional case of $S ^ { [ n ] }$ the situation becomes more involved as the possibilities for the divisor of $h$ increase in number.
Whenever the primitive vectors of length $d$ form more than one orbit, the moduli space of polarised irreducible symplectic manifolds of degree $d$ will not be connected: see [GHS5].

In order to discuss moduli spaces of polarised irreducible symplectic manifolds we first fix some discrete data: the dimension $2 n$ , the Beauville lattice (considered as an abstract lattice $L$ ), and the Fujiki invariant $c$ . Together

$L$ and $c$ define the numerical type of the irreducible symplectic manifold, denoted by $\mathbf { N }$ . Next we choose a polarisation type, i.e. an $\mathrm { O } ( L )$ -orbit of a primitive vector $h \in L$ . Viehweg’s theory gives us the existence of a moduli space ${ \mathcal { M } } _ { n , \mathbf { N } , h }$ parametrising polarised irreducible symplectic manifolds $( X , { \mathcal { L } } )$ of dimension $2 n$ with the chosen Beauville lattice, Fujiki invariant and polarisation type.
This is a quasi-projective variety and can be constructed as a GIT quotient as in the K3 case, the only difference being that we must here invoke Matsusaka’s big theorem [Mat] and a result of Koll´ar and Matsusaka [KM] to be guaranteed a uniform bound $N _ { 0 }$ such that $\mathcal { L } ^ { \otimes N _ { 0 } }$ is very ample for all pairs $( X , { \mathcal { L } } )$ .

Although there is not a Torelli theorem as in the K3 case, these moduli spaces are still related to quotients of homogeneous domains of type IV. Let $\Omega _ { L }$ be the period domain defined by the lattice $L$ and let $L _ { h } = h _ { L } ^ { \perp }$ . This is a lattice of signature $( 2 , \operatorname { r k } ( L ) - 3 )$ and defines a homogeneous domain $\Omega _ { L _ { h } }$ of type IV. Let $\mathrm { O } ( L , h )$ be the stabiliser of $h$ in $\mathrm { O } ( L )$ . This can be considered as a subgroup of $\mathrm { O } ( L _ { h } )$ . The domain $\Omega _ { L _ { h } }$ has two connected components, of which we choose one, which we denote by $\mathcal { D } _ { L _ { h } }$ . Again ${ \mathrm { O } } ^ { + } ( L , h )$ , the subgroup of $\mathrm { O } ( L , h )$ of real spinor norm 1, is the subgroup fixing the components of ΩLh.

Theorem 3.6 For every component $\mathcal { M } _ { n , \mathbf { N } , h } ^ { \prime }$ of the moduli space ${ \mathcal { M } } _ { n , \mathbf { N } , h }$ there exists a finite to one dominant morphism

$$
\psi \colon \mathcal { M } _ { n , \mathbf { N } , h } ^ { \prime } \to \mathrm { O } ^ { + } ( L , h ) \backslash \mathcal { D } _ { L _ { h } } .
$$

The proof of this is analogous to the proof of Theorem 2.10. There are, however, differences compared to the K3 case.
In general, $\psi$ will not be injective (see the discussion below).
There is also a difference concerning the image of $\psi$ . In the K3 case we know that a big and nef line bundle is ample if and only if it has positive degree on the nodal curves.
Hence it is necessary and sufficient to remove the hyperplanes orthogonal to the nodal classes.
So far, no complete analogue is known for the higher dimensional case, but Hassett and Tschinkel have proved partial results for $n = 2$ in [HT1], and more precise results in a special case in [HT2].

Nevertheless, Theorem 3.6 is enough to prove results on the Kodaira dimension of moduli spaces of polarised irreducible symplectic manifolds.
This was done in [GHS5], [GHS6]: see Theorem 6.2 and Theorem 6.3 below.

Very recent work of Verbitsky [Ver] and Markman [Mar4] improves Theorem 3.6, using a polarised analogue of the monodromy group $\operatorname { M o n } ^ { 2 } ( X ) \subset$ $\operatorname { O } ( H ^ { 2 } ( X ) , \mathbb { Z } )$ . Let $H$ be an ample divisor on $X$ . We call an element in $f \in \operatorname { M o n } ( X )$ a polarised parallel transport operator of the pair $( X , H )$ if it is a parallel transport operator for a family $\pi \colon \mathcal { X }  B$ with base point $b _ { 0 } \in B$ and isomorphism $\alpha \colon X \to \mathcal { X } _ { b _ { 0 } }$ which fixes $c _ { 1 } ( H )$ , such that there exists a flat section $h$ of $R ^ { 2 } \pi _ { * } \mathbb { Z }$ with $h ( b _ { 0 } ) = \alpha _ { * } ( c _ { 1 } ( H ) )$ and $h ( b )$ an ample class in $H ^ { 2 } ( \mathcal { X } _ { b } , \mathbb { Z } )$ for all $b \in B$ . These operators define a subgroup $\operatorname { M o n } ^ { 2 } ( X , H ) \subset \operatorname { O } ( H ^ { 2 } ( X ) , \mathbb { Z } )$ . It was shown by Markman [Mar4, Proposition 1.9] that $\mathrm { M o n } ^ { 2 } ( X , H )$ is the stabiliser of $c _ { 1 } ( H )$ in $\mathrm { M o n } ^ { 2 } ( X )$ . Given a marking $\phi \colon H ^ { \cdot 2 } ( X , \mathbb { Z } ) \to L$ this defines a subgroup

$$
\Gamma = \phi ( \operatorname { M o n } ^ { 2 } ( X , H ) ) \subset \operatorname { O } ( L , h ) ,
$$

which can be shown to be independent of the marking $\phi$ : see [Mar4, Section 7.1].

Let $\mathcal { M } _ { n , \mathbf { N } , h } ^ { \prime }$ be a component of the moduli space of polarised irreducible symplectic manifolds with fixed numerical type and polarisation type.
Given an element $( X , H )$ in this component one thus obtains a group $\Gamma \subset \operatorname { O } ( L , h )$ as above, which is also independent of the chosen pair $( X , H )$ by the results of [Mar4, Section 7.1]. In fact $\Gamma \subset \mathrm { O } ^ { + } ( L , h )$ , as monodromy operators are obviously orientation-preserving: see [Mar4, Section 1.2]. Thus $\Gamma$ acts on the homogeneous domain $\mathcal { D } _ { L _ { h } }$ .

Theorem 3.7 The map $\psi$ from Theorem 3.6 lifts to an open immersion

$$
\widetilde { \psi } \colon \mathcal { M } _ { n , \mathbf { N } , h } ^ { \prime } \to \Gamma \backslash \mathcal { D } _ { L _ { h } } ,
$$

where $\Gamma$ is as in Equation (12).

Proof.
It is easy to see that the map $\psi \colon \mathcal { M } _ { n , \mathbf { N } , h } ^ { \prime } \to \mathrm { O } ^ { + } ( L , h ) \backslash \mathcal { D } _ { L _ { h } }$ lifts to a map $\widetilde { \psi }$ : $\mathcal { M } _ { n , \mathbf { N } , h } ^ { \prime }  \Gamma \backslash \mathcal { D } _ { L _ { h } }$ (see the beginning of the proof of [GHS5, Theorem 2.3]). The hard part is the injectivity of $\widetilde { \psi }$ and this is where the Torelli theorem for irreducible symplectic manifolds is used.
For details we refer the reader to [Mar4]. ✷

Remark 3.8 We note that in general the projective group $\Gamma / \pm 1$ is a proper subgroup of $0 ^ { + } ( L , h ) / \pm 1$ and thus Theorem 3.7 is a substantial improvement of Theorem 3.6.

In the case of irreducible symplectic manifolds of $\mathrm { K 3 } ^ { [ n ] }$ type this can be made explicit.
For an even lattice $L$ we define ${ \mathrm { R e f } } ( L )$ to be the subgroup generated by $- 2$ -reflections and the negative of $+ 2$ -reflections.
This is a subgroup of $\mathrm { O } ^ { + } ( L )$ . If $X$ is an irreducible symplectic manifold of $\mathrm { K 3 } ^ { [ n ] }$ type, then we define $\operatorname { R e f } ( X )$ accordingly.

Theorem 3.9 (Markman) If $X$ is a deformation $\mathrm { K 3 } ^ { [ n ] }$ manifold then

$$
\operatorname { M o n } ^ { 2 } ( X ) = \operatorname { R e f } ( X ) .
$$

Proof.
This is proved in [Mar2, Theorem 1.2].

For a lattice $L$ we let

$$
\widehat { \mathrm { O } } ( L ) = \{ g \in \mathrm { O } ( L ) \ | \ g | _ { L ^ { \vee } / L } = \pm \mathrm { i d } _ { L ^ { \vee } / L } \}
$$

and given an element $h \in L$ we set ${ \widehat { \mathrm { O } } } ( L , h ) = \{ g \in { \widehat { \mathrm { O } } } ( L ) \ | \ g ( h ) = h \}$ . Recall the convention of Equation (7) and that by Proposition $3 . 2 ( \mathrm { i } )$ the Beauville lattice is $L _ { \mathrm { K 3 , 2 n - 2 } }$ .

It then follows from Theorem 3.9 in conjunction with Kneser’s result [Kn, Satz 4] that

$$
\mathrm { R e f } ( L _ { \mathrm { K 3 , 2 } n - 2 } ) = \widehat { \mathrm { O } } ^ { + } ( L _ { \mathrm { K 3 , 2 } n - 2 } ) .
$$

Combining this with Theorem 3.7 we thus obtain

Theorem 3.10 Let $\mathcal { M } _ { h } ^ { \prime }$ be an irreducible component of the moduli space of polarised deformation $\mathrm { K 3 } ^ { \lfloor n \rfloor }$ manifolds.
Then the map $\psi$ of Theorem 3.6 factors through the finite cover $\hat { \mathrm { ~ O ~ } } ^ { \dagger } ( L _ { \mathrm { K } 3 , 2 n - 2 } , h ) \backslash \mathcal { D } _ { L _ { h } }  \mathrm { O } ^ { + } ( L _ { \mathrm { K } 3 , 2 n - 2 } , h ) \backslash \mathcal { D } _ { L _ { h } }$ that is, there is a commutative diagram

$$
\begin{array} { r l r } {  { \mathcal { M } _ { h } ^ { \prime } \frac { \tilde { \psi } } { \longleftrightarrow } \widehat { \boldsymbol { 0 } } ^ { + } ( L _ { \mathrm { K 3 } , 2 n - 2 } , h ) \backslash \mathcal { D } _ { L _ { h } } } } \\ & { } & { \qquad \underset { \mathrm { O } ^ { + } ( L _ { \mathrm { K 3 } , 2 n - 2 } , h ) \backslash \mathcal { D } _ { L _ { h } } } { \downarrow } . } \end{array}
$$

Moreover the map $\widetilde { \psi }$ is an open immersion.

Remark 3.11 In [GHS5, Proposition 2.3] we stated that the map $\psi$ lifts to the quotient $\widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( L _ { \mathrm { K 3 } , 2 n - 2 } , h ) \backslash \mathcal { D } _ { L _ { h } }$ . This is not correct since, contrary to what was said in the proof, the projective groups $\widetilde { \mathrm { O } } ^ { + } ( L _ { \mathrm { K 3 , 2 } n - 2 } , h ) / \pm 1$ and $\widehat { \mathrm { O } } ^ { + } ( L _ { \mathrm { K } 3 , 2 n - 2 } , h ) / \pm 1$ are not identical if $n > 2$ . In that case, in fact, $\widetilde { \mathrm { O } } ^ { + } ( L _ { \mathrm { K 3 , 2 } n - 2 } , h ) / \pm 1$ is an index 2 subgroup of $\widehat { \mathrm { O } } ^ { + } ( L _ { \mathrm { K } 3 , 2 n - 2 } , h ) / \pm 1$ . If, however, $n = 2$ , then the two groups coincide since $\widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( L _ { \mathrm { K 3 , 2 } } ) = \widehat { \boldsymbol { \mathrm { O } } } ^ { + } ( L _ { \mathrm { K 3 , 2 } } )$ and thus the results of [GHS5] are not affected by this error.

Remark 3.12 Theorem 3.10 gives an affirmative answer to [GHS5, Question 2.6] (with the correct group).

Remark 3.13 The results discussed so far do not give an answer to the question whether moduli spaces of polarised irreducible symplectic manifolds of given deformation type and given type of polarisation are always connected.
Apostolov [Ap] has obtained some results on this.
For example in the Hilb $[ n ]$ case these moduli spaces are always connected for $n = 2$ (both in the split and the non-split case), but in general there can be more than one component.

# 4 Projective models

Besides the abstract theory of moduli spaces there is a vast literature which deals with concrete geometric descriptions of K3 surfaces, and to a much lesser degree, also of irreducible symplectic manifolds of higher dimension.
The easiest example is degree 4 surfaces in $\mathbb { P } ^ { 3 }$ . Any smooth quartic surface is a K3 surface and counting parameters one obtains a family of dimension $3 4 - 1 5 = 1 9$ , because 34 is the number of quartics and 15 is the dimension of $\mathrm { P G L } ( 4 , \mathbb { C } )$ . This argument shows that the moduli space ${ \mathcal { F } } _ { 4 }$ of polarised K3 surfaces of degree 4 is unirational.
The same approach yields unirationality for degrees $2 d = 2$ , $_ 6$ and 8, as these correspond to double covers of the projective plane branched along a sextic curve, complete intersections of type $( 2 , 3 )$ in $\mathbb { P } ^ { 4 }$ , and complete intersections of type $( 2 , 2 , 2 )$ in $\mathbb { P } ^ { 5 }$ respectively.

In general it can be very hard to decide whether a moduli space of polarised K3 surfaces of low degree is unirational or not.
Mukai ([Mu1], [Mu2], [Mu3], [Mu4], [Mu5]) has contributed most significantly to this problem.
So far there are three approaches to proving unirationality.

(1) Describing the K3 surfaces as complete intersections in homogeneous spaces (this can be used for $1 \leq d \leq 9$ , $d = 1 1$ , 12, 17, 19).\
(2) Using non-abelian Brill-Noether theory of vector bundles over algebraic curves (here one obtains results for $d = 6$ , 8, 10, 16).\
(3) Using specific geometric constructions for certain degrees ( $d = 1 1$ , 12, 15, 19). An example is Mukai’s most recent work ([Mu5]) for $d = 1 5$ where he describes K3 surfaces of degree 30 as complete intersections in a certain rank 10 vector bundle on the Ellingsrud-Piene-Strømme moduli space of twisted cubics.

There are only a few results about rationality for these cases.
ShepherdBarron proves rationality for the cases $d = 3$ in [S-B2] and $d = 9$ in [S-B1].

For a discussion of low degree cases we also refer the reader to Voisin’s Bourbaki expos´e [Vo2]. One can summarise the results as follows.

Theorem 4.1 The moduli spaces $\mathcal { F } _ { 2 d }$ of polarised K3 surfaces of degree $2 d$ are unirational for $1 \leq d \leq 1 2$ and $d = 1 5$ , 16, 17, 19.

Some other special moduli spaces related to K3 surfaces have also been studied.
Perhaps the most notable of these is the moduli space of Enriques surfaces, which is a special case of the lattice polarised K3 moduli spaces given in (9). This approach was first seen in Horikawa’s announcement [Hor2] of a Torelli theorem for Enriques surfaces.
It was shown by Kondo [Ko2] that the moduli space of Enriques surfaces is rational.

It is also natural in this context to consider moduli of K3 surfaces with automorphisms.
There is an extensive literature on such surfaces, much of it touching on moduli problems: for example [GaS] and the recent work of Ma and Yoshikawa [Ma].

Many of these moduli spaces turn out to be unirational or even rational, typically because the symmetry exhibits the K3 surfaces as covers of $\mathbb { P } ^ { 2 }$ and the family of possible ramification curves can be parametrised.

Some moduli of K3 surfaces with extra structure can be described as ball quotients: see for example [DGK]. Again there is an extensive literature on this subject.
For a guide, we refer the reader to the survey [DK] by Dolgachev and Kondo.
In the introduction to [DK] it is conjectured that all Deligne-Mostow arithmetic complex ball quotients are moduli spaces of K3 surfaces.

Much less is known in the case of irreducible symplectic manifolds, but some cases have been studied.

Example 4.2 A classical case is the Fano variety of lines contained in a cubic fourfold, which was studied in detail by Voisin [Vo1]. These are varieties of $\mathrm { K 3 ^ { [ 2 ] } }$ type.
In our terminology this corresponds to the degree 6 non-split case and the lattice $L _ { h }$ orthogonal to the polarisation vector is isomorphic to $2 U \oplus 2 E _ { 8 } ( - 1 ) \oplus A _ { 2 } ( - 1 )$ .

Example 4.3 O’Grady studied double covers of Eisenbud-Popescu-Walter sextics in [OG4]. This is the case of split polarisation of minimal degree (degree 2) for the $\mathrm { K 3 ^ { \lfloor 2 \rfloor } }$ -type.
The lattice $L _ { h }$ is $2 U \oplus 2 E _ { 8 } ( - 1 ) \oplus \langle - 2 \rangle \oplus \langle - 2 \rangle$ .

Example 4.4 Iliev and Ranestad ([IR1], [IR2]) have shown that the variety of sums of powers ${ \mathrm { V S P } } ( F , 1 0 )$ of presentations of a general cubic form $F$ in 6 variables as a sum of 10 cubes is an irreducible symplectic 4-fold.
These are deformations of length 2 Hilbert schemes of K3 surfaces with a degree 14 polarisation.
The precise nature of the polarisation of the irreducible symplectic manifold is unknown.

Example 4.5 Debarre and Voisin ([DV]) have constructed examples in the Grassmannian $\mathrm { G r } ( 6 , V )$ where $V$ is a 10-dimensional complex vector space.Starting with a sufficiently general form $\sigma \colon \wedge ^ { 3 } V \to \mathbb { C }$ they show that the subspace of $\mathrm { G r } ( 6 , V )$ consisting of 6-planes $L$ such that $\sigma | _ { \Lambda ^ { 3 } L } = 0$ is an irreducible symplectic fourfold of K3 $\lfloor 2 \rfloor$ -type.
This defines a 20-dimensional . $2 d = 2 2$ $L _ { h }$ $2 U \oplus 2 E _ { 8 } ( - 1 ) \oplus \binom { - 2 } { 1 } \ \stackrel { 1 } { - 6 } \Big )$

Many authors have asked about the construction of geometrically meaningful compactifications of moduli spaces of polarised K3 surfaces.
There are few general results known about this.
For small degree, some results can be found in [Sha2], [Sha3], [St] and [Sc]. A partial compactification is discussed in $\lfloor \mathrm { F r } \rfloor$ and there is an approach via log geometry in [Ol].

# 5 Compactifications

The spaces $\mathcal { F } _ { 2 d }$ (defined by (8) above) and the other quotients of period domains described in Section 4 are complex analytic spaces by construction.
We observed above that they are in fact quasi-projective varieties by the results of Baily and Borel, and the GIT moduli spaces of polarised K3 surfaces and of irreducible symplectic manifolds are quasi-projective by the general results of Viehweg.
Nevertheless, we require projective models and preferably smooth, or nearly smooth, models also.

In this section we describe the most commonly used compactifications and we give some results about the singularities that arise.
We begin by describing the class of spaces we wish to compactify.

# 5.1 Modular varieties of orthogonal type

As usual we let $L$ be an integral lattice of signature $( 2 , n )$ , $n \geq 3$ , and consider the symmetric space

$$
\mathcal { D } _ { L } = \{ x \in \mathbb { P } ( L \otimes \mathbb { C } ) \mid ( x , x ) = 0 , ( x , \bar { x } ) > 0 \} ^ { + }
$$

where the superscript $^ +$ denotes a choice of one of the two connected components of $\Omega _ { L }$ . We let $\Gamma$ be a subgroup of finite index in $\mathrm { O } ^ { + } ( L )$ . Any such $\Gamma$ acts properly discontinuously on $\mathcal { D } _ { L }$ , but in general there are elements of finite order in $\Gamma$ and they have fixed points in $\mathcal { D } _ { L }$ .

The quotient

$$
\mathcal { F } _ { L } ( \Gamma ) = \Gamma \backslash \mathcal { D } ( L )
$$

is called a modular variety of orthogonal type or orthogonal modular variety.
In particular it is a locally symmetric variety, i.e. a variety that is the quotient of a symmetric space by a discrete group of automorphisms.
It is not compact and is by its construction a complex analytic space: if $\Gamma$ is torsion-free it is a complex manifold.
In fact it is a quasi-projective variety by [BB].

Some particularly important examples of orthogonal modular varieties are:

(a) the moduli spaces of polarised K3 surfaces (the signature is $( 2 , 1 9 )$ );\
(b) the moduli spaces of lattice-polarised K3 surfaces (signature $( 2 , n )$ , with $n < 1 9$ );\
(c) the moduli spaces of polarised abelian or Kummer surfaces (signature $( 2 , 3 )$ );\
(d) the moduli space of Enriques surfaces (signature $( 2 , 1 0 )$ );\
(e) quotients of the period domains of polarised irreducible symplectic varieties (signature $( 2 , 4 )$ , $( 2 , 5 )$ , $( 2 , 2 0 )$ and $( 2 , 2 1 )$ in the known cases).

For nearly all the orthogonal modular varieties $\mathcal { F } _ { L } ( \Gamma )$ that occur in this article, $\Gamma$ is not torsion-free.
The fixed points can lead to singularities of $\mathcal { F } _ { L } ( \Gamma )$ . Since the stabiliser of any point of $\mathcal { D } _ { L }$ is finite, the singularities are finite quotient singularities: that is, locally analytically they are isomorphic to a quotient of $\mathbb { C } ^ { n }$ by a finite subgroup $G$ of ${ \mathrm { G L } } ( n , \mathbb { C } )$ . They are not arbitrary finite quotient singularities, though, and we give some details about them in Section 5.6.

The quotient $\mathbb { C } ^ { n } / G$ may in fact be smooth, however.
This happens, by a result of Chevalley [Ch], if and only if $G$ is generated by quasi-reflections (see Definition 5.8). More importantly for us, the ramification divisors of $\mathcal { D } _ { L } \to \mathcal { F } _ { L } ( \Gamma )$ are precisely the fixed loci of elements of $\Gamma$ acting as quasireflections on the tangent space.
In fact the only quasi-reflections that occur for orthogonal modular varieties are reflections.
(Let us emphasise that here we are discussing the action of an element of $G$ , not of $\Gamma$ : being a reflection on the tangent space to $\mathcal { D } _ { L }$ at a fixed point is not the same as being a reflection as an element of $\mathrm { O } ( L )$ .)

The existence of elements acting as reflections, and thus of ramification divisors, is a significant feature of orthogonal modular varieties.
For Siegel modular varieties (the symplectic group rather than the orthogonal group) there are no ramification divisors, except in the case of Siegel modular 3- folds.
Siegel modular 3-folds, however, may also be regarded as orthogonal modular varieties because of the isogeny between Sp $2$ and ${ \mathrm { S O } } ( 2 , 3 )$ .

Differential forms on $\mathcal { F } _ { L } ( \Gamma )$ may be interpreted as modular forms for $\Gamma$ : see Section 6.1 for more details.
Therefore arithmetic information (modular forms) may be used to obtain geometric information about $\mathcal { F } _ { L } ( \Gamma )$ . In particular we can use modular forms to decide whether $\mathcal { F } _ { L } ( \Gamma )$ is of general type, or more generally to try to determine its Kodaira dimension.
If $Y$ is a connected smooth projective variety of dimension $n$ , the Kodaira dimension $\kappa ( Y )$ of $Y$ is defined by

$$
\kappa ( Y ) = \mathrm { t r . d e g } \Big ( \bigoplus _ { k \geq 0 } H ^ { 0 } ( Y , k K _ { Y } ) \Big ) - 1 ,
$$

or $- \infty$ if $H ^ { 0 } ( Y , k K _ { Y } ) = 0$ for all $k > 0$ . Thus $h ^ { 0 } ( Y , k K _ { Y } ) \sim k ^ { \kappa ( Y ) }$ for $k$ sufficiently divisible.
The possible values of $\kappa ( Y )$ are $- \infty , 0 , 1 , \ldots , n =$ $\operatorname { d i m } Y$ , and $Y$ is said to be of general type if $\kappa ( Y )$ . The Kodaira dimension is a bimeromorphic invariant so it makes sense to extend the definition to arbitrary irreducible quasi-projective varieties $X$ by putting $\kappa ( X ) = \kappa ( \widetilde { X } )$ for $\widetilde { X }$ a desingularisation of a compactification of $X$ .

With this in mind, we now turn to describing some algebraic compactifications of $\mathcal { F } _ { L } ( \Gamma )$ , and the singularities that can occur.
Much further information about compactifications of locally symmetric varieties (not all algebraic) may be found in the book [BJ], especially in [BJ, Part III], and the references there.
However, the emphasis there is on the geometry and topology of symmetric and locally symmetric spaces as real manifolds.

We are interested in two kinds of compactification: the Baily-Borel compactification $\mathcal { F } _ { L } ( \Gamma ) ^ { * }$ and the toroidal compactifications $\overline { { \mathcal { F } _ { L } ( \Gamma ) } }$ . We shall describe the construction and some of the properties of each.

Remark 5.1 The constructions can also be made if $\Gamma$ is an arithmetic subgroup of $\mathrm { O } ^ { + } ( L \otimes \mathbb { Q } )$ ; that is, if $\Gamma < \mathrm { O } ( L \otimes \mathbb { Q } )$ and $\Gamma \cap { \mathrm { O } } ^ { + } ( L )$ is of finite index in both $\Gamma$ and $\mathrm { O } ^ { + } ( L )$ .

In some important ways the generalisation to arithmetic subgroups does not change things much.
If we are willing to change the lattice, by Proposition 5.2 we can always assume that $\Gamma$ is contained in $\mathrm { O } ( L )$ , so that we do not need rational entries in the matrices.
In particular the results of Sections 5.5–5.7 still hold.

Proposition 5.2 If $\Gamma < \mathrm { O } ( L \otimes \mathbb { Q } )$ is arithmetic then there exists a lattice $M \subset L \otimes \mathbb { Q }$ such that $\Gamma <  { \mathrm { O } } ( M )$ .

Proof.
Let us consider $g ( L )$ for all $g \in \Gamma$ . The index $[ \Gamma : \Gamma \cap { \mathrm { O } } ( L ) ]$ is finite, therefore the number of different copies $g ( L )$ of $L$ is finite.
Therefore the $\mathbb { Z }$ -module generated by the union of all $g ( L )$ ( $g \in \Gamma \}$ ) is finitely generated.
Denote this lattice by $M$ . Then $\Gamma$ is a subgroup of $\mathrm { O } ( M )$ by the definition of $M$ , and the quadratic form on $M$ is induced by the quadratic form on $L$ . If the quadratic form is not even integral, then we can make it integral taking a renormalisation by an integral constant $c$ , i.e. we set $( u , v ) _ { M } = c ( u , v ) _ { L }$ . Doing so does not change the orthogonal group.
It follows that $\Gamma$ can be considered as a subgroup of $\mathrm { O } ( M )$ for some even integral lattice $M$ . ✷

Notice, though, that the renormalisation by $c$ does change the stable orthogonal group.

# 5.2 The Baily-Borel compactification

The Baily-Borel compactification, which in this context is often also referred to as the Satake compactification, can be defined very quickly as $\mathrm { P r o j } \oplus M _ { k } ( \Gamma , 1 )$ , where $M _ { k } ( \Gamma , 1 )$ denotes the space of weight $k$ modular forms with trivial character: see Definition 6.4. A priori, however, it is not clear that the ring of modular forms is finitely generated, nor that the modular forms separate points of $\mathcal { F } _ { L } ( \Gamma )$ . Nor does that description immediately give a picture of the boundary $\mathcal { F } _ { L } ( \Gamma ) ^ { * } \setminus \mathcal { F } _ { L } ( \Gamma )$ . Instead the approach of Baily and Borel is to synthesise $\mathcal { F } _ { L } ( \Gamma )$ by topological and analytic methods, adding boundary components, and to show that the resulting space is a projective variety.
Full details are given in [BB], and a more detailed sketch than we give here may also be found in [BJ].

By writing $\mathcal { D } _ { L }$ in the form (14) we have exhibited it as a Hermitian domain of type IV. As a Riemannian domain, $\mathcal { D } _ { L } \cong \mathrm { S O } _ { 0 } ( 2 , n ) / \mathrm { S O } ( 2 ) \times \mathrm { S O } ( n )$ , where SO $_ 0 ( 2 , n )$ is the identity component.
The Baily-Borel compactification is defined for any Hermitian symmetric space $\mathcal { D } = G / K$ (instead of $\mathcal { D } _ { L }$ ) and for any quotient $X = \Gamma \backslash \mathcal { D }$ of $\mathcal { D }$ by an arithmetic group $\Gamma$ . We describe the construction in general but we keep in mind the case $\mathcal { D } = \mathcal { D } _ { L }$ as above.

An irreducible symmetric space $G / K$ is Hermitian if and only if the centre of the maximal compact subgroup $K$ has positive dimension: this explains why we consider only lattices of signature $( 2 , n )$ , because $\mathrm { S O } ( m ) \times \mathrm { S O } ( n )$ has discrete centre unless $n = 2$ or $m = 2$ . Any Hermitian symmetric space of noncompact type can be embedded as a bounded symmetric domain in the holomorphic tangent space $T _ { K } \mathcal { D }$ (the Harish-Chandra embedding).
For these facts see [BJ, Prop. I.5.9] or [Hel].

The Baily-Borel compactification $\mathcal { D } ^ { B B }$ of $\mathcal { D }$ is simply the closure of $\mathcal { D }$ in the Harish-Chandra embedding, which in this case is the closure $\mathcal { D } _ { L }$ of $\mathcal { D } _ { L }$ in $\mathbb { P } ( L \otimes \mathbb { C } )$ ; this in turn is contained in the compact dual, which in this case is the quadric

$$
\check { \mathcal { D } } = \{ x \in \mathbb { P } ( L \otimes \mathbb { C } ) \mid ( x , x ) = 0 \} .
$$

The tangent space to $G / K$ at $K$ is identified, as a complex manifold, with an open subset of $\check { \mathcal { D } }$ .

A subset of $\mathcal { D } ^ { B B }$ is called a boundary component if it is an analytic arc component: that is, an equivalence class under the relation $x \sim y$ if there exist finitely many holomorphic maps $f _ { i } \colon \Delta = \{ z \in \mathbb { C } \mid | z | < 1 \} $ $\mathcal { D } ^ { B B }$ such that $x \in f _ { 1 } ( \Delta )$ , $y \in f _ { k } ( \Delta )$ and $f _ { i } ( \Delta ) \cap f _ { i + i } ( \Delta ) \neq \emptyset$ for $1 \ \leq$ $i ~ < ~ k$ . The Baily-Borel compactification $\mathcal { D } ^ { B B }$ decomposes as a disjoint union of boundary components $F _ { P }$ , which are themselves symmetric spaces associated with certain parabolic subgroups $p$ of $G$ :

$$
{ \mathcal { D } } ^ { B B } = { \mathcal { D } } \amalg \coprod _ { P } F _ { P } .
$$

Not all parabolic subgroups occur, but only those associated with certain collections of strongly orthogonal roots.
See [BJ, Section I.5] for precise details.

By construction, $G$ acts on $\mathcal { D } ^ { B B }$ . The normaliser of $F _ { P }$ ,

$$
\begin{array} { r } { \mathcal { N } ( F _ { P } ) = \{ g \in G \ | \ g ( F _ { P } ) = F _ { P } \} } \end{array}
$$

is a maximal parabolic subgroup of $G$ (the parabolic subgroup $P$ is in general not maximal).
We shall later also need to consider the centraliser

$$
{ \mathcal { Z } } ( F _ { P } ) = \{ g \in G \mid g | _ { F _ { P } } = \operatorname { i d } \} .
$$

To construct the Baily-Borel compactification of $X - \mathrm { i n }$ our case, of $\mathcal { F } _ { L } ( \Gamma ) =$ $\Gamma \backslash \mathcal { D } _ { L }$ – one must first restrict to rational boundary components.

Definition 5.3 A boundary component $F$ is called a rational boundary component if

(i) the normaliser ${ \mathcal { N } } ( F )$ of $F$ in $G$ is a parabolic subgroup defined over $\mathbb { Q }$ , and\
(ii) the centraliser $\mathcal { Z } ( F )$ contains a cocompact subgroup, normal in ${ \mathcal { N } } ( F )$ , which is an algebraic subgroup defined over $\mathbb { Q }$ .

A boundary component satisfying (i) is called a weakly rational boundary component.
It is shown in [BB, Theorem 3.7] that for the Baily-Borel compactification (ii) follows from (i), so that weakly rational boundary components are automatically rational.

$G$ acts on $\mathcal { D } ^ { B B }$ but of course does not preserve rational boundary components.
However $\Gamma$ , being an arithmetic subgroup, does take rational boundary components to rational boundary components, so it acts on $\mathcal { D } ^ { \ast } : =$ $\mathcal { D } \amalg \amalg _ { F _ { P } }$ rational $F _ { P }$ . The effect of condition (ii) is that $\Gamma _ { P } = \Gamma \cap \mathcal { N } ( F _ { P } )$ is again a discrete group.
Moreover, $F _ { P }$ is again a Hermitian symmetric space and $\Gamma _ { P }$ is an arithmetic group acting on $F _ { P }$ .

We obtain the Baily-Borel compactification $( \Gamma \backslash \mathcal { D } ) ^ { * }$ by taking the quotient of ${ \mathcal { D } } ^ { * }$ by the action of $\Gamma$ . Each boundary component $\Gamma _ { P } \backslash F _ { P }$ has the structure of a complex analytic space and it is shown in [BB] that these structures can be glued together to give an analytic structure on $( \Gamma \backslash \mathcal { D } ) ^ { * }$ extending the analytic structure on $\Gamma \backslash D$ .

It is at this stage that modular forms enter the picture.
Each boundary component is an analytic space by construction but to show that their union is also an analytic space one must exhibit local analytic functions, and to show that the resulting space is projective we need analytic functions that separate points.
Baily and Borel do this by using the Siegel domain realisation of $\mathcal { D }$ over a boundary, which we describe below (Section 8.2) for the cases we need here.
For a more general description, see [Sat]. In these coordinates one may write down suitable series (Poincar´e-Eisenstein series) that define modular forms having the required properties.

Theorem 5.4 The Baily-Borel compactification $( \Gamma \backslash \mathcal { D } ) ^ { * }$ is an irreducible normal projective variety over $\mathbb { C }$ . It contains $\Gamma \backslash D$ (which in our case is $\mathcal { F } _ { L } ( \Gamma )$ ) as a Zariski-open subset, and may be decomposed as

$$
( \Gamma \backslash { \mathcal { D } } ) ^ { * } = \Gamma \backslash { \mathcal { D } } \operatorname { I I } \prod _ { P } \Gamma _ { P } \backslash X _ { P } ,
$$

where $P$ runs through representatives of $\Gamma$ -equivalence classes of parabolic subgroups determining rational boundary components.

Although we defined rational boundary components in terms of $\mathcal { D } ^ { B B }$ , they determin, according to condition (i) above, rational maximal parabolic subgroups of $G$ . If $G$ is simple, which will always be the case for us, the boundary components of $\mathcal { D } ^ { B B }$ correspond precisely to the maximal real parabolic subgroups: see [AMRT, §3.2, Proposition 2].

At least for the classical groups, the rational maximal parabolic subgroups can be described in combinatorial terms.
In the case of $\mathrm { O } ( L )$ with $L$ of signature $( 2 , n )$ they are the stabilisers of isotropic subspaces of $L \otimes \mathbb { Q }$ . Because of the signature, such spaces have dimension 2 or $^ 1$ (or 0, corresponding to the “boundary” component $\Gamma \backslash \mathcal { D } _ { L }$ ).Therefore we obtain the following description of $\mathcal { F } _ { L } ( \Gamma ) ^ { * }$ .

Theorem 5.5 $\mathcal { F } _ { L } ( \Gamma ) ^ { * }$ decomposes into boundary components as

$$
\mathcal { F } _ { L } ( \Gamma ) ^ { * } = \mathcal { F } _ { L } ( \Gamma ) \amalg \prod _ { \Pi } X _ { \Pi } \amalg \coprod _ { \ell } Q _ { \ell } ,
$$

where $\ell$ and $\Pi$ run through representatives of the finitely many $\Gamma$ -orbits of isotropic lines and isotropic planes in $L \otimes \mathbb { Q }$ respectively.
Each $X _ { \Pi }$ is a modular curve, each $Q _ { \ell }$ is a point, and $Q _ { \ell }$ is contained in the closure of $X _ { \Pi }$ if and only if the representatives may be chosen so that $\ell \subset \Pi$ .

$X _ { \Pi }$ and $Q _ { \ell }$ are usually referred to as 1-dimensional and 0-dimensional boundary components, or corank 1 and corank-2 boundary components.
The boundary components of the Baily-Borel compactification are also known as the cusps.

# 5.3 Toroidal compactifications

Toroidal compactifications in general are described in the book [AMRT]. They are made by adding a divisor at each cusp.
Locally in the analytic topology near a cusp, the toroidal compactification is a quotient of an open part of a toric variety over the cusp: this variety is determined by a choice of admissible fan in a suitable cone, and the choices must be made so as to be compatible with inclusions among the closures of the Baily-Borel boundary components.
A summary may be found in [AMRT, Chapter III, §5].

The case we are concerned with, of $\mathrm { O } ( 2 , n )$ , is simpler than the general case because only the 0-dimensional cusps need any attention.
However, we shall begin by describing the general theory, starting with $\mathcal { D } = G / K$ and an action of an arithmetic group $\Gamma$ .

Let $F$ be a boundary component: we may as well assume immediately that it is a rational boundary component.
In general one has a description of $\mathcal { D }$ as a Siegel domain, an analytic open subset inside

$$
\begin{array} { r } { \mathcal { D } ( F ) : = F \times V ( F ) \times U ( F ) _ { \mathbb { C } } . } \end{array}
$$

In this decomposition, $U ( F )$ is the centre of the unipotent radical $W ( { \boldsymbol { F } } )$ of ${ \mathcal { N } } ( F )$ , the normaliser of $F$ in $G$ , and $V ( F ) \cong W ( F ) / U ( F )$ is an abelian

Lie group.
This is not a holomorphic decomposition ( $V ( F )$ does not have a natural complex structure) but $U ( F ) _ { \mathbb { C } }$ acts holomorphically on ${ \mathcal { D } } ( F )$ and in the diagram

$$
\begin{array} { r l } { \overline { { D ( F ) } } } \\ { \pi _ { F } \Bigg | \underset { \pmb { \mathscr { D } } _ { F } } { \overset { \pi _ { F } ^ { \prime } } { \sum } } } \\ { \mathscr { D } ( F ) ^ { \prime } } \end{array} \qquad = \qquad &  \mathscr { D } ( F ) / U ( F ) _ { \mathbb { C } }
$$

all the maps are holomorphic.

Now $\mathcal { D }$ is given by a tube domain condition: there is a cone $C ( F ) \subset U ( F )$ such that

$$
\mathcal { D } = \{ x \in \mathcal { D } ( F ) \mid \mathrm { I m } ( \mathrm { p r } _ { U } ( x ) ) \in C ( F ) \} .
$$

where $\mathrm { p r } _ { U } \colon { \mathcal { D } } ( F ) \to U ( F ) _ { \mathbb { C } }$ is the projection map from the decomposition (21): this is a holomorphic map, even though (21) is not a holomorphic product decomposition.

In fact, there is a holomorphic product decomposition of ${ \mathcal { D } } ( F )$ which is (perhaps confusingly) similar:

$$
D ( F ) \cong U ( F ) _ { \mathbb { C } } \times \mathbb { C } ^ { k } \times F ,
$$

where, of course, $k = \textstyle { \frac { 1 } { 2 } } \dim _ { \mathbb { R } } V ( F )$ but $\mathbb { C } ^ { k }$ is not naturally identified with $V ( F )$ .

Denoting the map $x \in { \mathcal { D } } ( F ) \mapsto { \mathrm { I m } } ( { \mathrm { p r } } _ { U } ( x ) ) \in U ( F )$ by $\phi _ { F }$ , as in [AMRT], we have the diagram

![](images/8a64776d24454c404049d03cb4ade2e87555037405e53ed81957bc329326b579.jpg)

in which $\pi _ { F } ^ { \prime } \colon { \mathcal { D } } ( F ) \to { \mathcal { D } } ( F ) ^ { \prime }$ and $p _ { F } \colon { \mathcal { D } } ( F ) ^ { \prime }  F$ are principal homogeneous spaces for $U ( F ) _ { \mathbb { C } }$ and $V ( F )$ respectively.

When $\Gamma$ acts, the group that acts on ${ \mathcal { D } } ( F )$ and on $\mathcal { D }$ is $\mathcal { N } ( F ) _ { \mathbb { Z } } ~ =$ $\Gamma \cap { \cal N } ( F )$ , which is a discrete group because $F$ is a rational boundary component.
So, looking at the action of $U ( F ) _ { \mathbb { Z } } = \Gamma \cap U ( F )$ , we get a principal fibre bundle

$$
{ \mathcal { D } } ( F ) / U ( F ) _ { \mathbb { Z } } \longrightarrow { \mathcal { D } } ( F ) ^ { \prime }
$$

whose fibre is $T ( F ) = U ( F ) _ { \mathbb { C } } / U ( F ) _ { \mathbb { Z } }$ , an algebraic torus over $\mathbb { C }$ .

Toroidal compactification proceeds by replacing this torus with a toric variety $X _ { \Sigma ( F ) }$ and taking the closure of ${ \mathcal { D } } / U ( F ) _ { \mathbb { Z } }$ in the $X _ { \Sigma ( F ) }$ -bundle over $\mathcal { D } ( F ) ^ { \prime }$ that results.
Doing this for each cusp $F$ separately one can then take the quotients of each such $X _ { \Sigma ( F ) }$ by ${ \mathcal { N } } ( F ) _ { \mathbb { Z } }$ and (under suitable conditions) glue the resulting pieces together by identifying the copies of $\mathcal { D } / \Gamma$ contained in each one.

In this process $\Sigma ( F )$ is in general very far from unique.
It is a fan in $C ( F )$ (more precisely, of the convex hull of the rational points of the closure of $C ( F )$ ), i.e. a decomposition of $C ( F )$ into rational polyhedral cones (the integral structure is given by the lattice $U ( F ) _ { \mathbb { Z } } \subset U ( F ) _ { \cdot }$ , which is required to be ${ \mathcal { N } } ( F ) _ { \mathbb { Z } }$ -equivariant and locally finite, but is not itself finite except in trivial cases: thus $X _ { \Sigma ( F ) }$ is locally Noetherian, but not Noetherian.

In general, in order for the gluing procedure to work, the fans must satisfy a compatibility condition between fans for different cusps that arises when one cusp is in the closure of another, but in the case of $\mathrm { O } ( 2 , n )$ the condition is automatically satisfied.
The reason is that the 1-dimensional cusps have dimR $U ( F ) = 1$ and $C ( F ) = \mathbb { R } _ { + }$ , and the cone decomposition is therefore unique, and trivial.
At the 0-dimensional cusps, in contrast, one has $\dim _ { \mathbb { R } } U ( F )$ , so $\mathcal { D }$ is actually a tube domain in ${ \mathcal { D } } ( F )$ : we describe this situation explicitly in Section 8.2.

At the 0-dimensional cusps, therefore, many different choices of compactification are possible.
Below we shall choose one that suits our purpose.

In the end we need to take the quotient by ${ \mathcal { N } } ( F ) _ { \mathbb { Z } }$ , not just $U ( F ) _ { \mathbb { Z } }$ . This has two consequences.
First, this is why it is necessary to choose $\Sigma ( F )$ and hence $X _ { \Sigma ( F ) }$ in such a way that $N ( F ) _ { \mathbb { Z } }$ still acts; secondly, even if $X _ { \Sigma ( F ) }$ is chosen to be smooth, the action of $N ( F ) _ { \mathbb { Z } }$ may reintroduce quotient singularities into the finished toroidal compactification.
It is easy to choose $X _ { \Sigma ( F ) }$ to be smooth, by the usual method of subdivision to resolve toric singularities.

Theorem 5.6 A suitable choice of fans $\{ \Sigma ( F ) \}$ for rational boundary components $F$ determines a toroidal compactification $\overline { { \mathcal { D } / \Gamma } }$ of $\mathcal { D } / \Gamma$ . This compactification may be chosen to be projective, and to have at worst finite quotient singularities.

Proof.
The only part not described above is the assertion that the compactification may be chosen to be projective.
This is shown in [AMRT, Ch.IV, §2] with the extra assumption that $\Gamma$ is neat, which is harmless because one may work with a neat normal subgroup $\Gamma ^ { \prime } < \Gamma$ of finite index and then use the $\Gamma / \Gamma ^ { \prime }$ -action.
See also [FC, V.5] for more details in the Siegel (symplectic group) case, in a more arithmetic framework.
✷

# 5.4 Canonical singularities

In this part, we give sufficient conditions for the moduli space or a suitable toroidal compactification of it to have canonical singularities.
We outline the proof, from [GHS1, Section 2], that orthogonal modular varieties of dimension $n \geq 9$ satisfy these conditions.

Definition 5.7 A normal complex variety $X$ is said to have canonical singularities if it is $\mathbb { Q }$ -Gorenstein and for some (hence any) resolution of singularities $f \colon { \tilde { X } }  X$ the discrepancy $\Delta = K _ { \widetilde { X } } - f ^ { \ast } K _ { X }$ is an effective Weil $\mathbb { Q }$ -divisor.

Recall that $X$ being $\mathbb { Q }$ -Gorenstein means that for some $r \in \mathbb N$ , if $K _ { X }$ is a canonical (Weil) divisor on $X$ then $r K _ { X }$ is Cartier.
Therefore $f ^ { * } K _ { X }$ makes sense: by definition it is the $\mathbb { Q }$ -Cartier divisor $\scriptstyle { \frac { 1 } { r } } f ^ { * } ( r K _ { X } )$ .

$\Delta = \sum \alpha _ { i } E _ { i }$ is supported on the irreducible exceptional divisors $E _ { i }$ for $f$ , so $X$ has canonical singularities if and only if the rational numbers $\alpha _ { i }$ are all non-negative.
Equivalently, $X$ has canonical singularities if and only if on any open set $U \subset X$ , any pluricanonical form (i.e. section of $r K _ { x }$ for some $r$ ) on the smooth part of $U$ extends holomorphically to the whole of $\widetilde { U }$ . For more detail on canonical singularities, see $[ \mathrm { R e } ]$ .

A point $P \in X$ is said to be a canonical singularity if some neighbourhood $X _ { 0 }$ of $P$ has canonical singularities.

As we saw in Section 5.1, the singularities of $\mathcal { F } _ { L } ( \Gamma )$ are finite quotient singularities, arising at the images of points of $\mathcal { D }$ whose stabiliser in $\Gamma$ is a non-trivial finite group.
Any such action can be linearised locally [Ca]: we therefore consider the action of a finite subgroup $G < \mathrm { G L } ( n , \mathbb { C } )$ on $\mathbb { C } ^ { n }$ and the singularities of the quotient $X = \mathbb { C } ^ { n } / G$ . Any element $g \in G$ can be diagonalised since it is of finite order, and the eigenvalues of $g$ are roots of unity.

Definition 5.8 An element $g$ is a quasi-reflection if exactly one of the eigenvalues is different from 1. It is a reflection if that eigenvalue is $- 1$ .

For a cyclic subgroup $\langle g \rangle \subset \operatorname { G L } ( n , \mathbb { C } )$ of finite order $m > 1$ , we choose a primitive $m$ th root of unity $\zeta$ (without loss of generality, $\zeta = e ^ { 2 \pi i / m }$ ) and we define the Reid-Tai sum

$$
\begin{array} { r } { \Sigma ( g ) = \sum \left\{ \frac { a _ { i } } { m } \right\} } \end{array}
$$

where the eigenvalues of $g$ are $\zeta ^ { a _ { i } }$ and $\{ \}$ denotes the fractional part, $0 \leq$ $\{ q \} < 1$ . For convenience we set $\Sigma ( 1 ) = 1$ . The usual form of the Reid-Tai criterion is the following.

Proposition 5.9 Suppose that $G$ is a finite subgroup of ${ \mathrm { G L } } ( n , \mathbb { C } )$ containing no quasi-reflections.
Then $\mathbb { C } ^ { n } / G$ has canonical singularities if and only if $\Sigma ( g ) \geq 1$ for all $g \in G$ .

This is sufficient if one wants to classify singularities, since any quotient singularity is isomorphic to a quotient singularity where there are no quasireflections.
In our situation, the isotropy groups sometimes do contain quasireflections, so we want a version of the criterion that can be applied directly in that case.
First, we state a lemma that will allow us to consider the elements of $G$ one at a time.

Lemma 5.10 Suppose $G \subset \operatorname { G L } ( n , \mathbb { C } )$ is a finite group.
If $\mathbb { C } ^ { n } / \langle g \rangle$ has canonical singularities for every $g \in G$ , then $\mathbb { C } ^ { n } / G$ has canonical singularities.

Proof.
Let $\eta$ be a form on $( \mathbb { C } ^ { n } / G ) _ { \mathrm { r e g } }$ and let $\pi \colon \mathbb { C } ^ { n } \to \mathbb { C } ^ { n } / G$ be the quotient map.
Then $\pi ^ { * } ( \eta )$ is a $G$ -invariant regular form on $\mathbb { C } ^ { n } \setminus \pi ^ { - 1 } ( \mathbb { C } ^ { n } / G ) _ { \mathrm { s i n g } }$ . Since $\pi ^ { - 1 } ( \mathbb { C } ^ { n } / G ) _ { \mathrm { s i n g } }$ has codimension at least 2, the form $\pi ^ { * } ( \eta )$ extends by Hartog’s theorem to a $G$ -invariant regular form on all of $\mathbb { C } ^ { n }$ . Now the claim follows from [Ta, Proposition 3.1], which says that a $G$ -invariant form on $\mathbb { C } ^ { n }$ extends to a desingularisation of $\mathbb { C } ^ { n } / G$ if and only if it extends to a desingularisation of $\mathbb { C } ^ { n } / \langle g \rangle$ for every $g \in G$ . ✷

The converse of Lemma 5.10 is false.

Suppose that $g \in G L ( n , \mathbb { C } )$ is of order $m = s k$ , where $k$ is the smallest positive integer such that $g ^ { k }$ is either a quasi-reflection or the identity.
Order the eigenvectors so that the first $n - 1$ eigenvalues of $g ^ { k }$ are equal to 1, so that the last eigenvalue is a primitive $s$ th root of unity.
We define a modified Reid-Tai sum

$$
{ \Sigma } ^ { \prime } ( g ) = \left\{ \frac { s a _ { n } } { m } \right\} + { \sum } \left\{ \frac { a _ { i } } { m } \right\}
$$

where again the eigenvalues of $g$ are $\zeta ^ { a _ { i } }$ , and put $\Sigma ^ { \prime } ( 1 ) = 1$ . The idea (originating in an observation of Katharina Ludwig) is that this enables us to handle the quasi-reflections correctly.

Proposition 5.11 Suppose that $G$ is a finite subgroup of ${ \mathrm { G L } } ( n , \mathbb { C } )$ . Then $\mathbb { C } ^ { n } / G$ has canonical singularities if $\Sigma ^ { \prime } ( g ) \geq 1$ for all $g \in G$ .

Proof.
If no power of $g$ is a quasi-reflection then $s = 1$ and the usual Reid-Tai criterion (Proposition 5.9) shows that $\mathbb { C } ^ { n } / \langle g \rangle$ has canonical singularities.

Otherwise, consider $g$ with $g ^ { k } \ = \ h$ a quasi-reflection as above.
The eigenvalues of $g$ are $\zeta ^ { a _ { 1 } } , \ldots , \zeta ^ { a _ { n } }$ , where $\zeta$ is a primitive $_ { \mathbf { \nabla } ^ { \prime } \mathbf { \nabla } ^ { \prime } } \mathit { n } _ { \mathbf { \nabla } ^ { \prime } }$ th root of unity, $\operatorname { h c f } ( s , a _ { n } ) = 1$ and $s | a _ { i }$ for $i < n$ . The group $\langle h \rangle$ is generated by quasireflections so $\mathbb { C } ^ { n } / \langle h \rangle \cong \mathbb { C } ^ { n }$ , and we need to look at the action of the group $\langle g \rangle / \langle h \rangle$ on $\mathbb { C } ^ { n } / \langle h \rangle$ . The eigenvalues of the differential of $g ^ { l } \langle h \rangle$ on $\mathbb { C } ^ { n } / \langle h \rangle$ are $\zeta ^ { l a _ { 1 } } , \ldots , \zeta ^ { l a _ { n - 1 } } , \zeta ^ { s l a _ { n } }$ , so

$$
\Sigma ( g ^ { l } \langle h \rangle ) = \Sigma ^ { \prime } ( g ^ { l } ) \geq 1 .
$$

Thus $( \mathbb { C } ^ { n } / \langle h \rangle / \langle g \langle h \rangle ) \cong \mathbb { C } ^ { n } / \langle g \rangle$ has canonical singularities and the result follows by Lemma 5.10. ✷

# 5.5 Singularities of modular varieties

We are interested primarily in the singularities of $\mathcal { F } _ { 2 d }$ and the other spaces mentioned in Section 4, but we may more generally consider the singularities of compactified locally symmetric varieties associated with the orthogonal group of a lattice of signature $( 2 , n )$ . Unless $n$ is small, it turns out that the compactification may be chosen to have canonical singularities.

Theorem 5.12 Let $L$ be a lattice of signature $( 2 , n )$ with $n \geq 9$ , and let $\Gamma < \mathrm { O } ^ { + } ( L )$ be a subgroup of finite index.
Then there exists a projective toroidal compactification $\overline { { \mathcal { F } } } _ { L } ( \Gamma )$ of $\mathcal { F } _ { L } ( \Gamma ) = \Gamma \backslash \mathcal { D } _ { L }$ such that $\overline { { \mathcal { F } } } _ { L } ( \Gamma )$ has canonical singularities and there are no branch divisors in the boundary.
The branch divisors in $\mathcal { F } _ { L } ( \Gamma )$ arise from the fixed divisors of $\pm$ reflections.

There are three parts to the proof of this theorem.
One must first consider the singularities of the open part, which means working out some details of the action of $\Gamma$ on $\mathcal { D } _ { L }$ . Then there are the possible singularities over the 0-dimensional cusps: these lead to toric questions, and here one must choose the toroidal compactification appropriately.
Finally, in order to deal with the 1-dimensional cusps we need a full description of the geometry there.

# 5.6 Singularities in the interior

Here we are interested in the singularities that arise at fixed points of the action of $\Gamma$ on $\mathcal { D } _ { L }$ . Let $\mathbf { w } \in L _ { \mathbb { C } }$ and let $G \subset \Gamma$ be the stabiliser of $[ \mathbf { w } ] \in \mathcal { D } _ { L }$ . For $[ \mathbf { w } ] \in \mathcal { D } _ { L }$ we define $\mathbb { W } = \mathbb { C } \mathbf { w }$ . Then $G$ acts on $\mathbb { W }$ , so $g ( \mathbf { w } ) = \alpha ( g ) \mathbf { w }$ for some character $\alpha \colon G \to \mathbb { C } ^ { * }$ , and we put $G _ { 0 } ~ = ~ \ker \alpha$ . We also put $S = ( \mathbb { W } \oplus { \overline { { \mathbb { W } } } } ) ^ { \perp } \cap L$ (possibly $S = \{ 0 \}$ ) and $T = S ^ { \perp } \subset L$ . In the case of polarised K3 surfaces, $S$ is the primitive part of the Picard lattice and $T$ is the transcendental lattice of the surface corresponding to the period point w.

It is easy to check that $S _ { \mathbb { C } } \cap T _ { \mathbb { C } } = \{ 0 \}$ and that $G$ acts on $S$ and on $T$ moreover $G _ { 0 }$ acts trivially on $T _ { \mathbb { Q } }$ .

Since $G / G _ { 0 } \subset \operatorname { A u t } \mathbb { W } \cong \mathbb { C } ^ { * }$ it is a cyclic group: we denote its order by $r _ { \mathbf { w } }$ . So by the above, $\mu _ { r _ { \mathbf { w } } } \cong G / G _ { 0 }$ acts on $T _ { \mathbb { Q } }$ . (By $\mu _ { r }$ we mean the group of $r$ th roots of unity in $\mathbb { C }$ .)

For any $r \in \mathbb N$ there is a unique faithful irreducible representation of $\mu _ { r }$ over $\mathbb { Q }$ , which we call $\nu _ { r }$ . The dimension of $\mathcal { V } _ { r }$ is $\varphi ( r )$ , where $\varphi$ is the Euler $\varphi$ function and, by convention, $\varphi ( 1 ) = \varphi ( 2 ) = 1$ . The eigenvalues of a generator of $\mu _ { r }$ in this representation are precisely the primitive $r$ th roots of unity: $\nu _ { 1 }$ is the 1-dimensional trivial representation.
Note that $- \mathcal { V } _ { d } = \mathcal { V } _ { d }$ if $d$ is even and $- \mathscr { V } _ { d } = \mathscr { V } _ { 2 d }$ if $d$ is odd.

Using the fact that $S _ { \mathbb { C } } \cap T _ { \mathbb { C } } = 0$ , we may check that $T _ { \mathbb { Q } }$ splits as a direct sum of irreducible representations ${ { \mathcal { V } } _ { { { r _ { \mathbf { w } } } } } }$ (in particular, $\varphi ( r _ { \mathbf { w } } ) | \mathrm { d i m } T _ { \mathbb { Q } } )$ and that if $g \in G$ and $\alpha ( g )$ is of order $r$ (so $r | r _ { \mathbf { w } , \mathbf { \mu } }$ ), then $T _ { \mathbb { Q } }$ splits as a $g$ -module into a direct sum of irreducible representations $\nu _ { r }$ of dimension $\varphi ( r )$ .

We are interested in the action of $G$ on the tangent space to $\mathcal { D } _ { L }$ . We have a natural isomorphism

$$
T _ { [ \mathbf { w } ] } \mathcal { D } _ { L } \cong \mathrm { H o m } ( \mathbb { W } , \mathbb { W } ^ { \perp } / \mathbb { W } ) = : V .
$$

Suppose $g \in G$ is of order $m$ and $\alpha ( g )$ is of order $r$ : as usual we take $\zeta = e ^ { 2 \pi i / m }$ , and henceforth we think of $g$ as an element of $\operatorname { G L } ( V )$ , with eigenvalues $\zeta ^ { a _ { 1 } } , \ldots , \zeta ^ { a _ { n } }$ .

If $\varphi ( r )$ is not very small, the copy of $\mathcal { V } _ { r }$ containing $\mathbf { w }$ already contributes at least $1$ to $\Sigma ( g )$ . The cases $r = 1$ and $r = 2$ are also simple.

Proposition 5.13 Assume that $g \in G$ does not act as a quasi-reflection on $V$ and that $\varphi ( r ) > 4$ . Then $\Sigma ( g ) \geq 1$ .

Proof.
As $\xi$ runs through the $m$ th roots of unity, $\xi ^ { m / r }$ runs through the $r$ th roots of unity.
We denote by $k _ { 1 } , \ldots , k _ { \varphi ( r ) }$ the integers such that $0 < k _ { i } < r$ and $( k _ { i } , r ) = 1$ , in no preferred order.
Without loss of generality, we assume $\alpha ( g ) = \zeta ^ { m k _ { 2 } / r }$ and $\overline { { { \alpha ( g ) } } } = \alpha ( g ) ^ { - 1 } = \zeta ^ { m k _ { 1 } / r }$ , with $k _ { 1 } \equiv - k _ { 2 }$ mod $r$ .

One of the $\mathbb { Q }$ -irreducible subrepresentations of $g$ on $L _ { \mathbb { C } }$ contains the eigenvector w: we call this $\mathbb { V } _ { r } ^ { \mathbf { w } }$ (it is the smallest $g$ -invariant complex subspace of $L _ { \mathbb { C } }$ that is defined over $\mathbb { Q }$ and contains $\mathbf { w }$ ). It is a copy of $\nu _ { r } \otimes \mathbb { C }$ : to distinguish it from other irreducible subrepresentations of the same type we write $\mathbb { V } _ { r } ^ { \mathbf { w } } = \mathcal { V } _ { r } ^ { \mathbf { w } } \otimes \mathbb { C }$ .

If $\mathbf { v }$ is an eigenvector for $g$ with eigenvalue $\zeta ^ { m k _ { i } / r }$ , $i \neq 1$ (in particular $\textbf { v } \not \in \ \overline { { \mathbb { W } } } ,$ ), then $\textbf { v } \in \mathbb { W } ^ { \perp }$ since $( { \bf v } , { \bf w } ) = ( g ( { \bf v } ) , g ( { \bf w } ) ) = \zeta ^ { m k _ { i } / r } \alpha ( g ) ( { \bf v } , { \bf w } )$ . Therefore the eigenvalues of $g$ on $\mathbb { V } _ { r } ^ { \mathbf { w } } \cap \mathbb { W } ^ { \perp } / \mathbb { W }$ include $\zeta ^ { m k _ { i } / r }$ for $i ~ \geq 3$ , so the eigenvalues on $\operatorname { H o m } ( \mathbb { W } , \mathbb { V } _ { r } ^ { \mathbf { w } } \cap \mathbb { W } ^ { \bot } / \mathbb { W } ) \subset V$ include $\zeta ^ { m k _ { 1 } / r } \zeta ^ { m k _ { i } / r }$ for $i \geq 3$ . So

$$
\Sigma ( g ) \geq \sum _ { i = 3 } ^ { \varphi ( r ) } \left\{ { \frac { k _ { 1 } } { r } } + { \frac { k _ { i } } { r } } \right\} \geq 1 ,
$$

where the last inequality is an elementary verification.

The cases $r = 1$ and $r = 2$ are simple to deal with because one always finds two conjugate eigenvalues, which between them contribute 1 to $\Sigma ( g )$ .

So far we have needed no hypothesis on the dimension, but the remaining cases ( $r = 3$ , 4, 5, 6, 8, 10 or 12) do require such a condition because the contributions to $\Sigma ( g )$ from each $\mathcal { V } _ { r }$ are small and we need to have enough of them.
We refer to [GHS1] for details.
In the end we find

Theorem 5.14 Assume that $g \in G$ does not act as a quasi-reflection on $V$ and that $n \geq 6$ . Then $\Sigma ( g ) \geq 1$ .

One must then carry out a similar analysis for quasi-reflections.
One more dimension is needed to guarantee $\Sigma ^ { \prime } ( g ) \geq 1$ , because the $a _ { n }$ term does not help us.
The analysis also has the corollary that the quasi-reflections in the tangent space $V$ that arise are in this case always reflections, and moreover that the elements of $\Gamma$ that they come from are themselves (up to sign) reflections, considered as elements of $\mathrm { O } ( L )$ .

Corollary 5.15 If $n \geq 7$ then $\mathcal { F } _ { L } ( \Gamma )$ has canonical singularities.

# 5.7 Singularities at the cusps

We now consider the boundary $\overline { { \mathcal { F } } } _ { L } ( \Gamma ) \setminus \mathcal { F } _ { L } ( \Gamma )$ . Cusps, or boundary components in the Baily-Borel compactification, correspond to orbits of totally isotropic subspaces $E \subset L _ { \mathbb { Q } }$ . Since $L$ has signature $( 2 , n )$ , the dimension of $E$ is $^ 1$ or 2, corresponding to dimension $0$ and dimension 1 boundary components respectively.

A toroidal compactification over a cusp $F$ coming from an isotropic subspace $E$ corresponds to an admissible fan $\Sigma$ in some cone $C ( F ) \subset U ( F )$ . We have, as in [AMRT]

$$
\mathcal { D } _ { L } ( F ) : = U ( F ) _ { \mathbb { C } } \mathcal { D } _ { L } \subset \check { \mathcal { D } } _ { L }
$$

where $\check { \mathcal { D } } _ { L }$ is the compact dual of $\mathcal { D } _ { L }$ (see [AMRT, Chapter II, §2]).

The case $\dim E = 1$ , that is, isotropic vectors in $L$ , is the case of $0$ dimensional cusps in the Baily-Borel compactification and leads to a purely toric problem.
In this case we have

$$
{ \mathcal { D } } _ { L } ( F ) \cong F \times U ( F ) _ { \mathbb { C } } = U ( F ) _ { \mathbb { C } } .
$$

Put $M ( F ) = U ( F ) _ { \mathbb { Z } }$ and define the torus $\mathbf { T } ( F ) = U ( F ) _ { \mathbb { C } } / M ( F )$ . In general $( { \mathcal { D } } _ { L } / M ( F ) ) _ { \Sigma }$ is by definition the interior of the closure of $\mathcal { D } _ { L } / M ( F )$ in ${ \mathcal { D } } _ { L } ( F ) / M ( F ) \times _ { \mathbf { T } ( F ) } X _ { \Sigma } ( F )$ , i.e. in $X _ { \Sigma } ( F )$ in this case, where $X _ { \Sigma } ( F )$ is the torus embedding corresponding to the torus $\mathbf { T } ( F )$ and the fan $\Sigma$ . We may choose $\Sigma$ so that $X _ { \Sigma } ( F )$ is smooth and $G ( F ) : = N ( F ) _ { \mathbb { Z } } / U ( F ) _ { \mathbb { Z } }$ acts on $( { \mathcal { D } } _ { L } / M ( F ) ) _ { \Sigma }$ : this is also implicit in [AMRT] and explained in [FC, p.173]. The toroidal compactification is locally isomorphic to $X _ { \Sigma } ( F ) / G ( F )$ . Thus the problem of determining the singularities is reduced to a question about toric varieties, which is answered by Theorem 5.16, below.

We take a lattice $M$ of dimension $n$ and denote its dual lattice by $N$ . A fan $\Sigma$ in $N \otimes \mathbb { R }$ determines a toric variety $X _ { \Sigma }$ with torus $\mathbf { T } = \operatorname { H o m } ( M , \mathbb { C } ^ { * } ) =$ $N \otimes \mathbb { C } ^ { * }$ .

Theorem 5.16 Let $X _ { \Sigma }$ be a smooth toric variety and suppose that a finite group $G < \mathrm { A u t } ( \mathbf { T } ) = \mathrm { G L } ( M )$ of torus automorphisms acts on $X _ { \Sigma }$ . Then $X _ { \Sigma } / G$ has canonical singularities.

Proof.
This is [GHS1, Theorem 2.17]. The proof also shows (with a little modification) that there are no branch divisors contained in the boundary over 0-dimensional cusps either.
✷

It remains to consider the dimension 1 cusps.
We consider a rank 2 totally isotropic subspace $E _ { \mathbb { Q } } ~ \subset ~ L _ { \mathbb { Q } }$ , corresponding to a dimension 1 boundary component $F$ of $\mathcal { D } _ { L }$ . The idea is to choose standard bases for $L _ { \mathbb { Q } }$ so as to be able to identify $U ( F )$ , $U ( F ) _ { \mathbb { Z } }$ and $N ( F ) _ { \mathbb { Z } }$ explicitly, as is done in [Sc] for maximal K3 lattices, where $n = 1 9$ . Then, following Kondo [Ko1] one can analyse the group action in coordinates, using the Siegel domain realisation of $\mathcal { D }$ associated with the given cusp.
Both in [Ko1] and in [Sc] there are special features that allow one to work over $\mathbb { Z }$ , but in general one must work over $\mathbb { Q }$ . For details we refer to [GHS1].

# 6 Modular forms and Kodaira dimension

One of the main tools in the study of the geometry of the orthogonal modular varieties $\mathcal { F } _ { L } ( \Gamma )$ is the theory of modular forms with respect to an orthogonal group of type $\mathrm { O } ( 2 , n )$ . One application is to prove that $\mathcal { F } _ { L } ( \Gamma )$ is often of general type.
The methods described here were used in [GHS1] to prove the following result.

Theorem 6.1 The moduli space $\mathcal { F } _ { 2 d }$ of K3 surfaces with a polarisation of degree $2 d$ is of general type for any $d > 6 1$ and for $d = 4 6$ , 50, 52, 54, 57, 58 and 60.

If $d \geq 4 0$ and $d \neq 4 1$ , 44, 45 or 47 then the Kodaira dimension of ${ \mathcal { F } } _ { 2 d }$ is non-negative.

Similar methods apply to irreducible symplectic manifolds and their polarisations, discussed in Section 3.3. For deformations of length 2 Hilbert schemes of K3 surfaces with polarisation of split type (see Equation (10)) there is the following result, from [GHS5].

Theorem 6.2 The variety $\mathcal { M } _ { 2 d } ^ { [ 2 ] , s p l i t }$ is o eral t $d \geq 1 2$ . Moreover its Kodaira dimension is non-negative if $d = 9$ $d = 1 1$ .

For the ten-dimensional O’Grady case [OG1], there are again split and nonsplit polarisations, and a fairly complete general type result in the split case was proved in [GHS6].

Theorem 6.3 Let d be a positive integer not equal to $2 ^ { n }$ with $n \geq 0$ . Then every component of the moduli space of ten-dimensional polarised O’Grady varieties with split polarisation $h$ of Beauville degree $h ^ { 2 } = 2 d \neq 2 ^ { n + 1 }$ is of general type.

We do not attempt to prove Theorem 6.3 here but the theory we develop in the rest of this article will give proofs (though not with full details) of Theorem 6.1 and Theorem 6.2.

# 6.1 Modular forms of orthogonal type

In Definition 6.4 below we follow [B1]. An “affine” definition similar to the one usually given for of ${ \mathrm { S L } } ( 2 )$ can be found in [G2]. The affine cone over $\mathcal { D } _ { L }$ is ${ \mathcal { D } } _ { L } ^ { \bullet } = \left\{ y \in L \otimes \mathbb { C } \mid x = \mathbb { C } ^ { * } y \in { \mathcal { D } } _ { L } \right\}$ .

Definition 6.4 Suppose that $L$ has signature $( 2 , n )$ , with $n \geq 3$ . Let $k \in \mathbb { Z }$ and let $\chi \colon \Gamma  \mathbb { C } ^ { * }$ be a character of a subgroup $\Gamma < \mathrm { O } ^ { + } ( L )$ of finite index.
$A$ holomorphic function $F \colon { \mathcal { D } } _ { L } ^ { \bullet } \to \mathbb { C }$ is called a modular form of weight $k$ and character $\chi$ for the group $\Gamma$ if

$$
\begin{array} { r } { F ( t Z ) = t ^ { - k } F ( Z ) \quad \forall t \in \mathbb { C } ^ { * } , } \\ { F ( g Z ) = \chi ( g ) F ( Z ) \quad \forall g \in \Gamma . } \end{array}
$$

A modular form is called a cusp form if it vanishes at every cusp.

The weight as defined here is what is sometimes called arithmetic weight.
Some authors prefer to use the geometric weight, which is $k / n$ , normally only in contexts where $n | k$ . We shall always use the arithmetic weight.
One may choose a complex volume form $d Z$ on $\mathcal { D } _ { L }$ such that if $F$ is a modular form of weight ${ m n n }$ and character det for $\Gamma$ then $F ( d Z ) ^ { m }$ is a $\Gamma$ -invariant section of $m K _ { D _ { L } }$ : see [Bau] for a precise account.

If $n < 3$ then one has to add to Definition 6.4 the condition that $F$ is holomorphic at the boundary.
According to Koecher’s principle (see [Ba], [F1], [P-S]) this condition is automatically fulfilled if the dimension of a maximal isotropic subspace of $L \otimes \mathbb { Q }$ is smaller than $n$ . In particular, this is always true if $n \geq 3$ .

We denote the linear spaces of modular and cusp forms of weight $k$ and character $\chi$ by $M _ { k } ( \Gamma , \chi )$ and $S _ { k } ( \Gamma , \chi )$ respectively.
If $M _ { k } ( \Gamma , \chi )$ is nonzero then one knows that $k \geq ( n - 2 ) / 2$ (see [G2]). The minimal weight $k =$ $( n { - } 2 ) / 2$ is called singular.
Modular forms of singular weight are very special.
The first example of such forms for orthogonal groups was constructed in [G1]. Cusp forms are possible only if $k > ( n - 2 ) / 2$ . The weight $k =$ $\dim ( { \mathcal { F } } _ { L } ( \Gamma ) )$ is called canonical because by a lemma of Freitag

$$
S _ { n } ( \Gamma , \mathrm { d e t } ) \cong H ^ { 0 } \big ( \widetilde { \mathcal { F } } _ { L } ( \Gamma ) , K _ { \widetilde { \mathcal { F } } _ { L } ( \Gamma ) } \big ) ,
$$

where $\mathcal { \widetilde { F } } _ { L } ( \Gamma )$ is a smooth compact model of the modular variety $\mathcal { F } _ { L } ( \Gamma )$ and $K _ { \mathcal { \tilde { F } } _ { L } ( \Gamma ) }$ is the sheaf of canonical differential forms (see [F1, Hilfssatz 2.1, Kap. 3]). Therefore we have the following important formula for the geometric genus of the modular variety:

$$
p _ { g } ( \widetilde { \mathcal { F } } _ { L } ( \Gamma ) ) = \mathrm { d i m } S _ { n } ( \Gamma , \mathrm { d e t } ) .
$$

Remark 6.5 Below (see Section 8.3) we describe the property of being holomorphic at the boundary (needed only if $n \leq 2$ ) in terms of the Fourier expansions.

Remark 6.6 In this article we usually assume that $n \geq 3$ . In this case the order of any character $\chi$ in Definition 6.4 is finite according to Kazhdan’s property (T) (see [Ka]).

Remark 6.7 If the lattice $L$ contains two orthogonal copies of the hyperbolic plane $U \cong \left( \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right)$ and if its reduction modulo 2 (respectively 3) is of rank at least 6 (respectively 5) then $\tilde { \mathrm { O } } ^ { + } ( L )$ has only one non-trivial character, namely det (see [GHS4]). In particular the modular group $\widetilde { \mathrm { O } } ^ { + } ( L _ { 2 d } )$ related to the polarised K3 surfaces has only one non-trivial character.

Remark 6.8 If $L _ { 2 t } ^ { ( 5 ) } = 2 U \oplus \langle - 2 t \rangle$ , of signature $( 2 , 3 )$ , then the modular forms with respect to $\widetilde { \mathrm { S O } } ^ { + } ( L _ { 2 t } ^ { ( 5 ) } )$ coincide with Siegel modular forms with respect to the paramodular group $\Gamma _ { t }$ (see [G3], [GH2], [GN1], [GN3]). In parIn contrast to Remark 6.7 the group They were described in [GH3, Section ticular, if $t = 1$ we obtain the Siegel modular forms with respect to $\widetilde { \mathrm { S O } } ^ { + } ( L _ { 2 t } ^ { ( 5 ) } )$ has non-trivial characters.n construct important cusp $\operatorname { S p } _ { 2 } ( \mathbb { Z } )$ . forms of the minimal possible weight 1 with non-trivial character for the full modular group $\widetilde { \mathrm { S O } } ^ { + } ( L _ { 2 t } ^ { ( 5 ) } ) \cong \Gamma _ { t }$ for some $t$ (see [GN3]).

# 6.2 Rational quadratic divisors

For any $v \in L \otimes \mathbb { Q }$ such that $v ^ { 2 } = ( v , v ) < 0$ we define the rational quadratic divisor

$$
{ \mathcal { D } } _ { v } = { \mathcal { D } } _ { v } ( L ) = \{ [ Z ] \in { \mathcal { D } } _ { L } \mid ( Z , v ) = 0 \} \cong { \mathcal { D } } _ { v _ { L } ^ { \perp } }
$$

where $v _ { L } ^ { \perp }$ is an even integral lattice of signature $( 2 , n - 1 )$ . Therefore $\mathcal { D } _ { v }$ is also a homogeneous domain of type IV. We note that $\mathcal { D } _ { v } ( L ) = \mathcal { D } _ { t v } ( L )$ for any $t \neq 0$ . The theory of automorphic Borcherds products (see [B3]) gives a method of constructing automorphic forms with rational quadratic divisors.
Special divisors of this type (the reflective divisors defined below) play an important role in the theory of moduli spaces.

The reflection with respect to the hyperplane defined by a non-isotropic vector $r$ is given by

$$
\sigma _ { r } : l \longmapsto l - { \frac { 2 ( l , r ) } { ( r , r ) } } r .
$$

If $r$ is primitive in $L$ and the reflection $\sigma _ { r }$ fixes $L$ , i.e. $\sigma _ { r } \in \operatorname { O } ( L )$ , then we say that $r$ is a reflective vector, also known as a root.
If $( r , r ) = d$ we say that $r$ is a $d$ -vector or (if it is a root) a $d$ -root.
A 2-vector or a $- 2$ -vector is always a root.

If $v \in L ^ { \vee }$ and $( v , v ) < 0$ , the divisor $\mathcal { D } _ { v } ( L )$ is called a reflective divisor if $\sigma _ { v } \in \operatorname { O } ( L )$ . It was proved in [GHS1, Corollary 2.13] that for $n \geq 6$ the branch divisor of the modular projection

$$
\pi _ { \Gamma } \colon \mathcal { D } _ { L } \to \Gamma \setminus \mathcal { D } _ { L }
$$

is the union of the reflective divisors with respect to $\Gamma$ :

$$
\operatorname { B d i v } ( \pi _ { \Gamma } ) = \bigcup _ { \substack { \mathbb { Z } r \subset L , \sigma _ { r } \in \Gamma \cup - \Gamma } } \mathcal D _ { r } ( L ) .
$$

Note that here we have to allow $r$ such that $- \sigma _ { r } \in \Gamma$ as well as those with $\sigma _ { r } \in \Gamma$ : compare Remark 6.12 below, concerning modular forms.

# 6.3 Low weight cusp form trick

The next theorem, proved in [GHS1, Theorem 1.1], is called the low weight cusp form trick.
It plays a crucial role in the application of modular forms to moduli problems.
If $F$ is a modular form (of any weight or character) then the divisor div $F ^ { \prime }$ in $\mathcal { D } _ { L }$ is given by the equation $F ( Z ) = 0$ : this is well-defined in view of Definition 6.4.

Theorem 6.9 Let $L$ be an integral lattice of signature $( 2 , n )$ , $n \geq 9$ . The modular variety $\mathcal { F } _ { L } ( \Gamma )$ is of general type if there exists a non-zero cusp form $F _ { a } \in S _ { a } ( \Gamma , \chi )$ of small weight $a \ < \ n$ vanishing with order at least 1 at infinity such that div $F _ { a } \ge \mathrm { B d i v } ( \pi _ { \Gamma } )$ .

Proof.
We let $\overline { { \mathcal { F } } } _ { L } ( \Gamma )$ be a projective toroidal compactification of $\mathcal { F } _ { L } ( \Gamma )$ with canonical singularities and no ramification divisors at infinity, which exists by Theorem 5.12. We take a smooth projective model $Y$ of $\mathcal { F } _ { L } ( \Gamma )$ by taking a resolution of singularities of $\overline { { \mathcal { F } } } _ { L } ( \Gamma )$ . We want to show the existence of many pluricanonical forms on $Y$ .

Suppose that $F _ { n k } \in { \cal M } _ { n k } ( \Gamma , \operatorname* { d e t } ^ { k } )$ . By choosing a 0-dimensional cusp we may realise $\mathcal { D } _ { L }$ as a tube domain (see Section 8.2 for details) and use this to select a holomorphic volume element $d Z$ . Then the differential form $\Omega ( F _ { n k } ) = F _ { n k } ( d Z ) ^ { k }$ is $\Gamma$ -invariant and therefore determines a section of the pluricanonical bundle $k K = k K _ { Y }$ away from the branch locus of $\pi \colon { \mathcal { D } } _ { L } \to$ $\mathcal { F } _ { L } ( \Gamma )$ and the cusps: see [AMRT, p. 292] (but note that weight 1 in the sense of [AMRT] corresponds to weight $n$ in our definition).

In general $\Omega ( F _ { n k } )$ will not extend to a global section of $k K$ . We distinguish three kinds of obstruction to its doing so.
There are elliptic obstructions, arising because of singularities given by elliptic fixed points of the action of $\Gamma$ ; reflective obstructions, arising from the ramification divisors in $\mathcal { D } _ { L }$ ; and cusp obstructions, arising from divisors at infinity.

In order to deal with these obstructions we consider a neat normal subgroup $\Gamma ^ { \prime }$ of $\Gamma$ of finite index and set $G : = \Gamma / \Gamma ^ { \prime }$ . Let $X : = \mathcal { F } _ { L } ( \Gamma ^ { \prime } )$ and let $\overline { { \boldsymbol X } } : = \overline { { \mathcal F } } _ { L } ( \Gamma ^ { \prime } )$ be the toroidal compactification of $\mathcal { F } _ { L } ( \Gamma ^ { \prime } )$ given by the same choice of fan as for $\overline { { \mathcal { F } } } _ { L } ( \Gamma )$ . Then $\overline { { X } }$ is a smooth projective manifold with $\overline { { \mathcal { F } } } _ { L } ( \Gamma ) = \overline { { X } } / G$ . Let $D : = { \overline { { X } } } \setminus X$ be the boundary divisor of $\overline { { X } }$ . For any element $g \in G$ we define its fixed locus $X ^ { y } : = \{ x \in { \overline { { X } } } \mid g ( x ) = x \}$ and denote its divisorial part by $\overline { { { X } } } _ { ( 1 ) } ^ { g }$ . Then $R : = \cup _ { g \neq 1 } \overline { { X } } _ { ( 1 ) } ^ { g }$ is the ramification divisor of the map $\pi \colon { \overline { { X } } } \to { \overline { { X } } } / G$ .

The results of Section 5.5 (see Theorem 5.12 and Theorem 5.16 can be summarised as follows:

(i) $R$ does not contain a component of $D$ ;\
(ii) the ramification index of $\pi \colon { \overline { { X } } } \to { \overline { { X } } } / G$ along $R$ is 2;\
(iii) ${ \overline { { X } } } / G$ has canonical singularities.

We will now apply the low-weight cusp form trick, used for example in [F1] (for Siegel modular forms), [G2], [GH1] and [GS]. The main point is to use special cusp forms.
For this let the order of $\chi$ be $N$ and assume that $k$ is a multiple of $2 N$ . Then we consider forms $F _ { n k } ^ { 0 } \in S _ { n k } ( \Gamma , \operatorname* { d e t } ^ { k } ) = S _ { n k } ( \Gamma , 1 )$ of the form

$$
F _ { n k } ^ { 0 } = F _ { a } ^ { k } F _ { ( n - a ) k }
$$

where $F _ { ( n - a ) k } \in M _ { ( n - a ) k } ( \Gamma , 1 )$ is a modular form of weight $( n - a ) k \geq k$ . We claim that the corresponding forms $\Omega ( F _ { n k } ^ { 0 } )$ give rise to pluricanonical forms on $Y$ . To see this, we deal with the three kinds of obstruction in turn.
Cusp obstructions.
By definition, $\Omega ( F _ { n k } ^ { 0 } )$ is a $G$ -invariant holomorphic section of $k K _ { X }$ . Since $F _ { a }$ is a cusp form of weight $a < n$ , the form $F _ { n k } ^ { 0 }$ has zeroes of order $k$ along the boundary $D$ and hence extends to a $G$ -invariant holomorphic section of $k K _ { \overline { { X } } }$ by [AMRT, Chap. IV, Th. 1].

Reflective obstructions.
Since $R \subset \mathrm { d i v } ( F _ { a } )$ by assumption, $\Omega ( F _ { n k } ^ { 0 } )$ has zeroes of order $k$ on $R \backslash D$ . By (i) above, $\Omega ( F _ { n k } ^ { 0 } )$ actually has zeroes of order $k$ along all of $R$ . By (ii) the form $\Omega ( F _ { n k } ^ { 0 } )$ descends to a holomorphic section of $k K _ { ( \overline { { X } } / G ) _ { \mathrm { r e g } } }$ where $\left( { \overline { { X } } } / G \right) _ { \mathrm { r e g } }$ is the regular part of ${ \overline { { X } } } / G$ .

Elliptic obstructions.
By (iii) the form $\Omega ( F _ { n k } ^ { 0 } )$ extends to a holomorphic section of $k K _ { Y }$ .

Therefore $F _ { a } ^ { k } M _ { ( n - a ) k } ( \Gamma , 1 )$ is a subspace of $H ^ { 0 } ( Y , k K _ { Y } )$ . The theorem now follows because according to Hirzebruch-Mumford proportionality (see [Mum]), $\dim { \cal M } _ { ( n - a ) k } ( \Gamma , 1 )$ grows like $k ^ { n }$ . ✷

Remark 6.10 There is another way to deal with the reflective obstructions, which works even if a cusp form with the right properties cannot be found.
Among forms of very high weight there must be some that vanish along the reflective divisors, because $\dim M _ { k } ( \Gamma , 1 )$ grows faster with $k$ than the space of obstructions, which are sections in some bundles on the reflective divisors.
In [GHS3] we estimate these dimensions using Hirzebruch-Mumford proportionality.
This method can be used to produce general type results even in cases where special forms constructed by quasi pull-back are not available, but if the quasi pull-back method is available it normally produces much stronger results.

# 6.4 Reflective modular forms

For Theorem 6.9 we used cusp forms of low weight ( $k \ < \ n$ ) with large divisor (div $F \geq \operatorname { B d i v } ( \pi _ { \Gamma } ) ,$ ). We construct such modular forms for the moduli spaces of polarised K3 surfaces and other holomorphic symplectic varieties in Section 8. Modular forms of high weight ( $k \geq n$ ) with small divisor ( $\operatorname { d i v } F \leq \operatorname { B d i v } ( \pi _ { \Gamma } ) )$ also have applications to the theory of moduli spaces such as Theorem 6.15 below.

Definition 6.11 A modular form $F \in M _ { k } ( \Gamma , \chi )$ is called reflective if

$$
\operatorname { S u p p } ( \operatorname { d i v } F ) \subset \bigcup _ { \mathbb { Z } r \subset L , \ \sigma _ { r } \in \Gamma \cup - \Gamma } \mathcal { D } _ { r } ( L ) = \operatorname { B d i v } ( \pi _ { \Gamma } ) .
$$

We call $F$ strongly reflective if the multiplicity of any irreducible component of div $F$ is equal to one.

Remark 6.12 In the definition of reflective modular forms given in [GN2] only the condition $\sigma _ { r } \in \Gamma$ was considered.
The present definition, allowing $- \sigma _ { r } \in \Gamma$ , is explained by equation (32).

Example 6.13 The most famous example of a strongly reflective modular form is the Borcherds modular form $\Phi _ { 1 2 } \in { \cal M } _ { 1 2 } ( \mathrm { O } ^ { + } ( I I _ { 2 , 2 6 } ) , \mathrm { d e t } )$ (see [B1]). This is the unique modular form of singular weight 12 with character det with respect to the orthogonal group $\mathrm { O } ^ { + } ( I I _ { 2 , 2 6 } )$ of the even unimodular lattice $I I _ { 2 , 2 6 } \cong 2 U \oplus 3 E _ { 8 } ( - 1 )$ of signature $( 2 , 2 6 )$ . The form $\Phi _ { 1 2 }$ is the Kac-Weyl-Borcherds denominator function of the Fake Monster Lie algebra.
For any $\left( - 2 \right)$ -vector $r \in I I _ { 2 , 2 6 }$ we have

$$
\Phi _ { 1 2 } ( \sigma _ { r } ( Z ) ) = \operatorname* { d e t } ( \sigma _ { r } ) \Phi _ { 1 2 } ( Z ) = - \Phi _ { 1 2 } ( Z ) .
$$

Therefore $\Phi _ { 1 2 }$ vanishes along $\mathcal { D } _ { r } ( I I _ { 2 , 2 6 } )$ . According to [B1] the order of vanishing is $1$ and the full divisor of this modular form is the union of the mirrors of such reflections:

$$
\mathrm { d i v } _ { \mathcal { D } ( I I _ { 2 , 2 6 } ) } \Phi _ { 1 2 } = \sum _ { \stackrel { \pm r \in I I _ { 2 , 2 6 } } { r ^ { 2 } = - 2 } } \mathcal { D } _ { r } ( I I _ { 2 , 2 6 } ) .
$$

According to Eichler’s criterion (see Lemma 7.5) all $\left( - 2 \right)$ -vectors of $I I _ { 2 , 2 6 }$ constitute one $\tilde { \mathrm { O } } ^ { + } ( I I _ { 2 , 2 6 } )$ -orbit.
In other words, the ramification divisor of the 26-dimensional modular variety $\mathcal { F } _ { I I _ { 2 , 2 6 } } ( \widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( I I _ { 2 , 2 6 } ) )$ is irreducible.

Remark 6.14 Modular forms of weight $n$ (known as canonical weight) have special properties.
Suppose $L$ has signature $( 2 , n )$ and $F \in M _ { n } ( \Gamma , \operatorname* { d e t } )$ . If $\sigma _ { r } \in \Gamma$ , then $F ( \sigma _ { r } ( Z ) ) = - F ( Z )$ . Hence $F$ vanishes along $\mathcal { D } _ { r } ( L )$ . If $- \sigma _ { r } \in \Gamma$ , then

$$
( - 1 ) ^ { n } F ( \sigma _ { r } ( Z ) ) = F ( ( - \sigma _ { r } ) ( Z ) ) = \operatorname* { d e t } ( - \sigma _ { r } ) F ( Z ) = ( - 1 ) ^ { n + 1 } F ( Z )
$$

and $F$ also vanishes along $\mathcal { D } _ { r } ( L )$ . Therefore any $\Gamma$ -modular form of canonical weight with character det vanishes along $\operatorname { B d i v } ( \pi _ { \Gamma } )$ .

If $S _ { n } ( \Gamma , \operatorname* { d e t } ) \neq 0$ then the Kodaira dimension of $\overline { { \mathcal { F } } } _ { L } ( \Gamma )$ is non-negative (with no restriction needed on the dimension $n$ ), because if $F _ { n } \in S _ { n } ( \Gamma , \operatorname* { d e t } )$ then by Freitag’s lemma $F _ { n } ( Z ) d Z$ defines an element of $H ^ { 0 } ( \overline { \mathcal { F } } _ { L } ( \Gamma ) , K _ { \overline { \mathcal { F } } _ { L } ( \Gamma ) } )$ . Therefore $p _ { g } ( \overline { { \mathcal { F } } } _ { L } ( \Gamma ) ) \geq 1$ and the plurigenera do not all vanish.

The next theorem was proved in [G4] and contrasts with Theorem 6.9.

Theorem 6.15 Suppose that $L$ has signature $( 2 , n )$ , with $n \geq 3$ . Let $F _ { k } \in$ $M _ { k } ( \Gamma , \chi )$ be a strongly reflective modular form of weight $k$ and character $\chi$ for a subgroup $\Gamma < \mathrm { O } ^ { + } ( L )$ of finite index.
Then

$$
\kappa ( \mathcal { F } _ { L } ( \Gamma ) ) = - \infty
$$

if $k > n$ , or if $k$ and $F _ { k }$ is not a cusp form.
If $k$ and $F _ { n }$ is a cusp form whose order of zero at infinity is at least 1 then

$$
\begin{array} { r } { \kappa ( \Gamma _ { \chi } \backslash \mathcal { D } _ { L } ) = 0 , } \end{array}
$$

where $\Gamma _ { \chi } = \ker ( \chi \cdot \operatorname * { d e t } )$ is a subgroup of $\Gamma$

Proof.
The requirement that the cusp form should have order of vanishing at least 1 is almost always satisfied: see [GHS4].

To prove (33) we have to show that there are no pluricanonical differential forms on $\overline { { \mathcal { F } } } _ { L } ( \Gamma )$ . Any such differential form can be obtained using a modular form (see the proof of Theorem 6.9). The differential form $F _ { n m } ( d Z ) ^ { m }$ is $\Gamma$ - invariant and it determines a section of the pluricanonical bundle $m K$ over a smooth open part of the modular variety away from the branch locus of $\pi \colon { \mathcal { D } } _ { L } \to { \mathcal { F } } _ { L } ( \Gamma )$ and the cusps.
In the proof of Theorem 6.9 we indicated three kinds of obstruction to extending $F _ { n m } ( d Z ) ^ { m }$ to a global section of $m K$ . In the proof of this theorem we use the reflective obstruction, arising from the ramification divisor in $\mathcal { D } _ { L }$ by $\pm$ reflections in $\Gamma$ (see Equation (32)). Therefore if $F _ { n m }$ determines a global section then $F _ { n m }$ has zeroes of order at least $m$ on $\operatorname { B d i v } ( \pi _ { \Gamma } )$ . The modular form $F _ { k } \in M _ { k } ( \Gamma , \chi )$ is strongly reflective of weight $k \geq n$ . Hence $F _ { n m } / F _ { k } ^ { m }$ is a holomorphic modular form of weight $m ( n - k ) \leq 0$ . According to Koecher’s principle ( $n \geq 3$ ) this function is constant.
Therefore $F _ { n m } \equiv 0$ if $k > n$ or $F _ { n m } = C \cdot F _ { n } ^ { m }$ if $k$ . If the strongly reflective form $F _ { n }$ is non-cuspidal of weight $n$ , then $F _ { n } ^ { m } ( d Z ) ^ { \otimes m }$ cannot be extended to the compact model because of cusp obstructions ( $F _ { n } ^ { m }$ should have zeroes of order at least $m$ along the boundary).
If $F _ { n }$ is a cusp form of weight $k$ then we can consider $F _ { n }$ as a cusp form with respect to the subgroup $\Gamma _ { \chi }$ .

Then $F _ { n } ( Z ) d Z$ is $\Gamma _ { \chi }$ -invariant and, according to Freitag’s lemma, it can be extended to a global section of the canonical bundle $\Omega _ { \overline { { \mathcal { F } } } _ { L } ( \Gamma _ { \chi } ) }$ for any smooth compact model $\overline { { \mathcal { F } } } _ { L } ( \Gamma _ { \chi } )$ of $\mathcal { F } _ { L } ( \Gamma _ { \chi } )$ . Moreover Koecher’s principle shows that any $m$ -pluricanonical form is equal, up to a constant, to $F _ { n } ^ { m } ( d Z ) ^ { \otimes m }$ , proving (34). The strongly reflective cusp form of canonical weight determines essentially the unique $m$ -pluricanonical differential form on $\mathcal { F } _ { L } ( \Gamma _ { \chi } )$ . ✷

We can apply Theorem 6.15 to find examples of moduli spaces of latticepolarised K3 surfaces having $\kappa = - \infty$ and $\kappa = 0$ : see [G4].

# 7 Orthogonal groups and reflections

The material in this and subsequent sections is not so easily found in the literature, so from here on we shall give slightly more detail.

For applications, the most important subgroups of $\mathrm { O } ( L )$ are the stable orthogonal groups $\widetilde { \mathrm { O } } ( L )$ , $\tilde { \mathrm { O } } ^ { + } ( L )$ and $\widetilde { \mathrm { S O } } ^ { + } ( L )$ , as defined in Equations (6) and (7). The reason for using the word “stable” to describe $\widetilde { \mathrm { O } } ( L )$ is the following property.

Lemma 7.1 For any sublattice $S$ of a lattice $L$ the group $\widetilde { \mathrm { O } } ( S )$ can be considered as a subgroup of $\widetilde { \mathrm { O } } ( L )$ .

Proof.
Let $S ^ { \perp }$ be the orthogonal complement of $S$ in $L$ . We have

$$
S \oplus S ^ { \perp } \subset L \subset L ^ { \vee } \subset S ^ { \vee } \oplus ( S ^ { \perp } ) ^ { \vee }
$$

where $S \oplus S ^ { \perp }$ is a sublattice of finite index in $L$ . We can extend $g \in \widetilde { \mathrm { O } } ( S )$ on $S \oplus S ^ { \perp }$ putting $g | _ { S ^ { \bot } } \equiv \mathrm { i d }$ . It is clear that $g \in \widetilde { \mathrm { O } } ( S \oplus S ^ { \perp } )$ . We consider $g \in \widetilde { \mathrm { O } } ( S \oplus S ^ { \perp } )$ as an element of $\mathrm { O } ( S ^ { \vee } \oplus ( S ^ { \perp } ) ^ { \vee } )$ . For any $l ^ { \vee } \in L ^ { \vee }$ we have $g ( l ^ { \vee } ) \in l ^ { \vee } + ( S \oplus S ^ { \perp } )$ . In particular, $g ( l ) \in L$ for any $l \in L$ and $g \in \widetilde { \mathrm { O } } ( L )$ . ✷

Let $S$ be a primitive sublattice of $L$ . We define the groups

$$
\operatorname { O } ( L , S ) = \{ g \in \operatorname { O } ( L ) \mid g | _ { S } \in { \widetilde { \operatorname { O } } } ( S ) \} \quad { \mathrm { a n d } } \quad { \widetilde { \operatorname { O } } } ( L , S ) = \operatorname { O } ( L , S ) \cap { \widetilde { \operatorname { O } } } ( L ) .
$$

Note that $\mathrm { O } ( L , \mathbb { Z } h ) = \mathrm { O } ( L , h )$ if $h ^ { 2 } \neq \pm 2$ . The technique of discriminant forms developed by Nikulin in [Nik2] is very useful here, and we describe the main ideas behind it below.
For simplicity we assume that all the lattices we consider are even.

Let $S ^ { \perp }$ be the orthogonal complement of a primitive nondegenerate sublattice $S$ in $L$ . As in the proof of Lemma 7.1 we have the inclusions (35). The overlattice $L$ is defined by the finite subgroup

$$
H = L / ( S ^ { \perp } \oplus S ) < ( S ^ { \perp } ) ^ { \vee } / S ^ { \perp } \oplus S ^ { \vee } / S = D ( S ^ { \perp } ) \oplus D ( S )
$$

which is an isotropic subgroup of $D ( S ^ { \perp } ) \oplus D ( S )$ . Moreover $L / ( S \oplus S ^ { \perp } ) \cong$ $L ^ { \vee } / ( S ^ { \vee } \oplus ( S ^ { \perp } ) ^ { \vee } )$ . We define $\phi \colon L  S ^ { \vee }$ by $\phi ( l ) ( s ) = ( l , s )$ . Then $\ker ( \phi ) =$ $S ^ { \perp }$ . Since $L / ( S \oplus S ^ { \perp } ) \cong \phi ( L ) / S$ we obtain

$$
| L / ( S \oplus S ^ { \perp } ) | = | \phi ( L ) / S | = | \operatorname * { d e t } S | / [ S ^ { \vee } : \phi ( L ) ] ,
$$

as $| \operatorname* { d e t } S | = [ S ^ { \vee } : S ]$ . From the inclusions above

$$
| \operatorname * { d e t } S | \cdot | \operatorname * { d e t } S ^ { \perp } | = ( | \operatorname * { d e t } L | ) [ \phi ( L ) : S ] ^ { 2 } = | \operatorname * { d e t } L | \cdot | \operatorname * { d e t } S | ^ { 2 } / [ S ^ { \vee } : \phi ( L ) ] ^ { 2 } .
$$

In the particular case $S = \mathbb { Z } h$ and $L _ { h } = h _ { L } ^ { \perp }$ we have $[ S ^ { \vee } : \phi ( L ) ] = \operatorname { d i v } ( h )$ , where

$$
\mathrm { d i v } ( h ) \mathbb { Z } = ( h , L ) .
$$

The positive number $\mathrm { d i v } ( h )$ is called the divisor of $h$ in $L$ . We have now proved the following lemma.

Lemma 7.2 Let $L$ be any nondegenerate even integral lattice and let $h \in L$ be a primitive vector with $h ^ { 2 } = 2 d \neq 0$ . If $L _ { h }$ is the orthogonal complement of $h$ in $L$ then

$$
| \operatorname * { d e t } L _ { h } | = { \frac { | ( 2 d ) \cdot \operatorname * { d e t } L | } { \operatorname { d i v } ( h ) ^ { 2 } } } .
$$

We come back to the inclusion (36). Following [Nik2] we consider the projections

$$
p _ { S } \colon H \to D ( S ) , \qquad p _ { S ^ { \perp } } \colon H \to D ( S ^ { \perp } ) .
$$

Using the definitions and the fact that the lattices $S$ and $S ^ { \perp }$ are primitive in $L$ one can show (see [Nik2, Prop. 1.5.1]) that these projections are injective and moreover that if $d _ { S } \in p _ { S } ( H )$ then there is a unique $d _ { S ^ { \perp } } \in p _ { S ^ { \perp } } ( H )$ such that $d _ { S } + d _ { S ^ { \perp } } \in H$ . Using these arguments one proves the next lemma (see [GHS5, Lemma 3.2])

Lemma 7.3 Let $S$ be a primitive sublattice of an even lattice $L$ and denote by $\bar { g }$ the image in O $( D ( L ) )$ of $g \in \mathrm { O } ( L )$ .

(i) $g \in \operatorname { O } ( L , S )$ if and only if $g ( S ) = S$ , $\bar { g } | _ { D ( S ) } = \mathrm { i d }$ and $\bar { g } | _ { p _ { S ^ { \perp } } ( H ) } = \mathrm { i d }$ (ii) $\alpha \in \mathrm { O } ( S ^ { \perp } )$ can be extended to O $( L , S )$ if and only if $\bar { \alpha } | _ { p _ { S ^ { \perp } } ( H ) } = \mathrm { i d }$ (iii) ${ \cal I } f p _ { S ^ { \bot } } ( H ) = D ( S ^ { \bot } ) ~ t h e n ~ \mathrm { O } ( L , S ) | _ { S ^ { \bot } } \cong \widetilde { \mathrm { O } } ( S ^ { \bot } ) .$

(iv) Assume that the projection ${ \mathrm { O } } ( S ^ { \perp } ) \to { \mathrm { O } } ( D ( S ^ { \perp } ) )$ is surjective.
Then

$$
\mathrm { O } ( L , S ) | _ { S ^ { \perp } } / \widetilde { \mathrm { O } } ( S ^ { \perp } ) \cong \{ \bar { \gamma } \in \mathrm { O } ( D ( S ^ { \perp } ) ) \mid \bar { \gamma } | _ { p _ { S ^ { \perp } } ( H ) } = \mathrm { i d } \} .
$$

Corollary 7.4 If $| H | = | \operatorname* { d e t } S ^ { \perp } |$ then $\mathrm { O } ( L , S ) | _ { S ^ { \perp } } \cong \widetilde { \mathrm { O } } ( S ^ { \perp } )$

For example, the condition of Corollary 7.4 is true if $L$ is an even unimodular lattice and $S$ is any primitive sublattice of $L$ (see Example 7.6 below).
We recall the following result which we call Eichler’s criterion (see [E, Section 10], [G2, Section 3] and [GHS4]).

Lemma 7.5 Let $L$ be a lattice containing two orthogonal isotropic planes.
Then the $\widetilde { \mathrm { S O } } ( L )$ -orbit of a primitive vector $l \in L$ is determined by two invariants: by its length ${ { l } ^ { 2 } } = \left( l , l \right)$ and its image $l ^ { * } + L$ , where $l ^ { * } = l / \operatorname { d i v } ( l )$ , in the discriminant group $D ( L )$ .

We note that $l ^ { * }$ is a primitive element of the dual lattice $L ^ { \vee }$ . Therefore $\mathrm { d i v } ( l )$ is a divisor of the exponent of the discriminant group $D ( L )$ . In particular, $\mathrm { d i v } ( l )$ divides $\operatorname* { d e t } ( L )$ . Lemma 7.5 can be used to classify all possible vectors of fixed length in different lattices.

Example 7.6 (The K3 lattice.)
$L ( \mathrm { K 3 } ) = 3 U \oplus 2 E _ { 8 } ( - 1 )$ is the even unimodular lattice of signature $( 3 , 1 9 )$ : its discriminant group is trivial and all the primitive vectors $h _ { 2 d } \in { \cal L } _ { \mathrm { K 3 } }$ of length $2 d$ form a single SO( $L _ { \mathrm { K 3 } }$ )-orbit.
Therefore we can take $h _ { 2 d }$ in the first hyperbolic plane $U$ , so

$$
( h _ { 2 d } ) _ { L _ { { \bf K } 3 } } ^ { \perp } \cong L _ { 2 d } = 2 U \oplus 2 E _ { 8 } ( - 1 ) \oplus \langle - 2 d \rangle .
$$

Then according to Corollary 7.4

$$
{ \mathrm O } ^ { + } ( L _ { \mathrm { K } 3 } , h _ { 2 d } ) \cong \widetilde { { \mathrm O } } ^ { + } ( h _ { 2 d } ^ { \perp } ) = \widetilde { { \mathrm O } } ^ { + } ( 2 { U } \oplus 2 E _ { 8 } ( - 1 ) \oplus \langle - 2 d \rangle ) .
$$

The case of K3 surfaces is an exception, since the K3 lattice is unimodular.

Example 7.7 K3 $\lfloor 2 \rfloor$ -lattice, split and non-split polarisations.
We consider the Beauville lattice of a deformation $\mathrm { K 3 } ^ { \lfloor n \rfloor }$ manifold, which is isomorphic to $L _ { \mathrm { K 3 , 2 n - 2 } }$ by Proposition 3.2(i). In general there will be several, but finitely many, orbits of primitive polarisation vectors $h _ { 2 d }$ . Let $h _ { 2 d } \in ~ L _ { \mathrm { K 3 , 2 } }$ be a primitive vector of length $2 d > 0$ . Then $\mathrm { d i v } ( h _ { 2 d } )$ divides $\vert \operatorname* { d e t } L _ { \mathrm { K 3 , 2 } } \vert = 2$ .

All vectors with $\mathrm { d i v } ( h _ { 2 d } ) = 1$ constitute a single $\widetilde { \mathrm { S O } } ^ { + } ( L _ { \mathrm { K 3 } , 2 } )$ -orbit, by Lemma 7.5. Therefore, as in Example 7.6, we obtain

$$
( h _ { 2 d } ) _ { L _ { { \mathrm { K 3 , 2 } } } } ^ { \perp } \cong L _ { 2 , 2 d } = 2 U \oplus 2 E _ { 8 } ( - 1 ) \oplus \langle - 2 \rangle \oplus \langle - 2 d \rangle .
$$

We call a polarisation determined by a primitive vector $h _ { 2 d }$ with $\mathrm { d i v } ( h _ { 2 d } ) = 1$ a split polarisation.

If $h _ { 2 d } \in L _ { \mathrm { K 3 , 2 } }$ and $\mathrm { d i v } ( h _ { 2 d } ) = 2$ then we can write $h _ { 2 d }$ as $h _ { 2 d } = 2 v + c l _ { 2 }$ , where $v \in 3 U \oplus 2 E _ { 8 } ( - 1 )$ and $l _ { 2 }$ is a generator of the orthogonal component $\langle - 2 \rangle$ in $L _ { \mathrm { K 3 , 2 } }$ . The coefficient $c$ is odd because $h _ { 2 d }$ is primitive.
Note that $2 d = h _ { 2 d } ^ { 2 } = 4 ( v , v ) - 2 c ^ { 2 }$ , so $d \equiv - 1$ mod 4. According to Eichler’s criterion the $\mathrm { \check { S } O } ( L _ { \mathrm { K 3 } , 2 } )$ -orbit of $h _ { 2 d }$ is uniquely determined by the class $h _ { d } ^ { * } \equiv l _ { 2 } / 2 \mod L _ { \mathrm { K 3 , 2 } }$ . Therefore as in the case of $\mathrm { d i v } ( h _ { 2 d } ) = 1$ all vectors with $\mathrm { d i v } ( h _ { 2 d } ) = 2$ form only one orbit.
We can take a representative in the form $h _ { 2 d } = 2 v + c l _ { 2 } \in U \oplus \langle - 2 \rangle$ . The orthogonal complement of $h _ { 2 d }$ in $U \oplus \langle - 2 \rangle$ can be found by direct calculation.
This is an even rank 2 lattice $Q ( d )$ of determinant $d$ . It follows that if $d \equiv - 1$ mod 4 then there is only one orbit of vectors $h _ { 2 d }$ with $\mathrm { d i v } ( h _ { 2 d } ) = 2$ , and the orthogonal complement of $h _ { 2 d }$ is uniquely determined:

$$
\left( h _ { 2 d } \right) _ { L _ { \mathrm { K 3 , 2 } } } ^ { \perp } \cong L _ { Q \left( d \right) } = 2 U \oplus 2 E _ { 8 } ( - 1 ) \oplus \left( \begin{array} { c c } { { - 2 } } & { { 1 } } \\ { { 1 } } & { { - \frac { d + 1 } { 2 } \vphantom { | } } } \end{array} \right) .
$$

We call a polarisation of this kind a non-split polarisation.
We note that $| \operatorname * { d e t } L _ { Q ( d ) } | = d$ and the discriminant group of $L _ { Q ( d ) }$ is cyclic (see [GHS5, Remark 3.15]).

Remark 7.8 Taking the orthogonal complement of the $\left( - 2 \right)$ -vector in $Q ( d )$ we have a split sublattice of index 2

$$
\langle - 2 \rangle \oplus \langle - 2 d \rangle < Q ( d ) .
$$

Therefore $L _ { 2 , 2 d } ~ < ~ L _ { Q ( d ) }$ is also a sublattice of index 2 and according to Lemma 7.1

$$
\widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( L _ { 2 , 2 d } ) < \widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( L _ { Q ( d ) } )
$$

is a subgroup of finite index.
It follows from this that the modular variety $\mathcal { F } _ { L } ( \widetilde { \mathrm { O } } ^ { + } ( L _ { 2 , 2 d } ) )$ is a finite covering of $\mathcal { F } _ { L } ( \widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( L _ { Q ( d ) } ) )$ where $d \equiv - 1$ mod 4. One can calculate this index using the explicit formula for the Hirzebruch– Mumford volume (see [GHS2]).

We gave a classification of all possible type of polarisations for the symplectic varieties of $\mathrm { K 3 } ^ { [ n ] }$ type in [GHS5, Proposition 3.6]. Results about the polarisation types of 10-dimensional O’Grady varieties can be found in [GHS6, Theorem 3.1].

The branch divisor (Equation (32)) of the modular varieties is defined by $\pm$ reflections in the modular groups.
Below we give a description of the branch divisors in the cases of the polarised K3 surfaces and polarised holomorphic symplectic varieties of type K3[2].

Let $L$ be a nondegenerate integral lattice and $r \in L$ be a primitive vector.
If the reflection is integral, i.e. $\sigma _ { r } \in \operatorname { O } ( L )$ (see Equations (31)) and (37)), then

$$
\operatorname { d i v } ( r ) \mid r ^ { 2 } \mid 2 \operatorname { d i v } ( r ) .
$$

The following general result was proved in [GHS1].

Proposition 7.9 (i) Let $L$ be a nondegenerate even integral lattice.
Let $r \in L$ be primitive.
Then $\sigma _ { r } \in \widetilde { \mathrm { O } } ( L )$ if and only if $r ^ { 2 } = \pm 2$ .

$I f - \sigma _ { r } \in \widetilde { \mathrm { O } } ( L )$ , i.e. $\sigma _ { r } | _ { A _ { L } } = - \operatorname { i d }$ , then we also have (ii) $r ^ { 2 } = \pm 2 a$ and $\operatorname { d i v } ( r ) = a \equiv 1 { \bmod { 2 } }$ , or $r ^ { 2 } = \pm a$ and $\mathrm { d i v } ( r ) = a$ or $a / 2$ ; and

(iii) $A _ { L } \cong ( \mathbb { Z } / 2 \mathbb { Z } ) ^ { m } \times ( \mathbb { Z } / a \mathbb { Z } )$ , for some $m \geq 0$ .

If (iii) holds then

(iv) If $r ^ { 2 } = \pm a$ and either $\mathrm { d i v } ( r ) = a$ or $\operatorname { d i v } ( r ) = a / 2 \equiv 1$ mod 2, then $- \sigma _ { r } \in \widetilde { \mathrm { O } } ( L )$ ; (v) $I f r ^ { 2 } = \pm 2 a$ and $\operatorname { d i v } ( r ) = a \equiv 1$ mod 2, then $- \sigma _ { r } \in \widetilde { \mathrm { O } } ( L )$ .

With polarised K3 surfaces in mind, we consider in more detail the lattice $L _ { 2 d }$ (see Equation (38)). In this case the ramification divisor has three irreducible components.

Corollary 7.10 Let $\sigma _ { r }$ be a reflection in O $^ { + } ( L _ { 2 d } )$ defined by a primitive vector $r \in L _ { 2 d }$ . The reflection $\sigma _ { r }$ induces $\pm \mathrm { i d }$ on the discriminant group $L _ { 2 d } ^ { \vee } / L _ { 2 d }$ if and only if $r ^ { 2 } = - 2$ or $r ^ { 2 } = - 2 d$ and $\mathrm { d i v } ( r ) = d$ or $2 d$ . If $r ^ { 2 } = - 2$ then

$$
r _ { L _ { 2 d } } ^ { \perp } \cong 2 U \oplus E _ { 8 } ( - 1 ) \oplus E _ { 7 } ( - 1 ) \oplus \langle - 2 d \rangle .
$$

I ${ \mathrm { f } } \dim ( r ) = d$ then either

$$
r _ { L _ { 2 d } } ^ { \perp } \cong U \oplus 2 E _ { 8 } ( - 1 ) \oplus \langle 2 \rangle \oplus \langle - 2 \rangle
$$

or

$$
r _ { L _ { 2 d } } ^ { \perp } \cong U \oplus 2 E _ { 8 } ( - 1 ) \oplus U ( 2 ) .
$$

See the proof in [GHS1, Corollary 3.4 and Proposition 3.6]. Geometrically the three cases in the last proposition correspond to the N´eron-Severi group being (generically) $U$ , $U ( 2 )$ or $\langle 2 \rangle \oplus \langle - 2 \rangle$ respectively.
The K3 surfaces (without polarisation) themselves are, respectively, a double cover of the Hirzebruch surface $F _ { 4 }$ , a double cover of a quadric, and the desingularisation of a double cover of $\mathbb { P } ^ { 2 }$ branched along a nodal sextic.

We note that in the case of polarised deformation $\mathrm { K 3 ^ { \lfloor 2 \rfloor } }$ manifolds the branch divisor has one main (i.e. $\mathrm { d i v } ( r ) = 1$ ) component, with $r ^ { 2 } = - 2$ , and 6 (respectively, 1) additional components $\mathrm { { ( } d i v } ( r ) > 1 $ ) for split (respectively, non-split) type (see the proof of Proposition 8.13 below).

# 8 The quasi pull-back of modular forms

The main aim of this section is to show how we can construct cusp forms of small weight, for example on the moduli spaces of polarised K3 surfaces.
We use the method of quasi pull-back of the Borcherds form $\Phi _ { 1 2 }$ which was proposed in [B1, pp. 200-201]. This method was successfully applied to the theory of moduli spaces in [BKPS], [Ko3], [GHS1], [GHS5] and [GHS6]. In this section we review this method and prove a new result (Theorem 8.11 below) showing that non-trivial quasi pull-backs are cusp forms.

# 8.1 Quasi pull-back

First we give a general property of rational quadratic divisors.
Let $M$ be a lattice of signature $( 2 , m )$ and $L$ be a primitive nondegenerate sublattice of signature $( 2 , n )$ where $n < m$ . Then $L _ { M } ^ { \bot }$ is negative definite and we have as usual $L \oplus L _ { M } ^ { \perp } < M < M ^ { \vee } < L ^ { \vee } \oplus ( L ^ { \perp } ) ^ { \vee }$ . For $v \in M$ we write

$$
v = \alpha + \beta , \qquad \alpha = \mathrm { p r } _ { L ^ { \vee } } ( v ) \in L ^ { \vee } , \ \beta \in ( L ^ { \perp } ) ^ { \vee } .
$$

Lemma 8.1 Let $L$ and $M$ be as above.
Then for any $v \in M$ with $v ^ { 2 } < 0$ we have

$$
\mathcal { D } _ { L } \cap \mathcal { D } _ { v } ( M ) = \left\{ \begin{array} { l l } { \mathcal { D } _ { \alpha } ( L ) , } & { \ i f \ \alpha ^ { 2 } < 0 , } \\ { \emptyset , } & { \ i f \ \alpha ^ { 2 } \geq 0 , \ \alpha \neq 0 , } \\ { \mathcal { D } _ { L } , } & { \ i f \ \alpha = 0 , \ i . e . \ v \in L ^ { \perp } . } \end{array} \right.
$$

Proof.
We have $\mathcal { D } _ { L } \subset \mathcal { D } _ { M }$ because $L$ is a sublattice of $M$ . For any $Z =$ $X + i Y \in \mathcal { D } _ { L } ^ { \bullet }$ with $X , Y \in L \otimes \mathbb { R }$ we have $( X , Y ) = 0$ and $( X , X ) = ( Y , Y ) >$ $0$ . Therefore the quadratic space $\langle X , Y \rangle _ { \mathbb { R } }$ is of signature $( 2 , 0 )$ . Note that $( Z , v ) = 0$ is equivalent to $( Z , \alpha ) = 0$ . The signature of $L$ is equal to $( 2 , n )$ . Analysing the signature of $\langle X , Y \rangle _ { \mathbb { R } } \oplus \langle \alpha \rangle _ { \mathbb { R } }$ we get that $\mathcal { D } _ { L } \cap \mathcal { D } _ { v } ( M )$ is nonempty if and only if $\alpha = \mathrm { p r } _ { L ^ { \vee } } ( v )$ belongs to the negative definite quadratic space $\langle X , Y \rangle _ { M \otimes \mathbb { R } } ^ { \perp }$ . This proves the first two cases of the lemma.

The finite group ${ \cal H } = M / ( L \oplus L ^ { \perp } )$ is a subgroup of the orthogonal sum of the discriminant groups $D ( L ) \oplus D ( L ^ { \perp } )$ where $D ( L ) = L ^ { \vee } / L$ . The decomposition (44) defines a projection pr: $H \to D ( L ) \oplus D ( L ^ { \perp } )$ . For a primitive sublattice $L$ the class $( \alpha + L ) \in D ( L )$ is uniquely determined by the class $\beta + L ^ { \perp }$ in $D ( L ^ { \perp } )$ (see [Nik2, Proposition 1.5.1]). Therefore $\alpha \in L$ if and only if $\beta \in L ^ { \bot }$ . In particular $v$ is orthogonal to $L$ if and only if $\alpha = 0$ . This proves the last assertion of the lemma.
✷

In the next theorem we explain the main idea of the method of quasi pullback applied to the strongly reflective modular form $\Phi _ { 1 2 }$ (see [B1, pp. 200– 201] and [BKPS]).

Theorem 8.2 Let $L \hookrightarrow I I _ { 2 , 2 6 }$ be a primitive nondegenerate sublattice of signature $( 2 , n )$ , $n \geq 3$ , and let $\mathcal { D } _ { L } \hookrightarrow \mathcal { D } _ { I I _ { 2 , 2 6 } }$ be the corresponding embedding of the homogeneous domains.
The set of $\left( - 2 \right)$ -roots

$$
R _ { - 2 } ( L ^ { \perp } ) = \{ r \in I I _ { 2 , 2 6 } \mid r ^ { 2 } = - 2 , ( r , L ) = 0 \}
$$

in the orthogonal complement is finite.
We put $N ( L ^ { \perp } ) = \# R _ { - 2 } ( L ^ { \perp } ) / 2$ . Then the function

$$
\Phi | _ { L } = \frac { \Phi _ { 1 2 } ( Z ) } { \prod _ { r \in R _ { - 2 } ( L ^ { \perp } ) / \pm 1 } ( Z , r ) } \Bigg | _ { \mathscr { D } _ { L } } \in M _ { 1 2 + N ( L ^ { \perp } ) } ( \widetilde { \mathsf { O } } ( L ) , \operatorname * { d e t } ) ,
$$

where in the product over $r$ we fix a finite system of representatives in $R _ { - 2 } ( L ^ { \perp } ) / \pm 1$ . The modular form $\Phi | _ { L }$ vanishes only on rational quadratic divisors of type $\mathcal { D } _ { v } ( L )$ where $v \in L ^ { \vee }$ is the orthogonal projection of a $\left( - 2 \right)$ - root $r \in I I _ { 2 , 2 6 }$ on $L ^ { \vee }$ .

We say that the modular form $\Phi | _ { L }$ is a quasi pull-back of $\Phi _ { 1 2 }$ if the set of roots $R _ { - 2 } ( L ^ { \perp } )$ is non-empty.

Proof.
We introduce coordinates $Z ~ = ~ ( Z _ { 1 } , Z _ { 2 } ) ~ \in ~ { \mathcal { D } } _ { I I _ { 2 , 2 6 } }$ related to the embedding $L \hookrightarrow I I _ { 2 , 2 6 }$ and the splitting (44), namely $Z _ { 1 } ~ \in ~ L \otimes \mathbb { C }$ and $Z _ { 2 } \in ( L \otimes \mathbb { C } ) ^ { \perp }$ . We have $\widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( L ) < \boldsymbol { \mathrm { O } } ^ { + } ( I I _ { 2 , 2 6 } )$ (see Lemma 7.1) and we denote by $\tilde { g } \in \mathrm { O } ^ { + } ( I I _ { 2 , 2 6 } )$ the extension of $g \in \widetilde { \mathrm { O } } ^ { + } ( L )$ by $\tilde { g } | _ { L ^ { \perp } } = \mathrm { i d }$ .

If the root system $R _ { - 2 } ( L ^ { \perp } )$ is empty, then $\Phi | _ { L }$ is the usual pull-back of $\Phi _ { 1 2 }$ on $\mathcal { D } _ { L }$ . Then $\Phi | _ { L } \not \equiv 0$ and we have

$$
\operatorname * { d e t } ( g ) \Phi _ { 1 2 } ( Z _ { 1 } , Z _ { 2 } ) = \Phi _ { 1 2 } ( \tilde { g } ( Z _ { 1 } , Z _ { 2 } ) ) = \Phi _ { 1 2 } ( g \cdot Z _ { 1 } , Z _ { 2 } ) .
$$

Therefore the pull-back of $\Phi _ { \mathrm { 1 2 } }$ on $\mathcal { D } _ { L }$ is a modular form of weight 12. We note that even in this simple case one obtains interesting reflective modular forms (see [GN3, Section 4.2]).

If there are roots in $R _ { - 2 } ( L ^ { \perp } )$ then the pull-back of $\Phi _ { \mathrm { 1 2 } }$ on $\mathcal { D } _ { L }$ vanishes identically, and one has to divide by the equations of the rational quadratic divisors, as in Equation (45).

According to Lemma 8.1 the order of zero of $\Phi _ { 1 2 }$ along $\mathcal { D } _ { L }$ is equal to $N ( L ^ { \perp } ) = \# R _ { - 2 } ( L ^ { \perp } ) / 2$ . Therefore the non-zero function $\Phi | _ { L }$ is holomorphic on $\mathcal { D } _ { L } ^ { \bullet }$ . Moreover it is homogeneous of degree $1 2 + N ( L ^ { \perp } )$ . Any $g \in \widetilde { \mathrm { O } } ^ { + } ( L )$ acts trivially on $L ^ { \perp }$ and $( Z , r ) = ( Z _ { 1 } + Z _ { 2 } , r ) = ( Z _ { 2 } , r )$ . Therefore

$$
 { \frac { \Phi _ { 1 2 } ( g Z _ { 1 } , Z _ { 2 } ) } { \prod _ { r } ( Z _ { 2 } , r ) } } | _ { { \mathcal { D } } _ { L } } =  { \frac { \Phi _ { 1 2 } ( \tilde { g } \cdot ( Z _ { 1 } , Z _ { 2 } ) ) } { \prod _ { r } ( \tilde { g } \cdot ( Z _ { 1 } , Z _ { 2 } ) , r ) } } | _ { { \mathcal { D } } _ { L } } = \operatorname * { d e t } ( g ) { \frac { \Phi _ { 1 2 } ( Z ) } { \prod _ { r } ( Z , r ) } } | _ { { \mathcal { D } } _ { L } } .
$$

It follows that $\Phi | _ { L }$ is modular with respect to $\tilde { \mathrm { O } } ^ { + } ( L )$ with character det.\
We finish the proof using Koecher’s principle.

The zeros of $\Phi | _ { L }$ can be determined using Lemma 8.1 and the fact that $\Phi _ { \mathrm { 1 2 } }$ vanishes along $\mathcal { D } _ { r } ( I I _ { 2 , 2 6 } )$ with $r ^ { 2 } = - 2$ . ✷

Remark 8.3 Theorem 8.2 is still true for $n \ \leq \ 2$ . We can show this by computing the Fourier expansions of the quasi pull-back.
Moreover we prove in Theorem 8.11 that the quasi pull-back is always a cusp form.

Remark 8.4 The modular group of $\Phi | _ { L }$ might be larger than $\tilde { \mathrm { O } } ^ { + } ( L )$ (see, for example, [GHS6, Lemma 4.4]).

Remark 8.5 For the applications to the theory of moduli spaces we use the quasi pull-back of $\Phi _ { \mathrm { 1 2 } }$ . It is easy to prove an analogue of Theorem 8.2 for an arbitrary modular form whose divisor consists only of rational quadratic divisors (in the style of Theorem 8.11 below).

In [GHS1] we showed that some quasi pull-backs for lattices related to the moduli spaces of polarised K3 surfaces are cusp forms.
In this paper we prove a new, more general result: that the quasi pull-back construction always gives a cusp form.
The main idea of the proof is to consider the quasi pull-back as a differential operator (see [GHS1, Section 6]).

# 8.2 Tube domain realisation

We define a Fourier expansion of a modular form $F$ at a 0-dimensional cusp.
The Fourier expansion depends on the choice of affine coordinates at a cusp.
We consider the general case, following the approach used in [B2, Theorem 5.2 and page 542]: for more details see [GN3, Section 2.3] and [F2].

A 0-dimensional cusp of $\mathcal { D } _ { L }$ is defined by an isotropic sublattice of rank 1 or, equivalently, by a primitive isotropic vector $c \in L$ (up to sign: $c$ and $- c$ define the same cusp).
The choice of $c$ identifies $\mathcal { D } _ { L }$ with an affine quadric:

$$
{ \mathcal { D } } _ { L , c } = \{ Z \in { \mathcal { D } } _ { L } ^ { \bullet } \mid ( Z , c ) = 1 \} \cong { \mathcal { D } } _ { L } .
$$

The lattice

$$
L _ { c } : = c ^ { \perp } / c = c _ { L } ^ { \perp } / \mathbb { Z } c
$$

is an integral lattice of signature $( 1 , n - 1 )$ . We fix an element $b \in L ^ { \vee }$ such that $( c , b ) = 1$ . A choice of $b$ gives a realisation of the hyperbolic lattice $L _ { c }$ as a sublattice in $L$

$$
L _ { c } \cong L _ { c , b } = L \cap c ^ { \perp } \cap b ^ { \perp } .
$$

We have

$$
L \otimes \mathbb { Q } = L _ { c , b } \otimes \mathbb { Q } \oplus ( \mathbb { Q } b + \mathbb { Q } c ) .
$$

Using the hyperbolic lattice $L _ { c } \otimes \mathbb { R }$ we define a positive cone

$$
C ( L _ { c } ) = \{ x \in L _ { c } \otimes \mathbb { R } \mid ( x , x ) > 0 \} .
$$

We may choose $C ^ { + } ( L _ { c } )$ , one of the two connected components of $C ( L _ { c } )$ so that corresponding tube domain, which is the complexification of $C ^ { + } ( L _ { c } )$

$$
\mathcal { H } _ { c } = L _ { c } \otimes \mathbb { R } + i { \cal C } ^ { + } ( L _ { c } )
$$

has an isomorphism $\mathcal { H } _ { c }  \mathcal { D } _ { L , c } \cong \mathcal { D } _ { L }$ by

$$
z \mapsto [ z ] = z \oplus \big ( b - \frac { ( z , z ) + ( b , b ) } { 2 } c \big ) \quad ( z \in \mathcal { H } _ { c } , [ z ] \in \mathcal { D } _ { L , c } ) .
$$

Using the coordinate $z \in \mathcal { H } _ { c }$ defined by the choice of $c$ and $b$ we can identify an arbitrary modular form $F$ of weight $k$ with a modular form $F _ { c , b }$ (or simply $F _ { c }$ ) on the tube domain $\mathcal { H } _ { c }$ :

$$
F ( \lambda [ z ] ) = \lambda ^ { - k } F _ { c , b } ( z ) .
$$

# 8.3 Fourier expansion at 0-dimensional cusps

In order to define the Fourier expansion at the cusp $c$ we consider an unipotent subgroup of the stabiliser $\tilde { \mathrm { O } } ^ { + } ( L )$ , the subgroup of the Eichler transvections.
For any $a \in c _ { L } ^ { \perp }$ the map

$$
t ^ { \prime } ( c , a ) \colon v \longmapsto v - ( a , v ) c \qquad ( v \in c _ { L } ^ { \bot } )
$$

belongs to the orthogonal group $\mathrm { O } ( c _ { L } ^ { \perp } )$ . It has the unique orthogonal extension on $L$ which is given by the map

$$
t ( c , a ) \colon v \longmapsto v - ( a , v ) c + ( c , v ) a - { \frac { 1 } { 2 } } ( a , a ) ( c , v ) c .
$$

This element is called an Eichler transvection: see [E, Section 3] and [GHS4]. We note that $t ( c , a ) \in \widetilde { \mathrm { S O } } ^ { + } ( L )$ for any $a \in c _ { L } ^ { \perp }$ , that $t ( c , a ) ( c ) = c$ , and that for $a , \ a ^ { \prime } \in c _ { L } ^ { \bot }$

$$
t ( c , a ) t ( c , a ^ { \prime } ) = t ( c , a + a ^ { \prime } ) \quad { \mathrm { a n d } } \quad t ( c , a ) ^ { - 1 } = t ( c , - a ) .
$$

We can identify the lattice $L _ { c , b }$ with the corresponding group of transvections $E _ { c } ( L ) = \langle t ( c , a ) \mid a \in L _ { c } \rangle$ . The group $E _ { c } ( L )$ is the unipotent radical of the parabolic subgroup associated to $c$ . A direct calculation shows that $t ( c , a )$ acts as linear translation in the affine coordinates (48):

$$
t ( c , a ) ( [ z ] ) = [ z + a ] .
$$

Let $F \in M _ { k } ( \widetilde { \mathrm { S O } } ^ { + } ( L ) )$ . Then $F _ { c } ( z + a ) = F _ { c } ( z )$ for all $a \in L _ { c , b }$ and we obtain the Fourier expansion of $F$ at the cusp $c$ :

$$
F _ { c } ( z ) = \sum _ { l \in L _ { c , b } ^ { \vee } } f ( l ) \exp { \left( 2 \pi i \left( l , z \right) \right) } .
$$

The function $F _ { c } ( z )$ is holomorphic at the cusp $c$ if the Fourier coefficient $f ( l )$ can be different from 0 only if its index $l \in L _ { c , b } ^ { \vee }$ belongs to the closure of the positive cone $C ^ { + } ( L _ { c } )$ . Another formulation of this fact is $( l , Y ) > 0$ for any $Y$ in the positive cone $C ^ { + } ( L _ { c } )$ .

Remark 8.6 In general the Fourier expansion (50) depends on the choice of $b$ . For another $b ^ { \prime }$ the Fourier coefficients will be different by a factor $\exp ( 2 \pi i ( l , b - b ^ { \prime } ) )$ which is a root of unity (see details in [GN3, §2.3]). In particular the Fourier coefficient $f _ { 0 }$ (the value of $F$ at the cusp $c$ ) is welldefined.

Remark 8.7 The stabiliser of the cusp $c$ in $\tilde { \mathrm { O } } ^ { + } ( L )$ is isomorphic to the semi-direct product of $\widetilde { \mathrm { O } } ^ { + } ( L _ { c } )$ and $E _ { c } ( L )$ .

Remark 8.8 Let $\mathrm { d i v } _ { L } ( c ) = N$ . Then $\mathrm { d e t } \ : L = N ^ { 2 } \mathrm { d e t } L _ { c }$ . If $\dim ( c ) = 1$ then $c$ can be completed to a hyperbolic plane in $L$ and $L = U \oplus L _ { c }$ . This cusp is called the simplest cusp.
If $\mathrm { d i v } ( c ) > 1$ then $c / \operatorname { d i v } ( c ) + L$ is an isotropic element of the discriminant group $D ( L )$ and $| D ( L ) | = | \operatorname* { d e t } L |$ is divisible by $\mathrm { d i v } ( c ) ^ { 2 }$ . If $D ( L )$ contains no non-trivial isotropic elements (in this case the lattice is maximal) then all $0$ -dimensional cusps are equivalent to the simplest cusp.

Remark 8.9 If $L$ contains two hyperbolic planes then one can use the Eichler criterion (see Lemma 7.5) in order to classify the 0-dimensional cusps with respect to the action of $\widetilde { \mathrm { S O } } ^ { + } ( L )$ . The orbit of $c$ , in this case, is uniquely determined by the isotropic class $c / \operatorname { d i v } ( c ) + L$ in the discriminant group $D ( L )$ .

If $D ( L )$ does not contain isotropic elements (in particular if $\operatorname* { d e t } ( L )$ is square free) then the modular variety $\tilde { \mathrm { O } } ^ { + } ( L ) \backslash \mathcal { D } _ { L }$ has only one 0-dimensional cusp.

Remark 8.10 If $[ \mathrm { O } ( L ) : \Gamma ] < \infty$ and $F \in M _ { k } ( \Gamma , \chi )$ then we can define the Fourier expansion using a sublattice $L _ { c } ( \Gamma )$ of finite index in $L _ { c }$ corresponding to the group $E _ { c } ( L ) \cap \ker \chi$ .

# 8.4 Properties of quasi pull-back

We may consider the quasi pull-back of other modular forms, not only $\Phi _ { 1 2 }$ . If $L$ is of signature $( 2 , n )$ and $r \in L$ is primitive with $( r , r ) < 0$ then $\mathcal { D } _ { r } ( L ) =$ $\mathcal { D } _ { t r } ( L )$ for any $t \in \mathbb { Q } ^ { \times }$ , and we write $r ^ { \perp } = r _ { L } ^ { \perp }$ if there is no ambiguity.

Theorem 8.11 Let $L$ be an integral lattice of signature $( 2 , n )$ . Suppose that the modular form $F \in { \cal M } _ { k } ( \widetilde { \mathrm { S O } } ^ { + } ( L ) )$ vanishes with order $m > 0$ on the rational quadratic divisor $\mathcal { D } _ { r } ( L )$ where $r$ is a primitive vector in $L$ with $( r , r ) < 0$ . We define the quasi pull-back of $F$ on the domain $\mathcal { D } _ { r ^ { \perp } }$ of complex dimension $n - 1$ by

$$
F | _ { r ^ { \perp } } = \left. \frac { F ( Z ) } { ( Z , r ) ^ { m } } \right| _ { { \cal { D } } _ { r ^ { \perp } } } .
$$

Then the quasi pull-back is a cusp form of weight $k + m$

$$
F | _ { r ^ { \perp } } \in S _ { k + m } ( \widetilde { \mathrm { S O } } ^ { + } ( r ^ { \perp } ) ) .
$$

Proof.
There are two parts to the assertion: that $F | _ { r ^ { \perp } }$ is a modular form, and that it vanishes at every cusp.

For the first part, we have the inclusions

$$
r ^ { \perp } \oplus \mathbb { Z } r \subset L \subset L ^ { \vee } \subset ( r ^ { \perp } ) ^ { \vee } \oplus \mathbb { Z } \frac { r } { ( r , r ) } ,
$$

and $r ^ { \perp }$ has signature $( 2 , n - 1 )$ . We consider the two embeddings $\mathcal { D } _ { r ^ { \perp } } \hookrightarrow \mathcal { D } _ { L }$ and $\widetilde { \mathrm { S O } } ^ { + } ( r ^ { \perp } ) \hookrightarrow \widetilde { \mathrm { S O } } ^ { + } ( L )$ . We note that any element $g \in \widetilde { \mathrm { S O } } ^ { + } ( r ^ { \perp } )$ extends to $\tilde { g } \in \widetilde { \mathrm { S O } } ^ { + } ( L )$ by acting trivially on $r$ (see Lemma 7.1). Therefore any $\tilde { g }$ preserves $\mathcal { D } _ { r ^ { \perp } }$ and ${ \tilde { g } } \cdot r = r$ . The function $F | _ { r ^ { \perp } }$ is a holomorphic function on $\mathcal { D } _ { r ^ { \perp } }$ and it is homogeneous of degree $k + m$ . For any $g \in \widetilde { \mathrm { S O } } ^ { + } ( r ^ { \perp } )$ we have

$$
\left. \frac { F ( \tilde { g } Z ) } { ( \tilde { g } Z , r ) ^ { m } } \right| _ { { \cal D } _ { r ^ { \perp } } } = \left. \frac { F ( Z ) } { ( Z , r ) ^ { m } } \right| _ { { \cal D } _ { r ^ { \perp } } } .
$$

Therefore the quasi pull-back $F | _ { r ^ { \perp } }$ is $\widetilde { \mathrm { S O } } ^ { + } ( r ^ { \perp } )$ -invariant.
If instead $F$ has character $\chi$ then $F _ { r ^ { \perp } }$ tranforms according to the induced character $\chi | _ { \widetilde { \mathrm { S O } } ^ { + } ( r ^ { \perp } ) }$ . If $n > 3$ then using Koecher’s principle we conclude that

$$
F | _ { r ^ { \perp } } \in { \cal M } _ { k + m } ( \widetilde { \mathrm { S O } } ( r ^ { \perp } ) ) .
$$

If $n \leq 3$ we cannot apply Koecher’s principle and instead we must use the Fourier expansion to check that the quasi pull-back is a modular form as well as to show the vanishing at the cusps.

We calculate the Fourier expansion of the quasi pull-back at an arbitrary $0$ -dimensional cusp of $r ^ { \perp }$ . Let $c \in r ^ { \bot }$ be a primitive isotropic vector in $r ^ { \perp }$ (if there are any: if not, there is nothing more to prove).
We fix a vector $b \in ( r ^ { \perp } ) ^ { \vee }$ . Then we can define the two homogeneous domains $\mathcal { H } _ { c } ( r ^ { \perp } )$ and $\mathcal { H } _ { c } ( L )$ because the vector $c$ defines also a 0-dimensional cusp of $L$ . We write $Z \in { \mathcal { H } } _ { c } ( L )$ in the form $Z = Z _ { 1 } + z r$ where

$$
Z _ { 1 } \in r ^ { \perp } \otimes \mathbb { C } , \ z = x + i y \in \mathbb { C } , ( \operatorname { I m } Z _ { 1 } , \operatorname { I m } Z _ { 1 } ) + ( r , r ) y ^ { 2 } > 0 .
$$

If $[ Z ]$ is the image of $Z$ in $\mathcal { D } _ { c } ( L )$ (see (48)) then $( [ Z ] , r ) = ( r , r ) z$ . Therefore the equation of the divisor $\mathcal { D } _ { r } ( L )$ in the affine coordinates $Z = Z _ { 1 } \oplus z r \in \mathcal { H } _ { c }$ is $z = 0$ . The quasi pull-back $F | _ { r ^ { \perp } }$ is equal, up to a constant, to the first non-zero coefficient in the Taylor expansion of $F _ { c , b } ( Z )$ in $z$ .

Consider the Fourier expansion

$$
F _ { c , b } ( Z ) = \sum _ { l \in L _ { c , b } ^ { \vee } } f ( l ) \exp { ( 2 \pi i ( l , Z ) ) } .
$$

The modular form $F _ { c , b } ( Z )$ is holomorphic at the boundary.
Therefore $l$ belongs to the closure of the dual cone, in particular, $( l , l ) \geq 0$ . The vectors $c$ and $b$ are orthogonal to $r$ and the lattice $( r ^ { \perp } ) _ { c , b } \oplus \mathbb { Z } r$ is a sublattice of finite index in the lattice of translations $L _ { c , b }$ . For any $Z _ { 1 } \in \mathcal { H } _ { c } ( r ^ { \perp } ) \subset r ^ { \perp } \otimes \mathbb { C }$ we consider $z = x + i y$ such that $Z = Z _ { 1 } \oplus z r \in { \mathcal { H } } _ { c } ( L )$ . (If $y$ is small enough then $( \mathrm { I m } Z _ { 1 } , \mathrm { I m } Z _ { 1 } ) > - ( r , r ) y ^ { 2 } > 0$ .) Therefore we can rewrite the Fourier expansion using this parametrisation

$$
F _ { c , b } ( Z _ { 1 } + z r ) = \sum _ { l _ { 1 } \in ( r ^ { \perp } ) _ { c , b } ^ { \vee } , \ l _ { 2 } \in \mathbb { Z } r / ( r , r ) } f ( l _ { 1 } + l _ { 2 } ) \exp \left( 2 \pi i \left( l _ { 1 } , Z _ { 1 } \right) + z ( l _ { 2 } , r ) \right)
$$

where $( l , l ) = ( l _ { 1 } + l _ { 2 } , l _ { 1 } + l _ { 2 } ) = ( l _ { 1 } , l _ { 1 } ) + ( l _ { 2 } , l _ { 2 } ) \geq 0$ . The Fourier coefficients of $( F | _ { r ^ { \perp } } ) _ { c , b }$ are proportional to the Fourier coefficients of the $m$ -th Taylor coefficient

$$
\frac { \partial ^ { m } F _ { c , b } ( Z _ { 1 } + z r ) } { ( \partial z ) ^ { m } } \bigg | _ { z = 0 } .
$$

The derivatives of the terms in the Fourier expansion (52) vanish if $l _ { 2 } = 0$ . If $( l _ { 2 } , l _ { 2 } ) < 0$ then $( l _ { 1 } , l _ { 1 } ) > 0$ , so nonzero Fourier coefficients occur only when the index $l _ { 1 }$ has positive square.
We have proved this, which is much stronger than just the vanishing of the zeroth coefficient, for an arbitrary 0-dimensional cusp of $r ^ { \perp }$ , so we have shown that $F | _ { r ^ { \perp } }$ is holomorphic at the boundary even for $n = 1$ or $n = 2$ . Moreover the value of $F | _ { r ^ { \perp } }$ at an arbitrary 0-dimensional cusp is zero.

The Baily-Borel compactification of $\widetilde { \mathrm { S O } } ^ { + } ( r ^ { \perp } ) \setminus \mathcal { D } _ { r ^ { \perp } }$ contains only boundary components of dimension 0 and 1 (the latter only if $r ^ { \perp }$ contains a totally isotropic sublattice of rank two).
The Fourier expansion at a 1-dimensional cusp $E$ is called Fourier–Jacobi expansion (see [Ba], [P-S], [G2]). The value of a modular form $G$ on the boundary component $E$ is given by the Siegel operator $\Phi _ { E } ( G )$ (see [BB]). This is the zeroth coefficient of the Fourier– Jacobi expansion which is a modular form with respect to a subgroup of $\operatorname { S L } ( 2 , \mathbb { Z } )$ .

The boundary of a 1-dimensional cusp $E$ is a union of some 0-dimensional cusps.
We consider the Fourier expansion of $\Phi _ { E } ( F | _ { r ^ { \perp } } )$ at a 0-dimensional cusp $c$ associated to $E$ as a part of the Fourier expansion of $( F | _ { r ^ { \perp } } ) _ { c , h }$ (see [Ko1, Section 5.2] for the Fourier expansion of Fourier–Jacobi coefficients of modular forms).
The indices of the Fourier coefficients of $\Phi _ { E } ( F | _ { r ^ { \perp } } )$ are of hyperbolic norm 0. Therefore $\Phi _ { E } ( F | _ { r ^ { \perp } } ) \equiv 0$ because, as shown above, all such coefficients in $( F | _ { r ^ { \bot } } ) _ { c , h }$ are equal to zero.
Therefore the quasi pull-back $F | _ { r ^ { \perp } }$ is a cusp form.
✷

Using Theorem 8.11 we prove that the quasi pull-back defined in Theorem 8.2 is a cusp form.

Corollary 8.12 Let $L \hookrightarrow I I _ { 2 , 2 6 }$ be a nondegenerate sublattice of signature $( 2 , n )$ , $n \geq 1$ . We assume that the set $R _ { - 2 } ( L ^ { \perp } )$ of $\left( - 2 \right)$ -roots in $L ^ { \perp }$ is non-empty.
Then the quasi pull-back $\Phi | _ { L } \in S _ { 1 2 + N ( L ^ { \perp } ) } ( \widetilde { \mathrm { O } } ( L ) , \mathrm { d e t } )$ of the Borcherds form $\Phi _ { \mathrm { 1 2 } }$ is a cusp form.

Proof.
To prove the corollary we divide the procedure of the quasi pull-back of Theorem 8.2 into finitely many steps.

First, we take a root $r _ { 1 } \in R _ { - 2 } ( L ^ { \perp } ) \neq \emptyset$ and define $M _ { 1 } = ( r _ { 1 } ) _ { I I _ { 2 , 2 6 } } ^ { \perp }$ . The form $\Phi _ { \mathrm { 1 2 } }$ has a zero of order $1$ on $\mathcal { D } _ { r _ { 1 } } ( I I _ { 2 , 2 6 } )$ . According to Theorem 8.11 we have

$$
\Phi | _ { M _ { 1 } } = \left. \frac { \Phi _ { 1 2 } ( Z ) } { ( r _ { 1 } , Z ) } \right| _ { M _ { 1 } } \in S _ { 1 3 } ( \widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( M _ { 1 } ) , \det ) .
$$

We note that the cusp form $\Phi | _ { M _ { 1 } }$ might have divisors different from the $\left( - 2 \right)$ - divisors of $\Phi _ { 1 2 }$ . If $s \in R _ { - 2 } ( L ^ { \bot } )$ such that $( r _ { 1 } , s ) \neq 0$ then $s _ { 1 } = \mathrm { p r } _ { M _ { 1 } ^ { \vee } } ( s )$ has negative norm $- 2 < ( s _ { 1 } , s _ { 1 } ) < 0$ and $\Phi | _ { M _ { 1 } }$ vanishes along $\mathcal { D } _ { s _ { 1 } } ( M _ { 1 } )$ according to Lemma 8.1. Therefore the divisors of $\Phi | _ { M _ { 1 } }$ are rational quadratic divisors defined by some vectors in $v \in M _ { 1 } ^ { \vee }$ . But $\mathcal { D } _ { v } ( M _ { 1 } ) = \mathcal { D } _ { t v } ( M _ { 1 } )$ and we can fix $t$ in order to have a primitive vector $t v \in M _ { 1 }$ .

Second, we consider the lattice $L ^ { \perp } \cap M _ { 1 }$ . Suppose first that there is no vector $v \in L ^ { \bot } \cap M _ { 1 }$ such that $\Phi | _ { M _ { 1 } }$ vanishes on $\mathcal { D } _ { v } ( M _ { 1 } )$ . In this case $\Phi | _ { L }$ is equal to the pull-back of $\Phi | _ { M _ { 1 } }$ on $\mathcal { D } _ { L }$ . The pull-back of a cusp form is a cusp form and the proof is finished.

Otherwise, if $r _ { 2 } ~ \in ~ L ^ { \bot } \cap M _ { 1 }$ is a vector such that $\Phi | _ { M _ { 1 } }$ vanishes on $\mathcal { D } _ { r _ { 2 } } ( M _ { 1 } )$ , then we define $M _ { 2 } = ( r _ { 2 } ) _ { M _ { 1 } } ^ { \perp } = \langle r _ { 1 } , r _ { 2 } \rangle _ { I I _ { 2 , 2 6 } } ^ { \perp }$ . As in Theorem 8.11 we have

$$
\Phi | _ { M _ { 2 } } = \left. \frac { \Phi | _ { M _ { 1 } } } { ( r _ { 2 } , Z ) ^ { m } } \right| _ { M _ { 2 } } \in S _ { 1 3 + m } ( \widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( M _ { 2 } ) , \operatorname* { d e t } )
$$

where $m \geq 1$ is the degree of zero of $\Phi | _ { M _ { 1 } }$ on $\mathcal { D } _ { r _ { 2 } } ( M _ { 1 } )$ .

The function $\Phi | _ { M _ { 2 } }$ is a modular form vanishing along some rational quadratic divisors.
We can repeat the procedure described above for $M _ { 2 }$ . After a finite number of steps we get the cusp form $\Phi | _ { L }$ . ✷

Proposition 8.13 Let $L$ be one of the lattices $L _ { 2 d }$ , $\boldsymbol { L } _ { 2 , 2 d }$ or $L _ { Q ( d ) }$ defined in (38)–(41). We assume that there exists an embedding $L \hookrightarrow I I _ { 2 , 2 6 }$ such that the weight of the quasi pull-back $\Phi | _ { L }$ is smaller than the dimension of $\mathcal { D } _ { L }$ . Then $\Phi | _ { L }$ vanishes along the ramification divisor of the modular projection

$$
\pi \colon { \mathcal { D } } _ { L } \to \widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( L ) \setminus { \mathcal { D } } _ { L } .
$$

Proof.
We give here a proof which works for all cases including the moduli spaces of polarised holomorphic symplectic O’Grady varieties (see [GHS6, Corollary 4.6]).

The components of the branch divisor of $\pi$ are $\mathcal { D } _ { r } ( L )$ where $r \in L$ and $\sigma _ { r }$ or $- \sigma _ { r }$ is in $\tilde { \mathrm { O } } ^ { + } ( L )$ (see [GHS1, Corollary 2.13] and Equation (32) above).
If $\sigma _ { r } \in \widetilde { \mathrm { O } } ^ { + } ( L )$ , then $\Phi | _ { L }$ vanishes along $\mathcal { D } _ { r } ( L )$ because $\Phi | _ { L }$ is modular with

character det.
We have to prove that $\Phi | _ { L }$ vanishes also on $\mathcal { D } _ { r } ( L )$ with $- \sigma _ { r } \in \widetilde { \mathrm { O } } ^ { + } ( L )$ . To prove this we use the transitivity of the quasi pull-back construction.
Let $r \in L \hookrightarrow I I _ { 2 , 2 6 }$ and $L _ { r } = r _ { L } ^ { \perp }$ . Then

$$
( \Phi | _ { L } ) | _ { L _ { r } } = \Phi | _ { L _ { r } } .
$$

We have to consider three cases.

1. Let $r \in L = L _ { 2 d }$ . Then $\operatorname { r a n k } L _ { r } = 1 8$ . According to Corollary 7.10 $\operatorname* { d e t } | ( L _ { r } ) _ { I I _ { 2 , 2 6 } } ^ { \perp } | = 1$ or 4. In [CS, Table I] one can find all classes of the indecomposable lattices of small rank and determinant.
   Analysing that table we find three classes of lattices of rank 8 of determinant 1, 2 or 4:

$$
\begin{array} { r } { E _ { 8 } \ ( | R ( E _ { 8 } ) | = 2 4 0 ) , \quad E _ { 7 } \oplus A _ { 1 } \ ( | R ( E _ { 7 } \oplus A _ { 1 } ) | = 1 2 8 ) , \quad D _ { 8 } \ ( | R ( D _ { 8 } ) | = 1 1 2 ) . } \end{array}
$$

Therefore $\Phi _ { 1 2 }$ has a zero of order at least 56 along $\mathcal { D } _ { r } ( L )$ . The modular form $\Phi | _ { L }$ is of weight $k < 1 9$ . Therefore $R ( L _ { I I _ { 2 , 2 6 } } ^ { \perp } )$ has at most 12 roots.
Therefore $\Phi | _ { L }$ vanishes on $\mathcal { D } _ { r } ( L _ { 2 d } )$ with order at least 50.

2. Let $r \in L = L _ { 2 , 2 d }$ . Then $\operatorname { r a n k } L _ { r } = 1 9$ . We described reflective vectors $r$ with $- \sigma _ { r } \in \widetilde { \mathrm { O } } ^ { + } ( L )$ in Proposition 7.9. There are three possible cases:

$$
r ^ { 2 } = 2 d , \mathrm { \ d i v } ( r ) = d \mathrm { \ o r \ 2 } d \mathrm { \quad  a n d \quad } r ^ { 2 } = d = \mathrm { \ d i v } ( r ) ( d \mathrm { \ i s \ o d d } ) .
$$

According to Lemma 7.2, $\operatorname* { d e t } L _ { r } = 2$ , 4 or 8. Therefore the rank 7 lattice (Lr)⊥II2,26 has the same determinant.
According to [CS, Table I] there are six possible classes of such lattices:

$$
E _ { 7 } , D _ { 7 } , D _ { 6 } \oplus A _ { 1 } , A _ { 7 } , [ D _ { 6 } \oplus \langle 8 \rangle ] _ { 2 } , [ E _ { 6 } \oplus \langle 2 4 \rangle ] _ { 3 } ,
$$

where $\lfloor M \rfloor _ { n }$ denotes an overlattice of order $n$ of $M$ . Any of these lattices contains at least 60 roots $( | R ( D _ { 6 } ) | = 6 0 $ ). The modular form $\Phi | _ { L }$ is of weight $k < 2 0$ . Therefore $R ( L _ { I I _ { 2 , 2 6 } } ^ { \perp } )$ has at most 14 roots and $\Phi | _ { L }$ vanishes on $\mathcal { D } _ { r } ( L _ { 2 , 2 d } )$ with order at least 23.

3. Let $r \in L = L _ { Q ( d ) }$ . In this case $d \equiv 3 \mod 4$ , and the discriminant group $D \left( L _ { Q ( d ) } \right)$ is cyclic of order $d$ . Using Proposition 7.9 and Lemma 7.2 we obtain that only one class for $( L _ { r } ) _ { I I _ { 2 , 2 6 } } ^ { \perp }$ is possible.
   This is the lattice $E _ { 7 }$ . We finish the proof as above.
   ✷

# 9 Arithmetic of root systems

In this section we finish the proof of Theorem 6.1. To prove it we use the low weight cusp form trick (Theorem 6.9) by using the quasi pull-back of the Borcherds modular form $\Phi _ { 1 2 }$ to construct cusp forms of small weight with large divisor.

According to Theorem 8.2, Theorem 8.11 and Proposition 8.13 the main point for us is the following.
We want to know for which $2 d > 0$ there exists a vector

$$
l \in E _ { 8 } , \ l ^ { 2 } = 2 d , \ l \ \mathrm { i s \ o r t h o g o n a l \ t o \ a t \ l e a s t \ 2 \ a n d \ a t \ m o s t \ 1 2 \ r o o t s } .
$$

To solve this problem we use the combinatorial geometry of the root system $E _ { 8 }$ together with the theory of quadratic forms.
First we give some properties of the lattice $E _ { 8 }$ and we show how one can construct the first polarisations of general type in Theorem 6.1. After that we outline the answer to the question in (53).

# 9.1 Vectors in $E _ { 8 }$ and $E _ { 7 }$

By definition, the lattice $D _ { 8 }$ is an even sublattice of the Euclidean lattice $\mathbb { Z } ^ { 8 }$

$$
D _ { 8 } = \{ l = ( x _ { 1 } , \ldots , x _ { 8 } ) \in \mathbb { Z } ^ { 8 } | x _ { 1 } + \cdots + x _ { 8 } \in 2 \mathbb { Z } \} .
$$

The determinant of $D _ { 8 }$ is equal to 4. We denote by $e _ { 1 } , \ldots , e _ { 8 }$ the Euclidean basis of $\mathbb { Z } ^ { 8 }$ ( $( e _ { i } , e _ { j } ) = \delta _ { i j }$ ). The lattice $E _ { 8 }$ is the double extension of $D _ { 8 }$ :

$$
E _ { 8 } = D _ { 8 } \cup ( { \frac { e _ { 1 } + \cdot \cdot \cdot + e _ { 8 } } { 2 } } + D _ { 8 } ) .
$$

We consider the Coxeter basis of simple roots in $E _ { 8 }$ (see [Bou])

![](images/d46ac604e32c5ff43f06176b9458871d513946e1ff348854688003ff72e64ecb.jpg)

where

$$
\alpha _ { 1 } = \frac { 1 } { 2 } ( e _ { 1 } + e _ { 8 } ) - \frac { 1 } { 2 } ( e _ { 2 } + e _ { 3 } + e _ { 4 } + e _ { 5 } + e _ { 6 } + e _ { 7 } ) ,
$$

$$
\alpha _ { 2 } = e _ { 1 } + e _ { 2 } , ~ \alpha _ { k } = e _ { k - 1 } - e _ { k - 2 } ~ ( 3 \leq k \leq 8 )
$$

and $E _ { 8 } = \langle \alpha _ { 1 } , \dots \alpha _ { 8 } \rangle _ { \mathbb { Z } }$ . The lattice $E _ { 8 }$ contains 240 roots.
We recall that any root is a sum of simple roots with integral coefficients of the same sign.
The fundamental weights $\omega _ { j }$ of $E _ { 8 }$ form the dual basis, so $( \alpha _ { i } , \omega _ { j } ) = \delta _ { i j }$ . The formulae for the weights are given in [Bou, Tabl. VII]. We shall use the Cartan matrix of the dual basis

$$
\left( \left( \omega _ { i } , \omega _ { j } \right) \right) = \left( \begin{array} { l l l l l l l l } { 4 } & { 5 } & { 7 } & { 1 0 } & { 8 } & { 6 } & { 4 } & { 2 } \\ { 5 } & { 8 } & { 1 0 } & { 1 5 } & { 1 2 } & { 9 } & { 6 } & { 3 } \\ { 7 } & { 1 0 } & { 1 4 } & { 2 0 } & { 1 6 } & { 1 2 } & { 8 } & { 4 } \\ { 1 0 } & { 1 5 } & { 2 0 } & { 3 0 } & { 2 4 } & { 1 8 } & { 1 2 } & { 6 } \\ { 8 } & { 1 2 } & { 1 6 } & { 2 4 } & { 2 0 } & { 1 5 } & { 1 0 } & { 5 } \\ { 6 } & { 9 } & { 1 2 } & { 1 8 } & { 1 5 } & { 1 2 } & { 8 } & { 4 } \\ { 4 } & { 6 } & { 8 } & { 1 2 } & { 1 0 } & { 8 } & { 6 } & { 3 } \\ { 2 } & { 3 } & { 4 } & { 6 } & { 5 } & { 4 } & { 3 } & { 2 } \end{array} \right) .
$$

Let us assume that $l _ { 2 d } \in \ E _ { 8 }$ and $( l _ { 2 d } ) _ { E _ { 8 } } ^ { \perp }$ contains exactly 12 roots.
We consider two cases

$$
R ( ( l _ { 2 d } ) _ { E _ { 8 } } ^ { \perp } ) = A _ { 2 } \oplus 3 A _ { 1 } \quad \mathrm { o r } \quad R ( ( l _ { 2 d } ) _ { E _ { 8 } } ^ { \perp } ) = A _ { 2 } \oplus A _ { 2 } .
$$

There are four possible choices of the subsystem $A _ { 2 } \oplus 3 A _ { 1 }$ inside the Dynkin diagram of $E _ { 8 }$ . There are four choices for a copy of $A _ { 2 }$ :

$$
A _ { 2 } = \langle \alpha _ { 1 } , \alpha _ { 3 } \rangle , ~ \langle \alpha _ { 2 } , \alpha _ { 4 } \rangle , ~ \langle \alpha _ { 5 } , \alpha _ { 6 } \rangle , ~ \langle \alpha _ { 7 } , \alpha _ { 8 } \rangle .
$$

Then the three pairwise orthogonal copies of $A _ { 1 }$ are defined automatically.
For example, if $A _ { 2 } ^ { ( 1 ) } = \langle \alpha _ { 5 } , \alpha _ { 6 } \rangle$ then $3 A _ { 1 } ^ { ( 1 ) } = \left.
\alpha _ { 2 } \right.
\oplus \left.
\alpha _ { 3 } \right.
\oplus \left.
\alpha _ { 8 } \right.$ . The sum $A _ { 2 } ^ { ( 1 ) } \oplus 3 A _ { 1 } ^ { ( 1 ) }$ is the root system of the orthogonal complement of the vector $l _ { 5 , 6 } = \omega _ { 1 } + \omega _ { 4 } + \omega _ { 7 } \in E _ { 8 }$ . In fact, if $\textstyle r = \sum _ { i = 1 } ^ { 8 } x _ { i } \alpha _ { i }$ is a positive root $( x _ { i } \geq 0 )$ then $( r , l _ { 5 , 6 } ) = x _ { 1 } + x _ { 4 } + x _ { 7 } = 0$ . Therefore $x _ { 1 } = x _ { 4 } = x _ { 7 } = 0$ and $r$ belongs to $A _ { 2 } ^ { ( 1 ) } \oplus 3 A _ { 1 } ^ { ( 1 ) }$ (see the Dynkin diagram of $E _ { 8 }$ above).
Using the matrix (54) we find $l _ { 5 , 6 } ^ { 2 } = 4 6$ . Doing similar calculations with

$$
l _ { 1 , 3 } = \omega _ { 4 } + \omega _ { 6 } + \omega _ { 8 } , \quad l _ { 2 , 4 } = \omega _ { 3 } + \omega _ { 5 } + \omega _ { 7 } , \quad l _ { 7 , 8 } = \omega _ { 1 } + \omega _ { 4 } + \omega _ { 6 }
$$

we obtain polarisations for $d = 5 0$ , 54 and 57

$$
l _ { 1 , 3 } ^ { 2 } = 2 \cdot 5 0 , \qquad l _ { 2 , 4 } ^ { 2 } = 2 \cdot 5 4 , \qquad l _ { 7 , 8 } ^ { 2 } = 2 \cdot 5 7 .
$$

To get a good vector for $d = 5 2$ we consider the lattice $M = A _ { 2 } \oplus A _ { 2 } =$ $\langle \alpha _ { 3 } , \alpha _ { 4 } \rangle \oplus \langle \alpha _ { 6 } , \alpha _ { 7 } \rangle$ in $E _ { 8 }$ . Then $M$ is the root system of the orthogonal complement of $l _ { 1 0 4 } = \omega _ { 1 } + \omega _ { 2 } + \omega _ { 5 } + \omega _ { 8 }$ and $l _ { 1 0 4 } ^ { 2 } = 2 \cdot 5 2$ .

In this way we construct the first five polarisations of general type from the list of Theorem 6.1. These elementary arguments, similar to the arguments of Kondo in [Ko3], do not give the whole list but only a few early cases.
A sufficient condition for existence of vectors satisfying (53) is given in the theorem below.

Theorem 9.1 A vector $l$ satisfying (53) does exist if the inequality

$$
4 N _ { E 7 } ( 2 d ) > 2 8 N _ { E 6 } ( 2 d ) + 6 3 N _ { D 6 } ( 2 d )
$$

is valid, where $N _ { L } ( 2 d )$ denotes the number of representations of $2 d$ by the lattice $L$ .

Proof.
We use bouquets of copies of $A _ { 2 }$ in $E _ { 8 } \backslash E _ { 7 }$ . The root system $R ( E _ { 8 } )$ is a disjoint union of 126 roots of $E _ { 7 }$ and the bouquet of 28 copies of $A _ { 2 }$ centred in $A _ { 1 }$ . This fact explains the coefficients 28 and 63 in the right hand side of (55). See [GHS1, Section 7] for more details.
✷

In [GHS1] we found explicit formulae for the numbers of representations and we proved that

$$
N _ { E _ { 7 } } ( 2 m ) > \frac { 2 4 \pi ^ { 3 } } { 5 \zeta ( 3 ) } , \qquad 2 1 m ^ { 2 } > N _ { D _ { 6 } } ( 2 d ) , \qquad 1 0 3 . 6 9 m ^ { 2 } > N _ { E _ { 6 } } ( 2 d ) .
$$

These inequalities give a finite set of $d$ for which (55) is not valid.
Analysing the corresponding theta series we found the set of all such $d$ , containing 131 numbers.
The five tables in [GHS1, Section 7] and the argument above for $d = 5 2$ give the list of polarisations of general type of Theorem 6.1.

The geometric genus of $\mathcal { F } _ { 2 d }$ is positive if there exists a cusp form of canonical weight 19. For each $d$ not in the general type list but satisfying $d \geq 4 0$ and $d \neq 4 1$ , 44, 45 or 47, there exists a vector $h _ { 2 d } \in E _ { 8 }$ of length $2 d$ orthogonal exactly to 14 roots.
The corresponding quasi pull-back is a cusp forms of canonical weight.
For $d = 4 2$ , 43, 51, 53 and 55 such cusp forms were constructed by Kondo in [Ko3]. For other $d$ see [GHS1].

A similar arithmetic method applied to $E _ { 7 }$ (see [GHS5, Section 4]) gives the proof of Theorem 6.2. There is a significant technical difficulty in the case of $E _ { 7 }$ . The proof involves estimating the number of ways of representing certain integers by various root lattices of odd rank.
In [GHS5, Section 5]) we gave a new, clear, explicit version of Siegel’s formula for this number in the odd rank case.
It may be expressed either in terms of Zagier $L$ -functions or in terms of the H. Cohen numbers.
For example we obtained a new, very short formula for the number of representations by 5 squares (see [GHS5, Section 4] for the details).

# 9.2 Binary quadratic forms in $E _ { 8 }$

We saw in Example 4.5 that the results of Debarre and Voisin [DV] imply that the moduli space $\mathcal { M } _ { 2 \cdot 1 1 } ^ { [ 2 ] , \mathrm { n o n - s p l i t } }$ of Beauville degree $d = 1 1$ is unirational.
We note that M[2],split2·11 , which is a finite covering of $\mathcal { M } _ { 2 \cdot 1 1 } ^ { [ 2 ] , \mathrm { n o n - s p l i t } }$ by (42), has non-negative Kodaira dimension.
Theorem 6.2 shows that there can be at most 11 exceptional split polarisations of non general type.
Proposition 9.2 hints that one can expect a theorem for the non-split case, which we hope to prove in the future, similar to Theorem 6.2.

We recall that the Beauville degree $d \equiv - 1$ mod 4 if the polarisation $h _ { 2 d }$ is of non-split type.
For small $d$ we can calculate the class of the orthogonal complement of $Q ( d )$ . According to [CS, Table 0] the rank 6 lattice $Q ( d ) _ { E _ { 8 } } ^ { \perp }$ of determinant $d$ contains at least 24 roots for $d = 3$ , 7, 11 and 15. One can continue this analysis but we propose below a simple algorithm which gives us the first “good” embeddings of $Q ( d )$ in $E _ { 8 }$ .

Proposition 9.2 The moduli spaces $\mathcal { M } _ { 2 \cdot 3 9 } ^ { [ 2 ] , n o n - s p l i t }$ and M[2],no2·47 $\mathcal { M } _ { 2 \cdot 4 7 } ^ { [ 2 ] , n o n - s p l i t }$ are of general type.

Proof.
Let $Q ( d ) ( - 1 ) = \left( \begin{array} { c c } { { 2 } } & { { - 1 } } \\ { { - 1 } } & { { 2 c } } \end{array} \right) $ where $c = ( d + 1 ) / 4$ , be the binary quadratic form associated to a non-split polarisation of degree $2 d$ (see (41)). To make the notation simpler we denote this binary form by $Q ( d )$ . We have to embed $Q ( d )$ in $E _ { 8 }$ so as to satisfy

$$
2 \leq | R ( Q ( d ) _ { E _ { 8 } } ^ { \perp } ) | \leq 1 4 .
$$

We describe below a method (we call it $\textstyle { \frac { 1 } { 2 } } ( + + )$ -algorithm) which gives many such embeddings.
We take the following realisation of the binary quadratic form of determinant $d$ in $E _ { 8 }$ :

$$
Q ( d ) = \langle e _ { 2 } - e _ { 1 } , v _ { 2 c } \rangle = \langle e _ { 2 } - e _ { 1 } , \frac { 1 } { 2 } ( e _ { 1 } - e _ { 2 } + x _ { 3 } e _ { 3 } + \cdot \cdot \cdot + x _ { 8 } e _ { 8 } ) \rangle ,
$$

where $x _ { i } \geq 0$ and $2 c = ( 2 + x _ { 3 } ^ { 2 } + \cdot \cdot \cdot + x _ { 8 } ^ { 2 } ) / 4$ . The second generator $v _ { 2 c }$ of the binary quadratic form is a half-integral element of $E _ { 8 }$ . According to the definition of $E _ { 8 }$ given above

$$
v _ { 2 c } + \frac { 1 } { 2 } ( e _ { 1 } + \cdot \cdot \cdot + e _ { 8 } ) = e _ { 1 } + \frac { x _ { 3 } + 1 } { 2 } e _ { 3 } + \cdot \cdot \cdot + \frac { x _ { 8 } + 1 } { 2 } e _ { 8 } \in D _ { 8 } .
$$

Therefore $x _ { 3 } \equiv \cdots \equiv x _ { 8 }$ mod 2 and $x _ { 3 } + \cdot \cdot \cdot + x _ { 8 } \equiv 0$ mod 4. Now we can find all roots orthogonal to $Q ( d )$ .

First, we consider the integral roots of $E _ { 8 }$ . The roots $\pm ( e _ { 1 } + e _ { 2 } )$ are orthogonal to $Q ( d )$ therefore $R ( Q ( d ) _ { E _ { 8 } } ^ { \perp } )$ is not empty.
Then the integral roots $\pm ( e _ { i } \pm e _ { j } )$ $( i , j > 2 )$ are orthogonal to $Q ( d )$ if and only if $x _ { i } = \mp x _ { j }$ .

Second, a half-integral root orthogonal to $Q ( d )$ has the form

$$
\pm \frac { 1 } { 2 } ( e _ { 1 } + e _ { 2 } + \sum _ { i = 3 } ^ { 8 } ( - 1 ) ^ { \varepsilon _ { i } } e _ { i } )
$$

where the number of $-$ signs in the sum is even.
Therefore $v _ { 2 c }$ is orthogonal to a half-integral root if and only if we can divide the vector of coefficients $( x _ { 3 } , \ldots , x _ { 8 } )$ in two parts containing even number of terms and with the same sum.
If this is possible there are two pairs of roots orthogonal to $v _ { 2 c }$ . For example, if there is a root of type $\pm ( + + ; + + + + -- )$ then we also have $\pm ( + + ; -- -- + + )$ . The rules described above give the number (it is always positive) of roots orthogonal to $Q ( d )$ .

To finish the proof of Proposition 9.2 we consider two vectors

$$
v _ { 2 0 } = { \frac { 1 } { 2 } } ( 1 , 1 ; 5 , 5 , 3 , 3 , 3 , 1 ) \quad { \mathrm { a n d } } \quad v _ { 2 4 } = { \frac { 1 } { 2 } } ( 1 , 1 ; 7 , 5 , 3 , 3 , 1 , 1 ) .
$$

The quadratic forms $Q ( 3 9 )$ and $Q ( 4 7 )$ are orthogonal to exactly 14 roots in $E _ { 8 }$ . As above, using Theorem 8.2, Theorem 8.11 and Proposition 8.13 we see that the quasi pull-back of $\Phi _ { 1 2 }$ on the modular variety defined by the lattice $L _ { Q ( d ) }$ is a cusp form of weight 19 vanishing on the ramification divisor.
We finish the proof using Theorem 6.9. ✷

# References

[Ap] A. Apostolov, Forthcoming thesis, Leibniz Universit¨at Hannover.\
[AMRT] A. Ash, D. Mumford, M. Rapoport, Y. Tai, Smooth compactification of locally symmetric varieties.
Lie Groups: History, Frontiers and Applications, Vol. IV. Math.
Sci.
Press, Brookline, Mass., 1975.\
[Ar] M. Artin, Supersingular K3 surfaces.
Ann.
Scient.
Ec.
Norm.
Sup.
´ (4) 7 (1974), 543–568.\
[Ba] W.L. Baily, Fourier-Jacobi series, in Algebraic Groups and Discontinuous Subgroups, Proc.
Symp.
Pure Math.
Vol. IX, eds.
A. Borel, G. D. Mostow, Amer.
Math.
Soc., Providence, Rhode Island, 1966, 296–300.\
[BB] W.L. Baily Jr., A. Borel, Compactification of arithmetic quotients of bounded symmetric domains.
Ann.
of Math.
(2) 84 (1966), 442– 528.\
[BHPV] W. Barth, K. Hulek.
C. Peters, A. Van de Ven, Compact complex surfaces.
Second Enlarged Edition, Springer Verlag 2004.\
[Bau] J. Bauermann, Lokale Tensorfelder auf arithmetischen Quotienten symmetrischer beschr¨ankter Gebiete.
J. reine angew.
Math.
428 (1992), 111–138.\
[Be] A. Beauville, Vari´et´es K¨ahleriennes dont la premi\`ere classe de Chern est nulle.
J. Differential Geometry 18 (1983), 755–782.\
[BJ] A. Borel, L. Ji, Compactifications of symmetric and locally symmetric spaces.
Mathematics: Theory & Applications.
Birkh¨auser, Boston 2006.\
[Bog1] F. Bogomolov, Hamiltonian K¨ahlerian manifolds.
(Russian) Dokl.
Akad.
Nauk SSSR 243 (1978), 1101–1104.\
[Bog2] F. Bogomolov, The decomposition of K¨ahler manifolds with a trivial canonical class.
Mat.
Sb.
(N.S.) 93(135) (1974), 573–575, 630.\
[B1] R.E. Borcherds, Automorphic forms on $O _ { s + 2 , 2 } ( R )$ and infinite products.
Invent.
Math.
120 (1995), 161–213.\
[B2] R.E. Borcherds, The moduli space of Enriques surfaces and the fake monster Lie superalgebra.
Topology 35 (1996), 699–710.\
[B3] R.E. Borcherds, Automorphic forms with singularities on Grassmannians.
Invent.
Math.
132 (1998), 491–562.\
[BKPS] R.E. Borcherds, L. Katzarkov, T. Pantev, N.I. Shepherd-Barron, Families of K3 surfaces.
J. Algebraic Geom.
7 (1998), 183–193.\
[Bl] A. Borel, Some metric properties of arithmetic quotients of symmetric spaces and an extension theorem.
J. Differential Geometry 6 (1972), 543–560.\
[Bou] N. Bourbaki, Groupes et Alg\`ebres de Lie, Chapitres 4, 5 et 6. Hermann, 1968.\
[Br] R. Brussee, The canonical class and the $C ^ { \infty }$ properties of K¨ahler surfaces.
New York J. Math.
2 (1996), 103–146.\
[Bu] N. Buchdahl, On compact K¨ahler surfaces.
Ann.
Inst.
Fourier (Grenoble) 49 (1999), 287–302.\
[BR] D. Burns, M. Rapoport, On the Torelli problem for K¨ahlerian K3 surfaces., Ann.
Sc.
ENS. 8 (1975), 235–274.\
[Ca] H. Cartan, Quotient d’un espace analytique par un groupe d’automorphismes.
In: A symposium in honor of S. Lefschetz, Algebraic geometry and topology, 90–102. Princeton University Press, Princeton 1957.\
[Ch] C. Chevalley, Invariants of finite groups generated by reflections.
Amer.
J. Math.
77 (1955), 778–782.\
[CS] J.H. Conway, N.J.A. Sloane, Low-dimensional lattices I: quadratic forms of small determinant.
Proc.
Roy.
Soc.
London Ser.
A 418 (1988), no. 1854, 17–41.\
[Deb] O. Debarre, Un contre-exemple au th´eor\`eme de Torelli pour les vari´et´es symplectiques irr´eductibles.
C. R. Acad.
Sci.
Paris S´er.
I Math.
299 (1984), 681–684.\
[DV] O. Debarre, C. Voisin, Hyper-K¨ahler fourfolds and Grassmann geometry.
arXiv:0904.3974, 27 pp.\
[Do] I. Dolgachev, Mirror symmetry for lattice polarized K3 surfaces.
J. Math.
Sci.
81 (1996), 2599–2630.\
[DGK] I. Dolgachev, B. van Geemen, S. Kondo, A complex ball uniformization of the moduli space of cubic surfaces via periods of K3 surfaces.
J. Reine Angew.
Math.
588 (2005), 99–148.\
[DK] I. Dolgachev, S. Kondo, Moduli of K3 surfaces and complex ball quotients.
Arithmetic and geometry around hypergeometric functions, 43–100, Progr.
Math.
260, Birkh¨auser, Basel, 2007.\
[D¨u] M. D¨urr, Seiberg-Witten theory and the $C ^ { \infty }$ -classification of complex surfaces.
Ph.D. thesis, Z¨urich 2002.\
[E] M. Eichler, Quadratische Formen und orthogonale Gruppen.
Grundlehren der mathematischen Wissenschaften 63. SpringerVerlag, Berlin-New York, 1974.\
[FC] G. Faltings, C.-L. Chai, Degeneration of abelian varieties.
Ergebnisse der Mathematik und ihrer Grenzgebiete (3), 22 SpringerVerlag, Berlin, 1990.\
[F1] E. Freitag, Siegelsche Modulfunktionen.
Grundlehren der mathematischen Wissenschaften 254. Springer-Verlag, Berlin– G¨ottingen–Heidelberg, 1983.\
[F2] E. Freitag, Some modular forms related to cubic surfaces.
Kyungpook Math.
J. 43 (2003), 433–462.\
[Fr] R. Friedman A new proof of the global Torelli theorem for K3 surfaces.
Ann.
of Math.
(2) 120 (1984), 237–269.\
[FM] R. Friedman, J.W. Morgan, Algebraic surfaces and Seiberg-Witten invariants.
J. Algebraic Geom.
6 (1997), 445–479.\
[Fuj] A. Fujiki, On the de Rham cohomology group of a compact K¨ahler symplectic manifold.
In Algebraic geometry, Sendai, 1985. Adv.
Stud.
Pure Math.
10, 105–165. North-Holland, Amsterdam 1987.\
[GaS] A. Garbagnati, A. Sarti, Elliptic fibrations and symplectic automorphisms on K3 surfaces.
Comm.
Algebra 37 (2009), 3601–3631.\
[G1] V. Gritsenko, Jacobi functions of n-variables.
Zap.
Nauk.
Sem.
LOMI 168 (1988), 32–45 English transl.
in J. Soviet Math˙53 (1991), 243–252.\
[G2] V. Gritsenko, Modular forms and moduli spaces of Abelian and K3 surfaces.
Algebra i Analiz 6 (1994), 65–102; English translation in St. Petersburg Math.
J. 6 (1995), 1179–1208.\
[G3] V. Gritsenko, Irrationality of the moduli spaces of polarized Abelian surfaces.
Internat.
Math.
Res.
Notices 6 (1994), 235–243.\
[G4] V. Gritsenko, Reflective modular forms in algebraic geometry.
arXiv:1005.3753, 28 pp.\
[GH1] V. Gritsenko, K. Hulek, Appendix to the paper “Irrationality of the moduli spaces of polarized abelian surfaces”.
Abelian varieties.
Proceedings of the international conference held in Egloffstein, 83– 84. Walter de Gruyter Berlin, 1995.\
[GH2] V. Gritsenko, K. Hulek, Minimal Siegel modular threefolds.
Math.
Proc.
Cambridge Philos.
Soc.
123 (1998), 461–485.\
[GH3] V. Gritsenko, K. Hulek, Commutator coverings of Siegel threefolds.
Duke Math.
J. 94 (1998), 509–542.\
[GHS1] V. Gritsenko, K. Hulek, G.K. Sankaran, The Kodaira dimension of the moduli of K3 surfaces.
Invent.
Math.
169 (2007), 519–567.\
[GHS2] V. Gritsenko, K. Hulek, G.K. Sankaran, The Hirzebruch-Mumford volume for the orthogonal group and applications.
Documenta Math.
12 (2007), 215–241.\
[GHS3] V. Gritsenko, K. Hulek, G.K. Sankaran, Hirzebruch-Mumford proportionality and locally symmetric varieties of orthogonal type.
Documenta Mathematica 13 (2008), 1-19.\
[GHS4] V. Gritsenko, K. Hulek, G.K. Sankaran, Abelianisation of orthogonal groups and the fundamental group of modular varieties.
J. of Algebra 322 (2009), 463–478.\
[GHS5] V. Gritsenko, K. Hulek, G.K. Sankaran, Moduli spaces of irreducible symplectic manifolds.
Compos.
Math.
146 (2010), 404–434.\
[GHS6] V. Gritsenko, K. Hulek, G.K. Sankaran, Moduli spaces of polarised symplectic O’Grady varieties and Borcherds products.
J. Diff.
Geom., to appear.\
[GN1] V. Gritsenko, V. Nikulin, Siegel automorphic form correction of some Lorentzian Kac–Moody Lie algebras.
Amer.
J. Math.
119 (1997), 181–224.\
[GN2] V. Gritsenko, V. Nikulin, Automorphic forms and Lorentzian KacMoody algebras.
I. International J. Math.
9 (2) (1998), 153–200.\
[GN3] V. Gritsenko, V. Nikulin, Automorphic forms and Lorentzian KacMoody algebras.
II. International J. Math.
9 (2) (1998), 201–275.\
[GN4] V. Gritsenko, V. Nikulin, K3 surfaces, Lorentzian Kac–Moody algebras and mirror symmetry.
Math.
Res.
Lett.
3 (1996), 211–229.\
[GN5] V. Gritsenko, V. Nikulin, The arithmetic mirror symmetry and Calabi–Yau manifolds.
Comm.
Math.
Phys.
200 (2000), 1–11.\
[GS] V. Gritsenko, G.K. Sankaran, Moduli of abelian surfaces with a $( 1 , p ^ { 2 } )$ polarisation.
Izv.
Ross.
Akad.
Nauk Ser.
Mat.
60 (1996), 19–26; reprinted in Izv.
Math.
60 (1996), 893–900.\
[HT1] B. Hassett, Y. Tschinkel, Moving and ample cones of holomorphic symplectic fourfolds.
Geometric and Functional Analysis 19 (2009), 1065–1080.\
[HT2] B. Hassett, Y. Tschinkel, Flops on holomorphic symplectic fourfolds and determinantal cubic hypersurfaces.
J. Inst.
Math.
Jussieu 9 (2010), 125–153.\
[Hel] S. Helgason, Differential geometry, Lie groups, and symmetric spaces.
Graduate Studies in Mathematics 34, AMS, Providence 2001.\
[Hor1] E. Horikawa, Surjectivity of the period map of K3 surfaces of degree 2. Math.
Ann.
228 (1977), 113–146.\
[Hor2] E. Horikawa, On the periods of Enriques surfaces I. Proc.
Japan Acad.
53 (1977), 124–127.\
[Huy1] D. Huybrechts, Compact hyper-K¨ahler manifolds: basic results.
Invent.
Math.
135 (1999), 63–113.\
[Huy2] D. Huybrechts, A global Torelli theorem for hyperk¨ahler manifolds [after Verbitsky]. S´eminaire Bourbaki 2011.\
[IR1] A. Iliev, K. Ranestad, K3 surfaces of genus 8 and varieties of sums of powers of cubic fourfolds.
Trans.
Amer.
Math.
Soc.
353 (2001), 1455–1468.\
[IR2] A. Iliev, K. Ranestad, Addendum to K3 surfaces of genus 8 and varieties of sums of powers of cubic fourfolds.
C. R. Acad.
Bulgare Sci.
60 (2007), 1265–1270.\
[KLS] D. Kaledin, M. Lehn, C. Sorger, Singular symplectic moduli spaces.
Invent.
Math.
164 (2006), 591–614.\
[Ka] D. Kazhdan, On the connection of the dual space of a group with the structure of its closed subgroups.
Funkcional.
Anal.
i Pril.
1 (1967), 71–74.\
[Kaw] Y. Kawamata, Unobstructed deformations.
A remark on a paper of Z. Ran.
J. Algebraic Geom.
1 (1992), 183–190.\
[Kn] M. Kneser, Erzeugung ganzzahliger orthogonaler Gruppen durch Spiegelungen.
Math.
Ann.
255 (1981), 453–462.\
[Kod] K. Kodaira, On the structure of compact complex analytic surfaces.
I. Amer.
J. Math.
86 (1964), 751–789.\
[KS] K. Kodaira, D. C. Spencer, On deformations of complex analytic structures.
III. Stability theorems for complex structures.
Ann.
of Math.
(2) 71 (1960), 43–76.\
[KM] J. Koll´ar, T. Matsusaka, Riemann-Roch type inequalities.
Amer.
J. Math.
105 (1983), 229–252.\
[Ko1] S. Kondo, On the Kodaira dimension of the moduli space of K3 surfaces.
Compositio Math.
89 (1993), 251–299.\
[Ko2] S. Kondo, The rationality of the moduli space of Enriques surfaces.
Compositio Math.
91 (1994), 159–173.\
[Ko3] S. Kondo, On the Kodaira dimension of the moduli space of K3 surfaces.
II. Compositio Math.
116 (1999), 111–117.\
[Kul] V. Kulikov Degenerations of K3 surfaces and Enriques surfaces.
Izv.
Akad.
Nauk SSSR Ser.
Mat.
41 (1977), 1008–1042, 1199.\
[La] A. Lamari, Courants k¨ahl´eriens et surfaces compactes.
Ann.
Inst.
Fourier (Grenoble) 49 (1999), 263–285.\
[LM] D. Lieberman, D. Mumford, Matsusaka’s big theorem.
In Algebraic geometry, Arcata, 1974. Proc.
Sympos.
Pure Math.
29, 513–530. AMS, Providence 1975.\
[Lo] E. Looijenga, A Torelli theorem for K¨ahler-Einstein K3 surfaces., Lecture Notes in Math.
894, 107–112, Springer, Berlin-New York, 1981.\
[LP] E. Looijenga, C. Peters, Torelli theorems for K¨ahler K3 surfaces.
Compos.
Math.
42 (1981), 145–186.\
[Ma] S. Ma, The unirationality of the moduli spaces of 2-elementary K3 surfaces.
With an appendix by K. Yoshikawa.
arXiv:1011.1963\
[Mar1] E. Markman, On the monodromy of moduli spaces of sheaves on K3 surfaces.
J. Algebraic Geom.
17 (2008), 29–99.\
[Mar2] E. Markman, On the monodromy of moduli spaces of sheaves on K3 surfaces II. math.AG/0305043, 76 pp.\
[Mar3] E. Markman, Integral constraints on the monodromy group of the hyperkahler resolution of a symmetric product of a K3 surface.
Internat.
J. Math.
21 (2010), 169–223.\
[Mar4] E. Markman, A survey of Torelli and monodromy results for holomorphic-symplectic varieties.
To appear: Complex and Differential Geometry, Conference held at Leibniz Universit¨at Hannover, September 14 - 18, 2009. arXiv:1101.4606\
[Mat] T. Matsusaka, Polarized varieties with a given Hilbert polynomial.
Amer.
J. Math.
94 (1972), 1027–1077.\
[Mo] D. Morrison, Some remarks on the moduli of K3 surfaces.
Classification of algebraic and analytic manifolds (Katata, 1982), Progr.
Math., 39, Birkh¨auser Boston, Boston, MA, 1983, 303–332.\
[Mu1] S. Mukai, Curves, K3 surfaces and Fano 3-folds of genus ≤ 10. Algebraic geometry and commutative algebra, Vol. I, 357–377, Kinokuniya, Tokyo, 1988.\
[Mu2] S. Mukai, Polarized K3 surfaces of genus 18 and 20. Complex projective geometry (Trieste, 1989/Bergen, 1989), 264–276, London Math.
Soc.
Lecture Note Ser., 179, Cambridge Univ. Press, Cambridge, 1992.\
[Mu3] S. Mukai, Curves and K3 surfaces of genus eleven.
Moduli of vector bundles (Sanda, 1994; Kyoto, 1994), 189–197, Lecture Notes in Pure and Appl.
Math., 179, Dekker, New York, 1996.\
[Mu4] S. Mukai, Polarized K3 surfaces of genus thirteen.
Moduli spaces and arithmetic geometry (Kyoto 2004), 315–326, Adv.
Stud.
Pure Math., 45, Math.
Soc.
Japan, Tokyo, 2006.\
[Mu5] S. Mukai, Polarized K3 surfaces of genus sixteen.
Oberwolfach Report 02/2010, DOI: 10.4171/OWR/2010/02.\
[Mum] D. Mumford, Hirzebruch’s proportionality theorem in the noncompact case.
Invent.
Math.
42 (1977), 239–272.\
[Nam] Y. Namikawa, Counter-example to global Torelli problem for irreducible symplectic manifolds.
Math.
Ann.
324 (2002), 841–845.\
[Nik1] V.V. Nikulin, Finite automorphism groups of K¨ahler K3 surfaces.
Trudy Moskov.
Mat.
Obshch.
38 (1979), 75–137. English translation in Trans.
Mosc.
Math.
Soc.
2, 71-135 (1980).\
[Nik2] V.V. Nikulin, Integral symmetric bilinear forms and some of their applications.
Izv.
Akad.
Nauk SSSR Ser.
Mat.
43 (1979), 111–177. English translation in Math.
USSR, Izvestiia 14 (1980), 103–167.\
[Nyg] N. O. Nygaard, The Torelli theorem for ordinary K3 surfaces over finite fields.
In: Arithmetic and geometry, Progr.
Math.
35, Vol. I, 267–276, Birkh¨auser Boston, Boston, MA, 1983.\
[OG1] K. O’Grady, Desingularized moduli spaces of sheaves on a K3. J. Reine Angew.
Math.
512 (1999), 49–117.\
[OG2] K. O’Grady, A new six-dimensional irreducible symplectic variety.
J. Algebraic Geom.
12 (2003), 435–505.\
[OG4] K. O’Grady, Irreducible symplectic 4-folds and Eisenbud-PopescuWalter sextics.
Duke Math.
J. 134 (2006), 99–137.\
[Ogu] A. Ogus, A crystalline Torelli theorem for supersingular K3 surfaces.
In: Arithmetic and geometry, Progr.
Math.
36, Vol. II, 361– 394, Birkh¨auser, Boston, Boston, MA, 1983.\
[OV] C. Okonek, A. Van de Ven, Stable bundles, instantons and $C ^ { \infty }$ - structures on algebraic surfaces.
Several complex variables VI, Encyclopaedia Math.
Sci.
69, 197–249, Springer, Berlin, 1990.\
[Ol] M. Olsson, Semistable degenerations and period spaces for polarized K3 surfaces.
Duke Math.
J. 125 (2004), 121–203.\
[PP] U. Persson, H. Pinkham, Degeneration of surfaces with trivial canonical bundle.
Ann.
of Math.
(2) 113 (1981), 45–66.\
[PeSa] A. Peterson, G.K. Sankaran, On some lattice computations related to moduli problems.
With an appendix by V. Gritsenko.
Rend.
Semin.
Mat.
Univ. Politec.
Torino 68 (2010), 289–304.\
[P-S] I.I. Piatetskii-Shapiro Automorphic functions and the geometry of classical domains.
Gordon and Breach, New York, 1969.\
[P-SS] I. Piatetskii-Shapiro, I. Shafarevich, A Torelli theorem for algebraic surfaces of type K3. Izv.
Akad.
Nauk SSSR, Ser.
Mat.
35, 530–572 (1971). English translation in Math.
USSR, Izv.
5 (1971), 547–588 (1972).\
[Ran] Z. Ran, Deformations of manifolds with torsion or negative canonical bundle.
J. Algebraic Geom.
1 (1992), 279–291.\
[Rap1] A. Rapagnetta, On the Beauville form of the known irreducible symplectic varieties.
Math.
Ann.
340 (2008), 77–95.\
[Rap2] A. Rapagnetta, Topological invariants of O’Grady’s six dimensional irreducible symplectic variety.
Math.
Z. 256 (2007), 1–34.\
[Re] M. Reid, Young person’s guide to canonical singularities.
In: Algebraic geometry, Bowdoin, 1985 (Brunswick, Maine, 1985), 345– 414, Proc.
Sympos.
Pure Math., 46, Part 1, Amer.
Math.
Soc., Providence, RI, 1987.\
[S-D] B. Saint-Donat, Projective models of K3 surfaces.
Amer.
J. Math.
96 (1974), 602–639.\
[Sat] I. Satake, Algebraic structures of symmetric domains.
Kano Memorial Lectures 4. Iwanami Shoten, Tokyo; Princeton University Press, Princeton, N.J., 1980.\
[Sc] F. Scattone, On the compactification of moduli spaces of algebraic K3 surfaces., Mem.
Amer.
Math.
Soc.
70, no. 374, (1987).\
[Sch] M. Sch¨utt, Arithmetic of K3 surfaces.
Jahresber.
Deutsch.
Math.- Verein.
111 (2009), 23–41.\
[Sha1] J. Shah, Surjectivity of the period map in the case of quartic surfaces and sextic double planes.
Bull.
Amer.
Math.
Soc.
82 (1976), 716–718.\
[Sha2] J. Shah, A complete moduli space for K3 surfaces of degree 2. Ann.
of Math.
(2) 112 (1980), 485–510.\
[Sha3] J. Shah, Degenerations of K3 surfaces of degree 4. Trans.
Amer.
Math.
Soc.
263 (1981), 271–308.\
[S-B1] N.I. Shepherd-Barron, The rationality of some moduli spaces of plane curves.
Compos.
Math.
67 (1988), 51–88.\
[S-B2] N.I. Shepherd-Barron, Apolarity and its applications.
Invent.
Math.
97 (1989), 433–444.\
[St] H. Sterk, Lattices and K3 surfaces of degree 6. Linear Algebra Appl.
226–228 (1995), 297–309.\
[Siu] Y. T. Siu, Every K3 surface is K¨ahler.
Invent.
Math.
73 (1983), 139–150.\
[Ti] G. Tian, Smoothness of the universal deformation space of compact Calabi-Yau manifolds and its Petersson-Weil metric.
In: Mathematical aspects of string theory (S.-T. Yau, Ed.). Advanced Series in Mathematical Physics 1, 629–646. World Scientific, Singapore 1987.\
[Tod] A.N. Todorov, The Weil-Petersson geometry of the moduli space of SU( $n \geq 3$ ) (Calabi-Yau) manifolds I. Comm.
Math.
Phys.
126 (1989), 325–346.\
[Ta] Y. Tai, On the Kodaira dimension of the moduli space of abelian varieties.
Invent.
Math.
68 (1982), 425–439.\
[Ver] M. Verbitsky, A global Torelli theorem for hyperkahler manifolds.
arXiv:0908.4121, 47 pp.\
[Vi] E. Viehweg, Quasi-projective moduli for polarized manifolds.
Ergebnisse der Mathematik und ihrer Grenzgebiete (3), 30. SpringerVerlag, Berlin, 1995.\
[Vo1] C. Voisin, Th´eor\`eme de Torelli pour les cubiques de $\mathbb { P } ^ { 5 }$ . Invent.
Math.
86 (1986), 577–601.\
[Vo2] C. Voisin, G´eom´etrie des espaces de modules de courbes et de surfaces K3 [d’apr\`es Gritsenko-Hulek-Sankaran, Farkas-Popa, Mukai, Verra. . . ]. S´eminaire BOURBAKI 59\`eme ann´ee, 2006–2007, n 981.\
[Wei] A. Weil, Oeuvres scientifiques – Collected papers, Volumes I, II, III, Springer Verlag 1979.\
[Zo] M. Zowislok On moduli spaces of sheaves on K3 or abelian surfaces.
arXiv:1104.5629, 24 pp.\
V. Gritsenko\
Universit´e Lille 1\
Laboratoire Paul Painlev´e\
F-59655 Villeneuve d’Ascq, Cedex\
France\
mailto:valery.gritsenko@math.univ-lille1.fr\
K. Hulek\
Institut f¨ur Algebraische Geometrie\
Leibniz Universit¨at Hannover\
D-30060 Hannover\
Germany\
mailto:hulek@math.uni-hannover.de\
G.K. Sankaran\
Department of Mathematical Sciences\
University of Bath\
Bath BA2 7AY\
England\
mailto:g.k.sankaran@bath.ac.uk
