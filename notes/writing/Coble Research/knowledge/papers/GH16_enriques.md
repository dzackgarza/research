---
title: Moduli of polarized Enriques surfaces
authors:
- Gritsenko
year: 2015
bibkey: GH16_enriques
tags:
- paper
- extraction
abstract: |
  
---

# Moduli of polarized Enriques surfaces

V.
Gritsenko and K.
Hulek

# 1 Introduction

The moduli space $\mathcal { M } _ { \mathrm { E n } }$ of (unpolarized) Enriques surfaces is an open subset of a 10-dimensional orthogonal modular variety, which was shown by Kond¯o to be rational.
In this note we want to discuss moduli spaces of polarized and numerically polarized Enriques surfaces.
A polarized Enriques surface is, of course, a pair $( S , { \mathcal { L } } )$ , where $S$ is an Enriques surface and ${ \mathcal { L } } \in \operatorname { P i c } ( S )$ is an ample line bundle.
By numerically polarized Enriques surface we mean a pair $( S , h )$ where $h \in \operatorname { N u m } ( S )$ is the numerical class of an ample line bundle $\mathcal { L }$ .

One of the main results of this note is Theorem 3.2: for a given polarization $h$ , i.e. an ${ \mathrm { O } } ( U \oplus E _ { 8 } ( - 1 ) )$ -orbit of a primitive vector of positive degree in the abstract Enriques lattice $U \oplus E _ { 8 } ( - 1 )$ , we construct a suitable orthogonal modular variety $\mathcal { M } _ { \mathrm { E n } , h }$ of dimension 10 and identify in this an open subset $\mathcal { M } _ { \mathrm { E n } , h } ^ { a }$ whose points are in $1 : 1$ correspondence with isomorphism classes of numerically polarized Enriques surfaces with this polarization.
Moduli spaces of polarized Enriques surfaces, which exist as quasi-projective varieties by Viehweg’s theory, are then given by an ´etale $2 : 1$ cover of $\mathcal { M } _ { \mathrm { E n } , h } ^ { a }$ .
We ask the question when these covers are connected.

The main conclusion which we derive from our description of the moduli spaces is contained in Corollaries 3.5 and 4.4 and can be stated as follows:

Theorem 1.1 There are only finitely many isomorphism classes of moduli spaces of polarized and numerically polarized Enriques surfaces.

In section 5 we use automorphic forms to prove that some moduli spaces of numerically polarized Enriques surfaces have negative Kodaira dimension if the corresponding modular group contains sufficiently many reflections.
For example, this is true for all polarizations of degree $h ^ { 2 } \leq 3 2$ (see Corollary 5.6). In Proposition 5.7 we proved that for infinitely many polarizations $h$ the moduli space of numerically $h$ -polarised Enriques surfaces coincides with the moduli space of Enriques surfaces with a level-2 structure (see §2).
It was announced in [Gri2] that the last moduli space is of general type.

Moduli spaces of (polarized) Enriques surfaces have been studied by many authors, but not all of the results have appeared in the literature.
We have done our best to attribute published results wherever possible, but some further results in sections 2 to 4 are also likely to be known to experts, although they cannot be found in the literature.
Throughout this note we will be working over the complex numbers $\mathbb { C }$ , but we will also briefly comment on moduli spaces in positive characteristic.

Acknowledgement.
We have profited from many discussions on moduli spaces of Enriques surfaces, in particular with I.
Dolgachev, S.
Kond¯o, E.
Looijenga, D.
Markushevich and S.
Mukai.
This work was supported by Labex CEMPI in Lille.
We are grateful to G.
Nebe and D.
Lorch in Aachen for the MAGMA calculations which we used in the proof of Corollary 5.6. The first author gratefully acknowledges support by grant of the Government of the Russian Federation within the framework of the implementation of the 5-100 Programme Roadmap of the National Research University Higher School of Economics, AG Laboratory.
The second author gratefully acknowledges support by grant DFG Hu 337/6-2 and the Fund for Mathematics to the Institute of Advanced Study in Princeton, which provided excellent working conditions.
Finally we thank the referee for his/her careful reading of the article.

# 2 Enriques surfaces and the Torelli theorem

An Enriques surface (over the complex numbers) is a regular compact complex surface $S$ , i.e. $q ( S ) = h ^ { 1 } ( S , { \mathcal { O } } _ { S } ) = 0$ , whose canonical bundle $\omega _ { S }$ is not trivial, but has the property that it is 2-torsion, i.e. $\omega _ { S } ^ { \otimes 2 } = { \mathcal O } _ { S }$ .
Thus its holomorphic Euler characteristic is $\chi ( \mathcal { O } _ { S } ) = 1$ and by Noether’s formula its Euler number is $e ( S ) = 1 2$ .

Unlike K3 surfaces Enriques surfaces are always projective [BHPV, Section V.23] and since $H ^ { 0 , 2 } ( S ) = H ^ { 2 , 0 } ( S ) = H ^ { 0 } ( \omega _ { S } ) = 0$ all classes in $H ^ { 2 } ( S , \mathbb { Z } )$ are algebraic, in particular $H ^ { 2 } ( S , \mathbb { Z } ) \cong \operatorname { N S } ( S )$ .
Since the canonical bundle is 2-torsion the group $H ^ { 2 } ( S , \mathbb { Z } )$ is not-torsion free.
However, the canonical bundle is the only torsion element and there is a (non-canonical) splitting $H ^ { 2 } ( S , \mathbb { Z } ) = H ^ { 2 } ( S , \mathbb { Z } ) _ { f } \oplus \mathbb { Z } / 2 \mathbb { Z }$ where $H ^ { 2 } ( S , \mathbb { Z } ) _ { f } = H ^ { 2 } ( S , \mathbb { Z } ) /$ torsion is a free module of rank 10. The cup product, or intersection product, endows this with a lattice structure and one has, see [BHPV, Chapter VIII 15.1]

$$
H ^ { 2 } ( S , \mathbb { Z } ) _ { f } = \operatorname { N u m } ( S ) \cong U \oplus E _ { 8 } ( - 1 )
$$

where $U$ denotes the hyperbolic plane and $E _ { 8 } ( - 1 )$ is the negative definite $E _ { 8 }$ -lattice, i.e. it is negative definite, even, unimodular of rank 8.

The condition $\omega _ { S } ^ { 2 } = { \mathcal { O } } _ { S } $ implies the existence of an ´etale cover $p : X  S$ and by surface classification $X$ is a K3 surface.
We denote the corresponding involution on $X$ by $\sigma : X  X$ .
For a K3 surface $X$ it is well known that the intersection form on $H ^ { 2 } ( X , \mathbb { Z } )$ is a lattice of the form

$$
H ^ { 2 } ( X , \mathbb { Z } ) \cong 3 U \oplus 2 E _ { 8 } ( - 1 ) = : L _ { \mathrm { K } 3 }
$$

where $L _ { \mathrm { { K 3 } } }$ is the so-called K3 lattice.
Under the $2 : 1$ cover $p : X  S$ the

intersection form is multiplied by a factor 2 and thus

$$
p ^ { * } ( H ^ { 2 } ( S , \mathbb { Z } ) ) \cong U ( 2 ) \oplus E _ { 8 } ( - 2 ) = : M .
$$

By [Nik, Theorem 1.14.4] there is a unique embedding of the lattice $U ( 2 ) \oplus$ $E _ { 8 } ( - 2 )$ into the K3 lattice $L _ { \mathrm { { K 3 } } }$ and thus we may assume that $M$ is embedded into $L _ { \mathrm { { K 3 } } }$ by the embedding $( x , u ) \mapsto ( x , 0 , x , u , u )$ .
Whenever we refer to the sublattice $M$ of $L _ { \mathrm { K 3 } }$ we will use this embedding.

Consider the involution

$$
\rho : L _ { \mathrm { K 3 } } = 3 U \oplus 2 E _ { 8 } ( - 1 ) \to L _ { \mathrm { K 3 } } = 3 U \oplus 2 E _ { 8 } ( - 1 ) ,
$$

$$
\rho ( x , y , z , u , v ) = ( z , - y , x , v , u ) .
$$

Clearly $M = \operatorname { E i g } ( \rho ) ^ { + }$ is the $+ 1$ -eigenspace of this involution.
Let

$$
N = U \oplus U ( 2 ) \oplus E _ { 8 } ( - 2 ) .
$$

We think of $N$ as a primitive sublattice of $L _ { \mathrm { { K 3 } } }$ via the embedding $( y , z , v ) \mapsto$ $( z , y , - z , v , - v )$ .
Clearly

$$
N = M _ { L _ { \mathrm { K 3 } } } ^ { \perp } = \mathrm { E i g } ( \rho ) ^ { - } .
$$

Before we discuss markings and periods we will recall the basics about discriminant forms of lattices.
For every lattice $L$ its dual is defined by $L ^ { \vee } =$ ${ \mathrm { H o m } } ( L , \mathbb { Z } )$ , or equivalently $L ^ { \vee } = \{ x \in L \otimes \mathbb { Q } \mid ( x , y ) \in \mathbb { Z }$ , for $\mathrm { a l l } \ y \in L \}$ .
The discriminant group of $L$ is the finite abelian group

$$
D _ { L } = L ^ { \vee } / L .
$$

If $L$ is an even lattice, then the discriminant $D _ { L }$ carries a quadratic form with values in $\mathbb { Q } / 2 \mathbb { Z }$ induced from the form on $L$ .
As usual we shall denote the group of isometries of $L$ and $D _ { L }$ by $\mathrm { O } ( L )$ and $\mathrm { O } ( D _ { L } )$ respectively.
There is a natural homomorphism $\mathrm { O } ( L ) \to \mathrm { O } ( D _ { L } )$ and its kernel

$$
\widetilde { \mathrm { O } } ( L ) = \{ g \in \mathrm { O } ( L ) \ | \ g | _ { L ^ { \vee } / L } = \mathrm { i d } \}
$$

is called the stable orthogonal group of $L$ .
For the lattices $M$ and $N$ we have a natural isomorphism

$$
D _ { M } \cong D _ { N }
$$

which as an abelian group is the 2-elementary group $\mathbb { F } _ { 2 } ^ { 1 0 }$ .
Moreover $\mathrm { O } ( D _ { M } ) =$ $\mathrm { O } ( D _ { N } ) \cong \mathrm { O } ^ { + } ( \mathbb { F } _ { 2 } ^ { 1 0 } )$ is the orthogonal group of even type, whose order is $| \operatorname { O } ^ { + } ( \mathbb { F } _ { 2 } ) | = 2 ^ { 2 1 } \cdot 3 ^ { 5 } \cdot 5 ^ { 2 } \cdot 7 \cdot 1 7 \cdot 3 1$ , for details see [Kon2, §1], [Die, Chap. I, $\ S 1 6$ , Chap. II. §10].
We also know by [Nik, Theorem 3.6.3] that the homomorphisms $\pi _ { M } : \operatorname { O } ( M ) \to \operatorname { O } ( D _ { M } )$ and $\pi _ { N } : \operatorname { O } ( N ) \to \operatorname { O } ( D _ { N } )$ are surjective.

For future use we also describe a different description of the group $\mathrm { O } ( N )$ For this we notice that

$$
N ^ { \vee } ( 2 ) \cong U \oplus U ( 2 ) \oplus E _ { 8 } ( - 1 ) \cong 2 U \oplus D _ { 8 } ( - 1 )
$$

and hence

$$
{ \mathrm O } ( N ) \cong { \mathrm O } ( N ^ { \vee } ) \cong { \mathrm O } ( N ^ { \vee } ( 2 ) ) \cong { \mathrm O } ( 2 U \oplus D _ { 8 } ( - 1 ) ) .
$$

A marking of an Enriques surface $S$ is an isometry $\varphi : H ^ { 2 } ( S , \mathbb { Z } ) _ { f } \ \to$ $U \oplus E _ { 8 } ( - 1 )$ .
Every such marking, or more precisely the induced marking $\varphi : p ^ { * } ( ( H ^ { 2 } ( S , \mathbb { Z } ) ) \to U ( 2 ) \oplus E _ { 8 } ( - 2 )$ can be extended (not uniquely) to a marking $\widetilde { \varphi } : H ^ { 2 } ( X , \mathbb { Z } ) \to L _ { \mathrm { K 3 } }$ of the K3-cover $X$ .
This follows from [Nik, Corollary 1.5.2] together with the fact that $\mathrm { O } ( N ) \to \mathrm { O } ( D _ { N } )$ is surjective.
Moreover, we can assume that $\widetilde { \varphi } ( H ^ { 2 } ( X , \mathbb { Z } ) ) = M \subset L _ { \mathrm { K 3 } }$ , with $M$ the primitive sublattice of $L _ { \mathrm { K 3 } }$ as explained above.
The involution $\sigma ^ { * }$ acts trivially on $\widetilde { \varphi } ( H ^ { 2 } ( X , \mathbb { Z } ) )$ and by $- \mathrm { i d }$ on its orthogonal complement.
This implies that $\rho \circ \tilde { \varphi } = \tilde { \varphi } \circ \sigma ^ { * }$ .
We shall refer to a marking $\widetilde { \varphi }$ of $X$ with this property as an Enriques marking.
Note that if $\widetilde { \varphi }$ and $\widetilde { \varphi } ^ { \prime }$ are two Enriques markings extending the same marking $\varphi$ , then

$$
\begin{array} { r } { \widetilde { \varphi } \circ ( \widetilde { \varphi } ^ { \prime } ) ^ { - 1 } | _ { L _ { \mathrm { K 3 } } ^ { - } } \in \widetilde { \mathrm { O } } ( N ) . } \end{array}
$$

Markings allow us to define period points of Enriques surfaces: given a marked Enriques surface $( S , \varphi )$ we consider an Enriques marking $\widetilde { \varphi } \ :$ $H ^ { 2 } ( X , \mathbb { Z } ) \to L _ { \mathrm { K 3 } }$ as above.
The Enriques involution $\sigma$ on $X$ is non-symplectic, i.e. $\sigma ^ { * } ( \omega _ { X } ) = - \omega _ { X }$ and thus $\widetilde { \varphi } ( \omega _ { X } ) \in N _ { \mathbb { C } }$ .
The lattice $N$ is an even lattice of signture $( 2 , 1 0 )$ and we can associate to it the type IV domain

$$
\Omega _ { N } = \{ [ x ] \in \mathbb { P } ( N \otimes \mathbb { C } ) \mid ( x , x ) = 0 , ( x , { \bar { x } } ) > 0 \}
$$

which has two connected components $\Omega _ { N } = \mathcal { D } _ { N } \cup \mathcal { D } _ { N } ^ { \prime }$ .
The group $\mathrm { O } ( N )$ acts properly discontinuously on $\Omega _ { N }$ and we denote by $\mathrm { O } ^ { + } ( N )$ the index 2 subgroup of $\mathrm { O } ( N )$ with real spinor norm 1, i.e. the subgroup which fixes the connected components of $\Omega _ { N }$ .
We will call the group $\mathrm { O } ^ { + } ( N )$ the Enriques modular group.
Indeed $\mathrm { O } ^ { + } ( N )$ has index 2 in $\mathrm { O } ( N )$ , since the reflection with respect to a $+ 2$ -vector in a hyperbolic plane has real spinor norm $^ { - 1 }$ .
After possibly composing with an isometry $( \mathrm { i d } , - \mathrm { i d } , \mathrm { i d } , \mathrm { i d } , \mathrm { i d } )$ on $L _ { \mathrm { K 3 } } ~ = ~ 3 U ~ \oplus$ $2 E _ { 8 } ( - 1 )$ , which commutes with $\rho$ and interchanges the two components of $\Omega _ { N }$ , see [BHPV, Proposition VIII 20.2], we may assume that $[ \mathcal { \widetilde { S } } ( \omega _ { X } ) ] \in \mathcal { D } _ { N }$ is in a fixed connected component.
For this reason we refer to $\mathcal { D } _ { N }$ as the period domain of Enriques surfaces.
Clearly, the period point depends on the choice of the extension $\widetilde { \varphi }$ , but it also depends on the choice of the marking $\phi$ itself.
Since every isometry of the sublattice $M \subset L _ { \mathrm { { K 3 } } }$ can be extended to an isometry of the K3 lattice $L _ { \mathrm { K 3 } }$ one is thus led to consider the action of the group $\mathrm { O } ( N )$ on $\Omega _ { N }$ , respectively $\mathrm { O } ^ { + } ( N )$ on $\mathcal { D } _ { N }$ .

Unlike in the case of K3 surfaces not every point in the period domain $\mathcal { D } _ { N }$ comes from an Enriques surface.
To describe the image of the period domain we consider all vectors $- 2$ -vectors $l \in N$ , i.e. $l ^ { 2 } = - 2$ .
For each such root we obtain a hyperplane

$$
H _ { l } = \{ [ x ] \in \mathcal { D } _ { N } \mid ( x , l ) = 0 \} .
$$

We consider the union

$$
\mathscr { H } _ { - 2 } = \cup _ { l \in N , l ^ { 2 } = - 2 } H _ { l } .
$$

It was shown by Horikawa [Hor, Main Theorem], see also Nakamura [Nam, Theorem 7.2] and [BHPV, Chapter VIII, 21.4] that the image of the period domain is equal to the set $\mathcal { D } _ { N } \backslash \mathcal { H } _ { - 2 }$ .

Let us now consider the action of the group O $^ + ( N )$ on $\mathcal { D } _ { N }$ .
This group acts properly discontinuously and the quotient

$$
\mathcal { M } _ { \mathrm { E n } } = \mathrm { O } ^ { + } ( N ) \backslash \mathcal { D } _ { N }
$$

is a 10-dimensional quasi-projective variety.
It was shown by Namikawa, cf.
[Nam, Theorem 2.13], that all $- 2$ -vectors in $N$ are equivalent under the action of $\mathrm { O } ^ { + } ( N )$ .
Note that, using (2), this can also be deduced by standard methods by considering $2 U \oplus D _ { 8 } ( - 1 )$ , where we remark that $- 2$ vectors in $N$ correspond to reflective $- 4$ -vectors in $2 U \oplus D _ { 8 } ( - 1 )$ with the additional property that they pair to an even number with any other vector (we will call this later an even $- 4$ -vector) and vice versa.
Hence the union $\mathcal { H } _ { - 2 }$ maps to an irreducible hypersurface $\Delta _ { - 2 }$ in $\mathcal { M } _ { \mathrm { E n } }$ .
Let

$$
\mathcal { M } _ { \mathrm { E n } } ^ { 0 } = \mathcal { M } _ { \mathrm { E n } } \setminus \Delta _ { - 2 } .
$$

The global Torelli theorem for Enriques surfaces as proven by Horikawa $[ \mathrm { H o r } ]$ and refined by Namikawa in [Nam] implies the following

Theorem 2.1 There is a bijection

$$
\mathcal { M } _ { \mathrm { E n } } ^ { 0 } \stackrel { \cdot 1 : 1 } { \longleftrightarrow } \{ S \ | \ S i s \ a n \ E n r i q u e s \ s u r f a c e \ \} / \cong .
$$

For this reason the variety $\mathcal { M } _ { \mathrm { E n } } ^ { 0 }$ is often referred to as the moduli space of Enriques surfaces.

Remark 2.2 Strictly speaking it is a misnomer to speak of the moduli space of Enriques surfaces.
Although this spaces parametrizes the isomorphism classes of Enriques surfaces, it is, at least to us, not known that it represents a moduli functor.

At this point we would also like to recall the following important theorem due to Kond¯o [Kon1]:

Theorem 2.3 (Kond¯o) The space $\mathcal { M } _ { \mathrm { E n } } ^ { 0 }$ of Enriques surfaces is rational.

We also consider the modular variety

$$
\widetilde { \mathcal { M } } _ { \mathrm { E n } } = \widetilde { \mathrm { O } } ^ { + } ( N ) \backslash \mathcal { D } _ { N }
$$

which is a finite cover of $\mathcal { M } _ { \mathrm { E n } }$ with Galois group O $^ + ( \mathbb { F } _ { 2 } ^ { 1 0 } )$ .
Its open subset $\widetilde { \mathcal { M } } _ { \mathrm { E n } } ^ { 0 }$ which covers $\mathcal { M } _ { \mathrm { E n } } ^ { 0 }$ can be interpreted as the moduli space of Enriques surfaces with a level-2 structure (see [Kon2, §2]).
Gritsenko discussed the modular variety $\widetilde { \mathcal { M } } _ { \mathrm { E n } } = \widetilde { \mathrm { O } } ^ { + } ( N ) \backslash \mathcal { D } _ { N }$ at the Schiermonnikoog conference [Gri2] and outlined a proof that it is of general type, which of course implies that the moduli space Enriques surfaces with a level-2 structure is of general type.

# 3 Moduli spaces of numerically polarized Enriques surfaces

In this section we want to describe moduli spaces of numerically polarized Enriques surfaces in terms of modular varieties of orthogonal type.
We first recall that, since $H ^ { 2 , 0 } ( S ) = 0$ for an Enriques surface $S$ , every element in $H ^ { 2 } ( S , \mathbb { Z } )$ is represented by an algebraic class.
One consequence of this is that moduli spaces of polarized Enriques surfaces are of dimension 10, in contrast to the situation of K3 surfaces, where all K3 surfaces form a 20-dimensional family and polarized K3 surfaces have dimension 19.

We have already seen that $\operatorname { N S } ( S ) = H ^ { 2 } ( S , \mathbb { Z } ) \cong U \oplus E _ { 8 } ( - 1 ) \oplus \mathbb { Z } / 2 \mathbb { Z }$ .
Since $S$ is regular we can identify polarizations, i.e. ample line bundles $\mathcal { L }$ on $S$ with their first Chern classes $\ddot { h } : = c _ { 1 } ( \mathcal { L } ) \in H ^ { 2 } ( S , \mathbb { Z } )$ .
A polarized Enriques surface is a pair $( S , \tilde { h } )$ where $\tilde { h }$ represents an ample line bundle on $S$ .
We denote the numerical class defined by $\tilde { h }$ by $h = [ \tilde { h } ] \in \mathrm { N u m } ( S ) = H ^ { 2 } ( S , \mathbb { Z } ) _ { f } =$ $H ^ { 2 } ( S , \mathbb { Z } ) /$ torsion.
By a numerically polarized Enriques surface we mean a pair $( S , h )$ where $h \in \operatorname { N u m } ( S )$ comes from an ample line bundle.
Clearly every numerically polarized Enriques surface comes from two polarized Enriques surfaces $( S , \tilde { h } )$ and $( S , \tilde { h } + K _ { S } )$ .
Note that e.g. by Reider’s theorem $\tilde { h }$ is ample if and only if $\tilde { h } + K _ { S }$ is ample.

We shall first discuss moduli of numerically polarized Enriques surfaces.
For this we fix a primitive element $h \in { U } \oplus { E } _ { 8 } ( - 1 ) = { M } ( 1 / 2 )$ of positive degree $h ^ { 2 } = 2 d > 0$ .
Note that again the situation is different from K3 surfaces.
Any two primitive vectors $h \in L _ { \mathrm { K 3 } }$ of the same positive degree are equivalent under the orthogonal group $\mathrm { O } ( L _ { \mathrm { K 3 } } )$ .
This fails for $h ^ { 2 } \geq 4$ for the hyperbolic lattice $U \oplus E _ { 8 } ( - 1 )$ .

Now, given $h$ , we define the group

$$
\operatorname { O } ( M ( 1 / 2 ) , h ) = \operatorname { O } ( M , h ) = \{ g \in \operatorname { O } ( M ( 1 / 2 ) ) = \operatorname { O } ( M ) \mid g ( h ) = h \} .
$$

Next, we define the group

$$
\Gamma _ { h } = \pi _ { N } ^ { - 1 } ( \pi _ { M } ( \mathrm { O } ( M , h ) ) )
$$

where $\pi _ { M }$ and $\pi _ { N }$ are the natural projections onto the finite orthogonal groups $) ( D ( M ) )$ and $\mathrm { O } ( D ( N ) )$ respectively which, as we have seen, can be identified canonically.
Note that $\widetilde { \mathrm { O } } ( N ) \subset \Gamma _ { h }$ is a normal subgroup of $\mathrm { O } ( N )$ of finite index and hence $\Gamma _ { h }$ is an arithmetic subgroup of $\mathrm { O } ( N )$ .
We set

$$
\widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( N ) = \widetilde { \boldsymbol { \mathrm { O } } } ( N ) \cap \mathrm { O } ^ { + } ( N ) , \quad \Gamma _ { h } ^ { + } = \Gamma _ { h } \cap \mathrm { O } ^ { + } ( N ) .
$$

Again, we note that both subgroups have index 2, since the reflection with respect to a vector of length 2 in the summand $U$ of $N$ gives an element in $\widetilde { \mathrm { O } } ( N )$ of real spinor norm $^ { - 1 }$ .
The following space is crucial for us

$$
\begin{array} { r } { \mathcal { M } _ { \mathrm { E n } , h } : = \Gamma _ { h } ^ { + } \backslash \mathcal { D } _ { N } . } \end{array}
$$

The main point of this section is that we shall show that one can interpret an open set of this modular variety as a moduli space of numerically polarized Enriques surfaces.
Before discussing this we first observe that, if $h$ and $h ^ { \prime }$ belong to the same O $M ( 1 / 2 ) )$ -orbit, then the groups $\Gamma _ { h } ^ { + }$ and $\Gamma _ { h ^ { \prime } } ^ { + }$ are conjugate and hence $\mathcal { M } _ { \mathrm { E n } , h } \cong \mathcal { M } _ { \mathrm { E n } , h ^ { \prime } }$ .

Note that for every primitive vector $h \in M$ we have finite covering maps

$$
\widetilde { \mathcal { M } } _ { \mathrm { E n } }  \mathcal { M } _ { \mathrm { E n } , h }  \mathcal { M } _ { \mathrm { E n } } .
$$

Recall the hypersurface $\Delta _ { - 2 } \subset \mathcal { M } _ { \mathrm { E n } }$ and let $\Delta _ { - 2 , h }$ and $\bar { \Delta } _ { - 2 }$ be the preimages of $\Delta _ { - 2 }$ in $\mathcal { M } _ { \mathrm { E n } , h }$ and $\widetilde { \mathcal { M } } _ { \mathrm { E n } }$ respectively.
We set

$$
\mathcal { M } _ { \mathrm { E n } , h } ^ { 0 } = \mathcal { M } _ { \mathrm { E n } , h } \setminus \Delta _ { - 2 , h } , \quad \widetilde { \mathcal { M } } _ { \mathrm { E n } } ^ { 0 } = \widetilde { \mathcal { M } } _ { \mathrm { E n } } \setminus \widetilde { \Delta } _ { - 2 } .
$$

We will show that a suitable open subset of $\mathcal { M } _ { \mathrm { E n } , h } ^ { \mathrm { 0 } }$ gives a moduli space of numerically polarized Enriques surfaces.
Before we can do this, we need to recall some facts about smooth rational curves and ample divisors on Enriques surfaces.
By the adjunction formula a smooth rational curve $C$ has self-intersection $C ^ { 2 } = - 2$ .
For this reason we also refer to smooth rational curves as nodal curves.

Assume that an Enriques surface $S$ contains a smooth rational curve $C$ .
Then the pre-image of $C$ under the ´etale cover $p : X  S$ is a union of two disjoint smooth rational curves $C ^ { \prime }$ and $C ^ { \prime \prime }$ which are interchanged by the involution $\sigma$ and hence the class $[ C ^ { \prime } ] - [ C ^ { \prime \prime } ] \in H ^ { 2 } ( X , \mathbb { Z } )$ is in the $^ { - 1 }$ - eigenspace of $\sigma ^ { * }$ .
Hence, given an Enriques marking $\widetilde { \varphi } : H ^ { 2 } ( X , \mathbb { Z } ) \to L _ { \mathrm { K 3 } }$ this defines a primitive vector $l =  { \widetilde { \varphi } } ( [ C ^ { \prime } ] - [ C ^ { \prime \prime } ] ) \in N$ of length $l ^ { 2 } = - 4$ .
According to [Nam, Theorem 2.15] there are two $\mathrm { O } ( N )$ -orbits of vectors of length $- 4$ in $N$ , and the same argument also shows this to be true for $\mathrm { O } ^ { + } ( N )$ .
They are distinguished by the divisor $\mathrm { d i v } ( l )$ , which is defined as the positive generator of the ideal $\{ ( l , n ) \mid n \in N \} \subset \mathbb { Z }$ and which can be either $1$ or 2 here.
If $( u _ { 1 } , v _ { 1 } )$ and $( u _ { 2 } , v _ { 2 } )$ are a standard basis of the summands $U$ and $U ( 2 )$ of $N$ respectively, then the two orbits can be represented by $l _ { \mathrm { o d d } } = u _ { 1 } - 2 v _ { 1 }$ and $l _ { \mathrm { e v } } = u _ { 2 } - v _ { 2 }$ whose divisors are 1 and 2 respectively and which, for this reason, are called odd and even.
Note that their complements in $N$ are $l _ { \mathrm { o d d } } ^ { \perp } = E _ { 8 } ( - 2 ) \oplus U ( 2 ) \oplus \langle 4 \rangle$ and $l _ { \mathrm { e v } } ^ { \perp } = E _ { 8 } ( - 2 ) \oplus U \oplus \langle 4 \rangle$ .
It follows from [Nam, Proposition 2.16] that $l$ is of even type.
As before we consider $H _ { l } = \{ [ x ] \in \mathcal { D } _ { N } \mid ( x , l ) = 0 \}$ and the union

$$
\varkappa _ { - 4 , \mathrm { e v } } = \cup _ { l ^ { 2 } = - 4 , l \mathrm { e v e n } } H _ { l } .
$$

Since the group $\mathrm { O } ( N )$ acts transitively on all primitive vectors $l$ of length $l ^ { 2 } = - 4$ of given type ([Nam, Theorem 2.15]), the collection of hyperplanes ${ \mathcal { H } } _ { - 4 , { \mathrm { e v } } }$ maps to an irreducible hypersurface $\Delta _ { - 4 , \mathrm { e v } }$ in $\mathcal { M } _ { \mathrm { E n } }$ .
Note again that the irreducibility can also be deduced via the identification (2).

By Namikawa [Nam, Proposition 6.2] the points in $\mathcal { M } _ { \mathrm { E n } } ^ { 0 } \cap \Delta _ { - 4 , \mathrm { e v } }$ parameterize those Enriques surfaces which contain a nodal curve, the so called nodal Enriques surfaces.
Thus the open set

$$
\mathcal { M } _ { \mathrm { E n } } ^ { n n } = \mathcal { M } _ { \mathrm { E n } } \setminus \left( \Delta _ { - 2 } \cup \Delta _ { - 4 , \mathrm { e v } } \right)
$$

parametrizes the non-nodal Enriques surfaces.

The following lemma is standard, but we recall it for the reader’s convenience.

Lemma 3.1 Let $\mathcal { L }$ be a nef line bundle on an Enriques surface $S$ with $c _ { 1 } ( \mathcal { L } ) ^ { 2 } > 0$ .
Then $\mathcal { L }$ is ample if and only if there is no nodal curve $C$ with $c _ { 1 } ( \mathcal { L } ) . C = 0$ .

Proof.
Since $c _ { 1 } ^ { 2 } ( \mathcal { L } ) > 0$ it follows from Riemann-Roch that $\mathcal { L }$ or ${ \mathcal { L } } ^ { - 1 }$ must be effective.
Since $\mathcal { L }$ is nef it must be $\mathcal { L }$ itself.
To show ampleness it is enough by the Nakai-Moishezon criterion to show that $c _ { 1 } ( \mathcal { L } ) . C ~ > ~ 0$ for every irreducible curve $C$ .
Again by nefness of $\mathcal { L }$ the only obstruction to ampleness can thus be an irreducible curve $C$ with $c _ { 1 } ( \mathcal { L } ) . C = 0$ .
But then $C \in c _ { 1 } ( \mathcal { L } ) ^ { \perp }$ and the orthogonal complement of any vector of positive degree in the hyperbolic lattice $\operatorname { N u m } ( S ) \cong U \oplus E _ { 8 } ( - 1 )$ is negative definite, which implies $C ^ { 2 } < 0$ , which in turn means that $C$ is a nodal curve orthogonal to $c _ { 1 } ( \mathcal { L } )$ .
✷

Recall that we have fixed a primitive vector $h \in M \subset L _ { \mathrm { K 3 } }$ where $M$ is the $+ 1$ -eigenspace of the involution $\rho$ .
We fix the following set of roots in the K3 lattice

$$
R _ { h } = \{ \delta \in L _ { \mathrm { K 3 } } \mid \delta ^ { 2 } = - 2 , \delta . \rho ( \delta ) = 0 , \delta . h = 0 \} .
$$

Note that, since $h$ is invariant under $\rho$ , the condition $\delta . h = 0$ is equivalent to $( \delta + \rho ( \delta ) ) . h = 0$ and implies $( \delta - \rho ( \delta ) ) . h = 0$ .
Also note that $\delta \mathrm { - } \rho ( \delta ) \in N$ is an even vector of length $- 4$ [Nam, Proposition 2.16].
By [Nam, Proposition 4.5] the interpretation of $R _ { h }$ is the following: the classes $\delta$ and $\rho ( \delta )$ correspond to the classes $[ C ^ { \prime } ]$ and $[ C ^ { \prime \prime } ]$ where $C$ is a nodal curve on $S$ and $p ^ { - 1 } ( C ) =$ $C ^ { \prime } + C ^ { \prime \prime }$ with the additional property that $h . p ^ { - 1 } ( C ) = 0$ .
As before we set $H _ { \delta - \rho ( \delta ) } = \{ x \in \mathcal { D } _ { N } \mid ( x , \delta - \rho ( \delta ) ) = 0 \}$ .
Let

$$
\mathcal { H } _ { R _ { h } } = \cup _ { \delta \in R _ { h } } H _ { \delta - \rho ( \delta ) } .
$$

It follows from the construction of $\Gamma _ { h }$ and [Nik, Corollary 1.5.2] that every automorphism in $\Gamma _ { h }$ can be extended to an isometry of the K3 lattice $L _ { \mathrm { K 3 } }$ in such a way that it fixes $h$ and commutes with the involution $\rho$ .
This implies that $R _ { h }$ is mapped under $\Gamma _ { h }$ to itself and $\mathcal { H } _ { R _ { h } }$ maps to a hypersurface $\Delta _ { - 4 , \mathrm { e v } , h ^ { \perp } }$ in $\mathcal { M } _ { \mathrm { E n } , h }$ .
Note that if $\Delta _ { - 4 , \mathrm { e v } , h }$ denotes the pre-image of $\Delta _ { - 4 , \mathrm { { e v } } }$ under the map $\mathcal { M } _ { \mathrm { E n } , h } \to \mathcal { M } _ { \mathrm { E n } }$ , then by construction $\Delta _ { - 4 , \mathrm { e v } , h ^ { \perp } } \subset \Delta _ { - 4 , \mathrm { e v } , h }$ .
Geometrically this is the obvious fact that non-nodal Enriques cannot contain nodal curves orthogonal to $h$ .

Finally we set

$$
\mathcal { M } _ { \mathrm { E n } , h } ^ { a } = \mathcal { M } _ { \mathrm { E n } , h } \setminus \big ( \Delta _ { - 2 , h } \cup \Delta _ { - 4 , \mathrm { e v } , h ^ { \perp } } \big ) .
$$

By what we have just said $\mathcal { M } _ { { \mathrm { E n } } , h } ^ { n n } \subset \mathcal { M } _ { { \mathrm { E n } } , h } ^ { a }$ is an open set.
The main result of this section is the following:

Theorem 3.2 The open subset $\mathcal { M } _ { \mathrm { E n } , h } ^ { a }$ of $\mathcal { M } _ { \mathrm { E n } , h } ^ { 0 }$ has the following property: its points are in $1 : 1$ -correspondence with isomorphism classes of numerically polarized Enriques surfaces $( S , h )$ .

Proof.
We start with a pair $( S , H )$ and choose a marked polarization, i.e. a polarization $\varphi : H ^ { 2 } ( S , \mathbb { Z } ) _ { f } \to M ( 1 / 2 )$ with $\varphi ( H ) = h$ , which we extend to an Enriques marking on the K3 double cover $\widetilde { \varphi } : H ^ { 2 } ( X , \mathbb { Z } ) \to L _ { \mathrm { K 3 } }$ .
We then associate to $( S , H )$ the class of the period point $\widetilde { \varphi } ( \omega _ { X } )$ in $\mathcal { M } _ { \mathrm { E n } , h } ^ { \mathrm { 0 } }$ .
We must first show that this is well defined.
Two different Enriques markings extending $\varphi$ differ by an element in $\widetilde { \mathrm { O } } ( N )$ .
As this is a subgroup of $\Gamma _ { h }$ this defines the same point in $\mathcal { M } _ { \mathrm { E n } , h } ^ { \mathrm { 0 } }$ .
Next we have to consider the case where we have a different polarized marking $\varphi ^ { \prime } : H ^ { 2 } ( S , \mathbb { Z } ) _ { f } \to M ( 1 / 2 )$ with $\varphi ^ { \prime } ( H ) = h$ .
Let $\widetilde { \varphi }$ and ${ \widetilde { \varphi } } ^ { \prime }$ be Enriques markings extending $\varphi$ and $\varphi ^ { \prime }$ .
Then $\widetilde { \varphi } \circ \widetilde { \varphi } ^ { \prime - 1 } | _ { N } \in \Gamma _ { h }$ by the definition of the group $\Gamma _ { h }$ , and thus the map is well defined.

Clearly this map send $( S , H )$ and $( S , H + K _ { S } )$ to the same point in $\mathcal { M } _ { \mathrm { E n } , h } ^ { a }$ .
Next we want to show that these are the only points which are identified.
Let $( S , H )$ and $( S ^ { \prime } , H ^ { \prime } )$ be two polarized Enriques surfaces defining the same point in $\mathcal { M } _ { \mathrm { E n } , h } ^ { a }$ .
We want to show that $( S ^ { \prime } , H ^ { \prime } ) \cong ( S , H )$ or $( S ^ { \prime } , H ^ { \prime } ) \cong$ $( S , H + K _ { S } )$ .
For this we consider the K3 covers $( X , H )$ and $( X ^ { \prime } , H ^ { \prime } )$ together with polarized Enriques markings $\widetilde { \varphi }$ and ${ \widetilde { \varphi } } ^ { \prime }$ respectively.
Let $\psi \in \Gamma _ { h }$ be an automorphism with $\psi ( \widetilde { \varphi } ( \omega _ { X } ) ) = \widetilde { \varphi } ^ { \prime } ( \omega _ { X } ^ { \prime } )$ .
By definition of the group $\Gamma _ { h }$ we can extend $\psi$ to an isometry $\tilde { \psi } \in \mathrm { O } ( { \cal L } _ { \mathrm { K 3 } } )$ with ${ \\\widetilde { \psi } } ( h ) = h$ .
Since $\ddot { \psi }$ respects the subspaces $M$ and $N$ it follows that it commutes with $\rho$ .
Hence $\eta = ( \widetilde { \varphi } ^ { \prime } ) ^ { - 1 } \circ \widetilde { \psi } \circ \widetilde { \varphi } : H ^ { 2 } ( X , \mathbb { Z } ) \to H ^ { 2 } ( X ^ { \prime } , \mathbb { Z } )$ is a Hodge isometry with the additional properties that it commutes with the Enriques involutions, i.e. $\eta \circ \sigma ^ { \ast } = ( \sigma ^ { \prime } ) ^ { \ast } \circ \eta$ and that $\eta ( H ) = H ^ { \prime }$ .
Since $H$ and $H ^ { \prime }$ are ample we can apply the strong Torelli theorem to conclude that there is an isomorphism $f : X ^ { \prime } \cong X$ with $\eta = f ^ { * }$ and $f ^ { * } ( H ) = H ^ { \prime }$ .
Since moreover $f$ commutes with the Enriques involutions on $X$ and $X ^ { \prime }$ it descends to an isomorphism $g : S ^ { \prime } \to S$ with $g ^ { * } ( H ) = H ^ { \prime }$ or $g ^ { * } ( H ) = H ^ { \prime } + K _ { S ^ { \prime } }$ .

It remains to prove that every point in $\mathcal { M } _ { \mathrm { E n } , h } ^ { a }$ comes from a polarized Enriques surface.
By the surjectivity of the period map for K3-surfaces we can assume that there is a pair $( X , { \mathcal { L } } )$ where $X$ is a K3-surface and $\mathcal { L }$ a semiample line bundle, together with a marking $\widetilde { \varphi } : H ^ { 2 } ( X , \mathbb { Z } ) \to L _ { \mathrm { K 3 } }$ such that $\widetilde { \varphi } ( \omega _ { X } ) = \omega$ .
Via the marking $\widetilde { \varphi }$ the involution $\rho$ induces an involution $\iota$ on $H ^ { 2 } ( X , \mathbb { Z } )$ which is a Hodge isolmetry.
We want to argue that $\iota = \sigma ^ { * }$ for an Enriques involution $\sigma : X  X$ which has the additional property that it fixes $c _ { 1 } ( \mathcal { L } )$ .
For this we argue similar to the proof of [Nam, Theorem 3.13].
The idea is to find an element $w \in W _ { X }$ in the Weyl group of $X$ such that $w \circ \iota \circ w ^ { - 1 }$ is an effective Hodge isometry.
The main point is to find such a $w$ with the additional property that $w ( c _ { 1 } ( \mathcal { L } ) ) = c _ { 1 } ( \mathcal { L } )$ .
That this can be done follows from the fact that the subgroup $W _ { X , h }$ of $W _ { X }$ generated by reflection by roots orthogonal to $h$ acts transitively on the chambers of the positive cone, see [Bea, p. 151].
But then we can argue as in the proof of [Nam, Theorem 7.2]: the involution $w \circ \iota \circ w ^ { - 1 }$ is induced by an involution on $X$ which can be shown to have no fixed points, i.e. is an Enriques involution.
Hence the quotient of $( X , { \mathcal { L } } )$ is a pair $( S , { \mathcal { M } } )$ where $S$ is an Enriques surface and $\mathcal { M }$ is a nef line bundle.
(The involution $\iota$ can be lifted in two ways to an involution of the line bundle $\mathcal { L }$ , whose quotients give rise to $\mathcal { M }$ and $\mathcal { M } \otimes \omega _ { S }$ respectively).
The fact that $\mathcal { M }$ is ample now follows from Lemma 3.1 since $\omega \notin \mathcal { H } _ { R _ { h } }$ implies that there are no nodal curves on which $\mathcal { M }$ has degree 0. ✷

Remark 3.3 The points on the hypersurface $\Delta _ { - 4 , \mathrm { e v } , h ^ { \perp } } \setminus \Delta _ { - 2 }$ are in $1 : 1$ correspondence with numerically semi-polarized Enriques surfaces, where semi-polarization as usual means that the line bundle is nef but not ample.
The argument is as in $/ H P$ , Section 5], see also $\big [ B \mathrm { e a } \big ]$ .

Remark 3.4 Note that the variety $\mathcal { M } _ { \mathrm { E n } , h }$ and the hypersuface $\Delta _ { - 4 , \mathrm { e v } , h }$ contained in it only depend on the finite subgroup $\pi _ { M } ( \mathrm { O } ( M , h ) )$ in $\mathrm { O } ( D ( M ) )$ .
The hypersurface $\Delta _ { - 4 , \mathrm { e v } , h ^ { \perp } }$ on the other hand a priori depends on $h$ itself.
The difference between $\Delta _ { - 4 , \mathrm { e v } , h ^ { \perp } }$ and $\Delta _ { - 4 , \mathrm { e v } , h }$ is that $\Delta _ { - 4 , \mathrm { e v } , h ^ { \perp } }$ contains only some of the components of $\Delta _ { - 4 , \mathrm { e v } , h }$ .

One corollary from this is the following finiteness result:

Corollary 3.5 There are only finitely many different birational and isomorphism classes of moduli spaces of numerically polarized Enriques surfaces.

Proof.
By Theorem 3.2 every such moduli space is birational to a variety $\mathcal { M } _ { \mathrm { E n } , h }$ , which in turn only depends on a subgroup in $\mathrm { O } ( D ( M ) )$ .
Since this is a finite group the result follows.
However we can say more.
Since $\Delta _ { - 4 , \mathrm { e v } , h }$ only has finitely many components there are only finitely many possibilities for moduli spaces of polarized Enriques surfaces $\mathcal { M } _ { \mathrm { E n } , h } ^ { n n } \subset \mathcal { M } _ { \mathrm { E n } , h } ^ { a } \subset \mathcal { M } _ { \mathrm { E n } , h } ^ { \cup }$ and thus we also obtain the statement about the isomorphism classes.
$\boxed { \begin{array} { r l } \end{array} }$

# 4 Moduli spaces of polarized Enriques surfaces

In this section we want to discuss moduli spaces of polarized Enriques surfaces, i.e. pairs $( S , { \mathcal { L } } )$ where $S$ is an Enriques surfaces and $\mathcal { L }$ is an ample line bundle.
We fix the $\mathrm { O } ( M )$ -orbit of the numerical polarization defined projective moduli space by $c _ { 1 } ( \mathcal { L } )$ .
By Viehweg’s theory [Vie, Theorem 1.13] there exists a quasi- $\widehat { \mathcal { M } } _ { \mathrm { E n } , h } ^ { a }$ for these pairs.

Proposition 4.1 There exists an ´etale $2 : 1$ morphism $\widehat { \mathcal { M } } _ { \mathrm { E n } , h } ^ { a } \to \mathcal { M } _ { \mathrm { E n } , h } ^ { a }$

Proof.
We use the map which maps $( S , { \mathcal { L } } )$ and $( S , { \mathcal { L } } \otimes \omega _ { S } )$ to the numerically polarized Enriques surface $( S , h )$ where $h$ is the class of $c _ { 1 } ( \mathcal { L } )$ in $H ^ { 2 } ( S , \mathbb { Z } ) _ { f }$ .
Arguing as in [GHS2, Theorem 1.5], using Borel’s extension map $[ \mathrm { B o r } ]$ , we find that this map is not only a holomorphic map, but a morphism of quasiprojetive varieties, see also [Has, Proposition 2.2.2].
✷

It is not clear whether the covering McaEn,h → MaEn,h is connected or not.
The answer is known to be positive in some cases.
Classically studied examples include the polarizations in degree 4 and 6 where the polarization is base point free.
Note that in both degrees we have two orbits of primitive vectors.
One case is given by $h \ = \ e + d f \ \in \ U$ , $d = 2 , 3$ .
In this case $h ^ { \perp } \cong \langle - 2 d \rangle \oplus E _ { 8 } ( - 1 )$ .
The corresponding polarizations $H$ are in general ample but never base point free (and are in the literature partly excluded as polarizations on Enriques surfaces).
The reason they are not base point free is that $| 2 f |$ defines an elliptic fibration with two double fibres $F$ and $F ^ { \prime }$ (differing by the canoncal bundle) and $H . F = H . F ^ { \prime } = 1$ .
For the other cases $h ^ { \perp } \cong D _ { 9 } ( - 1 )$ and $h ^ { \perp } \cong A _ { 2 } ( - 1 ) \oplus E _ { 7 } ( - 1 )$ respectively.
The first of these cases was treated by Casnati who proved connectedness of the moduli space and rationality in [Cas].
In [Lie] these polarizations are called Cossec-Verra polarizations.
The second case is simply the classical fact that a general Enriques surface can be realized as a sextic surface in $\mathbb { P } ^ { 3 }$ passing doubly through the edges of the coordinate tetrahedron.
This space is also known to be rational, see Dolgachev [Dol1], [Dol2].
For further discussions about polarized Enriques surfaces, in particular of degrees $2 \leq h ^ { 2 } \leq 1 0$ , we refer the reader to [Dol3].

Question 4.2 When is the degree 2 cover $\widehat { \mathcal { M } } _ { \mathrm { E n } , h } ^ { a } \to \mathcal { M } _ { \mathrm { E n } , h } ^ { a }$ connected?

This question is related to the notion of supermarked Enriques surfaces, which has been developed by Dolgachev and Markushevich.
A supermarking is an isometry $\varphi : H ^ { 2 } ( S , \mathbb { Z } ) \to U \oplus E _ { 8 } ( - 1 ) \oplus \mathbb { Z } / 2 \mathbb { Z }$ .

A further question, which we do not know the answer to, is the following:

Question 4.3 Is $\widehat { \mathcal { M } } _ { \mathrm { E n } , h } ^ { a }$ the quotient of $\mathcal { D } _ { N }$ by a suitable arithmetic group?

Of course a positive answer to that would imply that $\widehat { \mathcal { M } } _ { \mathrm { E n } , h } ^ { a }$ is connected.
The above description is, however, enough to prove the

Corollary 4.4 There exist only finitely many different isomorphism classes of moduli spaces $\widehat { \mathcal { M } } _ { \mathrm { E n } , h } ^ { a }$ of polarized Enriques surfaces

Proof.
It is enough to show that each variety $\mathcal { M } _ { \mathrm { E n } , h } ^ { a }$ only admits finitely many ´etale $2 : 1$ coverings.
This follows since $\mathcal { M } _ { \mathrm { E n } , h } ^ { a }$ is a finite CW complex whose degree 2 coverings are classified by the elements in $H ^ { 1 } ( \mathcal { M } _ { \mathrm { E n } , h } ^ { a } , \mathbb { Z } / 2 \mathbb { Z } )$ .
This is a finite group.
✷

At this point we would like to comment briefly on the work of Liedtke in [Lie].
There he considers the moduli problem also in positive characteristic.
He treats in particular the case of Cossec-Verra polarizations in detail, see [Lie, Theorem 4.12].
Liedtke shows that this moduli problem carries the structure of a quasi-separated Artin stack of finite type over Spec $\mathbb { Z }$ , which over $\mathbb { Z } [ \frac { 1 } { 2 } ]$ is even a Deligne-Mumford stack.
In characteristic $p > 2$ the stack is irreducible and smooth of dimension 10. Liedtke also considers the functor of unpolarized Enriques surfaces.
This stack is, however, badly behaved, in particular its diagonal is not quasi-compact, see [Lie, Remark 5.3].
It is not clear whether this stack has an underlying coarse moduli space and if, how this is related to $\mathcal { M } _ { \mathrm { E n } }$ (over the complex numbers).

# 5 Modular varieties of negative Kodaira dimension

In this section we describe a class of modular varieties of dimension 10 of negative Kodaira dimension.

Theorem 5.1 Let $\Gamma ^ { + }$ be a group between the Enriques modular group and its stable subgroup $\widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( N ) < \boldsymbol { \Gamma } ^ { + } < \boldsymbol { \mathrm { O } } ^ { + } ( N )$ .
We assume that $\Gamma ^ { + }$ contains at least 26 reflections which are not conjugate with respect to $\widetilde { \mathrm { O } } ^ { + } ( N )$ .
Then the Kodaira dimension of the modular variety $\mathcal { M } _ { \Gamma ^ { + } } = \Gamma ^ { + } \backslash \mathcal { D } _ { N }$ is negative.

To prove this theorem we use the theory of reflective modular forms together with the general results about the compact models of modular varieties of orthogonal type obtained in [GHS1].

Definition 5.2 Let $\mathrm { s i g n } ( L ) = ( 2 , n )$ with $n \geq 3$ and let $\Gamma ^ { + }$ be a subgroup of $\mathrm { O } ^ { + } ( L )$ of finite index. A modular form of weight $k$ and character $\chi \colon \Gamma ^ { + } $ $\mathbb { C } ^ { * }$ with respect to $\Gamma ^ { + }$ is a holomorphic function $F \colon { \mathcal { D } } ( L ) ^ { \bullet } \to \mathbb { C }$ on the affine cone $\mathcal { D } _ { L } ^ { \bullet }$ over $\mathcal { D } _ { L }$ such that

$$
\begin{array} { l } { F ( t Z ) = t ^ { - k } F ( Z ) \quad \forall t \in \mathbb { C } ^ { * } , } \\ { F ( g Z ) = \chi ( g ) F ( Z ) \quad \forall g \in \Gamma ^ { + } . } \end{array}
$$

Note that by Koecher’s principle these forms are automatically holomorphic at the boundary.
We denote the (finite dimensional) space of modular forms of weight $k$ and character $\chi$ with respect to the group $\Gamma ^ { + }$ by $M _ { k } ( \Gamma ^ { + } , \chi )$ and the space of cusp forms, i.e. those forms vanishing at the boundary of the Baily-Borel compactification, by $S _ { k } ( \Gamma ^ { + } , \chi )$ .

The geometric type of a modular variety of orthogonal type depends very much on its ramification divisor.
For any non isotropic vector $r \in L$ we denote by $\sigma _ { r }$ the reflection with respect to $r$ :

$$
\sigma _ { r } ( l ) = l - \frac { 2 ( l , r ) } { ( r , r ) } r \in \mathrm { O } ( L \otimes \mathbb { Q } ) .
$$

This is an element of $\mathrm { O } ^ { + } ( L \otimes \mathbb { Q } )$ if and only if $( r , r ) < 0$ ( $\displaystyle \mathrm { s i g n } ( L ) = ( 2 , n ) ,$ A vector $r$ is called reflective if $\sigma _ { r } \in \mathrm { O } ^ { + } ( L )$ .
If $r ^ { 2 } = - 2$ , then $\sigma _ { r } \in \widetilde { \mathrm { O } } ^ { + } ( L )$ .

Definition 5.3 $A$ modular form $F \in M _ { k } ( \Gamma ^ { + } , \chi )$ is called reflective if

$$
{ \mathrm { S u p p } } ( { \mathrm { d i v } } F ) \subset \bigcup _ { \begin{array} { r l } { \pm r \in L } \\ { r { \mathrm { ~ i s ~ p r i m i t i v e } } } \\ { \sigma _ { r } \in \Gamma ^ { + } { \mathrm { ~ o r ~ } } - \sigma _ { r } \in \Gamma ^ { + } } \end{array} } H _ { r } ( L ) = : { \mathrm { R . d i v } } ( \pi _ { \Gamma ^ { + } } ) \subset { \mathcal { D } } _ { L } .
$$

We note that $\sigma _ { r } = \sigma _ { - r }$ and $H _ { r } = H _ { - r }$

The divisor $\mathrm { R . d i v } ( \pi _ { \Gamma ^ { + } } )$ in the above definition is the ramification divisor of the modular projection $\pi _ { \Gamma ^ { + } } : \mathcal { D } _ { L }  \Gamma ^ { + } \backslash \mathcal { D } _ { L }$ according to [GHS1, Corollary 2.13].
The ramification divisor of the full orthogonal group O $^ + ( N )$ has two irreducible components $\Delta _ { - 2 }$ and $\Delta _ { - 4 , \mathrm { e v } }$ defined by $- 2$ - and $- 4$ -reflective vectors in $N$ (see $\ S 3$ above).
We need two reflective modular forms, the so-called automorphic discriminants, of this moduli space.

Lemma 5.4 There exist two reflective modular forms

$$
\begin{array} { r l } { \Phi _ { 4 } \in M _ { 4 } ( \mathrm { O } ^ { + } ( N ) , \chi _ { 2 } ) , } & { \quad \mathrm { d i v } _ { \mathcal { D } _ { N } } \Phi _ { 4 } = \mathcal { H } _ { - 2 } , } \\ { \Phi _ { 1 2 4 } \in S _ { 1 2 4 } ( \mathrm { O } ^ { + } ( N ) , \mu _ { 2 } ) , } & { \quad \mathrm { d i v } _ { \mathcal { D } _ { N } } \Phi _ { 1 2 4 } = \mathcal { H } _ { - 4 , e v } } \end{array}
$$

where $\chi _ { 2 }$ and $\mu _ { 2 }$ are two binary characters of $\mathrm { O } ^ { + } ( N )$ .
Both modular forms vanish along the corresponding divisor with order one.

Proof.
This result is, in principle, known.
The form $\Phi _ { 4 }$ was found in [Bor] and is now called the Borcherds–Enriques modular form (of weight 4).
The additive lifting construction of $\Phi _ { 4 }$ in terms of vector valued modular forms was proposed by Kond¯o in [Kon2, Proposition 4.6].
For the second function see [Kon2, Theorem 4.4].
Note however, that the modular groups in the original constructions were smaller.
We propose here simple constructions of these forms which give us the maximal modular group, the formula for the characters together with the fact that the second form is cusp.
Recall from (2) that

$$
{ \mathrm { O } } ^ { + } ( N ) \cong { \mathrm { O } } ^ { + } ( 2 U \oplus D _ { 8 } ( - 1 ) )
$$

and that under the transformation $N ^ { \vee }  N ^ { \vee } ( 2 )$ the $- 2$ -vectors of $N$ and the even $- 4$ -reflective vectors (or the $^ { - 1 }$ -reflective vectors in the dual lattice) transform to the $- 4$ -reflective vectors and the $- 2$ -vectors respectively in $2 U \oplus D _ { 8 } ( - 1 )$ .

We recall that $D _ { 8 }$ is an even sublattice of the Euclidian lattice $\mathbb { Z } ^ { 8 }$

$$
D _ { 8 } = \{ n _ { 1 } e _ { 1 } + . . . + n _ { 8 } e _ { 8 } | n _ { i } \in \mathbb { Z } , \ n _ { 1 } + . . . + n _ { 8 } \in 2 \mathbb { Z } \} .
$$

In [Gri1] the modular form $\Phi _ { 4 }$ was constructed as the Jacobi lifting of the product of eight Jacobi theta-series

$$
\Phi _ { 4 } = \mathrm { L i f t } ( \vartheta ( \tau , z _ { 1 } ) \cdot \ldots \cdot \vartheta ( \tau , z _ { 8 } ) ) \in M _ { 4 } ( \mathrm { O } ^ { + } ( 2 U \oplus D _ { 8 } ( - 1 ) ) , \chi _ { 2 } )
$$

where $z _ { 1 } e _ { 1 } + \ldots + z _ { 8 } e _ { 8 } \in D _ { 8 } \otimes \mathbb { C }$ .
We note that

$$
{ \mathrm { O } } ^ { + } ( 2 U \oplus D _ { 8 } ( - 1 ) ) = \widetilde { \mathrm { O } } ^ { + } ( 2 U \oplus D _ { 8 } ( - 1 ) ) \cup \sigma _ { - 4 } \widetilde { \mathrm { O } } ^ { + } ( 2 U \oplus D _ { 8 } ( - 1 ) )
$$

where $\sigma _ { - 4 }$ is the reflection with respect to any $- 4$ reflective vector.
(For example, one can take the transformation $e _ { 1 } \mapsto - e _ { 1 }$ .) Using this we see that $\chi _ { 2 } | _ { \widetilde { O } ^ { + } ( 2 U \oplus D _ { 8 } ( - 1 ) ) } = 1$ and $\chi _ { 2 } ( \sigma _ { - 4 } ) = - 1$ .

To construct the second automorphic disriminant vanishing along the divisors defined by all $- 2$ -vectors of $2 U \oplus D _ { 8 } ( - 1 )$ we consider this lattice as a primitive sublattice of the even unimodular lattice $2 U \oplus N ( 3 D _ { 8 } ( - 1 ) )$ of signature $( 2 , 2 6 )$ where $N ( 3 D _ { 8 } )$ is the unimodular Niemeier lattice with root lattice $3 D _ { 8 }$ .
The arguments identical to the considerations in Theorem 3.2 of [GH2] show that the quasi-pullback (see [GHS3, §8]) of the Borcherds form $\Phi _ { 1 2 } \in M _ { 1 2 } ( \mathrm { O } ^ { + } ( 2 U \oplus N ( 3 D _ { 8 } ( - 1 ) ) ) , \mathrm { d e t } )$ to the lattice $2 U \oplus D _ { 8 } ( - 1 )$ is a $- 2$ -reflective cusp form of weight 124:

$$
\Phi _ { 1 2 4 } \in S _ { 1 2 4 } ( \mathrm { O } ^ { + } ( 2 U \oplus D _ { 8 } ( - 1 ) ) , \mu _ { 2 } )
$$

where $\mu _ { 2 } | _ { \widetilde { \mathsf { O } } ^ { + } ( 2 U \oplus D _ { 8 } ( - 1 ) ) } = \mathrm { d e t }$ , and $\mu _ { 2 } ( \sigma _ { - 4 } ) = 1$ .
We note that $\mu _ { 2 } ( \sigma _ { - 2 } ) =$ $\operatorname* { d e t } ( \sigma _ { - 2 } ) = - 1$ because $\sigma _ { - 2 } \in \widetilde { \cal O } ^ { + } ( 2 { \cal U } \oplus D _ { 8 } ( - 1 ) ) .$ ✷

Proof of Theorem 5.1. The modular variety $\mathcal { M } _ { \Gamma ^ { + } }$ of dimension 10 has a projective toroidal compactification $\overline { { \mathcal { M } } } _ { \Gamma ^ { + } }$ with canonical singularities and no ramification divisors at infinity (see [GHS1, Theorem 2]).
To prove the theorem we have to show that there are no pluricanonical differential forms on $\overline { { \mathcal { M } } } _ { \Gamma ^ { + } }$ .
Suppose that $F _ { 1 0 k } \in M _ { 1 0 k } ( \Gamma ^ { + } , \mathrm { d e t } ^ { k } )$ .
We may realise $\mathcal { D } _ { N }$ as a tube domain by choosing a 0-dimensional cusp.
In the corresponding affine coordinates of this tube domain we take a holomorphic volume element $d Z$ on $\mathcal { D } _ { N }$ .
Then the differential form $\Omega ( F _ { 1 0 k } ) = F _ { 1 0 k } ( d Z ) ^ { k }$ is $\Gamma ^ { + }$ -invariant.
Therefore it determines a section of the pluricanonical bundle over a smooth open part of the modular variety away from the branch divisor and the boundary.
Assume that $\Omega ( F _ { 1 0 k } )$ can be extended to a global section $H ( \overline { { \mathcal { M } } } _ { \Gamma ^ { + } } , k K _ { \overline { { \mathcal { M } } } _ { \Gamma ^ { + } } } )$ .
It follows that the modular form $F _ { 1 0 k }$ vanishes with order $k$ along the ramification divisor of $\Gamma ^ { + }$ in $\mathcal { D } _ { N }$ .

The group $\Gamma ^ { + }$ contains the element $- \mathrm { i d } _ { N }$ .
According to [GHS1, Corollary 2.13] the ramification divisor of $\pi _ { \Gamma } ^ { + }$ is equal to

$$
\bigcup _ { \pm r \in N , \ r ^ { 2 } = - 2 , \ - 4 } H _ { r } .
$$

The ramification divisor always contains components $H _ { r }$ with $- 2$ -vectors $r$ because the stable orthogonal group contains all such reflections: $\sigma _ { r } \in$ Oe +(N) < Γ+.
Moreover all −2-vectors of the lattice N belong to the same $\widetilde { \mathrm { O } } ^ { + } ( N )$ -orbit.
Therefore $F _ { 1 0 k }$ vanishes along $H _ { r }$ ( $r ^ { 2 } = - 2$ ) with order $k$ and it is divisible by the $k$ -power of the Borcherds-Enriques modular form $\Phi _ { 4 }$ .
According to the Koecher principle we have

$$
F _ { 6 k } = \frac { F _ { 1 0 k } } { \Phi _ { 4 } ^ { k } } \in M _ { 6 k } ( \Gamma ^ { + } , \chi )
$$

where $\chi$ is a binary character of $\Gamma ^ { + }$ .
The modular form $F _ { 6 k }$ vanishes with order $k$ along the ramification divisor of $\Gamma ^ { + }$ associated with all even -4- vectors.

Starting from $F _ { 6 k }$ we can construct a modular form with respect to $\mathrm { O } ^ { + } ( N )$ with $- 4$ -reflective divisor using the method of multiplicative symmetrisation (see [GN, §3.2] and [GH1, §1]).
We put

$$
F ^ { S y m } ( Z ) = \prod _ { g \in \Gamma ^ { + } \backslash \mathrm { O } ^ { + } ( N ) } F _ { 6 k } ( g Z ) \in M _ { 6 k [ \mathrm { O } ^ { + } ( N ) : \Gamma ^ { + } ] } ( \mathrm { O } ^ { + } ( N ) , \chi ^ { \prime } )
$$

where $\chi ^ { \prime }$ is a character of $\mathrm { O } ^ { + } ( N )$ .
We note that the function $F _ { 6 k } ^ { g } ( Z ) =$ $F _ { 6 k } ( g Z )$ is a modular form with respect to the group $g ^ { - 1 } \Gamma ^ { + } g$ containing the normal subgroup $\widetilde { \mathrm { O } } ^ { + } ( N )$ .
The modular form $F _ { 6 k }$ vanishes with order $k$ along the $^ { - 4 }$ -reflective divisors $H _ { r }$ where $r ^ { 2 } = - 4$ and $\sigma _ { r } \in \Gamma ^ { + }$ .
Therefore $F _ { 6 k } ^ { g }$ vanished along $H _ { g ^ { - 1 } r }$ .
The $- 4$ -part $\Delta _ { - 4 , e v }$ of the ramification divisor of $\mathrm { O } ^ { + } ( N ) \setminus \mathcal { D } _ { N }$ is irreducible because all $- 4$ -reflective vectors belong to the same $\mathrm { O } ^ { + } ( N )$ -orbit.
Two $- 4$ -reflective vectors $r _ { 1 }$ and $r _ { 2 }$ belong to the same $\widetilde { \mathrm { O } } ^ { + } ( N )$ -orbit if and only if they have the same images in the discriminate group or equivalently if $\textstyle { \frac { \scriptscriptstyle 1 \mathrm { \ : 1 } } { \mathrm { 2 } } } \equiv { \frac { \scriptscriptstyle 1 \mathrm { \ : 2 } } { \mathrm { 2 } } }$ mod $N$ (see [Ste, Corollary 3.3]).
We note that $\textstyle { \frac { r _ { 1 } } { 2 } }$ mod $N$ is a non isotropic element in the discriminant group $D ( N ) \cong$ $( \mathbb { F } _ { 2 } ^ { 1 0 } , q ^ { + } )$ of the lattice $N$ .
This quadratic space has 496 non isotropic vectors and all of them might be obtained as the image of a $^ { - 4 }$ -reflective vector in $U ( 2 ) \oplus E _ { 8 } ( - 2 )$ (see [CD, §9]).
Therefore there exist 496 different $\widetilde { \mathrm { O } } ^ { + } ( N )$ - orbits of $^ { - 4 }$ -reflective vectors in $N$ .

Let $R$ be the number of $\widetilde { \mathrm { O } } ^ { + } ( N )$ -orbits of $- 4$ -reflections in $\Gamma ^ { + }$ .
The multiplicity of $F ^ { S y m }$ along the irreducible divisor $\Delta _ { - 4 , e v }$ of the modular variety $\mathrm { O } ^ { + } ( N ) \setminus \mathcal { D } _ { N }$ is equal to

$$
m = \frac { k R [ \mathrm { O } ^ { + } ( N ) : \Gamma ^ { + } ] } { 4 9 6 } .
$$

Therefore $F ^ { S y m }$ is divisible by the $m$ -th power of the reflective form $\Phi _ { 1 2 4 }$ and

$$
6 k [ \Theta ^ { + } ( N ) : \Gamma ^ { + } ] \ge 1 2 4 m = \frac { k R [ \Theta ^ { + } ( N ) : \Gamma ^ { + } ] } { 4 } .
$$

Thus $2 4 \geq R$ .
It follows that $H ( \overline { { \mathcal { M } } } _ { \Gamma ^ { + } } , k K _ { \overline { { \mathcal { M } } } _ { \Gamma ^ { + } } } )$ is trivial for all $k$ if $R \geq 2 5$ This finishes the proof of Theorem 5.1.

Corollary 5.5 Let $h \in U \oplus E _ { 8 } ( - 1 )$ be a primitive element such that $h ^ { 2 } =$ $2 d > 0$ and the negative definite lattice $h _ { U \oplus E _ { 8 } ( - 1 ) } ^ { \perp }$ contain more than 48 vectors with length $- 2$ .
Then the moduli space $\mathcal { M } _ { \mathrm { E n } , h } = \Gamma _ { h } ^ { + } \setminus \mathcal { D } _ { N }$ of $h$ - polarized Enriques surfaces has negative Kodaira dimension.

Proof.
We first note that we have $\widetilde { \boldsymbol { \mathrm { O } } } ^ { + } ( N ) < \boldsymbol { \Gamma } _ { h } ^ { + } < \boldsymbol { \mathrm { O } } ^ { + } ( N )$ .
Secondly, any two $- 2$ -vectors $u \neq \pm v$ in the negative definite even lattice $h _ { U \oplus E _ { 8 } ( - 1 ) } ^ { \perp }$ are not congruent modulo $2 h _ { U \oplus E _ { 8 } ( - 1 ) } ^ { \perp }$ because $| ( u - v , u - v ) | < 8$ .
Therefore they define more than 24 reflections non conjugate with respect to $\widetilde { \mathrm { O } } ^ { + } ( N )$ .
We note that ${ \mathrm O } ( M , h ) \cong \widetilde { \mathrm O } ( h _ { U \oplus E _ { 8 } ( - 1 ) } ^ { \perp } )$ .
We finally remark that $\Gamma _ { h } ^ { + }$ contains the class of $- 2$ -reflections.
✷

Corollary 5.6 The modular variety $\mathcal { M } _ { \mathrm { E n } , h } : = \Gamma _ { h } ^ { + } \backslash \mathcal { D } _ { N }$ has negative $K o$ - daira dimension for all polarizations $h \in U \oplus E _ { 8 } ( - 1 )$ of degree $h ^ { 2 } \leq 3 2$ .

For $h ^ { 2 } = 3 4$ , 36, 38, 40, 42 the same is true for all polarizations of the corresponding degree except possibly one.

Proof.
We take a primitive vector in $h _ { 2 d } \in U \oplus E _ { 8 } ( - 1 )$ such that $h _ { 2 d } ^ { 2 } = 2 d$ .
The hyperbolic lattice is unimodular and the discriminant form of the orthogonal complement $h _ { 2 d } ^ { \perp }$ is equal to the discriminant form of rank one lattice $\langle - 2 d \rangle$ .
Therefore the lattice $h _ { 2 d } ^ { \perp }$ belongs to the genus ${ \mathfrak { G } } ( 2 d ) \ =$ ${ \mathfrak { G } } ( \langle - 2 d \rangle \oplus E _ { 8 } ( - 1 ) )$ which has finite number of classes.
They characterise all primitive vectors $h _ { 2 d }$ of degree $2 d$ .
For $d = 1$ there exist only one class $\langle - 2 \rangle \oplus E _ { 8 } ( - 1 )$ .
For $d = 2$ , 3, 4 the number of classes is equal to 2 and we can determine the second class.
For larger $d$ a MAGMA computation performed by Gabi Nebe and David Lorch in Aachen gives the following result where the notation $\mathbf { d } : [ n _ { 1 } , n _ { 2 } , \ldots , n _ { k } ]$ means the half-number of roots in the $k$ different classes of the genus ${ \mathfrak { G } } ( 2 d )$ .
We always have $n _ { 1 } = 1 2 0$ for the “trivial” class $\langle - 2 d \rangle \oplus E _ { 8 } ( - 1 )$ .

2 : [120, 72] 5 : [120, 64, 45] 8 : [120, 64, 56, 36] 11 : [120, 64, 63, 36, 33] 3 : [120, 66] 6 : [120, 56, 42] 9 : [120, 64, 39, 37] 12 : [120, 56, 39, 29] 4 : [120, 56] 7 : [120, 64, 43] 10 : [120, 56, 42, 30] 13 : [120, 64, 42, 38, 29] 14 : [120, 63, 56, 43, 36, 26] 15 : [120, 64, 39, 31, 25]  
$\mathbf { 1 6 } : [ 1 2 0 , 6 4 , 5 6 , 4 2 , 2 8 , 2 6 ]$  
$\mathbf { 1 7 } : [ 1 2 0 , 6 4 , 6 3 , 4 3 , 3 7 , 3 6 , 2 9 , 2 4 ]$ 18 : [120, 56, 42, 39, 26, 23]  
$\mathbf { 1 9 } : [ 1 2 0 , 6 4 , 6 3 , 4 2 , 3 1 , 2 8 , 2 4 ]$ 20 : [120, 63, 56, 36, 31, 28, 20]  
$\mathbf { 2 1 } : [ 1 2 0 , 6 4 , 3 9 , 3 7 , 2 9 , 2 5 , 2 3 ]$ .

We see that for $2 d \ : = \ : 3 4$ , 36, 38, 40, 42 there exits only one class $h _ { 2 d } ^ { \perp }$ containing less than 50 roots.
$\boxed { \begin{array} { r l } \end{array} }$

We mentioned above that the reflections defined by $- 2$ -vectors in the lattice $h _ { U \oplus E _ { 8 } ( - 1 ) } ^ { \perp }$ determine the transvections in the finite orthogonal group $\mathrm { O } ^ { + } ( \mathbb { F } _ { 2 } ^ { 1 0 } ) \cong \widetilde { \mathrm { O } } ^ { + } ( N ) \setminus \mathrm { O } ^ { + } ( N )$ .
The table from the proof of the last corollary shows that the group $\pi _ { M } ( \mathrm { O } ( M , h ) ) = \widetilde { \mathrm { O } } ^ { + } ( N ) \backslash \Gamma _ { h } ^ { + }$ is large for small degrees.
The next interesting question is how small this group might be.

Proposition 5.7 There exist $h _ { 2 d }$ such that $\Gamma _ { h _ { 2 d } } ^ { + } = \widetilde { \mathrm { O } } ^ { + } ( N )$

Proof.
This proposition follows form the following well-known fact in the theory of quadratic forms: most classes in a genus of a positive definite quadratic form with large determinant have trivial orthogonal group.
More exactly, let $c ( \mathfrak { G } )$ be the number of classes in the genus $\mathfrak { G }$ and $c _ { 0 } ( \mathfrak { G } )$ the number of classes $[ L ] \in { \mathfrak { G } }$ such that $\mathrm { O } ( L ) = \{ \pm 1 \}$ .
Then

$$
\frac { c _ { 0 } ( { \mathfrak { G } } ) } { c ( \mathfrak { G } ) }  1 , \qquad \mathrm { i f } \quad \operatorname* { d e t } ( \mathfrak { G } )  \infty .
$$

This was proved by J.
Biermann (1981) (see [Sch]).
Therefore for a large $d$ there exists a negative definite lattice $L \in { \mathfrak { G } } ( 2 d )$ such that $\mathrm { O } ( L ) = \{ \pm 1 \}$ .
Taking a unimodular extension of $\langle 2 d \rangle \oplus L$ we obtain a primitive vector $h _ { 2 d }$ in $U \oplus E _ { 8 } ( - 1 )$ such that $h _ { 2 d } ^ { \perp } \cong L$ .
Then we get $\mathrm { O } ( M , h ) \cong \widetilde { \mathrm { O } } ( h _ { 2 d } ^ { \perp } ) = \{ 1 \}$ and

$$
\Gamma _ { h _ { 2 d } } ^ { + } = \pi _ { N } ^ { - 1 } ( \pi _ { M } ( \mathrm { O } ( M , h _ { 2 d } ) ) ) \cap \mathrm { O } ^ { + } ( N ) = \widetilde { \mathrm { O } } ^ { + } ( N )
$$

which clearly implies the claim.

Remark 5.8 We note that Proposition 5.7 together with the fact mentioned at the end of $\ S 2$ that the modular variety $\widetilde { \mathcal { M } } _ { \mathrm { E n } } = \widetilde { \mathrm { O } } ^ { + } ( N ) \backslash \mathcal { D } _ { N }$ is of general type (see [Gri2]) show that there exist moduli spaces of numerically polarised (or polarized) Enriques surfaces of general type.

# References

[Bor] R.
E.
Borcherds, The moduli space of Enriques surfaces and the fake monster Lie superalgebra.
Topology 35 (1996), 699–710.  
[BHPV] W.
Barth, K.
Hulek, C.
Peters, A.
Van de Ven, Compact complex surfaces.
Second Enlarged Edition, Springer Verlag 2004.  
[Bea] A.
I.
Beauville, J.-P.
Bourguignon, M.
Demazure (eds), G´eom´etrie des surfaces K3: modules et p´eriodes.
S´eminaires Palaiseau, Ast´erisque 126 (1985).  
[Bor] A.
Borel, Some metric properties of arithmetic quotients of symmetric spaces and an extension theorem.
J.
Differential Geometry 6 (1972), 543–560.  
[Cas] G.
Casnati, The moduli space of Enriques surfaces with a polarization of degree 4 is rational.
Geom.
Dedicata 106 (2004), 185–194.  
[CD] F.
Cossec, I.
Dolgachev, Enriques Surfaces I.
Progress in Mathematics, vol.
76, 1989, Birkh¨auser.  
[Die] J.
Dieudonn´e, La g´eom´etrie des groupes classiques (2nd ed.).
Springer 1963.  
[Dol1] I.
Dolgachev, Rationality of fields of invariants.
In: S.
J.
Bloch (ed.), Algebraic Geometry (Bowdoin 1985), Proc.
Sympos.
Pure Math.
46, 1987.  
[Dol2] I.
Dolgachev, Enriques surfaces: what is left? Problems in the theory of surfaces and their classification (Cortona, 1988), Sympos.
Math., XXXII, 81–97, Academic Press, London, 1991.  
[Dol3] I.
Dolgachev, A brief introduction to Enriques surfaces.
arXiv:1412.7744, 31 pp.  
[Gri1] V.
Gritsenko, Reflective modular forms in algebraic geometry.
arXiv:1005.3753, 28 pp.  
[Gri2] V.
Gritsenko, Talk at the Schiermonnikoog conference, April 2014.  
[GH1] V.
Gritsenko, K.
Hulek, The modular form of the Barth–Nieto quintic.
Intern.
Math.
Res.
Notices 17 (1999), 915–938.  
[GH2] V.
Gritsenko, K.
Hulek, Uniruledness of orthogonal modular varieties.
J.
Algebraic Geometry 23 (2014), 711–725.  
[GHS1] V.
Gritsenko, K.
Hulek, G.K.
Sankaran, The Kodaira dimension of the moduli of K3 surfaces.
Invent.
Math.
169 (2007), 519–567.  
[GHS2] V.
Gritsenko, K.
Hulek, G.K.
Sankaran, Moduli spaces of irreducible symplectic manifolds.
Compos.
Math.
146 (2010), 404–434.  
[GHS3] V.
Gritsenko, K.
Hulek, G.K.
Sankaran, Moduli spaces of K3 surfaces and holomorphic symplectic varieties.
Handbook of Moduli(ed.
G.
Farkas and I.
Morrison), vol.
1, 459–526; Adv.
Lect.
in Math, Intern.
Press, MA, 2012.  
[GN] V.
Gritsenko, V.
Nikulin, Automorphic forms and Lorentzian KacMoody algebras, II.
International J.
Math.
9 (1998), 201–275.  
[Has] B.
Hassett, Special cubic fourfolds.
Compositio Math.
120 (2000), 1–23.  
[Hor] E.
Horikawa, On the periods of Enriques surfaces, I and II.
Math.
Ann.
234 (1978), 73–88; 235 (1978), 217–246.  
[HP] K.
Hulek, D.
Ploog, Fourier-Mukai partners and polarised K3 surfaces.
In: Arithmetic and geometry of $K 3$ surfaces and CalabiYau threefolds, 333–365, Fields Inst.
Commun., 67, Springer, New York, 2013.  
[Kon1] S.
Kond¯o, The rationality of the moduli space of Enriques surfaces.
Compositio Math.
91 (1994), 159–173.  
[Kon2] S.
Kond¯o, The moduli space of Enriques surfaces and Borcherds products.
J.
Algebraic Geom.
11 (2002), 601–627.  
[Lie] Ch.
Liedtke, Arithmetic moduli and lfting of Enriques surfaces.
J.
reine angew.
Math., DOI 10.1515/crelle-2013-0068.  
[Nam] Y.
Namikawa, Periods of Enriques surfaces.
Math.
Ann 270 (1985), 201–222.  
[Nik] V.V.
Nikulin, Integral symmetric bilinear forms and some of their applications.
Izv.
Akad.
Nauk SSSR Ser.
Mat.
43 (1979), 111–177.
English translation in Math.
USSR, Izvestiia 14 (1980), 103–167.  
[Sch] R.
Scharlau, Kartin Kneser’s work on quadratic forms and algebraic groups.
In Contemporary Mathematics 493 “Quadratic Forms-Algebra, Arithmetic, and Geometry.
2009, 339–358.  
[Ste] H.
Sterk, Compactifications of the period space of Enriques surfaces, I.
Math.
Z.
207 (1991), 1–36.  
[Vie] E.
Viehweg, Quasi-projective moduli for polarized manifolds.
Ergebnisse der Mathematik und ihrer Grenzgebiete (3), vol.
30, Springer, Berlin, 1995.

# Current Address:

Valery Gritsenko  
Laboratoire Paul Painlev´e et IUF Universit´e Lille 1  
F-59655 Villeneuve d’Ascq, Cedex France  
gritsenk@math.univ-lille1.fr

National Research University Higher School of Economics AG Laboratory, HSE 7 Vavilova str.
Moscow, Russia, 117312

Klaus Hulek  
Institut f¨ur Algebraische Geometrie  
Leibniz Universit¨at Hannover  
D-30060 Hannover  
Germany  
hulek@math.uni-hannover.de  
Current Address:  
Insitute for Advanced Study  
1, Einstein Drive  
Princeton, NJ 08540  
USA  
hulek@ias.edu