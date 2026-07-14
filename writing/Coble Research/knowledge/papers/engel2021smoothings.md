---
title: Smoothings and rational double point adjacencies for cusp singularities
authors:
- Engel
year: 2021
bibkey: engel2021smoothings
tags:
- paper
- extraction
abstract: |
  A cusp singularity is a surface singularity whose minimal resolution is a cycle of smooth rational curves meeting transversely.
  Cusp singularities come in dual pairs.
  Looijenga proved in 1981 that if a cusp singularity is smoothable, the minimal resolution of the dual cusp is the anticanonical divisor of some smooth rational surface.
  In 1983, the second author and Miranda gave a criterion for smoothability of a cusp singularity, in terms of the existence of a K-trivial semistable model for the central fiber of such a smoothing.
  We study these “Type III degenerations” of rational surfaces with an anticanonical divisor—their deformations, birational geometry, and monodromy.
  Looijenga’s original paper also gave a description of the rational double point configurations to which a cusp singularity deforms, but only in the case where the resolution of the dual cusp has cycle length 5 or less.
  We generalize this classification to an arbitrary cusp singularity, giving an explicit construction of a semistable simultaneous resolution of such an adjacency.
  The main tools of the proof are (1) formulas for the monodromy of a Type III degeneration, (2) a construction via surgeries on integral-affine surfaces of a degeneration with prescribed monodromy, (3) surjectivity of the period map for Type III central fibers, and (4) a theorem of Shepherd-Barron producing a simultaneous contraction to the adjacency.
---

# SMOOTHINGS AND RATIONAL DOUBLE POINT ADJACENCIES FOR CUSP SINGULARITIES

Philip Engel & Robert Friedman

# Abstract

A cusp singularity is a surface singularity whose minimal resolution is a cycle of smooth rational curves meeting transversely.
Cusp singularities come in dual pairs.
Looijenga proved in 1981 that if a cusp singularity is smoothable, the minimal resolution of the dual cusp is the anticanonical divisor of some smooth rational surface.
In 1983, the second author and Miranda gave a criterion for smoothability of a cusp singularity, in terms of the existence of a K-trivial semistable model for the central fiber of such a smoothing.
We study these “Type III degenerations” of rational surfaces with an anticanonical divisor—their deformations, birational geometry, and monodromy.
Looijenga’s original paper also gave a description of the rational double point configurations to which a cusp singularity deforms, but only in the case where the resolution of the dual cusp has cycle length 5 or less.
We generalize this classification to an arbitrary cusp singularity, giving an explicit construction of a semistable simultaneous resolution of such an adjacency.
The main tools of the proof are (1) formulas for the monodromy of a Type III degeneration, (2) a construction via surgeries on integral-affine surfaces of a degeneration with prescribed monodromy, (3) surjectivity of the period map for Type III central fibers, and (4) a theorem of Shepherd-Barron producing a simultaneous contraction to the adjacency.

# Introduction

Let $( X , x )$ be the germ of an isolated singularity.
Some basic questions that one can ask about the deformation theory of $( X , x )$ are: Is $( X , x )$ smoothable?
If so, how can we describe the smoothing components of $( X , x )$ ? What are the singularities adjacent to $( X , x )$ ? In particular, for a surface singularity, what are the rational double points adjacent to $( X , x )$ ? In case $( X , x )$ is itself a rational double point, the answers to these questions are well-known.
In this case, $( X , x )$ is smoothable and there is a unique smoothing component, as it is a hypersurface singularity, and the adjacent rational double points correspond to subgraphs of the Dynkin diagram corresponding to $( X , x )$ .

The next level of complexity for a normal surface singularity is the case where $( X , x )$ is a minimally elliptic singularity in Laufer’s terminology, i.e. a Gorenstein elliptic singularity, and here the simplest case is when the fundamental cycle of $( X , x )$ is reduced.
In this case, $( X , x )$ is either a simple elliptic, cusp, or triangle singularity.
These three types admit a resolution whose exceptional fiber is a smooth elliptic curve, a cycle of smooth rational curves, or either cuspidal, two smooth rational curves meeting at a tacnode, or three smooth rational curves meeting at a point, respectively.

The deformation theory of simple elliptic and triangle singularities is by now well understood, by work of Pinkham and Looijenga [32], [33], [25], [26]. The crucial point here is that the singularities in question have a $\mathbb { C } ^ { * }$ -action.
Thus questions about smoothings and adjacent singularities can be related to global questions about the existence of certain compact algebraic surfaces with configurations of curves on them: (generalized) del Pezzo surfaces with a smooth section of the anticanonical divisor in the case of simple elliptic singularities, $K 3$ surfaces with so-called $T _ { p , q , r }$ configurations in the case of triangle singularities.
For example, in case $( X , x )$ is simple elliptic, let $( \widetilde X , E )$ be the minimal resolution of $X$ and set $E ^ { 2 } = - d$ . Then we may realize the germ $( \widetilde X , E )$ on an elliptically ruled surface with zero section $E$ and infinity section $E ^ { \prime }$ satisfying $( E ^ { \prime } ) ^ { 2 } = d$ . We preserve the divisor $E ^ { \prime }$ on the nearby fibers of a negative weight deformation of $( X , x )$ to get pairs $( X _ { t } , E ^ { \prime } )$ , where $X _ { t }$ is a normal projective surface such that $E ^ { \prime } \in | - K _ { X _ { t } } |$ .

It follows that nontrivial negative weight deformations of $( X , x )$ correspond to generalized del Pezzo surfaces $X _ { t }$ , hence $d \leq 9$ whenever $( X , x )$ is smoothable (the converse also holds).
Furthermore, the adjacent configurations of rational double points to $( X , x )$ are those that appear on such an $X _ { t }$ . These in turn can be described by the configurations of curves, all of whose components are isomorphic to $\mathbb { P } ^ { 1 }$ and of self-intersection $- 2$ , which appear as the exceptional curves on a minimal resolution $Y _ { t }  X _ { t }$ . For $d$ small, $( X , x )$ is a complete intersection singularity ( $d \leq 4$ ) or a Pfaffian singularity ( $d = 5$ ). In this case, there is an associated root system $R$ given by taking the vectors of square $- 2$ in $( K _ { Y _ { t } } ) ^ { \perp }$ . (By the usual algebraic geometry conventions, all root systems in this paper will be negative definite.)
Then the possible Dynkin diagrams of configurations of rational double points on some $X _ { t }$ are given by root systems contained in $R$ satisfying a mild extra condition coming from the period map, which can in turn be described via embeddings into the extended Dynkin diagram of $R$ . For $d$ large, however, there can be several smoothing components of $( X , x )$ and $( K _ { Y _ { t } } ) ^ { \perp }$ need not be a root lattice.
Nonetheless, the possible adjacent rational double point configurations can still be described lattice-theoretically.

For the case of cusp singularities, Looijenga gave a beautiful description of the possible adjacencies in his breakthrough paper [27], but only in the case of multiplicity at most 5. In this case, the cusp singularity is either a complete intersection or Pfaffian, hence automatically smoothable and there is a unique smoothing component.
As in the case of simple elliptic singularities of multiplicity at most 5, there is again a diagram which determines the possible adjacent singularities, and it is the intersection graph for the root basis of a generalized root system of hyperbolic type.

As above, a key ingredient in Looijenga’s analysis is the existence of a complete surface containing the cusp $( X , x )$ on which one globalizes deformations.
But one must leave the world of algebraic geometry to produce such a surface.
The Inoue surface $V _ { 0 }$ associated to a cusp $( X , x )$ is a compact complex surface of type VII $_ 0$ such that $D + D ^ { \prime } \in | - K _ { V _ { 0 } } |$ , where an analytic neighborhood of $\begin{array} { r } { D ^ { \prime } = \sum _ { i = 1 } ^ { r ^ { \prime } } D _ { i } ^ { \prime } } \end{array}$ is a minimal resolution of the cusp $( X , x )$ , and by definition an analytic neighborhood of $D =$ $\sum _ { j = 1 } ^ { r } D _ { j }$ is a minimal resolution of the dual cusp $( \widehat { X } , \widehat { x } )$ to $( X , x )$ . (For notational reasons, it is more convenient to denote by $D ^ { \prime }$ the minimal resolution of the cusp we are interested in deforming and by $D$ the minimal resolution of its dual.)
Here $D$ is a cycle of smooth rational curves, or an irreducible nodal curve if $r ~ = ~ 1$ , and similarly for $D ^ { \prime }$ . By convention, $D _ { i } \cdot D _ { i \pm 1 } = 1$ , where the integer $i$ is taken mod $r$ , and $D _ { i } \cdot D _ { j } = 0$ otherwise.
The type or self-intersection sequence of $D$ is the sequence $( D _ { 1 } ^ { 2 } , \ldots , D _ { r } ^ { 2 } )$ mod cyclic permutations and order-reversing permutations.
There is a somewhat complicated recipe for obtaining $D$ , together with its self-intersection sequence, from $D ^ { \prime }$ .

Looijenga showed that, if $\overline { { \overline { { V } } } } _ { 0 }$ is the compact singular analytic surface obtained by contracting the curves $D ^ { \prime }$ and $D$ , then the deformation functor $\mathbf { D e f } _ { \overline { { \overline { { V } } } _ { 0 } } }$ of $\overline { { \overline { { V } } } } _ { 0 }$ is naturally isomorphic to $\mathbf { D e f } _ { ( \widehat { X } , \widehat { x } ) } \times \mathbf { D e f } _ { ( X , x ) }$ Thus, the deformations of $( X , x )$ , viewed as deformations of $( X , x )$ q $( \widehat { X } , \widehat { x } )$ for which the deformation of $( \widehat { X } , \widehat { x } )$ is trivial, can be identified with deformations of the pair $( \overline { { V } } _ { 0 } , D )$ keeping $D$ constant, where $\overline { { V } } _ { 0 }$ is the compact singular analytic surface obtained by contracting $D ^ { \prime }$ . A smoothing of $( X , x )$ then yields a pair $( Y _ { t } , D _ { t } )$ , where $Y _ { t }$ is a smooth rational surface and $D _ { t } \in \mathsf { \Omega } | - K _ { Y _ { t } } |$ is a cycle of rational curves of the same type as $D \subseteq V _ { 0 }$ . Briefly, we say that $D$ sits on a rational surface $Y$ (we identify $D _ { t }$ with $D$ ). Hence a smoothing component of $( X , x )$ determines a deformation type $[ ( Y , D ) ]$ of anticanonical pairs $( Y , D )$ , i.e. pairs consisting of a smooth rational surface $Y$ and a section $D \in | - K _ { Y } |$ which is a cycle of rational curves of the same type as the minimal resolution of the dual cusp to $( X , x )$ . We define a smoothing component of $( X , x )$ to be of type $[ ( Y , D ) ]$ in this case.
In particular, the existence of such a pair $( Y , D )$ is a necessary condition for the cusp $( X , x )$ to be smoothable.
In [27], Looijenga conjectured that it is also a sufficient condition:

Conjecture 0.1 (Looijenga’s conjecture).
The cusp $( X , x )$ is smoothable if and only if the minimal resolution of the dual cusp sits on a rational surface.

Motivated by the corresponding picture for degenerations of $K 3$ surfaces, the second author and R. Miranda showed in [10] that Looijenga’s conjecture was equivalent to the existence of a certain semistable model $Y _ { 0 }$ for the smoothing, whose description we recall in Section 2. The main idea is to show that the semistable fiber $\textstyle Y _ { 0 } = \bigcup _ { i = 0 } ^ { n } V _ { i }$ deforms in a smooth one parameter family $y  \Delta$ . Here $V _ { 0 }$ is the Inoue surface with the cycles $D ^ { \prime }$ and $D$ , and the $V _ { i }$ , $i \geq 1$ , are rational surfaces meeting $V _ { 0 }$ along the cycle $D ^ { \prime }$ . A theorem of Shepherd-Barron [34] shows that the divisor $\textstyle \bigcup _ { i = 1 } ^ { n } V _ { i }$ is exceptional in $y$ , although we might also have to contract some rational curves in the general fibers.
(The theorem of Shepherd-Barron is stated in the context of degenerations of $K 3$ surfaces, but the proof applies in this setting as well.)
The result is a singular complex threefold $\mathcal { V }$ and a flat morphism $\bar { \pi } \colon \overline { { \mathcal { V } } }  \Delta$ such that the fiber over 0 is the singular Inoue surface $\overline { { V } } _ { 0 }$ and the general fiber is a rational surface, possibly with rational double points.
In particular, $( X , x )$ is smoothable.
However, the complexity of constructing the possible semistable singular fibers seemed, in the words of [10], “rather daunting.”

Looijenga’s conjecture went unproven until quite recently.
The first proof, due to Gross-Hacking-Keel [14], is based on ideas from the GrossSiebert program [15] for proving mirror symmetry.
The second proof, due to the first author [5], uses ideas from symplectic geometry to construct the semistable models that are required in the approach of [10]. The two proofs can be viewed, respectively, as part of the “algebraic” and the “symplectic” aspects of mirror symmetry for the anticanonical pair $( Y , D )$ . While we have no proven claims regarding mirror symmetry, it serves as an underlying motivation for some of the constructions in this paper.

Mirror symmetry is, very roughly, a prediction originating in physics that Calabi-Yau varieties come in mirror pairs $X$ and $X ^ { m i r }$ on which algebraic and symplectic data are interchanged.
Kontsevich [20] formalized these physical ideas in homological mirror symmetry—that the derived category of coherent sheaves on $X$ is equivalent to the Fukaya category of $X ^ { m a r }$ . The Strominger-Yau-Zaslow program [36] sought to derive a more geometric origin of mirror symmetry—that $X$ and $X ^ { m i r }$ have dual special Lagrangian torus fibrations over a common base $B$ .

Hitchin [17] observed that the base $B$ carries two natural integralaffine structures.
These structures are interchanged by mirror symmetry.
The Gross-Siebert program built on this observation, providing a new interpretation of these integral-affine structures on $B$ in terms of tropical geometry.
Instead of just a Calabi-Yau variety $X$ , one should consider its “large complex structure limit”—a maximally unipotent degeneration ${ \mathcal { X } } \to \Delta$ of $X$ over a disc.
Then one of the affine structures on $B$ is identified via the tropical geometry with the dual complex $\Gamma ( X _ { 0 } )$ of the central fiber.
This affine structure ought to agree with the affine structure on $B$ coming from the symplectic geometry of the Lagrangian torus fibration $X ^ { m i r }  B$ .

It is possible to understand the results of this paper within such a framework.
Observe that a smoothing of $\overline { { V } } _ { 0 } - D$ is a degeneration of the open Calabi-Yau variety $Y - D$ . This degeneration is the large complex structure limit.
One expects then that the dual complex $B = \Gamma ( Y _ { 0 } )$ of the semistable resolution of the central fiber has two natural integralaffine structures.
In Section 2.2 we describe one of these structures, which is the other structure than the one considered by Gross-HackingKeel.
Our affine structure is identified with the base of a Lagrangian torus fibration of the mirror of $Y - D$ over $B$ .

While [14] builds a smoothing of the cusp by a “polytope” construction from their integral-affine structure on $B$ , we follow [5] to build a semistable resolution of a smoothing by a “fan” construction from the other structure.
One advantage of the approach of [14] is the construction of canonical theta functions on the deformation, analogous to theta functions on degenerations of abelian varieties.
Furthermore, our approach only produces a one-parameter smoothing as opposed to a versal deformation of the cusp.
However, the construction here and in [5] has many other advantages: the geometry of the degeneration, central fiber, and significantly, the semistable resolution, are much more explicit.
One can algorithmically build the central fiber of the resolution of a smoothing of the cusp.
Our methods yield a strengthening of Looijenga’s conjecture:

Theorem 0.2. Let $( X , x )$ be a cusp singularity with dual cusp of type $D$ . For each deformation type $[ ( Y , D ) ]$ of an anticanonical pair, there exists a smoothing component of $( X , x )$ of type $[ ( Y , D ) ]$ . Hence the number of smoothing components of $( X , x )$ is at least as large as the number of deformation types $[ ( Y , D ) ]$ .

There are examples where the number of smoothing components of $( X , x )$ is in fact larger than the number of deformation types $[ ( Y , D ) ]$ . For smoothable simple elliptic singularities of high multiplicity, this phenomenon was already observed by Looijenga-Wahl [28]. However, it seems likely that, as in the simple elliptic case, all smoothing components of a cusp singularity of type $[ ( Y , D ) ]$ are essentially isomorphic.

This paper has two goals: to analyze in detail the geometry of one parameter smoothings of cusp singularities via their semistable models, and then to use this study to describe the possible adjacencies of a cusp singularity to a union of rational double points (briefly, a rational double point configuration).
To describe the first goal, we begin by recalling some facts and terminology about anticanonical pairs using [9] as a reference (but these many of these ideas also appear in [13] and, in essence, date back to [27]).

Definition 0.3. Given a deformation type $[ ( Y , D ) ]$ of anticanonical pairs, we have the positive cone

$$
{ \mathcal { C } } = \{ x \in H ^ { 2 } ( Y ; \mathbb { R } ) : x ^ { 2 } > 0 \} ,
$$

which has two components.
Exactly one component $\mathcal { C } ^ { + }$ contains the classes of ample divisors.
Define ${ \mathcal { A } } _ { \mathrm { g e n } } \subseteq { \mathcal { C } } ^ { + }$ to be the “generic ample cone,” i.e. the ample cone of a very general deformation of $( Y , D )$ . It is invariant under the monodromy group of the deformation.
Define $\Lambda = \Lambda ( Y , D )$ be the orthogonal complement in $H ^ { 2 } ( Y ; \mathbb { Z } )$ of the classes $[ D _ { i } ]$ of the components of $D$ and set $\Lambda _ { \mathbb { R } } = \Lambda \otimes \mathbb { R }$ . Let $\overline { { A } } _ { \mathrm { g e n } }$ be the closure of $\mathcal { A } _ { \mathrm { g e n } }$ in the positive cone $\mathcal { C }$ and finally set $\boldsymbol { B } _ { \mathrm { g e n } }$ to be the interior in $\Lambda _ { \mathbb { R } }$ of the intersection $\overline { { \mathcal { A } } } _ { \mathrm { g e n } } \cap \Lambda _ { \mathbb { R } }$ .

One can then describe the monodromy group of the pair $( Y , D )$ as follows:

Definition 0.4. Let $\Gamma = \Gamma ( Y , D )$ , the group of admissible isometries of $( Y , D )$ , be the the group of integral isometries $\gamma$ of $H ^ { 2 } ( Y ; \mathbb { Z } )$ such that $\gamma ( [ D _ { i } ] ) = [ D _ { i } ]$ for all $i$ , $\gamma ( \mathcal { C } ^ { + } ) = \mathcal { C } ^ { + }$ , and

$$
\gamma ( \overline { { \mathcal { A } } } _ { \mathrm { g e n } } ( Y ) ) = \overline { { \mathcal { A } } } _ { \mathrm { g e n } } ( Y ) .
$$

In particular, $\Gamma$ acts on the sets $\boldsymbol { B } _ { \mathrm { g e n } }$ and $B _ { \mathrm { g e n } } \cap \Lambda$ .

Given a one parameter smoothing $\overline { { \pi } } \colon ( \mathcal { V } , \mathcal { D } ) \to \Delta$ of the pair $( V _ { 0 } , D )$ over the disk $\Delta$ such that $\mathcal { D } \cong D \times \Delta$ , we can find a “good” semistable model $\pi \colon ( \mathcal { V } , \mathcal { D } ) \to \Delta$ (possibly after a base change).
Here good roughly means that $\mathcal { V }$ is smooth and that the scheme-theoretic fiber $Y _ { 0 }$ over $0 \in \Delta$ has reduced normal crossings and satisfies $\omega _ { Y _ { 0 } } \cong \mathcal { O } _ { Y _ { 0 } } ( - D )$ , where $\omega _ { Y _ { 0 } }$ is the dualizing sheaf.
We shall refer to the family $\pi \colon ( \mathcal { V } , \mathcal { D } ) \to \Delta$ as a Type III degeneration of rational surfaces.
The detailed properties of $Y _ { 0 }$ are described in Definition 2.1.

We turn next to the description of the monodromy of a Type III degeneration of rational surfaces.
It is easy to show that, if $( Y , D )$ is a negative-definite anticanonical pair, then there is an exact sequence

$$
0 \to \mathbb { Z } \to H _ { 2 } ( Y - D ; \mathbb { Z } ) \to \Lambda \to 0 ,
$$

where $\mathbb { Z } = \mathbb { Z } \cdot \gamma$ is the radical of intersection pairing $\bullet$ on $H _ { 2 } ( Y - D ; \mathbb { Z } )$ . In particular, we can define the pairing between an element of $\Lambda$ and

an element of $H _ { 2 } ( Y - D ; \mathbb { Z } )$ . Our first main result is then roughly as follows:

Theorem 0.5. Let $\pi \colon ( \mathcal { V } , \mathcal { D } ) \to \Delta$ be a Type III degeneration of rational surfaces as above.
Let $T$ be the monodromy of the fiber, which acts on Λ and on $H _ { 2 } ( Y - D ; \mathbb { Z } )$ . Then:

(i) For the action of $T$ on $H _ { 2 } ( Y ; \mathbb { Z } )$ , $T = \mathrm { { I d } }$ (ii) There is a unique class $\lambda \in \Lambda$ such that, for all $x \in H _ { 2 } ( Y - D ; \mathbb { Z } )$ ,

$$
T ( x ) = x - \langle \lambda , x \rangle \gamma .
$$

(iii) With $\lambda$ as above, $\lambda ^ { 2 } = v$ , where $v$ is the number of triple points of the singular fiber $Y _ { 0 }$ .\
(iv) For a unique choice of sign, $\pm \lambda \in B _ { \mathrm { g e n } } \cap \Lambda$ .\
(v) The class $\lambda$ generates over $\mathbb { Q }$ the cokernel of the specialization map sp : $H ^ { 2 } ( Y _ { 0 } ; \mathbb { Q } ) \to H ^ { 2 } ( Y _ { t } ; \mathbb { Q } )$ .

It is natural to always choose the sign so that $\lambda \in B _ { \mathrm { g e n } } \cap \Lambda$ . The class $\lambda$ is only well-defined modulo the action of $\Gamma ( Y , D )$ . We define the monodromy invariant to be the image of $\lambda$ in $\Gamma \backslash ( \boldsymbol { B } _ { \mathrm { g e n } } \cap \Lambda )$ , but continue by abuse of notation to denote it by $\lambda$ . Our next result, which is a significant generalization of Theorem 0.2, states that all possible $\lambda$ arise.

Theorem 0.6. Let $D ^ { \prime }$ be the minimal resolution of a cusp singularity for which the dual $D$ sits on a rational surface.
Then for every deformation type of anticanonical pairs $( Y , D )$ and for every class $\lambda \in B _ { \mathrm { g e n } } \cap \Lambda$ , there exists a Type III degeneration of rational surfaces whose general fiber is deformation equivalent to $( Y , D )$ and whose monodromy invariant is $\lambda$ mod $\Gamma ( Y , D )$ .

Though the statements of Theorem 0.2 and Theorem 0.6 are purely algebraic, the method of proof relies on symplectic geometry, and in particular the geometry of Lagrangian torus fibrations.
There is a naturally defined singular integral-affine structure on the dual complex $\Gamma ( Y _ { 0 } )$ of the central fiber of a Type III degeneration of rational surfaces, defined in Section 2.2. When $Y _ { 0 }$ is generic, see Definition 2.9, work of Symington [37] allows us to construct a Lagrangian almost toric fibration of a symplectic 4-manifold with a degenerate symplectic anticanonical divisor $D$ :

$$
\mu \colon ( X , D , \omega )  \Gamma ( Y _ { 0 } ) .
$$

In Section 3.3, we prove that $( X , D )$ and $( Y _ { t } , D _ { t } )$ are naturally diffeomorphic, and that the fiber class of $\mu$ is identified under this diffeomorphism with $\gamma$ while the class $[ \omega ]$ is identified with $\lambda$ . The validity of this result is essentially a fluke of two dimensions—the 4-manifold $( X , D , \omega )$ is the symplectic mirror of the algebraic degeneration $y  \Delta$ and thus ought to carry a dual Lagrangian torus fibration, but dual fibrations of

2-tori are diffeomorphic because the inverse transpose of a $2 \times 2$ matrix happens to be conjugate to the original matrix.
Regardless, it is this result which allows us to bound below the number of smoothing components, by bounding below the diffeomorphism types of general fibers $( Y _ { t } , D _ { t } )$ .

The identification of the dual complex $\Gamma ( Y _ { 0 } )$ with the base of a Lagrangian torus fibration also provides a method for constructing smoothings.
If one can construct a Lagrangian fibration

$$
\mu \colon ( X , D , \omega )  S ^ { 2 }
$$

such that the natural integral-affine structure on the base of $\mu$ admits an appropriate triangulation, then the base is, as an integral-affine manifold, the dual complex of the central fiber of a Type III degeneration.
Thus, producing a degeneration with prescribed monodromy invariant $\lambda$ reduces to the construction of a Lagrangian torus fibration $( X , D , \omega )  S ^ { 2 }$ such that $[ \omega ] = \lambda$ . This is the goal of Sections 4 and 5.

By analogy with the case of $K 3$ surfaces, it is natural to conjecture that the monodromy invariant $\lambda$ mod $\Gamma$ is a complete invariant of the singular fiber of a Type III degeneration of rational surfaces up to locally trivial deformation and standard birational modifications.
We discuss this conjecture in more detail in Section 5.

Finally, we apply the above results to the study of rational double point adjacencies of cusps.
First, we recall Looijenga’s definition of certain distinguished elements of square $- 2$ in $\Lambda ( Y , D )$ .

Definition 0.7. Let $( Y , D )$ be an anticanonical pair, and let $\beta \in$ $\Lambda ( Y , D )$ with $\beta ^ { 2 } = - 2$ . Then $\beta$ is a Looijenga root or briefly a root if there exists a deformation of $( Y , D )$ over a connected base $S$ and a fiber $( Y _ { s } , D _ { s } )$ over $s \in S$ such that, in $\Lambda ( Y _ { s } , D _ { s } )$ , $\beta$ is the class of a smooth curve $C \cong \mathbb { P } ^ { 1 }$ disjoint from $D _ { s }$ . We let $R \subseteq \Lambda ( Y , D )$ be the set of roots.
If $D$ is negative-definite and has at most 5 components (equivalently, the dual cusp has multiplicity at most 5), then $R$ is a generalized root system of hyperbolic type, and in particular it spans $\Lambda$ . However, when the number of components of $D$ is larger than 5, there are many possibilities for the behavior of $R$ .

We can then describe the possible rational double point adjacencies of a cusp $( X , x )$ as follows.
Let $D$ be the minimal resolution of the dual cusp and let $( Y , D )$ be an anticanonical pair of type $D$ .

Definition 0.8. Let $\Upsilon$ be a negative definite sublattice of $\Lambda ( Y , D )$ . Then $\Upsilon$ is good if

(i) $\Upsilon$ is spanned by elements of $R$ .\
(ii) There exists a homomorphism $\varphi \colon \Lambda ( Y , D ) \to \mathbb { C } ^ { * }$ such that $\operatorname { K e r } \varphi \cap$ $R = \Upsilon \cap R$ .

The lattice $\Upsilon$ determines an RDP configuration (possibly consisting of more than one singular point) by taking the appropriate type (i.e. Dynkin diagram) of a set of simple roots for $\Upsilon \cap R$ . We say that the corresponding rational double point configuration is of type $\Upsilon$ .

We can then state our result about adjacencies of cusps to rational double points as follows:

Theorem 0.9. Suppose that $( X , x )$ is adjacent to a rational double point configuration on a smoothing component of type $[ ( Y , D ) ]$ . Then the components of the exceptional fibers of a minimal resolution span a good negative definite sublattice $\Upsilon$ of $\Lambda ( Y , D )$ , and the rational double point configuration is of type $\Upsilon$ .

Conversely, if Υ is a good negative definite sublattice of $\Lambda ( Y , D )$ , then there exists an adjacency of $( X , x )$ to a rational double point configuration of type Υ on some smoothing component of type $[ ( Y , D ) ]$

An equivalent and more geometric form of the above characterization is given in Proposition 9.6.

Remark 0.10. It is natural to conjecture that, given the good sublattice $\Upsilon$ of $\Lambda ( Y , D )$ , then there exists an adjacency of $( X , x )$ to a rational double point configuration of type $\Upsilon$ on every smoothing component of type $[ ( Y , D ) ]$ .

The methods of this paper say nothing about adjacencies of the cusp $( X , x )$ to non-rational singularities.
If $( X , x )$ is adjacent to a union of singularities, then at most one can be non-rational and all others are rational double points.
Moreover, the non-rational singularity, if it exists, is either a cusp singularity or a simple elliptic singularity.
Wahl described various adjacencies between elliptic singularities in [38], and P. Hacking (unpublished) has shown that these are the only possible adjacencies for cusp singularities.
More generally, one can make fairly precise conjectures about the possible adjacencies from a cusp to a union of an elliptic singularity and a number of rational double points (conjecturally a union of $A _ { k }$ singularities), which generalize Looijenga’s results for multiplicity at most 5. However, we shall not do so here.

A description of the contents of this paper is as follows: Section 1 deals with certain preliminary results on the geometry and topology of anticanonical pairs.
In Section 2, we study Type III degenerations of rational surfaces and in particular the possible singular fibers $Y _ { 0 }$ . Such a fiber has reduced normal crossings, and there is a unique component isomorphic to an Inoue surface $V _ { 0 }$ , with the dual cycle $\boldsymbol { D }$ contained in the smooth locus of $Y _ { 0 }$ . We call the pair $( Y _ { 0 } , D )$ a Type III anticanonical pair.
Although the Inoue surface $V _ { 0 }$ is not K¨ahler, there are analogues of a mixed Hodge structure and a limiting mixed Hodge structure for $Y _ { 0 }$ . We study the relevant spectral sequences and determine when they degenerate.
A general theme is that it is more useful to consider the topology of the pair $( Y _ { 0 } , D )$ as opposed to that of $Y _ { 0 }$ . We also introduce a singular integral-affine structure on the dual complex $\Gamma ( Y _ { 0 } )$ , and describe the almost toric fibration $( X , D , \omega )  \Gamma ( Y _ { 0 } )$ . We also describe the deformation theory of the pair $( Y _ { 0 } , D )$ in an appropriate sense.
Section 3 deals with the monodromy of a smoothing of the pair $( Y _ { 0 } , D )$ . In particular, we prove Theorem 0.5. We also prove that $( X , D , \omega )$ is naturally diffeomorphic to the general fiber $Y _ { t }$ of the Type III degeneration of rational surfaces with central fiber $Y _ { 0 }$ . Theorem 0.2 follows.
Furthermore, we show that the monodromy invariant $\lambda$ from Theorem 0.5 is identified under this diffeomorphism with the class of the symplectic form $[ \omega ]$ . In Sections 4 and 5 we prove Theorem 0.6. Section 4 collects results concerning birational modification and base change of Type III degenerations, and records their effect on the integral-affine structure defined on $\Gamma ( Y _ { 0 } )$ . In Section 5, we construct a Type III degeneration with arbitrary monodromy invariant $\lambda \in B _ { \mathrm { g e n } } \cap \Lambda$ , the method being to first construct the dual complex of the central fiber via surgeries on integral-affine surfaces.
Section 6 uses the description of the monodromy and the limiting cohomology to give an asymptotic formula for the period map of a general fiber in a Type III degeneration of rational surfaces.
Sections 7 and 8 are devoted to a study of an analogue of the period map for a Type III anticanonical pair.
We calculate the differential of the period map in Section 7 and, using this calculation, show in Section 8 that the period map is surjective for topologically trivial deformations of the pair $( Y _ { 0 } , D )$ . Moreover, for suitable lattices $\Upsilon$ inside an appropriate quotient of $\operatorname { P i c } Y _ { 0 }$ , we show that we can arrange a deformation of the pair $( Y _ { 0 } , D )$ so that the image of $\Upsilon$ is in the kernel of the period map for all smooth fibers $( Y _ { t } , D )$ . Finally, in Section 9, we prove Theorem 0.9. The strategy of the proof is as follows.
Given a good lattice $\Upsilon$ in $\Lambda ( Y , D )$ , we show that there exists a $\lambda \in B _ { \mathrm { g e n } } \cap \Lambda$ such that $\Upsilon$ is orthogonal to $\lambda$ . By Theorem 0.6, there exists a Type III degeneration of rational surfaces $( \mathcal { V } , \mathcal { D } )$ with invariant $\lambda$ . Using (v) of Theorem 0.5, we can identify $\Upsilon$ with a quotient of $\operatorname { P i c } Y _ { 0 }$ . By the surjectivity of the period map for $( Y _ { 0 } , D )$ , we can assume after deforming $( Y _ { 0 } , D )$ that $\Upsilon$ is exactly the kernel of the period map and that the same is true for all nearby smooth fibers $( Y _ { t } , D )$ . It then follows by invoking the full strength of Shepherd-Barron’s contraction result that, after blowing down all components of the central fiber not equal to $V _ { 0 }$ as well as some curves in the general fiber, we exactly contract the curves in a general fiber $Y _ { t }$ whose classes lie in $\Upsilon$ . Thus we obtain an adjacency of the cusp to a rational double point of type $\Upsilon$ .

Acknowledgements.
It is a pleasure to thank Eduard Looijenga and Radu Laza for helpful discussions and correspondence.
In addition, we thank for the referee for their careful reading and comments.

# 1. Preliminaries

# 1.1. Topology of anticanonical pairs.

Definition 1.1. Let $D = D _ { 1 } + \cdot \cdot \cdot + D _ { r }$ be a reduced cycle of smooth rational curves for $r \geq 2$ , or an irreducible nodal curve whose normalization is smooth rational for $r = 1$ . The integer $r = r ( D )$ is the length of $D$ . By convention, we take the indices $i$ mod $r$ and $D _ { i } \cap D _ { j } = \emptyset$ for $j \neq i \pm 1$ . An orientation for $D$ is a choice of generator for $H _ { 1 } ( D ; \mathbb { Z } ) \cong \mathbb { Z }$ . For $i \geq 3$ , an orientation determines and is determined by an indexing of the components of $D$ as above up to cyclic permutation, and we always assume that the indexing and the orientation are compatible in this sense.
Given an indexing of the components, we always assume that there is an associated type of $\boldsymbol { D }$ , which by definition is a sequence $( d _ { 1 } , \ldots , d _ { r } )$ of integers $d _ { i }$ , such that $d _ { i } \leq - 2$ for all $i$ and $d _ { i } \leq - 3$ for at least one $i$ . If $D$ is given as a Cartier divisor in a surface, we always assume that $d _ { i } = D _ { i } ^ { 2 }$ .

An anticanonical pair or simply pair $( Y , D )$ is a rational surface $Y$ with an anticanonical divisor $D \in \vert - K _ { Y } \vert$ which forms a reduced cycle of smooth rational curves $D = D _ { 1 } + \cdots + D _ { r }$ unless $r = 1$ in which case $D$ is a nodal rational curve.
The pair $( Y , D )$ is of type $D$ if the type of $D$ is $( D _ { 1 } ^ { 2 } , \ldots , D _ { r } ^ { 2 } )$ . We say $( Y , D )$ is toric if $V$ is a smooth toric surface and $D$ is the toric boundary.

Let $( Y , D )$ be an anticanonical pair.
Enumerate the components of $D$ as $D _ { 1 } , \ldots , D _ { r }$ and the set of nodes $T$ as $t _ { 1 } , \ldots , t _ { r }$ , with the convention that $D _ { i } \cap D _ { i + 1 } = \{ t _ { i } \}$ . If $[ D _ { i } ]$ denotes the class of the component $D _ { i }$ in $H ^ { 2 } ( Y ; \mathbb { Z } )$ , let $\Lambda = \Lambda ( Y , D ) = \{ [ D _ { 1 } ] , \ldots , [ D _ { r } ] \} ^ { \perp } \subseteq H ^ { 2 } ( Y ; \mathbb { Z } )$ . By definition $\Lambda$ is a primitive sublattice of $H ^ { 2 } ( Y ; \mathbb { Z } )$ . Its dual lattice $\Lambda ^ { \vee }$ is described as follows: let $\widehat { \mathrm { s p a n } } \{ [ D _ { 1 } ] , \ldots , [ D _ { r } ] \}$ be the saturation of the subgroup of $H ^ { 2 } ( Y ; \mathbb { Z } )$ generated by $[ D _ { 1 } ] , \ldots , [ D _ { r } ]$ . Then

$$
\begin{array} { r } { \Lambda ^ { \vee } = H ^ { 2 } ( Y ; \mathbb { Z } ) / \widehat { \mathrm { s p a n } } \{ [ D _ { 1 } ] , \ldots , [ D _ { r } ] \} . } \end{array}
$$

Via the Gysin spectral sequence (the Leray spectral sequence applied to the inclusion $i \colon Y - D \hookrightarrow Y$ ) there is an exact sequence

$$
0 \to H ^ { 2 } ( Y ; \mathbb { Z } ) / \operatorname { s p a n } \{ [ D _ { 1 } ] , \dots , [ D _ { r } ] \} \to H ^ { 2 } ( Y - D ; \mathbb { Z } ) \to \mathbb { Z } \to 0 ,
$$

where the right hand $\mathbb { Z }$ is the kernel of the Gysin map.
Thus, if $\overline { { H } } ^ { 2 } ( Y -$ $D ; \mathbb { Z } )$ denotes $H ^ { 2 } ( Y - D ; \mathbb { Z } )$ mod torsion, there is an exact sequence

$$
0 \to \Lambda ^ { \vee } \to \overline { { { H } } } ^ { 2 } ( Y - D ; \mathbb { Z } ) \to \mathbb { Z } \to 0 .
$$

Dually, there is an exact sequence

$$
0 \to \mathbb { Z } \to H _ { 2 } ( Y - D ; \mathbb { Z } ) \to \Lambda \to 0 ,
$$

arising from the exact sequence of the pair $( Y , Y - D )$ :

$$
0 = H _ { 3 } ( Y ; \mathbb { Z } ) \to H _ { 3 } ( Y , Y - D ; \mathbb { Z } ) \to H _ { 2 } ( Y - D ; \mathbb { Z } ) \to H _ { 2 } ( Y ; \mathbb { Z } ) .
$$

Poincar´e-Alexander duality identifies $H _ { 3 } ( Y , Y - D ; \mathbb { Z } )$ with $H ^ { 1 } ( D ; \mathbb { Z } ) =$ $\mathbb { Z }$ , and the image of $H _ { 2 } ( Y - D ; \mathbb { Z } ) \to H _ { 2 } ( Y ; \mathbb { Z } )$ corresponds exactly to those 2-cycles which have algebraic intersection 0 with every component of $D$ , and thus via Poincar´e duality with $\Lambda$ . In terms of compactly supported cohomology, we have a commutative diagram

$$
\begin{array} { r l } & { { \cal I } _ { 3 } ( Y , Y - D ; \mathbb { Z } ) \longrightarrow H _ { 2 } ( Y - D ; \mathbb { Z } ) \longrightarrow H _ { 2 } ( Y ; \mathbb { Z } ) } \\ & { \qquad \cong \Big \downarrow \cong } \\ & { \qquad H ^ { 1 } ( D ; \mathbb { Z } ) \longrightarrow H _ { c } ^ { 2 } ( Y - D ; \mathbb { Z } ) \longrightarrow H ^ { 2 } ( Y ; \mathbb { Z } ) \longrightarrow H ^ { 2 } ( D ; \mathbb { Z } ) } \end{array}
$$

Let $V$ be a small tubular neighborhood of $D$ in $Y$ , homotopy equivalent to $D$ , so that $Y - V$ is homotopy equivalent to $Y - D$ . Let $\partial = \partial V$ . Using the Mayer-Vietoris sequence applied to the decomposition $Y =$ $( Y - D ) \cup V$ , one easily computes that $H ^ { 1 } ( \partial ; \mathbb { Z } ) \cong H ^ { 1 } ( D ; \mathbb { Z } ) \cong \mathbb { Z }$ and that $H ^ { 2 } ( \partial ; \mathbb { Z } )$ has rank one.
The exact sequence for the pair $( Y - V , \partial )$ , which we shall write as $( Y - D , \partial )$ , is then (all groups with $\mathbb { Z }$ -coefficients)

$$
H ^ { 1 } ( Y - D ) = 0  H ^ { 1 } ( \partial )  H ^ { 2 } ( Y - D , \partial )  H ^ { 2 } ( Y - D )  H ^ { 2 } ( \partial )
$$

Lefschetz duality identifies $H ^ { 2 } ( Y - D , \partial )$ with $H _ { 2 } ( Y - D ; \mathbb { Z } )$ and identifies the image of $H ^ { 1 } ( \partial )$ with the subgroup $\mathbb { Z }$ above.
Moreover, Lefschetz duality is compatible with Poincar´e duality on $\partial$ , which identifies $H ^ { 1 } ( \partial )$ with $H _ { 2 } ( \partial )$ , and with the exact sequence of the pair $( Y - D , \partial )$ , so that the above exact sequence is identified with

Poincar´e duality identifies $\overline { { H } } _ { 2 } ( Y - D , \partial )$ with ${ \overline { { H } } } ^ { 2 } ( Y - D ; \mathbb { Z } )$ , and hence there is an inclusion of $\Lambda ^ { \vee }$ in $H _ { 2 } ( Y - D , \partial )$ for which the following diagram commutes:

$$
\begin{array} { r } { \frac { H _ { 2 } ( Y - D ; \mathbb { Z } ) } { \Lambda } \longrightarrow \overline { { H } } _ { 2 } ( Y - D , \partial ) } \\ { \Big \downarrow \qquad \Big \uparrow \qquad \Big \uparrow \qquad } \\ { \qquad \Lambda \qquad \longrightarrow \qquad \Lambda ^ { \vee } . } \end{array}
$$

It is easy to check that a generator of $H _ { 2 } ( \partial )$ is the class $\gamma$ which is the tube (with respect to some Hermitian metric) over a simple closed curve in $D _ { i }$ enclosing a double point: for example, there exists a curve $\gamma ^ { \prime }$ on $\partial$ projecting onto the generator of $H _ { 1 } ( D ; \mathbb { Z } )$ , and then $\gamma \bullet \gamma ^ { \prime } = \pm 1$ . Identifying $\gamma$ with its image in $H _ { 2 } ( Y - D ; \mathbb { Z } )$ , we see that the kernel of $H _ { 2 } ( Y - D ; \mathbb { Z } ) \to \Lambda$ is $\mathbb { Z } \gamma$ . Note that $\gamma$ is only well-defined up to sign, but is determined by an orientation of the cycle $D$ .

1.2. The generic ample cone and effective cone.
We recall the following terminology from [9] (see also [13]). Let $\mathcal { C } \subseteq H ^ { 2 } ( Y ; \mathbb { R } )$ be the positive cone and let $\mathcal { C } ^ { + }$ be the component of $\mathcal { C }$ containing the classes of ample divisors.
Inside $\mathcal { C } ^ { + }$ , we have the convex cone $\overline { { \mathcal { A } } } _ { \mathrm { g e n } }$ , which is the closure in $\mathcal { C } ^ { + }$ of the ample cone for a generic small deformation of

$Y$ . We define a $- 2$ -curve on $Y$ to be a smooth rational curve on $Y$ of self-intersection $- 2$ which is not a component of $\boldsymbol { D }$ , and define $Y$ to be generic if there are no $- 2$ -curves on $Y$ . If $Y$ is generic, then

For a generic $Y$ , we may replace the condition $x \cdot [ E ] \geq 0$ for all exceptional curves $E$ by the condition $x \cdot \alpha \geq 0$ for all effective numerical exceptional curves $\alpha$ , i.e. cohomology classes $\alpha$ such that $\alpha ^ { 2 } = \alpha \cdot \left[ K _ { Y } \right] =$ $- 1$ and $\alpha$ is the class of an effective divisor, or equivalently $\alpha \cdot \left[ H \right] \geq 0$ for some ample divisor $H$ [9, §5]. We set $\mathcal { A } _ { \mathrm { g e n } }$ equal to the interior of ${ \overline { { \mathcal { A } } } } _ { \mathrm { g e n } }$ .

We can omit the assumption that $x \in { \mathcal { C } }$ lies in the component $\mathcal { C } ^ { + }$

Lemma 1.2. If $x \in \mathcal { C }$ , and $x \cdot \alpha \geq 0$ for all effective numerical exceptional curves $\alpha$ and $x \cdot [ D _ { i } ] \geq 0$ for all $i$ , then $x \in { \mathcal { C } } ^ { + }$ .

Proof.
An easy induction on the number of blowups required to obtain $Y$ from a minimal surface shows that the union of the $D _ { i }$ and the effective numerical exceptional curves supports a nef and big divisor $H$ . Thus, for $x$ as in the hypothesis of the lemma, $x \cdot H \geq 0$ and so $x \in { \mathcal { C } } ^ { + }$ . q.e.d.

Definition 1.3. Let $\boldsymbol { B } _ { \mathrm { g e n } }$ be the interior of $\overline { { A } } _ { \mathrm { g e n } } \cap \Lambda _ { \mathbb { R } }$ in $\Lambda _ { \mathbb { R } } = \Lambda \otimes \mathbb { R }$ . Thus by definition, for $x \in \Lambda _ { \mathbb { R } }$ , $x \in \mathcal { B } _ { \mathrm { g e n } } \iff x \in \Lambda _ { \mathbb { R } } \cap \mathcal { C } ^ { + }$ and $x \cdot \alpha > 0$ for all effective numerical exceptional curves $\alpha$ . Note that, since the set of walls defined by the numerical exceptional classes and the $[ D _ { i } ]$ is locally finite in $\mathcal { C } ^ { + }$ , $\boldsymbol { B } _ { \mathrm { g e n } }$ is a nonempty open convex subset of $\Lambda _ { \mathbb { R } }$ .

Definition 1.4. A corner blow-up of $( Y , D )$ is a blow-up at a node of $D$ and an internal blow-up of $( Y , D )$ is a blow-up on the smooth locus of $D$ . Both the corner and internal blow-up have an anticanonical divisor $\pi ^ { * } D - E$ where $\pi$ is the blow-up and $E$ is the exceptional divisor.
An internal exceptional curve is an exceptional curve which is not a component of $D$ .

The dual of the ample cone is the effective cone.
The extremal rays of the effective cone are the classes of curves of negative self-intersection— generically, the internal exceptional curves and components of $D$ . With a mild assumption, every effective divisor on $Y$ is linearly equivalent to a union of components $D$ and disjoint internal exceptional curves:

Proposition 1.5. Let $( Y , D )$ be an anticanonical pair with $r ( D ) \geq 3$ and no $- 2$ -curves, besides components of $D$ . If $A$ is an effective curve on $Y$ , then $A$ is linearly equivalent to a curve of the form

$$
\sum a _ { j } D _ { j } + \sum b _ { i } E _ { i } ,
$$

where the $E _ { i }$ are disjoint internal exceptional curves and $a _ { j } , b _ { j } \geq 0$

Proof.
We begin with the following lemma:

Lemma 1.6. Let $G$ be an effective, nef, and nonzero divisor on $Y$ . Then there exists a component $D _ { j }$ of $D$ and an element of $| G |$ of the form $B + D _ { j }$ , where $B$ is effective.

Proof.
We may clearly assume that no component of $D$ is a fixed component of $| G |$ . Since $H ^ { 2 } ( Y ; { \mathcal O } _ { Y } ( G ) ) = 0$ , Riemann-Roch implies that

$$
h ^ { 0 } ( Y ; { \mathcal O } _ { Y } ( G ) ) = h ^ { 1 } ( Y ; { \mathcal O } _ { Y } ( G ) ) + \frac { 1 } { 2 } ( G ^ { 2 } + G \cdot D ) + 1 .
$$

Hence $h ^ { 0 } ( Y ; { \mathcal { O } } _ { Y } ( G ) ) \geq 2$ if $G \cdot D \neq 0$ . If $G \cdot D = 0$ , then $h ^ { 1 } ( Y ; { \mathcal { O } } _ { Y } ( G ) ) \geq$ $1$ by [9, Lemma 4.13], and so again $h ^ { 0 } ( Y ; { \mathcal { O } } _ { Y } ( G ) ) \geq 2$ . It follows that $\dim | G | \geq 1$ , so that, for every point $y$ of $Y$ , there exists a curve in $| G |$ passing through $y$ . Hence, if there exists a component $D _ { j }$ of $D$ such that $G \cdot D _ { j } = 0$ , then there exists a curve in $| G |$ meeting $D _ { j }$ and thus necessarily of the form $B + D _ { j }$ for some effective $B$ . In particular, if $G \cdot D \leq 2$ , then the assumption $r ( D ) \geq 3$ implies that such a component $D _ { j }$ must exist.

If $G ^ { 2 } = 0$ , then by [9, Theorem 4.19], $G$ is either of the form $k C$ , $k \geq 1$ , where $C \cdot D = 2$ , or of the form $k E$ where $E \cdot D = 0$ . In either case, there is a component $D _ { j }$ of $D$ such that $G \cdot D _ { j } = 0$ and we are done by the previous paragraph.
Thus, we may assume that $G ^ { 2 } > 0$ , i.e. that $G$ is big, and that $G { \cdot } D _ { j } > 0$ for every $j$ . By Ramanujam’s lemma (cf.
[9, Lemma 4.10]), the restriction map $H ^ { 0 } ( Y ; \mathcal { O } _ { Y } ( G ) ) \to H ^ { 0 } ( D ; \mathcal { O } _ { Y } ( G ) | D )$ is surjective.
The line bundle $\mathcal { O } _ { Y } ( G ) | D$ has positive degree on every component of $D$ . Choosing a component $D _ { j }$ , it is then easy, using the assumption $r ( D ) \geq 3$ , to construct a nonzero section of $\mathcal { O } _ { Y } ( G ) | D$ which vanishes identically on $D _ { j }$ . Lifting this section to a section of ${ \mathcal { O } } _ { Y } ( G )$ then gives a curve in $| G |$ which contains $D _ { j }$ as desired.
q.e.d.

Returning to the proof of Proposition 1.5, every curve in $| A |$ is of the form $\sum a _ { j } D _ { j } + \sum b _ { i } C _ { i }$ , where the $a _ { j } , b _ { i } \geq 0$ and the $C _ { i }$ are distinct irreducible curves which are not components of $D$ . Clearly the sum $\sum a _ { j }$ is bounded.
We may thus choose such a curve for which $\sum a _ { j }$ is maximal, possibly zero.
Since there are no $- 2$ -curves on $Y$ , one of the following holds:

(i) Some $C _ { i }$ is not exceptional.\
(ii) Every $C _ { i }$ is exceptional but two intersect.\
(iii) The $C _ { i }$ are disjoint exceptional curves.

If $C _ { i }$ is not exceptional, then it is nef and we can apply Lemma 1.6 to find an effective curve $C _ { i } ^ { \prime }$ linearly equivalent to $C _ { i }$ which contains $D _ { k }$ for some $k$ . But then there is a curve in $| A |$ of the form $\sum a _ { j } ^ { \prime } D _ { j } + \sum b _ { i } C _ { i } ^ { \prime }$ as above with $\textstyle \sum _ { j } a _ { j } ^ { \prime } > \sum a _ { j }$ , contradicting the hypothesis on $\sum a _ { j }$ is maximal.
Likewise, if there exist $i _ { 1 } , i _ { 2 }$ such that $C _ { i _ { 1 } } \cdot C _ { i _ { 2 } } > 0$ , then $\boldsymbol { G } = \boldsymbol { C } _ { i _ { 1 } } + \boldsymbol { C } _ { i _ { 2 } }$ is nef, and we again reach a contradiction by Lemma 1.6.

Thus we are in Case (iii), which is the statement of Proposition 1.5.\
q.e.d.

Remark 1.7. It is easy to see that the assumption $r ( D ) \geq 3$ is necessary.
For example, the class of a fiber on the a minimal anticanonical pair $( \mathbb { F } _ { N } , D _ { 1 } + D _ { 2 } )$ , where $D _ { 1 }$ and $D _ { 2 }$ are both irreducible sections, cannot be expressed as a linear combination of the components of $D$ .

# 2. Type III degenerations

# 2.1. Preliminaries.

Definition 2.1. A Type III degeneration of anticanonical pairs is a proper morphism $\pi \colon ( \mathcal { V } , \mathcal { D } )  \Delta$ , where $y$ is a smooth complex 3- fold, $\Delta$ is the unit disk, and $\mathcal { D } \to \Delta$ is a locally trivial relative normal crossings divisor in $\mathcal { V }$ whose intersection with the fiber $Y _ { t }$ is denoted by $D _ { t }$ for all $t$ , such that:

(i) The general fibers $\pi ^ { - 1 } ( t ) = ( Y _ { t } , D _ { t } )$ , $t \neq 0$ are anticanonical pairs and the central fiber $\pi ^ { - 1 } ( 0 ) = ( Y _ { 0 } , D _ { 0 } )$ with $\textstyle Y _ { 0 } = \bigcup _ { i = 0 } ^ { f - 1 } V _ { i }$ is a reduced normal crossings divisor.\
(ii) $V _ { 0 }$ is the Hirzebruch-Inoue surface with dual cycles $D$ and $D ^ { \prime }$ . The normalization $\ddot { V _ { i } }$ of $V _ { i }$ is a smooth rational surface for $i \neq 0$ . Furthermore $D _ { 0 } = D$ .\
(iii) Let $C _ { i }$ denote the union of the double curves $C _ { i j } = V _ { i } \cap V _ { j }$ which lie on $V _ { i }$ . Then the inverse image of $C _ { i }$ under the normalization map is an anticanonical divisor on $\tilde { V _ { i } }$ for $i ~ > ~ 0$ and $C _ { 0 } = D ^ { \prime }$ . Equivalently, $K y = \mathcal { O } y ( - \mathcal { D } )$ .

(iv) The triple point formula holds:

$$
\left( C _ { i j } { \big | } _ { \tilde { V _ { i } } } \right) ^ { 2 } + \left( C _ { i j } { \big | } _ { \tilde { V _ { j } } } \right) ^ { 2 } = \left\{ \begin{array} { l l } { - 2 } & { \mathrm { i f ~ } C _ { i j } \ \mathrm { i s ~ s m o o t h } } \\ { 0 } & { \mathrm { i f ~ } C _ { i j } \ \mathrm { i s ~ n o d a l . } } \end{array} \right.
$$

(v) The dual complex $\Gamma ( Y _ { 0 } )$ is a triangulation of the sphere.

A Type III anticanonical pair is a pair $( Y _ { 0 } , D _ { 0 } )$ , where $Y _ { 0 }$ is a reduced surface with simple normal crossings and $D _ { 0 }$ is a Cartier divisor on $Y _ { 0 }$ , satisfying (ii)-(v) above.
We say $( Y _ { 0 } , D _ { 0 } )$ is $d$ -semistable if in addition

$$
T _ { Y _ { 0 } } ^ { 1 } = E x t ^ { 1 } ( \Omega _ { Y _ { 0 } } ^ { 1 } , { \mathcal { O } } _ { Y _ { 0 } } ) \cong { \mathcal { O } } _ { ( Y _ { 0 } ) _ { \mathrm { s i n g } } } ,
$$

which is an analytic refinement of the triple point formula.
By [10, (2.6) and (2.9)], every Type III anticanonical pair can be deformed via a locally trivial deformation to one which is $d$ -semistable, and (as we shall discuss later) every $d$ -semistable Type III anticanonical pair can be smoothed in a one parameter family with smooth total space.

Notation 2.2. To simplify the notation, we will henceforth suppress the tildes on $\tilde { V _ { i } }$ so that $( V _ { i } , C _ { i } )$ denotes a smooth anticanonical pair.
In addition, we introduce the convention

$$
C _ { i j } = C _ { i j } \big | _ { V _ { i } } \mathrm { a n d } C _ { j i } = C _ { i j } \big | _ { V _ { j } }
$$

so that $C _ { i j }$ always denotes a curve on the smooth surface $V _ { i }$ . Then $C _ { i j }$ and $C _ { j i }$ have the same image in $Y _ { 0 }$ but may not be isomorphic.
In fact, the image of $C _ { i j }$ in $Y _ { 0 }$ is nodal if and only if exactly one of $C _ { i j }$ or $C _ { j i }$ is nodal.
We define

$$
c _ { i j } : = { \left\{ \begin{array} { l l } { - c _ { i j } ^ { 2 } } & { { \mathrm { i f ~ } } r ( C _ { i } ) \geq 2 } \\ { 2 - c _ { i j } ^ { 2 } } & { { \mathrm { i f ~ } } r ( C _ { i } ) = 1 . } \end{array} \right. }
$$

Then, the triple point formula states that $c _ { i j } + c _ { j i } = 2$ in all cases.

Definition 2.3. The charge of a pair $( V , C )$ is the integer

$$
Q ( V , C ) : = 1 2 + \sum ( c _ { i } - 3 )
$$

where

$$
c _ { i } = { \left\{ \begin{array} { l l } { - C _ { i } ^ { 2 } } & { { \mathrm { i f ~ } } r ( C ) > 1 } \\ { 2 - C _ { i } ^ { 2 } } & { { \mathrm { i f ~ } } r ( C ) = 1 } \end{array} \right. } .
$$

Then $Q ( V , C ) = 0$ if and only if $( V , C )$ is toric and otherwise $Q ( V , C ) >$ $0$ . A corner blow-up keeps the charge constant, while an internal blowup increases the charge by one.

Remark 2.4. When $( V , C )$ is an anticanonical pair,

$$
Q ( V , C ) = \chi _ { \mathrm { t o p } } ( V - C ) ,
$$

where $\chi _ { \mathrm { t o p } }$ is the (topological) Euler characteristic.
When $V$ is the Hirzebruch-Inoue surface, and $C$ is one of the cycles on $V$ , this formula does not hold.

Proposition 2.5 (Conservation of Charge).
Let $( Y _ { 0 } , D _ { 0 } )$ be a Type III anticanonical pair.
Then $\sum Q ( V _ { i } , C _ { i } ) = 2 4$ .

Proof.
See [10], Proposition 3.7.

# 2.2. The integral-affine structure on the dual complex.

Definition 2.6. An integral-affine manifold of dimension $n$ is a manifold with charts to $\mathbb { R } ^ { n }$ such that the transition functions are valued in the integral-affine transformation group $S L _ { n } ( \mathbb { Z } ) \ltimes \mathbb { R } ^ { n }$ . A lattice manifold is an integral-affine manifold whose transition functions are in $S L _ { n } ( \mathbb { Z } ) \ltimes \mathbb { Z } ^ { n }$ .

Note that a lattice manifold contains a lattice of points with integer coordinates in some (any thus any) chart.
We will endow $\Gamma ( Y _ { 0 } )$ with the structure of a triangulated lattice surface with singularities.
Define the following notation for the dual complex:

(i) The vertices $v _ { i }$ correspond to the components $V _ { i }$ , (ii) the directed edges $e _ { i j } = ( v _ { i } , v _ { j } )$ correspond to double curves $C _ { i j }$ , (iii) the triangular faces $f _ { i j k } = ( v _ { i } , v _ { j } , v _ { k } )$ correspond to triple points $p _ { i j k }$ .

We denote the $i$ -skeleton of $\Gamma ( Y _ { 0 } )$ by $\Gamma ( Y _ { 0 } ) ^ { [ i ] }$ . There is a natural (nonsingular) lattice manifold structure on

$$
\Gamma ( Y _ { 0 } ) - \{ v _ { i } \colon Q ( V _ { i } , C _ { i } ) > 0 \mathrm { ~ o r ~ } i = 0 \}
$$

which we now define, see also Remark 1.11 of Version 1 of [14]. We declare each triangular face $f _ { i j k }$ to be integral-affine equivalent to a basis triangle, that is, a lattice triangle of area $1 / 2$ . Then, we define the integral-affine structure on the union of two triangular faces $f _ { i j k }$ and $f _ { i k \ell }$ that share an edge $e _ { i k }$ by gluing two basis triangles in the plane along their shared edge.
We glue in the unique way such that

$$
c _ { i k } e _ { i k } = e _ { i j } + e _ { i \ell } ,
$$

where we view the directed edges $e _ { i j }$ , $e _ { i k }$ and $e _ { i \ell }$ as integral vectors.
By Propositions 2.2 and 2.3 of [5], this defines a unique integral-affine structure on $\Gamma ( Y _ { 0 } ) - \Gamma ( Y _ { 0 } ) ^ { \left[ 0 \right] }$ which naturally extends to the vertices $v _ { i }$ corresponding to toric pairs $( V _ { i } , C _ { i } )$ .

Definition 2.7. Let $( Y , D )$ be a pair with cycle components $D =$ $D _ { 1 } + \cdots + D _ { n }$ . The pseudo-fan of $( Y , D )$ is an integral-affine surface ${ \mathfrak { F } } ( Y , D )$ PL-equivalent to the cone over the dual complex of $D$ . For each intersection point $t _ { i } = D _ { i } \cap D _ { i + 1 }$ there is an associated face $f _ { i , i + 1 }$ of this cone integral-affine equivalent to a basis triangle.
Let $e _ { i }$ denote the primitive integral vector that originates at the cone point corresponding to some component $D _ { i }$ . We glue $f _ { i - 1 , i }$ and $f _ { i , i + 1 }$ together by an element of $S L _ { 2 } ( \mathbb { Z } )$ in the unique manner such that $e _ { i - 1 } + e _ { i + 1 } = d _ { i } e _ { i }$ where

$$
d _ { i } = { \left\{ \begin{array} { l l } { - D _ { i } ^ { 2 } } & { { \mathrm { i f ~ } } n > 1 } \\ { 2 - D _ { i } ^ { 2 } } & { { \mathrm { i f ~ } } n = 1 } \end{array} \right. } .
$$

The integral-affine structure has at most one singularity, at the cone point.
Compare to Section 1.2 of [14].

Note that the union of the triangles containing a vertex $v _ { i } \in \Gamma ( Y _ { 0 } )$ is the pseudo-fan $\mathfrak { F } ( V _ { i } , C _ { i } )$ .

Example 2.8. We can visualize the lattice structure on $\Gamma ( Y _ { 0 } )$ by cutting it open along a spanning tree of the singular vertices.
The resulting disc has an integral-affine chart to $\mathbb { R } ^ { 2 }$ whose image is a lattice polygon.
Figure 1 below depicts such an open chart.
The intersection complex of $Y _ { 0 }$ is overlaid by the dual complex, and each component of the anticanonical cycle of $( V _ { i } , C _ { i } )$ is labelled by its self-intersection.
The surface $Y _ { 0 }$ visibly satisfies conditions (ii)-(v) of Definition 2.1.

There are three anticanonical pairs $( V _ { i } , C _ { i } )$ with charge $Q ( V _ { i } , C _ { i } ) =$ $1$ , whose cycles of self-intersections are $( 3 , - 1 , - 1 , - 2 )$ , $( 6 , - 1 , - 1 , - 5 )$ , and $( 2 , - 1 , - 1 , - 1 )$ . The Hirzebruch-Inoue surface $V _ { 0 }$ meets the other components of $Y _ { 0 }$ along the cycle $D ^ { \prime } = C _ { 0 }$ whose components have self-intersections $( - 6 , - 9 )$ . Every other component of $Y _ { 0 }$ is toric.

![](images/cc52480cf2fe07423ac7631a9dda2381560ce959291a3e1b0fb81116ea8ceec4.jpg)\
Figure 1. A Type III anticanonical pair $Y _ { 0 }$ and the lattice manifold structure on its dual complex.
Double curves with self-intersection $^ { - 1 }$ on both components are unlabeled.

Definition 2.9. We say that $Y _ { 0 }$ is generic if $Q ( V _ { i } , C _ { i } ) \leq 1$ for all $i \neq 0$ .

Because of the formula $Q ( D ) + Q ( D ^ { \prime } ) = 2 4$ , genericity is equivalent to the condition that $\Gamma ( Y _ { 0 } )$ has $Q ( D ) + 1$ singularities.

Remark 2.10. Integral-affine manifolds appear naturally in symplectic geometry as bases of Lagrangian torus fibrations.
Let $\mu \colon ( X , \omega ) $ $B$ be a Lagrangian 2-torus fibration.
There are natural coordinates from $B$ to $\mathbb { R } ^ { 2 }$ well defined up to $G L _ { 2 } ( \mathbb { Z } ) \ltimes \mathbb { R } ^ { 2 }$ defined as follows: Choose a base point $p _ { 0 } \in B$ and let $U \ni p _ { 0 }$ be a contractible open set.
Let $\{ \alpha , \beta \}$ be a basis of $H _ { 1 } ( \mu ^ { - 1 } ( b _ { 0 } ) ; \mathbb { Z } )$ . Let $p \in U$ be a point, and let $\gamma \colon [ 0 , 1 ] \to U$ satisfy $\gamma ( 0 ) = p _ { 0 }$ , $\gamma ( 1 ) = p$ . Let $\ C _ { \alpha }$ and $C _ { \beta }$ be cylinders in $X$ which fiber over $\gamma$ and whose boundaries in $\mu ^ { - 1 } ( b _ { 0 } )$ are homologous to $\alpha$ and $\beta$ , respectively.
We may then define coordinates $U \to \mathbb { R } ^ { 2 }$ by

$$
\left( x ( p ) , y ( p ) \right) = \left( \int _ { C _ { \alpha } } \omega , \int _ { C _ { \beta } } \omega \right) .
$$

These integrals are well-defined because the fibers of $\mu$ are Lagrangian.
The only ambiguities are the choice of base point, and basis of $H _ { 1 }$ of a fiber; thus the coordinates are well-defined up to $G L _ { 2 } ( \mathbb { Z } ) \ltimes \mathbb { R } ^ { 2 }$ , and in fact lie in $S L _ { 2 } ( \mathbb { Z } ) \ltimes \mathbb { R } ^ { 2 }$ if there is a consistent choice of orientation on the fibers of $\mu$ .

Conversely, given an integral-affine manifold $B$ (without singularities), there is a natural lattice $T _ { \mathbb { Z } } B \subset T B$ in the tangent bundle consisting of tangent vectors which are integral in some, and thus any, chart.
Dualizing gives a lattice $T _ { \mathbb { Z } } ^ { * } B \subset T ^ { * } B$ in the cotangent bundle.
The cotangent bundle $T ^ { * } B$ admits a natural symplectic structure, and addition of a section of $T _ { \mathbb { Z } } ^ { * } B$ is a symplectomorphism.
Thus, there is a Lagrangian torus fibration

$$
\mu : T _ { \mathbb { Z } } ^ { * } B \backslash T ^ { * } B  B
$$

and this procedure locally describes an inverse to the above procedure.
In the local coordinates $( x , y )$ of an integral-affine chart on $B$ , the symplectic form is $\omega = d x \wedge d p + d y \wedge d q$ where $p , q \in \mathbb { R } / \mathbb { Z }$ are coordinates on the torus fibers which descend from the coordinates on fibers of the cotangent bundle.

Symington [37] was able to extend this correspondence in dimension two to Lagrangian fibrations with certain singular fibers.
Suppose there is a Lagrangian fibration of a symplectic 4-manifold $\mu \colon ( X , \omega ) \ \to \ B$ whose general fiber is a 2-torus, but degenerates over some fibers to a necklace of $k$ Lagrangian 2-spheres.
Then the base $B$ admits an integralaffine structure with an $A _ { k }$ singularity at the image of a singular fiber, around which the $S L _ { 2 } ( \mathbb { Z } )$ component of monodromy of the integralaffine structure is conjugate to

$$
{ \binom { 1 } { 0 } } \ k \quad
$$

Conversely, given an integral affine surface $B$ with $A _ { k }$ singularities, there is a Lagrangian torus fibration over $B$ which is unique up to (not necessarily fiber-preserving) symplectomorphism if the base either has a nonempty boundary or is noncompact.

Returning to Type III degenerations, suppose that $Y _ { 0 }$ is generic.
Then every singularity of $\Gamma ( Y _ { 0 } )$ other than $v _ { 0 }$ is of type $A _ { 1 }$ —this follows easily from Propositions 2.9 and 2.10 of [5]. Thus, there is a Lagrangian torus fibration

$$
\mu : ( X , \omega )  \Gamma ( Y _ { 0 } ) - \{ v _ { 0 } \}
$$

with irreducible nodal fibers exactly over the vertices $v _ { i }$ corresponding to pairs with $Q ( V _ { i } , C _ { i } ) = 1$ . The edges in $\Gamma ( Y _ { 0 } ) ^ { [ 1 ] }$ also have an interpretation in the symplectic 4-manifold $X$ : For any straight line segment $y ~ = ~ { \boldsymbol { \mathit { m } } } { \boldsymbol { \mathit { x } } }$ of rational slope in the base, there is a Lagrangian cylinder which fibers over it, whose fiber is the circle $p = - m q$ . Thus, there is a Lagrangian cylinder $A _ { i j }$ which fibers over each edge $e _ { i j }$ .

Proposition 3.14 below proves that $X$ is in fact diffeomorphic to $Y _ { t } - D _ { t }$ . Furthermore, under this diffeomorphism, the class of the symplectic form and the class of the fiber of $\mu$ are naturally identified with the two invariants describing the monodromy on $H _ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { Z } )$ . We prove that every monodromy-invariant class in $H _ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { Z } )$ may be constructed by patching together the $A _ { i j }$ by chains lying over $\Gamma ( Y _ { 0 } ) ^ { [ 0 ] }$ . Thus, the monodromy-invariant classes are represented by Lagrangians and perpendicular to $[ \omega ]$ .

Proposition 2.11. Let $Y _ { 0 }$ be a generic Type III anticanonical pair.
The Lagrangian fibration $\mu _ { 0 } \colon ( X _ { 0 } , \omega )  \Gamma ( Y _ { 0 } ) - \{ v _ { 0 } \}$ extends to a continuous map $\mu : ( X , D , \omega )  \Gamma ( Y _ { 0 } )$ where $X$ is a smooth, compact 4-manifold, $D = \mu ^ { - 1 } ( v _ { 0 } )$ is a cycle of 2-spheres with the appropriate self-intersections, and $\omega$ is the symplectic form on $X _ { 0 } = X - D$ .

Proof.
Let $U \ \ni \ v _ { 0 }$ be a contractible open set in $\Gamma ( Y _ { 0 } )$ containing no singularities other than $v _ { 0 }$ . Then the Lagrangian torus fibration over $U - \{ v _ { 0 } \}$ is, as a smooth 2-torus fibration, uniquely determined by the $S L _ { 2 } ( \mathbb { Z } )$ monodromy around $v _ { 0 }$ . We note that the HirzebruchInoue surface is topologically quite simple: It is a two-torus fibration over an annulus that undergoes symplectic boundary reduction over its two circular boundaries to produce the cycles $D$ and $D ^ { \prime }$ . It then follows easily from computing the monodromy around the vertex of the pseudo-fan $\mathfrak { F } ( V _ { 0 } , C _ { 0 } )$ that $\mu _ { 0 } ^ { - 1 } ( U - \{ v _ { 0 } \} )$ is diffeomorphic to $V _ { 0 } - D - D ^ { \prime }$ and that the boundary component of the annulus over which $D$ fibers corresponds to $v _ { 0 }$ . Thus, we may extend $\mu _ { 0 }$ in the desired manner by gluing $X _ { 0 }$ to a neighborhood of $D$ in $V _ { 0 }$ and declaring $\mu ( D ) = v _ { 0 }$ . q.e.d.

2.3. Topology and geometry of the central fiber.
We now collect various results on the cohomology of $Y _ { 0 }$ (both topological and analytic) and the limiting cohomology.
For notational simplicity, we shall just consider the case where $Y _ { 0 }$ has global normal crossings; minor modifications handle the general case.
Let $p _ { i j k } = V _ { i } \cap V _ { j } \cap V _ { k }$ denote a triple

point, and let

$$
\begin{array} { c } { { a _ { 0 } { : } \displaystyle { \prod _ { i } V _ { i } \to Y _ { 0 } } } } \\ { { a _ { 1 } { : } \displaystyle { \prod _ { i < j } C _ { i j } \to Y _ { 0 } } } } \\ { { a _ { 2 } { : } \displaystyle { \prod _ { i < j < k } { p _ { i j k } \to Y _ { 0 } } } } } \end{array}
$$

be the natural morphisms.

Lemma 2.12. $H ^ { 0 } ( Y _ { 0 } ; \mathcal { O } _ { Y _ { 0 } } ) \cong \mathbb { C } , H ^ { 1 } ( Y _ { 0 } ; \mathcal { O } _ { Y _ { 0 } } ) = H ^ { 2 } ( Y _ { 0 } ; \mathcal { O } _ { Y _ { 0 } } ) = 0 .$

Proof.
The sheaf ${ \mathcal { O } } _ { Y _ { 0 } }$ is quasi-isomorphic to the complex

$$
( a _ { 0 } ) _ { * } ( \bigoplus _ { i } \mathcal { O } _ { V _ { i } } ) \to ( a _ { 1 } ) _ { * } \left( \bigoplus _ { i < j } \mathcal { O } _ { C _ { i j } } \right) \to ( a _ { 2 } ) _ { * } \left( \bigoplus _ { i < j < k } \mathcal { O } _ { p _ { i j k } } \right) .
$$

Thus there is a spectral sequence converging to $H ^ { * } ( Y _ { 0 } ; { \mathcal { O } } _ { Y _ { 0 } } )$ whose $E _ { 1 }$ page is

<table><tr><td rowspan=1 colspan=1>H1(Vo; Ovo)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>Φi<iC</td><td rowspan=1 colspan=1>①i<i<k C</td></tr></table>

where $H ^ { 1 } ( V _ { 0 } ; \mathcal { O } _ { V _ { 0 } } ) \cong \mathbb { C }$ . The $E _ { 2 }$ page is then and the only possibly nonzero differential is $d _ { 2 } ^ { 0 , 1 } \colon \mathbb { C } \to \mathbb { C }$ . Then we have $H ^ { 1 } ( Y _ { 0 } ; { \mathcal { O } } _ { Y _ { 0 } } ) \cong \operatorname { K e r } d _ { 2 } ^ { 0 , 1 }$ and $H ^ { 2 } ( Y _ { 0 } ; { \mathcal O } _ { Y _ { 0 } } ) \cong \operatorname { C o k e r } d _ { 2 } ^ { \mathrm { 0 , 1 } }$ . By Serre duality, $H ^ { 2 } ( Y _ { 0 } ; { \mathcal { O } } _ { Y _ { 0 } } )$ is dual to $H ^ { 0 } ( Y _ { 0 } ; \omega _ { Y _ { 0 } } ) = H ^ { 0 } ( Y _ { 0 } ; \mathcal { O } _ { Y _ { 0 } } ( - D ) ) = 0$ . Thus $H ^ { 2 } ( Y _ { 0 } ; { \mathcal { O } } _ { Y _ { 0 } } ) = 0$ , so that $d _ { 2 } ^ { 0 , 1 }$ is an isomorphism and hence $H ^ { 1 } ( Y _ { 0 } ; { \mathcal { O } } _ { Y _ { 0 } } ) =$ $0$ as well.
q.e.d.

<table><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>C</td></tr></table>

Corollary 2.13. Pic $Y _ { 0 } \cong H ^ { : 2 } ( Y _ { 0 } ; \mathbb { Z } ) \cong H ^ { : 2 } ( \mathcal { V } ; \mathbb { Z } ) \cong \operatorname { P i c } \mathcal { V } .$

Proof.
The first isomorphism is immediate from the exponential sheaf sequence and Lemma 2.12, and the second is clear because $\mathcal { V }$ deformationretracts onto $Y _ { 0 }$ . To prove the final statement, it suffices to note that ${ \cal H } ^ { 1 } ( { \mathcal V } ; { \mathcal O } _ { \mathcal { Y } } ) = { \cal H } ^ { 2 } ( { \mathcal V } ; { \mathcal O } _ { \mathcal { Y } } ) = 0$ via the Leray spectral sequence.
q.e.d.

Lemma 2.14. $H ^ { 0 } ( Y _ { 0 } ; \mathbb { C } ) \cong \mathbb { C }$ , $H ^ { 1 } ( Y _ { 0 } ; \mathbb { C } ) = 0$ , and $H ^ { 4 } ( Y _ { 0 } ; \mathbb { C } ) \cong \mathbb { C } ^ { f }$ . If $d \colon \bigoplus _ { i } H ^ { 2 } ( V _ { i } ; \mathbb { C } ) \to \bigoplus _ { i < j } H ^ { 2 } ( C _ { i j } ; \mathbb { C } )$ is the natural map, then

$$
\begin{array} { l l } { { } } & { { H ^ { 2 } ( Y _ { 0 } ; \mathbb { C } ) \cong \operatorname { K e r } d } } \\ { { } } & { { } } \\ { { } } & { { H ^ { 3 } ( Y _ { 0 } ; \mathbb { C } ) \cong \operatorname { C o k e r } d \oplus \mathbb { C } . } } \end{array}
$$

Proof.
The Mayer-Vietoris spectral sequence for $H ^ { * } ( Y _ { 0 } ; \mathbb { C } )$ has $E _ { 1 }$ page

<table><tr><td rowspan=1 colspan=1>cf</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1> H²(Vi; C)</td><td rowspan=1 colspan=1>Oi&lt;j H²(Cij;C)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Cf</td><td rowspan=1 colspan=1>Ce</td><td rowspan=1 colspan=1>Cu</td></tr></table>

The $E _ { 2 }$ page is

<table><tr><td rowspan=1 colspan=1>Cf</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ker d</td><td rowspan=1 colspan=1>Coker d</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>C</td></tr></table>

It suffices to prove that $d _ { 2 } ^ { 0 , 1 }$ is an isomorphism.
However, $H ^ { 1 } ( V _ { 0 } ; \mathbb { C } ) \cong$ $H ^ { 1 } ( V _ { 0 } ; { \mathcal { O } } _ { V _ { 0 } } )$ , $H ^ { 0 } ( p _ { i j k } ; \mathbb { C } ) \cong H ^ { 0 } ( p _ { i j k } ; \mathcal { O } _ { p _ { i j k } } )$ , $H ^ { 0 } ( C _ { i j } ; \mathbb { C } ) \cong H ^ { 0 } ( C _ { i j } ; { \mathcal { O } } _ { C _ { i j } } )$ , so the fact that $d _ { 2 } ^ { 0 , 1 }$ is an isomorphism for this spectral sequence follows from the corresponding fact for the spectral sequence for ${ \mathcal { O } } _ { Y _ { 0 } }$ appearing in Lemma 2.12.

q.e.d.

Remark 2.15. For the Mayer-Vietoris spectral sequence, $E _ { 3 } = E _ { \infty }$ . We will see later that Coker $d = 0$ .

Lemma 2.16. $\operatorname { P i c } Y _ { 0 } = H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } )$ is torsion free and

$$
\mathrm { P i c } Y _ { 0 } \cong \mathrm { K e r } \left( \bigoplus _ { i } H ^ { 2 } ( V _ { i } ; \mathbb { Z } ) \to \bigoplus _ { i < j } H ^ { 2 } ( C _ { i j } ; \mathbb { Z } ) \right) .
$$

Proof.
By Corollary 2.13, $\operatorname { P i c } Y _ { 0 } ~ \cong ~ H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } )$ . The arguments of Lemma 2.14, but with $\mathbb { Z }$ -coefficients, then give an exact sequence

$$
\begin{array} { r l r } {  { 0 \to \mathrm { C o k e r } d _ { 2 } ^ { 0 , 1 } \to H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } ) \to } } \\ & { } & { \mathrm { K e r } ( \bigoplus _ { i } H ^ { 2 } ( V _ { i } ; \mathbb { Z } ) \to \bigoplus _ { i < j } H ^ { 2 } ( C _ { i j } ; \mathbb { Z } ) ) \to 0 , } \end{array}
$$

where now $d _ { 2 } ^ { 0 , 1 }$ refers to the differential in the corresponding spectral sequence with $\mathbb { Z }$ -coefficients.
By Lemma 2.14, $\mathrm { C o k e r } d _ { 2 } ^ { 0 , 1 }$ is torsion.
It suffices to prove that $H _ { 1 } ( Y _ { 0 } ; \mathbb { Z } )$ is torsion free, and in fact we will show directly that $H _ { 1 } ( Y _ { 0 } ; \mathbb { Z } ) = 0$ . Examining the Mayer-Vietoris homology spectral sequence computing $H _ { n } ( Y _ { 0 } ; \mathbb { Z } )$ , we must show that the differential $d _ { 2 , 0 } ^ { 2 } \colon E _ { 2 , 0 } ^ { 2 } = H _ { 2 } ( | \Gamma ( Y _ { 0 } ) | ; \mathbb { Z } ) \cong \mathbb { Z } \to E _ { 0 , 1 } ^ { 2 } = \bigoplus _ { i } H _ { 1 } ( V _ { i } ; \mathbb { Z } ) = H _ { 1 } ( V _ { 0 } ; \mathbb { Z } )$ is an isomorphism, where $| \Gamma ( Y _ { 0 } ) |$ is the topological realization of the dual complex of $Y _ { 0 }$ . It is straightforward to check that, in this special case, if $1$ is a generator of $H _ { 2 } ( | \Gamma ( Y _ { 0 } ) | ; \mathbb { Z } )$ , then $d _ { 2 , 0 } ^ { 2 } ( 1 )$ is represented by the 1-cycle in $V _ { 0 }$ formed by connecting the double points in the cycle $\textstyle \bigcup _ { i = 1 } ^ { r ^ { \prime } } C _ { 0 i } = D ^ { \prime }$ by (real) curves in the components.
By [18, (4.10)], inclusion induces isomorphisms $\pi _ { 1 } ( D ^ { \prime } , * ) \cong \pi _ { 1 } ( V _ { 0 } , * ) \cong \pi _ { 1 } ( D , * )$ and thus

$H _ { 1 } ( D ^ { \prime } , \mathbb { Z } ) \cong H _ { 1 } ( V _ { 0 } , \mathbb { Z } )$ . Hence $d _ { 2 , 0 } ^ { 2 } ( 1 )$ is a generator of $H _ { 1 } ( V _ { 0 } ; \mathbb { Z } )$ , so that $d _ { 2 , 0 } ^ { 2 }$ is surjective and $H _ { 1 } ( Y _ { 0 } ; \mathbb { Z } ) = 0$ . q.e.d.

Let $\Omega _ { Y _ { 0 } } ^ { * } / \tau _ { Y _ { 0 } } ^ { * }$ be the quotient of the complex $\Omega _ { Y _ { 0 } } ^ { * }$ by the subcomplex of torsion differentials (i.e. those sections supported on $( Y _ { 0 } ) _ { \mathrm { s i n g } }$ ). Here $\Omega _ { Y _ { 0 } } ^ { * } = \Lambda ^ { * } \Omega _ { Y _ { 0 } } ^ { 1 }$ , where $\Omega _ { Y _ { 0 } } ^ { 1 }$ is the sheaf of K¨ahler differentials on $Y _ { 0 }$ . By [6, (1.5)], we have the following:

Lemma 2.17. (i) There is an exact sequence

$$
0  \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 }  ( a _ { 0 } ) _ { * } ( \bigoplus _ { i } \Omega _ { V _ { i } } ^ { 1 } )  ( a _ { 1 } ) _ { * } ( \bigoplus _ { i < j } \Omega _ { C _ { i j } } ^ { 1 } )  0 .
$$

(ii) $\Omega _ { Y _ { 0 } } ^ { 2 } / \tau _ { Y _ { 0 } } ^ { 2 } \cong ( a _ { 0 } ) _ { * } \left( \bigoplus _ { i } \Omega _ { V _ { i } } ^ { 2 } \right)$

q.e.d.

Corollary 2.18. (i) With notation as in Lemma 2.14, $H ^ { 0 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) =$ $0$ , $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) \cong \mathrm { K e r } d$ , and $H ^ { 2 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) \cong \mathrm { C o k e r } d$ .

(ii) $H ^ { 0 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 2 } / \tau _ { Y _ { 0 } } ^ { 2 } ) = 0$ , $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 2 } / \tau _ { Y _ { 0 } } ^ { 2 } ) \cong H ^ { 1 } ( V _ { 0 } ; \Omega _ { V _ { 0 } } ^ { 2 } ) \cong \mathbb { C }$ , and

$$
H ^ { 2 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 2 } / \tau _ { Y _ { 0 } } ^ { 2 } ) \cong \bigoplus _ { i } H ^ { 2 } ( V _ { i } ; \Omega _ { V _ { i } } ^ { 2 } ) \cong \bigoplus _ { i } H ^ { 4 } ( V _ { i } ; \mathbb { C } ) = \mathbb { C } ^ { f } .
$$

By [6, (1.5)], there is a spectral sequence with $E _ { 1 }$ term $H ^ { q } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { p } / \tau _ { Y _ { 0 } } ^ { p } )$ converging to $H ^ { p + q } ( Y _ { 0 } ; \mathbb { C } )$ .

Lemma 2.19. The above spectral sequence degenerates at $E _ { 1 }$ .

Proof.
The $E _ { 1 }$ page looks like

<table><tr><td>cf</td><td></td><td></td></tr><tr><td>C</td><td></td><td></td></tr><tr><td>Ker d</td><td>Coker d</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>C</td><td></td><td></td></tr></table>

Comparing this with Lemma 2.14, we see that no differentials in the spectral sequence can ever be nonzero.
q.e.d.

A similar discussion handles the case of the complex $\Omega _ { Y _ { 0 } } ^ { * } ( \log D ) / \tau _ { Y _ { 0 } } ^ { * }$ We record for future reference the only cases we shall need:

Lemma 2.20. $H ^ { 0 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) = 0$ and $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) \cong$ $H ^ { 2 } ( Y _ { 0 } ; \mathbb { C } ) / \oplus _ { i } \mathbb { C } [ D _ { i } ]$ . Moreover $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) \cong H ^ { 2 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) .$

Proof.
From the exact sequence

$$
0 \to \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } \to \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } \to \oplus _ { i } \mathcal { O } _ { D _ { i } } \to 0 ,
$$

we get an exact sequence

$$
\begin{array} { r l } & { H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) = 0 \to H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) \to \bigoplus _ { i } H ^ { 0 } ( \mathcal { O } _ { D _ { i } } ) } \\ & { \quad \to H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) = \mathrm { K e r } d \to H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) \to 0 . } \end{array}
$$

As the map $\displaystyle \oplus _ { i } H ^ { 0 } ( { \mathcal { O } } _ { D _ { i } } ) \to \operatorname { K e r } d \subseteq \oplus _ { j } H ^ { 2 } ( V _ { j } ; \mathbb { C } )$ is injective,

$$
H ^ { 0 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) = 0
$$

and $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) \cong H ^ { 2 } ( Y _ { 0 } ; \mathbb { C } ) / \oplus _ { i } \mathbb { C } [ D _ { i } ]$ . The last statement follows since $H ^ { 1 } ( D _ { i } ; { \mathcal { O } } _ { D _ { i } } ) = H ^ { 2 } ( D _ { i } ; { \mathcal { O } } _ { D _ { i } } ) = 0$ . q.e.d.

We turn next to limiting cohomology.
We have the relative log complex $\Lambda _ { y / \Delta } ^ { * } = \Omega _ { y / \Delta } ^ { * } ( \log Y _ { 0 } )$ , and we denote the restriction of the relative log complex to $Y _ { 0 }$ by $\Lambda _ { Y _ { 0 } } ^ { * }$ . Note that, for $t \neq 0$ , the restriction to the fiber $Y _ { t }$ is just $\Omega _ { Y _ { t } } ^ { * }$ . The complex $\Lambda _ { \mathcal { V } / \Delta } ^ { * } ( \log \mathcal { D } ) = \Omega _ { \mathcal { V } / \Delta } ^ { * } ( \log ( Y _ { 0 } + \mathcal { D } ) )$ is defined in the obvious way.
Its restriction to $Y _ { t }$ for $t \neq 0$ is $\Omega _ { Y _ { t } } ^ { * } ( \log D )$ and its restriction to $Y _ { 0 }$ will be denoted by $\Lambda _ { Y _ { 0 } } ^ { * } ( \log D )$ . By [35] (see [31, Theorem 11.16]), the hypercohomology $\mathbb { H } ^ { * } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { * } )$ may be identified with the cohomology of the canonical fiber $Y _ { \infty } = \mathcal { V } \times _ { \Delta ^ { * } } \widetilde { \Delta ^ { * } }$ , where $\Delta ^ { * }$ is the punctured unit disk and $\widetilde { \Delta ^ { * } }$ is its universal cover.
It follows that the sheaves $\mathbb { R } ^ { q } \pi _ { * } \Lambda _ { y / \Delta } ^ { * }$ are locally free.
Minor modifications of the above arguments show that $\mathbb { H } ^ { * } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { * } ( \log D ) )$ may be identified with the cohomology of $Y _ { \infty } - D _ { \infty } = ( y - \mathcal { D } ) \times _ { \Delta ^ { * } } \widetilde { \Delta ^ { * } }$ and hence that the sheaves $\mathbb { R } ^ { q } \pi _ { * } \Lambda _ { y / \Delta } ^ { * } ( \log \mathcal { D } )$ are locally free.

We compute the cohomology of the sheaves $\Lambda _ { Y _ { 0 } } ^ { * }$ and $\Lambda _ { Y _ { 0 } } ^ { * } ( \log D )$ as follows.

Lemma 2.21. $H ^ { q } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { p } )$ and $H ^ { q } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { p } ( \log D ) )$ are zero except in the following cases:

(i) $p = 0$ , hence $\Lambda _ { Y _ { 0 } } ^ { 0 } = \Lambda _ { Y _ { 0 } } ^ { 0 } ( \log D ) = \mathcal { O } _ { Y _ { 0 } }$ , and $q = 0$ .\
(ii) $p = q = 1$ .\
(iii) $p = 2$ . In this case $\Lambda _ { Y _ { 0 } } ^ { 2 } = \omega _ { Y _ { 0 } } = \mathcal { O } _ { Y _ { 0 } } ( - D )$ and $\Lambda _ { Y _ { 0 } } ^ { 2 } ( \log D ) = \mathcal { O } _ { Y _ { 0 } }$ . Hence $H ^ { 2 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 2 } ) \cong H ^ { 0 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 2 } ( \log D ) ) \cong \mathbb { C }$ and $H ^ { q } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 2 } )$ and $H ^ { q } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 2 } ( \log D ) )$ are zero in all other cases.

Proof.
The cases $p = 0$ , $p = 2$ , and hence (i) and (iii), follow easily from Lemma 2.12.

To deal with the case $p = 1$ , let us first show that $H ^ { 0 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ) = 0$ (which is in fact already proved in [10, Lemma (2.7)]). Let $K$ be the kernel of the natural morphism

$$
( a _ { 1 } ) _ { * } \left( \bigoplus _ { i < j } \mathcal { O } _ { C _ { i j } } \right) \to ( a _ { 2 } ) _ { * } \left( \bigoplus _ { i < j < k } \mathcal { O } _ { p _ { i j k } } \right) .
$$

By [31, p. 268] or [6, Proposition (3.5)], there is an exact sequence

$$
0 \to \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } \to \Lambda _ { Y _ { 0 } } ^ { 1 } \to K \to 0 .
$$

Moreover $H ^ { 0 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) = 0$ by Corollary 2.18. The argument on p. 108 of [6] then shows that $H ^ { 0 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ) ~ = ~ 0$ . By Serre duality, $H ^ { 2 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ) = 0$ as well.
This handles the case of $\Lambda _ { Y _ { 0 } } ^ { 1 }$ .

Finally, we deal with $\Lambda _ { Y _ { 0 } } ^ { 1 } ( \log D )$ . First note that we have the usual Poincar´e residue sequence

$$
0 \to \Lambda _ { Y _ { 0 } } ^ { 1 } \to \Lambda _ { Y _ { 0 } } ^ { 1 } ( \log D ) \to \bigoplus _ { i } { \mathcal { O } } _ { D _ { i } } \to 0 .
$$

It follows that $H ^ { 2 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ( \log D ) ) \cong H ^ { 2 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ) = 0$ . Moreover, since $H ^ { 0 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ) = 0$ , it suffices to prove that the coboundary map

$$
\delta \colon \oplus _ { i } H ^ { 0 } ( { \mathcal { O } } _ { D _ { i } } ) \to H ^ { 1 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } )
$$

is injective.

As before, let $K = \operatorname { K e r } ( a _ { 1 } ) _ { * } \left( \bigoplus _ { i < j } \mathcal { O } _ { C _ { i j } } \right) \to ( a _ { 2 } ) _ { * } \left( \bigoplus _ { i < j < k } \mathcal { O } _ { p _ { i j k } } \right)$ . It follows easily that $H ^ { 0 } ( Y _ { 0 } ; K ) \cong \mathbb { C } ^ { f - 1 }$ and that $H ^ { 1 } ( Y _ { 0 } ; K ) \cong \mathbb { C }$ . Then there is a commutative diagram whose top row is exact

$$
\begin{array} { c c c c c c c c c c c c c c c c c c c c c c } { H ^ { 0 } ( Y ; K ) } & { \longrightarrow } & { H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) } & { \longrightarrow } & { H ^ { 1 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ) } & & & & & & \\ { \Big \Vert } & & & & { \Big \downarrow } & & & & & & & \\ { \mathbb { C } ^ { f - 1 } } & { \longrightarrow } & { \bigoplus _ { i } H ^ { 1 } ( V _ { i } ; \Omega _ { V _ { i } } ^ { 1 } ) } & & & & & & & & \\ & & & & & { \Big \downarrow } & & & & & & \\ & & & & & { \bigoplus _ { i < j } H ^ { 1 } ( C _ { i j } ; \Omega _ { C _ { i j } } ^ { 1 } ) } & & & & & & & & & \end{array}
$$

The classes $[ D _ { i } ]$ are linearly independent in $H ^ { 0 } ( V _ { 0 } ; \Omega _ { V _ { 0 } } ^ { 1 } )$ and map to $0$ in $\begin{array} { r l } {  { \bigoplus _ { i < j } H ^ { 1 } ( C _ { i j } ; \Omega _ { C _ { i j } } ^ { 1 } ) } \quad } & { { } } \end{array}$ , since the $D _ { i }$ are disjoint from the double curves $C _ { i j }$ . Moreover, the image of $H ^ { 0 } ( Y _ { 0 } ; K ) \cong \mathbb { C } ^ { f - 1 }$ in $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } )$ consists of the $\mathbb { C }$ -span of the Chern classes of the $f$ line bundles $\mathcal { O } _ { \mathcal { Y } } ( V _ { i } ) \big | _ { Y _ { 0 } }$ , subject to the relation

$$
 ( \mathcal { O } _ { \mathcal { V } } ( V _ { 0 } ) | _ { Y _ { 0 } } ) \otimes \cdots \otimes ( \mathcal { O } _ { \mathcal { V } } ( V _ { f - 1 } ) | _ { Y _ { 0 } } ) = \mathcal { O } _ { \mathcal { V } } ( Y _ { 0 } ) \big | _ { Y _ { 0 } } = \mathcal { O } _ { Y _ { 0 } } .
$$

In particular, the image of $\mathcal { O } y ( V _ { i } ) \big | _ { Y _ { 0 } }$ in $H ^ { 1 } ( V _ { j } ; \Omega _ { V _ { j } } ^ { 1 } )$ is $\left[ C _ { i j } \right]$ if $i \neq j$ and $- [ C _ { i } ]$ if $i = j$ . Then by the same argument as before, the classes $[ D _ { i } ]$ are linearly independent in $H ^ { 0 } ( V _ { 0 } ; \Omega _ { V _ { 0 } } ^ { 1 } )$ modulo the image of $H ^ { 0 } ( Y ; K )$ . It follows that their images in $H ^ { 1 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } )$ are linearly independent.
Thus, $\delta$ is injective.
q.e.d.

We then have:

Corollary 2.22. (i) The spectral sequence with $E _ { 1 }$ term $H ^ { q } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { p } )$ converging to $\mathbb { H } ^ { p + q } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { * } )$ degenerates at $E _ { 1 }$ .

(ii) The spectral sequence with $E _ { 1 }$ term $H ^ { q } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { p } ( \log D ) )$ and converging to $\mathbb { H } ^ { p + q } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { * } ( \log D ) )$ degenerates at $E _ { 1 }$ .

(iii) The sheaves $R ^ { q } \pi _ { * } \Lambda _ { y / \Delta } ^ { p }$ and $R ^ { p } \pi _ { * } \Lambda _ { y / \Delta } ^ { p } ( \log \mathcal { D } )$ are locally free, and are the successive quotients of $a$ filtration of $\mathbb { R } ^ { q } \pi _ { * } \Lambda _ { y / \Delta } ^ { * } ( \log \mathcal { D } )$ by holomorphic subbundles.

Proof.
To see (i) and (ii), a glance at the $E _ { 1 }$ pages of the spectral sequences shows that there are no nonzero differentials for any $E _ { r }$ , $r \geq 1$ . The argument that (i) and $( \mathrm { i i } ) \implies$ (iii) is standard, given that the sheaves $\mathbb { R } ^ { q } \pi _ { * } \Lambda _ { y / \Delta } ^ { * } ( \log \mathcal { D } )$ are locally free (see for example the proof of [31, Corollary 11.24]). q.e.d.

Corollary 2.23. Let $d$ be as in Lemma 2.14. The following are equivalent:

(i) $\mathrm { C o k e r } d = 0$ .\
(ii) $H ^ { 2 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) = 0$ .\
(ii)0 $H ^ { 2 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ( \log D ) ) = 0$ .\
(iii) The image of the specialization map $\operatorname { s p } _ { \mathbb { C } } \colon H ^ { 2 } ( Y _ { 0 } ; \mathbb { C } ) \to H ^ { 2 } ( Y _ { t } ; \mathbb { C } )$ has codimension one.\
(iii)0 The image of the specialization map $\operatorname { s p } _ { \mathbb { C } } \colon H ^ { 2 } ( Y _ { 0 } - D _ { 0 } ; \mathbb { C } )  H ^ { 2 } ( Y _ { t } -$ $D _ { t } ; \mathbb { C } )$ has codimension one.\
(iv) The specialization map $\operatorname { s p } _ { \mathbb { C } } \colon H ^ { \cdot 2 } ( Y _ { 0 } ; \mathbb { C } ) \to H ^ { \cdot 2 } ( Y _ { t } ; \mathbb { C } )$ is not surjective.\
(iv)0 The specialization map $\operatorname { s p } _ { \mathbb { C } } \colon H ^ { 2 } ( Y _ { 0 } - D _ { 0 } ; \mathbb { C } ) \to H ^ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { C } )$ is not surjective.

Proof.
(i) $\Longleftrightarrow$ (ii) follows from Corollary 2.18. The equivalence (i) $\iff \iff ( \mathrm { i i } ) ^ { \prime }$ follows from the last statement of Lemma 2.20. Next, we have an exact sequence defined in the proof of Lemma 2.21:

$H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } )  H ^ { 1 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } )  H ^ { 1 } ( Y _ { 0 } ; K )  H ^ { 2 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } )  0 ,$ using the fact that $H ^ { 1 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ) = 0$ . Moreover $\dim { H } ^ { 1 } ( Y _ { 0 } ; K ) \ : = \ : 1$ , again by the proof of Lemma 2.21. Thus $H ^ { 2 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) = 0 \iff$ the homomorphism $H ^ { 1 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } )  H ^ { 1 } ( Y _ { 0 } ; K )$ is surjective $\Longleftrightarrow$ the image of the homomorphism $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } )  H ^ { 1 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } )$ has codimension one $\Longleftrightarrow$ the homomorphism $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } )  H ^ { 1 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } )$ is not surjective.
Finally, $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) \cong H ^ { 2 } ( Y _ { 0 } ; \mathbb { C } )$ and $H ^ { 1 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ) \cong$ $H ^ { 2 } ( Y _ { t } ; \mathbb { C } )$ , and we can identify the homomorphism $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) $ $H ^ { 1 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } )$ with the specialization map (compare [31, §11.3]). This proves the equivalence of (ii) with (iii) and (iv), and the equivalence of (ii) $'$ with (iii)0 and $( \mathrm { i v } ) ^ { \prime }$ is similar.
q.e.d.

2.4. Smoothings of Type III pairs.
Let $( Y _ { 0 } , D )$ be a $d$ -semistable Type III anticanonical pair.
For simplicity, we shall just consider the case $r ( D ) > 1$ in what follows, i.e. all components $D _ { i }$ of $D$ are smooth.
The case where $D$ is irreducible is handled by minor modifications of the arguments.
Let $D _ { i } ^ { 2 } = - d _ { i }$ . The tangent space for the deformation functor of $Y _ { 0 }$ , keeping the divisor $D$ with normal crossings, is given by

$$
\mathbb { T } _ { Y _ { 0 } } ^ { 1 } ( - \log D ) = \mathrm { E x t } ^ { 1 } ( \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) , \mathcal { O } _ { Y _ { 0 } } ) ,
$$

and there is the usual local to global exact sequence

$$
\begin{array} { r l r } & { } & { 0 \to H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) ) \to \mathbb { T } _ { Y _ { 0 } } ^ { 1 } ( - \log D ) \to H ^ { 0 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } ) } \\ & { } & { \to H ^ { 2 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) ) \to \mathbb { T } _ { Y _ { 0 } } ^ { 2 } ( - \log D ) \to H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } ) . } \end{array}
$$

The term $H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) )$ is the tangent space to the functor of locally trivial deformations.
By $d$ -semistability, $T _ { Y _ { 0 } } ^ { 1 } ~ \cong ~ \mathcal { O } _ { ( Y _ { 0 } ) _ { \mathrm { s i n g } } }$ . The functor of locally trivial deformations is unobstructed, the map $\mathbb { T } _ { Y _ { 0 } } ^ { 1 } ( - \log D )  H ^ { 0 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } )$ is surjective, and the map $\mathbb { T } _ { Y _ { 0 } } ^ { 2 } ( - \log D ) $ $H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } )$ is an isomorphism because of the following:

Lemma 2.24. $H ^ { 2 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) ) = 0$ .

Proof.
By [6, (2.10)], $H ^ { 2 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) )$ is Serre dual to

$$
H ^ { 0 } ( Y _ { 0 } ; ( \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) \otimes \omega _ { Y _ { 0 } } ) = H ^ { 0 } ( Y _ { 0 } ; ( \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) ( - D ) ) .
$$

But $H ^ { 0 } ( Y _ { 0 } ; ( \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) ( - D ) ) \subseteq H ^ { 0 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } )$ , and

$$
H ^ { 0 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) = 0
$$

by Lemma 2.20.

q.e.d.

Note that the long exact Ext sequence associated to the exact sequence

$$
0 \to \Omega _ { Y _ { 0 } } ^ { 1 } \to \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) \to \bigoplus _ { i } { \mathcal { O } } _ { D _ { i } } \to 0
$$

gives the usual sequence

$$
\begin{array} { r l } & { 0 = \bigoplus _ { i } H ^ { 0 } ( D _ { i } ; N _ { D _ { i } / Y _ { 0 } } ) \to \mathbb { T } _ { Y _ { 0 } } ^ { 1 } ( - \log D ) \to \mathbb { T } _ { Y _ { 0 } } ^ { 1 } \to } \\ & { \to \bigoplus _ { i } H ^ { 1 } ( D _ { i } ; N _ { D _ { i } / Y _ { 0 } } ) \to \mathbb { T } _ { Y _ { 0 } } ^ { 2 } ( - \log D ) \to \mathbb { T } _ { Y _ { 0 } } ^ { 2 } \to 0 . } \end{array}
$$

Moreover $\mathbb { T } _ { Y _ { 0 } } ^ { 2 } ( - \log D ) \to \mathbb { T } _ { Y _ { 0 } } ^ { 2 }$ is an isomorphism, as both are identified with $H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } )$ .

Fixing a nowhere zero section $\xi$ of $H ^ { 0 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } )$ , Lie bracket defines a surjective homomorphism $T _ { Y _ { 0 } } ( - \log D ) \to T _ { Y _ { 0 } } ^ { \perp }$ whose kernel we denote by $S _ { Y _ { 0 } } ( - \log D )$ . By the proof of [6, (4.4)], the dual $( S _ { Y _ { 0 } } ( - \log D ) ) ^ { \vee }$ is isomorphic to $\Lambda _ { Y _ { 0 } } ^ { 1 } ( \log D )$ , which can be defined independently of the existence of a smoothing of $Y _ { 0 }$ or of the pair $( Y _ { 0 } , D )$ .

Lemma 2.25. (i) In the above notation, $H ^ { 2 } ( Y _ { 0 } ; S _ { Y _ { 0 } } ( - \log D ) ) = 0$ . (ii) There is an exact sequence

$$
\begin{array} { r l } & { H ^ { 0 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } ) \cong \mathbb { C }  H ^ { 1 } ( Y _ { 0 } ; S _ { Y _ { 0 } } ( - \log D ) )  H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) ) } \\ & { \qquad H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } ) \cong H ^ { 1 } ( ( Y _ { 0 } ) _ { \mathrm { s i n g } } ; O _ { ( Y _ { 0 } ) _ { \mathrm { s i n g } } } )  0 . } \end{array}
$$

(iii) The image of $H ^ { 1 } ( Y _ { 0 } ; S _ { Y _ { 0 } } ( - \log D ) )$ in $H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) )$ is the tangent space to the locally trivial deformations of $( Y _ { 0 } , D )$ which are $d$ -semistable.

(iv) The image of $H ^ { 1 } ( Y _ { 0 } ; S _ { Y _ { 0 } } ( - \log D ) )$ in $H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) )$ has codimension $f - 1$ .

(v) There is an exact sequence

$0 \to H ^ { 1 } ( Y _ { 0 } ; S _ { Y _ { 0 } } ( - \log D ) ) \to H ^ { 1 } ( Y _ { 0 } ; S _ { Y _ { 0 } } ) \to \bigoplus _ { i } H ^ { 1 } ( D _ { i } ; N _ { D _ { i } / Y _ { 0 } } ) \to 0 ,$ and hence the image of $H ^ { 1 } ( Y _ { 0 } ; S _ { Y _ { 0 } } ( - \log D ) )$ in $H ^ { 1 } ( Y _ { 0 } ; S _ { Y _ { 0 } } )$ has codimension $\textstyle \sum _ { i } ( d _ { i } - 1 )$ .

Proof.
(i) By Serre duality, we have

$$
H ^ { 2 } ( Y _ { 0 } ; S _ { Y _ { 0 } } ( - \log D ) ) ^ { \vee } \cong H ^ { 0 } ( Y _ { 0 } ; ( S _ { Y _ { 0 } } ( - \log D ) ) ^ { \vee } \otimes \mathcal { O } _ { Y _ { 0 } } ( - D ) ) .
$$

Furthermore,

$$
\begin{array} { r l r } {  { H ^ { 0 } ( Y _ { 0 } ; ( S _ { Y _ { 0 } } ( - \log D ) ) ^ { \vee } \otimes \mathcal { O } _ { Y _ { 0 } } ( - D ) ) \cong H ^ { 0 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ( \log D ) \otimes \mathcal { O } _ { Y _ { 0 } } ( - D ) ) } } \\ & { } & { \subseteq H ^ { 0 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ( \log D ) ) . } \end{array}
$$

By Lemma 2.21, $H ^ { 0 } ( Y _ { 0 } ; \Lambda _ { Y _ { 0 } } ^ { 1 } ( \log D ) ) = 0$ , hence $H ^ { 2 } ( Y _ { 0 } ; S _ { Y _ { 0 } } ( - \log D ) ) =$ $0$ as well.
The exact sequence in (ii) is then the long exact cohomology sequence associated to

$$
0 \to S _ { Y _ { 0 } } ( - \log D ) \to T _ { Y _ { 0 } } ( - \log D ) \to T _ { Y _ { 0 } } ^ { 1 } \to 0 .
$$

(iii) This follows from [6, (4.5)].

(iv) The codimension in question is

$$
h ^ { 1 } ( Y _ { 0 } , T _ { Y _ { 0 } } ^ { 1 } ) = h ^ { 1 } ( \mathcal { O } _ { ( Y _ { 0 } ) _ { \mathrm { s i n g } } } ) = \dim \operatorname { P i c } ( Y _ { 0 } ) _ { \mathrm { s i n g } } .
$$

The proof that $h ^ { 1 } ( \mathcal { O } _ { ( Y _ { 0 } ) _ { \mathrm { s i n g } } } ) = f - 1$ follows easily from the identities $2 e = 3 v$ and $v - e + f = 2$ [11, p. 25].

(v) The exact sequence in the first statement of (v) follows by taking the cohomology long exact sequence associated to

$$
0  S _ { Y _ { 0 } } ( - \log D )  S _ { Y _ { 0 } }  \bigoplus _ { i } N _ { D _ { i } / Y _ { 0 } }  0
$$

and using (i). The final statement follows since $N _ { D _ { i } / Y _ { 0 } }$ is a line bundle on $D _ { i }$ of degree $- d _ { i } < 0$ . q.e.d.

We now analyze the smoothings of the pair $( Y _ { 0 } , D )$ , following the method of [6] (although we could also use the arguments of [19]).

Theorem 2.26. Let $( Y _ { 0 } , D )$ be a $d$ -semistable Type III anticanonical pair.
Then the pair $( Y _ { 0 } , D )$ is smoothable.
More precisely, there is a unique smoothing component $( X , 0 )$ of the locally semi-universal deformation of the pair $( Y _ { 0 } , D )$ , and moreover:

(i) $X$ is smooth and the discriminant locus in $X$ is a smooth hypersurface.\
(ii) $\dim X = \dim \mathbb { T } _ { Y _ { 0 } } ^ { 1 } ( - \log D ) - f + 1 .$

(iii) Given a germ of a map of the disk $( \Delta , 0 )$ to $( X , 0 )$ , the pulled back family $( \mathcal { V } , \mathcal { D } ) \to \Delta$ is a Type III degeneration of anticanonical pairs, i.e. the total space is smooth $\Longleftrightarrow$ the map $\Delta  X$ is transverse to the discriminant locus.

Proof.
By the arguments of [6, (5.10)], there is a germ of a smoothing component $( \widehat { X } , 0 )$ of the surface $Y _ { 0 }$ . Here 0 corresponds to the surface $Y _ { 0 }$ , $\widehat { X }$ is smooth at $0$ and its tangent space at 0 is given by the exact sequence

$$
0 \to \mathbb { C } \to H ^ { 1 } ( Y _ { 0 } ; S _ { Y _ { 0 } } ) \to T _ { \widehat { X } , 0 } \to H ^ { 0 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } ) \cong \mathbb { C } \to 0 .
$$

Let ${ \widehat { \mathcal { X } } }  { \widehat { \mathcal { X } } }$ be the corresponding family.
For each component $D _ { i }$ of $D$ , consider the component $\mathcal { Z } _ { i }$ of the relative Hilbert-Douady scheme of curves in $\widehat { \mathcal X }$ containing $D _ { i }$ . We have the following exact sequence for the normal bundle of $D _ { i }$ in $\hat { \mathcal X }$ :

$$
0 \to N _ { D _ { i } / Y _ { 0 } } \to N _ { D _ { i } / \widehat { \chi } } \to \mathcal { O } _ { D _ { i } } \otimes _ { \mathbb { C } } T _ { \widehat { X } , 0 } \to 0 .
$$

Hence, taking Euler characteristics, we have

$$
\chi ( Y _ { 0 } ; N _ { D _ { i } / \widehat { \chi } } ) = \chi ( Y _ { 0 } ; N _ { D _ { i } / Y _ { 0 } } ) + \dim \widehat { X } = \dim \widehat { X } - d _ { i } + 1 .
$$

The dimension of $\mathcal { Z } _ { i }$ at the point corresponding to component $D _ { i }$ is at least $\chi ( Y _ { 0 } ; N _ { D _ { i } / \widehat { \chi } } )$ . Since $D _ { i } ^ { 2 } < 0$ , the corresponding Hilbert scheme over a point $x$ of $\widehat { X }$ is either empty or smooth of dimension zero.
It follows that (as germs) $\mathcal { Z } _ { i }$ can be identified with its image $Z _ { i } \subseteq { \widehat { X } }$ , and that $Z _ { i }$ is a smooth submanifold of $\widehat { X }$ of codimension at most $d _ { i } - 1$ . Setting $X = \textstyle \bigcap _ { i } Z _ { i }$ , $X$ is a subspace of $\widehat { X }$ and every component of $X$ has codimension at most $\textstyle \sum _ { i } ( d _ { i } - 1 )$ . On the other hand, clearly the Zariski tangent space of $X$ is contained in the subspace $T ^ { \prime }$ of $T _ { \widehat { X } , 0 }$ where the normal crossings divisor $\begin{array} { r } { D = \sum _ { i } D _ { i } } \end{array}$ deforms to first order.
There is an exact sequence

$$
0 \to \mathbb { C } \to H ^ { 1 } ( Y _ { 0 } ; S _ { Y _ { 0 } } ( - \log D ) ) \to T ^ { \prime } \to H ^ { 0 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } ) \cong \mathbb { C } .
$$

Comparing the above sequence with that in the first paragraph of the proof for $T _ { \widehat { X } , 0 }$ and using Lemma 2.25, we see that the codimension of $T ^ { \prime }$ in $T _ { \widehat { X } , 0 }$ bis either $\textstyle \sum _ { i } ( d _ { i } - 1 )$ or $\textstyle \sum _ { i } ( d _ { i } - 1 ) + 1$ , and the first case arises $\Longleftrightarrow$ the map $T ^ { \prime }  H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } )$ is surjective.
By the discussion on $X$ above, we see that $X$ is smooth, $\dim X = \dim { \widehat { X } } - \sum _ { i } ( d _ { i } - 1 )$ , $T _ { X , 0 } = T ^ { \prime }$ , and the homomorphism $T _ { X , 0 }  H ^ { 0 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } )$ is surjective.
The proofs of the remaining statements of the theorem are then straightforward.
q.e.d.

# 3. Monodromy

3.1. A formula for the monodromy.
We keep the notation of the previous section: $\pi \colon ( \mathcal { V } , \mathcal { D } ) \to \Delta$ is a Type III degeneration of anticanonical pairs.
Let $( Y , D ) = ( Y _ { t } , D _ { t } )$ be a general fiber of $\pi$ . Then the monodromy diffeomorphism of the family acts on $H _ { 2 } ( Y ; \mathbb { Z } )$ , $H _ { 2 } ( Y \textrm { -- }$ $D ; \mathbb { Z } )$ , and on $\overline { { H } } _ { 2 } ( Y - D , \partial )$ . Our goal is to analyze this action, primarily on $H _ { 2 } ( Y - D ; \mathbb { Z } )$ .

We begin with a discussion of the topology of $y$ . Let $c \colon Y = Y _ { t }  Y _ { 0 }$ be the Clemens collapsing map.
For each triple point $p \in Y _ { 0 }$ , $c ^ { - 1 } ( p ) = \tau _ { p }$ is a 2-torus in $Y$ . The argument of [11, Lemma (1.9)] shows that, for every $p$ and $q$ , the 2-tori $\tau _ { p }$ and $\tau _ { q }$ are homologous in $Y - D$ (up to sign).
Denote this common homology class (well-defined up to sign) by $\tau$ . Next, let $\alpha = \alpha _ { i j } ^ { k }$ be a (real) simple closed curve in a double curve $C _ { i j }$ simply enclosing the triple point $p = p _ { i j k }$ ; we can assume that $\alpha$ is contained in a small disk around $p$ . An examination of the local form for $c$ (see for example [30, §2.2]) shows that $c ^ { - 1 } ( \alpha ) = \tau _ { p }$ is homologous to $\tau$ .

Explicitly, there exist local analytic coordinates centered in a ball of radius $s$ at $p$ such that, for $| t | \ll s$ , $\pi$ is given by $x y z = t$ . We may model the collapsing map $c$ as follows: Given $( x , y , z )$ such that $x y z = t$ , let $( a , b , c ) \in \mathbb { R } _ { \ge 0 } ^ { 3 }$ be the unique point such that $a b c = 0$ and $( a , b , c ) = ( | x | , | y | , | z | ) - ( k , k , k )$ for some $k \in \mathbb { R }$ . Then the Clemens collapse is

$$
c ( x , y , z ) = \left( { \frac { a x } { | x | } } , { \frac { b y } { | y | } } , { \frac { c z } { | z | } } \right) .
$$

Thus,

$$
\tau _ { p } = c ^ { - 1 } ( 0 , 0 , 0 ) = \{ ( x , y , z ) \colon | x | = | y | = | z | = | t | ^ { 1 / 3 } \} .
$$

Restrict $( x , y , z )$ to lie in the polydisk $| x | , | y | , | z | \leq s$ . There is a topologically trivial two-torus fibration $( x , y , z ) \mapsto ( | x | , | y | , | z | )$ whose image is a two-simplex $\sigma _ { p }$ and whose fibers are homologous to $\tau _ { p }$ . The curve $\alpha$ can be taken to be $( 0 , 0 , r e ^ { i \theta } )$ and thus there is some $r ^ { \prime } > 0$ such that

$$
c ^ { - 1 } ( \alpha ) = \{ ( x , y , z ) \colon | x | = | y | = r ^ { \prime } , | z | = | t | / ( r ^ { \prime } ) ^ { 2 } \} .
$$

Hence $c ^ { - 1 } ( \alpha )$ and $\tau _ { p }$ are homologous.

Next suppose that $\alpha _ { 0 j } \subseteq C _ { 0 j }$ is a loop around a triple point contained in $V _ { 0 }$ . Then $c ^ { - 1 } ( \alpha _ { 0 j } ) = c ^ { - 1 } ( \tilde { \alpha } _ { 0 j } )$ , where $\tilde { \alpha } _ { 0 j } \subseteq V _ { 0 }$ is the tube over $\alpha _ { 0 j }$ in $V _ { 0 } - C _ { 0 } - D$ . By the explicit description of the topology of $V _ { 0 }$ (see [18, §4]), $\tilde { \alpha } _ { 0 j }$ is equal to $\gamma$ , where $\gamma \subseteq V _ { 0 } - C _ { 0 } - D$ is the tube over a simple closed curve in $D _ { i }$ enclosing a double point as in Section 1. Identifying the 2-torus $\gamma$ in $V _ { 0 }$ with $c ^ { - 1 } ( \gamma )$ in $Y$ , we see that, in the above notation, $\tau$ and $c ^ { - 1 } ( \alpha _ { 0 j } )$ are homologous to $\gamma$ . In particular, they are homologous to $0$ in $H _ { 2 } ( Y ; \mathbb { Z } )$ , but are nontrivial in $H _ { 2 } ( Y - D ; \mathbb { Z } )$ .

Similarly, for $i$ arbitrary (possibly $0$ ), if $\alpha _ { i j }$ is a loop in a double curve $C _ { i j }$ simply enclosing the triple point $p _ { i j k }$ , then we can define the class $\tau \in H _ { 2 } ( V _ { i } - C _ { i } ; \mathbb { Z } )$ .

Theorem 3.1. With notation as in Section 1,

(i) Let $T$ be the action of monodromy on $H _ { 2 } ( Y ; \mathbb { Z } )$ , $H _ { 2 } ( Y - D ; \mathbb { Z } )$ , or $\overline { { H } } _ { 2 } ( Y - D , \partial )$ . Then $T$ is unipotent and, if $N = T - \operatorname { I d }$ , then $N ^ { 2 } = 0$ .\
(ii) For the action of $T$ on $H _ { 2 } ( Y ; \mathbb { Z } )$ , $T = \mathrm { { I d } }$ and $N = 0$ .\
(iii) There is a unique class $\lambda \in \Lambda ^ { \vee }$ such that, for all $x \in { \overline { { H } } } _ { 2 } ( Y - D ; \mathbb { Z } )$ ,

$$
N ( x ) = - ( x \bullet \lambda ) \gamma .
$$

Moreover, $\lambda ^ { 2 } = v$ , where $v$ is the number of triple points.

Proof.
Since $\pi \colon \mathcal { V }  \Delta$ is a degeneration with reduced normal crossings, general results (for example [3]) show that $T$ is unipotent on $H _ { 2 } ( Y ; \mathbb { Z } )$ . Since $T ( [ D _ { i } ] ) = [ D _ { i } ]$ , $T$ induces a unipotent automorphism of $\Lambda$ as well.
For $H _ { 2 } ( Y - D ; \mathbb { Z } )$ , $T$ preserves the filtration

$$
0 \to \mathbb { Z } \gamma \to H _ { 2 } ( Y - D ; \mathbb { Z } ) \to \Lambda \to 0 ,
$$

and is unipotent on the graded pieces (in fact it is Id on $\mathbb { Z } \gamma$ ) and hence is unipotent on $H _ { 2 } ( Y - D ; \mathbb { Z } )$ . A similar argument handles $\overline { { H } } _ { 2 } ( Y - D , \partial )$ . We will deal with the index of unipotency shortly.

We can then apply [3, Theorem 5.6] to conclude that $N ~ = ~ 0$ on $H ^ { 2 } ( Y ; \mathbb { Z } )$ . In that notation, $s = 0$ since the $\tau _ { p }$ are homologous to $0$ in $H ^ { 2 } ( Y ; \mathbb { Z } )$ , and the classes denoted by $\psi ( \gamma ^ { \prime } )$ there are all of the form $c ^ { - 1 } ( \alpha )$ for $\alpha$ a simple closed curve in a double curve $C _ { i j }$ simply enclosing a triple point $p$ , hence as we have seen they are all homologous to $0$ in our case.
Thus $N = 0$ .

It follows that the induced automorphism $T$ of $\Lambda$ is Id as well.
Thus, for the action of $T$ on $H _ { 2 } ( Y - D ; \mathbb { Z } )$ , if $N = T - \operatorname { I d }$ , then $\operatorname { I m } N \subseteq \mathbb { Z } \gamma$ and thus $N$ is necessarily of the form $N ( x ) = - ( x \bullet \lambda ) \gamma$ for a unique class $\lambda \in \Lambda ^ { \vee }$ (with the understanding that $N ( x )$ is defined for all $x \in$ $H _ { 2 } ( Y - D ; \mathbb { Z } )$ via the homomorphism $H _ { 2 } ( Y - D ; \mathbb { Z } ) \to \Lambda$ ), and hence $N ^ { 2 } = 0$ .

We finally prove that $\lambda ^ { 2 } = v$ . The idea of the proof is similar to the argument of [11, Proposition (1.10)], but is complicated by the fact that we cannot simply consider $N ^ { 2 }$ because $N ^ { 2 } = 0$ . Instead, we will use the dual action of monodromy $\hat { T }$ on $\overline { { H } } _ { 2 } ( Y - D , \partial )$ . Let $\hat { N } = \hat { T } - \mathrm { I d }$ . We have the exact sequence

$$
0 \to \Lambda ^ { \vee } \to \overline { { { H } } } _ { 2 } ( Y - D , \partial ) \to \mathbb { Z } \to 0 .
$$

Let $\hat { \gamma }$ denote an element of $\overline { { H } } _ { 2 } ( Y - D , \partial )$ which maps onto a generator of the quotient $\mathbb { Z }$ above, i.e. $( \gamma \bullet \widehat { \gamma } ) = 1$ . By duality $\hat { N } ( \Lambda ^ { \vee } ) = 0$ and $\hat { N } ( \hat { \gamma } ) \in \Lambda ^ { \vee }$ , so that $\hat { N } ^ { 2 } = 0$ .

Lemma 3.2. $\hat { N } ( \hat { \gamma } ) = \lambda$ mod $\mathbb { Z } \gamma$

Proof.
Since monodromy is a diffeomorphism, for all $x \in H _ { 2 } ( Y - D )$ and for all $y \in \overline { { H } } _ { 2 } ( Y - D , \partial )$ , we have

$$
( T x \bullet { \hat { T } } y ) = ( x \bullet y ) .
$$

Using $T = \operatorname { I d } + N$ and $\hat { T } = \mathrm { I d } + \hat { N }$ , we have

$$
( x \bullet y ) = ( T x \bullet { \hat { T } } y ) = ( ( \operatorname { I d } + N ) x \bullet ( \operatorname { I d } + { \hat { N } } ) y ) ,
$$

and thus

$$
( N x \bullet y ) + ( x \bullet \hat { N } y ) = - ( N x \bullet \hat { N } y ) = 0 ,
$$

since $N x \in \mathbb { Z } \gamma$ is orthogonal to the image of $\hat { N }$ . In particular, taking $y = \hat { \gamma }$ , we see that, for all $x \in H _ { 2 } ( Y - D )$ ,

$$
( N x \bullet \hat { \gamma } ) = - ( x \bullet \lambda ) = - ( x \bullet \hat { N } \hat { \gamma } ) ,
$$

and hence $\hat { N } ( \hat { \gamma } ) = \lambda$ mod $\mathbb { Z } \gamma$

Corollary 3.3. If $N$ denotes the map $\Lambda _ { \mathbb { Q } } \to \mathbb { Q } \gamma$ induced by $N$ , then

$$
\overline { { { N } } } \circ \hat { N } ( \hat { \gamma } ) = - ( \lambda ^ { 2 } ) \gamma .
$$

Proof.
This is clear since, by definition, $\overline { { { N } } } \circ \hat { N } ( \hat { \gamma } ) = - ( \lambda \bullet \lambda ) \gamma$ . q.e.d.

To relate this to the number $v$ of triple points, the essentially local arguments used in the proof of [3, Theorem 4.4] show:

Lemma 3.4. For all $y \in \overline { { H } } _ { 2 } ( Y - D , \partial )$ ,

$$
\overline { { { N } } } \circ \hat { N } ( y ) = - v ( \gamma \bullet y ) \gamma . q . e . d .
$$

Combining Corollary 3.3 with Lemma 3.4, we see that

$$
\overline { { { N } } } \circ \hat { N } ( \hat { \gamma } ) = - ( \lambda ^ { 2 } ) \gamma = - v ( \gamma \bullet \hat { \gamma } ) \gamma = - v \gamma ,
$$

and hence $\lambda ^ { 2 } = v$ as claimed.

q.e.d.

3.2. Further properties of $\lambda .$ . To say more about the class $\lambda$ , we describe a geometric representative $\Sigma$ for $\lambda$ . For each double curve $C _ { i j }$ , choose a simple closed curve $\ell _ { i j }$ connecting the two triple points $p _ { i j k }$ , n t $p _ { i j \ell }$ lying in ks enclosing the twoesult of truncating . Let $C _ { i j } ^ { 0 }$ be the complement in iple points on near each of $C _ { i j }$ and let e triple $C _ { i j }$ $\ell _ { i j } ^ { 0 } = \ell _ { i j } \cap C _ { i j } ^ { 0 }$ of two small $\ell _ { i j }$ $T _ { i j } = c ^ { - 1 } ( \ell _ { i j } ^ { \mathsf { U } } ) = \ell _ { i j } ^ { \mathsf { U } } \times f _ { i j }$ is a cylinder, where $f _ { i j }$ is the fiber of the Clemens collapsing map over $C _ { i j } ^ { 0 }$ . Near the triple point $p _ { i j k }$ we have the local model $x y z = t$ and a torus fibration $( x , y , z ) \to ( | x | , | y | , | z | )$ . As above, we choose an appropriate neighborhood of $p _ { i j k }$ so that the image of this torus fibration is a 2-simplex $\sigma _ { p }$ . The sum $[ f _ { i j } ] + [ f _ { j k } ] + [ f _ { k i } ] = 0$ is zero in the homology of $\sigma _ { p } \times \tau _ { p }$ —for instance,

$$
\begin{array} { r l } & { f _ { i j } = c ^ { - 1 } ( \epsilon , 0 , 0 ) = \lbrace ( x , y , z ) : x = \epsilon ^ { \prime } , | y | = | z | \rbrace } \\ & { f _ { k i } = c ^ { - 1 } ( 0 , \epsilon , 0 ) = \lbrace ( x , y , z ) : y = \epsilon ^ { \prime } , | x | = | z | \rbrace } \\ & { f _ { j k } = c ^ { - 1 } ( 0 , 0 , \epsilon ) = \lbrace ( x , y , z ) : z = \epsilon ^ { \prime } , | x | = | y | \rbrace } \end{array}
$$

are three representatives which sum to zero in $H _ { 1 } ( \sigma _ { p } \times \tau _ { p } ; \mathbb { Z } )$ . Thus, there is a pair of pants $S _ { i j k }$ whose boundary is $\pm ( f _ { i j } + f _ { j k } + f _ { k i } )$ , depending on the choice of orientation.
We may patch together the cylinders $T _ { i j }$ and the pairs of pants $S _ { i j k }$ to form a closed surface $\Sigma$ in $Y _ { t } - D _ { t }$ .

Lemma 3.5. The surface $\Sigma$ is orientable.

Proof.
Fix a triple point $p = p _ { i j k }$ and fix once and for all an orientation on $\tau _ { p }$ . This orients the classes $\tau \in H _ { 2 } ( V _ { i } - C _ { i } )$ , and similarly for $H _ { 2 } ( V _ { j } - C _ { j } )$ and $H _ { 2 } ( V _ { k } - C _ { k } )$ . Using the fact that the dual complex $\Gamma ( Y _ { 0 } )$ is simply connected, it is easy to see that this determines a consistent orientation on $\tau _ { q }$ for every triple point $q$ . If $\alpha _ { i j } ^ { k }$ is the boundary of the small disk on $C _ { i j }$ enclosing $p _ { i j k }$ counterclockwise (in the complex orientation on $C _ { i j }$ ), then orient the fiber $f _ { i j } ^ { k }$ over $\alpha _ { i j } ^ { k } \cap \ell _ { i j }$ so that $\alpha _ { i j } ^ { k } \times f _ { i j } ^ { k }$ gives the natural orientation on $\tau _ { p }$ . Choose the orientation on the surface $S _ { i j k }$ such that $\partial S _ { i j k } = - ( f _ { i j } ^ { k } + f _ { j k } ^ { i } + f _ { k i } ^ { j } )$ . For the other triple point $p _ { i j } \ell$ on $C _ { i j }$ , note that $\alpha _ { i j } ^ { \ell } = - \alpha _ { i j } ^ { k }$ as homology classes in $H _ { 1 } ( C _ { i j } ^ { 0 } )$ , and hence $f _ { i j } ^ { \ell } = - f _ { i j } ^ { k }$ . If $\boldsymbol { { \mathit { I } } } _ { i j } ^ { \prime }$ is oriented so that $\partial T _ { i j } = f _ { i j } ^ { k } + f _ { i j } ^ { \ell }$ , then the orientations on the $T _ { i j }$ and $S _ { i j k }$ give a consistent orientation on $\Sigma$ . q.e.d.

The homology class $[ \Sigma ]$ as described above is well-defined up to sign.
But, if we choose a different pair of pants $S _ { i j k }$ whose boundary is $f _ { i j } \cup$ $f _ { j k } \cup f _ { k i }$ then $\lfloor \Sigma \rfloor$ changes by adding a multiple of $[ \tau _ { p } ] = \gamma$ . Hence $[ \Sigma ]$ is only naturally defined mod $\mathbb { Z } \gamma$ .

As oriented 2-manifolds $T _ { i j } = \ell _ { i j } ^ { 0 } \times f _ { i j } ^ { k }$ , where $\ell _ { i j } ^ { 0 }$ is oriented so that the endpoint is $\alpha _ { i j } ^ { k } \cap \ell _ { i j }$ and the starting point is $\alpha _ { i j } ^ { \ell } \cap \ell _ { i j }$ . With these choices of orientation, $\ell _ { i j } ^ { \mathrm { { u } } } \bullet \alpha _ { i j } = - 1$ for the pairing $H _ { 1 } ( C _ { i j } ^ { 0 } , \partial C _ { i j } ^ { 0 } ) { \otimes } H _ { 1 } ( C _ { i j } ^ { 0 } )  \mathbb { Z }$ . This is independent of the superscript $k$ , in the sense that if we replace $p _ { i j k }$ by the other triple point $p _ { i j \ell }$ contained in $C _ { i j }$ , then both $\ell _ { i j } ^ { 0 }$ and $\alpha _ { i j }$ change orientation, so that $\ell _ { i j } ^ { 0 } \bullet \alpha _ { i j }$ is unchanged.

Lemma 3.6. $[ \Sigma ] \cdot [ \Sigma ] = \lambda \cdot \lambda = v$ and $[ \Sigma ] \cap D _ { t } = 0$ . In particular, $[ \Sigma ] \neq 0$ in $H _ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { Z } )$ .

Proof.
First note that $\Sigma$ is supported in a neighborhood of the singular locus of $Y _ { 0 }$ , and thus $\Sigma \cap D _ { t } = 0$ since $D _ { 0 }$ does not intersect the singular locus of $Y _ { 0 }$ . To compute $\left[ \Sigma \right] \cdot \left[ \Sigma \right]$ , we sum local contributions to the intersection number.
Each cylinder $T _ { i j }$ may be perturbed to a cylinder $T _ { i j } ^ { \prime }$ by perturbing the path $\ell _ { i j }$ to a path $\ell _ { i j } ^ { \prime }$ which only intersects $\ell _ { i j }$ at the two triple points.
Then $T _ { i j } \cap T _ { i j } ^ { \prime } = 0$ .

In the model of the Clemens collapse above, $c ^ { - 1 } ( \alpha _ { i j } ^ { k } )$ , $c ^ { - 1 } ( \alpha _ { j k } ^ { i } )$ , and $c ^ { - 1 } ( \alpha _ { k i } ^ { j } )$ are three fibers of $\sigma _ { p } \times \tau _ { p } \to \sigma _ { p }$ which map to the three center points of the edges of $\sigma _ { p }$ . Then $f _ { i j } ^ { \prime }$ , $f _ { j k } ^ { \prime }$ , and $f _ { k i } ^ { \prime }$ are three circles in each of these three fibers, homologous to $f _ { i j }$ , $f _ { j k }$ , and $f _ { k i }$ . Let $q$ and $q ^ { \prime }$ be two points in the interior of $\sigma _ { p }$ .

Let $A _ { i j }$ , $A _ { j k }$ , and $A _ { k i }$ be three cylinders which fiber over segments connecting $q$ and the midpoints of the edges of $\sigma _ { p }$ , one boundary component of each cylinder being $f _ { i j }$ , $f _ { j k }$ , and $f _ { k i }$ . Then the union of the boundary components of $A _ { i j }$ , $A _ { j k }$ , and $A _ { k i }$ which are contained in the fiber over $q$ is null-homologous in this fiber.
Thus, there is a chain $B _ { i j k }$ supported in the fiber over $q$ such that $\partial ( B _ { i j k } \cup A _ { i j } \cup A _ { j k } \cup A _ { k i } ) \ =$ $- ( f _ { i j } + f _ { j k } + f _ { k i } )$ . In other words, we can replace the pair of pants $S _ { i j k }$ by $B _ { i j k } \cup A _ { i j } \cup A _ { j k } \cup A _ { k i }$ .

Define $A _ { i j } ^ { \prime }$ , $A _ { j k } ^ { \prime }$ , $A _ { k i } ^ { \prime }$ , and $B _ { i j k } ^ { \prime }$ analogously to replace a pair of pants $S _ { i j k } ^ { \prime }$ whose boundary is $- ( f _ { i j } ^ { \prime } + f _ { j k } ^ { \prime } + f _ { k i } ^ { \prime } )$ . By choosing paths from $q$ and $q ^ { \prime }$ to the midpoints appropriately, we can ensure that there is only one torus fiber in which the representatives of $S _ { i j k }$ and $S _ { i j k } ^ { \prime }$ can intersect.
Furthermore, we may assume that the two cylinders passing though this fiber are $A _ { i j }$ and $A _ { j k } ^ { \prime }$ . Then, our two representatives of $S _ { i j k }$ and $S _ { i j k } ^ { \prime }$ have exactly one positively oriented intersection.
Hence, each pair of pants $S _ { i j k }$ contributes 1 to the self-intersection of $\lfloor \Sigma \rfloor$ , and each cylinder $\mathit { T } _ { i j }$ contributes 0. Thus $[ \Sigma ] \cdot [ \Sigma ] = v$ . q.e.d.

Proposition 3.7. $[ \Sigma ]$ mod $\mathbb { Z } \gamma = \pm \lambda$ .

Proof.
Note that $[ \Sigma ] \in H _ { 2 } ( \mathcal { y } - \mathcal { D } ; \mathbb { Z } )$ can be constructed for arbitrarily small $t$ . Thus, $[ \Sigma ]$ is supported in an arbitrarily small tubular neighborhood of $\cup _ { i j } \ell _ { i j }$ . But $\cup _ { i j } \ell _ { i j }$ has real dimension one.
Hence the class $[ \Sigma ]$ in $H _ { 2 } ( \mathcal { V } - \mathcal { D } ; \mathbb { Z } ) = H _ { 2 } ( Y _ { 0 } - D _ { 0 } ; \mathbb { Z } )$ is zero.
That is, $[ \Sigma ]$ is in the kernel of the specialization map $H _ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { Z } ) \to H _ { 2 } ( Y _ { 0 } - D _ { 0 } ; \mathbb { Z } )$ .

Any element of $\operatorname { I m } ( H ^ { 2 } ( Y _ { 0 } - D _ { 0 } ; \mathbb { Q } ) \to H ^ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { Q } ) )$ pairs with $[ \Sigma ]$ to zero, since the specialization map preserves the pairing between homology and cohomology.
Furthermore $[ \Sigma ] \neq 0$ in $H _ { 2 } ( Y _ { t } - D _ { t } , \mathbb { Q } )$ by Lemma 3.6. By the equivalence of $( \mathrm { i i i } ) ^ { \prime }$ and $( \mathrm { i v } ) ^ { \prime }$ of Corollary 2.23, $\operatorname { I m } ( H ^ { 2 } ( Y _ { 0 } - D _ { 0 } ; \mathbb { Q } ) \to H ^ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { Q } ) )$ has codimension one in $H ^ { 2 } ( Y _ { t } -$ $D _ { t } ; \mathbb { Q } )$ , and hence

$$
\mathrm { I m } ( H ^ { 2 } ( Y _ { 0 } - D _ { 0 } ; \mathbb { Q } ) \to H ^ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { Q } ) ) = \{ \alpha \colon \alpha ( [ \Sigma ] ) = 0 \} .
$$

By definition, the $T$ -invariant classes in $x \in \overline { { H } } _ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { Z } )$ are those satisfying $x \bullet \lambda = 0$ . Since the image of the specialization map on cohomology is contained in the set of $T$ -invariant classes, we conclude that $\lambda = c [ \Sigma ]$ mod $\mathbb { Z } \gamma$ for some $c \in \mathbb { Q } ^ { * }$ . Since $\lambda \cdot \lambda = \left\lfloor \Sigma \right\rfloor \cdot \left\lfloor \Sigma \right\rfloor \neq 0$ , we must have $c = \pm 1$ . q.e.d.

A priori $\lambda \in \Lambda ^ { \vee }$ , but we may now conclude:

Corollary 3.8. The class $\lambda \in \Lambda$ .

Proof.
Visibly, $\lambda = \pm \lfloor \Sigma \rfloor$ is the image of a class in $H _ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { Z } )$ . q.e.d.

Proposition 3.9. Let sp: $H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } ) \to H ^ { 2 } ( Y _ { t } ; \mathbb { Z } )$ be the specialization map in cohomology.

(i) Coker sp $\cong \mathbb { Z }$ .\
(ii) In the notation of Lemma $\it 2 . 1 4$ , Coker $d = 0$ .\
(iii) An element $\alpha \ \in \ H ^ { 2 } ( Y _ { t } ; \mathbb { Z } )$ lifts to an element of $H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } ) \ \cong$ $\mathrm { P i c } Y _ { 0 } \cong \mathrm { P i c } y \iff \alpha ( \lambda ) = 0 \iff \alpha \cdot \lambda = 0$ , where in the last equality we identify $H _ { 2 } ( Y _ { t } ; \mathbb { Z } )$ with $H ^ { 2 } ( Y _ { t } ; \mathbb { Z } )$ via Poincar´e duality.

Proof.
(i) First we claim that Coker sp is torsion free.
Consider the Gysin spectral sequence for $\mathcal { V } - Y _ { 0 } = \mathcal { V } ^ { \ast }$ , i.e. the Leray spectral sequence for the inclusion $i \colon \mathcal { V } ^ { * } \to \mathcal { V }$ , with $E _ { 2 } ^ { p , q } = H ^ { p } ( \mathcal { V } ; R ^ { q } i _ { * } \mathbb { Z } )$ , converging to $H ^ { * } ( \mathcal { V } ^ { * } ; \mathbb { Z } )$ . Its $E _ { 2 }$ page is (all cohomology is with $\mathbb { Z }$ -coefficients):

<table><tr><td rowspan=1 colspan=1>i&lt;j&lt;k H°(pijk)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>i&lt;iHo(Cij)</td><td rowspan=1 colspan=1>①i<iH1(Cij)</td><td rowspan=1 colspan=1>①i<i H²(Cij)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1> H(Vi)</td><td rowspan=1 colspan=1>H(Vi)</td><td rowspan=1 colspan=1>H(Vi）</td><td rowspan=1 colspan=1>H(Vi)</td><td rowspan=1 colspan=1>H4(Vi)</td></tr><tr><td rowspan=1 colspan=1>H()</td><td rowspan=1 colspan=1>H1()</td><td rowspan=1 colspan=1>H²()</td><td rowspan=1 colspan=1>H3（）</td><td rowspan=1 colspan=1>H4（)</td></tr></table>

This yields an exact sequence

$$
\begin{array} { r } { \bigoplus _ { i } H ^ { 0 } ( V _ { i } ; \mathbb { Z } ) \cong \mathbb { Z } ^ { f } \to H ^ { 2 } ( \mathcal { V } ; \mathbb { Z } ) \to H ^ { 2 } ( \mathcal { V } ^ { * } ; \mathbb { Z } ) } \end{array}
$$

and $H ^ { 2 } ( \mathcal { V } ^ { * } ; \mathbb { Z } ) / \operatorname { I m } ( H ^ { 2 } ( \mathcal { V } ; \mathbb { Z } ) )$ has a filtration with one quotient equal to $\operatorname { K e r } ( \bigoplus _ { i } H ^ { 1 } ( V _ { i } ; \mathbb { Z } ) \to H ^ { 3 } ( \mathcal { V } ; \mathbb { Z } ) )$ and the second contained in

$$
\ker \big ( \bigoplus _ { i , j } H ^ { 0 } ( C _ { i j } ; \mathbb { Z } ) \to \bigoplus _ { i } H ^ { 2 } ( V _ { i } ; \mathbb { Z } ) \big ) .
$$

Both $\bigoplus _ { i } H ^ { 1 } ( V _ { i } ; \mathbb { Z } ) \ : = \ : H ^ { 1 } ( V _ { 0 } ; \mathbb { Z } ) \cong \mathbb { Z }$ and $\begin{array} { r l } {  { \bigoplus _ { i j } H ^ { 0 } ( C _ { i j } ; \mathbb { Z } ) } ~ } & { { } } \end{array}$ are torsion free.
Thus $H ^ { 2 } ( \mathcal { V } ^ { * } ; \mathbb { Z } ) / \operatorname { I m } ( H ^ { 2 } ( \mathcal { V } ; \mathbb { Z } ) )$ is torsion free.
By the Wang sequence, since $N = T - I = 0$ on $H ^ { 2 } ( Y _ { t } ; \mathbb { Z } )$ , restriction to a fiber induces an isomorphism $H ^ { 2 } ( \mathcal { V } ^ { * } ; \mathbb { Z } ) \cong H ^ { 2 } ( Y _ { t } ; \mathbb { Z } )$ . As $H ^ { 2 } ( \mathcal { V } ; \mathbb { Z } ) \cong H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } )$ , the map $H ^ { 2 } ( \mathcal { V } ; \mathbb { Z } ) \to H ^ { 2 } ( \mathcal { V } ^ { * } ; \mathbb { Z } )$ is identified with the specialization map $H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } ) \to H ^ { 2 } ( Y _ { t } ; \mathbb { Z } )$ . Thus $\mathrm { C o k e r s p } \cong H ^ { 2 } ( \mathcal { V } ^ { * } ; \mathbb { Z } ) / \operatorname { I m } ( H ^ { 2 } ( \mathcal { V } ; \mathbb { Z } ) )$ is torsion free.

The specialization map in cohomology is dual to the map $H _ { 2 } ( Y _ { t } ; \mathbb { Z } ) \to$ $H _ { 2 } ( Y _ { 0 } ; \mathbb { Z } )$ . Since $\lambda \in \operatorname { K e r } ( \operatorname { s p } \colon H _ { 2 } ( Y _ { t } ; \mathbb { Q } ) \to H _ { 2 } ( Y _ { 0 } ; \mathbb { Q } ) )$ and $\lambda \neq 0$ since $\lambda ^ { 2 } > 0$ , we see that the kernel of $H _ { 2 } ( Y _ { t } ; \mathbb { Z } ) \to H _ { 2 } ( Y _ { 0 } ; \mathbb { Z } )$ has rank at least one.
Dually, the rank of Coker sp is at least one.
Then Coker sp has rank exactly one by Corollary 2.23, and hence ${ \mathrm { C o k e r s p } } \cong \mathbb { Z }$ .

(ii) This follows immediately from Corollary 2.23.

(iii) By (i), the cokernel of $H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } ) \to H ^ { 2 } ( Y _ { t } ; \mathbb { Z } )$ is $\mathbb { Z }$ , and in particular the image of $H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } )$ in $H ^ { 2 } ( Y _ { t } ; \mathbb { Z } )$ is a primitive sublattice of corank one containing

$$
\{ \alpha \in H ^ { 2 } ( Y _ { t } ; \mathbb { Z } ) : \alpha ( \lambda ) = 0 \} .
$$

Since $\{ \alpha \in H ^ { 2 } ( Y _ { t } ; \mathbb { Z } ) : \alpha ( \lambda ) = 0 \}$ is also primitive of corank one, it is equal to the image of $H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } )$ in $H ^ { 2 } ( Y _ { t } ; \mathbb { Z } )$ , which is a restatement of (iii).
q.e.d.

Remark 3.10. The above shows that the local invariant cycle theorem holds for $H ^ { 2 } ( Y _ { t } - D _ { t } )$ , in fact over $\mathbb { Z }$ : A class $x \in H ^ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { Z } )$ is in the image of $H ^ { 2 } ( Y _ { 0 } - D _ { 0 } ; \mathbb { Z } ) \iff N ( x ) = 0$ . Note that this result fails for $H ^ { 2 } ( Y _ { t } )$ (even with $\mathbb { Q }$ -coefficients).

The class $\lambda$ has the following additional property, in the notation of Definition 1.3:

Proposition 3.11. Viewing $\lambda$ as an element of $\Lambda _ { \mathbb { R } }$ , for a unique choice of sign, $\pm \lambda \in B _ { \mathrm { g e n } }$ .

Proof.
Using Lemma 1.2, it suffices to show that (i) $\lambda \cdot \alpha \neq 0$ for all effective numerical exceptional curves $\alpha$ and that (ii) if $\alpha _ { 1 }$ and $\alpha _ { 2 }$ are two different effective numerical exceptional curves, then $\lambda \cdot \left[ \alpha _ { 1 } \right]$ and $\lambda \cdot \left[ \alpha _ { 2 } \right]$ have the same sign.
To see (i), suppose that $\alpha$ is an effective numerical exceptional curve and that $\lambda \cdot \alpha = 0$ . Note that the condition that $\alpha$ is effective is independent of $t \in \Delta ^ { * }$ . By Proposition 3.9, there exists a line bundle $\mathcal { L }$ on $y$ such that $c _ { 1 } ( \mathcal { L } | _ { Y _ { t } } ) = \alpha$ for $t \neq 0$ . Thus $h ^ { 0 } ( Y _ { t } ; \mathcal { L } \big | _ { Y _ { t } } ) > 0$ for all $t \neq 0$ , and hence by semicontinuity $h ^ { 0 } ( Y _ { 0 } ; \mathcal { L } \big | _ { Y _ { 0 } } ) > 0$ and there is a nonzero section $s$ of $\mathcal { L }$ . Choose a such a nonzero section $s$ . After removing all possible components of $Y _ { 0 }$ from the divisor $( s )$ of zeroes of s on Y, we can assume that (s) is flat over ∆, i.e. all fibers of π

(s) have dimension one.
Restricting to $Y _ { 0 }$ , there exists an effective Cartier divisor $C$ on $Y _ { 0 }$ such that $C \cdot D = 1$ . But every such divisor $C$ is a sum of the form $\textstyle \sum _ { i } n _ { i } D _ { i }$ , where $n _ { i } \geq 0$ , plus components disjoint from $D$ . Since $D \cdot D _ { i } \leq 0$ for every $i$ , this is impossible.

The proof of (ii) is similar: If $\alpha _ { 1 }$ and $\alpha _ { 2 }$ are two different effective numerical exceptional curves such that $\lambda \cdot [ \alpha _ { 1 } ]$ and $\lambda \cdot \left[ \alpha _ { 2 } \right]$ have opposite signs, then there exist positive integers $n$ and $m$ such that $\lambda \cdot \left( n \alpha _ { 1 } + \right.$ $m \alpha _ { 2 } ) = 0$ . Arguing as in the proof of (i), there exists an effective Cartier divisor $C$ on $Y _ { 0 }$ such that $C \cdot D = n + m > 0$ , and we reach a contradiction as before.
q.e.d.

Remark 3.12. In the above proof, it is crucial that $H ^ { 1 } ( Y _ { 0 } ; { \mathcal { O } } _ { Y _ { 0 } } ) = 0$ so that $\operatorname { P i c } Y _ { 0 } \cong \operatorname { P i c } y \cong H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } )$ .

From now on, by convention, we fix the orientation on $D$ so that $\lambda \in B _ { \mathrm { g e n } }$ .

Definition 3.13. If $\pi \colon ( \mathcal { V } , \mathcal { D } ) \to \Delta$ is a Type III degeneration, we define the monodromy invariant of $y$ to be the class $\lambda \in B _ { \mathrm { g e n } } \cap \Lambda$ modulo the action of $\Gamma ( Y , D )$ , the group of admissible isometries.
The monodromy invariant only depends on the central fiber $( Y _ { 0 } , D )$ , and so we shall also use the above to define the monodromy invariant of a $d$ -semistable Type III anticanonical pair.

A Type III degeneration is of $\mathbb { Q }$ -type $\lambda$ if its monodromy invariant is of the form $r \lambda$ , $r \in \mathbb { Q } ^ { + }$ . The $\mathbb { Q }$ -type only depends on the family $( \mathcal { V } ^ { * } , \mathcal { D } ^ { * } ) \ \to \ \Delta ^ { * }$ and is preserved by base change.
In particular, let $\overline { { \pi } } \colon ( \overline { { \mathcal { V } } } , \mathcal { D } )  \Delta$ a one parameter family whose central fiber is the contraction of the cusp $D ^ { \prime }$ in $V _ { 0 }$ and whose general fiber has only RDP singularities.
By the argument of [10, Theorem 2.5], possibly after a base change, the family $\overline { { \pi } } \colon ( \overline { { \mathcal { V } } } , \mathcal { D } )  \Delta$ is birational to a Type III degeneration $\pi \colon ( \mathcal { V } , \mathcal { D } )  \Delta$ via a birational isomorphism which is a minimal resolution on the fibers away from 0. Thus, it makes sense to say $\overline { { \pi } } \colon \overline { { \mathcal { V } } }  \Delta$ is of $\mathbb { Q }$ -type $\lambda$ .

3.3. A symplectic description of monodromy.
In this section we describe the monodromy of $y  \Delta$ in terms of the Lagrangian torus fibration over $\Gamma ( Y _ { 0 } ) \backslash \{ v _ { 0 } \}$ .

Proposition 3.14. Suppose that $Y _ { 0 }$ is generic as in Definition 2.9. Let

$$
\mu \colon ( X , D , \omega )  \Gamma ( Y _ { 0 } )
$$

be the map constructed in Proposition 2.11. There is a diffeomorphism $\phi \colon ( X , D )  ( Y _ { t } , D _ { t } )$ such that:

(i) $\phi ( D _ { i } ) = D _ { i }$ , (ii) $\phi _ { * } ( [ \mu ^ { - 1 } ( p ) ] ) = \gamma$ , and (iii) $\phi _ { * } ( [ \omega ] ) = \pm \lambda$ mod $\mathbb { Z } \gamma$ .

Proof.
We remark that (ii) is vacuous unless we restrict $\phi$ to $X - D$ . First, we construct the diffeomorphism $\phi$ . Let $B = \Gamma ( Y _ { 0 } ) - \{ v _ { 0 } \}$ and let $B _ { 0 }$ denote the non-singular locus of $B$ where the fibers of $\mu$ are smooth.
Then $\mu ^ { - 1 } ( B _ { 0 } )$ is the quotient of the symplectic manifold $T ^ { * } B _ { 0 }$ by a lattice $T _ { \mathbb { Z } } ^ { * } B _ { 0 } \subset T ^ { * } B _ { 0 }$ of Lagrangian sections of ${ T ^ { * } B _ { 0 } \to B _ { 0 } }$ :

$$
\mu ^ { - 1 } ( B _ { 0 } ) \cong T _ { \mathbb { Z } } ^ { * } B _ { 0 } \backslash T ^ { * } B _ { 0 } .
$$

Consider the intersection complex $\Gamma ( Y _ { 0 } ) ^ { \vee }$ of $Y _ { 0 }$ , which has a face for each surface $V _ { i }$ , an edge for each double curve $C _ { i j }$ , and a trivalent vertex for each triple point $p _ { i j k }$ . There is diffeomorphism from $\Gamma ( Y _ { 0 } ) ^ { \vee }$ into the dual complex $\Gamma ( Y _ { 0 } )$ such that:

1. The image of a vertex of $\Gamma ( Y _ { 0 } ) ^ { \vee }$ lies in the associated triangle of $\Gamma ( Y _ { 0 } )$ .

2. The image of an edge of $\Gamma ( Y _ { 0 } ) ^ { \vee }$ crosses the associated edge of $\Gamma ( Y _ { 0 } )$ .

3. The image of a face of $\Gamma ( Y _ { 0 } ) ^ { \vee }$ contains the associated vertex of $\Gamma ( Y _ { 0 } )$ .

See Figure 1 for example.
There is a canonical isomorphism

$$
H _ { 1 } ( X _ { b } ; \mathbb { Z } ) \cong T _ { \mathbb { Z } , b } ^ { * } B _ { 0 } \subset T _ { b } ^ { * } B _ { 0 } .
$$

Let $e _ { i j } ^ { \vee }$ be an edge in the one-skeleton of $\Gamma ( Y _ { 0 } ) ^ { \vee }$ . It intersects the associated edge $e _ { i j }$ in the one-skeleton of $\Gamma ( Y _ { 0 } )$ at one point $b \in B _ { 0 }$ . Up to sign, there is a unique primitive co-vector $\eta _ { i j } \in T _ { \mathbb { Z } , b } ^ { * } B _ { 0 } \subset T _ { b } ^ { * } B _ { 0 }$ which vanishes on the edge $e _ { i j }$ . The three cycles $\eta _ { i j }$ , $\eta _ { j k }$ , and $\eta _ { k i }$ mutually form bases of $H _ { 1 } ( X _ { b } , \mathbb { Z } )$ because $f _ { i j k }$ is a basis triangle.
Let $C _ { i j }$ , $C _ { i k }$ , and $C _ { i \ell }$ be three adjacent double curves on $V _ { i }$ . Then by construction of the integral-affine structure on $\Gamma ( Y _ { 0 } )$ , we have $\eta _ { i j } + \eta _ { i \ell } = d _ { i k } \eta _ { i k }$ , where $d _ { i k } = - C _ { i k } ^ { 2 }$ . For $i \neq 0$ let

$$
\mu _ { i } \colon ( V _ { i } , C _ { i } , \omega _ { i } )  B _ { i }
$$

be an arbitrary almost toric fibration of $( V _ { i } , C _ { i } )$ and for $i = 0$ let $\mu _ { 0 }$ denote the composition of the two-torus fibration of $V _ { 0 }$ over an annulus with the map which collapses the image of $D$ to a point.
Then for all $i$ , the components of $C _ { i }$ fiber over the components of the boundary of $B _ { i }$ .

Let $F _ { i }$ be the interior of a face of $\Gamma ( Y _ { 0 } ) ^ { \vee }$ and consider

$$
\mu { \big | } _ { F _ { i } } : \mu ^ { - 1 } ( F _ { i } ) \to F _ { i } .
$$

Suppose $i \neq 0$ . We claim there is a fiber-preserving diffeomorphism between $\mu { \big \vert } _ { F _ { i } }$ and $\left.
\mu _ { i } \right| _ { \mathrm { i n t } ( B _ { i } ) }$ . First note that the vanishing cycles $\eta _ { i j } ^ { \prime }$ associated to a component $C _ { i j } \subset C _ { i }$ in an almost toric fibration of $( V _ { i } , C _ { i } )$ also satisfy the equation

$$
\eta _ { i j } ^ { \prime } + \eta _ { i \ell } ^ { \prime } = d _ { i k } \eta _ { i k } ^ { \prime } .
$$

Thus, the monodromy of $\mu _ { i }$ restricted to a neighborhood of $\partial B _ { i }$ is the same as the monodromy of $\mu$ restricted to a neighborhood of $\partial F _ { i }$ . Thus, there is a diffeomorphism between $\mu { \big \vert } _ { F _ { i } }$ and $\mu _ { i } \big | _ { \mathrm { i n t } ( B _ { i } ) }$ in a neighborhood of their boundaries.
We may furthermore assume that the boundary components of $F _ { i }$ and $B _ { i }$ are identified and that in a neighborhood of a boundary component, $\eta _ { i j }$ and $\eta _ { i j } ^ { \prime }$ are identified by the diffeomorphism.

As there is either zero or one irreducible nodal fiber of both $\mu _ { i }$ and $\mu { \big \vert } _ { F _ { i } }$ , depending on whether $Q ( V _ { i } , C _ { i } ) = 0$ or $1$ , we can extend this diffeomorphism to one between all of $\mu { \big \vert } _ { F _ { i } }$ and $\left.
\mu _ { i } \right| _ { \mathrm { i n t } ( B _ { i } ) }$ . Note that these fibrations are smoothly equivalent, but not necessarily equivalent as Lagrangian torus fibrations.
Also, note that $\mu { \big \vert } _ { F _ { 0 } }$ and $\mu _ { 0 }$ are diffeomorphic as they both give the 2-torus fibration on $V _ { 0 } - C _ { 0 }$ , and the cycle $D$ is sent to itself.

We now construct a torus fibration in a neighborhood $U \subset Y _ { t }$ of $( Y _ { 0 } ) _ { \mathrm { s i n g } }$ as follows—in a neighborhood of a triple point $p \in Y _ { 0 }$ , we use the model $\sigma _ { p } \times \tau _ { p } \to \tau _ { p }$ defined above.
Near the degeneration to a double curve of $Y _ { 0 }$ , we have a local model defined by $x y = t$ . Furthermore, we may choose a third coordinate $z$ which restricts on the double locus $x y = 0$ to a global coordinate on $\mathbb { P } ^ { 1 }$ . Then

$$
( x , y , z ) \mapsto ( | x | , | y | , | z | )
$$

defines a 2-torus fibration on $x y = t$ whose fibers near $z = 0$ and $z = \infty$ are homologous to the fibers of the torus fibration near a triple point.
Let $\pi : U \to V$ be this two-torus fibration.
Then $V$ is diffeomorphic to a tubular neighborhood of the 1-skeleton of $\Gamma ( Y _ { 0 } ) ^ { \vee }$ , and we may further assume that $c ^ { - 1 } ( ( Y _ { 0 } ) _ { \mathrm { s i n g } } )$ fibers over the 1-skeleton of $\Gamma ( Y _ { 0 } ) ^ { \vee }$ . The class $\eta _ { i j } ^ { \prime }$ defined as the vanishing cycle of $C _ { i j }$ in the almost toric fibration $\mu _ { i }$ is identified in $c ^ { - 1 } ( V _ { i } ) \cap U$ with the class of $c ^ { - 1 } ( p _ { i j } )$ for some generic point $p _ { i j } \in C _ { i j }$ .

Thus, we see that $Y _ { t }$ is the fiber connect sum of the $\left.
\mu _ { i } \right| _ { \mathrm { i n t } ( B _ { i } ) }$ , in which $\eta _ { i j } ^ { \prime }$ is identified with $\eta _ { j i } ^ { \prime }$ . Since $\mu \colon ( X , D , \omega )  \Gamma ( Y _ { 0 } )$ is the fiber connect sum of the $\mu { \big \vert } _ { F _ { i } }$ in which $\eta _ { i j }$ and $\eta _ { j i }$ are identified, and we have fiberpreserving diffeomorphisms from $\left.
\mu _ { i } \right| _ { \mathrm { i n t } ( B _ { i } ) }$ to $\mu { \big \vert } _ { F _ { i } }$ which identify $\eta _ { i j }$ with $\eta _ { i j } ^ { \prime }$ , we conclude that there is a diffeomorphism $\phi \colon ( X , D )  ( Y _ { t } , D _ { t } )$ . The cycle $D$ is sent to $D _ { t }$ by construction, thus property $^ 1$ is satisfied.
Property 2 also follows immediately from construction.

Finally, we show $\phi _ { * } ( [ \omega ] ) : = ( \phi ^ { - 1 } ) ^ { * } ( [ \omega ] ) = \pm \lambda$ mod $\mathbb { Z } \gamma$ , in the sense that

$$
\phi _ { * } ( [ \omega ] ) ( x ) = \lambda \bullet x
$$

for any class $x \in H _ { 2 } ( Y _ { t } - D _ { t } ; \mathbb { Z } )$ . First, we must have $\phi _ { * } ( [ \omega ] ) ( \gamma ) = 0$ . This is clear because the fibers of $\mu$ are Lagrangian.
We henceforth elide $\phi _ { * }$ and consider $( X , D )$ and $( Y _ { t } , D _ { t } )$ identified.

Proposition 3.9 implies that an element $x \in H _ { 2 } ( Y _ { 0 } - D , \partial )$ may be represented by a union of surfaces $S _ { i } \subset V _ { i }$ , closed for $i \neq 0$ , meeting the $C _ { i j }$ transversally and such that $[ S _ { i } ] \cdot [ C _ { i j } ] = [ S _ { j } ] \cdot [ C _ { j i } ] : = n _ { i j }$ , and such that $\partial S _ { 0 } \subset \partial$ . Choose $S _ { i }$ such that $S _ { i } \cap C _ { i j } = S _ { j } \cap C _ { j i }$ and no $S _ { i }$ contains a triple point of $Y _ { 0 }$ . Letting $S = \cup S _ { i }$ we have that $c ^ { - 1 } ( S )$ is a surface whose class in $H _ { 2 } ( Y _ { t } - D _ { t } , \partial )$ specializes to $x$ . Let $A _ { i j } \subset ( X , D , \omega )$ denote a Lagrangian cylinder lying over the edge $e _ { i j } \subset \Gamma ( Y _ { 0 } ) ^ { [ 1 ] }$ in the one-skeleton of the dual complex.
Denote its two boundary components by $U _ { i j } \subset X _ { v _ { i } }$ and $U _ { j i } \subset X _ { v _ { j } }$ . Note that when $X _ { v _ { i } }$ is singular, we may have $U _ { i j } = \varnothing$ , because $U _ { i j }$ could be the vanishing cycle of the node of $X _ { v _ { i } }$ . We need the following lemma:

Lemma 3.15. For $i \neq 0$ there is a (unique) class $[ S _ { i } ] \in H _ { 2 } ( V _ { i } ; \mathbb { Z } )$ satisfying $[ S _ { i } ] \cdot [ C _ { i j } ] = n _ { i j }$ if and only if

$$
\sum _ { j } n _ { i j } [ U _ { i j } ] = 0 \in H _ { 1 } ( X _ { v _ { i } } ; \mathbb { Z } ) .
$$

For $i = 0$ , there are no linear conditions on the $n _ { 0 j }$

Proof.
When $v _ { i }$ is nonsingular, $( V _ { i } , C _ { i } )$ is toric, and there is an exact sequence

$$
0 \to H _ { 2 } ( V _ { i } ; \mathbb { Z } ) \to \bigoplus _ { j } \mathbb { Z } C _ { i j } ^ { * } \to \mathbb { Z } ^ { 2 } \to 0
$$

where the first map sends $x \mapsto ( n _ { i j } )$ if $x \cdot C _ { i j } = n _ { i j }$ and the second map sends $( n _ { i j } ) \mapsto \textstyle \sum _ { j } n _ { i j } v _ { i j }$ where $v _ { i j } = e _ { i j }$ are the primitive integral vectors spanning the one-dimensional rays of the fan of $( V _ { i } , C _ { i } )$ corresponding to the components $C _ { i j }$ . By the description of the Lagrangian cylinders $A _ { i j }$ given in Remark 2.10, the condition $\sum n _ { i j } v _ { i j } = 0$ exactly implies that the sum of the boundaries of $n _ { i j } A _ { i j }$ lying over $v _ { i }$ are null-homologous.

When $v _ { i }$ is singular and $i \neq 0$ , we have $Q ( V _ { i } , C _ { i } ) = 1$ . Let

$$
\pi \colon \left( V _ { i } , C _ { i } \right) \to \left( \overline { { V _ { i } } } , \overline { { C } } _ { i } \right)
$$

be an internal blow-down to a toric pair, if such a blowdown exists (the general case is easy to deduce from this case).
The exceptional curve $E$ meets a component $C _ { i j _ { 0 } }$ such that $e _ { i j _ { 0 } }$ lies in the monodromyinvariant line through $v _ { i }$ . Then every element of $H _ { 2 } ( V _ { i } ; \mathbb { Z } )$ is of the form $x = n E + \pi ^ { * } { \overline { { x } } }$ for some $\overline { { x } } \in H _ { 2 } ( \overline { { V _ { i } } } ; \mathbb { Z } )$ . Let $v _ { i j }$ be the primitive integral vectors in the fan of $\overline { { V _ { i } } }$ . Then there is a class in $x \in H _ { 2 } ( V _ { i } ; \mathbb { Z } )$ such that $x \cdot C _ { i j } = n _ { i j }$ if and only if $\textstyle \sum _ { j } n _ { i j } v _ { i j }$ lies in the line spanned by $v _ { i j _ { 0 } }$ . Equivalently, if we deformed $A _ { i j }$ slightly so that their boundaries lay in a fiber near the fiber over $v _ { i }$ , we would have that $\sum n _ { i j } A _ { i j }$ is homologous to the circle which when transported along the monodromyinvariant line produces a Lagrangian cylinder.
But this circle is exactly the vanishing cycle of the node in the fiber over $v _ { i }$ , and so $\textstyle \sum _ { j } n _ { i j } [ U _ { i j } ]$ is null-homologous in $X _ { v _ { i } }$ .

Possibly scaling all the $n _ { i j }$ by a large integer, we may construct a class $S _ { 0 }$ satisfying $\left.
S _ { 0 } \right.
\cdot C _ { 0 j } = n _ { 0 j }$ because the components of $C _ { 0 } = D ^ { \prime }$ span a negative-definite lattice.
q.e.d.

Thus, for $i \neq 0$ the boundary of $\sum n _ { i j } A _ { i j }$ is the boundary of a chain $Z$ supported in $\bigcup X _ { v _ { i } }$ . Note that $X _ { v _ { 0 } } = D$ , so the boundary of $A _ { 0 i }$ lying over $v _ { 0 }$ is contained in $\partial$ . Then under the identification defined by $\phi$ , the cycle $- Z + \textstyle \sum n _ { i j } A _ { i j }$ represents $[ c ^ { - 1 } ( S ) ]$ because each cylinder $A _ { i j }$ gets pinched by the Clemens collapse to give an intersection point with $C _ { i j }$ and a class in $H _ { 2 } ( Y _ { 0 } - D , \partial )$ is uniquely determined by the numbers $n _ { i j }$ . Since the fibers and $A _ { i j }$ are Lagrangian, we conclude that

$$
\int _ { c ^ { - 1 } ( S ) } \omega = 0 .
$$

Consider the exact sequence

$$
H _ { 2 } ( \partial )  H _ { 2 } ( Y _ { t } - D _ { t } )  H _ { 2 } ( Y _ { t } - D _ { t } , \partial )
$$

from Section 1.1. While there is no pairing between $H ^ { 2 } ( Y _ { t } - D _ { t } )$ , which contains $[ \omega ]$ , and $H _ { 2 } ( Y _ { t } - D _ { t } , \partial )$ , which contains $[ c ^ { - 1 } ( S ) ]$ , we may conclude that the monodromy-invariant classes in $H _ { 2 } ( Y _ { t } - D _ { t } )$ pair with $[ \omega ]$ to give zero, since these map to the monodromy-invariant classes in $H _ { 2 } ( Y _ { t } - D _ { t } , \partial )$ . We remark that that $[ \omega ]$ pairs with $\mathbb { Z } \gamma$ , the image of $H _ { 2 } ( \partial )$ , to be zero.

Since the monodromy-fixed classes in $H _ { 2 } ( Y _ { t } - D _ { t } )$ are those that pair with $\lambda$ to zero, we conclude $[ \omega ] = c \lambda$ mod $\gamma$ in the sense above, for some constant $c \in \mathbb { R }$ . Finally, we note that

$$
[ \omega ] \cdot [ \omega ] = 2 \cdot \mathrm { A r e a } ( \Gamma ( Y _ { 0 } ) ) = \# ( \mathrm { t r i p l e ~ p o i n t s ~ o f ~ } Y _ { 0 } ) = \lambda \cdot \lambda .
$$

Hence $c = \pm 1$ .

q.e.d.

Remark 3.16. The above proposition has an interpretation in terms of mirror symmetry.
Taking the connected sums of the almost toric fibrations $\mu _ { i }$ gives a topological model for the SYZ fibration on a general fiber of the algebraic degeneration $\mathcal { V }$ . This fibration is, topologically, the SYZ dual of the fibration $( X , D , \omega )  B$ , and thus, the fact that $( Y _ { t } , D _ { t } )$ and $( X , D )$ are diffeomorphic is essentially a fluke due to working in dimension two.

If we choose $\omega _ { i }$ in Proposition 3.14 such that $[ \omega _ { i } ] \cdot D _ { i j } = [ \omega _ { j } ] \cdot D _ { j i }$ , then the bases $B _ { i }$ glue together to produce an integral-affine structure on $\Gamma ( Y _ { 0 } ) ^ { \vee } \backslash \{ v _ { 0 } \}$ , see for instance the first author’s thesis, Example 6.3.5. This integral-affine structure, when “seen from a great distance” in the language of Gross-Hacking-Keel, is the main integral-affine manifold of interest in [14], cf.
Sections 0.3 and 1.2. It is essentially the pseudo-fan ${ \mathfrak { F } } ( Y , D )$ , but is constructed by gluing copies of $\mathbb { R } ^ { 2 }$ together, rather than lattice triangles.
The “fine detail” lost by viewing the SYZ fibration from a great distance is exactly the information of the SNC resolution of the smoothing.

Proposition 3.14 has appeared in various forms throughout the mirror symmetry literature.
Given a non-singular affine surface $B$ , its “radiance obstruction” is the class in $H ^ { 1 } ( B , T _ { B } ^ { \mathrm { H a t } } )$ which in local affine coordinates is represented by

$$
( \partial / \partial x ) \otimes d x + ( \partial / \partial y ) \otimes d y .
$$

The evaluation of this 1-cocycle on a 1-chain in $B$ coincides with the evaluation of the symplectic form $\omega$ on the associated cylinder, see e.g. Section 3.1.1 of [21]. The radiance obstruction measures the obstruction to the existence of a global flat section of the SYZ fibration.
Furthermore, the monodromy about a large complex structure limit point of Calabi-Yau manifolds is expected to be a higher dimensional analogue of a Dehn twist given by translation by a section of the SYZ fibration, see Conjecture 3.7 of [12]. Thus the monodromy action on cohomology is given by cup product with the radiance obstruction, as shown in

Theorem 5.1 of [16]. In fact, it is likely that the methods of proof there could verify Proposition 3.14 in this noncompact situation.

We may now strengthen Looijenga’s conjecture to give a lower bound for the number of smoothing components of a cusp singularity:

Theorem 3.17. The number of smoothing components of the cusp singularity $p ^ { \prime }$ with minimal resolution $D ^ { \prime }$ is greater than or equal to the number of deformation families of anticanonical pairs $( X , D )$ .

Proof.
The construction of [5] inputs an anticanonical pair $( X , D )$ and outputs some Type III anticanonical pair $Y _ { 0 }$ which is generic such that

$$
\mu : ( X , D , \omega )  \Gamma ( Y _ { 0 } )
$$

is the extension of a Lagrangian torus fibration as in Proposition 2.11, though $\omega$ is not kept track of in [5]. By Proposition 3.14, there is a diffeomorphism $( X , D )  ( Y _ { t } , D _ { t } )$ such that $\phi ( D _ { i } ) = D _ { i }$ . By Theorem 5.14 of [9], the existence of a diffeomorphism between two anticanonical pairs preserving the classes $[ D _ { i } ]$ implies that the pairs are deformation equivalent.
Thus $( Y _ { t } , D _ { t } )$ is deformation-equivalent to $( X , D )$ . Hence, we have constructed a semistable model of a smoothing of $p ^ { \prime }$ whose generic fiber is deformation-equivalent to $( X , D )$ . Furthermore, if two one-parameter smoothings have non-deformation equivalent generic fibers, they lie on different smoothing components.
The theorem follows.
q.e.d.

The Type III anticanonical pair $Y _ { 0 }$ in Theorem 3.17 is in fact reconstructed from $\mu$ by triangulating the base and inverting the procedure defined in Section 2.2 which constructs $\Gamma ( Y _ { 0 } )$ from $Y _ { 0 }$ . Essentially, Proposition 3.14 and the reconstruction procedure in [5] reduce the problem of finding a Type III degeneration $y  \Delta$ whose monodromy invariant is any given element of $B _ { \mathrm { g e n } } \cap \Lambda$ to finding an almost toric fibration $\mu : ( X , D , \omega )  S ^ { 2 }$ whose symplectic form has any given class in $B _ { \mathrm { g e n } } \cap \Lambda$ . This requires a more delicate construction than in [5], and is the purpose of Section 5.

# 4. Birational modification and base change of Type III degenerations

In this section we collect various ways to modify a Type III degeneration $y  \Delta$ , and then describe effect of these modifications on the dual complex of the central fiber $\Gamma ( Y _ { 0 } )$ , as an integral-affine surface.

Let $C \ \cong \ \mathbb { P } ^ { 1 }$ be a smooth rational curve in a smooth threefold $y$ whose normal bundle is $\mathcal { O } _ { C } ( - 1 ) \oplus \mathcal { O } _ { C } ( - 1 )$ . Then the exceptional locus of the blowup $\operatorname { B l } _ { C } \mathcal { y }$ is isomorphic to $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ and we may blow down by contracting along the other ruling of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ . Such a birational modification is an example of a flop.
Flops centered on the central fiber of $\mathcal { V }$ are (rather confusingly) called Type 0, I, and II birational modifications depending on how they meet the double locus of $Y _ { 0 }$ :

Definition 4.1. Let $y  \Delta$ be a Type III degeneration.
A flop centered on $C \subset Y _ { 0 }$ is called:

(i) A Type 0 modification if $C$ does not intersect $( Y _ { 0 } ) _ { \mathrm { s i n g } }$ . In this case, $C$ is a smooth $- 2$ -curve on a component of $Y _ { 0 }$ and $C$ does not deform to the general fiber.
(However, somewhat more general modifications are also allowed.)\
(ii) A Type I modification if $C$ intersects $( Y _ { 0 } ) _ { \mathrm { s i n g } }$ but is not contained in it.
In this case, $C$ is an exceptional curve on a component $V _ { i }$ of $Y _ { 0 }$ .\
(iii) A Type II modification if $C$ is contained in $( Y _ { 0 } ) _ { \mathrm { s i n g } }$ . In this case, $C = C _ { i j }$ is an exceptional curve on both components $V _ { i }$ and $V _ { j }$ which contain it.

Proposition 4.2. Let $y  \Delta$ be a Type III degeneration, and let $C \subset Y _ { 0 }$ be the center of a flop.

(i) A Type 0 modification does not change the isomorphism type of $Y _ { 0 }$ .\
(ii) A Type I modification blows down $C$ on the component $V _ { i }$ containing it and blows up the point $C \cap V _ { j }$ on $V _ { j }$ , where $V _ { j }$ is the unique component of $Y _ { 0 }$ such that $C \cdot C _ { i j } = 1$ . See Figure 2.\
(iii) A Type II modification blows down $C = C _ { i j }$ on the two components $V _ { i }$ and $V _ { j }$ containing it, and blows up the points $C \cap V _ { k }$ and $C \cap V _ { \ell }$ on the two remaining components $V _ { k }$ and $V _ { \ell }$ which intersect $C$ . See Figure 3.

Proof.
Since the components of $Y _ { 0 }$ are locally smooth divisors in $\mathcal { V }$ , the blow-up and blow-down commute with restriction to the components of $Y _ { 0 }$ . The proposition follows.
Note that the Type I modification is an internal blow-down on $V _ { i }$ and an internal blow-up on $V _ { j }$ while the Type II modification is a corner blow-down on $V _ { i }$ and $V _ { j }$ and a corner blow-up on $V _ { k }$ and $V _ { \ell }$ . q.e.d.

![](images/9defe05efadf3c61576c3567175896c63ecfba31bed667b750d68df1de20e935.jpg)\
Figure 2. Two components of the central fiber before and after a Type I modification.

Next, we describe a standard resolution of an order $k$ base change of a Type III degeneration which produces another Type III degeneration.

![](images/31383274bd6790cf3b1757dd6423b960aad0b80d8e76b1e4121f95ec802db594.jpg)\
Figure 3. Four components of the central fiber before and after a Type II modification.

![](images/73464911311707774cd9a6d58f8da488233376138692fccb616987a057060cad.jpg)\
Figure 4. On the right, the components of the central fiber $Y _ { 0 }$ [3] of the standard resolution $\mathcal { V } [ 3 ]  \Delta$ an order 3 base change.

Proposition 4.3. Let $y  \Delta$ be a Type III degeneration.
Consider the order $k$ base change:

$$
{ \begin{array} { r l } { \displaystyle { \mathcal { V } } \times _ { k } \Delta \ } & { \longrightarrow \ { \mathcal { V } } } \\ { \Big \downarrow } & { \Big \downarrow } \\ { \Delta } & { \mathrel { \xrightarrow { } } \ \Delta } \end{array} }
$$

There is a standard resolution $\mathcal { V } [ k ] \to \mathcal { V } \times _ { k } \Delta$ , see Figure 4, such that $\mathcal { V } [ k ]  \Delta$ is a Type III degeneration.
As an integral-affine manifold the dual complex of the central fiber $\Gamma ( Y _ { 0 } [ k ] )$ is the subdivision of each triangle of $\Gamma ( Y _ { 0 } )$ into $k ^ { 2 }$ triangles in the standard manner, where each of the $k ^ { 2 }$ sub-triangles has the structure of a lattice triangle of area $\frac { 1 } { 2 }$ .

Proof.
See [7] for proof of the first statement.
The second claim then follows directly from the definition of the integral-affine structure on the dual complex, see Section 2.2. q.e.d.

Remark 4.4. Note that Type 0, I, and II modifications do not change the monodromy invariant of the degeneration $y  \Delta$ because the punctured family $\mathcal { V } ^ { * } \to \Delta ^ { * }$ is unaffected by the modifications.
On the other hand, taking the base change $\mathcal { V } [ k ]  \Delta$ multiplies the monodromy invariant by $k$ , because the base change $t \mapsto t ^ { k }$ is a $k$ -fold covering of the punctured family.

We now examine the effect of the birational modifications on the dual complex.
The Type II modification is simplest:

Proposition 4.5. Let $\mathcal { V } \mathrm { ~ --  ~ } \mathcal { V } ^ { \prime }$ be a Type II modification along the double curve $C _ { i j } = V _ { i } \cap V _ { j }$ . The edge $e _ { i j }$ of $\Gamma ( Y _ { 0 } )$ associated to $C _ { i j }$ is the diagonal of a quadrilateral $( v _ { i } , v _ { k } , v _ { j } , v _ { \ell } )$ integral-affine equivalent to a unit square.
Furthermore $\Gamma ( Y _ { 0 } )$ and $\Gamma ( Y _ { 0 } ^ { \prime } )$ are isomorphic as integralaffine manifolds, but their triangulations differ: $\Gamma ( Y _ { 0 } ^ { \prime } )$ contains the other diagonal of this quadrilateral.

Proof.
Since $C _ { i j } ^ { 2 } = - 1$ , the directed edges of $\Gamma ( Y _ { 0 } )$ satisfy the equation

$$
e _ { i k } + e _ { i \ell } = e _ { i j } .
$$

Eq. (1) implies the first statement because the integral-affine structure on $( v _ { i } , v _ { k } , v _ { j } , v _ { \ell } )$ is uniquely determined by $C _ { i j } ^ { 2 }$ and the unit square satisfies Eq (1). The second statement follows from (iii) of Proposition 4.2: Switching the diagonal of the quadrilateral corresponds exactly to the changes in the self-intersection sequence of the four anticanonical pairs $V _ { i }$ , $V _ { j }$ , $V _ { k }$ , and $V _ { \ell }$ involved in the Type II modification.
q.e.d.

Before we describe the effect of a Type I modification on $\Gamma ( Y _ { 0 } )$ , we must introduce a surgery on integral-affine surfaces:

Definition 4.6. Let $S _ { 0 }$ be an integral-affine surface and let $p \in S _ { 0 }$ be an $A _ { 1 }$ singularity.
Parameterize a monodromy-invariant ray originating at $p$ by a segment

$$
\gamma \colon [ 0 , \epsilon ] \to S _ { 0 }
$$

where $\gamma ( 0 ) = p$ . There is a family of integral-affine manifolds $S _ { t }$ for all $t \in [ 0 , \epsilon ]$ which are isomorphic to $S _ { 0 }$ in the complement of $\gamma ( [ 0 , t ] )$ and which have an $A _ { 1 }$ singularity at $\gamma ( t )$ . We say that $S _ { t }$ is a nodal slide of $S _ { 0 }$ . See [37], Section 6.

Remark 4.7. It is shown in [37] that if the surfaces $S _ { t }$ are bases of almost toric fibrations $( X _ { t } , \omega _ { t } )  S _ { t }$ , then $( X _ { t } , \omega _ { t } )$ are symplectomorphic.
In particular, the class $\left[ \omega _ { t } \right]$ is constant under the Gauss-Manin connection.

To quantify the “amount” of nodal slide, we need a natural measure of the length of a straight line segment in an integral-affine manifold:

Definition 4.8. Let $L \subset S$ be a straight line segment with rational slope in an integral-affine surface $S$ . The lattice length of $L$ is the unique positive multiple $r$ of a primitive integral vector $\boldsymbol { v }$ such that $r v = L$ in some chart.

We may now describe the effect of a Type I modification on $\Gamma ( Y _ { 0 } )$

Proposition 4.9. Let $y \  \ y ^ { \prime }$ be a Type $I$ modification along a curve $C$ such that $C \cdot C _ { i j } = 1$ . Then $\Gamma ( Y _ { 0 } )$ and $\Gamma ( Y _ { 0 } ^ { \prime } )$ are isomorphic as simplicial complexes but the integral-affine structure on $\Gamma ( Y _ { 0 } ^ { \prime } )$ is the result of a nodal slide of lattice length 1 along the directed edge $e _ { i j }$ of $\Gamma ( Y _ { 0 } )$ .

Proof.
The proof follows from Proposition 4.2(ii) and Proposition 2.10 of [5], which describes the effect of an internal blow-up on the pseudo-fan of an anticanonical pair.
q.e.d.

Remark 4.10. Let $S _ { t }$ for $t \in \mathsf {  { \left[ 0 , 1 \right] } }$ denote the family of integralaffine surfaces in Proposition 4.9, so that $S _ { 0 } = \Gamma ( Y _ { 0 } )$ and $S _ { 1 } = \Gamma ( Y _ { 0 } ^ { \prime } )$ . Then $S _ { t }$ has an $A _ { 1 }$ singularity at $t$ for all $t \in ( 0 , 1 )$ but at $t = 0 , 1$ , this singularity may collide with an already existing singularity.
In particular, $p _ { i }$ is singular for $t \neq 0$ if $Q ( V _ { i } ^ { \prime } , C _ { i } ^ { \prime } ) \geq 1$ and $p _ { j }$ is singular for $t \neq 1$ if $Q ( V _ { j } , C _ { j } ) \geq 1$ . In these cases, the singularity at $p _ { i }$ or $p _ { j }$ factors into an $A _ { 1 }$ singularity and the remaining singularity as one performs the nodal slide which extracts the $A _ { 1 }$ singularity.

In light of Remark 4.10, we introduce the following definition:

Definition 4.11. Let $p$ be an integral-affine surface singularity.
A factorization of $p$ into $A _ { 1 }$ singularities is a collection of nodal slides of $A _ { 1 }$ singularities which collide to form $p$ .

Proposition 4.12. Let $\mathfrak { F } ( V , D )$ be the pseudo-fan of an anticanonical pair $( V , D )$ . Let $\pi \colon ( V , D ) \to ( { \overline { { V } } } , { \overline { { D } } } )$ be a toric model, that is, $a$ blowdown of $Q ( V , D )$ disjoint internal exceptional curves $\{ E _ { i } \}$ . Then $( \overline { { V } } , \overline { { D } } )$ is necessarily toric.
Let $n _ { j } : = \# \{ E _ { i } \left| \ E _ { i } \cdot D _ { j } = 1 \right.
\}$ . Then $\mathfrak { F } ( V , D )$ admits a factorization into $A _ { 1 }$ singularities where $n _ { j }$ of the singularities have monodromy-invariant lines along the edge $e _ { j } \subset \mathfrak { F } ( V , D )$ associated to the component $D _ { j }$ .

Proof.
Proposition 2.10 of [5] gives a construction of $\mathfrak { F } ( V , D )$ from $\mathfrak { F } ( \overline { { V } } , \overline { { D } } )$ which corresponds exactly to colliding an $A _ { 1 }$ singularities with monodromy-invariant lines along an edges of $\mathfrak { F } ( \overline { { V } } , \overline { { D } } )$ associated to components of $\overline { { D } }$ receiving an internal blow-up.
The Proposition follows.
q.e.d.

Example 4.13. The converse to Proposition 4.12 is false.
That is, even if $\mathfrak { F } ( V , D )$ has a factorization into $A _ { 1 }$ singularities with monodromyinvariant lines along a collection of edges $e _ { j }$ , the pair $( V , D )$ may not have a toric model with exceptional curves meeting the associated components $D _ { j }$ . For instance, keeping track of the labeling, there are two deformation types of anticanonical pairs $( V , D _ { 1 } + \cdots + D _ { 5 } )$ with

$$
( D _ { i } ^ { 2 } ) = ( 1 , - 1 - 2 , - 2 , - 1 ) .
$$

One has disjoint exceptional curves meeting $D _ { 2 }$ and $D _ { 4 }$ and the other has disjoint exceptional curves meeting $D _ { 3 }$ and $D _ { 5 }$ , but these two possibilities are mutually exclusive.
For either deformation type, $\mathfrak { F } ( V , D )$ is the same.
Thus $\mathfrak { F } ( V , D )$ admits two factorizations into $A _ { 1 }$ singularities, only one of which comes from a toric model of $( V , D )$ .

# 5. Degenerations with given monodromy invariant

5.1. Construction of degenerations.
We have most of the necessary tools to prove that any $\lambda \in B _ { \mathrm { g e n } } \cap \Lambda$ is the monodromy invariant of some Type III degeneration, but first we must introduce a surgery on integralaffine surfaces corresponding to an internal blow-up.
Let $( X , D , \omega )  B$ be an almost toric fibration.
Then $P = \partial B$ is locally polygonal, and the components $D _ { i } \subset D$ fiber over the edges $P _ { i } \subset P$ .

Definition 5.1. An almost toric blow-up, see [37] Section 5.4 or [5] Definition 3.3, is a surgery on $B$ which produces a new integral-affine surface with singularities $\tilde { B }$ and an almost toric fibration

$$
( \tilde { X } , \tilde { D } , \tilde { \omega } )  \tilde { B }
$$

whose base is $\tilde { B }$ . To construct $\tilde { B }$ , we remove a triangle, called the surgery triangle, in $B$ resting on an edge $P _ { i }$ and glue the two remaining edges together by a matrix conjugate to

$$
\left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 0 } } & { { 1 } } \end{array} \right) ,
$$

at the expense of introducing an $A _ { 1 }$ singularity at the interior vertex of the triangle, whose monodromy-invariant line is parallel to $P _ { i }$ . Then

$$
\pi \colon ( { \tilde { X } } , { \tilde { D } } )  ( X , D )
$$

is an interior blow-up at a point on $D _ { i }$ . The size $b$ of the surgery is the lattice length of the base of the surgery triangle, and is the area of the exceptional curve with respect to $\tilde { \omega }$ . In fact $[ \tilde { \omega } ] = \pi ^ { * } [ \omega ] - b E$ where $E$ is the class of the exceptional curve.

A sphere in $\tilde { X }$ representing the exceptional curve can be constructed which fibers over the path in $\tilde { B }$ which is the identified pair of edges of the surgery triangle.
This path connects $\tilde { P } _ { i }$ to the $A _ { 1 }$ singularity introduced.
One forms the sphere from a family of circles homologous to the vanishing cycle of the nodal fiber over the singularity.
These circles collapse to points over the two endpoints of the path.

Remark 5.2. Even when we begin with a symplectic anticanonical pair $( X , D , \omega )$ which has a compatible complex structure, such as a symplectic toric surface, Symington’s blow-up operation is a priori purely symplectic-topological.
We never use a complex structure on $( X , D , \omega )$ . But, it is possible when the size $b$ is small to upgrade the blow-up operation for Lagrangian fibrations with respect to a K¨ahler form, see e.g. Section 4 of [1]. In addition, it is possible to retain a Hamiltonian $S ^ { 1 }$ action in a neighborhood of each exceptional curve.

Definition 5.3. Let $L$ be a straight line segment in a non-singular integral-affine surface $S$ and let $v$ be a primitive integral vector pointing along $L$ . Suppose that $\gamma \colon [ 0 , 1 ] \to S$ is a path in $S$ such that $\gamma ( 0 ) \in L$ . The lattice distance (along $\gamma$ ) from $L \subset B$ to $\gamma ( 1 )$ is the integral

$$
\int _ { 0 } ^ { 1 } \gamma ^ { \prime } ( t ) \times v \ d t .
$$

Note that the cross product is preserved by integral-affine transformations, and thus the integral is well-defined.
In fact, the lattice length is invariant if we deform the path within the nonsingular locus of $B$ , so long as we fix $\gamma ( 1 )$ and keep the condition $\gamma ( 0 ) \in L$ . The lattice distance from the interior vertex of a surgery triangle to its base is necessarily equal to the lattice length of the base.

We begin with a theorem regarding the class of an ample divisor:

Theorem 5.4. Let $( X , D )$ be an anticanonical pair.
Suppose $\lambda \in$ $\mathcal { A } _ { \mathrm { g e n } }$ . There exists an almost toric fibration $( X , D , \omega )  B$ such that $[ \omega ] = \lambda$ .

Proof.
Suppose that $r ( D ) \geq 3$ and that $\lambda \in \mathcal { A } _ { \mathrm { g e n } } \cap H ^ { 2 } ( X ; \mathbb { Z } )$ . By Proposition 1.5, we may express $\lambda$ in the form

$$
\lambda = \sum a _ { j } [ D _ { j } ] + \sum b _ { i j } [ E _ { i j } ]
$$

with $E _ { i j }$ disjoint exceptional curves meeting $D _ { j }$ . Consider the blowdown

$$
( X , D )  ( X _ { 0 } , D _ { 0 } )
$$

of the curves $\{ E _ { i j } \}$ . By Proposition 1.3 of [13], after some corner blowups $( X _ { 1 } , D _ { 1 } )  ( X _ { 0 } , D _ { 0 } )$ there is a toric model $( X _ { 1 } , D _ { 1 } )  ( { \overline { { X } } } , { \overline { { D } } } )$ . Since $D  D _ { 0 }$ is an isomorphism, we may perform the same sequence of corner blow-ups $\nu \colon ( \tilde { X } , \tilde { D } ) \to ( X , D )$ to produce a toric model

$$
\pi \colon ( { \tilde { X } } , { \tilde { D } } )  ( { \overline { { X } } } , { \overline { { D } } } )
$$

which blows down the $E _ { i j }$ and possibly other internal exceptional curves.

Pulling back the expression for $\lambda$ gives

$$
\nu ^ { * } \lambda = \sum c _ { j } [ \tilde { D } _ { j } ] + \sum b _ { i j } [ E _ { i j } ]
$$

for some constants $c _ { j }$ . For simplicity of notation, we index the components of $\tilde { D }$ such that $\nu ( \tilde { D } _ { j } ) = D _ { j }$ . Then when $\tilde { D } _ { j }$ is not one of $c _ { j } = a _ { j }$\
the corner blow-ups of $\nu$ . Furthermore, we identify $\nu ^ { - 1 } ( E _ { i j } )$ with $E _ { i j }$ . Because $\lambda$ is nef, we have $\lambda \cdot [ E _ { i j } ] = c _ { j } - b _ { i j } \ge 0$ . Now re-write the above expression as

$$
\nu ^ { * } \lambda = \sum c _ { j } \pi ^ { * } ( [ \overline { { D } } _ { j } ] ) + \sum ( b _ { i j } - c _ { j } ) [ F _ { i j } ]
$$

where $\{ F _ { i j } \} \supset \{ E _ { i j } \}$ is the set of exceptional curves blown down by $\pi$ . We have $b _ { i j } = 0$ exactly for those exceptional curves in $\{ F _ { i j } \} - \{ E _ { i j } \}$ . The coefficients $b _ { i j } - c _ { j }$ are non-positive, and have absolute value less than or equal to $c _ { j }$ with equality if and only if the exceptional curve lies in $\{ F _ { i j } \} - \{ E _ { i j } \}$ . We then have the following lemma, which proves Theorem 5.4 under a technical assumption which we will later remove.

Lemma 5.5. Let $\lambda \in \mathcal { A } _ { \mathrm { g e n } } \cap H ^ { 2 } ( X ; \mathbb { Z } )$ and suppose $r ( D ) \geq 3$ . In the notation above, suppose that $b _ { i j } \neq 0$ for all $F _ { i j }$ . Then the conclusion of Theorem 5.4 holds for $\lambda$ .

Proof.
Linearizing the action of $( \mathbb { C } ^ { * } ) ^ { 2 }$ on the space of sections

$$
H ^ { 0 } ( \overline { { X } } ; \mathcal { O } _ { \overline { { X } } } ( \pi _ { * } ( \nu ^ { * } \lambda ) ) )
$$

gives a polytope $\overline { B }$ for $( \overline { { \cal X } } , \overline { { \cal D } } )$ whose integral points correspond to torus equivariant sections.
Note that $\sum c _ { j } \overline { { D } } _ { j }$ is a torus invariant divisor in the linear system of $\pi _ { * } ( \nu ^ { * } \lambda )$ because it is a linear combination of boundary components, so it corresponds to a lattice point $p \in { \overline { { B } } }$ .

The moment map is a Lagrangian torus fibration

$$
( \overline { { { X } } } , \overline { { { D } } } )  \overline { { { B } } }
$$

such that the components $\overline { { D } } _ { j }$ fiber over the components ${ \overline { { P } } } _ { j }$ . We will produce via almost toric blowups on $\overline { B }$ an almost toric fibration $( X , D , \omega ) $ $B$ such that $[ \omega ] = \lambda$ . We must therefore find for all $F _ { i j }$ disjoint surgery triangles of size $m _ { i j } : = c _ { j } - b _ { i j }$ resting on the edge ${ \overline { { P } } } _ { j }$ . To see why we can perform the necessary surgeries, we need the following facts:

Fact 1: The point $p$ has lattice distance $c _ { j }$ from the edge ${ \overline { { P } } } _ { j }$ . This is a well-known formula in toric geometry.
Fact 2: The lattice length of ${ \overline { { P } } } _ { j }$ is at least the sum of the lengths of the bases of all surgery triangles which must rest on ${ \overline { { P } } } _ { j }$ .

Fact 2 follows from the ampleness of $\lambda$ —we have the equation

$$
\mathrm { l a t t i c e ~ l e n g t h } ( \overline { { P } } _ { j } ) = \pi _ { * } ( \nu ^ { * } \lambda ) \cdot [ \overline { { D } } _ { j } ] = \nu ^ { * } \lambda \cdot \tilde { D } _ { j } + \sum _ { j } m _ { i j }
$$

![](images/290a2a46f27a34abf230edc430052ac1e50942cdc22338f2a4ae0c0d6d55a21f.jpg)\
Figure 5. Surgery triangles in $\overline { B }$ of size $m _ { i j } : = c _ { j } - b _ { i j }$ .

and thus the lattice length of $P _ { j }$ is at least $\textstyle \sum _ { j } m _ { i j }$ . By Fact $1$ , $p$ is at least as distant as is necessary to perform the surgeries associated to $\{ F _ { i j } \} _ { i }$ within the triangle formed by $P _ { j }$ and $p$ —each surgery has size $m _ { i j }$ . By Fact 2, the length of ${ \overline { { P } } } _ { j }$ is large enough to accommodate all the surgeries.

Figure 5 illustrates a general method for finding the necessary triangles, though the figure is deceptive in two ways: (1) Two $F _ { i j }$ satisfy $b _ { i j } = 0$ and correspondingly there are two surgery triangles which involve $p$ , whereas by assumption of the lemma $b _ { i j } \neq 0$ and (2) the edges of $B$ will have nonzero lattice length after the surgeries because $\lambda$ is ample.
We will ultimately relax both the ampleness condition and the assumption that $b _ { i j } \neq 0$ .

Let $P = \partial B$ . After surgeries, the lattice length of the edge $P _ { j } \subset P$ over which $D _ { j }$ fibers is $\nu ^ { * } \lambda \cdot [ \tilde { D } _ { j } ]$ , which is positive, since $\lambda \in \mathcal { A } _ { \mathrm { g e n } }$ . Since each edge of $B$ corresponding to one of the corner blow-ups in

$$
\nu : ( \tilde { X } , \tilde { D } ) \to ( X , D )
$$

has length zero, we have that $B$ is in fact the base of an almost toric fibration $( X , D , \omega )  B$ such that $[ \omega ] = \lambda$ . q.e.d.

We must now remove the assumption that $b _ { i j } ~ \neq ~ 0$ . When some $b _ { i j } = 0$ , the proof of Lemma 5.5 fails because multiple surgery triangles may overlap at the vertex $p$ . See for instance Figure 5 (though as before, the figure is still deceptive because the components $P _ { j }$ have positive lattice length when $\lambda$ is ample).
We may still construct $B$ as an integral-affine surface, but $B$ is not the base of an almost toric fibration, because $p$ need not be an $A _ { k }$ singularity.
Thus we show:

Lemma 5.6. There is a family of integral-affine surfaces $B _ { t }$ for $t \in$ $\left\lfloor 0 , \epsilon \right\rfloor$ with $B _ { 0 } = B$ which factorizes of $p$ into $A _ { 1 }$ singularities along nodal slides.
Furthermore, $B _ { t }$ for $t \neq 0$ is the base of an almost toric fibration

$$
( X _ { t } , D _ { t } , \omega _ { t } )  B _ { t }
$$

such that $[ \omega _ { t } ] = \lambda$ .

Proof.
Each surgery triangle resting on ${ \overline { { P } } } _ { j }$ introduces an $A _ { 1 }$ singularity with monodromy-invariant line parallel to $P _ { j }$ . We may therefore factor $p$ into a collection of $A _ { 1 }$ singularities $\{ q _ { i j } \}$ , one for each exceptional curve $F _ { i j }$ such that $b _ { i j } = 0$ . To construct $B _ { t }$ , we simultaneously perform nodal slides along segments which are cyclically ordered about $p$ in the same ordering as the edges of $P$ . Consider the almost toric fibration $( X _ { t } , D _ { t } , \omega _ { t } )  B _ { t }$ . We must show that $( X _ { t } , D _ { t } )$ is diffeomorphic to $( X , D )$ and that $\vert \omega _ { t } \vert = \lambda$ .

There is a collection of disjoint paths

$$
\gamma _ { i j } \colon [ 0 , 1 ] \to B _ { t }
$$

satisfying $\gamma _ { i j } ( 0 ) \in P _ { j }$ and $\gamma _ { i j } ( 1 ) = q _ { i j }$ . Furthermore, the monodromyinvariant line of $q _ { i j }$ is parallel to $P _ { j }$ under the trivialization of integralaffine structure along $\gamma _ { i j }$ . Thus, as is the case for the usual almost toric blow-up, there are smooth $( - 1 )$ -spheres $F _ { i j } ^ { \prime }$ which fiber over $\gamma _ { i j }$ and intersect $D _ { j }$ . So $( X _ { t } , D _ { t } )$ and $( X , D )$ have the same toric model, and are thus diffeomorphic.
To prove $[ \omega _ { t } ] = \lambda$ , we must show $\left.
\omega _ { t } \right.
\cdot F _ { i j } = m _ { i j }$ . But $\int _ { { F } _ { i j } } \omega _ { t }$ is the lattice distance from $P _ { j }$ to $q _ { i j }$ . This lattice distance is $m _ { i j }$ , because the lattice distance from $P _ { j }$ to $p$ is equal to $m _ { i j }$ and nodal slides parallel to $P _ { j }$ keep the lattice distance constant.
q.e.d.

Hence we have proven Theorem 5.4 for any $\lambda \in \mathcal { A } _ { \mathrm { g e n } } \cap H ^ { 2 } ( X ; \mathbb { Z } )$ such that $r ( D ) \ge 3$ . We may cheaply deduce the result for $\lambda \in \mathcal { A } _ { \mathrm { g e n } } \cap$ $H ^ { 2 } ( X ; \mathbb { Q } )$ by scaling the symplectic form.
To prove Theorem 5.4 for real classes, we must show that the conclusion of Proposition 1.5 holds with real coefficients for any $\lambda \in \mathcal { A } _ { \mathrm { g e n } }$ . We avoid going into details, since we will not use this result in the rest of the paper, but the proof follows from a continuity argument—the polyhedra in $\mathcal { A } _ { \mathrm { g e n } }$ defined by

$$
\left\{ \sum a _ { j } D _ { j } + \sum b _ { i } E _ { i } \left| a _ { j } , b _ { i } \in \mathbb { R } ^ { \geq 0 } \right. \right\} ,
$$

where the $E _ { i }$ are disjoint exceptional curves, are locally finite, and thus their union is closed.
Furthermore, their union contains $\mathcal { A } _ { \mathrm { g e n } } \cap$ $H ^ { 2 } ( X ; \mathbb { Q } )$ . Thus, any $\lambda \in { \mathcal { A } } _ { \mathrm { g e n } }$ may be expressed as $\sum a _ { j } D _ { j } + \sum b _ { i } E _ { i }$ for some $a _ { j } , b _ { i } \in \mathbb { R } ^ { + }$ and the proof of Theorem 5.4 goes through as before.

Finally, when $r ( D ) ~ \leq ~ 2$ we perform some corner blow-ups until $r ( D ) \ge 3$ . Then we may apply Proposition 1.5 and the proof applies, with the caveat that we must blow down these initial corner blow-ups (as the symplectic form will be degenerate on them) to produce a nondegenerate almost toric fibration on $( X , D )$ . q.e.d.

Remark 5.7. We can weaken the assumption of Theorem 5.4 by assuming only that $\lambda$ is nef and big.
In this case, we can apply the method of Theorem 5.4, but there are two ways the fibration $\mu$ can degenerate.

First, the length of a boundary component $P _ { j } \subset P$ has length zero if $\lambda \cdot [ D _ { j } ] = 0$ . This results in a fibration with $\mu ( D _ { j } )$ a point, in fact a vertex of $B$ . Furthermore, the symplectic form is only non-degenerate on the complement of $D _ { j }$ . If $\lambda \cdot [ D _ { j } ] = 0$ for all $j$ , that is $\lambda \in \Lambda$ , then the whole boundary $P$ consists of a single point, and thus the base of $\mu$ is an integral-affine sphere and the symplectic form is only non-degenerate on $X - D$ . This is the case shown in Figure 5.

Second, if $\lambda \cdot E _ { i j } = 0$ then the surgery associated to $E _ { i j }$ will have size zero, that is, $\mu ( E _ { i j } )$ will be some point on the interior of the edge $P _ { j }$ and $\omega$ will be the pull-back of a symplectic form from the blowdown of $E _ { i j }$ .

Proposition 5.8. Let $\lambda \in H ^ { 2 } ( X ; \mathbb { Z } )$ be big and nef.
Let $( X , D , \omega ) $ $B$ be the almost toric fibration constructed in Theorem 5.4, which may be degenerate in the sense of Remark 5.7. There are nodal slides on $B$ until every singularity lies at an integral point.

Proof.
First, undo the nodal slides of Lemma 5.6 which factor $p$ into $A _ { 1 }$ singularities, as $p$ is an integral point.
Even so, as shown in Figure 5, the surgery associated to an exceptional curve $E _ { i j }$ may introduce a singularity at a rational but non-integral point, and thus we must modify the construction of Lemma 5.5 slightly.
Within the triangle whose base is ${ \overline { { P } } } _ { j }$ and whose third vertex is $p$ , we fit triangles $\Delta _ { i j }$ whose base is a subsegment of ${ \overline { { P } } } _ { j }$ of lattice length $m _ { i j }$ and whose third vertex is $p$ , see Figure 6.

We would like to show that there is a lattice point $p _ { i j }$ of lattice distance $m _ { i j }$ from ${ \overline { { P } } } _ { j }$ within the triangle $\Delta _ { i j }$ . Let $L _ { i j }$ denote the segment inside $\Delta _ { i j }$ of points whose lattice distance is $m _ { i j }$ from ${ \overline { { P } } } _ { j }$ . Then the lattice length of $L _ { i j }$ is equal to

$$
m _ { i j } \frac { c _ { j } - m _ { i j } } { c _ { j } } .
$$

If this length is at least $_ 1$ , then $L _ { i j }$ contains an integral point.
Note

$$
m _ { i j } \frac { c _ { j } - m _ { i j } } { c _ { j } } \geq 1 \iff m _ { i j } ( c _ { j } - m _ { i j } ) \geq c _ { j } .
$$

Thus $L _ { i j }$ contains an integral point $p _ { i j }$ whenever $2 \leq m _ { i j } \leq c _ { j } - 2$

![](images/93d3ff9ec085b07c149c58d2587d48aa8a96cdedb621e3a7052a719fbe37acf6.jpg)\
Figure 6. Finding integral points for the surgery triangles resting on the edge ${ \overline { { P } } } _ { j }$ .

The remaining cases are when $m _ { i j } = 0$ , $1$ , $c _ { j } - 1$ , or $c _ { j }$ . The cases $m _ { i j } = 0$ and $m _ { i j } = c _ { j }$ are trivial—in the former case, there is no surgery to make and in the latter case, we must choose $p _ { i j } = p$ . Consider the cases mij = 1 and mij = cj − 1. Then Lij has lattice length cj−1c and its endpoints are rational points with denominator $c _ { j }$ . Thus it contains a lattice point $p _ { i j }$ . Choosing the surgery triangle associated to $F _ { i j }$ to be the triangle whose base is the segment of length $m _ { i j }$ and whose third vertex is $p _ { i j }$ produces an integral-affine surface with singularities at integral points which can be connected to $B$ by nodal slides.
q.e.d.

Theorem 5.9. For all $\lambda \in B _ { \mathrm { g e n } } \cap \Lambda$ there is a Type III degeneration $y  \Delta$ of anticanonical pairs such that the monodromy invariant of $\mathcal { V }$ is $\lambda$ .

Proof.
By Theorem 5.4 and Remark 5.7 we may construct a degenerate almost toric fibration $( X , D , \omega )  B ^ { \prime }$ with $[ \omega ] = \lambda$ . Then $B ^ { \prime }$ is a sphere, and $D$ maps to a point $v _ { 0 } \in B ^ { \prime }$ . Furthermore, we may assume that the only other singularities of $B ^ { \prime }$ are type $A _ { 1 }$ . By Proposition 5.8, we may assume that there is an integral-affine surface $B$ with singularities at integral points, connected to $B ^ { \prime }$ by small nodal slides of lattice lengths in $\scriptstyle { \frac { 1 } { n } } \mathbb { Z }$ . By Section 4 of [5], after triangulation, $B$ is the dual complex of the central fiber of a Type III degeneration $y  \Delta$ of anticanonical pairs.
But because $\Gamma ( Y _ { 0 } )$ is not generic, we cannot apply Proposition 3.14 directly.

Let $B ^ { \prime } [ n ]$ denote the integral-affine manifold which refines the lattice in $B ^ { \prime }$ to order $n$ . Equivalently, we post-compose the charts on $B ^ { \prime }$ with multiplication by $n$ . Then $B ^ { \prime } [ n ]$ is the base of an almost toric fibration on $( X , D , n \omega )$ . Note that $B ^ { \prime } [ n ]$ has singularities at integral points, and thus after triangulation, $B ^ { \prime } [ n ]$ is the dual complex of the central fiber $Y _ { 0 } ^ { \prime } [ n ]$ of a Type III degeneration

$$
\mathcal { V } ^ { \prime } [ n ]  \Delta .
$$

Furthermore, $Y _ { 0 } ^ { \prime } [ n ]$ is generic, and thus by Proposition 3.14, there is a diffeomorphism $\phi \colon X  Y _ { t } ^ { \prime } [ n ]$ such that $n \phi _ { * } ( [ \omega ] )$ is the monodromy invariant of $\mathcal { V } ^ { \prime } [ n ]$ .

Let $\mathcal { V } [ n ]  \Delta$ be the standard resolution as in Proposition 4.3 of the base change of $y  \Delta$ of order $n$ . Then $\Gamma ( Y _ { 0 } [ n ] ) = B [ n ]$ and the triangulation is the standard order $n$ refinement of the triangulation of $B$ . Note that $B ^ { \prime } [ n ]$ is given by a set of nodal slides on $B [ n ]$ all of integer lattice length.
Applying Proposition 4.5, we may perform Type II modifications on $\mathcal { \boldsymbol { y } } [ n ]$ to flip edges of the triangulation of $B [ n ]$ along diagonals of quadrilaterals.
Choosing $n$ large enough, we may ensure by [22] that there is a sequence of edge flips on $B [ n ]$ such that the segments along which one performs nodal slides to get from $B [ n ]$ to $B ^ { \prime } [ n ]$ are edges of the resulting re-triangulation.
Let $\mathcal { V } [ n ] \ \xrightarrow { } - \ \xrightarrow { } \ \mathcal { V } ^ { \prime \prime } [ n ]$ be this sequence of Type II modifications.
Then by Proposition 4.9, there is a series of Type I modifications $\mathcal { V } ^ { \prime \prime } [ n ] \ \xrightarrow { \scriptscriptstyle { - \to } } \ \mathcal { V } ^ { \prime } [ n ]$ such that $\Gamma ( \mathcal { Y } _ { 0 } ^ { \prime } [ n ] ) = B ^ { \prime } [ n ]$ , assuming we choose the appropriate toric model for the component of $Y _ { 0 } ^ { \prime \prime } [ n ]$ corresponding to the point $p$ .

Thus, $\nu [ n ]$ and $\mathcal { V } ^ { \prime } [ n ]$ are birational.
By Remark 4.4, $n [ \omega ] = n \lambda$ is the monodromy invariant of $\mathcal { V } [ n ]$ . Again by Remark 4.4, the base change of order $n$ multiplies the monodromy invariant by $n$ , and thus the monodromy invariant of $y  \Delta$ is $\lambda$ under the identification of $H ^ { 2 } ( Y _ { t } ; \mathbb { Z } )$ with $H ^ { 2 } ( X ; \mathbb { Z } )$ .

We have only proven existence up to diffeomorphism in the sense that we have constructed, for any $\lambda \in { \mathcal { B } } _ { \mathrm { g e n } } ( X ) \cap \Lambda$ , a Type III degeneration $y  \Delta$ and a diffeomorphism $\phi \colon X  Y _ { t }$ such that $\phi _ { * } [ D _ { i } ]$ is the class of the corresponding component of $D _ { t }$ and the monodromy invariant of $\mathcal { V }$ is the push-forward of $\lambda$ . By Theorem 5.14 of [9], we can conclude that $( X , D )$ and $( Y _ { t } , D _ { t } )$ are deformation equivalent.
Hence, up to self-diffeomorphism of $Y _ { t }$ preserving the components of $D _ { t }$ , every monodromy invariant can be attained.
Finally, by Theorem 5.14 of [9], the subgroup of the self-diffeomorphism group of $Y _ { t }$ which preserves the components of $D _ { t }$ acts on cohomology by the group $\Gamma = \Gamma ( Y _ { t } , D _ { t } )$ of admissible isometries, and thus, there is no difference between the monodromy invariant up to such diffeomorphisms and up to the action of $\Gamma$ . q.e.d.

Remark 5.10. Theorem 5.9 is to be expected from the perspective of mirror symmetry.
The deformation space of the partially contracted Inoue surface $\overline { { V } } _ { 0 }$ represents the “complex moduli space” for mirror symmetry, and thus should be isomorphic to the “K¨ahler moduli space” of the mirror $( X , D , \omega )$ , cf.
[29]. When $\lambda \in \mathcal { A } _ { \mathrm { g e n } } - B _ { \mathrm { g e n } }$ the linear system associated to $\lambda$ does not contract all of $D$ on the pair $( Y , D )$ , and thus, the mirror should be a Landau-Ginzburg model, whereas when $\lambda \in B _ { \mathrm { g e n } }$ , the situation is more similar to the Calabi-Yau case, as opposed to the log Calabi-Yau case.

In particular, given any class $\lambda \in B _ { \mathrm { g e n } }$ , there is a large symplectic structure limit on $( Y , D )$ given by scaling a K¨ahler form $\omega$ satisfying $[ \omega ] = \lambda$ in the complexified K¨ahler cone.
Here $\omega$ is only non-degenerate on $Y - D$ and trivial on $D$ . The corresponding deformation in the complex moduli space is a family of anticanonical pairs with monodromy invariant $\lambda$ over a punctured disk.
This family should be fillable at the origin of the disc by the large complex structure limit, i.e. $\overline { { V } } _ { 0 }$ . Thus, one expects that every $\lambda \in B _ { \mathrm { g e n } }$ arises as a monodromy invariant, and conversely that every monodromy invariant lies in $\boldsymbol { B } _ { \mathrm { g e n } }$ , as shown in Proposition 3.11.

5.2. An application to symplectic geometry.
Theorem 5.4 has a number of interesting consequences for the symplectic geometry of anticanonical pairs.
But first, we cite the following theorem about the symplectic geometry of rational surfaces, due to Li and Liu [23]:

Theorem 5.11. Let $X$ be a smooth 4-manifold with $b _ { 2 } ^ { + } ( X ) = 1$ and let $\boldsymbol { C } _ { X , K }$ denote the cone of classes of symplectic forms on $X$ with symplectic canonical class $K$ . Then

Let us further restrict to the cone $\boldsymbol { C } _ { ( X , D ) }$ of classes of symplectic forms on $X$ along with a normal crossings symplectic anticanonical divisor $D$ . By Theorem 5.11, we can conclude that

$$
\begin{array} { c } { C _ { ( X , D ) } \subset \{ x \in \mathcal { C } ^ { + } \colon x \cdot [ E ] > 0 \mathrm { ~ f o r ~ a l l ~ } E } \\ { \mathrm { ~ e x c e p t i o n a l ~ a n d ~ } x \cdot [ D _ { j } ] > 0 \} = \mathcal { A } _ { \mathrm { g e n } } } \end{array}
$$

Conversely, any element $x \in \mathcal { A } _ { \mathrm { g e n } }$ is in the K¨ahler cone of a generic $( X , D )$ because every ample class is K¨ahler.
Thus we in fact have an equality $C _ { ( X , D ) } = \mathcal { A } _ { \mathrm { g e n } }$ . Let $\mathcal { F }$ denote the set of classes of symplectic forms of almost toric fibrations $( X , D , \omega )  B$ . Clearly we have $\mathcal { F } \subset$ $\mathcal { C } _ { ( X , D ) }$ , but by Theorem 5.4, we also have ${ \mathcal { A } } _ { \mathrm { g e n } } \subset { \mathcal { F } }$ . Thus, all three are equal:

Corollary 5.12. $\mathcal { F } = C _ { ( X , D ) } = \mathcal { A } _ { \mathrm { g e n } }$ .

In particular, $\mathcal { F }$ is a convex cone.
Furthermore, every symplectic anticanonical pair $( X , D , \omega )$ has some other symplectic form in the class $[ \omega ]$ which admits a Lagrangian torus fibration.
By the main result of Li and Mak [24], we conclude that when $X$ is rational, any symplectic anticanonical pair $( X , D )$ is symplectic-isotopic (through symplectic anticanonical pairs with cycle $D$ ) to an almost toric fibration.

5.3. A conjecture on Type III degenerations.
Before we state the conjecture, let us recall the main results from [11]. Let $X$ be a $K 3$ surface.
The analogue of the group $\Gamma$ of admissible isometries is the group $O ^ { + } ( \Lambda _ { K 3 } )$ of integral isometries of spinor norm 1 of the $K 3$ lattice $\Lambda _ { K 3 }$ . Let ${ \mathcal { X } } \to \Delta$ be a (polarized or weakly K¨ahler) Type III degeneration of $K 3$ surfaces.
If $N$ is the logarithm of the monodromy of the degeneration ${ \mathcal { X } } \to \Delta$ acting on $H ^ { 2 } ( X )$ , then the saturation of $\operatorname { I m } N ^ { 2 }$ is of the form $\mathbb { Z } \gamma$ , where $\gamma$ is a primitive element of $\Lambda _ { K 3 }$ , and there exists an element $\lambda \in \gamma ^ { \perp } = W _ { 0 }$ such that, for all $x \in H ^ { 2 } ( X )$ ,

$$
N ( x ) = ( x \cdot \gamma ) \lambda - ( x \cdot \lambda ) \gamma .
$$

It is easy to see that $\lambda$ is well-defined mod $\gamma$ , i.e. as an element of $\gamma ^ { \perp } / \mathbb { Z } \gamma \cong U ^ { 2 } \oplus ( - E _ { 8 } ) ^ { 2 }$ . Furthal pair e i $\lambda ^ { 2 } > 0$ . The analogue of thepropriate component $\boldsymbol { B } _ { \mathrm { g e n } }$ $( Y , D )$ $\mathcal { C } _ { K 3 , \gamma } ^ { + }$ of the positive cone in $( \gamma ^ { \perp } / \mathbb { Z } \gamma ) \otimes _ { \mathbb { Z } } \mathbb { R }$ . Given an element $\lambda \in ( \gamma ^ { \perp } / \mathbb { Z } \gamma ) \cap$ $\mathcal { C } _ { K 3 , \gamma } ^ { + }$ , we can associate to $\lambda$ the pair of positive integers $( k , t )$ , where $t = \lambda ^ { 2 }$ and $k$ is the largest positive integer such that $\lambda = k \lambda _ { 0 }$ mod $\mathbb { Z } \gamma$ for some $\lambda _ { 0 } \in \Lambda _ { K 3 }$ . It is easy to see that the pair $( k , t )$ is a complete set of invariants for the pair $( \gamma , \lambda )$ , in the sense that, given two pairs $( \gamma , \lambda )$ and $( \gamma ^ { \prime } , \lambda ^ { \prime } )$ as above, the pairs have the same associated pair $( k , t ) \iff$ there exists a $\psi \in O ^ { + } ( \Lambda _ { K 3 } )$ such that $\psi ( \gamma ) = \gamma ^ { \prime }$ and, via the induced isometry $\gamma ^ { \perp } / \mathbb { Z } \gamma \to ( \gamma ^ { \prime } ) ^ { \perp } / \mathbb { Z } \gamma ^ { \prime }$ , $\psi ( \lambda ) = \lambda ^ { \prime }$ . The main result of [11] is then:

Theorem 5.13. (i) For every pair of positive integers $( k , t )$ , there exists a Type III degeneration of $K 3$ surfaces with invariants $( k , t )$ .

(ii) Given two Type III degenerations $x  \Delta$ and ${ \mathcal { X } } ^ { \prime } \to \Delta$ of $K 3$ surfaces, ${ \mathcal { X } } \to \Delta$ and $\mathcal { X } ^ { \prime } \to \Delta$ have the same invariants $\Longleftrightarrow$ there exists a locally trivial deformation from $X _ { 0 }$ to a Type III $K 3$ surface $X _ { 0 } ^ { \prime \prime }$ over a smooth connected base, with all fibers $d$ -semistable, and $a$ sequence of Type I and II birational modifications $X _ { 0 } ^ { \prime \prime } \ \mathrm { ~ -- \to ~ } X _ { 0 } ^ { \prime }$ .

Theorem 5.9 is then the analogue for Type III anticanonical pairs of the existence part (i) of Theorem 5.13. It is natural to conjecture that there is an analogue of (ii) of Theorem 5.13 as well:

Conjecture 5.14. Let $( \mathcal { V } , \mathcal { D } )  \Delta$ and $( \mathcal { V } ^ { \prime } , \mathcal { D } ^ { \prime } )  \Delta$ be two Type III degenerations of anticanonical pairs with monodromy invariants $\lambda$ and $\lambda ^ { \prime }$ , respectively.
Assume that $D$ and $D ^ { \prime }$ have the same self-intersection sequence and choose compatible labelings on them.
Then, there exists an admissible isometry [9, Definition 5.7] $\psi \colon H ^ { \cdot 2 } ( Y _ { t } ; \mathbb { Z } ) \to H ^ { \cdot 2 } ( Y _ { t } ^ { \prime } ; \mathbb { Z } )$ , $t \neq 0$ , such that $\psi ( \lambda ) = \lambda ^ { \prime } \iff$ there exists a locally trivial deformation from $( Y _ { 0 } , D )$ to a Type III anticanonical pair $( Y _ { 0 } ^ { \prime \prime } , D )$ over a smooth connected base, with all fibers $d$ -semistable, and a sequence of Type $I$ and II birational modifications $( Y _ { 0 } ^ { \prime \prime } , D ) \mathrel { \mathop { \textrm { -- } } } ( Y _ { 0 } ^ { \prime } , D )$ .

![](images/e0da026b08e38e9dc7df497644470c31af9b5441cdffef80e9053599e24d13d9.jpg)\
Figure 7. The combinatorial type of two Type III anticanonical pairs.

In other words, the class $\lambda$ mod $\Gamma ( Y , D )$ is a complete invariant of the combinatorial type of the central fiber.
Note that the existence of an admissible isometry implies that the pairs $( Y _ { t } , D )$ and $( Y _ { t } ^ { \prime } , D )$ are deformation equivalent, by [9, Theorem 5.13].

Example 5.15. Let $D ^ { \prime }$ be the cusp with self-intersection sequence $( - 1 2 , - 2 )$ . Consider the possible triples $( Y , D , \lambda )$ , where $D$ is the dual cusp, $\lambda \in \Lambda \cap B _ { \mathrm { g e n } }$ , and $\lambda ^ { 2 } = 2$ . There are two different Type III fibers $Y _ { 0 } = V _ { 0 } \cup V _ { 1 } \cup V _ { 2 }$ with 2 triple points.
Here $V _ { 0 }$ is the Inoue surface, $V _ { 1 } = \mathbb { F } _ { 6 }$ and the self-intersection sequence is $( 1 0 , - 6 )$ , and $V _ { 2 }$ has selfintersection sequence $( 0 , 4 )$ . Thus $V _ { 2 }$ can be either $\mathbb { F } _ { 0 } / \mathbb { F } _ { 2 }$ (and these are deformation equivalent) or $\mathbb { F } _ { 1 }$ (see Figure 7). These two Type III fibers deform into two different deformation types of anticanonical pair $( Y , D )$ with dual self-intersection sequence $( - 4 , - 2 , \ldots , - 2 )$ . The first is discussed in [8, Example 4.4]. Here $\Lambda$ is spanned by $G _ { 1 } , G _ { 2 }$ with $G _ { 1 } ^ { 2 } = 1 0 $ , $G _ { 2 } ^ { 2 } = - 2$ , and $G _ { 1 } \cdot G _ { 2 } = 0$ . It follows that the $D _ { i }$ span a primitive sublattice of $\operatorname { P i c } Y$ . There is just one $\lambda \in \Lambda$ with $\lambda ^ { 2 } = 2$ in $\boldsymbol { B } _ { \mathrm { g e n } }$ . There are no roots (i.e. $R = \emptyset$ ), $\boldsymbol { B } _ { \mathrm { g e n } }$ is an angular sector not meeting the boundary of ${ \mathcal { C } } ^ { + }$ away from $0$ , and $\Gamma ( Y , D ) = \{ 1 \}$ . This deformation type of $( Y , D )$ corresponds to the case where $V _ { 2 } = \mathbb { F } _ { 1 }$ .

To find the second embedding of the dual $D$ in a rational surface, index the curves in the dual cycle by $D _ { 0 } , \ldots , D _ { 9 }$ with $D _ { 0 } ^ { 2 } = - 4$ , $D _ { i } ^ { 2 } =$ $- 2$ , $i > 0$ , and $D _ { i }$ meets $D _ { i + 1 }$ , $D _ { 9 }$ meets $D _ { 0 }$ . Note generally that if there is a $- 1$ curve meeting $D _ { 1 }$ , then contracting it and then $D _ { 1 } , \ldots , D _ { 9 }$ leads to a surface $\overline { { Y } }$ and a nodal curve of square 8 on $\overline { { Y } }$ . Thus $Y$ must be either $\mathbb { F } _ { 0 } / \mathbb { F } _ { 2 }$ or $\mathbb { F } _ { 1 }$ . The case of ${ \overline { { Y } } } = \mathbb { F } _ { 1 }$ is the case considered above.
In case $Y = \mathbb { F } _ { 0 } / \mathbb { F } _ { 2 }$ , there is obviously a root for $( Y , D )$ (the proper transform of the $- 2$ curve on $\mathbb { F } _ { 2 }$ ). Also, one checks that the $D _ { i }$ span an index two sublattice of $\operatorname { P i c } Y$ and that $\Lambda$ is spanned by $G _ { 1 }$ , $G _ { 2 }$ with $G _ { 1 } ^ { 2 } = G _ { 2 } ^ { 2 } = - 2$ and $G _ { 1 } \cdot G _ { 2 } = 3$ . One can show that in fact both $G _ { 1 }$ and $G _ { 2 }$ are roots.
It follows that there are infinitely many roots, and hence $\Gamma ( Y , D )$ is infinite as well.
The set $\boldsymbol { B } _ { \mathrm { g e n } }$ is equal to $\mathcal { C } ^ { + }$ . It is straightforward to check that $\Gamma = \mathsf { W } ( R )$ , the reflection group generated by the roots, and all of the $\lambda \in \Lambda \cap B _ { \mathrm { g e n } }$ with $\lambda ^ { 2 } = 2$ are conjugate under $\Gamma$ . This case then corresponds to the case where $V _ { 2 }$ is either $\mathbb { F } _ { 0 }$ or $\mathbb { F } _ { 2 }$ .

To sum up, we see that within each deformation type, there is exactly one combinatorial possibility for $( Y _ { 0 } , D )$ and exactly one element of square 2 in $B _ { \mathrm { g e n } } \cap \Lambda$ mod $\Gamma$ . So Conjecture 5.14 is true in this case for classes of square 2.

# 6. Asymptotic behavior of the period map

Let $\pi \colon \mathcal { V }  \Delta$ be a Type III degeneration of anticanonical pairs.
Fix a coordinate t on ∆ and let z = $z ~ = ~ \frac { \log t } { 2 \pi \sqrt { - 1 } }$ be the corresponding coordinate on the universal cover $\nu \colon \widetilde { \Delta } ^ { * } \to \Delta ^ { * }$ . Thus $t = e ^ { 2 \pi \sqrt { - 1 } z }$ and $\operatorname { I m } z = - { \frac { \log | t | } { 2 \pi } }$ is well-defined on $\Delta ^ { * }$ . As usual, let $\mathcal { V } ^ { \ast } = \mathcal { V } | _ { \Delta ^ { \ast } }$ and let $\rho \colon \mathcal { V } ^ { * } - \mathcal { D }  \Delta ^ { * }$ be the restriction of $\pi$ . Then $R ^ { 2 } \rho _ { * } \mathbb { Z } / ( \mathrm { t o r s i o n } )$ is a local system with unipotent monodromy $T$ , which we denote by $\mathcal { H }$ . Let $N = \log T$ . Note that the pullback of $\mathcal { H }$ is trivialized by the choice of a point $t _ { 0 } \in \Delta ^ { * }$ : $\nu ^ { * } { \mathcal { H } }$ is isomorphic to the constant sheaf with fiber $\overline { { H } } ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { Z } )$ .

The associated flat vector bundle $\mathcal { H } \otimes _ { \mathbb { Z } } \mathcal { O } _ { \Delta ^ { * } }$ has the canonical extension $\mathcal { H }$ of Deligne [4]: $\mathcal { H }$ can be taken to be the trivial holomorphic vector bundle $\overline { { { H } } } ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { Z } ) \otimes _ { \mathbb { Z } } \mathcal { O } _ { \Delta } = H ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { C } ) \otimes _ { \mathbb { C } } \mathcal { O } _ { \Delta }$ , with the connection $D = - { \frac { N } { 2 \pi { \sqrt { - 1 } } } } { \frac { d t } { t } }$ A (local) flat section over $\Delta ^ { * }$ is then a section locally of the form $e ^ { z N } v$ , for $v \in H ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { C } )$ . In particular, we see that:

Proposition 6.1. Let s be a holomorphic section s of $\mathcal { H } \otimes _ { \mathbb { Z } } \mathcal { O } _ { \Delta ^ { * } }$ . Then s extends to a holomorphic section of $\overline { { \mathcal { H } } }$ if and only if, writing $\nu ^ { * } s$ as a holomorphic function on $\widetilde { \Delta } ^ { * }$ with values in $H ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { C } )$ , the function $e ^ { - z N } \nu ^ { * } s$ , viewed as a function on $\Delta ^ { * }$ , extends to $a$ (singlevalued) holomorphic function on $\Delta$ with values in $H ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { C } )$ . q.e.d.

On the other hand, by [35] (see also [4], [31]), the canonical extension $\mathcal { H }$ is also given by $\mathbb { R } ^ { 2 } \pi _ { * } \Lambda _ { y / \Delta } ^ { * } ( \log \mathcal { D } )$ . By Corollary 2.22, the subsheaf

$R ^ { 0 } \pi _ { * } \omega _ { \mathcal { V } / \Delta } ( \log \mathcal { D } )$ is a rank one subbundle of $\mathbb { R } ^ { 2 } \pi _ { * } \Lambda _ { y / \Delta } ^ { * } ( \log { \mathcal { D } } )$ . An easy argument shows that, for $\phi _ { t } \in H ^ { 0 } ( Y _ { t } ; \omega _ { Y _ { t } } ( D _ { t } ) )$ , if $\phi _ { t } \neq 0$ , then $\int _ { \gamma } \phi _ { t } \neq 0$ (including the case $t = 0$ ). We uniquely define an everywhere generating holomorphic section $\omega ( t )$ of $R ^ { 0 } \pi _ { * } \omega _ { \mathcal { V } / \Delta } ( \log \mathcal { D } )$ by the requirement that

$$
\int _ { \gamma } \omega ( t ) = 1 { \mathrm { ~ f o r ~ a l l ~ } } t \in \Delta \ .
$$

Now fix an integral splitting of the exact sequence

$$
0 \to \Lambda ^ { \vee } \to \overline { { { H } } } ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { Z } ) \to \mathbb { Z } \to 0 ,
$$

so that every element of $\overline { { H } } ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { C } )$ is uniquely written as $a \hat { \gamma } + \beta$ , where $\hat { \gamma } \in \overline { { H } } ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { Z } )$ maps to the (oriented) generator of $\mathbb { Z }$ and $\beta \in \Lambda _ { \mathbb { C } } ^ { \vee } = \Lambda _ { \mathbb { C } }$ . Note that, for $\overline { { H } } ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { Z } )$ , $N ( \xi ) = \xi ( \gamma ) \lambda$ , and in particular $N ( \hat { \gamma } ) = \lambda$ , where we identify $\lambda$ with its Poincar´e dual.
With our choice of $\omega ( t )$ , we can write

$$
\omega ( t ) = \hat { \gamma } + \beta ( t ) ,
$$

where $\beta ( t )$ is a multi-valued section of $\Lambda _ { \mathbb { C } }$ . By Proposition 6.1, the section $e ^ { - z N } \omega ( t )$ extends to a single-valued holomorphic function on $\Delta$ with values in $H ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { C } )$ . As

$$
e ^ { - z N } ( \xi ) = \xi - z \xi ( \gamma ) \lambda ,
$$

we see that

$$
e ^ { - z N } ( \omega ( t ) ) = \hat { \gamma } + \beta ( t ) - z \lambda = f ( t ) .
$$

where $f ( t )$ is a single valued holomorphic function on $\Delta ^ { * }$ with values in $H ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { C } )$ which extends to a holomorphic function on $\Delta$ .

Thus $\omega ( t ) = z \lambda + f ( t )$ , or equivalently:

Proposition 6.2. $\omega ( t ) = \frac { \log t } { 2 \pi \sqrt { - 1 } } \lambda + f ( t )$ , where $f ( t ) \in H ^ { 2 } ( Y _ { t _ { 0 } } -$ $D ; \mathbb { C } )$ and $f$ is holomorphic at $0$ . q.e.d.

We then have the following corollary, which is a partial strengthening of [27, III(2.12)]:

Corollary 6.3. The real, single-valued $C ^ { \infty }$ function $\operatorname { I m } \omega ( t ) = \operatorname { I m } \beta ( t )$ with values in $\Lambda _ { \mathbb { R } }$ satisfies: for $| t | \ll 1$ , ${ \mathrm { I m } } \omega ( t ) \in { \mathcal { C } } ^ { + }$ , and in fact $\operatorname { I m } \omega ( t )$ is in $\boldsymbol { B } _ { \mathrm { g e n } }$ .

Proof.
We have

$$
\mathrm { I m } \omega ( t ) = - { \frac { \log | t | } { 2 \pi } } \lambda + g ( t ) = \left( - { \frac { \log | t | } { 2 \pi } } \right) \left( \lambda - { \frac { 2 \pi g ( t ) } { \log | t | } } \right) ,
$$

where $g \colon \Delta  H ^ { 2 } ( Y _ { t _ { 0 } } { - } D ; \mathbb { R } )$ is a $C ^ { \infty }$ function.
The function $- \log | t | / 2 \pi$ is positive and tends to $+ \infty$ when $t  0$ , and hence $2 \pi g ( t ) / \log | t |$ extends to a continuous function on $\Delta$ with $\begin{array} { r } { \operatorname* { l i m } _ { t \to 0 } 2 \pi g ( t ) / \log | t | = 0 } \end{array}$ .

Thus $( \operatorname { I m } \omega ( t ) ) ^ { 2 } > 0$ for all $| t | \ll 1$ . With our sign conventions, it follows that ${ \mathrm { I m } } \omega ( t ) \in { \mathcal { C } } ^ { + }$ . Moreover, $\begin{array} { r } { \operatorname* { l i m } _ { t  0 } ( \lambda - 2 \pi g ( t ) / \log | t | ) = \lambda } \end{array}$ . Since $\boldsymbol { B } _ { \mathrm { g e n } }$ is open in $\Lambda _ { \mathbb { R } }$ , for $| t | \ll | t _ { 0 } |$ , $\lambda - 2 \pi g ( t ) / \log | t | \in B _ { \mathrm { g e n } }$ . Thus, for $| t | \ll | t _ { 0 } |$ , $\operatorname { I m } \omega ( t ) \in B _ { \mathrm { g e n } }$ . q.e.d.

Remark 6.4. There is a several variable version of the above.
The poldisk $\Delta ^ { k }$ has $k$ boundary components, defined by $t _ { i } = 0$ , where $t _ { i }$ is the coordinate on the $i ^ { \mathrm { t h } }$ factor.
Given $\pi \colon \mathcal { V }  \Delta ^ { k }$ , such that the generic fiber over each boundary component is $d$ -semistable, there is an associated monodromy transformation $T _ { i }$ with $N _ { i } = \log T _ { i }$ and $N _ { i } ( x ) =$ $- ( x \bullet \lambda _ { i } ) \gamma$ . Then the period $\omega ( t _ { 1 } , \ldots , t _ { k } )$ has the form

$$
\omega ( t _ { 1 } , \ldots , t _ { k } ) = \sum _ { i = 1 } ^ { k } { \frac { \log t _ { i } } { 2 \pi { \sqrt { - 1 } } } } \lambda _ { i } + f ( t _ { 1 } , \ldots , t _ { k } ) ,
$$

where $f \colon \Delta ^ { k } \to H ^ { 2 } ( Y _ { t _ { 0 } } - D ; \mathbb { C } )$ is holomorphic.

By applying semistable reduction to a one parameter family over a disk $\Delta \subseteq \Delta ^ { k }$ which has order of contact $n _ { i }$ with the $i ^ { \mathrm { t h } }$ component of the boundary, it follows that, for all $n _ { i } \in \mathbb { Z }$ , $n _ { i } > 0$ , we have $\begin{array} { r } { ( \sum _ { i } n _ { i } \lambda _ { i } ) ^ { 2 } > 0 } \end{array}$ . This easily implies that, for $i \neq j$ , $\lambda _ { i } \cdot \lambda _ { j } > 0$ , and hence either $\lambda _ { i } \in \mathcal { C } ^ { + }$ for all $i$ or $- \lambda _ { i } \in \mathcal { C } ^ { + }$ for all $i$ . Choosing orientations so that $\lambda _ { i } \in \mathcal { C } ^ { + }$ for all $i$ , it follows that, if $| t _ { i } | \ll 1$ for every $i$ , then $\operatorname { I m } \omega ( t _ { 1 } , \dots , t _ { k } ) \in { \mathcal { B } } _ { \mathrm { g e n } }$ .

# 7. The differential of the period map

We begin by discussing the smooth case, using [9] as a general reference.
Let $( Y , D )$ be an anticanonical pair (with a fixed orientation of $D$ ). For notational simplicity, we assume that each component of $D$ is smooth, i.e. that $r > 1$ ; minor modifications handle the case $r = 1$ . The period homomorphism is the homomorphism $\varphi _ { Y } \colon \Lambda \to \mathbb { C } ^ { * }$ defined by: if $\alpha \in \Lambda$ and $L _ { \alpha }$ is the corresponding line bundle, then $\varphi _ { Y } ( \alpha ) = L _ { \alpha } \big \rvert _ { D } \in$ $\operatorname { P i c } ^ { 0 } D \cong \mathbb { C } ^ { * }$ , and the period map is the map $Y \mapsto \varphi _ { Y } \in { \mathrm { H o m } } ( \Lambda , \mathbb { C } ^ { * } )$ . The period map is holomorphic: for a fixed $\alpha \in \Lambda$ , given a family $( \mathcal { F } , \mathcal { D } )$ of pairs over $S$ , after shrinking $S$ we can assume that $L _ { \alpha }$ extends to a holomorphic line bundle $\mathcal { L } _ { \alpha }$ over $\mathcal { F }$ and that ${ \mathcal { D } } \cong S \times D$ . The line bundle $\mathcal { L } _ { \boldsymbol { \alpha } } | _ { \mathcal { D } } \cong S \times D$ then defines a holomorphic map from $S$ to $\mathrm { P i c } ^ { 0 } D$ , and fitting these together for each $\alpha$ defines the period map as a holomorphic map $S \to \operatorname { H o m } ( \Lambda , \mathbb { C } ^ { * } )$ . The relationship between this period map and that considered in the previous section is as follows [9, (3.12)]:

$$
\varphi _ { Y } ( \alpha ) = \exp \left( 2 \pi { \sqrt { - 1 } } \int _ { \alpha } \omega \right) .
$$

The differential of the period map (for the semi-universal family) is then a map

$$
\begin{array} { r } { \psi \colon H ^ { 1 } ( Y ; T _ { Y } ( - \log D ) ) \to \mathrm { H o m } ( \Lambda , H ^ { 1 } ( D ; \mathcal { O } _ { D } ) ) = } \\ { \mathrm { H o m } _ { \mathbb { C } } ( \Lambda _ { \mathbb { C } } , H ^ { 1 } ( D ; \mathcal { O } _ { D } ) ) . } \end{array}
$$

We would like to describe the map $\psi$ . A local calculation shows:

Lemma 7.1. Let $\begin{array} { r } { \nu \colon \widetilde { D } = \coprod _ { i } D _ { i } \to Y } \end{array}$ be the composition of normalization and inclusion.
Then there is an exact sequence

$$
0 \to \Omega _ { Y } ^ { 1 } ( \log D ) ( - D ) \to \Omega _ { Y } ^ { 1 } \to \nu _ { * } \Omega _ { \widetilde { D } } ^ { 1 } \to 0 .
$$

Given a line bundle $L$ on $Y$ such that $\deg ( L | _ { D _ { i } } ) = 0$ for every $i$ , its Chern class $c _ { 1 } ( L ) \in H ^ { 1 } ( Y ; \Omega _ { Y } ^ { 1 } )$ i and its image in $\oplus _ { i } H ^ { 1 } ( D _ { i } ; \Omega _ { D _ { i } } ^ { 1 } )$ is zero.
Thus, from the exact sequence

$$
\begin{array} { r l } & { 0 = \bigoplus _ { i } H ^ { 0 } ( D _ { i } ; \Omega _ { D _ { i } } ^ { 1 } ) \to H ^ { 1 } ( Y ; \Omega _ { Y } ^ { 1 } ( \log D ) ( - D ) ) \to H ^ { 1 } ( Y ; \Omega _ { Y } ^ { 1 } ) \to } \\ & { \qquad \bigoplus _ { i } H ^ { 1 } ( D _ { i } ; \Omega _ { D _ { i } } ^ { 1 } ) , } \end{array}
$$

we see that $c _ { 1 } ( L )$ lifts to a unique element of $H ^ { 1 } ( Y ; \Omega _ { Y } ^ { 1 } ( \log D ) ( - D ) )$ , which we denote by $\hat { c } _ { 1 } ( L )$ . Note that $H ^ { 1 } ( Y ; \Omega _ { Y } ^ { 1 } ( \log D ) ( - D ) ) \cong \Lambda _ { \mathbb { C } }$ and we can think of $\hat { c } _ { 1 } ( L )$ as a Chern class with values in $\Lambda _ { \mathbb { C } }$ . The differential $\psi$ of the period map is then described as follows:

Theorem 7.2. Let $\partial \colon H ^ { 1 } ( D ; \mathcal { O } _ { D } ) \to H ^ { 2 } ( Y ; \mathcal { O } _ { Y } ( - D ) )$ be the coboundary map arising from the exact sequence

$$
0 \to { \mathcal { O } } _ { Y } ( - D ) \to { \mathcal { O } } _ { Y } \to { \mathcal { O } } _ { D } \to 0 ,
$$

which is an isomorphism since ${ \cal H } ^ { 1 } ( Y ; \mathcal { O } _ { Y } ) = { \cal H } ^ { 2 } ( Y ; \mathcal { O } _ { Y } ) = 0$ . Then

$$
\partial \circ \psi ( \theta ) ( \alpha ) = \theta \smile \hat { c } _ { 1 } ( L _ { \alpha } ) .
$$

where $\smile$ denotes the cup product

$$
H ^ { 1 } ( Y ; T _ { Y } ( - \log D ) ) \otimes H ^ { 1 } ( Y ; \Omega _ { Y } ^ { 1 } ( \log D ) ( - D ) ) \to H ^ { 2 } ( Y ; \mathcal { O } _ { Y } ( - D ) ) .
$$

Corollary 7.3. $\psi$ is an isomorphism.

Proof.
By Theorem 7.2, $\partial \circ \psi$ is the cup product map $H ^ { 1 } ( Y ; T _ { Y } ( - \log D ) ) \to \mathrm { H o m } ( H ^ { 1 } ( Y ; \Omega _ { Y } ^ { 1 } ( \log D ) ( - D ) ) , H ^ { 2 } ( Y ; O _ { Y } ( - D ) ) ) .$ This map is an isomorphism since $\mathcal { O } _ { Y } ( - D ) = \omega _ { D }$ and by Serre duality.
q.e.d.

Remark 7.4. The vector space $H ^ { 1 } ( Y ; \Omega _ { Y } ^ { 1 } ( \log D ) ( - D ) )$ is dual to $H ^ { 1 } ( Y ; \Omega _ { Y } ^ { 1 } ( \log D ) ) \ = \ \Lambda _ { \mathbb { C } } ^ { \vee }$ . Furthermore, $\mathrm { H o m } _ { \mathbb { C } } ( \Lambda _ { \mathbb { C } } , H ^ { 2 } ( Y ; { \mathcal { O } } _ { Y } ( - D ) ) )$ is canonically isomorphic to $\mathrm { H o m } _ { \mathbb { C } } ( H ^ { 0 } ( \Omega _ { Y } ^ { 2 } ( \log D ) ) , H ^ { 1 } ( Y ; \Omega _ { Y } ^ { 1 } ( \log D ) ) )$ ). This gives the usual form of the differential of the period map, via cup product and contraction:

$$
H ^ { 1 } ( Y ; T _ { Y } ( - \log D ) ) \otimes H ^ { 0 } ( Y ; \Omega _ { Y } ^ { 2 } ( \log D ) ) \to H ^ { 1 } ( Y ; \Omega _ { Y } ^ { 1 } ( \log D ) ) .
$$

Proof of Theorem 7.2. The class $\theta \in H ^ { 1 } ( Y ; T _ { Y } ( - \log D ) )$ corresponds to a first order deformation $( \mathcal { Z } , \mathcal { D } ) \to \operatorname { S p e c } \mathbb { C } [ \varepsilon ]$ . Explicitly, the correspondence is as follows: For a sufficiently small open cover $\{ U _ { i } \}$ of $Y$ , there exists an isomorphism $\phi _ { i } \colon \mathcal { O } _ { \mathcal { Z } } \big | _ { U _ { i } } \cong \mathcal { O } _ { U _ { i } } \oplus \mathcal { O } _ { U _ { i } } \cdot \varepsilon$ . Moreover, on $U _ { i } \cap U _ { j }$ , $\phi _ { j } \circ \phi _ { i } ^ { - 1 } - \mathrm { I d } = \theta _ { i j }$ , where $\theta _ { i j }$ is a 1-cocycle.
The condition that we keep the normal crossings divisor $\boldsymbol { D }$ means that, in local coordinates,

$$
\theta _ { i j } = a z _ { 1 } \frac { \partial } { \partial z _ { 1 } } + b z _ { 2 } \frac { \partial } { \partial z _ { 2 } }
$$

for some holomorphic functions $a$ , $b$ , i.e. that $\theta _ { i j }$ is a section of $T _ { Y } ( - \log D )$ over $U _ { i } \cap U _ { j }$ . However, in our situation we can do a little better:

Lemma 7.5. After possibly shrinking the cover $\{ U _ { i } \}$ and modifying $\{ \theta _ { i j } \}$ by a coboundary, we can assume that $\theta _ { i j } \big | _ { D } = 0$ , i.e. that $\theta _ { i j }$ has the local form a0z1z2 ∂∂z1 $\begin{array} { r } { a ^ { \prime } z _ { 1 } z _ { 2 } \frac { \partial } { \partial z _ { 1 } } + b ^ { \prime } z _ { 1 } z _ { 2 } \frac { \partial } { \partial z _ { 2 } } } \end{array}$ for some holomorphic functions $a ^ { \prime }$ , $b ^ { \prime }$ .

Proof.
We have a commutative diagram

$$
\begin{array} { l c l } { { 0 } } & { { \longrightarrow T _ { Y } ( - \log D ) { \longrightarrow } \ : T _ { Y } \longrightarrow \bigoplus _ { i } N _ { D _ { i } / Y } { \longrightarrow } \ : 0 } } \\ { { \Big . } } & { { \Big \downarrow } } & { { \Big \downarrow } } \\ { { 0 } } & { { \longrightarrow T _ { D } \longrightarrow  T _ { Y } | _ { D } \longrightarrow  N _ { D / Y } \longrightarrow  T _ { D } ^ { 1 } \longrightarrow 0  } } \end{array}
$$

A diagram chase shows that $T _ { Y } ( - \log D ) \to T _ { D }$ is surjective.
Hence there is an exact sequence

$$
0 \to T _ { Y } ( - D ) \to T _ { Y } ( - \log D ) \to T _ { D } \to 0 .
$$

But an easy calculation gives $H ^ { 1 } ( D ; T _ { D } ) = 0$ (i.e. every locally trivial deformation of $D$ is a product).
Thus the natural map $H ^ { 1 } ( Y ; T _ { Y } ( - D ) ) $ $H ^ { 1 } ( Y ; T _ { Y } ( - \log D ) )$ is surjective, which is the statement of the lemma.
q.e.d.

Returning to the proof of Theorem 7.2, fix once and for all a representative $\{ \theta _ { i j } \}$ for $\theta$ satisfying the conclusion of the lemma.
We have the usual exact sequence

$$
0 \to { \mathcal O } _ { Y } \to { \mathcal O } _ { \mathcal Z } ^ { * } \to { \mathcal O } _ { Y } ^ { * } \to 0 ,
$$

and hence $\operatorname { P i c } \mathcal { Z } \cong \operatorname { P i c } Y$ since ${ \cal H } ^ { 1 } ( Y ; { \mathcal O } _ { Y } ) = { \cal H } ^ { 2 } ( Y ; { \mathcal O } _ { Y } ) = 0$ . Hence, given a line bundle $L$ on $Y$ , $L$ lifts uniquely to a line bundle $\mathcal { L }$ on $\mathcal { Z }$ , which we see explicitly as follows: Every lifting $\tilde { \lambda } _ { i j }$ of $\lambda _ { i j }$ to an element of ${ \mathcal { O } } _ { \mathcal { Z } } ^ { * } | U _ { i }$ is necessarily of the form $\phi _ { i } ^ { - 1 } ( \lambda _ { i j } + \mu _ { i j } \varepsilon )$ for some holomorphic functions $\mu _ { i j }$ . The condition that $\tilde { \lambda } _ { i j }$ can be chosen to be a 1-cocycle is the equality

$$
\frac { \theta _ { j i } ( \lambda _ { j k } ) } { \lambda _ { j k } } = \lambda _ { i j } ^ { - 1 } \mu _ { i j } - \lambda _ { j k } ^ { - 1 } \mu _ { j k } + \lambda _ { i k } ^ { - 1 } \mu _ { i k } = \delta ( \{ \rho _ { i j } \} ) ,
$$

where $\rho _ { i j }$ is the 1-cochain $\lambda _ { i j } ^ { - 1 } \mu _ { i j }$ and $\delta$ here and for the rest of the proof denotes $\check { \mathrm { C } }$ ech coboundary.
In other words, the 2-cocycle $\theta \smile d \log \lambda _ { i j } =$ $\theta \smile c _ { 1 } ( L )$ is zero in $H ^ { 2 } ( Y ; { \mathcal { O } } _ { Y } )$ . In this case, the transition functions

$$
\tilde { \lambda } _ { i j } \phi _ { i } ^ { - 1 } ( \lambda _ { i j } ( 1 + \rho _ { i j } \varepsilon ) )
$$

define the lift of $L$ to $\mathcal { L }$ . Moreover, $\rho _ { i j } \big | _ { D }$ is then a 1-cocycle since

$$
\delta ( \left\{ \rho _ { i j } \right\} \big | _ { D } ) = \frac { \theta _ { j i } ( \lambda _ { j k } ) } { \lambda _ { j k } } \big | _ { D } = 0 ,
$$

and, in case $L \ = \ L _ { \alpha }$ for $\alpha \in \Lambda$ , then $\rho _ { i j } \big | _ { D }$ represents the element $\psi ( \theta ) ( \alpha ) \in H ^ { 1 } ( D ; { \mathcal { O } } _ { D } )$ .

We compute $\partial \circ \psi ( \theta ) ( \alpha )$ by lifting to a 1-cochain with values in $\mathcal { O } _ { Y }$ and taking its $\check { \mathrm { C } }$ ech coboundary.
Clearly, $\rho _ { i j }$ is such a lift, and thus $\partial \circ \psi ( \theta ) ( \alpha )$ is represented by the 2-cocycle $\theta _ { j i } ( \lambda _ { j k } ) / \lambda _ { j k }$ .

Finally we compute the term $\theta \sim \hat { c } _ { 1 } ( L )$ . We can write

$$
\frac { d \lambda _ { i j } } { \lambda _ { i j } } = \eta _ { i j } + ( \delta \{ \sigma _ { i } \} ) _ { i j } ,
$$

where $\eta _ { i j }$ is a 1-cocycle with values in $\Omega _ { Y } ^ { 1 } ( \log D ) ( - D )$ representing $\hat { c } _ { 1 } ( L )$ and $\sigma _ { i }$ is a 0-cochain with values in $\Omega _ { Y } ^ { 1 }$ . Thus $\theta \sim \hat { c } _ { 1 } ( L )$ is represented by the 1-cocycle

$$
\frac { \theta _ { j i } ( \lambda _ { j k } ) } { \lambda _ { j k } } - \theta _ { j i } ( \delta \{ \sigma _ { i } \} ) _ { j k } .
$$

But, since $\delta \theta = 0$ ,

$$
\theta _ { j i } ( \delta \{ \sigma _ { i } \} ) _ { j k } = \theta \smile \delta \{ \sigma _ { i } \} = \pm \delta ( \theta \smile \{ \sigma _ { i } \} ) .
$$

Since $\theta _ { i j }$ vanishes on $D$ , $\delta ( \boldsymbol { \theta } \sim \{ \sigma _ { i } \} )$ is a 1-coboundary with coefficients in $\mathcal { O } _ { Y } ( - D )$ . Thus, in cohomology, $\partial \circ \psi ( \theta ) ( \alpha ) = \theta \smile \hat { c } _ { 1 } ( L _ { \alpha } )$ as claimed.

We turn now to the case of a Type III degeneration $Y _ { 0 }$ . We define $\Lambda _ { 0 }$ and $\Lambda _ { 0 } ^ { \vee }$ by analogy with the smooth case:

$$
\begin{array} { r l } & { \Lambda _ { 0 } = \{ L \in \mathrm { P i c } Y _ { 0 } : \deg ( L \big | _ { D _ { i } } ) = 0 \mathrm { ~ f o r ~ a l l ~ } i \} ; } \\ & { \Lambda _ { 0 } ^ { \vee } = \mathrm { P i c } Y _ { 0 } / \bigoplus _ { i } \mathbb { Z } [ D _ { i } ] . } \end{array}
$$

Note that, by Lemma 2.20,

$$
( \Lambda _ { 0 } ) _ { \mathbb { C } } ^ { \vee } \cong H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ) .
$$

Lemma 7.6. $( \Lambda _ { 0 } ) _ { \mathbb { C } } \cong H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ( - D ) ) .$

Proof.
We have the analogue of the exact sequence of Lemma 7.1:

$$
0 \to \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ( - D ) \to \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } \to \nu _ { * } \Omega _ { \widetilde { D } } ^ { 1 } \to 0 .
$$

Thus there is an exact sequence

$$
0 \to H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ( - D ) ) \to H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) \to \bigoplus _ { i } H ^ { 1 } ( D _ { i } ; \Omega _ { D _ { i } } ^ { 1 } ) .
$$

This identifies $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ( - D ) )$ with the kernel of

$H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } ) \cong H ^ { 2 } ( Y _ { 0 } ; \mathbb { C } )  \bigoplus _ { i } H ^ { 1 } ( D _ { i } ; \Omega _ { D _ { i } } ^ { 1 } ) \cong \bigoplus _ { i } H ^ { 2 } ( D _ { i } ; \mathbb { C } ) .$ which is $( \Lambda _ { 0 } ) _ { \mathbb { C } }$ . q.e.d.

There is a period homomorphism $\varphi _ { Y _ { 0 } } \in \mathrm { H o m } ( \Lambda _ { 0 } , \mathbb { C } ^ { * } )$ and it extends to a holomorphic map on germs of deformations of $Y _ { 0 }$ . In particular, there is a well-defined differential

$$
\psi \colon \mathbb { T } _ { Y _ { 0 } } ^ { 1 } \bigl ( - \log D \bigr ) \to \mathrm { H o m } _ { \mathbb { C } } \bigl ( \bigl ( \Lambda _ { 0 } \bigr ) _ { \mathbb { C } } , H ^ { 1 } \bigl ( \mathcal { O } _ { D } \bigr ) \bigr ) .
$$

To compute it, note first that the analogue of Lemma 7.1 holds, so that given $L \in \Lambda _ { 0 }$ , we have $\hat { c } _ { 1 } ( L ) \in H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) ( - D ) )$ and its image $\bar { c } _ { 1 } ( L ) \in H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ( - D ) )$ . Then we have

Theorem 7.7. Let $\partial \colon H ^ { 1 } ( D ; \mathcal { O } _ { D } )  H ^ { 2 } ( Y _ { 0 } ; \mathcal { O } _ { Y _ { 0 } } ( - D ) )$ be the coboundary map arising from the exact sequence

$$
0 \to { \mathcal { O } } _ { Y _ { 0 } } ( - D ) \to { \mathcal { O } } _ { Y _ { 0 } } \to { \mathcal { O } } _ { D } \to 0 ,
$$

which is an isomorphism since $H ^ { 1 } ( Y _ { 0 } ; { \mathcal { O } } _ { Y _ { 0 } } ) = H ^ { 2 } ( Y _ { 0 } ; { \mathcal { O } } _ { Y _ { 0 } } ) = 0$ . Then

$$
\partial \circ \psi ( \theta ) ( L ) = \langle \theta , \hat { c } _ { 1 } ( L ) \rangle ,
$$

where $\langle \cdot , \cdot \rangle$ denotes Yoneda pairing

$$
\mathrm { E x t } ^ { 1 } ( \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) , \mathcal { O } _ { Y _ { 0 } } ) \otimes H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) ( - D ) )  H ^ { 2 } ( Y _ { 0 } ; \mathcal { O } _ { Y _ { 0 } } ( - D ) )
$$

Proof.
On the hyperplane $H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) )$ of $\mathbb { T } _ { Y _ { 0 } } ^ { 1 } ( - \log D )$ , the Yoneda product is just cup product, and the proof is exactly the same as the proof for Theorem 7.2. By linearity, it suffices to prove the formula of Theorem 7.7 for a single class $\theta$ projecting onto a nonzero element of $H ^ { 0 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } ) \cong \mathbb { C }$ . Fix a one parameter smoothing $\pi \colon ( \mathcal { V } , \mathcal { D } ) $ $\Delta$ . There are relative versions $\mathbb { T } _ { \mathcal { Y } / \Delta } ^ { 1 } ( - \log \mathcal { D } ) , R ^ { 1 } \pi _ { * } \Omega _ { \mathcal { Y } / \Delta } ^ { 1 } ( \log \mathcal { D } ) ( - \mathcal { D } )$ , $R ^ { 1 } \pi _ { * } \mathcal { O } _ { \mathcal { D } }$ , $R ^ { 2 } \pi _ { * } \mathcal { O } y ( - \mathcal { D } )$ . We also have the relative Kodaira-Spencer map $\kappa \colon T _ { \Delta }  \mathbb { T } _ { y / \Delta } ^ { 1 } ( - \log { \mathcal { D } } )$ , and $\kappa ( \partial / \partial t )$ is a section which restricts to an element $\theta$ with nonzero image in $H ^ { 0 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ^ { 1 } )$ . Given $L \in \operatorname { P i c } Y _ { 0 }$ , we can lift $L$ to a line bundle $\mathcal { L } \in \mathrm { P i c } \mathcal { y }$ , and there is a relative (modified) Chern class $\hat { c } _ { 1 } ( \mathcal { L } ) \in R ^ { 1 } \pi _ { * } \Omega _ { y / \Delta } ^ { 1 } ( \log \mathcal { D } ) ( - \mathcal { D } )$ . We want to establish the equality

$$
\partial \circ \psi ( \kappa ( \partial / \partial t ) ) ( \mathcal { L } ) = \langle \kappa ( \partial / \partial t ) , \hat { c } _ { 1 } ( \mathcal { L } ) \rangle .
$$

This holds for a general $t$ by Theorem 7.2, and thus follows by continuity for $t ~ = ~ 0$ , noting that $R ^ { 2 } \pi _ { * } \mathcal { O } _ { \mathcal { V } } ( - \mathcal { D } ) \cong \mathcal { O } _ { \Delta }$ is torsion free (see also Proposition 8.7 below).
Restricting to $t = 0$ gives the result for $\theta$ . q.e.d.

Remark 7.8. We will only need this result for $H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) )$ , the hyperplane tangent to the equisingular deformations.

Corollary 7.9. The restriction of the differential of the period map to $H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) )$ is an isomorphism and the differential of the period map on $\mathbb { T } _ { Y _ { 0 } } ^ { 1 } ( - \log D )$ is surjective.

Proof.
Note that $T _ { Y _ { 0 } } = H o m ( \Omega _ { Y _ { 0 } } ^ { 1 } , \mathcal { O } _ { Y _ { 0 } } ) = H o m ( \Omega _ { Y _ { 0 } } ^ { 1 } / \tau _ { Y _ { 0 } } ^ { 1 } , \mathcal { O } _ { Y _ { 0 } } )$ , and similarly for $T _ { Y _ { 0 } } ( - \log D )$ . Thus there is the cup product map

$H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) ) \otimes H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ( - D ) ) \to H ^ { 2 } ( Y _ { 0 } ; \mathcal O _ { Y _ { 0 } } ( - D ) ) ,$ which is identified via $\partial ^ { - 1 }$ with

$$
H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) ) \otimes ( \Lambda _ { 0 } ) _ { \mathbb { C } } \to H ^ { 1 } ( D ; { \mathcal { O } } _ { D } ) ,
$$

the differential of the period map.
By [6, (2.10)], the vector spaces $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ( - D ) )$ and $H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) )$ are dual under cup product, hence the above cup product is nondegenerate by Serre duality.
Moreover by compatibility of cup product,

$$
\langle \theta , { \hat { c } } _ { 1 } ( L ) \rangle = \langle \theta , { \bar { c } } _ { 1 } ( L ) \rangle ,
$$

where $\bar { c } _ { 1 } ( L ) \ \in \ H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ( - D ) )$ is the image of $\hat { c } _ { 1 } ( L ) \ \in$ $H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) ( - D ) )$ . This proves the first statement and the second then follows.
q.e.d.

# 8. Surjectivity of the period map

In this section, our goal is to use Theorem 7.7 to prove results about the surjectivity of the period map for families of $d$ -semistable Type III anticanonical pairs, and then to apply this to construct Type III degenerations $y  \Delta$ such that the kernel of the period map on a general fiber $Y _ { t }$ is of a special type.

Let $( Y _ { 0 } , D _ { 0 } )$ be a Type III anticanonical pair as defined in Definition 2.1. If $Y _ { 0 }$ is the central fiber of a Type III degeneration $\pi \colon \mathcal { V }  \Delta$ of anticanonical pairs, which is the case if and only if $Y _ { 0 }$ is $d$ -semistable, then there are $f$ line bundles on $Y _ { 0 }$ , namely $\mathcal { O } y ( V _ { i } ) \big | _ { Y _ { 0 } }$ , $i = 0 , \ldots , f - 1$ . By Lemma 2.16,

$$
\mathrm { P i c } Y _ { 0 } = H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } ) \cong \mathrm { K e r } \left( \bigoplus _ { i } H ^ { 2 } ( V _ { i } ; \mathbb { Z } ) \to \bigoplus _ { i < j } H ^ { 2 } ( C _ { i j } ; \mathbb { Z } ) \right) .
$$

Define a class $\xi _ { \ell } \in \bigoplus _ { i } H ^ { 2 } ( V _ { i } ; \mathbb { Z } )$ by the rule:

$$
\left. \xi \ell \right. _ { V _ { i } } = \left\{ \begin{array} { l l } { [ C _ { i \ell } ] , } & { \mathrm { i f ~ } i \neq \ell ; } \\ { - \sum _ { j \neq \ell } [ C _ { j \ell } ] = - [ C _ { \ell } ] , } & { \mathrm { i f ~ } i = \ell . } \end{array} \right.
$$

By the triple point formula, $\xi _ { \ell } \in \operatorname { K e r } ( \bigoplus _ { i } H ^ { 2 } ( V _ { i } ; \mathbb { Z } ) \to \bigoplus _ { i < j } H ^ { 2 } ( C _ { i j } ; \mathbb { Z } ) )$ , and hence $\xi _ { 0 } , \ldots , \xi _ { f - 1 } \in H ^ { : 2 } ( Y _ { 0 } ; \mathbb { Z } ) \cong \operatorname { P i c } Y _ { 0 }$ . It is easy to check that $\textstyle \sum _ { i } \xi _ { i } = 0$ . Clearly $\boldsymbol { \xi } _ { i } \boldsymbol { \cdot } [ D _ { j } ] = 0$ for every component $D _ { j }$ of $D$ .

Lemma 8.1. The homomorphism $\psi \colon \mathbb { Z } ^ { f } \to H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } )$ defined by

$$
( n _ { 0 } , \ldots , n _ { f - 1 } ) \mapsto \sum _ { i } n _ { i } \xi _ { i }
$$

has kernel $\{ ( n , \dots , n ) \ \in \ \mathbb { Z } ^ { f } \ : \ n \in \ \mathbb { Z } \}$ and thus defines an injective homomorphism $\mathbb { Z } ^ { f } / \mathbb { Z } \ \to \ H ^ { 2 } ( Y _ { 0 } ; \mathbb { Z } )$ . Moreover, the cokernel of $\psi$ is torsion free.

Proof.
Suppose that $( n _ { 0 } , \ldots , n _ { f - 1 } )$ is in the kernel.
After adding the element $( - n _ { 0 } , \ldots , - n _ { 0 } )$ , we may assume that $n _ { 0 } = 0$ and must show that $n _ { i } = 0$ for all $i$ . We have $\begin{array} { r } { \sum _ { V _ { i } \cap V _ { 0 } \neq \emptyset } n _ { i } [ C _ { 0 i } ] = 0 } \end{array}$ in $H ^ { 2 } ( V _ { 0 } ; \mathbb { Z } )$ . As the classes $[ C _ { 0 i } ]$ are linearly independent in $H ^ { 2 } ( V _ { 0 } ; \mathbb { Z } )$ , $n _ { i } = 0$ for all $i$ such that $V _ { i } \cap V _ { 0 } \neq \emptyset$ . Fix one such component $V _ { i }$ . Then there exists a component $V _ { j }$ such that $V _ { 0 } \cap V _ { i } \cap V _ { j } \neq \emptyset$ , corresponding to a triple point of $Y _ { 0 }$ lying on $C _ { 0 i }$ . By assumption, $\begin{array} { r } { \sum _ { V _ { i } \cap V _ { \ell } \neq \emptyset } n _ { \ell } | C _ { i \ell } | = 0 } \end{array}$ in $H ^ { 2 } ( V _ { i } ; \mathbb { Z } )$ , and $n _ { 0 } = n _ { i } = n _ { j } = 0$ . An easy argument (cf.
[9, 2.8]) shows that, if $( Y , D )$ is an anticanonical pair and $D _ { 1 } , \ldots , D _ { r - 2 }$ is a chain of length $r - 2$ , i.e. $D _ { i } \cdot D _ { i + 1 } = 1$ , $1 \leq i \leq r - 3$ , then the classes $[ D _ { 1 } ] , \ldots , [ D _ { r - 2 } ]$ are linearly independent in $H ^ { 2 } ( Y ; \mathbb { Z } )$ . Applying this fact to the pair $( V _ { i } , C _ { i } )$ , it follows that $n \ell = 0$ for all $\ell$ such that $V _ { \ell } \cap V _ { i } \neq \emptyset$ . Continuing in this way and using the fact that the dual complex of $Y _ { 0 }$ is connected, a straightforward argument then shows that $n _ { i } = 0$ for all $i$ .

Finally, we must show that Coker $\psi$ is torsion free.
This statement is invariant under a locally trivial deformation, so we can assume that $Y _ { 0 }$ is $d$ -semistable by [10, (2.16)], and that $\pi \colon \mathcal { V }  \Delta$ is a smoothing.
Thus $\xi _ { i } = \mathcal { O } _ { \mathcal { V } } ( V _ { i } ) \big | _ { Y _ { 0 } }$ as described above.
The proof of (i) of Proposition 3.9 shows that there is an inclusion of ${ \mathrm { C o k e r } } \psi$ in $H ^ { 2 } ( Y _ { t } ; \mathbb { Z } )$ for a general fiber $Y _ { t }$ . Hence ${ \mathrm { C o k e r } } \psi$ is torsion free.
q.e.d.

We next define the period map for $d$ -semistable Type III anticanonical pairs:

Definition 8.2. Let $\overline { { \Lambda } } _ { 0 }$ be the lattice defined by

Note that the condition $\alpha \cdot [ D _ { i } ] = 0$ is well-defined since $\xi _ { \ell } { \cdot } [ D _ { i } ] = 0$ for all $\ell$ and $i$ . By the proof of Lemma 8.1, if $Y _ { 0 }$ is $d$ -semistable and $\pi \colon \mathcal { V }  \Delta$ is a smoothing, then there is an inclusion of $\overline { { \Lambda } } _ { 0 }$ in $\Lambda = \Lambda ( Y _ { t } , D )$ for a general fiber $Y _ { t }$ .

For a Type III anticanonical pair $( Y _ { 0 } , D )$ , with $D$ oriented, we have the period map $\varphi _ { Y _ { 0 } } \colon \Lambda _ { 0 } \to \mathbb { C } ^ { * }$ defined by $L \in \operatorname { P i c } Y _ { 0 } \mapsto L { \big | } _ { D }$ . If $Y _ { 0 }$ is $d$ -semistable, then clearly $\varphi _ { Y _ { 0 } } ( \xi _ { i } ) = 1$ for every $i$ . We define $\bar { \varphi } _ { Y _ { 0 } } \colon \overline { { \Lambda } } _ { 0 } $ $\mathbb { C } ^ { * }$ to be the homomorphism induced by $\varphi _ { Y _ { 0 } }$ . Given a locally trivial deformation of the pair $( Y _ { 0 } , D )$ with trivial monodromy, over a smooth connected base $S$ , with all fibers $d$ -semistable, there exists a holomorphic map per: $S \to { \mathrm { H o m } } ( { \overline { { \Lambda } } } _ { 0 } , \mathbb { C } ^ { * } )$ in the usual way.

The following is then the main result of this section:

Theorem 8.3. Let $\bar { \varphi } \colon \overline { { \Lambda } } _ { 0 }  \mathbb { C } ^ { * }$ be a homomorphism.
Then there exists a locally trivial deformation of $Y _ { 0 }$ with trivial monodromy, over a smooth connected base $S$ which we can take to be of the form $( \mathbb { C } ^ { * } ) ^ { N }$ , such that all fibers are $d$ -semistable, and a point $s \in S$ such that, if $( Y _ { s } , D )$ is the corresponding Type III anticanonical pair, then $\varphi _ { Y _ { s } } ( \xi _ { i } ) = 1$ for all $i$ and the induced homomorphism $\overline { { \Lambda } } _ { 0 } \to \mathbb { C } ^ { * }$ is $\varphi$ .

Proof.
There are three ways that we can deform $Y _ { 0 }$ in a locally trivial way (cf.
[11, (4.3)] for more details):

1. We change the gluings $C _ { i j } \subseteq V _ { i } \cong C _ { j i } \subseteq V _ { j }$ by multiplying by $\lambda \in \mathbb { C } ^ { * }$ .
2. If $V _ { i }$ is obtained by blowing up a point $p \in C _ { i j } ^ { \mathrm { i n t } } \cong \mathbb { C } ^ { * }$ , we can deform the point $p$ to a point $p ^ { \prime } \in C _ { i j } ^ { \mathrm { i n t } }$ . (Note that a blowup at a singular point of the anticanonical divisor has no moduli.)
3. In most cases, $V _ { i }$ is obtained via iterated blowups from a minimal pair with no moduli (taut, in the terminology of [9]). In a very small number of exceptional cases ( $V _ { i } = \mathbb { F } _ { 0 }$ or $\mathbb { F } _ { 2 }$ is already minimal and the double curve on $V _ { i }$ is either irreducible nodal or has two components of self-intersection 2), the pair $( V _ { i } , C _ { i } )$ has moduli $\cong \mathbb { C } ^ { * }$ .

There is then a “universal” deformation $( \mathcal { U } , \mathcal { D } )$ of $Y _ { 0 }$ , parametrized by $T \ = \ ( \mathbb { C } ^ { * } ) ^ { M }$ , corresponding to the different possibilities (1), (2), (3) above.
Universal in this sense simply means that every locally trivial deformation of $( Y _ { 0 } , D )$ appears as a fiber.
After a translation on $T$ , we can assume that $1 \in { \mathit { I } } ^ { \prime }$ corresponds to $Y _ { 0 }$ . Furthermore, the monodromy of the family is trivial.
Finally, we can assume that there is a unique component of $\boldsymbol { u }$ isomorphic to $V _ { 0 } \times T$ .

Let $\Theta = ( Y _ { 0 } ) _ { \mathrm { s i n g } } = \cup _ { i < j } C _ { i j }$ be the double curve on $Y _ { 0 }$ . Then it is easy to check that $\Theta$ is rigid under locally trivial deformations and that $\operatorname { P i c } ^ { 0 } \Theta \cong ( \mathbb { C } ^ { * } ) ^ { f - 1 }$ . Furthermore, if $\mathrm { A u t } ^ { 0 } \Theta$ denotes the neutral component of $\operatorname { A u t } \Theta$ , then $\operatorname { A u t } ^ { 0 } \Theta \cong ( \mathbb { C } ^ { * } ) ^ { e }$ . Since $H _ { \mathrm { e t } } ^ { 1 } ( T , \mathbb { G } _ { m } ) = 0$ , $H _ { \mathrm { e t } } ^ { 1 } ( T , \mathrm { A u t } ^ { 0 } \Theta ) = 0$ as well, and thus we can choose an isomorphism of schemes

$$
( \mathcal { U } ) _ { \mathrm { s i n g } } \cong \Theta \times T .
$$

Since the monodromy of the family $( \mathcal { U } , \mathcal { D } ) \to T$ is trivial, there is a period map per: $T \to { \mathrm { H o m } } ( \Lambda _ { 0 } , \mathbb { C } ^ { * } )$ .

Lemma 8.4. Let $( \mathcal { U } , \mathcal { D } ) \to T$ be the deformation constructed above.
Then the period map p ${ \mathfrak { x } } \colon T \to { \mathrm { H o m } } ( \Lambda _ { 0 } , \mathbb { C } ^ { * } )$ is an affine map of tori.

Proof.
Very generally, if $\rho \colon ( \mathbb { C } ^ { * } ) ^ { N _ { 1 } } \to ( \mathbb { C } ^ { * } ) ^ { N _ { 2 } }$ is a morphism of algebraic varieties, then by a theorem of Rosenlicht $\rho$ is an affine map.
We will give an essentially direct argument that per is an affine map.
Thus, given a line bundle $L$ on $Y _ { 0 }$ , we must analyze how $L | _ { D }$ varies as we vary the gluings.

Let $\begin{array} { r } { D ^ { \prime } = \bigcup _ { i = 1 } ^ { r ^ { \prime } } D _ { i } ^ { \prime } } \end{array}$ be the dual cycle to $D$ on $V _ { 0 }$ . As previously noted, $\pi _ { 1 } ( D ^ { \prime } , * ) \cong \pi _ { 1 } ( V _ { 0 } , * ) \cong \pi _ { 1 } ( D , * )$ , and hence

$$
\begin{array} { c } { { H ^ { 1 } ( D ^ { \prime } ; \mathbb { Z } ) \cong H ^ { 1 } ( V _ { 0 } ; \mathbb { Z } ) \cong H ^ { 1 } ( D ; \mathbb { Z } ) ; } } \\ { { H ^ { 1 } ( D ^ { \prime } ; { \mathcal { O } } _ { D ^ { \prime } } ) \cong H ^ { 1 } ( V _ { 0 } ; { \mathcal { O } } _ { V _ { 0 } } ) \cong H ^ { 1 } ( D ; { \mathcal { O } } _ { D } ) . } } \end{array}
$$

Thus, an orientation on $D$ induces a compatible orientation on $D ^ { \prime }$ , and

$$
\mathrm { P i c } ^ { 0 } D ^ { \prime } \cong \mathrm { P i c } ^ { 0 } D \cong \mathrm { P i c } ^ { 0 } V _ { 0 } = H ^ { 1 } ( V _ { 0 } ; { \mathcal { O } } _ { V _ { 0 } } ^ { * } ) / H ^ { 1 } ( V _ { 0 } ; \mathbb { Z } ) .
$$

In particular, if $L ^ { \prime \prime }$ is a line bundle on $V _ { 0 }$ which restricts to a line bundle of multidegree $0$ on $D$ , then the map $\lambda \in \operatorname { P i c } ^ { 0 } V _ { 0 } \mapsto \left.
( L ^ { \prime \prime } \otimes \lambda ) \right| _ { D }$ is an affine isomorphism from $\operatorname { P i c } ^ { 0 } V _ { 0 } \cong \mathbb { C } ^ { * }$ to $\operatorname { P i c } ^ { 0 } D$ .

Choose an ordering on the components $V _ { i }$ of $Y _ { 0 }$ so that $D _ { i } ^ { \prime } = V _ { i } \cap V _ { 0 }$ , $1 \leq i \leq r ^ { \prime }$ , i.e. $D _ { i } ^ { \prime } = C _ { 0 i }$ , where the ordering of the components of $D ^ { \prime }$ is compatible with the orientation.
Let $\begin{array} { r } { Y _ { 0 } ^ { \prime } = \bigcup _ { i = 1 } ^ { f - 1 } V _ { i } } \end{array}$ . Then MayerVietoris applied to the union $Y _ { 0 } = Y _ { 0 } ^ { \prime } \cup V _ { 0 }$ implies that there is an exact sequence

$$
\{ 1 \} \to \mathrm { P i c } Y _ { 0 } \to \mathrm { P i c } Y _ { 0 } ^ { \prime } \times \mathrm { P i c } V _ { 0 } \to \mathrm { P i c } D ^ { \prime } \to \{ 1 \} ,
$$

i.e. a line bundle $L$ on $Y _ { 0 }$ is determined by line bundles $L ^ { \prime }$ on $Y _ { 0 } ^ { \prime }$ and $L ^ { \prime \prime }$ on $V _ { 0 }$ , such that $\left.
L ^ { \prime \prime } \right| _ { D ^ { \prime } } \cong \varphi ^ { * } ( L ^ { \prime } | _ { D ^ { \prime } } )$ , where $\varphi$ is the isomorphism $D ^ { \prime } \subseteq V _ { 0 } \cong D ^ { \prime } \subseteq Y _ { 0 } ^ { \prime }$ given by $Y _ { 0 }$ . Thus, if $s \in T$ , and the gluing $\varphi$ changes by $\varphi \circ \psi ( s )$ , where $\psi ( s ) \in \operatorname { A u t } ^ { 0 } D ^ { \prime }$ is given by a surjective homomorphism $\psi$ from $T$ to a subtorus of $\mathrm { A u t } ^ { 0 } D ^ { \prime }$ , then the line bundle $L$ deforms to some line bundle $L _ { s }$ corresponding to pairs $L _ { s } ^ { \prime }$ , the line bundle corresponding to $L ^ { \prime }$ over the corresponding deformation of $Y _ { 0 } ^ { \prime }$ and $L _ { s } ^ { \prime \prime } = L ^ { \prime \prime } \otimes \lambda ^ { \prime \prime } ( s )$ , with $\lambda ( s ) \in \operatorname { P i c } ^ { 0 } V _ { 0 }$ , such that

$$
\left( L ^ { \prime \prime } \otimes \lambda ^ { \prime \prime } ( s ) \right) \bigr | _ { D ^ { \prime } } \cong \psi ( s ) ^ { * } \varphi ^ { * } ( L _ { s } ^ { \prime } | _ { D ^ { \prime } } ) .
$$

If $\operatorname { A u t } ^ { 0 } D ^ { \prime } \cong ( \mathbb { C } ^ { * } ) ^ { r ^ { \prime } }$ , where the $i ^ { \mathrm { t h } }$ factor operates in the usual way on the $i ^ { \mathrm { t h } }$ component $D _ { i } ^ { \prime }$ of $D ^ { \prime }$ , then $\mathrm { A u t } ^ { 0 } D ^ { \prime }$ acts trivially on ${ \mathrm { P i c } } ^ { 0 } D ^ { \prime }$ , and $\left( z _ { 1 } , \ldots , z _ { r ^ { \prime } } \right)$ acts on $\mathrm { P i c } ^ { d _ { 1 } , \ldots , d _ { r ^ { \prime } } } D ^ { \prime }$ , the set of line bundles on $D ^ { \prime }$ of multidegree $( d _ { 1 } , \ldots , d _ { r ^ { \prime } } )$ , via $z _ { 1 } ^ { d _ { 1 } } \cdots z _ { r ^ { \prime } } ^ { d _ { r ^ { \prime } } }$ and the usual action of $\operatorname { P i c } ^ { 0 } D ^ { \prime } \cong \mathbb { C } ^ { * }$ on $\mathrm { P i c } ^ { d _ { 1 } , \ldots , d _ { r ^ { \prime } } } D ^ { \prime }$ . Given $L _ { s }$ and $\psi ( s )$ , there is a unique line bundle $\lambda ^ { \prime \prime } ( s ) \in \operatorname { P i c } ^ { 0 } V _ { 0 }$ for which the compatibility condition holds.
Thus, if we can show that $s \mapsto L _ { s } ^ { \prime } | _ { D ^ { \prime } }$ is an affine map, it follows that $s \mapsto \lambda ^ { \prime \prime } ( s )$ is affine and hence so is $\mathrm { p e r } ( s ) ( \alpha ) = \lambda ^ { \prime \prime } ( s ) | _ { D }$ , where $\alpha \in \Lambda _ { 0 }$ is the class corresponding to the line bundle $L$ .

The line bundle $L ^ { \prime }$ determines a multidegree $\mathbf { d } = ( d _ { i j } )$ , with $d _ { i j } =$ $\deg ( L ^ { \prime } | _ { C _ { i j } } )$ , and hence $d _ { i } ~ = ~ d _ { 0 i }$ , $1 \leq i \leq r ^ { \prime }$ . Restriction defines a morphism $\operatorname { P i c } ^ { \mathbf { d } } \Theta \to \operatorname { P i c } ^ { d _ { 1 } , \dots , d _ { r ^ { \prime } } } D ^ { \prime }$ , and it is equivariant with respect to the actions of $\operatorname { P i c } ^ { 0 } \Theta \cong ( \mathbb { C } ^ { * } ) ^ { f - 1 }$ on $\operatorname { P i c } ^ { \mathbf { d } } \Theta$ and $\operatorname { P i c } ^ { 0 } D ^ { \prime } \cong \mathbb { C } ^ { * }$ on $\mathrm { P i c } ^ { d _ { 1 } , \ldots , d _ { r ^ { \prime } } } D ^ { \prime }$ via the natural homomorphism $\operatorname { P i c } ^ { 0 } \Theta \to \operatorname { P i c } ^ { 0 } D ^ { \prime }$ . We now consider the various ways that the construction of Lemma 8.5 changes the line bundle $L ^ { \prime } | _ { \Theta }$ :

1. Suppose that we change the gluings $C _ { i j } \ \subseteq \ V _ { i } \cong C _ { j i } \ \subseteq \ V _ { j }$ by $\lambda \in \mathrm { A u t } C _ { i j } ^ { \mathrm { i n t } }$ . Here we may assume that $i , j \geq 1$ since we have already dealt with the gluings from $Y _ { 0 } ^ { \prime }$ to $V _ { 0 }$ . The line bundle $L ^ { \prime } | _ { \Theta }$ is then replaced by $\lambda ^ { * } ( L ^ { \prime } | _ { \Theta } )$ for the automorphism $\lambda \in \mathrm { A u t } ^ { 0 } \Theta$ corresponding to multiplying by $\lambda \in \mathbb { C } ^ { * }$ on the component $C _ { i j }$ . 2) If $V _ { i }$ is obtained by blowing up a point $p \in C _ { i j } ^ { \mathrm { i n t } } \cong \mathbb { C } ^ { * }$ , and we replace $p$ by $p ^ { \prime } \in C _ { i j } ^ { \mathrm { i n t } }$ , then the line bundle $L ^ { \prime } | _ { \Theta }$ is then replaced by $L ^ { \prime } \big | _ { \Theta } \otimes \mathcal { O } _ { \Theta } ( a ( p ^ { \prime } - p ) )$ for an appropriate integer $a$ . 3) In this exceptional case, a direct if somewhat tedious calculation shows that the corresponding map $\mathbb { C } ^ { * } \to \mathrm { P i c } ^ { \mathbf { d } } \Theta$ is affine (cf.
   [11, Lemma 4.6]). Alternatively, it is clear that the map $\mathbb { C } ^ { * } \to \mathrm { P i c } ^ { \mathbf { d } } \Theta$ is a morphism (i.e. algebraic) and hence it is affine by Rosenlicht’s theorem.

Combining the various possibilities, we see that we get an affine map from $S$ to $\mathrm { P i c } ^ { d _ { 1 } , \ldots , d _ { r ^ { \prime } } } D ^ { \prime }$ as claimed.
q.e.d.

Consider the affine map $\rho \colon T \to ( \mathbb { C } ^ { * } ) ^ { f - 1 }$ defined by

$$
\rho ( s ) = ( \varphi _ { Y _ { s } } ( \xi _ { 0 } ) , \ldots , \varphi _ { Y _ { s } } ( \xi _ { f - 1 } ) ) ,
$$

where we view the image of $\rho$ as contained in the subtorus defined by: the product of the components is 1. Let $S = ( \mathrm { K e r } \rho ) ^ { 0 }$ be the neutral component of $\operatorname { K e r } \rho$ .

Lemma 8.5. Let $( \mathcal { U } _ { S } , \mathcal { D } ) \to S$ be the restriction of the family $( \mathcal { U } , \mathcal { D } ) $ $T$ to the subtorus $S$ of $T$ . Then:

(i) For all $s \in S$ , $Y _ { s }$ is $d$ -semistable.\
(ii) The image of the Kodaira-Spencer map $T _ { S , 0 }  H ^ { 1 } ( Y _ { 0 } ; T _ { Y _ { 0 } } ( - \log D ) )$ is

$$
\{ \theta \in H ^ { 1 } ( Y _ { 0 } ; T _ { Y } ( - \log D ) ) : \theta \sim \hat { c } _ { 1 } ( \xi _ { 0 } ) = \cdot \cdot \cdot = \theta \sim \hat { c } _ { 1 } ( \xi _ { f - 1 } ) = 0 \} .
$$

Proof.
By arguments similar to the proof of Lemma 8.4, one checks that $\rho _ { 1 } \colon T \to \operatorname { P i c } ^ { 0 } \Theta \cong ( \mathbb { C } ^ { * } ) ^ { f - 1 }$ defined by $t \mapsto T _ { Y _ { t } } ^ { 1 } = E x t ^ { 1 } ( \Omega _ { Y _ { t } } ^ { 1 } , \mathcal { O } _ { Y _ { t } } )$ is an affine map and hence a homomorphism.
By definition, the locus of $d$ -semistable deformations is $\rho _ { 1 } ^ { - 1 } ( 1 )$ . Then both $\rho _ { 1 }$ and $\rho$ are homomorphisms since they take the identity to the identity, and $\rho _ { 1 } ^ { - 1 } ( 1 ) \subseteq \rho ^ { - 1 } ( 1 )$ . The differential of $\rho _ { 1 }$ is surjective at $t = 0$ by construction and [6, (5.9) and (4.5)]. Hence the codimension of $\mathrm { K e r } ( \rho _ { 1 } ) _ { * }$ is $f - 1$ . The differential of $\rho$ is also surjective by Corollary 7.9. Hence $\dim \operatorname { K e r } ( \rho _ { 1 } ) _ { * } ~ =$ $\dim \operatorname { K e r } ( \rho ) _ { * }$ . Thus the two subtori $\mathrm { ( K e r } \rho _ { 1 } \mathrm { ) ^ { \mathrm { 0 } } }$ and $S = ( \ker \rho ) ^ { 0 }$ have the same tangent space at 1 and hence are equal.
In particular, all fibers $Y _ { s }$ are $d$ -semistable.
The final statement (ii) about the Kodaira-Spencer map then follows from Theorem 7.7. q.e.d.

To complete the proof of Theorem 8.3, consider the family $( \mathcal { U } _ { S } , \mathcal { D } ) $ $S$ described in the remarks before Lemma 8.5. By construction, the family $( \mathcal { U } _ { S } , \mathcal { D } ) \to S$ induces a period map $\operatorname { p e r } _ { S } \colon S \to \operatorname { H o m } ( \overline { { \Lambda } } _ { 0 } , \mathbb { C } ^ { * } )$ . By Lemma 8.4, the map $\mathrm { p e r } _ { S }$ is an affine map.
We claim that the differential of ${ \mathrm { p e r } } _ { S }$ is surjective.
By Lemma 8.5 and the remarks before it, we are reduced to showing the following: let

$$
\{ \xi _ { 0 } , \dots , \xi _ { f - 1 } \} ^ { \perp } \subseteq H ^ { 1 } ( Y _ { 0 } ; T _ { Y } ( - \log D ) )
$$

be defined as $\{ \theta \ \in \ H ^ { 1 } ( Y _ { 0 } ; T _ { Y } ( - \log D ) ) : \ \theta \ \smile \ \hat { c } _ { 1 } ( \xi _ { 0 } ) = \dots = \theta \ \smile$ $\hat { c } _ { 1 } ( \xi _ { f - 1 } ) = 0 \}$ . We can replace $\hat { c } _ { 1 } ( \xi _ { i } )$ by $\bar { c } _ { 1 } ( \xi _ { i } )$ in the above.
Moreover,

$$
\begin{array} { r l } & { ( H ^ { 1 } ( Y _ { 0 } ; \Omega _ { Y _ { 0 } } ^ { 1 } ( \log D ) / \tau _ { Y _ { 0 } } ^ { 1 } ( - D ) ) ) / \operatorname { s p a n } \{ \bar { c } _ { 1 } ( \xi _ { 0 } ) , \dots , \bar { c } _ { 1 } ( \xi _ { f - 1 } ) \} } \\ & { \qquad \cong ( \Lambda _ { 0 } ) _ { \mathbb { C } } / \{ \xi _ { 0 } , \dots , \xi _ { f - 1 } \} = ( \overline { { \Lambda } } _ { 0 } ) _ { \mathbb { C } } . } \end{array}
$$

Then cup product induces a perfect pairing

$$
\{ \xi _ { 0 } , \ldots , \xi _ { f - 1 } \} ^ { \perp } \otimes ( \overline { { { \Lambda } } } _ { 0 } ) _ { \mathbb { C } } \to H ^ { 2 } ( Y _ { 0 } ; { \cal O } _ { Y _ { 0 } } ( - D ) ) \cong H ^ { 1 } ( D ; { \cal O } _ { D } ) .
$$

This says that the differential of $\mathrm { p e r } _ { S }$ is surjective.
Hence $\mathrm { p e r } { } _ { S }$ is an affine map of tori with surjective differential.
It follows that $\mathrm { p e r } _ { S }$ is surjective.
This is exactly the statement of Theorem 8.3. q.e.d.

Remark 8.6. Related methods give a somewhat more direct proof of Theorem 4.1 in [11].

We can relate the period map for a $d$ -semistable Type III anticanonical pair to the period map for nearby smoothings as follows.
Suppose that $\pi \colon ( \mathcal { V } , \mathcal { D } )  \Delta ^ { k }$ is a morphism from the smooth complex manifold $y$ to the polydisk, whose fibers are smooth anticanonical pairs for $t \in \Delta ^ { k - 1 } \times \Delta ^ { * }$ and such that the fibers over $\Delta ^ { k - 1 } \times \{ 0 \}$ are $d$ -semistable Type III anticanonical pairs.
We will apply this in the case of the germ of the smoothing component of a $d$ -semistable Type III anticanonical pair below and for one parameter families (the case $k = 1$ ) in Section $^ { 9 }$ . In this case, the monodromy on $\Lambda = \Lambda ( Y _ { t } , D _ { t } )$ is trivial, there is a well-defined monodromy invariant $\lambda \in \Lambda$ , and there is an inclusion $\overline { { \Lambda } } _ { 0 }  \Lambda$ identifying the image with $\lambda ^ { \perp }$ .

Proposition 8.7. Let $\rho \colon \operatorname { H o m } ( \Lambda , \mathbb { C } ^ { * } ) \to \operatorname { H o m } ( { \overline { { \Lambda } } } _ { 0 } , \mathbb { C } ^ { * } )$ denote restriction.
The function $\Phi \colon \Delta ^ { k }  \operatorname { H o m } ( { \overline { { \Lambda } } } _ { 0 } , \mathbb { C } ^ { * } )$ defined by

$$
\Phi ( t ) = \left\{ \rho \circ \varphi _ { Y _ { t } } , \quad i f t \in \Delta ^ { k - 1 } \times \Delta ^ { * } ; \right.
$$

is holomorphic.

Proof.
For a fixed $\alpha \in \overline { { \Lambda } } _ { 0 }$ , there is a corresponding line bundle ${ \mathcal { L } } _ { \alpha }$ on $\mathcal { V }$ , well defined up to twisting by components of the inverse image of $\Delta ^ { k - 1 } \times \{ 0 \} ^ { * }$ . Restricting ${ \mathcal { L } } _ { \alpha }$ to $\mathcal { D }$ and choosing a trivialization $\mathcal { D } \cong$ $D \times \Delta ^ { k }$ (which is always possible locally) gives a holomorphic map $\Delta ^ { k } \to \operatorname { P i c } ^ { 0 } D \cong \mathbb { C } ^ { * }$ . By definition, this map is independent of the choice of $\mathcal { L } _ { \alpha }$ and defines $\Phi$ , evaluated on the class $\alpha$ . Doing this construction for a basis of $\overline { { \Lambda } } _ { 0 }$ shows that $\Phi$ is holomorphic.
q.e.d.

Remark 8.8. Using the alternative formulation of the period map from the preceding section and Proposition 6.2 in the parametrized case, we see that, if $t _ { k }$ is a coordinate defining the last factor of $\Delta ^ { k }$ in the notation above, and $\alpha$ is a class in $\Lambda$ , then, for $t \in \Delta ^ { k - 1 } \times \Delta ^ { * }$ ,

$$
\varphi _ { Y _ { t } } ( \alpha ) = t _ { k } ^ { ( \alpha \cdot \lambda ) } h ( t ) ,
$$

where $h ( t )$ extends to a holomorphic, nowhere zero function on $\Delta ^ { k }$ . Hence, $\varphi _ { Y _ { t } } ( \alpha )$ extends to a holomorphic function on $\Delta ^ { k }$ with values in $\mathbb { C } ^ { * } \iff \alpha \in \Lambda _ { 0 }$ .

We will then need the following, which is in a sense complementary to Theorem 8.3:

Proposition 8.9. Suppose that $( Y _ { 0 } , D )$ is a $d$ -semistable Type III anticanonical pair.
Let $\Upsilon$ be a sublattice of $\overline { { \Lambda } } _ { 0 }$ such that $\bar { \varphi } _ { Y _ { 0 } } ( L ) = 1$ for all $L \in \Upsilon$ . Then there exists a Type III degeneration $y  \Delta$ , with special fiber $Y _ { 0 }$ such that, via the specialization map

$\varphi _ { Y _ { t } } ( \operatorname { s p } ( L ) ) = 1$ for all $t \in \Delta ^ { * }$ .

Proof.
Let $( \mathcal { V } , \mathcal { D } )  ( X , 0 )$ be the germ of the subspace of the semiuniversal deformation of the pair $( Y _ { 0 } , D )$ corresponding to the smoothing component and, on the discriminant locus, to preserving the condition of $d$ -semistability.
Note that $\operatorname { P i c } \mathcal { V } \cong \Lambda _ { 0 }$ and that the classes $\xi _ { 0 } , \ldots , \xi _ { f - 1 }$ extend to Cartier divisors on $\nu$ with trivial restriction to $\mathcal { D }$ . By Proposition 8.7, there is a well-defined, holomorphic period map (on the level of germs) $\Phi \colon X \to \operatorname { H o m } ( { \overline { { \Lambda } } } _ { 0 } , \mathbb { C } ^ { * } )$ . Via restriction, there is a surjection

$$
\operatorname { H o m } ( { \overline { { \Lambda } } } _ { 0 } , \mathbb { C } ^ { * } ) \to \operatorname { H o m } ( \Upsilon , \mathbb { C } ^ { * } ) ,
$$

and in particular the differential of the surjection is also surjective.
Taking the composition with the period map, there is a (germ of a) holomorphic map $\Phi _ { \Upsilon } \colon X \to \operatorname { H o m } ( \Upsilon , \mathbb { C } ^ { * } )$ . Theorem 7.7 and Corollary 7.9 imply that $\Phi \mathrm { r }$ is a submersion at $0 \in X$ and that $\Phi _ { \Upsilon } ^ { - 1 } ( 1 )$ is transverse to the discriminant hypersurface.
Taking a generic map of the disk $( \Delta , 0 )$ to $\Phi _ { \Upsilon } ^ { - 1 } ( 1 ) \subseteq ( X , 0 )$ (and which is in particular transverse to the discriminant) gives the existence of the Type III degeneration $y  \Delta$ above.
q.e.d.

# 9. Good sublattices and adjacent RDP singularities

Throughout this section, we fix a deformation type of a negative definite anticanonical pair $( Y , D )$ , $\Lambda = \Lambda ( Y , D )$ and $R$ denotes the set of roots of $\Lambda$ . We begin by describing a class of negative definite sublattices of $\Lambda$ :

Lemma 9.1. Let $( Y , D )$ be an anticanonical pair and let $\Upsilon$ be a negative definite sublattice of $\Lambda = \Lambda ( Y , D )$ , not necessarily primitive.
Suppose that

(i) Υ is spanned by elements of $R$ .\
(ii) The period homomorphism $\varphi _ { Y }$ satisfies: $\mathrm { K e r } \varphi _ { Y } \cap R = \Upsilon \cap R$ .

Then $\Upsilon \cap R$ is a root system in the real vector space $\Upsilon _ { \mathbb { R } } = \Upsilon \otimes \mathbb { R }$ and there exist a set of simple roots $\beta _ { 1 } , \ldots , \beta _ { n } \in \Upsilon$ such that

(i) For every $i$ , $\beta _ { i } = [ C _ { i } ]$ , where $C _ { i }$ is $a - 2$ -curve.\
(ii) If $\beta \in R$ and $\varphi _ { Y } ( \beta ) = 1$ , then $\beta = \pm \textstyle \sum _ { i } n _ { i } C _ { i }$ , where the $n _ { i }$ are nonnegative integers.
In particular, if $C$ is $a - 2$ -curve on $Y$ , then $C = C _ { i }$ for some $i$ .

Proof.
If $\beta _ { 1 } , \beta _ { 2 } \in \Upsilon \cap R$ , then $r _ { \beta _ { 1 } } ( \beta _ { 2 } ) \in \Upsilon \cap R$ by [9, (6.9)]. It then follows e.g. by Definition 1 in [2, IV §1] that $\Upsilon \cap R$ is a root system in $\Upsilon _ { \mathbb { R } }$ (and in fact that every element of square $- 2$ in the $\mathbb { Z }$ -span of $\Upsilon \cap R$ is a root).

Let $\Delta _ { Y }$ be the set of $- 2$ -curves on $Y$ , let $\mathsf { W } ( \Delta _ { Y } )$ be the reflection group generated by $\Delta _ { Y }$ , and let $R _ { Y } ^ { \mathrm { n o d } } = \mathsf { W } ( \Delta _ { Y } ) \cdot \Delta _ { Y }$ . Then, by [9, Theorem 6.6], $R _ { Y } ^ { \mathrm { n o d } } = \mathrm { K e r } \varphi _ { Y } \cap R = \Upsilon \cap R$ . Let $\beta _ { 1 } , \ldots , \beta _ { n } \in \Upsilon$ be the simple roots for a Weyl chamber in $\Upsilon _ { \mathbb { R } }$ defined by an ample divisor on $Y$ . By [8, Lemma 2.4(ii)], all positive roots are effective.
On the other hand, every $\beta \in R _ { Y } ^ { \mathrm { n o d } }$ is of the form $\textstyle \sum _ { i } n _ { i } [ C _ { i } ]$ , where the $C _ { i }$ are $- 2$ -curves on $Y$ . A standard argument using the fact that $\Upsilon$ is negative definite shows that, if $\beta$ is effective and of the form $\textstyle \sum _ { i } n _ { i } [ C _ { i } ]$ , where the $C _ { i }$ are $- 2$ -curves, then $n _ { i } \geq 0$ for all $i$ . Hence the positive roots are exactly the classes of the $\beta \in R _ { Y } ^ { \mathrm { n o d } }$ of the form $\textstyle \sum _ { i } n _ { i } [ C _ { i } ]$ , $n _ { i } \geq 0$ , and the simple roots $\beta _ { i }$ are exactly the classes of the $- 2$ -curves on $Y$ . q.e.d.

Lemma 9.2. Let $\Upsilon$ be a negative definite sublattice of $\Lambda$ and suppose that $\Upsilon$ is spanned by $R \cap \Upsilon$ . Then there exists a $\lambda \in B _ { \mathrm { g e n } }$ such that $\Upsilon \subseteq ( \lambda ) ^ { \perp }$ .

Proof.
Let $\Upsilon ^ { \prime }$ be the saturation of $\Upsilon$ , and let $\Upsilon ^ { \prime \prime }$ be the finite index sublattice of $\Upsilon ^ { \prime }$ spanned by $R \cap \Upsilon ^ { \prime }$ . Then there exists a $\varphi \colon \Lambda  \mathbb { C } ^ { * }$ with $\mathrm { K e r } \varphi = \Upsilon ^ { \prime }$ . Hence $\operatorname { K e r } \varphi \cap { \cal R } = { \cal R } \cap \Upsilon ^ { \prime } = { \cal R } \cap \Upsilon ^ { \prime \prime }$ , and $\Upsilon ^ { \prime \prime }$ is spanned by $R \cap \Upsilon ^ { \prime \prime }$ . Using the surjectivity of the period map, there exists a $Y$ such that $\varphi = \varphi _ { Y }$ . By Lemma 9.1, there exist $- 2$ -curves $C _ { 1 } , \ldots , C _ { k }$ whose classes span $\Upsilon ^ { \prime \prime }$ . Moreover, there is a nef and big divisor $H$ on $Y$ such that $\boldsymbol { H } \cdot \boldsymbol { C } _ { j } = 0$ for all $j$ , $\boldsymbol { H } \cdot \boldsymbol { D } _ { i } = 0$ for all $i$ and $H \cdot C > 0$ for every curve $C \neq C _ { j }$ or $D _ { i }$ . If $\lambda = [ H ]$ , then $\lambda \in \mathcal { B } _ { \mathrm { g e n } }$ and $\lambda \cdot [ C _ { j } ] = 0$ for all $j$ , hence $\lambda \cdot x = 0$ for all $x \in \Upsilon$ . q.e.d.

We can then rephrase the conditions of Lemma 9.1 as follows:

Lemma 9.3. Let $\lambda$ be a class in $ { B \_ { \mathrm { g e n } } }$ . Let $\beta \in \Lambda$ , $\beta ^ { 2 } = - 2$ . Suppose that $\beta \cdot \lambda = 0$ . Then $\beta \in R$ .

Hence, the condition (i) of Lemma 9.1 is equivalent to: there exists a $\lambda \in B _ { \mathrm { g e n } }$ such that $\Upsilon \subseteq ( \lambda ) ^ { \perp }$ and

(i)0 $\Upsilon$ is spanned by elements of $\Lambda$ of square $- 2$ .

Proof.
Since $\lambda$ is in the interior of $\boldsymbol { B } _ { \mathrm { g e n } }$ , it is easy to check that $\lambda$ is not orthogonal to any exceptional curve and hence that there is a neighborhood of $\lambda$ in $\mathcal { C } ^ { + }$ which is disjoint from $W ^ { E }$ for every exceptional curve $E$ . There exist positive $r _ { i }$ such that $\begin{array} { r } { ( \sum _ { i } r _ { i } [ D _ { i } ] ) \cdot [ D _ { j } ] < 0 } \end{array}$ for all $j$ , and hence

$$
( \lambda - \sum _ { i } r _ { i } [ D _ { i } ] ) \cdot [ D _ { j } ] > 0
$$

for all $j$ . Multiplying the $r _ { i }$ by a positive $t \ll 1$ , we can further assume that $\begin{array} { r } { \lambda - \sum _ { i } r _ { i } [ D _ { i } ] } \end{array}$ is not separated from $\lambda$ by a wall of the form $W ^ { E }$ , where $E$ is exceptional, and hence $\begin{array} { r } { \lambda - \sum _ { i } r _ { i } \lfloor D _ { i } \rfloor \in \mathcal { A } _ { \mathrm { g e n } } } \end{array}$ . Thus $W ^ { \beta }$ meets the interior of $\overline { { A } } _ { \mathrm { g e n } }$ . It follows from [9, Theorem 6.6] that $\beta \in R$ . q.e.d.

Definition 9.4. Let $\Upsilon$ be a negative definite sublattice of $\Lambda$ , not necessarily primitive.
Then $\Upsilon$ is good if

(i) $\Upsilon$ is spanned by elements of $R$ .\
(ii) There exists a homomorphism $\varphi \colon \Lambda \to \mathbb { C } ^ { * }$ such that $\mathrm { K e r } \varphi \cap R =$ $\Upsilon \cap R$ .

The lattice $\Upsilon$ determines an RDP configuration (possibly consisting of more than one singular point) by taking the appropriate type of a set of simple roots for $\Upsilon \cap R$ . We say that the corresponding RDP configuration is of type $\Upsilon$ .

Given $\lambda \in B _ { \mathrm { g e n } }$ , the lattice $\Upsilon$ is $\lambda$ -good if it is good and if $\Upsilon \subseteq ( \lambda ) ^ { \perp }$ . By Lemma 9.2, every good sublattice is $\lambda$ -good for some $\lambda$ .

Let $\Upsilon$ be a lattice spanned by elements of $R$ . If $\Upsilon$ is primitive, then it is good.
If $\Upsilon ^ { \prime }$ is the saturation of $\Upsilon$ and $\Upsilon ^ { \prime } / \Upsilon$ is cyclic, then $\Upsilon$ is good.
If $\Upsilon = \oplus \Upsilon _ { i }$ is the decomposition of $\Upsilon$ into its irreducible summands, then $\Upsilon$ is good $\iff \mathrm { ~ T ~ } _ { i }$ is good for every $i$ (this follows easily from the fact that, if $\beta = \textstyle \sum _ { i } \beta _ { i } \in \Lambda$ with $\beta _ { i } ^ { 2 } < 0$ for all $i$ and $\boldsymbol { \beta } _ { i } \boldsymbol { \cdot } \boldsymbol { \beta } _ { j } = 0$ if $i \neq j$ , then $\beta ^ { 2 } = - 2 \iff \beta = \beta _ { i }$ for some $i$ and $\beta _ { i } ^ { 2 } = - 2$ ).

To explain the geometric meaning of good lattices, we start with the following definition:

Definition 9.5. A generalized anticanonical pair is a pair $( \overline { { Y } } , D )$ , where $\overline { { Y } }$ is a rational surface, possibly with rational double points, and $D$ is a cycle contained in the smooth locus of $\overline { { Y } }$ , such that, if $\pi \colon Y \to { \overline { { Y } } }$ is the minimal resolution, then $( Y , D )$ is an anticanonical pair.

We then have the following alternate characterization of RDP configurations of type $\Upsilon$ (cf.
[27, II (2.7)]):

Proposition 9.6. Suppose that $( \overline { { Y } } , D )$ is a generalized anticanonical pair with minimal resolution $\pi \colon Y \to { \overline { { Y } } }$ such that every $- 2$ -curve on $Y$ is contained in a fiber of $\boldsymbol { \mathscr { u } }$ . Then the classes of the components of fibers of $\pi$ generate a good sublattice $\Upsilon$ of $\Lambda ( Y , D )$ , and every good sublattice of $\Lambda ( Y , D )$ arises in this way.

Hence the RDP configurations of type $\Upsilon$ , for some good sublattice of $\Lambda ( Y , D )$ , are exactly the RDP configurations which appear on a generalized anticanonical pair $( \overline { { Y } } , D )$ whose minimal resolution has deformation type $[ ( Y , D ) ]$ and which satisfy the condition that every $- 2$ -curve on the minimal resolution is contained in a fiber of $\pi$ .

Proof.
If $( \overline { { Y } } , D )$ is as in the statement of the proposition, let $\beta \in$ $\operatorname { K e r } \varphi _ { Y } \cap R$ . Then, by [9, 6.6] and its method of proof, $\pm \beta = \textstyle \sum _ { i } n _ { i } [ C _ { i } ]$ , where $C _ { i }$ is a $- 2$ -curve on $Y$ . Thus $\beta \in \Upsilon$ . It follows that $\Upsilon$ is a negative definite lattice spanned by $\operatorname { K e r } \varphi _ { Y } \cap R$ , so that $\Upsilon$ is good.

Conversely, suppose that $\Upsilon$ is a good sublattice.
By the surjectivity of the period map, we can choose an anticanonical pair $( Y , D )$ such that $\operatorname { K e r } \varphi _ { Y } \cap R = \Upsilon \cap R$ and $\Upsilon$ is spanned by $\Upsilon \cap R$ . By Lemma 9.1, there exists a set of simple roots $\beta _ { 1 } = [ C _ { 1 } ] , \ldots , \beta _ { k } = [ C _ { k } ]$ , where the $C _ { i }$ are exactly the $- 2$ -curves on $Y$ . Since $\Upsilon$ is negative definite, there exists a morphism $\pi \colon Y  Y$ , where $\overline { { Y } }$ is normal and $\pi$ exactly contracts the $C _ { i }$ . Hence $( \overline { { Y } } , D )$ is a generalized anticanonical pair with minimal resolution $\pi \colon Y \to { \overline { { Y } } }$ such that every $- 2$ -curve on $Y$ is contained in a fiber of $\pi$ . q.e.d.

We now relate the above discussion to the existence of adjacent RDP singularities.

Theorem 9.7. Let $\pi \colon \mathcal { V }  \Delta$ be a Type III degeneration with monodromy invariant $\lambda$ . Let $\beta _ { 1 } , \ldots , \beta _ { k }$ be the finite set of elements $\beta$ of $R$ such that $\beta \cdot \lambda = 0$ . Then, for all $t \in \Delta ^ { * }$ , $| t | \ll 1$ and for all $\beta \in R$ , $\varphi _ { Y _ { t } } ( \beta ) = 1 \iff \beta = \beta _ { i }$ for some i and the function $f ( t ) = \varphi _ { Y _ { t } } ( \beta _ { i } )$ is identically equal to 1 for all $t \in \Delta ^ { * }$ .

Proof.
$\Longleftarrow :$ Obvious.

$\Longrightarrow$ : Let $U$ be a neighborhood of $\lambda$ in $\mathcal { C } ^ { + }$ such that, if $\beta \in R$ and $W ^ { \beta }$ is a wall with $W ^ { \beta } \cap U \neq \emptyset$ , then $\beta = \beta _ { i }$ for some $i$ , i.e. $W ^ { \beta }$ is one of the finitely many walls corresponding to elements of $R$ and passing through $\lambda$ .

Given $\varphi _ { Y _ { t } } \colon \Lambda \to \mathbb { C } ^ { * }$ , the function $\log | \varphi _ { Y _ { t } } | \colon \Lambda \to \mathbb { R }$ is a well-defined, $C ^ { \infty }$ function on $\Delta ^ { * }$ and thus corresponds to a function $\Delta ^ { * }  \Lambda _ { \mathbb { R } } ^ { \vee } = \Lambda _ { \mathbb { R } }$ , which we continue to denote by $\log | \varphi _ { Y _ { t } } |$ . By [9, (3.12)],

$$
\log { \varphi _ { Y _ { t } } } = 2 \pi \sqrt { - 1 } \omega ( t )
$$

as multi-valued functions on $\Delta ^ { * }$ . Hence, by Proposition 6.2,

$$
\log { \varphi _ { Y _ { t } } } = 2 \pi { \sqrt { - 1 } } \omega ( t ) = ( \log { t } ) \lambda + 2 \pi { \sqrt { - 1 } } f ( t )
$$

for a single-valued holomorphic function $f$ which extends to a holomorphic function at $0$ . Taking real parts, we obtain an equality of

(single-valued) functions

$$
\log | \varphi _ { Y _ { t } } | = \operatorname { R e } ( ( \log t ) \lambda + 2 \pi { \sqrt { - 1 } } f ( t ) ) = \log | t | \lambda + g ( t ) ,
$$

where $g ( t )$ is a $C ^ { \infty }$ function at $0$ . Dividing by $\log | t |$ gives

$$
\frac { \log | \varphi _ { Y _ { t } } | } { \log | t | } = \lambda + \frac { g ( t ) } { \log | t | } .
$$

Thus $\log | \varphi _ { Y _ { t } } | / \log | t |$ defines a continuous function $h ( t ) \colon \Delta \to \Lambda _ { \mathbb { R } }$ with $h ( 0 ) = \lambda$ . Thus, for $| t | \ll 1$ , $h ( t ) \in U$ . It follows that, if $t \in \Delta ^ { * }$ , $| t | \ll 1$ , $\beta \in R$ , and $\varphi _ { Y _ { t } } ( \beta ) = 1$ , then $h ( t )$ lies on $W ^ { \beta }$ and so $\beta = \beta _ { i }$ for some $i$ .

Given $\beta _ { i }$ as above, either $\varphi _ { Y _ { t } } ( \beta _ { i } )$ is identically equal to $1$ for all $t \in \Delta$ or $\varphi _ { Y _ { t } } ( \beta _ { i } ) = 1$ for at most finitely many $t \in \Delta ^ { * }$ . Choosing $| t |$ smaller if need be, we can then assume that, for all $i$ , if $\varphi _ { Y _ { t } } ( \beta _ { i } )$ is not identically equal to $1$ , then $\varphi _ { Y _ { t } } ( \beta _ { i } ) \neq 1$ for all $t \in \Delta ^ { * }$ . q.e.d.

Given a Type III degeneration $y  \Delta$ , by a theorem of ShepherdBarron [34, Theorem 2A, p. 157], there exists a birational morphism $f \colon \mathcal { V }  \overline { { \mathcal { V } } }$ over $\Delta$ , where $f _ { 0 } = f | _ { Y _ { 0 } }$ contracts $\textstyle \bigcup _ { i > 0 } V _ { i }$ and the cycle $D ^ { \prime }$ to a point and, for $t \neq 0$ , $f _ { t } = f | _ { Y _ { t } } \colon Y _ { t } \to \overline { { Y } } _ { t }$ is the minimal resolution of a union of rational double points.
We then have the following (compare [27, III (2.12)]):

Proposition 9.8. For $0 < | t | \ll 1$ , the irreducible components of the exceptional fibers of $f _ { t }$ are exactly the $- 2$ -curves on $Y _ { t }$ .

Proof.
Clearly, if $C _ { t }$ is an irreducible component of an exceptional fiber of $f _ { t }$ , then $C _ { t }$ is a $- 2$ -curve on $Y _ { t }$ . Conversely, suppose that $C _ { t }$ is a $- 2$ -curve on $Y _ { t }$ for some for $0 < | t | \ll 1$ and let $\left[ C _ { t } \right] = \beta$ . Then $\varphi _ { Y _ { t } } ( \beta ) =$ 1. By Theorem 9.7, $\beta$ is orthogonal to $\lambda$ and $\varphi _ { Y _ { t } } ( \beta )$ is identically 1. It follows from Proposition 3.9 that $\beta$ corresponds to a line bundle $\mathcal { L }$ on $y$ . For all $s \in \Delta ^ { * }$ , $\pm \beta \in R _ { Y _ { s } } ^ { \mathrm { n o d } }$ , i.e. $\pm \beta = \textstyle \sum _ { i } [ C _ { i } ]$ where the $C _ { i }$ are $- 2$ -curves on $Y _ { s }$ . The condition on $s \in \Delta ^ { * }$ that $\beta$ is effective on $Y _ { s }$ is closed (by semicontinuity) and open (because we can choose a relatively ample divisor $\mathcal { H }$ on $y$ over small open subsets of $\Delta ^ { * }$ ). Since $\beta$ is effective on $Y _ { t }$ , it follows that $\beta$ is effective for all $s \in \Delta ^ { * }$ , and, for $s$ generic, $\beta = \lfloor C _ { s } \rfloor$ is the class of an irreducible curve.
Since $h ^ { 0 } ( Y _ { s } ; \mathcal { L } | _ { Y _ { s } } ) > 0$ for all $s \in \Delta ^ { * }$ , arguing as in the proof of Proposition 3.11, after modifying $\mathcal { L }$ by $\mathcal { O } _ { \mathcal { Y } } ( \sum _ { i } a _ { i } V _ { i } )$ , we can assume that $\mathcal { L } = \mathcal { O } _ { y } ( \mathcal { C } )$ where $\mathcal { C }$ is a surface on $y$ , not containing $V _ { i }$ for any $i$ , and such that ${ \mathcal { C } } \cap Y _ { t } = C _ { t }$ . In particular, there exists an effective Cartier divisor $C _ { 0 } = \mathcal { C } \cap Y _ { 0 }$ on $Y _ { 0 }$ such that $C _ { 0 } \cdot D _ { j } = 0$ for every $j$ . But every such divisor $C _ { 0 }$ is a sum of the form $\textstyle \sum _ { i } n _ { i } D _ { i }$ , where $n _ { i } \geq 0$ , plus components disjoint from $D$ , and hence is contained in $\textstyle \bigcup _ { i > 0 } V _ { i }$ . Since $( D _ { i } \cdot D _ { j } )$ is negative definite, this is only possible if $n _ { i } = 0$ for all $i$ . Thus $\textstyle C _ { 0 } \subseteq \bigcup _ { i > 0 } V _ { i }$ , so that, via the relative contraction morphism $f \colon \mathcal { V }  \overline { { \mathcal { V } } }$ over $\Delta$ , $C _ { 0 }$ is contracted to a point.
Since $\mathcal { C }$ fibers over $\Delta$ and $f$ contracts the fiber $C _ { 0 }$ to a point, $f$ must contract all fibers of $c \to \Delta$ to points as well.
Thus $f _ { t }$ contracts $C _ { t }$ to a point.
q.e.d.

We can now state the main result concerning possible adjacencies of the cusp to RDP singularities:

Theorem 9.9. (i) Suppose that $\lambda \in B _ { \mathrm { g e n } }$ and that $\Upsilon$ is a $\lambda$ -good sublattice of $\Lambda$ . Let $( Y _ { 0 } , D )$ be a Type III anticanonical pair of type $\lambda$ . Then the cusp $D ^ { \prime }$ is adjacent to an RDP configuration of type $\Upsilon$ . More precisely, after a locally trivial deformation of $Y _ { 0 }$ through $d$ -semistable varieties, there exists a Type III degeneration $y  \Delta$ with central fiber $Y _ { 0 }$ and a blowdown $\mathcal { V }  \overline { { \mathcal { V } } }$ over $\Delta$ , such that the central fiber of $\overline { { \mathcal { V } } }$ is $V _ { 0 }$ with $D ^ { \prime }$ contracted and the singular locus of the general fiber is an RDP configuration of type $\Upsilon$ .

(ii) Conversely, suppose that the cusp $D ^ { \prime }$ is adjacent to an RDP configuration via a one parameter family $\bar { \pi } : \overline { { \mathcal { V } } } \to \Delta$ of $\mathbb { Q }$ -type $\lambda$ . For $| t | \ll 1$ , if $Y _ { t }$ is the minimal resolution of a general fiber $\overline { { Y } } _ { t }$ of $\bar { \pi }$ , then the components of the exceptional curves generate a $\lambda$ -good sublattice $\Upsilon$ of $\Lambda$ , and the RDP configuration on the general fiber is of type $\Upsilon$ .

Proof.
(i) Given the $\lambda$ -good sublattice $\Upsilon$ , choose a $\varphi \colon \Lambda  \mathbb { C } ^ { * }$ such that $\operatorname { K e r } \varphi \cap R = \Upsilon \cap R$ . Let $\varphi$ be the restriction of $\varphi$ to $\overline { { \Lambda } } _ { 0 } = ( \lambda ) ^ { \perp }$ . By Theorem 8.3, after a locally trivial deformation of $Y _ { 0 }$ through $d$ - semistable varieties, we can assume that $\bar { \varphi } _ { Y _ { 0 } } = \bar { \varphi }$ . By Proposition 8.9, there exists a Type III degeneration $y  \Delta$ with central fiber $Y _ { 0 }$ such that, under the natural identification of $\Upsilon$ and $\overline { { \Lambda } } _ { 0 }$ with sublattices of $\Lambda ( Y _ { t } )$ , $\varphi _ { Y _ { t } } ( \beta ) = 1$ for all $\beta \in \Upsilon \cap R$ and all $t \in \Delta ^ { * }$ . Conversely, by Theorem 9.7, for $| t | \ll 1$ , if $\beta \in R$ and $\varphi _ { Y _ { t } } ( \beta ) = 1$ , then $\varphi _ { Y _ { t } } ( \beta )$ is identically 1 and $\beta \in ( \lambda ) ^ { \perp }$ , hence $\beta \in \overline { { \Lambda } } _ { 0 }$ . Using the continuity of $\varphi _ { Y _ { t } } ( \beta )$ (Proposition 8.7), $\bar { \varphi } _ { Y _ { 0 } } ( \beta ) = 1$ as well.
Thus $\beta \in \Upsilon \cap R$ . In particular, by Lemma 9.1, the $- 2$ -curves on $Y _ { t }$ correspond to a set of simple roots for $\Upsilon$ . By Proposition 9.8, these are exactly the exceptional fibers of the blowdown $Y _ { t }  \overline { { Y } } _ { t }$ . Hence the singular locus of $Y _ { t }$ is an RDP configuration of type $\Upsilon$ .

(ii) After a base change, we can assume that $\bar { \pi } \colon \overline { { \mathcal { V } } }  \Delta$ is birational to a Type III degeneration of $\mathbb { Q }$ -type $\lambda$ . For $0 < | t | \ll 1$ , let $\Upsilon$ be the sublattice of $\Lambda$ generated by ${ \mathrm { K e r } } \varphi _ { Y _ { t } } \cap R$ . By Theorem 9.7, if $\beta \in$ $\mathrm { K e r } \varphi _ { Y _ { t } } \cap R$ , then $\beta \in ( \lambda ) ^ { \perp }$ , and hence $\Upsilon \subseteq ( \lambda ) ^ { \perp }$ . Thus $\Upsilon$ is good, in fact it is $\lambda$ -good.
By Lemma 9.1, the classes of the $- 2$ -curves on $Y _ { t }$ are a set of simple roots for $\Upsilon$ . By Proposition 9.8, the $- 2$ -curves on $Y _ { t }$ are exactly the fibers of the morphism $Y _ { t }  Y _ { t }$ . Hence the RDP configuration on $Y _ { t }$ is of type $\Upsilon$ . q.e.d.

Corollary 9.10. Let $p ^ { \prime }$ be a cusp singularity with minimal resolution $D ^ { \prime }$ and let $D$ be the dual cycle.
Suppose that $( Y , D )$ is an anticanonical pair.
Then the possible nearby RDP configurations on some smoothing component of $p ^ { \prime }$ of type $( Y , D )$ are exactly the RDP configurations of type $\Upsilon$ , where $\Upsilon$ is a good sublattice of $\Lambda ( Y , D )$ .

Proof.
Suppose that there is a nearby RDP configuration on some smoothing component of $p ^ { \prime }$ of type $( Y , D )$ . Then we can choose a one parameter deformation $\pi \colon ( { \overline { { \mathcal { V } } } } , { \mathcal { D } } ) \to \Delta$ , where the central fiber $( Y _ { 0 } , D )$ is the Inoue surface with $D ^ { \prime }$ contracted.
After base change, there is a birational model for $\pi \colon ( { \overline { { \mathcal { V } } } } , { \mathcal { D } } ) \to \Delta$ which is a Type III degeneration with monodromy invariant $\lambda$ for some $\lambda \in B _ { \mathrm { g e n } }$ . By (ii) of Theorem 9.9, the RDP configuration on a general fiber of $\bar { \pi }$ is of type $\Upsilon$ , where $\Upsilon$ is a $\lambda$ -good and hence good sublattice of $\Lambda ( Y , D )$ .

Conversely, suppose that $\Upsilon$ is a good sublattice of $\Lambda ( Y , D )$ . By Lemma 9.2, $\Upsilon$ is $\lambda$ -good for some $\lambda \in B _ { \mathrm { g e n } }$ . By Theorem 5.9, there exists a Type III anticanonical pair $( Y _ { 0 } , D )$ with monodromy invariant $\lambda$ . Hence, by (i) of Theorem 9.9, $p ^ { \prime }$ is adjacent to an RDP of type $\Upsilon$ . q.e.d.

# References

[1] M. Abouzaid, D. Auroux, and L. Katzarkov, Lagrangian fibrations on blowups of toric varieties and mirror symmetry for hypersurfaces, https://arxiv.org/abs/1205.0053, 2012.\
[2] N. Bourbaki, Groupes et Alg\`ebres de Lie, Chap.
4, 5, et 6, Masson, Paris, 1981.\
[3] C.H. Clemens, Jr., Picard-Lefschetz theorem for families of nonsingular algebraic varieties acquiring ordinary singularities, Trans.
Amer.
Math.
Soc.
136 (1969), 93–108.\
[4] P. Deligne, Equations diff´erentielles \`a points singuliers r´eguliers ´ , Lecture Notes in Mathematics, Vol. 163. Springer-Verlag, Berlin-New York, 1970.\
[5] P. Engel, A proof of Looijenga’s conjecture via integral-affine geometry, http://arxiv.org/pdf/1409.7676, 2014.\
[6] R. Friedman, Global smoothing of varieties with normal crossings, Annals of Math.
118 (1983), 75–114.\
[7] R. Friedman, Base change, automorphisms, and stable reduction for type III K3 surfaces, in The Birational Geometry of Degenerations pp. 277–298, Progr.
Math.
29, Birkh¨auser, Boston, Mass., 1983.\
[8] R. Friedman, On the ample cone of a rational surface with an anticanonical cycle, Algebra & Number Theory 7 (2013), 1481–1504.\
[9] R. Friedman, On the geometry of anticanonical pairs, arxiv.org/abs/1502.02560, 2016.\
[10] R. Friedman and R. Miranda, Smoothing cusp singularities of small length, Math.
Ann.
263 (1983), 185–212.\
[11] R. Friedman and F. Scattone, Type III degenerations of K3 surfaces, Invent.
Math.
83 (1986), 1–39.\
[12] M. Gross.
Special Lagrangian fibrations I: Topology, https://arxiv.org/abs/alg-geom/9710006, 1997.\
[13] M. Gross, P. Hacking, and S. Keel, Moduli of surfaces with an anti-canonical cycle, Compos.
Math.
151 (2015), 265–291.\
[14] M. Gross, P. Hacking, and S. Keel, Mirror symmetry for log Calabi-Yau surfaces I, Publ.
Math.
Inst.
Hautes Etudes Sci.
´ 122 (2015), 65–168.\
[15] M. Gross and B. Siebert, Mirror symmetry via logarithmic degeneration data I, J. of Differential Geom.
72.2 (2006), 169–338.\
[16] M. Gross and B. Siebert.
Mirror symmetry via logarithmic degeneration data, II. J. of Algebraic Geom.
19.4 (2010), 679–780.\
[17] N. Hitchin, The moduli space of special Lagrangian sub manifolds, Annali Scuola Sup.
Norm.
Pisa Sci.
Fis.
Mat.
25 (1997), 503–515.\
[18] M. Inoue, New surfaces with no meromorphic functions II, in Complex analysis and algebraic geometry, 91–106. Iwanami Shoten, Tokyo, 1977.\
[19] Y. Kawamata and Y. Namikawa, Logarithmic deformation of normal crossing varieties and smoothing of degenerate Calabi-Yau manifolds, Invent.
Math.
118 (1994), 395–409.\
[20] M. Kontsevich, Homological algebra of mirror symmetry, https://arxiv.org/abs/alg-geom/9411018, 1994.\
[21] M. Kontsevich and Y. Soibelman.
Affine structures and non-Archimedean analytic spaces, The unity of mathematics, Birkh¨auser Boston (2006), 321–385.\
[22] C. L. Lawson, Transformation triangulations Discrete Math.
3 (1972), 365-272.\
[23] T.-J. Li and A.-K. Liu, Uniqueness of symplectic canonical class, surface cone and symplectic cone of 4-manifolds with $B ^ { + } = 1$ , J. Differential Geom.
58 (2001), 331–370.\
[24] T.-J. Li and C. Y. Mak, Symplectic log Calabi-Yau surface—deformation class, http://arxiv.org/pdf/1510.06131, 2015.\
[25] E. Looijenga, On the semi-universal deformation of a simple-elliptic hypersurface singularity.
II. The discriminant, Topology 17 (1978), 23–40.\
[26] E. Looijenga, The smoothing components of a triangle singularity.
II, Math.
Ann.
269 (1984), 357–387.\
[27] E. Looijenga, Rational surfaces with an anti-canonical cycle, Annals of Math.
114 (1981), 267–322.\
[28] E. Looijenga and J. Wahl, Quadratic functions and smoothing surface singularities, Topology 25 (1986), 261–291.\
[29] D. Morrison.
Compactifications of moduli spaces inspired by mirror symmetry, https://arxiv.org/abs/alg-geom/9304007, 1993.\
[30] U. Persson, On Degenerations of Algebraic Surfaces, Mem.
Amer.
Math.
Soc.
11 (1977), no. 189.\
[31] C.A.M. Peters and J.H.M. Steenbrink, Mixed Hodge structures, Ergebnisse der Mathematik und ihrer Grenzgebiete, 3. Folge, 52. Springer-Verlag, Berlin, 2008.\
[32] H. C. Pinkham, Simple elliptic singularities, Del Pezzo surfaces and Cremona transformations, in Several complex variables (Proc.
Sympos.
Pure Math., Vol. XXX, Part 1, Williams Coll., Williamstown, Mass., 1975), 69–71. Amer.
Math.
Soc., Providence, R. I., 1977.\
[33] H. C. Pinkham, Groupe de monodromie des singularit´es unimodulaires exceptionnelles, C. R. Acad.
Sci.
Paris S´er.
A-B 284 (1977), A1515–A1518.\
[34] N. I. Shepherd-Barron, Extending polarizations on families of K3 surfaces, in The Birational Geometry of Degenerations pp. 135–171, Progr.
Math.
29, Birkh¨auser, Boston, Mass., 1983.\
[35] J.H.M Steenbrink, Limits of Hodge structures, Invent.
Math.
31 (1975/76), 229– 257.\
[36] A. Strominger, S.-T. Yau, and E. Zaslow, Mirror symmetry is T-duality.
Nuclear Physics B 479.1-2 (1996), 243–259.\
[37] M. Symington, Four dimensions from two in symplectic topology, in Proceedings of Symposia in Pure Mathematics, Vol. 71, pp. 153–208. Amer.
Math.
Soc., 2003.\
[38] J. Wahl, Elliptic deformations of minimally elliptic singularities, Math.
Ann.
253 (1980), 241–262.\
Philip Engel\
Department of Mathematics\
Harvard University\
Cambridge, MA 02138\
USA\
mailto:engel@math.harvard.edu\
Robert Friedman\
Department of Mathematics\
Columbia University\
New York, NY 10027\
USA\
mailto:rf@math.columbia.edu
