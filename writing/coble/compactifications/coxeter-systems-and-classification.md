# Coxeter systems and their classification

::: {.remark title="Orientation and sign convention"}

A Coxeter--Vinberg diagram (@def:coxeter-vinberg-diagram) is the combinatorial record of a symmetric bilinear form, and the geometry on which the associated reflection group acts is determined by the definiteness of that form.

Simple roots are negative-definite directions of norm $-2$, following the algebraic-geometry convention of @def:root-lattice, so a spherical Coxeter system has a negative definite Gram form.
:::

## Coxeter matrices and their Gram forms

::: {.definition #def:coxeter-matrix}

Let $S$ be a finite set.
A **Coxeter matrix** on $S$ is a symmetric matrix $M = (m_{st})_{s,t\in S}$ with
$$
m_{ss} = 1,
\qquad
m_{st} = m_{ts} \in \theset{2,3,4,\dots}\unioninfty
\quad (s\neq t)
.
$$
The Coxeter group presented by $M$ is the group $W(M)$ of @def:coxeter-group, the relation $(s t)^{m_{st}} = e$ being imposed only for $m_{st} < \infty$.
The pair $(W(M), S)$ is a **Coxeter system** of **rank** $\abs{S}$.
Its **Coxeter diagram** $\Sigma(M)$ is the graph on the vertex set $S$ with an edge $\theset{s,t}$ whenever $m_{st}\geq 3$, labelled by $m_{st}$ when $m_{st}\geq 4$.
:::

::: {.definition #def:coxeter-gram-form title="The Gram form of a Coxeter matrix"}

Let $M$ be a Coxeter matrix on $S$.
The **Gram form** of $M$ is the symmetric bilinear form $G(M)$ on the real vector space $\RR^S$ with basis $\theset{\alpha_s}_{s\in S}$ determined by
$$
G(M)_{st} \definedas \beta(\alpha_s,\alpha_t) = 2\cos\!\left(\frac{\pi}{m_{st}}\right)
,
$$
read on the diagonal as $G(M)_{ss} = 2\cos\pi = -2$, and as $G(M)_{st} = 2$ when $m_{st} = \infty$.
Each $\alpha_s$ has norm $-2$ and is therefore a short root in the sense of @def:2elementary-roots; the reflections $s_{\alpha_s}$ of @def:reflection preserve $G(M)$, and $s\mapsto s_{\alpha_s}$ extends to an injective homomorphism $W(M)\to \Orth(\RR^S, G(M))$ [@Bou08; @Hum90].
:::

::: {.remark title="Normalized pairings"}

Dividing by the norms recovers the quantity that labels the edges of a Coxeter--Vinberg diagram: with $\alpha_s^2 = \alpha_t^2 = -2$,
$$
g_{st} = \frac{\beta(\alpha_s,\alpha_t)}{\sqrt{\alpha_s^2\,\alpha_t^2}}
= \frac{G(M)_{st}}{2}
= \cos\!\left(\frac{\pi}{m_{st}}\right)
,
$$
which is the normalization of @def:coxeter-vinberg-diagram.
A Coxeter matrix produces only the values $g_{st}\leq 1$; Vinberg's diagrams admit in addition the ultraparallel case $g_{st} > 1$, which corresponds to no finite $m_{st}$ and is drawn dotted.
:::

::: {.remark #rmk:coxeter-form-values title="The values at small orders"}

$$
\begin{array}{c|cccccc}
m & 2 & 3 & 4 & 5 & 6 & \infty \\\hline
2\cos(\pi/m) & 0 & 1 & \sqrt2 & \dfrac{1+\sqrt5}{2} & \sqrt3 & 2
\end{array}
$$
:::

::: {.remark #rmk:gram-versus-cartan title="Gram and Cartan matrices"}

Let $\theset{\alpha_s}_{s\in S}$ be simple roots in a lattice $L$.
Two matrices are attached to them.
The **Gram matrix** is $G_{st} = \beta_L(\alpha_s,\alpha_t)$; it is symmetric and records the form.
The **Cartan matrix** is
$$
A_{st} \definedas \frac{2\,\beta_L(\alpha_s,\alpha_t)}{\beta_L(\alpha_t,\alpha_t)}
,
$$
so that $A_{ss} = 2$ and $s_{\alpha_t}(\alpha_s) = \alpha_s - A_{st}\alpha_t$; it records the reflections and is symmetric only when all the $\alpha_s$ have equal norm.
The two are related by a diagonal factor on the right,
$$
A = G\cdot\diag\!\left(\frac{2}{G_{11}},\dots,\frac{2}{G_{nn}}\right),
\qquad
G = A\cdot\diag\!\left(\frac{G_{11}}{2},\dots,\frac{G_{nn}}{2}\right)
,
$$
so $G$ is the Cartan matrix symmetrized by the root lengths.
In the simply-laced case, where every $\alpha_s^2 = -2$, one has $A = -G$.
When two root lengths occur the two matrices record different data: for $\alpha_s^2 = -2$ and $\alpha_t^2 = -4$ with $\beta_L(\alpha_s,\alpha_t) = 2$, the Cartan entries are $A_{st} = 1$ and $A_{ts} = 2$.
:::

::: {.remark #rmk:schlafli-sign title="The opposite normalization"}

Much of the reflection-group literature normalizes simple roots to $\alpha_s^2 = +2$ and attaches to $M$ the **Schläfli matrix** $C_{st} = -2\cos(\pi/m_{st})$, with $C_{ss} = 2$.
Then $C = -G(M)$, and every definiteness statement below is read with the opposite sign: a spherical system has $C$ positive definite.
:::

## Classification by definiteness

::: {.definition #def:coxeter-system-type}

Let $(W,S)$ be an irreducible Coxeter system of rank $n$ with Coxeter matrix $M$ and Gram form $G = G(M)$.
Say that $(W,S)$, or $M$, is

- **spherical** if $G$ is negative definite;

- **euclidean** if $G$ is negative semidefinite and $\ker G$ has rank $1$;

- **hyperbolic** if $G$ is nondegenerate of signature $(1, n-1)$.

A Gram form of signature $(p,q)$ with $p\geq 2$ falls under none of the three.

For subdiagrams, @def:elliptic-subdiagram names the corresponding conditions **elliptic**, **parabolic**, and **hyperbolic**. An elliptic subdiagram is one all of whose components are spherical; a parabolic subdiagram on $k$ vertices with $c$ connected components has kernel of rank $c$, hence rank $k-c$.
:::

::: {.remark}

By Sylvester's law of inertia, invoked in the Lattice Theory section to define the signature, the numbers $n_+$ and $n_-$ of positive and negative squares in a diagonalization of $G$ over $\RR$, and the rank of $\ker G$, are independent of the basis.
The three conditions of @def:coxeter-system-type are therefore properties of the form $G$ rather than of the matrix representing it: spherical is $(n_+,n_-) = (0,n)$, euclidean is $(0,n-1)$ with a one-dimensional kernel, and hyperbolic is $(1,n-1)$.
:::

::: {.theorem #thm:coxeter-type-and-geometry title="The geometry of the three types"}

Let $(W,S)$ be an irreducible Coxeter system of rank $n$ with Gram form $G$.

1. $(W,S)$ is spherical if and only if $W$ is finite.
   In that case $W$ acts on the unit sphere of the negative definite space $(\RR^S, -G)$ as a finite reflection group whose fundamental domain is a spherical simplex [@Bou08; @Hum90].

2. $(W,S)$ is euclidean if and only if $W$ is infinite and admits a faithful action on a euclidean space $\EE^{\,n-1}$ as a discrete group generated by $n$ affine reflections, with fundamental domain a euclidean simplex [@Bou08; @Hum90].

3. If $(W,S)$ is hyperbolic, then $\RR^S$ with the form $G$ is a model of hyperbolic $(n-1)$-space in the sense of @def:hyperbolic-model, and the reflections $s_{\alpha_s}$ generate a discrete subgroup of its isometry group whose fundamental domain is the Coxeter polytope
   $$
   P \definedas \theset{\, [v] \in \HH^{\,n-1} \mid \beta(v,\alpha_s)\geq 0 \text{ for all } s\in S \,}
   $$
   of @def:coxeter-polytope and [@Vin67; @Vin85].
:::

::: {.proof}

All three are [@Bou08, Ch. V §4 and Ch. VI §4; @Hum90, §§2.3, 6.4 and 6.8], with $G = -2B$ for $B$ the sources' invariant form, so that definite for $B$ is the corresponding definite sign for $G$.

What the clauses add to the cited statements is which space these forms act on, and that is the only part read off @def:coxeter-system-type.
In (1) the source's sphere belongs to $(\RR^S,2B)$, which is $(\RR^S,-G)$; rescaling a metric by a positive constant preserves the sphere, the reflections and their fundamental domain, so the citation covers the clause as written.
In (2) the euclidean space is $\RR^S/\ker G$, of dimension $n-1$; the affine reflections are the $s_{\alpha_s}$, and the discreteness asserted is properness of the action, which is how the source states it.
In (3) the hyperboloid inside the nondegenerate space $(\RR^S,G)$ is the model of $\HH^{n-1}$ of @def:hyperbolic-model, and $P$ is the chamber of @def:coxeter-polytope; this is the one clause where nondegeneracy rather than definiteness is what is needed.
:::

::: {.remark}

Statement (3) asserts nothing about the volume of $P$: the finite-volume and compact cases are separated by the criterion of @thm:coxeter-polytope-volume.
:::

## Subdiagrams and the inheritance of signature

::: {.definition #def:coxeter-subdiagram}

Let $\Sigma$ be the Coxeter diagram of $(W,S)$ and let $I\iscontainedin S$.
The **subdiagram** $\Sigma_I$ is the induced diagram on $I$, with Coxeter matrix $M[I,I]$ and Gram form the principal submatrix $G[I,I]$.
The **rank** of $\Sigma_I$ is the rank of $G[I,I]$.
The subgroup
$$
W_I \definedas \generators{\, s \mid s\in I \,} \leq W
$$
is the **standard parabolic subgroup** determined by $I$, and $(W_I, I)$ is a Coxeter system with Coxeter matrix $M[I,I]$ [@Bou08].
:::

::: {.remark title="Parabolic subgroups and parabolic subdiagrams"}

The two uses of *parabolic* are independent.
The subgroup $W_I$ is a standard parabolic subgroup for every subset $I\iscontainedin S$, whatever the definiteness of $G[I,I]$.
The subdiagram $\Sigma_I$ is parabolic when each of its connected components is euclidean (@def:elliptic-subdiagram), and then $(W_I, I)$ is a product of irreducible euclidean Coxeter systems, one for each component.
:::

::: {.proposition #prop:signature-under-restriction title="Restriction cannot increase the positive index"}

Let $\beta$ be a symmetric bilinear form on a finite-dimensional real vector space $V$, write $n_\pm(\beta)$ for its numbers of positive and negative squares, and let $V'\leq V$ be a subspace of codimension $c$.
Then
$$
n_+(\beta) - c \;\leq\; n_+\!\left(\restrictionof{\beta}{V'}\right) \;\leq\; n_+(\beta)
,
$$
and the same inequalities hold for $n_-$.
:::

::: {.proof}
The integer $n_+(\beta)$ is the largest dimension of a subspace of $V$ on which $\beta$ is positive definite.
A subspace of $V'$ on which $\restrictionof{\beta}{V'}$ is positive definite is such a subspace of $V$, which gives the upper bound.
If $P\leq V$ is positive definite of dimension $n_+(\beta)$, then $\beta$ is positive definite on $P\intersect V'$, and $\dim(P\intersect V')\geq n_+(\beta) - c$, which gives the lower bound.
Applying both to $-\beta$ gives the statement for $n_-$.
:::

::: {.corollary #cor:subdiagram-inheritance}

Let $\Sigma$ be a Coxeter diagram on $S$ and $J\iscontainedin I\iscontainedin S$.

1. If $\Sigma_I$ is elliptic then so is $\Sigma_J$.
   Equivalently, a subdiagram that is not elliptic is contained in no elliptic subdiagram.

2. If the Gram form of $\Sigma$ has exactly one positive square --- in particular if $\Sigma$ is hyperbolic --- then the Gram form of every subdiagram of $\Sigma$ has at most one positive square, so every subdiagram is negative semidefinite or of signature $(1,q)$ with a possibly nontrivial kernel.
:::

::: {.proof}
For (1), the restriction of a negative definite form to a subspace is negative definite.
For (2), apply the upper bound of @prop:signature-under-restriction with $n_+(G) = 1$.
:::

::: {.remark}

Part (1) is what makes an enumeration of the elliptic subdiagrams of a Coxeter--Vinberg diagram tractable: a subset that fails to be elliptic can be discarded together with all subsets containing it, so the search runs over the order ideal of elliptic subsets rather than over all of $2^{S}$.
:::

## The spherical and euclidean classifications

::: {.theorem #thm:spherical-classification title="Classification of spherical Coxeter systems"}

An irreducible Coxeter system is spherical if and only if its Coxeter diagram is one of
$$
A_n\ (n\geq 1),\quad
B_n\ (n\geq 2),\quad
D_n\ (n\geq 4),\quad
E_6,\ E_7,\ E_8,\quad
F_4,\quad
H_3,\quad
H_4,\quad
I_2(p)\ (p\geq 5)
,
$$
and diagrams from distinct entries of this list are not isomorphic [@Bou08; @Hum90].
:::

::: {.proof}

This is the Cartan--Killing classification, [@Bou08, Ch. VI §4, Théorème 1] and [@Hum90, §2.4 and §3.6].

The cited statements classify connected Coxeter graphs carrying positive definite forms, which is the same list under $G = -2B$.
:::

::: {.remark}

Here $I_2(p)$ denotes the rank-two diagram with $m_{12} = p$, so that $I_2(3)\cong A_2$, $I_2(4)\cong B_2$ and $I_2(6)\cong G_2$; the list above records each isomorphism class once.
The root systems $B_n$ and $C_n$ of @def:root-system-Bn-Cn have the same Coxeter matrix and so contribute a single entry, the two being distinguished by their root lengths rather than by their Coxeter system.
:::

::: {.theorem #thm:euclidean-classification title="Classification of euclidean Coxeter systems"}

An irreducible Coxeter system is euclidean if and only if its Coxeter diagram is one of
$$
\tilde A_1,\quad
\tilde A_n\ (n\geq 2),\quad
\tilde B_n\ (n\geq 3),\quad
\tilde C_n\ (n\geq 2),\quad
\tilde D_n\ (n\geq 4),\quad
\tilde E_6,\ \tilde E_7,\ \tilde E_8,\quad
\tilde F_4,\quad
\tilde G_2
,
$$
each of rank $n+1$ and drawn in the diagram table of the Diagrams appendix [@Bou08].
The diagram $\tilde A_1$ has two vertices joined by a bond with $m_{12} = \infty$, and $\tilde A_n$ for $n\geq 2$ is the cycle on $n+1$ vertices with all bonds $m_{ij} = 3$.
:::

::: {.proof}

This is the classification of irreducible affine Coxeter diagrams, [@Bou08, Ch. VI §4, Théorème 2] and [@Hum90, §2.5 and §6.5].

The sources list the affine diagrams together with their completed Dynkin diagrams; the Dynkin diagram is the affine one with the vertex that $\delta$ of @prop:euclidean-radical meets with coefficient $1$ adjoined.
:::

::: {.proposition #prop:euclidean-radical title="The radical of a euclidean diagram"}

Let $\Sigma$ be an irreducible euclidean diagram on the vertex set $I$, with Gram form $G[I,I]$ and simple roots $\theset{\alpha_s}_{s\in I}$.
Then $\ker G[I,I]$ is spanned by a vector
$$
\delta = \Sum_{s\in I} n_s\,\alpha_s
\qquad\text{with all } n_s > 0
,
$$
unique up to scalar, and $\delta^2 = 0$ [@Bou08; @Hum90].
:::

::: {.proof}

That $\ker G[I,I]$ is one-dimensional with a generating vector of strictly positive coordinates is [@Bou08, Ch. VI §2.3, Proposition 6] and [@Hum90, §2.5]; the cited statement is for the positive semidefinite normalization, and invertibility of the sign change in @thm:coxeter-type-and-geometry preserves kernels, so the kernel is the same subspace here.

Two clauses follow formally once the generators are known, and are recorded because the page uses them:
$\delta^2 = \beta(\delta,\delta) = 0$, since $\delta$ lies in the kernel of the form;
and the uniqueness up to scalar is the one-dimensionality, an irreducible euclidean diagram being connected so that its Gram form is not a direct sum.

The positivity is the substantive part and is not formal: it says $\delta$ lies in the closed cone spanned by the simple roots, not merely in the kernel of the form.
That is what the remark below uses, and it is proved in the cited places by checking that the coefficients of the affine diagram's highest root, or an explicit solution of $G[I,I]x = 0$, are positive in each type.
:::

::: {.remark}

The positivity of the coefficients $n_s$ is what places $\delta$ in the closure of a cone rather than merely in the kernel of a form, and is the reason a parabolic subdiagram of a hyperbolic Coxeter polytope determines an ideal point of the boundary rather than an arbitrary isotropic line; see @prop:polytope-vertex-subdiagram.
For $\tilde E_8$ the coefficients are the marks $(1,2,3,4,6,5,4,3,2)$ of the highest root of $E_8$.
:::

## Crystallographic Coxeter systems

::: {.definition #def:crystallographic-coxeter}

A Coxeter matrix $M$ on $S$ is **crystallographic** if $m_{st}\in\theset{2,3,4,6,\infty}$ for all $s\neq t$.
:::

::: {.theorem #thm:crystallographic-lattice}

A Coxeter matrix $M$ is crystallographic if and only if the group $W(M)$ preserves a lattice of full rank in $\RR^S$ [@Bou08; @Hum90].
:::

::: {.proof}

This is [@Bou08, Ch. VI §4, no. 1] and [@Hum90, §2.11].

The forward direction is the one with content: for $m\in\{2,3,4,6\}$ the number $2\cos(\pi/m)$ is an integer, so $G[I,I]$ is an integral Gram matrix in the basis $\alpha_s$ by @prop:gram-form-integrality, and the span of that basis is then a full-rank lattice preserved by the reflections of @def:coxeter-gram-form, which act by the integral matrices $s_{\alpha_t}(\alpha_s) = \alpha_s - G_{st}\alpha_t$.

Conversely, if $W$ preserves a full-rank lattice $L$ then in a basis of $L$ the reflections act by integral matrices, and the entry $(s_{\alpha_t}(\alpha_s) : \alpha_t)$ is $-G_{st} = -2\cos(\pi/m_{st})$, an integer.
Write $\lambda \definedas 2\cos(\pi/m)$; it is an algebraic integer, being $\zeta+\zeta^{-1}$ for a root of unity $\zeta$, and lying in $\QQ$ it is then an integer in $[-2,2]$.
The values $2\cos(\pi/m)$ in that range are $2, 1, 0, -1, -2$ at $m = \infty, 3, 2, 4, 6$ respectively, and no other order qualifies, since $2\cos(\pi/m)$ is then strictly between $-2$ and $2$ and irrational by @prop:coxeter-base-field-degree.
So $m\in\{2,3,4,6,\infty\}$, which is @def:crystallographic-coxeter.
:::

::: {.example #ex:crystallographic-rescaling title="Rescaling to an integral form"}

The equal-norm normalization $\alpha_s^2 = -2$ of @def:coxeter-gram-form does not itself make the form integral, and a crystallographic $M$ becomes integral only after the simple roots are rescaled.
For $m_{st} = 4$ one has $\beta(\alpha_s,\alpha_t) = 2\cos(\pi/4) = \sqrt2$; replacing $\alpha_t$ by $\alpha_t' \definedas \sqrt2\,\alpha_t$ gives
$$
\alpha_s^2 = -2,
\qquad
(\alpha_t')^2 = -4,
\qquad
\beta(\alpha_s,\alpha_t') = 2
,
$$
a short root and a long root in the sense of @def:2elementary-roots.
For $m_{st} = 6$ the same rescaling by $\sqrt3$ gives norms $-2$ and $-6$ with pairing $3$, which is the ratio occurring in $G_2$.
For $m_{st}\in\theset{2,3}$ the entries $0$ and $1$ are already integral, and the simply-laced diagrams need no rescaling.
:::

::: {.definition #def:coxeter-base-field}

Let $M$ be a Coxeter matrix on $S$.
Its **base field** is the subfield
$$
K(M) \definedas \QQ\!\left(\, 2\cos(\pi/m_{st}) \;:\; s\neq t,\ m_{st} < \infty \,\right) \iscontainedin \RR
,
$$
the smallest field over which the Gram form $G(M)$ is defined.
:::

::: {.proposition #prop:coxeter-base-field-degree}

For an integer $m\geq 2$ one has $2\cos(\pi/m) = \zeta_{2m} + \inverseof{\zeta_{2m}}$ for a primitive $2m$-th root of unity $\zeta_{2m}$, so $\QQ(2\cos(\pi/m))$ is the maximal totally real subfield of $\QQ(\zeta_{2m})$ and
$$
\left[\QQ\!\left(2\cos(\pi/m)\right) : \QQ\right] = \tfrac12\,\#\unitsof{(\ZZ/2m\ZZ)}
.
$$
In particular $K(M) = \QQ$ exactly when $m_{st}\in\theset{2,3,\infty}$ for all $s\neq t$.
:::

::: {.proof}

The first identity is $\zeta_{2m} + \zeta_{2m}^{-1} = 2\cos(2\pi/2m) = 2\cos(\pi/m)$ for a primitive $2m$-th root, and $\zeta\mapsto\zeta^{-1}$ generates $\operatorname{Gal}(\QQ(\zeta_{2m})/\QQ)$, a group of order $\#(\ZZ/2m\ZZ)^{\!\times}$.
Complex conjugation is $\zeta\mapsto\zeta^{-1}$, so it is the involution $\sigma$ of that group, and an element $x$ of the cyclotomic field is fixed by $\sigma$ exactly when $x\in\QQ(\zeta_{2m})^{\langle\sigma\rangle}$.
The fixed field of conjugation is the maximal totally real subfield, and $\zeta+\zeta^{-1}$ generates it: it is fixed, and $[\QQ(\zeta):\QQ(\zeta+\zeta^{-1})] = 2$ because $\zeta$ satisfies the quadratic $T^2 - (\zeta+\zeta^{-1})T + 1$ over that field and is not in it.
Hence $\QQ(2\cos(\pi/m))$ is that fixed field, of degree $\tfrac12\#(\ZZ/2m\ZZ)^{\!\times}$ over $\QQ$.

For the specializations, Euler's $\varphi$ is $1$ exactly at $1$ and $2$, so $\tfrac12\varphi(2m) = 1$ exactly when $2m\in\{2,4\}$; $2m = 2$ would give $m = 1$, which is not an order $\geq2$, leaving $m = 2$.
The value $m = 3$ gives $\varphi(6) = 2$ and degree $1$ as well, so these two orders give rational values, and they give $2\cos(\pi/2) = 0$ and $2\cos(\pi/3) = 1$; the order $m = \infty$ is not in the index set of the union and contributes the diagonal value $2$ of @def:coxeter-gram-form.
Every order $m\geq4$ has $\varphi(2m)\geq 4$ and hence degree $\geq2$, so $K(M) = \QQ$ exactly for the three listed orders.
:::

::: {.proposition #prop:gram-form-integrality title="When the Gram form is integral"}

$G(M)$ has all its entries in $\ZZ$ if and only if $m_{st}\in\theset{2,3,\infty}$ for every $s\neq t$.
Among the Coxeter matrices with every $m_{st}$ finite, these are exactly the simply-laced ones.
:::

::: {.proof}
The entries are the values of @rmk:coxeter-form-values, and an entry lies in $\ZZ$ only if it lies in $\QQ$.
By @prop:coxeter-base-field-degree the degree of $\QQ(2\cos(\pi/m))$ over $\QQ$ is $\tfrac12\#(\ZZ/2m\ZZ)^\times$, which equals $1$ exactly when $2m\in\theset{4,6}$, that is when $m\in\theset{2,3}$; the value at $m=\infty$ is $2$.
The remaining orders therefore give irrational entries, and the three admissible orders give $0$, $1$ and $2$.
:::

::: {.example #ex:noncrystallographic-base-rings title="The non-crystallographic spherical types"}

Of the spherical types of @thm:spherical-classification, those that are not crystallographic are $H_3$, $H_4$, and $I_2(p)$ for $p\notin\theset{2,3,4,6}$.

For $m = 5$,
$$
2\cos(\pi/5) = \varphi \definedas \frac{1+\sqrt5}{2},
\qquad
\varphi^2 = \varphi + 1
,
$$
so $H_3$ and $H_4$ both have base field $K = \QQ(\sqrt5)$, and their Gram forms have entries in the ring of integers $\ZZ[\varphi]$ of that field.
For $m = 8$ the base field is $\QQ(\sqrt{2+\sqrt2})$, of degree $4$ over $\QQ$ by @prop:coxeter-base-field-degree.
:::

::: {.remark #rmk:galois-conjugate-gram-form title="Galois conjugates of a Gram form"}

Let $M$ be a Coxeter matrix with base field $K = K(M)$, a totally real number field, and let $\sigma\in\gal(K/\QQ)$.
Applying $\sigma$ entrywise to $G(M)$ produces a symmetric $K$-valued form $\sigma(G(M))$ of the same rank, with the same diagonal $-2$.
Its signature is not determined by that of $G(M)$: the signature of a symmetric form over a totally real field is not a Galois invariant, as the rank-one forms $\generators{1-\sqrt2}$ and $\generators{1+\sqrt2}$ over $\QQ(\sqrt2)$ show.
Whether every nontrivial conjugate of a hyperbolic Gram form is negative definite is a condition on $M$ that must be computed, and is the arithmeticity question recorded in the Open Problems section.
:::

## Origins

::: {.remark title="Attribution"}

Coxeter introduced the matrices and diagrams now named after him and classified the finite reflection groups, obtaining the list of @thm:spherical-classification with its two non-crystallographic exceptional types $H_3$ and $H_4$; the euclidean classification of @thm:euclidean-classification grew out of Weyl's theory of root systems and the affine reflection groups.
Both are given in Bourbaki [@Bou08] and in Humphreys [@Hum90], and the geometric and topological theory of general Coxeter groups in Davis [@Dav08].
The hyperbolic theory --- the polytope picture, the finite-volume criterion, and the algorithm of @thm:vinberg-algorithm --- is due to Vinberg [@Vin67; @Vin75; @Vin85]; Lannér classified the compact hyperbolic Coxeter simplices, and Vinberg and Kaplinskaja determined the reflection groups of the odd unimodular hyperbolic lattices $\latI_{18,1}$ and $\latI_{19,1}$ [@VK78], which are the ranks the moduli theory of this monograph meets.
:::
