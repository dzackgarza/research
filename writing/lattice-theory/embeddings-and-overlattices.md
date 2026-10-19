# Embeddings, overlattices, and gluing {#sec:embeddings-overlattices}

Throughout, $S$, $T$, and $L$ denote nondegenerate integral lattices. The notation $A_L$ always denotes the bilinear discriminant form of @def:discriminant; when $L$ is even, $A_{L,q}$ denotes its quadratic discriminant refinement.

## Primitive and saturated sublattices

::: {.definition #def:saturation title="Saturation"}

Let $\iota\colon S\injects L$ be a morphism of lattices, let
$\iota_\QQ\colon S_\QQ\injects L_\QQ$ be its base change along $\ZZ\to\QQ$, and let
$j_L\colon L\to L_\QQ$ be the canonical map.
The **saturation** of $\iota$ is the pullback in $\ZZ\text{-}\mathbf{Mod}$

```tikzcd
\Sat_L(\iota) \arrow[r] \arrow[d] & S_\QQ \arrow[d,"\iota_\QQ"] \\
L \arrow[r,"j_L"'] & L_\QQ
```

The maps $S\to S_\QQ$ and $\iota\colon S\to L$ induce a canonical morphism
$S\to\Sat_L(\iota)$.
The embedding $\iota$ is **saturated** when this morphism is an isomorphism.
:::

::: {.proposition #prop:primitive-characterization title="Characterization of primitive embeddings"}

Let $\iota\colon S\injects L$ be a morphism of lattices, and let
$$
0\too S\xrightarrow{\iota}L\xrightarrow{q}Q_\iota\too0
$$
be its cokernel sequence.
The following conditions are equivalent.

1. $Q_\iota$ is torsion-free.

2. The canonical comparison $S\to\Sat_L(\iota)$ of @def:saturation is an isomorphism.

3. There exists a $\ZZ$-linear retraction $r\colon L\to S$ with $r\circ\iota=\id_S$.

4. Every $\ZZ$-basis of $S$ extends along $\iota$ to a $\ZZ$-basis of $L$.

5. The restriction morphism $\iota^\vee\colon\Hom_\ZZ(L,\ZZ)\twoheadrightarrow\Hom_\ZZ(S,\ZZ)$ is an epimorphism in $\bZ\text{-}\mathbf{Mod}$.

6. The canonical morphism $S\to(S^{\perp L})^{\perp L}$ is an isomorphism.

A morphism satisfying these conditions is a **primitive embedding**.
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
is exact.
The last term is the torsion subgroup of the finitely generated $\ZZ$-module $Q_\iota$, proving $(1)\Longleftrightarrow(2)$.

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

::: {.definition #def:coble-embedding-equivalence title="The groupoid of primitive embeddings"}

Fix a lattice $S$.
Let $\mathbf{PrimEmb}_S$ be the core of the full subcategory of the undercategory
$S/\mathbf{Lat}_\ZZ$ on primitive morphisms.
Thus its objects are primitive embeddings $\iota\colon S\injects M$, and a morphism
from $\iota_1\colon S\injects M_1$ to $\iota_2\colon S\injects M_2$ is an isometry
$\varphi\colon M_1\isoto M_2$ for which the triangle
```tikzcd
& S \arrow[dl,"\iota_1"'] \arrow[dr,"\iota_2"] & \\
M_1 \arrow[rr,"\varphi"'] && M_2
```
commutes.

For a fixed target $L$, write
$\Emb(S,L)\definedas\operatorname{PrimEmb}(S,L)$ for the set of primitive embedding morphisms.
Postcomposition by $\Orth(L)$ gives the fixed-target isomorphism classes
$\Orth(L)\backslash\Emb(S,L)$.
The commuting right action of $\Orth(S)$ gives the primitive-subobject orbit set
$\Orth(L)\backslash\Emb(S,L)/\Orth(S)$.

Nikulin's primitive-embedding classification [@Nik80 Prop. 1.15.1] classifies the
fixed-source isomorphism classes $\Orth(L)\backslash\Emb(S,L)$ by the corresponding
gluing data; passing to primitive subobjects introduces the additional right
$\Orth(S)$-action.
:::

## Overlattices and gluing

::: {.definition #def:overlattice title="Overlattices and their discriminant subobjects"}

An **overlattice** of a lattice $S$ is a lattice morphism
$\iota\colon S\injects L$ whose cokernel $H_\iota$ is finite length, with exact sequence
$$
0\too S\xrightarrow{\iota}L\xrightarrow{c_\iota}H_\iota\too0.
$$
Since $\iota_\QQ\colon S_\QQ\isoto L_\QQ$, its inverse induces
$\lambda_\iota\colon L\injects S^\#$ with $\lambda_\iota\circ\iota=\iota_S$.
Functoriality of the bilinear cokernel gives
$\bar{\lambda}_\iota\colon(H_\iota,0)\injects A_S$.
If $S$ is even, $L$ is even exactly when this refines to
$\bar{\lambda}_{\iota,q}\colon(H_\iota,0)\injects A_{S,q}$.
:::

::: {.theorem #thm:nikulin-gluing title="Nikulin's gluing correspondence"}

Let $S$ be an even lattice.
Let $\operatorname{Over}^{\mathrm{ev}}(S)$ be the poset of even overlattice morphisms $S\injects L$, ordered by morphisms over $S$.
Let $\operatorname{IsoSub}(A_{S,q})$ be the poset of isotropic quadratic subobjects
$h_q\colon(H,0)\injects A_{S,q}$, ordered by factorization.
Then
$$
\operatorname{Over}^{\mathrm{ev}}(S)
\isoto
\operatorname{IsoSub}(A_{S,q})
$$
as posets [@Nik80, §1.4].

For $h_q$ with bilinear monomorphism $h\colon H\injects A_S^\sharp$, let
$\pi_S\colon S^\#\twoheadrightarrow A_S^\sharp$ be the cokernel morphism.
The corresponding overlattice is the pullback in $\bZ\text{-}\mathbf{Mod}$
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
be the right orthogonal-complement kernel of the underlying isotropic bilinear subobject $h\colon(H,0)\injects A_S$.
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
The index equality follows from the exact sequence
$$
0\to S\to L_h\to H\to0,
$$
and
$\abs{\disc{S}}=[L_h:S]^2\abs{\disc{L_h}}$.
Equivariance under $\Orth(S)$ follows from functoriality of $S\mapsto(S^\#,A_S,q_S)$.
:::

::: {.construction #cons:embedding-gluing-data title="Gluing data of a primitive embedding"}

Let $\iota_S\colon S\injects L$ be a primitive embedding of even lattices with $L$ even, and let
$\iota_T\colon T\injects L$ represent its orthogonal complement.
Then $j\definedas\iota_S\perp\iota_T\colon S\perp T\injects L$ is an even overlattice, with cokernel sequence
$$
0\too S\perp T\xrightarrow{j}L\too H_j\too0.
$$
Let $h_{j,q}\colon(H_j,0)\injects A_{S,q}\perp A_{T,q}$ be its isotropic quadratic subobject from @thm:nikulin-gluing.

Primitivity implies that the two projections of $h_{j,q}$ are monomorphisms.
Write the induced quadratic subobjects as
$$
h_{S,q}\colon H_{S,q}\injects A_{S,q},
\qquad
h_{T,q}\colon H_{T,q}\injects A_{T,q}.
$$
Then there is a unique isometry $\gamma_q\colon H_{S,q}\isoto H_{T,q}(-1)$ whose graph is $h_{j,q}$.
Thus the gluing construction attached to $\iota$ is $(h_{S,q},h_{T,q},\gamma_q)$.

The index/discriminant relation gives
$$
\abs{\disc{T}}
=
\frac{\abs{\disc{L}}\,\cardinality{H_j}^2}{\abs{\disc{S}}}.
$$
If $L$ is unimodular, the two projections are isomorphisms and $A_{S,q}\isoto A_{T,q}(-1)$.
This is the primitive-embedding gluing construction of [@Nik80, §1.4--1.5].
:::

## Splitting of unimodular sublattices

::: {.definition #def:lattice-split title="Orthogonal splitting"}

Let $\iota_S\colon S\injects L$ be a primitive embedding, and let
$\iota_T\colon T\injects L$ represent its orthogonal-complement subobject.
The pair induces the orthogonal-sum morphism
$$
j_{\iota_S}\colon S\oplus T\too L,
\qquad
(s,t)\longmapsto\iota_S(s)+\iota_T(t).
$$
The embedding $\iota$ **splits** when $j_\iota$ is an isomorphism.
:::

::: {.proposition #prop:unimodular-splits title="Unimodular sublattices split"}

Let $\iota\colon S\injects L$ be a primitive embedding with $S$ unimodular and $L$ nondegenerate.
Then the orthogonal-sum morphism of @def:lattice-split is an isometry
$j_\iota\colon S\oplus S^{\perp L}\isoto L$.
If $L$ is unimodular, then $S^{\perp L}$ is unimodular.
:::

::: {.proof}

Let $\beta_S^\sharp\colon S\isoto S^\vee$ be the adjoint isomorphism of the unimodular lattice $S$, and let
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
Moreover, $\ker r$ is exactly the orthogonal-complement subobject $S^{\perp L}\injects L$.
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

Let $L$ be a nondegenerate unimodular lattice and let $v\in L$ be a primitive isotropic vector.
Then there exists $w\in L$ with $\beta_L(v, w) = 1$.
In particular $\div_L(v) = 1$ for every primitive vector $v\in L$.
:::

::: {.proof}

Since $L$ is unimodular, the canonical map $L\to \dualof{L}$ is an isomorphism, so every functional in $\dualof{L} = \Hom_\ZZ(L, \ZZ)$ has the form $\beta_L(u,\,\cdot\,)$ for a unique $u\in L$.
Because $v$ is primitive, by the primitive-sublattice characterization (@prop:primitive-characterization) it extends to a $\ZZ$-basis $e_1 = v, e_2,\ldots,e_n$ of $L$.
Let $\varphi\colon L\to\ZZ$ be the dual-basis functional with $\varphi(v) = 1$ and $\varphi(e_j) = 0$ for $j > 1$.
Writing $\varphi = \beta_L(w,\,\cdot\,)$ for the corresponding $w\in L$ and using symmetry gives $\beta_L(v, w) = \beta_L(w, v) = \varphi(v) = 1$.
For the divisibility statement, the image $\beta_L(v, L) = \div_L(v)\ZZ$ contains $\beta_L(v, w) = 1$, so $\div_L(v) = 1$.
:::

::: {.corollary #cor:hyperbolic-splitting title="Hyperbolic splitting of unimodular lattices"}

Let $L$ be a nondegenerate unimodular lattice containing a primitive isotropic vector.
Then $L$ splits off a rank-$2$ unimodular hyperbolic plane:
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

Let $e\in L$ be a primitive isotropic vector.
By @lem:unimodular-divisibility choose $w\in L$ with $\beta_L(e, w) = 1$, and set $k\definedas w^2$.
The sublattice $P\definedas\generators{e, w}$ has Gram matrix $\begin{bmatrix}0 & 1\\ 1 & k\end{bmatrix}$ of determinant $-1$, hence $P$ is a rank-$2$ unimodular sublattice, and it is primitive since a unimodular sublattice is saturated by the primitive-sublattice characterization (@prop:primitive-characterization).
The isometry type of $P$ is governed by the parity of $k = w^2$: the Gram matrix $\begin{bmatrix}0 & 1\\ 1 & k\end{bmatrix}$ gives $P\cong U$ when $k$ is even and $P\cong\latI_{1, 1}$ (the odd rank-$2$ unimodular hyperbolic lattice) when $k$ is odd.
We adjust $w$ within its coset to realize the parity dictated by $L$; note that adding to $w$ any vector of $\generators{e}^{\perp L}$ preserves $\beta_L(e, w) = 1$.

If $L$ is even then $k = w^2$ is even; replacing $w$ by $w - \tfrac{k}{2}e$ (and $e\in\generators{e}^{\perp L}$ since $e^2 = 0$) leaves $\beta_L(e, w) = 1$ unchanged and makes $w^2 = 0$, so $P\cong U$.

If $L$ is odd we arrange $w^2$ to be odd, so that $P\cong\latI_{1, 1}$.
Every $x\in L$ satisfies $x - \beta_L(e, x)\,w\in\generators{e}^{\perp L}$, so $L = \generators{e}^{\perp L} + \ZZ w$.
Were $\generators{e}^{\perp L}$ to consist entirely of even-norm vectors and $w^2$ even, every $x = y + mw$ ($y\in\generators{e}^{\perp L}$) would have $x^2 = y^2 + 2m\,\beta_L(y, w) + m^2 w^2$ even, forcing $L$ even --- contrary to hypothesis.
Hence either $w^2$ is already odd, or $\generators{e}^{\perp L}$ contains a vector $u$ of odd norm; in the latter case replace $w$ by $w + u$, which preserves $\beta_L(e, w) = 1$ and gives $(w + u)^2 = w^2 + 2\beta_L(w, u) + u^2$ odd.
Either way $k = w^2$ is odd and $P\cong\latI_{1, 1}$.

Since $P$ is unimodular, @prop:unimodular-splits gives $L\cong P\oplus P^{\perp L}$.
:::

## Maximal and split maximal lattices

::: {.definition #def:maximal-lattice title="Maximal lattices"}

An even lattice $L'$ is **maximal** if $A_{L',q}$ has no nonzero isotropic quadratic subobject
$(H,0)\injects A_{L',q}$.
A maximal overlattice of $L$ is an even overlattice morphism
$\iota\colon L\injects L'$ whose target is maximal.
:::

::: {.lemma #lem:maximal-overlattice-exists}

Every even lattice admits a maximal overlattice.
A unimodular lattice is maximal.
:::

::: {.proof}

By @thm:nikulin-gluing,
$$
\operatorname{Over}^{\mathrm{ev}}(L)
\isoto
\operatorname{IsoSub}(A_{L,q})
$$
as posets, with overlattices ordered by morphisms over $L$ and isotropic quadratic subobjects ordered by factorization.
The discriminant module $A_L^\sharp$ has finite length, so $\operatorname{IsoSub}(A_{L,q})$ is a finite poset and has a maximal element.
Its corresponding even overlattice admits no proper even overlattice, hence is maximal.
For a unimodular lattice $A_{L,q}=0$, so the zero subobject is maximal.
:::

::: {.definition #def:split-maximal title="Maximal lattices with two hyperbolic summands"}

A maximal lattice $L'$ of signature $(2,n)$ is **$U^{\oplus2}$-decomposable** if
$U^{\oplus2}\oplus L_0\isoto L'$ for some lattice $L_0$.
Dawes uses the term *split maximal* for this decomposition hypothesis [@Daw22 §3.1].
:::

::: {.theorem #thm:maximal-splits-for-large-n title="Maximal lattices of signature $(2,n)$ are $U^{\oplus2}$-decomposable for $n\geq5$"}

Every maximal lattice of signature $(2,n)$ with $n\geq5$ is $U^{\oplus2}$-decomposable.
:::

::: {.proof}

This is the decomposition result recorded in [@Daw22 §3.1], where it is attributed to
Attwell-Duval; for smaller $n$, see also [@Nik80 Cor. 1.13.5].
:::

::: {.theorem #thm:split-maximal-isotropic-transitivity title="Isotropic transitivity for a maximal $U^{\oplus2}$-decomposable lattice"}

Let $L'$ be a maximal $U^{\oplus2}$-decomposable lattice of signature $(2,n)$.

1. For any $x,y\in L'^{\mathrm{prim}}[0]$ there exists
   $\tau(x,y)\in\Orth^+(L')$ with $\tau(x,y)x=y$; hence $\Orth^+(L')$ acts
   transitively on $L'^{\mathrm{prim}}[0]$.

2. Two primitive totally isotropic embeddings
   $\iota_i\colon E_i\injects L'$ lie in the same $\Orth^+(L')$-orbit if and only if
   $E_1^{\perp L'}/E_1\cong E_2^{\perp L'}/E_2$.
:::

::: {.proof}

Both statements are in [@Daw22 §3.1]: Algorithm 3.3 constructs $\tau(x,y)$ from the
two displayed hyperbolic summands, and the Attwell-Duval criterion gives the second
orbit statement.
:::


## Finiteness of embedding orbits

::: {.proposition #prop:embedding-finiteness title="Finiteness of primitive-embedding orbits into an even unimodular lattice"}

Let $S$ and $L$ be even lattices with $L$ unimodular.
Then $\Orth(L)\backslash\Emb(S,L)$ is finite.
:::

::: {.proof}

Fix $\iota\colon S\injects L$ and put $T\definedas S^{\perp L}$.
Unimodularity of $L$ gives an isometry $A_{S,q}\isoto A_{T,q}(-1)$.
The signature of $T$ together with $A_{T,q}$ is therefore fixed, so $T$ belongs to a fixed genus; that genus contains finitely many integral isometry classes.

For each such $T$, the set $\operatorname{Iso}\qty{A_{S,q},A_{T,q}(-1)}$ is finite because the discriminant modules $A_S^\sharp$ and $A_T^\sharp$ have finite cardinality.
Nikulin's equivalence relation on these gluing data is induced by isometries of the target and complement [@Nik80, Prop. 1.15.1].
Hence only finitely many $\Orth(L)$-orbits of primitive embeddings occur.
:::

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
Then there is a short exact sequence in $\mathbf{BilMod}_{\bZ}$
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

The metric dual of the twist is
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
which gives the displayed short exact sequence.
If $L$ is unimodular, then $A_L=0$, so the exact sequence gives $A_{L(m)}\isoto K_m(L)$.
:::

::: {.definition #def:simultaneous-discriminant-spinor-kernel title="Simultaneous discriminant and spinor kernel"}
For signature $(2,n)$, let $\Orth^+(L)\injects\Orth(L)$ denote the spinor kernel. Define $\widetilde\Orth^+(L)$ by the pullback
```tikzcd
\widetilde\Orth^+(L) \arrow[r] \arrow[d] & \widetilde\Orth(L) \arrow[d] \\
\Orth^+(L) \arrow[r] & \Orth(L).
```
:::
