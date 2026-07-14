---
title: The Period Lattice for Enriques Surfaces
authors:
- Allcock
year: 1999
bibkey: Allcock99
tags:
- paper
- extraction
abstract: |
  
---

# The Period Lattice for Enriques Surfaces

Daniel Allcock\*  
allcock@math.harvard.edu  
14 May 1999  
MSC: 14J28 (11F55, 11E12)

It is well-known that the isomorphism classes of complex Enriques surfaces are in 1-1 correspondence with a Zariski-open subset $( \mathcal { D } - H ) / \Gamma$ of the quotient of the Hermitian symmetric space $\mathcal { D }$ for $O ( 2 , 1 0 )$ .
Here $H$ is a totally geodesic divisor in $\mathcal { D }$ and $\Gamma$ is a certain arithmetic group.
In the usual formulation of this result [5], $\Gamma$ is described as the isometry group of a certain integral lattice $N$ of signature $( 2 , 1 0 )$ .
This lattice is quite complicated, and requires sophisticated techniques to work with.
The purpose of this note is to replace $N$ by the much simpler lattice $I _ { 2 , 1 0 }$ , the unique odd unimodular lattice of signature $( 2 , 1 0 )$ .
This allows for dramatic simplifications in several arguments concerning $N$ , replacing intricate analysis by elementary facts.
For example, in this setting it is easy to see that $H / \Gamma \subseteq { \mathcal { D } } / \Gamma$ is irreducible, and also easy to enumerate the boundary components in the Satake compactification of $\mathrm { { \mathcal { D } / \Gamma } }$ .
Using $I _ { 2 , 1 0 }$ in place of $N$ also allows one to show that $( \mathcal { D } - H ) / \Gamma$ has contractible universal cover.
The last of these results is new, and the full proof appears in [1]; here we only give the main idea.
The basis of this paper is a lattice-theoretic trick which is well-known to those who work with lattices; however, its applications in this setting do not appear to have been published before.

We review some notation and facts from [5].
$U$ denotes the two-dimensional lattice with inner product matrix $\textstyle { \binom { 0 } { 1 } } \left( { 1 \atop 0 } \right)$ .
If $A$ is a lattice then $A ( n )$ denotes a copy of $A$ with all inner products multiplied by $n$ .
An Enriques surface $S$ has fundamental group $\mathbb { Z } / 2$ and its universal cover $\tilde { S }$ is a K3 surface.
The covering transformation $\boldsymbol { \imath }$ acts on $L = H ^ { 2 } ( \tilde { S } , \mathbb { Z } ) \cong E _ { 8 } ( - 1 ) ^ { 2 } \oplus U ^ { 3 }$ , and its fixed lattice $M$ is primitive in $L$ and isomorphic to $E _ { 8 } ( - 2 ) \oplus U ( 2 )$ .
It turns out that $N = M ^ { \perp }$ is isomorphic to $E _ { 8 } ( - 2 ) \oplus U ( 2 ) \oplus U$ .
There is a holomorphic 2-form $\omega$ on $\tilde { S }$ , unique up to a multiplicative constant, and it satisfies $\iota ( \omega ) = - \omega$ .
This implies that as an element of $H ^ { 2 } ( S , \mathbb { C } ) = L \otimes \mathbb { C }$ , it lies in $N \otimes \mathbb { C }$ .
Furthermore, $\omega$ satisfies the equality $\langle \omega | \omega \rangle = 0$ and the inequality $\langle \omega | \bar { \omega } \rangle > 0$ , where $\langle \mid \rangle$ denotes the usual bilinear form on $H ^ { 2 } ( S , \mathbb { C } )$ .

We write $K$ for a fixed copy of $E _ { 8 } ( - 2 ) \oplus U ( 2 ) \oplus U$ ; by isometrically identifying $N$ with $K$ we may regard $\omega$ as defining an element of $K \otimes \mathbb { C }$ .
The isometry group of $K \otimes \mathbb { R }$ is isomorphic to $O ( 2 , 1 0 )$ , and we write $\mathcal { D }$ for the Hermitian symmetric space for this group.
A concrete model for $\mathcal { D }$ is the set of points in the complex projective space $P ( K \otimes \mathbb { C } )$ with a representative vector $v$ satisfying $\langle v | v \rangle = 0$ and $\langle v | \bar { v } \rangle > 0$ .
That is, under our identification of $N$ with $K$ we may regard $\omega$ as defining an element of $\mathcal { D }$ .
This element depends on the choice of identification, but the point of $\mathcal { D } / \Gamma$ defined by $\omega$ does not, where $\Gamma = \mathrm { A u t } \ : K$ .

The Torelli theorem for Enriques surfaces asserts that the map assigning to $S$ the point of $\mathcal { D } / \Gamma$ represented by $\omega$ is a bijection from the the set of isomorphism classes of Enriques surfaces onto a certain Zariski-open subset $\mathcal { D } _ { 0 } / \Gamma$ of $\mathcal { D } / \Gamma$ .
This map is called the period map.
The subset $\mathcal { D } _ { 0 }$ is $\mathcal { D } - H$ , where $H = \cup _ { \ell } H _ { \ell }$ , $\ell$ varies over the vectors of $K$ of norm $\langle \ell | \ell \rangle = - 2$ , and $H _ { \ell }$ denotes the set of points of $\mathcal { D }$ represented by vectors orthogonal to $\ell$ .

Our purpose is to restate the Torelli theorem in terms of the simpler (in particular, unimodular) lattice $I _ { 2 , 1 0 }$ .
For $p , m \geq 0$ we write $I _ { p , m }$ for the lattice with an orthogonal basis of $p + m$ vectors, $p$ of which have norm $+ 1$ and $m$ of which have norm $- 1$ .
If $p , m > 0$ then $I _ { p , m }$ is the unique odd unimodular lattice of signature $( p , m )$ .
For $p , m > 0$ and $p - m \equiv 0$ (mod 8) we write $I I _ { p , m }$ for the unique even unimodular lattice of signature $( p , m )$ .
This may be described as a direct sum of various copies of $E _ { 8 }$ , $E _ { 8 } ( - 1 )$ and $U$ ; in particular, $I I _ { 1 , 1 } \cong U$ .
The $I _ { p , m }$ and $I I _ { p , m }$ account for all the indefinite unimodular lattices.

Lemma 1. If $B$ is even and unimodular and $A \cong B ( 2 ) \oplus I I _ { 1 , 1 }$ , then there is a lattice $\hat { A }$ in $A \otimes \mathbb { R }$ isometric to $B \oplus I _ { 1 , 1 }$ such that every isometry of $A$ preserves $\hat { A }$ and vice-versa.
In particular, $\operatorname { A u t } ( B ( 2 ) \oplus I I _ { 1 , 1 } ) \cong \operatorname { A u t } ( B \oplus I _ { 1 , 1 } )$ .

Proof: One can check that $( 2 ^ { - 1 / 2 } A ) ^ { * } \cong B \oplus I I _ { 1 , 1 } ( 2 )$ lies in a unique odd unimodular lattice, which we take to be $\hat { A }$ .
Here the asterisk denotes the dual lattice.
By its oddness, unimodularity, and indefiniteness, $\hat { A }$ must be isometric to $B \oplus I _ { 1 , 1 }$ .
One can recover $A$ from $\hat { A }$ as $2 ^ { 1 / 2 } \cdot ( \hat { A } ^ { e } ) ^ { * }$ where $\hat { A } ^ { e }$ is the even sublattice of $\hat { A }$ .
The intrinsic nature of these constructions makes it clear that any isometry of $A$ or $\hat { A }$ preserves the other.
□

Applying the lemma to $K = E _ { 8 } ( - 2 ) \oplus U ( 2 ) \oplus U \cong I I _ { 1 , 9 } ( 2 ) \oplus I I _ { 1 , 1 }$ , we find that ${ \hat { K } } \cong I I _ { 1 , 9 } \oplus I _ { 1 , 1 } \cong$ $I _ { 2 , 1 0 }$ .
This yields our version of the Torelli theorem:

Theorem 2. The period map establishes a bijection between the isomorphism classes of Enriques surfaces and the points of $( \mathcal { D } - H ) / \Gamma$ , where $\Gamma = \mathrm { A u t } \hat { K }$ and $H$ is the divisor $\cup _ { \ell } H _ { \ell }$ with $\ell$ varying over the vectors of $\hat { K }$ of norm $- 1$ .

Proof: Applying the lemma we see that $\operatorname { A u t } K = \operatorname { A u t } { \hat { K } }$ .
The fact that the description of $H$ given here coincides with the one given earlier follows from the fact that the norm $- 2$ vectors of $K$ correspond bijectively with the norm $- 1$ vectors of $\hat { K }$ .
(Formally, we say that a primitive vector of $K$ and a primitive vector of $\hat { K }$ correspond to each other if they differ by a positive real scalar.) Then our statement of the Torelli theorem follows from that of Namikawa ([5], thm.
1.14), where all the hard work is actually done.
□

Although the lattice $K$ is more closely related to the geometry of Enriques surfaces than $\hat { K }$ is, using $\hat { K }$ offers some significant advantages.
We will illustrate this with several examples.
We will $( i )$ show that $H / \Gamma$ is an irreducible divisor in $\mathcal { D } / \mathcal { H }$ , $( i i )$ enumerate the boundary components of the Satake compactification $\overline { { \mathcal { D } / \Gamma } }$ , and $( i i i )$ indicate the proof of the fact that the universal (orbifold) covering space of $\mathcal { D } _ { 0 } / \Gamma$ is contractible.

Corollary 3. $H / \Gamma$ is an irreducible divisor of $\mathcal { D } / \Gamma$ .

Proof: This follows from the transitivity of $\operatorname { A u t } \hat { K }$ on the norm $^ { - 1 }$ vectors of $\hat { K }$ .
This in turn follows from the fact that the orthogonal complement in $\hat { K }$ of such a vector can only be a copy of $I _ { 2 , 9 }$ , since it is unimodular of signature $( 2 , 9 )$ .
Given two norm $- 1$ vectors of $\hat { K }$ it is now easy to construct an isometry of $\hat { K }$ carrying one to the other.
□

Corollary 3 was left open by Horikawa [4], and Namikawa ([5], thm.
2.13) proved it only by relying on a deep theorem of Nikulin.
Borcherds [2] has found an elementary but still somewhat involved proof (see the remark after his lemma 2.3).

Corollary 4. There are two orbits of primitive isotropic vectors $v$ in $\hat { K }$ , one with $v ^ { \perp } / \langle v \rangle \cong I _ { 1 , 9 }$ and one with $v ^ { \perp } / \langle v \rangle \cong I I _ { 1 , 9 }$ ; these correspond to the two 0-dimensional boundary components of $\overline { { \mathcal { D } / \Gamma } }$ .
There are two orbits of 2-dimensional primitive isotropic sublattices $V$ in $\hat { K }$ , one with $V ^ { \perp } / V \cong E _ { 8 } ( - 1 )$ and one with $V ^ { \perp } / V \cong I _ { 0 , 8 }$ ; these correspond to the two 1-dimensional boundary components of $\overline { { \mathcal { D } / \Gamma } }$ .

Proof: The Satake compactification is defined in terms of the isotropic sublattices of $\hat { K }$ , so it suffices to prove the transitivity claims.
It is well-known that when $p , m > 0$ , the orbits of primitive isotropic vectors in $I _ { p , m }$ are in 1-1 correspondence with the isomorphism classes of unimodular lattices of signature $( p - 1 , m - 1 )$ .
The lattice corresponding to a vector $v$ is $v ^ { \perp } / \langle v \rangle$ .
The first claim of the theorem follows because any unimodular lattice of signature $( 1 , 9 )$ is equivalent to either $I _ { 1 , 9 }$ or $I I _ { 1 , 9 }$ .
We say that $\boldsymbol { v }$ is odd or even in these cases, respectively.

Now consider a primitive 2-dimensional isotropic sublattice $V$ of $\hat { K }$ .
We claim first that $V$ contains an odd vector.
For otherwise it contains an even vector $v$ , so that $v ^ { \perp } / \langle v \rangle \cong I I _ { 1 , 9 }$ .
It is easy to find a sublattice $A \cong I I _ { 1 , 9 }$ of $v ^ { \perp }$ complementary to $\langle v \rangle$ .
Since $\hat { K }$ is odd, $A ^ { \perp } \cong I _ { 1 , 1 }$ .
Taking a primitive vector $w$ of $A \cap V$ we see that $w ^ { \perp }$ contains a copy of $I _ { 1 , 1 }$ , so that $w ^ { \perp } / \langle w \rangle$ is odd, so that $w$ is odd.
We have shown that $V$ contains an odd vector $w$ .
Next, consider the orbits of such pairs $( V , w )$ .
These are in 1-1 correspondence with orbits of pairs $( w , W )$ where $w$ is as before and $W$ is a 1-dimensional primitive isotropic lattice in $w ^ { \perp } / \langle w \rangle$ .
Since $w ^ { \perp } / \langle w \rangle \cong I _ { 1 , 9 }$ , there are exactly two possibilities for $W$ (up to isometry), corresponding to the unimodular lattices of signature $( 0 , 8 )$ .
In these two cases, $V ^ { \perp } / V \cong I _ { 0 , 8 }$ or $E _ { 8 } ( - 1 )$ .
Since there are only two orbits of pairs $( w , W )$ , there are two orbits of pairs $( V , w )$ , so there are at most two orbits of sublattices $V$ .
The corollary follows.

Corollary 4 was first proven by Sterk in [7], props.
4.5–4.6, using $K$ instead of $\hat { K }$ .
He relied on an intricate analysis of the orthogonal group of $K$ and also of a certain subgroup of finite index. He went much further than we have done, by making a detailed study of the boundary of the Satake compactification of the quotient of $\mathcal { D }$ by this subgroup.

Corollary 5. The universal cover of $\mathcal { D } _ { 0 }$ is contractible, as is the universal orbifold cover of $\mathcal { D } _ { 0 } / \Gamma$

Proof sketch: Since $\mathcal { D } _ { 0 }$ is an orbifold cover of $\mathrm { \mathcal { D } _ { 0 } / \Gamma }$ , the second claim follows from the first.
The first claim is proven in [1]; the idea is to show that the metric completion of the universal cover of $\mathcal { D } _ { 0 }$ is a metric space with non-positive curvature (in a suitable sense).
The essential ingredient in the proof is that the various components of $H$ meet orthogonally wherever they meet.
It is easy to see this in terms of $\hat { K }$ : if the components $H _ { r }$ and $H _ { s }$ of $H$ meet, where $r$ and $s$ are norm $- 1$ vectors of $\hat { K }$ , then $r$ and $s$ span a negative-definite sublattice of $\hat { K }$ .
Therefore $\langle r | s \rangle ^ { 2 } < \langle r | r \rangle \langle s | s \rangle = 1$ , which requires $\langle r | s \rangle = 0$ , and we conclude that $H _ { r }$ and $H _ { s }$ meet orthogonally.
□

Our final application concerns the norm $- 4$ vectors of $K$ .
According to [5], thm.
2.15, there are two orbits of such vectors, distinguished by their orthogonal complements.
Such a vector $\boldsymbol { v }$ is called even (resp.
odd) if $v ^ { \perp }$ is isometric to $E _ { 8 } ( - 2 ) \oplus U \oplus \langle 4 \rangle$ (resp.
to $E _ { 8 } ( - 2 ) \oplus U ( 2 ) \oplus \langle 4 \rangle$ ).
The vectors of even type are important because the reflections in them define isometries of $K$ ; for example, they play an essential role in Sterk’s work ([7], sec.
4).
The odd vectors of norm $- 4$ seem to be less useful.
Conveniently, after translating to the $\hat { K }$ setting the even vectors stand out and the odd vectors are pushed into the background.
That is, the even norm $- 4$ vectors of $K$ correspond bijectively to the norm $- 2$ vectors of $\hat { K }$ , while the odd norm $- 4$ vectors of $K$ correspond to some of the norm $^ { - 8 }$ vectors of $\hat { K }$ .

We close with a theorem that is not an application of theorem 2 but rather a simplification of another part of the arithmetic arguments of [5].
Part of the background for the Torelli theorem is the fact that there is essentially only one way to embed $I I _ { 1 , 9 } ( 2 ) \cong E _ { 8 } ( - 2 ) \oplus U ( 2 )$ as a primitive sublattice of $I I _ { 3 , 1 9 } \cong E _ { 8 } ( - 1 ) ^ { 2 } \oplus U ^ { 3 }$ .
Such an embedding arises from the map $H ^ { 2 } ( S , \mathbb { Z } ) \to H ^ { 2 } ( \tilde { S } , \mathbb { Z } )$ induced by the covering map from the K3 surface $\tilde { S }$ to the Enriques surface $S$ .
The uniqueness theorem implies that the orthogonal complement of the sublattice is isometric to $I I _ { 1 , 9 } ( 2 ) \oplus U \cong$ $E _ { 8 } ( - 2 ) \oplus U ( 2 ) \oplus U$ , setting the stage for the Torelli theorem.
The proof below may be regarded as a replacement for the argument (2.9) in [5].

Theorem 6. Two primitive sublattices of $I I _ { 3 , 1 9 }$ that are isometric to $I I _ { 1 , 9 } ( 2 )$ are equivalent under the isometry group of $^ { I I _ { 3 , 1 9 } }$ .
The orthogonal complement $B$ of such a sublattice $A$ is isometric to $I I _ { 1 , 9 } ( 2 ) \oplus I I _ { 1 , 1 }$ , and any isometry of $A$ or $B$ extends to $I I _ { 3 , 1 9 }$ .

Proof: First we show that if $A$ is any such sublattice then $B = A ^ { \perp }$ is isometric to $I I _ { 1 , 9 } ( 2 ) \oplus$

$I I _ { 1 , 1 }$ .
Since $I I _ { 3 , 1 9 }$ is unimodular its images under the projections to $A \otimes \mathbb { Q }$ and $B \otimes \mathbb { Q }$ are $A ^ { * }$ and $B ^ { * }$ , and the projections define a bijection (the gluing map) between $A ^ { * } / A$ and $B ^ { * } / B$ .
All elements of $A ^ { * }$ have integral norm, so the same is true of $B ^ { * }$ .
Reducing the norms of elements of $A ^ { * }$ and $B ^ { * }$ modulo 2 defines quadratic forms on $A ^ { * } / A$ and $B ^ { * } / B$ , and since $I I _ { 3 , 1 9 }$ is even the gluing map is an isometry.
Since $A ^ { * } / A$ contains a 5-dimensional isotropic subspace, so does $B ^ { * } / B$ , so that $B$ embeds in an even unimodular lattice $C$ , which must of course be isometric to $I I _ { 2 , 1 0 }$ .
Now $C / 2 C$ is equipped with a nondegenerate quadratic form obtained by halving norms of elements of $C$ and then reducing modulo 2. It is obvious that under this form $B / 2 C$ is orthogonal to the isotropic subspace $( 2 B ^ { * } ) / 2 C$ .
Since $| ( 2 B ^ { * } ) / 2 C | = 2 ^ { 5 }$ and $| B / 2 C | = 2 ^ { 7 }$ we see that $B$ is the preimage in $C$ of the orthogonal complement of a 5-dimensional isotropic subspace of $C / 2 C$ .
Since there is only one such subspace up to isometry of $C / 2 C$ , and every isometry of $C / 2 C$ is induced by one of $C$ , $B$ is determined up to isometry.
Since $I I _ { 1 , 9 } ( 2 ) \oplus I I _ { 1 , 1 }$ is a possibility for $B$ it is the only possibility.

Now, the even unimodular lattices containing $A \oplus B$ as a primitive sublattice are in 1-1 correspondence with the isometries $A ^ { * } / A \to B ^ { * } / B$ .
It is easy to check that every isometry of $I I _ { 1 , 9 } ( 2 ) ^ { * } / I I _ { 1 , 9 } ( 2 )$ is induced by one of $I I _ { 1 , 9 } ( 2 )$ .
It follows that every isometry of $A ^ { * } / A$ (resp.
$B ^ { * } / B )$ is induced by one of $A$ (resp.
$B$ ).
Now, if $A ^ { \prime }$ is another primitive sublattice of $I I _ { 3 , 1 9 }$ isometric to $A$ , then its orthogonal complement $B ^ { \prime }$ is isometric to $B$ .
Choosing any isometry $A \oplus B \to A ^ { \prime } \oplus B ^ { \prime }$ carries $I I _ { 3 , 1 9 }$ to some even unimodular lattice containing $A ^ { \prime } \oplus B ^ { \prime }$ .
By applying a symmetry of $A ^ { \prime }$ or $B ^ { \prime }$ we may arrange for $I I _ { 3 , 1 9 }$ to be carried to itself, so that $A$ and $A ^ { \prime }$ are equivalent under $\mathrm { A u t } I I _ { 3 , 1 9 }$ .
Finally, the isometries $f$ of $A$ that extend to $I I _ { 3 , 1 9 }$ are just those for which there is an isometry $g$ of $B$ such that the actions of $f$ on $A ^ { * } / A$ and $g$ on $B ^ { * } / B$ correspond under the gluing map.
Therefore any symmetry of $A$ extends to $I I _ { 3 , 1 9 }$ .
The same argument also shows that any symmetry of $B$ extends to $I I _ { 3 , 1 9 }$ .
□

Horikawa ([4], thm.
1.5) proved the first part of this theorem by geometric methods and Namikawa ([5], thm.
1.4) proved it all by using sophisticated arithmetic results of Nikulin [6].
Our argument can be used in more general settings, but our goal in this paper has been to present the most elementary possible approach to the arithmetic of the various lattices related to the Torelli theorem.
The theorem is a special case of Nikulin’s theorem 1.14.2, and our proof is presumably a special case of his proof.

Notes: As mentioned above, the trick used in lemma 1 to pass between $I I _ { 1 , 1 } ( 2 )$ and $I _ { 1 , 1 }$ is well-known to experts.
The passage between $K$ and $\hat { K }$ is implicit in the statement of Borcherds ([3], example 13.7) of the relationship between the automorphic form $\Psi _ { z }$ he constructs there and the automorphic form $\Phi$ he constructs in [2].
Also, Sterk ([7], props.
4.3.12 and 4.3.13) explicitly established a special case of lemma 1, namely the correspondence between $I _ { 1 , 9 }$ and $E _ { 8 } ( - 2 ) \oplus I I _ { 1 , 1 }$ .
If he had obtained this result in its natural generality, it might have simplified his work.

I am grateful to R.
Borcherds for stimulating discussions and correspondence.

# References

[1] D.
J.
Allcock.
Metric curvature of infinite branched covers.
Preprint 1999.  
[2] R.
E.
Borcherds.
The moduli space of Enriques surfaces and the fake monster Lie superalgebra.
Topology, 35(3):699–710, 1995.  
[3] R.
E.
Borcherds.
Automorphic forms with singularities on Grassmannians.
Invent.
Math., 132:491–562, 1998.  
[4] E.
Horikawa.
On the periods of Enriques surfaces.
I.
Math.
Ann., 234:73–88, 1978.  
[5] Y.
Namikawa.
Periods of Enriques surfaces.
Math.
Ann., 270:201–222, 1985.  
[6] V.
V.
Nikulin.
Integral bilinear forms and some of their applications.
Math.
USSR Izv., 14:103–167, 1980.

[7] H.
Sterk.
Compactifications of the period space of Enriques surfaces part I.
Math.
Z., 207:1– 36, 1991.

Department of Mathematics  
Harvard University  
One Oxford St  
Cambridge, MA 02139  
web page: http://www.math.harvard.edu/∼allcock