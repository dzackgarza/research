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

5. The restriction morphism $\iota^\vee\colon\Hom_\ZZ(L,\ZZ)\to\Hom_\ZZ(S,\ZZ)$ is surjective.

6. The canonical morphism $S\to(S^{\perp L})^{\perp L}$ is an isomorphism.

A morphism satisfying these conditions is a **primitive embedding**.
:::

::: {.proof}

Tensor the cokernel sequence with $\QQ$.
The saturation pullback of @def:saturation identifies with the kernel of the composite
$$
L\too L_\QQ\too (Q_\iota)_\QQ.
$$
The induced sequence
$$
0\too S\too\Sat_L(\iota)
\too\ker\bigl(Q_\iota\to(Q_\iota)_\QQ\bigr)
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
$$
\bigl((S_\QQ)^{\perp L_\QQ}\bigr)^{\perp L_\QQ}=S_\QQ.
$$
Pulling this identity back along $L\to L_\QQ$ identifies $(S^{\perp L})^{\perp L}$ canonically with $\Sat_L(\iota)$.
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
$$
\Emb(S,L)\definedas\operatorname{PrimEmb}(S,L)
$$
for the set of primitive embedding morphisms.
Postcomposition gives a left action of $\Orth(L)$ on $\Emb(S,L)$, and the isomorphism
classes in the fixed-target subgroupoid are therefore
$$
\Orth(L)\backslash\Emb(S,L).
$$
Precomposition gives the commuting right action of $\Orth(S)$.
Consequently the $\Orth(L)$-orbits of primitive subobjects of $L$ isometric to $S$ are
classified by the double quotient
$$
\Orth(L)\backslash\Emb(S,L)/\Orth(S),
$$
which is not the same object as $\Emb(S,L)$ or as $\Orth(L)\backslash\Emb(S,L)$.

Nikulin's primitive-embedding classification [@Nik80 Prop. 1.15.1] classifies the
fixed-source isomorphism classes $\Orth(L)\backslash\Emb(S,L)$ by the corresponding
gluing data; passing to primitive subobjects introduces the additional right
$\Orth(S)$-action.
:::

## Overlattices and gluing

::: {.definition #def:overlattice title="Overlattices and their discriminant subobjects"}

An **overlattice** of a lattice $S$ is a lattice morphism
$$
\iota\colon S\injects L
$$
whose carrier cokernel $H_\iota$ is a finite-length $\bZ$-module:
$$
0\too S\xrightarrow{\iota}L\xrightarrow{c_\iota}H_\iota\too0.
$$
Since $\iota_\QQ\colon S_\QQ\isoto L_\QQ$ is an isomorphism, its inverse induces a canonical monomorphism
$$
\lambda_\iota\colon L\injects S^\#
$$
with $\lambda_\iota\circ\iota=\iota_S$.
Functoriality of the bilinear cokernel gives an isotropic bilinear subobject
$$
\bar\lambda_\iota\colon(H_\iota,0)\injects A_S.
$$
If $S$ is even, the overlattice $L$ is even exactly when the same carrier monomorphism refines to an isotropic quadratic subobject
$$
\bar\lambda_{\iota,q}\colon(H_\iota,0)\injects A_{S,q}.
$$
:::

::: {.theorem #thm:nikulin-gluing title="Nikulin's gluing correspondence"}

Let $S$ be an even lattice.
Let $\operatorname{Over}^{\mathrm{ev}}(S)$ be the poset of even overlattice morphisms $S\injects L$, ordered by morphisms over $S$.
Let $\operatorname{IsoSub}(A_{S,q})$ be the poset of isotropic quadratic subobjects
$$
h_q\colon(H,0)\injects A_{S,q},
$$
ordered by factorization.
Then
$$
\operatorname{Over}^{\mathrm{ev}}(S)
\isoto
\operatorname{IsoSub}(A_{S,q})
$$
as posets [@Nik80, §1.4].

For $h_q$ with carrier monomorphism $h\colon H\injects S^\#/S$, let
$$
\pi_S\colon S^\#\twoheadrightarrow S^\#/S
$$
be the carrier quotient.
The corresponding overlattice is the pullback in $\bZ\text{-}\mathbf{Mod}$
```tikzcd id="overlattice-from-isotropic-subobject"
L_h \arrow[r] \arrow[d] & S^\# \arrow[d,"\pi_S"] \\
H \arrow[r,hook,"h"'] & S^\#/S .
```
It fits into
$$
0\too S\too L_h\too H\too0.
$$

Let
$$
(H^\perp,\bar\beta_S|_{H^\perp})\injects A_S
$$
be the bilinear orthogonal-complement subobject of the underlying isotropic bilinear subobject $(H,0)\injects A_S$.
Then the bilinear discriminant form of $L_h$ is the bilinear cokernel
$$
A_{L_h}
\isoto
\coker_{\mathbf{BilMod}_{\bZ}}\bigl((H,0)\injects H^\perp\bigr),
$$
while $A_{L_h,q}$ is the induced quadratic quotient of $A_{S,q}$.
Moreover,
$$
[L_h:S]=\abs H,
\qquad
\disc L_h=\frac{\disc S}{\abs H^2}.
$$
The natural $\Orth(S)$-actions on the two posets are intertwined by this correspondence.
:::

::: {.proof}

For an overlattice $\iota\colon S\injects L$, the morphism $\bar\lambda_\iota\colon H_\iota\injects A_S$ is isotropic precisely because the rational extension of the form on $S$ restricts to an even integral form on $L$.
If
$$
S\xrightarrow{\iota_1}L_1\xrightarrow{f}L_2
$$
is a morphism of overlattices, functoriality of cokernels gives a factorization of $\bar\lambda_{\iota_1}$ through $\bar\lambda_{\iota_2}$.
Thus the construction is order-preserving.

Conversely, the displayed pullback defining $L_h$ has kernel $S$ and cokernel $H$.
Isotropy of $h$ is exactly the condition that the rational extension of the form on $S$ restrict to an even integral form on $L_h$.
The two constructions are inverse by the universal properties of the cokernel and pullback.

The orthogonal-complement construction identifies $A_{L_h}$ with the cokernel of $H\to H^\perp$, giving the displayed short exact sequence.
The index equality follows from $0\to S\to L_h\to H\to0$, and the determinant formula follows from
$$
\abs{\disc S}=[L_h:S]^2\abs{\disc L_h}.
$$
Equivariance under $\Orth(S)$ follows from functoriality of $S\mapsto(S^\#,A_S,q_S)$.
:::

::: {.construction #cons:embedding-gluing-data title="Gluing data of a primitive embedding"}

Let
$$
\iota\colon S\injects L
$$
be a primitive embedding of even lattices with $L$ even, and let
$\kappa\colon T\injects L$ represent the orthogonal-complement subobject.
The induced morphism
$$
j\definedas\iota\perp\kappa\colon S\perp T\injects L
$$
is an even overlattice.
Let
$$
0\too S\perp T\xrightarrow{j}L\too H_j\too0
$$
be its carrier cokernel sequence, and let
$$
h_{j,q}\colon(H_j,0)\injects A_{S,q}\perp A_{T,q}
$$
be the isotropic quadratic subobject of @thm:nikulin-gluing.

Primitivity implies that the two carrier projections of $h_{j,q}$ are monomorphisms.
Write the induced quadratic subobjects as
$$
h_{S,q}\colon H_{S,q}\injects A_{S,q},
\qquad
h_{T,q}\colon H_{T,q}\injects A_{T,q}.
$$
Then there is a unique quadratic anti-isometry
$$
\gamma_q\colon H_{S,q}\isoto -H_{T,q}
$$
whose graph is $h_{j,q}$.
Thus the gluing construction attached to $\iota$ is $(h_{S,q},h_{T,q},\gamma_q)$.

The index/discriminant relation gives
$$
\abs{\disc T}
=
\frac{\abs{\disc L}\,\abs{H_j}^2}{\abs{\disc S}}.
$$
If $L$ is unimodular, the two projections are isomorphisms and
$$
A_{S,q}\isoto -A_{T,q}.
$$
This is the primitive-embedding gluing construction of [@Nik80, §1.4--1.5].
:::

## Splitting of unimodular sublattices

::: {.definition #def:lattice-split title="Orthogonal splitting"}

Let $\iota\colon S\injects L$ be a primitive embedding, and let
$\kappa\colon T\injects L$ represent its orthogonal-complement subobject.
The pair induces the orthogonal-sum morphism
$$
j_\iota\colon S\oplus T\too L,
\qquad
(s,t)\longmapsto\iota(s)+\kappa(t).
$$
The embedding $\iota$ **splits** when $j_\iota$ is an isomorphism.
:::

::: {.proposition #prop:unimodular-splits title="Unimodular sublattices split"}

Let $\iota\colon S\injects L$ be a primitive embedding with $S$ unimodular and $L$ nondegenerate.
Then the orthogonal-sum morphism $j_\iota$ of @def:lattice-split is an isometry
$$
j_\iota\colon S\oplus S^{\perp L}\isoto L.
$$
If $L$ is unimodular, then $S^{\perp L}$ is unimodular.
:::

::: {.proof}

Let
$$
\beta_S^\sharp\colon S\isoto S^\vee
$$
be the adjoint isomorphism of the unimodular lattice $S$, and let
$\iota^\vee\colon L^\vee\to S^\vee$ be restriction along $\iota$.
Define
$$
r\definedas
(\beta_S^\sharp)^{-1}
\circ\iota^\vee
\circ\beta_L^\sharp
\colon L\too S.
$$
Since $\iota$ preserves the bilinear forms,
$$
r\circ\iota=\id_S.
$$
Moreover, $\ker r$ is exactly the orthogonal-complement subobject $S^{\perp L}\injects L$.
Hence
$$
0\too S^{\perp L}\too L\xrightarrow{r}S\too0
$$
is split by $\iota$, and the induced map
$$
S\oplus S^{\perp L}\isoto L
$$
is an isometry.

If $L$ is unimodular, additivity of the discriminant functor for orthogonal direct sums gives
$$
A_L\isoto A_S\perp A_{S^{\perp L}}.
$$
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
By the unimodular-divisibility lemma (@lem:unimodular-divisibility) choose $w\in L$ with $\beta_L(e, w) = 1$, and set $k\definedas w^2$.
The sublattice $P\definedas\generators{e, w}$ has Gram matrix $\begin{bmatrix}0 & 1\\ 1 & k\end{bmatrix}$ of determinant $-1$, hence $P$ is a rank-$2$ unimodular sublattice, and it is primitive since a unimodular sublattice is saturated by the primitive-sublattice characterization (@prop:primitive-characterization).
The isometry type of $P$ is governed by the parity of $k = w^2$: the Gram matrix $\begin{bmatrix}0 & 1\\ 1 & k\end{bmatrix}$ gives $P\cong U$ when $k$ is even and $P\cong\latI_{1, 1}$ (the odd rank-$2$ unimodular hyperbolic lattice) when $k$ is odd.
We adjust $w$ within its coset to realize the parity dictated by $L$; note that adding to $w$ any vector of $\generators{e}^{\perp L}$ preserves $\beta_L(e, w) = 1$.

If $L$ is even then $k = w^2$ is even; replacing $w$ by $w - \tfrac{k}{2}e$ (and $e\in\generators{e}^{\perp L}$ since $e^2 = 0$) leaves $\beta_L(e, w) = 1$ unchanged and makes $w^2 = 0$, so $P\cong U$.

If $L$ is odd we arrange $w^2$ to be odd, so that $P\cong\latI_{1, 1}$.
Every $x\in L$ satisfies $x - \beta_L(e, x)\,w\in\generators{e}^{\perp L}$, so $L = \generators{e}^{\perp L} + \ZZ w$.
Were $\generators{e}^{\perp L}$ to consist entirely of even-norm vectors and $w^2$ even, every $x = y + mw$ ($y\in\generators{e}^{\perp L}$) would have $x^2 = y^2 + 2m\,\beta_L(y, w) + m^2 w^2$ even, forcing $L$ even --- contrary to hypothesis.
Hence either $w^2$ is already odd, or $\generators{e}^{\perp L}$ contains a vector $u$ of odd norm; in the latter case replace $w$ by $w + u$, which preserves $\beta_L(e, w) = 1$ and gives $(w + u)^2 = w^2 + 2\beta_L(w, u) + u^2$ odd.
Either way $k = w^2$ is odd and $P\cong\latI_{1, 1}$.

Since $P$ is unimodular, the unimodular-splitting proposition (@prop:unimodular-splits) gives $L\cong P\oplus P^{\perp L}$.
:::

## Maximal and split maximal lattices

::: {.definition #def:maximal-lattice title="Maximal lattices"}

An even lattice $L'$ is **maximal** if its quadratic discriminant form $A_{L',q}$ has no nonzero isotropic quadratic subobject
$$
(H,0)\injects A_{L',q}.
$$
A maximal overlattice of $L$ is an even overlattice morphism
$$
\iota\colon L\injects L'
$$
whose target is maximal.
:::

::: {.lemma #lem:maximal-overlattice-exists}

Every even lattice admits a maximal overlattice.
A unimodular lattice is maximal.
:::

::: {.proof}

Nikulin's correspondence is an isomorphism of posets when even overlattices of $L$
are ordered by embedding morphisms over $L$ and isotropic subgroups of $A_L$ are
ordered by inclusion.
Indeed, if $\eta\colon \dualof{L}\to A_L$ is the quotient map, then
$$
H_1\leq H_2
\quad\Longleftrightarrow\quad
\inverseof{\eta}(H_1)\injects\inverseof{\eta}(H_2)
$$
by the canonical inclusion over $L$.
Choose an isotropic subgroup maximal under inclusion; it exists because $A_L$ is finite.
The corresponding even overlattice admits no proper even overlattice, hence is maximal.
A unimodular lattice has $A_L = 0$, so the condition is vacuous.
:::

::: {.definition #def:split-maximal title="Maximal lattices with two hyperbolic summands"}

A maximal lattice $L'$ of signature $(2,n)$ is **$U^{\oplus2}$-decomposable** if there is
an isometry
$$
U^{\oplus2}\oplus L_0\isoto L'
$$
for some lattice $L_0$.
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
Then
$$
\Orth(L)\backslash\Emb(S,L)
$$
is finite.
:::

::: {.proof}

Fix $\iota\colon S\injects L$ and put $T\definedas S^{\perp L}$.
Unimodularity of $L$ gives a quadratic anti-isometry
$$
A_{S,q}\isoto -A_{T,q}.
$$
The signature of $T$ together with $A_{T,q}$ is therefore fixed, so $T$ belongs to a fixed genus; that genus contains finitely many integral isometry classes.

For each such $T$, the set
$$
\operatorname{AntiIso}(A_{S,q},A_{T,q})
$$
is finite because the common carrier modules have finite length over $\bZ$ and therefore finite cardinality.
Nikulin's equivalence relation on these gluing data is induced by isometries of the target and complement [@Nik80, Prop. 1.15.1].
Hence only finitely many $\Orth(L)$-orbits of primitive embeddings occur.
:::

::: {.proposition #prop:scaled-discriminant-ses title="Bilinear discriminant form of a scaled lattice"}

Let $L$ be an integral lattice and let $m>0$.
Define the finite value submodule
$$
W_m(L)
\definedas
\operatorname{im}\!\left(
L\tensor_\bZL
\xrightarrow{\ (x,y)\mapsto\beta_L(x,y)/m+\bZ\ }
\bQ/\bZ
\right),
$$
and define the bilinear module
$$
K_m(L)
\definedas
\left(
L/mL,
W_m(L),
\kappa_m
\right),
\qquad
\kappa_m(\bar x,\bar y)
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
If $L$ is unimodular, then
$$
A_{L(m)}\isoto K_m(L),
$$
whose carrier is
$$
L/mL\isoto(\bZ/m\bZ)^{\rank L}.
$$
:::

::: {.proof}

The metric dual of the twist is
$$
L(m)^\#
\isoto
\tfrac1mL^\#.
$$
Multiplication by $m$ on $L_\QQ$ induces the carrier morphism
$$
\tfrac1mL^\#/L
\too
L^\#/L,
\qquad
x+L
\longmapsto
mx+L.
$$
Together with multiplication by $m$ on the finite value modules, this defines the bilinear-module morphism
$$
F_m\colon A_{L(m)}\too A_L,
$$
because
$$
\bar\beta_L(mx,my)
=
m\,\bar\beta_{L(m)}(x,y).
$$

The kernel of $F_m$ in $\mathbf{BilMod}_{\bZ}$ has carrier
$$
\tfrac1mL/L
\isoto
L/mL
$$
and induced pairing $\kappa_m$ with exact value submodule $W_m(L)$.
Hence
$$
\ker_{\mathbf{BilMod}_{\bZ}}(F_m)
\isoto
K_m(L),
$$
which gives the displayed short exact sequence.
If $L$ is unimodular, then $A_L=0$, so the sequence identifies $A_{L(m)}$ with $K_m(L)$.
:::

The Miranda--Morrison exact sequence and Nikulin stable-range vanishing are @thm:miranda-morrison and @cor:nikulin-mm-vanishing.
::: {.definition #def:simultaneous-discriminant-spinor-kernel title="Simultaneous discriminant and spinor kernel"}
For signature $(2,n)$, let $\Orth^+(L)\injects\Orth(L)$ denote the spinor kernel. Define $\widetilde\Orth^+(L)$ by the pullback
```tikzcd id="disc-spinor-kernel-pullback"
\widetilde\Orth^+(L) \arrow[r] \arrow[d] & \widetilde\Orth(L) \arrow[d] \\
\Orth^+(L) \arrow[r] & \Orth(L).
```
:::
