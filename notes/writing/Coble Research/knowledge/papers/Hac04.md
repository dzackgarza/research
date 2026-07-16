---
title: Coble rational surfaces
authors:
- Dolgachev
year: 1999
bibkey: Hac04
tags:
- paper
- extraction
abstract: |
  
---

# COBLE RATIONAL SURFACES

Igor V.
Dolgachev and De-Qi Zhang

# Introduction

A Coble surface is a nonsingular projective rational surface $S$ with empty anticanonical linear system $| - K _ { S } |$ but non-empty bi-anticanonical system $\vert - 2 K _ { S } \vert$ .
A classical example of such surface is the blow-up of $\mathbb { P } ^ { 2 }$ at 10 nodes of an irreducible rational plane curve of degree 6 with ordinary nodes as singularities.
Rational plane sextics of this kind were intensively studied by A.
Coble [Co1,Co2].
Among other things he showed that a Cremona equivalence classe of such curve is the union of finitely many projective equivalence classes (see [Co2],[MS]).
This result can be interpreted as saying that the automorphism group of the associated Coble surface is isomorphic to a subgroup of finite index in the orthogonal group of the lattice $M _ { S } = ( K _ { S } ) _ { \mathrm { P i c } ( S ) } ^ { \perp }$ .
In fact, Coble shows that for a general sextic with 10 nodes this group is isomorphic to the congruence subgroup of level 2 of the group $O ( M _ { S } ) / \{ \pm 1 \}$ (see [Do2]).
The latter group is isomorphic to the Weyl group of infinite root system of type $E _ { 1 0 }$ .
A similar answer is known for a generic Enriques surface.
It was obtained much later by V.
Nikulin [Ni] and independently W.
Barth and C.
Peters [BP].

The connection between classical Coble surfaces and Enriques surfaces is a nice one: a double cover of a Coble surface branched along the proper transform of a reduced sextic is a K3 surface which is a degeneration of the K3-cover of an Enriques surface.
More geometrically, the embedding of a Coble surface in $\mathbb { P } ^ { 5 }$ defined by the linear system of curves of degree 10 with singular points of multiplicity 3 at the 10 nodes of the sextic is a surface of degree 10 which is a projective degeneration of an Enriques surface in its Fano embedding in $\mathbb { P } ^ { 5 }$ .

Another result of Coble is that the set of rational smooth curves with negative self-intersection on the blow-up of ten nodes of an irreducible sextic is finite modulo the automorphism group [Co2].
It is known that the same fact is true for all minimal non-rational algebraic surfaces [DP] and it is not true for any general blow-up of $\geq 9$ points in $\mathbb { P } ^ { 2 }$ .
This makes some (not all, as we shall see) of Coble surfaces exceptional in this respect.
In fact, this work in which we classify all Coble surfaces was partially motivated by the problem to classify all rational surfaces with finitely many smooth rational curves of negative self-intersection modulo automorphisms of the surface.

The classification of Coble surfaces is related to other classification problems.
To be precise, when $\mid - 2 K _ { S } \mid$ contains a reduced divisor, the double cover branched along this divisor is a normal K3 surface with an involution.
The classification of K3-surfaces with an involution can be found in [Zh3] extending some earlier results of Nikulin [Ni].
In particular, a terminal Coble surface is the minimal resolution of a maximum rational log Enriques surface of index 2 in the sense of [Zh2, OZ] (cf.
Proposition 6.4). The latter surfaces were classified in [Zh1, Zh2].

Let us describe the main results of this paper.
First of all we divide Coble surfaces into two major classes.
For a surface of the first class (elliptic type; cf.
2.9) there exists a birational morphism onto a surface $Y$ such that the anticanonical linear system $| - K _ { Y } |$ has only one member, and a general member of the mobile part of $\mid - 2 K _ { Y } \mid$ is a smooth elliptic curve.
Surfaces of the second class (rational type) admit a similar birational morphism only this time the mobile part of $ { - 2 K } _ { Y } \vert$ consists of divisors of arithmetic genus 0 (not necessarily irreducible).
We show that Coble surfaces of elliptic type are obtained as either blow-ups of singular points and their infinitely near points of a non-multiple fibre on a minimal rational elliptic surface with one multiple fibre of multiplicity 2 (Halphen type), or as blow-downs of some disjoint sections and maybe components of one fibre of a non-minimal rational elliptic surface with a section (Jacobian type).
We also give a construction for surfaces of rational type as blow-ups of minimal rational surfaces.
It turns out that surfaces of elliptic type always admit a birational morphism to $\mathbb { P } ^ { 2 }$ .
However, for any given $_ n$ there are Coble surfaces of rational type which do not admit a birational morphism to the minimal ruled surface ${ \bf F } _ { n }$ .
We prove that Coble surfaces of elliptic type are obtained by blowing up $\mathbb { P } ^ { 2 }$ with centers at singular points of certain plane curves $\Gamma$ of degree 6 (Coble sextics), but the center of the very last blow up may not be on $\Gamma$ .
We describe such sextics.

An important class of Coble surfaces $X$ to which the original example of Coble belongs is the one where the linear system $\mid - 2 K _ { X } \mid$ contains a reduced divisor.
In this case $X$ admits a double cover which is a K3-surface with at most ordinary double points.
We prove, under an appropriate condition of generality, that surfaces of this kind contain only finitely many smooth rational curves with negative intersection modulo automorphisms of the surface.
We show in Example 6.10, that this statement cannot be extended to all Coble surfaces.
It is possible that every Coble surface of rational type contains only finitely many negative rational curves; however we could not prove it.

(1) $p _ { a } ( D ) = h ^ { 0 } ( D + K _ { V } )$ ; in particular, $p _ { a } ( D _ { 1 } ) \leq p _ { a } ( D )$ if $D _ { 1 } \leq D$ .
(2) Pfm (D )> 1 (ear Vrhen theduel e,pnh efD- Panteina e leen) then m $( \Gamma \setminus \{ 0 , \} ) \setminus \{ 0 , \} $

Finally a word about the ground field $k$ .
We assume it to be algebraically closed, though most of the paper does not use any assumption on the characteristic.
However Theorem 6.7 assumes that $k = \mathbb { C }$ (with more efforts one can give another proof which does not use this assumption) and we assume that $k$ is uncountable in Example 6.10.

Acknowledgement.
This joint work was done during the second author’s visit at University of Michigan in Summer of 1999, who would like to thank its Department of Mathematics for the hospitality.
The first author would like to acknowledge the support and hospitality of the Mathematical Sciences Research Institute at Berkeley during June of 1999.

# 1. Some preliminary results

1.1 We shall consider an order on the set of Coble surfaces defined by dominant birational morphisms $f : X ^ { \prime } \to X$ .
Thus we can speak about a minimal Coble surface $X$ (which does not admit a birational, but not biregular, morphism onto another Coble surface) and a terminal Coble surface which is not the image of any birational but not biregular morphism of Coble surfaces.

We shall see that there exist minimal and terminal Coble surfaces, as well as non-minimal or nonterminal Coble surfaces (Example 2.6). It follows from the Riemann-Roch theorem that $K _ { X } ^ { 2 } \le - 1$ for any Coble surface.
Hence a Coble surface with $K _ { X } ^ { 2 } = - 1$ is always minimal.
We shall see that there are also minimal Coble surfaces with $K _ { X } ^ { 2 } < - 1$ (Example 4.9).

In the next paragraphs we shall give some conditions for a Coble surface to be minimal.

1.2 For any positive divisor $\boldsymbol { D }$ on a nonsingular projective surface $V$ we set

$$
p _ { a } ( D ) = \frac { 1 } { 2 } ( D ^ { 2 } + K _ { V } \cdot D ) + h ^ { 0 } ( \mathcal { O } _ { D } ) = h ^ { 1 } ( \mathcal { O } _ { D } ) .
$$

Here the last equality follows from Riemann-Roch, applied to the divisor $D + K _ { V }$ .

Lemma.
Assume $h ^ { 1 } ( { \mathcal { O } } _ { V } ) = h ^ { 2 } ( { \mathcal { O } } _ { V } ) = 0$ , for example, $V$ is a rational surface.
Then we have:

Proof.
We only need to show the first part of (1).
It follows from considering the exact sequence

$$
0 \to { \mathcal { O } } _ { V } ( - D ) \to { \mathcal { O } } _ { V } \to { \mathcal { O } } _ { D } \to 0 .
$$

Indeed, the sequence implies that $H ^ { 1 } ( D , { \mathcal { O } } _ { D } ) \cong H ^ { 2 } ( V , { \mathcal { O } } _ { V } ( - D ) ) = H ^ { 0 } ( V , { \mathcal { O } } ( D + K _ { V } ) .$

1.3 The part $h ^ { 0 } ( { \mathcal { O } } _ { D } )$ in (1.1) is often hard to compute.
We only cite the following useful results which can be found for example in $[ \mathrm { R e } ]$ , p.81.
Recall that an effective divisor is called numerically $k$ -connected, if for any decomposition $D = D _ { 1 } + D _ { 2 }$ into positive parts, we have $D _ { 1 } \cdot D _ { 2 } \geq k$ .

# Lemma.

(1) Let $0 < D ^ { \prime } < D$ .
Then there is an exact sequence

$$
0 \to \mathcal { O } _ { D - D ^ { \prime } } ( - D ^ { \prime } ) \to \mathcal { O } _ { D } \to \mathcal { O } _ { D ^ { \prime } } \to 0 .
$$

(2) Assume that $D$ is numerically 1-connected.
Then

$$
h ^ { 0 } ( { \mathcal { O } } _ { D } ) = 1 .
$$

(3) In particular, let $D _ { i } > 0$ such that $D _ { 1 } + D _ { 2 }$ is reduced and $D _ { 1 } , D _ { 2 } , D _ { 1 } + D _ { 2 }$ are all numerically 1-connected.
Then

$$
p _ { a } ( D _ { 1 } + D _ { 2 } ) = p _ { a } ( D _ { 1 } ) + p _ { a } ( D _ { 2 } ) + D _ { 1 } \cdot D _ { 2 } - 1 .
$$

Lemma 1.4. Let $X$ be a Coble surface.
Then any member $D$ of $\vert - 2 K _ { X } \vert$ consists of smooth rational curves and is of simple normal crossing.

Proof.
If Lemma 1.4 is false, then $D$ contains a reduced connected divisor $D _ { 1 }$ such that either $D _ { 1 }$ is irreducible with arithmetic genus $\geq 1$ , or $D _ { 1 }$ is a loop, or $D _ { 1 }$ is the sum of two curves with an order $\geq 2$ contact at a point, or $D _ { 1 }$ is the sum of 3 curves sharing one point.
This leads to $1 \leq p _ { a } ( D _ { 1 } ) \leq p _ { a } ( D ) = h ^ { \cup } ( - K _ { X } ) = 0$ (Lemma 1.2), a contradiction.
Hence Lemma 1.4 is true.

By an exceptional curve we shall mean a one-dimensional fibre of a birational morphism between nonsingular projective surfaces.
An irreducible exceptional curve is a $( - 1 )$ -curve.
Here by a $\left( - n \right)$ - curve we mean a smooth rational curve $R$ with $R ^ { 2 } = - n < 0$ .

1.5 Lemma.
Let $\pi : X \to Y$ be the blow-down of a $( - 1 )$ -curve $E$ on a smooth rational surface $X$ to a point $q$ on $Y$ .

(1) Suppose that $X$ is a Coble surface.
Then for any $D \in \vert - 2 K _ { X } \vert$ and any $s \geq 1$ , one has

$$
p _ { a } ( D + s E ) = h ^ { 0 } ( - K _ { Y } ) .
$$

In particular, $p _ { a } ( D + 2 E ) \leq 1 ; Y$ is also a Coble surface if and only if $p _ { a } ( D + 2 E ) = 0$ .

(2) Suppose that $h ^ { 0 } ( - K _ { Y } ) = 1$ .
Then $X$ is a Coble surface if and only if $q$ is a multiplicity $\geq 2$ point of a member in $\mid - 2 K _ { Y } \mid$ but $q$ is not a point of the unique member in $| - K _ { Y } |$ .

(3) Suppose that $Y$ is a Coble surface.
Then $X$ is also a Coble surface if and only $i f \mathrm { m u l t } _ { q } ( D ) \geq 2$ c $\smash {  { \mathcal { D } } _ { \perp } ^ { \mathrm { ~ ~ \tiny ~ { ~  ~ } ~ } } } \qquad { \mathbf { \Lambda } } \to  { \mathbb { T } } ^ { } \mapsto  { \mathbf { \Lambda } } ^ { | }$

Proof.
It follows from the projection formula and Lemma 1.2 that

$$
K _ { Y } ) = h ^ { 0 } ( X , \pi ^ { * } ( - K _ { Y } ) + ( s - 1 ) E ) = h ^ { 0 } ( X , - K _ { X } + s E ) = h ^ { 0 } ( X , K _ { X } + D + s E )
$$

To prove the last part in (1), we first note that $\vert - 2 K _ { Y } \vert = \vert \pi _ { * } ( - 2 K _ { X } ) \vert \neq \emptyset$ , so that $Y$ is a Coble surface if and only if $p _ { a } ( D + 2 E ) = 0$ .
Also, notice that $h ^ { 0 } ( - K _ { Y } ) \leq 1$ since otherwise we can find an anticanonical divisor on $Y$ which passes through the point $\pi ( E )$ .
This would imply that $\vert - K _ { X } \vert \neq \varnothing$ contradicting the assumption that $X$ is a Coble surface.

For (2) and (3), see Lemma 1.9 below.

1.6 Corollary.
A Coble surface $X$ is minimal if and only if, for any $( - 1 )$ -curve $E$ and any $D \in$ $\mid - 2 K _ { X } \mid$ ,

$$
p _ { a } ( D + 2 E ) = 1 .
$$

The next lemmas will be used frequently in the subsequent sections.

1.7 Lemma.
Let $X$ be a smooth rational surface.
Then we have:

(1) Suppose that $L$ is a smooth rational curve with $L ^ { 2 } \geq 0$ .
Then $| L |$ is base point free and $h ^ { 0 } ( Y , L ) = 2 + L ^ { 2 }$ .  
(2) Suppose that $L$ is an irreducible curve with $p _ { a } ( L ) = 1$ and $L ^ { 2 } \geq 1$ .
Then a general member of $| L |$ is smooth and $h ^ { 0 } ( Y , L ) = L ^ { 2 } + 1$ .
If $L ^ { 2 } \geq 2$ , then $B s | L | = \emptyset$ .
If $L ^ { 2 } = 1$ then $| L |$ has exactly one base point.  
(3) Suppose that $L$ is smooth elliptic with $L ^ { 2 } ~ = ~ 1$ and $G$ an effective divisor, not linearly equivalent to $L$ , such that $- 2 K _ { X } \sim L + G$ $( i f h ^ { 0 } ( X , - K _ { X } ) \leq 1$ one always has $G \notin | L |$ ).
Let $G _ { 1 }$ be the unique component in $G$ with $L \cdot G _ { 1 } = 1$ .
Then $G _ { 1 } \notin | L |$ and $L \cap G _ { 1 } = L \cap G$ i s the unique base point of $| L |$ .

Proof.
Let $\pi _ { 1 } : V \to V _ { 1 }$ be the composition of smooth blow-downs of all $( - 1 )$ -curves in fibers digicint fn pd。 Sinee beth tletfe ulen fhon $\pmb { r } , \pmb { \eta }$

Proof.
(1) follows from the exact sequence below, the induction on $L ^ { 2 }$ and the fact that the result is true when $L ^ { 2 } = 0$ :

$$
0 \to { \mathcal { O } } _ { X } \to { \mathcal { O } } _ { X } ( L ) \to { \mathcal { O } } _ { \mathbb { P } ^ { 1 } } ( L ^ { 2 } ) \to 0 .
$$

For (2), a similar exact sequence as in (1) shows that $h ^ { 0 } ( X , L ) = 1 + h ^ { 0 } ( L , { \mathcal O } _ { L } ( L ) ) = 1 +$ $h ^ { 0 } ( L , \omega _ { L } ( - L ) ) + 1 - p _ { a } ( L ) + L ^ { 2 } = 1 + L ^ { 2 }$ .
Here $\omega _ { L } \cong { \mathcal { O } } _ { L }$ is the dualizing sheaf and we have applied the duality and the Riemann Roch theorem for $L$ .

We assert that a general member of $| L |$ is smooth.
Take $L ^ { 2 } - 1$ generic points such that the linear system of divisors from $| L |$ passing through these points is one-dimensional.
By blowing up the points on $L$ , it suffices to prove the assertion when $L ^ { 2 } = 1$ .
Since the only base point of $| L |$ i s then simple, the assertion follows from Bertini’s theorem.

For (3), if $G _ { 0 } \leq G$ and $G _ { 0 } \in | L |$ , then $0 \sim ( K _ { X } + L ) + ( K _ { X } + G _ { 0 } ) + ( G - G _ { 0 } ) \geq G - G _ { 0 }$ , which leads to $G = G _ { 0 } \sim - K _ { X } \sim L$ , a contradiction.
It remains to show that $L \cap G _ { 1 }$ is equal to the unique base point $p$ of $| L |$ .
Let $\tau : Y  X$ be the blow-up of $p$ with $C$ the $\tau$ -exceptional curve.
Then $- 2 K _ { Y } \sim \tau ^ { - 1 } ( L ) + \tau ^ { - 1 } ( G ) - C$ (we use $\tau ^ { - 1 }$ to denote the proper inverse transform under a birational map).
Since $- 2 K _ { Y }$ , $\tau ^ { - 1 } ( L ) , \tau ^ { - 1 } ( G - G _ { 1 } )$ can be represented by a divisor contained in fibres, we obtain that the restriction of $\tau ^ { - 1 } ( G _ { 1 } )$ and $C$ to a general fibre is linearly equivalent.
This is obviously impossible (since no two distinct points on an irrational curve are linearly equivalent).

1.8 Lemma.
(M.
Miyanishi) Let $V  \mathbb { P } ^ { 1 }$ be a smooth rational ruled surface with two sections $s _ { 1 } , s _ { 2 }$ .
Then there is a birational morphism $\pi : V \to \mathbf { F } _ { d }$ onto a minimal ruled surface of degree $d$ , such that $\pi ( s _ { 1 } ) \cdot \pi ( s _ { 2 } ) = s _ { 1 } \cdot s _ { 2 }$ .
Moreover, if both $s _ { i } ^ { 2 }$ are negative we can choose $\pi$ such that $\pi ( s _ { 1 } ) ^ { 2 } = - d = - 1$ .
Finally, $\pi ( s _ { 2 } ) ^ { 2 } = - \pi ( s _ { 1 } ) ^ { 2 } + 2 ( s _ { 1 } \cdot s _ { 2 } )$ .

$V _ { 1 }$ , $s _ { 1 } + F _ { i } + s _ { 2 }$ has the following dual graph:

$$
s _ { 1 } - ( - 1 ) - ( - 2 ) - \cdot \cdot \cdot - ( - 2 ) - ( - 1 ) - s _ { 2 } .
$$

Note that $\pi _ { 1 } ( s _ { i } ) \cdot \pi _ { 1 } ( s _ { j } ) = s _ { i } \cdot s _ { j }$ .
Now a suitable blow-downs of $( - 1 )$ -curves in fibers on $V _ { 1 }$ will give the required birational morphism $\pi$ .
For the second assertion, we let $V _ { 1 }  \mathbf { F } _ { 1 }$ be the successive blow-downs of $( - 1 )$ -curves in fibers with exactly $- 1 - s _ { 1 } ^ { 2 }$ of them intersecting $s _ { 1 }$ ; this is possible because a minimal ruled surface has at most one negative section.
The last assertion follows by expressing $\pi ( s _ { 2 } ) \sim \pi ( s _ { 1 } ) + [ s _ { 1 } \cdot s _ { 2 } - \pi ( s _ { 1 } ) ^ { 2 } ] f$ , where $f$ denotes a fibre.

1.9 Lemma.
Let $X _ { 1 }  \cdots  X _ { n }$ ( $\mathrm { ~ n ~ } \geq 2$ ) be a sequence of blow-ups $\tau _ { i } : X _ { i }  X _ { i + 1 }$ of smooth surfaces with center $p _ { i + 1 } \in X _ { i + 1 }$ and exceptional curve $E _ { i } \subset X _ { i }$ .

(1) Assume that a positive divisor $D$ belongs to $\vert - 2 K _ { X _ { 1 } } \vert$ and denote by $D _ { i }$ its direct image on $X _ { i + 1 }$ .
Then each $p _ { i + 1 }$ is a singularity of $D _ { i + 1 }$ .
In particular, the divisor $D _ { n }$ is always singular.  
(2) $I f | { - 2 K _ { X _ { 1 } } | \neq \emptyset }$ , then there is a singular member $D _ { n }$ of $\left| - 2 K _ { X _ { n } } \right|$ such that the indeterminancy locus of the rational map $X _ { n } \cdots \to X _ { 1 }$ is contained in the singular locus of $D _ { n }$ .

Proof.
This follows from the fact that $D _ { i } \in \vert - 2 K _ { X _ { i } } \vert$ and hence $E _ { i } \cdot D _ { i } = 2$ .

In view of the next result, which follows from the fact that a Coble surface $X$ always has $K _ { X } ^ { 2 } \le - 1$ we only have to consider minimal Coble surfaces.

1.10 Lemma.
Suppose that $X$ is a Coble surface.
Then there is a sequence of blow-downs $X =$ $X _ { 1 } \to X _ { 2 } \to \cdots \to X _ { n }$ ( $\mathrm { \acute { n } \geq 2 }$ ) such that $X _ { n }$ is not Coble but $X _ { i }$ ( $i < n$ ) are all Coble and especially, $X _ { n - 1 }$ is a minimal Coble (see 1.5 and 1.9 for the restriction on the centers of blow-ups).

# 2. The elliptic case

2.1 Let $X$ be a Coble surface and $E$ a $( - 1 )$ -curve with $\pi : X \to Y$ the blow-down of $E$ .
Assume the hypothesis that $p _ { a } ( - 2 K _ { X } + 2 E ) = 1$ , i.e., $| - K _ { Y } | \neq \emptyset$ (on a minimal Coble surface, any $( - 1 )$ -curve satisfies this, by Lemma 1.5).

Consider the linear system

$$
| - 2 K _ { X } + 2 E | = \pi ^ { * } ( | - 2 K _ { Y } | ) .
$$

Note that $\mathrm { d i m } | - 2 K _ { Y } | > 0$ for otherwise $| - 2 K _ { Y } | = 2 | - K _ { Y } |$ and hence $\vert - K _ { X } \vert \neq \varnothing$ , a contradiction (cf.
Lemma 2.3 below).

Write

$$
| - 2 K _ { X } + 2 E | = | M | + P ,
$$

where $| M |$ is the mobile part, and $P$ the fixed part.
We also write

$$
P = G + H , G = \sum _ { i = 1 } ^ { J } g _ { i } G _ { i } ,
$$

where $G _ { i } \cdot M \geq 1$ while $\boldsymbol { H } \cdot \boldsymbol { M } = 0$ .

By Lemmas 1.2 and 1.5, $p _ { a } ( M ) \leq p _ { a } ( M + P ) = 1$ .
We say that $X$ is of elliptic type with respect to $E$ if $p _ { a } ( M ) = 1$ , and of rational type with respect to $E$ if $p _ { a } ( M ) = 0$ .
It may happen that the same Coble surface $X$ (even minimal one) is of elliptic type with respect to one $E _ { 1 }$ , but of rational :l tler $\prime \prime 1$ (ceeE- ple 2 11) The $\begin{array} { r l } { \boldsymbol { \zeta } } & { { } \textbf { \textsf { \textsf { \textsf { \textsf { \textsf { \textsf { \textsf { \Lambda } } } } } } } } \qquad \mathbf { \Phi } } \end{array}$ 1 dlil

to help classify Coble surfaces.
A minimal Coble surface will be called of rational type if it is of rational type with respect to any $E$ .

2.2 Lemma.
Let $X$ be a Coble surface with a $( - 1 )$ -curve $E$ satisfying $p _ { a } ( - 2 K _ { X } + 2 { \cal E } ) = 1$ (on a minimal Coble surface, this is always true for any $( - 1 )$ -curve, by Lemma 1.5). Then, with the above notation, we have the following:

(1) If $p _ { a } ( M ) = 1$ , then a general member of $| M |$ is a smooth elliptic curve, and ${ \cal G } \cdot { \cal M } = { \cal M } ^ { 2 }$ .  
(2) If $p _ { a } ( M ) = 0$ , then either $M = k M _ { 1 }$ ( $k \geq 1$ ) with $M _ { 1 } \cong \mathbb { P } ^ { 1 }$ , $M _ { 1 } ^ { 2 } = 0$ and $G \cdot M _ { 1 } = 4$ , or $M \cong \mathbb { P } ^ { 1 }$ , $M ^ { 2 } \geq 1$ and $G \cdot M = 4 + M ^ { 2 }$ .
In the following, we set $M _ { 1 } = M$ , when $M$ is irreducible.  
(3) $M _ { 1 } + P$ is of simple normal crossing.
$P$ consisits of $( - n )$ -curves with $n \geq 1$ .  
(4) Suppose that $D _ { 1 } + \cdots + D _ { s }$ is a chain in $P _ { \mathrm { r e d } }$ , such that $\begin{array} { r } { L : = M _ { 1 } + \sum _ { i } D _ { i } } \end{array}$ is a loop.
Then $p _ { a } ( M ) = 0$ , $L$ is a simple loop, and $\begin{array} { r } { \sum _ { i } D _ { i } ^ { 2 } \ \leq \ - 2 s - 1 } \end{array}$ ; moreover, $L$ is the only loop in M1 + Pred.

Proof.
For (1) and (2), we have only to consider the case where a general member of $| M |$ i s reducible.
Then by Stein factorization and the rationality of $X$ (or rather the vanishing of $q ( X )$ ), we have $M = k M _ { 1 }$ ( $k \geq 2 _ { , }$ ) with $\lvert M _ { 1 } \rvert$ an irreducible pencil.
Since $p _ { a } ( M _ { 1 } ) \leq p _ { a } ( M ) \leq 1$ , Lemma 1.7 and the fact that $\mathrm { d i m } | M _ { 1 } | = 1$ imply that either $p _ { a } ( M _ { 1 } ) = 0$ and $M _ { 1 } ^ { 2 } = 0$ , or $p _ { a } ( M _ { 1 } ) = 1$ and $M _ { 1 } ^ { 2 } \le 1$ .
The latter case leads to that $1 \geq p _ { a } ( M ) \geq p _ { a } ( 2 M _ { 1 } ) \geq 2$ (see Lemma 1.3 when $M _ { 1 } ^ { 2 } = 1$ ), a contradiction.
This proves (1) and (2); indeed the equality on $G \cdot M$ or $G \cdot M _ { 1 }$ is obtained by intersecting both sides of (2.1) with $M _ { 1 }$ .

Next we prove (3).
First $P$ is of simple normal crossing and contains no arithmetic genus $\geq 1$ curves, for otherwise, $1 \ge p _ { a } ( M _ { 1 } + P ) \ge h ^ { \upsilon } ( M _ { 1 } ) \ge 2$ by Lemma 1.2. Thus each curve in $P$ is a $( - n )$ -curve with $n \geq 1$ because $P$ is the fixed part and by Lemma 1.7. If $\mathrm { B s } | M | = \emptyset$ then (3) is clear.
So, in view of Lemma 1.7, we only need to consider the case where $p _ { a } ( M ) = 1$ .
Then (3) can be proved in a manner similar to (4) below.

Now we prove (4).
If $p _ { a } ( M _ { 1 } ) = 1$ or the dual graph of $L$ is not a simple loop then $2 \leq p _ { a } ( L ) \leq$ $p _ { a } ( M + P ) \leq 1$ ; if the dual graph of $M _ { 1 } + P _ { \mathrm { r e d } }$ contains another loop, then there is a linear chain $N$ having no common components with $L$ such that $N \cdot L \geq 2$ , which leads to $2 \leq p _ { a } ( L + N ) \leq$ $p _ { a } ( M + P ) \leq 1$ , again a contradiction.
As in Lemma 1.7, one sees easily that $h ^ { 0 } ( L ) = 1 + h ^ { 0 } ( L | L ) \geq$ $1 + \chi ( L | L ) = 1 + \chi ( \mathcal { O } _ { L } ) + L ^ { 2 } = 1 + L ^ { 2 }$ .
Substituting $h ^ { 0 } ( L ) = h ^ { 0 } ( M _ { 1 } ) = M _ { 1 } ^ { 2 } + 2$ and expanding $L ^ { 2 }$ , we will get the inequaltiy in (4).

2.3 Lemma.
Let $X , E$ and notation be as in Lemma 2.2. Then we have

(1) $E \cap P = \emptyset$ , whence $E \cdot M = E \cdot P = 0$ ,  
(2) $| M |$ and $P$ are pull backs of $| \pi ( M ) |$ and $\pi ( P )$ , whence a general member $M$ is disjoint from $E$ , and  
(3) $| M |$ contains a member $M ^ { \prime }$ with $M ^ { \prime } - 2 E \geq 0$ .

Proof.
Suppose $E \cap P \neq \emptyset$ .
Then the linear system $\mid - 2 K _ { Y } \mid$ has the point $p = \pi ( E )$ as a base point.
Let $C$ be the unique divisor in $| - K _ { Y } |$ .
The divisor $2 C \in \mathsf { \Omega } | - 2 K _ { Y } |$ and hence contains $p$ .
Thus $p \in C$ and hence $| - K _ { X } | \neq \emptyset$ .
This contradiction proves the first assertion, which, in turn, implies the rest.

In the rest of the section, we shall classify Coble surfaces $X$ of elliptic type (see 2.5, 2.6, 2.8, 2.9).

2.4 Case: $p _ { a } ( M ) = 1$ and $M ^ { 2 } = 0$ .
In this case, $| M |$ is a pencil of elliptic curves without base-points.
It defines an elliptic fibration $f : X \to \mathbb { P } ^ { 1 }$ , so that $E$ and $P$ are contained in fibres (Lemma 2.3). Blowing down $E$ , we get an elliptic fibration $f _ { Y } : Y \to \mathbb { P } ^ { 1 }$ .
Let $f _ { m } : Y _ { m } \to \mathbb { P } ^ { 1 }$ be its relative minimal medel ie $\backprime$ ia ebteined fron $\mathbf { \Delta } \mathbf { V } _ { \mathbf { \Delta } } / \mathbf { \Delta }$ bu blor 1 ined in fbrog of f

Recall that a relative minimal rational elliptic surface $V$ is called an Halphen surface of index $n$ if the divisor class of its fibre is equal to $- n K _ { V }$ .
Any relative minimal rational elliptic surface is an Halphen surface of some index $_ { n }$ .
An Halphen surface of index 1 is a Jacobian rational elliptic surface.
It is characterized by the condition that the fibration does not have multiple fibres, or equivalently, admits a section.
An Halphen surface of index $n \geq 2$ has a unique multiple fibre $n F _ { 1 } ^ { \prime }$ of multiplicity $n$ .
In this case

$$
| - i K _ { V } | = \{ i F _ { 1 } \} , \quad 1 \leq i \leq n - 1 .
$$

All of this is rather well-known and can be found for example in [CD], Chapter 5, §6.

Let $_ n$ be the index of $f _ { m } : Y _ { m } \to \mathbb { P } ^ { 1 }$ .
Since $| - K _ { Y } | \neq \emptyset$ and by Lemma 1.9, $Y$ is obtained from $Y _ { m }$ by a successive blow-ups of singular points and their infinitely near points on one fibre $F _ { 1 }$ (the unique multiple fibre if $n \geq 2$ ).
We know that $\mathrm { d i m } \mid - 2 K _ { Y _ { m } } \mid \geq \mathrm { d i m } \mid - 2 K _ { Y } \mid \geq 1$ .
Applying (2.2) this implies that $n \leq 2$ .
Moreover, if $n = 2$ , after one blow-up the anti-bicanonical linear system becomes of dimension 0. So, in this case, we must have $Y = Y _ { m }$ and $P = 0$ .

Suppose that $n = 1$ .
We claim that $X$ is not a minimal Coble surface.
Since $h ^ { 0 } ( Y _ { m } , - 2 K _ { Y _ { m } } ) = 2$ while $h ^ { 0 } ( Y , - K _ { Y } ) = 1$ (Lemma 1.5), we have $Y \neq Y _ { m }$ .
For simplicity, we assume that $Y  Y _ { m }$ is a single blow-down of a $( - 1 )$ -curve $E _ { 1 }$ to a point $q _ { 1 }$ on a fiber $F _ { 1 }$ (the general case is similar).
Then the mobile part of $\vert - 2 K _ { Y } \vert$ is equal to the pull back of the elliptic pencil, and its fixed part is equal to [(the proper inverse transform of $F _ { 1 }$ ) $+ ( m _ { 1 } - 2 ) E _ { 1 } ]$ , where $m _ { 1 }$ is the multiplicity of $F _ { 1 } ^ { \prime }$ at $q _ { 1 }$ .
The map $\pi : X \to Y$ in 2.1 is just the blow-down of the $( - 1 )$ -curve $E$ to a multiplicity $m$ ( $\geq 2$ ) singular point of a fibre $F \neq F _ { 1 }$ (cf.
Lemma 2.3 and Remark 2.9 below).
Moreover,

$$
| M | + P = \pi ^ { \ast } | - 2 K _ { Y } | = | F | + ( F _ { 1 } ^ { \prime } + ( m _ { 1 } - 2 ) E _ { 1 } ^ { \prime } ) ,
$$

$$
- 2 K _ { X } \sim P _ { 1 } + P _ { 2 } , P _ { 1 } : = F ^ { \prime } + ( m - 2 ) E , P _ { 2 } : = F _ { 1 } ^ { \prime } + ( m _ { 1 } - 2 ) E _ { 1 } ^ { \prime } .
$$

Here $F _ { 1 } ^ { \prime } , F ^ { \prime } , E _ { 1 } ^ { \prime }$ denote the proper inverse transforms of $F _ { 1 } , F , E _ { 1 }$ , and $F$ denotes a full fiber on $X$ by abuse of notation.

Let $C _ { m }$ be a section on $Y _ { m }$ and $C$ be its total inverse transform on $X$ .
Since we blow-up singular points of $F _ { 1 } , F $ , the map $X  Y _ { m }$ is an isomorphism over $C _ { m }$ .
Therefore $C$ is a $( - 1 )$ -curve.
Let us check that $p _ { a } ( - 2 K _ { X } + 2 C ) = 0$ so that after blowing down $C$ we get a Coble surface again.
Applying the exact sequence in Lemma 1.3 to compare $p _ { a } ( P _ { 1 } + P _ { 2 } + C )$ with $p _ { a } ( P _ { 1 } + P _ { 2 } + 2 C )$ and $p _ { a } ( P _ { 1 } + P _ { 2 } )$ , we find that $p _ { a } ( P _ { 1 } + P _ { 2 } + 2 C ) = p _ { a } ( P _ { 1 } + P _ { 2 } + C ) = p _ { a } ( P _ { 1 } + P _ { 2 } )$ .
The latter equality follows from the fact that $h ^ { 0 } ( { \mathcal { O } } _ { P _ { 1 } + P _ { 2 } } ) > h ^ { 0 } ( { \mathcal { O } } _ { P _ { 1 } + P _ { 2 } + S } )$ and the application of Lemma 1.3 with $D - D ^ { \prime } = C$ .
Since $p _ { a } ( P _ { 1 } + P _ { 2 } ) = h ^ { 0 } ( K _ { X } + P _ { 1 } + P _ { 2 } ) = 0$ , the claim is proved.

Summing up, we obtain

2.5 Theorem.
Let $X$ be a minimal Coble surface and $E$ a $( - 1 )$ -curve on $X$ .
Assume that the mobile part $| M |$ of $\big | - 2 K _ { X } + 2 E \big |$ satisfies $p _ { a } ( M ) = 1$ and $M ^ { 2 } = 0$ .
Then $| - 2 K _ { X } + 2 E | = | M |$ and $X$ is obtained from an Halphen surface $Y$ of index 2 by one blow-up $\pi$ of a singular point on a non-multiple fibre $F$ with $E$ the exceptional curve.

2.6 Definition, Remark and Example.
(1) A Coble surface $X$ is of Halphen type, or type(H), with respect to $E$ if it is obtained as in Theorem 2.5 above.
In general, a Coble surface $W$ is of Halphen type if there is a birational morphism $W  X$ such that $X$ is of Halphen type with respect to some $E$ .

(2) From 2.4 and 2.7 below, we see that an arbitrary Coble surface $X$ with a $( - 1 )$ -curve $E$ satisfying $p _ { a } ( - 2 K _ { X } + 2 E ) = 1$ , $p _ { a } ( M ) = 1$ and $M ^ { 2 } = 0$ , is equal to either $X$ in Theorem 2.5, or $X ^ { \prime }$ i Tl $\mathrm { ~ \bf ~ \odot ~ } \mathrm { ~ \bf ~ \odot ~ }$ whor ptof $\pmb { T } , \pmb { \rceil }$ (of Dor conlr 2.0)

(3) Let $Y  \mathbb { P } ^ { 1 }$ be an Halphen surface and $F$ a non-multiple singular fibre.
If $F$ is of type $I _ { n }$ ( $=$ $\tilde { A } _ { n - 1 }$ in other notation), then $F$ has exactly $n$ double points.
Blowing up one double point gives us a minimal Coble surface $X$ because $K _ { X } ^ { 2 } = - 1$ .
Blowing up all double points gives us a terminal (but non-minimal if $n \geq 2$ ) Coble surface (cf.
Proposition 6.4 in §6).
In particular, if $n = 1$ , we get a Coble surface which is both minimal and terminal.
The same is true when we blow up the unique singular point of a fibre of type $I I$ .
On the other hand, if we blow-up successively points on multiple components of a non-reduced fibre, we get examples of non-terminal Coble surfaces.

2.7 Case : $G _ { i } \cap G _ { j } = \varnothing$ $p _ { a } ( M ) = 1$ when $i \neq j$ and .
Thus $M ^ { 2 } = m \ge 1$ $\textstyle \sum _ { i = 1 } ^ { J } g _ { i } = m$ .
In notation of Lemma 2.2, we have by Lemma 2.2. $M \cdot G _ { i } = 1$ and

By Lemma 1.7, $\mathrm { d i m } | M | = m$ .
Fix a general member $M _ { 1 }$ of $| M |$ and put $p _ { i } = M _ { 1 } \cap G _ { i }$ .
Blow up the points $p _ { i }$ to get a surface $X _ { 1 }$ .
If $g _ { i } \geq 2$ , we pick the point $p _ { i } ^ { ( 1 ) }$ on $X _ { 1 }$ lying over $p _ { i }$ and on the proper inverse transform of $M _ { 1 }$ .
Continue in this way to get a surface $X ^ { \prime }$ obtained from $X$ by blowing up the points pi = p(0)i , p(1i $p _ { i } = p _ { i } ^ { ( 0 ) } , p _ { i } ^ { ( 1 ) } , \dots , p _ { i } ^ { ( g _ { i } - 1 ) }$ , where $p _ { i } ^ { ( s ) }$ is infinitely near to $p _ { i } ^ { ( s - 1 ) }$ and lies on the proper inverse transform of $M _ { 1 }$ .

Let $\Theta _ { i } ^ { ( j ) }$ be the proper inverse transform on $X ^ { \prime }$ of the $( - 1 )$ -curve lying over the point $p _ { i } ^ { ( j - 1 ) }$ .
Set $C _ { i } : = \Theta _ { i } ^ { ( g _ { i } ) }$ and denote by $M _ { 1 } ^ { \prime }$ , $G _ { i } ^ { \prime }$ the proper inverse transforms on $X ^ { \prime }$ of $M _ { 1 }$ , $G _ { i }$ .
Then $M _ { 1 } ^ { \prime } + C _ { i } + \Theta _ { i } ^ { ( g _ { i } - 1 ) } + \cdot \cdot \cdot + \Theta _ { i } ^ { ( 1 ) } + G _ { i } ^ { \prime }$ has the dual graph:

$$
( 0 ) - ( - 1 ) - ( - 2 ) - \cdot \cdot \cdot - ( - 2 ) - G _ { i } ^ { \prime } .
$$

Let $E ^ { \prime }$ be the pre-image of $E$ on $X ^ { \prime }$ .
Since each $p _ { i }$ is not on $E$ (Lemma 2.3), $X ^ { \prime }  X$ is an isomorphism over $E$ and hence $E ^ { \prime }$ is a $( - 1 )$ -curve.
Let $\pi ^ { \prime } : X ^ { \prime } \to Y ^ { \prime }$ be the blow-down of $E ^ { \prime }$ to a point $q$ .
Then there is a birational morphism $Y ^ { \prime }  Y$ such that two compositions $X ^ { \prime } \stackrel { \pi ^ { \prime } } {  } Y ^ { \prime }  Y$ and $X ^ { \prime }  X \stackrel { \pi } {  } Y$ are identical.
Applying Lemma 1.7 to $S$ , which is the blow-down of $C _ { 1 }$ to the point $p _ { 1 } ^ { ( g _ { 1 } - 1 ) }$ followed by the blow-down of $E ^ { \prime }$ , and $L : =$ (the image on $S$ of $M _ { 1 } ^ { \prime }$ ), we obtain $h ^ { 0 } ( X ^ { \prime } , M _ { 1 } ^ { \prime } ) = h ^ { 0 } ( S , L ) = 2$ .

Noting that each $p _ { i }$ is a point of multiplicity $1 + g _ { i } \ge 2$ in $\begin{array} { r } { M _ { 1 } + \sum _ { i = 1 } ^ { J } g _ { i } G _ { i } + H ( \sim - 2 K _ { X } + 2 E ) , } \end{array}$ we get

$$
( \pi ^ { \prime } ) ^ { * } ( - 2 K _ { Y ^ { \prime } } ) = - 2 K _ { X ^ { \prime } } + 2 E ^ { \prime } \sim M _ { 1 } ^ { \prime } + P ^ { \prime } ,
$$

where $P ^ { \prime }$ is the sum of the total transform of $H$ and the disjoint union of $J$ weighted linear chains $\Theta _ { i } + g _ { i } G _ { i } ^ { \prime }$ with $\begin{array} { r } { \Theta _ { i } = \sum _ { j = 1 } ^ { ( g _ { i } - 1 ) } ( g _ { i } - j ) \Theta _ { i } ^ { ( j ) } } \end{array}$ .

$| M _ { 1 } ^ { \prime } |$ defines a Jacobian elliptic fibration with sections $C _ { i }$ .
Since $P ^ { \prime } { \cdot } M _ { 1 } ^ { \prime } = 0$ and $E ^ { \prime } { \cdot } M _ { 1 } ^ { \prime } = E { \cdot } M = 0$ (Lemma 2.3), $P ^ { \prime } , E ^ { \prime }$ are contained in fibres $F _ { 1 } , F $ on $X ^ { \prime }$ , respectively.
Let $Y ^ { \prime }  Y _ { \mathrm { m i n } }$ be the smooth blow-down to a relative minimal model.
As we explained in 2.4, $X ^ { \prime }$ is obtained from $Y _ { \mathrm { m i n } }$ by blowing up singular points and their infinitely near points on a fibre $F _ { 1 }$ of the elliptic fibration on $Y _ { \mathrm { m i n } }$ followed by blowing up a point $q$ of another fibre $F ^ { \prime }$ to the curve $E ^ { \prime }$ .
Let us sum up the previous arguments by stating the following:

2.8 Theorem.
Let $X$ be a Coble surface with a $( - 1 )$ -curve $E$ satisfying $p _ { a } ( - 2 K _ { X } + 2 { \cal E } ) = 1$ (on a minimal Coble surface, any $( - 1 )$ -curve satisfies this).
Assume that the mobile part $| M |$ of $\vert - 2 K _ { X } + 2 E \vert$ satisfies $p _ { a } ( M ) = 1$ and $M ^ { 2 } = m > 0$ .
Then $X$ is obtained as follows.

There exist a relative minimal Jacobian rational elliptic surface $Y _ { \mathrm { m i n } }$ with a singular fibre $F _ { 1 }$ , $J$ disjoint linear chains $\Theta _ { i } + G _ { i } ^ { \prime }$ i n $F _ { 1 }$ of length $g _ { i }$ $( g _ { i } \geq 1 )$ with $\textstyle \sum _ { i = 1 } ^ { J } g _ { i } = m$ , and $J$ disjoint sections $C _ { i }$ on $Y _ { \mathrm { m i n } }$ so that $F _ { 1 } + C _ { i } + \Theta _ { i } + G _ { i } ^ { \prime }$ has the dual graph (2.3).

The surface $X$ is obtained by blowing up singular points (away from $\Theta _ { i }$ ) and their infinitely near points on $F _ { 1 }$ (to get $Y ^ { \prime }  Y _ { \mathrm { m i n } }$ ), then blowing up a point $q$ $( \notin C _ { i } )$ of a fibre $F$ $( \neq F _ { 1 }$ ) on $Y _ { \mathrm { m i n } }$ (to Pot $\_ I \_ V / \_ I \_ V / \_ I \_ I \_ I / \_ I$ ond Gnell.
blourina der oothl.: the linoer ehoing $\mathrm { ~ \bf ~ \mathscr ~ { ~ \textbf ~ { ~ \textbf { ~ \psi ~ } ~ } ~ } ~ }$

2.9 Definition and Remark.
(1) $Y ^ { \prime }  Y _ { \mathrm { m i n } }$ is not identical for otherwise $h ^ { 0 } ( - K _ { X } ) \geq h ^ { 0 } ( - K _ { X ^ { \prime } } ) =$ 1. Thus $| M ^ { \prime } | , P ^ { \prime }$ in (2.4) are exactly the mobile, fixed part of $\vert - 2 K _ { X ^ { \prime } } + 2 E ^ { \prime } \vert$ .
$P ^ { \prime }$ contains (but is contained in) the proper inverse transform (the total transform) of $F _ { 1 } ^ { \prime }$ .

(2) Note that the unique member in $\vert - K _ { Y ^ { \prime } } \vert$ contains $\pi _ { * } ^ { \prime } ( P ^ { \prime } )$ and also the support of the full fibre on $Y ^ { \prime }$ lying over $F _ { 1 } ^ { \prime }$ (cf.
Lemma 1.9). This and $h ^ { 0 } ( X ^ { \prime } , - K _ { X ^ { \prime } } ) = 0$ explain why $q \in F \neq F _ { 1 }$ .

(3) $X ^ { \prime }$ is a Coble surface if and only if $q$ is a singular point of $F ^ { \prime }$ (guaranteeing $\vert - 2 K _ { X ^ { \prime } } \vert \neq \varnothing $ ). If this is the case, then the $X$ constructed as in Theorem 2.8 with $m = 1$ is always a Coble surface (see 2.4 and Example 2.13); it is also minimal if $Y ^ { \prime }  Y _ { \mathrm { m i n } }$ is a single blow-up for then $K _ { X } ^ { 2 } = - 1$ .
See Example 2.10 for a situation where $q$ has 2-dimensional freedom to choose.

(4) A Coble surface $X$ is of Jacobian type, or type (J) with respect to $E$ if $X$ is equal to either $X$ in Theorem 2.8 with an associated $E$ there, or to $X ^ { \prime }$ with $E ^ { \prime } = E$ and $q$ a singular point of $F$ .
In general, a Coble surface $W$ is of Jacobian type if there is a birational morphism $W  X$ such that $X$ is of Jacobian type with respect to some $E$ ; $W$ is of elliptic type if it is either Jacobian or Halphen type (see 2.6); $W$ is of rational type if it is not of elliptic type (cf.
Example 2.11). We can construct a minimal Coble surface which is of Halphen type with respect to one curve but of Jacobian type with respect to another curve.

(5) The $\left( - 2 \right)$ -chain $\begin{array} { r } { \Theta _ { i } = \sum _ { j = 1 } ^ { ( g _ { i } - 1 ) } \Theta _ { i } ^ { ( j ) } } \end{array}$ meets only $G _ { i } ^ { \prime }$ i n $F _ { 1 }$ , for otherwise $M _ { 1 }$ , $G _ { i }$ and one more component $P _ { 1 }$ of $P$ will share the same point, which is absurd by Lemma 2.2. Similarly, $G _ { i } ^ { \prime } \cdot \Theta _ { i } = 1$ .
In particular, $g _ { i } \leq 6$ ( $= 6$ only when $F _ { 1 }$ is of type $I I ^ { * }$ ) and $g _ { i } = 0$ when $F _ { 1 }$ is reduced.
When $F _ { 1 }$ is not reduced, it is impossible that $g _ { i } \geq 2$ for two $i$ say $i = 1 , 2$ , for otherwise the shortest chain in $F _ { 1 } ^ { \prime }$ linking $G _ { 1 } ^ { \prime }$ and $G _ { 2 } ^ { \prime }$ will give rise to a chain $L$ in $P$ (not a trivial fact; cf.
Lemma 1.9 and (1), (2) above), and hence to a loop $M _ { 1 } + G _ { 1 } + L + G _ { 2 }$ in $M _ { 1 } + P$ , a contradiction to Lemma 2.2.

Thus $\begin{array} { r } { m = \sum _ { i } g _ { i } \le 6 } \end{array}$ .
Indeed, otherwise $m \geq 7$ , $F _ { 1 }$ is of type $I _ { s }$ ( $s \geq m$ ) and $C _ { i }$ are sections intersecting different components of $F _ { 1 }$ ; contracting all $C _ { i }$ and $[ m / 2 ]$ components of $F _ { 1 }$ , we get a smooth rational surface $V$ with $K _ { V } ^ { 2 } = m + [ m / 2 ] \geq 1 0$ , a contradiction.
See Example 2.13 for the converse to Theorem 2.8.

2.10 Example.
Let us give an example when $m = M ^ { 2 } = 6$ occurs.
Take two triples of nonconcurrent lines $( L _ { 1 } , L _ { 2 } , L _ { 3 } ) , ( L _ { 4 } , L _ { 5 } , L _ { 6 } )$ .
Let us denote by $p _ { i j }$ the intersection point of the lines $\boldsymbol { L } _ { i }$ and $L _ { j }$ .
We assume that $p _ { 1 2 } \in L _ { 4 } , p _ { 1 3 } \in L _ { 5 }$ , and $p _ { 2 3 } \in L _ { 6 }$ .
The curves $L _ { 1 } + L _ { 2 } + L _ { 3 }$ and $L _ { 4 } + L _ { 5 } + L _ { 6 }$ span a pencil of plane cubics with nine base points $p _ { 1 6 } , p _ { 2 5 } , p _ { 3 4 } , p _ { 1 2 } , p _ { 1 3 } , p _ { 2 3 }$ and infinitely near points $p _ { 1 2 } ^ { \prime }  p _ { 1 2 } , p _ { 1 3 } ^ { \prime }  p _ { 1 3 } , p _ { 2 3 } ^ { \prime }  p _ { 2 3 }$ lying on the proper inverse transforms of the lines $L _ { 4 } , L _ { 5 } , L _ { 6 }$ .
After blow up the base points we obtain a Jacobian elliptic surface with reducible fibres of type $I _ { 6 }$ (its image in $\mathbb { P } ^ { 2 }$ is the union of lines $L _ { 1 } , L _ { 2 } , L _ { 3 } )$ and of type $I _ { 3 }$ (its image in $\mathbb { P } ^ { 2 }$ is the union of lines $L _ { 4 } , L _ { 5 } , L _ { 6 } )$ .
It has six disjoint sections corresponding to the six base-points $p _ { 1 6 } , p _ { 2 5 } , p _ { 3 4 } , p _ { 1 2 } ^ { \prime } , p _ { 1 3 } ^ { \prime } , p _ { 2 3 } ^ { \prime }$ .
If we blow down the six sections and blow up all 6 singular points of the fibre of type $I _ { 6 }$ (to get $Y$ ), followed by the blow-up of a singular point $q$ (to get a curve $E$ ) of the fibre of type $I _ { 3 }$ , we obtain a minimal Coble surface of Jacobian type with $M ^ { 2 } = 6$ and $K _ { X } ^ { 2 } = - 1$ .
Note that we can choose $q$ to be any point as long as it is not on the fibre of type $I _ { 6 }$ (to make sure that $| - K _ { X } | = \varnothing .$ ), because $\mathrm { d i m } \mid - 2 K _ { X } + 2 E \mid = M ^ { 2 } = 6 > 2$ always implies that $\vert - 2 K _ { X } \vert \neq \varnothing$ .

2.11 Example.
We construct a minimal Coble surface $X$ with two disjoint $( - 1 )$ -curves $E _ { 0 }$ , $E _ { 2 }$ such that $X$ is of elliptic type with respect to the first $( - 1 )$ -curve $E _ { 0 }$ $\mathrm { \ t y p e ( J ) }$ with $m = g _ { 1 } = 2$ ) but of rational type with respect to the second one $E _ { 2 }$ and fitting Case (2) with $( m , k ) = ( 0 , 2 )$ in Theorem 3.2.

Consider a minimal rational Jacobian surface $V$ with two fibres $F _ { 1 } , F _ { 2 }$ of type $I _ { 0 } ^ { * }$ ${ \bf \chi } ( = \tilde { D } _ { 4 }$ ).
One obtains this surface as the blow up of 9 base points of the pencil of cubic curves spanned by the curve $L _ { 1 } + L _ { 2 } + L _ { 3 }$ , where $L _ { i }$ are lines concurrent at a point $q$ , and $H _ { 1 } + 2 H _ { 2 }$ , where $H _ { 1 }$ is a line through $q$ and $H _ { 2 }$ is a line not containing $q$ .
It is easy to locate four disjoint sections $E _ { i }$ on $V$ .
Three of th h1 $\tau \ \mathrm { ~  ~ { ~ \frown ~ } ~ } \tau$ d tle feunth one is blown up from an infinitely near base point to the point $q$ .
Let $C _ { i }$ be the components of the fibre $F _ { 1 }$ , intersecting $E _ { i }$ , and $C _ { i } ^ { \prime }$ the same for the other fibre $F _ { 2 }$ .
Let $X ^ { \prime }$ be the blow-up of $V$ at two points lying on the multiple component of $F _ { 1 } ^ { \prime }$ and one point $p$ lying on the multiple component of $F _ { 2 }$ .

Let $X$ be the blow-down of the section $E _ { 1 } ^ { \prime }$ and the component $C _ { 1 }$ .
This is a minimal Coble surface which is of elliptic type with respect to the exceptional curve $E _ { 0 }$ blown down to $p$ .
Now observe that if we blow down the section $E _ { 2 }$ on $X$ to get a surface $Y$ , we can verify that $| - 2 K _ { Y } | = | 2 L | + P$ , where $| L |$ is the pencil of smooth rational curves linearly equivalent to the image on $Y$ of the component $C _ { 1 } ^ { \prime }$ .
Another member of $| L |$ entering as a component of an anti-bicanonical effective divisor is equal to the image of $C _ { 2 } + C _ { 2 } ^ { \prime }$ .
Thus $X$ is of rational type with respect to $E _ { 2 }$ .

2.12 Example.
Here we construct examples of Coble surfaces $X$ of Jacobian type with respect to $E$ so that $M ^ { 2 } = 3$ in notation of Lemma 2.2. Consider the union of three lines $\boldsymbol { L } _ { i }$ and a conic $C$ (we may degenerate it into the sum $L _ { 4 } + L _ { 5 }$ of two distinct lines) in $\mathbb { P } ^ { 2 }$ such that $\textstyle C + \sum _ { i = 1 } ^ { 3 } L _ { i }$ is of simple normal crossing.
Blowing up the 9 intersection points $L _ { i } \cap L _ { j }$ , $C \cap L _ { i }$ , we obtain a surface $Y$ with isolated $\vert - K _ { Y } \vert$ represented by the proper inverse transform of $\textstyle \sum _ { i = 1 } ^ { 3 } L _ { i }$ .
Also we see that $\vert - 2 K _ { Y } \vert$ has the mobile part defined by the linear system of cubics through the six intersection points $C \cap L _ { i }$ .
To be precise, $\begin{array} { r } { \vert - 2 K _ { Y } \vert = \vert M \vert + \sum _ { i } L _ { i } ^ { \prime } } \end{array}$ , $M \sim L + C ^ { \prime }$ , where $L$ is the pull-back of a general line and $L _ { i } ^ { \prime } , C ^ { \prime }$ the proper inverses of $L _ { i } , C$ .
Now let $X$ be the blow-up of $Y$ at a point $q$ not on the unique member of $\vert - K _ { Y } \vert$ , with $E$ the exceptional curve.
Then $h ^ { 0 } ( - 2 K _ { X } ) \geq h ^ { 0 } ( - 2 K _ { Y } ) - 3 = 1$ and $X$ is a minimal Coble surface of Jacobian type with respect to $E$ .

Example 2.13. We now give examples with $g _ { i } = 1$ , kind of converse statement to Theorem 2.8 and Remark 2.9. The same idea can be applied to get examples with $g _ { i } \geq 2$ (see also Example 2.11).

Let $Y _ { \mathrm { m i n } }$ be a Jacobian minimal rational elliptic surface with singular fibres $F _ { 1 } , F$ .
Suppose that $C _ { i }$ ( $1 \leq i \leq m$ ) are $_ { m }$ disjoint sections meeting $m$ different components $G _ { i }$ of $F _ { 1 }$ .
We construct a blow-up $Y ^ { \prime }  Y _ { \mathrm { m i n } }$ in the following way: it is the minimal blow-up of singular points and their infinitely near points of $F _ { 1 }$ such that the proper inverses of $G _ { i }$ all become $( - 4 )$ -curves on $Y ^ { \prime }$ .
Let $Y ^ { \prime }  Y$ be the blow-down of $( - 1 )$ -curves $C _ { i }$ .

Then one can verify that $\vert - K _ { Y } \vert$ has only one member $\textstyle \sum _ { i } G _ { i } ^ { \prime } + \Delta$ , where $G _ { i } ^ { \prime }$ is the strict transform of $G _ { i }$ which is a $\left( - 3 \right)$ -curve with $G _ { i } ^ { \prime } \cdot \Delta = 2$ , where $\Delta$ is effective and contractible to the divisor $F _ { 1 } - \textstyle \sum _ { i } G _ { i }$ and hence further to Du Val singularities (to be precise, it is a set of a few smooth points when $F _ { 1 } ^ { \prime }$ is reduced).
We have also

$$
| - 2 K _ { Y } | = | M ^ { \prime } | + P ^ { \prime } , P ^ { \prime } = \sum _ { i } G _ { i } ^ { \prime } + H ^ { \prime } ,
$$

where $0 \le H ^ { \prime } \le \Delta$ , where $M ^ { \prime }$ is the strict transform of a general full fibre and hence a smooth elliptic curve with $( M ^ { \prime } ) ^ { 2 } = m$ , Let $\pi : X \to Y$ be the blow-up of a singular point $q$ on the strict transform $F ^ { \prime }$ on $Y$ of the second fibre $F ^ { \prime }$ .
Then $X$ is a Coble surface with $M ^ { 2 } = m$ in notation of Lemma 2.2, where $M = \pi ^ { * } M ^ { \prime }$ .
Indeed, $| - K _ { X } | = \emptyset$ for $q$ is not on the unique member of $\vert - K _ { Y } \vert$ ; $\vert - 2 K _ { X } \vert \neq \varnothing$ because $F ^ { \prime }$ is a member of $\vert M ^ { \prime } \vert$ with $\mathrm { m u l t } _ { q } F ^ { \prime } \ge 2$ (Lemma 1.5).

# 3. The rational case

3.1 Now we shall consider the case of a Coble surface $X$ and a $( - 1 )$ -curve $E$ with $p _ { a } ( - 2 K _ { X } + 2 { \cal E } ) =$ 1 (on a minimal Coble surface, any $( - 1 )$ -curve satisfies this), such that the mobile part $| M |$ o f $| - 2 K _ { X } + 2 E | = | M | + P$ satisfies $p _ { a } ( M ) = 0$ .
As in Lemma 2.2, write $M = k M _ { 1 }$ ( $k \geq 1 \mathrm { ~ , ~ }$ ) with $M _ { 1 } \cong \mathbb { P } ^ { 1 }$ , and the fixed part as $\begin{array} { r } { P = G + H = \sum _ { i = 1 } ^ { J } g _ { i } G _ { i } + H } \end{array}$ , where $G _ { i } \neq G _ { j }$ when $i \neq j$ .
Write also $\begin{array} { r } { H = \sum _ { i } H _ { i } } \end{array}$ where $H _ { i } = H _ { j }$ is allowed.
We note that $k \geq 2$ happens only when $M _ { 1 } ^ { 2 } = 0$ .
Set $m = M _ { 1 } ^ { 2 }$ .
Let us state the theorem classifying all Coble surfaces of rational type.

3.2 Theorem.
There is a birational morphism $\tau : X \to Y _ { \operatorname* { m i n } }$ onto a minimal rational surface $Y _ { \mathrm { m i n } }$ , factoring as the blow down $\pi : X \to Y$ of $E$ and a morphism $\tau _ { y } : Y \to Y _ { \mathrm { m i n } }$ , such that the direct image $\begin{array} { r } { \Gamma : = k \overline { { M } } _ { 1 } + \sum _ { i = 1 } ^ { J } g _ { i } \overline { { G } } _ { i } + \overline { { H } } \in \vert - 2 K _ { Y _ { \operatorname* { m i n } } } \vert } \end{array}$ of $k M _ { 1 } + G + H \in \vert - 2 K _ { X } + 2 E \vert$ are described as in one of the following Cases (1) - (16), where to save notation, we use the same $M _ { 1 } , G _ { i } , H _ { i }$ to denote their images $\overline { { M } } _ { 1 } , \overline { { G } } _ { i } , \overline { { H } } _ { i }$ on $Y _ { \mathrm { m i n } }$ .

In Cases (1) - (9), $Y _ { \mathrm { m i n } } = \mathbb { P } ^ { 2 }$ and hence $\Gamma$ is a sextic.

(1) $\Gamma = M _ { 1 } + 2 G _ { 1 } + H _ { 1 }$ ; $( m , k ) = ( 0 , 1 )$ ; $G _ { 1 }$ is a conic, $M _ { 1 }$ and $H _ { 1 }$ are distinct lines meeting at $p _ { 1 }$ ; Supp $\Gamma$ is of simple normal crossing.

(2) $\begin{array} { r } { \Gamma = k M _ { 1 } + 2 G _ { 1 } + \sum _ { i = 1 } ^ { 4 - k } H _ { i } } \end{array}$ ; $( m , k ) = ( 0 , 1 ) , ( 0 , 2 ) ;$ $M _ { 1 }$ and $H _ { i }$ are lines through the same point $p _ { 1 }$ ; $G _ { 1 }$ is a line not through $p _ { 1 }$ ; $H _ { i } = H _ { j }$ is allowed but $M _ { 1 } \neq H _ { i }$ .

(3) $\Gamma = M _ { 1 } + 2 G _ { 1 } + H _ { 1 }$ , $( m , k ) = ( 0 , 1 ) \colon$ ; $G _ { 1 }$ is a conic; $M _ { 1 }$ and $H _ { 1 }$ are distinct lines intersecting $G _ { 1 }$ transversally at the same point $p _ { 1 }$ and two other points.

(4) $\begin{array} { r } { \Gamma = k M _ { 1 } + \sum _ { i = 1 } ^ { 6 - k } H _ { i } } \end{array}$ ; $( m , k ) = ( 0 , k )$ with ( $1 \le k \le 6$ ); $M _ { 1 } , H _ { i }$ are lines through the same point $p _ { 1 }$ ; $H _ { i } = H _ { j }$ is allowed but $M _ { 1 } \neq H _ { i }$ .

(5) $\begin{array} { r } { \Gamma = M _ { 1 } + \sum _ { \ell = 1 } ^ { J } g _ { \ell } G _ { \ell } } \end{array}$ ; $( m , k ) = ( 1 , 1 )$ ; $g _ { 1 } = 1 , 2$ ; $\begin{array} { r } { 2 g _ { 1 } + \sum _ { j = 2 } ^ { J } g _ { j } = 5 } \end{array}$ ; $G _ { 1 }$ is a conic; $M _ { 1 }$ and $G _ { j }$ $( 2 \leq j \leq J )$ are $J$ distinct lines; Sing $\textstyle \sum _ { \ell = 1 } ^ { J } G _ { \ell }$ is disjoint from $M _ { 1 }$ .

(6) $\begin{array} { r } { \Gamma = M _ { 1 } + \sum _ { i = 1 } ^ { J } g _ { i } G _ { i } } \end{array}$ ; $( m , k ) = ( 1 , 1 )$ ; $\textstyle \sum _ { i = 1 } ^ { J } g _ { i } = 5$ ; $M _ { 1 }$ and $G _ { i }$ ( $1 \leq i \leq J$ ) are $J + 1$ distinct lines; $G _ { i }$ and $G _ { j }$ share no common points on $M _ { 1 }$ when $i \neq j$ .

(7) $\Gamma = M _ { 1 } + 3 G _ { 1 } + G _ { 2 }$ ; $( m , k ) = ( 3 , 1 )$ ; $M _ { 1 }$ is a conic; $G _ { i }$ are distinct lines; Supp $\Gamma$ is of simple normal crossing; let $p _ { 1 }$ be a common point of $M _ { 1 }$ and $G _ { 2 }$ .

(8) $\begin{array} { r } { \Gamma = M _ { 1 } + \sum _ { i = 1 } ^ { J } g _ { i } G _ { i } } \end{array}$ ; $( m , k ) = ( 3 , 1 )$ ; $g _ { 1 } = 1 , 2$ ; $\textstyle \sum _ { i = 1 } ^ { J } g _ { i } = 4$ ; $M _ { 1 }$ is a conic; $G _ { i }$ are distinct lines; all $G _ { j }$ $\mathit { T } \le j \le J$ ) intersect $M _ { 1 }$ transversally at the same point $p _ { 1 }$ and $J - 1$ other points; $G _ { 1 }$ meets $M _ { 1 }$ at two distinct points not in $M _ { 1 } \cap G _ { j }$ $( j \geq 2 )$ .

(9) $\Gamma = M _ { 1 } + 4 G _ { 1 }$ ; $( m , k ) = ( 4 , 1 )$ ; $M _ { 1 }$ is a conic; $G _ { 1 }$ is a line intersecting $M _ { 1 }$ at two distinct points.

(10) $Y _ { \mathrm { m i n } } = \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ $\begin{array} { r } { \Gamma = M _ { 1 } + \sum _ { \ell = 1 } ^ { J } g _ { \ell } G _ { \ell } } \end{array}$ ; $( m , k ) = ( 2 , 1 )$ ; $g _ { 1 } = 1 , 2$ ; $\begin{array} { r } { \sum _ { i = 2 } ^ { r } g _ { i } = \sum _ { j = r + 1 } ^ { J } g _ { j } = } \end{array}$ $3 - g _ { 1 } ; M _ { 1 }$ $G _ { 1 }$ at two distinct points; $G _ { i }$ $2 \leq i \leq r )$ and $G _ { j }$ ( $r + 1 \leq j \leq J _ { \ L }$ ) are distinct fibers of two different rulings such that Sing $\sum _ { \ell = 1 } ^ { J } G _ { \ell }$ is disjoint from $M _ { 1 }$ .

(11) $Y _ { \operatorname* { m i n } } = \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ ; $\begin{array} { r } { \Gamma = M _ { 1 } + \sum _ { \ell = 1 } ^ { J } g _ { \ell } G _ { \ell } } \end{array}$ ; $( m , k ) = ( 2 , 1 )$ ; $\textstyle \sum _ { i = 1 } ^ { r } g _ { i } = \sum _ { j = r + 1 } ^ { J } g _ { j } = 3$ ; $M _ { 1 }$ is a section (of both rulings) of self intersection 2; $G _ { i }$ ( $1 \leq i \leq r )$ and $G _ { j }$ $r + 1 \leq j \leq J _ { \ L }$ ) are distinct fibers of two different rulings such that $G _ { i } \cap G _ { j } \cap M _ { 1 } = \emptyset$ .

(12) $Y _ { \mathrm { m i n } } = \mathbf { F } _ { 2 }$ ; $\begin{array} { r } { \Gamma = M _ { 1 } + \sum _ { \ell = 1 } ^ { J } g _ { \ell } G _ { \ell } + h H _ { 1 } } \end{array}$ ( $0 \leq h \leq 3$ i ); $( m , k ) = ( 2 , 1 )$ ; $\begin{array} { r } { g _ { 1 } = 3 - h ; \sum _ { j = 2 } ^ { J } g _ { j } = 2 h } \end{array}$ $H _ { 1 }$ is the unique $\left( - 2 \right)$ -curve on $\mathbf { F } _ { 2 }$ ; $M _ { 1 }$ and $G _ { 1 }$ are two sections of self intersection 2 and intersect each other at two distinct points; $G _ { j }$ $\langle 2 \leq j \leq J \rangle$ ) are distinct fibers not through $M _ { 1 } \cap G _ { 1 }$ ; when $h = 0$ (resp.
$h = 3$ ), there is no such $G _ { j }$ (resp.
no such $G _ { 1 }$ ).

(13) $Y _ { \mathrm { m i n } } = \mathbf { F } _ { b }$ W $\left( b \geq 2 \right)$ ; $\begin{array} { r } { \Gamma = k M _ { 1 } + 4 G _ { 1 } + \sum _ { i = 1 } ^ { 2 ( b + 2 ) - k } H _ { i } } \end{array}$ ; $( m , k ) = ( 0 , k )$ with $1 \leq k < 2 ( b + 2 )$ $G _ { 1 }$ is the unique $( - b )$ -curve; $M _ { 1 }$ and $H _ { i }$ are fibres; $H _ { i } = H _ { j }$ is allowed but $H _ { i } \neq M _ { 1 }$ .

(14) $Y _ { \mathrm { m i n } } = \mathbf { F } _ { m - 2 }$ ; $\begin{array} { r } { \Gamma = M _ { 1 } + 3 G _ { 1 } + \sum _ { j = 2 } ^ { J } g _ { j } G _ { j } } \end{array}$ ; $( m , k ) = ( m , 1 )$ with $m \geq 3$ ; $\textstyle \sum _ { j = 2 } ^ { J } g _ { j } = m + 1$ ; $G _ { j }$ $( 2 \leq j \leq J )$ are distinct fibres not through $M _ { 1 } \cap G _ { 1 }$ ; $G _ { 1 }$ is the negative section with $G _ { 1 } ^ { 2 } = - ( m - 2 )$ ; $M _ { 1 }$ is a section with $M _ { 1 } ^ { 2 } = m$ .

(15) $Y _ { \mathrm { m i n } } = \mathbf { F } _ { m - 4 }$ ; $\begin{array} { r } { \Gamma = M _ { 1 } + 3 G _ { 1 } + \sum _ { j = 2 } ^ { J } g _ { j } G _ { j } } \end{array}$ ; $( m , k ) = ( m , 1 )$ with $m \geq 4$ ; $\textstyle \sum _ { j = 2 } ^ { J } g _ { j } = m - 2$ $G _ { j }$ $( 2 \leq j \leq J )$ are distinct fibres of a fixed ruling not through $M _ { 1 } \cap G _ { 1 }$ ; $G _ { 1 }$ is a section with $G _ { 1 } ^ { 2 } = - ( m - 4 )$ ; $M _ { 1 }$ is a section with $M _ { 1 } ^ { 2 } = m$ and meeting $G _ { 1 }$ at two distinct points.

$Y _ { \operatorname* { m i n } } = \mathbf { F } _ { m }$ ; $\begin{array} { r } { \Gamma = M _ { 1 } + 3 H _ { 1 } + \sum _ { i = 1 } ^ { J } g _ { i } G _ { i } } \end{array}$ ; $( m , k ) = ( m , 1 )$ ith $m \geq 3$ $\textstyle \sum _ { i = 1 } ^ { J } g _ { i } = m + 4$ ; $H _ { 1 }$ $\smash  \left( \begin{array} { l l l } { \begin{array} { r l } \end{array} } & { \begin{array} { r l } \end{array} } & { \begin{array} { r l } \end{array} \right) } \end{array}$ $\smash { \mathbf { V } _ { \perp } } , \ j \in  { \mathbb { N } } , $ $\textbf { \em n } \pmb { \mathcal { T } } 2$ $\smash {  { \mathrm { ~  ~ { ~ \Lambda ~ } ~ } } } / 1 \bigcup _ { i = 1 }  { \mathrm { ~  ~ { ~ \Lambda ~ } ~ } } _ { T } \rvert$

fibres.

3.3 Remark (1) Let $\tau _ { 0 } : Y _ { 0 }  Y _ { \operatorname* { m i n } }$ be the blow-up of the point $p _ { 1 }$ in Cases (1)-(4), (7), (8); and we set $\tau _ { 0 } = \mathrm { i d }$ for other cases.
Then $\tau$ constructed in the proof factors through $\tau _ { 0 }$ .
Moreover, $M _ { 1 }$ on $X$ is the total transform of the proper inverse image on $Y _ { 0 }$ of $\overline { { M } } _ { 1 }$ on $Y _ { \mathrm { m i n } }$ .
So the advantage of this classification is that we can cook up a Coble surface by choosing the right material: $( Y _ { \mathrm { m i n } } , \Gamma )$ according to the customer’s taste: like request for $M _ { 1 } ^ { 2 }$ , $h ^ { 0 } ( - 2 K _ { X } + 2 { \cal E } )$ , $| k M _ { 1 } |$ , $G \cap M _ { 1 }$ , etc.

(2) $\textstyle \sum _ { i } G _ { i }$ in Case (5) or (6) must be a non-reduced divisor (see Theorem 6.3 in §6).
In Cases (11) and (15) with $m = 4$ (resp.
Case (10)), $\tau _ { y } : Y \to \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ factors through the blow-up of the intersection $\bar { G } _ { i } \cap \bar { G } _ { j }$ of fibres of different rulings for some $i , j$ , by the argument in the proof of Theorem 3.2 for Case (10) to deduce $g _ { 1 } \leq 2$ (resp.
by the uniqueness of a loop, if exists, in $M + P$ on $X$ ; see Lemma 2.2).

(3) See Examples 2.11 and 4.8 and Remark 4.9 for the realizations of Case (2) with $( m , k ) = ( 0 , 2 )$ and Cases (13) - (16).

Let us start proving Theorem 3.2.

3.4 There are two main cases to consider (Lemma 2.2):

Case I: $| M | = | k M _ { 1 } |$ , where $M _ { 1 } \cong \mathbb { P } ^ { 1 }$ and $M _ { 1 } ^ { 2 } = 0$ .  
Case II: $M \cong \mathbb { P } ^ { 1 }$ , $M ^ { 2 } = m \ge 1$ and $\dim | M | = m + 1$ (Lemma 1.7).

3.5 We begin with Case I.
In notation of Lemma 2.2, we have $\begin{array} { r } { G \cdot M _ { 1 } = \sum _ { i = 1 } ^ { J } g _ { i } G _ { i } \cdot M _ { 1 } = 4 } \end{array}$ .
Since $\begin{array} { r } { | M | + G + H = | - 2 K _ { X } + 2 E | } \end{array}$ contains a divisor , where $D \in | - K _ { X } + E | = \pi ^ { * } | - K _ { Y } |$ and the (multi-)sections $G _ { i }$ cannot be a component of a divisor from $| M |$ , we see that each $g _ { i }$ is even.
Thus either $G = 2 G _ { 1 }$ , or $G = 4 G _ { 1 }$ , or $\begin{array} { r } { G = 2 G _ { 1 } + 2 G _ { 2 } } \end{array}$ .

Since $E \cdot H = 0 , E \cdot M _ { 1 } = 0$ (Lemma 2.3), $E , H$ are all contained in fibres of the fibration given by $\lvert M _ { 1 } \rvert$ .
Applying the blow-down $\pi : X \to Y$ , we get $\vert - 2 K _ { Y } \vert \sim \vert \pi _ { * } M \vert + \pi _ { * } ( G + H )$ .
Intersecting this equality with a negative curve $C$ on $Y$ , we see that either $C \leq \pi _ { * } ( G + H )$ or $C$ is a $( - n )$ -curve with $n = 1 , 2$ .
Let $\tau : Y  \mathbf { F } _ { b }$ be a suitable smooth blow-down of $( - 1 )$ -curves in fibres of the fibration given by $| \pi _ { * } M _ { 1 } |$ .
We will choose $b$ later.

3.6 Suppose $G = 2 G _ { 1 }$ .
Then $G _ { 1 }$ is a double section of the fibration given by $\lvert M _ { 1 } \rvert$ .
Now $1 \geq$ $p _ { a } ( k M _ { 1 } + G _ { 1 } ) \ge h ^ { 0 } ( ( k - 1 ) M _ { 1 } ) = k$ implies that $k = 1$ (Lemma 1.2). By 3.5 and the proof of Lemma 4.2 below, we can choose $\tau$ so that $b = 1$ (noting that $K _ { Y } ^ { 2 } \le 0 < 8$ ).
Combining $\pi , \tau$ and the blow-down $\mathbf { F } _ { 1 } \to \mathbb { P } ^ { 2 }$ , we get a birational morphism $X \to \mathbb { P } ^ { 2 }$ .
Clearly, Case (1) occurs; indeed, deg $\Gamma = 6$ implies that the image on $\mathbb { P } ^ { 2 }$ of $H$ is a line.

Suppose that $G = 4 G _ { 1 }$ .
Then $G _ { 1 }$ is a section of the fibration given by $\lvert M _ { 1 } \rvert$ .
This times, we can choose $b = - \tau ( G _ { 1 } ) ^ { 2 } = - G _ { 1 } ^ { 2 } \geq 1$ (cf.
Lemmas 1.8 and 2.2). If $b = 1$ , combine $\pi , \tau$ and the blow-down $\mathbf { F } _ { 1 } \to \mathbb { P } ^ { 2 }$ of $\tau ( G _ { 1 } )$ and we get $X \to \mathbb { P } ^ { 2 }$ fitting Case (4).
If $b \geq 2$ , then Case (13) occurs, and $k < 2 ( b + 2 )$ by the reasonning as in 3.14.

Suppose that $G = 2 ( G _ { 1 } + G _ { 2 } )$ .
Then the $G _ { i }$ are sections of the fibration given by $\lvert M _ { 1 } \rvert$ .
Since $p _ { a } ( k M _ { 1 } + G _ { 1 } + G _ { 2 } ) \leq 1$ and by Lemma 1.3, we have $( k , G _ { 1 } \cdot G _ { 2 } ) = ( 1 , 0 ) , ( 2 , 0 ) , ( 1 , 1 )$ .
By Lemma 1.8, we may choose $b = - \tau ( G _ { 2 } ) ^ { 2 } = 1$ with $\tau ( G _ { 1 } ) \cdot \tau ( G _ { 2 } ) = G _ { 1 } \cdot G _ { 2 }$ .
Thus Case (2) or (3) occurs.

3.7 Next we consider Case II.
We have $M = M _ { 1 }$ and $\begin{array} { r } { \sum _ { i } g _ { i } G _ { i } \cdot M = 4 + M ^ { 2 } } \end{array}$ (Lemma 2.2). Denote by $\tau : X \to \mathbb { P } ^ { m + 1 }$ a morphism given by the linear system $\vert M \vert$ (cf.
Lemma 1.7). Since $\begin{array} { r } { H \cdot M = 0 = } \end{array}$ $E \cdot M = 0$ , the map $\tau$ contracts $H$ and factors through the blow-down $\pi : X \to Y$ of $E$ .

Since $M ^ { 2 } = m$ , the image of $\tau$ is a surface of degree $\leq m$ in $\mathbb { P } ^ { m + 1 }$ .
On the other hand, a nondegenerate surface in $\mathbb { P } ^ { m + 1 }$ has degree $\geq m$ .
So $\tau$ is a birational morphism onto a surface $V$ of degree $m$ .
Such surfaces were classified by del Pezzo.
According to his classification (see for example, $[ \mathrm { R e } ]$ , 27)V ig eithon $ \mathtt { m 2 }$ $\yen 123,456$ or a V mfeee $\mathrm { ~ \textit ~ { ~  ~ } ~ } - \mathrm { \ m } 5$ $\smash { \int \ldots } \qquad A \searrow$ otionel gonoll $\smash { \mathbb { T } \mathbb { r } / \int \ldots \quad \ldots \bigr \rangle }$

The latter surface is the image of a minimal ruled surface ${ \bf F } _ { n }$ under the map given by the linear system $\left| a f + s _ { 0 } \right|$ , where $f$ is the general fibre of the fixed ruling and $s _ { 0 }$ a section with $s _ { 0 } ^ { 2 } = - n$ and $m = 2 a - n , a \geq n$ .
Note that $\mathbb { F } ( k , k )$ is the projective cone over a normal rational curve $C \subset \mathbb { P } ^ { k }$ of degree $k$ .

The following result follows easily from Lemma 2.2.

# 3.8 Lemma.

(1) $G _ { i } \cdot M \leq 2$ ; if $G _ { 1 } \cdot M = 2$ then $G _ { i } \cdot M = 1$ and $G _ { i } \cap G _ { 1 } = \emptyset$ for all $i \geq 2$ .
(2) $G _ { i } \cdot G _ { j } \leq 1$ for $i \neq j$ ; if $G _ { 1 } \cdot G _ { 2 } = 1$ then $G _ { i } \cdot M = 1$ and $G _ { i } \cap ( G _ { 1 } + G _ { 2 } ) = \emptyset$ for all $i \geq 3$

Now we shall treat possibilities of $V$ in 3.7 one by one.

3.9. Suppose that $m = 4$ and $V \subset \mathbb { P } ^ { 5 }$ is a Veronese surface.
Then $M$ is the pull back of a conic in $V$ , viewed as a curve in $\mathbb { P } ^ { 2 }$ .
Hence $M \cdot G _ { i } \geq 2$ always holds.
This, together with Lemma 3.8, implies that $G = 4 G _ { 1 }$ , the image $\tau ( G _ { 1 } )$ is a line in $V = \mathbb { P } ^ { 2 }$ and Case (9) occurs.

Suppose that $m = 1$ .
Then $V = \mathbb { P } ^ { 2 }$ and $M$ is the pull back of a line.
As in the case $m = 4$ Lemma 3.8 implies that Case (5) or (6) occurs.

3.10. Now let us consider the remaining cases where $V = \mathbb { F } ( a , n )$ .
First observe that in the case $V = \mathbb { F } ( m , m ) , m \geq 2$ , the map $\tau : X  V$ factors through a birational morphism $\overline { { \tau } } : X \to \overline { { V } }$ , where $\bar { V } =  { \mathbf { F } } _ { m }$ .
Now $| M | + G + H$ is a subsystem of the pull back of the linear system $| m f + s _ { 0 } |$ .

So, in the case $V = \mathbb { F } ( a , n ) , m \geq 2$ , we have a map from $X$ onto ${ \bf F } _ { n }$ such that $| M | + G + H$ is a subsystem of the pull back of $\left| a f + s _ { 0 } \right|$ , with $2 a - n = m$ and $a \geq n$ .
Let $\overline { { G } } _ { i } \sim a _ { i } f + b _ { i } s _ { 0 }$ be the image of $G _ { i }$ , and $\overline { { H } } = h s _ { 0 }$ the image of $H$ , where $h \geq 0$ and $h \geq 1$ only when $u = \pi = \pi \iota$ .
Since $( 2 n + 4 ) f + 4 s _ { 0 } \sim - 2 K _ { \overline { { V } } }$ is linearly equivalent to the direct image of $\begin{array} { r } { M + \sum _ { i } g _ { i } G _ { i } + H } \end{array}$ , we obtain

$$
\sum _ { i = 1 } ^ { J } g _ { i } a _ { i } + a = 2 n + 4 , \sum _ { i = 1 } ^ { J } g _ { i } b _ { i } + h = 3 .
$$

In particular, $0 \leq h \leq 3$ .

¿From Lemma 3.8, we also obtain $G _ { i } \cdot M = ( a _ { i } f + b _ { i } s _ { 0 } ) \cdot ( a f + s _ { 0 } ) = a _ { i } + ( a - n ) b _ { i } = 1$ or 2. Moreover, since $\overline { { G } } _ { i }$ is irreducible, $a _ { i } \geq n b _ { i }$ , unless $( a _ { i } , b _ { i } ) = ( 0 , 1 )$ .
This easily gives the following possible types:

$$
\begin{array} { r l } & { a _ { i } = 1 , b _ { i } = 0 ; G _ { i } \cdot M = 1 ; } \\ & { a _ { i } = 1 , b _ { i } = 1 , n = 0 , a = 1 , m = 2 ; G _ { i } \cdot M = 2 ; } \\ & { a _ { i } = 2 , b _ { i } = 1 , n = 2 , a = 2 , m = 2 ; G _ { i } \cdot M = 2 ; } \\ & { a _ { i } = 1 , b _ { i } = 1 , n = 1 , a = 2 , m = 3 ; G _ { i } \cdot M = 2 ; } \\ & { a _ { i } = 0 , b _ { i } = 1 , a = n + 1 , m = n + 2 ; G _ { i } \cdot M = 1 ; } \\ & { a _ { i } = 0 , b _ { i } = 1 , a = n + 2 , m = n + 4 ; G _ { i } \cdot M = 2 . } \end{array}
$$

On the other hand, by Lemma 2.2, $\begin{array} { r } { 4 + m = \sum _ { i } g _ { i } G _ { i } \cdot M = \sum _ { i } g _ { i } [ a _ { i } + ( a - n ) b _ { i } ] } \end{array}$ .
Substituting (3.1) into this, we get

$$
( a - n ) [ 3 - \sum _ { i = 1 } ^ { J } g _ { i } b _ { i } ] = 0 .
$$

Hence either $a = n = m$ and $\textstyle \sum _ { i } g _ { i } a _ { i } = m + 4$ , or $\textstyle \sum _ { i } g _ { i } b _ { i } = 3$ and $h = 0$ .

Clearly, now we can divide into the following situations in 3.11-14.

3.11 For all $1 \ \leq \ i \ \leq \ J$ , Type 3.10 (1) occurs, i.e., $a _ { i } = 1 , b _ { i } = 0$ .
Then by (3.2) and (3.1),  
4 $\qquad \pmb { L } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb { \cdot } \qquad \pmb \pmb { \cdot } \qquad \pmb \pmb { \cdot } \qquad \pmb \pmb { \cdot } \qquad \pmb \pmb { \cdot } \qquad \pmb \pmb { \cdot } \qquad \pmb \pmb { \cdot } \qquad \pmb \pmb { \cdot } \qquad \pmb \pmb { \cdot } \qquad \pmb \pmb { \cdot } \qquad \pmb \pmb \pmb { \cdot }$ Thia 6ta Cege (12) (m 2) on Cege (16) (om > 2) of the th

In the following, we assume that for at least one $i$ , Type 3.10 (1) does not occur.

3.12 $a = n = m$ .
By 3.10, for each $i$ , either Type 3.10 (1) or (3) occurs.
In view of Lemma 3.8, we may assume that $G _ { 1 } \cdot M _ { 1 } = 2$ (resp.
$G _ { i } \cdot M _ { i } = 1$ ) and Type 3.10 (3) (resp.
(1)) occurs for $i = 1$ (resp.
for $2 \leq i \leq J$ ).
Then $n = 2$ , $\begin{array} { r } { 2 g _ { 1 } + \sum _ { j \ge 2 } g _ { j } = 6 } \end{array}$ , $g _ { 1 } + h = 3$ .
This is Case (12) with $h \leq 2$ .

¿From now on, we assume that $a \geq n + 1$ and hence $h = 0$ .

3.13 Suppose that for all $i$ , we have $G _ { i } \cdot M = 1$ .
We may assume that for $1 \leq i \leq r ; r \geq 1$ (resp.
$r + 1 \le j \le J \rangle$ , Type 3.10 (5) (resp.
(1)) occurs.
Thus $a = n + 1 , m = n + 2$ , $\textstyle \sum _ { i = 1 } ^ { r } g _ { i } \ = \ 3$ , $\begin{array} { r } { \sum _ { j = r + 1 } ^ { J } g _ { j } = m + 1 } \end{array}$ .
If $n = 0$ , Case (11) occurs.
If $n \geq 1$ , then the uniqueness of a negative curve on ${ \bf F } _ { n }$ implies that $r = 1$ .
Hence $g _ { 1 } = 3$ and $\textstyle \sum _ { j \geq 2 } g _ { j } = m + 1$ .
Case (14) occurs.

3.14 In view of Lemma 3.8, we may assume now that $G _ { 1 } \cdot M = 2$ , i.e., for $i = 1$ Type 3.10 (2), (4) or (6) occurs, and $G _ { i } \cdot M = 1$ for all $i \geq 2$ .
Then $b _ { 1 } = 1$ .
We may also assume that for $2 \leq i \leq r$ $( r \geq 1 )$ (resp.
$r + 1 \leq i \leq J$ ) Type 3.10 (5) (resp.
(1)) occurs.
Thus $\begin{array} { r } { g _ { 1 } + \sum _ { i = 2 } ^ { r } g _ { i } = 3 } \end{array}$ , $\begin{array} { r } { g _ { 1 } a _ { 1 } + \sum _ { j = r + 1 } ^ { J } g _ { j } + a = 2 n + 4 } \end{array}$ .

If Type 3.10 (6) occurs when $i = 1$ , then $a = n + 2 , m = n + 4$ ; hence $r = 1$ , $\begin{array} { r } { g _ { 1 } = 3 , \sum _ { j \geq 2 } g _ { j } = m - 2 } \end{array}$ so Case (15) occurs.

If Type 3.10 (2) occurs when $i = 1$ , then $a = 1$ , $\begin{array} { r } { n = 0 , m = 2 , g _ { 1 } + \sum _ { i = 2 } ^ { r } g _ { i } = g _ { 1 } + \sum _ { j \geq r + 1 } g _ { j } = 3 } \end{array}$ .
So Case (10) occurs.
We note that $g _ { 1 } \leq 2$ for otherwise $Y  \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ is the blow-up of points on $G _ { 1 } \backslash M$ and their immediate infinitely near points (cf.
Lemma 1.9) and $G _ { 1 } + M \in \vert - K _ { Y _ { \mathrm { m i n } } } \vert$ would give rise to a member in $\vert - K _ { X } \vert$ $( = \emptyset$ ), a contradiction.

Suppose that Type 3.10 (4) occurs when $i \ : = \ : 1$ .
Then $a = 2$ , $n = 1 , m = 3 , g _ { 1 } + \textstyle \sum _ { i = 2 } ^ { r } g _ { i } =$ $\textstyle 3 , g _ { 1 } + \sum _ { j = r + 1 } ^ { J } g _ { j } = 4$ .
Thus, either $r = 1$ , or $r = 2$ and $\overline { { G } } _ { 2 }$ is the unique $( - 1 )$ -curve on $\mathbf { F } _ { 1 }$ =.
If $r = 1$ then $g _ { 1 } = 3 , g _ { 2 } = 1$ ; we blow down the $( - 1 )$ -curve $s _ { 0 }$ and see that Case (7) occurs.
If $r = 2$ , then $\begin{array} { r } { g _ { 1 } + g _ { 2 } = 3 , g _ { 1 } + \sum _ { j \geq 3 } g _ { j } = 4 } \end{array}$ ; we blow down the $( - 1 )$ -curve $\overline { { G } } _ { 2 }$ and see that Case (8) occurs.
This completes the proof of Theorem 3.2.

# 4. Basic surfaces

4.1 A rational surface is called basic if it admits a birational morphism to $\mathbb { P } ^ { 2 }$ [Ha].
In the present section, we shall describe minimal Coble surfaces which are basic surfaces.

We start with the following well-known result:

4.2 Lemma.
Let $V$ be a rational surface.
Suppose that $V$ does not have smooth rational curves with self-intersection $\leq - 3$ .
Then $V$ is a basic surface unless it is isomorphic to $\mathbf { F } _ { 0 }$ or $\mathbf { F } _ { 2 }$ .

Proof.
Let $\pi : V  S$ be a birational morphism to a minimal rational surface $S$ .
If $S \cong \mathbb { P } ^ { 2 }$ or $\mathbf { F } _ { 1 }$ , we are done.
If $S \cong \mathbf { F } _ { b }$ with $b \geq 3$ , then the proper inverse transform of the negative section $s _ { 0 }$ on $S$ is a curve on $V$ with self-intersection $\leq - b$ , contradicting the assumption.
If $S = \mathbf { F } _ { 2 }$ , then the same argument shows that $\pi$ is an isomorphism over the negative section $s _ { 0 }$ .
So $\pi$ factors through a map $V ^ { \prime }  S$ which is the blow-up at a point on a fibre not lying on $s _ { 0 }$ .
We blow down the proper transform of this fibre on $V ^ { \prime }$ to get a morphism $V  \mathbf { F } _ { 1 }$ .
The case $S = \mathbf { F } _ { 0 }$ is similar.

4.3 Theorem.
Any Coble surface $X$ of elliptic type is basic.

Proof.
We may assume that $X$ is of elliptic type with respect to some $E$ (cf.
Definition 2.9). By Remark 2.6 and Theorem 2.8, $X$ is either one blow-up of an Halphen surface of index 2, or is obtained by blowing up a Jacobian elliptic surface $Y _ { \mathrm { m i n } }$ to get $X ^ { \prime }$ and then blowing down linear chains of total length $m \leq 6$ (Remark 2.9). An Halphen surface is a basic surface since it does 1 +1 if $\angle \cdot \mathrm { ~ \bf ~ \delta ~ }$ +h fell c +

formula for the canonical class).
So, in the Halphen case $X$ is basic.
For the Jacobian case, note that the exceptional divisors of $X ^ { \prime }  Y _ { \mathrm { m i n } }$ and $X ^ { \prime }  X$ are disjoint.
Thus there are smooth blow-downs $Y _ { \operatorname* { m i n } }  Z$ and $Y  Z$ fitting the following commutative diagram (the rectangular part):

$$
X ^ { \prime } \stackrel { \pi ^ { \prime } } { \longrightarrow } Y ^ { \prime } \longrightarrow Y _ { \mathrm { m i n } }
$$

$$
\stackrel { \downarrow } { \substack { X  Y \longrightarrow Z \longrightarrow \mathbb { P } ^ { 2 } } }
$$

Since $Y _ { \mathrm { m i n } }$ satisfies the hypothesis of Lemma 4.2 so does $Z$ .
Therefore, there is a smooth blow-down $Z \to \mathbb { P } ^ { 2 }$ because $K _ { Z } ^ { 2 } = m + K _ { Y _ { \mathrm { m i n } } } ^ { 2 } < 8$ .
Theorem 4.3 follows.

4.4 Now let us assume that $X$ is a Coble surface of rational type with respect to a $( - 1 )$ -curve $E$ .
Write $| - 2 K _ { X } + 2 E | = | M | + P$ as in 2.1. By Theorem 3.2 and Remark 3.3, $X$ is basic unless one of Cases (12)-(16) occurs.
In these five cases we have a birational morphism $X  \mathbf { F } _ { d }$ .
If Case (13) occurs, then $M = k M _ { 1 }$ and $\lvert M _ { 1 } \rvert$ is a free pencil of rational curves.
There is no upper bound for $k$ (see Example 4.8 below); of course if $X$ dominates $\mathbb { P } ^ { 2 }$ , via the blow-down $\pi : X \to Y$ of $E$ , then $k \leq 6$ .
If one of Cases (12), (14)-(16) in Theorem 3.2 occurs, then $M$ is a smooth rational curve with $m = M ^ { 2 } \ge 2$ ; again there is no upper bound for $m$ (see Remark 4.9 below); however if $X$ dominates $\mathbb { P } ^ { 2 }$ , via $\pi$ , then clearly $M ^ { 2 } \leq 3 6$ .
We can do much better.
We shall start with the following:

4.5 Lemma.
Let $C$ be an irreducible rational plane curve of degree $4 \leq d \leq 6$ .
Assume that $C$ does not have a singular point of multiplicity $d - 1$ and, in the case $d = 6$ , there is a a point of multiplicity $\geq 3$ .
Then there exists a Cremona transformation with fundamental points among singular points of $C$ such that the image of $C$ is a curve of degree $\leq 3$ .

Proof.
We may assume that $M ^ { 2 } \geq 1$ and hence the general member $M$ of $| M |$ is a smooth $\smash { \mathrm { ~ \bf ~ { ~ r ~ } ~ } \to \mathrm { ~ \bf ~ { ~ r ~ } ~ } \to \mathrm { ~ \bf ~ { ~ v ~ } ~ } \to \mathrm { ~ \bf ~ { ~ v ~ } ~ } }$ he the blem deun ef $\pmb { r } , \tau$ rrhieh : imhbounleed

Proof.
Let $m _ { 1 } \geq m _ { 2 } \geq . . . \geq m _ { k }$ be the multiplicities of singular points of $C$ (including infinitely near points).
Consider the vector $( d ; m _ { 1 } , \ldots , m _ { k } )$ .

Case $d = 4$ .
The possible multiplicities of singular points are $( m _ { 1 } , \ldots , m _ { k } ) = ( 4 ; 2 , 2 , 2 )$ .
We apply the standard quadratic Cremona transformation $T$ with centers at the singular points to get a conic.

Case $d = 5$ .
Then $( d ; m _ { 1 } , \ldots , m _ { k } ) = ( 5 ; 3 , 2 , 2 , 2 ) ; ( 5 ; 2 , 2 , 2 , 2 , 2 , 2 )$ .
In the first case, applying $T$ as above with centers at the first three points, we get $( d ^ { \prime } ; m _ { 1 } ^ { \prime } , \ldots , m _ { k } ^ { \prime } ) = ( 3 ; 2 )$ .
In the second case, we use the Cremona transformation given by the linear system of quintics through the singular points of the curve.
We get a line.

Case $d = 6$ .
Assume $C$ has a point of multiplicity 4. Then $( d ; m _ { 1 } , \ldots , m _ { k } ) = ( 6 ; 4 , 2 , 2 , 2 , 2 )$ .
We make a standard Cremona transformation at the first three points.
Then $( d ^ { \prime } ; m _ { 1 } ^ { \prime } , \ldots , m _ { k } ^ { \prime } ) =$ $( 4 ; 2 , 2 , 2 )$ .
Applying again the standard quadratic Cremona transformation we get a conic.

Assume $C$ has a point of multiplicity 3 but no points of multiplicity 4. Then $( d ; m _ { 1 } , \ldots , m _ { k } ) =$ $( 6 ; 3 , 3 , 3 , 2 ) , ( 6 ; 3 , 3 , 2 , 2 , 2 , 2 ) , ( 6 ; 3 , 2 , 2 , 2 , 2 , 2 , 2 , 2 )$ ).
Again we make the standard quadratic Cremona transformation at the first three points.
We get $( d ^ { \prime } ; m _ { 1 } ^ { \prime } , \ldots , m _ { k } ^ { \prime } ) = ( 3 ; 2 ) , ( 4 ; 2 , 2 , 2 ) , ( 5 ; 2 , 2 , 2 , 2 , 2 , 2 )$ .
In the second case we apply again the standard qyadratic Cremona transformation to get a nonsingular conic.
In the third case we apply the Cremona transformation given by quintics through the six singular points of the curve.
We get a line.

4.6 Proposition.
Assume that a Coble surface $X$ admits a birational morphism $\tau : X  \mathbb { P } ^ { 2 }$ with $E$ a $( - 1 )$ -curve on it blown down.
Suppose further that $X$ is of rational type with respect to $E$ , and write $| - 2 K _ { X } + 2 E | = | M | + P$ as in 2.1. Then $M ^ { 2 } \leq 5$ (the equality is realizable).

4.0 Fopl。Lot。h+ of the divisor $M + P$ which is disjoint from $E$ (Lemma 2.3). Then $\tau$ is the composition of $\pi$ and a birational morphism $\tau _ { Y } : Y \to \mathbb { P } ^ { 2 }$ .
We have $| - 2 K _ { Y } | = | \pi ( M ) | + \pi ( P )$ (Lemma 2.3).

First observe that ${ \overline { { M } } } : = \tau ( M ) = \tau _ { Y } ( \pi ( M ) )$ is a component of the sextic $D : = \tau _ { * } ( { \cal M } + { \cal P } ) \in$ $\lvert - 2 K _ { \mathbb { P } ^ { 2 } } \rvert$ , and $\tau : M \to M$ is a resolution of the rational curve $\bar { M }$ .
In particular, $d : = \deg M \leq 6$ .
If $M$ has at worst $r$ double singular points (this is true when $d \leq 3$ ), then $r = ( d - 1 ) ( d - 2 ) / 2$ and $M ^ { 2 } \leq d ^ { 2 } - 4 r \leq 5$ .

Thus, we may assume that $d = 4 , 5 , 6$ and $M$ has a singular point of multiplicity $\geq 3$ .
Note that the surface $Y$ is obtained from $\mathbb { P } ^ { 2 }$ by successive blow-ups of singular points of effective antibicanonical divisors.
Let $T : \mathbb { P } ^ { 2 }  \mathbb { P } ^ { 2 }$ be a Cremona transformation with fundamental points in the set $\Sigma$ of indeterminancies of the rational map $\tau _ { Y } ^ { - 1 }$ .
Clearly, Sing $D \subseteq \Sigma$ .
Composing $T$ with $\tau _ { Y }$ , we get another birational morphism $Y  \mathbb { P } ^ { 2 }$ such that $D$ is replaced with the image of $\boldsymbol { D }$ under $T$ .

Let us show that this could be used to reduce our proof to the case when $d = \deg \bar { M } \leq 3$ .
Consider first the case $d = 6$ .
If $D = \bar { M }$ does not have a point of multiplicity 5, we apply Lemma 4.5 to get a Cremona transformation $T$ such that the image of $D$ is a cubic.
If $\boldsymbol { D }$ has a point $p$ of multiplicity 5, then the indeterminacy set $\Sigma$ of $\tau _ { Y } ^ { - 1 }$ consists of $p$ and its infinitely near points.
Applying Lemma 1.9 repeatedly, we see that $\vert - K _ { Y } \vert$ contains a member $3 F ^ { \prime } + 2 E _ { 0 } ^ { \prime } +$ (an effective divisor), where $E _ { 0 } ^ { ' }$ is the proper inverse transform of the exceptional curve lying over $p$ and $F$ is a smooth fibre of a $\mathbb { P } ^ { 1 }$ -fibration whose image on $\mathbb { P } ^ { 2 }$ is a line through $p$ .
This implies $\vert - K _ { X } \vert \neq \varnothing$ , a contradiction.

Consider the case $d = 5$ .
Then the residual component of $\bar { M }$ in $D$ is a line $L$ .
If all singular points of $\bar { M }$ are of multiplicity $\leq 3$ , then applying the previous lemma, we reduce $\bar { M }$ to a curve of degree $\leq 3$ .
If $\bar { M }$ has a point $p$ of multiplicity 4, we apply the standard Cremona transformation with fundamental points at $p$ and two points from the set $\Sigma \cap L \cap \bar { M }$ ; for the existence of these two points, we note that the proper inverse transform on $Y$ of $L$ and $M$ should meet each other at most twice (Lemma 2.2), while $L \cdot M = 5$ , whence we need to blow up at least 3 points in $L \cap M$ (including infinitely near).
This will transform $M$ to a quartic with a triple point.

If $\bar { M }$ is a quartic with a triple point $p$ , then the residual curve in $D$ is a conic $Q$ (possibly a double line $2 L$ ).
We apply the standard Cremona transformation with fundamental points at $p$ and two points from the set $\Sigma \cap Q \cap \bar { M }$ , which exist by the above reasonning.
This will transform $\bar { M }$ to a cubic.
Thus we have reduced to the case $d \leq 3$ and Proposition 4.6 is proved.

4.7 Theorem.
Any Coble surface $X$ with $h ^ { 0 } ( - 2 K _ { X } ) \ge 7$ is not basic (see Example 4.8 below for $X$ with arbitrarily large anti-bicanonical dimension).

Proof.
Let $W$ be a Coble surface with $h ^ { 0 } ( - 2 K _ { W } ) \ge 7$ .
Suppose the contrary that there is a birational morphism $W \to { \mathbb { P } } ^ { 2 }$ .
Clearly this map factors through $W  X$ with $X$ minimal Coble.
Note also that $h ^ { 0 } ( - 2 K _ { X } ) \ge h ^ { 0 } ( - 2 K _ { W } ) \ge 7$ .
Take any $( - 1 )$ -curve $E$ on $X$ blown down by the map $X \to \mathbb { P } ^ { 2 }$ .

Write $| - 2 K _ { X } + 2 E | = | M | + P$ as in 2.1. If $p _ { a } ( M ) = 1$ or $p _ { a } ( M ) = 0$ with $M = k M _ { 1 }$ and $M ^ { 2 } = 0$ , then $h ^ { 0 } ( X , - 2 K _ { X } ) \leq h ^ { 0 } ( X , M ) - 1 = M ^ { 2 } \leq 6$ , or $h ^ { 0 } ( X , - 2 K _ { X } ) \leq h ^ { 0 } ( X , k M _ { 1 } ) - 1 = k \leq$ $\mathrm { d e g } ( - 2 K _ { \mathbb { P } ^ { 2 } } ) = 6$ (cf.
Lemma 1.7, Remark 2.9), a contradiction, where we used the fact that $E$ is not in the fixed part of $\lvert - 2 K _ { X } + 2 E \rvert$ (Lemma 2.3).

Therefore, the hypothesis of Proposition 4.6 is satisfied and we have $h ^ { 0 } ( - 2 K _ { X } ) \leq h ^ { 0 } ( X , M ) - 1 =$ $M ^ { 2 } + 1 \le 6$ .
This contradiction proves Theorem 4.7.

4.8 Proposition.
Given any integers $a , b$ with $a \ge 4$ and $b \geq 2 a$ , there is a Coble surface $X$ which does not admit any birational morphism $X ~  ~ \mathbb { F } _ { d }$ , where $d \leq a - 3$ and which satisfies $h ^ { 0 } ( X , - 2 K _ { X } ) = a$ and $K _ { X } ^ { 2 } = 4 - a - b$ .

We prove this result by constructing examples fitting Case (13) of Theorem 3.2.

Let $s _ { 0 }$ be the negative section on $S = \mathbf { F } _ { b }$ with self-intersection $- b$ and $F ^ { \prime }$ a fibre.
Take distinct fibers $F _ { \ell }$ ( $1 \leq \ell \leq b - t - ( n - 2 ) )$ ).
Then we can write

$$
- K _ { S } = 2 s _ { 0 } + \sum _ { i = 1 } ^ { r } { F _ { i } } + 2 \sum _ { j = r + 1 } ^ { r + s } { F _ { j } } + 3 \sum _ { k = r + s + 1 } ^ { r + s + t } { F _ { k } } ,
$$

$$
- 2 K _ { S } = n F + 4 s _ { 0 } + 2 \sum _ { i = 1 } ^ { r } F _ { i } + 3 \sum _ { j = r + 1 } ^ { r + s } F _ { j } + 5 \sum _ { k = r + s + 1 } ^ { r + s + t } F _ { k } ,
$$

where we set

$$
r = b - t - 2 ( n - 1 ) , s = n - t .
$$

Let $\sigma : Y  S$ be the composite of the blow-ups of smooth points on $F _ { \ell } \setminus s _ { 0 }$ and their infinitely near points such that

$$
\begin{array} { r } { \sigma ^ { * } ( F _ { i } ) = H _ { i } + J _ { i } , ~ \sigma ^ { * } ( F _ { j } ) - J _ { j } = H _ { j } + 2 E _ { j } + 2 B _ { j } , } \end{array}
$$

$$
\sigma ^ { * } ( F _ { k } ) - J _ { k } = H _ { k } + 2 E _ { k } + 2 B _ { k } + 2 C _ { k } + 2 D _ { k }
$$

have the following dual graphs:

$$
\begin{array} { c } { { ( - 1 ) - ( - 1 ) , } } \\ { { \ } } \\ { { ( - 2 ) - ( - 2 ) - ( - 1 ) , } } \\ { { \ } } \\ { { ( - 2 ) - ( - 2 ) - ( - 2 ) - ( - 2 ) - ( - 1 ) . } } \end{array}
$$

Here $H _ { \ell }$ is the proper inverse transform of $F _ { \ell }$ , and $J _ { u }$ ( $\mathit { a } = \mathit { j }$ or $u \ : = \ : k$ ) is a $( - 2 )$ -curve with $J _ { u } \cdot E _ { u } = 1$ .

Then $- K _ { Y }$ equals

$$
\mathcal { I } _ { 1 } + \sum _ { i } H _ { i } + \sum _ { j } ( 2 H _ { j } + 2 E _ { j } + J _ { j } + B _ { j } ) + \sum _ { k } ( 3 H _ { k } + 4 E _ { k } + 2 J _ { k } + 3 B _ { k } + 2 C _ { k } + 4 H _ { k } )
$$

and $- 2 K _ { Y } = n M _ { 1 } + 4 G _ { 1 } + H$ where $G _ { 1 } : = \sigma ^ { * } ( s _ { 0 } )$ , $M _ { 1 } : = \sigma ^ { * } ( F )$ .
Here we set

$$
I = 2 \sum _ { i } H _ { i } + \sum _ { j } ( 3 H _ { j } + 2 E _ { j } + J _ { j } ) + \sum _ { k } ( 5 H _ { k } + 6 E _ { k } + 3 J _ { k } + 4 B _ { k } + 2 C _ { k } ) .
$$

Let $q \in Y$ be a point which either lies on $F _ { 0 } \setminus G _ { 1 }$ with a smooth fibre $F _ { 0 } \sim M _ { 1 }$ , or on $J _ { i } \setminus H _ { i } , i \leq r$ .
Let $\pi : X \to Y$ be the blow-up of $Y$ at $q$ and $E$ the exceptional curve.
We claim:

(1) $X$ is a Coble surface.  
(2) $| - 2 K _ { X } + 2 E | = | M | + G$ , where $M = \pi ^ { * } ( n M _ { 1 } ) = n ( \sigma \circ \pi ) ^ { * } ( F ) { \mathrm { ~ a n d ~ } } G = 4 \pi ^ { * } G _ { 1 } + \pi ^ { * } H$ .  
(3) $h ^ { 0 } ( X , M ) = n + 1$ and $h ^ { 0 } ( X , - 2 K _ { X } ) = n - 1$ .  
(4) $K _ { X } ^ { 2 } = 5 - ( n + t + b )$ .
In the following we assume that $n + t \geq 5$ and $q$ lies on a smooth fibre $F _ { 0 }$ .  
(5) $X$ does not admit a birational morphism to $\mathbf { F } _ { d }$ with $d \leq n + t - 4$ .
In particular, $X$ is not a basic surface.
Moreover, all negative curves $\left( \neq \pi ^ { - 1 } G _ { 1 } \right)$ ) are contained in fibres.  
(6) Suppose that $r = 0$ , i.e., $b = t + 2 ( n - 1 )$ .
Let $X  X _ { \operatorname* { m i n } }$ be the blow-down of the proper inverse transform of $F _ { 0 }$ .
Then $X _ { \mathrm { m i n } }$ is a minimal Coble surface.  
(7) Denote by $B _ { j } ^ { \prime }$ (when $s > 0$ ), $D _ { k } ^ { \prime }$ (when $t > 0$ ) the proper images on $X _ { \mathrm { m i n } }$ of $B _ { j } , D _ { k }$ .
Then both mobile parts of $| - 2 K _ { X _ { \mathrm { m i n } } } + 2 B _ { j } ^ { \prime } |$ and $| - 2 K _ { X _ { \mathrm { m i n } } } + 2 D _ { k } ^ { \prime } |$ are equal to $\lvert ( n + 1 ) F \rvert$ with $\pmb { T } , \pmb { \rceil }$ 1 Gull Gb f+l P1 $\mathbf { v }$

For (2), we only need to show that $\left| - 2 K _ { Y } \right| = \left| n M _ { 1 } \right| + 4 G _ { 1 } + H$ .
To do so, we use the fact that for an effective divisor $L$ and irreducible divisors $N _ { i }$ , if $L \cdot N _ { 1 } < 0 , ( L - N _ { 1 } ) \cdot N _ { 2 } < 0 , \cdot \cdot \cdot , ( L - \sum _ { i = 1 } ^ { v - 1 } N _ { i } ) \cdot N _ { v } <$ $0$ , then $\sum N _ { i }$ is a partial fixed part of $| L |$ .
Inductively, one can verify that $\mid - 2 K _ { Y } \mid$ contains the following as its partial fixed part:

$$
\begin{array} { l } { + \displaystyle \sum ( H _ { u } + E _ { u } + J _ { u } + B _ { k } + C _ { k } ) + G _ { 1 } + \displaystyle \sum ( H _ { u } + E _ { u } ) + G _ { 1 } + } \\ { ~ } \\ { \displaystyle \sum ( H _ { i } + H _ { u } + B _ { k } + E _ { k } + J _ { k } + E _ { k } + H _ { k } ) + G _ { 1 } + \displaystyle \sum H _ { i } , } \end{array}
$$

which is equal to $4 G _ { 1 } + 2 \sum H _ { i } +$ (other components).
Since $- 2 K _ { Y } - ( 4 G _ { 1 } + 2 \textstyle \sum _ { i } H _ { i } )$ is a disjoint union of $n M _ { 1 }$ and a negative definite divisor contained in fibers, $| n M _ { 1 } |$ is the mobile part of $\vert - 2 K _ { Y } \vert$ .

For the last part of (5), we assume $n \geq 5$ for simplicity.
Note that $- 2 K _ { X } \sim ( n - 2 ) \pi ^ { * } M _ { 1 } + G +$ $2 \pi ^ { - 1 } ( F _ { 0 } )$ .
Suppose the contrary that $C$ $\left( \neq \pi ^ { - 1 } G _ { 1 } \right)$ is a negative curve not contained in fibres.
Then $C \cdot ( - 2 K _ { X } ) \geq ( n - 2 ) M _ { 1 } \cdot \pi _ { * } C \geq n - 2 \geq 3$ .
This leads to that $2 p _ { a } ( C ) - 2 = C ^ { 2 } + C \cdot K _ { X } \leq - 1 - 2$ , a contradiction.
The rest of the Claim can now be verified with patience.

4.10 Remark.
For each $N = 1 4 , 1 5 , 1 6$ , we can construct similar Coble surfaces $X$ fitting Case (N) of Theorem 3.2 (as well as minimal Coble surface $X _ { \mathrm { m i n } }$ obtained as a single blow-down of $X$ ) and with arbitrarily large $- K _ { X } ^ { 2 }$ and $h ^ { 0 } ( - 2 K _ { X } )$ but with no birational morphism $X \to \mathbb { P } ^ { 2 }$ (cf.
4.7 and 5.6).

# 5. Coble sextics

Let $X$ be a basic Coble surface.
So there is a birational morphism $X \to \mathbb { P } ^ { 2 }$ .
The image of any divisor $D \in \vert - 2 K _ { X } \vert$ in $\mathbb { P } ^ { 2 }$ is a member of $\lvert - 2 K _ { \mathbb { P } ^ { 2 } } \rvert$ , whence a plane sextic.
A plane sextic which is the image of an anti-bicanonical divisor of a basic Coble surface (which we may assume minimal) will be called a Coble sextic.
In this section we shall describe Coble sextics.

5.1 Assume that $X$ is a minimal Coble surface of Halphen type.
Then it is obtained by blowing up a singular point of a fibre on an Halphen surface $V$ of index 2. We have already explained that $V$ is a basic surface.
The image on $\mathbb { P } ^ { 2 }$ of the pencil of elliptic curves on $V$ is an Halphen pencil of index 2 of elliptic curves of degree 6 with 9 double base points, including infinitely near.
There is a unique plane cubic $C$ through the base points, and the base points add up to a non-trivial 2-torsion point on the cubic with one of the inflection points chosen as the origin (see [CD,Do1]).
Even when the cubic is a nodal curve, this makes sense.
The cubic $C$ taken with multiplicity 2 is a member of the Halphen pencil.

A Coble sextic corresponding to $X$ is a member of an Halphen pencil of index 2 which has a singular point $p$ such that a preimage on $X$ of $p$ is also a singular point of a fibre dominating a member $\neq 2 C )$ of the pencil on $\mathbb { P } ^ { 2 }$ .
The classical Coble sextic is of this type.
The Halphen pencil has 9 distinct double base point, and an irreducible member of the pencil with an extra singular point $p$ is a rational sextic with 10 nodes.

5.2 Assume now that $X$ is a minimal Coble surface of Jacobian type as described in Theorem 2.8.  
We use the commutative diagram in the proof of Theorem 4.3.

Suppose that the center $q$ of the blow-up $\pi ^ { \prime } : X ^ { \prime } \to Y ^ { \prime }$ is a singular point of the fibre $F ^ { \prime }$ (this is not always true as shown in Example 2.10). Then by Remark 2.9, $X ^ { \prime }$ is a Coble surface and a member $D ^ { \prime }$ of $\vert - 2 K _ { X ^ { \prime } } \vert$ is of the form $D ^ { \prime } : = F _ { 1 } ^ { \prime } + F ^ { \prime } +$ (an effective divisor contractible by the map $X ^ { \prime }  Y _ { \mathrm { m i n } }$ ), where $F _ { 1 } ^ { \prime } , F ^ { \prime }$ are the proper inverse transforms of the two distinct fibres $F _ { 1 } , F $ on $Y _ { \mathrm { m i n } }$ .
The image $\boldsymbol { D }$ on $X$ of this $D ^ { \prime }$ is a member of $\vert - 2 K _ { X } \vert$ .
Now the commutatitve diagram in Theorem 4.2 ghorg thet the imome of $\curvearrowleft$ unden the $\textbf { \textit { v } } \cdot \textbf { \textit { m } } ^ { 2 }$ ic-ocuol to tho in6 of $\smash {  { \mathcal { L } } _ { \varepsilon ^ { \prime } } } \qquad \mapsto \qquad \mapsto \qquad \varepsilon ^ { \prime } \in  { \mathcal { L } }$ under the map $Y _ { \mathrm { m i n } }  \mathbb { P } ^ { 2 }$ .
Thus $X$ or rather its anti-bicanonical divisor $D$ , defines a Coble curve which is the union of two singular members of a cubic pencil dominated by the elliptic fibration on $Y _ { \mathrm { m i n } }$ .

For general $q$ in $F ^ { \prime }$ , as above, the sextic image $\Sigma$ of $M + P \in \vert - 2 K _ { X } + 2 E \vert$ (or equivalently of $\pi _ { * } ( M + P ) \in | - 2 K _ { Y } | ,$ ) under the birational morphism $X \ { \overset { \pi } { \to } } \ Y \to \mathbb { P } ^ { 2 }$ , is equal to the image of $M _ { 1 } ^ { \prime } + P ^ { \prime }$ (see (2.4)) under the map $X ^ { \prime }  \mathbb { P } ^ { 2 }$ , and hence equal to the image of $F _ { 1 } + F$ under the map $Y _ { \mathrm { m i n } }  \mathbb { P } ^ { 2 }$ (cf.
Remark 2.9). If either $F$ is smooth elliptic or both $F$ and $F _ { 1 }$ have irreducible images on $\mathbb { P } ^ { 2 }$ , such $\Sigma$ would never be realized from a Coble surface of rational type (cf.
Corollary 5.5 below).

5.3 Remark.
The birational morphism $X \to \mathbb { P } ^ { 2 }$ constructed in Theorem 4.3 is not unique as the following example shows.
Let $C _ { 5 }$ be a plane curve of degree 5 with six nodes.
Let $L$ be a line intersecting $C _ { 5 }$ at five distinct points.
Let us show that the sextic $C _ { 5 } + L$ is a Coble sextic obtained from a Coble surface of Jacobian type.
Let $f : Y ^ { \prime } \to \mathbb { P } ^ { 2 }$ be the blow-up of 5 nodes $p _ { i }$ of $C _ { 5 }$ and four common points $q _ { j }$ of $C _ { 5 }$ and $L$ .
The surface $Y ^ { \prime }$ has an elliptic pencil $\Lambda$ spanned by the proper transform $F _ { 1 }$ of $C _ { 5 }$ and the union $F _ { 2 } = L ^ { \prime } + 2 C _ { 2 } ^ { \prime }$ of the proper transforms of $L$ and the double conic $2 C _ { 2 }$ through the points $p _ { i }$ .
The pre-image of the point $q \in C _ { 5 } \cap L$ different from $q _ { j }$ ’s is the unique base point of the pencil $\Lambda$ .
The curves $F _ { 1 }$ and $F _ { 2 }$ are singular members of the pencil.
The singular point of $F _ { 1 }$ is the pre-image of the node $p$ of $C _ { 5 }$ different from the points $p _ { i }$ ’s.
The $C _ { 2 } ^ { \prime }$ is now a $( - 1 )$ -curve.
Let $\gamma : X  Y ^ { \prime }$ be the blow-up of the singular point of $F _ { 1 } ^ { \prime }$ with $E _ { 1 }$ the exceptional curve.
It is easy to see that $X$ is a minimal Coble surface of Jacobian type with respect to $E _ { 1 }$ and also $C _ { 2 } ^ { \prime }$ and with $\vert - 2 K _ { X } \vert = \{ C _ { 5 } ^ { \prime } + L ^ { \prime } \}$ , where $C _ { 5 } ^ { \prime }$ is the proper inverse of $C _ { 5 }$ (or $F _ { 1 }$ ).
The image of the anti-bicanonical divisor of $X$ in $\mathbb { P } ^ { 2 }$ , under the map $f \circ \gamma : X \to \mathbb { P } ^ { 2 }$ , is equal to $D _ { 6 } = C _ { 5 } + L$ with 11 nodes $p _ { i } , i = 1 , \ldots , 5 , q _ { j } , j = 1 , \ldots , 4$ and $p , q$ .

On the other hand, following Theorem 4.3, we blow down $E _ { 1 }$ , the $( - 1 )$ -curve $C _ { 2 } ^ { \prime }$ in $F _ { 2 }$ (to get $Y _ { \mathrm { m i n } }$ after further blow up the base point of $\Lambda$ ) and also sections and fibre components on $Y _ { \mathrm { m i n } }$ , we get a new birational morphism $\sigma : X  \mathbb { P } ^ { 2 }$ , which maps the anti-bicanonical divisor of $X$ onto the union of two nodal cubics (the images on this “new” $\mathbb { P } ^ { 2 }$ of $C _ { 5 } ^ { \prime } , L ^ { \prime } )$ .
The two different Coble sextics on two “different” $\mathbb { P } ^ { 2 }$ derived from the same surface $X$ are related by the Cremona transformation of $\mathbb { P } ^ { 2 }$ defined by the two different birational morphisms from $X$ to $\mathbb { P } ^ { 2 }$ .
It can be given by the linear system of quintics with double points at $q , p _ { i } , i = 1 , \ldots , 5$ , if one chooses $\sigma$ properly.

Next we consider Coble surface $X$ of rational type with respect to a $( - 1 )$ -curve $E$ on it.
As in Lemma 2.2, write $| - 2 K _ { X } + 2 E | = | M | + P$ , $M = k M _ { 1 }$ , $M _ { 1 } \cong \mathbb { P } ^ { 1 }$ , $P = G + H$ , $\begin{array} { r } { G = \sum _ { i = 1 } ^ { J } g _ { i } G _ { i } } \end{array}$ , $\begin{array} { r } { H = \sum _ { j } H _ { j } } \end{array}$ .
We note that if $\sigma : X  \mathbb { P } ^ { 2 }$ is a birational morphism, factoring as the blow-down $\pi : X \to Y$ of the curve $E$ and a morphism $\sigma _ { y } : Y \to \mathbb { P } ^ { 2 }$ , then $\Sigma : = \sigma _ { * } ( M + P )$ is a sextic plane curve and equal to the $\sigma _ { y }$ -image of the member $\pi _ { * } ( M + P )$ in $\mid - 2 K _ { Y } \mid$ .
We shall prove:

Theorem 5.4. Assume that $X$ is a basic surface of rational type with $E$ blown down by the map onto $\mathbb { P } ^ { 2 }$ .
Then there is a (possibly new) birational morphism $\sigma : X \to \mathbb { P } ^ { 2 }$ with $E$ also blown down by it, such that $\sigma$ and the sextic $\Sigma = \sigma _ { * } ( k M _ { 1 } + G + H )$ are equal to one of the following, where for simplicity, we employ the same symbols $M _ { 1 } , G _ { i } , H _ { i }$ to denote their $\sigma$ -images $\hat { M } _ { 1 } , \hat { G } _ { i } , \hat { H } _ { i }$ in $\mathbb { P } ^ { 2 }$ :

(1) $\sigma$ and $\Sigma$ are identical to $\tau$ , $\Gamma$ in one of Cases (1)-(9) in Theorem 3.2; so $\Sigma$ is a union of lines and conics.  
(2) $X , E$ fit Case (13) of Theorem 3.2 with $1 \le k \le 6$ ; $\sigma$ is the blow-down $X  \mathbf { F } _ { 1 }$ of $E$ and all curves in fibres of the $\mathbf { F } _ { 1 }$ , followed by the blow-down $\mathbb { P } ^ { 1 }$ -fibration given by $\mathbf { F } _ { 1 } \to \mathbb { P } ^ { 2 }$ of $G _ { 1 }$ $\lvert M _ { 1 } \rvert$ ; $\begin{array} { r } { \Sigma = k \hat { M } _ { 1 } + \sum _ { j = 1 } ^ { 6 - k } \hat { H } _ { j } } \end{array}$ so that $G _ { 1 }$ becomes the , where $( - 1 )$ $\hat { M } _ { 1 }$ -curve on , ${ \hat { H } } _ { j }$ are concurrent lines, with $\hat { M } _ { 1 } \neq \hat { H } _ { j }$ , but $\hat { H } _ { i } = \hat { H } _ { j }$ possible; the $H _ { j }$ here may be different from tho $\pmb { T } \pmb { T }$ in Th 22

(3) $X , E$ fit Case (14) of Theorem 3.2 with $m = 3$ ; $\sigma$ is the composition of $\tau : X  \mathbf { F } _ { 1 }$ and the blow-down $\mathbf { F } _ { 1 } \to \mathbb { P } ^ { 2 }$ of ${ \bar { G } } _ { 1 } = \tau ( G _ { 1 } )$ ; $\begin{array} { r } { \Sigma = \hat { M } + \sum _ { j = 2 } ^ { J } g _ { j } \hat { G } _ { j } } \end{array}$ with $\textstyle \sum _ { j = 2 } ^ { J } g _ { j } = 4$ , where $\hat { G } _ { j }$ are lines concurrent at $p$ and $\hat { M }$ is a conic through $p$ and transversal to all $\hat { G } _ { j }$ .

(4) blow-down fit Case (15) of Theorem 3.2 with of ; $m = 5$ ; $\sigma$ is the composition of with , where $\tau : X  \mathbf { F } _ { 1 }$ a cubic with and the $\mathbf { F } _ { 1 } \to \mathbb { P } ^ { 2 }$ $\bar { G } _ { 1 }$ $\begin{array} { r } { \Sigma = \hat { M } + \sum _ { j = 2 } ^ { J } g _ { j } \hat { G } _ { j } } \end{array}$ $\textstyle \sum _ { j = 2 } ^ { J } g _ { j } = 3$ $\hat { M }$ a node at $p$ , where $\hat { G } _ { j }$ are lines through $p$ and transversal to both tangents of $\hat { M }$ at $p$ .

(5) The well-defined morphism $\sigma$ is the composition of $\tau : X  \mathbb { P } ^ { 2 }$ in Case (10), or (11), or (15) with $m = 4$ of Theorem 3.2, the blow-up of an intersection point $\bar { G } _ { i } \cap \bar { G } _ { j }$ of fibres of two different rulings with exceptional divisor $\boldsymbol { D }$ and the blow-down of the proper inverses of these two fibres (Remark 3.3); $\Sigma = \hat { \Gamma } + ( g _ { i } + g _ { j } - 2 ) \hat { D }$ , where $\hat { \Gamma }$ is the strict transform of $\Gamma$ and $\hat { D }$ the image of $\boldsymbol { D }$ ; so $\Sigma$ is a union of lines, conics and at most one nodal cubic (only in Case (15), and then the $\Sigma$ here is the same as the one in (4) above).

(6) $X , E$ fit Case (12) of Theorem 3.2; there is a section $C$ of the $\mathbb { P } ^ { 1 }$ -fibration on $X$ induced from the one on $\mathbf { F } _ { 2 }$ , with $\pi ( C ) ^ { 2 } = - 1$ , $C \cap ( G + H ) = \emptyset$ and $C \cdot M = 2$ ; $\sigma$ is the blow-down $X  \mathbf { F } _ { 1 }$ of $E$ and all curves in fibres disjoint from $C$ followed by the blow-down $\mathbf { F } _ { 1 } \to \mathbb { P } ^ { 2 }$ of $C$ ; $\Sigma = \hat { M } + ( 3 - h ) \hat { G } _ { 1 } + h \hat { H } _ { 1 }$ , where $0 \leq h \leq 3$ , $\hat { M }$ is a cubic with a node at $p$ and $\hat { G } _ { 1 }$ , $\hat { H } _ { 1 }$ are distinct lines not through $p$ .

(7) $X , E$ fit Case (13) of Theorem 3.2 with $k = 1 , 2$ ; there is a section $C$ of the $\mathbb { P } ^ { 1 }$ -fibration on $X$ given by $\lvert M _ { 1 } \rvert$ , with $\pi ( C ) ^ { 2 } = - 1$ , $C \cap G = \emptyset$ and $C \cdot H = ( 2 - k )$ ; $\sigma$ is the blow-down $X  \mathbf { F } _ { 1 }$ of $E$ and all curves in fibres disjoint from $C$ followed by the blow-down $\mathbf { F } _ { 1 } \to \mathbb { P } ^ { 2 }$ of $C$ ; $\Sigma = k \hat { M } _ { 1 } + 4 \hat { G } _ { 1 } + ( 2 - k ) \hat { H } _ { 1 }$ , where $\hat { M } _ { 1 }$ , $\hat { G } _ { 1 }$ , $\hat { H } _ { 1 }$ are non-concurrent lines; the $H _ { 1 }$ here may be different from any $H _ { i }$ in Theorem 3.2.

If the claim is false for some $C$ on $Y$ , then $C \cdot M \geq 1$ for $\bar { M } _ { \mathbb { Q } } ^ { \perp } = \mathbb { Q } \bar { H } _ { 1 }$ ; using $C$ to intersect the olit., $\bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \ a \ a \ a \ a \ a \ a \ a \ a \ a \ a \ a \ a \ a \ a \ a \ a \ a \ a \ m \ a \ a \ a \ a \ a \ m \ m \ a \ m \ m \ m \ m \ a \ m \ a \ m \ a \ m \ m \ m \ m \ a \ m \ m \ a \ a \ m \ m \ m \ m \ m \ a \ m \ m \ a \ m \ m \ m \ a \ a \ m \ m \ m \ m \ a \ m \ m \ m \ m \ m \ m \ m \ m \ m \ a \ m \ m \ a \ a \ a \ m \ m \ m \ m \ m \ m \ a \ m \ m \ a \ m \ m \ m \ m \ a \ m \ m \ m \ a \ m \ m \ a \ m \ m \ m \ m \ m \ m \ m \ a \ m \ m$ goe thot $\curvearrowleft$ ic-o $\begin{array} { r l } { \boldsymbol { \mathcal { I } } } & { { } \textbf { \textsf { 1 } } ) } \end{array}$ wmith $\textrm { \textit { ( C ) } } \textrm { \textit { n r c } } \boldsymbol { \Omega } \cdot \boldsymbol { \mathcal { \tau } } \cdot \textrm { \textit { r } } \cdot \textrm { \textit { ( 1 ) } }$ (2.0)

5.5 Corollary.
With the assumptions in Theorem 5.1, we have:

(1) The plane sextic $\Sigma$ is a union of lines, conics and at most one nodal cubic; moreover, if a cubic does appear in $\Sigma$ then it is the image of the mobile part $M$ of $\big | - 2 K _ { X } + 2 E \big |$ .  
(2) $M ^ { 2 } \leq 5$ holds; if $M ^ { 2 } = 5$ then (4) above, or equivalently Theorem 3.2 (15) with $m = 5$ , occurs (actually realizable at least for $( g _ { 2 } , . . . , g _ { J } ) = ( 1 , 1 , 1 )$ ); see 4.6 for an alternative direct proof.

We need the following result first.

Lemma 5.6. Let $X$ be a Coble surface of rational type with respect to a $( - 1 )$ -curve $E$ and with $\pi : X \to Y$ the blow-down of $E$ .
Then we have:

(1) Suppose that $X$ fits Case (14) (resp.
Case (15)) of Theorem 3.2. Then $Y = \pi ( X )$ is basic if and only if $m = 3$ (resp.
$m = 4 , 5$ ).
(2) If $X$ fits Case (16), or Case (14) with $k > 6$ $= \mathrm { d e g } ( - 2 K _ { \mathbb { P } ^ { 2 } } ) )$ , then $Y$ is not basic.

Proof.
Consider Theorem 3.2 (16).
The others are similar (see Remark 3.3 and the proof of Lemma 4.2 for the “if” part of (1)).
In the following, we shall use $M , G , H , H _ { 1 }$ to denote their $\pi$ -images on $Y$ (cf.
Lemma 2.3).

5.6.1 Claim.
All negative curves $\ l \neq H _ { 1 }$ ) on $Y$ are contained in fibres of the $\mathbb { P } ^ { 1 }$ -fibration on $Y$ induced from the one on $Y _ { \mathrm { m i n } }$ .

Expressing $\bar { C } = \tau ( C ) \sim a \bar { H } _ { 1 } + b f$ with a general fibre $f$ on $Y _ { \operatorname* { m i n } } = \mathbf { F } _ { m }$ , we have $b \geq a m$ due to the irreducibility of $\bar { C }$ , and get $2 \geq C \cdot M = C \cdot M = b \geq a m \geq m$ , a contradiction to the fact that $m \geq 3$ in Theorem 3.2 (16).

Let $Y  Y _ { 1 }$ be the blow-down of all $( - 1 )$ -curves in fibres disjoint from $H _ { 1 } , M$ .
Then for each singular fibre $F _ { i }$ (of length $n _ { i }$ ) on $Y _ { 1 }$ , the dual graph of $H _ { 1 } + F _ { i } + M$ on $Y _ { 1 }$ is as in Lemma 1.8 with $s _ { 1 } = H _ { 1 } , s _ { 2 } = M$ .
By the claim above, the basicness of $Y$ would imply the existence of a blow-down $Y _ { 1 }  \mathbf { F } _ { 1 }$ of $( - 1 )$ -curves in fibres such that $H _ { 1 }$ becomes the unique $( - 1 )$ -curve on $\mathbf { F } _ { 1 }$ ; hence if $- b _ { 1 }$ is the self-intersection of $H _ { 1 }$ on $Y _ { 1 }$ , then $\begin{array} { r } { \sum _ { i } n _ { i } \geq b _ { 1 } - 1 } \end{array}$ .
On the other hand, the intersection of (the images of) $M$ and $H _ { 1 }$ on $X , Y , Y _ { 1 } , Y _ { \mathrm { { m i n } } }$ are the same by the construction of $Y _ { 1 }$ and by noting that $M$ is the $\tau$ -pull back of $\bar { M }$ on $Y _ { \mathrm { m i n } }$ (Remark 3.3). So $b _ { 1 } = b _ { 1 } + 2 ( M \cdot H _ { 1 } ) = M ^ { 2 } + \textstyle \sum _ { i } n _ { i } \geq m + b _ { 1 } - 1$ and $m \leq 1$ (cf.
the proof of Lemma 1.8 and blow down $Y _ { 1 }$ to $\mathbf { F } _ { b _ { 1 } }$ to see the second equality).
This contradicts the fact that $m \geq 3$ in Theorem 3.2 (16).
So $Y$ is not basic.

5.7 Now we prove Theorem 5.4. In view of Lemma 5.6, we only need to consider Cases (12) and (13) of Theorem 3.2. The former one will imply Theorem 5.4 (6) by the argument in Lemma 5.6; indeed, all components of $\pi ( G + H )$ are disjoint from $C$ and all, except $\pi ( G _ { 1 } ) , \pi ( H _ { 1 } )$ , contracted to points by the map $Y \  \ \mathbf { F } _ { 1 }$ , while $\pi ( G _ { 1 } ) , \pi ( H _ { 1 } )$ (resp.
$\pi ( M ) )$ are mapped to section(s) of self-intersection 1 (resp.
5) on $\mathbf { F } _ { 1 }$ (cf.
the proof of Lemma 1.8).

Consider Theorem 3.2 (13).
If all negative curves $( \neq \pi ( G _ { 1 } ) )$ on $Y$ are contained in fibres, then the basicness of $Y$ implies that Theorem 5.4 (2) occurs.
Otherwise, the proof of Lemma 5.6 shows the existence of a section $C$ $\left( \neq \pi ( G _ { 1 } ) \right)$ on $Y$ such that $C ^ { 2 } = - 1$ and $( k ; \pi ^ { - 1 } ( C ) \cdot M _ { 1 } , \pi ^ { - 1 } ( C ) \cdot G + H ) =$ $( 2 ; 1 , 0 ) , ( 1 ; 1 , 1 ) , ( 1 ; 2 , 0 )$ .
In particular, $\pi ^ { - 1 } ( C ) \cdot G _ { 1 } = 0$ for $G = 4 G _ { 1 }$ now.
The first two clearly imply Theorem 5.4 (7).

Now assume that $( k ; \pi ^ { - 1 } ( C ) \cdot M _ { 1 } , \pi ^ { - 1 } ( C ) \cdot G + H ) = ( 1 ; 2 , 0 )$ .
We shall show that this will imply Theorem 5.4 (2).
Let $Y  Y _ { 1 }$ be the blow-down of all $( - 1 )$ -curves in fibres disjoint from the double section $C$ .
Then for each singular fibre $F _ { i } ^ { \prime }$ on $Y _ { 1 }$ , either $C + F _ { i }$ is a simple loop so that $F _ { i } ^ { \prime }$ has the same dual graph as its namesake in Lemma 1.8, or $F _ { i } = 2 ( E _ { i } + H _ { i } ^ { ( 1 ) } + \cdots + H _ { i } ^ { ( n _ { i } - 2 ) } ) + H _ { i } ^ { ( n _ { i } - 1 ) } + H _ { i } ^ { ( n _ { i } ) }$ where $\sum H _ { i } ^ { ( j ) }$ has type $D _ { n _ { i } }$ Dynkin diagram ( $n _ { i } = 2 , 3$ are possible), where $E _ { i }$ is a $( - 1 )$ -curve meeting $C$ and $H _ { 1 }$ (and also $H _ { 2 }$ when $n _ { i } = 2$ ).
Now utilizing the equality $- 2 K _ { Y } = \pi ( k M _ { 1 } + G + H )$ and intersecting it with (inverses of) curves in the fibre $F _ { i }$ , we see that the loop case of $C + F _ { i }$ is impossible and we have

$$
- 2 K _ { Y _ { 1 } } = M _ { 1 } + 4 G _ { 1 } + \sum _ { i } [ \sum _ { j = 1 } ^ { n _ { i } - 2 } 2 j H _ { i } ^ { ( j ) } + ( n _ { i } - 2 ) H _ { i } ^ { ( n _ { i } - 1 ) } + n _ { i } H _ { i } ^ { ( n _ { i } ) } ] ,
$$

where we assume that the section $G _ { 1 }$ on $Y _ { 1 }$ meets the fibre $F _ { i }$ at $H _ { i } ^ { ( n _ { i } ) }$ .
Intersecting $G _ { 1 }$ with (5.1), one gets $2 G _ { 1 } ^ { 2 } = 3 \mathrm { - } \textstyle \sum _ { i } n _ { i }$ .
On the other hand, the disjointness of the section $G _ { 1 }$ with the $( - 1 )$ -double section $C$ on $Y _ { 1 }$ implies that $\begin{array} { r } { - 4 G _ { 1 } ^ { 2 } = C ^ { 2 } + \sum _ { i } n _ { i } } \end{array}$ (cf.
the proof of Lemma 1.8). $\dot { \iota }$ From these two equalities, one deduces that $G _ { 1 } ^ { 2 } = - 1$ on $Y _ { 1 }$ .
Hence Case (2) occurs.
This proves Theorem 5.4.

# 6. Rational curves with negative self-intersection

In this section we shall study $\left( - n \right)$ -curves on a Coble surface.
The goal is to see whether this set is finite, or finite modulo automorphisms of the surface.
We start with a definition:

6.1 Let $X$ be a Coble surface.
We say that $X$ is of $K 3$ -type if $\mid - 2 K _ { X } \mid$ contains a reduced divisor.
The reason for this definition is explained by the folowing:

6.2 Lemma.
Let $X$ be a Coble surface.
Then the following properties are equivalent:

(1) $\vert - 2 K _ { X } \vert$ contains a reduced divisor.  
(2) There exists a double cover ${ \tilde { X } }  X$ , where $\tilde { X }$ is a $K 3$ -surface with at most ordinary double points as singularities.

Proof.
$( 1 ) \Rightarrow ( 2 )$ Let $B \sim - 2 K _ { X }$ be a a reduced effective anti-bicanonical divisor.
Then $B$ is of simple normal crossing (Lemma 1.4). Let $\tilde { X }$ be the double cover of $X$ corresponding to the square root of $B$ defined by the line bundle $\mathcal { O } _ { X } ( - K _ { X } )$ .
By the formula for the canonical sheaf of a double cover we get $\omega _ { \tilde { X } } = \mathcal { O } _ { \tilde { X } }$ .
Since $B$ has at worst ordinary double points, $\tilde { X }$ is a K3 surface with at worst ordinary double points.

(2)⇒ (1) This follows from the formula for the canonical class of a double cover.

6.3 Theorem.
A Coble surface of rational type with respect to some $( - 1 )$ -curve $E$ will never be of K3-type.

Proof.
Suppose the contrary that $X$ is a Coble surface of rational type with respect to a $( - 1 )$ -curve $E$ , which is also of K3-type.
So if $\pi : X \to Y$ is the blow-down of $E$ , then we have $| - 2 K _ { X } + 2 E | =$ $\vert M \vert { + } G { + } H = \pi ^ { * } ( \vert { - } 2 K _ { Y } \vert )$ with $p _ { a } ( M ) = 0$ and $p _ { a } ( - 2 K _ { X } + 2 E ) = 1$ .
By the condition and Lemma 2.3 to the extent that $E \cap ( G + H ) = \emptyset$ , we see that $G + H$ is reduced; in particular, the $\tau$ -image $\Gamma = \overline { { M } } + \overline { { G } } + \overline { { H } }$ on $Y _ { \mathrm { m i n } }$ is also reduced.
By Remark 3.3 and calculating the image of $M + G + H$ on $Y _ { 0 }$ , we see that only Cases (5), (6), (10), (11) are possible.

Assume Case (5) or (6) occurs and $\textstyle \Gamma = M _ { 1 } + \sum _ { i } G _ { i }$ is of simple normal crossing; the general case and Cases (10) and (11) are similar.
Noting that $K _ { Y } ^ { 2 } \le 0$ and applying Lemma 1.9 repeatedly, we see that $Y  \mathbb { P } ^ { 2 }$ is the blow-up of the 9 intersection points in $\textstyle \sum _ { i } { \bar { G } } _ { i }$ ; we can not touch points on $\bar { M _ { 1 } }$ (see Remark 3.3). Thus $Y$ and $X$ are equal to their namesakes in Example 2.12. Hence $X$ is of elliptic type with respect to $E$ , a contradiction.
For general situation of Case (6) say, we need to apply Lemma 2.2 (4) (the uniqueness of a loop, if exists, and the inequality there); in particular, all triple points as well as all double points (with possibly one exception) of $\sum G _ { i }$ must be blown up; also note that there is no quadruple point of $\sum { \bar { G } } _ { i }$ due to the reducedness of $G + H$ .
This proves Theorem 6.3.

There is a strong relation between Coble surfaces of K3-type and minimal resolutions of rational log Enriques surfaces of index 2. A rational log Enriques surface $\bar { X }$ of index 2 is a normal rational surface with at worst quotient singularities such that $\mathcal { O } ( - 2 K _ { \bar { X } } ) \cong \mathcal { O } _ { \bar { X } }$ (cf.
[Zh1]).

# 6.4 Proposition.

(1) The minimal resolution $X$ of a rational log Enriques surface $\bar { X }$ of index 2 is a Coble surface such that $h ^ { 0 } ( - 2 K _ { X } ) = 1$ and the only member $D$ in $\mid - 2 K _ { X } \mid$ is a reduced divisor whose connected component is either a single $( - 4 )$ -curve or a linear chain with the following dual graph:

$$
( - 3 ) - ( - 2 ) - \cdot \cdot \cdot - ( - 2 ) - ( - 3 ) .
$$

The converse is also true.

(2) A terminal Coble surface has exactly one anti-bicanonical divisor $\boldsymbol { D }$ , and $\boldsymbol { D }$ is reduced and a disjoint union of $( - 4 )$ -curves.
The converse is also true.

(3) The minimal resolution $X$ of a rational normal surface $\bar { X }$ with at worst type $\textstyle { \frac { 1 } { 4 } } ( 1 , 1 )$ singularities is a terminal Coble surface.
The converse is also true.

(4) Let $X$ be a Coble surface with a reduced divisor $D \in \vert - 2 K _ { X } \vert$ .
Then there is an embedded resolution $( X ^ { \prime } , D ^ { \prime } )$ of $( X , D )$ with $D ^ { \prime }$ the proper inverse transform of $D$ , such that $X ^ { \prime }$ is a binel Cehle qunfeee writh $\curvearrowright$ og tho onlrr monabon in $\mathbf { \Sigma } \_ { | } \subset [ 0 , \pi ] $

Proof.
The first part of (1) is proved in [Zh1].
For the converse, if $X  { \bar { X } }$ is the contraction of $\boldsymbol { D }$ then one sees easily that $X$ is a rational log Enriques surface of index 2.

We prove (2).
If $X$ is terminal Coble, then an arbitrary member $\boldsymbol { D }$ of $ { - 2 K } _ { X } \vert$ is reduced and smooth (Lemma 1.9) and hence a disjoint union of $\left( - n _ { i } \right)$ -curves $D _ { i }$ (Lemma 1.4). Now $D _ { i } ^ { 2 } =$ $D \cdot D _ { i } = D _ { i } \cdot \left( - 2 K _ { X } \right)$ implies that $D _ { i }$ is a $( - 4 )$ -curve; in particular, $h ^ { 0 } ( - 2 K _ { X } ) = h ^ { 0 } ( D ) = 1$ .
This proves (2) (cf.
Lemma 1.9).

For the first part of (3), by the proof of (1), $\vert - 2 K _ { X } \vert$ has exactly one member $D$ which is reduced and a disjoint union of $( - 4 )$ -curves.
So $X$ is a terminal Coble surface (cf.
Lemma 1.9). For the converse of (3), we let $X  { \bar { X } }$ be the contraction of the unique divisor $\boldsymbol { D }$ in $\mid - 2 K _ { X } \mid$ .
Then $X$ satisfies the required condition.

Next we prove (4).
By Lemma 1.4, $\boldsymbol { D }$ has only nodes as singularities.
Let $X ^ { \prime }  X$ be the blow-up of all nodes in $D$ .
Then we have $- 2 K _ { X ^ { \prime } } \sim D ^ { \prime }$ .
This implies, as in (2), that $D ^ { \prime }$ is a disjoint union of $( - 4 )$ -curves.
Hence $X ^ { \prime }$ is terminal Coble.
This completes the proof of Proposition 6.4.

Let $f : X ^ { \prime } \to X$ be a birational morphism of Coble surfaces.
If $X ^ { \prime }$ is of $K 3$ -type then so is $X$ ; indeed, if $D ^ { \prime } \in \vert - 2 K _ { X ^ { \prime } } \vert$ is reduced then so is $f _ { * } ( D ^ { \prime } ) \in \vert - 2 K _ { X } \vert$ .
In view of the above observation and Lemma 1.10, among Coble surfaces of K3-type, minimal ones are the most interesting.
Such $X$ is of elliptic type with respect to any $( - 1 )$ -curve $E$ (Theorem 6.3). Suppose that $M ^ { 2 } = 0$ in notation of Lemma 2.2. Then $X$ is given in either Theorem 2.5 or Theorem 2.8 with $X = X ^ { \prime }$ and $E = E ^ { \prime }$ .

6.5 Theorem.
Suppose $X$ is a Coble surface with $M ^ { 2 } = 0$ .
If $X$ is of Halphen type obtained from a minimal Halphen surface $Y _ { m }$ of index 2 by one blow-up of a singular point on its non-multiple fibre $F ^ { \prime }$ , then it is of K3-type if and only if $F$ is of type $I _ { n }$ , $I I$ , III or IV.
If $X$ is of Jacobian type obtained as in Theorem 2.8 from a minimal Jacobian rational elliptic surface $Y _ { \mathrm { m i n } }$ by blowing up a singular point from one fibre $F ^ { \prime }$ and singular points (at least one) and their infinitely near points on another fibre $F _ { 1 }$ , then it is of K3-type if and only if each of $F ^ { \prime }$ and $F _ { 1 }$ is of type $I _ { n }$ , II, III, or IV.

Proof.
This follows immediately from the Kodaira classification of singular fibres.

There is an analogue of the K3-cover for Coble surfaces of elliptic type which are not of K3-type:

6.6 Theorem.
Suppose $X$ is a Coble surface of elliptic type with $M ^ { 2 } = 0$ in notation of 2.1, which is not of K3-type.
Then $X$ admits a double cover $\tilde { X }$ which is a non-minimal rational Jacobian elliptic surface.

Proof.
We do only the case when $X$ is of Halphen type; the Jacobian case can be considered similarly.
Then $X$ is obtained from a minimal Halphen elliptic surface $V$ of index 2 by blowing up a singular point of its non-multiple fibre $F$ of type $\neq I _ { n } , I I , I I I , I V$ .

We check the assertion by considering different types of the fibre.
Let us do for example, the case $F ^ { \prime }$ is of type $I _ { b } ^ { * }$ and leave the other cases to the reader.
Write $F = R _ { 1 } + R _ { 2 } + R _ { 3 } + R _ { 4 } + 2 ( R _ { 5 } + . ~ . ~ . R _ { b + 5 } )$ , where $R _ { 1 } , R _ { 2 }$ intersect $R _ { 5 }$ and $R _ { 3 } , R _ { 4 }$ intersect $R _ { b + 5 }$ .
Then

$$
R _ { 1 } + R _ { 2 } + R _ { 3 } + R _ { 4 } \sim - 2 K _ { X } - 2 ( R _ { 5 } + \ldots R _ { b + 5 } ) ,
$$

hence there exists a double cover $\pi : \tilde { V } \to V$ ramified over $R _ { 1 } + R _ { 2 } + R _ { 3 } + R _ { 4 }$ .
We have

$$
K _ { \tilde { V } } \sim - \pi ^ { - 1 } ( R _ { 5 } + \ldots R _ { b + 5 } ) .
$$

If $b = 0$ , $C = \pi ^ { - 1 } ( R _ { 5 } )$ is an elliptic curve with $C ^ { 2 } = - 4$ .
If $b \neq 0$ , $C = \pi ^ { - 1 } ( R _ { 5 } + \dots R _ { b + 5 } )$ is a reducible curve of arithmetic genus 1. The pre-image of a general fibre of the elliptic fibration on $\tilde { \textbf { r } } \tau$ grlita inte e digioint union of true ollintie A ften o boge chenge $\mathbb { m } 1 \quad \quad \dots \quad \mathbb { m } 1$ of deonee 2 ramified at two points, we obtain an elliptic fibration on $\tilde { V }$ with one of its fibre equal to $( \pi ^ { * } ( F ) ) _ { \mathrm { r e d } } =$ $C + ( \tilde { R } _ { 1 } + \tilde { R } _ { 2 } + \tilde { R } _ { 3 } + \tilde { R } _ { 4 } )$ , where $\pi ^ { * } ( R _ { i } ) = 2 \tilde { R } _ { i } , 1 \leq i \leq 4$ .
Note that the ${ \tilde { R } } _ { i }$ are $( - 1 )$ -curves on $\tilde { V }$ .
Blowing these four curves down, we obtain an elliptic surface $\hat { V }$ with the image $\hat { C }$ of $C$ , which is reduced and linearly equivalent to $- K _ { \hat { V } }$ .
One can verify that $\hat { V }$ is a Jacobian Halphen surface.

Now, if $X$ is obtained from $V$ by blowing up a point $p$ on $R _ { 5 } + \ldots + R _ { b + 5 }$ , it admits a double cover $\tilde { X }$ which is obtained from $\tilde { V }$ by blowing up two (or one if $p$ also lies on some $R _ { i }$ with $i \leq 4$ ) points on $C$ .
So $\tilde { X }$ is obtained from the minimal elliptic surface $\hat { V }$ by blowing up points on one fibre $\hat { C }$ .

Now we consider the finiteness problem of the number of negative curves on a Coble surface modulo automorphisms.

6.7 Theorem.
Assume $k = \mathbb { C }$ .
Let $X$ be a Coble surface of elliptic type.
Suppose that $X$ is a terminal Coble surface of K3-type.
Also assume that $X$ is general in the sense that any divisor class on the K3-cover is invariant with respect to the double cover involution.
Then the group $\operatorname { A u t } ( X )$ has finitely many orbits in the set of negative rational curves on $X$ .

Proof.
This follows from two well-known results about K3-surfaces.
The first one says that the group of automorphisms of any K3-surface has only finitely many orbits in the set of smooth rational curves (see [Na, St]).
The second one says that any automorphisms of the K3-cover of $X$ commutes with the involution (see [Ni]).

We do not know whether the same result is true for non-terminal Coble surfaces of K3-type.
However we shall show now that it cannot be extended to Coble surfaces not of K3-type.

Proof.
We have $( E ^ { \prime } - E ) ^ { 2 } = - 2 - 2 E ^ { \prime } \cdot E$ , so it suffices to show that the set $S ^ { \prime }$ of possible integers oftho fe $\smash { \mathrm { ~ \ p ~ } _ { \perp } } / \smash { \pi / \smash { \qquad \textit { \textbf { } } \rvert } ^ { 2 } }$ iainfnite Sinne $\begin{array}{c} \smash { \left( \begin{array} { l l l l l l l } { \boldsymbol { \Gamma } ^ { \prime } } & { } & { } & { \boldsymbol { \Gamma } ^ { \prime } } & { } & { } & { \cdots } & { } & { } & { \boldsymbol { \Omega } ^ { \prime } } \end{array} \right) ^ { } } \end{array}$ the dirigon elegg of $_ { \square } / \quad \square$ hel

6.8 Lemma.
Let $\pi _ { A } : S ( A ) \to S$ be the blow-up of a set $A$ of $_ n$ points on a nonsingular projective surface $S$ with zero irregularity.
Let $G ( A )$ be the subgroup of $\operatorname { A u t } ( S ( A ) )$ consisting of automorphims which are identical on the proper inverse transform $C ^ { \prime }$ of a nonsingular irreducible curve $C$ of positive genus on $S$ which contains $A$ .
Then the set of subsets $A$ of $C$ such that $G ( A )$ is not the lift of a subgroup $G ( A ) ^ { \prime }$ of $\operatorname { A u t } ( S )$ is countable.

Proof.
We use induction on $_ n$ .
Assume $n = 1$ .
Let $E _ { A }$ be the exceptional curve of $\pi _ { A }$ .
An element $g \in G ( A )$ is a lift of an automorphism of $S$ if and only if $g$ stabilizes $E _ { A }$ .
Suppose $g ( E _ { A } ) \neq E _ { A }$ .
The image $R _ { A }$ in $V$ of $g ( E _ { A } )$ intersects $C$ at one point $a$ with multiplicity $m + 1$ , where $m = E _ { A } \cdot g ( E _ { A } )$ .
The restriction of the linear system $| R _ { A } |$ to $C$ is of degree $m + 1$ , so that there are only finitely many points $c$ on $C$ which can be realized as a divisor $( m + 1 ) c$ from this linear system.
Here we use that the Jacobian of a curve of positive genus has only finitely many points of given finite order.
Since the set of divisor classes on a surface with zero irregularity is countable, only a countable set of points $a \in C$ may have the property $g ( E _ { A } ) \neq E _ { A }$ .
This proves the assertion for $n = 1$ .

If $n > 1$ , we write $A = A ^ { \prime } \cup \{ a \}$ , where $a \not \in A ^ { \prime }$ .
The map $\pi _ { A }$ is equal to the composition of the maps $\pi _ { a } : S ( A ) \to S ( A ^ { \prime } )$ and $\pi _ { A ^ { \prime } } : S ( A ^ { \prime } ) \to S$ .
It is clear that $C ^ { \prime }$ is equal to the proper inverse transform of a curve $C ^ { \prime \prime }$ on $S ( A ^ { \prime } )$ which is also the proper inverse transform of $C$ .
By the case $n = 1$ , we know that the set of points $a$ for which elements of $G ( A )$ do not descend to automorphims of $S ( A ^ { \prime } )$ is countable.
By induction, the set of subsets $A ^ { \prime }$ for which elements of $G ( A )$ do not descend further to $S$ is countable.
So, the set of all possible $A$ for which elements of $G ( A )$ do not descend to $S$ is countable.

6.9 Lemma.
Let $\Sigma$ be a set of $g$ points in $\mathbb { P } ^ { 2 }$ and let $X$ be the blow-up of $\Sigma$ .
Denote by $\varepsilon$ the set of all $( - 1 )$ -curves on $X$ .
Assume that $\varepsilon$ is infinite.
Then, for any $E \in { \mathcal { E } }$ , the image $S$ of the map $\mathcal { E }  \mathbb { Z }$ given by $E ^ { \prime } \to E ^ { \prime } \cdot E$ , is an infinite set.

to the orthogonal complement $( \mathbb { Z } K _ { X } ) _ { \operatorname { P i c } ( X ) } ^ { \perp }$ .
Since $K _ { X } ^ { 2 } = 0$ , the lattice $L = ( \mathbb { Z } K _ { X } ) _ { \operatorname { P i c } ( X ) } ^ { \perp } / \mathbb { Z } K _ { X }$ is negative definite.
This implies that the set of vectors in $L$ of fixed norm is a finite set.
In particular, if $S ^ { \prime }$ is finite, the set of cosets in $L$ of the classes $E ^ { \prime } - E$ is finite.
On the other hand, $( E ^ { \prime } - E ) - ( E ^ { \prime \prime } - E ) = E ^ { \prime } - E ^ { \prime \prime } \in \mathbb { Z } K _ { X }$ would imply that $0 = ( E ^ { \prime } - E ^ { \prime \prime } ) ^ { 2 } = - 2 - 2 E ^ { \prime } \cdot E ^ { \prime \prime }$ and hence $E ^ { \prime } = E ^ { \prime \prime }$ .
So $E ^ { \prime } - E$ and $E ^ { \prime \prime } - E$ cannot belong to the same coset modulo $\mathbb { Z } K _ { X }$ unless $E ^ { \prime } = E ^ { \prime \prime }$ .
This shows that the set of divisor classes of $E ^ { \prime } - E$ must be finite, contradicting the assumption that $\mathcal { E }$ is infinite.
This contradiction proves the lemma.

6.10 Example.
Here we give an example of a minimal Coble surface of Halphen type such that its automorphism group has infinitely many orbits on the set of $( - 1 )$ -curves.
We have to assume that the ground field $k$ is uncountable.

Let $V$ be an Halphen surface of index 2 with a reducible fibre of type $I _ { 0 } ^ { * }$ .
One can explicitly construct it as follows.
Take five lines $\boldsymbol { L } _ { i }$ ( $1 \leq i \leq 5$ ) in $\mathbb { P } ^ { 2 }$ in general linear position and consider a pencil of elliptic curves spanned by the curve $C _ { 6 } = L _ { 1 } + L _ { 2 } + L _ { 3 } + L _ { 4 } + 2 L _ { 5 }$ and the curve $2 C _ { 3 }$ , where $C _ { 3 }$ is the cubic which passes through 6 intersection points $p _ { i j } = L _ { i } \cap L _ { j } ; i , j = 1 , . . . , 4$ .
We assume that the cubic $C _ { 3 }$ intersects $L _ { 5 }$ at three distinct points $q _ { 1 } , q _ { 2 } , q _ { 3 }$ .
Resolving the base points of the pencil we arrive at a Halphen surface $V$ of index 2. The image to $\mathbb { P } ^ { 2 }$ of its fibre of type $I _ { 0 } ^ { * }$ is the sextic $C _ { 6 }$ .
If we choose a point $a \in L _ { 5 }$ and blow up the corresponding point on $V$ we obtain a minimal Coble surface $X$ of Halphen type.

Let $V ^ { \prime }$ be the Halphen surface obtained in the same way as $V$ but replacing the cubic curve by a new cubic which passes through the points $p _ { i j }$ and the points $q _ { 1 } , q _ { 2 } , a$ .
We have a natural map $f : X \to V ^ { \prime }$ which is the blow-up of the pre-image $q _ { 3 } ^ { \prime }$ of $q _ { 3 }$ on $V ^ { \prime }$ .
When $a$ is chosen general enough, the elliptic fibration $\pi : V ^ { \prime } \to \mathbb { P } ^ { 1 }$ has only one reducible fibre (of type $I _ { 0 } ^ { * }$ ).
Its Jacobian fibration (a relative minimal model of the Jacobian of the generic fibre of $\pi$ ) has only one reducible fibre of type $I _ { 0 } ^ { * }$ and hence its Mordell-Weil group MW is infinite (of rank 4).
Since MW acts freely by translations on the set of bi-sections of $\pi$ , we see that $V ^ { \prime }$ has infinitely many $( - 1 )$ -curves (which are rational bi-sections of $\pi$ ).
Let $E _ { a }$ be the exceptional curve on $V ^ { \prime }$ blown-up from the point $a$ .
Its pre-image, also denoted by $E _ { a }$ , under the map $f : X \to V ^ { \prime }$ , is the exceptional curve of the map $X  V$ .
By Lemma 6.9, $V ^ { \prime }$ has $( - 1 )$ -curves $E _ { i }$ with unbounded set of integers $m _ { i } = E _ { i } \cdot E _ { a }$ .
The pull-backs on $X$ , also denoted by $E _ { i }$ , of the curves $E _ { i }$ on $V ^ { \prime }$ , form an infinite set of $( - 1 )$ -curves (if $E _ { i }$ does not pass through $q _ { 3 } ^ { \prime }$ ) or $\left( - 2 \right)$ -curves (if $E _ { i }$ passes through $q _ { 3 } ^ { \prime }$ ) with unbounded intersection numbers with a general fibre of the elliptic fibration on $X$ (the pull-back of the elliptic fibration on $V$ ).
Since the set of $( - 1 )$ -curves on $V ^ { \prime }$ is countable we can always choose $a$ and $q _ { 3 }$ such that $( - 1 )$ -curves on $V ^ { \prime }$ do not pass through $q _ { 3 } ^ { \prime }$ .
So we can assume that all $E _ { i }$ ’s are $( - 1 )$ -curves.
Thus we have found infinitely many $( - 1 )$ -curves $E _ { i }$ on $X$ with unbounded intersection numbers with a general fibre of the elliptic fibration on $X$ .

Note that an automorphism $g$ of $X$ leaves invariant the isolated linear system $| - 2 K _ { X } | = \{ R _ { 1 } +$ $\cdots + R _ { 4 } + 2 R _ { 5 } \}$ , where $R _ { i }$ denotes the proper inverse transform of $\boldsymbol { L } _ { i }$ i n $X$ .
In particular, $R _ { 5 }$ i s $g$ -stable.
Let $G$ be the kernel of the natural action of $\operatorname { A u t } ( X )$ on the 4-point set $\{ R _ { 1 } , \cdot \cdot \cdot , R _ { 4 } \}$ .
Then $\operatorname { A u t } ( X ) / G$ is isomorphic to a subgroup of the symmetric group $S _ { 4 }$ in 4 letters.
Now each $g \in G$ fixes all 4 points $R _ { i } \cap R _ { 5 }$ of the rational curve $R _ { 5 }$ and hence $g$ acts identically on $R _ { 5 }$ (there is no non-trivial automorphism of $\mathbb { P } ^ { 1 }$ which fixes more than two distinct points).
Take the double cover $S  V$ branched along the union of the curves $R _ { 1 } + \ldots + R _ { 4 }$ (see Theorem 6.6). The pre-image of $R _ { 5 }$ is an elliptic curve $C$ on $S$ .
Let $A = \{ a ^ { \prime } , a ^ { \prime \prime } \}$ be the pre-image of $a \in R _ { 5 }$ on $C$ .
Consider the group $G ( A ) ^ { \prime }$ of automorphims of the blow-up $S ( A )$ of $A$ which are lifts of automorphisms $g \in G$ .
Recall that, since all elements of $G$ leave the square root invariant of the divisor class of the branch divisor, for every $g \in G$ there is an element $\tilde { g } \in \operatorname { A u t } ( S ( A ) )$ which commutes with the involution $\sigma$ of the double cover, and descends to an automorphism of $X$ .
Two lifts of the same $g$ differ by $\sigma$ .
f $\smash { \mathcal { O } _ { \perp } ( \textbf { \em i } ) }$ $\curvearrowleft$ T $\curvearrowleft$ 1 1 index 2 of $G ( A ) ^ { \prime }$ consisting of elements of $G ( A ) ^ { \prime }$ which act identically on $C ^ { \prime }$ .
We shall identify this group with the group $G$ .
By Lemma 6.8, we can choose $a$ such that all elements of $G ( A )$ are lifts of automorphisms of $S$ .
Thus all elements of $G$ are lifts of automorphims of $V$ to $X$ .
In particular, $g$ stabilizes $E _ { a }$ so that the full fibre $R _ { 1 } + \cdot \cdot \cdot + R _ { 4 } + 2 ( R _ { 5 } + E _ { a } )$ on $X$ is $g$ -stable.
Clearly each $g \in G$ preserves the degrees of the multi-sections $E _ { i }$ .
Hence the number of orbits of $G$ (and also of $\operatorname { A u t } ( X )$ , due to the finiteness of the index of $G$ in it) on the set of $( - 1 )$ -curves on $X$ is infinite.

6.11 Next we would like to study the set $\mathcal { E }$ of $\left( - n \right)$ -curves ( $n \geq 1$ ) on a Coble surface $X$ of rational type.
We still do not have a complete picture of $\mathcal { E }$ ; however we guess that this set is always finite.
In fact, by a theorem of Nagata ([Na], Theorem 5) this is always true if $X$ is not basic.
Another special case where it is true is when $\kappa ^ { - 1 } ( X ) = 2$ .
Here $\kappa ^ { - 1 } ( X )$ denotes the anti-Kodaira dimension.
This is the Iitaka-Kodaira dimension of the divisor $- K _ { X }$ .
Obviously $\kappa ^ { - 1 } ( X ) \geq 0$ for Coble surfaces.
It is also clear that $\kappa ^ { - 1 } ( X ) \leq 1$ for Coble surfaces $X$ of elliptic type with $M ^ { 2 } = 0$ in notation of Lemma 2.2.

We shall use the following result from [Sa]:

Lemma.
Let $X$ be a surface with $\kappa ^ { - 1 } ( X ) = 2$ .
Then $X$ has only finitely many curves with negative self-intersection.

6.12 Let $X$ be a Coble surface of rational or elliptic type with respect to a curve $E$ and let $\pi :$ $X \  \ Y$ be the blow down of $E$ .
By the definition, $\pi ^ { * } ( | - 2 K _ { Y } | ) = | M | + P$ , where $M ^ { 2 } \geq 0$ .
We have $\kappa ^ { - 1 } ( Y ) = 2$ if and only if either $M ^ { 2 } > 0$ , or $M ^ { 2 } = 0$ and $p _ { a } ( M ) = 0$ (noting that then $P \cdot M = 4 k > 0$ , see Lemma 2.2); if this is the case, $Y$ contains only finitely many negative rational curves.
Unfortunately, this does not automatically imply the finiteness of $\mathcal { E }$ for $X$ except in a few special cases which we list now.

6.13 Lemma.
Let $f : X ^ { \prime } \to X$ be the blow-up of a point $p \in X$ .
Then $\kappa ^ { - 1 } ( X ^ { \prime } ) \leq \kappa ^ { - 1 } ( X )$ .
The equality takes place if $p$ is a point of multiplicity $\geq n + 1$ of an effective divisor from $\vert - n K _ { X } \vert$ .

Proof.
The first assertion is obvious.
The second assertion follows from the fact that the antiKodaira dimension of a divisor $D$ depends only on $D _ { \mathrm { r e d } }$ .

# 6.14 Proposition.

In notation of Lemma 2.2,

(1) Assume that $M ^ { \prime } \geq 3 E$ for some $M ^ { \prime }$ in $\lvert M \rvert$ and $( p _ { a } ( M ) , M ^ { 2 } ) \neq ( 1 , 0 )$ .
Then $\kappa ^ { - 1 } ( X ) = 2$ .  
(2) If $M = k M _ { 1 }$ with $k \geq 3$ .
Then $\kappa ^ { - 1 } ( X ) = 2$ .  
(3) One has $\kappa ^ { - 1 } ( X ) = 2$ if either $p _ { a } ( M ) = 1$ and $M ^ { 2 } = 6$ , or $p _ { a } ( M ) = 0$ and $M ^ { 2 } \geq 4$ .

Proof.
For (1), we consider only the case where $M ^ { 2 } = 0$ and $p _ { a } ( M ) = 0$ .
Then $P \cdot M _ { 1 } = 4$ (Lemma 2.2). Thus $\kappa ^ { - 1 } ( X ) = \kappa ( X , M _ { 1 } + P ) = 2$ , where the first equality follows from the observation that $- 2 K _ { X } \sim ( M ^ { \prime } - 2 E ) + P$ and the latter has the same support as $M ^ { \prime } + P$ $( \sim k M _ { 1 } + P )$ .
(2) is a consequence of (1).

For (3), we consider only the case $p _ { a } ( M ) = 0$ .
By Lemma 1.7, $h ^ { 0 } ( M ) = M ^ { 2 } + 2$ .
Hence if $M ^ { 2 } \geq 5$ , then there is a member $M ^ { \prime }$ i n $| M |$ with $M ^ { \prime } \geq 3 E$ , or equivalently $\pi ( M ^ { \prime } )$ has multiplicity $\geq 3$ at the point $\pi ( E )$ (cf.
Lemma 2.3). So (3) is true in this case.
Suppose that $m = M ^ { 2 } = 4$ .
Then Case (9), (14), (15) or (16) in Theorem 3.2 occurs.
We treat Case (15) because the others are similar.
Now $M$ is the $\tau$ -pull back of $\bar { M } \sim \bar { G } _ { 1 } + ( m - 2 ) f$ , where $f$ is a fibre and $G _ { 1 }$ a section of self-intersection $- ( m - 4 ) = 0$ (cf.
Remark 3.3). Let $M ^ { \prime }$ be the sum of the $\tau$ -pull backs of $\bar { G } _ { 1 } ^ { \prime } \in | \bar { G } _ { 1 } |$ and $2 f ^ { \prime } \in | 2 f |$ through the point $\tau ( E )$ and (1) applies.
One can actually shows that (3) is still true even when $p _ { a } ( M ) = 0$ and $M ^ { 2 } = 3$ , unless Theorem 3.2 (14) with $m = 3$ occurs.

# References

[BP] Barth, W., Peters, C., Automorphisms of Enriques surfaces, Invent.
Math 73 (1983), 383-411.  
[Co1] Coble, A., Algebraic geometry and theta functions, vol.
10, AMS.
Coll.
Publ, 1929.  
[Co1] Coble, A., The ten nodes of a rational sextic and of the Cayley symmetroid, Amer.
J.
Math.
41 (1919), 1–27.  
[CD] Cossec, F., Dolgachev, I., Enriques surfaces $I$ , Birkh¨auser, 1988.  
[Do1] Dolgachev, I., On rational surfaces with a pencil of elliptic curves, Izv.
AN SSSR, Ser.
Math.
(in Russian)) 30 (1966), 1073-1100.  
[Do2] Dolgachev, I., Infinite Coxeter groups and automorphisms of algebraic surfaces, Contemp.
Math.
58 (1986), 91-106.  
[DP] Dolgachev, I., Persson, U., Negative rational curves on surfaces, in preparation.  
[Ha] Harbourne, B., Blowing-up of $P ^ { 2 }$ and their blowing-down, Duke Math.
Journ.
52 (1985), 129-148.  
[MS] Morrison, D., Saito, M.-H., Cremona transformations and degrees of period maps for K3 surfaces with ordinary double points, Adv.
Stud.
Pure Math.
10 (1985), 477-513.  
[Nag] Nagata, M., On rational surfaces, I, Mem.
Coll.
Sci.
Univ.
Kyoto 32 (1960), 351-370.  
[Na] Namikawa, Y., Periods of Enriques surfaces, Math.
Ann.
270 (1985), 201-222.  
[Ni] Nikulin, V., Quotient-groups of groups of automorphisms of hyperbolic forms by subgroups generated by 2- reflections, Algebro-geometric applications,, in ”Current problems in mathematics”, Moscow, VINITI 18 (1981), 3-114.  
[OZ] Oguiso, K., Zhang, D.
-Q., On the complete classification of extremal log Enriques surfaces, Math.
Zeit.
231 (1999), 23-50.  
[Re] Reid, M., Chapters on algebraic surfaces, in “Complex Algebraic Geometrty”, ed.
J.
Koll´ar, IAS/Park City Mathematics Series 3 (1997), 5-159.  
[Sa] Sakai, F., Anticanonical models of rational surfaces, Math.
Ann.
269 (1984), 389-410.  
[St] Sterk, H., Finiteness results for algebraic $K 3$ -surfaces, Math.
Zeit.
189 (1985), 507-513.  
[Zh1] Zhang, D.
-Q., Logarithmic Enriques surfaces, J.
Math.
Kyoto Univ.
31 (1991), 419–466.  
[Zh2] Zhang, D.
-Q., Logarithmic Enriques surfaces II, J.
Math.
Kyoto Univ.
33 (1993), 357–397.  
[Zh3] Zhang, D.
-Q., Quotients of K3 surfaces modulo involutions, Japan.
J.
Math.
(N.S.) 24 (1998), 335–366.  
Igor V.
Dolgachev: Department of Mathematics, University of Michigan  
Ann Arbor, MI 48109, USA  
e-mail: idolga@math.lsa.umich.edu  
De-Qi Zhang: Department of Mathematics, National University of Singapore  
Kent Ridge, Singapore  
e-mail: matzdq@math.nus.edu.sg