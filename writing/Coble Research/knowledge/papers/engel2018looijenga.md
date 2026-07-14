---
title: Looijenga's conjecture via integral-affine geometry
authors:
- Engel
year: 2014
bibkey: engel2018looijenga
tags:
- paper
- extraction
abstract: |
  A cusp singularity is a surface singularity whose minimal resolution is a cycle of smooth rational curves meeting transversely.
  Cusp singularities come in naturally dual pairs.
  In 1981, Looijenga proved that whenever a cusp singularity is smoothable, the minimal resolution of the dual cusp is an anticanonical divisor of some smooth rational surface.
  He conjectured the converse.
  Recent work of Gross, Hacking, and Keel has proven Looijenga’s conjecture using methods from mirror symmetry.
  This paper provides an alternative proof of Looijenga’s conjecture based on a combinatorial criterion for smoothability given by Friedman and Miranda in 1983.
---

# LOOIJENGA’S CONJECTURE VIA INTEGRAL-AFFINE GEOMETRY

Philip Engel

# Abstract

A cusp singularity is a surface singularity whose minimal resolution is a cycle of smooth rational curves meeting transversely.
Cusp singularities come in naturally dual pairs.
In 1981, Looijenga proved that whenever a cusp singularity is smoothable, the minimal resolution of the dual cusp is an anticanonical divisor of some smooth rational surface.
He conjectured the converse.
Recent work of Gross, Hacking, and Keel has proven Looijenga’s conjecture using methods from mirror symmetry.
This paper provides an alternative proof of Looijenga’s conjecture based on a combinatorial criterion for smoothability given by Friedman and Miranda in 1983.

# 1. Introduction

A cusp singularity $( \overline { { V } } , p )$ is the germ of a minimally elliptic surface singularity such that the exceptional divisor of the minimal resolution $\pi : V \to { \overline { { V } } }$ is a reduced anticanonical cycle of smooth rational curves meeting transversely:

$$
\pi ^ { - 1 } ( p ) = D = D _ { 1 } + \cdots + D _ { n } \in | - K _ { V } | .
$$

The analytic germ of a cusp singularity is uniquely determined by the self-intersections $D _ { i } ^ { 2 }$ of the components of $D$ .
Cusp singularities come in naturally dual pairs $( \overline { { V } } , p )$ and $( \overline { { V } } ^ { \prime } , p ^ { \prime } )$ , whose exceptional divisors $D$ and $D ^ { \prime }$ are called dual cycles.
For every pair of dual cusps, Inoue [7] constructs an associated hyperbolic Inoue surface—a smooth, non-algebraic, compact complex surface whose only curves are the components of two disjoint cycles $D$ and $D ^ { \prime }$ .
Contracting $D$ and $D ^ { \prime }$ produces a surface with two dual cusp singularities and no algebraic curves.

By working out the deformation theory of the contracted hyperbolic Inoue surface, Looijenga [9] proved that if the cusp with cycle $D ^ { \prime }$ is smoothable, then there exists an anticanonical pair $( Y , D )$ —a smooth rational surface $Y$ with an anticanonical divisor $D \in \mathsf { \Omega } | - K _ { Y } |$ whose components have the appropriate self-intersections.
Conversely, Looijenga conjectured that the existence of such an anticanonical pair $( Y , D )$

implies the smoothability of the cusp with cycle $D ^ { \prime }$ .
Recently, work of Gross, Hacking, and Keel proved Looijenga’s conjecture using methods from mirror symmetry [5].
In this paper, we provide an alternative proof of Looijenga’s conjecture.

In the first section, we review foundational material on cusp singularities, hyperbolic Inoue surfaces, anticanonical pairs, and discuss the main result of Friedman-Miranda [1]: The cusp with resolution $D ^ { \prime }$ is smoothable if there exists a simple normal crossings surface $\mathcal { X } _ { 0 } = \bigcup V _ { i }$ satisfying certain combinatorial conditions.

We begin the second section by defining the notion of a triangulated integral-affine surface (with singularities).
Then, we associate a triangulated integral-affine surface, called the pseudo-fan, to any anticanonical pair $( V , D )$ and describe two surgeries on the pseudo-fan that correspond to blowing up a point on a component of $D$ and smoothing a node of $D$ .
We describe a natural triangulated integral-affine structure on the dual complex $\Gamma ( \mathcal { X } _ { 0 } )$ of a surface $\mathcal { X } _ { 0 }$ satisfying the conditions of Friedman-Miranda.

In the third section, we define two of surgeries on an integral-affine surface $S$ —an internal blow-up and a node smoothing.
Both surgeries appear in Symington’s work [12] on almost toric fibrations of fourdimensional symplectic manifolds.
Assuming certain conditions, there is a unique symplectic four-manifold $Y$ with a Lagrangian torus fibration

$$
( Y , D , \omega )  S
$$

which attains certain allowable singular fibers over the singular points of $S$ .
An internal blow-up or node smoothing of $S$ is the base of a Lagrangian torus fibration of an internal blow-up or node smoothing of $( Y , D , \omega )$ , respectively.
When $S$ is a disc whose boundary satisfies a negativity condition, we define an integral-affine completion $\hat { S }$ to a sphere by attaching a cone $C$ with a distinguished vertex $v _ { 0 }$ to the boundary of $S$ .
Finally, we define the notion of an order $k$ refinement $S [ k ]$ of an integral-affine surface $S$ .

In the fourth section, we construct from an anticanonical pair $( Y , D )$ a surface $\mathcal { X } _ { 0 }$ satisfying the conditions of the theorem of FriedmanMiranda, thus proving Looijenga’s conjecture:

1. We express $( Y , D )$ as a sequence of internal blow-ups and node smoothings of a toric surface $( \overline { { Y } } , \overline { { D } } )$ .
   By performing the analogous surgeries on a moment polygon $S$ for $( \overline { { Y } } , \overline { { D } } )$ , we produce the base $S$ of an almost toric fibration of a symplectic surface $( Y , D , \omega )$ .
   We complete to $\hat { S }$ and take an order $k$ refinement $\hat { S } [ k ]$ which admits a triangulation.
2. We show that a neighborhood of every vertex $v _ { i }$ of the triangulation of $\hat { S } [ k ]$ with $i \neq 0$ is locally modeled by the pseudo-fan of an anticanonical pair $( V _ { i } , D _ { i } )$ .
   The cone point $v _ { 0 }$ is locally modeled

by the pseudo-fan of the hyperbolic Inoue pair $( V _ { 0 } , D ^ { \prime } )$ .
By gluing the surfaces $V _ { i }$ together, we produce a surface $\mathcal { X } _ { 0 }$ whose dual complex is $\hat { S } [ k ]$ , as a triangulated integral-affine surface.

The construction of $\mathcal { X } _ { 0 }$ may be phrased solely in terms of operations on integral-affine surfaces—no results in symplectic geometry are necessary for the proof, but they provide the primary motivation.
Our construction is algorithmic, providing a simple normal crossings resolution of at least one smoothing of any smoothable cusp singularity.
We describe, without proof, four modifications and generalizations of the construction and conclude by giving an example of the modified construction in the charge three case $Q ( Y , D ) = 3$ .

Our proof differs from the approach of Gross, Hacking, and Keel.
Unlike [5] this work relies on the main theorem of [1] to prove smoothability of the dual cusp.
This approach has advantages and disadvantages.
The delicate convergence arguments of [5] are avoided by using the deformation theory of global simple normal crossings varieties.
On the other hand, the techniques of this paper can only see one-parameter smoothings, because smoothings with a higher dimensional base need not have SNC resolutions.
The connection between the two proofs is still largely unexplored.
In terms of mirror symmetry and the Gross-Siebert program, we use a “fan” construction which appears to be Legendre dual to the “polytope” construction of [5].
For us, the fundamental piece of data to prove smoothability of the dual cusp is the existence of $( Y , D )$ , as a symplectic anticanonical pair.

Acknowledgements.
I thank my advisor, Robert Friedman, for the time he spent editing this paper, and for his numerous suggestions, explanations, and clarifications.
I thank Lucas Culler, who suggested a simplifying modification of the original construction.
I’d also like to thank Mark Gross, Paul Hacking, and Sean Keel for their comments.
In addition, I thank Eduard Looijenga for our productive conversation.
Finally, I would like to thank the referee for their careful reading and excellent suggestions.

# 2. Background

Let $( \overline { { V } } , p )$ be the germ of a cusp singularity.
The exception divisor of the minimal resolution

$$
\pi ^ { - 1 } ( p ) = D = D _ { 1 } + \cdot \cdot \cdot + D _ { n }
$$

is a cycle of smooth rational curves meeting transversely.
We define $\ell ( D ) : = n$ to be the length of the cycle.
Whenever $n \geq 3$ , we assume $D _ { i } \cdot D _ { i \pm 1 } = 1$ , with indices taken mod $n$ .
If $n = 1$ , then $D$ is an irreducible, nodal rational curve.
If $n = 2$ , then $D$ is the union of two smooth rational curves that meet transversely at two distinct points.

We define

$$
d _ { i } : = { \left\{ \begin{array} { l l } { - D _ { i } ^ { 2 } } & { { \mathrm { i f ~ } } n > 1 } \\ { 2 - D _ { i } ^ { 2 } } & { { \mathrm { i f ~ } } n = 1 . } \end{array} \right. }
$$

The analytic germ of a cusp singularity is uniquely determined by the cycle $\mathbf { d } : = \left( d _ { 1 } , \ldots , d _ { n } \right)$ , well-defined up to cyclic permutation and orientation.
As $D$ is contractible, Artin’s contractibility criterion implies that the intersection matrix $[ D _ { i } \cdot D _ { j } ]$ is negative-definite.
No component of $D$ is an exceptional curve, because it is a minimal resolution.
The negative-definite condition is then equivalent to

$$
\begin{array} { l l } { { d _ { i } \geq 2 } } & { { \mathrm { f o r ~ a l l ~ } i , } } \\ { { d _ { i } \geq 3 } } & { { \mathrm { f o r ~ s o m e ~ } i . } } \end{array}
$$

Cusp singularities arise in the classification of complex analytic surfaces.
Amongst those of Type $\mathrm { V I I _ { 0 } }$ are the hyperbolic Inoue surfaces, which have first Betti number $b _ { 1 } = 1$ and Kodaira dimension $\kappa = - \infty$ .
For a construction, see [7].
The only curves on a hyperbolic Inoue surface $V$ are the components of two contractible cycles $D$ and $D ^ { \prime }$ of rational curves satisfying $D + D ^ { \prime } \in \vert - K _ { V } \vert$ .
Both cycles can be blown down to give a surface $( \overline { { V } } , p , p ^ { \prime } )$ with two dual cusps.
For any cusp singularity $p$ , there is a construction of $\overline { V }$ as the compactification of a quotient of $\mathbb { H } \times \mathbb { C }$ by a discrete group action (hence the terminology “cusp”).
Suppose that the cycle of negative self-intersections of $D$ is

$$
\mathbf { d } = ( d _ { 1 } , \ldots , d _ { n } ) = ( a _ { 1 } + 3 , \underbrace { 2 , \ldots , 2 } _ { b _ { 1 } } , \ldots , a _ { k } + 3 , \underbrace { 2 , \ldots , 2 } _ { b _ { k } } )
$$

with $a _ { i } , b _ { i } \geq 0$ .
An explicit formula for the negative self-intersections of the dual cycle $D ^ { \prime }$ may be given from those of the original cycle $D$ by interchanging $a _ { i }$ and $b _ { i }$ :

$$
\mathbf { d } ^ { \prime } = ( d _ { 1 } ^ { \prime } , \ldots , d _ { s } ^ { \prime } ) = ( b _ { 1 } + 3 , \underbrace { 2 , \ldots , 2 } _ { a _ { 1 } } , \ldots , b _ { k } + 3 , \underbrace { 2 , \ldots , 2 } _ { a _ { k } } ) .
$$

Let $( \overline { { V } } , p , p ^ { \prime } )$ denote the (disconnected) germ of the two cusp singularities on the doubly contracted hyperbolic Inoue surface $V$ .
Looijenga [9] proves:

Theorem 2.1. $\overline { V }$ has a universal deformation which is semi-universal for the germ $( \overline { { V } } , p , p ^ { \prime } )$ .

Suppose that $p ^ { \prime }$ is smoothable.
By Theorem 2.1, there exists a deformation

$$
\pi : \mathcal { V } \to \Delta
$$

over an analytic disc, with $\mathcal { V } _ { 0 } = \overline { { V } }$ , which keeps the germ $( \overline { { V } } , p )$ constant while smoothing the germ $( \overline { { V } } , p ^ { \prime } )$ .
Any fiber $\nu _ { t }$ with $t \neq 0$ is a surface with a single cusp singularity $p = p _ { t }$ .
Simultaneously resolving the singularities $p _ { t }$ produces a family $y  \Delta$ whose central fiber is the partially contracted hyperbolic Inoue surface with cusp singularity $p ^ { \prime }$ and whose general fiber is a smooth surface.
Any fiber $y _ { t }$ with $t \neq 0$ is a simply connected surface with anticanonical divisor $D$ , which by the classification of surfaces must be rational.
Hence, the following corollary to Theorem 2.1:

Corollary 2.2. Suppose that $D ^ { \prime }$ contracts to a smoothable cusp singularity.
Then, $D$ is the anticanonical divisor of some rational surface.

Looijenga conjectured the converse, which by the work of Gross, Hacking, and Keel [5] on mirror symmetry for anticanonical pairs, is now a theorem:

Theorem 2.3 (Looijenga’s Conjecture).
If $D$ is the anticanonical divisor of some rational surface, then the cusp singularity associated to $D ^ { \prime }$ is smoothable.

Now we review some basic facts about rational surfaces with an anticanonical cycle $D$ .
Such surfaces are log generalizations of K3 surfaces: They are simply connected surfaces with a global non-vanishing meromorphic 2-form with poles along a simple normal crossings divisor $D$ :

Definition 2.4. An anticanonical pair or simply pair $( Y , D )$ is a rational surface $Y$ with an anticanonical divisor $D$ equal to a cycle of rational curves

$$
D = D _ { 1 } + \cdot \cdot \cdot + D _ { n } \in | - K _ { Y } |
$$

meeting transversely.
A negative-definite pair satisfies the additional condition that the intersection matrix $[ D _ { i } \cdot D _ { j } ]$ is negative-definite.
A toric pair is a pair where $Y$ is a toric surface and $D$ is the toric boundary.

Let $E$ be an exceptional curve on $( Y , D )$ —by this we always mean an exceptional curve of the first kind, i.e. $E \cong \mathbb { P } ^ { 1 }$ with $E ^ { 2 } = - 1$ .
Contracting $E$ gives a smooth anticanonical pair:

$$
\pi : ( Y , D )  ( { \overline { { Y } } } , { \overline { { D } } } ) .
$$

If $E$ is a component of $\boldsymbol { D }$ , then $E$ contracts to a node point of the cycle $\overline { { D } }$ .
In this case, we call $\pi$ a corner blow-up.
If $E$ is not a component of $D$ , then $E$ intersects $D$ at one of its smooth points.
Thus, $E$ contracts to a smooth point of the cycle $\overline { { D } }$ , in which case, we call $\pi$ an internal blowup.
Conversely, given any anticanonical pair, we can blow-up either a corner or a smooth point of the cycle to produce a new anticanonical pair.
In addition to blowing up on $D$ , we can smooth any node of $D$ :

Proposition 2.5. Let $( V , D )$ be an anticanonical pair and let $p$ be $a$ node of $\boldsymbol { D }$ .
There exists a family of anticanonical pairs

$$
( \gamma , { \mathcal { D } } ) \to \Delta
$$

over the disc whose central fiber is $( V , D )$ such that $\mathcal { D } \to \Delta$ is a smoothing of the node $p$ .

Proof.
The proposition follows from Corollary 3.6 of [3], which proves the result for any subset of the nodes of $D$ .
Roughly, the deformations of $( V , D )$ surject onto the deformations of $D$ .
q.e.d.

Definition 2.6. The charge of a cycle $D$ or of a pair $( Y , D )$ is defined by the formula

$$
Q ( D ) = Q ( Y , D ) : = 1 2 + \sum _ { i = 1 } ^ { n } { ( d _ { i } - 3 ) } = 1 2 + \sum _ { i = 1 } ^ { n } ( a _ { i } - b _ { i } ) .
$$

The formula for the dual cusp $D ^ { \prime }$ interchanges $a _ { i }$ with $b _ { i }$ and thus $Q ( D ) + Q ( D ^ { \prime } ) = 2 4$ .
The charge of an anticanonical pair $( Y , D )$ is essentially a measure of how far it is from being toric: All toric pairs have charge zero, while all other anticanonical pairs have positive charge.

Remark 2.7. Let $( Y , D )$ be a pair.
An internal blow-up on $D _ { i }$ changes the cycle $\mathbf { d }$ by

$$
( \dots , d _ { i } , \dots ) \ \mapsto \ ( \dots , d _ { i } + 1 , \dots )
$$

and increases the charge by 1. A corner blow-up at $D _ { i } \cap D _ { i + 1 }$ changes the cycle $\mathbf { d }$ by

$$
( \dots , d _ { i } , d _ { i + 1 } , \dots ) \ \mapsto \ ( \dots , d _ { i } + 1 , 1 , d _ { i + 1 } + 1 , \dots )
$$

and keeps the charge constant.
A node smoothing at $D _ { i } \cap D _ { i + 1 }$ changes the cycle $\mathbf { d }$ by

$$
( \dots , d _ { i } , d _ { i + 1 } , \dots ) \ \mapsto \ ( \dots , d _ { i } + d _ { i + 1 } - 2 , \dots )
$$

and increases the charge by 1.

Consider a smoothing family $y  \Delta$ whose central fiber is the partially contracted hyperbolic Inoue surface with cusp singularity $p ^ { \prime }$ .
Using the same methods as Kulikov [8] and Persson and Pinkham [10] in their study of degenerations of K3 surfaces, Friedman and Miranda [1] prove that after a finite base change and bi-meromorphic modifications on $y  \Delta$ , we can produce a smooth family ${ \mathcal { X } } \to \Delta$ such that $\mathcal { D } \in \vert - K _ { \mathcal { X } } \vert$ is a divisor restricting to $D$ on every fiber and the central fiber is a simple normal crossings surface.
In analogy with so-called Type III degenerations of K3 surfaces, the central fiber

$$
\mathcal { X } _ { 0 } = \bigcup _ { i = 0 } ^ { n } V _ { i }
$$

of the family ${ \mathcal { X } } \to \Delta$ satisfies the following conditions:

i.
$V _ { 0 }$ is the hyperbolic Inoue surface with cycles $D$ and $D ^ { \prime }$ .
For $i > 0$ , the normalization $\tilde { V _ { i } }$ of each $V _ { i }$ is a smooth rational surface.
ii.
Let $D _ { i j }$ denote an irreducible double curve of $\mathcal { X } _ { 0 }$ lying on $V _ { i }$ and $V _ { j }$ (if $V _ { i }$ is not normal, we may have $i = j$ ).
Define $D _ { i }$ to be the union of the double curves $D _ { i j }$ contained in $V _ { i }$ .
Let ${ \tilde { D } } _ { i }$ be the inverse image of $D _ { i }$ under the normalization map $\tilde { V _ { i } }  V _ { i }$ .
Then

$$
( \tilde { V } _ { i } , \tilde { D } _ { i } )
$$

is an anticanonical pair for $i > 0$ and $D _ { 0 } = D ^ { \prime }$ .

iii.
(Triple Point Formula) Let $D _ { i j }$ be a double curve joining the surfaces $V _ { i }$ and $V _ { j }$ .
Then

$$
\left( D _ { i j } \big | _ { \tilde { V _ { i } } } \right) ^ { 2 } + \left( D _ { i j } \big | _ { \tilde { V _ { j } } } \right) ^ { 2 } = \left\{ \begin{array} { l l } { - 2 } & { \mathrm { i f ~ } D _ { i j } \mathrm { ~ i s ~ s m o o t h } } \\ { 0 } & { \mathrm { i f ~ } D _ { i j } \mathrm { ~ i s ~ n o d a l . } } \end{array} \right.
$$

iv.
The dual complex of $\mathcal { X } _ { 0 }$ is a triangulation of the sphere.

Definition 2.8. We call a surface $\mathcal { X } _ { 0 }$ satisfying conditions i.-iv.
a Type III anticanonical pair $( \mathcal { X } _ { 0 } , D )$ .

Conditions i.-iv.
are the only combinatorial conditions necessary to ensure that $\mathcal { X } _ { 0 }$ smooths to an anticanonical pair $( Y , D )$ in a family ${ \mathcal { X } } \to \Delta$ .
The remaining condition, $d$ -semistability, is analytic:

$$
T _ { \mathcal { X } _ { 0 } } ^ { 1 } : = \mathcal { E } x t _ { \mathcal { O } _ { \mathcal { X } _ { 0 } } } ^ { 1 } ( \Omega _ { \mathcal { X } _ { 0 } } ^ { 1 } , \mathcal { O } _ { \mathcal { X } _ { 0 } } ) \cong \mathcal { O } _ { s i n g ( \mathcal { X } _ { 0 } ) } .
$$

Any Type III anticanonical pair has a topologically trivial deformation to one which is $d$ -semistable by [1], Lemma 2.6. Motivated by the result of [2] in the case of Type III K3 surfaces, [1] prove that a $d$ -semistable Type III anticanonical pair $( \mathcal { X } _ { 0 } , D )$ smooths to an anticanonical pair $( Y , D )$ .
By a result of Shepherd-Barron [11], the union of the surfaces $V _ { i }$ for $i > 0$ can be contracted to a point, assuming we also contract the cycle $D ^ { \prime }$ on $V _ { 0 }$ .
Thus, the existence of $( \mathcal { X } _ { 0 } , D )$ implies that $D ^ { \prime }$ is smoothable.
Hence, the Friedman-Miranda criterion [1]:

Theorem 2.9. The cusp singularity associated to $D ^ { \prime }$ is smoothable if and only if there exists a Type III anticanonical pair $( \mathcal { X } _ { 0 } , D )$ .

Notation 2.10. To simplify the notation, we will henceforth suppress the tildes on $( \tilde { V } _ { i } , \tilde { D } _ { i } )$ so that $( V _ { i } , D _ { i } )$ denotes a smooth anticanonical pair.
In addition, we introduce the convention

$$
D _ { i j } = D _ { i j } { \big | } _ { V _ { i } } \ { \mathrm { ~ a n d ~ } } \ D _ { j i } = D _ { i j } { \big | } _ { V _ { j } }
$$

so that $D _ { i j }$ always denotes a curve on the smooth surface $V _ { i }$ .
Then $D _ { i j }$ and $D _ { j i }$ have equal image in $\mathcal { X } _ { 0 }$ but may not be isomorphic.
In fact, the image of $D _ { i j }$ in $\mathcal { X } _ { 0 }$ is nodal if and only if exactly one of $D _ { i j }$ or $D _ { j i }$ is nodal.
We define

$$
d _ { i j } : = { \left\{ \begin{array} { l l } { - D _ { i j } ^ { 2 } } & { { \mathrm { i f ~ } } \ell ( D _ { i } ) \geq 2 } \\ { 2 - D _ { i j } ^ { 2 } } & { { \mathrm { i f ~ } } \ell ( D _ { i } ) = 1 . } \end{array} \right. }
$$

Then, the triple point formula states that ${ d _ { i j } } + { d _ { j i } } = 2$ in all cases.

Proposition 2.11 (Conservation of Charge).
Let $( \mathcal { X } _ { 0 } , D )$ be a Type III anticanonical pair.
Then,

$$
\sum Q ( V _ { i } , D _ { i } ) = 2 4 .
$$

Proof.
See [1], Proposition 3.7.

q.e.d.

Conservation of charge is analogous to the Gauss-Bonnet formula, where curvature and charge are equated: The sum of the charges is a constant multiple of the Euler characteristic.
Toric surfaces, which have charge zero, are “flat” in some sense.
This analogy will take a precise form in the following section; we show that the dual complex $\Gamma ( \mathcal { X } _ { 0 } )$ of a Type III anticanonical pair $X _ { 0 }$ admits a natural integral-affine structure with singularities at the vertices corresponding anticanonical pairs $( V _ { i } , D _ { i } )$ of positive charge.
Imposing a singular, integral-affine “fan” structure on the dual complex of a maximally unipotent degeneration of a Calabi-Yau manifold plays a role in the Gross-Siebert program [6] for proving the SYZ conjecture.
For instance, the case of a Type III degeneration of K3 surfaces is specifically discussed in [5].

# 3. Integral-Affine Surfaces and Type III Anticanonical Pairs

Before defining the integral-affine structure on $\Gamma ( \mathcal { X } _ { 0 } )$ , we give some general definitions and propositions regarding integral-affine surfaces.
A basis triangle of $\mathbb { R } ^ { 2 }$ is a triangle of area $\begin{array} { l } { { \frac { 1 } { 2 } } } \end{array}$ with integral vertices.
The edges of a basis triangle pairwise form a lattice basis.

Definition 3.1. A triangulated integral-affine surface with singularities is a triangulated real surface $S$ , possibly with boundary, such that (1) the complement of the vertices $\{ v _ { i } \} \subset S$ of the triangulation admits an atlas of charts into $\mathbb { R } ^ { 2 }$ with transition functions valued in the integral-affine transformation group $S L _ { 2 } ( \mathbb { Z } ) \ltimes \mathbb { Z } ^ { 2 }$ and (2) the interior of every triangle admits a chart to a basis triangle.

Note that all labeled basis triangles are equivalent, up to a unique integral-affine transformation.
An integral-affine surface with singularities has a canonical orientation induced from the standard orientation on $\mathbb { R } ^ { 2 }$ .
Let $e _ { i j }$ denote a directed edge of the triangulation of $S$ going from $v _ { i }$ to $v _ { j }$ and let $f _ { i j k }$ denote a triangle whose counterclockwise-ordered vertices are $v _ { i }$ , $v _ { j }$ , and $v _ { k }$ .
Within an integral-affine chart containing the interior of the edge $e _ { i j }$ , we may view $e _ { i j }$ as the vector $v _ { j } - v _ { i }$ .

Remark 3.2. Because $S$ is triangulated into basis triangles, the boundary $P$ is polygonal: There is a decomposition of the boundary $\partial S = P _ { 1 } + \cdot \cdot \cdot + P _ { n }$ such that each $P _ { i }$ is integral-affine equivalent to a line segment between two lattice points.
By convention, we assume that the boundary components $P _ { i }$ are maximal: The union of two distinct boundary components is never integral-affine equivalent to a single line segment between two lattice points.

If the atlas of integral-affine charts on $S - \{ v _ { i } \}$ extends to all vertices $v _ { i }$ , then we say that $S$ is non-singular.
For the remainder of the paper, we will implicitly assume that an integral-affine surface has singularities and we will specify when an integral-affine surface is non-singular.

Definition 3.3. Let $S _ { s i n g }$ denote the vertices of the triangulation of $S$ to which the integral-affine structure fails to extend.

Remark 3.4. Let $S$ be an integral-affine surface with singularities.
A small contractible open subset $U \subset S - S _ { s i n g }$ has a chart $\phi _ { U } : U \to \mathbb { R } ^ { 2 }$ which is uniquely defined up to integral-affine transformation.
We can then construct a developing map

$$
\phi : \widetilde { S - S } _ { s i n g }  \mathbb { R } ^ { 2 }
$$

from the universal cover of $S - S _ { s i n g }$ to $\mathbb { R } ^ { 2 }$ by gluing together local charts $\phi { } _ { U }$ and $\phi _ { V }$ that agree on $U \cap V$ .
The map $\phi$ is uniquely determined up to post-composition with an element of $S L _ { 2 } ( \mathbb { Z } ) \ltimes \mathbb { Z } ^ { 2 }$ .
The developing map is equivalent to the data of the monodromy representation

$$
M : \pi _ { 1 } ( S - S _ { s i n g } )  S L _ { 2 } ( \mathbb { Z } ) \ltimes \mathbb { Z } ^ { 2 }
$$

constructed from the parallel transport of the integral-affine structure along a loop.
We also make use of the less refined monodromy map $N : \pi _ { 1 } ( S - S _ { s i n g } )  S L _ { 2 } ( \mathbb { Z } )$ which projects onto the $S L _ { 2 } ( \mathbb { Z } )$ part of the monodromy.

Definition 3.5. Let $e _ { i k }$ be a directed edge in the interior of a triangulated integral-affine surface.
Let $e _ { i j }$ and $e _ { i \ell }$ be the edges emanating from $v _ { i }$ directly clockwise and counterclockwise to $e _ { i k }$ .
We define the negative self-intersection $d _ { i k }$ of the edge $e _ { i k }$ by the formula

$$
d _ { i k } e _ { i k } = e _ { i j } + e _ { i \ell } ,
$$

where we view the edges as lattice vectors in some chart.
Note that $d _ { i k }$ is an integer because $( e _ { i j } , e _ { i k } )$ and $( e _ { i k } , e _ { i \ell } )$ are both oriented lattice bases and $d _ { i k }$ is independent of the choice of integral-affine chart.

Proposition 3.6. Let $S$ be a triangulated integral-affine surface with singularities.
The formula $d _ { i k } + d _ { k i } = 2$ holds for all interior edges $e _ { i k }$

Proof.
By working within an integral-affine chart, the formula reduces to the following equivalence:

$$
d _ { i k } ( v _ { k } - v _ { i } ) = ( v _ { j } - v _ { i } ) + ( v _ { \ell } - v _ { i } ) \Longleftrightarrow ( 2 - d _ { i k } ) ( v _ { i } - v _ { k } ) = ( v _ { j } - v _ { k } ) + ( v _ { \ell } - v _ { k } ) .
$$

We now show that the negative self-intersections of the edges uniquely determine the integral-affine structure on $S$ :

![](images/9b43385a90f458baedb95df4e09a3b2e208448af277afade00bdde2abf3bbfbc.jpg)  
Figure 1. The integral-affine structure on the union of $f _ { 1 2 3 }$ and $f _ { 1 3 4 }$ if $d _ { 1 3 } = - 1$ .

Proposition 3.7. A triangulated integral-affine surface $S$ is uniquely determined by the data of a collection of negative self-intersections $d _ { i k }$ for each directed interior edge $e _ { i k }$ such that $d _ { i k } + d _ { k i } = 2$ .

Proof.
We construct a unique integral-affine surface $S$ from the collection of integers $d _ { i k }$ .
We must declare each triangle $f _ { i j k }$ of $S$ to be integral-affine equivalent to a basis triangle.
We now show that the integral-affine structure extends to the interior of an edge in a unique manner such that the negative self-intersection of $e _ { i k }$ is $d _ { i k }$ .
Given a chart for $f _ { i j k }$ there is a unique way to glue to it a basis triangle $f _ { i k \ell }$ sharing the edge $e _ { i k }$ which satisfies $d _ { i k } e _ { i k } = e _ { i j } + e _ { i \ell }$ —this equation specifies $e _ { i \ell } = d _ { i k } e _ { i k } - e _ { i j }$ .
See Figure 1, for example.
Note that $e _ { i k }$ and $e _ { i \ell }$ form an oriented lattice basis, so the triangle $f _ { i k \ell }$ formed by these vectors is a basis triangle.
By Proposition 3.6, gluing the triangles $f _ { k \ell i }$ and $f _ { k i j }$ along the directed edge $e _ { k i }$ using the integer $d _ { k i }$ results in the same integral-affine structure on the quadrilateral $f _ { i j k } \cup f _ { i k \ell }$ .
Thus, we have defined an integral-affine structure on $S - \{ v _ { i } \}$ .
q.e.d.

We now determine when the non-singular integral-affine structure on $S \mathrm { ~ - ~ } \{ v _ { i } \}$ extends to an interior vertex $v _ { i }$ .
But first, we require the following definition:

Definition 3.8. Let $( V , D )$ be an anticanonical pair with cycle components $D = D _ { 1 } + \cdot \cdot \cdot + D _ { n }$ .
The pseudo-fan of $( V , D )$ is a triangulated integral-affine surface whose underlying triangulated surface is the cone over the dual complex of $D$ .
By Proposition 3.7, it suffices to declare that the negative-self intersection of the directed edge $e _ { i }$ pointing from the cone point to the vertex corresponding to a component $D _ { i }$ is

![](images/89ccc9075b6a199e234ec4895c2436691232834360b2eb434cd868de818393ab.jpg)  
Figure 2. The integral-affine structure on the pseudofan of the toric pair $( \mathbb { P } ^ { 2 } , \triangle )$ where $\bigtriangleup$ is a union of three lines in $\mathbb { P } ^ { 2 }$ forming a triangle.

$$
d _ { i } = { \left\{ \begin{array} { l l } { - D _ { i } ^ { 2 } } & { { \mathrm { i f ~ } } n > 1 } \\ { 2 - D _ { i } ^ { 2 } } & { { \mathrm { i f ~ } } n = 1 } \end{array} \right. } .
$$

The imposed integral-affine structure has at most one singularity, at the cone point.
Compare to Section 0.3.1 and Lemma 1.3 of [5].

Proposition 3.9. The integral-affine structure on the pseudo-fan of $( V , D )$ extends to the cone point if and only if $( V , D )$ is toric.

Proof.
First suppose that $( V , D )$ is a smooth, complete toric surface.
Then, the one-dimensional rays of the fan $\mathfrak { F }$ are spanned by primitive integral vectors $e _ { i }$ such that $( e _ { i } , e _ { i + 1 } )$ is an oriented lattice basis.
By Section 2.5 of [4], we have the equation

$$
- D _ { i } ^ { 2 } e _ { i } = e _ { i - 1 } + e _ { i + 1 } .
$$

Thus, the polygon whose vertices are the endpoints of the vectors $e _ { i }$ forms a single chart for the pseudo-fan of $( V , D )$ .
This integral-affine structure visibly extends over the origin.
See Figure 2.

Conversely, if the integral-affine structure on the pseudo-fan of $( V , D )$ extends to the cone point, then we may take a chart around the cone point centered at the origin.
The directed edges emanating from the cone point generate the one-dimensional rays of the fan of some toric surface.
This toric surface is necessarily isomorphic to $( V , D )$ because the integers $- D _ { i } ^ { 2 }$ determine the fan of $( V , D )$ up to $S L _ { 2 } ( \mathbb { Z } )$ equivalence.
Note that $( V , D )$ is automatically toric because $Q ( V , D ) = 0$ .
q.e.d.

Consider a Type III anticanonical pair $\mathcal { X } _ { 0 }$ .
The dual complex $\Gamma ( \mathcal { X } _ { 0 } )$ is a triangulation of $S ^ { 2 }$ whose vertices $v _ { i }$ correspond to components $V _ { i }$ , whose directed edges $e _ { i j }$ correspond to double curves $D _ { i j }$ , and whose triangular faces $f _ { i j k }$ correspond to triple points $T _ { i j k }$ .

Proposition 3.10. Let $\mathcal { X } _ { 0 }$ be a Type III anticanonical pair.
The dual complex $\Gamma ( \mathcal { X } _ { 0 } )$ has a triangulated integral-affine structure such that the edge $e _ { i j }$ has negative self-intersection

$$
d _ { i j } : = { \left\{ \begin{array} { l l } { - D _ { i j } ^ { 2 } } & { i f \ell ( D _ { i } ) \geq 2 } \\ { 2 - D _ { i j } ^ { 2 } } & { i f \ell ( D _ { i } ) = 1 . } \end{array} \right. }
$$

Furthermore, this integral-affine structure extends maximally to

$$
\Gamma ( { \mathcal X } _ { 0 } ) - \{ v _ { i } : Q ( V _ { i } , D _ { i } ) > 0 ~ o r ~ i = 0 \} .
$$

Proof.
The triple point formula states that ${ d _ { i j } } + { d _ { j i } } = 2$ , and so by Proposition 3.7, we have the first statement.
Proposition 3.9 plus the fact that $Q ( V _ { i } , D _ { i } ) = 0$ if and only if a pair $( V _ { i } , D _ { i } )$ is toric imply that the integral-affine structure fails to extend to $v _ { i }$ with $Q ( V _ { i } , D _ { i } ) > 0$ .
While it is plausible that $Q ( V _ { 0 } , D _ { 0 } ) = 0$ , the integral-affine structure does not extend to the vertex $v _ { 0 }$ corresponding to $V _ { 0 }$ —if it did, $\mathbf { d } ^ { \prime }$ would be the negative self-intersection sequence of the boundary components of some toric surface.
But $D _ { 0 } = D ^ { \prime }$ is negative-definite, whereas on a toric surface, the boundary components span the Picard group, which has indefinite intersection form.
q.e.d.

Definition 3.11. Let $v$ be a vertex of a triangulated integral-affine surface.
Denote by $s t a r ( v )$ the union of the triangles containing $v$ .

It is automatic from the definitions that for $\Gamma ( \mathcal { X } _ { 0 } )$ we have an equality between the pseudo-fan of $( V _ { i } , D _ { i } )$ and $s t a r ( v _ { i } )$ for all $i$ .
For convenience, we extend Definition 3.8 to allow the pair $( V _ { 0 } , D _ { 0 } )$ , so that we may also discuss the pseudo-fan of the hyperbolic Inoue surface.

We now record the effect of node smoothings and internal blow-ups on the pseudo-fan:

Proposition 3.12. Let $( \tilde { V } , \tilde { D } )$ be a deformation of an anticanonical pair $( V , D )$ such that $\tilde { D }$ is the smoothing of the node $D _ { i - 1 } \cap D _ { i }$ .
The pseudo-fan of $( \tilde { V } , \tilde { D } )$ is the result of the following surgery on the pseudofan of $( V , D )$ : Collapse the triangular face with edges $e _ { i }$ and $e _ { i + 1 }$ to $a$ single edge with negative self-intersection $d _ { i } + d _ { i + 1 } - 2$ .

Proposition 3.13. Let $( \tilde { V } , \tilde { D } )$ be an internal blow-up of an anticanonical pair $( V , D )$ on the component $D _ { i }$ .
The pseudo-fan of $( \tilde { V } , \tilde { D } )$ is the result of the following surgery on the pseudo-fan of $( V , D )$ : Keep the integral-affine structure fixed away from the edge $e _ { i }$ and increase the negative self-intersection of $e _ { i }$ from $d _ { i }$ to $d _ { i + 1 }$ .

Proof.
Both Propositions 3.12 and 3.13 follow immediately from Remark 2.7. q.e.d.

If one begins with a toric surface $( V , D )$ , the $S L _ { 2 } ( \mathbb { Z } )$ component of monodromy around the cone point after either surgery is conjugate to

$$
\left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 0 } } & { { 1 } } \end{array} \right) .
$$

In particular, monodromy of the pseudo-fan of an internal blow-up of a toric surface is a shear along the edge $e _ { i }$ corresponding to the component receiving the blow-up.

# 4. Surgeries on Integral-Affine Surfaces

We next describe surgeries on integral-affine surfaces that prove useful in the next section when constructing a Type III anticanonical pair $\mathcal { X } _ { 0 }$ .
These surgeries are motivated by work of Symington [12] on almost toric fibrations, with further details in Remark 4.1. For the remainder of this section, let $S$ denote a singular integral-affine surface which is homeomorphic to a disc, so that the polygonal boundary $\partial S$ is a circle.
That is, the boundary

$$
\partial S = P _ { 1 } + \cdot \cdot \cdot + P _ { n }
$$

is the union of a sequence of segments $P _ { i }$ put end-to-end, with each segment integral-affine equivalent to a straight line segment between two lattice points.
We index the boundary components $P _ { i }$ such that they go counterclockwise around $S$ as $i$ increases.
Let

$$
v _ { i , i + 1 } : = P _ { i } \cap P _ { i + 1 }
$$

denote a vertex of $\partial S$ and let $x _ { i }$ and $y _ { i }$ denote the primitive integral vectors emanating from $v _ { i , i + 1 }$ along $P _ { i + 1 }$ and $P _ { i }$ , respectively.
Thus, $y _ { i + 1 } = - x _ { i }$ in a local chart on $S$ containing the edge $P _ { i }$ .
We further assume that $( x _ { i } , y _ { i } )$ is an oriented lattice basis.
Consequently, the interior angles at the vertices of $P$ are less than $\pi$ in any integral-affine chart.

Remark 4.1. Let $( X , \omega )$ by a symplectic, toric surface—that is, a compact symplectic 4-manifold equipped with a Hamilton two-torus action.
If we think of $X$ as a complex toric surface, we can view the Hamiltonian two-torus action as the action of $S ^ { 1 } \times S ^ { 1 } \subset \mathbb { C } ^ { * } \times \mathbb { C } ^ { * }$ .
Recall that there is a moment map

$$
\mu : ( X , \omega ) \to S
$$

to a convex planar polygon $S$ (including its interior) such that the toric boundary components of $X$ map to the components of $\partial S$ .
The general fiber of $\mu$ is a Lagrangian torus, which degenerates on the edges of $S$ to a circle and on the vertices of $S$ to a point.
When $[ \omega ] \in H ^ { 2 } ( Y , \mathbb { Z } )$ is integral, the moment polygon can be taken to have integral vertices.
Then

$S$ satisfies the assumptions of this section—in particular, the vectors $x _ { i }$ and $y _ { i }$ form an oriented lattice basis.

Following Symington [12], an almost toric fibration is a Lagrangian fibration $\mu : ( X , \omega ) \to S$ whose general fiber is a smooth 2-torus, which undergoes symplectic reduction over the boundary $\partial \cal S$ , but whose interior fibers may also degenerate to necklaces of spheres at some finite set of points.
The almost toric base $S$ is a generalization of the moment polygon, and has a natural integral affine-linear structure, with $v \in S _ { s i n g }$ whenever the fiber $\mu ^ { - 1 } ( v )$ is singular.
The inverse image of $\partial \cal S$ is an anticanonical divisor of $X$ in the sense of symplectic geometry.

If $S$ is homeomorphic to a disc, then an almost toric fibration over $S$ is a symplectic anticanonical pair

$$
( Y , D , \omega )  S
$$

which sends the components of $\boldsymbol { D }$ to the components of $\partial S$ .
Symington defines two surgeries on $S$ : An internal blow-up and a node smoothing (in the terminology of [12], an almost toric blow-up and a nodal trade, respectively).
An internal blow-up of $S$ on the boundary component $P _ { i }$ is the base of an almost toric fibration of an internal blow-up of $( Y , D , \omega )$ on the component $D _ { i }$ , and an analogous statement holds for a node smoothing.

Definition 4.2. Choose a chart of $S$ containing a neighborhood of the edge $P _ { i }$ .
We define the negative self-intersection $d _ { i }$ of the boundary component $P _ { i }$ by the formula

$$
\begin{array} { c } { { d _ { i } y _ { i } = y _ { i - 1 } - x _ { i } } } \\ { { \ l ( = y _ { i - 1 } + y _ { i + 1 } ) . } } \end{array}
$$

If $( Y , D , \omega )  S$ is an almost toric fibration, then the negative selfintersection of the edge $P _ { i }$ is equal to the negative self-intersection $- D _ { i } ^ { 2 }$ of the component of $D$ fibering over $P _ { i }$ .

We do not define $d _ { i }$ by the formula $d _ { i } y _ { i } = y _ { i - 1 } + y _ { i + 1 }$ because $y _ { i + 1 }$ is not a vector based at a point on $P _ { i }$ and thus, may not be defined in our chosen neighborhood of $P _ { i }$ .
By extending our chart to a neighborhood of $P _ { i } \cup P _ { i + 1 }$ , this definition would become valid.
Note that Definition 4.2 fails when $P$ has only one boundary component, as no neighborhood of the single edge is contractible.
This problem is resolved by working in a chart on the universal cover of a neighborhood of the boundary component.

Definition 4.3. We define an internal blow-up of $S$ on the boundary component $P _ { i }$ .
First, delete a triangle $T \subset S$ satisfying:

1. One edge of $T$ is a proper subset of $P _ { i }$ .
2. The remainder of $T$ lies in the interior of $S - S _ { s i n g }$ .
3. $T$ is an integer multiple $n$ of a basis triangle.

![](images/0fff6ae428158aadbcd5cdac37f77eca194c640fc30aafb353b8b9b5b4bc327a.jpg)  
Figure 3. An internal blow-up on $P _ { i }$ of size 2.

![](images/f6e754b63abe92ac037833fcb4b8fdaafb577aa488863c34725bbef463372232.jpg)  
Figure 4. A node smoothing of $v _ { i , i + 1 }$ of size 2.

Let $v$ be the unique vertex of $T$ contained in the interior of $S$ .
Denote by $( e _ { 1 } , e _ { 2 } )$ the oriented lattice basis emanating from $v$ along the edges of $T$ .
See Figure 3. Glue the edge along $e _ { 2 }$ of $S - T$ to the edge along $e _ { 1 }$ of $S - T$ via the unique affine-linear map which fixes $v$ , maps $e _ { 2 } \mapsto e _ { 1 }$ , and preserves the line containing $P _ { i }$ .
The resulting integral-affine surface is an internal blow-up of $S$ on the boundary component $P _ { i }$ .
Its singular set is $S _ { s i n g } \cup \{ v \}$ .
Call $n$ the size of the surgery.

The gluing map is a shear transformation along the line through $\boldsymbol { v }$ parallel to $e _ { 2 } - e _ { 1 }$ .
An internal blow-up does not change the number of boundary components because the lefthand and righthand pieces of $P _ { i }$ are glued into a single line segment.
After the surgery, $( x _ { j } , y _ { j } )$ is still an oriented lattice basis for all $j$ because the internal blow-up does not alter the integral-affine structure in the neighborhood of a vertex.

Definition 4.4. We define a node smoothing of $S$ at $P _ { i } \cap P _ { i + 1 }$ .
For some $n \in \mathbb N$ , make a cut along the segment from $v _ { i , i + 1 }$ to a point

$$
v : = v _ { i , i + 1 } + n ( x _ { i } + y _ { i } )
$$

lying in $S - \partial S$ .
See Figure 4. Glue the clockwise edge of the cut (from the perspective of $\boldsymbol { v }$ ) to the counterclockwise edge of the cut by the shearing map which point-wise fixes the line containing the cut and maps $x _ { i }$ to $- y _ { i }$ .
The resulting integral-affine surface is a node smoothing of $S$ at $P _ { i } \cap P _ { i + 1 }$ .
Its singular set is $A \cup \{ v \}$ .
Call $n$ the size of the surgery.

Note that even though the gluing fixes the cut point-wise, it alters the integral-affine structure along the cut.
Let $e _ { 1 } : = - x _ { i } - y _ { i }$ be the primitive integral vector emanating from $\boldsymbol { v }$ along the cut, and let $e _ { 2 }$ be any vector such that $( e _ { 1 } , e _ { 2 } )$ is an oriented lattice basis.
Then, in the $( e _ { 1 } , e _ { 2 } )$ basis, the gluing map is

$$
\left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 0 } } & { { 1 } } \end{array} \right) .
$$

The gluing is independent of the choice of $e _ { 2 }$ because it is a shear fixing $e _ { 1 }$ .
The boundary of a node smoothing of $S$ has one fewer edge than $S$ : After a node smoothing, the edges $P _ { i }$ and $P _ { i + 1 }$ are straightened into a single edge because the image of $x _ { i }$ under the gluing map is $- y _ { i }$ .
As in the case of the internal blow-up, $( x _ { j } , y _ { j } )$ is still an oriented lattice basis for all $j \neq i$ after the surgery because the node smoothing does not alter the integral-affine structure in the neighborhood of a vertex $v _ { j , j + 1 }$ such that $j \neq i$ .
The vertex $v _ { i , i + 1 }$ ceases to exist after the surgery.

Proposition 4.5. An internal blow-up of $S$ on the boundary component $P _ { i }$ transforms the negative self-intersections of the boundary components as follows:

$$
( \dots , d _ { i } , \dots ) \mapsto ( \dots , d _ { i } + 1 , \dots )
$$

while smoothing the node $P _ { i } \cap P _ { i + 1 }$ of $S$ transforms the negative selfintersections of the boundary components as follows:

$$
( \dots , d _ { i } , d _ { i + 1 } , \dots ) \mapsto ( \dots , d _ { i } + d _ { i + 1 } - 2 , \dots ) .
$$

Proof.
We omit the proof of the proposition.
It follows from straightforward computations involving the gluing matrices and the vectors $x _ { i }$ and $y _ { i }$ .
Also, it is implicitly proven in [12], because the negative self-intersection of $P _ { i }$ from Definition 4.2 is equal to the negative selfintersection $d _ { i }$ of the component $D _ { i }$ which maps to $P _ { i }$ under an almost toric fibration.
q.e.d.

We now describe how to complete the disc $S$ to a sphere when the boundary is negative, in the appropriate sense:

![](images/d26501c780a7c098c626bda219ae3dac85076babcd7d658b1aa9e9cfaea020d6.jpg)  
Figure 5. The image of the developing map of a collar neighborhood of the boundary of $S$ .

Proposition 4.6. Let $S$ be an integral-affine disc such that adjacent edges of $\partial S$ meet to form lattice bases and the negative self-intersections of components $P _ { i } \subset \partial S$ satisfy

$$
\begin{array} { l l } { { d _ { i } \geq 2 } } & { { \quad f o r \ a l l \ i , } } \\ { { d _ { i } \geq 3 } } & { { \quad f o r \ s o m e \ i . } } \end{array}
$$

Then there is an natural embedding $S \hookrightarrow \hat { S }$ into an integral-affine sphere such that $\hat { S } _ { s i n g } = S _ { s i n g } \cup \{ v _ { 0 } \}$ for a distinguished point $v _ { 0 } \in \hat { S } - S$ .

Proof.
Let $U \supset \partial S$ be a collar neighborhood of the boundary of $S$ containing no singular points.
Note that $\pi _ { 1 } ( U ) = \mathbb { Z }$ .
Consider the developing map

$$
\phi : \tilde { U } \to \mathbb { R } ^ { 2 }
$$

from the universal cover of $U$ to $\mathbb { R } ^ { 2 }$ .
The universal cover $\widetilde { \partial S }$ of the boundary maps to an infinite lattice polygon in $\mathbb { R } ^ { 2 }$ .
Each edge $P _ { i }$ is integral-affine equivalent to some interval $[ 0 , m i ]$ on the $x$ -axis, for a unique $m _ { i } \in \mathbb { N }$ .
Then $\phi ( { \widetilde { \partial S } } )$ is an infinite sequence of vectors $\{ m _ { i } z _ { i } \} _ { i \in \mathbb { Z } }$ put end-to-end, such that $\left( z _ { i + 1 } , - z _ { i } \right)$ is an oriented lattice basis, and

$$
d _ { i } z _ { i } = z _ { i - 1 } + z _ { i + 1 }
$$

for all $i$ (the indices of $m _ { i }$ and $d _ { i }$ are taken mod $n$ ).
We call $\phi ( { \widetilde { \partial S } } )$ a discrete hyperbola.
The interior angles of the discrete hyperbola are less than $\pi$ because $( z _ { i + 1 } , - z _ { i } )$ is a lattice basis for all $i \in \mathbb { Z }$ .
One possible image of $\tilde { U }$ under the developing map is shown in Figure 5 with the lower edge forming the discrete hyperbola.

We claim that the discrete hyperbola has two asymptotic lines $L _ { 1 }$ and $L _ { \mathrm { 2 } }$ which are the invariant lines of the monodromy transformation $M : =$ $M ( \gamma )$ associated to a counterclockwise loop $\gamma$ around the boundary of $S$ .
The change-of-basis from $\left( z _ { i } , - z _ { i - 1 } \right)$ to $( z _ { i + 1 } , - z _ { i } )$ is

$$
\left( \begin{array} { c c } { { d _ { i } } } & { { - 1 } } \\ { { 1 } } & { { 0 } } \end{array} \right) .
$$

Therefore, the $S L _ { 2 } ( \mathbb { Z } )$ part of the monodromy $N : = N ( \gamma )$ is conjugate in $S L _ { 2 } ( \mathbb { Z } )$ to the product

$$
\prod _ { i = 1 } ^ { n } { \binom { d _ { i } } { 1 } } \quad { \begin{array} { l } { - 1 } \\ { 0 } \end{array} } \quad
$$

because the counterclockwise monodromy is conjugate to the changeof-basis from $( z _ { 1 } , - z _ { 0 } )$ to $\left( z _ { n + 1 } , - z _ { n } \right)$ .
By choosing a basis properly, we may assume that $N$ is equal to the above product.
The full $S L _ { 2 } ( \mathbb { Z } ) \ltimes \mathbb { Z } ^ { 2 }$ monodromy transformation is then

$$
M \cdot v = N \cdot v + B
$$

for some $B \in \mathbb { Z } ^ { 2 }$ .
Since $( d _ { 1 } , \ldots , d _ { n } )$ is negative-definite, $\operatorname { t r } N > 2$ and therefore $N$ has two distinct, irrational positive eigenvalues.
We solve the equation $v = N \cdot v + B$ to find the unique, rational fixed point

$$
v _ { 0 } : = ( I - N ) ^ { - 1 } B
$$

of $M$ .
Then $L _ { 1 }$ and $L _ { \mathrm { 2 } }$ are the lines going through $v _ { 0 }$ parallel to the eigenvectors of $N$ .

The invariant line associated to the eigenvalue greater than one is stable, while the other invariant line is unstable.
To prove that the discrete hyperbola is asymptotic to $L _ { 1 }$ and $L _ { 2 }$ , we note that the monodromy transformation $M$ sends the discrete hyperbola to itself by mapping

$$
M : \phi ( \tilde { P } _ { i } ) \mapsto \phi ( \tilde { P } _ { i + n } ) .
$$

Thus, the edges $\phi ( { \tilde { P } } _ { i } )$ of the discrete hyperbola approach the stable and unstable invariant lines of $M$ as the index $i$ approaches positive and negative infinity, respectively.
The discrete hyperbola bounds a convex region because its interior angles are less than $\pi$ .
Any line going though $v _ { 0 }$ between $L _ { 1 }$ and $L _ { \mathrm { 2 } }$ eventually intersects this region, because the discrete hyperbola approaches the eigenlines of $M$ .
Then, convexity implies that the complement of this convex region is star-shaped at $v _ { 0 }$ .

Let $R$ denote the region bounded by $L _ { 1 }$ , $L _ { \mathrm { 2 } }$ , and the discrete hyperbola, with partial boundary $\phi ( { \widetilde { \partial S } } )$ .
Let $L$ be any line going through $v _ { 0 }$ between $L _ { 1 }$ and $L _ { 2 }$ (for instance, we may assume $L$ is a line through $v _ { 0 }$ and a vertex of the discrete hyperbola).
Then the region bounded by $L$ , $M \cdot L$ , and $\phi ( { \widetilde { \partial S } } )$ is a fundamental domain for the action of $M$ on $R$ , see Figure 6. The orbit space

$$
C : = \{ M ^ { n } : n \in \mathbb { Z } \} \backslash R
$$

![](images/08725b354208ed8177fa02ba3994b08bb0e70923511f5aef2070db9ccfdadc5c.jpg)  
Figure 6. A fundamental domain for the action of $M$ on $R$ .

inherits an integral-affine structure from $R$ non-singular away from $v _ { 0 }$ .
Furthermore $C$ is cone over $\partial S$ such that $C _ { s i n g } = \{ v _ { 0 } \}$ and the orientations on $C$ and $S$ induce opposite orientations on $\partial S$ .
Then, we define $\hat { S }$ to be the result of gluing $C$ and $S$ along their boundaries.

More precisely, we can form a quotient

$$
\{ M ^ { n } : n \in \mathbb { Z } \} \backslash ( \phi ( { \tilde { U } } ) \cup R ) = U \cup C
$$

and $U \cup C$ glues to $S$ along $U$ to produce an integral-affine sphere $\hat { S }$ such that ${ \hat { S } } _ { s i n g } = S \cup \{ v _ { 0 } \}$ .
q.e.d.

We note that $v _ { 0 }$ may only have rational coordinates.
Thus, even if $S$ admits a triangulation, $\hat { S }$ may not.
Hence we define:

Definition 4.7. Let $S$ be an integral-affine surface.
The order $k$ refinement $S [ k ]$ is produced by post-composing the charts on $S$ with multiplication by $k$ .

Note that $S [ k ] _ { s i n g }$ and $S _ { s i n g }$ are naturally identified.
We remark without proof that the order $k$ refinement of $\Gamma ( \mathcal { X } _ { 0 } )$ corresponds to a SNC resolution of the order $k$ base change of ${ \mathcal { X } } \to \Delta$ .

Remark 4.8. Let $S$ be as in Proposition 4.6. Then the point $v _ { 0 }$ in the definition of $\hat { S }$ may not be integral, but as it is rational, there exists some $k$ such that $v _ { 0 }$ lies at an integral point of $\hat { S } [ k ]$ .
Then if $S$ can be triangulated into basis triangles, so can ${ \hat { S } } [ k ] = S [ k ] \cup C [ k ]$ , as $C [ k ]$ has a fundamental domain given by a lattice polygon, see Figure 6, and thus can easily be triangulated into basis triangles.

# 5. A Proof of Looijenga’s Conjecture

In this section, we present the construction of a Type III anticanonical pair $( \mathcal { X } _ { 0 } , D )$ from an anticanonical pair $( Y , D )$ , thus proving Looijenga’s conjecture.
But first, we need:

Proposition 5.1. Every anticanonical pair $( Y , D )$ can be expressed as a sequence of node smoothings and internal blow-ups starting with $a$ toric pair $( \overline { { Y } } , \overline { { D } } )$ .

Proof.
First, we express $( Y , D )$ as a sequence of corner and internal blow-ups of a minimal anticanonical pair $( Y _ { 0 } , D _ { 0 } )$ .
We factor the blowdown to $( Y _ { 0 } , D _ { 0 } )$ into maps $\alpha$ and $\beta$

$$
( Y , D ) \stackrel { \alpha } {  } ( Y _ { 1 } , D _ { 1 } ) \stackrel { \beta } {  } ( Y _ { 0 } , D _ { 0 } )
$$

such that $\alpha$ consists only of interior blow-ups, while $\beta$ consists only of corner blow-ups, cf.
Remark 2.6 of [3].
By direct examination (see Lemma 3.2 of [1]), every minimal anticanonical pair $( Y _ { 0 } , D _ { 0 } )$ is a node smoothing of a minimal toric anticanonical pair, i.e. there is a family of anticanonical pairs with cycle $D _ { 0 }$ that degenerates to a toric pair.
Performing all the corner blow-ups of $\beta$ on this family expresses $( Y _ { 1 } , D _ { 1 } )$ as a node smoothing of a toric pair $( \overline { { Y } } , \overline { { D } } )$ .
Thus, $( Y , D )$ is the result of interior blow-ups and node smoothings on $( \overline { { Y } } , \overline { { D } } )$ .
q.e.d.

Theorem 5.2 (Looijenga’s Conjecture).
If $D$ is the anticanonical divisor of some rational surface, then the cusp singularity associated to $D ^ { \prime }$ is smoothable.

Proof.
Let $( Y , D )$ be an anticanonical pair.
We express $( Y , D )$ as a sequence of node smoothings and internal blow-ups on a toric pair $( \overline { { Y } } , \overline { { D } } )$ .
From this data, we construct a Type III anticanonical pair $\mathcal { X } _ { 0 }$ :

Construction: Let $\overline { S }$ be a moment polygon for $( \overline { { Y } } , \overline { { D } } )$ with integral vertices.
Then $S$ is an integral-affine disc with no singularities, such that $( x _ { i } , y _ { i } )$ is an oriented lattice basis.
The components ${ \overline { { P } } } _ { i } ~ \subset ~ \partial { \overline { { S } } }$ of the boundary have negative self-intersections $- \overline { { D } } _ { i } ^ { 2 }$ for all $i$ , in the sense of Definition 4.2. In fact we may simply choose a polygon $\overline { S }$ with this property, should we wish to avoid an appeal to symplectic geometry.

For each internal blow-up or node smoothing of $( \overline { { Y } } , \overline { { D } } )$ applied to produce $( Y , D )$ , we perform an associated internal blow-up or node smoothing surgery on the integral-affine surface $\overline { S }$ .
Assume that all surgeries have size 1, i.e. internal blow-ups remove a single basis triangle and node smoothings have cuts of minimal length, as in the example below.
We are applying $Q ( Y , D )$ surgeries of fixed size, but $\overline { S }$ may be chosen to be arbitrarily large (e.g. by scaling).
Thus we can ensure, and in fact we require, that $\overline { S }$ can accommodate all the necessary surgeries.
We denote the resulting integral-affine surface by $S$ .

![](images/7f30e8c6e789116bacba0d22910205ce42cfcf987b051735f1a4e96bc973ef83.jpg)  
Figure 7. A moment polygon $\overline { S }$ for $\overline { { Y } }$ .

By Proposition 4.5, the negative self-intersections of the boundary components $P _ { i } ~ \subset ~ \partial S$ are equal to the negative self-intersections $d _ { i }$ of the components of $D$ .
By Remark 4.1, $S$ is the base of an almost toric fibration of a symplectic rational surface $( Y , D , \omega )$ .
For example, Figure 7 is a moment polygon $S$ for the toric surface

$$
( \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 } , \overline { { D } } _ { 1 } + \overline { { D } } _ { 2 } + \overline { { D } } _ { 3 } + \overline { { D } } _ { 4 } ) .
$$

Figure 8 demonstrates 18 surgeries on $\bar { S }$ corresponding to four internal blow-ups on $\overline { { D } } _ { 1 }$ , two internal blow-ups on $\overline { { D } } _ { 2 }$ , six internal blow-ups on $\overline { { D } } _ { 3 }$ , five internal blow-ups on $\overline { { D } } _ { 4 }$ and a node smoothing of $\overline { { D } } _ { 1 } \cap \overline { { D } } _ { 2 }$ .
After the surgeries, the integral-affine surface $S$ is the almost toric base of a negative-definite anticanonical pair $( Y , D , \omega )$ with $\mathbf { d } = ( d _ { 1 } , d _ { 2 } , d _ { 3 } ) =$ $( 4 , 6 , 5 )$ .
The charge of $( Y , D )$ is 18, because each surgery increases the charge by 1.

The surgeries retain the property that $( x _ { i } , y _ { i } )$ is an oriented lattice basis, and hence $\partial S$ satisfies the conditions of Proposition 4.6. Thus, we may complete $S$ to a sphere $\hat { S } = S \cup C$ .
Note that $S$ admits a triangulation into basis triangles, for instance, we may triangulate the polygonal fundamental domain shown in Figure 8. By Remark 4.8, we may take an order $k$ refinement ${ \hat { S } } [ k ]$ such that $\hat { S } [ k ]$ admits a triangulation into basis triangles.
Now that we have established the existence of such a triangulation, we choose amongst all of them the one which attains the minimal possible number of edges emanating from $v _ { 0 }$ .

![](images/7acf850aa2097a53f4448b84824eadf9c54c21afe5194b0347b20b4c425eec91.jpg)  
Figure 8. An almost toric base $S$ for $Y$ .

Let $v _ { i }$ be a vertex of the triangulation of $\hat { S } [ k ]$ which is non-singular.
Then $s t a r ( v _ { i } )$ is the pseudo-fan of some toric surface $( V _ { i } , D _ { i } )$ .
Now suppose that $v _ { i } \in S | k | _ { s i n g }$ is a singular point not equal to $v _ { 0 }$ .
Each such singularity $v _ { i }$ is introduced by a surgery on $S$ .
Let $\overline { { v } } _ { i } \in \overline { { S } }$ denote the pre-image of $v _ { i } \in S$ .
In the case of an internal blow-up, one of the triangular faces of $s t a r ( \overline { { v } } _ { i } )$ is collapsed by the surgery, whereas in the case of a node smoothing, the integral-affine structure along an edge of $s t a r ( \overline { { v _ { i } } } )$ is changed.
In fact:

1. An internal blow-up on $S$ corresponds to a node smoothing on $s t a r ( \overline { { v } } _ { i } )$ by Proposition 3.12 and Definition 4.3. 2) A node smoothing on $\overline { S }$ corresponds to an internal blow-up on $s t a r ( \overline { { v } } _ { i } )$ by Proposition 3.13 and Definition 4.4.

We conclude that there is an anticanonical pair $( V _ { i } , D _ { i } )$ whose pseudofan is $s t a r ( v _ { i } )$ for all $i \neq 0$ .

Finally, we consider $v _ { 0 }$ .
The monodromy $N = N ( \gamma )$ of a counterclockwise loop around the boundary $\partial S$ is equal to the monodromy of a clockwise loop around $v _ { 0 }$ .
Thus, the monodromy of a counterclockwise loop around $v _ { 0 }$ is $N ^ { - 1 }$ .

Lemma 5.3. The pseudo-fan of $( V _ { 0 } , D ^ { \prime } )$ is isomorphic to $s t a r ( v _ { 0 } )$

Proof.
Let $\mathbf { d } _ { 0 } = ( d _ { 0 1 } , \ldots , d _ { 0 r } )$ denote the negative self-intersections of the edges $( e _ { 0 1 } , \ldots , e _ { 0 r } )$ emanating from $v _ { 0 }$ .
We claim that $d _ { 0 i } \geq 2$ for all $i$ .
First, we show that $d _ { 0 i } \leq 0$ is impossible.
Suppose for the sake of contradiction that $d _ { 0 i } \leq 0$ .
Then the formula

$$
d _ { 0 i } e _ { 0 i } = e _ { 0 ( i - 1 ) } + e _ { 0 ( i + 1 ) }
$$

implies that the angle $\mathscr { L } ( v _ { i - 1 } v _ { 0 } v _ { i + 1 } )$ subtended by $s t a r ( v _ { 0 } )$ between $e _ { 0 ( i - 1 ) }$ and $e _ { 0 ( i + 1 ) }$ is at least $\pi$ in any integral-affine chart.
But, by the definition of the integral-affine structure on $C$ from Proposition 4.6, the image of the developing map of $s t a r ( v _ { 0 } )$ lies within the region $R$ .
Thus $d _ { 0 i } \leq 0$ is impossible, because the image of the developing map of $s t a r ( v _ { 0 } )$ subtends an angle less than $\pi$ —it subtends the angle formed at $v _ { 0 }$ by $L _ { 1 }$ and $L _ { 2 }$ .

If $d _ { 0 i } ~ = ~ 1$ , then the union of the two triangles containing $e _ { 0 i }$ is integral-affine equivalent to the unit square.
But then we may alter the triangulation by flipping the diagonal of this square, thus decreasing the total number of edges emanating from $v _ { 0 }$ .
This contradicts our assumption that the number of edges emanating from $v _ { 0 }$ is minimal.
Hence $d _ { 0 i } \geq 2$ for all $i$ .
If $d _ { 0 i } = 2$ for all $i$ , then the image of developing map subtends an angle of exactly $\pi$ , which is also impossible.
Hence $d _ { 0 i } \geq 3$ for some $i$ .
Thus ${ \bf d } _ { 0 }$ is negative-definite.
We remark that similar ideas arise when constructing minimal resolutions of non-smooth toric surfaces, see Section 2.6 of [4].

The developing map, when restricted to the boundary of $s t a r ( v _ { 0 } )$ , maps to an infinite lattice polygon lying in $R$ and bounded by $L _ { 1 }$ and $L _ { 2 }$ .
Because ${ \bf d } _ { 0 }$ is negative-definite, the angles of this infinite lattice polygon are less than $\pi$ , and thus, it bounds a convex region.
Furthermore, the image of the developing map of $s t a r ( v _ { 0 } )$ contains no lattice points in its interior because it is a union of basis triangles containing $v _ { 0 }$ .
See Figure 9. This uniquely characterizes the image of the developing map of $s t a r ( v _ { 0 } )$ : It is the region between $L _ { 1 }$ and $L _ { 2 }$ in the complement of the convex hull of the lattice points between $L _ { 1 }$ and $L _ { 2 }$ .
We say $s t a r ( v _ { 0 } )$ has property $( { \star } )$ .

Let $\mathbf { d } = \left( d _ { 1 } , \ldots , d _ { n } \right)$ and $\mathbf { d } ^ { \prime } = ( d _ { 1 } ^ { \prime } , \ldots , d _ { s } ^ { \prime } )$ .
The following matrices are conjugate in $S L _ { 2 } ( \mathbb { Z } )$ :

$$
\prod _ { i = 1 } ^ { r } { \binom { 0 } { 1 } } \sim N ^ { - 1 } = \left[ \prod _ { i = 1 } ^ { n } { \binom { d _ { i } } { 1 } } \right] ^ { - 1 } \sim \prod _ { i = 1 } ^ { s } { \binom { 0 } { 1 } } \ - \ d _ { i } ^ { \prime } \
$$

where the last similarity is a general fact about dual cycles, see [7].
That is, the monodromy of $s t a r ( v _ { 0 } )$ is conjugate to the monodromy of the pseudo-fan of $( V _ { 0 } , D ^ { \prime } )$ .
By post-composing with an integral-affine transformation, we may assume that these monodromies are equal and that the developing map of the pseudo-fan of $( V _ { 0 } , D ^ { \prime } )$ maps into the region between $L _ { 1 }$ and $L _ { 2 }$ .
Since $\mathbf { d } ^ { \prime }$ is negative-definite, the image of the developing map of the pseudo-fan of $( V _ { 0 } , D ^ { \prime } )$ is also characterized by property $( \star )$ .
Since the monodromy acts the same on these images, the pseudo-fan of $( V _ { 0 } , D ^ { \prime } )$ and $s t a r ( v _ { 0 } )$ are isomorphic, as triangulated integral-affine surfaces.
q.e.d.

![](images/95ec7363a83d7b3367d280dd47fad4308aa2fb34eb1695907f5fbb1da8f57efc.jpg)  
Figure 9. The image of the developing map of $s t a r ( v _ { 0 } )$ .

For every vertex $v _ { i }$ with $i \neq 0$ of the triangulation of $\hat { S } [ k ]$ , we have found an anticanonical pair $( V _ { i } , D _ { i } )$ whose pseudo-fan is $s t a r ( v _ { i } )$ .
In addition, we have proved that the pseudo-fan of $( V _ { 0 } , D ^ { \prime } )$ is $s t a r ( v _ { 0 } )$ .
Consider the union of the surfaces

$$
\chi _ { 0 } : = \bigcup _ { v _ { i } \in \hat { S } [ k ] } ( V _ { i } , D _ { i } )
$$

where we identify $D _ { i j }$ with $D _ { j i }$ so that nodes of $D _ { i }$ are identified with nodes of $D _ { j }$ .
By Remark 3.6, $\mathcal { X } _ { 0 }$ satisfies the triple point formula.
So $\mathcal { X } _ { 0 }$ satisfies all the assumptions of a Type III anticanonical pair $( \mathcal { X } _ { 0 } , D )$ .
Theorem 2.9 implies that the cusp with resolution $D ^ { \prime }$ is smoothable.
q.e.d.

We now describe without proof a number of modifications of the construction, which still produce a Type III anticanonical pair $\mathcal { K } _ { 0 }$ but in which various conditions are weakened.

Modification 5.4. We need not assume that the singularities introduced in the surgeries on $S$ are distinct.
The number of surgeries in which the vertex $v _ { i }$ is involved (either as the vertex of a triangle removed from $\overline { S }$ for an internal blow-up, or as the end of a cut for a node smoothing) is equal to the charge $Q ( V _ { i } , D _ { i } )$ of the anticanonical pair whose pseudo-fan is $s t a r ( v _ { i } )$ .
In addition, the edges of the triangles removed for internal blow-ups may overlap, and may also overlap cuts for node smoothings.

Modification 5.5. We assumed that for every component of $\overline { { D } }$ , the length of the associated boundary component of $\overline { S }$ was positive.
This assumption is unnecessary—some may have length zero (but at least three edges must have positive length, because $\overline { S }$ must have nonempty interior to make surgeries).

Modification 5.6. The internal blow-ups on a boundary component of $S$ decrease its length.
After the surgeries, we may allow some of the boundary components of $S$ to have length zero.
When only some of the boundary components have length zero, we continue with the construction by applying the developing map to a collar neighborhood of the boundary, even though $( x _ { i } , y _ { i } )$ may cease to be a lattice basis.

Modification 5.7. If, after the surgeries, all the boundary components have length zero, then $S$ has no boundary, and is already homeomorphic to a sphere.
Then we may triangulate $S$ directly to produce the dual complex $\Gamma ( \mathcal { X } _ { 0 } )$ of a Type III anticanonical pair.

Remark 5.8. Modification 5.7 is always possible, thus eliminating the need for the completion process described in Proposition 4.6, but the construction is significantly more delicate.

We now present an example incorporating Modifications 5.4, 5.5, and 5.7 of the construction of $\mathcal { X } _ { 0 }$ :

Example 5.9. Let $( Y , D )$ be a negative-definite anticanonical pair such that $Q ( Y , D ) = 3$ .
It can be shown that all negative-definite anticanonical pairs with $Q ( Y , D ) = 3$ have three disjoint internal exceptional curves, which can be blown down to a toric surface

$$
\pi : ( Y , D )  ( { \overline { { Y } } } , { \overline { { D } } } ) .
$$

We call $( \overline { { Y } } , \overline { { D } } )$ a toric model.
Let $\overline { { D } } _ { a _ { 1 } }$ , $\overline { { { D } } } _ { a _ { 2 } }$ , and $\overline { { D } } _ { a _ { 3 } }$ be the three components of $\overline { { D } }$ that receive the internal blow-ups.
Up to scaling by $\mathbb { Z }$ , there is a unique moment polygon $\bar { S }$ of the toric model in which the boundary components $\overline { { P } } _ { a _ { 1 } }$ , $\overline { { P } } _ { a _ { 2 } }$ , and $\overline { { P } } _ { a _ { 3 } }$ are the only edges with nonzero length.

To construct $S$ , we perform internal blow-ups on the three boundary components of $\bar { S }$ .
To do so, we must delete a multiple of a basis triangle from each of the edges.
For any anticanonical pair $( Y , D )$ of charge three, it can be proven that $\overline { S }$ has room to perform internal blow-ups that decrease the lengths of all three edges to zero.
So $\partial S$ is empty, and $S$ may be directly triangulated into basis triangles, from which we construct $\mathcal { X } _ { 0 }$ .

Consider the cusp singularity $D ^ { \prime }$ with cycle $\mathbf { d } ^ { \prime } = ( 6 , 9 )$ .
The dual cycle is given by the formula

$$
\mathbf { d } = ( 3 , 2 , 2 , 2 , 3 , 2 , 2 , 2 , 2 , 2 , 2 ) .
$$

There are two distinct deformation families of pairs with anticanonical cycle $\boldsymbol { D }$ .
The deformations preserve the classes of exceptional curves, so each deformation family is associated to a different toric model.
Let $( ^ { \imath } Y , D )$ with $i = 1 , 2$ be two anticanonical pairs representing these two deformation families.
The cycles of negative self-intersections of the two toric models are

![](images/51876ccdc3f83cedff7ac150422f97e6670de14acfffc4ce9406b5a71e8007e0.jpg)  
Figure 10. Moment polygons for $( ^ { i } \overline { { Y } } , { ^ { i } \overline { { D } } } )$ .

![](images/f8a1b23dbceab5a750533ac6d2821daf6cedd07cac97e6eb33b4d591cd23edba.jpg)  
Figure 11. Almost toric bases for $( ^ { i } Y , D )$ .

![](images/72ef5e978e2221073dbf910fe4e3a393c2486aa64766c022401a46b3d8e12e19.jpg)  
Figure 12. Two Type III anticanonical pairs $( { \small \mathscr { X } } _ { 0 } , D )$ .

$$
\begin{array} { c } { { \overline { { \bf d } } = ( 3 , 2 , 1 , 2 , 3 , 1 , 2 , 2 , 2 , 2 , 1 ) } } \\ { { \overline { { \bf d } } = ( 3 , 2 , 2 , 1 , 3 , 2 , 1 , 2 , 2 , 2 , 1 ) } } \end{array}
$$

By blowing down exceptional curves in $^ { i } D$ , we can draw fans for $( ^ { i } \overline { { Y } } , { ^ { i } \overline { { D } } } )$ , from which we can construct moment polygons $^ { i } { \overline { { S } } }$ for $i = 1 , 2$ .
Using Modification 5.5, we choose a moment polygon $^ { 1 } \partial \overline { { S } }$ whose only boundary components of positive length are ${ } ^ { 1 } \overline { { P } } _ { 3 }$ , ${ } ^ { 1 } \overline { { P } } _ { 6 }$ , and $^ 1 \overline { { P } } _ { 1 1 }$ , while the only components of $^ { 2 } \partial \overline { { S } }$ of positive length are $^ 2 \overline { { P } } _ { 4 }$ , $^ { 2 } { \overline { { P } } } _ { 7 }$ , and $^ 2 \overline { { P } } _ { 1 1 }$ as in Figure 10.

We perform three internal blow-ups on $^ { i } { \overline { { S } } }$ by deleting a multiple of a basis triangle resting on each of the three edges, then gluing the remaining two edges of each triangle.
Furthermore, using Modification 5.7, we choose surgeries large enough to reduce the length of the boundary to zero.
The resulting integral affine surfaces $^ i S$ are shown Figure 11. Because $^ { i } S$ has no boundary, we immediately triangulate it into basis triangles, and construct the simple normal crossings surface ${ } ^ { i } X _ { 0 }$ whose dual complex is $^ i S$ .
Note that Modification 5.4 has been applied to $^ { 1 } S$ as two singularities introduced by surgeries overlap.
The triangulations of $^ { i } S$ and the surfaces ${ } ^ { i } X _ { 0 }$ are shown in Figure 12. The hyperbolic Inoue pair $( V _ { 0 } , D ^ { \prime } )$ is the outer face in both illustrations.

The surface ${ } ^ { i } X _ { 0 }$ smooths to give a family ${ } ^ { i } \mathcal { X }  \Delta$ of surfaces over the disc whose general fiber is a pair with anticanonical cycle $D$ .
It is a natural question to ask whether the general fiber of $^ { i } X$ is deformationequivalent to $( ^ { \imath } Y , D )$ .
In later work, we provide an affirmative answer to this question, verifying Conjecture 6.1 of [1].
To prove smoothability of the cusp $D ^ { \prime } = ( 6 , 9 )$ , Friedman and Miranda exhibited the special fiber $^ { 1 } \mathcal { X } _ { 0 }$ .
The surface $^ { 2 } \mathcal { X } _ { 0 }$ is the alternative special fiber with 50 triple points that they conjectured to exist.

# References

[1] Robert Friedman and Rick Miranda.
Smoothing cusp singularities of small length.
Mathematische Annalen, 263(2):185–212, 1983.  
[2] Robert Friedman.
Global smoothings of varieties with normal crossings.
Annals of Mathematics, 118(1):75–114, 1983.  
[3] Robert Friedman.
On the geometry of anticanonical pairs.
arXiv preprint 1502.02560, 2015.  
[4] William Fulton.
Introduction to toric varieties.
Annals of mathematics studies.
Princeton Univ.
Press, Princeton, NJ, 1993.  
[5] Mark Gross, Paul Hacking, and Sean Keel.
Mirror symmetry for log Calabi-Yau surfaces I.
Publications mathmatiques de l’IHES´ , 122(1):65-168, 2015.  
[6] Mark Gross and Bernd Siebert.
Affine manifolds, log structures, and mirror symmetry.
Turkish J.
Math, 27:33–60, 2003.  
[7] Masahisa Inoue.
New surfaces with no meromorphic functions, II.
In Complex analysis and algebraic geometry, 91–106.
Iwanami Shoten, Tokyo, 1977.  
[8] Viktor Kulikov.
Degenerations of K3 surfaces and Enriques surfaces.
Math.
USSR Izvestija, 11:957–989, 1977.  
[9] Eduard Looijenga.
Rational surfaces with an anticanonical cycle.
Annals of Mathematics, 114(2):267–322, 1981.  
[10] Ulf Persson and Henry Pinkham.
Degeneration of surfaces with trivial canonical bundle.
Annals of Mathematics, 113(1):45–66, 1981.  
[11] Nicholas Shepherd-Barron.
Extending polarizations on families of K3 surfaces.
In The birational geometry of degenerations, 29:135–171, 1983.  
[12] Margaret Symington.
Four dimensions from two in symplectic topology.
In Proceedings of Symposia in Pure Mathematics, 71:153–208, 2003.

[13] Jonathan Wahl.
Elliptic deformations of minimally elliptic singularities.
Mathematische Annalen, 253(3):241–262, 1980.

Harvard University Cambridge, MA 02139 United States E-mail address: engel@math.harvard.edu