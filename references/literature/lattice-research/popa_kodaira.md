NOTES FOR 483-3: KODAIRA DIMENSION OF ALGEBRAIC VARIETIES

CONTENTS

1. Plurigenera 2
2. Kodaira dimension 3
3. Projective bundles 6
4. Intersection numbers and Riemann-Roch-type theorems 8
5. Nef and big line bundles 16
6. Birational classification of surfaces 23
7. Iitaka's conjecture 30
8. Vanishing theorems 33
9. Castelnuovo-Mumford regularity 40
10. Log-resolutions, birational transformations, Kawamata-Viehweg 42
11. Vanishing for direct images of pluricanonical bundles 47
12. Positivity for vector bundles and torsion-free sheaves 50
13. Multiplication maps 59
14. Iitaka's conjecture for a base of general type 60
15. Variation of families of varieties 63
16. Bigness of the determinant implies Viehweg's conjecture 65
17. Vector bundle constructions, variation and positivity 68
18. Positivity for families of varieties of general type 71

References 74

## 1. Plurigenera

Let $X$ be a smooth projective variety over an algebraically closed field $k.$ The crucial invariant of $X$ we will repeatedly refer to is its canonical bundle

$\omega_{X}:=\wedge^{\dim X}\Omega^{1}_{X}.$

###### Definition 1.1.

The plurigenera of $X$ are the non-negative integers

$P_{m}(X)=h^{0}(X,\omega_{X}^{\otimes m}):=\dim_{k}H^{0}(X,\omega_{X}^{\otimes m}),\ \ \forall\ m\geq 0.$

###### Example 1.2 (Projective space).

If $X={\bf P}^{n},$ then $\omega_{X}={\mathcal{O}}_{{\bf P}^{n}}(-n-1),$ and so $P_{m}(X)=0$ for all $m\geq 0.$

###### Example 1.3 (Curves).

If $X=C,$ a smooth projective curve if genus $g,$ then by definition $P_{1}(X)=g.$ Moreover:

$\bullet$ If $C={\bf P}^{1},$ i.e. $g=0,$ then $\omega_{C}={\mathcal{O}}_{{\bf P}^{1}}(-2),$ and so $P_{m}(C)=0$ for all $m\geq 0.$

$\bullet$ If $C$ is elliptic, i.e. $g=1,$ then $\omega_{C}\simeq{\mathcal{O}}_{C},$ and in particular $P_{m}(C)=1$ for all $m\geq 0.$

$\bullet$ If $g\geq 2,$ then

$\deg\ \omega_{C}^{\otimes m}=m(2g-2)>2g-1,\ \ \forall\ m\geq 2,$

so $H^{1}(C,\omega_{C}^{\otimes m})=0,$ and so by Riemann-Roch

$P_{m}(C)=m(2g-2)-g+1=(2m-1)(g-1),\ \ \forall\ m\geq 2.$

###### Example 1.4 (Hypersurfaces).

Let $X\subset{\bf P}^{n}$ be a smooth hypersurface of degree $d.$ If ${\mathcal{O}}_{X}(1)$ is the restriction of ${\mathcal{O}}_{{\bf P}^{n}}(1),$ we have

$\omega_{X}\simeq{\mathcal{O}}_{X}(d-n-1).$

$\bullet$ If $d\leq n,$ then $P_{m}(X)=0$ for all $m\geq 0.$

$\bullet$ If $d=n+1,$ then $\omega_{X}\simeq{\mathcal{O}}_{X},$ and in particular $P_{m}(X)=1$ for all $m\geq 0.$

$\bullet$ If $d\geq n+2,$ then $\omega_{X}$ is a very ample line bundle. Using Serre Vanishing and the basic properties of the Hilbert polynomial of $X,$ we have

$P_{m}(X)=\chi(X,\omega_{X}^{\otimes m})=\frac{d(d-n-1)}{(n-1)!}\cdot m^{n-1}+O(m^{n-2})\ \ \mbox{for}\ m\gg 0.$

Recall also that if $n\geq 3,$ then

$H^{i}(X,{\mathcal{O}}_{X})=0,\ \ \forall\ 0<i<n-1.$

###### Exercise 1.5.

Recall that for a smooth complete intersection $X\subset{\bf P}^{N}$ of hypersufaces of degrees $d_{1},\ldots,d_{k}$, we have

$\omega_{X}\simeq{\mathcal{O}}_{X}(d_{1}+\cdots+d_{k}-n-1).$

Use this in order to do calculations similar to the case of hypersurfaces.

###### Exercise 1.6.

If $X$ and $Y$ are smooth projective varieties, show that

$P_{m}(X\times Y)=P_{m}(X)\cdot P_{m}(Y).$

###### Example 1.7 (Abelian varieties.)

Let $X$ be an abelian variety. Then $T_{X}$ is trivial, and in particular $\omega_{X}\simeq\mathcal{O}_{X}$. Thus this is another example where

$P_{m}(X)=1,\ \ \forall\ m\geq 0.$

However, note that unlike in the case of hypersurfaces

$H^{i}(X,\mathcal{O}_{X})\simeq\bigwedge^{i}H^{1}(X,\mathcal{O}_{X})\neq 0,\ \ \forall\ i\geq 0.$

###### Definition 1.8 (Calabi-Yau’s).

(1) We will call a *weak Calabi-Yau* variety a smooth projective variety $X$ with $\omega_{X}\simeq\mathcal{O}_{X}$. If in addition

$H^{i}(X,\mathcal{O}_{X})=0,\ \ \forall\ 0<i<\dim X,$

we will say that $X$ is *Calabi-Yau*. (Usually, even this is not enough for the proper definition: one should also require, over $\mathbf{C}$, that $X$ be simply connected, but we will ignore this here.)

Thus a hypersurface of degree $d=n+1$ in $\mathbf{P}^{n}$ is Calabi-Yau, while an abelian variety is weak Calabi-Yau, but not Calabi-Yau.

(2) A $K3$ *surface* is a Calabi-Yau variety $X$ of dimension $2$. In other words, $\omega_{X}\simeq\mathcal{O}_{X}$, and $H^{1}(X,\mathcal{O}_{X})=0$.

###### Example 1.9.

According to the examples above, a hypersurface of degree $4$ (a *quartic surface*) in $\mathbf{P}^{3}$ is a $K3$ surface. So is a complete intersection of type $(2,3)$, i.e. of a general quadric and a cubic in $\mathbf{P}^{4}$, and one of type $(2,2,2)$, i.e. of three general quadrics in $\mathbf{P}^{5}$. For simple numerical reasons, there are no other complete intersection $K3$ surfaces (check this!).

## 2. Kodaira dimension

Definition and first examples. Let $X$ be a smooth projective variety, and let $L$ be a line bundle on $X$. For each $m\geq 0$ such that $h^{0}(X,L^{\otimes m})\neq 0$, the linear system $|L^{\otimes m}|$ induces a rational map from $X$ to a projective space, and more precisely a morphism

$\varphi_{m}:X-B_{m}\to\mathbf{P}^{N_{m}},\ \ N_{m}=h^{0}(X,L^{\otimes m})-1,$

where $B_{m}=\mathrm{Bs}(L^{\otimes m})$ is its base locus. We denote by $\varphi_{m}(X)$ the closure of the image of $\varphi_{m}$ in $\mathbf{P}^{N_{m}}$.

###### Definition 2.1.

(1) The *Iitaka dimension* of $L$ is

$\kappa(X,L)=\max_{m\geq 1}\ \dim\varphi_{m}(X)$

if $\varphi_{m}(X)\neq\emptyset$ for some $m$. We set $\kappa(X,L)=-\infty$ otherwise (i.e. when $h^{0}(X,L^{\otimes m})=0$ for all $m\geq 0$). Note that

$\kappa(X,L)\in\{-\infty,0,1,\ldots,\dim X\}.$

(2) The line bundle $L$ is called *big* if $\kappa(X,L)=\dim X$.

(3) The *Kodaira dimension* of $X$ is $\kappa(X):=\kappa(X,\omega_{X})$. Moreover, $X$ is called of *general type* if $\kappa(X)=\dim X$, i.e. if $\omega_{X}$ is big.

######

###### Example 2.2.

If $L$ is ample, then it is big. Indeed, for $m\gg 0$ we have that $L$ is very ample, and so $\varphi_{m}$ is an embedding.

We could give concrete examples right away, but instead I will first give another interpretation, and then use the previous section. This is the original definition given by Iitaka; we will show the equivalence later.

###### Proposition 2.3.

In the setting above, let $\kappa=\kappa(X,L)$. Then there exist constants $a,b>0$ such that

$a\cdot m^{\kappa}\leq h^{0}(X,L^{\otimes m})\leq b\cdot m^{\kappa},$

for sufficiently large and divisible $m$.

In other words, the rough interpretation for the Kodaira dimension is that

$P_{m}(X)\sim m^{\kappa(X)}$

for $m$ sufficiently large and divisible.

###### Example 2.4.

$\kappa(\mathbf{P}^{n})=-\infty$.

###### Example 2.5.

Example 1.3 gives us the following classification of smooth projective curves $C$ of genus $g$ in terms of Kodaira dimension:

$\bullet$ $\kappa(C)=-\infty\iff g=0$, i.e. if $C\simeq\mathbf{P}^{1}$.

$\bullet$ $\kappa(C)=0\iff g=1$, i.e. if $C$ is elliptic.

$\bullet$ $\kappa(C)=1\iff g\geq 2$. These are the curves of general type.

###### Example 2.6.

If $X$ is a (weak) Calabi-Yau variety (like a $K3$ surface, an abelian variety, or a hypersurface of degree $n+1$ in $\mathbf{P}^{n}$), then $\kappa(X)=0$.

###### Example 2.7.

Example 1.4 gives us the Kodaira dimension of a hypersurface $X\subset\mathbf{P}^{n}$ of degree $d$.

$\bullet$ $d\leq n\iff\kappa(X)=-\infty$.

$\bullet$ $d=n+1\iff\kappa(X)=0$

$\bullet$ $d\geq n+2\iff\kappa(X)=n-1=\dim X$.

###### Exercise 2.8.

If $X$ and $Y$ are smooth projective varieties, then

$\kappa(X\times Y)=\kappa(X)+\kappa(Y).$

###### Example 2.9.

The exercise above shows that one can produce examples of varieties of any allowed Kodaira dimension. Let’s see this for surfaces: say $E$ is an elliptic curve, and $C$ is a curve of genus $g\geq 2$, and $D$ is any curve. Then:

$\bullet$ $\kappa(\mathbf{P}^{1}\times D)=-\infty$.

$\bullet$ $\kappa(E\times E)=0$.

$\bullet$ $\kappa(E\times C)=1$.

$\bullet$ $\kappa(C\times C)=2$.

######

This can easily be extended to arbitrary dimension.

### Equivalent interpretations

We come back to the alternative interpretation of the Iitaka dimension that was used above. Let’s be a bit more precise about what integers $m$ appear in the definition and in Proposition 2.3.

If $L$ is a line bundle on $X$, we consider

$N(L):=\{m\in\mathbf{N}\ |\ H^{0}(X,L^{\otimes m})\neq 0\}.$

This is the *semigroup* of $L$; indeed, it is a semigroup with respect to addition, because of the existence of multiplication maps

(1) $H^{0}(X,L^{\otimes k})\otimes H^{0}(X,L^{\otimes l})\longrightarrow H^{0}(X,L^{\otimes k+l}).$

We can consider

$e(L):=\gcd\ \{m\ |\ m\in N(L)\}\geq 1.$

All sufficiently large elements of $N(L)$ are multiples of $e(L)$, and all sufficiently large multiples of $e(L)$ are in $N(L)$. The number $e(L)$ is the largest with this property, and is called the *exponent* of $L$.

In any case, both in the definition, and in Proposition 2.3, the only relevant integers $m$ are those in $N(L)$; by sufficiently large and divisible we mean sufficiently large multiples of $e(L)$. We can consider an even more important definition:

###### Definition 2.10.

The *section ring* of $L$ is the ring

$R(L):=\bigoplus_{m\geq 0}H^{0}(X,L^{\otimes m}).$

This is a graded integral $k$-algebra due to the multiplication maps in (15).

For instance, the *canonical ring* of $X$ is $R(X):=R(\omega_{X})$. One of the most famous recent results in birational geometry, due to Birkar-Cascini-Hacon-M^{c}Kernan says that $R(X)$ is finitely generated. This is not true for arbitrary $L$.

###### Proof of Proposition 2.3.

The lower bound is a quite direct calculation; check it as an exercise! The more interesting part is the upper bound, and we concentrate on this.

We have $\dim\varphi_{m}(X)=\kappa(L)$, for all $m\in N(L)$ sufficiently large. Let’s first assume that $L$ is big, i.e. $\kappa(L)=\dim X$. Consider an ample line bundle $A$ in $X$ such that

$H^{0}(X,A\otimes L^{-1})\neq 0.$

(Note that this is always possible, since by Serre’s theorem $L^{-1}$ twisted by any large power of an ample line bundle is globally generated.) This gives the following sequence of inequalities, for some constant $C>0$.

$h^{0}(X,L^{\otimes m})\leq h^{0}(X,A^{\otimes m})\leq C\cdot m^{\dim X}=C\cdot m^{\kappa(L)},$

where the second inequality is given by the Hilbert polynomial of $A$

Assume now that $\kappa(L)<\dim X$; we reduce this case to the equality case. To this end, pick $H_{1},\ldots,H_{p}$ general very ample divisors on $X$, with $p=\dim X-\kappa(L)$, and denote $X^{\prime}=H_{1}\cap\cdots\cap H_{p}$. It is a standard fact that each $H_{i}$ dominates $\varphi_{m}(X)$, i.e. its image is dense. (Idea: one can reduce to the case when the map is defined everywhere, by considering the closure of the graph; if $H$ didn’t map surjectively, then it would not meet a general fiber of the map, which is positive dimensional because $\kappa(L)<\dim X$. But very ample divisors have to meet a general positive dimensional subvariety of a family sweeping $X$. We will understand this type of argument better once we study positivity in more detail.) We can do this in such a way that $X^{\prime}$ dominates $\varphi_{m}(X)$ for all sufficiently large $m$, and of course $\dim X^{\prime}=\kappa(L)$. The argument given in the equality case then gives

$h^{0}(X^{\prime},L^{\otimes m}_{|X^{\prime}})\leq C\cdot m^{\dim X^{\prime}}=C\cdot m^{\kappa(L)}.$

At this stage we are done, since we in fact have that the restriction map

$H^{0}(X,L^{\otimes m})\longrightarrow H^{0}(X^{\prime},L^{\otimes m}_{|X^{\prime}})$

is injective for all $m\in N(L)$ sufficiently large. Indeed, by the definition of the map induced by $L^{\otimes m}$, the sections in $H^{0}(X,L^{\otimes m})$ correspond to the hyperplanes in $\mathbf{P}^{N_{m}}$. If the restriction map in question weren’t injective, it would mean that there is a hyperplane in $\mathbf{P}^{N_{m}}$ containing the image of $X^{\prime}$. But this image is $\varphi_{m}(X)$, a contradiction. ∎

It is not too hard to obtain another interpretation of the Iitaka dimension that is sometimes useful. I will skip the proof, since we will not use it below.

###### Proposition 2.11.

If $\kappa(L)\geq 0$, and $Q\big{(}R(L)\big{)}$ is the quotient field of $R(L)$, then

$\kappa(L)=\operatorname{trdeg}_{k}\ Q\big{(}R(L)\big{)}-1.$

## 3. Projective bundles

Let $X$ be a noetherian scheme, and $E$ a locally free sheaf of rank $r$ on $X$. Then the symmetric algebra of $E$ is

$S(E):=\bigoplus_{m\geq 0}S^{m}E,$

a sheaf of graded $\mathcal{O}_{X}$-algebras, generated over $S^{0}E\simeq\mathcal{O}_{X}$ by its degree 1 part.

###### Definition 3.1.

The *projective bundle* of one-dimensional quotients of $E$ is the scheme over $X$:

$\pi:\mathbf{P}(E):=\operatorname{Proj}\big{(}S(E)\big{)}\longrightarrow X.$

A point in $\mathbf{P}(E)$ is the data of a point $x\in X$ and a one-dimensional quotient of the $\kappa(x)$-vector space $E(x)=E_{x}/\mathfrak{m}_{x}E_{x}$. Therefore we have $\pi^{-1}(x)=\mathbf{P}^{r-1}_{\kappa(x)}$. If $E$ has rank 1, then obviously $\mathbf{P}(E)\simeq X$. Recall that, as with each $\operatorname{Proj}$ construction, $\mathbf{P}(E)$ comes endowed with an invertible sheaf $\mathcal{O}_{\mathbf{P}(E)}(1)$, which restricts to $\mathcal{O}_{\mathbf{P}^{r-1}}(1)$ on each fiber.

###### Proposition 3.2.

Let $X$ be a noetherian scheme, and $E$ a locally free sheaf of rank $r\geq 2$ on $X$. Then the following properties of $\mathbf{P}=\mathbf{P}(E)$ hold:

(i) There is a canonical isomorphism of graded $\mathcal{O}_{X}$-algebras

$S(E)\simeq\bigoplus_{m\geq 0}\pi_{*}\mathcal{O}_{\mathbf{P}}(m).$

In particular, $\pi_{*}\mathcal{O}_{\mathbf{P}}(m)\simeq S^{m}E$ for all $m$ (which means $0$ for $m<0$).

(ii) $R^{i}\pi_{*}\mathcal{O}_{\mathbf{P}}(m)=0$ for all $m$ and all $0<i<r-1$; moreover

$R^{r-1}\pi_{*}\mathcal{O}_{\mathbf{P}}(m)\simeq\big{(}\pi_{*}\mathcal{O}_{\mathbf{P}}(-m-r)\big{)}^{\vee}\otimes\det\,E^{\vee},$

and in particular $R^{r-1}\pi_{*}\mathcal{O}_{\mathbf{P}}(m)=0$ for $m>-r$.

(iii) There is a natural short exact sequence

$0\longrightarrow\Omega^{1}_{\mathbf{P}/X}\otimes\mathcal{O}_{\mathbf{P}}(1)\longrightarrow\pi^{*}E\longrightarrow\mathcal{O}_{\mathbf{P}}(1)\longrightarrow 0.$

(The quotient $\pi^{*}E\to\mathcal{O}_{\mathbf{P}}(1)$ on the right is called the tautological quotient.) Consequently, if $X$ is say a smooth variety over a field, the canonical bundle of $\mathbf{P}(E)$ is given by the formula

$\omega_{\mathbf{P}}\simeq\pi^{*}(\det E\otimes\omega_{X})\otimes\mathcal{O}_{\mathbf{P}}(-r).$

(iv) $\mathrm{Pic}(\mathbf{P})\simeq\mathrm{Pic}(X)\times\mathbf{Z}.$

(v) If $F$ is another locally free sheaf of rank $r$ on $X$, then $\mathbf{P}(E)\simeq\mathbf{P}(F)$ as schemes over $X$ if and only if there is an invertible sheaf $L$ on $X$ such that $F\simeq E\otimes L$. If this holds, then $\mathcal{O}_{\mathbf{P}(F)}(1)\simeq\mathcal{O}_{\mathbf{P}(E)}(1)\otimes\pi^{*}L$.

###### Proof.

I will explain the essential ideas; it is straightforward to fill in the details. The key observation is the following: if $V$ is a free module of rank $r$ over a ring $A$, and $\mathbf{P}(V)\simeq\mathbf{P}_{A}^{r-1}$ is its projectivization, then $H^{0}(\mathbf{P}(V),\mathcal{O}_{\mathbf{P}(V)}(1))\simeq V$, and more generally

$H^{0}\big{(}\mathbf{P}(V),\mathcal{O}_{\mathbf{P}(V)}(m)\big{)}\simeq S^{m}V,\ \ \forall\ m\geq 0.$

This is a reflection of the standard identification

(2) $S(V)=\bigoplus_{m\geq 0}S^{m}V\simeq A[X_{0},\ldots,X_{r-1}]\simeq\bigoplus_{m\geq 0}H^{0}\big{(}\mathbf{P}(V),\mathcal{O}_{\mathbf{P}(V)}(m)\big{)}.$

Recall now that for each $U=\mathrm{Spec}\ A\subseteq X$, we have that

$\pi^{-1}(U)\simeq\mathbf{P}_{A}^{r-1}\simeq\mathbf{P}(E(U)).$

Thus (i) is simply a relative version of (2).

Part (ii) can be proved in an elementary fashion as well, but how about we practice our knowledge of cohomology and base change? Since the fibers of $\pi$ are all projective spaces of the same dimension, $\pi$ is a flat morphism, and for each $x\in X$, $\mathcal{O}_{\mathbf{P}}(m)$ restricts to $\mathcal{O}_{\mathbf{P}^{r-1}_{\kappa(x)}(m)}$ on $\pi^{-1}(x)$. Therefore the dimension of the cohomology along the fibers is constant, and so by cohomology and base change, the natural homomorphisms

$\varphi_{i,x}:R^{i}\pi_{*}\mathcal{O}_{\mathbf{P}}(m)\otimes\kappa(x)\longrightarrow H^{i}\big{(}\mathbf{P}^{r-1}_{\kappa(x)},\mathcal{O}_{\mathbf{P}^{r-1}_{\kappa(x)}(m)}\big{)}$

re isomorphisms, for all $i$ and all $x\in X$. Thus (ii) is just a consequence of the standard facts about the cohomology of line bundles on projective space (with the exception of the actual formula for $R^{r-1}\pi_{*}\mathcal{O}_{\mathbf{P}}(m)$, which I leave as an exercise).

For (iii), note that over $U=\operatorname{Spec}A\subseteq X$, if $V=E(U)$, we have a natural surjective evaluation map

$H^{0}\big{(}\mathbf{P}(V),\mathcal{O}_{\mathbf{P}(V)}(1)\big{)}\otimes\mathcal{O}_{\mathbf{P}(V)}\longrightarrow\mathcal{O}_{\mathbf{P}(V)}(1)\longrightarrow 0,$

since $\mathcal{O}(1)$ is globally generated. By the discussion above, this can be rewritten as

$V\otimes\mathcal{O}_{\pi^{-1}(U)}\longrightarrow\mathcal{O}_{\pi^{-1}(U)}(1)\longrightarrow 0,$

which by gluing over a cover with such open sets $U$ gives the natural quotient $\pi^{*}E\to\mathcal{O}_{\mathbf{P}}(1)$. Recall furthermore that we know the kernel of the evaluation map; indeed, for any ring $A$, and any free $A$-module $V$ of rank $r$, we have the *Euler sequence*

$0\longrightarrow\Omega^{1}_{\mathbf{P}(V)/A}(1)\longrightarrow V\otimes\mathcal{O}_{\mathbf{P}(V)}\longrightarrow\mathcal{O}_{\mathbf{P}(V)}(1)\longrightarrow 0.$

Again by gluing, this gives the full result in (iii). The statement about the canonical bundle is obtained by passing to determinants in the short exact sequence.

Parts (iv) and (v) are left as an exercise. ∎

###### Corollary 3.3.

Let $X$ be a smooth projective variety, and $E$ a locally free sheaf of rank $r\geq 2$. Then $P_{m}(\mathbf{P}(E))=0$ for all $m\geq 1$, and in particular $\kappa(\mathbf{P}(E))=-\infty$.

###### Proof.

By Proposition 3.2(iii) and the projection formula, we have that

$P_{m}(\mathbf{P}(E))=h^{0}\big{(}X,(\det E\otimes\omega_{X})^{\otimes m}\otimes\pi_{*}\mathcal{O}_{\mathbf{P}}(-rm)\big{)}.$

But we have seen in Proposition 3.2(i) that $\pi_{*}\mathcal{O}_{\mathbf{P}}(-k)=0$ for $k\geq 1$. ∎

###### Definition 3.4.

A *ruled surface* is a projective bundle $\pi:\mathbf{P}(E)\to C$, where $C$ is a smooth projective curve over an algebraically closed field, and $E$ is a locally free sheaf of rank $2$ on $C$. (The definition is often stated differently, namely as a surjective morphism $\pi:X\to C$ with fibers isomorphic to $\mathbf{P}^{1}$, but it is standard to see that it is equivalent to the one given here.)

Ruled surfaces provide us with new examples of smooth projective surfaces of Kodaira dimension $-\infty$ (and same for projective bundles in arbitrary dimension).

## 4. Intersection numbers and Riemann-Roch-type theorems

I will explain the theory in some detail for smooth projective surfaces, and then briefly mention results and references in higher dimension and when singularities are allowed.

Surfaces. Let $X$ be a smooth projective surface over $k=\overline{k}$. We cannot talk about the degree of a divisor any more, but we can talk about the *intersection number* of two divisors. Since we are dealing with smooth surfaces, we will switch back and forth between Weil and Cartier divisors whenever convenient.

Notes for 483-3

To begin with, the intuition is that when $C$ and $D$ are smooth irreducible curves intersecting transversely at $k$ points on $X$, then $C \cdot D = k$. We say that $C$ and $D$ intersect transversely at $x \in X$ if their local equations $f$ and $g$ at $x$ generate $\mathfrak{m}_x \subset \mathcal{O}_{X,x}$.

Theorem 4.1. One can define on $X$ a unique bilinear pairing

$$
\operatorname{Div}(X) \times \operatorname{Div}(X) \longrightarrow \mathbf{Z}, \quad (C, D) \mapsto C \cdot D
$$

such that:

(i) If $C$ and $D$ are smooth curves meeting transversely, then

$$
C \cdot D = \#(C \cap D).
$$

(ii) The pairing is symmetric, i.e. $C \cdot D = D \cdot C$.

(iii) The pairing is additive, i.e. $(C_1 + C_2) \cdot D = C_1 \cdot D + C_2 \cdot D$.

(iv) The pairing depends only on linear equivalence classes, i.e. if $C_1 \sim C_2$, then

$$
C_1 \cdot D = C_2 \cdot D.
$$

Recalling that we identify $\operatorname{Pic}(X)$ with $\operatorname{Div}(X) / \sim$, the group of divisors modulo linear equivalence, the theorem gives an intersection pairing

$$
\operatorname{Pic}(X) \times \operatorname{Pic}(X) \longrightarrow \mathbf{Z}.
$$

Proof. $\bullet$ Uniqueness: Fix $H$ an ample divisor on $X$. Let $C$ and $D$ be any two divisors. We can then fix an $m &gt; 0$ such that $mH$, $C + mH$ and $D + mH$ are all very ample.³ By Bertini's theorem, there exist $C' \in |C + mH|$ smooth, $D' \in |D + mH|$ smooth and transversal to $C'$, $E' \in |mH|$ smooth and transversal to $D'$, and $F' \in |mH|$ smooth and transversal to $C'$ and $E'$. Using properties (i)-(iv), we then have

$$
\begin{array}{l}
C \cdot D = (C + mH) \cdot (D + mH) - C \cdot (mH) - D \cdot (mH) - (mH) \cdot (mH) = \\
= C' \cdot D' - (C' - E') \cdot F' - (D' - F') \cdot E' - E' \cdot F' = \\
\end{array}
$$

$$
= C' \cdot D' - C' \cdot F' - D' \cdot E' - E' \cdot F' = \#(C' \cap D') - \#(C' \cap F') - \#(D' \cap E') + \#(E' \cap F').
$$

This shows that if such a pairing exists, the answer is uniquely determined by properties (i)-(iv).

$\bullet$ Existence: To define a pairing with these properties, we first note the following:

Claim: If $C$ is a smooth irreducible curve, and $D$ is any other curve on $X$ intersecting $C$ transversely, then

$$
\#(C \cap D) = \deg \mathcal{O}_C(D).
$$

Here $\mathcal{O}_C(D)$ is the line bundle $\mathcal{O}_X(D)_{|C}$ on $C$. To see this, we start with the short exact sequence

$$
0 \longrightarrow \mathcal{O}_X(-D) \longrightarrow \mathcal{O}_X \longrightarrow \mathcal{O}_D \longrightarrow 0
$$

³By Serre, we can find a $p$ such that $C + pH$ is basepoint free, and same for $D$. We can also find an $r$ such that $rH$ is very ample. But now recall (or take as an exercise) that very ample plus basepoint free is very ample.

on $X$, and twist is by $\mathcal{O}_{C}$ to get

$0\longrightarrow\mathcal{O}_{C}(-D)\longrightarrow\mathcal{O}_{C}\longrightarrow\mathcal{O}_{C\cap D}\longrightarrow 0.$

Here $C\cap D$ denotes the scheme theoretic intersection, and $\mathcal{O}_{C}(-D)$ can be identified with its ideal in $C$. But since the intersection is transversal, we indeed have

$\#(C\cap D)=\deg\ (C\cap D)=\deg\ \mathcal{O}_{C}(D).$

For the definition, the first step is the following:

Claim: If $C$ and $D$ are very ample divisors, then $C\cdot D$ exists and is well defined.

To this end, by Bertini we can consider $C^{\prime}\in|C|$ and $D^{\prime}\in|D|$ smooth and with transverse intersection, so that

$C\cdot D:=C^{\prime}\cdot D^{\prime}=\#(C^{\prime}\cap D^{\prime}).$

Now take another smooth $D^{\prime\prime}\in|D|$, transversal to $C^{\prime}$. By the previous Claim, we have

$\#(C^{\prime}\cap D^{\prime})=\deg\ \mathcal{O}_{C^{\prime}}(D^{\prime})=\deg\ \mathcal{O}_{C^{\prime}}(D^{\prime\prime})=\#(C^{\prime\prime}\cap D^{\prime\prime}).$

The same argument holds by replacing $C^{\prime}$ with a $C^{\prime\prime}$. Moreover, using properties of line bundles on curves, it is clear that (i)–(iv) hold in this setting.

To define a pairing in general, fix again all of the notation and choices in the Uniqueness section. Define

$C\cdot D=C^{\prime}\cdot D^{\prime}-C^{\prime}\cdot F^{\prime}-D^{\prime}\cdot E^{\prime}-E^{\prime}\cdot F^{\prime}.$

Each individual term on the right hand side exists and is well defined by the previous Claim. We finally have to check that the whole expression is well defined. Recall that we had $C\sim C^{\prime}-E^{\prime}$ and $D\sim D^{\prime}-F^{\prime}$, so let’s replace them by similarly chosen $C\sim C^{\prime\prime}-E^{\prime\prime}$ and $D\sim D^{\prime\prime}-F^{\prime\prime}$. We have that

$C^{\prime}+E^{\prime\prime}\sim C^{\prime\prime}+E^{\prime}$

are very ample, and so by the Claim above we have

$C^{\prime}\cdot D^{\prime}+E^{\prime\prime}\cdot D^{\prime}=C^{\prime\prime}\cdot D^{\prime}+E^{\prime}\cdot D^{\prime}.$

We then do the same thing symmetrically for the $D$’s and $F$’s, which altogether gives the invariance of the right hand side. ∎

Note that the definition depends on moving curves into transverse position. A posteriori however, for those that do not have common components, we can calculate without doing this.

###### Proposition 4.2.

Let $C,D\subset X$ be curves without common irreducible components. Then

$C\cdot D=\sum_{p\in C\cap D}(C\cdot D)_{p}$

where $(C\cdot D)_{p}:=\dim_{k}\mathcal{O}_{X,p}/(f,g)$ is the intersection multiplicity of $C$ and $D$ at $p$.

###### Proof.

###### Proof.

As before, we have an exact sequence

$0\longrightarrow\mathcal{O}_{C}(-D)\longrightarrow\mathcal{O}_{C}\longrightarrow\mathcal{O}_{C\cap D}\longrightarrow 0.$

Now at each $p\in C\cap D$ we have

$(\mathcal{O}_{C\cap D})_{p}\simeq\mathcal{O}_{X,p}/(f,g),$

and so

$h^{0}\mathcal{O}_{C\cap D}=\sum_{p\in C\cap D}(C\cdot D)_{p}.$

But from the exact sequence and the additivity of the Euler characteristic, we have

$h^{0}\mathcal{O}_{C\cap D}=\chi(\mathcal{O}_{C\cap D})=\chi(\mathcal{O}_{C})-\chi(\mathcal{O}_{C}(-D)).$

The expression on the right hand side depends only on the linear equivalence class of $D$, and so we can replace $D$ as in the theorem above by the difference of two smooth curves having transverse intersection, and we can easily conclude that this number is equal to $C\cdot D$. ∎

There is however an important case that is not covered by the above: if $D\in\mathrm{Div}(X)$, we can also consider the *self-intersection* $D^{2}:=D\cdot D$. We cannot use the Proposition above even if $D$ is smooth, but in that case we do know that

$D^{2}=\deg\,\mathcal{O}_{D}(D)=\deg\,N_{D/X}.$

###### Example 4.3.

If $X=\mathbf{P}^{2}$ and $C,D\in\mathrm{Div}(\mathbf{P}^{2})$, then if $L$ is a line we know that there exist $m,n\in\mathbf{Z}$ such that $C\sim mL$ and $D\sim nL$. This means that

$C\cdot D=mn\cdot L^{2}=mn.$

(Note that $L$ is linearly equivalent to another line $L^{\prime}$ meeting it in one point, and so $L^{2}=\#(L\cap L^{\prime})=1$.) This fully describes the intersection pairing on $\mathbf{P}^{2}$.

###### Example 4.4.

Let $X=\mathbf{P}^{1}\times\mathbf{P}^{1}$. Then recall that

$\mathrm{Pic}(X)\simeq\mathbf{Z}\times\mathbf{Z}\simeq\mathbf{Z}\cdot f_{1}\times\mathbf{Z}\cdot f_{2},$

where $f_{1}$ and $f_{2}$ are the classes of fibers with respect to the two projections. Then, by counting intersection points, we have

$f_{1}^{2}=f_{2}^{2}=0\;\text{ and }\;f_{1}\cdot f_{2}=1.$

The intersection pairing is then described as follows: if $C$ and $D$ are of types $(m,n)$ and $(p,q)$ respectively, then

$C\cdot D=(mf_{1}+nf_{2})\cdot(pf_{1}+qf_{2})=mq+np.$

###### Example 4.5.

Let $\tilde{X}$ be the blow up of a smooth surface $X$ at a point $x\in X$, with exceptional divisor $E$. Identifying $E$ with $\mathbf{P}^{1}$, we have seen before that

$N_{E/X}\simeq\mathcal{O}_{E}(E)\simeq\mathcal{O}_{\mathbf{P}^{1}}(-1).$

By what we remarked above, this means that $E^{2}=-1$. Note that this negative self-intersection means that “$E$ doesn’t move”: we cannot find another $E^{\prime}$ linearly (or numerically) equivalent to $E$ which is different from $E$, as otherwise by general properties the self-intersection would have to be non-negative.

###### Proposition 4.6 (Genus formula).

If $C$ is a smooth curve of genus $g$ on a smooth projective surface $X$, then

$C\cdot(C+K_{X})=2g-2.$

###### Proof.

Recall that the adjunction formula says that

$\omega_{C}\simeq\big{(}\omega_{X}\otimes\mathcal{O}_{X}(C)\big{)}_{|C}.$

We simply pass to degrees, to get

$2g-2=\deg\,\mathcal{O}_{C}(C+K_{X})=C\cdot(C+K_{X}).$

∎

###### Example 4.7.

In the example above, regarding the blow-up of $X$ at a point, we have $E\simeq\mathbf{P}^{1}$ and $E^{2}=-1$. By the genus formula, we get $E\cdot K_{X}=-1$.

###### Example 4.8.

If $C$ is a smooth projective curve of degree $d$ in $\mathbf{P}^{2}$, we have that $C\simeq dL$, where $L\subset\mathbf{P}^{2}$ is a line. Also, $K_{\mathbf{P}^{2}}\simeq-3L$. By the genus formula, we obtain

$g(C)=1+\frac{C^{2}+C\cdot K_{\mathbf{P}^{2}}}{2}=1+\frac{d^{2}-3d}{2}=\frac{(d-1)(d-2)}{2},$

the standard genus formula for plane curves.

###### Theorem 4.9 (Riemann-Roch for surfaces).

Let $D$ be a divisor on a smooth projective surface $X$. Then

$\chi(\mathcal{O}_{X}(D))=\frac{D\cdot(D-K_{X})}{2}+\chi(\mathcal{O}_{S}).$

###### Proof.

As in the proof of the existence of the intersection pairing, we can write $D\sim D^{\prime}-F^{\prime}$, with $D^{\prime}$ and $F^{\prime}$ smooth curves, and use this since both sides depend only on the linear equivalence class of $D$. We have

$0\longrightarrow\mathcal{O}_{X}(D^{\prime}-F^{\prime})\longrightarrow\mathcal{O}_{X}(D^{\prime})\longrightarrow\mathcal{O}_{F^{\prime}}(D^{\prime})\longrightarrow 0,$

from which we deduce

$\chi(\mathcal{O}_{X}(D))=\chi(\mathcal{O}_{X}(D^{\prime}))-\chi(\mathcal{O}_{F^{\prime}}(D^{\prime})).$

On the other hand, from the short exact sequence

$0\longrightarrow\mathcal{O}_{X}\longrightarrow\mathcal{O}_{X}(D^{\prime})\longrightarrow\mathcal{O}_{D^{\prime}}(D^{\prime})\longrightarrow 0$

we get

$\chi(\mathcal{O}_{X}(D^{\prime}))=\chi(\mathcal{O}_{D^{\prime}}(D^{\prime}))+\chi(\mathcal{O}_{X}),$

and therefore we obtain

(3) $\chi(\mathcal{O}_{X}(D))=\chi(\mathcal{O}_{D^{\prime}}(D^{\prime}))-\chi(\mathcal{O}_{F^{\prime}}(D^{\prime}))+\chi(\mathcal{O}_{X}).$

We can now use Riemann-Roch on curves, followed by the self-intersection and genus formula for $D^{\prime}\subset X$, to deduce that

$\chi(\mathcal{O}_{D^{\prime}}(D^{\prime}))=\deg\mathcal{O}_{D^{\prime}}(D^{\prime})-g(D^{\prime})+1=$
$=D^{\prime}{}^{2}-\big{(}1+\frac{D^{\prime}{}^{2}+D^{\prime}\cdot K_{X}}{2}\big{)}+1=\frac{D^{\prime}{}^{2}-D^{\prime}\cdot K_{X}}{2}.$

Similarly, we obtain

$\chi(\mathcal{O}_{F^{\prime}}(D^{\prime}))=\deg\mathcal{O}_{F^{\prime}}(D^{\prime})-g(F^{\prime})+1=D^{\prime}\cdot F^{\prime}-\frac{{F^{\prime}}^{2}+F^{\prime}\cdot K_{X}}{2}.$

Putting all of this together in (3) and doing a small calculation, we get what we want. ∎

###### Remark 4.10.

There are other versions of the Riemann-Roch theorem that are very useful. One of them is the formula

$\chi(\mathcal{O}_{X})=\frac{1}{12}\big{(}K_{X}^{2}+c_{2}(T_{X})\big{)},$

where $c_{2}(T_{X})$ is the second Chern class of the tangent bundle. Riemann-Roch can then be written equivalently as

$\chi(\mathcal{O}_{X}(D))=\frac{D\cdot(D-K_{X})}{2}+\frac{1}{12}\big{(}K_{X}^{2}+c_{2}(T_{X})\big{)}.$

This is a special case of the *Hirzebruch-Riemann-Roch theorem* (see also below). Moreover, over $\mathbf{C}$ one has *Noether’s formula*:

$\chi(\mathcal{O}_{X})=\frac{1}{12}\big{(}K_{X}^{2}+\chi_{\mathrm{top}}(X)\big{)},$

where

$\chi_{\mathrm{top}}(X)=\sum_{i}(-1)^{i}b_{i}(X),\ \ b_{i}(X)=\dim_{\mathbf{R}}H^{i}(X,\mathbf{R})$

is the topological Euler characteristic. Note that the Gauss-Bonet theorem says that $\chi_{\mathrm{top}}(X)=c_{2}(T_{X})$, so this is really a special case of Hirzebruch-Riemann-Roch.

Arbitrary dimension. Consider in general a projective (or just proper) variety $X$ of dimension $n$. For *Cartier* divisors $D_{1},\ldots,D_{n}$ on $X$ one defines an intersection product

$D_{1}\cdot\ldots\cdot D_{n}\in\mathbf{Z}.$

This is required to satisfy the following properties:

(i) If the $D_{i}$ are effective and only meet transversely at smooth points of $X$, then

$D_{1}\cdot\ldots\cdot D_{n}=\#(D_{1}\cap\ldots\cap D_{n}).$

(ii) It is symmetric and multilinear in any combination of entries.

(iii) It depends only on the linear equivalence classes of the $D_{i}$.

One framework for defining these numbers is that of general intersection theory over arbitrary fields as in Fulton’s book *[x10]*. Another is a rather elementary approach using numerical polynomials, developed by Snapper and Kleiman, and explained in detail in Kollár’s book *[x14]* Appendix VI.2. Another approach, over $\mathbf{C}$, is topological: to each $D_{i}$ one can associate the first Chern class

$c_{1}(\mathcal{O}_{X}(D_{i}))\in H^{2}(X,\mathbf{Z}).$

The intersection number is then the cup product

$D_{1}\cdot\ldots\cdot D_{n}:=c_{1}(\mathcal{O}_{X}(D_{1}))\cdot\ldots\cdot c_{1}(\mathcal{O}_{X}(D_{n}))\in H^{2n}(X,\mathbf{Z})\simeq\mathbf{Z}.$

Details on this approach are explained in Lazarsfeld’s book *[x10]* 1.1.C. When $X$ is smooth, these cohomology classes can also be represented by $(1,1)$ forms $\omega_{i}$, and then

$D_{1}\cdot\ldots\cdot D_{n}=\int_{X}\omega_{1}\wedge\cdots\wedge\omega_{n}.$

Note finally that for a Cartier divisor $D$ we can talk in particular about its self-intersection number $D^{n}$.

Now given Cartier divisors $D_{1},\ldots,D_{k}$, and $V\subseteq X$ a closed irreducible subvariety of dimension $k$, one can define an intersection number

$D_{1}\cdot\ldots\cdot D_{k}\cdot V\in\mathbf{Z}.$

Once we have intersection numbers of the type $D_{1}\cdot\ldots\cdot D_{n}$ as above, then just like in the case of surfaces one can compute this seemingly more general $D_{1}\cdot\ldots\cdot D_{k}\cdot V$ by choosing $D^{\prime}_{i}\sim D_{i}$ with support not containing $V$, restricting them to $V$, and then intersecting them on $V$.

###### Theorem 4.11 (Asymptotic Riemann-Roch).

Let $X$ be a projective variety of dimension $n$, $\mathcal{F}$ a coherent sheaf, and $D$ a divisor on $X$. Then $\chi\bigl{(}X,\mathcal{F}\otimes\mathcal{O}_{X}(mD)\bigr{)}$ is a polynomial of degree at most $n$ in $m$, satisfying

$\chi\bigl{(}X,\mathcal{F}\otimes\mathcal{O}_{X}(mD)\bigr{)}=\operatorname{rk}(\mathcal{F})\cdot\frac{D^{n}}{n!}\cdot m^{n}+O(m^{n-1}).$

In particular

$\chi\bigl{(}X,\mathcal{O}_{X}(mD)\bigr{)}=\frac{D^{n}}{n!}\cdot m^{n}+O(m^{n-1}).$

###### Corollary 4.12.

In the setting of the theorem above, provided that we have

$h^{i}\bigl{(}X,\mathcal{F}\otimes\mathcal{O}_{X}(mD)\bigr{)}=O(m^{n-1})\ \text{ for all }i>0,$

then

$h^{0}\bigl{(}X,\mathcal{F}\otimes\mathcal{O}_{X}(mD)\bigr{)}=\operatorname{rk}(\mathcal{F})\cdot\frac{D^{n}}{n!}\cdot m^{n}+O(m^{n-1})\ \text{ for }m\gg 0.$

This holds for instance for $D$ ample, when Serre’s theorem says that all higher cohomology groups are $0$ for $m\gg 0$. It also holds in this weaker form however even when $D$ is nef (see below). As for the proof of Theorem 4.11, this can be done in a rather elementary fashion according to the approach of Snapper-Kleiman (see for instance *[x11]* VI.2.14). It is however also a consequence of the celebrated Hirzebruch-Riemann-Roch theorem, which states that

$\chi\bigl{(}X,\mathcal{F}\otimes\mathcal{O}_{X}(mD)\bigr{)}=\bigl{(}\operatorname{ch}(\mathcal{F}\otimes\mathcal{O}_{X}(mD))\cdot\operatorname{Td}(X)\bigr{)}_{n},$

where $\operatorname{ch}(\cdot)$ denotes the Chern character, and $\operatorname{Td}(\cdot)$ the Todd class, while $(\cdot)_{n}$ denotes the component of top degree $n=\dim X$. It is immediate to see from the definitions that this leads to the formula in Theorem 4.11.

Numerical equivalence. In this section we consider $X$ to be a proper variety (or scheme) over a field.

###### Definition 4.13.

(1) Two Cartier divisors $D_{1}$ and $D_{2}$ on $X$ are *numerically equivalent*, denoted $D_{1}\equiv D_{2}$, if for every irreducible curve $C\subset X$ we have

$D_{1}\cdot C=D_{2}\cdot C.$

We have a similar definition for line bundles. A Cartier divisor $D$ is *numerically trivial* if $D\equiv 0$.

(2) We denote $\mathrm{Num}(X)\subset\mathrm{Div}(X)$ the subgroup of the group of Cartier divisors $\mathrm{Div}$ (X) consisting of numerically trivial divisors. The *Néron-Severi* group of $X$ is the quotient

$N^{1}(X):=\mathrm{Div}(X)/\mathrm{Num}(X),$

i.e. the group of numerical equivalence classes of divisors on $X$. Note that by definition the intersection form descends to

$N^{1}(X)\times\ldots\times N^{1}(X)\longrightarrow\mathbf{Z}.$

###### Example 4.14.

By the definition of the intersection form, if $D_{1}\sim D_{2}$, then $D_{1}\equiv D_{2}$, i.e. linear equivalence implies numerical equivalence. However, note for instance that if $D_{1}$ and $D_{2}$ are different fibers of a mapping $f:X\to C$ with $C$ a smooth projective curve of genus $g(C)\geq 1$, then $D_{1}\equiv D_{2}$, but $D_{1}\not\sim D_{2}$. (More generally, there is a notion of algebraic equivalence, which interpolates between linear and numerical equivalence; see for instance *[x11]* Exercise V.1.7. Such different fibers are in algebraically equivalent.)

As expected, numerical equivalence preserves *all* intersection numbers, and not just those with curves.

###### Lemma 4.15.

Let $X$ be a proper variety, and $D_{1}\equiv D_{1}^{\prime},\ldots,D_{k}\equiv D_{k}^{\prime}$ Cartier divisors on $X$. If $V$ is any $k$-dimensional subvariety of $X$, then

$D_{1}\cdot\ldots\cdot D_{k}\cdot V=D_{1}^{\prime}\cdot\ldots\cdot D_{k}^{\prime}\cdot V.$

###### Proof.

It is enough to show that if $D_{1}\equiv 0$, then $D_{1}\cdot\ldots\cdot D_{k}\cdot V=0$. Indeed, this will show that if $D_{1}\equiv D_{1}^{\prime}$, then

$D_{1}\cdot D_{2}\cdot\ldots\cdot D_{k}\cdot V=D_{1}^{\prime}\cdot D_{2}\cdot\ldots\cdot D_{k}\cdot V,$

and we can then proceed by induction on $k$. But note now that by general intersection theory (either algebraic, or topological), $D_{2}\cdot\ldots\cdot D_{k}\cdot V$ is represented by a $1$-dimensional class on $X$ (linear combination of classes of curves). Therefore the first assertion is clear by definition. ∎

###### Theorem 4.16.

The Néron-Severi group $N^{1}(X)$ is a free abelian group of finite rank. (This rank is called the *Picard* or *base* number of $X$, and is denoted $\rho(X)$.)

###### Proof.

This is true in general, but here I only mention the argument over $\mathbf{C}$, which is immediate using topology. Indeed, we have a group homomorphism

$\mathrm{Pic}(X)\longrightarrow H^{2}(X,\mathbf{Z}),\ \ L\mapsto c_{1}(L),$

and so for any Cartier divisor $D$ on $X$ we get a class

$[D]=c_{1}(\mathcal{O}_{X}(D))\in H^{2}(X,\mathbf{Z}).$

Note that by definition if $[D]=0$, then $D\equiv 0$; in other words $\mathrm{Hom}(X)\subset\mathrm{Num}(X)$, where $\mathrm{Hom}(X)$ is the subgroup of divisors with $[D]=0$ (cohomologically trivial). It follows that $N^{1}(X)$ is a quotient of $\mathrm{Div}(X)/\mathrm{Hom}(X)$. But this latter group is a subgroup of $H^{2}(X,\mathbf{Z})$, and so finitely generated, since $X$ is a compact analytic variety. The fact that $N^{1}(X)$ is torsion-free is immediate from its definition. ∎

## 5. Nef and big line bundles

First, recall one of the famous ampleness criteria; it will be the guiding statement for what follows next.

###### Theorem 5.1 (Nakai-Moishezon ampleness criterion).

Let $X$ be a proper variety over a field, and $L$ a line bundle on $X$. Then $L$ is ample if and only if $L^{\dim V}\cdot V>0$ for any subvariety $V\subseteq X$.

###### Proof.

Assume first that $L$ is ample, so that there is an $m>0$ such that $L^{\otimes m}$ is very ample. We know then that $L^{\otimes m}_{|V}$ is very ample on $V$ as well, and so it provides an embedding in projective space in which

$\deg V=(mL_{|V})^{\dim V}=m^{\dim V}\cdot(L^{\dim V}_{|V})=m^{\dim V}\cdot(L^{\dim V}\cdot V).$

But the degree is obviously a positive integer.

Assume now that $L^{\dim V}\cdot V>0$ for all $V$, and say $n=\dim X$. The result is clear for $n=1$, and we assume by induction that we know it for all varieties of dimension at most $n-1$.

Claim 1: We have

$H^{0}(X,L^{\otimes m})\neq 0\ \ \text{for}\ m\gg 0.$

To prove this, note first that asymptotic Riemann-Roch gives

$\chi(X,L^{\otimes m})=\frac{L^{n}}{n!}\cdot m^{n}+O(m^{n-1}),$

and recall that by assumption $L^{n}>0$. Write now, as we did when we defined intersection numbers:

$L\simeq\mathcal{O}_{X}(D-E),$

with $D$ and $E$ very ample divisors on $X$. We can consider two short exact sequences:

$0\longrightarrow L^{\otimes m}(-E)\stackrel{{\scriptstyle\cdot D}}{{\longrightarrow}}L^{\otimes m+1}\longrightarrow L^{\otimes m+1}_{|D}\longrightarrow 0$

and

$0\longrightarrow L^{\otimes m}(-E)\stackrel{{\scriptstyle\cdot E}}{{\longrightarrow}}L^{\otimes m}\longrightarrow L^{\otimes m}_{|E}\longrightarrow 0.$

Note that by induction $L_{|D}$ and $L_{|E}$ are ample, and so $L^{\otimes m+1}_{|D}$ and $L^{\otimes m}_{|E}$ have vanishing higher cohomology for $m\gg 0$. If we take $i\geq 2$, using both sequences we obtain

$H^{i}(X,L^{\otimes m})\simeq H^{i}(X,L^{\otimes m}(-E))\simeq H^{i}(X,L^{\otimes m+1})$

for $m\gg 0$, and so the higher cohomology for $i\geq 2$ stabilizes. This implies that there exists a constant $C$ such that

$\chi(X,L^{\otimes m})=h^{0}(X,L^{\otimes m})-h^{1}(X,L^{\otimes m})+C$

for $m\gg 0$. But we saw above that $\chi(X,L^{\otimes m})$ grows like a polynomial of degree $n$ in $m$, with positive leading coefficient, so the claim follows (and in fact $L^{\otimes m}$ eventually has lots of sections).

Since $L$ is ample if and only if $L^{\otimes m}$ is ample, given the claim we just proved we can assume from now on that $L={\mathcal{O}}_{X}(D)$ with $D$ effective.

Claim 2: $L^{\otimes m}$ is globally generated for $m\gg 0$.

Note first that this is obvious away from $D$, where $L$ is trivial. So the claim is that no point of $D$ is a base point of $L^{\otimes m}$ for $m\gg 0$. To show this, we can consider the short exact sequence

$0\longrightarrow L^{\otimes m-1}\stackrel{{\scriptstyle\cdot D}}{{\longrightarrow}}L^{\otimes m}\longrightarrow L^{\otimes m}_{|D}\longrightarrow 0.$

We again know by induction that $L_{|D}$ is ample, and therefore by Serre’s theorem $L^{\otimes m}_{|D}$ is globally generated and $H^{1}(D,L^{\otimes m}_{|D})=0$ for $m\gg 0$. This second fact implies that the induced map

$H^{1}(X,L^{\otimes m-1})\longrightarrow H^{1}(X,L^{\otimes m})$

is surjective for $m\gg 0$. It then has to eventually stabilize to an isomorphism, as these spaces are finite dimensional. But then the restriction maps

$H^{0}(X,L^{\otimes m})\longrightarrow H^{0}(D,L^{\otimes m}_{|D})$

must be surjective for $m\gg 0$, and since $L^{\otimes m}_{|D}$ is globally generated, it follows that $L^{\otimes m}$ cannot have base points along $D$. This concludes the proof of the claim.

Again by possibly replacing $L$ by $L^{\otimes m}$, we now want to prove ampleness for a globally generated line bundle $L$ with the property that $L^{\dim V}\cdot V>0$ for all subvarieties $V$. We now in fact only need this when $V$ is a curve; the statement is a consequence of the following Lemma. ∎

###### Lemma 5.2.

A globally generated line bundle $L$ is ample $\Longleftrightarrow\ L\cdot C>0$ for every irreducible curve $C\subset X\iff$ the morphism $\varphi_{L}:X\to{\mathbf{P}}^{n}$ is finite.

###### Proof.

We have that $L\simeq\varphi_{L}^{*}{\mathcal{O}}_{{\mathbf{P}}^{n}}(1)$, and so if $f$ is finite then $L$ is ample. Also, if $L$ is ample, we saw at the beginning of the previous proof that $L\cdot C>0$ for all curves $C$. Finally, assume that $f$ has some fibers that are positive dimensional, and let $C$ be an irreducible curve contained in one such. Since $L$ is a pullback, is restricts to the trivial line bundle on every fiber, and in particular $L_{|C}\simeq{\mathcal{O}}_{C}$. This contradicts the hypothesis $L\cdot C>0$. ∎

###### Corollary 5.3.

If $D_{1}\equiv D_{2}$ are numerically equivalent Cartier divisors on $X$, then $D_{1}$ is ample if and only if $D_{2}$ is ample.

###### Exercise 5.4.

Let $\pi:\tilde{X}={\rm Bl}_{x}(X)\to X$ be the blow-up of a smooth projective variety at a point $x\in X$. Let $H$ be a very ample divisor on $X$, and $E$ the exceptional divisor on $\tilde{X}$. Then $2\pi^{*}H-E$ is an ample divisor. (You can start first with the case $X={\mathbf{P}}^{2}$, and then generalize the argument.)

###### Exercise 5.5.

Let $f:X\to Y$ be a finite surjective morphism of projective varieties, and let $L$ be a line bundle on $Y$. Then $L$ is ample if and only if $f^{*}L$ is ample.

######

###### Definition 5.6 (Q-divisors).

A Q-divisor on a scheme $X$ is a linear combination $D=\sum a_{i}D_{i}$, with $a_{i}\in{\bf Q}$ and $D_{i}$ Cartier divisors. In other words, it is an element of the group

$\operatorname{Div}(X)_{\bf Q}:=\operatorname{Div}(X)\otimes_{\bf Z}{\bf Q}.$

Since intersection numbers are defined for each of the $D_{i}$, they are also defined for $D$, and therefore the intersection pairing extends to $\operatorname{Div}_{\bf Q}(X)$. We can therefore talk about numerical equivalence for Q-divisors, and extend the Néron-Severi group to $N^{1}(X)_{\bf Q}$.

We say that a Q-divisor $D$ is *ample* if there exists $r\in{\bf Z}$ such that $rD$ is an ample Cartier divisor. It is immediate that the Nakai-Moishezon criterion extends to Q-divisors.

### Nef line bundles

We will now study a semi-positivity notion.

###### Definition 5.7.

Let $X$ be a projective (or proper) scheme, and $D$ a Cartier divisor (or a Q-divisor) on $X$. Then $D$ is *nef* if $D\cdot C\geq 0$ for every irreducible curve $C\subseteq X$. We can of course make the same definition for line bundles.

The definition is numerical, and therefore we can actually talk about nef classes in $N^{1}(X)$ or $N^{1}(X)_{\bf Q}$.

###### Example 5.8.

(1) Ample divisors are nef by Nakai-Moishezon.

(2) More generally, semiample (i.e. such that a multiple is basepoint-free) divisors are nef.

(3) Any effective divisor on a homogeneous variety is nef (as we can translate it so it does not contain any given curve).

###### Exercise 5.9.

Let $f:X\to Y$ be a proper and surjective morphism, and $L$ a line bundle on $Y$. Then $L$ is nef if and only if $f^{*}L$ is nef.

###### Exercise 5.10.

Let $D$ and $E$ be Cartier divisors on $X$ such that $mD+E$ is nef for all $m\geq 1$ (or sufficiently large). Then $D$ is nef.

Note however that Nakai-Moishezon suggests a stronger notion of semi-positivity. This is in fact equivalent to nefness by the following important result of Kleiman:

###### Theorem 5.11.

Let $X$ be a proper variety (or scheme), and $D$ a Q-divisor on $X$. Then $D$ is nef if and only if

$D^{\dim V}\cdot V\geq 0$

for every irreducible subvariety $V\subseteq X$.

###### Proof.

I will only prove the statement in the projective case. One implication is clear. Assume now that $D$ is nef. We do induction on $n=\dim X$; the case $n=1$ is clear, and we assume that we know the statement for all proper varieties of dimension at most $n-1$. Thus we know inductively that

$D^{\dim V}\cdot V\geq 0,\ \ \forall\ V\subset X\ \text{of dimension}\ \leq n-1,$

where

and so we only need to show that $D^{n}\geq 0$.

To this end, fix an ample divisor $H$ on $X$, and consider the polynomial in $t\in{\bf R}$:

$P(t):=(D+tH)^{n}=\sum_{k=0}^{n}\binom{n}{k}\cdot t^{n-k}\cdot(D^{k}\cdot H^{n-k}).$

Note that we can formally do this, even though we haven’t talked about ${\bf R}$-divisors in detail; $P$ takes values in ${\bf R}$. Assuming that $P(0)<0$, we want to obtain a contradiction.

By the inductive hypothesis, for $k<n$ we have $D^{k}\cdot H^{n-k}\geq 0$, since $H^{n-k}$ is represented by an effective cycle class of dimension $k$. Thus the coefficients of $t^{n-k}$ in $P(t)$ are non-negative for all $k<n$. This implies that $P^{\prime}(t)>0$ for all $t\geq 0$, and so $P$ is increasing for $t>-\varepsilon$ for some positive $\varepsilon$. Since in addition we are assuming $P(0)<0$, it follows that $P$ has only one real root $a>0$.

We now show that $D+tH$ is ample for any rational number $t>a$. Using Nakai-Moishezon, we need to check that

$(D+tH)^{\dim V}\cdot V>0,\ \ \forall\ V\subseteq X.$

If $V=X$, then this simply says that

$P(t)>P(a)=0\ \ \mbox{for}\ t>a.$

If $V\subsetneq X$, then in the term by term expansion of $(D+tH)^{\dim V}\cdot V$ we have as above that $D^{k}\cdot H^{\dim V-k}\cdot V\geq 0$ for $k>0$, while $H^{\dim V}\cdot V>0$ since $H$ is ample. The claim follows.

Finally, write

$P(t)=Q(t)+R(t),\ \ Q(t)=D\cdot(D+tH)^{n-1},\ \ R(t)=tH\cdot(D+tH)^{n-1}.$

We know that if $t>a$, then $D+tH$ is ample, and so $Q(t)\geq 0$ since $(D+tH)^{n-1}$ is represented by an effective class of dimension 1. By continuity we have that $Q(a)\geq 0$. On the other hand, let’s note that $R(a)>0$, which gives our contradiction since then $P(a)>0$ as well. Indeed, yet again by the same argument as above, all the terms involving both $D$ and $H$ are non-negative, while $H^{n}>0$. ∎

One of the most important interpretations of this theorem is that nef divisors are limits of ample ones. More precisely:

###### Corollary 5.12.

Let $X$ be a projective scheme, and $D$ and $H$ ${\bf Q}$-divisors on $X$. Then:

(1) If $D$ is nef and $H$ is ample, then $D+\varepsilon H$ is ample for all $\varepsilon\in{\bf Q}_{>0}$.

(2) If $D+\varepsilon H$ is ample for all $\varepsilon\in{\bf Q}_{>0}$, then $D$ is nef.

###### Proof.

For (1) we apply Nakai-Moishezon; for every $V\subseteq X$ we have

$(D+\varepsilon H)^{\dim V}\cdot V=\sum_{k=0}^{\dim V}\binom{\dim V}{k}\cdot\varepsilon^{k}\cdot(D^{\dim V-k}\cdot H^{k}\cdot V).$

Since $H$ is ample, $H^{k}\cdot V$ is represented by an effective class of dimension $\dim V-k$ on $V$, and therefore the nefness of $D$ implies by Kleiman’s theorem above that all the terms are non-negative. Moreover, $H^{\dim V}\cdot V>0$, and so the full intersection number is $>0$.

For (2), consider any irreducible curve $C$ in $X$. Since $D+\varepsilon H$ is ample for all $\varepsilon>0$, we know that

$(D+\varepsilon H)\cdot C>0,\ \ \forall\varepsilon>0.$

Passing to the limit as $\varepsilon\to 0$, we obtain $D\cdot C\geq 0$. ∎

Let me finish by indicating that the notion of nefness is crucial in the birational classification of algebraic varieties. Start by recalling that Castelnuovo’s contractibility criterion for surfaces says that if a smooth projective surface $X$ contains a $(-1)$-curve $E$, then there exists a smooth projective surface $Y$ and a birational morphism $f:X\to Y$ which contracts precisely $E$ (the map is in fact the blow-up of a point on $Y$). This leads to the following:

###### Definition 5.13.

A smooth projective surface $X$ is *minimal* if it contains no $(-1)$-curves.

According to Castelnuovo’s criterion, starting with any smooth projective surface, one can always arrive at a minimal one after contracting a finite number of $(-1)$-curves.

###### Proposition 5.14.

Let $X$ be a smooth projective surface with $\kappa(X)\geq 0$. Then $X$ is minimal if and only if $K_{X}$ is nef.

###### Proof.

We have seen that a $(-1)$-curve is a rational curve $E$ such that $E^{2}=-1$, and consequently $K_{X}\cdot E=-1$. Therefore it is clear that if $K_{X}$ is nef, then such a curve cannot exist.

Assume now that $X$ is minimal. Since $\kappa(X)\geq 0$, we can find an effective divisor

$D=\sum a_{i}C_{i}\in|mK_{X}|,\ \ \text{some}\ m>0,$

with $a_{i}>0$ and $C_{i}$ irreducible curves. If $K_{X}$ were not nef, then there would exist $C\subset X$ irreducible curve such that $K_{X}\cdot C<0$, and so then clearly $C=C_{i}$ for some $i$. We then have

$0>D\cdot C\geq a_{i}\cdot(C_{i}\cdot C)$

and so $C^{2}<0$. But now the adjunction formula says

$2p_{a}(C)-2=C^{2}+K_{X}\cdot C$

and the left hand side is at least $-2$, while both numbers on the right hand side are negative. This implies immediately that $C$ is a $(-1)$-curve. ∎

###### Remark 5.15.

In dimension at least $3$, this is taken to be the definition of minimality in a birational equivalence class: a variety with $\kappa(X)\geq 0$ is *minimal* if $K_{X}$ is nef. However, in this case it soon becomes clear that one cannot stay inside the world of smooth varieties; in fact $X$ should be allowed to be a projective normal variety with $K_{X}$ Q-Cartier, and having terminal singularities. Whether such varieties exist in every birational equivalence class is the one of the main topics of the minimal model program.

Big line bundles. Recall that on a smooth projective variety $X$ over a field we have have defined the Iitaka dimension $\kappa(L)$ of a line bundle. The definition and general properties in fact work unchanged if $X$ is only assumed to be normal (and otherwise one obtains a definition by considering the pullback to the normalization). Recall that we have given the following

###### Definition 5.16.

A line bundle $L$ on $X$ is called *big* if $\kappa(L)=\dim X$. Equivalently, there exists a constant $C>0$ such that

$h^{0}(X,L^{\otimes m})\geq C\cdot m^{\dim X}\ \ \text{for}\ m\gg 0.$

We can make the same definition for a Cartier divisor $D$, by considering $L=\mathcal{O}_{X}(D)$. (Moreover, since the definition depends only on sufficiently large and divisible multiples, we can similarly define bigness if $D$ is a $\mathbf{Q}$-divisor.)

###### Example 5.17.

(1) An ample divisor is big. More generally, if $A$ is an ample divisor and $E$ is an effective divisor, then $A+E$ is big. Indeed, note that the number of sections of $\mathcal{O}_{X}(m(A+E))$ is larger than that of $\mathcal{O}_{X}(mA)$, and so the statement follows from asymptotic Riemann-Roch.

(2) If $f:X\to Y$ is a generically finite surjective morphism of proper schemes, and $L$ is a big line bundle on $Y$, then $f^{*}L$ is big on $X$. The most important instance is when $f$ is birational and $L$ is ample; for this reason bigness is sometimes called the birational version of ampleness.

> For the proof, note that we have
>
> $H^{0}(X,f^{*}L^{\otimes m})\simeq H^{0}(Y,f_{*}f^{*}L^{\otimes m})\simeq H^{0}(Y,L^{\otimes m}\otimes f_{*}\mathcal{O}_{X}),$

where for the second equality we applied the projection formula. But since $f$ is surjective, we have an inclusion $\mathcal{O}_{Y}\hookrightarrow f_{*}\mathcal{O}_{X}$, and therefore

$H^{0}(Y,L^{\otimes m})\subset H^{0}(X,f^{*}L^{\otimes m}),\ \ \text{for all}\ m.$

Note also that $\dim X=\dim Y$, since $f$ is generically finite. This immediately implies what we want.

###### Lemma 5.18.

Let $L$ be a big line bundle on $X$, and $M$ any other line bundle. Then

$H^{0}(X,L^{\otimes m}\otimes M)\neq 0$

for $m$ sufficiently large and divisible.

###### Proof.

As usual, write $M\simeq\mathcal{O}_{X}(D-E)$ with $D$ and $E$ very ample divisors. It obviously suffices to replace $M$ by $M(-D)$, i.e. by $\mathcal{O}_{X}(-E)$. Consider now the exact sequence

$H^{0}(X,L^{\otimes m}\otimes\mathcal{O}_{X}(-E))\longrightarrow H^{0}(X,L^{\otimes m})\longrightarrow H^{0}(E,L^{\otimes m}_{|E}).$

We know that there exists $C>0$ such that $h^{0}(X,L^{\otimes m})\geq C\cdot m^{n}$ for $m\gg 0$, where $n=\dim X$. On the other hand, since $E$ is a divisor $h^{0}(E,L^{\otimes m}_{|E})$ grows at most like $m^{n-1}$, and so for $m$ sufficiently large we get the conclusion. ∎

######

The following is Kodaira’s important characterization of big divisors; colloquially, it says that “big is ample plus effective”.

###### Proposition 5.19 (Kodaira’s Lemma).

If $D$ is a big divisor, then for any ample divisor $A$, there exists $m>0$ and an effective divisor $E$ such that $mD\sim A+E$. Conversely, if there exists an ample divisor $A$, an effective divisor $E$, and $m>0$ such that

$mD\equiv A+E,$

then $D$ is big.

###### Proof.

As $A$ is ample, there exists some $a\gg 0$ such that $aD\sim E_{1}$ and $(a+1)A\sim E_{2}$, with $E_{1}$ and $E_{2}$ effective divisors. We apply Lemma 5.18 with $M=\mathcal{O}_{X}(-E_{2})$ to obtain that there exists $m>0$ and an effective divisor $F$ such that

$mD\sim E_{2}+F\simeq A+E_{1}+F.$

We conclude by taking $E=E_{1}+F$.

If $mD\equiv A+E$, then $B=mD-E$ is numerically equivalent to an ample divisor, and hence ample. We then obviously have

$\kappa(D)\geq\kappa(B)=\dim X.$

∎

###### Corollary 5.20.

Bigness is also a numerical property: if $D_{1}\equiv D_{2}$, then $D_{1}$ is big if and only if $D_{2}$ is big.

###### Exercise 5.21.

(1) If $L$ is a big line bundle on $X$, then show that there is a proper closed subset $Z\subset X$ such that $L_{|V}$ is big for every subvariety $V$ of $X$ such that $V\subsetneq Z$.

(2) Give an example of a big line bundle $L$ and a subvariety $V\subset X$ such that $L_{|V}$ is not big.

### Nef and big divisors

The combination of these two notions is particularly powerful, and unlike bigness by itself, it can be characterized by a simple numerical condition. Note that the pullback of an ample divisor by a birational (or generically finite) morphism is big and nef.

###### Theorem 5.22.

Let $X$ be a projective variety of dimension $n$, and $D$ and $E$ nef $\mathbf{Q}$-divisors on $X$. If $D^{n}>n\cdot(D^{n-1}\cdot E)$, then $D-E$ is big.

###### Proof.

Note first that the inequality in the hypothesis still holds if we replace $D$ and $E$ by $D+\varepsilon A$ and $E+\varepsilon A$, where $A$ is an ample divisor and $0<\varepsilon\ll 1$. These are both ample, so after passing then to large multiples, we can assume that both $D$ and $E$ are very ample integral divisors.

Fix now $m>0$, and a divisor $E_{m}\in|mE|$. Consider the short exact sequence

$0\longrightarrow\mathcal{O}_{X}(m(D-E))\xrightarrow{E_{m}}\mathcal{O}_{X}(mD)\longrightarrow\mathcal{O}_{E_{m}}(mD)\longrightarrow 0.$

Since $D$ is very ample, we know that $h^{0}(X,\mathcal{O}_{X}(mD))$ grows like $D^{n}/n!\cdot m^{n}$, and so to conclude it suffices to prove that

$h^{0}(E_{m},\mathcal{O}_{E_{m}}(mD))\leq n\cdot\frac{D^{n-1}\cdot E}{n!}\cdot m^{n}+O(m^{n-1}).$

We are allowed to choose $E_{m}$ as we like, and so we can take $E_{m}=B_{1}+\cdots+B_{m}$, with $B_{i}\in|E|$ general members. A simple argument then shows that it suffices to have

$h^{0}(B_{i},\mathcal{O}_{B_{i}}(mD))\leq n\cdot\frac{D^{n-1}\cdot E}{n!}\cdot m^{n-1}+O(m^{n-2})$

for all $i$. But this is true, with equality, by Riemann-Roch. ∎

###### Corollary 5.23.

Let $X$ be a projective variety of dimension $n$, and $D$ a nef $\mathbf{Q}$-divisor on $X$. Then $D$ is big if and only if $D^{n}>0$.

###### Proof.

If $D^{n}>0$, then Theorem 5.22 applies with $E=0$. Conversely, assume that $D$ is nef and big. By bigness there exists $m>0$, $H$ a very ample divisor, and $E$ an effective divisor, such that

$mD\sim H+E.$

Now Kleiman’s theorem implies that $D^{n-1}\cdot E\geq 0$, and so

$m\cdot D^{n}=(H+E)\cdot D^{n-1}\geq H\cdot D^{n-1}.$

We can however choose $H$ general enough so that $D_{|H}$ is big (using for instance Exercise 5.21), and so reasoning inductively on dimension we get $H\cdot D^{n-1}=D^{n-1}_{|H}>0$. ∎

## 6. Birational classification of surfaces

The following result is crucial in treating birational isomorphism classes of smooth projective surfaces over algebraically closed fields. Its proof is a classical application of Zariski’s Main Theorem; see *[x10]* V.5 for a detailed discussion. Unless otherwise specified, blow-up means blow-up at one point.

###### Theorem 6.1.

A birational morphism of smooth projective surfaces factors as a finite sequence of blow-ups. A birational map between smooth projective surfaces factors as a finite sequence of blow-ups followed by a finite sequence of blow-downs; more precisely, if $X_{1}$ and $X_{2}$ are birational, then there exists a smooth projective surface $Y$ and morphisms $f_{1}:Y\to X_{1}$ and $f_{2}:Y\to X_{2}$ that are both finite compositions of blow-ups.

One thing this tells us is that in order to understand the behavior of various invariants under birational transformations, it is enough to know it for blow-ups. Let’s do a few basic calculations.

###### Proposition 6.2.

Let $X$ be a smooth projective surface, and $x\in X$, and let $\pi:\tilde{X}\to X$ be the blow-up of $X$ at $x$, with exceptional divisor $E$. Then:

(1) $\omega_{\tilde{X}}\simeq\pi^{*}\omega_{X}\otimes\mathcal{O}_{\tilde{X}}(E)$.

(2) $\pi_{*}\mathcal{O}_{\tilde{X}}(mE)\simeq\mathcal{O}_{X}$ for all $m\geq 0$.

(3) $P_{m}(\tilde{X})=P_{m}(X)$ for all $m\geq 0$, and in particular $\kappa(\tilde{X})=\kappa(X)$.

(4)

roof.

(1) Since $\pi$ is an isomorphism outside of $E$, the line bundles $\omega_{\tilde{X}}$ and $\pi^{*}\omega_{X}$ can only differ by something supported on $E$; in divisor language we have

$K_{\tilde{X}}-\pi^{*}K_{X}=aE$

for some $a\in{\bf Z}$. We can now intersect both sides with $E$. On the right hand side we obtain $-a$. On the left hand side, we have $K_{\tilde{X}}\cdot E=-1$, as we computed from the genus formula, and $\pi^{*}K_{X}\cdot E=0$, since $\pi^{*}\omega_{X}$ is trivial along $E$. We obtain that $a=1$.

(2) We proved last quarter using the theorem on formal functions that $\pi_{*}{\mathcal{O}}_{\tilde{X}}\simeq{\mathcal{O}}_{X}$ (and $R^{i}\pi_{*}{\mathcal{O}}_{\tilde{X}}=0$ for $i>0$). This is the case $m=0$; the others follow inductively from the short exact sequences

$0\longrightarrow{\mathcal{O}}_{\tilde{X}}((m-1)E)\stackrel{{\scriptstyle\cdot E}}{{\longrightarrow}}{\mathcal{O}}_{\tilde{X}}(mE)\longrightarrow{\mathcal{O}}_{E}(mE)\longrightarrow 0.$

Indeed, we know that ${\mathcal{O}}_{E}(E)\simeq{\mathcal{O}}_{{\bf P}^{1}}(-1)$, and so since $E$ is contracted to a point,

$\pi_{*}{\mathcal{O}}_{E}(mE)\simeq H^{0}({\bf P}^{1},{\mathcal{O}}_{{\bf P}^{1}}(-m))=0.$

This implies that $\pi_{*}{\mathcal{O}}_{\tilde{X}}((m-1)E)\simeq\pi_{*}{\mathcal{O}}_{\tilde{X}}(mE)$ for all $m\geq 1$.

(3) Using (1) and the projection formula, for every $m\geq 0$ we have that

$H^{0}(\tilde{X},\omega_{\tilde{X}}^{\otimes m})\simeq H^{0}\big{(}X,\omega_{\tilde{X}}^{\otimes m}\otimes\pi_{*}{\mathcal{O}}_{\tilde{X}}(mE)\big{)}.$

But now by (2) we have that $\pi_{*}{\mathcal{O}}_{\tilde{X}}(mE)\simeq{\mathcal{O}}_{X}$, which gives us an isomorphism between the spaces of pluricanonical sections on the two surfaces. ∎

In combination with Theorem 6.1, we obtain the following:

###### Corollary 6.3.

If $X_{1}$ and $X_{2}$ are birational smooth projective surfaces, then $\kappa(X_{1})=\kappa(X_{2})$.

###### Remark 6.4.

Note that the formulas $\pi_{*}{\mathcal{O}}_{\tilde{X}}\simeq{\mathcal{O}}_{X}$ and $R^{i}\pi_{*}{\mathcal{O}}_{\tilde{X}}=0$ for $i>0$, together with the Leray spectral sequence, imply the invariance under blow-ups of other important quantities:

$H^{i}(\tilde{X},{\mathcal{O}}_{\tilde{X}})\simeq H^{i}(X,{\mathcal{O}}_{X}),\ \ \forall i\geq 0.$

In particular, $\chi({\mathcal{O}}_{\tilde{X}})=\chi({\mathcal{O}}_{X})$, and $p_{a}(\tilde{X})=p_{a}(X)$.

The results above imply that if we want to classify surfaces according to Kodaira dimension, it is enough to focus on minimal models, i.e. those that do not contain $(-1)$-curves. Recall that, by Proposition 5.14, for $\kappa(X)\geq 0$ this is equivalent to $\omega_{X}$ being nef.

###### Example 6.5.

Among the surfaces we’ve discussed until now, ${\bf P}^{2}$ is minimal since all curves are very ample, while abelian surfaces and $K3$ surfaces are minimal since $\omega_{X}\simeq{\mathcal{O}}_{X}$. Surfaces of degree at least $5$ in ${\bf P}^{3}$ (i.e. those that are hypersurfaces of general type) are minimal since $\omega_{X}$ is ample.

Let’s see that almost all ruled surfaces are minimal as well. The first claim is that every ruled surface $\pi:X\to C$ with $C$ a curve of genus $g(C)\geq 1$ is minimal. Indeed, assume that $E$ is a rational curve in $X$; the induced map $E\to C$ cannot be surjective since $g(E)<g(C)$ (a consquence of the Riemann-Hurwitz formula), and so $\pi(E)$ is a

point. This means that $E$ is a fiber of $\pi$, and so $E^{2}=0$. Note that if we fix $C$, then all of these minimal models are birational to $C\times\mathbf{P}^{1}$. One can show that these are all the minimal models in this birational class.

Ruled surfaces over $\mathbf{P}^{1}$ are treated in the next example.

###### Example 6.6.

Now consider a rational ruled surface $\pi:X\to\mathbf{P}^{1}$. (Note that these are all birational to $\mathbf{P}^{2}$.) We know that $X=\mathbf{P}(E)$ for some rank $2$ vector bundle $E$ on $\mathbf{P}^{1}$.

###### Proposition 6.7.

Every rank $2$ vector bundle on $\mathbf{P}^{1}$ is decomposable, i.e. a direct sum of two line bundles. In particular, every ruled surface over $\mathbf{P}^{1}$ is isomorphic to

$F_{n}:=\mathbf{P}\big{(}\mathcal{O}_{\mathbf{P}^{1}}\oplus\mathcal{O}_{\mathbf{P}^{1}}(n)\big{)},\ \ \text{for some}\ n\geq 0.$

These are sometimes called *Hirzebruch surfaces*.

###### Proof.

Let $E$ be a rank $2$ vector bundle on $\mathbf{P}^{1}$. Recall that

$\deg E:=\deg(\det E)=\deg(\wedge^{2}E).$

If $L$ is a line bundle, we then have

$\deg(E\otimes L)=\deg\big{(}\wedge^{2}(E\otimes L)\big{)}=\deg(\wedge^{2}E\otimes L^{\otimes 2})=\deg E+2\deg L.$

Thus by twisting with an appropriate $L=\mathcal{O}_{\mathbf{P}^{1}}(m)$, we can assume that $d=\deg E$ is either $0$ or $-1$. The Riemann-Roch theorem for vector bundles on curves says

$\chi(E)=\deg E+\mathrm{rk}E\cdot(1-g),$

so in this particular case we have

$h^{0}(C,E)=h^{1}(C,E)+\deg E+2\geq 1.$

It follows that $E$ has nontrivial sections, and so there is some $k\geq 0$ and a short exact sequence

$0\longrightarrow\mathcal{O}_{\mathbf{P}^{1}}(k)\longrightarrow E\longrightarrow\mathcal{O}_{\mathbf{P}^{1}}(d-k)\longrightarrow 0.$

Thus $E$ is written as an extension of line bundles. These are parametrized by the group

$\mathrm{Ext}^{1}\big{(}\mathcal{O}_{\mathbf{P}^{1}}(d-k),\mathcal{O}_{\mathbf{P}^{1}}(k)\big{)}\simeq H^{1}\big{(}\mathbf{P}^{1},\mathcal{O}_{\mathbf{P}^{1}}(2k-d)\big{)}=0,$

and therefore the extension is split. We get that after twisting by $\mathcal{O}_{\mathbf{P}^{1}}(-k)$ our vector bundle is of the form given in the statement. But recall that $\mathbf{P}(E)\simeq\mathbf{P}(E\otimes M)$ for any line bundle $M$. ∎

###### Exercise 6.8.

With the notation above, show the following statements:

(1) $F_{n}\simeq F_{m}$ if and only if $n=m$.

(2) $F_{n}$ has a section over the base $\mathbf{P}^{1}$ with self-intersection $-n$.

(3) $F_{n}$ is minimal if and only if $n\neq 1$.

(4) $F_{1}\simeq\mathrm{Bl}_{p}(\mathbf{P}^{2})$ for some $p\in\mathbf{P}^{2}$.

(5)

It can be shown that every minimal rational surface is either $\mathbf{P}^{2}$ or one of the $F_{n}$ with $n\neq 1$. Thus overall for surfaces with $\kappa(X)=-\infty$, minimal models are not unique, but they are completely classified. On the other hand, one can show the following result:

###### Theorem 6.9.

Let $X_{1}$ and $X_{2}$ be non-ruled minimal surfaces. Then every birational map from $X_{1}$ to $X_{2}$ is an isomorphism. In particular, every non-ruled minimal surface admits a unique minimal model.

The main theorem in the birational classification of surfaces is the following list of minimal models. I will only state it in characteristic $0$; small modifications have to be made when char $k=p>0$. We use the following standard notation:

$p_{g}(X)=P_{1}(X)=h^{0}(X,\omega_{X})\ \ \text{and}\ \ q(X)=h^{1}(X,\mathcal{O}_{X})=h^{1}(X,\omega_{X}).$

###### Theorem 6.10.

Let $X$ be a minimal surface. Then one of the following holds:

(1) If $\kappa(X)=-\infty$, then $X$ is $\mathbf{P}^{2}$, a rational ruled surface different from $F_{1}$, or a ruled surface over a curve of genus at least $1$.

(2) If $\kappa(X)=0$, then $X$ belongs to one of the following four classes:

- $p_{g}(X)=0$ and $q(X)=0$; in this case $2K_{X}\sim 0$, and we say that $X$ is an *Enriques surface*.
- $p_{g}(X)=0$ and $q(X)=1$; in this case $S$ is a *bielliptic surface*: $S\simeq E\times F/G$, where $E$ and $F$ are elliptic curves, and $G$ is a finite group of translations of $E$ acting on $F$ such that $F/G\simeq\mathbf{P}^{1}$.
- $p_{g}(X)=1$ and $q(X)=0$; in this case $K_{X}\sim 0$, and $X$ is a $K3$ surface.
- $p_{g}(X)=1$ and $q(X)=2$; in this case $X$ is an *abelian surface*.

(3) If $\kappa(X)=1$, then there exists a smooth projective curve $C$ and a surjective morphism $p:X\to C$, such that the general fiber of $p$ is an elliptic curve. Such a surface is called an *elliptic surface*.

(4) If $\kappa(X)=2$, then $X$ is by definition a surface of *general type*.

Note. Much of the general material in this section can be found in *[x10]* Ch.V. The more refined results, including the main classification theorem, are the subject of Beauville’s book *[x2]*. The proof of (2) and some of (1) in Theorem 6.9 is the crux of the matter, and takes a good part of *[x2]*.

###### Example 6.11 (Enriques surfaces).

We have not seen Enriques surfaces before, so let’s establish their existence. First I recall the following general fact:

###### Proposition 6.12.

If $X$ be a variety, then there exists a one-to-one correspondence between étale double covers $\pi:\tilde{X}\to X$ and $2$-torsion line bundles $L$, i.e. $L\neq\mathcal{O}_{X}$ such that $L^{\otimes 2}\simeq\mathcal{O}_{X}$. This is characterized by

$\pi_{*}\mathcal{O}_{\tilde{X}}\simeq\mathcal{O}_{X}\oplus L^{-1}\ \ \text{and}\ \ \pi^{*}L\simeq\mathcal{O}_{\tilde{X}}.$

roof.

I will only sketch the proof, and let you fill in the details. Think of $L$ as a vector bundle of rank $1$ rather than an invertible sheaf, and consider its total space $p:\mathbb{L}\to X$. Fix an isomorphism $\alpha:L^{\otimes 2}\simeq\mathcal{O}_{X}$, so that in vector bundle language we have an isomorphism

$\alpha:\mathbb{L}\otimes\mathbb{L}\longrightarrow X\times\mathbf{C}$

sitting over the identity on $X$. We now consider

$\tilde{X}=\{(x,u)\ |\ \alpha(x,u\otimes u)=(x,1)\}\subset\mathbb{L},$

i.e. via $\alpha$ we put over each $x\in X$ the two roots of unity in $\mathbf{C}$. The projection $p$ induces a morphism $\pi:\tilde{X}\to X$, which is everywhere $2:1$. Also, the mapping

$\tilde{X}\longrightarrow\tilde{X}\times_{X}\mathbb{L}=\pi^{*}\mathbb{L},\ \ (x,u)\mapsto(x,(u,u))$

gives a global section of $\pi^{*}\mathbb{L}$ that does not vanish anywhere. But the existence of such a section equivalent to saying that $\pi^{*}L\simeq\mathcal{O}_{\tilde{X}}$.

On the other hand, if we start with $\pi:\tilde{X}\to X$ as in the statement, the $\mathbf{Z}_{2}$-action on $\pi_{*}\mathcal{O}_{\tilde{X}}$ decomposes it into eigenbundles, and $L^{-1}$ is the nontrivial one. ∎

###### Proposition 6.13.

Let $X$ be an Enriques surface, and $\pi:\tilde{X}\to X$ the étale double cover corresponding to $\omega_{X}$ (recall that $\omega_{X}^{\otimes 2}\simeq\mathcal{O}_{X}$). Then $\tilde{X}$ is a $K3$ surface. Conversely, any quotient of a $K3$ surface by a fixed-point-free involution is an Enriques surface.

###### Proof.

For the first implication, by Proposition 6.12 we have $\pi^{*}\omega_{X}\simeq\mathcal{O}_{\tilde{X}}$. On the other hand, $\pi$ is étale, and so $\pi^{*}\omega_{X}\simeq\omega_{\tilde{X}}$. It follows that $\omega_{\tilde{X}}\simeq\mathcal{O}_{\tilde{X}}$. Note also that since $\pi$ is étale of degree $2$, we have

$2-q(\tilde{X})=\chi(\mathcal{O}_{\tilde{X}})=2\cdot\chi(\mathcal{O}_{X})=2$

and so $q(\tilde{X})=0$. These are the two requirements in the definition of a $K3$ surface.

Assume now that $\pi$ is an étale double cover and $\tilde{X}$ is $K3$. We have

$\pi^{*}\omega_{X}\simeq\omega_{\tilde{X}}\simeq\mathcal{O}_{\tilde{X}}$

and so by the projection formula

$\omega_{X}\otimes\pi_{*}\mathcal{O}_{\tilde{X}}\simeq\pi_{*}\mathcal{O}_{\tilde{X}}.$

But now by Proposition 6.12 we have $\pi_{*}\mathcal{O}_{\tilde{X}}\simeq\mathcal{O}_{X}\oplus\omega_{X}^{-1}$. It follows that $\omega_{\tilde{X}}^{\otimes 2}\simeq\mathcal{O}_{X}$ (pass to determinants), and that $p_{g}(X)=0$. Note also as above that $\chi(\mathcal{O}_{X})=\chi(\mathcal{O}_{\tilde{X}})/2=1$, and so $q(X)=0$. Therefore $X$ is Enriques. ∎

Here is a concrete example. Consider quadrics

$Q_{1},Q_{2},Q_{3}\in k[X_{0},X_{1},X_{2}]\ \ \text{and}\ \ Q_{1}^{\prime},Q_{2}^{\prime},Q_{3}^{\prime}\in k[X_{3},X_{4},X_{5}],$

and using these build the quadrics

$P_{i}=Q_{i}(X_{0},X_{1},X_{2})+Q_{i}^{\prime}(X_{3},X_{4},X_{5})\in k[X_{0},\ldots,X_{5}],\ \ i=1,2,3.$

Assuming that the $Q_{i}$ and $Q_{i}^{\prime}$ are generic, we get three smooth quadrics in $\mathbf{P}^{5}$. Taking the complete intersection

$X=Z(P_{1})\cap Z(P_{2})\cap Z(P_{3})\subset\mathbf{P}^{5}$

we have a complete intersection of type $X_{2,2,2}$, and so $X$ is a $K3$ surface. We now construct a fixed-point-free involution $i$ on $X$; according to Proposition 6.13, we will then have that $X/i$ is an Enriques surface.

To this end, consider first the involution

$\sigma:\mathbf{P}^{5}\longrightarrow\mathbf{P}^{5},\ \ (x_{0}:\cdots:x_{5})\mapsto(x_{0}:x_{1}:x_{2}:-x_{3}:-x_{4}:-x_{5}).$

Clearly $\sigma(X)=X$, and so we have an induced involution $i:X\to X$. Now the fixed locus of $\sigma$ is

$F(\sigma)=Y_{1}\cup Y_{2},\ \ Y_{1}=(x_{0}=x_{1}=x_{2}=0)\text{ and }Y_{2}=(x_{3}=x_{4}=x_{5}=0).$

But as the $Q_{i}$ are generic, they do not have any points in common on $Y_{1}$, and similarly for the $Q_{i}^{\prime}$ on $Y_{2}$ (check!). It follows that $i$ has no fixed points.

###### Remark 6.14.

It can be shown that the generic Enriques surface is isomorphic to one as in the example above.

###### Example 6.15 (Elliptic surfaces).

Let’s also sketch the proof of part (3) in Theorem 6.9, i.e. the fact that minimal surfaces of Kodaira dimension $1$ are elliptic surfaces. We begin with some preliminaries; the surfaces will always be smooth and projective.

###### Lemma 6.16.

If $X$ is a minimal surface with $\kappa(X)=0,1$, then $K_{X}^{2}=0$.

###### Proof.

Since $X$ is minimal, $K_{X}$ is nef, and therefore $K_{X}^{2}\geq 0$. But if we had $K_{X}^{2}>0$, then by Corollary 5.23 $K_{X}$ would be big, which is equivalent to $\kappa(X)=2$. ∎

###### Lemma 6.17.

Let $X$ be a minimal surface with $K_{X}^{2}=0$, and assume that $P_{m}(X)\geq 2$ for some $m$, so that we can write

$|mK_{X}|=|M|+F$

with $F$ the fixed part and $M$ the moving part. Then

$K_{X}\cdot F=K_{X}\cdot M=F^{2}=F\cdot M=M^{2}=0.$

###### Proof.

The hypothesis implies that $K_{X}\cdot M+K_{X}\cdot F=0$. But $K_{X}$ is nef, and so both summands are non-negative. It follows that

$K_{X}\cdot M=K_{X}\cdot F=0.$

Now $M$ does not have fixed components, and so $M^{2}\geq 0$ and $M\cdot F\geq 0$. Using that $M\cdot K_{X}=M^{2}+M\cdot F$ and $F\cdot K_{X}=M\cdot F+F^{2}$, we easily obtain the other identities. ∎

Now start with $X$ minimal with $\kappa(X)=1$. This last condition implies that there exists an $m>0$ such that $P_{m}(X)\geq 2$, i.e. $|mK_{X}|$ is a positive dimensional linear system. Take its decomposition into the moving part and fixed part

$mK_{X}=M+F.$

A priori the moving part gives a rational map $\varphi_{M}:X\to\mathbf{P}^{N}$. By Lemma 6.16 and Lemma 6.17 we have however that $M^{2}=0$, which implies that $\varphi_{M}$ is really a morphism (otherwise different divisors in $M$ would intersect in the finite base locus, giving $M^{2}>0$). The hypothesis also implies that we can take $\varphi_{M}(X)$ to be a curve, say $B$

We now consider the Stein factorization $p:X\to C$ of the induced $\varphi_{M}:X\to B$, so that $p$ has connected fibers and $C$ is a normal and hence smooth curve. Denote by $E$ the general fiber of $p$. Note that

$M\simeq\varphi_{M}^{*}\mathcal{O}_{\mathbf{P}^{N}}(1)\simeq p^{*}\mathcal{O}_{C}(1),$

and so $M$ is linearly equivalent to a sum of general fibers of $p$. By Lemma 6.17 we have that $K_{X}\cdot M=0$. On the other hand, since $K_{X}$ is nef we have that $K_{X}\cdot E\geq 0$. Putting all of this together, it follows that $K_{X}\cdot E=0$.

Note however that since $E$ is a fiber, we also have that $E^{2}=0$. But the genus formula says that $2g(E)-2=E^{2}+K_{X}\cdot E$, so we conclude that $g(E)=1$.

Subadditivity of Kodaira dimension. Note that in all the examples that we had until now, whenever there is a fibration $f:X\to C$ from a smooth projective surface to a smooth projective curve, we have the formula $\kappa(X)=\kappa(F)+\kappa(C)$, where $F$ is the general fiber of $f$. For instance, if $\kappa(X)=-\infty$, we have ruled surfaces and so the fiber also has $\kappa(F)=-\infty$. In the case of $\kappa(X)=1$, we have that $\kappa(F)=0$.

However, it turns out that there are many examples where equality does not hold. In those cases one always has $\kappa(X)>\kappa(F)+\kappa(C)$, so overall the following inequality holds:

$\kappa(X)\geq\kappa(F)+\kappa(C).$

Here are some examples where equality doesn’t hold:

###### Example 6.18.

Some $K3$ surfaces can be written as fibrations $f:X\to\mathbf{P}^{1}$, where the general fiber is an elliptic curve.

In fact, assume that there is a smooth elliptic curve $C\subset X$ inside a $K3$ surface. Then by the genus formula we obtain $C^{2}=0$. Note also that Riemann-Roch gives us

$h^{0}(X,\mathcal{O}_{X}(C))-h^{1}(X,\mathcal{O}_{X}(C))+h^{2}(X,\mathcal{O}_{X}(C))=2.$

On the other hand, since $\omega_{X}\simeq\mathcal{O}_{X}$, Serre duality immediately implies that $h^{2}(X,\mathcal{O}_{X}(C))=0$, while $h^{1}(X,\mathcal{O}_{X}(C))=h^{1}(X,\mathcal{O}_{X}(-C))$. But this last group is also $0$, as it can be seen by passing to cohomology in the exact sequence

$0\longrightarrow\mathcal{O}_{X}(-C)\longrightarrow\mathcal{O}_{X}\longrightarrow\mathcal{O}_{C}\longrightarrow 0.$

It follows that $h^{0}(X,\mathcal{O}_{X}(C))=2$, and so the linear system $|C|$ is a pencil inducing a rational map $f:X\to\mathbf{P}^{1}$. As $C^{2}=0$, it follows (as in the proof of the fact that surfaces with $\kappa(X)=1$ are elliptic) that $f$ is in fact a morphism; its fibers are the members of the pencil, and so the general one is a smooth elliptic curve.

Here is a concrete example when one can find such elliptic curves on a $K3$. Take $X$ to be a smooth quartic surface in $\mathbf{P}^{3}$ containing a line $L$. (Exercise: show that such quartics exist.) Take $H$ to be a hyperplane section of $X$ containing $L$, and then consider the linear system $|H-L|$ on $X$. There is a $1$-dimensional family of planes in $\mathbf{P}^{3}$ containing $L$, and so this is a pencil. Now by Bézout $H$ is a curve of degree $4$, living inside a hyperplane in $\mathbf{P}^{3}$, i.e. a $\mathbf{P}^{2}$. But it contains the line $L$, which must then be a component, so there is a residual component $C$ of degree $3$. One can easily check that $|H-L|$ is a basepoint-free

linear system (exercise), and so the general such $C$ is smooth; it is then a smooth cubic in $\mathbf{P}^{2}$, so an elliptic curve.

###### Example 6.19.

There exist examples of surfaces of Kodaira dimension $1$ such that the base of the elliptic fibration has genus $0$ or $1$.

###### Example 6.20.

There exist surfaces of general type with $q(X)=1$; these takes a little work, but for instance one with $p_{g}(X)=1$ is the minimal resolution of a $C_{1}\times C_{2}/G$, where $C_{1}$ and $C_{2}$ are smooth projective curves of genus $2$ and $3$ respectively, and $G$ is a finite group acting on them, with $C_{1}/G\simeq\mathbf{P}^{1}$ and $C_{2}/G$ elliptic. All such surfaces can be written (via the Albanese map) as fibrations $f:X\to E$, where $E$ is an elliptic curve and the general fiber is a curve of genus at least $2$.

## 7. Iitaka’s conjecture

Considerations as those above, and further work in higher dimensions, led Iitaka to formulate a famous conjecture that was one of the main reasons for the development of the minimal model program. In this section we work with varieties defined over an algebraically closed field $k$ of characteristic $0$.

###### Conjecture 7.1 (Iitaka’s $C_{n,m}$ conjecture).

Let $f:X\to Y$ be a surjective morphism with connected fibers (fiber space) between two smooth projective varieties, and denote by $F$ the generic fiber of $f$. Then

$\kappa(X)\geq\kappa(F)+\kappa(Y).$

###### Remark 7.2.

This is clear when $X$ is of general type, since $\dim X=\dim F+\dim Y$.

The conjecture is known for surfaces, as we will discuss below, but is very hard in general. Very roughly speaking it is known in arbitrary dimension only when $Y$ is of general type, or when $F$ is of general type or has semiample canonical bundle.

Let’s note however that if we replace $\kappa(Y)$ by $\dim Y$, then the inequality is known to go in the other direction. This is a consequence of the more general:

###### Theorem 7.3 (Easy addition formula).

Let $f:X\to Y$ be a fiber space between normal projective varieties, with general fiber $F$, and let $L$ be a line bundle on $X$. Then

$\kappa(X,L)\leq\kappa(F,L_{|F})+\dim Y.$

To prove Easy Addition, as well as other results later, the following technical statement is very useful.

###### Lemma 7.4.

Let $f:X\to Y$ be a fibration with general fiber $F$, and $N$ a line bundle on $X$. Then there exists a big line bundle $L$ on $Y$ and an integer $m>0$ with $f^{*}L\hookrightarrow N^{\otimes m}$ if and only if

$\kappa(X,N)=\kappa(F,N_{|F})+\dim Y.$

I will prove this later, but for now let’s see how it gives the theorem.

###### Proof of Theorem 7.3.

If $\kappa(X,L)=-\infty$ there is nothing to prove. Assuming that $\kappa(X,L)\geq 0$, there exists some $m>0$ such that $H^{0}(X,L^{\otimes m})\neq 0$. Fix now a very ample line bundle $A$ on $Y$. Since $L^{\otimes m}$ has nontrivial sections, we have a sequence of inclusions

$f^{*}A\hookrightarrow L^{\otimes m}\otimes f^{*}A\hookrightarrow(L\otimes f^{*}A)^{\otimes m}.$

(For the second inclusion we use the fact that, since $A$ is very ample, $f^{*}A$ has sections as well.) We can now apply Lemma 7.4 to $N=L\otimes f^{*}A$ to conclude that

$\kappa(X,L\otimes f^{*}A)=\kappa(F,L_{|F})+\dim Y.$

But since $f^{*}A$ is effective, we clearly have

$\kappa(X,L\otimes f^{*}A)\geq\kappa(X,L).$

###### Corollary 7.5.

Under the hypotheses of Conjecture 7.1, we have

$\kappa(X)\leq\kappa(F)+\dim Y.$

In particular, if $\kappa(X)\geq 0$, then $\kappa(F)\geq 0$.

###### Proof.

This is a consequence of Theorem 7.3 applied to $L=\omega_{X}$, and the following exercise. ∎

###### Exercise 7.6.

Let $f:X\to Y$ be a fiber space between smooth projective varieties. Then for every smooth fiber $F$ of $f$, we have

$\omega_{F}\simeq\omega_{X|F}.$

Intuitive approach to the conjecture. Let $f:X\to Y$ be a fiber space between smooth projective varieties. Denote

$\mathcal{F}_{m}:=f_{*}\omega_{X/Y}^{\otimes m},\ \ m\geq 1.$

Since $f$ is generically flat, at a general point of $y$ we can apply the Base Change theorem and deduce that $\mathcal{F}_{m}$ is a (torsion-free, more on this later) coherent sheaf on $Y$ of rank

$\operatorname{rk}(\mathcal{F}_{m})=P_{m}(F)=h^{0}(F,\omega_{F}^{\otimes m}).$

By the projection formula we have

$f_{*}\omega_{X}^{\otimes m}\simeq\mathcal{F}_{m}\otimes\omega_{Y}^{\otimes m},$

and so

$P_{m}(X)=h^{0}(Y,\mathcal{F}_{m}\otimes\omega_{Y}^{\otimes m}),\ \ \forall\ m\geq 1.$

As we will see later, one of the key properties all fiber spaces is that they come with naturally attached positivity properties, reflected precisely in the canonically defined sheaves $\mathcal{F}_{m}$. It is not quite true that they are globally generated, but these properties go roughly in this direction; let’s assume now for intuition that we were actually able to prove that $\mathcal{F}_{m}$ are globally generated. We can then apply Exercise 7.7 below to deduce that there exists a sheaf inclusion

$\bigoplus_{\operatorname{rk}(\mathcal{F}_{m})}\omega_{Y}^{\otimes m}\hookrightarrow\mathcal{F}_{m}\otimes\omega_{Y}^{\otimes m}.$

Putting everything together, we would conclude that

$P_{m}(X)\geq P_{m}(F)\cdot P_{m}(Y),$

which after comparing the rate of growth on the two sides would imply the inequality in Conjecture 7.1.

###### Exercise 7.7.

Let $\mathcal{F}$ be a globally generated coherent sheaf of generic rank $r$ on a variety $X$. Then there exists an sheaf inclusion

$\mathcal{O}_{X}^{\oplus r}\hookrightarrow\mathcal{F}.$

### Calabi-Yau fibers

Some of you are particularly interested in Calabi-Yau varieties, or families thereof, and so let’s see how the previous discussion simplifies further if we assume $\omega_{F}\simeq\mathcal{O}_{F}$ for the general fiber of $F$. We have in particular $\operatorname{rk}(\mathcal{F}_{m})=1$ for all $m\geq 1$, and one only needs to show that $\kappa(X)\geq\kappa(Y)$.

Let’s note that in this case it is enough to show that $H^{0}(Y,\mathcal{F}_{m})\neq 0$ for some $m$. Indeed, this would imply that

$\omega_{Y}^{\otimes m}\hookrightarrow\mathcal{F}_{m}\otimes\omega_{Y}^{\otimes m},$

and so $P_{m}(X)\geq P_{m}(Y)$. But then this would in fact happen for all multiples of $m$. To see this, let’s simplify the discussion by assuming that $m=1$. This means that

$h^{0}(X,\omega_{X/Y})=h^{0}(Y,f_{*}\omega_{X/Y})\neq 0.$

This basically says that “$K_{X}\geq K_{Y}$”. By taking powers of a non-zero section on $X$, we obtain that

$h^{0}(X,\omega_{X/Y}^{\otimes k})=h^{0}(Y,\mathcal{F}_{k})\neq 0,\ \ \forall\ k\geq 1.$

The actual proof indeed goes via producing nontrivial sections, but not directly for $\mathcal{F}_{m}$. Also, note that in the previous subsection I could have actually said *generically* globally generated, and the argument would be the same; but in the case when $\operatorname{rk}(\mathcal{F}_{m})=1$, this means precisely the existence of a non-trivial section, so this is really a special case of what we discussed above.

### Iitaka’s conjecture for surfaces

Let $f:X\to C$ be a fiber space with $X$ a smooth projective surface and $C$ a smooth projective curve. To check Iitaka’s conjecture, we can safely assume that

$g(C)\geq 1\ \ \text{and}\ \ g(F)\geq 1.$

In this case we can also assume that $X$ is a minimal surface, since the all rational curves must then live in the fibers of $f$, and the Kodaira dimension is a birational invariant.

The problem can be approached without using the classification of surfaces, but this is part of a more general program of which we’ll discuss a bit later. But even using classification, let’s note that the elementary results we know are not enough in the case $\kappa(X)=0$.

First the other cases: we saw that $\kappa(X)=2$ is clear. Since besides $\mathbf{P}^{2}$ in the $\kappa(X)=-\infty$ case we only have ruled surfaces, this case is also clear (again, rational curves cannot dominate curves of higher genus). Now a minimal surface with $\kappa(X)=1$ has a, possibly different, fibration $g:X\to B$, with general fiber $E$ an elliptic curve. Now compare $E$ with the fibration $f:X\to C$. If $g(C)\geq 2$, then $E$ cannot dominate $C$, and so it must be a fiber of $f$ as well. It follows that then that $f$ and $g$ must coincide, so $f$ is also an elliptic fibration and we are done. If $g(C)\leq 1$, then we are done anyway.

Thus the only case that is not clear is $\kappa(X)=0$. One must show that $g(C)=1$ and $g(F)=1$, but there is nothing in the classification list that tells us yet that this is the case. The key point is the following completely nontrivial result, first observed by Ueno in this case, and then generalized by Fujita, Kawamata, Viehweg, etc. in various ways to higher dimension, which we will discuss later:

###### Theorem 7.8.

If $f:X\to C$ is a fiber space as above, then $\deg f_{*}\omega_{X/C}\geq 0$.

This is a concrete instance of the fact alluded to earlier that every family comes with some inherent positivity. Let’s apply this: assume for instance that $\omega_{X}\simeq\mathcal{O}_{X}$, like in the $K3$ or abelian case. Since $f_{*}\mathcal{O}_{X}\simeq\mathcal{O}_{C}$ by the fiber space assumption, we have that

$\deg f_{*}\omega_{X/C}=\deg\omega_{C}^{-1}=2-2g(C)\geq 0,$

and so $g(C)\leq 1$. On the other hand $\omega_{X|F}\simeq\omega_{F}\otimes\mathcal{O}_{F}(-F)$. But $F^{2}=0$ since $F$ is a fiber, and so we get that $\deg\omega_{F}=0$, which means that $F$ is an elliptic curve. (Or simply apply Exercise 7.6 directly.)

In the Enriques or bielliptic case the canonical is not trivial, but only torsion. The exact same argument shows in any case that $F$ must be an elliptic curve. As for $C$, one can argue by taking a base change $C^{\prime}\to C$ of the base which makes the canonical of $X$ trivial, or apply directly as above an important generalization of Theorem 7.8 which says that in fact

$\deg f_{*}\omega_{X/C}^{\otimes m}\geq 0,\ \ \forall\ m\geq 1.$

We will come back to this result in a more general context. To address positivity results of this sort, one of the most important tools are vanishing theorems for cohomology groups, and we will study this next.

## 8. Vanishing theorems

In this section we deal only with varieties defined over $\mathbf{C}$. The results can be shown to hold for all algebraically closed fields in characteristic $0$, but are known to fail as stated in positive characteristic. We start with perhaps the best known vanishing theorem.

###### Theorem 8.1 (Kodaira Vanishing).

Let $X$ be a smooth complex projective variety of dimension $n$, and let $L$ be an ample line bundle on $X$. Then

$H^{i}(X,\omega_{X}\otimes L)=0\ \text{for all}\ i>0.$

Equivalently,

$H^{i}(X,L^{-1})=0\ \text{for all}\ i<n.$

Kodaira Vanishing is the special case $p=n$ of the following result about all bundles of holomorphic forms.

###### Theorem 8.2 (Nakano Vanishing).

Let $X$ be a smooth complex projective variety of dimension $n$, and $L$ an ample line bundle on $X$. Then

$H^{q}(X,\Omega_{X}^{p}\otimes L)=0\ \text{for}\ p+q>n,$

and

or equivalently

$H^{q}(X,\Omega^{p}_{X}\otimes L^{-1})=0\ \ \text{for}\ p+q<n.$

In these notes I will prove these theorems using a method first introduced by Kollár, based on what are called injectivity theorems. The approach to the proof is due to Esnault-Viehweg; a lot about this can be found in their book *[x11]*.

###### Definition 8.3 (Forms with log-poles).

Let $X$ be a smooth variety, and $D$ a smooth effective divisor on $X$. The sheaf of 1-forms on $X$ with log-poles along $D$ is

$\Omega^{1}_{X}(\log D)=\Omega^{1}_{X}<\frac{df}{f}>,\ f\ \text{local equation for}\ D.$

Concretely, if $z_{1},\ldots,z_{n}$ are local coordinates on $X$, chosen such that $D=(z_{n}=0)$, then $\Omega^{1}_{X}(\log D)$ is locally generated by $dz_{1},\ldots,dz_{n-1}$, $\frac{dz_{n}}{z_{n}}$. This is a free system of generators, so $\Omega^{1}_{X}(\log D)$ is locally free of rank $n$. For any integer $p$, we define

$\Omega^{p}_{X}(\log D):=\bigwedge^{p}\big{(}\Omega^{1}_{X}(\log D)\big{)}.$

###### Lemma 8.4.

There are short exact sequences:

(i) $0\longrightarrow\Omega^{p}_{X}\longrightarrow\Omega^{p}_{X}(\log D)\longrightarrow\Omega^{p-1}_{D}\longrightarrow 0$.

(ii) $0\longrightarrow\Omega^{p}_{X}(\log D)(-D)\longrightarrow\Omega^{p}_{X}\longrightarrow\Omega^{p}_{D}\longrightarrow 0$.

###### Proof.

I will sketch the proof for $p=1$; in general it is only notationally more complicated. The comprehensive source for this is *[x11]* Section 2.

Choose local analytic coordinates $z_{1},\ldots,z_{n}$ so that $D=(z_{n}=0)$. For (i), the map on the right is the *residue map* along $D$

$\text{res}_{\text{D}}:\Omega^{1}_{X}(\log D)\longrightarrow\mathcal{O}_{D}$

given by

$f_{1}dz_{1}+\cdots+f_{n-1}dz_{n-1}+f_{n}\frac{dz_{n}}{z_{n}}\mapsto f_{n|D},$

where $f_{1},\ldots,f_{n}$ are local functions on $X$. The right hand side is $0$ if one can write $f=z_{n}\cdot g$ for an arbitrary regular function $g$. Therefore we can see the kernel as being locally generated by $dz_{1},\ldots,dz_{n}$, hence isomorphic to $\Omega^{1}_{X}$.

For (ii), the map on the right is given by restriction of forms. Since locally $D=(z_{n}=0)$, the kernel of the restriction map $\Omega^{1}_{X}\to\Omega^{1}_{D}$ is locally generated by $z_{n}dz_{1},\ldots,z_{n}dz_{n-1},dz_{n}$. But these obviously generate the subsheaf $\Omega^{1}_{X}(\log D)(-D)\subset\Omega^{1}_{X}(\log D)$. ∎

###### Cyclic covers.

I will state here a useful technical result needed in order to “take $m$-th roots” of divisors $B\in|mD|$ with $m\geq 2$. For a thorough survey and other useful covering constructions see *[x17]* 4.1.B and *[x11]* Section 3.

###### Proposition 8.5.

Let $X$ be a variety over an algebraically closed field $k$, and let $L$ be a line bundle on $X$. Let $0\neq s\in H^{0}(X,L^{\otimes m})$ for some $m\geq 1$, with $D=Z(s)\in|mL|$.

Then there exists a finite flat morphism $f:Y\to X$ of degree $m$, where $Y$ is a scheme over $k$ such that if $L^{\prime}=f^{*}L$, there is a section

$s^{\prime}\in H^{0}(Y,L^{\prime})\text{ satisfying }\left(s^{\prime}\right)^{m}=f^{*}s.$

Moreover:

$\bullet$ if $X$ and $D$ are smooth, then so are $Y$ and $D^{\prime}=Z(s^{\prime})$.

$\bullet$ the divisor $D^{\prime}$ maps isomorphically onto $D$.

$\bullet$ there is a canonical isomorphism $f_{*}\mathcal{O}_{Y}\simeq\mathcal{O}_{X}\oplus L^{-1}\oplus\cdots\oplus L^{-(m-1)}$.

$\bullet$ for every $p\geq 1$, one has

$f_{*}\Omega_{Y}^{p}\simeq\Omega_{X}^{p}\oplus\bigoplus_{i=1}^{m-1}\Omega_{X}^{p}(\log\,D)\otimes L^{-i}.$

###### Proof.

Let’s first do this construction locally: assume that $X=\operatorname{Spec}A$, and think of $s$ as a function $s\in A$. Then, introducing a new variable $t$, one can simply define

$Y=\operatorname{Spec}\frac{A[t]}{(t^{m}-s)}\subset X\times\mathbf{A}^{1}.$

The natural morphism from $A$ to this new ring (or the projection onto the first factor of $X\times\mathbf{A}^{1}$) induces a map $f:Y\to X$, which is clearly finite. If $X$ and $D$ are smooth, we can more specifically assume that $X$ has a coordinate system $x_{1},\ldots,x_{n}$ such that $s=x_{1}$. Then $Y$ has a coordinate system $y_{1},\ldots,y_{n}$ with $t=y_{1}$, so that the map $f$ can be described as

(4) $(y_{1},y_{2},\ldots,y_{n})\mapsto(y_{1}^{m},y_{2},\ldots,y_{n}).$

It follows that $Y$ is smooth as well, and we also see that $f$ is ramified exactly over $D=(x_{1}=0)$, where it is in fact maximally ramified. Note moreover that $D^{\prime}=(y_{1}=0)$ maps isomorphically onto $D$.

Note furthermore that the ring $B=A[t]/(t^{m}-s)$, which can be identified with the sheaf $f_{*}\mathcal{O}_{Y}$, admits a decomposition

(5) $B=\bigoplus_{i=0}^{m-1}A\cdot t^{i},$

and we know that $t^{m}=s\in A$. Now the group $\mu_{m}$ of $m$-th roots of unity acts on $B$ (so on $Y$) as follows: if $\mu$ is a primitive $m$-th root, then $\mu$ acts on $t$ by $\mu\cdot t$. It is clear that the eigenspace associated to $\mu^{i}$ is precisely the summand $A\cdot t^{i}$ in the decomposition above.

This is the local version. Now start with global $X$ and $D$, where $D$ is a divisor associated to a section $s$ of $L^{\otimes m}$. Choose an affine open cover of $X$ on which $L$ can be trivialized, and for each open $U_{i}\subset X$ in this cover, think of $s_{U_{i}}$ as a function $s_{i}$ on $U_{i}$. The construction above can be performed to get

$f_{i}:Y_{i}=\operatorname{Spec}\frac{\mathcal{O}_{X}(U_{i})[t_{i}]}{(t_{i}^{m}-s_{i})}\longrightarrow U_{i}.$

$U_{i}$ and $U_{j}$ are open sets in the cover, the line bundle comes with transition functions $g_{ij}\in\mathcal{O}_{X}^{*}(U_{i}\cap U_{j})$; the transition functions of $L^{\otimes m}$ are therefore $g_{ij}^{m}$, so the $s_{i}$ satisfy

$s_{i}=g_{ij}^{m}\cdot s_{j}.$

We can now glue $Y_{i}$ and $Y_{j}$ over $U_{i}\cap U_{j}$ by using the rule

(6) $t_{i}=g_{ij}\cdot t_{j},$

which is compatible with the formula above since $t_{i}^{m}=s_{i}$. We get a variety $Y$, due to the fact that the gluing behaves well on triple overlaps because of the cocyle condition

$g_{ij}\cdot g_{jk}\cdot g_{ki}=1$

satisfied by the transition functions. The $g_{ij}$ are also the transition functions of the line bundle $L^{\prime}=f^{*}L$, and so (6) implies that the $t_{i}$ glue to give a global section $t\in H^{0}(Y,L^{\prime})$. Obviously $t^{m}=f^{*}s$. Since $f$ is a finite morphism, if $X$ is projective then $Y$ is projective as well. Also, the considerations in the local case apply to say that if $X$ and $D$ are smooth, then $Y$ is also smooth.

Finally, we need to establish the decomposition formulas for push-forwards of bundles of holomorphic forms. Using an open cover as above, recall that over $U_{j}$ the sheaf $f_{*}\mathcal{O}_{Y}$ can be described as the $A_{i}$-algebra

$B_{j}:=\operatorname{Spec}\,\frac{A_{j}[t_{j}]}{(t_{j}^{m}-s_{j})}=\bigoplus_{i=0}^{m-1}A_{j}\cdot t_{j}^{i},$

where the decomposition into a direct sum of free rank 1 $A_{j}$-modules on the right hand side corresponds to the eigenspaces of the $\mu_{m}$-action. Each of these glue to a line bundle; note that since the $t_{j}^{i}$ transform according to the formula

$t_{j}^{i}=g_{jk}^{i}\cdot t_{k}^{i},$

it follows that this line bundle is that given by the transition functions $g_{jk}^{-i}$, i.e. $L^{-i}$. This proves the formula for $f_{*}\mathcal{O}_{Y}$.

Let’s conclude by proving the formula for $f_{*}\Omega_{Y}^{1}$; that for arbitrary $p$ is left as an exercise. On one of the open sets $U_{j}$ of our cover, consider a local coordinate system $x_{1}\ldots,x_{n}$ on $X$ such that $D=(x_{1}=0)$ as above, so that $\Omega_{X}^{1}(\log\,D)$ is generated by $dx_{1}/x_{1},dx_{2},\ldots,dx_{n}$. Consider also a coordinate system $y_{1},\ldots,y_{n}$ on $Y$ so that the mapping is given by (4), and $t_{j}$ corresponds to $y_{1}$. Over $U_{j}$ we have

$f_{*}\Omega_{Y}^{1}(U_{j})\simeq\bigoplus_{k=1}^{n}B_{j}\cdot dy_{k}\simeq\bigoplus_{k=1}^{n}\bigoplus_{i=0}^{m-1}A_{j}\cdot y_{1}^{i}dy_{k}.$

Note now that for $k\geq 2$ we have $y_{1}^{i}dy_{k}=y_{1}^{i}dx_{k}$. For $k=1$, the formula $x_{1}=y_{1}^{m}$ implies that $dx_{1}=m\cdot y_{1}^{m-1}dy_{1}$, and in particular $dx_{1}/x_{1}=m\cdot dy_{1}/y_{1}$. We conclude that

$y_{1}^{i}dy_{1}=\frac{1}{m}y_{1}^{i+1}\frac{dx_{1}}{x_{1}}.$

The eigenspaces of $f_{*}\Omega_{Y}^{1}(U_{j})$ under the action of $\mu_{m}$ are obtained by putting together the terms which contain the same power of $y_{1}$, and one easily checks that they correspond to the summands in the statement. ∎

We will use Proposition 8.5 and some basic information coming from Hodge theory in order to prove the following “injectivity theorem”, originally due to Kollár, which turns out to be stronger than Kodaira vanishing.

###### Theorem 8.6.

Let $X$ be a smooth projective variety, $L$ a line bundle on $X$, and a non-trivial section $s\in H^{0}(X,L^{\otimes m})$ such that $D=Z(s)$ is a smooth divisor. Then, for each $j$, the map

$H^{j}(X,\omega_{X}\otimes L)\longrightarrow H^{j}(X,\omega_{X}\otimes L^{\otimes m+1})$

induced by multiplication by $s$ is injective.

###### Proof.

We use the construction and notation of Proposition 8.5. Since $f$ is finite, we obtain isomorphisms

$H^{j}(Y,\mathcal{O}_{Y})\simeq H^{j}(X,\mathcal{O}_{X})\oplus\bigoplus_{i=1}^{m-1}H^{j}(X,L^{-i})$

and

$H^{j}(Y,\Omega_{Y}^{p})\simeq H^{j}(X,\Omega_{X}^{p})\oplus\bigoplus_{i=1}^{m-1}H^{j}(X,\Omega_{X}^{p}(\log\,D)\otimes L^{-i}).$

We consider now the exterior derivative

$d:\mathcal{O}_{Y}\longrightarrow\Omega_{Y}^{1},$

which is a $\mathbf{C}$-linear sheaf homomorphism. This induces for each $j$ a homomorphism on cohomology

$d:H^{j}(Y,\mathcal{O}_{Y})\longrightarrow H^{j}(Y,\Omega_{Y}^{1}).$

But Hodge theory tells us that this homomorphism is always zero; this is a special case of the degeneration at $E_{1}$ of the Hodge-to-de Rham spectral sequence. In more elementary terms, the reason is that these two spaces are isomorphic to the spaces $H^{0,j}(Y)$ and $H^{1,j}(Y)$ of forms of the corresponding types. But each element in $H^{0,j}(Y)$ can be represented by a harmonic form, and all such forms are $d$-closed.

Note that $d$ is compatible with the decompositions above (exercise; see also the proof of Lemma 8.7 below), and so it induces maps

$d:H^{j}(X,L^{-1})\longrightarrow H^{j}(X,\Omega_{X}^{1}(\log\,D)\otimes L^{-1})$

which are also identically zero. Now recall from Lemma 8.4 that we have a residue mapping $\Omega_{X}^{1}(\log\,D)\to\mathcal{O}_{D}$. Tensoring it with $L^{-1}$ and passing to cohomology, we finally get that the induced homomorphism

$H^{j}(X,L^{-1})\longrightarrow H^{j}(D,L_{|D}^{-1})$

is zero as well. But Lemma 8.7 below tells us that up to scalar this is the same as the homomorphism induced from the short exact sequence

$0\longrightarrow L^{-1}(-D)\longrightarrow L^{-1}\longrightarrow L_{|D}^{-1}\longrightarrow 0.$

Looking at the long exact sequence on cohomology, it follows that the induced homomorphisms

$H^{j}(X,L^{-1}(-D))\longrightarrow H^{j}(X,L^{-1})$

are all surjective. Recalling that $L^{\otimes m}\simeq\mathcal{O}_{X}(D)$, Serre duality implies the statement we want. ∎

###### Lemma 8.7.

The homomorphism

$H^{j}(X,L^{-1})\longrightarrow H^{j}(D,L_{|D}^{-1})$

above, obtained using the residue map, is the same as the natural homomorphism induced by restriction, after multiplication by $m$.

###### Proof.

We in fact prove the pre-cohomology statement that the mapping

$L^{-1}\longrightarrow\Omega_{X}^{1}(\log\,D)\otimes L^{-1}\longrightarrow L_{|D}^{-1}$

obtained by composing $d$ on the eigensheaves corresponding to $\mu$ with the residue map along $D$ is equal to the restriction map up to a factor of $m$. We are then allowed to work in local coordinates, and we use the notation in the proof of Proposition 8.5.

In local coordinates on an open set $U$, the summand $L^{-1}$ of $f_{*}\mathcal{O}_{Y}$ is generated by elements of the form $fy_{1}$, with $f\in\mathcal{O}_{X}(U)$. Note that

$d(fy_{1})=dfy_{1}+fdy_{1}=y_{1}\left(df+\frac{f}{m}\cdot\frac{dx_{1}}{x_{1}}\right),$

which is a section of $\Omega_{X}^{1}(\log\,D)\otimes L^{-1}$ over $U$. Its residue along $(x_{1}=0)$ is equal to $y_{1}\cdot\frac{f}{m}$ restricted to $(x_{1}=0)$, which after multiplication by $m$ coincides with the restriction of $fy_{1}$. ∎

###### Proof of Theorem 8.1 using Theorem 8.6.

Let $L$ be an ample line bundle. Then there exists $m\gg 0$ such that $L$ is very ample and

$H^{i}(X,\omega_{X}\otimes L^{\otimes m+1})=0\quad\text{for all}\ \ i>0.$

But the linear system $|mL|$ contains a smooth divisor, so we can apply Theorem 8.6 to deduce that $H^{i}(X,\omega_{X}\otimes L)$ embeds in this space.

Kollár vanishing. Theorem 8.6 also leads to important generalization of Kodaira Vanishing to higher direct images of canonical bundles; the point is to use the more general case when $L$ is not necessarily ample.

###### Theorem 8.8 (Kollár Vanishing).

Let $f:X\to Y$ be a morphism from a smooth projective variety $X$ to a projective variety $Y$, and let $L$ be an ample line bundle on $Y$. Then

$H^{j}(Y,R^{i}f_{*}\omega_{X}\otimes L)=0,\ \ \text{for all}\ i\ \text{and all}\ j>0.$

###### Proof.

Let $m$ be a sufficiently large integer such that $L^{\otimes m}$ is very ample. If $B\in|mL|$ is a general element and $D=f^{*}B$, then by Bertini’s theorem $D$ is a smooth hypersurface on $X$. We apply Theorem 8.6 to the (semiample) line bundle $f^{*}L$ and to the divisor $D$ on $X$, to conclude that the natural maps

(7) $H^{j}(X,\omega_{X}\otimes f^{*}L)\overset{D}{\longrightarrow}H^{j}(X,\omega_{X}\otimes f^{*}L^{\otimes m+1})$

are injective for all $j$. Let’s denote

$f_{D}:D\longrightarrow B$

the restriction of $f$ to $D$. By induction on dimension, we can assume that

$H^{j}(Y,R^{i}f_{D_{*}}\omega_{D}\otimes L_{|B})=0,\ \ \text{for all $i$ and all $j>0$}.$

Note now that by the adjunction formula $\omega_{D}\simeq(\omega_{X}\otimes\mathcal{O}_{X}(D))_{|D}$. On the other hand $\mathcal{O}_{X}(D)\simeq f^{*}L^{\otimes m}$, so

$\omega_{D}\simeq\omega_{X|D}\otimes g^{*}L^{\otimes m}_{|B}.$

It follows that we have a short exact sequence

$0\longrightarrow\omega_{X}\otimes f^{*}L\longrightarrow\omega_{X}\otimes f^{*}L^{\otimes m+1}\longrightarrow\omega_{D}\otimes f_{D}^{*}L_{|B}\longrightarrow 0.$

Pushing this sequence forward, we obtain a long exact sequence

$\cdots\longrightarrow R^{i}f_{*}\omega_{X}\otimes L\stackrel{{\scriptstyle\cdot B}}{{\longrightarrow}}R^{i}f_{*}\omega_{X}\otimes L^{\otimes m+1}\longrightarrow R^{i}f_{D_{*}}\omega_{D}\otimes L_{|B}\longrightarrow\cdots$

We can however choose the divisor $B$ sufficiently general, such that the mapping

$R^{i}f_{*}\omega_{X}\otimes L\stackrel{{\scriptstyle\cdot B}}{{\longrightarrow}}R^{i}f_{*}\omega_{X}\otimes L^{\otimes m+1}$

is in fact injective; this follows from Lemma 8.9 below. In this case the long exact sequence above reduces to a collection of short exact sequences

$0\longrightarrow R^{i}f_{*}\omega_{X}\otimes L\stackrel{{\scriptstyle\cdot B}}{{\longrightarrow}}R^{i}f_{*}\omega_{X}\otimes L^{\otimes m+1}\longrightarrow R^{i}f_{D_{*}}\omega_{D}\otimes L_{|B}\longrightarrow 0$

We can also choose $m$ large enough so that the higher cohomology of all $R^{i}f_{*}\omega_{X}\otimes L^{\otimes m+1}$ vanishes. Combined with the inductive assumption about the right-most sheaf, this implied first of all that

$H^{j}(Y,R^{i}f_{*}\omega_{X}\otimes L)=0,\ \ \forall\ j\geq 2.$

For the final case $j=1$ we need to use the Leray spectral sequence

$E_{2}^{p,q}=H^{p}(Y,R^{q}f_{*}\omega_{X}\otimes L)\implies H^{p+q}(X,\omega_{X}\otimes f^{*}L).$

We have already shown that $E_{2}^{p,q}=0$ for $p\geq 2$ and all $q$, which implies that the spectral sequence degenerates at $E_{2}$. This means in particular that for all $i$ we have an injection

$E_{2}^{1,i}=H^{1}(Y,R^{i}f_{*}\omega_{X}\otimes L)\hookrightarrow H^{i+1}(X,\omega_{X}\otimes f^{*}L).$

On the other hand, by (7) this last group injects into $H^{i+1}(X,\omega_{X}\otimes f^{*}L^{\otimes m+1})$. But the composition of these two injections also factors as in the following commutative diagram

where the bottom left term is $0$ for $m\gg 0$ by Serre Vanishing. We finally conclude that

$H^{1}(Y,R^{i}f_{*}\omega_{X}\otimes L)=0$

as well.

Mihnea Popa

Lemma 8.9. Let  $\mathcal{F}$  be a coherent sheaf and  $L$  a very ample line bundle on a projective variety  $X$ . If  $s \in H^0(X, L)$  is a general section, then the induced morphism

$$
\mathcal {F} \xrightarrow {\cdot^ {s}} \mathcal {F} \otimes L
$$

is injective.

Proof. Exercise.

# 9. CASTELNUOVO-MUMFORD REGULARITY

An effective link between vanishing and global generation is provided by the theory of Castelnuovo-Mumford regularity. This is usually defined with respect to  $\mathcal{O}_{\mathbf{P}}(1)$  on a projective space, but we can consider a slightly more general class of line bundles.

Definition 9.1. Let  $X$  be a projective variety, and  $L$  an ample and globally generated line bundle on  $X$ . A coherent sheaf  $\mathcal{F}$  on  $X$  is called  $m$ -regular with respect to  $L$  if

$$
H ^ {i} (X, \mathcal {F} \otimes L ^ {\otimes m - i}) = 0 \forall i &gt; 0.
$$

Theorem 9.2 (Castelnuovo-Mumford Lemma). Let  $X$  be a projective variety, and  $L$  an ample and globally generated line bundle on  $X$ . Let  $\mathcal{F}$  be a coherent sheaf on  $X$  which is  $m$ -regular with respect to  $L$ , and let  $k \geq 0$ . Then:

(i)  $\mathcal{F}$  is  $(m + k)$ -regular with respect to  $L$ .
(ii)  $\mathcal{F}\otimes L^{\otimes m + k}$  is globally generated.
(iii) The multiplication map

$$
H ^ {0} (X, \mathcal {F} \otimes L ^ {\otimes m}) \otimes H ^ {0} (X, L ^ {\otimes k}) \longrightarrow H ^ {0} (X, \mathcal {F} \otimes L ^ {\otimes m + k})
$$

is surjective.

Proof. Note first that it is enough to prove only (i) and (iii). Indeed, if we know (iii) for all  $k$ , we can combine it with the fact that by Serre's theorem  $\mathcal{F} \otimes L^{\otimes m + k}$  is globally generated for  $k \gg 0$ . But we have a commutative diagram

![img-0.jpeg](img-0.jpeg)

where the vertical and bottom horizontal maps are obtained from the evaluation of global sections of the sheaves in question. It follows that for  $k \gg 0$  the composition of the top horizontal and left vertical maps is surjective. Therefore the bottom horizontal map is surjective, which means precisely that  $\mathcal{F} \otimes L^{\otimes m}$  is globally generated. Also, because of the inductive nature of (i), it is in fact enough to prove (i) and (iii) for  $k = 1$ .

Denote  $V = H^{0}(X,L)$ , and say  $\dim V = n$ . Since  $L$  is globally generated, we have a surjective map

$$
V \otimes \mathcal {O} _ {X} \xrightarrow {\mathrm {e v}} L.
$$

hinking of this as a nowehere-vanishing section of the vector bundle $V^{\vee}\otimes L$, we can associate to it a Koszul complex

$0\longrightarrow\bigwedge^{n}V\otimes L^{\otimes-n}\longrightarrow\dots\longrightarrow\bigwedge^{2}V\otimes L^{\otimes-2}\longrightarrow V\otimes L^{\otimes-1}\longrightarrow\mathcal{O}_{X}\longrightarrow 0.$

Note that this is an exact complex, and the kernels (= cokernels) of the maps in the complex are all locally free. Indeed, recall that on projective space $\mathbf{P}=\mathbf{P}(V)$ we have the Euler sequence

$0\longrightarrow\Omega^{1}_{\mathbf{P}}\longrightarrow V\otimes\mathcal{O}_{\mathbf{P}}(-1)\longrightarrow\mathcal{O}_{\mathbf{P}}\longrightarrow 0,$

and so the kernel of the map $V\otimes L^{\otimes-1}\to\mathcal{O}_{X}$ is the vector bundle $f^{*}\Omega^{1}_{\mathbf{P}}$, with $f:X\to\mathbf{P}$ the morphism induced by $L$. Then it is not hard to see that the other kernels in the Koszul complex are isomorphic to $f^{*}\Omega^{i}_{\mathbf{P}}$.

Twisting the Koszul complex by $\mathcal{F}\otimes L^{\otimes m+1}$, we then get another exact complex

$0\longrightarrow\bigwedge^{n}V\otimes\mathcal{F}\otimes L^{\otimes m+1-n}\longrightarrow\dots\longrightarrow\bigwedge^{2}V\otimes\mathcal{F}\otimes L^{\otimes m-1}\longrightarrow V\otimes\mathcal{F}\otimes L^{\otimes m}\longrightarrow\mathcal{F}\otimes L^{\otimes m+1}\longrightarrow 0.$

Since $\mathcal{F}$ is $m$-regular, we have that

(8) $H^{i}(X,\bigwedge^{i+1}V\otimes\mathcal{F}\otimes L^{\otimes m-i})=0,\ \ \forall\ i>0.$

Chasing cohomology inductively from left to right in the exact sequence, applying the vanishing in (8) at each step, we finally obtain surjectivity at the $H^{0}$-level on the right, i.e. that of the map

$V\otimes H^{0}(X,\mathcal{F}\otimes L^{\otimes m})\longrightarrow H^{0}(X,\mathcal{F}\otimes L^{\otimes m+1})$

which is exactly (iii) for $k=1$. To prove (i), we twist the Koszul complex by $\mathcal{F}\otimes L^{\otimes m}$ instead of $\mathcal{F}\otimes L^{\otimes m+1}$. Using again the vanishing in (8), twisting successively further by $L^{\otimes-i}$ and chasing trough the sequence, we always obtain precisely the vanishing we need at the right-most term (exercise!). ∎

###### Exercise 9.3.

A coherent sheaf $\mathcal{F}$ on $\mathbf{P}^{n}$ is $m$-regular (with respect to $\mathcal{O}_{\mathbf{P}^{n}}(1)$) if and only if it admits a resolution of the form

$\dots\longrightarrow\bigoplus\mathcal{O}(-m-2)\longrightarrow\bigoplus\mathcal{O}(-m-1)\longrightarrow\bigoplus\mathcal{O}(-m)\longrightarrow\mathcal{F}\longrightarrow 0.$

The main statement we will extract from Theorem 9.2 is the following:

###### Corollary 9.4.

If $\mathcal{F}$ is $0$-regular with respect to $L$, then $\mathcal{F}$ is globally generated.

###### Corollary 9.5.

(i) Let $X$ be a smooth projective complex variety of dimension $n$, and $L$ an ample and globally generated line bundle on $X$. Then

$\omega_{X}\otimes L^{\otimes m}$

is globally generated for all $m\geq n+1$.

(ii) More generally, if $f:X\to Y$ is a morphism from a smooth projective complex variety $X$ to a projective variety $Y$ of dimension $n$, and $L$ is an ample and globally generated line bundle on $Y$, then

$R^{i}f_{*}\omega_{X}\otimes L^{\otimes m}$

is globally generated for all $i$ and all $m\geq n+1$.

###### Proof.

Kodaira vanishing (for (i)) and Kollár Vanishing (for (ii)) imply that $\omega_{X}\otimes L^{\otimes m}$, and $R^{i}f_{*}\omega_{X}\otimes L^{\otimes m}$ respectively, are $0$-regular with respect to $L$. We then apply Corollary 9.4. ∎

###### Remark 9.6 (Fujita’s Conjecture).

T. Fujita has formulated one of the most appealing conjectures in higher dimensional geometry, saying that if $L$ is an ample line bundle on a smooth projective variety of dimension $n$, then $\omega_{X}\otimes L^{\otimes m}$ is globally generated for $m\geq n+1$, and very ample for $m\geq n+2$.

The Corollary above shows that this is true (over $\mathbf{C}$) when $L$ is *ample and globally generated*. The general case is much more complicated: the global generation statement is known in dimension two (Reider), three (Ein-Lazarsfeld) and four (Kawamata), and in general if the bound $n+1$ is replaced by $\binom{n+1}{2}$ (Angehrn-Siu). Almost nothing is known about very ampleness in dimension three or more.

## 10. Log-resolutions, birational transformations, Kawamata-Viehweg

We now discuss briefly a few results from Hironaka’s package of resolution of singularities, and put them to a first use by proving a useful generalization of Kodaira Vanishing.

###### Definition 10.1.

Let $X$ be a smooth variety. An effective divisor $D=\sum_{i}D_{i}$ on $X$ has *simple normal crossings* if each $D_{i}$ is smooth and around each point of $X$ there is a coordinate system $x_{1},\ldots,x_{n}$ such that locally $D$ is given by

$x_{1}\cdot\ldots\cdot x_{k}=0\ \ \text{for some}\ k\leq n.$

More generally, a $\mathbf{Q}$-divisor $\sum_{i}d_{i}D_{i}$ has *simple normal crossing support* if $\sum_{i}D_{i}$ has simple normal crossings.

###### Definition 10.2 (Log-resolution).

(i) Say $X$ is a smooth variety and $D=\sum_{i}d_{i}D_{i}$ an effective $\mathbf{Q}$-divisor on $X$. A *log-resolution* of $D$ is a projective birational morphism $f:Y\to X$ with $Y$ smooth, such that if $E$ is the exceptional divisor of $f$ (the sum of the divisors contracted by $f$), then

$f^{-1}(D)\cup E$

is a divisor with simple normal crossings support.

(ii) More generally, let $X$ be an arbitrary variety and $D=\sum_{i}d_{i}D_{i}$ a Weil $\mathbf{Q}$-divisor on $X$. A *log-resolution* of the pair $(X,D)$ is a projective birational morphism $f:Y\to X$ with $Y$ smooth, such that if $E$ is the exceptional divisor of $f$, then

$f^{-1}(D)\cup E$

is a divisor with simple normal crossings support.

The following is Hironaka’s celebrated theorem:

###### Theorem 10.3 (Hironaka resolution).

Over a field of characteristic $0$, every pair $(X,D)$ as in (ii) above has a log-resolution.

This implies in particular that every variety (over a field of characteristic $0$) has a resolution of singularities, i.e. a projective birational morphism from a smooth variety. As for how this is approached, Hironaka in fact showed the following more general statement:

###### Theorem 10.4 (Hironaka principalization).

Let $X$ be a smooth variety, and $\mathcal{I}$ an ideal sheaf on $X$. Then there exists a birational morphism $f:Y\to X$ obtained as a composition of blow-ups along smooth centers contained in $\operatorname{Supp}(\mathcal{O}_{X}/\mathcal{I})$, such that $f^{*}\mathcal{I}$ is locally a principal ideal.

To deduce Theorem 10.3 from this, one roughly proceeds as follows: first embed $X$ into a smooth variety $Z$. (In general this may only work locally, but let’s assume for simplicity that it can be done; for instance one can always use a projective space for quasi-projective varieties.) We can then consider a birational morphism $f:W\to Z$ which principalizes $\mathcal{I}_{X}$, as in Theorem 10.4. Since $f$ is a composition of smooth blow-ups, it follows that at some point in the process $X$ is contained in a center of one of the blow-ups. But since $f^{-1}(X)$ is a divisor on $W$, it means that when this happens, the center must in fact be $X$ itself. This in particular means that one can resolve the singularities of $X$, after which one can replace $D$ by its proper transform plus the exceptional locus on the smooth model. We can then assume that $X$ is smooth, and then again apply the principalization theorem for $\mathcal{I}_{D}$ on $X$.

In this course we will mostly apply Theorem 10.3 when $X$ is smooth. In this case $D$ is $\mathbf{Q}$-Cartier, and the theorem is simply saying that after a birational modification we can arrange that (the proper transform of ) $D$ has simple normal crossing support, and intersects the exceptional locus of the modification transversely.

###### Example 10.5.

(i) Let $D=(y^{2}=x^{2}+x^{3})\subset\mathbf{A}^{2}$ be an irreducible nodal curve in the plane. Then the blow-up $f:\operatorname{Bl}_{0}\mathbf{A}^{2}\to\mathbf{A}^{2}$ is a log-resolution of the pair $(\mathbf{A}^{2},D)$. Note that $D$ itself is normal crossings in a neighborhood of the node, but it is a singular irreducible divisor, so the *simple* normal crossings condition is not satisfied.

(ii) Let $D=(y^{2}=x^{3})\subset\mathbf{A}^{2}$ be an irreducible cuspidal curve in the plane. This time the branches of $D$ at the cusp do not intersect transversely, and $f:\operatorname{Bl}_{0}\mathbf{A}^{2}\to\mathbf{A}^{2}$ is not a log-resolution any more. In fact one needs to blow up two more times in order to achieve simple normal crossings. I will draw the picture on the board, but see also *[x10]* V.3.9.1.

### Vanishing for higher direct images

I will take for granted the following local vanishing statement, which is a fundamental result on birational morphisms:

###### Theorem 10.6.

Let $f:Y\to X$ be a birational morphism between smooth varieties. Then

$R^{i}f_{*}\mathcal{O}_{Y}=0\quad\text{for }i>0.$

This is well-known (but nontrivial) in characteristic $0$, showing it first for a blow-up along a smooth subvariety (using the theorem on formal functions), and then using the fact that $f$ can be dominated by another birational morphism which is a composition of blow-ups with smooth centers; this last thing of course uses the statement of the principalization theorem. If resolution were known in characteristic $p>0$, the argument would go through; at the moment this is not the case. However, the statement above was recently proved, with different methods, by Chatzistamatiou-Rülling.

###### Corollary 10.7.

Let $f:Y\to X$ be a birational morphism between smooth varieties. Then

$f_{*}\omega_{Y}\simeq\omega_{X}\ \ \text{and}\ \ R^{i}f_{*}\omega_{Y}=0\quad\text{for}\ i>0.$

###### Proof.

Recall that in addition to Theorem 10.6 we also have the basic statement that $f_{*}\mathcal{O}_{Y}\simeq\mathcal{O}_{X}.$ This is something I can only quote here, but now one uses the relative version of Serre Duality due to Grothendieck. In this case it says that

$\mathbf{R}f_{*}\omega_{Y}\simeq\mathbf{R}\mathcal{H}om(\mathbf{R}f_{*}\mathcal{O}_{Y},\omega_{X})$

in the derived category of sheaves on $X$. But due to the vanishing in Theorem 10.6, on the right hand side we in fact have $\mathbf{R}f_{*}\mathcal{O}_{Y}\simeq\mathcal{O}_{X}$ and so the above implies the more familiar statement

$R^{i}f_{*}\omega_{Y}\simeq\mathcal{E}xt^{i}(\mathcal{O}_{X},\omega_{X})\ \ \forall\ i\geq 0.$

But this last sheaf is obviously $0$ for $i>0$, and $\omega_{X}$ for $i=0$. ∎

###### Exercise 10.8.

Use Theorem 10.6 to show that the Hodge numbers $h^{0,i}=h^{i}(X,\mathcal{O}_{X})$ are birational invariants for all $i$. Give examples to show that other Hodge numbers are birational invariants.

### Kawamata-Viehweg vanishing

We can now establish the following useful generalization of Kodaira Vanishing; since a few of the details will only be sketched, note that I am following the argument in *[x10]* 4.3, which goes along the lines of Kawamata’s original approach.

###### Theorem 10.9 (Kawamata-Viehweg Vanishing).

Let $X$ be a smooth complex projective variety of dimension $n$, and let $L$ be a big and nef line bundle on $X$. Then

$H^{i}(X,\omega_{X}\otimes L)=0\ \text{for all}\ i>0.$

More generally, the same conclusion holds if $L$ is a line bundle on $X$ such that

$L\sim_{\mathbf{Q}}A+D,$

with $A$ a big and nef $\mathbf{Q}$-divisor, and $D=\sum_{i}a_{i}D_{i}$ a $\mathbf{Q}$-divisor with simple normal crossings support satisfying $0\leq a_{i}<1$ for all $i$.

###### Proof.

I will divide the proof into a few steps; in the first three steps we will assume that $L$ is a big and nef line bundle, and $D=0$, while the last deals with the general case.

The line bundle case. Note to begin with that since $L$ is big, in general there exist an $m>0$, an ample line bundle $A$, and an effective divisor $E$, such that

(9) $L^{\otimes m}\simeq A\otimes\mathcal{O}_{X}(E).$

######

Step 1. We first show that if $A$ is an ample line bundle, and $E\subset X$ is a reduced simple normal crossings divisor on $X$, then

$H^{i}\big{(}X,\omega_{X}\otimes A\otimes\mathcal{O}_{X}(E)\big{)}=0\ \ \text{for all}\ i>0.$

Let’s assume first that $E$ is a smooth divisor. Twisting the defining sequence for $E$ by $\omega_{X}\otimes A$, we have a short exact sequence

$0\longrightarrow\omega_{X}\otimes A\longrightarrow\omega_{X}\otimes A\otimes\mathcal{O}_{X}(E)\longrightarrow\omega_{E}\otimes A_{|E}\longrightarrow 0$

where for the last term we used the adjunction formula

$\omega_{E}\simeq(\omega_{X}\otimes\mathcal{O}_{X}(E))_{|E}.$

The statement follows then immediately by passing to cohomology and using Kodaira Vanishing for the left and right terms in the short exact sequence.

In general we have $E=E_{1}+\cdots+E_{k}$, where $E_{j}$ are smooth divisors with transverse intersections. The statement can be easily proved by induction on $k$, using exact sequences of the form

$0\longrightarrow\omega_{X}\otimes A\otimes\mathcal{O}_{X}(E_{1}+\cdots+E_{j-1})$ $\longrightarrow\omega_{X}\otimes A\otimes\mathcal{O}_{X}(E_{1}+\cdots+E_{j})\longrightarrow$
$\longrightarrow\omega_{E_{j}}\otimes A_{|E_{j}}\otimes\mathcal{O}_{E_{j}}(E_{1}+\cdots+E_{j-1})\longrightarrow 0$

Step 2. In this step we show that we can reduce the general statement to the case where in (9) we have that $E$ has simple normal crossings support. Starting with an arbitrary $E$, we consider $\mu:Y\to X$ a log-resolution of $E$, so that $\mu^{*}E+F$ has simple normal crossings support, where $F$ is the exceptional divisor of $\mu$.

Assuming that we proved that

(10) $H^{i}(Y,\omega_{Y}\otimes\mu^{*}L)=0\ \ \text{for all}\ i>0,$

this implies the vanishing we want on $X$, as $\mu_{*}\omega_{Y}\simeq\omega_{X}$ and $R^{i}\mu_{*}\omega_{Y}=0$ for $i>0$, by Theorem 10.7.

Let’s now write

$\mu^{*}E=\sum_{j}a_{j}E_{j},$

with the convention that $a_{j}\geq 0$, so that we may assume that the sum contains all the exceptional divisors of $\mu$ among the $E_{j}$. Note that we have

$\mu^{*}L^{\otimes m}\simeq\mu^{*}A\otimes\mathcal{O}_{Y}(\sum_{j}a_{j}E_{j}).$

To conclude, one appeals to a version of the Negativity Lemma, stating that for some $k\gg 0$, there exist $b_{j}\geq 0$ such that

$\mu^{*}A^{\otimes k}\otimes\mathcal{O}_{Y}(-\sum_{j}b_{j}E_{j})$

is ample, where the sum runs over the exceptional divisors of $\mu$ (and so with the same convention as above we can assume that it runs over all $E_{j}$). But now we can write

$\mu^{*}L^{\otimes mk}\simeq\big{(}\mu^{*}A^{\otimes k}\otimes\mathcal{O}_{Y}(-\sum_{j}b_{j}F_{j})\big{)}\otimes\mathcal{O}_{Y}\big{(}\sum_{j}(ka_{j}+b_{j})F_{j}\big{)},$

which is of the form required at the beginning of this reduction step.

Step 3. In this last step we conclude the proof assuming that $E$ in (9) has simple normal crossings support, which is the outcome of Step 2. Write

$E=\sum_{i=1}^{t}e_{i}E_{i},\ \ e_{i}>0,$

and define $e=e_{1}\cdot\ldots\cdot e_{t}$ and $e_{i}^{\prime}=e/e_{i}$. Now by Kawamata’s covering construction, see Proposition 10.10 below, there exists a finite cover $f:Y\to X$ with $Y$ smooth projective, and a simple normal crossings divisor $E^{\prime}=\sum_{i=1}^{t}E_{i}^{\prime}$ on $Y$, such that

$f^{*}E_{i}=me_{i}^{\prime}E_{i}^{\prime}\ \ \text{for all}\ i=1,\ldots,k.$

Given (9), we consequently have

$f^{*}L^{\otimes m}\simeq f^{*}A\otimes\mathcal{O}_{Y}(meE^{\prime}).$

Using additive notation somewhat abusively, we can rewrite this as

$mf^{*}L\sim f^{*}A+meE^{\prime}.$

This implies the equivalence

$me(f^{*}L-E^{\prime})\sim f^{*}A+m(e^{\prime}-1)f^{*}L,$

and note that the right hand side is a divisor $A^{\prime}$ such that $A^{\prime\prime}=A^{\prime}/me$ is also Cartier. But $A^{\prime}$ is ample: indeed, $f^{*}A$ is ample since $f$ is finite, while $f^{*}L$ is nef since $L$ is so. We finally obtain the isomorphism

$f^{*}L\simeq A^{\prime\prime}\otimes\mathcal{O}_{Y}(E^{\prime}),$

with $A^{\prime\prime}$ ample, and $E^{\prime}$ a reduced simple normal crossings divisor.

We are now in a position to apply Step 1, by which we have

$H^{i}(Y,\omega_{Y}\otimes f^{*}L)=0\ \ \text{for all}\ i>0.$

As $\omega_{X}$ is a direct summand of $f_{*}\omega_{Y}$ via the trace map, we obtained the desired vanishing using the projection formula.

Step 4. This step deals with the general $\mathbf{Q}$-divisor case: recall that we are assuming that $D=\sum_{i=1}^{k}a_{i}D_{i}$ is a divisor with simple normal crossings support, with $0<a_{i}<1$.

The strategy is to prove the statement by induction on $k$. The case $k=0$ is the line bundle case proved above. Assume now that $k>0$, and let’s write $a_{1}=\frac{p}{q}$. Note that $0<p\leq q-1$. Just as in Step 3, one considers a Kawamata cover associated to the divisor

$D_{1}$; concretely, there exists a finite morphism $f:Y\to X$, with $Y$ smooth projective, such that on $Y$ the divisor $D_{1}$ becomes divisible by $d$. In other words, we have

$L^{\prime}:=f^{*}L\sim_{\mathbf{Q}}A^{\prime}+cD_{1}^{\prime}+\sum_{i=2}^{k}a_{i}D_{i}^{\prime},$

where $A^{\prime}=f^{*}A$ and $D_{i}^{\prime}=f^{*}D_{i}$, still satisfying the fact that $\sum D_{i}^{\prime}$ has simple normal crossings.

By induction we can now assume that the line bundle $L^{\prime}\otimes\mathcal{O}_{Y}(-cD_{1}^{\prime})$ satisfies

$H^{i}\left(Y,\omega_{Y}\otimes L^{\prime}\otimes\mathcal{O}_{Y}(-cD_{1}^{\prime})\right)=0\ \ \text{for all}\ i>0.$

On the other hand, just as in Proposition 8.5, it is standard that in the covering construction above we have that $f_{*}\left(L^{\prime}\otimes\mathcal{O}_{Y}(-cD_{1}^{\prime})\otimes\omega_{Y}\right)$ contains $\omega_{X}\otimes L$ as a direct summand, which gives the vanishing we want. ∎

Here is the more refined covering construction that was used in the proof above. I will not include the proof here, but a very good treatment is given in *[x14]* 4.1.B.

###### Proposition 10.10 (Kawamata covers).

Let $X$ be a smooth variety, and $D=\sum_{i=1}^{t}D_{i}$ be a simple normal crossings divisor on $X$. Given positive integers $m_{1},\ldots,m_{k}$, there exists a finite flat morphism $f:Y\to X$ with $Y$ smooth, and a simple normal crossings divisor $D^{\prime}=\sum_{i=1}^{t}D_{i}^{\prime}$ on $Y$, such that

$f^{*}D_{i}=m_{i}D_{i}^{\prime}\ \ \text{for all}\ i=1,\ldots,k.$

Finally, similarly to the proof of Theorem 8.8 and the proof above, one can also prove the following more general statement, also due to Kollár:

###### Theorem 10.11.

Let $f:X\to Y$ be a morphism from a smooth projective variety $X$ to a projective variety $Y$, and let $L$ be a line bundle on $X$ such that

$L\sim_{\mathbf{Q}}f^{*}N+D,$

with $N$ a nef and big $\mathbf{Q}$-Cartier $\mathbf{Q}$-divisor on $Y$, and $D=\sum_{i}d_{i}D_{i}$ a $\mathbf{Q}$-divisor with simple normal crossings support satisfying $0\leq d_{i}<1$ for all $i$. Then

$H^{j}\left(Y,R^{i}f_{*}(\omega_{X}\otimes L)\right)=0,\ \ \text{for all}\ i\ \text{and all}\ j>0.$

## 11. Vanishing for direct images of pluricanonical bundles

I will now explain a vanishing theorem that will allow us to give algebraic proofs of the positivity results for direct images of pluricanonical bundles that we are after. It is inspired by the following observation, which shows that Kodaira vanishing can be extended to powers of the canonical bundle. All the varieties considered in this section are over the complex numbers.

###### Proposition 11.1.

Let $X$ be a smooth projective variety, $L$ an ample line bundle on $X$, and $k\geq 1$ an integer. Then

$H^{i}(X,\omega_{X}^{\otimes k}\otimes L^{k(n+1)-n})=0,\ \ \forall\ i>0.$

roof.

For clarity, I’ll use additive notation. We write

$kK_{X}+(k(n+1)-n)\,L=K_{X}+(k-1)\,(K_{X}+(n+1)L)+L.$

Recall that Fujita’s conjecture predicts that $K_{X}+(n+1)L$ is globally generated; the weaker statement that it is nef is however already known as part of Mori’s proof of the Cone and Rationality theorem. It follows that

$(k-1)\,(K_{X}+(n+1)L)+L$

is an ample line bundle, and therefore Kodaira Vanishing applies. ∎

The following is a partial extension to direct images that Schnell and I have obtained recently. Note that the case $k=1$ is a weaker form of Kollár’s vanishing theorem, in which one can assume that $L$ is only ample, and which works for all $R^{i}f_{*}\omega_{X}$. We conjecture that the result holds when $L$ is only assumed to be ample.

###### Theorem 11.2.

Let $f\colon X\to Y$ be a morphism of projective varieties, with $X$ smooth and $Y$ of dimension $n$. If $L$ is an ample and globally generated line bundle on $Y$, and $k>0$ is an integer, then

$H^{i}(Y,f_{*}\omega_{X}^{\otimes k}\otimes L^{\otimes l})=0\ \ \text{for all}\ i>0\ \ \text{and}\ \ l\geq k(n+1)-n.$

###### Proof.

We will first show that we can reduce to the case when the image of the adjunction morphism

(11) $f^{*}f_{*}\omega_{X}^{\otimes k}\to\omega_{X}^{\otimes k}.$

is a line bundle. A priori the image is $\mathfrak{b}\otimes\omega_{X}^{\otimes k}$, where $\mathfrak{b}$ is the relative base ideal of $\omega_{X}^{\otimes k}$. (Note that on the general fiber $F$ the adjunction morphism is simply the evaluation map $H^{0}(F,\omega_{F}^{\otimes k})\otimes\mathcal{O}_{F}\to\omega_{F}^{\otimes k}$.) We consider a log-resolution

$\mu:\tilde{X}\longrightarrow X$

of the ideal sheaf $\mathfrak{b}$. Since $\tilde{X}$ and $X$ are smooth, we have that

$\mu_{*}\omega_{\tilde{X}}^{\otimes k}\simeq\omega_{X}^{\otimes k},$

and so we can replace $X$ by $\tilde{X}$ and $f$ by $f\circ\mu$ without changing the conclusion. Going back to the original notation, we can thus assume that the image sheaf of the adjunction morphism (11) is of the form $\omega_{X}^{\otimes k}\otimes\mathcal{O}_{X}(-E)$ for a divisor $E$ with simple normal crossings support.

Since $L$ is ample, there is a smallest integer $m\geq 0$ such that $f_{*}\omega_{X}^{\otimes k}\otimes L^{\otimes m}$ is globally generated. Then $f^{*}f_{*}\omega_{X}^{\otimes k}\otimes f^{*}L^{\otimes m}$ is globally generated as well, and so using the adjunction morphism (11) we can write

$\omega_{X}^{\otimes k}\otimes f^{*}L^{\otimes m}\simeq\mathcal{O}_{X}(D+E),$

with $D$ smooth and $D+E$ a divisor with simple normal crossings support. In divisor notation, we obtain

(12) $K_{X}\ \ \sim_{\mathbf{Q}}\ \ \frac{1}{k}D+\frac{1}{k}E-\frac{m}{k}f^{*}L.$

For any integer $l\geq 0$, using (12) we can then write the following equivalence:

$kK_{X}-\left\lfloor\frac{k-1}{k}E\right\rfloor+lf^{*}L=K_{X}+(k-1)K_{X}-\left\lfloor\frac{k-1}{k}E\right\rfloor+lf^{*}L$
(13) $\sim_{\mathbf{Q}}\ \ K_{X}+\Delta+\left(l-\frac{k-1}{k}\cdot m\right)f^{*}L,$

where

$\Delta=\frac{k-1}{k}D+\frac{k-1}{k}E-\left\lfloor\frac{k-1}{k}E\right\rfloor$

is a boundary divisor (meaning $\Delta=\sum_{i}d_{i}\Delta_{i}$ with $0<d_{i}<1$) with simple normal crossings support.

Observe now that for every effective Cartier divisor $E^{\prime}\preceq E$ we have

(14) $f_{*}\left(\omega_{X}^{\otimes k}\otimes\mathcal{O}_{X}(-E^{\prime})\right)\simeq f_{*}\omega_{X}^{\otimes k}.$

Indeed, it is enough to have this for $E$ itself; but this is the base locus of $\omega_{X}^{\otimes k}$ relative to $f$, so by construction we have that the adjunction morphism factors as

$f^{*}f_{*}\omega_{X}^{\otimes k}\to\omega_{X}^{\otimes k}\otimes\mathcal{O}_{X}(-E)\hookrightarrow\omega_{X}^{\otimes k}.$

The claimed isomorphism follows by noting that the composition

$f_{*}\omega_{X}^{\otimes k}\longrightarrow f_{*}\left(\omega_{X}^{\otimes k}\otimes\mathcal{O}_{X}(-E)\right)\longrightarrow f_{*}\omega_{X}^{\otimes k}$

of the push-forward maps is the identity. Using (14) and the projection formula, we obtain that

$f_{*}\left(\omega_{X}^{\otimes k}\left(-\left\lfloor\frac{k-1}{k}E\right\rfloor\right)\otimes f^{*}L^{\otimes l}\right)\simeq f_{*}\omega_{X}^{\otimes k}\otimes L^{\otimes l}.$

On the other hand, because of (13), the left hand side can also be written as

$f_{*}\mathcal{O}_{X}\left(K_{X}+\Delta+\left(l-\frac{k-1}{k}\cdot m\right)f^{*}L\right),$

to which one can apply Kollár vanishing in the form of Theorem 10.11 if the number in the parenthesis is positive. In other words,

$H^{i}(Y,f_{*}\omega_{X}^{\otimes k}\otimes L^{\otimes l})=0\ \ \text{for all}\ i>0\ \ \text{and}\ \ l>\frac{k-1}{k}\cdot m.$

Using the Castelnuovo-Mumford Lemma (see Corollary 9.4), we conclude that $f_{*}\omega_{X}^{\otimes k}\otimes L^{\otimes l}$ is globally generated for $l>\frac{k-1}{k}\cdot m+n$. But $m$ was chosen minimal with this property, which means that we must have

$\frac{k-1}{k}\cdot m+n+1\geq m,$

which translates into $m\leq k(n+1)$. Consequently, vanishing holds for all $l\geq k(n+1)-n$.

∎

##

###### Corollary 11.3.

Let $f\colon X\to Y$ be a morphism of projective varieties, with $X$ smooth and $Y$ of dimension $n$. If $L$ is an ample and globally generated line bundle on $Y$, and $k\geq 1$ an integer, then

$f_{*}\omega_{X}^{\otimes k}\otimes L^{\otimes l}$

is $0$-regular, and therefore globally generated, for $l\geq k(n+1)$.

###### Proof.

Just like the corollaries of Kodaira and Kollár vanishing in the section on Castelnuovo-Mumford regularity, this follows immediately from Theorem 11.2, since vanishing holds after subtracting up to $n$ copies of $L$. ∎

## 12. Positivity for vector bundles and torsion-free sheaves

Positivity for vector bundles. The natural extensions of the standard positivity properties for line bundles are the following:

###### Definition 12.1.

Let $X$ be a projective scheme, and $E$ a vector bundle on $X$. Then $E$ is called nef, or ample, if $\mathcal{O}_{\mathbf{P}}(1)$ is a nef, or ample, line bundle on $\mathbf{P}=\mathbf{P}(E)$.

Here I will only give a glimpse of some useful properties of ample and nef vector bundles. For a complete treatment, see *[x10]* Ch.6.

###### Exercise 12.2.

If $E$ and $F$ are ample (nef) vector bundles on $X$, then $E\oplus F$ is ample is ample (nef).

###### Lemma 12.3.

Let $E$ be an ample (nef) vector bundle on a projective scheme $X$ over a field of characteristic zero. Then:

(i) If $E\to G$ is a quotient vector bundle, then $G$ is ample (nef).

(ii) $S^{k}E$ is ample (nef) for all $k\geq 1$.

(iii) $E^{\otimes k}$ is ample (nef) for any $k\geq 1$. Consequently, $\wedge^{k}E$ is ample (nef) for any $k\geq 1$, and so $\det E$ is an ample (nef) line bundle.

###### Proof.

(i) This holds in arbitrary characteristic. Since our projective bundles parametrize one-dimensional quotients, the surjection $E\to G$ corresponds to an inclusion $\mathbf{P}(G)\subseteq\mathbf{P}(E)$, such that the restriction of $\mathcal{O}_{\mathbf{P}(E)}(1)$ is $\mathcal{O}_{\mathbf{P}(G)}(1)$. The assertion is then clear.

(ii) We first show that $S^{m}E$ is ample for $m\gg 0$. Since the ampleness of $E$ means by definition the ampleness of $\mathcal{O}_{\mathbf{P}}(1)$ on $\pi:\mathbf{P}=\mathbf{P}(E)\to X$, and since $\pi_{*}\mathcal{O}_{\mathbf{P}}(m)\simeq S^{m}E$, an argument completely similar to Serre’s theorem implies that for any coherent sheaf $\mathcal{F}$ on $X$ there exists some positive integer $m_{0}=m_{0}(\mathcal{F})$ such that

$S^{m}E\otimes\mathcal{F}\text{ is globally generated for }m\geq m_{0}.$

In particular, we can take $\mathcal{F}=A^{-1}$, where $A$ is an ample line bundle on $X$. We deduce that there is a surjection

$\bigoplus A\longrightarrow S^{m}E\longrightarrow 0$

and hence by part (i) $S^{m}E$ is ample, for every $m\geq m_{0}$

Now fix an arbitrary $k\geq 1$. According to Exercise 12.4 below, for each $\ell\geq 1$, there exists a finite map

$\varphi:\mathbf{P}(S^{k}E)\longrightarrow\mathbf{P}(S^{k\ell}E)\ \ \text{with}\ \ \mathcal{O}_{\mathbf{P}(S^{k}E)}(1)\simeq\varphi^{*}\mathcal{O}_{\mathbf{P}(S^{k\ell}E)}(1).$

We’ve seen above that the line bundle on the right hand side is ample for $\ell\gg 0$, so $\mathcal{O}_{\mathbf{P}(S^{k}E)}(1)$ is ample as well, being its pullback by a finite map. With a little care, the analogous nefness result is a simple application of what we just proved about ampleness, combined with the fact that nef divisors are limits of ample $\mathbf{Q}$-divisors.

(iii) Since all the other linear algebra constructions are quotients of tensor products, it is enough to show that $E^{\otimes k}$ is ample (nef) for $k\geq 1$. More generally, we show that if $E$ and $F$ are ample (nef) vector bundles, then so is $E\otimes F$. But note that $E\otimes F$ is a direct summand of $S^{2}(E\oplus F)$, and so the result follows combining Exercise 12.2 and part (ii). ∎

###### Exercise 12.4.

Let $E$ be a vector bundle on a projective scheme $X$ over a field of characteristic zero, and let $k,\ell\geq 1$ be two integers. Then there exists a finite (onto its image) morphism

$\varphi:\mathbf{P}(S^{k}E)\longrightarrow\mathbf{P}(S^{k\ell}E)$

compatible with $\mathcal{O}(1)$, i.e. such that $\varphi^{*}\mathcal{O}_{\mathbb{P}(S^{k\ell}E)}(1)\simeq\mathcal{O}_{\mathbf{P}(S^{k}E)}(1)$. (Hint: think of a Veronese-type construction.)

###### Exercise 12.5.

A vector bundle $E$ on $X$ is nef if and only if for every ample line bundle $H$ on $X$ and every integer $\alpha>0$, there exists an integer $\beta>0$ such that $S^{\alpha\beta}E\otimes H^{\otimes\beta}$ is globally generated.

###### Lemma 12.6.

Let $E$ be a locally free sheaf on a smooth projective variety $X$. If there exists a line bundle $L$ on $X$ such that $E^{\otimes m}\otimes L$ is globally generated for every $m\geq 1$, then $E$ is nef.

###### Proof.

Denoting $\mathbf{P}=\mathbf{P}(E)$, we have the natural projection $\pi:\mathbf{P}\to X$, and recall that

$\pi_{*}\mathcal{O}_{\mathbf{P}}(m)\simeq S^{m}E,\ \ \forall\ m\geq 0.$

Since symmetric powers are quotients of tensor powers, the hypothesis implies that $S^{m}E\otimes L$ is globally generated for $m\geq 1$. Using the isomorphisms above, and the fact that $\mathcal{O}_{\mathbf{P}}(m)$ is globally generated on the fibers, the adjunction mapping gives a surjective homomorphism

$\pi^{*}S^{m}E\otimes\pi^{*}L\longrightarrow\mathcal{O}_{\mathbf{P}}(m)\otimes\pi^{*}L.$

It follows that $\mathcal{O}_{\mathbf{P}}(m)\otimes\pi^{*}L$ is a globally generated line bundle for all $m\geq 1$. This in turn implies that $\mathcal{O}_{\mathbf{P}}(1)$ is nef by Exercise 5.10. ∎

### Motivation: positivity for families of curves

A first motivation for understanding the positivity properties of direct images of relative pluricanonical bundles comes from looking at morphisms where the fibers have dimension $1$, so in particular the general one is a smooth projective curve. In this case, the problem is intimately related to the existence and projectivity of the moduli space of stable curves. The discussion here is just in order to explain the picture; I will not define the terminology or give details.

Mihnea Popa

Fix a genus  $g \geq 1$ , and recall that there exists a quasi-projective variety  $M_g$  which is a coarse moduli space for isomorphism classes of smooth projective curves of genus  $g$ . It admits a projective compactification  $\overline{M}_g$ , which parametrizes isomorphism classes of stable curves. If  $g = 1$ , the dimension of  $M_g$  is 1, otherwise it is equal to  $3g - 3$ . One important (and unfortunate) feature of  $M_g$  and  $\overline{M}_g$  is that they are only coarse moduli spaces; what captures the properties of families of curves somewhat more accurately, but at the same time are more technical objects, are the Deligne-Mumford stacks  $\mathcal{M}_g$  and  $\overline{\mathcal{M}}_g$ , whose associated coarse moduli spaces are  $M_g$  and  $\overline{M}_g$ .

Over  $\overline{M}_g$  sits the universal curve

$$
\pi : \overline {{C}} _ {g} \longrightarrow \overline {{M}} _ {g},
$$

whose fiber over a point in  $\overline{M}_g$  is precisely the curve parametrized by that point. These spaces are not smooth, but their singularities are mild enough that we can still talk about  $\omega_{\overline{C}_g / \overline{M}_g}$ , whose restriction to each fiber is the dualizing sheaf  $\omega_C$  of the stable curve  $C$ . We can then consider

$$
\mathcal {H} _ {m} := \pi_ {*} \omega_ {\overline {{C}} _ {g} / \overline {{M}} _ {g}} ^ {\otimes m}, \quad \forall m \geq 1.
$$

These are vector bundles on  $\overline{M}_g$ , since  $\pi$  is flat and the dimension of the space of sections  $H^0(C, \omega_C^{\otimes m})$  depends only on  $g$  and not on  $C$ . For  $m = 1$ , this is the celebrated Hodge bundle, of rank  $g$ . Here are some important theorems about these bundles:

-  $\mathcal{H}_m$  is nef for all  $m \geq 1$ ; in particular so is  $\operatorname{det} \mathcal{H}_m$ .
-  $\operatorname{det} \mathcal{H}_m$  is ample for  $m \gg 0$ .

Finally, let  $f: X \to Y$  be a surjective morphism of, say, smooth projective varieties such that its general fiber is a smooth projective curve of genus  $g$ . Let's assume for simplicity that  $f$  is flat, so that all fibers are 1-dimensional; by a process called stable reduction, after a finite base change we can even assume that all fibers are stable curves, so let's say that this is the case.

In other words, we consider a flat family  $f: X \to Y$  of stable curves of genus  $g$ . Let's assume that it comes by base change from the moduli space, i.e. that there exists a morphism  $\varphi: Y \to \overline{M}_g$  and a fiber diagram

![img-1.jpeg](img-1.jpeg)

(This is strictly the case only after a finite cover, which is a reflection of the fact that  $\overline{M}_g$  is not a fine moduli space; note however that our end goal, which is positivity in a loose sense, behaves well with respect to finite maps.) As the construction is canonical, relative dualizing sheaves for families are compatible with base change. We conclude that

$$
\mathcal {F} _ {m} = f _ {*} \omega_ {X / Y} ^ {\otimes m} \simeq \varphi^ {*} \mathcal {H} _ {m} \quad \mathrm {a n d} \quad \det  \mathcal {F} _ {m} \simeq \varphi^ {*} \det  \mathcal {H} _ {m}.
$$

Thus the basic properties of the moduli space imply positivity for families; if follows from the above that for stable families of curves  $f$  as above:

$\bullet$ $\mathcal{F}_{m}$ is a nef vector bundle, and $\det\mathcal{F}_{m}$ is a nef line bundle.

$\bullet$ if $f$ is a finite mophism, then $\det F_{m}$ is ample for $m\gg 0$.

$\bullet$ if $f$ is a generically finite morphism (i.e. the general fiber is isomorphic only to at most finitely many other fibers of $f$), then $\det\mathcal{F}_{m}$ is a nef and big line bundle for $m\gg 0$.

$\bullet$ more generally, for arbitrary $f$, we have that $\kappa(Y,\det\mathcal{F}_{m})\geq\dim\varphi(Y)$ (the “variation” of the family in moduli).

It is worth noting however that beyond the intuitive picture, in general things go mostly the other way: one tries to prove positivity results for $\mathcal{F}_{m}$ for every (stable) family by other means precisely in order to deduce the projectivity of moduli spaces, according to a strategy introduced by Kollár and Viehweg.

Viehweg’s fiber product trick. Let $f:X\to Y$ be a projective surjective morphism of smooth quasi-projective varieties. Denote

$f^{s}:X^{s}=X\times_{Y}X\times_{Y}\dots\times_{Y}X\longrightarrow Y$

the $s$-fold fiber product induced by $f$.

###### Exercise 12.7.

(i) With the notation above, show that there is a unique irreducible component of $X^{s}$ which dominates $Y$.

(ii) Let $\pi:X=\operatorname{Bl}_{y}(Y)\to Y$ be the blow-up of $Y$ at a point. Show that $X\times_{Y}X$ is reducible (so that $X^{2}\neq X\times_{Y}X$).

(iii) If $f:X\to Y$ is a smooth morphism, then $X^{s}$ is irreducible and smooth, and the morphism $f^{s}:X^{s}\to Y$ is smooth as well. If $X_{y}$ is the fiber of $f$ over $y\in Y$, then one has

$(f^{s})^{-1}(X_{y})\simeq X_{y}\times\dots\times X_{y},$

the usual $s$-fold product.

In general, denote by $X^{(s)}$ a resolution of singularities of the irreducible component in the exercise above. There is an induced morphism

$f^{(s)}:X^{(s)}\longrightarrow Y.$

Since any two resolutions are dominated by a third, and for a birational morphism between $g:W\to Z$ of smooth varieties we have $g_{*}\omega_{W}^{\otimes m}\simeq\omega_{Z}^{\otimes m}$, we have that the sheaf

$f_{*}^{(s)}\omega_{X^{(s)}/Y}^{\otimes m}$

is independent of the resolution. We first state the crucial result we need in a special situation, and then more generally.

###### Proposition 12.8.

If $f$ is a smooth morphism, then

$f_{*}^{s}\omega_{X^{s}/Y}^{\otimes m}\simeq\big{(}f_{*}\omega_{X/Y}^{\otimes m}\big{)}^{\otimes s}.$

(Note that $X^{s}$ is already smooth by Exercise 12.7(iii).)

######

###### Proposition 12.9.

If $f$ is arbitrary, there is an inclusion

$\left(f_{*}^{(s)}\omega_{X^{(s)}/Y}^{\otimes m}\right)^{\vee\vee}\hookrightarrow\left(\left(f_{*}\omega_{X/Y}^{\otimes m}\right)^{\otimes s}\right)^{\vee\vee}$

which is generically an isomorphism. More precisely, it is an isomorphism over the locus where $f$ is smooth, and more generally where $f$ is semistable.

I have not discussed this last notion yet; I may say a few words about it later. Also, the Propositions above are formal consequences of general duality theory, which requires a long discussion in a direction different from the main purpose of this course. I will take the statements for granted for now.

###### Remark 12.10.

Note that in general it is not the case that $f_{*}^{(s)}\omega_{X^{(s)}/Y}^{\otimes m}\simeq\left(f_{*}\omega_{X/Y}^{\otimes m}\right)^{\otimes s}$ everywhere on $Y$. One can show however that, after performing a process called semistable reduction, there is a closed subset $Z\subset Y$ of codimension at least 2 such that this isomorphism holds over $U=Y-Z$. The main technical point is to show that $X^{s}$ has rational singularities over this open set $U$ (over which the morphism is semistable).

Positivity for direct images of relative pluricanonical bundles. I will start with the case of smooth morphisms, which is easiest to explain, and where the (semi)positivity of direct images holds in a strong form. We will later prove a generalization of this statement due to Viehweg, which holds for arbitrary morphisms, but where the conclusion is necessarily weaker; the proofs are similar, and we will obtain them here as relatively quick applications of Corollary 11.3.

###### Theorem 12.11.

Let $f:X\to Y$ be a smooth morphism of smooth projective varieties. Then

$\mathcal{F}_{m}=f_{*}\omega_{X/Y}^{\otimes m}$

is a nef vector bundle for all $m\geq 0$.

###### Proof.

Since $f$ is smooth, and in particular flat, by the Cohomology and Base Change theorem the fact that $\mathcal{F}_{m}$ is a vector bundle is equivalent to saying that the plurigenera $P_{m}(F)$ of the fibers of $f$ are constant. But this is a well-known theorem of Siu, the “deformation invariance of plurigenera” (proved with analytic methods); see also *[x10]* 11.5 for an algebraic proof in the case of varieties of general type.

To prove nefness, consider the line bundle

$A:=\omega_{Y}\otimes L^{\otimes n+1},$

where $n=\dim Y$ and $L$ is an ample and globally generated line bundle on $Y$. According to Lemma 12.6, it suffices to show that $\mathcal{F}_{m}^{\otimes s}\otimes A^{\otimes m}$ is globally generated for all $s\geq 1$. Note first that we know the result for $\mathcal{F}_{m}$ itself; indeed, we have

$\mathcal{F}_{m}\otimes A^{\otimes m}\simeq f_{*}\omega_{X}^{\otimes m}\otimes L^{\otimes m(n+1)},$

and one can apply Corollary 11.3.

To prove the statement for arbitrary $s$, one uses Viehweg’s trick based on the construction explained in the previous subsection; we will make $\mathcal{F}_{m}^{\otimes s}$ look like $\mathcal{F}_{m}$ itself, so

that we can again apply the argument above, but after changing the domain $X$. To this end consider the $s$-fold fiber product induced by $f$,

$f^{s}:X^{s}:=X\times_{Y}X\times_{Y}\cdots\times_{Y}X\longrightarrow X,$

and the induced

$f^{(s)}:X^{(s)}\longrightarrow X,$

where $X^{(s)}$ is the unique component of $X^{s}$ which dominates $X$. Since $f$ is smooth, by Proposition 12.8 we have an isomorphism

$f^{(s)}_{*}\omega_{X^{(s)}/Y}^{\otimes m}\simeq\left(f_{*}\omega_{X/Y}^{\otimes m}\right)^{\otimes s}=\mathcal{F}_{m}^{\otimes s}.$

But the left hand side of the isomorphism is again a direct image of a relative pluricanonical bundle, and so we can apply Corollary 11.3 to conclude that $\mathcal{F}_{m}^{\otimes s}\otimes A^{\otimes m}$ is globally generated. ∎

###### Remark 12.12 (Base of dimension one).

Recall that in a previous section we saw that Iitaka’s conjecture for surfaces would follow if we knew that for a morphism $f:S\to C$ from a surface to a curve one had

$\deg\,f_{*}\omega_{S/C}^{\otimes m}\geq 0,\;\;\;\forall\;m\geq 1.$

More generally, let $f:X\to C$ be a fiber space with $X$ a smooth projective variety of arbitrary dimension, and $C$ a smooth projective curve. If $f$ is smooth, Theorem 12.11 says that $\mathcal{F}_{m}=f_{*}\omega_{X/C}^{\otimes m}$ is a nef vector bundle on $C$, which in particular implies that $\det\mathcal{F}_{m}$ is nef as well by Lemma 12.3. This last assertion is equivalent to

$\deg\,\mathcal{F}_{m}\geq 0,\;\;\;\forall\;m\geq 1,$

as the degree of $\mathcal{F}_{m}$ is equal to that of its determinant. We will see that the same statement holds even if $f$ is not necessarily assumed to be smooth, but this requires more work. (Note that since $C$ is a curve, $\mathcal{F}_{m}$ is automatically locally free for any morphism $f$, since it is torsion-free; more on this in the next subsection.)

### Torsion-free, reflexive, and weakly positive sheaves

Let $X$ be an integral scheme of finite type. For an $\mathcal{O}_{X}$-module $\mathcal{F}$, we denote by $\mathcal{F}^{\vee}$ the sheaf dual of $\mathcal{F}$, i.e.

$\mathcal{F}^{\vee}:=\mathcal{H}om(\mathcal{F},\mathcal{O}_{X}).$

###### Definition 12.13.

An $\mathcal{O}_{X}$-module $\mathcal{F}$ is *torsion-free* if $\mathcal{F}_{x}$ is a torsion-free $\mathcal{O}_{X,x}$-module for all $x\in X$. Equivalently, the natural mapping

$\varphi:\mathcal{F}\longrightarrow\mathcal{F}^{\vee\vee}$

is injective. Moreover, $\mathcal{F}$ is called *reflexive* if $\varphi$ is an isomorphism, so that $\mathcal{F}\simeq\mathcal{F}^{\vee\vee}$. In general, $\mathcal{F}^{\vee\vee}$ is called the *reflexive hull* of $\mathcal{F}$.

###### Exercise 12.14.

If $f:X\to Y$ is a surjective morphism of varieties, and $\mathcal{F}$ is a torsion-free sheaf on $X$, then $f_{*}\mathcal{F}$ is torsion-free on $Y$.

###### Exercise 12.15.

A coherent sheaf $\mathcal{F}$ on $X$ is called a *$k$-th syzygy sheaf* if locally around each point there exists an exact sequence

$0\longrightarrow\mathcal{F}\longrightarrow\mathcal{E}_{k}\longrightarrow\ldots\longrightarrow\mathcal{E}_{1}\longrightarrow\mathcal{G}\longrightarrow 0$

$Z_{j}$ free for all $j$. Show that $1$-st syzygy sheaf is equivalent to torsion-free, and $2$-nd syzygy sheaf is equivalent to reflexive.

###### Lemma 12.16.

If $\mathcal{F}$ is a coherent sheaf, then $\mathcal{F}^{\vee}$ is reflexive.

###### Proof.

First note that $\mathcal{F}^{\vee}$ is torsion-free. Indeed, $\mathcal{F}$ is locally a quotient

$\mathcal{O}_{X}^{\oplus r}\longrightarrow\mathcal{F}$

and dualizing this we obtain a local inclusion of $\mathcal{F}^{\vee}$ in a free sheaf. Now dualizing the natural map $\mathcal{F}\to\mathcal{F}^{\vee\vee}$ and then composing it with the similar map for $\mathcal{F}^{\vee}$ leads to a composition

$\mathcal{F}^{\vee\vee\vee}\to\mathcal{F}^{\vee}\to\mathcal{F}^{\vee\vee\vee}$

which can be easily seen to be the identity. It follows that the last map is surjective; it is however also injective, since $\mathcal{F}^{\vee}$ is torsion-free. ∎

###### Proposition 12.17.

If $\mathcal{F}$ is a coherent sheaf on a smooth variety $X$, denote by $S(\mathcal{F})$ the closet subset of $X$ where $\mathcal{F}$ is not locally free. Then, if $\mathcal{F}$ is a $k$-th syzygy sheaf, then

$\operatorname{codim}_{X}S(\mathcal{F})>k.$

In particular:

(i) If $\mathcal{F}$ is torsion-free, then $\operatorname{codim}_{X}S(\mathcal{F})\geq 2$. In particular, if $X$ is a smooth curve, then torsion-free is equivalent to locally free.

(ii) If $\mathcal{F}$ is reflexive, then $\operatorname{codim}_{X}S(\mathcal{F})\geq 3$. In particular, if $X$ is a smooth surface, then reflexive is equivalent to locally free.

###### Proof.

Note that a module over a local ring is free if and only if its projective dimension is $0$, and so by definition we have

$S(\mathcal{F})=\{x\in X\ |\ \operatorname{pd}\ \mathcal{F}_{x}\geq 1\}.$

Fix a point $x\in X$, and denote $A=\mathcal{O}_{X,x}$ and $M=\mathcal{F}_{x}$. Our hypothesis says that $M$ is a finitely generated $A$-module that sits in an exact sequence

$0\longrightarrow M\longrightarrow A^{\oplus r_{k}}\longrightarrow\dots\longrightarrow A^{\oplus r_{1}}\longrightarrow N\longrightarrow 0,$

with $N$ another finitely generated $A$-module. Using the standard interpretation of projective dimension in terms of $\operatorname{Ext}$ groups, we see that $x\in S(\mathcal{F})$ is equivalent to

$0\neq\operatorname{Ext}_{A}^{i}(M,A)\simeq\operatorname{Ext}_{A}^{i+k}(N,A)$

for some $1\leq i\leq n=\dim X$.

Thus locally there exists a coherent sheaf $\mathcal{G}$ such that

$S(\mathcal{F})=\bigcup_{i=1}^{n}\ \operatorname{Supp}\ \mathcal{E}xt^{i}(\mathcal{F},\mathcal{O}_{X})=\bigcup_{j=k+1}^{n}\ \operatorname{Supp}\ \mathcal{E}xt^{j}(\mathcal{G},\mathcal{O}_{X}).$

But a well-known application of the Auslander-Buchsbaum theorem says that for any coherent sheaf $\mathcal{G}$ on a smooth variety, one has

$\operatorname{codim}_{X}\operatorname{Supp}\ \mathcal{E}xt^{j}(\mathcal{G},\mathcal{O}_{X})\geq j\quad\text{for all}\ \ j\geq 0.$

###### Exercise 12.18.

Check the last assertion in the proof above.

###### Lemma 12.19.

A coherent sheaf $\mathcal{F}$ on a smooth variety $X$ is reflexive if and only if it is torsion-free and the following property holds: for every open set $U\subseteq X$ and every closed subset $Z\subseteq U$ of codimension at least $2$, the restriction map

$\mathcal{F}(U)\longrightarrow\mathcal{F}(U-Z)$

is an isomorphism.

###### Proof.

Assume first that $\mathcal{F}$ is reflexive, so clearly also torsion-free. Moreover, locally there exist exact sequences

$0\longrightarrow\mathcal{F}\longrightarrow\mathcal{O}_{X}^{\otimes r_{2}}\longrightarrow\mathcal{O}_{X}^{\otimes r_{1}}$

and the restriction map $\mathcal{O}_{X}(U)\to\mathcal{O}_{X}(U-Z)$ is an isomoprhism since regular functions extend over codimension two subsets on smooth (or just normal) varieties. This implies the same assertion for $\mathcal{F}$.

To prove the opposite implication, note that $\mathcal{F}$ and $\mathcal{F}^{\vee\vee}$ are isomorphic outside of the singularity set $\mathcal{S}(\mathcal{F})$. Since $\mathcal{F}$ is torsion-free, Proposition 12.17 implies that $S(\mathcal{F})$ has codimension at least $2$ (in every open set in $X$). The second hypothesis then implies that $\varphi\colon\mathcal{F}\to\mathcal{F}^{\vee\vee}$ is an isomorphism on any open set $U$, hence an isomorphism of sheaves. ∎

###### Lemma 12.20.

If $\mathcal{F}$ is a torsion-free sheaf on $X$, then there exists a birational modification $f:X^{\prime}\to X$ such that if $T$ is the torsion sheaf of $f^{*}\mathcal{F}$, then $f^{*}F/T$ is locally free.

Weak positivity for torsion-free sheaves. In this section we work over the complex numbers. We will prove a fundamental result of Viehweg on the weak positivity of direct images of relative pluricanonical bundles.

Notation: Since this will appear repeatedly, it is convenient to introduce the following notation: if $\mathcal{F}$ is a coherent sheaf on $X$ and $k$ is an integer, then

$\widehat{S}^{k}\mathcal{F}:=\big{(}S^{k}\mathcal{F}\big{)}^{\vee\vee}.$

Note that if $\mathcal{F}$ is torsion-free $S^{k}\mathcal{F}$ injects into $\widehat{S}^{k}\mathcal{F}$, while $\big{(}\mathcal{F}^{\otimes k}\big{)}^{\vee\vee}$ surjects onto $\widehat{S}^{k}\mathcal{F}$.

###### Definition 12.21.

Let $X$ be a smooth quasi-projective variety. A torsion-free coherent sheaf $\mathcal{F}$ on $X$ is *weakly positive over an open set $U\subseteq X$* if for every integer $\alpha>0$ and every ample line bundle $H$ on $X$, there exists an integer $\beta>0$ such that

$\widehat{S}^{\alpha\beta}\mathcal{F}\otimes H^{\otimes\beta}$

is generated by global sections at each point of $U$. It is simply called *weakly positive* if such an open set $U$ exists.

###### Example 12.22 (Line bundles).

Let’s see what weak positivity means in the case of line bundles on projective varieties. Note that a line bundle $L$ is generically globally generated

$\alpha\beta M+\beta H$ is effective.

Dividing by $\beta$ and letting $\alpha\to\infty$, we see that this is equivalent to $M$ being in the closure of the cone of effective divisors. i.e. with $M$ being pseudoeffective.

###### Example 12.23 (Nef vector bundles).

If $E$ is a nef vector bundle on a smooth projective variety $X$, then $E$ is weakly positive. Indeed, fix an ample line bundle $H$ on $X$, and a positive integer $\alpha$. If $\pi:\mathbf{P}=\mathbf{P}(E)\to X$ is the associated projective bundle, note first that $\mathcal{O}_{\mathbf{P}}(\alpha)\otimes\pi^{*}H$ is an ample line bundle on $\mathbf{P}$; indeed, both $\mathcal{O}_{\mathbf{P}}(\alpha)$ and $\pi^{*}H$ are nef, so have non-negative intersection with all subvarieties. On the other hand, $\mathcal{O}_{\mathbf{P}}(\alpha)$ is relatively ample, and so has positive intersection with subvarieties in the fibers of $\pi$ (“vertical” subvarieties), while $\pi^{*}H$ has positive intersection with subvarieties that are not contracted to a point by $\pi$ (“horizontal” subvarieties). It follows that $\mathcal{O}_{\mathbf{P}}(\alpha\beta)\otimes\pi^{*}H^{\otimes\beta}$ is globally generated for $\beta\gg 0$. On the other hand, by the projection formula we have that

$\pi_{*}\big{(}\mathcal{O}_{\mathbf{P}}(\alpha\beta)\otimes\pi^{*}H^{\otimes\beta}\big{)}\simeq S^{\alpha\beta}E\otimes H^{\otimes\beta}.$

It is not hard to deduce from here that $S^{\alpha\beta}E\otimes H^{\otimes\beta}$ itself is globally generated for $\beta\gg 0$ (see also Exercise 12.5). It follows that $E$ is weakly positive over $X$.

Given the example above, the following result is an extension of Theorem 12.11 to morphisms that are not necessarily smooth.

###### Theorem 12.24 (Viehweg).

Let $f:X\to Y$ be a surjective morphism of projective varieties. Then, for every $m\geq 0$, the sheaf $f_{*}\omega_{X/Y}^{\otimes m}$ is weakly positive.

###### Proof.

Recall the notation in the section on Viehweg’s fiber product trick. If we denote by $X^{(s)}$ a resolution of singularities of the irreducible component of the $s$-fold fiber product of $X$ over $Y$, there is an induced morphism

$f^{(s)}:X^{(s)}\longrightarrow Y.$

Given that a torsion-free sheaf by definition injects into its double-dual, by Proposition 12.9 for every $s\geq 1$ there is an inclusion

$\varphi:f_{*}^{(s)}\omega_{X^{(s)}/Y}^{\otimes m}\hookrightarrow\left(\left(f_{*}\omega_{X/Y}^{\otimes m}\right)^{\otimes s}\right)^{\vee\vee}$

which is generically an isomorphism. (Proposition 12.8 says that it is for instance an isomorphism on the locus in $Y$ over which $f$ is smooth.)

Let $H$ be an ample line bundle on $Y$, and $\alpha>0$ an integer. Since $H$ is ample, there exists some $k>0$ such that $H^{\otimes k}$ is very ample, and Corollary 11.3 implies that

$f_{*}^{(s)}\omega_{X^{(s)}/Y}^{\otimes m}\otimes A^{\otimes m}$

is globally generated, where $n=\dim Y$ and

$A=\omega_{Y}\otimes H^{\otimes k(n+1)}.$

Notes for 483-3

But the generic isomorphism $\varphi$ above implies then that

$$
\left(\left(f_* \omega_{X/Y}^{\otimes m}\right)^{\otimes s}\right)^{\vee \vee} \otimes A^{\otimes m}
$$

is generated by global sections over the locus where $\varphi$ is an isomorphism. Since $H$ is ample, there is also an integer $a$ such that $H^{\otimes b} \otimes \omega_Y^{\otimes -m}$ is globally generated for all $b \geq a$. Taking tensor product, we conclude that

$$
\left(\left(f_* \omega_{X/Y}^{\otimes m}\right)^{\otimes s}\right)^{\vee \vee} \otimes H^{\otimes \beta}
$$

is generically globally generated for $\beta \geq a + mk(n + 1)$. The key point is that this $\beta$ is independent of $s$, while the open set $U$ on which generation by global section happens can also be chosen to be independent of $s$, since it contains the locus over which $f$ is smooth. Finally, note that $\left(\left(f_* \omega_{X/Y}^{\otimes m}\right)^{\otimes s}\right)^{\vee \vee}$ surjects onto $\widehat{S}^s f_* \omega_{X/Y}^{\otimes m}$, and so by taking $s = \alpha \beta$ with $\beta$ satisfying the bound above we obtain that

$$
\widehat{S}^{\alpha \beta} f_* \omega_{X/Y}^{\otimes m} \otimes H^{\otimes \beta}
$$

is generated by global sections over $U$, which is what we wanted to show.

Remark 12.25. The proof above gives something a bit stronger than the statement, namely an "effective" version of weak positivity. Indeed, once we fix the very ample line bundle $H^{\otimes k}$, then we have the effectively constructed $A^{\otimes m}$ that can be taken to verify the definition of weak positivity.

## 13. Multiplication maps

Let $X$ be a projective scheme, and $L$ a line bundle on $X$. For each $m, n \geq 0$ we have multiplication maps on global sections

$$
H^0(X, L^{\otimes m}) \otimes H^0(X, L^{\otimes n}) \longrightarrow H^0(X, L^{\otimes m + n}). \tag{15}
$$

In particular, for each $m \geq 0$ there is a natural map

$$
H^0(X, L)^{\otimes m} \longrightarrow H^0(X, L^{\otimes m}).
$$

Since the product of sections does not depend on the order of multiplication, it is clear that this map factors through the symmetric algebra, meaning that the natural map to consider is in fact

$$
S^m H^0(X, L) \longrightarrow H^0(X, L^{\otimes m}). \tag{16}
$$

Example 13.1. If $X = \mathbf{P}^n$ and $L = \mathcal{O}_{\mathbf{P}^n}(d)$, then the map in (16) is given by multiplication of polynomials, and is in fact an isomorphism: both sides coincide with the space of homogeneous polynomials of degree $md$ in $n + 1$ variables.

Exercise 13.2. If $\mathfrak{b}_k$ denotes the base ideal of the linear system $|kL|$, then show that

$$
\mathfrak{b}_m \cdot \mathfrak{b}_n \subseteq \mathfrak{b}_{m + n}.
$$

Exercise 13.3. Let $L$ be an ample line bundle. Then there exists $m_0 \in \mathbf{N}$ such that the multiplication maps in (15) are surjective for all $m, n \geq m_0$.

Consider now a projective morphism $f:X\to Y$ of quasi-projective varieties, and let $L$ be a line bundle on $X$. On any fiber $F$, the restriction $L_{F}$ induces multiplication maps as in (16), namely

$S^{m}H^{0}(F,L_{F})\longrightarrow H^{0}(F,L_{F}^{\otimes m}).$

In fact it is not hard to check there are also induced morphisms

$\varphi_{m}:S^{m}f_{*}L\longrightarrow f_{*}L^{\otimes m},$

which factor the natural morphism $(f_{*}L)^{\otimes m}\to f_{*}L^{\otimes m}$. Note that if $U\subseteq Y$ is the open set over which $f$ is flat, and $V_{k}\subseteq Y$ is the open set over which $h^{0}(F,L_{F}^{\otimes k})$ is constant, by Grauert’s theorem it follows that at a point $y\in U\cap V_{1}\cap V_{m}$ the morphism $\varphi_{m}$ is precisely the multplication map on the fiber $F$ over $y$ described above.

Now the domain and target of $\varphi_{m}$ are torsion-free sheaves, and therefore if $Y$ is smooth they are locally free in codimension one. By Lemma 12.19 it follows that $\varphi_{m}$ extends uniquely to a morphism

(17) $\widehat{\varphi}_{m}:\widehat{S}^{m}f_{*}L\longrightarrow\big{(}f_{*}L^{\otimes m}\big{)}^{\vee\vee}.$

Such maps will be useful in what follows.

## 14. Iitaka’s conjecture for a base of general type

In this section we will show that Theorem 12.24 can be used to prove Iitaka’s conjecture on the subaddititvity of the Kodaira dimension when the base is of general type. The result and the proof presented here are both due to Viehweg (as is most of this part of the course). Let’s start with a few preliminary results.

###### Lemma 14.1.

Let $f:X\to Y$ be a surjective projective morphism with connected fibers between smooth varieties, and let $L$ be a line bundle on $X$. Then for any $k\geq 1$ there exists an effective divisor $B$ on $X$ such that $\operatorname{codim}_{Y}f(B)\geq 2$ and

$\big{(}f_{*}L^{\otimes m}\big{)}^{\vee\vee}\simeq f_{*}\big{(}L^{\otimes m}(mB)\big{)},\quad\forall\ m\leq k.$

###### Proof.

Let $U$ be the maximal open set on which $f_{*}L^{\otimes m}$ is locally free for all $m\leq k$, and denote $V=f^{-1}(U)$. Since all of these push-forward sheaves are torsion-free, we know that $Y\smallsetminus U$ has codimension at least $2$ in $Y$, and therefore

$\big{(}f_{*}L^{\otimes m}\big{)}^{\vee\vee}\simeq i_{*}\left((f_{*}L^{\otimes m})_{|U}\right)\simeq i_{*}f_{V_{*}}(L_{|V}^{\otimes m})\simeq f_{*}\big{(}j_{*}L_{|V}^{\otimes m}\big{)},$

where the maps are summarized in the following diagram, the horizontal maps being the natural inclusions:

where the map

Denote $D=X\smallsetminus V$. If the codimension of $D$ is again at least $2$, since $L^{\otimes m}$ is locally free we have that $j_{*}L^{\otimes m}_{|V}\simeq L^{\otimes m}$, so we can take $B=0$. If $D$ is a divisor, then

$j_{*}L^{\otimes m}_{|V}\simeq L^{\otimes m}(*D):=\bigcup_{p\geq 0}L^{\otimes m}(pD),$

i.e. the quasi-coherent sheaf of sections of $L^{\otimes m}$ with poles of arbitrary order along $D$. (Locally over some Spec $A$, this is isomorphic to the localization $A_{f}$, where $f$ is a local equation of $D$.) Note then that for each $m$ we have an ascending chain of coherent subsheaves

$\cdots\subseteq f_{*}\big{(}L^{\otimes m}(pD)\big{)}\subseteq f_{*}\big{(}L^{\otimes m}((p+1)D)\big{)}\subseteq\cdots\subseteq\big{(}f_{*}L^{\otimes m}\big{)}^{\vee\vee}.$

Since $\big{(}f_{*}L^{\otimes m}\big{)}^{\vee\vee}$ is a coherent sheaf as well, it follows that each such chain must stabilize, and at some $p_{0}$ where it does we have

$f_{*}\big{(}L^{\otimes m}(pD)\big{)}\simeq\big{(}f_{*}L^{\otimes m}\big{)}^{\vee\vee},\ \ \forall\ p\geq p_{0}.$

Finally, as we are only looking at finitely many $m$, choosing $B$ to be a sufficiently large multiple of $D$ implies the slightly more precise version in the statement. ∎

###### Lemma 14.2.

Let $f:X\to Y$ be a morphism of smooth varieties. Then there exists a proper birational morphism $\tau:Y^{\prime}\to Y$ with $Y^{\prime}$ smooth, and a resolution of singularities $X^{\prime}$ of the main component of $X\times_{Y}Y^{\prime}$, such that the induced morphism $f^{\prime}:X^{\prime}\to Y^{\prime}$ has the property that every divisor $B^{\prime}$ in $X^{\prime}$ with $\operatorname{codim}f^{\prime}(B^{\prime})\geq 2$ is contained in the exceptional locus of $\tau^{\prime}:X^{\prime}\to X$.

###### Proof.

The main point is the “flattening” theorem due to Hironaka and Gruson-Raynaud, whose proof goes beyond the scope of this course: one can find a proper birational morphism $\tau:Y^{\prime}\to Y$ with $Y^{\prime}$ smooth such that the induced morphism

$\tilde{f}:\tilde{X}=(X\times_{Y}Y^{\prime})_{\operatorname{main}}\to Y^{\prime}$

is flat. Denoting by $\mu:X^{\prime}\to\tilde{X}$ a resolution of singularities, since $\tilde{f}$ is flat it follows that if $B^{\prime}$ is contracted by $f^{\prime}$, then it must already be exceptional for $\mu$, so also for $\tau^{\prime}$. ∎

###### Theorem 14.3.

Let $f:X\to Y$ be a surjective morphism with connected fibers between smooth projective varieties, and denote by $F$ the general fiber of $f$. Then:

(i) If $L$ is an ample line bundle on $Y$, and $m\geq 1$, then

$\kappa\left(X,\omega^{\otimes m}_{X/Y}\otimes f^{*}L\right)=\kappa(F)+\dim Y.$

(ii) If $Y$ is of general type, then

$\kappa(X)=\kappa(F)+\dim Y,$

i.e. Iitaka’s conjecture holds.

###### Proof.

We first consider the following technical point: according to Lemma 14.2, there exists a smooth birational modification $\tau\colon Y^{\prime}\to Y$, and a resolution $X^{\prime}$ of $X\times_{Y}Y^{\prime}$

Mihnea Popa

giving a commutative diagram

![img-2.jpeg](img-2.jpeg)

with the property that every effective divisor  $B$  on  $X'$  such that  $\operatorname{codim} f'(B) \geq 2$  lies in the exceptional locus of  $\tau'$ . Note that for such a divisor  $B$  we have

$$
\tau_ {*} ^ {\prime} \omega_ {X ^ {\prime}} ^ {\otimes m} (m B) \simeq \omega_ {X} ^ {\otimes m}, \quad \forall m \geq 0.
$$

Fix now an ample line bundle  $L$  on  $Y$ , and consider the big line bundle  $L' = \tau^{*}L$  on  $Y'$ . By Theorem 12.24 we have that for any  $m &gt; 0$  (which we can assume to be such that  $f_{*}'\omega_{X'/Y'}^{\otimes m} \neq 0$ ) there exists  $b &gt; 0$  such that

$$
\widehat {S} ^ {2 b} f _ {*} ^ {\prime} \omega_ {X ^ {\prime} / Y ^ {\prime}} ^ {\otimes m} \otimes L ^ {\prime \otimes b}
$$

is generically globally generated. Moreover, we have seen in (17) that there exists a morphism

$$
\widehat {S} ^ {2 b} f _ {*} ^ {\prime} \omega_ {X ^ {\prime} / Y ^ {\prime}} ^ {\otimes m} \longrightarrow \left(f _ {*} ^ {\prime} \omega_ {X ^ {\prime} / Y ^ {\prime}} ^ {\otimes 2 m b}\right) ^ {\vee \vee}
$$

induced by the relative multiplication map, which is non-trivial at the general point of  $Y$ . On the other hand, by Lemma 14.1 there exists an effective divisor  $B$  on  $X'$ , exceptional for  $f'$ , such that

$$
\left(f _ {*} ^ {\prime} \omega_ {X ^ {\prime} / Y ^ {\prime}} ^ {\otimes p}\right) ^ {\vee \vee} \simeq f _ {*} ^ {\prime} \left(\omega_ {X ^ {\prime} / Y ^ {\prime}} ^ {\otimes p} (p B)\right), \quad \forall p \leq 2 m b.
$$

Putting everything together, it follows that

$$
f _ {*} ^ {\prime} \left(\omega_ {X ^ {\prime} / Y ^ {\prime}} ^ {\otimes 2 m b} (2 m b B)\right) \otimes L ^ {\prime \otimes b}
$$

has a non-zero section. Using the projection formula, we obtain an inclusion

$$
f ^ {\prime *} L ^ {\prime \otimes b} \hookrightarrow \left(\omega_ {X ^ {\prime} / Y ^ {\prime}} (B)\right) ^ {\otimes 2 m b} \otimes f ^ {\prime *} L ^ {\prime \otimes 2 b}.
$$

According to Lemma 7.4, we obtain that

$$
\kappa \left(\left(\omega_ {X ^ {\prime} / Y ^ {\prime}} (B)\right) ^ {\otimes k} \otimes f ^ {\prime *} L ^ {\prime}\right) = \kappa (F ^ {\prime}) + \dim Y ^ {\prime} = \kappa (F) + \dim Y,
$$

where  $F'$  is the general fiber of  $f'$ . For the second equality, note on one hand that  $F'$  and  $F$  are birational, while on the other hand since  $B$  is contracted by  $f'$ , it does not meet  $F'$ , and therefore the restriction of  $\omega_{X'/Y'}(B)$  to  $F'$  is  $\omega_{F'}$ .

To deduce (i), note that since by Easy Addition we have

$$
\kappa (F) + \dim Y \geq \kappa \left(X, \omega_ {X / Y} ^ {\otimes m} \otimes f ^ {*} L\right),
$$

it suffices to show that

$$
\kappa \left(X, \omega_ {X / Y} ^ {\otimes m} \otimes f ^ {*} L\right) \geq \kappa \left(\left(\omega_ {X ^ {\prime} / Y ^ {\prime}} (B)\right) ^ {\otimes m} \otimes f ^ {\prime *} L ^ {\prime}\right),
$$

for which in turn, it suffices to have an inclusion

$$
\tau_ {*} ^ {\prime} \left(\omega_ {X ^ {\prime}} ^ {\otimes m} (m B) \otimes f ^ {\prime *} \omega_ {Y ^ {\prime}} ^ {\otimes - m} \otimes f ^ {\prime *} L ^ {\prime}\right) \hookrightarrow \omega_ {X / Y} ^ {\otimes m} \otimes f ^ {*} L.
$$

Notes for 483-3

To deduce (ii), since $Y'$ is of general type recall that by Kodaira's Lemma there exists an inclusion $L' \hookrightarrow \omega_{Y'}^{\otimes r}$ for some $r &gt; 0$. This implies that

$$
\kappa (X) = \kappa (X ^ {\prime}, \omega_ {X ^ {\prime}} (B)) \geq \kappa \left(\left(\omega_ {X ^ {\prime} / Y ^ {\prime}} (B)\right) ^ {\otimes r} \otimes f ^ {\prime *} L ^ {\prime}\right),
$$

which is equal to $\kappa(F) + \dim Y$ by the above.

# 15. VARIATION OF FAMILIES OF VARIETIES

Let $f: X \to Y$ be a fiber space between smooth projective varieties over $\mathbf{C}$, and let $\eta$ be the generic point of $Y$. We use the notation $X_{\eta}$ for the generic fiber of $f$, and $X_{\overline{\eta}}$ the generic geometric fiber, i.e.

$$
X _ {\overline {{\eta}}} \simeq X _ {\eta} \times_ {k (\eta)} \overline {{k (\eta)}}.
$$

**Definition 15.1 (Variation).** The variation of $f$, denoted $\operatorname{Var}(f)$, is the smallest integer $\ell$ such that there exists an algebraically closed subfield

$$
K \subseteq \overline {{K (Y)}} = \overline {{k (\eta)}} \quad \text{with} \quad \operatorname{trdeg}_{\mathbf{C}} K = \ell,
$$

and a smooth projective variety $T$ defined over $K$, such that

$$
T \times_ {K} \overline {{K (Y)}} \sim X _ {\overline {{\eta}}}.
$$

(Here $\sim$ means birational.) Note that

$$
0 \leq \operatorname{Var} (f) \leq \dim Y,
$$

and if $\operatorname{Var}(f) = \dim Y$ we say that $f$ has *maximal variation*; this last condition means that any smooth fiber of $f$ can be birational to at most countably many other fibers.

The study of arbitrary families is sometimes reduced to that of families of maximal variation by means of the following useful result. Doing this properly requires quite a bit of extra preparation, so I will only quote it here.

**Proposition 15.2.** Let $f: X \to Y$ be a fiber space of smooth projective varieties. Then there exists another fiber space $f'': X'' \to Y''$ of smooth projective varieties, with

$$
\operatorname{Var} (f) = \operatorname{Var} (f ^ {\prime \prime}) = \dim Y ^ {\prime \prime} \quad \text{and} \quad X _ {\overline {{\eta}}} \simeq X _ {\overline {{\eta^ {\prime \prime}}}} ^ {\prime \prime} \times_ {\overline {{k (\eta^ {\prime \prime})}}} \overline {{k (\eta)}},
$$

and another smooth projective variety $Y'$ with a generically finite map $\tau: Y' \to Y$, and a map $\rho: Y' \to Y''$ such that $X \times_Y Y'$ and $X'' \times_{Y''} Y'$ are birationally isomorphic over $Y'$ (meaning that the birational isomorphism respects the projections onto $Y'$).

Denoting by $X'$ a common resolution of $X \times_Y Y'$ and $X'' \times_{Y''} Y'$ in the Proposition above, we obtain a commutative diagram

$$
\begin{array}{c}
X \xleftarrow {\tau^ {\prime}} X ^ {\prime} \xrightarrow {\rho^ {\prime}} X ^ {\prime \prime} \\
\Biggl \downarrow_ {f} \quad \Biggl \downarrow_ {f ^ {\prime}} \quad \Biggl \downarrow_ {f ^ {\prime \prime}} \\
Y \xleftarrow {\tau} Y ^ {\prime} \xrightarrow {\rho} Y ^ {\prime \prime}
\end{array} \tag {18}
$$

###### Example 15.3.

An isotrivial family has variation equal to $0$. More generally, one has $\mathrm{Var}(f)=0$ if and only if $f$ is birationally isotrivial, i.e. there exists a generically finite cover $\tau:Y^{\prime}\to Y$ such that the fiber product $X\times_{Y}Y^{\prime}$ is birational to $Y^{\prime}\times F$, where $F$ is the general fiber of $f$. Indeed, in this case $Y^{{}^{\prime\prime}}$ in the Proposition above is just a point.

###### Example 15.4.

Say $f:X\to Y$ is a family of stable curves with general member a smooth curve of genus $g\geq 2$, induced by pullback from the moduli space $\overline{\mathcal{M}_{g}}$ via a morphism $\varphi:Y\to\overline{\mathcal{M}_{g}}$. Then

$\mathrm{Var}(f)=\dim\varphi(Y).$

In particular, $f$ has maximal variation if and only if $\varphi$ is a generically finite onto its image. Given our previous discussion of positivity coming from the moduli space of curves, in this case we have that

$\det f_{*}\omega_{X/Y}^{\otimes m}$

is a big and nef line bundle for $m\gg 0$. We will focus on this property even when there is no moduli space involved.

The example above, and other similar consideration involving other parameter spaces (like period domains), suggests that when the familiy has non-trivial variation there is extra positivity in the sheaves $f_{*}\omega_{X/Y}^{\otimes m}$, which may lead to even better bounds for $\kappa(X)$ than what is predicted by Iitaka’s conjecture. This was formalized by Viehweg:

###### Conjecture 15.5 (Viehweg’s $C_{n,m}^{+}$ conjecture).

Let $f:X\to Y$ be a fiber space between smooth projective varieties, with $\kappa(Y)\geq 0$, and denote by $F$ the generic fiber of $f$. Then

$\kappa(X)\geq\kappa(F)+\max\{\kappa(Y),\mathrm{Var}(f)\}.$

###### Example 15.6.

Let $f:S\to E$ be a surjective morphism from a smooth projective surface to an elliptic curve, with general fiber $F$ satisfying $g(F)\geq 2$. There are two main possibilities, according to the two possible values $0$ and $1$ for $\mathrm{Var}(f)$:

(i) $f$ is isotrivial, meaning a product $E\times F$ at least after a finite cover of $E$. In this case it is not hard to show that $\kappa(S)=1=\kappa(F)+\kappa(E)$, so in particular $S$ also has an elliptic fibration. (Note that in the case of families of smooth projective curves isotrivial and birationally isotrivial is essentially the same thing, since such curves do not have other smooth birational models.)

(ii) $f$ is not isotrivial. In this case one can check that $f$ cannot also have an elliptic fibration, and since in any case $\kappa(S)\geq 1$, it means that $S$ must be of general type. (As mentioned in Example 6.20, surfaces of general type with $q(S)=1$ do exist.) Note that in this case

$\kappa(S)=\kappa(F)+\mathrm{Var}(f)>\kappa(F)+\kappa(E).$

Conjecture 15.5 is clear when $X$ is of general type, as $\mathrm{Var}(f)$ cannot go beyond the dimension of $Y$. Also, it is equivalent to the usual $C_{n,m}$ conjecture when $Y$ is of general type, and we have seen that this is known to be true. The most important known result that goes beyond $C_{n,m}$ is Kollár’s proof of the conjecture when the fibers are of general type.

Notes for 483-3

Theorem 15.7 (Kollár). The  $C_{n,m}^{+}$  conjecture holds when  $F$  is of general type.

The rest of the notes (when I eventually post them) will be devoted to proving this result, following a strategy due to Viehweg. This involves algebraic techniques; Kollár's original approach was somewhat more analytic in nature. The statement follows in fact from two separate statements that are both important on their own.

First, Viehweg in fact showed that the  $C_{n,m}^{+}$  conjecture is a consequence of an even stronger conjecture regarding direct images of relative pluricanonical bundles.

Conjecture 15.8 (Viehweg's  $Q_{n,m}$  conjecture). Let  $f: X \to Y$  be a fiber space between smooth projective varieties, such that  $\operatorname{Var}(f) = \dim Y$ . Then  $\det f_*\omega_{X/Y}^{\otimes m}$  is a big line bundle on  $Y$  for some  $m &gt; 0$ .

Theorem 15.9 (Viehweg). The  $Q_{n,m}$  conjecture implies the  $C_{n,m}^{+}$  conjecture.

On the other hand Kollár showed that the  $Q_{n,m}$  conjecture holds in a slightly stronger form for fiber spaces with fibers of general type. This implies Theorem 15.7.

Theorem 15.10 (Kollár). Let  $f: X \to Y$  be a fiber space between smooth projective varieties, whose general fiber is of general type. If  $\operatorname{Var}(f) = \dim Y$ , then for sufficiently large and divisible  $m$ ,  $\det f_*\omega_{X/Y}^{\otimes m}$  is a big line bundle on  $Y$ .

# 16. BIGNESS OF THE DETERMINANT IMPLIES VIEHWEG'S CONJECTURE

THE COURSE ROUGHLY ENDED HERE, BUT I INCLUDED A FEW MORE IMPORTANT RESULTS BELOW, IN A BIT OF A RUSH. THIS SECTION NEEDS A FEW MORE EXPLANATIONS. I WILL ADD THEM WHEN I FIND A MOMENT.

In this section we will prove Theorem 15.9 following Viehweg, and therefore reduce the  $C_{n,m}^{+}$  conjecture to showing the bigness of determinants of push-forwards of relative dualizing sheaves. The first thing to note is that using Lemma 14.2, diagram (18) can be refined to the following

![img-3.jpeg](img-3.jpeg)

where  $\gamma$  and  $\gamma'$  are birational, and if a divisor is  $f_1$ -exceptional, then it is  $\gamma'$ -exceptional, while all the other maps have the properties in Proposition 15.2. Moreover, by allowing  $X'$  and  $Y''$  to be only normal projective Gorenstein, with rational singularities, we can assume that  $\rho$  and  $f''$  are weakly semistable morphisms with connected fibers, and in particular flat. (EXPLAIN.)

Lemma 16.1. In the situation of the above diagram, we have

$$
\rho^ {*} f _ {*} ^ {\prime \prime} \omega_ {X ^ {\prime \prime} / Y ^ {\prime \prime}} ^ {\otimes m} \simeq f _ {*} ^ {\prime} \omega_ {X ^ {\prime} / Y ^ {\prime}} ^ {\otimes m},
$$

and this is a reflexive sheaf on $Y^{\prime}$.

###### Proposition 16.2.

In the situation of diagram (19), assume that $\det f_{*}\omega_{X^{\prime\prime}/Y^{\prime\prime}}^{\otimes m}$ is a big line bundle for some $m>0$. Then

$\kappa(Y,\det f_{*}\omega_{X/Y}^{\otimes m})\geq\operatorname{Var}(f).$

###### Proof.

Recall first that by Lemma 16.1 we have

$\rho^{*}f_{*}^{\prime\prime}\omega_{X^{\prime\prime}/Y^{\prime\prime}}^{\otimes m}\simeq f_{*}^{\prime}\omega_{X^{\prime}/Y^{\prime}}^{\otimes m}.$

As $\rho$ has connected fibers and hence $\rho_{*}\mathcal{O}_{Y^{\prime}}\simeq\mathcal{O}_{Y^{\prime\prime}}$, we then have

$\kappa(Y^{\prime},\det f_{*}^{\prime}\omega_{X^{\prime}/Y^{\prime}}^{\otimes m})=\kappa(Y^{{}^{\prime\prime}},\det f_{*}^{{}^{\prime\prime}}\omega_{X^{\prime\prime}/Y^{\prime\prime}}^{\otimes m})=\dim Y^{{}^{\prime\prime}}=\operatorname{Var}(f).$

Denote $\nu=\gamma\circ\tau:Y^{\prime}\to Y$ and $\nu^{\prime}=\gamma^{\prime}\circ\tau^{\prime}:X^{\prime}\to X$. All the sheaves involved in the argument are reflexive (in fact here they are line bundles), and so to do calculations of sections we are allowed to use formulas obtained after throwing away closed subsets of codimension at least $2$ in $Y$ and $Y^{\prime}$; we can therefore assume that $\nu$ is flat and $Y^{\prime}$ is smooth.

By the flat base change theorem we obtain then an inclusion

$\det f_{*}^{\prime}\omega_{X^{\prime}/Y^{\prime}}^{\otimes m}\hookrightarrow\nu^{*}\det f_{*}\omega_{X/Y}^{\otimes m}.$

As before, this implies

$\kappa(Y,\det f_{*}\omega_{X/Y}^{\otimes m})=\kappa(Y^{\prime},\nu^{*}\det f_{*}\omega_{X/Y}^{\otimes m})\geq\kappa(Y^{\prime},\det f_{*}^{\prime}\omega_{X^{\prime}/Y^{\prime}}^{\otimes m})=\operatorname{Var}(f).$

∎

###### Proposition 16.3.

In the situation of diagram (19), assume that $\det f_{*}^{\prime\prime}\omega_{X^{\prime\prime}/Y^{\prime\prime}}^{\otimes m}$ is a big line bundle for some $m>0$. If $L$ is a line bundle on $Y$ such that $\kappa(L)\geq 0$, then

$\kappa(X,\omega_{X/Y}\otimes f^{*}L)\geq\kappa(F)+\max\{\kappa(L),\operatorname{Var}(f)\}.$

###### Proof.

The first claim is that the bigness of $\det f_{*}\omega_{X^{\prime\prime}/Y^{\prime\prime}}^{\otimes m}$ implies that we may assume that there is an ample line bundle $H$ on $Y^{{}^{\prime\prime}}$ such that

$H\hookrightarrow f_{*}^{\prime\prime}\omega_{X^{\prime\prime}/Y^{\prime\prime}}^{\otimes m}.$

(EXPLAIN.) By Lemma 16.1 we obtain then the inclusion

$\rho^{*}H\hookrightarrow f_{*}^{\prime}\omega_{X^{\prime}/Y^{\prime}}^{\otimes m}.$

Pulling this back to $X^{\prime}$ and using the adjunction mapping, we get the inclusion

$f^{\prime*}\rho^{*}H\hookrightarrow\omega_{X^{\prime}/Y^{\prime}}^{\otimes m}.$

Using the notation in the proof of the previous Proposition, and the fact that $\kappa(L)\geq 0$, we obtain

$\kappa\big{(}X^{\prime},(\omega_{X^{\prime}/Y^{\prime}}\otimes\nu^{\prime*}f^{*}L)^{\otimes a}\otimes f^{\prime*}\rho^{*}H^{\otimes-b}\big{)}\geq 0$

for some $a,b>0$.

Now consider the fiber space $g=\rho\circ f^{\prime}:X^{\prime}\to Y^{{}^{\prime\prime}}.$ Because of the formula above, the line bundle $\omega_{X^{\prime}/Y^{\prime}}\otimes\nu^{\prime*}f^{*}L$ on $X^{\prime}$ satisfies the hypothesis of Lemma 7.4 with respect to

this fibration. On the other hand, the general fiber $G$ of this map is birational to $F^{\prime}\times F_{\rho}$, where $F_{\rho}$ is the general fiber of $\rho$. Note that the restriction of $\omega_{X^{\prime}/Y^{\prime}}\otimes\nu^{\prime*}f^{*}L$ to this is the box product $\omega_{F^{\prime}}\boxtimes(\nu^{*}L)_{F_{\rho}}$. Using Lemma 7.4 we therefore obtain

$\kappa(X^{\prime},\omega_{X^{\prime}/Y^{\prime}}\otimes\nu^{\prime*}f^{*}L)=\dim Y^{{}^{\prime\prime}}+\kappa(F^{\prime})+\kappa(F_{\rho},(\nu^{*}L)_{F_{\rho}}).$

Recall that $\dim Y^{{}^{\prime\prime}}=\mathrm{Var}(f)$, and $\kappa(F^{\prime})=\kappa(F)$ since the two are birational. Using the Easy Addition, Lemma 7.3, for the morphism $\rho$, we also have

$\dim Y^{{}^{\prime\prime}}+\kappa(F_{\rho},(\nu^{*}L)_{F_{\rho}})\geq\kappa(Y^{\prime},\nu^{*}L)\geq\kappa(L).$

Putting the last two formulas together, we obtain

$\kappa(X^{\prime},\omega_{X^{\prime}/Y^{\prime}}\otimes\nu^{\prime*}f^{*}L)\geq\kappa(F)+\max\{\kappa(L),\mathrm{Var}(f)\}.$

We will now show that there exists an $f_{1}$-exceptional effective divisor $B$ such that

(20) $\kappa\big{(}X_{1},\omega_{X_{1}/Y_{1}}\otimes\gamma^{\prime*}f^{*}L\otimes\mathcal{O}_{X_{1}}(B)\big{)}\geq\kappa(X^{\prime},\omega_{X^{\prime}/Y^{\prime}}\otimes\nu^{\prime*}f^{*}L).$

Assuming this, since $B$ is also $\gamma^{\prime}$-exceptional by our set-up, we obtain

$\kappa(X,\omega_{X/Y}\otimes f^{*}L)\geq\kappa\big{(}X_{1},\omega_{X_{1}/Y_{1}}\otimes\gamma^{\prime*}f^{*}L\otimes\mathcal{O}_{X_{1}}(B)\big{)}.$

Indeed, since both $K_{X_{1}/X}$ and $K_{Y_{1}/Y}$ are supported on $\gamma^{\prime}$ and $\gamma$-exceptional divisors, we have that

$K_{X_{1}/Y_{1}}+B\leq\gamma^{\prime*}K_{X/Y}+B+E,$

where $E+B$ is a $\gamma^{\prime}$-exceptional divisor, and this immediately implies the inequality. Combined with the inequalities above, this implies the result we are after.

Finally, we need to show (20). EXPLAIN. ∎

Assuming Theorem 15.10, Propositions 16.2 and 16.3 imply the following more general version of the $C_{n,m}^{+}$ conjecture when the fibers are of general type. Note that (iii) below is the special case of (ii) when $L=\omega_{Y}$. The proof of Theorem 15.10 occupies the next two sections.

###### Corollary 16.4.

Let $f:X\to Y$ be a fiber space between smooth projective varieties, whose general fiber is of general type. Then the following hold:

(i) For sufficiently large and divisible $m$,

$\kappa(Y,\det f_{*}\omega_{X/Y}^{\otimes m})\geq\mathrm{Var}(f).$

(ii) If $L$ is any line bundle on $Y$ with $\kappa(L)\geq 0$, then

$\kappa(X,\omega_{X/Y}\otimes f^{*}L)\geq\kappa(F)+\max\{\kappa(L),\mathrm{Var}(f)\}.$

(iii) If $\kappa(Y)\geq 0$, then $C_{n,m}^{+}$ holds for $f$, i.e.

$\kappa(X)\geq\kappa(F)+\max\{\kappa(Y),\mathrm{Var}(f)\}.$

Mihnea Popa

# 17. VECTOR BUNDLE CONSTRUCTIONS, VARIATION AND POSITIVITY

Universal basis morphism. Let $X$ be an irreducible scheme over a field $k$. Recall that for a vector space $V$, we denote by $\mathbb{P}(V)$ the space of one-dimensional quotients of $V$, and the same for a locally free sheaf $\mathcal{E}$ and $\mathbb{P}(\mathcal{E})$; see Section 3 for general facts about projective bundles that we will use here.

Let now $\mathcal{E}$ be a locally free sheaf of rank $r$ on $X$. Consider the projective bundle

$$
\mathbb {P} = \mathbb {P} \big (\bigoplus^ {r} \mathcal {E} ^ {\vee} \big) \xrightarrow {\pi} X.
$$

Over each $x \in X$, one can think of this as the projectivized space of matrices whose columns are vectors in $\mathcal{E}_x$. We then have

$$
\pi_ {*} \mathcal {O} _ {\mathbb {P}} (k) \simeq S ^ {k} \big (\bigoplus^ {r} \mathcal {E} ^ {\vee} \big) \simeq \bigoplus_ {\sum_ {i = 1} ^ {r} a _ {i} = k} \left(\bigotimes_ {i = 1} ^ {r} S ^ {a _ {i}} \mathcal {E} ^ {\vee}\right).
$$

We also have the natural morphism

$$
\pi^ {*} \bigoplus^ {r} \mathcal {E} ^ {\vee} \longrightarrow \mathcal {O} _ {\mathbb {P}} (1),
$$

or dually

$$
\sigma : \mathcal {O} _ {\mathbb {P}} (- 1) \longrightarrow \bigoplus^ {r} \pi^ {*} \mathcal {E}.
$$

We can think of this morphism as sending a matrix as above to its columns. It induces what Viehweg calls the universal basis morphism:

$$
s: \bigoplus^ {r} \mathcal {O} _ {\mathbb {P}} (- 1) \longrightarrow \pi^ {*} \mathcal {E},
$$

a morphism of vector bundles of the same rank $r$, which is injective and degenerates precisely along the locus corresponding to matrices with trivial determinant. This is a divisor, which we call $\Delta$. We obtain in particular

$$
\mathcal {O} _ {\mathbb {P}} (\Delta) \simeq \mathcal {O} _ {\mathbb {P}} (r) \otimes \pi^ {*} \det  \mathcal {E}.
$$

Grassmannians and vector bundle quotients. Let $V$ be a vector space over a field $k$, and $0 \leq s \leq \dim V = n$. We will denote by $\mathbb{G} := \operatorname{Grass}(V, s)$ the Grassmannian of $s$-dimensional quotients of $V$. Upon choosing a basis of $V$, this can be identified with $\operatorname{Grass}(k^n, s)$ (and therefore with $G(n - s, n)$ in the perhaps more standard notation).

The Grassmannian $\mathbb{G}$ is a fine parameter space for such quotients, and so it supports a universal quotient

$$
q: V \otimes_ {k} \mathcal {O} _ {\mathbb {G}} \longrightarrow \mathcal {S},
$$

given by the corresponding quotient parametrized by each point in $\mathbb{G}$. Passing to exterior powers, we obtain a surjective vector bundle morphism

$$
\wedge^ {s} q: \wedge^ {s} V \otimes_ {k} \mathcal {O} _ {\mathbb {G}} \longrightarrow \wedge^ {s} \mathcal {S} = \det  \mathcal {S}.
$$

12For instance, $\mathbb{P}(V) = \mathrm{Grass}(V,1)$, and $\mathcal{S} \simeq \mathcal{O}_{\mathbb{P}}(1)$, with the map $q$ being the evaluation map of the global sections of $\mathcal{O}_{\mathbb{P}}(1)$.

$\mathcal{S}$ is a line bundle on $\mathbb{G}$ generated by $\wedge^{s}V$, and in fact well-known to be very ample. This induces the celebrated Plücker embedding

$p:\mathrm{Grass}(V,s)\hookrightarrow\mathbb{P}^{M}=\mathbb{P}(\wedge^{s}V).$

Note that by definition $p^{*}\mathcal{O}_{\mathbb{P}^{M}}(1)\simeq\det\mathcal{S}$.

Analogously, let $\mathcal{E}$ be a locally free sheaf on $X$. Just as the projective bundle $\mathbb{P}(\mathcal{E})$ parametrizes one-dimensional quotients of each fiber of $E$, fixing an integer $s$ as above one defines the Grassmann bundle

$\pi:\mathrm{Grass}_{X}(\mathcal{E},s)\longrightarrow X,$

where the fiber over each point $x\in X$ is $\mathrm{Grass}(\mathcal{E}(x),s)$. In particular, if $\mathcal{E}\simeq V\otimes_{k}\mathcal{O}_{X}$ is a trivial bundle, then we can identify

$\mathrm{Grass}_{X}(V\otimes_{k}\mathcal{O}_{X},s)\simeq\mathrm{Grass}(V,s)\times X\xrightarrow{p_{2}}X.$

###### Classifying map.

Consider now a quotient of locally free sheaves of ranks $n$ and $s$ respectively:

$\varphi:\mathcal{E}\longrightarrow\mathcal{Q}.$

Over each point $x\in X$, we have a quotient $\mathcal{E}(x)\to\mathcal{Q}(x)$, which gives an element in $\mathrm{Grass}(k^{n},s)$ once we fix a basis of $\mathcal{E}(x)$. Thus if we let $G=GL_{n}(k)$ act on $\mathrm{Grass}(k^{n},s)$ by changing the basis of $k^{n}$, we obtain a mapping

$X\longrightarrow\mathrm{Grass}(k^{n},s)/G$

called the classifying map; note that it is not necessarily a morphism. However, below we will construct a (quasi-projective) space $U$ of all bases of the fibers of $\mathcal{E}$, with a projection to $X$. Then, by the universal property of the Grassmannian, the classifying map lifts to a morphism

(21) $U\longrightarrow\mathrm{Grass}(k^{n},s).$

###### Variation and positivity.

Let $\mathcal{E}$ be a locally free sheaf of rank $r$ on a projective scheme $X$ over $k$, and for some $\mu>0$ consider a locally free quotient

$\delta:S^{\mu}\mathcal{E}\longrightarrow\mathcal{Q}$

of rank $s$. For each $x\in X$, let

$K(x):=\ker(\delta_{x})\otimes_{\mathcal{O}_{X,x}}\kappa(x).$

By choosing a basis of $\mathcal{E}(x)$, we get a point

$[K(x)]\in\mathbb{G}:=\mathrm{Grass}(S^{\mu}\mathbf{C}^{r},s).$

Now the group $G=\mathrm{SL}_{r}(\mathbf{C})$ acts on $\mathbb{G}$ by changing the basis of $\mathcal{E}(x)$. The quotient $[K(x)]$ depends on the choice of basis, but its orbit $G(x):=G_{[K(x)]}$ does not, so it is an invariant of $\delta$.

###### Definition 17.1.

We say that $\ker(\delta)$ has maximal variation at $x\in X$ if the set of $y\in X$ with equal orbit $G(y)=G(x)$ is finite, and if $\dim G(x)=\dim G$.

######

###### Theorem 17.2.

Let $X$ be a projective scheme, and $\mathcal{E}$ a nef locally free sheaf on $X$. Assume that for some $\mu>0$ there exists a surjective morphism of locally free sheaves

$\delta:S^{\mu}\mathcal{E}\longrightarrow\mathcal{Q}.$

If $\mathrm{Ker}(\delta)$ has maximal variation at all $x\in X$, then $\det\mathcal{Q}$ is big.

###### Proof.

We use the notation in the previous section. In particular, recall that on

$\mathbb{P}=\mathbb{P}\big{(}\bigoplus^{r}\mathcal{E}^{\vee}\big{)}\stackrel{{\scriptstyle\pi}}{{\longrightarrow}}X$

we have the universal basis morphism

$t:\bigoplus^{r}\mathcal{O}_{\mathbb{P}}(-1)\longrightarrow\pi^{*}\mathcal{E}.$

Consider the composition

$\varphi:S^{\mu}\big{(}\bigoplus^{r}\mathcal{O}_{\mathbb{P}}\big{)}\otimes\mathcal{O}_{\mathbb{P}}(-\mu)\simeq S^{\mu}\big{(}\bigoplus^{r}\mathcal{O}_{\mathbb{P}}(-1)\big{)}\to\pi^{*}S^{\mu}\mathcal{E}\to\pi^{*}\mathcal{Q}.$

As in the previous section, this map is surjective away from the divisor $\Delta$ of matrices with trivial determinant. If we denote $\mathcal{G}:=\mathrm{Im}(\varphi)$, then this is a torsion-free sheaf that is free outside of $\Delta$. Lemma 12.20 implies that there is a birational modification $\tau:\mathbb{P}^{\prime}\to\mathbb{P}$ (obtained by blowing-up smooth centers contained in $\Delta$) such that $\mathcal{G}^{\prime}:=\tau^{*}\mathcal{G}/T$ is locally free, where $T$ is the torsion sheaf of $\tau^{*}\mathcal{G}$. We have induced objects

$\pi^{\prime}=\pi\circ\tau:\mathbb{P}^{\prime}\to X,\ \ \Delta^{\prime}=\tau^{*}\Delta,\ \ \mathcal{O}_{\mathbb{P}^{\prime}}(1):=\tau^{*}\mathcal{O}_{\mathbb{P}}(1),$

and a surjective map of locally free sheaves

$\varphi^{\prime}:S^{\mu}\big{(}\bigoplus^{r}\mathcal{O}_{\mathbb{P}^{\prime}}\big{)}\otimes\mathcal{O}_{\mathbb{P}^{\prime}}(-\mu)\longrightarrow\mathcal{G}^{\prime}.$

As in (21), to this surjection one associates a composite morphism

$\rho^{\prime}:\mathbb{P}^{\prime}\to\mathrm{Grass}(S^{\mu}\mathbf{C}^{r},s)\hookrightarrow\mathbb{P}^{M},$

where $s=\mathrm{rk}(\mathcal{Q})$, and the second map is the Plücker embedding. Note that if $\mathcal{S}$ is the universal quotient on $\mathrm{Grass}(S^{\mu}\mathbf{C}^{r},s)$, then its pull-back to $\mathbb{P}^{\prime}$ is $\mathcal{G}^{\prime}$, and therefore we have

(22) $\rho^{\prime}{}^{*}\mathcal{O}_{\mathbb{P}^{M}}(1)\simeq\det(\mathcal{G}^{\prime}(\mu))\simeq\det\mathcal{G}^{\prime}\otimes\mathcal{O}_{\mathbb{P}^{\prime}}(\mu\cdot s).$

As in the beginning of the section, the group $G=\mathrm{SL}_{r}(\mathbf{C})$ acts on $\mathrm{Grass}(S^{\mu}\mathbf{C}^{r},s)$. The next thing to note is that for a point $x\in X$, the orbit $G(x)$ associated to the map $\rho^{\prime}$ is precisely

$G(x)=\rho^{\prime}(\pi^{\prime}{}^{-1}(x)-\Delta^{\prime}\cap\pi^{\prime}{}^{-1}(x)).$

Indeed, note that $\mathbb{P}^{\prime}-\Delta^{\prime}=\mathbb{P}-\Delta$ is the locus of invertible matrices, so over a point $x$ this locus coincides with all possible choices of a basis for the fiber of the vector bundle at $x$. But now at each point in $\pi^{\prime}{}^{-1}(x)-\Delta^{\prime}\cap\pi^{\prime}{}^{-1}(x)$, the map $\rho^{\prime}$ coincides with the map $\delta$. Since $\mathrm{ker}(\delta)$ has maximal variation at each point, we get that $\rho^{\prime}$ is *generically finite* onto its image (and in fact has finite fibers when restricted to $\mathbb{P}^{\prime}-\Delta^{\prime}$).

This gives us the positivity we need: since $\rho^{\prime}$ is generically finite, the line bundle $\rho^{\prime}{}^{*}\mathcal{O}_{\mathbb{P}^{M}}(1)$ is big and nef on $\mathbb{P}^{\prime}$. We will use this below in order to show that $\det\mathcal{Q}$ is

e big. To this end, fix an ample divisor $H$ on $X$. Since $\rho^{\prime}{}^{*}\mathcal{O}_{\mathbb{P}^{M}}(1)$ is big on $\mathbb{P}^{\prime}$, Lemma 5.18 implies that for $\nu\gg 0$ one has

$H^{0}\big{(}\mathbb{P}^{\prime},\rho^{\prime}{}^{*}\mathcal{O}_{\mathbb{P}^{M}}(\nu)\otimes\pi^{\prime}{}^{*}\mathcal{O}_{X}(-H)\big{)}\neq 0.$

Recall now from (22) that $\rho^{\prime}{}^{*}\mathcal{O}_{\mathbb{P}^{M}}(\nu)\simeq(\det\mathcal{G}^{\prime})^{\otimes\nu}\otimes\mathcal{O}_{\mathbb{P}^{\prime}}(\nu\cdot\mu\cdot s)$. But by construction we have that $\det\mathcal{G}^{\prime}\subseteq\pi^{\prime}{}^{*}\det\mathcal{Q}$, so we conclude that

$H^{0}\big{(}\mathbb{P}^{\prime},\pi^{\prime}{}^{*}\big{(}(\det\mathcal{Q})^{\otimes\nu}\otimes\mathcal{O}_{X}(-H)\big{)}\otimes\mathcal{O}_{\mathbb{P}^{\prime}}(\nu\cdot\mu\cdot s)\big{)}\neq 0.$

Using the projection formula and the fact that $\pi^{\prime}_{*}\mathcal{O}_{\mathbb{P}^{\prime}}(\nu\cdot\mu\cdot s)\big{)}\simeq S^{\nu\cdot\mu\cdot s}\big{(}\bigoplus^{r}\mathcal{E}^{\vee}\big{)}$, we obtain a non-trivial homomorphism

$\alpha:S^{\nu\cdot\mu\cdot s}\big{(}\bigoplus^{r}\mathcal{E}\big{)}\longrightarrow(\det\mathcal{Q})^{\otimes\nu}\otimes\mathcal{O}_{X}(-H).$

As above, by passing to a birational modification if needed, we can assume that $N=\operatorname{Im}(\alpha)$ is locally free, and hence an invertible sheaf; indeed, the self-intersection number of $\det Q$ is equal to that of its pull-back on the modification. On the other hand, since $\mathcal{E}$ is semipositive, so is $N$, or in other words $N$ is a nef line bundle.

Now we have an inclusion $N\subseteq(\det\mathcal{Q})^{\otimes\nu}\otimes\mathcal{O}_{X}(-H)$, and so there exists an effective divisor $F$ on $X$ such that

$(\det\mathcal{Q})^{\otimes\nu}=N\otimes\mathcal{O}_{X}(H+F).$

With a slight abuse of notation, it suffices then to show that $(N+H+F)$ is big. But $N$ is nef and $H$ is ample, we have that $N+H$ is ample as well. We are then done by Kodaira’s Lemma. ∎

###### Remark 17.3.

Since $\mathcal{E}$ is nef, Lemma 12.3 implies that $\det\mathcal{Q}$ is a nef line bundle in any case. Therefore Proposition 5.23 says that its bigness proved above is equivalent to

$(\det\mathcal{Q})^{n}>0,$

where $n=\dim X$. Moreover, with a bit of care, essentially the same proof works if $X$ is only assumed to be proper, and $H$ in the proof is only taken to be nef and big. By restricting $\det\mathcal{Q}$ to each irreducible closed subscheme $Z$ of $X$ and repeating the argument, one shows in fact that

$(\det\mathcal{Q})_{|Z}^{\dim Z}>0.$

By the Nakai-Moishezon criterion, it follows that $\det\mathcal{Q}$ is ample, and hence $X$ is in fact projective. This is an important technique introduced by Viehweg and Kollár for checking the projectivity of certain moduli spaces.

## 18. Positivity for families of varieties of general type

In this section we will finally prove Theorem 15.10, using a method due to Viehweg which is based on the vector bundle constructions in the previous section.

Flat families of canonical models. In this subsection we consider the following setting: $f:X\to Y$ is a flat morphism of projective varieties, with irreducible general fiber $F$ with Gorenstein canonical singularities, and with $\omega_{F}$ ample.

###### Theorem 18.1.

(i) For every $m>0$, $f_{*}\omega_{X/Y}^{\otimes m}$ is a nef locally free sheaf on $Y$.

(ii) If in addition $\mathrm{Var}(f)=\dim Y$, then $\det f_{*}\omega_{X/Y}^{\otimes m}$ is a big line bundle for all $m$ sufficiently large and divisible.

The key point will be that varieties with ample canonical bundle (or canonically polarized varieties) can essentially be recovered from the multiplication maps on sections of powers of their canonical bundle. The first step is the following:

###### Lemma 18.2.

Let $X$ be a projective variety with $\omega_{X}$ ample. Then there exists an integer $\ell_{0}>0$ such that for all $\ell\geq\ell_{0}$ one has:

(i) $H^{i}(X,\omega_{X}^{\otimes\ell})=0$ for all $i>0$.

(ii) $\omega_{X}^{\otimes\ell}$ gives a projectively normal embedding, i.e. it is very ample and the multiplication map

$S^{\mu}H^{0}(X,\omega_{X}^{\otimes\ell})\longrightarrow H^{0}(X,\omega_{X}^{\otimes\mu\ell})$

is surjective for all integers $\mu>0$.

###### Proof.

This is just the special case $L=\omega_{X}$ in Exercise 13.3, as imposing the vanishing of higher cohomology is automatic by Serre’s theorem. ∎

Given a morphism $f$ as above, since $Y$ is a bounded family of canonically polarized varieties, we can fix an $\ell>0$ as in Lemma 18.2 that works for all fibers of $f$, so that in particular $\omega_{X/Y}$ is $f$-very ample, and for each integer $\mu>0$ the multiplication map

$S^{\mu}f_{*}\omega_{X/Y}^{\otimes\ell}\longrightarrow f_{*}\omega_{X/Y}^{\otimes\mu\ell}$

is surjective. Fix now a sufficiently large $\mu>0$, so that for each $y\in Y$ the sheaf $\mathcal{I}_{X_{y}}(\mu)$ is globally generated. We denote

$\mathcal{E}:=f_{*}\omega_{X/Y}^{\otimes\ell}\ \ \text{and}\ \ \mathcal{Q}:=f_{*}\omega_{X/Y}^{\otimes\mu\ell},$

so that indeed we have a surjective morphism

(23) $\delta:S^{\mu}\mathcal{E}\longrightarrow\mathcal{Q}$

as in the statement of Theorem 17.2.

###### Lemma 18.3.

With choices of $\ell$ and $\mu$ as above, $\mathrm{Var}(f)=\dim Y$ if and only if $\mathrm{Ker}(\delta)$ has maximal variation.

###### Proof.

First, note that since $\ell$ is chosen such that

$H^{i}(X_{y},\omega_{X_{y}}^{\otimes\ell})=0\ \ \text{for all}\ i>0,$

the morphism $f$ being flat implies that $h^{0}(X_{y},\omega_{X_{y}}^{\otimes\ell})$ is a constant, say $N+1$, as we vary the point $y$. Thus once we choose a basis of $H^{0}(X_{y},\omega_{X_{y}}^{\otimes\ell})$ giving an isomorphism with $\mathbf{C}^{N+1}$, we can consider all fibers as being embedded in a fixed projective space: $X_{y}\subseteq\mathbb{P}^{N}$.

Over each $y\in Y$, the morphism $\delta$ in (23) corresponds to a short exact sequence

$0\longrightarrow H^{0}(\mathbb{P}^{N},\mathcal{I}_{X_{y}}(\mu))\longrightarrow H^{0}(\mathbb{P}^{N},\mathcal{O}_{\mathbb{P}^{N}}(\mu))\longrightarrow H^{0}(X_{y},\mathcal{O}_{X_{y}}(\mu))\longrightarrow 0,$

and so it determines $H^{0}(\mathbb{P}^{N},\mathcal{I}_{X_{y}}(\mu))$ (the space of hypersurfaces of degree $\mu$ vanishing along $X_{y}$ in the embedding given by $\omega_{X_{y}}^{\otimes\ell}$). But we are assuming that $\mathcal{I}_{X_{y}}(\mu)$ is globally generated, so in turn this space determines the ideal sheaf $\mathcal{I}_{X_{y}}$, hence the scheme $X_{y}$.

Note also that once we choose a basis for $H^{0}(X_{y},\omega_{X_{y}}^{\otimes\ell})$, we can identify $\delta_{y}$ with a point in

$\mathrm{Grass}(S^{\mu}\mathbf{C}^{N+1},s)$

i.e. the Grassmannian of quotients of $S^{\mu}\mathbf{C}^{N+1}$ of dimension $s:=h^{0}(X_{y},\omega_{X_{y}}^{\otimes\mu\ell})=\mathrm{rk}\ \mathcal{Q}$. By what we said above, this point determines the isomorphism class of $X_{y}$ up to a change of basis, i.e. up to the natural action of $\mathrm{SL}_{N+1}(\mathbf{C})$ on $\mathrm{Grass}(S^{\mu}\mathbf{C}^{N+1},s)$.

We now check that the two conditions in Definition 17.1 are satisfied if and only if $\mathrm{Var}(f)=\dim Y$. Note first that by fixing $y\in Y$ and changing the basis of $H^{0}(X_{y},\omega_{X_{y}}^{\otimes\ell})$, by the procedure above the new kernel determines another subvariety $X^{\prime}\subset\mathbb{P}^{N}$ which is projectively equivalent (hence isomorphic) to $X_{y}$. Thus the stabilizer of the action of $G$ on the quotient $\delta_{y}$ is contained in $\mathrm{Aut}(X_{y})$. Since $X_{y}$ is of general type, a well-known theorem says that this is a finite group, and hence $\dim G(y)=\dim G$. On the other hand, if $G(y)\simeq G(y^{\prime})$, it follows in particular that $X_{y}\simeq X_{y^{\prime}}$. Since the fibers are canonically polarized, $f$ has maximal variation if and only if, for a fixed $y$, this happens only for a finite number of $y^{\prime}$. ∎

###### Proof.

(*of Theorem 18.1.*) (i) Besides local freeness (include explanation), this is essentially identical to the proof of Theorem 12.11. Indeed, instead of smoothness, one notes that when $f:X\to Y$ is weakly semistable, then $X^{s}$ is normal, Gorenstein, with canonical singularities, for all $s\geq 1$. The rest of the argument is therefore the same. Note that here we do not even need to assume that the canonical bundle is ample on the fibers, but rather just that they are of general type.

(ii) Fix notation as in the discussion preceding Lemma 18.3, so that by that result we have a morphism

$\delta:S^{\mu}\mathcal{E}\longrightarrow\mathcal{Q}$

of maximal variation. By part (i) the vector bundle $\mathcal{E}$ is nef. Theorem 17.2 implies then that $\det\mathcal{Q}$ is big (for all $\mu$ sufficiently large). ∎

###### Proof of Theorem 15.10.

We are finally able to prove Kollár’s theorem on families of varieties of general type. Assume that $f:X\to Y$ is a fiber space of smooth projective varieties, with general fiber $F$ of general type. We will show that $\det f_{*}\omega_{X/Y}^{\otimes m}$ is big, for $m$ sufficiently large and divisible, by reducing to Theorem 18.1. I am following an approach that I learned from a paper of Fujino *[x10]*, which simplifies Viehweg’s alegbraic approach to Kollár’s theorem using a number of more recent developments like weak semistable reduction and the existence of canonical models for varieties of general type. I WILL ALSO INCLUDE MORE DETAILS HERE.

*Step 1.* First we perform what is called a weak semistable reduction. According to a theorem of Abramovich-Karu, we can find a generically finite morphism $\tau:Y^{\prime}\to Y$ with $Y^{\prime}$ smooth and projective, and a morphism $f_{1}:X_{1}\to Y^{\prime}$ with the following properties

$\bullet$ $X_{1}$ is a normal projective Gorenstein variety with canonical singularities, birational to $X\times_{Y}Y^{\prime}$.

$\bullet$ $f_{1}$ is toroidal with reduced equidimensional fibers; in particular it is flat.

If we denote by $X^{\prime}$ a resolution of the main component of $X\times_{Y}Y^{\prime}$, and by $f^{\prime}:X^{\prime}\to Y^{\prime}$ the induced morphism, then we have

$f^{\prime}_{*}\omega_{X^{\prime}/Y^{\prime}}^{\otimes m}\simeq f_{1*}\mathcal{O}_{X_{1}}(mK_{X_{1}/Y^{\prime}}).$

Step 2. The morphism $f_{1}$ has general fiber of general type by assumption; according to the BCHM theorem, it admits a relative canonical model $f^{{}^{\prime\prime}}:X^{{}^{\prime\prime}}\to Y^{{}^{\prime\prime}}$. Again by birationality and the Gorenstein canonical singularities property, we have

$f^{{}^{\prime\prime}}_{*}\mathcal{O}_{X^{{}^{\prime\prime}}}(mK_{X^{{}^{\prime\prime}}/Y^{{}^{\prime\prime}}})\simeq f_{1*}\mathcal{O}_{X_{1}}(mK_{X_{1}/Y^{\prime}}).$

Note that $f^{{}^{\prime\prime}}$ continues to be a flat morphism; its fibers have ample canonical bundle. Thus we have reduced to the hypothesis of Theorem 18.1. From that result it follows that $\det f^{\prime}_{*}\omega_{X^{\prime}/Y^{\prime}}^{\otimes m}$ is a big and nef line bundle. Just as at the end of the proof of Proposition 16.2, we deduce that $\det f_{*}\omega_{X/Y}^{\otimes m}$ is big as well.

## References

- [Be] A. Beauville, Complex algebraic surfaces 26
- [EV] H. Esnault and E. Viehweg, Lectures on vanishing theorems, Birkhäuser, Basel, 1992.
- [Fuj] O. Fujino, Subadditivity of the logarithmic Kodaira dimension for morphisms of relative dimension one revisited, available at https://www.math.kyoto-u.ac.jp/ˇ fujino/papersandpreprints.html
- [Fu] W. Fulton, Intersection theory, 2nd edition, Springer-Verlag, Berlin, 1998.
- [Ha] R. Hartshorne, Algebraic geometry, Springer-Verlag, 1977.
- [Ko] J. Kollár, Rational curves on algebraic varieties, Springer-Verlag, Berlin, 1996.
- [La] R. Lazarsfeld, Positivity in algebraic geometry I & II, Springer-Verlag, Berlin, 2004.
- [