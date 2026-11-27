# Embeddings, overlattices, and gluing {#sec-embeddings-overlattices}


Throughout, $S$, $T$, and $L$ denote nondegenerate integral lattices. The notation $A_L$ always denotes the bilinear discriminant form of @def:discriminant; when $L$ is even, $A_{L,q}$ denotes its quadratic discriminant refinement.

## Primitive and saturated sublattices

::: {.definition #def:saturation title="Saturation" defines="saturation; saturated; $\Sat_L(\iota)$"}

Let $\iota\colon S\injects L$ be a morphism of lattices, let
$\iota_\QQ\colon S_\QQ\injects L_\QQ$ be its base change (@def:module-base-change) along $\ZZ\to\QQ$, and let
$j_L\colon L\to L_\QQ$ be the canonical map.
The **saturation** of $\iota$ is the pullback (@def:pullback-square) in $\ZZ\text{-}\mathbf{Mod}$

```tikzcd
\Sat_L(\iota) \arrow[r] \arrow[d] & S_\QQ \arrow[d,"\iota_\QQ"] \\
L \arrow[r,"j_L"'] & L_\QQ
```

The maps $S\to S_\QQ$ and $\iota\colon S\to L$ induce a canonical morphism
$S\to\Sat_L(\iota)$.
The embedding $\iota$ is **saturated** when this morphism is an isomorphism (@def:isomorphism-of-objects).
:::

::: {.proposition #prop:primitive-characterization title="Characterization of primitive embeddings"}

Let $\iota\colon S\injects L$ be a morphism of lattices, and let
$$
0\too S\xrightarrow{\iota}L\xrightarrow{q}Q_\iota\too0
$$
be its cokernel (@def:kernel-cokernel) sequence.
The following conditions are equivalent.

1. $Q_\iota$ is torsion-free (@def:module-subcategories).

2. The canonical comparison $S\to\Sat_L(\iota)$ of @def:saturation is an isomorphism (@def:isomorphism-of-objects).

3. There exists a $\ZZ$-linear retraction $r\colon L\to S$ with $r\circ\iota=\id_S$.

4. Every $\ZZ$-basis (@def:based-module) of $S$ extends along $\iota$ to a $\ZZ$-basis of $L$.

5. The restriction morphism $\iota^\vee\colon\Hom_\ZZ(L,\ZZ)\twoheadrightarrow\Hom_\ZZ(S,\ZZ)$ is an epimorphism in $\bZ\text{-}\mathbf{Mod}$.

6. The canonical morphism $S\to(S^{\perp L})^{\perp L}$ is an isomorphism.

A morphism satisfying these conditions is a **primitive embedding** (@def:primitive-embedding).
:::

::: {.proof}

Tensor the cokernel sequence with $\QQ$.
The universal property of @def:saturation gives
$\Sat_L(\iota)\isoto\ker\qty{L\too L_\QQ\too(Q_\iota)_\QQ}$.
The induced sequence
$$
0\too S\too\Sat_L(\iota)
\too\ker\qty{Q_\iota\to(Q_\iota)_\QQ}
\too0
$$
is exact (@def:exact-complex).
The last term is the torsion subgroup of the finitely generated (@def:module-subcategories) $\ZZ$-module $Q_\iota$, proving $(1)\Longleftrightarrow(2)$.

A finitely generated torsion-free $\ZZ$-module is free.
Hence $(1)$ implies that the cokernel sequence splits, producing the retraction in $(3)$.
Conversely, a retraction gives $L\cong S\oplus\ker r$, so $Q_\iota\cong\ker r$ is free.
Thus $(1)\Longleftrightarrow(3)$.

A splitting $L\cong S\oplus\ker r$ extends every basis of $S$ to a basis of $L$, so $(3)\Longrightarrow(4)$.
Condition $(4)$ implies $(5)$ by extending the values of a functional on an extended basis.
For $(5)\Longrightarrow(1)$, the Smith normal form of $\iota$ shows that a nonzero torsion invariant factor in $Q_\iota$ would obstruct surjectivity of $\iota^\vee$.
Hence $Q_\iota$ is torsion-free.

Over $\QQ$, nondegeneracy gives
$\qty{(S_\QQ)^{\perp L_\QQ}}^{\perp L_\QQ}=S_\QQ$.
Pulling this identity back along $L\to L_\QQ$ gives the canonical isomorphism
$(S^{\perp L})^{\perp L}\isoto\Sat_L(\iota)$.
Hence $(2)\Longleftrightarrow(6)$.
:::

## Primitive-embedding groupoid and orbit sets

::: {.definition #def:coble-embedding-equivalence title="The groupoid of primitive embeddings" defines="groupoid of primitive embeddings; $\mathbf{PrimEmb}_S$; $\Emb(S,L)$; fixed-target isomorphism classes; primitive-subobject orbit set"}

Fix a lattice $S$.
Let $\mathbf{PrimEmb}_S$ be the core (@def:core) of the full subcategory (@def:subcategory) of the undercategory
$S/\mathbf{Lat}_\ZZ$ on primitive (@def:primitive-embedding) morphisms.
Thus its objects are primitive embeddings (@def:primitive-embedding) $\iota\colon S\injects M$, and a morphism
from $\iota_1\colon S\injects M_1$ to $\iota_2\colon S\injects M_2$ is an isometry
$\varphi\colon M_1\isoto M_2$ for which the triangle
```tikzcd
& S \arrow[dl,"\iota_1"'] \arrow[dr,"\iota_2"] & \\
M_1 \arrow[rr,"\varphi"'] && M_2
```
commutes.

For a fixed target (@def:globular-boundary) $L$, write
$\Emb(S,L)\definedas\operatorname{PrimEmb}(S,L)$ for the set of primitive embedding morphisms.
Postcomposition by $\Orth(L)$ gives the fixed-target isomorphism (@def:isomorphism-of-objects) classes
$\Orth(L)\backslash\Emb(S,L)$.
The commuting right action of $\Orth(S)$ gives the primitive-subobject (@def:subobject-relation) orbit (@def:group-orbit) set
$\Orth(L)\backslash\Emb(S,L)/\Orth(S)$.

Nikulin's primitive-embedding classification [@Nik80 Prop. 1.15.1] classifies the
fixed-source isomorphism classes $\Orth(L)\backslash\Emb(S,L)$ by the corresponding
gluing data (@cons:embedding-gluing-data); passing to primitive subobjects introduces the additional right
$\Orth(S)$-action.
:::

## Overlattices and gluing

::: {.definition #def:overlattice title="Overlattices and their discriminant subobjects" defines="overlattice; $H_\iota$"}

An **overlattice** of a lattice $S$ is a lattice morphism
$\iota\colon S\injects L$ whose cokernel (@def:kernel-cokernel) $H_\iota$ is finite length, with exact (@def:exact-complex) sequence
$$
0\too S\xrightarrow{\iota}L\xrightarrow{c_\iota}H_\iota\too0.
$$
Since $\iota_\QQ\colon S_\QQ\isoto L_\QQ$, its inverse induces
$\lambda_\iota\colon L\injects S^\#$ with $\lambda_\iota\circ\iota=\iota_S$.
Functoriality of the bilinear cokernel gives
$\bar{\lambda}_\iota\colon(H_\iota,0)\injects A_S$.
If $S$ is even (@def:form-axioms), $L$ is even exactly when this refines to
$\bar{\lambda}_{\iota,q}\colon(H_\iota,0)\injects A_{S,q}$.
:::

::: {.theorem #thm:nikulin-gluing title="Nikulin's gluing correspondence"}

Let $S$ be an even (@def:form-axioms) lattice.
Let $\operatorname{Over}^{\mathrm{ev}}(S)$ be the poset (@def:preorder-category) of even overlattice (@def:overlattice) morphisms $S\injects L$, ordered by morphisms over $S$.
Let $\operatorname{IsoSub}(A_{S,q})$ be the poset of isotropic (@def:orthogonal-complement) quadratic subobjects (@def:subobject-relation)
$h_q\colon(H,0)\injects A_{S,q}$, ordered by factorization.
Then
$$
\operatorname{Over}^{\mathrm{ev}}(S)
\isoto
\operatorname{IsoSub}(A_{S,q})
$$
as posets [@Nik80, §1.4].

For $h_q$ with bilinear monomorphism $h\colon H\injects A_S^\sharp$, let
$\pi_S\colon S^\#\twoheadrightarrow A_S^\sharp$ be the cokernel (@def:kernel-cokernel) morphism.
The corresponding overlattice is the pullback (@def:pullback-square) in $\bZ\text{-}\mathbf{Mod}$
```tikzcd
L_h \arrow[r] \arrow[d] & S^\# \arrow[d,"\pi_S"] \\
H \arrow[r,hook,"h"'] & A_S^\sharp .
```
It fits into
$$
0\too S\too L_h\too H\too0.
$$

Let
$$
\kappa_h\colon
H^{\perp_{A_S}}
\injects
A_S
$$
be the right orthogonal-complement kernel (@def:kernel-cokernel) of the underlying isotropic bilinear subobject $h\colon(H,0)\injects A_S$.
Since $h$ is isotropic, the universal property of the orthogonal-complement kernel gives the unique monomorphism
$$
\lambda_h\colon(H,0)\injects H^{\perp_{A_S}},
\qquad
\kappa_h\circ\lambda_h=h.
$$
Then
$$
A_{L_h}
\isoto
\coker_{\mathbf{BilMod}_{\bZ}}(\lambda_h),
$$
while $A_{L_h,q}$ is the corresponding quadratic cokernel of the induced isotropic quadratic subobject.
Moreover,
$$
[L_h:S]=\cardinality{H},
\qquad
\disc{L_h}=\frac{\disc{S}}{\cardinality{H}^2}.
$$
The natural $\Orth(S)$-actions on the two posets are intertwined by this correspondence.
:::

::: {.proof}

For an overlattice $\iota\colon S\injects L$, the morphism $\bar{\lambda}_\iota\colon H_\iota\injects A_S$ is isotropic precisely because the rational extension of the form on $S$ restricts to an even integral form on $L$.
If $S\xrightarrow{\iota_1}L_1\xrightarrow{f}L_2$ is a morphism of overlattices, functoriality of cokernels gives the unique morphism
$\bar{f}\colon H_{\iota_1}\too H_{\iota_2}$ satisfying
$\bar{\lambda}_{\iota_2}\circ\bar{f}=\bar{\lambda}_{\iota_1}$.
Thus the construction is order-preserving.

Conversely, the displayed pullback defining $L_h$ has kernel $S$ and cokernel $H$.
Isotropy of $h$ is exactly the condition that the rational extension of the form on $S$ restrict to an even integral form on $L_h$.
The two constructions are inverse by the universal properties of the cokernel and pullback.

The bilinear discriminant object is therefore the cokernel sequence
$$
0
\too
(H,0)
\xrightarrow{\lambda_h}
H^{\perp_{A_S}}
\too
A_{L_h}
\too
0
$$
in $\mathbf{BilMod}_{\bZ}$.
The index (@def:index) equality follows from the exact (@def:exact-complex) sequence
$$
0\to S\to L_h\to H\to0,
$$
and
$\abs{\disc{S}}=[L_h:S]^2\abs{\disc{L_h}}$.
Equivariance under $\Orth(S)$ follows from functoriality of $S\mapsto(S^\#,A_S,q_S)$.
:::

::: {.construction #cons:embedding-gluing-data title="Gluing data of a primitive embedding" defines="gluing data; $h_{S,q}$; $h_{T,q}$; $\gamma_q$"}

Let $\iota_S\colon S\injects L$ be a primitive embedding (@def:primitive-embedding) of even (@def:form-axioms) lattices with $L$ even, and let
$\iota_T\colon T\injects L$ represent its orthogonal complement.
Then $j\definedas\iota_S\perp\iota_T\colon S\perp T\injects L$ is an even overlattice (@def:overlattice), with cokernel (@def:kernel-cokernel) sequence
$$
0\too S\perp T\xrightarrow{j}L\too H_j\too0.
$$
Let $h_{j,q}\colon(H_j,0)\injects A_{S,q}\perp A_{T,q}$ be its isotropic (@def:orthogonal-complement) quadratic subobject (@def:subobject-relation) from @thm:nikulin-gluing.

Primitivity implies that the two projections of $h_{j,q}$ are monomorphisms.
Write the induced quadratic subobjects as
$$
h_{S,q}\colon H_{S,q}\injects A_{S,q},
\qquad
h_{T,q}\colon H_{T,q}\injects A_{T,q}.
$$
Then there is a unique isometry $\gamma_q\colon H_{S,q}\isoto H_{T,q}(-1)$ whose graph is $h_{j,q}$.
Thus the gluing construction attached to $\iota$ is $(h_{S,q},h_{T,q},\gamma_q)$.

The index (@def:index)/discriminant relation gives
$$
\abs{\disc{T}}
=
\frac{\abs{\disc{L}}\,\cardinality{H_j}^2}{\abs{\disc{S}}}.
$$
If $L$ is unimodular, the two projections are isomorphisms (@def:isomorphism-of-objects) and $A_{S,q}\isoto A_{T,q}(-1)$.
This is the primitive-embedding gluing construction of [@Nik80, §1.4--1.5].
:::

## Splitting of unimodular sublattices

::: {.definition #def:lattice-split title="Orthogonal splitting" defines="orthogonal splitting"}

Let $\iota_S\colon S\injects L$ be a primitive embedding (@def:primitive-embedding), and let
$\iota_T\colon T\injects L$ represent its orthogonal-complement subobject (@def:subobject-relation).
The pair induces the orthogonal-sum morphism
$$
j_{\iota_S}\colon S\oplus T\too L,
\qquad
(s,t)\longmapsto\iota_S(s)+\iota_T(t).
$$
The embedding $\iota$ **splits (@def:lattice-split)** when $j_\iota$ is an isomorphism (@def:isomorphism-of-objects).
:::

::: {.proposition #prop:unimodular-splits title="Unimodular sublattices split"}

Let $\iota\colon S\injects L$ be a primitive embedding (@def:primitive-embedding) with $S$ unimodular and $L$ nondegenerate (@def:polarization).
Then the orthogonal-sum morphism of @def:lattice-split is an isometry
$j_\iota\colon S\oplus S^{\perp L}\isoto L$.
If $L$ is unimodular, then $S^{\perp L}$ is unimodular.
:::

::: {.proof}

Let $\beta_S^\sharp\colon S\isoto S^\vee$ be the adjoint (@def:adjoint-morphism) isomorphism (@def:isomorphism-of-objects) of the unimodular lattice (@def:unimodular) $S$, and let
$\iota^\vee\colon L^\vee\to S^\vee$ be restriction along $\iota$.
Define
$$
r\definedas
(\beta_S^\sharp)^{-1}
\circ\iota^\vee
\circ\beta_L^\sharp
\colon L\too S.
$$
Since $\iota$ preserves the bilinear forms, $r\circ\iota=\id_S$.
Moreover, $\ker r$ is exactly the orthogonal-complement subobject (@def:subobject-relation) $S^{\perp L}\injects L$.
Hence
$$
0\too S^{\perp L}\too L\xrightarrow{r}S\too0
$$
is split by $\iota$, and
$j_\iota\colon S\oplus S^{\perp L}\isoto L$ is an isometry.

If $L$ is unimodular, additivity of the discriminant functor gives
$A_L\isoto A_S\perp A_{S^{\perp L}}$.
Since $A_L=0=A_S$, one has $A_{S^{\perp L}}=0$.
Thus $S^{\perp L}$ is unimodular.
:::

::: {.lemma #lem:unimodular-divisibility title="Divisibility of isotropic vectors in unimodular lattices"}

Let $L$ be a nondegenerate (@def:polarization) unimodular lattice (@def:unimodular) and let $v\in L$ be a primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) vector.
Then there exists $w\in L$ with $\beta_L(v, w) = 1$.
In particular $\divisibility_L(v) = 1$ for every primitive vector $v\in L$.
:::

::: {.proof}

Since $L$ is unimodular, the canonical map $L\to \dualof{L}$ is an isomorphism (@def:isomorphism-of-objects), so every functional in $\dualof{L} = \Hom_\ZZ(L, \ZZ)$ has the form $\beta_L(u,\,\cdot\,)$ for a unique $u\in L$.
Because $v$ is primitive, by the primitive-sublattice characterization (@prop:primitive-characterization) it extends to a $\ZZ$-basis $e_1 = v, e_2,\ldots,e_n$ of $L$.
Let $\varphi\colon L\to\ZZ$ be the dual-basis functional with $\varphi(v) = 1$ and $\varphi(e_j) = 0$ for $j > 1$.
Writing $\varphi = \beta_L(w,\,\cdot\,)$ for the corresponding $w\in L$ and using symmetry gives $\beta_L(v, w) = \beta_L(w, v) = \varphi(v) = 1$.
For the divisibility (@def:lattice-divisibility) statement, the image $\beta_L(v, L) = \divisibility_L(v)\ZZ$ contains $\beta_L(v, w) = 1$, so $\divisibility_L(v) = 1$.
:::

::: {.corollary #cor:hyperbolic-splitting title="Hyperbolic splitting of unimodular lattices"}

Let $L$ be a nondegenerate (@def:polarization) unimodular lattice (@def:unimodular) containing a primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) vector.
Then $L$ splits (@def:hyperbolic-plane) off a rank-$2$ unimodular hyperbolic plane (@def:hyperbolic-plane):
$$
L \cong P\oplus P^{\perp L},
\qquad
P \cong
\begin{cases}
U, & L \text{ even},\\
\latI_{1, 1}, & L \text{ odd}.
\end{cases}
$$
:::

::: {.proof}

Let $e\in L$ be a primitive isotropic vector (@def:isotropic-subspace).
By @lem:unimodular-divisibility choose $w\in L$ with $\beta_L(e, w) = 1$, and set $k\definedas w^2$.
The sublattice $P\definedas\generators{e, w}$ has Gram matrix $\begin{bmatrix}0 & 1\\ 1 & k\end{bmatrix}$ of determinant $-1$, hence $P$ is a rank-$2$ unimodular sublattice, and it is primitive since a unimodular sublattice is saturated by the primitive-sublattice characterization (@prop:primitive-characterization).
The isometry type of $P$ is governed by the parity of $k = w^2$: the Gram matrix $\begin{bmatrix}0 & 1\\ 1 & k\end{bmatrix}$ gives $P\cong U$ when $k$ is even and $P\cong\latI_{1, 1}$ (the odd rank-$2$ unimodular hyperbolic lattice (@not:reflection-groups-sign-convention)) when $k$ is odd.
We adjust $w$ within its coset to realize the parity dictated by $L$; note that adding to $w$ any vector of $\generators{e}^{\perp L}$ preserves $\beta_L(e, w) = 1$.

If $L$ is even (@def:form-axioms) then $k = w^2$ is even; replacing $w$ by $w - \tfrac{k}{2}e$ (and $e\in\generators{e}^{\perp L}$ since $e^2 = 0$) leaves $\beta_L(e, w) = 1$ unchanged and makes $w^2 = 0$, so $P\cong U$.

If $L$ is odd we arrange $w^2$ to be odd, so that $P\cong\latI_{1, 1}$.
Every $x\in L$ satisfies $x - \beta_L(e, x)\,w\in\generators{e}^{\perp L}$, so $L = \generators{e}^{\perp L} + \ZZ w$.
Were $\generators{e}^{\perp L}$ to consist entirely of even-norm (@def:lattice-basic-invariants) vectors and $w^2$ even, every $x = y + mw$ ($y\in\generators{e}^{\perp L}$) would have $x^2 = y^2 + 2m\,\beta_L(y, w) + m^2 w^2$ even, forcing $L$ even --- contrary to hypothesis.
Hence either $w^2$ is already odd, or $\generators{e}^{\perp L}$ contains a vector $u$ of odd norm; in the latter case replace $w$ by $w + u$, which preserves $\beta_L(e, w) = 1$ and gives $(w + u)^2 = w^2 + 2\beta_L(w, u) + u^2$ odd.
Either way $k = w^2$ is odd and $P\cong\latI_{1, 1}$.

Since $P$ is unimodular, @prop:unimodular-splits gives $L\cong P\oplus P^{\perp L}$.
:::

## Maximal and split maximal lattices

::: {.definition #def:maximal-lattice title="Maximal lattices" defines="maximal lattice; maximal overlattice"}

An even (@def:form-axioms) lattice $L'$ is **maximal** if $A_{L',q}$ has no nonzero isotropic (@def:orthogonal-complement) quadratic subobject (@def:subobject-relation)
$(H,0)\injects A_{L',q}$.
A maximal overlattice (@def:overlattice) of $L$ is an even overlattice morphism
$\iota\colon L\injects L'$ whose target (@def:globular-boundary) is maximal.
:::

::: {.lemma #lem:maximal-overlattice-exists}

Every even (@def:form-axioms) lattice admits a maximal (@def:maximal-lattice) overlattice (@def:overlattice).
A unimodular lattice (@def:unimodular) is maximal.
:::

::: {.proof}

By @thm:nikulin-gluing,
$$
\operatorname{Over}^{\mathrm{ev}}(L)
\isoto
\operatorname{IsoSub}(A_{L,q})
$$
as posets (@def:preorder-category), with overlattices ordered by morphisms over $L$ and isotropic (@def:orthogonal-complement) quadratic subobjects (@def:subobject-relation) ordered by factorization.
The discriminant module $A_L^\sharp$ has finite length, so $\operatorname{IsoSub}(A_{L,q})$ is a finite poset and has a maximal element.
Its corresponding even overlattice admits no proper even overlattice, hence is maximal.
For a unimodular lattice $A_{L,q}=0$, so the zero subobject is maximal.
:::

::: {.definition #def:split-maximal title="Maximal lattices with two hyperbolic summands" defines="split maximal; $U^{\oplus2}$-decomposable"}

A maximal (@def:maximal-lattice) lattice $L'$ of signature (@def:signature) $(2,n)$ is **$U^{\oplus2}$-decomposable** if
$U^{\oplus2}\oplus L_0\isoto L'$ for some lattice $L_0$.
Dawes uses the term *split maximal* for this decomposition hypothesis [@Daw22 §3.1].
:::

::: {.theorem #thm:maximal-splits-for-large-n title="Maximal lattices of signature $(2,n)$ are $U^{\oplus2}$-decomposable for $n\geq5$"}

Every maximal (@def:maximal-lattice) lattice of signature (@def:signature) $(2,n)$ with $n\geq5$ is $U^{\oplus2}$-decomposable.
:::

::: {.proof}

This is the decomposition result recorded in [@Daw22 §3.1], where it is attributed to
Attwell-Duval; for smaller $n$, see also [@Nik80 Cor. 1.13.5].
:::

::: {.theorem #thm:split-maximal-isotropic-transitivity title="Isotropic transitivity for an even maximal $U^{\oplus2}$-decomposable lattice"}

Let $L'$ be an *even* (@def:form-axioms) maximal (@def:maximal-lattice) $U^{\oplus2}$-decomposable lattice of signature (@def:signature) $(2,n)$.

1. For any $x,y\in L'^{\mathrm{prim}}[0]$ there exists
   $\tau(x,y)\in\Orth^+(L')$ with $\tau(x,y)x=y$; hence $\Orth^+(L')$ acts
   transitively on $L'^{\mathrm{prim}}[0]$.

2. Two primitive (@def:primitive-embedding) totally isotropic (@def:orthogonal-complement) embeddings
   $\iota_i\colon E_i\injects L'$ lie in the same $\Orth^+(L')$-orbit if and only if
   $E_1^{\perp L'}/E_1\cong E_2^{\perp L'}/E_2$.
:::

::: {.proof}

Both statements are in [@Daw22 §3.1]: Algorithm 3.3 constructs $\tau(x,y)$ from the
two displayed hyperbolic (@def:hyperbolic-plane) summands, and the Attwell-Duval criterion gives the second
orbit (@def:group-orbit) statement.
:::

::: {.definition #def:characteristic-vector title="Characteristic vectors" defines="characteristic vector"}

A vector $c$ of a unimodular lattice (@def:unimodular) $L$ is **characteristic** if $c\cdot x\equiv x^2\pmod 2$ for every
$x\in L$.
:::

::: {.lemma #lem:characteristic-vectors-of-Ipq title="Characteristic vectors of $\latI_{p,q}$"}

Every characteristic vector (@def:characteristic-vector) of $\latI_{p,q}$ has square $\equiv p-q\pmod 8$. Hence, if
$p-q\not\equiv0\pmod 8$, no isotropic (@def:orthogonal-complement) vector of $\latI_{p,q}$ is characteristic.
:::

::: {.proof}

Let $e_1,\dots,e_{p+q}$ be the standard orthogonal basis (@def:based-module), with $e_i^2=1$ for $i\leq p$ and $e_i^2=-1$ for
$i>p$, and let $c=\sum_ic_ie_i$ be characteristic. For $x=e_i$ the condition reads $\pm c_i\equiv\pm1\pmod 2$,
so every $c_i$ is odd and $c_i^2\equiv1\pmod 8$. Hence
$c^2=\sum_{i\leq p}c_i^2-\sum_{i>p}c_i^2\equiv p-q\pmod 8$; this is the case $L=\latI_{p,q}$ of van der
Blij's congruence $c^2\equiv\sigma(L)\pmod 8$ [@Nik80, §1.9]. An isotropic vector (@def:isotropic-subspace) has square $0$, so it is
not characteristic when $p-q\not\equiv0\pmod 8$.
:::

::: {.proposition #prop:odd-unimodular-rank-one-transitivity title="The odd lattice $B = \latI_{2,9}$: primitive isotropic vectors, full orthogonal group"}

$\Orth(\latI_{2,9})$ acts transitively on the primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) vectors of $\latI_{2,9}$.
:::

::: {.proof}

James' integral Witt theorem [@Jam68, Theorem, p. 303]: for $L$ unimodular, an isometry between primitive
sublattices $J$, $K$ with $r(L)-\abs{\fs(L)}\geq2(r(J)+1)$ extends to an isometry of $L$ if and only
if it carries characteristic vectors (@def:characteristic-vector) to characteristic vectors. For $B=\latI_{2,9}$ one has
$r-\abs{\fs}=11-7=4=2(1+1)$, so the inequality holds for a primitive rank-one $J$ with equality, and
it is the only hypothesis besides the characteristic clause. Given two primitive isotropic vectors (@def:isotropic-subspace) $v$,
$w$, the isometry $\langle v\rangle\to\langle w\rangle$, $v\mapsto w$, therefore extends provided
neither line is characteristic. Neither is, by @lem:characteristic-vectors-of-Ipq, since
$2-9=-7\not\equiv0\pmod 8$; so the clause is vacuous and the isometry extends.
:::

::: {.example #ex:I22-two-isotropic-orbits title="Two orbits of primitive isotropic vectors of $\latI_{2,2}$"}

The lattice $\latI_{2,2}$ has $r-\abs{\fs}=4-0=4$, and $2-2\equiv0\pmod 8$. The vectors $c=(1,1,1,1)$ and
$v=(1,0,1,0)$ are primitive and isotropic. The vector $c$ is characteristic, since
$c\cdot x=x_1+x_2-x_3-x_4\equiv x^2\pmod 2$ for every $x$; the vector $v$ is not, since $v\cdot e_2=0$
and $e_2^2=1$. An isometry preserves the characteristic condition, so no isometry carries $c$ to $v$, and
$\Orth(\latI_{2,2})$ is not transitive on primitive isotropic vectors.
:::

::: {.lemma #lem:odd-unimodular-isotropic-splitting title="Splitting an odd unimodular lattice at a primitive isotropic line"}

Let $L$ be an odd unimodular lattice (@def:unimodular) of signature $(p,q)$ and let $l$ be a primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) line of $L$.
Then $L=P\perp M$ with $l\subset P\cong\latI_{1,1}$ and $M$ unimodular of signature $(p-1,q-1)$, and
$l^{\perp L}=l\perp M$, so $l^{\perp L}/l\cong M$. Moreover:

1. if $L=\latI_{2,9}$, then $M\cong\latI_{1,8}$;
2. if $L=\latI_{1,8}$, then $M\cong\latI_{0,7}$.
:::

::: {.proof}

By @cor:hyperbolic-splitting, $L$ being odd, $L=P\perp M$ with $l\subset P\cong\latI_{1,1}$, and $M$ is
unimodular of signature $(p-1,q-1)$ because $P$ is unimodular of signature $(1,1)$. Let $e,f$ be an
orthogonal basis (@def:based-module) of $P$ with $e^2=1$, $f^2=-1$. The primitive isotropic vectors (@def:isotropic-subspace) of $P$ are $\pm(e\pm f)$,
so after replacing $f$ by $-f$ one has $l=\ZZ(e+f)$. An element $ae+bf+m$ with $m\in M$ is orthogonal to
$l$ exactly when $a=b$, so $l^{\perp L}=l\perp M$.

(1) An even (@def:form-axioms) unimodular lattice has signature $\equiv0\pmod 8$, and $1-8\not\equiv0\pmod 8$, so $M$ is odd
and indefinite (@def:definiteness) of signature $(1,8)$, and $M\cong\latI_{1,8}$ by @thm:indefinite-unimodular-classification.

(2) An even unimodular definite (@def:definiteness) lattice has rank divisible by $8$, so $M$, of rank $7$, is odd. The odd
definite unimodular lattice of rank $7$ is unique by @thm:definite-unimodular-class-numbers and the first
row of @tbl-unimodular-definite-class-numbers, for the negative-definite sign by the sign twist (@def:sign-twist-equivalence) that theorem
records. So $M\cong\latI_{0,7}$.
:::

::: {.lemma #lem:odd-rank-scaled-unimodular-line-transitivity title="Primitive isotropic lines of odd-rank scaled unimodular lattices"}

Let $B$ be a nondegenerate integral unimodular lattice of odd rank and signature $(p,q)$, with $p,q\geq2$, and let $L=B(d)$ for a positive integer $d$. Then $\Orth(L)$ is transitive on its primitive isotropic vectors, hence on its primitive isotropic lines. In particular the set of $\Orth(L)$-orbits of primitive isotropic lines has exactly one element.

:::

::: {.proof}

The form of $B$ is odd because an even unimodular integral lattice has even rank (its reduction modulo $2$ is nondegenerate alternating). By the indefinite unimodular classification, $B\cong\latI_{p,q}$ (C. Peters and H. Sterk, [*Symmetric and Quadratic Forms*, Theorem 2.3.1, p. 62](https://www-fourier.univ-grenoble-alpes.fr/~peters/Books/QuadraticForms/QuadForms.pdf)). In particular $B$ has a primitive isotropic vector, the sum of a positive and a negative unit vector. In that diagonal model every characteristic vector has all coordinates odd, and its square is congruent to $p-q$ modulo $8$ by @lem:characteristic-vectors-of-Ipq. Since the rank is odd, $p-q$ is odd; no isotropic vector is characteristic.

For an arbitrary primitive isotropic $v$, choose $w$ with $(v,w)=1$ using unimodularity. If $w^2$ is odd, there is an element $z\in v^\perp$ of odd square: otherwise, writing every $x\in B$ as $(v,x)w+z_x$ with $z_x\in v^\perp$ gives $x^2\equiv (v,x)\pmod 2$ and makes $v$ characteristic. Replace $w$ by $w+z$ in this case, so in either case $w$ has even square and $(v,w)=1$. Then $f=w-(w^2/2)v$ satisfies $f^2=0$, $(v,f)=1$. The span $\ZZ v+\ZZ f$ is unimodular, hence splits off orthogonally. Its complement is unimodular of signature $(p-1,q-1)$, of odd rank, hence odd and indefinite. Again the indefinite unimodular classification identifies the complement with $\latI_{p-1,q-1}$. For two primitive isotropic vectors choose these splittings; mapping the marked hyperbolic bases and any isometry between the two complements gives an integral isometry carrying the first vector to the second.

Scaling the form by $d$ does not change its integral orthogonal group, primitive vectors, or isotropic vectors, so the result follows for $L$. This argument does not classify characteristic isotropic vectors in even rank, or definite complements when one signature index is one. It proves the ambient orbit assertion independently of any discriminant-image or stabilizer-image computation.

:::

::: {.proposition #prop:rank-nine-line-transitivity title="Primitive isotropic lines of $\latI_{1,8}$ and of its twist"}

Let $L$ be $\latI_{1,8}$ or its twist $\latI_{1,8}(2)$, of rank $9$ and signature $(1,8)$. Then $\Orth(L)$
and $\Orth^+(L)$ both act transitively on the primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) **lines** of $L$.
:::

::: {.proof}

Twisting by $2$ preserves the module, the isometry group (@def:group) as a subgroup of $\GL_9(\ZZ)$ and isotropy, so it
suffices to treat $L=\latI_{1,8}$.

Let $\ZZ v$ and $\ZZ v'$ be primitive isotropic lines. By @lem:odd-unimodular-isotropic-splitting(2),
$L=P\perp M=P'\perp M'$ with $v\in P$, $v'\in P'$, $P\cong P'\cong\latI_{1,1}$ and $M\cong M'\cong\latI_{0,7}$,
and $v=\pm(e+f)$, $v'=\pm(e'+f')$ in orthogonal bases of $P$ and $P'$ as there. The isometry $P\to P'$ with
$e\mapsto e'$, $f\mapsto f'$ and an isometry $M\to M'$ together give $g\in\Orth(L)$ with $g(\ZZ v)=\ZZ v'$.
So $\Orth(L)$ is transitive on lines.

By @lem:minus-identity-spinor-norm, $-\id_L\notin\Orth^+(L)$, since the positive index (@def:maximal-positive-definite-subspace) is $1$, and
$\Orth^+(L)$ has index (@def:index) $2$ in $\Orth(L)$. Hence for $g$ carrying $\ZZ v$ to $\ZZ v'$, either $g$ or $-g$ lies
in $\Orth^+(L)$, and $-g$ also carries $\ZZ v$ to $\ZZ v'$. So $\Orth^+(L)$ is transitive on lines too.
:::

::: {.proposition #prop:rank-nine-vector-transitivity title="Primitive isotropic vectors of $\latI_{1,8}$ and of its twist"}

Let $L$ be $\latI_{1,8}$ or $\latI_{1,8}(2)$, of signature $(1,8)$, and fix a component $C^+$ of the positive cone (@not:reflection-groups-sign-convention) $\theset{x\in L\otimes\bR\st x^2>0}$.
For a primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) $v\in L$ the sign of $\beta_\bR(v,e)$ is independent of the choice of $e\in C^+$, because $\beta_\bR(v,-)$ has no zero on $C^+$ --- a zero would put the isotropic $v$ in the negative definite (@def:definiteness) hyperplane $e^{\perp}$ --- and $C^+$ is connected; call that sign the **side** of $v$.
Then

1. $\Orth(L)$ acts transitively on the primitive isotropic vectors (@def:isotropic-subspace) of $L$;

2. $\Orth^+(L)$ has exactly two orbits (@def:group-orbit) on them, the vectors of side $+1$ and the vectors of side $-1$; $-\id_L$ lies in $\Orth(L)\setminus\Orth^+(L)$ and exchanges the two;

3. every $g\in\Orth(L)$ carrying a vector of side $+1$ to a vector of side $+1$ lies in $\Orth^+(L)$.

:::

::: {.proof}

Twisting by $2$ preserves the module, the isometry group (@def:group) as a subgroup of $\GL_9(\bZ)$ and isotropy, as in @prop:rank-nine-line-transitivity, so it suffices to treat $L=\latI_{1,8}$.

(1) By @prop:rank-nine-line-transitivity there is $g\in\Orth(L)$ with $g(\bZ v)=\bZ v'$, that is $g(v)=\pm v'$; composing with $-\id_L$, which lies in $\Orth(L)$, gives the sign.

(2) By @lem:minus-identity-spinor-norm, $\spinornorm_\bR(-\id_L)=[(-1)^1]=-1$ because the positive index (@def:maximal-positive-definite-subspace) is $1$, so $-\id_L\notin\Orth^+(L)$ and $\Orth(L)=\Orth^+(L)\cup(-\id_L)\Orth^+(L)$.
Hence $\Orth(L)\cdot v=\Orth^+(L)\cdot v\cup\Orth^+(L)\cdot(-v)$, and by (1) there are at most two $\Orth^+(L)$-orbits.
There are at least two: $\Orth^+(L)$ preserves each component of $C^+$ by @prop:spinor-plus-cone-components, so for $g\in\Orth^+(L)$ and $e\in C^+$ one has $ge\in C^+$ and
$$
\operatorname{sign}\beta_\bR(gv,e)=\operatorname{sign}\beta_\bR(v,g^{-1}e)=\operatorname{sign}\beta_\bR(v,e),
$$
the middle step by invariance of $\beta_\bR$ and the last by $g^{-1}e\in C^+$; so the side is constant on an $\Orth^+(L)$-orbit, while $\operatorname{side}(-v)=-\operatorname{side}(v)$.
So the two orbits are the two sides.

(3) Let $g\in\Orth(L)$ with $\operatorname{side}(gv)=\operatorname{side}(v)$. If $g$ exchanged the components of $C(L)$ then $ge\in-C^+$ for $e\in C^+$, and $\beta_\bR(gv,ge)=\beta_\bR(v,e)$ together with $\operatorname{sign}\beta_\bR(gv,-C^+)=-\operatorname{side}(gv)$ would give $-\operatorname{side}(gv)=\operatorname{side}(v)$, contradicting the hypothesis. So $g$ preserves the components, that is $g\in\Orth^+(L)$ by @prop:spinor-plus-cone-components.
:::

::: {.lemma #lem:split-isometry-spinor-norm title="Spinor norm of an isometry fixing a summand"}

Let $B=P\perp M$ be an orthogonal splitting (@def:lattice-split) of a nondegenerate (@def:polarization) lattice and let $\varphi\in\Orth(M)$. Then
$\spinornorm_\bR(\id_P\perp\varphi)=\spinornorm_\bR(\varphi)$, so $\id_P\perp\varphi\in\Orth^+(B)$ exactly
when $\varphi\in\Orth^+(M)$.
:::

::: {.proof}

By the Cartan--Dieudonné theorem write $\varphi\otimes\bR=s_{u_1}\cdots s_{u_k}$ with anisotropic
$u_i\in M\otimes\bR$. Each reflection $s_{u_i}$ of $B\otimes\bR$ fixes $P\otimes\bR$ pointwise and restricts
to the reflection $s_{u_i}$ of $M\otimes\bR$, so $\id_P\perp\varphi=s_{u_1}\cdots s_{u_k}$ in
$\Orth(B\otimes\bR)$, and the two spinor norms (@def:lattice-basic-invariants) agree by @def:spinor-norm. The group (@def:group) $\Orth^+$ is the kernel (@def:kernel-cokernel)
of the real spinor norm.
:::

::: {.lemma #lem:I29-plus-line-transitivity title="$\Orth^+(\latI_{2,9})$ on primitive isotropic lines and vectors"}

$\Orth^+(\latI_{2,9})$ acts transitively on the primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) lines and on the primitive isotropic
vectors of $\latI_{2,9}$.
:::

::: {.proof}

Let $B=\latI_{2,9}$ and let $l,l'$ be primitive isotropic lines. By
@lem:odd-unimodular-isotropic-splitting(1), $B=P\perp M=P'\perp M'$ with $l=\ZZ(e+f)\subset P$,
$l'=\ZZ(e'+f')\subset P'$ and $M\cong M'\cong\latI_{1,8}$. The isometry $\psi\colon P\to P'$ with
$e\mapsto e'$, $f\mapsto f'$ and an isometry $\vartheta\colon M\to M'$ give $g=\psi\perp\vartheta\in\Orth(B)$
with $g(l)=l'$. Put $\sigma'=\id_{P'}\perp(-\id_{M'})$. It fixes $l'$, and $\sigma'\notin\Orth^+(B)$ by
@lem:split-isometry-spinor-norm, since $-\id_{M'}\notin\Orth^+(M')$ by @lem:minus-identity-spinor-norm.
As $\Orth^+(B)$ has index (@def:index) $2$ in $\Orth(B)$, one of $g$ and $\sigma'g$ lies in $\Orth^+(B)$ and carries $l$
to $l'$.

For primitive isotropic vectors (@def:isotropic-subspace) $v,v'$, an element $g\in\Orth^+(B)$ with $g(\ZZ v)=\ZZ v'$ has $g(v)=\pm v'$,
and $-\id_B\in\Orth^+(B)$ by @lem:minus-identity-spinor-norm, since the positive index (@def:maximal-positive-definite-subspace) is $2$.
:::

::: {.theorem #thm:plane-transitivity-tco title="Primitive isotropic planes of $T_\Co$"}

$\Orth^+(T_\Co)$ acts transitively on the primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) planes of $T_\Co$.
:::

::: {.proof}

By @prop:tco-as-twist $T_\Co=B(2)$ with $B=\latI_{2,9}$. Twisting by $2$ preserves the module, isometries,
orthogonality and isotropy, so $\Orth^+(T_\Co)=\Orth^+(B)$ as subgroups of $\GL(B)$, and the primitive
isotropic planes of the two lattices are the same set.

Let $J,J'$ be primitive isotropic planes of $B$, and choose primitive isotropic lines $l\subset J$ and
$l'\subset J'$; a primitive vector of a primitive sublattice is primitive in $B$. By
@lem:I29-plus-line-transitivity some $g\in\Orth^+(B)$ carries $l$ to $l'$. Split (@def:hyperbolic-plane) $B=P'\perp M'$ at $l'$ by
@lem:odd-unimodular-isotropic-splitting(1), so $l'^{\perp B}=l'\perp M'$ with $M'\cong\latI_{1,8}$. An
isotropic plane $K\supset l'$ lies in $l'^{\perp B}$, and $K=l'\oplus(K\cap M')$ with $K\cap M'$ a primitive
isotropic line of $M'$, because the $M'$-component of an element of $K$ lies in $K$. Apply this to $K=g(J)$
and $K=J'$. By @prop:rank-nine-line-transitivity some $\varphi\in\Orth^+(M')$ carries $g(J)\cap M'$ to
$J'\cap M'$. Then $\id_{P'}\perp\varphi\in\Orth^+(B)$ by @lem:split-isometry-spinor-norm, it fixes $l'$, and it
carries $g(J)$ to $J'$. So $(\id_{P'}\perp\varphi)\circ g\in\Orth^+(B)$ carries $J$ to $J'$.
:::

::: {.corollary #cor:tco-isotropic-splitting title="Isotropic quotients of $T_\Co$"}

Let $l$ be a primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) line and $J$ a primitive isotropic plane of $T_\Co$. Then
$T_\Co=\latI_{1,1}(2)\perp\latI_{1,8}(2)$ with $l\subset\latI_{1,1}(2)$, and
$$
l^{\perp T_\Co}/l\cong\latI_{1,8}(2),\qquad J^{\perp T_\Co}/J\cong\latI_{0,7}(2).
$$
Moreover $T_\Co\cong U(2)\perp U(2)\perp\latI_{0,7}(2)$.
:::

::: {.proof}

By @prop:tco-as-twist, $T_\Co=B(2)$ with $B=\latI_{2,9}$. Twisting by $2$ preserves the underlying module,
orthogonality and isotropy, so it suffices to prove the untwisted statements for $B$ and twist the result.
The splitting and $l^{\perp B}/l\cong\latI_{1,8}$ are @lem:odd-unimodular-isotropic-splitting(1).

For $J$, choose a primitive isotropic line $l\subset J$ and split (@def:hyperbolic-plane) $B=P\perp M$ at $l$. As in the proof of
@thm:plane-transitivity-tco, $J=l\oplus\ZZ m$ with $\ZZ m$ a primitive isotropic line of
$M\cong\latI_{1,8}$. Then $J^{\perp B}=\theset{x\in l\perp M\st x\cdot m=0}=l\perp m^{\perp M}$, and
$m^{\perp M}=\ZZ m\perp N$ with $N\cong\latI_{0,7}$ by @lem:odd-unimodular-isotropic-splitting(2). Hence
$J^{\perp B}=J\perp N$ and $J^{\perp B}/J\cong\latI_{0,7}$.

The lattice $U\perp U\perp\latI_{0,7}$ is odd, unimodular and indefinite (@def:definiteness) of signature $(2,9)$, so it is
isometric to $B$ by @thm:indefinite-unimodular-classification.
:::

## Finiteness of embedding orbits

::: {.proposition #prop:embedding-finiteness title="Finiteness of primitive-embedding orbits into an even unimodular lattice"}

Let $S$ and $L$ be even lattices (@def:even-lattice) with $L$ unimodular.
Then $\Orth(L)\backslash\Emb(S,L)$ is finite.
:::

::: {.proof}

Fix $\iota\colon S\injects L$ and put $T\definedas S^{\perp L}$.
Unimodularity of $L$ gives an isometry $A_{S,q}\isoto A_{T,q}(-1)$.
The signature (@def:signature) of $T$ together with $A_{T,q}$ is therefore fixed, so $T$ belongs to a fixed genus; that genus contains finitely many integral isometry classes.

For each such $T$, the set $\operatorname{Iso}\qty{A_{S,q},A_{T,q}(-1)}$ is finite because the discriminant modules $A_S^\sharp$ and $A_T^\sharp$ have finite cardinality.
Nikulin's equivalence relation (@def:equivalence-relation) on these gluing data (@cons:embedding-gluing-data) is induced by isometries of the target (@def:globular-boundary) and complement [@Nik80, Prop. 1.15.1].
Hence only finitely many $\Orth(L)$-orbits of primitive embeddings (@def:primitive-embedding) occur.
:::

::: {.proposition #prop:fixed-norm-orbit-finiteness title="Finiteness of fixed-square vector orbits"}

Let $L$ be a nondegenerate integral lattice and let $n\in\bZ$.
There are finitely many $\Orth(L)$-orbits of primitive vectors of square $n$.
If $n\ne0$, there are also finitely many orbits of all vectors of square $n$.
If $L$ contains a nonzero isotropic vector, the set of all vectors of square zero has infinitely many orbits.
:::

::: {.proof}

Use the classical finiteness of integral isometry classes of nondegenerate forms of fixed rank and determinant (for example, *Quantitative Reduction Theory and Unlikely Intersections*, IMRN 2022, [Lemma 2.4](https://academic.oup.com/imrn/article/2022/20/16138/6322312)). The determinant of a rank-zero lattice is taken to be one.

First suppose $v$ is primitive and $v^2=n\ne0$. Write $d>0$ for the positive generator of $(v,L)$ and set $K=v^{\perp_L}$. The homomorphism $(v,-)/d\colon L\to\bZ$ is onto, has kernel $K$, and maps $\bZ v$ onto $(n/d)\bZ$. Therefore
$$
[L:\bZ v\perp K]=|n|/d,\qquad
|\det K|=\frac{|n|}{d^2}|\det L|.
$$
The number of possible $d$ is finite since $d\mid n$. For each $d$ the rank and absolute determinant of $K$ are fixed, so there are finitely many possibilities for its isometry class. Fix one representative $K$ and a generator $e$ of the rank-one lattice $[n]$ of square $n$. Every such marked pair $(L,v)$ arises from an integral overlattice of $M=\bZ e\perp K$ inside $M^\vee$, with $v$ identified with $e$. There are finitely many intermediate lattices since $M^\vee/M$ is finite. Equal intermediate lattices give isometric marked pairs, hence one $\Orth(L)$-orbit when the underlying lattice is $L$.

Now suppose $v$ is primitive and isotropic. The class of $v/d$ in $L^\vee/L$ has order $d$, by primitivity, so $d\mid|\det L|$. Choose $w\in L$ with $(v,w)=d$. The map $(v,-)/d$ exhibits $L=v^\perp\oplus\bZ w$ as abelian groups. The quotient $K=v^\perp/\bZ v$ is free (because $v$ is primitive) and nondegenerate: over $\bQ$, the radical of $v^\perp$ is precisely $\bQ v$. Lifting a basis of $K$ gives an integral basis of $L$ together with $v,w$. In this ordered basis the Gram matrix is
$$
\begin{pmatrix}
0&0&d\\
0&G_K&b\\
d&b^\mathsf{T}&c
\end{pmatrix},
\qquad
\det L=-d^2\det K.
$$
Again there are finitely many $d$ and possible isometry classes of $K$. Choose one basis for each class. Adding multiples of $v$ to its lifted basis vectors changes the entries of $b$ by arbitrary multiples of $d$ without changing $G_K$; replacing $w$ by $w+kv$ changes $c$ by $2kd$ and leaves $b$ unchanged. Thus all marked Gram matrices have representatives with $0\le b_i<d$ and $0\le c<2d$. There are only finitely many such matrices. Equality of two marked Gram matrices gives an integral isometry mapping their first basis vector to the other, proving the primitive assertion.

For nonzero square $n$, each nonprimitive vector is $m v$ with $v$ primitive and $m>0$ satisfying $m^2\mid n$. This is a finite union of images of finite primitive orbit sets. For square zero, choose any nonzero primitive isotropic $v$; the multiples $mv$ for positive integers $m$ have distinct contents in the underlying free abelian group, which are invariant under every integral automorphism. They are therefore in distinct orbits.
:::

The last assertion is essential when interpreting representation-counting
results. Ratcliffe–Tschantz, [*On the Representation of Integers by the
Lorentzian Quadratic Form*](https://doi.org/10.1006/jfan.1997.3129),
counts nonzero-square representations in a Euclidean ball. Lauret,
[*An asymptotic formula for representations of integers by indefinite
hermitian forms*](https://arxiv.org/abs/1109.6697), treats a fixed negative
value for forms of signature $(n,1)$. Gorodnik–Nevo,
[*Counting lattice points*](https://arxiv.org/abs/0903.1515), concerns
quantitative counting in lattice orbits under stated regularity and
ergodic hypotheses. None of these assertions, as stated, removes the
primitive restriction at square zero.

::: {.proposition #prop:scaled-discriminant-ses title="Bilinear discriminant form of a scaled lattice"}

Let $L$ be an integral lattice and let $m>0$.
Define the finite-length value module
$$
W_m(L)
\definedas
\operatorname{im}\!\qty{
L\tensor_\bZ L
\xrightarrow{\ (x,y)\mapsto\beta_L(x,y)/m+\bZ\ }
\bQ/\bZ
},
$$
and define the bilinear module
$$
K_m(L)
\definedas
\qty{
L/mL,
W_m(L),
\kappa_m
},
\qquad
\kappa_m(\bar{x},\bar{y})
=
\frac{\beta_L(x,y)}{m}+\bZ.
$$
Then there is a short exact (@def:exact-complex) sequence in $\mathbf{BilMod}_{\bZ}$
$$
0
\too
K_m(L)
\too
A_{L(m)}
\xrightarrow{F_m}
A_L
\too
0.
$$
If $L$ is unimodular, then $A_{L(m)}\isoto K_m(L)$ and $A_{L(m)}^\sharp\isoto L/mL\isoto(\bZ/m\bZ)^{\rank L}$.
:::

::: {.proof}

The metric dual of the twist (@def:form-twist) is
$$
L(m)^\#
\isoto
\tfrac1mL^\#.
$$
Multiplication by $m$ on $L_\QQ$ induces $U(F_m)\colon A_{L(m)}^\sharp\too A_L^\sharp$, characterized by
$$
U(F_m)\circ\pi_{L(m)}
=
\pi_L\circ[m]_{L_\QQ}.
$$
Together with multiplication by $m$ on the value modules, this defines
$F_m\colon A_{L(m)}\too A_L$ in $\mathbf{BilMod}_{\bZ}$, because
$$
\bar{\beta}_L(mx,my)
=
m\,\bar{\beta}_{L(m)}(x,y).
$$

The forgetful functor gives
$$
U\qty{\ker_{\mathbf{BilMod}_{\bZ}}(F_m)}
\isoto
L/mL,
$$
and the induced pairing is $\kappa_m$ with value submodule $W_m(L)$.
Hence
$$
\ker_{\mathbf{BilMod}_{\bZ}}(F_m)
\isoto
K_m(L),
$$
which gives the displayed short exact sequence (@def:exact-complex).
If $L$ is unimodular, then $A_L=0$, so the exact sequence gives $A_{L(m)}\isoto K_m(L)$.
:::

::: {.definition #def:simultaneous-discriminant-spinor-kernel title="Simultaneous discriminant and spinor kernel" defines="simultaneous discriminant and spinor kernel; $\widetilde\Orth^+(L)$"}
Let $\Orth^+(L)\injects\Orth(L)$ be the spinor kernel of @def:lattice-spinor-kernels. Define $\widetilde\Orth^+(L)$ by the pullback (@def:pullback-square)
```tikzcd
\widetilde\Orth^+(L) \arrow[r] \arrow[d] & \widetilde\Orth(L) \arrow[d] \\
\Orth^+(L) \arrow[r] & \Orth(L).
```
:::
