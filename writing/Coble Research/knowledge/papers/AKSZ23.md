---
title: Compact moduli of K3 surfaces with a nonsymplectic automorphism
authors:
- Valery Alexeev
- Philip Engel
- ''
- Changho Han
year: 2022
bibkey: AKSZ23
tags:
- paper
- extraction
abstract: |
  We construct a modular compactification via stable slc pairs for the moduli spaces of K3 surfaces with a nonsymplectic group of automorphisms under the assumption that some combination of the fixed loci of automorphisms defines an effective big divisor, and prove that it is semitoroidal.
---

# COMPACT MODULI OF K3 SURFACES WITH A NONSYMPLECTIC AUTOMORPHISM

VALERY ALEXEEV, PHILIP ENGEL, AND CHANGHO HAN

Abstract.
We construct a modular compactification via stable slc pairs for the moduli spaces of K3 surfaces with a nonsymplectic group of automorphisms under the assumption that some combination of the fixed loci of automorphisms defines an effective big divisor, and prove that it is semitoroidal.

# Contents

1. Introduction 1
2. Moduli of K3s with a nonsymplectic automorphism 37
3. Stable pair compactifications
4. Moduli of quotient surfaces 15
5. Extensions 16\
   References 17

# 1. Introduction

Let $X$ be a smooth K3 surface over the complex numbers.
An automorphism $\sigma$ of $X$ is called non-symplectic if it has finite order $n > 1$ and $\sigma ^ { * } ( \omega _ { X } ) = \zeta _ { n } \omega _ { X }$ , where $\omega _ { X } \in H ^ { 2 , 0 } ( X )$ is a nonzero 2-form and $\zeta _ { n }$ is a primitive $n$ th root of identity.
By changing the generator of the cyclic group $\mu _ { n }$ we can and will assume that $\zeta _ { n } =$ $\exp ( 2 \pi i / n )$ . It is well known that a K3 surface admitting such an automorphism is projective.
The possibilities for the order are the numbers $n$ whose Euler function satisfies $\varphi ( n ) \leq 2 0$ with the single exception $n \neq 6 0$ , see [MO98, Thm. 3].

In this paper we study compactification of moduli spaces of pairs $( X , \sigma )$ . But to begin with, the automorphism group $\operatorname { A u t } ( X , \sigma )$ , i.e. those automorphisms of $X$ commuting with $\sigma$ , may be infinite.
To fix this, we will usually additionally assume:

By looking at the $\mu _ { n }$ -action on the tangent space of any fixed point, it is easy to see that $\operatorname { F i x } ( \sigma )$ is a disjoint union of several smooth curves and points.
The Hodge index theorem implies at most one of the fixed curves has genus $g \geq 2$ . One could instead have one or two fixed curves of genus $g = 1$ . All other fixed curves are isomorphic to $\mathbb { P } ^ { 1 }$ .

Under the ( $\exists g \ \geq \ 2$ ) assumption, the group $\operatorname { A u t } ( X , \sigma )$ is finite.
The opposite is almost true.
For example let $n = 2$ , i.e. $\sigma$ is an involution.
Then $\sigma ^ { * }$ fixes the

Neron-Severi lattice $S _ { X } \subset H ^ { 2 } ( X , \mathbb { Z } )$ and acts as multiplication by $( - 1 )$ on the lattice $T _ { X } = S _ { X } ^ { \perp }$ of transcendental cycles.
In this case $\operatorname { A u t } ( X , \sigma ) = \operatorname { A u t } ( X )$ .

Deformation classes of such K3 surfaces $( X , \sigma )$ are classified by the primitive 2-elementary hyperbolic sublattices $S \subset L _ { K 3 }$ . By Nikulin [Nik79b] there are 75 cases, uniquely determined by certain invariants $( g , k , \delta )$ . Among them 51 satisfy ( $\exists g \ \geq \ 2$ ). The only case when $| \operatorname { A u t } ( X ) | < \infty$ but ( $\exists g \ \geq \ 2$ ) is not satisfied is $( g , k , \delta ) \ : = \ : ( 1 , 9 , 1 )$ which is the one-dimensional mirror family to K3 surfaces of degree 2. In the case $( g , k , \delta ) = ( 2 , 1 , 0 )$ one has $| \operatorname { A u t } ( X ) | = \infty$ but the set $\operatorname { F i x } ( \sigma )$ consists of two elliptic curves, so ( $\exists g \geq 2$ ) does not hold.

Since the moduli stack of smooth quasipolarized K3 surfaces is notoriously nonseparated, so is usually the moduli stack of smooth K3s with a nonsymplectic automorphism.
For a fixed isometry $\rho ~ \in ~ O ( L _ { K 3 } )$ of order $n$ , there exists the moduli stack and moduli space of smooth K3 surfaces “of type $\rho ^ { \dagger }$ : those pairs $( X , \sigma )$ where the action of $\sigma ^ { * }$ on $H ^ { 2 } ( X , \mathbb { Z } )$ can be modeled by . We construct $\rho$ them in Section 2. The maximal separated quotient of $F _ { \rho }$ is $( { \mathbb D } _ { \rho } \setminus \Delta _ { \rho } ) / \Gamma _ { \rho }$ , where $\mathbb { D } _ { \rho }$ is a symmetric Hermitian domain of type IV if $n = 2$ or a complex ball if $n > 2$ , $\Gamma _ { \rho }$ is an arithmetic group, and $\Delta _ { \rho } \subset \mathbb { D } _ { \rho }$ is the discriminant locus.

Under the assumption ( $\exists g \ \geq 2$ ), the space $F _ { \rho } ^ { \mathrm { a d e } } : = ( \mathbb { D } _ { \rho } \setminus \Delta _ { \rho } ) / \Gamma _ { \rho }$ is the coarse moduli space for the K3 surfaces $\overline { { X } }$ with $A D E$ singularities, obtained from the smooth K3 surfaces $X$ by contracting the $\left( - 2 \right)$ -curves perpendicular to the component $C _ { 1 }$ with $g \geq 2$ in $\operatorname { F i x } ( \sigma )$ . The stack of such $A D E$ K3 surfaces is separated.

The main goal of this paper is to construct a functorial, geometrically meaningful compactification of the moduli space $F _ { \rho } ^ { \mathrm { a d e } }$ , under the assumption ( $\exists g \ \geq \ 2$ ). Let $R = C _ { 1 }$ , $\varphi _ { \vert m R \vert } \colon X \to { \overline { { X } } }$ be the contraction as above and $\overline { { R } }$ be the image of $R$ . Then for any $0 < \epsilon \ll 1$ the pair $( { \overline { { X } } } , \epsilon { \overline { { R } } } )$ is a stable pair with semi log canonical singularities.
Then the theory of KSBA moduli spaces (see [Kol21] for the general case or [AET19, ABE20] for the much easier special case needed here) gives a moduli compactificatio n F slc to a space of stable pairs with automorphism.

Our main Theorem 3.24 says that F slcρ is a semitoroidal compactification of $\mathbb { D } _ { \rho } / \Gamma _ { \rho }$ . This class of compactifications was introduced by Looijenga [Loo03b] as a common generalization of Baily-Borel and toroidal compactifications.
As a corollary, the family of $A D E \ \mathrm { K 3 }$ surfaces with an automorphism extends along the inclusion $( { \mathbb D } _ { \rho } \setminus \Delta _ { \rho } ) / \Gamma _ { \rho } \hookrightarrow { \mathbb D } _ { \rho } / \Gamma _ { \rho }$ .

The proof applies a modified form of one of the main theorems of [AE21] about so-called recognizable divisors.
The $g \geq 2$ component of the fixed locus is a canonical choice of a polarizing divisor.
We prove that this divisor is recognizable.

As we point out in Section 5, the results also extend to the more general situation of a symmetry group $G \subset \operatorname { A u t } X$ which is not purely symplectic.

The cases $n = 2 , 3 , 4 , 6$ are of the most interest for compactifications.
If $n \neq$ $2 , 3 , 4 , 6$ then the space $\mathbb { D } _ { \rho } / \Gamma _ { \rho }$ is already compact, see [Mat16] or Corollary 3.14.

K3 surfaces with an involution were classified by Nikulin in [Nik79b]. K3s with a non-symplectic automorphism of prime order $p \geq 3$ we classified by Artebani, Sarti, and Taki in [AS08, AST11]. The case $n = 4$ was treated by Artebani-Sarti in [AS15] and the case $n = 6$ by Dillies in [Dil09, Dil12].

We note two cases where our KSBA, semitoroidal compactification $\overline { { \boldsymbol F } } _ { \rho } ^ { \mathrm { s l c } }$ is computed in complete detail: Alexeev-Engel-Thompson [AET19] for the case of K3 surfaces of degree 2, generically double covers of $\mathbb { P } ^ { 2 }$ , and a forthcoming work Deopurkar-Han [DH22] which treats a 9-dimensional component in the moduli for $n = 3$ .

The paper is organized as follows.
In Section 2 we set up the general theory of the moduli of K3 surfaces with a non-symplectic automorphisms.
In Section 3 we define the stable pair compactifications and prove the main Theorem 3.24. In Section 4 we relate K3 surfaces with nonsymplectic automorphisms with their quotients $Y =$ X/µn, and the compactification F slcρ with the KSBA compactification of the moduli spaces of log del Pezzo pairs $( Y , \frac { n - 1 + \epsilon } { n } B )$ n−1+ B).

In Section 5 we extend the results in two different ways: to K3 surfaces with a finite group of symmetries $G \subset \operatorname { A u t } X$ which is not purely symplectic, and to more general polarizing divisors associated with such a group action.

Throughout, we work over the field of complex numbers.

Acknowledgements.
The first author was partially supported by NSF under DMS-1902157.

# 2. Moduli of K3s with a nonsymplectic automorphism

2A. Notations.
A lattice is a free abelian group with an integral-valued symmetric bilinear form.
Let $L = H ^ { \oplus 3 } \oplus E _ { 8 } ^ { \oplus 2 }$ be a fixed copy of the even unimodular lattice of signature $( 3 , 1 9 )$ , where $H = \mathrm { { I l } _ { 1 , 1 } }$ corresponds to the bilinear form $b ( x , y ) = x y$ and $E _ { 8 }$ is the standard negative definite even lattice of rank 8. For any smooth K3 surface $X$ the cohomology lattice $H ^ { 2 } ( X , \mathbb { Z } )$ is isometric to $L$ .

Denote by $S = S _ { X }$ the Neron-Severi lattice $\operatorname { P i c } ( X ) = \operatorname { N S } ( X )$ . By the Lefschetz $( 1 , 1 )$ -theorem, it equals $( H ^ { 2 , 0 } ( X ) ) ^ { \perp } \cap H ^ { 2 } ( X , \mathbb { Z } ) \subset H ^ { 2 } ( X , \mathbb { C } )$ . We have $H ^ { 2 , 0 } ( X ) =$ $\mathbb { C } \omega _ { X }$ for some nowhere vanishing holomorphic two-form $\omega _ { X }$ . If $X$ is projective, then $S _ { X }$ is nondegenerate of signature $( 1 , r _ { X } - 1 )$ . In this case, its orthogonal complement $T _ { X } = ( S _ { X } ) ^ { \perp } \subset H ^ { 2 } ( X , \mathbb { Z } )$ is the transcendental lattice, of signature $( 2 , 2 0 - r _ { X } )$ . The K¨ahler cone $K _ { X } \subset H ^ { 1 , 1 } ( X , \mathbb { R } )$ is the set of classes of K¨ahler forms on $X$ ; it is an open convex cone.

Theorem 2.1 (Torelli Theorem for K3 surfaces, [PSS71]). The isomorphisms $\sigma \colon X ^ { \prime } \to X$ are in bijection with the isometries $\sigma ^ { * } \colon H ^ { 2 } ( X , \mathbb { Z } ) \to H ^ { 2 } ( X ^ { \prime } , \mathbb { Z } )$ satisfying the conditions $\sigma ^ { * } ( H ^ { 2 , 0 } ( X ) ) = H ^ { 2 , 0 } ( X ^ { \prime } )$ and $\sigma ^ { * } ( { \boldsymbol { K } } _ { X } ) = { \boldsymbol { K } } _ { X ^ { \prime } }$ .

For any lattice $H$ , a root is a vector $\delta \in H$ with $\delta ^ { 2 } = - 2$ . The set of all roots is denoted by $H _ { - 2 }$ . The Weyl group $W ( H )$ is the group generated by reflections $\boldsymbol { v } \mapsto \boldsymbol { v } + ( \boldsymbol { v } , \boldsymbol { \delta } ) \boldsymbol { \delta }$ for $\delta \in H _ { - 2 }$ . It is a normal subgroup of the isometry group $O ( H )$ .

2B. Moduli of marked unpolarized K3s. The basic reference here is [ast85]. Let $X$ be a K3 surface.
A marking is an isometry $\phi \colon H ^ { 2 } ( X , \mathbb { Z } ) \to L$ . Let

$$
\mathbb { D } = \mathbb { P } \{ x \in L _ { \mathbb { C } } \mid x \cdot x = 0 , \ x \cdot { \bar { x } } > 0 \} , \quad \dim \mathbb { D } = 2 0 .
$$

There exists a fine moduli space $\mathcal { M }$ of marked $K \mathcal { 3 }$ surfaces and a period map $\pi \colon { \mathcal { M } }  \mathbb { D }$ , $( X , \phi ) \mapsto \phi ( H ^ { 2 , \cup } ( X ) ) \in \mathbb { P } ( L _ { \mathbb { C } } )$ . $\mathcal { M }$ is a non-Hausdorff 20-dimensional complex manifold with two isomorphic connected components interchanged by negating $\phi$ . The period map is ´etale and surjective.

For a period point $x \in \mathbb { D }$ , the vector space $( \mathbb { C } x \oplus \mathbb { C } \bar { x } ) \cap L _ { \mathbb { R } } \subset L _ { \mathbb { C } }$ is positive definite of rank 2 and its orthogonal complement $x ^ { \perp } \cap L _ { \mathbb { R } }$ has signature $( 1 , 1 9 )$ . Let

$$
\{ v \in x ^ { \perp } \cap L _ { \mathbb { R } } \mid v ^ { 2 } > 0 \} = P _ { x } \sqcup ( - P _ { x } )
$$

be the two connected components of the set of positive square vectors.
Then the fiber $\pi ^ { - 1 } ( x )$ is identified with the set of connected components $\boldsymbol { \mathscr { C } }$ of

$$
\left( P _ { x } \sqcup ( - P _ { x } ) \right) \setminus \cup _ { \delta } \delta ^ { \perp } { \mathrm { ~ f o r ~ } } \delta \in ( x ^ { \perp } \cap L ) _ { - 2 } .
$$

Namely, an open chamber $\boldsymbol { \mathscr { C } }$ is identified with the K¨ahler cone $\kappa _ { X }$ of the corresponding marked K3 surface $X$ via the marking $\phi$ . The connected components are permuted by the reflections and $\pm \mathrm { i d }$ , and $\pi ^ { - 1 } ( x )$ is a torsor under the group $\mathbb { Z } _ { 2 } \times W _ { x }$ , where $W _ { x } = W ( x ^ { \perp } \cap L )$ . Since $x ^ { \perp } \cap L _ { \mathbb { R } }$ is hyperbolic, the group and the fiber $\pi ^ { - 1 } ( x )$ may be infinite.
For a general point $x \in \mathbb { D }$ , the lattice $x ^ { \perp } \cap L$ has no roots and the fiber $\pi ^ { - 1 } ( x )$ consists of two points, one in each connected component of $\mathcal { M }$ .

2C. Moduli of $\rho$ -marked and $\rho$ -markable K3 surfaces with automorphisms.
Fix $\rho \in O ( L )$ an isometry of order $n > 1$ and consider a K3 surface $X$ with a nonsymplectic automorphism $\sigma$ of order $n$ .

Definition 2.2. A $\rho$ -marking of $( X , \sigma )$ is an isometry $\phi : H ^ { 2 } ( X , \mathbb { Z } ) \to L$ such that $\sigma ^ { * } = \phi ^ { - 1 } \circ \rho \circ \phi$ . We say that $( X , \sigma )$ is $\rho$ -markable if it admits a $\rho$ -marking.

A family of $\rho$ -marked surfaces is a smooth morphism $f \colon ( { \mathcal { X } } , \sigma _ { B } ) \to B$ with an automorphism $\sigma _ { B } \colon \mathcal X \to \mathcal X$ over $B$ , together with an isomorphism of local systems $\phi _ { S } \colon R ^ { 2 } f _ { * } \mathbb { Z } \to L \otimes \underline { { \mathbb { Z } } } _ { B }$ such that every fiber is a K3 surface with a $\rho$ -marking.
A family $f \colon ( { \mathcal { X } } , \sigma _ { B } ) \to B$ is $\rho$ -markable if such an isomorphism exists locally in complex-analytic topology on $B$ .

We define the moduli stacks $\mathcal { M } _ { \rho }$ of $\rho$ -marked, resp.
$F _ { \rho }$ of $\rho$ -markable K3 by taking $\mathcal { M } _ { \rho } ( B )$ , resp.
$F _ { \rho } ( B )$ to be the groupoids of such families over base $B$ .

Definition 2.3. Define $L _ { \mathbb { C } } ^ { \zeta _ { n } }$ to be the eigenspace $x \in L _ { \mathbb { C } }$ such that $\rho ( x ) = \zeta _ { n } x$ , and the subdomain $\mathbb { D } _ { \rho } = \mathbb { P } ( L _ { \mathbb { C } } ^ { \zeta _ { n } } ) \cap \mathbb { D } \subset \mathbb { D }$ . Define $\Gamma _ { \rho } \subset O ( L )$ as the group of changes-of-marking: $\Gamma _ { \rho } : = \{ \gamma \in O ( L ) \mid \gamma \circ \rho = \rho \circ \gamma \}$ .

Definition 2.4. Let the generic transcendental lattice $T _ { \rho } : = L _ { \mathbb { C } } ^ { \mathrm { p r i m } } \cap L$ be the intersection of $L$ with the sum of all primitive eigenspaces of $\rho$ , and let the generic Picard lattice be $S _ { \rho } = ( T _ { \rho } ) ^ { \perp }$ . Let $L ^ { G } = \operatorname { F i x } ( \rho ) \subset S _ { \rho }$ be classes in $L$ fixed by $\rho$ . (Here, we use $G = \langle \rho \rangle \simeq \mathbb { Z } _ { n }$ to avoid confusing notation, as $L ^ { G }$ would be.)

Note that the $\zeta _ { n }$ -eigenspaces $L _ { \mathbb { C } } ^ { \zeta _ { n } }$ and $T _ { \rho , \mathbb { C } } ^ { \zeta _ { n } }$ coincide, and that for any K3 surface with a $\rho$ -marking the two fixed sublattices $\phi \colon S _ { X } ^ { G } = H ^ { 2 } ( X , \mathbb { Z } ) ^ { G } \ \xrightarrow { \sim } \ L ^ { G }$ are identified.

For there to exist a $\rho$ -markable algebraic K3 surface, the signature of $T _ { \rho }$ must be $( 2 , \ell )$ for some $\ell$ , as there is necessarily a vector of positive norm fixed by $\sigma ^ { * }$ (the sum of a $\sigma ^ { * }$ -orbit of an ample class).
The converse is also true.

When $n = 2$ , we have that $\mathbb { D } _ { \rho } \subset \mathbb { P } ( T _ { \rho , \mathbb { C } } )$ is (two copies of) the Type IV domain associated to the lattice $T _ { \rho }$ . When $n \geq 3$ , the condition that $x \cdot x = 0$ is vacuous on $\mathbb { D } _ { \rho }$ because $x \cdot y = 0$ for eigenvectors $x , y$ of $\rho$ with non-conjugate eigenvalue.
Thus,

$$
\mathbb { D } _ { \rho } = \mathbb { P } \{ x \in T _ { \rho , \mathbb { C } } ^ { \zeta _ { n } } \mid x \cdot \bar { x } > 0 \}
$$

is a complex ball, a Type I domain.
The Hermitian form $x \cdot y$ on $T _ { \rho , \mathbb { C } } ^ { \zeta _ { n } }$ necessarily has signature $( 1 , \ell )$ for some for there to exist a $\rho$ -markable K3 surface.

Definition 2.5. The discriminant locus is $\Delta _ { \rho } : = ( \cup _ { \delta } \delta ^ { \perp } ) \cap \mathbb { D } _ { \rho }$ ranging over all roots $\delta$ in $( L ^ { G } ) ^ { \perp }$ .

Lemma 2.6. Let $\rho \in O ( L )$ be an isometry of order $n > 1$ . Then

(1) A marking $\phi \colon H ^ { 2 } ( X , \mathbb { Z } ) \to L$ defines a $\rho$ -marking, i.e. defines an automorphism $\sigma$ such that $\sigma ^ { * } = \phi ^ { - 1 } \circ \rho \circ \phi$ iff the period $x = \pi ( ( X , \phi ) )$ lies in $\mathbb { D } _ { \rho } \backslash \Delta _ { \rho }$ and there exists an ample line bundle $\mathcal { L } _ { h }$ on $X$ with $h = \phi ( \mathcal { L } _ { h } ) \in L ^ { G }$ .\
(2) For a point $x \in \mathbb { D } _ { \rho } \backslash \Delta _ { \rho }$ the set of $\rho$ -marked K3s with this period is a torsor over the group $\Gamma _ { \rho } \cap ( \mathbb { Z } _ { 2 } \times W _ { x } )$ .

Proof.
Because the action is nonsymplectic, $\rho ( x ) = \zeta _ { n } x \neq x$ . For any $h \in L ^ { G }$ one has $\rho ( h ) = h$ , which implies that $h x = 0$ . Thus, $L ^ { G } \perp x$ and $S _ { X } ^ { G } \simeq L ^ { G }$ .

Clearly, one must have $x \in \mathbb { D } _ { \rho }$ . By the Torelli theorem, automorphism $a =$ $\phi ^ { - 1 } \circ \rho \circ \phi$ of $H ^ { 2 } ( X , \mathbb { Z } )$ is induced by an automorphism $\sigma$ of $X$ iff it sends the K¨ahler cone $\chi _ { X }$ to itself.
By averaging, this is equivalent to having an $a$ -invariant K¨ahler class $\mathcal { L } _ { h } \in \mathcal { K } _ { X } \cap H ^ { 2 } ( X , \mathbb { Z } )$ . And since $L ^ { G } \perp x$ , one has $\mathcal { L } _ { h } ~ \perp ~ \omega _ { X }$ , so $\mathcal { L } _ { h } \in S _ { X }$ and $\mathcal { L } _ { h }$ is an ample line bundle.
This proves (1).

If $x \perp \delta$ for some root $\delta \in ( L ^ { G } ) ^ { \perp }$ then ${ \mathcal { L } } _ { \delta } = \phi ^ { - 1 } ( \delta ) \in \operatorname { P i c } ( X )$ and either $\mathcal { L } _ { \delta }$ or ${ \mathcal { L } } _ { \delta } ^ { - 1 }$ is effective.
Then for $\mathcal { L } _ { h }$ as in part (1) one has both $\mathcal { L } _ { h } \cdot \mathcal { L } _ { \delta } = 0$ because $h \perp \delta$ and $\mathcal { L } _ { h } \cdot \mathcal { L } _ { \delta } \ne 0$ because $\mathcal { L } _ { h }$ is ample.
Contradiction.

On the other hand, let $x \in \mathbb { D } _ { \rho } \backslash \Delta _ { \rho }$ . Then $L ^ { G } \not \subset \cup _ { \delta } \delta ^ { \bot }$ for $\delta \in ( x ^ { \perp } \cap L ) _ { - 2 }$ . Thus, there exists a chamber $c$ in $P _ { x } \setminus \cup _ { \delta } \delta ^ { \perp }$ such that ${ \mathcal { C } } \cap L ^ { G } \neq \emptyset$ . Let $( X , \phi )$ be the K3 surface corresponding to this chamber.
Then there exists $h \in \mathcal { C } \cap L ^ { G }$ and by part (1) the marking $\phi$ is a $\rho$ -marking.

Any surface with the same period $x$ is isomorphic to $X$ , but with a marking $\phi ^ { \prime } = g \circ \phi$ for some $g \in \mathbb { Z } _ { 2 } \times W _ { x }$ . Then one has both $\sigma ^ { * } = \phi ^ { - 1 } \circ \rho \circ \phi$ and $\sigma ^ { * } = ( \phi ^ { \prime } ) ^ { - 1 } \circ \rho \circ \phi ^ { \prime }$ iff $g \in \Gamma _ { \rho }$ . This proves (2). $\boxed { \begin{array} { r l } \end{array} }$

Lemma 2.7. There exists a fine moduli space $\mathcal { M } _ { \rho }$ of $\rho$ -marked $K \mathcal { 3 }$ surfaces with $a$ non-symplectic automorphism.
$\mathcal { M } _ { \rho }$ an open subset of $\pi ^ { - 1 } ( \mathbb { D } _ { \rho } \setminus \Delta _ { \rho } )$ .

Proof.
The points of $\mathcal { M }$ are chambers $\boldsymbol { \mathscr { C } }$ in Equation (1) over $x \in \mathbb { D } _ { \rho } \backslash \Delta _ { \rho }$ . As in the proof of Lemma 2.6, one has $\mathcal { C } \in \mathcal { M } _ { \rho }$ iff $\mathcal { C } \cap L ^ { G } \neq \emptyset$ . This is an open condition.
$\boxed { \begin{array} { r l } \end{array} }$

The restriction of $\pi \colon { \mathcal { M } }  \mathbb { D }$ gives the period map $\pi _ { \rho } \colon { \mathcal { M } } _ { \rho } \to { \mathbb { D } } _ { \rho } \setminus \Delta _ { \rho }$ . The general fiber of $^ { \prime \prime } \rho$ is a torsor over $\Gamma _ { \rho } \cap ( \mathbb { Z } _ { 2 } \times W ( S _ { \rho } ) )$ . Thus, $\mathcal { M } _ { \rho }$ is not separated iff there exists $x \in \mathbb { D } _ { \rho } \backslash \Delta _ { \rho }$ such that $\Gamma _ { \rho } \cap W _ { x } \supset \Gamma _ { \rho } \cap W ( S _ { \rho } )$ . This indeed happens:

Example 2.8. Consider the 9-dimensional family of $\mu _ { 3 }$ -covers of $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 }$ branched in a curve $B$ of bidegree $( 3 , 3 )$ , studied by Kond¯o [Kon02]. In this case,

$$
S _ { \rho } = L ^ { G } = \big ( \mathrm { P i c } ( \mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 } ) \big ) ( 3 ) = H ( 3 ) \quad \mathrm { a n d } \quad T _ { \rho } = ( L ^ { G } ) ^ { \perp } = H \oplus H ( 3 ) \oplus E _ { 8 } ^ { 2 } .
$$

Let $Y$ be a degeneration of the quadric $\mathbb { P } ^ { 1 } \times \mathbb { P } ^ { 1 } \subset \mathbb { P } ^ { 3 }$ to a quadratic cone and ${ \overline { { X } } } \to { \overline { { Y } } }$ be the $\mu _ { 3 }$ -cover branched in a curve $\overline { { B } } \in | \mathcal { O } _ { \overline { { Y } } } ( 3 ) |$ not passing through the apex.
Let $Y = \mathbb { F } _ { 2 }$ and $X$ be the minimal resolutions of $\overline { { Y } }$ and $\overline { { X } }$ . The $\mathbb { P } ^ { 1 }$ -fibration on $Y$ gives an elliptic fibration on $X$ , and the preimage of the $\left( - 2 \right)$ -section of $Y$ is a union of three disjoint $\left( - 2 \right)$ -sections $e$ , $\sigma e$ , $\sigma ^ { 2 } e$ on $X$ , interchanged by the automorphism $\sigma$ . The invariant sublattice $S _ { X } ^ { \sigma } = \big ( \mathrm { P i c } ( \mathbb { F } _ { 2 } ) \big ) ( 3 ) = H ( 3 )$ is generated by $f$ and $\begin{array} { r } { f ^ { \prime } = f + \sum _ { i = 0 } ^ { 2 } \sigma ^ { i } e } \end{array}$ .

The only $\left( - 2 \right)$ -curves on $X$ are $\sigma ^ { i } e$ and they do not lie in $( S _ { X } ^ { \sigma } ) ^ { \perp }$ . Thus, once we fix a marking $\phi$ , the period $x$ of $X$ will be in $\mathbb { D } _ { \rho } \setminus \Delta _ { \rho }$ . The reflections $w _ { i }$ in the roots $\rho ^ { i } \phi ( e )$ commute.
Their product $w = w _ { 0 } w _ { 1 } w _ { 2 }$ is non-trivial: on $L ^ { G }$ it acts as the reflection that interchanges $\phi ( f )$ and $\phi ( f ^ { \prime } )$ . It is easy to check that $w \in \Gamma _ { \rho }$ . So $\Gamma _ { \rho } \cap W _ { x } \neq 1$ and $W ( L ^ { G } ) = 1$ .

Thus, the map $\mathcal { M } _ { \rho } \to \mathbb { D } _ { \rho } \setminus \Delta _ { \rho }$ is not separated in this case.
Locally it looks like the “double-headed snake” $\mathbb { A } ^ { 1 } \cup _ { \mathbb { A } ^ { 1 } \backslash 0 } \mathbb { A } ^ { 1 }  \mathbb { A } ^ { 1 }$ times A8. Here is another way to see the same.
The positive cone $P$ in $H ( 3 ) _ { \mathbb { R } }$ is the unique Weyl chamber for the Weyl group $W \big ( H ( 3 ) \big ) = 1$ ; its rays are $\phi ( f )$ and $\phi ( f ^ { \prime } )$ . The hyperplane $\phi ( e ) ^ { \perp }$ cuts it in half.
The intersections of the Weyl chambers ${ \mathcal { C } } \subset P _ { x } \backslash \cup \delta ^ { \perp }$ of Equation 1 with $P$ are either halves of $P$ .

Theorem 2.9. The moduli stack $F _ { \rho }$ of $\rho$ -markable $K \mathcal { 3 }$ surfaces with a non-symplectic automorphism is the quotient $F _ { \rho } = \mathcal { M } _ { \rho } / \Gamma _ { \rho }$ . Its coarse moduli space admits a bijective period map to $( { \mathbb D } _ { \rho } \setminus \Delta _ { \rho } ) / \Gamma _ { \rho }$ , and the coarse moduli space of the separated quotient $F _ { \rho } ^ { \mathrm { s e p } }$ is $( { \mathbb D } _ { \rho } \setminus \Delta _ { \rho } ) / \Gamma _ { \rho }$ . The generic stabilizer is the group

$$
K _ { \rho } : = \ker ( \Gamma _ { \rho } \to \operatorname { A u t } ( \mathbb { D } _ { \rho } ) ) / \Gamma _ { \rho } \cap ( \mathbb { Z } _ { 2 } \times W ( S _ { \rho } ) )
$$

Proof.
The statement is immediate from the definitions and the above two Lemmas by quotienting the period map $\pi _ { \rho }$ . The points of $\pi _ { \rho } ^ { - 1 } ( x )$ are permuted by $\Gamma _ { \rho }$ , thus they are identified in the $\Gamma _ { \rho }$ -quotient.
They are also identified in the separated quotient.

For $\rho$ to correspond to any K3 surface with a nonsymplectic automorphism, $S _ { \rho }$ must have signature $( 1 , r - 1 )$ for some $r$ , and for $T _ { \rho }$ to have signature $( 2 , 2 0 - r )$ . The action of $\Gamma _ { \rho }$ on the Type IV domain $\mathbb { D } ( T _ { \rho } )$ factors through $O ( T _ { \rho } )$ and is therefore properly discontinuous.
Thus, the action of $\Gamma _ { \rho }$ on $\mathbb { D } _ { \rho }$ is properly discontinuous, and so $( { \mathbb D } _ { \rho } \backslash \Delta _ { \rho } ) / \Gamma _ { \rho }$ is makes sense as a complex-analytic space.
(It is also quasiprojective by Baily-Borel.)

The last statement follows from Lemma 2.6(2) by noting that for a generic $x \in$ ${ \mathbb D } _ { \rho } \setminus \Delta _ { \rho }$ one has $x ^ { \perp } \cap L = S _ { \rho }$ . 

Remark 2.10. The proof of part (1) of Lemma 2.6 and of Theorem 2.9 follow the arguments of Dolgachev-Kondo [DK07, Thms. 11.2, 11.3]. Sections 10 and 11 of [DK07] contain a construction of the moduli space of K3 surfaces with a nonsymplectic automorphism that is based on moduli of lattice polarized K3s. But it uses [Dol96, Thm. 3.1] which unfortunately is false, as was noted in [AE21] and as Example 2.8 also shows.
For this reason, we decided to give an alternative construction.

Remark 2.11. Even though the map to $( { \mathbb D } _ { \rho } \setminus \Delta _ { \rho } ) / \Gamma _ { \rho }$ in Theorem 2.9 is bijective, the coarse moduli space of $F _ { \rho }$ is a non-separated algebraic space when $\mathcal { M } _ { \rho }$ is not separated.
This is very similar to the algebraic space obtained by dividing a “twoheaded snake” $\mathbb { A } ^ { 1 } \cup _ { \mathbb { A } ^ { 1 } \backslash 0 } \mathbb { A } ^ { 1 }$ by the involution $z  - z$ exchanging the heads.
The quotient is a non-separated algebraic space with a bijection to $\mathbb { A } ^ { 1 } = \mathbb { A } ^ { 1 } / \pm$ .

We note that the separated quotient $F _ { \rho } ^ { \mathrm { s e p } }$ is a stack $[ \mathbb { D } _ { \rho } \setminus \Delta _ { \rho } : _ { W } \Gamma _ { \rho } ]$ which can be locally constructed near $x \in \mathbb { D } _ { \rho } \setminus \Delta _ { \rho }$ by first taking a coarse quotient by the normal subgroup $\Gamma _ { \rho } \cap ( \mathbb { Z } _ { 2 } \times W _ { x } ) \triangleleft \operatorname { S t a b } _ { x } ( \Gamma _ { \rho } )$ and then taking the stack quotient by $\operatorname { S t a b } _ { x } ( \Gamma _ { \rho } ) / \Gamma _ { \rho } \cap ( \mathbb { Z } _ { 2 } \times W _ { x } )$ . See [AE21, Rem. 2.36].

Proposition 2.12. Suppose $\sigma \in \operatorname { A u t } ( X )$ fixes a curve $R$ of genus at least 2, i.e.\
the assumption ( $\exists g \geq 2$ ) holds.
Then $\operatorname { A u t } ( X , \sigma )$ is finite.

Proof.
Let $h \in \operatorname { A u t } ( X , \sigma )$ be an automorphism of $X$ satisfying $h \circ \sigma = \sigma \circ h$ . Then $h$ permutes the fixed components of $\sigma$ . Since there is at most one component $R$ of genus $g \geq 2$ , we conclude $h ( R ) = R$ . Hence $h \in \operatorname { A u t } ( X , { \mathcal { O } } ( R ) )$ , a finite group.


Note that generic stabilizer $K _ { \rho }$ from Theorem 2.9 is never the trivial group, as $\rho \in K _ { \rho }$ is a nontrivial element.
As this is the automorphism group of a generic element $( X , \sigma ) \in F _ { \rho }$ , if ( $\exists g \geq 2$ ) holds then $K _ { \rho }$ is finite by Proposition 2.12.

Example 2.13. Consider the double cover $\pi \colon X  \mathbb { P } ^ { 2 }$ branched over a smooth sextic $B$ . There is a non-symplectic involution $\sigma$ switching the two sheets of $X$ , acting on $H ^ { 2 } ( X , \mathbb { Z } )$ by fixing $h = c _ { 1 } ( \pi ^ { * } { \mathcal { O } } ( 1 ) )$ and negating $h ^ { \perp }$ . Choosing a model $\rho$ for the action of $\sigma ^ { * }$ on cohomology, we have that $S _ { \rho } = \langle 2 \rangle$ and ${ \cal T } _ { \rho } = \langle - 2 \rangle \oplus { \cal H } ^ { \oplus 2 } \oplus$ $E _ { 8 } ^ { \oplus 2 }$ are the (+1)- and $( - 1 )$ -eigenspaces, respectively.

The divisor $\Delta _ { \rho } / \Gamma _ { \rho } \subset \mathbb { D } _ { \rho } / \Gamma _ { \rho } = F _ { 2 }$ has two irreducible components corresponding to $\Gamma _ { \rho }$ -orbits of roots $\delta \in \mathsf { \Gamma } ( T _ { \rho } ) _ { - 2 }$ . Such an orbit is uniquely determined by the divisibility (1 or 2) of $\delta \in T _ { \rho } ^ { * }$ . The case where the divisibility is 2 corresponds to when $B$ acquires a node.
Then there is an involution $\sigma$ on the minimal resolution of the double cover $X  \overline { { X } }  \mathbb { P } ^ { 2 }$ , but $\sigma ^ { * } ( \delta ) = \delta$ , $\sigma ^ { * } ( h ) = h$ and the $( + 1 , - 1 )$ - eigenspaces of $\sigma ^ { * }$ have dimensions $( 2 , 2 0 )$ . Thus, no $\rho$ -marking can be extended over a family $\mathcal { X }  \mathcal { C }$ with central fiber $X$ and general fiber as above.

When the divisibility of $\delta$ is $1$ , $\mathbb { P } ^ { 2 }$ degenerates to $\mathbb { F } _ { 4 } ^ { 0 } = \mathbb { P } ( 1 , 1 , 4 )$ and the minimal resolution of the double cover $X  \overline { { X } }  \mathbb { F } _ { 4 } ^ { 0 }$ is an elliptic K3 surface with $\sigma$ the elliptic involution.
Again the eigenspaces have dimension profile $( 2 , 2 0 )$ and so $( X , \sigma )$ is not $\rho$ -markable for the $\rho$ as above.

# 3. Stable pair compactifications

3A. Complete moduli of stable slc pairs.
We refer the reader to [ABE20, Sec. 2B] and [AE21, Sec. 7D] for a detailed discussion of stable K3 surface pairs and their compactified moduli.
Briefly:

Definition 3.1. In our context, a stable slc surface pair is a pair $( S , \epsilon D )$ , where

(1) $S$ is a connected, reduced, projective Gorenstein surface $S$ with $\omega _ { S } \simeq \mathcal { O } _ { S }$ which has semi log canonical singularities.\
(2) $D$ is an effective ample Cartier divisor on $S$ that does not contain any log canonical centers of $S$ .

Then for sufficiently small rational number $\epsilon > 0$ the pair $( S , \epsilon D )$ is stable, meaning:

(1) it has semi log canonical singularities, and (2) the $\mathbb { Q }$ -Cartier divisor $K _ { S } + \epsilon D$ is ample.

“Sufficiently small” works in families: for a fixed $D ^ { 2 }$ there exists $\epsilon _ { \mathrm { 0 } }$ so that if a pair $( S , \epsilon D )$ is stable in the above definition for some $\epsilon$ then it is stable for any $0 < \epsilon \le \epsilon _ { 0 }$ .

The main application to K3 surfaces is an observation that for any K3 surface $\overline { { X } }$ with ADE singularities and an effective ample divisor $\overline { { R } }$ , the pair $( { \overline { { X } } } , \epsilon { \overline { { R } } } )$ is stable.
Indeed, $\omega _ { \overline { { X } } } \simeq \mathcal { O } _ { \overline { { X } } }$ , the surface $X$ has canonical singularities—which is much better than semi log canonical—and there are no log centers.

As usual, let $F _ { 2 d }$ denote the moduli space of polarized K3 surfaces $( \overline { { X } } , \overline { { L } } )$ with ADE singularities and ample primitive line bundle $\overline { { L } }$ of degree $\overline { { L } } ^ { 2 } ~ = ~ 2 d$ , and $P _ { 2 d , m }  F _ { 2 d }$ denote the moduli space of pairs $( { \overline { { X } } } , \epsilon { \overline { { R } } } )$ with an effective divisor $\overline { { R } } \in | m \overline { { L } } |$ . Then the main result for K3 surfaces is the following:

Theorem 3.2. (1) For the stable pairs as above there exists an algebraic DeligneMumford moduli stack $\mathcal { M } ^ { \mathrm { s l c } }$ , with a coarse moduli space $M ^ { \mathrm { s l c } }$ .

(2) The closure P slc2d,m of P2d,m in M slc is projective and provides a compacti

To apply this result to a compactification of $F _ { \rho } ^ { \mathrm { s e p } }$ one needs to choose, in a canonical manner, a big and nef divisor on the generic $( X , \sigma ) \in F _ { \rho }$ .

Definition 3.3. A canonical choice of polarizing divisor is an algebraically varying big and nef divisor $R$ defined over a Zariski dense subset $U \subset F _ { \rho }$ of the moduli space of $\rho$ -markable K3 surfaces.

3B. Stable pair compactification of $F _ { \rho } ^ { \mathrm { s e p } }$ . We apply Theorem 3.2 to construct a stable pair compactification in the present context as follows.

Suppose that for each surface $( X , \sigma ) \in F _ { \rho }$ assumption ( $\exists g \ \geq 2$ ) holds, i.e. the fixed locus $\operatorname { F i x } ( \sigma )$ contains a component $C _ { 1 }$ of genus $g \geq 2$ , as well as possibly several smooth rational curves $C _ { i }$ and some isolated points.
In fact, it suffices that a single $( X , \sigma ) \in F _ { \rho }$ satisfies assumption ( $\exists g \geq 2$ ) because the genus of $C _ { 1 }$ is constant in a family of smooth K3 surfaces with non-symplectic automorphism.
So $R = C _ { 1 }$ gives a canonical choice of polarizing divisor for all of $U = F _ { \rho }$ .

Let $\pi \colon X \to X$ be the contraction to an ADE K3 surface such that the divisor ${ \overline { { R } } } : = \pi ( C _ { 1 } )$ is ample; it has degree $\overline { { R } } ^ { 2 } = 2 g ( C _ { 1 } ) - 2 > 0$ . It provides us with an ample divisor on $\overline { { X } }$ . If ${ \mathcal { O } } ( { \overline { { R } } } ) = { \overline { { L } } } ^ { m }$ for a primitive $\overline { { L } }$ then the pair $( { \overline { { X } } } , { \mathcal { O } } ( { \overline { { R } } } ) )$ is a point of $F _ { 2 d , m }$ and the pair $( { \overline { { X } } } , \epsilon { \overline { { R } } } )$ is a point of $P _ { 2 d , m }$ .

Definition 3.4. We define the map $\psi \colon F _ { \rho } \to P _ { 2 d , m }$ as follows.
Pointwise, it sends $( X , \sigma )$ to $( { \overline { { X } } } , \epsilon { \overline { { R } } } )$ . In every flat family $f \colon \mathcal { X }  S$ of K3 surfaces with automorphism, the sheaf ${ \mathcal { O } } _ { \mathcal { X } } ( { \mathcal { R } } )$ is relatively big and nef.
Since $R ^ { i } { \mathcal { L } } ^ { d } = 0$ for $i > 0$ , $d > 0$ , it gives a contraction to a flat family ${ \bar { f } } \colon ( { \overline { { \mathcal { X } } } } , { \overline { { \mathcal { R } } } } ) \to S$ . This induces the map on moduli.

Lemma 3.5. The map $\psi \colon F _ { \rho } \to P _ { 2 d , m }$ defined above induces an injective map $F _ { \rho } ^ { \mathrm { s e p } } \to \mathrm { i m } ( \psi )$ .

Proof.
The map $\psi$ factors through the separated quotient of $F _ { \rho }$ because $P _ { 2 d , m }$ is separated.
Now suppose there is an isomorphism of pairs ${ \overline { { f } } } \colon ( { \overline { { X } } } _ { 1 } , { \overline { { R } } } _ { 1 } ) \to ( { \overline { { X } } } _ { 2 } , { \overline { { R } } } _ { 2 } )$ inducing an isomorphism of the minimal resolutions $f \colon ( X _ { 1 } , R _ { 1 } ) \to ( X _ { 2 } , R _ { 2 } )$ . Consider the morphism $\varphi = \sigma _ { 1 } ^ { - 1 } f ^ { - 1 } \sigma _ { 2 } f$ . Then $\varphi$ is a symplectic automorphism of $X _ { 1 }$ fixing the curve $R _ { 1 }$ pointwise.
Since $\varphi$ preserves ${ \mathcal { O } } _ { X _ { 1 } } ( R _ { 1 } )$ , it has finite order.
By [Nik79a] the fixed set of a finite order symplectic K3 automorphism is finite.
Thus, $\varphi = \mathrm { i d }$ and $f$ preserves the group action.
So, $( X , \sigma )$ is uniquely determined by $( { \overline { { X } } } , { \overline { { R } } } )$ . $\boxed { \begin{array} { r l } \end{array} }$

Remark 3.6. $F _ { \rho } ^ { \mathrm { s e p } }$ itself has a moduli interpretation: It is the moduli space $F _ { \rho } ^ { \mathrm { a d e } }$ of $A D E$ K3 surfaces $( { \overline { { X } } } , { \overline { { \sigma } } } )$ with automorphism, for which $\operatorname { F i x } ( { \overline { { \sigma } } } )$ is ample, and for which the minimal resolution $( X , \sigma ) \to ( { \overline { { X } } } , { \overline { { \sigma } } } )$ is $\rho$ -markable.

Definition 3.7. Let $Z = \operatorname { i m } ( \psi )$ and let $\overline { { Z } }$ be its closure in $\overline { { P } } _ { 2 d , m } ^ { \mathrm { s l c } }$ , with reduced

$$
F _ { \rho } ^ { \mathrm { s e p } } = F _ { \rho } ^ { \mathrm { a d e } } \hookrightarrow { \overline { { F } } } _ { \rho } ^ { \mathrm { s l c } }
$$

is defined as the normalization of $\overline { Z }$ .

In particular, $\overline { { \boldsymbol F } } _ { \rho } ^ { \mathrm { s l c } }$ is normal by definition.
Points correspond to the pairs $( { \overline { { X } } } , \epsilon { \overline { { R } } } )$ , possibly degenerate, with some finite data.

3C. Kulikov degenerations of K3 surfaces.
A basic tool in the study of degenerations of K3 surfaces is Kulikov models.
We use them in the argument below, so we briefly recall the definition.

Let $( C , 0 )$ denote the germ of a smooth curve at a point $0 \in C$ and let $C ^ { * } = C \backslash 0$ . Let $X ^ { * } \to C ^ { * }$ be a family of algebraic K3 surfaces.

Definition 3.8. A Kulikov model $X \to ( C , 0 )$ is an extension of $X ^ { * } \to C ^ { * }$ for which $X$ is a smooth algebraic space, $K _ { X } \sim _ { C } 0$ , and $X _ { 0 }$ has reduced normal crossings.
We say the $X$ is Type I, $I I$ , or III, respectively, depending on whether $X _ { 0 }$ is smooth, has double curves but no triple points, or has triple points, respectively.
We call the central fiber $X _ { 0 }$ of such a family a Kulikov surface.

A key result on the degenerations of K3 surfaces is the theorem of Kulikov [Kul77] and Persson-Pinkham [PP81]:

Theorem 3.9. Let $Y ^ { * } \to C ^ { * }$ be a family of algebraic $K \mathcal { 3 }$ surfaces.
Then there is a finite base change $( C ^ { \prime } , 0 )  ( C , 0 )$ and a sequence of birational modifications of the pull back $Y ^ { \prime }  X$ such that $X$ has smooth total space, $K _ { X } \sim _ { C ^ { \prime } } 0$ , and $X _ { 0 }$ has reduced normal crossings.

We recall some fundamental results about Kulikov models.
The primary reference is [FS86]. Let $T : H ^ { 2 } ( X _ { t } , \mathbb { Z } )  H ^ { 2 } ( X _ { t } , \mathbb { Z } )$ denote the Picard-Lefschetz transformation associated to an oriented simple loop in $C ^ { * }$ enclosing 0. Since $X _ { 0 }$ is reduced normal crossings, $T$ is unipotent.
Let

$$
\begin{array} { r } { N : = \log T = ( T - I ) - \frac { 1 } { 2 } ( T - I ) ^ { 2 } + \cdot \cdot \cdot } \end{array}
$$

be the logarithm of the monodromy.

Theorem 3.10. [FS86][Fri84] Let $X \to ( C , 0 )$ be a Kulikov model.
We have that

if $X$ is Type $I$ , then $N = 0$ , if $X$ is Type $I I$ , then $N ^ { 2 } = 0$ but $N \neq 0$ , if $X$ is Type III, then $N ^ { 3 } = 0$ but $N ^ { 2 } \neq 0$

The logarithm of monodromy is integral, and of the form $N x = ( x \cdot \lambda ) \delta - ( x \cdot \delta ) \lambda$ for $\delta \in H ^ { 2 } ( X _ { t } , \mathbb { Z } )$ a primitive isotropic vector, and $\lambda \in \delta ^ { \perp } / \delta$ satisfying

$$
\lambda ^ { 2 } = \# \{ t r i p l e \ p o i n t s \ o f X _ { 0 } \} .
$$

When $\lambda ^ { 2 } = 0$ , its imprimitivity is the number of double curves of $X _ { 0 }$ .

Thus, the Types I, II, III of Kulikov model are distinguished by the behavior of the monodromy invariant $\lambda$ : either $\lambda = 0$ , $\lambda ^ { 2 } = 0$ but $\lambda \neq 0$ , or $\lambda ^ { 2 } \neq 0$ respectively.

Definition 3.11. Let $J \subset H ^ { 2 } ( X _ { t } , \mathbb { Z } )$ denote the primitive isotropic lattice $\mathbb { Z } \delta$ in Type III or the saturation of $\mathbb { Z } \delta \oplus \mathbb { Z } \lambda$ in Type II.

3D. Baily-Borel compactification.
Let $N$ be a lattice of signature $( 2 , \ell )$ , together with an isometry $\rho \in O ( N )$ of finite order $n$ , such that all eigenvalues of $\rho$ on $N _ { \mathbb { C } }$ are primitive $n$ th roots of unity, and $N _ { \mathbb { C } } ^ { \zeta _ { n } }$ contains a vector $x$ of positive Hermitian norm $x \cdot x$ . This is the situation which arises for a non-symplectic automorphism of an algebraic K3 surface, with $N = T _ { \rho }$ . Then we have a Type IV domain

$$
\mathbb { D } _ { N } = \mathbb { P } \{ x \in N _ { \mathbb { C } } \mid x \cdot x = 0 , ~ x \cdot { \bar { x } } > 0 \}
$$

For $n = 2$ one has $\mathbb { D } _ { \rho } = \mathbb { D } _ { N }$ . For $n > 2$ one has a Type I subdomain of $\mathbb { D } _ { N }$

$$
\mathbb { D } _ { \rho } = \mathbb { P } \{ x \in N _ { \mathbb { C } } ^ { \zeta _ { n } } \mid x \cdot \bar { x } > 0 \}
$$

$\mathbb { D } _ { \rho }$ admits the action of the arithmetic group $\widetilde \Gamma _ { \rho } : = \{ \gamma \in O ( N ) \mid \gamma \circ \rho = \rho \circ \gamma \}$ . Fix a finite index subgroup $\Gamma \subset \widetilde { \Gamma } _ { \rho }$ .

Recall that $\mathbb { D } _ { N }$ and $\mathbb { D } _ { \rho }$ embed into their compact duals $\mathbb { D } _ { N } ^ { c }$ , $\mathbb { D } _ { \rho } ^ { c }$ , which are defined by dropping the condition that $x \cdot \bar { x } > 0$ . Define $\overline { { \mathbb { D } } } _ { N } \subset \mathbb { D } _ { N } ^ { c }$ , $\overline { { \mathbb { D } } } _ { \rho } \subset \mathbb { D } _ { \rho } ^ { c }$ as their topological closures.
One has a well known description of the rational boundary components of $\mathbb { D } _ { N }$ , see e.g. see [Loo03b].

Definition 3.12. A rational boundary component of $\mathbb { D } _ { N }$ is an analytic subset $B _ { J } \subset \overline { { \mathbb { D } } } _ { N }$ of the form:

(1) $( \mathbb { P } J _ { \mathbb { C } } \setminus \mathbb { P } J _ { \mathbb { R } } ) \cap \overline { { \mathbb { D } } } _ { N }$ for $\operatorname { r k } J = 2$ a primitive isotropic sublattice of $N$ , (2) $\mathbb { P } J _ { \mathbb { C } } \cap \mathbb { D } _ { N }$ for $\operatorname { r k } J = 1$ a primitive isotropic sublattice of $N$ .

The rational boundary components of $\mathbb { D } _ { \rho }$ are intersections of $B _ { J } ^ { \prime } = B _ { J } \cap \mathbb { D } _ { \rho }$ .

One defines the rational closure of $\mathbb { D } _ { \rho }$ to be $\overline { { \mathbb { D } } } _ { \rho } ^ { \mathrm { b b } } : = \mathbb { D } _ { \rho } \cup _ { J } B _ { J } ^ { \prime }$ ,, topologized via a horoball topology at the boundary.
Then the Baily-Borel compactification of $\mathbb { D } _ { \rho } / \Gamma$ is (at least topologically) $\overline { { \mathbb { D } _ { \rho } / \Gamma } } ^ { \mathrm { b b } } : = \overline { { \mathbb { D } } } _ { \rho } ^ { \mathrm { b b } } / \Gamma$ .

The space $\overline { { \mathbb { D } _ { \rho } / \Gamma } } ^ { \mathrm { b b } }$ was shown to have the structure of a projective variety by Baily-Borel [BB66]. For Type IV domains $\mathbb { D } _ { N }$ and $\mathbb { D } _ { \rho }$ if $n = 2$ , the boundary components (1) are isomorphic to $\mathbb { H } \sqcup \left( - \mathbb { H } \right)$ and the boundary components (2) are points.
For $n > 2$ , the boundary components of the Type I domain $\mathbb { D } _ { \rho }$ are points.
If $\operatorname { r k } J = 2$ then a point $[ x ] \in B _ { J }$ corresponds to the elliptic curve $E _ { x } = J _ { \mathbb { C } } / ( J + \mathbb { C } x )$ .

Lemma 3.13. In the case $n > 2$ , for each boundary component $B _ { J } ^ { \prime }$ we necessarily have $\operatorname { r k } J = 2$ and $n \in \{ 3 , 4 , 6 \}$ , and $x \in B _ { J } ^ { \prime }$ corresponds to the elliptic curve with $j ( E _ { x } ) = 0$ if $n = 3$ or $_ 6$ , and with $j ( E _ { x } ) = 1 7 2 8$ if $n = 4$ .

Proof.
If $B _ { J } ^ { \prime }$ is boundary component of $\mathbb { D } _ { \rho }$ then $N _ { \mathbb { C } } ^ { \zeta _ { n } } \cap J _ { \mathbb { C } } \neq 0$ . Since $J$ is defined over $\mathbb { Z }$ and $\zeta _ { n } \notin \mathbb { R }$ , then $N _ { \mathbb { C } } ^ { \zeta _ { n } } \cap J _ { \mathbb { C } } \neq 0$ as well.
This implies that $\operatorname { r k } J = 2$ and

$$
J _ { \mathbb { C } } = J _ { \mathbb { C } } ^ { \zeta _ { n } } \oplus J _ { \mathbb { C } } ^ { \zeta _ { n } } .
$$

Thus, $\rho ( J _ { \mathbb { C } } ) = J _ { \mathbb { C } }$ , implying that $\rho ( J ) = J$ . Therefore $\rho \big | _ { J } \in \mathrm { G L } ( J ) \cong \mathrm { G L } _ { 2 } ( \mathbb { Z } )$ necessarily has order $n$ . Thus, $n \in \{ 3 , 4 , 6 \}$ . For a point $[ x ] \in B _ { J } ^ { \prime }$ one has $x \in N _ { \mathbb { C } } ^ { \zeta _ { n } }$ and $\mu _ { n } \subset \operatorname { A u t } ( E _ { x } )$ . This determines $E _ { x }$ . $\boxed { \begin{array} { r l } \end{array} }$

Corollary 3.14. If $n \neq 2 , 3 , 4 , 6$ then the rational closure of $\mathbb { D } _ { \rho }$ is simply $\mathbb { D } _ { \rho }$ itself.\
$S o \mathbb { D } _ { \rho } / \Gamma$ is already compact.

The following is a well-known consequence of Schmid’s nilpotent orbit theorem:

Proposition 3.15. Let $X ^ { * } \to C ^ { * }$ be a degeneration of a $\rho$ -markable $K \mathcal { 3 }$ surfaces over a punctured analytic disk $C ^ { * }$ . $A$ lift of the period mapping $\widetilde { C ^ { * } } \cong \mathbb { H }  \mathbb { D } _ { \rho }$ approaches the Baily-Borel cusp $B _ { J }$ as $\operatorname { I m } ( \tau )  \infty$ , where $J$ is the monodromy lattice in $H ^ { 2 } ( X _ { t } , \mathbb { Z } )$ , cf.
Definition 3.11. When $\operatorname { r k } ( J ) = 2$ , the limiting point $x \in B _ { J }$ corresponds to an elliptic curve $E _ { x }$ isomorphic to any double curve of the central fiber $X _ { 0 }$ of a Kulikov model $X  C$ .

Corollary 3.16. If $n \neq 2 , 3 , 4 , 6$ , any degeneration of $( X , \sigma ) \in F _ { \rho }$ has Type I. If $n \in \{ 3 , 4 , 6 \}$ , any degeneration of $( X , \sigma ) \in F _ { \rho }$ has Type $I$ or $I I$ .

The last statement was also proved by Matsumoto [Mat16] using different techniques.
His proof also holds in some prime characteristics.

3E. Semitoroidal compactifications.
Semitoroidal compactifications of arithmetic quotients $\mathbb { D } / \Gamma$ for type IV Hermitian symmetric domains $\mathbb { D }$ were defined by Looijenga [Loo03b] (where they were called “semitoric”). They simultaneously generalize toroidal and Baily-Borel compactifications of $\mathbb { D } / \Gamma$ . The case of the complex ball $\mathbb { D }$ (a type I symmetric Hermitian domain) is comparatively trivial.
The semitoroidal compactifications in this case are implicit in [Loo03a, Loo03b]. We quickly overview the construction in both cases now.

Definition 3.17. A $\Gamma$ -admissible semifan $\mathfrak { F }$ consists of the following data:

When $n = 2$ , it is a convex, rational, locally polyhedral decomposition $\mathfrak { F } \mathrm { { J } }$ of the rational closure ${ \mathcal { C } } ^ { + } ( J ^ { \perp } / J )$ of the positive norm vectors, for all rank 1 primitive isotropic sublattices $J \subset N$ , such that:

(1) $\{ \mathfrak { F } \mathrm { { J } } \} _ { J \subset N }$ is $\Gamma$ -invariant.
In particular, a fixed $\mathfrak { F } \mathrm { { J } }$ is invariant under the natural action of $\mathrm { S t a b } _ { J } ( \Gamma )$ on ${ \mathcal { C } } ^ { + } ( J ^ { \perp } / J )$ .\
(2) A compatibility condition of the $\{ \mathfrak { F } \mathrm { { J } } \} _ { J \subset N }$ along any primitive isotropic lattice $J ^ { \prime } \subset N$ of rank 2 holds, see Definition 3.18.

When $n > 2$ , the data is much simpler: It consists, for each primitive isotropic sublattice $J \subset N$ satisfying $J _ { \mathbb { C } } \cap N _ { \mathbb { C } } ^ { \zeta _ { n } } \neq \emptyset$ , of a primitive sublattice $\mathfrak { F } _ { J } \subset J ^ { \perp } / J$ such that the collection $\{ \mathfrak { F } _ { J } \}$ is $\Gamma$ -invariant.

Definition 3.18. Let $J ^ { \prime } \subset N$ be primitive isotropic of rank 2. We say that the collection $\{ \mathfrak { F } \mathrm { \mathcal { I } } \} \mathrm { \mathcal { I } } \mathrm { \subset } \mathrm { N }$ is compatible along $J ^ { \prime }$ if, given any primitive sublattice $J \subset J ^ { \prime }$ of rank 1, the kernel of the hyperplanes of $\mathfrak { F } \mathrm { { J } }$ containing $J ^ { \prime } / J$ , when intersected with $( J ^ { \prime } ) ^ { \bot } / J \subset J ^ { \bot } / J$ and then descended to $( J ^ { \prime } ) ^ { \bot } / J ^ { \prime }$ , cut out a fixed sublattice $\mathfrak { F } _ { J ^ { \prime } } \subset ( J ^ { \prime } ) ^ { \perp } / J ^ { \prime }$ which is independent of $J$ .

In both the $n = 2$ and $n > 2$ cases, we use the same notation $\mathfrak { F } : = \{ \mathfrak { F } \mathrm { \mathcal { I } } \} _ { J \subset N }$ even though $J$ ranges over rank 1 isotropic sublattices when $n = 2$ and ranges over rank 2 isotropic sublattices when $n > 2$ .

In the Type IV case, Looijenga constructs a compactification $\mathbb { D } / \Gamma \hookrightarrow \overline { { \mathbb { D } / \Gamma } } ^ { \tilde { s } }$ for any $\Gamma$ -admissible semifan $\tilde { \mathfrak { s } }$ , so consider the Type I case.
By Lemma 3.13 we may restrict to $n \in \{ 3 , 4 , 6 \}$ . There is a $\mathbb { Z } [ \zeta _ { n } ]$ -lattice

$$
Q : = ( N \otimes _ { \mathbb { Z } } \mathbb { Z } [ \zeta _ { n } ] ) ^ { \zeta _ { n } } \subset N _ { \mathbb { C } } ^ { \zeta _ { n } } = Q _ { \mathbb { C } }
$$

on which Hermitian form $x \cdot y$ defines a $\mathbb { Z } [ \zeta _ { n } ]$ -valued Hermitian pairing of signature $( 1 , \ell )$ for some $\ell$ . Any element of $\widetilde { \Gamma } _ { \rho }$ (in particular, any element of $\Gamma$ ) preserves $Q$ and the Hermitian form on it.
The converse also holds.
Thus $\Gamma \subset U ( Q )$ is a finite index subgroup of the group of unitary isometries of $Q$ and $\Gamma _ { \mathbb { R } } = U ( Q _ { \mathbb { C } } ) = U ( 1 , \ell )$ . The boundary components $B _ { J } = \mathbb { P } ( J _ { \mathbb { C } } ^ { \zeta _ { n } } )$ are then projectivizations of the isotropic $\mathbb { Z } [ \zeta _ { n } ]$ -lines $K \subset Q$ . Here $K _ { \mathbb { C } } = J _ { \mathbb { C } } ^ { \zeta _ { n } }$ .

Choose a generator $k \in K$ . Then any $[ x ] \in \mathbb { D } _ { \rho } \subset \mathbb { P } Q _ { \mathbb { C } }$ has a unique representative $x \in Q _ { \mathbb { C } }$ for which $k \cdot x = 1$ . This realizes $\mathbb { D } _ { \rho }$ as a generalized tube domain in the affine hyperplane $V _ { k } : = \{ k \cdot x = 1 \} \subset Q _ { \mathbb { C } }$ .

Let $U _ { K } \subset \operatorname { S t a b } _ { K } ( \Gamma )$ be the unipotent subgroup (i.e. $U _ { K }$ acts on $K$ , $K ^ { \perp } / K$ , and $Q / K ^ { \perp }$ by the identity).
Then $U _ { K }$ acts on $V _ { k }$ by translations.
Choosing some isotropic $k ^ { \prime } \in Q _ { \mathbb { C } }$ for which $k ^ { \prime } \cdot k = 1$ , any element $x \in V _ { k }$ can be written uniquely as $x = k ^ { \prime } + x _ { 0 } + c k$ for some $x _ { 0 } \in \{ k , k ^ { \prime } \} ^ { \perp }$ and $c \in \mathbb { C }$ . The image of $\mathbb { D } _ { \rho }$ is exactly those $x$ satisfying $2 \mathrm { R e } ( c ) > - x _ { 0 } \cdot \bar { x } _ { 0 }$ .

The fibration $\mathbb { D } _ { \rho } \to K _ { \mathbb { C } } ^ { \perp } / K _ { \mathbb { C } }$ sending $x \mapsto x _ { 0 }$ mod $K _ { \mathbb { C } }$ is a fibration of right half-planes.
The action of $U _ { K }$ fibers over the action of a translation subgroup ${ \overline { { U } } } _ { K } \subset K ^ { \perp } / K$ on $K _ { \mathbb { C } } ^ { \bot } / K _ { \mathbb { C } }$ and thus, there is a fibration

$$
\mathbb { D } _ { \rho } / U _ { K } \to ( K _ { \mathbb { C } } ^ { \perp } / K _ { \mathbb { C } } ) / \overline { { U } } _ { K } = : A _ { K }
$$

over an abelian variety.
The fibers are quotients of the right half-planes with coordinate $c$ by a discrete, purely imaginary, translation group isomorphic to $\mathbb { Z }$ . This realizes $\mathbb { D } _ { \rho } / U _ { K }$ is a punctured holomorphic disc bundle over $A _ { K }$ .

Definition 3.19. $\mathbb { D } _ { \rho } / U _ { K }$ is the first partial quotient associated to the Baily-Borel cusp $K$ . The extension of this punctured disc bundle to a disc bundle $\overline { { \mathbb { D } _ { \rho } / U _ { K } } } ^ { \mathrm { c a n } } \to$ $A _ { K }$ for a given $K$ is called the toroidal extension at the cusp $K$ .

We will identify the divisor at infinity, i.e. the zero section of the disc bundle, with $A _ { K }$ itself.

Construction 3.20. The toroidal compactification of $\mathbb { D } _ { \rho } / \Gamma$ is constructed as follows: Let $\Gamma _ { K }$ be the finite group defined by the exact sequence

$$
0 \to U _ { K } \to \operatorname { S t a b } _ { K } ( \Gamma ) \to \Gamma _ { K } \to 0 .
$$

For each cusp $K$ , quotient the toroidal extension

$$
V _ { K } : = \overline { { \mathbb { D } _ { \rho } / U _ { K } } } ^ { \mathrm { c a n } } / \Gamma _ { K } \supset \mathbb { D } _ { \rho } / \mathrm { S t a b } _ { K } ( \Gamma ) .
$$

A well-known theorem states that there exists a horoball neighborhood $\mathbb { P } K _ { \mathbb { C } } ~ \in$ $N _ { K } \subset \mathbb { D } _ { \rho } ^ { \mathrm { b b } }$ such that $( N _ { K } \setminus \mathbb { P } K _ { \mathbb { C } } ) / { \operatorname { S t a b } _ { K } ( \Gamma ) } \hookrightarrow \mathbb { D } _ { \rho } / \Gamma$ injects.
Thus, we can glue a neighborhood of the boundary $A _ { K } / \Gamma _ { K } \subset V _ { K }$ to $\mathbb { D } _ { \rho } / \Gamma$ , ranging over all $\Gamma$ -orbits of cusps $K$ . The result is the toroidal compactification $\overline { { \mathbb { D } _ { \rho } / \Gamma } } ^ { \mathrm { t o r } }$

The boundary divisors of $\overline { { \mathbb { D } _ { \rho } / \Gamma } } ^ { \mathrm { t o r } }$ are in bijection with $\Gamma$ -orbits of isotropic $\mathbb { Z } [ \zeta _ { n } ]$ - lines $K \subset Q$ and the boundary divisor is isomorphic to $A _ { K } / \Gamma _ { K }$ , where $\Gamma _ { K }$ acts by a subgroup of the finite group $U ( K ^ { \perp } / K )$ . There is a morphism

$$
\overline { { \mathbb { D } _ { \rho } / \Gamma } } ^ { \mathrm { t o r } } \to \overline { { \mathbb { D } _ { \rho } / \Gamma } } ^ { \mathrm { b b } }
$$

which contracts each boundary divisor to a point.
As such, the normal bundle of the boundary divisor is anti-ample.
Passing to a finite index subgroup $\Gamma _ { 0 } \subset \Gamma$ , we can assume that $\Gamma _ { K }$ is trivial for all cusps $K$ and the anti-ampleness still holds.
This proves that the normal bundle to $A _ { K } \subset \overline { { \mathbb { D } _ { \rho } / U _ { K } } } ^ { \mathrm { c a n } }$ in the first partial quotient is anti-ample.

Using [Gra62] one shows that a divisor in a smooth analytic space, isomorphic to an abelian variety and with anti-ample normal bundle, can be contracted along any abelian subvariety.
In particular, for any sub- $\mathbb { Z } [ \zeta _ { n } ]$ -lattice $\mathfrak { F } _ { K } \subset K ^ { \perp } / K$ , there is a contraction

$$
\overline { { \mathbb { D } _ { \rho } / U _ { K } } } ^ { \mathrm { c a n } } \to \overline { { \mathbb { D } _ { \rho } / U _ { K } } } ^ { \mathfrak { F } _ { \ K } }
$$

which is an isomorphism away from the boundary divisor and contracts exactly the translates of the abelian subvariety $\mathrm { i m } ( \mathfrak { F } _ { K } ) _ { \mathbb { C } } \subset A _ { K }$ .

cu $K$ nstruct the semitoroidal compactifica a punctured analytic open neighborho $\overline { { \mathbb { D } _ { \rho } / \Gamma } } ^ { \mathfrak { F } }$ ish try of $\overline { { \mathbb { D } _ { \rho } / U _ { K } } } ^ { \mathfrak { F } _ { K } } / \Gamma _ { K }$ $\mathbb { D } _ { \rho } / \Gamma$ $\Gamma _ { K }$ $\overline { { \mathbb { D } _ { \rho } / U _ { K } } } ^ { \mathrm { c a n } }$ above contraction.
The condition in Definition 3.17 ensures that the collection $\mathfrak { F } = \{ \mathfrak { F } \kappa \}$ is $\Gamma$ -invariant.
So an individual $\mathfrak { F } _ { K }$ is $\Gamma _ { K }$ -invariant and the $\Gamma _ { K }$ action descends.
Thus, we have constructed the semitoroidal compactification.

Remark 3.21. A feature of the construction is that one can pull back a semifan $\tilde { s }$ for a Type IV domain to any Type I subdomain, and there will be a morphism between the corresponding semitoric compactifications.

3F. Recognizable divisors.
We recall the main new concept “recognizability” introduced in [AE21]. We slightly modify the definition as necessary for moduli spaces of K3 surfaces with $\rho$ -markable automorphism:

Definition 3.22. A canonical choice of polarizing divisor $R$ for $U \subset F _ { \rho }$ is recognizable if for every Kulikov surface $X _ { 0 }$ of Type I, II, or III which smooths to some $\rho$ -markable K3 surface, there is a divisor $R _ { 0 } ~ \subset ~ X _ { 0 }$ such that on any smoothing into $\rho$ -markable K3 surfaces $X \to ( C , 0 )$ with $C ^ { * } \subset U$ , the divisor $R _ { 0 }$ is, up to the action of $\mathrm { A u t } ^ { 0 } ( X _ { 0 } )$ , the flat limit of $R _ { t }$ for $t \neq 0 \in C ^ { * }$ .

We use the term “smoothing” to mean specifically a Kulikov model $X \to ( C , 0 )$ . Roughly, Definition 3.22 amounts to saying that the canonical choice $R$ can also be made on any Kulikov surface, including smooth K3s.

Theorem 3.23. If R is recognizable, then F slcρ is semitoroidal compactification of $F _ { \rho }$ for a unique semifan $\mathfrak { F } _ { R }$ .

Proof.
The proof when $n = 2$ is essentially the same as [AE21, Thm. 1.2]. So we anyways.
First, we show that restrict our attention to the Type I case $\overline { { \boldsymbol F } } _ { \rho } ^ { \mathrm { s l c } }$ contains $n > 2$ $\mathbb { D } _ { \rho } / \Gamma _ { \rho }$ , which is ultimately much simpler .

Let $\mathcal { M } _ { \rho } ^ { \ast }$ be the closure of the moduli space of $\rho$ -marked K3 surfaces $\mathcal { M } _ { \rho }$ in the space of all marked K3 surfaces $\mathcal { M }$ and let $F _ { \rho } ^ { * } = \mathcal { M } _ { \rho } ^ { * } / \Gamma _ { \rho }$ be the quotient.
Given any smooth K3 surface $X _ { 0 } \in \ F _ { \rho } ^ { * } \setminus U$ , the recognizability implies that the universal family $( { \mathcal { X } } ^ { * } , { \mathcal { R } } ^ { * } ) \to U$ extends over $F _ { \rho } ^ { \ast }$ by the same argument as [AE21, Prop. 6.3]. Thus, the argument of Lemma 3.5 shows that there is a morphism $( F _ { \rho } ^ { * } ) ^ { \mathrm { s e p } } = \mathbb { D } _ { \rho } / \Gamma _ { \rho } \to P _ { 2 d , m }$ and so we may as well have constructed $\overline { { \boldsymbol F } } _ { \rho } ^ { \mathrm { s l c } }$ by taking the normalization of the closure of the image of $\mathbb { D } _ { \rho } / \Gamma _ { \rho }$ , which is notably already normal.
This completes the proof when $n \neq 3 , 4 , 6$ .

So let $\mathbb { P } K _ { \mathbb { C } }$ be a Baily-Borel cusp of $\mathbb { D } _ { \rho }$ when $n \in \{ 3 , 4 , 6 \}$ . We observe that the closure of $\mathbb { D } _ { \rho } / U _ { K }$ in the toroidal extension $\mathbb { D } ( J ) \subset \mathbb { D } ( J ) ^ { \lambda }$ of the “universal” first partial quotient for unpolarized K3 surfaces, cf.
[AE21, Def. 4.18], is simply the first partial quotient $\overline { { \mathbb { D } _ { \rho } / U _ { K } } } ^ { \mathrm { c a n } }$ . [AE21, Prop. 4.16] shows that $\mathbb { D } ( J )$ embeds into a family of affine lines over $J ^ { \perp } / J \otimes _ { \mathbb { Z } } \tilde { \mathcal { E } }$ where $\tilde { \mathcal { E } }$ is the universal elliptic curve over $\mathbb { H } \sqcup \left( - \mathbb { H } \right)$ and $\mathbb { D } ( J ) ^ { \lambda }$ is its closure in a projective line bundle.
The space $\mathbb { D } _ { \rho } / U _ { K }$ sits inside this affine line bundle as the inverse image of

$$
K ^ { \perp \mathrm { i n } Q } / K \otimes _ { \mathbb { Z } [ \zeta _ { n } ] } E \subset J ^ { \perp } / J \otimes _ { \mathbb { Z } } \widetilde { \mathcal { E } }
$$

where $E$ is the elliptic curve admitting an action of $\zeta _ { n }$ (note that $K = J$ but with the additional structure of a $\mathbb { Z } [ \zeta _ { n } ]$ -lattice).

Thus we may restrict a Type II $\lambda$ -family, cf.
[AE21, Def. 5.34], to a family

$$
\chi \to \overline { { \mathbb { D } _ { \rho } / U _ { K } } } ^ { \mathrm { c a n } }
$$

of Kulikov surfaces of Types $1 + 1 1$ . We call $\mathcal { X }$ a $K$ -family.
Note that any $K$ -family admits a birational automorphism which is the action of the automorphism $\sigma$ on the restriction of $\mathcal { X }$ to $( \mathbb { D } _ { \rho } \setminus \Delta _ { \rho } ) / U _ { K }$ .

The arguments in [AE21, Secs. $6 , 8 ]$ , leading up to the proof of Theorem 1.2 of loc.
cit.
now all apply to $K$ -families $\mathcal { X }$ , showing that there is a sandwich of normal compactifications

$$
\overline { { \mathbb { D } _ { \rho } / \Gamma _ { \rho } } } ^ { \mathrm { t o r } } \to \overline { { F } } _ { \rho } ^ { \mathrm { s l c } } \to \overline { { \mathbb { D } _ { \rho } / \Gamma _ { \rho } } } ^ { \mathrm { b b } } .
$$

Using that the normal image of an abelian variety is an abelian variety (a similar argument is used in [AE21, Thm. 7.18]), we conclude that there must exist a $\Gamma _ { \rho }$ - admissible semifan FR for which F slcρ $\overline { { F } } _ { \rho } ^ { \mathrm { s l c } } = \overline { { \mathbb { D } _ { \rho } / \Gamma _ { \rho } } } ^ { \mathfrak { F } _ { \mathrm { R } } }$ . 

# 3G.

The main theorem.

Theorem 3.24. Under the assumption ( $\exists g \geq 2$ ), $R = C _ { 1 }$ is recognizable for $F _ { \rho }$ The stable pair compactification F slcρ i s a semitoroidal compactification of $\mathbb { D } _ { \rho } / \Gamma _ { \rho }$ .

Proof.
By Theorem 3.23, the second statement follows from the first.
Let $( X , R ) \to$ $( C , 0 )$ be a Kulikov model with a flat family of divisors $R \subset X$ for which

(1) there is an automorphism $\sigma$ on $X ^ { * } \to C ^ { * }$ making $( X _ { t } , \sigma _ { t } ) \in F _ { \rho }$ for $t \neq 0$ , (2) $R _ { t } \subset { \mathrm { F i x } } ( \sigma _ { t } )$ is the fixed component of genus at least 2 for $t \neq 0$ , and (3) $R _ { 0 } = \operatorname* { l i m } _ { t  0 } R _ { t }$ .

By [AE21, Prop. 6.12], it suffices to show that if we make a one-parameter deformation the smoothing of $X _ { 0 }$ into $F _ { \rho }$ that keeps $X _ { 0 }$ constant, the limiting curve $R _ { 0 }$ does not deform, up to $\mathrm { A u t } ^ { 0 } ( X _ { 0 } )$ .

The automorphism $\sigma$ on the generic fiber of any smoothing defines a birational automorphism of $X$ . Any two Kulikov models are related by an automorphism followed by a sequence of Atiyah flops of types $0$ , I, $\amalg$ along curves in $X _ { 0 }$ which are either $\left( - 2 \right)$ -curves or $( - 1 )$ -curves on component(s) of $X _ { 0 }$ . As such, there are only countably many curves in $X _ { 0 }$ along which it is possible to make an Atiyah flop, and this continues to be the case after a flop is made.
Thus, up to conjugation by $\mathrm { A u t } ^ { 0 } ( X _ { 0 } )$ , there are only countably many possibilities for the birational automorphism $\sigma _ { 0 } : = \sigma | _ { X _ { 0 } } \colon X _ { 0 } \to X _ { 0 }$ .

Hence if $X _ { 0 } ~ \hookrightarrow ~ X$ and $X _ { 0 } ~ \hookrightarrow ~ \tilde { X }$ are smoothings into $F _ { \rho }$ as above, we have $\widetilde { \sigma } _ { 0 } = \psi \circ \sigma _ { 0 } \circ \psi ^ { - 1 }$ for some $\psi \in \operatorname { A u t } ^ { 0 } ( X _ { 0 } )$ .

Let $\{ A _ { j } \}$ be the countable set of curves in $X _ { 0 }$ along which $\sigma _ { 0 }$ can be indeterminate.
Any such curve $A _ { j }$ is $\mathrm { A u t } ^ { 0 } ( X _ { 0 } )$ -invariant.
Let $A = \cup _ { j } A _ { j }$ be their union.
Clearly, the limit divisor $R _ { 0 }$ is contained in the union of $A \cup S$ where $S$ is the closure of the fixed locus of $\sigma _ { 0 }$ in its locus of determinacy.
Similarly, $\widetilde { R } _ { 0 }$ is contained in $A \cup \widetilde { S }$ and $\sigma _ { 0 } ( P ) = P$ if and only if $\widetilde { \sigma } _ { 0 } ( \psi ( P ) ) = \psi ( P )$ . Since the smoothing $\tilde { X }$ is a deformation of the smoothing $X$ eand the limiting divisor of $R$ varies continuously, we conclude that ${ \cal \tilde { R } } _ { 0 } = \psi ( { \cal R } _ { 0 } )$ and therefore $R$ is recognizable.


Proposition 3.25. Any element $( \overline { { X } } , \epsilon \overline { { R } } ) \in \overline { { F } } _ { \rho } ^ { \mathrm { s l c } }$ has an automorphism ${ \overline { { \sigma } } } \in \operatorname { A u t } ( { \overline { { X } } } )$ Furthermore, $\overline { { R } } = \operatorname { F i x } ( \overline { \sigma } )$ and $\overline { { \sigma } } ^ { \ast }$ acts on $H ^ { 0 } ( \overline { { X } } , \omega _ { \overline { { X } } } ) \cong \mathbb { C }$ by multiplication by $\zeta _ { n }$ .

Proof.
As noted in Remark 3.6, any point in $F _ { \rho } ^ { \mathrm { s e p } } = ( \mathbb { D } _ { \rho } \setminus \Delta _ { \rho } ) / \Gamma _ { \rho }$ corresponds to a pair $( { \overline { { X } } } , { \overline { { \sigma } } } )$ of an ADE K3 surface with automorphism, for which $\overline { { R } } = \operatorname { F i x } ( \overline { { \sigma } } )$ is ample and the minimal resolution is $( \overline { { X } } _ { 0 } , \epsilon \overline { { R } } _ { 0 } ) \in \overline { { F } } _ { \rho } ^ { \mathrm { s l c } }$ is a stable limit of such $\rho$ -markable.
Then any boundary point DE K3 surface pairs $f \colon ( \overline { { X } } , \epsilon \overline { { R } } )  C$ .

Since $R _ { t }$ is $\overline { { \sigma } } _ { t }$ -invariant and the canonical model is unique, $\overline { { X } }$ admits an automorphism $\overline { { \sigma } }$ whose fixed locus contains $\overline { { R } } _ { 0 }$ . In fact, $\operatorname { F i x } ( { \overline { { \sigma } } } _ { 0 } ) = { \overline { { R } } } _ { 0 }$ : $\operatorname { F i x } ( { \overline { { \sigma } } } )$ is a

Cartier divisor, and thus forms a flat family of divisors containing $\overline { { R } }$ . But $\operatorname { F i x } ( { \overline { { \sigma } } } _ { 0 } )$ already contains the flat limit $R _ { 0 }$ . The statement about $\omega _ { \overline { { X } } _ { 0 } }$ follows from the fact that $f _ { * } \omega _ { \overline { { X } } / C }$ is invertible (by Base Change and Cohomology, since $R ^ { 1 } f _ { * } \omega _ { \overline { { X } } / C } = 0 ,$ ) and $\overline { { \sigma } } _ { t } ^ { \ast }$ acts by $\zeta _ { n }$ on the generic fiber of this line bundle.


# 4. Moduli of quotient surfaces

We refer the reader to [Kol13] for the notions appearing in the following definitions.
The pair $( Y , \Delta )$ is called demi-normal if $X$ satisfies Serre’s $S _ { 2 }$ condition, has double normal crossing singularities in codimension 1, and $\Delta = \sum d _ { i } D _ { i }$ is an effective Weil $\mathbb { Q }$ -divisor with $0 < d _ { i } \le 1$ not containing any components of the double crossing locus of $Y$ .

The following is [Kol13, Prop. 2.50(4)], using our adopted notations.

Proposition 4.1. Etale locally, there is a one-to-one correspondence between ´

(a) Local demi-normal pairs $\textstyle ( y \in Y , { \frac { n - 1 } { n } } B )$ of index $n$ , i.e. such that the divisor $n K _ { Y } + ( n - 1 ) B$ is Cartier.\
(b) Local demi-normal pairs ( $\widetilde y \in \widetilde Y )$ ) such that $K _ { \widetilde { Y } }$ is Cartier, with a $\mu _ { n }$ -action e ethat is free on a dense open subset, and such that the induced action on $\omega _ { \widetilde { Y } } \otimes \mathbb { C } ( \widetilde { y } )$ is faithful.

Moreover, the pair $( Y , { \frac { n - 1 } { n } } B )$ is slc iff so is $\widetilde { Y }$ .

The variety $\widetilde { Y }$ is called the local index-1 cover of the pair $( Y , { \frac { n - 1 } { n } } B )$ . [Kol13, Sec. 2] also gives a global construction.

Theorem 4.2. Let (X, R) ∈ F slcρ and let $\pi \colon { \overline { { X } } } \to Y = { \overline { { X } } } / \mu _ { n }$ be the quotient map with the branch divisor $B = f ( { \overline { { R } } } )$ . Then

(1) $n K _ { Y } + ( n - 1 ) B \sim 0$ ,\
(2) $B$ and $- K _ { Y }$ are ample $\mathbb { Q }$ -Cartier divisors,\
(3) the pair singulari $( Y , \frac { n - 1 + \epsilon } { n } B )$ s stable-divisor al is $0 < \epsilon \ll 1$ , i.e. it has slc $\mathbb { Q }$ $\begin{array} { r } { K _ { Y } + \frac { n - 1 + \epsilon } { n } B } \end{array}$

Vice versa, for a pair $( Y , B )$ satisfying the above conditions, its index-1 cover $\overline { { X } }$ with the ramification divisor $\overline { { R } }$ satisfies:

(1) $K _ { \overline { { X } } } \sim 0$ and the $\mu _ { n }$ -action on $\overline { { X } }$ is non-symplectic, (2) $\overline { { R } }$ is $\mathbb { Q }$ -Cartier, (3) the pair $( { \overline { { X } } } , \epsilon { \overline { { R } } } )$ is stable for any rational $0 < \epsilon \ll 1$

Proof.
Follows from the above Proposition 4.1 and the formulas

$$
\pi ^ { * } ( B ) = n \overline { { { R } } } , \qquad \pi ^ { * } \left( K _ { Y } + \frac { n - 1 + \epsilon } { n } B \right) = K _ { \overline { { X } } } + \epsilon \overline { { { R } } } .
$$

Corollary 4.3. The coarse moduli space F slcρ coincides with the normalization of the KSBA compactification of the irreducible component in the moduli space of the log canonical pairs $( Y , \frac { n - 1 + \epsilon } { n } B )$ of log del Pezzo surfaces $Y$ with $( n - 1 ) B \in | - n K _ { Y } |$ in which a generic surface is a quotient of a $K \mathcal { 3 }$ surface with a non-symplectic automorphism of type $\rho$ . The stack for the former is a $\mu _ { n }$ -gerbe over the stack for the latter.

For the proof, we note that a small deformation of a K3 surface is a K3 surface.

Example 4.4. The KSBA compactification moduli of K3 surfaces of degree 2 for the ramification divisor $R$ constructed in [AET19] is equivalent to the Hacking’s compactification [Hac04] of the moduli space of pairs $( { \mathbb { P } } ^ { 2 } , { \frac { 1 + \epsilon } { 2 } } B _ { 6 } )$ of plane sextic curves.

# 5. Extensions

The results of this paper are easily extended to the case of a nonsymplectic action by an arbitrary finite group $G$ and to more general divisors defined by group actions.
Most of the changes amount to introducing more cumbersome notations.

# 5A.

A general nonsymplectic group of automorphisms.

Definition 5.1. Let $X$ be a smooth K3 surface and $\sigma \colon G \subset \operatorname { A u t } X$ be a finite symmetry group.
The action of $G$ on $H ^ { 2 , 0 } ( X ) = \mathbb { C } \omega _ { X }$ gives the exact sequence

$$
0 \to G _ { 0 } \to G { \overset { \alpha } { \to } } \mu _ { n } \to 1 , \qquad \mu _ { n } \subset \mathbb { C } ^ { * } .
$$

One says that $G$ is nonsymplectic (or not purely symplectic) if $G \neq G _ { 0 }$ , i.e. $\alpha \neq 1$

We now extend the results of Section 2 directly to this more general setting.

Definition 5.2. Fix a finite subgroup $\rho \colon G \to O ( L )$ and a nontrivial character $\chi \colon G \ \to \ \mathbb { C } ^ { * }$ . Let $X , \sigma \colon G \ \to \ \operatorname { A u t } X \rangle$ ) be a K3 surface with a non-symplectic automorphism group.

A $( \rho , \chi )$ -marking of $( X , \sigma )$ is an isometry $\phi : H ^ { 2 } ( X , \mathbb { Z } ) \to L$ such that for any $g \in G$ one has $\phi \circ \sigma ( g ) ^ { * } = \rho ( g ) \circ \phi$ and such that the character $\alpha \colon G \to \mathbb { C } ^ { * }$ induced by $\sigma$ coincides with $\chi$ . We say that $( X , \sigma )$ is $\rho$ -markable if it admits a $\rho$ -marking.

A family of $( \rho , \chi )$ -marked K3 surfaces is a smooth family $f \colon ( \mathcal { X } , \sigma _ { B } , \phi _ { B } ) \ $ $B$ with a group of automorphisms $\sigma _ { B } \colon G \ \to \ \operatorname { A u t } ( { \mathcal { X } } / B )$ and with a marking $\phi _ { B } \colon R ^ { 2 } f _ { * } \mathbb { Z } \to L \otimes \underline { { \mathbb { Z } } } _ { B }$ such that every fiber is a $( \rho , \chi )$ -marked K3 surface.

A family of smooth $\rho$ -markable K3 surfaces is a family $f \colon ( { \mathcal { X } } , \sigma _ { B } ) \to B$ of K3 surfaces with a group of automorphisms over base $B$ which admits a $\rho$ -marking locally on $B$ .

We define the moduli stacks ${ \mathcal M } _ { \rho , \chi }$ of $( \rho , \chi )$ -marked, resp.
$F _ { \rho , \chi }$ of $( \rho , \chi )$ -markable K3 by taking $\mathcal { M } _ { \rho , \chi } ( B )$ , resp.
$F _ { \rho , \chi } ( B )$ to be the groupoids of such families over $B$ .

Definition 5.3. Define the vector space

$$
L _ { \mathbb { C } } ^ { \rho , \chi } = \{ x \in L _ { \mathbb { C } } \mid \rho ( g ) ( x ) = \chi ( g ) x \}
$$

to be the intersection of the eigenspaces for the individual $g \in G$ , and the period domain as

$$
\mathbb { D } _ { \rho , \chi } = \mathbb { P } \{ x \in L _ { \mathbb { C } } ^ { \rho , \chi } \mid x \cdot \bar { x } > 0 \}
$$

The second condition is redundant if there exists $g \in G$ with $\chi ( g ) > 2$ . Thus, $\mathbb { D } _ { \rho }$ is a type IV domain if $| \chi ( G ) | = 2$ and a complex ball, a type I domain if $| \chi ( G ) | > 2$ .

The discriminant locus is $\Delta _ { \rho } : = \cup _ { \delta } \delta ^ { \perp } \cap \Delta _ { \rho }$ ranging over all roots $\delta$ in $( L ^ { G } ) ^ { \perp }$ , where $L ^ { G } = \{ a \in L \mid \rho ( g ) ( a ) = a \}$ is the sublattice of $L$ fixed by $G$ .

Definition 5.4. The group of changes-of-marking is

$$
\Gamma _ { \rho } : = \{ \gamma \in O ( L ) \mid \gamma \circ \rho = \rho \circ \gamma \} .
$$

Then the direct analogue of Lemma 2.6 and Theorem 2.9 is

Theorem 5.5. For a fixed finite group $\rho \colon G \to O ( L )$ with a nontrivial character $\chi \colon G \to \mathbb { C } ^ { * }$ :

(1) There exists a fine moduli space ${ \mathcal M } _ { \rho , \chi }$ of $( \rho , \chi )$ -marked $K \mathcal { 3 }$ surfaces $( X , \sigma , \phi )$ . It admits an ´etale period map $\pi _ { \rho } \colon { \mathcal { M } } _ { \rho , \chi } \to { \mathbb { D } } _ { \rho , \chi } \backslash \Delta _ { \rho }$ . The fiber $\pi _ { \rho } ^ { - 1 } ( x )$ over a point $x \in \mathbb { D } _ { \rho , \chi } \setminus \Delta _ { \rho }$ is a torsor over $\Gamma _ { \rho } \cap ( \mathbb { Z } _ { 2 } \cap W _ { x } )$ .\
(2) The moduli stack of $\rho$ -markable $K \mathcal { 3 }$ surfaces $( X , \sigma )$ is obtained as a quotient of $F _ { \rho , \chi }$ by $\Gamma _ { \rho }$ . On the level of coarse moduli spaces it admits a bijective map to $( \mathbb { D } _ { \rho , \chi } \setminus \Delta _ { \rho } ) / \Gamma _ { \rho }$ .

Proof.
If the group $G$ does not act purely symplectically, i.e. there exists $g \in G$ with $\rho ( g ) ( x ) \neq x$ then $L ^ { G } \perp x$ and $S _ { X } ^ { G } \simeq L ^ { G }$ . The rest of the proof of Lemma 2.6 works the same for any finite group.
And the proof of Theorem 2.9 goes through verbatim.


5B. More general polarizing divisors.
With a more general group action, there are more choices for the polarizing divisors.
For a generic K3 surface $X$ with a period $x \in \mathbb { D } _ { \rho , \chi } \setminus \Delta _ { \rho }$ we can consider any combination $\sum b _ { i } B _ { i }$ of curves $B _ { i }$ which are either fixed by some element $g \in G$ or are some of the $\left( - 2 \right)$ -curves corresponding to the roots in the generic Picard lattice $( L _ { \mathbb { C } } ^ { \rho , \chi } ) ^ { \perp } \cap L$ that generically gives a big and nef divisor on $X$ . Theorem 3.24 extends immediately to this situation with the same proof.

# References

[ABE20] Valery Alexeev, Adrian Brunyate, and Philip Engel, Compactifications of moduli of elliptic $K \mathcal { S }$ surfaces: stable pair and toroidal, Geom.
and Topology, to appear (2020), arXiv:2002.07127.\
[AE21] Valery Alexeev and Philip Engel, Compact moduli of K3 surfaces, Submitted (2021), arXiv:2101.12186.\
[AET19] Valery Alexeev, Philip Engel, and Alan Thompson, Stable pair compactification of moduli of K3 surfaces of degree 2, arXiv:1903.09742.\
[AS08] Michela Artebani and Alessandra Sarti, Non-symplectic automorphisms of order 3 on $_ { K 3 }$ surfaces, Math.
Ann.
342 (2008), no. 4, 903–921.\
[AS15] Symmetries of order four on K3 surfaces, J. Math.
Soc.
Japan 67 (2015), no. 2, 503–533.\
[ast85] G´eom´etrie des surfaces $_ { K 3 }$ : modules et p´eriodes, Soci´et´e Math´ematique de France, Paris, 1985, Papers from the seminar held in Palaiseau, October 1981–January 1982, Ast´erisque No. 126 (1985).\
[AST11] Michela Artebani, Alessandra Sarti, and Shingo Taki, $_ { K 3 }$ surfaces with non-symplectic automorphisms of prime order, Math.
Z. 268 (2011), no. 1-2, 507–533, With an appendix by Shigeyuki Kond¯o.\
[BB66] W. L. Baily, Jr. and A. Borel, Compactification of arithmetic quotients of bounded symmetric domains, Ann.
of Math.
(2) 84 (1966), 442–528.\
[DH22] Anand Deopurkar and Changho Han, Stable quadrics, admissible covers, and Kond¯o’s sextic K3 surfaces, In preparation, 2022.\
[Dil09] Jimmy Dillies, Order 6 non-symplectic automorphisms of K3 surfaces, arXiv:0912.5228 (2009).\
[Dil12] , On some order 6 non-symplectic automorphisms of elliptic K3 surfaces, Albanian J. Math.
6 (2012), no. 2, 103–114.\
[DK07] Igor V. Dolgachev and Shigeyuki Kond¯o, Moduli of $_ { K 3 }$ surfaces and complex ball quotients, Arithmetic and geometry around hypergeometric functions, Progr.
Math., vol. 260, Birkh¨auser, Basel, 2007, pp. 43–100.\
[Dol96] I. V. Dolgachev, Mirror symmetry for lattice polarized K3 surfaces, J. Math.
Sci.
81 (1996), no. 3, 2599–2630, Algebraic geometry, 4.\
[Fri84] Robert Friedman, A new proof of the global Torelli theorem for K3 surfaces, Ann.
of Math.
(2) 120 (1984), no. 2, 237–269.\
[FS86] Robert Friedman and Francesco Scattone, Type III degenerations of K3 surfaces, Invent.
Math.
83 (1986), no. 1, 1–39.\
[Gra62] Hans Grauert, Uber Modifikationen und exzeptionelle analytische Mengen ¨ , Math.
Ann.
146 (1962), 331–368.\
[Hac04] P. Hacking, Compact moduli of plane curves, Duke Math.
J. 124 (2004), no. 2, 213–257.\
[Kol13] J´anos Koll´ar, Singularities of the minimal model program, Cambridge Tracts in Mathematics, vol. 200, Cambridge University Press, Cambridge, 2013, With a collaboration of S´andor Kov´acs.\
[Kol21] Families of varieties of general type, To appear, 2021, availabe at https://web.math.princeton.edu/ $\sim$ kollar/.\
[Kon02] Shigeyuki Kond¯o, The moduli space of curves of genus 4 and Deligne-Mostow’s complex reflection groups, Algebraic geometry 2000, Azumino (Hotaka), Adv.
Stud.
Pure Math., vol. 36, Math.
Soc.
Japan, Tokyo, 2002, pp. 383–400.\
[Kon20] Shigeyuki Kond¯o, K3 surfaces, vol. 32, EMS Tracts in Mathematics, 2020.\
[Kul77] Vik.
S. Kulikov, Degenerations of $_ { K 3 }$ surfaces and Enriques surfaces, Izv.
Akad.
Nauk SSSR Ser.
Mat.
41 (1977), no. 5, 1008–1042, 1199.\
[Loo03a] Eduard Looijenga, Compactifications defined by arrangements.
I. The ball quotient case, Duke Math.
J. 118 (2003), no. 1, 151–187.\
[Loo03b] Compactifications defined by arrangements.
II. Locally symmetric varieties of type IV, Duke Math.
J. 119 (2003), no. 3, 527–588.\
[Mat16] Yuya Matsumoto, Degeneration of K3 surfaces with non-symplectic automorphisms, arXiv:1612.07569 (2016).\
[MO98] Natsumi Machida and Keiji Oguiso, On K3 surfaces admitting finite non-symplectic group actions, J. Math.
Sci.
Univ. Tokyo 5 (1998), no. 2, 273–297.\
[Nik79a] V. V. Nikulin, Finite groups of automorphisms of K¨ahlerian K3 surfaces, Trudy Moskov.
Mat.
Obshch.
38 (1979), 75–137.\
[Nik79b] Integer symmetric bilinear forms and some of their geometric applications, Izv.
Akad.
Nauk SSSR Ser.
Mat.
43 (1979), no. 1, 111–177, 238.\
[PP81] Ulf Persson and Henry Pinkham, Degeneration of surfaces with trivial canonical bundle, Ann.
of Math.
(2) 113 (1981), no. 1, 45–66.\
[PSS71] I. I. Pjatecki˘ı-Shapiro and I. R. Shafareviˇc, Torelli’s theorem for algebraic surfaces of type K3, Izv.
Akad.
Nauk SSSR Ser.
Mat.
35 (1971), 530–572.

Email address: mailto:valery@uga.edu

Email address: mailto:philip.engel@uga.edu

Email address: mailto:changho.han@uga.edu

Department of Mathematics, University of Georgia, Athens GA 30602, USA
