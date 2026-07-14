---
title: Explicit constructions of Halphen pencils
authors:
- Aline Zanardini
year: 2020
bibkey: Zan20
tags:
- paper
- extraction
abstract: |
  We construct rational elliptic surfaces of index two by explicitly constructing their associated Halphen pencils in the projective plane $\mathbb { P } ^ { 2 }$ .
  For each of the types of singular fibers that occur we construct at least one example having that type of fiber and in fact, for some, we construct all possible examples.
  We establish a precise dictionary between the fibers in a rational elliptic surface and the corresponding plane curves and, in particular, we study the singularities of the curves appearing in a Halphen pencil.
---

# EXPLICIT CONSTRUCTIONS OF HALPHEN PENCILS

ALINE ZANARDINI

Abstract.
We construct rational elliptic surfaces of index two by explicitly constructing their associated Halphen pencils in the projective plane $\mathbb { P } ^ { 2 }$ . For each of the types of singular fibers that occur we construct at least one example having that type of fiber and in fact, for some, we construct all possible examples.
We establish a precise dictionary between the fibers in a rational elliptic surface and the corresponding plane curves and, in particular, we study the singularities of the curves appearing in a Halphen pencil.

# Contents

1. Introduction 2\
   Organization 4\
   Acknowledgments 4
2. The Log Canonical Threshold 5
3. Rational Elliptic Surfaces with a Multiple Fiber 6\
   3.1. Halphen Pencils 7\
   3.2. The Jacobian 7
4. Halphen Pencils and Rational Elliptic Surfaces of index $m$ 8\
   4.1. The (unique) multiple cubic 11\
   4.2. The singularities of $B$ and the log canonical threshold 12
5. The curve $B$ when $F$ is of type $I I ^ { * } , I I I ^ { * }$ o r $I V ^ { * }$ 15\
   5.1. Non-Examples 16\
   5.2. All possible examples 24
6. Constructions of Halphen Pencils of index two 25
7. Geometric Descriptions 33\
   7.1. Type $I _ { n }$ 33\
   7.2. Type $I I$ 36\
   7.3. Type III 36\
   7.4. Type $I V$ 36\
   7.5. Type $I _ { n } ^ { * }$ 37\
   7.6. Type $I V ^ { * }$ 41\
   7.7. Type $I I I ^ { * }$ 49\
   7.8. Type $I I ^ { * }$ 54\
   References 57

# 1. Introduction

Elliptic surfaces play an important role in many questions from different areas of Mathematics and also in theoretical Physics.
They are central in the classification of algebraic surfaces, they appear in the construction of exotic four manifolds and they are also present in the formulation of F-theory.
Examples of elliptic surfaces include Enriques surfaces, Dolgachev surfaces, all surfaces of Kodaira dimension one and many rational surfaces.
In this paper we are interested in the latter.

We say a rational surface $Y$ is a rational elliptic surface if $Y$ admits a fibration $f : Y \to \mathbb { P } ^ { 1 }$ whose generic fiber is a smooth curve of genus one.
We do not necessarily assume the existence of a global section.
If $Y$ is a rational elliptic surface, then there exists some $m \geq 1$ , called the index of the fibration, so that $f$ is given by the anti-pluricanonical system $| - m K _ { Y } |$ . Moreover, $m = 1$ if and only if $f$ admits a global section and whenever $m > 1$ there exists exactly one multiple fiber in $Y$ , this of multiplicity $m$ (see e.g. [13, Chapter V, §6]).

Rational elliptic surfaces admitting a global section have been widely studied under many different points of view.
Different compactifications for their moduli space have been constructed and are well understood [1], [3], [4], [22], [33],[34]; their automorphism groups have been classified [24],[25]; and all possible configurations of singular fibers are known [36],[40]. It is also known that these surfaces can be realized from a pencil of cubic curves in the plane (by blowing-up their nine base points) and explicit examples having a Mordell-Weil group with some particular rank have been considered in [13, Theorem 5.6.2], [19],[39] and [42].

Nevertheless, there are not many explicit constructions in the literature for those rational elliptic surfaces that do not admit a global section.
The goal of this paper is to provide such explicit constructions.
For each of the types of singular fibers that occur we construct at least one example having that type of fiber and in fact, for some, we construct all possible examples.
Our approach is purely geometric.

Similar to the $m = 1$ case, rational elliptic surfaces of any index $m$ can be realized as a nine point blow-up of $\mathbb { P } ^ { 2 }$ , where the nine points are base points of a certain pencil of plane curves.
These are called Halphen pencils (of index $m$ ), after the French mathematician Georges Henri Halphen who first studied these objects in [21].

Concretely, if $f : Y \to \mathbb { P } ^ { 1 }$ is a rational elliptic surface, then there exists a birational map $\pi : Y \to \mathbb { P } ^ { 2 }$ so that $f \circ \pi ^ { - 1 }$ is a pencil of plane curves of degree $3 m$ having nine (possibly infinitely near) singular base points of multiplicity $m$ . In particular, any fiber $F$ corresponds to a plane curve $B$ of degree $3 m$ , namely $\pi ( F )$ [13, Theorem 5.6.1].

An important ingredient in our approach is the study of the singularities of a plane curve occurring in a Halphen pencil.
The log canonical threshold (lct) plays an important role.
We establish some precise relations between the log canonical thresholds of the pairs $( Y , F )$ and $( \mathbb { P } ^ { 2 } , B )$ , which provide us with bounds for the lct of the latter.
We prove the following results, where $M _ { B }$ (resp.
$M _ { F }$ ) denotes the largest multiplicity of a component of $B$ (resp.
$F$ ):

Theorem 1.1. If $F ^ { \prime }$ is any (non-multiple) fiber of $Y$ , then the corresponding plane curve $B$ is such that

$$
l c t ( \mathbb { P } ^ { 2 } , B ) \leq \frac { 1 } { M _ { B } } \leq 2 l c t ( Y , F )
$$

and these inequalities do not depend on the index m of the fibration.

Further,

(i) if $m > 1$ and $F$ is reduced, then $B$ is reduced and we have

$$
\frac { 1 } { m } < l c t ( \mathbb { P } ^ { 2 } , B ) \leq l c t ( Y , F )
$$

(ii) if $M _ { F } \geq m$ and $F$ is not reduced, then

$$
l c t ( Y , F ) \leq l c t ( \mathbb { P } ^ { 2 } , B )
$$

In fact we establish a dictionary between the fibers in the surface and the corresponding plane curves.
When $m \ = \ 2$ and $F$ is of type $I I ^ { * } , I I I ^ { * }$ or $I V ^ { * }$ we obtain the following complete characterization for the plane curve $B$ :

Theorem 1.2. A fiber $F$ of type $I I ^ { * }$ can only be realized by one of the following plane curves:

(i) a triple conic (ii) a nodal cubic and an inflection line, with the line taken with multiplicity three (iii) two triples lines (iv) a conic and a tangent line, with the line taken with multiplicity four (v) a line with multiplicity five and another line If $F$ is of type $I I I ^ { * }$ , then $F$ can only be realized by one of the following curves: (i) a double line, a cubic and another line (ii) a double conic and another conic (iii) a triple conic (iv) two triple lines (v) a triple line, a double line and another line (vi) a triple line, a conic and a line (vii) a triple line and a cubic (viii) a conic and a line, with the line taken with multiplicity four (ix) a line with multiplicity four and two other lines

And whenever $F ^ { \prime }$ is of type $I V ^ { * }$ we have that $F$ can only be realized by one of the curves below:

(i) a double conic and a conic (ii) a double line, a conic and two lines (iii) a double line, a cubic and a line (iv) a double line and two conics (v) two double lines and two lines (vi) two double lines and a conic (vii) a double conic and two lines (viii) a triple conic (ix) a triple line, a conic and a line (x) a triple line, a double line and another line (xi) a triple line and three lines (xii) a triple line and a cubic

Conversely, we can construct a Halphen pencil of index two, $\lambda B + \mu ( 2 C ) = 0$ , where $B$ is any one of the curves above and the corresponding (non-multiple) fiber is of type $I I ^ { * } , I I I ^ { * }$ or $I V ^ { * }$ .

And for any index $m$ we prove Proposition 1.3 below, providing a new proof for a result of Miranda [33, Lemma 6.4].

The many examples we construct complement (and in some sense complete) the few existing ones considered in [15],[16],[26] and [27]. Some examples of rational elliptic surfaces $Y$ of index two have also been constructed independently by Antonio Laface [31]. His approach, however, builds on the analysis of lattices by considering the $( - 1 )$ curves of $Y$ as integer points in a polytope inside $P i c ( Y )$ and then using information about the intersection form.

Surprisingly, Halphen pencils have appeared in [6] in the solution of a problem in Diophantine geometry and a generalization to higher dimensions has been considered in [11] and [12]. Other possible applications include the study of certain $K 3$ surfaces [2], [45] and the construction of: F-theory compactifications [26],[27], discrete Painlevé equations [41] and a moduli space for rational elliptic surfaces of index two [44].

In a forthcoming paper [44] we will use the constructions of Halphen pencils presented here and the results from Section 4 to study the stability, in the sense of geometric invariant theory (GIT), of Halphen pencils under the action of $S L ( 3 )$ and hence, to construct a compactification for the moduli space of rational elliptic surfaces of index two.
This was our original motivation and it also explains why we have exhibited all possible examples of Halphen pencils yielding rational elliptic surfaces with fibers of type $I I ^ { * } , I I I ^ { * }$ or $I V ^ { * }$ (Theorems 5.15, 5.16 and 5.17). In [44] we show these types of fiber are associated with unstability.

The work of Miranda in [33] describes the GIT stability conditions for pencils of plane cubics, which leads to a compactification of the moduli space of rational elliptic surfaces with section.
Such compactification agrees with the one obtained by the same author in [34], where the surfaces are described by equations, namely their Weierstrass models.

When the existence of a global section is not assumed, there is no analogue for the Weierstrass model and even the dimensions of the parameter spaces involved are much higher, which makes it much harder to solve the classification problem.
Tools from Birational Geometry and the results obtained in this paper have helped us to overcome such difficulties.

Organization.
The paper is organized as follows: We begin, in Section 2, by presenting some basic background material from Birational Geometry that will be needed later.
Next, in Section 3 we introduce the geometric objects we are interested in, namely rational elliptic surfaces and their associated Halphen pencils.
Section 4 is devoted to establishing the dictionary between the curves in a Halphen pencil and the fibers in the corresponding elliptic surface.
In particular, we study the log canonical thresholds of the plane curves that can occur in a Halphen pencil.
In Section 5 we prove Theorems 5.15, 5.16 and 5.17 that completely characterize all possible examples of Halphen pencils of index two yielding fibers of type $I I ^ { * } , I I I ^ { * }$ and $I V ^ { * }$ . Then in Section 6 we present many new constructions of Halphen pencils of index two.
These are summarized in Tables 2 through 8. A more detailed and explicit geometric description is given right after in Section 7. We work over $\mathbb { C }$ .

Acknowledgments.
I would like to thank my advisor, Antonella Grassi, for the many insightful conversations, the numerous enriching suggestions on earlier drafts and the encouragement for writing this paper.
I also would like to thank Antonio Laface for helpful conversations.
This work is part of my PhD thesis and it was partially supported by a

Dissertation Completion Fellowship at the University of Pennsylvania.
This project originated from work supported by NSF Grant No. DMS-1440140 while the author was a program associate at MSRI during the Spring 2019 semester.

# 2. The Log Canonical Threshold

We first recall some necessary background notions in Birational Geometry concerning log canonical pairs.
We refer to [30] for a more detailed exposition.

Let $X$ be a normal algebraic variety and let $\Delta = \sum d _ { i } D _ { i } \subset X$ be a $\mathbb { Q }$ -divisor, i.e. a $\mathbb { Q }$ -linear combination of prime divisors.

Definition 2.1. Given any birational morphism $\mu : \tilde { X } \to X$ , with $\tilde { X }$ normal, we can write

$$
K _ { \tilde { X } } \equiv \mu ^ { * } ( K _ { X } + \Delta ) + \sum a _ { E } E
$$

where $E \subset { \tilde { X } }$ are distinct prime divisors, $a _ { E } \doteq a ( E , X , \Delta )$ are the discrepancies of $E$ with respect to $( X , \Delta )$ and a nonexceptional divisor $E$ appears in the sum if and only if $E = \mu _ { * } ^ { - 1 } D _ { i }$ for some $i$ (in that case with coefficient $a ( E , X , \Delta ) = - d _ { i } )$ .

Definition 2.2. A log resolution of the pair $( X , \Delta )$ consists of a proper birational morphism $\mu : \tilde { X } \to X$ such that $\tilde { X }$ is smooth and $\mu ^ { - 1 } ( \Delta ) \cup E x c ( \mu )$ is a divisor with global normal crossings.

Definition 2.3. We say $( X , \Delta )$ is log canonical if $K _ { X } + \Delta$ is $\mathbb { Q }$ -Cartier and given any log resolution $\mu : \tilde { X } \to X$ we have

$$
K _ { \tilde { X } } \equiv \mu ^ { * } ( K _ { X } + \Delta ) + \sum a _ { E } E
$$

with all $a _ { E } \geq - 1$ .

Remark 2.4. In particular, if $X$ is smooth and $\Delta = d _ { i } D _ { i }$ is simple normal crossings, then $( X , \Delta )$ is log canonical if and only if $d _ { i } \leq 1$ for all $i$ .

Definition 2.5. The number

$l c t ( X , \Delta ) \doteq \operatorname* { s u p } \{ \ t \ ; \ ( X , t \Delta )$ is log canonical}

is called the log canonical threshold of $( X , \Delta )$ .

We can also consider a local version:

$l c t _ { p } ( X , \Delta ) \doteq \operatorname* { s u p } \{ \ t \ ; \ ( X , t \Delta )$ is log canonical in an open neighborhood of $p \}$

where $p \in X$ is a closed point.

Lemma 2.6. Given a log resolution $\mu : \tilde { X } \to X$ , write

$$
K _ { \tilde { X } } = \mu ^ { * } K _ { X } + \sum a _ { i } E _ { i } ~ a n d ~ \mu ^ { * } \Delta = \tilde { \Delta } + \sum b _ { i } E _ { i }
$$

where $\tilde { \Delta } = d _ { i } \tilde { D } _ { i }$ (resp.
${ \tilde { D } } _ { i }$ ) denotes the strict transform of $\Delta$ (resp.
$D _ { i }$ ) under $\mu$ and $E _ { i } \subset { \tilde { X } }$ are the exceptional divisors of $\mu$ . Then

$$
l c t ( X , \Delta ) = \operatorname* { m i n } \left\{ \frac { 1 + a _ { i } } { b _ { i } } , \frac { 1 } { d _ { i } } , 1 \right\}
$$

We now introduce the geometric objects we are interested in studying in this paper, namely rational elliptic surfaces and their associated Halphen pencils.
We point the reader to [13, Chapter V, §6] for more details.

Let $Y$ be a smooth and projective surface and let $f : Y  C$ be a fibration (a surjective proper flat morphism) such that the generic fiber is a smooth genus one curve.
And, further, assume $Y$ is relatively minimal, meaning there are no $( - 1 ) -$ curves in any fiber.
We will refer to this data as an elliptic surface1, even though the generic fiber of $f$ does not necessarily have the structure of an elliptic curve.

Any elliptic surface has finitely many singular fibers and the configuration of all nonmultiple singular fibers is exactly the same as the one in the associated Jacobian fibration (see Section 3.2). The possible non-multiple singular fibers have been classified by Kodaira and Néron [28],[29] and [38] and Table 1 below gives the full classification.
Over a field of characteristic zero, any multiple fiber is of type $I _ { n }$ for some $n \geq 0$ [13, Proposition 5.1.8] .

Table 1. Kodaira’s Classification

<table><tr><td>Kodaira Type</td><td> Number of Components</td><td>Dual Graph</td></tr><tr><td>I</td><td>1 (smooth)</td><td>·</td></tr><tr><td>1</td><td>1 (with a node)</td><td>.</td></tr><tr><td>In</td><td>n≥2</td><td>An-1</td></tr><tr><td>II</td><td>1 (with a cusp)</td><td>·</td></tr><tr><td>III</td><td>2</td><td>A</td></tr><tr><td>IV</td><td>3</td><td>A</td></tr><tr><td>I</td><td>n+5</td><td>D4+n</td></tr><tr><td>IV*</td><td>7</td><td>E6</td></tr><tr><td>III*</td><td>8</td><td>E</td></tr><tr><td>II*</td><td>9</td><td>E</td></tr></table>

Given $f : Y \to C$ as before, we define the index of the fibration, and denote it by $d _ { Y }$ , as the positive generator of the ideal

$$
\{ D \cdot Y _ { \eta } \ ; \ D \in \operatorname { P i c } ( Y ) \} \preceq \mathbb { Z }
$$

where $Y _ { \eta }$ is a generic fiber.
Since $Y$ is projective $d _ { Y }$ is always finite.

Note that $d _ { Y } = 1$ if and only if $f$ admits a section, if and only if the generic fiber has the structure of a (smooth) elliptic curve.

In this paper we are interested in the situation where $Y$ is rational and $d _ { Y } > 1$ . One can show that when $Y$ is rational then $C \simeq \mathbb { P } ^ { 1 }$ (Luröth’s Theorem) and $f$ is given by the linear system $\vert - m K _ { Y } \vert$ , where $m = d _ { Y }$ (Proposition 3.2). In particular, $K _ { Y } ^ { 2 } = 0$ and $Y$ can be obtained as a nine-point blow-up of $\mathbb { P } ^ { 2 }$ .

# 3.1. Halphen Pencils.

Definition 3.1. A Halphen pencil of index m is a pencil of plane curves of degree 3m with nine (possibly infinitely near) base points of multiplicity $m$ .

Such geometric object is in one-to-one correspondence with rational elliptic surfaces:

Proposition 3.2 ([13, Theorem 5.6.1], [15, Main Theorem 2.1]). Let $f : Y \to \mathbb { P } ^ { 1 }$ be a rational elliptic surface of index m and let $F ^ { \prime }$ be a choice of a fiber of $f$ , then there exists a birational map $\pi : Y  \mathbb { P } ^ { 2 }$ so that $f \circ \pi ^ { - 1 }$ is a Halphen pencil of index m and, moreover, $B \doteq \pi ( F )$ is a plane curve of degree $3 m$ :

$$
\begin{array} { r } { F \subset \underset { \substack { f \searrow \hdots \hdots \hdots \hdots \hdots } } { \underbrace { Y \textrm { -- } \pi \textrm { -- } \pi } } \underset { \substack { f \hdots \hdots \hdots } } { \underbrace { \pi } } } & { } \\ { \underset { \substack { \mathrm { ~ \textemdash ~ } \biggr } } { \overbrace { f } } } \end{array}
$$

Conversely, given a Halphen pencil of index $m$ , taking the minimal resolution of its base points we obtain a rational elliptic surface of index $m$ .

Moreover, since the canonical bundle formula (see e.g. [5, Theorem 12.1]) implies Lemma 3.3 below we have that any Halphen pencil of index $m$ contains exactly one cubic of multiplicity $m$ , which corresponds to the unique multiple fiber in the associated rational elliptic surface.
In fact the cubic corresponds to a fiber of type $I _ { n }$ for some $n \leq 9$ [13, Proposition 5.1.8]. And if none of the base points are singular points of the cubic, then we can further restrict to $n \leq 3$ (Lemma 4.8).

Lemma 3.3 ([13, Proposition 5.61,(iii)]). If $f : Y \to \mathbb { P } ^ { 1 }$ is a rational elliptic surface, then $f$ has at most one multiple fiber.

3.2. The Jacobian.
If $f : Y \to C$ is an elliptic surface of index $m > 1$ , then the generic fiber $Y _ { \eta }$ is a smooth genus one curve over the function field of $C$ that has no rational points over this field (the fibration has no sections).
If we let $J a c ( Y _ { \eta } )$ denote the corresponding Jacobian variety of divisors of degree 0 on $Y _ { \eta }$ that is, the connected component of the identity of $P i c ( Y _ { \eta } )$ , then we can construct an elliptic surface $J  C$ with a section whose generic fiber $J _ { \eta }$ is isomorphic to $J a c ( Y _ { \eta } )$ . The fibration $J  C$ is called the associated Jacobian fibration (to $f : Y \to C$ ).

If $Y$ is rational, then $J$ is also rational [13, Proposition 5.6.1 (ii)] and one can prove the following:

Theorem 3.4 ([13, Corollary 5.4.7]). Let $J \to \mathbb { P } ^ { 1 }$ be a rational elliptic surface with section.
Given $m \geq 1$ and a closed point $p \in \mathbb { P } ^ { 1 }$ such that $J _ { p }$ is of type $I _ { n } , 0 \leq n \leq 9$ , there exists a rational elliptic surface $Y  \mathbb { P } ^ { 1 }$ of index m with unique multiple fiber $Y _ { p } = m { \overline { { Y } } } _ { p }$ satisfying $\overline { { Y } } _ { p } \simeq J _ { p }$ . Moreover, $[ Y ]$ is an element of order $m$ in $H ^ { 1 } ( \mathbb { P } ^ { 1 } , \mathcal { I } )$ , the group of isomorphism classes of torsors over the generic fiber $J _ { \eta }$ .

Moreover, the Shioda-Tate formula (see e.g. [43, Corollary 6.13]) applied to the associated Jacobian fibration $J \to \mathbb { P } ^ { 1 }$ implies that the possible singular fibers occurring on $J$ (hence on $Y$ ) can have at most 9 irreducible components.
In particular, following Kodaira’s classification, if $F ^ { \prime }$ is a singular fiber of a rational elliptic surface $Y  \mathbb { P } ^ { 1 }$ , then $F$ is of type $I _ { n }$ for $n \leq 9 , I I , I I I , I V , I _ { n } ^ { * }$ for $n \leq 4 , I I ^ { * } , I I I ^ { * }$ o r $I V ^ { * }$ . In fact, given any integer $m > 1$ any type in this list can be realized by some rational elliptic surface $Y  \mathbb { P } ^ { 1 }$ of index $m$ . More precisely,

Proposition 3.5 ([13, Corollary 5.6.6]). If $Y _ { p }$ is a non-multiple fiber of a rational elliptic surface $Y  \mathbb { P } ^ { 1 }$ of index $m$ , then $b _ { 2 } ( Y _ { p } ) \leq 9$ and any Kodaira type satisfying this condition can be realized.

Such statement, however, does not provide explicit constructions, which we do in this paper.

4. Halphen Pencils and Rational Elliptic Surfaces of index m

In this section we will establish a dictionary between the curves in a Halphen pencil and the fibers in the corresponding rational elliptic surface.
In particular, we will provide a description of the singularities of a plane curve in a Halphen pencil.
But first we need to introduce some notations and deduce some equations.

We will fix a Halphen pencil of index $m$ and we will denote it by $\mathcal { P }$ . The corresponding rational elliptic surface will be denoted by $f : Y \to \mathbb { P } ^ { 1 }$ and $\pi : Y  \mathbb { P } ^ { 2 }$ will denote the blow-up at the nine base points of $\mathcal { P }$ .

If $F ^ { \prime }$ is any (non-multiple) fiber of $Y$ we will denote by $B$ the corresponding plane curve of degree $3 m$ , i.e. $\pi ( F )$ . Further, $m C$ will denote the unique multiple cubic of $\mathcal { P }$ and $m E$ will denote the unique multiple fiber of $f$ .

Because $- K _ { Y }$ is nef, every smooth rational curve $R$ on $Y$ has self-intersection $R ^ { 2 } \geq - 2$ (adjunction formula).
This implies we can write the set of base points of $\mathcal { P }$ as in [7, Section 2]:

$$
\{ P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( a _ { 1 } ) } , \ldots , P _ { k } ^ { ( 1 ) } , \ldots , P _ { k } ^ { ( a _ { k } ) } \}
$$

where $a _ { 1 } + \ldots + a _ { k } = 9$ , $P _ { j } ^ { ( 1 ) }$ are points in $\mathbb { P } ^ { 2 }$ and $P _ { j } ^ { ( i + 1 ) }$ is infinitely near to the previous point $P _ { j } ^ { ( i ) }$ (of order 1).

Moreover, if $C$ is smooth and we choose a flex point as the origin for the group law $\bigoplus$ on $C$ , then [7]:

$$
a _ { 1 } P _ { 1 } ^ { ( 1 ) } \oplus . . . \oplus a _ { k } P _ { k } ^ { ( 1 ) } = \varepsilon _ { m }
$$

where $\varepsilon _ { m }$ is a torsion point of order $m$ in $C$ (w.r.t $\bigoplus$ ).

Expressing the base points of $\mathcal { P }$ as in (1) is the same as saying that each exceptional curve

$$
E _ { j } \doteq \pi ^ { - 1 } ( P _ { j } ^ { ( 1 ) } )
$$

consists of a chain of $\left( - 2 \right)$ curves of length $( a _ { j } - 1 )$ with one more $( - 1 )$ curve at the end of the chain.
The latter a multisection of degree $m$ .

Thus, whenever we write

$$
F = \overline { { F } } + d _ { 1 } ^ { ( 1 ) } E _ { 1 } ^ { ( 1 ) } + \ldots + d _ { 1 } ^ { ( a _ { 1 } - 1 ) } E _ { 1 } ^ { ( a - 1 ) } + \ldots + d _ { k } ^ { ( 1 ) } E _ { k } ^ { ( 1 ) } + \ldots + d _ { k } ^ { ( a _ { k } - 1 ) } E _ { k } ^ { ( a _ { k } - 1 ) }
$$

where $\overline { F }$ denotes the strict transform of $B$ under $\pi$ and each $E _ { j } ^ { ( i ) }$ is the $\pi$ -exceptional divisor over the base point $P _ { j } ^ { ( i ) }$ ; we have the following (dual) picture for the components of $E _ { j }$ appearing in the fiber $F ^ { \prime }$ :

![](images/36ba4984c686f8afb5562c396ee467f2539eec6311e2e0b207d1db80a2e4bb17.jpg)\
Figure 1. Chains of exceptional rational curves appearing in $F ^ { \prime }$

Because the chains $E _ { j }$ are disjoint from each other, it follows that:

Lemma 4.1. If we color the nodes of the dual graph of $F$ corresponding to the components coming from $B$ in blue and the nodes corresponding to the exceptional components $d _ { j } ^ { ( i ) } E _ { j } ^ { ( i ) }$ in black, then every black node is connected to at most two other black nodes.

This simple observation has some interesting consequences like Propositions 4.2 and 4.3 below.
In Section 5 we also use Lemma 4.1 repeatedly in order to characterize which curves $B$ can yield a fiber of type $I I ^ { * } , I I I ^ { * }$ or $I V ^ { * }$ when $m = 2$ .

Proposition 4.2. If $F$ is of type $I I ^ { * } , I I I ^ { * }$ or $I V ^ { * }$ , then $B \doteq \pi ( F )$ cannot be reduced.

Proof.
If $B$ were reduced, then coloring the dual graph of $F$ as in Lemma 4.1 we would obtain a black node which is connected to more than two black nodes.


Proposition 4.3. If $F$ is of type $I I ^ { * }$ , then $M _ { B } \geq 3$ , where $M _ { B }$ denotes the largest multiplicity of a component of $B$ .

Proof.
Again, we look at the dual graph of $F$ . Assuming $M _ { B } < 3$ contradicts Lemma 4.1.

Writing $F ^ { \prime }$ as in (2) we can further deduce Equation (3) below, which computes the number of components of $F ^ { \prime }$ .

Proposition 4.4. If $n _ { F }$ and $n _ { B }$ denote the number of components of $F$ and $B$ , respectively, then

$$
{ \mathrm { \Pi } } _ { F } = n _ { B } + \sum _ { j = 1 } ^ { k } ( a _ { j } - 1 ) - n _ { E \backslash C } = n _ { B } + \sum _ { j = 1 } ^ { k } a _ { j } - k - n _ { E \backslash C } = n _ { B } + 9 - k - n _ { E \backslash C } = n _ { C } + 1 .
$$

where $n _ { E \backslash C }$ denotes the difference between the number of components of $E$ and the number of components of $C$ .

The type of the multiple fiber $m E$ imposes restrictions on the numbers $n _ { E \backslash C }$ appearing in Equation 3 above.
For instance, whenever $m > 1$ we have that

Lemma 4.5. If $F$ is of type $I V ^ { * }$ , then $n _ { E \backslash C } \in \{ 0 , 1 , 2 \}$ and if $F$ is of type $I I I ^ { * }$ (resp.
$I I ^ { * }$ ) , then $n _ { E \backslash C } \in \{ 0 , 1 \}$ (resp.
$n _ { E \backslash C } = 0$ ).

Proof.
If $m > 1$ and $F$ is of type $I V ^ { * } , I I I ^ { * }$ o r $I I ^ { * }$ , then the classification in [36] tells us the unique multiple fiber $m E$ of $Y$ can be realized as the strict transform of $m C$ . If $F$ is of type $I V ^ { * }$ , then $E$ is of type $I _ { 0 } , I _ { 1 } , I _ { 2 }$ or $I _ { 3 }$ . Whereas if $F$ is of type $I I I ^ { * }$ (resp.
$I I ^ { * }$ ), then $E$ is of type $I _ { 0 } , I _ { 1 }$ or $I _ { 2 }$ (resp.
$I _ { 0 }$ or $I _ { 1 }$ ). 

Remark 4.6. If $m = 1$ and $B$ is any given curve in $\mathcal { P }$ , then we can always take the other generator of $\mathcal { P }$ to be a smooth cubic.
In particular, we can always assume that $n _ { E \backslash C } = 0$ i n Equation (3).

We can also write

$$
K _ { Y } = \pi ^ { * } K _ { \mathbb { P } ^ { 2 } } + b _ { 1 } ^ { ( 1 ) } E _ { 1 } ^ { ( 1 ) } + \ldots + b _ { 1 } ^ { ( a _ { 1 } ) } E _ { 1 } ^ { ( a _ { 1 } ) } + \ldots + b _ { k } ^ { ( 1 ) } E _ { k } ^ { ( 1 ) } + \ldots + b _ { k } ^ { ( a _ { k } ) } E _ { k } ^ { ( a _ { k } ) }
$$

and

$$
\pi ^ { * } { \cal B } = \overline { { { { \cal F } } } } + c _ { 1 } ^ { ( 1 ) } E _ { 1 } ^ { ( 1 ) } + \ldots + c _ { 1 } ^ { ( a _ { 1 } ) } E _ { 1 } ^ { ( a _ { 1 } ) } + \ldots + c _ { k } ^ { ( 1 ) } E _ { k } ^ { ( 1 ) } + \ldots + c _ { k } ^ { ( a _ { k } ) } E _ { k } ^ { ( a _ { k } ) }
$$

and we know how to compute each of the multiplicities $b _ { j } ^ { ( i ) } \doteq b _ { j } ^ { ( i ) } ( B ) , c _ { j } ^ { ( i ) } \doteq c _ { j } ^ { ( i ) } ( B )$ and $d _ { j } ^ { ( i ) } \doteq d _ { j } ^ { ( i ) } ( B )$ rather explicitly.

For any base point $P _ { j } ^ { ( 1 ) }$ , the induced pencil on the surface obtained by blowing-up $P _ { j } ^ { ( 1 ) }$ is

$$
( \pi _ { j } ^ { ( 1 ) } ) ^ { * } \mathcal { P } - m E _ { j } ^ { ( 1 ) }
$$

where $\pi _ { j } ^ { ( 1 ) }$ is the blow-up map.
In particular, given any curve $B$ of $\mathcal { P }$ , the induced member is

$$
B _ { j } ^ { ( 1 ) } + ( m _ { P _ { j } ^ { ( 1 ) } } ( B ) - m ) E _ { j } ^ { ( 1 ) }
$$

where ${ B } _ { j } ^ { ( 1 ) }$ is the strict transform of $B$ under $\pi _ { j } ^ { ( 1 ) }$ and $m _ { P _ { j } ^ { ( 1 ) } } ( B )$ denotes the multiplicity of the point $P _ { j } ^ { ( 1 ) }$ on the curve $B$ .

In other words, $d _ { j } ^ { ( 1 ) } = m _ { P _ { j } ^ { ( 1 ) } } ( B ) - m$ and, more generally,

$$
d _ { j } ^ { ( i ) } = d _ { j } ^ { ( i - 1 ) } + m _ { P _ { j } ^ { ( i ) } } ( B ) - m
$$

where m (i)(B) denotes the multiplicity of the point $P _ { j } ^ { ( i ) }$ on the strict transform of the curve $B$ under the blow-up of (1), . . . , P (i−1)j .

On the other hand, we also know that $c _ { j } ^ { ( 1 ) } = m _ { p _ { j } ^ { ( 1 ) } } ( B )$ and

$$
c _ { j } ^ { ( i ) } = c _ { j } ^ { ( i - 1 ) } + m _ { P _ { j } ^ { ( i ) } } ( B ) = m _ { P _ { j } ^ { ( 1 ) } } ( B ) + . . . + m _ { P _ { j } ^ { ( i ) } } ( B )
$$

Thus,

$$
I _ { j } ^ { ( i ) } = c _ { j } ^ { ( i - 1 ) } + m _ { P _ { j } ^ { ( i ) } } ( B ) - i \cdot m = c _ { j } ^ { ( i ) } - i \cdot m = m _ { P _ { j } ^ { ( 1 ) } } ( B ) + \ldots + m _ { P _ { j } ^ { ( i ) } } ( B ) - i \cdot m = c _ { j } ^ { ( i ) } - i \cdot m = 0 ,
$$

In particular,

$$
d _ { j } ^ { ( i ) } \leq i \cdot ( m _ { P _ { j } ^ { ( 1 ) } } ( B ) - m ) \leq i \cdot 2 m
$$

And the condition $d _ { j } ^ { ( a _ { j } ) } = 0$ implies

$$
m _ { P _ { j } ^ { ( 1 ) } } ( B ) + \ldots + m _ { P _ { j } ^ { ( a _ { j } ) } } ( B ) = a _ { j } \cdot m
$$

Therefore, whenever $C$ is smooth at the base point $P _ { j } ^ { ( 1 ) }$ , using Noether’s formula [17] we obtain

$$
I _ { P _ { j } ^ { ( 1 ) } } ( B , C ) = a _ { j } \cdot m
$$

where I (1)(B, C) denotes the intersection multiplicity of $B$ and $C$ at the point $P _ { j } ^ { ( 1 ) }$ .

Lastly, we have $b _ { j } ^ { ( i ) } = i$ for all $j = 1 , \dots k$ and $i = 1 , \dotsc , a _ { j }$

4.1. The (unique) multiple cubic.
The cubic $C$ is smooth at every base point of $\mathcal { P }$ if and only if $\pi$ restricts to an isomorphism $E \simeq C$ . This implies any $\pi -$ exceptional curve must be either a multisection or a component of $F$ .

We also prove a partial converse of this statement:

Lemma 4.7. For any index m and any type of fiber we have

$$
d _ { j } ^ { ( 1 ) } > 0 \Rightarrow m _ { P _ { j } ^ { ( 1 ) } } ( m C ) = m
$$

That is, if the exceptional curve $E _ { j } ^ { ( 1 ) }$ appears as a component in $F$ (with multiplicity $d _ { j } ^ { ( 1 ) } > 0$ ) then $C$ is smooth at the point $P _ { j } ^ { ( 1 ) }$ .

Proof.
If the exceptional curve $E _ { j } ^ { ( 1 ) }$ appears as a component in $F$ , then $m E _ { j } ^ { ( 1 ) }$ cannot appear as a component of the multiple fiber $m E$ . Hence $m _ { P _ { j } ^ { ( 1 ) } } ( m C ) - m = 0$ . 

Corollary 4.7.1. If $C$ is singular at a base point $P _ { j } ^ { ( 1 ) }$ , then $m _ { P _ { j } ^ { ( 1 ) } } ( B ) = m$ . Moreover, at the point $P _ { j } ^ { ( 1 ) }$ the curve $B$ consists of a single component (branch) with multiplicity $m$ .

Proof.
It follows from Lemma 4.7 that if $C$ is singular at a base point $P _ { j } ^ { ( 1 ) }$ , then $E _ { j } ^ { ( 1 ) }$ is not a component of $F ^ { \prime }$ , hence $d _ { j } ^ { ( 1 ) } = 0$ , which further implies $m _ { P _ { j } ^ { ( 1 ) } } ( B ) = m$ . The last statement is obvious, otherwise one would need to blow-up more than one point lying in $E _ { j } ^ { ( 1 ) }$ in order to separate $\mathcal { P }$ . 

Since we are working over a field of characteristic zero, the unique multiple fiber $m E$ can only be of multiplicative type, i.e. of type $I _ { n }$ . If $n \leq 3$ , then $m E$ can be realized as the strict transform (under $\pi$ ) of the unique multiple cubic $m C$ . But if $n > 3$ , then, necessarily, $C$ must be singular at a base point of $\mathcal { P }$ . In other words,

Lemma 4.8. If $Y$ contains a multiple fiber of type $I _ { n }$ with $4 \leq n \leq 9$ , then $C$ is singular at a base point of $\mathcal { P }$ .

Proof.
If $C$ is smooth at every base point of $\mathcal { P }$ , then the corresponding multiple fiber on $Y$ is given by

$$
m \overline { { C } } + m \cdot \sum _ { i , j } ( m _ { P _ { j } ^ { ( i ) } } ( C ) - 1 ) E _ { j } ^ { ( i ) } = m \overline { { C } }
$$

where $\overline { C }$ is the strict transform of $C$ under $\pi$ and $m _ { P _ { j } ^ { ( i ) } } ( C ) = 1$ is the multiplicity of $P _ { j } ^ { ( i ) }$ on the strict transform of $C$ under the blow-up of $P _ { j } ^ { ( 1 ) } , \ldots , P _ { j } ^ { ( i - 1 ) }$ . That is, the multiple fiber of $Y$ is simply given by the strict transform of $m C$ . But each of the fibers $I _ { n } ( 4 \leq n \leq 9 )$ have at least four components and hence the corresponding multiple fiber cannot be realized as strict transforms of a multiple cubic in the plane, a contradiction.


When $C$ is singular at a base point of $\mathcal { P }$ , it is also useful and interesting to understand how singular it can be.

Proposition 4.9. For any index m we have that $l c t ( \mathbb { P } ^ { 2 } , m C ) = \frac { 1 } { m } .$

Proof.
If $C$ is irreducible, then there is nothing to prove.
Otherwise, we claim that $C$ consists of either a conic and a line intersecting it transversally or three distinct lines in general position (i.e. not concurrent at a point).

Clearly $C$ cannot be non-reduced so we must exclude the following three cases:

(a) a cusp (b) a conic and a tangent line (c) three concurrent lines

Because the unique multiple fiber of $Y$ can only be of type $I _ { n } , n \leq 9$ , in any of the above cases the singular point of $C$ must be a base point of the pencil $\mathcal { P }$ . Moreover, since (c) can be obtained as soon as one blow-up (of the tangency point) is performed in a cubic as in (b) and, in turn, (b) can be obtained as soon as one blow-up (of the cusp) is performed in a cubic as in (a), it suffices to consider only case (c). But blowing-up the concurrency point yields a component with multiplicity $2 m$ , which is an absurd.
Such component is not a multisection of degree $m$ and it cannot be a component in the multiple fiber either.


Proposition 4.10. If $F ^ { \prime }$ is of type $I V ^ { * }$ o r $I I I ^ { * }$ , then $C$ is singular at most one base point of $\mathcal { P }$ .

Proof.
From the proof of Proposition 4.9 we know that $C$ is reduced and either $C$ is irreducible or it consists of a conic and a line intersecting transversally or three lines in general position.
Moreover, from the classification in [36] we also know that if $F ^ { \prime }$ is of type $I V ^ { * }$ (resp.
$I I I ^ { * }$ ), then the multiple fiber $m E$ can only be of type $I _ { 0 } , I _ { 1 } , I _ { 2 }$ or $I _ { 3 }$ (resp.
$I _ { 0 } , I _ { 1 }$ or $I _ { 2 }$ ). Now, if $C$ were singular at more than one base point of $\mathcal { P }$ , then $C$ would necessarily consist of a conic and a line intersecting transversally and the two intersecting points would be base points of $\mathcal { P }$ . But then we would need to blow-up each of those two points at least twice, which would yield at least two more components in the multiple fiber.
That is, $m E$ would be of type $I _ { n }$ with $n \geq 4$ , a contradiction.


Remark 4.11. If $F ^ { \prime }$ is of type $I I ^ { * }$ , then $C$ must be smooth at every base point of $\mathcal { P }$ , because $E$ is of type $I _ { 0 }$ or $I _ { 1 }$ [36]. In particular, $E$ (hence $C$ ) is irreducible, $\pi$ restricts to an isomorphism $E \simeq C$ and $C$ cannot be singular at any base point of $\mathcal { P }$ .

4.2. The singularities of $B$ and the log canonical threshold.
We are now ready to study the singularities of the curve $B$ in terms of the type of the fiber $F ^ { \prime }$ . We investigate the multiplicities of $B$ at the base points of $\mathcal { P }$ and we compute bounds for the log canonical threshold of the pair $\left( \mathbb { P } ^ { 2 } , B \right)$ by establishing some relations between the log canonical thresholds of the pairs $( Y , F )$ and $( \mathbb { P } ^ { 2 } , B )$ .

We begin by proving the following Lemma:

Lemma 4.12. If $\mathcal { P }$ does not contain an infinitely near point as a base point (i.e $a _ { j } = 1$ for all $j = 1 , \ldots , k _ { j }$ , then $k = 9$ and

$$
F = \overline { { { F } } } + \sum _ { j = 1 } ^ { 9 } ( m _ { P _ { j } ^ { ( 1 ) } } ( B ) - m ) E _ { j } ^ { ( 1 ) } = \overline { { { F } } }
$$

Proof.
If $a _ { j } = 1$ for all $j = 1 , \dots , k$ , then it is clear that $k = 9$ , since $a _ { 1 } + \ldots + a _ { k } = 9$ . Moreover, $0 = d _ { j } ^ { ( a _ { j } ) } = d _ { j } ^ { ( 1 ) } = m _ { P _ { j } ^ { ( 1 ) } } ( B ) - m$ for all $j = 1 , \dots , 9$ . 

Corollary 4.12.1. Let $S _ { F }$ denote the sum of all the multiplicities of the components of $a$ fiber $F$ and let $n _ { F }$ denote the number of its components.
If either $S _ { F } > 3 m$ or $n _ { F } > 3 m$ , then $\mathcal { P }$ must contain an infinitely near point as a base point.
In particular, there exists some $1 \le j \le k$ so that $a _ { j } > 1$ and $d _ { j } ^ { ( 1 ) } \geq 1$ .

Proof.
If $\mathcal { P }$ does not contain an infinitely near point as a base point, then Lemma 4.12 tells us $F ^ { \prime }$ is the strict transform of a member of $\mathcal { P }$ , which implies both $S _ { F } \leq 3 m$ and $n _ { F } \le 3 m$ . 

Corollary 4.12.2. Using the same notations as in Corollary 4.12.1, if a fiber $F$ is such that $S _ { F } > 3 m$ or $n _ { F } > 3 m$ , then there exists a base point $P _ { j } ^ { ( 1 ) }$ in $\mathcal { P }$ such that $m _ { P _ { j } ^ { ( 1 ) } } \geq m + 1$ .

Proof.
By Corollary 4.12.1 there exists some $j$ so that $d _ { j } ^ { ( 1 ) } \geq 1$ and the result follows from the equality $d _ { j } ^ { ( 1 ) } = m _ { P _ { j } ^ { ( 1 ) } } ( B ) - m$ . 

We also prove the following:

Lemma 4.13. Every base point $P _ { j } ^ { ( 1 ) }$ of $\mathcal { P }$ is such that $m _ { P _ { j } ^ { ( 1 ) } } ( B ) \leq \operatorname* { m i n } \{ M _ { F } + m , 3 m \}$ , where $M _ { F }$ denotes the largest multiplicity of a component of $F$ .

Proof.
If follows from the fact that $B$ has degree $3 m , d _ { j } ^ { ( 1 ) } = m _ { P _ { j } ^ { ( 1 ) } } ( B ) - m$ and $d _ { j } ^ { ( 1 ) } \leq M _ { F }$

Corollary 4.13.1. If $F$ is non-reduced and $m \le M _ { F }$ , then every base point $P _ { j } ^ { ( 1 ) }$ of $\mathcal { P }$ is such that $m _ { P _ { j } ^ { ( 1 ) } } \leq 2 M _ { F }$ .

Proposition 4.14. If $F$ is reduced, then $B$ is reduced and,

$$
\frac { 1 } { m + 1 } < l c t ( { \mathbb { P } } ^ { 2 } , B ) = \operatorname* { m i n } \left\{ l c t _ { P _ { j } ^ { ( 1 ) } } ( { \mathbb { P } } ^ { 2 } , B ) , l c t ( Y , F ) \right\} \leq l c t ( Y , F ) \leq l c t ( Y , \overline { { F } } )
$$

Proof.
We first show the equality.
We have that $l c t ( \mathbb { P } ^ { 2 } , B ) = \operatorname* { m i n } _ { P } \{ l c t _ { P } ( \mathbb { P } ^ { 2 } , B ) \}$ , where $P$ runs over the singular points of $B$ . But any singular point of $B$ is either a base point of $\mathcal { P }$ of it is not a base point and hence it must satisfy $l c t _ { P } ( \mathbb { P } ^ { 2 } , B ) = l c t _ { P } ( Y , { \overline { { F } } } )$ . Moreover, $l c t _ { P } ( Y , { \overline { { F } } } ) = l c t ( Y , F )$ , because either $F ^ { \prime }$ is of type $I I , I I I$ or $I V$ and $F ^ { \prime }$ contains a unique singular point, namely (the strict transform of) $P$ ; or $F$ is of type $I _ { n } , 1 \leq n \leq 9$ and every singular point of $F ^ { \prime }$ is an ordinary node and we have that $l c t _ { P } ( Y , { \overline { { F } } } ) = l c t ( Y , F ) = 1$ .

Now, because $F ^ { \prime }$ is reduced we have

$$
\frac { 1 } { m + 1 } \leq \frac { 1 } { 2 } < l c t ( { \cal Y } , { \cal F } )
$$

On the other hand, for any $j$ we can find some $i$ so that

$$
l c t _ { P _ { j } ^ { ( 1 ) } } ( \mathbb { P } ^ { 2 } , B ) = \frac { 1 + b ^ { ( i ) } } { c _ { j } ^ { ( i ) } } = \frac { 1 + i } { c _ { j } ^ { ( i ) } } \geq \frac { 1 + i } { i \cdot m + 1 } > \frac { 1 } { m + 1 }
$$

where we have used Equation (5) together with the fact that each $d _ { j } ^ { ( i ) }$ satisfies $d _ { j } ^ { ( i ) } \leq 1$ . More precisely,

$$
c _ { j } ^ { ( i ) } = m _ { P _ { j } ^ { ( 1 ) } } + \ldots + m _ { P _ { j } ^ { ( i ) } } = i \cdot m + d _ { j } ^ { ( i ) } \leq i \cdot m + 1
$$

Finally, it is clear that (see e.g. [30, Theorem 8.20]) $l c t ( Y , F ) \leq l c t ( Y , { \overline { { F } } } )$ because

$$
F = \overline { { F } } + \sum _ { i , j } d _ { j } ^ { ( i ) } E _ { j } ^ { ( i ) }
$$

Proposition 4.15. If $m > 1$ and $F ^ { \prime }$ is reduced, then $l c t ( \mathbb { P } ^ { 2 } , B ) > \frac { 1 } { m }$

Proof.
It follows from the proof of Proposition 4.14 by observing that $l c t ( Y , F ) > \frac { 1 } { 2 } \geq \frac { 1 } { m }$ and

$$
\frac { 1 + i } { i \cdot m + 1 } > \frac { 1 } { m }
$$

Proposition 4.16. If $F$ is non-reduced and $m ~ \leq ~ M _ { F }$ , where $M _ { F }$ denotes the largest multiplicity of a component of $F$ , then

$$
l c t ( Y , F ) \leq l c t ( \mathbb { P } ^ { 2 } , B ) \leq l c t ( Y , \overline { { F } } )
$$

Proof.
If $F$ is non-reduced, then $\pi : Y \to \mathbb { P } ^ { 2 }$ is a log resolution of the pair $( \mathbb { P } ^ { 2 } , B )$ (see Definition 2.2). It follows from Lemma 2.6 that

$$
l c t ( \mathbb { P } ^ { 2 } , B ) = \operatorname* { m i n } _ { i , j } \left\{ \frac { 1 + b _ { j } ^ { ( i ) } } { c _ { j } ^ { ( i ) } } , \frac { 1 } { M _ { B } } \right\} \leq \frac { 1 } { M _ { B } } = l c t ( Y , \overline { { F } } )
$$

where $M _ { B }$ denotes the largest multiplicity of a component of $B$ .

If $l c t ( \mathbb { P } ^ { 2 } , B ) = 1 / M _ { B }$ there is nothing to prove, since $M _ { B } \le M _ { F }$ and $l c t ( Y , F ) = 1 / M _ { F }$ Thus, assume there exists some $i$ and some $j$ such that

$$
l c t ( \mathbb { P } ^ { 2 } , B ) = \frac { 1 + b _ { j } ^ { ( i ) } } { c _ { j } ^ { ( i ) } } < \frac { 1 } { M _ { F } } \le \frac { 1 } { M _ { B } }
$$

If $i = 1$ , then

$$
\frac { 1 + b _ { j } ^ { ( i ) } } { c _ { j } ^ { ( i ) } } = \frac { 2 } { m _ { P _ { j } ^ { ( 1 ) } } } < \frac { 1 } { M _ { F } } \Longleftrightarrow m _ { P _ { j } ^ { ( 1 ) } } > 2 M _ { F }
$$

which contradicts Corollary 4.13.1.

Similarly, if $i = 2$ , then

$$
\frac { 1 + b _ { j } ^ { ( i ) } } { c _ { j } ^ { ( i ) } } = \frac { 3 } { m _ { P _ { j } ^ { ( 1 ) } } + m _ { P _ { j } ^ { ( 2 ) } } } < \frac { 1 } { M _ { F } } \Longleftrightarrow m _ { P _ { j } ^ { ( 1 ) } } + m _ { P _ { j } ^ { ( 2 ) } } > 3 M _ { F }
$$

but $m _ { P _ { j } ^ { ( 1 ) } } + m _ { P _ { j } ^ { ( 2 ) } } = d _ { j } ^ { ( 2 ) } + 2 m \leq M _ { F } + 2 m \leq 3 M _ { F }$

Otherwise, using Equation 5, we can write $c _ { j } ^ { ( i ) } = d _ { j } ^ { ( i ) } + i \cdot m$ . Then,

$$
\begin{array} { r c l } { { \displaystyle \frac { 1 + b _ { j } ^ { ( i ) } } { c _ { j } ^ { ( i ) } } = \frac { 1 + b _ { j } ^ { ( i ) } } { d _ { j } ^ { ( i ) } + i \cdot m } < \frac { 1 } { M _ { F } } } } & { { \Longleftrightarrow } } & { { M _ { F } ( 1 + b _ { j } ^ { ( i ) } ) < d _ { j } ^ { ( i ) } + i \cdot m } } \\ { { } } & { { \Longleftrightarrow } } & { { M _ { F } ( 1 + i ) < d _ { j } ^ { ( i ) } + i \cdot m } } \end{array}
$$

which is a contradiction because $M _ { F } \geq d _ { j } ^ { ( i ) }$ and $M _ { F } \geq m$

Remark 4.17. Note that Equation (9) in the proof of Proposition 4.16 holds for any index $m$ . In particular, if $F$ is of type $I _ { n } ^ { * } , I I ^ { * } , I I I ^ { * }$ or $I V ^ { * }$ , then we also have that (see e.g. [10])

$$
\frac { 1 } { m _ { P _ { j m a x } ^ { ( 1 ) } } } \leq l c t ( \mathbb { P } ^ { 2 } , B )
$$

where $m _ { P _ { j m a x } ^ { ( 1 ) } } \doteq \operatorname* { m a x } _ { j } m _ { P _ { j } ^ { ( 1 ) } } ( B )$

Then Propositions 4.2 and 4.3 allow us to further prove:

Proposition 4.18. For any index m we have $l c t ( Y , { \overline { { F } } } ) \leq 2 l c t ( Y , F )$ .

Proof.
By contradiction, assume $1 / M _ { B } > 2 l c t ( Y , F )$ . If $F$ does not contain a component with multiplicity $\geq 3$ , then $2 l c t ( Y , F ) \ge 1$ and we conclude $M _ { B } < 1$ , a contradiction.
If $F$ is of type $I I I ^ { * }$ or $I V ^ { * }$ , then $B$ must be reduced (i.e., $M _ { B } = 1$ ) and if $F ^ { \prime }$ is of type $I I ^ { * }$ , then we conclude $M _ { B } < 3$ , contradicting Propositions 4.2 and 4.3. 

Remark 4.19. Note that when $F ^ { \prime }$ is of type $I I ^ { * } , I I I ^ { * }$ o r $I V ^ { * }$ , then the inequality $1 / M _ { B } \le$ $2 l c t ( Y , \boldsymbol { F } )$ implies Propositions 4.2 and 4.3.

In particular, combining Propositions 4.14, 4.16 and 4.18 we obtain:

Corollary 4.19.1. For any index m we have $l c t ( \mathbb { P } ^ { 2 } , B ) \leq 2 l c t ( Y , F )$ .

5. The curve $B$ when $F$ is of type $I I ^ { * } , I I I ^ { * }$ or $I V ^ { * }$

We will now assume $m = 2$ and $\mathcal { P }$ is a Halphen pencil of index two and we will only consider fibers $F$ of type $I I ^ { * } , I I I ^ { * }$ and $I V ^ { * }$ . The results obtained in the previous sections allow us to completely characterize which sextics can and which cannot yield these types of fiber.

We adopt the same notations as in Section 4 and our strategy can be summarized as follows: given $F$ we know the number of its components $n _ { F }$ . Assuming we also know the number $n _ { B }$ of components of $B$ we can compute $k$ , the number of base points 2 in $B$ , from Equation 3, which we recall next

$$
n _ { F } = n _ { B } + 9 - k - n _ { E \backslash C }
$$

and Lemma 4.5, where $n _ { E \backslash C }$ denotes the difference between the number of components of $E$ and the number of components of $C$ .

There are exactly $k - n _ { E \backslash C }$ disjoint chains of rational curves in $F$ as in Figure 1. And, moreover, together with the strict transform of $B$ under $\pi$ these are all the components of $F ^ { \prime }$ . Thus, analyzing how the dual graph of $F ^ { \prime }$ must look like we can decide whether the components coming from $B$ and these chains could possibly yield the given fiber.

The desired configuration of rational curves imposes restrictions on how the curves $B$ and $C$ can intersect and how the components of $B$ must intersect.
Since $B$ and $C$ can only intersect at base points of $\mathcal { P }$ we can use Equation (8), which we also recall below

$$
I _ { P _ { j } ^ { ( 1 ) } } ( B , C ) = a _ { j } \cdot m
$$

The desired configuration also imposes restrictions on the multiplicities $d _ { j } ^ { ( 1 ) }$ of the components $E _ { j } ^ { ( 1 ) }$ appearing in $F ^ { \prime }$ . Recall we have (Equation (5))

$$
d _ { j } ^ { ( 1 ) } = m _ { P _ { j } ^ { ( 1 ) } } ( B ) - 2
$$

In particular, we know what $m _ { P _ { j } ^ { ( 1 ) } } ( B )$ , the multiplicity of $B$ at the base point $P _ { j } ^ { ( 1 ) }$ , must be.

Moreover, every time we consider the dual graph of $F ^ { \prime }$ we can color the components coming from $B$ in blue and in black we indicate the missing components as in Lemma 4.1. Then the possible configurations are those where the components in black are arranged in exactly $k - n _ { E \backslash C }$ disjoint chains as in Figure 1. In particular, every black node can only be connected to at most two other black nodes (Lemma 4.1).

These considerations not only give us an algorithm to decide whether a sextic $B$ can yield the desired type of fiber but they also give us an algorithm to construct all possible examples for a given type of fiber, which we do in Section 6.

# 5.1. Non-Examples.

Proposition 5.1. If $F$ is of type $I I ^ { * }$ , then $B$ does not consist of any of the following curves:

(i) a line with multiplicity 6 (ii) a line with multiplicity four and a double line (iii) a triple line, a double line and another line

Proof.
If $B = 6 L$ , where $L$ is a line, then Equation (3) implies $k = 1$ . And $\pi$ consists of blowing-up a single point $P _ { 1 }$ in $B$ nine times.
In particular, $L$ must be an inflection line of $C$ , with the flex at $P _ { 1 }$ . But then blowing-up $\mathbb { P } ^ { 2 }$ at the nine base points $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 9 ) }$ of $\mathcal { P }$ would yield a (dual) configuration of rational curves in $F$ , which is different from the (affine) Dynkin diagram ${ \tilde { E } } _ { 8 }$ , the dual graph of a fiber of type $I I ^ { * }$ .

If $B$ consists of a line with multiplicity 4 and another line with multiplicity 2 and $F$ is of type $I I ^ { * }$ , then $n _ { F } = 9 , B _ { B } = 2 , n _ { E \backslash C } = 0$ , hence $k = 2$ and the only possible picture is the following one:

![](images/25fa4db1722098f857abc2d473e4e668db30a1f71f688b402b7b57f8fd95c110.jpg)

In particular, up to relabeling, $\pi$ is the blow-up of $\mathbb { P } ^ { 2 }$ at the nine points (1) , . . . , P (8)1 , P and, moreover, the two lines do not intersect at a base point of $\mathcal { P }$ .

But $C$ must intersect each of the two lines at least once (at a base point) and $k = 2$ . So both lines must be inflection lines of $C$ . In particular, we need to blow-up each of the base points at least three times in order to separate $\mathcal { P }$ . That is, $a _ { 1 } \geq 3$ and $a _ { 2 } \geq 3$ , a contradiction.

Finally, if $B$ consists of a triple line, a double line and another line, it follows from Equation (3) that $k = 3$ and $\pi$ is the blow-up of $\mathbb { P } ^ { 2 }$ at the nine points

$$
P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( a _ { 1 } ) } , P _ { 2 } ^ { ( 1 ) } , \ldots , P _ { 2 } ^ { ( a _ { 2 } ) } , P _ { 3 } ^ { ( 1 ) } , \ldots , P _ { 3 } ^ { ( a _ { 3 } ) }
$$

If we consider the dual graph of $F ^ { \prime }$ , the picture must be one of the following:

![](images/862f4906ad60fdfba3733d4841ef328e65bba61a6950b46918bd4efc0bd3be6a.jpg)

If either the line with multiplicity three is not an inflection line of $C$ or the three lines are not concurrent at a base point, then we need to blow-up at least two points lying in the triple line and, in order to separate $\mathcal { P }$ , we need to blow-up each of these points at least twice.
This means that in $F ^ { \prime }$ we would have at least two disjoint chains connected to the blue component of multiplicity 3, where each chain has length $\geq 1$ , excluding both pictures.

Thus, the only possibility is for the line with multiplicity three to be an inflection line of $C$ and for the three lines to be concurrent at a base point, which excludes the second picture.
It is routine to check that this case does not yield the first picture either.

Proposition 5.2. If $F ^ { \prime }$ is of type $I I I ^ { * }$ , then $B$ does not consist of a double line and a (rational) quartic.

Proof.
By contradiction, assume $B = 2 L + Q$ , where $L$ is a line and $Q$ is a rational quartic.
Then from Equation (3) and Lemma 4.5 we know that either $k = 3$ ( $n _ { E \backslash C } = 0$ ) or $k = 2$ ( $n _ { E \backslash C } = 1$ ). In any case, considering the dual graph of $F ^ { \prime }$ , we conclude the picture must be the following one:

![](images/7d872d908d4a2243dae63c21eba879c00f2d97ff744cdce0af61b43840d80766.jpg)

Thus, up to relabeling, we have that $Q \cap L = \{ P _ { 1 } ^ { ( 1 ) } \}$ and we also have that either $a _ { 1 } = 7$ and $a _ { 2 } = a _ { 3 } = 1$ ( $k = 3$ ) or $a _ { 1 } = 7$ and $a _ { 2 } = 2$ ( $k = 2$ ). Moreover, if the former holds then $d _ { 1 } ^ { ( 7 ) } = d _ { 2 } ^ { ( 1 ) } = d _ { 3 } ^ { ( 1 ) } = 0$ and if the latter holds, then $d _ { 1 } ^ { ( 7 ) } = d _ { 2 } ^ { ( 1 ) } = d _ { 2 } ^ { ( 2 ) } = 0$ .

In any case we know from Equation (8) that we must have

$$
I _ { P _ { 1 } ^ { ( 1 ) } } ( B , C ) = a _ { 1 } \cdot m = 1 4
$$

and since $I _ { P _ { 1 } ^ { ( 1 ) } } ( B , C ) = I _ { P _ { 1 } ^ { ( 1 ) } } ( Q , C ) + 2 I _ { P _ { 1 } ^ { ( 1 ) } } ( L , C )$ , it follows that if $k = 3$ , then either

• $I _ { P _ { 1 } ^ { ( 1 ) } } ( Q , C ) = 1 2$ and $I _ { P _ { 1 } ^ { ( 1 ) } } ( L , C ) = 1$ o r $\bullet$ $I _ { P _ { 1 } ^ { ( 1 ) } } ( Q , C ) = 1 0$ and $I _ { P _ { 1 } ^ { ( 1 ) } } ( L , C ) = 2$ or

The conclusion is that $Q$ must be singular at $P _ { 1 } ^ { ( 1 ) }$ because $Q$ must be rational and any other base point lying in $Q$ must be an ordinary double point.
Note that there is only one chain of exceptional curves intersecting the reduced component in blue.

But if $Q$ is singular at $P _ { 1 } ^ { ( 1 ) }$ , then $m _ { P _ { 1 } ^ { ( 1 ) } } ( B ) > 3$ , hence $d _ { 1 } ^ { ( 1 ) } > 1$ . From the picture, this further implies we have $d _ { 1 } ^ { ( 1 ) } = 2$ and $E _ { 1 } ^ { ( 1 ) }$ meets the strict transform of $Q$ under . The only possibility then is for $E _ { 1 } ^ { ( 6 ) }$ to appear with multiplicity one in $F ^ { \prime }$ and we must have $E _ { 1 } ^ { ( 6 ) } \cdot E _ { 1 } ^ { ( 7 ) } = 2$ . But the two curves meet transversally at a single point.

Finally, if $k = 2$ then there are no other base points lying in neither $Q$ nor $L$ (besides $P _ { 1 } ^ { ( 1 ) }$ ). Thus, the intersection multiplicity of $Q$ (resp.
$L$ ) and $C$ at $P _ { 1 } ^ { ( 1 ) }$ is twelve (resp.
three).
But then

$$
I _ { P _ { 1 } ^ { ( 1 ) } } ( B , C ) = I _ { P _ { 1 } ^ { ( 1 ) } } ( Q , C ) + 2 I _ { P _ { 1 } ^ { ( 1 ) } } ( L , C ) = 1 8
$$

contradicting Equation 10.

Proposition 5.3. If $F ^ { \prime }$ is of type $I I I ^ { * }$ , then $B$ does not consist of a double line and two conics.

Proof.
By contradiction, assume $B = Q _ { 1 } + Q _ { 2 } + 2 L$ , where the $Q _ { i }$ are conics and $L$ is a line.
Then from Equation (3) and Lemma 4.5 we know that either $k = 4$ ( $n _ { E \backslash C } = 0$ ) or $k = 3$ ( $n _ { E \backslash C } = 1$ ). In any case the picture of the dual graph of $F$ must be:

![](images/2dbe68df2635ab489d08f452eb734ba08e08184156dab58877736ac219d2fec1.jpg)

Thus, up to relabeling , all the curves $Q _ { 1 } , Q _ { 2 }$ and $L$ must intersect at the base point $P _ { 1 } ^ { ( 1 ) }$ and we have that $\boldsymbol { L } \cap \boldsymbol { Q } _ { 1 } = \boldsymbol { L } \cap \boldsymbol { Q } _ { 2 } = \{ P _ { 1 } ^ { ( 1 ) } \}$ that is, $L$ is tangent to both $Q _ { 1 }$ and $Q _ { 2 }$ at $P _ { 1 } ^ { ( 1 ) }$ so Q1 and Q2 must be tangent at P (1)1 .

It is routine to check that blowing-up $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 6 ) }$ does not yield the desired chain of exceptional curves.
Therefore, we do not obtain a fiber of type $I I I ^ { * }$ .

Proposition 5.4. If $F ^ { \prime }$ is of type $I I I ^ { * }$ , then $B$ does not consist of a double conic and a double line.

Proof.
By contradiction, assume $B = 2 Q + 2 L$ , where $Q$ is a conic and $L$ is a line.
Then from Equation (3) and Lemma 4.5 we know that either $k = 3$ ( $n _ { E \backslash C } = 0$ ) or $k = 2$ ( $n _ { E \backslash C } = 1$ ). In any case the picture of the dual graph of $F$ must be the following one:

![](images/42b54852238f4ba57cd4351665b88879acd256f77f7c19d295ca789476c0e478.jpg)

Thus, up to relabeling we have $d _ { 1 } ^ { ( 1 ) } \geq 1$ and $d _ { 2 } ^ { ( 1 ) } \geq 1$ . Since $k = 2$ would imply $a _ { 1 } = 6$ and $a _ { 2 } = 3$ we see that we must have $k = 3$ and $a _ { 1 } = 6 , a _ { 2 } = 2 , a _ { 3 } = 1$ . Moreover, $L$ must be tangent to $Q$ at $P _ { 1 } ^ { ( 1 ) }$ . Otherwise, $E _ { 1 } ^ { ( 1 ) }$ would appear with multiplicity 2 in $F$ , but the picture tells us such curve appears with multiplicity 3 since $d _ { 1 } ^ { ( 1 ) } = m _ { P _ { 1 } ^ { ( 1 ) } } ( B ) - 2 \ge 2$ .

It is routine to check that blowing-up P (1)1 , . . . , P (6)1 does not yield the desired chain of exceptional curves.
Thus, we do not obtain a fiber of type $I I I ^ { * }$ . 

Proposition 5.5. If $F ^ { \prime }$ is of type $I I I ^ { * }$ , then $B$ does not consist of a double conic and two lines.

Proof.
By contradiction, assume $B = 2 Q + L _ { 1 } + L _ { 2 }$ , where $Q$ is a conic and each $L _ { i }$ is a line.
Then from Equation (3) and Lemma 4.5 we know that either $k = 4$ ( $n _ { E \backslash C } = 0$ ) or $k = 3$ ( $n _ { E \backslash C } = 1$ ). In any case, considering the dual graph of $F ^ { \prime }$ , the picture must be:

![](images/8817527312f68214120089198605dd886ad65fd09728786090e1f68b566660cc.jpg)

Therefore, up to relabeling, we have that either $a _ { 1 } = 6$ and $a _ { 2 } = a _ { 3 } = a _ { 4 } = 1$ ( $k = 4$ ) or $a _ { 1 } = 6 , a _ { 2 } = 2$ and $a _ { 3 } = 1$ ( $k = 3$ ). If the former holds, then $d _ { 2 } ^ { ( 1 ) } = d _ { 3 } ^ { ( 1 ) } = d _ { 4 } ^ { ( 1 ) } = 0$ and if the latter holds, then $d _ { 2 } ^ { ( 1 ) } = d _ { 2 } ^ { ( 2 ) } = d _ { 3 } ^ { ( 1 ) } = 0$ . But then, in any case, we must have that both $Q \cap L _ { 1 } = \{ P _ { 1 } ^ { ( 1 ) } \}$ and $Q \cap L _ { 2 } = \{ P _ { 1 } ^ { ( 1 ) } \}$ . That is, $L _ { 1 }$ and $L _ { \mathrm { 2 } }$ are both tangent lines to $Q$ a t $P _ { 1 } ^ { ( 1 ) }$ , which is an absurd.


Proposition 5.6. If $F$ is of type $I I I ^ { * }$ , then $B$ does not consist of two double lines and a conic.

Proof.
By contradiction, assume $B = 2 L _ { 1 } + 2 L _ { 2 } + Q$ , where each $L _ { i }$ is a line and $Q$ is a conic.
Then from Equation (3) and Lemma 4.5 we know that either $k = 4$ ( $n _ { E \backslash C } = 0$ ) or $k = 3$ ( $n _ { E \backslash C } = 1$ ). In both cases the picture of the dual graph of $F ^ { \prime }$ must be one of the following:

![](images/d31e66bdb77c337d8ad52712e14caf40752e6220d0a1a6a29fd23576fdf646a1.jpg)

If we hhave that $L _ { 1 } \cap L _ { 2 } = \{ P _ { 1 } ^ { ( 1 ) } \}$ g, $P _ { 1 } ^ { ( 1 ) } \notin Q$ (from the left to the right), then, up to relabeling, we and we know from Equation (8) that the intersection multiplicity of $B$ and $C$ at $P _ { 1 } ^ { ( 1 ) }$ is equal to

$$
I _ { P _ { 1 } ^ { ( 1 ) } } ( B , C ) = 2 I _ { P _ { 1 } ^ { ( 1 ) } } ( L _ { 1 } , C ) + 2 I _ { P _ { 1 } ^ { ( 1 ) } } ( L _ { 2 } , C ) = a _ { 1 } \cdot m = 1 2
$$

Thus, it must be the case that $I _ { P _ { 1 } ^ { ( 1 ) } } ( L _ { 1 } , C ) = I _ { P _ { 1 } ^ { ( 1 ) } } ( L _ { 2 } , C ) = 3$ . That is, both $L _ { 1 }$ and $L _ { 2 }$ are inflection lines of $C$ at $P _ { 1 } ^ { ( 1 ) }$ , which is an absurd.

Now, if we have the second configuration, then up to relabeling, $L _ { 1 } \cap L _ { 2 } = \{ P _ { 1 } ^ { ( 1 ) } \}$ , we have $P _ { 1 } ^ { ( 1 ) } \in Q$ and there are at most two base points lying in $Q$ . Thus, one of the lines, say $L _ { 1 }$ , must be tangent to $Q$ at $P _ { 1 } ^ { ( 1 ) }$ and since both lines cannot be tangent to $Q$ at $P _ { 1 } ^ { ( 1 ) }$ we must have $P _ { 2 } ^ { ( 1 ) } \in Q$ , $I _ { P _ { 2 } ^ { ( 1 ) } } ( Q , C ) = 2$ and $I _ { P _ { 1 } ^ { ( 1 ) } } ( Q , C ) = 4$ .

Now, Equation (8) gives the intersection multiplicity of $B$ and $C$ at $P _ { 1 } ^ { ( 1 ) }$ is equal to

$$
I _ { P _ { 1 } ^ { ( 1 ) } } ( B , C ) = I _ { P _ { 1 } ^ { ( 1 ) } } ( Q , C ) + 2 I _ { P _ { 1 } ^ { ( 1 ) } } ( L _ { 1 } , C ) + 2 I _ { P _ { 1 } ^ { ( 1 ) } } ( L _ { 2 } , C ) = a _ { 1 } \cdot m = 1 2
$$

and it follows that $I _ { P _ { 1 } ^ { ( 1 ) } } ( L _ { 1 } , C ) = 3$ and $I _ { P _ { 1 } ^ { ( 1 ) } } ( L _ { 2 } , C ) = 1$ , since $L _ { 2 }$ cannot be tangent to $C$ at $P _ { 1 } ^ { ( 1 ) }$ 1 1. It is routine to check that blowing-up $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 5 ) }$ does not yield the desired chain of exceptional curves.

Proposition 5.7. If $F$ is of type $I I I ^ { * }$ , then $B$ does not consist of three double lines.

Proof.
By contradiction, assume $B = 2 L _ { 1 } + 2 L _ { 2 } + 2 L _ { 3 }$ , where each $L _ { i }$ is a line.
The picture of the dual graph of $F$ can only be:

![](images/354ea9de8230fc534c0fdc804041c3769108fd80af136595549b437b842c5c5e.jpg)

Thus, the three lines $L _ { 1 } , L _ { 2 }$ and $L _ { 3 }$ must be concurrent at the base point $P _ { 1 } ^ { ( 1 ) }$ . But if that is the case, then $E _ { 1 } ^ { ( 1 ) }$ would appear with multiplicity 4 in $F$ .

Proposition 5.8. If $F$ is of type $I I I ^ { * }$ , then $B$ does not consist of two double lines and two other lines.

Proof.
By contradiction, assume $B = 2 L _ { 1 } + 2 L _ { 2 } + L _ { 3 } + L _ { 4 }$ , where each $L _ { i }$ is a line.
If we consider the dual graph of $F$ , the picture is the following one:

![](images/8bcc826ce8ad0ee0065b3e711a03242cdcdbcd0cc6a862eb8c6d39807b2e84f9.jpg)

In particular, up to relabeling, the two double lines together with one of the other lines, say $L _ { 3 }$ , must be concurrent at the point $P _ { 1 } ^ { ( 1 ) }$ and, further, $C$ must be smooth at $P _ { 1 } ^ { ( 1 ) }$ , since $d _ { 1 } ^ { ( 1 ) } > 0$ (see Lemma 4.7).

In particular, Equation (8) gives us

$$
I _ { P _ { 1 } ^ { ( 1 ) } } ( B , C ) = a _ { 1 } \cdot m = 1 0
$$

where $I _ { P _ { 1 } ^ { ( 1 ) } } ( B , C )$ denotes the intersection multiplicity of $B$ and $C$ at the point $P _ { 1 } ^ { ( 1 ) }$ , but

$$
I _ { P _ { 1 } ^ { ( 1 ) } } ( B , C ) = 2 I _ { P _ { 1 } ^ { ( 1 ) } } ( L _ { 1 } , C ) + 2 I _ { P _ { 1 } ^ { ( 1 ) } } ( L _ { 2 } , C ) + I _ { P _ { 1 } ^ { ( 1 ) } } ( L _ { 3 } , C ) \leq 2 \cdot 3 + 1 + 1 = 8
$$

contradicting Equation 11.

Proposition 5.9. If $F$ is of type $I I I ^ { * }$ , then $B$ does not consist of a line with multiplicity four and a double line.

Proof.
By contradiction, assume $B = 4 L + 2 L ^ { \prime }$ , where $L$ and $L ^ { \prime }$ are two distinct lines.
It follows from Equation (3) and Lemma 4.5 that either $k = 3$ ( $n _ { E \backslash C } = 0$ ) or $k = 2$ ( $n _ { E \backslash C } = 1$ ). Thus, if we look at the dual graph of $F ^ { \prime }$ , the picture is:

![](images/79c6c22cd5869d60ee4d9b6bce709b61769ab9f731adb34c2ba6785d74db1705.jpg)

and twe have o not and base point of . So that the e $\mathcal { P }$ . In ality abeling, implies $P _ { 1 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 1 ) } \in L$ $P _ { 1 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 1 ) } \notin L ^ { \prime }$ $d _ { j } ^ { ( 1 ) } = m _ { P _ { j } ^ { ( 1 ) } } ( B ) - 2$ both $E _ { 1 } ^ { ( 1 ) }$ and $E _ { 2 } ^ { ( 1 ) }$ appear with multiplicity 2 in $F$ , a contradiction.

Lemma 5.10. Let $C : c = 0$ be a smooth cubic.
Let $P \in C$ be a flex point and let $L : l = 0$ be the corresponding inflection line.
If $Q : q = 0$ is a quartic such that $I _ { P } ( Q , L ) = 3$ , then

$$
q = l c ^ { \prime } - l ^ { \prime } c
$$

where $c ^ { \prime }$ has degree three and $P$ does not lie in the line $l ^ { \prime } = 0$ .

Proof.
We can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $C$ is the cubic $y ^ { 2 } z - x ( x - z ) ( x - \alpha \cdot z ) = 0$ for some $a \in \mathbb { C } \backslash \{ 0 , 1 \}$ . Then we can assume $P$ is the point $( 0 : 1 : 0 )$ and $L$ is the line $z = 0$ .

Since $I _ { P } ( Q , L ) = 3$ we have that $q ( x , y , 0 ) = \alpha x ^ { 4 } + \beta x ^ { 3 } y$ for some $\alpha , \beta \in \mathbb { C }$ with $\beta \neq 0$ .

Letting $q ^ { \prime } ( x , y , z )$ be the polynomial

$$
q + ( \alpha x + \beta y + \gamma z ) ( y ^ { 2 } z - x ( x - z ) ( x - a \cdot z ) )
$$

it follows that $q ^ { \prime } ( x , y , 0 ) = 0$ .

Thus, there exists $c ^ { \prime }$ a polynomial of degree three such that $q ^ { \prime } = l c ^ { \prime }$ . Letting $l ^ { \prime }$ be the line $\alpha x + \beta y + \gamma z = 0$ it follows that

$$
q = l c ^ { \prime } - l ^ { \prime } c
$$

and $p$ is not a point in the line $l ^ { \prime } = 0$ , since $\beta \neq 0$ .

Corollary 5.10.1. Let $Q , C , L$ and $P$ be as in Lemma 5.10. If $I _ { P } ( Q , C ) = 6$ , then

$$
c ^ { \prime } = l q ^ { \prime \prime } - c
$$

where $q ^ { \prime \prime }$ has degree two and does not vanish on $P$ .

Proof.
Since we can write $q = l c ^ { \prime } - l ^ { \prime } c$ , the condition $I _ { P } ( Q , C ) = 6$ implies $I _ { p } ( C ^ { \prime } , C ) = 3$ , where $C ^ { \prime }$ is the cubic $c ^ { \prime } = 0$ . Thus, $c ^ { \prime } ( x , y , 0 ) = \alpha x ^ { 3 }$ for some $\alpha \neq 0$ and, up to a change of coordinates we can assume $\alpha = 1$ . Letting $c ^ { \prime \prime }$ be the polynomial $c ^ { \prime } + c$ , it follows that $c ^ { \prime \prime } ( x , y , 0 ) = 0$ . And we conclude there exists $q ^ { \prime \prime }$ a polynomial of degree two such that $c ^ { \prime \prime } = l q ^ { \prime \prime }$ . By assumption, such polynomial cannot vanish on $P$ . 

Combining Lemma 5.10 and Corollary 5.10.1 we obtain:

Corollary 5.10.2. Let $Q , C , L$ and $P$ be as in Lemma 5.10. If $I _ { P } ( Q , C ) = 6$ , then

$$
q = l ^ { 2 } q ^ { \prime \prime } - ( l ^ { \prime } + l ) c
$$

Corollary 5.10.3. Let $C , L$ and $P$ be as in Lemma 5.10. The space of quartics $Q$ such that $I _ { P } ( Q , L ) = 3$ and $I _ { P } ( Q , C ) = 6$ has dimension eight.

Proof.
It follows from the proofs of Lemma 5.10 and Corollary 5.10.1 (or Corollary 5.10.3). The quartic $Q$ is determined by 9 coefficients (the coefficients of $q ^ { \prime \prime }$ and the coefficients of $l ^ { \prime }$ ) . 

Lemma 5.11. Let $C : c = 0$ be a smooth cubic.
Let $P \in C$ be a flex point and let $L : l = 0$ be the corresponding inflection line.
Choose three distinct points in $C$ , say $P _ { 1 } , P _ { 2 } , P _ { 3 }$ different from $p$ . There does not exist a quartic $Q$ with nodes at $P _ { 1 } , P _ { 2 } , P _ { 3 }$ and such that $I _ { P } ( Q , L ) = 3$ and $I _ { P } ( Q , C ) = 6$ .

Proof.
By Corollary 5.10.3, the space of quartics $Q$ satisfying the conditions $I _ { P } ( Q , L ) = 3$ and $I _ { P } ( Q , C ) = 6$ has dimension eight.
Asking for $Q$ to have nodes at three points imposes nine more conditions.
Alternatively, one can check that a quartic with equation in the form of Corollary 5.10.2 does not have three nodes.


Proposition 5.12. If $F ^ { \prime }$ is of type $I V ^ { * }$ , then $B$ does not consist of a double line and a rational quartic.

Proof.
If $B$ consists of a double line and a rational quartic and $F$ is of type $I V ^ { * }$ , then the picture of the dual graph of $F$ is one of the following:

![](images/680a6826ba5f6b699d3af811337fefdd8b1d67c09ef7d1faebf364c07a05a39f.jpg)

In any case one can deduce the rational quartic must have three nodes from how the curves $B$ and $C$ must intersect.

In the first picture (from the left to the right ), we can show that the quartic must intersect $C$ at a flex point with multiplicity 6 and the corresponding inflection line (of $C$ ) must intersect the quartic at the flex with multiplicity three; and at a fourth point which is not in $C$ . Thus, all the missing base points must lie in the quartic, but not in the line.
Since the quartic is reduced these points must be ordinary double points.
In particular, up to relabeling, $a _ { 1 } = 6 , a _ { 2 } = a _ { 3 } = a _ { 4 } = 1$ .

Similarly, in the second picture the quartic must intersect $C$ at a flex point with multiplicity 4 and the corresponding inflection line (of $C$ ) must intersect the quartic at the flex with multiplicity three; and at a fourth point where the quartic is tangent to $C$ with multiplicity two.
Again, we conclude the missing base points must be ordinary double points.
But then, up to relabeling, we would have $a _ { 1 } = 5 , a _ { 2 } = 2 , a _ { 3 } = a _ { 4 } = a _ { 5 } = 1$ , contradicting the fact that $\sum a _ { i } = 9$ .

Thus, the only possible picture is the first one.
Since Equation (3) tells us $C$ must be smooth, the result follows from Lemma 5.11. 

Proposition 5.13. If $F$ is of type $I V ^ { * }$ , then $B$ does not consist of three double lines.

Proof.
If $B$ consists of three double lines and $F ^ { \prime }$ is of type $I V ^ { * }$ , then the picture of the dual graph of $F ^ { \prime }$ is the following one:

![](images/f68e685cc142406956b6aaf28aadec23dbbf10fb7f830affbe814402decb88c0.jpg)

Thus, up to relabeling, the three lines must be concurrent at the base point $P _ { 1 } ^ { ( 1 ) }$ . But then $d _ { 1 } ^ { ( 1 ) } = m _ { P _ { 1 } ^ { ( 1 ) } } ( B ) - 2 = 4$ and $E _ { 1 } ^ { ( 1 ) }$ appears with multiplicity four in $F ^ { \prime }$ , which is an absurd.


Proposition 5.14. If $F ^ { \prime }$ is of type $I V ^ { * }$ , then $B$ does not consist of a double conic and a double line.

Proof.
If $B$ consists of a double conic and a double line and $F ^ { \prime }$ is of type $I V ^ { * }$ , it follows from Equation (3) and Lemma 4.5 that either $k = 4 \left( n _ { E \backslash C } = 0 \right)$ , or $k = 3 \left( n _ { E \backslash C } = 1 \right)$ ), or $k = 2 \left( n _ { E \backslash C } = 2 \right)$ . Since the picture of the dual graph of $F$ can only be the following one:

![](images/ed578c149e4bf348ddc8a28f31493a14af2e68d6074af0c7dbaeffdd42f6e89b.jpg)

we must have $k = 4$ and, up to relabeling, $a _ { 1 } = 4 , a _ { 2 } = 2 , a _ { 3 } = 2$ and $a _ { 4 } = 1$ . Moreover, since the two blue components do not intersect, any intersection point between the line and the conic must be a base point of $\mathcal { P }$ . But then for at least some $j = 1 , \dots , 4$ we must have $d _ { j } ^ { ( 1 ) } = m _ { P _ { j } ^ { ( 1 ) } } ( B ) - 2 = 2$ , which implies $E _ { j } ^ { ( 1 ) }$ must appear with multiplicity 2 in $F ^ { \prime }$ . Thus, we cannot possibly obtain the desired type of fiber.

5.2. All possible examples.
At last we can completely characterize the curve $B$ whenever $F ^ { \prime }$ is of type $I I ^ { * } , I I I ^ { * }$ o r $I V ^ { * }$ .

When $F ^ { \prime }$ is of type $I I ^ { * }$ the characterization is as follows:

Theorem 5.15. If $F ^ { \prime }$ is of type $I I ^ { * }$ , then the sextic $B$ consists of one of the following (non-reduced) curves:

(i) a triple conic (Example 7.55)\
(ii) a nodal cubic and an inflection line, with the line taken with multiplicity three (Example 7.57)\
(iii) two triples lines (Example 7.56)\
(iv) a conic and a tangent line, with the line taken with multiplicity four (Example 7.58)\
(v) a line with multiplicity five and another line (Example 7.59)

Proof.
A fiber of type $I I ^ { * }$ has exactly two components with multiplicity three, two components with multiplicity two and only one component with multiplicity one.
Thus, combining Propositions 4.2, 4.3 and 5.1 we conclude the only possibilities for $B$ are the ones listed above.

If $B$ consists of a nodal cubic and a triple line, then the line must be an inflection line of the cubic because of the following reasoning.
From Equation (3) we know that $k = 2$ so we need to blow-up exactly two points in $B$ . But all the components of $F$ are supported in smooth curves so we also know that we have to blow-up the node.
That is, the node is a base point.
But then the second base point must lie in both the triple line and the cubic and that must be their only intersection point.

Similarly, in case $( i v )$ we can deduce how the components of $B$ must intersect from Equations (3) and (8), the dual graph of $F$ and Lemma 4.1. 

When $F$ is of type $I I I ^ { * }$ we obtain the following description for the curve $B$ :

Theorem 5.16. If $F ^ { \prime }$ is of type $I I I ^ { * }$ , then $B$ consists of one of the following curves:

(i) a double line, a cubic and another line (Example 7.45) (ii) a double conic and another conic (Example 7.46) (iii) a triple conic (Example 7.47) (iv) two triple lines (Example 7.48) (v) a triple line, a double line and another line (Examples 7.49 and 7.50 ) (vi) a triple line, a conic and a line (Example 7.51) (vii) a triple line and a cubic (Example 7.52) (viii) a conic and a line, with the line taken with multiplicity four (Example 7.53) (ix) a line with multiplicity four and two other lines (Example 7.54)

Proof.
It follows from Propositions 4.2 and 5.2 through 5.9.

Finally, when $F ^ { \prime }$ is of type $I V ^ { * }$ the description for the curve $B$ is as follows:

Theorem 5.17. If $F ^ { \prime }$ is of type $I V ^ { * }$ , then $B$ consists of one of the following curves:

(i) a double conic and a conic (Example 7.33) (ii) a double line, a conic and two lines (Example 7.34) (iii) a double line, a cubic and a line (Example 7.35) (iv) a double line and two conics (Example 7.36) (v) two double lines and two lines (Example 7.37) (vi) two double lines and a conic (Example 7.38) (vii) a double conic and two lines (Example 7.39) (viii) a triple conic (Example 7.40) (ix) a triple line, a conic and a line (Example 7.41) (x) a triple line, a double line and another line (Example 7.42) (xi) a triple line and three lines (Example 7.43) (xii) a triple line and a cubic (Example 7.44)

Proof.
Combining Propositions 4.2, 5.12,5.13 and 5.14we conclude the only possibilities for $B$ are the ones listed above.

In Sections 6 and 7 we show the converse statements of Theorems 5.15, 5.16 and 5.17 also hold.
More precisely, we explicitly construct Halphen pencils of index two, $\lambda B + \mu ( 2 C ) = 0$ , where $B$ is one of the possible curves we have listed and the corresponding (non-multiple) fiber is of type $I I ^ { * } , I I I ^ { * }$ o r $I V ^ { * }$ .

# 6. Constructions of Halphen Pencils of index two

Following the algorithm outlined in the previous section, for each of the types of singular fibers that occur (see Proposition 3.5) we can construct explicit examples of a rational elliptic surface $f : Y \to \mathbb { P } ^ { 1 }$ of index $m = 2$ having that type of singular fiber.
In view of Proposition 3.2, these are obtained by explicitly constructing the corresponding Halphen pencils $\mathcal { P }$ .

We use the same notations as in Section 4. In particular $\mathcal { P }$ is the pencil3 $\lambda B + \mu ( 2 C ) = 0$ , where $C$ is the unique cubic through the nine base points and $B$ corresponds to a (nonmultiple) singular fiber $F ^ { \prime }$ of $f$ having the desired Kodaira type.
We further assume $C$ is smooth at a base point and use an additive notation when referring to both the components of a curve in the pencil $\mathcal { P }$ and the components of the corresponding fiber.

All the information we need to completely characterize $\mathcal { P }$ , hence $Y$ , can be encoded into some numerical data that we describe next.

From Proposition 3.2 we know that we obtain the rational elliptic surface $Y$ from $\mathcal { P }$ by blowing-up $\mathbb { P } ^ { 2 }$ at its nine base points $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( a _ { 1 } ) } , \ldots , P _ { k } ^ { ( 1 ) } , \ldots , P _ { k } ^ { ( a _ { k } ) }$ . We call the $k -$ uple $( a _ { 1 } , \ldots , a _ { k } )$ the characteristic sequence of $Y$ (and/or $\mathcal { P }$ ), where the choice of name is borrowed from [32].

Now, the curve $B$ has $n _ { B }$ components, where $n _ { B }$ satisfies Equation (3), and since each of these components appears with a certain multiplicity, we can associate to it a multiplicity sequence $( m _ { 1 } - d _ { 1 } , \dots , m _ { n _ { B } } - d _ { n _ { B } } )$ . And we simply mean that we can write

$$
B = m _ { 1 } B _ { 1 } + . . . + m _ { n _ { B } } B _ { n _ { B } }
$$

where each $B _ { i }$ is a reduced and irreducible curve of degree $d _ { i }$ and $m _ { i }$ is its multiplicity in $B$ . For instance, if $B$ consists of a double line and two conics, then $B$ has a multiplicity sequence $( 2 - 1 , 1 - 2 , 1 - 2 )$ . It also has $( 1 - 2 , 2 - 1 , 1 - 2 )$ as a multiplicity sequence as well as $( 1 - 2 , 1 - 2 , 2 - 1 )$ . Any choice is fine.

Once we choose a multiplicity sequence it is relevant to consider the intersection multiplicity of the components of $B$ and $C$ at a base point $P _ { j } ^ { ( 1 ) }$ and record these numbers by arranging them in a matrix.

Given a Halphen pencil $\mathcal { P }$ generated by $B = m _ { 1 } B _ { 1 } + \ldots + m _ { n _ { B } } B _ { n _ { B } }$ and $2 C$ we define its intersection matrix as the $n _ { B } \times k$ matrix $A = \left( a _ { i j } \right)$ whose entries $a _ { i j }$ are given precisely by the intersection multiplicities of $m _ { i } B _ { i }$ and $C$ at the point $P _ { j } ^ { ( 1 ) }$ .

These three numerical data (the multiplicity and characteristic sequences and the intersection matrix) allows us to present all of our constructions4 in Tables 2 through 8 below.
A much more detailed geometric description of the constructions is given in the next section.

<table><tr><td rowspan=1 colspan=1>TypeofFiber</td><td rowspan=1 colspan=1>lct(P²,B)</td><td rowspan=1 colspan=1>MultiplicitySequence</td><td rowspan=1 colspan=1>Characteristic Sequence</td><td rowspan=1 colspan=1>IntersectionMatrix</td><td rowspan=1 colspan=1>Example</td></tr><tr><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>2-3</td><td rowspan=1 colspan=1>(1- 1,...,1-1)6</td><td rowspan=1 colspan=1>?</td><td rowspan=1 colspan=1>/1 000 1 10020 0 1 0 0 0 0101000010000101 01 1011００000010110</td><td rowspan=1 colspan=1>7.11</td></tr><tr><td rowspan=1 colspan=1>I8</td><td rowspan=1 colspan=1>2-3</td><td rowspan=1 colspan=1>(1 - 1.,...,1−1)6</td><td rowspan=1 colspan=1>(2,2,1,...,1)3</td><td rowspan=1 colspan=1>/1 1 ０００１１００１01002010000000 0 1 1 10200 0 010 1 1 1 0 00</td><td rowspan=1 colspan=1>7.12</td></tr><tr><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>2-3</td><td rowspan=1 colspan=1>(1-1,...,1-1)6</td><td rowspan=1 colspan=1>(2,2,2,1,1,1)</td><td rowspan=1 colspan=1>/2 0１0０１００１０0１１001010 1 1 0 1 00020010 201 00</td><td rowspan=1 colspan=1>7.13</td></tr></table>

Table 2. Examples yielding a fiber of type $I _ { 7 } , I _ { 8 }$ or $I _ { 9 }$

Table 3. Examples yielding a fiber of type $I _ { n } , n \leq 4$

<table><tr><td rowspan=1 colspan=1>TypeopeFiber</td><td rowspan=1 colspan=1>MultiplicitySequence</td><td rowspan=1 colspan=1>Characteristic Sequence</td><td rowspan=1 colspan=1>IntersectionMatrix</td><td rowspan=1 colspan=1>Example</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>(1-6)</td><td rowspan=1 colspan=1>(1,1....1)9</td><td rowspan=1 colspan=1>(2 2· 2)</td><td rowspan=1 colspan=1>7.1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>(1-3,1-3)</td><td rowspan=1 colspan=1>(,1...1)9</td><td rowspan=1 colspan=1>(&quot;i)</td><td rowspan=1 colspan=1>7.3</td></tr><tr><td rowspan=2 colspan=1>1</td><td rowspan=1 colspan=1>(1-4,1- 2)</td><td rowspan=1 colspan=1>(11..1)9</td><td rowspan=1 colspan=1>(tim i)</td><td rowspan=1 colspan=1>7.4</td></tr><tr><td rowspan=1 colspan=1>(1-5,1- 1)</td><td rowspan=1 colspan=1>(1,1,..,.1)9</td><td rowspan=1 colspan=1>(1: t)</td><td rowspan=1 colspan=1>7.5</td></tr><tr><td rowspan=3 colspan=1>1</td><td rowspan=1 colspan=1>(1−2,1- 2,1- 2)</td><td rowspan=1 colspan=1>(1,1,...,1)9</td><td rowspan=1 colspan=1>(111111000)1i000111666iiiii1</td><td rowspan=1 colspan=1>7.6</td></tr><tr><td rowspan=1 colspan=1>(1 −4,1−1,1−1)</td><td rowspan=1 colspan=1>(1,1,...,1)9</td><td rowspan=1 colspan=1>(222111111)666111660(000666iii)</td><td rowspan=1 colspan=1>7.7</td></tr><tr><td rowspan=1 colspan=1>(1-3,1- 2,1−1)</td><td rowspan=1 colspan=1>(1,1,...1)9</td><td rowspan=1 colspan=1>(211111110011111001(000000iii)</td><td rowspan=1 colspan=1>7.8</td></tr><tr><td rowspan=2 colspan=1>IA</td><td rowspan=1 colspan=1>(1-3,1- 1,1-1,1−1)</td><td rowspan=1 colspan=1>(1,1....1)g</td><td rowspan=1 colspan=1>(2111   111001100000100011000C00066ii10</td><td rowspan=1 colspan=1>7.9</td></tr><tr><td rowspan=1 colspan=1>(1-2,1- 2,1-1,1-1)</td><td rowspan=1 colspan=1>(1,1.,1)9</td><td rowspan=1 colspan=1>(111111000)111100110000001101(0000i60ii)</td><td rowspan=1 colspan=1>7.10</td></tr></table>

<table><tr><td rowspan=1 colspan=1>TypeofFiber</td><td rowspan=1 colspan=1>lct(P²,B)</td><td rowspan=1 colspan=1> Multiplicity Sequence</td><td rowspan=1 colspan=1>Characteristic Sequence</td><td rowspan=1 colspan=1>IntersectionMatrix</td><td rowspan=1 colspan=1>Example</td></tr><tr><td rowspan=1 colspan=1>I</td><td rowspan=1 colspan=1>5-6</td><td rowspan=1 colspan=1>(1-6)</td><td rowspan=1 colspan=1>(1.1)9</td><td rowspan=1 colspan=1>(2 2·· 2)</td><td rowspan=1 colspan=1>7.14</td></tr><tr><td rowspan=3 colspan=1>II</td><td rowspan=1 colspan=1>3-4</td><td rowspan=1 colspan=1>(1-3,1-3)</td><td rowspan=1 colspan=1>(1.1)9</td><td rowspan=1 colspan=1>(211111110)(011111112)</td><td rowspan=1 colspan=1>7.15</td></tr><tr><td rowspan=1 colspan=1>3-4</td><td rowspan=1 colspan=1>(1-4,1-2)</td><td rowspan=1 colspan=1>(1·1)9</td><td rowspan=1 colspan=1>(222111111)000111111)</td><td rowspan=1 colspan=1>7.16</td></tr><tr><td rowspan=1 colspan=1>3-4</td><td rowspan=1 colspan=1>(1-5,1-1)</td><td rowspan=1 colspan=1>(1,.,1)g</td><td rowspan=1 colspan=1>(222222111)(000000111)</td><td rowspan=1 colspan=1>7.17</td></tr><tr><td rowspan=3 colspan=1>IV</td><td rowspan=1 colspan=1>2-3</td><td rowspan=1 colspan=1>(1-2,1–2,1-2)</td><td rowspan=1 colspan=1>(1,...,g</td><td rowspan=1 colspan=1>(111111000)1110001110001111111</td><td rowspan=1 colspan=1>7.18</td></tr><tr><td rowspan=1 colspan=1>2-3</td><td rowspan=1 colspan=1>(1−4,1−1,1−1)</td><td rowspan=1 colspan=1>(1,.,1)g</td><td rowspan=1 colspan=1>(222111111)000111000(000000111)</td><td rowspan=1 colspan=1>7.19</td></tr><tr><td rowspan=1 colspan=1>2-3</td><td rowspan=1 colspan=1>(1-3,1-2,1-1)</td><td rowspan=1 colspan=1>(1,.1)9</td><td rowspan=1 colspan=1>(211111110)011111001(000000111)</td><td rowspan=1 colspan=1>7.20</td></tr></table>

Table 4. Examples yielding a fiber of type $I I , I I I$ or $I V$

Remark 6.1. All the examples listed in Tables 3 and 5 are such that $l c t ( \mathbb { P } ^ { 2 } , B ) = l c t ( Y , F )$

<table><tr><td rowspan=1 colspan=1>TypeofFiber</td><td rowspan=1 colspan=1>MultiplicitySequence</td><td rowspan=1 colspan=1>CharacteristicSequence</td><td rowspan=1 colspan=1>IntersectionMatrix</td><td rowspan=1 colspan=1>Example</td></tr><tr><td rowspan=4 colspan=1>1</td><td rowspan=1 colspan=1>(1−1,1−1,1−1,1−1,2−1)</td><td rowspan=1 colspan=1>(1,1,..,.1)g</td><td rowspan=1 colspan=1>/1 1100000０)100110000010101000001011 一 00000000222）</td><td rowspan=1 colspan=1>7.21</td></tr><tr><td rowspan=1 colspan=1>(2 -2,1-2)</td><td rowspan=1 colspan=1>(2,2,2,1,1,1)</td><td rowspan=1 colspan=1>(2222 22)(2 2 26 60</td><td rowspan=1 colspan=1>7.22</td></tr><tr><td rowspan=1 colspan=1>(2-1,1-2,1-2)</td><td rowspan=1 colspan=1>(2,2,1...1)5</td><td rowspan=1 colspan=1>22200002)201111010211110</td><td rowspan=1 colspan=1>7.23</td></tr><tr><td rowspan=1 colspan=1>(2 −1,1− 2,1−1,1−1)</td><td rowspan=1 colspan=1>(2,1..,1)</td><td rowspan=1 colspan=1>/222000 一 02000111100。1111000i06i1</td><td rowspan=1 colspan=1>7.25</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>(2 -2,1-2)</td><td rowspan=1 colspan=1>(2,2,3,1,1)</td><td rowspan=1 colspan=1>2422)</td><td rowspan=1 colspan=1>7.27</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>(2 - 2,1- 1,1− 1)</td><td rowspan=1 colspan=1>(1,1,3,3,1)</td><td rowspan=1 colspan=1>200244002010621)</td><td rowspan=1 colspan=1>7.28</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>(2–1,2–1,1–1,1–1)</td><td rowspan=1 colspan=1>(3,2,2,1,1)</td><td rowspan=1 colspan=1>(42000２０0202201000210</td><td rowspan=1 colspan=1>7.29</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>(2−1,2−1,1−1,1−1)</td><td rowspan=1 colspan=1>(3,3,2,1)</td><td rowspan=1 colspan=1>/2420200102300</td><td rowspan=1 colspan=1>7.30</td></tr></table>

Table 5. Examples yielding a fiber of type $I _ { n } ^ { * } , n \leq 4$

<table><tr><td rowspan=1 colspan=1>TypeofFiber</td><td rowspan=1 colspan=1>lct(P²,B)</td><td rowspan=1 colspan=1>Multiplicity Sequence</td><td rowspan=1 colspan=1>Characteristic Sequence</td><td rowspan=1 colspan=1>IntersectionMatrix</td><td rowspan=1 colspan=1>Example</td></tr><tr><td rowspan=8 colspan=1>1V*</td><td rowspan=1 colspan=1>1-2</td><td rowspan=1 colspan=1>(2 −1,2−1,1–1,1−1)</td><td rowspan=1 colspan=1>(3,2,1,1,1,1)</td><td rowspan=1 colspan=1>/220020-2200200２０00102010</td><td rowspan=1 colspan=1>7.37</td></tr><tr><td rowspan=1 colspan=1>2-5</td><td rowspan=1 colspan=1>(2 –1,2 –1,1− 2)</td><td rowspan=1 colspan=1>(2,2,3,1,1)</td><td rowspan=1 colspan=1>/202202002202220</td><td rowspan=1 colspan=1>7.38</td></tr><tr><td rowspan=1 colspan=1>3-7</td><td rowspan=1 colspan=1>(2–2,1−1,1−1)</td><td rowspan=1 colspan=1>(4,2,1,1,1)</td><td rowspan=1 colspan=1>(42222)3000012000</td><td rowspan=1 colspan=1>7.39</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3-2)</td><td rowspan=1 colspan=1>(3,3,3)</td><td rowspan=1 colspan=1>(666)</td><td rowspan=1 colspan=1>7.40</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3–1,1− 2,1-1)</td><td rowspan=1 colspan=1>(2,2,3,1,1)</td><td rowspan=1 colspan=1>/333001031 10ioi1</td><td rowspan=1 colspan=1>7.41</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3–1,2 –1,1− 1)</td><td rowspan=1 colspan=1>(3,3,1,1,1)</td><td rowspan=1 colspan=1>/36。。0²2 230000</td><td rowspan=1 colspan=1>7.42</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3−1,1−1,1−1,1−1)</td><td rowspan=1 colspan=1>(2,2,2,1,1,1)</td><td rowspan=1 colspan=1>/33300000110010 101(0oioii)</td><td rowspan=1 colspan=1>7.43</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3-1,1-3)</td><td rowspan=1 colspan=1>(3,3,2,1)</td><td rowspan=1 colspan=1>(3330)(3 31 2)</td><td rowspan=1 colspan=1>7.44</td></tr></table>

Table 6. Examples yielding a fiber of type $I V ^ { * }$

<table><tr><td rowspan=1 colspan=1>TypeofFiber</td><td rowspan=1 colspan=1>lct(P2,B)</td><td rowspan=1 colspan=1>MultiplicitySequence</td><td rowspan=1 colspan=1>CharacteristicSequence</td><td rowspan=1 colspan=1>IntersectionMatrix</td><td rowspan=1 colspan=1>Example</td></tr><tr><td rowspan=10 colspan=1>III</td><td rowspan=1 colspan=1>2-5</td><td rowspan=1 colspan=1>(2 -1,1- 3,1− 1)</td><td rowspan=1 colspan=1>(1,6,1,1)</td><td rowspan=1 colspan=1>060025 11(6iii)</td><td rowspan=1 colspan=1>7.45</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>(2-2,1-2)</td><td rowspan=1 colspan=1>(7,1,1)</td><td rowspan=1 colspan=1>(）</td><td rowspan=1 colspan=1>7.46</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3-2)</td><td rowspan=1 colspan=1>(3,6)</td><td rowspan=1 colspan=1>(612)</td><td rowspan=1 colspan=1>7.47</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3 - 1,3 - 1)</td><td rowspan=1 colspan=1>(3,3,3)</td><td rowspan=1 colspan=1>(883)</td><td rowspan=1 colspan=1>7.48</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3−1,2 − 1,1−1)</td><td rowspan=1 colspan=1>(5,2,1,1)</td><td rowspan=1 colspan=1>90000222(i 60</td><td rowspan=1 colspan=1>7.49</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3–1,2-1,1−1)</td><td rowspan=1 colspan=1>(4,3,1,1)</td><td rowspan=1 colspan=1>C60002000</td><td rowspan=1 colspan=1>7.50</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3−1,1− 2,1 −1)</td><td rowspan=1 colspan=1>(5,1,1,2)</td><td rowspan=1 colspan=1>(6003)41100ii1</td><td rowspan=1 colspan=1>7.51</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3-1,1-3)</td><td rowspan=1 colspan=1>(1,5,3)</td><td rowspan=1 colspan=1>(</td><td rowspan=1 colspan=1>7.52</td></tr><tr><td rowspan=1 colspan=1>1-4</td><td rowspan=1 colspan=1>(4-1,1− 2)</td><td rowspan=1 colspan=1>(4,3,2)</td><td rowspan=1 colspan=1>(13)</td><td rowspan=1 colspan=1>7.53</td></tr><tr><td rowspan=1 colspan=1>1-4</td><td rowspan=1 colspan=1>(4−1,1− 1,1− 1)</td><td rowspan=1 colspan=1>(3,3,2,1)</td><td rowspan=1 colspan=1>（44402001( 2o1)</td><td rowspan=1 colspan=1>7.54</td></tr></table>

Table 7. All possible example yielding a fiber of type $I I I ^ { * }$

<table><tr><td rowspan=1 colspan=1>Type ofFiber</td><td rowspan=1 colspan=1>lct(P²,B)</td><td rowspan=1 colspan=1>MultiplicitySequence</td><td rowspan=1 colspan=1>CharacteristicSequence</td><td rowspan=1 colspan=1>IntersectionMatrix</td><td rowspan=1 colspan=1>Example</td></tr><tr><td rowspan=5 colspan=1>11*</td><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3-2)</td><td rowspan=1 colspan=1>(9)</td><td rowspan=1 colspan=1>(18)</td><td rowspan=1 colspan=1>7.55</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3 -1,3 - 1)</td><td rowspan=1 colspan=1>(6,3)</td><td rowspan=1 colspan=1>(88）</td><td rowspan=1 colspan=1>7.56</td></tr><tr><td rowspan=1 colspan=1>1-3</td><td rowspan=1 colspan=1>(3-1,1-3)</td><td rowspan=1 colspan=1>(1,8)</td><td rowspan=1 colspan=1>(2 </td><td rowspan=1 colspan=1>7.57</td></tr><tr><td rowspan=1 colspan=1>1-4</td><td rowspan=1 colspan=1>(4 -1,1− 2)</td><td rowspan=1 colspan=1>(7,2)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>7.58</td></tr><tr><td rowspan=1 colspan=1>1-5</td><td rowspan=1 colspan=1>(5-1,1-1)</td><td rowspan=1 colspan=1>(4,5)</td><td rowspan=1 colspan=1>）</td><td rowspan=1 colspan=1>7.59</td></tr><tr><td rowspan=4 colspan=1>1V*</td><td rowspan=1 colspan=1>4-9</td><td rowspan=1 colspan=1>(2 -2,1- 2)</td><td rowspan=1 colspan=1>(6,1,1,1)</td><td rowspan=1 colspan=1>(888</td><td rowspan=1 colspan=1>7.33</td></tr><tr><td rowspan=1 colspan=1>3-7</td><td rowspan=1 colspan=1>(2 –1,1− 2,1–1,1− 1)</td><td rowspan=1 colspan=1>(4,1,1,1,1,1)</td><td rowspan=1 colspan=1>(400002)311 1001       01 000iii0</td><td rowspan=1 colspan=1>7.34</td></tr><tr><td rowspan=1 colspan=1>4-9</td><td rowspan=1 colspan=1>(2 -1,1-3,1− 1)</td><td rowspan=1 colspan=1>(5,1,1,1,1)</td><td rowspan=1 colspan=1>(60000)41112oiii0</td><td rowspan=1 colspan=1>7.35</td></tr><tr><td rowspan=1 colspan=1>3-7</td><td rowspan=1 colspan=1>(2 -1,1-2,1− 2)</td><td rowspan=1 colspan=1>(5,1,1,1,1)</td><td rowspan=1 colspan=1>(60000)2(oiiio)</td><td rowspan=1 colspan=1>7.36</td></tr></table>

Table 8. All possible examples yielding a fiber of type $I I ^ { * }$ and more examples yielding a fiber of type $I V ^ { * }$

# 7. Geometric Descriptions

We now provide a detailed geometric description of all the examples we constructed.
Our exposition is organized as follows: All the examples of Halphen pencils yielding a fixed type of singular fiber are grouped together within a subsection.
The title of each subsection indicates the type of fiber.
Further, we adopt the following pattern: inside parenthesis (and next to the numeration of each example) we describe the components of the curve $B$ .

For completeness we also present some constructions that can be found in the literature and proper references are mentioned.
However, the vast majority of the examples are new and these are marked with a dagger (†).

# 7.1. Type $I _ { n }$ .

Example 7.1 (A rational sextic [26]). Let $\boldsymbol { S } = \{ P _ { 1 } , \ldots , P _ { 1 0 } \}$ be the set consisting of the ten nodes of an irreducible rational plane curve $B$ of degree 6. Any choice of nine points in $\boldsymbol { S }$ defines a Halphen pencil of index two.
Blowing-up the chosen nine points, the strict transform of $B$ becomes a singular fiber of type $I _ { 1 }$ .

Remark 7.2. Note that if $F ^ { \prime }$ is of type $I _ { 1 }$ (resp.
II), then $B$ must be an irreducible rational curve of degree six with a single node (resp.
cusp) and 9 ordinary double points.
Thus, there are 19 (resp.
17) (see e.g. [23],[20]) independent sextics in $\mathbb { P } ^ { 2 }$ so that blowing-up its nine nodes we obtain a rational elliptic surface of index two with a singular fiber of type $I _ { 1 }$ (resp.
II).

Example 7.3 (Two cubics [26]). Consider two nodal cubics $C _ { 1 }$ and $C _ { 2 }$ . Denote the two nodes by $P _ { 1 }$ and $P _ { 2 }$ . The two cubics intersect at nine other points $P _ { 3 } , . . . , P _ { 9 } , P _ { 1 0 } , P _ { 1 1 }$ .

Blowing-up the nine points $P _ { 1 } , \ldots , P _ { 9 }$ we obtain a rational elliptic surface of index two with a fiber of type $I _ { 2 }$ , namely the strict transform of $B = C _ { 1 } + C _ { 2 }$ .

$\dagger$ Example 7.4 (A quartic and a conic).
Consider a quartic $Q _ { 1 }$ with three nodes $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ and a conic $Q _ { 2 }$ that intersects $Q _ { 1 }$ at other eight points $P _ { 4 } , . . . , P _ { 9 } , P _ { 1 0 } , P _ { 1 1 }$ . If we blow-up the nine points $P _ { 1 } , \ldots , P _ { 9 }$ we obtain a rational elliptic surface of index two with a fiber of type $I _ { 2 }$ . Such fiber is given by the strict transform of $B = Q _ { 1 } + Q _ { 2 }$ .

$\dagger$ Example 7.5 (A quintic and a line).
Choose a quintic $Q$ with six nodes $P _ { 1 } , \ldots , P _ { 6 }$ and a line $L$ that intersects $Q$ at other five points $P _ { 7 } , . . . , P _ { 9 } , P _ { 1 0 } , P _ { 1 1 }$ . We get a Halphen pencil of index two generated by $B = Q + L$ and the unique cubic through the nine points $P _ { 1 } , \ldots , P _ { 9 }$ . Thus, blowing-up the nine base points we obtain a rational elliptic surface of index two.
The strict transform of $B$ is a singular fiber of type $I _ { 2 }$ .

Example 7.6 (Three conics [26]). Consider three conics $C _ { 1 } , C _ { 2 }$ and $C _ { 3 }$ . They intersect at twelve points.
Among those, we can choose three points so that if we blow-up the remaining nine points $P _ { 1 } , \ldots , P _ { 9 }$ , the strict transform of $B = C _ { 1 } + C _ { 2 } + C _ { 3 }$ becomes a fiber of type $I _ { 3 }$ in the corresponding rational elliptic surface.

$\dagger$ Example 7.7 (A quartic with three nodes and two lines).
Let $Q$ be a rational plane quartic with three nodes $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ . Consider two lines $L _ { 1 }$ and $L _ { 2 }$ that intersect $Q$ at other eight points $P _ { 4 } , . . . , P _ { 9 } , P _ { 1 0 } , P _ { 1 1 }$ and denote by $P _ { 1 2 }$ the point of intersection of $L _ { 1 }$ and $L _ { \mathrm { 2 } }$ , which we can assume to be distinct from the other $P _ { i }$ . Without loss of generality, we may further assume $P _ { 1 0 } \in L _ { 1 }$ and $P _ { 1 1 } \in L _ { 2 }$ . Then, blowing-up the nine points $P _ { 1 } , \ldots , P _ { 9 }$ we obtain a rational elliptic surface of index two with a singular fiber of type $I _ { 3 }$ . Namely, the strict transform of $B = Q + L _ { 1 } + L _ { 2 }$ .

† Example 7.8 (A cubic with a node, a conic and a line).
Let $C ^ { \prime }$ be a nodal cubic (hence a rational curve).
Let $Q$ be a conic and let $L$ be a line.
Generically, these curves determine twelve distinct intersection points (of multiplicity 2). We can choose three of these points so that if we blow-up the remaining nine points $P _ { 1 } , \ldots , P _ { 9 }$ , the strict transform of $B = C ^ { \prime } { + } Q { + } L$ is a singular fiber of type $I _ { 3 }$ in the corresponding rational elliptic surface.

$\dagger$ Example 7.9 (A cubic with a node and three lines).
Consider a nodal cubic $C ^ { \prime }$ and three distinct lines $L _ { 1 } , L _ { 2 }$ and $L _ { 3 }$ . Generically, these curves determine 13 distinct intersection points: each line intersects the cubic at three points and any two pair of lines intersect at a point.
We can then choose four of these points so that if we blow-up the remaining nine points $P _ { 1 } , \ldots , P _ { 9 }$ , the strict transform of $B = C ^ { \prime } + L _ { 1 } + L _ { 2 } + L _ { 3 }$ becomes a singular fiber of type $I _ { 4 }$ .

† Example 7.10 (Two conics and two lines).
Consider two distinct conics $Q _ { 1 }$ and $Q _ { 2 }$ and a pair of distinct lines $L _ { 1 }$ and $L _ { \mathrm { 2 } }$ . There is a way of choosing four points, among their 13 intersection points, so that if we blow-up the remaining nine points the strict transform of $B = Q _ { 1 } + Q _ { 2 } + L _ { 1 } + L _ { 2 }$ is a singular fiber of type $I _ { 4 }$ in the corresponding rational elliptic surface.

† Example 7.11 (Three concurrent lines and three other lines).
Choose six lines $L _ { 1 } , \ldots , L _ { 6 }$ intersecting as in the picture below

![](images/2bc1340f82f23f75995c5851a1d4fba014618b24fff9fb6b1be99a2ce4b6112d.jpg)\
Figure 2. Six lines yielding a fiber of type $I _ { 7 }$

and so that we can choose a smooth cubic that is tangent to $L _ { 2 }$ at $P _ { 1 }$ (with multiplicity 2) and that passes through P2, . . . , P8. The blow-up of P2 at P (1)1 , P (2)1 , $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 1 ) } , . . . , P _ { 8 } ^ { ( 1 ) }$ determines a rational elliptic surface of index two with a singular fiber of type $I _ { 7 }$ .

† Example 7.12 (Two pairs of three concurrent lines).
Choose six lines $L _ { 1 } , \ldots , L _ { 6 }$ as in the picture below:

![](images/5987c81c507b362d96cd9a51f6997ef674e90d22a794ab7d5a636e2eb5d30cd9.jpg)\
Figure 3. Six lines yielding a fiber of type $I _ { 8 }$

and such that we choose a smooth cubic that is tangent to $L _ { 3 }$ at $P _ { 1 }$ (with multiplicity 2), is tangent to $\mathbb { P } ^ { 2 }$ at $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , . . . , P _ { 7 } ^ { ( 1 ) }$ $L _ { 5 }$ at $P _ { 2 }$ (with multiplicity 2) and that passes through , . . . , P (1)7 gives rise to a rational elliptic surface of index two with $P _ { 3 } , \ldots , P _ { 7 }$ . The blow-up of a singular fiber of type $I _ { 8 }$ .

Example 7.13 (Six Lines [27]). Choose six lines $L _ { 1 } , \ldots , L _ { 6 }$ intersecting as in the picture below:

![](images/b47eee8e3a18a669ec7ba54adaab1d53c44212d03979b596fc840e14487735cb.jpg)\
Figure 4. Six lines yielding a fiber of type $I _ { 9 }$

and such that we can choose a smooth cubic $C$ that is tangent to $L _ { 1 }$ at $P _ { 1 }$ (with multiplicity 2), is tangent to $L _ { 5 }$ at $P _ { 3 }$ (with multiplicity 2), is tangent to $L _ { 6 }$ at $P _ { 2 }$ (with multiplicity 2)

and that also passes through $P _ { 4 } , P _ { 5 }$ and $P _ { 6 }$ . Then, blowing-up $\mathbb { P } ^ { 2 }$ at the points

$$
P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) } , P _ { 6 } ^ { ( 1 ) }
$$

yields a rational elliptic surface of index two with a fiber of type $I _ { 9 }$ .

# 7.2. Type $I I$

$\dagger$ Example 7.14 (A rational sextic).
Let $B$ denote a rational sextic curve with exactly a single cusp and nine nodes, say $P _ { 1 } , \ldots , P _ { 9 }$ . Note that such curve indeed exists (see Remark 7.2). Letting $C$ denote a smooth cubic through the nine points $P _ { 1 } , \ldots , P _ { 9 }$ we obtain a Halphen pencil of index two, namely the pencil generated by $B$ and $2 C$ . Blowing-up $\mathbb { P } ^ { 2 }$ at its nine base points $P _ { 1 } , \ldots , P _ { 9 }$ , but not the cusp, the strict transform of $B$ is a singular fiber of type II in the corresponding elliptic surface.

# 7.3. Type III.

$\dagger$ Example 7.15 (Two cubics).
Let $C _ { 1 }$ and $C _ { 2 }$ be two distinct nodal cubics which are tangent with multiplicity two at a single point and assume $C _ { 1 }$ and $C _ { 2 }$ do not intersect at their nodes.

Denote by $B$ the sextic curve defined by $C _ { 1 } + C _ { 2 }$ and let $C$ denote a smooth cubic through the two nodes and the seven points where $C _ { 1 }$ and $C _ { 2 }$ intersect transversally.
We obtain a Halphen pencil of index two generated by $B$ and $2 C$ . Blowing-up $\mathbb { P } ^ { 2 }$ at the nine base points (but not the tangency point), the strict transform of $B$ is a type III singular fiber in the corresponding elliptic surface.

$\dagger$ Example 7.16 (A quartic and a conic).
Consider a quartic $Q _ { 1 }$ with three nodes $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ and a conic $Q _ { 2 }$ that intersects $Q _ { 1 }$ at other seven points $P _ { 4 } , \dots , P _ { 9 } , P _ { 1 0 }$ , where $P _ { 1 0 }$ is $a$ tangency point.
If we blow-up the nine points $P _ { 1 } , \ldots , P _ { 9 }$ we obtain a rational elliptic surface of index two with a fiber of type $I I I$ , namely the strict transform of $B = Q _ { 1 } + Q _ { 2 }$ .

† Example 7.17 (A quintic and a line).
Choose a quintic $Q$ with six nodes $P _ { 1 } , \ldots , P _ { 6 }$ and a line L that intersects $Q$ at other four points $P _ { 7 } , \dots , P _ { 9 } , P _ { 1 0 }$ , where $P _ { 1 0 }$ is a tangency point.
Consider the Halphen pencil of index two generated by $B = Q + L$ and $2 C$ , where $C$ is the unique cubic through the nine points $P _ { 1 } , \ldots , P _ { 9 }$ . Blowing-up the nine base points we obtain a rational elliptic surface of index two and the strict transform of $B$ is a singular fiber of type III.

# 7.4. Type IV .

† Example 7.18 (Three conics).
Let $C _ { 1 } , C _ { 2 }$ and $C _ { 3 }$ be three different conics through a common fixed point $P$ . Denote by $B$ the sextic curve defined by $C _ { 1 } + C _ { 2 } + C _ { 3 }$ and note that, generically, the three conics intersect at other nine points, say $P _ { 1 } , \ldots , P _ { 9 }$ . Letting $C$ denote a smooth cubic through the points $P _ { 1 } , \ldots , P _ { 9 }$ we obtain a Halphen pencil of degree two generated by $B$ and $2 C$ . Blowing-up $\mathbb { P } ^ { 2 }$ at the nine base points $P _ { 1 } , \ldots , P _ { 9 }$ , but not $P$ , the strict transform of $B$ is a type $I V$ singular fiber in the corresponding elliptic surface.

$\dagger$ Example 7.19 (A quartic with three nodes and two lines).
Let $Q$ be a plane quartic with three nodes $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ , then $Q$ is rational.
Consider two lines $L _ { 1 }$ and $L _ { \mathrm { 2 } }$ that intersect $Q$ at other seven points $P _ { 4 } , \dots , P _ { 9 } , P _ { 1 0 }$ . That is, assume $L _ { 1 } , L _ { 2 }$ and $Q$ pass through a common point $P _ { 1 0 }$ . Then, blowing-up the nine points $P _ { 1 } , \ldots , P _ { 9 }$ we obtain a rational elliptic surface of index two with a singular fiber of type $I V$ , which is given by the strict transform of $B = Q + L _ { 1 } + L _ { 2 }$ .

† Example 7.20 (A cubic with a node, a conic and a line).
Let $C ^ { \prime }$ be a nodal cubic (hence a rational curve).
Let $Q$ be a conic and let $L$ be a line.
Assume these curves pass through a common point and hence determine other nine distinct intersection points (of multiplicity 2). Blowing-up these nine double points, the strict transform of $B = C ^ { \prime } + Q + L$ is a singular fiber of type $I V$ in the corresponding rational elliptic surface.

# 7.5. Type $I _ { n } ^ { * }$

Example 7.21 (Five lines [14].). Take five lines in the plane in general position, say $L _ { 1 } , L _ { 2 } , L _ { 3 } , L _ { 4 }$ and $L _ { 5 }$ . Choose three distinct points in $L _ { 5 }$ that do not lie in any of the other four lines.
Consider the six intersection points $L _ { i } \cap L _ { j }$ for $i , j \neq 5$ and choose a cubic $C$ through these nine points.
Let $B = L _ { 1 } + L _ { 2 } + L _ { 3 } + L _ { 4 } + 2 L _ { 5 }$ , then the pencil generated by $B$ and $2 C$ is a Halphen pencil of index 2 and the corresponding rational elliptic surface contains a singular fiber of type $I _ { 0 } ^ { * }$ . Namely, the strict transform of $B$ .

$\dagger$ Example 7.22 (A double conic and another conic).
Let $Q$ be a (smooth) conic and choose three distinct points on it, say $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ . We can construct a cubic $C$ so that $C$ is tangent to $Q$ at $P _ { i }$ with multiplicity two.
Let $Q ^ { \prime }$ be another conic through $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ so that $Q ^ { \prime }$ intersects $Q$ at a fourth point $P$ , then $P \notin C$ . We can construct $Q ^ { \prime }$ (and $C$ ) so that $Q ^ { \prime }$ intersects $C$ at three other points, say $P _ { 4 } , P _ { 5 }$ and $P _ { 6 }$ . Then the pencil generated by $B = 2 Q ^ { \prime } + Q$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I _ { 0 } ^ { * }$ in the associated rational elliptic surface.

Concretely, we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $Q$ is the conic given by $x ^ { 2 } + y z = 0$ and we have $P _ { 1 } = ( 0 : 0 : 1 ) , P _ { 2 } = ( 0 : 1 : 0 )$ and $P _ { 3 } = ( 1 : - 1 : 1 )$ . Then we can let $C$ be the cubic given by

$$
y ( z ( 2 x + y - z ) + x ^ { 2 } + y z ) = 0
$$

and we can choose $Q ^ { \prime }$ to be the conic given by $x y + 2 x z + y z = 0$ .

Blowing-up P2 at the points P (1), P (2), P (1), $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) } , P _ { 6 } ^ { ( 1 ) }$ we obtain the following (dual) configuration of rational curves:

![](images/f41034691ad77c9fe39ccb2abe03c9f44e380078a2a39fefd3283ff9c61c8f68.jpg)

† Example 7.23 (A double line and two conics).
Let $Q _ { 1 }$ and $Q _ { 2 }$ be two (smooth) conics intersecting at four distinct points, say $P _ { 3 } , P _ { 4 } , P _ { 5 }$ and $P _ { 6 }$ . Let $P _ { 1 }$ be a point in $Q _ { 1 }$ that is not in $Q _ { 2 }$ and let $P _ { 2 }$ be a point in $Q _ { 2 }$ that is not in $Q _ { 1 }$ . Let $L$ be the line joining $P _ { 1 }$ and $P _ { 2 }$ . We can choose $P _ { 1 }$ and $P _ { 2 }$ so that the $P _ { i }$ for $i = 3 , \ldots , 6$ are not in $L$ and $L$ intersects both $Q _ { 1 }$ and $Q _ { 2 }$ at a second point different than the $P _ { i }$ for $i = 3 , \ldots , 6$ .

Now, we can construct a cubic $C$ through $P _ { 1 } , \ldots , P _ { 6 }$ such that the intersection multiplicity of $C$ and $Q _ { i }$ at $P _ { i }$ is two, for $i = 1 , 2$ , and $C$ intersects $L$ at a third point, say $P _ { 7 }$ .

The pencblowing-up generated by at its nine b $B = 2 L + Q _ { 1 } + Q _ { 2 }$ $2 C$ x two andwe obtain $\mathbb { P } ^ { 2 }$ $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) } , P _ { 6 } ^ { ( 1 ) } , P _ { 7 } ^ { ( 1 ) }$ the following (dual) configuration of rational curves:

![](images/10f7f6fd9701739715137d5a85b73fb3914933804ea63dbece60ba5c076437dc.jpg)

That is, we obtain a fiber of type $I _ { 0 } ^ { * }$ in the corresponding rational elliptic surface.

Concretely, we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $Q _ { 1 }$ is the conic given by $x ^ { 2 } + y z = 0$ and $Q _ { 2 }$ is the conic given by $y ^ { 2 } + x z = 0$ . Then we can let $P _ { 1 } = ( 1 : - 1 : 1 )$ and $P _ { 2 } = ( - 4 : - 2 : 1 )$ so that $C$ is the cubic

$$
x ^ { 3 } - 4 x ^ { 2 } y + 2 x y ^ { 2 } + y ^ { 3 } - 2 x ^ { 2 } z + 2 x y z - 5 y ^ { 2 } z - x z ^ { 2 } - 4 y z ^ { 2 } = 0
$$

and $L$ is the line $x - 5 y - 6 z = 0$ .

Lemma 7.24 ([18, Problem 5.41]). Let $C$ be a smooth cubic, let $P _ { 1 } , \ldots , P _ { 3 d }$ be points on $C$ (not necessarily distinct) and choose the group law $\bigoplus$ on $C$ with a flex point $O$ as the origin.
These points satisfy the equation $P _ { 1 } \oplus . . . \oplus P _ { 3 d } = 0$ if and only if there exists a plane curve $D$ of degree $d$ intersecting $C$ precisely at them (where a certain number of repetitions means the intersection multiplicity of $C$ and $\boldsymbol { D }$ at that point).

† Example 7.25 (A double line, a conic and two lines).
Let $C$ be a smooth cubic.
Let $P$ be one of its flex points, which we fix as the origin for the natural group law $\bigoplus$ . Let $\varepsilon _ { 2 }$ be $a$ 2-torsion point $( w . r . t \oplus )$ and choose another point $P _ { 4 } \in C$ . Let $P _ { 1 } \doteq P _ { 4 } - \varepsilon _ { 2 }$ . Then there exist points $P _ { 2 } , P _ { 3 } , P _ { 5 } , P _ { 6 } \in C$ (all distinct) such that

$$
P _ { 1 } \oplus P _ { 2 } \oplus P _ { 3 } = 0 \quad P _ { 4 } \oplus P _ { 5 } \oplus P _ { 6 } = 0 \quad a n d \quad P _ { 4 } \oplus P _ { 7 } \oplus P _ { 8 } = 0
$$

By construction we have

$$
\begin{array} { l l l } { { P _ { 2 } \oplus P _ { 3 } \oplus P _ { 4 } } } & { { = } } & { { \varepsilon _ { 2 } } } \\ { { } } & { { } } & { { P _ { 1 } \oplus P _ { 5 } \oplus P _ { 6 } } } & { { = } } & { { - \varepsilon _ { 2 } = \varepsilon _ { 2 } } } \\ { { } } & { { } } & { { P _ { 1 } \oplus P _ { 7 } \oplus P _ { 8 } } } & { { = } } & { { - \varepsilon _ { 2 } = \varepsilon _ { 2 } } } \end{array}
$$

In particular, $2 P _ { 1 } \oplus P _ { 2 } \oplus . . . \oplus P _ { 8 } = 3 \cdot \varepsilon _ { 2 } = \varepsilon _ { 2 }$ and $2 P _ { 1 } \oplus P _ { 5 } \oplus P _ { 6 } \oplus P _ { 7 } \oplus P _ { 8 } = 2 \cdot \varepsilon _ { 2 } = 0$ .

It follows from Lemma 7.24 that we can construct three lines $L _ { 1 } , L _ { 2 }$ and $L _ { 3 }$ such that $P _ { 1 } , P _ { 2 } , P _ { 3 } \in L _ { 1 }$ , $P _ { 4 } , P _ { 5 } , P _ { 6 } \in L _ { 2 }$ and $P _ { 4 } , P _ { 7 } , P _ { 8 } \in L _ { 3 }$ . By Lemma 7.24 we can also construct $a$ conic $Q$ through $P _ { 1 } , P _ { 5 } , P _ { 6 } , P _ { 7 }$ and $P _ { 8 }$ so that the intersection multiplicity of $Q$ and $C$ at $P _ { 1 }$ is two.

The pencil generatwo and blowing-up by at i $B = 2 L _ { 1 } + L _ { 2 } + L _ { 3 } + Q$ $2 C$ $\mathbb { P } ^ { 2 }$ $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) } , P _ { 6 } ^ { ( 1 ) } , P _ { 7 } ^ { ( 1 ) } , P _ { 8 } ^ { ( 1 ) }$ (1)6 , P (1)7 ,\
we obtain the following (dual) configuration of rational curves:

![](images/07c8d346f99f0c81824a6df425be6d0317747182d6a08a18c78af44fcc2d57bf.jpg)

That is, we obtain a fiber of type $I _ { 0 } ^ { * }$ in the corresponding rational elliptic surface.

Example 7.26 (Five lines, with three lines concurrent at a point [31]). This next example is a geometrical description of an example communicated by Antonio Laface.
The associated Jacobian is the surface $X _ { 1 4 1 }$ in Miranda and Persson’s list [37].

Consider five distinct lines in $\mathbb { P } ^ { 2 }$ , say $L _ { 1 } , L _ { 2 } , L _ { 3 } , L _ { 4 }$ and $L _ { 5 }$ and assume that $L _ { 1 } , L _ { 3 }$ and $L _ { 5 }$ are concurrent at a point $P _ { 1 }$ .

We can choose coordinates in $\mathbb { P } ^ { 2 }$ so that we have $L _ { 1 } : z = 0 , L _ { 2 } : y - z = 0 , L _ { 3 } : x - z = 0$ , $L _ { 4 } : x - y - z = 0$ and $L _ { 5 } : x = 0$ . These lines determine eight intersection points:

$$
{ \begin{array} { r l } & { P _ { 1 } = \left( 0 : 1 : 0 \right) \left( L _ { 1 } \cap L _ { 3 } \cap L _ { 5 } \right) } \\ & { P _ { 2 } = \left( 1 : 0 : 1 \right) \left( L _ { 3 } \cap L _ { 4 } \right) } \\ & { P _ { 3 } = \left( 1 : 1 : 0 \right) \left( L _ { 1 } \cap L _ { 4 } \right) } \\ & { P _ { 4 } = \left( 2 : 1 : 1 \right) \left( L _ { 2 } \cap L _ { 4 } \right) } \end{array} } \qquad { \begin{array} { r l } & { \bullet P _ { 5 } = \left( 1 : 0 : 0 \right) \left( L _ { 1 } \cap L _ { 2 } \right) } \\ & { \bullet P _ { 6 } = \left( 1 : 1 : 1 \right) \left( L _ { 2 } \cap L _ { 3 } \right) } \\ & { \bullet Q _ { 1 } = \left( 0 : 1 : 1 \right) \left( L _ { 2 } \cap L _ { 5 } \right) } \\ & { \bullet Q _ { 2 } = \left( 0 : 1 : - 1 \right) \left( L _ { 4 } \cap L _ { 5 } \right) } \end{array} }
$$

Now consider the lines $R _ { 1 } : x - y = 0$ determined by the points $P _ { 3 }$ and $P _ { 6 }$ ; $R _ { 2 } : y = 0$ , determined by the points $P _ { 2 }$ and $P _ { 5 }$ ; and $R _ { 3 } : x - 2 z = 0$ determined by the points $P _ { 1 }$ and $P _ { 4 }$ There exists a unique cubic $C$ through $P _ { 1 } , \ldots , P _ { 6 }$ which is tangent to $R _ { 3 }$ at $P _ { 1 } = ( 0 : 1 : 0 )$ and which has a node at $P _ { 7 } \doteq ( 0 : t : 1 )$ (for a parameter $t \neq \pm 1$ and $t \neq 0$ ).

Such curves determine five more intersection points

$$
\begin{array} { r l } & { \bullet P _ { 8 } = ( 0 : 0 : 1 ) \qquad } \\ & { \qquad \{ P _ { 8 } \} = R _ { 1 } \cap R _ { 2 } \cap L _ { 5 } \qquad } \\ & { \bullet Q _ { 6 } \in R _ { 1 } \cap R _ { 3 } } \end{array} \qquad \begin{array} { r l } & { \bullet \{ Q _ { 4 } \} = R _ { 2 } \cap R _ { 3 } } \\ & { \bullet Q _ { 5 } \in R _ { 1 } \cap C } \\ & { \bullet Q _ { 6 } \in R _ { 2 } \cap C } \end{array}
$$

Consider the pencil $\mathcal { P }$ generated by $B \doteq L _ { 1 } + L _ { 2 } + L _ { 3 } + L _ { 4 } + 2 L _ { 5 }$ and $D \doteq C + R _ { 1 } + R _ { 2 } + R _ { 3 }$ . If we blow-up of P2 at the points P (1)1 , P (2)1 , P (1)2 , P (1)3 , . . . we obtain a rational elliptic surface of index two with a singular fiber $F$ of type $I _ { 1 } ^ { * }$ and a singular fiber $F ^ { \prime }$ of type $I _ { 4 }$ . We have the following (dual) configurations of rational curves:

![](images/f9b59666ff1a7274316d953d6118f0867049f8bbe23ef064856f554512814283.jpg)

![](images/774ecdeb2ad8d60e48a0e8fbbfcf7b97db59c90c1fb332eb09db33dcff0b44aa.jpg)

$\dagger$ Example 7.27 (A double conic and another conic).
Let $Q$ be a smooth conic and choose three (distinct) points on it, say $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ . Then we can construct a cubic $C$ through $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ so that $C$ is tangent to $Q$ at each $P _ { i }$ with multiplicity two.
And we can also construct another conic $Q ^ { \prime }$ through $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ so that $Q ^ { \prime }$ is tangent to $Q$ and to $C$ at $P _ { 3 }$ (with multiplicity two) and $Q ^ { \prime }$ intersects $C$ at two other points, say $P _ { 4 }$ and $P _ { 5 }$ .

Concretely, we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $Q$ is the conic given by $x ^ { 2 } + y z = 0$ . We can let $P _ { 1 } = ( 0 : 0 : 1 ) , P _ { 2 } = ( 0 : 1 : 0 )$ and $P _ { 3 } = ( 1 : - 1 : 1 )$ . And we can take $C$ to be the cubic given by

$$
y z ( 2 x + y - z ) - x ( x ^ { 2 } + y z ) = y ^ { 2 } z - y z ^ { 2 } - x ^ { 3 } + x y z = 0
$$

Then $Q ^ { \prime }$ is the conic given by $x ^ { 2 } + x y - x z - y z = 0$ and we have that $P _ { 4 } = ( 1 : 1 : 1 )$ and $P _ { 5 } = ( - 1 : 1 : 1 )$ .

By letting $B = 2 Q ^ { \prime } + Q$ we have that the pencil generated by $B$ and $2 C$ is a Halphen pencil of index two.
Moreover, the corresponding rational elliptic surface has a fiber of type $I _ { 1 } ^ { * }$ .

We blow-up P2 at the points P (1), P (2), P (1), P (2), $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 3 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) }$ , which produces the following (dual) configuration of rational curves:

![](images/3676a734dcca3b4f2ba7ed6bceb47951709456b1acfd1d8191ec8a767c4b5468.jpg)

$\dagger$ Example 7.28 (A double conic and two tangent lines).
Let $C$ be a smooth cubic.
Choose two distinct points $P _ { 3 }$ and $P _ { 4 }$ on $C$ such that the lines $L _ { 1 }$ (resp.
$L _ { 2 }$ ) tangent to $C$ at $P _ { 3 }$ (resp.
$P _ { 4 }$ ) intersect at a fifth point $P _ { 5 }$ that is also in $C$ . Then there exists a unique conic $Q$ that is tangent to the lines $L _ { 1 }$ (resp.
$L _ { 2 }$ ) at $P _ { 3 }$ (resp.
$P _ { 4 }$ ). Such conic intersects $C$ at two other distinct points, say $P _ { 1 }$ and $P _ { 2 }$ . If we let $B = 2 Q + L _ { 1 } + L _ { 2 }$ , it follows that the $B$ $2 C$ of index two.
Thus, blowing-up the ninewe obtain a rational elliptic surface of points P (1)1 , P (1)2 , P $P _ { 1 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 3 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 2 ) } , P _ { 4 } ^ { ( 3 ) } , P _ { 5 } ^ { ( 1 ) }$\
index two with a type $I _ { 2 } ^ { * }$ singular fiber.

In fact, we obtain the following (dual) configuration of rational curves:

![](images/8430c7da9905bd8551aa3934671edbd11daf09072a479a84d904c443426b38b1.jpg)

$\dagger$ Example 7.29 (Two double lines and two other lines).
Let $C$ be a smooth cubic.
Choose $P _ { 1 } \in C$ not a flex point and let $L _ { 1 }$ be the tangent line to $C$ at $P _ { 1 }$ . Then $C$ intersects $L _ { 1 }$ at another point, say $P _ { 2 }$ . We can choose $P _ { 1 }$ so that $P _ { 2 }$ is not a flex point.
Let $L _ { 3 }$ be the tangent line to $C$ at $P _ { 2 }$ and let $P _ { 4 }$ be the third intersection point.
Choose a line $L _ { 4 }$ through $P _ { 4 }$ which is tangent to $C$ at a point $P _ { 3 }$ . Let $L _ { 2 }$ be the line joining $P _ { 1 }$ and $P _ { 3 }$ . Then $L _ { 2 }$ intersects $C$ at a third point $P _ { 5 }$ .

Letting $B = 2 L _ { 1 } + 2 L _ { 2 } + L _ { 3 } + L _ { 4 }$ we have that the pencil generated by $B$ and $2 C$ is a Halphen pencil of index two, which yields a fiber of type $I _ { 3 } ^ { * }$ in the corresponding rational elliptic surface.
More precisely, blowing-up P (1)1 , P (2)1 , P (3)1 , P (1)2 , P (2)2 , $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 1 } ^ { ( 3 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) }$ gives the following (dual) configuration of rational curves:

![](images/46e836b8ae10766b5d7a19b6e43a9743cccf540d5b3b4ab0af44d29d576ed949.jpg)

† Example 7.30 (Two double lines and two other lines).
Let $C$ be a smooth cubic.
Let $P _ { 1 } \in C$ be a flex point and let $L _ { 4 }$ be the corresponding inflection line.
Let $L _ { 1 }$ be a line through $P _ { 1 }$ which is tangent to $C$ at $P _ { 2 }$ and let $L _ { 3 }$ be another line through $P _ { 1 }$ which is tangent to $C$ at $P _ { 3 } \neq P _ { 2 }$ . Let $L _ { 2 }$ be the line joining $P _ { 2 }$ and $P _ { 3 }$ . Then $L _ { 2 }$ intersects $C$ at $a$ third point $P _ { 4 }$

If we let $B = 2 L _ { 1 } + 2 L _ { 2 } + L _ { 3 } + L _ { 4 }$ , then the pencil generated by $B$ and $2 C$ is a Halphen pencil of indexThe blow-up of , wat $I _ { 4 } ^ { * }$ ng rational elliptic surface.yields the following (dual) $\mathbb { P } ^ { 2 }$ $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 1 } ^ { ( 3 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 3 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 4 } ^ { ( 1 ) }$ configuration of rational curves:

![](images/08df4272c911ced7d6fea8026586c92399c394434493b81b4403b86bc8b0df02.jpg)

7.6. Type $I V ^ { * }$ . We now construct all possible examples of Halphen pencils of index two that yield a fiber of type $I V ^ { * }$ in the corresponding rational elliptic surface (Theorem 5.17).

Definition 7.31. Given a cubic $C$ , a conic $Q$ and a point $P \in C$ , we say $Q$ is an osculating conic of $C$ at $P$ if $I _ { P } ( Q , C ) \ge 5$ , where $I _ { P } ( Q , C )$ denotes the intersection multiplicity of $Q$ and $C$ at $P$ .

Definition 7.32. Given a cubic $C$ , any point on it where a tangent conic intersects $C$ with multiplicity six is called a sextactic point.
If $C$ is smooth, there are exactly 27 such points and if $C$ is nodal, then there only 3 sextactic points (see e.g. [8],[9]).

† Example 7.33 (A double conic and a conic).
Consider a smooth cubic $C$ and let $P _ { 1 }$ be a sextactic point.
Let $Q _ { 1 }$ be the corresponding osculating conic.
Assume we can construct another conic $Q _ { 2 }$ so that $Q _ { 2 }$ is tangent to both $Q _ { 1 }$ and $C$ at $P _ { 1 }$ with multiplicity three, $Q _ { 2 }$ intersects $C$ at other three points $P _ { 2 } , P _ { 3 } , P _ { 4 }$ . Then the fourth intersection point between the two conics is different than the $P _ { i }$ ’s.

Letting $B = Q _ { 1 } + 2 Q _ { 2 }$ we have that the pencil generated by $B$ and $2 C$ is a Halphen pencil of index two and the corresponding rational elliptic surface has a fiber of type $I V ^ { * }$ .

For instance, let $C$ be the cubic given by $x z ^ { 2 } + y ^ { 2 } z + x ^ { 3 } = 0$ , then we can let $P _ { 1 } = ( 0 : 0 : 1 )$ and we have that $Q _ { 1 }$ is the conic $y ^ { 2 } + x z = 0$ . Choosing $Q _ { 2 }$ to be the conic $x y + y ^ { 2 } + x z = 0$ we get the desired pencil.

Blowing-up $\mathbb { P } ^ { 2 }$ at the points $P _ { 1 } ^ { ( 1 ) } , . . . , P _ { 1 } ^ { ( 6 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) }$ (1)2 , P (1)3 , P we obtain the following (dual) configuration of rational curves:

![](images/84ebab0f5b90202bff4471797801ad5a7cc284439dbbd4d264613511c58278a0.jpg)

$\dagger$ Example 7.34 (A double line, a conic and two lines).
Let $Q$ be a (smooth) conic and choose $P _ { 1 } \in Q$ . Let $T$ be the tangent line to $Q$ at $P _ { 1 }$ . Let $L _ { 1 }$ be a line through $P _ { 1 }$ , intersecting $Q$ a t a second point $P _ { 2 }$ . Choose two other points $P _ { 3 }$ and $P _ { 4 }$ in $Q$ , let $L _ { 2 }$ be the line joining them and let $\{ P _ { 5 } \} = L _ { 1 } \cap L _ { 2 }$ . Assume we can construct a cubic $C$ through $P _ { 1 } , \ldots , P _ { 5 }$ which is tangent to $Q$ (resp.
$T$ ) with multiplicity 3 (resp.
2.). Then $C$ intersects $T$ at another point $P _ { 6 }$ .

Letting $B = 2 T + Q + L _ { 1 } + L _ { 2 }$ we have that the pencil generated by $B$ and $2 C$ is a Halphen pencil of index two and the corresponding rational elliptic surface has a fiber of type $I V ^ { * }$ .

For instance, we can choose coordinates so that $Q$ is the conic $y ^ { 2 } + x z = 0$ and we can choose $P _ { 1 } = ( 0 : 0 : 1 )$ . Then $T$ is the line $x = 0$ . Choosing $L _ { 1 }$ to be the line $x + y = 0$ we have that $P _ { 2 } = ( - 1 : - 1 : 1 )$ . Now, if we choose $P _ { 4 }$ and $P _ { 5 }$ so that $L _ { 2 }$ is the line $x + y + z$ , then $P _ { 5 } = ( - 1 : 1 : 0 )$ and $C$ is the cubic $x ^ { 3 } + y ^ { 3 } + 2 x y z + y ^ { 2 } z + x z ^ { 2 } = 0$ . Thus, $P _ { 6 }$ is the point $( 0 : 1 : - 1 )$ .

Blowing-up $\mathbb { P } ^ { 2 }$ at the points $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 4 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) } , P _ { 6 } ^ { ( 1 ) }$ we obtain the following (dual) configuration of rational curves:

![](images/802320b0a64b30368735801fb04a6e7ca7cc0d42c1d70d03afdefd57d2560a9e.jpg)

† Example 7.35 (A double line, a cubic and another line).
Let $D$ be a nodal cubic and denote its node by $P _ { 5 }$ . Let $P _ { 1 }$ be a flex point of $D$ and denote the corresponding inflection line by $L$ . Let $L ^ { \prime }$ be a line that intersects $D$ at three other points $P _ { 2 } , P _ { 3 }$ and $P _ { 4 }$ . Assume we can construct a cubic $C$ through $P _ { 1 } , \ldots , P _ { 5 }$ so that $C$ is tangent to $D$ (resp.
$L$ ) at $P _ { 1 }$ with multiplicity 4 (resp.
3).

For instance, let $D$ be the nodal cubic $y ^ { 2 } z - x ^ { 2 } ( x + z ) = 0$ . Then $P _ { 5 } = ( 0 : 0 : 1 )$ and we can let $P _ { 1 } = ( 0 : 1 : 0 )$ so that $L$ is the line $z = 0$ . Choosing $L ^ { \prime }$ to be the line $x + y + z = 0$ we have that $C$ is the cubic $x y z + x z ^ { 2 } + y ^ { 2 } z - x ^ { 3 } = 0$ .

Letting $B = 2 L + L ^ { \prime } + D$ we have that the pencil generated by $B$ and $2 C$ is a Halphen pencil of index two and the corresponding rational elliptic surface has a fiber of type $I V ^ { * }$ .

Blowing-up $\mathbb { P } ^ { 2 }$ at the points $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 5 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) }$ we obtain the following (dual) configuration of rational curves:

![](images/44badcb9efbc65bb97328d9bfbb4556eadf383e825e844660bc563016cb919e6.jpg)

Example 7.36 (A double line and two conics).
Let $C$ be a smooth cubic.
Let $P _ { 2 }$ be a flex point.
There exists a line $L$ through $P _ { 2 }$ which is tangent to $C$ at another point $P _ { 1 }$ . Then $P _ { 1 }$ is a sextactic (see Definition 7.32) point of $C$ .

In fact, by Lemma 7.24 we have

$$
2 P _ { 1 } \oplus P _ { 2 } = 0 \qquad 3 P _ { 2 } = 0
$$

hence $3 ( 2 P _ { 1 } \oplus P _ { 2 } ) = 6 P _ { 1 } = 0$ , where $\bigoplus$ denotes the group law with another flex point taken as the origin.
Again, using Lemma 7.24 we conclude there exists an osculating conic which is tangent to $C$ with multiplicity at $P _ { 1 }$ .

Concretely, we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $C$ is the cubic given by

$$
y ^ { 2 } z = x ( x - z ) ( x - \alpha \cdot z ) \quad \alpha \in \mathbb { C } \backslash \{ 0 , 1 \}
$$

and $C$ has a flex point at $P _ { 2 } = ( 0 : 1 : 0 )$ . The line $x = 0$ is tangent to $C$ at $P _ { 1 } = ( 0 : 0 : 1 )$ and the flex $P _ { 2 }$ is a point in that line.

Now, let $\varepsilon _ { 2 }$ be a two torsion point of $C$ . Using the same argument as in Example 7.25, we can always find three points $P _ { 3 } , P _ { 4 }$ and $P _ { 5 }$ in $C$ so that $P _ { 3 } \oplus P _ { 4 } \oplus P _ { 5 } = \varepsilon _ { 2 }$ . In particular, $2 P _ { 3 } \oplus 2 P _ { 4 } \oplus 2 P _ { 5 } = 0$ and we claim we must have

$$
3 P _ { 1 } \oplus P _ { 3 } \oplus P _ { 4 } \oplus P _ { 5 } = 0
$$

and

$$
P _ { 1 } \oplus 2 P _ { 2 } \oplus P _ { 3 } \oplus P _ { 4 } \oplus P _ { 5 } = 0
$$

In fact, if one of these sums is non zero, then adding the two equations we obtain

$$
0 \neq 4 P _ { 1 } \oplus 2 P _ { 2 } \oplus 2 P _ { 3 } \oplus 2 P _ { 4 } \oplus 2 P _ { 5 } = 4 P _ { 1 } \oplus 2 P _ { 2 } = 0
$$

a contradiction.

Applying Lemma 7.24 two Equations (12) and (13) we conclude there exists two conics $Q$ and $Q ^ { \prime }$ so that: $P _ { 1 } , P _ { 3 } , P _ { 4 } , P _ { 5 } \in Q$ , the cubic $C$ is tangent $Q$ at $P _ { 1 }$ with multiplicity three, $P _ { 1 } , P _ { 2 } , P _ { 3 } , P _ { 4 } , P _ { 5 } \in Q ^ { \prime }$ and the cubic $C$ is tangent $Q$ at $P _ { 2 }$ with multiplicity two.

Note that, by construction, $L$ is also tangent to $Q$ at $P _ { 1 }$

Letting $B = 2 L + Q + Q ^ { \prime }$ we have that the pencil generated by $B$ and $2 C$ is a Halphen pencil of index two and the corresponding rational elliptic has a fiber of type $I V ^ { * }$ .

More precisely, blowing-up P2 at the points P (1)1 , $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 4 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) }$ we obtain the following (dual) configuration of rational curves:

![](images/c8e6f45ceeb25ca6cdacc1db641c88c1d9ff5b16f90fae1e74f14b7dcd7b90d2.jpg)

$\dagger$ Example 7.37 (Two double lines and two other lines).
Let $Q$ be a smooth conic.
And choose three distinct points on $Q$ say $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ . For each $i = 1 , 2$ let $T _ { i }$ be the tangent line to $Q$ at $P _ { i }$ . Let $L _ { i }$ be the line joining $P _ { 1 }$ and $P _ { i }$ , for $i = 2 , 3$ . And let $L$ be a line through $\{ P _ { 4 } \} = T _ { 1 } \cap T _ { 2 }$ different than the $T _ { i }$ and such that $P _ { 3 } \notin { L }$ . Then $L$ intersects both $L _ { 2 }$ and $L _ { 3 }$ at two other points $P _ { 5 } \in L _ { 2 }$ and $P _ { 6 } \in L _ { 3 }$ .

Letting $C$ be the cubic $Q + L$ and $B$ be the sextic $T _ { 1 } + T _ { 2 } + 2 L _ { 2 } + 2 L _ { 3 }$ we have that the pencil $\mathcal { P }$ generated by $B$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I V ^ { * }$ in the associated elliptic surface.

Blowing-up P2 at the nine points P (1)1 , P (2)1 , P (3)1 , $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 1 } ^ { ( 3 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) } , P _ { 6 } ^ { ( 1 ) }$ we obtain the following (dual) configuration of rational curves:

![](images/54c4c23492b8e031dee8f4d8a6deed42813d4b703ad8852e73bd733b752ab715.jpg)

$\dagger$ Example 7.38 (Two double lines and a conic).
Let $Q$ be a smooth conic.
And choose three distinct points on $Q$ say $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ . For each $i = { 1 , 2 , 3 }$ let $L _ { i }$ be the tangent line to $Q$ a t $P _ { i }$ . Let $L$ (resp.
$R$ ) be the lines joining $P _ { 1 }$ and $P _ { 3 }$ (resp.
$P _ { 2 }$ and $P _ { 3 }$ ). And let $\{ P _ { 4 } \} = L \cap L _ { 2 }$ and $\{ P _ { 5 } \} = R \cap L _ { 1 }$ .

Then the cubic $C = L _ { 1 } + L _ { 2 } + L _ { 3 }$ is such that the intersection multiplicity of $Q$ and $C$ at $P _ { i }$ , for $i = 1 , 2 , 3$ is two and the pencil $\mathcal { P }$ generated by $B = Q + 2 L + 2 R$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I V ^ { * }$ in the associated elliptic surface.
In fact the Jacobian fibration of such surface is the surface $X _ { 4 3 1 }$ in Miranda and Persson’s list [37].

Concretely, we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $Q$ is given by $x ^ { 2 } - y z = 0$ , $P _ { 1 } = ( 0 :$ $0 : 1 ) , P _ { 2 } = ( 0 : 1 : 0 )$ and $P _ { 3 } = ( 1 : - 1 : - 1 )$ . Then $L _ { 1 }$ is the line $y = 0$ , $L _ { 2 }$ is the line $z = 0$ and $L _ { 3 }$ is the line $2 x + y + z = 0$ . And, therefore, $L$ and $R$ are the lines $x + y = 0$ and $x + z = 0$ , respectively.
Moreover, $P _ { 4 } = ( 1 : - 1 : 0 )$ and $P _ { 5 } = ( 1 : 0 : - 1 )$ .

Blowing-up the nine points P (1)1 , P (2)1 , $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 3 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) }$ we obtain the following (dual) configuration of rational curves:

![](images/96c90ee1337c5d8454d63197d5f66638f630a58873d49eb267036623e537e1b1.jpg)

† Example 7.39 (A double conic and two lines).
Let $C$ be a smooth cubic.
Let $L _ { 1 }$ be an inflection line of $C$ at a point $P _ { 1 }$ and choose a line $L _ { 2 }$ through $P _ { 1 }$ which is tangent to $C$ at another point $P _ { 2 }$ . We can construct a conic $Q$ through $P _ { 1 }$ and $P _ { 2 }$ so that $Q$ is tangent to $C$ at $P _ { 1 }$ with multiplicity two and $Q$ meets $C$ transversally at $P _ { 2 }$ . Moreover, $Q$ intersects $C$ at other three points, say $P _ { 3 } , P _ { 4 }$ and $P _ { 5 }$ .

Concretely, choose coordinates in $\mathbb { P } ^ { 2 }$ so that $C$ is the cubic given by

$$
y ^ { 2 } z = x ( x - z ) ( x - \alpha \cdot z ) \quad \alpha \in \mathbb { C } \backslash \{ 0 , 1 \}
$$

Then we can let $L _ { 1 }$ be the line $z = 0$ and hence $P _ { 1 } = ( 0 : 1 : 0 )$ and we can let $L _ { 2 }$ be either one of the lines $x = 0 , x - z = 0$ or $x - \alpha \cdot z = 0$ .

If we choose $L _ { 2 }$ as $x = 0$ , then $P _ { 2 } = ( 0 : 0 : 1 )$ and, similarly, if we take $L _ { 2 }$ as $x - z = 0$ (resp.
$x - \alpha \cdot z = 0$ ), then $P _ { 2 } = ( 1 : 0 : 1 )$ (resp.
$P _ { 2 } = ( \alpha : 0 : 1 ) ,$ .

Say we choose $L _ { \mathrm { 2 } }$ to be the line $x = 0$ , then we can let $Q$ be the conic $x ^ { 2 } + y z = 0$ .

Now, the pencil $\mathcal { P }$ generated by $B = 2 Q + L _ { 1 } + L _ { 2 }$ and $2 C$ is a Halphen pencil of index two that yields a fiber of type $I V ^ { * }$ in the corresponding rational elliptic surface.

More precisely, blowing-up $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 4 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) }$ we obtain the following (dual) configuration of rational curves:

![](images/fdc62e79a5e266559c836ce9a6d97aecf637a9bdf9b262672100a9720e219c8e.jpg)

Example 7.40 (A triple conic [35, I.5.11]). In this example we consider a rational elliptic surface of index two whose Jacobian is the surface $X _ { 4 3 1 }$ in Miranda and Persson’s list [37].

Let $Q \subset \mathbb { P } ^ { 2 }$ be a smooth conic and choose three distinct points $P _ { 1 } , P _ { 2 }$ and $P _ { 3 }$ on $Q$ . Let $L _ { i }$ be the line tangent to $Q$ at $P _ { i }$ and consider the pencil generated by $B = 3 Q$ and $2 C$ , where $C = L _ { 1 } + L _ { 2 } + L _ { 3 }$ . Then the associated rational elliptic surface has as its Jacobian the surface $X _ { 4 3 1 }$ .

Note that we need to blow-up each of the three points three times.
That is, to construct the desired surface we blow-up $\mathbb { P } ^ { 2 }$ at $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 1 } ^ { ( 3 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 3 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 3 ) }$ , which produces three disjoint chains of $\left( - 2 \right)$ -curves, each of length 2 and formed by exceptional divisors over the corresponding three points.
Pictorially,

![](images/5d1340490cd4441ff805a87c279cda0e982cbe01a6f7f7be0ee790f1c646acf1.jpg)

† Example 7.41 (A triple line, a conic and another line).
Choose two (distinct) lines $L _ { 1 }$ and $L _ { \mathrm { 2 } }$ and a smooth conic $Q$ in general position.
Let $\{ P _ { 2 } \} = L _ { 1 } \cap L _ { 2 }$ , let $\{ P _ { 2 } , P _ { 4 } \} = L _ { 1 } \cap Q$ and let $\{ P _ { 1 } , P _ { 3 } \} = L _ { 3 } \cap Q$ . We can find a cubic $C$ so that $P _ { 1 } , P _ { 2 } , P _ { 3 } , P _ { 4 } , P _ { 5 } \in C$ and $C$ is tangent to $Q$ at $P _ { 3 }$ with multiplicity three.

Concretely, we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $Q$ is the conic $x ^ { 2 } + y z + x z = 0$ and $L _ { 1 }$ and $L _ { \mathrm { 2 } }$ are the lines $x + 2 y + z = 0$ and $x = 0$ , respectively.

Then $P _ { 1 } = ( 0 : 1 : 0 ) , P _ { 2 } = ( 0 : 1 : - 2 ) , P _ { 3 } = ( 0 : 0 : 1 ) , P _ { 4 } = ( 1 : 0 : - 1 )$ and $P _ { 5 } = ( 1 : - 1 : 1 )$ and we have that $C$ is the cubic given by

$$
x y ( x + z ) + ( x ^ { 2 } + y z + x z ) ( 2 y + z ) = 0
$$

Now, the pencil generated by $B = Q + L _ { 1 } + 3 L _ { 2 }$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I V ^ { * }$ in the associated elliptic surface.

If we blow-up P2 at the nine points P (1)1 , P (2)1 , P (1)2 , $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 3 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) }$ we obtain the following (dual) configuration of rational curves:

![](images/2592cb355cee9d92b9ab2137f9efc5daa405dd31194b3a228d1a1299e8111623.jpg)

$\dagger$ Example 7.42 (A triple line, a double line and another line).
Let $C$ be a smooth cubic and let $L _ { 1 }$ be an inflection line of $C$ at a point $P _ { 1 }$ . We can choose another line $L _ { 2 }$ through $P _ { 1 }$ which is tangent to $C$ at another point $P _ { 2 }$ . Let $L _ { 3 }$ be a third line which intersects $C$ at three distinct points, say $P _ { 3 } , P _ { 4 }$ and $P _ { 5 }$ , all different than $P _ { 1 }$ and $P _ { 2 }$ . Then the pencil $\mathcal { P }$ generated by $B = L _ { 1 } + 3 L _ { 2 } + 2 L _ { 3 }$ and $2 C$ is a Halphen pencil of index two and it yields a fiber of type $I V ^ { * }$ in the corresponding elliptic surface.

Concretely, we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $C$ is the cubic given by

$$
y ^ { 2 } z = x ( x - z ) ( x - \alpha \cdot z ) \qquad \alpha \in \mathbb { C } \backslash \{ 0 , 1 \}
$$

e can let $L _ { 1 }$ be the line $z = 0$ (hence $P _ { 1 } = ( 0 : 1 : 0 ) )$ and we can choose $L _ { 2 }$ to be either ne of the lines $x = 0 , x - z = 0$ or $x - \alpha \cdot z = 0$ .

If we choose $L _ { 2 }$ as $x = 0$ , then $P _ { 2 } = ( 0 : 0 : 1 )$ and we can let $L _ { 3 }$ be the line $x + y + z = 0$ Now, if we blow-up $\mathbb { P } ^ { 2 }$ at the nine base points

$$
P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 1 } ^ { ( 3 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 3 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) }
$$

we obtain the following (dual) configuration of rational curves:

![](images/c19b265d61ca8ec273f88f75701bf62483ae7e8d6e9b9dda9017a729ca9f6688.jpg)

† Example 7.43 (A triple line and three more lines).
Consider four (distinct) lines $L _ { 1 } , L _ { 2 } , L _ { 3 }$ and $L _ { 4 }$ in general position.
That is, such that the $L _ { i }$ determine six intersection points, say $P _ { 1 } , \ldots , P _ { 6 }$ . Now, choose a cubic $C$ through these six points so that $C$ intersects each of the lines transversally, i.e. the $L _ { i }$ are not tangent lines to $C$ .

The pencil $\mathcal { P }$ generated by $B = L _ { 1 } + L _ { 2 } + L _ { 3 } + 3 L _ { 4 }$ and $2 C$ is a Halphen pencil of index two and it yields a fiber of type $I V ^ { * }$ in the corresponding rational elliptic surface.

Concretely, we blow-up P2 at the base points P (1)1 , P (2)1 , $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 5 } ^ { ( 1 ) } , P _ { 6 } ^ { ( 1 ) }$ of $\mathcal { P }$ so that we obtain the following (dual) configuration of rational curves:

![](images/78fbc7a1617a8672272fb3c86316a5cf7cbe7ae12f88916ded25176d669ae702.jpg)

If we take $B$ and $C$ as in the picture below, then we obtain a rational elliptic surface whose Jacobian is the surface $X _ { 4 3 1 }$ in Miranda and Persson’s list [37].

![](images/a553a4f9582ff3bacf879350e2a598ff7f4c15fbac02d5c38f51873df23ffa65.jpg)\
Figure 5. The two generators of $\mathcal { P }$ yielding a fiber of type $I V ^ { * }$ and a multiple fiber of type $I _ { 3 }$

† Example 7.44 (A triple line and a cubic).
Let $D : d = 0$ be a nodal cubic with node at a point $P _ { 4 }$ . Let $L _ { 1 } : l _ { 1 } = 0$ and $L _ { 2 } : l _ { 2 } = 0$ be two of its inflections lines at points $P _ { 1 }$ and $P _ { 2 } ~ ( \ne P _ { 4 } )$ , respectively.
And let $L _ { 3 }$ be a line through the node $P _ { 4 }$ which does not contain the flex points $P _ { 1 }$ and $P _ { 2 }$ . Then the cubic $C$ given by $l _ { 1 } l _ { 2 } l _ { 3 } + d = 0$ is such that the intersection multiplicity of $D$ and $C$ at $P _ { i }$ for $i = 1 , 2$ i s

$$
I _ { P _ { i } } ( C , D ) = I _ { P _ { i } } ( l _ { i } , d ) = 3
$$

and, by construction, the node $P _ { 4 }$ lies on it.

Now let $L$ be the line joining $P _ { 1 }$ and $P _ { 2 }$ . Then $L$ intersects $D$ at a third (flex) point $P _ { 3 }$ and we have that the pencil $\mathcal { P }$ generated by $B = D + 3 L$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I V ^ { * }$ in the corresponding elliptic surface.

Blowing-up $\mathbb { P } ^ { 2 }$ at the nine base points $P _ { 1 } ^ { ( 1 ) } , P _ { 1 } ^ { ( 2 ) } , P _ { 1 } ^ { ( 3 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 3 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 4 } ^ { ( 1 ) }$ we obtain the following (dual) configuration of rational curves:

![](images/cda2f213301c9096d3687326e72ca54402d43ccc3eb369150c357ac64ee3baaf.jpg)

7.7. Type $I I I ^ { * }$ . We now construct all possible examples of Halphen pencils of index two that yield a fiber of type $I I I ^ { * }$ in the corresponding rational elliptic surface (Theorem 5.16).

† Example 7.45 (A double line, a cubic and another line).
Let $D$ be a nodal cubic and denote its node by $P _ { 1 }$ . Let $P _ { 2 }$ be a flex point of $\boldsymbol { D }$ and denote the corresponding inflection line by $L _ { 1 }$ . Let $L _ { \mathrm { 2 } }$ be a line through $P _ { 2 }$ so that $L _ { 2 }$ intersects $D$ at two other points, say $P _ { 3 }$ and $P _ { 4 }$ . We can construct a cubic $C$ through $P _ { 1 } , \ldots , P _ { 4 }$ so that $C$ is tangent to $D$ (resp.
$L _ { 1 }$ ) at $P _ { 2 }$ with multiplicity five (resp.
three).

Concretely, let $D$ be the nodal cubic given by $y ^ { 2 } z - x ^ { 2 } ( x + z ) = 0$ . Then $P _ { 1 } = ( 0 : 0 : 1 )$ and we can let $L _ { 1 }$ be the line $z = 0$ , hence $P _ { 2 } = ( 0 : 1 : 0 )$ . Thus we can take $L _ { 2 }$ to be the line $x - z = 0$ . And, further, we have that $P _ { 4 } = ( 1 : { \sqrt { 2 } } : 1 )$ and $P _ { 5 } = ( 1 : - { \sqrt { 2 } } : 1 )$ . Choosing $C$ to be the cubic given by

$$
y ^ { 2 } z - x ( x ^ { 2 } + z ^ { 2 } ) = 0
$$

we have that all the points $P _ { 1 } , \ldots , P _ { 4 }$ lie in $C$ and, moreover, the intersection multiplicity of $C$ and $D$ (resp.
$L _ { 1 }$ ) at $P _ { 2 }$ is five (resp.
three).

Now, the pencil $\mathcal { P }$ generated by $B = D + 2 L _ { 1 } + L _ { 2 }$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I I I ^ { * }$ in the corresponding rational elliptic surface.
More precisely, blowing-u p P (1)1 , P (1)2 , . $P _ { 1 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 1 ) } , \dots , P _ { 2 } ^ { ( 6 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) }$ we obtain the following (dual) configuration of rational curves

![](images/0b56d7f1ccd7e6416c317a5a7a12b8ba7fcef2961d660c999d3ca35a0098f8e5.jpg)

$\dagger$ Example 7.46 (A double conic and another conic).
Let $Q$ be a conic and choose a point $P _ { 1 } \in Q$ . We can construct another conic $Q ^ { \prime }$ and a smooth cubic $C$ so that $Q$ is tangent to both $C$ and $Q ^ { \prime }$ at $P _ { 1 }$ with full multiplicity and, moreover, the intersection multiplicity of $Q ^ { \prime }$ and $C$ at $P _ { 1 }$ is four and $Q ^ { \prime }$ intersects $C$ at two other points, say $P _ { 2 }$ and $P _ { 3 }$ .

Concretely, choose coordinates in $\mathbb { P } ^ { 2 }$ so that $Q$ is the conic given by $x ^ { 2 } + y z = 0$ and $P _ { 1 }$ be the point $( 0 : 0 : 1 )$ . Then we can let $Q ^ { \prime }$ be the conic given by $x ^ { 2 } + y z + y ^ { 2 } = 0$ and can let $C$ be the cubic given by

$y ^ { 3 } + z ( x ^ { 2 } + y z ) = 0$ Thus, $P _ { 2 } = ( \alpha : 1 : 1 )$ and $P _ { 3 } = \left( - \alpha : 1 : 1 \right)$ , where $\alpha ^ { 2 } + 2 = 0$

Now, the pencil $\mathcal { P }$ generated by $B = 2 Q ^ { \prime } + Q$ and $2 C$ is a Halphen pencil of index two such that the corresponding elliptic surface has a fiber of type .

Blowing-up $\mathbb { P } ^ { 2 }$ at $P _ { 1 } ^ { ( 1 ) } , . . . , P _ { 1 } ^ { ( 7 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 1 ) }$ we obtain the following (dual) configuration of $\dagger$ Example 7.47 (A triple conic).
In this new example we construct a rational elliptic surface whose Jacobian is the surface $X _ { 3 2 1 }$ in Miranda and Persson’s list [37].

![](images/21a46e977eb546de5e13ad235673a28194284b803af44af75af2151d3bfa845e.jpg)

Let $Q \subset \mathbb { P } ^ { 2 }$ be a (smooth) conic.
Then, there exists a line $L$ (resp.
a conic $R$ ) that is tangent to $Q$ with full multiplicity 2 (resp.
4). In fact we can assume we have determined two distinct intersection points this way.
Now, generically, $L$ intersects R at two other points.

Letting $C = L + R$ and $B = 3 Q$ we have that the pencil generated by $B$ and $2 C$ is a Halphen npencil of index two.
In particular, blowing-up $\mathbb { P } ^ { 2 }$ at the nine base points $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 3 ) } , P _ { 2 } ^ { ( 1 ) } , \ldots , P _ { 2 } ^ { ( 6 ) }$ . . . , P (6)2 we obtain a rational elliptic surface of index two.
And such surface has a type $I I I ^ { * }$ singular fiber.

In fact, we obtain the following (dual) configuration of rational curves:

![](images/dbd84f678adeee5d9cee5cbc9b670b935bd4e8a4c4e57a441caea93d495b6c4a.jpg)

† Example 7.48 (Two triple lines).
Consider two (distinct) lines $L _ { 1 }$ and $L _ { 2 }$ and let $P _ { 3 }$ be their intersection point.
Choose a cubic $C$ which intersects $L _ { 1 }$ and $L _ { 2 }$ at $P _ { 3 }$ with multiplicity one and which is tangent to each $L _ { i }$ at a point $P _ { i }$ (with multiplicity two).
The pencil $\mathcal { P }$ generated by $B = 3 L _ { 1 } + 3 L _ { 2 }$ and $2 C$ is a Halphen pencil of index two and it yields a fiber of type $I I I ^ { * }$ in the corresponding rational elliptic surface.

Concretely, we blow-up P2 at the base points P (1)1 , P (2)1 , P (3)1 , P (1)2 , P (2)2 , P (3)2 , of $\mathcal { P }$ so that we obtain the following (dual) configuration of rational curves:

![](images/0f93880ff3c6c384c6468c99a00a8f38994a1799dd82af7bff893a23544fcbff.jpg)

If we take $B$ and $C$ as in the picture below, we obtain a rational elliptic surface whose Jacobian is the surface $X _ { 3 2 1 }$ in Miranda and Persson’s list [37].

![](images/563f3f88af9f25f2a04420c6e50ea80de8035b19199bd12e8d9a62c1ec9378eb.jpg)\
Figure 6. The two generators of $\mathcal { P }$ yielding a fiber of type $I I I ^ { * }$ and a multiple fiber of type $I _ { 2 }$

† Example 7.49 (A triple line, a double line and another line).
Let $C$ be a smooth cubic.
Let $L _ { 1 }$ be an inflection line of $C$ at a point $P _ { 1 }$ and choose a line $L _ { 2 }$ through $P _ { 1 }$ which is tangent to $C$ at another point $P _ { 2 }$ . Let $L _ { 3 }$ be any line through $P _ { 2 }$ which intersects $C$ at another two points, say $P _ { 3 }$ and $P _ { 4 }$ .

Then the pencil $\mathcal { P }$ generated by $B = 3 L _ { 1 } + L _ { 2 } + 2 L _ { 3 }$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I I I ^ { * }$ in the associated rational elliptic surface.

Concretely, we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $C$ is the cubic given by

$$
y ^ { 2 } z = x ( x - z ) ( x - \alpha \cdot z ) \qquad \alpha \in \mathbb { C } \backslash \{ 0 , 1 \}
$$

we can let $L _ { 1 }$ be the line $z = 0$ (hence $P _ { 1 } = ( 0 : 1 : 0 ) ,$ and we can choose $L _ { 2 }$ to be either one of the lines $x = 0 , x - z = 0$ or $x - \alpha \cdot z = 0$ . If we choose $L _ { 2 }$ as $x = 0$ , then $P _ { 2 } = ( 0 : 0 : 1 )$ and we can let $L _ { 3 }$ be the line $y = 0$ .

Now, if we blow-up P2 at the nine base points P (1)1 , $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 5 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) }$ P (1)4 we obtain the following (dual) configuration of rational curves:

![](images/2c701737bfb1297a71d6fe93a713e2d6647bb8a3db20de61219d452a4335d001.jpg)

† Example 7.50 (A triple line, a double line and another line concurrent at a point).
Consider three lines $L _ { 1 } , L _ { 2 }$ and $L _ { 3 }$ concurrent at a point $P _ { 1 }$ and choose a cubic $C$ as in the picture below

![](images/99397d464d68bf9f6a1958869a1358db6525d0f6cb55ab4de41cc9127612b143.jpg)\
Figure 7. The two generators of $\mathcal { P }$ yielding a fiber of type $I I I ^ { * }$ and a multiple fiber of type $I _ { 0 }$

That is, choose a cubic $C$ so that $C$ is tangent to $L _ { 1 }$ at $P _ { 1 }$ with full multiplicity, $C$ is tangent to $L _ { 2 }$ at a point $P _ { 2 } ( \neq P _ { 1 } )$ (with multiplicity two) and it intersects $L _ { 3 }$ at two other points $P _ { 3 }$ and $P _ { 4 }$ .

The pencil $\mathcal { P }$ generated by $B = L _ { 1 } + 3 L _ { 2 } + 2 L _ { 3 }$ and $2 C$ is a Halphen pencil of index two and such pencil yields a fiber of type $I I I ^ { * }$ in the associated rational elliptic surface.

Concretely, we blow-up P2 at the base points P (1), P (2), P (3), P (4), P (1), P (2), P (3), P (1), of $\mathcal { P }$ so that we obtain the following (dual) configuration of rational curves:

![](images/97469e675a90bc24cc54c5a15f5d6214b53768352d0cc693f5956f221434b48b.jpg)

$\dagger$ Example 7.51 (A triple line, a conic and a line).
Let $Q$ be a (smooth) conic.
Choose a point $P _ { 1 }$ in $Q$ and let $L _ { 1 }$ be the tangent line to $Q$ at $P _ { 1 }$ . Choose two other points in $Q$ , say $P _ { 2 }$ and $P _ { 3 }$ , and let $L _ { 2 }$ be the line joining them.
Let $P _ { 4 }$ be the intersection point between $L _ { 1 }$ and $L _ { 2 }$ . We can construct a cubic $C$ through these four points so that $C$ is tangent to $Q$ (resp.
$L _ { 1 }$ ) at $P _ { 1 }$ with multiplicity four (resp.
two).

The pencil $\mathcal { P }$ generated by $B = 3 L _ { 1 } + Q + L _ { 2 }$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I I I ^ { * }$ in the corresponding rational elliptic surface.

Concretely, we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $Q$ is the conic given by $x ^ { 2 } + y z = 0$ and we have $P _ { 1 } = ( 0 : 1 : 0 ) , P _ { 2 } = ( - 1 : - 1 : 1 )$ and $P _ { 3 } = ( 0 : 0 : 1 )$ . Then $L _ { 1 }$ is the line $z = 0$ , $L _ { 2 }$ is the line $x + y = 0 , P _ { 4 } = ( - 1 : 1 : 0 )$ and $C$ is the cubic given by

$$
( x + z ) x z + ( x ^ { 2 } + y z ) ( x + y ) = 0
$$

If we blow-up $\mathbb { P } ^ { 2 }$ at the nine base points $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 5 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 1 ) } , P _ { 4 } ^ { ( 2 ) }$ P (5)1 we obtain the following (dual) configuration of rational curves:

![](images/87159c808cce614af9db9a8adc9cb71e0ba303240565bfd91c058cf41242ddee.jpg)

$\dagger$ Example 7.52 (A triple line and a cubic).
Let $D : d = 0$ be a nodal cubic and let $P _ { 1 }$ denote its node.
Let $P _ { 2 }$ be a point in $\boldsymbol { D }$ which is not a flex and let $L : l = 0$ denote the tangent line to $D$ at $P _ { 2 }$ . Let $P _ { 3 }$ be the third intersection point between $L$ and $\boldsymbol { D }$ and let $L ^ { \prime } : l ^ { \prime } = 0$ denote the line joining $P _ { 1 }$ and $P _ { 3 }$ .

Then the cubic $C$ given by ${ l ^ { 2 } l ^ { \prime } + d = 0 }$ is such that the intersection multiplicity of $D$ and $C$ at $P = P _ { 2 }$ (resp.
$P = P _ { 3 }$ ) is 4 (resp.
3). Moreover, by construction, the node $P _ { 1 }$ lies in $C$ .

Concretely, if $D$ is the nodal cubic given by $y ^ { 2 } z = x ^ { 2 } ( x + z )$ we have that $P _ { 1 } = ( 0 : 0 : 1 )$ and we can let $P _ { 2 } = ( 1 : 0 : - 1 )$ so that $L$ is the line $x + z = 0$ . Then $P _ { 3 } = ( 0 : 1 : 0 )$ and $L ^ { \prime }$ is the line $x = 0$ . Thus, $C$ is the cubic given by

$$
z ( y ^ { 2 } + x ^ { 2 } + x z ) = 0
$$

Note that $C$ consists of a line ( $z = 0$ ) and a conic $( y ^ { 2 } + x ^ { 2 } + x z = 0 )$ ). Moreover, the line is an inflection line of $D$ and the node $P _ { 1 }$ lies in the conic.

Now, the pencil $\mathcal { P }$ generated by $B = 3 L + D$ and $2 C$ is a Halphen pencil of index two and the associated rational elliptic surface has a fiber of type $I I I ^ { * }$ .

More precisely, blowing-up $\mathbb { P } ^ { 2 }$ at $P _ { 1 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 1 ) } , \ldots , P _ { 2 } ^ { ( 5 ) } , P _ { 3 } ^ { ( 1 ) } , \ldots , P _ { 3 } ^ { ( 3 ) }$ we obtain the following (dual) configuration of rational curves:

![](images/3a7aafbc854ae2b74dc88bdfec9a45550071fb354a6e5914f79687f44f600060.jpg)

$\dagger$ Example 7.53 (A line with multiplicity four and a conic).
Consider either a smooth or nodal cubic $C$ . Choose smooth points $P _ { 1 } , P _ { 2 } \in C$ so that there exists a conic $Q$ which is tangent to $C$ at $P _ { 1 }$ (resp.
$P _ { 2 }$ ) with multiplicity 4 (resp.
2). Let $L$ be the line joining $P _ { 1 }$ and $P _ { 2 }$ and let $P _ { 3 }$ be the third intersection point between $L$ and $C$ . Then the pencil $\mathcal { P }$ generated by $B = Q + 4 L$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I I I ^ { * }$ in the associated rational elliptic surface.

For instance, consider the cubic $C$ given by $x ^ { 2 } z + ( x ^ { 2 } + y z ) ( y + z ) = 0$ and let $P _ { 1 } = ( 0 : 1 : 0 )$ and $P _ { 2 } = ( 0 : 0 : 1 )$ . Then $L : x = 0$ and $P _ { 3 } = ( 0 : 1 : - 1 )$ and we can take $Q : x ^ { 2 } + y z = 0$ .

Now, if we blow-up $\mathbb { P } ^ { 2 }$ at the nine base points $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 4 ) } , P _ { 2 } ^ { ( 1 ) } , \ldots , P _ { 2 } ^ { ( 3 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) }$ P (3)2 we obtain the following (dual) configuration of rational curves:

![](images/7969cefbf737de8654b784c4b4af5a720cd950c4d1f6bfc57a8d9bc07362114e.jpg)

$\dagger$ Example 7.54 (A line with multiplicity four and two other lines).
Consider either a smooth or nodal cubic $C$ and let $P _ { 4 }$ be a flex point of $C$ . We can always choose two lines $L _ { 1 }$ and $L _ { 2 }$ through $P _ { 4 }$ which are tangent to $C$ at two other points $P _ { 1 }$ and $P _ { 2 }$ , respectively.
Moreover, if $L _ { 3 }$ is the line joining $P _ { 1 }$ and $P _ { 2 }$ , then $C$ intersects $L _ { 3 }$ at a third point $P _ { 3 }$ and we have that the pencil $\mathcal { P }$ generated by $B = L _ { 1 } + L _ { 2 } + 4 L _ { 3 }$ and $2 C$ is a Halphen pencil of index two with base points

$$
P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 3 ) } , P _ { 2 } ^ { ( 1 ) } , \ldots , P _ { 2 } ^ { ( 3 ) } , P _ { 3 } ^ { ( 1 ) } , P _ { 3 } ^ { ( 2 ) } , P _ { 4 } ^ { ( 1 ) }
$$

Blowing-up $\mathbb { P } ^ { 2 }$ at these nine base points yields a fiber of type $I I I ^ { * }$ in the associated rational elliptic surface.
Explicitly, we obtain the following (dual) configuration of rational curves:

![](images/6fbefd80a49ab38e4288f77c13ae9f0640570cb6170846ecda2a7ba92183a687.jpg)

Note that, concretely, we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $C$ is the cubic given by

$$
y ^ { 2 } z = x ( x - z ) ( x - \alpha \cdot z ) \qquad \alpha \in \mathbb { C } \backslash \{ 0 , 1 \}
$$

we can let $P _ { 4 } = ( 0 : 1 : 0 )$ and we can choose $L _ { 1 }$ and $L _ { 2 }$ to be the lines $x = 0$ and $x - z = 0$ .\
Then $P _ { 1 } = ( 0 : 0 : 1 ) , P _ { 2 } = ( 1 : 0 : 1 ) , L _ { 3 }$ is the line $y = 0$ and $P _ { 3 } = ( \alpha : 0 : 1 )$ .

7.8. Type $I I ^ { * }$ . We now construct all possible examples of Halphen pencils of index two that yield a fiber of type $I I ^ { * }$ in the corresponding rational elliptic surface (Theorem 5.15).

Example 7.55 (A triple conic [16]). We begin with an example of a rational elliptic surface whose Jacobian is the surface $X _ { 2 1 1 }$ in Miranda and Persson’s list [37].

Let $C$ be a cubic with a node and let $P _ { 0 }$ be an inflection point of $C$ that we take as the identity for the group law.
Choose another point $P$ in $C$ satisfying $6 P = P _ { 0 }$ . Then there exists a conic $Q$ tangent to $C$ at $P$ with multiplicity 6 and to the pencil generated by $B = 3 Q$ and $2 C$ we can associate a rational elliptic fibration $Y  \mathbb { P } ^ { 1 }$ of index two with $I I ^ { * } + { } _ { 2 } I _ { 1 } + I _ { 1 }$ singular fibers.

Concretely, we blow-up $\mathbb { P } ^ { 2 }$ at the nine points $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 9 ) }$ where $P _ { 1 } ^ { ( 1 ) } = P$ . The strict transform of $C$ is the multiple fiber and the strict transform of $Q$ is the component of multiplicity 3 in the $I I ^ { * }$ fiber that intersects the component of multiplicity 6.

More precisely, we get the following (dual) configuration of rational curves:

![](images/d0db72a7b720958678fe42e06d1f12d8689ee286899404e194fd0a1597ec0164.jpg)

† Example 7.56 (Two triple lines).
Let $C$ be either a smooth or nodal cubic.
Let $L _ { 1 }$ be an inflection line of $C$ at a point $P _ { 1 }$ and let $L _ { 2 }$ be a line through $P _ { 1 }$ which is tangent to $C$ at another point $P _ { 2 }$ .

Then the pencil $\mathcal { P }$ generated by $B = 3 L _ { 1 } + 3 L _ { 2 }$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I I ^ { * }$ in the associated rational elliptic surface.

Concretely, (if $C$ is smooth) we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $C$ is the cubic given by

$$
y ^ { 2 } z = x ( x - z ) ( x - \alpha \cdot z ) \qquad \alpha \in \mathbb { C } \backslash \{ 0 , 1 \}
$$

e can let $L _ { 1 }$ be the line $z = 0$ (hence $P _ { 1 } = ( 0 : 1 : 0 ) )$ and we can choose $L _ { 2 }$ to be either ne of the lines $x = 0 , x - z = 0$ or $x - \alpha \cdot z = 0$ .

If we choose $L _ { 2 }$ as $x = 0$ , then $P _ { 2 } = ( 0 : 0 : 1 )$ and, similarly, if we take $L _ { 2 }$ as $x - z = 0$ (resp.
$x - \alpha \cdot z = 0$ ), then $P _ { 2 } = ( 1 : 0 : 1 )$ (resp.
$P _ { 2 } = ( \alpha : 0 : 1 ) )$ .

In any case we blow-up $\mathbb { P } ^ { 2 }$ at the nine base points $P _ { 1 } ^ { ( 1 ) } , . . . , P _ { 1 } ^ { ( 6 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) } , P _ { 2 } ^ { ( 3 ) }$ and we obtain the following (dual) configuration of rational curves:

![](images/e61ac9ec1da021263c6f88d1e5535fe03b8217a73af9268e79af1c41c974f1ee.jpg)

† Example 7.57 (A triple line and a cubic).
Let $D : d = 0$ be a nodal cubic and let $P _ { 1 }$ denote its node.
Let $L : l = 0$ be an inflection line of $\boldsymbol { D }$ and denote the flex point by $P _ { 2 }$ . Let $L ^ { \prime } : l ^ { \prime } = 0$ be the line joining $P _ { 1 }$ and $P _ { 2 }$ .

Then the cubic $C$ given by $l ^ { 2 } l ^ { \prime } + d = 0$ is such that the intersection multiplicity of $D$ and $C$ at $P _ { 2 }$ is 7 and, by construction, the node $P _ { 1 }$ lies on it.
We also have that $L$ is also an inflection line of $C$ at $P _ { 2 }$ .

Concretely, we can choose as $\boldsymbol { D }$ the nodal cubic given by $y ^ { 2 } z = x ^ { 2 } ( x + z )$ , then $P _ { 1 } = ( 0 :$ $0 : 1 )$ and we can choose $L$ to be the line $z = 0$ so that $P _ { 2 } = ( 0 : 1 : 0 )$ . Then $L ^ { \prime }$ is the line $x = 0$ and $C$ has equation

$$
z ^ { 2 } x + y ^ { 2 } z - x ^ { 3 } - x ^ { 2 } z = 0
$$

Now, the pencil $\mathcal { P }$ generated by $B = D + 3 L$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I I ^ { * }$ in the associated rational elliptic surface.

If we blow-up $\mathbb { P } ^ { 2 }$ at the nine base points $P _ { 1 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 1 ) } , . . . , P _ { 2 } ^ { ( 8 ) }$ (2 then we obtain the following (dual) configuration of rational curves:

![](images/91b676d7551f771320bcc088d356194d33a68b6deb6f9fa8227a425dea20ef08.jpg)

Example 7.58 (A line with multiplicity four and a conic).
Let $C$ be either a smooth or nodal cubic.
Choose a sextactic point $P _ { 1 } \in C$ (see Definition 7.32). And let $Q$ be the corresponding osculating conic at $P _ { 1 }$ . Choose a line $L$ which is tangent to both $Q$ and $C$ at $P _ { 1 }$ and let $P _ { 2 }$ be the third point of intersection between $L$ and $C$ . Then the pencil $\mathcal { P }$ generated by $B = Q + 4 L$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I I ^ { * }$ i n the associated rational elliptic surface.

For instance, consider the cubic $C$ given by

$$
- 3 x ^ { 3 } + x z ^ { 2 } + y ^ { 2 } z + 2 x y ^ { 2 } = x ^ { 3 } + ( y ^ { 2 } - 2 x ^ { 2 } + x z ) \cdot ( 2 x + z ) = 0
$$

Let $P _ { 1 } = ( 0 : 0 : 1 )$ , let $Q : y ^ { 2 } - 2 x ^ { 2 } + x z = 0$ and let $L : x = 0$ . Then the intersection multiplicity of $Q$ and $C$ at $P _ { 1 }$ is 6 and we have that $P _ { 2 } = ( 0 : 1 : 0 )$ is a flex point with inflection line $2 x + z = 0$ .

Now, if we blow-up $\mathbb { P } ^ { 2 }$ at $P _ { 1 } ^ { ( 1 ) } , . . . , P _ { 1 } ^ { ( 7 ) } , P _ { 2 } ^ { ( 1 ) } , P _ { 2 } ^ { ( 2 ) }$ we obtain the following (dual) configuration of rational curves:

![](images/c5e0e01f9b969c86dbd569a293e20e9ecb2aae3e0242086de8a5e807bec48b62.jpg)

$\dagger$ Example 7.59 (A line with multiplicity five and another line).
Consider either a smooth or nodal cubic $C$ and let $L _ { 1 }$ be an inflection line of $C$ at a point $P _ { 1 }$ . We can always choose another line $L _ { 2 }$ through $P _ { 1 }$ which is tangent to $C$ at another point $P _ { 2 }$ . And the pencil $\mathcal { P }$ generated by $B = 5 L _ { 2 } + L _ { 1 }$ and $2 C$ is a Halphen pencil of index two which yields a fiber of type $I I ^ { * }$ in the associated rational elliptic surface.

Concretely, (if $C$ is smooth) we can choose coordinates in $\mathbb { P } ^ { 2 }$ so that $C$ is the cubic given by

$$
y ^ { 2 } z = x ( x - z ) ( x - \alpha \cdot z ) \qquad \alpha \in \mathbb { C } \backslash \{ 0 , 1 \}
$$

we can let $L _ { 1 }$ be the line $z = 0$ (hence $P _ { 1 } = ( 0 : 1 : 0 ) ,$ and we can choose $L _ { 2 }$ to be either one of the lines $x = 0 , x - z = 0$ or $x - \alpha \cdot z = 0$ .

If we choose $L _ { 2 }$ as $x = 0$ , then $P _ { 2 } = ( 0 : 0 : 1 )$ and, similarly, if we take $L _ { 2 }$ as $x - z = 0$ (resp.
), then $P _ { 2 } = ( 1 : 0 : 1 )$ (resp.
$P _ { 2 } = ( \alpha : 0 : 1 ) )$ .

− ·In any case we blow-up $\mathbb { P } ^ { 2 }$ at $P _ { 1 } ^ { ( 1 ) } , \ldots , P _ { 1 } ^ { ( 4 ) } , P _ { 2 } ^ { ( 1 ) } , \ldots , P _ { 2 } ^ { ( 5 ) }$ and we obtain the following (dual) configuration of rational curves:

![](images/b1ebe106107fa97ac6bd9eef5b0ce20512f900da5f6459043b57a8d38017b3c6.jpg)

# References

[1] D. Abramovich and A. Vistoli.
Complete moduli for fibered surfaces.
In Recent progress in intersection theory (Bologna, 1997), Trends Math., pages 1–31. Birkhäuser Boston, Boston, MA, 2000.\
[2] V. Alexeev and V. V. Nikulin.
Chapter 2. General Theory of DPN surfaces and K3 surfaces with nonsymplectic involution, volume Volume 15 of MSJ Memoirs, pages 20–49. The Mathematical Society of Japan, Tokyo, Japan, 2006.\
[3] K. Ascher and D. Bejleri.
Moduli of weighted stable elliptic surfaces and invariance of log plurigenera.
https://arxiv.org/pdf/1702.06107v3.pdf, 05 2018.\
[4] K. Ascher and D. Bejleri.
Moduli of fibered surface pairs from twisted stable maps.
Math.
Ann., 374(1- 2):1007–1032, 2019.\
[5] W. Barth, C. Peters, and A. van de Ven.
Compact Complex Surfaces.
Ergebnisse der Mathematik und ihrer Grenzgebiete.
3. Folge / A Series of Modern Surveys in Mathematics.
Springer Berlin Heidelberg, 2012.\
[6] E. Bombieri and J. Bourgain.
A problem on sums of two squares.
Int.
Math.
Res.
Not.
IMRN, (11):3343– 3407, 2015.\
[7] S. Cantat and I. Dolgachev.
Rational surfaces with a large group of automorphisms.
Journal of the American Mathematical Society, 25(3):863–905, 2012.\
[8] A. Cayley.
On the conic of five-pointic contact at any point of a plane curve.
Philosophical Transactions of the Royal Society of London, 149:371–400, 1859.\
[9] A. Cayley.
On the sextactic points of a plane curve.
Philosophical Transactions of the Royal Society of London, 155:545–578, 1865.\
[10] I. Cheltsov.
Worst singularities of plane curves of given degree.
The Journal of Geometric Analysis, 27(3):2302–2338, Jul 2017.\
[11] I. Cheltsov and I. Karzhemanov.
Halphen pencils on quartic threefolds.
Adv.
Math., 223(2):594–618, 2010.\
[12] I. Cheltsov and J. Park.
Halphen pencils on weighted Fano threefold hypersurfaces.
Cent.
Eur.
J. Math., 7(1):1–45, 2009.\
[13] I. Dolgachev and F. Cossec.
Enriques Surfaces I, volume 76 of Progress in Mathematics.
Birkhäuser, 1989.\
[14] I. Dolgachev and D-Q. Zhang.
Coble rational surfaces.
American Journal of Mathematics, 123(1):79–114, 2001.\
[15] Y. Fujimoto.
On rational elliptic surfaces with multiple fibers.
Publications of the Research Institute for Mathematical Sciences, 26:1–13, 1990.\
[16] Y. Fujimoto.
On explicit constructions of rational elliptic surfaces with multiple fibers.
Journal of Mathematics of Kyoto University, 38(3):517–523, 1998.\
[17] W. Fulton.
Introduction to intersection theory in algebraic geometry, volume 54 of CBMS Regional Conference Series in Mathematics.
Published for the Conference Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI, 1984.\
[18] W. Fulton and R. Weiss.
Algebraic Curves: An Introduction to Algebraic Geometry.
Advanced book classics.
Addison-Wesley Publishing Company, Advanced Book Program, 1989.\
[19] D. Fusi.
Construction of linear pencils of cubic curves with Mordell-Weil rank six and seven.
Comment.
Math.
Univ. St. Pauli, 55(2):195–205, 2006.\
[20] M. A. Gradolato and E. Mezzetti.
Curves with nodes, cusps and ordinary triple points.
Ann.
Univ. Ferrara Sez.
VII (N.S.), 31:23–47 (1986), 1985.\
[21] G-H Halphen.
Sur les courbes planes du sixième degré à neuf points doubles.
Bulletin de la Société Mathématique de France, 10:162–172, 1882.\
[22] G. Heckman and E. Looijenga.
The moduli space of rational elliptic surfaces.
In Algebraic Geometry 2000, Azumino, pages 185–248, Tokyo, Japan, 2002. Mathematical Society of Japan.\
[23] P-L. Kang.
A note on the variety of plane curves with nodes and cusps.
Proceedings of the American Mathematical Society, 106(2):309–312, 1989.\
[24] T. Karayayla.
The classification of automorphism groups of rational elliptic surfaces with section.
Adv.
Math., 230(1):1–54, 2012.\
[25] T. Karayayla.
Automorphism groups of rational elliptic surfaces with section and constant $J .$ -map.
Cent.
Eur.
J. Math., 12(12):1772–1795, 2014.\
[26] Y. Kimura.
K3 surfaces without section as double covers of Halphen surfaces, and F-theory compactifications.
PTEP. Prog.
Theor.
Exp.
Phys., (4):043B06, 13, 2018.\
[27] Y. Kimura.
$S U ( n ) \times \mathbb { Z } _ { 2 }$ in F-theory on K3 surfaces without section as double covers of Halphen surfaces.
https://arxiv.org/abs/1806.01727v2, 2018.\
[28] K. Kodaira.
On the structure of compact complex analytic surfaces, i. American Journal of Mathematics, 86(4):751–798, 1964.\
[29] K. Kodaira.
On the structure of compact complex analytic surfaces, ii.
American Journal of Mathematics, 88(3):682–721, 1966.\
[30] J. Kollár.
Singularities of pairs.
In Algebraic geometry—Santa Cruz 1995, volume 62 of Proc.
Sympos.
Pure Math., pages 221–287. Amer.
Math.
Soc., Providence, RI, 1997.\
[31] A. Laface.
Private Communication.\
[32] A. Laface and D. Testa.
On minimal rational elliptic surfaces.
https://arxiv.org/abs/1502.00275„ 02 2015.\
[33] R. Miranda.
On the stability of pencils of cubic curves.
American Journal of Mathematics, 102(6):1177– 1202, 1980.\
[34] R. Miranda.
The moduli of Weierstrass fibrations over $\mathbb { P } ^ { 1 }$ . Mathematische Annalen, 255:379–394, 09 1981.\
[35] R. Miranda.
The basic theory of elliptic surfaces: notes of lectures.
ETS Editrice, 1989.\
[36] R Miranda.
Persson’s list of singular fibers for a rational elliptic surface.
Mathematische Zeitschrift, 205(2):191–212, 1990.\
[37] R. Miranda and U. Persson.
On extremal rational elliptic surfaces.
Mathematische Zeitschrift, 193(4):537–558, Dec 1986.\
[38] A. Néron.
Modèles minimaux des variétés abéliennes sur les corps locaux et globaux.
Publications Mathématiques de l’IHÉS, 21:5–128, 1964.\
[39] V. Pastro.
Construction of rational elliptic surfaces with Mordell-Weil rank four.
Comment.
Math.
Univ. St. Pauli, 61(1):29–42, 2012.\
[40] U. Persson.
Configurations of Kodaira fibers on rational elliptic surfaces.
Math.
Z., 205(1):1–47, 1990.\
[41] H. Sakai.
Rational surfaces associated with affine root systems and geometry of the Painlevé equations.
Comm.
Math.
Phys., 220(1):165–229, 2001.\
[42] C. Salgado.
Construction of linear pencils of cubics with Mordell-Weil rank five.
Comment.
Math.
Univ. St. Pauli, 58(2):95–104, 2009.\
[43] M. Schütt and T. Shioda.
Elliptic surfaces.
In Algebraic Geometry in East Asia — Seoul 2008, pages 51–160, Tokyo, Japan, 2010. Mathematical Society of Japan.\
[44] A. Zanardini.
Stability of pencils of plane curves and moduli of rational elliptic surfaces.
In preparation.\
[45] D.-Q. Zhang.
Quotients of $K 3$ surfaces modulo involutions.
Japan.
J. Math.
(N.S.), 24(2):335–366, 1998.
