---
title: Complete moduli spaces of branchvarieties
authors:
- Valery Alexeev
- Allen Knutson
year: 2010
bibkey: Ale02
tags:
- paper
- extraction
abstract: |
  The space of subvarieties of $\mathbb { P } ^ { { n } }$ with a fixed Hilbert polynomial is not complete.
  Grothendieck defined a completion by relaxing “variety” to “scheme”, giving the complete Hilbert scheme of subschemes of $\mathbb { P } ^ { { \mathrm { n } } }$ with fixed Hilbert polynomial.
  
  We instead relax “sub” to “branch”, where a branchvariety of $\mathbb { P } ^ { { \mathrm { n } } }$ is defined to be a reduced (though possibly reducible) scheme with a finite morphism to $\mathbb { P } ^ { { \mathrm n } }$ .
  Our main theorems are that the moduli stack of branchvarieties of $\mathbb { P } ^ { { n } }$ with fixed Hilbert polynomial and total degrees of i-dimensional components is a proper (complete and separated) Artin stack with finite stabilizer, and has a coarse moduli space which is a proper algebraic space.
  
  Families of branchvarieties have many more locally constant invariants than families of subschemes; for example, the number of connected components is a new invariant.
  In characteristic 0, one can extend this count to associate a $\mathbb { Z }$ -labeled rooted forest to any branchvariety.
---

# COMPLETE MODULI SPACES OF BRANCHVARIETIES

VALERY ALEXEEV AND ALLEN KNUTSON

ABSTRACT. The space of subvarieties of $\mathbb { P } ^ { { n } }$ with a fixed Hilbert polynomial is not complete.
Grothendieck defined a completion by relaxing “variety” to “scheme”, giving the complete Hilbert scheme of subschemes of $\mathbb { P } ^ { { \mathrm { n } } }$ with fixed Hilbert polynomial.

We instead relax “sub” to “branch”, where a branchvariety of $\mathbb { P } ^ { { \mathrm { n } } }$ is defined to be a reduced (though possibly reducible) scheme with a finite morphism to $\mathbb { P } ^ { { \mathrm n } }$ . Our main theorems are that the moduli stack of branchvarieties of $\mathbb { P } ^ { { n } }$ with fixed Hilbert polynomial and total degrees of i-dimensional components is a proper (complete and separated) Artin stack with finite stabilizer, and has a coarse moduli space which is a proper algebraic space.

Families of branchvarieties have many more locally constant invariants than families of subschemes; for example, the number of connected components is a new invariant.
In characteristic 0, one can extend this count to associate a $\mathbb { Z }$ -labeled rooted forest to any branchvariety.

# CONTENTS

0. Introduction 25
1. Boundedness
2. One-parameter families 8
3. Construction of the moduli space 11
4. Examples 14\
   4.1. Further elementary examples 14\
   4.2. Stable toric varieties 16\
   4.3. Balanced normal cones 17\
   4.4. Chiriv\`ı’s degeneration of flag manifolds as a limit of branchvarieties 17
5. Line bundles on Branch 18
6. K-classes of degenerations 19
7. The forest of a branchvariety 20
8. U-invariant branchvarieties 23\
   8.1. Spaces of cubic curves 25
9. Relations to other moduli spaces 25\
   9.1. Branch vs. Hilbert 26\
   9.2. Branch vs. Chow 27\
   9.3. Branch vs. stable maps 27
10. Other versions 27\
    10.1. Multigraded Branch 27\
    10.2. Complex-analytic Branch 27\
    References 27

Date: July 31, 2006.

# 0. INTRODUCTION

Consider a family of reduced plane conics $\{ \boldsymbol { x } _ { 1 } ^ { 2 } = \mathbf { t } \cdot \boldsymbol { x } _ { 0 } \boldsymbol { x } _ { 2 } \}$ over $\mathbb { A } _ { \mathrm { t } } ^ { 1 } \setminus { 0 }$ with coordinate t. By using the same equation, this family can be completed to a flat family $Z \subset \mathbb { P } ^ { 2 } \times \mathbb { A } _ { \mathrm { t } } ^ { 1 }$ projective over $\mathbb { A } _ { \mathrm { t } } ^ { 1 }$ ; the central fiber is the double line ${ \cal Z } _ { 0 } = \{ x _ { 1 } ^ { 2 } = 0 \} ,$ a nonreduced subscheme of $\mathbb { P } ^ { 2 }$ . On the other hand, after the finite ramified base change $\mathrm { t } = s ^ { 2 }$ and simple substitution $\begin{array} { r } { \mathbf { x } _ { 1 } ^ { \prime } = \mathbf { x } _ { 1 } / s , } \end{array}$ this family can be completed to a flat family $X = \{ ( \mathsf { x } _ { 1 } ^ { \prime } ) ^ { 2 } = \mathsf { x } _ { 0 } \mathsf { \bar { x } } _ { 2 } \}$ with a finite morphism f : $\mathsf { X } \to \mathbb { P } ^ { 2 } \overset { \cdot } { \times } \mathbb { A } _ { s } ^ { 1 } ,$ , rather than an inclusion.
The central fiber $X _ { 0 }$ is a reduced $\mathbb { P } ^ { 1 }$ , and $\dot { \mathsf { f } } _ { 0 } : \mathsf { X } _ { 0 } \to \mathbb { P } ^ { 2 }$ is a double cover of the line $\{ x _ { 1 } = 0 \} = ( Z _ { 0 } ) _ { \mathrm { r e d } }$ .

How general is this phenomenon?
We pose two forms of this question:

(1) Does every one-parameter flat family of reduced subschemes of $\mathbb { P } ^ { { \mathfrak { n } } }$ have a welldefined flat completion whose special fiber is a reduced scheme mapping finitely to $\mathbb { P } ^ { { \mathrm { n } } _ { ? } }$ (Possibly after base change, like s for t in the above example.)\
(2) Is there a universal substitute for the Hilbert scheme, some other moduli space for reduced schemes X carrying finite morphisms $\smash {  { \mathrm { \ X } } \to  { \mathbb { P } } ^ { \mathrm { n } _ { 2 } } }$ (Such a moduli space would necessarily be coarse since Aut(f) may be nontrivial; indeed it is $\mathbb { Z } _ { 2 }$ for the double cover $\mathsf { f } _ { 0 }$ above.)

In this paper we answer both of these positively, generalizing two known situations:

(1) In [Ale02, AB05] there were constructed the moduli spaces of stable toric and spherical varieties over Y. This can be interpreted as answering both questions above in the multigraded multiplicity-free case.
The one-parameter limits were constructed by making a base change $\mathbf { t } = s ^ { \mathrm { n } }$ and normalizing, which in the multiplicityfree case amounts to saturating a semigroup.
These moduli spaces are projective, and they should be considered to be the substitute for the toric Hilbert scheme of [PS02], the multigraded multiplicity-free Hilbert scheme.

(2) For every closed subscheme X of a reduced Noetherian scheme Y, there is a flat degeneration of Y to the normal cone $\operatorname { C } _ { X } Y ,$ , which is usually nonreduced.
In [Knu05] there is presented an alternative degeneration of Y to a “balanced” normal cone $\overline { { C } } _ { X } \Upsilon$ which is reduced, and comes with a finite morphism $\overline { { { \mathsf { C } } } } _ { \mathsf { X } } \mathsf { Y } \to \mathsf { C } _ { \mathsf { X } } \mathsf { Y }$ . The schemes $\Chi , \sf Y$ are otherwise general, and there is no multiplicity-free restriction or group action.

The need for the base change, and the loosening of “inclusion of a subscheme” to “finite morphism”, are already both illustrated by the simple example $\mathsf { f } : \mathbb { A } _ { \mathsf { u } } ^ { 1 } \to \mathbb { A } _ { \mathsf { t } } ^ { 1 } , \mathsf { t } = \mathsf { u } ^ { 2 }$ . The general fiber of this flat family is two (reduced) points, which cannot be disentangled because the source is irreducible.
Pulling back this family along the base change $s ^ { 2 } = \mathrm { t } ,$ we get another flat family $\mathsf { f } ^ { \prime } : \mathbb { A } _ { s = \mathrm { u } } ^ { 1 } \cup _ { 0 } \mathbb { A } _ { s = - \mathrm { u } } ^ { \breve { 1 } } \to \mathbb { A } _ { s } ^ { 1 }$ with the same central fiber (a double point), where the total space of the family is given by $s ^ { 2 } = \mathrm { u } ^ { 2 }$ . Then we normalize to pull the two components apart; now the central fiber too is two reduced points.

A similar normalization step will introduce finite morphisms in general, taking us out of the class of subvarieties (i.e. injective morphisms of reduced schemes).
We now spell out what class will replace them.

Definition 0.1. Let $\mathsf { Y } \subset \mathbb { P } ^ { \mathfrak { n } }$ be a projective scheme over a field $\boldsymbol { \mathrm { k } }$ . A branchvariety of $\mathbf { Y }$ is a variety $\boldsymbol { x }$ (by which we mean a scheme of finite type over $\boldsymbol { \mathrm { k } }$ such that $\overline { { \boldsymbol { x } } } = \dot { \boldsymbol { x } } \otimes _ { \mathsf { k } } \bar { \mathsf { k } }$ is reduced, so $a$ forteriori, $\boldsymbol { x }$ is reduced) equipped with a finite (hence proper) morphism $\mathsf { f } : \mathsf { X } \to \mathsf { Y }$ .

The Hilbert polynomial of a branchvariety is $\begin{array} { r } { \mathtt { h ( d ) } : = \chi ( X , \mathtt { L ^ { d } ) } , } \end{array}$ where $\mathrm { L } = \mathsf { f } ^ { \ast } \mathcal { O } _ { \mathbb { P } ^ { \mathrm { n } } } ( 1 )$ . One has di $\mathrm { n } \mathsf { H } ^ { \mathrm { o } } ( \mathsf { X } , \mathrm { L } ^ { \mathrm { d } } ) = \mathsf { h } ( \mathrm { d } )$ for ${ \mathrm { ~ d ~ } } \gg 0$ . Writing the leading term of $\boldsymbol { \mathrm { h } } ( \mathrm { d } )$ as $\left( \mathbf { c } / \mathsf { D } ! \right) \mathbf { d } ^ { \mathrm { D } } ,$ , the coefficient c is the degree $\deg X$ of the branchvariety.

We could even assume without much loss of generality that $\boldsymbol { x }$ is connected, since by Lemma 7.1 to come (and in contrast to families of subschemes) the number of connected components is locally constant in families of branchvarieties.
Then $\boldsymbol { x }$ is indeed what is commonly called a “variety”, albeit not irreducible, much as a “stable curve” is not irreducible in general.
We also note that one can define in the same way a branchvariety X of an arbitrary, not necessarily projective scheme Y, though giving up the notion of $\times ^ { \prime } \mathrm { s }$ Hilbert polynomial and degree.

Let us fix a Noetherian base scheme C (for example the spectrum of $\mathbb { Z }$ or of a field of arbitrary characteristic), and a projective scheme $\mathsf { Y } \subset \mathbb { P } _ { \mathsf { C } } ^ { \mathsf { n } }$ flat over C. All our schemes will be assumed to be locally Noetherian (but see Remark 0.6).

# Definition 0.2. The functor of subschemes or Hilbert functor

$$
\mathrm { H i l b } _ { \mathrm { h , \vec { Y } } } \colon ( C \mathrm { - s c h e m e s } ) \to ( \mathrm { S e t s } ) ^ { \mathrm { o p p } }
$$

is defined by associating to each scheme S the set $\mathrm { H i l b } _ { \mathsf { h } , \mathsf { Y } } ( S )$ of proper subschemes $Z \subset$ $\mathsf { Y } _ { \mathsf { S } } = \mathsf { Y } \times _ { \mathsf { C } } { \mathsf { S } }$ which are flat over S.

Because of the importance of flatness in this and the next definition, in this paper we will only be interested in flat families, and will always use the term “family” to mean “flat family”.

One fixes the Hilbert polynomial in the above definition in order that the functor be representable by a scheme of finite type.
(Otherwise one gets a disjoint union of schemes of finite type, one for each possible Hilbert polynomial.)
In the corresponding definition for branchvarieties, fixing the Hilbert polynomial is not enough to obtain a finite-type family, as Example 1.1 will show.
One easy workaround is to look at only equidimensional branchvarieties; instead, to avoid loss of generality, we measure some additional parameters beyond h. For a branchvariety X, let

$$
\int \{ \mathrm { t h e ~ i - d i m e n s i o n a l ~ i r r e d u c i b l e ~ c o m p o n e n t s ~ o f ~ } \mathbb { X } \} , \qquad \mathsf { b } _ { \mathrm { i } } ( \boldsymbol { X } ) : = \deg \boldsymbol { X } ^ { \dim i } \setminus \mathbb { Z } .
$$

where $\chi ^ { \mathrm { { d i m } \ i } }$ is considered as a branchvariety in a natural way and hence has a degree.
By Lemma 1.3 the degree sequence $\boldsymbol { \mathsf { b } } = \left( \boldsymbol { \mathsf { b } } _ { 0 } , \ldots , \boldsymbol { \mathsf { b } } _ { \dim x } \right)$ of nonnegative integers is locally constant in families of branchvarieties.

# Definition 0.3. The functor of branchvarieties

$$
{ \mathrm { B r a n c h } } _ { \mathrm { h } , \Upsilon } ^ { \mathrm { b } } : ( { \mathrm { C } } \mathrm { - s c h e m e s } ) \to ( { \mathrm { S e t s } } ) ^ { \mathrm { o p p } }
$$

is defined by associating to each scheme S, the set $\mathrm { B r a n c h } _ { \mathrm { h } , \Upsilon } ( S )$ of proper families f : ${ \sf X }  { \sf Y } _ { \sf S } = { \sf Y } \times _ { \sf C } { \sf S }$ such that $x  s$ is flat and every fiber $\boldsymbol { \mathfrak { f } } _ { s } : \boldsymbol { X } _ { s } \to \bar { \mathsf { Y } } _ { s } = \mathsf { Y } \times _ { C } \boldsymbol { \mathbf { k } } ( s )$ is a branchvariety of $\Upsilon _ { s }$ with Hilbert polynomial h and degree sequence $\boldsymbol { \mathrm { b } }$ , up to isomorphism.

We avoid the set-theoretic difficulties in this definition (the “set” of branchvarieties may be too big to actually be a set) in a standard way, by fixing a universe, or by demanding that they are subschemes of some fixed $\mathbb { P } ^ { \infty }$ . We prove in Theorem 1.7 that $\infty$ can actually be lowered to a finite bound $\mathrm { d } _ { 0 } ( \mathsf { h } , \mathsf { b } )$ .

We define the stack in groupoids Branch $^ { \mathrm { ~ b ~ } } _ { \mathrm { ~ h , Y } }$ by associating to each scheme S a category $B r a n c h _ { \mathrm { h , Y } } ^ { \mathrm { b } } ( S )$ whose objects are the families f : $X  Y _ { S }$ as above, and morphisms are isomorphisms intertwining the structure morphisms f.

Theorem 0.4. The stack in groupoids Branch $^ { \mathrm { { b } } } _ { \cdot \mathrm { { h , Y } } }$ is an algebraic Artin stack with a finite stabilizer.\
It has a coarse moduli space $\mathrm { B r a n c h } _ { \mathrm { h , Y } } ^ { \mathrm { b } }$ which is a proper algebraic space.

In particular, $\mathrm { B r a n c h } _ { \mathrm { h , Y } } ^ { \mathrm { b } }$ has finitely many connected components.
It is not connected for most $( \mathsf { h } , \mathsf { b } , \mathsf { Y } )$ , since different connected components may often be distinguished by their associated (labeled rooted) “forests”, an invariant we develop in Section 7. (This is in contrast with the Hilbert scheme, which is connected for each h.) The forest can be defined when the characteristic of our field is 0 or larger than any degree $\mathsf { b } _ { \mathrm { i } } ( \mathsf { X } ) .$ , and is a refinement of both the degree sequence and the Hilbert polynomial.

The characterization of the set of connected components of $\mathrm { B r a n c h } _ { \mathrm { h , Y } } ^ { \mathrm { b } }$ remains open, though we have one tiny result in this direction in Theorem 9.3.

The proof of Theorem 0.4 uses the general procedure which was developed for constructing compactifications of moduli spaces of surfaces of general type (moduli of stable surfaces and pairs), see e.g. [Kol90, Ale96], and it goes as follows.

In Section 2 we establish the most important property of our moduli functor, properness: every one-parameter family of branchvarieties has at most one limit, and the limit always exists after a finite ramified base change.

In Section 1 we prove that the family of branchvarieties with fixed numerical invariants is bounded, i.e. there exists a universal constant $\mathsf { N }$ such that $L ^ { \mathsf { N } }$ is very ample for each such branchvariety and embeds it into a fixed projective space $\mathbb { P } ^ { \mathrm { { D } } }$ . Once this is established, the branchvarieties of Y can be parametrized by a locally closed subscheme V of the Hilbert scheme of $\mathsf { Y } \times \mathbb { P } ^ { \mathsf { D } }$ , up to a choice of embedding $\boldsymbol { x } \hookrightarrow \mathbb { P } ^ { \mathrm { { D } } }$ . The moduli space can then be constructed by taking the quotient $\mathrm { V } / \mathrm { P G L } _ { \mathrm { D } + 1 }$ . We do this in Section 3.

For the quotient, we do not use Geometric Invariant Theory, which would have involved a delicate analysis of stability.
Instead, we use a well-known observation that a quotient by a proper group action always exists as an algebraic space.
Properness of the group action follows from separatedness of the moduli functor and finiteness of the automorphism groups.
Since the moduli functor of branchvarieties is also proper, the moduli space is a proper algebraic space.

In the case of stable surfaces of general type, there is one additional step one can add to this procedure: by using [Kol90] one proves that the thus obtained moduli space is projective, and in particular a scheme, because some naturally defined invertible sheaves on it are ample.
In our case this part is missing.
As we show in Section 5, the basic invertible sheaves that come with Branch are, curiously, not ample.
However, it is possible that some of their linear combinations are ample.

Remark 0.5. We would like to note that Branch does not suffer from the limitations afflicting the Chow variety (and the similar Barlet space in complex-analytic geometry) which parametrizes cycles of a fixed degree in Y. In the Chow theory, there is no notion of an infinitesimal family of algebraic cycles, say over Spec $\mathbb { C } [ \epsilon ] / ( \epsilon ^ { 2 } )$ ; the best one can do is to consider families of algebraic cycles over a reduced and seminormal base.
In this sense, the Chow variety should be considered to be a “parameter space” rather than a “moduli space”.
See [Kol96, I.3-4] for a comprehensive rigorous treatment.

Remark 0.6. The Hilbert scheme has been constructed in the more general situation of families over non-Noetherian schemes.
In this case, the Hilbert functor is defined by requiring that the sheaves $( \mathtt { p } _ { 2 } ) _ { * } \mathcal { O } _ { Z } ( \mathtt { d } )$ are locally free of rank $\boldsymbol { \mathrm { h } } ( \mathrm { d } )$ , in a neighborhood of every point $s \in S$ and for $\mathrm { d } \geq \mathrm { d } _ { 0 } ( s )$ . This is equivalent to flatness in the Noetherian case since a finitely generated module over a Noetherian ring is flat iff it is locally free.

Similarly, we can define a family of branchvarieties over a general scheme S by requiring that the sheaves $\pi _ { * } \mathrm { L } ^ { \mathrm { d } }$ are locally free of rank $\boldsymbol { \mathrm { h } } ( \mathrm { d } )$ . The moduli space of branchvarieties is constructed in Theorem 0.4 by taking a quotient of a Hilbert scheme, which is already quasiprojective over C. Then, in order to use the result from [KM97] concerning this quotient, we only need to assume that C is locally Noetherian.

Remark 0.7. Since the moment this paper was widely circulated, two extensions have already appeared: M. Lieblich [Lie06] and J. Starr [Sta06] extended some of our constructions to the case of an Artin stack Y as the target.
In addition, [Ale06] contains an application of branchvarieties to the moduli of weighted stable pairs.

Acknowledgements.
We would like to thank H´el\`ene Esnault for an argument with Frobenius used in the proof of Theorem 1.7, and J´anos Koll´ar for suggesting Theorem 9.3; of course any errors remaining are ours.
Also, we thank Patricia Hersh for discussions about rooted forests, David Speyer for correcting our calculation of stable cubics, and Diane Maclagan for asking about multigraded b-sheaves.

Michael Thaddeus informed us that he proposed the functor of this paper in the case of curves in a 1995 talk at Harvard, with the family of plane cubics as evidence (treated here in Section 8.1). We also note that Morten Hønsen constructed a proper moduli space of curves X with a finite morphism $\mathbf { f } :  { \mathbb { X } } \to  { \mathbb { P } } ^ { \mathfrak { n } }$ [Høn04]; in place of our assumption that X is reduced (S1 and R0), he only requires $\boldsymbol { x }$ to be S1, but also that f be generically an embedding.

# 1. BOUNDEDNESS

We will now fix a certain class of branchvarieties, and show that this class is bounded.
By this we will mean that for every branchvariety $\mathbf { f } :  { \mathbb { X } } \to  { \mathbb { P } } ^ { \mathrm { n } }$ in our class, over an algebraically closed field ${ \sf k } = \bar { \sf k } ,$ some fixed power $\mathsf { f } ^ { \ast } \mathcal { O } _ { \mathbb { P } ^ { \mathrm { n } } } ( 1 ) ^ { \mathrm { d } _ { 0 } }$ is very ample.
Eventually this will give us a dimension D to use in the construction of the moduli space described in the Introduction.

Example 1.1. Let n be a nonnegative integer and $\boldsymbol { x }$ be a union of two $\mathbb { P } ^ { 1 } \mathbf { s }$ joined at n simple nodes, plus a disjoint union of n points.
For any such $( X , \mathsf { f } : X \to { \bar { \mathbb { P } } } ^ { 1 }$ of degree 2), the Hilbert polynomial is the same, $\mathrm { h ( d ) } = 2 ( \mathrm { d } + 1 )$ . But as Lemma 1.3 will show, if the degree sequences $\mathsf { b } _ { 0 } = \mathsf { n } , \mathsf { b } _ { 1 } = 2$ of these curves were to all appear in a single family, the base scheme would need infinitely many connected components and hence not be of finite type.

This shows that branchvarieties with a fixed Hilbert polynomial do not form a bounded class unless one adds some further restrictions.
The easiest would be to require that X be equidimensional.
We describe a more general solution below, which we refine further in Section 7 in the case char ${ \sf k } = 0$ or large enough.

Let us introduce some notation.
Let $Z \subset \mathbb { P } ^ { \mathfrak { n } }$ be the image of $\Sigma ,$ with reduced scheme structure.
Choose a sequence of general linear forms $\mathsf { l } _ { 1 } , \ldots , \mathsf { l } _ { \mathrm { d i m } \times } \mathrm { o n } \mathbb { P } ^ { \mathrm { n } } ,$ and define $Z _ { \mathrm { i } } , X _ { \mathrm { i } }$ inductively as the Cartier divisors ${ \mathrm { l } } _ { \mathrm { i } } = 0$ in $Z _ { \mathrm { i } - 1 } , X _ { \mathrm { i } - 1 }$ respectively, with $Z _ { 0 } = Z ,$ , $\mathsf X _ { 0 } = \mathsf X$ . We know that the $Z _ { \mathrm { i } }$ are reduced irrespective of char $\boldsymbol { \mathrm { k } }$ ([Har77, II.8.18], [Fle77]) but $X _ { \mathrm { i } }$ need not be reduced if $\mathsf { f } : \mathsf { X } \to \mathsf { Z }$ is not separated: consider for example the geometric Frobenius map f $: \mathbb { P } ^ { 1 } \to \mathbb { P } ^ { 1 }$ , $x \mapsto x ^ { \mathfrak { p } }$ , in which $\mathsf { X } _ { 1 }$ is seen to be a point of multiplicity p.

Remark 1.2. The precise generality condition on the linear forms is that each $\mathsf { l } _ { \mathrm { i } }$ does not vanish identically on any of a certain finite set of proper subvarieties of $\mathbb { P } ^ { { \mathfrak { n } } }$ , namely, the associated components of $Z _ { \mathrm { i } - 1 }$ and the subvarieties appearing in Bertini’s theorem.
For the proofs of the statements of this Section we are free to make finite base extensions, and may thereby assume that such general linear forms do indeed exist.

Lemma 1.3. The integers $\mathbf { b } _ { \mathrm { i } } = \mathrm { d e g } X ^ { \mathrm { d i m i } }$ are locally constant in families of branchvarieties.

Proof.
By making a base change Spec $A \to S$ , it is sufficient to consider the case of a regular one-dimensional base, for example $\boldsymbol { \mathsf { A } }$ a DVR. Any Cartier divisor $\mathfrak { l } _ { 1 } = 0$ on the central fiber $X _ { 0 }$ can be extended to a Cartier divisor on the generic fiber $X _ { \mathfrak { \eta } }$ . Hence, the Cartier divisors $\mathsf { X } _ { 1 }$ form a flat family over Spec A with the Hilbert polynomial ${ \mathfrak { p } } _ { 1 } ( { \mathfrak { d } } ) = { \mathfrak { p } } ( { \mathfrak { d } } ) -$ $\mathsf { p } ( \mathsf { d } - 1 )$ . By induction we see that all $X _ { \mathrm { i } }$ can be put in flat families.

Now, $\mathrm { d e g } X ^ { \mathrm { d i m } \ o i } = \mathrm { d e g } ( X _ { \mathrm { i } } ) ^ { \mathrm { d i m } \ o 0 }$ . The latter space is a union of connected components of $X _ { \mathrm { i } }$ . Hence, it too is flat over Spec $A$ , and its length (or cardinality, if it is reduced and ${ \sf k } = \bar { \sf k } )$ ) is constant.

Recall the following definitions:

Definition 1.4 (Kleiman).
Let $\boldsymbol { \mathsf { b } } = \left( \boldsymbol { \mathsf { b } } _ { 0 } , \boldsymbol { \mathsf { b } } _ { 1 } , \ldots , \boldsymbol { \mathsf { b } } _ { \boldsymbol { \mathsf { n } } } \right)$ be a sequence of integers.
A coherent sheaf $\digamma$ on $\mathbb { P } ^ { { \mathfrak { n } } }$ is a b-sheaf if for generic hyperplanes $\mathfrak { l } _ { 1 } , \ldots , \mathfrak { l } _ { n }$ and the inductively defined sheaves $\mathsf { F } _ { 0 } = \mathsf { F } ,$ , $\mathsf { F } _ { \mathrm { i } } = \mathsf { F } _ { \mathrm { i } - 1 } / \mathsf { l } _ { \mathrm { i } } \mathsf { F } _ { \mathrm { i } - 1 } ,$ one has $\mathsf { h } ^ { \bar { 0 } } ( \mathsf { F } _ { \mathrm { i } } ( - 1 ) ) \le \mathsf { b } _ { \mathrm { i } }$ .

Definition 1.5. A coherent sheaf $\digamma$ on $\mathbb { P } ^ { { \mathfrak { n } } }$ is said to be Castelnuovo-Mumford m-regular if ${ \mathsf { H } } ^ { \mathrm { i } } ( { \mathsf { F } } ( \mathfrak { m } - \mathfrak { i } ) ) = 0$ for all $\mathfrak { i } > 0$ .

The following is possibly the strongest known result implying boundedness of various classes of coherent sheaves.

Theorem 1.6 (Kleiman, [SGA6], Thm.
XIII.1.11). For fixed b and $\boldsymbol { \mathrm { h } } ( \mathrm { d } )$ there exists an integer m such that every b-sheaf F with Hilbert polynomial $\chi ( \mathsf { F } ( \mathsf { d } ) ) = \mathsf { h } ( \mathsf { d } )$ is m-regular.

Here is our application of this result.

Theorem 1.7. Fix a Hilbert polynomial $\boldsymbol { \mathrm { h } } ( \mathrm { d } )$ and nonnegative integers $\mathbf { b } _ { 0 } , \mathbf { b } _ { 1 } , \ldots , \mathbf { b } _ { \mathrm { d e g h } }$ . Then there exists a positive integer ${ \mathrm { d } } _ { 0 }$ such that the following holds:

For any branchvariety $\mathbf { f } : {  { \mathbb { X } } } \to {  { \mathbb { P } } } ^ { \mathrm { n } }$ with Hilbert polynomial $\boldsymbol { \mathrm { h } } ( \mathrm { d } )$ and $\deg X ^ { \mathrm { { d i m } \mathrm { { i } } } } = \mathsf { b } _ { \mathrm { { i } } } \forall \mathsf { i } ,$ the sheaf ${ \mathrm { ~ L ~ } } ^ { \mathrm { d } }$ is very ample for ${ \mathrm { ~ d ~ } } { \geq } { \mathrm { ~ d } } _ { 0 }$ and the algebra

$$
{ \mathsf { R } } ( { \mathsf { X } } , { \mathsf { L } } ) ^ { ( { \mathsf { d } } _ { 0 } ) } = { \mathsf { k } } \oplus \bigoplus _ { { \mathsf { d } } \geq 1 } { \mathsf { H } } ^ { \circ } ( { \mathsf { X } } , { \mathsf { L } } ^ { { \mathsf { d d } } _ { 0 } } )
$$

is generated in degree 1.

(Although we won’t need it, for a slightly larger ${ \mathrm { d } } _ { 0 }$ one can also ensure that the relations are generated in degree 2.)

Proof.
By [Mum70, Thm. 3], the statement would follow if we could prove that $\mathsf { H } ^ { \mathrm { i } } ( \mathsf { X } , \mathsf { L } ^ { \mathrm { d } } ) =$ 0 for all $\mathrm { d } \geq \mathrm { d } _ { 1 }$ and $\mathfrak { i } > 0$ (we note the importance of the fact that L is free, which we have): then $\mathbf { L } ^ { ( \dim \mathbf { X } + 1 ) \mathrm { d } _ { 1 } }$ is very ample.

We apply Theorem 1.6 to the sheaf $\mathsf { F } = \mathsf { f } _ { \ast } \mathcal { O } _ { X }$ . Then $\mathsf { F } _ { \mathrm { i } } = \mathsf { f } _ { \ast } ( \mathcal { O } _ { \mathsf { X } _ { \mathrm { i } } } )$ and ${ \mathsf { H } } ^ { 0 } ( \mathsf { F } _ { \mathrm { i } } ( - 1 ) ) =$ ${ \mathsf { H } } ^ { 0 } ( X _ { \mathrm { i } } , { \mathsf { L } } ^ { - 1 } )$ . If char ${ \mathrm {  ~ k ~ } } = 0$ , the generic sections $X _ { \mathrm { i } }$ are reduced by Bertini’s theorem, so $\mathsf { h } ^ { \circ } ( \mathsf X _ { \mathrm { i } } , \mathsf L ^ { - 1 } ) = \mathrm { d e g } \mathsf X _ { \mathrm { i } } ^ { \mathrm { d i m } 0 } = \mathsf b _ { \mathrm { i } } ,$ and we are done.

If char $\mathtt { k } = \mathtt { p } > 0$ , one has to be a little more careful.
Decompose $x  Z$ into a purely inseparable morphism $\Chi \to \mathsf { Y }$ followed by a separable morphism $\Upsilon  Z$ . Then all ${ \bar { X _ { \mathrm { i } } } } \to { \bar { Z } } _ { \mathrm { i } }$ decompose into purely inseparable $\Chi _ { \mathrm { i } } \to \mathsf { Y } _ { \mathrm { i } }$ followed by separable $\Upsilon _ { \mathrm { i } } ~  ~ Z _ { \mathrm { i } } ,$ and for generic hyperplanes ${ \mathrm { l } } _ { \mathrm { i } }$ the schemes $\mathsf { Y } _ { \mathrm { i } }$ are reduced.
Since ${ X } _ { \mathrm { i } }  { Y } _ { \mathrm { i } }$ is purely inseparable, it can be dominated $\mathsf { F } ^ { \mathrm { k } } ( \mathsf { Y } _ { \mathrm { i } } ) \to \mathsf { X } _ { \mathrm { i } } \to \mathsf { Y } _ { \mathrm { i } }$ by a power $\mathsf { F } ^ { \mathrm { k } } ( \mathsf { Y } _ { \mathrm { i } } )$ of the absolute Frobenius $\mathsf { F } ( \mathsf { Y } _ { \mathrm { i } } )$ . Hence,

$$
\mathsf { H } ^ { \circ } ( \mathcal { O } _ { \mathsf { X } _ { \mathrm { i + 1 } } } ) \subset \mathsf { H } ^ { \circ } ( \mathcal { O } _ { \mathsf { p } ^ { \mathrm { k } } \mathsf { Y } _ { \mathrm { i + 1 } } } ) ,
$$

$\mathsf { Y } _ { \mathrm { i } }$ $\mathsf { l } _ { \mathrm { i } + 1 } ^ { \mathrm { p } ^ { \mathrm { k } } }$

Now, let $\mathrm { D }$ be a reduced ample Cartier divisor on a projective scheme $\Upsilon$ and assume that every connected component of $\mathrm { D }$ has dimension $\geq 1$ . Then the basic exact sequence

$$
0  \mathcal { O } _ { \mathrm { D } } ( - ( s - 1 ) \mathrm { D } )  \mathcal { O } _ { s \mathrm { D } }  \mathcal { O } _ { ( s - 1 ) \mathrm { D } }  0
$$

implies that

$$
\mathtt { h } ^ { \scriptscriptstyle 0 } ( \mathcal { O } _ { \mathrm { s D } } ( - \mathsf { D } ) ) \le \mathtt { h } ^ { \scriptscriptstyle 0 } ( \mathcal { O } _ { ( s - 1 ) \mathrm { D } } ( - \mathsf { D } ) ) \le \cdots \le \mathtt { h } ^ { \scriptscriptstyle 0 } ( \mathcal { O } _ { \mathrm { D } } ( - \mathsf { D } ) ) = 0
$$

Applying this to $\textrm { D } = \textrm { Y } _ { \mathrm { i } + 1 }$ on ${ \mathsf { Y } } = { \mathsf { Y } } _ { \mathrm { i } } ,$ we see that again only the zero-dimensional connected components contribute, and so $\mathsf { h } ^ { \circ } ( \mathsf X _ { \mathrm { i } } , \mathsf L ^ { - 1 } ) = \bar { \mathrm { d e g } } \mathsf X _ { \mathrm { i } } ^ { \mathrm { d i m } 0 ^ { \circ } } = \mathsf b _ { \mathrm { i } }$ as before.


Theorem 1.8. Fix a Hilbert polynomial h and degree sequence b, and let ${ \mathrm { d } } _ { 0 }$ be as in Theorem 1.7. Then a family of branchvarieties over $\Upsilon _ { \mathrm { S p e c } A }$ with Hilbert polynomial $\boldsymbol { \mathrm { h } } ( \mathrm { d } )$ and with each $\mathrm { d e g } X ^ { \mathrm { d i m i } } = \mathbf { \dot { b } } _ { \mathrm { i } }$ is equivalent to a graded ring R together with a homomorphism $\Phi : A [ x _ { 0 } , \ldots , x _ { \mathsf { N } } ] \to$ R, $\mathsf { N } = \binom { \mathsf { n } + \mathsf { d } _ { 0 } } { \mathsf { n } }$ such that

(1) $\mathrm { R } _ { 0 } = \lambda ,$\
(2) the $\mathsf { R } _ { \mathrm { d } }$ are finite locally free A-modules of rank $\hslash ( \mathrm { d d } _ { 0 } )$ ,\
(3) R is finite over the image of $\Phi$ ,\
(4) ker $\Phi$ contains the ideal of the ${ \mathrm { d } } _ { 0 }$ -tuple Veronese image of Y, and\
(5) for every homomorphism $\bar { A } \to \bar { \mathbb { k } }$ to an algebraically closed field, $\mathsf { R } \otimes _ { \mathsf { A } } \bar { \mathsf { k } }$ is reduced.

Moreover, any such algebra R is generated over A in degree 1.

Proof.
We first note that under the isomorphism between Y and its Veronese embedding $\nu _ { \mathrm { d } _ { 0 } } ( \mathsf { Y } )$ , the families of branchvarieties $\mathsf { f } _ { 1 } : \mathsf { X } \to \mathsf { Y } _ { S }$ and $\mathsf { f } _ { 2 } : \mathsf { X } \to \nu _ { \mathrm { d } _ { 0 } } ( \mathsf { Y } ) _ { S }$ are in natural bijective correspondence.
The (same) invertible sheaf $\mathrm { L }$ is uniquely determined by either $\mathsf { f } _ { 1 }$ or $\mathsf { f } _ { 2 }$ . Hence, without loss of generality we can replace Y by $\mathsf { Y } ^ { \prime } = \boldsymbol { \nu } _ { \mathrm { d } _ { 0 } } ( \mathsf { Y } )$ .

Given a family $\mathrm { f } : \mathsf { X } \to \mathsf { Y } _ { \mathsf { S } } ^ { \prime } ,$ , we set

$$
\mathsf { R } = \mathsf { R } ( X / S , \mathsf { L } ^ { \prime } ) ^ { ( \mathrm { d o } ) } = A \oplus \bigoplus _ { \mathrm { d } \ge 1 } \mathsf { H } ^ { \circ } ( X , ( \mathsf { L } ^ { \prime } ) ^ { \mathrm { d } } ) , \quad \mathrm { w h e r e ~ } \mathsf { L } ^ { \prime } = \mathsf { f } _ { 2 } ^ { \ast } \mathcal { O } _ { \mathbb { P } ^ { \mathrm { N } } } ( 1 ) = \mathsf { L } ^ { \mathrm { d o } } .
$$

Since the higher cohomology groups of $( \mathrm { L } ^ { \prime } ) ^ { \mathrm { d } }$ vanish, by the Cohomology and Base Change Theorem $\mathsf { H } ^ { \bar { 0 } } ( \mathsf { X } , ( \mathsf { L } ^ { \prime } ) ^ { \mathsf { k } } )$ are locally free modules of rank $\hslash ( \mathrm { d d } _ { 0 } )$ .

In the opposite direction, we set $X = \mathrm { P r o j } { \sf R } ,$ and the condition (3) gives a morphism f : $\mathsf { X } \to \mathbb { P } _ { A } ^ { \mathsf { N } } ,$ which factors through ${ \mathsf { Y } } ^ { \prime }$ by the condition (4). Clearly, the associations $( \mathbb { R } , \Phi ) $ $( X , \mathsf { f } )$ are inverses of each other, and the condition (5) is equivalent to the condition that the geometric fibers of $\boldsymbol { x }$ are reduced.

The last statement is a direct consequence of Theorem 1.7.

# 2. ONE-PARAMETER FAMILIES

In this section, A is a DVR with maximal ideal (t), residue field ${ \sf k } = \lambda / { \sf t A } ,$ and fraction field $\mathsf { K } = \mathsf { A } [ 1 / \mathrm { t } ]$ . The ring $\mathsf { R } = \oplus _ { \mathsf { d } \ge 0 } \mathsf { R } _ { \mathrm { d } }$ is a finitely generated A-algebra, and each $\mathsf { R } _ { \mathrm { d } }$ is a locally free $\boldsymbol { A }$ -module of rank $\hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom { - } \hphantom \hphantom { - } \hphantom \hphantom { - } \hphantom \hphantom { } \hphantom \hphantom { - } \hphantom \hphantom \hphantom \hphantom { \hphantom \hphantom } \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \hphantom \ h$ . By Theorem 1.8, after replacing $\mathsf { Y } \subset \mathbb { P } ^ { \mathfrak { n } }$ with its Veronese embedding $\nu _ { \mathrm { d } _ { 0 } } ( \mathsf { Y } ) \subset \mathbb { P } ^ { \mathsf { N } } .$ , such an algebra $\mathsf { R }$ is equivalent to a family of branchvarieties over Spec A.

Let $\widetilde { \sf R }$ denote the integral closure of $\mathsf { R }$ in $\mathsf { R } _ { \mathsf { K } } : = \mathsf { R } \otimes _ { \mathsf { A } } \mathsf { K } ,$ i.e. in the general fiber of the family Spec $R \to \operatorname { S p e c } A$ . Since by definition $\widetilde { \sf R } \subset \oplus _ { { \sf d } \geq 0 } { \sf R } _ { \sf d } \otimes _ { \sf A } { \sf K } ,$ it is also a graded ring.
A ring finitely generated over a DVR has a finite normalization, and therefore $\widetilde { \sf R }$ is a finitely generated R-module.
It follows that each $\widetilde { \mathsf { R } } _ { \mathrm { d } }$ is again a finitely generated A-module, so it is free of the same rank $\boldsymbol { \mathrm { h } } ( \mathrm { d } )$ and for each $\mathrm { d }$ , there exists a $\mathrm { k _ { d } }$ such that $\mathsf { R } _ { \mathrm { d } } \subset \widetilde { \mathsf { R } } _ { \mathrm { d } } \subset \mathsf { t } ^ { - \mathrm { k } _ { \mathrm { d } } } \mathsf { R } _ { \mathrm { d } }$ .

By an n-ramified base change we will mean another DVR $A ^ { \prime } \supset A$ with uniformizing parameter $\mathrm { t } ^ { \prime }$ , so that $\mathbf { t } = \mathbf { c } ^ { \prime } ( \mathbf { t } ^ { \prime } ) ^ { \mathrm { n } }$ for some unit $c ^ { \prime } \in \mathcal { A } ^ { \prime }$ . We will use $\mathsf { R } ^ { \prime }$ for $\mathsf { R } \otimes _ { \mathsf { A } } \mathsf { A } ^ { \prime } , \mathsf { K } ^ { \prime }$ for the fraction field, and ${ \widetilde { \mathsf { R } } } ^ { \prime }$ for the integral closure $\widetilde { \left( \mathbb { R } ^ { \prime } \right) }$ of $\mathsf { R } ^ { \prime }$ in $\mathsf { K } ^ { \prime }$ .

Lemma 2.1. (1) $\boldsymbol { \mathrm { R } } / ( \mathrm { t } ) \ i s \ r e d u c e d \implies \widetilde { \boldsymbol { \mathrm { R } } } = \boldsymbol { \mathrm { R } } .$ (2) R/(t) is not reduced $\Longrightarrow$ after some ramified base change $\widetilde { \sf R } ^ { \prime } \neq \sf R ^ { \prime }$ .

Proof.
(1) Suppose $\widetilde { \sf R } \neq \sf R$ . Then there exists ${ \boldsymbol { x } } \in \mathsf { R } \setminus \mathsf { t R }$ such that $x / \mathrm { t } \in \widetilde { \sf R } \setminus \sf R ,$ and it satisfies some monic equation

$$
{ \begin{array} { r l } { \left( { \frac { x } { \mathbf { t } } } \right) ^ { \mathrm { n } } + \mathbf { r } _ { \mathrm { n } - 1 } \left( { \frac { x } { \mathbf { t } } } \right) ^ { \mathrm { n } - 1 } + \cdots + \mathbf { r } _ { 0 } = 0 } & { \Longrightarrow \quad x ^ { \mathrm { n } } + \mathbf { t } \mathbf { r } _ { \mathrm { n } - 1 } x ^ { \mathrm { n } - 1 } + \cdots + \mathbf { t } ^ { \mathrm { n } } \mathbf { r } _ { 0 } = 0 } \\ & { \Longrightarrow \quad x ^ { \mathrm { n } } \in ( \mathbf { t } ) } \\ & { \Longrightarrow \quad { \bar { x } } \in \mathbf { R } / ( \mathbf { t } ) { \mathrm { i s ~ a ~ n o n z e r o ~ n i l p o t e n } } ! } \end{array} }
$$

(2) Suppose some $\bar { x } \in \mathsf { R } / ( \mathrm { t } )$ is a nonzero nilpotent, i.e. there exists some ${ \boldsymbol { x } } \in \mathsf { R } \setminus \mathsf { t R }$ such that $\boldsymbol { x } ^ { \mathrm { n } } \in \mathrm { t R }$ . Then after an n-ramified base change one has $\boldsymbol { x } ^ { \mathrm { n } } \in ( \mathrm { t } ^ { \prime } ) ^ { \mathrm { n } } \mathsf { R } ^ { \prime }$ . So $( \mathsf { x } / \mathsf { t } ^ { \prime } ) ^ { \mathrm { n } } \in \mathsf { R } ^ { \prime }$ . Hence, $\boldsymbol { \mathbf { \mathit { x } } } / \mathrm { t ^ { \prime } }$ is integral over ${ \sf R ^ { \prime } }$ , and so $x / \mathrm { t ^ { \prime } } \in \widetilde { \sf R } ^ { \prime }$ . It remains to show $\boldsymbol { x } / \mathrm { t } ^ { \prime } \notin \mathsf { R } ^ { \prime }$ .

Since R, $\mathsf { R } ^ { \prime }$ are torsion-free $A , A ^ { \prime }$ -modules over DVRs, for any $x \in \mathbb { R }$ we have the equivalences

${ \mathfrak { x } } / { \mathfrak { t } } \in { \mathbb { R } } \iff { \mathfrak { x } } \in { \mathfrak { t } } { \mathbb { R } } \iff$ the $\mathsf { A }$ -module $\mathsf { R } / { \boldsymbol { x } } \mathsf { A }$ has torsion $\iff \mathsf { R } / { \mathsf { x } } \mathsf { A }$ is not flat ${ \boldsymbol { \mathrm { x } } } / { \mathrm { t } } ^ { \prime } \in \mathbb { R } ^ { \prime } \iff { \boldsymbol { \mathrm { x } } } \in { \mathrm { \mathbf { \mathrm { t } } } } ^ { \prime } \mathbb { R } ^ { \prime } \iff$ the $A ^ { \prime }$ -module $\mathsf { R } ^ { \prime } / \mathsf { x } \mathsf { A } ^ { \prime }$ has torsion $\iff \mathsf { R } ^ { \prime } / \mathsf { x } \mathsf { A } ^ { \prime }$ is not flat.

So $x / \mathrm { t } \notin \mathrm { ~ \sf R }$ implies $\mathsf { R } / { \boldsymbol { x } } \mathsf { A }$ is flat, which implies ${ \sf R } ^ { \prime } / x { \cal A } ^ { \prime } = ( { \sf R } / x { \cal A } ) \otimes _ { \cal A } { \cal A } ^ { \prime }$ is flat, which implies $\boldsymbol { x } / \mathrm { t } ^ { \prime } \notin \mathrm  ~ \} \mathsf { R } ^ { \prime }$ .

Corollary 2.2 (The functor $\mathrm { B r a n c h } _ { \mathrm { h , Y } } ^ { \mathrm { b } }$ is separated).
An element of $\mathrm { B r a n c h } _ { \mathrm { h , Y } } ^ { \mathrm { b } } ( \mathsf { K } )$ has at most one extension to an element of $\mathrm { B r a n c h } _ { \mathrm { h , Y } } ^ { \mathrm { b } } ( A )$ .

Proof.
Call the original element $\mathsf { K } [ { \mathsf { x } } _ { 0 } , \ldots , { \mathsf { x } } _ { \mathsf { n } } ] \to \mathsf { R } _ { \mathsf { K } }$ . The only possible R will be the integral closure of the image of $A [ x _ { 0 } , \ldots , x _ { \mathrm { n } } ]$ in $\mathsf { R } _ { \mathsf { K } } ,$ as we now show in two steps.

Let $\boldsymbol { A } [ x _ { 0 } , \ldots , x _ { n } ]  \mathtt { R }$ be an extension.
Then R is finite over the image of $A [ x _ { 0 } , \ldots , x _ { \mathrm { n } } ]$ in ${ \sf R } ,$ so $\widetilde { \sf R }$ is the integral closure of the image of $A [ x _ { 0 } , \ldots , x _ { \mathrm { n } } ]$ in $\mathsf { R } _ { \mathsf { K } }$ .

The special fiber ${ \sf R } / { \sf t R }$ is reduced because so is the geometric fiber $( { \sf R } / { \sf t R } ) \otimes _ { \sf k } \bar { \sf k } .$ . But then ${ \sf R } = \widetilde { { \sf R } }$ by Lemma 2.1(1). 

Remark 2.3. For any finitely generated algebra S over a field k, $S \otimes _ { \mathsf { k } } \bar { \mathsf { k } }$ is reduced $\Longrightarrow$ S is reduced.
The converse is true if $\boldsymbol { \mathrm { k } }$ is a field of characteristic zero or a perfect field of characteristic $\mathfrak { p } > 0$ . Moreover, if $S \otimes _ { \mathsf { k } } \bar { \mathsf { k } }$ is not reduced then already for some finite purely inseparable extension $\mathsf { k } ^ { \prime } / \mathsf { k } , \mathsf { S } \otimes _ { \mathsf { k } } \mathsf { k } ^ { \prime }$ is not reduced.

Lemma 2.4. Let R be a Noetherian ring which has finite normalization (e.g. R has no embedded primes and is finitely generated over a field or a DVR), $\mathrm { \Delta t } \in \mathrm { \sf R }$ a nonzerodivisor, and assume that R is integrally closed in $\mathsf { R } [ \mathsf { t } ^ { - 1 } ]$ . Then the ring R/(t) does not have embedded primes; it satisfies Serre’s condition S1.

In particular, if Spec R is reduced, R is finite over a DVR and integrally closed in $\mathsf { R } [ \mathsf { t } ^ { - 1 } ] ,$ , and Spec R/(t) is generically regular, then Spec R/(t) too is reduced.

By the normalization of R we understand its integral closure in the total ring of fractions ${ \mathsf { R } } [ { \mathsf { S } } ^ { - 1 } ]$ , the localization in all nonzerodivisors.

If we assumed R to be reduced and equal to its normalization, then R would satisfy Serre’s condition S2, so $\mathsf { R } / ( \mathsf { t } )$ would be S1. This Lemma clarifies how much integral closure one actually needs to draw this conclusion.

Proof of Lemma 2.4, latter conclusion.
There is a simpler proof in this special case (which is all we will need).
Or rather, the only subtle point is encapsulated in a familiar formulation “normal domains are $S 2 ^ { \prime \prime }$ .

Let $\mathsf { R } ^ { \prime }$ be the normalization of R. By our assumptions on R, the ring $\mathsf { R } ^ { \prime }$ is a direct sum of finitely many normal domains.
Consider the map $\mathsf { R } / \mathsf { t R } \to \mathsf { R } ^ { \prime } / \mathsf { t R } ^ { \prime }$ . Its kernel is

$$
\frac { \textsf { R } \cap { \mathsf { t R } ^ { \prime } } } { \mathsf { t R } } \cong \frac { \mathsf { t } ^ { - 1 } \mathsf { R } \cap \mathsf { R } ^ { \prime } } { \mathsf { R } } \subset \frac { \mathsf { R } [ \mathsf { t } ^ { - 1 } ] \cap \mathsf { R } ^ { \prime } } { \mathsf { R } } = 0
$$

thanks to the assumptions on t and on R. Hence the map $\mathsf { R } / \mathsf { t R } \to \mathsf { R } ^ { \prime } / \mathsf { t R } ^ { \prime }$ is an inclusion.

Since $X _ { 0 } : = { \mathrm { S p e c } } \mathsf { R } / ( \mathrm { t } )$ is generically regular, there exists an open subset $\mathsf { U } \subset \mathrm { S p e c } \mathsf { R }$ such that U is regular and such that $\mathsf { U } \cap \mathsf { X } _ { 0 }$ is dense in $X _ { 0 }$ . Then the normalization morphism Spec $\mathsf { R } ^ { \prime } \to \operatorname { S p e c } \mathsf { R }$ is an isomorphism over U. So Spec $\mathsf { R } ^ { \prime } / ( \mathsf { t } )$ is generically regular.

Since $\mathsf { R } ^ { \prime }$ is S2, and $\mathrm { t }$ is not a zero divisor, $\mathsf { R } ^ { \prime } / ( \mathsf { t } )$ is S1. Being S1 and generically regular, $\mathsf { R } ^ { \prime } / ( \mathsf { t } )$ is reduced.
Since $\mathsf { R } / ( \mathsf { t } )$ is a subring of a reduced ring, it too is reduced.


Proof of Lemma 2.4 in general.
Essentially, we must modify the proof that normal domains are S2. Let us introduce some notation.
Let $X = { \mathrm { S p e c } } \mathbf { R } ,$ , and let $\mathcal { F }$ be a coherent sheaf on X, corresponding to a finite R-module $M$ . Let $X _ { 0 } = { \mathrm { S p e c } } \mathrm { R } / ( \mathrm { t } ) ,$ , and define the saturation of $\mathcal { F }$ in codimension 2 along $X _ { 0 }$ by the formula

$$
{ \mathcal { F } } ^ { \mathrm { s a t } } = \varinjlim _ { Z } { \mathcal { F } } ( X \setminus Z ) ,
$$

where $\textsf { Z }$ goes over closed subsets of $X _ { 0 }$ that have $\mathrm { c o d i m } _ { Z } \mathsf { X } _ { 0 } \geq 1$ , equivalently $\mathrm { c o d i m } _ { Z } X \geq$ 2 since t is a nonzerodivisor in R. Let $M ^ { \mathrm { s a t } } = \Gamma ( X , { \mathcal { F } } ^ { \mathrm { s a t } } )$ be the corresponding R-module.

It is true that the sheaf $\mathcal { F } ^ { \mathrm { s a t } }$ is coherent provided all $Z s$ have codimension $\geq 2$ in associated primes of $M _ { ☉ }$ , cf.
[EGA4-2, 5.9-11], but we do not need this.
We merely observe that $\mathcal { O } _ { X } ^ { \mathrm { s a t } } = \mathcal { O } _ { X }$ since every $\Gamma ( X \setminus Z , { \mathcal { O } } _ { X } )$ is contained in the normalization of R and also in $\Gamma ( X \setminus X _ { 0 } , { \mathcal { O } } _ { X } ) = \mathsf { R } [ \mathrm { t } ^ { - 1 } ]$ .

Let $\sf G$ be a coherent sheaf supported on an irreducible subset ${ \cal Z }$ of $X _ { 0 }$ with $\mathrm { c o d i m } _ { X } Z \ge 2$ Then every extension

$$
0 \to { \mathcal { O } } _ { \mathsf { X } } \to { \mathsf { F } } \to { \mathsf { G } } \to 0
$$

splits.
Indeed, $\mathsf { F } ^ { \mathrm { s a t } } = { \mathcal { O } } _ { \mathsf { X } } ^ { \mathrm { s a t } } = { \mathcal { O } } _ { \mathsf { X } } ,$ and the canonical restriction morphism $\mathsf { F } \to \mathsf { F } ^ { \mathrm { s a t } }$ provides the splitting.
Therefore, $\mathrm { E x t } ^ { 1 } ( \mathbf { G } , \mathcal { O } _ { x } ) = 0$ . By the cohomological characterization of depth (see e.g. [Mat89, Thm. 28] or [Eis95, 18.4]) this implies that the local ring $\mathcal { O } _ { Z , X }$ has depth $\geq 2 ,$ and therefore $\mathcal { O } _ { Z , X _ { 0 } }$ has depth $\geq 1$ , i.e. the ideal $_ { \mathsf { p } _ { Z } }$ is not an embedded prime of R/(t). 

Theorem 2.5 (The functor $\mathrm { B r a n c h } _ { \mathrm { h , Y } } ^ { \mathrm { b } }$ is proper).
Every element of $\mathrm { B r a n c h } _ { \mathrm { h , } \Upsilon } ^ { \mathrm { b } } ( \mathsf { K } )$ has an extension to one of $\mathrm { B r a n c h } _ { \mathrm { h , \tt Y } } ^ { \mathrm { b } } ( A ^ { \prime } ) ,$ , after a finite ramified base change $\mathbf { S } ^ { \prime } = \operatorname { S p e c } A ^ { \prime }  \mathbf { S } = \operatorname { S p e c } A$ .

The necessary base change $\deg ( S ^ { \prime } / S )$ divides $( \prod _ { i = 0 } ^ { \mathrm { d e g h } } { \mathsf { b } } _ { \mathrm { i } } ! ) ^ { 2 } .$ , and if the residue field $\mathsf { k } = \mathsf { A } / ( \mathsf { t } )$ has characteristic zero, then the necessary base change even divides $\textstyle \prod _ { \mathrm { i = 0 } } ^ { \mathrm { d e g h } } { { \mathsf { b } } _ { \mathrm { i } } } !$ .

Let $X  \operatorname { S p e c } { j }$ A be a flat proper extension (before any base change), $\widetilde { x }$ the normalization of X in the generic fiber, and $\widetilde { X } _ { 0 }$ the special fiber of $\widetilde { x }$ . Denote the multiplicities of the geometric fiber $\widetilde { x } _ { 0 } \times \widetilde { \mathtt { k } }$ by $\{ \mathfrak { m } _ { \mathrm { i } } \}$ .

$I f \operatorname { c h a r } \mathbf { k } = 0 ,$ then the base change can be taken to be ${ \mathrm { t } } = s ^ { \mathfrak { m } }$ , where $\mathrm { { m } = \mathrm { { l c m } ( \{ m _ { i } \} ) , } }$ , the least common multiple of the multiplicities.

$I f \mathrm { c h a r } \mathbf k > 0 ,$ , the base change can be chosen to be a composition of a base change $\mathbb { A } ^ { \prime } / \mathbb { A }$ such that $\mathrm { t } A ^ { \prime } = \mathrm { t } ^ { \prime } A ^ { \prime }$ and the residue field extension ${ \sf k ^ { \prime } } / { \sf k }$ is purely inseparable of degree dividing $\prod \mathfrak { m } _ { \mathrm { i } } ,$ and the base change $\mathbf { t } ^ { \prime } = s ^ { \mathsf { m } }$ .

Proof.
We first provide a flat A-algebra R extending $\mathsf { R } _ { \mathsf { K } }$ . Let ${ \mathfrak { q } } _ { 1 } , \dotsc , { \mathfrak { q } } _ { s } \in { \mathsf { R } } _ { \mathsf { K } }$ be homogeneous elements generating $\mathsf { R } _ { \mathsf { K } }$ as a ${ \mathsf { K } } [ { \mathsf { x } } _ { 0 } , \ldots , { \mathsf { x } } _ { \mathrm { n } } ]$ -module.
Each ${ \mathfrak { q } } _ { \mathrm { i } }$ is integral over $\mathsf { K } [ \mathsf { x } _ { 0 } , \ldots , \mathsf { x } _ { \mathrm { n } } ]$ Since $\mathsf { K } = \mathsf { A } [ 1 / \mathrm { t } ]$ , there exist $\mathfrak { n } _ { \mathrm { i } } \in \mathbb { N }$ such that $\mathbf { t } ^ { \mathrm { n } _ { \mathrm { i } } } \mathbf { q } _ { \mathrm { i } }$ are integral over $A [ x _ { 0 } , \ldots , x _ { \mathrm { n } } ]$ . Therefore, the algebra $\mathsf { R } _ { 1 } : = ( \mathrm { i m } \mathsf { A } [ \mathsf { x } _ { 0 } , \mathsf { \ldots } , \mathsf { x } _ { \mathrm { n } } ] ) [ \mathsf { t } ^ { \mathsf { n } _ { \mathrm { i } } } \mathsf { q } _ { \mathrm { i } } ]$ is finite over $A [ x _ { 0 } , \ldots , x _ { \mathrm { n } } ] .$ , graded, and free over A. Take $\mathsf { R } = \widetilde { \mathsf { R } } _ { 1 }$ to be its normalization in $\mathsf { R } _ { 1 } [ \mathsf { t } ^ { - 1 } ] ,$ , as before.
(These ${ \sf R } _ { 1 }$ , $\widetilde { \sf R } _ { 1 }$ are the coordinate rings of $x , \tilde { x }$ in the statement of the Theorem.)

Next, we find a ramified base change $S ^ { \prime } \to S$ so that the geometric fiber Spec $\widetilde { \sf R ^ { \prime } } \otimes _ { \bf k ^ { \prime } } \bar { \sf k } ^ { \prime }$ is reduced.
By Lemma 2.4 we only need to prove that it is generically reduced.

Assume first that char $\ k = 0$ . Let Z be an irreducible component of the central fiber ${ \sf X } _ { 0 } ,$ with generic point $z$ . The ring $\mathcal { O } _ { z , x }$ has dimension 1 and is integrally closed in the generic fiber, since normalization commutes with localization.
(This is where we must use $\widetilde { \sf R } _ { 1 }$ and not ${ \sf R } _ { 1 }$ .) Therefore, it is integrally closed, so it is a DVR with a uniformizing parameter, denote it by $\pi$ .

We have $\mathbf { t } = \mathbf { a } \pi ^ { \mathfrak { n } }$ for some invertible a. Let us make a base change $\mathbf { t } = s ^ { \mathfrak { n } }$ . Then the normalization $\widetilde { \mathcal { O } } _ { z ^ { \prime } , X ^ { \prime } }$ of $\mathcal { O } _ { z , x \otimes A } A ^ { \prime }$ is regular and its central fiber has multiplicity 1. Indeed, $\pi / s \in \widetilde { \mathcal { O } } _ { z , x }$ and is invertible, so $s = \mathbf { b } \pi$ in $\widetilde { \mathcal { O } } _ { z ^ { \prime } , X ^ { \prime } }$ with invertible b. Hence, after making the base change ${ \mathrm { t } } = s ^ { \mathfrak { m } }$ , where $\mathrm { { m } = \mathrm { { l c m } ( \{ m _ { i } \} ) } }$ , the central fiber is generically regular, and we are done.

If char ${ \sf k } > 0$ , then we first make an unramified base change $S ^ { \prime } / S$ with a purely inseparable field extension ${ \sf k ^ { \prime } } / { \sf k }$ after which the multiplicities of the irreducible components of $X _ { 0 } ^ { \prime }$ and $X _ { 0 } \times _ { \mathsf { k } } { \bar { \mathsf { k } } }$ are the same; the degree of this base change divides $\prod { \mathfrak { m } } _ { \mathrm { i } }$ . Then we proceed as above.


Corollary 2.6. For any further ramified base change $A ^ { \prime \prime } \supset A ^ { \prime }$ , the central fiber does not change except for the extension of the residue fields: $X _ { 0 } ^ { \prime \prime } = X _ { 0 } ^ { \prime } \otimes _ { \mathbf { k } ^ { \prime } } \mathbf { k } ^ { \prime \prime }$ . In other words, every 1-parameter family of branchvarieties has a unique limit, up to extensions of the residue field.

Proof.
Indeed, the geometric central fiber of $X ^ { \prime } \otimes _ { S ^ { \prime } } S ^ { \prime \prime }$ is the same as that of $X ^ { \prime }$ , so it is reduced.
By Lemma 2.1(1), one has $X ^ { \prime \prime } = X ^ { \prime } \times _ { S ^ { \prime } } S ^ { \prime \prime }$ . 

The $\{ \mathfrak { m } _ { \mathrm { i } } \}$ have a simple interpretation in the case that $\boldsymbol { x }$ is a family of points over Spec C[[t]]: they are the lengths of the cycles in the monodromy around 0 of the generic fiber.
The degree $\mathrm { { l c m } ( \{ m _ { i } \} ) }$ base change replaces the monodromy in this finite family by a high enough power to make it trivial.

Example 2.7. In examples, where one has a family of subvarieties limiting to a subscheme, one often knows the Hilbert extension $X  \operatorname { S p e c } A$ . So it is tempting to work with the multiplicities of the special fiber $X _ { 0 }$ to compute the necessary base change, rather than those of $\widetilde { X } _ { 0 }$ as stated in the Theorem.
But consider the family

$$
X = \left\{ [ x , y ] : ( y ^ { 2 } + \pm x ^ { 2 } ) ( y ^ { 3 } - \pm x ^ { 3 } ) = 0 \right\}
$$

of 5-tuples of points.
In this case $X _ { 0 }$ is a quintuple point, but the necessary base change has $\deg ( S ^ { \prime } / S ) = 6 ,$ correctly calculable from $\widetilde { X } _ { 0 } = \left\{ \begin{array} { l l } { \begin{array} { r l r } \end{array} } \end{array} \right.$ {double point, triple point}.

Remark 2.8. In [Ale06] it is proved that the canonical limits of varieties and pairs of general type, whose construction follows from the log Minimal Model, are S2, in addition to being S1, as in Theorem 2.5. This result, however, applies to a less general class of degeneration families than (2.5).

# 3. CONSTRUCTION OF THE MODULI SPACE

For every family of branchvarieties $\mathsf { f } : X \to \mathsf { Y } _ { S } ,$ define a functor

$$
{ \mathrm { A u t } } ( \mathbf { f } ) : ( { \mathrm { S } } { \mathrm { - s c h e m e s } } ) \to ( { \mathrm { G r o u p s } } ) ^ { \mathrm { o p p } }
$$

by setting $\operatorname { A u t } ( \mathbf { f } ) ( S ^ { \prime } )$ to be the automorphism group of $\mathsf { f } ^ { \prime } : \mathsf { X } ^ { \prime } \to \mathsf { Y } _ { S ^ { \prime } } ^ { \prime } ,$ where ${ \cal { X } } ^ { \prime } = { \cal { X } } \times _ { S } { \cal { S } } ^ { \prime } .$ , $\mathsf { Y } ^ { \prime } = \mathsf { Y } \times _ { \mathsf { S } } \mathsf { S } ^ { \prime } .$ , and $\mathsf { Y } _ { \mathsf { S } ^ { \prime } } ^ { \prime } = \mathsf { Y } _ { \mathsf { S } } \times _ { \mathsf { S } } \mathsf { S } ^ { \prime } = \mathsf { Y } \times _ { \mathsf { C } } \mathsf { S } ^ { \prime }$ .

Theorem 3.1. $\operatorname { A u t } ( \mathsf { f } )$ is represented by $a$ finite group scheme over S.

Proof.
Let $\mathsf X ^ { ( 2 ) } : = \mathsf X \times _ { \mathsf Y _ { \mathsf S } } \mathsf X ,$ a proper and projective scheme over S.

For every automorphism ${ \mathfrak { g } } : { \mathsf { X } } ^ { \prime } \to { \mathsf { X } } ^ { \prime }$ over $\Upsilon _ { S ^ { \prime } } ^ { \prime }$ , its graph $\Gamma _ { 9 }$ is a closed subscheme of $X ^ { ( 2 ) } \times _ { S } S ^ { \prime }$ . Therefore, it represents an $S ^ { \prime }$ -point of the Hilbert scheme Hilb $X ^ { ( 2 ) }$ , i.e. an element of $( \mathrm { H i l b } ( X ) ^ { 2 } ) ( S ^ { \prime } )$ . Moreover, there is a natural open subscheme U of Hilb $X ^ { ( 2 ) }$ parametrizing subschemes $Z \subset X ^ { ( 2 ) } \times _ { S } S ^ { \prime }$ that project isomorphically to both factors, and $\Gamma _ { 9 }$ gives an $S ^ { \prime }$ -point of U. The opposite is clear as well: every such subscheme Z is the graph of a unique automorphism.
Hence, the quasiprojective-over-S scheme U represents Aut(f). It is obviously a group scheme.

$\operatorname { A u t } ( \mathsf { f } )$ satisfies the valuative criterion of properness thanks to the properness of the functor of branchvarieties, Theorem 2.5. To prove that $\operatorname { A u t } ( \mathsf { f } )$ is finite over S we need to check that the geometric fibers are finite.

So let f $: X \to \Upsilon$ be a branchvariety over a field k. Cover Y by finitely many open affines ${ \mathrm { V } } _ { \mathrm { i } }$ . Since the morphism f is finite, each $\mathrm { U } _ { \mathrm { i } } = \mathrm { f } ^ { - 1 } ( \mathrm { V } _ { \mathrm { i } } )$ are affine as well, and we only need to show that $\mathrm { A u t ( U _ { i } / V _ { i } ) }$ is finite.
Let $\gamma \in \kappa [ \mathrm { U } _ { \mathrm { i } } ]$ . It satisfies some monic polynomial equation with coefficients in $\mathrm { k } [ \mathrm { V _ { i } } ]$ , and the image of r under any automorphism must satisfy it too.
Since $\mathrm { k } [ \mathrm { U } _ { \mathrm { i } } ]$ is reduced, it is embedded into a direct sum of finitely many fields, one for each irreducible component.
A monic (hence nonzero) polynomial has only finitely many roots in a field, so we are done.


For a branchvariety $\boldsymbol { x }$ over a field of characteristic 0 it is easy to say more: $\operatorname { A u t } ( \mathsf { f } )$ is a subgroup of the product of Galois groups of the irreducible components of $\Sigma ,$ and therefore a subgroup of the product of several symmetric groups.
And, of course, by Cartier’s theorem any group scheme in characteristic zero is reduced.

Example 3.2. Let char ${ \textsf { k } } = { \mathfrak { p } }$ and f $\colon \boldsymbol { \mathsf { X } } = \mathbb { P } ^ { 1 }  \boldsymbol { \mathsf { Y } } = \mathbb { P } ^ { 1 }$ be the geometric Frobenius morphism, $x \mapsto x ^ { \mathtt { p } }$ . Then $\mathrm { A u t } ( \mathsf { f } ) = \mathsf { \textmu } _ { \mathsf { p } } = \mathrm { S p e c } \mathsf { k } [ \mathsf { x } ] / ( \mathsf { x } ^ { \mathsf { p } } - 1 ) = \mathrm { S p e c } \mathsf { k } [ \mathsf { x } ] / ( \mathsf { x } - 1 ) \mathsf { p } ^ { }$ , a finite nonreduced group scheme.

Proof of the Main Theorem 0.4. We first prove that branchvarieties together with some additional data can be parametrized by a locally closed subscheme of a certain Hilbert scheme.
This is done by a classical argument, as in the case of curves [MFK94, Prop. 5.1], with necessary modifications.

Then the moduli space is constructed by taking the quotient by a PGL group action.
We do not use Geometric Invariant Theory for this step.
Instead, the quotient by a proper group action immediately gives the moduli stack as an algebraic Artin stack.
By applying standard results on representability, we obtain its coarse moduli space as an algebraic space.

Let ${ \textsf { f } } : X \to \mathsf { Y }$ be a branchvariety defined over an algebraically closed field ${ \sf k } ,$ with fixed Hilbert polynomial $\mathrm { \hslash }$ and degree sequence b. By Theorem 1.7, we know that there exists some integer $\mathrm { d } _ { 0 } ( \mathsf { h } , \mathsf { b } )$ such that ${ \mathrm { ~ L } } ^ { \mathrm { d } _ { 0 } }$ has vanishing higher cohomology, is very ample, and such that the ring of global sections $\mathbb { R } ( \mathbb { X } , \mathbb { L } ^ { \mathrm { d } _ { 0 } } )$ is generated in degree 1. Let $\mathrm { ~ D ~ } =$ $\mathsf { h } ^ { 0 } ( \mathsf { X } , \mathsf { L } ^ { \mathrm { d } _ { 0 } } ) - 1$ . A choice of a basis in the vector space $\bar { { \sf H } } ^ { 0 } ( X , \mathrm { { L } } ^ { \mathrm { d } _ { 0 } } )$ defines an embedding $\mathbf { \boldsymbol { X } } \hookrightarrow \mathbb { P } ^ { \mathrm { { D } } } .$ , and two such choices differ by an element of $\mathrm { P G L } _ { \mathrm { D } + 1 } ( \mathbf { k } )$ .

Let $\mathbb { P } ^ { \mathrm { n } } \supset \mathsf { Y }$ be the projective embedding of Y. Let $\mathbb { P } ^ { \mathrm { D } } \times \mathbb { P } ^ { \mathrm { n } } \hookrightarrow \mathbb { P } ^ { \mathrm { m } }$ be the Segre embedding, $\mathfrak { m } + 1 = ( \mathsf { D } + \bar { 1 } ) ( \mathfrak { n } + 1 )$ . The restriction of $\mathcal { O } _ { \mathbb { P } ^ { \mathrm { m } } } ( 1 )$ to $\ b \chi \subset \mathbb { P } ^ { \mathrm { D } } \times \ b \Upsilon \subset \mathbb { P } ^ { \mathrm { D } } \times \mathbf { \tilde { P } } ^ { \mathrm { n } } \subset \mathbb { P } ^ { \mathrm { m } }$ is isomorphic to $\mathbf { L } ^ { \mathrm { ~ d } _ { 0 } } \otimes \mathbf { L }$ and has Hilbert polynomial ${ \sf H } ( { \sf d } ) = { \sf h } ( { \sf d } ( { \sf d } _ { 0 } + 1 ) )$ .

Let $\mathrm { H i l b } _ { \mathsf { H } , \mathbb { P } ^ { \mathrm { D } } \times \mathsf { Y } }$ be the Hilbert scheme parametrizing closed subschemes of $\mathbb { P } ^ { \mathrm { { D } } } \times \mathsf { Y }$ that have Hilbert polynomial H. The properties of being geometrically reduced, the first projection being a closed embedding with the image spanning $\mathbb { P } ^ { \mathrm { { D } } }$ , and the second projection being finite, are all open in projective families over a quasiprojective base.
Thus, there exists an open subscheme ${ \cal V } _ { 1 }$ of $\mathrm { H i l b } _ { \mathsf { H } , \mathbb { P } ^ { \mathsf { D } } \times \mathsf { Y } }$ whose $\boldsymbol { \mathrm { k } }$ -points correspond to branchvarieties of Y embedded in $\mathbb { P } ^ { \mathrm { { D } } } \times \mathsf { Y }$ and spanning $\mathbb { P } ^ { \mathrm { { D } } }$ .

The Hilbert polynomials of the ample sheaves $\mathfrak { p } _ { 1 } ^ { * } \mathcal { O } _ { \mathbb { P } ^ { \mathrm { D } } } ( 1 )$ and $\mathfrak { p } _ { 2 } ^ { * } \mathcal { O } _ { \mathtt { Y } } ( 1 )$ are locally constant.
By Lemma 1.3, the degree sequence is locally constant as well.
This gives an open subscheme ${ \sf V } _ { 2 } \subseteq { \sf V } _ { 1 }$ over which the branchvarieties have invariants $( \mathsf { h } , \mathsf { b } )$ and such that the sheaf $\mathcal { O } _ { \mathbb { P } ^ { \mathrm { D } } } ( 1 ) | _ { X }$ has the same Hilbert polynomial as the sheaf ${ \bf L } ^ { \mathrm { d } _ { 0 } }$ .

Let $\mathcal { X } _ { 2 }  \mathsf { V } _ { 2 }$ be the universal family.
On this family, we have two invertible sheaves, $\mathfrak { p } _ { 1 } ^ { * } \mathcal { O } _ { \mathbb { P } ^ { \mathrm { D } } } ( 1 )$ and $\mathfrak { p } _ { 2 } ^ { * } \mathcal { O } _ { \Upsilon } ( \mathrm { d } _ { 0 } )$ . We claim that there exists a locally closed subscheme $\vee$ of ${ \sf V } _ { 2 }$ parametrizing branchvarieties on which these two sheaves coincide.
Indeed, the relative Picard functor $\mathrm { P i c } _ { \mathcal { X } _ { 2 } / \mathcal { V } _ { 2 } }$ is represented by an algebraic space (this is Artin’s theorem, see [Art69, Thm. 7.3] or [BLR90, Thm. 8.3.1]). The two sheaves above define sections of this algebraic space over $\mathrm { V } _ { 2 } ,$ and $\vee$ is the locus where these sections coincide.

To summarize: we have constructed a scheme $\vee$ parametrizing branchvarieties of Y together with an embedding by a complete linear system ${ \mathrm { ~ L } } ^ { \mathrm { d } _ { 0 } }$ into a fixed projective space $\mathbb { P } ^ { \breve { D } }$ so that the image spans $\mathbf { \bar { \mathbb { P } } ^ { D } }$ . Two points in ${ \sf V } ( { \sf k } )$ define isomorphic branchvarieties iff they are in the same orbit of the group $\mathrm { P G L } _ { \mathrm { D } + 1 } ( \mathbf { k } )$ .

Now consider a family of branchvarieties ${ \mathfrak { f } } : X \to \Upsilon _ { \mathbb { S } } , \pi : X \to S$ over an arbitrary C-scheme S. By the Cohomology and Base Change Theorem [Har77, III.12.11], the sheaf $\mathsf { F } _ { \mathrm { d } _ { 0 } } = \pi _ { * } \mathsf { L } ^ { \mathrm { d } _ { 0 } }$ is locally free, so it becomes trivial on some open affine cover $S = \cup S _ { \mathrm { i } }$ . The choice of trivializations of $\mathsf { F } _ { \mathrm { d } _ { 0 } , \mathrm { i } } = \mathsf { F } _ { \mathrm { d } _ { 0 } } | _ { \mathsf { S } _ { \mathrm { i } } }$ gives the choice of embeddings of $X _ { \mathrm { i } }$ into $\mathbb { P } ^ { \mathrm { { D } } } \times \mathsf { Y } _ { S _ { \mathrm { i } } } ,$ , and two such embeddings differ by an element of $\mathrm { P G L } _ { \mathrm { D } + 1 } ( S _ { \mathrm { i } } )$ . This gives a collection of $\mathsf { S } _ { \mathrm { i } }$ -points of $\mathsf { V } _ { \iota }$ , up to actions of the groups $\mathrm { P G L } _ { \mathrm { D } + 1 } ( S _ { \mathrm { i } } )$ .

It follows that the stack in groupoids $B r a n c h _ { \mathrm { h , Y } } ^ { \mathrm { b } }$ is just the quotient stack $[ \mathsf { V } / \mathsf { P G L _ { D + 1 } } ] .$ , in other words the quotient of $\vee$ by a smooth pre-equivalence relation

$$
{ \mathfrak { j } } : \mathbb { R } = \nabla \times \operatorname { P G L } _ { \operatorname { D } + 1 } \to \nabla \times \mathsf { V } .
$$

It is well known that the separatedness of the moduli functor (Corollary 2.2) and finiteness of the automorphism schemes (Theorem 3.1) imply that the group action is proper.
In particular, the stabilizer $\mathrm { j } ^ { - 1 } ( \mathrm { d i a g } \mathsf { V } ) \to \mathsf { V }$ is finite.

Thus, $\mathrm { B r a n c h } _ { \mathrm { h , Y } } ^ { \mathrm { b } }$ is an algebraic Artin stack; see [LMB00] for a general reference.
By either [KM97] or [Kol97] it has a coarse moduli space as an algebraic space (see [Knu71] for the general reference on algebraic spaces).
Finally, by Theorem 2.5 the functor is proper, so the moduli space is too.


Remark 3.3. A separated Artin stack with a finite stabilizer is Deligne-Mumford if its stabilizer groups are reduced.
By Theorem 3.1, in characteristic 0 our moduli stacks of branchvarieties are Deligne-Mumford (and more generally, under Assumption 7.2 to come), but Example 3.2 shows that in general they are not.
Nor are the stabilizer groups always linearly reductive in characteristic ${ \mathfrak { p } } ,$ , as the branchvariety of $\mathfrak { p }$ points mapping to a point (with automorphism group $S _ { \mathrm { { p } } }$ ) demonstrates.

Remark 3.4. Recall that the tangent space to the Hilbert scheme has a particularly simple description: if $Z \subset \mathbb { P } ^ { \mathrm { D } } \times \mathsf { Y }$ is a closed subscheme defined by an ideal sheaf $\mathrm { I } _ { Z }$ then

$$
\mathsf { T } _ { [ Z ] , \mathrm { H i l b } ( \mathbb { P } ^ { \mathrm { D } } \times \mathsf { Y } ) } = \mathrm { H o m } ( \mathrm { I } _ { Z } / \mathrm { I } _ { Z } ^ { 2 } , \mathcal { O } _ { Z } ) .
$$

Applying [Ols06, Theorem 1.5] to the representable morphism $\begin{array} { r } { \mathsf { V } \twoheadrightarrow \thinspace [ \mathrm { V / P G L _ { D + 1 } } ] , } \end{array}$ , and chasing a couple of short exact sequences relating the cotangent complexes [Ill71, Ill72], we can describe the tangent space to the corresponding point of Branch as

$$
\mathsf { T } _ { [ Z ] , \mathrm { B r a n c h } ( \mathsf { Y } ) } = \mathsf { T } _ { [ Z ] , \mathrm { H i l b } ( \mathbb { P } ^ { \mathrm { D } } \times \mathsf { Y } ) } \big / \mathsf { L i } e \big ( \mathrm { P G L } _ { \mathsf { D } + 1 } \big ) .
$$

In addition, one can identify the corresponding obstruction spaces on the nose (no quotient by $\mathsf { L i e } \big ( \mathrm { P G L } _ { \mathsf { D } + 1 } \big ) ,$ ).

# 4. EXAMPLES

We begin with some simple examples in the first section, and then present the ones that principally guided each of us to the theory of branchvarieties.

4.1. Further elementary examples.
In the examples below, we take $\begin{array} { r } { \mathsf { A } = \mathbb { C } [ [ \mathsf { t } ] ] } \end{array}$ , with K its field of fractions.

Example 4.1. Consider two skew lines in $\mathbb { A } ^ { 3 }$ approaching each other as $\begin{array} { r } { \mathrm { ~  ~ t ~ }  \ 0 : \ { \sf R } \ = \ } \end{array}$ $A [ x , y , z ] / ( z , x ) \cap ( z - \mathrm { t } , y )$ . The central fiber

$$
A [ x , y , z ] / ( x y , z ^ { 2 } , z x , z y )
$$

is two lines with an embedded prime at the point of intersection, and is not reduced.
No ramification is necessary in this case (as follows from Theorem 2.5, since the central fiber is generically reduced).
The integral closure is the union of two disjoint families of lines

$$
\widetilde { \mathsf { R } } = \mathsf { A } [ { \boldsymbol { x } } , { \boldsymbol { y } } , z ] / ( z , x ) \oplus \mathsf { A } [ { \boldsymbol { x } } , { \boldsymbol { y } } , z ] / ( z - \mathrm { t } , \boldsymbol { y } ) .
$$

The central fiber is a disjoint union of two lines, with a finite map to the two intersecting lines in $\mathbb { A } ^ { 3 }$ .

The total space of the Hilbert family Spec R is the union of two planes meeting at a point, everyone’s first example of a scheme smooth in codimension 1 yet still abnormal: it is not S2, and a hyperplane section has an embedded prime.
The integral closure just pulls those two planes apart.

Example 4.2. Let X be a union of 3 copunctal lines in $\mathbb { P } ^ { 2 }$ , say with slopes 0, 1, and $\infty _ { \ast }$ , and let $\mathsf { f } _ { \mathrm { t } } : \mathsf { X } \to \mathbb { P } ^ { 1 }$ be a projection with the angle t. The tangent space to the common point is 2-dimensional, and contains four 1-d subspaces: the tangents to the lines, and the kernel of the derivative of $\mathsf { f } _ { \mathrm { t } }$ . In these terms, t is a cross-ratio.
Consider this as a 1-parameter family as $\mathrm { t }$ goes to 0.

In coordinates, the generic fiber $X _ { \mathfrak { \eta } }$ corresponds to a graded ring R which is a subring of $\mathsf { K } [ \mathsf { x } _ { 0 } , \mathsf { x } _ { 1 } ] \oplus \mathsf { K } [ \mathsf { y } _ { 0 } , \mathsf { y } _ { 1 } ] \oplus \mathsf { K } [ \mathsf { z } _ { 0 } , \mathsf { z } _ { 1 } ]$ consisting of homogeneous polynomial $( \mathsf { f } , \mathsf { g } , \mathsf { h } )$ such that

$$
\mathbf { \boldsymbol { \mathsf { f } } } ( 1 , 0 ) = \mathbf { \boldsymbol { \mathsf { g } } } ( 1 , 0 ) = \mathbf { \boldsymbol { \mathsf { h } } } ( 1 , 0 ) , \qquad \mathbf { \boldsymbol { \mathsf { t f } } } ^ { \prime } ( 1 , 0 ) + \mathbf { \boldsymbol { \mathsf { g } } } ^ { \prime } ( 1 , 0 ) = ( 1 + \mathbf { \boldsymbol { \mathsf { t } } } ) \mathbf { \boldsymbol { \mathsf { h } } } ^ { \prime } ( 1 , 0 ) ,
$$

where the derivatives are with respect to the second variable, $x _ { 1 } , y _ { 1 }$ or $z _ { 1 }$ respectively.
The $\mathsf { K } [ \mathsf { t } _ { 0 } , \mathsf { t } _ { 1 } ]$ -module structure is given by the homomorphisms $\mathfrak { t } _ { \mathrm { i } } \mapsto ( { \tt x } _ { \mathrm { i } } , { \tt y } _ { \mathrm { i } } , z _ { \mathrm { i } } )$ .

We can use the same equations for the total family $\Sigma ,$ replacing $\mathsf { K }$ by A. Specializing $\mathrm { t } = 0$ , one obtains the ring of triples $( \mathsf { f } , \mathsf { g } , \mathsf { h } )$ such that

$$
{ \sf f } ( 1 , 0 ) = { \sf g } ( 1 , 0 ) = { \sf h } ( 1 , 0 ) , \qquad { \sf g } ^ { \prime } ( 1 , 0 ) = { \sf h } ^ { \prime } ( 1 , 0 ) ,
$$

Hence, the central fiber $X _ { 0 }$ is a union of three $\mathbb { P } ^ { 1 } \mathbf { s }$ passing through one point, the second and the third $\mathbb { P } ^ { 1 } \mathbf { s }$ are tangent to each other, and the first is transverse to them.
Note that $X _ { 0 }$ can no longer be embedded in $\mathbb { P } ^ { 2 }$ .

Example 4.3. We will assume for simplicity that char $\mathtt { k } \neq 2$ in this example.

Consider the space of branchvarieties of $\mathbb { P } ^ { 2 }$ including the plane conics, so $\mathtt { h } ( \mathtt { n } ) = 2 \mathtt { n } + 1$ , ${ \bf b } _ { 0 } = 0 ,$ , $\mathtt { b } _ { 1 } = 2$ . In short, this coarse moduli space is the “space of complete conics”, or $\mathbb { P } ^ { 5 }$ blown up along the Veronese surface, while the stack structure agrees with that on the corresponding Kontsevich moduli space of stable maps.
Indeed, each branchcurve X has arithmetic genus 0, and so has at worst nodes as singularities.
We include some standard facts about this stack.

There are two obvious closed substacks: ${ \textsf { T } } = \left\{ \begin{array} { r l r l } \end{array} \right.$ {reducible branchvarieties} and ${ \textsf { N } } =$ {noninjective branchvarieties}. Each of the points in the substack $\mathsf { N }$ has automorphism group $\mathbb { Z } / ( 2 )$ . The complementary set ${ \mathsf { N } } ^ { { \mathsf { c } } }$ corresponds to reduced plane conics, has trivial stack structure, and is isomorphic as a space to $\mathbb { P } ^ { 5 }$ with the Veronese surface removed.
The set $\mathsf { T } ^ { \mathrm { c } } \cap \mathsf { N }$ consists of double covers $\bar { \mathbb { P } } ^ { 1 } \to \mathbb { P } ^ { 1 }$ of lines; such a cover is uniquely determined by its image line and the two (distinct) branch points.
If we let the branch points collide, we get the space $\mathsf { T } \cap \mathsf { N }$ consisting of pairs of crossing lines double covering a line in $\mathbb { P } ^ { 2 }$ .

The whole space is 5-dimensional.
The substack $\mathsf { N }$ is 4-dimensional.
The substack T ∩N is 3-dimensional, and isomorphic as a stack to the manifold of flags in $\mathbb { P } ^ { 2 }$ modulo a trivial $\mathbb { Z } / ( 2 )$ action.

In the case of plane cubics, the moduli stacks of branchcurves and of stable maps are not naturally isomorphic, which we will see in Section 8.1.

Example 4.4. Fix ${ \mathfrak { g } } \in \mathbb { N } ,$ , and let $\mathfrak { h } = 2 \mathfrak { n } + 1 - \mathfrak { g } , \mathfrak { b } _ { 0 } = 0 , \mathfrak { b } _ { 1 } = 2 .$ . We can make some of the branchcurves of $\mathbb { P } ^ { 1 }$ with these invariants by joining two $\mathbb { P } ^ { 1 } \mathbf { s }$ along $9 + 1$ distinct points; the arithmetic genus of such a curve is g.

The generic branchcurve of $\mathbb { P } ^ { 1 }$ with these invariants is a smooth curve of genus $^ { 9 , }$ branched over $\mathbb { P } ^ { 1 }$ at $2 ( 9 + 1 )$ points, and the coarse moduli space is just

$$
( \mathbb { P } ^ { 1 } ) ^ { 2 ( { 9 + 1 } ) } / \mathrm { S } _ { 2 ( { 9 + 1 } ) } \cong \mathbb { P } ^ { 2 ( { 9 + 1 } ) } .
$$

For example, consider ${ \mathfrak { g } } = 1$ , so the generic branchcurve is an elliptic curve branched over $\mathbb { P } ^ { 1 }$ at four distinct points.
If two branch points coalesce, $4 = 2 + 1 + 1$ , the branchcurve is a nodal cubic with the node mapping to the double branch point.
If the other two coalesce also, $4 = 2 + 2 ,$ the branchcurve is as described a moment ago – two $\mathbb { P } ^ { 1 } \mathbf { s }$ glued together at two points.
If three branch points coalesce, $4 = 3 + 1 ,$ , the branchcurve is a cuspidal cubic with the cusp mapping to the triple branch point.
If all four coalesce, the branchcurve is a union of two $\mathbb { P } ^ { \bar { 1 } } \bar { \mathbf { s } }$ along a point of tangency.

We note that the moduli space of branchvarieties of $\mathbb { P } ^ { 1 }$ contains the classical Hurwitz schemes parametrizing degree $\mathrm { d }$ covers of $\mathbb { P } ^ { 1 }$ with certain ramification conditions.
We see from the above example that the compactification of these Hurwitz schemes provided by branchvarieties is very different from the compactification obtained by adding “admissible covers” as done, e.g., in [HM82].

4.2. Stable toric varieties.
Let ${ \sf T } = ( \mathbb { G } _ { \mathrm { m } } ) ^ { \sf r }$ be a split multiplicative torus, a direct sum of r copies of the multiplicative group $\mathbb { G } _ { \mathrm { m } }$ . Let $\mathbb { P } ^ { { \mathfrak { n } } }$ be a projective space endowed with a T-action and with a T-linearized $\mathcal { O } ( 1 )$ .

Definition 4.5. A stable toric variety over $\mathbb { P } ^ { { \mathfrak { n } } }$ over an algebraically closed field is a seminormal projective variety $\boldsymbol { x }$ endowed with a T-action such that

(1) there are only finitely many orbits, and (2) the isotropy groups are subtori, so in particular connected and reduced together with a finite and $\intercal$ -equivariant morphism f $: X \to \mathbb { P } ^ { \mathfrak { n } }$ .

When T acts on $( \mathbb { P } ^ { \mathrm { n } } , \mathcal { O } ( 1 ) )$ with $\mathfrak { n } + 1$ distinct characters, the data for the morphism $\mathbf { f } : {  { \mathbb { X } } } \to {  { \mathbb { P } } } ^ { \mathfrak { n } }$ is equivalent to the data for an effective ample Cartier divisor $_ \mathrm { D }$ on $\boldsymbol { x }$ which does not contain any ${ \sf T }$ -orbits.
So, in this case a stable toric variety over $\mathbb { P } ^ { { \mathfrak { n } } }$ is the same as a stable toric pair $( \mathsf { X } , \mathsf { D } )$ with a T-linearized line bundle ${ \sf L } = \mathcal { O } _ { \sf X } ( { \sf D } )$ , see [Ale02, 2.14], [AB05, Prop. 3.3.2]. The latter paper also includes the more general case of stable spherical varieties, where $\intercal$ is replaced by a reductive group.

The higher cohomologies $\mathsf { H } ^ { \mathrm { i } } ( \mathsf { X } , \mathsf { L } ^ { \mathrm { d } } )$ vanish for $\mathrm { ~ d ~ } > 0$ . Therefore, for every family $x $ $\mathbb { P } _ { S } ^ { \mathrm { n } }$ of stable toric varieties the graded $\mathcal { O } _ { S }$ -algebra ${ \sf R } ( X / { \sf S } , { \sf L } ) = \oplus _ { \tt d \geq 0 } \pi _ { * } { \tt L } ^ { \tt d }$ is locally free.
The T-action is equivalent to the grading of $\mathsf { R } ( { \mathsf { X } } / { \mathsf { S } } , { \mathsf { L } } )$ by the character group $\Lambda = \mathbb { Z } ^ { \mathrm { r } }$ of ${ \sf T }$ , and each graded piece $\mathsf { R } ( { \boldsymbol { \mathrm { X } } } / { \mathsf { S } } , { \mathsf { L } } ) _ { \lambda } , \lambda \in \bar { \Lambda } ,$ is of finite rank $\mathrm { h } ( \lambda ) .$ , i.e. ${ \sf R } ( { \sf X } / { \sf S } , { \sf L } )$ is multiplicityfinite.
When ${ \sf R } ( { \sf X } / { \sf S } , { \sf L } )$ is multiplicity-free, i.e. each $\boldsymbol { \mathrm { h } } ( \lambda )$ is 0 or 1, a stronger statement is true: X reduced implies that $\boldsymbol { x }$ is seminormal.

We see that the moduli of multiplicity-free stable toric varieties over $\mathbb { P } ^ { { \mathfrak { n } } }$ is just the branch-analogue of the toric Hilbert scheme of Peeva-Stillman [PS02] and the more general multigraded Hilbert scheme of Haiman-Sturmfels [HS04].

This “toric Branch” moduli space is constructed in [AB05] more directly, as the quotient $\mathsf { U } / \mathsf { r }$ of $\begin{array} { r } { \mathsf { U } = \operatorname { H i l b } _ { \mathsf { h } } ( Z ) . } \end{array}$ , where $Z \to \mathbb { P } ^ { \mathrm { n } }$ is an A-cover, by a finite diagonalizable group, i.e. product of several groups $\mu _ { \mathrm { m } }$ of roots of unity.
The reason for the relative simplicity of this case is that the monic polynomials appearing in the finite ring extensions have the very simple form $z ^ { \mathfrak { m } } = { \mathfrak { r } }$ . The projectivity of the moduli space is immediate from this description.

Since some of the varieties appearing below in Section 8 are stable toric varieties, we recall briefly their classification.
Each stable toric variety over an algebraically closed field defines a complex of polytopes $\Delta$ with a reference map to $\Lambda _ { \mathbb { R } }$ . This means that we have a topological space $| \Delta |$ with a cell decomposition $| \bar { \Delta } | = \cup \delta$ and a finite map $\rho : | \Delta |  \Lambda \otimes { \overline { { \mathbb { R } } } }$ identifying each δ with a lattice polytope.
Then X is a union of ordinary (normal) projective toric varieties $X _ { \delta }$ which are glued the same way as the complex $\Delta$ .

A variety $\boldsymbol { x }$ is multiplicity-free precisely when the map $\rho$ is injective.
One-parameter degenerations correspond to convex subdivisions of $\Delta$ .

4.3. Balanced normal cones.
Let Q be a commutative $\boldsymbol { \mathrm { k } }$ -algebra without nilpotents, and I an ideal.
The Rees algebra is the graded subring

$$
{ \sf R } = \left( \bigoplus _ { { \mathfrak { n } } < 0 } { \mathfrak { t } } ^ { - { \mathfrak { n } } } { \mathrm { I } } ^ { \mathfrak { n } } \right) \oplus \left( \bigoplus _ { { \mathfrak { n } } \geq 0 } { \mathfrak { t } } ^ { \mathfrak { n } } { \mathrm { Q } } \right)
$$

of $\mathrm { Q } [ \mathrm { t } , \mathrm { t } ^ { - 1 } ]$ . Under the evident map $\mathbb { k } [ { \sf t } ]  \ \mathbb { R } ,$ we see that the map Spec $\mathsf { R } \to \mathrm { S p e c } \mathsf { k } [ \mathsf { t }$ ] defines a flat family whose $\mathrm { t } = 1$ fiber is $\mathrm { Q }$ and $\mathrm { t } = 0$ fiber is $\begin{array} { r } { \mathrm { g r } _ { \mathrm { I } } \mathrm { Q } : = { \hat { \mathrm { Q } } } / \mathrm { I } \oplus \mathrm { I } / \mathrm { I } ^ { 2 } \oplus \mathrm { I } ^ { 2 } / \mathrm { I } ^ { 3 } \oplus . . . , } \end{array}$ the associated graded with respect to the I-adic filtration.
If we assume in addition that $\cap _ { \mathfrak { n } } \operatorname { I } ^ { \mathfrak { n } } = \{ 0 \} ,$ then this family is locally free.
Geometrically, this family is the degeneration of Spec Q to the normal cone of Spec $\mathrm { Q } / \mathrm { I }$ .

In [Sam52], Samuel defined a variant of the I-adic filtration

$$
\forall { \mathfrak { q } } \in \mathrm { Q } , \quad { \mathfrak { f } } ( { \mathfrak { q } } ) : = \operatorname* { m a x } \{ \mathfrak { n } : { \mathfrak { q } } \in { \Gamma } ^ { \mathfrak { n } } \}
$$

called its homogenization,

$$
\forall \mathbf { q } \in \mathbf { Q } , \quad \overline { { \mathbf { f } } } ( \mathbf { q } ) : = \operatorname* { l i m } _ { \mathbf { k } \to \infty } \frac { \mathbf { f } ( \mathbf { q } ^ { \mathbf { k } } ) } { \mathbf { k } } ,
$$

and proved that this limit exists.
Rees (see the book [Ree88]) and Nagata $[ \mathrm { N a g } 5 7 ]$ proved that the limit is rational with bounded denominator (depending on $\mathrm { Q } , \mathrm { I } )$ . Let $\mathsf { N }$ be divisible by all the possible denominators of ${ \overline { { \mathsf { f } } } } _ { j }$ ; of course their LCM will do.

To this “homogeneous” filtration ${ \overline { { \mathsf { f } } } } ,$ one can again associate a Rees algebra (now $\frac { 1 } { \mathsf { N } } \mathbb { N } -$ graded) giving a flat degeneration of $\mathrm { Q }$ to an associated graded ring $\overline { { \mathrm { g r } } } _ { \mathrm { I } } { \sf R } ,$ this time automatically without nilpotents.
The corresponding geometry was studied in [Knu05] under the name “degeneration to the balanced normal cone”.

We now relate this construction to the one in Section 2. Make the ramified base change $\mathrm { \Delta t = \Psi ( t ^ { \prime } ) ^ { N } }$ . Let $\widetilde { \sf R }$ denote the integral closure of $\mathsf { R }$ in $\begin{array} { r } { \mathsf { R } \otimes _ { \mathsf { k } [ \mathsf { t } ] } \mathsf { k } [ \mathsf { t } ^ { \prime } ] \subseteq \mathsf { Q } [ \mathsf { t } , \mathsf { t } ^ { - 1 } ] \otimes _ { \mathsf { k } [ \mathsf { t } ] } \mathsf { k } [ \mathsf { t } ^ { \prime } ] = } \end{array}$ $\mathrm { Q } [ \mathrm { t } ^ { \prime } , \mathrm { t } ^ { \prime - 1 } ]$ . Then for ${ \mathfrak { n } } \geq 0$ ,

$$
\begin{array} { r } { \begin{array} { r l } { \mathfrak { q } / \mathfrak { t } ^ { \prime \mathfrak { n } } \in \widetilde { \mathsf { R } } \ \iff } & { \mathfrak { q } / \mathfrak { t } ^ { \prime \mathfrak { n } } \mathrm { i s ~ i n t e g r a l ~ o v e r ~ } \mathsf { R } } \\ { \iff } & { ( \mathfrak { q } / \mathfrak { t } ^ { \prime \mathfrak { n } } ) ^ { \mathsf { N } } \mathrm { i s ~ i n t e g r a l ~ o v e r ~ } \mathsf { R } } \\ { \iff } & { \mathfrak { q } ^ { \mathsf { N } } / \mathfrak { t } ^ { \mathsf { n } } \mathrm { i s ~ i n t e g r a l ~ o v e r ~ } \mathsf { R } } \\ { \implies } & { \overline { { \mathsf { f } } } ( \mathfrak { q } ) \geq \mathfrak { n } / \mathsf { N } . } \end{array} } \end{array}
$$

By Rees’ valuative formula for $\overline { { \mathsf { f } } }$ [Ree88, Thm. 4.16], the converse of this last implication is also true.
Hence

$$
{ \widetilde { \mathsf { R } } } = \left( \bigoplus _ { \mathfrak { n } < 0 } \mathfrak { t ^ { \prime - \mathfrak { n } } } \{ \mathsf { q } : { \overline { { \mathsf { f } } } } ( \mathfrak { q } ) \geq \mathfrak { n } / \mathsf { N } \} \right) \oplus \left( \bigoplus _ { \mathfrak { n } \geq 0 } \mathfrak { t ^ { \prime \mathsf { n } } } \mathbf { Q } \right)
$$

is the Rees algebra associated to the filtration given by $\overline { { \mathsf { f } } }$ .

Craig Huneke informed us that much the same interpretation of Rees’ results on the Samuel filtration occurs in Theorem 10.6.6 of his forthcoming book [HuSw06].

4.4. Chiriv\`ı’s degeneration of flag manifolds as a limit of branchvarieties. We describe a special case of Chiriv\`ı’s geometric interpretation of the Littelmann-Lakshmibai-Seshadri weight multiplicity formula [Chi00], using the language of balanced normal cones.
This example was what motivated the second author to seek a general theory of automatically reduced degenerations.
The details will appear elsewhere [Knu06].

Let G be a complex connected algebraic group with maximal torus ${ \sf T }$ , and $\lambda$ a dominant weight.
Then there is a natural $G$ -equivariant graded ring structure on $\mathsf { R } : = \oplus _ { \mathsf { n } \in \mathbb { N } } \mathsf { V } _ { \mathsf { n } \lambda }$ (the nth piece being the irreducible representation of G with high weight nλ), whose Proj is a generalized flag manifold $\mathsf { G } / \mathsf { P }$ .

Through a careful analysis of generators and relations of the ring R, Chiriv\`ı gave a collection of T-equivariant degenerations $\mathsf { R } ^ { \prime }$ of R, where each Proj $\mathsf { R } ^ { \prime }$ is a stable toric variety. In some cases, the underlying complex $\Delta$ of polytopes is in fact a simplicial complex, with one simplex for each chain in the Bruhat order of $\mathsf { G } / \mathsf { P } .$ ; we will call this a simplicial Chiriv\`ı degeneration.

This degeneration was already well known in the case that $\mathsf { G } / \mathsf { P }$ is a Grassmannian in its Pl ¨ucker embedding [DEP82]. In this case, each component of the stable toric variety maps isomorphically, not just finitely, to a coordinate subspace of projective space.

By the flatness of these degenerations, one can compute the T-weight multiplicities in the representation ${ \sf V } _ { \lambda }$ as a sum over chains in the Bruhat order, and for each chain, a count of lattice points in a certain simplex (determined using $\lambda$ ). This weight multiplicity formula had already been proven by Littelmann using his path model, confirming a conjecture of Lakshmibai and Seshadri (inspired by [DEP82] and followup work [DL81] generalizing it to other minimal embeddings of minimal classical flag manifolds).

We now sketch a way to see a simplicial Chiriv\`ı degeneration as a flat limit of branchvarieties, with proofs to appear in [Knu06]. The principal benefit of this viewpoint is that the construction does not require special analysis of the ring R.

The extremal weights of ${ \sf V } _ { \lambda }$ are of the form $w \cdot \lambda$ for $_ w$ in the Weyl group of G. Each extremal weight space is 1-dimensional; let $\mathsf { E } \leq \mathsf { V } _ { \lambda }$ be their direct sum.
Then we make ${ \sf G } / { \sf P } = \mathrm { P r o j } \breve { \sf R }$ a branchvariety of projective space, using the map Proj ${ \sf R }  \mathrm { P r o j } \mathrm { S y m } { \sf E } .$ (Indeed, E is the smallest ${ \sf T }$ -invariant subspace such that this map has no basepoints.)

The Bruhat order of $\mathsf { G } / \mathsf { P }$ gives a natural partial order on the extremal weights; pick a linear extension (which will be immaterial) to a total order.
Running through the sequence of extremal weights, we get a series of degenerations to balanced normal cones

$$
\begin{array} { r l r l r l r l r l } { \mathsf { R } } & { { } \to \to } & { \overline { { \mathbb { g r } } } _ { \mathrm { I _ { 1 } } } \mathsf { R } } & { } & { \to \to } & { \overline { { \mathbb { g r } } } _ { \mathrm { I _ { 2 } } } \overline { { \mathbb { g r } } } _ { \mathrm { I _ { 1 } } } \mathsf { R } } & { } & { \to \to } & { } & { \dots } & { } & { \to \overline { { \mathbb { g r } } } _ { \mathrm { I _ { m } } } \cdot \cdot \cdot \overline { { \mathbb { g r } } } _ { \mathrm { I _ { 1 } } } \mathsf { R } } & { } & { } & { } & { } \end{array}
$$

where the ideal $\mathrm { I _ { k } }$ is generated by the kth extremal weight space in the total order (or rather, by the image of that extremal weight space in the $( \ k - 1 )$ st ring in the sequence).

Since these ideals are ${ \sf T }$ -invariant, the degenerations are ${ \sf T }$ -equivariant.
Each component of the resulting scheme is a weighted cone on a weighted cone on . . . on a point, i.e. a toric variety associated to a weighted simplex.

It is reasonably straightforward to show that the final ring so constructed is a subring of Chiriv\`ı’s “discrete LS algebra” $\mathsf { R } ^ { \prime }$ . One can then e.g. invoke Littelmann’s result to show they are equal.

# 5. LINE BUNDLES ON BRANCH

By Section 1, for any ${ \mathrm { ~ d ~ } } \geq { \mathrm { ~ d } } _ { 0 }$ the sheaves ${ \mathrm { ~ L } } ^ { \mathrm { d } }$ on our branchvarieties do not have higher cohomology.
Therefore, for any family $\mathrm { f } : X  \Upsilon _ { S } , \pi : X  S ,$ the sheaves $\mathsf { F } _ { \mathrm { d } } = \bar { \pi } _ { * } \mathrm { L } ^ { \mathrm { d } }$ are locally free, and they induce natural line bundles $\lambda _ { \mathrm { d } } = \operatorname* { d e t } \mathsf { F } _ { \mathrm { d } }$ on our moduli stacks.
One might therefore hope (cf.
[Kol90] for a quite similar situation) that these line bundles are ample.
(In particular, this would immediately imply that the coarse moduli spaces of branchvarieties are projective schemes.)
So, the following is a somewhat surprising observation.

Example 5.1. Consider the moduli space of 1-dimensional branchvarieties of $\mathbb { P } ^ { 2 }$ which include the plane cubics.
For any family $\mathbf { f } :  { \mathbb { X } } \to  { \mathbb { P } } _ { S } ^ { 2 }$ whose fibers are reduced planar cubics, each $\lambda _ { \mathrm { d } } | _ { S }$ has a positive degree.
Indeed, this part of the branchvariety moduli coincides with part of the Hilbert scheme, and $\lambda _ { \mathrm { d } }$ is the pullback of the (very ample) standard line bundle on a Grassmannian into which the Hilbert scheme is embedded.

On the other hand, consider the family over $S = \mathbb { P } ^ { 1 }$ of Example 4.2 (see also Section 8.1). In this family, ${ \mathcal { O } } _ { X }$ is embedded into $\mathcal { O } _ { \widetilde { \chi } } = \oplus _ { \mathrm { i } = 1 } ^ { 3 } \mathcal { O } _ { \mathbb { P } ^ { 1 } }$ , for the normalization $\widetilde { x }$ of $\Sigma ,$ and the induced morphism $\widetilde { X }  \Upsilon = \mathbb { P } ^ { 1 }$ is constant.
Therefore, each $\mathsf { F } _ { \mathsf { k } }$ is a nonconstant subbundle of a constant vector bundle $\oplus _ { \mathrm { i = 1 } } ^ { 3 } \mathsf { H } ^ { \circ } ( \mathbb { P } ^ { 1 } , \mathcal { O } ( \mathsf { d } ) ) \otimes \mathcal { O } _ { S }$ . Hence, $\lambda _ { \mathrm { d } } | _ { S }$ has a negative degree!

Remark 5.2. We do not claim that the moduli spaces $\mathrm { B r a n c h } _ { \mathrm { h , Y } } ^ { \mathrm { b } }$ are not projective.
In particular, it seems possible that for $\mathrm { d } , \mathrm { k } \gg 0$ the line bundles $\lambda _ { \mathbf { d k } } { \overset { \cdot } { \otimes } } \lambda _ { \mathbf { d } } { } ^ { - ( \deg \mathsf { h } - 1 / 2 ) \mathbf { k } }$ on Branchbh,Y are ample.
See also Theorem 9.3, which gives a large set of projective examples.

# 6. K-CLASSES OF DEGENERATIONS

We follow the notation of Section 2. Fix a projective dimension n, a Hilbert function $\mathsf { h } ,$ an $\mathbb { N } .$ -graded locally free A-algebra ${ \sf R }$ , and a homomorphism $\boldsymbol { A } [ x _ { 0 } , \ldots , x _ { n } ]  \mathbb { R }$ making R a finite $A [ x _ { 0 } , \ldots , x _ { \mathrm { n } } ]$ -module.
Let $\mathsf { R } ^ { \prime }$ be the integral closure of R in $\mathsf { R } \otimes _ { \mathsf { A } } \mathsf { K }$ .

Since R and $\mathsf { R } ^ { \prime }$ are finite modules over $A [ x _ { 0 } , \ldots , x _ { n } ] ,$ , we see that ${ \sf R } / { \sf t R }$ and $\mathsf { R } ^ { \prime } / \mathrm { t } \mathsf { R } ^ { \prime }$ are finite modules over $\mathbb { k } [ \mathbb { x } _ { 0 } , . . . , \mathbb { x } _ { \mathrm { n } } ]$ , and define elements of algebraic K-homology of $\mathbb { k } [ x _ { 0 } , \ldots , x _ { n } ]$ . Since R and $\mathsf { R } ^ { \prime }$ are both locally free and agree after inverting t, these two elements $[ { \sf R } / { \sf t R } ]$ , $[ { \sf R } ^ { \prime } / { \sf t } { \sf R } ^ { \prime } ]$ of K-homology coincide.
We now give a direct proof of this $\mathsf { K }$ -equivalence, allowing us to strengthen the statement.

Proposition 6.1. Let t be a non-zero-divisor in ${ \sf R } ,$ and let $\mathsf { R } ^ { \prime }$ stand between R and its integral closure in $\mathsf { R } [ \mathsf { t } ^ { - 1 } ]$ . Assume that $\mathsf { R } ^ { \prime }$ is finite over R (e.g. if R is finitely generated over a DVR A).

Then ∃ $\mathsf N > 0$ such that ${ \sf R } / { \sf t R }$ and $\mathsf { R } ^ { \prime } / \mathrm { t } \mathsf { R } ^ { \prime }$ are K-equivalent modules over the ring $\mathsf { R } / ( \mathsf { t } ^ { \mathsf { N } } )$ .

Proof.
Consider the short exact sequences of R-modules

$$
0 \to \mathbb { R } / \mathrm { t R } \to \mathbb { R } ^ { \prime } / \mathrm { t R } \to \mathbb { R } ^ { \prime } / \mathrm { R } \to 0
$$

$$
0  \mathrm { t R ^ { \prime } / t R }  \mathrm { R ^ { \prime } / t R }  \mathrm { R ^ { \prime } / t R ^ { \prime } }  0
$$

Since t is not a zero divisor, the natural map $\mathsf { R } ^ { \prime } / \mathsf { R } \longrightarrow \mathsf { t R } ^ { \prime } / \mathsf { t R }$ is an isomorphism.
So we get the $\mathsf { K }$ -equation

$$
[ \mathsf { R } / \mathsf { t R } ] = [ \mathsf { R } ^ { \prime } / \mathsf { t R } ] - [ \mathsf { R } ^ { \prime } / \mathsf { R } ] = [ \mathsf { R } ^ { \prime } / \mathsf { t R } ] - [ \mathsf { t R } ^ { \prime } / \mathsf { t R } ] = [ \mathsf { R } ^ { \prime } / \mathsf { t R } ^ { \prime } ] .
$$

By the assumptions on ${ \sf R ^ { \prime } }$ , there exists an $\mathsf { N }$ such that $\mathsf { t } ^ { \mathsf { N } - 1 } \mathsf { R } ^ { \prime } \subset \mathsf { R }$ . Therefore $\mathrm { t } ^ { \mathsf { N } }$ annihilates all of these modules, so they are modules over the ring $\mathsf { R } / ( \mathsf { t } ^ { \mathsf { N } } )$ , and the derivation of this K-equation holds there.


The fact that ${ \sf R } / { \sf t R }$ and $\mathsf { R } ^ { \prime } / \mathrm { t } \mathsf { R } ^ { \prime }$ have the same Hilbert polynomial says only that they define K-equivalent sheaves on $\mathbb { P } ^ { { \mathfrak { n } } }$ . Both sheaves are supported on thickenings of the same subvariety.
The above Proposition says that they are already K-equivalent on some larger thickening of this same variety.

Note that there is a ring homomorphism ${ \sf R } / ( { \sf t } )  { \sf R } ^ { \prime } / ( { \sf t } )$ . Hence, given a family over Spec K of subvarieties of projective space, there is a map from the limit branchvariety to the limit subscheme inducing this K-equivalence.

Example 6.2. Recall the colliding skew lines from Example 4.1. In this case, Proj $\mathsf { R } ^ { \prime } / ( \mathsf { t } )$ i s the two disjoint lines and Proj R/(t) has the lines crossing with an extra point embedding at the cross.
If $\pi : { \mathrm { P r o j } } \mathrm { R } ^ { \prime } / ( \mathrm { t } ) \to { \mathrm { P r o j } } \mathrm { R } / ( \mathrm { t } )$ denotes the obvious collapse, then $\pi _ { * }$ of the structure sheaf on the two lines is K-equivalent, but not isomorphic, to the structure sheaf of Proj R/(t).

The map ${ \sf R } / ( { \sf t } )  { \sf R } ^ { \prime } / ( { \sf t } )$ was studied in [Knu05] (where one can find many more examples) in the balanced normal cone context of Section 4.3. A principal result of that paper was that the corresponding map from the balanced normal cone to the ordinary normal cone takes the fundamental Chow class to the fundamental Chow class, a consequence of this lemma.

# 7. THE FOREST OF A BRANCHVARIETY

Hartshorne proved [Har66] that Hilbert schemes are connected.
This is in some sense a negative result; it says that the only locally constant invariants are the embedding dimension n and the Hilbert polynomial h. We already proved in Lemma 1.3 that for branchvarieties, the degree sequence b is an additional such invariant.
In this section we develop a still finer invariant, assuming the characteristic is 0 or large enough.

Lemma 7.1. Let f : $x \to \mathbb { P } _ { s } ^ { n }$ be a family of branchvarieties.
Then the number of connected components (not irreducible components) of X is locally constant.

Proof.
It is sufficient to assume that S is a germ of a one-dimensional scheme, for example the Spec of a DVR. Let $X _ { \mathfrak { \eta } }$ be the generic fiber.
Make a ramified base change $A ^ { \prime } \supset A$ so that the connected components of $X _ { \mathfrak { n } } \otimes _ { \mathbf { k } _ { \mathfrak { n } } } \overline { { \mathbf { k } } } _ { \mathfrak { n } }$ are already defined over $A ^ { \prime }$ ; call them $X _ { \mathrm { i } }$ . Then $\coprod X _ { \mathrm { i } } \longrightarrow X$ is finite and they have the same generic fiber, so by the separatedness of Branch (Corollary 2.2) these two spaces coincide.


As Example 4.1 of the two colliding lines shows, this is not an invariant for connected families of subschemes (it only behaves semicontinuously).

Assumption 7.2. Now let us fix a Hilbert polynomial $\boldsymbol { \mathrm { h } } ( \mathrm { d } )$ and a sequence of nonnegative integers $\boldsymbol { \mathsf { b } } = ( \boldsymbol { \mathsf { b } } _ { 0 } , \ldots , \boldsymbol { \mathsf { b } } _ { \mathrm { d e g h } } )$ . For the rest of this section we will assume that our base scheme C is defined over $\mathbb { Z } [ 1 / ( \operatorname* { m a x } { \mathfrak { b } } _ { \mathrm { i } } ) ! ]$ ]. In other words, all prime numbers ${ \mathfrak { p } } \leq \operatorname* { m a x } { \mathfrak { b } } _ { \mathrm { i } }$ are invertible, and in particular any field over C either has characteristic zero or char ${ \boldsymbol { \mathrm { k } } } =$ ${ \mathfrak { p } } > \operatorname* { m a x } { \mathfrak { b } } _ { \mathrm { i } }$ . (For example, one can take C itself to be Spec of a field $\boldsymbol { \mathrm { k } }$ whose characteristic is 0 or some ${ \mathfrak { p } } >$ max $\mathtt { b } _ { \mathrm { i } }$ .)

With this assumption on characteristic, every generic plane section $X _ { \mathrm { i } }$ is reduced, hence is itself a branchvariety.

In this case, families of branchvarieties have some additional locally constant invariants.
For each connected component $\mathsf { X } ( \mathsf { j } )$ of $\Sigma ,$ the number of connected components of its general hyperplane section $\mathsf { X } ( \mathsf { j } ) _ { 1 }$ is locally constant, and we can continue by induction.

To organize this induction, recall first the definition of a rooted forest, which is a graph with no cycles and a choice of “root” vertex in each connected component.
The vertices of a rooted forest naturally form a ranked poset, where the rank of a vertex is the length of the unique path to a root, and $\nu \geq w$ if $\nu ^ { \prime } \mathrm { s }$ path to a root goes through w. Each component of a rooted forest, minus its root, is itself naturally a rooted forest whose roots are the neighbors of the old root.
This allows rooted forests to be described inductively.

Definition 7.3. Define the (labeled rooted) forest Forest(X) of a branchvariety X inductively as follows:

(1) $\begin{array} { r } { \mathrm { F o r e s t } ( \boldsymbol { X } ) = \prod _ { \boldsymbol { x } ( \mathfrak { j } ) } \mathrm { F o r e s t } ( \boldsymbol { X } ( \mathfrak { j } ) ) , } \end{array}$ , where $\{ \mathsf { X } ( \mathsf { j } ) \}$ are the connected components of X. (This includes the case $\ d \mathsf { X } = \emptyset .$ .)\
(2) If X is connected, then Forest $( \boldsymbol { \mathsf { X } } )$ has one root (so, it is also connected).
The label on the root is the integer $\chi ( \mathcal { O } _ { X } )$ , the constant term in the Hilbert polynomial.
Removing the root leaves $\mathrm { F o r e s t } ( X _ { 1 } )$ , where $X _ { 1 }$ is a general hyperplane section of $\boldsymbol { x }$ . (In order to have general enough hyperplanes, we work with the geometric fiber $x \otimes _ { \mathsf { k } } \bar { \mathsf { k } } . ,$ )

So each vertex $\nu$ has two numbers associated: its rank $\operatorname { r k } ( \nu )$ and its label $\chi ( \nu )$ . Also, if we have picked specific plane sections $x \supset X _ { 1 } \supset X _ { 2 } \supset$ . . . of X, then we can speak of the branchvariety associated to $\nu ,$ , meaning the corresponding connected component of $X _ { \mathrm { r k } ( \nu ) }$ . (By Assumption 7.2, this is again a branchvariety.)
In this way we can reduce arguments about a general vertex $\nu$ to the case that $\nu$ is a root, and the only one.

Proposition 7.4. Forest $( \boldsymbol { \mathsf { X } } )$ is locally constant in families of branchvarieties.
The Hilbert polynomial of $x$ and its degree sequence $\left( \mathsf { b } _ { \mathrm { i } } \right)$ can be computed from Forest(X) by the formulae

$$
\mathrm { h } _ { \mathrm { X } } ( \mathrm { d } ) = \sum _ { \substack { v \in \mathrm { F o r e s t } ( X ) } } \chi ( v ) \binom { \mathrm { d } + \mathrm { r k } ( v ) - 1 } { \mathrm { r k } ( v ) } , \qquad \mathrm { b } _ { \mathrm { i } } = t h e n u m b e r \circ f l e a v e s \ o f r a n k
$$

where $a$ leaf is a maximal element of the poset Forest(X).

Proof.
The first part follows from the argument in Lemma 7.1 applied to generic plane sections (which are again branchvarieties, by Assumption 7.2) and the invariance of the Hilbert polynomial in flat families.

For the Hilbert polynomial formula, it is enough to check that the two sides agree at $\mathrm { d } = 0$ (which is obvious) and also after applying the differencing operator $\Delta$ defined by $( \Delta g ) ( { \bf d } ) = { \bf g } ( { \bf d } ) - { \bf g } ( { \bf d } - 1 )$ . The left hand side is $\bar { ( \Delta \mathsf { h } _ { \mathsf { X } } ) } ( \bar { \mathsf { d } } ) = \mathsf { h } _ { X _ { 1 } } ( \bar { \mathsf { d } } )$ . The right hand is

$$
\begin{array} { r l } { \displaystyle \sum _ { v \in \mathrm { F o r e s t } ( X ) } \chi ( v ) \Delta \left( \begin{array} { l } { \mathrm { d } + \mathrm { r k } ( v ) - 1 } \\ { \mathrm { ~ \mathrm { r k } } ( v ) } \end{array} \right) } & { = \displaystyle \sum _ { v \in \mathrm { F o r e s t } ( X ) } \chi ( v ) \left( \begin{array} { l } { \mathrm { d } + \left( \mathrm { r k } ( v ) - 1 \right) - 1 } \\ { \mathrm { ~ \mathrm { r k } } ( v ) - 1 } \end{array} \right) } \\ & { = \displaystyle \sum _ { v \in \mathrm { F o r e s t } ( X _ { 1 } ) } \chi ( v ) \left( \begin{array} { l } { \mathrm { d } + \mathrm { r k } ( v ) - 1 } \\ { \mathrm { ~ \mathrm { r k } } ( v ) } \end{array} \right) } \end{array}
$$

which by induction is also $\mathrm { h } _ { X _ { 1 } } ( \mathrm { d } )$ .

A leaf corresponds to an isolated point of a plane section.
The degree of an irreducible component can be computed as the number of points in a generic plane section of complementary dimension, which implies the formula given for $\mathtt { b } _ { \mathrm { i } }$ . 

If we write the Hilbert polynomial and degree sequence associated to a forest F as $\mathtt { h } ( \mathsf { F } )$ and $\boldsymbol { \mathsf { b } } ( \mathsf { F } )$ , we can write

$$
\mathrm { B r a n c h } _ { \mathrm { h , Y } } ^ { \mathrm { b } } = \coprod _ { \mathrm { F : ~ b ( F ) = b , h ( F ) = h } } \mathrm { B r a n c h } _ { \mathrm { F , Y } }
$$

where BranchF,Y denotes the evident substack of $\mathrm { B r a n c h } _ { \mathrm { h , Y } } ^ { \mathrm { b } }$ . Note that this right-hand side is a finite union, since the left-hand side has only finitely many connected components by Theorem 0.4; only finitely many $\digamma$ with $\mathsf { b } ( \mathsf { F } ) = \mathsf { b } , \mathsf { h } ( \mathsf { F } ) = \mathsf { h }$ give nonempty BranchF,Y.

Example 7.5. If X is an irreducible branchvariety of dimension n and degree $\mathrm { d } ,$ then X’s forest looks like a lone palm tree, with one vertex of each rank $< \mathrm { ~ n ~ }$ and d vertices of rank n. More generally, $\boldsymbol { \chi } ^ { \prime } \boldsymbol { \mathrm { s } }$ forest is a palm tree iff $\boldsymbol { x }$ is equidimensional and connected in codimension 1.

Example 7.6. Consider two branchvarieties (indeed, reduced subschemes) of $\mathbb { P } ^ { 3 }$ :

(1) $\mathsf X = \mathsf X ( 1 ) \sqcup \mathsf X ( 2 ) .$ , where $\mathbf {  { X } } ( 1 ) , \mathbf {  { X } } ( 2 )$ are each a union of two copunctal lines; (2) $\mathsf X ^ { \prime } = \mathsf X ^ { \prime } ( 1 ) \sqcup \mathsf X ^ { \prime } ( 2 )$ , where $X ^ { \prime } ( 1 )$ is a line, and $X ^ { \prime } ( 2 )$ is a union of three lines that pass though a common point but do not lie in a common plane.

Then $\boldsymbol { x }$ and $X ^ { \prime }$ have the same Hilbert polynomial $\mathfrak { p } ( \mathrm { d } ) \ : = \ : 4 \mathrm { d } + 2$ and the same degree sequence ${ \mathfrak { b } } _ { 0 } = 0$ , $\mathtt { b } _ { 1 } = 4$ . However, Forest(X) consists of two trees with two leaves each, and Forest $( X ^ { \prime } )$ consists of a tree with three leaves and a tree with one leaf.
X and $X ^ { \prime }$ therefore belong to different connected components of Branch.

Example 7.7. Consider two branchvarieties of $\mathbb { P } ^ { 1 }$ :

(1) $\ X = X ( 1 ) \sqcup X ( 2 ) ,$ , where each of X(1), X(2) is a union of two tangent $\mathbb { P } ^ { 1 } \mathbf { s } _ { }$ ; (2) $\begin{array} { r } { X ^ { \prime } = X ^ { \prime } ( 1 ) \sqcup X ^ { \prime } ( 2 ) . } \end{array}$ , where $X ^ { \prime } ( 1 )$ is a union of two crossing $\mathbb { P } ^ { 1 } \mathbf { s }$ and $X ^ { \prime } ( 2 )$ is union of two $\mathbb { P } ^ { 1 } \mathbf { s }$ meeting in a triple point.

(Each irreducible component is degree 1 as a branchvariety.)

Then $\boldsymbol { x }$ and $X ^ { \prime }$ have the same Hilbert polynomial $\mathfrak { p } ( \mathrm { d } ) = 4 \mathrm { d } ,$ the same degree sequence ${ \mathfrak { b } } _ { 0 } = 0 .$ , $\mathtt { b } _ { 1 } = 4 ,$ , and the same unlabeled rooted forest.
However, the labels at the two roots of $\mathsf { F } ( { \boldsymbol { X } } )$ are $0 , 0$ and at the two roots of $\mathsf { F } ( \mathbf { \boldsymbol { X } } ^ { \prime } )$ are $+ 1 , - 1$ . $\boldsymbol { x }$ and $X ^ { \prime }$ therefore belong to different connected components of Branch.

Example 7.8. If $\digamma$ is a forest with all labels 1, then Proj of the Stanley-Reisner ring of the order complex of the poset F is a reduced subscheme of projective space whose forest is F. So every (finite) labeled rooted forest is, up to relabeling, the forest of some branchvariety.

However, not every labeling can occur; here is one of the simplest required conditions.
We give another necessary condition in Proposition 8.8.

Proposition 7.9. Let F be the forest of a branchvariety X, and v a vertex of F with only one leaf above it (not necessarily directly above).
Then the label on v is 1.

Proof.
We can reduce to the case that $\boldsymbol { x }$ is connected and $\nu$ is the root.
Then by Proposition 7.4, X is degree 1, so by Zariski’s Main Theorem the map $\mathbf { f } :  { \mathbb { X } } \to  { \mathbb { P } } ^ { \mathbf { n } }$ is the inclusion of a linear subspace.
Hence $\chi ( \nu ) = \chi ( \mathcal { O } _ { \mathbb { P } ^ { \mathrm { d i m } } } x ) = 1$ . 

Question 7.10. Let f be a rooted unlabeled forest.
Which labelings F of f actually arise as forests of branchvarieties?

The corresponding question for subschemes (namely, which polynomials can arise as Hilbert polynomials) was solved by Macaulay (see [Stn78, Gre89]).

Question 7.11. For those F that are forests of branchvarieties, is the open and closed subset BranchF,Pn of $\mathrm { B r a n c h } _ { \mathrm { h ( F ) , \mathbb { P } ^ { n } } } ^ { \mathrm { b ( F ) } }$ corresponding to a fixed forest F connected?

As we will see in Corollary 8.2 in the next section, this connectivity depends only on F and not the dimension of $\mathbb { P } ^ { { \mathfrak { n } } }$ (as long as n is greater than or equal to the maximum rank of ${ \sf F } ,$ for otherwise there are no branchvarieties).

Example 7.12. Abandon Assumption 7.2 on characteristics for this example.
Assume char $\mathtt { k } = \mathtt { p } > 0$ and consider a family of branchvarieties $x = \mathbb { P } ^ { 1 }$ of $\mathsf { Y } = \mathbb { P } ^ { 1 }$ parametrized by $S = \mathbb { A } _ { \mathrm { t } } ^ { 1 } ,$ with f given by the formula

$$
( { \mathfrak { x } } _ { 0 } , { \mathfrak { x } } _ { 1 } ) \mapsto ( \mathfrak { y } _ { 0 } = { \mathfrak { x } } _ { 0 } ^ { \mathfrak { p } } , \mathfrak { y } _ { 1 } = { \mathfrak { x } } _ { 1 } ^ { \mathfrak { p } } - \mathfrak { t } \cdot { \mathfrak { x } } _ { 1 } { \mathfrak { x } } _ { 0 } ^ { \mathfrak { p } - 1 } )
$$

For $\mathbf t \neq 0$ this is an unramified map, in fact Galois with Galois group $\mathbb { Z } / ( { \mathfrak { p } } )$ , and Forest $( \boldsymbol { \mathsf { X } } )$ is a tree with $\mathfrak { p }$ leaves.
For $\mathrm { t } = 0$ we get a geometric Frobenius, a purely inseparable map, and $\mathsf { X } _ { 1 }$ is not a branchvariety.

Hence, in this case the $\mathfrak { p }$ leaves “glue together” into a “thick” branch.

# 8. U-INVARIANT BRANCHVARIETIES

In this section, we operate under the same Assumption 7.2 on characteristics.

The space BranchF,Pn of branchvarieties of $\mathbb { P } ^ { { \mathfrak { n } } }$ with forest F carries an action of $\mathrm { P G L } _ { \mathrm { n + 1 } }$ . Let $u _ { n + 1 }$ or just U, denote the group of upper triangular matrices with 1s on the diagonal.
This acts on $\mathbb { P } ^ { { \mathfrak { n } } }$ with $\mathfrak { n } + \mathbb { 1 }$ orbits; two points are in the same orbit if they have the same last nonvanishing homogeneous coordinate.
We will call the closures of these orbits the standard $\mathbb { P } ^ { \mathrm { d } } \mathbf { s }$ in $\mathbb { P } ^ { { \mathfrak { n } } }$ . One motivation for studying actions of U is the following:

Lemma 8.1. [Hor69] Let U act on a complete space $\mathsf { X } ,$ and let $X ^ { \mathrm { u } }$ be its fixed point set.
Then $X ^ { \mathrm { u } }$ is connected iff X is connected, and the inclusion $x ^ { \mathrm { u } } \to x$ induces an isomorphism on (algebraic) fundamental groups.

(It is also easy to show that $X ^ { \mathrm { u } }$ is rationally connected iff $\boldsymbol { x }$ is, which we will neither prove nor use.)

Corollary 8.2. Let F be a rooted forest with maximum rank d. Then the number of components of BranchF,Pn is constant for ${ \mathfrak { n } } \geq { \mathfrak { d } }$ (and 0 for ${ \mathfrak { n } } < { \mathfrak { d } } ,$ ).

More precisely, let ${ \mathfrak { n } } _ { 1 } \geq { \mathfrak { n } } _ { 2 } \geq { \mathfrak { d } }$ . Then the natural inclusion $\mathrm { B r a n c h } _ { \mathsf { F } , \mathbb { P } ^ { \mathsf { n } _ { 2 } } } \hookrightarrow \mathrm { B r a n c h } _ { \mathsf { F } , \mathbb { P } ^ { \mathsf { n } _ { 1 } } }$ induces isomorphisms on $\pi _ { 0 }$ and $\pi _ { 1 }$ .

Proof.
The dimension of a branchvariety is the maximum rank of the vertices in its forest.
Hence the $\mathrm { ~ n ~ } < \mathrm { ~ d ~ }$ statement is trivial; in this case there are no finite maps from a d-dimensional scheme to $\mathbb { P } ^ { { \mathfrak { n } } }$ .

For a branchvariety $\mathbf { f } : {  { \mathbb { X } } } \to {  { \mathbb { P } } } ^ { \mathfrak { n } }$ to be U-invariant (as a point of $\mathrm { B r a n c h } _ { \mathsf { F } , \mathbb { P } ^ { \mathtt { n } } } ,$ ), its image must be U-invariant.
The only d-dimensional U-invariant reduced subscheme of $\mathbb { P } ^ { { \mathfrak { n } } }$ is the $\mathbb { P } ^ { \mathrm { d } }$ with vanishing last ${ \mathfrak { n } } - { \mathfrak { d } }$ coordinates.
Hence

$$
\left( \mathrm { B r a n c h } _ { \mathsf { F } , \mathbb { P } ^ { \mathrm { n } } } \right) ^ { \mathrm { U } _ { \mathrm { n } + 1 } } \cong ( \mathrm { B r a n c h } _ { \mathsf { F } , \mathbb { P } ^ { \mathrm { d } } } ) ^ { \mathrm { U } _ { \mathrm { d } + 1 } } .
$$

Now apply the lemma.

The case ${ \mathfrak { n } } = { \mathfrak { d } }$ has the following classical description: it parametrizes reduced schemes equipped with Noether normalizations.

We now attempt to better describe the elements of the U-fixed point set.

Lemma 8.3. Let f : $X ^ { \mathrm { d } }  \mathbb { P } ^ { \mathrm { n } }$ be an irreducible branchvariety, defining a U-invariant point in the moduli stack.
(In this case all Assumption 7.2 says is that char ${ \sf k } = 0$ or char $\mathrm { k } > \deg { X } . ,$ ) Then f is just the inclusion of the standard $\mathbb { P } ^ { \mathrm { d } }$ into $\mathbb { P } ^ { { \mathfrak { n } } }$ .

Proof.
In the proof of Corollary 8.2, we already determined the image.
So we may as well assume $\mathrm { d } = \mathfrak { n }$ for ease of description.

Let $\mathbb { A } ^ { { \mathfrak { n } } }$ denote the open U-orbit, with last coordinate nonvanishing.
Then $\mathsf { X } ^ { \circ } : = \mathsf { f } ^ { - 1 } ( \mathbb { A } ^ { \mathsf { n } } )$ is open and nonempty in $\mathsf X$ , hence irreducible.
The map $\mathsf { f } ^ { \circ } : X ^ { \circ } \ \overset { \circ } { \to } \ \mathbb { A } ^ { \mathsf { n } }$ is a U-invariant branchvariety of $\mathbb { A } ^ { { \mathfrak { n } } }$ . By the U-invariance, $\mathsf { f } ^ { \circ }$ is ramified either everywhere or nowhere.

If it is ramified everywhere (which can only happen in characteristic $\mathfrak { p }$ ), then the degree of this cover is at least char k. But this violates our assumption on the characteristic.

Hence f◦ is a trivial cover, and for $X ^ { \circ }$ to be irreducible $\mathsf { f } ^ { \circ }$ must be a degree 1 cover, again by the assumption on the characteristic.
So f : $X \to \mathbb { P } ^ { \mathrm { d } }$ is degree 1. By Zariski’s Main Theorem, f is an isomorphism.


Example 8.4. We note that the conclusion of this Lemma is no longer true in small characteristics.
Indeed, let char ${ \sf k } = { \sf p }$ and let $\mathsf { f } ^ { \circ } : \mathbb { A } ^ { 1 } \to \mathbb { A } ^ { 1 }$ be a morphism defined by $\mathsf { y } = \mathsf { x } ^ { \mathsf { p } } - \mathsf { x } ;$ homogenize to obtain a branchvariety $\textsf { f } : X = \mathbb { P } ^ { 1 } \to \textsf { Y } \stackrel { \bullet } { = } \mathbb { P } ^ { 1 }$ . Then $\mathsf { f } ^ { \circ }$ is a nontrivial ´etale cover; in fact it is Galois with the Galois group $\mathbb { Z } / ( { \mathfrak { p } } )$ . One easily checks that the branchvariety $\boldsymbol { x }$ is U-invariant.

Lemma 8.5. Let f : $X \to \mathbb { P } ^ { \mathrm { n } }$ be a branchvariety defining a U-invariant point in the moduli stack.\
Then there is an action of U on X such that f is equivariant (and this action is unique).

Proof.
Let $\mathrm { ~ J ~ } \subset \mathrm { ~ A u t } ( \mathsf X , \mathsf L ) \times \mathsf { U }$ be the closed subscheme of pairs $\{ ( \mathbf { a } , \mathbf { u } ) : \mathsf { f } \circ \mathbf { a } = \mathsf { u } \circ \mathsf { f } \} .$ . (We note that $\mathrm { A u t } ( X , \mathrm { L } )$ is a closed subgroup of $\mathrm { P G L } _ { \mathrm { N } + 1 }$ and is an algebraic group.)
Its projection ${ \tt p } _ { 2 }$ to the second factor is onto, by the assumption of U-invariance.

The scheme J carries an action of $\operatorname { A u t } ( \mathsf { f } )$ which on points is defined by $9 \cdot ( \mathrm { a } , \mathrm { u } ) : = ( \mathrm { g } \circ$ $\mathbf { a } , \mathfrak { u } )$ , and it is easily seen to be free.
We note that J is just the automorphism group scheme for a family of branchvarieties over U, as defined in Section 3. Hence $\mathrm { J } \to \mathsf { U }$ is finite.
Since the action is free, $\mathrm { J } \to \mathsf { U }$ is ´etale.
By the assumption on the characteristic, U does not have irreducible finite ´etale covers of small degrees.
So J breaks into a disjoint union of sections.
Writing the section through (1, 1) as $\mathfrak { u } \mapsto ( \alpha ( \mathfrak { u } ) , \mathfrak { u } ) .$ , the map $\alpha : \mathsf { U } \to \mathrm { A u t } ( X , \mathrm { L } )$ is easily seen to give an action, and we are done.


Theorem 8.6. Let f : $X \to \mathbb { P } ^ { \mathrm { n } }$ be $a$ U-invariant branchvariety in $\mathrm { B r a n c h } _ { \mathrm { h , \mathbb { P } ^ { n } } } ^ { \mathsf { F } }$ . Then $\boldsymbol { x }$ is a union of projective spaces, where the number of irreducible components of dimension i is the number of leaves of F of rank i. Any (nontrivial) intersection of components is irreducible, and identified by f with a U-invariant thickening of one of the standard $\mathbb { P } ^ { \mathrm { d } _ { \boldsymbol { S } } }$ in $\mathbb { P } ^ { { \mathfrak { n } } }$ .

Proof.
Let $X ( 1 ) , . . . , X ( \mathfrak { m } )$ be a nonempty set of components of $\Sigma ,$ and $\mathsf { H } = \cap _ { \mathrm { j } } X ( \mathrm { j } )$ , considered as a subscheme of $\mathsf X ( 1 )$ . Then under the identification $\mathfrak { f } : X ( 1 ) { \overset { \sim } { \longrightarrow } } \mathbb { P } ^ { \dim X ( 1 ) }$ guaranteed by Lemma 8.3, $\sf H _ { \mathrm { r e d } }$ maps to a reduced U-invariant subscheme of the standard $\mathbb { P } ^ { \mathrm { d i m } \times ( 1 ) }$ The only possibility is the standard $\mathbb { P } ^ { \mathrm { d i m } \mathrm { \ : H } }$ .

Since the components are all degree 1, the number of components of dimension i is the degree of $\chi ^ { \mathrm { d i m i } }$ , which we already knew to be the number of leaves of F of rank i. 

Remark 8.7. It is not difficult to see that the seminormalization of any U-invariant branchvariety is exactly the Stanley-Reisner scheme from Example 7.8 for the same rooted forest (but all labels changed to 1).

Proposition 8.8. Let F be the forest of a branchvariety $\mathsf { X } ,$ and v a maximal fork of F, i.e. each $w > \nu$ has only one leaf above $_ w$ . Then the label $\chi ( \nu )$ on $\nu$ is at most 1.

Proof.
As already explained, we can reduce to the case that $\boldsymbol { x }$ is connected and $\nu$ is the root.
By Lemma 8.1 and Proposition 7.4, we can assume X is U-invariant.
Then the condition on $\nu ,$ plus the proof of Proposition 7.9, says that the seminormalization $\widetilde { x }$ is an isomorphism away from the standard $\mathbb { P } ^ { 0 }$ . If Y is the scheme-theoretic fiber lying over $\mathbb { P } ^ { 0 }$ (a fat point), then $\chi ( \mathcal { O } _ { \chi } ) - \chi ( \mathcal { O } _ { \mathbb { P } ^ { 0 } } ) = \chi ( \mathcal { O } _ { \widetilde { \chi } } ) - \chi ( \mathcal { O } _ { \Upsilon } ) = 1 - \mathsf { l e n } ( \Upsilon ) ,$ , where $\mathsf { l e n } ( \mathsf { Y } ) \geq 1$ is the length of the fat point Y. Hence $0 \geq \chi ( \mathcal { O } _ { \mathbb { X } } ) - \chi ( \mathcal { O } _ { \mathbb { P } ^ { 0 } } ) = \chi ( \nu ) - 1$ . 

(We won’t need it, but even if the $\boldsymbol { x }$ in the above proof is not assumed U-invariant, one can give a good description of it: $\boldsymbol { x }$ is the connected union of a set $\{ \mathsf { P } _ { \mathrm { i } } \}$ of projective spaces, each including into $\mathbb { P } ^ { { \mathfrak { n } } }$ as a linear subspace, and a set of curves $\{ { \mathsf { C } } _ { \mathrm { { j } } } \} ,$ where all intersections $\mathsf { P } _ { \mathrm { i } } \cap \mathsf { P } _ { \mathrm { j } }$ are 0-dimensional.)

Example 8.9. Not all labels on forests of branchvarieties are at most 1. If $\boldsymbol { x }$ is a quartic hypersurface in $\mathbb { P } ^ { 3 }$ , e.g. a K3 surface, then the label on the root of its forest is 2.

8.1. Spaces of cubic curves.
Consider the space of branchvarieties of $\mathbb { P } ^ { 2 }$ including the plane cubics, so $\mathtt { h } ( \mathtt { n } ) = 3 \mathtt { n } , \mathtt { b } _ { 0 } = 0 , \mathtt { b } _ { 1 } = 3$ . According to the description in Theorem 8.6, a U-invariant branchvariety is a union of three copunctal lines.
These already appeared in Example 4.2, where the angle of intersection gave a $\mathbb { P } ^ { 1 } / S _ { 3 }$ worth of such branchvarieties.

On the other hand, there is a 3-dimensional space of U-invariant stable curves of degree 3 and genus 0. Each has an elliptic curve (which collapses entirely) meeting three $\mathbb { P } ^ { 1 } \mathbf { s }$ each in a point.
So the space of branchcubics does not match the corresponding moduli space of stable maps.

# 9. RELATIONS TO OTHER MODULI SPACES

In each of Hilb, Branch, and Chow there is an open set corresponding to reduced subschemes, and these three open sets are naturally identified.
In general, the only natural morphisms extending this identification go from Hilb or Branch to Chow, as the following examples show.

# 9.1. Branch vs. Hilbert.

Example 9.1. The moduli stack of n points branched over a reduced scheme Y is easily computed to be the “symmetric product” stack $[ \mathsf { Y } ^ { \mathrm { n } } / \mathsf { S } _ { \mathrm { n } } ]$ . If $\Upsilon = \mathbb { P } ^ { 2 }$ and ${ \mathfrak { n } } > 1$ then the Hilbert scheme of n points has a nontrivial blowdown to the coarse moduli space ${ \Upsilon } ^ { { \mathrm { n } } } / { \mathsf { S } } _ { { \mathrm { n } } }$ (which is in fact the Chow variety).
However, there is no natural stack map Hilb Branch, and no continuous map Branch $ \mathrm { H i l b }$ .

Example 9.2. The Hilbert scheme of plane conics is simply $\mathbb { P } ^ { 5 }$ . The branchvariety stack of plane conics is (coarsely) $\mathbb { P } ^ { 5 }$ blown up along the Veronese surface.
So in this case there is no continuous map Hilb Branch.

On the other hand, as was pointed out to us by J´anos Koll´ar, the classical Hilbert scheme can be properly embedded into Branch, albeit for different parameters.

Theorem 9.3. There exists a closed embedding $\Psi : { \mathrm { H i l b } } _ { \boldsymbol { \mathrm { h } } , \mathbb { P } ^ { \mathrm { n } } } \to { \mathrm { B r a n c h } } _ { 2 \boldsymbol { \mathrm { q } } - \boldsymbol { \mathrm { h } } , \mathbb { P } ^ { \mathrm { n } } } ^ { ( 0 , \dots , 0 , 2 ) } ,$ where ${ \mathfrak { q } } ( { \mathfrak { d } } ) =$ $\mathrm { B r a n c h } _ { 2 \mathbf { q } - \mathbf { h } , \mathbb { P } ^ { \mathbf { n } } } ^ { ( 0 , . . . , 0 , 2 ) }$ . As a stack, this connected component of $\mathrm { H i l b } _ { \mathsf { h } , \mathbb { P } ^ { \mathsf { n } } }$ is (coarsely) a connected component of $\mathrm { B r a n c h } _ { 2 \mathbf { q } - \mathbf { h } , \mathbb { P } ^ { \mathtt { h } } } ^ { ( \bar { 0 } , \dots , 0 , 2 ) }$ is $\mathrm { H i l b } _ { \mathsf { h } , \mathbb { P } ^ { \mathsf { n } } }$ modulo $a$ trivial $\mathbb { Z } / ( 2 )$ action.

By Proposition 7.4, each branchvariety in this connected component has the same forest F. If char $\mathtt { k } \neq 2 \mathtt { \_ }$ , then the converse holds; each branchvariety with forest F is of the sort just constructed.
In particular, BranchF,Pn is connected, giving a positive answer to Question 7.11 for this F.

Proof.
The morphism $\psi$ associates to each family of subschemes $Z \subset \mathbb { P } _ { S } ^ { n }$ the following family $\boldsymbol { x }$ of branchvarieties of $\mathbb { P } ^ { { \mathfrak { n } } }$ : X consists of two copies of $\mathbb { P } _ { S } ^ { \mathrm { n } }$ glued along Z; the structure sheaf of $\boldsymbol { x }$ is $\varprojlim ( \mathcal { O } _ { \mathbb { P } _ { S } ^ { \mathrm { n } } } \oplus \mathcal { O } _ { \mathbb { P } _ { S } ^ { \mathrm { n } } } \to \mathcal { O } _ { Z } )$ . Clearly, this gives a closed embedding.

By [Kol95, Cor. 12.7], if codim $Z \geq 3$ then any deformation of $\boldsymbol { x }$ extends to a deformation of the two copies of $\mathbb { P } ^ { { \mathfrak { n } } }$ , i.e. it is of the same type.
In this case, the whole connected component consists of branchvarieties glued from two copies of $\mathbb { P } ^ { { \mathfrak { n } } }$ , and Z can be recovered from it.
The two copies of $\mathbb { P } _ { S } ^ { \mathrm { n } }$ can be unambiguously called the “first” and “second” copy, without monodromy in $Z _ { \cdot }$ , hence the triviality of the $\mathbb { Z } / ( 2 )$ action.

It is easy to describe the forest $\digamma$ of any one of these branchvarieties.
Taking a plane section with a plane of codimension $\boldsymbol { \mathrm { k } }$ gives two copies of $\mathbb { P } _ { S } ^ { { \mathrm { n - k } } }$ glued along a plane section of Z. If $\begin{array} { r } { \boldsymbol { \mathrm { k } } \leq \mathrm { d e g h } , } \end{array}$ the plane section of Z is nonempty, so the branchvariety $X _ { \mathrm { k } }$ is connected.
For $\mathrm {  ~ \cdot ~ } \mathrm {  ~ \ l ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \ l ~ } \mathrm { d e g h } ,$ the plane section $X _ { \mathrm { k } }$ is a union of two copies of $\mathbb { P } _ { S } ^ { { \mathrm { n - k } } }$ . So F looks like a tuning fork; it has one vertex $\nu$ for each rank $0 , \ldots , \deg \ h ,$ labeled $1 - ( \Delta ^ { \mathrm { r k \nu } } \mathrm { h } ) ( 0 ) ,$ , the fork vertex at rank ${ \mathrm { d e g h } } ,$ and two vertices (each labeled 1, as to be expected from Proposition 7.9) for each rank $\mathbf { k } + 1 , \ldots , \mathbf { n }$ .

Now we want to show that the only connected component of Branch(0,...,0,2)2q−h,Pn with this forest $\digamma$ is the one described above.
By Lemma 8.1, it is enough to check that any Uinvariant branchvariety $\boldsymbol { x }$ with this forest is in the connected component above.
But by Theorem 8.6 (for which we need char $\mathtt { k } \neq 2$ ), such an $\boldsymbol { x }$ is obviously a union of two copies of $\mathbb { P } _ { S } ^ { \mathrm { n } }$ along a $\left( \mathrm { d e g h } \right)$ -dimensional scheme.


Example 9.4. Consider the case when Z is two points (or one point of multiplicity 2) in $\mathbb { P } ^ { 1 }$ . In this case the Hilbert scheme is $( \mathbb { P } ^ { 1 } ) ^ { 2 } / S _ { 2 } \cong \mathbb { P } ^ { \bar { 2 } }$ . Whereas Branch is $( { \mathbb { P } } ^ { 1 } ) ^ { 4 } / S _ { 4 } ,$ as explained in Example 4.4.

Remark 9.5. This example was the case of codim $Z = 1$ . When codim $Z = 2 ,$ one can say that $( \mathrm { H i l b } _ { 2 \mathsf { q } - \mathsf { h } , \mathbb { P } ^ { \mathsf { n } } } ) _ { \mathrm { r e d } }$ is a connected component of $\mathrm { ( B r a n c h ) } _ { \mathrm { r e d } } ,$ since a degeneration of a branchvariety connected in codimension 1 is again connected in codimension 1. However, the scheme structures in this case are not obvious.

9.2. Branch vs. Chow.
The Chow variety of plane conics, like the Hilbert scheme, is $\mathbb { P } ^ { 5 }$ .\
So there is no continuous morphism in general from Chow to Branch.

If ${ \textsf { f } } : X \to \mathsf { Y }$ is a branchvariety of Y then $\big ( \mathrm { f } _ { * } [ X ^ { \dim \mathrm { i } } ] \big )$ is a well-defined collection of cycles on Y, of dimension i and degree $\mathsf { b } _ { \mathrm { i } }$ . This gives a set-theoretic map from Branch to a product of Chow varieties.
Putting this into arbitrary families is somewhat delicate since, as we already noted in 0.5, Chow lacks the infinitesimal theory.
J. Koll´ar [Kol96, I.3- 4] defines the Chow functor on the category of reduced and seminormal schemes.
This immediately gives a functorial morphism

$$
\mathrm { ( B r a n c h _ { h , Y } ^ { b } ) _ { \mathrm { r e d } } ^ { s e m i } } \longrightarrow \prod _ { \mathrm { i } } \mathrm { C h o w } _ { \mathrm { i , b _ { i } , Y } }
$$

from the seminormalization of the reduced part of Branch.

We note that the information encoded in Branch is much richer, and the cycle $\mathsf { f } _ { * } [ \mathsf { X } ]$ is but a shadow of $\boldsymbol { x }$ .

9.3. Branch vs. stable maps.
Any proper map $\Chi \to \Upsilon$ (for X reduced) admits a Stein factorization $X  X ^ { \prime }  Y$ where $\bar { \mathsf X ^ { \prime } } \to \mathsf Y$ is a branchvariety.
This suggests that there might be natural transformations to Branch from other spaces of maps – in particular, stable maps of curves.

However, $\chi ( \mathrm { X } , \mathrm { L } ^ { \mathrm { d } } ) \neq \chi ( \mathrm { X } ^ { \prime } , \mathrm { L } ^ { \mathrm { d } } )$ in general, which would make such a transformation discontinuous.
One case in which they are equal is $\Chi \to \mathsf { Y }$ a stable curve of genus zero, and indeed the Stein factorization gives a natural transformation $\overline { { \mathbf { M } } } _ { 0 , 0 } ( \mathsf { Y } ) \to \bar { \mathrm { B r a n c h } } _ { \mathsf { Y } }$ . The details will appear in [Lin06].

# 10. OTHER VERSIONS

10.1. Multigraded Branch.
There are two multigraded analogues of the classical Hilbert scheme: the toric Hilbert scheme [PS02] and the multigraded Hilbert scheme of [HS04]. As was explained in Section 4.2, the toric Branch already exists: it is the moduli space of multiplicity-free stable toric varieties.
To construct the multigraded Branch in full generality using the methods of this paper would appear to require a definition of b-sheaf in the equivariant setting, where invariant hyperplanes are not generic.

10.2. Complex-analytic Branch.
The complex-analytic analogues of the Hilbert scheme and Chow varieties classifying complex-analytic subspaces, resp.
cycles of a complexanalytic space are well known; they are called the Douady space and Barlet space respectively.
Clearly, a complex-analytic analogue of Branch can and should be constructed as well.

# REFERENCES

[Ale96] V. Alexeev, Moduli spaces $M _ { \mathfrak { g } , \mathfrak { n } } ( W )$ for surfaces, Higher-dimensional complex varieties (Trento, 1994), de Gruyter, Berlin, 1996, pp. 1–22.

[Ale02] , Complete moduli in the presence of semiabelian group action, Ann.
of Math.
(2) 155 (2002), no. 3, 611–708. math.AG/9905103\
[Ale06] , Limits of stable pairs, math.AG/0607684\
[AB05] , M. Brion, Stable spherical varieties and their moduli, math.AG/0505673\
[Art69] M. Artin, Algebraization of formal moduli.
I, Global Analysis (Papers in Honor of K. Kodaira), Univ. Tokyo Press, Tokyo, 1969, pp. 21–71.\
[BLR90] S. Bosch, W. L ¨utkebohmert, and M. Raynaud, N´eron models, Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)], vol. 21, Springer-Verlag, Berlin, 1990.\
[Chi00] R. Chiriv\`ı, LS algebras and application to Schubert varieties, Transform.
Groups 5 (2000), no. 3, 245– 264.\
[DEP82] C. de Concini, D. Eisenbud, C. Procesi, Hodge algebras, Ast´erisque (1982), 91.\
[DL81] C. de Concini, V. Lakshmibai, Arithmetic Cohen-Macaulayness and arithmetic normality for Schubert varieties, Amer.
J. Math.
103 (1981), no. 5, 835–850.\
[Eis95] D. Eisenbud, Commutative algebra, with a view toward algebraic geometry, Graduate Texts in Mathematics, vol. 150, Springer-Verlag, New York, 1995.\
[EGA4-2] A. Grothendieck, El´ements de g´eom´etrie alg´ebrique.
IV. ´ Etude locale des sch´emas et des morphismes de ´ sch´emas.
II, Inst.
Hautes Etudes Sci.
Publ.
Math.
(1965), no. 24, 231. ´\
[Fle77] H. Flenner, Die S¨atze von Bertini f ¨ur lokale Ringe, Math.
Ann.
229 (1977), no. 2, 97–111.\
[Gre89] M. Green, Restrictions of linear series to hyperplanes, and some results of Macaulay and Gotzmann, Algebraic curves and projective geometry (Trento, 1988), 76–86, Lecture Notes in Math., 1389, Springer, Berlin, 1989.\
[HS04] M. Haiman and B. Sturmfels, Multigraded Hilbert schemes, J. Algebraic Geom.
13 (2004), no. 4, 725–769. math.AG/0201271\
[HM82] J. Harris and D. Mumford, On the Kodaira dimension of the moduli space of curves, Invent.
Math.
67 (1982), no. 1, 23–88.\
[Har66] R. Hartshorne, Connectedness of the Hilbert scheme, Inst.
Hautes Etudes Sci.
Publ.
Math.
No. 29 ´ (1966), 5–48.\
[Har77] R. Hartshorne, Algebraic geometry, Springer-Verlag, New York, 1977, Graduate Texts in Mathematics, No. 52.\
[Høn04] M. Hønsen, A compact moduli space for Cohen-Macaulay curves in projective space, MIT Thesis (2004), 1–59.\
[Hor69] G. Horrocks, Fixed point schemes of additive group actions, Topology 8 (1969), 233–242.\
[HuSw06] C. Huneke, I. Swanson, Integral Closure of Ideals, Rings, and Modules, in preparation.
Available at http://www.reed.edu/∼iswanson/book/\
[Ill71] L. Illusie, Complexe cotangent et d´eformations.
I, Springer-Verlag, Berlin, 1971, Lecture Notes in Mathematics, Vol. 239.\
[Ill72] Complexe cotangent et d´eformations.
II, Springer-Verlag, Berlin, 1972, Lecture Notes in Mathematics, Vol. 283.\
[KM97] S. Keel and S. Mori, Quotients by groupoids, Ann.
of Math.
(2) 145 (1997), no. 1, 193–213. alg-geom/9508012\
[Knu71] D. Knutson, Algebraic spaces, Springer-Verlag, Berlin, 1971, Lecture Notes in Mathematics, Vol. 203.\
[Knu05] A. Knutson, Balanced normal cones and Fulton-MacPherson’s intersection theory, preprint (2005). math.AG/0512632\
[Knu06] , Standard bases for homogeneous coordinate rings, in preparation.\
[Kol90] J. Koll´ar, Projectivity of complete moduli, J. Differential Geom.
32 (1990), no. 1, 235–268.\
[Kol95] , Flatness criteria, J. Algebra 175 (1995), no. 2, 715–727.\
[Kol96] , Rational curves on algebraic varieties, Ergebnisse der Mathematik und ihrer Grenzgebiete [Results in Mathematics and Related Areas]. 3. Folge.
A Series of Modern Surveys in Mathematics, vol. 32, Springer-Verlag, Berlin, 1996.\
[Kol97] Quotient spaces modulo algebraic groups, Ann.
of Math.
(2) 145 (1997), no. 1, 33–79. alg-geom/9503007\
[LMB00] G. Laumon and L. Moret-Bailly, Champs alg´ebriques, Ergebnisse der Mathematik und ihrer Grenzgebiete [Results in Mathematics and Related Areas]. 3. Folge.
A Series of Modern Surveys in Mathematics, vol. 39, Springer-Verlag, Berlin, 2000.\
[Lie06] M. Lieblich, Remarks on the stack of coherent algebras, Int.
Math.
Res.
Notices (2006), article ID 75273 math.AG/0603034\
[Lin06] J. Lin, The Betti numbers of moduli of branchvarieties, in preparation.\
[Mat89] H. Matsumura, Commutative ring theory, second ed., Cambridge Studies in Advanced Mathematics, vol. 8, Cambridge University Press, Cambridge, 1989.\
[Mum70] D. Mumford, Varieties defined by quadratic equations, Questions on Algebraic Varieties (C.I.M.E., III Ciclo, Varenna, 1969), Edizioni Cremonese, Rome, 1970, pp. 29–100.\
[MFK94] D. Mumford, J. Fogarty, and F. Kirwan, Geometric invariant theory, third ed., Ergebnisse der Mathematik und ihrer Grenzgebiete (2) [Results in Mathematics and Related Areas (2)], vol. 34, Springer-Verlag, Berlin, 1994.\
[Nag57] M. Nagata, Note on a paper of Samuel concerning asymptotic properties of ideals, Mem.
Coll.
Sci.
Univ. Kyoto.
Ser.
A. Math.
30 (1957), 165–175.\
[Ols06] M. Olsson, Deformation theory of representable morphisms of algebraic stacks, to appear in Math.
Zeit.\
[PS02] I. Peeva and M. Stillman, Toric Hilbert schemes, Duke Math.
J. 111 (2002), no. 3, 419–449.\
[Ree88] D. Rees, Lectures on the asymptotic theory of ideals, London Mathematical Society Lecture Note Series, 113, Cambridge University Press, Cambridge, 1988.\
[Sam52] P. Samuel, Some asymptotic properties of powers of ideals, Ann.
of Math.
(2) 56 (1952), 11–21.\
[SGA6] Th´eorie des intersections et th´eor\`eme de Riemann-Roch, Springer-Verlag, Berlin, 1971, S´eminaire de G´eom´etrie Alg´ebrique du Bois-Marie 1966–1967 (SGA 6), Dirig´e par P. Berthelot, A. Grothendieck et L. Illusie.
Avec la collaboration de D. Ferrand, J. P. Jouanolou, O. Jussila, S. Kleiman, M. Raynaud et J. P. Serre, Lecture Notes in Mathematics, Vol. 225.\
[Stn78] R. Stanley, Hilbert functions of graded algebras, Advances in Math.
28 (1978), 57–83.\
[Sta06] J. Starr, Artin’s axioms, composition and moduli spaces, preprint.
math.AG/0602646

DEPARTMENT OF MATHEMATICS, UNIVERSITY OF GEORGIA, ATHENS GA 30602, USA E-mail address: mailto:valery@math.uga.edu
