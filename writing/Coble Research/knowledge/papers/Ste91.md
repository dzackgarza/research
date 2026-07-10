---
title: Compactifications of the period space of Enriques surfaces. I
authors:
- Department Of Mathematics
- Columbia University
- New York
- Ny 10027
- Usa
year: 1991
bibkey: Ste91
tags:
- paper
- extraction
abstract: |
  
---

# Compactifications of the period space of Enriques surfaces Part I

Hans Sterk\*\*\*

Department of Mathematics,Columbia University,New York,NY 10027,USA

Received April 27,1989,in final form November 5,1990

# Introduction

This paper is the first of two papers dealing with compactifications of the period space of Enriques surfaces which are of geometric intercst.
The motivation for this work comes from two origins.
One is the work of Shah [24] on projective degenerations of Enriques surfaces.The other is the work of Looijenga [14,15] on new compactification techniques for locally symmetric varieties.
Shah's paper can be interpreted as dealing with the moduli aspect (it is phrased in terms of Mumford's geometric invariant theory [16]),whereas Looijenga's work refers to the period space aspect.
Our ultimate aim then is to describe a compactification of the period space of Enriques surfaces which accounts for Shah's results.
This turns out to be a normalized blow-up of the Satake-Baily-Borel compactification along the closure of the divisor describing periods of ‘special’ Enriques surfaces (see $\ S 2$ for the notion of a ‘special Enriques surface).

The period space which we use is of the form $D / \Gamma$ where $D$ is a bounded symmetric domain of type IV and dimension 10 and $\Gamma$ is some arithmetic group (see $\ S 2 )$ .
Such a situation also occurred in the work of Horikawa [11,12] and Namikawa [17] on Enriques surfaces.
It should be pointed out, however, that our group is smaller than theirs.
The reason is that we wish to take into account the specific geometric setting of Shah's approach i.e.,we think of our Enriques surfaces as being endowed with an (almost） polarization (of degree 2),which realizes the $K 3$ cover as the minimal resolution of a branched double cover of $\begin{array} { r } { \sum _ { 0 } = \mathbf { P } ^ { 1 } \times \mathbf { P } ^ { 1 } } \end{array}$ or a quadratic cone $\Sigma _ { 2 } ^ { 0 } \subset \mathbf { P } ^ { 3 }$ .The degree of the resulting map between the two spaces, $2 ^ { 7 } \cdot 1 7 \cdot 3 1$ (S2),expresses the fact that a ‘general' Enriques surface (in the sense of [2])\_can be given,up to automorphisms,an (almost） polarization of degree 2 in $2 ^ { 7 } \cdot 1 7 \cdot 3 1$ different ways.
We then expect this geometric background to be at least partially reflected in, for instance, the Satake-Baily-Borel compactification of the period space ([21,22] and [1]).We refer to $\ S 5$ for the first relation.
Indeed, in part I we shall confine ourselves to this Satake-Baily-Borel compactification, postponing a more refined analysis of the results of Shah in terms of the period space to part II.
We remark here that it is easily deduced from Shah's work that we should be looking for a compactification of the period space which is actually bigger than the Satake-Baily-Borel compactification (and yet not of toroidal type).

In $\ S 1$ we collect some definitions and notations.
In $\ S 2$ we give a description of the period space as a quotient of a bounded symmetric domain of type IV by a certain arithmetic group.

To determine the boundary components of the Satake-Baily-Borel compactification we need some arithmetical results, due to Looijenga,which are stated in $\ S 3 ,$ ,as well as several corollaries.

Then in $\ S 4$ we actually compute the boundary components.
An important tool here is Vinberg's theory of reflection groups in hyperbolic space [26].The incidence relations between the boundary components is described by the diagram in (4.4).

Finally, in $\ S 5$ we indicate a relation between Shah's list of degenerations and our list of boundary components.
Our method involves the use of ‘stable $K 3$ surfaces'as introduced by Friedman [9,10] and (part of) the Clemens-Schmid exact sequence.

# 1 Notations and preliminaries

1.1If $\Lambda$ is a $\mathbf { z }$ -module of finite rank,then we denote by $\Lambda _ { f }$ the quotient by its torsion subgroup.
A lattice is a free $\mathbf { Z }$ -module of finite rank endowed with an integral symmetric bilinear form,which we usually denote by（，).
If $\Lambda$ is a lattice and for all $x \in \Lambda \ ( x , x )$ is even, then the lattice $\Lambda$ is called even; otherwise it is called odd.The lattice $\Lambda$ is called positive (resp.negative) definite if $( x , x ) > 0$ (resp.
$( x , x ) < 0 )$ for all $x \in \Lambda - \{ 0 \}$ The signature of $\Lambda$ is the pair of integers $( p , n )$ where $p$ (resp.n) is the maximal possible rank of a positive (resp.
negative) definite sublattice of $\Lambda$ ，We have a natural homomorphism (the correlation morphism） from $\Lambda$ to its dual $\Lambda ^ { * } : = \operatorname { H o m } _ { \mathbf { Z } } ( \Lambda , \mathbf { Z } )$ defined by $x \mapsto ( x , - )$ .If this map is injective we say that $\Lambda$ is nondegenerate.In this case $\Lambda$ is identified with a submodule of $\Lambda ^ { \ast }$ .The bilinear form on $\Lambda$ extends to $\Lambda ^ { * }$ and although it is usually not $\mathbf { Z }$ -valued we nevertheless usually refer to $\Lambda ^ { * }$ with this bilinear form as the dual lattice.In case $\Lambda ( \ne 0 )$ is actually identified with $\Lambda ^ { * }$ we call $\Lambda$ unimodular (equivalently $| \operatorname* { d e t } ( ( v _ { i } , v _ { j } ) ) | = 1$ ，where $v _ { 1 } , \ldots , v _ { m }$ is a basis of $\Lambda )$ .By $\Lambda ( n )$ ,for $\pmb { n } \in \mathbb { N }$ ，we mean the $\mathbf { z }$ -module $\Lambda$ with bilinear form $n ( \mathbf { \partial \phi } , \mathbf { \partial \phi } ) . \mathbf { A }$ sublattice $K \subset \Lambda$ is called isotropic if the restriction of the bilinear form to $K$ vanishes identically.
The sublattice $\kappa$ is called primitive if $\Lambda / K$ is torsion free.
For a lattice $\pmb { \Lambda }$ we denote by $O ( \Lambda )$ the orthogonal group of $\Lambda$ and by $I _ { m } ( \Lambda )$ the set of primitive rank $m$ isotropic sublattices of $\Lambda$ For $\Lambda$ nondegenerate we set

$$
{ \cal O } ^ { \bullet } ( \Lambda ) : = \{ g \in { \cal O } ( \Lambda ) : g \quad \mathrm { a c t s ~ a s ~ i d e n t i t y ~ o n } \quad \Lambda ^ { \bullet } / \Lambda \} .
$$

1.2A $K 3$ surfaces is a compact connected complex analytic surface $X$ with dim $H ^ { 1 } ( X , { \mathcal { O } } ) = 0$ and trivial canonical bundle.
An Enriques surface is a compact connected complex analytic surface $Y$ such that dim $H ^ { 1 } ( Y , \mathcal { O } ) \dot { = } 0$ ， $K _ { Y } \not \sim 0$ and $2 K _ { Y } \sim 0$ where $K _ { Y }$ denotes the canonical divisor.It is also characterized by the fact that its universal (double) cover is a $K 3$ surface.
For a $K 3$ surface $X$ (resp.
Enriques surface $Y$ ）we have $H ^ { 2 } ( X ; \mathbf { Z } ) \cong \mathbf { Z } ^ { 2 2 }$ (resp.
$H ^ { 2 } ( Y ; { \mathbf { Z } } ) \cong { \mathbf { Z } } ^ { 1 0 } \oplus { \mathbf { Z } } _ { 2 } )$ and the cup product provides $H ^ { 2 } ( X ; \mathbf { Z } )$ (resp.
$H ^ { 2 } ( Y ; \pmb { \mathbb { Z } } ) _ { f } )$ with the structure of an even unimodular latice of signature (3,19) (resp.
(1,9)).
In fact we have

and

$$
\begin{array} { c } { { H ^ { 2 } ( X ; { \bf Z } ) \cong \mathbf { H } ^ { \oplus 3 } \oplus E _ { 8 } ( - 1 ) ^ { \oplus 2 } } } \\ { { { } } } \\ { { H ^ { 2 } ( Y ; { \bf Z } ) _ { f } \cong \mathbf { H } \oplus E _ { 8 } ( - 1 ) } } \end{array}
$$

(as latices), where we have fixed the following notation.

$\mathbf { H } = \mathbf { Z } e \oplus \mathbf { Z } f$ with $( e , e ) = ( f , f ) = ( e , f ) - 1 = 0$ ，the hyperbolic plane.
Notations like $\widetilde { e } , \widetilde { f }$ or $e ^ { \prime } , f ^ { \prime }$ etc. will also be used occasionally to denote the standard basis of $\mathbf { H }$ or $\mathbf { H } ( n )$

$E _ { 8 }$ : root lattce for Dynkin diagram $E _ { 8 }$

$$
\frac { \alpha _ { 1 } \alpha _ { 3 } \alpha _ { 4 } \alpha _ { 5 } \alpha _ { 6 } \alpha _ { 7 } \alpha _ { 8 } } { \alpha _ { 1 } }
$$

Fig.

1.

By $\overline { { \alpha } } _ { 1 }$ …， $\overline { { \alpha } } _ { 8 } \in E _ { 8 }$ we denote the basis of $E _ { 8 }$ such that $( \overleftrightarrow { \boldsymbol { \alpha } } _ { i } , \boldsymbol { \alpha } _ { j } ) = \delta _ { i j }$

We set:

and

$$
\begin{array} { r l } { \dot { \mathbf { \eta } } } & { = \mathbf { H } ^ { \oplus 3 } \oplus E _ { 8 } ( - 1 ) ^ { \oplus 2 } , \quad \mathrm { a n d ~ c a l l ~ i t ~ t h e ~ } K 3 ~ l a t t i c } \\ { \mathbf { \eta } } & { \qquad \quad } \\ { \mathbf { \eta } } & { = \mathbf { H } \oplus E _ { 8 } ( - 1 ) , \quad \mathrm { t h e ~ } E n r i q u e s ~ l a t t i c e . } \end{array}
$$

1.3Involutions induced by (or related to) the covering transformation of the universal cover $\pi : X \to Y$ of an Enriques surface $Y$ will usually be denoted by $I$ or $I ^ { * }$ .Write ${ \cal L } = { \cal M } \oplus { \cal M } \oplus { \bf H }$ and let $I : L \to L$ be the involution defined by

$$
I : ( m , m ^ { \prime } , h ) \mapsto ( m ^ { \prime } , m , - h ) .
$$

This definition is motivated by a result of Horikawa [11],Theorem 5.1,which states that there exists an isometry $\mu : H ^ { 2 } ( X ; \mathbf { Z } ) \to L$ satisfying $I \circ \mu = \mu \circ I ^ { * }$ .It gives rise to the following commutative diagram

$$
\begin{array} { l l c c c } { { H ^ { 2 } ( X ; { \bf Z } ) } } & { { \stackrel { \sim } { \longrightarrow } } } & { { L } } & { { ( m , m , 0 ) } } \\ { { \uparrow } } & { { } } & { { \uparrow } } & { { \uparrow } } \\ { { H ^ { 2 } ( Y ; { \bf Z } ) _ { f } } } & { { \stackrel { \sim } { \longrightarrow } } } & { { M } } & { { m } } \end{array}
$$

Fix the following notation:

$$
\begin{array} { r l } & { L _ { + } = \big \{ x \in L : I ( x ) = x \big \} = \big \{ ( m , m , 0 ) \in M \oplus M \oplus \mathbf { H } : m \in M \big \} ; } \\ & { L _ { - } = \big \{ x \in L : I ( x ) = - x \big \} = \big \{ ( m , - m , h ) \in M \oplus M \oplus \mathbf { H } : m \in M , h \in \mathbf { H } \big \} . } \end{array}
$$

We have identifications

$$
\begin{array} { l l } { { \varepsilon _ { + } : L _ { + } \to M ( 2 ) } } & { { ( m , m , 0 ) \longleftrightarrow m , } } \\ { { \varepsilon _ { - } : L _ { - } \to { \bf H } \oplus M ( 2 ) } } & { { ( m , - m , h ) \mapsto ( h , m ) . } } \end{array}
$$

In general, a superscript $^ +$ (resp.
$^ -$ ）orsubscript $^ +$ (resp.
$\underline { { \cdot } }$ ） will be used to denote the invariant (resp.anti-invariant) part with respect to some involution (usually $I , I ^ { * }$ etc.).

1.4The quotient $L _ { - } ^ { * } / L _ { - } ( \cong M ( 2 ) ^ { * } / M ( 2 ) )$ isa $\mathbf { Z } / 2$ -module of rank 10 and inherits a $\mathbf { Z } / 2 \mathbf { Z }$ -valued bilinear form（，） given by

$$
( x + L _ { - } , y + L _ { - } ) ^ { \prime } : = 2 ( x , y ) { \bmod { 2 } }
$$

and a nondegenerate quadratic form $q$

$$
q ( x + L _ { - } ) = ( x , x ) { \bmod { 2 } } ,
$$

satisfying

$$
q ( \overline { { { x } } } + \overline { { { y } } } ) = q ( \overline { { { x } } } ) + q ( \overline { { { y } } } ) + ( x , y ) ^ { \prime } \quad ( \overline { { { x } } } = x + L _ { - } , \overline { { { y } } } = y + L _ { - } ) .
$$

Denote by $O ( L _ { - } ^ { \bullet } / L _ { - } , q ) )$ （or $O ( q )$ for short） the group of automorphisms of $L _ { \mathrm { - } } ^ { * } / L _ { \mathrm { - } }$ which respect $q$ .It follows from a result of Nikulin [18],Theorem 1.13.2, that $L _ { - }$ is determined up to isometry by its signature,which is (2,1O),and its quadratic form.
Moreover, the natural maps

$$
O ( L _ { + } ) \to O ( L _ { + } ^ { * } / L _ { + } , q )
$$

and

$$
{ \cal O } ( L _ { - } ) \to { \cal O } ( L _ { - } ^ { * } / L _ { - } , q )
$$

are surjective ([18],Theor.
1.14.2) and from this it follows that every $g \in O ( L _ { - } )$ (resp.
$g \in O ( L _ { + } ) )$ extends to an element of $O ( L )$ commuting with the involution ([19,Prop.
1.1). Note that $L _ { + } ^ { \bullet } / L _ { + } \cong L _ { - } ^ { \bullet } / L _ { - }$

# 2 Description of the period space

Let $Y$ be an Enriques surface and let $\pi : X \to Y$ be its universal $K 3$ cover.
According to results of Horikawa [11] (see also [3],Chap.VIII $\ S 1 8 ]$ we are always in one of the following two situations.

(1) There exists an $I$ -invariant bihomogeneous polynomial of bidegree (4,4) with zero-set $B$ such that $X$ is the minimal resolution of thedoublecovering of $\textstyle \sum _ { 0 }$ ramified over $B$ .We refer to this case as the general case (see [loc. cit.] and the introduction of [24]).  
(2) There exists an $I$ -invariant polynomial of degree 4 in $z _ { 0 } , z _ { 1 } , z _ { 2 } , z _ { 3 }$ defining a curve $\pmb { B }$ on the quadratic cone $\textstyle \sum _ { 2 } ^ { 0 } = \{ z _ { 0 } z _ { 3 } = z _ { 1 } ^ { 2 } \} \subset { \bf P } ^ { 3 }$ ，such that $X$ is the minimalresolutionofthedoublecoverof ${ \boldsymbol { \sum } } _ { 2 } ^ { 0 }$ ramified over $B$ We refer to this case as the special case.

These two kinds of realizations suggest to study Enriques surfaces together with an almost polarization of degree 2 (i.e.a line bundle of self-intersection 2,which intersects any curve nonnegatively).In the general case above, the two rulings of $\Sigma _ { 0 }$ define two elliptic pencils on $X$ and the‘sum'of these gives rise to an almost polarization of degree 2 on $Y$ .
In the special case,the ruling on $\boldsymbol { \sum } _ { 2 } ^ { 0 }$ defines an elliptic pencil on $X$ and over the vertex of ${ \boldsymbol { \Sigma } } _ { 2 } ^ { 0 }$ we find two nodal curves.
The ‘sum’gives rise to an almost polarization of degree 2 on $Y$ .
In particular, Horikawa's results show that any Enriques surface can be endowed with an almost polarization of degree 2.

2.1 Remark.
We can also exploit the geometry of $H ^ { 2 } ( Y ; \mathbf { Z } )$ and $H ^ { 2 } ( X ; \mathbf { Z } )$ to prove the existence of an almost polarization of degree 2 on $Y$ ([25], p.35-37).

The ‘splitting’of the polarization on $X$ we observed is determined by the almost polarization on $Y$ .
To make this more precise, let $\eta _ { Y }$ be an almost polarization of degree 2 on $Y$ .
Choose isometries $\phi _ { Y } : H ^ { 2 } ( Y ; { \bf Z } ) _ { f } \to M$ and $\phi _ { X } : H ^ { 2 } ( X ; \mathbf { Z } ) \to L$ such that the following diagram commutes :

$$
\begin{array} { r l r l } { H ^ { 2 } ( X ; \mathbf { Z } ) } & { { } } & { { \xrightarrow { \phi _ { X } } } } & { } & { { L } } \\ { \pi ^ { * } \uparrow } & { { } } & { } & { { \uparrow } } \\ { H ^ { 2 } ( Y ; \mathbf { Z } ) _ { f } } & { { } } & { { \xrightarrow { \phi _ { Y } } } } & { } & { { M } } \end{array}
$$

and such that $\phi _ { Y } ( \eta _ { Y } ) = e + f$ Except for the last condition,this follows from Horikawa's result mentioned in (1.3).As for the last condition,we note the following.
We have $O ( M ) = \{ \pm 1 \} \cdot W ( M )$ ,where $W ( M )$ is the group generated by reflections in $( - 2 )$ -vectors (see e.g. [26], p.340-341).A Dynkin diagram for $W ( M )$ is given on p.
347 of [loc.cit.].
Any vector of norm 2 is equivalent to one contained in a fundamental domain for $W ( M )$ .Such a vector is a nonnegative linear combination of the weights corresponding to a root basis.
It is easily checked that there is only one possibility, i.e. $O ( M )$ acts transitively on the set of elements of norm 2 in $M$ Moreover,since ${ \cal O } ( M ( 2 ) )  { \cal O } ( M ( 2 ) ^ { \bullet } / M ( 2 ) )$ is surjective,see (1.4),any $g \in O ( M )$ can be lifted to a $\widetilde g \in O ( L )$ commuting with $I$

For later purposes we state here the following definition.

2.2 Definition.
A pair $\boldsymbol { \Phi } = ( \phi _ { X } , \phi _ { Y } )$ of isometries as above will be called a marking for $( Y , \eta _ { Y } )$ 1：

2.3 Proposition.If $( Y , \eta _ { Y } )$ is general,then the eliptic fbrations are given by $| \phi _ { X } ^ { - 1 } ( e , e , 0 ) |$ and $| \phi _ { X } ^ { - 1 } ( f , f , 0 ) |$

Proof.
The orthogonal complement $( e + f ) ^ { \perp }$ splits as $A _ { 1 } ( - 1 ) \oplus E _ { 8 } ( - 1 )$ If $e + f = a + b$ with $a ^ { 2 } = b ^ { 2 } = ( a , b ) - 1 = 0$ ，then it is easily verified that $a - b$ spans the $A _ { 1 } ( - 1 )$ -summand which implies $\{ a , b \} = \{ e , f \}$ So,in fact $e + f$ determines the set $\{ e , f \}$ .Apply this to the images of the two elliptic pencils on $X$ □

In the special case, the linear system $| \phi ^ { - 1 } ( \eta , \eta , 0 ) |$ is of the form $| 2 \overline { { { E } } } ^ { \prime } + \widetilde { A } + \widetilde { A } ^ { \prime } |$ where ${ \overline { { E } } } ^ { \prime }$ is elliptc and $\widetilde { A } , \widetilde { A } ^ { \prime }$ are nodal curves arising from the vertex of ${ \boldsymbol { \Sigma } } _ { 2 } ^ { 0 }$ Reasoning as in the proof of (2.3) yields in this case:

2.4 Proposition.
$I f \left( Y , \eta _ { Y } \right)$ is special, $\overline { { E } } ^ { \prime }$ is an elliptic curve of the elliptic pencil ${ \tilde { A } } , { \tilde { A } } ^ { \prime }$ the two nodal curves,then $\{ ( e , e , 0 ) , ( f , f , 0 ) \} = \{ \phi ( [ \overline { { E } } ^ { \prime } ] ) , \phi ( [ \overline { { E } } ^ { \prime } + \widetilde { A } + \widetilde { A } ^ { \prime } ] ) \}$

2.5 Remark.In [7], Proposition 1.6.1, Cossec shows that $O ( \mathbf { H } ) \oplus E _ { 8 } ( - 1 ) )$ acts transitively on the set of exceptional sequences of length $r < 9$ (an exceptional sequence of length $r > 1$ being a sequence $( f _ { 1 } , \ldots , f _ { r } )$ of $r > 1$ isotropic vectors with $( f _ { i } , f _ { j } ) = 1$ for $i \neq j ,$ .
Implicit in our argument above is a proof for the case $r = 2$

2.6 Remark.
The fact that an element of square 2 determines its decomposition as a sum of two isotropic elements having inner product 1 shows that our notion of an almost polarized Enriques surface of degree 2 is equivalent to Dolgachev's notion of an H-marked Enriques surfaces [8].

Next we define the period point of an almost polarized Enriques surface of degree 2. Let $( Y , \eta _ { Y } )$ be an almost polarized Enriques surface of degree 2 and let $\Phi$ be a marking.
Choose $\omega _ { X } \in H ^ { 2 } ( \Omega _ { X } ^ { 2 } ) - \{ 0 \}$ As $h ^ { 0 } ( Y , \Omega _ { Y } ^ { 2 } ) = 0$ we have $I \omega _ { X } = - \omega _ { X }$ and therefore $\omega _ { X } \in H ^ { 2 } ( X ; \mathbf { C } ) _ { - }$ .The Hodge-Riemann bilinear relations then show that $\phi _ { X , \mathbf { C } } ( \omega _ { X } )$ determines a point in

$$
\Omega _ { - } : = \{ \omega \in \mathbf { P } ( L _ { - } \otimes \mathbf { C } ) : ( \omega , \omega ) = 0 , ( \omega , \overline { { \omega } } ) > 0 \} ,
$$

independent of the choice of $\omega _ { X }$ If $\Phi ^ { \prime } = ( \phi _ { X } ^ { \prime } , \phi _ { Y } ^ { \prime } )$ is another marking, then we find on the level of $M$ ：

$$
( \phi _ { Y } ^ { \prime } ) ^ { - 1 } \circ \phi _ { Y } \in \{ g \in O ( M ) : g ( e + f ) = e + f \}
$$

and on the level of $L$

$$
( \phi _ { X } ^ { \prime } ) ^ { - 1 } \circ \phi _ { X } \in \{ g \in O ( L ) : g \circ I = I \circ g , g ( e + f , e + f , 0 ) = ( e + f , e + f , 0 ) \} .
$$

To get rid of the ambiguities, due to choosing a marking, we therefore divide out by the group $\Gamma$ ，where $\Gamma$ is the image of

$$
\{ g \in O ( L ) : g \circ I = I \circ g , g ( e + f , e + f , 0 ) = ( e + f , e + f , 0 ) \}
$$

in $O ( L _ { - } )$

2.7 Proposition.
This image $\Gamma$ is precisely the set of all $g \in O ( L _ { - } )$ such that the induced map on

$$
L _ { - } ^ { \bullet } / L _ { - } = { \frac { 1 } { 2 } } { \bf H } ( 2 ) / { \bf H } ( 2 ) \oplus { \frac { 1 } { 2 } } E _ { 8 } ( - 2 ) / E _ { 8 } ( - 2 )
$$

respects the decomposition in two summands.

Proof.The isomorphism $L _ { + } ^ { \bullet } / L _ { + } \cong L _ { - } ^ { \bullet } / L _ { - }$ (1.4) arises in the following way.
The correlation morphism $L \to L ^ { * }$ induces isomorphisms $L / L _ { + } \oplus L _ { - } \to L _ { + } ^ { * } / L _ { + }$ and $L / L _ { + } \oplus L _ { - } \to L _ { - } ^ { * } / L _ { - }$ and by composing we find $L _ { + } ^ { * } / L _ { + } \cong L _ { - } ^ { * } / L _ { - }$ If we identify $L _ { + } ^ { * } / L _ { + }$ and $L _ { - } ^ { * } / L _ { - }$ with

$$
\frac { 1 } { 2 } { \bf H } ( 2 ) / { \bf H } ( 2 ) \oplus \frac { 1 } { 2 } E _ { 8 } ( - 2 ) / E _ { 8 } ( - 2 )
$$

in the obvious way, then the isomorphism $L _ { + } ^ { * } / L _ { + } \cong L _ { - } ^ { * } / L _ { - }$ is just the identity.
Suppose now that $g \in O ( L )$ is such that

$$
g \circ I = I \circ g \quad { \mathrm { a n d } } \quad g ( e + f , e + f , 0 ) = ( e + f , e + f , 0 ) ,
$$

then the restriction $g \vert L _ { + }$ stabilizes

$$
e + f \in L _ { + } = \mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 2 )
$$

and

$$
( e + f ) ^ { \perp } = { \bf Z } ( e - f ) \oplus E _ { 8 } ( - 2 ) \cong A _ { 1 } ( - 2 ) \oplus E _ { 8 } ( - 2 ) .
$$

It therefore stabilizes the $A _ { 1 } ( - 2 )$ -summand.
Using the above remarks about the identifications of $L _ { + } ^ { \star } / L _ { + }$ with $L _ { - } ^ { * } / L _ { - }$ we conclude that $g | L _ { - }$ belongs to the set mentioned in the lemma.

Conversely,let $g \in O ( L _ { - } )$ respect the decomposition of $L _ { - } ^ { * } / L _ { - }$ .By composing $g$ ,if necessary,with the involution $p$ on $L _ { - }$ defined by: $p$ is the identity on the summands $\mathbf { H }$ and $E _ { 8 } ( - 2 )$ and $p$ interchanges the two vectors $e ^ { \prime }$ and $f ^ { \prime }$ in the summand ${ \bf H } ( 2 )$ ，we may restrict our attention to $g ^ { \ast } s$ which induce the identity on $\scriptstyle { \frac { 1 } { 2 } } \mathbf { H } ( 2 ) / \mathbf { H } ( 2 )$ .Note that $p$ is easily seen to extend to an involution on $L$ which commutes with $I$ and fixes $( e + f , e + f , 0 )$ .The surjectivity of the map

$$
{ \cal O } ( E _ { 8 } ( - 2 ) )  { \cal O } ( \frac { 1 } { 2 } E _ { 8 } ( - 2 ) / E _ { 8 } ( - 2 ) , q )
$$

(see [2],p.388) and the obvious injection ${ \cal O } ( E _ { 8 } ( - 2 ) ) \hookrightarrow { \cal O } ( L _ { - } )$ allow us to change $g$ in such a way that the induced map on $L _ { - } ^ { * } / L _ { - }$ is the identity (again, elements of ${ \cal O } ( E _ { 8 } ( - 2 ) ) \subset { \cal O } ( L _ { - } )$ extend to elements in $O ( L )$ commuting with $I$ and fixing $( e + f , e + f , 0 ) )$ .
Now lift the result to $L$ (use (1.4)).□

2.8 Remark.
Contrary to what one might hope, $\Gamma$ does not equal

$$
\Bigg \{ g \in O ( L _ { - } ) : g \quad \mathrm { s t a b i l i z e s } \quad \frac { 1 } { 2 } ( e ^ { \prime } - f ^ { \prime } ) + L _ { - } \Bigg \} .
$$

o

$$
\begin{array} { l } { \displaystyle \psi ( y ) = y + ( y , \frac 1 2 \overline { { \alpha } } _ { 1 } ) ( e ^ { \prime } + f ^ { \prime } + \alpha _ { 2 } ) } \\ { \displaystyle \qquad - \frac 1 2 \biggl ( \frac 1 2 \overline { { \alpha } } _ { 1 } \biggr ) ^ { 2 } ( y , e ^ { \prime } + f ^ { \prime } + \alpha _ { 2 } ) ( e ^ { \prime } + f ^ { \prime } + \alpha _ { 2 } ) - ( y , e ^ { \prime } + f ^ { \prime } + \alpha _ { 2 } ) \frac 1 2 \overline { { \alpha } } _ { 1 } . } \end{array}
$$

Then $\psi \in O ( L _ { - } ) , \psi ( e ^ { \prime } ) = e ^ { \prime } + 2 ( e ^ { \prime } + f ^ { \prime } + \alpha _ { 2 } ) - \overline { { { \alpha } } } _ { 1 }$ and $\psi ( f ^ { \prime } ) = f ^ { \prime } { + } 2 ( e ^ { \prime } { + } f ^ { \prime } { + } \alpha _ { 2 } ) { - } \overline { { \alpha } } _ { 1 }$ from which it follows that $\psi$ stabilizes ${ \textstyle \frac { 1 } { 2 } } ( e ^ { \prime } - f ^ { \prime } ) + L _ { - }$ and $\psi \not \in \Gamma$ ，

The image of $\phi _ { X , C } ( \omega _ { X } )$ in $\Omega _ { - } / \Gamma$ is now well-defined (the period point）and we obtain the period map $P : { \cal M } _ { E }  \Omega _ { - } / \Gamma ,$ where $M _ { E }$ is the set of isomorphism classes of almost polarized Enriques surfaces of degree 2.

2.9 Remark.
The space $\Omega _ { - }$ consists of two disjoint (isomorphic） connected complex manifolds of dimension 10, both of which are isomorphic to a bounded symmetric domain of type IV.
The group $\Gamma$ acts properly discontinuously on $\Omega _ { - }$ ，which implies that the quotient $\Omega _ { - } / \Gamma$ inherits the structure of a normal analytic space by Cartan's result [5].
The space $\Omega _ { - } / \Gamma$ is connected as $( - 1 ) _ { \mathbf { H } } \oplus 1 _ { \mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 2 ) } \in \Gamma$ interchanges the two components.
The analytic structure on $\Omega _ { - } / \Gamma$ even underlies the structure of a quasi-projective variety [1].

To state the appropriate Torelli theorem, we first make a definition.

2.10 Definition.
For any subset $V \subset L _ { \sim }$ with $v ^ { 2 } < 0$ for all $v \in V$ define

$$
D _ { V } : = \{ \omega \in \Omega _ { - } : ( \omega , v ) = 0 \quad f o r \ s o m e \ v \in V \} .
$$

If $V$ is a union of finitely many $\Gamma$ -orbits, then $D _ { V }$ is locally finite and $D _ { V } / \Gamma$ is a Weil-divisor in $\Omega _ { - } / \Gamma$ As we shall see later (see 3.6), the set

$$
R _ { - } = \left\{ x \in L _ { - } : ( x , x ) = - 2 \right\}
$$

satisfies this condition.
In fact, $R _ { - }$ is a single $\Gamma$ -orbit, which means that $D _ { R _ {  } } / \Gamma$ is irreducible.This is an analogue of [17],Theorem (2.13).
The Torelli theorem in our seting can now be stated as follows (see [11,12] and [25]):

2.11 Proposition.
The map $P$ establishesa bijection

$$
M _ { E }  ( \Omega _ { - } - D _ { R _ { - } } ) / \Gamma .
$$

2.12 Remark.Horikawa [11,12] and Namikawa [17] consider $\Omega _ { - } / G _ { ; }$ where $G$ is the set of all $g \in O ( L _ { - } )$ such that $\pmb { g }$ is the restriction of an element of $O ( L )$ which commutes with $I$ Actually,Namikawa shows that $G = O ( L _ { - } )$ .It is straightforward to compute the degree of the natural map $\Omega _ { - } / \Gamma \to \Omega _ { - } / O ( L _ { - } )$ i.e. the index $[ O ( L _ { - } ) : \Gamma ]$ .
As the map ${ \cal O } ( L _ { - } )  { \cal O } ( L _ { - } ^ { * } / L _ { - } )$ is surjective, see (1.4), we have

$$
[ O ( L _ { - } ) : \Gamma ] = ( O ( L _ { - } ^ { * } / L _ { - } ) : \mathrm { I m a g e } ( \Gamma \to O ( L _ { - } ^ { * } / L _ { - } ) ) ]
$$

and by [2],p.388,we find that this last index equals

$$
( 2 ^ { 2 1 } \cdot 3 ^ { 5 } \cdot 5 ^ { 2 } \cdot 7 \cdot 1 7 \cdot 3 1 ) / ( 2 \cdot 2 ^ { 1 3 } \cdot 3 ^ { 5 } \cdot 5 ^ { 2 } \cdot 7 ) = 2 ^ { 7 } \cdot 1 7 \cdot 3 1 ,
$$

which of course agrees with the number of inequivalent realizations of an Enriques surface,‘general’ in the sense of [loc. cit.],as a‘double plane' ([loc. cit.], Theor.
3.9).

# 3 Arithmetical results

We collect several arithmetical results,which we shall use in later paragraphs, and some of their consequences.

3.1 Proposition.
Let $\Lambda = \mathbf { H } \oplus \mathbf { H } ( 2 )$ with basis $e , f \in \mathbf { H } , e ^ { \prime } , f ^ { \prime } \in \mathbf { H } ( 2 )$ Suppose $v \in \Lambda$ is primitive.Then:

$$
\begin{array} { r } { { v } \sim _ { O ( \Lambda ) } e + k f \quad i f \quad ( v , v ) = 2 k \quad a n d \quad v \not \in 2 \Lambda ^ { * } } \\ { { v } \sim _ { O ( \Lambda ) } e ^ { \prime } + k f ^ { \prime } \quad i f \quad ( v , v ) = 4 k \quad a n d \quad v \in 2 \Lambda ^ { * } . } \end{array}
$$

Proof.
Let

$$
\begin{array}{c} M : = { \left\{ \begin{array} { l l } { \left( a \right)} & { b } \\ { c } & { d } \end{array}  \in M _ { 2 } ( \mathbf { Z } ) : c { \mathrm { ~ e v e n } } \right\} \end{array} }  .
$$

This is a lattice with quadratic form given by the determinant.
(Note that the associated bilinear form assumes its values in ${ \frac { 1 } { 2 } } \mathbf { Z } .$ ）

Set $B : = \Im L _ { 2 } ( \mathbf { Z } ) \cap M$ and let $G$ be the group of automorphisms of $M$ generated by $B \times B$ ,where the first factor acts on the left and the second on the right,and the involution which sends

$$
\left( \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right)
$$

to

$$
\left( \begin{array} { l l } { { d } } & { { b } } \\ { { c } } & { { a } } \end{array} \right) .
$$

This group leaves the determinant det : $M \to \mathbf { Z }$ invariant.
We have an isometry $\Lambda \to M ( 2 )$ defined by

$$
x e + y f + x ^ { \prime } e ^ { \prime } + y ^ { \prime } f ^ { \prime } \mapsto { \binom { x } { - 2 y ^ { \prime } } } \quad x ^ { \prime } \triangleq y .
$$

Let $v \in \Lambda$ be primitive and suppose it corresponds to

$$
\sigma = { \binom { a } { c } } \ { \stackrel { b } { d } } \ ) \in M .
$$

$\sigma$ is not primitive in $M _ { 2 } ( \mathbf { Z } )$ ，then $a , b , d$ are even and ${ \scriptstyle { \frac { 1 } { 2 } } } c$ is odd.
If we first apply to $v$ the automorphism of $\Lambda$ which interchanges $e ^ { \prime }$ and $f ^ { \prime }$ ,then $\pmb { \sigma }$ changes to

$$
\left( \begin{array} { c c } { { a } } & { { - \frac { 1 } { 2 } c } } \\ { { - 2 b } } & { { d } } \end{array} \right) .
$$

Therefore we may assume that $\pmb { \sigma }$ is primitive.
Let $e _ { 1 } , e _ { 2 }$ be the standard basis of $\mathbf { Z } ^ { 2 }$ .We distinguish between 2 cases.

1. $\sigma ( e _ { 1 } + 2 { \bf Z } ^ { 2 } )$ contains a primitive vector  
   In this case there exists a primitive $\ b u _ { 1 } \in \ b { e } _ { 1 } + 2 \ b { \mathbf { Z } } ^ { 2 }$ such that $\sigma ( u _ { 1 } )$ is primitive (and $\sigma ( u _ { 1 } ) \in e _ { 1 } + 2 \mathbf { Z } ^ { 2 } )$ .
   Choose $u _ { 2 } , v _ { 2 }$ such that $( u _ { 1 } , u _ { 2 } )$ and $( v _ { 1 } = \sigma ( u _ { 1 } ) , v _ { 2 } )$ are oriented bases.
   Define $U$ ， $V \in B$ by: $U ( e _ { i } ) = u _ { i }$ ， $V ( e _ { i } ) = v _ { i }$ $( i = 1 , 2 )$ .
   Then $V ^ { - 1 } \pmb { \sigma U }$ looks like

$$
\left( \begin{array} { c c } { { 1 } } & { { \ast } } \\ { { 0 } } & { { \ast } } \end{array} \right) ( V ^ { - 1 } \sigma U e _ { 1 } = V ^ { - 1 } \sigma u _ { 1 } = e _ { 1 } ) .
$$

It is clear that

$$
\left( \begin{array} { c c } { { 1 } } & { { * } } \\ { { 0 } } & { { * } } \end{array} \right) \sim _ { G } \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { * } } \end{array} \right) .
$$

So $v \sim _ { o ( \Lambda ) } e + k f$ for some $k \in \mathbf { Z }$

2. $\sigma ( e _ { 1 } + 2 \mathbf { Z } ^ { 2 } )$ does not contain a primitive vector.

As $\pmb { \sigma }$ is primitive, $\sigma ( { \bf Z } ^ { 2 } )$ does*contain a primitive vector.
It follows that there exists a primitive $\boldsymbol { u } * { 1 } \in e _ { 1 } + 2 \mathbf { Z } ^ { 2 }$ with $\sigma ( u _ { 1 } ) = 2 v _ { 1 } , v _ { 1 }$ primitive.

a) $\boldsymbol { v } _ { 1 } \in \mathbf { Z } e _ { 1 } + 2 \mathbf { Z } ^ { 2 }$

Define $\boldsymbol { U }$ and $V$ as in (1.).
Then $V ^ { - 1 } \sigma U$ is of the following type

$$
\left( { \begin{array} { c c } { 2 } & { * } \\ { 0 } & { * } \end{array} } \right)
$$

and we get for $b$ even:

$$
\left( \begin{array} { l l } { 2 } & { b } \\ { 0 } & { d } \end{array} \right) \sim _ { G } \left( \begin{array} { l l } { 2 } & { 0 } \\ { 0 } & { d } \end{array} \right) \quad \left( \mathrm { m u l t i p l y ~ o n ~ t h e ~ r i g h t ~ b y } \quad \left( \begin{array} { l l } { 1 } & { \frac { b } { 2 } } \\ { 0 } & { 1 } \end{array} \right) \right)
$$

and

$$
\left( \begin{array} { c c } { { 2 } } & { { 0 } } \\ { { 0 } } & { { d } } \end{array} \right) \sim _ { G } \left( \begin{array} { c c } { { d } } & { { 0 } } \\ { { 0 } } & { { 2 } } \end{array} \right) .
$$

Now $d$ is odd because $\sigma ^ { ( \mathbf { Z } ^ { 2 } ) }$ contains a primitive vector.
But then we are back in case (1.).For $b$ odd:

$$
\begin{array} { r l } { ( \begin{array} { l l } { 2 } & { b } \\ { 0 } & { d } \end{array} ) \sim _ { G } ( \begin{array} { l l } { 2 } & { 1 } \\ { 0 } & { d } \end{array} ) } & { \bigg ( \mathrm { m u l t i p l e ~ o n ~ t h e ~ r i g h t ~ b y } ( \begin{array} { l l } { 1 } & { \frac { - ( b - 1 ) } { 2 } } \\ { 0 } & { 1 } \end{array} ) \bigg ) , } \\ { ( \begin{array} { l l } { 2 } & { 1 } \\ { 0 } & { d } \end{array} ) \sim _ { G } \bigg ( \begin{array} { l l } { 0 } & { 1 } \\ { 1 - 2 d } & { d } \end{array} ) } & { \bigg ( \mathrm { m u l t i p l y ~ o n ~ t h e ~ r i g h t ~ b y } ( \begin{array} { l l } { 1 } & { 0 } \\ { - 2 } & { 1 } \end{array} ) \bigg ) , } \end{array}
$$

f $d$ is even:

$$
\left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - 2 d } } & { { d } } \end{array} \right) \sim _ { G } \left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - 2 d } } & { { 0 } } \end{array} \right) \quad \left( \mathrm { m u l t i p l y ~ o n ~ t h e ~ l e f t ~ b y } \quad \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { - d } } & { { 1 } } \end{array} \right) \right) .
$$

$\mathrm { S } \circ v \sim _ { O ( \Lambda ) } e ^ { \prime } + d f ^ { \prime }$ in this case.
If $d$ is odd:

$$
\left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - 2 d } } & { { 1 } } \end{array} \right) \sim _ { G } \left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { - 2 d } } & { { 0 } } \end{array} \right) .
$$

According to case (1.
） we then have $v \sim _ { O ( \Lambda ) } e + k f$ for some $k$

b） $\boldsymbol { v } _ { 1 } \notin \mathbf { Z } \boldsymbol { e } _ { 1 } + 2 \mathbf { Z } ^ { 2 }$

In this case the second coordinate of $\pmb { v } _ { 1 }$ is odd.Choose a'vector $v _ { 2 }$ such that the second coordinate of $v _ { 2 }$ is even and $\{ v _ { 2 } , v _ { 1 } \}$ is a positively oriented basis.
Define $V \in B$ by $V e _ { 1 } \simeq \upsilon _ { 2 } , \ V e _ { 2 } = \upsilon _ { 1 } , \ U \ \in \ B$ by $\it U e _ { i } = u _ { i } ( i = 1 , 2 )$ Then $V ^ { - 1 } \sigma U ( e _ { 1 } ) = V ^ { - 1 } ( 2 v _ { 1 } ) = 2 e _ { 2 } .$ sC $, V ^ { - 1 } \sigma U$ is of the form

$$
\left( \begin{array} { l l } { 0 } & { b } \\ { 2 } & { d } \end{array} \right) .
$$

f $\pmb { d }$ is even:

$$
\left( { \begin{array} { l l } { 0 } & { b } \\ { 2 } & { d } \end{array} } \right) \sim _ { G } \left( { \begin{array} { l l } { 0 } & { b } \\ { 2 } & { 0 } \end{array} } \right) \quad \left( { \mathrm { m u l t i p l y ~ o n ~ t h e ~ r i g h t ~ b y } } \quad \left( { \begin{array} { l l } { 1 } & { { \frac { - d } { 2 } } } \\ { 0 } & { 1 } \end{array} } \right) \right)
$$

and so $V \sim _ { O ( \Lambda ) } e ^ { \prime } + k f ^ { \prime }$ for some ${ \boldsymbol { k } } \in { \mathbf { Z } } ,$

If $d$ is odd:

$$
\left( \begin{array} { c c } { { 0 } } & { { b } } \\ { { 2 } } & { { d } } \end{array} \right) \sim _ { G } \left( \begin{array} { c c } { { 0 } } & { { b } } \\ { { 2 } } & { { 1 } } \end{array} \right) \sim _ { G } \left( \begin{array} { c c } { { 1 } } & { { b } } \\ { { 2 } } & { { 0 } } \end{array} \right) .
$$

By case (1.): $v \sim _ { o ( \Lambda ) } e + k f$

3.2 Corollary.Suppose $v \in \Lambda$ is primitive.
Then

$$
v \sim _ { O ^ { \star } ( \Lambda ) } \left\{ \begin{array} { l l } { e + k f } & { i f \ ( v , v ) = 2 k \quad a n d \quad v \not \in 2 { \Lambda ^ { \star } } . } \\ { e ^ { \prime } + k f ^ { \prime } } & { o r } \\ { k e ^ { \prime } + f ^ { \prime } } & { i f \ ( v , v ) = 4 k \quad a n d \quad v \in 2 { \Lambda ^ { \star } } . } \end{array} \right.
$$

Proof.This is an immediate consequence of (3.1) and the fact that the involution determined by

$$
e ^ { \prime } \mapsto f ^ { \prime } , f ^ { \prime } \mapsto e ^ { \prime } , e \mapsto e , f \mapsto f
$$

generates the quotient $O ( \Lambda ) / O ^ { * } ( \Lambda )$

3.3 Corollary.Let $P$ be an even nondegenerate lattice and let $N : = \Lambda \oplus P$ .1 $v , w \in N$ are primitive such that

$$
\begin{array} { l } { { \displaystyle ( v , v ) = ( w , w ) , } } \\ { { \displaystyle ( v , N ) = ( w , N ) ( = : p { \bf Z } , p > 0 ) , } } \\ { { \displaystyle v \equiv w \bmod p N , } } \end{array}
$$

then $v \sim _ { O ^ { * } ( N ) } w$

Proof.
In two steps.

Step 1. $\exists j \in O ^ { \bullet } ( N )$ such that $( j ( v ) , f ) = p$ .The previous corollary implies the existence of a $j _ { 1 } \in O ^ { \bullet } ( \Lambda ) \subseteq O ^ { \bullet } ( P )$ such that $v ^ { \prime } : = j _ { 1 } ( v ) \in \mathbf { H } ( 2 ) \oplus P$ or $v ^ { \prime } \in { \bf { H } } \oplus P$ In the first case we choose $y \in { \bf H } ( 2 ) \oplus P$ such that $\ ( v ^ { \prime } , y ) = p$ Consider the SiegelEichler transformation $E _ { e , y }$ ,defined by

$$
E _ { e , y } ( x ) = x + ( x , y ) e - { \frac { 1 } { 2 } } ( y , y ) ( x , e ) e - ( x , e ) y .
$$

One easily verifies that $E _ { e , y } O ^ { * } ( N )$ Now $E _ { e , y } ( v ^ { \prime } ) \ = \ p e \ + \ v ^ { \prime }$ and therefore $( E _ { e , y } ( v ^ { \prime } ) , f ) = p$ 、In the second case we choose $y \in \textbf { H } \oplus P$ with $\begin{array} { r } { ( y , v ^ { \prime } ) = p . } \end{array}$ Let $v ^ { \prime \prime } : = E _ { e ^ { \prime } , y } ( v ^ { \prime } ) = v ^ { \prime } + p e ^ { \prime }$ If the $\Lambda$ -component of $v ^ { \prime \prime }$ is $k \times$ primitive vector, then $k | p .$ ，Applying (3.1） again yields: $\exists j _ { 2 } \in O ^ { \bullet } ( \Lambda )$ such that for $v ^ { \prime \prime \prime } : = j _ { 2 } ( v ^ { \prime \prime } )$ we have: $v ^ { \prime \prime \prime } \in { \bf { H } } ( 2 ) \oplus { \cal P }$ ,and this brings us back to the first case, or the $\Lambda$ -component of $\boldsymbol { v } ^ { \prime \prime \prime }$ is of the form $k ( e { + } l f )$ for some $l \in \mathbf { Z }$ Then $( f , v ^ { \prime \prime \prime } ) = k$ so $p | k$ .
We conclude $p = k$

Step 2. Conclusion.
By step 1 we may assume $( v , f ) = ( w , f ) = p$ Now $v - w = p u$ (some $u \in N$ and of course $( u , f ) = 0$ Then for $\psi : = E _ { f , u }$ we find:

$$
\psi ( v ) \equiv v - ( f , v ) u \mathrm { m o d } \mathbf { Z } f \equiv w \mathrm { m o d } \mathbf { Z } f .
$$

If we write $\psi ( v ) ~ = ~ w + \lambda f$ ，then from $( w , w ) \ = \ ( v , v ) \ = \ ( \psi ( v ) , \psi ( v ) ) = $ $( w + \lambda f , w + \lambda f ) = ( w , w ) + 2 \lambda p$ we conclude that $\lambda = 0$ □

Let

$$
S : = \left\{ \alpha \in L : ( \alpha , \alpha ) = - 2 , ( \alpha , I \alpha ) = 0 , \alpha + I \alpha = ( f - e , f - e , 0 ) \right\}
$$

and let $s _ { - }$ be the orthogonal projection of $s$ in $L _ { - } ^ { * }$ .If ${ \pmb { \alpha } } \in { \pmb { S } }$ then $\begin{array} { r } { { \frac { 1 } { 2 } } \left( \alpha - I \alpha \right) } \end{array}$ is the orthogonal projection of $\alpha$ in $L _ { - } ^ { * }$ .Write $\alpha = ( a , b , h ) \in M \oplus M \oplus \mathbf { H } ,$ then we have $a + b = f - e$ and so $\begin{array} { r } { \frac { 1 } { 2 } ( a - b ) = \frac { 1 } { 2 } ( f - e ) - b } \end{array}$ We therefore find:

$$
\begin{array} { l } { \displaystyle \frac 1 2 ( a - I a ) = \left( \frac 1 2 ( a - b ) , \frac 1 2 ( b - a ) , h \right) } \\ { \displaystyle = \left( \frac 1 2 ( f - e ) , \frac 1 2 ( e - f ) , 0 \right) + ( - b , b , h ) \in \frac 1 2 \bigg ( f - e , e - f , 0 \bigg ) + L _ { - } . } \end{array}
$$

3.4 Lemma.
Under the action of $\Gamma$ on $L _ { \mathrm { ~ \tiny ~ , ~ } } ^ { \ast } \mathrm  ~ \} s _ { \scriptscriptstyle \mathrm { ~ \tiny ~ \mathscr ~ { ~ r ~ } ~ } }$ is precisely the $\Gamma$ orbit of ${ \textstyle \frac { 1 } { 2 } } ( f - e , e - f , 0 ) .$

Proof.
Let $\smash { \alpha _ { s c } \in S _ { - } }$ and suppose it is the orthogonal projection of ${ \pmb { \alpha } } \in { \pmb S }$ .Then we have

$$
( \alpha _ { - } , \alpha _ { - } ) = \frac { 1 } { 4 } ( \alpha , \alpha ) + \frac { 1 } { 4 } ( I \alpha , I \alpha ) = - 1 .
$$

Moreover $( \alpha _ { - } , ( e , - e , 0 ) ) \equiv 1 ( \mathrm { m o d } 2 ) ( \mathrm { u s e } \alpha _ { - } \in \frac 1 2 ( f - e , e - f , 0 ) + L _ { - } )$ As $( \pmb { \alpha } _ { - } , 2 \alpha ) =$ 2 and $2 \mathsf { \alpha \_ t } \mathsf { L } _ { - }$ we conclude: $( { \pmb { \alpha } } _ { - } , { \pmb { L } } _ { - } ) = { \pmb { \mathrm { Z } } }$ Clearly $\pmb { \alpha _ { - } }$ and ${ \scriptstyle \frac { 1 } { 2 } } ( f - e , e - f , 0 )$ have the same reduction in $L _ { - } ^ { * } / L _ { - }$ so (3.3) implies: $\alpha _ { - } \sim _ { O ^ { \bullet } ( L - ) } { \textstyle \frac { 1 } { 2 } } ( f - e , e - f , 0 )$ ,which suffices since $O ^ { * } ( L _ { - } ) \subset \Gamma$

Conversely, let $\beta _ { - } = g ( \textstyle { \frac { 1 } { 2 } } ( f - e , e - f , 0 ) )$ for some $g \in \Gamma$ By (2.7) there exists an extension $\widetilde { g } \in O ( L )$ such that $\widetilde { g } ( e + f , e + f , 0 ) = ( e + f , e + f , 0 )$ and $\widetilde g \circ I = I \circ \widetilde g$ Consider $\beta : = ( f , f , 0 ) - \widetilde { g } ( e , f , 0 ) \in L$ Then $\beta + I \beta = ( f - e , f - e , 0 )$ ， $( \beta , I \beta ) = 0$ and $( \beta , \beta ) = - 2$ so $\beta \in S$ .□

3.5 Proposition.
Let $( Y , \eta _ { Y } )$ be an almost polarized Enriques surface of degree  
2 and let $\Phi$ be a marking.
Then:

$$
\phi _ { X } ( \alpha + I ^ { \ast } \alpha ) = \pm ( f - e , f - e , 0 ) .
$$

Proof.
$\ ' \Rightarrow \ '$ : Clear from (2.4).
$\bullet _ { \infty } ,$ : Suppose $\alpha \in \ \operatorname { P i c } X$ satisfies the above mentioned conditions.
We may assume that $\pmb { \alpha }$ is an effective class,say $\alpha = [ D ]$ where $D \not \equiv 0$ Suppose $( Y , \pmb { \eta } _ { Y } )$ is ‘general', so $| \pi ^ { * } \eta _ { Y } |$ maps $X 2 : 1$ onto $\Sigma _ { 0 }$ Then $| \phi _ { X } ^ { - 1 } ( e , e , 0 ) |$ and $| \phi _ { X } ^ { - 1 } ( f , f , 0 ) |$ correspond to two elliptic pencils $| E |$ and $| F |$ on $X$ by (2.3).
Clearly $D + I D \in | E - F |$ $\mathbf { r } \in \left| F - E \right| )$ .
So there exists a fibre $E ^ { \prime }$ of

$$
X { \overset { | E | } { \to } } \mathbb { P } ^ { 1 }
$$

and a $F ^ { \prime } \in \left. F \right.$ such that $F ^ { \prime } \leqslant E ^ { \prime }$ As $( F ^ { \prime } , F ^ { \prime } ) = 0 $ ,we must have $F ^ { \prime } \sim r E ^ { \prime }$ (some $r \in \mathbf { Q } )$ .
But then $2 = ( E , F ) = r ( E , E ) = 0$ a contradiction.□

This proposition enables us to describe the‘special’ divisor in $\Omega _ { - } / \Gamma$ determined by the periods of special Enriques surfaces.
Let $( Y , \eta _ { Y } , \Phi )$ be as usual.
Choose $\omega \in H ^ { 0 } ( X , \Omega ^ { 2 } ) - \{ 0 \}$ and let $\smash { \alpha _ { - } \in S _ { - } }$ be the orthogonal projection of ${ \mathfrak { a } } \in S$ .If $( \propto _ { - } , \phi _ { X , \mathbf { C } } ( \omega ) ) = 0$ ,then also $( \alpha , \phi _ { X , \mathbf { C } } ( \omega ) ) = 0$ and so $\phi _ { X } ^ { - 1 } ( \alpha ) \in \operatorname { P i c } X$ By (3.5) we conclude that $( Y , \eta _ { Y } )$ is special.In the terminology of (2.10) we obtain a special divisor $D _ { S _ { - } } / \Gamma$ which parametrizes (outside $D _ { R _ { - } } / \Gamma )$ periods of special Enriques surfaces.
Lemma 3.4 implies that $D _ { S _ { - } } / \Gamma$ is actually irreducible.

3.6 Remark.
Corollary (3.3) implies that $R _ { - }$ (see (2.10)) is also a single $\Gamma$ -orbit.
To see this, let $x \in R _ { - }$ .
Then surely $2 \mathbf { Z } \subset ( x , L _ { - } )$ as $x ^ { 2 } = - 2$ Write $x = a + b$ with $a \in \mathbb { H }$ and $b \in { \bf H } ( - 2 ) \oplus E _ { 8 } ( - 2 )$ .Now $a \neq 0$ ，since otherwise $4 \{ x ^ { 2 } = b ^ { 2 }$ .Let $a = k \alpha$ with $k \in \mathbf { Z }$ and $\pmb { \alpha }$ primitive.
The integer $k$ must be odd (otherwise $4 | x ^ { 2 } )$ and so we find that $( x , L _ { - } ) = 2 \mathbf { Z } + k \mathbf { Z } = \mathbf { Z }$ The rest of the proof is left to the reader.

We*conclude_thissection with some results related to the natural map $\Omega * { - } / \Gamma \to \Omega _ { - } / O ( L _ { - } )$

3.7 Proposition.
$\{ g ( e ^ { \prime } - f ^ { \prime } ) : g \in O ^ { \bullet } ( L _ { - } ) \} = \{ g ( e ^ { \prime } - f ^ { \prime } ) : g \in \Gamma \}$ and the $O ( L _ { - } )$ -orbit of $e ^ { \prime } - f ^ { \prime }$ consists of precisely four $\Gamma$ -orbits.

Proof.The first equality follows from the proof of (3.4).

Let $x$ be of the form $g ( e ^ { \prime } { - } f ^ { \prime } )$ with $g \in O ( L _ { - } )$ ,then $( x , L _ { - } ) = ( e ^ { \prime } - f ^ { \prime } , L _ { - } ) = 2 { \bf Z }$ and $x ^ { 2 } = - 4$ We obtain $\frac { 1 } { 2 } x + L _ { - } \in L _ { - } ^ { * } / L _ { - }$ with $q ( { \scriptstyle { \frac { 1 } { 2 } } } + L _ { - } ) = 1 { \bmod { 2 } }$ Upon writing ${ \frac { 1 } { 2 } } x + L _ { - } = x _ { 1 } + x _ { 2 }$ ，with $x _ { 1 } \in \mathbf \Gamma _ { 2 } ^ { 1 } \mathbf H / \mathbf H$ and $x _ { 2 } \in \frac 1 2 E _ { 8 } ( - 2 ) / E _ { 8 } ( - 2 ) ,$ we distinguish two cases.

Case $A$ $q ( x _ { 1 } ) = 0 { \bmod { 2 } }$ ， $q ( x _ { 2 } ) \ = \ 1 \ { \bmod { 2 } }$ Let $\alpha \in E _ { 8 } ( - 2 )$ ， $\alpha ^ { 2 } = - 4$ ，then, possibly after applying an element of $O ( \mathbf { H } ( 2 ) ) \times O ( E _ { 8 } ( - 2 ) )$ ,we may assume that either $\frac { 1 } { 2 } e ^ { \prime } + L _ { - }$ or $\frac { 1 } { 2 } \left( e ^ { \prime } + \alpha \right)$ equals $\frac { 1 } { 2 } x + L _ { - }$ .If $y \in L _ { \sim }$ $( y , L _ { - } ) = 2 \mathbf { Z }$ $y ^ { 2 } = - 4$ ,then, by (3.3), $y \sim _ { \Gamma } \alpha$ or $y \sim _ { \Gamma } e ^ { \prime } + \alpha$ if $q ( y _ { 1 } ) = 0 { \bmod { 2 } }$ (where we have decomposed $\frac { 1 } { 2 } y + L _ { - } )$ .
Note that $\pmb { \alpha }$ and $e ^ { \prime } + \alpha$ are not $\Gamma$ -equivalent.

Case $B$ $q ( x _ { 1 } ) \ = \ 1 { \bmod { 2 } }$ ， $q ( x _ { 2 } ) \ = \ 0 { \bmod { 2 } }$ Proceeding as in $A$ we find $x \sim _ { \Gamma } e ^ { \prime } - f ^ { \prime }$ or $x \sim _ { \Gamma } e ^ { \prime } + f ^ { \prime } + \omega$ ，where $\omega \in E _ { 8 } ( - 2 )$ satisfies $\omega ^ { 2 } = - 8$

It is easily checked that no two elements of $\left\{ \alpha , e ^ { \prime } + \alpha , e ^ { \prime } - f ^ { \prime } , e ^ { \prime } + f ^ { \prime } + \omega \right\}$ are $\Gamma$ -equivalent, but that all belong to the $O ( L _ { - } )$ -orbit of $e ^ { \prime } - f ^ { \prime }$ as there is only one $O ( \mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 2 ) )$ -orbit of $( - 4 )$ -vectors in $\mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 2 )$ □

According to [2],p.393,nodal Enriques surfaces have their periods in the set $D _ { \mathrm { r o o t s ~ i n } L _ { + } }$ .
In fact,if $Y$ is nodal with $C \subset Y$ a nodal curve, then $\bar { \pi } ^ { - 1 } ( C ) = B + I ( B ) .$ yielding a class $b ( = \ [ B ] )$ with $b ^ { 2 } \ = \ - 2$ $( b , I b ) \ = \ 0$ The 2-form $\omega _ { X }$ will be $\perp b$ and of course $\perp b - I b$ In terms of $L _ {  }$ we are considering the set $N : = \{ b - I b : ( b , I b ) = 0$ $b ^ { 2 } = - 2 \}$ .
Conversely, suppose $b \in N$ with $( b , \omega _ { X } ) = 0 ;$ then $\boldsymbol { \cdot } \boldsymbol { b } = \left[ B \right]$ for some effective $B$ and $B + I B = \pi ^ { * } ( D )$ for some effective divisor $D$ with $D ^ { 2 } = - 2$ .But this implies that $Y$ is nodal.

Let $b - I b \in N$ In particular, $( b - I b ) ^ { 2 } = - 4$ so $b - I b$ is* primitive in $L * { - }$ and therefore $( b - I b , L _ { \ldots } ) = \mathbf { Z }$ or $\mathbf { 2 } \mathbf { Z }$ If $\beta \in L _ { \cdots }$ ,then $( b - I b , \beta ) = 2 ( b , \beta ) \in 2 { \bf Z } ,$ so $b - I b \in 2 L _ { - } ^ { * }$ and an analysis as before shows that $b - I b = g ( e ^ { \prime } - f ^ { \prime } )$ with g ∈ O(L*).
Moreover, if b-Ib ∈ N and g ∈ O(L*), then using an extension ${ \widetilde { g } } \in O ( L )$ of $g$ satisfying $\widetilde g \circ I \ : = \ : I \circ \widetilde g$ we deduce that $g ( b - I b ) \ \in \ N$ and g(b-Ib) ∈ {h(e'-f') :h ∈O(L*)}.In conclusion,N equals the O(L*)-orbit of $e ^ { \prime } - f ^ { \prime }$

3.8 Proposition.a) Every nodal Enriques surface can be given a special almost polarization of degree 2.  
b)A‘general’nodal Enriques surface can be given both a special and a general almost polarization of degree 2.

Proof.a) Consider $p : \Omega _ { - } / \Gamma  \Omega _ { - } / O ( L _ { - } )$ Let $[ \omega ] \in \Omega _ { - } / O ( L _ { - } )$ correspond to a nodal Enriques surface, so $( \omega , n ) = 0$ for some $n \in N$ .By applying an element of $O ( L _ { - } )$ we may assume $n \in S _ { - }$ .But then $[ \omega ]$ is in the image of $D _ { S _ { - } } / \Gamma$ As $| R _ { - } / \Gamma | = | R _ { - } / O ( L _ { - } ) |$ ,we still have $[ \omega ] \notin D _ { R _ { - } } / \Gamma$ so $[ \omega ]$ corresponds to a special Enriques surface.

b) As the $O ( L _ { - } )$ -orbit of $e ^ { \prime } - f ^ { \prime }$ strictly contains the $\Gamma$ -orbit of $e ^ { \prime } - f ^ { \prime }$ $p ^ { - 1 } p ( D _ { S _ { - } } / \Gamma )$ strictly contains $D _ { S _ { - } } / \Gamma$ Therefore,if the period point $\mathrm { i n } \Omega _ { - } / O ( L _ { - } ) )$ of a nodal Enriques surface in sufficiently general, then it will also have a preimage outside $D _ { S _ { - } } / \Gamma$ □

# 4 The Satake-Baily-Borel compactification of $\Omega _ { - } / \Gamma$

In this paragraph we determine the boundary components of the Satake-BailyBorel compactification $\widehat { \Omega } _ { - } / \Gamma$ .
Their incidence relations are described by the diagram in (4.4).The structure of the one-dimensional boundary components is given in (4.3.16) and (4.3.17).
Before we start with the actual computations,let us recall the description of this Satake-Baily-Borel compactification in a somewhat larger setting.

4.1Let $_ D$ be a bounded symmetric domain,i.e. $D$ is a connected complex ndimensional manifold such that:

1. $D$ can be embedded in $C ^ { n }$ as an open bounded set;  
   2．every point in $D$ is an isolated fixed point of an involution of $D$

Examples are the (generalized) upper half-space or a connected component of $\Omega _ { - }$

The (holomorphic) automorphism group of $D$ acts transitively on $D$ with compact isotropy groups and can be viewed as a union of connected components of the set of real points $G ( \mathbb { R } )$ of some connected semi-simple linear algebraic group $G$ defined over R.
Suppose $G$ is actually defined over Q and let $\Gamma \subset G ( \mathbf { Q } )$ be an arithmetic group,meaning that $\Gamma$ is commensurable with $\varrho ^ { - 1 } G L _ { m } ( \mathbf { Z } )$ for some faithful representation $\varrho \colon G \to G L _ { m }$ defined over Q.
$D$ is then said to have a $\mathbf { Q }$ -structure.
The group $\Gamma$ is discrete in $G ( \mathbf { R } )$ and acts properly on $D$ ，hence $D / \Gamma$ is a (usually non-compact) analytic space in a natural way [5].
The domain $D$ is embedded as an open subset in its so-called compact dual $\check { D }$ ，a projective manifold.
E.g. $H \subset \check { H } = \mathbf { P } ^ { 1 } ( F$ H : upper half-plane),

$$
\Omega _ { - } \subset \check { \Omega } _ { - } = \{ \omega \in \mathbf { P } ( L _ { - } \otimes C ) : ( \omega , \omega ) = 0 \} .
$$

The boundary $\partial D$ of $D$ in $\check { D }$ decomposes into boundary components,the maximal connected complex analytic submanifolds of $\overline { { D } } - D$ This decomposition is compatible with $G$ The boundary components correspond precisely to the maximal parabolic subgroups of $G ( \mathbb { R } )$ via

$$
\longmapsto N ( F ) = \{ g \in G ( \mathbf { R } ) : g ( F ) = F \} { \mathrm { . } }
$$

Just like $D$ itself, these boundary components are bounded symmetric domains.
A boundary component $F$ is called rational if $N ( F )$ is defined over $\mathbf { Q }$ with respect to the $\mathbf { Q }$ -structure of $G$ .
It then has a $\mathbf { Q }$ -structure and $\Gamma ( F ) = N _ { \Gamma } ( F ) / Z _ { \Gamma } ( F )$ is an arithmetic group of automorphisms of $F$ .
Now set

$$
\widehat { \boldsymbol { D } } : = \boldsymbol { D } \cup \bigcup \{ \boldsymbol { F } : \boldsymbol { F } \quad \mathrm { i s ~ a ~ r a t i o n a l ~ b o u n d a r y ~ c o m p o n e n t } \} .
$$

The group $\Gamma$ acts on this set and $\widehat { D }$ can be given a topology (not the one induced by $\check { D }$ ）such that $\widehat { D } / \Gamma$ is a compact Hausdorff space which contains $D / \Gamma$ as a dense open set.
The topology on $\widehat { D } / \Gamma$ underlies the structure of a normal analytic space which extends the analytic structures on $D / \Gamma$ and the strata $F / \Gamma ( F )$ (Cartan's result);this compactification is even projective.

A simple example ilustrating the above construction is the following.
$D = H \subset \check { H } = \mathbf { P } ^ { 1 }$ ,Γ = SL2(Z).
Now

$$
{ \widehat { H } } = H \cup \mathbf { Q } \cup \{ \infty \} = H \cup \mathbf { P } ^ { 1 } ( Q )
$$

and the topology (the horocycle topology)on $\widehat { H }$ is generated by:

1．the topology on $H$ ·，  
2.sets of the form $\{ z \in H : \operatorname { I m } z > r > 0 \} \cup \{ \infty \}$  
3.sets of the form $\{ r \} \cup \{ z \in H : | z - a | < | a - r | , a \in H , \mathrm { R e } a = r \}$ where $r \in \mathbf { Q }$

The quotient $\widehat { H } / S L _ { 2 } ( \mathbf { Z } )$ is isomorphic to $\mathbf { P } ^ { 1 }$

Let us describe the rational boundary components in our main example $\Omega _ { - } \subset \check { \Omega } _ { - }$ .
The closure of a boundary component $F _ { I }$ of $\Omega _ { - }$ is of the form $\overline { { F } } _ { I } = \mathbf { P } ( I _ { \mathrm { C } } ) \cap \overline { { \Omega } } _ { \mathrm { - } }$ where $I$ is a nontrivial isotropic subspace of $L _ { - } \otimes \mathbb { R }$ Such a boundary component is rational precisely when $I$ is defined over $\mathbf { Q }$ As $\mathsf { s g n } L _ { - } = ( 2 , 1 0 )$ there are only two possibilities: either $\dim _ { \mathbb { R } } I = 1$ and $F _ { I }$ isa singleton or $\dim _ { \mathbb { R } } I = 2$ and in this case $F _ { I } \subset \mathbf { P } ( I _ { \mathbf { C } } )$ is a half-plane.
In particular $\dim _ { \mathbb { C } } ( { \widehat \Omega } _ { - } / \Gamma - \Omega _ { - } / \Gamma ) \leq 1 .$

# 4.2 Zero-dimensional boundary components

The zero-dimensional boundary components of the Satake-Baily-Borel compactification $\widehat { \Omega } _ { - } / \Gamma$ (now $\Gamma$ is the group we determined in (2.7)) are in 1-1 correspondence with the $\Gamma$ -orbits of primitive isotropic sublattices of rank one.
In this subparagraph we compute the number of these orbits,i.e. we compute $I _ { 1 } ( L _ { - } ) / \Gamma$ ，

Let $e , f$ (resp.
$e ^ { \prime } , f ^ { \prime } )$ be the standard basis of the $\mathbf { H }$ (resp.
$\mathbf { H } ( 2 )$ ）summand in $L _ { - }$

4.2.1 Lemma.
Let $v \in L _ { \infty }$ be a primitive isotropic vector such that $( v , L _ { - } ) = \mathbf { Z }$ Then $v \sim _ { \Gamma } e$ (i.e. $v \in \Gamma \{ e \} ,$

Proof.
Apply corollary (3.3） to $v$ and $e$ to conclude $v \sim _ { O ^ { * } ( L _ { - } ) } e$ and a fortiori $v \sim _ { \Gamma } e$

4.2.2Suppose $\mathbf { Z } v \in I _ { 1 } ( L _ { - } )$ and $( v , L _ { - } ) \neq \mathbf { Z }$ Write $v = m a + n b$ with $a \in \mathbf { H } ,$ $b \in { \bf H } ( 2 ) \oplus E _ { 8 } ( - 2 )$ primitive, and $m , n \in \mathbf { Z }$ ； then $( v , L _ { - } ) = \mathbf { Z } m + \mathbf { Z } 2 n$ As $v$ is primitive we must have gcd $( m , n ) = 1$ .It is easy now to conclude $( v , L _ { - } ) = 2 \mathbf { Z }$ .So $\scriptstyle { \frac { 1 } { 2 } } v$ determines a nontrivial element in $L _ { - } ^ { * } / L _ { - }$ .
Our strategy is to do computations in this simpler space,which is endowed with a quadratic form (see $\ S 1$ ,first.
Let

$$
a = h + y \in \frac { 1 } { 2 } { \bf H } ( 2 ) / { \bf H } ( 2 ) \oplus \frac { 1 } { 2 } E _ { 8 } ( - 2 ) / E _ { 8 } ( - 2 ) = L _ { - } ^ { * } / L _ { - }
$$

be isotropic.
Then $0 = q ( a ) = q ( h ) + q ( y )$

Case (i) $q ( h ) = q ( y ) = 0$ In this case $h = 0$ ${ \frac { 1 } { 2 } } e ^ { \prime } + L _ { - }$ or ${ \frac { 1 } { 2 } } f ^ { \prime } + { \cal L } _ { - }$ .
Using

$$
\Gamma _ { q } = \{ g \in O ( L _ { - } ^ { \bullet } / L _ { - } , q ) : g \quad \mathrm { r e s p e c t s ~ t h e ~ d e c o m p o s i t i o n ~ } \}
$$

which is the image of $\Gamma$ under ${ \cal O } ( L _ { - } ) \to { \cal O } ( L _ { - } ^ { \ast } / L _ { - } , q )$ , we can arrange $h = 0$ or $h = { \textstyle \frac { 1 } { 2 } } e ^ { \prime } + L _ { - }$ .From (1.4) we conclude that either $y = 0$ or $y = \frac { 1 } { 2 } \alpha + L _ { - }$ for some $\pmb { \mathscr { x } } \in E _ { 8 } ( - 2 )$ with $\alpha ^ { 2 } = - 8$ As all $( - 8 )$ -vectors in $E _ { 8 } ( - 2 )$ are $O ( E _ { 8 } ( - 2 ) )$ -equivalent (by an argument similar to the one preceding (2.2)),we see that in this case the possibilities modulo $\Gamma _ { q }$ are $\begin{array} { r } { a = 0 , \frac { 1 } { 2 } e ^ { \prime } + L _ { - } } \end{array}$ and $\textstyle { \frac { 1 } { 2 } } e ^ { \prime } + { \frac { 1 } { 2 } } { \boldsymbol { \alpha } } + { \boldsymbol { L } } _ { - }$

Case (ii) $q ( h ) = q ( y ) = 1 \in { \bf Z } / 2$ Here we have: $\begin{array} { r } { h = \frac { 1 } { 2 } e ^ { \prime } + \frac { 1 } { 2 } f ^ { \prime } + L _ { - } } \end{array}$ and $\begin{array} { r } { y = \frac { 1 } { 2 } \omega + L _ { - } } \end{array}$ with $\omega \in E _ { 8 } ( - 2 )$ ， $\omega ^ { 2 } = - 4$ (again using (1.4).
So in this case there is, mod $\Gamma _ { q }$ ,only one possibility: $\begin{array} { r } { \frac { 1 } { 2 } e ^ { \prime } + \frac { 1 } { 2 } f ^ { \prime } + \omega + L _ { - } } \end{array}$

These four vectors in $L _ { - } ^ { * } / L _ { - }$ can all be ‘lifted’ to primitive isotropic vectors in $L _ { - }$ .
To see this consider $e ^ { \prime } , 2 e + 2 f + \alpha , e ^ { \prime } + 2 f ^ { \prime } + \alpha ( \alpha \in E _ { 8 } ( - 2 )$ $\alpha ^ { 2 } = - 8 ) , e ^ { \prime } + f ^ { \prime } + \omega ( \omega \in E _ { 8 } ( - 2 ) , \omega ^ { 2 } = - 4 )$

4.2.3 Proposition.Let $v \in L _ { \cdot , \cdot }$ bea primitive isotropic vector.
Then $v$ is in the $\Gamma$ orbit of one of the following vectors: $e , e ^ { \prime } , e ^ { \prime } + f ^ { \prime } + \omega , e ^ { \prime } + 2 f ^ { \prime } + \dot { \alpha } , 2 e + 2 f + \alpha ( \alpha , \omega \in$ $E _ { 8 } ( - 2 ) , \alpha ^ { 2 } \ = \ - 8 , \omega ^ { 2 } \ = \ - 4 )$ .
Moreover, these five vectors are all inequivalent modulo $\Gamma$

Proof.
By (4.2.1) we may assume $v \in 2 L _ { - } ^ { \star }$ .Then $\scriptstyle { \frac { 1 } { 2 } } v$ determines a nontrivial isotropic element in $L _ { - } ^ { * } / L _ { - }$ .
The discussion above implies the existence of a $g \in \Gamma$ such that for the induced $\overline { { g } } \in \Gamma _ { q }$ we have $\begin{array} { r } { \overline { { g } } ( \frac { 1 } { 2 } v + L _ { - } ) = \frac { 1 } { 2 } \beta + L _ { - } } \end{array}$ where $\beta$ is one of the vectors mentioned in the proposition $( { \tt b u t } \ne e )$ .
Now apply (3.3) to conclude $v \sim _ { \Gamma } \beta$ ，

The last statement of the proposition is easy.□

4.2.4 Remark.
It follows form (4.2.3) that $\widehat { \Omega } _ { - } / \Gamma$ contains precisely five zerodimensional boundary components.

# 4.3 One-dimensional boundary components

The one-dimensional boundary components correspond to $\Gamma$ -orbits of primitive isotropic planes in $L _ { - }$ To determine $I _ { 2 } ( L _ { - } ) / \Gamma$ we use Vinberg's work on hyperbolic reflection groups [26].

4.3.1If $v \in L _ { - }$ is primitive isotropic, then the quotient ${ \pmb v } ^ { \perp } / { \pmb Z } { \pmb v }$ inheritsa quadratic form of hyperbolic signature (which is (1,9) here),and the stabilizer $\Gamma _ { v }$ of $v$ determines a subgroup $G _ { v } \subset O ( v ^ { \perp } / \mathbf { Z } v )$ If $F \in I _ { 2 } ( L _ { - } )$ contains $v$ ,then $F$ determines an element of $I _ { 1 } ( v ^ { \perp } / \mathbf { Z } v )$ .
Vinberg's results can be used to find $I _ { 1 } ( v ^ { \perp } / \mathbf { Z } v ) / G _ { v }$ .If we follow this procedure for each of the five equivalence classes of isotropic primitive vectors (4.2.3)，we will end up with a complete list of $I _ { 2 } ( L _ { - } ) \bmod { \Gamma }$ ,though we must be careful as the same $F$ will occur for different $v$

4.3.2We briefly discuss Vinberg's results.Let $N$ be a nondegenerate lattice of signature $( 1 , n )$ (in the application we have in mind $n = 9$ ）and let $C$ be one of the connected components of

$$
\{ x \in N _ { \mathbb { R } } = N \otimes \mathbb { R } : ( x , x ) > 0 \} .
$$

The quotient $\Lambda ( N ) \ = \ C / { \bf R } _ { + }$ is the associated Lobachevskii space.
Points of $\widehat { \Lambda ( N ) } - \Lambda ( N )$ where $\overrightarrow { \Lambda ( N ) }$ denotes the closure of $\Lambda ( N )$ in $( N _ { \mathbf { R } } - \{ 0 \} ) / \mathbf { R } _ { + }$ are called points at infinity and correspond to isotropic lines in $N _ { \mathbf { R } }$ Let $G$ be a subgroup of $O _ { C } ( N )$ $\left( = \right.$ isometries of $N$ which fix $C$ of finite index and let $W ( G )$ be it subgroup generated by reflections $s _ { v } \in G$ ，where

$$
s _ { v } ( x ) = x - { \frac { 2 ( x , v ) } { ( v , v ) } } v \quad ( ( v , v ) < 0 ) .
$$

If $W ( G )$ is of finite index in $G$ ，then it has a polyhedral fundamental domain $P \subset \Lambda ( N )$ of finite volume, some of whose vertices however are at infinity and

$$
G = W ( G ) \rtimes S ,
$$

where $s$ is a subgroup of the group of symmetries of $P$ .
The polyhedron $P$ and the group $W ( G )$ can best be described in terms of its Dynkin diagram.
Suppose $P$ is bounded by hyperplanes $H _ { i } \left( i \in I \right)$ , none of which is superfuous,orthogonal to $e _ { i }$

$$
P = \{ x \in C : ( x , e _ { i } ) \geq 0 , \forall i \in I \} / \mathbf { R } _ { + } .
$$

The Dynkin diagram $\Sigma ( G )$ is then constructed as follows: the vertices represent the indices $i \in I$ (or the faces of $P$ ).
The vertices $i$ and $j$ are then connected as shown in the table below.
Here $g _ { i j } = ( e _ { i } , e _ { j } ) / { \sqrt { ( e _ { i } , e _ { i } ) ( e _ { j } , e _ { j } ) } }$ and (if $\vert g _ { i j } \vert \le 1$ $m _ { i j }$ is the positive integer such that $g _ { i j } = \cos ( \pi / m _ { i j } )$ (then $m _ { i j }$ is the order of the product of reflections $s _ { e _ { i } } \ s _ { e _ { j } } )$

![](images/056a102c543b40e79455d25bf36fd92c890271c8521f5aa9c6698fe09acd340e.jpg)  
Fig.
2.

If $( e _ { i } , e _ { i } ) \neq ( e _ { j } , e _ { j } )$ ， then an arrow $( > )$ points in the direction of the vector with smallest (absolute) length.

4.3.3In this setting Vinberg shows:

1.every isotropic line in $N _ { \mathbf { Q } }$ is $W ( G )$ -equivalent to some vertex at infinity of $P$ ：  
2.the vertices at infinity of $P$ correspond to the parabolic subdiagrams of rank $n - 1$ of $\sum ( G )$

Here a diagram is called parabolic if each of its connected components is an extended Dynkin diagram as in [26],table 2. The rank of a parabolic diagram is the number of vertices minus the number of connected components.It is clear that the group S can be identified with a subgroup of the symmetry group of $\sum \{ G \}$ and so by using (4.3.3) $I _ { 1 } ( N )$ .modulo $G$ can be determined (for each parabolic subdiagram a suitable linear combination of the vectors corresponding to the vertices in this subdiagram yields a representative isotropic vector, see [27],(1.9)).
Vinberg also describes an effective algorithm to determine the diagram $\sum ( G )$ Roughly speaking,it comes down to the following.
Take a vector $x \in C \cap N$ Then look for hyperplanes $H _ { 1 } = e _ { 1 } ^ { \perp } , H _ { 2 } = e _ { 2 } ^ { \perp } , . .$ (where $s _ { e _ { 1 } } , s _ { e _ { 2 } } , \ldots \in \ W ( G ) )$ such that $H _ { 1 }$ is closest to $x$ (in $\Lambda ( N )$ ; according to Vinberg this means that the expression

$$
\frac { ( x , y ) ^ { 2 } } { | ( y , y ) | }
$$

is minimal for $\boldsymbol { y } = \boldsymbol { e } _ { \mathrm { i } } \mathrm { \cdot } \mathrm { \nabla }$ and $e _ { 2 }$ is such that $( e _ { 1 } , e _ { 2 } ) \not \equiv 0$ and $H _ { 2 }$ is closest to $x$ under the above conditions, and so on.

4.3.4 Lemma.Let $v$ be one of the five vectors in (4.2.3).
Then $v ^ { \perp } / Z v \cong$ $\mathbf { H } \oplus E _ { 8 } ( - 2 )$ for $v \neq e$ and $e ^ { \perp } / \mathbf { Z } e \cong \mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 2 )$

Proof.The claim is trivial for $v = e $ If $v \in { \bf H } ( 2 ) \oplus E _ { 8 } ( - 2 )$ ,then

$$
v \sim _ { o ( \mathrm { { H } } ( 2 ) \oplus E _ { 8 } ( - 2 ) ) } e ^ { \prime }
$$

and clearly $( e ^ { \prime } ) ^ { \perp } / { \bf Z } e ^ { \prime } \cong { \bf H } \oplus E _ { 8 } ( - 2 )$ .We are left with the case $v = 2 e + 2 f + \alpha$ It suffices to show $e ^ { \prime } \sim _ { o ( L _ { - } ) } 2 e + 2 f + \alpha$ To see this look at the diagram of $E _ { 8 } ( - 2 )$ We may assume $\alpha \in E _ { 8 } ( - 2 )$ has coeficients as indicated.
(An argument as given just above (2.2) shows that there is only one $( - 8 )$ -vector modulo $O ( E _ { 8 } ( - 2 ) . )$

![](images/989298e666b4ee474f3bca6379ee2215d88efbd74c1bb342fb8239ff7ac3bc41.jpg)  
Fig.
3.

Consider $y : = \alpha + 2 ( \alpha _ { 1 } + e ^ { \prime } + 2 f ^ { \prime } )$ ，then $y ^ { 2 } = 0$ It follows from (3.3) that $y \sim _ { O ^ { \bullet } ( L _ { - } ) } 2 e + 2 f + \alpha$ Now $y \in { \bf H } ( 2 ) \oplus E _ { 8 } ( - 2 )$ and therefore $y \sim e ^ { \prime }$ □

We treat each of the five cases of (4.2.3) separately.
Set $G _ { v } : = { \mathrm { I m a g e } }$ of $\Gamma _ { v }$ in $O ( v ^ { \perp } / \mathbf { Z } v )$ ,where $\Gamma _ { v } = \{ g \in \Gamma : g ( v ) = v \}$ .
The first case is:

4.3.5 $e _ { \parallel }$ ，The summand $M ( 2 )$ of $L _ { - }$ projects isomorphically onto $e ^ { \perp } / \mathbf { Z } e$ It is easy to see that $G _ { e } = \{ g \in O ( M ( 2 ) )$ ：the induced map on $M ( 2 ) ^ { * } / M ( 2 )$ respects the decomposition}.

The diagram of the reflection group $W _ { e } \subset G _ { e }$ is as follows.

![](images/2053b8dbc8adbf77ff0b8aa1885f6114a76cb7a55d46aaf7bd669b00c9f1a762.jpg)  
Fig.
4.

$$
\begin{array} { l } { \alpha _ { \vartheta } = f ^ { \prime } - e ^ { \prime } } \\ { \alpha _ { 1 0 } = \bar { \alpha } _ { \vartheta } + 2 e ^ { \prime } } \\ { \alpha _ { 1 1 } = 2 e ^ { \prime } + 2 f ^ { \prime } + \bar { \alpha } _ { 1 } + \bar { \alpha } _ { \vartheta } } \\ { \alpha _ { 1 2 } = 5 e ^ { \prime } + 3 f ^ { \prime } + 2 \bar { \alpha } _ { 2 } } \end{array}
$$

Let us indicate Vinberg's algorithm in this case.
As our vector $x$ we take $x = e ^ { \prime } + f ^ { \prime }$ .
Orthogonal to $x$ we find ${ \mathfrak { A } } _ { 1 } , \dots , { \mathfrak { A } } _ { 8 }$ and $\alpha _ { 9 }$ Then $\alpha _ { 1 0 }$ satisfies $( \alpha _ { 1 0 } , \alpha _ { i } ) \geq 0 , i = 1 , \ldots , 9 .$ ,it minimalizes the expression mentioned above (under therestriction that the reflection S10 belongs to $\Gamma _ { e } ,$ ).
In the same way we find $\alpha _ { 1 1 }$ and $\alpha _ { 1 2 }$ .
We have

$$
{ \frac { ( \alpha _ { 1 0 } , e ^ { \prime } + f ^ { \prime } ) ^ { 2 } } { | ( \alpha _ { 1 0 } , \alpha _ { 1 0 } ) | } } = 4 , \quad { \frac { ( \alpha _ { 1 1 } , e ^ { \prime } + f ^ { \prime } ) ^ { 2 } } { | ( \alpha _ { 1 1 } , \alpha _ { 1 1 } ) | } } = 1 6 , \quad { \frac { ( \alpha _ { 1 2 } , e ^ { \prime } + f ^ { \prime } ) ^ { 2 } } { | ( \alpha _ { 1 2 } , \alpha _ { 1 2 } ) | } } = 6 4 .
$$

Note that $\{ \overline { { \alpha } } _ { i } , \alpha _ { i } \} = 2$ ,because we are working in $E _ { 8 } \{ - 2 )$ .It is left to the reader to verify that the symmetries of the diagram come from isometries in $G _ { e }$ (these can then be lifted to $\Gamma _ { e }$ by letting them be the identity on the $\mathbf { H }$ -summand).
So

$$
G _ { e } \cong \{ \pm 1 \} W _ { e } \rtimes S _ { e }
$$

where $S _ { e } \cong \mathbf { Z } / 2 \times \mathbf { Z } / 2$ .
The maximal parabolic subdiagrams (modulo symmetries) are indicated below.

In this way we have (essentially) computed $I _ { 1 } ( e ^ { \perp } / { \bf Z } e ) / G _ { e }$ .It is straightforward now to compute explicitly isotropic vectors representing these four classes.
We leave this to the reader.

![](images/bc13591003db12010416dec9dd71ede172eee96d3d6d47d6706923131df2200c.jpg)  
Fig.
5.

Note that we do not only find four equivalence classes in $I _ { 1 } ( e ^ { \perp } / { \bf Z } e )$ ,but that we find four labelled classes,the labelling being given by the root systems $\widetilde { A } _ { 7 } \oplus \widetilde { A } _ { 1 }$ etc. We may therefore speak of an isotropic plane of type $\widetilde { A } _ { 7 } \oplus \widetilde { A } _ { 1 }$ or $A _ { 7 } \oplus A _ { 1 }$ etc. These four classes are not distinguished by the isomorphism type of $F ^ { \bot } / F$ where $F \in I _ { 2 } ( L _ { - } )$ is one of the above types.
In all cases we even find the same isomorphism type,namely $E _ { 8 } ( - 2 )$ ，because modulo $O ( L _ { - } )$ the four types are equivalent.
But things change if we consider such isotropic planes as sublattices of the polarized $K 3$ lattice of degree 4

$$
L _ { 4 } : = ( e + f , e + f , 0 ) ^ { \perp }
$$

$\left( \subset M \oplus M \oplus \mathbf { H } = L \right)$ .
Here we can distinguish them by looking at $F ^ { \bot } / F$ and its (generalized) type [23], 5.6.10 and $\ S 6 .$ Scattone [loc.cit.],p.100 lists the following nine possibilities:

$$
\begin{array} { r l } & { E _ { 8 } ( - 1 ) \Phi { \cal E } _ { 8 } ( - 1 ) \Phi < - 4 > ; } \\ & { D _ { 1 6 } ( - 1 ) \Phi < - 4 > ; } \\ & { E _ { 8 } ( - 1 ) \Phi { \cal D } _ { 9 } ( - 1 ) ; } \\ & { E _ { 7 } ( - 1 ) \Phi { \cal E } _ { 7 } ( - 1 ) \Phi A _ { 3 } ( - 1 ) ; } \\ & { D _ { 1 7 } ( - 1 ) ; } \\ & { D _ { 1 2 } ( - 1 ) \Phi { \cal D } _ { 5 } ( - 1 ) ; } \\ & { D _ { 8 } ( - 1 ) \Phi D _ { 8 } ( - 1 ) \Phi < - 4 > ; } \\ & { A _ { 1 5 } ( - 1 ) \Phi A _ { 1 } ( - 1 ) \Phi A _ { 1 } ( - 1 ) ; } \\ & { E _ { 6 } ( - 1 ) \Phi A _ { 1 1 } ( - 1 ) . } \end{array}
$$

What is behind this of course,is the fact that not all elements of $O ( L _ { - } )$ can be lifted to $O ( L _ { 4 } )$ .In $\ S 5$ we shall find an application for the remarks above when we look at the relation with Shah's work [24].

The four classes that we have found so far correspond to four onedimensional boundary components in $\widehat { \Omega } _ { - } / \Gamma$ which have the zero-dimensional boundary component corresponding to $e$ in their closure.
The root systems occurring in the diagrams are not without geometric significance.
See $\ S$ and Part II.

${ \pmb 4 . 3 . 6 \ e ^ { \prime } }$ In this case $( e ^ { \prime } ) ^ { \perp } / \mathbf { Z } e ^ { \prime }$ can be identified with the sublattice $\mathbf { H } \oplus E _ { 8 } ( - 2 )$ of $L _ { - }$ .
It is evident that $G _ { e ^ { \prime } } = O ( \mathbf { H } \oplus E _ { 8 } ( - 2 ) )$

The diagram of the reflection subgroup looks like:

$$
\begin{array} { l } { \alpha _ { \vartheta } = \bar { \alpha } _ { \vartheta } + 2 f } \\ { \alpha _ { 1 0 } = e - f } \\ { \circ : ( - 4 ) - \mathrm { v e c t o r } } \\ { \bullet : ( - 2 ) - \mathrm { v e c t o r } } \end{array}
$$

![](images/e027acbbce8ea4ba63178b01592fa713e1b8bedc0b448ed34529158e063c96f7.jpg)  
Fig.
6.

As there are no symmetries we have

$$
O ( \mathbf { H } \oplus E _ { 8 } ( - 2 ) ) = \{ \pm 1 \} \cdot W _ { e ^ { \prime } } .
$$

![](images/1ea53614e2c0e1518c3636f7f18aec94bddd6ed756809274519159428c2c3dd1.jpg)  
Fig.
7.

In the picture we see the two maximal parabolic subdiagrams.
The equivalence class of rank 2 primitive isotropic latices corresponding to the first parabolic subdiagram is the same as the one labelled ${ \widetilde { E } } _ { 8 }$ in (4.3.5).
It is represented by the lattice spanned by $^ e$ and $e ^ { \prime }$

4.3.7. $e ^ { \prime } + f ^ { \prime } + \overline { { \alpha } } _ { 8 }$ Set $v = e ^ { \prime } + f ^ { \prime } + \overline { { \alpha } } _ { 8 }$ By lemma (4.3.4） we have $v ^ { \perp } / \mathbf { Z } v \cong$ $\mathbf { H } \oplus E _ { 8 } ( - 2 )$ a basis of $\pmb { v } ^ { \perp } / \pmb { Z } \pmb { v }$ being $e , f , \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { 7 } , - f ^ { \prime } + \alpha _ { 8 }$

The diagram of the reflection subgroup of $G _ { v }$ is:

![](images/23b802e0e8ed8daefb138a1ab66921cc85e900e38d7c8c1465f36f94867bff85.jpg)  
Fig.
8.

The $\mathbf { z }$ -span of the roots is

$$
\mathbf { Z } \{ \alpha _ { 1 } , \ldots , \alpha _ { 7 } , \alpha _ { 8 } - f ^ { \prime } , e + f , e - f \} .
$$

It can be checked that the symmetry of the diagram comes from an element in $\Gamma _ { v }$ (see (4.3.10)).
We find

$$
G _ { v } = \{ \pm 1 \} W _ { v } \rtimes \mathbf { Z } / 2 .
$$

The parabolic subdiagrams of maximal rank (up to symmetry) are:

![](images/885f617c02fd2a03ec1ee9e64533effccdff243dcce3c13c5e5f495d99ea6e44.jpg)  
Fig.
9.

The $\widetilde { E } _ { 7 } \oplus \widetilde { A } _ { 1 }$ -diagram determines the same equivalence class of isotropic planes as the $\widetilde { E } _ { 7 } \oplus \widetilde { A } _ { 1 }$ -diagram in (4.3.5): the isotropic vector we read off from that diagram is $\alpha _ { 9 } + \alpha _ { 1 0 } = ( f ^ { \prime } - e ^ { \prime } ) + ( \overline { { { \alpha } } } _ { 8 } + 2 e ^ { \prime } ) = e ^ { \prime } + f ^ { \prime } = \overline { { { \alpha } } } _ { 8 } .$

4.3.8 $2 e ^ { \prime } + f ^ { \prime } + \overline { { \alpha } } _ { 1 }$ .Let $v = 2 e ^ { \prime } + f ^ { \prime } + \overline { { \alpha } } _ { 1 }$ ,then a basis for $v ^ { \perp } / \mathbf { Z } v \cong \mathbf { H } \oplus E _ { 8 } ( - 2 )$ is $e , f , - e ^ { \prime } + \alpha _ { 1 }$ ， $\alpha _ { 2 }$ ， $\alpha _ { 8 }$ .
The diagram for the reflection subgroup of $G _ { v }$ is as in the picture below.

$$
\begin{array} { l l l l l l } { { } } & { { } } & { { } } & { { } } & { { \alpha _ { 9 } = f - e } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { \alpha _ { 1 0 } = \bar { \alpha } _ { 3 } + 2 e ^ { \prime } } } \\ { { \displaystyle \alpha _ { 1 1 } \quad \alpha _ { 3 } \quad \alpha _ { 4 } \quad \alpha _ { 5 } \quad \alpha _ { 6 } \quad \alpha _ { 7 } \quad \alpha _ { 8 } \quad \alpha _ { 1 2 } \quad \alpha _ { 9 } } } & { { } } & { { \alpha _ { 1 1 } = e + f + \alpha _ { 1 } - e ^ { \prime } } } \\ { { } } & { { } } & { { } } & { { } } & { { \displaystyle \prod _ { \alpha _ { 2 } } \quad \alpha _ { 3 } - \sum _ { \alpha _ { 1 3 } } e ^ { \alpha _ { 3 } } } } & { { } } & { { \alpha _ { 1 2 } = 2 e - 2 e ^ { \prime } + \bar { \alpha } _ { 8 } - \bar { \alpha } _ { 1 2 } } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \alpha _ { 2 } } } & { { } } & { { \alpha _ { 1 0 } } } & { { } } & { { } } & { { } } \end{array}
$$

Fig.
10.

The roots span the sublatice

$$
{ \bf Z } \{ e + f , e - f , - e ^ { \prime } + \alpha _ { 1 } , \alpha _ { 2 } , \dots , \alpha _ { 8 } \}
$$

and the symmetry is induced by an element of $\Gamma _ { v }$ (see (4.3.10)).We obtain the following maximal parabolic subdiagrams (modulo symmetry):

![](images/627f9a50255f4b05eda4229739ffb32e92dc7649811e8b452401d617ea5dfb64.jpg)  
Fig.
11.

The diagram labelled ${ \widetilde { D } } _ { 8 }$ (resp.
${ \tilde { C } } _ { 8 } \rangle$ ） represents the same class of isotropic planes as the one labelled ${ \widetilde { D } } _ { 8 }$ (resp.
${ \widetilde { C } } _ { 8 } )$ in (4.3.5) (resp.
(4.3.7)).

4.3.9 $2 e + 2 f + \widetilde { \alpha } _ { 1 }$ .Set $v = 2 e + 2 f + \overline { { \alpha } } _ { 1 }$ .We have the following basis for ${ \pmb v } ^ { \perp } / { \pmb Z } { \pmb v }$ $\widetilde { e } = e + e ^ { \prime } + f ^ { \prime } - \alpha _ { 1 }$ $\widetilde { f } = f + e ^ { \prime } + f ^ { \prime } - \alpha _ { 1 }$ $\widetilde { \alpha } _ { 1 } = e ^ { \prime } - f ^ { \prime }$ ， $\widetilde { \alpha } _ { 2 } = \alpha _ { 2 }$ $\widetilde { \pmb { \alpha } } _ { 3 } = { \pmb f } ^ { \prime } + { \pmb \alpha } _ { 3 } ,$ $\widetilde { \alpha } _ { 4 } = \alpha _ { 4 } , \dots$ ， $\widetilde { \alpha } _ { 8 } = \alpha _ { 8 } ; \widetilde { e } , \widetilde { f }$ span a $\mathbf { H }$ -summand, $\widetilde { \alpha } _ { 1 } , \dots , \widetilde { \alpha } _ { 8 }$ an $E _ { 8 } ( - 2 )$ -summand.

We obtain the following diagram:

![](images/67a42f79352428e16d967eba20db240dc408f3f2345877e50e19d09163f83d52.jpg)  
Fig.
12.

$$
\begin{array} { r l } & { \alpha _ { 9 } = 2 \bar { e } - \tilde { \alpha } _ { 1 } } \\ & { \alpha _ { 1 0 } = 2 \bar { e } + \left( \bar { \tilde { \alpha } } _ { 2 } - \bar { \tilde { \alpha } } _ { 3 } \right) } \\ & { \alpha _ { 1 1 } = \bar { f } - \tilde { e } } \\ & { \alpha _ { 1 2 } = \bar { e } + \bar { f } + \left( \bar { \tilde { \alpha } } _ { 6 } - \bar { \tilde { \alpha } } _ { 3 } \right) } \\ & { \alpha _ { 1 3 } = \bar { e } + \tilde { f } + \left( \bar { \tilde { \alpha } } _ { 1 } + \bar { \tilde { \alpha } } _ { 6 } - \bar { \tilde { \alpha } } _ { 3 } \right) } \\ & { \alpha _ { 1 4 } = \tilde { e } + \tilde { f } + \bar { \alpha } _ { 3 } } \end{array}
$$

The span of the roots in this case is

$$
\mathbf { Z } \{ \widetilde e + \widetilde f , \widetilde e - \widetilde f , \widetilde { \alpha } _ { 1 } , \widetilde { \alpha } _ { 2 } , \dots , \widetilde { \alpha } _ { 8 } \} .
$$

Symmetries of the graph can be lifted to $\Gamma _ { v }$ (see (4.3.10)).Parabolic subdiagrams of maximal rank (up to symmetry) arc as indicated below.

![](images/6f3518ca224172e4064baac02c7c15f637ab2c67925dc4145cd81a7663407ecc.jpg)  
Fig.
13.

The diagram labelled $\widetilde { A } _ { 7 } \oplus \widetilde { A } _ { 1 }$ (resp.
$\widetilde { C } _ { 8 } , \widetilde { C } _ { 6 } \oplus \widetilde { C } _ { 2 } , \widetilde { C } _ { 4 } \oplus \widetilde { C } _ { 4 } )$ represents the same class of isotropic planes as the one labelled $\widetilde { A } _ { 7 } \oplus \widetilde { A } _ { 1 }$ (resp.
$\widetilde { B } _ { 8 } , \widetilde { B } _ { 6 } \oplus \widetilde { C } _ { 2 } , \widetilde { B } _ { 4 } \oplus \widetilde { B } _ { 4 } )$ in (4.3.5) (resp.
(4.3.6), (4.3.7), (4.3.8)).

4.3.10To check whether a symmetry of a diagram lifts to the stabilizer group of the corresponding isotropic vector, one can proceed as follows.
Note that in the last cases (4.3.7), (4.3.8), (4.3.9)) the span of the roots occurring in the diagram is of the form ${ \bf Z } \{ e - f , e + f \} \oplus E _ { 8 } ( - 2 ) ( e , f$ standard basis for H).Firstly, we show that isometries of this lattice extend to $\mathbf { H } \oplus E _ { 8 } ( - 2 )$

Let $K = I \oplus I ( - 1 ) \oplus E _ { 8 } ( - 1 )$ $I$ denotes a rank one lattice here,such that $( x , x ) = 1$ for a generator $x$ ).Thelattice $K$ is odd and unimodular of signature (1,9).
Suppose ${ \pmb I } = { \bf Z } { \pmb v }$ $I ( - 1 ) = \mathbf { Z } w$ .Consider the inclusion $\mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 1 ) \subset K$ where $\mathbf { H } ( 2 ) = \mathbf { H } ( 2 ) = \mathbf { Z } \{ v + w , v - w \}$

4.3.11 Lemma.
$\mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 1 )$ is the largest even sublattice of $K$

Proof.
Let $\widetilde { K }$ be an even sublatice and let $a v + b w + \alpha \in \widetilde { K } \ ( a , b \in { \mathbf Z } , \alpha \in E _ { 8 } ( - 1 ) )$ Then $\qquad \alpha ^ { 2 } - b ^ { 2 } \equiv 0 { \bmod { 2 } }$ and consequently $a - b$ and $a + b$ are even.
But then

$$
a v + b w + \alpha = \left( \frac { a + b } { 2 } \right) ( v + w ) + \left( \frac { a - b } { 2 } \right) ( v - w ) + \alpha \in { \bf H } ( 2 ) \oplus E _ { 8 } ( - 1 )
$$

which finishes the proof.□

Let $\Lambda = { \bf H } \oplus E _ { 8 } ( - 2 ) \ /$ $( \mathbf { H } = \mathbf { Z } \{ e , f \} )$ and let

$$
K ^ { \prime } = \mathbf { Z } \{ e + f , e - f \} \oplus E _ { 8 } ( - 2 ) \subset \Lambda
$$

a sublattice of index 2. Note that $K ^ { \prime } \cong K ( 2 )$

4.3.12 Proposition.Every $g \in O ( K ( 2 ) )$ extends to an isometry of $\Lambda$

Proof.The inclusion $K ^ { \prime } = K ( 2 ) \hookrightarrow \Lambda$ induces $\Lambda ^ { * } \hookrightarrow K ^ { \prime * }$ and so

$$
\begin{array} { r l } { { \Lambda ^ { * } ( 2 ) } } & { { } \hookrightarrow \quad \frac { 1 } { 2 } K ( 4 ) \cong K } \\ { { | | } } & { { } \mathstrut } & { { | | } } \\ { { \mathbf { H } ( 2 ) \oplus \frac { 1 } { 2 } E _ { 8 } ( - 4 ) } } & { { } } & { { \mathbf { Z } \{ \frac { 1 } { 2 } ( e + f ) , \frac { 1 } { 2 } ( e - f ) \} \oplus \frac { 1 } { 2 } E _ { 8 } ( - 4 ) } } \end{array}
$$

a situation as described in the lemma.
Now let $g \in O ( K ( 2 ) )$ ,then $g$ acts on $K ( 2 ) ^ { * }$ and therefore both $\Lambda ^ { * } ( 2 ) \subset K$ and $g ( \Lambda ^ { \ast } ( 2 ) ) \subset K$ satisfy the conditions of the lemma.
So $g ( \Lambda ^ { \bullet } ( 2 ) ) = \Lambda ^ { \bullet } ( 2 )$ .But then $g$ fixes $\Lambda$ i.e. $g \in O ( \Lambda )$ □

Actually, the resulting injection $O ( K ( 2 ) ) \subset O ( \Lambda )$ is an isomorphism.To see this, we give an intrinsic description of the sublattice $K ( 2 ) \subset \Lambda$

4.3.13 Proposition.
$K ( 2 )$ is the unique rank 10 sublattice $\widetilde { \Lambda }$ of $\Lambda$ such that $\begin{array} { r } { \widetilde { \Lambda } ^ { * } = \frac { 1 } { 2 } \widetilde { \Lambda } } \end{array}$ and $\frac 1 2 \widetilde { \Lambda } ( 2 )$ is odd.

Proof.First of all $K ( 2 )$ indeed satisfies $K ( 2 ) ^ { \bullet } \ = \ { \textstyle { \frac { 1 } { 2 } } } K ( 2 ) , { \textstyle { \frac { 1 } { 2 } } } K ( 4 )$ is odd.
Now suppose $\widetilde { \Lambda } \subset \Lambda$ satisfies these properties.
Then we have

$$
{ \bf H } \oplus { \frac { 1 } { 2 } } E _ { 8 } ( - 2 ) = \Lambda ^ { * } \hookrightarrow \widetilde { \Lambda } ^ { * } = { \frac { 1 } { 2 } } \widetilde { \Lambda } \subset { \frac { 1 } { 2 } } \Lambda = { \frac { 1 } { 2 } } { \bf H } \oplus { \frac { 1 } { 2 } } E _ { 8 } ( - 2 ) \quad ( \mathrm { o f ~ i n d e x ~ } 4 ) .
$$

The following two alternatives do not occur :

1 $\widetilde { \Lambda } ^ { \bullet } = \Lambda ^ { \bullet }$ ,for then $\widetilde { \Lambda } = 2 \Lambda ^ { * } = 2 { \bf H } \oplus E _ { 8 } ( - 2 )$ ， contradicting $\widetilde { \Lambda } ^ { * } = { \textstyle \frac { 1 } { 2 } } \widetilde { \Lambda }$  
2. $\begin{array} { r } { \widetilde \Lambda ^ { * } = \frac { 1 } { 2 } \Lambda , } \end{array}$ for then $\widetilde { \Lambda } = \Lambda$ and we arrive again at a contradiction.

Therefore the image of $\widetilde { \Lambda } ^ { * }$ under ${ \widetilde { \Lambda } } ^ { \bullet }  { \textstyle { \frac { 1 } { 2 } } } \Lambda / \Lambda ^ { \bullet } ( = { \textstyle { \frac { 1 } { 2 } } } { \bf H } / { \bf H } )$ is of order two.
If X= Z²e+Zf +Eg(-2),then A = Ze+ Z2f + E8(-2) and ¹(2) is even.
Likewise,A\*= Ze+Z¹f +E8(-2) is impossible.
The only posibility left is:

$$
\widetilde { \Lambda } ^ { * } = \left( { \bf Z } { \frac { 1 } { 2 } } ( e + f ) + { \bf H } \right) \oplus { \frac { 1 } { 2 } } E _ { 8 } ( - 2 )
$$

and so

$$
\widetilde \Lambda = ( \mathbf { Z } ( e + f ) + 2 \mathbf { H } ) \oplus E _ { 8 } ( - 2 ) = \mathbf { Z } \{ e + f , e - f \} \oplus E _ { 8 } ( - 2 ) = K ( 2 ) .
$$

Consequently any $g \in O ( \Lambda )$ preserves the sublattice $K ( 2 )$ .
Another proof,perhaps closer to the methods of this paragraph, is based on Vinberg's theory.
It comes down to checking that the Dynkin diagrams for $O ( \Lambda )$ and $O ( K ( 2 ) )$ are the same.

In the cases (4.3.7), (4.3.8) and (4.3.9)， we define a decomposition of $L _ { - }$ as follows.

$$
\begin{array} { l l l l l l } { { v = e ^ { \prime } + f ^ { \prime } + \overline { { { \alpha } } } _ { 8 } } } & { { e , f } } & { { \begin{array} { l l l l l } { { \oplus } } & { { { \bf H } ( 2 ) } } & { { \oplus } } & { { E _ { 8 } ( - 2 ) } } & { { } } \\ { { v , f ^ { \prime } } } & { {  } } & { {  } } & { {  } } & { {  } } & { {  } } \\ { { v = 2 e ^ { \prime } + f ^ { \prime } + \overline { { { \alpha } } } _ { 1 } } } & { { e , f } } & { { e ^ { \prime } , v } } & { {  } } & { { - e ^ { \prime } + \alpha _ { 1 } , \alpha _ { 2 } , \dots , \alpha _ { 8 } } } & { { } } \\ { { v = 2 e + 2 f + \overline { { { \alpha } } } _ { 1 } } } & { { \widetilde e , \widetilde { f } } } & { { v , e - \widetilde e } } & { { } } & { { \widetilde \alpha _ { 1 } , \dots , \widetilde \alpha _ { 8 } } } & { { } } \end{array} } } &  { \begin{array} { l } { { } } } \end{array} \end{array}
$$

Using these decompositions of $L _ { - }$ and the results above, it is fairly easy to lift symmetries of a diagram to isometries of $L _ { - }$ fixing the relevant isotropic vector.
What remains to be checked is that we actually end up in $\Gamma$ This (computational) step as well as the treatment of the case (4.3.5) (which is much easier) is left to the reader.

4.3.14 Remark.
The labeling of isotropic planes, using the parabolic diagrams is not unambiguous.
For instance, $\widetilde { B }$ and $\widetilde { C }$ diagrams sometimes correspond to the same class of isotropic planes.IfF = Zv+Zw ∈ I(L*),then the stabilizers (Gw) and $( G * { v } ) \_ { w }$ are not necessarily isomorphicand this is reflected in thecorresponding affine root systems.
So we must be careful with our terminology.

4.3.15 Remark.
It is not diffcult to see beforehand what types of primitive isotropic vectors may or may not be combined to span an isotropic plane.
For example,the first isotropic vector of the list (4.2.3) can be combined with any of the other four types to yield a primitive isotropic plane, but there is no isotropic plane all of whose primitive isotropic elements are equivalent to e.
To specify the type of an isotropic plane we can also indicate the types of isotropic vectors it contains.For example:

$$
A _ { 7 } \oplus A _ { 1 } \longleftrightarrow \{ 1 , 2 \}
$$

(e (resp.
$e ^ { \prime }$ ）corresponds to an isotropic vector of type 1 (resp.2)).

4.3.16To describe the precise structure of the one-dimensional boundary components we have to compute the group $\Gamma ( F ) = N _ { \Gamma } ( F ) / Z _ { \Gamma } ( F )$ for each type of isotropic plane $F$

Let us first deal with the boundary components of type $E _ { 8 } , \ D _ { 8 } , \ A _ { 7 } \oplus A _ { 1 }$ and $E _ { 7 } \oplus A _ { 1 }$ (we occasionally forget about $( - 1 ) s ,$ ，which should not give rise to confusion).
Let $E \in I _ { 2 } ( L _ { - } )$ be of the form $\boldsymbol { E } = \mathbf { Z } e + \mathbf { Z } v$ where $v \in { \bf H } ( 2 ) \oplus E _ { 8 } ( - 2 )$ and so $( v , L _ { - } ) = 2 \mathbf { Z }$ Then $v$ is in the $O ( \mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 2 ) )$ -orbit of $e ^ { \prime }$ and hence there is a decomposition.

$$
L _ { - } \cong { \bf H } \oplus { \bf H } ( 2 ) \oplus E ^ { \perp } / E
$$

with $E \subset { \mathbf { H } } \oplus { \mathbf { H } } ( 2 )$ Suppose $g \in N _ { \Gamma } ( E )$ and write $g ( e ) = a e + c v , g ( v ) = b e + d v ,$ As $( e , L _ { - } ) = { \bf Z }$ and $( v , L _ { - } ) = 2 \mathbf { Z }$ we find $( g ( e ) , L _ { - } ) = { \bf Z } $ so $a$ is odd and $( g ( v ) , L _ { - } ) = 2 \mathbf { Z }$ so $b$ is even.
Conversely，any element of $G L ( E )$ satisfying these restrictions is easily seen to extend to an element of $O ^ { * } ( L _ { - } )  \colon$ just use the decomposition $L _ { - } \cong { \bf H } \oplus { \bf H } ( 2 ) \oplus E ^ { \perp } / E$ .
In conclusion:

$$
\Gamma ( E ) \cap S L ( E ) \cong \left\{ \left( \begin{array} { l l } { { a } } & { { 2 b } } \\ { { c } } & { { d } } \end{array} \right) \in S L _ { 2 } ( { \bf Z } ) \right\} = \Gamma ^ { 1 } ( 2 ) ,
$$

(a congruence subgroup of $S L _ { 2 } ( \mathbf { Z } ) )$ .
The corresponding boundary components $B _ { E }$ are isomorphic to $H / \Gamma ^ { 1 } ( 2 )$ ((4.1)) and we have also seen how a natural ( $\left( = \right.$ SatakeBaily-Borel) compactification is constructed: $\widehat { H } / \Gamma ^ { 1 } ( 2 )$ ，where ${ \widehat { H } } = H \cup \mathbf { Q } \cup \{ \infty \}$ is endowed with the horocycle topology.
The closure of $B _ { E }$ in $\widehat { \Omega } _ { - } / \Gamma$ is obtained from $\widehat { H } / \Gamma ^ { 1 } ( 2 )$ by possibly identifying some of the cusps.
However, the fact that each of the isotropic planes of type $E _ { 8 } , D _ { 8 } , A _ { 7 } \oplus A _ { 1 } , E _ { 7 } \oplus A _ { 1 }$ is built up from two nonequivalent isotropic vectors implies that no identification among the cusps occurs.

4.3.17The computations in the remaining five cases are more involved.
(We refer the reader to [23], Chap.
5,for more details.
） By explicit computation one finds a splitting

$$
L _ { - } \cong { \bf H } ( 2 ) \oplus { \bf H } ( 2 ) \oplus F ^ { \perp } / F
$$

where $F$ denotes the isotropic plane.
It is then easy to see that $\Gamma \cap S L ( F )$ contains $\Gamma ( 2 )$ ，the level 2 subgroup of $S L _ { 2 } ( \mathbf { Z } )$ (under the appropriate identifications).
The number of inequivalent (mod $\Gamma$ ）primitive isotropic vectors in $F$ restricts the possibilities even further.
If necessary，the use of certain Siegel-Eichler transformations finishes the job.Let us illustrate the last two steps for $F$ of type $\{ 3 , 4 \}$ .From (4.3.7) we see that

$$
F = \mathbf { Z } ( v = e ^ { \prime } + f ^ { \prime } + \overline { { \alpha } } _ { 8 } ) \oplus \mathbf { Z } \omega
$$

with $\omega = \alpha _ { 9 } + \alpha _ { 1 2 } + \alpha _ { 1 } + \alpha _ { 3 } + \alpha _ { 4 } + \alpha _ { 5 } + \alpha _ { 6 } + \alpha _ { 7 } + \alpha _ { 1 3 } .$ Suppose $g \in N _ { F }$ $g ( v ) = a v + b \omega ( a , b \in \mathbf { Z } )$ As $\omega$ is of type 4 (i.e. $\omega \sim _ { \Gamma } 2 e ^ { \prime } + f ^ { \prime } + \overrightarrow { \alpha } _ { 1 } ) \textit { k }$ $b$ must be even.
So we find

$$
\Gamma ( 2 ) \subset \Gamma ( F ) \cap S L ( F ) \subset \Gamma ^ { 1 } ( 2 )
$$

with

$$
\Gamma ^ { 1 } ( 2 ) = \Biggl \{ \left( \begin{array} { r r } { { a } } & { { c } } \\ { { b } } & { { d } } \end{array} \right) \in S L _ { 2 } ( { \bf Z } ) : b \mathrm { ~ e v e n } \Biggr \} .
$$

Now consider the Siegel-Eichler transformation $E _ { v , \frac { e ^ { \prime } - f ^ { \prime } } { 2 } } : L _ { - }  L _ { - }$ given by

$$
y \mapsto y + \bigg ( y , \frac { e ^ { \prime } - f ^ { \prime } } { 2 } \bigg ) v - \frac { 1 } { 2 } \bigg ( \frac { e ^ { \prime } - f ^ { \prime } } { 2 } \bigg ) ^ { 2 } ( y , v ) v - ( y , v ) \frac { e ^ { \prime } - f ^ { \prime } } { 2 } .
$$

It is easily checked that $E _ { v , \frac { e ^ { \prime } - f ^ { \prime } } { 2 } } \in N _ { F }$ and that

$$
E _ { v , \frac { e ^ { \prime } - f ^ { \prime } } { 2 } } ( v ) = v , \quad E _ { v , \frac { e ^ { \prime } - f ^ { \prime } } { 2 } } ( \omega ) = \omega - v .
$$

Conclusion : $\Gamma ( F ) \cap S L ( F ) \cong \Gamma ^ { 1 } ( 2 )$

Summarizing then, the results about the stabilizers of the remaining five types are as follows:

$$
\begin{array} { r l } { F \mathrm { o f ~ t y p e } \left\{ 2 , 4 , 5 \right\} : } & { \Gamma ( F ) \cap S L ( F ) \cong \Gamma ( 2 ) ; } \\ { F \mathrm { o f ~ t y p e } \left\{ 4 , 5 \right\} : } & { \Gamma ( F ) \cap S L ( F ) \cong \Gamma ^ { 1 } ( 2 ) ; } \\ { F \mathrm { o f ~ t y p e } \left\{ 3 , 5 \right\} : } & { \Gamma ( F ) \cap S L ( F ) \cong \Gamma ^ { 1 } ( 2 ) ; } \\ { F \mathrm { o f ~ t y p e } \left\{ 3 , 4 \right\} : } & { \Gamma ( F ) \cap S L ( F ) \cong \Gamma ^ { 1 } ( 2 ) ; } \\ { F \mathrm { o f ~ t y p e } \left\{ 5 , 5 \right\} : } & { \Gamma ( F ) \cap S L ( F ) \cong \Gamma L _ { 2 } ( \mathbf { Z } ) . } \end{array}
$$

4.4The incidence relations between boundary components (resp.
equivalence classes of isotropic sublattices) can be represented by a diagram as follows.
A closed (resp.
open) dot represents a zero-dimensional (resp.one-dimensional) boundary component or, equivalently, the corresponding $\Gamma$ -equivalence class of primitive isotropic rank one (resp.two) sublattices of $L _ { - }$ .
The specific type a dot represents is also indicated.
An open dot representing a boundary component $B$ is connected with a closed dot representing a boundary point $p$ if $p \in { \overline { { B } } }$ If $B$ corresponding to $[ E ] \in I _ { 2 } ( L _ { - } ) / \Gamma$ and $p$ to $[ { \bf Z } v ] \in I _ { 1 } ( L _ { - } ) / \Gamma$ this means that $E$ contains a vector equivalent to $v$

![](images/a0bcf6e7f4c33978f80800dc1e9444c0c8c42ccf97d72cb4228d6113d2e84568.jpg)  
Fig.14.Incidence relations between the boundary components

If we forget about the almost polarization, i.e.replace $\Gamma$ by $o ( L _ { - } )$ ,the results about the boundary components would be as follows.

4.5 Proposition.
There are only two types of primitive isotropic vectors in $L _ { - }$ modulo $O ( L _ { - } )$ ,representatives being e and $e ^ { \prime }$

Proof.
$e$ and $e ^ { \prime }$ are certainly inequivalent as $( e , L _ { - } ) = { \bf Z }$ and $( e ^ { \prime } , L _ { - } ) = 2 { \bf Z }$ It remains to show that $e ^ { \prime } , 2 e + 2 f + \alpha , e ^ { \prime } + f ^ { \prime } + \alpha$ and $e ^ { \prime } + f ^ { \prime } + \omega$ are all equivalent.
As $\mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 2 )$ contains only one primitive isotropic vector modulo $O ( \mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 2 ) )$ we may restrict our attention to $2 e + 2 f + \alpha .$ Now use the proof of 4.3.4.

4.6 Proposition.
There are two types of primitive isotropic rank 2 sublattices modulo $O ( L _ { - } )$ ，

Proof.
Let $F$ be an isotropic plane and suppose that $e \in F$ Then $F$ determines a primitive isotropic rank 1 sublattice in $e ^ { \perp } / \mathbf { Z } e = \mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 2 )$ As all primitive isotropic elements of $\mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 2 )$ are in the same $O ( \mathbf { H } ( 2 ) \oplus E _ { 8 } ( - 2 ) )$ -orbit we may assume that this sublattice is generated by $e ^ { \prime }$ i.e. $F = \mathbf { Z } e \oplus \mathbf { Z } e ^ { \prime }$ ，

Suppose $e ^ { \prime } \in F$ ，then in $e ^ { \prime \perp } / { \bf Z } e ^ { \prime }$ we find two types of isotropic vectors according to our earlier computations (see (4.3.6)).
One of them leads again to $\mathbf { Z } e \oplus \mathbf { Z } e ^ { \prime }$ ,the other one only contains primitive isotropic vectors equivalent to $e ^ { \prime }$ ， so is not equivalent to the previous one.□

As to the stabilizers of the two one-dimensional boundary components we have

4.7 Proposition.
$I f F$ is equivalent to $\mathbf { Z } e \oplus \mathbf { Z } e ^ { \prime }$ ,then $N _ { F } / Z _ { F } \cap S L ( F ) \cong \Gamma ^ { 1 } ( 2 )$ .In the other case $N _ { F } / Z _ { F } \cap S L ( F ) \cong S L ( F )$

Proof.
The argument we gave in the case of $\Gamma$ also works here for the first case.
As for the second case use our result for the boundary component of type{5,5}.
□

# 5A first comparison with Shah's results

In [24] J.
Shah uses the techniques of geometric invariant theory [16],GIT for short, to study projective degenerations of Enriques surfaces.
As we saw before $( \ S 2 )$ ,any Enriques surface $T$ can be obtained as a quotient of a $K 3$ surface $s$ of degree 4 which itself is a double cover of $\Sigma _ { 0 }$ or $\Sigma _ { 2 } ^ { 0 }$ (a cone over a smooth quadric in $\mathbf { P } ^ { 2 }$ ).The covering involution of $s \to T$ is a lift of $I : \Sigma _ { 0 } \to \Sigma _ { 0 }$ given by

$$
I ( ( x _ { 0 } : x _ { 1 } ) , ( y _ { 0 } : y _ { 1 } ) ) = ( ( x _ { 0 } : - x _ { 1 } ) , ( y _ { 0 } : - y _ { 1 } ) ) .
$$

By doing GIT in the space of branch curves (bidegree (4,4)） he finds a list of standard forms of central fibres of one-parameter degenerations of Enriques surfaces.He subdivides this list according to what he calls the type.

5.1 ·Type I\*:MHS on $H ^ { 2 }$ of the double cover is pure of weight 2. · Type II\*: MHS on $H ^ { 2 }$ of the double cover has $h ^ { 0 , 0 } = 0 , h ^ { 1 , 0 } \neq 0 .$ · Type III\*: MHS on $H ^ { 2 }$ of the double cover has $h ^ { 0 , 0 } \neq 0$

(MHS: mixed Hodge structure.)

In this paragraph we willink the Type II\* branch curve configurations on $\Sigma _ { 0 }$ of his list with the one-dimensional Satake-Baily-Borel boundary components (because of this link, they are also referred to as type II boundary components; similarly,zero-dimensional boundary components are said to be type III boundary components） of the Satake-Baily-Borel compactification $\widehat { \Omega } _ { - } / \Gamma$ To be more accurate, suppose $X ~  ~ \triangle$ isa one-parameter degeneration of

Enriques surfaces with central fibre of type II\*.
The corresponding period map $p : \triangle ^ { * } \to \Omega _ { - } / \Gamma$ extends to a holomorphic map

$$
\smash { \widetilde { p } : \triangle \to \widehat { \Omega } _ { - } / \Gamma }
$$

by Borel's extension theorem [4].The limit point $\overline { { p } } ( 0 )$ will be an element of a type II Satake-Baily-Borel boundary component which we shall determine.In proving this we modify the covering family of K3's so that we obtain a family in which the central fibre is a stable $K 3$ in the sense of Friedman [1O].
The Clemens-Schmid exact sequence is then used to find the isotropic plane which determines the boundary component.
The results are summarized in (5.15).

Let us briefly recall some of the relevant facts about ‘stable $K 3 \mathbf { s } ^ { \prime }$ See [10] for further details.
Firstly recall the following result due to Kulikov [13] and Persson-Pinkham [20].

5.2 Theorem.Let $\pi : X \to \triangle$ be a semistable degeneration of $K 3$ surfaces with all components of the central fibre ${ \pi } ^ { - 1 } ( 0 ) \ = \bigcup _ { i } \ \bar { V } _ { i }$ algebraic,and let $N =$ logarithm of the monodromy on $H ^ { 2 } ( X _ { t } )$ .
Then，after birational modifications,it may be assumed that $K _ { X } \sim 0$ In this case $\pi ^ { - 1 } ( 0 )$ is one of the following:

(1) Type I: $\pi ^ { - 1 } ( 0 )$ is a smooth $K 3$ surface and $N = 0$ (2) Type $I \colon \pi ^ { - 1 } ( 0 ) = V _ { 0 } \cup V _ { 1 } \cup . . . \cup V _ { r } ; V _ { 0 }$ and $V _ { r }$ are smooth rational, $V _ { 1 } , \dots , V _ { r - 1 }$ smooth elliptic ruled and $V _ { i } \cap V _ { j } \neq \emptyset$ if and only ij $\begin{array} { r } { \dot { ~ } j = i \pm 1 . } \end{array}$ 1f $V _ { i }$ and $V _ { j }$ meet, the intersection is a smooth elliptic curve and a section of the ruling on $V _ { i }$ if $V _ { i }$ is elliptic ruled.
$N \neq 0 , N ^ { 2 } = 0 .$

(3) Type I: $\pi ^ { - 1 } ( 0 ) = \bigcup _ { i } \ V _ { i }$ ，where each $\widetilde { V } _ { i }$ $^ { r } =$ normalization of $V _ { i \textrm { \tiny i } }$ ）is smooth rational and all double curves are cycles of rational curves.
The dual graph is $a$ triangulation of the sphere $S ^ { 2 } . ~ N ^ { 2 } \ne 0 , ~ N ^ { 3 } = 0 ,$

We will be concerned (of course) with the surfaces of type II.
Note the various uses of the same terminology type I, $\Gamma ^ { \star }$ etc. This reflects the intimate connections of the corresponding notions.
This paragraph will illustrate this point again.

5.3 Definition.Let X be a variety with normal crosings and let D := Xing (singular locus).
If

$$
( T _ { X } ^ { 1 } : = ) \operatorname { E x t } ^ { 1 } ( \Omega _ { X } ^ { 1 } , { \mathcal { O } } _ { X } ) \cong { \mathcal { O } } _ { D } \qquad .
$$

then $X$ is called $d$ -semistable.(This notion is inspired by deformation theory.
It is useful in dealing with ‘smoothability’ matters.)

5.4If $X = V _ { 0 } \cup V _ { 1 }$ is a union of two smooth surfaces meeting normally along a smooth curve $D$ ,then

$$
X { \mathrm { i s ~ } } d { \mathrm { - s e m i s t a b l e } } \quad \Leftrightarrow \quad N _ { D / V _ { 0 } } \otimes N _ { D / V _ { 1 } } \cong { \mathcal { O } } _ { D }
$$

5.5 Definition.
A stable $K 3$ surface of type I is a $d$ -semistable surface (5.3) of the form $X ~ = ~ V _ { 0 } \cup V _ { 1 }$ as in (5.2) type II $( r ~ = ~ 1 )$ such that $D = X _ { \mathrm { s i n g } } = V _ { 0 } \cap V _ { 1 } \in | - K _ { V _ { i } } |$ for $i = 0 , 1$

5.6Now suppose a stable $K 3$ surface $X _ { 0 }$ occurs as the central fibre in a semistable degeneration $\pi : X \to \triangle$ .
The Clemens-Schmid exact sequence [6]

relates the limiting mixed Hodge structure (LMHS) $L H ^ { 2 } ( \widetilde { X } ^ { \ast } )$ and the canonically defined mixed Hodge structure on $H ^ { 2 } ( X _ { 0 } )$ .The central fibre $X _ { 0 }$ comes with a canonical Cartier divisor

$$
\xi = \mathcal { O } _ { X } ( V _ { 0 } ) | X _ { 0 }
$$

which restricts to

$$
\xi | V _ { 0 } = \mathcal { O } _ { V _ { 0 } } ( - D ) , \quad \xi | V _ { 1 } = \mathcal { O } _ { V _ { 1 } } ( D ) .
$$

5.7 Facts.
i) The following portion of the Clemens-Schmid sequence,

$$
H _ { 4 } ( X _ { 0 } )  H ^ { 2 } ( X _ { 0 } )  L H ^ { 2 } ( \widetilde { X } ^ { * } ) \stackrel { N } {  } L H ^ { 2 } ( \widetilde { X } ^ { * } ) ,
$$

is exact over $\mathbf { Z }$

ii $W _ { 1 } H ^ { 2 } ( X _ { 0 } ) \cong W _ { 1 } L H ^ { 2 } ( \widetilde { X } ^ { * } )$

ii) $I f \xi$ is viewed as a class in $H ^ { 2 } ( V _ { 0 } ) \oplus H ^ { 2 } ( V _ { 1 } )$ then $\xi ^ { 2 } = 0$ and:

$$
W _ { 2 } L H ^ { 2 } ( \widetilde { X } ^ { \ast } ) / W _ { 1 } L H ^ { 2 } ( \widetilde { X } ^ { \ast } ) \cong \{ \xi \} ^ { \perp } / { \bf Z } \xi .
$$

iv) $W _ { 1 } L H ^ { 2 } ( \widetilde { X } ^ { \ast } ) = \operatorname { I m } N$ is a primitive isotropic sublattice of $L H ^ { 2 } ( \widetilde { X } ^ { \ast } )$ of rank 2.

5.8 Definition.
A polarization on a stable $K 3$ surface $X$ of type $\mathrm { I I }$ isa Cartier divisor $L$ on $X$ which is numerically effective and satisfies $L ^ { 2 } > 0$ Two polarizations $L _ { 1 }$ and $L _ { 2 }$ are called equivalent if

$$
L _ { 1 } \equiv L _ { 2 } \mod \xi
$$

i.e. $L _ { 1 }$ and $L _ { 2 }$ define the same class in $H ^ { 2 } ( X ; \mathbf { Z } / \mathbf { Z } \xi$

Now consider a branch curve configuration $C _ { 0 } ( \subset \Sigma _ { 0 } )$ of type II\* as in Shah's list [24], p.
482and assume,for simplicity,that it issuficiently general.
Note that $C _ { 0 }$ hasan $I$ -invariant equation, say $f _ { 0 }$ Let $C$ be a general curve of bidegree (4,4) on $\Sigma _ { 0 }$ with $I$ -invariant equation $f$ and consider the one-parameter family of curves over the disk $\bigtriangleup$ (which may be made smaller if necessary;we shall not bother about such details)

$$
\mathscr { C } : = \{ C _ { t } : C _ { t } \mathrm { ~ \ h a s ~ e q u a t i o n ~ } f _ { 0 } + t f \mathrm { ~ \ w h e r e ~ } t \in \triangle \} \subset \Sigma _ { 0 } \times \triangle .
$$

Take the double cover branching along this $\mathcal { C }$ This yields a one-parameter degeneration $X  \triangle$ of $K 3 \mathbf { \ ' } \mathbf { s }$ of degree 4, together with an involution $I$ which lifts the involution on $\textstyle \sum _ { 0 }$ The quotient $X / I  \bigtriangleup$ is then a degeneration of Enriques surfaces.
As usual we have a period map

$$
p : \triangle ^ { * }  \Omega _ { - } / \Gamma .
$$

Let $\Omega _ { 4 }$ be the period domain for $K$ 3's of degree 4, $\Gamma _ { 4 }$ the corresponding arithmetic group associated with the lattice $L _ { 4 }$ (see (4.3.5)).
The inclusion $\Omega _ { - } \subset \Omega _ { 4 }$ induces $\Omega _ { - } / \Gamma \to \Omega _ { 4 } / \Gamma _ { 4 }$ and the composition

$$
\triangle ^ { * }  \Omega _ { - } / \Gamma  \Omega _ { 4 } / \Gamma _ { 4 }
$$

is the period map for the restriction of the family $X  \triangle$ to $\triangle ^ { * }$ .
The first thing we shall do is study the extension

$$
\triangle  \widehat { \Omega } _ { 4 } / \Gamma _ { 4 } .
$$

Suppose we have modified the family so that the central fibre is a polarized stable $K 3$ Then $\mathbf Ḋ \mathbf Ḋ N Ḍ Ḍ$ determines the isotropic plane corresponding to the boundary component we are looking for (modulo the involution $I$ ).The isomorphism type of ker $N / \operatorname { I m } N$ (within $L _ { 4 }$ ） completely determines the equivalence class of $\operatorname { I m } N$ in $I _ { 2 } ( L _ { 4 } )$ and $\Gamma _ { 4 }$ and using (5.7ii) this quotient $\mathbf { k e r } N / \operatorname { I m } N$ can be computed.
Below we shall discuss this procedure for some of the nine types of configurations in Shah's list (referring for more details concerning the other cases to [25]） and then return to the original question.

5.9First we reproduce Shah's list of branch curves as far as we need it, describing only‘generic' members of his list.The branch curve is called $B$

1. $B = 2 C$ where $C$ is a smooth genus one curve whose equation is $I$ -invariant.

2. $B = 2 C$ ，where $C$ is a smooth genus one curve whose equation is $I$ -antiinvariant.

3. $B = 2 C + B _ { 0 } .$ where $C$ has bidegree (1,1) and is $I$ -invariant, and where $B _ { 0 }$ is a genus one curve as in (1.).

4 $B = C + I ( C ) + L + I ( L )$ ,where $C$ is a twisted cubic and $L$ is a line such that $C , I ( C )$ and $\pmb { L }$ are mutually tangent at a point $P$ (and therefore $C , I \{ C \}$ and $I ( L )$ are mutually tangent at $I ( P ) )$ .
None of the curves passes through a fixed point of $I$

5. $B$ has two quadruple points $P$ and $P ^ { \prime } , B$ consists of four distinct curves of  
   bidegree (1,1),each passing through $P$ and $P ^ { \prime }$  
   a) $P$ and $P ^ { \prime }$ are fixed by $\pmb { I }$  
   b $P$ and $P ^ { \prime }$ are not fixed by $I$

6. $B = 2 C + L + I ( L )$ ，where $C$ is a twisted cubic and $L$ is a line which is not an edge (the four lines $x _ { 0 } = 0 , x _ { 1 } = 0 , y _ { 0 } = 0 , y _ { 1 } = 0$ are called the edges),such that $C \cap L$ consists of two distinct points.
   $C$ is $\pmb { I }$ -invariant and contains exactly two points of the fixed locus of $\pmb { I }$ which are connected by an edge.

7. $B$ consists of lines, $B = 2 C + 2 C ^ { \prime } + L + I ( L ) + I ( L ^ { \prime } )$ with $C$ and $C ^ { \prime }$ skew, $L$ and $L ^ { \prime }$ skew and neither $L$ nor $L ^ { \prime }$ an edge.  
   a) $C ^ { \prime } = I ( C )$  
   b） $C$ and $C ^ { \prime }$ are different edges.

5.10Case (1.).
Let $C _ { 0 }$ be a smooth genus one curve on $\Sigma _ { 0 }$ as in case (1.) above, so that $B = 2 C _ { 0 }$ A general curve $c$ intersects $C _ { 0 }$ in 16(distinct） points $\boldsymbol { p } _ { 1 } , \dots , \boldsymbol { p } _ { 1 6 }$ The resulting flat divisor ${ \mathcal { C } } \subset \Sigma _ { 0 } \times \triangle$ exhibits ordinary double points at $p _ { 1 } , \ldots , p _ { 1 6 }$ (local equation $x ^ { 2 } + t y = 0 )$ .The double cover $X  \triangle$ therefore has singularities at the 16 points lying over $p _ { 1 } , \ldots , p _ { 1 6 }$ (local equation $z ^ { 2 } + x ^ { 2 } + t y = 0 )$ Blow up these points.
It introduces 16 exceptional surfaces $S _ { 1 } , \ldots , S _ { 1 6 }$ ${ \mathrm { a l l } } \cong { \Sigma } _ { 0 }$ in the central fibre.The components $S _ { i }$ meet the strict transform of the original two components in the central fibre in a sum of fibres: $S _ { i S _ { i } } = - F _ { 1 , i } - F _ { 2 , i }$ Using the Nakano criterion we see that we can smoothly blow down the $S _ { i } ^ { \phantom { \dagger } } \mathbf { s }$ along either of the two rulings.This yields a family $\overline { { X } }  \triangle$ where the central fibre consists of two rational components $T _ { 1 }$ and $T _ { 2 }$ glued along an elliptic curve $( C _ { 0 } ) . \ T _ { 1 }$ is obtained from $\Sigma _ { 0 }$ by blowing up some of the points $p _ { 1 } , \ldots , p _ { 1 6 }$ and $T _ { 2 }$ is obtained from $\Sigma _ { 0 }$ by blowing up the remaining ones.
The two rulings of $\Sigma _ { 0 }$ yield generators $E _ { 1 }$ and

$F _ { 1 }$ (resp.
$E _ { 2 }$ and $F _ { 2 }$ of $H ^ { 2 } ( \Sigma _ { 0 } ; \mathbf { Z } ) \subset H ^ { 2 } ( T _ { 1 } ; \mathbf { Z } )$ (resp.
$H ^ { 2 } ( \Sigma _ { 0 } ; { \bf Z } ) \subset H ^ { 2 } ( T _ { 2 } ; { \bf Z } ) )$ Let $e _ { 1 } , \ldots , e _ { i }$ (resp.
$f _ { 1 } , \dots , f _ { 1 6 - i } )$ denote the exceptional classes in $H ^ { 2 } ( T _ { 1 } ; \mathbf { Z } )$ (resp.
$H ^ { 2 } ( T _ { 2 } ; \mathbf { Z } ) )$ .Then the polarization class in $H ^ { 2 } ( T _ { 1 } ) \oplus H ^ { 2 } ( T _ { 2 } )$ is $h = E _ { 1 } + F _ { 1 } + E _ { 2 } + F _ { 2 }$ and the class $\xi ~ ( ( 5 . 6 ) - ( 5 . 7 ) )$ is given by

$$
\xi = 2 E _ { 1 } + 2 F _ { 1 } - e _ { 1 } - \cdot \cdot \cdot \cdot - e _ { i } - 2 E _ { 2 } - 2 F _ { 2 } + f _ { 1 } + \cdot \cdot \cdot + f _ { 1 6 - i } .
$$

Now look for the roots in $\xi ^ { \perp } / \mathbf { Z } \xi \cap h ^ { \perp }$ ：

$$
\begin{array} { r l r l } { \underset { e _ { 1 } \to - e _ { 2 } } {  } \dotsm \dotsm \dotsm \dotsm \frac { e _ { i } + f _ { 1 } e _ { - i } } { e _ { i - 1 } - e _ { i } } \dotsm \dotsm \dotsm \dotsm \dotsm } & & { A _ { 1 ^ { \delta } } ( - 1 ) } \\ & { } & & { } \\ { E _ { 1 } - F _ { 1 } } & { \bullet } & { A _ { 1 } ( - 1 ) } \\ & { } & & { } \\ & { E _ { 2 } - F _ { 2 } } & { \bullet } & { A _ { 1 } ( - 1 ) } \end{array}
$$

Fig.
15.

If you do everything compatibly with the involution $I$ ,then we may assume that $p _ { 9 } = I p _ { 1 } , \dotsc , p _ { 1 6 } = I p _ { 8 }$ and that $T _ { 1 }$ (resp.
$T _ { 2 } ) ^ { \mathbf { \lambda } }$ is blown up in $p _ { 1 } , \ldots , p _ { 8 }$ (resp.
$I p _ { 1 } , \ldots , I p _ { 8 } )$ .
The involution acts on the diagram as indicated.

![](images/538052ab95116effa91233f3ca58c4923ae3149d5e47a7a3638af178f93feafe.jpg)  
Fig.
16.

5.11 Remark． Considering vectors $\alpha - I \alpha$ where $\pmb { \alpha }$ occurs in the above diagram, one obtains a diagram of type $A _ { 7 } \oplus A _ { 1 }$ , suggesting what the relation with Enriques surfaces is.

5.12Case (2.
） is similar to case (1.).
The difference is in the action of the involution.

5.13Case (3.).
$C _ { 0 } = 2 B + \Gamma$ where $B$ is an $I$ -invariant curve of bidegree (1,1) and $\Gamma$ is $I$ -invariant of bidegree (2,2) Blow up $\Sigma _ { 0 } \times \triangle$ along $B \times \{ 0 \}$ .This creates a copy of $\Sigma _ { 2 }$ in the central fibre which meets the strict transform of $\Sigma _ { 0 } \times \{ 0 \}$ in its unique section $E$ with $E ^ { 2 } = - 2$ If $F$ denotes a fibre of $\Sigma _ { 2 }$ w.r.t.
the ruling, then the strict transform $\widehat { \mathcal { C } }$ of the branching divisor $\mathscr { C }$ meets $\Sigma _ { 2 }$ in a smooth curve $\widetilde \Gamma \in | 2 E + 8 F |$ .Now take the double cover branching over $\widehat { \pmb { \mathscr { C } } }$ In the central

fibre we obtain two components:

$$
\begin{array} { r l } & { S _ { 1 }  \Sigma _ { 2 } , \mathrm { ~ a ~ d o u b l e ~ c o v e r ~ b r a n c h i n g ~ o v e r ~ } \widetilde \Gamma ; } \\ & { S _ { 2 }  \Sigma _ { 0 } , \mathrm { ~ a ~ d o u b l e ~ c o v e r ~ b r a n c h i n g ~ o v e r ~ } \Gamma . } \end{array}
$$

By using Castelnuovo's criterion,one shows that $S _ { 1 }$ and $S _ { 2 }$ are rational with $h ^ { 2 } ( S _ { 1 } ) = 1 4 , h ^ { 2 } ( S _ { 2 } ) = 6$ .
The computational data are (we may think of $S _ { 1 }$ and $s _ { 2 }$ as being obtained by blowing up $\mathbf { P } ^ { 1 } \times \mathbf { P } ^ { 1 }$ ; the $e _ { i }$ denote exceptional classes, $E _ { i }$ and $F _ { i }$ come from the rulings on $\mathbf { P } ^ { 1 } \times \mathbf { P } ^ { 1 }$ ：

$$
\begin{array} { l } { { \xi = ( 2 E _ { 1 } + 2 F _ { 1 } - e _ { 1 } - \dots - e _ { 1 2 } ) - ( 2 F _ { 2 } + 2 F _ { 2 } - f _ { 1 } - \dots - f _ { 4 } ) ; } } \\ { { \nonumber } } \\ { { h = 2 ( e _ { 1 } + 2 F _ { 1 } - e _ { 1 } - e _ { 2 } ) + 2 E _ { 2 } + 2 F _ { 2 } - f _ { 1 } - \dots - f _ { 4 } . } } \end{array}
$$

The rootsystem is:

![](images/cac5145b5e8ed975a16dbce9300b0751c3def3c3f49fc3369d7d104636b8ea1c.jpg)  
Fig.
17.

5.14In Shah's list nine types of Type II\* degenerations occur and our computations yielded nine type II Satake-Baily-Borel boundary components.
Any $F _ { - } \in I _ { 2 } ( L _ { - } )$ determines via $L _ { - } \subseteq L _ { 4 }$ an element $F$ in $I _ { 2 } ( L _ { 4 } )$ , and, modulo $\Gamma _ { 4 : }$ ，these can be distinguished by ${ \cal F } ^ { \bot } / { \cal F }$ (see (4.3.5)).
The above computations give us the following correspondence.

$$
\begin{array} { r l r l } { 1 . ~ D _ { 1 6 } ( - 1 ) } & { \oplus \langle - 4 \rangle : } & & { \mathrm { c a s e ~ ( 6 . ) . } } \\ { 2 . ~ D _ { 1 2 } ( - 1 ) } & { \oplus D _ { 5 } ( - 1 ) : } & & { \mathrm { c a s e ~ ( 3 . ) . } } \\ { 3 . ~ E _ { 8 } ( - 1 ) } & { \oplus E _ { 8 } ( - 1 ) \oplus \langle - 4 \rangle : } & { \mathrm { c a s e ~ ( 4 . ) . } } \\ { 4 . ~ D _ { 8 } ( - 1 ) } & { \oplus D _ { 8 } ( - 1 ) \oplus \langle - 4 \rangle : } & { \mathrm { c a s e ~ ( 7 a ) ~ a n d ~ ( 7 b ) . } } \\ { 5 . ~ E _ { 7 } ( - 1 ) } & { \oplus E _ { 7 } ( - 1 ) \oplus A _ { 3 } ( - 1 ) : } & { \mathrm { c a s e ~ ( 5 a ) ~ a n d ~ ( 5 b ) . } } \\ { 6 . ~ A _ { 1 5 } ( - 1 ) } & { \oplus A _ { 1 } ( - 1 ) \oplus A _ { 1 } ( - 1 ) : \mathrm { c a s e ~ ( 1 . ) ~ a n d ~ ( 2 . ) } . } \end{array}
$$

For a pair of configurations in one of the last three situations, the two can be distinguished by the isomorphism type of ${ F _ { - } ^ { \perp } } / { F _ { - } }$ for the corresponding isotropic plane.The above considerations set up a bijective correspondence between the nine configurations and the nine one-dimensional Satake-Baily-Borel boundary components.
To make this more explicit,consider the following map

$$
I _ { 2 } ( L _ { - } ) / \Gamma  I _ { 2 } ( L _ { 4 } ) / \Gamma _ { 4 }
$$

induced by $L _ { - } \subseteq L _ { 4 }$ .
Computation (in which the diagrams of $\ S 3$ can be of help, since the root systems there should be the ‘anti-invariant part' of a root system occurring for some $F \in I _ { 2 } ( L _ { 4 } ) )$ yields:

$$
\begin{array} { r l r l } & { E _ { 8 } \bmod \Gamma } & & { \mapsto E _ { 8 } \oplus E _ { 8 } \oplus \left. - 4 \right. \bmod \Gamma _ { 4 } } \\ & { D _ { 8 } \bmod \Gamma } & & { \mapsto D _ { 8 } \oplus D _ { 8 } \oplus \left. - 4 \right. \bmod \Gamma _ { 4 } } \\ & { E _ { 7 } \oplus A _ { 1 } \bmod \Gamma } & & { \mapsto E _ { 7 } \oplus E _ { 7 } \oplus A _ { 3 } \bmod \Gamma _ { 4 } } \\ & { A _ { 7 } \oplus A _ { 1 } \bmod \Gamma } & & { \mapsto A _ { 1 5 } \oplus A _ { 1 } \oplus A _ { 1 } \bmod \Gamma _ { 4 } } \\ & { B _ { 6 } \oplus B _ { 2 } \bmod \Gamma } & & { \mapsto D _ { 1 2 } \oplus D _ { 5 } \bmod \Gamma _ { 4 } } \\ & { B _ { 4 } \oplus B _ { 4 } \bmod \Gamma } & & { \mapsto D _ { 8 } \oplus D _ { 8 } \oplus \left. - 4 \right. \bmod \Gamma _ { 4 } } \\ & { B _ { 3 } \oplus B _ { 3 } \oplus B _ { 2 } \bmod \Gamma } & & { \mapsto E _ { 7 } \oplus E _ { 7 } \oplus A _ { 3 } \bmod \Gamma _ { 4 } } \\ & { B _ { 8 } \oplus \mathrm { t y p e } \left\{ 3 , 4 \right\} \bmod \Gamma } & & { \mapsto A _ { 1 5 } \oplus A _ { 1 } \oplus A _ { 1 } \bmod \Gamma _ { 4 } } \\ & { B _ { 8 } \oplus ( \mathrm { t y p e } \left\{ 2 , 4 , 5 \right\} ) \bmod \Gamma \mapsto D _ { 1 6 } \oplus \left. - 4 \right. \bmod \Gamma _ { 4 } } \end{array}
$$

The fact that in the left column all of the last five lattices contain $( - 2 )$ -vectors implies that the corresponding configurations meet the fixed point locus of $\pmb { I }$ on $\Sigma _ { 0 }$ ； it also means that the limit period point is in the closure of the divisor determined by the collection $R _ {  }$ (see (2.10) and (3.6)).

5.15These considerations finally lead to the following correspondence.

1. $B _ { 8 }$ (type {2,4,5}) : case (6.);
2. $B _ { 6 } \oplus B _ { 2 }$ ： case (3.);
3. $E _ { 8 }$ ： case (4.);  
   4 $D _ { 8 }$ ： case $\mathbf { ( 7 a ) }$
4. $B _ { 4 } \oplus B _ { 4 }$ ： case (7b);
5. $E _ { 7 } \oplus A _ { 1 }$ ： case (5b);  
   7 $B _ { 3 } \oplus B _ { 3 } \oplus B _ { 2 } \ ;$ case (5a);
6. $A _ { 7 } \oplus A _ { 1 }$ ： case (1.);
7. $B _ { 8 }$ ： case (2.).

Acknowledgements.The work presented here is based on a chapter of the author's Ph.D.thesis at the Katholieke Universiteit Nijmegen,The Netherlands.I would like to take this opportunity to thank my supervisor,Eduard Looijenga,for introducing me to the subject and for mathematical guidance.Furthermore,I would like to thank Chris Peters for several helpful conversations.

# References

1.Baily, W.L.Jr., Borel,A.: Compactification of arithmetic quotients of bounded symmetric domains.
Ann.
Math.84,442-528 (1966)  
2.Barth,W.,Peters,C.: Automorphisms of Enriques surfaces.Invent.Math.73,383-411 (1983)  
3. Barth,W.,Peters,C.,Van de Ven,A.:Compact complex surfaces,Berlin Heidelberg New York: Springer 1984  
4. Borel,A.: Some metric properties of arithmetic quotients of symmetric spaces and an extension theorem.
J.Differ.Geom.6,543-560 (1972)  
5.Cartan, H.: Quotient d'un espace analytique par un groupe d'automorphismes.
In: Symposium in Honor of S.Lefschetz.Princeton:Princeton University Press 1957  
6.Clemens, C.H.: Degenerations of Kahler manifolds.
Duke Math.J.44,215-290 (1977)  
7. Cossec,F.:On the Picard groups of Enriques surfaces.
Math.Ann.271,577-600 (1985)  
8.Dolgachev,I.: On automorphisms of Enriques surfaces.Invent.Math.76,163-177 (1984)  
9. Friedman,R.: Hodge theory,degenerations,and the global Torell problem.Ph.D.thesis,Harvard University 1981  
10. Friedman,R.:A new proof of the global Toreli theorem for K3 surfaces.Ann.
Math.120, 237--296 (1984)  
11. Horikawa,E.:On the periods of Enriques surfaces I,Math.Ann.234,73-88 (1978)  
12. Horikawa,E.: On the periods of Enriques surfaces II,Math.Ann.235,217-246 (1978)  
13. Kulikov,V.: Degenerations of K3 surfaces and Enriques surfaces,Math.
USSR Isv.11,957-989 (1977)  
14. Looijenga,E.: Semi-toric partial compactifications.Report 8520 (1985)，Department of Mathematics,Catholic University Nijmegen,The Netherlands  
15. Looijenga,E.:New compactifications of locally symmetric varieties.In:Proceedings of the 1984 Vancouver conference in algebraic geometry.
(C.M.S.
Conference Proceedings,vol.
6, pp.
341-364) Providence,Rhode Island:Am.Math.
Soc.1986  
16.Mumford,D.,Fogarty, J.:Geometric invariant theory $2 ^ { \mathfrak { n } \mathfrak { d } }$ edition).Berlin Heidelberg New York: Springer 1982  
17. Namikawa,Y.: Periods of Enriques surfaces.Math.Ann.
270,201-222 (1985)  
18. Nikulin, V.: Integral symmetric bilinear forms and some of their applications.Math.UsSR Izv.
14,103-167 (1980)  
19. Nikulin,V.: Finite automorphism groups of Kahler K3'surfaces.Trans.
Moscow Math.
Soc.38, 71-135 (1980)  
20. Persson, U.,Pinkham,H.: Degenerations of surfaces with trivial canonical bundle.Ann.
Math.
113,45-66 (1981)  
21.Satake,I.: On the compactifications of the Siegel space.J.Indian Math.Soc.20,259-281 (1956)  
22. Satake,I.: On compactifications of quotient spaces for arithmetically discontinuous groups.
Ann.
Math.72,555-580 (1960)  
23. Scattone,F.:On the compactification of moduli spaces for algebraic $K 3$ surfaces.Ph.D.
thesis, Columbia University 1984  
24. Shah,J.: Projective degenerations of Enriques surfaces.Math.Ann.256,475-495 (1981)  
25. Sterk,H.: Compactifications of the period space of Enriques surfaces.Arithmetic and geometric aspects.Ph.D.thesis,Katholieke Unitersiteit Nijmegen, The Netherlands 1988  
26. Vinberg,E.B.:Some arithmetical discrete groups in Lobachevskii spaces.In:Proc.Int.
Coll.
on Discrete Subgroups of Lie Groups and Appl.
to Moduli.
(Tata Institute of Fundamental Research Studies in Mathematics,Vol.7,pp.323-348) Oxford:Oxford University Press 1975  
27. Vinberg,E.B.: The two most algebraic K3 surfaces.Math.Ann.265,1-21 (1983)