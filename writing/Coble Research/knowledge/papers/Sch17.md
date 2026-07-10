---
title: Sch17
authors: []
year: ''
bibkey: Sch17
tags:
- paper
- extraction
abstract: |
  We describe the moduli compactification by stable pairs (also known as KSBA compactification) of a 4-dimensional family of Enriques surfaces, which arise as specific bidouble covers of the blow up of the projective plane at three general points branched along a configuration of three pairs of lines.
  The chosen divisor is an appropriate multiple of the ramification locus.
  We study the degenerations parametrized by the boundary and its stratification.
  We relate this compactification to the Baily-Borel compactification of the same family of Enriques surfaces.
  Part of the boundary of this stable pairs compactification has a toroidal behavior, another part is isomorphic to the BailyBorel compactification, and what remains is a mixture of these two.
  To conclude, we construct an explicit Looijenga’s semitoric compactification whose boundary strata are in bijection with the boundary strata of the KSBA compactification considered.
  
  Index words:
  
  Moduli spaces, compactifications, stable pairs, Enriques surfaces, stable toric pairs, secondary polytopes, lattices, discrete reflection groups.
  
  by
  
  Luca Schaffler
  
  B.S., Roma Tre University, 2010
  
  M.S., Roma Tre University, 2012
  
  A Dissertation Submitted to the Graduate Faculty of The University of Georgia in Partial Fulfillment
  
  of the
  
  Requirements for the Degree
  
  Doctor of Philosophy
  
  Athens, Georgia
  
  Luca Schaffler
  
  All Rights Reserved
  
  Luca Schaffler
  
  Approved:
  
  Professor: Valery Alexeev
  
  Committee: Angela Gibney Dino Lorenzini Robert Varley
  
  Electronic Version Approved:
  
  Suzanne Barbour  
  Dean of the Graduate School  
  The University of Georgia  
  August 2017
---

Luca Schaffler

(Under the Direction of Valery Alexeev)

# Abstract

We describe the moduli compactification by stable pairs (also known as KSBA compactification) of a 4-dimensional family of Enriques surfaces, which arise as specific bidouble covers of the blow up of the projective plane at three general points branched along a configuration of three pairs of lines.
The chosen divisor is an appropriate multiple of the ramification locus.
We study the degenerations parametrized by the boundary and its stratification.
We relate this compactification to the Baily-Borel compactification of the same family of Enriques surfaces.
Part of the boundary of this stable pairs compactification has a toroidal behavior, another part is isomorphic to the BailyBorel compactification, and what remains is a mixture of these two.
To conclude, we construct an explicit Looijenga’s semitoric compactification whose boundary strata are in bijection with the boundary strata of the KSBA compactification considered.

Index words:

Moduli spaces, compactifications, stable pairs, Enriques surfaces, stable toric pairs, secondary polytopes, lattices, discrete reflection groups.

by

Luca Schaffler

B.S., Roma Tre University, 2010

M.S., Roma Tre University, 2012

A Dissertation Submitted to the Graduate Faculty of The University of Georgia in Partial Fulfillment

of the

Requirements for the Degree

Doctor of Philosophy

Athens, Georgia

Luca Schaffler

All Rights Reserved

Luca Schaffler

Approved:

Professor: Valery Alexeev

Committee: Angela Gibney Dino Lorenzini Robert Varley

Electronic Version Approved:

Suzanne Barbour  
Dean of the Graduate School  
The University of Georgia  
August 2017

# Acknowledgements

I would like to thank my advisor Valery Alexeev, which followed and assisted me during my PhD studies.
I will always be grateful for all the beautiful mathematics you taught me and for all the opportunities you provided me.

I would also like to thank the members of the Algebraic Geometry community at the University of Georgia, in particular Angela Gibney, Daniel Krashen, Dino Lorenzini, and Robert Varley.
Thank you for your help and for all the stimulating conversations in these years.

To conclude, I would like to thank my parents, family, colleagues, and friends for always being present and for their invaluable support.

# Contents

# Acknowledgements iv

# 1 Introduction 1

1.1 Motivation and general framework 1  
1.2 Main results .
.
2  
1.3 Background .
5

# 2 Lattice Theory 7

2.1 Basic definitions and facts  
2.2 Unimodular lattices 9  
2.3 The $D _ { p , q }$ lattice .
.
10

# 3 Vinberg’s Algorithm 12

3.1 Roots and reflections .
12  
3.2 Hyperbolic lattices and hyperbolic spaces 13  
3.3 Fundamental domains and Coxeter diagrams 13  
3.4 Algorithm to determine a fundamental domain 14  
3.5 Stopping criterion 15

# K3 Surfaces and Enriques Surfaces 16

4.1 Basic definitions and notations 16  
4.2 K3 surfaces 17  
4.3 Enriques surfaces .
20  
4.4 Half-fibers and the canonical class of an Enriques surface 22

# 5 Convex Geometry and the Secondary Polytope 24

5.1 Basic definitions in convex geometry 24  
5.2 Polyhedral subdivisions 25  
5.3 The secondary polytope 27  
5.4 Polyhedral subdivisions of the unit cube 28

# 6 Moduli of Stable Toric Pairs 32

6.1 Stable toric pairs 32  
6.2 The stack of stable toric pairs 34  
6.3 An explicit computation 35

# 7 Moduli of Stable Pairs 38

7.1 Weighted stable curves .
38  
7.2 Singularities of pairs 39  
7.3 Extension to the non-normal case: semi-log canonical singularities 41  
7.4 Stable pairs and Viehweg’s moduli functor .
.
43

# 8 The KSBA Compactification of the Moduli Space of $D _ { 1 , 6 }$ -polarized Enriques

# Surfaces 45

8.1 $D _ { 1 , 6 }$ -polarized Enriques surfaces and the choice of the divisor 45  
8.2 Stable replacement in a one-parameter family 53  
8.3 Analysis of stability 56  
8.4 KSBA compactification for $D _ { 1 , 6 }$ -polarized Enriques surfaces 67  
8.5 Relation with the Baily-Borel compactification 74  
8.6 Relation with Looijenga’s semitoric compactifications .
81  
8.7 Final remarks .
.
.
86

# Bibliography 88

# Chapter 1

# Introduction

# 1.1 Motivation and general framework

In the study of moduli spaces, it is a problem to provide compactifications which are functorial and with meaningful geometric and combinatorial properties.
A leading example in this sense is the Deligne-Mumford and Knudsen compactification ${ \overline { { M } } } _ { g , n }$ of the moduli space $M _ { g , n }$ , which parametrizes isomorphism classes of smooth $n$ -pointed curves of genus $g$ (see [DM69, Knu83a, Knu83b]).
Another successful example is the toroidal compactification $\overline { { A } } _ { g } ^ { \tau }$ , where $A _ { g }$ is the moduli space parametrizing isomorphism classes of $g$ -dimensional principally polarized abelian varieties and $\tau$ is the second Voronoi fan.
In [Ale02], Alexeev proved that $\overline { { A } } _ { g } ^ { \tau }$ has a modular interpretation, extending previous work of Mumford, Namikawa, and Nakamura (see [Mum72, Nam76, AN99, Ale02]).

After considering curves and abelian varieties, it is natural to look for such “model” compactifications in the case of the moduli space of algebraic surfaces, and there are many techniques that can be used to compactify it.
Among these, the natural analogue for surfaces of $M _ { g , n }$ originated from work of Koll´ar, Shepherd-Barron, and Alexeev (see [KSB88, Ale94, Ale96a, Ale96b] and [Fuj15, Kol09, Kol13a, KP15, HMX14] for recent developments), and it is usually referred to as the KSBA compactification.
This compactification has the advantage of being automatically functorial, and in particular gives a modular interpretation of the points of the boundary.
In addition, although the KSBA compactification depends on the choice of a divisor on the surfaces we want to study, it can be defined canonically provided there is a natural choice for this divisor.
The disadvantage is that in general the KSBA compactification is hard to study.
In addition, it is not known what to expect in terms of the structure of the boundary.
One of the difficulties comes from the substantial use of the Minimal Model Program (MMP), which also makes some results conjectural for moduli of varieties of dimension strictly greater than 2 (most difficulties with applying higher-dimensional MMP have been recently overcome).
Therefore, it is important to understand examples of such compactifications and build techniques that allow to get around these difficulties.

In this dissertation, we are interested in studying the KSBA compactification in the case of the moduli space of Enriques surfaces.
Enriques surfaces were introduced in 1896 and are very classical objects in algebraic geometry (see [Dol16] and references there).
The universal cover of an Enriques surface is a K3 surface, and compactifications of the moduli space of polarized K3 surfaces also received a lot of attention (see [Sca87, Sha80, Sha81, Laz16, AT15]).
More specifically, we consider a 4-dimensional family of Enriques surfaces which are called $D _ { 1 , 6 }$ -polarized, and we study its moduli compactifications in the context of Hodge theory, toric geometry, and MMP.
The interplay between these different points of view is the object of this dissertation (see Chapter 8).

# 1.2 Main results

$D _ { 1 , 6 }$ -polarized Enriques surfaces were considered in [Oud10].
$D _ { 1 , 6 }$ denotes the sublattice of $\mathbb { Z } \oplus \mathbb { Z } ^ { 6 } ( - 1 )$ of vectors of even square.
A $D _ { 1 , 6 }$ -polarization on an Enriques surface $S$ is a primitive embedding of $D _ { 1 , 6 }$ into $\mathrm { P i c } ( S )$ with some additional requirements (see Definition 8.2). More geometrically, an appropriate $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of the blow up of $\mathbb { P } ^ { 2 }$ at three general points branched along a configuration of three pairs of lines is an Enriques surface with two choices of $D _ { 1 , 6 }$ -polarization (see Proposition 8.8). Our choice of divisor consists of the ramification divisor multiplied by a rational number $\epsilon$ , $0 < \epsilon \ll 1$ .
Let $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ be the normalization of the closure in the coarse moduli space of stable surface pairs of the locus of points parametrizing these Enriques surfaces with our choice of divisor (the precise definition can be found in Section 8.1.5).

Theorem 1.1. The boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ has two divisorial components and one of codimension 3. For a full description of the stratification of the boundary and the degenerations parametrized by it, see Theorem 8.43.

Let us explain the techniques used to prove this result.
Denote by $\Delta$ the toric boundary of $( \mathbb { P } ^ { 1 } ) ^ { 3 }$ and let $B \subset ( \mathbb { P } ^ { 1 } ) ^ { \mathrm { 3 } }$ be a general effective divisor of class $( 1 , 1 , 1 )$ .
Then the $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of

$B$ branched along $\Delta | _ { B }$ is a $D _ { 1 , 6 }$ -polarized Enriques surface (see Proposition 8.14), and we can reduce our problem to considering the pairs $\left( B , \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) \Delta | _ { B } \right)$ (this is explained in Remark 8.11). The advantage of this setting is that if $Q$ denotes the unit cube, then $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , B )$ is a stable toric pair of type $\leq Q$ (see Definition 6.4), and therefore we can take advantage of the moduli theory for such pairs, which is developed in [Ale02].
Observe that given the stable toric pair $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , B )$ , then $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , \Delta + \epsilon B )$ is a stable pair (see [Ale06, Lemma 4.4]), which is not yet what we want.
Let $\overline { { M } } _ { Q } ^ { \nu }$ be the normalization of the projective coarse moduli space parametrizing $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , B )$ and its degenerations.
The next result summarizes Theorems 8.40 and 8.41.

Theorem 1.2. If $\operatorname { S y m } ( Q )$ denotes the symmetry group of $Q$ , then ${ \overline { { M } } } _ { Q } ^ { \nu } / \mathrm { S y m } ( Q ) \cong { \overline { { M } } } _ { D _ { 1 , 6 } } ^ { \nu }$ .
On a dense open subset, the isomorphism maps the Sym $( Q )$ -class of a stable toric pair $( X , B )$ to $\left( B , \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) \Delta | _ { B } \right)$ , where $\Delta$ denotes the toric boundary of $X$ .

One of the main problems in the proof of Theorem 1.2 is to compute the image of $( X , B )$ when $\left( B , \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) \Delta | _ { B } \right)$ is unstable, which happens if and only if the polyhedral subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ associated to $( X , B )$ has a corner cut (see Definition 8.22). This aspect is analyzed in Section 8.2, where we describe a modification of $( X , B )$ , which we denote by $( X ^ { \bullet } , B ^ { \bullet } )$ , such that $\left( B ^ { \bullet } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \Delta ^ { \bullet } | _ { B ^ { \bullet } } \right)$ is a stable pair.
Moreover, this modification can be performed in a oneparameter family.
At this point, given the isomorphism of Theorem 1.2, we can explicitly describe $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ because the moduli space $\overline { { M } } _ { Q } ^ { \nu }$ is the projective toric variety associated to the secondary polytope of $Q$ , and it is stratified according to the (regular) polyhedral subdivisions of $Q$ .

Consider the Baily-Borel compactification $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$ , where $\mathcal { D }$ is the period domain parametrizing $D _ { 1 , 6 }$ -polarized Enriques surfaces.
This compactification was studied in [Oud10], and its boundary has two rational 1-cusps and three 0-cusps.
The following theorem is proved in Section 8.5.

Theorem 1.3. There exists a birational morphism MνD1,6 → D/ΓBB e xtending the period map to the boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ (see Theorem 8.52).

In our case, proving that the period map extends is nontrivial because the boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ is not divisorial, and therefore we cannot make use of the standard extension criterion [BJ06, Corollary III.22.19].
Also in this case, we obtain the desired extension using one-parameter families.
To compute the limit of a one-parameter family in the Baily-Borel compactification, it is crucial to understand the Kulikov type of a KSBA degeneration of K3 surface pairs which are the double covers of our Enriques surface pairs.
This is studied in Section 8.5.1.

Label the 0-cusps of $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$ even, odd of type 1, and odd of type 2 (see Figure 8.7). We observe that the boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ has a toroidal behavior in a neighborhood of the preimage of the even 0-cusp, and is isomorphic to the Baily-Borel compactification in a neighborhood of the preimage of the odd 0-cusp of type 2. Above the odd 0-cusp of type 1 the behavior of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ is neither toroidal nor Baily-Borel.
These considerations make us consider Looijenga’s semitoric compactifications (see [Loo03]), which generalize the Baily-Borel and toroidal compactifications in the case of type IV Hermitian symmetric domains.
A semitoric compactification $\overline { { \mathcal { D } / \Gamma } } ^ { \Sigma }$ depends on a choice of combinatorial data $\Sigma$ called an admissible decomposition of the conical locus of $\mathcal { D }$ (see Definition 8.58). To construct $\Sigma$ in our case, for each 0-cusp we consider the associated hyperbolic lattice, and we compute a fundamental domain for the discrete reflection group generated by the reflections with respect to the $( - 1 )$ -vectors.
The computation at the odd 0-cusp of type 1 in Section 8.6.2 is noteworthy: Vinberg’s algorithm produces in one step an infinite Coxeter diagram (this also happens in [Con83]).
We obtain the following result.

Theorem 1.4. The admissible decomposition $\Sigma$ described in Definition 8.59 produces a semitoric compactification $\overline { { \mathcal { D } / \Gamma } } ^ { \Sigma }$ birational to $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ and whose boundary strata are in bijection with the boundary strata of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ .
This bijection preserves the dimensions of the strata and the intersections between them (see Theorem 8.67).

Motivated by these observations, we make the following conjecture, which will be object of further investigation.

Conjecture 1.5. The compactifications $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ and $\overline { { \mathcal { D } / \Gamma } } ^ { \Sigma }$ are isomorphic.

The double nature, namely toroidal and Baily-Borel, of the boundary of the moduli space $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ produced by the theory of stable pairs is remarkable: it illustrates the behavior one should expect in general when considering compactifications by stable pairs (see also [AT15, Remark 1.5]).

After reducing the problem to considering lines on the blow up of $\mathbb { P } ^ { 2 }$ at three general points, it is natural to ask whether the techniques in [Ale08, Ale15, AP09, Hu14] apply in our case.
The answer to this is no, and the reason is we do not allow any $( - 1 )$ -curve to be part of our chosen divisor, making our stable pairs not compatible with only considering lines in $\mathbb { P } ^ { 2 }$ (see Remark 8.12).

More connections and differences with the cited works are discussed in Remarks 8.5 and 8.72. A compact moduli space for del Pezzo surfaces using stable pairs was constructed in [HKT09], but in our case we have a different choice of the divisor.
Our work is also related to [Hac04] in the case of sextic plane curves, but here we consider the blow up of $\mathbb { P } ^ { 2 }$ .
Some of the techniques we use are closely related to [AT15] (for instance the use of stable toric pairs and polyhedral subdivisions).

The reason why we focused on this particular type of Enriques surface is the following.
$D _ { 1 , 6 } .$ - polarized Enriques surfaces come with a degree six polarization given by half the ramification locus of the $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover (this is the polarization which gives the classical construction of Enriques).
The techniques used in this dissertation can be generalized to describe a compactification by stable pairs of the entire 10-dimensional family of polarized Enriques surfaces of degree six.
This will be object of future work.

Chapter 8 is organized as follows.
In Section 8.1 we define the $D _ { 1 , 6 }$ -polarized Enriques surfaces and the surface pairs we want to study.
Here we also define our moduli spaces of interest: $\overline { { M } } _ { Q }$ and $M _ { D _ { 1 , 6 } }$ .
Section 8.2 is devoted to the definition of $( X ^ { \bullet } , B ^ { \bullet } )$ for a stable toric pair $( X , B )$ of type $\leq Q$ .
In Section 8.3 we prove that $\left( B ^ { \bullet } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \Delta ^ { \bullet } | _ { B ^ { \bullet } } \right)$ is stable for every stable toric pair $( X , B )$ of type $\leq Q$ .
In Section 8.4 we first construct a morphism $\overline { { M } } _ { Q } ^ { \nu }  \overline { { M } } _ { D _ { 1 , 6 } }$ , and then we prove the isomorphism $\overline { { { M } } } _ { Q } ^ { \nu } / \mathrm { S y m } ( Q ) \cong \overline { { { M } } } _ { D _ { 1 , 6 } } ^ { \nu }$ , which allows us to describe the stable pairs parametrized by the boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ and its stratification.
In Section 8.5 we relate $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ with the Baily-Borel compactification $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$ .
Finally, the connection with Looijenga’s semitoric compactifications is studied in Section 8.6.

# 1.3 Background

The background part of this dissertation is articulated in 6 chapters.
Chapter 2 is a brief introduction to lattice theory, and it includes the main definitions and notations.
Particular attention is devoted to the classification of indefinite unimodular lattices.
In Chapter 3 we consider the specific case of hyperbolic lattices, and we review Vinberg’s method to determine a fundamental domain for a given discrete reflection group.
In Chapter 4 we define K3 surfaces and Enriques surfaces.
We study their basic numerical invariants and geometric properties.
In particular, we classify the lattice $H ^ { 2 } ( S ; \mathbb { Z } )$ (resp.
$H ^ { 2 } ( S ; \mathbb { Z } )$ modulo torsion), where $S$ is a K3 surface (resp.
an Enriques surface).
In Chapter 5 we define the notion of secondary polytope, and we illustrate it with two examples: the Stasheff polytope and the secondary polytope of the unit cube.
In Chapter 6 we survey the theory of stable toric pairs and their moduli.
Chapter 7 is devoted to the study of stable pairs.
We start with the definition of weighted stable curve (which is the very first example of stable pair).
Then we review the definition of log canonical singularities and its extension to the non-normal case, i.e. semi-log canonical singularities.
After this, we define stable pairs and their corresponding Viehweg’s moduli functor.

We work over an arbitrary algebraically closed field k of characteristic zero, exception made for Sections 8.5 and 8.6 where we work over $\mathbb { C }$ .

# Chapter 2

# Lattice Theory

This chapter is a brief introduction to lattice theory, and it includes the main definitions and notations.
Particular attention is devoted to the classification of indefinite unimodular lattices.
Our main references are [BHPV04, Chapter I, Section 2] and [Ser73, Chapter V].

# 2.1 Basic definitions and facts

Definition 2.1. A lattice is a pair $( L , b _ { L } )$ , where $L$ is a free finitely generated $\mathbb { Z }$ -module and $b _ { L } \colon L \times L \to \mathbb { Z }$ is a symmetric bilinear form.
A lattice is usually denoted by its underlying $\mathbb { Z }$ - module $L$ .
Another lattice $L ^ { \prime } \subseteq L$ is a sublattice of $L$ if $b _ { L ^ { \prime } } = b _ { L } | _ { L ^ { \prime } \times L ^ { \prime } }$ .
Two lattices $L _ { 1 } , L _ { 2 }$ are isometric if there exists a $\mathbb { Z }$ -modules isomorphism $\varphi \colon L _ { 1 } \to L _ { 2 }$ such that $b _ { L _ { 2 } } ( \varphi ( a ) , \varphi ( b ) ) = b _ { L _ { 1 } } ( a , b )$ for all $a , b \in L _ { 1 }$ .
Such isomorphism $\varphi$ is called an isometry.

Definition 2.2. Let $L$ be a lattice and let $e _ { 1 } , \ldots , e _ { n }$ be a $\mathbb { Z }$ -basis for $L$ .
Then the Gram matrix of $L$ associated to the chosen $\mathbb { Z }$ -basis is the matrix $( b _ { L } ( e _ { i } , e _ { j } ) ) _ { 1 \leq i , j \leq n }$ .

Definition 2.3. Let $L$ be a lattice and let $M$ be a Gram matrix for $L$ .
Then we define the rank (resp.
discriminant, signature) of $L$ as the rank (resp.
determinant, signature) of $M$ .
These definitions do not depend on the choice of $M$ .
If $N$ is another Gram matrix for $L$ , then there exist an integral matrix $B$ with integral inverse such that $N = B ^ { t } M B$ .
Therefore, $N$ and $M$ have the same rank and signature.
In addition, $\operatorname* { d e t } ( N ) = \operatorname* { d e t } ( B ^ { t } ) \operatorname* { d e t } ( M ) \operatorname* { d e t } ( B ) = \operatorname* { d e t } ( B ) ^ { 2 } \operatorname* { d e t } ( M ) =$ $1 \cdot \operatorname* { d e t } ( M ) = \operatorname* { d e t } ( M )$ .
We denote the rank (resp.
discriminant) of $L$ as $\operatorname { r k } ( L )$ (resp.
$\mathrm { d i s c r } ( L ) ,$ ).
The signature of $M$ is denoted by $( t _ { + } , t _ { - } )$ , where $t _ { + }$ (resp.
$t _ { - }$ ) is the number of positive (resp.
negative) eigenvalues.
$L$ is indefinite if $t _ { + } , t _ { - } \ge 1$ .

Definition 2.4. Let $L$ be a lattice.
We say that $L$ is unimodular (resp.
nondegenerate) if $\mathrm { d i s c r } ( L ) =$ $\pm 1$ (resp.
$\mathrm { d i s c r } ( L ) \ne 0$ ).
Observe that if $L$ is nondegenerate, then its rank equals the rank of $L$ as a free $\mathbb { Z }$ -module.

Assumption.
In what follows we are concerned with nondegenerate lattices.
Therefore, when we consider a lattice, it is assumed to be nondegenerate.

Observation 2.5. Let $L$ be a (nondegenerate) lattice.
Then denote by $L ^ { * }$ its dual, i.e. ${ \mathrm { H o m } } _ { \mathbb { Z } } ( L , \mathbb { Z } )$ .
$L ^ { * }$ is naturally identified with

$$
\{ v \in L \otimes _ { \mathbb { Z } } \mathbb { Q } \mid b _ { L } ( v , w ) \in \mathbb { Z } { \mathrm { ~ f o r ~ a l l ~ } } w \in L \} .
$$

$L ^ { * }$ has a natural bilinear form with values in $\mathbb { Q }$ induced by $L$ , and it is called the dual lattice of $L$ .
(Observe that, strictly speaking, $L ^ { * }$ is not a lattice.
To be more rigorous, one can define a lattice to have the bilinear form defined over $\mathbb { Q }$ , and then call a lattice integral if its bilinear form is defined over $\mathbb { Z }$ .) Let $n = { \mathrm { r k } } ( L )$ and let $M$ be a Gram matrix for $L$ .
Then $L$ is isometric to $( \mathbb { Z } ^ { n } , M )$ and $L ^ { * }$ is generated over $\mathbb { Z }$ by the rows (or the columns) of $M ^ { - 1 }$ .
In particular, $\operatorname { r k } ( L ) = \operatorname { r k } ( L ^ { * } )$ and $\mathrm { d i s c r } ( L ^ { * } ) = 1 / \mathrm { d i s c r } ( L ) .$ .

Definition 2.6. Let $L$ be a lattice.
We define the discriminant group of $L$ as the abelian group $A _ { L } = L ^ { * } / L$ .

Lemma 2.7 ([BHPV04, Chapter I, (2.1) Lemma]).
Let L be a lattice.
Then the following hold:

(i) $| \mathrm { d i s c r } ( L ) | = | A _ { L } |$ (in particular, $A _ { L }$ is a finite group);

(ii) If $L ^ { \prime } \subset L$ is a sublattice of the same rank, then

$$
| L / L ^ { \prime } | ^ { 2 } = \mathrm { d i s c r } ( L ^ { \prime } ) / \mathrm { d i s c r } ( L ) .
$$

Definition 2.8. A lattice $L$ is said to be even if $b _ { L } ( a , a )$ is an even integer for all $a \in L$ .
Otherwise, we call $L$ an odd lattice.

# 2.2 Unimodular lattices

Examples 2.9. Denote by $I _ { n }$ the $n \times n$ identity matrix.
In what follows we give some fundamental examples of unimodular lattices.

(a) Let $p , q \in \mathbb { Z } _ { \geq 0 }$ .
Then denote by $\mathbb { Z } ^ { p , q }$ the lattice $\mathbb { Z } ^ { p + q }$ with the symmetric bilinear form given by the matrix

$$
\left( \frac { I _ { p } \ \biggr \vert \quad 0 } { 0 \ \biggr \vert \ - I _ { q } } \right) ,
$$

where the “ $0$ ” symbols denote zero matrices of appropriate dimensions.
Then $\mathbb { Z } ^ { p , q }$ is odd, unimodular, and of signature $( p , q )$ .

(b) The lattice $U = ( \mathbb { Z } ^ { 2 } , ( \mathbf { \Sigma } _ { 1 } ^ { 0 } \mathbf { \Sigma } _ { 0 } ^ { 1 } ) )$ is obviously even, unimodular, and of signature $( 1 , 1 )$ .

(c) The lattice $E _ { 8 }$ is given by $( \mathbb { Z } ^ { 8 } , B )$ , where

Observe that, if $A$ denotes the adjacency matrix of the $E _ { 8 }$ Dynkin diagram (see Figure 2.11), then $B = A - 2 I _ { 8 }$ .
One can check that the lattice $E _ { 8 }$ is even, unimodular, and of signature $( 0 , 8 )$ .

![](images/df56995457e70cdf817949dedf4bbe04fba0720ca2c73ba0b721df2288740d34.jpg)  
Figure 2.1: The $E _ { 8 }$ Dynkin diagram

The next theorem completely classifies indefinite unimodular lattices.

Theorem 2.10 ([Mil58, Theorem 1] or [Ser73, Chapter V, Theorem 6]).
Indefinite even (resp.
odd) unimodular lattices of the same signature are isometric.
More explicitly, up to isometry, the only indefinite unimodular lattices of signature $( p , q )$ , are given by

• $\mathbb { Z } ^ { p , q }$ (odd case);  
• $U ^ { \oplus p } \oplus E _ { 8 } ^ { \oplus ( q - p ) / 8 }$ if $p \leq q$ , or $U ^ { \oplus q } \oplus E _ { 8 } ( - 1 ) ^ { \oplus ( p - q ) / 8 }$ otherwise (even case).
(Given a lattice L and an integer $n$ , $L ( n )$ denotes the lattice $( L , n b _ { L } )$ .)

Example 2.11. Let $L$ be an even unimodular lattice of signature $( 2 , 1 0 )$ .
Then by Theorem 2.10 $L$ has to be isometric to $U ^ { \oplus 2 } \oplus E _ { 8 }$ .

Applications of this theorem to algebraic geometry can be found in Chapter 4.

# 2.3 The $D _ { p , q }$ lattice

Definition 2.12. Let $p , q \in \mathbb { Z } _ { \geq 0 }$ .
Then define the lattice $D _ { p , q }$ to be the sublattice of $\mathbb { Z } ^ { p , q }$ (see Examples 2.9 (a)) of vectors of even square.
Equivalently, $D _ { p , q }$ is the sublattice of $\mathbb { Z } ^ { p , q }$ of vectors of even sum of coordinates with respect to the canonical basis of $\mathbb { Z } ^ { p + q }$ .

Observation 2.13. $D _ { p , q }$ is by definition even and it has index 2 in $\mathbb { Z } ^ { p , q }$ (if $x \in \mathbb { Z } ^ { p , q }$ , then $2 x \in D _ { p , q }$ ).
Therefore, $D _ { p , q }$ and $\mathbb { Z } ^ { p , q }$ have the same signature.
Moreover, using Lemma 2.7 (ii), we have that

$$
\mathrm { d i s c r } ( D _ { p , q } ) = \mathrm { d i s c r } ( \mathbb { Z } ^ { p , q } ) \cdot | \mathbb { Z } ^ { p , q } / D _ { p , q } | ^ { 2 } = ( - 1 ) ^ { q } \cdot 2 ^ { 2 } = ( - 1 ) ^ { q } \cdot 4 .
$$

In particular, the discriminant group $A _ { D _ { p , q } }$ is isomorphic to $\mathbb { Z } _ { 4 }$ or $\mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 }$ (from what follows, we can see that both can occur as discriminant groups).

Definition 2.14. For $n \geq 4$ , denote by $D _ { n }$ the usual root lattice given by $\left( \mathbb { Z } ^ { n } , A - 2 I _ { n } \right)$ , where $A$ is the adjacency matrix of the $D _ { n }$ Dynkin diagram (see Figure 2.2). One can check that $D _ { n }$ is even, has signature $( 0 , n )$ , and $\operatorname { d i s c r } ( D _ { n } ) = ( - 1 ) ^ { n } \cdot 4$ .
In particular, it is well known that

$$
A _ { D _ { n } } \cong \left\{ \begin{array} { l l } { \mathbb { Z } _ { 4 } } & { \mathrm { i f ~ } n \mathrm { ~ i s ~ o d d , } } \\ { \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } } & { \mathrm { i f ~ } n \mathrm { ~ i s ~ e v e n . } } \end{array} \right.
$$

(See for instance [Ebe13, Section 1.4].) Equivalently, $D _ { n }$ is the sublattice of vectors of $\mathbb { Z } ^ { 0 , n }$ of even square, i.e. $D _ { n } = D _ { 0 , n }$ (this is the standard definition of $D _ { n }$ ).
It follows that the lattice $D _ { p , q }$ is the natural generalization of $D _ { n }$ to arbitrary signatures.

![](images/4713e2d4856c93a209725d7b9bb6400a182cf1427b67ee97eb467228a46a857e.jpg)  
Figure 2.2: The $D _ { n }$ Dynkin diagram

In Chapter 8 we are concerned with the lattice $D _ { 1 , 6 }$ .

Proposition 2.15. The lattice $D _ { 1 , 6 }$ has discriminant group $\mathbb { Z } _ { 4 }$ .

Proof.
Let $e _ { 0 } , \ldots , e _ { 6 }$ be the canonical basis for $\mathbb { Z } ^ { 7 }$ .
Then it is easy to check that $2 e _ { 0 } , e _ { 0 } - e _ { 1 } , \ldots , e _ { 0 } -$ $e _ { 6 }$ is a basis for $D _ { 1 , 6 }$ .
The vector $v = { \textstyle { \frac { 1 } { 2 } } } ( e _ { 0 } + \dots + e _ { 6 } )$ is an element of $D _ { 1 , 6 } ^ { * }$ by Observation 2.5. Since $2 v \notin D _ { 1 , 6 }$ , we can conclude that $v + D _ { 1 , 6 }$ has order 4 in $A _ { D _ { 1 , 6 } }$ .
Therefore, $A _ { D _ { 1 , 6 } } \cong \mathbb { Z } _ { 4 }$ .

Observe that Proposition 2.15 trivially follows from the following more general result.

Proposition 2.16. Let $p , q \in \mathbb { Z } _ { > 0 }$ with $p < q$ .
Then $D _ { p , q }$ is isometric to $U ^ { p } \oplus D _ { q - p }$ .

Proof.
The lattice $U ^ { p } \oplus D _ { q - p }$ is the sublattice of $U ^ { p } \oplus \mathbb { Z } ^ { 0 , q - p } \cong \mathbb { Z } ^ { p , q }$ of vectors of even square, and therefore it can be identified with $D _ { p , q }$ .
□

# Chapter 3

# Vinberg’s Algorithm

In this chapter we study discrete reflection groups for hyperbolic lattices.
In particular, we review Vinberg’s method to determine a fundamental domain for a given discrete reflection group.
The main reference for what follows is [Vin75].

# 3.1 Roots and reflections

Notation 3.1. In what follows, given a lattice $L$ and vectors $v , w \in L$ , we denote $b _ { L } ( v , w )$ (resp.  
$b _ { L } ( v , v ) ,$ ) simply by $v \cdot w$ (resp.
$v ^ { 2 }$ ).

Definition 3.2. Let $L$ be a lattice.
A root of $L$ is a vector $\alpha \in L$ such that $\alpha ^ { 2 } \neq 0$ and the fraction $2 ( \alpha \cdot v ) / \alpha ^ { 2 }$ is an integer for all $v \in L$ .

Example 3.3. Vectors $\alpha \in L$ such that $\alpha ^ { 2 } = \pm 1 , \pm 2$ are examples of roots.
We call $( - 1 )$ -vector (resp.
$\left( - 2 \right)$ -vector ) a vector $\alpha$ such that $\alpha ^ { 2 } = - 1$ (resp.
$\alpha ^ { 2 } = - 2$ ).

The roots of a lattice $L$ can be used to define special isometries of $L$ called reflections.

Definition 3.4. If $\alpha \in L$ is a root, then the map $r _ { \alpha } \colon L \to L$ given by

$$
v \mapsto v - 2 { \frac { \alpha \cdot v } { \alpha ^ { 2 } } } \alpha ,
$$

is an isometry of $L$ called reflection with respect to $\alpha$ .
Observe that $r _ { \alpha } \circ r _ { \alpha } = \mathrm { i d } _ { L }$ and $r _ { \alpha } ( \alpha ) = - \alpha$ .
The hyperplane $\alpha ^ { \perp } \otimes _ { \mathbb { Z } } \mathbb { R }$ in $L _ { \mathbb { R } } = L \otimes _ { \mathbb { Z } } \mathbb { R }$ is called the mirror of the reflection $r _ { \alpha }$ , and we denote it by $H _ { \alpha }$ .

Definition 3.5. Let $O ( L )$ denote the group of isometries of $L$ .
Then a subgroup of $O ( L )$ generated by reflections is called a reflection group for $L$ .

# 3.2 Hyperbolic lattices and hyperbolic spaces

Definition 3.6. Let $L$ be a lattice.
We say that $L$ is hyperbolic if it has signature $( 1 , n )$ for some positive integer $n$ .

Definition 3.7. Let $L$ be a hyperbolic lattice and endow $L _ { \mathbb { R } }$ with the euclidean topology.
Then the subset $\{ x \in L _ { \mathbb { R } } \mid x \cdot x > 0 \} \subset L _ { \mathbb { R } }$ has two connected components.
Let $C$ be one of these two components, and denote by $\overline { C }$ its closure in $L _ { \mathbb { R } }$ .
We call $\overline { C }$ a light cone.

Definition 3.8. Let $L$ be a hyperbolic lattice.
Then the quotient $\Lambda ( L ) = C / \mathbb { R } _ { > 0 }$ is called hyperbolic space.
$\Lambda ( L )$ is compactified by $\Lambda ( L ) = ( \overline { { C } } \setminus \{ 0 \} ) / \mathbb { R } _ { > 0 }$ , and the points we add are called points at infinity.

Definition 3.9. Let $L$ be a hyperbolic lattice and let $\alpha \in { \cal L }$ be a root such that $\alpha ^ { 2 } < 0$ .
Then $H _ { \alpha }$ has nonempty intersection with $C$ , hence it defines a hyperplane in the hyperbolic space $\Lambda ( L )$ given by $h _ { \alpha } = ( H _ { \alpha } \cap C ) / \mathbb { R } _ { > 0 }$ .
If we have another such hyperplane $h _ { \beta } \subset \Lambda ( L )$ , we say that $h _ { \alpha }$ and $h _ { \beta }$ are

• adjacent if $h _ { \alpha } \cap h _ { \beta } \neq \emptyset$ ;  
• parallel if $\overline { { h } } _ { \alpha } , \overline { { h } } _ { \beta } \subset \Lambda ( L )$ intersect at a point at infinity;  
• divergent if $\overline { { h } } _ { \alpha } \cap \overline { { h } } _ { \beta } = \emptyset$ .

If the hyperplanes are adjacent, then the angle between them is equal to $\pi / m$ , where

$$
\cos \left( { \frac { \pi } { m } } \right) = { \frac { \alpha \cdot \beta } { \sqrt { \alpha ^ { 2 } \beta ^ { 2 } } } } .
$$

# 3.3 Fundamental domains and Coxeter diagrams

Definition 3.10. Let $\Gamma$ be a discrete reflection group for a hyperbolic lattice $L$ .
Then the mirrors of the reflections in $\Gamma$ decompose the hyperbolic space $\Lambda ( L )$ into convex polyhedra which are in the same $\Gamma$ -orbit.
A fundamental domain for $\Gamma$ is the choice of one of these convex polyhedra.

Definition 3.11. Let $\Gamma$ be a discrete reflection group for a hyperbolic lattice $L$ .
Then we can construct a graph $G ( \Gamma )$ as follows.
Choose a fundamental domain for $\Gamma$ and let $\mathcal { X }$ be the set of hyperplanes in $\Lambda ( L )$ which bound it.

• Let $\{ v _ { \alpha } \mid h _ { \alpha } \in \mathcal { X } \}$ be the set of vertices of $G ( \Gamma )$ ;

• An edge between $v _ { \alpha } , v _ { \beta }$ is determined as follows.
Consider $h _ { \alpha } , h _ { \beta } \in \mathcal { X }$ .

– If $h _ { \alpha } , h _ { \beta }$ are adjacent and the angle between them is $\pi / m$ with $m \neq 2$ , then draw an edge between $v _ { \alpha }$ and $v _ { \beta }$ labeled by $m - 2$ ; $-$ If $h _ { \alpha } , h _ { \beta }$ are parallel, then draw an edge between $v _ { \alpha }$ and $v _ { \beta }$ labeled by $\infty$ ; $-$ If $h _ { \alpha } , h _ { \beta }$ are divergent, then draw a dotted edge between $v _ { \alpha }$ and $v _ { \beta }$ .

The graph $G ( \Gamma )$ obtained this way is called the Coxeter diagram of $\Gamma$ .

Definition 3.12. Let $G ( \Gamma )$ as in Definition 3.11 and let $G$ be a connected subdiagram of $G ( \Gamma )$ .
Then $G$ is called elliptic if the corresponding Gram matrix is definite.
If $G$ has $t$ vertices, then $G$ is called parabolic if the corresponding Gram matrix is semidefinite of rank $t - 1$ .
A subdiagram of $G ( \Gamma )$ is called elliptic (resp.
parabolic) if all its connected components are such.

# 3.4 Algorithm to determine a fundamental domain

Fix a hyperbolic lattice $L$ of signature $( 1 , n )$ and let $\Gamma = \langle r _ { \alpha } \mid \alpha \in \mathcal { R } \rangle$ be a discrete reflection group, where $\mathcal { R } \subset L$ consists of roots of negative square.
In [Vin75], Vinberg gives an algorithm to determine a fundamental domain $P$ for $\Gamma$ .
(We are interested in running Vinberg’s algorithm to produce interesting decompositions of light cones, and we use these decompositions in Chapter 8 to construct compactifications of certain moduli spaces.)

Description of the algorithm.

• Preparation: Fix a vector $v _ { 0 }$ in the light cone $\overline { C }$ .
From the set $\{ \alpha \in \mathcal { R } \mid v _ { 0 } \cdot \alpha = 0 \}$ choose a subset $S _ { 0 }$ of fundamental roots.
Let $n = 1$ .

• Step: Define

$S _ { n } = S _ { n - 1 } \cup \{ \alpha \in \mathcal { R } \mid v _ { 0 } \cdot \alpha = n$ and $\alpha \cdot \beta \geq 0$ for all $\beta \in S _ { n - 1 } \}$ .

Then let $n = n + 1$ and repeat Step.

Then the hyperplanes $h _ { \alpha }$ for $\alpha \in \cup _ { n \geq 0 } S _ { n }$ bound a fundamental domain $P$ for the $\Gamma$ -action.

Definition 3.13. We say that Vinberg’s algorithm finishes if there exists $\overline { { n } } ~ \in ~ \mathbb { Z } _ { \ge 0 }$ such that $S _ { n } = S _ { \overline { { n } } }$ for all $n > \pi$ .
It is possible that the algorithm does not finish.

# 3.5 Stopping criterion

Vinberg gives a criterion to recognize if the algorithm is finished at a given step $n$ .

Observation 3.14. First observe that, if the hyperplanes $h _ { \alpha }$ for $\alpha \in S _ { n }$ bound a polyhedron $P _ { n }$ of finite volume, then $P _ { n }$ equals the fundamental domain $P$ (see [Vin75, Section 2.4]).

Theorem 3.15 ([Vin75, Theorem 2.6 bis]).
Assume $G ( \Gamma )$ contains no dotted edges and no Lanner’s subdiagrams (these are listed in [Vin75, Table 3]).
Then $P$ has finite volume if and only if every connected parabolic subdiagram of $G ( \Gamma )$ is a connected component of some parabolic subdiagram of rank $n - 1$ .

Let us explain how to use Theorem 3.15 as a stopping criterion.
At step $n$ of Vinberg’s algorithm, draw the Coxeter diagram for the discrete reflection group generated by the reflections $r _ { \alpha }$ for $\alpha \in S _ { n }$ .
Then Theorem 3.15 tells us whether $P _ { n }$ has finite volume.
If it does, then $P = P _ { n }$ by Observation 3.14, and the algorithm finishes.
If $P _ { n }$ does not have finite volume, then we continue with the algorithm.

Examples 3.16. Let $L$ be a hyperbolic lattice and let $\Gamma$ be the discrete reflection group generated by the reflections with respect to the $( - 1 )$ -vectors.
In Section 8.6.2 we run Vinberg’s algorithm and we compute the Coxeter diagram of $\Gamma$ for $L = \mathbb { Z } ^ { 1 , 3 }$ and $L = \mathbb { Z } ^ { 1 , 1 } \oplus \mathbb { Z } ^ { 2 } ( - 2 )$ (recall that $\mathbb { Z } ^ { p , q }$ denotes the unique odd unimodular lattice of signature $( p , q )$ ).

# Chapter 4

# K3 Surfaces and Enriques Surfaces

In this chapter we define K3 surfaces and Enriques surfaces.
We study their basic numerical invariants and geometric properties.
In particular, we classify the lattice $H ^ { 2 } ( S ; \mathbb { Z } )$ (resp.
$H ^ { 2 } ( S ; \mathbb { Z } )$ modulo torsion), where $S$ is a K3 surface (resp.
an Enriques surface).
Our main references are [BHPV04, Bea96, GH94].

# 4.1 Basic definitions and notations

A variety is a connected and reduced scheme of finite type over our fixed base field k.
A surface is a 2-dimensional smooth projective variety.
Given a surface $S$ , we briefly recall the following notation and definitions:

• $p _ { g } ( S ) = h ^ { 0 } ( S , \omega _ { S } )$ is the geometric genus;  
• $q ( S ) = h ^ { 1 } ( S , { \mathcal { O } } _ { S } )$ is the irregularity;  
• $\kappa ( S )$ is the Kodaira dimension;  
• $b _ { i } ( S ) = \operatorname { r k } ( H ^ { \ i } ( S ; \mathbb { Z } ) )$ is the $i$ -th Betti number ;  
• $\begin{array} { r } { \chi _ { \mathrm { t o p } } ( S ) = \sum _ { i = 0 } ^ { 4 } ( - 1 ) ^ { i } b _ { i } ( S ) } \end{array}$ is the topological Euler characteristic.
This is equal to $2 - 2 b _ { 1 } ( S ) +$ $b _ { 2 } ( S )$ by Poincar´e duality (see [GH94, Chapter 0, Section 4]);  
• $\mathrm { N S } ( S ) = \mathrm { P i c } ( S ) / \mathrm { P i c } ^ { 0 } ( S )$ is the N´eron-Severi group;  
• $\mathrm { N u m } ( S ) = \mathrm { N S } ( S ) / \equiv$ , where “≡” denotes numerical equivalence.

Observation 4.1. In this chapter we are concerned with surfaces $S$ with $K _ { S } \equiv 0$ .
This condition automatically implies that $S$ is minimal, which means that $S$ does not contain a $( - 1 )$ -curve (i.e. a curve $E \subset S$ isomorphic to $\mathbb { P } ^ { 1 }$ such that $E ^ { 2 } = - 1$ ).
To show this, assume $E \subset S$ is a $( - 1 )$ -curve.
Then [Bea96, I.15 The genus formula] implies that

$$
p _ { g } ( E ) = 0 = 1 + { \frac { - 1 + E \cdot K _ { S } } { 2 } } \implies E \cdot K _ { S } = - 1 ,
$$

which is a contradiction.

# 4.2 K3 surfaces

Definition 4.2. A K3 surface is a surface $S$ such that $K _ { S } \sim 0$ (so that $p _ { g } ( S ) = 1$ ) and $q ( S ) = 0$ .

Example 4.3. The simplest example of a K3 surface is the following.
Let $S$ be a smooth quartic hypersurface in $\mathbb { P } ^ { 3 }$ .
Then $K _ { S } \sim 0$ by adjunction formula.
To show that $q ( S ) = 0$ , consider the short exact sequence

$$
0 \to \mathcal { O } ( - 4 ) \to \mathcal { O } \to \mathcal { O } _ { S } \to 0 ,
$$

where we set $\mathcal { O } = \mathcal { O } _ { \mathbb { P } ^ { 3 } }$ .
Consider the associated long exact sequence in cohomology

$$
\dots \to H ^ { 1 } ( \mathbb { P } ^ { 3 } , { \mathcal { O } } ) \to H ^ { 1 } ( S , { \mathcal { O } } _ { S } ) \to H ^ { 2 } ( \mathbb { P } ^ { 3 } , { \mathcal { O } } ( - 4 ) ) \to \dots
$$

Since $H ^ { 1 } ( \mathbb { P } ^ { 3 } , { \mathcal { O } } )$ and $H ^ { 2 } ( \mathbb { P } ^ { 3 } , { \mathcal { O } } ( - 4 ) )$ are both isomorphic to $\{ 0 \}$ , we conclude that $H ^ { 1 } ( S , { \mathcal { O } } _ { S } ) \cong \{ 0 \}$ .  
Therefore $S$ is a K3 surface.

Example 4.4. Let $S \subset ( \mathbb { P } ^ { 1 } ) ^ { 3 }$ be a multidegree $( 2 , 2 , 2 )$ smooth hypersurface.
We have that $K _ { S } \sim 0$ by adjunction formula.
Consider the short exact sequence

$$
0 \to \mathcal { O } ( - 2 , - 2 , - 2 ) \to \mathcal { O } \to \mathcal { O } _ { S } \to 0 ,
$$

where we set $\mathcal { O } = \mathcal { O } _ { ( \mathbb { P } ^ { 1 } ) ^ { 3 } }$ .
Consider the associated long exact sequence in cohomology

$$
\begin{array} { r } { \dots \to H ^ { 1 } ( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , \mathcal { O } ) \to H ^ { 1 } ( S , \mathcal { O } _ { S } ) \to H ^ { 2 } ( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , \mathcal { O } ( - 2 , - 2 , - 2 ) ) \to \dots } \end{array}
$$

By Kodaira vanishing theorem (see [Har77, Chapter III, Remark 7.15]), we obtain that

$$
H ^ { 1 } ( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , \mathcal { O } ) \cong \{ 0 \} , \ H ^ { 2 } ( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , \mathcal { O } ( - 2 , - 2 , - 2 ) ) \cong \{ 0 \} ,
$$

hence $q ( S ) = 0$ and $S$ is a K3 surface.

Proposition 4.5. Let $S$ be a K3 surface.
Then $S$ is minimal, $\kappa ( S ) = 0$ , $b _ { 1 } ( S ) = 0$ , $b _ { 2 } ( S ) = 2 2$ , $h ^ { 1 , 1 } = 2 0$ , and $\pi _ { 1 } ( S ) = \{ 1 \}$ .

Proof.
$S$ is minimal by Observation 4.1. $\kappa ( S ) = 0$ follows by the definition of Kodaira dimension together with $K _ { S } \sim 0$ .
Using [Bea96, Fact III.19], we have that $b _ { 1 } ( S ) = 2 q ( S ) = 0$ .
By Noether’s formula (see [Bea96, I.14]), we have that

$$
\chi _ { \mathrm { t o p } } ( S ) = 1 2 \chi ( \mathcal { O } _ { S } ) = 2 4 = 2 b _ { 0 } ( S ) - 2 b _ { 1 } ( S ) + b _ { 2 } ( S ) \implies b _ { 2 } ( S ) = 2 2 .
$$

The Hodge decomposition (see [GH94, Chapter 0, Section 7]) tells us that

$$
H ^ { 2 } ( { \cal S } ; \mathbb { C } ) \cong H ^ { 2 , 0 } ( { \cal S } ) \oplus H ^ { 1 , 1 } ( { \cal S } ) \oplus H ^ { 0 , 2 } ( { \cal S } ) .
$$

Therefore, $H ^ { 1 , 1 } ( S )$ is 20-dimensional because $H ^ { 2 , 0 } ( S ) , H ^ { 0 , 2 } ( S )$ are both 1-dimensional and we just proved that $b _ { 2 } ( S ) = 2 2$ .
To conclude, all K3 surfaces are diffeomorphic to each other (see [BHPV04, Chapter VIII, (8.6) Corollary]).
In particular, $S$ is diffeomerphic to a quartic hypersurface in $\mathbb { P } ^ { 3 }$ (see Example 4.3), which is simply-connected by the Lefschetz hyperplane theorem (see [GH94, Chapter 1, Section 2]).
□

Proposition 4.6 ([Huy16, Chapter 1, Proposition 2.4]).
Let $S$ be a K3 surface.
Then the natural surjections $\operatorname { P i c } ( S ) \to \operatorname { N S } ( S ) \to \operatorname { N u m } ( S )$ are isomorphisms.

Proof.
First, consider the exponential short exact sequence

$$
0 \to \mathbb { Z } _ { S } \to \mathcal { O } _ { S } \to \mathcal { O } _ { S } ^ { * } \to 0 ,
$$

where $\underline { { \mathbb { Z } } } _ { S }$ denotes the constant sheaf of stalk $\mathbb { Z }$ on $S$ .
Recall that $H ^ { 1 } ( S , { \mathcal { O } } _ { S } ^ { * } ) \cong \operatorname { P i c } ( S )$ (see [Har77, Chapter III, Exercise 4.5]).
Looking at the associated long exact sequence in cohomology

$$
\begin{array} { r } { \ldots \to H ^ { 1 } ( S , { \mathcal { O } } _ { S } ) \to \operatorname { P i c } ( S ) \to H ^ { 2 } ( S ; \mathbb { Z } ) \to H ^ { 2 } ( S , { \mathcal { O } } _ { S } ) \to \ldots , } \end{array}
$$

we obtain that $\mathrm { P i c } ( S )$ is isomorphic to the image of $c _ { 1 }$ in $H ^ { 2 } ( S ; \mathbb { Z } )$ , which is $\mathrm { N S } ( S )$ .

To see that $\operatorname { P i c } ( S ) \to \operatorname { N u m } ( S )$ is an isomorphism, assume by contradiction there exists a nontrivial line bundle ${ \mathcal { L } } \in \operatorname { P i c } ( S )$ which is numerically trivial.
Let $\mathcal { M }$ be an ample line bundle on $S$ .
Then we have that $\mathcal { L } \cdot \mathcal { M } = 0$ .
Consider the linear system $| { \mathcal { L } } |$ and assume it is not empty.
Since ${ \mathcal { L } } \ { \mathcal { Z } } \ { \mathcal { O } } _ { S }$ , we can find a nonzero effective divisor $E \in \ | { \mathcal { L } } |$ .
This implies that $\mathcal { L } \cdot \mathcal { M } = E \cdot \mathcal { M } > 0$ , which cannot be.
Hence $| { \mathcal { L } } | = \emptyset$ and $h ^ { 0 } ( { \mathcal { L } } ) = 0$ .
Similarly, we can argue that $h ^ { 2 } ( { \mathcal { L } } ) = h ^ { 0 } ( { \mathcal { L } } ^ { - 1 } ) = 0$ .
By Riemann-Roch formula (see [Bea96, Theorem I.12]), we have that

$$
2 + \frac { 1 } { 2 } \mathcal { L } \cdot \mathcal { L } = \chi ( \mathcal { L } ) = - h ^ { 1 } ( \mathcal { L } ) \leq 0 .
$$

This implies that $\mathcal { L } \cdot \mathcal { L } < 0$ , which is a contradiction.
Therefore, the map $\operatorname { P i c } ( S ) \to \operatorname { N u m } ( S )$ is an isomorphism.

To conclude, we showed that $\operatorname { P i c } ( S ) \to \operatorname { N S } ( S )$ and $\operatorname { P i c } ( S ) \to \operatorname { N u m } ( S )$ are isomorphism, hence also $\mathrm { N S } ( S ) \to \mathrm { N u m } ( S )$ is.
□

Proposition 4.7. Let $S$ be a $K 3$ surface.
Then $H ^ { 2 } ( S ; \mathbb { Z } ) , \smile )$ is a lattice isometric to ${ U } ^ { \oplus 3 } \oplus { E } _ { 8 } ^ { \oplus 2 }$ , which is called the K3 lattice.

Proof.
By the universal coefficient theorem for cohomology (see [Hat02, Theorem 3.2]) we have that

$$
\begin{array} { r } { H ^ { 2 } ( S ; \mathbb { Z } ) \cong \operatorname { H o m } _ { \mathbb { Z } } ( H _ { 2 } ( S ; \mathbb { Z } ) , \mathbb { Z } ) \oplus \operatorname { E x t } _ { \mathbb { Z } } ^ { 1 } ( H _ { 1 } ( S ; \mathbb { Z } ) , \mathbb { Z } ) . } \end{array}
$$

The homology group $H _ { 1 } ( S ; \mathbb { Z } )$ is isomorphic to $\{ 0 \}$ because $H _ { 1 } ( S ; \mathbb { Z } )$ is the abelianization of $\pi _ { 1 } ( S ) \cong$ $\{ 0 \}$ (see Proposition 4.5). Therefore $H ^ { 2 } ( S ; \mathbb { Z } ) \cong \operatorname { H o m } _ { \mathbb { Z } } ( H _ { 2 } ( S ; \mathbb { Z } ) , \mathbb { Z } )$ , which tells us that $H ^ { 2 } ( S ; \mathbb { Z } )$ is torsion free.
We can conclude that $H ^ { 2 } ( S ; \mathbb { Z } )$ is isomorphic to $\mathbb { Z } ^ { 2 2 }$ as a $\mathbb { Z }$ -module because $b _ { 2 } ( S ) = 2 2$ by Proposition 4.5. The lattice $( H ^ { 2 } ( S ; \mathbb { Z } ) , \smile )$ , which is obviously nondegenerate, is unimodular by Poincar´e duality and even by Wu’s formula (see [MS74]).
Finally, let $( t _ { + } , t _ { - } )$ be the signature of $( H ^ { 2 } ( S ; \mathbb { Z } ) , \smile )$ .
Then the Hodge-Riemann bilinear relations (see [GH94, Chapter 0, Section 7])

imply that

$$
t _ { + } - t _ { - } = \sum _ { p + q \mathrm { ~ i s ~ e v e n } } ( - 1 ) ^ { p } h ^ { p , q } = h ^ { 0 , 0 } + h ^ { 2 , 0 } - h ^ { 1 , 1 } + h ^ { 0 , 2 } + h ^ { 2 , 2 } = - 1 6 .
$$

Since $t _ { + } + t _ { - } = 2 2$ , we argue that $( t _ { + } , t _ { - } ) = ( 3 , 1 9 )$ .
We can conclude that $H ^ { 2 } ( S ; \mathbb { Z } )$ is isometric to ${ \cal U } ^ { \oplus 3 } \oplus { \cal E } _ { 8 } ^ { \oplus 2 }$ by Theorem 2.10. □

# 4.3 Enriques surfaces

Definition 4.8. An Enriques surface is a surface $S$ such that $2 K s \sim 0$ and $p _ { g } ( S ) = q ( S )$ .

Proposition 4.9. Let $S$ be an Enriques surface.
Then $S$ is minimal, $\kappa ( S ) = 0$ , $p _ { g } ( S ) = q ( S ) = 0$ , $K _ { S } \nsim 0$ , $b _ { 1 } ( S ) = 0$ , and $b _ { 2 } ( S ) = 1 0$ .

Proof.
$S$ is minimal by Observation 4.1. $\kappa ( S ) = 0$ follows by the definition of Kodaira dimension because $P _ { n } ( S ) = 1$ for $n$ even and $P _ { n } ( S ) \leq 1$ for $n$ odd (by contradiction, if $P _ { n } ( S ) > 1$ for $n$ odd, then $P _ { 2 n } ( S ) > 1$ ).
By the classification of surfaces of Kodaira dimension 0 (see [Bea96, Theorem VIII.2]), the only possibility is $p _ { g } ( S ) = q ( S ) = 0$ .
In particular, $K _ { S } \nsim 0$ , otherwise $p _ { g } ( S ) = 1$ .
The first Betti number $b _ { 1 } ( S )$ is equal to $2 q ( S ) = 0$ .
Noether’s formula gives that $1 2 = 2 b _ { 0 } ( S ) - 2 b _ { 1 } ( S ) + b _ { 2 } ( S )$ , hence $b _ { 2 } ( S ) = 1 0$ .
□

Proposition 4.10. Let $S$ be an Enriques surface and let $\pi \colon X  S$ be the ´etale double cover corresponding to the 2-torsion sheaf $\omega _ { S }$ .
Then $X$ is a $K \mathcal { 3 }$ surface.
In particular, the universal cover of $S$ is a $K \mathcal { 3 }$ surface with a fixed-point-free involution and $\pi _ { 1 } ( S ) \cong \mathbb { Z } _ { 2 }$ .
Conversely, the quotient of a K3 surface $X$ by a fixed-point-free involution is an Enriques surface.

Proof.
First observe that $\omega _ { X } = \pi ^ { * } \omega _ { S } = \mathcal { O } _ { X }$ .
Moreover, $\chi _ { \mathrm { t o p } } ( X ) = 2 \chi _ { \mathrm { t o p } } ( S ) = 2 4$ , implying that $\chi ( \mathcal { O } _ { X } ) = 2 = 1 - q ( X ) + p _ { g } ( X )$ .
In conclusion, $q ( X ) = 0$ and $X$ is a K3 surface.
$X$ is the universal cover of $S$ because $X$ is simply connected.
Since $\pi$ has degree 2, we have that $\pi _ { 1 } ( S )$ has cardinality 2, hence $\pi _ { 1 } ( S ) \cong \mathbb { Z } _ { 2 }$ .

For the converse, let $\iota \colon X \to X$ be a fixed-point-free involution and denote by $S$ the quotient $X / \iota$ .
Let $\pi \colon X  S$ be the quotient map.
$\chi _ { \mathrm { t o p } } ( S ) = { \textstyle \frac { 1 } { 2 } } \chi _ { \mathrm { t o p } } ( X ) = 1 2$ , hence $\chi ( \mathcal { O } _ { S } ) = 1$ , which implies that $p _ { g } ( S ) = q ( S )$ .
Finally, ${ \mathcal O } _ { X } = \omega _ { X } = \pi ^ { * } \omega _ { S }$ , which gives $\omega _ { S } ^ { \otimes 2 } = \pi _ { * } \pi ^ { * } \omega _ { S } = \pi _ { * } \mathcal { O } _ { X } = \mathcal { O } _ { S }$ .
Therefore, $S$ is an Enriques surface.
□

Example 4.11. Let $X$ be the vanishing locus in $( \mathbb { P } ^ { 1 } ) ^ { 3 }$ of the following multidegree $( 2 , 2 , 2 )$ equation:

$$
\sum _ { \begin{array} { l } { { i , j , k = 0 , 1 , 2 } } \\ { { i + j + k \equiv 0 ( \bmod ~ 2 ) } } \end{array} } d _ { i j k } X _ { 0 } ^ { 2 - i } X _ { 1 } ^ { i } Y _ { 0 } ^ { 2 - j } Y _ { 1 } ^ { j } Z _ { 0 } ^ { 2 - k } Z _ { 1 } ^ { k } .
$$

For a general choice of the coefficients $d _ { i j k }$ , we can assume that $X$ is smooth.
By Example 4.4 we know that $X$ is a K3 surface.
The involution $( \mathbb { P } ^ { 1 } ) ^ { 3 } \to ( \mathbb { P } ^ { 1 } ) ^ { 3 }$ given by

$$
\left( [ X _ { 0 } : X _ { 1 } ] , [ Y _ { 0 } : Y _ { 1 } ] , [ Z _ { 0 } : Z _ { 1 } ] \right) \mapsto \left( [ X _ { 0 } : - X _ { 1 } ] , [ Y _ { 0 } : - Y _ { 1 } ] , [ Z _ { 0 } : - Z _ { 1 } ] \right) ,
$$

restricts to an involution $\iota \colon X \to X$ , which is fixed-point-free if we assume the coefficients of the monomials $X _ { a } ^ { 2 } Y _ { b } ^ { 2 } Z _ { c } ^ { 2 }$ , $a , b , c \in \{ 0 , 1 \}$ , to be nonzero.
Under this assumption, $X / \iota$ is an Enriques surface by Proposition 4.10.

Proposition 4.12. For an Enriques surface $S$ , we have that the natural maps $\operatorname { P i c } ( S ) \to \operatorname { N S } ( S ) \hookrightarrow$ $H ^ { 2 } ( S ; \mathbb { Z } )$ are isomorphisms.

Proof.
Considering the long exact sequence in cohomology associated to the exponential short exact sequence

$$
\begin{array} { r } { \ldots \to H ^ { 1 } ( S , { \mathcal { O } } _ { S } ) \to \operatorname { P i c } ( S ) \to H ^ { 2 } ( S ; \mathbb { Z } ) \to H ^ { 2 } ( S , { \mathcal { O } } _ { S } ) \to \ldots , } \end{array}
$$

we obtain the claimed isomorphisms because $p _ { g } ( S ) = q ( S ) = 0$ .

Observation 4.13. For an Enriques surface $S$ , we have that $\operatorname { N u m } ( S ) \not \cong \operatorname { P i c } ( S )$ because $\omega _ { S } \equiv 0$ , but $\omega _ { S } \not \cong { \mathcal { O } } _ { S }$ .

Proposition 4.14. Let $S$ be an Enriques surface.
Then the torsion part $T$ of $H ^ { 2 } ( S ; \mathbb { Z } )$ is isomorphic to $\mathbb { Z } _ { 2 }$ , and the quotient $H ^ { 2 } ( S ; \mathbb { Z } ) _ { f } = H ^ { 2 } ( S ; \mathbb { Z } ) / T$ endowed with the cup product is a lattice isometric to $U \oplus E _ { 8 }$ , which is called the Enriques lattice.

Proof.
By the universal coefficient theorem for cohomology we have that

$$
\begin{array} { r } { H ^ { 2 } ( S ; \mathbb { Z } ) \cong \operatorname { H o m } _ { \mathbb { Z } } ( H _ { 2 } ( S ; \mathbb { Z } ) , \mathbb { Z } ) \oplus \operatorname { E x t } _ { \mathbb { Z } } ^ { 1 } ( H _ { 1 } ( S ; \mathbb { Z } ) , \mathbb { Z } ) . } \end{array}
$$

The homology group $H _ { 1 } ( S ; \mathbb { Z } )$ is isomorphic to $\mathbb { Z } _ { 2 }$ because $H _ { 1 } ( S ; \mathbb { Z } )$ is the abelianization of $\pi _ { 1 } ( S ) \cong$ $\mathbb { Z } _ { 2 }$ (see Proposition 4.10). Therefore, since $b _ { 2 } ( S ) ~ = ~ 1 0$ , we have that $H ^ { 2 } ( S ; \mathbb { Z } ) \cong \mathbb { Z } ^ { 1 0 } \oplus \mathbb { Z } _ { 2 }$ ,

showing that $T \cong \mathbb { Z } _ { 2 }$ .
The $\mathbb { Z }$ -module $H ^ { 2 } ( S ; \mathbb { Z } ) _ { f }$ endowed with the cup product is a nondegenerate unimodular lattice of rank 10. It is also even by the Riemann-Roch formula: any class $C \in$ $H ^ { 2 } ( S ; \mathbb { Z } ) _ { f }$ is algebraic because $\operatorname { P i c } ( S ) \cong H ^ { 2 } ( S ; \mathbb { Z } )$ (see Proposition 4.12), and hence

$$
\chi ( \mathcal { O } _ { S } ( C ) ) = \chi ( \mathcal { O } _ { S } ) + \frac { 1 } { 2 } ( C ^ { 2 } - C \cdot K _ { S } ) \implies C ^ { 2 } ~ \mathrm { i s ~ e v e n } .
$$

The signature of $H ^ { 2 } ( S ; \mathbb { Z } ) _ { f }$ is $( 1 , 9 )$ by the Hodge-Riemann bilinear relations, or by the Hodge index theorem (see [BHPV04, Chapter IV, (2.16) Corollary]).
In conclusion, $H ^ { 2 } ( S ; \mathbb { Z } ) _ { f }$ is isometric to $U \oplus E _ { 8 }$ by Theorem 2.10.

# 4.4 Half-fibers and the canonical class of an Enriques surface

Proposition 4.15. Let $S$ be an Enriques surface and let $f \colon S \to \mathbb { P } ^ { 1 }$ be a genus 1 pencil.
Then (i) $f$ has exactly two multiple fibers, and their multiplicities are equal to 2;

(ii) If $F _ { 1 } , F _ { 2 }$ are these double fibers, then $K _ { S } \sim F _ { 1 } - F _ { 2 }$ .

Proof.
The following proof is taken from [BHPV04, Chapter VIII, (17.1) Lemma].
Let $F _ { 1 } , \ldots , F _ { k }$ be the multiple fibers of $f$ , and assume they have multiplicities $r _ { 1 } , \ldots , r _ { k } \ge 2$ respectively.
If $p$ is a general point in $\mathbb { P } ^ { 1 }$ , then the formula for the canonical class of a genus 1 fibration (see [BHPV04, Chapter V, (12.3) Corollary]) gives that

$$
K _ { S } \sim f ^ { * } ( - p ) + \sum _ { i = 1 } ^ { k } ( r _ { i } - 1 ) F _ { i } .
$$

But $K _ { S }$ is 2-torsion, therefore

$$
0 \sim f ^ { * } ( - 2 p ) + \sum _ { i = 1 } ^ { k } ( 2 r _ { i } - 2 ) F _ { i } .
$$

Fix an arbitrary $j \in \{ 1 , \ldots , k \}$ .
Restricting (4.2) to $F _ { j }$ , we obtain that

$$
0 \sim ( 2 r _ { j } - 2 ) F _ { j } | _ { F _ { j } } .
$$

Since $F _ { j } | _ { F _ { j } }$ has order $r _ { j }$ (see [BHPV04, Chapter II, (8.3) Lemma]), we have that $r _ { j } \ | \ ( 2 r _ { j } - 2 )$ .
This implies that $( 2 - h ) r _ { j } = 2$ for $h = 0$ or $1$ .
But $r _ { j } > 1$ , so $h = 1$ and $r _ { j } = 2$ .
We conclude that $r _ { 1 } , \ldots , r _ { k } = 2$ , because $j$ was arbitrary.
In particular, (4.2) becomes

$$
0 \sim f ^ { * } ( - 2 p ) + \sum _ { i = 1 } ^ { k } 2 F _ { i } \implies f ^ { * } ( 2 p ) = f ^ { * } ( k p ) \implies k = 2 ,
$$

which completes the proof of (i).
To prove (ii), now (4.1) gives that

$$
K _ { S } \sim f ^ { * } ( - p ) + F _ { 1 } + F _ { 2 } ,
$$

which combined with $f ^ { * } ( p ) \sim 2 F _ { 2 }$ implies that $K _ { S } \sim F _ { 1 } - F _ { 2 }$ .

Definition 4.16. The fibers $F _ { 1 } , F _ { 2 }$ of Proposition 4.15 are called the half-fibers of the genus 1 pencil f : S → P1.

# Chapter 5

# Convex Geometry and the Secondary Polytope

In this chapter we define the notion of secondary polytope, and we illustrate it with two examples: the Stasheff polytope and the secondary polytope of the unit cube.
Our main references are [GKZ08, DLRS10].

# 5.1 Basic definitions in convex geometry

Definition 5.1. Let $A$ be a subset of $\mathbb { R } ^ { k }$ .
Then the convex hull of $A$ is the intersection of all the closed half-spaces containing $A$ .
Using open half-spaces instead gives the same result.

Definition 5.2. A polytope $Q \subset \mathbb { R } ^ { k }$ is the convex hull of a given finite set of points $A \subset \mathbb { R } ^ { k }$ .
The pair $( Q , A )$ is called marked polytope.

Definition 5.3. Let $Q \subset \mathbb { R } ^ { k }$ be a polytope, $H \subset \mathbb { R } ^ { k }$ an affine hyperplane, and denote by $H ^ { + } , H ^ { - }$ its corresponding open half spaces.
Assume that $Q \cap H ^ { - } = \emptyset$ and $Q \cap H \neq \emptyset$ .
Then we call $Q \cap H$ a face of $Q$ .
The polytope $Q$ itself is considered a face of $Q$ .
The faces of $Q$ are also polytopes.
The vertices of $Q$ are the faces of $Q$ that consist of a single point.

Definition 5.4. Let $Q \subset \mathbb { R } ^ { k }$ be a polytope, and let $v _ { 0 }$ be one of its vertices.
Then define the dimension of $Q$ , which we denote by $\dim ( Q )$ , as the dimension of the $\mathbb { R }$ -vector space spanned by the vectors $v - v _ { 0 }$ as $v$ varies among the vertices of $Q$ .
This definition is independent from the choice of $v _ { 0 }$ .

Observation 5.5. Let $Q \subset \mathbb { R } ^ { k }$ be a polytope and let $F$ be one of its faces.
Then $0 \leq \dim ( F ) \leq$ $\dim ( Q ) \leq k$ , and $F ^ { \prime }$ is a vertex if and only if $\dim ( F ) = 0$ .

Definition 5.6. Given a polytope, the faces of dimension 1 are called edges.
Codimension 1 faces are called facets.

Definition 5.7. Let $Q$ be a polytope.
If $\dim ( Q ) = \# { \mathrm { v e r t i c e s } } - 1$ , then $Q$ is called a simplex.

# 5.2 Polyhedral subdivisions

Definition 5.8. A polyhedral subdivision of a given a marked polytope $( Q , A )$ is a finite collection $\mathcal { Q } = \{ Q _ { i } \} _ { i }$ of polytopes such that:

• $\cup _ { i } Q _ { i } = Q$ ;  
• $Q _ { i } \cap Q _ { j }$ is either empty, or a face of both $Q _ { i }$ and $Q _ { j }$ for all $i , j$ ;  
• The vertices of $Q _ { i }$ are contained in $A$ for all $i$ ;  
• If $Q _ { i } \in \mathcal { Q }$ and $F$ is a face of $Q _ { i }$ , then $F \in \mathcal { Q }$ .

A polyhedral subdivision which only uses simplices is called triangulation.
See Figure 5.1 for some concrete examples.

![](images/997ade43011e053b196c958363f5ffc2ee276974137d3215ed867fdf5c37c244.jpg)  
Figure 5.1: On the left an example of triangulation.
On the right a non-example of polyhedral subdivision

Definition 5.9. Let $( Q , A )$ be a marked polytope with $Q \subset \mathbb { R } ^ { k }$ and let $h \colon A \to \mathbb { R }$ be a function (we call $h$ a height function on $A$ ).
Let $Q ^ { + } \subset \mathbb { R } ^ { k } \times \mathbb { R }$ be the convex hull of the half lines $( a , h ( a ) +$ $\mathbb { R } _ { \geq 0 }$ ) for $a \ \in \ A$ .
The images of the faces of $Q ^ { + }$ under the projection $\mathbb { R } ^ { k } \times \mathbb { R }  \mathbb { R } ^ { k }$ give a polyhedral subdivision of $( Q , A )$ , which we call the polyhedral subdivision induced by the height function h.
Figure 5.2 illustrates this construction for a one-dimensional marked polytope.
A polyhedral subdivision of $( Q , A )$ is regular if it is induced by some height function on $A$ .
In the literature, regular subdivisions are sometimes also called coherent or convex.

![](images/eb38a350c7fe99f89e32fe101f28eb65bca532ae3bf946a49ac5b13390deabef.jpg)  
Figure 5.2: Polyhedral subdivision of $Q$ induced by a height function $h$

Example 5.10. The simplest example of polyhedral subdivision which is not regular is given in Figure 5.3. To show this subdivision is not regular, assume by contradiction it is induced by a height function $h$ .
We can assume without loss of generality that $h ( a _ { 4 } ) = h ( a _ { 5 } ) = h ( a _ { 6 } ) = 0$ because the polytope with vertices $a _ { 4 } , a _ { 5 } , a _ { 6 }$ is part of the subdivision.
We have that $h ( a _ { 1 } ) > 0$ , otherwise we would not see the edge with vertices $a _ { 1 } , a _ { 4 }$ .
Observe that $h ( a _ { 1 } ) \neq h ( a _ { 2 } )$ , otherwise we would not have the edge with vertices $a _ { 2 } , a _ { 4 }$ .
Therefore, assume that $h ( a _ { 1 } ) > h ( a _ { 2 } )$ (a similar argument holds for the opposite inequality).
But the symmetry of the figure implies that $h ( a _ { 2 } ) > h ( a _ { 3 } ) > h ( a _ { 1 } )$ , which is a contradiction.

![](images/b679a7f883d126f474be84974936b08d2cfbe00c09ce7c1b9a8166a447e184a1.jpg)  
Figure 5.3: Example of nonregular polyhedral subdivision

# 5.3 The secondary polytope

Let $( Q , A )$ be a marked polytope and assume $Q \subset \mathbb { R } ^ { k }$ is nondegenerate (i.e. $\dim ( Q ) = k$ ).
We are ready to define the secondary polytope of the marked polytope $( Q , A )$ .
Let ${ \mathcal { T } } = \{ Q _ { i } \} _ { i }$ be a triangulation of $( Q , A )$ .
Then define

$$
\varphi _ { \mathcal { T } } \colon A \to \mathbb { R }  \\  a \mapsto \sum _ { \substack { a \colon \ : a \in Q _ { i } \mathrm { ~ i s ~ a ~ v e r t e x } } } \mathrm { V o l } ( Q _ { i } ) .
$$

Observe that, if $A = \{ a _ { 1 } , \ldots , a _ { n } \}$ , then $\varphi _ { T }$ can be identified with the point $( \varphi _ { \mathcal { T } } ( a _ { 1 } ) , \ldots , \varphi _ { \mathcal { T } } ( a _ { n } ) )$ in $\mathbb { R } ^ { | A | }$ .

Definition 5.11. The secondary polytope $\Sigma ( A )$ of the marked polytope $( Q , A )$ is the convex hull of the set $\{ \varphi \tau \vert \mathcal { T }$ is a triangulation of $( Q , A ) \} \subset \mathbb { R } ^ { | A | }$ .
If $A$ coincide with the set of vertices of $Q$ , then we denote $\Sigma ( A )$ by $\Sigma ( Q )$ instead.

Theorem 5.12 ([GKZ08, Chapter 7, Theorem 1.7]).
Let $( Q , A )$ be a marked polytope.
Then

$$
\dim ( \Sigma ( A ) ) = | A | - \dim ( Q ) - 1 .
$$

Theorem 5.13 ([GKZ08, Chapter 7, Theorem 2.4]).
The faces of the secondary polytope $\Sigma ( A )$ are in bijection with the regular subdivisions of $( Q , A )$ .
Moreover, containment of faces of $\Sigma ( A )$ corresponds to refinement of subdivisions of $( Q , A )$ .
In particular, the vertices of $\Sigma ( A )$ correspond to the regular triangulations of $( Q , A )$ .

Example 5.14. One of the first interesting examples of secondary polytopes is the Stasheff polytope.
For $n \geq 3$ , let $A _ { n }$ be the set of vertices of a planar $n$ -gon.
Then, the $n$ -th Stasheff polytope is the secondary polytope $\Sigma ( A _ { n } )$ .
It is easy to observe that $\Sigma ( A _ { 3 } )$ is a point, $\Sigma ( A _ { 4 } )$ is a segment, and $\Sigma ( A _ { \mathrm { 5 } } )$ is a planar pentagon (see Figure 5.4). For $n \geq 6$ , the $n$ -th Stasheff polytope is more complicated.
We just remark that $\Sigma ( A _ { n } )$ has dimension $n - 3$ by Theorem 5.12, and $\textstyle { \frac { 1 } { n - 1 } } { \binom { 2 n - 4 } { n - 2 } }$ vertices (see [GKZ08, Chapter 7, Section 3, B]).

![](images/b9e4977015042997348c1ab55618cc33f5cc3b0e5364124fab42824ba5b93b30.jpg)  
Figure 5.4: The Stasheff polytopes $\Sigma ( A _ { n } )$ for $n = 3 , 4 , 5$

# 5.4 Polyhedral subdivisions of the unit cube

In this section we fix $Q$ to be the unit cube $[ 0 , 1 ] ^ { 3 } \subset \mathbb { R } ^ { 3 }$ .
The marking of $Q$ is chosen to be its set of vertices $Q \cap \mathbb { Z } ^ { 3 }$ (and therefore it is omitted).
Let us enumerate all the possible polyhedral subdivisions of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ .

We start by listing all the possible subpolytopes of $Q$ with vertices in $Q \cap \mathbb { Z } ^ { 3 }$ .
These are represented in Figure 5.5 with the corresponding lattice volume.
For a nondegenerate polytope $P \subset \mathbb { R } ^ { k }$ , recall that the lattice volume of $P$ is defined to be $k ! \cdot \operatorname { V o l } ( P )$ .
We can combine the polytopes in Figure 5.5 to form a subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ , knowing that the sum of the lattice volumes of the polytopes chosen has to be 6.

A complete list of all the possible polyhedral subdivisions of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ up to symmetry can be found in Figure 5.6. A polyhedral subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ is represented by a graph whose vertices correspond to the maximal dimensional polytopes in the subdivision and there is an edge between two vertices if and only if the corresponding polytopes share a facet.
When this graph is not enough to distinguish two distinct polyhedral subdivisions, we associate a number to each vertex which represents the number of facets of the corresponding polytope.
If this is not enough, instead we draw a dotted edge between two vertices if the corresponding polytopes share an edge and not a facet.
The sum in the top left corner of each box in Figure 5.6 represents the lattice volume of the polytopes used in the subdivisions.
In the next proposition we observe that all these subdivisions are regular.

# Proposition 5.15. All the polyhedral subdivisions of the unit cube $Q$ are regular.

Proof.
We know from [San01, Corollary 2.9] that a marked polytope with a nonregular subdivision has a nonregular triangulation.
But all the triangulations of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ are regular (see [DL96, Theorem 3.2] or [DLRS10, Theorem 6.3.10]).
These triangulations are pictured in Figure 5.7 up to symmetry with a corresponding height function.
□

For more information about $\Sigma ( Q )$ , we refer to [Pfe00].
Here we just observe that $\Sigma ( Q )$ has dimension 4 and 74 vertices (the number of vertices can easily be counted from Figure 5.7). The secondary polytope $\Sigma ( Q )$ has an important role in Chapter 8.

![](images/a43c87da8555839d668871685164d1b3a9626961db1b99a741a9fa0cca535ab5.jpg)  
Figure 5.5: List of all the possible subpolytopes of $Q$ up to symmetry with vertices in $Q \cap \mathbb { Z } ^ { 3 }$ and their corresponding lattice volume

![](images/17b77e872a30ee6e97dc049c67a99e5e39d7157062b5245993c0b5834de64e59.jpg)  
Figure 5.6: List of all the polyhedral subdivisions of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ , $Q = [ 0 , 1 ] ^ { 3 }$ , up to symmetry

![](images/c6e6a403aa17656a66fba6b59f49d8c21f9e4cb543fec6a27dc605a9e36d6d63.jpg)  
Figure 5.7: The triangulations of the unit cube $Q$ up to symmetry and a corresponding height functions on the vertices.
This figure is a reproduction of [DLRS10, Figure 1.33])

# Chapter 6

# Moduli of Stable Toric Pairs

In this chapter we survey the theory of stable toric pairs and their moduli.
Our main references are [Ale02, Ale06, Ale15].

# 6.1 Stable toric pairs

For us, a variety is a connected and reduced scheme of finite type over an arbitrary algebraically closed field k of characteristic zero (in particular, a variety need not be irreducible).
$T$ denotes a fixed (split) torus over k and let $M$ be its character lattice.
$M _ { \mathbb { R } }$ denotes the tensor product $M \otimes _ { \mathbb { Z } } \mathbb { R }$ .
We want to remark that the theory of stable toric pairs we are about to review works in any characteristic.

Definition 6.1. Let $X$ be a variety with a $T$ -action.
We say that $X$ is a stable toric variety if $X$ is seminormal and its irreducible components are toric varieties under the $T$ -action.
The toric boundary of a stable toric variety is defined to be the sum of the boundary divisors of each irreducible component which are not in common with other irreducible components.
If $X$ is projective and $\mathcal { L }$ is an ample and $T$ -linearized invertible sheaf on $X$ , we say that the pair $( X , { \mathcal { L } } )$ is a polarized stable toric variety.

Remark 6.2. Assume we have a polarized stable toric variety $( X , { \mathcal { L } } )$ .
Then we can associate to each irreducible component $X _ { i }$ of $X$ a lattice polytope $P _ { i }$ .
These polytopes can be glued to one another in the same way as $X$ is the union of its irreducible components.
This results into a topological space $\cup _ { i } P _ { i }$ which is called the topological type of $X$ .
The topological type comes together with a finite map $\cup _ { i } P _ { i }  M _ { \mathbb { R } }$ , called the reference map, which embeds each $P _ { i }$ as a lattice polytope in $M _ { \mathbb { R } }$ .
The set of the faces of all the polytopes $P _ { i }$ , together with the identifications coming from the gluing, forms what is called a complex of polytopes.
Up to isomorphism, there is a 1-to-1 correspondence between polarized stable toric varieties (for a fixed torus $T$ ) and the following data:

(a) A complex of polytopes $_ { \mathcal { P } }$ ;  
(b) A reference map $\cup _ { P \in \mathcal { P } } P \to M _ { \mathbb { R } }$ ;  
(c) An element of the cohomology group we are about to describe.
For each $P \in \mathcal { P }$ , let $C _ { P }$ be the saturated sublattice of $\mathbb { Z } \oplus M$ generated by $( 1 , P )$ , and let $T _ { P }$ be the torus $\mathrm { H o m } ( C _ { P } , \mathbb { k } ^ { * } )$ .
The tori $T _ { P }$ for $P \in \mathcal { P }$ define a sheaf $\underline { { T } }$ of abelian groups on the poset $\mathcal { P }$ with the order topology.
So we want to consider an element of $H ^ { 1 } ( \mathcal { P } , \underline { { T } } )$ , which describes the way the irreducible components of $X$ are glued together.

For more details about this, see [Ale06, Section 4.3] or [Ale02, Theorem 1.2.6].

Definition 6.3. Let $( X , { \mathcal { L } } )$ be a polarized stable toric variety and let $Q \subset M _ { \mathbb { R } }$ be a lattice polytope.
We say that $X$ has type $\leq \ Q$ if the complex of polytopes $\mathcal { P }$ associated to $X$ is a polyhedral subdivision of the marked polytope $( Q , Q \cap M )$ .
Observe that in this case the reference map is implicitly given by the inclusion of $Q$ in $M _ { \mathbb { R } }$ .
Furthermore, the toric boundary of $X$ is given by the sum of the divisors corresponding to the facets in $\mathcal { P }$ contained in the boundary of $Q$ .

Definition 6.4. A stable toric pair is the datum of a polarized stable toric variety $( X , { \mathcal { L } } )$ together with an effective Cartier divisor $B$ which is the divisor of zeros of a global section of $\mathcal { L }$ .
Also, we require that $B$ does not contain any torus fixed point (or equivalently any $T$ -orbit).
We denote a stable toric pair simply by $( X , B )$ because it is understood that ${ \mathcal { L } } \cong { \mathcal { O } } _ { X } ( B )$ .
Two stable toric pairs $( X , B )$ and $( X ^ { \prime } , B ^ { \prime } )$ are isomorphic if there exists an isomorphism $f \colon X \to X ^ { \prime }$ that preserves the $T$ -action and such that $f ^ { * } B ^ { \prime } = B$ .
We say that a stable toric pair has type $\leq Q$ if the corresponding polarized stable toric variety has type $\leq Q$ .

Remark 6.5. Let $( X , B )$ be a stable toric pair and let $\mathcal { P }$ be the complex of polytopes corresponding to the polarized stable toric variety $( X , { \mathcal { O } } _ { X } ( B ) )$ .
If $X _ { i }$ is any irreducible component of $X$ , then the restriction $B | _ { X _ { i } }$ can be described combinatorially as follows (see [Ale02, Theorem 1.2.7] in combination with [Ale02, Lemma 2.2.7, part 2]).
Consider the marking on the corresponding lattice polytope $P _ { i }$ given by $P _ { i } \cap M$ .
Observe that these lattice points in $P _ { i }$ correspond to monomials (recall that $M$ is the character lattice of the fixed torus $T$ ).
Now, $B | _ { X _ { i } }$ is determined (not uniquely) by a function $f \colon P _ { i } \cap M \to \mathbb { k } ^ { * }$ , which assigns to each monomial a corresponding coefficient (which we want to be nonzero because $B$ does not contain any torus fixed point).

# 6.2 The stack of stable toric pairs

By $\mathbf { S c h } _ { \mathbb { k } }$ we denote the category of locally noetherian schemes over our fixed base field $\Bbbk$ .

Definition 6.6. Given $S \in \mathrm { O b } ( \mathbf { S c h } _ { \mathbb { k } } )$ , a family of stable toric pairs $( { \mathfrak { X } } , { \mathfrak { B } } ) / S$ is the datum of a proper and flat morphism of schemes $\pi \colon { \mathfrak { X } }  S$ , a compatible $T _ { S } = T \times _ { \mathbb { k } } S$ action on $\boldsymbol { \mathcal { X } }$ , and an effective Cartier divisor $\mathfrak { B } \subset \mathfrak { X }$ such that $\pi | _ { \mathfrak { B } }$ is flat and the fiber $( { \mathfrak { X } } _ { s } , { \mathfrak { B } } _ { s } )$ over every geometric point $s  S$ is a stable toric pair with the action induced by $T _ { S }$ .
Two families of stable toric pairs over the same base are isomorphic if there exists an isomorphism of pairs over $S$ preserving the torus action.
Given a lattice polytope $Q$ , we say that a family of stable toric pairs has $t y p e \le Q$ if every geometric fiber has type $\leq Q$ .

Remark 6.7. Let $( { \mathfrak { X } } , { \mathfrak { B } } ) / S$ be a family of stable toric pairs.
Denote by $\pi$ the morphism ${ \mathfrak { X } } \to S$ and let ${ \mathcal { L } } = { \mathcal { O } } _ { \mathfrak { X } } ( \mathfrak { B } )$ .
Following [Ale02, Proof of Lemma 2.10.1], for $d \geq 0$ the sheaves $\pi _ { * } \mathcal { L } ^ { \otimes d }$ are locally free, and the torus action gives a decomposition $\pi _ { * } { \mathcal { L } } ^ { \otimes d } = \bigoplus _ { m \in M } R _ { ( d , m ) }$ into sheaves that are also locally free.
This results into a locally free $( \mathbb { Z } \oplus M )$ -graded $\mathcal { O } _ { S }$ -algebra $R = \oplus _ { ( d , m ) \in \mathbb { Z } \oplus M } R _ { ( d , m ) }$ together with a $\mathbb { Z }$ -degree 1 section $\theta$ of $R$ corresponding to $\mathfrak { B }$ .
Conversely a pair $( R , \theta )$ , where $R$ is a locally free graded $\mathcal { O } _ { S }$ -algebra and $\theta$ a degree 1 section, uniquely determines a family of stable toric pairs up to isomorphism (see [Ale02, Proof of Theorem 2.10.8] or [Ale06, Section 4]).

Remark 6.8. After defining families of stable toric pairs we automatically have a notion of stack over k.
Given a lattice polytope $Q$ , denote by $\mathcal { M } _ { Q }$ the category of families of stable toric pairs of type $\leq Q$ , where a morphism $f = ( f _ { t } , f _ { b } ) \colon ( { \mathfrak { X } } ^ { \prime } , { \mathfrak { B } } ^ { \prime } ) / S ^ { \prime } \to ( { \mathfrak { X } } , { \mathfrak { B } } ) / S$ is a pullback diagram

$$
\begin{array} { c } { { ( { \mathfrak { X ^ { \prime } } } , { \mathfrak { B ^ { \prime } } } ) \xrightarrow { f _ { t } } ( { \mathfrak { X } } , { \mathfrak { B } } ) } } \\ { { \downarrow } } \\ { { S ^ { \prime } \xrightarrow [ f _ { b } ] { } { } S . } } \end{array}
$$

Let $\mathcal { M } _ { Q }  \mathbf { S } \mathbf { c h } _ { \mathbb { k } }$ be the functor sending $( { \mathfrak { X } } , { \mathfrak { B } } ) / S$ to $S$ and a morphism $f$ to $f _ { b }$ .
Then $\mathcal { M } _ { Q }$ is a stack over k parametrizing families of stable toric pairs of type $\leq Q$ .

The main result about the stack $\mathcal { M } _ { Q }$ is the following theorem due to Alexeev.

Theorem 6.9 ([Ale02, Theorem 1.2.15]).
Let $Q$ be a lattice polytope and let $\mathcal { M } _ { Q }$ be the stack of stable toric pairs of type $\leq Q$ .
Then the following hold:

(i) $\mathcal { M } _ { Q }$ is a proper quotient stack (and therefore an Artin stack) with finite stabilizers1;  
(ii) It has a coarse moduli space $\overline { { M } } _ { Q }$ which is a projective scheme;  
(iii) $\overline { { M } } _ { Q }$ is naturally stratified, and every stratum corresponds in a 1-to-1 way to a polyhedral subdivision of $( Q , Q \cap M )$ ;  
(iv) The normalization of the main irreducible component of $( { \overline { { M } } } _ { Q } ) _ { \mathrm { r e d } }$ is isomorphic to the toric variety associated to the secondary polytope $\Sigma ( Q \cap M )$ .

Remark 6.10. In Theorem 6.9 (iv), one could define the main irreducible component of $( M _ { Q } ) _ { \mathrm { r e d } }$ as the irreducible component of $( \overline { { M } } _ { Q } ) _ { \mathrm { r e d } }$ satisfying the claimed property.
Equivalently, the main irreducible component can be characterized by the fact that on a dense open subset it parametrizes stable toric pairs whose corresponding polyhedral subdivision of $( Q , Q \cap M )$ is the trivial one.

# 6.3 An explicit computation

The goal of this section is to explicitly compute a cohomology group $H ^ { 1 } ( \mathcal { P } , \underline { { T } } )$ for a given polytope $Q$ and polyhedral subdivision $\mathcal { P }$ (this is explained in Remark 6.2). The example we analyze is fundamental later in Chapter 8.

Theorem 6.11. Let $Q$ be the unit cube and let $_ { \mathcal { P } }$ be a polyhedral subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ .
Then $H ^ { 1 } ( \mathcal { P } , \underline { { T } } ) = \{ 1 \}$ .

To prove Theorem 6.11 we need some general preliminaries.

Observation 6.12. Let $_ { \mathcal { P } }$ be a complex of polytopes obtained by gluing finitely many polytopes $\{ P _ { i } \} _ { i \in I }$ of the same dimension.
Let $\cup _ { P \in \mathcal P P } P \to M _ { \mathbb { R } }$ be a reference map.
Recall that $\Lambda _ { P _ { i } }$ (which 1Since we are working in characteristic $_ 0$ , we have that ${ \mathcal { M } } _ { Q }$ is actually a Deligne-Mumford stack.

we denote for brevity $\Lambda _ { i }$ ) is the saturated sublattice of $\mathbb { Z } \oplus M$ generated by $( 1 , P _ { i } )$ .
For any $\{ i _ { 1 } , \dotsc , i _ { s } \} \subset I$ , let $\Lambda _ { i _ { 1 } . . . i _ { s } }$ be the intersection $\Lambda _ { i _ { 1 } } \cap \ldots \cap \Lambda _ { i _ { s } }$ .
An element of $H ^ { 1 } ( \mathcal { P } , \underline { { T } } )$ is a tuple $( \dots , t _ { i j } , \dots )$ indexed by pairs in $I$ , with $t _ { i j } \in \mathrm { H o m } ( \Lambda _ { i j } , \mathbb { k } ^ { * } )$ satisfying the cocycle condition and modulo coboundaries.
The cocycle condition is the following: if $i , j , k \in I$ is any triple, then

$$
t _ { i j } | _ { \Lambda _ { i j k } } t _ { j k } | _ { \Lambda _ { i j k } } = t _ { i k } | _ { \Lambda _ { i j k } } .
$$

A coboundary is a tuple $\big ( \dots , t _ { i } \big | _ { \Lambda _ { i j } } t _ { j } \big | _ { \Lambda _ { i j } } ^ { - 1 } , \dots \big )$ for $t _ { i } \in \mathrm { H o m } ( \Lambda _ { i } , \mathbb { k } ^ { * } )$ and $t _ { j } \in \mathrm { H o m } ( \Lambda _ { j } , \Bbbk ^ { * } )$ .
Therefore, we have an equivalence relation on the cocycles given by

$$
\big ( . . . , t _ { i j } , . . . \big ) \sim \big ( . . . , t _ { i j } t _ { i } | _ { \Lambda _ { i j } } ^ { - 1 } t _ { j } \big | _ { \Lambda _ { i j } } , . . . \big ) .
$$

Lemma 6.13. Let $\mathcal { P }$ be a connected complex of polytopes obtained by gluing finitely many polytopes of the same dimension.
Let $P$ be one of these polytopes and assume $P$ has exactly one facet in common with some other maximal dimensional polytope in $\mathcal { P }$ .
Let ${ \mathcal { P } } ^ { \prime }$ be the complex of polytopes obtained from $\mathcal { P }$ by eliminating $P$ .
Then $H ^ { 1 } ( \mathcal { P } , \underline { { T } } ) \cong H ^ { 1 } ( \mathcal { P } ^ { \prime } , \underline { { T } } )$ .

Proof.
Label $P$ by 1 and the polytope adjacent to $P$ by 2. Consider an arbitrary cocycle $c =$ $( t _ { 1 2 } , \ldots )$ .
Let $t _ { 1 } \in \mathrm { H o m } ( \Lambda _ { 1 } , \mathbb { k } ^ { * } )$ be such that $t _ { 1 } | _ { \Lambda _ { 1 2 } } = t _ { 1 2 }$ (observe that there can be different choices for $t _ { 1 }$ ).
If we consider the coboundary $( t _ { 1 } | _ { \Lambda _ { 1 2 } } 1 | _ { \Lambda _ { 1 2 } } ^ { - 1 } , 1 , . . . )$ , then $c \sim ( 1 , \ldots )$ , giving the required isomorphism.
□

Definition 6.14. Let $P$ be a polytope as in the statement of Lemma 6.13. We call $P$ a hanging polytope of $\mathcal { P }$ .

Lemma 6.15. Let $\mathcal { P }$ be a connected complex of polytopes obtained by gluing finitely many polytopes $\{ P _ { i } \} _ { i = 1 } ^ { n }$ of the same dimension.
Assume that all these polytopes share a fixed face of codimension 2 and that they are organized around it as follows: for $i = 1 , \ldots , n - 1$ , $P _ { i }$ and $P _ { i + 1 }$ share a facet, and also $P _ { 1 }$ and $P _ { n }$ do.
Then $H ^ { 1 } ( \mathcal { P } , \underline { { T } } ) = \{ 1 \}$ .

Proof.
Let $c = ( t _ { 1 2 } , t _ { 2 3 } , \ldots , t _ { n - 1 , n } , t _ { n 1 } )$ be a cocycle and consider a coboundary with $t _ { n } | _ { \Lambda _ { n 1 } } = t _ { n 1 }$ and the other $t _ { i }$ equal to 1. Then $c \sim ( t _ { 1 2 } ^ { \prime } , t _ { 2 3 } ^ { \prime } , \ldots , t _ { n - 1 , n } ^ { \prime } , 1 )$ .
We can iterate this strategy until we obtain $c \sim ( \tau , 1 , \dots , 1 )$ for some $\tau \in \mathrm { H o m } ( \Lambda _ { 1 2 } , \mathbb { K } ^ { * } )$ .
Now consider a coboundary with $t _ { 1 } | _ { \Lambda _ { 1 2 } } = \tau$ , $t _ { 1 } | _ { \Lambda _ { n 1 } } = 1$ and the other $t _ { i }$ equal to $^ 1$ .
This makes sense because $\tau | _ { \Lambda _ { n 1 2 } } = 1$ by the cocycle condition on $( \tau , 1 , \dots , 1 )$ .
We can conclude that $c \sim ( \tau , 1 , \dots , 1 ) \sim ( 1 , \dots , 1 )$ .

proof of Theorem 6.11. Let $\mathcal { P }$ be any polyhedral subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ where $Q$ is the unit cube.
Applying Lemma 6.13, we can reduce our problem to compute $H ^ { 1 } ( \mathcal { P } ^ { \prime } , \underline { { T } } )$ with ${ \mathcal { P } } ^ { \prime }$ without hanging polytopes (see Definition 6.14). After enumerating all the possibilities for $\mathcal { P }$ , one can observe that either ${ \mathcal { P } } ^ { \prime }$ is generated by a single maximal dimensional polytope, or it is as in the statement of Lemma 6.15. In both cases, we can conclude that $H ^ { 1 } ( \mathcal { P } , \underline { { T } } ) \cong H ^ { 1 } ( \mathcal { P } ^ { \prime } , \underline { { T } } ) \cong \{ 1 \}$ .
The complete list of all the possibilities for $\mathcal { P }$ is in Figure 5.6 (see Section 5.4). □

# Chapter 7

# Moduli of Stable Pairs

This chapter is devoted to the study of stable pairs.
We start with the definition of weighted stable curve (which is the very first example of stable pair).
Then we review the definition of log canonical singularities and its extension to the non-normal case, i.e. semi-log canonical singularities.
After this, we define stable pairs and their corresponding Viehweg’s moduli functor.
We follow [Ale15, Kol13b, KM98].
Recall that we work over an algebraically closed field k of characteristic zero.

# 7.1 Weighted stable curves

Definition 7.1. Let $n \in \mathbb { Z } _ { \geq 0 }$ and fix $b _ { 1 } , \dots , b _ { n } \in ( 0 , 1 ] \cap \mathbb { Q }$ .
A weighted stable curve for the weight $\underline { { b } } = ( b _ { 1 } , \ldots , b _ { n } )$ is a pair $\begin{array} { r } { ( C , B = \sum _ { i = 1 } ^ { n } b _ { i } p _ { i } ) } \end{array}$ such that the following hold:

(i) $C$ is a nodal curve;  
(ii) The points $p _ { 1 } , \ldots , p _ { n }$ lie on the smooth locus of $C$ , and if $p _ { i _ { 1 } } , \ldots , p _ { i _ { m } }$ coincide, then $b _ { i _ { 1 } } +$ .
$\dots + b _ { i _ { m } } \leq 1$ ;  
(iii) Let $C = \cup _ { j } C _ { j }$ be the decomposition of $C$ into its irreducible components and let $C _ { j } ^ { \nu }$ be the normalization of $C _ { j }$ .
Let $d _ { j }$ be the cardinality of the preimage of the nodes of $C$ under the composition $C _ { j } ^ { \nu }  C _ { j } \hookrightarrow C$ .
Then for all $j$ we require that

$$
2 p _ { g } ( C _ { j } ^ { \nu } ) - 2 + d _ { j } + \sum _ { p _ { i } \in C _ { j } } b _ { i } > 0 .
$$

Observation 7.2. Condition (iii) of Definition 7.1 is equivalent to $( K _ { C } + B ) | _ { C _ { j } }$ ample for all $j$ , which is equivalent to $K _ { C } + B$ ample.

Theorem 7.3 ([Has03, Theorem 2.1]).
For any $n , g \in \mathbb { Z } _ { \geq 0 }$ and collection of weights $\underline { { b } } = ( b _ { 1 } , \ldots , b _ { n } )$ , there exists a connected, smooth, and proper Deligne-Mumford stack $\overline { { \mathcal { M } } } _ { g , \mathfrak { b } }$ parametrizing weighted stable curves for the weight $\underline b$ of arithmetic genus $g$ .
The corresponding coarse moduli scheme $\overline { { M } } _ { g , \underline { { b } } }$ is projective.
(These results also hold over $\mathbb { Z }$ .)

# 7.2 Singularities of pairs

Definition 7.4. Let $X$ be a normal variety and let $B$ be a $\mathbb { Q }$ -divisor on $X$ with coefficients in $( 0 , 1 ]$ such that $K _ { X } + B$ is $\mathbb { Q }$ -Cartier.
Let $f \colon Y \to X$ be a birational morphism.
If $\{ E _ { i } \} _ { i }$ is the set of irreducible exceptional divisors of $f$ , then there exist rational numbers $a ( E _ { i } , X , B )$ such that

$$
K _ { Y } + f _ { * } ^ { - 1 } B \sim _ { \mathbb { Q } } f ^ { * } ( K _ { X } + B ) + \sum _ { i } a ( E _ { i } , X , B ) E _ { i } ,
$$

where $f _ { * } ^ { - 1 } B$ denotes the strict transform of $B$ under $f$ .
We define the discrepancy of the pair $( X , B )$ as

$$
\operatorname { d i s c r } ( X , B ) = \operatorname* { i n f } \{ a ( E , X , B ) \} ,
$$

where we take the infimum over all birational morphisms $f \colon Y \to X$ and all irreducible exceptional divisors $E \subset Y$ .

Definition 7.5. Let $X$ be a normal variety and let $B$ be a $\mathbb { Q }$ -divisor on $X$ with coefficients in $( 0 , 1 ]$ such that $K _ { X } + B$ is $\mathbb { Q }$ -Cartier.
We say that the singularities of the pair $( X , B )$ are

• terminal if discrep $( X , B ) > 0$ ;  
• canonical if discrep $( X , B ) \geq 0$ ;  
• Kawamata log terminal (or $k l t$ for short) if discrep $( X , B ) > - 1$ and $\lfloor B \rfloor = 0$ ;  
• purely log terminal if discrep $( X , B ) > - 1$ ;  
• log canonical if discrep $( X , B ) \geq - 1$ .

In general, it is not very easy to compute the discrepancy of a pair $( X , B )$ , especially because we need to consider all birational morphisms $Y  X$ .
However, it is possible to tell whether $( X , B )$ has log canonical or klt singularities just by considering a log resolution of $( X , B )$ .

Theorem 7.6 ([Hir64]).
Let $X$ be a scheme and $B$ a $\mathbb { Q }$ -divisor on $X$ .
Then there exists a proper birational morphism $\sigma \colon Y  X$ such that $Y$ is smooth, $\operatorname { E x c } ( \sigma )$ is a divisor, and $\mathrm { E x c } ( \sigma ) \cup \mathrm { S u p p } ( \sigma _ { * } ^ { - 1 } B )$ is simple normal crossing.
We call $\sigma$ a log resolution of $( X , B )$ .

Proposition 7.7 ([Kol13b, Corollary 2.13]).
Let $X$ be a normal variety and let $B$ be a $\mathbb { Q }$ -divisor on $X$ with coefficients in $( 0 , 1 ]$ such that $K _ { X } + B$ is $\mathbb { Q }$ -Cartier.
Let $\sigma \colon Y  X$ be a log resolution of $( X , B )$ , so that

$$
K _ { Y } \sim _ { \mathbb { Q } } \sigma ^ { * } ( K _ { X } + B ) + \sum _ { i } a _ { i } E _ { i } .
$$

(Observe that, writing in this way, a divisor $E _ { i } \subset Y$ is not necessarily exceptional.) Then

• $( X , B )$ is log canonical if and only if $a _ { i } \geq - 1$ for all $i$ ;  
• $( X , B )$ is klt if and only if $a _ { i } > - 1$ for all $i$ .

Observation 7.8. In Proposition 7.7 the condition $a _ { i } \geq 1$ for $E _ { i }$ not exceptional is automatically satisfied because the coefficients of the divisor $B$ are assumed to be in the interval $( 0 , 1 ]$ .

Example 7.9. Let $X = \mathbb { A } ^ { 2 }$ , $C = Z ( y ^ { 2 } - x ^ { 3 } )$ , and $\beta \in ( 0 , 1 ] \cap \mathbb { Q }$ .
Let us compute the singularities of the pair $( X , \beta C )$ using Proposition 7.7. For simplicity of notation, when blowing up at a point, we denote the strict transform of a divisor $D$ by the same letter $D$ .
A log resolution of $( X , \beta C )$ is given by $\sigma = \sigma _ { 1 } \cup \sigma _ { 2 } \cup \sigma _ { 3 }$ , where

• $\sigma _ { 1 } \colon X ^ { \prime } \to X$ is the blow up of $X$ at $( 0 , 0 )$ with exceptional divisor $E _ { 1 }$ ;  
• $\sigma _ { 2 } \colon X ^ { \prime \prime } \to X ^ { \prime }$ is the blow up of $X ^ { \prime }$ at $C \cap E _ { 1 }$ with exceptional divisor $E _ { 2 }$ ;  
• $\sigma _ { 3 } \colon Y  X ^ { \prime \prime }$ is the blow up of $X ^ { \prime \prime }$ at $C \cap E _ { 1 } \cap E _ { 2 }$ with exceptional divisor $E _ { 3 }$ .

We have that

$$
K _ { Y } = \sigma _ { 3 } ^ { * } ( K _ { X ^ { \prime \prime } } ) + E _ { 3 } = \sigma _ { 3 } ^ { * } ( \sigma _ { 2 } ^ { * } ( K _ { X ^ { \prime } } ) + E _ { 2 } ) + E _ { 3 } = \sigma _ { 3 } ^ { * } ( \sigma _ { 2 } ^ { * } ( K _ { X ^ { \prime } } ) ) + E _ { 2 } + 2 E _ { 3 }
$$

$$
= \sigma _ { 3 } ^ { * } ( \sigma _ { 2 } ^ { * } ( \sigma _ { 1 } ^ { * } ( K _ { X } ) + E _ { 1 } ) ) + E _ { 2 } + 2 E _ { 3 } = \sigma _ { 3 } ^ { * } ( \sigma _ { 2 } ^ { * } ( E _ { 1 } ) ) + E _ { 2 } + 2 E _ { 3 }
$$

$$
= \sigma _ { 3 } ^ { * } ( E _ { 1 } + E _ { 2 } ) + E _ { 2 } + 2 E _ { 3 } = E _ { 1 } + 2 E _ { 2 } + 4 E _ { 3 } ,
$$

$$
\sigma ^ { * } C = \sigma _ { 3 } ^ { * } \sigma _ { 2 } ^ { * } \sigma _ { 1 } ^ { * } C = \sigma _ { 3 } ^ { * } \sigma _ { 2 } ^ { * } ( C + 2 E _ { 1 } ) = \sigma _ { 3 } ^ { * } ( C + 2 E _ { 1 } + 3 E _ { 2 } ) = C + 2 E _ { 1 } + 3 E _ { 2 } + 6 E _ { 3 } .
$$

It follows that

$$
\begin{array} { c } { { \displaystyle { K _ { Y } = \sigma ^ { * } ( K _ { X } + \beta C ) + \sum _ { i = 1 } ^ { 3 } a _ { i } E _ { i } - \sigma _ { * } ^ { - 1 } ( \beta C ) } } } \\ { { \mathrm { } } } \\ { { \Longrightarrow ~ E _ { 1 } + 2 E _ { 2 } + 4 E _ { 3 } = \beta ( C + 2 E _ { 1 } + 3 E _ { 2 } + 6 E _ { 3 } ) + \sum _ { i = 1 } ^ { 3 } a _ { i } E _ { i } - \beta C } } \end{array}
$$

$$
\implies \left\{ \begin{array} { l l } { a _ { 1 } = 1 - 2 \beta , } \\ { a _ { 2 } = 2 - 3 \beta , } \\ { a _ { 3 } = 4 - 6 \beta . } \end{array} \right.
$$

Therefore, by Proposition 7.7, we have that $( X , \beta C )$ has log canonical (resp.
klt) singularities if and only if $1 - 2 \beta , 2 - 3 \beta , 4 - 6 \beta , - \beta \ge - 1$ (resp.
$> - 1$ ), which is true if and only if $\beta \leq \frac { 5 } { 6 }$ (resp.
$\beta < \frac { 5 } { 6 }$ ).

7.3 Extension to the non-normal case: semi-log canonical singularities

# 7.3.1 Demi-normal schemes

Definition 7.10. Let $X$ be a scheme.
A point $p \in X$ is called a node if $\mathcal { O } _ { X , p } \cong R / ( f )$ where $( R , { \mathfrak { m } } )$ is a regular local ring of dimension 2, $f \in { \mathfrak { m } } ^ { 2 }$ , and $f$ is not a square in $\mathfrak { m } ^ { 2 } / \mathfrak { m } ^ { 3 }$ .

Example 7.11. Let $X = \operatorname { S p e c } ( \mathbb { k } [ x , y ] / ( x y ) )$ .
We want to verify that $p = ( x , y ) / ( x y ) \in X$ is a node.
Let $R = \mathbb { k } [ x , y ] _ { ( x , y ) }$ , ${ \mathfrak { m } } = ( x , y ) \mathbb { k } [ x , y ] _ { ( x , y ) }$ , and $f = x y$ .
Then $\mathcal { O } _ { X , p } \cong R / ( f )$ , $( R , { \mathfrak { m } } )$ is a regular local ring of dimension 2, $f \in { \mathfrak { m } } ^ { 2 }$ , and $f$ is not a square in $\mathfrak { m } ^ { 2 } / \mathfrak { m } ^ { 3 }$ .

Definition 7.12. Let $X$ be an equidimensional noetherian scheme.
Then $X$ is called demi-normal if $X$ is $S _ { 2 }$ and, given any $p \in X$ with $\dim { \mathcal { O } } _ { X , p } = 1$ , then $p$ is regular or a node.

Observation 7.13. By definition, a demi-normal scheme $X$ is Gorenstein in codimension 1. Therefore, it makes sense to consider the canonical class $K _ { X }$ .

# 7.3.2 Normalization of a demi-normal scheme

We start with some algebra preliminaries.
The following lemma is a straightforward application of Zorn’s lemma.

Lemma 7.14. Let $A \subseteq B$ be an extension of rings.
Then there exists a unique largest ideal of $A$ which is also an ideal of $B$ .
We denote this ideal by $I _ { A , B }$ .

Proposition 7.15. Let $A \subseteq B$ be an extension of rings.
Then $I _ { A , B } = \mathrm { A n n } _ { A } ( B / A )$ .

Proof.
Let us first show that $I _ { A , B } \supseteq \mathrm { A n n } _ { A } ( B / A )$ .
By Lemma 7.14 it is enough to show that $\mathrm { A n n } _ { A } ( B / A )$ , which is obviously an ideal of $A$ , is also an ideal of $B$ .
So let $a \in \mathrm { A n n } _ { A } ( B / A )$ and $b \in B$ .
We want to show that $a b \in \mathrm { A n n } _ { A } ( B / A )$ .
So take any $b ^ { \prime } + A \in B / A$ .
We have that $a b ( b ^ { \prime } + A ) = a ( b b ^ { \prime } + A ) = 0 + A$ because $b b ^ { \prime } \in B$ and $a \in \mathrm { A n n } _ { A } ( B / A )$ .
Therefore $a b \in \mathrm { A n n } _ { A } ( B / A )$ .

For the other containment, let $a \in I _ { A , B }$ and take any $b + A \in B / A$ .
Then $a ( b + A ) = 0 + A$ because $I _ { A , B }$ is an ideal in $B$ and $a b \in I _ { A , B } \subseteq A$ .
Hence $a \in \mathrm { A n n } _ { A } ( B / A )$ .
□

Definition 7.16. Let $A$ be a ring and let $A$ be the integral closure of $A$ in its total ring of fractions $\operatorname { F r a c } ( A )$ .
Then $I _ { A , { \overline { { A } } } } = \mathrm { A n n } _ { A } ( \overline { { A } } / A )$ is called the conductor ideal of $A$ .

Now we translate into sheaf theory the notion of conductor ideal.

Definition 7.17. Let $X$ be a reduced scheme and let $\nu \colon X ^ { \nu } \to X$ be its normalization.
Define the conductor ideal sheaf of $X$ as:

$$
\mathrm { c o n d } _ { X } : = \mathrm { A n n } _ { \mathcal { O } _ { X } } ( \nu _ { * } \mathcal { O } _ { X ^ { \nu } } / \mathcal { O } _ { X } ) .
$$

By our previous discussion, $\mathrm { c o n d } _ { X }$ is also an ideal sheaf on $X ^ { \nu }$ .
When we look at cond $X$ as an ideal sheaf on $X ^ { \nu }$ , we denote it by $\mathrm { c o n d } _ { X ^ { \nu } }$ .

Definition 7.18. Let $X$ be a reduced scheme and let $\nu \colon X ^ { \nu } \to X$ be its normalization.
Define the conductor subschemes $D \subseteq X$ and $D ^ { \nu } \subseteq X ^ { \nu }$ as:

$$
D : = \operatorname { S p e c } _ { X } ( \mathcal { O } _ { X } / \operatorname { c o n d } _ { X } ) , \ D ^ { \nu } : = \operatorname { S p e c } _ { X ^ { \nu } } ( \mathcal { O } _ { X ^ { \nu } } / \operatorname { c o n d } _ { X ^ { \nu } } ) .
$$

In the case of demi-normal schemes, the conductor subschemes have the following properties.

Proposition 7.19 ([Kol13b, Section 5.1]).
Let $X$ be a demi-normal scheme, $\nu \colon X ^ { \nu } \to X$ its normalization, and $D , D ^ { \nu }$ the corresponding conductor subschemes.
Then $D , D ^ { \nu }$ are both reduced subschemes of pure codimension 1.

Proposition 7.20 ([Kol13b, Section 5.1]).
Let $X$ be a demi-normal projective scheme, $\nu \colon X ^ { \nu } \to X$ its normalization, and $D , D ^ { \nu }$ the corresponding conductor subschemes.
Let $B$ be an effective $\mathbb { Q }$ - divisor such that $K _ { X } + B$ is $\mathbb { Q }$ -Cartier.
Then

$$
\nu ^ { * } ( K _ { X } + B ) \sim _ { \mathbb { Q } } K _ { X ^ { \nu } } + \nu _ { * } ^ { - 1 } B + D ^ { \nu } .
$$

# 7.3.3 Semi-log canonical singularities

Definition 7.21. Let $X$ be a variety and let $B$ be a $\mathbb { Q }$ -divisor on $X$ with coefficients in $( 0 , 1 ]$ .
Then the pair $( X , B )$ is semi-log canonical if the following conditions are satisfied:

(i) $X$ is demi-normal;  
(ii) If $\nu \colon X ^ { \nu } \to X$ is the normalization with conductors $D \subset X$ and $D ^ { \nu } \subset X ^ { \nu }$ , then the support of $B$ does not contain any irreducible component of $D$ ;  
(iii) $K _ { X } + B$ is $\mathbb { Q }$ -Cartier;  
(iv) The pair $( X ^ { \nu } , D ^ { \nu } + \nu _ { * } ^ { - 1 } B )$ is log canonical (i.e. for each connected component $Z$ of $X ^ { \nu }$ the pair $( Z , ( D ^ { \nu } + \nu _ { * } ^ { - 1 } B ) | _ { Z } )$ is log canonical).

# 7.4 Stable pairs and Viehweg’s moduli functor

# 7.4.1 Stable pairs

Definition 7.22. A pair $( X , B )$ is stable if the following conditions are satisfied:

(i) On singularities: $( X , B )$ is a semi-log canonical pair;  
(ii) Numerical: $K _ { X } + B$ is ample.

Example 7.23. It is immediate from the definitions that a weighted stable curve $( C , B )$ (see Definition 7.1) is an example of stable pair.

Example 7.24. Another fundamental example of stable pair is given by $( S , 0 )$ where $S$ is the canonical model (see [KM98, Section 3.8]) of a surface of general type (i.e. $\kappa ( S ) = 2$ ).
We have that $S$ is normal, $K _ { S }$ is $\mathbb { Q }$ -Cartier and ample, and $S$ has canonical singularities.

# 7.4.2 The Viehweg’s moduli stack

Definition 7.25. The Viehweg’s moduli stack $\overline { { \mathcal { M } } } _ { d , N , C , b }$ is defined as follows.
Let us fix constants $d , N \in \mathbb { Z } _ { > 0 }$ , $C \in \mathbb { Q } _ { > 0 }$ , and $\underline { { b } } = ( b _ { 1 } , \ldots , b _ { n } )$ with $b _ { i } \in ( 0 , 1 ] \cap \mathbb { Q }$ and $N b _ { i } \in \mathbb { Z }$ for all $i = 1 , \ldots , n$ .
For any scheme $S$ over $\Bbbk$ , $\mathcal { M } _ { d , N , C , \underline { { b } } } ( S )$ is the set of proper flat families ${ \mathfrak { X } } \to S$ together with a divisor $\begin{array} { r } { \mathfrak { B } = \sum _ { i } b _ { i } \mathfrak { B } _ { i } } \end{array}$ satisfying the following properties:

• For all $i = 1 , \ldots , n$ , $\mathfrak { B } _ { i }$ is a codimension 1 closed subscheme which is flat over $S$ ; • Every geometric fiber $( X , B )$ is a stable pair of dimension $d$ with $( K _ { X } + B ) ^ { d } = C$ ; • There exists an invertible sheaf $\mathcal { L }$ on $\boldsymbol { \mathfrak X }$ such that for every geometric fiber $( X , B )$ one has $\mathcal { L } | _ { X } \cong \mathcal { O } _ { X } ( N ( K _ { X } + B ) ) .$

Remark 7.26. Whether the stack $\overline { { \mathcal { M } } } _ { d , N , C , b }$ is coarsely represented by a projective scheme is a subtle matter.
In our case (see Section 8.1.5) it is.
More details can be found in [Ale15, Vie95].

# Chapter 8

# The KSBA Compactification of the Moduli Space of D1,6-polarized Enriques Surfaces

In the current chapter we discuss the original results of this dissertation.

# 8.1 $D _ { 1 , 6 }$ -polarized Enriques surfaces and the choice of the divisor

# 8.1.1 The $D _ { 1 , 6 }$ polarization

We refer to Chapter 4 for the definition and the main properties of Enriques surfaces.

Definition 8.1. Recall from Section 2.3 that the $D _ { 1 , 6 }$ lattice is the index 2 sublattice of $\mathbb { Z } ^ { 1 , 6 }$ (see Examples 2.9 (a)) consisting of the vectors with even square (or equivalently, we can require the sum of the coordinates to be even).
If $e _ { 0 } , e _ { 1 } , \ldots , e _ { 6 }$ is the canonical basis of $\mathbb { Z } ^ { 1 , 6 }$ , then we distinguish the following vectors in $D _ { 1 , 6 }$ : $2 e _ { 0 } , e _ { 1 } \pm e _ { 2 } , e _ { 3 } \pm e _ { 4 } , e _ { 5 } \pm e _ { 6 }$ .

Definition 8.2. A $D _ { 1 , 6 }$ -polarized Enriques surface is an Enriques surface $S$ whose Picard group contains a primitively embedded copy of $D _ { 1 , 6 }$ (this means that $\mathrm { P i c } ( S ) / D _ { 1 , 6 }$ is torsion free) such that:

(a) The distinguished vector $2 e _ { 0 }$ corresponds to a nef divisor class $H$ (observe that $H$ is also big because $H ^ { 2 } = ( 2 e _ { 0 } ) ^ { 2 } = 4$ );

(b) The distinguished vectors $e _ { 1 } \pm e _ { 2 } , e _ { 3 } \pm e _ { 4 } , e _ { 5 } \pm e _ { 6 }$ correspond to six irreducible curves $R _ { 1 } ^ { \pm } , R _ { 2 } ^ { \pm } , R _ { 3 } ^ { \pm }$ respectively (these curves are $\left( - 2 \right)$ -curves, i.e. isomorphic to $\mathbb { P } ^ { 1 }$ and with self-intersection $- 2$ ).

The next proposition is well known from [Oud10, Section 3].
However, given its importance for us, we briefly sketch its proof.

Proposition 8.3. Let $S$ be a $D _ { 1 , 6 }$ -polarized Enriques surface.
Then the linear system $| H - R _ { i } ^ { + } - R _ { i } ^ { - } |$ is a genus 1 pencil, $i = 1 , 2 , 3$ .

Proof.
The linear system $| H |$ is base point free and 2-dimensional (see [Oud10, Proposition 3.1]).
Moreover, $| H |$ contracts the curves $R _ { i } ^ { \pm }$ , $i = { 1 , 2 , 3 }$ , because $H \cdot R _ { i } ^ { \pm } = 0$ .
On the other hand, $| H - R _ { i } ^ { + } - R _ { i } ^ { - } |$ is a proper linear subsystem of $| H |$ (for instance, it does not contract $R _ { i } ^ { \pm }$ and contracts $R _ { j } ^ { \pm }$ for $j \neq i$ ).
Therefore, $| H - R _ { i } ^ { + } - R _ { i } ^ { - } |$ is a pencil and a curve $C$ in this linear system has (arithmetic) genus 1 because $C ^ { 2 } = ( H - R _ { i } ^ { + } - R _ { i } ^ { - } ) ^ { 2 } = 0$ (now use [Bea96, I.15 The genus formula]).
□

Observation 8.4. Every genus 1 fibration on an Enriques surface has two half-fibers (see Section 4.4). Therefore, for a $D _ { 1 , 6 }$ -polarized Enriques surface $S$ , denote by $E _ { i }$ and $E _ { i } ^ { \prime }$ the two half-fibers in the genus 1 pencil $| H - R _ { i } ^ { + } - R _ { i } ^ { - } |$ , $i = 1 , 2 , 3$ .
Then the divisor $\textstyle \sum _ { i = 1 } ^ { 3 } ( E _ { i } + E _ { i } ^ { \prime } )$ is canonically associated to the $D _ { 1 , 6 }$ -polarization, and its intrinsic nature leads us to consider moduli of pairs $\begin{array} { r } { \Big ( S , \epsilon \cdot \sum _ { i = 1 } ^ { 3 } ( E _ { i } + E _ { i } ^ { \prime } ) \Big ) } \end{array}$ for $0 < \epsilon \ll 1$ , $\epsilon \in \mathbb { Q }$ .
Observe also that the divisor $\textstyle \sum _ { i = 1 } ^ { 3 } E _ { i }$ is a degree 6 polarization which gives the classical construction of Enriques: it realizes $S$ as the normalization of a degree 6 surface in $\mathbb { P } ^ { 3 }$ with only double crossing singularities along the edges of the coordinate tetrahedron.

Remark 8.5. If $S$ is a $D _ { 1 , 6 }$ -polarized Enriques surface, then the divisor $\begin{array} { r } { C = H + \sum _ { i = 1 } ^ { 3 } ( R _ { i } ^ { + } + R _ { i } ^ { - } ) } \end{array}$ is divisible by 2 in $\mathrm { P i c } ( S )$ .
The $\mathbb { Z } _ { 2 }$ -cover of $S$ branched along $C$ has six $( - 1 )$ -curves.
Blowing down these curves we obtain a Campedelli surface with (topological) fundamental group $\mathbb { Z } _ { 2 } ^ { 3 }$ (these were considered in [AP09]).
Conversely, such a Campedelli surface $X$ can be realized as the $\mathbb { Z } _ { 2 } ^ { 3 }$ -cover of $\mathbb { P } ^ { 2 }$ branched along seven lines.
The minimal desingularization of the quotient of $X$ by the involution fixing pointwise the preimage of one of these lines is a $D _ { 1 , 6 }$ -polarized Enriques surface.

Remark 8.6. By [Cos85, Theorem 3] we know that every Enriques surface contains three genus 1 pencils $\vert 2 E _ { 1 } \vert , \vert 2 E _ { 2 } \vert , \vert 2 E _ { 3 } \vert$ such that $E _ { 1 } \cdot E _ { 2 } = E _ { 2 } \cdot E _ { 3 } = E _ { 3 } \cdot E _ { 1 } = 1$ .
Moreover, observe that

Enriques surfaces with a $D _ { 1 , 6 }$ -polarization are a specialization of the family of Enriques surfaces considered in [Ver83].

# 8.1.2 $D _ { 1 , 6 }$ -polarized Enriques surfaces as $\mathbb { Z } _ { 2 } ^ { 2 }$ -covers

Notation 8.7. Let $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ be the blow up of $\mathbb { P } ^ { 2 }$ at $[ 1 : 0 : 0 ] , [ 0 : 1 : 0 ] , [ 0 : 0 : 1 ]$ .
$\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ comes with three genus 0 pencils $\pi _ { 1 } , \pi _ { 2 } , \pi _ { 3 }$ : $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 } \to \mathbb { P } ^ { 1 }$ , and denote by $\ell _ { i } , \ell _ { i } ^ { \prime }$ two distinct irreducible elements in the $i$ -th pencil, $i = 1 , 2 , 3$ .

Proposition 8.8. Let $S$ be a $D _ { 1 , 6 }$ -polarized Enriques surface.
Then there exists a divisor $\textstyle \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } +$ $\ell _ { i } ^ { \prime }$ ) on $\mathrm { B l _ { 3 } \mathbb { P } ^ { 2 } }$ (see Notation 8.7) without triple intersection points and a morphism $\pi \colon S \to \mathrm { { B l _ { 3 } } } \mathbb { P } ^ { 2 }$ such that

(i) $\pi$ is a $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of $\mathrm { B l _ { 3 } \mathbb { P } ^ { 2 } }$ ramified at $\textstyle \sum _ { i = 1 } ^ { 3 } ( E _ { i } + E _ { i } ^ { \prime } )$ and branched along $\textstyle \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } )$ ;  
(ii) The linear system $\left| 2 E _ { i } \right|$ is the pullback of $| \ell _ { i } |$ , $i = { 1 , 2 , 3 }$ .

Conversely, given any divisor $\textstyle \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } )$ on $\mathrm { B l _ { 3 } \mathbb { P } ^ { 2 } }$ without triple intersection points, an appropriate $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of $\mathrm { B l _ { 3 } \mathbb { P } ^ { 2 } }$ branched along $\textstyle \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } )$ is an Enriques surface with exactly two choices of $D _ { 1 , 6 }$ -polarization: $H$ is the pullback of a general line in $\mathrm { B l _ { 3 } \mathbb { P } ^ { 2 } }$ , and the six lines $R _ { i } ^ { \pm }$ , $i = 1 , 2 , 3$ , are the preimages of the exceptional divisors in $\mathrm { B l _ { 3 } \mathbb { P } ^ { 2 } }$ , or the other three $( - 1 )$ -curves.
These two choices are exchanged by the Cremona involution of $\mathrm { B l _ { 3 } \mathbb { P } ^ { 2 } }$ (see Observation 8.9).

Proof.
(i) and (ii) are discussed in [Oud10, Section 3].
The divisor $\textstyle \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } )$ cannot have triple intersection points otherwise $S$ would be singular (see [Par91, Proposition 3.1]).

For the inverse construction, we use the general theory of abelian covers developed in [Par91].
Let $\mathbb { Z } _ { 2 } ^ { 2 } = \{ e , a , b , c \}$ where $e$ is the identity element, and let $\left\{ \chi _ { 0 } , \chi _ { 1 } , \chi _ { 2 } , \chi _ { 3 } \right\}$ be the characters of $\mathbb { Z } _ { 2 } ^ { 2 }$ with $\chi _ { 0 } = 1$ and $\chi _ { 1 } ( b ) = \chi _ { 1 } ( c ) = \chi _ { 2 } ( a ) = \chi _ { 2 } ( c ) = \chi _ { 3 } ( a ) = \chi _ { 3 } ( b ) = - 1$ .
Define $D _ { a } = \ell _ { 1 } + \ell _ { 1 } ^ { \prime } , D _ { b } =$ $\ell _ { 2 } + \ell _ { 2 } ^ { \prime } , D _ { c } = \ell _ { 3 } + \ell _ { 3 } ^ { \prime }$ .
Consider the building data (see [Par91, Definition 2.1]) consisting of the divisors $D _ { a } , D _ { b } , D _ { c }$ and the line bundles $L _ { \chi _ { 1 } } , L _ { \chi _ { 2 } } , L _ { \chi _ { 3 } }$ satisfying

$$
2 L _ { \chi _ { 1 } } = D _ { b } + D _ { c } , ~ 2 L _ { \chi _ { 2 } } = D _ { a } + D _ { c } , ~ 2 L _ { \chi _ { 3 } } = D _ { a } + D _ { b } .
$$

This building data determines a $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover $\pi \colon S \to \mathrm { { B l _ { 2 } } } \mathbb { P } ^ { 2 }$ branched along $\textstyle \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } )$ which is unique up to isomorphism of $\mathbb { Z } _ { 2 } ^ { 2 }$ -covers (see [Par91, Theorem 2.1]).
By [Par91, Proposition 3.1] we have that $S$ is smooth, and using [Par91, Proposition 4.2, formula (4.8)] one can easily compute that $\chi ( \mathcal { O } _ { S } ) = 1$ , which tells us that $h ^ { 0 } ( { \cal S } , \omega _ { \cal S } ) = h ^ { 1 } ( { \cal S } , \mathcal { O } _ { \cal S } )$ .
If $R$ denotes the ramification divisor of the cover, then $K _ { S } \sim \pi ^ { * } ( K _ { \mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 } } ) + R$ and $\begin{array} { r } { 2 R \sim \pi ^ { * } ( \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } ) ) } \end{array}$ imply that $2 K _ { S } \sim 0$ , hence $S$ is an Enriques surface.
□

Observation 8.9. In the statement of Proposition 8.8, the ambiguity for the choice of $D _ { 1 , 6 } \cdot$ - polarization on the $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of $\mathrm { B l _ { 3 } \mathbb { P } ^ { 2 } }$ branched along $\textstyle \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } )$ is not an issue for our purposes.
This is because the Cremona involution on $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ does not change the isomorphism class of the pair $\textstyle ( \mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 } , \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } ) )$ , even though it changes the line configuration.

Lemma 8.10. Let $S$ be a $D _ { 1 , 6 }$ -polarized Enriques surface and let $\pi \colon S  \mathrm { { B l _ { 3 } } \mathbb { P } ^ { 2 } }$ be the corresponding $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover ramified at $\begin{array} { r } { E = \sum _ { i = 1 } ^ { 3 } ( E _ { i } + E _ { i } ^ { \prime } ) } \end{array}$ and branched along $\begin{array} { r } { L = \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } ) } \end{array}$ (see Proposition 8.8). Then

$$
K _ { S } + \epsilon E \sim _ { \mathbb { Q } } \pi ^ { * } \left( K _ { { \mathrm { B l } } _ { 3 } \mathbb { P } ^ { 2 } } + \left( { \frac { 1 + \epsilon } { 2 } } \right) L \right) .
$$

In particular, $( S , \epsilon E )$ is stable if and only if $\left( \operatorname { B l _ { 3 } } \mathbb { P } ^ { 2 } , \left( { \frac { 1 + \epsilon } { 2 } } \right) L \right)$ is stable.

Proof.
We have that $K _ { S } \sim \pi ^ { * } ( K _ { \mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 } } ) + E$ and $2 E \sim \pi ^ { * } ( L )$ .
This implies that $K _ { S } \sim _ { \mathbb { Q } } \pi ^ { * } ( K _ { \mathrm { B l _ { 3 } } ( \mathbb { P } ^ { 2 } ) } ) +$ ${ \frac { 1 } { 2 } } \pi ^ { * } ( L )$ , and by adding $\epsilon E \sim _ { \mathbb { Q } } \frac { \epsilon } { 2 } \pi ^ { * } ( L )$ to both sides we obtain what claimed.
For the last statement about stability, we have that $( S , \epsilon E )$ is semi-log canonical if and only if $\left( \mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 } , \left( { \frac { 1 + \epsilon } { 2 } } \right) L \right)$ is semi-log canonical by [AP12, Lemma 2.3], and $K _ { S } + \epsilon E$ is ample if and only if $K _ { \mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 } } + \left( { \frac { 1 + \epsilon } { 2 } } \right) L$ is ample by [Laz04, Proposition 1.2.13 and Corollary 1.2.28].
□

Remark 8.11. With the notation introduced in Lemma 8.10, we claim that studying the degenerations of the stable pairs $( S , \epsilon E )$ is equivalent to the study of the degenerations of the stable pairs $\left( \mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 } , \left( { \frac { 1 + \epsilon } { 2 } } \right) L \right)$ .
To prove this, let $K$ be the field of fractions of a DVR $( A , { \mathfrak { m } } )$ , where $\mathfrak { m }$ is the maximal ideal of $A$ .
Let $( \mathfrak { S } ^ { \circ } , \mathcal { E } ^ { \circ } )$ (resp.
$( \mathfrak { B } ^ { \circ } , \mathcal { L } ^ { \circ } )$ ) be a family of stable pairs over Spec $K$ ) with fibers isomorphic to $( S , \epsilon E )$ (resp.
$\left( \operatorname { B l } _ { 3 } \mathbb { P } ^ { 2 } , \left( { \frac { 1 + \epsilon } { 2 } } \right) L \right)$ ).
Let $G ^ { \circ } \to \mathfrak { B } ^ { \circ }$ be the appropriate $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover ramified at $\mathcal { E } ^ { \circ }$ and branched along $\mathcal { L } ^ { \mathrm { o } }$ .
Let $( \mathfrak { S } , \mathcal { E } )$ be the completion of $( \mathfrak { S } ^ { \circ } , \mathcal { E } ^ { \circ } )$ over Spec $( A )$ , or a ramified base change of it, having as central fiber a stable pair (see [Ale06, Theorem 2.1]).
Denote by $( \mathfrak { S } _ { \mathfrak { m } } , \mathcal { E } _ { \mathfrak { m } } )$ the central fiber of $( \mathfrak { S } , \mathcal { E } )$ .
We adopt a similar notation for $( \mathfrak { B } ^ { \circ } , \mathcal { L } ^ { \circ } )$ .
What we want to show is that $( \mathfrak { S } _ { \mathfrak { m } } , \mathcal { E } _ { \mathfrak { m } } )$ is a $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of $( { \mathfrak { B } } _ { \mathfrak { m } } , { \mathcal { L } } _ { \mathfrak { m } } )$ .
This is automatic if we can show that the $\mathbb { Z } _ { 2 } ^ { 2 }$ -action on ${ \mathfrak { S } } ^ { \circ }$ extends to $\mathfrak { S }$ (in this case, the quotient of $\mathfrak { S }$ by $\mathbb { Z } _ { 2 } ^ { 2 }$ is isomorphic to $\mathfrak { B }$ by the uniqueness of the completion of $\mathfrak { B } ^ { \circ }$ over Spec $( A )$ , and this implies what we want).
Fix any $g \in \mathbb { Z } _ { 2 } ^ { 2 }$ and consider its corresponding action $\alpha _ { g } \colon { \mathfrak { S } } \ \xrightarrow { } \ \infty \ { \mathfrak { S } }$ .
Resolving the indeterminacies of $\alpha _ { g }$ , we obtain a morphism $\alpha _ { g } ^ { \prime } \colon { \mathfrak { S } } ^ { \prime } \to { \mathfrak { S } }$ where ${ \mathfrak { S } } ^ { \prime }$ is obtained by blowing up $\mathfrak { S }$ .
Then $\alpha _ { g } ^ { \prime }$ corresponds to a morphism $\alpha _ { g }$ from the log canonical model of ${ \mathfrak { S } } ^ { \prime }$ to the log canonical model of $\mathfrak { S }$ , which are both isomorphic to $\mathfrak { S }$ .
Then $\overline { { \alpha } } _ { g } \colon \mathfrak { S }  \mathfrak { S }$ is the desired extension of $\alpha _ { g }$ .
Since this extension is unique, there is a unique way to build the $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover ${ \mathfrak { S } } _ { \mathfrak { m } } \to { \mathfrak { B } } _ { \mathfrak { m } }$ branched along ${ \mathcal { L } } _ { \mathfrak { m } }$ , and this way is determined by ${ \mathfrak { S } } ^ { \circ } \to { \mathfrak { B } } ^ { \circ }$ .

Remark 8.12. As we already commented in Section 1.2, after reducing our problem to considering lines on $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ , we cannot use the hyperplane arrangements machinery from [Ale08, Ale15, AP09].
The reason is that the divisor $\begin{array} { r } { L = \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } ) } \end{array}$ does not contain any $( - 1 )$ -curve, and therefore $L$ is not the pullback from $\mathbb { P } ^ { 2 }$ of a line arrangement.

# 8.1.3 Reduction to stable toric pairs

Notation 8.13. Let $( [ X _ { 0 } : X _ { 1 } ] , [ Y _ { 0 } : Y _ { 1 } ] , [ Z _ { 0 } : Z _ { 1 } ] )$ be coordinates in $( \mathbb { P } ^ { 1 } ) ^ { 3 }$ .
We denote by $\Delta$ the toric boundary $V ( X _ { 0 } X _ { 1 } Y _ { 0 } Y _ { 1 } Z _ { 0 } Z _ { 1 } ) \subset ( \mathbb { P } ^ { 1 } ) ^ { 3 }$ ( $V ( I )$ denotes the closed subscheme associated to the homogeneous ideal $I$ ).

Proposition 8.14. Consider $\mathrm { B l _ { 3 } \mathbb { P } ^ { 2 } }$ together with a divisor $\textstyle \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } )$ (see Notation 8.7) without triple intersection points.
Then there exists $\begin{array} { r } { B = V \left( \sum _ { i , j , k = 0 , 1 } c _ { i j k } X _ { i } Y _ { j } Z _ { k } \right) \subset ( \mathbb { P } ^ { 1 } ) ^ { 3 } } \end{array}$ with coefficients $c _ { i j k } \neq 0$ such that $\left( \mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 } , \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } ) \right)$ is isomorphic to $( B , \Delta | _ { B } )$ .
Moreover, such $B \subset ( \mathbb { P } ^ { 1 } ) ^ { 3 }$ is uniquely determined up to the action of $\mathbb { G } _ { m } ^ { 3 } \rtimes \mathrm { S y m } ( Q )$ , where $Q$ is the unit cube.

Proof.
Consider the three projections $\pi _ { i } \colon { \mathrm { B l } } _ { 3 } \mathbb { P } ^ { 2 } \to \mathbb { P } ^ { 1 }$ , $i = { 1 , 2 , 3 }$ .
Let $\ell _ { i } = \pi _ { i } ^ { - 1 } ( [ a _ { 0 i } : a _ { 1 i } ] )$ and $\ell _ { i } ^ { \prime } = \pi _ { i } ^ { - 1 } ( [ a _ { 0 i } ^ { \prime } : a _ { 1 i } ^ { \prime } ] )$ .
The morphism $( \pi _ { 1 } , \pi _ { 2 } , \pi _ { 3 } ) \colon \mathrm { { B l } _ { 3 } \mathbb { P } ^ { 2 }  ( \mathbb { P } ^ { 1 } ) ^ { 3 } }$ is an embedding whose image is a divisor of class $( 1 , 1 , 1 )$ (observe that the restriction of $\Delta$ to this divisor gives the six $( - 1 )$ - curves, each one with multiplicity 2).
For each one of the three copies of $\mathbb { P } ^ { 1 }$ (which we label with $i = 1 , 2 , 3$ ) choose an automorphism $\varphi _ { i }$ sending $[ a _ { 0 i } : a _ { 1 i } ] , [ a _ { 0 i } ^ { \prime } : a _ { 1 i } ^ { \prime } ]$ to $[ 1 : 0 ] , [ 0 : 1 ]$ respectively.
Let $B$ be the image of the composition of the embedding $( \pi _ { 1 } , \pi _ { 2 } , \pi _ { 3 } )$ followed by the automorphism $( \varphi _ { 1 } , \varphi _ { 2 } , \varphi _ { 3 } )$ .
Then, under this morphism, $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 } \cong B$ and $\textstyle \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } )$ corresponds to $\Delta | _ { B }$ .
Moreover, $\begin{array} { r } { B = V \left( \sum _ { i , j , k = 0 , 1 } c _ { i j k } X _ { i } Y _ { j } Z _ { k } \right) } \end{array}$ where the coefficients $c _ { i j k }$ are nonzero (otherwise $\Delta | _ { B }$ would have triple intersection points).

In the construction of $B$ above we made some choices.
There is a Sym $( Q )$ -action which comes from the fact that we can permute the three projections $\pi _ { 1 } , \pi _ { 2 } , \pi _ { 3 }$ and for each $i$ we can exchange $[ a _ { 0 i } : a _ { 1 i } ]$ with $[ a _ { 0 i } ^ { \prime } : a _ { 1 i } ^ { \prime } ]$ (Sym $( Q )$ is isomorphic to the wreath product $\mathbb { Z } _ { 2 } \wr S _ { 3 }$ ).
There is also a $\mathbb { G } _ { m } ^ { 3 }$ -action due to the fact that each $\varphi _ { i }$ is uniquely determined up to $\mathbb { G } _ { m }$ .
It is easy to observe that our construction of $B$ is invariant under the action of $\mathrm { { A u t } ( B l _ { 3 } \mathbb { P } ^ { 2 } ) }$ on the line arrangement (see [Dol12, Theorem 8.4.2] for the description of $\mathrm { { A u t } ( B l _ { 3 } \mathbb { P } ^ { 2 } ) }$ ).

To conclude we need to show that any realization $\begin{array} { r } { B = V \left( \sum _ { i , j , k = 0 , 1 } c _ { i j k } X _ { i } Y _ { j } Z _ { k } \right) \subset ( \mathbb { P } ^ { 1 } ) ^ { 3 } } \end{array}$ with coefficients $c _ { i j k } \neq 0$ such that $\Big ( \mathrm { B l } _ { 3 } \mathbb { P } ^ { 2 } , \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } ) \Big ) \cong ( B , \Delta | _ { B } )$ can be obtained as we described up to ( $\mathbb { G } _ { m } ^ { 3 } \rtimes \mathrm { S y m } ( Q ) )$ -action.
But this is true because, up to $\mathbb { G } _ { m } ^ { 3 } \rtimes \mathrm { S y m } ( Q )$ , there is a unique way to realize $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ in $( \mathbb { P } ^ { 1 } ) ^ { 3 }$ so that the six $( - 1 )$ -curves are given by the restriction of $\Delta$ , and this is given by $V ( X _ { 0 } Y _ { 0 } Z _ { 0 } - X _ { 1 } Y _ { 1 } Z _ { 1 } )$ (we omit the proof of this).
□

Summing up, starting from our pairs of interest $\begin{array} { r } { ( S , \epsilon \cdot \sum _ { i = 1 } ^ { 3 } ( E _ { i } + E _ { i } ^ { \prime } ) ) } \end{array}$ defined in Observation 8.4, the considerations we made so far (Proposition 8.8, Lemma 8.10, Remark 8.11, and Proposition 8.14) allow us to consider moduli of the pairs $\left( B , \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) \Delta | _ { B } \right)$ with $B \subset ( \mathbb { P } ^ { 1 } ) ^ { 3 }$ as prescribed by Proposition 8.14 (observe that $\left( B , \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) \Delta | _ { B } \right)$ is obviously stable).
This approach in terms of $B \subset ( \mathbb { P } ^ { 1 } ) ^ { 3 }$ is convenient because $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , B )$ is a stable toric pair of type $\leq Q$ where $Q$ is the unit cube, and Theorem 6.9 gives an explicit description of the moduli space $\overline { { M } } _ { Q }$ parametrizing $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , B )$ and its degenerations.

Remark 8.15. Let $B \subset ( \mathbb { P } ^ { 1 } ) ^ { \mathrm { 3 } }$ as in Proposition 8.14. An alternative construction of the $\mathbb { Z } _ { 2 } ^ { 2 }$ - cover of $B$ branched along $\Delta | _ { B }$ which gives a $D _ { 1 , 6 }$ -polarized Enriques surface is the following.
Let $\begin{array} { r } { \widetilde { S } = V \left( \sum _ { i , j , k = 0 , 1 } c _ { i j k } X _ { i } ^ { 2 } Y _ { j } ^ { 2 } Z _ { k } ^ { 2 } \right) \subset ( \mathbb { P } ^ { 1 } ) ^ { 3 } } \end{array}$ .
The restriction to $\bar { S }$ of the map $( \mathbb { P } ^ { 1 } ) ^ { 3 }  ( \mathbb { P } ^ { 1 } ) ^ { 3 }$ given in an affine patch by $( x , y , z ) \ \mapsto \ ( x ^ { 2 } , y ^ { 2 } , z ^ { 2 } )$ is a $\mathbb { Z } _ { 2 } ^ { 3 }$ -cover of $B$ branched along $\Delta | _ { B }$ .
To show that $\widetilde { S }$ is smooth, we first observe that $\widetilde { S }$ is smooth in the complement of the ramification locus because $B$ is smooth.
If $\widetilde { S }$ is singular at a point in the ramification locus, then one can explicitly compute using the equation of $\widetilde { S }$ that one of the irreducible components of $\Delta$ restricts to $B$ giving a reducible curve, which is against our assumptions.
Therefore $\widetilde { S }$ is smooth, implying that $\widetilde { S }$ is a K3 surface (see Example 4.4). If $\iota$ is the involution $( \mathbb { P } ^ { 1 } ) ^ { 3 } \to ( \mathbb { P } ^ { 1 } ) ^ { 3 }$ given in an affine patch by $( x , y , z ) \mapsto ( - x , - y , - z )$ , then $S = \widetilde { S } / \langle \iota \rangle$ is a $D _ { 1 , 6 }$ -polarized Enriques surface.

# 8.1.4 The moduli space $\overline { { M } } _ { Q }$

Let $B \subset ( \mathbb { P } ^ { 1 } ) ^ { 3 }$ as in Proposition 8.14. Denote by $Q$ the unit cube.
Then, according to Definition 6.4, $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , B )$ is a stable toric pair of type $\leq Q$ .
Let $\overline { { M } } _ { Q }$ be the projective coarse moduli space parametrizing these pairs and their degenerations (see Theorem 6.9). In the next proposition we prove some first properties of $\overline { { M } } _ { Q }$ , and we can see how the geometry of $\overline { { M } } _ { Q }$ interacts with the combinatorics of the polyhedral subdivisions of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ .

Notation 8.16. Let $X$ be a scheme.
We denote by $X ^ { \nu }$ the normalization of $X$ with the reduced scheme structure.

Proposition 8.17. Let $Q \subset \mathbb { Z } ^ { 3 }$ be the unit cube.
Then the coarse moduli space $\overline { { M } } _ { Q }$ is irreducible and has dimension 4.

Proof.
The irreducibility of $M _ { Q }$ follows from the fact that, if $\mathcal { P }$ is any polyhedral subdivisions of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ , then $\mathcal { P }$ is regular and $H ^ { 1 } ( \mathcal { P } , \underline { { T } } ) ~ = ~ \{ 1 \}$ (see Proposition 5.15 and Section 6.3 respectively).

For the dimension count, we know that $\overline { { M } } _ { Q } ^ { \nu }$ is the projective toric variety associated to the secondary polytope $\Sigma ( Q \cap \mathbb { Z } ^ { 3 } )$ (see [Pfe00] for a complete description of this polytope), which has dimension $\# ( Q \cap \mathbb { Z } ^ { 3 } ) - \dim ( Q ) - 1 = 4$ (see Theorem 5.12). In conclusion, $\mathrm { d i m } ( M _ { Q } ) = 4$ .

# 8.1.5 The moduli space $\overline { { M } } _ { D _ { 1 , 6 } }$

With reference to Section 7.4.2, consider the moduli stack $\overline { { \mathcal { M } } } _ { C } = \overline { { \mathcal { M } } } _ { d , N , C , \underline { { b } } }$ with $d = 2$ , $\underline { { b } } =$ $( b _ { 1 } , b _ { 2 } , b _ { 3 } ) = \left( \frac { 1 + \epsilon } { 2 } , \frac { 1 + \epsilon } { 2 } , \frac { 1 + \epsilon } { 2 } \right)$ (because we want three pairs of divisors, and we do not distinguish divisors in the same pair) where $0 ~ < ~ \epsilon ~ \ll ~ 1$ is a fixed rational number and $C = 6 \epsilon ^ { 2 }$ (given $\left( B , \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) \Delta | _ { B } \right)$ as in Proposition 8.14, it is easy to compute that $( K _ { B } + ( { \textstyle { \frac { 1 + \epsilon } { 2 } } } ) \Delta | _ { B } ) ^ { 2 } = 6 \epsilon ^ { 2 }$ ).
For a suitably chosen positive integer $N$ depending on $d , \underline { { b } }$ , and $C$ (which does not need to be specified, see [Ale96b, 3.13]), the Viehweg’s moduli functor $\overline { { \mathcal { M } } } _ { 6 \epsilon ^ { 2 } }$ above is coarsely represented by a projective scheme, which we denote by $\overline { { M } } _ { 6 \epsilon ^ { 2 } }$ .
This is true because we are working with surface pairs ( $d = 2$ ) and our coefficients are strictly greater than $\frac { 1 } { 2 }$ (see [Ale15, Theorem 1.6.1, case 2]).

Observation 8.18. The group $S _ { 3 }$ has a natural action on the Viehweg moduli stack $\overline { { \mathcal { M } } } _ { 6 \epsilon ^ { 2 } }$ given by permuting the labels of the three divisors $\mathfrak { B } _ { 1 } , \mathfrak { B } _ { 2 } , \mathfrak { B } _ { 3 }$ .
In particular, we have an induced $S _ { 3 }$ -action on the coarse moduli space $\overline { { M } } _ { 6 \epsilon ^ { 2 } }$ .

Now we want to identify inside $\boldsymbol { M } _ { 6 \epsilon ^ { 2 } } / \boldsymbol { S } _ { 3 }$ the Zariski closed subscheme containing a dense open subset whose points parametrize the stable pairs given by $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ together with our three undistinguished pairs of lines of weight $\frac { 1 + \epsilon } { 2 }$ .
The next lemma allows us to do so.

Lemma 8.19. The coarse moduli space $\overline { { M } } _ { Q }$ contains a dense open subset U which is a fine moduli space parametrizing all the stable toric pairs $( X , B )$ with $X \cong ( \mathbb { P } ^ { 1 } ) ^ { 3 }$ .
U is isomorphic to the dense open subtorus of the toric variety $\overline { { M } } _ { Q } ^ { \nu }$ .
The universal family on $\boldsymbol { \mathcal { U } }$ is of the form $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } \times \mathcal { U } , \mathfrak { S } )$ .

Proof.
Let $\mathcal { P }$ be the complex of polytopes given by $Q$ and its faces.
Let $C$ be the set of vertices of $Q$ .
Following [Ale02, Definition 2.6.6], let MP ${ \mathrm { ~ \operatorname ~ { ~ f ~ r ~ } ~ } } [ { \mathcal { P } } , C ] ( \mathbb { k } )$ be the groupoid of stable toric pairs $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , B )$ over $\Bbbk$ with the linearized line bundle $\mathcal { O } _ { ( \mathbb { P } ^ { 1 } ) ^ { 3 } } ( B )$ in which the arrows are the isomorphisms identical on the torus $T$ .
By [Ale02, Lemma 2.6.7], we have that $\mathrm { M P } ^ { \mathrm { f r } } [ \mathcal { P } , C ] ( \mathbb { k } )$ is equivalent to the quotient stack $\big [ \mathbb { G } _ { m } ^ { 8 } / \mathbb { G } _ { m } ^ { 4 } \big ]$ , where $\mathbb { G } _ { m } ^ { 8 }$ represents the space of coefficients of the divisor $B =$ $\begin{array} { r } { V \left( \sum _ { i , j , k = 0 , 1 } c _ { i j k } X _ { i } Y _ { j } Z _ { k } \right) } \end{array}$ on $( \mathbb { P } ^ { 1 } ) ^ { 3 }$ and $( \lambda , \mu _ { 1 } , \mu _ { 2 } , \mu _ { 3 } ) \in \mathbb { G } _ { m } ^ { 4 }$ acts on $\mathbb { G } _ { m } ^ { \aleph }$ as follows:

$$
( \lambda , \mu _ { 1 } , \mu _ { 2 } , \mu _ { 3 } ) \cdot ( \ldots , c _ { i j k } , \ldots ) = ( \ldots , \lambda \mu _ { 1 } ^ { i } \mu _ { 2 } ^ { j } \mu _ { 3 } ^ { k } c _ { i j k } , \ldots ) .
$$

Observe that the quotient $\mathbb { G } _ { m } ^ { \aleph } / \mathbb { G } _ { m } ^ { 4 }$ exists as a scheme and it is isomorphic to $\mathbb { G } _ { m } ^ { 4 }$ .
The stabilizers of the action $\mathbb { G } _ { m } ^ { 4 } \cap \mathbb { G } _ { m } ^ { 8 }$ are trivial.
It follows that the quotient stack $[ \mathbb { G } _ { m } ^ { \aleph } / \mathbb { G } _ { m } ^ { 4 } ]$ is finely represented by $\mathbb { G } _ { m } ^ { \aleph } / \mathbb { G } _ { m } ^ { 4 }$ .
This gives us a dense open subset $\boldsymbol { \mathcal { U } }$ of $\overline { { M } } _ { Q }$ isomorphic to $\mathbb { G } _ { m } ^ { 4 }$ with a universal family which can be realized as the quotient of the pair $\begin{array} { r } { \left( ( \mathbb { P } ^ { 1 } ) ^ { 3 } \times \mathbb { G } _ { m } ^ { 8 } , V \left( \sum _ { i , j , k = 0 , 1 } c _ { i j k } X _ { i } Y _ { j } Z _ { k } \right) \right) } \end{array}$ under the $\mathbb { G } _ { m } ^ { 4 }$ -action on the coefficients $c _ { i j k }$ .
□

Definition 8.20. Let $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } \times \mathcal { U } , \mathfrak { S } )$ be the universal family over $\boldsymbol { \mathcal { U } }$ constructed in Lemma 8.19. Denote by $\mathcal { U } _ { \mathrm { s m } }$ the open subset of $\boldsymbol { \mathcal { U } }$ parametrizing stable toric pairs $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , B )$ such that $( B , \Delta | _ { B } )$ is as in Proposition 8.14. Let ${ \mathfrak { S } } _ { \mathrm { s m } }$ be the pullback of $\mathfrak { S } / \mathcal { U }$ along the inclusion $\mathcal { U } _ { \mathrm { s m } } \hookrightarrow \mathcal { U }$ .
Then $\left( { \mathfrak { S } _ { \mathrm { s m } } } , \left( \frac { 1 + \epsilon } { 2 } \right) \left( \Delta \times \mathcal { U } _ { \mathrm { s m } } \right) | _ { { \mathfrak { S } _ { \mathrm { s m } } } } \right) / \mathcal { U } _ { \mathrm { s m } }$ is a family for the moduli functor $\overline { { \mathcal { M } } } _ { 6 \epsilon ^ { 2 } }$ , and hence we have an induced morphism $f \colon { \mathcal { U } } _ { \mathrm { s m } } \to M _ { 6 \epsilon ^ { 2 } } / S _ { 3 }$ .
We define $M _ { D _ { 1 , 6 } }$ to be the closure of the image of $f$ .
In particular, by construction we have a dominant rational map $\overline { { { M } } } _ { Q } ^ { \nu } \ \xrightarrow { } - \overline { { { M } } } _ { D _ { 1 , 6 } }$ .

Observation 8.21. Let $p$ be a point in $\mathcal { U } _ { \mathrm { s m } }$ and let $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , B )$ be the corresponding stable toric pair.
Then the fiber of $f \colon \mathcal { U } _ { \mathrm { s m } }  \overline { { M } } _ { D _ { 1 , 6 } }$ over $f ( \boldsymbol p )$ is in bijection with the $\operatorname { S y m } ( Q )$ -orbit of $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } , B )$ (this follows from Proposition 8.14). In particular, $f$ is a quasi-finite map.
This, together with the fact that $f$ is dominant, implies that $\mathrm { d i m } ( M _ { D _ { 1 , 6 } } ) = \mathrm { d i m } ( \mathcal { U } _ { \mathrm { s m } } ) = \mathrm { d i m } ( M _ { Q } ) = 4$ .
$M _ { D _ { 1 , 6 } }$ is irreducible because $\mathcal { U } _ { \mathrm { s m } }$ is irreducible.
In conclusion, ${ \overline { { M } } } _ { D _ { 1 , 6 } }$ is a 4-dimensional irreducible projective coarse moduli space whose points in a dense open subset parametrize isomorphism classes of $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ together with the three undistinguished pairs of undistinguished weighted lines (and hence Enriques surfaces with our choice of divisor after an appropriate $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover).

# 8.2 Stable replacement in a one-parameter family

Let $Q$ be the unit cube and let $( A , { \mathfrak { m } } )$ be a DVR.
Let $( { \mathfrak { X } } , { \mathfrak { B } } )$ be a family of stable toric pairs of type $\leq Q$ over Spec $( A )$ .
Define $X = { \mathfrak { X } } _ { \mathfrak { m } }$ , $B = \mathfrak { B } _ { \mathfrak { m } }$ , and assume that the fiber of $\boldsymbol { \mathcal { X } }$ over the generic point is isomorphic to $( { \mathbb { P } } ^ { 1 } ) _ { K } ^ { 3 }$ where $K$ is the field of fractions of $A$ .
Observe that the pair $\left( B , \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) \Delta | _ { B } \right)$ may be not stable: to start with, the restriction $\Delta | _ { B }$ makes no sense if $\Delta$ is not $\mathbb { Q }$ - Cartier (see Proposition 8.28). In this section we define a new family $( { \mathfrak { X } } ^ { \bullet } , { \mathfrak { B } } ^ { \bullet } )$ which is isomorphic to the original one in the complement of the central fiber, but the new central fiber $( X ^ { \bullet } , B ^ { \bullet } )$ is such that $\left( B ^ { \bullet } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \Delta ^ { \bullet } | _ { B ^ { \bullet } } \right)$ is a stable pair ( $\Delta ^ { \bullet }$ denotes the toric boundary of $X ^ { \bullet }$ ).
The stability of the pair $\left( B ^ { \bullet } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \Delta ^ { \bullet } | _ { B ^ { \bullet } } \right)$ is proved later in Section 8.3.

# 8.2.1 Families of stable toric pairs over a DVR

Let $( A , { \mathfrak { m } } )$ be a DVR with field of fractions $K$ , uniformizing parameter $t$ , and residue field our fixed base field $\Bbbk$ .
Let $T$ be a torus over $\Bbbk$ with character lattice $M$ .
Let $Q \subset M _ { \mathbb { R } }$ be a lattice polytope.
Define

$$
\theta = \sum _ { m \in Q \cap M } c _ { m } ( t ) t ^ { h ( m ) } x ^ { ( 1 , m ) } ,
$$

where, for all $m \in Q \cap M$ , $c _ { m } ( t ) \in A$ , $c _ { m } ( 0 ) \in \mathbb { k } ^ { * }$ , and $h ( m ) \in \mathbb { Z }$ .
Observe that the map $m \mapsto h ( m )$ gives a height function $h \colon Q \cap M \to \mathbb { Z }$ .
Let $Q ^ { + } \subset M _ { \mathbb { R } } \oplus \mathbb { R }$ be the convex hull of the half-lines $( m , h ( m ) + \mathbb { R } _ { \ge 0 } )$ , $m \in Q \cap M$ , and let $\operatorname { C o n e } ( Q ^ { + } ) \subset \mathbb { R } \oplus M _ { \mathbb { R } } \oplus \mathbb { R }$ be the cone over $( 1 , Q ^ { + } )$ with vertex at the origin.
Then $h$ defines the following $( \mathbb { Z } \oplus M )$ -graded $A$ -algebra:

$$
R = A [ t ^ { \ell } x ^ { ( d , m ) } \mid ( d , m , \ell ) \in \operatorname { C o n e } ( Q ^ { + } ) \cap ( \mathbb { Z } \oplus M \oplus \mathbb { Z } ) ] .
$$

Observe that $\theta \in R$ is an element of $\mathbb { Z }$ -degree 1. Let $( { \mathfrak { X } } , { \mathfrak { B } } ) / { \operatorname { S p e c } } ( A )$ be the family of stable toric pairs associated to $( R , \theta )$ (see Remark 6.7). If $\eta$ is the generic point of Spec $( A )$ , then $\mathfrak { X } _ { \eta } =$ $Y \times \mathrm { S p e c } ( K )$ , where $Y$ is the toric variety associated to the polytope $Q$ .
The central fiber $\left( \mathfrak { X } _ { \mathfrak { m } } , \mathfrak { B } _ { \mathfrak { m } } \right)$ is a stable toric pair whose corresponding polyhedral subdivision of $( Q , Q \cap M )$ is induced by the height function $h$ (hence, it is a regular subdivision).
The equation of ${ \mathfrak { B } } _ { \mathfrak { m } }$ is given by

$$
\sum _ { m \in Q \cap M } c _ { m } ( 0 ) x ^ { ( 1 , m ) } = 0 .
$$

For more details about this construction we refer to [Ale02, Section 2.8].

# 8.2.2 Corner cuts

Definition 8.22. Let $Q$ be the unit cube.
We call corner cut a subpolytope of $Q$ which is equal to the convex hull of the points $( 0 , 0 , 0 ) , ( 1 , 0 , 0 ) , ( 0 , 1 , 0 ) , ( 0 , 0 , 1 )$ up to a symmetry of $Q$ .
An example of corner cut can be found in Figure 8.1 on the left.
We call apex the vertex of a corner cut which is at the intersection of three edges of the cube.

Notation 8.23. Let $\mathcal { P }$ be a polyhedral subdivision of a lattice polytope $Q$ .
We denote by $\mathcal { P } _ { i }$ the set of $i$ -dimensional faces in $\mathcal { P }$ .

Definition 8.24. Let $\mathcal { P }$ be a polyhedral subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ .
We define a polyhedral subdivision $\mathcal { P } ^ { \bullet }$ of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ via the following algorithm:

(1) $\mathcal { R } = \mathcal { P } ;$  
(2) If $\mathcal { R }$ contains no corner cut, define $\mathcal { P } ^ { \bullet } = \mathcal { R }$ and stop.
Otherwise, go to step (3);  
(3) Let $P \in \mathcal { R }$ be a corner cut and let $R \in \mathcal { R }$ be that unique polytope sharing exactly a facet with $P$ .
Define

$$
S = ( \mathcal { R } _ { 3 } \setminus \{ P , R \} ) \cup \{ P \cup R \} .
$$

Then redefine $\mathcal { R }$ to be the polyhedral subdivision of $Q$ generated by $\boldsymbol { S }$ .
Go to step (2).

In Figure 8.1 we give an explicit example of $\mathcal { P } ^ { \bullet }$ given $\mathcal { P }$ .

![](images/240d73681b5dd87eb9968b72696a7944ebe0164353a4696e2c7a55f283a6dada.jpg)  
Figure 8.1: Modification $\mathcal { P } ^ { \bullet }$ of the polyhedral subdivision $\mathcal { P }$

# 8.2.3 The modified family $( { \mathfrak { X } } ^ { \bullet } , { \mathfrak { P } } ^ { \bullet } )$

Let us adopt the same notation introduced in Section 8.2.1, but set $Q$ to be the unit cube.
We define another $( \mathbb { Z } \oplus M )$ -graded $A$ -algebra induced by $\theta$ as follows.
Denote by $\mathcal { P }$ the regular polyhedral subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ associated to $( { \mathfrak { X } } _ { \mathfrak { m } } , { \mathfrak { B } } _ { \mathfrak { m } } )$ .
Assume $P \in \mathcal { P } _ { 3 }$ is a corner cut and let $P ^ { \prime } \in \mathcal { P }$ be that unique polytope sharing exactly a facet with $P$ .
Denote by $L$ the unique hyperplane in $\mathbb { R } ^ { 3 } \oplus \mathbb { R }$ containing the points $( m , h ( m ) )$ for $m \in P ^ { \prime } \cap \mathbb { Z } ^ { 3 }$ .
If $m$ is the apex of the corner cut $P$ , then there exists a unique positive rational number $q _ { m }$ such that $( m , h ( m ) - q _ { m } ) \in L$ .
Moreover, up to a ramified finite base change, we can assume that $q _ { m }$ is integral.
Let us consider the height function

$$
h ^ { \bullet } ( m ) = \left\{ \begin{array} { l l } { { h ( m ) - q _ { m } } } & { { \mathrm { i f ~ } m { \mathrm { ~ i s ~ t h e ~ a p e x ~ o f ~ a ~ c o r n e r ~ c u t , } } } } \\ { { } } & { { } } \\ { { h ( m ) } } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right.
$$

Define a new $( \mathbb { Z } \oplus M )$ -graded $A$ -algebra $R ^ { \bullet }$ as we did in Section 8.2.1, but using $h ^ { \bullet }$ in place of $h$ .
Observe that $R \subset R ^ { \bullet }$ is a degree preserving embedding of graded algebras.
Therefore $\theta \in R ^ { \bullet }$ is an element of $\mathbb { Z }$ -degree 1 and the pair $( R ^ { \bullet } , \theta )$ corresponds to a family ${ \mathfrak { X } } ^ { \bullet } / \operatorname { S p e c } ( A )$ of stable toric varieties together with a Cartier divisor $\mathfrak { B } ^ { \bullet } \subset \mathfrak { X } ^ { \bullet }$ given by the vanishing of $\theta$ .
Observe that $( { \mathfrak { X } } _ { \eta } , { \mathfrak { B } } _ { \eta } )$ and $( ( { \mathfrak { X } } ^ { \bullet } ) _ { \eta } , ( { \mathfrak { B } } ^ { \bullet } ) _ { \eta } )$ are isomorphic over Spec $( K )$ by construction.
The central fiber $( ( \mathfrak { X ^ { \bullet } } ) _ { \mathfrak { m } } , ( \mathfrak { B ^ { \bullet } } ) _ { \mathfrak { m } } )$ is not a stable toric pair if and only if $\mathcal { P }$ contains corner cuts.
However, $\big ( ( \boldsymbol { \mathfrak { X } } ^ { \bullet } ) _ { \mathfrak { m } } , \mathcal { O } \big ( ( \mathfrak { B } ^ { \bullet } ) _ { \mathfrak { m } } \big ) \big )$ is always a polarized stable toric variety whose corresponding polyhedral subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ is $\mathcal { P } ^ { \bullet }$ (see Definition 8.24). The equation of $( { \mathfrak { B } } ^ { \bullet } ) _ { \mathfrak { m } }$ is given by

$$
\sum _ { m \in Q \cap M , \atop n { \mathrm { ~ i s ~ n o t ~ a n ~ a p e x } } } c _ { m } ( 0 ) x ^ { ( 1 , m ) } = 0 .
$$

Observe that if $\mathcal { P }$ has no corner cuts, then $( { \mathfrak { X } } , { \mathfrak { B } } ) = ( { \mathfrak { X } } ^ { \bullet } , { \mathfrak { B } } ^ { \bullet } )$ .

Remark 8.25. With the same notation introduced above, denote by $( X , B )$ (resp.
$( X ^ { \bullet } , B ^ { \bullet } ) _ { . }$ ) the central fiber of $( { \mathfrak { X } } , { \mathfrak { B } } )$ (resp.
$( { \mathfrak { X } } ^ { \bullet } , { \mathfrak { B } } ^ { \bullet } ) _ { , }$ ).
Then $( X ^ { \bullet } , B ^ { \bullet } )$ only depends on $( X , B )$ and it is independent from the whole family $( { \mathfrak { X } } , { \mathfrak { B } } ) / { \operatorname { S p e c } } ( A )$ .

Definition 8.26. Let $( X , B )$ be a stable toric pair of type $\leq Q$ .
Define $( X ^ { \bullet } , B ^ { \bullet } )$ to be the central fiber of $( { \mathfrak { X } } ^ { \bullet } , { \mathfrak { B } } ^ { \bullet } )$ , where $( { \mathfrak { X } } , { \mathfrak { B } } ) / { \operatorname { S p e c } } ( A )$ is any one-parameter family with central fiber $( X , B )$ and smooth generic fiber (such a family exists because $\overline { { M } } _ { Q }$ is irreducible, hence $( X , B )$ is smoothable).
The pair $( X ^ { \bullet } , B ^ { \bullet } )$ is well defined by Remark 8.25. Observe that, if $\mathcal { P }$ has no corner cuts, then $( \boldsymbol { X } , \boldsymbol { B } ) = ( \boldsymbol { X ^ { \bullet } } , \boldsymbol { B ^ { \bullet } } )$ .

# 8.3 Analysis of stability

# 8.3.1 Preliminaries

Throughout this section let $Q$ be the unit cube.
We show that if $( X , B )$ is a stable toric pair of type $\leq Q$ , then $( B ^ { \bullet } , ( { \textstyle \frac { 1 + \epsilon } { 2 } } ) \Delta ^ { \bullet } | _ { B _ { P } ^ { \bullet } } )$ is stable.
Before formally stating this result, we need some preliminaries.

Notation 8.27. Consider a stable toric pair $( X , B )$ of type $\leq Q$ and let $\mathcal { P }$ be the corresponding polyhedral subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ .
Let $\Pi _ { P \in { \mathcal P } _ { 3 } } X _ { P }  X$ be the normalization of $X$ , where $X _ { P }$ is the toric variety corresponding to the polytope $P$ .
Then we denote by $\Delta _ { P }$ the toric boundary of $X _ { P }$ , by $D _ { P } \subset X _ { P }$ the conductor divisor, and by $B _ { P }$ the restriction to $X _ { P }$ of the preimage of $B$ under the normalization morphism.
Define $X _ { P } ^ { \bullet } , \Delta _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } , B _ { P } ^ { \bullet }$ analogously with $( X ^ { \bullet } , B ^ { \bullet } )$ in place of $( X , B )$ .

Proposition 8.28. Let $( X , B )$ be a stable toric pair of type $\leq Q$ and let $\mathcal { P }$ be the associated polyhedral subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ .
If $_ { \mathcal { P } }$ does not contain a corner cut, then $\Delta$ is Cartier.
If $_ { \mathcal { P } }$ contains a corner cut, then $\Delta$ is not $\mathbb { Q }$ -Cartier.

Proof.
Define a piecewise linear function on the normal fan of each maximal dimensional polytope $P \in \mathcal { P }$ as follows: associate to the $\mathbb { Z }$ -generators of the rays, negative the lattice distance between the facet of $2 P$ normal to the ray and the lattice point $( 1 , 1 , 1 )$ .
Observe that this number is 0 if the facet contains $( 1 , 1 , 1 )$ , and $- 1$ otherwise.
If $_ { \mathcal { P } }$ has no corner cuts, then this gives a Cartier divisor on $X$ equal to $\Delta$ .

Now assume $\mathcal { P }$ contains a corner cut $P$ .
Denote with $R$ that unique polytope in $_ { \mathcal { P } }$ sharing exactly a facet with $P$ .
Let $\ell _ { 1 } , \ell _ { 2 } , \ell _ { 3 }$ be the three edges of $P$ which do not contain the apex. Observe that $\ell _ { i }$ can be contained in two or three maximal dimensional polytopes in $\mathcal { P }$ ( $P$ and $R$ included), $i = 1 , 2 , 3$ .

If some $\ell _ { i }$ is contained in three maximal dimensional polytopes, then take a point $x \in X$ lying on the torus invariant line corresponding to $\ell _ { i }$ .
If $\Delta$ is $\mathbb { Q }$ -Cartier, then $m \Delta$ is given by the vanishing of one equation in an open neighborhood of $x$ for some $m > 0$ .
However, the vanishing locus of this equation on $X _ { R }$ has codimension 2, which cannot be.

Assume that each $\ell _ { i }$ is only contained in $P$ and $R$ .
Denote by $\nu \colon X ^ { \nu } \to X$ the normalization.
If $\Delta$ is $\mathbb { Q }$ -Cartier, then $( \nu ^ { * } \Delta ) | _ { X _ { R } } = \Delta _ { R } - D _ { R }$ is also $\mathbb { Q }$ -Cartier.
But this is a contradiction because there is no $\mathbb { Q }$ -piecewise linear function on the normal fan of $R$ corresponding to $\Delta { { _ R } } - D _ { R }$ (consider the normal cone to a vertex of $R$ in common with $P$ ).
□

Theorem 8.29. Let $Q$ be the unit cube and let $( X , B )$ be a stable toric pair of type $\leq Q$ .
Consider $( X ^ { \bullet } , B ^ { \bullet } )$ as in Definition 8.26. Then $\left( B ^ { \bullet } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \Delta ^ { \bullet } | _ { B ^ { \bullet } } \right)$ is a stable pair (it makes sense to consider $\Delta ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ by Proposition 8.28).

# 8.3.2 Proof of Theorem 8.29

Let $\mathcal { P }$ be the polyhedral subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ associated to $( X , B )$ .
We show that for all $P \in \mathcal { P } ^ { \bullet }$ , the pair $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ is stable.
It is easy to observe that there are four possibilities for $P$ up to symmetries of $Q$ as shown in Figure 8.2.

Definition 8.30. We say that $P \in \mathcal { P } ^ { \bullet }$ has type $( a )$ (resp.
$( b ) , ( c ) , ( d ) )$ if $P$ is equal to the polytope in Figure 8.2 ( $a$ ) (resp.
$( b ) , ( c ) , ( d ) )$ up to a symmetry of $Q$ .

Proposition 8.31. Given $P$ of type $( a )$ , then the pair $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ is a stable pair.

![](images/a066370dfe97ddddce5e24bc566b740b5dd6907011472c04005876e1ae088db4.jpg)  
Figure 8.2: Possible maximal dimensional polytopes in $\mathcal { P } ^ { \bullet }$ up to symmetries of $Q$

Proof.

$$
\begin{array} { r l } & { X _ { P } ^ { \bullet } = \mathbb { P } ^ { 3 } \ni [ W _ { 0 } : \ldots : W _ { 3 } ] , } \\ & { D _ { P } ^ { \bullet } = V ( W _ { 0 } ) + V ( W _ { 1 } ) , } \\ & { \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } = V ( W _ { 2 } ) + V ( W _ { 3 } ) , } \\ & { B _ { P } ^ { \bullet } = V ( a _ { 0 } W _ { 0 } + \ldots + a _ { 3 } W _ { 3 } ) , } \end{array}
$$

where $a _ { i } \neq 0$ for all $i = 0 , \ldots , 3$ .
To find the equation of $B _ { P } ^ { \bullet }$ we used Remark 6.5, and $a _ { i } \neq 0$ for all $i$ because there is no corner cut that can possibly be contained in $P$ (see the construction of $( X ^ { \bullet } , B ^ { \bullet } )$ in Section 8.2.3). Then $B _ { P } ^ { \bullet }$ is isomorphic to $\mathbb { P } ^ { 2 }$ and $\Delta _ { P } ^ { \bullet }$ restricts to $B _ { P } ^ { \bullet }$ giving four lines in general linear position, implying that $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ is log canonical.
Finally, if $L$ denotes a general line in $B _ { P } ^ { \bullet }$ , then

$$
K _ { B _ { P } ^ { \bullet } } + D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \frac { 1 + \epsilon } { 2 } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \sim \epsilon L ,
$$

which is ample.

The next lemma is used in the analysis of the cases $P$ of type $( b ) , ( c ) , ( d )$ .

Lemma 8.32. Let $L _ { 1 } , L _ { 2 } , L _ { 3 }$ be three distinct lines in A $^ 2$ through the point $( 0 , 0 )$ .
Then the pair $\left( \mathbb { A } ^ { 2 } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \left( L _ { 1 } + L _ { 2 } + L _ { 3 } \right) \right)$ is log canonical.

Proof.
Consider the blow up morphism $\sigma \colon \mathrm { B l } _ { ( 0 , 0 ) } \mathbb { A } ^ { 2 } \to \mathbb { A } ^ { 2 }$ and let $E$ be the exceptional divisor.

Then we have that

$$
\begin{array} { l } { { \displaystyle K _ { \mathrm { B l } _ { ( 0 , 0 ) } \mathbb { A } ^ { 2 } } + \sigma _ { * } ^ { - 1 } \left( \left( \frac { 1 + \epsilon } { 2 } \right) \sum _ { i = 1 } ^ { 3 } L _ { i } \right) = \sigma ^ { * } \left( K _ { \mathbb { A } ^ { 2 } } + \left( \frac { 1 + \epsilon } { 2 } \right) \sum _ { i = 1 } ^ { 3 } L _ { i } \right) + a E } } \\ { { \displaystyle \implies E = 3 \left( \frac { 1 + \epsilon } { 2 } \right) E + a E } } \\ { { \displaystyle \implies a = - \frac { 1 + 3 \epsilon } { 2 } > - 1 } . } \end{array}
$$

Therefore, $\left( \mathbb { A } ^ { 2 } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \left( L _ { 1 } + L _ { 2 } + L _ { 3 } \right) \right)$ is log canonical because $\sigma$ is a log resolution (see Proposition 7.7).

Proposition 8.33. Given $P$ of type $( b )$ , then the pair $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ is a stable pair.

Proof.

$$
\begin{array} { r l } & { X _ { P } ^ { \bullet } = V ( W _ { 0 } W _ { 1 } - W _ { 2 } W _ { 3 } ) \subset \mathbb { P } ^ { 4 } \ni [ W _ { 0 } : \dots : W _ { 4 } ] , } \\ & { D _ { P } ^ { \bullet } = V ( W _ { 0 } , W _ { 2 } ) + V ( W _ { 0 } , W _ { 3 } ) = V ( W _ { 0 } W _ { 1 } - W _ { 2 } W _ { 3 } , W _ { 0 } ) , } \\ & { \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } = V ( W _ { 1 } , W _ { 2 } ) + V ( W _ { 1 } , W _ { 3 } ) + V ( W _ { 0 } W _ { 1 } - W _ { 2 } W _ { 3 } , W _ { 4 } ) } \\ & { \qquad \quad = V ( W _ { 0 } W _ { 1 } - W _ { 2 } W _ { 3 } , W _ { 1 } ) + V ( W _ { 0 } W _ { 1 } - W _ { 2 } W _ { 3 } , W _ { 4 } ) , } \\ & { B _ { P } ^ { \bullet } = V ( a _ { 0 } W _ { 0 } + \dots + a _ { 4 } W _ { 4 } ) \cap X _ { P } ^ { \bullet } , } \end{array}
$$

where $a _ { i } \neq 0$ for $i = 1 , \dots , 4$ and $a _ { 0 }$ can possibly vanish (we can have at most one corner cut contained in $P$ ).
$B _ { P } ^ { \bullet } \cong \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ because it is a hyperplane section of the projective cone $X _ { P } ^ { \bullet }$ which does not pass through the vertex.

Now let us study the restrictions of $D _ { P } ^ { \bullet }$ and $\Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet }$ to $B _ { P } ^ { \bullet }$ .
This boils down to understand how the coordinate hyperplanes $H _ { i } = V ( W _ { i } )$ , $i = 0 , \dots , 4$ , restrict to $B _ { P } ^ { \bullet }$ .
First of all, observe that $H _ { i }$ cuts on $B _ { P } ^ { \bullet }$ a curve $C$ of divisor class $( 1 , 1 )$ .
To show this, denote by $( a , b )$ the divisor class of $C = B _ { P } ^ { \bullet } \cap H _ { i }$ .
If $H ^ { \prime } = V ( a _ { 0 } W _ { 0 } + . . . + a _ { 4 } W _ { 4 } )$ and $H$ is a general hyperplane in $\mathbb { P } ^ { 4 }$ , then the self-intersection of $C$ is given by

$$
C ^ { 2 } = H _ { i } | _ { B _ { P } ^ { \bullet } } \cdot H _ { i } | _ { B _ { P } ^ { \bullet } } = H _ { i } \cdot H _ { i } \cdot B _ { P } ^ { \bullet } = H _ { i } \cdot H _ { i } \cdot X _ { P } ^ { \bullet } \cdot H ^ { \prime } = H _ { i } \cdot H _ { i } \cdot 2 H \cdot H ^ { \prime } = 2 .
$$

On the other hand, $C ^ { 2 } = ( a , b ) ^ { 2 } = 2 a b = 2$ , implying that $( a , b ) = ( 1 , 1 )$ .
For $i \neq 4$ , $H _ { i } \cap B _ { P } ^ { \bullet }$ is always reducible, so it is given by two curves of divisor classes $( 1 , 0 )$ and $( 0 , 1 )$ .
If $a _ { 0 } \neq 0$ , then it is easy to check that $H _ { 4 } \cap B _ { P } ^ { \bullet }$ is smooth for a general choice of the coefficients, but it can possibly break into two curves.
In any case, $\Delta _ { P } ^ { \bullet }$ restricts to $B _ { P } ^ { \bullet }$ giving a simple normal crossing divisor, implying that $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ is log canonical.

If $a _ { 0 } = 0$ , then $H _ { 4 } \cap B _ { P } ^ { \bullet }$ is irreducible, but it passes through the singular point of $H _ { 1 } \cap B _ { P } ^ { \bullet }$ .
However, we have that $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ is log canonical by Lemma 8.32.

Finally, observe that

$$
K _ { B _ { P } ^ { \bullet } } + D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \frac { 1 + \epsilon } { 2 } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \sim ( - 2 , - 2 ) + ( 1 , 1 ) + \left( \frac { 1 + \epsilon } { 2 } \right) ( 2 , 2 ) = \epsilon ( 1 , 1 ) .
$$

which is ample.

Proposition 8.34. Given $P$ of type $( c )$ , then the pair $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ is a stable pair.

Proof.

$$
\begin{array} { r l } & { X _ { P } ^ { \bullet } = \mathbb { P } ^ { 2 } \times \mathbb { P } ^ { 1 } \ni \big ( [ X _ { 0 } : X _ { 1 } : X _ { 2 } ] , [ Y _ { 0 } : Y _ { 1 } ] \big ) , } \\ & { D _ { P } ^ { \bullet } = V ( X _ { 2 } ) , } \\ & { \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } = V ( X _ { 0 } X _ { 1 } Y _ { 0 } Y _ { 1 } ) , } \\ & { B _ { P } ^ { \bullet } = V ( ( a _ { 0 } X _ { 0 } + a _ { 1 } X _ { 1 } + a _ { 2 } X _ { 2 } ) Y _ { 0 } + ( b _ { 0 } X _ { 0 } + b _ { 1 } X _ { 1 } + b _ { 2 } X _ { 2 } ) Y _ { 1 } ) . } \end{array}
$$

where $a _ { 0 } , a _ { 1 } , b _ { 0 } , b _ { 1 } \neq 0$ and exactly one among $a _ { 2 }$ and $b _ { 2 }$ can possibly be zero (there is at most one corner cut contained in $P$ ).
Let us start by assuming that $a _ { 2 } b _ { 2 } \neq 0$ .

If $B _ { P } ^ { \bullet }$ is singular, assume without loss of generality that there is a singular point in the affine patch where $X _ { 0 } \neq 0$ and $Y _ { 0 } \neq 0$ .
Let $\begin{array} { r } { x _ { i } = \frac { X _ { i } } { X _ { 0 } } } \end{array}$ , $i = 1 , 2$ , and $\begin{array} { r } { y = \frac { Y _ { 1 } } { Y _ { 0 } } } \end{array}$ be the coordinates in this affine patch.
Then the equation of $B _ { P } ^ { \bullet }$ becomes

$$
a _ { 0 } + a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + ( b _ { 0 } + b _ { 1 } x _ { 1 } + b _ { 2 } x _ { 2 } ) y = 0 .
$$

Therefore the following system of equations has a solution:

$$
\left\{ \begin{array} { l l } { a _ { 0 } + a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + ( b _ { 0 } + b _ { 1 } x _ { 1 } + b _ { 2 } x _ { 2 } ) y = 0 , } \\ { a _ { 1 } + b _ { 1 } y = 0 , } \\ { a _ { 2 } + b _ { 2 } y = 0 , } \\ { b _ { 0 } + b _ { 1 } x _ { 1 } + b _ { 2 } x _ { 2 } = 0 , } \end{array} \right. \Longrightarrow \left\{ \begin{array} { l l } { y = - \frac { a _ { 1 } } { b _ { 1 } } , } \\ { y = - \frac { a _ { 2 } } { b _ { 2 } } , } \\ { a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } = - a _ { 0 } , } \\ { b _ { 1 } x _ { 1 } + b _ { 2 } x _ { 2 } = - b _ { 0 } . } \end{array} \right.
$$

This implies that $a _ { 1 } b _ { 2 } - a _ { 2 } b _ { 1 } = 0 \quad$ , and therefore the two vectors $( a _ { 0 } , a _ { 1 } , a _ { 2 } )$ and $( b _ { 0 } , b _ { 1 } , b _ { 2 } )$ are proportional because the matrix $\left( \begin{array} { l l l } { a _ { 1 } } & { a _ { 2 } } & { - a _ { 0 } } \\ { b _ { 1 } } & { b _ { 2 } } & { - b _ { 0 } } \end{array} \right)$ has rank 1. If $( b _ { 0 } , b _ { 1 } , b _ { 2 } ) = \lambda ( a _ { 0 } , a _ { 1 } , a _ { 2 } )$ for $\lambda \in \mathbb { K } ^ { * }$ , then the equation of $B _ { P } ^ { \bullet }$ becomes

$$
( a _ { 0 } X _ { 0 } + a _ { 1 } X _ { 1 } + a _ { 2 } X _ { 2 } ) ( Y _ { 0 } + \lambda Y _ { 1 } ) = 0 ,
$$

where $V ( Y _ { 0 } + \lambda Y _ { 1 } ) \cong \mathbb { P } ^ { 2 }$ and $V ( a _ { 0 } X _ { 0 } + a _ { 1 } X _ { 1 } + a _ { 2 } X _ { 2 } ) \cong \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ are glued along a ruling of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ and the line $a _ { 0 } X _ { 0 } + a _ { 1 } X _ { 1 } + a _ { 2 } X _ { 2 } = 0$ in $\mathbb { P } ^ { 2 }$ .
The restrictions of $D _ { P } ^ { \bullet }$ and $\Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet }$ to these two irreducible components are described in Remark 8.37 ( $^ { c 3 }$ ).
In this case, to conclude that $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ is stable, we reduce the question to each connected component of the normalization of $B _ { P } ^ { \bullet }$ and we apply what we already proved in the $( a ) , ( b )$ cases (see the proofs of Propositions 8.31 and 8.33).

Now let us assume that $B _ { P } ^ { \bullet }$ is smooth (and hence irreducible).
By the discussion above, the two vectors $( a _ { 0 } , a _ { 1 } , a _ { 2 } )$ and $( b _ { 0 } , b _ { 1 } , b _ { 2 } )$ are not proportional.
Denote by $p$ the point of intersection of the two lines $a _ { 0 } X _ { 0 } + a _ { 1 } X _ { 1 } + a _ { 2 } X _ { 2 } = 0$ and $b _ { 0 } X _ { 0 } + b _ { 1 } X _ { 1 } + b _ { 2 } X _ { 2 } = 0$ in $\mathbb { P } ^ { 2 }$ .
If $\pi \colon B _ { P } ^ { \bullet } \to \mathbb { P } ^ { 2 }$ is the restriction to $B _ { P } ^ { \bullet }$ of the usual projection map $\mathbb { P } ^ { 2 } \times \mathbb { P } ^ { 1 } \to \mathbb { P } ^ { 2 }$ , observe that $\pi$ is an isomorphism if restricted to the complement of $\pi ^ { - 1 } ( p )$ and $\pi ^ { - 1 } ( p ) \cong \mathbb { P } ^ { 1 }$ .
This proves that $B _ { P } ^ { \bullet } \cong \mathbb { F } _ { 1 }$ .
In this case, let us explain how $D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ depends on the coefficients $a _ { i } , b _ { j }$ .
The restriction $D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ has equation

$$
\left\{ \begin{array} { l } { { X _ { 2 } = 0 , } } \\ { { ( a _ { 0 } X _ { 0 } + a _ { 1 } X _ { 1 } ) Y _ { 0 } + ( b _ { 0 } X _ { 0 } + b _ { 1 } X _ { 1 } ) Y _ { 1 } = 0 . } } \end{array} \right.
$$

By using an argument completely analogous to what we just did for $B _ { P } ^ { \bullet }$ , we have that this restriction is irreducible if and only if $( a _ { 0 } , a _ { 1 } )$ and $( b _ { 0 } , b _ { 1 } )$ are not proportional.
In this case, $D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ is a section of $B _ { P } ^ { \bullet }$ with self-intersection 1. If $( a _ { 0 } , a _ { 1 } )$ and $( b _ { 0 } , b _ { 1 } )$ are proportional, then the equation of $D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$

becomes

$$
\left\{ \begin{array} { l l } { { X _ { 2 } = 0 , } } \\ { { ( a _ { 0 } X _ { 0 } + a _ { 1 } X _ { 1 } ) ( Y _ { 0 } + \lambda Y _ { 1 } ) = 0 . } } \end{array} \right.
$$

for some $\lambda \in \mathbb { K } ^ { * }$ .
The irreducible component $V ( X _ { 2 } , a _ { 0 } X _ { 0 } + a _ { 1 } X _ { 1 } )$ (resp.
$V ( X _ { 2 } , Y _ { 0 } + \lambda Y _ { 1 } ) )$ is the exceptional section (resp.
a fiber) of $B _ { P } ^ { \bullet }$ .
We are left with understanding $( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } }$ , and for this we need to study how $V ( X _ { i } ) , V ( Y _ { i } )$ , $i = 0 , 1$ , restrict to $B _ { P } ^ { \bullet }$ .
But $V ( Y _ { i } )$ restricts giving a fiber, and we can study $V ( X _ { i } ) | _ { B _ { P } ^ { \bullet } }$ in the same way we did for $D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ .
Observe that at most one among $V ( X _ { 0 } ) | _ { B _ { P } ^ { \bullet } } , V ( X _ { 1 } ) | _ { B _ { P } ^ { \bullet } } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ can be reducible (otherwise $B _ { P } ^ { \bullet }$ would be reducible).
We conclude that $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ is log canonical.

Now we consider the case where exactly one among $a _ { 2 }$ and $b _ { 2 }$ is zero.
It is easy to check that $B _ { P } ^ { \bullet }$ is automatically smooth and a similar description to the one above applies, with the only difference that the restriction $( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } }$ can acquire a triple intersection point.
But then we can apply Lemma 8.32 to conclude that $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ is log canonical.

For the ampleness condition, on $B _ { P } ^ { \bullet } \cong \mathbb { F } _ { 1 }$ denote by $h$ a section of self-intersection 1 and by $f$ a fiber.
Then

$$
, + D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \frac { 1 + \epsilon } { 2 } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \sim - 2 h - f + h + \left( \frac { 1 + \epsilon } { 2 } \right) ( 2 h + 2 f ) = \epsilon ( h + f ) .
$$

which is ample.

To deal with the last case (type $( d )$ ), we need an additional preliminary lemma.

Lemma 8.35. Let $H _ { 1 } , H _ { 2 } , H _ { 3 }$ , and $H$ be four distinct planes in A $^ 3$ through the origin in general position.
Then $\begin{array} { r } { \left( \mathbb { A } ^ { 3 } , \left( \frac { 1 + \epsilon } { 2 } \right) \left( H _ { 1 } + H _ { 2 } + H _ { 3 } \right) + H \right) } \end{array}$ is log canonical.

Proof.
Consider the blow up morphism $f \colon \mathrm { B l } _ { ( 0 , 0 , 0 ) } \mathbb { A } ^ { 3 } \to \mathbb { A } ^ { 3 }$ and let $E$ be the exceptional divisor.
If $\textstyle \alpha = { \frac { 1 + \epsilon } { 2 } } $ , then we have that

$$
\begin{array} { r l } & { \dot { \mathcal { C } } _ { \mathrm { B l } _ { ( 0 , 0 , 0 ) } , \mathbb { A } ^ { 3 } } + f _ { * } ^ { - 1 } \big ( \alpha \big ( H _ { 1 } + H _ { 2 } + H _ { 3 } \big ) + H \big ) = f ^ { * } \big ( K _ { \mathbb { A } ^ { 3 } } + \alpha \big ( H _ { 1 } + H _ { 2 } + H _ { 3 } \big ) + H \big ) + a E } \\ & { \qquad \implies 2 E = ( 3 \alpha + 1 ) E + a E } \\ & { \qquad \implies a = ( - 3 \alpha + 1 ) > - 1 . } \end{array}
$$

This implies that $\begin{array} { r } { \left( \mathbb { A } ^ { 3 } , \left( \frac { 1 + \epsilon } { 2 } \right) \left( H _ { 1 } + H _ { 2 } + H _ { 3 } \right) + H \right) } \end{array}$ is log canonical because $f$ is a log resolution of singularities (see Proposition 7.7).

Proposition 8.36. Given $P$ of type $( d )$ , then the pair $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ is a stable pair.

Proof.

$$
\begin{array} { r l } & { X _ { P } ^ { \bullet } = ( \mathbb { P } ^ { 1 } ) ^ { 3 } \ni \left( \left[ X _ { 0 } : X _ { 1 } \right] , \left[ Y _ { 0 } : Y _ { 1 } \right] , \left[ Z _ { 0 } : Z _ { 1 } \right] \right) , } \\ & { D _ { P } ^ { \bullet } = \emptyset \mathrm { ~ ( t h e r e ~ i s ~ n o ~ c o n d u c t o r ~ d i v i s o r ~ i n ~ t h i . } } \\ & { \Delta _ { P } ^ { \bullet } = V ( X _ { 0 } X _ { 1 } Y _ { 0 } Y _ { 1 } Z _ { 0 } Z _ { 1 } ) , } \\ & { B _ { P } ^ { \bullet } = V \left( \displaystyle \sum _ { i , j , k = 0 , 1 } c _ { i j k } X _ { i } Y _ { j } Z _ { k } \right) , } \end{array}
$$

where any two distinct coefficients $c _ { i j k }$ and $c _ { i ^ { \prime } j ^ { \prime } k ^ { \prime } }$ cannot be simultaneously zero if $( i , j , k )$ and $( i ^ { \prime } , j ^ { \prime } , k ^ { \prime } )$ are vertices of the same edge of the cube (this is because inside $Q$ we cannot fit two corner cuts with apices lying on the same edge).

Let us first assume that $B _ { P } ^ { \bullet }$ is smooth (hence irreducible), which happens for a general choice of the coefficients $c _ { i j k }$ by Bertini’s Theorem (see [Har77, Chapter II, Theorem 8.18]).
Then the anticanonical class $- K _ { B _ { P } ^ { \bullet } } = - ( K _ { ( \mathbb { P } ^ { 1 } ) ^ { 3 } } + B _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } = ( 1 , 1 , 1 ) | _ { B _ { P } ^ { \bullet } }$ is ample and $K _ { B _ { P } ^ { \bullet } } ^ { 2 } = 6$ , implying that $B _ { P } ^ { \bullet } \cong \mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ (see [Bea96, Exercise V.21(1)]).
If all the $c _ { i j k }$ are nonzero, then the restriction $\Delta _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ can be as in Proposition 8.14 (general case), or some of these lines can break into the union of two incident $( - 1 )$ -curves.
If some coefficients $c _ { i j k }$ are zero, then the lines configuration $\Delta _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ acquires triple intersection points.
In any case, the pair $\left( B _ { P } ^ { \bullet } , \left( { \textstyle { \frac { 1 + \epsilon } { 2 } } } \right) \Delta _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } \right)$ is log canonical (here we use Lemma 8.32 in case of triple intersection points).

Now assume that $B _ { P } ^ { \bullet }$ is irreducible but singular.
Let $p \in B _ { P } ^ { \bullet }$ be a singular point.
We prove that $p$ is a singularity of type $A _ { 1 }$ and the only singular point of $B _ { P } ^ { \bullet }$ .
We can assume that $p$ is in the form $( [ 1 : a ] , [ 1 : b ] , [ 1 : c ] )$ .
Consider the invertible change of coordinates $X _ { 0 } ^ { \prime } \ = \ X _ { 0 }$ , $X _ { 1 } ^ { \prime } = X _ { 1 } - a X _ { 0 }$ and so on.
This automorphism sends $B _ { P } ^ { \bullet }$ to an isomorphic surface $B _ { P } ^ { \prime }$ which is singular at $p ^ { \prime } = ( [ 1 : 0 ] , [ 1 : 0 ] , [ 1 : 0 ] )$ .
If we set $\begin{array} { r } { x ^ { \prime } = \frac { X _ { 1 } ^ { \prime } } { X _ { 0 } ^ { \prime } } , y ^ { \prime } = \frac { Y _ { 1 } ^ { \prime } } { Y _ { 0 } ^ { \prime } } , z ^ { \prime } = \frac { Z _ { 1 } ^ { \prime } } { Z _ { 0 } ^ { \prime } } } \end{array}$ , then the equation of $B _ { P } ^ { \prime }$

in this affine patch is in the form

$$
c _ { 0 } x ^ { \prime } y ^ { \prime } + c _ { 1 } x ^ { \prime } z ^ { \prime } + c _ { 2 } y ^ { \prime } z ^ { \prime } + c _ { 3 } x ^ { \prime } y ^ { \prime } z ^ { \prime } = 0 .
$$

The coefficients $c _ { 0 } , c _ { 1 } , c _ { 2 }$ are nonzero because $B _ { P } ^ { \prime }$ is irreducible.
Therefore it is clear that the singularity is of type $A _ { 1 }$ .
Now we show that $p ^ { \prime }$ is the only singularity of $B _ { P } ^ { \prime }$ , whose equation is given by

$$
c _ { 0 } X _ { 1 } Y _ { 1 } Z _ { 0 } + c _ { 1 } X _ { 1 } Y _ { 0 } Z _ { 1 } + c _ { 2 } X _ { 0 } Y _ { 1 } Z _ { 1 } + c _ { 3 } X _ { 1 } Y _ { 1 } Z _ { 1 } = 0 ,
$$

where we intentionally dropped the “prime” signs for simplicity of notation.
It is enough to check the affine patches $X _ { 0 } Y _ { 0 } Z _ { 0 } \neq 0 , X _ { 0 } Y _ { 0 } Z _ { 1 } \neq 0 , X _ { 0 } Y _ { 1 } Z _ { 1 } \neq 0 , X _ { 1 } Y _ { 1 } Z _ { 1 } \neq 0$ because of the symmetries of our equation.

• In $X _ { 0 } Y _ { 0 } Z _ { 0 } \ne 0$ we have

$$
\left\{ { \begin{array} { l } { c _ { 0 } x y + c _ { 1 } x z + c _ { 2 } y z + c _ { 3 } x y z = 0 , } \\ { c _ { 0 } y + c _ { 1 } z + c _ { 3 } y z = 0 , } \\ { c _ { 0 } x + c _ { 2 } z + c _ { 3 } x z = 0 , } \\ { c _ { 1 } x + c _ { 2 } y + c _ { 3 } x y = 0 . } \end{array} } \right.
$$

Let us show that this system has no solution other than $( 0 , 0 , 0 )$ .
Observe that $x = 0 , y = 0$ , or $z = 0$ implies that $x = y = z = 0$ .
Therefore, assume $x , y , z$ nonzero.
But if we multiply the last equation of the system by $z$ , then the first equation implies that $c _ { 0 } x y = 0$ , which is a contradiction.

• In $X _ { 0 } Y _ { 0 } Z _ { 1 } \neq 0$ we have to study the solutions of

$$
\left\{ \begin{array} { l l } { c _ { 0 } x y z + c _ { 1 } x + c _ { 2 } y + c _ { 3 } x y = 0 , } \\ { c _ { 0 } y z + c _ { 1 } + c _ { 3 } y = 0 , } \\ { c _ { 0 } x z + c _ { 2 } + c _ { 3 } x = 0 , } \\ { c _ { 0 } x y = 0 . } \end{array} \right.
$$

But this system has no solutions because $x = 0$ or $y = 0$ implies $c _ { 2 } = 0$ or $c _ { 1 } = 0$ respectively.

• In $X _ { 0 } Y _ { 1 } Z _ { 1 } \neq 0$ consider

$$
\left\{ \begin{array} { l l } { c _ { 0 } x z + c _ { 1 } x y + c _ { 2 } + c _ { 3 } x = 0 , } \\ { c _ { 0 } z + c _ { 1 } y + c _ { 3 } = 0 , } \\ { c _ { 1 } x = 0 , } \\ { c _ { 0 } x = 0 , } \end{array} \right.
$$

which has no solutions because $x = 0$ implies $c _ { 2 } = 0$ .

• In the affine patch $X _ { 1 } Y _ { 1 } Z _ { 1 } \neq 0$ , we obviously have no singular points because the dehomogeneization of equation (8.2) is linear.

It is easy to see that the singular point $p$ can lie on at most one irreducible component of $\Delta _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ (in checking this, it is fundamental that if two distinct coefficients $c _ { i j k } , c _ { i ^ { \prime } j ^ { \prime } k ^ { \prime } }$ are both zero, then $( i , j , k )$ and $( i ^ { \prime } , j ^ { \prime } , k ^ { \prime } )$ are not vertices of the same edge of the cube).
To prove that $\left( B _ { P } ^ { \bullet } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \Delta _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } \right)$ is log canonical, we show that $\left( X _ { P } ^ { \bullet } , ( { \textstyle { \frac { 1 + \epsilon } { 2 } } } ) \Delta _ { P } ^ { \bullet } + B _ { P } ^ { \bullet } \right)$ is log canonical and then we use inversion of adjunction (see [Kaw07]).
This is done in two steps.

• $\left( X _ { P } ^ { \bullet } , ( { \textstyle { \frac { 1 + \epsilon } { 2 } } } ) \Delta _ { P } ^ { \bullet } + B _ { P } ^ { \bullet } \right)$ is log canonical in an neighborhood of a quadruple intersection point $p$ of $\Delta _ { P } ^ { \bullet } + B _ { P } ^ { \bullet }$ .
Assume without loss of generality that $p = ( [ 1 : 0 ] , [ 1 : 0 ] , [ 1 : 0 ] )$ , an therefore $c _ { 0 0 0 } = 0$ .
In an affine neighborhood of $p$ the equation of $B _ { P } ^ { \bullet }$ becomes

$$
c _ { 1 0 0 } x + c _ { 0 1 0 } y + c _ { 0 0 1 } z + c _ { 1 1 0 } x y + c _ { 1 0 1 } x z + c _ { 0 1 1 } y z + c _ { 1 1 1 } x y z = 0 .
$$

where we must have $c _ { 1 0 0 } , c _ { 0 1 0 } , c _ { 0 0 1 }$ nonzero.
The affine equations for $\Delta _ { P } ^ { \bullet }$ at $p$ are $x = 0 , y =$ $0 , z = 0$ .
Therefore, locally at $p$ , the four irreducible components of $\Delta _ { P } ^ { \bullet } + B _ { P } ^ { \bullet }$ are equivalent to hyperplanes in general linear position.
Now we use Lemma 8.35;

• $\left( X _ { P } ^ { \bullet } , ( { \textstyle { \frac { 1 + \epsilon } { 2 } } } ) \Delta _ { P } ^ { \bullet } + B _ { P } ^ { \bullet } \right)$ is log canonical in the complement of the quadruple intersection points.
This is true in the complement of $\Delta _ { P } ^ { \bullet }$ because $B _ { P } ^ { \bullet }$ has at most an $A _ { 1 }$ singularity.
Let $H \subset \Delta _ { P } ^ { \bullet }$ be an irreducible component.
We show that $( X _ { P } ^ { \bullet } , \Delta _ { P } ^ { \bullet } + B _ { P } ^ { \bullet } )$ is log canonical in a neighborhood of $H$ away from the quadruple intersection points.
But this follows from inversion of adjunction because it is easy to observe that $( H , ( \Delta _ { P } ^ { \bullet } - H + B _ { P } ^ { \bullet } ) | _ { H } )$ is log canonical away from the quadruple intersection points (more precisely, $H \cong \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ , $( \Delta _ { P } ^ { \bullet } - H ) | _ { H }$ gives the toric boundary, and $B _ { P } ^ { \bullet } | _ { H }$ is a $( 1 , 1 )$ -curve with no components in common with the toric boundary).

We are left with the case $B _ { P } ^ { \bullet }$ reducible.
Decompositions into two irreducible components are given by

$$
( a X _ { 0 } Y _ { 0 } + b X _ { 0 } Y _ { 1 } + c X _ { 1 } Y _ { 0 } + d X _ { 1 } Y _ { 1 } ) ( e Z _ { 0 } + f Z _ { 1 } ) ,
$$

for any choice of nonzero coefficients such that $a d \neq b c$ .
It is easy to see that these two components are isomorphic to $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ and how they are glued together.
Decompositions into three irreducible components are given by

$$
( a X _ { 0 } + b X _ { 1 } ) ( c Y _ { 0 } + d Y _ { 1 } ) ( e Z _ { 0 } + f Z _ { 1 } ) ,
$$

for any choice of nonzero coefficients.
Up to $\mathrm { A u t } ( ( \mathbb { P } ^ { 1 } ) ^ { 3 } )$ there is only one choice of coefficients.
In both cases $\left( B _ { P } ^ { \bullet } , \left( { \textstyle { \frac { 1 + \epsilon } { 2 } } } \right) \Delta _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } \right)$ is semi-log canonical.

To conclude, $K _ { B _ { P } ^ { \bullet } } + \left( { \textstyle { \frac { 1 + \epsilon } { 2 } } } \right) \Delta _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ is ample because it is the pullback to $B _ { P } ^ { \bullet }$ of the following divisor:

$$
K _ { X _ { P } ^ { \bullet } } + B _ { P } ^ { \bullet } + \left( { \frac { 1 + \epsilon } { 2 } } \right) \Delta _ { P } ^ { \bullet } \sim \epsilon ( 1 , 1 , 1 ) ,
$$

which is ample (we used the adjunction formula to say that $K _ { B _ { P } ^ { \bullet } } \sim ( K _ { X _ { P } ^ { \bullet } } + B _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } )$ .

This completes the proof of Theorem 8.29.

Remark 8.37. The proof of Theorem 8.29 gives us an explicit description of the possible stable pairs $\begin{array} { r } { \left( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \frac { 1 + \epsilon } { 2 } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B ^ { \bullet } } \right) } \end{array}$ for all the stable toric pairs $( X , B )$ of type $\leq Q$ .
Here we want to summarize these possibilities.
In Figure 8.3, a triangle (resp.
trapezoid, parallelogram) means $B _ { P } ^ { \bullet } \cong \mathbb { P } ^ { 2 }$ (resp.
$\mathbb { F } ^ { 1 }$ ${ \ v O } ^ { 1 } , \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ ).
$D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ is represented by the thickened segments and $( \Delta _ { P } ^ { \bullet } -$ $D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } }$ by the colored segments.
First, let us assume that $\mathcal { P }$ has no corner cuts, so that $( X , B ) =$ $( X ^ { \bullet } , B ^ { \bullet } )$ .
In all the cases that follow, $\Delta _ { P } | _ { B _ { P } }$ is simple normal crossing.

(a) $B _ { P } \cong \mathbb { P } ^ { 2 }$ and $D _ { P } | _ { B _ { P } }$ (resp.
$( \Delta _ { P } - D _ { P } ) | _ { B _ { P } } )$ consists of two lines;

(b) $B _ { P } \cong \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ and $D _ { P } | _ { B _ { P } }$ consists of two incident rulings.
$( \Delta _ { P } - D _ { P } ) | _ { B _ { P } }$ is given by two incident rulings and a curve of divisor class $( 1 , 1 )$ which can possibly be reducible;

(c1) $B _ { P } \cong \mathbb { F } _ { 1 }$ and $D _ { P } | _ { B _ { P } }$ is a line disjoint from the exceptional divisor.
$( \Delta _ { P } - D _ { P } ) | _ { B _ { P } }$ is given by two fibers and two lines disjoint from the exceptional divisor.
Exactly one of these last two lines can possibly break into the union of the exceptional divisor and a fiber;

(c2) $B _ { P } \cong \mathbb { F } _ { 1 }$ and $D _ { P } | _ { B _ { P } }$ is the union of the exceptional divisor and a fiber.
$( \Delta _ { P } - D _ { P } ) | _ { B _ { P } }$ is given by two fibers and two lines disjoint from the exceptional divisor;

(c3) $B _ { P }$ is isomorphic to the union of $\mathbb { P } ^ { 2 }$ and $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ glued along a line in $\mathbb { P } ^ { 2 }$ and a ruling in $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ .
$D _ { P } | _ { B _ { P } }$ consists of a line in $\mathbb { P } ^ { 2 }$ and a ruling in $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ .
$( \Delta _ { P } - D _ { P } ) | _ { B _ { P } }$ is given by two lines on the $\mathbb { P } ^ { 2 }$ component and four rulings on $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ arranged as shown in Figure 8.3 $\left( c 3 \right)$ ;

(d1) $B _ { P } \cong \mathrm { B l _ { 3 } \mathbb { P } ^ { 2 } }$ and $D _ { P } | _ { B _ { P } } = \emptyset$ .
$\Delta _ { P } | _ { B _ { P } }$ is as in Proposition 8.8 (this is the general case), or some lines can possibly break into two intersecting $( - 1 )$ -curves;

$( d 1 ^ { \prime } )$ $B _ { P }$ is a singular del Pezzo surface of degree 6 with exactly one $A _ { 1 }$ singularity.
This singularity can lie on at most one irreducible component of $\Delta _ { P } | _ { B _ { P } }$ ;

( $d ^ { \prime }$ 2) $B _ { P }$ is isomorphic to the union of two copies of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ glued along a ruling and an irreducible curve of divisor class $( 1 , 1 )$ .
$\Delta _ { P } | _ { B _ { P } }$ is given by four rulings on one component and six rulings on the other.
These are arranged as shown in Figure 8.3 ( $d 2$ );

( $d .$ 3) $B _ { P }$ is isomorphic to the union of three copies of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ glued along rulings as shown in Figure 8.3 ( $d _ { \mathrm { e } } ^ { \ast }$ 3).
$\Delta _ { P } | _ { B _ { P } }$ consists of four rulings on each component as shown in Figure 8.3 $( d 3 )$ .

Now assume that $_ { \mathcal { P } }$ has a corner cut and let $P \in \mathcal { P } ^ { \bullet }$ .
In this case, the possibilities for the pair $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ are as above, with the difference that now $( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } }$ is allowed to have triple intersection points.

# 8.4 KSBA compactification for $D _ { 1 , 6 }$ -polarized Enriques surfaces

# 8.4.1 Map to the KSBA compactification

In Theorem 8.40 we describe a surjective (algebraic) morphism $\overline { { M } } _ { Q } ^ { \nu }  \overline { { M } } _ { D _ { 1 , 6 } }$ (see Notation 8.16 for the meaning of $X ^ { \nu }$ for a given scheme $X$ ) which gives a geometric interpretation of the k-points of $\overline { { M } } _ { D _ { 1 , 6 } }$ (the global geography of $\overline { { M } } _ { D _ { 1 , 6 } }$ is described in Section 8.4.2). We need some preliminaries from [GG14].

![](images/2980ce6340fc6c02ca34023637908a8b64165446b7baacedb2241772afe911ac.jpg)  
Figure 8.3: The pictures represent $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ for $P \in \mathcal { P } ^ { \bullet }$ (see Remark 8.37). The restriction $( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } }$ is in blue, green, and red, $D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } }$ is thickened.
Two irreducible components are glued together along the yellow curves

Notation 8.38. Consider a map $g \colon { \mathrm { S p e c } } ( K ) \to Y$ , where $K$ is the field of fractions of a DVR $( A , { \mathfrak { m } } )$ with residue field our fixed base field $\Bbbk$ .
Let $Y$ be a proper scheme over a noetherian scheme $S$ .
By the valuative criterion of properness, $g$ extends in a unique way to a map $\overline { { g } }$ : S $\operatorname { \mathrm { ) e c } } ( A ) \to Y$ .
We denote by $\operatorname { l i m } g$ the point $\overline { { g } } ( \mathfrak { m } )$ .

Theorem 8.39 ([GG14, Theorem 7.3]).
Suppose $X _ { 1 }$ and $X _ { 2 }$ are proper schemes over a noetherian scheme $S$ with $X _ { 1 }$ normal.
Let $U \subseteq X _ { 1 }$ be an open dense subset and $f \colon U  X _ { 2 }$ an $S$ -morphism.
Then $f$ extends to an $S$ -morphism ${ \overline { { f } } } \colon X _ { 1 } \to X _ { 2 }$ if and only if for any point $x \in X _ { 1 }$ , any $D V R$ $( A , { \mathfrak { m } } )$ as in Notation 8.38, and any morphism $g \colon { \mathrm { S p e c } } ( K ) \to U$ such that $\operatorname* { l i m } g = x$ , the point $\operatorname* { l i m } ( f \circ g )$ of $X _ { 2 }$ only depends on $x$ , and not on the choice of $g$ .

Theorem 8.40. Let $Q$ be the unit cube.
Then there is a surjective (algebraic) morphism $\overline { { M } } _ { Q } ^ { \nu } $ ${ \overline { { M } } } _ { D _ { 1 , 6 } }$ which is given on k-points by

$$
( X , B ) \mapsto \left( B ^ { \bullet } , \left( { \frac { 1 + \epsilon } { 2 } } \right) \Delta ^ { \bullet } | _ { B ^ { \bullet } } \right) .
$$

Proof.
Set $X _ { 1 } = \overline { { M } } _ { Q } ^ { \nu } , X _ { 2 } = \overline { { M } } _ { D _ { 1 , 6 } } , U = \mathcal { U } _ { \mathrm { s m } }$ (which was constructed in Definition 8.20), and let $S = { \mathrm { S p e c } } ( \mathbb { k } )$ .
The claimed morphism $X _ { 1 }  X _ { 2 }$ is obtained by extending $f \colon \mathcal { U } _ { \mathrm { s m } } \to X _ { 2 }$ to the whole $X _ { 1 }$ by means of Theorem 8.39.

Let $( A , { \mathfrak { m } } )$ be any DVR and consider a map $g \colon { \mathrm { S p e c } } ( K ) \to { \mathcal { U } } _ { \mathrm { s m } }$ .
The point $\operatorname* { l i m } g \in X _ { 1 }$ corresponds to a stable toric pair $( X , B )$ of type $\leq Q$ .
Denote by $\Delta$ the toric boundary of $X$ .
If we prove that $\operatorname { l i m } ( f \circ g )$ corresponds to the stable pair $\left( B ^ { \bullet } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \Delta ^ { \bullet } | _ { B ^ { \bullet } } \right)$ , then we are done by Theorem 8.39, because this shows that $\operatorname { l i m } ( f \circ g )$ only depends on $\operatorname { l i m } g$ , and not from the way we approach it (see Remark 8.25).

Let $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } \times \mathcal { U } _ { \mathrm { s m } } , \mathfrak { S } _ { \mathrm { s m } } ) / \mathcal { U } _ { \mathrm { s m } }$ be as in Definition 8.20. Let $\big ( \big ( \mathbb { P } _ { K } ^ { 1 } \big ) ^ { 3 } , \mathfrak { B } ^ { \circ } \big )$ be the pullback of $( ( \mathbb { P } ^ { 1 } ) ^ { 3 } \times$ $\mathcal { U } _ { \mathrm { s m } } , \mathfrak { S } _ { \mathrm { s m } }$ ) under the map $g$ and denote by $( { \mathfrak { X } } , { \mathfrak { B } } )$ its completion over Spec $( A )$ , or a finite ramified base change of it, as a family of stable toric pairs (so that the central fiber is $( X , B )$ ).
Consider $( { \mathfrak { X } } ^ { \bullet } , { \mathfrak { P } } ^ { \bullet } )$ and, if $D$ denotes the toric boundary of $( \mathbb { P } ^ { 1 } ) ^ { 3 }$ , let $\overline { { D } } _ { K }$ be the closure of $D _ { K } = D \times \mathrm { S p e c } ( K )$ in ${ \mathfrak { X } } ^ { \bullet }$ .
Then the central fiber of $\left( \mathfrak { B } ^ { \bullet } , \left( \frac { \mathbb { 1 } + \epsilon } { 2 } \right) \overline { { D } } _ { K } | _ { \mathfrak { B } ^ { \bullet } } \right)$ , which is $\left( B ^ { \bullet } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \Delta ^ { \bullet } | _ { B ^ { \bullet } } \right)$ by construction, is the stable pair corresponding to $\operatorname* { l i m } ( f \circ g )$ .
□

Theorem 8.41. Let $\overline { { M } } _ { Q } ^ { \nu } \to \overline { { M } } _ { D _ { 1 , 6 } }$ be the morphism in Theorem 8.40. Then the induced morphism $\overline { { M } } _ { Q } ^ { \nu } / \mathrm { S y m } ( Q ) \to \overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ is an isomorphism.

Proof.
The group $\operatorname { S y m } ( Q )$ acts on $\overline { { M } } _ { Q } ^ { \nu }$ because $\overline { { M } } _ { Q } ^ { \nu }$ is the projective toric variety associated to the secondary polytope of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ .
The modular interpretation of the action is the following: $\operatorname { S y m } ( Q )$ acts on the stable toric pair $( X , B )$ by changing the torus action on it.
In particular, the morphism $\overline { { { M } } } _ { Q } ^ { \nu }  \overline { { { M } } } _ { D _ { 1 , 6 } }$ is Sym $( Q )$ -equivariant.
Therefore, we have an induced morphism $\overline { { M } } _ { Q } ^ { \nu } / \mathrm { S y m } ( Q ) \to \overline { { M } } _ { D _ { 1 , 6 } }$ which lifts to the normalization of ${ \overline { { M } } } _ { D _ { 1 , 6 } }$ .

The fibers of the restriction of $\overline { { { M } } } _ { Q } ^ { \nu }  \overline { { { M } } } _ { D _ { 1 , 6 } }$ to $\mathcal { U } _ { \mathrm { s m } }$ are exactly $\operatorname { S y m } ( Q )$ -orbits (see Definition 8.20 and Observation 8.21), and hence the morphism $\overline { { M } } _ { Q } ^ { \nu } / \mathrm { S y m } ( Q ) \to \overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ is bijective on a dense open subset.
In what follows, we show that $\overline { { M } } _ { Q } ^ { \nu } \to \overline { { M } } _ { D _ { 1 , 6 } }$ is quasi-finite, which implies that $\overline { { M } } _ { Q } ^ { \nu } / \mathrm { S y m } ( Q ) \to \overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ is an isomorphism by the Zariski Main Theorem (see [Mum99, Chapter III, Section 9]).

![](images/80d5a8e8303f3d5c085539e45cd67aba0a2ad56f3d85dc0196e7ae93174a3ad6.jpg)  
Figure 8.4: Subpolytopes of $Q$ which can be subdivided further only once (see the proof of Theorem 8.41)

To prove that $\overline { { M } } _ { Q } ^ { \nu }  \overline { { M } } _ { D _ { 1 , 6 } }$ is quasi-finite, it is enough to check that no 1-dimensional boundary stratum of $\overline { { M } } _ { Q } ^ { \nu }$ is contracted by $\overline { { M } } _ { Q } ^ { \nu }  \overline { { M } } _ { D _ { 1 , 6 } }$ .
These strata correspond to the minimal elements of the poset of regular polyhedral subdivisions of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ which are not triangulations (all the polyhedral subdivisions of $( Q , Q \cap \mathbb { Z } )$ are regular, see the proof of Proposition 8.17). If $\mathcal { P }$ is one of these polyhedral subdivisions, then it has to contain a subpolytope of $Q$ with vertices in $Q \cap \mathbb { Z } ^ { 3 }$ which can be subdivided further only once.
An easy enumeration shows that $\mathcal { P }$ has to contain one of the polytopes listed in Figure 8.4. Denote by $P$ one of such polytopes, and let $( X , B )$ be any stable toric pair with $\mathcal { P }$ as corresponding polyhedral subdivision of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ .
Then, as $( X , B )$ varies among the stable toric pairs parametrized by the 1-dimensional boundary stratum corresponding to $_ { \mathcal { P } }$ , $( B ^ { \bullet } , ( { \textstyle \frac { 1 + \epsilon } { 2 } } ) \Delta ^ { \bullet } | _ { B ^ { \bullet } } )$ describes a 1-dimensional family of stable pairs (to see this, if $P ^ { \bullet } \in { \mathcal { P } } ^ { \bullet }$ is the polytope corresponding to $P \in \mathcal { P }$ , it is enough to consider the irreducible component of $( B ^ { \bullet } , ( { \textstyle \frac { 1 + \epsilon } { 2 } } ) \Delta ^ { \bullet } | _ { B ^ { \bullet } } )$ corresponding to $P ^ { \bullet }$ ).
In conclusion, the 1-dimensional boundary stratum corresponding to $\mathcal { P }$ is not contracted.
□

# 8.4.2 Description of the boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$

Definition 8.42. The boundary of the moduli space $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ is the closed subset whose k-points parametrize stable pairs $( B , D )$ with $B$ reducible.
Let $( B , D )$ be a stable pair parametrized by the boundary, and consider the locus of points in $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ parametrizing stable pairs $( B ^ { \prime } , D ^ { \prime } )$ such that $B \cong B ^ { \prime }$ .
We call the closure of such locus a stratum.

Theorem 8.43. The boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ is stratified as shown in Figure 8.6. The strata are organized from bottom to top in increasing order of dimension.
Going from left to right in Figure 8.6, call the 0-dimensional strata even, odd of type 1, and odd of type 2 (this terminology is borrowed from [Oud10]).
Then the strata containing the even 0-dimensional stratum correspond bijectively to the polyhedral subdivisions of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ without corner cuts up to symmetries of $Q$ , where $Q$ is the unit cube.

Proof.
By Theorem 8.41 any stable pair parametrized by $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ is in the form $\left( B ^ { \bullet } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \Delta ^ { \bullet } | _ { B ^ { \bullet } } \right)$ for some stable toric pair $( X , B )$ parametrized by $\overline { { M } } _ { Q } ^ { \nu }$ .
In Remark 8.37 we listed all the possibilities for the pairs $\Big ( B _ { P } ^ { \bullet } , D _ { P } ^ { \bullet } | _ { B _ { P } ^ { \bullet } } + \left( \textstyle { \frac { 1 + \epsilon } { 2 } } \right) ( \Delta _ { P } ^ { \bullet } - D _ { P } ^ { \bullet } ) | _ { B _ { P } ^ { \bullet } } \Big )$ , which can be glued together for $P \in \mathcal { P } ^ { \bullet }$ to recover $\left( B ^ { \bullet } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \Delta ^ { \bullet } | _ { B ^ { \bullet } } \right)$ , where $\mathcal { P } ^ { \bullet }$ is a polyhedral subdivisions of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ without corner cuts.
These subdivisions are shown in Figure 8.5 up to symmetries of $Q$ .
The end result is shown in Figure 8.6, where for each stratum we picture the stable pair parametrized by a general point in it.
The three colors (blue, green, and red) used to draw the divisor have the following meaning: lines sharing the same color come from the same pair of lines on the original $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ .
We want to remark that, even though we use three different colors, we do not distinguish the three pairs because we took the quotient by $S _ { 3 }$ in our definition of ${ \overline { { M } } } _ { D _ { 1 , 6 } }$ .
The yellow color is used to indicate lines along which two irreducible components are glued together.
The claimed combinatorial interpretation of the strata containing the even 0-dimensional stratum follows immediately after comparing Figure 8.5 and Figure 8.6. □

# 8.4.3 Degenerations of Enriques surfaces

After describing all the degenerations of $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ together with the three undistinguished pairs of undistinguished weighted lines parametrized by $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ , we want to discuss what are the overlying $\mathbb { Z } _ { 2 } ^ { 2 }$ -covers which correspond to actual degenerations of Enriques surfaces.
We describe such $\mathbb { Z } _ { 2 } ^ { 2 }$ - covers for the stable pairs parametrized by a general point in each boundary stratum of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ .
In what follows, we refer to the $\mathbb { Z } _ { 2 } ^ { 2 }$ -covers with the appropriate building data that comes from the subdivision into three pairs of lines (which we kept track of).
In some cases, the double locus is part of the branch locus.

![](images/af7997b50a47047c819e63cd3903f6fce5304ea01d8771cfda9e7939f2e4d992.jpg)  
Figure 8.5: Polyhedral subdivisions of $( Q , Q \cap \mathbb { Z } ^ { 3 } )$ without corner cuts up to symmetry and ordered by refinement

![](images/842ec86f84862bd7fd40522b4c4572ae39f911b4f4dc96731799eed73a94dc98.jpg)  
Figure 8.6: Stratification of the boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$

(a) Consider the stable pair parametrized by the odd 0-dimensional stratum of type 2. Then its $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover is isomorphic to the quotient of

$$
V ( ( X _ { 0 } ^ { 2 } - X _ { 1 } ^ { 2 } ) ( Y _ { 0 } ^ { 2 } - Y _ { 1 } ^ { 2 } ) ( Z _ { 0 } ^ { 2 } - Z _ { 1 } ^ { 2 } ) ) \subset ( \mathbb { P } ^ { 1 } ) ^ { 3 } ,
$$

by the involution $\iota$ (see Remark 8.15 and the proof of Proposition 8.36). This quotient consists of three copies of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ glued along rulings in such a way that its dual complex gives a triangulation of the real projective plane.

(b) The stable pair parametrized by a general point in the maximal 1-dimensional stratum of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ has $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover isomorphic to the quotient of

$$
V ( ( X _ { 0 } ^ { 2 } - X _ { 1 } ^ { 2 } ) ( Y _ { 0 } ^ { 2 } Z _ { 0 } ^ { 2 } + Y _ { 1 } ^ { 2 } Z _ { 0 } ^ { 2 } + Y _ { 0 } ^ { 2 } Z _ { 1 } ^ { 2 } + \lambda Y _ { 1 } ^ { 2 } Z _ { 1 } ^ { 2 } ) ) \subset ( \mathbb { P } ^ { 1 } ) ^ { 3 } , \lambda \neq 0 , 1 ,
$$

by $\iota$ (again, see Remark 8.15 and the proof of Proposition 8.36). If we define

$$
E = V ( Y _ { 0 } ^ { 2 } Z _ { 0 } ^ { 2 } + Y _ { 1 } ^ { 2 } Z _ { 0 } ^ { 2 } + Y _ { 0 } ^ { 2 } Z _ { 1 } ^ { 2 } + \lambda Y _ { 1 } ^ { 2 } Z _ { 1 } ^ { 2 } ) \subset \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 } ,
$$

then the irreducible components of this $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover are a copy of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ , and an elliptic fibration $F ^ { \prime }$ over $\mathbb { P } ^ { 1 }$ with fibers isomorphic to $E$ and two double fibers.
These surfaces are glued along $E \subset \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ and a reduced fiber of $F ^ { \prime }$ .

(c) Consider the stable pair parametrized by a general point in the irreducible boundary divisor containing two 0-dimensional strata.
Let us describe the $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover $X$ of one of the two irreducible components, which are both isomorphic to $\mathbb { F } _ { 1 }$ .
Let $h$ be a section of selfintersection $1$ and $f$ a fiber.
Then the building data for the cover $\pi \colon X  \mathbb { F } _ { 1 }$ is given by $D _ { a } \sim 2 f + h , D _ { b } \sim D _ { c } \sim h$ , implying that

$$
K _ { X } \sim _ { \mathbb { Q } } \pi ^ { * } \left( K _ { \mathbb { F } _ { 1 } } + \frac { 1 } { 2 } ( D _ { a } + D _ { b } + D _ { c } ) \right) \sim _ { \mathbb { Q } } - \frac { 1 } { 2 } \pi ^ { * } ( h ) .
$$

This shows that $- K _ { X }$ is big, nef, and $K _ { X } ^ { 2 } = 1$ .
Therefore, $X$ is a weak del Pezzo surface of degree 1. The total degeneration is given by two of such weak del Pezzo surfaces glued along a genus 1 curve.

(d) Let $X$ be the $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of the $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ in Figure 8.3 ( $b$ ).
Denote by $\ell _ { 1 }$ and $\ell _ { 2 }$ two incident rulings.
Then the building data for the cover $\pi \colon X \to \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ is given by $D _ { a } \sim D _ { b } \sim D _ { c } \sim \ell _ { 1 } + \ell _ { 2 }$ .
From this we obtain that $\begin{array} { r } { K _ { X } \sim _ { \mathbb { Q } } - \frac { 1 } { 2 } \pi ^ { * } ( \ell _ { 1 } + \ell _ { 2 } ) } \end{array}$ .
It follows that $- K _ { X }$ is ample and $K _ { X } ^ { 2 } = 2$ .
Hence, $X$ is a del Pezzo surface of degree 2.

(e) Let us describe the $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of the $\mathbb { P } ^ { 2 }$ in Figure 8.3 ( $a$ ).
If $\ell$ denotes a line in $\mathbb { P } ^ { 2 }$ , then the building data for the cover $\pi \colon X \to \mathbb { P } ^ { 2 }$ is $D _ { a } \sim D _ { b } \sim 2 \ell , D _ { c } \sim 0$ .
Therefore, $K _ { X } \sim _ { \mathbb { Q } } - \pi ^ { * } ( \ell )$ , implying that $- K \boldsymbol { X }$ is ample and $K _ { X } ^ { 2 } = 4$ .
Hence, $X$ is a del Pezzo surface of degree 4.

(f) Let us describe the $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of the $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ -component in Figure 8.3 ( $c { \overset { \cdot } { \mathrm { c } } }$ ).
If $\ell _ { 1 }$ and $\ell _ { 2 }$ denote two incident rulings, then the building data for the cover $\pi \colon X \to \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ is given by $D _ { a } \sim 2 \ell _ { 1 } + \ell _ { 2 } , D _ { b } \sim D _ { c } \sim \ell _ { 2 }$ .
Therefore, $K _ { X } \sim _ { \mathbb { Q } } - \frac { 1 } { 2 } \pi ^ { * } ( 2 \ell _ { 1 } + \ell _ { 2 } )$ , $- K _ { X }$ is ample, $K _ { X } ^ { 2 } = 4$ , and $X$ is a del Pezzo surface of degree 4.

Remark 8.44. A Coble surface is a smooth rational projective surface $X$ with $| - K _ { X } | = \emptyset$ and $\vert - 2 K _ { X } \vert \neq \varnothing$ (see [DZ01]).
These are related to our degenerations of Enriques surfaces as follows.
Let $S$ be the appropriate $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ branched along $\textstyle \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } + \ell _ { i } ^ { \prime } )$ (see Notation 8.7), and assume that this lines configuration has exactly one triple intersection point.
Then $S$ has a quotient singularity of type $\textstyle { \frac { ( 1 , 1 ) } { 4 } }$ over this triple intersection point, and the minimal resolution $\bar { S }$ of $S$ is a Coble surface.
This follows from Castelnuovo rationality criterion, and from $K _ { \widetilde { S } } = - \frac { 1 } { 2 } E$ , where $E$ is the exceptional divisor over the quotient singularity.
The Zariski closure in $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ of the locus of points parametrizing these surfaces $S$ defines a divisor.

# 8.5 Relation with the Baily-Borel compactification

In what follows we construct a morphism from the KSBA compactification $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ to the BailyBorel compactification of $\mathcal { D } / \Gamma$ , where $\mathcal { D }$ is the period domain parametrizing $D _ { 1 , 6 }$ -polarized Enriques surfaces (details in Section 8.5.2). Section 8.5.1 contains a technical result which is fundamental to construct such morphism.
In Section 8.5.3 we show that the combinatorics of the boundary strata of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ has an interpretation in terms of Vinberg diagrams.
Let $\Bbbk = \mathbb { C }$ be our base field.

# 8.5.1 Generalized type of degenerations of stable K3 surface pairs

Remark 8.45. In Section 8.5 our focus moves from Enriques surfaces to K3 surfaces.
The reason for this is that in Theorem 8.52 we compute limits of one-parameter families of $D _ { 1 , 6 }$ -polarized Enriques surfaces in the Baily-Borel compactification of $\mathcal { D } / \Gamma$ .
This is done by using the corresponding K3 covers.

Let $\Delta$ be the unit disk $\{ t \in \mathbb { C } \mid | t | < 1 \}$ and let $\Delta ^ { * } = \Delta \setminus \{ 0 \}$ .
We are interested in proper flat families ${ \mathfrak { X } } ^ { * } \to \Delta ^ { * }$ with ${ \mathfrak { X } } ^ { * }$ smooth and where $\mathfrak { X } _ { t } ^ { * }$ is a smooth K3 surface for all $t \in \Delta ^ { * }$ .
Equip the family ${ \mathfrak { X } } ^ { * }$ with an effective relative Cartier divisor $\mathcal { H } ^ { \ast }$ such that $( { \mathfrak { X } } ^ { * } , { \mathcal { H } } ^ { * } ) \to \Delta ^ { * }$ is a family of stable pairs.
Let $\boldsymbol { \mathscr { X } }$ be a semistable degeneration with $K _ { \mathfrak { X } } \sim 0$ (or simply Kulikov degeneration for short) completing ${ \mathfrak { X } } ^ { * }$ over $\Delta$ (see [Kul77, PP81]).
Recall that the central fiber $\boldsymbol { \mathfrak { X } } _ { 0 }$ can be of type I, II or III (see [Kul77, Theorem II]).
In type II, denote by $j ( \mathfrak { X } _ { 0 } )$ the $j$ -invariant of one of the mutually isomorphic genus 1 double curves on $\mathfrak { X } _ { 0 }$ .
Then define $\mathcal { H }$ to be the closure of $\mathcal { H } ^ { \ast }$ inside $\boldsymbol { \mathcal { X } }$ ( $\mathcal { H }$ is flat over $\Delta$ ).
We can define a second completion of $( { \mathfrak { X } } ^ { * } , { \mathcal { H } } ^ { * } )$ over $\Delta$ , which we denote by $( \mathfrak { X ^ { \prime } } , \mathcal { H } ^ { \prime } )$ , such that $( \mathfrak { X } _ { 0 } ^ { \prime } , \epsilon \mathcal { H } _ { 0 } ^ { \prime } )$ is a stable pair for all $0 < \epsilon \ll 1$ .

Definition 8.46. With the notation introduced above, define the dual graph of $\mathfrak { X } _ { 0 } ^ { \prime }$ as follows.
Draw a vertex $v _ { i }$ for each irreducible component $V _ { i }$ of $\mathfrak { X } _ { 0 } ^ { \prime }$ .
Then, given any two distinct irreducible components $V _ { i }$ and $V _ { j }$ , draw one edge between $v _ { i }$ and $v _ { j }$ for each irreducible curve in $V _ { i } \cap V _ { j }$ .
If an irreducible component $V _ { i }$ self-intersects along a curve $C$ , then draw one loop on $v _ { i }$ for each irreducible component of $C$ .
Denote by $G ( \mathfrak { X } _ { 0 } ^ { \prime } )$ the dual graph of $\mathfrak { X } _ { 0 } ^ { \prime }$ .

Definition 8.47. Let $\mathfrak { X } ^ { \prime }$ as defined above.
We say that $\mathfrak { X } _ { 0 } ^ { \prime }$ has generalized type I, $I I$ , or $I I I$ if the following hold:

• Type I: $G ( \mathfrak { X } _ { 0 } ^ { \prime } )$ consists of one vertex and $\mathfrak { X } _ { 0 } ^ { \prime }$ has at worst Du Val singularities;  
• Type II: $G ( \mathfrak { X } _ { 0 } ^ { \prime } )$ is a chain and $\mathfrak { X } _ { 0 } ^ { \prime }$ has at worst elliptic singularities.
If there are at least two vertices and the double curves are mutually isomorphic genus 1 curves, then denote by $j ( \mathfrak { X } _ { 0 } ^ { \prime } )$ the $j$ -invariant of one of these;  
• Type III: otherwise.

The proof of the following theorem, which builds upon the proof of [Laz16, Theorem 2.9], was communicated to me by Valery Alexeev.

Theorem 8.48. With the notation introduced above, $\mathfrak { X } _ { 0 }$ and $\mathfrak { X } _ { 0 } ^ { \prime }$ have the same type.
In addition, if $\mathfrak { X } _ { 0 } , \mathfrak { X } _ { 0 } ^ { \prime }$ have type II and $j ( \mathfrak { X } _ { 0 } ^ { \prime } )$ can be defined, then $j ( \mathfrak { X } _ { 0 } ) = j ( \mathfrak { X } _ { 0 } ^ { \prime } )$ .

Proof.
The proof of [Laz16, Theorem 2.9] describes a procedure to construct the unique stable model $( \mathfrak { X } ^ { \prime } , \epsilon \mathcal { H } ^ { \prime } )$ by modifying $( { \mathfrak { X } } , { \mathcal { H } } )$ .
This procedure consists mainly of the following two steps:

• Step 1: Replace $\boldsymbol { \mathscr { X } }$ with another Kulikov degeneration such that $\mathcal { H }$ is nef and it does not contain double curves or triple points (this may involve, among other things, base changes); • Step 2: For $n \geq 4$ , the line bundle $\mathcal { O } _ { \mathfrak { X } } ( n \mathcal { H } )$ induces a birational morphism $( { \mathfrak { X } } , { \mathcal { H } } ) \to ( { \mathfrak { X } } ^ { \prime } , { \mathcal { H } } ^ { \prime } )$ where ${ \mathfrak { X } } ^ { \prime } = \operatorname { P r o j } _ { \Delta } \left( \bigoplus _ { n \geq 0 } { \mathcal { O } } _ { \mathfrak { X } } ( n { \mathcal { H } } ) \right)$ (see [SB83, Theorem 2, part (i)]).
This birational morphism consists of the contraction of some components or curves in the central fiber $\boldsymbol { \mathfrak { X } } _ { 0 }$ .

In step 1, the new Kulikov model is obtained from the one we started by applying elementary modifications of type 0, I, II (see [FM83, pages 12–15] for their definitions), base changes, and blow ups of $\mathfrak { X } _ { 0 }$ along double curves or triple points.
The elementary modifications and the blow ups obviously do not change the type of the central fiber.
A description of how the central fiber is modified after a base change can be found in [Fri83], and also in this case the type does not change.
In step 2, it follows from our definition of generalized type that $\mathfrak { X } _ { 0 } ^ { \prime }$ has the same type as $\mathfrak { X } _ { 0 }$ .

This shows that if $\mathfrak { X } _ { 0 }$ has type I, II, or III, then $\mathfrak { X } _ { 0 } ^ { \prime }$ has type I, II, or III respectively.
The converse follows from this and from the uniqueness of the stable model.
The claim about the $j$ -invariants also follows from our discussion.
□

# 8.5.2 Map to the Baily-Borel compactification

The period domain $\mathcal { D } _ { L } = \mathcal { D }$ parametrizing $D _ { 1 , 6 }$ -polarized Enriques surfaces (where $L$ is the lattice $\mathbb { Z } ^ { 2 } ( 2 ) \oplus \mathbb { Z } ^ { 4 } ( - 1 )$ , see [Oud10, Section 3.4.2] for the details) and its Baily-Borel compactification $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$ ( $\Gamma$ denotes the isometry group of $L$ ) are studied in [Oud10].
Oudompheng shows that the boundary of $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$ consists of two rational 1-cusps and three 0-cusps (see [Oud10, Proposition 7.7]).
The 1-cusps are labeled even and odd.
The 0-cusps are labeled even, odd of type 1, and odd of type 2. These are arranged as shown in Figure 8.7. In what follows we construct a birational morphism $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }  \overline { { \mathcal { D } / \Gamma } } ^ { B B }$ which highlights a correspondence between the boundary strata of the two compactifications.

![](images/26be2dd74f8944ef103fc4d0d123d416500990f9fec2c8197d68b5f3362216b6.jpg)  
Figure 8.7: Boundary of the Baily-Borel compactification $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$

Observation 8.49. The two rational 1-cusps of the Baily-Borel compactification D/ΓBB a re degree 3 covers of the modular curve $X ( 1 ) \cong \mathbb { P } ^ { 1 }$ (see [Oud10, Section 7.3]).

Lemma 8.50. There exists a compactification $\overline { { \mathcal { D } / \Gamma } } ^ { \prime }$ of $\mathcal { D } / \Gamma$ obtained from $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$ by gluing the three 0-cusps together and by gluing the two 1-cusps to a rational curve with one node whose smooth points correspond to isomorphism classes of elliptic curves.
Moreover, D/ΓBB i s the normalization of $\overline { { \mathcal { D } / \Gamma } } ^ { \prime }$ .

Proof.
The main technique we use for the proof is [Fer03, Theorem 5.4].
Let us briefly recall it.
Let $X ^ { \prime }$ be a scheme, $Y ^ { \prime }$ a closed subscheme of $X ^ { \prime }$ , and $Y ^ { \prime }  Y$ a finite morphism.
Consider the ringed space $X = X ^ { \prime } \operatorname { I I } _ { Y ^ { \prime } } Y$ and the cocartesian square

$$
\begin{array} { c c } { { Y ^ { \prime } \longrightarrow Y } } & { { } } \\ { { \Big \downarrow } } & { { \Big \downarrow } } \\ { { X ^ { \prime } \longrightarrow X . } } & { { \longrightarrow X . } } \end{array}
$$

Let us assume that any finite sets of points in $X ^ { \prime }$ (resp.
$Y$ ) are contained in an open affine subset of $X ^ { \prime }$ (resp.
$Y$ ).
Then $X$ is a scheme verifying the same property on finite sets of points, the above diagram is cartesian, $Y  X$ is a closed immersion, the morphism $X ^ { \prime }  X$ is finite, and it induces an isomorphism $X ^ { \prime } \setminus Y ^ { \prime } \cong X \setminus Y$ .

Back to our case, denote by Ceven, Codd the two 1-cusps of D/ΓBB.
We want to first consider the finite morphism $C _ { \mathrm { e v e n } }  X ( 1 )$ to build the projective scheme $X _ { 1 } = \overline { { { D / \Gamma } } } ^ { B B } \operatorname { I I } _ { C _ { \mathrm { e v e n } } } X ( 1 )$ (the hypothesis on finite sets of points is satisfied because $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$ and $X ( 1 )$ are projective).
Repeat the gluing on $X _ { 1 }$ by considering now $C _ { \mathrm { o d d } } \to X ( 1 )$ to obtain $X _ { 2 }$ .
Now glue together the two copies of $X ( 1 )$ on $X _ { 2 }$ to obtain $X _ { 3 }$ .
Finally, identify the images in $X _ { 3 }$ of the three 0-cusps to obtain the claimed compactification $\overline { { \mathcal { D } / \Gamma } } ^ { \prime }$ .
The isomorphism $\overline { { \mathcal { D } / \Gamma } } ^ { B B } \cong ( \overline { { \mathcal { D } / \Gamma } } ^ { \prime } ) ^ { \nu }$ follows from the Zariski Main Theorem because D/ΓBB is normal and the morphism $\overline { { \mathcal { D } / \Gamma } } ^ { B B } \to \overline { { \mathcal { D } / \Gamma } } ^ { \prime }$ is finite and birational.

Definition 8.51. Recall the family $\mathfrak { S } _ { \mathrm { s m } } / \mathcal { U } _ { \mathrm { s m } }$ in Definition 8.20. We denote by ${ \mathfrak { S } } _ { \mathrm { s m } } ^ { \mathrm { K 3 } }$ the appropriate $\mathbb { Z } _ { 2 } ^ { 3 }$ -cover of ${ \mathfrak { S } } _ { \mathrm { s m } }$ branched along $( \Delta \times \mathcal { U } _ { \mathrm { s m } } ) | _ { \mathfrak { S } _ { \mathrm { s m } } }$ , which is a family of K3 surfaces.
Observe that ${ \mathfrak { S } } _ { \mathrm { s m } } ^ { \mathrm { K 3 } }$ , like ${ \mathfrak { S } } _ { \mathrm { s m } }$ , is embedded in $( { \mathbb { P } } ^ { 1 } ) ^ { 3 } \times \mathcal { U } _ { \mathrm { s m } }$ .

Theorem 8.52. There exists a birational morphism MνD1,6 → D/ΓBB which maps the boundary of M νD1,6 to the boundary of D/ΓBB.

Proof.
The GIT interpretation of D/ΓBB i n [Oud10] as quotient of the Grassmannian ${ \mathrm { G r } } ( 3 , 6 )$ gives us a birational morphism D/ΓBB 9 $\overline { { { \mathcal { D } / \Gamma } } } ^ { B B } \ _ { -- \to } \ \overline { { { M } } } _ { D _ { 1 , 6 } } ^ { \nu }$ (this morphism is defined at points corresponding to arrangements of six lines in $\mathbb { P } ^ { 2 }$ without triple intersection points).
Given the open subset $\mathcal { U } _ { \mathrm { s m } } \subset \overline { { M } } _ { Q } ^ { \nu }$ , consider the composition Usm → MνD1,6 99K D/ΓBB ( which is regular).
We show that this morphism extends to $\overline { { M } } _ { Q } ^ { \nu }$ giving a Sym $( Q )$ -equivariant morphism.
This extension is induced by the universal property of the normalization after we extend to MνQ the composition Usm → D/ΓBB → D/Γ0, which we denote by $\rho$ (the compactification $\overline { { \mathcal { D } / \Gamma } } ^ { \prime }$ is constructed in Lemma 8.50). To extend $\rho$ we use Theorem 8.39. So let $K$ be the field of fractions of a DVR $( A , { \mathfrak { m } } )$ and consider any $g \colon { \mathrm { S p e c } } ( K ) \to { \mathcal { U } } _ { \mathrm { s m } }$ .
We show that $\operatorname* { l i m } ( \rho \circ g ) \in { \overline { { \mathcal { D } / { \Gamma } } } } ^ { \prime }$ can be computed using only $\operatorname* { l i m } g \in \overline { { M } } _ { Q } ^ { \nu }$ .

Let $( X , B )$ be the stable toric pair parametrized by $\operatorname* { l i m } g \in \overline { { M } } _ { Q } ^ { \nu }$ and consider the corresponding stable pair $\left( B ^ { \bullet } , \left( { \textstyle \frac { 1 + \epsilon } { 2 } } \right) \Delta ^ { \bullet } | _ { B ^ { \bullet } } \right)$ .
We distinguish the following three cases:

• Case I: $B ^ { \bullet }$ is irreducible;  
• Case II: $B ^ { \bullet }$ has exactly two irreducible components glued along an irreducible curve;  
• Case III: otherwise.

Denote by $p _ { 0 }$ (resp.
$C _ { 0 }$ ) the image of the 0-cusps (resp.
1-cusps) under the morphism $\overline { { \mathcal { D } / \Gamma } } ^ { B B } $ $\overline { { \mathcal { D } / \Gamma } } ^ { \prime }$ .
The point $\operatorname* { l i m } ( \rho \circ g )$ can be computed as follows.
$\mathcal { U } _ { \mathrm { s m } }$ carries the family of $K 3$ surfaces $\left( { \mathfrak { S } } _ { \mathrm { s m } } ^ { \mathrm { K 3 } } , \epsilon ( \Delta \times \mathcal { U } _ { \mathrm { s m } } ) | _ { { \mathfrak { S } } _ { \mathrm { s m } } ^ { \mathrm { K 3 } } } \right)$ , where $\Delta$ is the toric boundary of $( \mathbb { P } ^ { 1 } ) ^ { 3 }$ .
Let $\mathcal { V } ^ { \prime }$ be the completion over ${ \mathrm { S p e c } } ( A )$ , or a finite ramified base change of it, of the restriction of ${ \mathfrak { S } } _ { \mathrm { s m } } ^ { \mathrm { K 3 } }$ to $\operatorname { S p e c } ( K )$ as a family of stable pairs (we omit the divisor for simplicity of notation).
In particular, ${ \mathcal { V } } _ { \mathfrak { m } } ^ { \prime }$ is the $\mathbb { Z } _ { 2 } ^ { 3 }$ -cover of $B ^ { \bullet }$ branched along $\Delta ^ { \bullet } | _ { B ^ { \bullet } }$ and it is the stable model of a degeneration of smooth K3 surface pairs.
Let $y$ be a birational modification of $\mathcal { V } ^ { \prime }$ which is a Kulikov degeneration.
Then $y _ { \mathfrak { m } }$ determines a unique point in $\overline { { \mathcal { D } / \Gamma } } ^ { \prime }$ , which depends on the type of $y _ { \mathfrak { m } }$ as follows:

• Type I: lim(ρ ◦ g) ∈ D/ΓBB is the image under the quotient $\mathcal { D } \to \mathcal { D } / \Gamma$ of the period point corresponding to $y _ { \mathfrak { m } }$ ;

• Type II: $\operatorname* { l i m } ( \rho \circ g ) \in C _ { 0 }$ and it corresponds to $j ( \mathcal { V } _ { \mathfrak { m } } )$ ;

• Type III: $\operatorname* { l i m } ( \rho \circ g ) = p _ { 0 }$ .

It is easy to observe that $B ^ { \bullet }$ falls into case I (resp.
II, III) if and only if ${ \mathcal { V } } _ { \mathfrak { m } } ^ { \prime }$ has generalized type I (resp.
II, III) (by Remark 8.37 $( d 1 ) , ( d 1 ^ { \prime } )$ , if $B ^ { \bullet }$ falls into case I, then ${ \mathcal { V } } _ { \mathfrak { m } } ^ { \prime }$ is smooth or it has isolated singularities of type $A _ { 1 }$ or $A _ { 3 }$ ).
Moreover, the generalized type of ${ \mathcal { V } } _ { \mathfrak { m } } ^ { \prime }$ equals the type of $y _ { \mathfrak { m } }$ by Theorem 8.48. In addition, if we are in case II, then it makes sense to define the $j$ -invariant $j ( \mathcal { V } _ { \mathfrak { m } } ^ { \prime } )$ , and this equals $j ( \mathcal { V } _ { \mathfrak { m } } )$ again by Theorem 8.48. In conclusion, we proved that $\operatorname* { l i m } ( \rho \circ g )$ only depends on $\operatorname { l i m } g$ .
□

Remark 8.53. Consider the three 0-cusps of D/ΓBB ( even, odd of type 1, and odd of type 2).
From the way we constructed the morphism $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }  \overline { { \mathcal { D } / \Gamma } } ^ { B B }$ , it is not clear to which one of these 0-cusps is a given 0-dimensional stratum mapped to.
Let us briefly show that a 0-dimensional boundary stratum maps to the 0-cusp with the same label (recall the terminology for the 0-dimensional boundary strata in Theorem 8.43). It is enough to show that a given point in the interior of the maximal 1-dimensional stratum of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ is mapped to the 1-cusp $C _ { \mathrm { o d d } }$ .
Consider a smooth oneparameter family with fibers isomorphic to $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ .
Equip this family with a divisor of coefficient $\frac { 1 + \epsilon } { 2 }$ cutting on each fiber our usual configuration of three pairs of lines without triple points, exception made for the central fiber where two lines belonging to the same pair come together and the other four lines are general.
It is easy to compute that the limit of this one-parameter family in $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ lies on the maximal 1-dimensional stratum (to show this, one has to compute the stable replacement of the central fiber, but this is done by blowing up the double line and then contracting the strict transforms of the two $( - 1 )$ -curves intersecting the double line).
The limit of the same family in $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$ belongs to $C _ { \mathrm { o d d } }$ , and this can be deduced using the GIT interpretation of $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$ in terms of degenerations of line arrangements in $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ (see [Oud10]).
This shows what we claimed.

# 8.5.3 Comparison between the boundaries of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ and $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$

We want to analyze the preimages of the three 0-cusps of D/ΓBB u nder the morphism $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu } $ D/ΓBB o f Theorem 8.52.

Observation 8.54. It follows from the proof of Theorem 8.52 and from Remark 8.53 that the preimage of the even 0-cusp (resp.
odd of type 1, odd of type 2) consists of the union of the strata of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ containing the even 0-dimensional stratum (resp.
odd of type 1, odd of type 2), and parametrizing degenerate stable pairs whose $\mathbb { Z } _ { 2 } ^ { 3 }$ -coves has generalized type III (see Definition 8.47). In what follows, we refer to the stable pairs $( a ) , ( b ) , ( c 2 ) , ( c 3 ) , ( d 3 )$ in Figure 8.3. Observe that $( b ) , ( c 2 )$ have 1-dimensional moduli, and $( a ) , ( c 3 ) , ( d 3 )$ are unique up to isomorphism.

# Even 0-cusp

The preimage of the even 0-cusp is the union of the boundary strata whose points parametrize stable pairs obtained by gluing copies of $( a ) , ( b )$ as shown in Figure 8.6. In particular, this preimage consists of the union of a divisor and a codimension 2 boundary stratum.
In Section 8.6 we show that the boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ has a toroidal behavior in a neighborhood of the preimage of the even 0-cusp.

# Odd 0-cusp of type 1

The preimage of the odd 0-cusp of type 1 is a codimension 2 stratum.
A point in this stratum parametrizes one of the following stable pairs:

• Glue two (c2);  
• Glue ( $c .$ 2) and $\left( c 3 \right)$ ;  
• Glue two (c3) (this is the stable pair parametrized by the odd 0-stratum of type 1).

The behavior of the compactification $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ in a neighborhood of the preimage of this 0-cusp is neither toroidal nor Baily-Borel (more about this is discussed in Section 8.6).

# Odd 0-cusp of type 2

By the stratification of the boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ in Figure 8.6, we can see that the preimage of the odd 0-cusp of type 2 consists only of the point parametrizing the stable pair ( $d \mathrm { { - } }$ ).

Observation 8.55. The compactification $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ is isomorphic to the Baily-Borel compactification in a neighborhood of the preimage of the odd 0-cusp of type 2. To prove this isomorphism, just

observe that the restriction of the morphism MνD1,6 → D/ΓBB t o this neighborhood is birational and finite, hence an isomorphism by the Zariski Main Theorem because D/ΓBB i s normal.

# 8.6 Relation with Looijenga’s semitoric compactifications

The behavior of the boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ suggests that $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ can possibly be isomorphic to a semitoric compactification $\overline { { \mathcal { D } / \Gamma } } ^ { \Sigma }$ .
These semitoric compactifications were introduced in [Loo03], and they depend on the choice of $\Sigma$ , which is called an admissible decomposition of the conical locus of $\mathcal { D }$ (see Definition 8.58). In what follows, we provide a natural choice of $\Sigma$ such that the boundary strata of the corresponding semitoric compactification $\overline { { \mathcal { D } / \Gamma } } ^ { \Sigma }$ are in bijection with the boundary strata of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ .
These considerations make us conjecture that $\overline { { \mathcal { D } / \Gamma } } ^ { \Sigma }$ is actually isomorphic to $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ .
We will address this conjecture in future work.

# 8.6.1 Admissible decomposition of the conical locus

Notation 8.56. We adopt the same notation as in [Loo03].
Let $V = L \otimes _ { \mathbb { Z } } \mathbb { C }$ , where the lattice $L = \mathbb { Z } ^ { 2 } ( 2 ) \oplus \mathbb { Z } ^ { 4 } ( - 1 )$ was introduced in Section 8.5.2. We call $\mathbb { Q }$ -isotropic an isotropic subspace $W ~ \subset ~ V$ which is defined over $\mathbb { Q }$ .
Denote by $I$ (resp.
$J$ ) a $\mathbb { Q }$ -isotropic line (resp.
plane) in $V$ .
Denote by $C _ { I } \subset ( I ^ { \perp } / I ) ( \mathbb { R } )$ (resp.
$C _ { J } \subset { \textstyle \bigwedge } ^ { 2 } J ( \mathbb { R } ) )$ one of the two connected components of $\{ x \in ( I ^ { \perp } / I ) ( \mathbb { R } ) \mid x \cdot x > 0 \}$ (resp.
$\bigwedge ^ { 2 } J ( \mathbb { R } ) \setminus \{ 0 \} )$ .
There is a canonical choice for $C _ { I }$ and $C _ { J }$ if we specify a connected component of $\mathcal { D }$ , as it is explained in [Loo03, Sections 1.1 and 1.2] (in this case, we let $\Gamma$ be the subgroup of isometries of $L$ which preserve the chosen connected component).
Denote by $C _ { I , + }$ (resp.
$C _ { J , + }$ ) the convex hull of the $\mathbb { Q }$ -vectors in $\overline { { C } } _ { I }$ (resp.
$\overline { { C } } _ { J }$ ).

Definition 8.57 ([Loo03, Definition 2.1]).
The conical locus of $\mathcal { D }$ is defined as

$$
C ( { \mathcal { D } } ) = \coprod _ { W \subset V , \mathrm { { \small ~ \alpha ~ } } } C _ { W } .
$$

Definition 8.58 ([Loo03, Definition 6.1]).
An admissible decomposition of $C ( \mathcal { D } )$ is a $\Gamma$ -invariant locally rational decomposition of $C _ { I , + }$ for all $\mathbb { Q }$ -isotropic lines $I$ such that, for all $\mathbb { Q }$ -isotropic planes $J$ , the support space of $C _ { J , + } \subset ( I ^ { \perp } / I ) ( \mathbb { R } )$ (see [Loo03, Lemma-Definition 4.5]) is independent of $I$ when we regard that support space as a subspace of $J ^ { \perp }$ containing $J$ .

We are ready to define our choice of admissible decomposition of $C ( \mathcal { D } )$ .

Definition 8.59. For any $\mathbb { Q }$ -isotropic line $I$ , consider the decomposition of $C _ { I , + }$ induced by the mirrors of the reflections with respect to the vectors of square $^ { - 1 }$ in the hyperbolic lattice $( I ^ { \perp } / I ) ( \mathbb { Z } )$ (recall that these vectors are called $( - 1 )$ -vectors).
Let $\Sigma$ be the decomposition of $C ( \mathcal D )$ induced by these mirrors.
This is an admissible decomposition of $C ( \mathcal { D } )$ , as we show in Corollary 8.65 after the considerations in Section 8.6.2.

# 8.6.2 Study of the decomposition $\Sigma$

There are three choices of $\mathbb { Q }$ -isotropic lines $I \subset V$ up to isometries of $L$ .
In each case, the hyperbolic lattice $( I ^ { \perp } / I ) ( \mathbb { Z } )$ is computed in [Oud10, Proposition 7.5].
Let $\Gamma _ { I }$ be the discrete reflection group generated by the reflections with respect to the $( - 1 )$ -vectors in $( I ^ { \perp } / I ) ( \mathbb { Z } )$ .

# Even 0-cusp

For $I$ corresponding to the even 0-cusp, we have that $( I ^ { \perp } / I ) ( \mathbb { Z } ) \cong \mathbb { Z } ^ { 1 , 3 }$ .
Running Vinberg’s algorithm to determine a fundamental domain for $\Gamma _ { I }$ (see [Vin75, Section 1] and [Vin75, Theorem 2.6 bis] for the stopping condition), we obtain the Coxeter diagram (see [Vin75, Section 1] or [Sca87, Table 2.2.8]) shown on the left in Figure 8.8. For the computations, we chose $( 1 , 0 , 0 , 0 )$ as our initial vector.

Observation 8.60. There is a bijection between the strata of the boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ containing the even 0-dimensional stratum (see Figure 8.6) and the elliptic and maximal parabolic subdiagrams of the Coxeter diagram up to isometries of $\mathbb { Z } ^ { 1 , 3 }$ (on the right in Figure 8.8).

Remark 8.61. Let $J$ be a $\mathbb { Q }$ -isotropic plane containing $I$ .
Consider the hyperplanes $v ^ { \bot } \subset$ $( I ^ { \perp } / I ) ( \mathbb { R } )$ where $v \in ( I ^ { \bot } / I ) ( \mathbb { Z } )$ is a $( - 1 )$ -vector and $C _ { J , + } \subset v ^ { \perp }$ .
All these hyperplanes intersect $C _ { I }$ nontrivially and their intersection is $C _ { J , + }$ .
Therefore, the support space of $C _ { J , + }$ is equal to $J$ when we regard it as a subspace of $J ^ { \perp }$ containing $J$ .

# Odd 0-cusp of type 1

If $I$ corresponds to the odd 0-cusp of type 1, then $( I ^ { \perp } / I ) ( \mathbb { Z } ) \cong \mathbb { Z } ^ { 1 , 1 } \oplus \mathbb { Z } ^ { 2 } ( - 2 )$ .
We run Vinberg’s algorithm to determine a fundamental domain for $\Gamma _ { I }$ .
Choose $v _ { 0 } = ( 1 , - 1 , 0 , 0 )$ as initial vector.

![](images/a577481b5e2a6650482268faf316c39f506b62549287949bc4041a9ae33fedfb.jpg)  
Figure 8.8: On the left, we show the Coxeter diagram for the discrete reflection group $\Gamma _ { I }$ , where $I$ corresponds to the even 0-cusp.
On the right are its elliptic and maximal parabolic subdiagrams, up to isometries of Z1,3

In step 0 of the algorithm, we first determine all the $( - 1 )$ -vectors which are orthogonal to $v _ { 0 }$ , and there are no such vectors.
In step 1, we determine all the $( - 1 )$ -vectors $x$ such that $v _ { 0 } \cdot x = 1$ .
These vectors are given by

$$
\alpha _ { ( a , b ) } = ( a ^ { 2 } + b ^ { 2 } , 1 - a ^ { 2 } - b ^ { 2 } , a , b ) , \ \mathrm { w i t h } \ ( a , b ) \in \mathbb { Z } ^ { 2 } .
$$

At step $n \geq 2$ no new vectors are added.
More precisely, if $n$ is even, then there are no $( - 1 )$ -vectors such that $v _ { 0 } \cdot x = n$ .
If $n$ is odd, let $x$ be a $( - 1 )$ -vector such that $v _ { 0 } \cdot x = n$ .
Then $x$ is not accepted by the algorithm because it is easy to check that $x \cdot \alpha _ { ( a , b ) } < 0$ if we choose $( a , b ) \in \mathbb { Z } ^ { 2 }$ such that $\begin{array} { r } { \left| a - \frac { x _ { 3 } } { n } \right| , \left| b - \frac { x _ { 4 } } { n } \right| \le \frac { 1 } { 2 } } \end{array}$ .
Therefore, $\mathbb { Z } ^ { 2 }$ is the set of vertices of the Coxeter diagram for $\Gamma _ { I }$ , where $( a , b ) \in \mathbb { Z } ^ { 2 }$ corresponds to $\alpha _ { ( a , b ) }$ .
Observe that

$$
\alpha _ { ( a , b ) } \cdot \alpha _ { ( c , d ) } = - 1 + ( a - c ) ^ { 2 } + ( b - d ) ^ { 2 } .
$$

This implies that, given any $( a , b ) \in \mathbb { Z } ^ { 2 }$ , then • There is no edge between $( a , b )$ and $( a \pm 1 , b ) , ( a , b \pm 1 )$ ;

![](images/3dd7cf1f9d7b6764fb11180f2e8c95dadccbacb52e65731d412da544543e3c81.jpg)  
Figure 8.9: On the left, we show part of the Coxeter diagram for $\Gamma _ { I }$ where we omit the dotted edges.
Here $I$ corresponds to the odd 0-cusp of type 1. On the right are its elliptic and maximal parabolic subdiagrams, up to isometries of $\mathbb { Z } ^ { 1 , 1 } \oplus \mathbb { Z } ^ { 2 } ( - 2 )$

• There is an edge labeled by $\infty$ between $( a , b )$ and $( a \pm 1 , b \pm 1 ) , ( a \pm 1 , b \mp 1 )$ ;

• $( a , b )$ is connected by a dotted edge to any other vertex different from $( a \pm 1 , b ) , ( a , b \pm 1 ) , ( a \pm$ $1 , b \pm 1 ) , ( a \pm 1 , b \mp 1 ) .$

Part of the infinite Coxeter diagram is shown on the left in Figure 8.9. (The computation we just carried out shares some similarities with [Con83].)

Observation 8.62. Also in this case there is a bijection between the strata of the boundary of $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ containing the odd 0-dimensional stratum of type 1 (see Figure 8.6) and the elliptic and maximal parabolic subdiagrams of the Coxeter diagram up to isometries of $\mathbb { Z } ^ { 1 , 1 } \oplus \mathbb { Z } ^ { 2 } ( - 2 )$ (on the right in Figure 8.9).

Remark 8.63. Let $J$ be a $\mathbb { Q }$ -isotropic plane containing $I$ and consider $C _ { J , + }$ .
Up to isometry there are two possibilities for $C _ { J , + }$ .
Assume that $C _ { J , + }$ is the ray generated by $( 2 , 0 , 1 , 1 )$ in $C _ { I , + } \subset$ $( I ^ { \perp } / I ) ( \mathbb { R } )$ .
One can easily see that the support space of $C _ { J , + }$ is $J$ (this is similar to what we did in Remark 8.61). If $C _ { J , + }$ is the ray generated by $( 1 , - 1 , 0 , 0 )$ , then $C _ { J , + }$ is not orthogonal to any $( - 1 )$ -vector in $( I ^ { \perp } / I ) ( \mathbb { Z } )$ , hence its support space is $J ^ { \perp }$ .
By [Oud10, Lemma 7.2], we have that $J$ corresponds to the even 1-cusp in the first case, and the odd 1-cusp in the second case.

# Odd 0-cusp of type 2

Let $U$ be the unique even unimodular lattice of signature $( 1 , 1 )$ (see Examples 2.9 (b)).
Then for $I$ corresponding to the odd 0-cusp of type 2, we have that $( I ^ { \perp } / I ) ( \mathbb { Z } ) \cong U \oplus \mathbb { Z } ^ { 2 } ( - 2 )$ , which is an even lattice.
In particular, $( I ^ { \perp } / I ) ( \mathbb { Z } )$ does not contain $( - 1 )$ -vectors.
Therefore, the decomposition of $C _ { I , + }$ induced by $\Sigma$ is given by $C _ { I , + }$ itself.

Remark 8.64. If $J$ is a $\mathbb { Q }$ -isotropic plane containing $I$ , then the support space of $C _ { J , + }$ is $J ^ { \perp }$ .

# 8.6.3 Conclusions

Corollary 8.65. The decomposition $\Sigma$ in Definition 8.59 is an admissible decomposition of $C ( \mathcal { D } )$ , and hence it gives rise to a semitoric compactification $\overline { { \mathcal { D } / \Gamma } } ^ { \Sigma }$ .

Proof.
We have that $\Sigma$ is admissible because Remarks 8.61, 8.63, and 8.64 imply that, for any $\mathbb { Q }$ -isotropic plane $J$ , the support space of $C _ { J , + }$ is independent from the choice of $\mathbb { Q }$ -isotropic line $I \subset J$ .
□

Observation 8.66. The Baily-Borel compactification D/ΓBB can be thought of as the semitoric compactification of $\mathcal { D } / \Gamma$ associated to the trivial admissible decomposition of $C ( \mathcal { D } )$ (see [Loo03, Example 6.2]).
In particular, by [Loo03, Lemma 6.6] we have a birational morphism $\overline { { \mathcal { D } / \Gamma } } ^ { \Sigma } $ $\overline { { \mathcal { D } / \Gamma } } ^ { B B }$ which is an isomorphism on $\mathcal { D } / \Gamma$ .

Theorem 8.67. Consider the two birational modifications $\overline { { { M } } } _ { D _ { 1 , 6 } } ^ { \nu } \right. \overline { { { D / \Gamma } } } ^ { B B } \left. \overline { { { D / \Gamma } } } ^ { \Sigma }$ of the BailyBorel compactification of $\mathcal { D } / \Gamma$ .
Then these are isomorphic in a neighborhood of the preimage of the odd 1-cusp of type 2. Moreover, there is an intersection-preserving bijection between the boundary strata of the two compactifications which also preserves the dimensions of the strata.

Proof.
The statement of the theorem summarizes Observations 8.55, 8.60, and 8.62.

Conjecture 8.68. The KSBA compactification $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ and the semitoric compactification $\overline { { \mathcal { D } / \Gamma } } ^ { \Sigma }$ of $\mathcal { D } / \Gamma$ are isomorphic.

Remark 8.69. To prove Conjecture 8.68 the first step would be to show that the birational map $\overline { { { M } } } _ { D _ { 1 , 6 } } ^ { \nu } \ _ { -- \to } ^ { } \overline { { { \mathcal { D } } / { \Gamma } } } ^ { \Sigma }$ is an isomorphism in a neighborhood of the preimage of the even 0-cusp, which is where we have a toroidal behavior.
To prove this, we plan to use the standard extension criterion used for instance in [AB12, CMGHL15], but adapted to our specific situation.
For this adaptation, the results in [Laz08] will be helpful to us.

# 8.7 Final remarks

Remark 8.70. In the case considered in this dissertation, it is remarkable that the theory of stable pairs produced a compactification $\overline { { M } } _ { D _ { 1 , 6 } } ^ { \nu }$ which has a toroidal behavior at the even 0-dimensional stratum, is isomorphic to the Baily-Borel compactification at the odd 0-dimensional stratum of type 2, and is a “mixture” of toroidal and Baily-Borel at the odd 0-dimensional stratum of type 1. In particular, this illustrates the behavior that should be expected in general when using stable pairs to compactify moduli spaces.

Remark 8.71. Associated to our 4-dimensional family of $D _ { 1 , 6 }$ -polarized Enriques surfaces there is a 4-dimensional family of K3 surfaces given by the $\mathbb { Z } _ { 2 } ^ { 3 }$ -covers $X  \mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ branched along three pairs of lines (see also Remark 8.15). One can also consider the minimal desingularization of the $\mathbb { Z } _ { 2 }$ -cover of $\mathbb { P } ^ { 2 }$ branched along six lines, which gives rise to a second 4-dimensional family of K3 surfaces.
These two families are distinct and they are related as follows.
We know from Remark 8.15 that $X$ can be viewed as a $( 2 , 2 , 2 )$ hypersurface in $( \mathbb { P } ^ { 1 } ) ^ { 3 }$ .
The group action $\mathbb { Z } _ { 2 } ^ { 3 } \cap X$ can be realized as the action of the restriction to $X$ of the involutions of $( \mathbb { P } ^ { 1 } ) ^ { 3 }$ given in an affine patch by $( x , y , z ) \mapsto ( ( - 1 ) ^ { i } x , ( - 1 ) ^ { j } y , ( - 1 ) ^ { k } z ) .$ , $i , j , k \in \{ 0 , 1 \}$ .
The subgroup $G < \mathbb { Z } _ { 2 } ^ { 3 }$ corresponding to $i + j + k = 2$ is isomorphic to $\mathbb { Z } _ { 2 } ^ { 2 }$ and acts symplectically on $X$ .
This means that the minimal resolution of $X / G$ is again a K3 surface, which in this case belongs to the second 4-dimensional family of K3 surfaces above.

Remark 8.72. Degenerations of six undistinguished lines in $\mathbb { P } ^ { 2 }$ with weight $\frac { 1 } { 2 } + \epsilon$ were considered in [Ale15, Section 6.2.1].
However, our case is different for the following reasons:

• First of all, we already explained in Remark 8.12 that our situation cannot be reduced to considering line arrangements in $\mathbb { P } ^ { 2 }$ ;  
• We keep track of three pairs of lines, and this is necessary to reconstruct the overlying degenerations of Enriques surfaces;

• Given a degeneration of $\mathbb { P } ^ { 2 }$ with the six lines, it is not clear how to immediately obtain the corresponding degeneration of $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ and the divisor on it;

• The boundaries of the two compactifications parametrizing in the interior six lines in $\mathbb { P } ^ { 2 }$ and three pairs of lines in $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ respectively are distinct, and the reason is the following.
A $D _ { 1 , 6 }$ - polarized Enriques surface $S$ can be realized as the minimal desingularization of the $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of $\mathbb { P } ^ { 2 }$ branched along three pairs of lines.
In this way $S$ comes with a natural polarization of degree 4, i.e. the pullback of a line in $\mathbb { P } ^ { 2 }$ .
However, the polarization coming from the $\mathbb { Z } _ { 2 } ^ { 2 }$ -cover of $\mathrm { B l _ { 3 } } \mathbb { P } ^ { 2 }$ has degree 6 and is given by $E _ { 1 } + E _ { 2 } + E _ { 3 }$ (see Observation 8.4).

# Bibliography

[Ale94] Alexeev, V.: Boundedness and $K ^ { 2 }$ for log surfaces.
Internat.
J.
Math.
5 (1994), no.
6, 779–810.

[Ale96a] : Log canonical singularities and complete moduli of stable pairs (1996).
arXiv:alggeom/9608013

[Ale96b] : Moduli spaces $M _ { g , n } ( W )$ for surfaces.
Higher-Dimensional Complex Varieties (Trento, 1994), de Gruyter, Berlin, 1996, pp.
1–22.

[Ale02] : Complete moduli in the presence of semiabelian group action.
Ann.
of Math.
(2) 155 (3) (2002), 611–708.

[Ale06] : Higher-dimensional analogues of stable curves.
International Congress of Mathematicians.
Vol.
II, 515–536, Eur.
Math.
Soc., Z¨urich, 2006.

[Ale08] : Weighted grassmannians and stable hyperplane arrangements (2008).
arXiv:0806.0881

[Ale15] : Moduli of weighted hyperplane arrangements.
Edited by Gilberto Bini, Mart´ı Lahoz, Emanuele Macr\`ı and Paolo Stellari.
Advanced Courses in Mathematics.
CRM Barcelona.
Birkh¨auser/Springer, Basel, 2015.

[AB12] Alexeev, V., Brunyate, A.: Extending the Torelli map to toroidal compactifications of Siegel space.
Invent.
Math.
188 (2012), no.
1, 175–196.

[AN99] Alexeev, V., Nakamura, I.: On Mumford’s construction of degenerating abelian varieties.
Tohoku Math.
J.
(2) 51 (1999), no.
3, 399–420.

[AP09] Alexeev, V., Pardini, R.: Explicit compactifications of moduli spaces of Campedelli and Burniat surfaces (2009).
arXiv:0901.4431

[AP12] : Non-normal abelian covers.
Compos.
Math.
148, no.
4, 1051–1084 (2012).
[AT15] Alexeev, V., Thompson, A.: Modular compactification of moduli of K3 surfaces of degree 2. Manuscript in preparation (2015).

[BHPV04] Barth, W.P., Hulek, K., Peters, C.A.M., Van de Ven, A.: Compact complex surfaces.
Second edition.
Ergebnisse der Mathematik und ihrer Grenzgebiete.
3. Folge.
A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics], 4. Springer-Verlag, Berlin, 2004.

[Bea96] Beauville, A.: Complex algebraic surfaces.
Translated from the 1978 French original by R.
Barlow, with assistance from N.
I.
Shepherd-Barron and M.
Reid.
Second edition.
London Mathematical Society Student Texts, 34. Cambridge University Press, Cambridge, 1996.

[BJ06] Borel, A., Ji, L.: Compactifications of symmetric and locally symmetric spaces.
Mathematics: Theory & Applications.
Birkh¨auser Boston, Inc., Boston, MA, 2006.

[CMGHL15] Casalaina-Martin, S., Grushevsky, S., Hulek, K., Laza, R.: Complete moduli of cubic threefolds and their intermediate Jacobians (2015).
arXiv:1510.08891

[Con83] Conway, J.H.: The automorphism group of the 26-dimensional even unimodular Lorentzian lattice.
J.
Algebra 80 (1983), no.
1, 159–163.

[Cos85] Cossec, F.R.: On the Picard group of Enriques surfaces.
Math.
Ann.
271 (1985), no.
4, 577–600.

[DM69] Deligne, P., Mumford, D.: The irreducibility of the space of curves of given genus.
Inst.
Hautes Etudes Sci.
Publ.
Math.
No.
36 1969 75–109.
´

[DL96] De Loera, J.A.: Nonregular triangulations of products of simplices.
Discrete Comput.
Geom.
15 (1996), no.
3, 253–264.

[DLRS10] De Loera, J.A., Rambau, J., Santos, F.: Triangulations.
Structures for algorithms and applications.
Algorithms and Computation in Mathematics, 25. Springer-Verlag, Berlin, 2010.

[Dol12] Dolgachev, I.: Classical algebraic geometry.
A modern view.
Cambridge University Press, Cambridge, 2012.

[Dol16] Dolgachev, I.: A brief introduction to Enriques surfaces (2016).
arXiv:1412.7744 [DZ01] Dolgachev, I., Zhang, D.-Q.: Coble rational surfaces.
Amer.
J.
Math.
123 (2001), no.
1, 79–114.

[Ebe13] Ebeling, W.: Lattices and codes.
A course partially based on lectures by Friedrich Hirzebruch.
Third edition.
Advanced Lectures in Mathematics.
Springer Spektrum, Wiesbaden, 2013.

[Fer03] Ferrand, D.: Conducteur, descente et pincement.
Bull.
Soc.
Math.
France 131 (2003), no.
4, 553–585.

[Fri83] Friedman, R.: Base change, automorphisms, and stable reduction for type III K3 surfaces.
The birational geometry of degenerations (Cambridge, Mass., 1981), pp.
277–298, Progr.
Math., 29, Birkh¨auser, Boston, Mass., 1983.

[FM83] Friedman, R., Morrison, D.R.: The birational geometry of degenerations: an overview.
The birational geometry of degenerations (Cambridge, Mass., 1981), pp.
1–32, Progr.
Math., 29, Birkh¨auser, Boston, Mass., 1983.

[Fuj15] Fujino, O.: Semipositivity theorems for moduli problems (2015).
arXiv:1210.5784 [GG14] Giansiracusa, N., Gillam, W.D.: On Kapranov’s description of $M _ { 0 , n }$ as a Chow quotient.
Turkish J.
Math.
38 (2014), no.
4, 625–648.

[GH94] Griffiths, P., Harris, J.: Principles of algebraic geometry.
Reprint of the 1978 original.
Wiley Classics Library.
John Wiley & Sons, Inc., New York, 1994.

[GKZ08] Gel’fand, I.M., Kapranov, M.M., Zelevinsky, A.V.: Discriminants, resultants and multidimensional determinants.
Reprint of the 1994 edition.
Modern Birkh¨auser Classics.
Birkh¨auser Boston, Inc., Boston, MA, 2008.

[Hac04] Hacking, P.: Compact moduli of plane curves.
Duke Math.
J.
124 (2004), no.
2, 213–257.
[HKT09] Hacking, P., Keel, S., Tevelev, J.: Stable pair, tropical, and log canonical compactifications of moduli spaces of del Pezzo surfaces.
Invent.
Math.
178 (2009), no.
1, 173–227.

[HMX14] Hacon, C., McKernan, J., Xu, C.: Boundedness of moduli of varieties of general type (2014).
arXiv:1412.1186

[Har77] Hartshorne, R.: Algebraic geometry.
Graduate Texts in Mathematics, No.
52. SpringerVerlag, New York-Heidelberg, 1977.

[Has03] Hassett, B.: Moduli spaces of weighted pointed stable curves.
Adv.
Math.
173 (2003), no.
2, 316–352.

[Hat02] Hatcher, A.: Algebraic topology.
Cambridge University Press, Cambridge, 2002.

[Hir64] Hironaka, H.: Resolution of singularities of an algebraic variety over a field of characteristic zero.
I, II.
Ann.
of Math.
(2) 79 (1964), 109–203; ibid.
(2) 79 1964 205–326.

[Hu14] Hu, X.: The compactifications of moduli spaces of Burniat surfaces with $2 \le K ^ { 2 } \le 5$ (2014).
arXiv:1312.3854

[Huy16] Huybrechts, D.: Lectures on K3 Surfaces.
Volume 158 of Cambridge Studies in Advanced Mathematics, Cambridge University Press, 2016.

[Kaw07] Kawakita, M.: Inversion of adjunction on log canonicity.
Invent.
Math.
167 (2007), no.
1, 129–133.

[Knu83a] Knudsen, F.F.: The projectivity of the moduli space of stable curves.
II.
The stacks $M _ { g , n }$ .
Math.
Scand.
52 (1983), no.
2, 161–199.

[Knu83b] Knudsen, F.F.: The projectivity of the moduli space of stable curves.
III.
The line bundles on $M _ { g , n }$ , and a proof of the projectivity of $M _ { g , n }$ in characteristic 0. Math.
Scand.
52 (1983), no.
2, 200–212.

[Kol09] Koll´ar, J.: Hulls and husks (2009).
arXiv:0805.0576  
[Kol13a] : Moduli of varieties of general type.
Handbook of moduli.
Vol.
II, 131–157, Adv.
Lect.
Math.
(ALM), 25, Int.
Press, Somerville, MA, 2013.

[Kol13b] : Singularities of the minimal model program.
With a collaboration of S´andor Kov´acs.
Cambridge Tracts in Mathematics, 200. Cambridge University Press, Cambridge, 2013.

[KM98] Koll´ar, J., Mori, S.: Birational geometry of algebraic varieties.
With the collaboration of C.
H.
Clemens and A.
Corti.
Translated from the 1998 Japanese original.
Cambridge Tracts in Mathematics, 134. Cambridge University Press, Cambridge, 1998.

[KSB88] Koll´ar, J., Shepherd-Barron, N.: Threefolds and deformations of surface singularities.
Invent.
Math.
91 (1988), no.
2, 299–338.

[KP15] Kov´acs, S., Patakfalvi, Z.: Projectivity of the moduli space of stable log-varieties and subadditvity of log-Kodaira dimension (2015).
arXiv:1503.02952

[Kul77] Kulikov, V.S.: Degenerations of K3 surfaces and Enriques surfaces.
Izv.
Akad.
Nauk SSSR Ser.
Mat.
41 (1977), no.
5, 1008–1042, 1199.

[Laz08] Laza, R.: Triangulations of the sphere and degenerations of K3 surfaces (2008).
arXiv:0809.0937

[Laz16] : The KSBA compactification for the moduli space of degree two K3 pairs.
J.
Eur.
Math.
Soc.
(JEMS) 18 (2016), no.
2, 225–279.

[Laz04] Lazarsfeld, R.: Positivity in algebraic geometry.
I.
Classical setting: line bundles and linear series.
Ergebnisse der Mathematik und ihrer Grenzgebiete.
3. Folge.
A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics], 48, Springer-Verlag, Berlin, 2004.

[Loo03] Looijenga, E.: Compactifications defined by arrangements.
II.
Locally symmetric varieties of type IV.
Duke Math.
J.
119 (2003), no.
3, 527–588.

[Mil58] Milnor, J.: On simply connected 4-manifolds.
1958 Symposium internacional de topolog´ıa algebraica International symposium on algebraic topology pp.
122–128 Universidad Nacional Aut´onoma de M´exico and UNESCO, Mexico City.

[MS74] Milnor, J.; Stasheff, J.: Characteristic classes.
Annals of Mathematics Studies, No.
76. Princeton University Press, Princeton, N.
J.; University of Tokyo Press, Tokyo, 1974.

[Mum72] Mumford, D.: An analytic construction of degenerating abelian varieties over complete rings.
Compositio Math.
24 (1972), 239–272.

[Mum99] : The red book of varieties and schemes.
Second, expanded edition.
Includes the Michigan lectures (1974) on curves and their Jacobians.
With contributions by Enrico Arbarello.
Lecture Notes in Mathematics, 1358. Springer-Verlag, Berlin, 1999.

[Nam76] Namikawa, Y.: A new compactification of the Siegel space and degeneration of Abelian varieties.
I.
II.
Math.
Ann.
221 (1976), no.
2, 97–141.

[Oud10] Oudompheng, R.: Periods of an arrangement of six lines and Campedelli surfaces.
Universit´e de Nice-Sophia Antipolis, PhD thesis, Part II (2010).
arXiv:1106.4846

[Par91] Pardini, R.: Abelian covers of algebraic varieties.
J.
Reine Angew.
Math.
417 (1991), 191– 213.

[PP81] Persson, U., Pinkham, H.: Degeneration of surfaces with trivial canonical bundle.
Ann.
of Math.
(2) 113 (1981), no.
1, 45–66.

[Pfe00] Pfeifle, J.: Secondary polytope of the 3-cube.
Electronic Geometry Model No.
2000.09.031. http://www.eg-models.de/models/Polytopes/Secondary_Polytopes/2000.09.031/_preview.html

[San01] Santos, F.: On the refinements of a polyhedral subdivision.
Collect.
Math.
52 (2001), no.
3, 231–256.

[Sca87] Scattone, F.: On the compactification of moduli spaces for algebraic K3 surfaces.
Mem.
Amer.
Math.
Soc.
70 (1987), no.
374, x+86 pp.

[Ser73] Serre, J.P.: A course in arithmetic.
Graduate Texts in Mathematics, No.
7. Springer-Verlag, New York-Heidelberg, 1973.

[Sha80] Shah, J.: A complete moduli space for K3 surfaces of degree 2. Ann.
of Math.
(2) 112 (1980), no.
3, 485–510.

[Sha81] Shah, J.: Degenerations of K3 surfaces of degree 4. Trans.
Amer.
Math.
Soc.
263 (1981), no.
2, 271–308.

[SB83] Shepherd-Barron, N.I.: Extending polarizations on families of K3 surfaces.
The birational geometry of degenerations (Cambridge, Mass., 1981), pp.
135–171, Progr.
Math., 29, Birkh¨auser, Boston, Mass., 1983.

[Ver83] Verra, A.: On Enriques surface as a fourfold cover of $\mathbb { P } ^ { 2 }$ .
Math.
Ann.
266 (1983), no.
2, 241–250.

[Vie95] Viehweg, E.: Quasi-projective moduli for polarized manifolds.
Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)], 30. SpringerVerlag, Berlin, 1995.

[Vin75] Vinberg, E.B.: \` Some arithmetical discrete groups in Lobaˇcevski˘ı spaces.
Discrete subgroups of Lie groups and applications to moduli (Internat.
Colloq., Bombay, 1973), pp.
323–348.
Oxford Univ.
Press, Bombay, 1975.