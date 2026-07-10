---
title: Compactifications defined by arrangements II - locally symmetric varieties
  of type IV
authors:
- Eduard Looijenga
year: 2002
bibkey: Loo03b
tags:
- paper
- extraction
abstract: |
  We define a new class of completions of locally symmetric varieties of type IV which interpolates between the Baily-Borel compactification and Mumford’s toric compactifications.
  An arithmetic arrangement in a locally symmetric variety of type IV determines such a completion canonically.
  This completion admits a natural contraction that leaves the complement of the arrangement untouched.
  The resulting completion of the arrangement complement is very much like a Baily-Borel compactification: it is the proj of an algebra of meromorphic automorphic forms.
  When that complement has a moduli space interpretation, then what we get is often a compactification obtained by means of geometric invariant theory.
  We illustrate this with several examples: moduli spaces of polarized $_ { K 3 }$ and Enriques surfaces and the semi-universal deformation of a triangle singularity.
  
  We also discuss the question when a type IV arrangement is definable by an automorphic form.
---

# COMPACTICATIONS DEFINED BY ARRANGEMENTS II: LOCALLY SYMMETRIC VARIETIES OF TYPE IV

EDUARD LOOIJENGA

Abstract.
We define a new class of completions of locally symmetric varieties of type IV which interpolates between the Baily-Borel compactification and Mumford’s toric compactifications.
An arithmetic arrangement in a locally symmetric variety of type IV determines such a completion canonically.
This completion admits a natural contraction that leaves the complement of the arrangement untouched.
The resulting completion of the arrangement complement is very much like a Baily-Borel compactification: it is the proj of an algebra of meromorphic automorphic forms.
When that complement has a moduli space interpretation, then what we get is often a compactification obtained by means of geometric invariant theory.
We illustrate this with several examples: moduli spaces of polarized $_ { K 3 }$ and Enriques surfaces and the semi-universal deformation of a triangle singularity.

We also discuss the question when a type IV arrangement is definable by an automorphic form.

# Introduction

There are two classes of irreducible bounded symmetric domains which admit complex totally geodesic hypersurfaces: the balls, which are associated to unitary groups of signature $( 1 , n )$ , and the type IV-domains, associated to real orthogonal groups of signature $( 2 , n )$ .
A domain of either class comes naturally with an embedding in a complex projective space for which its totally geodesic hypersurfaces are precisely the hyperplane sections.
This is why we call a locally finite collection of these an arrangement on such a domain.
We are interested in the case when this arrangement is arithmetic in the sense that it is a finite union of orbits of an arithmetic group of automorphisms of the domain in the set of hyperplane sections.
If we denote the domain by $\mathbb { D }$ and the arithmetic group by $\Gamma$ , then $X : = \Gamma \backslash \mathbb { D }$ is a quasi-projective orbifold and our assumption implies that the arrangement defines a hypersurface $D$ in $X$ ; a Cartier divisor on $X$ (when viewed as an orbifold) supported by $D$ amounts to assigning to every $\Gamma$ -orbit of the arrangement a nonzero integer.
We investigated this situation already for ball quotients in Part I [16]; here we concentrate on the more involved type IV quotients and so in the remainder of this introduction we shall assume that we are in that case.

The variety $X$ has as its natural projective completion the Baily-Borel compactification $X ^ { b b }$ .
If $\dim X \geq 3$ , then $X ^ { b b }$ has the short (though not very informative) characterization as the proj of the algebra of $\Gamma$ -automorphic forms on the domain.
Its boundary is of dimension $\leq 1$ and $X ^ { b b }$ is in general highly singular there—for this reason we cannot expect the natural extension $D ^ { b b }$ of $D$ to $X ^ { b b }$ to be the support of a Cartier divisor.
On the other hand, an automorphic form always defines a

Cartier divisor on $X ^ { b b }$ , so this is presumably the main reason why $D$ is usually not definable by an automorphic form.
Indeed, the necessary and sufficient condition that we find for a divisor supported by $D$ to be Cartier shows that this is a highly nontrivial property.
This is also the point of view taken by Bruinier and Freitag in [8], who show that in some special cases the Cartier property along one-dimensional boundary components suffices for $D$ being the zero set of an automorphic form that admits a product expansion.

But our main goal is different, namely to define a natural projective compactification of $X ^ { \circ } : = X - D$ in the spirit of the Satake, Baily-Borel theory.
This compactification, which we denote by ${ \widehat { X ^ { \circ } } }$ , is obtained via two intermediate compactifications which have an interest in their own right: First we define a normal blowup of $X ^ { b b }$ which leaves $X$ untouched and has the virtue that the closure of each irreducible component of $D$ in this blowup is Cartier.
This is basically the minimal normal blowup with this property.
We do this in a constructive, Satakelike, fashion.
The strict transforms of the irreducible components of $D$ form what we still might call an arrangement on this blowup.
We blow up this arrangement in a rather obvious manner and then we prove that this second blowup has a natural blowdown—this is our ${ \widehat { X ^ { \circ } } }$ .
The construction also yields an ample line bundle $\widehat { \mathcal { L } }$ on ${ \widehat { X ^ { \circ } } }$ which has the same restriction to $X ^ { \circ }$ as the automorphic line bundle on $X$ .
So every meromorphic $\Gamma$ -automorphic form whose polar locus is contained in the arrangement defines a meromorphic section of $\widehat { \mathcal { L } }$ that is regular on $X ^ { \circ }$ .
This has an interesting consequence, as we shall now explain.
If $D$ is the zero set of an automorphic form, then the boundary of this compactification is always a hypersurface.
But that situation is rather special and quite often this boundary has codimension $\geq 2$ .
This implies that a meromorphic $\Gamma$ -automorphic form as above defines a regular section of a nonnegative tensor power of $\widehat { \mathcal { L } }$ .
So the algebra of such forms is in fact finitely generated with positive degree generators and ${ \widehat { X ^ { \circ } } }$ can be characterized as the proj of this algebra.
This fact is very useful in the situation where the automorphic bundle over $X ^ { \circ }$ also appears as the quotient of an ample line bundle over a normal variety relative a proper action of a reductive algebraic group: we show that ${ \widehat { X ^ { \circ } } }$ is then likely to appear as a GIT compactification.
This happens for instance for the moduli spaces of sextic curves, of quartic surfaces (in both cases simple singularities allowed) and of curves on $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ of bidegree $( 4 , 4 )$ , which have in common that they all parametrize certain families of $K 3$ -surfaces.
In these cases, the first intermediate blowup of $X ^ { b b }$ has also algebro-geometric relevance.
An application in the same spirit concerns the semi-universal deformation of a triangle singularity.
These applications are all discussed in this paper, although we intend to discuss some of them in more detail elsewhere.

Let us now say something about the way this paper is organized.
The first two sections are essentially a review of the Baily-Borel compactification of a locally symmetric variety of type IV: Section 1 is devoted to the domains of that type, its boundary components and relevant groups, whereas Section 2 deals with the BailyBorel compactification proper.
We use the occasion not only to set up notation, but also to state the basic results in a manner that is best suited for our purposes.
This leads to a purely geometric approach, which almost avoids any reference to the general theory of algebraic groups (for instance, parabolic subgroups are never mentioned).
The next four sections make up what is perhaps the core of this paper: the main goal here is to define a modification of the Baily-Borel compactification

$X ^ { b b }$ in terms of combinatorial data.
We first do this over the one-dimensional boundary components.
Here the situation is relatively simple: the data in question then consist of giving a $\mathbb { Q }$ -vector subspace of a certain vector space.
Such a subspace comes up naturally when we are given an arithmetic arrangement.
We also give a necessary and sufficient condition for an arrangement to support a $\mathbb { Q }$ -Cartier divisor near a one-dimensional boundary stratum.
At this point it takes us only half a page to prove that the ‘rational double point locus’ in the moduli space of semipolarized $K 3$ -surfaces of genus $g > 2$ does not extend as a $\mathbb { Q }$ -Cartier divisor in its Baily-Borel compactification.
This implies that this locus is not definable by an automorphic form, thus completing an earlier result due to Nikulin (which says that this is so for infinitely many values of $g$ ).
The same program for the zero dimensional boundary strata (the ‘cusps’) is carried out in Sections 4 and 5: the former treats the modification of the local Baily-Borel compactification, the latter connects this with arrangements.
The necessary and sufficient condition that we find for an arrangement to support a Cartier divisor near a cusp is familiar in the theory of generalized root systems [13] and Lie-algebra’s of Kac-Moody type.
We show that in this context it implies the first half of the Arithmetic Mirror Symmetry Conjecture of Gritsenko and Nikulin [10].

We put things together in Section 6, where we find that our modifications of the Baily-Borel compactification form a big class that can be described in a uniform manner and has the Baily-Borel compactification and Mumford’s toroidal compactifications as extremal cases.
We remark here that this class of compactifications generalizes to all locally symmetric varieties, just like the Baily-Borel and toroidal compactifications, but since we presently see no applications of this generalization we have not endeavoured to set up things in this generality.

An arithmetic arrangement gives rise to a compactification of this type and it is this case that is discussed in Section 7. It is here where our main results are to be found.

A new technique must, if not guided, at least be motivated by examples and the one developed here is no exception.
This is why we have included three sections with worked examples to see the theory in action.
(Yet they are all of the same type, namely moduli spaces of $K 3$ -surfaces $S$ equipped with an embedding of a certain lattice in $\mathrm { P i c } ( S )$ , subject to some geometric condition which is generically satisfied.) In Section 7 we do this for the geometric invariant theory of $K 3$ -surfaces of small degree.
The GIT quotient of the space of plane sextics resp.
quartic surfaces (yielding compactifications of the moduli space of nonunigonal $K 3$ -surfaces of degree 2 and the nonhyperelliptic $K 3$ -surfaces of degree 4) has been worked out by Shah [20], [21] and we recover this quotient as a stratified space in the above setting.
(We do not identify here GIT strata with our strata, but we intend to do that in a future paper, in which we shall discuss these examples in more detail.) As far as we know, no one has done this for the space of complete intersections of a quadric and a cubic in $\mathbb { P } ^ { 4 }$ resp.
of three quadrics in $\mathbb { P } ^ { 5 }$ (which give compactifications of the moduli space of nonhyperelliptic $K 3$ -surfaces of degree 6 and 8 respectively).
Yet our technique predicts what the GIT boundary will be as a stratified space (their dimensions will be 3 and 2 respectively).
Section 8 treats the moduli spaces of ‘digonal’ $K 3$ -surfaces and of Enriques surfaces in this spirit.
The last case had already been treated by Sterk [24] in his Ph.D.
thesis, so here we limit ourself to describing the connection with his work.
Section 10 does not involve geometric invariant theory, but concerns an application to singularity theory: we obtain a precise description of the normalization of the union of the smoothing components of a triangle singularity.
This, incidentally, is the example that guided us in the first place a long time ago.

The dependence of this paper on its predecessor [16] is modest.
Strictly speaking this is only so in Section 7, where we need the notion of a linearized arrangement, which is explained at the beginning of that paper.

Acknowledgements This work has developed over a number of years—I dare not say how many, but the reader can guess—and during this period I have benefited from conversations and correspondence with many colleagues, among them Egbert Brieskorn, Igor Dolgachev, Gert Heckman, David Mumford, Henry Pinkham, Kyoji Saito, Peter Slodowy, Hans Sterk and Jonathan Wahl.
I thank them all.
I thank Igor Dolgachev, Gert Heckman and Hans Sterk once more for comments on a first version.

The finishing stage of this work was carried out while I was a visitor of the Mathematical Sciences Research Institute at Berkeley and in this capacity supported by an NSF grant.
I extend my thanks to both the MSRI and the NSF.

# List of Notation

Notation of a very local nature is omitted here.

$A$ In Sections 4 and 5 an affine space over $L$ efines over $\mathbb { R }$ .
$b b$ Denotes the Baily-Borel compactification.
$C$ In Section 4 a quadratic cone.
$c$ A tube domain open in $A$ (in Section 4).
$C _ { + }$ The convex hull of the set of rational points in the closure of $C$ .
$C _ { I }$ The cone naturally associated to the real isotropic subspace $I$ of $V$ : a half line in ${ \textstyle \bigwedge } ^ { I }$ resp.
a quadratic cone in $I \otimes I ^ { \perp } / I$ resp.
$\{ 0 \}$ if $I$ is of dimension 2, 1 or 0. $C ( \mathbb { D } )$ The conical locus defined by $\mathbb { D }$ in ${ \mathfrak { s o } } ( \phi )$ , see Definition 2.1. $\Gamma$ An arithmetic group, usually of $G ( \mathbb { Q } )$ , the exception being Sections 4 and 5, where $\Gamma$ is an arithmetic subgroup of hyperbolic type.
$\tilde { \Gamma }$ An arithmetic group of automorphisms of the tube domain $\boldsymbol { \mathscr { C } }$ .
$\Gamma _ { I } , \Gamma ^ { I } , \Gamma ( I )$ The $\Gamma$ -counterparts of $G _ { I } , G ^ { I } , G ( I )$ that are arithmetic in these groups; here $L$ is a $\mathbb { Q }$ -subspace of $V$ .
$\Gamma _ { \sigma } , \Gamma ^ { \sigma }$ Γσ is the group of $\gamma \in \Gamma$ which preserve $\sigma$ and $\Gamma ^ { \sigma }$ the group of $\gamma \in \Gamma _ { \sigma }$ which act trivially on $V / V _ { \sigma }$ (see 6.5). Here $\Gamma$ is an arithmetic group acting on $\mathbb { D }$ and $\sigma$ is a member of an admissible decomposition of the conical locus of $\mathbb { D }$ .
$\mathbb { D }$ A domain of type IV in $\mathbb { P } ( V )$ defined by the form $\phi$ .
$\eta$ Usually an ample line bundle.
$\phi$ A nondegenerate symmetric bilinear form on the vector space $V$ defined over $\mathbb { R }$ or $\mathbb { Q }$ and of signature $( 2 , n )$ .
$\phi _ { J }$ The form $\phi$ induces in $J ^ { \perp } / J$ , where $J$ is an istropic subspace of $V$ .
$G$ The stabilizer of $\mathbb { D }$ in $\mathrm { O } ( \phi ) ( { \mathbb R } )$ .
GIT abbreviation of Geometric Invariant Theory.
$G _ { I } , G ^ { I }$ The group of $g \in G$ that preserve resp.
act as the identity on an istropic subspace $I$ of $V$ .
$G ( I )$ The subgroup of $\operatorname { G L } ( I )$ defined by $G _ { I } / G ^ { I }$ .
$G ^ { I }$ The stabilizer of the $\mathbb { R }$ -isotropic subspace $I$ of $V$ in $G$ .

$H$ Usually a hyperplane.
When used as a subscript (like in $\mathbb { L } _ { H }$ and $\mathbb { B } _ { H }$ ) it means that we take the intersection with $H$ (or $\mathbb { P } ( H )$ ).
It is also used for orbit spaces of such intersections relative to an action of an arithmetic group (like in $X _ { H }$ ).
$\mathcal { H }$ An arithmetic arrangement in $V$ .
$I , J$ Usually an isotropic subspace in the inner product space $V$ .
$I ( \sigma )$ The isotropic center of $\sigma$ , see Definition 6.1. $L$ In Sections 4 and 5 a vector space defined over $\mathbb { Q }$ , equipped with a nondegenerate quadratic form of hyperbolic signature.
$L _ { \sigma }$ The $\Sigma$ -support space of a member $\sigma$ of the decomposition $\Sigma$ , see 4.5. $\mathbb { L }$ The automorphic line bundle over the type IV domain $\mathbb { D }$ .
$\mathbb { L } ^ { \times }$ The automorphic $\mathbb { C } ^ { \times }$ -bundle over the type IV domain $\mathbb { D }$ (contained in $V$ ).
$\mathcal { L }$ The automorphic (orbi)line bundle over the Baily-Borel compactification $X$ .
Also used for its pull-back on other extensions of $X$ that dominate $X ^ { b b }$ .
$\mathcal { L } ( \mathcal { H } )$ and $\mathscr { L } ( \mathscr { H } ) ^ { ( l ) }$ are coherent sheaves of rank one defined just before Theorem 7.4. $\ell$ A line bundle over the abelian torsor $Z ( J )$ whose total space contains $Z ^ { t o r }$ .
$\Lambda$ The $K 3$ -lattice.
$\Lambda _ { g }$ The orthogonal complement of a primitive vector of $\Lambda$ with selfproduct $2 g - 2$ .
$N _ { I }$ The unipotent radical of $G _ { I }$ .
This is also the kernel of the homomorphism $G _ { I } \to \operatorname { O } ( I ^ { \perp } / I ) \times \operatorname { G L } ( I )$ .
$N _ { \sigma }$ See the notational convention 6.5. O $\left( \phi \right)$ The orthogonal group defined by the symmetric bilinear form $\phi$ .
$P _ { k }$ The linear system of degree $k$ divisors on the projective line $P$ .
$P _ { k } ^ { \prime }$ The subset $P _ { k }$ defined by the reduced divisors.
$\mathbb { P } ( \mathbf { \pi } )$ The projective space of one-dimensional subspaces of the argument (a vector space).
$\operatorname { P O } ( \mathcal { H } )$ The partially ordered set of irreducible components of intersections of members of the arrangement $\mathcal { H }$ .
$\pi _ { L }$ Projection along a subspace $L$ of the vector space $V$ : $\pi _ { L } : V \to V / L$ .
It is also used for its projectivization $\mathbb { P } ( V ) - \mathbb { P } ( L ) \to \mathbb { P } ( V / L )$ .
ss Superscript standing for the set of stable points of.
st Superscript standing for the set of semistable points of.
Star Given a stratification of a topological space of which $S$ is a member, then $S t a r ( S )$ is the union of the members of that partition having $S$ in their closure.
$\Sigma$ A decomposition into locally rational cones of $C _ { + }$ (in Sections 4 and 5) or of the conical locus $C ( \mathbb { D } )$ of $\mathbb { D }$ .
When used as a superscript: the associated semitoric extension.
$\Sigma ( \mathcal { H } )$ The decomposition defined by the arrangement $\mathcal { H }$ .
$V$ A complex vector space with $\mathbb { Q }$ -structure endowed with a symmetric bilinear form $\phi$ also defined over $\mathbb { Q }$ and of signature $( 2 , n )$ .
$V _ { \sigma }$ The $\Sigma$ -support space of a member $\sigma$ of an admissible decomposition of the conical locus, see Definition 6.1. $X$ The orbifold $\Gamma \backslash \mathbb { D }$ .
$\widetilde { X ^ { \circ } }$ Denotes an arrangement blowup, see the discussion following (7.3).
${ \widehat { X ^ { \circ } } }$ Denotes the contraction of an arrangement blowup defined by Theorem 7.4. $X ( L )$ The variety $\Gamma _ { L } \backslash \pi _ { L } \mathbb { D }$ .
$Z$ In Section 3 synonymous with $\Gamma ^ { J } \backslash \mathbb { D }$ , where $J$ is a $\mathbb { Q }$ -isotropic plane, in Sections 4 and 5 essentially of the same form, where $I$ is a $\mathbb { Q }$ -isotropic line.
$Z ^ { t o r }$ A toric extension of $Z$ .

$Z ^ { L }$ In Section 3 an extension of $Z = \Gamma ^ { J } \backslash \mathbb { D }$ defined by a $\mathbb { Q }$ -subspace of $J ^ { \perp }$ which contains $J$ .
The boundary is $Z ( L )$ .
$Z ( L )$ In Sections 3, 4, 5 synonymous with $\Gamma ^ { J } \backslash \pi _ { L } \mathbb { D }$ , elsewhere, in case the argument is a group, it has the traditional meaning of the center of that group.
\\ Formation of a categorical quotient.
◦ Superscript (as in $X ^ { \circ }$ ) indicates that we take the complement of an arrangement in the space in question.

# Contents

Introduction 1  
List of Notation 4

1. Structure associated to boundary components 6  
   1A.
   Isotropic planes 7  
   1B.
   Isotropic lines 8
2. The Baily-Borel compactification 9
3. Modification over a one-dimensional boundary component 12  
   3A.
   Arrangements near the boundary component 13  
   3B.
   Arrangements that define $\mathbb { Q }$ -Cartier divisors 15  
   3C.
   Application to moduli spaces of $K 3$ surfaces 15
4. Semitoric extension of certain tube domains 16
5. Arrangements on tube domains 22  
   5A.
   Arrangements definable by a product expansion 24
6. Semi-toric compactification of type IV domains 28
7. Arrangements on a type IV domain 30
8. Applications to period mappings of polarized $K 3$ -surfaces 35  
   8A.
   Semiample linear systems on $K 3$ -surfaces 35  
   8B.
   $K 3$ -surfaces of small genus 38
9. Application to moduli of general Enriques surfaces 40
10. Application to smoothing components of triangle singularities 42  
    References 45

# 1. Structure associated to boundary components

Throughout this paper, $n$ is a nonnegative integer, $V$ a complex vector space of dimension $n + 2$ and $\phi : V \times V \to \mathbb { C }$ a nondegenerate symmetric bilinear form.
We assume that $( V , \phi )$ has been defined over $\mathbb { Q }$ and that $\phi$ has signature $( 2 , n )$ relative to this $\mathbb { Q }$ -structure.
The corresponding orthogonal group O( $\phi$ ) is therefore an algebraic group defined over $\mathbb { Q }$ .
Its Lie algebra ${ \mathfrak { s o } } ( \phi )$ is the space of endomorphisms of $V$ that are antisymmetric relative to $\phi$ and we shall often identify the underlying vector space via $\phi$ with $\wedge ^ { 2 } V$ in the obvious manner.

The subset of $\mathbb { P } ( V )$ defined by $\phi ( z , z ) = 0$ and $\phi ( z , \bar { z } ) > 0$ has two connected components that are interchanged by complex conjugation.
Denote by $G$ the subgroup of $\mathrm { O } ( \phi ) ( { \mathbb R } )$ (of index two) which respects the components.
Its Lie algebra is of course ${ \mathfrak { s o } } ( \phi ) ( \mathbb { R } )$ .
We choose one of the connected components and denote it by $\mathbb { D } ^ { 1 }$ .
It is a Hermitian symmetric domain for $G$ .

Let $\mathbb { L } ^ { \times }$ be the corresponding subset of $V - \{ 0 \}$ so that the projection $\mathbb { L } ^ { \times } \to \mathbb { D }$ is a $\mathbb { C } ^ { \times }$ -bundle.
For every integer $k \in \mathbb Z$ , the character $z \in \mathbb { C } ^ { \times } \mapsto z ^ { k } \in \mathbb { C } ^ { \times }$ defines an equivariant line bundle $\mathbb { L } ^ { k } \to \mathbb { D }$ .
We get $\mathbb { L } : = \mathbb { L } ^ { 1 }$ by filling in the zero section of $\mathbb { L } ^ { \times }$ and we shall refer to this bundle as the natural automorphic line bundle over $\mathbb { D }$ .
Filling in the section at infinity yields its dual $\mathbb { L } ^ { - 1 }$ .
So a function $f : \mathbb { L } ^ { \times } \to \mathbb { C }$ that is homogeneous of degree $- k$ may be considered as section of $\mathbb { L } ^ { k }$ .
The canonical bundle of $\mathbb { D }$ can be identified with $\mathbb { L } ^ { n }$ : if $p \in \mathbb D$ is represented by the line $L \subset V$ , then the tangent space $T _ { p } \mathbb { D }$ is naturally isomorphic to $\mathrm { H o m } ( L , L ^ { \perp } / L )$ .
Since $\wedge ^ { n } ( L ^ { \bot } / L ) \cong \wedge ^ { n + 2 } V$ canonically, we find that ${ \textstyle \bigwedge } ^ { n } T _ { p } ^ { * } \mathbb { D } \cong L ^ { n } \otimes { \textstyle \bigwedge } ^ { n + 2 } V ^ { * }$ .

We denote by $\Gamma$ an arithmetic subgroup of $G$ , that is, a subgroup of $G$ that is of finite index in the $G$ -stabilizer of some lattice in $V ( \mathbb { Q } )$ .
It contains a subgroup of finite index $\Gamma ^ { \prime }$ that is neat.
(This means that the multiplicative subgroup of $\mathbb { C } ^ { \times }$ generated by the eigenvalues of its elements has no torsion.) Since $\Gamma ^ { \prime }$ acts properly discretely on $\mathbb { D }$ and without fixed points, the orbit space $\Gamma ^ { \prime } \backslash \mathbb { D }$ exists as an analytic manifold.
We regard the $\Gamma$ -quotient of $\mathbb { D }$ as an orbifold and denote it by $X$ .
An important feature of this structure is that it remembers the isotropy groups of orbits.
In particular, it detects the center of $\Gamma$ as the kernel of the action of $\Gamma$ on $\mathbb { D }$ .
The $\Gamma$ -quotient of $\mathbb { L }$ defines a line bundle $\mathcal { L }$ on the orbifold $X$ and ${ \mathcal { L } } ^ { \otimes n }$ is just the $\Gamma$ -quotient of $\mathbb { L } ^ { n }$ .

A real isotropic subspace of $V$ is of dimension $\leq 2$ .
Let us first consider the case of dimension 2.

1A.
Isotropic planes.
Let $J \subset V$ be a real isotropic plane.
Then $J ^ { \perp } / J$ is negative definite of dimension $n$ .
Any element $g$ of the $G$ -stabilizer $G _ { J }$ of $J$ induces a linear transformation in $J$ and an orthogonal transformation in $J ^ { \perp } / J$ .
We thus get a group homomorphism $G _ { J } \to \operatorname { G L } ( J ) ( \mathbb { R } ) \times \operatorname { O } ( J ^ { \perp } / J ) ( \mathbb { R } )$ .
This homomorphism has an open subgroup as its image, whereas its kernel $N _ { J }$ consists of transformations that act trivially on the successive quotients of the flag $0 \subset J \subset J ^ { \perp } \subset V$ .
So $N _ { J }$ is the unipotent radical of $G _ { J }$ and the Levi quotient $G _ { J } / N _ { J }$ can be identified with an open subgroup of $\operatorname { G L } ( J ) ( { \mathbb { R } } ) \times \operatorname { O } ( J ^ { \perp } / J ) ( { \mathbb { R } } )$ .

For $g \in N _ { J }$ , the restriction of $g - 1$ to $J ^ { \perp }$ drops to a linear map $J ^ { \perp } / J \to J$ .
We thus get a map

$$
N _ { J }  \mathrm { H o m } ( J ^ { \perp } / J , J ) ( \mathbb { R } ) \cong ( J \otimes J ^ { \perp } / J ) ( \mathbb { R } ) ,
$$

where the last isomorphism used the nondegenerate form on $J ^ { \perp } / J$ .
This is a surjective homomorphism to a vector group.
Its kernel $Z ( N _ { J } )$ consists of the elements that are the identity on $J ^ { \perp }$ and every such element is of the form

$$
z \in V \mapsto z + \phi ( z , e ) f - \phi ( z , f ) e
$$

for certain $e , f \in J ( \mathbb { R } )$ .
As this transformation only depends on the image of $e \wedge f$ in $\wedge ^ { 2 } J$ , we thus obtain an identification

$$
\exp : \wedge ^ { 2 } J ( \mathbb { R } ) \cong Z ( N _ { J } ) .
$$

Here we identify $\operatorname { L i e } ( G ) = { \mathfrak { s o } } ( \phi ) ( \mathbb { R } )$ with $\wedge ^ { 2 } V ( \mathbb { R } )$ so that $\wedge ^ { 2 } J ( \mathbb { R } )$ may be regarded as an abelian subalgebra of this Lie algebra.
The commutator must define a linear map

$$
\wedge ^ { 2 } ( J \otimes J ^ { \perp } / J )  \wedge ^ { 2 } J .
$$

This map turns out to be the obvious one, namely contraction by means of $\phi$ .
It is in particular nondegenerate so that $Z ( N _ { J } )$ is the center of $N _ { J }$ as the notation suggested.
This shows that $N _ { J }$ is a real Heisenberg group.
We shall write $N _ { J }$ for the abelian quotient $N _ { J } / Z ( N _ { J } )$ .

The action of $N _ { J }$ on $\mathbb { D }$ realizes the latter as a Siegel domain of the third kind.
First notice that the choice of the component $\mathbb { D }$ determines an orientation of $J ( \mathbb { R } )$ .
This means that the punctured line $\wedge ^ { 2 } J ( \mathbb { R } ) - \{ 0 \}$ has a distinguished component.
We shall denote this component by $C _ { J }$ .
The corresponding half-plane in $\wedge ^ { 2 } J$ , $\mathcal { C } _ { J } : = \wedge ^ { 2 } J ( \mathbb { R } ) + \sqrt { - 1 } C _ { J } \subset \wedge ^ { 2 } J$ , is thought of as a subset of the complex Lie algebra ${ \mathfrak { s o } } ( \phi )$ .
Notice that $\exp ( \mathscr { C } _ { J } )$ is then a semigroup in the complexification of $Z ( N _ { J } )$ (acting by the same formula on $V$ ) which preserves $\mathbb { D }$ .

The set of oriented bases of $J ^ { * } ( \mathbb { R } )$ defines a half-sphere in the Riemann sphere $\mathbb { P } ( J ^ { * } )$ .
This half-sphere is just $\pi _ { J ^ { \perp } } \underline { { \mathbb { D } } }$ once we identify $V / J ^ { \perp }$ with $J ^ { * }$ .
In the diagram

$$
\mathbb { D } \to \pi _ { J } \mathbb { D } \to \pi _ { J ^ { \perp } } \mathbb { D } ,
$$

the first projection is a half-plane bundle (of complex dimension one), each fiber being a free orbit of the half-plane semigroup $\exp ( \mathcal { C } _ { J } )$ .
So $Z ( N _ { J } ) = \exp ( \land ^ { 2 } J ( \mathbb { R } ) )$ acts by translation parallel to the boundary.
The action of $N _ { J }$ on $\pi _ { J } \mathbb { D }$ is via $\bar { N } _ { J } \cong$ $J \otimes J ^ { \perp } / J$ and $\pi _ { J } \mathbb { D } \to \pi _ { J ^ { \perp } } \mathbb { D }$ is a principal $N _ { J }$ -bundle.
Each fiber of $\mathbb { D } \to \pi _ { J ^ { \perp } } \mathbb { D }$ is a free orbit of the semigroup $\mathrm { e x p } ( \sqrt { - 1 } C _ { J } ) \cdot N _ { J }$

In case $J$ is defined over $\mathbb { Q }$ , then so is $G _ { J }$ and $\Gamma _ { J } : = \Gamma \cap G _ { J }$ is arithmetic in $G _ { J }$ .
In particular, $\Gamma _ { N _ { J } } : = \Gamma \cap N _ { J }$ is cocompact in $N _ { J }$ and the image of $\Gamma _ { J }$ in the unitary group of $J ^ { \perp } / J$ is finite.
Let us now assume that $\Gamma$ is neat.
Then this image is reduced to the identity element so that $\Gamma _ { N J }$ is equal to the subgroup $\Gamma ^ { J } \subset \Gamma _ { J }$ of $\gamma \in \Gamma _ { J }$ that act trivially on $J$ .
The quotient $\Gamma ( J ) : = \Gamma _ { J } / \Gamma ^ { J }$ is arithmetic, when regarded as a subgroup of $G L ( J )$ .
In particular, $X ( J ^ { \bot } ) : = \Gamma ( J ) \backslash \pi _ { J ^ { \bot } } \mathbb { D }$ is a modular curve.
The property of $\Gamma ^ { J }$ being cocompact in $N _ { J }$ means that $\Gamma ^ { J } \cap Z ( N _ { J } )$ is infinite cyclic and that the image of $\Gamma ^ { J }$ in $N _ { J }$ is a lattice.
If we form the diagram of orbit spaces

$$
\Gamma ^ { J } \backslash \mathbb { D }  \Gamma ^ { J } \backslash \pi _ { J } \mathbb { D }  \pi _ { J ^ { \perp } } \mathbb { D } ,
$$

then the first morphism is a punctured disk bundle and the second a principal (real) torus bundle.
The torus in question has $( J \otimes J ^ { \perp } / J ) ( \mathbb { R } )$ as universal covering.
It inherits a complex structure from each fiber in such a manner that in the complex-analytic category, the bundle is isogenous to a repeated fiber product of the tautological bundle of elliptic curves over the half-plane $\pi _ { J ^ { \perp } } \underline { { \mathbb { D } } }$ .
A similar description applies to the diagram

$$
\Gamma _ { J } \backslash \mathbb { D }  \Gamma _ { J } \backslash \pi _ { J } \mathbb { D }  X ( J ^ { \perp } ) ,
$$

the only difference being that everything is now fibered over the modular curve $X ( J ^ { \perp } )$ .

1B.
Isotropic lines.
Suppose that $I$ is a real isotropic line in $V$ .
Then the form on $I ^ { \perp } / I$ induced by $\phi$ has signature $( 1 , n - 1 )$ .
For our purpose it is however better

to tensor this vector space with the line $I$ .
Then $\phi$ induces a symmetric bilinear map

$$
( I \otimes I ^ { \perp } / I ) ( \mathbb { R } ) \times ( I \otimes I ^ { \perp } / I ) ( \mathbb { R } ) \to I \otimes I
$$

which is still defined over $\mathbb { R }$ .
Since the line $( I \otimes I ) ( \mathbb { R } )$ has a natural orientation, we can still speak of its signature.
As this signature remains $( 1 , n - 1 )$ , the set of positive vectors is the union of a cone and its antipode.
But the choice of $\mathbb { D }$ now singles out one of these two cones.
We shall denote that distinguished cone by $C _ { I }$ .

The stabilizer $G _ { I }$ acts on $I ^ { \perp } / I \otimes I$ with image $G _ { I }$ the group of real orthogonal transformations of $I ^ { \perp } / I \otimes I$ that preserve $C _ { I }$ .
The kernel $N _ { I }$ of this action consists of the transformations in $G _ { I }$ that act trivially on $I ^ { \perp } / I \otimes I$ .
If $e \in I ( \mathbb { R } )$ is a real generator, and we use it to identify $I ^ { \perp } / I \otimes I$ with $I ^ { \perp } / I$ , then any such element is of the form

$$
\psi _ { e , f } : z \mapsto z + \phi ( z , e ) f - \phi ( z , f ) e - \textstyle { \frac { 1 } { 2 } } \phi ( f , f ) \phi ( z , e ) e
$$

for some $f \in I ^ { \bot } ( \mathbb { R } )$ .
Conversely, every element of this form lies in $N _ { I }$ .
Since $f$ is unique modulo $I$ , we obtain an identification of $N _ { I }$ with a vector group:

$$
\exp : ( I \otimes I ^ { \perp } / I ) ( \mathbb { R } ) \cong N _ { I } , \quad ( e \otimes f ) \mapsto \psi _ { e , f }
$$

so that $N _ { I }$ is commutative.
We regard here $I \otimes I ^ { \perp } / I \subset { \wedge } ^ { 2 } V$ as an abelian Lie subalgebra of ${ \mathfrak { s o } } ( \phi )$ defined over $\mathbb { R }$ .

The line $I$ determines a realization of $\mathbb { D }$ as a tube domain: the projection $\mathbb { D } $ $\pi _ { I } \mathbb { D }$ is a $G _ { I }$ -equivariant isomorphism and $\pi _ { I } \mathbb { D }$ can be characterized as a subset of $\mathbb { P } ( V / I )$ as follows.
The space $\mathbb { P } ( V / I ) { - } \mathbb { P } ( I ^ { \perp } / I )$ is an affine space for the vector group $\mathrm { H o m } ( V / I ^ { \perp } , I ^ { \perp } / I ) \cong I \otimes I ^ { \perp } / I$ and is as such defined over $\mathbb { R }$ .
If we divide out the affine space $\mathbb { P } ( V / I ) - \mathbb { P } ( I ^ { \perp } / I )$ by its real translations, then we obtain a vector space (the origin is the image of the real part of the affine space); this vector space is of course identifiable with $( I \otimes I ^ { \perp } / I ) ( \mathbb { R } )$ .
The tube domain $( I \otimes I ^ { \perp } / I ) ( \mathbb { R } ) + \sqrt { - 1 } C _ { I } \subset$ $I \otimes I ^ { \perp } / I$ exponentiates to the semigroup $N _ { I } \exp ( \sqrt { - 1 } C _ { I } )$ in the complexification of $N _ { I }$ .
This semigroup preserves $\mathbb { D }$ .
Observe that $\mathbb { P } ( V / I ^ { \perp } )$ and hence $\pi _ { I ^ { \perp } } \mathbb { D }$ is a singleton.

If $I$ is defined over $\mathbb { Q }$ , then so is $G _ { I }$ and $\Gamma _ { I }$ is arithmetic in $G _ { I }$ .
This implies that $\Gamma _ { N _ { I } }$ defines a lattice in $I ^ { \perp } / I \otimes I$ (preserved by $\bar { \Gamma } _ { I }$ , of course) and that $\bar { \Gamma } _ { I }$ arithmetic in $G _ { I }$ .

A real isotropic plane $J$ in $V$ containing $I$ corresponds to a real isotropic line $J$ in $I ^ { \perp } / I$ and vice versa.
In that case, $\wedge ^ { 2 } J$ can be regarded as a line in $I \otimes I ^ { \perp } / I$ and via this inclusion, $C _ { J }$ is contained in the boundary of $C _ { I }$ .

# 2. The Baily-Borel compactification

The isotropic subspaces defined over $\mathbb { Q }$ play a central role in the construction of the Baily-Borel compactification of $X$ .
We observed that every $\mathbb { Q }$ -isotropic line $I \subset V$ defines a cone $C _ { I } \subset ( I \otimes I ^ { \perp } / I ) ( \mathbb { R } ) \subset \Lambda ^ { 2 } V ( \mathbb { R } ) \cong { \mathfrak { s o } } ( \phi ) ( \mathbb { R } )$ .
Similarly, every $\mathbb { Q }$ -isotropic plane $I \subset V$ defines an open half-line $C _ { I }$ in $\wedge ^ { \cdot 2 } I ( \mathbb { R } ) \subset { \mathfrak { s o } } ( \phi ) ( \mathbb { R } )$ .
It is clear that these cones are mutually disjoint and that $C _ { J }$ meets the closure of $C _ { I }$ if and only if $I \subseteq J$ .
We also consider $\{ 0 \}$ as an isotropic subspace of $V$ and put $C _ { \{ 0 \} } : = \{ 0 \}$ and $N _ { \{ 0 \} } = \{ 1 \}$ .
Let $\mathcal { L }$ denote the collection of all $\mathbb { Q }$ -isotropic subspaces of $V$ , including $\{ 0 \}$ .
A partial order on $\mathcal { L }$ is defined by the incidence relations, not of the isotropic subspaces, but of the corresponding cones.
For instance, $\{ 0 \} < J < I$ if $J$ is an isotropic plane containing the isotropic line $I$ .
For $I \in \mathbb { Z }$ , we put

$$
V _ { I } : = { \left\{ \begin{array} { l l } { I ^ { \perp } } & { { \mathrm { ~ i f ~ } } I \neq \{ 0 \} , } \\ { \{ 0 \} } & { { \mathrm { ~ i f ~ } } I = \{ 0 \} . } \end{array} \right. }
$$

So if $I , J \in { \mathcal { T } }$ , then $J \le I$ if and only if $V _ { J } \subseteq V _ { I }$ .

Definition 2.1. We call the subset $\cup _ { I \in { \mathcal { I } } } C _ { I }$ of ${ \mathfrak { s o } } ( \phi ) ( \mathbb { R } )$ (a disjoint union) the conical locus of $\mathbb { D }$ .
We shall denote it by $C ( \mathbb { D } )$ .

This locus depends on the domain $\mathbb { D }$ with its $\mathbb { Q }$ -structure’.
If we replace $\mathbb { D }$ by it complex conjugate (the other component), then the conical locus is replaced by its antipode.

We write $\Gamma ^ { I }$ for the group of $\gamma \in \Gamma$ that preserve $I$ and act as the identity on $V / V _ { I }$ .
It is clear that $\Gamma ^ { \{ 0 \} } = \{ 1 \}$ .
When $I \neq \{ 0 \}$ , then $V / V _ { I }$ can be identified with the dual of $I$ and so $\Gamma ^ { I }$ is then simply the group $\gamma \in \Gamma$ that leave $I$ pointwise fixed and so this agrees with our earlier notation.
The group $\Gamma ^ { I }$ is an extension of an automorphism group of $C _ { I }$ by $N _ { I }$ and so is in fact equal to $\Gamma _ { N _ { I } }$ when $\dim I \neq 1$ .
For the same reason we have $\Gamma ^ { I } N _ { I } = N _ { I }$ unless $\dim I = 1$ .
Notice that $\textit { J } \leq \textit { I }$ implies that $\Gamma ^ { J } \subseteq \Gamma ^ { I }$ .
Now consider the disjoint unions

$$
\mathbb { D } ^ { b b } : = \prod _ { I \in \mathcal { I } } \pi _ { V _ { I } } \mathbb { D } , \quad ( \mathbb { L } ^ { \times } ) ^ { b b } : = \prod _ { I \in \mathcal { I } } \pi _ { V _ { I } } \mathbb { L } ^ { \times }
$$

(so the term indexed by $\{ 0 \} \in \mathcal { T }$ yields $\mathbb { D }$ resp.
$\mathbb { L } ^ { \times }$ ).
Both unions come with an obvious action of $G ( \mathbb { Q } )$ .
The group $\Gamma$ has finitely many orbits in $\mathcal { L }$ and so the $\Gamma$ - orbit set of $\mathbb { D } ^ { b b }$ is the union of $X$ and finitely many modular curves and singletons.
The Baily-Borel theory puts a $G ( \mathbb { Q } )$ -invariant topology on these spaces such that $\Gamma \backslash ( \mathbb { L } ^ { \times } ) ^ { b b }  \Gamma \backslash \mathbb { D } ^ { b b }$ becomes a $\mathbb { C } ^ { \times }$ -bundle over a compact Hausdorff space.
This topology, which is at first sight perhaps somewhat unnatural, is almost forced upon us if we want $\Gamma$ -automorphic forms to have a continuous extension for it.
Here is the definition.

Definition 2.2. For a subset $K \subset \mathbb { D }$ resp.
$K \subset \mathbb { L } ^ { \times }$ we define its $( \Gamma , I )$ -saturation in $\mathbb { D } ^ { b b }$ resp.
$( \mathbb { L } ^ { \times } ) ^ { b b }$ by

$$
K ^ { b b } ( \Gamma , I ) : = \prod _ { J \in \mathcal { T } , J \leq I } \pi _ { V J } ( \Gamma ^ { I } N _ { I } \exp ( \sqrt { - 1 } C _ { I } ) K ) .
$$

Here we note that $\Gamma ^ { I }$ normalizes $C _ { I }$ so that $\Gamma ^ { I } N _ { I } \exp ( \sqrt { - 1 } C _ { I } )$ is a semigroup in $\mathrm { O } ( \phi )$ .
If $K$ runs over the open subsets of $\mathbb { D }$ resp.
$\mathbb { L } ^ { \times }$ and $I$ over $\mathcal { L }$ , then these form the basis of a topology, called the Satake topology.

These topologies depend of course on the $\mathbb { Q }$ -structure on $V$ , but not on the particular arithmetic group $\Gamma$ in $G ( \mathbb { Q } )$ since it can be shown that $G ( \mathbb { Q } )$ acts on both spaces as a group of homeomorphisms.
We regard $\mathbb { D } ^ { b b }$ as a ringed space by equipping it with the sheaf $\mathcal { O } _ { \mathbb { D } ^ { b b } }$ of complex valued continuous functions on open subsets that are analytic on each piece $\pi _ { V _ { I } } \mathbb { D }$ .
We do similarly for $( \mathbb { L } ^ { \times } ) ^ { b b }$ .
For such ringed spaces we borrow the terminology that is standard use in the complexanalytic category.
For instance, $\mathcal { O } _ { \mathbb { D } ^ { b b } }$ is called the structure sheaf of $\mathbb { D } ^ { b b }$ , a local section of this sheaf is called an analytic function and the projection $( \mathbb { L } ^ { \times } ) ^ { b b }  \mathbb { D } ^ { b b }$ is a morphism, more specifically, it is an analytic $\mathbb { C } ^ { \times }$ -bundle.

For every $k \in \mathbb { Z }$ we denote by $( \mathbb { L } ^ { k } ) ^ { b b }$ the line bundle over $\mathbb { D } ^ { b b }$ defined by the representation of $\mathbb { C } ^ { \times }$ whose character is the $k$ th power.
It is still true that $\mathbb { L } ^ { b b } =$ $( \mathbb { L } ^ { 1 } ) ^ { b b }$ resp.
$( \mathbb { L } ^ { - 1 } ) ^ { b b }$ is obtained by filling in the zero section resp.
the section at infinity.

The first steps of the theory yield that $\Gamma \backslash ( \mathbb { L } ^ { \times } ) ^ { b b }$ is a locally compact Hausdorff space with proper $\mathbb { C } ^ { \times }$ -action whose orbit space is compact and can be identified with $\Gamma \backslash \mathbb { D } ^ { b b }$ .
The next step is to show that we land in the category of normal analytic spaces if we take our quotients in the category of ringed spaces (so $\Gamma \backslash ( \mathbb { L } ^ { \times } ) ^ { b b }$ is then equipped with the sheaf of continuous complex valued functions whose pull-back to $( \mathbb { L } ^ { \times } ) ^ { b b }$ is piecewise analytic).
For us the following geometric definition of an automorphic form is convenient.

Definition 2.3. A $\Gamma$ -automorphic form of degree $k \in \mathbb { Z }$ on $\mathbb { D }$ is a $\Gamma$ -invariant morphism $( \mathbb { L } ^ { \times } ) ^ { b b } \to \mathbb { C }$ that is homogeneous of degree $- k$ , in other words, a continuous complex valued function on $( \mathbb { L } ^ { \times } ) ^ { b b }$ that is analytic and homogeneous of degree $- k$ on each piece $\pi _ { V _ { I } } \mathbb { L } ^ { \times }$ .

Such a form can also be thought of as a section of $( \mathbb { L } ^ { k } ) ^ { b b }$ .
There is the related notion of a meromorphic automorphic form, whose definition the reader will be able to guess.
A standard procedure produces plenty of such forms (see Proposition 7.3 for a generalization).
Baily and Borel show that the $\Gamma$ -automorphic forms thus produced separate the points of $( \mathbb { L } ^ { \times } ) ^ { b b }$ , which establishes the major part of

Theorem 2.4 (Baily-Borel [2]).
If $\Gamma$ is neat, then the ringed space $\Gamma \backslash \mathbb { L } ^ { b b }$ defines a complex-analytic line bundle $\mathcal { L }$ on the compact analytic space $X ^ { b b } : = \Gamma \backslash \mathbb { D } ^ { b b }$ .
This bundle is ample so that $X ^ { b b }$ is in fact projective and the partition $\{ X ( V ^ { I } ) \} _ { I \in \mathbb { Z } }$ that comes with its definition is a finite decomposition into subvarieties.
The sections of its kth tensor power are precisely the $\Gamma$ -automorphic forms of degree $k$ .
The requirement that $\Gamma$ be neat may be dropped, provided that $\mathcal { L }$ is understood as an orbiline bundle.

Actually a bit of a shortcut is possible: if one only knows that $\Gamma \backslash \mathbb { D } ^ { b b }$ is compact, then the fact that the $\Gamma$ -automorphic forms separate the points of $\Gamma \backslash \mathbb { D } ^ { b b }$ can be used to show that it is an analytic space.

2.5 (Baily-Borel extension).
Locally, the Baily-Borel compactification exists on an intermediate level as an extension in a suitable complex-analytic category.
We explain.
For $I \in \mathbb { Z }$ , we consider the open neighborhood

$$
S t a r ( \pi _ { V _ { I } } \mathbb { D } ) : = \prod _ { J \leq I } \pi _ { V _ { J } } \mathbb { D }
$$

of $\pi _ { V _ { I } } \mathbb { D }$ in $\mathbb { D } ^ { b b }$ .
There is an evident retraction $S t a r ( \pi _ { V _ { I } } \mathbb { D } )  \pi _ { V _ { I } } \mathbb { D }$ (as a morphism of ringed spaces) which is equivariant relative to the action of the $\Gamma$ -stabilizer $\Gamma _ { I }$ of $I$ .
If $\Gamma ^ { I } \subset \Gamma _ { I }$ denotes the subgroup that acts as the identity on $\pi _ { V _ { I } } \mathbb { D }$ , then $\Gamma ^ { I } \backslash S t a r ( \pi _ { V _ { I } } \mathbb { D } )$ is already a normal analytic space and the projection

$$
\Gamma ^ { I } \backslash S t a r ( \pi _ { V _ { I } } \mathbb { D } )  \pi _ { V _ { I } } \mathbb { D }
$$

is analytic.
The group $\Gamma ^ { I } / \Gamma _ { I }$ acts properly discretely on the base and hence also on the total space.
It follows that we have a morphisms of analytic spaces

$$
\Gamma \backslash { \mathbb { D } } ^ { b b } \left. \Gamma _ { I } \backslash S t a r ( \pi _ { V _ { I } } { \mathbb { D } } ) \right. X ( V ^ { I } ) .
$$

that are the identity on $X ( V ^ { I } )$ .
Reduction theory tells us that the first map is an isomorphism over a neighborhood of $X ( V ^ { I } )$ .
In other words, there exists a neighborhood $U _ { I }$ of $\pi _ { V _ { I } } \mathbb { D }$ in $S t a r ( \pi _ { V _ { I } } \mathbb { D } )$ such that every $\Gamma$ -orbit meets that neighborhood in a $\Gamma _ { I }$ -orbit or not at all, so that $\Gamma _ { I } \backslash U _ { I }$ maps isomorphically onto a neighborhood of $X ( I ^ { \perp } )$ in $X ^ { b b }$ .
We shall refer to the extensions (of normal analytic spaces) $\Gamma ^ { I } \backslash \mathbb { D } \subset \Gamma ^ { I } \backslash S t a r ( \pi _ { V _ { I } } \mathbb { D } )$ and $\Gamma _ { I } \backslash \mathbb { D } \subset \Gamma _ { I } \backslash S t a r ( \pi _ { V _ { I } } \mathbb { D } )$ as Baily-Borel extensions.

Remark 2.6. It can be shown that for every nonzero $\mathbb { Q }$ -isotropic subspace $I \subset V$ , the Baily-Borel extension of $\Gamma ^ { I } \backslash \mathbb { D }$ is a normal Stein space.
Since the boundary of this extension is of dimension $\leq 1$ , this gives for $n = \dim \mathbb { D } \geq 3$ the a priori characterization of the Baily-Borel extension as a Stein completion of $\Gamma ^ { I } \backslash \mathbb { D }$ .

3. Modification over a one-dimensional boundary component

In this section we fix a $\mathbb { Q }$ -isotropic plane $J$ and we abbreviate

$$
Z : = \Gamma ^ { J } \backslash \mathbb { D } , \quad Z ( J ) : = \Gamma ^ { J } \backslash \pi _ { J } \mathbb { D } .
$$

Recall that $Z$ is a punctured disk bundle over $Z ( J )$ and that $Z ( J )$ is a relative abelian variety over the half-plane $\pi _ { J ^ { \perp } } \mathbb { D }$ .
To be precise, $\Gamma ^ { J }$ defines a lattice $M \subset$ $( J \otimes J ^ { \perp } / J ) ( \mathbb { R } )$ so that if we ignore the complex structure on $Z ( J )$ we get a $M \otimes$ $\mathbb { R } / \mathbb { Z } )$ -principal bundle.
We also recall that the center of the Heisenberg group $\Gamma ^ { J }$ has a preferred generator so that formation of the commutator therefore defines a nondegenerate symplectic form $M \times M \to \mathbb { Z }$ .
This form is a positive multiple of the symplectic form that is defined by

$$
\begin{array} { r } { ( J \otimes J ^ { \perp } / J ) \times \left( J \otimes J ^ { \perp } / J \right) \xrightarrow { \phi _ { J } } J \times J \to \wedge ^ { 2 } J \cong \mathbb { C } , } \end{array}
$$

where $\phi _ { J }$ is quadratic form on $J ^ { \perp } / J$ induced by $\phi$ .

The Baily-Borel extension $Z ^ { b b }$ adds to $Z$ a copy of $\pi _ { J ^ { \bot } } \underline { { \mathbb { D } } }$ and its analytic structure can be understood as follows.
Filling in the zero section of the punctured disk bundle $Z \to Z ( J )$ (so a copy of $Z ( J )$ ) produces a disk bundle.
This disk bundle is a simple example of the class of toric extensions considered by Mumford et al.
in [1], and so we denote that bundle ${ Z ^ { t o r }  Z ( J ) }$ .
The bundle is contained in the total space of a line bundle $\ell$ over $Z ( J )$ ; we can identify $\ell$ with the normal bundle of the zero section.
The first Chern class of $\ell$ is given by the symplectic form above and from what has been remarked there it follows that its Riemann form on $J ^ { \perp } / J$ is a positive multiple of $\phi _ { J }$ .
Since $\phi _ { J }$ is negative definite, the classical theory of abelian varieties then guarantees that the zero section can be analytically contracted in $Z ^ { t o r }$ along the projection $Z ( J ) \to \pi _ { J ^ { \bot } } \mathbb { D }$ .
The result of this contraction is the Baily-Borel extension $Z ^ { b b }$ of $Z$ .

3.1. In fact, any $\mathbb { Q }$ -subspace $L$ of $J ^ { \perp }$ that contains $J$ defines a partial blowup

$$
Z ^ { L } \to Z ^ { b b }
$$

of the Baily-Borel extension by contracting $Z ( J )$ along the $L ( \mathbb { R } )$ -orbits in $Z ( J )$ (instead of contracting along $Z ( J ) \to \pi _ { J ^ { \perp } } \mathbb { D }$ ).
This can be done analytically for the same reason as before, but perhaps a clearer picture is obtained by dividing out not by $\Gamma ^ { J }$ , but by $\Gamma ^ { L }$ , the subgroup of elements of $\Gamma _ { J }$ that act as the identity on $V / L$ and to define a Baily-Borel extension of $\Gamma ^ { L } \backslash \mathbb { D }$ as follows.
First note that $\Gamma ^ { L } \backslash \mathbb { D }$ is a punctured disk bundle over $\Gamma ^ { L } \backslash \pi _ { J } \mathbb { D }$ , the latter being a bundle of abelian varieties over $\pi _ { L } \mathbb { D }$ .
Filling in the zero section adds a copy of $\Gamma ^ { L } \backslash \pi _ { J } \mathbb { D }$ .
We obtain the BailyBorel extension alluded to by contracting the zero section along the projection $\Gamma ^ { L } \backslash \pi _ { J } \mathbb { D }  \pi _ { L } \mathbb { D }$ .
The abelian group $\Gamma ^ { J } / \Gamma ^ { L }$ acts on this Baily-Borel extension properly discontinuously and if we pass to the quotient space we get the partial blowup described above.

However for our purpose it is better to work in a Satake setting from the start.
This goes as follows.
Let $N _ { L }$ denote the group of real orthogonal transformations of $V$ that leave the flag $\{ 0 \} \subset J \subset L \subset V$ invariant and act as the identity on the successive quotients.
This is a Heisenberg subgroup of $N _ { J }$ .
We then put a topology on the disjoint union $\mathbb { D } ^ { L } : = \mathbb { D } \sqcup \pi _ { L } \mathbb { D }$ : if we define for a subset $K \subset \mathbb { D }$ its $L$ -saturation as the subset

$$
{ \cal K } ^ { L } : = { \cal N } _ { L } \exp ( \sqrt { - 1 } C _ { J } ) { \cal K } \prod \pi _ { L } ( { \cal N } _ { L } \exp ( \sqrt { - 1 } C _ { J } ) { \cal K } )
$$

of $\mathbb { D } ^ { L }$ , then the collection of open subsets of $\mathbb { D }$ and their $L$ -saturations define a $N _ { J }$ - invariant topology on $\mathbb { D } ^ { L }$ .
If we give it the structure of a ringed space in the usual manner, then $\Gamma ^ { L } \backslash \mathbb { D } ^ { L }  \pi _ { L } \mathbb { D }$ is a morphism of normal analytic spaces that exhibits $\Gamma ^ { L } \backslash \mathbb { D } ^ { L }$ as a ‘mapping cylinder’ of the relative abelian variety $\Gamma ^ { L } \backslash \pi _ { J } \mathbb { D }  \pi _ { L } \mathbb { D }$ .
The projection $\pi _ { L } \mathbb { D } \to \pi _ { J ^ { \perp } } \mathbb { D }$ is, if we ignore the complex structure, also a principal bundle of the vector group $( J ^ { \perp } / L \otimes J ) ( \mathbb { R } )$ .
The group $\Gamma ^ { J } / \Gamma ^ { L }$ may be identified with a lattice in this vector group and hence

$$
Z ( L ) : = ( \Gamma ^ { J } / \Gamma ^ { L } ) \backslash \pi _ { L } \mathbb { D } \to \pi _ { J ^ { \perp } } \mathbb { D }
$$

is an abelian torsor.
The group $\Gamma ^ { J } / \Gamma ^ { L }$ also acts on the map $\Gamma ^ { L } \backslash \mathbb { D } ^ { L }  \pi _ { L } \mathbb { D }$ .
This action is proper and free (because it is so on the base), so that we have an analytic retraction

$$
Z ^ { L } \to Z ( L ) .
$$

If $L ^ { \prime }$ is a $\mathbb { Q }$ -subspace of $L$ containing $J$ , then we have a natural map $Z ^ { L ^ { \prime } } \to Z ^ { L }$ that is the identity on $Z$ .
It is clear that this is a proper analytic morphism.

3A.
Arrangements near the boundary component.
We encounter such a situation if we are given a $\Gamma ^ { J }$ -invariant collection $\mathcal { H }$ of $\mathbb { Q }$ -hyperplanes of $V$ that contain $J$ in which $\Gamma ^ { J }$ has only finitely many orbits.
The subspace $L$ of $J ^ { \perp }$ in question is then $\cap _ { H \in \mathcal { H } } H \cap J ^ { \perp }$ .
For each $H \in \mathcal { H }$ , the intersection $\mathbb { D } _ { H } : = \mathbb { D } \cap \mathbb { P } ( H )$ is a domain of the same type as $\mathbb { D }$ whose image in $Z$ is of the same type as $Z$ .
This image, which we denote by $Z _ { H }$ , is a smooth hypersurface in $Z$ .
The inclusion of $Z _ { H }$ in $Z$ has a Baily-Borel extension $Z _ { H } ^ { b b } \to Z ^ { b b }$ (as ringed spaces, so analytic) which is injective and proper.
The image is the closure of $Z _ { H }$ in $Z$ , which is in general only a Weil divisor.
The situation is different for its closure in $Z ^ { L }$ .
First notice that the boundary of $\mathbb { D } _ { H }$ in $\mathbb { D } ^ { L }$ is the hyperplane section $\pi _ { L } \mathbb { D } _ { H }$ of $\pi _ { L } \mathbb { D }$ and that the $\mathbb { D } ^ { L }$ -closure of $\mathbb { D } _ { H }$ , $\| \mathsf { D } _ { H } \cup \pi _ { L } \mathbb { D } _ { H }$ , is the preimage of $\pi _ { L } \mathbb { D } _ { H }$ under the retraction $\mathbb { D } ^ { L } \to \pi _ { L } \mathbb { D }$ .
The image of $\pi _ { L } \mathbb { D } _ { H }$ in the abelian torsor $Z ( L )$ is an abelian subtorsor $Z ( L ) _ { H }$ of codimension one, and this is also the boundary of $Z _ { H }$ in $Z ^ { L }$ .
It is clear that the $Z ^ { L }$ -closure of $Z _ { H }$ is the preimage of $Z ( L ) _ { H }$ under the retraction $Z ^ { L } \to Z ( L )$ .
In particular, this closure is a Cartier divisor.
This proves the first part of the following lemma.

Lemma 3.2. The $Z ^ { L }$ -closure of each hypersurface $Z _ { H }$ is a Cartier divisor so that the collection of these defines an arrangement in $Z ^ { L }$ .
For some positive integer $k$ , the fractional ideal $\begin{array} { r l } { ~ } & { { } \sum _ { H } \mathcal { O } _ { Z _ { L } } ( k Z _ { H } ) } \end{array}$ is generated by its global sections.
These global sections separate the points of the arrangement complement in $Z ^ { L }$ and that arrangement complement is Stein.

Proof.
Assume for a moment that $\mathcal { H }$ is a single $\Gamma ^ { J }$ -orbit.
So if $H \ \in \ { \mathcal { H } }$ , then $L = H \cap J ^ { \perp }$ and $Z ^ { L } \to Z ( L )$ is a relative elliptic curve.
Choose $e \in J - \{ 0 \}$ .
If $H$ is defined by the linear form $f _ { 0 }$ on $V$ , then $g _ { 0 } ( z ) : = f _ { 0 } ( z ) / \phi ( z , e )$ is a well-defined function on $\mathbb { D }$ , which even factors through $\pi _ { L } \mathbb { D }$ .
We form

$$
E ^ { ( k ) } : = \sum _ { g \in \Gamma ^ { L } g _ { 0 } } g ^ { - k }
$$

The index set of this series is actually a rank two quotient of $\Gamma ^ { L }$ : it is in fact a classical Eisenstein series.
For $k > 2$ the series represents a meromorphic function on $Z ( L )$ which has a pole of exact order $k$ along $Z ( L ) _ { H }$ and nowhere else.
The algebra generated by these Eisenstein series (over the algebra of holomorphic functions on the upper half-plane $\pi _ { L } \mathbb { D }$ ) contains a set of generators of $\mathcal { O } _ { Z ( L ) } ( k Z ( L ) _ { H } )$ , when $k$ is sufficiently large.
By viewing these as sections of $\mathcal { O } _ { Z ^ { b b } } ( k Z _ { H } )$ , the lemma follows in this case.

The general case is easily deduced from this: for each $H \in \mathcal { H }$ , we get a morphism $Z ^ { L } \ \to \ Z ^ { H \cap J ^ { \bot } }$ such that the $Z ^ { L }$ -closure of $Z _ { H }$ is the preimage of the $Z ^ { H \cap J ^ { \perp } }$ - closure of $Z _ { H }$ .
This implies the second assertion of the lemma.
As the morphism $Z ^ { L } \to Z ^ { H \cap J ^ { \bot } }$ only depends on the $\Gamma ^ { J }$ -orbit of $H$ , there is a natural morphism from $Z ^ { L }$ to the fiber product of the blowups $Z ^ { H \cap J ^ { \bot } } \to Z ^ { b b }$ , where $H$ runs over the finite set $\Gamma ^ { J } \backslash \mathcal { H }$ .
This morphism is finite.
The arrangement complement in $Z ^ { L }$ is the preimage under this finite map of a fiber product of Stein manifolds over a Stein manifold and hence Stein.
□

Corollary 3.3. Denote by $D \subset Z$ the union of the hypersurfaces $Z _ { H }$ .
If $L$ is of dimension $\geq 2$ , then $Z ^ { L } \to Z ^ { b b }$ is the normalized blowup of the fractional ideal $O _ { Z ^ { b b } } ( D )$ and the arrangement complement in $Z ^ { L }$ is the Stein completion of the arrangement complement $Z - D$ (that is, $Z ^ { L }$ is a Stein space which has the same algebra of holomorphic functions as $Z - D _ { - }$ ).

Proof.
According to Lemma 3.2, the arrangement on $Z ^ { L }$ is a Cartier divisor and its complement in $Z ^ { L }$ is Stein.
A meromorphic function on $Z ^ { b b }$ which is regular on $Z - D$ defines a meromorphic function on $Z ^ { L }$ .
The polar set of the latter is of pure codimension one everywhere and lies in the preimage of the arrangement.
Hence it lies in the arrangement on $Z ^ { L }$ .
So the direct image of ${ \mathcal { O } } _ { Z ^ { L } } ( k D )$ on $Z ^ { b b }$ is $\mathcal { O } _ { Z ^ { b b } } ( k D )$ .
The corollary follows.
□

The arrangement on $Z ^ { L }$ is in fact the preimage of an arrangement on $Z ( L )$ under the retraction $Z ^ { L } \to Z ( L )$ ; we denote its complement in $Z ^ { L }$ by $( Z ^ { L } ) ^ { \circ }$ .
So we can form without difficulty the arrangement blowup of $Z ^ { L }$ as in Part I [16] to obtain

$$
{ \widetilde { Z ^ { \circ } } } \to Z ^ { L } .
$$

It follows from Lemma 3.2 that this is the blowup of an ideal:

Proposition 3.4. The morphism $\widetilde { Z ^ { \circ } }  Z ^ { b b }$ is the blowup of the fractional ideal $\sum _ { H } \mathcal { O } _ { Z ^ { b b } } ( Z _ { H } )$ .

It is worth noting that we can also obtain $\widetilde { Z ^ { \circ } }$ as the $\Gamma ^ { J }$ -quotient of the arrangement blowup of $\mathbb { D } ^ { \mathcal { H } } \to \mathbb { D } ^ { L }$ (since this is locally the preimage of an ordinary analytic blowup under a retraction, the absence of a locally compact setting is of cause of concern).
The exceptional divisors of this blowup are indexed by the collection $\operatorname { P O } ( \mathcal { H } )$ of intersections of members from $\mathcal { H }$ .
This index set is partially ordered by inclusion and the exceptional divisors indexed by a subset of $\mathrm { P O } ( \mathcal { H } )$ have nonempty common intersection if and only if this subset is linearly ordered.

3B.
Arrangements that define $\mathbb { Q }$ -Cartier divisors.
The closure of $Z _ { H }$ in $Z ^ { J }$ is the bundle restriction of the disk bundle $Z ^ { J } \to Z ( J )$ to $Z ( J ) _ { H } \subset Z ( J )$ .
There is a $\mathbb { Q }$ -linear form $l _ { H } : J ^ { \perp } / J \to \mathbb { C }$ whose zero set is the hyperplane $H \cap J ^ { \perp } / J$ in $J ^ { \perp } / J$ and has the property that the rank two symplectic form

$$
( J ^ { \perp } / J \otimes J ) \times ( J ^ { \perp } / J \otimes J ) \xrightarrow { l _ { H } \otimes { \bf 1 } \times l _ { H } \otimes { \bf 1 } } J \times J \to \wedge { ^ { 2 } J } \cong \mathbb { C }
$$

represents the first Chern class of $Z _ { H } ^ { t o r } \cdot A$ .
This linear form is clearly unique up to sign and its square, $l _ { H } ^ { 2 }$ , is the Riemann form of the divisor $Z _ { H } ^ { t o r } \cdot A$ .

A $\Gamma _ { J }$ -invariant function $H \in { \mathcal { H } } \to m _ { H } \in \mathbb { Q }$ defines a Cartier divisor $Z _ { \mathcal { H } } ( m )$ on $Z$ (in an orbi-sense) and a Weil divisor on $Z ^ { b b }$ which we also denote by $Z _ { \mathcal { H } } ( m )$ .

The following proposition appears in a somewhat different guise in a recent paper by Bruinier and Freitag (Proposition 4.4 of [8]).

Proposition 3.5. The Weil divisor $Z _ { \mathcal { H } } ( m )$ is a $\mathbb { Q }$ -Cartier divisor if and only if the quadratic form $\sum _ { H \in \Gamma ^ { J } \backslash \mathcal { H } } n _ { H } l _ { H } ^ { 2 }$ on $J ^ { \perp } / J$ (where the sum is over a system of representive $\Gamma ^ { J }$ -orbits in $\mathcal { H }$ ) is proportional to $\phi _ { J }$ .

Proof.
The proof is standard (see also Section 6 of [16]): if $Z _ { \mathcal { H } } ( m )$ is principal on $Z ^ { b b }$ , then some multiple must be defined by a section of a tensor power of $\ell$ .
Comparing Chern classes then gives the proportionality assertion.
If conversely the quadratic forms are proportional, then the restriction of the strict transform of $Z _ { \mathcal { H } } ( m )$ in $Z ^ { J }$ to $A$ and $\ell$ have proportional Chern classes.
So a nonzero multiple of the former is a divisor of a tensor power of $\ell$ translated over an element of $M \otimes \mathbb { R } / \mathbb { Z }$ .
It is not hard to check that this translation lies in $M \otimes \mathbb { Q } / \mathbb { Z }$ .
So a nonzero multiple of the strict transform of $Z _ { \mathcal { H } } ( m )$ on $Z ^ { J }$ is the pull-back along $Z ^ { J }  A$ of a divisor of a tensor power of $\ell$ .
This means that this multiple is the divisor of a holomorphic function on $Z ^ { b b }$ .
□

Corollary 3.6. If $\mathcal { H }$ is nonempty and such that the union of the hypersurfaces $Z _ { H }$ supports an effective principal divisor, then the common intersection of $J ^ { \perp }$ and the hyperplanes from $\mathcal { H }$ is equal to $J$ .

Proof.
This is because a Riemann form of such a divisor will vanish on $\cap _ { H \in \mathcal { H } } H \cap$ $J ^ { \perp } / J$ .
□

3C.
Application to moduli spaces of $K 3$ surfaces.
We digress to show that this corollary almost immediately implies that the moduli space of polarized $K 3$ - surfaces of given genus and without rational double points cannot be affine.

It is well-known that for any integer $g \ \geq \ 2$ the moduli space of primitively polarized $K 3$ surfaces of genus $g$ $= { \mathrm { d e g r e e 2 } } g - 2 )$ is isomorphic to an arithmetic quotient of an arrangement complement, the isomorphism being induced by a period mapping.
To be precise, consider the $K 3$ -lattice

$$
\Lambda : = E _ { 8 } ( - 1 ) \perp E _ { 8 } ( - 1 ) \perp { \cal U } \perp { \cal U } \perp { \cal U } .
$$

Here $E _ { 8 } ( - 1 )$ stands for the $E _ { 8 }$ lattice whose quadratic form has been multiplied by $^ { - 1 }$ (so this lattice is negative definite of rank 8) and $U$ is the hyperbolic lattice of rank two.
The latter has isotropic generators $e , f$ with inner product 1. Consider

the vector $h _ { g } : = e _ { 3 } + ( g - 1 ) f _ { 3 }$ in the last hyperbolic summand.
It is indivisible and has self product $2 g - 2$ .
Its orthogonal complement is

$$
\Lambda _ { g } \cong E _ { 8 } ( - 1 ) \perp E _ { 8 } ( - 1 ) \perp { \cal U } \perp { \cal U } \perp { \cal I } ( 2 - 2 g ) ,
$$

where $I ( 2 - 2 g )$ is the rank one lattice with a generator whose self product is $2 - 2 g$ (in this case $e _ { 3 } + ( 1 - g ) f _ { 3 } )$ .
Notice that its signature is $( 2 , 1 9 )$ .
Let $\mathbb { D } _ { g } \subset \mathbb { P } ( \Lambda _ { g } \otimes \mathbb { C } )$ be as usual and let $\Gamma _ { g }$ be the group of $\gamma \in \mathrm { O } ( \Lambda )$ that fix $h _ { g }$ and leave $\mathbb { D } _ { g }$ invariant.
Consider the collection $N _ { g }$ of $\left( - 2 \right)$ -vectors in $\Lambda _ { g }$ which span with $h _ { g }$ a primitive sublattice of $\Lambda$ .
(In case $g > 2$ , all $\left( - 2 \right)$ -vectors span with $h _ { g }$ a primitive sublattice, but for $g = 2$ that is not the case: take for instance $e _ { 3 } - f _ { 3 }$ .) It is known that $N _ { g }$ is an orbit under the group $\Gamma _ { g }$ .
The collection of hyperplanes in $\Lambda _ { g } \otimes \mathbb { C }$ orthogonal to a member of $N _ { g }$ is an arithmetic arrangement and determines therefore an irreducible divisor $D _ { g }$ on $X _ { g } : = \Gamma _ { g } \backslash \mathbb { D } _ { g }$ .
Its complement $X _ { g } \mathrm { ~ - ~ } D _ { g }$ can be identified with the coarse moduli space of $K 3$ surfaces of genus $g$ .
The question has been raised whether $D _ { g }$ is definable by an automorphic form.
Nikulin [19] proved by means of a Koecher principle that the answer is no for arbitrary large values of $g$ .
We shall see right away the necessary condition stated in Corollary 3.6 fails for all $g$ , so that the answer is no always.
This necessary condition comes down to the requirement that for every isotropic rank 2 sublattice $1 1 \subset \Lambda ^ { g }$ , the image of $\Pi ^ { \perp } \cap N _ { g }$ in the negative definite lattice $\Pi ^ { \perp } \cap \Lambda _ { g } / \Pi$ spans a sublattice of maximal rank.
This is clearly not the case: for the simplest choice $\mathrm { I I } = \mathbb { Z } e _ { 1 } + \mathbb { Z } e _ { 2 }$ we have

$$
\Pi ^ { \perp } \cap \Lambda _ { g } / \Pi \cap \Lambda _ { g } \cong E _ { 8 } ( - 1 ) \perp E _ { 8 } ( - 1 ) \perp I ( 2 - 2 g ) ,
$$

and the image of $N _ { g } \cap \Pi ^ { \perp }$ herein consists of all the $\left( - 2 \right)$ -vectors in the first two summands.
So this image spans a sublattice of corank one.

# 4. Semitoric extension of certain tube domains

We shall describe a class of modifications of the Baily-Borel extension of tube domain quotients in terms of combinatorial data.
This class was introduced in [12], [14] and there baptized the class of semitoric extensions.
It includes both Mumford’s toric extensions and the Baily-Borel extension as special cases.

Definition 4.1. Let $L$ be a finite dimensional complex vector space defined over $\mathbb { Q }$ .
Recall that a convex cone in $L ( \mathbb { R } )$ is called nondegenerate if it does not contain an affine line.
We shall call a cone rational if it is the convex cone spanned by a finite subset of $L ( \mathbb { Q } )$ .
We say that a finite collection $\Sigma$ of nondegenerate rational convex cones in $L ( \mathbb { R } )$ is a rational cone system if a face of a member of $\Sigma$ belongs to $\Sigma$ and any two members of $\Sigma$ meet along a common face.

If $L$ is obtained from tensoring the cocharacter group of an algebraic torus with $\mathbb { C }$ , then a rational cone system $\Sigma$ in $L ( \mathbb { R } )$ determines a normal torus embedding of that torus.
This construction is well-known, but since we prefer to work with a torsor of such a torus, or rather with its universal cover, it may be worthwhile to present this from a corresponding, inherently analytic, point of view.
One reason being that this will make the connection with the Baily-Borel compactification clearer.

So let us start with an affine space $A$ over $L$ and a lattice $L ( \mathbb { Z } ) \subset L ( \mathbb { Q } )$ .
Then $L / L ( \mathbb { Z } )$ is an algebraic torus and $L ( \mathbb { Z } ) \backslash A$ is a principal homogeneous space for this torus.
A rational cone system $\Sigma$ in $L ( \mathbb { R } )$ determines a normal affine torus embedding

$L ( \mathbb { Z } ) \backslash A \subset ( L ( \mathbb { Z } ) \backslash A ) ^ { \Sigma }$ as follows.
For $\sigma \in \Sigma$ , denote by $\pi _ { \sigma } : A \to \langle \sigma \rangle _ { \mathbb { C } } \backslash A$ the projection along the complex span of $\sigma$ and consider the finite disjoint union

$$
A ^ { \Sigma } : = \coprod _ { \sigma \in \Sigma } \langle \sigma \rangle _ { \mathbb { C } } \backslash A .
$$

Notice that $L$ acts on $A ^ { \Sigma }$ .
For every $K \subset A$ and $\sigma \in \Sigma$ , let

$$
K ( \sigma ) : = \coprod _ { \tau \leq \sigma } \pi _ { \tau } ( \langle \sigma \rangle _ { \mathbb { R } } + { \sqrt { - 1 } } \sigma + K ) \subset A ^ { \Sigma } .
$$

If $K$ runs over the open subsets of $A$ and $\sigma$ over $\Sigma$ , then we get a $L$ -invariant topology on $A ^ { \Sigma }$ .
We make $A ^ { \Sigma }$ a ringed space by endowing it with the sheaf of complex valued continuous functions that are analytic on its affine pieces.
The lattice $L ( \mathbb { Z } )$ acts as a group of automorphisms of this ringed space and if we pass to the orbit space in this category, then we get a normal analytic variety that can be identified with the torus embedding $( L ( \mathbb { Z } ) \backslash A ) ^ { \Sigma }$ .

We need local versions of the above notions.

Definition 4.2. Let $C \subset L ( \mathbb { R } )$ be an open nondegenerate convex cone and denote by $C _ { + } \supset C$ the convex hull of $L ( \mathbb { Q } ) \cap { \overline { { C } } }$ (this is a nondegenerate cone also).
A subset of $C _ { + }$ is said to be a locally rational cone in $C _ { + }$ if its intersection with every rational subcone of $C _ { + }$ is rational.
A collection of convex cones in $L ( \mathbb { R } )$ is said to be a locally rational decomposition of $C _ { + }$ if the union of these cones is $C _ { + }$ and the restriction to every rational subcone of $C _ { + }$ is a rational cone system.

The coarsest locally rational decomposition of $C$ is the collection of faces of $C _ { + }$ (this includes $C _ { + }$ itself); for reasons that will become clear below, we shall denote this facial decomposition of $C _ { + }$ by $\Sigma ( b b )$ (the abbreviation of Baily-Borel).

More interesting examples involve a cone that is homogeneous under a real semisimple group defined over $\mathbb { Q }$ .
The following special case is relevant for what follows.

Example 4.3 (See [14]).
Assume $C$ is a quadratic cone.
More precisely, assume there exists a nondegenerate symmetric bilinear form $L \times L \to \mathbb { C }$ , $( x , y ) \mapsto x \cdot y$ , defined over $\mathbb { Q }$ and of hyperbolic signature $( 1 , \dim L - 1 )$ such that $C$ is a connected component of the set of $x \in L ( \mathbb { R } )$ with $x \cdot x > 0$ .
Let $\Gamma$ be an arithmetic subgroup of the orthogonal group of $L ( \mathbb { Q } )$ which preserves $C$ .
Here are two constructions of $\Gamma$ -invariant locally rational decomposition of $C _ { + }$ .

(a) Given a finite union $\boldsymbol { \mathcal { O } }$ of $\Gamma$ -orbits in $L ( \mathbb { Q } ) \cap C _ { + }$ , let $\Sigma$ be the coarsest decomposition of $C _ { + }$ which is closed under ‘taking faces’ and is such that $\operatorname { i n f } _ { p \in { \mathcal { O } } } ( - \cdot$ ) is linear on its members.
Then $\Sigma$ is a locally rational decomposition of $C _ { + }$ .
If $\boldsymbol { \mathcal { O } }$ $p$ is a single $\Gamma$ -orbit, then the members of $\Sigma$ are rational polydral cones if and only if $\mathcal { O } \subset C$ .
If $\boldsymbol { \mathcal { O } }$ is a regular orbit, then a maximal member of $\Sigma$ is a fundamental domain for the action of $\Gamma$ on $C _ { + }$ .

(b) Let $\mathcal { H }$ be a collection of $\mathbb { Q }$ -hyperplanes of $L$ which meet $C$ such that the corresponding subset of the Grassmannian of $L$ is a finite union of $\Gamma$ -orbits.
Then this collection is locally finite on $C$ and decomposes $C _ { + }$ into locally rational decomposition $\Sigma ( \mathcal { H } )$ .

In a similar fashion, a locally rational decomposition of $C _ { + }$ will define a semitoric embedding (of an open subset of this torus).
In its full generality, this notion is a bit involved, but since we only need it for the case of Example 4.3, we restrict ourself to that case.
So in the remainder of this section (as well in the next) we are in

The setting 4.4. Let $( L , \cdot )$ , $C$ and $\Gamma$ be as in Example 4.3: we are given a nondegenerate symmetric bilinear form $L \times L \to \mathbb { C }$ , $( x , y ) \mapsto x \cdot y$ , defined over $\mathbb { Q }$ and of hyperbolic signature $( 1 , \dim L - 1 )$ , a connected component $C$ of the set of $x \in L ( \mathbb { R } )$ with $x \cdot x > 0$ and an arithmetic subgroup $\Gamma$ of the orthogonal group of $L ( \mathbb { Q } )$ which preserves $C$ .
We let $\Sigma$ be a $\Gamma$ -invariant locally rational decomposition of $C _ { + }$ .
We further assume given an affine space $A$ over $L$ defined over $\mathbb { R }$ and a group $\bar { \Gamma }$ of affine-linear transformations of $A$ whose translation subgroup $L ( \mathbb { Z } )$ is a lattice in $L ( \mathbb { Q } )$ with $\Gamma$ as linear quotient.
Since $A$ is defined over $\mathbb { R }$ we can identify it with $A ( \mathbb { R } ) \times { \sqrt { - 1 } } L ( \mathbb { R } )$ .
Its open subset ${ \mathcal { C } } : = A ( \mathbb { R } ) \times { \sqrt { - 1 } } C$ is a tube domain invariant under the action $\bar { \Gamma }$ .
That action is proper since the action of $\Gamma$ on $C$ is.
So the orbit space $Z : = { \tilde { \Gamma } } \backslash { \mathcal { C } }$ is in a natural manner a normal analytic variety.

The semitoric embeddings we are about to define are extensions of $Z$ as a normal analytic variety.
But before we start, it is useful to understand the $\Gamma$ -stabilizer $\Gamma _ { \sigma }$ of a $\sigma \in \Sigma$ , at least up to a subgroup of finite index. In case $\sigma \in \Sigma$ meets $C$ , then the subgroup of $\Gamma$ that acts as the identity on the orthogonal complement of $\sigma$ is of finite index in the $\Gamma$ -stabilizer $\Gamma _ { \sigma }$ of $\sigma$ (because that orthogonal complement is negative definite) and so $\ddot { \Gamma } _ { \sigma }$ acts on $\langle \sigma \rangle _ { \mathbb { C } } \backslash A$ via the extension of a finite group by the translation group $L ( \mathbb { Z } ) / L ( \mathbb { Z } ) \cap \langle \sigma \rangle _ { \mathbb { R } }$ .

In case $\sigma \in \Sigma$ spans an isotropic line $I$ in $L$ , then we have a homomorphism

$$
\exp : I \otimes I ^ { \perp } / I \to \mathrm { S O } ( L )
$$

which assigns to $e \otimes f$ the transformation

$$
\begin{array} { r } { l \mapsto l + ( l \cdot e ) \tilde { f } - ( l \cdot \tilde { f } ) e + \frac { 1 } { 2 } ( \tilde { f } \cdot \tilde { f } ) ( l \cdot e ) e , } \end{array}
$$

where $\bar { f } \in I ^ { \perp }$ is a lift of $f$ .
The image is the unipotent radical of the $\mathrm { S O } ( L )$ - stabilizer of $I$ .
The generator $e _ { \sigma }$ of the semigroup $\sigma \cap L ( \mathbb { Z } )$ enables us to identify $I \otimes I ^ { \perp } / I$ with $I ^ { \perp } / I$ .
The group of $f \in I ^ { \perp } / I$ that correspond via this identification to an element of $\Gamma$ make up a lattice (contained in the image of $L ( \mathbb { Z } ) \cap I ^ { \perp } )$ and this subgroup of $\Gamma$ is of finite index in $\Gamma _ { \sigma }$ .
Let us, for the sake of simplicity, assume that we have equality here: so if $\gamma \in \Gamma$ acts trivially on $I ^ { \perp }$ or $L / I$ , then $\gamma = 1$ .
The $\bar { \Gamma }$ -stabilizer $\ddot { \Gamma } _ { \sigma }$ of $\sigma$ is an extension of this abelian group by $L ( \mathbb { Z } )$ .
This extension does not split: it is a Heisenberg group with center generated by the translation over $e _ { \sigma }$ .
Consider now the restriction of the chain of affine maps $A \to I \backslash A \to I ^ { \perp } \backslash A$ to $c$ :

$$
\mathcal { C } \to \pi _ { I } \mathcal { C } \to \pi _ { I ^ { \bot } } \mathcal { C } .
$$

The last space is a copy of an upper half-plane on which $\tilde { \Gamma } _ { \sigma }$ acts via an infinite cyclic group of translations (the image of $L ( \mathbb { Z } )$ in $L / I ^ { \perp }$ ).
Dually, the first projection is an upper half-plane bundle and the group of elements of $\boldsymbol { \tilde { \Gamma } _ { \sigma } }$ that act as the identity on $I \backslash A$ is generated by the translation $e _ { \sigma }$ .
The second projection is a fibration by affine spaces: it is the restriction of $I \backslash A  I ^ { \perp } \backslash A$ to $\pi _ { I ^ { \bot } } \mathcal { C }$ .
The Heisenberg group $\tilde { \Gamma } _ { \sigma }$ acts on each fiber of $I \backslash A  I ^ { \perp } \backslash A$ as a lattice of translations (relative to the underlying real affine space) with the center acting trivially.
So if we pass to orbit spaces with respect to $\boldsymbol { \tilde { \Gamma } _ { \sigma } }$ , we find that $\tilde { \Gamma } _ { \sigma } \backslash { \mathcal C }$ is a punctured disk bundle over $\tilde { \Gamma } _ { \sigma } \backslash \pi _ { I } \mathcal { C }$ and that the latter is a bundle of complex tori (isogenous to a repeated fiber product of the bundle of elliptic curves with itself) over the punctured disk $\Gamma _ { \sigma } \backslash \pi _ { I ^ { \perp } } \mathcal { C }$ .
Compare this with our discussion of the isotropic planes in Section 2.

Lemma-Definition 4.5. Let $\sigma \in \Sigma$ .
If $\tau \in \Sigma$ is such that $\tau \geq \sigma$ and $\tau \cap C \neq \emptyset$ , then the common zero set of the real linear forms on $V$ which are nonnegative on $\tau$ and zero on $o$ is a subspace that is independent of $\tau$ .
We call this subspace the $\Sigma$ -support space of $\sigma$ and denote it by $L _ { \sigma }$ .
It is the complex span of $\sigma$ unless $\sigma$ spans an isotropic line $I$ , in which case $L _ { \sigma }$ is the intersection of the hyperplane $I ^ { \perp }$ and the complex linear spaces $\langle \tau \rangle _ { \mathbb { C } }$ with $\tau \in \Sigma$ and $\tau > \sigma$ .

Proof.
These assertions are clear in case $\sigma$ is not an isotropic half line.
So let us assume that $\sigma$ spans an isotropic line $I$ .
We observe that the image of $C$ under the projection $\pi _ { I } : L \to L / I$ is a real half-space bounded by $( I ^ { \perp } / I ) ( \mathbb { R } )$ .
The image of $C _ { + }$ under this projection is the union of that half-space plus the origin; we prefer to think of this image as a cone over a real affine space $A _ { I } ( \mathbb { R } )$ over $( I \otimes I ^ { \perp } / I ) ( \mathbb { R } )$ .
As we have seen, a subgroup of finite index of the stabilizer $\Gamma _ { \sigma }$ acts on this affine space as a lattice of translations.
Any $\tau \in \Sigma$ with $\sigma < \tau$ maps under $\pi _ { I }$ to a (possibly degenerate) convex cone in $\pi _ { I } ( C _ { + } )$ and thus determines a rational polyhedron in $A _ { I } ( \mathbb { R } )$ .
These cones decompose $A _ { I } ( \mathbb { R } )$ in a locally finite $\Gamma _ { \sigma }$ -invariant manner.
A minimal member of this decomposition must be an affine subspace of $A _ { I } ( \mathbb { R } )$ .
If $U \subset I ^ { \bot } / I ( \mathbb { R } )$ denotes its translation space, then it clear that this is contained in the translation space of the members of the decomposition of $A _ { I } ( \mathbb { R } )$ that are adjacent to this minimal member.
With induction it follows that the whole decomposition is invariant under $U$ and is the preimage of a decomposition of $U \backslash A _ { I } ( \mathbb { R } )$ into bounded rational polyhedra.
The assertions now follow easily with $L _ { \sigma }$ characterized by the property that $L _ { \sigma } / I \otimes I$ is the complexification of $U$ □

So the support spaces of $\Sigma ( b b )$ are $V$ , $\{ 0 \}$ and the hyperplanes orthogonal to a $\mathbb { Q }$ -isotropic line.

We define an extension of $\boldsymbol { \mathscr { C } }$ as a ringed space.
Let

$$
\pi _ { \sigma } : = \pi _ { L _ { \sigma } } : A  L _ { \sigma } \backslash A .
$$

be the projection along $L _ { \sigma }$ and denote by $\tilde { \Gamma } ^ { \sigma }$ be the subgroup of $\gamma \in \tilde { \Gamma }$ which preserve $\sigma$ and each fiber of $\pi _ { \sigma }$ .
Then $\Gamma ^ { \sigma } \cdot ( L _ { \sigma } ( \mathbb { R } ) + \sqrt { - 1 } \sigma )$ is a semigroup of transformations of $A$ which preserves $\boldsymbol { \mathscr { C } }$ .
We put a topology on the disjoint union

$$
c ^ { \Sigma } : = \coprod _ { \sigma \in \Sigma } \pi _ { \sigma } \mathcal { C }
$$

as follows.
If $\Sigma$ is the facial decomposition, then we also write ${ \mathcal { C } } ^ { b b }$ instead of ${ \mathcal { C } } ^ { \Sigma ( b b ) }$ .
For every $K \subset { \mathcal { C } }$ and $\sigma \in \Sigma$ , let

$$
K ^ { \Sigma } ( \tilde { \Gamma } , \sigma ) : = \coprod _ { \tau \in \Sigma , \tau \leq \sigma } \pi _ { \tau } ( \tilde { \Gamma } ^ { \sigma } ( L _ { \sigma } ( \mathbb { R } ) + \sqrt { - 1 } \sigma + K ) ) .
$$

If $K$ is open in $\boldsymbol { \mathscr { C } }$ , then so is $\tilde { \Gamma } ^ { \sigma } ( L _ { \sigma } ( \mathbb { R } ) + \sqrt { - 1 } \sigma + K )$ .
So if we let $K$ run over the open subsets of $\boldsymbol { \mathscr { C } }$ and $\sigma$ over $\Sigma$ , we get a $\tilde { \Gamma }$ -invariant topology on $\mathcal { C } ^ { \Sigma }$ that is invariant under the $\bar { \Gamma }$ -stabilizer $\ddot { \Gamma } _ { \sigma }$ of $\sigma$ .
We make $\mathcal { C } ^ { \Sigma }$ a ringed space by equipping it with the sheaf of continuous, piecewise analytic complex valued functions.
We denote the $\tilde { \Gamma }$ -orbit space of $\mathcal { C } ^ { \Sigma }$ (as a ringed space) by $Z ^ { \Sigma }$ .
It is clear that $Z ^ { \Sigma }$ naturally decomposes into finitely many subspaces of the type

$$
Z ( \sigma ) : = \tilde { \Gamma } _ { \sigma } \backslash \pi _ { \sigma } \mathcal { C } .
$$

Let us first get a rough picture of the incidence relations.
For every $\sigma \in \Sigma$ , the set $A ( \mathbb { R } ) + { \sqrt { - 1 } } ( C \cap S t a r ( \sigma ) )$ is open in $c$ and has the virtue that if a $\bar { \Gamma }$ -orbit meets

$\mathit { { \vec { C } } _ { \sigma } }$ , then it meets the latter in a $\boldsymbol { \tilde { \Gamma } _ { \sigma } }$ -orbit.
This is also true for the interior of the closure of this set in $\mathcal { C } ^ { \Sigma }$ ,

$$
U _ { \sigma } : = \prod _ { \tau \leq \sigma } \pi _ { \tau } ( A ( \mathbb { R } ) + { \sqrt { - 1 } } ( S t a r ( \sigma ) \cap C ) ) .
$$

This is an open neighborhood of $\pi _ { \sigma } { \mathcal { C } }$ that comes with a natural retraction on $\pi _ { \sigma } { \mathcal { C } }$ (a morphism in the category of ringed spaces).
Notice that $U _ { \sigma }$ and $U _ { \tau }$ are disjoint unless $\sigma \cup \tau$ is contained in a member of $\Sigma$ , in which case their intersection is $U _ { \sigma \vee \tau }$ .
The map

$$
\tilde { \Gamma } _ { \sigma } \backslash U _ { \sigma }  Z ^ { \Sigma }
$$

is an isomorphism onto an open neighborhood $U _ { Z ( \sigma ) }$ of $Z ( \sigma )$ that retracts naturally onto $Z ( \sigma )$ .
This clearly helps us in understanding $Z ^ { \Sigma }$ as a ringed space.

We now investigate what the strata $Z ( \sigma )$ are like.
When $\sigma \in \Sigma$ meets $C$ , then by the previous discussion $Z ( \sigma )$ is a finite quotient of the algebraic torus torsor $( L _ { \sigma } + L ( \mathbb { Z } ) ) \backslash A$ .
The situation is somewhat more involved in case $\sigma \in \Sigma$ spans an isotropic line $I$ .
Then we have a flag of vector spaces $I \subseteq L _ { \sigma } \subseteq I ^ { \bot }$ which yields the factorization

$$
\mathcal { C } \to \pi _ { I } \mathcal { C } \to \pi _ { \sigma } \mathcal { C } \to \pi _ { I ^ { \perp } } \mathcal { C } .
$$

The preceding discussion shows that $\tilde { \Gamma } _ { \sigma } \backslash { \mathcal C }$ is a punctured disc bundle over $\tilde { \Gamma } _ { \sigma } \backslash \pi _ { I } \mathcal { C }$ and that the latter is a bundle of abelian varieties over the punctured disk $\tilde { \Gamma } _ { \sigma } \backslash \pi _ { I ^ { \perp } } \mathcal { C }$ which contains the stratum $Z ( \sigma )$ as an abelian subbundle.

So every stratum $Z ( \sigma )$ of $Z ^ { \Sigma }$ is in fact an analytic orbifold.
For $\sigma \neq \{ 0 \}$ it is either of toric or of (relative) abelian type.
This is of course precisely the situation that we considered in Section 3.

Proposition 4.6. The ringed space $Z ^ { \Sigma }$ is a normal analytic space.
Each stratum $Z ( \sigma )$ receives the normal analytic structure exhibited above (so that it becomes locally closed for the analytic Zariski topology of $Z ^ { \Sigma }$ ) and the retraction $U _ { Z ( \sigma ) } \to Z ( \sigma )$ is analytic.

Proof.
We only give some indications of the proof; for details we refer to [14] (a key point of the argument also appears in [13]).
According to Baily-Borel [2], Theorem 92, we must verify the following properties:

(i) The space $Z ^ { \Sigma }$ is locally compact Hausdorff.  
(ii) The topological boundary of each stratum $Z ( \sigma )$ is a union of lower dimensional strata.  
(iii) The space $Z ^ { \Sigma }$ is normal in the topological sense that it has a basis for its topology whose members meet $Z$ in connected subsets.  
(iv) For every stratum $Z ( \sigma )$ , the restriction map from the $Z ( \sigma )$ -restriction of ${ \mathcal { O } } _ { Z ^ { \Sigma } }$ to the structure sheaf of $Z ( \sigma )$ is surjective.  
(v) Each point of $Z ^ { \Sigma }$ has a neighborhood on which the local sections of ${ \mathcal { O } } _ { Z ^ { \Sigma } }$ separate the points.

Property (i) can be proved directly as in [14]: given a compact subset $K$ of $\boldsymbol { \mathscr { C } }$ one shows, using the fact that $\Gamma$ has a rational cone in $C _ { + }$ as fundamental domain, that $K ^ { \Sigma } ( \tilde { \Gamma } , \{ 0 \} )$ maps to a compact subset of in $Z ^ { \Sigma }$ .
It is clear that this implies that every point of $Z ^ { \Sigma }$ has a compact neighborhood.

The fact that $Z ( \sigma )$ is a retract of a neighborhood immediately implies that distinct points of $Z ( \sigma )$ have disjoint neighborhoods in $Z ^ { \Sigma }$ .
The Hausdorff property for other pairs is somewhat more subtle, but not that hard.
We sketch another proof below that it is perhaps more instructive.

Properties (ii) and (iii) are easy.

Property (iv) is immediate from the fact that the retraction $U _ { Z ( \sigma ) } \to Z ( \sigma )$ is a morphism of ringed spaces.

Property (v) is proved as follows.
Fix a $\sigma \in \Sigma$ .
Let $f : A  \mathbb { C }$ be a real affinelinear form whose linear part is nonnegative on $\sigma$ and in some point of $C$ (the latter is automatic if $\sigma$ meets $C$ , of course).
Denote by $e _ { 0 } ^ { f }$ the restriction of $\exp ( 2 \pi \sqrt { - 1 } f )$ to $\boldsymbol { \mathscr { C } }$ .
Let $\tau \leq \sigma$ .
If the linear part of $f$ vanishes on $\tau$ , then it vanishes on $L _ { \tau }$ by Lemma 4.5 and so $f$ factors over $L _ { \tau } \backslash A$ .
We denote the corresponding factor of $e _ { \tau } ^ { f }$ on $\pi _ { \tau } \mathcal { C }$ by $e _ { \tau } ^ { f }$ .
Otherwise $e _ { \tau } ^ { f }$ stands for the zero function on $\pi _ { \tau } \mathcal { C }$ .
The union of the functions just defined is easily seen to be continuous on the basic open set $U _ { \sigma }$ .
So that function, denoted $e ^ { f }$ , is a local section of the structure sheaf.
Now assume in addition that the linear part of $f$ is integral on $L ( \mathbb { Z } )$ .
It is clear that $e ^ { f }$ then factors through $L ( \mathbb { Z } ) \backslash U _ { \sigma }$ .
If $\boldsymbol { \mathcal { O } }$ denotes the $\tilde { \Gamma } _ { \sigma }$ -orbit of $e ^ { f }$ , then a straightforward estimate shows that $\sum _ { f ^ { \prime } \in \mathcal { O } } e ^ { f ^ { \prime } }$ converges on $U _ { \sigma }$ uniformly on subsets of the form $K ^ { \Sigma } ( \tilde { \Gamma } , \sigma )$ with $K \subset U _ { \sigma }$ compact.
So this defines a section over $U _ { Z ( \sigma ) }$ of the structure sheaf.
One verifies that there are sufficiently many of these functions to separate the points of UZ(σ).
□

Remark 4.7. One can show that each open subset $U _ { Z ( \Sigma ) }$ is a Stein space.

Suppose we are given another $\tilde { \Gamma }$ -invariant locally rational decomposition $\Sigma ^ { \prime }$ which is refined by $\Sigma$ .
So every $\sigma \in \Sigma$ is contained in a member of $\Sigma ^ { \prime }$ .
If $\sigma ^ { \prime } \in \Sigma ^ { \prime }$ is the smallest member with this property, then $L _ { \sigma } \subset L _ { \sigma ^ { \prime } }$ and hence there is a natural projection $\pi _ { \sigma } { \mathcal { C } } \to \pi _ { \sigma ^ { \prime } } { \mathcal { C } }$ .
It follows that we have an evident map

$$
\mathcal { C } ^ { \Sigma } \to \mathcal { C } ^ { \Sigma ^ { \prime } }
$$

of which it is straightforward to verify that it is a morphism of ringed spaces (i.e., is continuous and takes the local sections of the sheaf on the range to local sections of the sheaf on the domain).
In particular, we have always a morphism ${ \mathcal { C } } ^ { \Sigma } \to { \mathcal { C } } ^ { b b }$ .
So if we write $Z ^ { b b }$ for $Z ^ { \Sigma ( b b ) }$ , then:

Corollary 4.8. The projection $Z ^ { \Sigma } \to Z ^ { \Sigma ^ { \prime } }$ is a proper analytic morphism.
In particular, we have a proper analytic morphism $Z ^ { \Sigma } \to Z ^ { b b }$ .

4.9. We show that an extension of $Z$ as decribed above lies between the minimal extension $Z ^ { b b }$ and one of toric type.
This can be used to give another proof that $Z ^ { \Sigma }$ and $Z ^ { b b }$ are locally compact Hausdorff (which is perhaps somewhat easier then the one sketched above because it brings us in an analytic context at an earlier stage).
First assume that $\Sigma$ is a decomposition into rational cones.
This is the case considered by Mumford and his collaborators [1]: $\Sigma$ determines a normal torus embedding $L ( \mathbb { Z } ) \backslash A \subset ( L ( \mathbb { Z } ) \backslash A ) ^ { \Sigma }$ and $L ( \mathbb { Z } ) \backslash { \mathcal { C } } ^ { \Sigma }$ can be identified with the interior of the closure of $L ( \mathbb { Z } ) \backslash { \mathcal { C } }$ in this torus embedding.
So then we are in the nice situation that $L ( \mathbb { Z } ) \backslash { \mathcal { C } } ^ { \Sigma }$ has the structure of a normal analytic space.
The group $\Gamma$ acts on this analytic space and one verifies that the action is properly discrete.
Hence its orbit space is in a natural way a normal analytic space as well.
It is not hard to see that this orbit space can be identified with $Z ^ { \Sigma }$ .

We have seen that the boundary strata of $Z ^ { \Sigma }$ come in two types: the toric strata indexed by $\sigma \in \Sigma$ which meet $C$ and the abelian strata indexed by an isotropic half-line.
A toric stratum is an algebraic torus modulo a finite group and is relatively compact in $Z ^ { \Sigma }$ ; an abelian stratum is a hypersurface in $Z ^ { \Sigma }$ that is fibered over a punctured disc.
The morphism to the Baily-Borel extension, $Z ^ { \Sigma } \to Z ^ { b b }$ , contracts each toric stratum to a point and is on an abelian stratum the collapse to a punctured disc.

For a general $\Sigma$ , we are in between these two extremes.
For instance, we may intersect $\Sigma$ with any $\Gamma$ -invariant decomposition of $C _ { + }$ into rational cones to produce a refinement $\tilde { \Sigma }$ as above.
We then have a continous map $\pi : Z _ { \tilde { \Sigma } }  Z ^ { \Sigma }$ .
It is not difficult to show that $Z ^ { \Sigma }$ has the quotient topology with respect to this map.
The fibers are compact and connected.
From this it follows that $\pi$ is proper and that $Z ^ { \Sigma }$ is locally compact Hausdorff.
The functions constructed in our first proof show that $\pi _ { * } \mathcal { O } _ { Z _ { \widetilde { \Sigma } } }$ separates the points of $Z ^ { \Sigma }$ .
So this contraction is analytic.

# 5. Arrangements on tube domains

We restrict ourself to the case where the decomposition of $C _ { + }$ arises as in $\mathrm { E x }$ - ample 4.3-b. To be precise, we assume given a finite union $\tilde { \mathcal { H } }$ of $\tilde { \Gamma }$ -orbits in the collection of affine hyperplanes of $A$ which are defined over $\mathbb { Q }$ and meet $c$ .
The corresponding collection $\mathcal { H }$ of linear hyperplanes of $L$ is then as in Example 4.3- b and so defines a locally rational decomposition $\Sigma ( \mathcal { H } )$ of $C _ { + }$ .
Notice that the $\Sigma ( \mathcal { H } )$ -support space of a face spanning an isotropic line $I$ is equal to $I ^ { \perp }$ in case no member of $\mathcal { H }$ contains $I$ and is the common intersection of the $H \in \mathcal { H }$ that contain $I$ otherwise.

For $\tilde { H } \in \tilde { \mathcal { H } }$ , we denote by $\mathcal { C } _ { \tilde { H } }$ the hyperplane section $\mathcal { C } \cap \bar { H }$ .
The $\mathcal { C } ^ { \Sigma ( \mathcal { H } ) }$ -closure of $\mathcal { C } _ { \tilde { H } }$ is of the same form as $\mathcal { C } ^ { \Sigma ( \mathcal { H } ) }$ itself: it meets a stratum $\pi _ { \sigma } { \mathcal { C } }$ if and only if $\sigma \subset H$ and in that case the intersection is $\pi _ { \sigma } ( \mathcal { C } _ { \tilde { H } } )$ .
In other words, we get the extension of $\mathcal { C } _ { \tilde { H } }$ defined by the arrangement restriction of $\ddot { \mathcal { H } }$ to $\tilde { H }$ .
This applies in fact to arbitrary intersections: if a collection of such hypersurfaces has nonempty intersection, then their common intersection meets $\boldsymbol { \mathscr { C } }$ and the inclusion of the latter in the former is of the same type as ${ \mathcal { C } } \subset { \mathcal { C } } ^ { \Sigma ( { \mathcal { H } } ) }$ .
If we regard the $\mathcal { C } ^ { \Sigma ( \mathcal { H } ) }$ -closures of the hypersurfaces $\mathcal { C } _ { \tilde { H } }$ as an arrangement on $\mathcal { C } ^ { \Sigma ( \mathcal { H } ) }$ , then the retractions $U _ { \sigma } \to \pi _ { \sigma } { \mathcal { C } }$ are compatible with this arrangement: the restriction of the arrangement to $U _ { \sigma }$ is the preimage of its restriction to $\pi _ { \sigma } { \mathcal { C } }$ .
So the arrangement is in normal directions as if it were one in an analytic manifold.

The hyperplane section $\mathcal { C } _ { \tilde { H } }$ maps to an irreducible hypersurface $Z _ { \tilde { H } }$ in $Z$ .
This is a Cartier divisor which only depends on the image of $\tilde { H }$ in $\Gamma \backslash \tilde { \mathcal { H } }$ and since the latter set is finite, so is the collection divisors thus obtained.
The union of the corresponding collection of hypersurfaces will be denoted by $D$ .
We have the following analogue of Lemma 3.2.

Lemma 5.1. The closure of $Z _ { \tilde { H } }$ in $Z ^ { \Sigma ( \mathcal { H } ) }$ is a Cartier divisor.

Proof.
We show that the closure of $Z _ { \tilde { H } }$ in $Z ^ { \Sigma ( \mathcal { H } ) }$ is Cartier in the neighborhood $U _ { Z ( \sigma ) }$ of $Z ( \sigma )$ .
For this we use the retraction $U _ { \sigma } \to \pi _ { \sigma } { \mathcal { C } }$ .
The members of $\ddot { \mathcal { H } }$ that are parallel to $L _ { \sigma }$ define a locally finite arrangement on $\pi _ { \sigma } { \mathcal { C } }$ and thus determine an arrangement of Cartier divisors on $Z ( \sigma )$ .
The preimage of this arrangement in $U _ { Z ( \sigma ) }$ under the retraction $U _ { Z ( \sigma ) } \to Z ( \sigma )$ is the trace of the collection of closures of the $Z _ { H }$ ’s on this open set.
The lemma follows.
□

Lemma 5.2. After passing to a subgroup of $\Gamma$ of finite index, the closure of any hypersurface $Z _ { \tilde { H } }$ in $Z ^ { \Sigma ( \mathcal { H } ) }$ is without selfintersection.

Proof.
This is similar to that of Lemma 5.1 in Part I [16] and so we omit it.

Proposition 5.3. For some $k > 0$ , $\begin{array} { r } { \sum _ { \tilde { H } } \mathcal { O } _ { Z ^ { \Sigma ( \mathcal { H } ) } } ( k Z _ { \tilde { H } } ) } \end{array}$ is generated by its global sections and these global sections separate the points of the arrangement complement in $Z ^ { \Sigma ( \mathcal { H } ) }$ .
The arrangement complement in $Z ^ { \Sigma ( \mathcal { H } ) }$ is Stein.

Proof.
Since $Z ^ { \Sigma ( \mathcal { H } ) }$ is normal, we are already satisfied if we can find a set of global sections $f _ { 0 } , \ldots , f _ { N }$ of $\begin{array} { r } { \sum _ { \tilde { H } } \mathcal { O } _ { Z ^ { \Sigma ( \mathcal { H } ) } } ( k Z _ { \tilde { H } } ) } \end{array}$ which generate the latter as a sheaf such that the associated meromorphic map $Z ^ { \Sigma ( \mathcal { H } ) } \to \mathbb { P } ^ { N } \times Z ^ { b b }$ is regular on the arrangement complement and has finite fibers there.
By passing to a subgroup of $\bar { \Gamma }$ of finite index we may and will assume that each $Z _ { \tilde { H } }$ is without selfintersection.
Since $Z ^ { b b }$ is Stein, its global holomorphic functions separate its points.

Fix a $\ddot { H } _ { 0 } \in \ddot { \mathcal { H } }$ and choose an affine-linear form $f _ { 0 } : A  \mathbb { C }$ defined over $\mathbb { R }$ which has $\ddot { H } _ { 0 }$ as zero hyperplane.

If $K \subset { \mathcal { C } }$ is compact, then a standard estimate shows that the number of $f \in \ddot { \Gamma } f _ { 0 }$ with $N - 1 < \operatorname* { s u p } _ { K } | d f | \leq N$ is bounded by a polynomial in $N$ of degree $2 \dim L - 1$ .
This implies that for $k > 2 \dim L$ , the series

$$
S _ { \tilde { \Gamma } f _ { 0 } } ^ { ( k ) } : = \sum _ { f \in \tilde { \Gamma } f _ { 0 } } f ^ { - k }
$$

normally converges to a $\tilde { \Gamma }$ -invariant analytic function on $\mathcal { C } - \cup _ { \tilde { H } \in \tilde { \Gamma } \{ H _ { 0 } \} } \mathcal { C } _ { H }$ .
We claim however that such an estimate holds, not just on $K$ , but also on $\tilde { \Gamma } ( K + L ( \mathbb { R } ) +$ $\sqrt { - 1 } C _ { + }$ ).
To see this, we choose a rational cone $\mathrm { ~ \bf ~ l ~ l ~ } \subset \mathrm { ~ \cal { C } _ { + } ~ }$ such that $\Gamma { \bf l } { \bf l } = C _ { + }$ (these exist, see [1], Ch.
II, 4.3, Thm.

1. and then observe that what is needed here is to show that for some compact $K ^ { \prime } \subset C$ , the number of $\operatorname { I m } ( f ) \in \Gamma \operatorname { I m } ( f _ { 0 } )$ with $N - 1 < \operatorname* { s u p } _ { \Pi \cap \Gamma _ { \cdot } ( K ^ { \prime } + C _ { + } ) } | \operatorname { I m } ( f ) | \leq N$ is bounded by a polynomial of degree $\dim L - 1$ in $N$ .
   According to [1], Ch.
   II, $\ S 5$ , Π∩Γ.
   $( K ^ { \prime } { + } C _ { + } )$ is of the form $K ^ { \prime \prime } { + \Pi }$ with $K ^ { \prime \prime } \subset \Pi$ compact.
   So it is enough to verify our estimates on $K ^ { \prime \prime } { + \Pi }$ .
   But this follows from the fact that only finitely many $H \in \mathcal { H }$ meet $\textstyle 1 1 \cap C$ .

As a consequence, (k) $S _ { \tilde { \Gamma } f _ { 0 } } ^ { ( k ) }$ represents a $\tilde { \Gamma }$ -invariant analytic function on the arrangement complement in $\mathcal { C } ^ { \Sigma ( \mathcal { H } ) }$ with a pole of exact order $k$ along the omitted hypersurfaces, the restriction to $\pi _ { \sigma } { \mathcal { C } }$ being given by the subseries whose terms are constant on the fibers of $\pi _ { \sigma }$ .
We show that this yields enough of such functions to separate the points of the arrangement complement in $Z ^ { \Sigma ( \mathcal { H } ) }$ .
In case $\sigma$ is an isotropic half-line this has been established in Section 3. So let us focus on the remaining case, namely when $\sigma$ meets $C$ .
Then $\pi _ { \sigma } { \mathcal { C } }$ is an affine space and $\Gamma ( \sigma )$ contains the image of $L ( \mathbb { Z } )$ in $L / L _ { \sigma }$ as a subgroup of finite index. Since $L _ { \sigma }$ is an intersection of members of $\mathcal { H }$ , the issue is easily reduced to the one-dimensional case, as phrased in Lemma 5.4 below.
□

Lemma 5.4. Let a be a positive integer.
Then for $k > 1$ the series

$$
S ^ { ( k ) } ( z ) : = \sum _ { n \in \mathbb { Z } } ( a z + n ) ^ { - k }
$$

is a rational function in $\exp ( 2 \pi \sqrt { - 1 } z )$ .
If we use the latter to identify $\mathbb { C } / \mathbb { Z }$ with $\mathbb { C } ^ { \times }$ and if the set of ath roots of unity is regarded as a (reduced) divisor $\mu _ { a }$ on $\mathbb { C } ^ { \times }$ , then $k ( \mu _ { a } )$ is the polar divisor of $S ^ { ( k ) }$ .

Proof.
Normal convergence away from the set of poles is easy.
So we may think of $S ^ { ( k ) }$ as a meromorphic function on $\mathbb { C } ^ { \times }$ .
That the poles are as decribed is also clear.
It remains to see that $S ^ { ( k ) }$ is rational as a function on $\mathbb { C } ^ { \times }$ .
This will follow if we show that it is also meromorphic at $0$ and $\infty$ .
But since the series defining $S ^ { ( k ) }$ converges absolutely and uniformly on $| \operatorname { I m } ( z ) | > 1$ , $| \operatorname { R e } ( z ) | \leq 1$ , we see that the latter is even holomorphic at these points.
□

Corollary 5.5. Denote by $D$ the union of the hypersurfaces $Z _ { H }$ in $Z$ .
If no stratum in $Z ^ { \Sigma ( \mathcal { H } ) }$ is of codimension one (which in case $\mathrm { d i m } ( L ) > 2$ amounts to: any intersection of members of $\mathcal { H }$ which meets $C _ { + } - \{ 0 \}$ is of dimension $\geq 2$ ), then $Z ^ { \Sigma ( \mathcal { H } ) }$ is the blowup of the fractional ideal $O _ { Z ^ { b b } } ( D )$ and the arrangement complement in $Z ^ { \Sigma ( \mathcal { H } ) }$ is the Stein completion of $Z - D$ .

Proof.
According to Lemma 5.1, the arrangement on $Z ^ { \Sigma ( \mathcal { H } ) }$ is a Cartier divisor.
A meromorphic function on $Z ^ { b b }$ which is regular on $Z$ defines a meromorphic function on $Z _ { \mathcal { H } ( \Sigma ) }$ .
The polar set of the latter is of pure codimension one everywhere and lies in the preimage of the arrangement.
Hence it lies in the arrangement on $Z _ { \mathcal { H } ( \Sigma ) }$ .
So the direct image of $\mathcal { O } _ { Z ^ { \Sigma ( H ) } } ( k D )$ on $Z ^ { b b }$ is $\mathcal { O } _ { Z ^ { b b } } ( k D )$ .
The assertions then follow from Proposition 5.3. □

If we are in the situation of the conclusion of Lemma 5.2, then we may form the arrangement blowup of $Z ^ { \Sigma ( \mathcal { H } ) }$ relative to the closures of the hypersurfaces $\{ Z _ { \tilde { H } } \} _ { \tilde { H } \in \tilde { \mathcal { H } } }$ .
But it is better to work independently of $\tilde { \Gamma }$ and to introduce this blowup as the $\tilde { \Gamma }$ -quotient of an arrangement blowup of $\mathcal { C } ^ { \Sigma ( \mathcal { H } ) }$ .
We can perform that blowup as in Part I [16] to obtain

$$
{ \widetilde { \mathscr { C } ^ { \circ } } } \to { \mathscr { C } } ^ { \Sigma ( \mathcal { H } ) } .
$$

Since this is locally the preimage of an ordinary analytic blowup under a retraction, the absence of a locally compact setting is of no concern to us.
The exceptional divisors of this blowup are indexed by the collection PO( $\bar { \mathcal { H } } | _ { c } )$ of intersections of members from $\tilde { \mathcal { H } }$ that have nonempty intersection with $c$ .
This index set is partially ordered by inclusion and the exceptional divisors indexed by a subset of $\mathrm { P O } ( \ddot { \mathcal { H } } | _ { \mathcal { C } } )$ have nonempty common intersection if and only if this subset is linearly ordered.
If we pass to $\tilde { \Gamma }$ -orbit spaces we get an analytic morphism

$$
\widetilde { Z ^ { \circ } } : = \widetilde { \Gamma } \backslash \widetilde { \mathcal { C } ^ { \circ } }  Z ^ { \Sigma ( \mathcal { H } ) } .
$$

It follows from the preceding that this is the blowup of an ideal on $Z ^ { b b }$ :

Proposition 5.6. The morphism $\widetilde { Z ^ { \circ } }  Z ^ { b b }$ is the blowup of the fractional ideal $\sum _ { \tilde { H } } \mathcal { O } _ { Z ^ { b b } } \big ( Z _ { \tilde { H } } \big )$ .

5A.
Arrangements definable by a product expansion.
This subsection is not indispensable for the rest of this paper.
We here investigate the situation where the arrangement complement $Z - D$ is Stein.
Suppose we are given a $\tilde { \Gamma }$ -invariant function $\tilde { H } \in \tilde { \mathcal { H } } \mapsto m _ { \tilde { H } } \in \mathbb { Z }$ .
This defines a Cartier divisor

$$
Z _ { \tilde { \mathcal { H } } } ( m ) : = \sum _ { \tilde { H } \in \Gamma \backslash \tilde { \mathcal { H } } } m _ { \tilde { H } } Z _ { \tilde { H } }
$$

on $Z$ which we also regard as a Weil divisor on $Z ^ { b b }$ .
We ask a similar question as in Section 3: when is $Z _ { \tilde { \mathcal { H } } } ( m )$ Cartier on $Z ^ { b b }$ ? Proposition 3.5 gives us immediately a rather strong necessary condition: recall that $Z ^ { b b } - Z$ has strata $Z ( \sigma )$ , with $\sigma$ either a $\mathbb { Q }$ -isotropic half-line of $C _ { + }$ (these have dimension one) and or $\sigma = \{ 0 \}$ (this is a singleton).
In the former case $\sigma$ , the local structure of $Z ^ { b b }$ near $Z ( \sigma )$ is not very complicated: as we have seen that it is basically like the $\ddot { \Gamma } _ { I }$ -orbit space of $\mathcal { C } \sqcup \pi _ { I ^ { \bot } } \mathcal { C }$ , where $I$ is the span of $I$ .
This is the situation considered in 3.5. Let us translate the statement of that proposition to the present situation.
The $\bar { \Gamma }$ -stabilizer $\tilde { \Gamma } _ { I }$ of $I$ has finitely many orbits in the set $\mathcal { \tilde { H } } ^ { I }$ of $I$ -invariant members of $\tilde { \mathcal { H } }$ .
Every $\tilde { H } \in \tilde { \mathcal { H } } ^ { I }$ determines a -hyperplane in $I ^ { \perp } / I$ and has associated to it a -linear form given up to sign defining this hyperplane: $\pm l _ { \tilde { H } } : I ^ { \perp } / I \to \mathbb { C }$ .
Its square $l _ { \tilde { H } } ^ { 2 }$ depends in a $\ddot { \Gamma } _ { I }$ -invariant manner on $\ddot { H }$ and in order that $Z _ { \tilde { \mathcal { H } } } ( m )$ is principal near $Z ( \sigma )$ a necessary and sufficient condition is that the quadratic form

$$
\sum _ { \tilde { H } \in \tilde { \Gamma } _ { I } \backslash \tilde { \mathcal { H } } ^ { I } } m _ { \tilde { H } } l _ { \tilde { H } } ^ { 2 }
$$

on $I ^ { \perp } / I$ is proportional to the form that the given hyperbolic form induces on this subquotient of $L$ .
If $\mathcal { \tilde { H } } ^ { I }$ is nonempty, then this proportionality factor must be nonzero and so the intersection of the hyperplanes taken from $\mathcal { \bar { H } } ^ { I }$ must be reduced to $I$ .
In particular, the $\Sigma ( \mathcal { H } )$ -support space of $\sigma$ as defined in 4.5 is equal to $I$ .

5.7. Let us call a member of $\Sigma ( \mathcal { H } )$ with nonempty interior a chamber of $\Sigma ( \mathcal { H } )$ .
For every chamber $\sigma$ of $\Sigma ( \mathcal { H } )$ and $\ddot { H } \in \ddot { \mathcal { H } }$ , there is a unique affine-linear form $f : A  \mathbb { C }$ with (i) $\ddot { H }$ as zero set, (ii) has a linear part that is positive on $\sigma$ and (iii) whose orbit under the translation lattice $L ( \mathbb { Z } )$ is $f + \mathbb { Z }$ .
We denote that function $f _ { \tilde { H } } ^ { \sigma }$ and let $e ^ { f _ { \tilde { H } } ^ { o } }$ have the meaning as before: the restriction of $\exp ( 2 \pi \sqrt { - 1 } f _ { \tilde { H } } ^ { \sigma } )$ to $c$ .
Since $e ^ { f _ { \tilde { H } } ^ { o } }$ is $L ( \mathbb { Z } )$ -invariant, we may also regard it as a function on $L ( \mathbb { Z } ) \backslash { \mathcal { C } }$ .
If $\sigma ^ { \prime }$ is another chamber then the collection $\tilde { \mathcal { H } } ( \sigma , \sigma ^ { \prime } )$ of members of $\ddot { \mathcal { H } }$ whose translation space separates $\sigma ^ { \prime }$ from $\sigma$ is a union of finitely many $L ( \mathbb { Z } )$ -orbits.
This allows us to define the product

$$
e ^ { m } ( \sigma , \sigma ^ { \prime } ) : = \prod _ { \tilde { H } \in L ( \mathbb { Z } ) \backslash \tilde { \mathcal { H } } ( \sigma , \sigma ^ { \prime } ) } ( - e ^ { f _ { \tilde { H } } ^ { \sigma } } ) ^ { m _ { \tilde { H } } } .
$$

It is easily checked that if $\sigma ^ { \prime \prime }$ is a third member of $\Sigma ( \mathcal { H } )$ , then

$$
e ^ { m } ( \sigma , \sigma ^ { \prime \prime } ) = e ^ { m } ( \sigma , \sigma ^ { \prime } ) . e ^ { m } ( \sigma ^ { \prime } , \sigma ^ { \prime \prime } ) .
$$

It is also clear that $e ^ { m }$ is $\Gamma$ -invariant: for $\gamma \in \Gamma$ we have $e ^ { m } ( \gamma \sigma , \gamma \sigma ^ { \prime } ) = \gamma e ^ { m } ( \sigma , \sigma ^ { \prime } ) ( =$ $( \gamma ^ { - 1 } ) ^ { * } e ( \sigma , \sigma ^ { \prime } ) )$ .
This implies that

$$
e ^ { m } ( \sigma , \gamma \gamma ^ { \prime } \sigma ) = e ^ { m } ( \sigma , \gamma \sigma ) . \gamma e ^ { m } ( \sigma , \gamma ^ { \prime } \sigma ) .
$$

In other words, for a fixed $\sigma$ , $\gamma \in \Gamma \mapsto e _ { \sigma } ^ { m } ( \gamma ) : = e ^ { m } ( \sigma , \gamma \sigma )$ is a 1-cocycle of $\Gamma$ with values in the group of quasi-characters of $L ( \mathbb { Z } ) \backslash A$ .
Such a cocycle defines an action of $\Gamma$ on the trivial line bundle $\mathbb { C } \times L ( \mathbb { Z } ) \backslash A  L ( \mathbb { Z } ) \backslash A$ by letting $\gamma \in \Gamma$ send $( t , z )$ to $( e _ { \sigma } ^ { m } ( \gamma ^ { - 1 } ) ( z ) t , \gamma z )$ .
The special form of $e _ { \sigma } ^ { m }$ makes that the action even extends to one of the semidirect product of $\Gamma$ with the torus $V / L ( \mathbb { Z } )$ .
The restriction of this bundle to $L ( \mathbb { Z } ) \backslash { \mathcal { C } }$ descends to a orbiline bundle on $Z$ that we will denote by $\mathbb { E } ^ { m }$ .
A section of the latter is given by a function $k : L ( \mathbb { Z } ) \backslash { \mathcal { C } }  \mathbb { C }$ with the property that $\gamma k = e _ { \sigma } ^ { m } ( \gamma ) . k$ for all $\gamma \in \Gamma$ .
The identity $e _ { \sigma ^ { \prime } } ^ { m } ( \gamma ) . e _ { \sigma } ^ { m } ( \gamma ) ^ { - 1 } = \gamma e ^ { m } ( \sigma , \sigma ^ { \prime } ) . e ^ { m } ( \sigma , \sigma ^ { \prime } ) ^ { - 1 }$ shows that the cohomology class of $e _ { \sigma } ^ { m }$ is independent of $\sigma$ so that the isomorphism class of $\mathbb { E } ^ { m }$ is well-defined.

A divisor for $\mathbb { E } ^ { m }$ is obtained as follows.
Consider the product expansion

$$
P _ { \sigma } ^ { m } : = \prod _ { \tilde { H } \in L ( \mathbb { Z } ) \backslash \tilde { \mathcal { H } } } ( 1 - e ^ { f _ { \tilde { H } } ^ { \sigma } } ) ^ { m _ { \tilde { H } } } .
$$

It represents an analytic function on $L ( \mathbb { Z } ) \backslash { \mathcal { C } }$ for if $K \subset C$ is compact, then the series $\sum _ { \tilde { H } \in L ( \mathbb { Z } ) \backslash \tilde { \mathcal { H } } } | e ^ { f _ { \tilde { H } } ^ { o } } |$ converges uniformly on $A + { \sqrt { - 1 } } K$ and as is well-known, then the same must hold for the corresponding product.
We notice that $P _ { \sigma } ^ { m }$ satisfies the functional equation

$$
\gamma P _ { \sigma } ^ { m } = e _ { \sigma } ^ { m } ( \gamma ) ^ { - 1 } . P _ { \sigma } ^ { m }
$$

and so $P _ { \sigma } ^ { m }$ represents a section of the dual of $\mathbb { E } ^ { m }$ .
The divisor of this section is clearly $- Z _ { \tilde { \mathcal { H } } } ( m )$ .

Proposition 5.8. The line bundle $\mathbb { E } ^ { m }$ is trivial if and only if there exists a quasicharacter $e ^ { \rho }$ on $L ( \mathbb { Z } ) \backslash { \mathcal { C } }$ such that $\gamma e ^ { \rho } = e _ { \sigma } ( \gamma ) . e ^ { \rho }$ .
This quasicharacter is unique up to constant and in that case $e ^ { - \rho } . P _ { \sigma } ^ { m }$ represents an analytic function on $Z ^ { b b }$ with divisor $Z _ { \tilde { \mathcal { H } } } ( m )$ .

Proof.
The line bundle $\mathbb { E } ^ { m }$ is trivial if and only the line bundle $\mathbb { C } \times L ( \mathbb { Z } ) \backslash { \mathcal { C } } $ $L ( \mathbb { Z } ) \backslash { \mathcal { C } }$ with the given $\Gamma$ -action admits a $\Gamma$ -invariant section.
Such a section amounts to an analytic function $k : L ( \mathbb { Z } ) \backslash { \mathcal { C } }  \mathbb { C } ^ { \times }$ satisfying the functional equation $\gamma k = e _ { \sigma } ^ { m } ( \gamma ) . k$ for all $\gamma \in \Gamma$ .
If we have such a $k$ , then any nonzero term of its Fourier development yields a quasicharacter satisfying the same functional equation.
If two quasicharacters have that property, then their quotient is a $\Gamma$ -invariant quasicharacter.
But it is clear that such a quasicharacter has to be constant.

Given such a $\rho$ , then $e ^ { - \rho } . P _ { \sigma } ^ { m }$ is $\tilde { \Gamma }$ -invariant and hence represents an analytic function on $Z$ .
If $Z ^ { b b } - Z$ is of codimension $\geq 2$ in the normal analytic space $Z ^ { b b }$ , then this function extends analytically to $Z ^ { b b }$ .
But this codimension condition only fails in cases where there is nothing to prove, namely when $\dim L \leq 1$ or $\dim L = 2$ and the form represents zero, for then $\Gamma$ is finite.
□

Remark 5.9. The above proposition can also be phrased in terms of toroidal geometry: for any quasicharacter $e ^ { \rho } : L ( \mathbb { Z } ) \backslash { \mathcal { C } }  \mathbb { C } ^ { \times }$ , we define a continuous function $r : C _ { + } \to \mathbb { R }$ which is $\mathbb { Z }$ -valued on $L ( \mathbb { Z } ) \cap C _ { + }$ and piecewise affine-linear relative to the decomposition $\Sigma ( \mathcal { H } )$ by letting it on $\sigma ^ { \prime } \in \Sigma ( \mathcal { H } )$ be given as the linear part of $\rho$ plus the sum of the linear parts of the functions $m _ { \tilde { H } } f _ { \tilde { H } }$ , where $\ddot { H }$ runs over a system of representatives of the (finitely many) $L ( \mathbb { Z } )$ -orbits in $\bar { \mathcal { H } } ( \sigma , \sigma ^ { \prime } )$ .
Since $f _ { \tilde { H } }$ is constant on $\tilde { H }$ , the function $r$ is well-defined and continuous.
(In case $m _ { \tilde { H } } \geq 0$ for all $\tilde { H }$ , then this function is also convex in the sense that the set of $( x , t ) \in C _ { + } \times \mathbb { R }$ with $t \geq r ( x )$ has that property.) Then $e ^ { \rho }$ satisfies the functional equation if and only if $r$ is $\Gamma$ -invariant.
It is not hard to show that a converse also holds: any $\Gamma$ - invariant $\mathbb { R }$ -valued continuous function $r : C _ { + } \to \mathbb { R }$ that is $\mathbb { Z }$ -valued on $L ( \mathbb { Z } ) \cap C _ { + }$ and piecewise affine-linear with respect to the decomposition $\Sigma ( \mathcal { H } )$ comes from a function $m : \tilde { \Gamma } \backslash \tilde { \mathcal { H } }  \mathbb { Z }$ to which the above proposition applies.

Proposition 5.8 yields strong restrictions on the chamber structure:

Proposition 5.10. Suppose that we are in the situation where Proposition 5.8 applies: the closure of $D$ in $Z ^ { b b }$ is the support of a (not necessarily) effective Cartier divisor.
Assume also that $\mathrm { d i m } ( L ) > 2$ and that $\mathcal { H }$ is nonempty.
Given a chamber $\sigma$ of $\Sigma ( \mathcal { H } )$ , let $v _ { \sigma } \in L ( \mathbb { Q } )$ be characterized by the property that the inner product with $v _ { \sigma }$ is the linear part of $\rho$ , where $e ^ { \rho }$ is as in 5.8. Then:

(i) the $\Gamma$ -stabilizers of $\sigma$ and $v _ { \sigma }$ coincide,  
(ii) $\sigma$ is a rational cone if and only if $v _ { \sigma } \cdot v _ { \sigma } > 0$ , and  
(iii) in case $o$ is not a rational cone, then (a) $v _ { \sigma }$ is isotropic and nonzero, (b) $v _ { \sigma }$ lies in the span of an isotropic edge of $\sigma$ , (c) $\Gamma _ { \sigma }$ contains a finite index subgroup which is free abelian of rank $\mathrm { d i m } ( L ) - 2$ and $( d ) \ \sigma$ is a locally polyhedral cone in the half space that contains $C _ { + }$ and has $v _ { \sigma }$ in its boundary.

Proof.
The first assertion follows from the fact that $v _ { \gamma \sigma } = \gamma ( v _ { \sigma } )$ for all $\gamma \in \Gamma$

If $\sigma$ is a rational cone, then the $\Gamma$ -stabilizer of $v _ { \sigma }$ must be finite.
Since $v _ { \sigma } \in L ( \mathbb { Q } )$ and $\mathrm { d i m } ( L ) > 2$ , this can only be if $v _ { \sigma } \cdot v _ { \sigma } > 0$ .

Assume now that $\sigma$ is not a rational cone.
We first show that there exists a rational cone $\pi \subset \sigma$ such that $\Gamma _ { \sigma } . \pi = \sigma$ .
By reduction theory there exists a rational cone $\mathrm { ~ \bf ~ I ~ I ~ } \subset \mathrm { ~ \cal { C } _ { + } ~ }$ such that $\Gamma _ { \sigma } . \Pi = C _ { + }$ .
We know that the decomposition $\Sigma ( \mathcal { H } ) | _ { \Pi }$ is finite.
For every piece $P$ of this decomposition that lies in $\Gamma . \sigma$ we choose a $\gamma _ { P } \in \Gamma$ such that $\gamma _ { P } P \subset \sigma$ .
If we take for $\pi \subset \sigma$ the cone spanned by the finitely many rational cones $\gamma _ { P } P$ thus found, then $\pi$ is as desired.

Let $\tau$ be any (one-dimensional) isotropic edge of $\pi$ .
If $\tau$ is an intersection of members of the arrangement, then it is also an intersection of finitely many supporting hyperplanes of $\sigma$ .
If all isotropic edges of $\pi$ are of this form, then the same must be true for all edges of $\sigma$ and so the projectivization of $\sigma$ is a convex locally polyhedral subset of the projective space of $L$ .
But such a subset is in fact a finite polyhedron, and this contradicts our assumption that $\sigma$ is not a rational cone.

So there exists an isotropic edge $\tau$ that is not an intersection of members of the arrangement.
According to Corollary 3.6, $\tau$ is then not contained in any member of the arrangement.
This implies that $\sigma$ is invariant under $\Gamma _ { \tau }$ .
The fixed point subspace of $\Gamma _ { \tau }$ in $L$ is equal to the span of $\tau$ , and so both (iii-a) and (iii-b) follow.
This shows in particular that $\tau$ is unique and that $\Gamma _ { \sigma } = \Gamma _ { \tau }$ .
Assertion (iii-c) the follows from the fact that $\Gamma _ { \tau }$ contains a free abelian subgroup of finite index of rank $\mathrm { d i m } ( L ) - 2$ .
Now let $\pi ^ { \prime }$ be the intersection of $\sigma$ and the half spaces whose bounding hyperplane supports $\pi$ and contains $\tau$ .
Clearly, $\pi$ is then a neighborhood of $\tau$ in $\pi ^ { \prime }$ and $\Gamma _ { \sigma } \pi ^ { \prime } = \sigma$ .
Since the projectivization of $\pi ^ { \prime }$ is convex and locally polyhedral in the projective space of $L$ , $\pi ^ { \prime }$ is a rational cone.
This implies assertion (iii-d).

The two preceding propositions are related to work of Gritsenko and Nikulin.
For this we assume that $\tilde { \mathcal { H } }$ is a reflection arrangement in the sense that each member is the fixed point hyperplane of a (real) reflection contained in $\bar { \Gamma }$ .
Since $\ddot { \mathcal { H } }$ is $\tilde { \Gamma }$ -invariant, the subgroup $\tilde { W }$ of $\tilde { \Gamma }$ generated by these reflections is normal in $\tilde { \Gamma }$ .
Then the image $W$ of $\tilde { W }$ in $\Gamma$ is generated by the $\mathcal { H }$ -reflections and is normal in $\Gamma$ .
It is well-known that the latter is a Coxeter group which permutes the chambers simply transitively.
Now part (i) of their Arithmetic Mirror Symmetry Conjecture 2.2.4 in [10] follows from assertions (ii) and (iii-d) of Proposition 5.10. The triple $( V ( \mathbb { Q } ) , \Gamma , W )$ is almost the same thing as what Gritsenko and Nikulin call a reflective hyperbolic lattice (Definition (1.5.1) of [11]).
They observe (Proposition (1.5.2) of op.
cit.) that there are only finitely many isomorphism types of these in dimension $> 2$ .
They can be enumerated, at least in principle, and this leads to a classication of what they call Lorentzian Kac-Moody algebras.

We conclude this section by mentioning the following consequence of Proposition 5.8 (the proof of which we omit):

Proposition 5.11. When the arrangement is reflective in the above sense, then the closure of $D$ in $Z ^ { b b }$ supports an effective Cartier divisor if and only if we can assign in a $\Gamma$ -equivariant manner to each chamber $o$ a nonzero vector $v _ { \sigma } \in \sigma \cap L ( \mathbb { Q } )$ which does not lie in any member of $\mathcal { H }$ .

Example 5.12. A beautiful (and now classical) example to which these results apply is due to Conway (Chapter 27 of [9]) and Borcherds [5] respectively: take for $L ( \mathbb { Z } )$ any even unimodular lattice of signature $( 1 , 2 5 )$ (there is only one isomorphism class of these), let $\mathcal { H }$ be the collection of all hyperplanes perpendicular to the $\left( - 2 \right)$ - vectors in $L ( \mathbb { Z } )$ , $C \subset L ( \mathbb { R } )$ one of the two cones and let $\Gamma$ be the subgroup of the orthogonal group of $L ( \mathbb { Z } )$ which preserves $C$ .
Since the direct sum of the Leech lattice (with a minus sign) and a hyperbolic lattice is even unimodular of signature $( 1 , 2 5 )$ , it follows that there exists a primitive isotropic vector $v \in L ( \mathbb { Z } )$ in the closure of the positive cone such that $v ^ { \perp } / \mathbb { Z } v$ is isomorphic to (minus) the Leech lattice.
It also follows that such vectors make up a $\Gamma$ -orbit.
Let us fix such a $\boldsymbol { v }$ .
Clearly, $\boldsymbol { v }$ is not in any reflection hyperplane.
It is easy to see that $\Gamma _ { v }$ maps isomorphically onto the group of affine-linear isometries of $v ^ { \perp } / \mathbb { Z } v$ .
One verifies that if $u$ is a primitive isotropic vector not in $\Gamma v$ , then the $\left( - 2 \right)$ -vectors in $u ^ { \perp } / \mathbb { Z } u$ span a sublattice of finite index. So if $\sigma$ is the unique chamber that contains $v$ , then $v$ is a Weyl vector, by Proposition 5.11. We can therefore write down a $\Gamma$ -invariant infinite product expansion (Borcherds’ denominator formula) which defines the discriminant $D$ .

# 6. Semi-toric compactification of type IV domains

We return to the situation of Section 2.

Definition 6.1. We say that a $\Gamma$ -invariant collection $\Sigma$ of cones in the faces of the conical locus of $\mathbb { D }$ is an admissible decomposition of the conical locus if

(i) for every $\mathbb { Q }$ -isotropic line $I$ , the members of $\Sigma$ contained in $C _ { I , + }$ define a locally rational decomposition of $C _ { I , + }$ and  
(ii) if $J$ is a $\mathbb { Q }$ -isotropic plane (so that the cone $C _ { J , + } = C _ { J }$ in $\wedge ^ { 2 } J$ is member of $\Sigma$ ) and $I$ is any $\mathbb { Q }$ -isotropic line in $J$ (so that $J / I$ is a $\mathbb { Q }$ -isotropic line in $I ^ { \perp } / I$ ), then the support space of $C _ { J , + }$ in $I ^ { \perp } / I \otimes I$ relative to the decomposition $\Sigma | C _ { I , + }$ (see 4.5) is independent of $I$ when we regard that support space as a subspace of $J ^ { \perp }$ containing $J$

and we then define for any $\sigma \in \Sigma$ its $\Sigma$ -support space $V _ { \sigma } \subset V$ as follows:

(i) if $\sigma$ lies in $C _ { I , + }$ for some $\mathbb { Q }$ -isotropic line $I$ , but is not an isotropic half-line in $C _ { I , + }$ , then $V _ { \sigma }$ is the subspace of $I ^ { \perp }$ containing $I$ corresponding to the complex-linear span of $\sigma$ ,  
(ii) if $\sigma = C _ { J , + }$ for some $\mathbb { Q }$ -isotropic plane, then $V _ { \sigma }$ is the subspace of $J ^ { \perp }$ containing $J$ as defined by condition (ii) above.

There is a slight ambiguity of notation in case (ii), for then $V _ { \sigma }$ not only depends on $o$ (or equivalently, $J$ ), but also on $\Sigma$ .
We therefore sometimes write $J _ { \Sigma }$ for this space instead.
The isotropic center $I ( \sigma )$ of $\sigma$ is the subspace $V _ { \sigma } \cap V _ { \sigma } ^ { \perp }$ of $V _ { \sigma }$ .

Example 6.2. The simplest example is the decomposition of the conical locus into its faces.
The support spaces are $\{ 0 \}$ and the orthogonal complements of the nontrivial $\mathbb { Q }$ -isotropic subspaces.
We will see that this decomposition gives rise to the Baily-Borel compactification and so we call it the Baily-Borel decomposition.

Example 6.3. Suppose we are given for every $\mathbb { Q }$ -isotropic plane $J$ a positive rational generator $r _ { J } \in \land ^ { 2 } J ( \mathbb { Q } )$ such that this assignment is $\Gamma$ -equivariant.
Fix for the moment a $\mathbb { Q }$ -isotropic line $I$ .
For any $\mathbb { Q }$ -isotropic plane $J \supset I$ , $r _ { J }$ can be regarded as an isotropic vector in $( C _ { I } ) _ { + }$ via the inclusion $\wedge ^ { 2 } J \subset I \otimes I ^ { \perp } / I$ .
The bounded faces of the convex hull of these isotropic vectors are convex hulls of finite sets of such vectors.
The cones over these define a decomposition $\Sigma _ { I }$ of $( C _ { I } ) _ { + }$ into rational cones.
The union $\Sigma : = \cup _ { I } \Sigma _ { I }$ is an admissible decomposition of the conical locus into rational cones.
It has the property that for every $\mathbb { Q }$ -isotropic plane $J$ we have $J _ { \Sigma } = J$ .

Notice that there is a natural choice for the assignment $J \mapsto r _ { J }$ if we are given a $\Gamma$ -invariant lattice $V ( \mathbb { Z } ) \subset V ( \mathbb { Q } )$ : just take $r _ { J }$ to be the positive generator of $\wedge ^ { 2 } J ( \mathbb { Z } )$ .

We can also do a dual construction by taking instead for $\Sigma _ { I }$ the coarsest decomposition of $C _ { + }$ which is closed under taking faces and is such that $\mathrm { i n f } _ { J \supset I } \phi ( - , r _ { J } )$ is linear on each member.
Then $\Sigma _ { I }$ is only a locally rational decomposition of $( C _ { I } ) _ { + }$ .
The union $\Sigma : = \cup _ { I } \Sigma _ { I }$ is admissible as before, and now we have $J _ { \Sigma } = J ^ { \perp }$ for every $\mathbb { Q }$ -isotropic plane $J$ .

Example 6.4 (Admissible decompositions from arrangements).
Our main example of interest is the one that arises from an arithmetic arrangement on $\mathbb { D }$ .
First note that every hyperplane $H \subset V$ defined over $\mathbb { R }$ of signature $( 2 , n - 1 )$ gives a nonempty hyperplane section $\mathbb { D } _ { H } : = \mathbb { P } ( H ) \cap \mathbb { D }$ of $\mathbb { D }$ .
This is a symmetric domain for its $G$ -stabilizer and a totally geodesic hypersurface of $\mathbb { D }$ .
Now let $H$ run over a finite union $\mathcal { H }$ of $\Gamma$ -orbits in the Grassmannian of $\mathbb { Q }$ -hyperplanes of $V$ of signature $( 2 , n - 1 )$ .
Then the corresponding collection of totally geodesic hypersurfaces $\mathcal { H } _ { | \mathbb { D } } : = \{ \mathbb { D } _ { H } \} _ { H \in \mathcal { H } }$ is locally finite on $\mathbb { D }$ .
For a $\mathbb { Q }$ -isotropic line $I$ in $V$ , the $H \in \mathcal { H }$ containing $I$ correspond to $\mathbb { Q }$ -hyperplanes in $I ^ { \perp } / I \otimes I$ of signature $( 1 , n - 2 )$ and so according to example 4.3-b these decompose $C _ { I , + }$ into locally rational cones.
It follows from this and Example 4.3-b that conditions $( i )$ and $( i i )$ of Definition 6.1 are satisfied: the space $J _ { \mathcal { H } }$ associated to a $\mathbb { Q }$ -isotropic plane $J$ is the common intersection of $J ^ { \perp }$ and the hyperplanes $H \in \mathcal { H }$ containing $J$ .
We denote this admissible partition by $\Sigma ( \mathcal { H } )$ .

Notice that for empty $\mathcal { H }$ , we recover the Baily-Borel decomposition.

Fix an admissible $\Gamma$ -invariant decomposition $\Sigma$ of the conical locus of $\mathbb { D }$ .
We shall see that this determines a compactification of $X = \Gamma \backslash \mathbb { D }$ .
We first introduce some notation.

Notation 6.5. We abbreviate $\pi _ { V _ { \sigma } }$ (which we recall, stands for the projections $V $ $V / V _ { \sigma }$ and $\mathbb { P } ( V ) - \mathbb { P } ( V _ { \sigma } ) \to \mathbb { P } ( V / V _ { \sigma } ) )$ by $\pi _ { \sigma }$ .
We denote the $\Gamma$ -stabilizer of $\sigma$ by $\Gamma _ { \sigma }$ and by $\Gamma ^ { \sigma }$ the subgroup of $\Gamma _ { \sigma }$ that acts trivially on $V / V _ { \sigma }$ .
The group of real orthogonal transformations of $V$ which leave $\sigma$ pointwise fixed and act as the identity on $V _ { \sigma } / \langle \sigma \rangle _ { \mathbb { C } }$ and $V / V _ { \sigma }$ is denoted $N _ { \sigma }$ .

So $N _ { \sigma }$ is a subgroup of $N _ { I ( \sigma ) }$ , the group of real orthogonal transformations of $V$ which act as the identity on $I ( \sigma )$ , $I ( \sigma ) ^ { \bot } / I ( \sigma )$ and (hence) $V / I ( \sigma ) ^ { \perp }$ .
To be concrete, if $I = I ( \sigma )$ is a line, then $N _ { \sigma }$ is the subgroup of $N _ { I }$ that is the image of $I \otimes V _ { \sigma } / I ) ( \mathbb { R } )$ under the exponential map; if it is a plane, then $N _ { \sigma }$ is a Heisenberg subgroup of $N _ { I }$ that modulo its center is the image of $( I \otimes V _ { \sigma } / I ) ( \mathbb { R } )$ under the exponential map.
We have $N _ { \{ 0 \} } = \{ 1 \}$ , of course.

Observe that $N _ { \sigma } \exp ( { \sqrt { - 1 } \sigma } )$ is a semisubgroup of $\mathrm { O } ( \phi )$ which leaves each fiber of $\lVert \mathbb { D } \to \pi _ { \sigma } \rVert )$ invariant.
(In fact, it is not difficult to verify that every such fiber is an orbit of the semigroup that we get if we replace in the definition $\sigma$ by its relative interior.)

We form the disjoint union

$$
\mathbb { D } ^ { \Sigma } : = \coprod _ { \sigma \in \Sigma } \pi _ { \sigma } \mathbb { D }
$$

and define a topology on it as follows.
For a subset $K \subset \mathbb { D }$ and $\sigma \in \Sigma$ we define its $( \Gamma , \sigma )$ -saturation in $\mathbb { D } ^ { \Sigma }$ by

$$
K ^ { \Sigma } ( \Gamma , \sigma ) : = \prod _ { \tau \in \Sigma , \tau \leq \sigma } \pi _ { \tau } ( \Gamma ^ { \sigma } N _ { \sigma } \exp ( \sqrt { - 1 } \sigma ) K ) .
$$

These saturated subsets form the basis of a topology if $K$ runs over the open subsets of $\mathbb { D }$ and $\sigma$ over $\Sigma$ .
We regard $\mathbb { D } ^ { \Sigma }$ as a ringed space in the usual way: it comes equipped with the sheaf of complex valued, continuous, piecewise analytic functions.
Similarly for $( \mathbb { L } ^ { \times } ) ^ { \Sigma } : = \sqcup _ { \sigma \in \Sigma } \pi _ { \sigma } \mathbb { L } ^ { \times }$ .
It is clear that in either case $\Gamma$ acts as a group of homeomorphisms.
We put $X ^ { \Sigma } : = \Gamma \backslash \mathbb { D } ^ { \Sigma }$ (as a ringed space).
The image of $\pi _ { \sigma } \underline { { \| } } )$ is the orbit space of the latter by the group $\Gamma ( \sigma ) : = \Gamma _ { \sigma } / \Gamma ^ { \sigma }$ ; we denote this orbit space by $X ( \sigma )$ .
This is an algebraic torus when $\dim I ( \sigma ) = 1$ and the total space of a bundle of abelian varieties over a modular curve when $\dim I ( \sigma ) = 2$ .

Notice that we recover the Baily-Borel extensions $\mathbb { D } ^ { b b }$ and $X ^ { b b }$ as topological spaces if we take for $\Sigma$ the coarsest admissible decomposition.
We shall see that as in the Baily-Borel case, $X ^ { \Sigma }$ is a normal analytic space.

The proof of the following lemma is straightforward.

Lemma 6.6. Let $\Sigma ^ { \prime }$ be a $\Gamma$ -invariant admissible decomposition of the conical locus that is refined by $\Sigma$ .
Given $\sigma \in \Sigma$ , let $\sigma ^ { \prime }$ be the smallest member of $\Sigma ^ { \prime }$ that contains $\sigma$ .
Then $V _ { \sigma } \subset V _ { \sigma ^ { \prime } }$ , so that we have a factorization of $\mathbb { D }  \pi _ { \sigma ^ { \prime } } \mathbb { D }$ over $\pi _ { \sigma } \underline { { \| } } )$ .
The disjoint union of the maps $\pi _ { \sigma } \mathbb { D } \to \pi _ { \sigma ^ { \prime } } \mathbb { D }$ over all members $\sigma \in \Sigma$ defines a continuous, $\Gamma$ -equivariant morphism of ringed spaces $\mathbb { D } ^ { \Sigma } \to \mathbb { D } ^ { \Sigma ^ { \prime } }$ .
In particular we have $a$ morphism of ringed spaces $X ^ { \Sigma }  X ^ { \Sigma ^ { \prime } }$ .
Likewise for $( \mathbb { L } ^ { \times } ) ^ { \Sigma } \to ( \mathbb { L } ^ { \times } ) ^ { \Sigma ^ { \prime } }$ .

This applies in particular to the case when $\Sigma ^ { \prime }$ is the Baily-Borel decomposition so that we always have a map XΣ → Xbb.

Theorem 6.7. The ringed space $X ^ { \Sigma }$ is a normal analytic space.
The pull-back of the automorphic $\mathbb { C } ^ { \times }$ -bundle on $X ^ { b b }$ to $X ^ { \Sigma }$ can be identified with $( \Gamma \backslash \mathbb { L } ^ { \times } ) ^ { \Sigma }$ .

Proof.
We need to verify this over a neighborhood of any boundary stratum $X ( I ^ { \perp } )$ of $X ^ { b b }$ .
According to the discussion in 2.5 this then becomes an issue on the level of a Baily-Borel extension $\Gamma ^ { I } \backslash S t a r ( \pi _ { V ^ { I } } \mathbb { D } )$ .
The two cases (corresponding to $\dim I = 2$ and $\dim I = 1$ ) are then covered by Section 3 and Proposition 4.6. The last assertion is easy.
□

# 7. Arrangements on a type IV domain

We now assume given a $\Gamma$ -invariant arithmetic arrangement $\mathcal { H }$ in $V$ as in Example 4.3-b. We write

$$
\mathbb { D } ^ { \circ } : = \mathbb { D } - \cup _ { H \in \mathcal { H } } \mathbb { D } _ { H } \mathrm { ~ a n d ~ } X ^ { \circ } : = \Gamma \backslash \mathbb { D } ^ { \circ }
$$

for the arrangement complement and its orbit space respectively.
We shall describe a compactification of $X ^ { \circ }$ that is similar to what we did in [16] for the ball quotient case.
We noted in Example 6.4 that $\mathcal { H }$ defines an admissible partition $\Sigma ( \mathcal { H } )$ of the conical locus.
Any $H \in { \mathcal { H } }$ defines a hypersurface $X _ { H }$ in $X$ which only depends on the image of $H$ in $\Gamma \backslash \mathcal { H }$ .
This collection hypersurfaces is finite.
We also regard $X _ { H }$ $X _ { H } ^ { \Sigma ( \mathcal { H } ) }$ as a Weil divisor .
$X _ { H }$ on $X ^ { b b }$ and we denote its strict transform in $X ^ { \Sigma ( \mathcal { H } ) }$ by

Analogous to the proof of Lemma (5.1) of [16] one establishes:

Lemma 7.1. After passing to a subgroup of Γ of finite index, each hypersurface $X _ { H }$ is without self-intersection in the sense that its normalization is a homeomorphism that is an isomorphism over $X _ { H }$ .

From now on we assume that we have made this passage, so that each $X _ { H }$ is without self-intersection.

A linear subspace $L$ of $V$ contains a vector $z$ with $\phi ( z , z ) > 0$ if and only if $\mathbb { P } ( L )$ meets $\mathbb { D }$ .
In that case $\mathbb { D } _ { L } : = \mathbb { D } \cap \mathbb { P } ( L )$ is totally geodesic in $\mathbb { D }$ and is the bounded symmetric domain for its group of complex-analytic automorphisms.
If moreover $L$ is defined over $\mathbb { Q }$ , then the $\Gamma$ -stabilizer acts as an arithmetic group on $L$ and the closure of $\mathbb { D } _ { L }$ in $\mathbb { D } ^ { b b }$ is just the Baily-Borel extension of $\mathbb { D } _ { L }$ and hence we denote that closure $\mathbb { D } _ { L } ^ { b b }$ .
It is not hard to see that a similar property holds for the closure $\mathbb { D } _ { L }$ in $\mathbb { D } _ { L } ^ { \Sigma ( \mathcal { H } ) }$ : is it the extension defined by the restriction of $\mathcal { H }$ to $L$ ; we denote that closure by $\mathbb { D } _ { L } ^ { \Sigma ( \mathcal { H } ) }$ .

Let $\mathrm { P O } ( \mathcal { H } _ { | \mathbb { D } } )$ denote the collection intersections $L$ from members of $\mathcal { H }$ which have the above property, i.e., which contain a vector $z$ with $\phi ( z , z ) > 0$ .
For an $L$ o f this type, the image $X _ { L }$ of $\mathbb { D } _ { L }$ in $X$ depends only on the image of $L$ in $\Gamma \backslash \mathrm { P O } ( \mathcal { H } _ { | \mathbb { D } } )$ .
It is a connected component of intersections of members of the arrangement $\Gamma \backslash \mathcal { H }$ resp.
(and each such component occurs once and only once).
The closure of $X ^ { \Sigma ( \mathcal { H } ) }$ is the image of $\mathbb { D } _ { L } ^ { b b }$ resp.
$\mathbb { D } _ { L } ^ { \Sigma ( \mathcal { H } ) }$ and denoted $X _ { L }$ resp.
$X _ { L } ^ { \Sigma ( \mathcal { H } ) }$ $X _ { L }$ in $X ^ { b b }$

Proposition 7.2. The closure $X _ { H } ^ { \Sigma ( \mathcal { H } ) }$ of the hypersurface $X _ { H }$ in $X ^ { \Sigma ( \mathcal { H } ) }$ supports an effective Cartier divisor and the collection of these Cartier divisors is an arrangement on $X ^ { \Sigma ( \mathcal { H } ) }$ linearized by $\mathcal { L }$ .
If no one-dimensional intersection from $\mathcal { H }$ is positive semidefinite, then $X ^ { \Sigma ( \mathcal { H } ) } \to X ^ { b b }$ is the normalized blowup of the reduced sum of these Cartier divisors.

Proof.
That closure of $X _ { H }$ in $X ^ { \Sigma ( \mathcal { H } ) }$ is Cartier follows from Lemma’s 3.2 and 5.1. The condition that no one-dimensional intersection from $\mathcal { H }$ is positive semidefinite amounts to the nonoccurence in $X ^ { \Sigma ( \mathcal { H } ) }$ of strata of codimension one.
So the last assertion follows form Corollaries 3.3 and Corollary5.5.

As for what remains, let $H \in \mathcal { H }$ be defined by the $\mathbb { Q }$ -linear form $f : V \to \mathbb { C }$ .
We regard $f$ as an object on $\mathbb { D }$ in a standard manner, namely as a section of $\mathbb { L } ^ { - 1 }$ with divisor $\mathbb { D } _ { H }$ .
This section is clearly equivariant with respect to the action of the $G$ - stabilizer $G _ { f }$ of $F$ .
It extends across the union of the strata of $\mathbb { D } ^ { \Sigma ( \mathcal { H } ) }$ that are of the form $\pi _ { W } \mathbb { D }$ , where $W$ is a linear subspace of $H$ (simply because $f$ factors through $V / W$ in that case).
The union of these strata is open and makes up a neighborhood of the closure $\mathbb { D } _ { H } ^ { \Sigma ( \mathcal { H } ) }$ of $\mathbb { D } _ { H }$ in $\mathbb { D } ^ { \Sigma ( \mathcal { H } ) }$ .
The extension in question is still $G _ { f }$ -invariant and has DΣ(H as ‘divisor’.
This drops and restricts to a generating section of the coherent restriction of $\displaystyle { \mathcal { L } } ^ { - 1 } \bigl ( - X _ { H } \bigr )$ to $X _ { H } ^ { \Sigma ( \mathcal { H } ) }$ .
□

Proposition 7.3. Given $H \in \mathcal { H }$ , then the sheaf $\mathcal { L } ^ { \otimes k } ( k X _ { H } ^ { \Sigma ( \mathcal { H } ) } )$ on $X ^ { \Sigma ( \mathcal { H } ) }$ is generated by its sections when $k$ is large enough.

Proof.
Let $v _ { 0 } \in V ( \mathbb { Q } )$ be perpendicular to $H$ and denote by $\boldsymbol { \mathcal { O } }$ the $\Gamma$ -orbit of $v _ { 0 }$ .
We claim that for $k \geq n + 2$ , the series

$$
F ^ { ( k ) } ( z ) : = \sum _ { v \in \mathcal { O } } \phi ( z , v ) ^ { - k }
$$

represents a $\Gamma$ -invariant meromorphic section of $\mathbb { L } ^ { \otimes k }$ .
To see this, let $K \subset \mathbb { L } ^ { \times }$ be compact.
Denote by $Y$ the hypersurface in $V ( \mathbb { R } )$ defined by $\phi ( x , x ) = \phi ( v , v )$ .
It has real dimension $n + 1$ .
The $\Gamma$ -orbit $\boldsymbol { \mathcal { O } }$ generates a lattice in $V ( \mathbb { Q } )$ .
The number $A ( N )$ of points $w$ of this lattice for which $\mathrm { m i n } _ { z \in \cal K } | \phi ( z , w ) |$ lies in the interval $[ t - 1 , t ]$ is for large $N$ proportional to the $( n + 1 )$ -dimensional volume of the corresponding subset of $Y$ .
So $A ( t )$ is bounded by a polynomial of degree $n$ in $t$ .
We find that in the series only finitely many terms have a pole on $K$ whereas the sum over the absolute values of the other terms is bounded by a constant plus $\begin{array} { r } { \sum _ { t \geq 2 } A ( t ) ( t - 1 ) ^ { - k } } \end{array}$ .
This converges since $k \geq n + 2$ .
We extend $F ^ { ( k ) }$ meromorphically over $( \mathbb { L } ^ { \times } ) ^ { \Sigma ( \mathcal { H } ) }$ by letting its restriction to $\pi _ { V _ { I } } { \mathbb { L } } ^ { \times }$ b e

$$
\pi _ { V _ { I } } ( z ) \in \pi _ { V _ { I } } \mathbb { L } ^ { \times } \mapsto \sum _ { v \in \mathcal { O } \cap I ^ { \perp } } \phi ( z , v ) ^ { - k } .
$$

A mition of the arguments used in ths extension indeed defines of of Letion of $\mathcal { L } ^ { \otimes k } ( k X _ { H } ^ { \Sigma ( \mathcal { H } ) } )$ Proposi-.
Notice $\pi _ { V _ { I } } ( z _ { o } ) \in \pi _ { V _ { I } } \mathbb { L } ^ { \times }$ $F ^ { ( k ) }$  
$v \in \mathcal { O } \cap I ^ { \perp }$ with $\phi ( z _ { o } , v ) = 0$ .
This $\boldsymbol { v }$ is the unique (since we assumed $X _ { H }$ to be  
without selfintersection) and the polar part of $F ^ { ( k ) } | \pi _ { V _ { I } } \mathbb { D }$ at $\pi _ { V _ { I } } ( z _ { o } ) \in \pi _ { V _ { I } } \mathbb { L } ^ { \times }$ is the  
single term $\phi ( z , v ) ^ { - k }$ .

It is well-known that for $k$ large enough, $\mathcal { L } ^ { \otimes k }$ is generated by its sections (in fact the same construction—but now with $\phi ( v _ { o } , v _ { o } ) \ \leq \ 0$ —produces enough of these).
The proposition follows.

Let $\widetilde { X ^ { \circ } }  X ^ { \Sigma ( \mathcal { H } ) }$ the blowup of the arrangement defined by $\mathcal { H }$ in the sense of [16].
This means that we blow up successively the connected components of intersections of members of the arrangement, in the order of increasing dimension.
We prefer to obtain this as the $\Gamma$ -orbit space of a similar construction on $\mathbb { D } ^ { \Sigma ( \mathcal { H } ) }$ : $\widetilde { \mathbb { D } ^ { \circ } }  \mathbb { D } ^ { \Sigma ( \mathcal { H } ) }$ is the successive blowup of the submanifolds $\mathbb { D } _ { L } ^ { \Sigma ( \mathcal { H } ) }$ .

We denote the exceptional hypersurface associated to $L \in \mathrm { P O } ( \mathcal { H } _ { | \mathbb { D } } )$ by $E ( L ) \subset$ ${ \overline { { \mathbb { D } ^ { \circ } } } }$ .
The linearization defines a projection $E ( L ) \to \mathbb { P } ( V / L )$ .
The members of $\mathcal { H }$ that contain $L$ are finite in number and define an arrangement on $\mathbb { P } ( V / L )$ .
The arrangement complement in the latter is denoted $\mathbb { P } ( V / L ) ^ { \circ }$ .
The preimage $E ( L ) ^ { \circ }$ of this arrangement complement in $E ( L )$ is naturally a product: $L \times \mathbb { P } ( V / L ) ^ { \circ }$ and so we have a projection $E ( L ) ^ { \circ } \to \mathbb { P } ( V / L ) ^ { \circ } = \pi _ { L } \mathbb { D } ^ { \circ }$ .

The hypersurfaces indexed by a subset of $\mathrm { P O } ( \mathcal { H } _ { | \mathbb { D } } )$ have a nonempty common intersection if and only if that subset is linearly ordered, i.e., of the form $L _ { 0 } ~ \subset$ $L _ { 1 } \subset \cdots \subset L _ { r }$ .
The corresponding intersection $E ( L _ { 0 } , \ldots , L _ { r } ) = \cap _ { i } E ( L _ { i } )$ is the closure of a stratum that we will denote by $E ( L _ { 0 } , \ldots , L _ { r } ) ^ { \circ }$ .
Now ${ \overline { { \mathbb { D } ^ { \circ } } } }$ is the disjoint union of the arrangement complement $( \mathbb { D } ^ { \Sigma ( \mathcal { H } ) } ) ^ { \circ }$ and the collection $E ( L _ { \bullet } ) ^ { \circ }$ , where $L _ { \bullet }$ runs over the nonempty linearly ordered subsets of $\mathrm { P O } ( \mathcal { H } _ { | \mathbb { D } } )$ .
A quotient set $\widehat { \mathbb { D } ^ { \circ } }$ of $\widetilde { \mathbb { D } ^ { \circ } }$ is defined by the disjoint union of $( \mathbb { D } ^ { \Sigma ( \mathcal { H } ) } ) _ { - } ^ { \circ }$ and the projective arrangement complements $\mathbb { P } ( V / L ) ^ { \circ }$ with the quotient map $\widetilde { \mathbb { D } ^ { \circ } } \to \widehat { \mathbb { D } ^ { \circ } }$ being the union of the identity on $( \mathbb { D } ^ { \Sigma ( \mathcal { H } ) } ) ^ { \circ }$ and the projections $E ( L ) ^ { \circ } \to \mathbb { P } ( V / L ) ^ { \circ }$ .
We give $\widehat { \mathbb { D } ^ { \circ } }$ the quotient topology.
Let us see what happens over a boundary component.

A $\mathbb { Q }$ -isotropic plane $J$ defines the stratum $\pi _ { J ^ { \mathcal { H } } } \mathbb { D }$ of $\mathbb { D } ^ { \Sigma ( \mathcal { H } ) }$ , where we recall that $J ^ { \mathcal { H } }$ is the intersection of $J ^ { \perp }$ with all the members of $\mathcal { H }$ that contain $J$ .
The subset $\mathcal { H } ^ { J }$ of $\mathcal { H }$ defined by this last condition defines an arrangement in $\pi _ { J ^ { \mathcal { H } } } \mathbb { D }$ .
This arrangement is blown up and then blown down in the manner we described earlier.
The arrangement complement is clearly unaffected by this and so appears in $\widehat { \mathbb { D } ^ { \circ } }$ ; it is just $\pi _ { J ^ { \mathcal { H } } } \mathbb { D } ^ { \cup }$ .
The total transform of the arrangement on $\pi _ { J ^ { \mathcal { H } } } \mathbb { D }$ is already accounted for, at least in $\widehat { \mathbb { D } ^ { \circ } }$ , since it will map to the union of the strata $\pi _ { L } \mathbb { D } ^ { \circ }$ .

When $I$ is a $\mathbb { Q }$ -isotropic line, then the collection $\mathcal { H } ^ { I }$ of members of $\mathcal { H }$ containing $I$ define an arrangement on $\| \mathcal { D } \cong \pi _ { I } \mathbb { D }$ .
The latter yields a semitoric embedding.
A stratum of this torus embedding that does not come from an isotropic plane is defined by a $\sigma \in \Sigma$ which meets $C _ { I }$ .
In that case $\pi _ { \sigma } \underline { { \| \partial } } = \pi _ { V _ { \sigma } } \underline { { \| \partial } }$ , where $V _ { \sigma }$ is the common intersection of $I ^ { \perp }$ and the members of $\mathcal { H }$ that contain $I$ .
We conclude that

$$
\widehat { \mathbb { D } ^ { \circ } } = \mathbb { D } ^ { \circ } \sqcup \prod _ { L \in \mathrm { P O } ( \mathcal { H } _ { \mid \mathbb { D } } ) } \pi _ { L } \mathbb { D } ^ { \circ } \sqcup \prod _ { \sigma \in \Sigma ( \mathcal { H } ) } \pi _ { V _ { \sigma } } \mathbb { D } ^ { \circ } .
$$

In this disjoint union we may have repetitions: this happens for instance if two distinct members of $\Sigma$ which meet $C _ { I }$ have the same linear span.
Since $\mathbb { D } ^ { \circ }$ is open and dense in $\widehat { \mathbb { D } ^ { \circ } }$ , we regard the latter as an extension of the former.
If we pass to the $\Gamma$ -orbit space, then

$$
{ \widehat { X ^ { \circ } } } : = \Gamma \backslash { \widehat { \mathbb { D } ^ { \circ } } }
$$

is a compactification of $X ^ { \circ }$ whose boundary is decomposed into finitely many strata.
Each boundary stratum has the structure of an arrangement complement, which can be of projective type, of relative abelian type (over a modular curve) or of toric type.

As in part I [16], the $k$ -th power of a fractional ideal $\mathcal { L }$ on a variety $Y$ (where $k$ is a positive integer), denoted $\mathcal { T } ^ { ( k ) }$ , is the image of $\mathcal { T } ^ { \otimes k }$ in the sheaf of rational functions on $Y$ and hence itself a fractional ideal.
We put

$$
\mathcal { L } ( \mathcal { H } ) : = \sum _ { H \in \Gamma \backslash \mathcal { H } } \mathcal { L } _ { X ^ { \Sigma ( \mathcal { H } ) } } ( X _ { H } ^ { \Sigma ( \mathcal { H } ) } ) .
$$

Since the arrangement on $X ^ { \Sigma ( \mathcal { H } ) }$ is linearized by $\mathcal { L }$ , the coherent pull-back of $\mathcal { L } ( \mathcal { H } )$ to $\widetilde { X ^ { \circ } }$ is an orbiline bundle which is constant along the fibers of the map $\widetilde { X ^ { \circ } }  \widehat { X ^ { \circ } }$ .

Theorem 7.4. The coherent pull-back of $\mathcal { L } ( \mathcal { H } )$ to $\widetilde { X ^ { \circ } }$ is a semi-ample line bundle which defines the contraction $\widetilde { X ^ { \circ } }  \widehat { X ^ { \circ } }$ (by which we mean that a suitable power of this bundle defines a morphism onto a projective variety which as a topological quotient of $\widetilde { X ^ { \circ } }$ is just $\widehat { X ^ { \circ } }$ ).

Proof.
That the coherent pull-back of $\mathcal { L } ( \mathcal { H } )$ to $\widetilde { X ^ { \circ } }$ is an line bundle is a general  
property of the blowubundle by the subbun ofes ment.
Its .
Since t $k$ th power ise subbund erated as a linere generated by $\mathcal { L } ^ { \otimes k } \big ( X _ { H } ^ { \Sigma ( \mathcal { H } ) } \big )$ $k$ $\mathcal { L } ( \mathcal { H } )$  
power of $\mathcal { L } ( \mathcal { H } )$ is constant along the fibers of the map $\widetilde { X ^ { \circ } }  \widehat { X ^ { \circ } }$ .
Since $\mathcal { L }$ is ample,  
they separate these fibers.
The theorem follows.
□

Corollary 7.5. Suppose that no one-dimensional intersection of members of the arithmetic arrangement $\mathcal { H }$ in $V$ is positive semidefinite.
Then the algebra of automorphic forms

$$
\oplus _ { k \in \mathbb { Z } } H ^ { 0 } ( \mathbb { D } ^ { \circ } , { \mathcal { O } } ( \mathbb { L } ^ { k } ) ) ^ { \Gamma }
$$

(where L is the natural automorphic bundle over $\mathbb { D }$ and $\mathbb { D } ^ { \circ }$ is the arrangement complement) is finitely generated with positive degree generators and its proj is the compactification ${ \widehat { X ^ { \circ } } }$ of $X ^ { \circ }$ .
Moreover, the boundary ${ \widehat { X ^ { \circ } } } - X ^ { \circ }$ is the strict transform of the boundary $X ^ { \Sigma ( \mathcal { H } ) } - X$ .

Proof.
The assumption implies that $( X ^ { \Sigma ( \mathcal { H } ) } ) ^ { \circ } - X ^ { \circ }$ is dense in $\widehat { X ^ { \circ } } - X ^ { \circ }$ .
The last assertion then follows and for the other assertions it suffices to note that $X ^ { \Sigma ( \mathcal { H } ) } - X$ is of codimension $\geq 2$ in $X ^ { \Sigma ( \mathcal { H } ) }$ .
□

In applications pertaining to $K 3$ -surfaces, we often get the finite generation of the algebra of automorphic forms via the following theorem.
The previous corollary can then be used to interpret its proj.

Theorem 7.6. Let $Y$ be a normal projective variety with ample line bundle $\eta$ , $G$ a reductive group acting on the pair $( Y , \eta )$ and $U \subset Y$ a $G$ -invariant open-dense subset on which $G$ acts properly.
Suppose that any $G$ -invariant section of a tensor power of $\eta$ over $U$ extends across $Y$ (a condition that is certainly satisfied if $Y - U$ is of codimension $> 1$ in $Y$ ).
Let $\mathcal { H }$ be an arithmetic arrangement on a type $I V$ domain $\mathbb { D }$ relative to an arithmetic group $\Gamma$ .

Then an identification (in the analytic category) of the line bundle $G \backslash ( U , \eta | U )$ with the pair $( X ^ { \circ } , { \mathcal { L } } | X ^ { \circ } )$ associated to this arrangement gives rise to an isomorphism of $\mathbb { C }$ -algebra’s

$$
\begin{array} { r } { \oplus _ { k = 0 } ^ { \infty } H ^ { 0 } ( Y , \eta ^ { \otimes k } ) ^ { G } \cong \oplus _ { k \in \mathbb { Z } } H ^ { 0 } ( \mathbb { D } ^ { \circ } , { \mathcal { O } } ( \mathbb { L } ) ^ { \otimes k } ) ^ { \Gamma } . } \end{array}
$$

In particular, the algebra of meromorphic automorphic forms is finitely generated with positive degree generators, $U$ consists of stable $G$ -orbits, and $G \backslash \backslash Y ^ { \mathrm { s s } } \cong \widehat { X ^ { \circ } }$ .

Proof.
To say that we have an isomorphism between $H ^ { 0 } ( G \backslash U , G \backslash ( \eta ^ { \otimes k } | U ) )$ and $H ^ { 0 } ( X ^ { \circ } , { \mathcal { L } } ^ { \otimes k } )$ is saying that we have an isomorphism between $H ^ { 0 } ( U , \eta ^ { \otimes k } ) ^ { G }$ and $H ^ { 0 } ( \mathbb { D } ^ { \circ } , { \mathcal { O } } ( \mathbb { L } ) ^ { \otimes k } ) ^ { \Gamma }$ .
Since $H ^ { 0 } ( Y , \eta ^ { \otimes k } ) ^ { G } \to H ^ { 0 } ( U , \eta ^ { \otimes k } ) ^ { G }$ is an isomorphism by assumption, the assertion follows.
□

As in the ball quotient case, the identification demanded by the theorem will often come from a period mapping.
In the following sections we shall discuss a few examples related to $K 3$ -surfaces.

Borcherds described in [4] a technique that produces in a systematic fashion arithmetic arrangements that are definable by an automorphic form.
Here we note a necessary condition for this to be the case: the divisor on $X$ defined by such an arrangement must then extend across the Baily-Borel compactification $X ^ { b b }$ as a Cartier divisor.
Proposition 5.8 gives us immediately:

Theorem 7.7. Let a divisor on $X$ be defined by the Γ-invariant arrangement $\mathcal { H }$ and the $\Gamma$ -invariant function $m : \mathcal { H }  \mathbb { Z }$ .
Then the divisor has the Cartier property at the boundary if and only if for every $\mathbb { Q }$ -isotropic line $I$ there exists a quasicharacter $e ^ { \rho _ { I } } : \mathbb { P } ( V ) - \mathbb { P } ( I ^ { \perp } ) \to \mathbb { C }$ satisfying the functional equation of Proposition 5.8 relative to $\Gamma _ { I }$ and the restriction of $m$ to the arrangement defined by the collection of $H \in \mathcal { H }$ containing $I$ .

It is clear that this property needs only be tested for a system of representatives of the $\Gamma$ -orbits in the collection of $\mathbb { Q }$ -isotropic lines.
Still, it is quite a strong condition.
If it is satisfied and if the Picard group of $X ^ { b b }$ happens to have rank one, then it follows that a multiple of the corresponding divisor is defined by an automorphic form.
It would be nice to have here an analogue of Proposition 5.8.

# 8. Applications to period mappings of polarized $K 3$ -surfaces

8A.
Semiample linear systems on $K 3$ -surfaces.
We return to the moduli spaces of $K 3$ -surfaces.
Suppose $S$ is a $K 3$ -surface equipped with a primitive semiample class $h \in \operatorname { P i c } ( S )$ with $h \cdot h = 2 g - 2$ .
The linear system defined by $h$ consist of genus $g$ curves and is of dimension $g$ .
According to A.
Mayer [17], we are then in one of the following situations:

The unigonal case: the linear system maps to a rational curve.
This happens precisely when there is an elliptic curve on $S$ on which $h$ has degree 1, a condition equivalent to the existence of an isotropic class $f \in \operatorname { P i c } ( S )$ with $h \cdot f = 1$ .
The moving part of the linear system gives $S$ the structure of an elliptic surface with section.  
The digonal case: the linear system defines a morphism of degree 2 on its image (a rational surface).
This is always so when $g = 2$ (unless we are in the unigonal case, of course): then the linear system realizes $S$ as a double cover of $\mathbb { P } ^ { 2 }$ ramified along a sextic curve with simple singularities.
When $g > 2$ , this happens precisely when there is an elliptic curve on $S$ on which $h$ has degree 2, a condition equivalent to the existence of a primitive isotropic class $f \in \operatorname { P i c } ( S )$ with $h \cdot f = 2$ , again assuming we are not in the unigonal case.
The moving part of the linear system gives $S$ the structure of an elliptic surface, in general without a section.  
The nonhyperelliptic case: the linear system maps $S$ birationally onto its image.

This means that the question of whether a given pair $( S , h )$ is unigonal or digonal can be read off from its periods: Adhering to the notation in the final subsection of Section 3, consider the set $E _ { g } ^ { \prime }$ resp.
$E _ { g } ^ { \prime \prime }$ of primitive isotropic vectors $f$ in the $K 3$ -lattice $\Lambda$ with $f \cdot h _ { g } = 1$ resp.
$f \cdot h _ { g } = 2$ .
It is well-known that each of these sets is a single orbit of $\Gamma _ { g }$ .
Representative elements are $f _ { 3 }$ and $2 f _ { 3 } + f _ { 2 }$ respectively.
The span of $h _ { g } = e _ { 3 } + ( g - 1 ) f _ { 3 }$ and $f _ { 3 }$ is a hyperbolic summand $U$ , whereas the span of $h _ { g }$ and $2 f _ { 3 } + f _ { 2 }$ is isomorphic to $I ( 2 ) \perp I ( - 2 )$ or $U ( 2 )$ , depending on whether $g$ is even or odd.
These are even rank two lattices of hyperbolic signature so that their orthogonal complements have signature $( 2 , 1 8 )$ .
We notice in passing that in each case the discriminant group of the rank two lattice is 2-torsion, which implies that this lattice is the fixed point set of an involution in $\Gamma _ { g }$ .
Such an involution acts on $\mathbb { D } _ { g }$ as reflection.
So the collection $\mathcal { H } _ { g } ^ { \prime }$ resp.
$\mathcal { H } _ { g } ^ { \prime \prime }$ of hyperplanes in $\Lambda _ { g } \otimes \mathbb { C }$ perpendicular to the span of $h _ { g }$ and a vector in $E _ { g } ^ { \prime }$ resp.
$E _ { g } ^ { \prime \prime }$ make up an ‘reflection angement’ on .
Via the per $\mathbb { D } _ { g }$ .
Each of these in turn determ mapping, the generic point of s a diresp.
$D _ { g } ^ { \prime }$ resp.
rrespo $D _ { g } ^ { \prime \prime }$ in to $X _ { g }$ $D _ { g } ^ { \prime }$ $D _ { g \geq 3 } ^ { \prime \prime }$ the property of the $K 3$ -surface being unigonal resp.
digonal.
We therefore put

$$
E _ { g } : = { \left\{ \begin{array} { l l } { E _ { 2 } ^ { \prime } { \mathrm { ~ i f ~ } } g = 2 , } \\ { E _ { g } ^ { \prime } \cup E _ { g } ^ { \prime \prime } { \mathrm { ~ i f ~ } } g \geq 3 . } \end{array} \right. }
$$

We denote by $\mathcal { H } _ { g }$ the corresponding collection of hyperplanes and by $X _ { g } ^ { \circ }$ the associated arrangement complement.
We will see that for small $g$ , $\widehat { X _ { g } ^ { \circ } }$ has the interpretation of a GIT compactification.
In order to understand the strata of $X _ { g } ^ { \Sigma ( \mathcal { H } _ { g } ) }$ we need the following lemma.

Lemma 8.1. Let $M \subset \Lambda$ be a nondegenerate sublattice of signature $( 1 , r )$ with $r \geq 2$ spanned by $h _ { g }$ and elements of $E _ { g }$ .
Then $g \in \{ 3 , 4 \}$ , $M \cap E _ { g } = M \cap E _ { g } ^ { \prime \prime \prime }$ and and $v _ { 1 } \cdot v _ { 2 } = 1$ for every pair $v _ { 1 } , v _ { 2 } \in M \cap E _ { g } ^ { \prime \prime }$ which spans with $h _ { g }$ a rank 3 lattice.
In case $g = 4$ , $M$ is isometric to $U \perp I ( - 2 )$ (and so $r = 2$ ) and $M \cap E _ { g } ^ { \prime \prime }$ consists of three elements whose sum is $h _ { 4 }$ .

Proof.
Suppose $v _ { 1 } , v _ { 2 } \in M \cap E _ { g }$ are such that they form with $h _ { g }$ a linearly independent set.
Then the quadratic form on the span of $h _ { g } , v _ { 1 } , v _ { 2 }$ has in this basis the expression $( 2 g - 2 ) x ^ { 2 } + 2 a _ { 1 } x y _ { 1 } + 2 a _ { 2 } x y _ { 2 } + 2 \lambda y _ { 1 } y _ { 2 }$ , with $a _ { i } \in \{ 1 , 2 \}$ , depending on whether $v _ { i }$ is in $E _ { g } ^ { \prime }$ or $E _ { g } ^ { \prime \prime }$ .
The determinant of this quadratic form is $2 \lambda ( a _ { 1 } a _ { 2 } - ( g - 1 ) \lambda )$ .
We want it to be negative, which means that $0 ~ < ~ \lambda ~ <$ $a _ { 1 } a _ { 2 } ( g - 1 ) ^ { - 1 }$ .
As $\lambda$ is an integer, this can only be if $g - 1 \in \{ 2 , 3 \}$ , $a _ { 1 } = a _ { 2 } = 2$ and $\lambda = 1$ (recall that when $g = 2$ , we have $a _ { i } = 1$ , by assumption).
This proves the first part of the lemma.

If $v _ { 1 } , v _ { 2 } , v _ { 3 }$ are three distinct elements of $M \cap E _ { 4 } ^ { \prime \prime }$ , then the lattice spanned by the elements $v _ { 1 } , v _ { 2 } , v _ { 3 }$ is isomorphic with $U \perp I ( - 2 )$ (take as basis $( v _ { 1 } , v _ { 2 } , v _ { 3 } - v _ { 1 } - v _ { 2 } )$ and so has hyperbolic signature.
Now notice that $h _ { 4 } - v _ { 1 } - v _ { 2 } - v _ { 3 }$ is perpendicular to the sublattice $N \subset M$ spanned by $v _ { 1 } , v _ { 2 } , v _ { 3 } , h _ { 4 }$ .
Since $M$ has hyperbolic signature, this can only be if $h _ { 4 } = v _ { 1 } + v _ { 2 } + v _ { 3 }$ .
It also follows that $M \cap E _ { 4 } ^ { \prime \prime }$ cannot have more than three elements.
□

Remark 8.2. Let us briefly comment on the remaining (and quite interesting) case $g = 3$ .
If $v \in M \cap E _ { 3 } ^ { \prime \prime }$ , then its image under the orthogonal projection $\Lambda \to \Lambda _ { 3 } \otimes \mathbb { Q }$ is $\textstyle v - { \frac { 1 } { 2 } } h$ , whose double $2 v - h _ { 3 }$ is a $( - 4 )$ -vector.
Notice that $h _ { 3 } - v \in M \cap E _ { 3 } ^ { \prime \prime }$ also and that its image in $\Lambda _ { 3 } \otimes \mathbb { Q }$ is the antipode of the orthogonal projection of $v$ .
If $v ^ { \prime } \in M \cap E _ { 3 } ^ { \prime \prime }$ is distinct from $\boldsymbol { v }$ and $h _ { 3 } - v$ , then the orthogonal projections $\textstyle v - { \frac { 1 } { 2 } } h$ and $v ^ { \prime } - { \textstyle \frac { 1 } { 2 } } h _ { 3 }$ are perpendicular.
This shows that $M \cap E _ { 3 } ^ { \prime \prime }$ has exactly $2 r$ elements $v _ { 1 } , v _ { 2 } , \ldots , v _ { r } , h _ { 3 } - v _ { 1 } , \ldots , h _ { 3 } - v _ { r }$ whose orthogonal projection in $\Lambda _ { 3 } \otimes \mathbb { Q }$ is the union of an orthonormal set and its antipode.
Let us denote by $M _ { r }$ the abstract lattice defined by such a system $( h _ { 3 } , v _ { 1 } , \ldots , v _ { r } )$ and remember that $M _ { r }$ has the distinguished vector $h _ { 3 }$ .
Suppose $r \geq 3$ .
Then the elements $v _ { 1 } , v _ { 2 }$ span a copy of $U$ in $M _ { r }$ and the orthogonal complement of this copy in $M _ { r }$ has the basis $( h _ { 3 } - v _ { 1 } - v _ { 2 } - v _ { 3 } , v _ { 1 } + v _ { 2 } - v _ { 3 } , v _ { 3 } - v _ { 4 } , v _ { 4 } - v _ { 5 } , . . . , v _ { r } - v _ { r - 1 }$ , which is a root basis of type $D _ { r - 1 }$ .
So $M _ { r } \cong U \perp D _ { r - 1 } ( - 1 )$ .
In order that $M _ { r }$ embeds in $\Lambda$ , we must have $r \leq 1 9$ , for reasons of signature.
The value $r = 1 9$ is attained, for one can easily show that $U \perp D _ { 1 8 } ( - 1 ) \perp I ( 2 ) \perp I ( 2 )$ has an even unimodular overlattice (of signature $( 3 , 1 9 )$ and as is well-known, such a lattice is isomorphic to $\Lambda$ .

Lemma 8.3. The group $\Gamma _ { g }$ acts transitively on $E _ { g } ^ { \prime }$ for $g \geq 2$ ) and on $E _ { g } ^ { \prime \prime }$ for $g \geq 3$ .
If $g \geq 4$ and $r$ is a positive integer, then $\Gamma _ { g }$ is also transitive on the collection of nondegenerate sublattices of $\Lambda$ of signature $( 1 , r )$ spanned by $h _ { g }$ and elements of $E _ { g } ^ { \prime \prime }$ , provided that this collection is nonempty.

Proof.
We will first prove this lemma for equivalence with respect to the stabilizer ${ \mathrm { O } } ( \Lambda ) _ { h _ { g } }$ of $h _ { g }$ in the orthogonal group of $\Lambda$ .
For this we need the following wellknown transitivity property: given an even nondegenerate lattice $M$ of rank $\rho$ and an even unimodular lattice $N$ which contains a copy of $U ^ { \perp ( \rho + 1 ) }$ , then the primitive embeddings of $M$ in $N$ are all in the same orbit of the orthogonal group of $N$ .

For all $g \geq 2$ resp.
$g \geq 3$ , $h _ { g }$ and an element of $E _ { g } ^ { \prime }$ resp.
$E _ { g } ^ { \prime \prime }$ span a primitive sublattice of $\Lambda$ and so the above transitivity property implies that $E _ { g } ^ { \prime }$ ( $g \geq 2$ ) and $E _ { g } ^ { \prime \prime }$ ( $g \geq 3$ ) is an orbit of $\mathrm { O } ( \Lambda ) _ { h _ { g } }$ .
This already covers all cases $g \geq 5$ .
For $g = 4$ , the remaining case is when the sublattice in question is isometric to $U \perp I ( - 2 )$ .
Since $U$ embeds uniquely up to orthogonal transformation in $\Lambda$ , the issue is equivalent to the uniqueness of the embedding of $I ( - 2 )$ in the even unimodular lattice $\Lambda ^ { \prime } : =$ $U ^ { \perp 2 } ~ \perp ~ E _ { 8 } ( - 1 ) ^ { \perp 2 }$ .
This is also covered by the quoted transitivity property.
To finish the proof we observe that in all cases we can find an element in $\mathrm { O } ( \Lambda ) _ { h _ { g } }$ which stabilizes an element of $E _ { g } ^ { \prime }$ resp.
a sublattice as in the lemma and sends $\mathbb { D } _ { g }$ to its complex conjugate.
□

This lemma shows in particular that $D _ { g } ^ { \prime }$ and $D _ { g \geq 3 } ^ { \prime \prime }$ are irreducible.

Remark 8.4. The second clause of the lemma above is not true as stated when $g = 3$ , since for $r = 9$ and $r = 1 7$ there exist imprimitive embeddings of $M _ { r } \cong U \perp D _ { r - 1 }$ in $\Lambda$ for which the image of $h _ { 3 }$ is still primitive.
However it can be shown that Lemma 8.3 still holds for primitive sublattices.
The imprimitive sublattices—which exist only for $r = 9$ and $r = 1 7$ —also form a single $\Gamma _ { 3 }$ -orbit.

From Lemma 8.1 and Corollary 7.5 we deduce:

Corollary 8.5. For all $g \geq 2$ , $g \neq 3$ , the algebra of meromorphic automorphic forms

$$
\oplus _ { k \in \mathbb { Z } } H ^ { 0 } ( \mathbb { D } _ { g } ^ { \circ } , \mathcal { O } ( \mathbb { L } ^ { k } ) ) ^ { \Gamma _ { g } }
$$

is finitely generacompactification $X _ { g } ^ { \Sigma ( \mathcal { H } _ { g } ) }$ poof $X _ { g }$ ive degree generators.
Theand of the compactification $\widehat { X _ { g } ^ { \circ } }$ nda of $X _ { g } ^ { \circ }$ of the semitoric is of dimension 2, except when $g = 4$ , where this dimension is 3. The closures of $D _ { g } ^ { \prime }$ and $D _ { g } ^ { \prime \prime }$ are disjoint in X Σ(H)g a nd $D _ { g } ^ { \prime }$ is without selfintersection.
The same is true of $D _ { g } ^ { \prime \prime }$ when $g > 4$ .

We shall see that the first part of the statement of this corollary also holds for $g = 3$ .

Saint-Donat [23] made a detailed study of the projective models of $K 3$ -surfaces and it is interesting to observe that the loci $D _ { g } ^ { \prime }$ , $D _ { g } ^ { \prime \prime }$ and their selfintersections parametrize semipolarized $K 3$ -surfaces that appear in his classification.
This correspondence is as follows (we omit the proofs, which are not difficult):

$D _ { g } ^ { \prime }$ : The $K 3$ -surfaces endowed with an elliptic fibration with a section; the polarization is $( g - 1 )$ times the class of the fibration plus the class of a section.
The morphism to $\| ^ { p g }$ defined by the polarization is the composite of the fibration and a degree embedding of the base curve in $\| ^ { p g }$ .
These $g$ families become pairwise isomorphic if we forget their polarization.
D′′ $D _ { g \geq 3 } ^ { \prime \prime }$ : The $K 3$ -surfaces $S$ of genus $g \geq 3$ endowed with an elliptic fibration and a bisection.
The bisection is a smooth curve of genus $i ~ = ~ 0$ or $i = 1$ depending on whether $g$ is even or odd.
The polarization is $[ { \frac { 1 } { 2 } } g ] =$ $\textstyle { \frac { 1 } { 2 } } ( g - i )$ times the class of the fibration plus the class of the bisection.
The morphism $S \to \mathbb { P } ^ { g }$ defined by the polarization factors as a degree two cover $S  \Sigma _ { i }$ (here $\Sigma _ { i }$ is the $\mathbb { P } ^ { 1 }$ -bundle over $\mathbb { P } ^ { 1 }$ with a section of selfintersection $- \imath$ ) followed by the embedding of the latter in $\varPsi ^ { g }$ by the linear system defined by a section of selfintersection $- i$ plus $[ \textstyle { \frac { 1 } { 2 } } g ]$ times a fiber.

$( D _ { 4 } ^ { \prime \prime } ) ^ { ( 2 ) }$ : The $K 3$ -surfaces $S$ of genus 4 endowed with an elliptic fibration, a section $C _ { 0 }$ and a smooth rational curve $C _ { 1 }$ in a fiber met by the section $C _ { 0 }$ , the polarization being 3 times the class of the fibration plus the class of $2 C _ { 0 } + C _ { 1 }$ .
The morphism $S \to \mathbb { P } ^ { 4 }$ defined by the polarization has image in $\mathbb { P } ^ { 4 }$ the cone over a smooth rational cubic curve in $\mathbb { P } ^ { 3 }$ ; the map to the image is of degree two and ramifies over the vertex.

$( D _ { 3 } ^ { \prime \prime } ) ^ { ( r ) }$ : The $K 3$ -surfaces $S$ of genus 3 endowed with an elliptic fibration, a section $C _ { 0 }$ and smooth rational curves $C _ { 1 } , \ldots , C _ { r - 1 }$ such that the intersection diagram of $( ( \mathrm { f i b e r } ) + C _ { 0 } , C _ { 1 } , \dots , C _ { r } )$ is the affine Dynkin diagram type $\widehat { B } _ { r }$ : for $r = 2$ , $C _ { 1 }$ is a section disjoint from $C _ { 0 }$ , for $r = 3$ , $C _ { 1 }$ and $C _ { 2 }$ lie in distinct fibers and both meet $C _ { 0 }$ , for $4 \leq r \leq 1 9 C _ { 1 } , \ldots , C _ { r - 1 }$ lie in single fiber and make up with $C _ { 0 }$ a $D _ { r }$ -configuration.
The polarization is given by the positive generator of the radical of the $\widehat { B } _ { r }$ -diagram: $2 ( ( \mathrm { f i b e r } ) +$ $C _ { 0 } + \cdot \cdot \cdot + C _ { r - 3 } ) + C _ { r - 2 } + C _ { r - 1 }$ .
The morphism $S  \mathbb { P } ^ { 3 }$ defined by the polarization has image a quadric cone; the map to the image is of degree two and does not ramify over the vertex. (For $r \geq 4$ , the curves $C _ { 1 } , \ldots , C _ { r - 1 }$ lie on a Kodaira fiber of the elliptic fibration.)

8B.
$K 3$ -surfaces of small genus.
A $K 3$ -surface $X$ of genus 2 for which the linear system is of digonal type is realized by the linear system as a double cover of a projective plane ramifying along a sextic curve with only simple singularities.
A $K 3$ -surface of genus 3, 4 or 5 for which the linear system is nonhyperelliptic is realized as a quartic hypersurface in $\mathbb { P } ^ { 3 }$ , resp.
a complete intersection of bidegree $( 2 , 3 )$ in $\mathbb { P } ^ { 4 }$ , resp.
a complete intersection of three quadrics in $\mathbb { P } ^ { 5 }$ .

We fix a vector space $W _ { g }$ of dimension $g + 1$ and a generator $\alpha _ { g }$ of $\wedge ^ { g + 1 } W _ { g }$ , which we shall view as a translation invariant $( g + 1 )$ -form on $W _ { g } ^ { * }$ .
For $g = 2 , 3 , 4 , 5$ we define a projective variety $Y _ { g }$ with very ample class $\eta _ { g }$ on which the group $\operatorname { S L } ( W _ { g } )$ naturally acts through its simple quotient $\operatorname { P S L } ( W _ { g } )$ :

$g = 2$ : $Y _ { 2 }$ is the projective space $\mathbb { P } ( \mathrm { S y m } ^ { 6 } W _ { 2 } )$ of all sextics in $\mathbb { P } ( W _ { 2 } ^ { * } )$ and $\eta _ { 2 } =$ $\mathcal { O } _ { \mathbb { P } ( \mathrm { S y m } ^ { 6 } W _ { 2 } ) } ( 1 )$ ,  
$g = 3$ : $Y _ { 3 }$ is the projective space $\mathbb { P } ( \mathrm { S y m } ^ { 4 } W _ { 3 } )$ of all quartics in $\mathbb { P } ( W _ { 3 } ^ { * } )$ and $\eta _ { 3 } =$ $\mathcal { O } _ { \mathbb { P } \mathrm { ( S y m ^ { 4 } } ~ W _ { 3 } ) } ( 1 )$ ,  
$g = 4$ : $Y _ { 4 } = \mathbb { P } ( \mathbb { E } )$ , where $\mathbb { E }  \mathbb { P } ( \mathrm { S y m } ^ { 2 } W _ { 4 } )$ is the vector bundle whose fiber over $[ Q ]$ is the cokernel of $W _ { 4 } \to \mathrm { S y m } ^ { 3 } W _ { 4 }$ , $w \mapsto Q . w$ (this makes $Y _ { 4 }$ the space of all complete intersections of bidegree $( 2 , 3 )$ in $\mathbb { P } ( W _ { 4 } ^ { * } )$ ), and $\eta _ { 4 } = \mathcal { O } _ { \mathbb { P } ( \mathbb { E } ) } ( 1 ) \otimes \mathcal { O } _ { \mathbb { P } ( \mathrm { { S y m } ^ { 2 } } W _ { 4 } ) } ( 1 )$ ,  
$g = 5$ : $Y _ { 5 }$ is the Grassmannian $G _ { 3 } \ : \mathrm { S y m ^ { 2 } } ( W _ { 5 } )$ (in other words, the space of all complete intersections of tridegree $( 2 , 2 , 2 )$ in $\mathbb { P } ( W _ { 5 } ^ { * } ) )$ and $\eta _ { 5 }$ the line bundle defining the Pl¨ucker embedding.

We denote by $U _ { g } \subset Y _ { g }$ the subset of complete intersections for which the only singular points are simple singularities.

The following theorem implies among other things that the algebra of meromorphic automorphic forms $\oplus _ { k \in \mathbb { Z } } H ^ { 0 } ( \mathbb { D } _ { g } ^ { \circ } , \mathcal { O } ( \mathbb { L } ^ { k } ) ) ^ { \downarrow } g$ is generated with positive degree generators also when $g = 3$ .

Theorem 8.6. Let $g \in \{ 2 , 3 , 4 , 5 \}$ .
Then the period mapping defines an isomorphism $\operatorname { P S L } ( W _ { g } ) \backslash U _ { g }  X _ { g } ^ { \circ }$ .
This isomorphism lifts naturally to an isomorphism between the line bundle PS $\operatorname { L } ( W _ { g } ) \backslash ( U _ { g } , \eta _ { g } | U _ { g } )$ and the line bundle $( X _ { g } , { \mathcal { L } } )$ when $g \neq 2$ and the quotient of $( X _ { 2 } , { \mathcal { L } } )$ by the center $\{ \pm 1 \}$ of $\Gamma _ { 2 }$ in case $g = 2$ .
This, in turn, determines an isomorphism of normal projective varieties $\operatorname { P S L } ( W _ { g } ) \backslash \backslash Y _ { g } ^ { \mathrm { s s } } \cong { \widehat { X _ { g } ^ { \circ } } }$ an d an isomorphism of graded -algebra’s

$$
\begin{array} { r } { \oplus _ { k = 0 } ^ { \infty } H ^ { 0 } ( Y _ { g } , \eta _ { g } ^ { \otimes k } ) ^ { \mathrm { P S L } ( W _ { g } ) } \cong \oplus _ { k \in \mathbb { Z } } H ^ { 0 } ( \mathbb { D } _ { g } ^ { \circ } , \mathcal { O } ( \mathbb { L } ^ { k } ) ) ^ { \Gamma _ { g } } . } \end{array}
$$

Proof.
We begin with showing that given a $y \in U _ { g }$ , then every nonzero linear form $F$ on the line $\eta _ { g } ( y )$ defines a $K 3$ -surface $S ( F )$ together with a generating section $\alpha ( F )$ of its dualizing sheaf in such a manner that the dependence on $F$ is of degree $^ { - 1 }$ : $S ( t F )$ is canonically isomorphic to $S ( F )$ and under this isomorphism $\alpha ( t F )$ corresponds to $t ^ { - 1 } \alpha ( F )$ .
In the case $g = 2$ , which we discuss first, this has to be qualified since the objects of interest all come with a nontrivial involution.

So assume that $g = 2$ and let us write $\mathbb { P }$ for $\mathbb { P } ( W _ { 2 } ^ { * } )$ .
Let $\mathbb { E }$ denote the total space of the line bundle over $\mathbb { P }$ whose sheaf of sections is $\mathcal { O } _ { \mathbb { P } } ( - 3 )$ .
Its dualizing sheaf $\omega _ { \mathbb { E } }$ is naturally identified with the pull-back of $\omega _ { \mathbb { P } } ( 3 )$ .
The choice of generator for $\wedge ^ { 3 } W _ { 2 }$ defines a nowhere zero section of $\omega _ { \mathbb { P } } ( 3 )$ and hence a nowhere zero section of $\omega _ { E }$ .
Denote this section by $\alpha$ .

Now let $y \in U _ { 2 }$ define the sextic curve $C ( y )$ in $\mathbb { P } ( W _ { 2 } ^ { * } )$ and let $F \in \mathrm { S y m } ^ { 6 } W _ { 2 }$ be a defining equation for this curve (equivalently, a nonzero linear form on $\eta _ { 2 } ( y )$ ).
We regard $F ^ { \prime }$ as a regular function on $\mathbb { E }$ which is homogeneous of degree 2. Then the zero set of $F - 1$ , closed off in the projective completion of $E$ is a double cover $S ( F ) \to \mathbb { P }$ ramified along $C ( y )$ and the residue of $( F - 1 ) ^ { - 1 } \alpha$ on $S ( F )$ is a nowhere zero section $\alpha ( F )$ of its dualizing sheaf $\omega _ { S ( F ) }$ .
This construction is homogeneous of degree $- \frac { 1 } { 2 }$ in the following sense: multiplication by $t$ in $\mathbb { E }$ sends $S ( F )$ to $S ( t ^ { - 2 } F )$ and under this isomorphism $\alpha ( t ^ { - 2 } F )$ corresponds to $t \alpha ( F )$ .
This is also reflected by the fact that the involution sends $\alpha ( F )$ to $- \alpha ( F )$ .
So a complete invariant for $\pm ( S ( F ) , \alpha ( F ) )$ is $\alpha ( F ) ^ { 2 }$ , viewed as a section of either $\omega _ { S ( F ) } ^ { \otimes 2 }$ o r $\omega _ { \mathbb { P } } ^ { \otimes 2 } ( C ( y ) )$ .
We then obtain an isomorphism between the lines $\eta ( y )$ and $H ^ { \cup } ( \omega _ { \mathbb { P } } ( C ( y ) ) ) ^ { \otimes 2 }$ .

For $g = 3 , 4 , 5$ we proceed in a similar fashion, although the situation is simpler.
For instance, a nonzero linear form on $\eta _ { 5 } ( y )$ is represented by a nonzero decomposable element $F _ { 0 } \wedge F _ { 1 } \wedge F _ { 2 }$ of $\wedge ^ { 3 } ( \mathrm { S y m } ^ { 2 } W _ { 5 } )$ whose factors define $S ( y )$ in $\mathbb { P } ( W _ { 5 } ^ { * } )$ .
The iterated residue of $\alpha _ { 5 }$ relative to the ordered triple $( F _ { 0 } , F _ { 1 } , F _ { 2 } )$ defines a generator of the dualizing sheaf of the common zero set of this triple in $W _ { 5 } ^ { * }$ .
This 3-form is $\mathbb { C } ^ { \times }$ -invariant, and by taking the residue at infinity, we get a generating section α(F ) of ωS(y).

Let $\widehat { S } ( y )$ be the minimal resolution of $S ( y )$ .
We recall that $H ^ { 2 } ( \widehat { S } ( y ) , \mathbb { Z } )$ is a free abelian group and equipped with its intersection pairing isomorphic to the $K 3$ - lattice $\Lambda$ .
The isomorphism can be chosen in such a manner that the pull-back to $\widehat { S } ( y )$ of the hyperplane class of $\mathbb { P } ( W _ { g } ^ { * } )$ is mapped to $h _ { g }$ .
Under such an isomorphism, $H ^ { 0 } ( \omega _ { \widehat { S } ( y ) } )$ is mapped to $\scriptstyle { \underline { { \mathbb { L } } } } _ { g }$ or its complex conjugate.
We can (and will) choose the isomorphism such that the former occurs.
It is clear from the definition that $\Gamma _ { g }$ permutes the collection of such isomorphisms simply transitively, so we get a period morphism on the level of line bundles (with the usual qualification in case $g = 2$ ):

$$
\mathrm { P S L } ( W _ { g } ) \backslash ( U _ { g } , \eta _ { g } | U _ { g } )  ( X _ { g } , { \mathcal { L } } ) .
$$

The theory of period mappings for $K 3$ -surfaces tells us that this morphism is an open embedding whose image on the base is just $X _ { g } ^ { \circ }$ .
If we combine this with the observation that the deleted part $Y _ { g } - U _ { g }$ is of codimension $\geq 2$ , all assertions follow.
□

Problem 8.7. We have not been able to generalize this theorem to higher values of $g$ , although work of Mukai [18] suggests that this could be done at least for $g \leq 1 0$ : he observed that in the range $6 \leq g \leq 1 0$ , a general primitively semipolarized $K 3$ of genus $g$ is still a complete intersection on a homogeneous projective variety (in fact a linear section for $7 \leq g \leq 1 0$ ).
If this produces all nonhyperelliptic $K 3$ -surfaces with rational double points in $\mathbb { P } ^ { g }$ that are primitively polarized by the hyperplane class for these values of $g$ , then Theorem 8.6 extends to that range.

Problem 8.8. The singular objects parametrized by $Y _ { g }$ define for $g \leq 5$ a hypersurface in $Y _ { g }$ .
This hypersurface is defined by a section of a (computable) power of $\eta _ { g }$ .
Via Theorem 8.6 we deduce that there must exist a meromorphic $\Gamma _ { g }$ -automorphic form whose divisor is twice the arrangement defined by the $\left( - 2 \right)$ -vectors in $\Lambda _ { g }$ plus a linear combination of the arrangements defined by $E _ { g } ^ { \prime }$ ( $g \geq 2$ ) and $E _ { g } ^ { \prime \prime }$ ( $g \geq 3$ ).
We expect this automorphic form to have a product expansion.
We wonder whether this is true for all $g$ .
Again, Mukai’s work suggests this to be so for $g \leq 1 0$ .
A theorem due to Borcherds, Katzarkov, Pantev and Shepherd-Barron [6] implies that there is an automorphic form whose zero set is an arrangement which contains the locus in question.

# 9. Application to moduli of general Enriques surfaces

In this section we briefly explain how the work of H.
Sterk fits in this setting (but his results go well beyond what is discussed here; see his two part paper [24]).
Let us recall that an Enriques surface is a surface which admits a $K 3$ surface as an unramified covering of degree two.
Since a $K 3$ -surface is simply connected, an Enriques surface $S$ is essentially the same thing as a $K 3$ -surface $S$ equipped with a fixed point free involution.
All of the cohomology of an Enriques surface is algebraic and so the same is true for the cohomology of $S$ invariant under the involution.

Every Enriques surface $S$ admits a semipolarization of degree 2, that is, a class $\bar { h } \in \operatorname { P i c } ( \bar { S } )$ intersecting every effective class nonnegatively and with $\bar { h } \cdot \bar { h } = 2$ .
Let $\bar { h } \in \operatorname { P i c } ( \bar { S } )$ be such a class.
Then its preimage $h$ in $S$ defines a digonal semipolarization of degree 4 on $S$ : its linear system defines a morphism of degree two from $\widehat { S }$ onto a nonsingular quadric or a quadric cone in projective three space.
Its discriminant curve is the intersection of this quadric with a quartic surface.
Following Horikawa we call $( S , h )$ general or special according to whether the quadric is smooth or not.
We shall concentrate here on the general case.
Let us first do the discussion for general digonal $K 3$ -surfaces of genus 3.

9.1. We start out with two complex vector spaces $W$ , $W ^ { \prime }$ of dimension two and abbreviate $\mathbb { P } : = \mathbb { P } ( W ^ { * } )$ and $\mathbb { P } ^ { \prime } : = \mathbb { P } ( W ^ { \prime * } )$ .
Let $\mathbb { E }  \mathbb { P } \times \mathbb { P } ^ { \prime }$ be the line bundle whose sheaf of sections is the exterior tensor product $\mathcal { O } _ { \mathbb { P } } ( - 2 ) \boxtimes \mathcal { O } _ { \mathbb { P } ^ { \prime } } ( - 2 )$ .
A straightforward argument shows that the choice of a generator of $\wedge ^ { 2 } W \otimes \wedge ^ { 2 } W ^ { \prime }$ determines a generating section $\alpha$ of its dualizing sheaf $\omega _ { \mathbb { E } }$ .

The divisors of bidegree $( 4 , 4 )$ on $\mathbb { P } \times \mathbb { P } ^ { \prime }$ are parametrized by the projective space $Y : = \mathbb { P } ( \mathrm { S y m } ^ { 4 } W \otimes \mathrm { S y m } ^ { 4 } W ^ { \prime } )$ ).
Take $\eta : = \mathcal { O } _ { Y } ( 1 )$ and let $U ~ \subset ~ Y$ be the locus parametrizing divisors with only simple singularities.
Choose $y \in U$ and let $F \in \operatorname { S y m } ^ { 4 } W \otimes \operatorname { S y m } ^ { 4 } W ^ { \prime }$ be a nonzero element lying over $y$ .
Then $F$ defines a regular function on $E$ which is homogeneous of degree 2. This gives rise to a double cover $S ( F ) \to \mathbb { P } \times \mathbb { P } ^ { \prime }$ and a generating section $\alpha ( F )$ of its dualizing sheaf.
Its minimal resolution is naturally a $K 3$ -surface endowed with a genus 3 semipolarization of digonal type.
As in the case for $K 3$ -surfaces of genus 2, we get a natural isomorphism between the fiber $\eta ( y )$ and the set of isomorphism classes of pairs $( S ( F ) , \alpha ( F ) )$ .
The subgroup $G$ of $\operatorname { P S L } ( W \oplus W ^ { \prime } )$ which preserves the direct sum decomposition (allowing the summands to interchange) acts on $\mathrm { S y m } ^ { 4 } W \otimes$ $\mathrm { S y m } ^ { 4 } W ^ { \prime }$ and hence on $( Y , { \mathcal { O } } _ { Y } ( 1 ) )$ and the $G$ -orbit space of $( U , { \mathcal { O } } _ { U } ( 1 ) )$ can be understood as an open part of the moduli space of digonal $K 3$ -surfaces of genus 3.

Next assume we are given involutions $i$ in $W$ resp.
$i ^ { \prime }$ in $W ^ { \prime }$ with one-dimensional eigenspaces.
Notice that the involution $( i , i ^ { \prime } )$ has four fixed points in $\mathbb { P } \times \mathbb { P } ^ { \prime }$ .
The involution $( i , i ^ { \prime } )$ also acts naturally in $\mathbb { E }$ (with the four fibers as fixed point set).
We put

$$
Y _ { E } : = \mathbb { P } ( ( \mathrm { S y m } ^ { 4 } W \otimes \mathrm { S y m } ^ { 4 } W ^ { \prime } ) ^ { i \otimes i ^ { \prime } } ) \mathrm { ~ a n d ~ } \eta _ { E } : = \mathcal { O } _ { Y _ { E } } ( 1 ) ,
$$

and denote by $U _ { E } \subset Y _ { E }$ the open subset parametrizing divisors not passing through a fixed point and with simple singularities only.
For a nonzero $F \in { \mathrm { { S y m } } } ^ { 4 } W \otimes$ $\operatorname { S y m } ^ { 4 } W ^ { \prime } ) ^ { i \otimes i ^ { \prime } }$ over $U _ { E }$ , the involution $- ( i , i ^ { \prime } )$ restricts to a fixed point free involution on the minimal resolution ${ \widehat { S } } ( F )$ of $S ( F )$ and so its orbit variety is an Enriques surface.
This Enriques surface comes naturally with an a semipolarization of degree two and is general.
If $G _ { E }$ is the $G$ -centralizer of the involution $( i , i ^ { \prime } )$ , then $G \backslash U _ { E }$ can be understood as the coarse moduli space of semipolarized Enriques surfaces of general type.

9.2. It is well-known that the action of a fixed point free involution of a $K 3$ -surface $S$ induces in $H ^ { 2 } ( S ; \mathbb { Z } )$ an involution equivalent to the involution $\iota$ of $\Lambda$ defined as follows: if we write $\Lambda _ { E }$ for the Enriques lattice $E _ { 8 } ( - 1 ) \perp U$ and identify $\Lambda$ with $\Lambda _ { E } \perp \Lambda _ { E } \perp { \cal U }$ , then $\iota ( a , b , c ) = ( b , a , - c )$ .
Notice that the eigenlattices $\Lambda ^ { + }$ resp.
$\Lambda ^ { - }$ are isometric to $\Lambda _ { E } ( 2 )$ resp.
$\Lambda _ { E } ( 2 ) \perp { \cal U }$ .
The name of $\Lambda _ { E }$ is explained by the fact that an equivariant isometry $H ^ { 2 } ( S ; \mathbb { Z } ) \cong \Lambda$ identifies $H ^ { 2 } ( S , \mathbb { Z } )$ modulo its torsion with the lattice $\Lambda ^ { + } ( \frac { \ d H _ { 1 } } { \ d z } ) \cong \Lambda _ { E }$ .
Observe that the signature of $\Lambda ^ { - }$ is $( 2 , 1 0 )$ .

We put $h ^ { + } : = ( e + f , e + f , 0 ) \in \Lambda ^ { + }$ .
It is not difficult to verify that there are exactly two isotropic vectors in $\Lambda ^ { + }$ with inner product 2 with $h ^ { + }$ , namely $e ^ { + } : = { }$ $( e , e , 0 )$ and $f ^ { + } : = ( f , f , 0 )$ .
If $h \in \operatorname { P i c } ( S )$ is the pull-back of an semipolarization of degree two, then there is always an equivariant isometry $H ^ { 2 } ( S ; \mathbb { Z } ) \cong \Lambda _ { E } \ \bot$ $\Lambda _ { E } \perp U$ which maps to $h$ to $h ^ { + }$ .
In that case the preimages of $e ^ { + }$ and $f ^ { + }$ are classes of effective divisors and $S$ is general precisely when these are the classes of elliptic fibrations.
The only way this can fail is when $S$ contains a $\left( - 2 \right)$ -class whose intersection product with these two isotropic classes is $^ { 1 }$ and $^ { - 1 }$ respectively.
So this is a property that is detected by the Picard lattice.

We are now ready to set up a period mapping on the level of line bundles.
Let $\mathbb { L } _ { E } ^ { \times }$ be a connected component in $\Lambda ^ { - } \otimes \mathbb { C }$ defined by the conditions $z \cdot z = 0$ , $z \cdot \bar { z } > 0$ and let $\mathbb { D } _ { E }$ be its projectivization.
Denote by $\Gamma _ { E }$ the group of isometries of $\Lambda$ that centralize $\iota$ and preserve both $h ^ { + }$ and $\mathbb { D } _ { E }$ .
Put $X _ { E } : = \Gamma _ { E } \backslash \mathbb { D } _ { E }$ and let $\mathcal { L } _ { E }$ be the line bundle over $X _ { E }$ defined by $\mathbb { L } _ { E }$ .
Then we have a refined period mapping

$$
G _ { E } \backslash ( U _ { E } , \eta _ { E } | U _ { E } )  ( X _ { E } , { \mathcal { L } } _ { E } ) .
$$

A Torelli theorem asserts that this is an open embedding with image the complement $X _ { E } ^ { \circ }$ of a hypersurface $D _ { E }$ in $X _ { E }$ defined by an arithmetic arrangement.
This arrangement is the collection $\mathcal { H } _ { E }$ of hyperplanes in $\Lambda ^ { - } \otimes \mathbb { C }$ that are perpendicular to a $\left( - 2 \right)$ -vector $r$ in $\Lambda$ with $r \cdot e ^ { + } = 1$ and $r \cdot f ^ { + } = - 1$ .
This missing hypersurface parametrizes the special Enriques surfaces.
As a subset of the Grassmannian, $\mathcal { H } _ { E }$ is an orbit of $\Gamma _ { E }$ and so $D _ { E }$ is irreducible.
The maximal codimension of an intersection of hyperplanes from $\mathcal { H } _ { E }$ which meets $\mathbb { D } _ { E }$ is $2$ .
Since $Y _ { E } - U _ { E }$ is of codimension $> 1$ in $Y - E$ , it follows from Theorem 7.6:

Theorem 9.3. The refined period mapping determines an isomorphism of normal projective varieties $G _ { E } \backslash \backslash Y _ { E } ^ { \mathrm { s s } } \cong \widehat { X _ { E } ^ { \circ } }$ and an isomorphism of graded $\mathbb { C }$ -algebra’s

$$
\oplus _ { k = 0 } ^ { \infty } H ^ { 0 } ( Y _ { E } , \eta _ { E } ^ { \otimes k } ) ^ { G _ { E } } \cong \oplus _ { k = 0 } ^ { \infty } H ^ { 0 } ( \mathbb { D } _ { E } ^ { \circ } , \mathcal { O } ( \mathbb { L } _ { E } ^ { k } ) ) ^ { \Gamma _ { E } } .
$$

A stratification of $G _ { E } \backslash \backslash Y _ { E } ^ { \mathrm { s s } }$ has been worked out by Shah [22].
Sterk shows that if this stratification is transfered to the arithmetic side of the equation, then it is the s with the ddefined by ition of is obta $\widehat { X _ { E } ^ { \circ } }$ .
He also proves that the compactication as GIT quotient of a natural blowup of $X _ { E } ^ { \Sigma ( \mathcal { H } _ { E } ) }$ $X _ { E }$ $\mathcal { H } _ { E }$ $Y _ { E }$

Remark 9.4. The singular divisors parametrized by $Y _ { E }$ make up a hypersurface.
This hypersurface is given by a section of a power of $\eta _ { E }$ .
On the arithmetic side it must be given by a meromorphic automorphic form whose divisor is supported by the arithmetic arrangement that is the union of $\mathcal { H } _ { E }$ and the hyperplanes perpendicular to $\left( - 2 \right)$ -vectors in $\Lambda ^ { - }$ .
(This form is not the one exhibited by R.
Borcherds in [3], since we also excluded the locus of special Enriques surfaces.) We see from this discussion that this form already lives on the 18-dimensional domain of digonal $K 3$ -surfaces of degree 4.

# 10. Application to smoothing components of triangle singularities

In this section we give an application in the same spirit to the semi-universal deformation of a triangle singularity.
Let us first recall what these are.
Given integers $2 \leq p _ { 1 } \leq p _ { 2 } \leq p _ { 3 }$ with $p _ { 1 } ^ { - 1 } + p _ { 2 } ^ { - 1 } + p _ { 3 } ^ { - 1 } < 1$ , then a triangle singularity of type $( p _ { 1 } , p _ { 2 } , p _ { 3 } )$ is a normal surface singularity which admits a (nonminimal) resolution consisting of a ‘central’ smooth rational curve of selfintersection $^ { - 1 }$ and three smooth rational curves of selfintersection $- p _ { 1 } , - p _ { 2 } , - p _ { 3 }$ , which are pairwise disjoint and meet the central curve transversally in a single point.
These conditions characterize the singularity up to isomorphism.
This singularity has a $\mathbb { C } ^ { \times }$ -action with positive weights: that is, it sits naturally on a normal affine surface with $\mathbb { C } ^ { \times }$ -action such that all $\mathbb { C } ^ { \times }$ -orbits have the singularity in their closure.
Its semiuniversal deformation inherits this $\mathbb { C } ^ { \times }$ -action but here all but one of the weights are positive so that the positive weight part is of codimension one in the full semiuniversal deformation.
We can realize this singularity and the positive weight part of semi-universal deformation in a projective setting as follows.

By a standard procedure we can canonically complete this surface to a normal projective surface $Z _ { o }$ that is smooth away from the $T _ { p _ { 1 } , p _ { 2 } . p _ { 3 } }$ -singularity.
What has been added at infinity is a $T _ { p _ { 1 } , p _ { 2 } , p _ { 3 } }$ -curve $T _ { o }$ : that is a union of smooth rational curves whose dual intersection graph is a $T$ -shape whose arms have $p _ { 1 } - 1$ , $p _ { 2 } - 1$ , $p _ { 3 } - 1$ edges.
The naturality guarantees that the $\mathbb { C } ^ { \times }$ action extends to $Z _ { o }$ .
One can further show that $Z _ { o }$ is regular ( $H ^ { 1 } ( \mathcal { O } _ { Z _ { o } } ) = 0$ ) and that its dualizing sheaf is trivial with $\mathbb { C } ^ { \times }$ -acting on $H ^ { 0 } ( \omega _ { Z _ { o } } )$ with degree one.
A deformation of $Z _ { o }$ which preserves $T _ { o }$ induces a deformation of the singularity $( Z _ { o } , x _ { o } )$ of positive weight.
To be precise, there exist

a proper flat morphism $Z \to S$ whose fibers are normal surfaces and whose base is an affine scheme,  
a distinguished point $o \in S$ such that the fiber $Z _ { o }$ is identified with its namesake above,  
an $S$ -embedding of $T _ { o } \times S$ in the open subset of $Z$ where $\pi$ is smooth and which over $o$ is the inclusion,  
a good $\mathbb { C } ^ { \times }$ -action on $\pi$ preserving these data, such that the local-analytic germ of $\pi$ at $x _ { o }$ is the the positive weight part of a semi-universal deformation of the singularity $( Z _ { o } , x _ { o } )$ .

In this situation we can find a generating section $\zeta$ of the relative dualizing sheaf $\omega _ { Z / S }$ such that $t \in \mathbb { C } ^ { \times }$ sends $\zeta$ to $t \zeta$ .
So for every fiber $s \in S$ , we have a triple $( Z _ { s } , T _ { o } \hookrightarrow Z _ { s } , \zeta _ { s } )$ , where $Z _ { s }$ is a regular normal surface of zero irregularity, $T _ { o } \hookrightarrow Z _ { s }$ an embedding in the smooth part of $Z _ { s }$ and $\zeta _ { s }$ a generator of its dualizing sheaf.
A fiber with only rational double points as singularities is necessarily a $K 3$ -surface.
We denote the corresponding subset of $S$ by $S ^ { \circ }$ .
It is open in $S$ .
An irreducible component of $S$ which meets $S ^ { \circ }$ contains points with a smooth fiber and is therefore called a smoothing component of $Z _ { o }$ .
The fibers parametrized by $S - S ^ { \circ }$ have a unique minimally elliptic singularity, other singularities being rational double points.
Denote by $S ^ { \circ } \subset S$ the locus over which the only singularities are rational double points.
It is known that $S ^ { \circ }$ has pure dimension $2 2 - \textstyle \sum _ { i } p _ { i }$ .
We shall describe the normalization of the closure of $S ^ { \circ }$ in terms of our construction.

10.1. Let $Q _ { p 1 , p 2 , p 3 }$ denote the abstract lattice spanned by the irreducible components of $T _ { o }$ and with symmetric bilinear form dictated by the intersection matrix of these irreducible components.
This is a nondegenerate hyperbolic lattice of signature $( 1 , \sum _ { i } ( p _ { i } - 1 ) )$ ).
Any $K 3$ -surface $S$ that we get as a fiber comes with an embedding $T _ { o } \hookrightarrow S$ .
This clearly induces an injection of lattices $Q _ { p _ { 1 } , p _ { 2 } , p _ { 3 } } \hookrightarrow H ^ { 2 } ( S ; \mathbb { Z } )$ whose image lands in $\mathrm { P i c } ( S )$ .
From this we get that we must have $p _ { 1 } + p _ { 2 } + p _ { 3 } \leq 2 2$ .

But the existence of an isometric embedding of $Q _ { p _ { 1 } , p _ { 2 } , p _ { 3 } }$ in the Picard group of a $K 3$ -surface need not imply the existence of an embedding of $T _ { o }$ in that surface.
Let $k ( p _ { 1 } , p _ { 2 } , p _ { 3 } )$ be $6 , 7 , 8$ according to whether $( p _ { 1 } , p _ { 2 } ) = ( 3 , 3 )$ (and hence $p _ { 3 } \geq$ 4) resp.
$( p _ { 1 } , p _ { 2 } ) \ : = \ : ( 2 , 4 )$ (and hence $p _ { 3 } ~ \geq ~ 5$ ) resp.
$( p _ { 1 } , p _ { 2 } ) \ : = \ : ( 2 , 3 )$ (and hence $p _ { 3 } ~ \geq ~ 7$ ).
Then $Q _ { p _ { 1 } , p _ { 2 } , p _ { 3 } }$ contains in an evident manner the affine root lattice $\widehat { E } _ { k ( p _ { 1 } , p _ { 2 } , p _ { 3 } ) } ( - 1 )$ .
This lattice is negative semidefinite and its radical $I ( p _ { 1 } , p _ { 2 } , p _ { 3 } )$ is generated by a positive integral linear combination of its basis vectors, called in [15] the fundamental isotropic element of $Q _ { p _ { 1 } , p _ { 2 } , p _ { 3 } }$ .
Let us denote it by $n$ .
Suppose that $S$ is a $K 3$ -surface and that we are given an embedding of lattices $j : Q _ { p _ { 1 } , p _ { 2 } , p _ { 3 } } \hookrightarrow$ $\mathrm { P i c } ( S )$ .
The theory of $K 3$ -surfaces tells us that by composing $j$ with an isometry of $H ^ { 2 } ( S , \mathbb { Z } )$ which is plus or minus the identity on the orthogonal complement of $\operatorname { P i c } ( Y )$ in $H ^ { 2 } ( Y , \mathbb { Z } )$ , we can arrange that the fundamental isotropic element is mapped to the class of an elliptic fibration $Y ~  ~ \mathbb { P } ^ { 1 }$ with each basis vector of $Q _ { p 1 , p 2 , p 3 }$ mapping to the class of a (unique) effective divisor.
Each of these effective divisors is supported by a configuration of $\left( - 2 \right)$ -curves of type $A$ , $D$ or $E$ .
The question is whether we can arrange this in such a manner that these divisors are all irreducible, for if that is the case, then we clearly have an embedding of $T _ { o }$ in $Y$ .
It is certainly true that in the given situation the effective divisors associated to the basis vector of $\widehat { E } _ { k ( p _ { 1 } , p _ { 2 } , p _ { 3 } ) } ( - 1 )$ are supported by a single fiber of the elliptic fibration.
One of the main results of [15] states that what we want is possible precisely when the basis vectors of $\widehat { E } _ { k }$ are mapped to classes of irreducible curves whose union makes up an entire fiber of the elliptic fibration $Y  \mathbb { P } ^ { 1 }$ .
If this fails, then by the Kodaira classification of such fibers, the fiber in question must have type $\widehat { E } _ { l } ( - 1 )$ for some $l > k ( p _ { 1 } , p _ { 2 } , p _ { 3 } )$ .
So this can only happen if $k ( p _ { 1 } , p _ { 2 } , p _ { 3 } ) \in \{ 6 , 7 \}$ .

This property can be expressed in purely lattice theoretic terms.
Let us abbreviate $k$ for $k ( p _ { 1 } , p _ { 2 } , p _ { 3 } )$ and $I$ for $I ( p _ { 1 } , p _ { 2 } , p _ { 3 } )$ .
We call an embedding $j$ of $Q _ { p 1 , p 2 , p 3 }$ in an arbitrary lattice $M$ a critical if there exists a $e \in M$ with $e \cdot e = - 2$ , $e \perp j ( I )$ and such that $e$ is neither contained in $j ( \widehat { E } _ { k } )$ nor in its orthogonal complement; we call $j$ good if no such $e$ exists in in the primitive hull of the image of $j$ .
If $M$ happens to be nondegenerate of hyperbolic signature $( 1 , \rho )$ (such as is the case for $\operatorname { P i c } ( Y )$ above), then $I ^ { \perp } / I$ is a negative definite lattice.
The set of $\left( - 2 \right)$ -vectors herein decomposes naturally into irreducible root systems of type $A$ , $D$ or $E$ , and one of these contains the image of $j ( \widehat { E } _ { k } )$ .
So it must be of type $E _ { k ( j ) }$ for some $k ( j ) \geq k$ .
To say that the embedding is critical is to say that $k ( j ) > k$ .
It is clear that this never happens if $k = 8$ .

10.2. Still following [15], this leads to the following setup.
Let $\mathbb { L } _ { p _ { 1 } , p _ { 2 } , p _ { 3 } } ^ { \times }$ be the set of $( j , z ) \in \mathrm { H o m } ( Q _ { p _ { 1 } , p _ { 2 } , p _ { 3 } } , \Lambda ) \times ( \Lambda \otimes \mathbb { C } )$ with $j$ a good embedding and $z$ perpendicular to the image of $j$ and satisfying the familiar period conditions $z \cdot z = 0$ and $z \cdot \bar { z } > 0$ .
The corresponding subset $\mathbb { D } _ { p _ { 1 } , p _ { 2 } , p _ { 3 } }$ of $\mathrm { H o m } ( Q _ { p _ { 1 } , p _ { 2 } , p _ { 3 } } , \Lambda ) \times \mathbb { P } ( \Lambda \otimes \mathbb { C } )$ is a disjoint union of type IV domains of dimension $2 2 - \textstyle \sum _ { i } p _ { i }$ .
The orthogonal group $\mathrm { O } ( \Lambda )$ , which operates in an obvious manner on this space, has has only finitely many orbits in the connected component set $\pi _ { 0 } ( \mathbb { L } _ { p _ { 1 } , p _ { 2 } , p _ { 3 } } ^ { \times } )$ .
Moreover, the stabilizer of every connected component is an arithmetic group acting as such on that component.

Let us say that a pair $( j , [ z ] ) \in \mathbb { D } _ { p _ { 1 } , p _ { 2 } , p _ { 3 } }$ is critical if the embedding defined by $j$ in the orthogonal complement of $[ z ]$ in $\Lambda$ is.
Denote by $\mathbb { D } _ { p _ { 1 } , p _ { 2 } , p _ { 3 } } ^ { \circ }$ the subset of noncritical pairs.
The following is proved in [15]:

The critical pairs define an arithmetic arrangement in (each connected component of) $\mathbb { D } _ { p _ { 1 } , p _ { 2 } , p _ { 3 } }$ .  
The arrangement in question is empty when $k = 8$ .
The maximal codimension of an intersection from this arrangement is $\leq 1$ when $k = 7$ and $\leq 2$ when $k = 6$ .  
The quotient $\mathrm { O } ( \Lambda ) \backslash ( \mathbb { L } _ { p _ { 1 } , p _ { 2 } , p _ { 3 } } ^ { \times } ) ^ { \circ }$ is naturally identified with the set $S ^ { \circ }$ of $s \in S$ for which each singular point of $Z _ { s }$ is a rational double point.  
The dimension of the boundary of $S ^ { \circ }$ in $S$ is $\leq 1 0 - k$ .

Corollary 10.3. Suppose that $p _ { 1 } + p _ { 2 } + p _ { 3 } - k \le 1 1$ .
Then the algebra of meromorphic automorphic forms

$$
\oplus _ { d \in \mathbb { Z } } H ^ { 0 } ( \mathbb { D } _ { p _ { 1 } , p _ { 2 } , p _ { 3 } } ^ { \circ } , \mathcal { O } ( \mathbb { L } _ { p _ { 1 } , p _ { 2 } , p _ { 3 } } ^ { d } ) ) ^ { \mathrm { O } ( \Lambda ) }
$$

is finitely generated with positive degree generators.
Its spectrum is the normalization of $S ^ { \circ }$ in $S$ .

Proof.
Denote by $S _ { 1 }$ the relevant smoothing component of $S$ .
The elements of degree $d$ of this algebra can be regarded as functions on $S ^ { \circ }$ that are homogeneous of degree $d$ and so the spectrum in question is the affine completion of $S ^ { \circ }$ .
The assumption $p _ { 1 } + p _ { 2 } + p _ { 3 } - k \le 1 1$ implies (according to the above) that the boundary of $S ^ { \circ }$ in $S$ is of codimension $\geq 2$ in the closure of $s ^ { \circ }$ .
So the affine completion of $S ^ { \circ }$ is the normalization of $S ^ { \circ }$ in $S$ .
□

A triangle singularity of type $( p _ { 1 } , p _ { 2 } , p _ { 3 } )$ has a semi-universal deformation with (irreducible) smooth base if $p _ { 1 } + p _ { 2 } + p _ { 3 }$ is not too large (so that $\dim \mathbb { D } _ { p _ { 1 } , p _ { 2 } , p _ { 3 } }$ is not too small).
For instance, $p _ { 1 } + p _ { 2 } + p _ { 3 } \leq 1 2 + k$ will do, for in these cases we get a hypersurface.
So then not only all good embeddings of $Q _ { p _ { 1 } , p _ { 2 } , p _ { 3 } }$ in the $K 3$ -lattice are conjugate, but more striking perhaps is the conclusion that the corresponding algebra of meromorphic automorphic forms is a polynomial algebra, a property which seems very hard to establish without such a geometric translation.
In these cases, the discriminant hypersurface in the base must be defined by a meromorphic automorphic form whose divisor is supported by the union of the arrangement above and the arrangement of hyperplanes in perpendicular to $\left( - 2 \right)$ -vectors that contain the image of $j$ .
It should have an infinite product expansion.

# References

[1] A.
Ash, D.
Mumford, M.
Rapoport, Y.
Tai: Smooth compactification of locally symmetric varieties, Lie Groups: History, Frontiers and Applications, IV.
Math.
Sci.
Press, Brookline, Mass.
(1975).
[2] W.L.
Baily, Jr.
and A.
Borel: Compactifiation of arithmetic quotients of bounded symmetric domains, Ann.
of Math.
84 (1966), 442–528.
[3] R.E.
Borcherds: The moduli space of Enriques surfaces and the fake Monster Lie superalgebra, Topology 35 (1996), 699–710.
[4] R.E.
Borcherds: Automorphic forms with singularities on Grassmannians, Invent.
Math.
132 (1998), 491–562.
[5] R.E.
Borcherds: Monstrous moonshine and monstrous Lie superalgebras, Invent.
Math.
109 (1992), 405–444.
[6] R.E.
Borcherds, L.
Katzarkov, T.
Pantev, N.I.
Shepherd-Barron: Families of K3 surfaces, J.
Algebraic Geom.
7 (1998), 183–193.  
[7] A.
Borel: Introduction aux Groupes Arithm´etiques, Publ.
Inst.
Math.
Univ.
Strasbourg, XV.
Actualit´es Scientifiques et Industrielles, No.
1341, Hermann, Paris (1969).  
[8] J.H.
Bruinier, E.
Freitag: Local Borcherds products, Ann.
Inst.
Fourier 51 (2001), 1–26.  
[9] J.H.
Conway, N.J.A.
Sloane: Sphere packings, lattices and groups, 3rd edition, Grundlehren der Mathematischen Wissenschaften, 290. Springer-Verlag, New York (1999).  
[10] V.A.
Gritsenko, V.V.
Nikulin: Automorphic forms and Lorentzian Kac-Moody Algebras, Part I, Internat.
J.
Math.
9 (1998), no.
2, 201–275.  
[11] V.A.
Gritsenko, V.V.
Nikulin: On classification of Lorentzian Kac-Moody algebras, available at math.QA/0201162.  
[12] E.
Looijenga: New compactifications of locally symmetric varieties, in: Proceedings of the 1984 Conference in Algebraic Geometry, 341–364, J.
Carrell, A.V.
Geramita, P.
Russell eds.
CMS Conference Proceedings, vol.
6, Amer.
Math.
Soc.
Providence RI (1984).  
[13] E.
Looijenga: Invariant theory for generalized root systems, Invent.
Math.
61 (1980), 1–32.  
[14] E.
Looijenga: Semi-toric partial compactifications I, Report 8520 (1985), 72 pp., Catholic University Nijmegen.  
[15] E.
Looijenga: The Smoothing Components of a Triangle Singularity.
II, Math.
Ann.
269 (1984), 357–387.  
[16] E.
Looijenga: Compactifications defined by arrangements I: the ball quotient case, 27 pp., available at math.AG/0106228.
To appear in Duke Math.
J.  
[17] A.L.
Mayer: Families of $K 3$ surfaces, Nagoya Math.
J.
48 (1972), 1–17.  
[18] S.
Mukai: Curves, $_ { K 3 }$ -surfaces and Fano 3-folds of genus $\leq 1 0$ , in: Algebraic geometry and commutative algebra, Vol.
1, 357–377, H.
Hijikata et al.
eds., Kinokuniya Co.
Ltd., Tokyo (1988).  
[19] V.V.
Nikulin: A remark on discriminants for moduli of $_ { K 3 }$ surfaces as sets of zeros of automorphic forms, J.
Math.
Sci.
81 no.
3 (1996), 2738–2743.  
[20] J.
Shah: A complete moduli space for K3 surfaces of degree 2, Ann.
of Math.
112 (1980), 485–510.  
[21] J.
Shah: Degenerations of $_ { K 3 }$ surfaces of degree 4, Trans.
Amer.
Math.
Soc.
263 (1981), 271–308.  
[22] J.
Shah: Projective degenerations of Enriques surfaces, Math.
Ann.
256 (1981), 475–495.  
[23] B.
Saint-Donat: Projective models of $K - 3$ surfaces, Am.
J.
Math.
96 (1974), 602-639.  
[24] H.
Sterk: Compactifications of the period space of Enriques surfaces.
I, II, Math.
Z.
207 (1991), 1–36 and Math.
Z.
220 (1995), 427–444.  
[25] H.
Sterk: Lattices and K3 surfaces of degree 6, Linear Algebra Appl.
226/228 (1995), 297– 309. Faculteit Wiskunde en Informatica, Universiteit Utrecht, Postbus 80.010, NL-3508  
TA Utrecht, Nederland E-mail address: looijeng@math.uu.nl