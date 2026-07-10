---
title: ADE surfaces and their moduli
authors:
- We Define A Class Of Surfaces Corresponding To The $A D E$ Root Lattices
- Construct Compactifications Of Their Moduli Spaces As Quotients Of Projective Varieties
  For Coxeter Fans
- Generalizing Losev-Manin Spaces Of Curves.
year: 2017
bibkey: alexeev17ade-surfaces
tags:
- paper
- extraction
abstract: |
  We define a class of surfaces corresponding to the $A D E$ root lattices and construct compactifications of their moduli spaces as quotients of projective varieties for Coxeter fans, generalizing Losev-Manin spaces of curves.
  We exhibit modular families over these moduli spaces, which extend to families of stable pairs over the compactifications.
  One simple application is a geometric compactification of the moduli of rational elliptic surfaces that is a finite quotient of a projective toric variety.
---

# ADE SURFACES AND THEIR MODULI

Abstract.
We define a class of surfaces corresponding to the $A D E$ root lattices and construct compactifications of their moduli spaces as quotients of projective varieties for Coxeter fans, generalizing Losev-Manin spaces of curves.
We exhibit modular families over these moduli spaces, which extend to families of stable pairs over the compactifications.
One simple application is a geometric compactification of the moduli of rational elliptic surfaces that is a finite quotient of a projective toric variety.

# Contents

1. Introduction 2

2. Log del Pezzo index 2 pairs and their double covers 5

Definitions of $A D E$ , $\widetilde A D E$ surfaces, pairs, and double covers 7

3A.
Toric pure shapes 8  
3B.
Nontoric $\widetilde { A }$ shapes  
3C.
Primed shapes  
3D.
Primed shapes which are toric  
3E.
Singularities of $A D E$ and $\widetilde A D E$ surfaces  
3F.
Recovering a precursor of pure shape 18  
4A.
The case $K _ { M } + L _ { M }$ is not nef 2020  
4B.
$K _ { M } + L _ { M }$ is nef and $g \geq 2$  
4C.
$K _ { M } + L _ { M }$ is nef and $g = 1$ 23

5. Moduli of $A D E$ pairs 24

5A.
Two-dimensional projections of $A D E$ lattices  
5B.
Moduli of $A D E$ pairs of pure shapes  
5C.
Moduli of $A D E$ pairs of toric primed shapes  
5D.
Moduli of $A D E$ pairs of all primed shapes  
$\mathrm { 5 E }$ .
Definitions of the naive $A D E$ families  
5F.
Action of the extra Weyl group $W _ { 0 }$ 28  
6. Compactifications of moduli of $A D E$ pairs  
6A.
Stable pairs in general and stable $A D E$ pairs  
6B.
Compactifications of the naive families for the $A$ shapes  
6C.
Compactifications of the naive families for the $A$ , $D$ , $^ - E$ shapes  
6D.
Compactifications of the naive families for all primed shapes  
6E.
A generalized Coxeter fan  
6F.
Description of the compactified moduli space of $A D E$ pairs

7. Canonical families and their compactifications 37

7A.
Two notions of the discriminant 3838  
7B.
Canonical families  
7C.
Compactifications of the canonical families 42  
7D.
Singularities of divisors in $A D E$ pairs 43  
8. Applications and connections with other works 4747  
8A.
Toric compact moduli of rational elliptic surfaces  
8B.
Moduli of Looijenga pairs after Gross-Hacking-Keel  
8C.
Involutions in the Cremona group 50

References List of Tables List of Figures

52

# 1. Introduction

There are two sources of motivation for this work: Losev-Manin spaces [LM00] and degenerations of K3 surfaces with a nonsymplectic involution [AET19].

Let $L _ { n + 3 }$ be the moduli space parameterizing weighted stable curves $( Z , Q _ { 0 } + Q _ { \infty } + \epsilon \textstyle \sum _ { i = 1 } ^ { n + 1 } P _ { i } )$ of genus $0$ with $n + 3$ points, where $0 < \epsilon \ll 1$ .
Equivalently, the singularity condition is that the $n + 1$ points $P _ { i }$ are allowed to collide while the remaining two may not collide with any others.
One has $\dim L _ { n + 3 } = n$ .
Quite remarkably, $L _ { n + 3 }$ is a projective toric variety for the Coxeter fan (also called the Weyl chamber fan) for the root lattice $A _ { n }$ , formed by the mirrors to the roots.
Of course it comes with an aspace of the pairs group for t $W ( A _ { n } ) = S _ { n + 1 }$ ing the points with unordere $P _ { i }$ .
The moduli points is then $( Z , Q _ { 0 } + Q _ { \infty } + \epsilon R )$ $\begin{array} { r } { R = \sum _ { i = 1 } ^ { n + 1 } P _ { i } } \end{array}$ $L _ { n + 3 } / S _ { n + 1 }$ .

There are other ways in which $L _ { n + 3 }$ corresponds to the root lattice $A _ { n }$ .
For example, its interior, over which the fibers are $Z \simeq \mathbb { P } ^ { 1 }$ , is the torus $\operatorname { H o m } ( A _ { n } , \mathbb { C } ^ { * } )$ , and the discriminant locus, where some of the points $P _ { i } , P _ { j }$ coincide, is a union of root hypertori $\cup _ { \alpha } \{ e ^ { \alpha } = 1 \}$ with $\alpha = e _ { i } - e _ { j }$ going over the roots of $A _ { n }$ .
Additionally, the worst singularity that the divisor $\textstyle \sum P _ { i }$ can have is $( x - 1 ) ^ { n + 1 } = 0$ , which is an $A _ { n }$ -singularity.

Losev and Manin asked in [LM00] if similar moduli spaces existed for other root lattices.
This was partially answered by Batyrev and Blume in [BB11] where they constructed compact moduli spaces for the $B _ { n }$ and $C _ { n }$ lattices as moduli of certain pointed rational curves with an involution.
Batyrev-Blume’s method works only for infinite series of root lattices, such as $A B C D$ , and it breaks down for $D _ { n }$ where it leads to non-flat families (most fibers have dimension 1 but some have 2).

In this paper, we generalize Losev-Manin spaces to the $D _ { n }$ and $E _ { n }$ lattices by replacing stable curve pairs $( Z , Q _ { 0 } + Q _ { \infty } + \epsilon R )$ by (KSBA) stable slc surface pairs $( X , D + \epsilon R )$ and constructing their compact moduli.

Namely, we define a class of surface pairs $( X , D + \epsilon R )$ naturally associated with the root lattices $A _ { n }$ , $D _ { n }$ , and $E _ { n }$ .
We call these pairs $A D E$ double covers, as all of them are double covers $\pi \colon X \to Y$ of surface pairs $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ .
Here, $C$ and $D$ are reduced boundaries (downstairs and upstairs), $R$ he ramification divisor, and pairs, and the underlying p $B$ isrs ranc the sor of surfa $\pi$ .
We call the pairss (with reduced bo $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ the $A D E$ $( Y , C )$ $A D E$ $C$

We prove that the moduli space $M$ of $A D E$ pairs (equivalently of $A D E$ double covers) of a fixed type is a torus for the associated $A D E$ lattice $\Lambda$ modulo a Weyl group $W$ , and that the normalization of the moduli compactification $\overline { { M } } ^ { \mathrm { s l c } }$ is the $W$ -quotient of a projective toric variety for a generalized Coxeter fan corresponding to $\Lambda$ .
Moreover, for each type we construct an explicit modular family of $A D E$ pairs over $M$ and show that, after a suitable coordinate change, the discriminant locus in $M$ , where $B$ is singular, is a union of root hypertori $\cup _ { \alpha } \{ e ^ { \alpha } = 1 \}$ with $\alpha$ going over the roots of $\Lambda$ .
Additionally, the worst singularity appearing in the double cover $X$ is the surface Du Val singularity of type $\Lambda$ .

For $\Lambda = A _ { n }$ we get the standard Coxeter fan and $\overline { { M } } ^ { \mathrm { s l c } } = L _ { n + 3 } / S _ { n + 1 }$ .
The ramification curve $R =$ $B$ in this case is hyperelliptic, a double cover $f \colon B \to Z$ of a rational genus 0 curve.
The boundary $C$ has two irreducible components defining the boundary $Q _ { 0 } + Q _ { \infty }$ of $Z$ , and the ramification points of $f$ provide the remaining $n + 1$ points in the data for a stable Losev-Manin curve $( Z , Q _ { 0 } + Q _ { \infty } +$ $\epsilon \textstyle \sum _ { i = 1 } ^ { n + 1 } P _ { i } )$ .

For $\Lambda = D _ { n }$ and $E _ { n }$ the fan is a generalized Coxeter fan, a coarsening of the standard Coxeter fan.
It is the normal fan of a permutahedron given by a classical Wythoff construction.

We found these $A D E$ surfaces and pairs by studying degenerations of K3 surfaces of degree 2. A polarized K3 surface $( X , L )$ of degree $L ^ { 2 } = 2$ comes with a canonical double cover $\pi \colon X \to Y$ .
The ramification divisor moduli of (KSBA) s $R$ of ble $\pi$ is intrinsic to lc pairs provid $( X , L )$ , and the pairnonical modu $( X , \epsilon R )$ is a stableactification air.
Thus, the of the moduli $\overline { { F } } _ { 2 } ^ { \mathrm { s l c } }$ space of K3 surfaces of degree 2.

On the other hand, there exists a nice toroidal compactification $\overline { { F } } _ { 2 } ^ { \mathrm { t o r } }$ defined by the Coxeter fan for the ection group of the root lattice associated to $F _ { 2 }$ .
The type III strata $\overline { { F } } _ { 2 } ^ { \mathrm { t o r } }$ are $W$ -quotients of projective toric varieties for the Coxeter fans of certain $A D E$ root lattices.
These strata look like the moduli spaces of degenerate stable slc pairs $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ whose 2 we confirmed this in many examples.
We determine the precise connection between irreducible components are some of the $A D E$ surface pairs discussed above.
Indeed, $\overline { { F } } _ { 2 } ^ { \mathrm { s l c } }$ and $\overline { { F } } _ { 2 } ^ { \mathrm { t o r } }$ in [AET19], which is a continuation of this paper.

We work over the field $\mathbb { C }$ of complex numbers.
Throughout, $\epsilon$ will denote a sufficiently small real number: $0 < \epsilon \ll 1$ .
This means that for fixed numerical invariants there exists an $\epsilon _ { 0 } > 0$ such that the stated conditions hold for any $0 < \epsilon \le \epsilon _ { 0 }$ .
Now let us explain the main results and the structure of the present paper in more detail.

In Section 2 we define $( K + D )$ -trivial polarized involution pairs $( X , D , \iota )$ and study their basic properties.
Roughly speaking, such pairs consist of a normal surface $X$ with an anticanonical divisor $D$ and an involution $\iota \colon X \to X$ that preserves $D$ .
They naturally appear when studying stable degenerations of K3 surfaces with a nonsymplectic involution.
We prove that the quotient $( Y , C ) \ : = \ : ( X , D ) / \iota$ of an involution pair is a log del Pezzo surface of index 2, i.e. the divisor $- 2 ( K _ { Y } + C )$ is Cartier and ample.

Denoting by $\pi \colon X \to Y$ the double cover, $B \in | - 2 ( K _ { Y } + C ) |$ the branch divisor and $R \subset X$ the ramification divisor, one has $K _ { X } + D + \epsilon R = \pi ^ { * } ( K _ { Y } + C + { \textstyle { \frac { 1 + \epsilon } { 2 } } } B )$ .
Then the pair $( X , D + \epsilon R )$ is a (KSBA) stable slc pair iff the pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ is such.

By analogy with Kulikov degenerations of K3 surfaces, we divide the pairs $( X , D , \iota )$ and their quotients $( Y , C )$ into types I, II, III.
For type I, one has $C = D = 0$ , the surface $X$ is an ordinary K3 surface with Du Val singularities, and the pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ is klt.
For types II and III, the pairs $( X , D + \epsilon R )$ and $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ are both not klt; these types are distinguished by the properties of the boundary $D$ , which is a disjoint union of smooth elliptic curves in type II and a cycle of rational curves in type III.

With this motivation, we set out to investigate log canonical non-klt del Pezzo surfaces with boundary $( Y , C )$ of index 2, and the moduli spaces of log canonical pairs $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ , with $B \in \vert - 2 ( K _ { Y } + C ) \vert$ .

In Section 3 we explicitly define many examples of such surfaces $( Y , C )$ in an ad hoc way.
Since the word type is already used for “types I, II, III”, we call the combinatorial classes of such surfaces shapes.
Those of type III we call $A D E$ shapes, and of type II we call $\widetilde A D E$ shapes.
We call the corresponding surfaces $( Y , C )$ $A D E$ resp.
$\widetilde A D E$ e e esurfaces, the stable pairs $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ ) $A D E$ resp.
pairs, and their covers $( X , D + \epsilon R )$ $A D E$ resp.
double covers.
To each shape we associate a decorated $A D E$ , resp.
$\widetilde A D E$ Dynkin diagram, which we use to label the shape, and a corresponding $A D E$ , resp.
$\widetilde A D E$ lattice.
The main reason for this association comes later, when considering the moduli spaces and their compactifications.

In the simplest cases, the surfaces $Y$ are toric and $C$ is a part of the toric boundary, with two components $C _ { 1 } , C _ { 2 }$ in type III and one component in type II.
These shapes are labeled by diagrams of types $A _ { n }$ , $D _ { n }$ , $E _ { n }$ , $\widetilde { D } _ { 2 n }$ , ${  { \widetilde { E } } } _ { 7 }$ and ${ \widetilde { E } } _ { 8 }$ .
At this point there is a clear motivation behind this labeling scheme, as the defining lattice polytopes of the toric surfaces $Y$ contain the corresponding Dynkin diagrams in an obvious way.
In type $\amalg$ we also introduce several nontoric shapes, which we call $\tilde { A } _ { 2 n - 1 }$ , ${ \tilde { A } } _ { 1 } ^ { * }$ , and $\widetilde { A } _ { 0 } ^ { - }$ .
Interestingly there is no ${ \widetilde { E } } _ { 6 }$ shape; Remark 3.10 discusses some reasons for that.

Next we define a procedure, which we call priming, for producing a new lc nonklt del Pezzo pair $( \overline { { Y } } ^ { \prime } , \overline { { C } } ^ { \prime } )$ of index 2 from an old such pair $( Y , C )$ .
The procedure consists of making weighted blowups $Y ^ { \prime }  Y$ at a collection of up to 4 points on the boundary $C$ , and then performing a contraction $Y ^ { \prime }  \overline { { Y } } ^ { \prime }$ defined by the divisor $- 2 ( K _ { Y ^ { \prime } } + C ^ { \prime } )$ (where $C ^ { \prime }$ is the strict transform of $C$ ), provided that it is big and nef.

We list all the $A D E$ and $\widetilde A D E$ shapes, together with their basic numerical invariants and singularities in Tables 2 and 3. In all, there are 43 $A D E$ shapes and 17 $\widetilde A D E$ shapes, some of which define infinite families.
Whilst this list seems rather large, most are obtained by applying the priming operation to a very short list of fundamental shapes.
We call these fundamental shapes pure shapes, and call the ones obtained from them by priming primed shapes.

In Section 4 we prove our first main result, which justifies our interest in the $A D E$ and $\widetilde A D E$ surfaces.

Theorem A.
The log canonical non-klt del Pezzo surfaces $( Y , C )$ with $2 ( K _ { X } + C )$ Cartier and $C$ reduced (or possibly empty) are exactly the same as the $A D E$ and $\widetilde A D E$ surfaces $( Y , C )$ , pure and primed.

Most of the proof can be extracted from the work of Nakayama [Nak07], with additional arguments necessary in genus 1. Nakayama’s classification of log del Pezzo pairs of index 2 was done in very different terms and the connection with root lattices did not appear in it.

In Section 5, for each shape we describe the moduli spaces of $A D E$ (i.e. type III) pairs and their double covers.
For each shape we have a root lattice $\Lambda$ of $A D E$ type.
It has an associated torus $T _ { \Lambda } : = \mathrm { H o m } ( \Lambda , \mathbb { C } ^ { * } )$ and Weyl group $W _ { \Lambda }$ .
Then our second main result is as follows.

Theorem B.
The moduli stack of $A D E$ pairs of a fixed $A D E$ shape is

$$
\begin{array} { r l r } & { \left[ \mathrm { H o m } ( \Lambda ^ { * } , \mathbb { C } ) : \mu _ { \Lambda } \times \mu _ { 2 } \right] = \left[ T _ { \Lambda } : W _ { \Lambda } \times \mu _ { 2 } \right] } & { f o r ~ p u r e ~ A ~ s h a p e s , } \\ & { \left[ \mathrm { H o m } ( \Lambda ^ { * } , \mathbb { C } ) : \mu _ { \Lambda } \right] = \left[ T _ { \Lambda } : W _ { \Lambda } \right] } & { f o r ~ p u r e ~ D ~ a n d ~ E ~ s h a p e s , } \\ & { \left[ \mathrm { H o m } ( \Lambda ^ { * } , \mathbb { C } ) : \mu _ { \Lambda ^ { \prime } } \times W _ { 0 } \right] = \left[ T _ { \Lambda ^ { \prime } } : W _ { \Lambda } \times W _ { 0 } \right] } & { f o r ~ p r i m e d ~ s h a p e s . } \end{array}
$$

Here, $\Lambda$ is an $A D E$ root lattice, $\Lambda ^ { * }$ is its dual weight lattice, $\Lambda ^ { \prime }$ is a lattice satisfying $\Lambda \subset \Lambda ^ { \prime } \subset \Lambda ^ { * }$ given explicitly in Theorem 5.12, $T _ { \Lambda ^ { \prime } } : = \mathrm { H o m } ( \Lambda ^ { \prime } , \mathbb { C } ^ { * } )$ , $\mu _ { \Lambda ^ { \prime } } : = \mathrm { H o m } ( \Lambda ^ { * } / \Lambda ^ { \prime } , \mathbb { C } ^ { * } )$ , and the additional Weyl group $W _ { 0 }$ is given in Theorem 3.32, with action described in Theorem 5.13.

This result is proved as Thms.
5.9 (for pure shapes) and 5.12 (for primed shapes).
To conclude Section 5, for each pure $A D E$ shape we construct a Weyl group invariant modular family of $A D E$ pairs, which we call the naive family, over the torus $T _ { \Lambda ^ { * } }$ .

In Section 6 for each $A D E$ (i.e. type III) shape we construct a modular compactification of the moduli space of $A D E$ pairs of this shape.
In 6A we begin with a general discussion of moduli compactifications using stable pairs, and we define stable $A D E$ pairs.
Next, for each $A D E$ shape we construct a Weyl group invariant family of stable slc pairs $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ over a projective toric variety $V _ { M } ^ { \mathrm { { c o x } } }$ for the Coxeter fan of an appropriate over-lattice $M \supset \Lambda ^ { * }$ of index $2 ^ { k }$ (Thms.
6.18, 6.26, 6.28). These theorems also describe the combinatorial types of the stable pairs over each point of $V _ { M } ^ { \mathrm { { c o x } } }$ .
For the $A D E$ surfaces where $C$ has two components, the irreducible components of these pairs are again $A D E$ pairs for Dynkin subdiagrams.
For some of the primed $A D E$ shapes where $C$ has one or zero components, new “folded” shapes appear.

Next, we define a generalized Coxeter fan as a coarsening of the Coxeter fan, corresponding to a decorated Dynkin diagram, and the corresponding projective toric variety $V _ { M } ^ { \mathrm { s e m } 1 }$ .
We prove that our family is constant on the fibers of $V _ { M } ^ { \mathrm { c o x } } \to V _ { M } ^ { \mathrm { s e m i } }$ and the types of degenerations are in a bijection with the strata of $V _ { M } ^ { \mathrm { s e m i } }$ , with the moduli of the same dimension.
As a consequence, we obtain our third main theorem.
This theorem follows from Thm.
6.38, which is a slightly stronger result.

Theorem C.
For each $A D E$ shape the moduli space $M _ { A D E } ^ { \mathrm { s l c } }$ is proper and the stable limit of $A D E$ pairs are stable $A D E$ pairs.

(1) For the pure $A D E$ shapes, the normalization of $M _ { A D E } ^ { \mathrm { s l c } }$ is $V _ { \Lambda } ^ { \mathrm { s e m } } / W _ { \Lambda }$ , a $W _ { \Lambda }$ -quotient of the projective toric variety for the generalize(2) For the primed shapes, the normalization $( M _ { A D E } ^ { \mathrm { s l c } } ) ^ { \nu }$ fais $V _ { \Lambda ^ { \prime } } ^ { \mathrm { s e m 1 } } / W _ { \Lambda } \rtimes W _ { 0 }$ , for a lattice extension $\Lambda ^ { \prime } \supset \Lambda$ .
The lattice $\Lambda ^ { \prime }$ and the Weyl group $W _ { 0 }$ are as in Theorem $B$ .

The moduli spaces described in Theorem B have many automorphisms, some of which extend to automorphisms of our compactification.
In Section 7 we prove that there exists an essentially unique deformation of the naive family such that its pullback to the torus $T _ { \Lambda ^ { * } }$ has the following wonderful property: the discriminant locus becomes the union of the root hypertori $\{ e ^ { \alpha } = 1 \}$ , with $\alpha$ going over the roots of the corresponding $A D E$ root lattice.
We also prove that this deformation extends to the compactification.
This is our fourth main theorem.

Theorem D.
For each $A D E$ shape there exists a unique deformation of the equation $f$ of the naive family such that $\operatorname { D i s c r } ( f ) = \operatorname { D i s c r } ( \Lambda )$ .
The resulting canonical family of $A D E$ pairs extends to $a$ family of stable pairs on the compactification for the generalized Coxeter fan.
The restriction of this compactified canonical family to a boundary stratum is the canonical family for a smaller Dynkin diagram.

This theorem is proved in two parts, as Theorems 7.2 and 7.11. In the final subsection 7D we use these canonical families to explicitly determine all the possible singularities of the branch divisor $B$ that can appear in our $A D E$ pairs.

In Section 8 we discuss an application of our results and its connections with other work.
In Section 8A, as an application we construct a compactification $M _ { \mathrm { e l l } }$ of the moduli space of rational elliptic surfaces with section and a distinguished $I _ { 1 }$ fiber (i.e. irreducible rational with one node).
The compactification is by the stable slc pairs $( X , D + \epsilon R )$ where $D$ is the $I _ { 1 }$ fiber and $R$ is the fixed locus of the elliptic involution.
We prove that the normalization of $\overline { { M } } _ { \mathrm { e l l } }$ is a $W _ { E _ { 8 } }$ -quotient of a projective toric variety for the generalized Coxeter fan for the $E _ { 8 }$ lattice.
In Section 8B we discuss the relationship of our work to that of Gross-Hacking-Keel on moduli of anticanonical pairs [GHK15], and in Section 8C we discuss its relationship with the classification of birational involutions in the Cremona group $\operatorname { B i r } ( \mathbb { P } ^ { 2 } )$ [BB00].

# 2. Log del Pezzo index 2 pairs and their double covers

Definition 2.1. A $( K + D )$ -trivial polarized involution pair $( X , D , \iota )$ consists of a normal surface $X$ with an effective reduced divisor $D$ , and an involution $\iota \colon X \to X$ , $\iota ( D ) = D$ such that

(1) $K _ { X } + D \sim 0$ is a Cartier divisor linearly equivalent to $0$ ,  
(2) the fixed locus of $\iota$ consists of an ample Cartier divisor $R$ , henceforth called the ramification divisor, possibly along with some isolated points, and  
(3) the pair $( X , D + \epsilon R )$ has log canonical (lc) singularities for $0 < \epsilon \ll 1$ .

Remark 2.2. Such pairs naturally appear when studying degenerations of K3 surfaces with an involution.
In [AET19] we show that for any one parameter degeneration of K3 surfaces ${ \cal S }  ( Z , 0 )$ with a nonsymplectic involution $\iota _ { S }$ and a ramification divisor $\mathcal { R } _ { \mathcal { S } }$ , if $( S _ { 0 } , \epsilon { \mathcal { R } } _ { 0 } )$ is the stable slc limit of the pairs $( S _ { t } , \epsilon \mathcal { R } _ { t } )$ for $0 < \epsilon \ll 1$ , then each irreducible component $X$ of the normalization of $( S _ { 0 } , \mathcal { R } _ { 0 } )$ comes with an involution $\iota$ and, denoting by $D$ its double locus, the pair $( X , D , \iota )$ is a $( K + D )$ -trivial polarized involution pair as in (2.1).

Let $\omega$ be a global generator of the 1-dimensional space $H ^ { 0 } { \big ( } { \mathcal { O } } _ { X } ( K _ { X } + D ) { \big ) }$ .
The ramification divisor $R$ is nonempty by ampleness and has no components in common with $D$ by the lc condition.
For a generic point $x \in R$ there are local parameters $( u , v )$ such that $\iota ( u , v ) \ : = \ : ( u , - v )$ .
Then $\iota ^ { * } ( d u \wedge d v ) = - d u \wedge d v$ .
Thus, the involution $\iota$ is non-symplectic, meaning $\iota ( \omega ) = - \omega$ .

Let $\pi \colon X \to Y = X / \iota$ be the quotient map, $C = \pi ( D )$ the boundary and $B = \pi ( R )$ the branch divisors.
By Hurwitz formula, $K _ { X } + D \equiv \pi ^ { * } ( K _ { Y } + C + { \textstyle { \frac { 1 } { 2 } } } B )$ .

Lemma 2.3. There is a one-to-one correspondence between $( K + D )$ -trivial polarized involution pairs $( X , D , \iota )$ and pairs $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ such that

(1) $Y$ is a normal surface and $C , B$ are reduced effective Weil divisors on it.
(2) $( Y , C )$ is a (possibly singular) del Pezzo surface with boundary of index $\leq 2$ , i.e. $- 2 ( K _ { Y } + C )$ is an ample Cartier divisor.
(3) $B \in | - 2 ( K _ { Y } + C ) |$ ; in particular $B$ is Cartier.
(4) The pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ has lc singularities for $0 < \epsilon \ll 1$ .
Moreover, if $( 1 )$ –(4) hold then one also has (5) For any singular point $y \in Y$ : if $y \in B$ then $y$ is Du Val and $y \not \in C$ .

Proof.
Suppose (1)–(4) hold and $y \in B$ is a non Du Val singularity of $Y$ or a Du Val singularity with $y \in C$ .
Then on a minimal resolution $g \colon \widetilde { Y }  Y$ there exists an exceptional divisor $E$ whose discrepancy with respect to $K _ { Y } + C$ is $< 0$ .
Since $2 ( K _ { Y } + C )$ is Cartier, one has $a _ { E } ( K _ { Y } + C ) \leq - \frac { 1 } { 2 }$ .
But $B$ is Cartier, so

$$
a _ { E } \left( K _ { Y } + C + \frac { 1 + \epsilon } { 2 } B \right) \le - \frac { 1 } { 2 } - \frac { 1 + \epsilon } { 2 } < - 1 ,
$$

and the pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ is not $\mathrm { l c }$ , a contradiction.
This proves (5).

Now let $( X , D , \iota )$ be a $( K + D )$ -trivial polarized involution pair.
Using $\iota ^ { * } ( \omega ) = - \omega$ , it follows by [Kol13, Prop.2.50(4)] that for any $x \in X$ ´etale-locally $( X , x ) \to ( Y , \pi ( x ) )$ is the index-1 cover for the pair $( Y , C + { \textstyle { \frac { 1 } { 2 } } } B )$ .
Thus, $\pi _ { * } { \mathcal { O } } _ { X } = { \mathcal { O } } _ { Y } \oplus \omega _ { Y } ( C )$ , the divisor $2 ( K _ { X } + C )$ is Cartier, and $B = ( s )$ , $s \in H ^ { 0 } ( \mathcal { O } _ { Y } ( - 2 ( K _ { Y } + C ) ) )$ .
From the identity $K _ { X } + D + \epsilon R \equiv \pi ^ { * } ( K _ { Y } + C + { \textstyle { \frac { 1 + \epsilon } { 2 } } } B )$ it follows that the divisor $K _ { Y } + C + \frac { 1 + \epsilon } { 2 } B$ is ample and the pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ has lc singularities.

Vice versa, let $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ be a pair as above, and let $X : = \operatorname { S p e c } _ { Y } \mathcal { O } _ { Y } \oplus \omega _ { Y } ( C )$ be the double cover corresponding to a section $s \in H ^ { 0 } ( \mathcal { O } _ { Y } ( - 2 ( K _ { Y } + C ) ) )$ , $B = ( s )$ .
Thus, ´etale-locally it is the index-1 cover for the pair $( Y , C + { \textstyle { \frac { 1 } { 2 } } } B )$ .
Then $K _ { X } + D \sim 0$ , $K _ { X } + D + \epsilon R$ is ample and lc, and $2 R = \pi ^ { * } ( B )$ is an ample Cartier divisor.

We claim that $R$ itself is Cartier.
Pick a point $x \in R$ and let $y = \pi ( x ) \in B$ .
The cover $\pi$ corresponds to the divisorial sheaf $\mathcal { O } _ { Y } ( K _ { Y } + C )$ , which is locally free at $y$ by (5).
Then the double cover is given by a local equation $u ^ { 2 } = s$ , and $R$ is given by one local equation $u = 0$ , so it is Cartier.


Thus, the classification of $( K + D )$ -trivial polarized involution pairs is reduced to that of del Pezzo surfaces $( Y , C )$ with reduced boundary of index $\leq 2$ plus a divisor $B \in | - 2 ( K _ { Y } + C ) |$ satisfying the lc singularity condition.
In the case when $C = 0$ , del Pezzo surfaces of index $\leq 2$ with log terminal singularities were classified by Alexeev-Nikulin in [AN88, AN89, AN06].
There are 50 main cases which are further subdivided into 73 cases according to the singularities of $Y$ .
However, all these surfaces are smoothable, which follows either by using the theory of K3 surfaces or by [HP10, Prop. 3.1].
Thus, there are only 10 overall families, with a generic element a smooth del Pezzo surface of degree $1 \le K _ { Y } ^ { 2 } \le 9$ (for $K _ { Y } ^ { 2 } = 8$ there are two families, for $\mathbb { F } _ { 0 }$ and $\mathbb { F } _ { 1 }$ ).
The dimension of the family of pairs $( Y , B )$ , equivalently of the double covers $( X , \iota )$ , is $1 0 + K _ { Y } ^ { 2 }$ .

Del Pezzo surfaces with a half-integral boundary $C$ of index $\leq 2$ were classified by Nakayama in [Nak07].
An important result of Nakayama is the Smooth Divisor Theorem [Nak07, Cor.3.20] generalizing that of [AN06, Thm.1.4.1].
It says that for any del Pezzo surface $( Y , C )$ with boundary of index $\leq 2$ a general divisor $B \in | - 2 ( K _ { Y } + C ) |$ is smooth and in particular does not pass through the singularities of $Y$ .
Thus, every such surface $( Y , C )$ produces a family of $( K + D )$ -trivial polarized involution pairs $( X , D , \iota )$ .

Remark 2.4. The divisors $C$ and $B$ play a very different role: $C$ is fixed, and $B$ varies in a linear system.
For this reason, we will refer to them differently.
We will call $C$ the boundary and say that $( Y , C )$ is a surface with boundary (and sometimes we will drop the words “with boundary”).
We will call $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ a pair, consisting of a surface with boundary $( Y , C )$ plus an additional choice of divisor $B$ on it.
In many cases, surfaces with boundary are rigid, but pairs have moduli.

Let $f \colon { \tilde { X } }  X$ be the minimal resolution of singularities, and let $\widetilde { D }$ be the effective $\mathbb { Z }$ -divisor on $\widetilde { X }$ defined by the formula $K _ { \widetilde { X } } + \widetilde { D } = f ^ { \ast } ( K _ { X } + D ) \sim 0$ .
It follows from the lc condition that $\widetilde { D }$ is reduced.

Lemma 2.5. For the minimal resolution of $a$ $( K + D )$ -trivial polarized involution pair, one of the following holds:

(I) $D = 0$ , $\widetilde { D } = 0$ , and $X$ is canonical.
Then $X$ is a $K \mathcal { 3 }$ surface with $A D E$ singularities and $\iota$ is an non-symplectic involution.  
(II) $( X , D )$ is strictly log canonical and $\widetilde { D }$ is one or two isomorphic smooth elliptic curve(s),  
(III) $( X , D )$ is strictly log canonical and $\widetilde { D }$ is a cycle of $\mathbb { P } ^ { 1 } s$ .

Accordingly, we will say that the $( K + D )$ -trivial polarized involution pair $( X , D , \iota )$ and the corresponding del Pezzo surface $( Y , C )$ with boundary have type I, II, or III.
In type I $( Y , C )$ is klt, and in types II, III it is not klt.

Proof.
(I) (Compare [AN06, Sec. 2.1]) $\widetilde { X }$ is either a K3 surface or an Abelian surface.
If ${ \overset { \underset { \ r { X } } { \sim } } { X } } = X$ is an Abelian surface then the involution is different from $( - 1 )$ since $R \neq 0$ .
Thus, the induced involution $\iota ^ { * }$ on $H ^ { 0 } ( \Omega _ { X } ^ { \scriptscriptstyle 1 } )$ is different from $( - 1 )$ and there exists a nontrivial 1-differential on $X$ which descends to a minimal resolution $\widetilde { Y }$ of $Y$ .
But $Y$ is a del Pezzo surface with log terminal singularities, so basic vanishing gives $h ^ { 0 } ( \Omega _ { \widetilde { Y } } ^ { 1 } ) = h ^ { 1 } ( \mathcal { O } _ { \widetilde { Y } } ) = h ^ { 1 } ( \mathcal { O } _ { Y } ) = 0$ .
Thus, $\widetilde { X }$ is a K3 surface, and we already noted ethat the involution is non-symplectic.

$( \mathrm { I I } , \mathrm { I I I } )$ Since $\omega _ { \widetilde { D } } \simeq \mathcal { O } _ { \widetilde { D } }$ by adjunction, every connected component of $\widetilde { D }$ is either a smooth elliptic curve or a cycle of $\mathbb { P } ^ { 1 } \mathrm { s }$ .
Since $K _ { \widetilde { X } } = - \widetilde { D }$ is not effective, $\widetilde { X }$ is birationally ruled over a curve $E$ and $\widetilde { D }$ is a bisection.
The curve $E$ has genus $1$ or $0$ since it is dominated by $\widetilde { D }$ .
If one of the connected components of $\widetilde { D }$ is a cycle of $\mathbb { P } ^ { 1 } \mathrm { s }$ then $g ( E ) = 0$ and $X$ is rational.
In that case from $H ^ { 1 } ( - \tilde { D } ) = H ^ { 1 } ( K _ { \tilde { X } } ) = 0$ we get $h ^ { \scriptscriptstyle 0 } ( \mathcal { O } _ { \widetilde { D } } ) = h ^ { \scriptscriptstyle 0 } ( \mathcal { O } _ { \widetilde { X } } ) = 1$ , so $\bar { D }$ is connected.
If $g ( E ) = 1$ and $\widetilde { D }$ has e e emore than one connected component then then they all must be horizontal.
Thus, there must be two of them, each a section of $\widetilde X  E$ , so they are both isomorphic to $E$ .


3. Definitions of $A D E$ , $\widetilde A D E$ surfaces, pairs, and double covers

Definition 3.1. The $A D E$ and $\widetilde A D E$ surfaces are certain normal surfaces $( Y , C )$ with reduced boundary defined by the explicit constructions of this section.
They are examples of log del Pezzo surfaces of index 2, i.e. each pair $( Y , C )$ has log canonical singularities, and the divisor $- 2 ( K _ { Y } + C )$ is Cartier and ample.

In the sense of Lemma 2.5, the $A D E$ surfaces are of type III, and $\widetilde A D E$ surfaces are of type II.

Definition 3.2. Given an $A D E$ , resp.
$\widetilde A D E$ surface $( Y , C )$ , let $L = - 2 ( K _ { Y } + C )$ be its polarization, an ample line bundle.
If $B \in | L |$ is an effective divisor such that $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ is log canonical for $0 < \epsilon \ll 1$ then $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ is called an $A D E$ , resp.
$\widetilde A D E$ pair.
The double cover $\pi \colon X \to Y$ as in Lemma 2.3 is then called an $A D E$ , resp.
$\widetilde A D E$ double cover.

Remark 3.3. By (2.3)(5) the points of intersection $B \cap C$ are nonsingular points of $Y$ , and the log canonicity of $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ implies that $B$ intersects $C$ transversally.
Consequently, $R$ intersects $D$ transversally at smooth points of $X$ .

By construction, the $A D E$ and $\widetilde A D E$ surfaces will admit a combinatorial classification.
Since the word type is overused, we call the classes shapes.
To each shape we associate:

(1) a decorated $A D E$ or affine, extended $\widetilde A D E$ Dynkin diagram, (2) a decorated Dynkin symbol, e.g $\overline { { A } } _ { 5 } ^ { - }$ or ${ \widetilde { E } } _ { 8 } ^ { - }$ , (3) an ordinary $A D E$ , resp.
affine $\widetilde { A } \widetilde { D } \widetilde { E }$ root lattice, e.g. $A _ { 5 }$ or ${ \widetilde { E } } _ { 8 }$

Parts (1) and (2) are equivalent, and (3) may be obtained from them by deleting the decorations.
The main reason for this association will become apparent later, in the description of the moduli spaces and their compactifications.
But in the cases where $Y$ is toric and $C$ is part of its toric boundary, they also encode some data about the defining polytope.

We divide the shapes into two classes, which we call pure and primed.
$A D E$ and $\widetilde A D E$ surfaces of pure shape are fundamental, we define them all explicitly in subsections 3A and 3B.
In type III the pure shapes form 5 infinite families along with 3 exceptional shapes.
In type II there are 2 infinite families and 4 exceptional shapes.

The $A D E$ and $\widetilde { A } \widetilde { D } \widetilde { E }$ surfaces of primed shape are secondary and there are many more of them; they can all be obtained from surfaces of pure shape by an operation which we call “priming”, explained in subsection 3C.

3A.
Toric pure shapes.
The $A D E$ surfaces (type III) of pure shape are all toric, as are 3 of the $\widetilde A D E$ surfaces (type II) of pure shape.
To construct them we begin with polarized toric surfaces $( Y , L )$ , where $L = - 2 ( K _ { Y } + C )$ .
Such toric surfaces correspond in a standard way with lattice polytopes $P$ with vertices in $M \simeq \mathbb { Z } ^ { 2 }$ .

Lemma 3.4. Let $P$ be an integral polytope with a distinguished vertex $p _ { * }$ and $( Y , L )$ be the corresponding polarized projective toric variety.
Let $C$ be the torus-invariant divisor corresponding to the sides passing through $p _ { * }$ .
Suppose that all the other sides of $P$ are at lattice distance $\boldsymbol { \mathcal { Z } }$ from $p _ { * }$ .
Then $- 2 ( K _ { Y } + C ) \sim L$ is ample and Cartier, and the pair $( Y , C )$ has log canonical singularities.

Proof.
Let $C ^ { \prime } = \textstyle \sum C _ { i } ^ { \prime }$ be the divisor corresponding to the sides not passing through the vertex $p _ { * }$ .
The zero divisor of the section $e ^ { p _ { * } } \in H ^ { \cup } ( Y , L )$ is $\sum d _ { i } C _ { i } ^ { \prime }$ where $d _ { i }$ are the lattice distances from $p _ { * }$ to the corresponding sides.
This gives $L \sim 2 C ^ { \prime }$ .
Combining it with the identity $K _ { Y } + C + C ^ { \prime } \sim 0$ gives the first statement.
It is well known that the pair $( Y , C + C ^ { \prime } )$ has log canonical singularities.
Thus, the smaller pair $( Y , C )$ also has log canonical singularities.


Definition 3.5. We now apply this Lemma to define some of our $A D E$ and $\widetilde A D E$ surfaces $( Y , C )$ of pure shape.
For each shape we list its decorated Dynkin symbol and the vertices of its defining polytope in Table 1, and illustrate them with pictures in Figures 1, 2, 3, 4. In these Figures the sides of the polytope through $p _ { * }$ are drawn in bold blue; they correspond to irreducible components of the divisor $C$ .
Within the polytopes we draw the decorated Dynkin diagrams, the rules for doing this are explained in Notation 3.7. Finally, we also label some of the lattice points $p _ { i }$ , for later use in Section 5.

The surface $Y$ of shape $\widetilde { D } _ { 2 n }$ is toric with a torus-invariant boundary $C$ only for $2 n \geq 6$ .
In the ${ \widetilde { D } } _ { 4 }$ shape we formally define $( Y , C )$ to be either $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ with a smooth diagonal $C \sim s + f$ or, as a degenerate subcase, a quadratic cone $\mathbb { P } ( 1 , 1 , 2 )$ with a conic section.

Definition 3.6. Given a surface $( Y , C )$ of pure shape, we call the irreducible components of $C$ sides.
If $( Y , C )$ is of type III there are two sides, we call them left and right and decompose $C = C _ { 1 } + C _ { 2 }$ correspondingly.
If $( Y , C )$ is of type II there may be one side or no sides.

Let $L = - 2 ( K _ { Y } + C )$ .
We call a side $C ^ { \prime }$ long if $L . C ^ { \prime } = 2$ or 4, and short if $L . C ^ { \prime } = 1$ or 3.

Table 1. Polytopes for the pure shapes  
![](images/cc2271ae4808db00b4ef6b22a900c4f4684ea3cbf928ba02eb747fff93e324a4.jpg)

![](images/b559889b5dfee1c75a50081dd8fb32b181ed5ea13c4423d2b5b5126db6023d87.jpg)  
Figure 1. A shapes: $A _ { 3 }$ , $\overline { { A _ { 3 } } } ^ { - }$ , $A _ { 2 } ^ { - }$ , $A _ { 0 } ^ { - }$

![](images/44cfcb674c7b4f26777df3531ac1b4da23070d9d1824c090a607c00a91695553.jpg)  
Figure 2. $D$ shapes: $D _ { 4 }$ , ${ D } _ { 5 } ^ { - }$ , $D _ { 6 }$

![](images/8170d81b8efbaeeaa15238c851de8ca2e094e44a4d7035e90d9cd3bb3f5ff5c6.jpg)  
Figure 3. $E$ shapes: $^ - E _ { 6 } ^ { - }$ , ${ } ^ { - } E _ { 7 }$ , $^ - E _ { 8 } ^ { - }$

In the type III cases illustrated in Figures 1, 2, 3, long sides have lattice length 2 and short sides have lattice length 1. In the type II cases illustrated in Figure 4, long sides have lattice length 4 and short sides have lattice length 3.

![](images/331e2940fda7cc719b4e095e7523bf2406c3c8627c3b360df47fe574e0433c39.jpg)  
Figure 4. Type II shapes ${ \widetilde { D } } _ { 8 }$ , ${  { \widetilde { E } } } _ { 7 }$ and ${ \widetilde { E } } _ { 8 } ^ { - }$

Within each polytope in Figures 1, 2, 3, 4 we draw the corresponding decorated Dynkin diagram, using the following rule.

Notation 3.7. Given a surface of pure shape $( Y , C )$ defined torically by a polytope $P$ as above, mark a node for each lattice point on the boundary of of $P$ which is not contained in $C$ , and join them with edges along the boundary.
For any node that lies at a corner of $P$ , add an additional internal node to the diagram and connect it to the corner node.
We distinguish such internal nodes by circling them in our diagrams.

This process associates an $A D E$ (resp.
$\widetilde A D E$ ) diagram to each of our torically-defined pure shapes of type III (resp.
type II), but it does not give a bijective correspondence between diagrams and shapes.
To fix this we also need to keep track of the parity.
We color the nodes of a diagram lying at lattice length 2 from $p _ { * }$ black, and the nodes lying at lattice length 1 from $p _ { * }$ white.
Internal nodes are always colored white.

In the type III cases, note that each diagram has a leftmost and rightmost node, which sit next to the left and right sides respectively.
The length of the sides may be read off from the colors of these nodes: white nodes correspond to long sides and black nodes to short sides.

Notation 3.8. For ease of reference, to each decorated Dynkin diagram we also associate a decorated Dynkin symbol, in a unique way.
For the pure shapes, this is given by the name of the (undecorated) Dynkin diagram, with superscript minus signs on the left/right to denote the locations of short sides; as noted above, this can be read off from the colors of the nodes at the ends of the diagram.
For instance, as illustrated in Figure 1, $A _ { 3 }$ has two long sides, $\overline { { A } } _ { 3 } ^ { - }$ has two short sides, and $A _ { 2 } ^ { - }$ has a long side on the left and a short side on the right.
In type II cases, which have only one side, we place all decorations on the right by convention.

Remark 3.9. With this notation, the two shapes ${ \overline { { A } } } _ { 2 n - 2 }$ and $A _ { 2 n - 2 } ^ { - }$ are identical up to labeling of the components of $C$ .
Where this labeling is unimportant, we will refer to these surfaces by the symbol $A _ { 2 n - 2 } ^ { - }$ , with the short side on the right.
There are, however, some settings in which it will be important to keep track of the labels, such as when we come to study degenerations.

Remark 3.10. Curiously, there is no ${ \widetilde { E } } _ { 6 }$ shape.
In our ad hoc definition above, the process of adding internal nodes can only produce branches of length 2. This rules out Dynkin diagram ${ \widetilde { E } } _ { 6 }$ , which has three branches of length 3. A deeper reason is that in Arnold’s classification of singularities [Arn72] the ${  { \widetilde { E } } } _ { 7 }$ and ${ \widetilde { E } } _ { 8 }$ singularities exist in all dimensions $\geq 2$ , but ${ \widetilde { E } } _ { 6 }$ starts in dimension 3 and so cannot appear on a surface.

3B.
Nontoric $\widetilde { A }$ shapes.
In addition to the toric surfaces described above, there are also three nontoric $\widetilde A D E$ surfaces (type II) of pure shape.
These are the $\widetilde { A }$ shapes, their decorated Dynkin diagrams and symbols are chosen to be compatible with moduli and degenerations, although they do not admit the same nice description in terms of polytopes as the toric shapes.
They are illustrated in Figure 5.

(1) $\tilde { A } _ { 2 n - 1 }$ .
The surface $Y$ is a cone over an elliptic curve and $C = 0$ , so there is no boundary.
More precisely, let $\mathcal { F }$ be a line bundle of degree $n > 0$ on an elliptic curve $E$ , and let $\widetilde { Y }$ be the surface $\operatorname { P r o j } _ { E } ( { \mathcal { O } } \oplus { \mathcal { F } } )$ .
Let $s , s _ { \infty }$ be the zero, resp.
infinity sections, and let $f \colon { \widetilde { Y } }  Y$ be the contraction of the zero section.
Then $f ^ { * } K _ { Y } = K _ { \widetilde { Y } } + s = - s _ { \infty }$ , so $- K _ { Y }$ is ample with $K _ { Y } ^ { 2 } = n$ .
If $B \in | - 2 K _ { Y } |$ is a generic section then $p _ { a } ( B ) = n + 1$ and the map $B  E$ has $2 n$ points of ramification.
Of course, the surface $Y$ is not toric.
The double cover $X  Y$ branched in $B$ is unramified at the singular point, and $X$ has two elliptic singularities.
One has $R ^ { 2 } = 2 K _ { Y } ^ { 2 } = 2 n$ .

(2) $\stackrel { \sim } { A } _ { 1 } ^ { * }$ .
The surface is the projective plane $Y = \mathbb { P } ^ { 2 }$ , the boundary $C$ is a smooth conic, and the branch curve $B$ is a possibly singular conic.
If $B$ is smooth then the double cover $X = \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ ; if $B$ is two lines then $X = \mathbb { F } _ { 2 } ^ { \cup } = \mathbb { P } ( 1 , 1 , 2 )$ with $R$ passing through the singular point of $X$ .
We also include here as a degenerate subcase when $\mathbb { P } ^ { 2 }$ degenerates to $Y = \mathbb { F } _ { 4 } ^ { 0 }$ .
Then $X = \mathbb { F } _ { 2 } ^ { 0 }$ with $R$ not passing through the singular point.

(3) $\widetilde { A } _ { 0 } ^ { - }$ .
The surface is the quadratic cone $Y = \mathbb { P } ( 1 , 1 , 2 )$ with minimal resolution $\overset { \sim } { Y } = \mathbb { F } _ { 2 }$ .
The strict preimage of $C$ on $\widetilde { Y }$ is a divisor in the linear system $\vert s + 3 f \vert$ , where $s$ is the $\left( - 2 \right)$ -section and $f$ is a fiber.
The curve $C$ passes through the vertex of the cone and is smooth at that point.
The branch curve $B$ is a hyperplane section disjoint from the vertex. The double cover is $X = \mathbb { P } ^ { 2 }$ with an involution $( x , y , z ) \mapsto ( x , - y , z )$ , and the boundary divisor is a smooth elliptic curve $y ^ { 2 } z = f _ { 3 } ( x , z )$ .

![](images/f310928853bbd24ee2c32e2fed88d488b443a8676c215fa58fe96f81470965b5.jpg)  
Figure 5. Nontoric type II $\widetilde { A }$ shapes: ${ \widetilde { A } } _ { 5 }$ , $\dot { A } _ { 1 }$ , ${ \tilde { A } } _ { 1 } ^ { * }$ , $\widetilde { A } _ { 0 } ^ { - }$

The surface $Y$ of shape ${ \tilde { A } } _ { 1 } ^ { * }$ is obtained by a “corner smoothing” of a surface of toric shape $A _ { 1 }$ : the union of two lines $C _ { 1 } + C _ { 2 }$ in $\mathbb { P } ^ { 2 }$ is smoothed to a conic $C$ .
Similarly, $\widetilde { A } _ { 0 } ^ { - }$ is obtained by a “corner smoothing” of $A _ { 0 } ^ { - }$ .
We add the star in $\tilde { A } _ { 1 } ^ { * }$ to distinguish it from the ordinary $\stackrel { \sim } { A } _ { 1 }$ shape, which has no boundary.

Remark 3.11. One observes that the $\widetilde { A }$ shapes cannot be toric because the Dynkin diagram is not a tree.

Remark 3.12. With the single exception of ${ \tilde { A } } _ { 1 } ^ { * }$ , all of our decorated Dynkin graphs are bipartite: black and white nodes appear in alternating order.

3C.
Primed shapes.
Priming is a natural operation producing a new del Pezzo surface $( \overline { { Y } } ^ { \prime } , \overline { { C } } ^ { \prime } )$ of index 2 from an old one $( Y , C )$ .
Let $I _ { i } \simeq ( y , x ^ { 2 } )$ be an ideal with support at a smooth point $P _ { i } \in C$ whose direction is transversal to $C$ .
A weighted blowup at $I _ { i }$ is a composition of two ordinary blowups: at $P _ { i }$ and at the point $P _ { i } ^ { \prime }$ corresponding to the direction of $I _ { i }$ , followed by a contraction of an $\left( - 2 \right)$ -curve, making an $A _ { 1 }$ surface singularity at a point contained in the strict preimage $C ^ { \prime }$ of $C$ .
Weighted blowups of this form are the basis of the priming operation.

Definition 3.13. Let $( Y , C )$ be an $A D E$ or $\widetilde A D E$ surface and let $P _ { 1 } , \dots , P _ { k } \ \in \ C$ be distinct nonsingular points of $Y$ and $C$ .
Choose ideals $I _ { i } \simeq ( y , x ^ { 2 } )$ with supports at $P _ { i }$ and directions transversal to $C$ (the closed subschemes Spec ${ \mathcal { O } } _ { Y } / I _ { i }$ can be thought of as vectors).
Let $k _ { s }$ denote the number of points on side $C _ { s }$ , so $k = \sum k _ { s }$ .
Define $f \colon Y ^ { \prime } \to Y$ to be the weighted blowup at $\begin{array} { r } { I = \prod _ { i = 1 } ^ { k } I _ { i } } \end{array}$ and let $C ^ { \prime }$ be the strict preimage of $C$ .
Let $F = \textstyle \sum F _ { i }$ be the sum of the exceptional divisors and $L ^ { \prime } = - 2 ( K _ { Y ^ { \prime } } + C ^ { \prime } )$ ; note that $L ^ { \prime }$ is a line bundle since an $A _ { 1 }$ singularity has index 2.

Assume that $L ^ { \prime }$ is big, nef, and semiample.
Then the priming of $( Y , C )$ is defined to be the pair $( \overline { { Y } } ^ { \prime } , \overline { { C } } ^ { \prime } )$ obtained by composing $f$ with the contraction $g \colon Y ^ { \prime } \to { \overline { { Y } } } ^ { \prime }$ given by $| N L ^ { \prime } |$ , $N \gg 0$ .
The divisor $\overline { { C } } ^ { \prime }$ is defined to be the strict transform of $C$ .
The resulting pair $( \overline { { Y } } ^ { \prime } , \overline { { C } } ^ { \prime } )$ is an $A D E$ or $\widetilde A D E$ surface of primed shape.

k 3.14. Priming hasbe a curve such that geometric meaning for the pairs is log canonical.
By (3.3) the cu $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ .
Letversal $B \in | L |$ $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ $B$ to $C$ .
In this case we take the ideals $I _ { i }$ to be supported at some of the points $P _ { i } \in B \cap C$ , with the directions equal to the tangent directions of $B$ at $P _ { i }$ .
Priming then produces a new pair $( \overline { { { Y } } } ^ { \prime } , \overline { { { C } } } ^ { \prime } + { \textstyle \frac { 1 + \epsilon } { 2 } } \overline { { { B } } } ^ { \prime } )$ which disconnects $B$ from $C$ at the points $P _ { i }$ .
If a component of $C ^ { \prime }$ is completely disconnected from $B ^ { \prime }$ then it is contracted on ${ \overline { { Y } } } ^ { \prime }$ .

But it is on the double cover $\pi \colon ( X , D + \epsilon R ) \to ( Y , C + { \frac { 1 + \epsilon } { 2 } } B )$ where the priming operation becomes the most natural and easiest to understand.
The double cover $X ^ { \prime }$ of $Y ^ { \prime }$ branched in $B ^ { \prime }$ is an ordinary smooth blowup of $X$ at the points $Q _ { i } = \pi ^ { - 1 } ( P _ { i } )$ .
So on the cover we simply make $k$ ordinary blowups at some points $Q _ { i } \in D \cap R$ in the boundary $D$ which are fixed by the involution, then apply the linear system $| N R ^ { \prime } |$ , $N \gg 0$ , provided that $R ^ { \prime }$ is big, nef and semiample, to obtain the primed pair $( \overline { { \boldsymbol X } } ^ { \prime } , \overline { { \boldsymbol D } } ^ { \prime } + \epsilon \overline { { \boldsymbol R } } ^ { \prime } )$ .
This disconnects $R$ from $D$ at the points $Q _ { i }$ .
If a component of $D ^ { \prime }$ is completely disconnected from $R ^ { \prime }$ then it is contracted on ${ \overline { { X } } } ^ { \prime }$ .

Definition 3.15. In terms of the pairs, we will call the above operation priming of an $A D E ( r e s p$ .
$\widetilde A D E$ ) pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ , resp.
priming of an $A D E ( r e s p . \ \widetilde { A } \widetilde { D } \widetilde { E } _ { \mathbf { \Gamma } }$ double cover $( X , D + \epsilon R )$ .
The result is an $A D E ( \mathrm { r e s p . } \ \tilde { A } \tilde { D } \tilde { E } )$ pair/double cover of primed shape.

We reiterate that a priming only exists if $L ^ { \prime }$ is big, nef, and semiample.
Below we will give a necessary and sufficient condition for existence of a priming that is easier to check; before that, however, we need to introduce some basic invariants.

Definition 3.16. The basic numerical invariants of an $A D E$ or $\widetilde A D E$ surface $( Y , C )$ , with polarization $L = - 2 ( K _ { Y } + C )$ , are

(1) the volume $v = L ^ { 2 } / 2 > 0$ , (2) the genus $g = { \textstyle { \frac { 1 } { 2 } } } ( K _ { Y } + L ) L - 1 \ge 0$ , (3) the lengths $L C _ { s } > 0$ of the sides.

The Hilbert polynomial of $( Y , L )$ is $\chi ( Y , x L ) = v x ^ { 2 } + ( v + 1 - g ) x + 1$ .
The Hilbert polynomials of $( C _ { s } , L )$ are $2 x + 1$ for a long side and $x + 1$ for a short side.
It is immediate to compute these invariants for the pure shapes.
We list them in the highlighted rows of Tables 2 and 3.

Lemma 3.17. With notation as in Definition 3.13:

(1) For the main divisors, one has $C ^ { \prime } = f ^ { * } C - F , \quad K _ { Y ^ { \prime } } = f ^ { * } K _ { Y } + 2 F , \quad L ^ { \prime } = f ^ { * } L - 2 F , \quad K _ { Y ^ { \prime } } + L ^ { \prime } = f ^ { * } ( K _ { Y } + L ) .$

(2) The basic invariants change as follows:

$$
L ^ { \prime 2 } / 2 = L ^ { 2 } / 2 - k , \quad g ( L ^ { \prime } ) = g ( L ) , \quad L ^ { \prime } C _ { s } ^ { \prime } = L C _ { s } - k _ { s } .
$$

Theorem 3.18 (Allowed primings).
Let $( Y , C )$ be an $A D E$ or $\widetilde A D E$ surface of pure shape, as defined in sections 3A and $\mathcal { B }$ , and $I _ { 1 } , \ldots , I _ { k }$ a collection of ideals as in Definition 3.13. Then $a$ necessary and sufficient condition for a priming to exist is: $L ^ { \prime 2 } > 0$ and $L ^ { \prime } C _ { s } ^ { \prime } \ge 0$ for the sides $C _ { s }$ .
Under these conditions, $L ^ { \prime }$ is big, nef, and semiample, and contracts $Y ^ { \prime }$ to a normal surface ${ \overline { { Y } } } ^ { \prime }$ with ample Cartier divisor $- 2 ( K _ { \overline { { Y } } ^ { \prime } } + \overline { { C } } ^ { \prime } )$ .

Proof.
The conditions $L ^ { \prime 2 } > 0$ and $L ^ { \prime } C _ { s } ^ { \prime } \ge 0$ are necessary since $L ^ { \prime }$ is big and nef.
Now assume that they are satisfied.
We exclude $\tilde { A } _ { 2 n - 1 }$ since its boundary is empty and no primings are possible.
We can also exclude the shapes of volume 1, which are $A _ { 0 } ^ { - }$ and $\widetilde { A } _ { 0 } ^ { - }$ .
By (3.17) one has

$$
{ \frac { 1 } { 2 } } L ^ { \prime } = ( K _ { Y ^ { \prime } } + L ^ { \prime } ) + C ^ { \prime } = f ^ { * } ( K _ { Y } + L ) + C ^ { \prime } .
$$

Thus, if $K _ { Y } + L$ is nef then $L ^ { \prime }$ is nef.
One checks that for all the pure shapes except for $A _ { 1 }$ and ${ \widetilde { A } } _ { 1 } ^ { * }$ the divisor $K _ { Y } + L$ is nef.
Indeed, the surfaces of $A _ { 2 n - 1 }$ , $A _ { 2 n - 2 } ^ { - }$ , $\overline { { A } } _ { 2 n - 3 } ^ { - }$ and ${  { \widetilde { E } } } _ { 7 }$ , ${ \widetilde { E } } _ { 8 } ^ { - }$ shapes have Picard rank 1, so $K _ { Y } + L$ is nef iff the genus $g \geq 0$ , i.e. all except $A _ { 1 }$ and the excluded $A _ { 0 } ^ { - }$ .
For the $D _ { 4 } , \widetilde { D } _ { 4 }$ shapes one has $K _ { Y } + L = 0$ .
For the other $D _ { 2 n }$ , $D _ { 2 n - 1 } ^ { - }$ , $\widetilde { D } _ { 2 n }$ shapes $K _ { Y } + L$ gives a $\mathbb { P } ^ { 1 }$ -fibration.
Finally, for the $E$ shapes the divisor $K _ { Y } + L$ is big and nef: for $^ - E _ { 6 } ^ { - }$ it is ample, for ${ } ^ { - } E _ { 7 }$ it contracts the left side $C _ { 1 }$ to an ${  { \widetilde { E } } } _ { 7 }$ surface, and for $^ - E _ { 8 } ^ { - }$ it contracts the right side $C _ { 2 }$ to an ${ \widetilde { E } } _ { 8 } ^ { - }$ surface.

The remaining shapes $A _ { 1 }$ and ${ \tilde { A } } _ { 1 } ^ { * }$ are easy to check directly.
In both cases $Y = \mathbb { P } ^ { 2 }$ and $C$ is a conic: two lines for $A _ { 1 }$ and a smooth conic for ${ \tilde { A } } _ { 1 } ^ { * }$ .
The divisor $L ^ { \prime }$ is big and nef and contracts a $( - 1 )$ -curve $E ^ { \prime }$ , the strict preimage of a line $E$ with the direction of the ideal $I$ , to a surface of shape $A _ { 0 } ^ { - }$ , resp.
$\widetilde { A } _ { 0 } ^ { - }$ .

Since $\scriptstyle { \frac { 1 } { 2 } } L ^ { \prime }$ is of the form $- ( K _ { Y } ^ { \prime } + C ^ { \prime } )$ , if it is big and nef then it is automatically semiample, see e.g. [Fuj12, Thm.6.1].
This concludes the proof.


Corollary 3.19. The shapes $A _ { 2 n - 1 }$ , $D _ { 2 n }$ , $\widetilde { D } _ { 2 n }$ , ${  { \widetilde { E } } } _ { 7 }$ can be primed a maximum of 4 times, shapes $ { \widetilde { A } } _ { 2 n - 2 } ^ { - }$ , $\widetilde { D } _ { 2 n - 1 } ^ { - }$ , ${ \widetilde { E } } _ { 8 } ^ { - }$ 3 times, and $\overline { { A } } _ { 2 n - 2 } ^ { - }$ , $^ - E _ { 6 } ^ { - }$ , $^ - E _ { 8 } ^ { - }$ 2 times each.

Remark 3.20. As we can see from the above proof, the cases $A _ { 1 } ^ { \prime } = A _ { 0 } ^ { - }$ and $( \widetilde { A } _ { 1 } ^ { * } ) ^ { \prime } = \widetilde { A } _ { 0 } ^ { - }$ are special.
Also, as we will see below, the dimension of the moduli space of pairs in these cases drops after priming, but in all other cases it is preserved.
For these reasons, and to avoid redundancy in our naming scheme, we do not allow primings of $A _ { 1 }$ and $\tilde { A } _ { 1 } ^ { * }$ .

We associate decorated Dynkin diagrams and symbols to primed shapes by modifying those of the corresponding pure shapes, as follows.
Recall that, in the pure Type III cases, each diagram has a leftmost and rightmost node, which sit next to the left and right sides, and these nodes are colored white/black if and only if the corresponding side is long/short.

Notation 3.21. For an $A D E$ shape, when priming on a long side once we circle the corresponding white node, and when priming a second time we also circle the neighboring black node.
In the Dynkin symbol we add a prime, resp.
double prime on the left or right, depending on whether we are priming at a point of the left side $C _ { 1 }$ or the right side $C _ { 2 }$ .
When priming on a short side, we circle the corresponding black node once and turn the $-$ superscript into a $^ +$ superscript (visually $-$ and 0 gives $^ +$ ).

For an $\widetilde A D E$ shape, we add up to 4 primes to the Dynkin symbol for a long side in $\widetilde { D } _ { 2 n }$ and ${  { \widetilde { E } } } _ { 7 }$ .
We also turn ${ \widetilde { E } } _ { 8 } ^ { - }$ into ${ \widetilde { E } } _ { 8 } ^ { + }$ before adding up to two more primes.
In the corresponding decorated diagrams, we circle one node for each prime using the following rule: first circle black nodes at the ends of the diagram, then white nodes at the ends of the diagram, then finally black nodes connected to circled white ones.

Remark 3.22. We note two pieces of mild ambiguity in this notation.
The first is that the decorated diagrams for the two shapes $' / A _ { 3 } ^ { \prime } , A _ { 3 } ^ { \prime \prime }$ and also for ${ } ^ { \prime \prime } D _ { 4 } ^ { \prime } , D _ { 4 } ^ { \prime \prime }$ are the same, so the diagram in these cases does not distinguish left and right sides.
In practice this won’t cause a problem: if we need to distinguish sides in these cases we will use the Dynkin symbols $' / A _ { 3 } ^ { \prime } , A _ { 3 } ^ { \prime \prime }$ , resp.
${ } ^ { \prime \prime } D _ { 4 } ^ { \prime } , D _ { 4 } ^ { \prime \prime }$ .

The decorated diagrams for the shapes ${ \mathrm { } } ^ { \prime } { \cal A } _ { 2 } ^ { + }$ and $" A _ { 2 } ^ { - }$ are also identical.
In fact, in this case we find that the $A D E$ surfaces ${ \mathrm { } } ^ { \prime } { \mathrm { } } A _ { 2 } ^ { + }$ and $\overline { { A } } _ { 2 } ^ { \prime \prime }$ are isomorphic, so this is just another instance of the diagram not distinguishing left and right sides.
These surfaces are obtained by priming $' A _ { 2 } ^ { - }$ and $\mathrm { \overline { { \Omega } } } A _ { 2 } ^ { \prime }$ , respectively, once on the right and a surface of $' A _ { 2 } ^ { - }$ shape is left/right symmetric (in fact it has a toric description which makes this symmetry apparent, see Lemma 3.25 and Figure 7).
One way to think of this symmetry is to consider $\mathrm { \Delta } ^ { \prime } A _ { 2 } ^ { - } = \mathrm { \Delta } ^ { - } A _ { 2 } ^ { \prime }$ as a symmetric $^ - D _ { 2 } ^ { - }$ shape.

Remark 3.23. If we wish to refer to an $A D E$ or $\widetilde A D E$ surface with an unspecified decoration (i.e. either undecorated or one of $- , \prime , \prime \prime , +$ ), we will use a question mark decoration ?.
For example,

$A _ { 2 n - 1 } ^ { \prime \prime }$ refers to one of the surfaces $A _ { 2 n - 1 }$ , $A _ { 2 n - 1 } ^ { \prime }$ , or $A _ { 2 n - 1 } ^ { \prime \prime }$ , while $' A _ { 2 n - 2 } ^ { ? }$ refers to one of the surfaces $' A _ { 2 n - 2 } ^ { - }$ or $' A _ { 2 n - 2 } ^ { + }$ .

Note that circled white nodes can denote either internal nodes or long sides on which a single priming has taken place.
This apparent notational ambiguity will be explained in the following subsection.

![](images/0cb3948e0c8e2f1844f11ef6622fca46689b1c70d8f0cf75231dfaf4a616c077.jpg)  
Figure 6. Decorated Dynkin diagrams for shapes $' / A _ { 3 } ^ { \prime }$ , ${ } ^ { \prime \prime } D _ { 5 } ^ { + }$ , ${ \widetilde { E } } _ { 8 } ^ { + \prime }$

Example 3.24. In Fig.
6 we give several examples of such diagrams.
The surfaces in these cases are not toric.
However, we can still use pseudo-toric pictures to indicate the lengths $\overline { { L } } \overline { { C } } _ { s } ^ { \prime }$ of the sides and the sides $C _ { s } ^ { \prime }$ which are contracted by $Y ^ { \prime }  { \overline { { Y } } } ^ { \prime }$ .
The volume of the surface is the volume of the polytope minus the number of primes, i.e. additional circles in the diagram as compared to a pure shape.

We list all the resulting 43 $A D E$ and 17 $\widetilde A D E$ shapes and their basic invariants in Tables 2 and 3. The pure shapes are highlighted.
Note that this table does not distinguish between left and right sides of $A$ -shapes (see Remark 3.9), so e.g. $A _ { 2 n - 2 } ^ { - }$ and ${ \overline { { A } } } _ { 2 n - 2 }$ are listed as the same surface.
The column for the singularities is explained in section 3E.

3D.
Primed shapes which are toric.
We observe that some of the primed shapes also admit toric descriptions.
This provides an explanation for a piece of notational ambiguity mentioned in the previous subsection: the priming operation on a long edge (white node) may be interpreted as modifying the diagram to make that node internal in the toric representation.

Lemma 3.25. The shapes $ { { \mathrm { \mathit { A } } } } _ { 2 n - 1 }$ , $' A _ { 2 n - 2 } ^ { - }$ , $D _ { 2 n } ^ { \prime }$ , $A _ { 2 n - 1 } ^ { \prime }$ are toric and can be represented by the polytopes listed in Table 4 and illustrated in Figs.
7 and $\delta$ .

Proof.
In these cases we can choose the ideals $I _ { i }$ to be torus invariant, with $\operatorname { S u p p } I _ { i }$ corresponding to vertices of the polytopes of the pure shapes $A _ { 2 n - 1 }$ , $A _ { 2 n - 2 } ^ { - }$ , $D _ { 2 n }$ , and $I _ { i }$ pointing in the directions of the respective sides.
Then the blown up surface $Y ^ { \prime } = \overline { { Y } } ^ { \prime }$ is also toric, for the polytope obtained from the old polytope by cutting corners, as in Table 4 and Fig.
8. 

![](images/16c269f117c26e6e952212333ae9cca2a6db09a4fc2409a25bdcf51ce10c3a98.jpg)  
Figure 7. Toric A0 shapes: $A _ { 2 } ^ { - } = \mathrm { \bar { ~ } A _ { 2 } ^ { \prime } } = \mathrm { \bar { ~ } D _ { 2 } ^ { - } }$ , $\mathrm { { \mathit { A } } _ { 3 } }$ , $' A _ { 4 } ^ { - }$

Remark 3.26. For other primed shapes, the surfaces are generally not toric but toric surfaces do appear for certain special directions of the ideals being blown up.
Some of them are shown in Fig.
9.

Table 2. All $A D E$ shapes  
![](images/5ca3995175c34e60f103b92299337038d1862865d811b54ca731b684ffbcc679.jpg)

Table 3. All $\widetilde A D E$ shapes  
![](images/0ad007d0250bb38a31b19ac7a3721615ba031a77aefd0e7a1ac9129e564b68cd.jpg)

Table 4. Polytopes for the toric primed shapes  
![](images/78b416be5555645312860493d95180d70aa50ead083648ddbc2a39d6cc0835b3.jpg)

![](images/59576a6dd35b8672bdf019678d11926a153c18ab740b846323b80cdac4c7d6d8.jpg)  
Figure 8. Toric $D ^ { \prime }$ and $A ^ { \prime }$ shapes: $D _ { 8 } ^ { \prime }$ , ${ \mathit { A } } _ { 5 } ^ { \prime }$ , ${ \mathrm { \Delta } } ^ { \prime } A _ { 7 } ^ { \prime }$

![](images/f83f2a5925424fa065b872f84d3d92f83e319ef3fe68c61b47cfee869a2cd354.jpg)  
Figure 9. Some special toric surfaces in shapes $\mathcal { D } _ { 7 } ^ { - }$ , ${ \cal { D } } _ { 4 } ^ { \prime }$

# 3E.

Singularities of $A D E$ and $\widetilde A D E$ surfaces.

Theorem 3.27 (Singularities).
Let $( Y , C )$ be a surface of pure $s h a p e \neq A _ { 1 } , \widetilde { A } _ { 1 } ^ { * }$ .
With notation as in Definition 3.13, when priming $( Y , C )$ to $( \overline { { Y } } ^ { \prime } , \overline { { C } } ^ { \prime } )$ the only curves contracted by $g \colon Y ^ { \prime } \to { \overline { { Y } } } ^ { \prime }$ are:

(1) The sides $C _ { s } ^ { \prime }$ with $L ^ { \prime } C _ { s } ^ { \prime } = 0$ .
These contract to nonklt $( \overline { { \mathrm { Y } } } ^ { \prime } , \overline { { \mathrm { C } } } ^ { \prime } )$ .  
(2) A collection of $\left( - 2 \right)$ curves disjoint from $C ^ { \prime }$ .
These contract to Du Val singularities disjoint from nonklt $\mathrm { ( Y , C ) }$ .

Proof.
Let $E ^ { \prime }$ be a curve with $L ^ { \prime } E ^ { \prime } = 0$ .
As in the proof of Theorem 3.18, if $K _ { Y } + L$ is nef and $E ^ { \prime } \neq C _ { s } ^ { \prime }$ then $( K _ { Y ^ { \prime } } + L ^ { \prime } ) E ^ { \prime } = 0$ , so $K _ { Y ^ { \prime } } E ^ { \prime } = 0$ .
Since $E ^ { \prime }$ is disjoint from the boundary, it lies in the smooth part of $Y ^ { \prime }$ .
We have $E ^ { \prime 2 } < 0$ , and by the genus formula the only possibility is $E ^ { \prime } \simeq \mathbb { P } ^ { 1 }$ with $E ^ { \prime 2 } = - 2$ .


Corollary 3.28. The singularities of the $A D E$ and $\widetilde A D E$ surfaces $( Y , C )$ lying in the nonklt locus of $( Y , C )$ depend only on the shape and are those listed in the last column of Tables 2 and 3.

Notation 3.29. In Tables 2 and 3 we use the following notation for singularities.
We denote simple nodes by the usual $A _ { 1 }$ .
For cyclic quotient singularities, whose resolutions are a chain of curves, we use the notation $( n _ { 1 } , n _ { 2 } , \ldots , n _ { k } )$ , where $- n _ { i }$ is the self-intersection number of the $_ i$ th curve in the chain; note that $( 2 , 2 , \ldots , 2 )$ corresponds to the Du Val singularity $A _ { n }$ .
For more complicated singularities, whose resolution is not necessarily a chain of curves, we use the following notation: $( n _ { 1 } , n _ { 2 } , \ldots , n _ { k } ; 2 ^ { 2 } )$ denotes a singularity obtained by contracting a configuration of exceptional curves with the first dual graph in Fig.
10. Note that this includes Du Val singularities of type $D _ { n }$ , which are denoted by $( 2 , 2 , \ldots , 2 ; 2 ^ { 2 } )$ .

![](images/266408cdcdd347834e99e67d555db8e08ebd899c2010f87f0917ec124339a64f.jpg)  
Figure 10. Singularities $( n _ { 1 } , n _ { 2 } , \ldots , n _ { k } ; 2 ^ { 2 } )$ and $( 2 ^ { 2 } ; n _ { 1 } , n _ { 2 } , \ldots , n _ { k } ; 2 ^ { 2 } )$

Finally, we will use the expression $( 2 ^ { 2 } ; n _ { 1 } , n _ { 2 } , \ldots , n _ { k } ; 2 ^ { 2 } )$ to denote a singularity obtained by contracting a configuration of exceptional curves with the second dual graph in Fig.
10. Two apparently degenerate cases of this notation are $A _ { 1 } = ( 2 )$ and $( n ; 2 ^ { 2 } ) = ( 2 , n , 2 )$ ; we nonetheless use both notations, as it is useful to make a distinction when we discuss double covers.
We will also often use $( n ; 2 ^ { 4 } )$ in place of $( 2 ^ { 2 } ; n ; 2 ^ { 2 } )$ .
Separately note that for $n = 1$ the “singularities” $( n )$ and $( n , 2 )$ are in fact smooth points.

For completeness, we also note the corresponding singularities on the double covers.
The double cover of a simple node $A _ { 1 }$ is always a smooth point, and the double cover of a cyclic quotient singularity $( n _ { 1 } , n _ { 2 } , \ldots , n _ { k } )$ is always a pair of cyclic quotient singularities with the same resolution; this explains why we draw a distinction between $A _ { 1 }$ , which has smooth double cover, and (2), which has double cover a pair of (2) singularities.

The double cover of a singularity of type $( n _ { 1 } , n _ { 2 } , \ldots , n _ { k } ; 2 ^ { 2 } )$ is a cyclic quotient singularity $( n _ { 1 } , n _ { 2 } , \ldots , n _ { k - 1 } , 2 n _ { k } - 2 , n _ { k - 1 } , \ldots , n _ { 1 } )$ ; this explains the second degenerate piece of notation, as $( 2 , n , 2 )$ has double cover a pair of $( 2 , n , 2 )$ singularities, and $( n ; 2 ^ { 2 } )$ has double cover a single $( 2 n - 2 )$ singularity.
Finally, the double cover of a $( 2 ^ { 2 } ; n _ { 1 } , n _ { 2 } , \ldots , n _ { k } ; 2 ^ { 2 } )$ singularity, for $k \geq 2$ , is a cusp singularity whose resolution is a cycle of rational curves with the negatives of self-intersections $( 2 n _ { 1 } - 2 , n _ { 2 } , \ldots , n _ { k - 1 } , 2 n _ { k } - 2 , n _ { k - 1 } , \ldots , n _ { 2 } )$ ordered cyclically, and the double cover of an $( n ; 2 ^ { 4 } )$ singularity is a simple elliptic singularity whose resolution is a smooth elliptic curve with the minus self-intersection $2 n - 4$ .

3F.
Recovering a precursor of pure shape.
The aim of this subsection is to explore to what extent the priming operation is reversible.
In other words, given an $A D E$ or $\widetilde A D E$ surface of primed shape, can we uniquely recover the surface of pure shape from which it was obtained by priming?

Lemma 3.30 (Non-redundancy).
When distinguishing the left and right sides, the only redundant case in the decorated Dynkin symbol notation for the shapes is $A _ { 2 } ^ { - } = - A _ { 2 } ^ { \prime }$ , for which also a symmetric but degenerate notation $^ - D _ { 2 } ^ { - }$ may be used.
(See Remark 3.22. Recall also that $A _ { 1 } ^ { \prime } = A _ { 0 } ^ { - }$ , ${ \cal { A } } _ { 1 } = { \cal { - A } } _ { 0 }$ , and $( \widetilde { A } _ { 1 } ^ { * } ) ^ { \prime } = \widetilde { A } _ { 0 } ^ { - }$ ; for this reason we do not allow primings of $A _ { 1 }$ and ${ \widetilde { A } } _ { 1 } ^ { * }$ .)

When not distinguishing the left and right sides, there are also the cases coming from the $\mathbb { Z } _ { 2 }$ symmetry of $A _ { 2 n - 1 }$ , $\overline { { A } } _ { 2 n - 3 } ^ { - }$ , $^ - D _ { 2 } ^ { - }$ , $D _ { 4 }$ , and $^ - E _ { 6 } ^ { - }$ : ${ \mathrm { \mathit { A } } } _ { 5 } = { \mathrm { \mathit { A } } } _ { 5 } ^ { \prime }$ , $D _ { 4 } ^ { \prime } = D _ { 4 }$ , $E _ { 6 } ^ { - } = ~ ^ { - } E _ { 6 }$ , etc., including ${ } ^ { \prime \prime } A _ { 2 } ^ { - } = { } ^ { \prime } A _ { 2 } ^ { + }$ .
(See Remarks 3.9 and 3.22.)

Proof.
By Tables 2 and 3, most of the shapes are already distinguished by the main invariants and singularities.
The only exception is $D _ { 2 n } ^ { \prime }$ and $\left. T _ { 2 n } \right.$ for $2 n \geq 6$ .
However, in these cases the sheaf $K _ { Y } + L$ gives a $\mathbb { P } ^ { 1 }$ -fibration.
The left side $C _ { 1 }$ is a bisection of this fibration and $C _ { 2 }$ lies in a fiber, so the two primings are not isomorphic.


Definition 3.31. Let $f \colon { \widetilde { Y } }  Y$ be the minimal resolution of an $A D E$ or $\widetilde { A } \widetilde { D } \widetilde { E }$ surface $( Y , C )$ .
Let $\widetilde { C } _ { s }$ be the strict transforms on $\widetilde { Y }$ of the components $C _ { s }$ of $C$ , and let $F _ { i }$ be the $f$ -exceptional curves.
Let $C ^ { \perp } : = \langle C _ { s } , F _ { i } \rangle ^ { \perp } \subset \operatorname { P i c } \widetilde { Y }$ and let $\Lambda _ { 0 } : = C ^ { \bot } \cap B ^ { \bot }$ .
Denote by $\Delta _ { 0 } ^ { ( 2 ) }$ the set of $\left( - 2 \right)$ vectors in $\Lambda _ { 0 }$ , by $\Lambda _ { 0 } ^ { ( 2 ) }$ the root system generated by them, and by $W _ { 0 } = W ( \Delta _ { 0 } ^ { ( 2 ) } )$ the corresponding Weyl group.
Since $B ^ { 2 } > 0$ , the lattice $\Lambda _ { 0 }$ is negative definite, and ${ \Lambda } _ { 0 } ^ { ( 2 ) }$ and $W _ { 0 }$ are of $A D E$ type.

Theorem 3.32. For a surface $( \overline { { Y } } ^ { \prime } , \overline { { C } } ^ { \prime } )$ of a primed shape, its pure shape precursor $( Y , C )$ , from which it comes by priming, is defined up to the action of $W _ { 0 }$ .
The group $W _ { 0 }$ is trivial except for the following shapes:

(1) For $2 n \geq 6$ , for $D _ { 2 n }$ and $D _ { 2 n - 1 } ^ { - }$ with $k$ primes on the left and any number of primes on the right, and for $\widetilde { D } _ { 2 n }$ with $k$ primes one has $W _ { 0 } = W ( A _ { 1 } ^ { k } ) = S _ { 2 } ^ { k }$ .

(2) the following exceptional shapes of genus $\mathit { 1 }$

$$
\frac { s h a p e \ | \ A _ { 3 } ^ { \prime } \ A _ { 3 } ^ { \prime \prime } \ D _ { 4 } ^ { \prime \prime } \ D _ { 4 } ^ { \prime \prime } \ D _ { 4 } ^ { \prime \prime } \ D _ { 4 } ^ { \prime } \quad ^ { \prime } D _ { 4 } ^ { \prime \prime } \quad \widetilde { D } _ { 4 } \quad \widetilde { D } _ { 4 } ^ { \prime } \quad \widetilde { D } _ { 4 } ^ { \prime \prime } \quad \widetilde { D } _ { 4 } ^ { \prime \prime \prime } } { \Lambda _ { 0 } ^ { ( 2 ) } } \ ^ { * } \ A _ { 1 } \quad A _ { 1 } ^ { 2 } \quad A _ { 2 } ^ { 3 } \quad \ A _ { 3 } ^ { \prime } \quad \ A _ { 4 } ^ { \prime \prime } \quad ^ { \prime \prime } \ .
$$

For the ADE shapes for a generic surface of the given shape the Weyl group $W _ { 0 }$ acts freely on the choices of a precursor, and for the $\widetilde { D }$ shapes it acts with a degree 2 stabilizer.
For a generic surface of the given shape there are no singularities outside the set nonklt $( \overline { { \mathrm { Y } } } ^ { \prime } , \overline { { \mathrm { C } } } ^ { \prime } )$ .
For special surfaces there may exist additional Du Val singularities for all the $A D E$ root sublattices of ${ \Lambda } _ { 0 } ^ { ( 2 ) }$ , and all of these appear.

In addition, for the exceptional case $\mathrm { \Delta } ^ { \prime \prime } A _ { 2 } ^ { - } = \mathrm { \Delta } ^ { + } A _ { 2 } ^ { \prime }$ of Lemma 3.30 one has $W _ { 0 } = 0$ , and there are two choices for the ${ \overline { { \mathbf { A } } } } _ { 2 }$ precursors, and only one choice for $A _ { 2 } ^ { - }$ .

Example 3.33. For $' / T _ { 6 }$ one has $W ( A _ { 1 } ^ { 2 } ) = S _ { 2 } ^ { 2 }$ , and generically there are 4 choices for a precursor of shape $D _ { 6 }$ .
For special choices of the directions of priming ideals $I _ { i }$ the surfaces may have additional singularities of types $2 A _ { 1 }$ or $A _ { 1 }$ .

For $\widetilde { D } _ { 4 } ^ { \prime \prime \prime }$ one has $| W ( D _ { 4 } ) | = 1 9 2$ , and generically there are 96 choices for a precursor of shape ${ \widetilde { D } } _ { 4 }$ .
For special choices of the directions of priming ideals $I _ { i }$ the surfaces may have additional singularities of types $D _ { 4 }$ , $A _ { 3 }$ , $3 A _ { 1 }$ , $A _ { 2 }$ , $2 A _ { 1 }$ , $A _ { 1 }$ .

Proof of Thm.
3.32. We computed the lattice $\Lambda _ { 0 }$ for every shape in Tables 2, 3 by a lengthy but straightforward computation.
The root systems $\Lambda _ { 0 } ^ { ( 2 ) }$ are the ones stated in (1), (2).
For example, for ${ } ^ { \prime \prime } D _ { 2 n } ^ { \prime \prime }$ one has $\Lambda _ { 0 } = A _ { 1 } ^ { 2 } \oplus \left. - 4 \right.$ , and the root system is $A _ { 1 } ^ { 2 }$ .
We skip the details.

We find the precursors and singularities separately but then confirm that the answer is the same as above.
Let $f \colon Y ^ { \prime } \to Y$ be the first step in the priming, before the contraction $Y ^ { \prime }  \overline { { Y } } ^ { \prime }$ (see

Definition 3.13). Let $E ^ { \prime } \neq C _ { s } ^ { \prime }$ be a curve with $L ^ { \prime } E ^ { \prime } = 0$ and $E$ its image on $Y$ .
As in the proofs of Theorem 3.18, 3.27, one must have $( K _ { Y } + L ) E = 0$ , and such a curve may only exist in

(1) $D _ { 2 n }$ , $D _ { 2 n - 1 } ^ { - }$ shapes for $2 n \geq 6$ , where $K _ { Y } + L$ gives a $\mathbb { P } ^ { 1 }$ -fibration over $\mathbb { P } ^ { 1 }$ , (2) the shapes of genus 1, where $K _ { Y } + L = 0$ .

Let us consider the case (1).
The only possibilities for $E$ are the fibers of the $\mathbb { P } ^ { 1 }$ fibration.
Let $P _ { i } \in C _ { 1 }$ , and $I _ { i }$ with $\operatorname { S u p p } I _ { i } = P _ { i }$ be an ideal appearing in the priming.
Let $E$ be a fiber of the $\mathbb { P } ^ { 1 }$ fibration passing through $P _ { i }$ .
If the direction of $I _ { i }$ is generic, namely it is not the direction of $E$ then on the blowup $Y ^ { \prime }$ the preimage $f ^ { - 1 } ( E )$ consists of two curves: the strict preimage $E ^ { \prime } = f _ { * } ^ { - 1 } ( E )$ and the exceptional divisor $F ^ { \prime }$ .
Both of them are $\mathbb { P } ^ { 1 }$ , and one has $( E ^ { \prime } ) ^ { 2 } = F ^ { 2 } = - { \textstyle \frac { 1 } { 2 } }$ and $E ^ { \prime } C = F C = 1$ .
Contracting either $F ^ { \prime }$ or $E ^ { \prime }$ gives a pure shape precursor, so we get two choices.
On the other hand, if $I _ { i }$ has the direction $E$ , i.e. $I _ { i } \supset I ( E )$ then $f ^ { - 1 } ( E ) = E ^ { \prime } \cup F$ , $E ^ { \prime }$ lies in the smooth part of $Y ^ { \prime }$ , and one has $( E ^ { \prime } ) ^ { 2 } = - 2$ and $E ^ { \prime } C = 0$ .
The linear system $| L ^ { \prime } |$ contracts $E ^ { \prime }$ to an $A _ { 1 }$ singularity.
Thus, in this case there is one precursor and ${ \overline { { Y } } } ^ { \prime } \setminus { \overline { { C } } } ^ { \prime }$ has an extra $A _ { 1 }$ singularity.

In the case (2) for any curve $E \subset Y$ one has $E ^ { \prime } \cdot f ^ { * } ( K _ { Y } + L ) = 0$ .
The shapes of genus 1 are $A _ { 3 }$ , $A _ { 2 } ^ { - }$ , $\overline { { \mathbf { A } } } _ { 1 } ^ { - }$ , $D _ { 4 }$ , ${ \widetilde { D } } _ { 4 }$ and those obtained from these by priming.
For all of them the minimal resolution $\widetilde { Y }$ is a weak del Pezzo (i.e. with big and nef $- K _ { \widetilde { Y } }$ ) of degree 2, 4, 6, or 8. To analyze both possible precursors and singularities we computed the graphs of $( - 1 )$ and $\left( - 2 \right)$ curves on the minimal resolution of singularities $\widetilde { Y }$ .
These graphs are classically known, see e.g. [Dol12, Ch.8].
The answers are the same as given in the statement of the Theorem.

The exceptional case $\mathrm { \Delta } ^ { \prime \prime } A _ { 2 } ^ { - } = \mathrm { \Delta } ^ { + } A _ { 2 } ^ { \prime }$ of genus 1 is treated in the same way.

4. Classification of nonklt log del Pezzo surfaces of index 2

The purpose of this Section is to prove:

Theorem A.
The log canonical non-klt del Pezzo surfaces $( Y , C )$ with $2 ( K _ { X } + C )$ Cartier and $C$ reduced (or possibly empty) are exactly the same as the $A D E$ and $\widetilde { A } \widetilde { D } \widetilde { E }$ surfaces $( Y , C )$ , pure and primed.

Log del Pezzo surfaces with boundary $( Y , C )$ such that $- 2 ( K _ { Y } + C )$ is ample and Cartier were classified by Nakayama in [Nak07], over fields of arbitrary characteristic.
Some work is still required to extract Theorem A from his classification.
First, in [Nak07] the divisor $C$ is half-integral, and in our case it should be integral.

Secondly, the case of genus $g = 1$ in [Nak07] is reduced to classifying log canonical pairs $( Y , C )$ such that $Y$ is a Gorenstein del Pezzo surface and $C$ is an effective Weil divisor with $- K _ { Y } \sim 2 C$ .
The classification of such pairs is not provided.
Rather than trying to perform such a classification, we adapt the arguments from other parts of [Nak07] to deal with this case.

For ease of the use of [Nak07], for this section only, we adopt the notation of the latter paper.
The basic setup is as follows.
The log del Pezzo surface with boundary is denoted $( S , B )$ , versus our $( Y , C )$ .
At the outset, let us mention an important general result [Nak07, Cor.3.20] generalizing that of [AN06, Thm.1.4.1]:

Theorem 4.1 (Smooth Divisor Theorem).
Let $( S , B )$ be a log del Pezzo surface with boundary of index $\leq 2$ .
Then a general element of the linear system $| - 2 ( K _ { S } + B ) |$ is smooth.

By [Nak07, 3.16, 3.10], the only pairs with irrational $S$ and integral $B$ are cones over elliptic curves which we call $\tilde { A } _ { 2 n - 1 }$ .
So below we assume that $S$ is rational.
The minimal resolution of singularities of $S$ is denoted by $\alpha \colon M \to S$ .
One defines:

(1) An effective $\mathbb { Z }$ -divisor $E _ { M }$ on $M$ by the formula $K _ { M } = \alpha ^ { * } ( K _ { S } + B ) - { \textstyle { \frac { 1 } { 2 } } } E _ { M }$ .
Since we assume the pair $( S , B )$ to be lc, $E _ { M }$ has multiplicities 1 and 2. If $B = 0$ and $S$ is log terminal then $E _ { M }$ is reduced.
Otherwise, there is at least one component of multiplicity 2.  
(2) A big and nef line bundle $L _ { M } = \alpha ^ { * } ( - 2 ( K _ { S } + B ) )$ .
Thus, one has $L _ { M } = - 2 K _ { M } - E _ { M }$ .

(3) The genus $g ( S , B ) = \textstyle { \frac { 1 } { 2 } } ( K _ { M } + L _ { M } ) L _ { M } + 1$ .
This is the genus of a general element of $| - 2 ( K _ { S } + B ) |$ .

This is the standard notation used in [Nak07]:

On $\mathbb { P } ^ { 2 }$ , a line is denoted by $\ell$ .  
On $\mathbb { F } _ { n }$ , a zero section is $\sigma$ , an infinite section $\sigma _ { \infty }$ , and a fiber $\ell$ .  
• On $\mathbb { P } ( 1 , 1 , n )$ , $\ell$ is the image of a fiber from $\mathbb { F } _ { n }$ , i.e. a line through the $\textstyle { \frac { 1 } { n } } ( 1 , 1 )$ singular point $( 0 , 0 , 1 )$ .
$\bar { \sigma } _ { \infty }$ is the image of $\sigma _ { \infty }$ on $\mathbb { P } ( 1 , 1 , n )$ ; note that $\bar { \sigma } _ { \infty } \sim n \ell$ .

The classification of log del Pezzo surfaces with boundary is divided into three cases:

(1) $K _ { M } + L _ { M }$ is not nef.  
(2) $K _ { M } + L _ { M }$ is nef and $g \geq 2$ .  
(3) $K _ { M } + L _ { M }$ is nef and $g = 1$ .

4A.
The case $K _ { M } + L _ { M }$ is not nef.
By [Nak07, 3.11], the only cases for us are:

(1) $S = \mathbb { P } ^ { 2 }$ , $\deg B = 2 \implies B$ is a smooth conic (our $\tilde { A } _ { 1 } ^ { * }$ ) or two lines ( $A _ { 1 }$ ).  
(3) $S = \mathbb { P } ( 1 , 1 , n )$ , $n \geq 2$ and $B \in | ( \frac { n } { 2 } + 2 ) \ell |$ , in particular $n$ is even.

In the latter case, note that the smallest divisor not passing through the singular point $( 0 , 0 , 1 )$ is $\bar { \sigma } _ { \infty } \sim n \ell$ .
We consider the subcases:

(a) $B \not \ni ( 0 , 0 , 1 )$ .
We need $\frac { n } { 2 } + 2 \geq n \implies n = 2 , 4$ .
If $n = 2$ then $B \in | 3 \bar { \ell } |$ is not Cartier, a contradiction.
If $n = 4$ then $B \in | 4 \ell | = | O ( 1 ) |$ , $L _ { M } = \mathcal { O } ( 1 )$ .
This is a degenerate subcase of $\widetilde { A } _ { 1 } ^ { * }$ , when $\mathbb { P } ^ { 2 }$ degenerates to $\mathbb { F } _ { 4 } ^ { 0 } = \mathbb { P } ( 1 , 1 , 4 )$ (see Subsection $\mathrm { 3 B ( 2 ) }$ ).  
(b) $B \ni ( 0 , 0 , 1 )$ and is smooth there.
The strict preimage of $B$ is then $\tilde { B } \sim \ell + k \sigma _ { \infty }$ for some $k \geq 0$ .
Then $B \sim ( 1 + k n ) \ell \implies { \textstyle { \frac { n } { 2 } } } + 2 = 1 + k n$ .
It follows that $n = 2$ and $k = 1$ .
If $B$ is irreducible then this is our $\widetilde { A } _ { 0 } ^ { - }$ case; if $B = \ell + \bar { \sigma } _ { \infty }$ then this is $A _ { 0 } ^ { - }$ .  
(c) $B \ni ( 0 , 0 , 1 )$ and has two branches there.
Then $\tilde { B } \sim 2 \ell + k \sigma _ { \infty }$ and $\begin{array} { r } { B \sim ( 2 + k n ) \ell \sim ( \frac { n } { 2 } + 2 ) \ell } \end{array}$ .
This is impossible.

4B.
$K _ { M } + L _ { M }$ is nef and $g \geq 2$ .
Nakayama defines a basic pair to be a projective surface $X$ and a nonzero effective $\mathbb { Z }$ -divisor $E$ so that, for $L = - 2 K _ { X } - E$ one has:

(C1) $K _ { X } + L$ is nef,  
$( \mathcal { C } 2 )$ $( K _ { X } + L ) L = 2 g - 2 > 0$ ,  
(C3) $L E _ { i } \geq 0$ for any irreducible component $E _ { i }$ of $E$ .

So, the minimal resolution of a log del Pezzo surface with boundary of index $\leq 2$ is a basic pair, unless $B = 0$ and $S$ has Du Val singularities (because then $E = 0$ ).
Vice versa, by [Nak07, 3.19], any basic pair is the minimal resolution of a log del Pezzo surface with boundary of index $\leq 2$ , with the semiample line bundle $N L$ , $N \gg 0$ , providing the contraction.

The next step is to run MMP for the divisor $K _ { X } + { \textstyle { \frac { 1 } { 2 } } } L$ .
Namely, if for some $( - 1 )$ -curve $\gamma$ one has $( 2 K _ { X } + L ) \gamma = - E \gamma < 0$ then $L \gamma = E \gamma = 1$ , the curve $\gamma$ can be contracted $\tau \colon X  Z$ to obtain a new basic pair $( Z , E _ { Z } )$ , and one has $K _ { X } + L = \tau ^ { * } ( K _ { Z } + L _ { Z } )$ , $K _ { X } + E = \tau ^ { * } ( K _ { Z } + E _ { Z } )$ .
Here, $E _ { Z } = \tau _ { * } ( E )$ and it is again nonzero.

The minimal basic pairs, without the $( - 1 )$ -curves as above are $\mathbb { P } ^ { 2 }$ and $\mathbb { F } _ { n }$ , and it is easy to list the possibilities for $E$ on them.
Nakayama proves that the morphism $\phi \colon M \to X$ to a minimal basic pair is a sequence of blowups of the simplest type which can be conveniently locally encoded by a zero-dimensional subscheme $\Delta$ of a smooth curve, i.e. a subscheme given by an ideal $I = ( y , x ^ { k } )$ for some local parameters $x , y$ and $k > 0$ .
If $\mu \colon Y  X$ is a simple blowup then $I _ { Y } = \mu ^ { * } I =$ $( y , x ^ { k - 1 } ) \otimes \mathcal { O } _ { Y } ( - \Gamma )$ , where $\Gamma$ is the exceptional $( - 1 )$ -curve of $\mu$ .
Then one continues to eliminate $I _ { Y }$ by induction, making $k$ blowups in total.
Equivalently, one can blow up the ideal $I$ and then take the minimal resolution.

In this way, we obtain a triple $( X , E , \Delta )$ satisfying ( $\mathcal { F } 1$ ) $( X , E )$ is a minimal basic pair, $L = - 2 K _ { X } - E$ .

$( \mathcal { F } 2 )$ $\Delta$ is empty or a zero-dimensional subscheme of $X$ which is locally a subscheme of a smooth curve,  
$\left( \mathcal { F 3 } \right)$ $\Delta$ is a subscheme of $E$ considered as a subscheme of $X$ (recall that $E$ is an effective Cartier divisor with multiplicities $1$ or 2) such that for every reduced irreducible component $E _ { i }$ of $E$ one has $L E _ { i } \ge \deg ( \Delta \cap E _ { i } )$ .

Nakayama calls these quasi fundamental triplets.
Vice versa, by [Nak07, 4.2] for any quasi fundamental triplet $( X , E , \Delta )$ the pair $( M , E _ { M } )$ obtained by eliminating $\Delta$ is a basic pair, that is the minimal resolution of singularities of a log del Pezzo surface with boundary.
Thus, one is reduced to enumerating quasi fundamental triplets.

For a given basic pair $( M , E _ { M } )$ , the sequence of blowdowns of $( - 1 )$ -curves and thus the resulting quasi fundamental triplet $( X , E , \Delta )$ are not unique.
To cure this, Nakayama defines a fundamental triplet that satisfies additional normalizing conditions [Nak07, Def. 4.3].
He then proves in [Nak07, 4.9] that the fundamental triplet exists and is unique in most cases, including all the cases when $( S , B )$ is strictly log canonical – the case that we operate in.
For this case, the possible fundamental triplets are listed in [Nak07, 4.7(2)].

It remains to consider these fundamental triplets and the resulting minimal resolutions $M$ .
But first, we can narrow down the possibilities for $\Delta$ since our situation is restricted by the condition that $B$ is integral and not half-integral as in [Nak07].

Definition 4.2. We introduce the following simple subschemes $\Delta \subset E$ .

$$
{ \begin{array} { r l r l } & { ~ ( \mathbf { \nabla } \cdot \mathbf { \nabla } ) } & { ( y ) } & { ~ ( y , x ) } & { ~ { \mathrm { d e g } } ( \Delta ) } & { ~ { \mathrm { m u l t } } _ { P } ( \Delta \cap E _ { i } ) } \\ & { ~ ( - ) _ { 1 } ~ { \mathrm { ~ ( ~ } } y ) } & { ( y , x ^ { 2 } ) } & { 1 } & { 1 } \\ & { ~ ( - ) ~ } & { ( y ^ { 2 } ) } & { ( y , x ^ { 2 } ) } & { 2 } & { 2 } \\ & { ~ ( \mathbf { \nabla } \cdot \mathbf { \nabla } ) } & { ( y ^ { 2 } , x ) } & { 2 } & { 1 } & { \qquad \mathbf { \nabla } \cdot \mathbf { \nabla } } \\ & { ~ ( + ) } & { ( y ^ { 2 } ) } & { ( y ^ { 2 } , y + \epsilon x ^ { 2 } ) , \epsilon \neq 0 } & { 4 } & { 2 } \end{array} }
$$

An alternative description for the last subscheme is $( y + \epsilon x ^ { 2 } , x ^ { 4 } )$ .

The subschemes appearing in this definition are given suggestive names, which reflect the notation used for priming in Section 3C.
The reason for this will become clear in the proof of Theorem 4.8.

Lemma 4.3. The effect of eliminating the subschemes of (4.2) is as follows.

$( \cdot \cdot )$ $E _ { M } = 1 E _ { i } + 0 \Gamma _ { 1 }$ , $\Gamma _ { 1 } ^ { 2 } = - 1$ , $E _ { i } \Gamma _ { 1 } = 1$ , $L _ { M } \Gamma _ { 1 } = 1$ .  
$( - ) _ { 1 }$ $( - )$ $E _ { M } = 1 E _ { i } + 0 \Gamma _ { 1 } + 0 \Gamma _ { 2 }$ $E _ { M } = 2 E _ { i } + 2 \Gamma _ { 1 } + 1 \Gamma _ { 2 }$ , , $\Gamma _ { 1 } ^ { 2 } = - 1$ $\Gamma _ { 1 } ^ { 2 } = - 1$ , , Γ 22 $\Gamma _ { 2 } ^ { 2 } = - 2$ $\Gamma _ { 2 } ^ { 2 } = - 2$ Γ22 , , $E _ { i } \Gamma _ { 1 } = \Gamma _ { 1 } \Gamma _ { 2 } = 1$ $E _ { i } \Gamma _ { 1 } = \Gamma _ { 1 } \Gamma _ { 2 } = 1$ , , $L _ { M } \Gamma _ { 1 } = 1$ $L _ { M } \Gamma _ { 1 } = 1$ .
.  
( 0 ) $E _ { M } = 2 E _ { i } + 1 \Gamma _ { 1 } + 0 \Gamma _ { 2 }$ , $\Gamma _ { 1 } ^ { 2 } = - 2$ , $\Gamma _ { 2 } ^ { 2 } = - 1$ , $E _ { i } \Gamma _ { 1 } = \Gamma _ { 1 } \Gamma _ { 2 } = 1$ , $L _ { M } \Gamma _ { 2 } = 1$ .  
(+) $E _ { M } = 2 E _ { i } + 2 \Gamma _ { 1 } + 1 \Gamma _ { 2 } + 1 \Gamma _ { 3 } + 0 \Gamma _ { 4 }$ , $\Gamma _ { 1 } ^ { 2 } = \Gamma _ { 2 } ^ { 2 } = \Gamma _ { 3 } ^ { 2 } = - 2$ , $\Gamma _ { 4 } ^ { 2 } = - 1$ , $E _ { i } \Gamma _ { 1 } = \Gamma _ { 1 } \Gamma _ { 2 } = \Gamma _ { 1 } \Gamma _ { 3 } =$ $\Gamma _ { 3 } \Gamma _ { 4 } = 1$ , $L _ { M } \Gamma _ { 4 } = 1$ .

It is pictured in Fig.
11.

![](images/9127d7dc4348f1e10836bc7a04080337b750751f27a667868e38a52417a259eb.jpg)  
Figure 11. Effect of eliminating simple subschemes

Proof.
This is direct computation, following [Nak07, Sec.2].

Notation 4.4. In Fig.
11, the rectangle with label “ $d ^ { \ast }$ denotes an irreducible component $E _ { i }$ of $E$ with $E _ { i } ^ { 2 } = - d$ .
The small nodes are $\mathbb { P } ^ { 1 }$ ’s of square $( - 1 )$ , the large ones of square $\left( - 2 \right)$ .
Rectangles and nodes are shown in bold black, resp.
gray or white, if they appear in $E _ { M }$ with multiplicity 2, resp.
1 or 0. The half-edges denote $\mathrm { m u l t } _ { P } ( \Delta \cap E _ { i } )$ , which are 2 (double line) or 1 (single line).
When we are working with a geometric triple $( X , B + { \textstyle { \frac { 1 + \epsilon } { 2 } } } D )$ , where $D \in \vert - 2 K _ { S } - E \vert$ is a section, these half edges are the local intersection numbers $D E _ { i }$ at a point $P \in D \cap E _ { i }$ .
The double edge means that $D$ is tangent to $E _ { i }$ at $P$ .

The following lemma is a direct consequence of a proof from [Nak07].

Lemma 4.5. The pair $( S , B )$ is log canonical iff for every irreducible component $E _ { i }$ of $E$ in the fundamental triplet $( X , E , \Delta )$ , one has $\mathrm { m u l t } _ { E } ( E _ { i } ) \leq 2$ , $\Delta$ is disjoint from the nodes of the double part $\llangle E \lrcorner$ of $E$ , and $\mathrm { m u l t } _ { P } ( \Delta \cap E _ { i } ) \leq 2$ for every irreducible component $E _ { i }$ with $\mathrm { m u l t } _ { E } ( E _ { i } ) = \ 2$ and all $P \in \Delta$ .

Proof.
Follows immediately from the proof of [Nak07, Cor. 4.7].

Theorem 4.6. Let $( M , E _ { M } )$ be a basic pair with $M$ the minimal resolution of singularities of $a$ strictly log canonical log del Pezzo surface with boundary $( S , B )$ of index $\leq 2$ with integral $B$ , and let $\phi \colon M \to X$ be a contraction to a minimal basic pair so that $( M , E _ { M } )$ is obtained from a quasi fundamental triplet $( X , E , \Delta )$ by eliminating the 0-dimensional scheme $\Delta$ .
Then

(1) If a component $E _ { i }$ of $E$ has multiplicity $\mathit { 1 }$ then its strict preimage on M must be isomorphic to $\mathbb { P } ^ { 1 }$ and have $E _ { i } ^ { 2 } \le - 2$ .  
(2) Additionally, assume that $\Delta$ is disjoint from the singular part of $E _ { \mathrm { r e d } }$ and that for every irreducible component $E _ { i }$ of $E$ with $\mathrm { m u l t } _ { E } ( E _ { i } ) = 1$ , one has m $\mathrm { u l t } _ { P } ( \Delta \cap E _ { i } ) \leq 2$ .
Then the only connected components of $\Delta$ are the five subschemes of Def.
4.2.

Remark 4.7. Concerning the additional assumptions of (2), we note that they are satisfied for the strictly log canonical fundamental triplets by [Nak07, 4.6].
So we can ignore them in the case $g ( S , B ) \geq 2$ .

Proof.
(1) Our condition for the integrality of $B$ means that all components of $E _ { M }$ of multiplicity 1 must be contracted by $\alpha \colon M \to S$ .
They are all $\mathbb { P } ^ { 1 }$ ’s with $E _ { i } ^ { 2 } \le - 2$ .

(2) We then go through the short list of subschemes with $\mathrm { m u l t } _ { P } ( \Delta \cap E _ { i } ) \leq 2$ , eliminating those that lead to $( - 1 )$ -curves $\Gamma$ with $\mathrm { m u l t } _ { E _ { M } } ( \Gamma ) = 1$ .
For example, the case $\Delta = ( x , y ) \subset E = ( y ^ { 2 } )$ is eliminated.


Nakayama defined fundamental triplets $( X , E , \Delta )$ (without “quasi”) in order to obtain uniqueness for them, in most cases.
We pick a different normalization: we pick $( X , E )$ to correspond to one of the pure shapes and all connected components of $\Delta$ to be of type $( \prime )$ .

Theorem 4.8. Let $( S , B )$ be a log del Pezzo surface with boundary $( S , B )$ of index $\leq 2$ of genus $g ( S , B ) \ge 2$ .
Then it is one of the following shapes or is obtained from them by any allowable primings as in Theorem 3.18.

(1) $\widetilde { D } _ { 2 n }$ , $D _ { 2 n }$ , $D _ { 2 n - 1 } ^ { - }$ , $A _ { 2 n - 1 }$ , $A _ { 2 n - 2 } ^ { - }$ , $^ - A _ { 2 n - 3 } ^ { - }$ for $2 n \geq 6$ .  
(2) $\tilde { E } _ { 7 } , \ ^ { - } E _ { 7 } , \ ^ { - } E _ { 6 } ^ { - }$ .  
(3) ${ \widetilde { E } } _ { 8 } ^ { - }$ , $^ - E _ { 8 } ^ { - }$ .

Proof.
We go through the complete list [Nak07, 4.7(2)] of fundamental triplets and see that they are as above.

Case $[ n ; 2 , e ] _ { 2 }$ for $n \geq 0$ , $e \leq \operatorname* { m a x } ( 4 , n + 1 )$ with $\mathrm { m u l t } _ { \ell } F \le 2$ for any $\ell \leq F$ .
This means that $X = \mathbb { F } _ { n }$ and $E = 2 \sigma + F$ , where $F \sim e \ell$ is a sum of several fibers, each with multiplicity $\leq 2$ , and $\Delta \cap \sigma = \emptyset$ .
We have $L \sim 2 \sigma _ { \infty } + ( 4 - e ) \ell$ and $L \sigma = 4 - e$ .

If $e = 0$ then $\Delta = \emptyset$ .
This is ${ \widetilde { D } } _ { 2 n + 8 }$ , so we obtain $\widetilde { D } _ { 2 m }$ for $2 m \geq 8$

If $e = 1$ then we must have $\Delta = ( \cdots )$ , that is two disjoint copies of $( \cdot )$ contained in a fiber $F ^ { \prime }$ , or $( - ) _ { 1 }$ which is a degeneration of it.
Let us use the extended notation $[ n ; 2 , 0 ; \cdots ]$ , resp.
$[ n ; 2 , 0 ; - _ { 1 } ]$ by writing $\Delta$ at the end.
Note that we must apply $( \cdot )$ twice, otherwise $\widetilde { F }$ is a $( - 1 )$ -curve in $E _ { M }$ with multiplicity 1, which is not allowed by Theorem 4.6.

Contracting one of the $( - 1 )$ -curves back and then $F _ { i }$ , we can view this as the quasi fundamental triplet $[ n - 1 ; 2 , 0 ; \prime ]$ , which is ${ \widetilde { D } } _ { 2 n + 6 } ^ { \prime }$ .
Thus, we get ${ \widetilde { D } } _ { 2 m } ^ { \prime }$ for $2 m \geq 6$ .

In the degenerate case $\Delta = ( - ) _ { 1 }$ of $( \cdots )$ , the direction of the “prime” coincides with the direction of the fiber $\ell$ on $\mathbb { F } _ { n - 1 }$ for the triplet $[ n - 1 ; 2 , 0 ; \prime ]$ .
In that case the strict preimage of this fiber gives an extra $\left( - 2 \right)$ -curve, and the surface $Y$ acquires an extra $A _ { 1 }$ singularity outside of $B$ .

If $e = 2$ and $F = \ell _ { 1 } + \ell _ { 2 }$ then we get $[ n - 2 ; 2 , 0 ; \prime \prime ]$ this way, which is $\tilde { D } _ { 2 n + 4 } ^ { \prime \prime }$ .
Since $n \geq 1$ , we get $\widetilde { D } _ { 2 m } ^ { \prime \prime }$ for $2 m \geq 6$ .
Similarly when $e = 3 , 4$ and $F ^ { \prime }$ is the sum of $e$ distinct fibers, we get $\widetilde { D } _ { 2 m } ^ { \prime \prime \prime }$ and $\widetilde { D } _ { 2 m } ^ { \prime \prime \prime \prime }$ for $2 m \geq 6$ .
Similar to the above, for every priming the preimage of the corresponding fiber $\ell$ gives an $\left( - 2 \right)$ -curve which gives an additional singularity of $Y$ .

Now consider the case when $e = 2$ and $F = 2 \ell$ is a double fiber.
If $\Delta = \emptyset$ then this is $D _ { 2 n + 4 }$ , i.e. $D _ { 2 m }$ for $2 m \geq 6$ .
For $\Delta = - , \prime , \prime \prime , +$ we get $D _ { 2 m - 1 } ^ { - }$ , $D _ { 2 m } ^ { \prime }$ , $D _ { 2 m } ^ { \prime \prime }$ , $D _ { 2 m - 1 } ^ { + }$ for $2 m \geq 6$ .
Adding single fibers to $F$ , i.e. $F = 2 \ell + \ell _ { 1 }$ or $2 \ell + \ell _ { 1 } + \ell _ { 2 }$ , gives priming on the left side, which produces all the cases $\mathbf { \nabla } ^ { \prime } D ^ { \prime }$ and $" T D ?$ for $2 m \geq 6$ .

Finally, $e = 4$ , $F = 2 \ell _ { 1 } + 2 \ell _ { 2 }$ and $\Delta = \emptyset$ gives $A _ { 2 n - 1 }$ .
Adding $\Delta = - , \prime , \prime \prime , +$ adds corresponding decorations in the $A$ case, with each $- , +$ decreasing the index by $^ { 1 }$ .

Ca $\ L _ { 3 } e \ [ 1 ; 2 , 2 ] _ { 2 \infty } \colon Y = \mathbb { F } _ { 1 }$ , $E = 2 \sigma _ { \infty }$ , and $\Delta = \emptyset$ .
This is ${ \widetilde { D } } _ { 6 }$ .

Case [2]2 with $\mathrm { m u l t } _ { P } ( \Delta \cap \ell ) \leq 2$ for any $P \in \ell$ : $Y = \mathbb { P } ^ { 2 }$ , $E = 2 \ell$ and $L = \mathcal { O } ( 4 )$ .
For $\Delta = \emptyset$ , this is ${  { \widetilde { E } } } _ { 7 }$ .
For $\Delta = ( - )$ , resp.
$\left( -- \right)$ , this is ${ } ^ { - } E _ { 7 }$ , $^ - E _ { 6 } ^ { - }$ .
Considering various other possibilities for $\Delta$ leads to all the allowable primings of ${  { \widetilde { E } } } _ { 7 }$ , ${ } ^ { - } E _ { 7 }$ , $^ - E _ { 6 } ^ { - }$ .

Case $[ 2 ; 1 , 2 ] _ { 2 + }$ with $\mathrm { m u l t } _ { P } ( \Delta \cap \ell ) \leq 2$ for any $P \in \ell$ : $Y = \mathbb { F } _ { 2 }$ , $E = \sigma + 2 \ell$ , $\deg ( \Delta \cap \ell ) \leq 3$ and $\Delta \cap \sigma = \emptyset$ .
For $\Delta = \emptyset$ this is ${ \widetilde { E } } _ { 8 } ^ { - }$ , and for $\Delta = ( - )$ this is $^ - E _ { 8 } ^ { - }$ .
Considering various other possibilities for $\Delta$ leads to all the allowable primings of ${ \widetilde { E } } _ { 8 } ^ { - }$ and $^ - E _ { 8 } ^ { - }$ .

Case $[ 0 ; 2 , 1 ] _ { 0 }$ .
This is a typo, this is a klt case so it does not appear.

4C.
$K _ { M } + L _ { M }$ is nef and $g = 1$ .
In this case the main result of [Nak07] is (3.12) which says that $S$ must be a Gorenstein log del Pezzo surface and $2 B \sim - K _ { S }$ .
To apply it in our case, we would have to find all Gorenstein del Pezzo surfaces with Du Val singularities and $K _ { S }$ divisible by 2 as a Weil divisor – of which there are many – and then consider all the possibilities for $B$ .

Instead, we adopt a different strategy.
Let us define a weak basic pair with the same definition as a basic pair but dropping the condition (C2) that $2 g - 2 > 0$ .
Similarly, we define a weak quasi fundamental triplet $( X , E , \Delta )$ by asking that $X$ in $( \mathcal { F } 1 )$ is merely a weak minimal basic pair.
Then:

(1) It is still true that $K _ { M } + L _ { M }$ is nef for any weak basic pair obtained by eliminating a 0- dimensional scheme of a weak fundamental triple $( X , E , \Delta )$ : the corresponding proofs in [Nak07, 4.2, 3.14 nefness] go through.  
(2) We have additional conditions $K _ { M } + L _ { M } = K _ { M } + E _ { M } = 0$ by [Nak07, 3.12].  
(3) Our Theorem 4.6 still holds.  
(4) We have to check separately that $L _ { M }$ is big, this condition is no longer automatic.
However, this is easy to do: $L ^ { 2 } / 2$ drops by $\deg ( \Delta ) / 2$ , i.e. by 1 under the operations $( \prime )$ , $( - ) _ { 1 }$ , $( - )$ , and by 2 under $( \prime \prime )$ .

Lemma 4.9. The weak fundamental triplets for strictly lc pairs $( S , B )$ are:

(1) $X = \mathbb { P } ^ { 2 }$ , $E = 2 \ell _ { 1 } + \ell _ { 2 }$ .  
(2) $X = \mathbb { F } _ { 0 }$ , and (a) $E = 2 \sigma + 2 \ell$ , $( b$ ) $E = 2 \sigma + \ell _ { 1 } + \ell _ { 2 }$ , (c) $E = 2 D$ , $D \sim \sigma + \ell$ .  
(3) $X = \mathbb { F } _ { 1 }$ , and (a) $E = 2 \sigma + 2 \ell _ { 1 } + \ell _ { 2 } , ( b ) E = 2 \sigma + \ell _ { 1 } + \ell _ { 2 } + \ell _ { 3 }$ , (c) $E = \sigma + \sigma _ { \infty } + 2 \ell$ , (d) $E = 2 \sigma _ { \infty } + \ell$ .

(4) $X = \mathbb { F } _ { 2 }$ , and (a) $E = 2 \sigma + 2 \ell _ { 1 } + 2 \ell _ { 2 }$ , $( b _ { , }$ ) $E = 2 \sigma + 2 \ell _ { 1 } + \ell _ { 2 } + \ell _ { 3 }$ , (c) $E = 2 \sigma + \ell _ { 1 } + \ell _ { 2 } + \ell _ { 3 } + \ell _ { 4 }$ , (d) $E = \sigma + 2 \ell + \sigma _ { \infty }$ , (e) $E = 2 \sigma _ { \infty }$

Proof.
Immediate: $X = \mathbb { P } ^ { 2 }$ or $\mathbb { F } _ { n }$ , $L = - K _ { X }$ must be nef, and $E = - 2 K _ { X } - L$ must have at least one component of multiplicity 2. We simply list the possibilities.


Theorem 4.10. Let $( S , B )$ be a log del Pezzo surface with boundary $( S , B )$ of index $\leq 2$ of genus $g ( S , B ) = 1$ .
Then it is one of one of the shapes ${ \widetilde { D } } _ { 4 }$ , $D _ { 4 }$ , $A _ { 3 }$ , $A _ { 2 } ^ { - }$ , $^ - A _ { 1 } ^ { - }$ , or is obtained from one of them by any allowable primings as in Theorem 3.18.

Proof.
The pairs of Lemma 4.9 in which all components of $E$ have multiplicity 2 already appear in our classification: (2a) $D _ { 4 }$ , (2c) ${ \widetilde { D } } _ { 4 }$ , (4a) $A _ { 3 }$ , (4e) degenerate case of ${ \widetilde { D } } _ { 4 }$ .
Our first step is to reduce all other cases to them.

Let us begin with case (1).
The line $\ell _ { 2 }$ must be blown up at least once by Theorem $4 . 6 ( 1 )$ .
Thus, we are reduced to case (2).

Now consider for example case (2b).
The fiber $\ell _ { 1 }$ must be blown up at least once, again by (4.6)(1).
Let $\tau \colon X ^ { \prime } \to X$ be the first blowup at a point $P \in E$ and let $E _ { 0 }$ be the exceptional $( - 1 )$ -curve.
We have $K _ { X ^ { \prime } } + E ^ { \prime } = \tau ^ { * } ( K _ { X } + E ) = 0$ .
If $P = \ell _ { 1 } \cap \sigma$ then $E _ { 0 }$ appears in $E ^ { \prime }$ with coefficient 2, otherwise it appears with coefficient $0$ ; either way it is even.
Let $X ^ { \prime }  X ^ { \prime \prime }$ be the contraction of the strict preimage of $\ell _ { 1 }$ , which is a $( - 1 )$ -curve on $X ^ { \prime }$ .
We obtain another minimal model $M  X ^ { \prime \prime }$ for $M$ which has fewer components of multiplicity $1$ in $E$ .

This way, we reduce all cases to the purely even cases above except cases (3c) and (4d).
Consider now (3c).
The curve $\sigma _ { \infty }$ has to be blown up at least once.
Blowing up and contracting the strict preimage of a fiber reduces to the case (3a) which was already considered.
The case (4d) reduces to (3c) and then to (3a).

So now we are reduced to the pairs of shapes $D _ { 4 }$ , $A _ { 3 }$ , ${ \widetilde { D } } _ { 4 }$ and the pairs obtained from them by eliminating 0-dimensional subschemes $\Delta$ .
The conditions of Theorem 4.6(2) hold, so the connected components of $\Delta$ have types $( \prime )$ , $( - )$ , $( + )$ .
In the cases $D _ { 4 }$ , $A _ { 3 }$ we also have $\deg ( \Delta \cap E _ { i } ) \leq 2$ for $i = 1 , 2$ .
In all three cases, $\deg ( \Delta ) \leq 6$ by the condition $L _ { M } ^ { 2 } > 0$ .

So let us now begin with $D _ { 4 }$ and consider different possibilities for $\Delta$ .
If one or two components of $\Delta$ are $( - )$ then we get respectively $D _ { 3 } ^ { - } = A _ { 3 } ^ { \prime }$ and ${ } ^ { - } D _ { 2 } ^ { - } = { } ^ { - } A _ { 2 } ^ { \prime }$ .
If the components are $( + )$ then we get respectively $D _ { 3 } ^ { + } = A _ { 3 } ^ { \prime \prime }$ and $^ { - } D _ { 2 } ^ { + } = { ^ { \prime \prime } A } _ { 3 } ^ { - }$ .
When the components of $\Delta$ are $( \prime )$ , we get the usual primings.

For ${ \widetilde { D } } _ { 4 }$ , $\Delta = ( - )$ gives $D _ { 4 } ^ { \prime }$ and $\Delta = ( -- )$ gives $' A _ { 3 } ^ { \prime }$ , with other combinations of $( - )$ , $( + )$ , $( \prime )$ giving primings of those.
For $A _ { 3 }$ , it is easier: $\Delta = ( - )$ , $( - , - )$ , $( + )$ etc. gives the usual $A _ { 2 } ^ { - }$ , $^ - A _ { 1 } ^ { - }$ , $A _ { 2 } ^ { + }$ and adding $( \prime )$ ’s gives the usual primings.
$\boxed { \begin{array} { r l } \end{array} }$

This completes the proof of Theorem A.
We now switch back from the notation of [Nak07] to our notation $\pi \colon ( X , D + \epsilon R ) \to ( Y , C + { \frac { 1 + \epsilon } { 2 } } B )$ .

# 5. Moduli of $A D E$ pairs

5A.
Two-dimensional projections of $A D E$ lattices.
Here, we fix the notations from representation theory and prove a number of basic results that will be used in the remainder of the paper.

Notation 5.1. $\Lambda$ will denote one of the root lattices $A _ { n }$ , $D _ { n }$ , $E _ { n }$ , and $N ^ { * } \supset \Lambda$ its dual, the weight lattice.
One has $\Lambda ^ { * } = \oplus _ { i = 1 } ^ { n } \mathbb { Z } \alpha _ { i }$ and $\Lambda ^ { * } = \oplus _ { i = 1 } ^ { n } \mathbb { Z } \varpi _ { i }$ , where $\alpha _ { i }$ are the simple roots and $\varpi _ { i }$ the fundamental weights (same as fundamental coweights).
One has $\langle \alpha _ { i } , \varpi _ { j } \rangle = \sigma _ { i j }$ .

Notation 5.2. We label the nodes of the Dynkin diagrams as in Figs.
1, 2, 3. For example, for the $E _ { 8 }$ diagram we denote the nodes by $p ^ { \prime \prime }$ , $p _ { 1 } ^ { \prime }$ , $p _ { 2 } ^ { \prime }$ , $p _ { 0 } , \ldots , p _ { 4 }$ .
For the $D _ { n }$ diagram they are $p ^ { \prime \prime }$ , $p _ { 1 } ^ { \prime } = p ^ { \prime }$ , $p _ { 0 } , \ldots , p _ { n - 3 }$ .
We use the same notation to denote the roots and fundamental weights, i.e. we call them $\alpha ^ { \prime \prime }$ , $\alpha _ { 1 } ^ { \prime } = \alpha ^ { \prime }$ , etc.

In addition, for each of the polytopes $P$ in Figs.
1, 2, 3 we have the special vertex $p _ { * }$ and two vertices $p \ell , p _ { r }$ which are the end points of the left and right sides.
For example, for the $E _ { 8 }$ diagram one has $p _ { \ell } = p _ { 3 } ^ { \prime }$ and $p _ { r } = p _ { 5 }$ , and for $D _ { n }$ they are $p _ { \ell } = p _ { 2 } ^ { \prime }$ and $p _ { r } = p _ { n - 2 }$ .

Definition 5.3. We define the extended weight lattice as $\Lambda ^ { * } \oplus \mathbb { Z } ^ { 2 }$ , and we denote the basis of $\mathbb { Z } ^ { 2 }$ by $\{ \varpi _ { l } , \varpi _ { r } \}$ .

Lemma 5.4. For pure $A D E$ shapes, the rule $\varpi _ { i } \mapsto p _ { i } - p _ { * }$ defines a homomorphism

$$
\phi \colon \Lambda ^ { * } \oplus \mathbb { Z } \varpi _ { \ell } \oplus \mathbb { Z } \varpi _ { r } \stackrel { \phi } { \to } \mathbb { Z } ^ { 2 } .
$$

The projection $\pi _ { 1 } \colon \Lambda ^ { * } \oplus \mathbb { Z } \varpi _ { \ell } \oplus \mathbb { Z } \varpi _ { r } \to \Lambda ^ { * }$ identifies $\ker \phi$ with $\Lambda$ .
The homomorphism $\phi$ is surjective for $D , E$ shapes, and one has $\mathrm { c o k e r } \phi = \mathbb { Z } _ { 2 }$ for $A$ shapes.

Proof.
Any root $\alpha$ can be expressed as $\begin{array} { r } { \alpha = \sum _ { \varpi } \langle \alpha , \varpi \rangle } \end{array}$ with the sum going over the $n$ fundamental weights $\varpi$ .
In particular, if $p _ { i - 1 }$ , $p _ { i }$ , $p _ { i + 1 }$ are three consecutive nodes in a chain then

$$
\alpha _ { i } = 2 \varpi _ { i } - \varpi _ { i - 1 } - \varpi _ { i + 1 } \stackrel { \phi } { \to } 2 p _ { i } - p _ { i - 1 } - p _ { i + 1 } = 0
$$

For an end node $p _ { i }$ next to $p _ { r }$ one has

$$
\alpha _ { i } - \varpi _ { r } = 2 \varpi _ { i } - \varpi _ { i - 1 } - \varpi _ { r } \stackrel { \phi } { \to } 2 p _ { i } - p _ { i - 1 } - p _ { r } = 0
$$

and similarly for the node next to $p \ell$ .
For a node $p _ { 0 }$ occurring at a corner of the polytope, one has

$$
\alpha _ { 0 } = 2 \varpi _ { 0 } - \varpi _ { 1 } - \varpi _ { 1 } ^ { \prime } - \varpi ^ { \prime \prime } \stackrel { \phi } {  } 2 p _ { 0 } - p _ { 1 } - p _ { 1 } ^ { \prime } - p ^ { \prime \prime } + p _ { * } = 0
$$

Thus, $\Lambda = \langle \alpha \rangle \subset \ker \phi$ , and it is easy to see that the equality holds.

Recall that the finite group $\Lambda ^ { * } / \Lambda$ is $\mathbb { Z } _ { n + 1 }$ for $A _ { n }$ , $\mathbb { Z } _ { 2 } ^ { 2 }$ for $D _ { 2 n }$ , $\mathbb { Z } _ { 4 }$ for $D _ { 2 n - 1 }$ , and $\mathbb { Z } _ { 3 }$ , $\mathbb { Z } _ { 2 }$ , $0$ for $E _ { 6 }$ , $E _ { 7 }$ , $E _ { 8 }$ respectively.

Corollary 5.5. $\mathbb { Z } ^ { 2 } / \langle p _ { \ell } - p _ { * } , p _ { r } - p _ { * } \rangle$ is equal to $\Lambda ^ { * } / \Lambda$ for the pure $D$ and $E$ shapes, and $( \Lambda ^ { * } / \Lambda ) \oplus \mathbb { Z } _ { 2 }$ for the pure $A$ shapes.

Lemma 5.6. For primed $A D E$ shapes which admit a toric description (see Subsection $\it 3 D$ ) the rule $\varpi \mapsto p { - } p _ { * }$ defines a homomorphism $\phi \colon \Lambda ^ { * } \oplus \mathbb { Z } \varpi _ { \ell } \oplus \mathbb { Z } \varpi _ { r } \ { \stackrel { \phi } { \to } } \ \mathbb { Z } ^ { 2 }$ .
The projection $\pi _ { 1 } \colon \Lambda ^ { * } \oplus \mathbb { Z } \varpi _ { \ell } \oplus \mathbb { Z } \varpi _ { r } $ $\Lambda ^ { * }$ identifies $\ker \phi$ with $\Lambda \subset \Lambda ^ { \prime } \subset \Lambda ^ { * }$ given below

![](images/68a7f26bc7eeae3746339c1a2be1493791b00fc4a332b9dacdc4364648eebc51.jpg)

Proof.
For the corner node $p _ { 0 }$ in $' A _ { 2 n - 1 } , ' A _ { 2 n - 2 } ^ { - }$ one uses the corner relation (5.3) with $\varpi ^ { \prime }$ replaced by $\varpi \ell$ , and similarly for $D _ { 2 n } ^ { \prime }$ .
Additionally: for $A _ { 2 n - 1 } ^ { \prime }$ one has $\varpi _ { n } - \varpi _ { \ell } - \varpi _ { r } \stackrel { \phi } { \to } 0$ , and for $D _ { 2 n }$ one has $\begin{array} { r } { \phi ( \varpi _ { r } + \lfloor \frac { n } { 2 } \rfloor \varpi _ { \ell } ) = \phi ( \varpi ^ { \prime } ) } \end{array}$ , resp.
$= \phi ( \varpi ^ { \prime \prime } )$ .
See Fig.
8 for the node notations.
$\boxed { \begin{array} { r l } \end{array} }$

5B.
Moduli of $A D E$ pairs of pure shapes.
In this subsection we prove the first part of Theorem B.
Recall that in Section 3 we associated to each $A D E$ pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ an $A D E$ root lattice.
We use the notation introduced in Section 5A.

Definition 5.7. We define the tori $T _ { \Lambda } = \operatorname { H o m } ( \Lambda , \mathbb { C } ^ { * } )$ and $T _ { \Lambda ^ { * } } = \mathrm { H o m } ( \Lambda ^ { * } , \mathbb { C } ^ { * } )$ both isomorphic to $( \mathbb { C } ^ { * } ) ^ { n }$ .
We also define a finite multiplicative group $\mu _ { \Lambda } = \mathrm { H o m } ( \Lambda ^ { * } / \Lambda , \mathbb { C } ^ { * } )$ .
Thus, $\mu _ { \Lambda } = \mu _ { n + 1 }$ for $A _ { n }$ , $\mu _ { 2 } ^ { 2 }$ for $D _ { 2 n }$ , $\mu _ { 4 }$ for $D _ { 2 n - 1 }$ , and it is $\mu _ { 3 }$ , $\mu _ { 2 }$ , $^ { 1 }$ for $E _ { 6 }$ , $E _ { 7 }$ , $E _ { 8 }$ respectively.

Warning 5.8. The theorem below is for pairs in which we distinguish the two sides $C _ { 1 }$ and $C _ { 2 }$ .
The moduli stack for the pairs with a single $C$ is the $\mathbb { Z } _ { 2 }$ -quotient for the shapes with the left / right symmetry, and is the same for the nonsymmetric shapes.

Theorem 5.9. The moduli stack of $A D E$ pairs of a fixed pure ADE shape is

$$
\begin{array} { r l r } & { [ \mathrm { H o m } ( \Lambda ^ { * } , \mathbb { C } ) : \mu _ { \Lambda } \times \mu _ { 2 } ] = [ T _ { \Lambda } : W _ { \Lambda } \times \mu _ { 2 } ] } & { f o r ~ A ~ s h a p e s } \\ & { [ \mathrm { H o m } ( \Lambda ^ { * } , \mathbb { C } ) : \mu _ { \Lambda } ] = [ T _ { \Lambda } : W _ { \Lambda } ] } & { f o r ~ D ~ a n d ~ E ~ s h a p e s . } \end{array}
$$

Remark 5.10. The first presentation is convenient for finding automorphism groups.
In particular, the maximal automorphism group that a pair can have is $\mu _ { \Lambda } \times \mu _ { 2 }$ for $A$ shapes and $\mu _ { \Lambda }$ for $D$ and $E$ shapes.
The second form is convenient for compactifications, which in Section 6 are shown to be quotients of toric varieties by Weyl groups.

Proof.
We first note that the pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ is log canonical near the boundary $C$ iff the divisor $B$ intersects $C$ transversally.
Vice versa, with this condition satisfied the pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ for $0 < \epsilon \ll 1$ is automatically log canonical.
Otherwise, the pair $( Y , C + { \textstyle { \frac { 1 } { 2 } } } B )$ is not log canonical.
But by [Sho92, 6.9] the non-klt locus must be connected, with a single exception when it may have two components, both of them simple, i.e. on a resolution each should give a unique curve with discrepancy $^ { - 1 }$ .
For an $A D E$ surface the curve $C = C _ { 1 } + C _ { 2 }$ is connected with two irreducible components, so they are not simple.
(We thank V.V.
Shokurov for this argument.)

Each of the $A D E$ shapes is toric, and the polarized toric variety $( Y , L )$ corresponds to a lattice polytope $P$ as in Figs.
1, 2, 3. However, $C = C _ { 1 } + C _ { 2 }$ gives only part of the toric boundary.
Fixing the torus structure is equivalent to making a choice for the remainder of the torus boundary: one curve for the $A$ shapes and two curves for the $D , E$ shapes.
With this choice made $( Y , L )$ is a polarized toric surface, and the equation of $B$ is $f \in H ^ { \cup } ( Y , L ) = \oplus _ { m \in \mathbb { Z } ^ { 2 } \cap P } \mathbb { C } e ^ { m }$ , where $e ^ { ( k , l ) } = x ^ { k } y ^ { l }$ .

For the $A$ shapes the remaining toric boundary has the equation $y ^ { 2 } \in H ^ { 0 } ( Y , L )$ .
All the other choices for the toric boundary differ by the transformation $y \mapsto y + a ( x )$ .
Completing the square we can make the coefficients of the monomials $y x ^ { i }$ in $f$ all zero.
By rescaling $x \mapsto \alpha x$ , $y \mapsto \beta y$ we can put the equation $f$ in the form given in Table 5. In this table, $A _ { n } ^ { \prime }$ denotes either $A _ { n }$ or $A _ { n } ^ { - }$ depending on the parity of $n$ , and similarly for $D , E$ .

![](images/b5e11717f3eea5ee5b787ea6493acd013a7ef8a72f3ac8d2318c61dce5a89113.jpg)
Table 5. Normal forms for the equation $f = f _ { \mathrm { b d r y } } + f _ { \mathrm { d y n } }$ of divisor $B$

For the $D$ and $E$ shapes the remaining toric boundary has the equation $( x y ) ^ { 2 } \in H ^ { \cup } ( Y , L )$ .
All other choices for the toric boundary differ by the transformations $x \mapsto x + a$ , $y \mapsto y + b ( x )$ , with $\deg b ( x ) \leq \frac { 1 } { 2 } ( n - 3 )$ for $D _ { n }$ and $\deg b ( x ) \leq \frac { 1 } { 2 } ( n - 4 )$ for $E _ { n }$ ; and then rescaling $x$ and $y$ .
Using such transformations, one can put the equation $f$ in the form given in Table 5 in an essentially unique way .

The only remaining choice is the normalization of $f _ { \mathrm { b d r y } }$ , which is unique up to the action of $\mathrm { H o m } ( \mathbb { Z } ^ { 2 } / \langle p _ { \ell } - p _ { * } , p _ { r } - p _ { * } \rangle , \mathbb { C } ^ { * } )$ , equal to $\mu _ { \Lambda }$ by Corollary 5.5. The end result is a normal form, given in Table 5, which is unique up to $\mu _ { \Lambda }$ .
This gives the stack $\left[ \mathbb { A } ^ { n } : \mu _ { \Lambda } \right]$ .
Finally, in the $A$ shapes every pair has an additional $\mu _ { 2 }$ automorphism $y \mapsto - y$ .
This gives the first presentation of the moduli stack, as a $\mu _ { \Lambda } \times \mu _ { 2 }$ , resp.
$\mu _ { \Lambda }$ quotient of $\mathbb { A } ^ { n }$ .

It is a well known and easy to prove fact that the ring of invariants $\mathbb { C } [ \Lambda ^ { * } ] ^ { W _ { \Lambda } }$ is the polynomial ring $\mathbb { C } [ \chi _ { 1 } , \dots , \chi _ { n } ]$ , where $\chi _ { i } = \chi ( \varpi _ { i } )$ are the characters of the fundamental weights ([Bou05, Ch.8, §7, Thm.2]).
In other words, $T _ { \Lambda ^ { * } } / W _ { \Lambda } = \mathbb { A } ^ { n }$ , with the coordinates $\chi _ { i }$ .
The $\mu _ { \Lambda }$ -actions on $T _ { \Lambda ^ { * } }$ and $\mathbb { A } ^ { n }$ are given by the compatible $( \Lambda ^ { * } / \Lambda )$ -gradings; thus they commute with the $W$ -action.
The $\mu _ { \Lambda }$

action on $T _ { \Lambda ^ { * } }$ is free, and $T _ { \Lambda ^ { * } } / \mu _ { \Lambda } = T _ { \Lambda }$ .
Thus

$$
[ \mathbb { A } ^ { n } : \mu _ { \Lambda } ] = [ ( T _ { \Lambda ^ { * } } : W ) : \mu _ { \Lambda } ] = [ ( T _ { \Lambda ^ { * } } : \mu _ { \Lambda } ) : W ] = [ T _ { \Lambda } : W ] ,
$$

giving the second presentation.
For the $A$ shapes the additional $\mu _ { 2 }$ action commutes with both $\mu _ { \Lambda }$ and $W$ .


5C.
Moduli of $A D E$ pairs of toric primed shapes.
We state the theorem analogous to Theorem 5.9 for the primed $A D E$ shapes which admit a toric description (see Section 3D).
It can be proved analogously to the theorem above, using Lemma 5.6, or can be seen as an immediate consequence of Theorem 5.12.

Theorem 5.11. The moduli stack of $A D E$ pairs of $a$ fixed toric primed shape is

$$
[ \mathrm { H o m } ( \Lambda ^ { * } , \mathbb { C } ) : \mu _ { \Lambda ^ { \prime } } ] = [ T _ { \Lambda ^ { \prime } } : W _ { \Lambda } ] , \quad w h e r e \ T _ { \Lambda ^ { \prime } } = \mathrm { H o m } ( \Lambda ^ { \prime } , \mathbb { C } ^ { * } ) ,
$$

$\mu _ { \Lambda ^ { \prime } } = \mathrm { H o m } ( \Lambda ^ { * } / \Lambda ^ { \prime } , \mathbb { C } ^ { * } )$ , and the lattice $\Lambda \subset \Lambda ^ { \prime } \subset \Lambda ^ { * }$ is given in Lemma 5.6.

5D.
Moduli of $A D E$ pairs of all primed shapes.
In this subsection we find the moduli stack for all primed shapes, including those which do not admit a toric description, and in doing so complete the proof of Theorem B.
We still mark the sides as left and right, even if some or all of the boundary curves are contracted.

Theorem 5.12. The moduli stack of pairs of a fixed primed shape is

$$
[ \mathrm { H o m } ( \Lambda ^ { * } , \mathbb { C } ) : \mu _ { \Lambda ^ { \prime } } \times W _ { 0 } ] = [ T _ { \Lambda ^ { \prime } } : W _ { \Lambda } \times W _ { 0 } ] .
$$

where $\mu _ { \Lambda ^ { \prime } } = \mathrm { H o m } ( \Lambda ^ { * } / \Lambda ^ { \prime } , \mathbb { C } ^ { * } )$ and the lattice $\Lambda \subset \Lambda ^ { \prime } \subset \Lambda ^ { * }$ is as follows:

$$
\begin{array} { l l } { { } } & { { \begin{array} { l l l l } { { s h a p e } } & { { \Lambda ^ { \prime } / \Lambda } } & { { g e n e r a t o r s } } \\ { { A _ { 2 n - 1 } , ^ { \prime } A _ { 2 n - 2 } ^ { - } } } & { { 0 } } & { { g } } \end{array} } } \\ { { \begin{array} { l l l } { { { \cal A } _ { 2 n - 1 } ^ { \prime } } } & { { { \mathbb { Z } } _ { 2 } } } & { { \varpi _ { n } } } \\ { { D _ { 2 n } ^ { \prime } f o r n ~ e v e n , ~ r e s p . ~ o d d } } & { { { \mathbb { Z } } _ { 2 } } } & { { \varpi ^ { \prime } ~ r e s p . ~ \varpi ^ { \prime \prime } } } \\ { { { \cal D } _ { 2 n } , ~ r e s p . ~ { \cal T } _ { 2 n - 1 } ^ { - } } } & { { { \mathbb { Z } } _ { 2 } } } & { { \varpi _ { 2 n - 3 } , ~ r e s p . ~ \varpi _ { 2 n - 4 } } } \\ { { { \cal D } _ { 2 n } ^ { \prime } f o r n ~ e v e n , ~ r e s p . ~ o d d } } & { { { \mathbb { Z } } _ { 2 } \times { \mathbb { Z } } _ { 2 } } } & { { \varpi _ { 2 n - 3 } , \varpi ^ { \prime } , ~ r e s p . ~ \varpi _ { 2 n - 3 } , \varpi ^ { \prime \prime } } } \end{array} } } \\ { { \begin{array} { l } { { - { \cal E } _ { 7 } ^ { \prime } } } & { { { \mathbb { Z } } _ { 2 } } } \end{array} } } & { { { \mathbb { Z } } _ { 2 } } } \end{array}
$$

For shapes $^ { \prime \prime } S$ and $S ^ { \prime \prime }$ the lattices $\Lambda ^ { \prime }$ are the same as for the unprimed shape $S$ , and similarly for $^ + S$ resp.
$S ^ { + }$ and the unprimed shapes $^ - S$ resp.
$S ^ { - }$ .
The additional Weyl group $W _ { 0 }$ is the one given in Theorem 3.32, and its action is described in Theorem 5.13.

Proof.
The pair $\begin{array} { r l } { ( \overline { { Y } } ^ { \prime } , \overline { { C } } _ { 1 } ^ { \prime } + \overline { { C } } _ { 2 } ^ { \prime } + \frac { 1 + \epsilon } { 2 } \overline { { B } } ^ { \prime } ) } & { { } } \end{array}$ is obtained from a pair $\begin{array} { r l } { ( Y , C _ { 1 } + C _ { 2 } + \frac { 1 + \epsilon } { 2 } B ) } \end{array}$ of pure shape by blowing up several points $P _ { i } \in B \cap C$ at the ideals $I _ { i }$ with directions equal to the tangent directions of $B$ , and then contracting by the semiample line bundle $L ^ { \prime }$ .
This construction works for the entire family over $\mathbb { A } ^ { n } = \mathrm { H o m } ( \Lambda ^ { * } , \mathbb { C } )$ : we blow up sections and it is easy to see that the sheaf $\mathcal { L } ^ { \prime }$ in the family is relatively semiample.

When priming on a short side, or priming twice on a long side, there are no choices for $\prod I _ { i }$ .
The only 2:1 choice is when there is a long side $C _ { s }$ and we prime only at one of the two points in $B \cap C _ { s }$ .
Secondly, as stated in Theorem 3.32, for some shapes of genus 1 there is more than one precursor.
These choices define an additional quotient by $W _ { 0 }$ .

5E.
Definitions of the naive $A D E$ families.
For the toric $A D E$ shapes $A$ , $A$ , $D$ and $E$ we define explicit modular families of $A D E$ pairs over the torus $T _ { \Lambda ^ { * } }$ .
We call these the naive families.
Blowing up the sections corresponding to the points in $C \cap B$ , we obtain the naive families for all the primed $A D E$ shapes.

For the $A _ { n } ^ { \prime }$ -shapes, where $A _ { n } ^ { \because }$ is either $A _ { n }$ or $A _ { n } ^ { - }$ depending upon the parity of $n$ , we take the equation of Table 5 with $c _ { i } = \chi _ { i } = \chi ( \varpi _ { i } )$ , the characters of the fundamental weights, and with $y ^ { 2 }$ rescaled to $- \bigl ( \frac { y } { 2 } \bigr ) ^ { 2 }$ , which will be convenient when we come to discuss degenerations.

We recall that the $A _ { n }$ root lattice is $\langle e _ { i } - e _ { j } \rangle \subset \mathbb { Z } ^ { n + 1 }$ and the dual weight lattice is $A _ { n } ^ { * } = \langle f _ { i } \rangle$ , where $f _ { i } = e _ { i } - p$ , $\begin{array} { r } { p = \frac { 1 } { n + 1 } \sum e _ { i } } \end{array}$ , so that $\textstyle \sum _ { i = 1 } ^ { n + 1 } f _ { i } = 0$ .
Thus, $\mathbb { C } [ \Lambda ^ { * } ] = \mathbb { C } [ t _ { 1 } ^ { \pm } , \dots , t _ { n + 1 } ^ { \pm } ] / ( \prod t _ { k } - 1 )$ and $\mathbb { C } [ \Lambda ] = \mathbb { C } [ t _ { i } / t _ { j } ]$ , with $t _ { i } = e ^ { f _ { i } }$ .
The first torus is $T _ { \Lambda ^ { * } } = \{ \prod t _ { i } = 1 \} \subset ( \mathbb { C } ^ { * } ) ^ { n + 1 }$ , and the second one is $T _ { \Lambda } = ( \mathbb { C } ^ { * } ) ^ { n + 1 } / \operatorname { d i a g } \mathbb { C } ^ { * }$ .
One has $T _ { \Lambda } = T _ { \Lambda ^ { * } } / \mu _ { n + 1 }$ .

The Weyl group is $S _ { n + 1 }$ , and the characters of the fundamental weights are the symmetric polynomials $\chi _ { i } = \sigma _ { i } ( t _ { k } )$ .
Therefore, the defining equation of the naive family is

$$
A _ { n } ^ { ? } : \ f = - \left( { \frac { y } { 2 } } \right) ^ { 2 } + \prod _ { i = 1 } ^ { n + 1 } ( x + t _ { i } ) = - \left( { \frac { y } { 2 } } \right) ^ { 2 } + 1 + \chi _ { 1 } x + \dots \chi _ { n } x ^ { n } + x ^ { n + 1 } .
$$

For ${ \mathrm { - } } A _ { n } ^ { \prime }$ shapes we number the nodes $\cdot \ldots , n + 1$ (cf.
Fig.

1. and the equation is as follows, where $\chi _ { k } = \sigma _ { i - 1 } ( t _ { i } )$ :

$$
\exists _ { n } ^ { ? } : f = - \left( { \frac { y } { 2 } } \right) ^ { 2 } + x \prod _ { i = 1 } ^ { n + 1 } ( x + t _ { i } ) = - \left( { \frac { y } { 2 } } \right) ^ { 2 } + x \left( 1 + \chi _ { 2 } x + \dots \chi _ { n + 1 } x ^ { n } + x ^ { n + 1 } \right) .
$$

For the toric shapes with one corner, i.e. $D _ { n } ^ { \prime }$ , ${ } ^ { - } E _ { n } ^ { \prime }$ and ${ \bf \ddot { A } } _ { n } ^ { \prime }$ (here again the ? is either no decoration or a $-$ , depending upon the parity), we make the following change of coordinates.
We begin with the affine equation of a double cover $X  Y$ of the form

$$
F ( x , y , z ) = - x y z + z ^ { 2 } + c ^ { \prime \prime } z + p ( x ) + q ( y ) = 0 .
$$

Introducing the variable $\begin{array} { r } { w = z - \frac { 1 } { 2 } ( x y - c ^ { \prime \prime } ) } \end{array}$ , the equation becomes

$$
w ^ { 2 } + f ( x , y ) = 0 , \qquad f ( x , y ) = - \left( { \frac { x y - c ^ { \prime \prime } } { 2 } } \right) ^ { 2 } + p ( x ) + q ( y )
$$

with the same $p ( x )$ , $q ( y )$ .
Thus, the affine equation of the branch curve $B$ is $f ( x , y )$ , which we accept as our main equation.
Explicitly, the families are:

$$
\begin{array} { l l l } { { } } & { { } } & { { { \displaystyle f = - \left( \frac { x y - c ^ { \prime \prime } } { 2 } \right) ^ { 2 } + y + c _ { 0 } + c _ { 1 } x + \cdot \cdot \cdot + c _ { n - 2 } x ^ { n - 2 } + x ^ { n - 1 } } } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle D _ { n } ^ { 2 } : } } &  { { \displaystyle f = - \left( \frac { x y - c ^ { \prime \prime } } { 2 } \right) ^ { 2 } + y ^ { 2 } + c _ { 1 } ^ { \prime } y + c _ { 0 } + c _ { 1 } x + \cdot \cdot \cdot + c _ { n - 3 } x ^ { n - 3 } + x ^ { n - 2 } } } \\ { { } } & { { } } & { { - E _ { n } ^ { 2 } : } } \\ { { } } & { { } } &  { { \displaystyle f = - \left( \frac { x y - c ^ { \prime \prime } } { 2 } \right) ^ { 2 } + y ^ { 3 } + c _ { 2 } ^ { \prime } y ^ { 2 } + c _ { 1 } ^ { \prime } y + c _ { 0 } + \cdot \cdot \cdot + c _ { n - 4 } x ^ { n - 4 } + x ^ { n - 3 } } } \end{array}
$$

In all of these families we take the coefficients to be $c = \chi ( \varpi )$ , the fundamental characters, i.e. the characters of the fundamental weights corresponding to the $n$ nodes of the Dynkin diagram, using our Notation 5.2.

5F.
Action of the extra Weyl group $W _ { 0 }$ .
When a pure shaped precursor is not uniquely determined, as in Theorem 3.32, there is an additional Weyl group $W _ { 0 }$ acting on the pure shape moduli torus $T _ { \Lambda ^ { \prime } }$ .
We divide by it in Theorem 5.12.

Theorem 5.13. The Weyl group $W _ { 0 }$ of Theorem 3.32 acts on $T _ { \Lambda ^ { \prime } }$ as follows:

(1) Genus $> 1$ .
For $\mathbf { \Delta } ^ { \prime } D _ { 2 n } ^ { \prime }$ and $\mathbf { \mathit { { D } } _ { 2 n - 1 } ^ { \prime } }$ shapes, $W _ { 0 } = W ( A _ { 1 } ) = S _ { 2 }$ acts by an automorphism of the $D$ -lattice switching the two short legs $p ^ { \prime }$ and $p ^ { \prime \prime }$ .
For $^ { \prime \prime } D _ { 2 n } ^ { \prime }$ and $^ { \prime \prime } D _ { 2 n - 1 } ^ { \prime }$ shapes, one has $W _ { 0 } = W ( A _ { 1 } ^ { 2 } ) = S _ { 2 } ^ { 2 }$ .
The first $S _ { 2 }$ acts by switching the two short legs $p ^ { \prime }$ and $p ^ { \prime \prime }$ .
The second $S _ { 2 }$ gives an additional $S _ { 2 }$ automorphism of the pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ .  
(2) Genus 1. For the following shapes the action is as in (1) under the identifications: ${ \mathrm { ^ { \prime } } } A _ { 3 } ^ { \prime } =$ ${ \mathrm { \mathit { D } } } _ { 3 } ^ { - }$ , $\mathit { A } _ { 3 } ^ { \prime \prime } = \mathit { \prime \prime } \mathit { D } _ { 3 } ^ { - }$ , $D _ { 4 } ^ { \prime } = \mathrm { { \Delta } } ^ { \prime } D _ { 4 }$ , $D _ { 4 } ^ { \prime \prime } \ = \ ^ { \prime \prime } D _ { 4 }$ .
For ${ \cal { D } } _ { 4 } ^ { \prime }$ the group $W _ { 0 } = W ( A _ { 2 } ) = S _ { 3 }$ acts by permuting the three legs of the $D _ { 4 }$ diagram.
For $\mathcal { D } _ { 4 } ^ { \prime \prime }$ , one has $W _ { 0 } = W ( A _ { 3 } ) = S _ { 4 } = S _ { 3 } \ltimes S _ { 2 } ^ { 2 }$ .
Here, $S _ { 3 }$ acts by permuting the legs and $S _ { 2 } ^ { 2 }$ gives an extra automorphism group of the pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ .

Proof.
(1) From the equation (5.7) of the $D$ -family we see that the side $C _ { 1 }$ is defined by $( y _ { 0 } : y _ { 1 } ) =$ $( 0 : 1 )$ , where $\begin{array} { r } { y \ = \ \frac { y _ { 1 } } { y _ { 0 } } } \end{array}$ .
There are two points $x = \pm 2$ on $C _ { 1 }$ at which one can prime.
For $x = 2$ , consider the map $\begin{array} { r } { \varphi _ { + } \colon y \mapsto \frac { c ^ { \prime \prime } + c ^ { \prime } } { x - 2 } - y } \end{array}$ , $x \mapsto x$ .
It is easy to check that the equation (5.7) maps to the same equation but with $c ^ { \prime }$ and $c ^ { \prime \prime }$ switched.
The map is a rational map for a surface of $D ^ { ? }$ shape $\varphi _ { + }$ but it becomes regular on the blowup, a surface of $\mathbf { \nabla } ^ { \prime } D ^ { \prime }$ shape.
Similarly, for priming at $x = - 2$ the map $\varphi _ { - } \colon y \mapsto \frac { c ^ { \prime \prime } - c ^ { \prime } } { x + 2 } + y$ works the same way.
The composition $\begin{array} { r } { \varphi _ { - } \circ \varphi _ { + } \colon y \mapsto \frac { c ^ { \prime \prime } - c ^ { \prime } } { x + 2 } + \frac { c ^ { \prime \prime } + c ^ { \prime } } { x - 2 } - y } \end{array}$ , $x \mapsto x$ exchanges the two branches of the curve $B$ , a two-section of the $\mathbb { P } ^ { 1 }$ -fibration.
For surfaces $Y$ of $D ^ { ? }$ and $\mathbf { \nabla } ^ { \prime } D ^ { \prime }$ shapes this is a rational involution.
It becomes a regular involution of a surface of $^ { \prime \prime } D ^ { \prime }$ shape, where $B$ is disconnected from $C _ { 1 }$ .
Case (2) is checked similarly.


Definition 5.14. Let $W _ { 0 0 } \subset W _ { 0 }$ be the subgroup which acts trivially on the the points of $T _ { \Lambda ^ { \prime } }$ , giving extra automorphisms of the pairs.

Corollary 5.15. The group $W _ { 0 } / W _ { 0 0 }$ acts by diagram automorphisms of the decorated Dynkin diagram, permuting the short legs, all of them white circled vertices: for $\mathbf { \Delta } ^ { \prime } D _ { 2 n } ^ { \prime }$ , $\mathbf { \mathcal { D } } _ { 2 n - 1 } ^ { \prime }$ , $'  { D _ { 2 n } ^ { \prime } }$ , $^ { \prime \prime } D _ { 2 n - 1 } ^ { \prime }$ ${ \mathrm { \mathit { A } } } _ { 3 } ^ { \prime }$ , ${ \bf { \mathit { A } } } _ { 3 } ^ { \prime \prime }$ it is two legs, and for ${ \cal { D } } _ { 4 } ^ { \prime }$ , $\mathcal { D } _ { 4 } ^ { \prime \prime }$ three legs, cf.
Fig.
6.

# 6. Compactifications of moduli of $A D E$ pairs

6A.
Stable pairs in general and stable $A D E$ pairs.
We recall some standard definitions from the theory of moduli of stable pairs.
We note in particular a close relationship between the contents of this subsection and work of Hacking [Hac04a, Hac04b], who studied similar ideas in the context of moduli of plane curves.

Definition 6.1. A pair $\left( X , B = \sum b _ { i } B _ { i } \right)$ consisting of a reduced variety and a $\mathbb { Q }$ -divisor is semi log canonical (slc) if $X$ is $S _ { 2 }$ , has at worst double crossings in codimension 1, and for the normalization $\nu \colon X ^ { \nu } \to X$ writing

$$
\nu ^ { * } ( K _ { X } + B ) = K _ { X ^ { \nu } } + B ^ { \nu } ,
$$

the pair $( X ^ { \nu } , B ^ { \nu } )$ is log canonical.
Here $B ^ { \nu } = D + \textstyle \sum b _ { i } \nu ^ { - 1 } ( B _ { i } )$ and $D$ is the double locus.

Definition 6.2. A pair $( X , B )$ consisting of a connected projective variety $X$ and a $\mathbb { Q }$ -divisor $B$ is stable if

(1) $( X , B )$ has slc singularities, in particular $K _ { X } + B$ is $\mathbb { Q }$ -Cartier.  
(2) The $\mathbb { Q }$ -divisor $K _ { X } + B$ is ample.

Next we introduce the objects that we are interested in here: We could work equivalently with the pairs $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ or with their double covers $( X , D + \epsilon R )$ .
We choose the former.

Definition 6.3. For a fixed degree $e \in \mathbb { N }$ a fixed rational number $0 < \epsilon \leq 1$ , a stable del Pezzo pair of type $( e , \epsilon )$ is a pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ such that

(1) $2 ( K _ { X } + C ) + B \sim 0$ (2) The divisor $B$ is an ample Cartier divisor of degree $\boldsymbol { B } ^ { 2 } = \boldsymbol { e }$ .
(3) $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ is stable in the sense of Definition 6.2.

Definition 6.4. A family of stable del Pezzo pairs of type $( e , \epsilon )$ is a flat morphism $f \colon ( \mathcal { V } , \mathcal { C } + \textstyle \frac { 1 + \epsilon } { 2 } \mathcal { B } ) $ $S$ such that $( \omega _ { y / S } ^ { \otimes 2 } ( \mathcal { C } ) ^ { * * } \simeq \mathcal { O } _ { Y }$ locally on $S$ , the divisor $\boldsymbol { \beta }$ is a relative Cartier divisor, such that every fiber is a stable del Pezzo pair of type $( e , \epsilon )$ .
We will denote by $\mathcal { M } _ { \mathrm { d p } } ^ { \mathrm { s l c } } ( e , \epsilon )$ its moduli stack.

Proposition 6.5. For a fixed degree $e$ there exists an $\epsilon _ { 0 } ( e ) > 0$ such that for any $0 < \epsilon \le \epsilon _ { 0 }$ the moduli stacks $\mathcal { M } ^ { \mathrm { s l c } } ( e , \epsilon _ { 0 } )$ and $\mathcal { M } ^ { \mathrm { s l c } } ( e , \epsilon )$ coincide.
The stack $\mathcal { M } ^ { \mathrm { s l c } } ( e , \epsilon _ { 0 } )$ is a Deligne-Mumford stack of finite type with a coarse moduli space $M ^ { \mathrm { s l c } } ( e , \epsilon _ { 0 } )$ which is a separated algebraic space.

Proof.
For a fixed surface $Y$ , there exists an $0 < \epsilon _ { 0 } \ll 1$ such that the pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ is slc iff $B$ does not contain any centers of log canonical singularities of $( Y , C + { \textstyle { \frac { 1 } { 2 } } } B )$ : images of the divisors with codiscrepancy of such centers.
Th $b _ { i } = 1$ on a any solution o, the pair $Z \to Y ^ { \nu } \to Y$ finitely many is.
Now since $\epsilon < \epsilon _ { 0 }$ $\begin{array} { r } { ( Y , C + \frac { 1 + \epsilon _ { 0 } } { 2 } B ) } \end{array}$ $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ is ample Cartier of a fixed degree, the family of the pairs is bounded, and the number $\epsilon _ { \mathrm { 0 } }$ with this property can be chosen universally.

We refer to [KSB88, Kol15], [Ale06] for the existence and projectivity of the moduli space of stable pairs $( X , \sum b _ { i } B _ { i } )$ .
There are complications arising in the construction when some coefficients $b _ { i } \leq \frac { 1 } { 2 }$ and when the divisor $B$ is not $\mathbb { Q }$ -Cartier, all of which are not present in this situation.
$\boxed { \begin{array} { r l } \end{array} }$

Definition 6.6. For a fixed $A D E$ shape, we denote by $M _ { A D E } ^ { \mathrm { s l c } }$ the closure of the moduli space of $A D E$ pairs of this shape in $M _ { \mathrm { d P } } ^ { \mathrm { s l c } } ( e , \epsilon _ { 0 } )$ for $e = B ^ { 2 }$ , with the reduced scheme structure.

In this Section will show that $M _ { A D E } ^ { \mathrm { s l c } }$ is proper and that in fact the stable limits of $A D E$ pairs are of a very special kind: they are stable pairs.
We will also show that the normalization of $M _ { A D E } ^ { \mathrm { s l c } }$ is an explicit projective toric variety for a generalized Coxeter fan.

Definition 6.7. A stable $A D E$ pair is a stable del Pezzo pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ ) such that its normalization is a union of $A D E$ pairs $\begin{array} { r } { \sqcup ( Y _ { k } ^ { \nu } , C _ { k } ^ { \nu } + \frac { 1 + \epsilon } { 2 } B _ { k } ^ { \nu } ) } \end{array}$ .

Theorem 6.8. For a stable $A D E$ pair the irreducible components are of two kinds:

(1) normal, i.e. $\nu \colon Y _ { k } ^ { \nu } \xrightarrow { \sim } Y _ { k }$ , or  
(2) folded: the morphism $\nu \colon Y _ { k } ^ { \nu }  Y _ { k }$ is an isomorphism outside of $C _ { k }$ , and is a double cover $\mathbb { P } ^ { 1 } \to \mathbb { P } ^ { 1 }$ k on one or two sides $C _ { k , s } ^ { \nu } \to C _ { k , s }$ , $s = 1 , 2$ .
In this case, the side $C _ { k , s } ^ { \nu }$ is necessarily a long side of the $A D E$ pair.

Proof.
The normalization of a stable pair is an isomorphism outside of the double locus and is 2:1 on the double locus, so these are the two possibilities.
The side must be long because $\nu ^ { * } B _ { k } \cdot C _ { k , s } ^ { \nu } =$ $2 B _ { k } \cdot C _ { k , s }$ is even and $\geq 2$ .


Definition 6.9. We will calldenote a fold by adding the $f$ he surfaces of type (2) in the above theorem the folsuperscript to the corresponding long side, e.g. $A _ { 2 n - 1 } ^ { f }$ a, $\boldsymbol { \mathrm { \mathit { 1 } } } _ { A _ { 2 n - 1 } ^ { f } } ^ { f }$ $- _ { A _ { 2 n } ^ { f } }$ , $\boldsymbol { \mathrm { \mathit { A } } } _ { 2 n - 1 } ^ { f }$ .
We define the decorated Dynkin diagrams for these shapes by double circling the corresponding end (unfilled) node.
We do not draw any pictures for these here.

Next, we extend the naive families of $A D E$ pairs, defined in section $\mathrm { 5 E }$ , to families of stable pairs over a projective toric variety corresponding to the Coxeter fan.
We start with the $A _ { n }$ case.

6B.
Compactifications of the naive families for the $A$ shapes.
Recall that ${ \cal T } _ { \Lambda ^ { * } } = \mathrm { S p e c } \mathbb { C } | \Lambda ^ { * } |$ .
We define the following elements of the homogeneous ring $\mathbb { C } [ \Lambda ^ { * } ] [ x , y ] [ \xi ]$ , with the grading defined by $\deg \xi = 1$ .

Definition 6.10. In the $A _ { n } ^ { \prime }$ shape, where the ? denotes either no decoration or a $-$ depending upon the parity of $n$ , for each node $p _ { 1 } , \ldots , p _ { n }$ of the Dynkin diagram we introduce a degree 2 element $u _ { i } = e ^ { \varpi _ { i } } x ^ { i } \cdot \xi ^ { 2 }$ , where $e ^ { \varpi _ { i } } \in \mathbb { C } [ \Lambda ^ { * } ]$ is the monomial corresponding to the fundamental weight $\varpi _ { i } \in \Lambda ^ { * }$ .
In addition, we introduce the degree 2 elements $u _ { 0 } = 1 \cdot \xi ^ { 2 }$ and $u _ { n + 1 } = x ^ { n + 1 } \cdot \xi ^ { 2 }$ , corresponding to the left and right nodes $p _ { l } = p _ { 0 }$ and $p _ { r } = p _ { n + 1 }$ , and $u _ { * } = y ^ { 2 } \cdot \xi ^ { 2 }$ corresponding to the vertex $p _ { * }$ .
Similarly, in the ${ \mathrm { - } } A _ { n } ^ { \prime }$ shape we define the elements $u _ { 1 } , \ldots , u _ { n + 2 }$ and $u _ { * }$ .

Because even the simplest $A D E$ surface of $A _ { 0 } ^ { - }$ -shape is a weighted projective space $\mathbb { P } ( 1 , 1 , 2 )$ , it is convenient to introduce some square roots.

Definition 6.11. For the even nodes $p _ { 2 i }$ we introduce the degree 1 elements of the ring $R [ \xi ]$ $v _ { 2 i } = e ^ { \varpi _ { 2 i } / 2 } x ^ { i } \cdot \xi$ and $v _ { * } = y \cdot \xi$ .
Thus, $v _ { 2 i } ^ { 2 } = u _ { 2 i }$ and $v _ { * } ^ { 2 } = u _ { * }$ .

We recall that in the naive families (5.4), (5.5) we take the coefficients $c _ { i } = \chi _ { i }$ , the fundamental characters.
As in Section 5A, let $\alpha _ { i }$ be the simple roots.

Definition 6.12. Set $a _ { i } = e ^ { - \alpha _ { i } }$ for all $i$ , and for odd indices set $b _ { 2 i + 1 } = e ^ { - \alpha _ { 2 i + 1 } / 2 }$ .
Finally, define normalized coefficients $\widehat { c } _ { i } = e ^ { - \varpi _ { i } } c _ { i }$ .

It is well known that for any dominant weight $\lambda \in \Lambda ^ { * }$ the character $\chi ( \lambda ) \in \mathbb { C } [ \Lambda ^ { * } ]$ is a $W _ { \Lambda }$ -invariant Laurent polynomial whose highest weight is $\lambda$ and the other weights are of the form $\mu = \lambda - \textstyle \sum n _ { i } \alpha _ { i }$ for some $n _ { i } \geq 0$ .
Thus, $\widehat { c } _ { k }$ are polynomials in $a _ { i }$ ’s, and $\widehat { c } _ { k } = 1 +$ (higher terms in $a _ { i }$ ).

bWith these notations, we consider the equation $f$ bof the naive family (5.4) to be the following homogeneous degree 2 element in $\mathbb { C } [ \Lambda ^ { * } ] [ x , y ] [ \xi ]$ (similarly for ${ \mathrm { - } } A _ { n } ^ { \prime }$ ):

$$
f = - \left( \frac { v _ { * } } { 2 } \right) ^ { 2 } + u _ { 0 } + \widehat { c } _ { 1 } u _ { 1 } + \ldots + \widehat { c } _ { n } u _ { n } + u _ { n + 1 } \in \mathbb { C } [ \Lambda ^ { * } ] [ x , y ] \cdot \xi ^ { 2 }
$$

For the construction of the family one might as well work with the ring $\mathbb { C } [ \frac { 1 } { 2 } \Lambda ^ { * } ]$ but we will use the minimal choice for clarity.

Definition 6.13. Let $M$ be the lattice obtained by adjoining to $\Lambda ^ { * }$ the vectors $\varpi _ { 2 i } / 2$ and $\alpha _ { 2 i + 1 } / 2$ for all $_ i$ .
Let $M ^ { + } = M \cap \sum \mathbb { R } _ { \geq 0 } { \bigl ( } - \alpha _ { i } { \bigr ) }$ and $R = \mathbb { C } [ M ^ { + } ]$ .
Thus, Spec $R$ is a normal affine toric variety which is a $\mu _ { 2 } ^ { N }$ -cover of $\mathbb { A } ^ { n } = \operatorname { S p e c } \mathbb { C } [ a _ { i } ]$ for some $N$ .

Definition 6.14 (Compactified naive families for the $A _ { n } ^ { \because }$ , $-  { \boldsymbol { A } } _ { n } ^ { \because }$ shapes).
Let $S$ be the graded subring of $R [ x , y ] [ \xi ]$ generated by $v _ { 2 i }$ , $u _ { 2 i + 1 }$ , and $v _ { * }$ .
The compactified naive family is $y : = \operatorname { P r o j } S \to \operatorname { S p e c } R$ with a relative Cartier divisor $\boldsymbol { B } = \boldsymbol { \left( f \right) }$ , $f \in H ^ { 0 } ( { \mathcal { O } } ( 2 ) )$ .
We note that since the subring $S ^ { ( 2 ) }$ is generated in degree 1, the sheaf $\mathcal { O } _ { \mathrm { P r o j } S } ( 2 )$ is invertible and ample.

Example 6.15. For the $A _ { 1 }$ shape, the $A _ { 1 }$ root lattice has $\mathbb { C } [ \Lambda ^ { * } ] = \mathbb { C } [ t _ { 1 } ^ { \pm } , t _ { 2 } ^ { \pm } ] / ( t _ { 1 } t _ { 2 } - 1 ) \cong \mathbb { C } [ t ^ { \pm } ]$ , with $t = e ^ { \alpha _ { 1 } / 2 }$ .
The family is ${ \mathrm { P r o j ~ } } S \to { \mathbb { A } } ^ { 1 } = { \mathrm { S p e c } } \mathbb { C } [ b _ { 1 } ]$ , where $S = R [ v _ { * } , v _ { 0 } , u _ { 1 } , v _ { 1 } ] / ( v _ { 0 } v _ { 2 } - b _ { 1 } u _ { 1 } )$ .
One has $\chi _ { 1 } = t + t ^ { - 1 } = t ( 1 + b _ { 1 } ^ { 2 } )$ , and the equation of the divisor $\boldsymbol { \beta }$ is

$$
f = - \left( \frac { v _ { * } } { 2 } \right) ^ { 2 } + v _ { 0 } ^ { 2 } + ( 1 + b _ { 1 } ^ { 2 } ) u _ { 1 } + v _ { 2 } ^ { 2 } .
$$

Setting $b _ { 1 } = 0$ gives the degenerate fiber $\mathbb { P } ( 1 , 1 , 2 ) \cup \mathbb { P } ( 1 , 1 , 2 )$ with the coordinates $v _ { * } , v _ { 0 } , u _ { 1 }$ , resp.
$v _ { * } , v _ { 2 } , u _ { 1 }$ , glued along a $\mathbb { P } ^ { 1 }$ with the coordinate $u _ { 1 }$ .
The restriction of $f$ to $\mathbb { P } ( v _ { * } , v _ { 0 } , u _ { 1 } )$ is $v _ { * } ^ { 2 } + v _ { 0 } ^ { 2 } + u _ { 1 }$ , and for $\mathbb { P } ( v _ { * } , v _ { 2 } , u _ { 1 } )$ it is $v _ { * } ^ { 2 } + v _ { 2 } ^ { 2 } + u _ { 1 }$ .
Thus, the degenerate fiber is a union of two $A D E$ pairs $A _ { 0 } ^ { - } \bar { A } _ { 0 }$ glued along a short side.

For the $\overline { { A } } _ { 1 } ^ { - }$ shape the family is $\operatorname { P r o j } S \to \mathbb { A } ^ { 1 } = \operatorname { S p e c } \mathbb { C } [ a _ { 1 } ]$ , where $S = R [ u _ { 1 } , v _ { 2 } , u _ { 3 } ] / ( u _ { 1 } u _ { 3 } - a _ { 1 } v _ { 2 } ^ { 4 } )$ , and the equation of the divisor is

$$
f = - \left( \frac { v _ { * } } { 2 } \right) ^ { 2 } + u _ { 1 } + ( 1 + a _ { 2 } ) v _ { 2 } ^ { 2 } + u _ { 2 } .
$$

Setting $a _ { 1 } = 0$ gives the degenerate fiber $\mathbb { P } ( 1 , 1 , 2 ) \cup \mathbb { P } ( 1 , 1 , 2 )$ with the coordinates $v _ { * } , v _ { 2 } , u _ { 1 }$ , resp.
$v _ { * } , v _ { 2 } , u _ { 3 }$ , which is the union of two $A D E$ pairs $\overline { { A } } _ { 0 } A _ { 0 } ^ { - }$ glued along a long side, a $\mathbb { P } ^ { 1 }$ with the coordinate $v _ { 2 }$ .

The general case is essentially a generalization of this simple example.
The degenerations of pairs for the slightly more complicated $A _ { 2 } ^ { - }$ shape are illustrated in Fig.
12.

![](images/11fab3407652a0a81ccb9ec61619cd417310d7a0fbfc04c2d0b1a9c0edf97463.jpg)  
Figure 12. $A _ { 2 } ^ { - }$ and its degenerations: $A _ { 0 } ^ { - } \bar { A } _ { 1 } ^ { - }$ , $A _ { 1 } A _ { 0 } ^ { - }$ , and $A _ { 0 } ^ { - } \bar { A } _ { 0 } A _ { 0 } ^ { - }$

Definition 6.16. The Coxeter fan for a root lattice $\Lambda$ is the fan on $\Lambda _ { \mathbb { R } } = \Lambda _ { \mathbb { R } } ^ { * }$ obtained by cutting this vector space by the mirrors $\alpha ^ { \perp }$ to the roots $\alpha$ .
Its maximal cones are chambers, the translates of the positive chamber under the action of the Weyl group $W _ { \Lambda }$ .
We denote by $V _ { M } ^ { \mathrm { { c o x } } }$ the torus embedding of $T _ { M } = \operatorname { H o m } ( M , \mathbb { C } ^ { * } )$ for the Coxeter fan of $A _ { n }$ .

Lemma 6.17. The following relations hold:

(2) (Secondary) (1) (Primary) $v _ { 2 i } v _ { 2 i + 2 } = b _ { 2 i + 1 } u _ { 2 i + 1 }$ $u _ { 2 i - 1 } u _ { 2 j + 1 } = v _ { 2 i } ^ { 2 } v _ { 2 j } ^ { 2 } \cdot A$ and , $v _ { 2 i - 2 } u _ { 2 j + 1 } = v _ { 2 i } v _ { 2 j } ^ { 2 } \cdot b _ { 2 i - 1 } A$ $u _ { 2 i - 1 } u _ { 2 i + 1 } = a _ { 2 i } v _ { 2 i } ^ { 4 }$ .
, and v2i−2v2j+2 = v2iv2j · $b _ { 2 i - 1 } b _ { 2 j + 1 } A$ , where $\textstyle A = \prod _ { k = 2 i } ^ { 2 j } a _ { k }$ .

Proof.
An easy direct check using equations (5.1), (5.2).

Theorem 6.18. The compactified family $y = \operatorname { P r o j } S \to \operatorname { S p e c } R$ of shape $A _ { n } ^ { ? }$ or ${ \mathbf { } } ^ { - } A _ { n } ^ { ? }$ is flat.
The degenerate fibers are over the subsets given by setting some $a _ { i }$ ’s to zero.
Every fiber of this family is a stable $A D E$ pair which is a union of $A D E$ pairs of shapes obtained by subdividing the $A _ { n } ^ { ? }$ , resp.
${ \mathrm { \overline { { \mathbf { A } } } } } _ { n } ^ { ? }$ , polytope into integral subpolytopes of smaller $A$ shapes by intervals from the vertex $p _ { * }$ to the points $p _ { i }$ for which one has $a _ { i } = 0$ .

The $W _ { \Lambda }$ -translates of this family glue into a flat $W _ { \Lambda }$ -invariant family $\begin{array} { r } { ( \mathcal { V } , \mathcal { C } + \frac { 1 + \epsilon } { 2 } \mathcal { B } ) \to V _ { M } ^ { \mathrm { c o x } } } \end{array}$ of stable $A D E$ pairs.

Proof.
Let $t \in { \mathrm { S p e c } } R$ be a closed point and $\mathcal { V } _ { t }$ be a fiber over $t$ .
Suppose that some $a _ { k } ( t ) = 0$ or $b _ { k } ( t ) = 0$ .
The relations of Lemma 6.17 imply that any two ( $u$ or $v$ ) variables with indices $i < k$ and $j > k$ multiply to give zero.
On the other hand, the product of two variables with indices $i , j$ for which the coordinates with $i < k < j$ satisfy $a _ { k } ( t ) , b _ { k } ( t ) \neq 0$ , is a nonzero monomial.

Let $P$ be the polytope corresponding to the shape $A _ { n } ^ { \prime }$ , resp.
${ \mathrm { - } } A _ { n } ^ { \prime }$ .
The above equations define a stable toric variety $Z = \cup Z _ { s }$ for the polyhedral decomposition $P = \cup P _ { s }$ obtained by cutting $P$ by the intervals from the vertex $p _ { * }$ to the points $p _ { k }$ for each $k$ with $a _ { k } = 0$ or $b _ { k } = 0$ , cf.
[Ale02].
In other words, $Z$ is a reduced seminormal variety which is a union of projective toric varieties, glued along torus orbits.

The fiber $\mathcal { V } _ { t }$ is a closed subscheme of $Z$ .
But the Hilbert polynomial of $Z$ with respect to $\mathcal { O } ( 2 )$ is the same as for a general fiber, a projective toric variety for the polytope $P$ .
By the semicontinuity of Hilbert polynomials in families, $\mathscr { D } _ { t } = Z$ .
Since the base $T _ { \Lambda ^ { * } }$ is reduced, the constancy of the Hilbert polynomial implies that the family is flat.

The equation $f$ restricts on each irreducible component to the naive equation of an $A D E$ pair for a smaller $A$ shape by Lemma 6.19.

The $W _ { \Lambda }$ -translates of this family automatically glue into a $W _ { \Lambda }$ -invariant family over a torus embedding of $T _ { M }$ for the Coxeter fan of $A _ { n }$ because the $u , v$ variables map to the corresponding variables for a different choice of positive roots, and the equation $f$ is $W$ -invariant.
Flatness is a local condition, so it holds.


Lemma 6.19. Let $\Lambda$ be a an irreducible $A D E$ root lattice with Dynkin diagram $\Delta$ and Weyl group $W = \langle w _ { \alpha } \mid \alpha \in \Delta \rangle$ .
Let $\beta \in \Delta$ be a simple root, and $\Lambda ^ { \prime }$ be the lattice (not necessarily irreducible) corresponding to $\Delta ^ { \prime } = \Delta \setminus \beta$ , with Weyl group $W ^ { \prime } = \langle w _ { \alpha } \mid \alpha \neq \beta \rangle$ .
Let $r$ be the natural restriction homomorphism

$$
r \colon k [ e ^ { - \alpha } , \alpha \in \Delta ] \to k [ e ^ { - \alpha } , \alpha \in \Delta ^ { \prime } ] , \qquad e ^ { - \beta } \mapsto 0 , \quad e ^ { - \alpha } \mapsto e ^ { - \alpha } f o r \alpha \neq \beta .
$$

Then for the normalized fundamental character $\widehat { \chi } _ { \alpha } = e ^ { - \varpi _ { \alpha } } \chi _ { \alpha }$ corresponding to a simple root $\alpha$ one has

$$
r ( \widehat { \chi } _ { \alpha } ) = \left\{ \begin{array} { l l } { { 1 } } & { { f o r \alpha = \beta } } \\ { { \widehat { \chi } _ { \alpha } } } & { { f o r \alpha \neq \beta } } \end{array} \right.
$$

Proof.
Consider a dominant weight $\mu \in \Lambda ^ { * }$ .
We first make an elementary observation about the weight diagram of the highest weight representation $V ( \mu )$ .
The weight diagram is obtained by starting with the highest weight $\mu = \sum m _ { k } \varpi _ { k }$ and subtracting simple roots $\alpha _ { s }$ if the corresponding

coordinate $m _ { s }$ of $\mu$ is positive.
Thus, for $\mu = \varpi _ { \beta }$ the first and only move down is to the weight $\mu - \beta$ .
This says that $\widehat { \chi } ( \varpi _ { \beta } ) = 1 + e ^ { - \beta } ( \dots )$ .
Therefore, $r ( \widehat { \chi } ( \varpi _ { \beta } ) ) = 1$ .

For $\alpha \neq \beta$ b, the moves down in the weight diagram of $V ( \varpi _ { \alpha } )$ not involving $\beta$ are the same as the moves in the Dynkin diagram $\Delta \setminus \beta$ .
So the monomials appearing in $r \big ( \widehat { \chi } ( \varpi _ { \alpha } ) \big )$ for the Dynkin diagram $\Delta$ and the monomials appearing in $\widehat { \chi } ( \varpi _ { \alpha } )$ for the Dynkin diagram $\Delta \setminus \beta$ are the same.

bWe have to show that the coefficients of these monomials are also the same.
This follows from the Weyl character formula

$$
\chi ( \lambda ) = \frac { \sum _ { w \in W } \varepsilon ( w ) e ^ { w ( \lambda + \rho ) } } { \sum _ { w \in W } \varepsilon ( w ) e ^ { w ( \rho ) } } , \quad \mathrm { w h e r e ~ } \rho = \sum _ { \varpi \in \Pi } \varpi .
$$

Isolating the terms $e ^ { \mu }$ on the top and the bottom where the linear function $( \beta , \mu )$ takes the maximum, and setting other terms to zero gives the same Weyl Character formula expression for the Weyl group $W ^ { \prime }$ .
This concludes the proof.


Remark 6.20. The construction of the family of curve pairs over the Losev-Manin space for $A _ { n }$ follows from this by an easy simplification: the two-dimensional polytope is replaced by $[ 0 , n + 1 ]$ and there are only $u _ { i }$ variables, all of degree 1.

6C.
Compactifications of the naive families for the A0 , $D$ , $^ - E$ shapes.
Before stating the general result, we begin with an elementary example.

![](images/f509d0e9e086b785cb104d5e4ffa16b50c827e246341350e6c997380cdef13ac.jpg)  
Figure 13. $D _ { 4 }$ and its degenerations $A _ { 0 } ^ { - } A _ { 3 }$ , $A _ { 1 } A _ { 1 }$ , $A _ { 3 } ^ { \prime } \bar { A } _ { 0 }$ , $A _ { 3 }$

Example 6.21. An $A D E$ surface $Y , C = C _ { 1 } + C _ { 2 } )$ of shape $D _ { 4 }$ is $Y = \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ , with $C _ { 1 } = s$ , $C _ { 2 } = f$ a section and a fiber.
In an $A D E$ pair $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ , the divisor $B$ is in the linear system $| 2 s + 2 f |$ .
There are three obvious toric degenerations corresponding to removing the nodes $p _ { 1 } ^ { \prime }$ , $p _ { 0 }$ , $p _ { 1 }$ in the Dynkin diagram, shown in the middle three pictures of Figure 13. In the degeneration corresponding to $p _ { 1 } ^ { \prime }$ we get a 3-dimensional family of stable $A D E$ pairs with two components corresponding to $A _ { 0 } ^ { - } A _ { 3 }$ .
By symmetry, we get $A _ { 3 } ^ { \prime } \ { \overline { { A } } } _ { 0 }$ surfaces for the node $p _ { 1 }$ .

The toric degeneration for the node $p _ { 0 }$ is already somewhat unusual.
Here $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ degenerates to $\mathbb { P } ^ { 2 } \cup \mathbb { P } ^ { 2 }$ , and the stable $A D E$ pairs of shape $A _ { 1 } A _ { 1 }$ form only a 2-dimensional family, so some moduli are lost.

Additionally, there is an obvious nontoric degeneration of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ to a quadratic cone $\mathbb { P } ( 1 , 1 , 2 )$ , with the limits of $C _ { 1 } , C _ { 2 }$ passing through the vertex, and $B$ a double section.
These are pairs of shape $A _ { 3 }$ forming a 3-dimensional family.

Definition 6.22. In the $\mathbf { \ddot { A } } _ { n } ^ { \prime }$ , $D _ { n } ^ { \prime }$ , ${ } ^ { - } E _ { n } ^ { \prime }$ shapes, where ? denotes either no decoration or a $-$ depending upon the parity of $n$ , we introduce the following elements of the homogeneous ring $\mathbb { C } [ \Lambda ^ { * } ] [ x , y ] [ \xi ]$ :

$$
u _ { i } = e ^ { \varpi _ { i } } x ^ { i } \cdot \xi ^ { 2 } , \quad v _ { 2 i } = e ^ { \varpi _ { 2 i } / 2 } x ^ { i } \cdot \xi , \quad u _ { i } ^ { \prime } = e ^ { \varpi _ { i } ^ { \prime } } y ^ { i } \cdot \xi ^ { 2 } , \quad v _ { 2 i } ^ { \prime } = e ^ { \varpi _ { 2 i } ^ { \prime } / 2 } y ^ { i } \cdot \xi .
$$

We also have the $u$ variables for the left and right sides $p \ell$ , $p _ { r }$ and, when these are even, their square roots, the $\boldsymbol { v }$ variables.
Additionally, we define a special non-monomial variable $v _ { * } = ( x y - c ^ { \prime \prime } ) \cdot \xi$ of degree 1.

As before, the coefficients $c = \chi ( \varpi )$ are the characters of the fundamental weights, and we define the normalized characters by $\widehat { c } = e ^ { - \varpi } c$ .
With these notations, the naive families (5.6), (5.7), (5.8) become

$$
\begin{array} { l l l } { { \displaystyle { \mathcal { A } _ { n } ^ { \prime } : } } } & { { f = - \left( \frac { v _ { * } } { 2 } \right) ^ { 2 } + u _ { 1 } ^ { \prime } + \widehat { c } _ { 0 } u _ { 0 } + \widehat { c } _ { 1 } u _ { 1 } + \dots + \widehat { c } _ { n - 2 } u _ { n - 2 } + u _ { n - 1 } } } \\ { { \displaystyle { D _ { n } ^ { \prime } : } } } & { { f = - \left( \frac { v _ { * } } { 2 } \right) ^ { 2 } + u _ { 2 } ^ { \prime } + \widehat { c } _ { 1 } ^ { \prime } u _ { 1 } ^ { \prime } + \widehat { c } _ { 0 } u _ { 0 } + \widehat { c } _ { 1 } u _ { 1 } + \dots + \widehat { c } _ { n - 3 } u _ { n - 3 } + u _ { n - 2 } } } \\ { { \displaystyle { - E _ { n } ^ { 2 } : } } } & { { f = - \left( \frac { v _ { * } } { 2 } \right) ^ { 2 } + u _ { 3 } ^ { \prime } + \widehat { c } _ { 2 } ^ { \prime } u _ { 2 } ^ { \prime } + \widehat { c } _ { 1 } ^ { \prime } u _ { 1 } ^ { \prime } + \widehat { c } _ { 0 } u _ { 0 } + \dots + \widehat { c } _ { n - 4 } u _ { n - 4 } + u _ { n - 3 } } } \end{array}
$$

Definition 6.23. Let $M$ be the lattice obtained by adjoining to $\Lambda ^ { * }$ the vectors $\varpi _ { 2 i } / 2$ , $\varpi _ { 2 i } ^ { \prime } / 2$ $\alpha _ { 2 i + 1 } / 2$ (for all $_ i$ ), and $\alpha ^ { \prime \prime } / 2$ .
Let $\begin{array} { r } { M ^ { + } = M \cap \sum _ { \alpha } \mathbb { R } _ { \ge 0 } ( - \alpha ) } \end{array}$ and $R = \mathbb { C } [ M ^ { + } ]$ .

We define $a _ { i } = e ^ { - \alpha _ { i } }$ , resp.
$a _ { i } ^ { \prime } = e ^ { - \alpha _ { i } ^ { \prime } }$ , for each node $p _ { i }$ in the Dynkin diagram, and also $a ^ { \prime \prime } = e ^ { - \alpha ^ { \prime \prime } }$ .
For the odd nodes $p _ { 2 i + 1 }$ we define $b _ { 2 i + 1 } = e ^ { - \alpha _ { 2 i + 1 } / 2 }$ , resp.
$b _ { 2 i + 1 } ^ { \prime } = e ^ { - \alpha _ { 2 i + 1 } ^ { \prime } / 2 }$ , and also $b ^ { \prime \prime } = e ^ { - \alpha ^ { \prime \prime } / 2 }$

Definition 6.24 (Compactified naive families for the $A , D , E$ shapes).
Let $S$ be the graded subring of $R [ x , y ] [ \xi ]$ generated by $v _ { 2 i }$ , $u _ { 2 i + 1 }$ , $v _ { 2 i } ^ { \prime }$ , $u _ { 2 i + 1 } ^ { \prime }$ , and $v _ { * }$ .
The compactified naive family is $\mathcal { V } : =$ $\mathrm { P r o j } S  \mathrm { S p e c } R$ with a relative Cartier divisor $\boldsymbol { B } = \left( \boldsymbol { f } \right)$ , $f \in H ^ { \mathrm { 0 } } ( { \mathcal { O } } ( 2 ) )$ .
We note that since the subring $S ^ { ( 2 ) }$ is generated in degree 1, the sheaf $\mathcal { O } _ { \mathrm { P r o j } S } ( 2 )$ is invertible and ample.

Lemma 6.25. The following relations hold:

(1) The same monomial relations as in Lemma 6.17 for the variables $u _ { i } , v _ { i }$ , with $i \geq 0$ , and for the variables $u _ { i } ^ { \prime }$ , $\boldsymbol { v } _ { i } ^ { \prime }$ , $v _ { 0 }$ .  
(2) A non-monomial “corner” relation $u _ { 1 } u _ { 1 } ^ { \prime } = a _ { 0 } v _ { 0 } ^ { 3 } ( \widehat { c } ^ { \prime \prime } v _ { 0 } + b ^ { \prime \prime } v _ { * } )$ .  
(3) For each equations as in Lemma 6.17, but with A = bc00v0+b00v∗ $u _ { i } ^ { \prime } , v _ { i } ^ { \prime }$ variable and each $u _ { i } , v _ { i }$ $\begin{array} { r } { A = \frac { \widehat { c } ^ { \prime \prime } v _ { 0 } + b ^ { \prime \prime } v _ { * } } { v _ { 0 } } \prod _ { k = 2 i } ^ { 2 j } a _ { k } } \end{array}$ bvariable lying on the different sides of .
$v _ { 0 }$ , the same

roof.
We check the non-monomial relation.
The LHS is $e ^ { \varpi _ { 1 } + \varpi _ { ^ { 1 } } ^ { \prime } } x y \cdot \xi ^ { 4 }$ .
The RHS:

$$
e ^ { - \alpha _ { 0 } + { \frac { 3 } { 2 } } \varpi _ { 0 } } ( e ^ { - \varpi ^ { \prime \prime } + { \frac { 1 } { 2 } } \varpi _ { 0 } } c ^ { \prime \prime } + e ^ { - { \frac { 1 } { 2 } } \alpha ^ { \prime \prime } } x y - e ^ { - { \frac { 1 } { 2 } } \alpha ^ { \prime \prime } } c ^ { \prime \prime } ) \cdot \xi ^ { 4 }
$$

The equality now follows from $\begin{array} { r } { - \varpi ^ { \prime \prime } + \frac { 1 } { 2 } \varpi ^ { \prime \prime } = - \frac { 1 } { 2 } \alpha ^ { \prime \prime } } \end{array}$ and $- \alpha _ { 0 } + { \textstyle { \frac { 3 } { 2 } } } \varpi _ { 0 } - { \textstyle { \frac { 1 } { 2 } } } \alpha ^ { \prime \prime } = \varpi _ { 1 } + \varpi _ { 1 } ^ { \prime }$ , which hold because $\alpha ^ { \prime \prime } = 2 \varpi ^ { \prime \prime } - \varpi _ { 0 }$ and $\alpha _ { 0 } = 2 \varpi _ { 0 } - \varpi _ { 1 } - \varpi _ { 1 } ^ { \prime } - \varpi ^ { \prime \prime }$ .
The proof of part (3) is formally the same as for the secondary monomial relations, with each term $\widehat { c } ^ { \prime \prime } v _ { 0 } + b ^ { \prime \prime } v _ { * }$ contributing an extra $x y$ .
$\boxed { \begin{array} { r l } \end{array} }$

Theorem 6.26. The compactified families $y = \operatorname { P r o j } S \to \operatorname { S p e c } R$ of ${ \bf \ddot { A } } _ { n } ^ { ? }$ , $D _ { n } ^ { \prime }$ , $^ - E _ { n } ^ { ? }$ shapes are flat.
The degenerate fibers are over the subsets given by setting some a’s to zero.
Every fiber is a stable $A D E$ pair which is a union of $A D E$ pairs of shapes obtained as follows:

(1) For the degenerations $a _ { i } = 0$ and $a _ { i } ^ { \prime } = 0$ : by subdividing the corresponding polytope into integral subpolytopes by intervals from the vertex $p _ { * }$ to the point $p _ { i }$ , resp.
$p _ { i } ^ { \prime }$ .  
(2) For the degeneration $a ^ { \prime \prime } = 0$ : by “straightening the corner”, i.e. to the shape obtained by removing the node $p ^ { \prime \prime }$ from the Dynkin diagram.

The $W$ -translates of these families glue into flat $W _ { \Lambda }$ -invariant families $\mathbf { ( ) } \mathbf { , } \mathcal { C } + \frac { 1 + \epsilon } { 2 } \mathbf {  { B } } ) \to V _ { M } ^ { \mathrm { c o x } }$ of stable $A D E$ pairs over a torus embedding of $T _ { M } = \mathrm { H o m } ( M , \mathbb { C } ^ { * } )$ for the Coxeter fan of $A _ { n }$ , resp.
$D _ { n }$ , resp.
$E _ { n }$ .

Proof.
The proof for the toric degenerations is the same as in Theorem 6.18. Gluing the family over Spec $R$ to a $W$ -invariant family over a projective toric variety for the Coxeter fan is also the same.
We do not repeat these parts.
Instead, we concentrate on the degenerations involving the corner relation (2) of Lemma 6.25.

When $a _ { 0 } = 0$ we get the toric relation $u _ { 1 } u _ { 1 } ^ { \prime } = 0$ which as before gives a stable $A D E$ pair for the subdivision of our polytope into two polytopes obtained by cutting it from $p _ { * }$ to $p _ { 0 }$ into the shapes $\because A _ { m ^ { \prime } } A _ { m } ^ { \prime }$ .
The only observation here is that $m + m ^ { \prime } = n - 2$ , not $n - 1$ , so the moduli count drops by two, not one.

When $b ^ { \prime \prime } = 0$ , we also get $\widehat { c } ^ { \prime \prime } = 1$ by Lemma 6.19, and the corner relation becomes $u _ { 1 } u _ { 1 } ^ { \prime } = a _ { 0 } v _ { 0 } ^ { 4 }$ .
bThus, the new set of relations is equivalent to those for the $\mathrm { \ddot { A } } _ { n - 1 } ^ { \mathrm { \prime } }$ shape.
The equations (6.2), (6.3), (6.4) reduce to the equation (6.1).


6D.
Compactifications of the naive families for all primed shapes.
Theorems 6.18, 6.26 describe all stable $A D E$ pairs that appear as degenerations of $A D E$ pairs of pure shapes.
In particular, irreducible components of degenerate pairs $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ are normal, and they are $A D E$ pairs for smaller shapes.
For some degenerations of pairs of primed shapes the folded shapes of Definition 6.9 appear.

Definition 6.27. The Priming Rules are $A _ { 1 } ^ { \prime }  A _ { 0 } ^ { - }$ , ${ \cal { A } } _ { 1 }  { \cal { - } } { \cal { A } } _ { 0 }$ ; $\mathrm { \bar { \Delta } A _ { 0 } ^ { \prime } }  0$ , $\boldsymbol { { A } } _ { 0 } ^ { - } \to 0$ ; and $A _ { 0 } ^ { + }  f$ , $^ { + } { \cal A } _ { 0 }  f$ are folds applied to the neighboring surface.

8. or each primed shape, therr the a torus embedding of at family of stable for the Coxeter fa $A D E$ airs , re $( \mathcal { V } , \mathcal { C } \mathrm { ~ + ~ }$ $\textstyle { \frac { 1 + \epsilon } { 2 } } { \boldsymbol { B } } ) \to V _ { M } ^ { \cos }$ $\mathrm { H o m } ( M , \mathbb { C } ^ { * } )$ $A _ { n }$ $D _ { n }$ resp.
   $E _ { n }$ , where $M$ is the lattice defined in (6.13) for the $A$ $D , E$ shapes.
   The fibers over the toric strata of $V _ { M } ^ { \mathrm { { c o x } } }$ are computed by starting with the fibers of the family for the pure shape and then applying the Priming Rules one prime at a time.

Example 6.29. We list the degenerate fibers in the compactified families for the pure shape $A _ { 2 } ^ { - }$ (see Fig.
12) and the corresponding fibers in the families for the primed shapes $' A _ { 2 } ^ { - }$ , $" \boldsymbol { A } _ { 2 } ^ { - }$ , $A _ { 2 } ^ { + }$ .

![](images/7a87cb8b815c5710d9ab85fc2ca6a48afecc360530d915ec993a23da2c0b28d5.jpg)

Before proving the theorem, we explain the meaning of the Priming Rules.

Lemma 6.30. One has the following:

(1) Priming a surface of shape $A _ { 1 }$ gives a surface of shape $A _ { 0 } ^ { - }$ .  
(2) Priming a surface $Y$ of shape ${ \overline { { \mathbf { A } } } } _ { 0 }$ on the long side $C _ { 2 }$ gives a surface $Y ^ { \prime }$ and a nef line bundle $L ^ { \prime }$ such that $( L ^ { \prime } ) ^ { 2 } = 0$ and $| L ^ { \prime } |$ contracts $Y ^ { \prime }$ to $\mathbb { P } ^ { 1 }$ , with the other side $C _ { 1 }$ mapping isomorphically to $\mathbb { P } ^ { 1 }$ .  
(3) Priming a surface $Y$ of shape ${ \overline { { A } } } _ { 0 }$ on the short side $C _ { 1 }$ gives a surface $Y ^ { \prime }$ and a nef line bundle $L ^ { \prime }$ such that $( L ^ { \prime } ) ^ { 2 } = 0$ and $| L ^ { \prime } |$ contracts $Y ^ { \prime }$ to $\mathbb { P } ^ { 1 }$ , with the other side $C _ { 2 }$ folding 2:1 to $\mathbb { P } ^ { 1 }$ .

Proof.
We proved in (1) in Theorem 3.18 already, see also Remark 3.20. Parts (2,3) are easy computations.


Proof of Thm.
6.28. Let $f \colon ( \mathcal { V } , \mathcal { C } + \textstyle \frac { 1 + \epsilon } { 2 } \mathcal { B } ) \to \mathit { V } _ { M } ^ { \mathrm { c o x } }$ be a family for a pure shape.
It comes with canonical sections: one for a short side of the shape, and two disjoint sections for a long side.
Now make a weighted blow up one of the sections to obtain a family $f ^ { \prime } \colon ( \mathcal { V } ^ { \prime } , \mathcal { C } ^ { \prime } + \textstyle \frac { 1 + \epsilon } { 2 } \mathcal { B } ^ { \prime } ) \to V _ { M } ^ { \mathrm { c o x } }$ .
Then the sheaf $\mathcal { L } ^ { \prime } = \mathcal { O } _ { 3 ^ { \prime } } ( - 2 ( K _ { 3 ^ { \prime } / Z } + C ^ { \prime } )$ is invertible and relatively nef.
As in proof of Theorem 3.18, this sheaf is relatively semiample and gives a contraction $\mathcal { V } ^ { \prime }  \overline { { \mathcal { V } ^ { \prime } } }$ to a family $\bar { f } ^ { \prime } \colon ( \overline { { \mathcal { V } ^ { \prime } } } , \overline { { \mathcal { C } ^ { \prime } } } + \textstyle \frac { 1 + \epsilon } { 2 } \overline { { \mathcal { B } ^ { \prime } } } ) \to V _ { M } ^ { \mathrm { c o x } }$ over the same base.
For a reducible fiber $Y ^ { \prime } = \cup Y _ { k } ^ { \prime }$ of the family $f ^ { \prime }$ , the sheaf $\mathcal { L } ^ { \prime }$ is ample on all components $Y _ { k } ^ { \prime }$ except possibly on the blown up surface on the end.
For this surface the resulting surface $\overline { { Y } } _ { k } ^ { \prime }$ is given by Lemma 6.30. The other sections of $\mathcal { V } \to \ V _ { M } ^ { \mathrm { c o x } }$ map to disjoint sections of $\overline { { \mathcal { V } ^ { \prime } } } \to V _ { M } ^ { \mathrm { c o x } }$ .
We then repeat the process for the second prime, etc. 

Remark 6.31. Theorem 6.28 extends to the degenerations of surfaces of shapes with folds, e.g. $A _ { 2 n - 1 } ^ { f }$ as follows: the degenerations are the same as for the shape with a long side, but that long side is folded.

6E.
A generalized Coxeter fan.
As Examples 6.21 and 6.29 show, the families $( \mathcal { V } , \mathcal { C } + \textstyle \frac { 1 + \epsilon } { 2 } \mathcal { B } ) \to$ $V _ { M } ^ { \mathrm { { c o x } } }$ 2over the projective toric variety for the Coxeter fan have repeating fibers over certain boundary strata.
Here we define a coarser generalized Coxeter fan and a birational contraction $\rho \colon V _ { M } ^ { \mathrm { c o x } }  V _ { M } ^ { \mathrm { s e m } }$ such that the families are constant on the fibers of $\rho$ and such that the correspondence between the isomorphism classes of the pairs $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ and the points of $V _ { M } ^ { \mathrm { s e m i } }$ is finite to one.

The Coxeter fan $\tau ^ { \mathrm { c o x } }$ on the vector space $N _ { \mathbb { R } } = \Lambda _ { \mathbb { R } } = \Lambda _ { \mathbb { R } } ^ { * }$ is obtained by cutting it with the mirror hyperplanes $\alpha ^ { \perp }$ for the roots $\alpha \in \Lambda$ .
Another definition is: it is the normal fan to the permutahedron, $\operatorname { C o n v } ( W _ { \Lambda \cdot p } )$ , the convex hull of the $W _ { \Lambda }$ -orbit of a generic point $p$ in the interior of the positive chamber $C ^ { + } = \{ \alpha \geq 0 \}$ , where $\Delta = \{ \alpha \}$ are the simple roots.
In particular, the maximal cones of the Coxeter fan are in a bijection with the vertices of $\operatorname { C o n v } ( W _ { \Lambda } . p )$ and with the elements of the Weyl group $W = W _ { \Lambda }$ .

Definition 6.32. For a proper subset $\Delta ^ { 0 } \subset \Delta$ of the simple roots, let $p \in C ^ { + }$ be a point such that $\alpha \cdot p = 0$ for $\alpha \in \Delta ^ { 0 }$ and $\alpha \cdot p > 0$ for $\alpha \in \Delta \setminus \Delta ^ { \mathrm { 0 } }$ .
A generalized permutahedron is the convex hull $\operatorname { C o n v } ( W _ { \Lambda \cdot p } )$ and a generalized Coxeter fan $\tau ^ { \mathrm { s e m 1 } }$ is defined to be its normal fan.

Definition 6.33. We will call $\Delta ^ { 0 }$ the irrelevant subset.
For $S \subset \Delta$ we define its relevant content $S ^ { \mathrm { r e l } }$ to be the union of the connected components not lying in $\Delta ^ { 0 }$ .
We will call a connected component $S ^ { \prime }$ of $S \subset \Delta$ irrelevant if $S ^ { \prime } \subset \Delta ^ { 0 }$ .

The proof of the following lemma is straightforward.

Lemma 6.34. (1) The $W$ -orbits of cones of $\tau ^ { \mathrm { c o x } }$ are in bijection with the subsets $S \subset \Delta$ via: $S \mapsto \operatorname { C o n v } ( W _ { S } . p )$ , where $W _ { S } \subset W _ { \Lambda }$ is the Weyl subgroup generated by the simple roots $\alpha \in S$ .
(2) The $W$ -orbits of cones of $\tau ^ { \mathrm { c o x } }$ are in bijection with the subsets without irrelevant connected components.
(3) The fan $\tau ^ { \mathrm { s e m i } }$ is a coarsening of the fan $\tau ^ { \mathrm { c o x } }$ and the morphism $\rho \colon V ^ { \mathrm { c o x } }  V ^ { \mathrm { s e m } }$ of the corresponding projective toric varieties is proper and birational.
(4) The image of a torus orbit $O _ { S } ~ \subset ~ V ^ { \mathrm { c o x } }$ is $O _ { S ^ { \mathrm { { r e l } } } } \subset V ^ { \mathrm { { s e m 1 } } }$ .
One has $\dim O _ { S } \ = \ | S |$ and $\dim O _ { S ^ { \mathrm { r e l } } } = | S ^ { \mathrm { r e l } } |$ .
If $S$ has no irrelevant components the morphism $\begin{array} { l l l } { O _ { S } } & { { \stackrel { \sim } { \to } } } & { O _ { S ^ { \mathrm { r e l } } } } \end{array}$ is an isomorphism.

Definition 6.35. For a decorated Dynkin diagram of a (possibly primed) shape, we define the irrelevant subset $\Delta ^ { 0 } \subset \Delta$ to be the set of circled white (i.e. unfilled) nodes.

Example 6.36. In the pure $D , ~ E$ shapes, and also in the toric $A$ shape, the interior circled white node is irrelevant, see Figs.
2, 3, 7. In the toric shapes $D ^ { \prime }$ and $A ^ { \prime }$ the irrelevant subset consists of two nodes, see Fig.
8. In the primed shapes there may be more irrelevant nodes, cf.
Fig 6.

Theorem 6.37. The pairs in the family $\mathbf { ( ) } \mathbf { , } \mathcal { C } + \frac { 1 + \epsilon } { 2 } \mathbf {  { B } } ) \to V _ { M } ^ { \mathrm { c o x } }$ are isomorphic on each fiber of the contraction $\rho \colon V _ { M } ^ { \mathrm { c o x } }  V _ { M } ^ { \mathrm { s e m i } }$ 2 .
The correspondence between the points of $V _ { M } ^ { \mathrm { s e m i } }$ and the isomorphism M M classes of the pairs (Y, C + 1+2 B) is finite to one.

Proof.
Consider a codimension 1 orbit of $V _ { M } ^ { \mathrm { c o x } }$ corresponding to setting $a = e ^ { - \alpha }$ to zero for a single node of the Dynkin diagram $p$ .
By Theorems 6.26 and 6.28 the dimension of the family over the boundary stratum drops by 2 instead of the expected 1 exactly when one of the following happens:

(1) In the $A$ , $D$ , $E$ shapes, we remove the corner node $p _ { 0 }$ , leaving the circled white node $p ^ { \prime \prime }$ isolated.  
(2) A single left-most or right-most white node which in our shape is primed or doubly primed (so white and circled) becomes an isolated $A _ { 1 } ^ { \prime }$ or $\boldsymbol { \mathrm { { \mathit { A } } _ { 1 } } }$ after a node next to it is removed.

In both cases this happens precisely when the subdiagram $S = \Delta - p$ corresponding to the codimension 1 orbit of $V _ { M } ^ { \mathrm { { c o x } } }$ has an irrelevant component, a single node.

We now observe that for any shape the irrelevant subset consists of several disjoint isolated nodes.
There is a drop in the moduli count by one for each of them.
On the other hand, for the orbits $O _ { S }$ for $S$ without irrelevant components, the restriction of the family to $O _ { S }$ is the naive family for the Dynkin diagram $S$ .
The set of the isomorphism classes in the latter family is $O _ { S }$ modulo a finite Weyl group $W _ { S } \rtimes W _ { 0 }$ and a finite multiplicative group $\mu _ { S }$ .
This proves the statement.


6F.
Description of the compactified moduli space of $A D E$ pairs.
We now prove Theorem C.
In fact we will prove the following slightly stronger result, which contains more information about the toric primed shapes.

Theorem 6.38. For each $A D E$ shape the moduli space $M _ { A D E } ^ { \mathrm { s l c } }$ is proper and the stable limit of $A D E$ pairs are stable $A D E$ pairs.

(1) For the pure $A D E$ shapes, the normalization $( M _ { A D E } ^ { \mathrm { s l c } } ) ^ { \nu }$ is $V _ { \Lambda } ^ { \mathrm { s e m } _ { 1 } } / W _ { \Lambda }$ , $a$ $W _ { \Lambda }$ -quotient of the projective toric variety for the generalized Coxeter fan.  
(2) For the toric primed shapes ${ \mathrm { \Delta } } A _ { 2 n - 1 }$ , $\mathrm { \mathrm { ~ \cal ~ A ~ } } _ { 2 n - 2 } ^ { - }$ , $A _ { 2 n - 1 } ^ { \prime }$ , $D _ { 2 n } ^ { \prime }$ with $n \geq 3$ , the normalization $( M _ { A D E } ^ { \mathrm { s l c } } ) ^ { \nu }$ is $V _ { \Lambda ^ { \prime } } ^ { \mathrm { s e m } 1 } / W _ { \Lambda }$ −with the lattice $\Lambda ^ { \prime }$ − − described in (5.11).  
(3) For an arbitrary primed shape, the normalization $( M _ { A D E } ^ { \mathrm { s l c } } ) ^ { \nu }$ is $V _ { \Lambda ^ { \prime } } ^ { \mathrm { s e m 1 } } / W _ { \Lambda } \rtimes W _ { 0 }$ , for a lattice extension $\Lambda ^ { \prime } \supset \Lambda$ .
The lattice $\Lambda ^ { \prime }$ and the Weyl group $W _ { 0 }$ are described in (5.12).

Proof.
(1) By Theorems 6.18, 6.26, 6.28, every one-parameter family of $A D E$ pairs has a limit which is a stable $A D E$ pair, since it has a limit (after a finite base change) in the family over $V _ { M } ^ { \mathrm { { c o x } } }$ .
By Theorem 6.37 the classifying morphism $\phi \colon V _ { M } ^ { \mathrm { s e m i } } / W \to M _ { A D E } ^ { \mathrm { s l c } }$ is finite-to-one.
By Theorem 5.9 on a dense open set it equals $\operatorname { H o m } ( M , \mathbb { C } ^ { * } ) / W \to \operatorname { H o m } ( \Lambda , \mathbb { C } ^ { * } ) / W$ , and it factors through the homomorphism ${ \mathrm { H o m } } ( M , \mathbb { C } ^ { * } ) \to { \mathrm { H o m } } ( \Lambda , \mathbb { C } ^ { * } )$ , the quotient by the finite multiplicative group $\mu : = \operatorname { H o m } ( M / \Lambda , \mathbb { C } ^ { * } )$ .
Thus, isomor $\phi$ factors through hism over an op $V _ { \Lambda } ^ { \mathrm { s e m i } } = V _ { M } ^ { \mathrm { s e m i } } / \mu$ , and Since orphism is norm $V _ { M } ^ { \mathrm { s e m i } } \to M _ { A D E } ^ { \mathrm { s l c } }$ is finite to omalization of an.
$V _ { M } ^ { \mathrm { s e m i } }$ $M _ { A D E } ^ { \mathrm { s l c } }$

Parts (2) and (3) are proved the same way.

Remark 6.39. Theorem 6.38 extends to surfaces of shapes with folds, e.g. $A _ { 2 n - 1 } ^ { f }$ , cf.
Remark 6.31.

# 7. Canonical families and their compactifications

In the previous Section we compactified the stack of $A D E$ pairs – which for the pure shapes is $\left[ \mathbb { A } ^ { n } : \mu _ { \Lambda } \right]$ – and extended the naive family over it to a family of stable pairs.
However, $\left[ \mathbb { A } ^ { n } : \mu _ { \Lambda } \right]$ has many automorphisms, and consequently in the equation $f$ of the divisor $B$ we have a lot of freedom for the coefficients $c _ { i } = c _ { i } ( \chi _ { 1 } , \ldots , \chi _ { n } )$ as polynomials in the fundamental characters.
Many of these choices extend to the compactification.

Example 7.1. For the $A _ { 1 }$ shape the moduli stack is $\left[ \mathbb { A } ^ { 1 } : \mu _ { 2 } \right]$ , and we write $\mathbb { A } ^ { 1 }$ as the quotient of the torus $\mathbb { C } _ { t } ^ { * }$ by the Weyl group $W _ { \Lambda } = \mathbb { Z } _ { 2 }$ , $t  t ^ { - 1 }$ .
The compactification is $[ \mathbb { P } ^ { 1 } : \mu _ { 2 } ]$ .
The equation of $B$ is $f = 1 + c _ { 1 } x + x ^ { 2 }$ , where in the naive family we have $c _ { 1 } = \chi _ { 1 } = t + t ^ { - 1 }$ .
We can apply to $\mathbb { A } ^ { 1 }$ an automorphism $c _ { 1 } \mapsto a c _ { 1 } + b$ , with $a , b \in \mathbb { C }$ and $a \neq 0$ , then pull the family back to $\mathbb { C } _ { t } ^ { * }$ .
This automorphism extends to the compactification $\mathbb { P } ^ { 1 }$ of $\mathbb { A } ^ { 1 }$ , but the coordinate change is not compatible with the $\mu _ { \Lambda }$ -action (i.e. with the $( \Lambda ^ { * } / \Lambda )$ -grading) unless $b = 0$ , since $( - 1 ) \in \mu _ { 2 }$ acts by $a c _ { 1 } + b \mapsto - a c _ { 1 } + b$ , so it is not an automorphism of $\left[ \mathbb { A } ^ { 1 } : \mu _ { 2 } \right]$ .
In this case the naive family is effectively unique.

However, for the root systems $D _ { n }$ ( $n \geq 5$ ) and $E _ { n }$ ( $n = 6 , 7 , 8$ ) there exist dominant weights $\lambda < \varpi _ { i }$ lying below the fundamental weights and with $\lambda \equiv \varpi _ { i }$ in $\Lambda ^ { * } / \Lambda$ , and we can modify the coefficients $c _ { i } = \chi _ { i }$ by adding linear combinations of their characters $\chi ( \lambda )$ .
For example, for $E _ { 8 }$ there are 23 dominant weights $\lambda$ below , and $\Lambda ^ { * } / \Lambda = 0$ .
Counting all fundamental weights $\varpi$ and their lower terms, there is a $\mathbb { C } ^ { 5 1 }$ worth of choices for $\begin{array} { r } { c = \chi ( \varpi ) + \sum _ { \lambda < \varpi } c _ { \lambda } \chi ( \lambda ) } \end{array}$ , all extending to automorphisms of our moduli compactification.

In this Section we show that the naive family can be deformed in an essentially unique way so that the new family, which we call the canonical family, has the following wonderful property: the discriminant locus in $T _ { \Lambda }$ , over which the divisor $B$ in our $A D E$ pairs become singular, is a union of root hypertori $\{ e ^ { \alpha } = 1 \}$ , with $\alpha$ going over the roots of the lattice $\Lambda$ .

We then show that the canonical family extends to the compactification and that on the boundary strata it restricts to the canonical families for smaller Dynkin diagrams.

7A.
Two notions of the discriminant.
Let $f ( x , y )$ be one of the polynomials in the equations (5.4)–(5.8), which we related to the root lattices $\Lambda = A _ { n }$ , $D _ { n }$ , $E _ { n }$ .
There are two different notions of the discriminant in this situation:

(1) The discriminant $\operatorname { D i s c r } ( f )$ of a polynomial $f ( x , y )$ .
This is a polynomial in the coefficients $c _ { i }$ of $f$ for which the zero set of $f$ on $Y \backslash C$ is singular.
If $c _ { i } = c _ { i } ( \chi _ { j } )$ are polynomials in the fundamental characters of the lattice $\Lambda$ , then $\operatorname { D i s c r } ( f )$ becomes a polynomial in $\chi _ { j }$ .

(2) The discriminant $\mathrm { D i s c r } ( \Lambda )$ of the lattice, the square of the expression

$$
\prod _ { \alpha \in \Phi ^ { + } } ( e ^ { \alpha / 2 } - e ^ { - \alpha / 2 } ) = \sum _ { w \in W _ { \Lambda } } \varepsilon ( w ) e ^ { w \cdot \rho } , \quad \mathrm { w h e r e ~ } \rho = \sum _ { \varpi \in \Pi } \varpi = \frac { 1 } { 2 } \sum _ { \alpha \in \Phi ^ { + } } \alpha .
$$

appearing in the Weyl character formula.
$\mathrm { D i s c r } ( \Lambda )$ is $W _ { \Lambda }$ -invariant, so it is also a polynomial in the fundamental characters.
The zero set of $\mathrm { D i s c r } ( \Lambda )$ is obviously the union of the root hypertori $e ^ { \alpha } = 1$ .

The following theorem forms the first part of Theorem D.
We prove it separately for the $A , D , E$ shapes in Theorems 7.3, 7.5, 7.7, respectively.

Theorem 7.2. For each $A D E$ pair of pure shape, there exists a unique deformation of the form $c = \chi ( \varpi ) +$ (lower terms) of the naive equation such that $\operatorname { D i s c r } ( f ) = \operatorname { D i s c r } ( \Lambda )$ .

# 7B.

Canonical families.

Theorem 7.3 ( $A$ shapes).
For the pure shapes $A _ { n } ^ { \prime }$ , resp.
${ \mathrm { - } } A _ { n } ^ { \prime }$ , in Theorem 7.2 one has $c _ { i } = \chi _ { i }$ resp.
$c _ { i } = \chi _ { i - 1 }$ .

Proof.
For $A _ { n } ^ { \prime }$ the curve $- { \textstyle { \frac { 1 } { 4 } } } y ^ { 2 } + c ( x )$ is singular iff $c ( x )$ has a double root.
If

$$
c ( x ) = \prod _ { i = 1 } ^ { n + 1 } ( x + t _ { i } ) = 1 + \chi _ { 1 } x + \ldots + \chi _ { n } x ^ { n } + x ^ { n + 1 }
$$

then this happens iff $e ^ { e _ { i } - e _ { j } } = t _ { i } / t _ { j } = 1$ .
Here, $e _ { i } - e _ { j }$ are precisely the roots of $A _ { n }$ .
Thus, the statement holds for $c _ { i } ~ = ~ \chi _ { i }$ .
For $A _ { n }$ there are no lower weights below the fundamental weights, so the solution is unique.
The open sets $Y \setminus C$ for the shapes $A _ { n } ^ { \prime }$ and ${ \mathrm { - } } A _ { n } ^ { \prime }$ are the same, so this argument applies to the ${ \mathrm { - } } A _ { n } ^ { \prime }$ shapes as well.


Recall from section 5E that for the $D$ and $E$ shapes there are two equivalent forms of the equation: $F ( x , y , z )$ and $f ( x , y )$ , and the latter is obtained from the former by completing the square in $z$ .
For $D _ { n }$ one has the following root lattice, weight lattice, Weyl group, fundamental roots $\alpha _ { i }$ , and fundamental weights $\varpi _ { i }$ :

$$
\begin{array} { r l } & { \Lambda = \Big \{ ( a _ { i } ) \in \mathbb { Z } ^ { n } = \Phi \mathbb { Z } e _ { i } \mid \sum a _ { i } \mathrm { ~ i s ~ e v e n } \Big \} , \quad \Lambda ^ { * } = \mathbb { Z } ^ { n } + \frac { 1 } { 2 } \sum e _ { i } . } \\ & { W _ { \Lambda } = \mathbb { Z } _ { 2 } ^ { n - 1 } \times S _ { n } , } \\ & { \alpha _ { n - 2 - i } = e _ { i } - e _ { i + 1 } \mathrm { ~ f o r ~ } i \le n - 2 , \ \alpha _ { 1 } ^ { \prime } = e _ { n - 1 } - e _ { n } , \ \alpha ^ { \prime \prime } = e _ { n - 1 } + e _ { n } . } \\ & { \varpi _ { n - 2 - i } = \displaystyle \sum _ { k = 1 } ^ { i } e _ { k } \mathrm { ~ f o r ~ } i \le n - 2 , \ \varpi _ { 1 } ^ { \prime } = \frac { 1 } { 2 } \left( - e _ { n } + \displaystyle \sum _ { i = 1 } ^ { n - 1 } e _ { i } \right) , \ \varpi ^ { \prime \prime } = \frac { 1 } { 2 } \left( \displaystyle \sum _ { i = 1 } ^ { n } e _ { i } \right) . } \end{array}
$$

Denoting by $\sigma _ { i }$ the $i$ -th symmetric polynomial, the fundamental characters are

$$
\chi _ { i } = \sigma _ { n - 2 - i } ( t _ { k } ^ { \pm } ) \mathrm { ~ f o r ~ } i \leq n - 2 , \mathrm { ~ } \chi _ { 1 } ^ { \prime } = \frac { \sum _ { s \geq 0 } \sigma _ { 2 s + 1 } ( t _ { k } ) } { \sqrt { \prod t _ { k } } } , \mathrm { ~ } \chi ^ { \prime \prime } = \frac { \sum _ { s \geq 0 } \sigma _ { 2 s } ( t _ { k } ) } { \sqrt { \prod t _ { k } } } ,
$$

where $t _ { k } ^ { \pm }$ are $t _ { 1 } , t _ { 1 } ^ { - 1 } , \ldots , t _ { n } , t _ { n } ^ { - 1 }$

Definition 7.4. Let $f _ { k } ( x )$ be the polynomials defined recursively by $f _ { 0 } = 1$ , $f _ { 1 } = x$ , and $f _ { k + 2 } =$ $x f _ { k + 1 } - f _ { k }$ .
These are the Fibonacci polynomials, except for the signs and a shift in degrees by 1. One has $f _ { 2 } = x ^ { 2 } - 1$ , $f _ { 3 } = x ^ { 3 } - 2 x$ , etc.

Theorem 7.5 ( $D$ shapes).
For the $D _ { n } ^ { ? }$ shapes, in Theorem 7.2 one has $c _ { 1 } ^ { \prime } = \chi _ { 1 } ^ { \prime }$ , $c ^ { \prime \prime } = \chi ^ { \prime \prime }$ , and the expression for $c ( x )$ can be obtained from the generating function

$$
c ( x , \chi ) = \sum _ { i , j \geq 0 } c _ { i j } x ^ { i } \chi ^ { j } = \sum _ { i \geq 0 } c _ { i } ( \chi ) x ^ { i } = \sum _ { j \geq 0 } p _ { j } ( x ) \chi ^ { j }
$$

by substituting $\chi _ { j }$ for $\chi ^ { j }$ and setting $\chi _ { n - 2 } = 1$ and $\chi _ { j } = 0$ for $j > n - 2$ .
One has

$c ( x , \chi ) = \frac { 1 } { ( 1 - \chi ^ { 2 } ) ( 1 - x \chi + \chi ^ { 2 } ) } \ a n d \ c _ { i } ( \chi ) = \frac { \chi ^ { i } } { ( 1 - \chi ^ { 4 } ) ( 1 + \chi ^ { 2 } ) ^ { i } } .$ (2) $p _ { 2 k } ( x ) = f _ { k } ^ { 2 }$ and $p _ { 2 k + 1 } = f _ { k } f _ { k + 1 }$ .
(3) $c _ { i j } = 0$ if $j - i$ is odd or $i > j$ .
Otherwise,

$$
c _ { i , i + 2 k } = \sum _ { p \geq 0 } ^ { k } ( - 1 ) ^ { p } { \binom { i + p } { i } } = ( - 1 ) ^ { k } \sum _ { q \geq 0 } { \binom { i + k - 1 - 2 q } { i - 1 } } .
$$

The central fiber has a $D _ { n }$ singularity at the point $( x , y , z ) = ( - 2 , - 2 ^ { n - 3 } , - 2 ^ { n - 3 } )$ .

Example 7.6. For $D _ { 7 }$ we obtain for the following expressions for $c ( x )$ :

$$
\begin{array} { c } { { \chi _ { 0 } + \chi _ { 1 } x + \chi _ { 2 } x ^ { 2 } + \chi _ { 3 } x ( x ^ { 2 } - 1 ) + \chi _ { 4 } ( x ^ { 2 } - 1 ) ^ { 2 } + ( x ^ { 2 } - 1 ) ( x ^ { 3 } - 2 x ) = } } \\ { { { } } } \\ { { ( \chi _ { 0 } + \chi _ { 4 } ) + ( \chi _ { 1 } - \chi _ { 3 } + 2 ) x + ( \chi _ { 2 } - 2 \chi _ { 4 } ) x ^ { 2 } + ( \chi _ { 3 } - 3 ) x ^ { 3 } + \chi _ { 4 } x ^ { 4 } + x ^ { 5 } } } \end{array}
$$

and for any lower $D _ { n }$ the formulas can be obtained from these by truncation.

Proof of Thm.
7.5. We start with the polynomial $f ( x , y )$ in equation (5.7).
As a quadratic polynomial in $y$ , it represents a curve which is a double cover of $\mathbb { A } ^ { 1 }$ .
This curve is singular when the following polynomial in $x$

$$
\mathrm { D i s c r } _ { y } ( f ) = ( x ^ { 2 } - 4 ) c ( x ) + c _ { 1 } ^ { \prime } c ^ { \prime \prime } x + c _ { 1 } ^ { \prime 2 } + c ^ { \prime \prime 2 }
$$

has a double root.
On the other hand, the polynomial $\begin{array} { r } { p ( x ) = \prod _ { i = 1 } ^ { n } ( x + t _ { i } + t _ { i } ^ { - 1 } ) } \end{array}$ has a double root iff some $t _ { i } + t _ { i } ^ { - 1 } = t _ { j } + t _ { j } ^ { - 1 }$ , i.e. $t _ { i } t _ { j } ^ { - 1 } = 1$ or $t _ { i } t _ { j } = 1$ .
These are exactly the root hypertori for the root lattice $D _ { n }$ .

Thus, $\operatorname { D i s c r } ( f ) = \operatorname { D i s c r } ( \Lambda )$ iff $\mathrm { D i s c r } _ { y } ( f ) = p ( x )$ .
The coefficients of $p ( x )$ are $\sigma _ { i } ( t _ { k } + t _ { k } ^ { - 1 } )$ , and they are invariant under the $W ( D _ { n } )$ -action, so they are polynomials in the fundamental characters $\chi _ { i }$ listed above.
The rest of the proof is a combinatorial manipulation to get the exact formula.
From this procedure we see that the solution is unique.


Theorem 7.7 ( $E$ shapes).
For the ${ } ^ { - } E _ { n } ^ { \prime }$ shapes, in Theorem 7.2 one has

$$
\begin{array} { l } { { c ^ { \prime \prime } = \chi ^ { \prime \prime } - 6 ~ c _ { 2 } ^ { \prime } = \chi _ { 2 } ^ { \prime } ~ c _ { 1 } ^ { \prime } = \chi _ { 1 } ^ { \prime } - \chi _ { 2 } } } \\ { { c _ { 0 } = \chi _ { 0 } - 3 \chi ^ { \prime \prime } + 9 ~ c _ { 1 } = \chi _ { 1 } - \chi _ { 2 } ^ { \prime } ~ c _ { 2 } = \chi _ { 2 } } } \end{array}
$$

$\scriptstyle { E _ { 7 } }$

$$
\begin{array} { l } { { c ^ { \prime \prime } = \chi ^ { \prime \prime } - 6 \chi _ { 3 } ~ c _ { 2 } ^ { \prime } = \chi _ { 2 } ^ { \prime } - 2 5 ~ c _ { 1 } ^ { \prime } = \chi _ { 1 } ^ { \prime } - \chi _ { 2 } - 1 6 \chi _ { 2 } ^ { \prime } + 2 0 6 } } \\ { { c _ { 0 } = \chi _ { 0 } - 3 \chi ( \varpi ^ { \prime \prime } + \varpi _ { 3 } ) + \chi ( 2 \varpi _ { 2 } ^ { \prime } ) - 1 2 \chi _ { 1 } ^ { \prime } + 9 \chi ( 2 \varpi _ { 3 } ) + 1 6 \chi _ { 2 } + 6 9 \chi _ { 2 } ^ { \prime } - 5 4 8 } } \\ { { c _ { 1 } = \chi _ { 1 } - \chi ( \varpi _ { 2 } ^ { \prime } + \varpi _ { 3 } ) - 6 \chi ^ { \prime \prime } + 2 8 \chi _ { 3 } ~ c _ { 2 } = \chi _ { 2 } - 2 \chi _ { 2 } ^ { \prime } + 2 3 ~ c _ { 3 } = \chi _ { 3 } } } \end{array}
$$

$E _ { 8 }$

$$
\begin{array} { l } { { c ^ { \prime \prime } = \chi ^ { \prime \prime } - 6 \chi _ { 3 } - 3 5 \chi _ { 2 } ^ { \prime } + 9 2 0 \chi _ { 4 } - 5 7 5 0 5 \qquad c _ { 2 } ^ { \prime } = \chi _ { 2 } ^ { \prime } - 2 5 \chi _ { 4 } + 2 3 2 5 } } \\ { { c _ { 1 } ^ { \prime } = \chi _ { 1 } ^ { \prime } - \chi _ { 2 } - 1 6 \chi ( \varpi _ { 2 } ^ { \prime } + \varpi _ { 4 } ) - 4 4 \chi ^ { \prime \prime } + 2 0 6 \chi ( 2 \varpi _ { 4 } ) + } } \\ { { \qquad + 3 6 0 \chi _ { 3 } + 2 1 9 6 \chi _ { 2 } ^ { \prime } - 5 1 2 4 6 \chi _ { 4 } + 2 4 0 1 9 0 0 } } \\ { { c _ { 0 } = \chi _ { 0 } - 3 \chi ( \varpi ^ { \prime \prime } + \varpi _ { 3 } ) + \chi ( 2 \varpi _ { 2 } ^ { \prime } + \varpi _ { 4 } ) - 1 2 \chi ( \varpi _ { 1 } ^ { \prime } + \varpi _ { 4 } ) - 2 8 \chi ( \varpi _ { 2 } ^ { \prime } + \varpi ^ { \prime \prime } ) + } } \end{array}
$$

$$
+ 9 \chi ( 2 \varpi _ { 3 } ) + 1 6 \chi ( \varpi _ { 2 } + \varpi _ { 4 } ) - 6 8 \chi _ { 1 } + 6 9 \chi ( \varpi _ { 2 } ^ { \prime } + 2 \varpi _ { 4 } ) + 2 1 2 \chi ( \varpi _ { 2 } ^ { \prime } + \varpi _ { 3 } ) +
$$

$$
+ 1 0 2 4 \chi ( \varpi ^ { \prime \prime } + \varpi _ { 4 } ) + 2 3 6 \chi ( 2 \varpi _ { 2 } ^ { \prime } ) + 2 4 5 3 \chi _ { 1 } ^ { \prime } - 5 4 8 \chi ( 3 \varpi _ { 4 } ) -
$$

$$
- 5 2 2 8 \chi ( \varpi _ { 3 } + \varpi _ { 4 } ) - 1 5 0 7 \chi _ { 2 } - 4 2 6 5 6 \chi ( \varpi _ { 2 } ^ { \prime } + \varpi _ { 4 } ) - 1 0 7 6 3 6 \chi ^ { \prime \prime } +
$$

$$
c _ { 1 } = \chi _ { 1 } - \chi ( \varpi _ { 2 } ^ { \prime } + \varpi _ { 3 } ) - 6 \chi ( \varpi ^ { \prime \prime } + \varpi _ { 4 } ) + 2 \chi ( 2 \varpi _ { 2 } ^ { \prime } ) - 1 7 \chi _ { 1 } ^ { \prime } +
$$

$$
+ 2 8 \chi ( \varpi _ { 3 } + \varpi _ { 4 } ) - 7 9 \chi _ { 2 } + 3 8 3 \chi ( \varpi _ { 2 } ^ { \prime } + \varpi _ { 4 } ) + 1 4 2 9 \chi ^ { \prime \prime } -
$$

$$
- 4 4 1 4 \chi ( 2 \varpi _ { 4 } ) + 8 4 \chi _ { 3 } - 4 9 7 6 8 \chi _ { 2 } ^ { \prime } + 2 7 1 9 3 4 \chi _ { 4 } + 4 5 2 8 1 9 2
$$

$$
\begin{array} { l } { { c _ { 2 } = \chi _ { 2 } - 2 \chi ( \varpi _ { 2 } ^ { \prime } + \varpi _ { 4 } ) - 9 \chi ^ { \prime \prime } + 2 3 \chi ( 2 \varpi _ { 4 } ) - 1 1 4 \chi _ { 3 } + 6 0 1 \chi _ { 2 } ^ { \prime } + 7 6 7 3 \chi _ { 4 } - 9 5 5 9 5 5 } } \\ { { c _ { 3 } = \chi _ { 3 } - 3 \chi _ { 2 } ^ { \prime } - 1 7 0 \chi _ { 4 } + 2 3 4 0 5 \qquad c _ { 4 } = \chi _ { 4 } - 2 4 8 } } \end{array}
$$

The central fiber with an $E _ { 6 }$ , resp.
$E _ { 7 }$ , resp.
$E _ { 8 }$ singularity is

$\mathbf { { E _ { 6 } } }$ : $x y z = z ^ { 2 } + 7 2 z + y ^ { 3 } + 2 7 y ^ { 2 } + 3 2 4 y + 2 7 0 0 + 3 2 4 x + 2 7 x ^ { 2 } + x ^ { 3 } ~ \mathrm { ~ d }$ at $( x , y , z ) = ( - 6 , - 6 , - 1 8 )$ .  
$\scriptstyle { E _ { 7 } }$ : $x y z = z ^ { 2 } + 5 7 6 z + y ^ { 3 } + 1 0 8 y ^ { 2 } + 5 1 8 4 y + 1 9 3 5 3 6 + 1 7 2 8 0 x + 1 2 9 6 x ^ { 2 } + 5 6 x ^ { 3 } + x ^ { 4 }$ at $( x , y , z ) =$ $( - 1 2 , - 2 4 , - 1 4 4 )$ .  
$E _ { 8 }$ : $x y z = z ^ { 2 } + y ^ { 3 } + x ^ { 5 }$ at $( 0 , 0 , 0 )$ .

The formulas for the polynomials $F ( x , y , z )$ were found by Etingof, Oblomkov, Rains in [EOR07] in a completely different context, as relations for the centers of certain non-commutative algebras associated to affine star-shaped Dynkin diagrams $\tilde { D } _ { 4 } , \tilde { E } _ { 6 } , \tilde { E } _ { 7 } , \tilde { E } _ { 8 }$ .
We found them independently, using Tjurina’s construction as explained below.
The answer given above is in terms of the additive basis of characters of dominant weights, which is needed for computing the degenerations in Theorem 7.11. Once we recomputed our answer in the polynomial basis of the fundamental characters $\chi _ { i }$ and did a web search for the largest coefficient, a single mathematical match came up, to [EOR07, Sec. 9].

Before proving the theorem, we begin with preliminary observations and lemmas.

In [Tju70] Tjurina constructed a versal deformation of an $E _ { 8 }$ singularity as a family over $\mathbb { A } ^ { \mathrm { s } } = \mathrm { t h e }$ parameter space for 8 smooth points on a cuspidal cubic $C$ (note that one has $C \setminus \mathrm { c u s p } \simeq \mathbb { A } ^ { 1 } ,$ ).
See also [DPT80, p.190].
The discriminant locus of this family is a union of affine hyperplanes $e ^ { \alpha } = 0$ for the roots $\alpha \in E _ { 8 }$ .
Our observation is that replacing the cuspidal cubic by a nodal cubic $C$ (so that $C \setminus \mathrm { n o d e } \simeq \mathbb { C } ^ { * }$ ) gives a multiplicative version of Tjurina’s family over $( \mathbb { C } ^ { * } ) ^ { \ 8 }$ that we are after.

lattice The lattice $A _ { 8 } ^ { * }$ 8 is generated by can be realized as an intermediate sublattice of index 3 in $e _ { i } - p$ , where $1 \leq i \leq 9$ and $\textstyle p = { \frac { 1 } { 9 } } \sum _ { i = 1 } ^ { 9 } e _ { i }$ 8. The lattice $A _ { 8 } \subset E _ { 8 } \subset A _ { 8 } ^ { * }$ $A _ { 8 }$ 8 ⊂ 8 is generated by .
The $e _ { i } - e _ { j }$ , and the intermediate lattice $E _ { 8 }$ is obtained by adding $\ell - e _ { 1 } - e _ { 2 } - e _ { 3 }$ , where $\ell = 3 p$ .

Now let $C$ be an irreducible curve of genus $^ { 1 }$ , so $C$ is either smooth, or has a node, or a cusp.
Let $G = \operatorname { P i c } ^ { 0 } C$ , so either an elliptic curve (with a choice of $0$ ), or $\mathbb { C } ^ { * } \ni 1$ , or $\mathbb { G } _ { a } \ni 0$ .
The nonsingular locus $C ^ { 0 }$ is a $G$ -torsor.

Lemma 7.8. Let $A _ { n } , E _ { 8 }$ be the standard root lattices, and $A _ { n } ^ { * }$ the dual lattice.
Then:

(1) $\mathrm { H o m } ( A _ { n } , G ) = A _ { n } ^ { * } \otimes G = G ^ { n + 1 } / \mathrm { d i a g } G = ( C ^ { 0 } ) ^ { n + 1 } / G$ parametrizes $( n + 1 )$ nonsingular points $P _ { i }$ on $C$ modulo translations by $G$ .
(2) $\mathrm { H o m } ( A _ { n } ^ { * } , G ) = A _ { n } \otimes G = \left\{ ( g _ { 1 } , \dotsc , g _ { n + 1 } ) \ | \ \sum g _ { i } = 0 \right\}$ parametrizes the choice of an origin $P _ { 0 } \in C ^ { 0 }$ plus $( n + 1 )$ nonsingular points $P _ { i } \in C ^ { 0 }$ such that $( n + 1 ) P _ { 0 } \sim \sum P _ { i }$ .

(3) ${ \mathrm { H o m } } ( E _ { 8 } , G ) = E _ { 8 } \otimes G$ parametrizes embeddings $C \subset \mathbb { P } ^ { 2 }$ as a cubic curve plus $\delta$ points $P _ { i } \in C ^ { 0 }$ , or equivalently embeddings $C \subset \mathbb { P } ^ { 2 }$ plus $g$ points $P _ { i } \in C ^ { 0 }$ such that $\textstyle \prod _ { i = 1 } ^ { 9 } P _ { i } = 1$ in the group law of $C ^ { 0 }$ .
Thus, $P _ { 9 }$ is the 9th base point of the pencil $| C |$ of cubic curves on $\mathbb { P } ^ { 2 }$ through $P _ { 1 } , \ldots , P _ { 8 }$ .

Proof.
We have $A _ { n } ^ { * } = \mathbb { Z } ^ { n + 1 } / \operatorname { d i a g } \mathbb { Z }$ and $A _ { n } = \{ ( a _ { 1 } , \ldots , a _ { n + 1 } ) \in \mathbb { Z } ^ { n + 1 } \mid \sum a _ { i } = 0 \}$ , so (1) and (2) follow.
Hence, $\mathrm { H o m } ( A _ { 8 } ^ { * } , G )$ parametrizes embeddings $C \subset \mathbb { P } ^ { 2 }$ with 8 points and a choice of a flex, and $E _ { 8 } \otimes G = \mathrm { H o m } ( A _ { 8 } ^ { * } , G ) / G [ 3 ]$ forgets the flex. 

Thus, the torus $T _ { A _ { 8 } ^ { * } }$ parametrizes 8 smooth points $P _ { 1 } , \ldots , P _ { 8 }$ on a nodal cubic curve $C \subset \mathbb { P } ^ { 2 }$ with a chosen flex, and the torus $T _ { E _ { 8 } }$ the same, but forgetting the flex. We now take a concrete rational nodal cubic $C \subset \mathbb { P } ^ { 2 }$ given by the equation $g _ { 0 } = - u v w + v ^ { 3 } + w ^ { 3 }$ with a rational parametrization $( u : v : w ) = ( t ^ { 3 } - 1 : t : - t ^ { 2 } )$ , so that the singular point of $C$ is $( 1 : 0 : 0$ ) corresponding to $t = 0$ or $\infty$ .
Now consider a family over $\mathbb { A } ^ { 8 }$ of cubics

$$
g _ { 1 } = \sum _ { i , j \geq 0 , \ i + j \leq 3 } a _ { i j } u ^ { 3 - i - j } v ^ { i } w ^ { j } , \quad a _ { 0 0 } = 1 , \ a _ { 1 1 } = 0
$$

Then any pencil of cubic curves, parametrized by $x$ , with a smooth generic fiber which has $C$ at $x = \infty$ has a unique representation by a polynomial $g ( x ; u , v , w ) = x g _ { 0 } + g _ { 1 }$ .
It is a simple exercise to put this pencil into the Weierstrass form $\phi ^ { 2 } = y ^ { 3 } + A ( x ) y + B ( x )$ using Nagell’s algorithm or simply by using the [Sage17] function WeierstrassForm.
The polynomials $A ( x )$ , $B ( x )$ have degrees 4 and 5 (not 6 since $C$ is singular).
The following is an easy explicit computation:

Lemma 7.9. There is a unique change of coordinates of the form $x \mapsto x + d$ , $y \mapsto y + a x ^ { 2 } + b x + c$ which leaves the fiber $C$ at $x = \infty$ in the pencil intact and takes the polynomial $f ( x , y ) = y ^ { 3 } + A ( x ) y + B ( x )$ into the form of the equation (5.8) for $E _ { 8 }$ .

We will use this to build a family over $( \mathbb { C } ^ { * } ) ^ { \ 8 }$ with the required properties.
We pick $t _ { 1 } , \ldots , t _ { 8 }$ in $\mathbb { C } ^ { * }$ arbitrarily and then also $t _ { 9 }$ so that $\textstyle \prod _ { i = 1 } ^ { 9 } t _ { i } = 1$ .
Using the rational parametrization of the nodal cubic $C$ , this gives 9 smooth points $P _ { 1 } , \dots , P _ { 9 } \in C$ .

Lemma 7.10. The pencil $g ( x ; u , v , w )$ passes through the points $P _ { 1 } , \ldots , P _ { 9 }$ iff

$$
\begin{array} { c c c c } { { a _ { 1 0 } = \sigma _ { 8 } } } & { { a _ { 0 1 } = \sigma _ { 1 } } } & { { a _ { 2 1 } = - \sigma _ { 2 } + \sigma _ { 5 } - \sigma _ { 8 } } } & { { a _ { 1 2 } = - \sigma _ { 1 } + \sigma _ { 4 } - \sigma _ { 7 } } } \\ { { } } & { { } } & { { } } \\ { { a _ { 3 0 } = - 3 + \sigma _ { 6 } } } & { { a _ { 0 3 } = - 3 + \sigma _ { 3 } } } & { { a _ { 2 0 } = - \sigma _ { 1 } + \sigma _ { 7 } } } & { { a _ { 0 2 } = \sigma _ { 2 } - \sigma _ { 8 } , } } \end{array}
$$

where $\sigma _ { i }$ are the elementary symmetric polynomials in $t _ { 1 } , \ldots , t _ { 9 }$ .

Proof.
We plug the rational parametrization $( u : v : w ) = ( t ^ { 3 } - 1 : t : - t ^ { 2 } )$ into $g _ { 1 } ( u , v , w )$ to obtain a monic polynomial of degree 9 with constant coefficient $^ { - 1 }$ which we set equal to $\begin{array} { r } { \prod _ { k = 1 } ^ { 9 } ( x - t _ { k } ) = } \end{array}$ $\scriptstyle \sum _ { n = 0 } ^ { 9 } ( - 1 ) ^ { n + 1 } \sigma _ { i } x ^ { i }$ .
Then we solve the resulting linear equations for $a _ { i j }$ .


Proof of Thm.
7.7. Define the pencil $g ( x ; u , v , w )$ as in Lemma 7.10, convert into Weierstrass form $\phi ^ { 2 } = y ^ { 3 } + A ( x ) y + B ( x )$ , then apply Lemma 7.9 to obtain a polynomial $f ( x , y )$ in the form of equation (5.8).
The coefficients $c _ { i }$ in the resulting expression for $f ( x , y )$ satisfy $c _ { i } \in \mathbb { C } [ A _ { 8 } ^ { * } ] ^ { S _ { 9 } }$ , so we obtain a family parametrized by the torus $T ( A _ { 8 } ^ { * } ) = \operatorname { H o m } ( A _ { 8 } ^ { * } , \mathbb { C } ^ { * } )$ .
The final very computationally intensive step, accomplished using [Sage17], is to rewrite it in terms of the characters of $E _ { 8 }$ .

We now prove that the discriminant $\operatorname { D i s c r } ( f )$ of this family of polynomials coincides with the discriminant $\mathrm { D i s c r } ( E _ { 8 } )$ .
We have a trivial family $\tilde { \mathcal { X } } ^ { 0 } = \mathbb { P } ^ { 2 } \times T _ { A _ { 8 } ^ { * } }  T _ { A _ { 8 } ^ { * } }$ with 9 sections, call them $s _ { 1 } , \ldots , s _ { 9 }$ , corresponding to the points $P _ { i } \in C ^ { 0 }$ .
Let ${ \widetilde { \chi } } ^ { n }$ , $1 \leq n \leq 9$ , be the family obtained by performing a smooth blowup of $\widetilde { \chi } ^ { n - 1 }$ along the strict preimage of $s _ { n }$ .

On each fiber the points $P _ { 1 } , \dots , P _ { 8 } \in \mathbb { P } ^ { 2 }$ are in an almost general position because they lie on an irreducible cubic (see [DPT80, p.39]).
This means that $- K _ { \mathcal { X } ^ { 8 } }$ is relatively nef and semiample, and defines a contraction to a family ${ \mathcal { X } } ^ { \mathrm { s } } \to { T } ( A _ { 8 } ^ { * } )$ of del Pezzo surfaces with relatively ample $- K _ { X ^ { 8 } }$ and with Du Val singularities.

On the other hand, $\widetilde { \mathcal X } ^ { 9 }$ is a family of Jacobian elliptic surfaces with a section $s _ { 9 }$ corresponding to the last point $P _ { 9 }$ .
The linear system $| N s _ { 9 } |$ , $N \gg 0$ gives a contraction $\tilde { \mathcal { X } } ^ { 9 }  \mathcal { X } ^ { 9 }$ to a family of surfaces with $A D E$ singularities.
Let $\widetilde { \iota _ { 9 } }$ be an elliptic involution $w \mapsto - w$ for this choice of a ezero section.
It descends to an involution $\widetilde { \iota _ { 8 } }$ of $\widetilde { \mathcal X } ^ { 8 }$ which in turn descends to an involution $\iota _ { 8 }$ of $\mathcal { X } ^ { \mathrm { s } }$ e.
It is easy to see that the quotients are families of the surfaces $X ^ { 9 } / \iota _ { 9 } = \mathbb { F } _ { 2 }$ and $Y ^ { \mathrm { s } } = X ^ { \mathrm { s } } / \iota _ { 8 } =$ $\mathbb { F } _ { 2 } ^ { \cup } = \mathbb { P } ( 1 , 1 , 2 )$ .
The families of the polynomials $f ( x , y )$ written above are just the equations of the branch curves.
On each fiber, the ramification curve passes through the singular point of the nodal cubic $C$ .
Blowing up the image of this point on $Y ^ { \ 8 }$ finally gives the toric $E _ { 8 }$ -surface $Y$ as in Fig.
3 corresponding to the Newton polytope of $f ( x , y )$ .

The branch curve $f = 0$ is singular iff the double cover $X ^ { \mathrm { s } }$ is singular.
This happens precisely when the points $P _ { 1 } , \ldots , P _ { 8 }$ are not in general position:

(1) some 3 out of 9 points $P _ { i } , P _ { j } , P _ { k }$ lie on a line $\Longleftrightarrow$ the complementary 6 points lie on a conic $\iff \ t _ { i } t _ { j } t _ { k } = 1$ .  
(2) some 2 out of 9 points $P _ { i } = P _ { j }$ ( $( i > j$ ) coincide $\Longleftrightarrow$ the complementary 7 points lie on a cubic which also has a node at $P _ { j } \iff t _ { i } = t _ { j }$ .

These are precisely the root loci for the roots of $E _ { 8 }$ in terms of the lattice $A _ { 8 } ^ { * }$ , with $t _ { i } = e ^ { e _ { i } - p }$ .
For our explicit parametrization of the nodal cubic $C$ this can be seen from

$$
\operatorname * { d e t } { \left| \begin{array} { l l l } { t _ { i } ^ { 3 } - 1 } & { t _ { i } } & { - t _ { i } ^ { 2 } } \\ { t _ { j } ^ { 3 } - 1 } & { t _ { j } } & { - t _ { j } ^ { 2 } } \\ { t _ { k } ^ { 3 } - 1 } & { t _ { k } } & { - t _ { k } ^ { 2 } } \end{array} \right| } = ( t _ { i } t _ { j } t _ { k } - 1 ) ( t _ { i } - t _ { j } ) ( t _ { i } - t _ { k } ) ( t _ { j } - t _ { k } ) .
$$

This shows that $\operatorname { D i s c r } ( f )$ is a product of the equations $( e ^ { \alpha } - 1 )$ of the root loci, and it is easy to see that they appear with multiplicity 1. Thus, $\operatorname { D i s c r } ( f ) = \pm \operatorname { D i s c r } ( E _ { 8 } )$ .

This completes the proof in the $E _ { 8 }$ case.
The $E _ { 7 }$ and $E _ { 6 }$ cases are obtained as degenerations of this construction.
In the $E _ { 7 }$ we blow up 7 smooth points of the cubic $C$ and the node $P _ { 8 }$ .
Then there exists a unique point $P _ { 9 }$ which is infinitely near to $P _ { 8 }$ such that all the cubics in the pencil $| C - P _ { 1 } - \cdot \cdot \cdot P _ { 8 } |$ pass through $P _ { 9 }$ .
In other words, $P _ { 9 }$ is a point on the exceptional divisor $E _ { 8 }$ of the blowup at $P _ { 8 }$ corresponding to a direction $t _ { 9 } \neq 0 , \infty$ at $P _ { 8 }$ for which we can write an explicit equation.
Blowing up at $P _ { 9 }$ gives an elliptic surface $\widetilde { \mathcal { X } } ^ { 9 }  \mathbb { P } ^ { 1 }$ with a zero section and an elliptic involution.
The preimage of $C$ on $\widetilde { \mathcal X } ^ { 9 }$ is an $I _ { 2 }$ Kodaira fiber, instead of an $I _ { 1 }$ fiber in the $E _ { 8 }$ case.
In the same way as above, the discriminant locus is a union of root loci for the roots of $E _ { 7 }$ .

The $E _ { 6 }$ case is a further degeneration.
We pick 6 smooth points on $C$ plus the node $P _ { 7 }$ plus an infinitely near point $P _ { 8 }  P _ { 7 }$ corresponding to one of the directions at the node.
Then there exists a unique infinitely near point $P _ { 9 } \to P _ { 8 }$ such that all the cubics in the pencil $| C - P _ { 1 } - \cdot \cdot \cdot P _ { 8 } |$ pass through $P _ { 9 }$ .
Blowing up at $P _ { 9 }$ gives an elliptic surface $\widetilde { \mathcal { X } } ^ { 9 } \to \mathbb { P } ^ { 1 }$ with a zero section and an elliptic involution.
The preimage of $C$ on $\widetilde { \mathcal X } ^ { 9 }$ is an $I _ { 3 }$ Kodaira fiber.
In the same way as above, the discriminant locus is a union of root loci for the roots of $E _ { 6 }$ .

For the uniqueness, write $\begin{array} { r } { c _ { i } = \chi _ { i } + \sum _ { \lambda < \varpi _ { i } } c _ { i , \lambda } \chi ( \lambda ) } \end{array}$ .
The weights $\lambda < \varpi _ { i }$ all lie below $\varpi _ { 0 }$ , there are 23 of them, and the partial order on them is described in Remark 7.12. Equating $\operatorname { D i s c r } ( f ) = \operatorname { D i s c r } ( \Lambda )$ gives a system of polynomial equations in $c _ { i , \lambda }$ which is upper triangular: There is a linear equation for the highest coefficient $c _ { i , \lambda }$ with no other coefficients present, so with a unique solution.
Then the equation for the next coefficient $c _ { j , \lambda ^ { \prime } }$ is linear with a unique solution once the higher coefficients are known, etc. The solutions are obtained recursively, in a unique way at every step.


7C.
Compactifications of the canonical families.
In this subsection we prove the remaining portion of Theorem D.

Theorem 7.11. The canonical family extends to the compactifications $V _ { M } ^ { \mathrm { { c o x } } }$ of Theorems 6.18, 6.26, 6.28. The restriction of the compactified canonical family to a boundary stratum is the canonical family for a smaller Dynkin diagram.

Proof.
For the compactification we use exactly the same formulas as in Theorems 6.18, 6.26, 6.28, and the proofs go through unchanged.
Indeed, the only fact we used was that the leading monomial in each coefficient $c$ is $e ^ { \omega }$ , and that the other monomials are of the form $e ^ { w }$ for some weights of the form $\begin{array} { r } { w = \varpi - \alpha - \sum _ { \beta } n _ { \beta } \beta } \end{array}$ .
These are automatically satisfied if we modify $\chi ( \varpi )$ only by adding characters of some lower weights $\lambda < \varpi$ .

For the fact that a canonical family restricts to canonical families on the boundary strata, a sketch of a possible proof, which can be made precise, is that the defining property of the canonical family is automatically satisfied for the restrictions.
Instead, we check the equations directly.

For $A _ { n }$ the check is immediate: the coefficients $\widehat { \chi } _ { i }$ of equation (6.1) restrict to $\widehat { \chi } _ { i }$ by Lemma 6.19, so (6.1) restricts to the $A _ { m }$ family for a smaller $A _ { m }$ diagram.

For $D _ { n }$ there are no dominant weights below $\varpi ^ { \prime }$ , $\varpi ^ { \prime \prime }$ , and the dominant weights below $\varpi _ { i }$ are $\varpi _ { i + 2 }$ , $\varpi _ { i + 4 }$ , etc., with the relations

$$
\varpi _ { i } - \varpi _ { i + 2 } = \alpha ^ { \prime } + \alpha ^ { \prime \prime } + 2 \alpha _ { 0 } + \cdot \cdot \cdot + 2 \alpha _ { i } + \alpha _ { i + 1 } .
$$

By Lemma 6.19, the character $\chi ( \lambda ) = e ^ { \lambda } { \widehat \chi } ( \lambda )$ under the degeneration $a _ { i } = e ^ { - \alpha _ { i } } \to 0$ goes to:

(1) $0$ if in the expression $\begin{array} { r } { \lambda = \varpi - \sum n _ { \alpha } \alpha } \end{array}$ one has $n _ { \alpha _ { i } } > 0$ , or to (2) $\widehat { \chi } ( \boldsymbol { p } ( \lambda ) )$ if $n _ { \alpha _ { i } } = 0$ , where $p ( \varpi _ { i } ) = 0$ and $p ( \varpi _ { j } ) = \varpi _ { j }$ for $j \neq i$

Thus, under the degenerations $a ^ { \prime } = 0$ , resp.
$a ^ { \prime \prime } = 0$ all the lower weights disappear, and we are left with an equation for the $A _ { n - 1 }$ , resp.
$A _ { n - 1 }$ family.
Under the degeneration $a _ { i } = 0$ , the limit surface has two components, and on the left, resp.
right, surface the equation becomes the $D _ { i + 2 }$ , resp.
$A _ { n - i - 3 }$ family if $i > 0$ .
For $i = 0$ we get the equations of $A _ { 1 }$ and $A _ { n - 3 }$ .

The $E _ { 8 }$ case is the hardest to analyze.
We computed the poset of dominant weights below $\varpi _ { 0 }$ in Table 6. Every line is a “cover”, a minimal step in the partial order, and we write the difference as a positive combination of simple roots.
The difference in a cover is known to be equal to the highest root of some connected Dynkin subdiagram, see e.g. [Ste98, Thm.2.6].
We give this diagram in the last column.
The corollary of that table is Table 7 showing the weights that do survive under degenerations.
All other lower weights under these and all other degenerations vanish.
From this table we immediately see for example that when either of the coordinates $a ^ { \prime \prime }$ , $a _ { 1 } ^ { \prime }$ , $a _ { 0 }$ , $a _ { 1 }$ is zero, then all the lower weights vanish and we are left with the equations of the $A$ or $A$ shapes.

In the degeneration $a _ { 2 } ^ { \prime } = 0$ the $E _ { 8 }$ equation of Theorem 7.7 reduces to $c ( x ) = ( \chi _ { 0 } + \chi _ { 4 } ) + ( \chi _ { 1 } -$ $\chi _ { 3 } + 2 ) x + ( \chi _ { 2 } - 2 \chi _ { 4 } ) x ^ { 2 } + ( \chi _ { 3 } - 3 ) x ^ { 3 } + \chi _ { 4 } x ^ { 4 } + x ^ { 5 }$ , which is precisely the equation of the canonical $D _ { 7 }$ family from Example 7.6.

For the degeneration $a _ { 4 } = 0$ one can check that the $E _ { 8 }$ equation reduces to the canonical $E _ { 7 }$ equation of Theorem 7.7, and for $a _ { 3 } = 0$ it reduces to the $E _ { 6 }$ equation.
The other cases are checked similarly.
The $E _ { 7 }$ and $E _ { 6 }$ cases now follow.
$\boxed { \begin{array} { r l } \end{array} }$

Remark 7.12. As we see, the poset of the dominant weights below the 8 fundamental weights of $E _ { 8 }$ is very complicated.
We make the following interesting observation.
Associate to the 8 nodes of the Dynkin diagram the following points in $\mathbb { Z } ^ { 3 }$ : $p _ { i } = ( i , 0 , 0 )$ , $p _ { j } ^ { \prime } = ( 0 , j , 0 )$ , $p _ { k } ^ { \prime \prime } = ( 0 , 0 , k )$ , and choose the special point $p _ { * } = ( 1 , 1 , 1 )$ .
Consider the projection $\psi \colon E _ { 8 } \to \mathbb { Z } \oplus \mathbb { Z } ^ { 3 }$ by the rule $\psi ( \varpi ) = ( 1 , p - p _ { * } )$ .
Then for a fundamental weight $\varpi$ , a dominant weight $\lambda$ satisfies $\lambda < \varpi$ iff $\psi ( \varpi - \lambda )$ is a non-negative combination of the 8 vectors $\psi ( \varpi _ { i } )$ and the vector $( - 1 , 0 , 0 , 0 )$ .

The same procedure works for $D _ { n }$ , $E _ { 6 }$ , $E _ { 7 }$ .
In the $D _ { n }$ case this becomes an especially easy way to see the relation (7.1).
Our two-dimensional projection of section 5A is a further projection from $\mathbb { Z } ^ { 3 }$ to $\mathbb { Z } ^ { 2 }$ obtained by “completing the square in the $z$ variable”.

7D.
Singularities of divisors in $A D E$ pairs.
By Theorem 7.2, the singularities of $B \cap ( Y \setminus C )$ in the canonical families occur on the fibers $Y _ { t }$ for $t \in \cup _ { \alpha } \{ e ^ { \alpha } = 1 \}$ , the union of root hypertori.
Generically, these are $A _ { 1 }$ singularities.
On the intersections of several hypertori some worse singularities occur.
Below we describe them explicitly.
For each of the lattices $\Lambda = A _ { n } , D _ { n } , E _ { n }$ the singularity over the point $1 \in T _ { \Lambda ^ { * } }$ is that same $A _ { n } , D _ { n } , E _ { n }$ .
However, there are zero-dimensional strata of the hypertori arrangement different from 1. Some other maximal rank singularities occur on the fibers over those points.

Table 6. Partial order on dominant weights of $E _ { 8 }$ below $\varpi _ { 0 }$  
![](images/74df733c72cb02799f9e97390a32c8b6664726a3a1cd8f95159e041425b5f5a6.jpg)

Definition 7.13. Let $\Lambda$ be an $A D E$ lattice with a root system $\Phi$ and Dynkin diagram $\Delta$ , and let $G$ be some abelian group which we will write multiplicatively.
Let $t \in { \mathrm { H o m } } ( \Lambda , G )$ be a homomorphism.
Define the sublattice

It is well known that a sublattice of an $A D E$ lattice generated by some of the roots is a direct sum of root lattices corresponding to smaller $A D E$ Dynkin diagrams.
All such root sublattices can be obtained by the Dynkin-Borel-de Siebenthal (DBS) algorithm, see [Dyn52, Thms. 5.2, 5.3], as follows.
Make several of the steps (DBS1): replace a connected component of the Dynkin diagram by an extended Dynkin diagram and then remove a node; and then several of the steps (DBS2): remove a node.
Below, we determine which of these lattices are realizable as $\Lambda _ { t }$ .

All root sublattices are listed in [Dyn52, Tables 9–11].
The answer is as follows.
Recall that the lattice $A _ { n } \subset \mathbb { Z } ^ { n + 1 }$ is generated by the roots $e _ { i } - e _ { j }$ .
All root sublattices of $A _ { n }$ are of the form

Table 7. For $E _ { 8 }$ , the dominant weights $\lambda < \varpi$ in $c$ which survive degenerations  
![](images/6c1c49bdf9d91cb5355ca1b4deed96be63948b7fb800eda3f42a8fc6ba397360.jpg)

$A _ { | I _ { 1 } | - 1 } \oplus \cdot \cdot \cdot \oplus A _ { | I _ { s } | - 1 }$ , where $I _ { 1 } \sqcup \cdot \cdot \cdot \sqcup I _ { s } = \{ 1 , . . . , n + 1 \}$ is a partition, $| I _ { i } | \geq 1$ .
Here, $A _ { \left| I _ { i } \right| - 1 } = 0$ if $| I _ { i } | = 1$ .

The lattice $D _ { n } \subset \mathbb { Z } ^ { n }$ is generated by the roots $e _ { i } \pm e _ { j }$ .
All root sublattices of $D _ { n }$ are of the form $A _ { | I _ { 1 } | - 1 } \oplus \cdots \oplus A _ { | I _ { s } | - 1 } \oplus D _ { | J _ { 1 } | } \oplus \cdots \oplus D _ { | J _ { r } | }$ , where $I _ { 1 } \sqcup \dots \sqcup I _ { s } \sqcup J _ { 1 } \sqcup \dots \sqcup J _ { r } = \{ 1 , \dots , n \}$ is a partition, $| I _ { i } | \geq 1$ and $| J _ { j } | \geq 2$ .
$D _ { 2 }$ and $D _ { 3 }$ are a special case.
They are isomorphic to $2 A _ { 1 }$ and $A _ { 3 }$ respectively as abstract lattices, but they are different as sublattices of $D _ { n }$ .

The sublattices of $E _ { 6 } , E _ { 7 } , E _ { 8 }$ are listed in [Dyn52, Table 11] but note the typos: in the $E _ { 8 }$ table one of the two $A _ { 7 } + A _ { 1 }$ is $E _ { 7 } + A _ { 1 }$ , and $A _ { 6 } + A _ { 2 }$ should be $E _ { 6 } + A _ { 2 }$ .

Definition 7.14. Let $M \subset \Lambda$ be two $A D E$ lattices.
Let $\operatorname { T o r s } ( \Lambda / M )$ be the torsion subgroup of $\Lambda / M$ and $\mathrm { i m } ( \Phi \cap M _ { \mathbb { R } } ) \subset \mathrm { T o r s } ( \Lambda / M )$ be the image of the set of roots $\alpha \in \Phi \cap M _ { \mathbb { R } }$ .
We define the closure ${ \overline { { \mathrm { i m } } } } ( \Phi \cap M _ { \mathbb { R } } )$ to be the subset of $\operatorname { T o r s } ( \Lambda / M )$ consisting of the elements $x \neq 0$ such that $0 \neq n x \in \operatorname { i m } ( \Phi \cap M _ { \mathbb { R } } )$ for some $n \in  { \mathbb { N } }$ ; plus $x = 0$ .
Both $\mathrm { i m } ( \Phi \cap M _ { \mathbb { R } } )$ and $\overline { { \mathrm { i m } } } ( \Phi \cap M _ { \mathbb { R } } )$ are finite sets, and a priori neither of them has to be a group.

Lemma 7.15. Let $M \subset \Lambda$ be two $A D E$ lattices.
Let $G$ be an abelian group containing $\mathbb { Z } ^ { r }$ , where $r \ = \ \operatorname { r k } \Lambda - \operatorname { r k } M$ .
Then $M \ = \ \Lambda _ { t }$ for some $t \in \mathrm { H o m } ( \Lambda , G )$ iff there exists a homomorphism $\phi$ : $\operatorname { T o r s } ( \Lambda / M ) \to G$ such that for any $0 \neq x \in { \overline { { \operatorname { i m } } } } ( \Phi \cap M _ { \mathbb { R } } )$ one has $\phi ( x ) \neq 0$ .

Proof.
Of course one must have $M \subset \ker ( t )$ , so the question is whether there exists a homomorphism $\Lambda / M \to G$ which does not map any roots not lying in $M$ to zero.
We have $\Lambda / M = \mathbb { Z } ^ { r } \oplus { \mathrm { T o r s } } ( \Lambda / M )$ .
An embedding $\mathbb { Z } ^ { r } \to G$ can always be adjusted by an element of $\operatorname { G L } ( r , \mathbb { Z } )$ so that the images of roots not in $\operatorname { T o r s } ( \Lambda / M )$ do not map to zero.
So the only condition is on $\mathrm { i m } ( \Phi \cap M _ { \mathbb { R } } )$ in $\operatorname { T o r s } ( \Lambda / M )$ or, equivalently, on its closure.
$\boxed { \begin{array} { r l } \end{array} }$

Corollary 7.16. Let $M \subset \Lambda$ be two $A D E$ lattices and let $k$ be an algebraically closed field of characteristic zero.
If the group $\operatorname { T o r s } ( \Lambda / M )$ is cyclic then $M \ = \ \Lambda _ { t }$ for some $t \in \mathrm { H o m } ( \Lambda , \mathbb { C } ^ { * } )$ .
In the opposite direction, if $\overline { { \mathrm { i m } } } ( \Phi \cap M _ { \mathbb { R } } )$ contains a non-cyclic subgroup then $M \ne \Lambda _ { t }$ for any $t \in { \mathrm { H o m } } ( \Lambda , \mathbb { C } ^ { * } )$ .

Proof.
This follows from the fact that any finite cyclic group can be embedded into $\mathbb { C } ^ { * }$ , and there are no non-cyclic finite subgroups in $\mathbb { C } ^ { * }$ .


Theorem 7.17. Let Λ be an irreducible $A D E$ lattice and $M$ be an $A D E$ root sublattice.
Assume that the field $k$ is algebraically closed of characteristic zero.
Then $M = \Lambda _ { t }$ for some $t \in { \mathrm { H o m } } ( \Lambda , \mathbb { C } ^ { * } )$ iff any of the following equivalent conditions holds:

(1) $\operatorname { T o r s } ( \Lambda / M )$ is cyclic.  
(2) $M$ is obtained from Λ by a single DBS1 step and then some DBS2 steps.  
(3) $M$ corresponds to a proper subdiagram of the extended Dynkin diagram $\widetilde { \Delta }$ .  
(4) $M$ corresponds to a subdiagram $\Delta$ of the following Dynkin diagrams: $A _ { n }$ : $A _ { n }$ ; $D _ { n } \colon D _ { n }$ or $D _ { a } D _ { b } \subset \widetilde { D } _ { n }$ with $a + b = n$ , $a , b \geq 2$ .
$E _ { 6 }$ : $E _ { 6 }$ , $A _ { 5 } A _ { 1 }$ , $3 A _ { 2 }$ ; $E _ { 7 } \colon E _ { 7 }$ , $D _ { 6 } A _ { 1 }$ , $A _ { 7 }$ , $A _ { 5 } A _ { 2 }$ , $2 A _ { 3 } A _ { 1 }$ ; $E _ { 8 }$ : $E _ { 8 }$ , $E _ { 7 } A _ { 1 }$ , $E _ { 6 } A _ { 2 }$ , $D _ { 8 }$ , $D _ { 5 } A _ { 3 }$ , $A _ { 8 }$ , $A _ { 7 } A _ { 1 }$ , $2 A _ { 4 }$ , $A _ { 5 } A _ { 2 } A _ { 1 }$ .  
(5) $M$ is not one of the following forbidden sublattices: $D _ { n }$ : a sublattice with $\geq 3$ $D$ -blocks; $E _ { 7 }$ : D4 3A1, $7 A _ { 1 }$ , 6A1; $E _ { 8 }$ : $4 A _ { 2 }$ , $2 D _ { 4 }$ , $D _ { 6 } 2 A _ { 1 }$ , $D _ { 4 } 4 A _ { 1 }$ , $2 A _ { 3 } 2 A _ { 1 }$ , $8 A _ { 1 }$ ,D43A1,7A1,A34A1,6A1.

Proof.
We first prove the equivalence of the conditions (1-5).
For one direction, the identity $\begin{array} { r } { \sum _ { \alpha \in { \widetilde { \Delta } } } m _ { \alpha } \alpha = 0 } \end{array}$ implies that if the Dynkin diagram $\Delta ( M )$ is obtained from $\widetilde { \Delta }$ by removing one node (i.e. by a single DBS1 step) then the cotorsion group is cyclic of the order equal to the multiplicity $m _ { \alpha }$ of the removed node in the highest root of $\Delta$ .
Any sublattice of these lattices obtained by DBS2 steps also has cyclic cotorsion.
The lists in (4) are simply the lattices obtained by one DBS1 step.
To complete the equivalence of (1-5) for $E _ { n }$ we use Dynkin’s lists of sublattices together with [Per90, Table 1] which gives the torsion groups, and check the finitely many cases.
The $D _ { n }$ case is easy.

Now let $M$ be a sublattice as in (1).
Then $M = \Lambda _ { t }$ for some $t \in \mathrm { H o m } ( \Lambda , \mathbb { C } ^ { * } )$ by Cor.
7.16. Vice versa, let $M$ be one of the sublattices with a non-cyclic $\operatorname { T o r s } ( \Lambda / M )$ , which are listed in (5).
If $\Lambda = D _ { n }$ and $M$ has $r \geq 3$ $D$ -blocks then $\mathrm { T o r s } ( \Lambda / M ) = \mathbb { Z } _ { 2 } ^ { r - 1 }$ and we easily calculate $\mathrm { i m } ( \Phi \cap M _ { \mathbb { R } } )$ to be $\{ 0 , e _ { i } , e _ { i } + e _ { j } \mid 1 \leq i , j \leq r - 1 \}$ .
This set contains a non-cyclic subgroup $\mathbb { Z } _ { 2 } ^ { 2 } = \{ 0 , e _ { 1 } , e _ { 2 } , e _ { 1 } + e _ { 2 } \}$ , so $M \neq \Lambda _ { t }$ by Cor.
7.16.

For each sublattice of $E _ { 7 }$ and $E _ { 8 }$ listed in (5) we explicitly compute $\overline { { \mathrm { i m } } } ( \Phi \cap M _ { \mathbb { R } } )$ .
We have $( \Lambda \cap M _ { \mathbb { R } } ) / M \subset M ^ { * } / M$ , so we find the images of the roots $\alpha \in \Phi \cap M _ { \mathbb { R } }$ in $M ^ { * } / M$ .
The result is as follows.
For $8 A _ { 1 }$ the set $\mathrm { i m } ( \Phi \cap M _ { \mathbb { R } } )$ has 15 elements and contains $\mathbb { Z } _ { 2 } ^ { 3 }$ ; for $2 A _ { 3 } 2 A _ { 1 }$ it has 7 elements and its closure is $\mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 2 }$ ; for $4 A _ { 2 }$ it has 8 elements and its closure is $\mathbb { Z } _ { 3 } ^ { 2 }$ .
In all the other cases, one has $\mathrm { i m } ( \Phi \cap M _ { \mathbb { R } } ) = \mathrm { T o r s } ( \Lambda / M )$ .
We conclude that $M \neq \Lambda _ { t }$ by Cor.
7.16. 

Theorem 7.18. Consider a canonical family of $A D E$ pairs of Theorems 7.3, 7.5, 7.7. Then for $a$ point $t \in T$ , the singularities of the curve $B _ { t } \cap ( Y _ { t } \setminus C _ { t } )$ and of the double cover $X _ { t } \setminus D _ { t }$ near $R _ { t }$ are Du Val of the type corresponding to the lattice $\Lambda _ { t }$ .
In particular, a curve is singular iff $t$ lies in a union of root hypertori $\{ e ^ { \alpha } = 1 \}$ , and for $t = 1$ there is a unique singularity of the same Du Val type as the root lattice.

Proof.
The $A _ { n }$ case is obvious: the curve curve $- y ^ { 2 } / 4 + c ( x )$ , $c ( \boldsymbol { x } ) = \prod ( \boldsymbol { x } + t _ { i } )$ has singularities $A _ { m _ { 1 } - 1 } , \ldots , A _ { m _ { s } - 1 }$ , each occurring when some $m _ { k }$ of the $t _ { i }$ ’s coincide, i.e. when several of the monomials $e ^ { t _ { i } - t _ { j } }$ vanish at the same time.

Let $\begin{array} { r } { \operatorname { D i s c r } _ { y } ( f ) = \prod _ { i = 1 } ^ { n } ( x + t _ { i } + t _ { i } ^ { - 1 } ) } \end{array}$ as in the proof of Thm.
7.5. It is easy to see that for every root $x \neq \pm 2$ of $\operatorname { D i s c r } _ { y }$ of multiplicity $m$ , the curve $f = 0$ has an $A _ { m - 1 }$ -singularity, and if $x = \pm 2$ is a root of $\operatorname { D i s c r } _ { y }$ of multiplicity $m$ then $f$ has a $D _ { m }$ -singularity.
This includes $D _ { 3 } = A _ { 3 }$ , $D _ { 2 } = 2 A _ { 1 }$ , and $D _ { 1 } = \mathrm { s m o o t h }$ .
On the other hand, the root tori are of the form $\{ t _ { i } t _ { j } ^ { \pm 1 } = 1 \}$ .
The irreducible components of $\Lambda _ { t }$ correspond to the disjoint subsets $I \subset \{ 1 , \ldots , n \}$ of indices for which $t _ { i } = t _ { j } ^ { \pm 1 }$ for $i , j \in I$ .
If $t _ { i } \neq \pm 1$ , i.e. $t _ { i } + t _ { i } ^ { - 1 } \neq \pm 2$ , then the component is of the $A _ { | I | - 1 }$ -type; otherwise it is of the $D _ { | I | }$ -type.

In the $E _ { n }$ cases the singularities are Du Val by construction in the proof of 7.7. Using notation as in the proof, let us fix a linear function $\varphi$ on $E _ { 8 } \subset A _ { 8 } ^ { * }$ such that $\varphi ( p ) > \varphi ( e _ { 1 } ) > \cdot \cdot \cdot > \varphi ( e _ { 8 } )$ , and let the positive roots $\alpha$ be those with $\varphi ( \alpha ) > 0$ .
Then for any subroot system of $E _ { 8 }$ the simple roots are exactly the roots that are realizable by irreducible $\left( - 2 \right)$ -curves on $\widetilde { X } ^ { 8 }$ : $e _ { i } - e _ { j }$ for $i > j$ (preimages of the exceptional divisors $E _ { i }$ of blowups at $P _ { i }$ ), $\ell - e _ { i } - e _ { j } - e _ { k }$ (preimages of lines passing through

3 points $P _ { i } , P _ { j } , P _ { k } )$ , $\textstyle 2 \ell - \sum _ { k = 1 } ^ { 6 } e _ { i _ { k } }$ (preimages of conics through 6 points), and $\begin{array} { r } { 3 \ell - 2 e _ { j } - \sum _ { k = 1 } ^ { 7 } e _ { i _ { k } } } \end{array}$ (preimages of nodal cubics through 8 points).
So for every $t \in \mathrm { H o m } ( E _ { 8 } , \mathbb { C } ^ { * } )$ , the simple roots in the lattice $\Lambda _ { t }$ are realized by $\left( - 2 \right)$ -curves on ${ \tilde { X } } _ { 8 }$ which contract to a configuration of singularities on $X ^ { \mathrm { s } }$ with the same Dynkin diagram as $\Lambda _ { t }$ .
The $E _ { 7 }$ and $E _ { 6 }$ cases are done similarly.


Remark 7.19. By the proof of Theorem 7.7, the surfaces in the $E _ { 6 } , E _ { 7 } , E _ { 8 }$ families correspond to rational elliptic fibrations with an $I _ { 3 } , I _ { 2 } , I _ { 1 }$ fiber respectively.
The singularity type of the double cover $X _ { t } \setminus D _ { t }$ is obtained from the Kodaira type of the elliptic fibration by dropping one $I _ { 3 } , I _ { 2 } , I _ { 1 }$ fiber respectively (it gives a singularity of $X _ { t }$ lying in the boundary $D _ { t }$ ; of type $A _ { 2 } , A _ { 1 }$ , or none resp.) and converting the other Kodaira fibers into the $A D E$ singularities.

As a check, we note that the list of maximal sublattices in Theorem $7 . 1 7 ( 4 )$ is equivalent to the list of the rational extremal non-isotrivial elliptic fibrations in [MP86, Thm. 4.1], and that the full list of sublattices in Theorem 7.17 is consistent with the full list of Kodaira fibers of rational elliptic fibrations in [Per90].
Persson’s list contains 6 surfaces with an $I _ { m }$ fiber for which the corresponding sublattice of $E _ { 8 }$ has non-cyclic cotorsion: $I _ { 2 } ^ { * } 2 I _ { 2 }$ $( D _ { 6 } 2 A _ { 1 } )$ , $I _ { 0 } ^ { * } 3 I _ { 2 }$ $( D _ { 4 } 3 A _ { 1 } )$ , $2 I _ { 4 } 2 I _ { 2 }$ $\left( 2 A _ { 3 } 2 A _ { 1 } \right)$ , $I _ { 4 } 4 I _ { 2 }$ $\left( A _ { 3 } 4 A _ { 1 } \right)$ , $4 I _ { 3 }$ ( $4 A _ { 2 }$ ), $6 I _ { 2 }$ ( $6 A _ { 1 }$ ).
But $D _ { 6 } A _ { 1 }$ , $D _ { 4 } 2 A _ { 1 }$ , $2 A _ { 3 } A _ { 1 }$ , $A _ { 3 } 3 A _ { 1 }$ and $5 A _ { 1 }$ are sublattices of $E _ { 7 }$ and $3 A _ { 2 }$ is a sublattice of $E _ { 6 }$ , all with cyclic cotorsion.

# 8. Applications and connections with other works

8A.
Toric compact moduli of rational elliptic surfaces.
Let $M _ { \mathrm { e l l } }$ be the moduli space of smooth rational elliptic relatively minimal surfaces $S \to \mathbb { P } ^ { 1 }$ with a section $E$ .
Let $M _ { \mathrm { e l l } } ( I _ { 1 } )$ be the moduli space of such surfaces $( S , E , F )$ together with a fixed $I _ { 1 }$ Kodaira fiber $F$ (i.e. a rational nodal curve).
This is a $1 2 : 1$ cover of a dense open subset of $M _ { \mathrm { e l l } }$ since a generic rational elliptic surface has $1 2 \ I _ { 1 }$ fibers.

Theorem 8.1. There exists a moduli compactification of $M _ { \mathrm { e l l } } ( I _ { 1 } )$ by stable slc pairs whose normalization is the quotient $V _ { \Lambda } ^ { \mathrm { s e m 1 } } / W _ { \Lambda }$ of the projective toric variety $V _ { \Lambda } ^ { \mathrm { s e m } }$ for the generalized Coxeter fan by the Weyl group $W _ { \Lambda }$ , where $\Lambda$ is the root lattice $E _ { 8 }$ .

Proof.
Let $j \colon S \to S$ be the elliptic involution with respect to the section $E$ and $E \sqcup R$ be the fixed locus of $j$ .
Contracting the $\left( - 2 \right)$ -curves in the fibers which are disjoint from the section $E$ and then $E$ itself gives a pair $( X , D + \epsilon R )$ which is an $A D E$ double cover of shape $E _ { 8 }$ .
Vice versa, any pair $( X , D + \epsilon R )$ of $E _ { 8 }$ shape is a del Pezzo surface of degree 1 with Du Val singularities.
Blowing up the unique base point of $\vert - K _ { X } \vert$ and resolving the singularities gives a rational elliptic fibration $S \to \mathbb { P } ^ { 1 }$ and the strict preimage of $D$ is an $I _ { 1 }$ fiber of this fibration.
This theorem is now the $E _ { 8 }$ case of Theorem 6.38. 

Similarly, the $E _ { 7 }$ compactified family gives a moduli compactification $M _ { \mathrm { e l l } } ( I _ { 2 } )$ of the moduli space $M _ { \mathrm { e l l } } ( I _ { 2 } )$ of rational elliptic surfaces with an $I _ { 2 }$ Kodaira fiber; the $E _ { 6 }$ family gives ${ \overline { { M } } } _ { \mathrm { e l l } } ( I _ { 3 } )$ ; the $D _ { 5 } ^ { - }$ family gives $\overline { { M } } _ { \mathrm { e l l } } ( I _ { 4 } )$ ; and the $' A _ { 4 } ^ { - }$ family gives ${ \overline { { M } } } _ { \mathrm { e l l } } ( I _ { 5 } )$ .

8B.
Moduli of Looijenga pairs after Gross-Hacking-Keel.
A Looijenga pair is a smooth rational surface $( \widetilde X , \widetilde D )$ such that $K _ { \widetilde { X } } + \widetilde { D } \sim 0$ and $\widetilde { D }$ is a cycle of rational curves.
In [GHK15], Gross-Hacking-Keel construct moduli of Looijenga pairs of a fixed type, given by the configuration of the rational curves $\widetilde { D }$ .
The result is as follows.
First, one defines the lattice $\Delta \subset \operatorname { P i c } { \tilde { X } }$ as the orthogonal to the irreducible components of $\widetilde { D }$ , and the torus $T _ { \Delta } = \mathrm { H o m } ( \Delta , \mathbb { C } ^ { * } )$ .
One glues several copies of this moduli torus along dense open subsets into a nonseparated scheme $U$ and divides it by a group Adm of admissible monodromies, including reflections in the $\left( - 2 \right)$ -curves appearing on some deformations of $( \widetilde X , \widetilde D )$ .
The non-separatedness is expected since $\widetilde { X }$ in this setup are smooth surfaces without a polarization.
The separated quotient of $[ U / \mathrm { A d m } ]$ is $[ T _ { \Delta } / \mathrm { A d m } ]$ .

For an $A D E$ double cover $( X , D { + } \epsilon R )$ , the minimal resolution of singularities $( \widetilde X , \widetilde D )$ is a Looijenga pair.
In Theorems 5.9, 5.11, 5.12 we proved that the moduli space of $A D E$ pairs and of their double covers is a torus $T _ { \Lambda ^ { \prime } } = \mathrm { H o m } ( \Lambda ^ { \prime } , \mathbb { C } ^ { * } )$ modulo a certain Weyl group $W _ { \Lambda } \rtimes W _ { 0 }$ .
The lattices $\Lambda$ , $\Lambda ^ { \prime }$ and the Weyl groups $W _ { \Lambda }$ , $W _ { 0 }$ were introduced in Section 5. We now relate them to the lattices naturally associated to Looijenga pairs with a nonsymplectic involution.

Definition 8.2. Let $( \widetilde X , \widetilde D )$ be a Looijenga pair with an involution.
Let $\Delta = \widetilde { D } ^ { \perp }$ be the sublattice of $\operatorname { P i c } \tilde { X }$ which is orthogonal to the curves in the boundary.
Assume that there is an involution $\iota \colon { \widetilde { X } } \to { \widetilde { X } }$ with $\iota ( \tilde { D } ) = \tilde { D }$ .
We define $\Delta _ { + }$ and $\Delta _ { - }$ as the $( \pm 1 )$ -eigensublattices of the induced involution $\iota ^ { * } \colon \Delta \  \ \Delta$ .
Denote by ${ \Delta } _ { - } ^ { ( 2 ) }$ the set of $\left( - 2 \right)$ -vectors in $\Delta _ { - }$ , and by $W _ { - } ^ { ( 2 ) }$ the group generated by reflections in them.

Theorem 8.3. Let $( Y , C + \textstyle { \frac { 1 + \epsilon } { 2 } } B )$ be an $A D E$ pair and $( X , D + \epsilon R )$ be its double cover, with the minimal resolution $( \widetilde X , \widetilde D )$ .
Then one has $\Lambda = \Delta _ { - }$ and $W _ { \Lambda } = W _ { - } ^ { ( 2 ) }$ .
Further, $\Lambda ^ { \prime } \subset \Delta / \Delta _ { + }$ , with −equality if and only if the shape has no doubly primed sides.
For a doubly primed shape $S ^ { \prime \prime }$ (resp.
$^ { \prime \prime } S$ ), $\Delta / \Delta _ { + }$ is the same as for the shape $S ^ { \prime }$ (resp.
$^ { \prime } S$ ); it thus contains $\Lambda ^ { \prime }$ as a sublattice of index $2 ^ { N }$ , where $N$ is the number of sides on which the shape has a double prime.

Proof.
We prove the statement in representative $D$ cases, with the other cases done by similar computations.

$\left( D _ { 2 n } \right)$ The easiest model for a generic surface $X = { \overset { \sim } { X } }$ of this shape is as a blowup of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ divisorby theacts by with a section $s$ and a fiber $f$ at $2 n$ points lying on a curve in $\vert 2 s + f \vert$ .
Using $e _ { i }$ for the exceptional Thenam.
and s generatede involutionis the root $\operatorname { P i c } X$ $\begin{array} { r } { D _ { 1 } \sim 2 s + f - \sum _ { i = 1 } ^ { 2 n } e _ { i } } \end{array}$ $D _ { 2 } \sim f$ $\Delta$ $e _ { i } - e _ { i + 1 }$ $1 \leq i \leq 2 n - 1$ $f - e _ { 1 } - e _ { 2 }$ $D _ { 2 n }$ $f \mapsto f$ $\begin{array} { r } { s \mapsto s + n f - \sum _ { i = 1 } ^ { 2 n } e _ { i } } \end{array}$ $e _ { i } \mapsto f - e _ { i }$ $( - 1 )$ $\Delta$ $\Delta _ { - }$ $\Lambda$ $D _ { 2 n }$ $\Delta _ { + } = 0$ $\Delta / \Delta _ { + } = \Delta _ { - } = \Lambda = \Lambda ^ { \prime }$

$( D _ { 2 n } ^ { \prime } )$ The surface $X$ is obtained from the one for $D _ { 2 n }$ by a blowup at one of the two points in $R \cap D _ { 2 }$ .
Denoting by $g$ the exceptional divisor, one has $\begin{array} { r } { D _ { 1 } \sim 2 s + f - \sum _ { i = 1 } ^ { 2 n } e _ { i } } \end{array}$ , and $D _ { 2 } \sim f - g$ .
The lattice $\Delta$ is generated by the $2 n$ roots above and an additional root $\beta = s - e _ { 1 } - g$ .
This forms a Dynkin diagram obtained by attaching an additional node $\beta$ to one of the short legs of $D _ { 2 n }$ , $\alpha ^ { \prime }$ or $\alpha ^ { \prime \prime }$ .
Without loss of generality, let us say $\beta \alpha ^ { \prime } = 1$ .
The involution $\iota$ acts on the vectors $s , f , e _ { i }$ the same way as above, and $\iota ^ { * } g = g$ .
Thus, $\Delta _ { + }$ is spanned by the vector $t = \beta + \iota ^ { * } \beta$ and $\Delta _ { - }$ is the same $D _ { 2 n }$ root lattice as before.
We have an orthogonal projection $p \colon \Delta  { \frac { 1 } { 2 } } \Delta _ { - }$ identifying $\Delta / \Delta _ { + }$ with a sublattice of ${ \scriptstyle { \frac { 1 } { 2 } } } \Delta _ { - }$ generated by $\Delta _ { - }$ and the image $p ( \beta )$ .
For a root $\alpha \in \Delta _ { - }$ one has $p ( \beta ) \alpha = \beta \alpha$ , so $\beta \alpha ^ { \prime } = 1$ and $\beta r = 0$ for the other roots $\alpha$ .
Thus, $p ( \beta ) = \varpi ^ { \prime }$ , the fundamental weight $\varpi ^ { \prime }$ for the root $\alpha ^ { \prime }$ , and $\Delta / \Delta _ { + } = \Lambda + \varpi ^ { \prime }$ is our $\Lambda ^ { \prime }$ .

$( \prime D _ { 2 n } )$ The surfac.
Denotinhe lattice $X$ s obtained from the exceptionalenerated by the e one for visor agairoots abo $D _ { 2 n }$ by ane has nd an oints, and This $R \cap D _ { 1 }$ $g$ $\begin{array} { r } { D _ { 1 } \sim 2 s + f - \sum _ { i = 1 } ^ { 2 n } e _ { i } - g } \end{array}$ $D _ { 2 } \sim f$ $\Delta$ $2 n$ $\beta = e _ { 2 n } - g$ forms a Dynkin diagram obtained by attaching an additional node $\beta$ to the long leg of $D _ { 2 n }$ , i.e. to $\alpha _ { 2 n - 3 }$ in our notation.
The $( - 1 )$ -eigenspace $\Delta _ { - }$ is again the $D _ { 2 n }$ root lattice generated by the first $2 n$ roots.
The space $\Delta _ { + }$ is generated by $t = \beta + \iota ^ { * } \beta = f - 2 g$ .
The orthogonal projection $p$ identifies $\Delta / \Delta _ { + }$ with $\Delta _ { - } + p ( \alpha )$ .
And since one has $\beta \alpha _ { 2 n - 3 } = ~ 1$ and $\beta$ is orthogonal to the other $2 n - 1$ roots, $p ( \beta ) = \varpi _ { 2 n - 3 }$ .
So one has $\Delta / \Delta _ { + } = \Lambda + \varpi _ { 2 n - 3 } = \Lambda ^ { \prime }$ , as claimed.

( ${ \cal D } _ { 2 n } ^ { \prime } )$ Similarly, in $\Delta$ one has two extra roots $\beta _ { 1 } = s - e _ { 1 } - g _ { 1 }$ and $\beta _ { 2 } = e _ { 2 n } - g _ { 2 }$ whose images in ${ \frac { 1 } { 2 } } \Delta _ { - }$ are $\varpi ^ { \prime }$ or $\varpi ^ { \prime \prime }$ depending on the parity of $n$ , and $\varpi _ { 2 n - 3 } ^ { \prime }$ , so $\Delta / \Delta _ { + } = \Lambda ^ { \prime }$ again.

When priming a surface of shape $S$ twice on the same side (say on the right), there are two exceptional divisors $g _ { 1 } , g _ { 2 }$ .
Then $\Delta ( S ^ { \prime \prime } ) = \Delta ( S ^ { \prime } ) \oplus \mathbb { Z } ( g _ { 1 } - g _ { 2 } )$ , $\Delta _ { + } ( S ^ { \prime \prime } ) = \Delta _ { + } ( S ^ { \prime } ) \oplus \mathbb { Z } ( g _ { 1 } - g _ { 2 } )$ , $\Delta _ { - } ( S ^ { \prime \prime } ) = \Delta _ { - } ( S ^ { \prime } )$ .
Therefore, $\Delta / \Delta _ { + } ( S ^ { \prime \prime } ) = \Delta / \Delta _ { + } ( S ^ { \prime } )$ .
This applies to $D _ { 2 n } ^ { \prime \prime }$ , ${ } ^ { \prime \prime } D _ { 2 n }$ and all the other doubly primed shapes.


Next, we define an action of the Weyl group $W _ { 0 }$ of the lattice $\Lambda _ { 0 } = C ^ { \perp } \cap B ^ { \perp }$ introduced in Def.
3.31.

Definition 8.4. Let $\pi \colon X \to Y$ be an double cover of a $A D E$ pair with a branch divisor $B$ .
Let $\tilde { \pi } \colon \tilde { X }  \tilde { Y }$ be a double cover of its resolution of singularities.
Let $e \in \Lambda _ { 0 } ^ { ( 2 ) }$ be a cycle, so $e \in C ^ { \bot } \cap B ^ { \bot }$ and $e ^ { 2 } = - 2$ .
Then $\pi ^ { * } e = e _ { 1 } + e _ { 2 }$ with $\iota ^ { * } e _ { 1 } = e _ { 2 }$ , $e _ { 1 } ^ { 2 } = e _ { 2 } ^ { 2 } = - 2$ and $e _ { 1 } e _ { 2 } = 0$ .

We define $v _ { + } = \pi ^ { * } ( e ) = e _ { 1 } + e _ { 2 } \in \Delta _ { + }$ and $v _ { - } = e _ { 1 } - e _ { 2 } \in \Delta _ { - }$ .
The composition of two reflections $w _ { e _ { 1 } } \cup w _ { e _ { 2 } } = w _ { e _ { 2 } } \cup w _ { e _ { 1 } }$ acts on $\Delta _ { - }$ as a reflection $w _ { v _ { - } }$ in the $( - 4 )$ -vector $v _ { - }$ , and on $\Delta _ { + }$ as a reflection $w _ { v + }$ in the $( - 4 )$ -vector $v _ { + }$ .

Lemma 8.5. Given $e \in \Lambda _ { 0 }$ , $w _ { e _ { 1 } } \cup w _ { e _ { 2 } }$ is well defined up to a conjugation by $W _ { - } ^ { ( 2 ) }$ .

Proof.
Suppose we have another decomposition $v _ { + } = e _ { 1 } + e _ { 2 } = e _ { 1 } ^ { \prime } + e _ { 2 } ^ { \prime }$ .
One has $e _ { 1 } = \frac { _ { 1 } } { _ 2 } ( v _ { + } + v _ { - } )$ and $e _ { 1 } ^ { \prime } = \frac { _ { 1 } } { ^ { 2 } } ( v _ { + } + v _ { - } ^ { \prime } )$ .
Then $\begin{array} { r } { e _ { 1 } e _ { 1 } ^ { \prime } = - 1 + \frac { 1 } { 4 } v _ { - } v _ { - } ^ { \prime } } \end{array}$ .
Since $\Delta _ { - } \subset R ^ { \bot }$ and $R ^ { 2 } > 0$ , $\Delta _ { - }$ is negative 2definite.
Thus, $| v _ { - } v _ { - } ^ { \prime } | < 4$ 4 −, and we conclude that $e _ { 1 } e _ { 1 } ^ { \prime } = - 1$ − .
The elements $w _ { e _ { 1 } } \cup w _ { e _ { 2 } }$ − and $w _ { e _ { 1 } ^ { \prime } } \circ w _ { e _ { 2 } ^ { \prime } }$ are conjugate by the reflection $w _ { e _ { 1 } - e _ { 1 } ^ { \prime } } = w _ { e _ { 2 } - e _ { 2 } ^ { \prime } }$ .
Finally, $e _ { 1 } - e _ { 1 } ^ { \prime } \in \Delta _ { - }$ and $( e _ { 1 } - e _ { 1 } ^ { \prime } ) ^ { 2 } = - 2$ , so we1 e0 ∈ W (2).


Definition 8.6. We define the Weyl group $W _ { - } ^ { ( 2 , 4 ) }$ as the group of reflections of $\Delta$ generated by $W _ { - } ^ { ( 2 ) }$ and the elements $w _ { e _ { 1 } } \cup w _ { e _ { 2 } }$ for $e \in \Lambda _ { 0 }$ .
By the above, it preserves both $\Delta _ { - }$ and $\Delta _ { + }$ , with $W _ { - } ^ { ( 2 ) }$ acting trivially on $\Delta _ { + }$ .
Thus, we have the induced actions of $W _ { - } ^ { ( 2 , 4 ) }$ on $\Delta _ { - }$ and of $W _ { - } ^ { ( 2 , 4 ) } / W _ { - } ^ { ( 2 ) }$ on $\Delta _ { + }$ .

Theorem 8.7. One has $W _ { - } ^ { ( 2 , 4 ) } / W _ { - } ^ { ( 2 ) } = W _ { 0 }$ .
The subgroup $W _ { 0 0 }$ from Definition 5.14 is the subgroup of $W _ { 0 }$ which acts trivially on $\Delta _ { - }$ .

Proof.
We compute the action of $W _ { 0 }$ in the representative $D$ cases using the same notation as in the proof of Theorem 8.3. The lattice $\Delta _ { + } \cap R ^ { \perp }$ can be identified with $\pi ^ { * } ( \Lambda _ { 0 } )$ and the $( - 4 )$ -vectors $v _ { + }$ in $\Delta _ { + } \cap R ^ { \perp }$ with the vectors $\pi ^ { * } ( e )$ for $e \in \Lambda _ { 0 } ^ { ( 2 ) }$ .

( $D _ { 2 n }$ ) $\Lambda _ { 0 } = 0$ and $\Delta _ { + } = 0$ ; there is nothing to check.
$( D _ { 2 n } ^ { \prime } )$ One has $t ^ { 2 } = 2 n - 8$ .
This equals $^ { - 4 }$ only for $n = 2$ and then $D _ { 4 } ^ { \prime } = D _ { 4 }$ .
$( \ d ^ { \prime } D _ { 2 n } )$ One has $\boldsymbol { \beta } \cdot \boldsymbol { \iota } ^ { * } \boldsymbol { \beta } = 0$ .
So for the generator $t = \beta + \iota ^ { * } \beta = f - 2 g$ of $\Delta _ { + }$ one has $t ^ { 2 } = - 4$ .
Indeed, $t = v _ { + } = \pi ^ { * } e$ for the generator $e$ of $\Lambda _ { 0 }$ .
Then $v _ { - } = \beta - \iota ^ { * } \beta = 2 e _ { 2 n } - f$ .
Reflection $w _ { v _ { - } }$ in this vector fixes all roots of the $D _ { 2 n }$ diagram except for $w _ { v _ { - } } ( \alpha _ { n - 3 } ) = \alpha : = e _ { 2 n - 1 } + e _ { 2 n } - f$ .
Together with the other $2 n$ roots, $\alpha$ forms the $\widetilde { D } _ { 2 n }$ diagram in which $\alpha _ { n - 3 }$ , $\alpha$ are two short legs.
Thus, $w _ { v _ { - } }$ acts as an outer automorphism of $\Lambda ( D _ { 2 n } )$ swapping two short legs.
This is the same action for $W _ { 0 } = S _ { 2 }$ which we computed in subsection 5F.

$( \mathbf { \boldsymbol { \mathbf { \mathit { \Pi } } } } ^ { \prime \prime } \mathbf { \boldsymbol { D } } _ { 2 n } )$ One has $\Delta _ { + } = \langle f - 2 g _ { 1 } , g _ { 2 } - g _ { 1 } \rangle$ .
The only vectors $v _ { + }$ of square $^ { - 4 }$ in $\Delta _ { + }$ are $f - 2 g _ { 1 }$ and $f - 2 g _ { 2 }$ $v _ { - } = 2 e _ { 2 n } - f$ , which are the pullbacks of the two vectors in .
Thus, $w _ { e _ { 1 } } ^ { ( 1 ) } \circ w _ { e _ { 2 } } ^ { ( 1 ) }$ and $w _ { e _ { 1 } } ^ { ( 2 ) } \circ w _ { e _ { 2 } } ^ { ( 2 ) }$ w(2)e2 for these two vectors act in the same way on ∆− ${ \Lambda } _ { 0 } ^ { ( 2 ) }$ .
For both of them we get the same vector but differently on $\Delta _ { + }$ .
We conclude that they generate $S _ { 2 } \times S _ { 2 }$ and their difference acts trivially on $\Delta _ { - }$ .
This is the same description of $W _ { 0 } = S _ { 2 } \times S _ { 2 }$ and $W _ { 0 0 } = S _ { 2 }$ as in 5F.

$( D _ { 4 } ^ { \prime } ) ~ \pi ^ { * } \Lambda _ { 0 }$ is generated by $v _ { + } ^ { 1 } = \beta _ { 1 } + \iota ^ { * } \beta _ { 1 }$ and $v _ { + } ^ { 2 } = \beta _ { 2 } + \iota ^ { * } \beta _ { 2 }$ , $\beta _ { 1 } = s - e _ { 1 } - g _ { 1 }$ and $\beta _ { 2 } = e _ { 4 } - g _ { 2 }$ .
Then $v _ { - } ^ { 1 } = - f - e _ { 1 } + e _ { 2 } + e _ { 3 } + e _ { 4 }$ and $v _ { - } ^ { 2 } = - f + 2 e _ { 4 }$ .
Denote by $- \alpha$ the highest root, so that together with the other 4 roots it forms the ${ \widetilde { D } } _ { 4 }$ diagram.
Then $w _ { v _ { - } ^ { 1 } }$ swaps $\alpha ^ { \prime }$ and $\alpha$ , and $w _ { v _ { - } ^ { 2 } }$ swaps $\alpha _ { 1 }$ and $\alpha$ .
Thus, $W _ { 0 }$ acts as the group $S _ { 3 }$ of outer automorphisms of $\Lambda ( D _ { 4 } )$ , the same as in 5F.
$\boxed { \begin{array} { r l } \end{array} }$

We now describe, without proof, how our moduli stack of $A D E$ pairs (equivalently, up to the $\mu _ { 2 }$ -cover, the stack of $A D E$ double covers with involution), which by Theorem 5.12 equals $\left[ T _ { \Lambda ^ { \prime } } \right. : :$ $W _ { \Lambda } \rtimes W _ { 0 } ]$ , is related to the moduli of Looijenga pairs.
In the moduli torus $T _ { \Delta }$ of Looijenga pairs the subtorus $T _ { \Delta / \Delta _ { + } }$ corresponds to the pairs admitting a nonsymplectic involution.
The moduli stack is the quotient of it by the group of admissible monodromies of $T _ { \Delta }$ leaving $T _ { \Lambda ^ { \prime } }$ invariant.
A part of this group is obvious: reflections $W _ { - } ^ { ( 2 ) }$ in the vectors in ${ \Delta } _ { - } ^ { ( 2 ) }$ .
Also, for each side which has a double prime there is a root $g _ { 1 } - g _ { 2 }$ which gives a quotient by $\mu _ { 2 }$ that forgets the ordering of the two primed points.
This accounts for the fact that $\Lambda ^ { \prime }$ is a sublattice of $\Delta / \Delta _ { + }$ for shapes with doubly primed sides.
Less obviously, for each $e \in \Lambda _ { 0 } ^ { ( 2 ) }$ , with $\pi ^ { * } ( e ) = e _ { 1 } + e _ { 2 }$ , while the reflections $w _ { e _ { 1 } }$ and $w _ { e _ { 2 } }$ by themselves do not fix $\Delta _ { - }$ , their composition $w _ { e _ { 1 } } \cup w _ { e _ { 2 } }$ does.

One thus takes a quotient of $T _ { \Lambda ^ { \prime } }$ by $W _ { - } ^ { ( 2 ) } = W _ { \Lambda }$ followed by a quotient by $W _ { - } ^ { ( 2 , 4 ) } / W _ { - } ^ { ( 2 ) } = W _ { 0 }$ The subgroup $W _ { 0 0 } \subset W _ { - } ^ { ( 2 , 4 ) } / W _ { - } ^ { ( 2 ) }$ acts trivially on the coarse moduli space $T _ { \Lambda ^ { \prime } }$ but nontrivially on the stack, giving extra automorphisms of the pairs.

8C.
Involutions in the Cremona group.
Classically, the involutions in the Cremona group $\operatorname { C r } ( \mathbb { P } ^ { 2 } )$ , the group of birational automorphisms of $\mathbb { P } ^ { 2 }$ , are of three types: De Jonqui\`eres, Geiser, and Bertini.
For a nice modern treatment that uses equivalent MMP, see [BB00].
For a $( K + D )$ -trivial polarized involution pair $( X , D , \iota )$ , if $X$ is rational then $\iota$ is an involution in $\mathrm { C r } ( \mathbb { P } ^ { 2 } )$ .

Theorem 8.8. Let $( X , D , \iota )$ be $a$ $( K + D )$ -trivial polarized involution pair with rational surface $X$ and a smooth ramification curve $R$ .
Then

(1) If $( X , D , \iota )$ is of shape $\widetilde { D }$ , $D$ , or $A$ (pure or primed) then ι is De Jonqui\`eres.  
(2) If it is of shape ${ \widetilde { E } } _ { 7 }$ , $E _ { 7 }$ , or $E _ { 6 }$ (pure or primed) then ι is Geiser.  
(3) If it is of shape ${ \widetilde { E } } _ { 8 }$ or $E _ { 8 }$ (pure or primed) then ι is Bertini.

Proof.
By [BB00, Prop. 2.7], the type of the involution is uniquely determined by the normalization $\widetilde { R }$ of the ramification curve $R$ : for De Jonqui\`eres $\widetilde { R }$ is hyperelliptic, for Geiser it is non-hyperelliptic of genus 3, and for Bertini it is non-hyperelliptic of genus 4. In the $\widetilde { D }$ - $D$ - $A$ cases the branch curve $B \simeq R$ is a two-section of a ruling, so it is hyperelliptic.
In the ${  { \widetilde { E } } } _ { 7 }$ - $E _ { 7 }$ - $E _ { 6 }$ cases $R$ is a quartic curve in $\mathbb { P } ^ { 2 }$ , so a non-hyperelliptic curve of genus 3, and in the ${ \widetilde { E } } _ { 8 }$ - $E _ { 8 }$ cases it is a section of $\mathcal { O } ( 1 )$ on the quadratic cone $\mathbb { F } _ { 2 } ^ { \mathrm { { u } } }$ , so a non-hyperelliptic curve of genus 4. 

Remark 8.9. When $R$ has nodes, the involution may easily be of a different type.
When it has $\geq 2$ nodes, the involution is always De Jonqui\`eres.

We can give an alternative proof for the classification of the double covers $( X , D ) \to ( Y , C )$ of log canonical non-klt surfaces using [BB00] in some cases:

Theorem 8.10. Let $( X , D , \iota )$ be a $( K + D )$ -trivial polarized involution pair with rational $X$ .
Suppose that $X$ is smooth outside of the boundary $D$ , and in particular that the ramification curve $R$ is smooth.
Then the quotient $( Y , C )$ of this pair is an $A D E$ or $\widetilde A D E$ surface defined in Section 3.

Sketch of the proof.
Let $\widetilde { X }$ be the minimal resolution of $X$ , it comes with an induced involution $\ddot { \iota }$ .
[BB00, Thm. 1.4] gives six possibilities for the pair $( \widetilde X , \tilde { \iota } )$ when it is minimal, i.e. there does not exist one or two $( - 1 )$ -curves that can be equivariantly contracted to another smooth surface with an involution.
In our case, $\widetilde { X }$ is obtained from such a minimal surface by a sequence of single or double blowups which satisfy two conditions: they have to be involution-invariant, and there are no $\left( - 2 \right)$ -curves disjoint from $B$ .

It follows that $\widetilde { X }$ is obtained by blowups at the points $B \cap R$ , either one involution-invariant point or two points exchanged by the involution.
We analyze them directly.
The different cases of [BB00, Thm. 1.4] then lead to the following:

(i) impossible, i.e. does not lead to a $( K + D )$ -trivial polarized involution pair with ample $R$ .  
(ii) $( i i ) _ { \mathrm { s m } }$ is impossible, and $( i i ) _ { g }$ gives the $\widetilde { D }$ - $D$ - $A$ shapes.  
(iii) $A _ { 0 } ^ { - }$ and $\widetilde { A } _ { 0 } ^ { - }$ .  
(iv) $\widetilde { A } _ { 1 } ^ { * }$ , $A _ { 1 }$ .  
(v) ${  { \widetilde { E } } } _ { 7 }$ , ${ } ^ { - } E _ { 7 }$ , $^ - E _ { 6 } ^ { - }$ and the primed shapes.  
(vi) ${ \widetilde { E } } _ { 8 } ^ { - }$ , $^ - E _ { 8 } ^ { - }$ and the primed shapes.

One could try to extend the results of this section to classify families of log del Pezzo pairs, in which the surface $Y$ may acquire singularities away from the boundary.
This would give an alternative proof of Theorem A.
For this, we would first need to know that the branch divisor $B$ can be smoothed.
This is known, see [Nak07, Cor.3.20].
Secondly, we would also need to know that the singular points of the surface $Y$ away from the boundary can be smoothed.
For surfaces without the boundary, this is [HP10, Prop. 3.1].
For the pairs $( Y , C )$ with boundary this does not seem to be easy to prove directly.
This follows a posteriori from the classification of all log del Pezzo surfaces with boundary given in Sections 3 and 4.

# References

[AET19] Valery Alexeev, Philip Engel, and Alan Thompson, Stable pair compactification of moduli of K3 surfaces of degree 2, Preprint (2019), arXiv:1903.09742.  
[Ale02] Valery Alexeev, Complete moduli in the presence of semiabelian group action, Ann.
of Math.
(2) 155 (2002), no.
3, 611–708.  
[Ale06] Higher-dimensional analogues of stable curves, International Congress of Mathematicians.
Vol.
II, Eur.
Math.
Soc., Z¨urich, 2006, pp.
515–536.  
[AN88] Valery Alexeev and V.
V.
Nikulin, Classification of del Pezzo surfaces with log-terminal singularities of index $\leq 2$ , involutions on K3 surfaces, and reflection groups in Lobachevski˘ı spaces, Lectures in mathematics and its applications, Vol.
2, No.
2 (Russian), Ross.
Akad.
Nauk V.
A.
Steklov Inst.
Mat., Moscow, 1988, pp.
51–150.  
[AN89] , Classification of del Pezzo surfaces with log-terminal singularities of index $\leq 2$ and involutions on $_ { K 3 }$ surfaces, Dokl.
Akad.
Nauk SSSR 306 (1989), no.
3, 525–528.  
[AN06] Valery Alexeev and Viacheslav V.
Nikulin, Del Pezzo and K3 surfaces, MSJ Memoirs, vol.
15, Mathematical Society of Japan, Tokyo, 2006.  
[Arn72] V.
I.
Arnol0d, Normal forms of functions near degenerate critical points, the Weyl groups $A _ { k } , D _ { k } , E _ { k }$ and Lagrangian singularities, Funkcional.
Anal.
i Priloˇzen.
6 (1972), no.
4, 3–25.  
[BB00] Lionel Bayle and Arnaud Beauville, Birational involutions of $\mathbf { P } ^ { 2 }$ , Asian J.
Math.
4 (2000), no.
1, 11–17, Kodaira’s issue.  
[BB11] Victor Batyrev and Mark Blume, On generalisations of Losev-Manin moduli spaces for classical root systems, Pure Appl.
Math.
Q.
7 (2011), no.
4, Special Issue: In memory of Eckart Viehweg, 1053–1084.  
[Bou05] Nicolas Bourbaki, Lie groups and Lie algebras.
Chapters 7–9, Elements of Mathematics (Berlin), SpringerVerlag, Berlin, 2005, Translated from the 1975 and 1982 French originals by Andrew Pressley.  
[Dol12] Igor V.
Dolgachev, Classical algebraic geometry, Cambridge University Press, Cambridge, 2012, A modern view.  
[DPT80] Michel Demazure, Henry Charles Pinkham, and Bernard Teissier (eds.), S´eminaire sur les Singularit´es des Surfaces, Lecture Notes in Mathematics, vol.
777, Springer, Berlin, 1980, Held at the Centre de Math´ematiques de l’Ecole Polytechnique, Palaiseau, 1976–1977.
´  
[Dyn52] E.
B.
Dynkin, Semisimple subalgebras of semisimple Lie algebras, Mat.
Sbornik N.S.
30(72) (1952), 349–462 (3 plates).  
[EOR07] Pavel Etingof, Alexei Oblomkov, and Eric Rains, Generalized double affine Hecke algebras of rank 1 and quantized del Pezzo surfaces, Adv.
Math.
212 (2007), no.
2, 749–796.  
[Fuj12] Osamu Fujino, Minimal model theory for log surfaces, Publ.
Res.
Inst.
Math.
Sci.
48 (2012), no.
2, 339–371.  
[GHK15] Mark Gross, Paul Hacking, and Sean Keel, Moduli of surfaces with an anti-canonical cycle, Compos.
Math.
151 (2015), no.
2, 265–291.  
[Hac04a] P.
Hacking, Compact moduli of plane curves, Duke Math.
J.
124 (2004), no.
2, 213–257.  
[Hac04b] Paul Hacking, A compactification of the space of plane curves, Preprint (2004), arXiv:math/0104193.  
[HP10] Paul Hacking and Yuri Prokhorov, Smoothable del Pezzo surfaces with quotient singularities, Compos.
Math.
146 (2010), no.
1, 169–192.  
[Kol13] J´anos Koll´ar, Singularities of the minimal model program, Cambridge Tracts in Mathematics, vol.
200, Cambridge University Press, Cambridge, 2013, With a collaboration of S´andor Kov´acs.  
[Kol15] Book on moduli of surfaces ongoing project, 2015, Available at https://web.math.princeton.edu/˜kollar.  
[KSB88] J.
Koll´ar and N.
I.
Shepherd-Barron, Threefolds and deformations of surface singularities, Invent.
Math.
91 (1988), no.
2, 299–338.  
[LM00] A.
Losev and Y.
Manin, New moduli spaces of pointed curves and pencils of flat connections, Michigan Math.
J.
48 (2000), 443–472.  
[MP86] Rick Miranda and Ulf Persson, On extremal rational elliptic surfaces, Math.
Z.
193 (1986), no.
4, 537–558.  
[Nak07] Noboru Nakayama, Classification of log del Pezzo surfaces of index two, J.
Math.
Sci.
Univ.
Tokyo 14 (2007), no.
3, 293–498.  
[Per90] Ulf Persson, Configurations of Kodaira fibers on rational elliptic surfaces, Math.
Z.
205 (1990), no.
1, 1–47.  
[Sage17] The Sage Developers, Sagemath, the Sage Mathematics Software System (Version 7.5.1), 2017, http://www.sagemath.org.  
[Sho92] V.
V.
Shokurov, Three-dimensional log perestroikas, Izv.
Ross.
Akad.
Nauk Ser.
Mat.
56 (1992), no.
1, 105–203.  
[Ste98] John R.
Stembridge, The partial order of dominant weights, Adv.
Math.
136 (1998), no.
2, 340–364.  
[Tju70] G.
N.
Tjurina, Resolution of singularities of flat deformations of double rational points, Funkcional.
Anal.
i Priloˇzen.
4 (1970), no.
1, 77–83.

# List of Tables

1 Polytopes for the pure shapes 9

2 All $A D E$ shapes 15

3 All $\widetilde A D E$ shapes 16

4 Polytopes for the toric primed shapes 16

5 Normal forms for the equation $f = f _ { \mathrm { b d r y } } + f _ { \mathrm { d y n } }$ of divisor $B$ 26

6 Partial order on dominant weights of $E _ { 8 }$ below $\varpi _ { 0 }$ 44

7 For $E _ { 8 }$ , the dominant weights $\lambda < \varpi$ in $c$ which survive degenerations 45

List of Figures

1 $A$ shapes: $A _ { 3 }$ , −A −3 , A −2 , A −0 9

$D$ shapes: $D _ { 4 }$ , $D _ { 5 } ^ { - }$ , $D _ { 6 }$ 9

$E$ shapes: −E−6 , −E7, −E−8 9

4 Type II shapes ${ \widetilde { D } } _ { 8 }$ , ${  { \widetilde { E } } } _ { 7 }$ and ${ \widetilde { E } } _ { 8 } ^ { - }$ 10

5 Nontoric type II $\widetilde { A }$ shapes: ${ \widetilde { A } } _ { 5 }$ , $\stackrel { \sim } { A } _ { 1 }$ , ${ \widetilde { A } } _ { 1 } ^ { * }$ , $\widetilde { A } _ { 0 } ^ { - }$ 11

6 Decorated Dynkin diagrams for shapes $' / A _ { 3 } ^ { \prime }$ , ${ } ^ { \prime \prime } D _ { 5 } ^ { + }$ , ${ \widetilde { E } } _ { 8 } ^ { + \prime }$ 14

7 Toric $A$ shapes: $A _ { 2 } ^ { - } = \bar { { } A } _ { 2 } ^ { \prime } = \bar { { } - } D _ { 2 } ^ { - }$ , $\mathrm { { \mathit { A } } _ { 3 } }$ , $' A _ { 4 } ^ { - }$ 14

8 Toric $D ^ { \prime }$ and $A ^ { \prime }$ shapes: $D _ { 8 } ^ { \prime }$ , ${ \mathit { A } } _ { 5 } ^ { \prime }$ , ${ \mathrm { \Delta } } ^ { \prime } A _ { 7 } ^ { \prime }$ 16

9 Some special toric surfaces in shapes $\mathcal { D } _ { 7 } ^ { - }$ , ${ \cal { D } } _ { 4 } ^ { \prime }$ 16

10 Singularities $( n _ { 1 } , n _ { 2 } , . . . , n _ { k } ; 2 ^ { 2 } )$ and $( 2 ^ { 2 } ; n _ { 1 } , n _ { 2 } , \ldots , n _ { k } ; 2 ^ { 2 } )$ 17

11 Effect of eliminating simple subschemes 21

12 $A _ { 2 } ^ { - }$ and its degenerations: $A _ { 0 } ^ { - } \bar { A } _ { 1 } ^ { - }$ , $A _ { 1 } A _ { 0 } ^ { - }$ , and $A _ { 0 } ^ { - } \bar { A } _ { 0 } A _ { 0 } ^ { - }$ 31

13 $D _ { 4 }$ and its degenerations $A _ { 0 } ^ { - } A _ { 3 }$ , $A _ { 1 } A _ { 1 }$ , $A _ { 3 } ^ { \prime } \ { \overline { { A } } } _ { 0 }$ , $A _ { 3 }$ 33

E-mail address: valery@uga.edu

Department of Mathematics, University of Georgia, Athens GA 30602, USA

$E$ -mail address: a.m.thompson@lboro.ac.uk

Department of Mathematical Sciences, Loughborough University, Loughborough, Leicestershire, LE11 3TU, UK