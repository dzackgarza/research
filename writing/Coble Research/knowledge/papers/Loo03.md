---
title: 'Compactifications defined by arrangements I: The ball quotient case'
authors:
- Eduard Looijenga
year: 2003
bibkey: Loo03
tags:
- paper
- extraction
abstract: |
  We define a natural compactification of an arrangement complement in a ball quotient.
  We show that when this complement has a moduli space interpretation, then this compactification is often one that appears naturally by means of geometric invariant theory.
  We illustrate this with the moduli spaces of smooth quartic curves and rational elliptic surfaces.
---

# COMPACTIFICATIONS DEFINED BY ARRANGEMENTS I: THE BALL QUOTIENT CASE

EDUARD LOOIJENGA

Abstract.
We define a natural compactification of an arrangement complement in a ball quotient.
We show that when this complement has a moduli space interpretation, then this compactification is often one that appears naturally by means of geometric invariant theory.
We illustrate this with the moduli spaces of smooth quartic curves and rational elliptic surfaces.

# Introduction

We wish to compare two compactifications of an algebro-geometric nature: those obtained by means of geometric invariant theory (GIT) and the ones defined by the Baily-Borel theory ( $B B$ ), in situations were both are naturally defined.
The examples that we have in mind are moduli spaces of varieties for which a period mapping identifies that space with an open-dense subvariety of an arithmetic quotient of a type IV domain or a complex ball.
This includes moduli spaces of (perhaps multiply) polarized $K 3$ -surfaces, Enriques surfaces and Del Pezzo surfaces, but excludes for instance the moduli spaces of principally polarized abelian varieties of dimension at least three.
In these examples, the GIT-boundary parametrizes degenerate forms of varieties, so that this boundary is naturally stratified with strata parametrizing degenerate varieties of the same type.
The strata and their incidence relations have been computed in a number of cases, sometimes after hard work and patient analysis, but we believe that it is fair to say that these efforts failed to uncover any well-understood, predictable pattern.

In this paper and a subsequent part we shall describe in such cases the GITcompactification as a stratified space in terms of the BB-compactification plus some simple data of an arithmetic nature.
Not only will this render the stratified structure more transparant, but we will also see that the theory is strong enough to be able to guess in many cases what the GIT-compactification should be like.

We shall be more explicit now.
Let $\mathbb { B }$ be a complex ball, $\mathbb { L }  \mathbb { B }$ its natural automorphic line bundle and $\Gamma$ an arithmetic group operating properly on $( \mathbb { B } , \mathbb { L } )$ . Then the orbit space $X : = \Gamma \backslash \mathbb { B }$ is a quasiprojective variety and $\mathbb { L }$ descends to an ‘orbiline bundle’ $\mathcal { L }$ over $X$ . The Baily-Borel theory projectively compactifies $X$ by adding only finitely many points (the cusps).
Suppose that we are also given a $\Gamma$ -invariant locally finite union of hyperballs in $\mathbb { B }$ . This determines a hypersurface in $X$ whose complement we shall denote by $X ^ { \circ }$ . The central construction in this paper is a natural projective compactification ${ \widehat { X ^ { \circ } } }$ of $X ^ { \circ }$ that (i) is explicitly given as a blowup of the Baily-Borel compactication of $X$ followed by a blowdown and (ii)

is naturally stratified.
Perhaps the most important property for applications is that the boundary $\widehat { X ^ { \circ } } - X ^ { \circ }$ is everywhere of codimension $\geq 2$ in case every nonempty intersection of the given hyperballs (including the intersection with empty index set, i.e., $\mathbb { B }$ ) has dimension $\geq 2$ .

Here is how this is used.
Let $G$ be a reductive group acting on an integral quasi-projective variety endowed with an ample bundle $( Y , \eta )$ . Assume that we are given a nonempty open subset $U \subset Y$ which is a union of $G$ -stable orbits.
Then $G \backslash ( U , \eta | U )$ exists as a quasi-projective variety with orbiline bundle.
To be precise, the $G$ -invariants in the algebra of sections of powers of $\eta$ is finitely generated and the normalized proj of this graded algebra is a projective variety whose points correspond to the minimal orbits in the semistable part $Y ^ { \mathrm { s s } }$ (and is therefore denoted $G \backslash Y ^ { \mathrm { s s } } )$ and contains $G \backslash U$ as an open-dense subvariety.
Assume that we are given an isomorphism of orbiline bundles

$$
G \backslash ( U , \eta | U ) \cong ( X ^ { \circ } , { \mathcal { L } } | X ^ { \circ } )
$$

for some triple $( X , X ^ { \circ } , { \mathcal { L } } )$ as above.
Assume also that the boundary at each side (so in $G \backslash Y ^ { \mathrm { s s } }$ resp.
$\widehat { X ^ { \circ } }$ ) is of codimension $\geq 2$ . Perhaps contrary to what one might think, there are many examples of interest for which these assumptions are satisfied with the isomorphism in question then being given by a period map.
Then we show that the isomorphism $G \backslash U \cong X ^ { \circ }$ extends to an isomorphism

$$
G \backslash \backslash Y ^ { \mathrm { s s } } \cong { \widehat { X ^ { \circ } } } .
$$

It turns out that in all cases that we are aware of the stratification of $\widehat { X ^ { \circ } }$ has an interpretation in terms of the left hand side.
Among these are the moduli space of quartic curves (equivalently, of degree two Del Pezzo surfaces) and of rational elliptic fibrations admitting a section (equivalently, of degree one Del Pezzo surfaces).

In the course of our discussion we touch briefly on a few topics that are perhaps not indispensable for getting at our main results, but that we included here since they involve little extra effort, can be illuminating to put things in perspective, and have an interest on their own.

One of these starts with the observation that the construction of ${ \widehat { X ^ { \circ } } }$ makes sense and is useful in a wider setting than ball quotients.
For instance, we may take for $X ^ { \circ }$ the complement of an arrangement in a projective space or more generally, in a torus embedding.
This case is relevant for producing a compactification of the universal smooth genus three curve and the universal smooth cubic surface, as they involve adjoint tori of type $E _ { 7 }$ and $E _ { 6 }$ respectively.
We showed on previous occasions ([10], [13]) that these constructions are sufficiently explicit for calculating the orbifold fundamental group of these universal objects.
(This enabled us to find a new, natural, simple presentation of the pointed mapping class group of genus three.)

Another such topic concerns a relatively simple nontrivial necessary condition that an ‘arithmetic’ locally finite union of hyperballs in a complex ball must satisfy in order that it be the zero set of an automorphic form (Section 6).

Let us finally point out that this paper builds on work of ours that goes back to the eighties, when we set out to understand the semi-universal deformations of triangle singularities and the GIT compactifications of J. Shah of polarized K3 surfaces of degree 2 and 4. Our results were announced in [11], but their technical nature was one of the reasons that the details got only partially published (in a preprint form in [12] and in H. Sterk’s analysis of the moduli space of Enriques surfaces [16]). We believe that the situation has now changed.
Until our recent work with Gert Heckman [7] we had not realized that the constructions also work for ball quotients and that they form an attractive class to treat before embarking on the more involved case of type IV domain quotients.
It also turned out that by doing this case first helped us in finding a natural setting for the construction (in particular, the notion 1.2 of a linearization of an arrangement thus presented itself) which makes its relative simplicity more visible.
This was for us an important stimulus to return to these questions.
In part II we shall develop the story for type IV domains.

I thank Gert Heckman for his many useful comments on the first version of this paper.

# 1. Arrangements and their linearizations

We begin with a definition.

Definition 1.1. Let $X$ be a connected complex-analytic manifold and $\mathcal { H }$ a collection of smooth connected hypersurfaces of $X$ . We say that $( X , { \mathcal { H } } )$ is an arrangement if each point of $X$ admits a coordinate neighborhood such that every $H \in \mathcal { H }$ meeting that neighborhood is given by a linear equation.
In particular, the collection $\mathcal { H }$ is locally finite.

Fix an arrangement $( X , { \mathcal { H } } )$ . Suppose we are given a line bundle $\mathcal { L }$ on $X$ and for every $H \in \mathcal { H }$ an isomorphism $\mathcal { L } ( H ) \otimes \mathcal { O } _ { H } \cong \mathcal { O } _ { H }$ , or equivalently, an isomorphism between the normal bundle $\nu _ { H / X }$ and the coherent restriction of $\mathcal { L } ^ { \ast }$ to $H$ . We shall want these isomorphisms to satisfy a normal triviality condition which roughly says that if $L$ is any connected component of an intersection of members of $\mathcal { H }$ , then these isomorphisms trivialize the projectivized normal bundle of $L$ . To be precise, if $\mathcal { H } ^ { L }$ denotes the collection of $H \in { \mathcal { H } }$ that contain $L$ , then the normal bundle $\nu _ { L / X }$ is naturally realized as a subbundle of $\mathcal { L } ^ { \ast } \otimes \mathcal { O } _ { L } ^ { \mathcal { H } ^ { L } }$ by means of the homomorphism

$$
\nu _ { L / X } \to \oplus _ { H \in \mathcal { H } ^ { L } } \nu _ { H / X } \otimes \mathcal { O } _ { L } \cong \mathcal { L } ^ { * } \otimes \mathcal { O } _ { L } \otimes _ { \mathbb { C } } \mathbb { C } ^ { \mathcal { H } ^ { L } } .
$$

The condition alluded to is given in the following

Definition 1.2. A linearization of an arrangement $( X , { \mathcal { H } } )$ consists of the data of a line bundle $\mathcal { L }$ on $X$ and for every $H \in { \mathcal { H } }$ an isomorphism ${ \mathcal { L } } ( H ) \otimes { \mathcal { O } } _ { H } \cong { \mathcal { O } } _ { H }$ such that the image of the above embedding $\nu _ { L / X } \to \mathcal { L } ^ { * } \otimes \mathcal { O } _ { L } \otimes _ { \mathbb { C } } \mathbb { C } ^ { \mathcal { H } ^ { L } }$ is given by a linear subspace $N ( L , X )$ of $\mathbb { C } ^ { \mathcal { H } ^ { L } }$ . (Here $L$ is any connected component of an intersection of members of $\mathcal { H }$ .) We then refer to $N ( L , X )$ as the normal space of $L$ in $X$ and to its projectivization $\mathbb { P } ( L , X ) : = \mathbb { P } ( N ( L , X ) )$ as the projectively normal space of $L$ in $X$ .

The condition imposed over $L$ is empty when $L$ has codimension one and is automatically satisfied when each $H$ is compact: if $I \subset \mathcal { H } ^ { L }$ consists of $\operatorname { c o d i m } L$ elements such that $L$ is a connected component of $\cap _ { H \in I } H$ , then $\nu _ { L / X }$ projects isomorphically on the subsum of $\mathcal { L } ^ { \ast } \otimes \mathbb { C } ^ { \mathcal { H } ^ { L } }$ defined by $I$ and hence is given $\nu _ { L / X }$ by a matrix all of whose entries are nowhere zero sections of $\mathcal { O } _ { L }$ . So these entries are constant.

Here are some examples.

Example 1.3 (Affine arrangements).
The most basic example is when $X$ is a complex affine space, $\mathcal { H }$ a locally finite collection of affine-linear hyperplanes and ${ \mathcal { L } } = { \mathcal { O } } _ { X }$ . If the collection is finite, then by including the hyperplane at infinity, this becomes a special case of:

Example 1.4 (Projective arrangements).
Here $X$ is a projective space $\mathbb { P } ( W )$ , $\mathcal { H }$ is a finite collection of projective hyperplanes and $\mathcal { L } = \mathcal { O } _ { \mathbb { P } ^ { n } } ( - 1 )$ .

Example 1.5 (Toric arrangements).
Now $X$ is a principal homogeneous space of an algebraic torus $T$ , $\mathcal { H }$ is a finite collection of orbits of hypertori of $T$ in $X$ and ${ \mathcal { L } } = { \mathcal { O } } _ { X }$ . From this example we may obtain new ones by extending these data to certain smooth torus embeddings of $X$ . The kernel of the exponential map $\exp : \operatorname { L i e } ( T ) \to T$ is a lattice $\operatorname { L i e } ( T ) ( \mathbb { Z } )$ in $\operatorname { L i e } ( T )$ . So it defines a $\mathbb { Q }$ -structure on $\mathrm { L i e } ( T )$ . We recall that a normal torus embedding $X \subset X _ { \Sigma }$ is given by a finite collection $\Sigma$ of closed rational polyhedral cones in $\mathrm { L i e } ( T ) ( \mathbb { R } ) \}$ with the property that the intersection of any two members is a common facet of these members.
The torus $T$ acts on $X _ { \Sigma }$ and the orbits of this action are naturally indexed by $\Sigma$ : the orbit corresponding to $\sigma \in \Sigma$ is identified with the quotient $T ( \sigma )$ of $T$ by the subtorus whose Lie algebra is the complex span of $\sigma$ . The torus embedding is smooth precisely when each $\sigma$ is spanned by part of a basis of $\operatorname { L i e } ( T ) ( \mathbb { Z } )$ and in that case $\Delta : = X _ { \Sigma } - X$ is a normal crossing divisor.

If we want the closure of $H$ in $X _ { \Sigma }$ to meet $\Delta$ transversally for every $H \in { \mathcal { H } }$ , then we must require that $\Sigma$ is closed under intersections with the real hyperplanes $\operatorname { L i e } ( T _ { H } ) ( \mathbb { R } )$ , where $T _ { H } \subset T$ is the stabilizer of $H$ (a hypertorus).
Then the normal bundle of $\overline { H }$ is isomorphic to $\mathcal { O } ( - \Delta ) { \otimes } \mathcal { O } _ { H _ { \Sigma } }$ (choose a general $T$ -invariant vectorfield on $X _ { \Sigma }$ and restrict to $\overline { H }$ ). So $\mathcal { O } ( \Delta )$ may take the role of $\mathcal { L }$ .

A case of special interest is when $T$ is the adjoint torus of a semisimple algebraic group $G$ and $\mathcal { H }$ is the collection of hyperplanes defined by the roots.
The corresponding hyperplanes in $\operatorname { L i e } ( T ) ( \mathbb { R } )$ are reflection hyperplanes of the associated Weyl group and these decompose the latter into chambers.
Each chamber is spanned by a basis of $\operatorname { L i e } ( T ) ( \mathbb { Z } )$ and so the corresponding decomposition $\Sigma$ defines a smooth torus embedding $T \subset T _ { \Sigma }$ . Any root of $( G , T )$ , regarded as a nontrivial character of $T$ , extends to a morphism $T _ { \Sigma } \to \mathbb { P } ^ { 1 }$ that is smooth over $\mathbb { C } ^ { \times }$ . The fiber over 1 is the closure in $T _ { \Sigma }$ of the kernel of this root and hence is smooth.

Example 1.6 (Abelian arrangements).
Let $X$ be a torsor (i.e., a principal homogeneous space) over an abelian variety, $\mathcal { H }$ a collection of abelian subtorsors of codimension one and ${ \mathcal { L } } = { \mathcal { O } } _ { X }$ .

Example 1.7 (Diagonal arrangements).
Let be given a smooth curve $C$ of genus and a nonempty finite set $N$ . For every two-element subset $I \subset N$ the set of maps $g$\
$N  C$ that are constant on $I$ is a diagonal hypersurface in $C ^ { N }$ and the collection of these is an arrangement.
But if $| N | > 2$ and $C$ is a general complete connected curve of genus $\neq 1$ , then a linearization will not exist: it is straightforward to check that there is no linear combination of the diagonal hypersurfaces and pull-backs of divisors on the factors with the property that its restriction to every diagonal hypersurface is linearly equivalent to its conormal bundle.
(If the genus is one, then the diagonal arrangement is abelian, hence linearizable.)

Example 1.8 (Complex ball arrangements).
Let $W$ be a complex vector space of finite dimension $n + 1$ equipped with a Hermitian form $\psi : W \times W \to \mathbb { C }$ of signature $( 1 , n )$ , $\mathbb { B } \subset \mathbb { P } ( W )$ the open subset defined $\psi ( z , z ) > 0$ and $\mathcal { O } _ { \mathbb { B } } ( - 1 )$ the restriction of the ‘tautological’ bundle $\mathcal { O } _ { \mathbb { P } ( W ) } ( - 1 )$ to $\mathbb { B }$ . Then $\mathbb { B }$ is a complex ball of complex dimension $n$ . It is also the Hermitian symmetric domain of the special unitary group $\mathrm { S U } ( \psi )$ . The group $\mathrm { S U } ( \psi )$ acts on the line bundle $\mathcal { O } _ { \mathbb { B } } ( - 1 )$ and the latter is the natural automorphic line bundle over $\mathbb { B }$ . Every hyperplane $H \subset W$ of hyperbolic signature gives a (nonempty) hyperplane section $\mathbb { B } _ { H } : = \mathbb { P } ( H ) \cap \mathbb { B }$ of $\mathbb { B }$ . The latter is the symmetric domain of the special unitary group $\operatorname { S U } ( H )$ of $H$ . In terms intrinsic to $\mathbb { B }$ : $\mathbb { B } _ { H }$ is a totally geodesic hypersurface of $\mathbb { B }$ and any such hypersurface is of this form.
Notice that the normal bundle of $\mathbb { B } _ { H }$ is naturally isomorphic with $\mathcal { O } _ { \mathbb { B } _ { H } } ( 1 ) \otimes _ { \mathbb { C } } W / H$ . Hence we have an $\operatorname { S U } ( H )$ -equivariant isomorphism

$$
{ \mathcal O } _ { \mathbb { B } } ( - 1 ) ( { \mathbb B } _ { H } ) \otimes { \mathcal O } _ { \mathbb { B } _ { H } } \cong { \mathcal O } _ { \mathbb { B } _ { H } } \otimes _ { \mathbb { C } } W / H \cong { \mathcal O } _ { \mathbb { B } _ { H } } .
$$

Locally finite collections of hyperplane sections of $\mathbb { B }$ arise naturally in an arithmetic setting.
Suppose that $( W , \psi )$ is defined over an imaginary quadratic extension $k$ of $\mathbb { Q }$ , which we think of as a subfield of $\mathbb { C }$ . So we are given a $k$ -vector space $W ( k )$ and an Hermitian form $\psi ( k ) : W ( k ) \times W ( k ) \to k$ such that we get $( W , \psi )$ after extension of scalars.
We recall that a subgroup of $\mathrm { S U } ( \psi ) ( k )$ is said to be arithmetic if it is commensurable with the group of elements in $\mathrm { S U } ( \psi ) ( k )$ that stabilize the ${ \mathcal { O } } _ { k }$ -submodule spanned by a basis of $W ( k )$ (where ${ \mathcal { O } } _ { k }$ denotes the ring of integers of $k$ ). It is known that an arithmetic subgroup of $\mathrm { S U } ( \psi ) ( k )$ acts properly discontinuously on $\mathbb { B }$ . Let us say that a collection $\mathcal { H }$ of hyperbolic hyperplanes of $W$ is arithmetically defined if $\mathcal { H }$ , regarded as a subset of $\mathbb { P } ( W ^ { * } )$ , is a finite union of orbits of an arithmetic subgroup of $\mathrm { S U } ( \psi ) ( k )$ and has each point defined over $k$ . In that case the corresponding collection of hyperplane sections $\mathcal { H } | \mathbb { B }$ of $\mathbb { B }$ is locally finite (this known fact is part of Lemma 5.4 below).

Example 1.9 (Type IV arrangements).
Let $V$ be a complex vector space of dimension $n + 2$ equipped with a nondegenerate symmetric bilinear form $\phi : V \times V $ $\mathbb { C }$ . Assume that $( V , \phi )$ is defined over $\mathbb { R }$ in such a way that $\phi$ has signature $( 2 , n )$ . Let $\mathbb { D } \subset \mathbb { P } ( V )$ be a connected component of the subset defined $\phi ( z , z ) = 0$ and $\phi ( z , \bar { z } ) > 0$ . We let $\mathcal { O } _ { \mathbb { D } } ( - 1 )$ be the restriction of ${ \mathcal { O } } _ { \mathbb { P } ( V ) }$ to $\mathbb { D }$ as in the previous example.
Then $\mathbb { D }$ is a the Hermitian symmetric domain of the $\operatorname { S L } ( \phi ) ( { \mathbb { R } } )$ -stabilizer of $\mathbb { D }$ . The group $G ( V )$ also acts on the line bundle $\mathcal { O } _ { \mathbb { D } } ( - 1 )$ and the latter is the natural automorphic line bundle over $X$ . Every hyperplane $H \subset V$ defined over $\mathbb { R }$ of signature $( 2 , n - 1 )$ gives a (nonempty) hyperplane section $\mathbb { D } _ { H } : = \mathbb { P } ( H _ { \mathbb { C } } ) \cap \mathbb { D }$ of $\mathbb { D }$ . This is a symmetric domain for the group its $\operatorname { S L } ( \phi ) ( { \mathbb { R } } )$ -stabilizer.
As in the previous example, it is a totally geodesic hypersurface of $\mathbb { D }$ , any such hypersurface is of this form, and we have an equivariant isomorphism $\mathcal { O } _ { \mathbb { H } } ( - 1 ) ( \mathbb { D } _ { H } ) \cong \mathcal { O } _ { \mathbb { D } _ { H } }$ . Any collection of totally geodesic hypersurfaces of $X$ that is arithmetically defined in the sense of the example above (with the number field $k$ replaced by $\mathbb { Q }$ ) is locally finite on $\mathbb { D }$ .

A ball naturally embeds in a type IV domain: if $( W , \psi )$ is as in the ball example, then $V : = W \oplus { \overline { { W } } }$ has signature $( 2 , 2 n )$ . A real structure is given by stipulating that the interchange map is complex conjugation and this yields a nondegenerate symmetric bilinear form $\phi$ defined over $\mathbb { R }$ . For an appropriate choice of component $\mathbb { D }$ , we thus get an embedding $\Downarrow \subset \ U$ . If $( W , \psi )$ is defined over an imaginary quadratic field, then $( W \oplus { \overline { { W } } } , \phi )$ is defined over $\mathbb { Q }$ and an arithmetic arrangement on $\mathbb { D }$ restricts to one on $\mathbb { B }$ .

# 2. Blowing up arrangements

2.1. Blowing up a fractional ideal.
In this subsection we briefly recall the basic notion of blowing up a fractional ideal.
Our chief references are [6] and [5].

Suppose $X$ is a variety and ${ \mathcal { T } } \subset { \mathcal { O } } _ { X }$ is a coherent ideal.
Then $\mathbb { \oplus } _ { k = 0 } ^ { \infty } \mathcal { T } ^ { k }$ is a $\mathcal { O } _ { X }$ - algebra that is generated as such by its degree one summand (it should be clear that $\mathcal { T } ^ { 0 } : = \mathcal { O } _ { X }$ ). Its proj is a projective scheme over $X$ , $\pi : \tilde { X } \to X$ , called the blowup of $\mathcal { L }$ , with the property that $\pi ^ { * } \mathcal { L } _ { X }$ is invertible and relatively very ample.

If $X$ is normal and $\mathcal { L }$ defines a reduced subscheme of $X$ , then its blowup is normal also.
The variety underlying $\ddot { X }$ is over $X$ locally given as follows: if $\mathcal { L }$ is generated over an open subset $U \subset X$ by $f _ { 0 } , \dots , f _ { r } \in \mathbb { C } [ U ]$ , then these generators determine a rational map $[ f _ { 0 } : \cdot \cdot \cdot : f _ { r } ] : U \to \mathbb { P } ^ { r }$ and the closure of the graph of this map in $U \times \mathbb { P } ^ { r }$ with its projection onto $U$ can be identified with $( \tilde { X } _ { U } ) _ { \mathrm { r e d } } \to U$ . This construction only depends on $\mathcal { L }$ as a $\mathcal { O } _ { X }$ -module.
So if $\mathcal { L }$ is an invertible sheaf on $X$ , and $\mathcal { L }$ is a nowhere zero coherent subsheaf of $\mathcal { L }$ , then we still have defined the blowup of $\mathcal { L }$ as the proj of $\oplus _ { k = 0 } ^ { \infty } \mathcal { T } ^ { ( k ) } \subset \oplus _ { k = 0 } ^ { \infty } \mathcal { L } ^ { \otimes k }$ , where $\mathcal { T } ^ { ( k ) }$ denotes the $k$ th power of $\mathcal { L }$ : the image of $\mathcal { T } ^ { \otimes k }$ in $\mathcal { L } ^ { \otimes k }$ . In fact, for the definition it suffices that $\mathcal { L }$ is a nowhere zero coherent subsheaf of the sheaf of rational sections of $\mathcal { L }$ .

The coherent pull-back of $\mathcal { L }$ along $\tilde { X }  X$ is invertible and the latter morphism is universal for that property: any morphism from a scheme to $X$ for which coherent pull-back of $\mathcal { L }$ is invertible factorizes over $\ddot { X }$ . In particular, if $Y \subset X$ is a closed subvariety, then the blowup $\tilde { X }  X$ of the ideal defining $Y$ is an isomorphism when $Y$ is a Cartier divisor.
If $Y$ is the support of an effective Cartier divisor, then ${ \ddot { X } }  X$ is still finite, but if $Y$ is only a hypersurface, then some fibers of ${ \ddot { X } }  X$ may have positive dimension.

Here is a simple example that has some relevance to what will follow.
The fractional ideal in the quotient field of $\mathbb { C } [ z _ { 1 } , z _ { 2 } ]$ generated by $z _ { 1 } ^ { - 1 } z _ { 2 } ^ { - 1 }$ is uninteresting as it defines the trivial blowup of $\mathbb { C } ^ { 2 }$ . But the blowup of the ideal generated by $z _ { 1 } ^ { - 1 }$ and $z _ { 2 } ^ { - 1 }$ amounts to the usual blowup of the origin in $\mathbb { C } ^ { 2 }$ .

2.2. The arrangement blowup.
Let $( X , { \mathcal { H } } )$ be an arrangement.
There is a simple and straightforward way to find a modification $X _ { \mathcal { H } }  X$ of $X$ such that the preimage of $D$ is a normal crossing divisor: first blow up the union of the dimension $0$ intersections of members of the $\mathcal { H }$ , then then the strict transform of the dimension 1 intersections of members of the $\mathcal { H }$ , and so on, finishing with blowing up the strict transform of the dimension $n - 2$ intersections of members of the $\mathcal { H }$ :

$$
X = X ^ { 0 }  X ^ { 1 }  \cdot \cdot  X ^ { n - 2 } = \tilde { X } ^ { \mathcal { H } } .
$$

We refer to $\tilde { X } ^ { \mathcal { H } }$ as the blow-up of $X$ defined by the arrangement $\mathcal { H }$ or briefly, as the $\mathcal { H }$ -blow-up of $X$ . To understand the full picture, it is perhaps best to do one blow-up at a time.
In what follows we assume that we are also given a linearization $\mathcal { L }$ of the arrangement $( X , { \mathcal { H } } )$ . We begin with a basic lemma.

Let us denote by $\mathrm { P O } ( \mathcal { H } )$ the partially ordered set of connected components of intersections of members of $\mathcal { H }$ which have positive codimension.
For $L \in \mathrm { P O } ( \mathcal { H } )$ , we denote by $\mathcal { H } ^ { L }$ the collection of $H \in { \mathcal { H } }$ containing $L$ as a lower dimensional subvariety (so this collection is empty when $\mathrm { c o d i m } ( L ) = 1$ ). The following lemma is clear.

Lemma 2.1. Given $L \in \operatorname { P O } ( \mathcal { H } )$ , then the members of $\mathcal { H } ^ { L }$ define a linear arrangement in $N ( L , X )$ . If $L ^ { \prime } \in \operatorname { P O } ( \mathcal { H } )$ contains $L$ , then we have a natural exact sequence of vector spaces

$$
0 \to N ( L , L ^ { \prime } ) \to N ( L , X ) \to N ( L ^ { \prime } , X ) \to 0 .
$$

If $\mathcal { L }$ is an invertible sheaf on $X$ , then we shall write $\mathcal { L } ( \mathcal { H } )$ for the subsheaf $\textstyle \sum _ { H \in { \mathcal { H } } } { \mathcal { L } } ( H )$ of the sheaf of rational sections of $\mathcal { L }$ . This sheaf is a coherent $\mathcal { O } _ { X }$ - module, but need not be invertible.
In particular, it should not be confused with the invertible sheaf ${ \mathcal { L } } ( \sum _ { H \in { \mathcal { H } } } H )$ . The $k$ th power of $\mathcal { L } ( \mathcal { H } )$ ‘as a fractional ideal’ is

$$
\mathcal { L } ( \mathcal { H } ) ^ { ( k ) } : = \sum _ { ( H _ { 1 } , \ldots , H _ { k } ) \in \mathcal { H } ^ { k } } \mathcal { L } ^ { \otimes k } ( H _ { 1 } + \cdot \cdot \cdot + H _ { k } )
$$

and so its blowup is the proj of $\oplus _ { k = 0 } ^ { \infty } { \mathcal { L } } ( \mathcal { H } ) ^ { ( k ) }$ .

Let $L \subset X$ be a minimal member of $\operatorname { P O } ( \mathcal { H } )$ and of codimension $\geq 2$ and let $\pi : { \ddot { X } } \to X$ blow up $L$ . The exceptional divisor $E : = \pi ^ { - 1 } L$ is then the projectivized normal bundle $\mathbb { P } \big ( \nu _ { L / X } \big )$ of $L$ . In case a linearization exists, the previous lemma identifies this exceptional divisor with $L \times \mathbb { P } ( L , X )$ in such a manner that the strict transform $\tilde { H }$ of $H \in \mathcal { H } ^ { L }$ meets it in $L \times \mathbb { P } ( L , H )$ .

Lemma 2.2. Suppose that the arrangement $( X , { \mathcal { H } } )$ is linearized by the invertible sheaf $\mathcal { L }$ . Then the strict transform of $\mathcal { H }$ in $\tilde { X }$ is an arrangement that is naturally linearized by ${ \bar { \mathcal { L } } } : = \pi ^ { * } { \mathcal { L } } ( E )$ . Precisely, if ⊠ stands for the exterior coherent tensor product, then

(i) $\nu _ { E / \tilde { X } } = ( \mathcal { L } ^ { \ast } \otimes \mathcal { O } _ { L } ) \boxtimes \mathcal { O } _ { \mathbb { P } ( L , X ) } ( - 1 )$ ,\
(ii) $\begin{array} { r } { \pi ^ { * } \mathcal { L } ( \mathcal { H } ) \otimes \mathcal { O } _ { E } = ( \mathcal { L } ^ { * } \otimes \mathcal { O } _ { L } ) \boxtimes ( \sum _ { H \in \mathcal { H } ^ { L } } \mathcal { O } _ { \mathbb { P } ( L , X ) } ( - 1 ) ( \mathbb { P } ( L , H ) ) \ \mathrm { ~ , ~ } } \end{array}$ and (iii) for every $H \in \mathcal { H } ^ { L }$ we have $\tilde { \mathcal { L } } ( \tilde { H } ) \otimes \mathcal { O } _ { \tilde { H } } \cong \mathcal { O } _ { \tilde { H } }$ .

Proof.
Assertion (i) is an immediate consequence of Lemma 2.1. If $H \in \mathcal { H } ^ { L }$ , then the coherent restriction of $\tilde { \mathcal { L } } ( \tilde { H } ) = ( \pi ^ { * } \mathcal { L } ) ( E + \tilde { H } ) = \pi ^ { * } ( \mathcal { L } ( H ) )$ to the preimage of $H$ is trivial.
Hence the same is true for its coherent restriction to $E$ or $\tilde { H }$ , which proves assertion (ii).
It is clear that $\mathcal { O } _ { \tilde { X } } ( \tilde { H } ) \otimes \mathcal { O } _ { E } = \mathcal { O } _ { L } \boxtimes \mathcal { O } _ { \mathbb { P } ( L , X ) } ( \mathbb { P } ( L , H ) )$ . Now (iii) follows also:

$$
\begin{array} { r l } { \pi ^ { * } \mathcal { L } ( \mathcal { H } ) \otimes \mathcal { O } _ { E } = ( \pi ^ { * } \mathcal { L } ) \big ( \displaystyle \sum _ { H \in \mathcal { H } ^ { L } } \mathcal { O } _ { E } ( E + \tilde { H } ) \big ) } & { } \\ { = \pi ^ { * } \mathcal { L } \otimes \nu _ { E / \tilde { X } } \big ( \displaystyle \sum _ { H \in \mathcal { H } ^ { L } } \mathcal { O } _ { E } ( E \cap \tilde { H } ) } & { } \\ { = ( \mathcal { L } ^ { * } \otimes \mathcal { O } _ { L } ) \boxtimes \big ( \displaystyle \sum _ { H \in \mathcal { H } ^ { L } } \mathcal { O } _ { \mathbb { P } ( L , X ) } ( - 1 ) ( \mathbb { P } ( L , H ) ) . } & { } \end{array}
$$

Hence $( \tilde { X } , \{ \tilde { H } \} _ { H \in \mathcal { H } } , \tilde { \mathcal { L } } )$ satisfies the same hypotheses as $( X , \{ H \} _ { H \in \mathcal { H } } , \mathcal { L } )$ . Our gain is that we have eliminated an intersection component of $\mathcal { H }$ of minimal dimension.
We continue in this manner, until the strict transforms of the members of $\mathcal { H }$ are disjoint and end up with ${ \tilde { X } } ^ { \mathcal { H } }  X$ .

Convention 2.3. If an arrangement $\mathcal { H }$ on a connected complex manifold $X$ is understood, we often omit it from notation that a priori depends on $\mathcal { H }$ . For instance, we may write $\ddot { X }$ for the corresponding blow-up $\ddot { X } ^ { \mathcal { H } }$ of $X$ and $X ^ { \circ }$ for the complementary Zariski open subset (as lying either in $X$ or in $\ddot { X }$ ).

The members of $\mathcal { H } - \mathcal { H } ^ { L }$ that meet $L$ define an arrangement $\mathcal { H } _ { L }$ in $L$ . So we have defined $\ddot { L }$ and $L ^ { \circ }$ . It is realized as the strict transform of $L$ under the blowups of members of $\mathrm { P O } ( \mathcal { H } )$ smaller than $L$ . Lemma 2.2 shows that the projectivized normal bundle of $\tilde { L }$ in $X$ can be identified with the trivial bundle $\tilde { L } \times \mathbb { P } ( L , X )$ such that the members of $\mathcal { H } ^ { L }$ determine a projective arrangement in $\mathbb { P } ( L , X )$ . So we have defined $\tilde { \mathbb { P } } ( L , X )$ and $\mathbb { P } ( L , X ) ^ { \circ }$ . The preimage of $\tilde { L }$ in $\tilde { X }$ is a smooth divisor that can be identified with

$$
E ( L ) : = \tilde { L } \times \tilde { \mathbb { P } } ( L , X ) .
$$

It contains

$$
E ( L ) ^ { \circ } : = L ^ { \circ } \times \mathbb { P } ( L , X ) ^ { \circ } .
$$

as an open-dense subset.

Lemma 2.2 yields with induction:

Lemma 2.4. Under the assumtions of Lemma 2.2 we have:

(i) The morphism $\pi : { \ddot { X } } \to X$ is obtained by blowing up the fractional ideal sheaf $\mathcal { O } ( \mathcal { H } )$ ,\
(ii) for every $L \in \mathrm { P O } ( \mathcal { H } )$ , the coherent pull-back of $\mathcal { L } ( \mathcal { H } )$ to $E ( L )$ is identified with the coherent pull-back of the sheaf $\mathcal { O } _ { \mathbb { P } ( L , X ) } ( - 1 ) ( \mathcal { H } ^ { L } )$ on $\mathbb { P } ( L , X )$ under the projection $E ( L ) \to \varmathbb { P } ( L , X ) \to \mathbb { P } ( L , X )$ and\
(iii) the coherent pull-back of $\mathcal { L } ( \mathcal { H } )$ to $\tilde { L }$ is identified with the coherent pull-back of $\mathcal { L } ( \mathcal { H } _ { L } )$ to $\tilde { L }$ (a line bundle by (i)) tensorized over $\mathbb { C }$ with the vector space $H ^ { 0 } ( \mathcal { O } _ { \mathbb { P } ( L , X ) } ( - 1 ) ( \mathcal { H } ^ { L } ) )$ .

Lemma 2.5. If $L$ and $L ^ { \prime }$ are distinct members of $\mathrm { P O } ( \mathcal { H } )$ , then $E ( L )$ and $E ( L ^ { \prime } )$ do not intersect unless $L$ and $L ^ { \prime }$ are incident.
If they are, and $L \subset L ^ { \prime }$ , say, then

$$
E ( L ) \cap E ( L ^ { \prime } ) = \tilde { L } \times \tilde { \mathbb { P } } ( L , L ^ { \prime } ) \times \tilde { \mathbb { P } } ( L ^ { \prime } , X ) .
$$

Proof.
The first assertion is clear.
The strict transform of $L$ in the blowing ups of members of $\mathrm { P O } ( \mathcal { H } )$ contained in $L$ is $\tilde { L } \times \mathbb { P } ( L , X )$ . The strict transform of $L ^ { \prime }$ meets the latter in $\tilde { L } \times \mathbb { P } ( L , L ^ { \prime } )$ . Then $E ( L ) \cap E ( L ^ { \prime } )$ must be the closure of the preimage of $\tilde { L } \times \mathbb { P } ( L , L ^ { \prime } ) ^ { \circ }$ in $\ddot { X }$ . If we next blow up the members of $\mathrm { P O } ( \mathcal { H } )$ strictly between $L$ and $L ^ { \prime }$ , the strict transform of $\tilde { L } \times \mathbb { P } ( L , L ^ { \prime } )$ is $\tilde { L } \times \tilde { \mathbb { P } } ( L , L ^ { \prime } )$ . Blowing up $L ^ { \prime }$ yields $\tilde { L } \times \tilde { \mathbb { P } } ( L , L ^ { \prime } ) \times \mathbb { P } ( L ^ { \prime } , X )$ , Finally, blowing up the members of $\mathrm { P O } ( \mathcal { H } )$ strictly containing $L ^ { \prime }$ gives $\ddot { L } \times \ddot { \mathbb { P } } ( L , L ^ { \prime } ) \times \ddot { \mathbb { P } } ( L ^ { \prime } , X )$ . The lemma now follows easily.
□

This generalizes in a straightforward manner as follows:

Lemma 2.6. Let $L _ { 0 } , L _ { 1 } , \ldots , L _ { r }$ be distinct members of $\mathrm { P O } ( \mathcal { H } )$ , ordered by dimension: $\dim ( L _ { 0 } ) \leq \dim ( L _ { 1 } ) \leq \cdots \leq \dim ( L _ { r } )$ . Then $\cap _ { i } E ( L _ { i } )$ is nonempty if and only if these members make up a flag $L _ { \bullet } = ( L _ { 0 } \subset L _ { 1 } \subset \cdots \subset L _ { r }$ ) and in that case the intersection in question equals

$$
E ( L _ { \bullet } ) : = \tilde { L } _ { 0 } \times \tilde { \mathbb { P } } ( L _ { 0 } , L _ { 1 } ) \times \cdots \times \tilde { \mathbb { P } } ( L _ { r - 1 } , L _ { r } ) \times \tilde { \mathbb { P } } ( L _ { r } , X ) .
$$

Moreover, its open-dense subset

$$
E ( L _ { \bullet } ) ^ { \circ } : = L _ { 0 } ^ { \circ } \times \mathbb { P } ( L _ { 0 } , L _ { 1 } ) ^ { \circ } \times \cdots \times \mathbb { P } ( L _ { r - 1 } , L _ { r } ) ^ { \circ } \times \mathbb { P } ( L _ { r } , X ) ^ { \circ }
$$

is a minimal member of the Boolean algebra of subsets of $X _ { \mathcal { H } }$ generated by the divisors $E ( L )$ . These elements define a stratification of $\ddot { X } - X ^ { \circ }$ .

2.3. Minimal (Fulton-MacPherson) blowup of an arrangement.
The simple blowing-up procedure described above turns the arrangement into a normal crossing divisor, but it is clearly not minimal with respect that property.
If $V$ is a vector space and $( W _ { i } \subset V ) _ { i }$ is a collection subspaces that is linearly independent in the sense that $V \to \oplus _ { i } V / W _ { i }$ is surjective, then the blowup of $\cup _ { i } W _ { i }$ defines a morphism $\tilde { V }  V$ for which the total transform of $\cup _ { i } W _ { i }$ is a normal crossing divisor: the strict transform ${ \ddot { W } } _ { i }$ of $W _ { i }$ is a smooth divisor and these divisors meet transversally, their common intersection being fibered over $\cap _ { i } W _ { i }$ with fiber $\Pi _ { i } \mathbb { P } ( V / W _ { i } )$ . It is also obtained by blowing up the strict transforms of the $W _ { i }$ ’s in any order.
So in case of an arrangement we can omit the blowups along $L \in \operatorname { P O } ( \mathcal { H } )$ with the property that the minimal elements of $\mathcal { H } ^ { L }$ are independent along $L$ in the above sense.
Since we still end up with a normal crossing situation, we call this the minimal normal crossing resolution of the arrangement.
It is not hard to specify a fractional ideal on $X$ whose blowup yields this minimal normal crossing resolution.
These and similar blowups have been introduced and studied by Yi Hu [8] who built on earlier work of A. Ulyanov [17].

A case that is perhaps familiar is the diagonal arrangement of Example 1.7: we get the Fulton-MacPherson compactification of the space of injective maps from a given finite nonempty set to a given smooth curve $C$ . (We may subsequently pass to the orbit space relative to the action automorphism group of $C$ if that group acts properly.)

# 3. Contraction of blown-up arrangements

Throughout the rest of this paper, $( X , { \mathcal { H } } , { \mathcal { L } } )$ stands for a linearized arrangement.

According to Lemma 2.4 the pull-back $\pi ^ { * } { \mathcal { L } } ( { \mathcal { H } } )$ on $\ddot { X }$ is invertible.
Suppose for a moment that $X$ is compact and $\mathcal { L } ( \mathcal { H } )$ is generated by its sections.
Then so are $\ddot { X }$ and $\pi ^ { * } { \mathcal { L } } ( { \mathcal { H } } )$ and hence the latter defines a morphism from $\tilde { X }$ to a projective space.
By Lemma 2.4 again, this morphism will be constant on the fibers of the projections $E ( L ) \to { \bar { \mathbb { P } } } ( L , X )$ . In other words, if $R$ is the equivalence relation on $\ddot { X }$ generated by these projections, then the morphism will factorize through the quotient space ${ \tilde { X } } / R$ . Our goal is to find conditions under which $\pi ^ { * } { \mathcal { L } } ( { \mathcal { H } } )$ is semiample, more precisely, conditions under which this quotient space is projective and $\pi ^ { * } { \mathcal { L } } ( { \mathcal { H } } )$ is the coherent pull-back of an ample line bundle on ${ \tilde { X } } / R$ .

Let us first focus on $R$ as an equivalence relation.
We begin with noting that on a stratum $E ( L _ { 0 } \subset \cdots \subset L _ { r } ) ^ { \circ }$ the equivalence relation is defined by the projection on the last factor $\mathbb { P } ( L _ { r } , X ) ^ { \circ }$ . So the quotient $\tilde { X } / R$ is as a set the disjoint union of $X ^ { \circ }$ and the projective arrangement complements $\mathbb { P } ( L , X ) ^ { \circ }$ , $L \in \operatorname { P O } ( \mathcal { H } )$ .

Lemma 3.1. The equivalence relation $R$ , when viewed as a subset of $\ddot { X } \times \ddot { X }$ , is equal to the union of the diagonal and the $E ( L ) \times _ { \tilde { \mathbb { P } } ( L , X ) } E ( L )$ . In particular, $R$ is closed and hence $\ddot { X } / R$ is Hausdorff.

Proof.
By definition $R$ contains the union in the statement.
The opposite inclusion also holds: $x \in E ( L _ { 0 } \subset \cdots \subset L _ { r } ) ^ { \circ }$ and $x ^ { \prime } \in E ( L _ { 0 } ^ { \prime } \subset \cdots \subset L _ { s } ^ { \prime } ) ^ { \circ }$ are related if and only if $L _ { r } = L _ { s } ^ { \prime }$ and both have the same image in $\mathbb { P } ( L _ { r } , X ) ^ { \circ }$ . □

Theorem 3.2. Suppose $X$ compact and that some positive power of $\mathcal { L } ( \mathcal { H } )$ is generated by its sections and that these sections separate the points of $X ^ { \circ }$ . Then the pull-back of $\mathcal { L } ( \mathcal { H } )$ to $\ddot { X }$ is a semi-ample invertible sheaf and a positive power of this sheaf defines a morphism from $\ddot { X }$ to a projective space whose image $\hat { X }$ realizes the quotient space $X / R$ with the strata $X ^ { \circ }$ and $\mathbb { P } ( L , X ) ^ { \circ }$ of $X / R$ realized as subvarieties of $\hat { X }$ .

Proof.
Let $\mathcal { L } ( \mathcal { H } ) ^ { ( k ) }$ be generated by its sections and separate the points of $X ^ { \circ }$ . Then the invertible sheaf $\pi ^ { * } ( { \mathcal { L } } ( \mathcal { H } ) ^ { ( k ) } )$ has the same property.
Let $f : \dot { X } \to \mathbb { P } ^ { N }$ be the morphism defined by a basis of its sections.
A possibly higher power of $\mathcal { L } ( \mathcal { H } )$ will have a normal variety as its image and so it suffices to prove that $f$ separates the points of every stratum of ${ \tilde { X } } / R$ . By hypothesis this is the case for $X ^ { \circ }$ . Given $L \in \mathrm { P O } ( \mathcal { H } )$ of codimension $\geq 2$ , then it follows from Lemma 2.4 that the pull-back of $\mathcal { L } ( \mathcal { H } )$ to $\tilde { L }$ is isomorphic to a line bundle on $\tilde { L }$ tensorized over $\mathbb { C }$ with $H ^ { 0 } ( \mathcal { O } _ { \mathbb { P } ( L , X ) } ( - 1 ) ( \mathcal { H } ^ { L } ) )$ . Any set of generating sections of $\mathcal { L } ( \mathcal { H } )$ must therefore determine a set of generators of the vector space $H ^ { 0 } ( \mathcal { O } _ { \mathbb { P } ( L , X ) } ( - 1 ) ( \mathcal { H } ^ { L } ) )$ . Such a generating set separates the points of $\mathbb { P } ( L , X ) ^ { \circ }$ . The same is true for a set of generating sections of a power of $\mathcal { L } ( \mathcal { H } )$ . So for some positive $k$ , $\mathcal { L } ( \mathcal { H } ) ^ { ( k ) }$ separates the points of every stratum of $\ddot { X } / R$ . □

This theorem applies to some of the examples mentioned at the beginning.

3.1. Projective arrangements.
The hypotheses of Theorem 3.2 are satisfied if the collection $\mathcal { H }$ of hyperplanes has no point in common: if $f _ { H } \in V ^ { * }$ is a defining equation for $H \subset \mathbb { P } ( V )$ , then $\mathcal { O } _ { \mathbb { P } ( V ) } ( - 1 ) ( \mathcal { H } )$ is generated by the sections $\{ f _ { H } ^ { - 1 } \} _ { H \in \mathcal { H } }$ . There is no need to pass to a higher power of this sheaf: the variety ${ \hat { \mathbb { P } } } ( V )$ appears as the image of the rational map $\mathbb { P } ( V ) \to \mathbb { P } ( \mathbb { C } ^ { \mathcal { H } } )$ with coordinates $( f _ { H } ^ { - 1 } ) _ { H \in \mathcal { H } }$ . If $V = \mathbb { C } ^ { n + 1 }$ and $\mathcal { H }$ is the set of coordinate hyperplanes, then $\hat { \mathbb P } ^ { n } = \mathbb P ^ { n }$ and this map is just the standard Cremona transformation in dimension $n$ .

Of particular interest are the cases when $\mathcal { H }$ is the set of reflection hyperplanes of a finite complex reflection group $G$ with $V ^ { G } = \{ 0 \}$ . Then ${ \hat { \mathbb { P } } } ( V )$ has a $G$ -action so that we can form the orbit space $G \backslash { \hat { \mathbb { P } } } ( V )$ . (A theorem of Chevalley implies that $G \backslash \mathbb { P } ( V )$ is rational, hence so is this completion.)

3.2. Toric arrangements defined by root systems.
Let $T$ be the adjoint torus of a semisimple algebraic group.
It comes with an action of the Weyl group $W$ . The collection of reflection hyperplanes of $W$ in $\operatorname { L i e } ( T ) ( \mathbb { R } )$ defines a torus embedding $T \subset T _ { \Sigma }$ . The roots define a collection of ‘hypertorus embeddings’ $\mathcal { H }$ in $T _ { \Sigma }$ . We may also state this as follows: the set $R$ of roots define an embedding $T \to ( \mathbb { C } ^ { \times } ) ^ { R }$ , $T _ { \Sigma }$ is the closure of its image in $( \mathbb { P } ^ { 1 } ) ^ { R }$ and $H _ { \alpha }$ is the fiber over $[ 1 : 1 ]$ of the projection of $T _ { \Sigma } \to \mathbb { P } _ { \alpha } ^ { 1 }$ on the factor indexed by $\alpha$ . A $T$ -orbit $T ( \sigma )$ in $T \subset T _ { \Sigma }$ is also an adjoint torus (associated to a parabolic subgroup), its closure in $T _ { \Sigma }$ is the associated torus embedding (hence smooth) and the roots of $T$ restrict to roots of $T ( \sigma )$ and vice versa.
Denote by $\mathrm { I I }$ the collection of indivisible elements of $\operatorname { L i e } ( T ) ( \mathbb { Z } )$ that generate a (one dimensional) face of $\Sigma$ (these are just the coweights that are fundamental relative a chamber).
The closure $D ( \varpi )$ of $T ( \mathbb { R } _ { > 0 } \varpi )$ in $T _ { \Sigma }$ is a (smooth) $T$ -invariant divisor and all such are so obtained.
The meromorphic functions $\{ f _ { \alpha } : = ( e ^ { \alpha } - 1 ) ^ { - 1 } \} _ { \alpha \in R }$ separate the points of $T ^ { \circ }$ . They also separate the $T$ -orbits from each other: The divisor of $f _ { \alpha }$ is

$$
- H _ { \alpha } + \sum _ { \sigma \in \Sigma _ { 1 } } \alpha ( \varpi ) D ( \varpi ) .
$$

Two distinct members of $\mathrm { I I }$ can be distinguished by a root and so the corresponding $T$ -orbits are separated by the corresponding meromorphic function.
Given a $\varpi \in \mathrm { I I }$ , then each $f _ { \alpha }$ with $\alpha ( \varpi ) = 0$ restricts to a meromorphic function on $D ( \varpi )$ of the same type.
For that reason these meromorphic functions also separate the points of any stratum $T ( \sigma ) ^ { \circ }$ .

So $\widehat { T _ { \Sigma } }$ exists as a projective variety.
It comes with an action of the Weyl group $W$ of the root system.
Notice that the subvariety of $\widehat { T _ { \Sigma } }$ over the identity element of $T$ is the modification $\hat { \mathbb { P } } ( \mathrm { L i e } ( T ) )$ of the projectivized tangent space $\mathbb { P } ( \mathrm { L i e } ( T ) )$ defined by the arrangement of tangent spaces of root kernels.

Example 3.3 (The universal cubic surface).
Suppose $( T , W )$ is an adjoint torus of type $E _ { 6 }$ . Then the construction of [10] (see also [13]) shows that $( \{ \pm 1 \} \cdot W ) \widehat { T _ { \Sigma } }$ may be regarded as a compactification of the universal smooth cubic surface.
Let us briefly recall the construction.
If $S \subset \mathbb { P } ^ { 3 }$ is a cubic surface, then for a general $p \in S$ , the projective tangent space of $S$ at $p$ meets $S$ in a nodal cubic $C _ { p }$ . The latter is also an anticanonical curve.
The identity component $\mathrm { P i c } _ { o } ( C _ { p } )$ of the Picard group of $C _ { p }$ is a copy of $\mathbb { C } ^ { \times }$ . The preimage $\operatorname { P i c } _ { o } ( S )$ of ${ \mathrm { P i c } } _ { o } ( C _ { p } )$ in $\mathrm { P i c } ( S )$ is a root lattice of type $E _ { 6 }$ and so $\operatorname { H o m } ( \operatorname { P i c } _ { o } ( S ) , \operatorname { P i c } _ { o } ( C _ { p } ) )$ is an adjoint $E _ { 6 }$ -torus.
The restriction map defines an element of this torus.
It turns out that it does not lie in any reflection hypertorus.
We proved in [10] that this element is a complete invariant of the pair $( S , p )$ : the $\{ \pm 1 \} \cdot W$ -orbit in $T ^ { \circ }$ defined by the restriction map determines $( S , p )$ up to isomorphism.
All orbits in $T ^ { \circ }$ so arise and so $( \{ \pm 1 \} \cdot W ) \backslash T ^ { \circ }$ is a coarse moduli space for pairs $( S , p )$ as above.

If we allow $p$ to be an arbitrary point of a smooth cubic, then $C _ { p }$ may degenerate into any reduced cubic curve.
The type of this curve corresponds in fact to $\{ \pm 1 \} \cdot W$ - invariant union of strata of $\widehat { T _ { \Sigma } }$ in a way that $( \{ \pm 1 \} \cdot W ) \backslash T ^ { \circ }$ is going to contain the coarse moduli space of pairs $( S , p )$ with $p$ an arbitrary point of the smooth cubic $S$ . To be precise: if $C _ { p }$ becomes a cuspidal curve (with a cusp at $p$ ), then there is a unique stratum, it is projective of type $E _ { 6 }$ (it is the one defined by the identity element of $T$ : a copy of $\mathbb { P } ( \mathrm { L i e } ( T ) ) ^ { \circ } )$ . If $C _ { p }$ becomes a conic plus a line, then we get the projective or toric strata of type $D _ { 5 }$ , depending on whether or not the line is tangent to the conic.
Finally, if $C _ { p }$ becomes a sum of three distinct lines, then we get projective or toric strata of type $D _ { 4 }$ , depending on whether or not the lines are concurrent.

Example 3.4 (The universal quartic curve).
The story is quite similar to the preceding case (we refer again to [10] and [13]). We now assume that $( T , W )$ is an adjoint torus of type $E _ { 7 }$ . A smooth quartic curve $Q$ in $\mathbb { P } ^ { 2 }$ determines a Del Pezzo surface of degree 2: the double cover $S \to \mathbb { P } ^ { 2 }$ ramified along $Q$ . This sets up a bijective correspondence between isomorphism classes of quartic curves and isomorphism classes of Del Pezzo surface of degree 2. If $p \in Q$ is such that the projective line $T _ { p } Q$ meets $Q$ in two other distinct points, then the preimage $Q _ { p }$ of $T _ { p } Q$ in $S$ is a nodal genus one curve.
Starting with the homomorphism $\operatorname { P i c } ( S ) \to \operatorname { P i c } ( Q _ { p } )$ , we define $\operatorname { P i c } _ { o } ( S )$ as before (it is a root lattice of type $E _ { 7 }$ ) so that we have an adjoint $E _ { 7 }$ -torus $\operatorname { H o m } ( \operatorname { P i c } _ { o } ( S ) , \operatorname { P i c } _ { o } ( Q _ { p } ) )$ . Proceeding as in the previous case we find that $W \backslash T ^ { \circ }$ is a coarse moduli space for pairs $( Q , p )$ as above (now $- 1 \in W$ ) and that allowing $p$ to be arbitrary yields an open-dense embedding of the corresponding coarse moduli space in $W \backslash \widehat { T _ { \Sigma } }$ . The added strata are as follows: allowing $T _ { p } Q$ to become a flex (but not a hyperflex) point yields the projective stratum of type $E _ { 7 }$ over the identity element.
If $T _ { p } Q$ is a bitangent, then we get the toric or projective strata of type $E _ { 6 }$ , depending on whether the bitangent is a hyperflex.
Our compactification of $W \backslash T ^ { \circ }$ has another interesting feature as well.
We have also $A _ { 6 }$ and $A _ { 7 }$ -strata, both of projective type.
These are single orbits and have an interpretation as the coarse moduli space of pairs $( Q , p )$ , where $p$ is a point of a hyperelliptic curve $Q$ of genus 3: we are on a $A _ { 6 }$ or $A _ { 7 }$ -stratum depending on whether or not $p$ is a Weierstrass point.
So $W \backslash \widehat { T _ { \Sigma } }$ contains in fact the coarse moduli space of smooth pointed genus three curves $\mathcal { M } _ { 3 , 1 }$ . We used aspects of this construction in [11] and [13] to compute the rational cohomology resp.
the orbifold fundamental group of $\mathcal { M } _ { 3 , 1 }$ .

3.3. Abelian arrangements.
Let $X$ be a torsor over an abelian variety $A$ , and $\mathcal { H }$ a finite collection of abelian subtorsors of codimension one.
Denote by $A _ { 0 }$ the identity component of the group of translations of $X$ that stabilize $\mathcal { H }$ (an abelian variety).
First assume that $A _ { 0 }$ reduces to the identity element.
This ensures that $\textstyle { \mathcal { O } } _ { X } ( \sum _ { H \in { \mathcal { H } } } H )$ is ample.
Hence a power of ${ \mathcal { O } } _ { X } ( { \mathcal { H } } )$ separates the points of $X ^ { \circ }$ . It is now easy to see that $\hat { X }$ is defined.
For every $H \in \mathcal { H }$ , $X / H$ is an elliptic curve (the origin is the image of $H$ ). A rational function on $X / H$ that is regular outside the origin and has a pole of order $k$ at the origin can be regarded as a section of ${ \mathcal { O } } _ { X } ( k { \mathcal { H } } )$ . For a sufficiently large $k$ , the collection of these functions define a morphism from $\ddot { X }$ to a projective space which factorizes over $\hat { X }$ . The morphism from $\hat { X }$ to this projective space is finite.
In the general situation (where $A _ { 0 }$ may have positive dimension), the preceding construction can be carried out in a $A _ { 0 }$ - equivariant manner to produce a projective completion $\hat { X }$ of $Y ^ { \circ }$ with $A _ { 0 }$ -action.

Here is a concrete example.
If $R$ is a reduced root system with root lattice $Q$ and $E$ is an elliptic curve, then $X : = \operatorname { H o m } ( Q , E )$ is an abelian variety on which the Weyl group $W$ of $R$ acts.
The fixed point loci of reflections in $W$ define an abelian arrangement $\mathcal { H }$ on $X$ with $\cap _ { H \in { \mathcal { H } } } H$ finite.
So $\hat { X }$ is defined and comes with an action of $W$ .

Example 3.5. For $R$ of type $E _ { 6 }$ , $( \{ \pm 1 \} \cdot W ) \backslash X ^ { \circ }$ is the moduli space of smooth cubic surfaces with hyperplane section isomorphic to $E$ , provided that $E$ has no exceptional automorphisms.
Hence $( \{ \pm 1 \} \cdot W ) \hat { X }$ is some compactification of this moduli space.

Example 3.6. For $R$ of type $E _ { 7 }$ there is a similar relationship with the moduli space of smooth quartic curves with a line section for which the four intersection points define a curve isomorphic to $E$ .

3.4. Ample line bundles over abelian arrangements.
This is a variation on 3.3, which we mention here because of a later application to automorphic forms on ball quotients and type IV domains with product expansions.
Suppose that in the situation of 3.3 we are given an ample line bundle $\ell$ over $X$ . Let $C$ be the corresponding affine cone over $X$ , that is, the variety obtained from the total space of the dual of $\ell$ by collapsing its zero section.
In more algebraic terms, $C _ { H }$ is spec of the graded algebra $\Phi _ { k = 0 } ^ { \infty } H ^ { 0 } ( \ell ^ { \otimes k } )$ . Each $H \in \mathcal { H }$ defines a hypersurface (a subcone of codimension one) $C _ { H } \subset C$ . We put $C _ { \mathcal { H } } : = \cup _ { H \in \mathcal { H } } C _ { H }$ .

Lemma 3.7. If $\mathcal { H } \neq \emptyset$ , then the hypersurface $C _ { \mathcal { H } }$ is the zero set of a regular function on $C$ if and only if the class of $\ell$ in $\operatorname { P i c } ( X ) \otimes \mathbb { Q }$ is a positive linear combination of the classes $H$ , $H \in \mathcal { H }$ .

Proof.
If $f$ is a regular function on $C$ with zero set $C _ { \mathcal { H } }$ , then $f$ must be homogeneous, say of degree $k$ . So $f$ then defines a section of $\ell$ with divisor $\textstyle \sum _ { H \in { \mathcal { H } } } n _ { H } H$ , with $n _ { H }$ a positive integer.
This means that $\ell ^ { \otimes k } \cong \mathcal { O } _ { X } ( \sum _ { H } n _ { H } H )$ . Conversely, an identity of this type implies the existence of such an $f$ . □

Since $\ell$ is ample, the condition that $\ell$ is a positive linear combination of the classes indexed by $\mathcal { H }$ , is not fulfilled if $A _ { 0 }$ (the identity component of the group of translations of $X$ that stabilize $\mathcal { H }$ ) is positive dimensional.

3.5. Dropping the condition of smoothness.
If in the situation of the previous theorem, $Y$ is a normal subvariety of $X$ which meets the members of $\mathrm { P O } ( \mathcal { H } )$ transversally, the strict transform of $Y$ in $\hat { X }$ only depends on the restriction of the arrangement to $Y$ . This suggests that the smoothness condition imposed on $X$ can be weakened to normality.
This is indeed the case:

Definition 3.8. Let $X$ be a normal connected (hence irreducible) variety, $\mathcal { L }$ be a line bundle over $X$ . A linearized arrangement on $X$ consists of a locally finite collection of (reduced) Cartier divisors $\{ H \} _ { H \in \mathcal { H } }$ on $X$ , a line bundle $\mathcal { L }$ and and for each $H \in \mathcal { H }$ an isomorphism ${ \mathcal { L } } ( H ) \otimes { \mathcal { O } } _ { H } \cong { \mathcal { O } } _ { H }$ such that for every connected component $L$ of an intersection of members of $\mathcal { H }$ the following conditions are satisfied:

(i) the natural homomorphism $\oplus _ { H \in \mathcal { H } ^ { L } } \mathbb { Z } _ { H } / \mathbb { Z } _ { H } ^ { 2 } \otimes \mathcal { O } _ { L } \to \mathbb { Z } _ { L } / \mathbb { Z } _ { L } ^ { 2 }$ is surjective and not identically zero on any summand,\
(ii) if we identify $\oplus _ { H \in \mathcal { H } ^ { L } } \mathcal { T } _ { H } / \mathcal { T } _ { H } ^ { 2 } \otimes \mathcal { O } _ { L }$ with $\mathcal { L } \otimes \mathcal { O } _ { L } \otimes _ { \mathbb { C } } \mathbb { C } ^ { \mathcal { H } ^ { L } }$ via the given isomorphisms, then the kernel of the above homomorphism is spanned by a subspace $K ( L , X ) \subset \mathbb { C } ^ { \mathcal { H } ^ { L } }$ whose codimension is that of $L$ in $X$ .

Notice that these conditions imply that the conormal sheaf $\mathcal { T } _ { L } / \mathcal { T } _ { L } ^ { 2 }$ is a locally free $\mathcal { O } _ { L }$ -module of rank equal to the codimension of $L$ in $X$ . The normal space $N ( L , X )$ is now defined as the space of linear forms on $\mathbb { C } ^ { \mathcal { H } ^ { L } }$ that vanish on $K ( L , X )$ .

The conditions of this definition are of course chosen in such a manner as to ensure that the validity of the discussion for the smooth case is not affected.
In particular, we have defined a blow-up $\tilde { X }  X$ whose exceptional locus is a union of divisors $E ( L ) \cong \tilde { L } \times \tilde { \mathbb { P } } ( L , X )$ .

Theorem 3.9. Suppose that is $X$ compact and that a power of $\mathcal { L } ( \mathcal { H } )$ is generated by its sections and separates the points of $X ^ { \circ }$ . Then the pull-back of $\mathcal { L } ( \mathcal { H } )$ t o $\ddot { X }$ is semi-ample and the corresponding projective contraction $\tilde { X }  \hat { X }$ has the property that $\hat { X } - X ^ { \circ }$ is naturally stratified into subvarieties indexed by $\mathrm { P O } ( \mathcal { H } )$ : to $L \in \mathrm { P O } ( \mathcal { H } )$ corresponds a copy of $\mathbb { P } ( L , X ) ^ { \circ }$ (this assignment reverses the order relation).

# 4. Complex ball arrangements

We take up Example 1.8. We shall assume that $n \geq 2$ . It is clear that Theorem 3.2 does not cover this situation and so there is work to do.

4.1. The ball and its natural automorphic bundle.
We choose an arithmetic subgroup $\Gamma$ of $\mathrm { S U } ( \psi ) ( k )$ , although we do not really want to fix it in the sense that we always allow the passage to an arithmetic subgroup of $\Gamma$ of finite index.
In particular, we shall assume that $\Gamma$ is neat, which means that the multiplicative subgroup of $\mathbb { C } ^ { \times }$ generated by the eigen values of elements of $\Gamma$ is torsion free.
This implies that every subquotient of $\Gamma$ that is ‘arithmetically defined’ is torsion free.

We write $X$ for the $\Gamma$ -orbit space of $\mathbb { B }$ . A cusp of $\mathbb { B }$ relative the given $k$ -structure is an element in the boundary of $\mathbb { B }$ in $\mathbb { P } ( W )$ that is defined over $k$ . A cusp corresponds to an isotropic line $I \subset W$ defined over $k$ .

Denote by $\mathbb { L } ^ { \times } \subset W$ the set of $w \in W$ with $\psi ( w , w ) > 0$ . The obvious projection $\mathbb { L } ^ { \times } \to \mathbb { B }$ is a $\mathbb { C } ^ { \times }$ bundle.
We may view this as the complement of the zero section of the tautological line bundle over $\mathbb { P } ( W )$ restricted to $\mathbb { B }$ :

$$
\mathbb { L } : = \mathbb { L } ^ { \times } \times ^ { \mathbb { C } ^ { \times } } \mathbb { C } .
$$

A a nonzero $v \in L$ defines a homogeneous function $f : L - \{ 0 \} \to \mathbb { C }$ of degree $^ { - 1 }$ characterized by the property that $f ( v ) = 1$ . So a nonzero holomorphic function on $\mathbb { L } ^ { \times }$ that is homogeneous of degree $- k$ defines a holomorphic section of $\mathbb { L } ^ { \otimes k }$ and vice versa.

Let us point out here the relation between $\mathbb { L }$ and the canonical bundle of $\mathbb { B }$ . If $p \in \mathbb { B }$ is represented by the line $L \subset W$ , then the tangent space $T _ { p } \mathbf { \mathbb { B } }$ is naturally isomorphic to ${ \mathrm { H o m } } ( L , W / L )$ . So ${ \textstyle \bigwedge } ^ { n } T _ { p } ^ { * } \mathbb { B } \cong L ^ { n + 1 } \otimes { \textstyle \bigwedge } ^ { n + 1 } W ^ { * }$ . This proves that the canonical bundle of $\mathbb { B }$ is $\mathrm { S U } ( \psi )$ -equivariantly isomorphic to $\mathbb { L } ^ { \otimes ( n + 1 ) }$ . We regard $\mathbb { L }$ as the natural automorphic bundle over $\mathbb { B }$ . Since $\Gamma$ is neat, $\mathbb { L }$ drops to a line bundle over $X$ .

4.2. The stabilizer of a cusp.
The following bit of notation will be useful.

Convention 4.1. Given a subspace $J$ of $W$ and a subset $\Omega \subset W$ resp.
$\Omega \subset \mathbb { P } ( W ) -$\
$\mathbb { P } ( J )$ , then $\Omega ( J )$ denotes the image of $\Omega$ in $W / V$ resp.
$\mathbb { P } ( W / J )$ .

Suppose that $J$ is a degenerate subspace of $\mathbb { B }$ , so that $I : = J \cap J ^ { \perp }$ is an isotropic line with $I ^ { \perp } = J + J ^ { \perp }$ . Then

$$
\begin{array} { r } { \mathbb { L } ^ { \times } ( J ) = W / J - I ^ { \perp } / J \quad \mathrm { a n d ~ h e n c e } \quad \mathbb { B } ( J ) = \mathbb { P } ( W / J ) - \mathbb { P } ( I ^ { \perp } / J ) . } \end{array}
$$

In the first case we have the complement of a linear hyperplane in a vector space; in the second case the complement of a projective hyperplane in a projective space, hence an affine space (with $\mathrm { H o m } ( W / I ^ { \perp } , I ^ { \perp } / J )$ as translation group).
The former is a $\mathbb { C } ^ { \times }$ -bundle over this affine space.
Notice that for the maximal choice $J = I ^ { \perp }$ , this is a $\mathbb { C } ^ { \times }$ -bundle over a singleton.

Let $I \subset W$ be an isotropic line.
We begin with recalling the structure of the stabilizer $\mathrm { S U } ( \psi ) _ { I }$ . If $e$ is a generator of $I$ , then the unipotent radical $N _ { I }$ of the $\mathrm { S U } ( \psi )$ -stabilizer of $I$ consists of transformations of the form

$$
T _ { e , v } : z \in W \mapsto z + \psi ( z , e ) v - \psi ( z , v ) e - { \textstyle { \frac { 1 } { 2 } } } \psi ( v , v ) \psi ( z , e ) e
$$

for some $v \in I ^ { \perp }$ . Notice that ${ T _ { e , \lambda v } = T _ { \overline { { \lambda } } e , v } }$ and that $T _ { e , v + \lambda e } = T _ { e , v }$ when $\lambda \in \mathbb R$ . So $T _ { e , v }$ only depends on the image of $e \otimes v$ in $\overline { { I } } \otimes _ { \mathbb { C } } I ^ { \perp } / ( \overline { { I } } \otimes I ) ( \mathbb { R } )$ (observe $\overline { { I } } \otimes I$ has a natural real structure indeed).
A simple calculation yields

$$
T _ { e , u } T _ { e , v } = T _ { e , u + v + \frac { 1 } { 2 } \psi ( u , v ) e }
$$

showing that $N _ { I }$ is an Heisenberg group: its center $Z ( N _ { I } )$ is identified with the real line ${ \sqrt { - 1 } } ( { \overline { { I } } } \otimes _ { \mathbb { C } } I ) ( \mathbb { R } )$ and the quotient $N _ { I } / Z ( N _ { I } )$ with the vector group $\overline { { I } } \otimes I ^ { \perp } / I$ , the commutator given essentially by the skew form that the imaginary part $\psi$ induces on $I ^ { \perp } / I$ . One can see this group act on $\mathbb { B }$ as follows.
The domain $\mathbb { B }$ lies in $\mathbb { P } ( W ) - \mathbb { P } ( I ^ { \perp } )$ . The latter is an affine space for ${ \mathrm { H o m } } ( W / I ^ { \perp } , I ^ { \perp } )$ and so $N _ { I }$ will act on this as an affine transformation group.
This group preserves the fibration

$$
\begin{array} { r } { \mathbb { P } ( W ) - \mathbb { P } ( I ^ { \perp } )  \mathbb { P } ( W / I ) - \mathbb { P } ( I ^ { \perp } / I ) = \mathbb { B } ( I ) . } \end{array}
$$

This is a fibration by affine lines whose base $\mathbb { P } ( W / I ) - \mathbb { P } ( I ^ { \perp } / I )$ is an affine space over $\mathrm { H o m } ( W / I ^ { \perp } , I ^ { \perp } / I )$ . The center $Z ( N _ { I } )$ of $N _ { I }$ respects each fiber and acts there as a group of translations and the quotient vector group $N _ { I } / Z ( N _ { I } )$ is faithfully realized on the base as its group of translations.
The domain $\mathbb { B }$ is fibered over $\mathbb { B } ( I )$ by half planes such that the $Z ( N _ { I } )$ -orbit space of a fiber is a half line.

Let us first decribe $\mathbb { B }$ as such in terms of (partial) coordinates: choose $f \in V$ such that $\psi ( e , f ) = 1$ and denote the orthogonal complement of the span of $e$ and $f$ by $A$ . It is clear that $A$ is negative definite and can as an inner product space be identified with $I ^ { \perp } / I$ . The map $( s , a ) \in \mathbb { C } \times A \mapsto [ s e + f + a ] \in \mathbb { P } ( V ) - \mathbb { P } ( I ^ { \perp } )$ is an isomorphism of affine spaces and in these terms $\mathbb { B }$ is defined by $\mathrm { 2 R e } ( s ) > - \psi ( a , a )$ . This is known as the realization of $\mathbb { B }$ as a Siegel domain of the second kind.

A somewhat more intrinsic description goes as follows.
Consider the group homomorphism $T _ { e } : \mathbb { C } \to { \mathrm { G L } } ( W )$ defined by

$$
T _ { e } ^ { s } ( z ) = z + s \psi ( z , e ) e .
$$

A simple computation shows that

$$
\psi ( T _ { e } ^ { s } z , T _ { e } ^ { s } z ) = \psi ( z , z ) + 2 \mathrm { R e } ( s ) | \psi ( z , e ) | ^ { 2 } .
$$

The restriction of $T _ { e }$ to the imaginary axis parametrizes $Z ( N _ { I } )$ and therefore $T _ { e }$ maps to the complexification $\mathrm { S U } ( \psi )$ . Since $T ^ { s }$ maps $\mathbb { B }$ into itself for $\operatorname { R e } ( s ) \geq 0$ , the image $\mathcal { T } _ { I }$ in $G L ( W )$ of the right half plane is a semigroup that acts (freely) on $\mathbb { B }$ . As the notation suggests it does not depend on the generator $e$ of $I$ . The fibers of $\mathbb { B } \to \mathbb { B } ( I )$ are orbits of this semigroup.
The image of $T$ lies in the complexification of $\mathrm { S U } ( \psi )$ . It is normalized by $N _ { I }$ and so $N _ { I } \mathcal { T } _ { I } = \mathcal { T } _ { I } N _ { I }$ is a semigroup in $\mathrm { S U } ( \psi ) _ { \mathbb { C } }$ . The domain $\mathbb { B }$ is a free orbit of this semigroup.

Suppose now that $I$ is defined over $k$ . The Levi quotient $\mathrm { { ; U } } ( \psi ) _ { I } / N _ { I }$ of $\mathrm { S U } ( \psi ) _ { I }$ is the group of unitary transformations of $I ^ { \perp } / I$ , hence compact, and the corresponding subquotient of $\Gamma$ is finite.
Since we assumed $\Gamma$ to be neat, the latter is trivial and so the stabilizer $\Gamma _ { I }$ is contained in $N _ { I }$ . It is in fact a cocompact subgroup of $N _ { I }$ : the center $Z ( \Gamma _ { I } )$ of $\Gamma _ { I }$ is infinite cyclic (a subgroup of ${ \sqrt { - 1 } } ( { \overline { { I } } } \otimes I ) ( \mathbb { R } ) )$ , and $\Gamma _ { I } / Z ( \Gamma _ { I } )$ is an abelian group that naturally lies as a lattice in the vector group $\overline { { I } } \otimes I ^ { \perp } / I$ .

4.3. Compactications of a ball quotient.
Let $J$ be a complex subspace of $W$ with radical $I$ . The group $N ^ { J }$ of $\gamma \in \Gamma$ that act as the identity on $J ^ { \perp } \cong \overline { { W / J } } ^ { * }$ is a normal (Heisenberg) subgroup of $N _ { I }$ with quotient identifyable with the vector group $\overline { { I } } \otimes I ^ { \perp } / J$ ). The latter may be regarded as the vector space of translations of the affine space $\mathbb { B } ( J ) = \mathbb { P } ( W / J ) - \mathbb { P } ( I ^ { \perp } / J )$ . Let us assume that $J$ is defined over $k$ . Then the discrete counterparts of these statements hold for $\Gamma$ . In particular, $\Gamma _ { I } / \Gamma ^ { J }$ can be identified with a lattice in $\overline { { I } } \otimes J / I$ . So if we denote the orbit space of this lattice acting on $\mathbb { B } ( J )$ by $X ( J )$ , then $X ( J )$ is a principal homogenenous space of a complex torus that has $\overline { { I } } \otimes I ^ { \perp } / J$ ) as its universal cover.
For an intermediate $k$ -space $I \subset J ^ { \prime } \subset J$ we have a natural projection $X ( I )  X ( J )$ of abelian torsors.
Notice that $X ( I ^ { \perp } )$ is just a singleton.

Definition 4.2. An arithmetic system (of degenerate subspaces) assigns in a $\Gamma$ - equivariant manner to every $k$ -isotropic line $I$ a degenerate subspace $j ( I )$ defined over $k$ with radical $I$ . We call the two extremal cases $b b ( I ) : = I ^ { \perp }$ resp.
$t o r ( I ) : = I$ the Baily-Borel system and the toroidal system respectively.

Such a system $j$ leads to a compactification $X ^ { j }$ of $X$ as follows.
Form the disjoint unions

$$
( \mathbb { L } ^ { \times } ) ^ { j } : = \mathbb { L } ^ { \times } \sqcup _ { I \mathrm { ~ } k \mathrm { - i s o t r o p i c } } \mathbb { L } ^ { \times } ( j ( I ) ) \quad \mathrm { a n d } \quad \mathbb { B } ^ { j } : = \mathbb { B } \sqcup _ { I \mathrm { ~ } k \mathrm { - i s o t r o p i c } } \mathbb { B } ( j ( I ) ) .
$$

Both come with an obvious action of $\Gamma$ and the projection $( \mathbb { L } ^ { \times } ) ^ { j }  \mathbb { B } ^ { j }$ is a $\mathbb { C } ^ { \times }$ - bundle.
We introduce a $\Gamma$ -invariant topology on these sets as follows.
Recall that $N ^ { j ( I ) }$ is the subgroup of $g \in N _ { I }$ that act as the identity on $W / j ( I )$ . Then $N ^ { j ( I ) } \mathcal { T } _ { I } =$ $\mathcal { T } _ { I } N ^ { j ( I ) }$ is a semigroup and the fibers of $\mathbb { B } \to \mathbb { B } ( j ( I ) )$ are orbits of this semigroup.
A basis of a topology on $( \mathbb { L } ^ { \times } ) ^ { j }$ is specified by the following collection of subsets:

(i) the open subsets of $\mathbb { L } ^ { \times }$ ,\
(ii) for every $k$ -isotropic line $I$ and $N ^ { j ( I ) } \mathcal { T } _ { I }$ -invariant open subset $\Omega \subset \mathbb { L } ^ { \times }$ the subset $\Omega \sqcup \Omega ( j ( I ) )$ .

The same definition with obvious modifications defines a topology for $\mathbb { B } ^ { j }$ . It makes

$$
\mathbb { L } ^ { j } : = ( \mathbb { L } ^ { \times } ) ^ { j } \times ^ { \mathbb { C } ^ { \times } } \mathbb { C } .
$$

a topological complex line bundle over $\mathbb { B } ^ { j }$ . We are interested in the orbit space

$$
X ^ { j } : = \Gamma \backslash \mathbb { B } ^ { j }
$$

and the line bundle over $X ^ { j }$ defined by $\Gamma \backslash \mathbb { L } ^ { j }$ . Notice that as a set, $X ^ { j }$ is the disjoint union of $X$ and the torsors $X ( j ( I ) )$ , where $I$ runs over a system of representatives of the $\Gamma$ -orbits in the set of cusps.
Fundamental results from the theory of automorphic forms assert that:

(i) $\Gamma$ has only finitely many orbits in its set of cusps and $X ^ { j }$ is a compact Hausdorff space.\
(ii) The sheaf of complex valued continuous functions on $X ^ { j }$ that have analytic restrictions to the strata $X$ and $X ( j ( I ) )$ gives $X ^ { j }$ the structure of a normal analytic variety.\
(iii) The line bundle $\mathbb { L } ^ { j } \to \mathbb { B } ^ { j }$ descends to an analytic line bundle on $\Gamma \backslash \mathbb { B } ^ { j }$ (a local section is analytic if it is continuous and analytic on strata).
We denote its sheaf of sections by $\mathcal { L }$ (the suppression of $j$ in the notation is justified by (v) below).\
(iv) The line bundle $\mathcal { L }$ is ample on $X ^ { b b }$ , so that the graded algebra $A ^ { \bullet } : = \oplus _ { k } H ^ { 0 } ( X ^ { b b } , { \mathcal { L } } ^ { \otimes k } )$ is finitely generated with positive degree generators, having $X ^ { b b }$ as its proj.\
(v) If $j ^ { \prime }$ is an arithmetic system that refines $j$ in the sense that $j ^ { \prime } ( I ) \subset j ( I )$ for all $I$ , then the obvious map $X ^ { j ^ { \prime } }  X ^ { j }$ is a morphism of analytic spaces and the line bundle $\mathcal { L }$ on $X ^ { j ^ { \prime } }$ is the pull-back of of its namesake on $X ^ { j }$ .

The projective variety $X ^ { b b }$ is known as the Baily-Borel compactification and $X ^ { t o r }$ as the toric compactification of $X$ . The boundary of $X ^ { b b } - X$ is finite (its points are called the cusps of $X ^ { b b }$ ).

Let us see how this works out locally.
Given a $k$ -isotropic line, then the orbit space $E _ { I } : = \Gamma _ { I } \backslash ( \mathbb { P } ( W ) - \mathbb { P } ( I ^ { \perp } ) )$ lies as a $\mathbb { C } ^ { \times }$ -bundle over $X ( I )$ and contains $\Gamma _ { I } \backslash \mathbb { B }$ as a punctured disc bundle.
The obvious morphism $\Gamma _ { I } \backslash \mathbb { B }  \Gamma \backslash \mathbb { B } = X$ restricts to an isomorphism of an open subset of $X$ (in fact, a punctured neighborhood of the cusp defined by $I$ ) onto a smaller punctured disc bundle so that the insertion of $X ( j ( I ) )$ can be described in terms of the $\mathbb { C } ^ { \times }$ -bundle $E _ { I } \to X ( I )$ . For instance, the toric compactification amounts to simply filling in the zero section: we get $E _ { I } ^ { t o r }$ as a union of $E _ { I }$ and $X ( I )$ . The line bundle $E _ { I } ^ { t o r }  X ( I )$ is anti-ample (the real part of $\psi _ { I }$ is a Riemann form).
This implies that we can contract the zero section analytically; the result is a partial Baily-Borel compactification $E _ { I } ^ { b b }$ , which adds to $E ^ { I }$ a singleton.
The intermediate case $E _ { I } ^ { j }$ (a union of $E _ { I }$ and $X ( j ( I ) ) )$ is obtained from $E _ { I } ^ { t o r }$ by analytical contraction via the map $X ( I ) \to X ( j ( I ) )$ . (This in indeed possible.)

# 5. Arithmetic ball arrangements and their automorphic forms

Let now be given a collection $\mathcal { H }$ of hyperplanes of $W$ of hyperbolic signature that is arithmetically defined relative to $\Gamma$ . So $\mathcal { H }$ , when viewed as a subset of $\mathbb { P } ( W ^ { * } )$ , is a finite union of $\Gamma$ -orbits and contained in $\mathbb { P } ( W ^ { * } ) ( k )$ .

We note that for each $H \in { \mathcal { H } }$ , $\mathbb { B } _ { H } = \mathbb { P } ( H ) \cap \mathbb { B }$ is a symmetric subdomain of $\mathbb { B }$ . Its $\Gamma$ -stabilizer $\Gamma _ { H }$ is arithmetic in its $\mathrm { S U } ( \psi ) .$ -stabilizer and so the orbit space $X _ { H } : = \Gamma _ { H } \backslash \mathbb { B } _ { H }$ has its own Baily-Borel compactification $X _ { H } ^ { b b }$ . The inclusion $\mathbb { B } _ { H } \subset \mathbb { B }$ induces an analytic morphism $X _ { H } \to X$ . This morphism is finite and birational onto its image (which we denote by $D _ { H }$ ) and extends to a finite morphism $X _ { H } ^ { b b }  X ^ { b b }$ whose image is the closure of $D _ { H }$ in $X ^ { b b }$ (which we denote by $D _ { H } ^ { b b }$ ). Clearly, $D _ { H } ^ { b b }$ only depends on the $\Gamma$ -equivalence class of $H$ and so the union $D _ { \mathcal { H } } ^ { b b } : = \cup _ { H \in \mathcal { H } } D _ { H } ^ { b b }$ is a finite one.

Lemma 5.1. After passing to an arithmetic subgroup of $\Gamma$ of finite index, each hypersurface $D _ { H } ^ { b b }$ is without self-intersection in the sense that $X _ { H } ^ { b b } \  \ D _ { H } ^ { b b }$ is $a$ homeomorphism and $X _ { H }  D _ { H }$ is an isomorphism.

Proof.
We do this in two steps.
The set $S _ { H }$ of $\gamma \in \Gamma$ such that $\gamma \mathbb { B } _ { H } \cap \mathbb { B } _ { H }$ is nonempty and not equal to $\mathbb { B } _ { H }$ is a union of double cosets of $\Gamma _ { H }$ in $\Gamma$ distinct from $\Gamma _ { H }$ . Each such double coset defines an ordered pair of distinct irreducible hypersurfaces in $X _ { H }$ with the same image in $X$ and vice versa.
Since $X _ { H }  D _ { H }$ is finite and birational, there are only finitely many such pairs of irreducible hypersurfaces and hence $S _ { H } = \Gamma _ { H } C _ { H } \Gamma _ { H }$ for some finite set $C _ { H } \subset \Gamma _ { H }$ . Let $C$ be the union of the sets $C _ { H }$ , for which $H$ runs over a system of representatives of $\Gamma$ in $\mathcal { H }$ . This is a finite subset of $\Gamma - \{ 1 \}$ . If we now pass from $\Gamma$ to a normal arithmetic subgroup of $\Gamma$ of finite index which avoids $C$ , then the natural maps $X _ { H }  X$ are injective and local embeddings.
They are also proper, and so they are closed embeddings.

It is still possible that $X _ { H } ^ { b b }  X ^ { b b }$ fails to be injective for some for some $H$ (although this can only happen when $n = 2$ ). We avoid this situation essentially by proceeding as before: given isotropic line $I \subset W$ defining a cusp then the set $\gamma \in \Gamma - \Gamma _ { I }$ such that for some $H \in { \mathcal { H } } \gamma H \neq H$ and $\gamma H \cap H \supset I$ is a union of double cosets of $\Gamma _ { I }$ in $\Gamma$ . The number of such double cosets is at most the number of branches of $D _ { H } ^ { b b }$ at this cusp and hence finite.
If $C _ { I } ^ { \prime } \subset \Gamma - \Gamma _ { I }$ is a system of representatives, then let $C ^ { \prime }$ be a of union $C _ { I } ^ { \prime }$ , where $I$ runs over a (finite) system of representatives of $\Gamma$ in the set $\mathbb { B } ^ { b b } - \mathbb { B }$ . Choose a normal arithmetic subgroup of $\Gamma$ of finite index which avoids $C ^ { \prime }$ . Then this subgroup is as desired.
□

We assume from now on that the hypersurfaces $D _ { H } ^ { b b }$ are without self-intersection in the sense of Lemma 5.1 and we identify $X _ { H }$ with its image $D _ { H }$ in $X$ . Then the collection $\mathcal { H } _ { \Gamma }$ of the hypersurfaces $D _ { H } ^ { b b }$ is an arrangement on $X$ . We want to determine whether the algebra

$$
A _ { \mathcal { H } } ^ { \bullet } : = \oplus _ { k = 0 } ^ { \infty } H ^ { 0 } ( X ^ { b b } , \mathcal { L } ( \mathcal { H } _ { \Gamma } ) ^ { ( k ) } ) )
$$

is finitely generated and if so, find its proj.

The hypersurface $D _ { H } ^ { b b }$ on $X ^ { b b }$ will in general not support a Cartier divisor.
On ot in hand, the closure will be dominate $D _ { H } ^ { t o r }$ $D _ { H }$ in his $X ^ { t o r }$ is even smooth.
So the blow-up ofen also true for the minimal normal $D _ { H } ^ { b b }$ $X ^ { b b }$ $X ^ { t o r }$ blow-up of $X ^ { b b }$ for which the strict transform of each $D _ { H } ^ { b b }$ is a Cartier divisor.
It is easy to describe this intermediate blow-up of $X ^ { b b }$ . For this, we let for a $k$ -isotropic line $I \subset W$ , $j _ { \mathcal { H } } ( I )$ be the common intersection of $I ^ { \perp }$ and the members of $\mathcal { H }$ that contain $I$ .

Lemma 5.2. The assignment $j _ { \mathcal { H } }$ is an arithmetic system relative to $\Gamma$ and the corresponding morphism $X ^ { j _ { \mathcal { H } } }  X ^ { b b }$ is the smallest normalized blow-up that makes the fractional ideals $\mathcal { O } _ { X ^ { b b } } ( D _ { H } ^ { b b } )$ invertible.
The strict transform of $D _ { H } ^ { b b }$ in $X ^ { j \varkappa }$ is an integral Cartier divisor.

Proof.
Let $I \subset W$ be a $k$ -isotropic line.
Then $J : = j _ { \mathcal { H } } ( I )$ contains $I$ , is contained in $I ^ { \perp }$ and is defined over $k$ since it is an intersection of hyperplanes defined over $k$ . Let $H \in \mathcal { H }$ contain $I$ . Then $H$ defines a hypersurface $E _ { I , H } ^ { b b }$ in $E _ { I } ^ { b b }$ and an abelian subtorsor $X ( I ) _ { H }$ of $X ( I )$ with quotient $X ( H \cap I ^ { \perp } )$ . The latter is a genus one curve which apparently comes with an origin $o$ (it is an elliptic curve) and the complement of this origin of is affine.
Any regular function on the affine curve $X ( H \cap I ^ { \bot } ) - \{ o \}$ with given pole order at $o$ lifts to a regular function on $E _ { I } ^ { t o r } - E _ { I , H } ^ { t o r }$ with the same pole order along $E _ { I , H } ^ { t o r }$ (and zero divisor disjoint from the polar set).
This proves that the effect of theto replace the vertex lize of owiby e fractional ideal . The strict tran $\mathcal { O } _ { E _ { I } ^ { b b } } ( E _ { I , H } ^ { b b } )$ $X ( I ^ { \perp } )$ $E _ { I } ^ { b b }$ $X ( H \cap I ^ { \perp } )$ $E _ { I , H } ^ { b b }$ $H \in { \mathcal { H } }$ contain $I$ , then the vertex gets replaced by $X ( J )$ as asserted.
□

With Convention 2.3 in mind we write $X ^ { j }$ for $X ^ { j \varkappa }$ .

Proposition 5.3. For $\it l$ sufficiently large, $\mathcal { L } ( \mathcal { H } _ { \mathrm { T } } ) ^ { ( l ) }$ is generated by its sections.

We prove this proposition via a number of lemma’s.

Let $\boldsymbol { \mathcal { O } }$ be a $\Gamma$ -orbit in $W ( k ) \ : - \ : \{ 0 \}$ . The projectivization of the hyperplane perpendicular to $w \in \mathcal { O }$ meets $\mathbb { B }$ precisely when $\psi ( w , w ) < 0$ and in that case $\psi ( \textit { \textbf { \xi } } , w ) ^ { - 1 }$ defines a meromorphic section of $\mathcal { O } _ { \mathbb { B } } ( - 1 )$ . Let $\it { \Delta } l$ be an integer $> 2 n + 1$ and consider the Poincar´e-Weierstrass series

$$
F _ { \mathcal { O } } ^ { ( l ) } : = \sum _ { w \in \mathcal { O } } \psi ( \mathbf { \epsilon } , w ) ^ { - l } .
$$

Lemma 5.4. Let $K \subset \mathbb { L } ^ { \times }$ be a compact subset.
Then the set $\mathcal { O } _ { 0 }$ of $w \in \mathcal { O }$ for which $\mathbb { P } ( w ^ { \perp } )$ meets $K$ is finite and the series

$$
\sum _ { w \in \mathcal { O } - \mathcal { O } _ { 0 } } \psi ( \mathbf { \partial } , w ) ^ { - l }
$$

converges uniformly and absolutely on $K$ . In particular, $F _ { \mathcal { O } } ^ { ( l ) }$ represents a meromorphic function on $\mathbb { L } ^ { \times }$ that is homogeneous of degree $- l$ .

Proof.
Since $\boldsymbol { \mathcal { O } }$ is an orbit of the arithmetic group $\Gamma$ in $W ( k ) \ : - \ : \{ 0 \}$ , the ${ \mathcal { O } } _ { k }$ - submodule $\Lambda \subset W$ spanned by this orbit is discrete in $W$ . Now $\boldsymbol { \mathcal { O } }$ is also contained in the real hypersurface $\Sigma _ { a } ~ \subset ~ W$ defined by $\psi ( w , w ) = a$ for some $a \ < \ 0$ . The map $m : \Sigma _ { a }  [ 0 , \infty )$ defined by $m ( w ) : = \mathrm { m i n } _ { z \in K } | \psi ( z , w ) |$ is proper. A standard argument shows that the cardinality of $\Lambda \cap \Sigma _ { a } \cap m ^ { - 1 } ( N - 1 , N ]$ is proportional to the $( 2 n + 1 )$ -volume of $\Sigma _ { a } \cap m ^ { - 1 } ( N - 1 , N ]$ and hence is $\leq c N ^ { 2 n }$ for some $c > 0$ . So $\mathcal { O } _ { 0 }$ is finite and for $z \in K$ we have the uniform estimate

$$
\sum _ { w \in \mathcal { O } - \mathcal { O } _ { 0 } } \left. \psi ( z , w ) \right. \leq \mathrm { c o n s t a n t } + \sum _ { N = 2 } ^ { \infty } c N ^ { 2 n } ( N - 1 ) ^ { - l } .
$$

The righthand side converges since $l > 2 n + 1$ .

For $\boldsymbol { \mathcal { O } }$ and $\it { \Delta } l$ as above, we extend $F _ { \mathcal { O } } ^ { ( l ) }$ to each stratum $\mathbb { L } ^ { \times } ( I )$ of $( \mathbb { L } ^ { \times } ) ^ { t o r }$ by taking the subseries defining $F _ { \mathcal { O } } ^ { ( l ) }$ whose terms makes sense on that stratum:

$$
F _ { \mathcal { O } } ^ { ( l ) } ( z ) : = \sum _ { w \in \mathcal { O } \cap I ^ { \perp } } \psi ( z , w ) ^ { - l } \mathrm { ~ i f ~ } z \in \mathbb { L } ^ { \times } ( I ) .
$$

It is clear from the preceding that this subseries represents a meromorphic function on $\mathbb { L } ^ { \times } ( I )$ . The bundle $\mathbb { L } ^ { \times } ( I )  \mathbb { B } ( I )$ is canonically isomorphic to the trivial bundle with fiber $W / I ^ { \perp } - \{ 0 \}$ . So after choosing a generator of $W / I ^ { \perp }$ we can think of this subseries as defining a rational function on $\mathbb { B } ( I )$ .

Lemma 5.5. The Γ-invariant piecewise rational function on $( \mathbb { L } ^ { \times } ) ^ { t o r }$ defined by $F _ { \mathcal { O } } ^ { ( l ) }$ represents a meromorphic section of $\mathcal { L }$ over the toroidal compactification $X ^ { t o r }$ of $X$ .

Proof.
Given the $k$ -isotropic line $I \subset W$ , choose a $k$ -generator $e \in { I }$ and consider the action of the right half plane on $\mathbb { L } ^ { \times }$ defined by $T _ { e }$ (see Subsection 4.2): $T _ { e } ^ { s } ( z ) =$ $\boldsymbol { z } + s \psi ( \boldsymbol { z } , e ) e$ . In view of the characterization in Subsection 4.3 of the analytic structure on $( \mathbb { L } ^ { \times } ) ^ { t o r }$ it is enough to show that $\mathrm { l i m } _ { \mathrm { R e } ( s )  + \infty } F _ { \mathcal { O } } ^ { ( l ) } T _ { e } ^ { s } | K$ exists as a meromorphic function and this limit is equal to the subseries defined above.
We claim that with $K$ , $\Sigma _ { a }$ and $\Lambda$ as in the proof of Lemma 5.4 above, the map

$$
( z , w ) \in K \times ( \Lambda \cap ( \Sigma _ { a } \setminus I ^ { \perp } ) ) \mapsto \operatorname { R e } \left( \frac { \psi ( z , w ) } { \psi ( z , e ) \psi ( e , w ) } \right)
$$

is bounded from below, say by $\ge - s _ { o }$ . Once we establish this we are done, for then

$$
s \mapsto | \psi ( T _ { e } ^ { s } z , w ) | = | \psi ( z , e ) \psi ( e , w ) | \cdot \Big | \frac { \psi ( z , w ) } { \psi ( z , e ) \psi ( e , w ) } + \mathrm { R e } ( s ) \Big |
$$

is monotone increasing for $\mathrm { R e } ( s ) \geq s _ { o }$ for any for $z \in K$ and $w \in \mathcal { O } \setminus I ^ { \perp }$ , implying that the limit is as stated.

In order to prove our claim, we first note that without any loss of generality we may assume that $\psi ( z , e ) = 1$ for all $z \in K$ (just replace $z \in K$ by $\psi ( z , e ) ^ { - 1 } z )$ . Write $e _ { 0 }$ for $e$ and choose an isotropic $e _ { 1 } \in W ( k )$ such that $\psi ( e _ { 0 } , e _ { 1 } ) = 1$ . Since the orthogonal complement of $\mathbb { C } e _ { 0 } + \mathbb { C } e _ { 1 }$ is negative definite, we denote the restriction of $- \psi$ to this complement by $\langle ~ , ~ \rangle$ . We write any $w \in W$ as $w _ { 0 } e _ { 0 } + w _ { 1 } e _ { 1 } + w ^ { \prime }$ with $w ^ { \prime } \perp ( \mathbb { C } e _ { 0 } + \mathbb { C } e _ { 1 } )$ . Notice that the function $w \in \Lambda \setminus I ^ { \perp } \mapsto | w _ { 1 } | = | \psi ( w , e ) |$ has a positive minimum $c > 0$ . Then for $z \in K$ and $w \in \Lambda \cap ( \Sigma _ { a } \setminus I ^ { \perp } )$ we have the

estimate

$$
\begin{array} { r l } & { \mathrm { R e } \Big ( \frac { \psi ( z , w ) } { \psi ( e , w ) } \Big ) = \mathrm { R e } \Big ( \frac { z _ { 0 } \overline { { w } } _ { 1 } + \overline { { w } } _ { 0 } - \langle z ^ { \prime } , w ^ { \prime } \rangle } { \overline { { w } } _ { 1 } } \Big ) } \\ & { \quad \quad \quad \quad \quad \quad \quad = \mathrm { R e } ( z _ { 0 } + | w _ { 1 } | ^ { - 2 } \overline { { w } } _ { 0 } w _ { 1 } - \langle z ^ { \prime } , w ^ { \prime } / w _ { 1 } \rangle ) } \\ & { \quad \quad \quad \quad \quad = \mathrm { R e } ( z _ { 0 } ) + | w _ { 1 } | ^ { - 2 } ( a + \langle w ^ { \prime } , w ^ { \prime } \rangle ) - \langle z ^ { \prime } , w ^ { \prime } / w _ { 1 } \rangle ) } \\ & { \quad \quad \quad \quad = \mathrm { R e } ( z _ { 0 } ) + | w _ { 1 } | ^ { - 2 } a + \| w ^ { \prime } / w _ { 1 } - \frac { 1 } { 2 } z ^ { \prime } \| ^ { 2 } - \frac { 1 } { 4 } \| z ^ { \prime } \| ^ { 2 } } \\ & { \quad \quad \quad \quad \quad \geq \mathrm { R e } ( z _ { 0 } ) - c ^ { - 2 } a - \frac { 1 } { 4 } \| z ^ { \prime } \| ^ { 2 } . } \end{array}
$$

The claim follows and with it, the lemma.

If $I$ and $\boldsymbol { \mathcal { O } }$ are such that $\mathcal { O } \cap I ^ { \perp }$ is a single $\Gamma _ { I }$ -orbit, say of $w _ { 0 } \in I ^ { \perp }$ , then if $H _ { 0 }$ denotes the orthogonal complement of $w _ { 0 }$ in $W$ , $H _ { 0 } \cap I ^ { \perp }$ is independent of the choice of $w _ { 0 }$ . The same is true for the abelian divisor $X ( I ) _ { H _ { 0 } }$ in $X ( I )$ and the restriction of $F _ { \mathcal { O } } ^ { ( l ) }$ to the abelian variety $X ( I )$ is in fact the pull-back of a meromorphic function on the elliptic curve $X ( I ) / X ( I ) _ { H _ { 0 } } = X ( H _ { 0 } \cap I ^ { \perp } )$ . It has the Weierstrass form in the sense of Lemma 5.6 below.

Lemma 5.6. Let $L \subset \mathbb { C }$ be a lattice.
Then for $k \geq 3$ the series

$$
\wp _ { k } ( z ) : = \sum _ { a \in L } ( z + a ) ^ { - k }
$$

represents a rational function on the elliptic curve $\mathbb { C } / L$ and for any $k _ { 0 } \geq 3$ , the $\wp _ { k }$ with $k \geq k _ { 0 }$ generate the function field of this curve.

We omit the proof of this well-known fact.

Proof of 5.3. It suffices to prove this statement for $\mathcal { L } ( \mathcal { H } _ { \mathrm { T } } ) ^ { ( k ) }$ ) instead of $\mathcal { L } ( \mathcal { H } _ { \mathrm { T } } )$ for some $k > 0$ . We first show that for $k > 2 n + 1$ the sections of $\mathcal { L } ( \mathcal { H } _ { \mathrm { T } } ) ^ { ( k ) }$ generate this sheaf over $X$ . Let $H _ { 0 } \in \mathcal { H }$ and $z _ { o } \in H _ { 0 } \cap \mathbb { L } ^ { \times }$ . Choose $w _ { 0 } \in W ( k )$ spanning the orthogonal complement of $H _ { 0 }$ and let $\boldsymbol { \mathcal { O } }$ denote the $\Gamma$ -orbit of $w _ { 0 }$ . Then according to Lemma 5.4 $F _ { \mathcal { O } } ^ { ( k ) }$ defines a section of $\mathcal { L } ( \mathcal { H } _ { \mathrm { T } } ) ^ { ( k ) }$ . It is in fact a section of the invertible subsheaf $\mathcal { L } ( D _ { H _ { 0 } } ^ { j } ) ^ { ( k ) }$ on $X ^ { j }$ and nonzero as such at $z _ { 0 }$ . These subsheafs generate $\mathcal { L } ( \mathcal { H } _ { \mathrm { T } } ) ^ { ( k ) }$ .

So it remains to verify the generating property over a cusp.
But this follows from the conjunction of Lemma’s 5.5 and 5.6. □

This has the following corollary, which we state as a theorem:

Theorem 5.7. The line bundle $\mathcal { L }$ and the collection of strict transforms of the hypersurfaces $D _ { H } ^ { b b }$ in $X ^ { j \varkappa }$ satisfy the conditions of Theorem 3.9 so that the diagram of birational morphisms and projective completions of $X ^ { \circ }$

$$
X ^ { b b }  X ^ { j \varkappa }  \tilde { X } ^ { \mathcal { H } }  \hat { X } ^ { \mathcal { H } }
$$

is defined.
The morphism $\tilde { X } ^ { \mathcal { H } }  X ^ { b b }$ is the blowup defined by $\mathcal { O } _ { X ^ { b b } } ( \mathcal { H } _ { \Gamma } )$ on $X ^ { b b }$ . The coherent pull-back of $\mathcal { L } ( \mathcal { H } _ { \mathrm { T } } )$ to $\ddot { X } ^ { \mathcal { H } }$ is semiample and defines the contraction $\tilde { X } ^ { \mathcal { H } } \to \hat { X } ^ { \mathcal { H } }$ .

It is worth noting that the difference $\hat { X } ^ { \mathcal { H } } - X ^ { \circ }$ need not be a hypersurface: if $\mathcal { H }$ is nonempty, then the complex codimension of this boundary is the minimal dimension of a nonempty intersection of members of $\mathcal { H }$ in $\mathbb { B }$ . In many interesting examples this is $> 1$ and in such cases a section of $\mathcal { L } ^ { \otimes k }$ over $X ^ { \circ }$ extends to a section of $\hat { \mathcal { L } } ( \mathcal { H } _ { \Gamma } ) ^ { \otimes k }$ . This gives the following useful application:

Corollary 5.8. Let $\mathcal { H }$ be an arithmetic arrangement on a complex ball $\mathbb { B }$ of dimension $\geq 2$ that is arithmetic relative to the arithmetic group $\Gamma$ . Suppose that any intersection of members of the arrangement $\mathcal { H }$ that meets $\mathbb { B }$ has dimension $\geq 2$ in $\mathbb { B }$ . Then the algebra of automorphic forms

$$
\oplus _ { k \in \mathbb { Z } } H ^ { 0 } ( \mathbb { B } ^ { \circ } , { \mathcal { O } } ^ { \mathrm { a n } } ( \mathbb { L } ) ^ { \otimes k } ) ^ { \Gamma }
$$

(where L is the natural automorphic bundle over $\mathbb { B }$ and $\mathbb { B } ^ { \circ }$ is the arrangement complement) is finitely generated with positive degree generators and its proj is the modification $\hat { X } ^ { \mathcal { H } }$ of $X ^ { b b }$ .

# 6. Ball arrangements that are defined by automorphic forms

The hypotheses of Corollary 5.8 are in a sense opposite to those that are needed to ensure that an arithmetically defined ball arrangement is the zero set of an automorphic form on that ball.
This will follow from Lemma 3.7 and the subsequent remark.
Assume we are in the situation of this section and that we are given a function $H \in { \mathcal { H } } \mapsto n _ { H } \in \{ 1 , 2 , \cdot \cdot \cdot \}$ that is constant on the $\Gamma$ -orbits.
This amounts to giving an effective divisor on $X ^ { b b }$ supported by $D _ { \mathcal { H } } ^ { b b }$ . Let $I \subset W$ be a $k$ -isotropic line contained in a member of $\mathcal { H }$ . Then the collection $\mathcal { H } _ { I }$ of $H \in \mathcal { H }$ passing through $I$ decomposes into a finite collection of $\Gamma _ { I }$ -orbits of hyperplanes.
Each $H \in \mathcal { H } _ { I }$ defines a hyperplane $( I ^ { \perp } / I ) _ { H }$ in $I ^ { \perp } / I$ with $\Gamma _ { I }$ -equivalent hyperplanes defining the same $\Gamma _ { I }$ -orbit.

Suppose now that $\textstyle \sum _ { H } n _ { H } { \mathbb { B } } _ { H }$ is the divisor of an automorphic form.
Then Lemma 3.7 implies that

$$
\sum _ { H \in \Gamma _ { I } \backslash \mathcal { H } _ { I } } n _ { H } ( I ^ { \perp } / I ) _ { H }
$$

should represent the Euler class of an ample line bundle.
This Euler class is in fact known to be the negative of the Hermitian form on $I ^ { \perp } / I$ . This implies that the intersection of the hyperplanes $( I ^ { \perp } / I ) _ { H }$ is reduced to the origin.
In other words: the collection of $H \in \mathcal { H }$ containing a $k$ -isotropic line is either empty or has intersection equal to that line.
Although this is formally weaker than the above property, this simple requirement turns out be already rather strong.

Question 6.1. Suppose that the effective divisor $\textstyle \sum _ { H } n _ { H } { \mathbb { B } } _ { H }$ is at every cusp the zero divisor of an automorphic function at that cusp.
In other words, suppose that the corresponding Weil divisor on the Baily-Borel compactification is in fact a Cartier divisor.
Is it then the divisor of an automorphic form?
More generally, if $H \in \mathcal { H } \mapsto n _ { H }$ is $\mathbb { Z }$ -valued and $\Gamma$ -invariant in such a way that $\textstyle \sum _ { H } n _ { H } { \mathbb { B } } _ { H }$ defines a Cartier divisor on the Baily-Borel compactification, is $\textstyle \sum _ { H } n _ { H } { \mathbb { B } } _ { H }$ then the divisor of a meromorphic automorphic form?

In case such an automorphic form exists, we expect it of course to have a product expansion.

# 7. Some applications

There are a number of concrete examples of moduli spaces to which Corollary 5.8 applies.
To make the descent from the general to the special in Bourbakian style, let us start out from the following situation: we are given an integral projective variety $Y$ with ample line bundle $\eta$ and a reductive group $G$ acting on the pair $( Y , \eta )$ . Assume also given a $G$ -invariant open-dense subset $U \subset Y$ consisting of $G$ -stable orbits.
Then $G$ acts properly on $U$ and the orbit space $G \backslash U$ exists as a quasi-projective orbifold with the restriction $\eta | U$ descending to an orbifold line bundle $G \backslash ( \eta | U )$ over $G \backslash U$ . To be precise, geometric invariant theory tells us that the algebra of invariants $\oplus _ { k \in \mathbb { Z } } H ^ { 0 } ( Y , \eta ^ { \otimes k } ) ^ { G }$ is finitely generated with positive degree generators.
Its proj is denoted $G \backslash Y ^ { \mathrm { s s } }$ , because a point of this proj can be interpreted as a minimal $G$ -orbit in the semistable locus $Y ^ { \mathrm { s s } } \subset Y$ . It contains $G \backslash U$ as an open dense subvariety.
The orbifold line bundle $G \backslash ( \eta | U )$ extends to an orbifold line bundle $G \backslash \backslash \eta$ over $G \backslash Y ^ { \mathrm { s s } }$ in a way that the space of global sections of its $k$ th tensor power can be identified with $H ^ { 0 } ( Y , \eta ^ { \otimes k } ) ^ { G }$ .

Theorem 7.1. Suppose we are given identification of $G \backslash ( U , \eta | U )$ with a pair coming from a ball arrangement $( X ^ { \circ } , { \mathcal { L } } | X ^ { \circ } )$ , such that

(i) any nonempty intersection of members of the arrangement $\mathcal { H }$ with $\mathbb { B }$ has dimension $\geq 2$ and (ii) the boundary $G \backslash \backslash Y ^ { \mathrm { s s } } - G \backslash U$ is of codimension $\geq 2$ in $G \backslash Y ^ { \mathrm { s s } }$ .

Then this identification determines an isomorphism

$$
\scriptstyle \oplus _ { k \in \mathbb { Z } } H ^ { 0 } ( Y , \eta ^ { \otimes k } ) ^ { G } \cong \oplus _ { k \in \mathbb { Z } } H ^ { 0 } ( \mathbb { B } ^ { \circ } , { \mathcal { O } } ^ { \mathrm { a n } } ( \mathbb { L } ) ^ { \otimes k } ) ^ { \Gamma }
$$

in particular, the algebra of automorphic forms is finitely generated with positive degree generators.
Moreover, the isomorphism $G \cup \cong X ^ { \circ }$ extends to an isomorphism $G \backslash \backslash Y ^ { \mathrm { s s } } \cong { \hat { X } } ^ { \mathcal { H } }$ .

Proof.
The codimension assumption implies that any section of $G \backslash ( \eta ^ { \otimes k } | U )$ extends to $( G \backslash \backslash \eta ^ { \mathrm { s s } } ) ^ { \otimes k }$ . Since $H ^ { 0 } ( \mathbb { B } ^ { \circ } , { \mathcal { O } } ( \mathbb { L } ) ^ { \otimes k } ) ^ { \Gamma } = H ^ { 0 } ( X , { \mathcal { L } } ^ { \otimes k } )$ , the first assertion follows.
This induces an isomorphism between the underlying proj’s and so we obtain an isomorphism $G \backslash \backslash Y ^ { \mathrm { s s } } \cong \hat { X } ^ { \mathcal { H } }$ , as stated.
□

The identification demanded by the theorem will usually come from a period mapping.
In such cases the codimension hypotheses of are often fulfilled.
Let us now be more concrete.

7.1. Unitary lattices attached to directed graphs.
The only imaginary quadratic fields we will be concerned with are the cyclotomic ones, i.e., $\mathbb { Q } ( \zeta _ { 4 } )$ and $\mathbb { Q } ( \zeta _ { 6 } )$ . Their rings of integers are the Gaussian integers $\mathbb { Z } [ \zeta _ { 4 } ]$ and the Eisenstein integers $\mathbb { Z } [ \zeta _ { 6 } ]$ respectively.
It is then convenient to have the following notation at our disposal.
Let $D$ be a finite graph without loops and multiple edges and suppose all edges are directed, in other words $D$ is a finite set $I$ plus a collection of 2-element subsets of $I$ , each such subset being given as an ordered pair.
Then a Hermitian lattice $\mathbb { Z } [ \zeta _ { k } ] ^ { D }$ is defined for $k = 4 , 6$ as follows: $\mathbb { Z } [ \zeta _ { k } ] ^ { D }$ is the free $\mathbb { Z } [ \zeta _ { k } ]$ -module on the set of vertices $( r _ { i } ) _ { i \in I }$ of $D$ and a $\mathbb { Z } [ \zeta _ { k } ]$ -valued Hermitian form $\psi$ on this module defined by

$$
\psi ( r _ { i } , r _ { j } ) = { \left\{ \begin{array} { l l } { | 1 + \zeta _ { k } | ^ { 2 } = k / 2 } & { { \mathrm { ~ i f ~ } } j = i , } \\ { - 1 - \zeta _ { k } } & { { \mathrm { ~ i f ~ } } ( i , j ) { \mathrm { ~ i s ~ a ~ d i r e c t e d ~ e d g e } } , } \\ { 0 } & { { \mathrm { ~ i f ~ } } i { \mathrm { ~ a n d ~ } } j { \mathrm { ~ a r e ~ n o t ~ c o n n e c t e d } } . } \end{array} \right. }
$$

We denote the group of unitary transformations of $\mathbb { Z } [ \zeta _ { k } ] ^ { D }$ by $\mathrm { U } ( D , \zeta _ { k } )$ . This is an arithmetic group in the unitary group of the complexification of $\mathbb { Z } [ \zeta _ { k } ] ^ { D }$ . The elements in $\mathbb { Z } [ \zeta _ { k } ] ^ { D }$ of square norm $k / 2$ are called the roots of $\mathbb { Z } [ \zeta _ { k } ] ^ { D }$ .

If $D$ is a forest, then the isomorphism class $\mathbb { Z } [ \zeta _ { k } ] ^ { D }$ is independent of the way the edges are directed.
Usually it is only the isomorphism class that matters to us, and so in this case there is no need to specify these orientations.

7.2. The moduli space of quartic curves.
It is well-known fact that the anticanonical map of a Del Pezzo surface of degree two realizes that surface as a double cover of a projective plane ramified along a smooth quartic curve and that this identifies the coarse moduli space of Del Pezzo surfaces of degree two and that of smooth quartic curves.
The latter is also the the coarse moduli space of nonhyperelliptic genus three curves.
The invariant theory of quartic curves is classical (Hilbert-Mumford).
A period map taking values in a ball quotient has been constructed by Kond¯o [9]. Heckman recently observed that the relation between the two is covered by Theorem 7.1 (unpublished) and that the situation is very similar to the case of rational elliptic surfaces discussed below, it is only simpler.
We briefly review this work.

Let us first recall the invariant theory of quartic curves.
Fix a projective plane $P$ . Put $H _ { k } : = H ^ { \cup } ( P , { \mathcal { O } } _ { P } )$ , so that $P _ { k } : = \mathbb { P } ( H _ { k } )$ is the space of effective degree $k$ divisors on $P$ . We take $Y : = P _ { 4 }$ and $\eta : = \mathcal { O } _ { Y } ( 1 )$ and $G : = { \mathrm { S L } } ( H _ { 1 } )$ . Following [15] a point of $P _ { 4 }$ is $G$ -stable precisely if the corresponding divisor is reduced and has cusp singularities at worst (i.e., locally formally given by $y ^ { 2 } = x ^ { i }$ with $i = { 1 , 2 , 3 }$ ). It is semistable precisely when it is reduced and has tacnodes at worst (like $y ^ { 2 } = x ^ { 2 }$ with $1 \leq i \leq 4$ ) or is a double nonsingular conic.
A divisor has a minimal strictly semistable orbit precisely when it is sum of two reduced conics, at least one of which is nonsingular, which are tangent to each other at two points.
If $( x , y )$ are affine coordinates in $P$ , then these orbits are represented by the quartics $( x y - \lambda _ { 0 } ) ( x y - \lambda _ { 1 } )$ , with $[ \lambda _ { 0 } : \lambda _ { 1 } ] \in \mathbb { P } ^ { 1 }$ and so $G \backslash \backslash Y ^ { \mathrm { s s } } - G \backslash Y ^ { \mathrm { s t } }$ is a rational curve.
The nonsingular quartics are stable and define an open subset $Y ^ { \prime } \subset Y$ .

Kond¯o’s period map is defined as follows: given a smooth quartic curve $Q \subset P$ , he considers the $\mu _ { 4 }$ -cover of $P$ that is totally ramified along $Q$ . This is a smooth K3-surface of degree 4 that clearly double covers the degree two Del Pezzo surface attached to $P$ . For such surfaces there is a period map taking values in an arithmetic group quotient of a type IV domain of dimension 19. But the $\mu _ { 4 }$ -symmetry makes it actually map in a ball quotient of dimension 6. To be precise, consider the Hermitian lattice $\mathbb { Z } [ \zeta _ { 4 } ] ^ { E _ { 7 } }$ . Its signature is $( 6 , 1 )$ and so its complexification defines a 6-dimensional ball $\mathbb { B }$ . We form $X : = \mathrm { U } ( E _ { 7 } , \zeta _ { 4 } ) \backslash \mathbb { B }$ . It turns out that $\mathrm { U } ( E _ { 7 } , \zeta _ { 4 } )$ acts transitively on the set of cusps so that $X ^ { b b }$ is topologically the one-point compactification of $X$ . The roots (i.e., the vectors of square norm 2) come in two $\mathrm { U } ( E _ { 7 } , \zeta _ { 4 } )$ -equivalence classes: the one represented by the orthogonal complement of any generator $r _ { i }$ , denoted $\mathcal { H } _ { n }$ , and the rest, $\mathcal { H } _ { h }$ , represented by $r _ { i } - ( 1 + \zeta _ { 4 } ) r _ { j }$ , where $r _ { i } , r _ { j }$ are two generators with $\psi ( r _ { i } , r _ { j } ) = 1 + \zeta _ { 4 }$ . This defines a hypersurface $D$ in $X$ with two irreducible components $D _ { n }$ and $D _ { h }$ respectively.
The hyperplane sections of $\mathbb { B }$ of type $\mathcal { H } _ { h }$ are disjoint and so $D _ { h }$ has no self-intersection.
Kond¯o’s theorem states that the period map defines isomorphisms

$$
G \backslash Y ^ { \prime } \cong X - D , \quad G \backslash Y ^ { \mathrm { s t } } \cong X - D _ { h } .
$$

The last isomorphism is covered by an isomorphism of orbiline bundles $G \backslash \backslash \eta $ $\mathcal { L } | X - D _ { h }$ and so Theorem 7.1 applies with $U = Y ^ { \mathrm { s s } }$ : we find that the period map extends to an isomorphism

$$
G \backslash \backslash Y ^ { \mathrm { s s } } \cong \hat { X } ^ { \mathcal { H } _ { h } } .
$$

7.3. A nine dimensional ball quotient.
We begin with a Deligne-Mostow example which involves work of Allcock [1]. Fix a projective line $P$ , put $H _ { k } : =$ $H ^ { \cup } ( P , { \mathcal { O } } _ { P } ( k ) )$ , and identify $P _ { k } : = \mathbb { P } ( H _ { k } )$ with the $k$ -fold symmetric product of $P$ , or what amounts to the same, the linear system of effective degree $k$ divisors on $P$ . The group $G : = { \mathrm { S L } } ( H _ { 1 } )$ acts on the pair $( P _ { k } , \mathcal { O } _ { P _ { k } } ( 1 ) )$ . Following Hilbert, a degree $k$ divisor is stable resp.
semistable if and only if all its multiplicities are $< k / 2$ resp.
$\leq k / 2$ . We only have a strictly semistable orbit if $k$ is even $\geq 4$ and in that case there is a unique minimal such orbit: the divisors with two distinct points of multiplicity $k / 2$ . The nonreduced divisors define a discriminant hypersurface in $P _ { k }$ , whose complement we shall denote by $P _ { k } ^ { \prime }$ .

Now take $k = 1 2$ . Given a reduced degree 12 divisor $D$ on $P$ we can form the $\mu _ { 6 }$ -cover $C  P$ that is totally ramified over $D$ . The Jacobian $J ( C )$ of $C$ comes with an action of the covering group $\mu _ { 6 }$ and the part where that group acts with a primitive character defines a quotient abelian variety of dimension 10. The isomorphism type of this quotient abelian variety is naturally given by a point in a ball quotient.
To be precise, if $A _ { 1 0 }$ is the string with 10 nodes, then $\mathbb { Z } [ \zeta _ { 6 } ] ^ { A _ { 1 0 } }$ is nondegenerate of signature $( 9 , 1 )$ and so defines a ball $\mathbb { B }$ of complex dimension 9. The group $\mathrm { U } ( A _ { 1 0 } , \zeta _ { 6 } )$ is arithmetic and so we may form

$$
X : = \operatorname { U } ( A _ { 1 0 } , \zeta _ { 6 } ) \backslash \mathbb { B } .
$$

It acts transitively on the cusps so that the Baily-Borel compactification $X ^ { b b }$ of $X$ is a one-point compactification.
The hyperplanes perpendicular to a root makes up an arrangement that is arithmetically defined.
Since they are transivily permuted by $\mathrm { U } ( A _ { 1 0 } , \zeta _ { 6 } )$ , they define an irreducible hypersurface $D$ in $X$ . A theorem of DeligneMostow [4] implies that $X - D$ parametrizes the isomorphism types of the quotients of the Jacobians that we encounter in the situation described above and that the ‘period map’

$$
G \backslash P _ { 1 2 } ^ { \prime }  X - D
$$

is an isomorphism.
It also follows from their work (see also [7]) that this period isomorphism extends to isomorphisms

$$
G \backslash P _ { 1 2 } ^ { \mathrm { s t } } \cong X , \quad G \backslash \backslash P _ { 1 2 } ^ { \mathrm { s s } } \cong X ^ { b b } ,
$$

(with the unique minimal strictly semistable orbit corresponding to the unique cusp) and that the latter identifies $\mathcal { L } ^ { \otimes 1 2 }$ with $\Gamma \backslash \mathcal { O } _ { P _ { 1 2 } ^ { \mathrm { s s } } } ( 1 )$ . (In this situation $\Gamma$ is not neat and so $\mathcal { L }$ is merely an orbiline bundle on $X ^ { b b }$ .)

We can also think of $G \backslash P _ { 1 2 } ^ { \prime }$ as the moduli space of hyperelliptic curves of genus 5 or as the moduli space of 12-pointed smooth rational curves (with the 12 points not numbered).
For either interpretation this moduli space has a Deligne-Mumford compactification and these two coincide as varieties.
It can be verified that the Deligne-Mumford compactification is just the minimal normal crossings blowup in the sense of Subsection 2.3 of $D$ in $X ^ { b b }$ .

7.4. Miranda’s moduli space of rational elliptic surfaces.
In this discussion a rational elliptic surface is always assumed to have a section.
The automorphisms of such a surface permute the sections transivitively, so when we are concerned with isomorphism classes, there is no need to single out a specific section.
Contraction of a section yields a Del Pezzo surface of degree one and vice versa, so the moduli space of rational elliptic surfaces is the same as the moduli space of degree one Del Pezzo surfaces.
A rational elliptic surface can always be represented in Weierstrass form: $y ^ { 2 } = x ^ { 3 } + 3 f _ { 0 } ( t ) x + 2 f _ { 1 } ( t )$ , where $x , y , t$ are the affine coordinates of a $\mathbb { P } ^ { 2 }$ - bundle over $\mathbb { P } ^ { 1 }$ and $f _ { 0 }$ and $f _ { 1 }$ are rational functions of degree 4 and 6 repectively.
(We normalized the coefficients as to have the discriminant of the surface take the simple form $f _ { 0 } ^ { 3 } + f _ { 1 } ^ { 2 }$ .) This is Miranda’s point of departure [14] for the construction of a compactification by means of geometric invariant theory of this moduli space.
With the notation of the previous subsection, let $Y$ be the ‘orbiprojective’ space obtained as the orbit space of $H _ { 4 } \oplus H _ { 6 } - \{ ( 0 , 0 ) \}$ relative to the action of the center $\mathbb { C } ^ { \times } \subset \mathrm { G L } ( H _ { 1 } )$ . It comes with a natural ample orbifold line bundle $\eta$ over $Y$ endowed with an action of $G = { \mathrm { S L } } ( H _ { 1 } )$ . It has the property that the pull-back of $\mathcal { O } _ { P _ { 1 2 } }$ under the equivariant ‘discriminant morphism’

$$
\Delta : Y  P _ { 1 2 } , \quad ( f _ { 0 } , f _ { 1 } ) \mapsto f _ { 0 } ^ { 3 } + f _ { 1 } ^ { 2 }
$$

is equivariantly isomorphic to $\eta ^ { \otimes 6 }$ . The above morphism is finite and birational with image a hypersurface.
The preimage $\Delta ^ { - 1 } ( P _ { 1 2 } ^ { \prime } )$ , which clearly parametrizes the rational elliptic fibrations over $P$ with reduced discriminant, maps isomorphically to its image in $P _ { 1 2 }$ and is contained in the $Y ^ { \mathrm { s t } }$ . We denote its $G$ -orbit space by $\mathcal { M }$ . But a stable point of $Y$ need not have a stable image in $P _ { 1 2 }$ : Miranda shows that the $G$ -orbit space of $Y ^ { \mathrm { s t } } \Omega \Delta ^ { - 1 } ( P _ { 1 2 } ^ { \mathrm { s t } } )$ , denoted here by $\mathcal { M }$ , parametrizes the Mirandastable rational elliptic surfaces with reduced fibers and stable discriminant, in other words, the allowed singular fibers have Kodaira type $I _ { k }$ with $k < 6$ , $I I$ , $I I I$ or $I V$ , whereas the difference $G \backslash Y ^ { \mathrm { s t } } - \mathcal { M }$ parametrizes rational elliptic surfaces with an $I _ { k }$ -fiber with $6 \leq k \leq 9$ . The minimal orbits in $Y ^ { \mathrm { s s } } - Y ^ { \mathrm { s t } }$ parametrize rational elliptic surfaces with two $I _ { 0 } ^ { * }$ -fibers or a $I _ { 4 } ^ { * }$ -fiber (they make up a rational curve).
So the projective variety $\mathcal { M } ^ { M } : = G \backslash \backslash Y ^ { \mathrm { s s } }$ still parametrizes distinct isomorphism classes of elliptic surfaces.
We regard this variety as a projective completion of $\mathcal { M }$ and call it the Miranda compactification.
The boundary $\mathcal { M } ^ { M } - \mathcal { M }$ is of codimension 5 in $\mathcal { M } ^ { M }$ and $\mathcal { M } ^ { M } - \mathcal { M }$ is a hypersurface in $\mathcal { M } ^ { M }$ .

7.5. A period map for rational elliptic surfaces.
Assigning to a rational elliptic fibration with reduced discriminant its discriminant defines a morphism

$$
\mathcal { M } = G \backslash Y ^ { \prime }  G \backslash P _ { 1 2 } ^ { \prime }  X - D .
$$

and the pull-back of $\mathcal { L } ^ { \otimes 1 2 }$ can be identified with $G \backslash \eta ^ { \otimes 6 }$ . It is proved by HeckmanLooijenga [7] that this morphism is a closed embedding with image a deleted hyperball quotient.
To be precise, choose a vector in $\mathbb { Z } [ \zeta _ { 6 } ] ^ { A _ { 1 0 } }$ of square norm 6 (for instance, the sum of two perpendicular roots) and let $\Lambda _ { o } \subset \mathbb { Z } [ \zeta _ { 6 } ] ^ { A _ { 1 0 } }$ be its orthogonal complement.
It is shown in $o p$ . cit.
that all such vectors are $\mathrm { U } ( A _ { 1 0 } , \zeta _ { 6 } )$ -equivalent and for that reason the choice of this vector is immaterial for what follows.
The $\mathrm { U } ( A _ { 1 0 } , \zeta _ { 6 } )$ -stabilizer of $\Lambda _ { o }$ acts on $\Lambda _ { o }$ through its full unitary group, which we denote by $\Gamma _ { o }$ . The sublattice $\Lambda _ { o }$ defines a hyperball $\mathbb { B } _ { o } \subset \mathbb { B }$ , a ball quotient $X _ { o } : = \mathbb { B } _ { o , \Gamma _ { o } }$ and a natural map $p : X _ { o } \to X$ . The restriction of $\mathcal { H }$ to $\mathbb { B } _ { o }$ is an arrangement on $\mathbb { B } _ { o }$ that is arithmetically defined and the corresponding hypersurface $D _ { o }$ on $X _ { o }$ is just $p ^ { - 1 } ( D )$ . It is proved in [7] that the period map defines an isomorphism

$$
\mathcal { M } = G \backslash Y ^ { \prime } \cong X _ { o } - D _ { o } .
$$

It is easily seen to extend to a morphism ${ \mathcal { M } } \to X _ { o }$ . This extension is not surjective.
This is related to the fact that $D _ { o }$ has four irreducible components, or equivalently, that the restriction of the arrangement $\mathcal { H }$ to $\mathbb { C } \otimes _ { \mathcal { O } } \Lambda _ { o }$ is not a single $\Gamma _ { o }$ -equivalence class, but decomposes into four such classes.
These four classes are distinguished by a numerical invariant (for the definition of which we refer to op.
cit.)
that takes the values $6 , 9 , 1 5 , 1 8$ . So $\mathcal { H } | \mathbb { C } \otimes \mathcal { O } \Lambda _ { o }$ is the disjoint union of the $\Gamma _ { o }$ -equivalence classes $\mathcal { H } ( d )$ with $d$ running over these four numbers and $\mathcal { H } ( d )$ defines an irreducible hypersurface $D ( d ) \subset X _ { o }$ . The image of the period map is the complement of $D ( 6 ) \cup D ( 9 )$ . In fact, we have an isomorphism

$$
\mathcal { M } \cong X _ { o } - ( D ( 6 ) \cup D ( 9 ) )
$$

with the generic point of $D ( 1 8 )$ resp.
$D ( 1 2 )$ describing semistable elliptic fibrations with a $I _ { 2 }$ resp.
$I I$ -fiber.
This isomorphism is covered by an isomorphism of orbifold line bundles: $G \backslash \eta ^ { \otimes 6 }$ is isomorphic to the pull-back of the $\mathcal { L } ^ { 1 2 }$ . It is shown in [7] that any nonempty intersection of hyperplane sections of $\mathbb { B } _ { o }$ taken from $\mathcal { H } ( 6 ) \cup \mathcal { H } ( 9 )$ has dimension $\geq 5$ . Since $\mathcal { M } ^ { M } - \mathcal { M }$ is of codimension 5 on $\mathcal { M } ^ { M }$ , theorem 7.1 applies with $U : = Y ^ { \mathrm { s t } } \cap \Delta ^ { - 1 } ( P _ { 1 2 } ^ { \mathrm { s t } } )$ and we find:

Corolspace $\mathcal { M } ^ { M }$ 7.2. The period map extends to an isomorphism ofof rational elliptic surfaces onto the modification $\hat { X } _ { o } ^ { \mathcal { H } ( 6 ) \cup \mathcal { H } ( 9 ) }$ moof $X _ { o } ^ { b b }$ defined by the arrangement $\mathcal { H } ( 6 ) \cup \mathcal { H } ( 9 )$ .

7.6. The moduli spaces of cubic surfaces and cubic threefolds.
The previous two examples describe the moduli spaces of Del Pezzo surfaces of degree one and two as a ball quotient and express its GIT compactification as a modified BailyBorel compactification of the ball quotient.
This can also be done for Del Pezzo surfaces of degree three, that is for smooth cubic surfaces.
Allcock, Carlson and Toledo gave in [3] a 4-ball quotient description of this moduli space, by assiging to a smooth cubic surface $S \subset \mathbb { P } ^ { 3 }$ first the $\mu _ { 3 }$ -cover $K  \mathbb { P } ^ { 3 }$ totally ramified over $S$ and then the intermediate Jacobian of $K$ with its $\mu _ { 3 }$ -action.
But in this case they find that the GIT compactification coincides with the Baily-Borel compactification (one might say that the relevant arrangement is empty).
However, they recently extended this to the moduli space of smooth cubic threefolds: the GIT compactification has been recently given by Allcock [2], whereas Allcock, Carlson and Toledo found a 10-ball quotient description of the moduli space (yet unpublished).
It comes naturally with an arrangement and it seems that Theorem 7.1 applies here, too.

# References

[1] D. Allcock: The Leech Lattice and Complex Hyperbolic Reflections, Invent.
Math.
140 (2000), 283–301.\
[2] D. Allcock: The moduli space of cubic threefolds, to appear in J. Alg.
Geom., also available at http://www.math.harvard.edu/ allcock/research/3foldgit.ps.\
[3] D. Allcock, J.A. Carlson, D. Toledo: The complex hyperbolic geometry for moduli of cubic surfaces, 55 pp., available at math.AG/0007048, to appear in J. Alg.
Geom., see also A complex hyperbolic structure for moduli of cubic surfaces, C. R. Acad.
Sci.
Paris, t. 326, S´erie I (1998), 49–54.\
[4] P. Deligne, G.D. Mostow: Monodromy of hypergeometric functions and non-lattice integral monodromy, Inst.
Hautes Etudes Sci.
Publ.
Math.
63 (1986), 58–89. ´\
[5] A. Grothendieck: El´ements de g´eom´etrie alg´ebrique.
II. ´ Etude globale ´el´ementaire de quelques ´ classes de morphismes.
Inst.
Hautes Etudes Sci.
Publ.
Math.
8 (1961), 222 pp. ´\
[6] R. Hartshorne: Algebraic Geometry, Graduate Texts in Mathematics, 52, Springer-Verlag, New York-Heidelberg (1977).\
[7] G. Heckman, E. Looijenga: The moduli space of rational elliptic surfaces, 47 pp., to appear in the Proceedings of the Conference Algebraic Geometry 2000 (Azumino), also available at math.AG/0010020.\
[8] Yi Hu: A Compactification of Open Varieties, 21 pp., available at math.AG/9910181.\
[9] S. Kond¯o: A complex hyperbolic structure on the moduli space of curves of genus three, J. reine u. angew.
Math.
525 (2000), 219–232.\
[10] E. Looijenga: Moduli spaces of marked Del Pezzo surfaces, Appendix to a paper by I. Naruki.
Proc.
London Math.
Soc.
45 (1982), 24–30.\
[11] E. Looijenga: New compactifications of locally symmetric varieties, in: Proceedings of the 1984 Conference in Algebraic Geometry, 341–364, J. Carrell, A.V. Geramita, P. Russell eds.
CMS Conference Proceedings, vol. 6, Amer.
Math.
Soc.
Providence RI (1984).\
[12] E. Looijenga: Semi-toric partial compactifications I, Report 8520 (1985), 72 pp., Catholic University Nijmegen.\
[13] E. Looijenga: Affine Artin groups and the fundamental groups of some moduli spaces, 41 pp., available at math.AG/9801117.\
[14] R. Miranda: The Moduli of Weierstrass Fibrations over $\mathbb { P } ^ { 1 }$ , Math.
Ann.
255 (1981), 379–394.\
[15] D. Mumford, J. Fogarty, F. Kirwan: Geometric Invariant Theory, 3rd ed., Erg.
der Math.
u. i. Grenzgebiete 34, Springer-Verlag Berlin etc. 1994.\
[16] H. Sterk: Compactifications of the period space of Enriques surfaces.
I, II, Math.
Z. 207 (1991), 1–36 and Math.
Z. 220 (1995), 427–444.\
[17] A. Ulyanov: Polydiagonal compactification of configuration spaces, 28 pp., available at math.AG/9904049. Faculteit Wiskunde en Informatica, Universiteit Utrecht, Postbus 80.010, NL-3508\
TA Utrecht, Nederland E-mail address: mailto:looijeng@math.uu.nl
