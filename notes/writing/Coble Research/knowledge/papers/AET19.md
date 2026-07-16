---
title: Compact moduli of elliptic K3 surfaces
authors:
- Kenneth Ascher & Dori Bejleri
year: 2019
bibkey: AET19
tags:
- paper
- extraction
abstract: |
  We construct various modular compactifications of the space of elliptic K3 surfaces using tools from the minimal model program, and explicitly describe the surfaces parametrized by their boundaries.
  The coarse spaces of our constructed compactifications admit morphisms to the Satake-Baily-Borel compactification and the GIT compactification of Miranda.
---

# COMPACT MODULI OF ELLIPTIC K3 SURFACES

KENNETH ASCHER & DORI BEJLERI

Abstract.
We construct various modular compactifications of the space of elliptic K3 surfaces using tools from the minimal model program, and explicitly describe the surfaces parametrized by their boundaries.
The coarse spaces of our constructed compactifications admit morphisms to the Satake-Baily-Borel compactification and the GIT compactification of Miranda.

# 1. Introduction

Ever since the compactification of the moduli space of smooth curves by Deligne-Mumford was accomplished, the search for analogous compactifications in higher dimensions became an actively studied problem in algebraic geometry.
While moduli in higher dimensions is highly intricate, the pioneering work of Koll´ar-Shepherd-Barron [KSB88] and Alexeev [Ale94], (see also [HX13, HMX18, KP17, Kol21], etc.) has established much of the underlying framework for modular compactifications in the (log) general type case via KSBA stable pairs, where semi-log canonical singularities serve as the generalization of nodal curves (see the survey [Kol18]).

One of the most sought after compactifications is for the space of K3 surfaces.
K3 surfaces do not immediately fit into the above framework as they are not of general type, but rather Calabi-Yau varieties.
On the other hand, like for abelian varieties, since the space of (polarized) K3 surfaces is a locally symmetric variety, it has several natural compactifications, e.g. the Satake-Baily-Borel (SBB), toroidal, and semi-toric compactifications of Looijenga.
Unlike the KSBA approach, these compactifications do not necessarily carry a universal family or modular meaning over the boundary.

As such, one of the central questions in moduli theory is to give the aforementioned naturally arising compactifications a stronger geometric meaning by connecting them with a KSBA compactification.
With this in mind, the goal of this paper is to construct modular compactifications for elliptic K3 surfaces – compactifications where the degenerate objects are K3 surfaces with controlled singularities – and understand how they compare to the Satake-Baily-Borel compactification.

By the Torelli theorem, the moduli space of polarized K3 surfaces is a 19 dimensional locally symmetric variety.
Similarly, it is well known that the moduli space of elliptic K3 surfaces with a section, which we denote by $W$ , is an 18 dimensional locally symmetric variety, corresponding to $U$ -polarized K3 surfaces (see [Dol96, Nik79]).
Recall that a generic elliptic K3 surface $f : X \to \mathbb { P } ^ { 1 }$ with section $S$ has $2 4 \ \mathrm { I } _ { 1 }$ singular fibers.
Let $\textstyle F _ { { \mathcal { A } } } = \sum a _ { i } F _ { i }$ denote the sum of these 24 fibers weighted by $a _ { i } \in \mathbb { Q } \cap [ 0 , 1 ] ^ { 2 4 }$ .
We consider the closure of the locus of pairs ( $f : X \to C , S + F _ { \mathcal { A } } )$ inside the KSBA moduli space.
For the moment, we assume all $a _ { i } = a$ , so that we can quotient by $S _ { 2 4 }$ .
Denote the closure of the resulting locus by $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ , and let $0 < \epsilon \ll 1$ .

Theorem 1.1. (see Theorem 6.13, Theorem 6.15, Theorem 6.14, and Figure 1) The proper DeligneMumford stacks $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ for $a \in \mathbb { Q } \cap [ 0 , 1 ]$ give modular compactifications of $W$ .
There is an explicit classification of the broken elliptic $K \mathcal { 3 }$ surfaces parametrized by $\overline { { \mathscr { W } } } _ { \sigma } ( \epsilon )$ , and an explicit morphism from the coarse space $\overline { { \mathrm { W } } } _ { \sigma } ( \epsilon )  \overline { { \mathrm { W } } } ^ { * }$ to the SBB compactification of $W$ .
Furthermore, the surfaces paramaterized by $\overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ satisfy $\mathrm { H } ^ { 1 } ( X , { \mathcal { O } } _ { X } ) = 0$ and $\omega _ { X } \cong { \mathfrak { O } } _ { X }$ .

Theorem 1.1 shows that the boundary of $\overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ parametrizes K3 surfaces with slc singularities.
Although $\overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ compactifies a moduli spaces of pairs, it gives a natural compactification of the space of elliptic K3s as the choice of fibers is intrinsic.
Indeed, without a boundary divisor, the moduli space is a non-separated Artin stack.
In Section 7, we present an alternative explicit description of the surfaces parametrized on the boundary more akin to Kulikov models.
In particular, we show that we can decompose the boundary of $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ into combinatorially described parameter spaces.

As mentioned above, viewing the moduli space of elliptic K3 surfaces as a locally symmetric variety, one naturally obtains the SBB compactification $W ^ { * }$ .
While a priori the SBB compactification does not have a modular meaning, it turns out that in the case of elliptic K3 surfaces, this compactification can be identified with the GIT compactification of Weierstrass models of Miranda ${ \overline { { \mathrm { W } } } } ^ { G }$ (see Section 2.6 and [OO18, Theorem 7.9]), which provides some geometric meaning.
In particular, in the theorem above, as well as the remainder of this section, all of our spaces admit morphisms to ${ \overline { { \mathrm { W } } } } ^ { G }$ .

One benefit of the SBB compactification is that all of the parametrized surfaces are irreducible.
The next theorem discusses a modular compactification, coming from the KSBA approach, where the boundary parametrizes irreducible surfaces.
Indeed, consider pairs $f : X \to \mathbb { P } ^ { 1 } , S + \epsilon F )$ for $0 < \epsilon \ll 1$ , i.e. only one singular fiber carries a non-zero weight, and this weight is infinitesimally small.
We denote the closure of this locus by $\overline { { \mathcal { K } } } _ { \epsilon }$ .

Theorem 1.2. (see Theorem 8.1, Theorem 8.2, and Figure 1) The compact moduli space $\mathcal { K } _ { \epsilon }$ parametrizes irreducible semi-log canonical Weierstrass K3 surfaces satisfying $\mathrm { H } ^ { 1 } ( X , { \mathcal { O } } _ { X } ) = 0$ and $\omega _ { X } \cong { \mathfrak { O } } _ { X }$ .
Moreover, there is an explicit generically finite morphism from the coarse space $\overline { { \mathrm { K } } } _ { \epsilon }  \overline { { \mathrm { W } } } ^ { * }$ .

In light of the above theorem, it is natural to ask how the compactifications $\overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ and $\overline { { \mathcal { K } } } _ { \epsilon }$ are related.
In previous work (see [AB21a]) we showed the existence of wall-crossing morphisms on moduli spaces of elliptic surfaces.
In particular, our previous work implies that (up to a 24-to-1 base change corresponding to choosing a singular fiber) the universal families of $\overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ and $\overline { { \mathcal { K } } } _ { \epsilon }$ are related by an explicit series of flips and divisorial contractions as the weights of 23 of the marked fibers are reduced from $\epsilon$ to $0$ .
This aspect is crucial to our work (see e.g. Section 8.1) – these explicit morphisms allow us to understand how our compactifications are related to each other, and how they compare to others lacking a modular meaning.

Finally, we introduce one more KSBA compactification.
While in $\overline { { \mathcal { K } } } _ { \epsilon }$ we mark one singular fiber with weight $\epsilon$ , it is natural to ask what happens if we mark any fiber, not necessarily singular, with weight $\epsilon$ .
We denote this compactification by $\overline { { \mathcal { F } } } _ { \epsilon }$ .
Before stating the final theorem of the introduction, we point the reader to Figure 1 for an overview of the spaces introduced in this paper.

![](images/36258bd2fecc73a17830787ad16a7f37f8a7aad4d717b0ebbcda3ac76805ba84.jpg)  
Figure 1. This diagram shows the various compactifications we introduce in this paper as well as how they are related (see also Remark 4.10).

$\overline { { \mathcal { B } } } ^ { \nu }$ : The normalization of Brunyate’s compactification with small weights on both section and singular fibers (see Section 1.1).  
$\overline { { \mathcal { W } } } ( \mathcal { A } )$ : KSBA compactification with $\mathcal A$ -weighted singular fibers.  
$\mathcal { W } _ { \sigma } ( a )$ : When ${ \mathcal { A } } = ( a , \ldots , a )$ , we quotient by $\mathrm { S _ { 2 4 } }$ .
$\overline { { \mathcal { K } } } _ { \epsilon }$ : KSBA compactification with a single $\epsilon$ -marked singular fiber (where $\epsilon \ll 1$ ).
${ \mathcal { F } } _ { \epsilon }$ : KSBA compactification with any fiber marked by $\epsilon$ (where $\epsilon \ll 1$ ).
$\overline { { \mathrm { W } } } ^ { * }$ : SBB compactification of the period domain moduli space $W$ .
${ \overline { { \mathrm { W } } } } ^ { G }$ : Miranda’s GIT compactification of Weierstrass models (see Section 2.6). ${ \widetilde { \mathrm { W } } } ^ { G }$ : GIT compactification of Weierstrass models with a chosen fiber (see discussion after Theorem 1.3).

Theorem 1.3. (see Theorem 8.8 and Figure 1) There exists a smooth proper Deligne-Mumford stack $\overline { { \mathcal { F } } } _ { \epsilon }$ parametrizing semi-log canonical elliptic $K \mathcal { 3 }$ surfaces with a single marked fiber.
Its coarse space is isomorphic to an explicit GIT quotient $\widetilde { \mathrm { W } } ^ { G }$ of Weierstrass $K \mathcal { 3 }$ surfaces and a chosen fiber.
Furthermore, the surfaces parametrized by $\overline { { \mathcal { F } } } _ { \epsilon }$ satisfy $\mathrm { H } ^ { 1 } ( X , { \mathcal { O } } _ { X } ) = 0$ and $\omega _ { X } \cong { \mathfrak { O } } _ { X }$ .

On the interior, $\overline { { \mathcal { F } } } _ { \epsilon }$ is a $\mathbb { P } ^ { 1 }$ bundle over $W$ .
In this sense, $\overline { { \mathcal { F } } } _ { \epsilon }$ is similar in spirit to the KSBA compactification of Laza of degree two K3 surfaces [Laz16].
The GIT problem of Miranda can be modified to parametrize Weierstrass fibrations with a chosen fiber (see Section 8.3), denoted above by $\widetilde { \mathrm { W } } ^ { G }$ .
It turns out that $\widetilde { \mathrm { W } } ^ { G }$ is precisely the coarse moduli space of $\overline { { \mathcal { F } } } _ { \epsilon }$ – in particular, the morphism $\overline { { \mathcal { F } } } _ { \epsilon }  \widetilde { \mathrm { W } } ^ { G }$ realizes $\mathcal { F } _ { \epsilon }$ as a smooth Deligne-Mumford stack.

Our approach in this paper combines explicit use of the theory of twisted stable maps (see e.g. [AB19]) with the minimal model program.
The various compactifications are then related by an explicit series of wall-crossing morphisms.
In particular, we wish to emphasize that the power of our approach lies in understanding the compactifications for various coefficients and how they are related via wall crossing morphisms.
Often the spaces with very small coefficients are the smallest compactifications which are still modular, but having access to the spaces for all coefficients is fruitful in understanding the geometry of compactifications obtained via different methods.

1.1. Previous results.
Using Kulikov models, Brunyate’s thesis [Bru15] constructs a stable pairs compactification of the space of elliptic K3 surfaces $\overline { { \mathcal { B } } }$ which parametrizes pairs $( X , \epsilon S + \delta F )$ , where $\epsilon$ and $\delta$ are both small.
In particular, Brunyate gives a classification of the surfaces appearing on the boundary, and conjectures that the normalization of $\overline { { \mathcal { B } } }$ is a toroidal compactification.
Recently, Alexeev-Brunyate-Engel [ABE20] confirmed Brunyate’s conjecture, and showed that this space is isomorphic to a particular toroidal compactification using the theory of integral affine geometry and continuing the program started in [AET19].

One difference between our approach and the work of Brunyate, is in our descriptions of the compactifications at various weights and choice of markings.
Instead of using Kulikov models, we describe the steps of MMP and the induced wall-crossing morphisms that relate the stable limits of elliptic K3 surfaces for different weights to highlight the underlying geometry of the various compactifications.
Brunyate’s space $\overline { { \mathcal { B } } }$ admits a morphism $\overline { { \mathscr { W } } } _ { \sigma } ( \epsilon )  \overline { { \mathscr { B } } }$ which identifies $\mathcal { W } _ { \sigma } ( \epsilon )$ with the normalization of $\overline { { \mathcal { B } } }$ (see Proposition 4.4 and Remark 4.7). In particular, the boundary components of $\overline { { \mathcal { B } } }$ and $\overline { { \mathscr { W } _ { \sigma } ( \epsilon ) } }$ are in bijection (see Remark 4.5) and the moduli spaces parametrize essentially the same surfaces.
Indeed there is a sequence of flips relating the universal family of $\overline { { \mathcal { B } } }$ and the universal family over $\overline { { \boldsymbol { \mathcal { W } } } } _ { \sigma } ( \epsilon )$ which induces this morphism.

Finally, we note that in a slightly different direction, Inchiostro constructs a KSBA compactification of the space of Weierstrass fibrations (of not necessarily K3 surfaces) with both section and fibers marked by $0 < \epsilon , \delta \ll 1$ [Inc20],

1.2. Other lattice polarizations.
It is natural to consider fibrations with specified singular fibers.
In this case, one obtains a moduli space which is a locally symmetric variety, corresponding to a $M$ -lattice polarization, encoding the singular fiber type.
Our methods work in that case as well.
Here we quickly discuss an example of this point of view.

Example 1.4. Consider the lattice $M = U \oplus D _ { 4 } ^ { \oplus 4 }$ .
Then $M$ -polarized K3 surfaces correspond to $4 \mathrm { { I } _ { 0 } ^ { * } }$ isotrivial elliptic K3 surfaces.
Equivalently, these are Kummer K3 surfaces obtained from abelian surfaces of the form $E \times E ^ { \prime }$ with the elliptic fibration induced by the projection $E \times E ^ { \prime } \to E$ .
Marking the 4 minimal Weierstrass cusps by a single weight $a$ gives us a moduli space whose coarse space is two copies of the $j$ -line, one parametrizing the $j$ -invariant of the fibration, and the other the $j$ -invariant of the configuration of singular fibers.
The stable pairs compactification has coarse space given by $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 } = \overline { { M } } _ { 0 , 4 } \times \overline { { M } } _ { 0 , 4 }$ .
The universal family consists of $4 \mathrm { N } _ { 1 }$ isotrivial $j$ -invariant $\infty$ fibrations over the locus $\{ \infty \} \times \mathbb { P } ^ { 1 }$ , a union $X \cup _ { \mathrm { I 0 } } X$ of two copies of the $2 \mathrm { I } _ { 0 } ^ { \ast }$ rational elliptic surface glued along a smooth fiber over the locus $\mathbb { P } ^ { 1 } \times \{ \infty \}$ , and a union $X \cup _ { \mathrm { N } _ { 0 } } X$ of two copies of the 2N $^ { 1 }$ isotrivial $j$ -invariant $\infty$ fibration glued along an $\mathrm { N } _ { 0 }$ fiber over the point $( \infty , \infty )$ .

1.3. Structure of the paper.
In Section 2 we discuss the background on elliptic K3 surfaces and their moduli (as a period domain, the Satake-Baily-Borel compactification, and a Geometric Invariant Theory compactification).
In Section 3 we review the results from our previous works ([AB17, AB19, AB21a, AB21b]) on KSBA compactifications of moduli spaces of elliptic fibrations and the connection with twisted stable maps.
In Section 4 we restrict to the case of elliptic K3 surfaces and collect the definitions of and preliminary observations on the compactifications we consider in this paper, including a discussion on isotrivial $j$ -invariant $\infty$ fibrations of K3 type.

The main body of the paper begins with Section 5 where we discuss the wall-crossings that occur for the compactification $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ as the coefficient $a$ is lowered from 1 down to $1 / 1 2 + \epsilon$ for $0 < \epsilon \ll 1$ .
In Section 6 we continue the wall-crossing analysis as $a$ is decreased down to $0 < \epsilon \ll 1$ , and we prove Theorem 1.1, which describes the surfaces appearing on the boundary of the moduli space $\overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ .
In Section 7 we use Theorem 1.1 and twisted stable maps (Section 3.2) to explicitly describe the boundary components of $\overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ .
Finally, in Section 8 we describe the moduli spaces with one marked fiber ( $\overline { { \mathcal { K } } } _ { \epsilon }$ and $\overline { { \mathcal { F } } } _ { \epsilon }$ ) and prove Theorem 1.2 and Theorem 1.3; the latter theorem is proven by introducing a modified version of Miranda’s GIT compactification (see Section 8.3).

Acknowledgments.
We thank Valery Alexeev, Izzet Coskun, Kristin DeVleming, Giovanni Inchiostro, J´anos Koll´ar, Radu Laza, Yuchen Liu, Siddharth Mathur, Yuji Odaka, and David Yang.
We thank Adrian Brunyate for pointing out a gap in a previous version.
We thank the referees for their very helpful comments and suggestions.
Both authors supported by NSF Postdoctoral Fellowships.
Part of this paper was written while K.A.
was in residence at Mathematical Sciences Research Institute in Berkeley, CA, during the Spring 2019, supported by the National Science Foundation under Grant No.
1440140. K.A.
partially supported by NSF grant DMS-2140781 (formerly DMS-2001408).

# 2. Elliptic K3 surfaces and their moduli

2.1. Elliptic surfaces.
We begin with the basic definitions surrounding elliptic surfaces following [AB21a] (see also [Mir89]).

Definition 2.1. An irreducible elliptic surface with section ( $f : X \to C , S )$ is an irreducible surface $X$ together with a surjective proper flat morphism $f : X \to C$ to a smooth curve $C$ and a section $S$ such that:

(1) the generic fiber of $f$ is a stable elliptic curve, and (2) the generic point of the section is contained in the smooth locus of $f$ .

We call the pair ( $f : X \to C , S ,$ ) standard if all of $S$ is contained in the smooth locus of $f$

Definition 2.2. A Weierstrass fibration is an elliptic surface obtained from a standard elliptic surface by contracting all fiber components not meeting the section.
We call the output of this process a Weierstrass model.
If starting with a smooth relatively minimal elliptic surface, we call the result a minimal Weierstrass model.

The geometry of an elliptic surface is largely influenced by the fundamental line bundle $\mathcal { L }$

Definition 2.3. The fundamental line bundle of a standard elliptic surface is $\mathcal { L } : = ( f _ { \ast } \mathcal { N } _ { S / X } ) ^ { - 1 }$ , where $\mathcal { N } _ { S / X }$ denotes the normal bundle of $S$ in $X$ .
For an arbitrary elliptic surface we define $\mathcal { L }$ as the line bundle associated to its minimal semi-resolution1.

For $X$ a standard elliptic surface, the line bundle $\mathcal { L }$ is invariant under taking a semi-resolution or Weierstrass model, is independent of choice of section $S$ , has non-negative degree, and determines the canonical bundle of $X$ if $X$ is either relatively minimal or Weierstrass (see [Mir89, III.1.1]).

2.2. Singular fibers.
If $f : X \to C , S )$ is a smooth relatively minimal elliptic surface, then $f$ has finitely many singular fibers which are each unions of rational curves with possibly non-reduced components whose dual graphs are ADE Dynkin diagrams.
The singular fibers were classified by Kodaira-Ner´on (see [BHPVdV04, Section V.7]).

An elliptic surface in Weierstrass form can be described locally by an equation of the form $y ^ { 2 } = x ^ { 3 } + A x + B$ where $A$ and $B$ are functions of the base curve.
Furthermore, the possible singular fiber types can be characterized in terms of vanishing orders of $A$ and $B$ by Tate’s algorithm (see [SS09, Table 1]).
Moreover, if the smooth relatively minimal model ( $f : X \to C , S )$ has a singular fiber with a given Dynkin diagram, the minimal Weierstrass model will have an ADE singularity of the same type.

2.3. Elliptic K3 surfaces.
By the canonical bundle formula and the observation that $\deg \mathcal { L } = 0$ if and only if the surface is a product, a smooth elliptic surface with section ( $f : X \to C , S )$ ) is a K3 surface if and only if $C \cong \mathbb { P } ^ { 1 }$ and $\deg ( \mathcal { L } ) = 2$ (see [Mir89, III.4.6]).

Definition 2.4. A standard (possibly singular) elliptic surface is of $\mathbf { \delta \mathbf { k 3 } }$ type if $C \cong \mathbb { P } ^ { 1 }$ and $\deg ( \mathcal { L } ) = 2$ .

For an elliptic surface of K3 type, the Weierstrass model is given by $y ^ { 2 } = x ^ { 3 } + A x + B$ , where $A$ and $B$ are sections of $\mathcal { O } ( 8 )$ and O(12) respectively, and the discriminant $\mathcal { D } = 4 A ^ { 3 } + 2 7 B ^ { 2 }$ is a section of ${ \mathcal { L } } ^ { \otimes 1 2 } \cong { \mathcal { O } } ( 2 4 )$ .

Remark 2.5. The number of singular fibers of a Weierstrass elliptic K3 counted with multiplicity is 24, and a generic elliptic K3 has exactly 24 nodal (I1) singular fibers.

We now discuss lattice polarized K3 surfaces and their moduli (see [HT15, Fri84a, Fri84b]).

2.4. Moduli of lattice polarized K3 surfaces.
An elliptic K3 with section $f : X \to \mathbb { P } ^ { 1 } , S )$ are characterized by the fact that NS(X) contains a lattice $U$ which is spanned by the classes of the fiber $f$ and section $S$ .
The moduli of K3 surfaces with specified NS(X) were studied by Dolgachev [Dol96] (see also [Nik79]).
By the Torelli theorem for polarized K3 surfaces, the moduli space of minimal Weierstrass elliptic K3 surfaces with at worst ADE singularities is an 18-dimensional locally symmetric variety $W = \Gamma \backslash D$ associated to the lattice $U _ { \mathrm { K 3 } } ^ { \perp } \cong U ^ { 2 } \oplus E _ { 8 } ^ { 2 }$ .

2.5. The Satake-Baily-Borel compactification.
One can use the techniques of Baily-Borel [BB66] to obtain a compactification $\overline { { \mathrm { W } } } ^ { * }$ by adding some curves and points.
We briefly review this compactification following [LZ16, Section 3.1].
The boundary components of $\overline { { \mathrm { W } } } ^ { * }$ are determined by rational maximal parabolic subgroups of the identity component of the orthogonal group $O ( 2 , 1 8 )$ of the lattice $U _ { \mathrm { K 3 } } ^ { \perp }$ .
Every boundary component of $\overline { { \mathrm { W } } } ^ { * }$ has the structure of a locally symmetric variety of lower dimension.
Furthermore, we recall the following properties:

(3) It is minimal : if $S$ is a smooth variety with $\bar { S }$ a smooth simple normal crossing compactification, then any locally liftable map $S  W$ extends to a regular map $\overline { { S } }  \overline { { \mathrm { W } } } ^ { * }$ .

Theorem 2.6. (see [HT15, Section 2.3] and [Sca87]) The boundary of $\overline { { \mathrm { W } } } ^ { * }$ is a union of zero and one dimensional strata.
The 0-dim strata correspond to K3s of Type III, and the 1-dim strata to degenerate K3’s of Type II.
Moreover, the 1-dim strata are all rational curves, each parametrizing the $j$ -invariant of the elliptic double curves appearing in the corresponding Type II degenerate K3.

2.6. Geometric invariant theory.
Miranda [Mir81] used geometric invariant theory (GIT) to construct a compactification of the moduli space of Weierstrass fibrations, and completed an explicit classification in the case of rational elliptic surfaces.
More recently, Odaka-Oshima [OO18] explicitly calculated Miranda’s compactification for the case of elliptic K3 surfaces.
Moreover, they showed that the GIT compactification of Miranda ${ \overline { { \mathrm { W } } } } ^ { G }$ is isomorphic to $W ^ { * }$ , the SBB compactification.
In particular, using this identification, one is able to give a geometric meaning to $W ^ { * }$ by relating the boundary of $W ^ { * }$ with the GIT polystable orbits in ${ \overline { { \mathrm { W } } } } ^ { G }$ .
We review these results now.

Let $\Gamma _ { n } = \Gamma ( \mathbb { P } ^ { 1 } , \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( n ) )$ .
The surface $X$ has a Weierstrass equation, and as such $X$ can be realized as a divisor in a $\mathbb { P } ^ { 2 }$ -bundle over the base curve.
For the Weierstrass model of an elliptic K3 surface, we think of $X$ as being the closed subscheme of $\mathbb { P } ( \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( 4 ) \oplus \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( 6 ) \oplus \mathcal { O } _ { \mathbb { P } ^ { 1 } }$ ) defined by the equation $y ^ { 2 } z = x ^ { 3 } + A x z ^ { 2 } + B z ^ { 3 }$ , where $A \in \Gamma _ { 8 }$ , $B \in \Gamma _ { 1 2 }$ , and

(1) $4 A ( q ) ^ { 3 } + 2 7 B ( q ) ^ { 2 } = 0$ precisely at the (finitely many) singular fibers $X _ { q }$ (2) and for each $q \in \mathbb { P } ^ { 1 }$ we have $v _ { q } ( A ) \leq 3$ or $v _ { q } ( B ) \leq 5$ .

We note that any Weierstrass elliptic K3 surface (with section) and ADE singularities satisfies the above conditions, and conversely, the surface defined as above is a Weierstrass elliptic K3 surface with section and ADE singularities (see [OO18, Theorem 7.1]).

We denote by $V _ { 2 4 } = \Gamma _ { 8 } \oplus \Gamma _ { 1 2 }$ and the GIT moduli space for Weierstrass elliptic K3 surfaces by $\overline { { \mathrm { W } } } ^ { G } = V _ { 2 4 } ^ { s s } / / S L _ { 2 }$ .
By the above discussion the open locus $\mathrm { W } ^ { G } \subset \overline { { \mathbb { W } } } ^ { G }$ parametrizes the ADE Weierstrass elliptic K3 surfaces.
The following theorem describes the boundary $\overline { { \mathrm { W } } } ^ { G } \setminus \mathrm { W } ^ { G }$ .

heorem 2.7. [OO18, Proposition 7.4] The boundary $\overline { { \operatorname { W } } } ^ { G } \setminus \operatorname { W } ^ { G }$ is as follows, namely there is a  
(1) 1-di(2) 1-di ensional component ensional component $\overline { { \mathrm { W } } } _ { s l c } ^ { G }$ parametrizing iswhose open locus al p $j$ -invariant rametrizes $\infty$ slc surfaces.rmal surfaces with 2 $\overline { { \mathrm { W } } } _ { L } ^ { G }$ $\overline { { \mathrm { W } } } _ { L , o } ^ { G }$ $L$

Furthermore, the intersection of the two components is the infinity point of both $\mathbb { P } ^ { 1 } s$ parametrizing semistable locus is the unique $j$ -invariant $\overline { { \mathrm { W } } } _ { L } ^ { G }$ $\infty$ , i.e slc surface with two $\overline { { \mathrm { W } } } _ { s l c } ^ { G }$ is part of the GIT-stable locus of $L$ type cusps.
This point is polystable, and the strictly ${ \overline { { \mathrm { W } } } } ^ { G }$ .

A natural question is how the GIT compactification ${ \overline { { \mathrm { W } } } } ^ { G }$ compares to the SBB compactification $\overline { { \mathrm { W } } } ^ { * }$ .
This is the content of [OO18, Theorem 7.9], where we denote $\overline { { \mathbf { W } } } _ { s l c , o } ^ { G } : = \overline { { \mathbf { W } } } _ { s l c } ^ { G } \setminus \overline { { \mathbf { W } } } _ { L } ^ { G }$

2.8. [OO18, Theorem 7.9] The period ma.
Moreover, the above isomorphism identifies $\mathrm { W } ^ { G }  W$ extends to an isomorphismwith the 1-dimensional cusps, $\overline { { \mathrm { W } } } ^ { G } \cong \overline { { \mathrm { W } } } ^ { * }$ $\overline { { \mathrm { W } } } _ { s l c , o } ^ { G } \cup \overline { { \mathrm { W } } } _ { L , o } ^ { G }$ and identifies $\overline { { \mathrm { W } } } _ { s l c } ^ { G } \cap \overline { { \mathrm { W } } } _ { L } ^ { G }$ with the 0-dimensional cusp.

# 3. Moduli of $\mathcal A$ -broken elliptic surfaces and wall-crossing

In this section we review and supplement the results from our previous work on compactifications of the moduli spaces of elliptic surfaces via KSBA stable pairs.

Definition 3.1. A KSBA stable pair $( X , D )$ is a pair consisting of a variety $X$ and a Weil divisor $D$ such that

(1) $( X , D )$ has semi-log canonical (slc) singularities, and (2) $K _ { X } + D$ is an ample $\mathbb { Q }$ -Cartier divisor.

Stable pairs are the natural higher dimensional generalization of stable curves and their moduli space compactifies the moduli space of log canonical models of pairs of log general type.

In [AB21a], we defined KSBA compactifications $\mathcal { E } _ { \mathcal { A } }$ of the moduli space of log canonical (lc) models ( $f : X \to C , S + F _ { \mathcal { A } } )$ of $\mathcal A$ -weighted Weierstrass elliptic surface pairs.
For each admissible weight vector $\mathcal A$ , we obtain a compactification $\mathcal { E } _ { \mathcal { A } }$ , which is representable by a proper DeligneMumford stack of finite type [AB21a, Theorem 1.1 & 1.2].
These spaces parameterize slc pairs ( $f : X \to C , S + F _ { \mathcal { A } } )$ , where $( f : X \to C , S )$ is an slc elliptic surface with section, and $\begin{array} { r } { F _ { \mathcal { A } } = \sum a _ { i } F _ { i } } \end{array}$ is a weighted sum of marked fibers with ${ \mathcal { A } } = ( a _ { 1 } , \ldots , a _ { n } )$ and $0 < a _ { i } \le 1$ , and $( X , S + F _ { { \mathcal { A } } } )$ is a stable pair.

Before stating the main result Theorem 3.6, we must first discuss the different (singular) fiber types that appear in semi-log canonical models of elliptic fibrations as studied in [AB17].

Definition 3.2. Let $( g : Y  C , S ^ { \prime } + a F ^ { \prime } )$ be a Weierstrass elliptic surface pair over the spectrum of a DVR and let $f : X \to C , S + F _ { a } )$ be its relative log canonical model.
We say that $X$ has a(n):

(1) twisted fiber if the special fiber $f ^ { * } ( s )$ is irreducible and $( X , S + E )$ has (semi-)log canonical singularities where $E = f ^ { * } ( s ) ^ { r e d }$ ;  
(2) intermediate fiber if $f ^ { * } ( s )$ is a nodal union of an arithmetic genus zero component $A$ , and a possibly non-reduced arithmetic genus one component supported on a curve $E$ such that the section meets $A$ along the smooth locus of $f ^ { * } ( s )$ and the pair $( X , S + A + E )$ has (semi-)log canonical singularities.

Given an elliptic surface $f : X \to C$ over the spectrum of a DVR such that $X$ has an intermediate fiber, we obtain the Weierstrass model of $X$ by contracting the component $E$ , and we obtain the twisted model by contracting the component $A$ .
As such, the intermediate fiber can be seen to interpolate between the Weierstrass and twisted models.

One can consider a Weierstrass elliptic surface ( $g : Y  C , S ^ { \prime } + a F ^ { \prime } )$ over the spectrum of a DVR, where $F ^ { \prime }$ is either a Kodaira singular fiber type, or $g$ is isotrivial with constant $j$ -invariant $\infty$ with $F ^ { \prime }$ being an $\mathrm { N } _ { k }$ fiber type.
Then the relative log canonical model ( $f : X \to C , S + F _ { a } )$ depends on the value of $a$ .
When $a = 1$ , the fiber is in twisted form, when $a = 0$ the fiber is in Weierstrass form, and for some $0 < a _ { 0 } < 1$ , the fiber enters intermediate form.
The values $a _ { 0 }$ were calculated for all fiber types in [AB21a, Theorem 3.10].

$$
a _ { 0 } = \left\{ \begin{array} { c c } { { 5 / 6 } } & { { \mathrm { I I } } } \\ { { 3 / 4 } } & { { \mathrm { I I I } } } \\ { { 2 / 3 } } & { { \mathrm { I V } } } \\ { { 1 / 2 } } & { { \mathrm { N } _ { 1 } } } \end{array} \right. a _ { 0 } = \left\{ \begin{array} { c c } { { 1 / 6 } } & { { \mathrm { I I } ^ { * } } } \\ { { 1 / 4 } } & { { \mathrm { I I I } ^ { * } } } \\ { { 1 / 3 } } & { { \mathrm { I V } ^ { * } } } \\ { { 1 / 2 } } & { { \mathrm { I } _ { n } ^ { * } } } \end{array} \right.
$$

We now state the definition of pseudoelliptic surfaces which appear as components of surfaces in our moduli spaces, a phenomenon first observed by La Nave [LN02].

Definition 3.3. A pseudoelliptic pair is a surface pair $( Z , F )$ obtained by contracting the section of an irreducible elliptic surface pair ( $f : X \to C , S + F ^ { \prime } )$ .
We call $F$ the marked pseudofibers of $Z$ .
We call ( $f : X \to C , S ,$ the associated elliptic surface to $( Z , F )$ .

The MMP will contract the section of an elliptic surface if it has non-positive intersection with the log canonical divisor of the surface.
There are two types of pseudoelliptic surfaces which appear, and we refer the reader to [AB21a, Definition 4.6, 4.7] for the precise definitions.

Definition 3.4. A pseudoelliptic surface of Type II is formed by the log canonical contraction of a section of an elliptic component attached along twisted or stable fibers.

Definition 3.5. A pseudoelliptic surface of Type I appear in pseudoelliptic trees attached by gluing an irreducible pseudofiber $G _ { 0 }$ on the root component to an arithmetic genus one component $E$ of an intermediate (pseudo)fiber of an elliptic or pseudoelliptic component.

Figure 2 has a tree of pseudoelliptic surfaces of Type I circled on the right, with a pseudoelliptic of Type II circled on the left.

Theorem 3.6. [AB21a, Theorem 1.6] The boundary of the proper moduli space $\mathcal { E } _ { v , \mathcal { A } }$ parametrizes $\mathcal { A }$ -broken stable elliptic surfaces, which are pairs ( $f : X  C , S + F _ { \mathcal { A } } )$ ) consisting of a stable pair $( X , S + F _ { { \mathcal { A } } } )$ with a map to a nodal curve $C$ such that:

• $X$ is an slc union of elliptic surfaces with section $S$ and marked fibers, as well as • chains of pseudoelliptic surfaces of type $I$ and $I I$ (Definition 3.3) contracted by $f$ with marked pseudofibers.

![](images/d76eb4bca0a1e240cfad538a5fd6a2dd157dbdae77a17b2c001e2ff19f9a1469.jpg)  
Figure 2. An $\mathcal A$ -broken elliptic surface.
Two types of pseudoelliptic surfaces (see Definitions 3.4 and 3.5) circled.
Left: Type II and Right: Type I.

Contracting the section of a component to form a pseudoelliptic component corresponds to stabilizing the base curve as an $\mathcal { A }$ -stable curve in the sense of Hassett (see [AB17, Corollaries 6.7 & 6.8]).
In particular we have the following.

Theorem 3.7. [AB21a, Theorem 1.4] There are forgetful morphisms $\mathcal { E } _ { v , \mathcal { A } } \to \overline { { \mathcal { M } } } _ { g , \mathcal { A } }$

Remark 3.8. For an irreducible component with base curve $\mathbb { P } ^ { 1 }$ and $\deg \mathcal { L } > 0$ , contracting the section of an elliptic component may not be the final step in the MMP – we may need to contract the entire pseudoelliptic component to a curve or a point (see [AB17, Proposition 7.4]).

3.0.1. Wall and chamber structure.
We are now ready to discuss how the moduli spaces $\mathcal { E } _ { \mathcal { A } }$ change as we vary $\mathcal { A }$ .
There are three types of walls in our wall and chamber decomposition.

# Definition 3.9.

(I) A wall of Type W $^ { 1 }$ is a wall arising from the log canonical transformations, i.e. the walls where the fibers of the relative log canonical model transition between fiber types.  
(II) A wall of Type WII is a wall at which the morphism induced by the log canonical contracts the section of some components.  
(III) A wall of Type WIII is a wall where the morphism induced by the log canonical contracts an entire rational pseudoelliptic component (see Remark 3.8).

# Remark 3.10.

(1) The walls of Type WII are precisely the walls of Hassett’s wall and chamber decomposition [Has03] (see discussion preceding Theorem 3.7).  
(2) There are finitely many walls (see [AB21a, Theorem 6.3]).

Theorem 3.11. [AB21a, Theorem 1.5] Le $\ u ^ { \prime } \mathcal { A } , \mathcal { B } \in \mathbb { Q } ^ { r }$ be weight vectors with $0 < \mathcal { A } \leq \mathcal { B } \leq 1$ .
Then

(1) If A and $\mathcal { B }$ are in the same chamber, then the moduli spaces and universal families are isomorphic.  
(2) If ${ \mathcal { A } } \leq { \mathcal { B } }$ then there are reduction morphisms $\mathcal { E } _ { v , \mathcal { B } } \to \mathcal { E } _ { v , \mathcal { A } }$ on moduli spaces which are compatible with the reduction morphisms on the Hassett spaces:  
(3) The universal families are related by a sequence of explicit divisorial contractions and flips More precisely, across WI and WIII walls there is a divisorial contraction of the universal family and across a WII wall the universal family undergoes a log flip.

Remark 3.12. For more on Theorem 3.11 (3), we refer the reader to [AB21a, Section 8].
La Nave (see [LN02, Section 4.3, Theorem 7.1.2]) noticed that the contraction of the section of a component is a log flipping contraction inside the total space of a one parameter degeneration.
In particular, the Type I pseudoelliptic surfaces are thus attached along the reduced component of an intermediate (pseudo)fiber (see [AB21a, Figure 13]).

3.1. Strictly (semi-)log canonical Weierstrass models.
In order to understand the stable pair degenerations of log canonical models of Weierstrass elliptic surfaces, we need to understand strictly log canonical and semi-log canonical Weierstrass fibrations.
We collect some results in this direction here, beginning with the definition of a type L singular fiber.

Definition 3.13. (see [LN02, Section 3.3]) Let $f : X \to C$ be a Weierstrass fibration with smooth generic fiber and Weierstrass data $( A , B )$ .
If $1 2 = \operatorname* { m i n } ( 3 v _ { q } ( A ) , 2 v _ { q } ( B ) )$ where $v _ { q }$ denotes the order of vanishing at a point $q \in \mathbb { P } ^ { 1 }$ we say that $f$ has a type $\mathbf { L }$ fiber at $q$ .

Lemma 3.14. If $F$ is a type $L$ cusp of $X$ then $X$ has strictly log canonical singularities in a neighborhood of $F ^ { \prime }$ and the log canonical threshold $\operatorname* { l c t } ( X , 0 , F ) = 0$ .

Proof.
After performing a weighted blowup $\mu : Y \to X$ at the cuspidal point of $F$ , we get an exceptional divisor $E$ a possibly nodal elliptic curve and strict transform $A : = \mu _ { * } ^ { - 1 } ( F )$ a rational curve meeting $E$ transversely.
Writing $\mu ^ { * } K _ { X } = K _ { Y } + a E$ , it follows from the projection formula that $K _ { Y } . E + a E ^ { 2 } = 0$ .
On the other hand, $K _ { Y } . E + E ^ { 2 } = K _ { E } = 0$ by the adjunction formula and $E ^ { 2 } \neq 0$ since it is exceptional.
Therefore $a = 1$ so $X$ has a strictly log canonical singularity at the cuspidal point of $F$ and the discrepancy of $( X , \epsilon F )$ for any $\epsilon > 0$ will be strictly greater than 1. $\boxed { \begin{array} { r l } \end{array} }$

Remark 3.15. The type L cusp decreases the self intersection $S ^ { 2 }$ by $_ 1$ , and thus increases $\deg \mathcal { L }$ by 1 (see [LN02, Remark 5.3.8]).

We now discuss some facts on non-normal Weierstrass fibrations with generic fiber a nodal elliptic curve.
These appear as semi-log canonical degenerations of normal elliptic surfaces and as isotrival $j$ -invariant $\infty$ components of broken elliptic surfaces.

We first recall the definition of the fiber types N $k$ that these fibrations possess ([AB17, Section 5] and [LN02, Lemma 3.2.2]).

Definition 3.16. The fibers N $\boldsymbol { k }$ are the fiber types with Weierstrass equation $y ^ { 2 } = x ^ { 2 } ( x - t ^ { k } )$ .

Lemma 3.17. [LN02, Lemma 3.2.2] Fibers of type N $k$ are slc if and only if $k \in \{ 0 , 1 , 2 \}$

# Remark 3.18.

(1) The general fiber of an isotrivial $j$ -invariant $\infty$ fibration is type N $_ 0$ (2) N $^ 2$ is the $j$ -invariant $\infty$ version of the L cusp (see Remark 3.19).

Remark 3.19. The N $^ 2$ fiber behaves analogously to the type L fiber.
Indeed by the proof of [AB17, Lemma 5.1], on the normalization $( X ^ { \nu } , D )$ of a surface $X$ with an N $^ 2$ fiber, the double locus $D$ consists of a nodal curve with node lying over the cuspidal point of the N $^ 2$ fiber, and $X ^ { \nu }$ is smooth in a neighborhood of this point.
In particular, $( X ^ { \nu } , D )$ has log canonical singularities in a neighborhood of the nodal point of $D$ and $\operatorname* { l c t } ( X ^ { \nu } , D , A ) = 0$ for any curve $A$ passing through this point.
Therefore by definition of semi-log canonical, $X$ has strictly semi-log canonical singularities in a neighborhood of the N fiber $F$ and $\mathrm { s l c t } ( X , 0 , F ) = 0$ .  
$^ 2$

The local equation given above for a type $\mathrm { N } _ { k }$ fiber is not a standard Weierstrass equation.
One can check that the standard equation of an N $k$ fiber is given by

$$
y ^ { 2 } = x ^ { 3 } - \frac { 1 } { 3 } t ^ { 2 k } x + \frac { 2 } { 2 7 } t ^ { 3 k } .
$$

Proposition 3.20. If $a _ { k }$ type N $\kappa$ fibers, then $( f : X \to C , S )$ $\begin{array} { r } { - S ^ { 2 } = \deg ( \mathcal { L } ) = \sum _ { k } a _ { k } \frac { k } { 2 } } \end{array}$ is an isotrivial .
$j$ -invariant $\infty$ slc Weierstrass fibration with

Proof.
Let $A$ and $B$ the Weierstrass data of $( f : X \to C , S )$ .
If $q \in C$ lies under an $\mathrm { N } _ { k }$ fiber, then $A$ vanishes to order $2 k$ and $B$ to order $3 k$ at $q$ .
Then $A , B$ have degree $\sum 2 k a _ { k }$ and $\sum 3 k a _ { k }$ respectively.
The result follows since the degree of $A$ and $B$ are $4 \deg \mathcal { L }$ and $6 \deg \mathcal { L }$ respectively.


Note that for $k$ even, the N $\boldsymbol { k }$ fiber has trivial monodromy and for $k$ odd it has $\mu _ { 2 }$ monodromy.
This determines the twisted models of these fibers.

Corollary 3.21. Let $F$ be an N $k$ fiber.
Then the twisted model of $F$ is an $\mathrm { N } _ { 0 }$ (respectively twisted N $\bot$ ) if $k$ is even (respectively odd).

Proof.
By the local analysis of [AB19, Section 6.2], in the even case the twisted model must be stable since there is no base change required, and the odd case there is a $\mu _ { 2 }$ base change so the twisted model is a nodal cubic curve modulo the $\mu _ { 2 }$ action, i.e. a twisted N $^ 2$ .


Thus given an $\mathrm { N } _ { k }$ fiber, we can cut it out and glue in an $\mathrm { N } _ { k + 2 }$ fiber since the families are isomorphic to $\mathrm { N } _ { 0 }$ (respectively N $^ { 1 }$ ) families over a punctured neighborhood.
We can ask how this surgery affects $- S ^ { 2 } = \deg { \mathcal { L } }$ .

Corollary 3.22. Let $f : X \to C , S )$ be an isotrivial $j$ -invariant $\infty$ Weierstrass fibration and let $f : X ^ { \prime } \to C , S ^ { \prime } )$ be the result of replacing an $\mathrm { N } _ { k }$ fiber by an $\mathrm { N } _ { k + 2 }$ fiber.
Then $- ( S ^ { \prime } ) ^ { 2 } = - S ^ { 2 } + 1$ .

3.2. Elliptic fibrations via twisted stable maps.
In [AB19] we used the theory of twisted stable maps, originally developed by Abramovich-Vistoli (see [AV97, AV02]) to understand limits of families of elliptic fibrations.
The basic idea is that an elliptic surface $f : X \to C$ gives an a priori rational map $C \mathrm { ~ -- } \partial \overline { { \mathcal { M } } } _ { 1 , 1 }$ which extends to a morphism $\mathcal { C } \mathrm { ~ --  ~ } \overline { { \mathcal { M } } } _ { 1 , 1 }$ from an orbifold curve $\mathcal { C }$ with coarse moduli space $C$ .
Now we understand limits of a family of elliptic surfaces by computing limits of the corresponding family of such maps.
The twisted stable limits serve the same purpose for elliptic fibrations that Kulikov models serve for K3 surfaces, i.e. they form the starting point from which applying the MMP yields the stable limit.

3.2.1. Twisted stable maps limits.
We now recall structure of the limiting surfaces obtained using the twisted stable maps construction.
As we will be studying slc degenerations of surfaces, the surfaces themselves will degenerate into possibly reducible surfaces.
The degenerate surfaces will carry a fibration over a nodal curve whose $j$ -map is the limit of the $j$ -map of the degenerating family.
Furthermore, there is a balancing condition on the stabilizers of the orbicurve C over nodes which implies the action on the tangent spaces of the two branches at a node must be dual (see [AV97, Definition 3.2.4] and [Ols07]).
Finally, the stabilizers of a twisted stable map are concentrated either over nodes or at marked gerbes contained in the smooth locus.
In particular, the limit of a map from a smooth schematic curve $C$ can only have stabilizers over the nodes.

These observations motivate the following necessary conditions for a twisted surface to appear as a limit of a family of degenerating elliptic surfaces.
We consider the case where the degenerating family of elliptic surfaces has $1 2 d \mathrm { I } _ { 1 }$ marked singular fibers where $d = \deg \mathcal { L }$ as this is the generic situation and the relevant one for the present paper.
This corresponds to the moduli map $C  \overline { { \mathcal { M } } } _ { 1 , 1 }$ extending to a morphism on all of $C$ such that the $j$ -map $C  \overline { { M } } _ { 1 , 1 } \cong \mathbb { P } ^ { 1 }$ has degree $1 2 d$ , and is unramified over $\infty$ .

Proposition 3.23. Suppose $f : X \to C , S + F )$ is a twisted elliptic surface [AB19] over a rational curve which is the limit of a degenerating family of smooth elliptic surfaces with $1 2 d \mathrm { I } _ { 1 }$ and arbitrary marked fibers.
Then the following hold.

(1) If $X$ is reducible, its irreducible components are either attached along nodal fibers, or in the following pairs of twisted fibers: $\mathrm { I } _ { a } ^ { * } / \mathrm { I } _ { b } ^ { * } / \mathrm { N } _ { 1 }$ , II/II $^ *$ , III/III $^ *$ or IV/IV $^ *$ .  
(2) The total degree of the $j$ -map $C  \overline { { M } } _ { 1 , 1 }$ is $1 2 d$ .  
(3) Away from the singular locus of $C$ , the fibers of $f$ are at worst nodal.
In particular, every marked fiber in $\textstyle F = \sum _ { i = 1 } ^ { n } F _ { i }$ is an $I _ { a }$ fiber for some $a \geq 0$ .

The surfaces of Proposition 3.23 correspond to genus 0 balanced twisted stable maps to $\overline { { \mathcal { M } } } _ { 1 , 1 }$ of degree $1 2 d$ which are parametrized by the space $\mathcal { K } _ { 0 , n } ( \overline { { \mathcal { M } } } _ { 1 , 1 } , 1 2 d ) ( \underline { { 0 } } )$ .
Here $\underline { { 0 } }$ is the tuple of $n$ zeroes denoting the fact that the marked points have trivial stabilizer.

Theorem 3.24. [AB21b, Theorem 5.5] Each point $( f : \mathcal { C } \to \overline { { \mathcal { M } } } _ { 1 , 1 } , p _ { 1 } , \dotsc , p _ { n } ) ] \in \mathcal { K } _ { 0 , n } ( \overline { { \mathfrak { M } } } _ { 1 , 1 } , 1 2 d ) ( \underline { { 0 } } )$ admits a smoothing to a map from a non-singular $n$ -pointed schematic rational curve.

Corollary 3.25. A twisted elliptic surface admits a smoothing to a generic $1 2 d \mathrm { I } _ { 1 }$ elliptic surface if and only if it satisfies the conditions of Proposition 3.23.

3.2.2. Relative twisted stable maps.
One of the primary moduli spaces of interest from the perspective of stable pairs is the closure of the locus where the marked fibers are exactly the $1 2 d \mathrm { I } _ { 1 }$ fibers.
These fibers lie above the preimages of $\infty \in \overline { { \mathcal { M } } } _ { 1 , 1 }$ under the $j$ -invariant map $C  \overline { { \mathcal { M } } } _ { 1 , 1 }$ and thus we are concerned with the closure $\mathcal { K } _ { \infty } \subset \mathcal { K } _ { 0 , 2 4 } ( \overline { { \mathcal { M } } } _ { 1 , 1 } , 2 4 )$ of the locus parametrizing maps from a smooth rational curve which are unramified over $\infty$ and such that all marked fibers map to $\infty$ .
Equivalently, this locus is the space of maps relative to the divisor $\left[ \infty \right]$ with multiplicities $( 1 , \ldots , 1 )$ .
The closure of such loci has been studied in the Gromov-Witten literature under the name of relative stable maps (see e.g. [Vak00], [Gat02], and [Cad07]).
In [AB21b], we consider the question of determining the points of this locus for twisted stable maps to stacky curves.
The conditions characterizing this locus [AB21b, Conditions $( * ) ]$ can be phrased as follows in the context of elliptic fibrations.

Proposition 3.26. Suppose ( $f : X \to C , S + F )$ is a twisted elliptic surface over a rational curve which is the limit of a degenerating family of $1 2 d \mathrm { { I } _ { 1 } }$ elliptic surfaces with marked singular fibers.
Then the following hold in addition to the conditions of Proposition 3.23.

(1) $F ^ { \prime }$ consists of 12d nodal singular fibers.

(2) Every fiber with $j = \infty$ which is not on an isotrivial component is marked.  
(3) For each maximal connected tree $T$ of isotrivial $j = \infty$ components $X$ , the number of marked fibers contained on $T$ is equal to the sum of the multiplicities of the twisted fibers of the non-isotrivial components along which $T$ is attached.

Remark 3.27. The last condition says e.g. that if an isotrivial $j$ -invariant $\infty$ component is attached to an $\mathbf { l } _ { n }$ fiber, there must be $n$ markings on that component, since an $\mathrm { I } _ { n }$ fiber is produced when $n$ marked $\mathbf { l } _ { 1 }$ fibers collide.

Theorem 3.28. [AB21b, Theorems 1.7 & 1.8] The conditions of Proposition 3.26 characterize the boundary of $\mathcal { K } _ { \infty }$ .
In particular, any twisted surface satisfying these conditions is the limit of $a$ family of smooth $1 2 d \mathrm { I } _ { 1 }$ elliptically fibered surface with marked singular fibers.

Remark 3.29. After determining the shape of a twisted stable maps limits, we will use wall-crossing to compute the limits as one reduces weights.

# 4. Moduli of weighted stable elliptic K3 surfaces

In this section, we specialize the discussion of Section 3 to the case of elliptic K3 surfaces and define the various compactifications of the stack $\mathcal { W }$ of elliptic K3 surfaces, and its coarse space $W$ , which we study in this paper.
The goal is to obtain an explicit description of the compactifications for various choices of weights $\mathcal { A }$ .
In particular, we will explicitly describe the surfaces parametrized by the boundary of $\mathcal { E } _ { \mathcal { A } }$ in this case as well as understand the wall-crossing morphisms.

From now on we assume that $g ( C ) = 0$ and $\deg \mathcal { L } = 2$ so that $C \cong \mathbb { P } ^ { 1 }$ and $\mathcal { L } = \mathcal { O } _ { \mathbb { P } ^ { 1 } } ( 2 )$ and $( f : X \to C , S )$ is an elliptic K3 surface with section.

Definition 4.1. Let $\overline { { \mathscr { W } } } ( A )$ be the closure in $\mathcal { E } _ { \mathcal { A } }$ of the locus of pairs ( $f : X \to C , S + F _ { { \mathcal { A } } } )$ where $X$ is an elliptic K3 surface and $\operatorname { S u p p } ( F _ { \mathcal { A } } )$ consists of $2 4 ~ \mathrm { { I } _ { 1 } }$ singular fibers.

Definition 4.2. If ${ \mathcal { A } } = ( a , \ldots , a )$ is the constant weight vector, then $S _ { 2 4 }$ acts on $\overline { { \mathscr { W } } } ( A )$ by permuting the marked fibers, and we denote the quotient by $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ .

Proposition 4.3. ${ \mathcal { W } } ( { \mathcal { A } } )$ and $\mathscr { W } _ { \sigma } ( a )$ are proper Deligne-Mumford stacks.
Moreover, the coarse space $W _ { \sigma } ( a )$ of $\mathscr { W } _ { \sigma } ( a )$ is a modular compactifications of $W$ for each $0 < a \le 1$ .

Proof.
The fact that they are proper Deligne-Mumford stacks follows from [AB21a].
By construction, $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ has an open set parametrizing elliptic K3s with 24I $^ { 1 }$ fibers.
Recall that $W$ parametrizes lattice polarized K3 surfaces, and such a lattice polarization is equivalent to the structure of an elliptic fibration with chosen section.
The result follows by the observation that a generic elliptically fibered K3 surface has $2 4 \mathrm { { I } _ { 1 } }$ fibers.


Brunyate constructs a compactification $\overline { { \mathcal { B } } }$ of the space of elliptic K3 surface by studying degenerations of pairs $( X , \epsilon _ { 1 } S + F _ { \mathcal { B } } )$ where $\mathcal { B } = ( \epsilon , \dots , \epsilon )$ , i.e. with small weight on both the section and the fibers (in particular, Brunyate requires $\epsilon _ { 1 } \ll \epsilon$ ), so that $\operatorname { S u p p } ( F _ { \mathbb { B } } )$ is the closure of the rational curves on $X$ [Bru15] (see also [ABE20, Section 7]).
In fact there is a morphism $\overline { { \mathcal { B } } } ^ { \nu } \to \overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ , given by increasing the weight on the section to 1.

Proposition 4.4. There is a morphism $\overline { { \mathcal { B } } } ^ { \nu } \to \overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ for $\epsilon \ll 1$ .

Proof.
Consider a 1-parameter degeneration of pairs $( X , \epsilon S + F _ { \mathcal { B } } )$ inside $\overline { { \mathcal { B } } }$ .
We may choose a generic choice of smooth fibers $G = \cup _ { i \in I } G _ { i }$ to mark so that the pair $( X , S + F _ { \mathcal { B } } + G )$ is stable, where the section has coefficient 1. By the results of [AB21a], there is a sequence of flips and contractions as one reduces the coefficients of $G$ from 1 to 0. The resulting stable limit in $\overline { { \boldsymbol { \mathcal { W } } } } _ { \sigma } ( \epsilon )$ only depends on the point $( X _ { 0 } , \epsilon { \cal S } _ { 0 } + ( { \cal F } _ { \mathcal { B } } ) _ { 0 } )$ in $\overline { { \mathcal { B } } }$ and not on the family or choice of auxiliary markings.
Therefore we obtain the desired morphism by [GG14, Theorem 7.3].


Remark 4.5. Comparing Theorem 6.13 with [Bru15, Theorem 9.1.4] (see also [ABE20, Section 7]), we see that there is a bijection between the boundary strata of $\mathcal { B }$ and $\mathcal { W } _ { \sigma } ( \epsilon ) = \mathcal { W } ( \mathcal { B } ) / S _ { 2 4 }$ .
For example, the third case in [Bru15, Theorem 9.1.4] maps to case (E) of Theorem 6.13 if there are no $\mathbb { F } _ { 0 }$ components, and to either type (D) or (F) depending on the parity of the number of components if there are $\mathbb { F } _ { 0 }$ components.

Corollary 4.6. The morphism from Proposition 4.4 is an isomorphism.

Proof.
It is a proper birational set-theoretic bijection between normal spaces.

Remark 4.7. It follows from Corollary 4.6 that there is in fact a morphism $\overline { { \mathscr { W } } } _ { \sigma } ( \epsilon )  \overline { { \mathscr { B } } }$ which can be thought of as induced by decreasing weights on the section.

Definition 4.8. Let $\overline { { \mathcal { K } } } _ { \epsilon }$ denote stable pairs compactification of the space parametrizing pairs with only one singular fiber marked with weight $0 < \epsilon \ll 1$ , and let $\overline { { \mathrm { K } } } _ { \epsilon }$ be its coarse moduli space.

Next, we define the moduli space $\overline { { \mathcal { F } } } _ { \epsilon }$ which is like $\overline { { \mathcal { K } } } _ { \epsilon }$ , only we allow any fiber to be marked.

Definition 4.9. Let $\overline { { \mathcal { F } } } _ { \epsilon }$ be the closure in $\mathcal { E } _ { \mathcal { A } }$ of the locus of pairs ( $f : X  C , S + \epsilon F )$ where $f$ has precisely $2 4 ~ \mathrm { { I } _ { 1 } }$ fibers, $0 < \epsilon \ll 1$ , and $F$ is any fiber.

Remark 4.10. At this point we have introduced many compactifications (see Figure 1):

• ${ \mathcal { W } } ( { \mathcal { A } } )$ : Stable pair compactification with $\mathcal { A }$ -weighted singular fibers.  
• $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ : When ${ \mathcal { A } } = ( a , \ldots , a )$ , we can quotient by S $2 4$ .  
• $\overline { { \mathcal { K } } } _ { \epsilon }$ : Stable pairs compactification with a single $\epsilon$ -marked singular fiber.  
• $\overline { { \mathcal { F } } } _ { \epsilon }$ : Stable pairs compactification with any fiber marked by $\epsilon$ .  
• $\overline { { \mathrm { W } } } ^ { * }$ : SBB compactification of the period domain moduli space $W$ .

We now give a brief overview of how they are related (again, see Figure 1).

(1) There are 24 generically finite morphisms $\overline { { \mathcal { W } } } ( \mathcal { A } )  \overline { { \mathcal { K } } } _ { \epsilon }$ of degree 23!, corresponding to a forgetting all but one marked singular fiber.  
(2) There is a degree 24 generically finite rational map $\mathcal { K } _ { \epsilon } \mathrm { ~ -- } \partial \overline { { \mathrm { W } } } _ { \sigma } ( \epsilon )$ corresponding to choosing a singular fiber.  
(3) We will see that there are morphisms $\overline { { \mathrm { W } } } _ { \sigma } ( \epsilon )  \overline { { \mathrm { W } } } ^ { * }$ and $\overline { { \mathrm { K } } } _ { \epsilon }  \overline { { \mathrm { W } } } ^ { * }$ (see Theorems 6.15 and 8.2 resp.).  
(4) We will see in Section 8.3 that the moduli space $\overline { { \mathcal { F } } } _ { \epsilon }$ is a smooth Deligne-Mumford stack whose coarse space is an (explicit) GIT quotient.
Furthermore, there is a morphism $\overline { { \mathcal { F } } } _ { \epsilon }  \overline { { \mathrm { W } } } ^ { * }$ (see Theorem 8.8) which is generically a $\mathbb { P } ^ { 1 }$ bundle.

We end this section with an important proposition.

Proposition 4.11. For any surface $X$ parametrized by $\overline { { \mathscr { W } } } ( A )$ (for any $\mathcal A$ ) or $\overline { { \mathcal { F } } } _ { \epsilon }$ (in particular $\overline { { \mathcal { K } } } _ { \epsilon }$ ), we have that $\mathrm { H } ^ { 1 } ( X , { \mathcal { O } } _ { X } ) = 0$ .

Proof.
Since slc singularities are Du Bois (see [KK10] and [Kol13, Corollary 6.32]), $X$ has Du Bois singularities.
Then $\mathrm { H } ^ { 1 } ( X , { \mathcal { O } } _ { X } ) = 0$ since $\mathrm { H } ^ { \ i } ( X _ { b } , \mathcal { O } _ { X _ { b } } )$ is constant in any flat family of varieties with Du Bois singularities (see [KK10, Corollary 1.2]), and any $X$ arises as the special fiber of a flat family whose general fiber is a surface $X _ { \eta }$ with $\mathrm { H } ^ { 1 } ( X _ { \eta } , { \mathcal { O } } _ { X _ { \eta } } ) = 0$ .


Remark 4.12. We will see in Theorem 8.1 that the surfaces on the boundary of $\overline { { \mathcal { F } } } _ { \epsilon }$ (and thus also $\overline { { \mathcal { K } } } _ { \epsilon }$ ) satisfy that $\omega _ { X } \cong { \mathfrak { O } } _ { X }$ .
Moreover, if $F$ is the marked fiber, then $2 F$ is an ample Cartier divisor such that $( 2 F ) ^ { 2 } = 2$ .
Then following [AET19, Definition 3.4, Proposition 3.8, and Theorem 3.11], we see that $\overline { { \mathcal { F } } } _ { \epsilon }$ and $\overline { { \mathcal { K } } } _ { \epsilon }$ are proper Deligne-Mumford stacks representing a functor over arbitrary base schemes.
Due to subtleties with defining moduli spaces in higher dimensions, the remaining spaces follow the formalism developed in [AB21a] and thus correspond to Deligne-Mumford stacks representing functors only over normal base schemes (see [AB21a, Section 2.2.2] for more details).

4.1. Isotrivial $j$ -invariant $\infty$ fibrations.
Here we prove some preliminary results on isotrivial $j$ -invariant $\infty$ elliptic fibrations of K3 type which appear in the boundary of the various moduli spaces described above.
We begin by bounding the number of N $\textit { \textbf { \ i } }$ fibers (Definition 3.16) which can appear on an slc elliptic K3.

Proposition 4.13. Let ( $f : X \to \mathbb { P } ^ { 1 } , S )$ be an isotrivial $j = \infty$ slc Weierstrass fibration of $K \mathcal { 3 }$ type.  
Then $X$ has one of the following configurations of cuspidal fibers: $\left( 1 \right) 4 \mathrm { N } _ { 1 } , \left( 2 \right) 2 \mathrm { N } _ { 1 } \mathrm { N } _ { 2 }$ , or (3) 2N $^ 2$ .

Proof.
We must have only $\mathrm { N } _ { 0 } , \mathrm { N } _ { 1 }$ and N $^ 2$ by the slc assumption so by Proposition 3.20, $2 = a _ { 1 } / 2 + a _ { 2 }$ which only admits the non-negative integer solutions $( a _ { 1 } , a _ { 2 } ) = ( 4 , 0 ) , ( 2 , 1 )$ and $( 0 , 2 )$ .


Remark 4.14. Up to automorphisms of $\mathbb { P } ^ { 1 }$ , the global Weierstrass equation for the surfaces in Proposition 4.13 can be written as follows:

$$
\begin{array} { r l } & { y ^ { 2 } = x ^ { 3 } - \frac { 1 } { 3 } t ^ { 2 } s ^ { 2 } ( t - s ) ^ { 2 } ( t - \lambda s ) ^ { 2 } x + \frac { 2 } { 2 7 } t ^ { 3 } s ^ { 3 } ( t - s ) ^ { 3 } ( t - \lambda s ) ^ { 3 } , \lambda \in \mathbb { P } ^ { 1 } \setminus \{ 0 , 1 , \infty \} , } \\ & { y _ { \circ } ^ { 2 } = x ^ { 3 } - \frac { 1 } { 3 } t ^ { 2 } s ^ { 2 } ( t - s ) ^ { 4 } x + \frac { 2 } { 2 7 } t ^ { 3 } s ^ { 3 } ( t - s ) ^ { 6 } , } \end{array}
$$

In particular, up to isomorphism there is a unique surface with configuration (2) and (3).

Finally, we need the following key proposition.

Proposition 4.15. Suppose $( f _ { 0 } : X \to \mathbb { P } ^ { 1 } , S )$ is an isotrivial $j = \infty$ slc Weierstrass fibration of $K \mathcal { 3 }$ type and $F \subset X$ is an $\mathrm { N } _ { k }$ fiber.
If $f _ { 0 }$ is the central fiber of a 1-parameter family of Weierstrass models $f : \mathcal { X } \to \mathcal { C } , \mathcal { S } ) \to B$ with generic fiber $f _ { \eta } : \mathcal { X } _ { \eta } \to C _ { \eta } , \mathcal { S } _ { \eta } )$ $a$ $2 4 \mathrm { { I } _ { 1 } }$ elliptic fibration, then there are at least $k + 1$ type $\mathrm { I } _ { 1 }$ fibers of $f _ { \eta }$ that limit to the $\mathrm { N } _ { k }$ fiber $F$ for $k = 1 , 2 , 3 , 4$ .

Proof.
Consider the twisted stable maps limit of $f _ { \eta }$ .
By Proposition 3.23 (1), the Weierstrass N $^ { 1 }$ fiber $F ^ { \prime }$ must be replaced by a surface component $Y$ attached along the twisted model of $F$ by a twisted fiber of type $\mathrm { I } ^ { * }$ (resp.
I) if $k$ is odd (resp.
even).
By Proposition 4.13, the possibilities for $X$ are $4 \mathrm { N } _ { 1 }$ , 2N1N $^ 2$ , $\mathrm { 2 N _ { 2 } }$ as well as the non-slc cases $\mathrm { N _ { 1 } N _ { 3 } }$ and $\mathrm { N _ { 4 } }$ .
Since the degree of the $j$ -map is constant for a family of twisted stable maps, the sum of degrees of the $j$ -map of the components of the twisted model is 24. This means that $Y$ is rational when $k = 1 , 2$ or K3 when $k = 3 , 4$ .
The number of $\mathrm { I _ { 1 } }$ fibers of $f _ { \eta }$ limiting to the $\mathrm { N _ { 1 } }$ fiber $F$ of $f _ { 0 }$ is the same as the number of $\mathrm { I } _ { 1 }$ fibers limiting to the component $Y$ in the twisted model.
By conditions (2) and (3) in loc.
cit., the component $Y$ cannot be isotrivial and $\deg ( \mathcal { L } ) \geq 1$ .
By Persson’s classification [Per90], a rational elliptic surface $Y$ with an $\mathrm { I } ^ { * }$ fiber has $\geq 2 \mathrm { { I } _ { 1 } }$ fibers, and one with an $\mathrm { I } _ { n }$ has $\geq 3$ other $\mathrm { I _ { 1 } }$ fibers counted with multiplicity.
Similarly, by [Shi03, Theorem 1.1 and 1.2], an elliptic K3 surface with an $\mathrm { I } ^ { * }$ fiber has $\geq 4 1 _ { 1 }$ fibers, and one with an $I _ { n }$ fiber has $\geq 5$ other $\mathrm { I } _ { 1 }$ fibers counted with multiplicity.
$\boxed { \begin{array} { r l } \end{array} }$

# 5. Wall crossings inside $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ for $\begin{array} { r } { a > \frac { 1 } { 1 2 } } \end{array}$

Recall that $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ denotes the space where all singular fibers are marked with weight $a$ and we have taken the $S _ { 2 4 }$ quotient.
The main goal of this section (see Section 5.1) is to describe the surfaces parametrized by $\overline { { \mathscr { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ for $0 < \epsilon \ll 1$ .
In particular, we explicitly describe the wall crossings that happen as we vary the weight vector from $a = 1$ to $a = 1 / 1 2 + \epsilon$ .

By Corollary 5.6 we see that surfaces parametrized by $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ have at most two elliptically fibered components, but possibly with trees of pseudoelliptic surfaces attached to them.
In Proposition 5.15 we classify the possible surfaces parametrized by $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ with a single normal elliptically fibered component.
In Theorem 5.16 we classify the possible surfaces parametrized by $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ with a single non-normal elliptically fibered component.
In Theorem 5.19, we classify the possible surfaces parametrized by $\mathscr { W } _ { \sigma } ( a )$ with two elliptically fibered components.
Finally, in Proposition 5.18 and Proposition 5.20, we show that surfaces of each type appearing in the aforementioned results do exist on the boundary of $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ .

Lemma 5.1. There are Type WII walls where Type I pseudoelliptic surfaces form at $\textstyle a = { \frac { 1 } { k } }$ for $k = 1 , \ldots , 1 1$ .

Proof.
Recall that Type I pseudoelliptic surfaces form when a component of the underlying weighted curve is contracted – this occurs when $k a = 1$ .
Finally, note that $2 4 a > 2$ for each of these values of $k$ so that the moduli space is nontrivial.


Lemma 5.2. There are Type WIII walls at $\begin{array} { r } { a = \frac { 5 } { 1 2 } , \frac { 3 } { 1 2 } } \end{array}$ , and $\frac { 2 } { 1 2 }$ where rational pseudoelliptic surfaces

Proof.
This follows from [AB21a, Theorem 6.3] as well as the observation that that a rational elliptic surface attached to a type II, III or IV fiber must have a $\mathrm { I I ^ { * } , I I I ^ { * } }$ , or IV∗ fiber respectively and so it has $2 , 3$ , or 4 other marked fibers counted with multiplicity.


Since the above walls are all above $\frac { 1 } { 1 2 }$ , we obtain the following:

Corollary 5.3. Any type II, III and IV fiber on a surface parametrized by $\overline { { \mathcal { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ is a Weierstrass fiber.
In particular, there are no pseudoelliptic trees sprouting off of it.

In a similar vein we have the following two lemmas:

Lemma 5.4. There are Type WIII walls at $a = { \textstyle { \frac { 1 } { 4 } } } , { \textstyle { \frac { 1 } { 6 } } } , { \textstyle { \frac { 1 } { 8 } } }$ , and $\frac { 1 } { 1 0 }$ , where: (1) rational pseudoelliptic surfaces attached along intermediate type $\mathrm { N _ { 1 } }$ fibers contract onto a point; (2) isotrivial $j$ -invariant $\infty$ surfaces with $\deg \mathcal { L } = 1$ attached along intermediate type N $^ { 1 }$ fibers contract onto a point.

Proof.
A rational elliptic surface attached along an N $^ { 1 }$ fiber must have an $\mathrm { I } _ { k } ^ { * }$ fiber in the double locus.
Since an $\mathrm { I } _ { k } ^ { * }$ has discriminant $6 + k$ , then there are $6 - k$ markings counted with multiplicity on the rational pseudoelliptic.
By the classification in [Per90], there exist rational elliptic surfaces with $\mathrm { I } _ { k } ^ { * }$ for $0 \leq k \leq 4$ .
Since the log canonical threshold of an intermediate $\mathrm { N _ { 1 } }$ fiber is $\frac { 1 } { 2 }$ , then the surfaces with $\mathrm { N } _ { 1 } / \mathrm { I } _ { k } ^ { \ast }$ double locus contract at $\frac { 1 } { 2 ( 6 - k ) }$ .
These give walls above $\textstyle { \frac { 1 } { 1 2 } }$ for $1 \leq k \leq 4$ Similarly, isotrivial $j$ -invariant $\infty$ surfaces with an $\mathrm { N _ { 1 } }$ fiber and $\deg \mathcal { L } = 1$ must be attached along another $\mathrm { N } _ { 1 }$ fiber and so contract at $\scriptstyle { \frac { 1 } { 2 k } }$ where they support $k$ fibers.


Next we consider the base curve at ${ \frac { 1 } { 1 2 } } + \epsilon$

emma 5.5. Let ${ \mathcal { A } } = ( a , \ldots , a )$ for $\begin{array} { r } { a = \frac { 1 } { 1 2 } + \epsilon } \end{array}$ .
Then curves $C$ parametrized by $\overline { { \mathcal { M } } } _ { 0 , \mathcal { A } }$ are either (1) a smooth $\mathbb { P } ^ { 1 }$ with 24 marked points, with at most 11 markings coinciding, or (2) the union of two rational curves, each with 12 marked points and at most 11 markings coinciding.

Proof.
If $C$ is a smooth $\mathbb { P } ^ { 1 }$ , since the total weight for any marking is $\leq 1$ we see that $\leq 1 1$ points can coincide.
If $C$ is the union of two rational curves, since each point is weighted by ${ \frac { 1 } { 1 2 } } + \epsilon$ , and since each curve needs total weight $> 2$ (including the node), each curve must have (exactly) 12 points, and again at most 11 can coincide.
Finally, suppose $C$ is the union of three components $C = \cup _ { i = 1 } ^ { 3 } C _ { i }$ with $C _ { 1 }$ and $C _ { 3 }$ the end components.
Since the $C _ { 2 }$ component needs at least one marking to be stable, at least one of $C _ { 1 } , C _ { 3 }$ will not have enough marked points to be stable.


Corollary 5.6. Let ( $f : X  C , S + F _ { a } )$ ) be a surface pair parametrized by $\overline { { \mathscr { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ .
Then $f : X \to C$ has at most two elliptically fibered components.

Remark 5.7. Note that $X$ can have many Type I pseudoelliptic components mapping by $f$ onto marked points of $C$ .

Definition 5.8. If $f : X \to C , S + F _ { a } )$ a surface pair parametrized by $\overline { { \mathcal { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ , the main component of $X$ denoted by $X _ { m }$ , is the union of all elliptically fibered components of $f : X \to C$

Remark 5.9. By Corollary 5.6, for all surfaces pairs parametrized by $\mathcal { W } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ , either $X _ { m }$ and $C$ are irreducible or $X _ { m } = X _ { 1 } \cup X _ { 2 }$ and $C = C _ { 1 } \cup C _ { 2 }$ where $X _ { i }$ and $C _ { i }$ are irreducible $f | _ { X _ { i } } : X _ { i }  C _ { i }$ is an elliptic fibration.

5.1. Explicit classification of surfaces inside $\overline { { \mathscr { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ .
We conclude that every surface parametrized by $\overline { { \mathcal { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ consists of a main component (see Definition 5.8) possibly with trees of pseudoelliptics sprouting off.
In order to do understand the possible main components $X _ { m }$ parametrized by $\overline { { \mathscr { W } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon ) } }$ , we will use the following construction of a Weierstrass model for $X _ { m }$

5.1.1. Construction of a family of Weierstrass models.
Let $f _ { 0 } : X _ { 0 }  C _ { 0 } , S _ { 0 } + ( F _ { a } ) _ { 0 } )$ be an elliptic surface pair parametrized by $\overline { { \mathcal { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ , which by Corollary 5.6 has at most two elliptic components.
Consider a 1-parameter family ( $f : \mathcal { X }  \mathcal { C } , \mathcal { S } + \mathcal { F } _ { a } )  T$ with generic fiber $( f : X _ { \eta } \to C _ { \eta } , S _ { \eta } + ( F _ { a } ) _ { \eta } )$ a $2 4 \mathrm { { I } _ { 1 } }$ elliptic K3 surface and special fiber $X _ { 0 }$ .
Let $\mathcal { G } _ { \eta }$ be a generic smooth fiber of the elliptic fibration $f : \mathcal { X }  \mathcal { C }$ so that the closure $\mathcal { G }$ is a generic smooth fiber of $f _ { 0 } : X _ { 0 }  C _ { 0 }$ .
In particular, $G _ { 0 } = \mathcal { G } _ { 0 }$ avoids any pseudoelliptic trees of $X _ { 0 }$ .

Let $Y _ { 0 }$ denote the irreducible component of $X _ { 0 }$ on which $G _ { 0 }$ lies.
The component $Y _ { 0 }$ is necessarily elliptically fibered, and so either $Y _ { 0 } = X _ { m }$ is the main component or $X _ { m } = Y _ { 0 } \cup _ { H _ { 0 } } Y _ { 1 }$ glued along a twisted fiber $H _ { 0 }$ .
To classify the possible elliptically fibered components of $X _ { 0 }$ , we will take the relative log canonical model of the pair $( \mathcal { X } , \mathcal { S } + \mathcal { G } )  T$ using the main results of [AB21a].

First, if $X _ { m } = Y _ { 0 } \cup Y _ { 1 }$ , there is a Type WII crossing causing a flip of the section of $Y _ { 1 }$ so that $Y _ { 1 }$ becomes a Type I pseudoelliptic.
Then in either case, we have a new family where $Y _ { 0 }$ is the unique elliptically fibered component with trees of Type I pseudoelliptic surfaces sprouting off of it.
We make the following assumption, and revisit it when we see it holds in Lemmas 5.13 and 5.14.

Assumption 5.10. Suppose every Type I pseudoelliptic tree attached to $Y _ { 0 }$ is attached along the intermediate model of a log canonical Weierstrass cusp.

There exists a sequence of Type WIII extremal contractions followed by a Type WIII relative log canonical morphism of the family that contract the trees of Type I pseudoelliptic components to a point resulting in a Weierstrass model $Y ^ { \prime }$ of $Y _ { 0 }$ .
Denote the resulting family of surfaces $\mathcal { X } ^ { \prime }  T$ .

Since Type WIII contractions preserve the generic fiber of the family $\mathcal { X }  T$ , we must only check Type WII contractions of the section $S$ .
By [Inc20, Proposition 5.9], we may blow up the point to which the section has contracted to preserve the generic fiber of the family, and so we have that $\mathcal { X } _ { \eta } ^ { \prime } = \mathcal { X }$ .
The resulting family of fibrations $\langle \mathcal { X } ^ { \prime } \to \mathcal { C } \rangle \to T$ is a family of slc Weierstrass models over $\mathbb { P } ^ { 1 }$ with $\deg ( \mathcal { L } ) = 2$ , generic fiber a $2 4 1 _ { 1 }$ elliptic K3, and special fiber $Y ^ { \prime }$ .
By Remark 3.15, we can conclude that $Y ^ { \prime }$ is one of the following:

# Weierstrass Limits.

(1) a minimal Weierstrass elliptic K3 surface ( $\deg \mathcal { L } = 2$ ),  
(2) a rational elliptic surface with a single type L cusp, or  
(3) an isotrivial elliptic surface with two type L cusps and all other fibers stable.

By considering the discriminant of $\mathcal { X } ^ { \prime } \to \mathcal { C }$ as a flat family of divisors on $\mathcal { C }$ , we have the following key observation:

Remark 5.11. Suppose $Y ^ { \prime }  C _ { 0 }$ is normal.
The number of $\mathbf { l } _ { 1 }$ fibers of the generic fibration $X _ { \eta }  C _ { \eta }$ that collide onto a singular fiber $F$ of $Y ^ { \prime }  C _ { 0 }$ is the multiplicity of $F$ in the discriminant of the Weierstrass model $Y ^ { \prime }  C _ { 0 }$ .

We can use this observation to constrain the possible components of the twisted stable maps limit of $f : \mathcal { X } _ { \eta }  \mathcal { C } _ { \eta } , \mathcal { S } _ { \eta } + \mathcal { F } )$ .
In this limit, the singular fibers ( $f : \mathcal { X } _ { \eta } \to \mathcal { C } _ { \eta }$ ) cannot collide since they are marked with coefficient one.
Let $Y ^ { \prime \prime }$ be the unique component of a twisted model that maps birationally to the component $Y ^ { \prime }$ in the above family of Weierstrass models.
Then each connected component of the complement of $Y ^ { \prime \prime }$ is a tree of twisted surfaces that gets collapsed onto a fiber of $Y ^ { \prime \prime }$ by the sequence of flips and contractions that produce the Weierstrass model above.
In particular the number of marked fibers on each tree of elliptic components sprouting off a fiber of $Y ^ { \prime \prime }$ is exactly the multiplicity of the resulting of the discriminant of the resulting singular fiber on the Weierstrass model $Y ^ { \prime }$ .

Remark 5.12. The type L cusps are the Weierstrass model of an intermediate fiber of type $\mathrm { I } _ { m }$ for $m \geq 0$ .
Such fibers are not contracted until they have coefficient 0, and so any pseudoelliptic tree glued along a type $\boldsymbol { \mathrm { l } } _ { m }$ fiber will remain when lowering coefficients to any $\epsilon > 0$ .

Finally we revisit Assumption 5.10. We first need the following characterization of intermediate models of non-log-canonical Weierstrass cusps.

Lemma 5.13. Suppose $X = X _ { 0 } \cup _ { G } X _ { 1 }$ is a smoothable broken elliptic surface that is the union of broken elliptic surfaces $X _ { i } \to C _ { i }$ where $C _ { i } \cong \mathbb { P } ^ { 1 }$ and each $X _ { i }$ has a unique main component.
Let $X ^ { \prime }$ be the result of the Type II pseudoelliptic flip of the section of $X _ { 0 }$ , so that the strict transform $X _ { 0 } ^ { \prime }$ is attached to $X _ { 1 } ^ { \prime }$ by an intermediate fiber $A \cup G$ .
Then $A \cup G$ is the intermediate fiber of an slc cusp if and only if $- S _ { 0 } ^ { 2 } \leq 1$ , where $S _ { 0 }$ is the section of $X _ { 0 }  C _ { 0 }$ .

Proof.
The question is local around a neighborhood of the flip.
Therefore, we may assume that $X _ { 0 }$ and $X _ { 1 }$ are irreducible, so that there are no pseudoelliptic trees sprouting off either of them.
On the component $X _ { 1 } ^ { \prime }$ we have the divisor $S _ { 1 } + a A + G$ .
Note that $G$ has coefficient one since it is in the double locus, and the coefficient $a$ is given by the sum of coefficients of marked fibers on $X _ { 1 } ^ { \prime }$ .
Then the Weierstrass model of $A \cup G$ inside $X _ { 1 } ^ { \prime }$ has log canonical singularities if and only if the $G$ contracts onto the Weierstrass model in the log canonical model of the pair $( X _ { 1 } , S + G )$ , i.e., when all the coefficients on $X _ { 0 } ^ { \prime }$ are $0$ .
Since the pair is smoothable, this occurs if and only if $X _ { 0 } ^ { \prime }$ contracts to a point in the log canonical model of $X$ , where all the coefficients on $X _ { 0 } ^ { \prime }$ are set to 0. Since $G$ is marked with coefficient one on $X _ { 0 } ^ { \prime }$ , this occurs if only if $X _ { 0 } ^ { \prime }$ is a minimal rational elliptic surface by [AB17, Proposition 7.4] which holds if and only if $- S _ { 0 } ^ { 2 } \leq 1$ (where the case $< 1$ happens if $G$ is a twisted fiber rather than a stable fiber of $X _ { 0 }$ ).


Lemma 5.14. Let $X$ be a surface parametrized by $\overline { { \mathscr { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ and suppose $Y \subset X _ { m }$ is a normal main component.
Then Assumption 5.10 is satisfied for every pseudoelliptic tree attached to $Y$ .
Moreover, the fibers these pseudoelliptic trees are attached to are minimal intermediate fibers.

Proof.
Let $X ^ { \prime }  C ^ { \prime }$ denote the twisted stable maps model of $X  C$ , and let $X _ { m } ^ { \prime }$ and $Y ^ { \prime }$ denote the strict transform of $X _ { m }$ and $Y$ in $X ^ { \prime }$ .
Let $Z$ be a pseudoelliptic glued to an intermediate fiber $F$ of $Y$ , and let $Z ^ { \prime }$ be the components of $X ^ { \prime }$ that map to $Z$ .
By Remark 5.11, the number of markings on $Z$ is equal to the contribution of $F$ to the discriminant of the Weierstrass model of $Y$ .
Since $X _ { m }$ is the main component, there are $< 1 2$ markings on $Z$ , and so the order of vanishing of the discriminant of $F$ in $Y$ is $< 1 2$ .
It follows that the order of vanishing of the Weierstrass data in a neighborhood of this fiber satisfy $\operatorname* { m i n } \{ 3 v ( a ) , 2 v ( b ) \} < 1 2$ so these are minimal Kodaira types by the standard classification.


5.1.2. $X _ { m }$ is irreducible.
We first deal with the case where the main component $X _ { m }$ of a surface parametrized by $\mathcal { W } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ is irreducible.

Proposition 5.15. Let $X$ be a surface parametrized by $\mathcal { W } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ such that the main component $X _ { m }$ is irreducible and normal.
Then $X _ { m }$ is a minimal elliptic $K \mathcal { S }$ surface with trees of pseudoelliptic surfaces of Type $I$ attached along intermediate models of $\mathrm { I } _ { n } ^ { * } , \mathrm { I I } ^ { * } , \mathrm { I I I } ^ { * }$ and IV $^ *$ fibers.

Proof.
By Lemma 5.14, Assumption 5.10 is satisfied.
Following Construction 5.1.1, we saw that there are three possibilities for the Weierstrass stable replacement of the main component $X _ { m }$ of a surface in $\overline { { \mathscr { W } _ { \sigma } } } ( \frac { 1 } { 1 2 } + \epsilon )$ .
In case (1) we have a minimal Weierstrass elliptic K3 surface.
Then since all fibers are minimal Weierstrass fibers, any pseudoelliptic surface has to be attached by the intermediate model of a minimal Weierstrass fiber.
These are exactly the intermediate models of type $\mathrm { I } _ { n } ^ { * } , \mathrm { I I , I I I , I V , I I ^ { * } , I I I ^ { * } , I V ^ { * } }$ , since type $\mathbf { l } _ { n }$ Weierstrass fibers do not have intermediate models.
By Lemma 5.3, pseudoelliptics sprouting off of II, III and IV fibers have contracted onto the Weierstrass model.
We now rule out cases (2) and (3) of Construction 5.1.1.

In case (2), the Weierstrass model of the main component is a rational elliptic surface with exactly one type $\mathrm { L }$ cusp.
In this case, there must be a Type I pseudoelliptic tree $Z$ in $X$ attached to $X _ { m }$ along an intermediate model of an L cusp, and by Remark 5.11, there are 12 marked pseudofibers on $Z$ .
Let $X _ { 1 }  C _ { 1 }$ be a twisted stable maps model that maps to $X$ in $\overline { { \mathscr { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ .
We may write $X _ { 1 } = Y _ { 1 } \sqcup _ { \operatorname { I } _ { n } } Z _ { 1 }$ where

(1) $Z _ { 1 }$ is a broken elliptic fibration that dominates the pseudoelliptic tree $Z$ ,  
(2) $Y _ { 1 }$ is a broken elliptic fibration that dominates $X \setminus Z$ ,  
(3) the component of $Y _ { 1 }$ supporting the fiber $Y _ { 1 } \cap Z _ { 1 } = \operatorname { I } _ { n }$ is birational to $X _ { m }$ , and  
(4) the $Y _ { 1 } \cap Z _ { 1 } = \operatorname { I } _ { n }$ fiber becomes the intermediate fiber on $X _ { m }$ after $Z _ { 1 }$ undergoes a Type II transformation into the pseudoelliptic tree $Z$ .

Then 12 of the marked fibers of $X _ { 1 }  C _ { 1 }$ must lie on $Z _ { 1 }$ and the other 12 on $Y _ { 1 }$ .
In particular there is a node of $C _ { 1 }$ , such that if we separate $C _ { 1 }$ along that node, we obtain two trees of rational curves each with 12 marked points.
However, this means the stable replacement of $C _ { 1 }$ inside the Hassett space $\overline { { \mathcal { M } } } _ { 0 , \mathcal { A } }$ for ${ \mathcal { A } } = ( a , \ldots , a )$ with $\begin{array} { r } { a = \frac { 1 } { 1 2 } + \epsilon } \end{array}$ , is a nodal union of two components, contradicting that $X$ has only one main component.

In case (3), the Weierstrass model of $X _ { m }$ is a trivial surface with exactly two type L cusps and all other fibers stable.
There must be Type I pseudoelliptic trees attached along each of these L cusp fibers in $X _ { m }$ , and no other pseudoelliptic trees attached to $X _ { m }$ , as every other fiber of its Weierstrass model is stable.
As in the previous analysis, let $X _ { 1 }  C _ { 1 }$ be a twisted stable maps surface whose image in $\mathscr { W } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ is $X$ , and let $X ^ { \prime }$ be the component of $X _ { 1 }$ that dominates $X _ { m }$ Then $X ^ { \prime }$ is attached to exactly two other components of $X _ { 1 }$ , so by stability it must have at least one marked point on it.
Since $X _ { 1 }  C _ { 1 }$ is the twisted stable maps model, all the marked fibers have $j$ -invariant $\infty$ and so since $X ^ { \prime }$ is isotrivial, it must be non-normal, a contradiction.


Next we consider the irreducible, but non-normal main component case.

Theorem 5.16. Let $X$ be a surface parametrized by $\mathcal { W } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ with an irreducible non-normal main component $X _ { m }$ .
Then one of the following holds.

(a) $X _ { m }$ is an isotrivial $j = \infty$ fibration with 4N $^ { 1 }$ minimal Weierstrass fibers;  
(b) $X _ { m }$ is an isotrivial $j = \infty$ fibration with 2N $\bot$ minimal Weierstrass fibers, as well as an intermediate N $^ 2$ fiber which must have a tree of pseudoelliptic surfaces attached to it along a type $\mathrm { I } _ { n }$ pseudofiber;  
(c) $X _ { m }$ is an isotrivial $j = \infty$ fibration with 2N $^ 2$ intermediate fibers each of which has a tree of pseudoelliptic surfaces attached to it by an $\mathrm { I } _ { n }$ fiber;  
(d) $X _ { m }$ is an isotrivial $j = \infty$ fibration with a minimal Weierstrass $\mathrm { N _ { 1 } }$ fiber as well as an intermediate N $^ 3$ fiber which has a tree of pseudoelliptic surfaces attached to it by an $\mathrm { I } _ { n } ^ { * }$ fiber.  
(e) $X _ { m }$ is an isotrivial $j = \infty$ fibration with a single intermediate $\mathrm { N _ { 4 } }$ fiber which has a tree of pseudoelliptic surfaces attached to it by an $\mathrm { I } _ { n }$ fiber; or

Moreover, if we denote by $l$ the number of marked $\mathrm { N } _ { 0 }$ fibers on $X _ { m }$ , then $l$ lies in the following range: (a): $4 \leq l \leq 1 6$ , $( b )$ : $3 \leq l \leq 1 7$ , (c): $2 \leq l \leq 1 8$ , (d): $8 \leq l \leq 1 8$ , (e): $1 3 \leq l \leq 1 9$ .

Proof.
Suppose that Assumption 5.10 is satisfied.
By Construction 5.1.1, the Weierstrass model of the main component must be an slc isotrivial $j = \infty$ Weierstrass fibration with $\deg \mathcal { L } = 2$ , which are classified by Proposition 4.13. The lct of a type N $^ 2$ fiber is $0$ , so these do not contract to Weierstrass models, and any attached pseudoelliptic trees do not contract for nonzero weight.

In case $( c )$ , the stability condition on the twisted stable maps limit implies that there must be at least one marked N $_ 0$ to give that rational component of the base curve at least three special points.

The types of pseudofibers that are attached to intermediate $\mathrm { N } _ { 1 }$ and N $^ 2$ fibers respectively must have $j$ -invariant $\infty$ , so they are either type $\mathbf { l } _ { n }$ or $\mathrm { I } _ { n } ^ { * }$ .
The twisted model of an N fiber is a $\bot$ nonreduced rational curve, and so must have a stabilizer at the corresponding point of the twisted stable map.
Therefore, it must be attached to an $\mathrm { I } _ { n } ^ { * }$ fiber, which also has a nontrivial stabilizer at the corresponding point of the twisted stable map.
Similarly, the twisted model of an N $^ 2$ fiber is a nodal curve so it has no stabilizer, and therefore must be attached to an $\mathrm { I } _ { n }$ fiber.

If Assumption 5.10 is not satisfied, then by Lemma 5.13 we must have a K3 component $Y$ attached to $X _ { m }$ along a fiber $F$ such that $Y$ is not the main component.
This only happens if $Y$ has $< 1 2$ singular fibers counted with multiplicity away from the fiber along which $Y$ is attached to $X _ { m }$ .
In that case $F$ is a fiber of $Y$ with discriminant $\geq 1 3$ so $F ^ { \prime }$ is either an $\mathbf { l } _ { n }$ fiber for $n \geq 1 3$ or an $\mathrm { I } _ { n } ^ { * }$ for $n \geq 7$ .
Consider a generic family of $2 4 1 _ { 1 }$ surfaces degenerating to this surface as in Section 5.1.1.

In the first case, we have that $n$ type $\mathrm { I _ { 1 } }$ fibers collide to sprout out a trivial component with $n$ markings which becomes the main component when $Y$ flips into a pseudoelliptic.
Since $X _ { m }$ has only N fibers away from where $Y$ is attached and the degree of $\mathcal { L }$ must be 2, then the attaching $_ 0$ fiber is an N $^ 4$ by Proposition 3.20. This gives us (e).
In the second case, let us denote by $Y ^ { \prime }$ and $X _ { m } ^ { \prime }$ the strict transforms of $Y$ and $X _ { m }$ in the twisted stable maps replacement of the limit of the family.
Then $Y ^ { \prime }$ and $X _ { m } ^ { \prime }$ are glued along twisted $\mathrm { I } _ { n } ^ { * } / \mathrm { N } _ { 1 }$ fibers since the order of the stabilizer is 2. Then the base curve of the $X _ { m } ^ { \prime }$ component must have at least one more point with a stabilizer since any finite cover of $\mathbb { P } ^ { 1 }$ is ramified in at least two points.
On the other hand, the stabilizer of any $j$ -invariant $\infty$ curve is $\mu _ { 2 }$ so these other points have to have stabilizers of order 2. Now when the component $Y ^ { \prime }$ flips into the pseudoelliptic surface $Y$ , then the twisted fiber on $X _ { m } ^ { \prime }$ it is attached must flip into a non semi-log canonical intermediate fiber since Assumption 5.10 fails.
Thus it must be an $\mathrm { N } _ { k }$ fiber for $k \geq 3$ .
The other twisted fibers on $X _ { m } ^ { \prime }$ must flip into intermediate models of $\mathrm { N } _ { k }$ fibers for $k \geq 1$ since the $\mathrm { N } _ { 0 }$ fiber has no stabilizers.
Since the degree of $\mathcal { L }$ for the main component $X _ { m }$ must be 2, then by Proposition 3.20, the fiber along which $Y$ is attached must be an N $^ 3$ and the only other non-stable fiber is a single N $^ { 1 }$ .
This gives us case (d).

To obtain the number of markings, we may apply Proposition 4.15 to see that each N $k$ fiber is marked with multiplicity at least $k + 1$ .
This gives an upper bound on $n$ .
For the lower bound, we look at the largest number of marked $\mathrm { I } _ { 1 }$ fibers that can appear on a component attached to the $\mathrm { N } _ { k }$ fiber.
For an N $^ { 1 }$ this is 5 markings on an $\mathrm { 5 I _ { 1 } I _ { 1 } ^ { * } }$ rational, for N $^ 2$ this is 11 markings on a $1 2 1 _ { 1 }$ (attached along one of the $\mathbf { l } _ { 1 }$ fibers), for N $^ 3$ this is 11 markings on an $1 1 \mathrm { I } _ { 1 } \mathrm { I } _ { 7 } ^ { \ast }$ elliptic K3, and for N $^ 4$ this is 11 markings on an 12I1I13 elliptic K3.
Here we have used that $X _ { m }$ is the main component so all the other components must have undergone pseudoelliptic flips at a wall above $1 / 1 2 + \epsilon$ .
Finally, each N $^ { 1 }$ fiber is Weierstrass since there are at most 5 markings on the component attached to it and so by Lemma 5.4, these components contract to a point at a WIII wall above $1 / 1 2 + \epsilon$ .


Remark 5.17. Each of the main components in Theorem 5.16 that have only intermediate models of semi-log canonical cusps (e.g. cases (a), (b) and (c)) are $j = \infty$ limits of normal isotrivial elliptic surfaces.
The 4N $\bot$ surfaces are limits of $4 \mathrm { { I } _ { 0 } ^ { * } }$ isotrivial fibrations.
Indeed, the locus in the moduli space of such surfaces is birational to $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ where the first coordinate parametrizes the $j$ -invariant of the fibration and the second coordinate parametrizes the configuration of the 4I $_ { 0 } ^ { * }$ (respectively $4 \mathrm { N } _ { 1 }$ ) singular fibers.
Similarly the 2N1N $^ 2$ surface is the limit of the isotrivial 2I $^ { * } _ { 0 } \mathrm { L }$ , surface and there is a rational curve of these in the moduli space.
Finally the 2N $^ 2$ surface is the limit of isotrivial 2L Weierstrass fibrations, but this family of 2L surfaces does not actually appear on this component of the moduli space as we describe below.

Note that in each of these cases, when the surface is isotrivial with $j \neq \infty$ , all the markings must be concentrated on the special fibers.
Indeed by Remark 5.11, there must be six markings concentrated at an $\mathrm { I } _ { 0 } ^ { \ast }$ fiber and 12 concentrated at a type L fiber.
Therefore the isotrivial $j = \infty$ surface pairs that are limits of Weierstrass models as in the above paragraph must have six markings concentrated at each N $^ { 1 }$ fiber, and 12 markings concentrated at each N $^ 2$ fiber.
In particular, they cannot have any marked N $_ 0$ fibers.
Therefore, not all surface pairs with isotrivial $j = \infty$ main components are in the limit of the above locus of normal Weierstrass fibrations.
In particular, since the type 2N $^ 2$ fibrations must have at least one marked N $_ 0$ fiber by stability for twisted stable maps, we see that the 2L family limiting to 2N $^ 2$ does not appear.

Finally we address the question of existence of each of the limits described above.

Proposition 5.18. Each of the cases described by Proposition 5.15 and Theorem 5.16 occurs in $\mathcal { W } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ .

Proof.
We may take the Weierstrass model of the described main component.
In each case it has a Weierstrass equation with $A , B$ of degree 8 and 12 respectively.
Since the space of Weierstrass equations is irreducible, then there exists a family of $2 4 1 _ { 1 }$ elliptic $K 3$ surfaces with this Weierstrass limit.
By taking the stable replacement in $\overline { { \mathscr { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ we must obtain stable limits as described.
$\boxed { \begin{array} { r l } \end{array} }$

5.1.3. $X _ { m }$ is reducible.
Now we classify the broken elliptic surfaces in $\overline { { \mathscr { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ where $X _ { m }$ is the union of two irreducible surfaces.

Theorem 5.19. Let $X$ be a surface parametrized by $\mathcal { W } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ with reducible main component, i.e. $X _ { m } = Y _ { 0 } \cup Y _ { 1 }$ .
Then one of the following holds.

(1) $Y _ { i }$ are rational elliptic surfaces glued along an $\mathrm { I _ { 0 } }$ fiber.
They are minimal Weierstrass surfaces away from possible intermediate Type $\mathrm { I I ^ { * } , I I I ^ { * } }$ and IV∗ fibers along which Type I pseudoelliptic trees are attached.  
(2) $Y _ { 0 }$ is an elliptic K3 surface, $Y _ { 1 }$ is a trivial $j$ -invariant $\infty$ surface, and they are glued along $\mathrm { I _ { 1 2 } / N _ { 0 } }$ fibers.
There are 12 marked $\mathrm { N } _ { 0 }$ fibers on $Y _ { 1 }$ , and $Y _ { 0 }$ has minimal Weierstrass fibers or minimal intermediate fibers Type II $^ *$ , III $^ *$ , or IV∗ fibers where Type I pseudoelliptic trees are attached.  
(3) $Y _ { 0 }$ is an elliptic $K \mathcal { 3 }$ with an $\mathrm { I } _ { 6 } ^ { * }$ fiber, $Y _ { 1 }$ is an $\mathrm { 2 N _ { 1 } }$ isotrivial $j$ -invariant $\infty$ surface, and they are glued along twisted $\mathrm { I _ { 6 } ^ { * } / N _ { 1 } }$ fibers.
Away from the $\mathrm { I } _ { 6 } ^ { * }$ fiber, $Y _ { 0 }$ has minimal Weierstrass fibers or minimal intermediate $\operatorname { I I } ^ { * } , \operatorname { I I I } ^ { * }$ , and $\mathrm { I V ^ { * } }$ fibers where Type I pseudoelliptic trees are attached.
There are $7 \leq l \leq 1 0$ marked $\mathrm { N } _ { 0 }$ fibers on $Y _ { 1 }$ .  
(4) $Y _ { i }$ are isotrivial $j$ -invariant $\infty$ surfaces glued along $\mathrm { N } _ { 0 }$ fibers.
Each surface has a single intermediate $\mathrm { N _ { 2 } }$ fiber with a Type I pseudoelliptic tree attached.
There are $1 \leq l _ { i } \leq 9$ marked $\mathrm { N } _ { 0 }$ fibers on $Y _ { i }$ .  
(5) $Y _ { i }$ are isotrivial $j$ -invariant $\infty$ surfaces glued along $\mathrm { N } _ { 0 }$ fibers.
Each surface has 2 minimal Weierstrass $\mathrm { N _ { 1 } }$ fibers.
There are $2 \leq l _ { i } \leq 8$ marked $\mathrm { N } _ { 0 }$ fibers on $Y _ { i }$ .  
(6) $Y _ { i }$ are isotrivial $j$ -invariant $\infty$ surfaces glued along $\mathrm { N } _ { 0 }$ fibers.
$Y _ { 0 }$ has 2 minimal Weierstrass fibers $\mathrm { N _ { 1 } }$ fibers and $Y _ { 1 }$ has one intermediate $\mathrm { N _ { 2 } }$ fiber with a Type I pseudoelliptic tree attached.
There are $2 \leq l _ { 0 } \leq 8$ marked $\mathrm { N } _ { 0 }$ fibers on $Y _ { 0 }$ and $1 \leq l _ { 1 } \leq 9$ marked $\mathrm { N } _ { 0 }$ fibers on $Y _ { 1 }$ .

Proof.
We will proceed by taking the Weierstrass limit of the main component and using the classification in Section 5.1.1 to determine what can be attached as the other main component.

First suppose that Assumption 5.10 does not hold for the fiber along which $Y _ { i }$ are glued, so that after performing a pseudoelliptic flip of $Y _ { 0 }$ , the fiber on $Y _ { 1 }$ is not the intermediate model of a semi-log canonical Weierstrass cusp.
Then as in the proof of Theorem 5.16, $Y _ { 0 }$ is a K3 component and $Y _ { 1 }$ is an isotrivial $j$ -invariant $\infty$ surface.
Furthermore, they are either glued along twisted $\mathrm { I } _ { n } / \mathrm { N } _ { 0 }$ or $\mathrm { I } _ { n } ^ { * } / \mathrm { N } _ { 1 }$ fibers.
Since they are the two main components, they must each have 12 markings, so we conclude that $n = 1 2$ in the first case and $n = 6$ in the second case.
Furthermore, as in the proof of Theorem 5.16, in the $\mathrm { I } _ { n } ^ { * } / \mathrm { N } _ { 1 }$ case, $Y _ { 1 }$ must have another N $\bot$ fiber.
This gives us cases (2) and (3) respectively.

From now on we can suppose that Assumption 5.10 holds.
Let us fix some notation.
Denote the Weierstrass limit of $Y _ { i }$ by $Y _ { i } ^ { 0 }$ which must be one of the surfaces list in Section 5.1.1 if it is normal, or Proposition 4.13 if it is isotrivial $j$ -invariant $\infty$ .
We will denote by $X ^ { 1 }  C ^ { 1 }$ a twisted stable maps model of the surface $X  C$ in $\overline { { \mathcal { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ and we will denote by $Y _ { i } ^ { 1 }$ the unique component of $X ^ { 1 }$ dominating $Y _ { i }$ .
Finally let $Z _ { i } ^ { 1 } \subset X ^ { 1 }$ the maximal connected union of connected components of $X ^ { 1 }$ that contains $Y _ { i } ^ { 1 }$ .
Finally we will denote by $G$ the fiber along which $Y _ { 0 }$ and $Y _ { 1 }$ are glued, and by $G _ { i }$ its model in the Weierstrass limit, which is obtained by flipping one of $Y _ { i }$ and contracting the transform on $G$ on the other.
See Figure 3.

![](images/729b190c74a9bce0c5d0c3d4a84d077fc342b4c508889a82b524c60447afd262.jpg)  
Figure 3. The circled components $Z _ { i }$ represent the union of $Y _ { i } ^ { \prime }$ along with the pseudoelliptic trees emanating from $Y _ { i } ^ { \prime }$ .
The entire $Z _ { i }$ component dominates $Y _ { i }$ , and the $Y _ { i } ^ { \prime }$ components are the components containing the pseudoelliptics.

Now since $Y _ { 0 }$ and $Y _ { 1 }$ satisfy Assumption 5.10 for the fiber along which they are glued, then by Lemma 5.13 we must have $0 < - S _ { i } ^ { 2 } \leq 1$ where $S _ { i }$ are the sections of $Y _ { i }$ .
Note that $S _ { 0 } ^ { 2 } \neq 0$ , otherwise $Y _ { 0 }$ would be trivial and so the degree the $j$ -map on $Z _ { 0 }$ would be 0 and the degree of the $j$ -map on $Z _ { 1 }$ would be 24, but then this would put us in situation (2).

Suppose that $Y _ { 0 }$ is normal.
Then by Section 5.1.1, $Y _ { 0 }$ is a rational elliptic surface and $G _ { 0 }$ is a type L cusp.
Since the twisted model of a type L cusp is a stable curve, then $G$ is an $\mathbf { l } _ { n }$ fiber.
On the other hand, there must be 12 markings on $Y _ { 0 }$ away from $G$ , and so $n = 0$ and $G$ is in fact a smooth fiber.
Since $G$ is smooth, then $Y _ { 1 }$ cannot be isotrivial $j$ -invariant $\infty$ so it is normal and the same analysis applies to $Y _ { 1 }$ .
Thus we obtain (1).

Next if $Y _ { 0 }$ is not normal, then as above $Y _ { 1 }$ is also non-normal.
Now $Y _ { i }$ satisfy Assumption 5.10 for the fiber $G$ .
We claim that they must also satisfy it for any pseudoelliptic trees away from $G$ .
Indeed suppose that $Y _ { 0 }$ has an intermediate fiber $F$ not satisfying 5.10. Then by Lemma 5.13, there must be an elliptic K3 attached to it.
Every fiber of $Y _ { i }$ is $\mathrm { N } _ { k }$ for $k \leq 2$ and we get cases (4), (5), (6) by considering the various possible $\mathrm { N } _ { k }$ fibers on a surface with $- S ^ { 2 } \leq 1$ .

Since N $^ 2$ fibers have 0 lct, they must be intermediate with pseudoelliptic trees attached, while pseudoelliptic trees attached to an N $\bot$ fiber undergo type WIII contractions at walls above $1 / 1 2 + \epsilon$ by Lemma 5.4 so $\mathrm { N _ { 1 } }$ fibers are minimal Weierstrass.
Finally, the number of markings is constrained by Proposition 4.15, stability, and the fact that there are two main components so there must be 12 total markings on each.


Proposition 5.20. Each of the cases described in Theorem 5.19 occurs in the boundary of $\overline { { \mathscr { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ .

Proof.
Case (1) is the stable replacement in $\mathcal { W } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ of a Kulikov degeneration of Type II.
Case (2) occurs when $1 2 \mathrm { { I } _ { 1 } }$ fibers collide to give an $\mathrm { I _ { 1 2 } }$ fiber.
Similarly, case (3) occurs when 12I1 fibers collide to form an $\mathrm { I } _ { 6 } ^ { * }$ fiber.
Case (4) occurs when one starts with a degeneration of type (1) and take the limit as the $\mathrm { I _ { 1 } }$ fibers approach the double locus $G$ .
Since marked $\mathbf { l } _ { 1 }$ fibers from both $Y _ { 0 }$ and $Y _ { 1 }$ must fall into $G$ as the $j$ -invariant of $G$ must match on both sides, then two isotrivial components appear so that each rational surface is attached to one of them along an N $_ 0$ which leads to N $^ 2$ fibers when the rational surfaces undergo a flip.
Similarly, case (5) occurs when you start with a surface of type (1) and degenerate the two rational components into $2 \mathrm { N } _ { 1 }$ isotrivial $j$ -invariant $\infty$ surfaces.
Finally, for case (6), take a degeneration as in case (1) and then further degenerate $Y _ { 0 }$ so that it is an isotrivial $2 \mathrm { { I } _ { 0 } ^ { * } }$ surface.
Then the stable replacement of the limit as the $j$ -invariant of the 2I $\mathbf { \Pi } _ { 0 } ^ { * }$ surface approaches $\infty$ is case (6).
$\boxed { \begin{array} { r l } \end{array} }$

# 6. Surfaces in $\overline { { \mathscr { W } } } _ { \sigma } ( \epsilon )$ , the 24-marked space at $a = \epsilon$

In the previous section, we studied the wall crossings that occur in $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ as we let the weight vary from 1 to $1 / 1 2 + \epsilon$ , and we used this to classify the surfaces parametrized by the boundary of $\overline { { \mathscr { W } } } _ { \sigma } ( a )$ for $a = 1 / 1 2 + \epsilon$ .
The goal of this section is to explicitly study the wall crossings that occur as we reduce the weight further, from $a = 1 / 1 2 + \epsilon$ to $a = \epsilon$ for $0 < \epsilon \ll 1$ .
As a result, we determine the surfaces parametrized by the boundary of $\overline { { \mathscr { W } _ { \sigma } ( \epsilon ) } }$ .
The main results in this direction are Theorems 6.13 and Theorem 6.14. In Theorem 6.13 we describe the possible surfaces on the boundary, and in Theorem 6.14 we use the theory of twisted stable maps (see Section 3.2) to show that all such surfaces appear on the boundary.
Finally, in Theorem 6.15, we describe a morphism from the coarse space of $\overline { { \mathscr { W } } } _ { \sigma } ( \epsilon )$ to the GIT quotient ${ \overline { { \mathrm { W } } } } ^ { G }$ .
These three theorems together give a proof of Theorem 1.1.

We begin with the wall at $\textstyle { \frac { 1 } { 1 2 } }$ .

Lemma 6.1. At $\begin{array} { r } { a = \frac { 1 } { 1 2 } } \end{array}$ , there are Type III contractions of rational pseudoelliptic components attached by an $\mathrm { I } _ { 0 } ^ { \ast }$ fiber.

Proof.
An $\mathrm { I } _ { 0 } ^ { \ast }$ must be attached along an other $\mathrm { I } _ { 0 } ^ { \ast }$ by the stabilizer condition.
Furthermore, an $\mathrm { I } _ { 0 } ^ { \ast }$ rational surface has 6 other markings with multiplicity.
Putting this together with the description of the walls, we get a wall at $\begin{array} { r } { \frac { 1 } { 2 k } = \frac { 1 } { 1 2 } } \end{array}$ since $\frac { 1 } { 2 }$ is the lct of $\mathrm { I } _ { 0 } ^ { \ast }$ (see Equation 2 in Section 3).


Lemma 6.2. At $\begin{array} { r } { a = \frac { 1 } { 1 2 } } \end{array}$ the trivial component $Y _ { 1 }$ in case (2) of Theorem 5.19 contracts onto the $\mathrm { I _ { 1 2 } }$ fiber it is attached to.

Proof.
The component of the base curve lying under $Y _ { 1 }$ contracts to a point but since $Y _ { 1 }$ is trivial, it contracts onto a fiber.


Lemma 6.3. Let $X$ be a surface parametrized by $\overline { { \mathscr { W } _ { \sigma } } } ( \frac { 1 } { 1 2 } + \epsilon )$ from Theorem 5.19(3). Then the stable replacement for coefficients ${ \frac { 1 } { 1 2 } } - \epsilon$ is an irreducible pseudoelliptic K3 surface with an $\mathrm { I } _ { 6 } ^ { * }$ fiber.

Proof.
$X$ has main component $X _ { m } = Y _ { 0 } \cup Y _ { 1 }$ consisting of an elliptic K3 with a twisted $\mathrm { I } _ { 6 } ^ { * }$ fiber glued to an isotrivial $j$ -invariant $\infty$ surface along a twisted N $\bot$ fiber.
Each surface has 12 markings.
At coefficient ${ \frac { 1 } { 1 2 } } - \epsilon$ , both section components are contracted by an extremal contraction.
We first perform the extremal contraction of the section of $Y _ { 1 }$ which results in a flip of $Y _ { 1 }$ to a pseudoelliptic surface.
Then the section of $Y _ { 0 }$ contracts to form a pseudoelliptic with the pseudoelliptic model of $Y _ { 1 }$ glued along an $\mathrm { I } _ { 6 } ^ { * }$ pseudofiber.
Finally, $Y _ { 1 }$ contracts onto a point as in Lemma 6.1. 

Putting the above together with the observation that the Hassett space becomes a point at $\textstyle { \frac { 1 } { 1 2 } }$ so the base curves all contract to a point, we get the following:

Theorem 6.4. Let $X$ be a surface parametrized by $\overline { { \mathcal { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } - \epsilon )$ .

(1) If $X$ has a single main component, then $X _ { m }$ is the pseudoelliptic surface associated to an elliptic surface as in Proposition 5.15 and Theorem 5.16 with an $A _ { 1 }$ singularity where the section contracted.
Any type II, III, IV, $\mathrm { N _ { 1 } }$ and $\mathrm { I } _ { k } ^ { * }$ for $k \leq 5$ pseudofibers of $X _ { m }$ are Weierstrass and any $\mathrm { I } _ { n }$ fibers satisfy $n \leq 1 2$ .
There are pseudoelliptic trees sprouting off of intermediate Type $\mathrm { I I ^ { * } , I I I ^ { * } , I V ^ { * } }$ and $\mathrm { N } _ { k }$ for $k \geq 2$ fibers as before.  
(2) If $X$ has two main components, then $X _ { m }$ is a union along a twisted pseudofiber of the surfaces appearing in Theorem 5.19, parts $( 1 )$ , (4), (5) and (6).
Any type II, III, IV, N $\bot$ and $\mathrm { I } _ { k } ^ { * }$ for $k \leq 5$ pseudofibers are Weierstrass.
There are pseudoelliptic trees sprouting off of intermediate $\mathrm { I I ^ { * } , I I I ^ { * } , I V ^ { * } }$ and $\mathrm { N _ { 2 } }$ fibers as before.

Lemma 6.5. There are Type III walls at $\begin{array} { r } { a = \frac { 1 } { 6 0 } , \frac { 1 } { 3 6 } } \end{array}$ , and $\textstyle { \frac { 1 } { 2 4 } }$ where rational pseudoelliptic surfaces attached along intermediate type $\mathrm { I I ^ { * } }$ , III $^ *$ and $\mathrm { I V ^ { * } }$ fibers respectively contract to a point.

Proof.
This follows from [AB21a, Theorem 6.3] as well as the observation that that a rational elliptic surface attached to a type $\mathrm { I I ^ { * } , I I I ^ { * } }$ or IV $^ *$ fiber must have a $\operatorname { I I } , \operatorname { I I I }$ , or IV fiber respectively and so it has $1 0 , 9$ , or 8 other marked fibers counted with multiplicity.


Next we study some examples of the transformations that occur for small coefficient.

Example 6.6. (See Figure 4) Suppose $X _ { \eta }$ is a smooth elliptic K3 surface with 24 (I $^ { 1 }$ ) fibers, and suppose it appears as the general fiber of a family $f : \mathcal { X }  B , \mathcal { S } + \mathcal { F } _ { a } )$ with limit as in Theorem 5.16 case (d).
In particular, this is a stable limit for $\begin{array} { r } { a = \frac { 1 } { 1 2 } + \epsilon } \end{array}$ and $\mathcal { F }$ consisting of the $2 4 1 _ { 1 }$ fibers on the generic surface $X _ { \eta }$ .
We will compute the stable limit of this family for $a < \frac { 1 } { 1 2 }$ .
We will denote by $X ^ { a }$ the $a$ -stable special fiber of $\mathcal X  B$ .

We begin with the twisted stable maps limit $X ^ { 1 }  C ^ { 1 }$ .
It consists of a union $Y _ { 0 } ^ { 1 } \cup Y _ { 1 } ^ { 1 }$ where $Y _ { 0 } ^ { 1 }$ is an elliptic K3 and $Y _ { 1 } ^ { 1 }$ is a trivial $j$ -invariant $\infty$ surface with $n$ marked fibers glued along an $\mathbf { l } _ { n }$ fiber of $Y _ { 0 } ^ { 1 }$ where $n > 1 2$ .
At $\textstyle a = { \frac { 1 } { 2 4 - n } }$ , the component $Y _ { 0 } ^ { 1 }$ undergoes a pseudoelliptic flip to obtain the model in Theorem 5.16 (d), i.e. $Y _ { 0 } ^ { a }$ is a pseudoelliptic K3 glued along an intermediate N $^ 4$ fiber $A ^ { a } \cup G ^ { a }$ of $Y _ { 1 } ^ { a }$ .
Next, for $\ a \leq \frac { 1 } { 1 2 }$ , the section of $Y _ { 1 } ^ { a }$ contracts onto an $A _ { 1 }$ singularity so that $X ^ { a }$ consists of a pseudoelliptic isotrivial $j$ -invariant $\infty$ surface with an intermediate N $^ 4$ pseudofiber and a pseudoelliptic K3 sprouting off it.
To continue the MMP on this 1-parameter family and compute the stable limit for smaller $a$ , we need to compute $( K \mathcal { X } ^ { a } + \mathcal { F } ^ { a } ) . A ^ { a }$ and $( K \mathcal { X } ^ { a } + \mathcal { F } ^ { a } ) . G ^ { a }$ .

We can restrict the log canonical divisor to the component $Y _ { 1 } ^ { a }$ to obtain $K _ { Y _ { 1 } ^ { a } } + G + ( 2 4 - n ) a A ^ { a } + n a f$ where $f$ is a pseudofiber class.
Pulling back to the blowup of the section $\mu : Y _ { 1 } ^ { b }  Y _ { 1 } ^ { a }$ where $\begin{array} { r } { b = \frac { 1 } { 1 2 } + \epsilon } \end{array}$ , we get

$$
\mu ^ { * } ( K _ { Y _ { 1 } ^ { a } } + G + ( 2 4 - n ) a A ^ { a } + n a f ^ { a } ) = K _ { Y _ { 1 } ^ { b } } + G ^ { b } + ( 2 4 - n ) a A ^ { b } + n a f ^ { b } + 1 2 a S _ { 1 } ^ { b } .
$$

Here $S _ { 1 } ^ { b }$ is the section which is a $- 2$ curve and $f ^ { b }$ is a fiber class.
Now $A ^ { b }$ is the curve obtained by flipping the section $S _ { 0 }$ of $Y _ { 0 } ^ { 1 }$ .
Using the local structure of the flip (see e.g. [LN02, Section 7.1]), we compute that $( A ^ { b } ) ^ { 2 } = - \frac { 1 } { 2 }$ , $\begin{array} { r } { A ^ { b } . G ^ { b } = \frac { 1 } { 2 } } \end{array}$ and $( G ^ { b } ) ^ { 2 } = - \frac { 1 } { 2 }$ .
Similarly, using push-pull for the contraction $\rho : Y _ { 1 } ^ { b }  Y _ { 1 } ^ { 1 }$ onto the twisted model of $Y _ { 1 } ^ { 1 }$ we get that $K _ { Y _ { 1 } ^ { b } } = - 2 f ^ { b } + 2 A ^ { b }$ .
Putting all these together and using push-pull for $\mu$ we get that

$$
\begin{array} { l } { { - G + ( 2 4 - n ) a A ^ { a } + n a f ) . A ^ { a } = ( K _ { Y _ { 1 } ^ { b } } + G ^ { b } + ( 2 4 - n ) a A ^ { b } + n a f ^ { b } + 1 2 a S _ { 1 } ^ { b } ) . A ^ { b } = \frac { n a } { 2 } , } } \\ { { - G + ( 2 4 - n ) a A ^ { a } + n a f ) . B ^ { a } = ( K _ { Y _ { 1 } ^ { b } } + G ^ { b } + ( 2 4 - n ) a A ^ { b } + n a f ^ { b } + 1 2 a S _ { 1 } ^ { b } ) . G ^ { b } } } \\ { { \ } } \\ { { \ = \displaystyle \frac { 1 } { 2 } + ( 2 4 - n ) \frac { a } { 2 } . } } \end{array}
$$

In particular, for $\textstyle a < { \frac { 1 } { n } }$ , there is an extremal contraction of the curve class of $A ^ { a }$ in ${ \mathcal { X } } ^ { a }$ .
On the other hand, since $( A ^ { b } ) ^ { 2 } = - \frac { 1 } { 2 }$ and $\mu$ is the contraction of a $- 2$ curve which intersects $A ^ { b }$ transversely, we have $( A ^ { a } ) ^ { 2 } = 0$ so this curve class rules $Y _ { 1 } ^ { b }$ over $G ^ { b }$ and the extremal contraction for $\textstyle a < { \frac { 1 } { n } }$ contracts $X ^ { a }$ onto $Y _ { 0 } ^ { a }$ , the pseudoelliptic K3.

Remark 6.7. We note that in the above example $n \leq 1 9$ by e.g. [Shi03].

Example 6.8. (See Figure 5) Suppose $X _ { \eta }$ as above is a smooth elliptic K3 surface with 24 (I1) fibers which appears as the general fiber of a family ( $f : \mathcal { X } \to B , \mathcal { S } + \mathcal { F } _ { a } )$ with limit as in Theorem 5.16 (e).
We compute the stable limit for small $a$ as above and we keep the same notation.

The twisted stable maps limit $X ^ { 1 }  C ^ { 1 }$ consists of a union $Y _ { 0 } ^ { 1 } \cup Y _ { 1 } ^ { 1 }$ where $Y _ { 0 } ^ { 1 }$ is an elliptic K3 and $Y _ { 1 } ^ { 1 }$ is a $2 \mathrm { N } _ { 1 }$ isotrivial $j$ -invariant $\infty$ surface.
They are glued along twisted $\mathrm { I } _ { n } ^ { * } / \mathrm { N } _ { 1 }$ fibers with $n > 6$ .
At $\textstyle a = { \frac { 1 } { 1 8 - n } }$ , the component $Y _ { 0 } ^ { 1 }$ undergoes a pseudoelliptic flip to obtain the model in Theorem 5.16 case (e), i.e. $Y _ { 0 } ^ { a }$ is a pseudoelliptic K3 with a twisted $\mathrm { I } _ { n } ^ { * }$ pseudofiber glued along an intermediate N $^ 3$ fiber $A ^ { a } \cup G ^ { a }$ of $Y _ { 1 } ^ { a }$ .
As above, the section of $Y _ { 1 } ^ { a }$ contracts onto an $A _ { 1 }$ singularity for $\ a \leq \frac { 1 } { 1 2 }$ so that $X ^ { a }$ consists of a pseudoelliptic isotrivial $j$ -invariant $\infty$ surface with an intermediate $\mathrm { N _ { 3 } }$ pseudofiber and a pseudoelliptic K3 sprouting off it.
The N $^ { 1 }$ pseudofiber of $Y _ { 1 } ^ { a }$ may have a pseudoelliptic tree sprouting off of it, but it exhibits a Type $\mathrm { W _ { I I I } }$ contraction onto the Weierstrass model of the N $\bot$ fiber by Lemma 5.4.

Restricting the log canonical divisor to the component $Y _ { 1 } ^ { a }$ , we obtain $K _ { Y _ { 1 } ^ { a } } + G + ( 1 8 - n ) a A ^ { a } + ( 6 + n ) a f$ where $f$ is a pseudofiber class.
Pulling back to the blowup of the section $\mu : Y _ { 1 } ^ { b }  Y _ { 1 } ^ { a }$ where $b = { \frac { 1 } { 1 2 } } + \epsilon$ , we get

$$
\mu ^ { * } ( K _ { Y _ { 1 } ^ { a } } + G + ( 1 8 - n ) a A ^ { a } + ( 6 + n ) a f ^ { a } ) = K _ { Y _ { 1 } ^ { b } } + G ^ { b } + ( 1 8 - n ) a A ^ { b } + ( 6 + n ) a f ^ { b } + ( 1 8 - n ) a A ^ { c } + ( 1 8 - n ) a A ^ { c } .
$$

![](images/36c91fbc693ab653f2be7ebd8fae6183a4cafe5b1b5ed95d6619230ce59a112c.jpg)  
Figure 4. Illustration of Example 6.6

As above, $A ^ { b }$ is the curve obtained by flipping the section $S _ { 0 }$ of $Y _ { 0 } ^ { 1 }$ which is a rational curve with self intersection $- \frac { 3 } { 2 }$ since $Y _ { 0 } ^ { 1 }$ has a twisted $\mathrm { I } _ { n } ^ { * }$ fiber.
Thus we can compute that $( A ^ { b } ) ^ { 2 } = - \frac { 2 } { 3 }$ , $\begin{array} { l } { { A ^ { b } . G ^ { b } = \frac { 1 } { 3 } } } \end{array}$ and $( G ^ { b } ) ^ { 2 } = - { \frac { 1 } { 6 } }$ .
Using push-pull for the contraction $\rho : Y _ { 1 } ^ { b }  Y _ { 1 } ^ { 1 }$ onto the model of $Y _ { 1 } ^ { 1 }$ with a twisted $\mathrm { N } _ { 1 }$ for the double locus and a Weierstrass N $^ { 1 }$ for the other $\mathrm { N _ { 1 } }$ , we get that $K _ { Y _ { 1 } ^ { b } } = - f ^ { b } + A ^ { b }$ .
Putting all these together and using push-pull for $\mu$ we get that

$$
\begin{array} { l } { { \displaystyle { \mathrm {  ~ \ell ~ } } ^ { \prime } + G + ( 1 8 - n ) a A ^ { a } + ( 6 + n ) a f ) . A ^ { a } = ( K _ { Y _ { 1 } ^ { b } } + G ^ { b } + ( 1 8 - n ) a A ^ { b } + ( 6 + n ) a f ^ { b } + 1 2 a ( 1 8 - n ) a ^ { a } { \cal A } ^ { b } } } \\ { ~ } \\ { { \displaystyle ~ = \frac { 2 a n } { 3 } - \frac { 1 } { 3 } } } \\ { { \mathrm {  ~ \ell ~ } } ^ { \prime } + G + ( 1 8 - n ) a A ^ { a } + ( 6 + n ) a f ) . B ^ { a } = ( K _ { Y _ { 1 } ^ { b } } + G ^ { b } + ( 1 8 - n ) a { \cal A } ^ { b } + ( 6 + n ) a f ^ { b } + 1 2 a ( 1 8 - n ) a { \cal A } ^ { b } }  \\ { ~ } \\ { { \displaystyle ~ = \frac { 1 } { 6 } + ( 1 8 - n ) \frac { a } { 3 } . } } \end{array}
$$

For $\begin{array} { r } { a < \frac { 1 } { 2 n } } \end{array}$ , there is an extremal contraction of the curve class of $A ^ { a }$ in $\mathcal { X } ^ { a }$ .
On the other hand, since $( A ^ { b } ) ^ { 2 } = - \frac { 2 } { 3 }$ and $\mu$ is the contraction of a $- 2$ curve which intersects $A ^ { b }$ transversely, we have $( A ^ { a } ) ^ { 2 } = - \frac { 1 } { 6 }$ so this curve class is rigid and therefore undergoes a flip.
After the flip the strict transform $Y _ { 1 } ^ { a }$ for $\begin{array} { r } { a < \frac { 1 } { 2 n } } \end{array}$ is now a pseudoelliptic attached along an intermediate pseudofiber of $Y _ { 0 } ^ { a }$ By Lemma 5.13, the flipped pseudoelliptic contracts and goes through a Type WIII pseudoelliptic flip for some small $a = \epsilon > 0$ giving the stable limit as the minimal Weierstrass pseudoelliptic of $Y _ { 0 } ^ { a }$ .

Remark 6.9. By e.g. [Shi03], the maximum $n$ such that there exists an elliptic K3 with an $\mathrm { I } _ { n } ^ { * }$ is 14 and so the above phenomena occur for $6 < n \le 1 4$ .

Combining these examples above we get the following:

# Proposition 6.10.

(1) There are type III walls at $\frac { 1 } { k }$ for $1 3 \leq k \leq 1 9$ where the isotrivial $j$ -invariant $\infty$ main component of the surfaces from Theorem 5.16 case (d) contract as a ruled surface onto the $\mathbf { l } _ { n }$ fiber of the pseudoelliptic K3 sprouting off of it.

![](images/3f69465b8abb11567a306a12695c81a43c099b81e28155b7a3ace0f33c0ca969.jpg)  
Figure 5. Illustration of Example 6.8

(2) There are type III walls at $\textstyle { \frac { 1 } { 2 n } }$ for $6 < n \le 1 4$ where the isotrivial $j$ -invariant $\infty$ main component as in Theorem 5.16 case (e) goes through a flip to become a pseudoelliptic attached to an intermediate model of the $\mathrm { I } _ { n } ^ { * }$ on the $K 3$ component.
At some smaller $a = \epsilon > 0$ , this pseudoelliptic contracts onto the Weierstrass model of the $\mathrm { I } _ { n } ^ { * }$ fiber.

Corollary 6.11. The stable replacement in $\overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ of the two main component surfaces of $\overline { { \mathcal { W } } } _ { \sigma } ( \frac { 1 } { 1 2 } + \epsilon )$ from Theorem 5.19 (d) and (e) is a pseudoelliptic $K \mathcal { 3 }$ with a Weierstrass $\mathrm { I } _ { n }$ respectively $\mathrm { I } _ { n } ^ { * }$ fiber.

Proposition 6.12. If $X$ is a surface parametrized by $\overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ then $\omega _ { X } \cong { \mathcal { O } } _ { X }$ .

Proof.
If $X$ is irreducible then the result is clear since $X$ is the contraction of the section, a $\left( - 2 \right)$ -curve, on a K3 type Weierstrass fibration.

Therefore, suppose $X$ is consists of multiple components.
Let $p : \mathcal { X }  D$ be a 1-parameter family over the spectrum of a DVR with generic fiber a $2 4 \mathrm { { I } _ { 1 } }$ elliptic K3 and central fiber $X$ .
Now there is a sequence of pseudoelliptic flips producing a model $p ^ { \prime } : \mathcal { X } ^ { \prime }  D$ where the sections of $X$ are blown back up so that the components of central fiber $X ^ { \prime }$ of $p ^ { \prime }$ are all elliptically fibered and glued along twisted fibers (for example these flips occur as part of the MMP when decreasing the coefficient on the section of the twisted model, or equivalently, $X ^ { \prime }$ is the model parametrized by the Brunyate/Inchiostro moduli space).
Then $X ^ { \prime } = X _ { 0 } \cup _ { F _ { 0 } } X _ { 1 } , \ldots , \cup X _ { n } \cup _ { F _ { n } } X _ { n + 1 }$ , where $X _ { 0 }$ and $X _ { n + 1 }$ are rational elliptic surfaces, and $X _ { 1 } , \ldots , X _ { n }$ are trivial $j$ -invariant $\infty$ fibrations.

Then $K _ { X ^ { \prime } } | _ { X _ { 0 } } = K _ { X _ { 0 } } + F _ { 0 }$ , $K _ { X ^ { \prime } } | _ { X _ { n + 1 } } = K _ { X _ { n + 1 } } + F _ { n }$ , and $K _ { X } | _ { X _ { i } } = K _ { X _ { i } } + F _ { i - 1 } + F _ { i }$ for $i = 1 , \ldots , n$ which are all $0$ by the canonical bundle formula since $X _ { 0 } , X _ { n + 1 }$ (resp.
$X _ { 1 } , \ldots , X _ { n } $ ) satisfy $\deg \mathbb { L } = 1$ (resp.
$\mathrm { d e g } \mathbb { L } = 0$ ).
Thus $K _ { X ^ { \prime } }$ is numerically trivial, that is, $K _ { X ^ { \prime } } \equiv 0$ .

We proceed in two steps – first we show that $X ^ { \prime }$ is Gorenstein and then we show that the pullback

$$
\operatorname { P i c } ( X ^ { \prime } ) \to \bigoplus _ { i = 0 } ^ { n + 1 } \operatorname { P i c } ( X _ { i } )
$$

is injective.
For the first claim, note that away from the gluing fibers $F _ { i }$ , the surface $X ^ { \prime }$ is a minimal Weierstrass fibration.
From the classification of surfaces (e.g. see Corollary 6.11), the components

$X _ { i }$ are glued along $\mathbf { l } _ { n }$ type fibers and so in a neighborhood of $F _ { i }$ , the surface corresponds to a map from a non-stacky nodal curve into $\overline { { \mathcal { M } } } _ { 1 , 1 }$ .
In particular, in a neighborhood of $F _ { i }$ , the elliptic fibration $X ^ { \prime }  C$ is a flat family of nodal curves over a nodal curve.
In either case, $X ^ { \prime }$ is Gorenstein.

Next denote by $\pi : \sqcup X _ { i } \to X ^ { \prime }$ the natural morphism.
By [HP15, Proposition 2.6, Remark 2.7] there is a diagram of short exact sequences of sheaves of abelian groups on $X ^ { \prime }$

$$
\begin{array} { r l } { 1 \longrightarrow \mathbb { O } _ { X ^ { \prime } } ^ { * } \longrightarrow \underset { \begin{array} { l } { \between \atop \end{array} } } { \overset { \alpha } { \longrightarrow } } \prod _ { i = 0 } ^ { n + 1 } \pi _ { * } \mathbb { O } _ { X _ { i } } ^ { * } \longrightarrow \mathbb { N } \longrightarrow 0 } \\ { 1 \longrightarrow \mathbb { O } _ { F ^ { \prime } } ^ { * } \xrightarrow [ ] { \beta } } & { \underset { \ast } { \overset { \alpha } { \longrightarrow } } \mathbb { N } \longrightarrow 0 } \end{array}
$$

where $F ^ { \prime }$ is the double locus on $X ^ { \prime }$ and $F$ is the double locus on $X _ { i }$ .
Note that as an abstract variety, $F$ is the disjoint union of two copies of $F ^ { \prime }$ .
By [HP15, Proposition 4.2], the map (4) is injective if and only if $\gamma : \operatorname { P i c } ( F ^ { \prime } ) \to \operatorname { P i c } ( F )$ is injective and $\mathrm { c o k e r } H ^ { \cup } ( \alpha ) = \mathrm { c o k e r } H ^ { \cup } ( \beta )$ .
The map $\gamma$ is simply the diagonal so it is injective.
Moreover, since $X ^ { \prime }$ , $X _ { i }$ and $F _ { i }$ are all connected projective varieties, taking $H ^ { 0 }$ of the above diagram gives

$$
\begin{array} { r l } & { 1 \longrightarrow k ^ { * } \xrightarrow { \qquad H ^ { 0 } ( \alpha ) } \prod _ { i = 0 } ^ { n + 1 } k ^ { * } } \\ & { ~ \xrightarrow { \qquad f _ { 1 } \bigg \downarrow } \qquad } \\ & { 1 \longrightarrow \prod _ { i = 0 } ^ { n } k ^ { * } \xrightarrow { \qquad H ^ { 0 } ( \beta ) \large } \prod _ { i = 0 } ^ { n } k ^ { * } \times k ^ { * } . } \end{array}
$$

Here $f _ { 1 }$ and $H ^ { 0 } ( \alpha )$ are the diagonal maps, $H ^ { 0 } ( \beta )$ is the product of diagonal maps for each $i$ , and $f _ { 2 }$ is given by $( x _ { 0 } , \ldots , x _ { n + 1 } ) \mapsto ( x _ { 0 } , x _ { 1 } , x _ { 1 } , x _ { 2 } , \ldots , x _ { n } , x _ { n + 1 } )$ .
The cokernel of $H ^ { 0 } ( \alpha )$ can be identified with $\Pi _ { i = 1 } ^ { n + 1 } k ^ { * }$ by the map $( x _ { 0 } , \ldots , x _ { n + 1 } ) \mapsto ( x _ { 1 } / x _ { 0 } , \ldots , x _ { n + 1 } / x _ { 0 } )$ .
Similarly, the cokernel of $H ^ { 0 } ( \beta )$ can be identified with $\Pi _ { i = 0 } ^ { n } k ^ { * }$ by the map $( a _ { 0 } , b _ { 0 } , a _ { 1 } , b _ { 1 } , \ldots , a _ { n } , b _ { n } ) \mapsto ( b _ { 0 } / a _ { 0 } , b _ { 1 } / a _ { 1 } , \ldots , b _ { n } / a _ { n } )$ .
Putting this together, we see the induced map on cokernels is given by $( x _ { 1 } , \ldots , x _ { n + 1 } ) \mapsto$ $( x _ { 1 } , x _ { 2 } / x _ { 1 } , \ldots , x _ { n + 1 } / x _ { n } )$ which is an isomorphism.
Thus we conclude that (4) is an injection.

Putting it all together, we have that $X ^ { \prime }$ is Gorenstein and $\omega _ { X ^ { \prime } }$ pulls back to the trivial line bundle under (4) so $\omega _ { X ^ { \prime } } \cong \operatorname { \langle \langle } ) _ { X ^ { \prime } }$ .
It follows that $\omega _ { \mathcal { X } ^ { \prime } / D } \cong \mathcal { O } _ { \mathcal { X } ^ { \prime } }$ .
Now $\mathcal { X } ^ { \prime }$ is related to $\mathcal { X }$ by a sequence of log flips.
Since these flips always contract $K$ -trivial curves, we conclude from the Cone Theorem (e.g. [KM98, Theorem 3.7 (4)]) that the canonical is preserved so $\omega \mathcal { X } \cong \mathcal { O } \mathcal { X }$ so $\omega _ { X } \cong { \mathfrak { O } } _ { X }$ .
$\boxed { \begin{array} { r l } \end{array} }$

Putting all of this together, we have a classification of the boundary components of $\mathcal { W } _ { \sigma } ( \epsilon )$ (see Section 7 for an alternate description).

Theorem 6.13. The surfaces in $\overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$ are the following:

(A) An irreducible pseudoelliptic $K \mathcal { 3 }$ with the section contracted to an $A _ { 1 }$ singularity and minimal Weierstrass pseudofibers.  
(B) An irreducible isotrivial $j = \infty$ pseudoelliptic with 4N $^ { 1 }$ Weierstrass fibers.  
(C) An isotrivial $j = \infty$ fibration with 2N $^ { 1 }$ Weierstrass fibers and an $\mathrm { N _ { 2 } }$ intermediate fiber with a tree of pseudoelliptics sprouting off of it.  
(D) An isotrivial $j = \infty$ fibration with 2N $^ 2$ intermediate fibers each sprouting a tree of pseudoelliptics.  
(E) A union of irreducible pseudoelliptic rational surfaces along an I0 fiber.  
(F) A union of isotrivial $j = \infty$ pseudoelliptic surfaces with a single intermediate N $2$ fiber sprouting a pseudoelliptic tree on each, glued along an N0 fiber.  
(G) A union of irreducible isotrivial $j = \infty$ surfaces each with $\mathrm { 2 N _ { 1 } }$ Weierstrass fibers glued along an $\mathrm { N } _ { 0 }$ fiber.

(H) $A$ union of an irreducible isotrivial $j = \infty$ surface with 2N $^ { 1 }$ Weierstrass fibers and an isotrivial $j = \infty$ surface with a single N $^ 2$ fiber sprouting a pseudoelliptic tree, glued along an $\mathrm { N } _ { 0 }$ fiber.

Furthermore, every surface $X$ satisfies $\omega _ { X } \cong { \mathcal { O } } _ { X }$ and $\mathrm { H } ^ { 1 } ( \mathrm { X } , { \mathcal { O } } _ { \mathrm { X } } ) = 0$ .
Finally the number of marked N $_ 0$ fibers are as in Theorem 5.16 and Theorem 5.19.

Now we show that each surface actually appears on the boundary, using the full smoothability results of Section 3.2.

Theorem 6.14. Every slc surface pair in Theorem 6.13 appears in the boundary of $\overline { { \mathscr { W } _ { \sigma } ( \epsilon ) } }$ .

Proof.
Given any surface satisfying the conditions of Theorem 6.13, we can construct a twisted surface whose stable replacement is the surface obtained by flipping the pseudoelliptic components into elliptically fibered ones as in the previous section, replacing each cuspidal fiber by a twisted fiber, and attaching a component with dual monodromy satisfying the conditions of Propositions 3.23 & 3.26 to each of these twisted fibers.
By the full smoothability Theorems $3 . 2 4 \ \& \ 3 . 2 8$ , this twisted model is the limit of a family of $2 4 1 _ { 1 }$ elliptic K3 surfaces with singular fibers marked and its stable replacement must be the initial surface as computed in the previous two sections.
$\boxed { \begin{array} { r l } \end{array} }$

We conclude this section by discussion the connection between $\overline { { \mathrm { W } } } _ { \sigma } ( \epsilon )$ and the GIT quotient ${ \overline { { \mathrm { W } } } } ^ { G }$

Theorem 6.15 (Connection with GIT/SBB).
If $\mathrm { W } _ { \sigma } ( \epsilon )$ denotes the coarse space of $\mathcal { W } _ { \sigma } ( \epsilon )$ , then there is a morphism $\overline { { \mathrm { W } } } _ { \sigma } ( \epsilon )  \overline { { \mathrm { W } } } ^ { G } \cong \overline { { \mathrm { W } } } ^ { * }$ with the following structure:

(1) The locus of surfaces of type (2) The locus of surfaces of type ( ) maps isomorphica) maps as a generic onto -bund $\mathrm { W } _ { s } ^ { G }$ .nto by forgetting the $B$ $\mathbb { P } ^ { 1 2 }$ $\overline { { \mathbb { W } } } _ { s l c , o } ^ { G }$ marked fibers.
The closure of this locus in $\overline { { \mathrm { W } } } _ { \sigma } ( \epsilon )$ parametrizes the unique surface of type ( $G$ ) along with a choice of marked fibers and this locus all maps onto $\overline { { \mathrm { W } } } _ { s l c } ^ { G } \cap \overline { { \mathrm { W } } } _ { L } ^ { G }$ .
(3) The locus of surfaces of type ( $E$ ) maps onto $\overline { { \mathrm { W } } } _ { L } ^ { G }$ by taking the $j$ -invariant of the $\mathrm { I _ { 0 } }$ fiber along which the two components are glued.
(4) The surfaces of type ( $\psi$ ), ( $D$ ), ( $F ^ { \prime }$ ), and ( $H$ ) all get mapped onto the point $\overline { { \mathrm { W } } } _ { s l c } ^ { G } \cap \overline { { \mathrm { W } } } _ { L } ^ { G }$ .

Proof.
By Theorem 6.13, we have a classification of surfaces in $\overline { { \mathscr { W } _ { \sigma } ( \epsilon ) } }$ .
Each of the irreducible surfaces mentioned in the theorem are also parametrized by $\overline { { \mathrm { W } } } ^ { * }$ yielding a rational map $\overline { { \mathrm { W } } } _ { \sigma } ( \epsilon )  \overline { { \mathrm { W } } } ^ { G }$ defined on a dense open subset.
Now one can easily check that the limit in ${ \overline { { \mathrm { W } } } } ^ { G }$ of a Weierstrass family limiting to a surface of type (B) (resp.
of type (C), (D), (G), (F) and (H)) is the $j$ -invariant of the L (resp.
N $^ 2$ ) fiber in $\overline { { \mathrm { W } } } _ { L } ^ { G }$ .
This depends only the central fiber of the family, not the family itself, so the morphism extends uniquely by normality after applying [GG14, Theorem 7.3].
$\boxed { \begin{array} { r l } \end{array} }$

# 7. Explicit description of the boundary of $\overline { { \mathcal { W } } } _ { \sigma } ( \epsilon )$

In the previous section, specifically Theorems 6.13 and 6.14, we gave an explicit description of the surfaces parametrized by the boundary of $\overline { { \mathscr { W } } } _ { \sigma } ( \epsilon )$ .
The goal of this section, is to enumerate the resulting boundary strata of $\overline { { \mathscr { W } _ { \sigma } ( \epsilon ) } }$ in a combinatorial way, and akin to Kulikov models (see Proposition 7.2 for the analogue of Type $I I$ degenerations, and Theorems 7.5, 7.7, and 7.9 for the analogues of the Type III degenerations).

Before starting, we define $R _ { n }$ to be the space parametrizing pairs $( X , S + F )$ , where $X$ is a minimal Weierstrass rational elliptic surface, $S$ is a section, and $F$ is a fiber of type $\mathrm { I } _ { n }$ .
Note $n \leq 9$ .
The following is well known.

Lemma 7.1. [HL02, Section 3.3] $R _ { n }$ is a $9 - n$ dimensional affine variety which is irreducible for $n \neq 8$ while $R _ { 8 }$ has two components.

Using these spaces, we will explicitly describe the boundary of $\overline { { \mathscr { W } } } _ { \sigma } ( \epsilon )$ .
To do so, we use the notation of Kulikov models (i.e. type II and type III).

7.1. Type II degenerations.
We begin with the Type II degenerations.

Proposition 7.2. There are two Type II strata described as follows.

(1) A dim.
17 stratum WII isomorphic to a quotient of the fiber product $R _ { 0 } \times _ { j } R _ { 0 }$ : namely the self fiber product of the $j$ -map $j : R _ { 0 } \to \mathbb { A } ^ { 1 }$ .
A point parametrizes two rational elliptic surfaces with a marked $\mathrm { I _ { 0 } }$ fiber of the same $j$ -invariant glued along this fiber and the quotient comes from swapping the two surfaces ( $( E )$ in Theorem 6.13).  
(2) A dim.
17 stratum $\mathrm { W } _ { \mathrm { I I } } ^ { \infty } \cong \mathrm { S y m } ^ { 1 6 } ( \mathbb { P } ^ { 1 } ) \times \mathbb { A } ^ { 1 }$ where A1 is the $j$ -line.
The $j$ -line parametrizes the $\mathrm { 4 N _ { 1 } }$ isotrivial $j$ -invariant $\infty$ component and Sym $\mathbb { \Lambda } ^ { 1 6 } ( \mathbb { P } ^ { 1 } )$ parametrizes the m markings on this surface other than the $\mathrm { N _ { 1 } }$ fibers counted with multiplicity (Theorem 6.13 $B$ ).

7.2. Type III degenerations.
We now discuss the type III degenerations.
The first step is to “un-flip” the pseudoelliptic components in the description in Theorem 6.13. After, we can describe each surface as a chain $X _ { 0 } \cup \ldots \cup X _ { n + 1 }$ , where both $X _ { 0 }$ and $X _ { n + 1 }$ are Weierstrass fibrations of rational type (i.e. $\deg \mathcal { L } = 1$ ), and $X _ { 1 } , \ldots , X _ { n }$ are all isomorphic to trivial $j$ -invariant $\infty$ fibrations $C \times \mathbb { P } ^ { 1 }$ , with $C$ being a nodal cubic.
These surfaces are all glued along nodal cubic fibers (i.e. either $\mathbf { l } _ { n }$ or $\mathrm { N } _ { 0 }$ fibers).
Further, each $X _ { i }$ for $i = 1 , \ldots , n$ must have at least one marked fiber by stability.
We call the surfaces $X _ { 0 }$ and $X _ { n + 1 }$ the end components and $X _ { 1 } , \ldots , X _ { n }$ the intermediate components.

Lemma 7.3. An end component must have at least (a) 3 marked fibers if it is normal, or (b) 4 marked fibers if it is isotrivial $j$ -invariant $\infty$ , counted with multiplicity.

Proof.
If an end component is an isotrivial $j$ -invariant $\infty$ surface, then it must be 2N $^ { 1 }$ fibration glued along an N $_ 0$ fiber.
Each N $\bot$ must carry at least 2 markings counted with multiplicity so the surface carries at least 4. If it is a normal rational elliptic surface, then the number of markings is given by $1 2 - n$ where the surface is glued along an $\mathrm { I } _ { n }$ fiber.
Since $n \leq 9$ for $I _ { n }$ fibers on a rational elliptic surface, then there are at most 3 markings on such a component.


Corollary 7.4. For the chains $X _ { 0 } \cup \ldots \cup X _ { n + 1 }$ in the Type III locus, n is at most 18.

Proof.
As there is $\geq 1$ marking on each of the intermediate components, the number of components is bounded by the number of markings not on $X _ { 0 }$ and $X _ { n + 1 }$ .
By Lemma 7.3, there are $\geq 6$ combined on these components so $\leq 1 8$ markings to be distributed among the intermediate components.
$\boxed { \begin{array} { r l } \end{array} }$

Now we will describe an explicit parameterization of each of the Type III strata.
There are three cases depending on whether none, one, or both of the end components $X _ { 0 }$ and $X _ { n + 1 }$ are isotrivial $j$ -invariant $\infty$ .
We call these strata of type III $_ 0$ , $\mathrm { I I I } _ { 1 }$ and $\mathrm { { I I I } _ { 2 } }$ respectively.
The type $\mathrm { I I I } _ { 0 }$ strata are further indexed by the fiber types $\boldsymbol { \mathrm { I } } _ { r }$ and $1 _ { s }$ along which $X _ { 0 }$ and $X _ { n + 1 }$ are glued.
In this case, there are $1 2 - r$ and $1 2 - s$ fibers marked on $X _ { 0 }$ and $X _ { n + 1 }$ respectively which gives us $( r + s )$ markings remaining for the middle components $X _ { 1 } , \ldots , X _ { n }$ .
Thus, $n$ must satisfy $1 \leq n \leq ( r + s )$ .

Finally, for each $n$ , we can fix a single marking on each component $X _ { 1 } , \ldots , X _ { n }$ and fix coordinates so that the components are glued along fibers at $0 , \infty$ and the chosen marking is at 1. That gives us freedom to parametrize $\boldsymbol { r } + \boldsymbol { s } - \boldsymbol { n }$ additional markings among the $X _ { 1 } , \ldots , X _ { n }$ .
For each choice of partition $\textstyle \sum _ { i = 1 } ^ { n } a _ { i } = r + s - n$ we can consider the stratum where there are $a _ { i }$ markings on $X _ { i }$ .

Theorem 7.5 (Type III $_ 0$ locus).
Fix data

$$
1 \leq r , s \leq 9 , \quad 1 \leq n \leq r + s , \quad \sum _ { i = 1 } ^ { n } a _ { i } = r + s - n ,
$$

$A$ $\operatorname { I I I } _ { 0 , a _ { 1 } , \dots , a _ { n } } ^ { r , s , n }$ of oint $\dim ( \mathrm { I I I } _ { 0 , a _ { 1 } , \ldots , a _ { n } } ^ { r , s , n } ) = 1 8 - n$ with a finite parameterirmines the surface pairs $R _ { s } \times \mathbb { G } _ { m } ^ { a _ { 1 } } \times . . . \times \mathbb { G } _ { m } ^ { a _ { n } } \times R _ { r }$ $X _ { 0 } , X _ { n + 1 }$ as well as the configuration of $a _ { i }$ marked fibers on the $X _ { 1 } , \ldots , X _ { n }$ avoiding the double locus.

Remark 7.6. Just to reiterate, the $R _ { s }$ and $R _ { r }$ parametrize the surfaces $X _ { 0 }$ and $X _ { n + 1 }$ respectively, and the $\mathbb { G } _ { m } ^ { a _ { i } }$ parametrize the marked fibers on $X _ { i }$ avoiding the double locus.

Next, we consider type $\operatorname { I I I } _ { 1 }$ strata where exactly one of the end surfaces, without loss of generality $X _ { 0 }$ , is an isotrivial $j$ -invariant $\infty$ surface of rational type.
Then $X _ { 0 }$ must be the $2 \mathrm { N } _ { 1 }$ surface glued along an $\mathrm { N } _ { 0 }$ fiber.
There are 2 markings each on the N $^ { 1 }$ fibers for a total of 4. Then for each $0 \leq s \leq 1 7$ , there is a stratum with $1 7 - s$ marked N $_ 0$ fibers on $X _ { 0 }$ (c.f.
Theorem 5.16). After picking coordinates so that the N $^ { 1 }$ fibers are at $0$ and 1 and the double locus is at $\infty$ , these $1 7 - s$ markings must avoid $\infty$ and so give a a factor of $\mathbb { A } ^ { 1 7 - s }$ parametrizing $X _ { 0 }$ .
The other end component $X _ { n + 1 }$ is a rational elliptic surface glued along an $1 _ { r }$ fiber for some $r$ and with $1 2 - r$ marked fibers.

This gives $3 3 - s - r$ total markings on $X _ { 0 }$ and $X _ { n + 1 }$ .
On the other hand, there are at most 24 markings so $3 3 - s - r \leq 2 4$ .
In the case of equality, there are no intermediate components and we have a stratum parametrized by $\mathbb { A } ^ { 1 7 - s } \times R _ { r }$ .
Otherwise, we have $1 \leq n \leq s + r - 9$ intermediate components with $s + r - 9$ markings distributed on them.
After fixing one marking on each intermediate component at coordinate 1, there are $r + s - 9 - n$ marked fibers partitioned into $\textstyle \sum _ { i = 1 } ^ { n } a _ { i } = r + s - 9 - n$ .
This gives a finite parameterization by $\mathbb { A } ^ { 1 7 - s } \times \mathbb { G } _ { m } ^ { a _ { 1 } } \times \ldots \times \mathbb { G } _ { m } ^ { a _ { n } } \times R _ { r }$ .

Theorem 7.7 (Type III1 locus).

(1) Fix the data

$$
1 \leq r \leq 9 , \quad 0 \leq s \leq 1 7 , \quad s + r = 9
$$

There is a type $\operatorname { I I I } _ { 1 }$ stratum $\mathrm { I I I } _ { 1 } ^ { r , s }$ of $\dim ( \mathrm { I I I } _ { 1 } ^ { r , s } ) \ : = \ : 1 7$ with a finite parameterization by $\mathbb { A } ^ { 1 7 - s } \times R _ { r }$ .

(2) Fix the data

$$
1 \leq r \leq 9 , \quad 1 \leq s \leq 1 7 , \quad 1 \leq n \leq s + r - 9 , \quad \sum _ { i = 1 } ^ { n } a _ { i } = r + s - 9 - n .
$$

There is a type $\operatorname { I I I } _ { 1 }$ stratum $\operatorname { I I I } _ { 1 , a _ { 1 } , \dots , a _ { n } } ^ { r , s , n }$ of $\dim ( \operatorname { I I I } _ { 1 , a _ { 1 } , \dots , a _ { n } } ^ { r , s , n } ) = 1 7 - n$ with a finite pamaterization by $\mathbb { A } ^ { 1 7 - s } \times \mathbb { G } _ { m } ^ { a _ { 1 } } \times \ldots \times \mathbb { G } _ { m } ^ { a _ { n } } \times R _ { r }$ .

Remark 7.8. Again, here $\mathbb { A } ^ { \times - s }$ parametrizes the $8 - s$ marked $\mathrm { N } _ { 0 }$ on $X _ { 0 }$ , the $\mathbb { G } _ { m } ^ { a _ { i } }$ parametrizes the marked N $_ 0$ on the $X _ { i }$ , and $R _ { r }$ parametrizes the surface $X _ { n + 1 }$ .

Finally, we have the type $\mathrm { I I I _ { 2 } }$ stratum where both $X _ { 0 }$ and $X _ { n + 1 }$ are isotrivial $j$ -invariant $\infty$ In this case both $X _ { 0 }$ and $X _ { n + 1 }$ are described by an affine space of dimension $1 7 - s$ and $1 7 - r$ respectively, where there are $1 7 - s$ and $1 7 - r$ marked $\mathrm { N } _ { 0 }$ fibers on $X _ { 0 }$ and $X _ { n + 1 }$ in addition to the $2 \mathrm { N } _ { 1 }$ which each appear with multiplicity 2. This gives $4 2 - r - s$ total marked fibers among the end components, so $4 2 - r - s \leq 2 4$ and we again have two cases: this is an equality and there are no intermediate components, or this inequality is strict and there are intermediate components with $r + s - 1 8$ marked fibers.
Thus, as before so we obtain the following:

Theorem 7.9 (Type III2 locus).

(1) Fix the data

$$
0 \leq s , r \leq 1 7 , \quad s + r = 1 8
$$

There is a Type $\mathrm { I I I _ { 2 } }$ stratum $\mathrm { I I I } _ { 2 } ^ { r , s }$ of $\dim ( \mathrm { I I I } _ { 2 } ^ { r , s } ) \ : = \ : 1 6$ with a finite parameterization by $\mathbb { A } ^ { 1 7 - s } \times \mathbb { A } ^ { 1 7 - s } = \mathbb { A } ^ { 1 6 }$ .

(2) Fix the data

$$
1 \leq s , r \leq 1 7 , \quad 1 \leq n \leq s + r - 1 8 \quad \sum _ { i = 1 } ^ { n } a _ { i } = r + s - n - 1 8 .
$$

There is a Type III2 stratum $\operatorname { I I I } _ { 2 , a _ { 1 } , \dots , a _ { n } } ^ { r , s , n }$ of $\dim ( \mathrm { I I I } _ { 2 , a _ { 1 } , \ldots , a _ { n } } ^ { r , s , n } ) = 1 6 - n$ with a finite parameterization by $\mathbb { A } ^ { 1 7 - s } \times \mathbb { G } _ { m } ^ { a _ { 1 } } \times \ldots \times \mathbb { G } _ { m } ^ { a _ { n } } \times \mathbb { A } ^ { 1 7 - r }$ .

Remark 7.10. In the above theorem, the $\mathbb { A } ^ { 1 7 - s }$ (resp.
A $_ { 1 7 - r }$ ) parametrize the markings on $X _ { 0 }$ (resp.
$X _ { n + 1 }$ ), and the $\mathbb { G } _ { m } ^ { a _ { i } }$ parametrize the markings on $X _ { i }$ .

# 8. The spaces with one marked fiber

The goal of this section is to describe the surfaces parametrized by the boundary of the moduli spaces $\overline { { \mathcal { K } } } _ { \epsilon }$ (resp.
$\overline { { \mathcal { F } } } _ { \epsilon }$ ), i.e. the moduli spaces parametrizing one $\epsilon$ -marked singular fiber (resp.
any fiber).
In Section 8.1 we describe the boundary of the two moduli spaces (see Theorem 8.1). In Section 8.2 we prove Theorem 8.2, which describes a morphism from $\overline { { \mathcal { K } } } _ { \epsilon }$ to ${ \overline { { \mathrm { W } } } } ^ { G }$ .
Finally, in Section 8.3 we extend Miranda’s GIT construction to produce a moduli space of Weierstrass surfaces with a choice of marked fiber.
The main result in this direction is Theorem 8.8, which shows that $\overline { { \mathcal { F } } } _ { \epsilon }$ is a smooth Deligne-Mumford stack with coarse space map $\overline { { \mathcal { F } } } _ { \epsilon }  \widetilde { \mathrm { W } } ^ { G }$ given by the extended GIT compactification we discuss in Section 8.3.

8.1. The spaces with one marked fiber.
In this section we first consider the moduli space $\overline { { \mathcal { F } } } _ { \epsilon }$ (see Definition 4.9), which corresponds to marking only one (possibly singular) fiber with $\epsilon$ weight.
In particular, we give a description of the surfaces parametrized by the boundary.
Note that since $\overline { { \mathcal { K } } } _ { \epsilon }$ is a slice of $\overline { { \mathcal { F } } } _ { \epsilon }$ , this description also applies to the surfaces parametrized by $\overline { { \mathcal { K } } } _ { \epsilon }$ .

Theorem 8.1 (Characterization of the boundary).
The surfaces parametrized by $\overline { { \mathcal { F } } } _ { \epsilon }$ are single component pseudoelliptic $K \mathcal { 3 }$ surfaces whose corresponding elliptic surfaces are semi-log canonical Weierstrass elliptic K3s, and the marked fiber $F$ can be any fiber other than an $L$ type cusp.
Moreover, all surfaces parametrized by $\overline { { \mathcal { F } } } _ { \epsilon }$ satisfy $\mathrm { H } ^ { 1 } ( X , { \mathcal { O } } _ { X } ) = 0$ and $\omega _ { X } \cong { \mathfrak { O } } _ { X }$ .

Proof.
We follow the explicit stable reduction process explained in e.g. [AB21a, Section 6].
Let ( $f : \mathcal { X }  \mathcal { C } , \mathcal { S } + \mathcal { F } )  T$ be a 1-parameter family whose generic fiber $f : X _ { \eta } \to C _ { \eta } , S _ { \eta } + F _ { \eta } )$ is a Weierstrass elliptic K3 surface with $2 4 ~ \mathrm { { I } _ { 1 } }$ fibers, and a single (possibly singular) marked fiber $F _ { \eta }$ Denote by ( $f _ { 0 } : X _ { 0 } \to C _ { 0 } , S _ { 0 } + F _ { 0 } )$ the special fiber, and consider the limit obtained via twisted stable maps (see e.g. [AB19]).
The limit ( $f _ { 0 } : X _ { 0 } ^ { \prime } \to C _ { 0 } ^ { \prime } , S _ { 0 } ^ { \prime } + F _ { 0 } ^ { \prime } )$ , will be a tree of elliptic fibrations glued along twisted fibers, and the closure of the fiber $F$ will be contained in precisely one such surface component.
While this surface will be stable as a map to $\mathcal { \mathrm { M } } _ { 1 , 1 }$ , it will not necessarily be stable as a surface pair.
To resolve this, pick some generic choice of markings $G = \cup _ { i \in I } G _ { i }$ to make the above limit stable as a surface pair.
In this case, $G$ will consist of generic smooth fibers.

As we (uniformly) lower the coefficients marking $G$ towards 0, there will be some choice of coefficient so that the weighted stable base curve is an irreducible rational curve.
Indeed, the components of the base curve will contract precisely when there is not enough weight being supported on the marked fibers.
As we only lowered the coefficients marking $G$ , and the fiber $F _ { 0 } ^ { \prime }$ remained marked with coefficient one, the (unique) main component, call it $Y _ { 0 }$ fibered over the rational curve will contain the original marked fiber.

Now we have a single main component with marked fiber $F _ { 0 } ^ { \prime }$ with Type I pseudoelliptic trees attached to it.
When the coefficients of $G$ are set to 0 the Type I trees will undergo Type WIII contractions to a point to produce the Weierstrass model of $Y _ { 0 }$ , away from the fiber $F _ { 0 } ^ { \prime }$ .
When the coefficient of $F _ { 0 } ^ { \prime }$ is reduced to $0 < \epsilon \ll 1$ , it will cross $\mathrm { W _ { I } }$ walls to become a Weierstrass fiber.

We saw in Proposition 4.11 that $\mathrm { H } ^ { 1 } ( \mathrm { X } , { \mathcal { O } } _ { \mathrm { X } } ) = 0$ , so it suffices to show that $\omega _ { X } \cong { \mathfrak { O } } _ { X }$ .
This holds on any Weierstrass elliptic K3 surface (see [Mir89, Proposition III.1.1]), and since $X$ is obtained from a Weierstrass elliptic K3 by contracting a $\left( - 2 \right)$ curve (the section), we have $\omega _ { X } \cong { \mathfrak { O } } _ { X }$ .
$\boxed { \begin{array} { r l } \end{array} }$

8.2. Stable pairs to GIT / SBB.
The goal of this section is to describe the morphism from $\overline { { \mathrm { W } } } _ { \sigma } ( \epsilon )  \overline { { \mathrm { W } } } ^ { G }$ (and thus to $\overline { { \mathrm { W } } } ^ { * }$ ).

Theorem 8.2 (Connection with GIT / SBB).
Let $\overline { { \mathrm { K } } } _ { \epsilon }$ be the coarse moduli space of $\overline { { \mathcal { K } } } _ { \epsilon }$ and let $\Delta \subset \overline { { \mathrm { K } } } _ { \epsilon }$ be the boundary locus parametrizing surfaces with an $L$ type cusp, with $U = \overline { { \mathrm { K } } } _ { \epsilon } \backslash \Delta$ .
There is a morphism $\overline { { \mathrm { K } } } _ { \epsilon }  \overline { { \mathrm { W } } } ^ { G } \cong \overline { { \mathrm { W } } } ^ { * }$ , such that the following diagram commutes:

![](images/77a064649b958a9468b84010370225fb5e926a9d1202a17274579416dbcea3c2.jpg)

$j : \Delta \to \mathbb { P } ^ { 1 }$ sends a surface with an $L$ cusp to its $j$ -invariant, the morphism $U  \overline { { \mathbb { W } } } _ { s } ^ { G }$ , is proper and finite of degree 24, and $\mathbb { P } ^ { 1 } \to \overline { { \mathbb { W } } } _ { L } ^ { G } \subset \overline { { \mathbb { W } } } ^ { G }$ maps bijectively onto the strictly GIT semistable locus.

Proof.
By Theorem 8.1 every surface parametrized by $\overline { { \mathcal { K } } } _ { \epsilon }$ is a single component pseudoelliptic K3 surface.
In particular, if we blow up the point to where the section contracted, we obtain an (unstable) slc Weierstrass elliptic K3 surface.
Consider the PGL $^ 2$ -torsor: $\operatorname { \mathcal { P } } = \{ ( X , s , t ) ~ | ~ ( s , t ) \in C \cong \mathbb { P } ^ { 1 } \} / \sim$ , where $X$ is an slc Weierstrass elliptic K3 surface obtained by blowing up the section of a surface parametrized by $\mathcal { K } _ { \epsilon }$ , the $( s , t )$ are coordinates on the base $C \cong \mathbb { P } ^ { 1 }$ (or equivalently a basis for the linear series $| F |$ of a fiber $F$ on $X$ ), and we quotient by scaling.
Note that the Weierstrass coefficients $( A ( s , t ) , B ( s , t ) )$ defining $X$ are unique up to the scaling of the $\mathbb { G } _ { m }$ action $( A , B ) \mapsto ( \lambda ^ { 4 } A , \lambda ^ { 6 } B )$ .

Since the semi-log canonical Weierstrass elliptic K3 surfaces are GIT semistable ([Mir81, Proposition 5.1]), we obtain a PGL -equivariant morphism $\mathcal { P }  V$ which induces a morphism $\phi : \overline { { \mathcal { K } } } _ { \epsilon } \to \overline { { \mathbb { W } } } ^ { G }$ .
$^ 2$

# Remark 8.3.

(1) The morphism $\overline { { \mathcal { K } } } _ { \epsilon }  \overline { { \mathbb { W } } } ^ { G }$ is generically a 24 to 1 cover, as it requires the choice of some marked fiber, and generically there are 24 choices.
The morphism is not finite – e.g. families with one L type cusp of fixed $j$ -invariant are all collapsed to the same polystable point.
(2) All the underlying surfaces of pairs parametrized by $\mathcal { K } _ { \epsilon }$ are in fact GIT semi-stable, even though all pairs with an $\mathrm { L }$ type cusp of fixed $j$ -invariant map to the same GIT polystable point.
One might wonder if the locus inside the GIT stack $[ V _ { 2 4 } ^ { s s } / / P G L _ { 2 } ]$ consisting of those surfaces that appear in $\overline { { \mathcal { K } } } _ { \epsilon }$ is an open Deligne-Mumford substack with proper coarse moduli space factoring the morphism $\overline { { \mathcal { K } } } _ { \epsilon }  \overline { { \mathbb { W } } } ^ { G }$ .
Furthermore, it is natural to compare this to a Kirwan desingularization of ${ \overline { { \mathrm { W } } } } ^ { G }$ .
We will pursue these questions in the future.
(3) In the morphism from stable pairs to GIT, all surfaces with an L type cusp get collapsed to the polystable orbit corresponding to the KSBA-unstable, but GIT semistable (unique) surface with 2L cusps of the same $j$ -invariant.

(4) The locus of surfaces with an L type cusp is 9 dimensional.
Indeed, such surfaces are birational to a rational elliptic surface (which have an 8 dimensional moduli space) with a choice of a fiber to replace by an L type cusp.
There is a $\mathbb { P } ^ { 1 }$ worth of choices.

8.3. GIT for Weierstrass surfaces with a marked fiber.
We extend Miranda’s GIT construction to produce a moduli space of Weierstrass surfaces with a choice of marked fiber.
Such data can be represented by triples $( A , B , l )$ where $( A , B ) \in V _ { 4 N } \oplus V _ { 6 N }$ are Weierstrass data as above, and $l \in V _ { 1 }$ is a linear form.
Then $\mathbb { G } _ { m } \times \mathbb { G } _ { m } \times S L _ { 2 }$ acts naturally on $V _ { 4 N } \oplus V _ { 6 N } \oplus V _ { 1 }$ where the first $\mathbb { G } _ { m }$ acts on $V _ { 4 N } \oplus V _ { 6 N }$ with weights $4 N$ and $6 N$ and the second copy acts on $V _ { 1 }$ with weight one.

To study GIT (semi-)stability, we follow Miranda’s strategy.
Consider the natural morphism $f : V _ { 4 N } \oplus V _ { 6 N } \to S ^ { 3 } V _ { 4 N } \oplus S ^ { 2 } V _ { 6 N }$ , let $Z _ { N }$ be the image of $f$ , and let $\mathfrak { M } _ { N } \subset \mathbb { P } ( S ^ { 3 } V _ { 4 N } \oplus S ^ { 2 } V _ { 6 N } )$ be its projectivization.
The following proposition follows from [Mir81, Propositions $3 . 1 \ \&$ 3.2]:

Proposition 8.4. The morphism $f \times i d : V _ { 4 N } \oplus V _ { 6 N } \oplus V _ { 1 } \to S ^ { 3 } V _ { 4 N } \oplus S ^ { 2 } V _ { 6 N } \oplus V _ { 1 }$ is finite and $S L _ { 2 }$ -equivariant with fibers contained in $\mathbb { G } _ { m } \times \mathbb { G } _ { m }$ orbits.
In particular, two triples $( A , B , l )$ and $( A ^ { \prime } , B ^ { \prime } , l ^ { \prime } )$ are in the same $\mathbb { G } _ { m } \times \mathbb { G } _ { m } \times S L _ { 2 }$ orbit if and only if the corresponding points in ${ \mathfrak { M } } _ { N } \times { \mathbb { P } } ( V _ { 1 } )$ are in the same $S L _ { 2 }$ orbit.

This allows us to compute a GIT compactification of the moduli space of minimal Weierstrass fibrations with a chosen marked fiber as a GIT quotient $( \mathfrak { M } _ { N } \times \mathbb { P } ^ { 1 } ) \ / \subset S L _ { 2 }$ .
We will linearize the moduli problem using the Segre embedding of $\mathbb { P } ( S ^ { 3 } V _ { 4 N } \oplus S ^ { 2 } V _ { 6 N } ) \times \mathbb { P } ^ { 1 }$ .

Proposition 8.5. $A$ triple $( A , B , l )$ is stable if and only if it is semi-stable.
Furthermore, it is not stable if and only if there exists a point $q \in \mathbb { P } ^ { 1 }$ with $v _ { q } ( A ) > 2 N$ and $v _ { q } ( B ) > 3 N$ or with $v _ { q } ( A ) \geq 2 N , \ v _ { q } ( B ) \geq 3 N ,$ and $v _ { q } ( l ) = 1$ and at least one an equality.

Proof.
Let $( A , B , l ) \in \mathfrak { M } _ { N }$ and let $\lambda : \mathbb { G } _ { m } \to S L _ { 2 }$ be a 1-parameter subgroup and pick coordinates $[ T _ { 0 } , T _ { 1 } ]$ so that $\lambda$ acts by $T _ { 0 } \mapsto \lambda ^ { e } T _ { 0 }$ and $T _ { 1 } \mapsto \lambda ^ { - e } T _ { 1 }$ .
Then it acts on $( A , B , l )$ by

$$
\begin{array} { r l } { } & { \sim \displaystyle \sum _ { i = 0 } ^ { 4 N } a _ { i } T _ { 0 } ^ { i } t _ { 1 } ^ { 4 N - i } \mapsto \displaystyle \sum _ { i = 0 } ^ { 4 N } a _ { i } \lambda ^ { 2 e i - 4 e N } T _ { 0 } ^ { i } t _ { 1 } ^ { 4 N - i } , \quad B = \displaystyle \sum _ { i = 0 } ^ { 6 N } b _ { i } T _ { 0 } ^ { i } t _ { 1 } ^ { 6 N - i } \mapsto \displaystyle \sum _ { i = 0 } ^ { 4 N } b _ { i } \lambda ^ { 2 e i - 6 e N } T _ { 0 } ^ { i } t _ { 2 } ^ { 2 N - i } } \\ { } & { \mapsto l _ { 0 } T _ { 1 } + l _ { 1 } T ^ { 0 } \mapsto l _ { 0 } \lambda ^ { - e } T _ { 1 } + l _ { 1 } \lambda ^ { e } T _ { 0 } . } \end{array}
$$

The coordinates of $\mathbb { P } ( S ^ { 3 } V _ { 4 N } \oplus S ^ { 2 } V _ { 6 N } ) \times \mathbb { P } ( V _ { 1 } )$ are given by $l _ { 0 } a _ { i } a _ { j } a _ { k } , l _ { 0 } b _ { l } b _ { m }$ , $l _ { 1 } a _ { i } a _ { j } a _ { k }$ , and $l _ { 0 } b _ { l } b _ { m }$ which respectively have weights

$$
\begin{array} { r } { - k ) - 1 2 e N - e , \quad 2 e ( l + m ) - 1 2 e N - e , \quad 2 e ( i + j + k ) - 1 2 e N + e , \mathrm { a n d } \quad 2 e ( l + m ) - 1 2 e _ { N } } \end{array}
$$

By the Hilbert-Mumford criterion, a point is not (semi-)stable if and only if there exists a 1-parameter subgroup such that all the weights are non-negative (respectively positive).

Suppose $( A , B , l )$ is not (semi-)stable and pick a 1-parameter subgroup and coordinates as above.
Then we have, after dividing by $e \neq 0$ ,

$$
\begin{array} { r l } & { + k ) - 1 2 e N - e < ( \leq ) \ 0 \implies l _ { 0 } a _ { i } a _ { j } a _ { k } = 0 , 2 e ( l + m ) - 1 2 e N - e < ( \leq ) \ 0 \implies l _ { 0 } b _ { l } } \\ & { + k ) - 1 2 e N + e < ( \leq ) \ 0 \implies l _ { 1 } a _ { i } a _ { j } a _ { k } = 0 , 2 e ( l + m ) - 1 2 e N + e < ( \leq ) \ 0 \implies l _ { 1 } b _ { l } } \end{array}
$$

Note that the left hand side is always odd and so equality is never achieved.
From this we can conclude that stability coincides with semi-stability.
Now consider the cases where $i = j = k$ and $l = m$ .
Then we see that $l _ { 0 } a _ { i } ^ { 3 } = 0$ for $i \leq 2 N$ , $l _ { 1 } a _ { i } ^ { 3 } = 0$ for $i \le 2 N - 1$ , $l _ { 0 } b _ { l } ^ { 2 } = 0$ for $l \leq 3 N$ , and $l _ { 1 } b _ { l } ^ { 2 } = 0$ for $l \le 3 N - 1$ .
Let $q = \lfloor 0 , 1 \rfloor$ be the point given by $T _ { 0 } = 0$ .
If $l _ { 0 } \neq 0$ , then we must have that $a _ { i } = 0$ for $i \le 2 N$ and $b _ { l } = 0$ for $i \le 3 N$ .
Thus the order of vanishing $v _ { q } ( A ) > 2 N$ and $v _ { q } ( B ) > 3 N$ .
Otherwise, if $l _ { 0 } = 0$ then $l _ { 1 } \neq 0$ so we must have that $a _ { i } = 0$ for $i \leq 2 N - 1$ and $b _ { l } = 0$ for $i \le 3 N - 1$ .
In this case, $v _ { q } ( l ) = 1$ , $v _ { q } ( A ) \geq 2 N$ and $v _ { q } ( B ) \geq 3 N$ .

Conversely, given a triple $( A , B , l )$ satisfying such order of vanishing conditions, we may pick coordinates such that $q = \lfloor 0 , 1 \rfloor$ .
Then it is easy to see that the 1-parameter subgroup acting by $( T _ { 0 } , T _ { 1 } ) \mapsto ( \lambda T _ { 0 } , \lambda ^ { - 1 } T _ { 1 } )$ demonstrates that $( A , B , l )$ is not stable.


In the case of K3 surfaces where $N = 2$ , we obtain an especially pleasant result:

Corollary 8.6. A point of $\mathfrak { M } _ { 2 }$ is stable if and only if it represents a 1-marked Weierstrass fibration $( f : X \to \mathbb { P } ^ { 1 } , S + \epsilon F )$ with at worst semi-log canonical singularities.

Proof.
First note that the generic fiber of the fibration $f : X \to \mathbb { P } ^ { 1 }$ represented by a stable point in ${ \mathfrak { M } } _ { N }$ is at worst nodal since the Weierstrass data of a stable point cannot be identically 0. Then combining the above Proposition 8.5 with [LN02, Lemma 3.2.1, Lemma 3.2.2, Corollary 3.2.4], and noting that the log canonical threshold of a type L/N $^ 2$ fiber is 0 (see Lemma 3.14), a point is unstable if and only if there exists a point $q \in \mathbb { P } ^ { 1 }$ such that the pair $( X , S + \epsilon F )$ is not semi-log canonical around the singular point of $f ^ { - 1 } ( q )$ .
The result then follows since a Weierstrass fibration $( X , S + \epsilon F )$ has semi-log canonical singularities away from the singular points of the fibers.


Definition 8.7. If $\mathfrak { M } _ { 2 } ^ { s }$ denotes the stable/semi-stable locus, we denote $\widetilde { \mathrm { W } } ^ { G } = \mathfrak { M } _ { 2 } ^ { s } / / \mathrm { S L _ { 2 } }$

Theorem 8.8. $\overline { { \mathcal { F } } } _ { \epsilon }$ is a smooth Deligne-Mumford stack with coarse space map $\overline { { \mathcal { F } } } _ { \epsilon }  \widetilde { \mathrm { W } } ^ { G }$ given by the GIT compactification.
Furthermore, there is a morphism $\overline { { \mathcal { F } } } _ { \epsilon }  \overline { { \mathrm { W } } } ^ { G }$ given by forgetting the marked fiber.
A Weierstrass fibration ( $f : X \to \mathbb { P } ^ { 1 } , S )$ is represented by a point in $\overline { { \mathrm { W } } } ^ { G }$ if and only if there exists a fiber $F$ so that $( X , S + \epsilon F )$ is a stable pair.

Proof.
By the proof of Theorem 8.2, we obtain a birational morphism $\overline { { \mathcal { F } } } _ { \epsilon }  [ \mathfrak { M } _ { 2 } ^ { s } / \mathrm { P G L _ { 2 } } ]$ .
On the other hand, by the above Corollary 8.6, there is a family of KSBA-stable one $\epsilon$ -marked Weierstrass fibrations $f : X \to \mathbb { P } ^ { 1 } , S + \epsilon F )$ over $\mathfrak { M } _ { 2 } ^ { s }$ .
This induces a PGL $^ 2$ equivariant map $\mathfrak { M } _ { 2 } ^ { s } \to \overline { { \mathcal { F } } } _ { \epsilon }$ which gives an inverse map $[ \mathfrak { M } _ { 2 } ^ { s } / \mathrm { P G L _ { 2 } } ] \to \mathcal { F } _ { \epsilon }$ exhibiting these as isomorphisms.
On the other hand, $[ \mathfrak { M } _ { 2 } ^ { s } / \mathrm { P G L _ { 2 } } ]$ is a smooth stack as $\mathfrak { M } _ { 2 } ^ { s }$ is an open subset of a smooth variety so $\overline { { \mathcal { F } } } _ { \epsilon }$ is smooth.

The composition $\mathcal { F } _ { \epsilon }  [ \mathfrak { M } _ { 2 } ^ { s } / \mathrm { P G L _ { 2 } } ]  \mathfrak { M } _ { 2 } / / \mathrm { S L _ { 2 } }$ is the coarse moduli space map.
Indeed, $[ \mathfrak { M } _ { 2 } ^ { s } / \mathrm { S L } _ { 2 } ]$ and $\lfloor \mathfrak { M } _ { 2 } ^ { s } / \mathrm { P G L _ { 2 } } \rfloor$ have the same coarse moduli space; note that $\mathrm { [ \mathfrak { M } _ { 2 } ^ { \mathfrak { s } } / S L _ { 2 } ] } \to \mathrm { [ \mathfrak { M } _ { 2 } ^ { \mathfrak { s } } / P G L _ { 2 } ] }$ is a $\mu _ { 2 }$ -gerbe being the base change of the map $B \mathrm { S L _ { 2 } } \to B \mathrm { P G L _ { 2 } }$ so $[ \mathfrak { M } _ { 2 } ^ { s } / \mathrm { S L } _ { 2 } ] \to [ \mathfrak { M } _ { 2 } ^ { s } / \mathrm { P G L } _ { 2 } ]$ is a relative coarse space and the coarse map $[ \mathfrak { M } _ { 2 } ^ { s } / \mathrm { S L } _ { 2 } ] \to \mathfrak { M } _ { 2 } ^ { s } / / \mathrm { S L } _ { 2 }$ factors through it.

If $( A , B , l )$ is in $\mathfrak { M } _ { 2 } ^ { s }$ , then $( A , B )$ is a semi-stable point for Miranda, and conversely, if $( A , B )$ is semi-stable in Miranda’s space then for a generic choice of fiber $F$ , the corresponding fibration ( $X \to \mathbb { P } ^ { 1 } , S + e F )$ is a stable pair and the corresponding GIT data $( A , B , l )$ is GIT stable.


# References

[AB17] Kenneth Ascher and Dori Bejleri.
Log canonical models of elliptic surfaces.
Advances in Mathematics, 320:210– 243, 2017.  
[AB19] Kenneth Ascher and Dori Bejleri.
Moduli of fibered surface pairs from twisted stable maps.
Mathematische Annalen, 374(1-2):1007–1032, 2019.  
[AB21a] Kenneth Ascher and Dori Bejleri.
Moduli of weighted stable elliptic surfaces and invariance of log plurigenera.
Proc.
Lond.
Math.
Soc, 122(5):617–677, 2021.  
[AB21b] Kenneth Ascher and Dori Bejleri.
Smoothability of relative stable maps to stacky curves.
arXiv:2108.05324, 2021.  
[ABE20] Valery Alexeev, Adrian Brunyate, and Philip Engel.
Compactifications of moduli of elliptic K3 surfaces: stable pair and toroidal.
arXiv e-prints, page arXiv:2002.07127, Feb 2020.  
[AET19] Valery Alexeev, Philip Engel, and Alan Thompson.
Stable pair compactification of moduli of K3 surfaces of degree 2. arXiv e-prints, page arXiv:1903.09742, Mar 2019.  
[Ale94] Valery Alexeev.
Boundedness and $K ^ { 2 }$ for log surfaces.
Internat.
J.
Math., 5(6):779–810, 1994.  
[AV97] Dan Abramovich and Angelo Vistoli.
Complete moduli for fibered surfaces.
Recent progress in intersection theory (Bologna, 1997), 1997.  
[AV02] Dan Abramovich and Angelo Vistoli.
Compactifying the space of stable maps.
J.
Amer.
Math.
Soc., 15(1):27–75, 2002.  
[BB66] W.
L.
Baily, Jr.
and A.
Borel.
Compactification of arithmetic quotients of bounded symmetric domains.
Ann.
of Math.
(2), 84:442–528, 1966.  
[BHPVdV04] Wolf P.
Barth, Klaus Hulek, Chris A.
M.
Peters, and Antonius Van de Ven.
Compact complex surfaces, volume 4 of Ergebnisse der Mathematik und ihrer Grenzgebiete.
3. Folge.
A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics].
SpringerVerlag, Berlin, second edition, 2004.  
[Bru15] Adrian Brunyate.
A Modular Compactification of the Space of Elliptic K3 Surfaces.
PhD thesis, The University of Georgia, 2015.  
[Cad07] Charles Cadman.
Using stacks to impose tangency conditions on curves.
Amer.
J.
Math., 129(2):405–427, 2007.  
[Dol96] I.
V.
Dolgachev.
Mirror symmetry for lattice polarized $_ { K 3 }$ surfaces.
J.
Math.
Sci., 81(3):2599–2630, 1996. Algebraic geometry, 4.  
[Fri84a] Robert Friedman.
A new proof of the global Torelli theorem for $_ { K 3 }$ surfaces.
Ann.
of Math.
(2), 120(2):237–269, 1984.  
[Fri84b] Robert Friedman.
The period map at the boundary of moduli.
In Topics in transcendental algebraic geometry (Princeton, N.J., 1981/1982), volume 106 of Ann.
of Math.
Stud., pages 183–208.
Princeton Univ.
Press, Princeton, NJ, 1984.  
[Gat02] Andreas Gathmann.
Absolute and relative Gromov-Witten invariants of very ample hypersurfaces.
Duke Math.
J., 115(2):171–203, 2002.  
[GG14] Noah Giansiracusa and William Danny Gillam.
On Kapranov’s description of $M _ { 0 , n }$ as a Chow quotient.
Turkish J.
Math., 38(4):625–648, 2014.  
[Has03] Brendan Hassett.
Moduli spaces of weighted pointed stable curves.
Advances in Mathematics, pages 316–352, 2003.  
[HL02] Gert Heckman and Eduard Looijenga.
The moduli space of rational elliptic surfaces.
In Algebraic Geometry 2000, volume 36 of Adv.
Stud.
Pure Math.
Math.
Soc.
Japan, 2002.  
[HMX18] Christopher D.
Hacon, James McKernan, and Chenyang Xu.
Boundedness of moduli of varieties of general type.
J.
Eur.
Math.
Soc.
(JEMS), 20(4):865–901, 2018.  
[HP15] Robin Hartshorne and Claudia Polini.
Divisor class groups of singular surfaces.
Trans.
Amer.
Math.
Soc., 367(9):6357–6385, 2015.  
[HT15] Andrew Harder and Alan Thompson.
The geometry and moduli of K3 surfaces.
In Calabi-Yau varieties: arithmetic, geometry and physics, volume 34 of Fields Inst.
Monogr., pages 3–43.
Fields Inst.
Res.
Math.
Sci., Toronto, ON, 2015.  
[HX13] Christopher D.
Hacon and Chenyang Xu.
Existence of log canonical closures.
Invent.
Math., 192(1):161–195, 2013.  
[Inc20] G.
Inchiostro.
Moduli of Weierstrass fibrations with marked section.
Advances in Mathematics, 2020. To appear.  
[KK10] J´anos Koll´ar and S´andor J.
Kov´acs.
Log canonical singularities are Du Bois.
J.
Amer.
Math.
Soc., 23(3):791–813, 2010.  
[KM98] J´anos Koll´ar and Shigefumi Mori.
Birational geometry of algebraic varieties, volume 134 of Cambridge Tracts in Mathematics.
Cambridge University Press, Cambridge, 1998. With the collaboration of C.
H.
Clemens and A.
Corti, Translated from the 1998 Japanese original.  
[Kol13] J´anos Koll´ar.
Singularities of the minimal model program, volume 200 of Cambridge Tracts in Mathematics.
Cambridge University Press, Cambridge, 2013. With a collaboration of S´andor Kov´acs.  
[Kol18] J´anos Koll´ar.
Mumford’s influence on the moduli theory of algebraic varieties.
arXiv e-prints, page arXiv:1809.10723, September 2018.  
[Kol21] J´anos Koll´ar.
Families of varieties of general type.
Available at https://web.math.princeton.edu/\~kollar/, 2021.  
[KP17] S´andor J.
Kov´acs and Zsolt Patakfalvi.
Projectivity of the moduli space of stable log-varieties and subadditivity of log-Kodaira dimension.
J.
Amer.
Math.
Soc., 30(4):959–1021, 2017.  
[KSB88] J.
Koll´ar and N.
I.
Shepherd-Barron.
Threefolds and deformations of surface singularities.
Invent.
Math., 91(2):299–338, 1988.  
[Laz16] Radu Laza.
The KSBA compactification for the moduli space of degree two $_ { K 3 }$ pairs.
J.
Eur.
Math.
Soc.
(JEMS), 18(2):225–279, 2016.  
[LN02] Gabrielle La Nave.
Explicit stable models of elliptic surfaces with sections.
arXiv: 0205035, 2002.  
[LZ16] Radu Laza and Zheng Zhang.
Classical period domains.
In Recent advances in Hodge theory, volume 427 of London Math.
Soc.
Lecture Note Ser., pages 3–44.
Cambridge Univ.
Press, Cambridge, 2016.  
[Mir81] Rick Miranda.
The moduli of weierstrass fibrations over $\mathbb { P } ^ { 1 }$ .
Math.
Ann., 255(3):379–394, 1981.  
[Mir89] Rick Miranda.
The basic theory of elliptic surfaces.
Dottorato di Ricerca in Matematica.
[Doctorate in Mathematical Research].
ETS Editrice, Pisa, 1989.  
[Nik79] V.
V.
Nikulin.
Finite groups of automorphisms of K¨ahlerian $_ { K 3 }$ surfaces.
Trudy Moskov.
Mat.
Obshch., 38:75–137, 1979.  
[Ols07] Martin C Olsson.
(log) twisted curves.
Compositio Mathematica, 143(2):476–494, 2007.  
[OO18] Y.
Odaka and Y.
Oshima.
Collapsing K3 surfaces, Tropical geometry and Moduli compactifications of Satake, Morgan-Shalen type.
ArXiv e-prints, October 2018.  
[Per90] Ulf Persson.
Configurations of Kodaira fibers on rational elliptic surfaces.
Math.
Z., 205(1):1–47, 1990.  
[Sca87] Francesco Scattone.
On the compactification of moduli spaces for algebraic $_ { K 3 }$ surfaces.
Mem.
Amer.
Math.
Soc., 70(374):x+86, 1987.  
[Shi03] Tetsuji Shioda.
The elliptic k3 surfaces with a maximal singular fibre.
Comptes Rendus Mathematique, 337(7):461 – 466, 2003.  
[SS09] M.
Schuett and T.
Shioda.
Elliptic Surfaces.
ArXiv e-prints, July 2009.  
[Vak00] Ravi Vakil.
The enumerative geometry of rational and elliptic curves in projective space.
J.
Reine Angew.
Math., 529:101–153, 2000.