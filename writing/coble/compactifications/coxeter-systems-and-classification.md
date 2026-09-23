# Coxeter systems and their classification

::: {.Remark}
### Orientation and sign convention

A Coxeter--Vinberg diagram (\longref{def:coxeter-vinberg-diagram}) is the combinatorial record of a symmetric bilinear form, and the geometry on which the associated reflection group acts is determined by the definiteness of that form.

Simple roots are negative-definite directions of norm $-2$, following the algebraic-geometry convention of \longref{def:root-lattice}, so a spherical Coxeter system has a negative definite Gram form.
:::

## Coxeter matrices and their Gram forms

::: {.Definition #def:coxeter-matrix}

Let $S$ be a finite set.
A **Coxeter matrix** on $S$ is a symmetric matrix $M = (m_{st})_{s,t\in S}$ with
$$
m_{ss} = 1,
\qquad
m_{st} = m_{ts} \in \ts{2,3,4,\dots}\union\ts{\infty}
\quad (s\neq t)
.
$$
The Coxeter group presented by $M$ is the group $W(M)$ of \longref{def:coxeter-group}, the relation $(s t)^{m_{st}} = e$ being imposed only for $m_{st} < \infty$.
The pair $(W(M), S)$ is a **Coxeter system** of **rank** $\abs{S}$.
Its **Coxeter diagram** $\Sigma(M)$ is the graph on the vertex set $S$ with an edge $\ts{s,t}$ whenever $m_{st}\geq 3$, labelled by $m_{st}$ when $m_{st}\geq 4$.
:::

::: {.Definition #def:coxeter-gram-form}
### The Gram form of a Coxeter matrix

Let $M$ be a Coxeter matrix on $S$.
The **Gram form** of $M$ is the symmetric bilinear form $G(M)$ on the real vector space $\RR^S$ with basis $\ts{\alpha_s}_{s\in S}$ determined by
$$
G(M)_{st} \da \beta(\alpha_s,\alpha_t) = 2\cos\!\left(\frac{\pi}{m_{st}}\right)
,
$$
read on the diagonal as $G(M)_{ss} = 2\cos\pi = -2$, and as $G(M)_{st} = 2$ when $m_{st} = \infty$.
Each $\alpha_s$ has norm $-2$ and is therefore a short root in the sense of \longref{def:2elementary-roots}; the reflections $s_{\alpha_s}$ of \longref{def:reflection} preserve $G(M)$, and $s\mapsto s_{\alpha_s}$ extends to an injective homomorphism $W(M)\to \Orth(\RR^S, G(M))$ [@Bou08; @Hum90].
:::

::: {.Remark}
### Normalized pairings

Dividing by the norms recovers the quantity that labels the edges of a Coxeter--Vinberg diagram: with $\alpha_s^2 = \alpha_t^2 = -2$,
$$
g_{st} = \frac{\beta(\alpha_s,\alpha_t)}{\sqrt{\alpha_s^2\,\alpha_t^2}}
= \frac{G(M)_{st}}{2}
= \cos\!\left(\frac{\pi}{m_{st}}\right)
,
$$
which is the normalization of \longref{def:coxeter-vinberg-diagram}.
A Coxeter matrix produces only the values $g_{st}\leq 1$; Vinberg's diagrams admit in addition the ultraparallel case $g_{st} > 1$, which corresponds to no finite $m_{st}$ and is drawn dotted.
:::

::: {.Remark #rmk:coxeter-form-values}
### The values at small orders

$$
\begin{array}{c|cccccc}
m & 2 & 3 & 4 & 5 & 6 & \infty \\\hline
2\cos(\pi/m) & 0 & 1 & \sqrt2 & \dfrac{1+\sqrt5}{2} & \sqrt3 & 2
\end{array}
$$
:::

::: {.Remark #rmk:gram-versus-cartan}
### Gram and Cartan matrices

Let $\ts{\alpha_s}_{s\in S}$ be simple roots in a lattice $L$.
Two matrices are attached to them.
The **Gram matrix** is $G_{st} = \beta_L(\alpha_s,\alpha_t)$; it is symmetric and records the form.
The **Cartan matrix** is
$$
A_{st} \da \frac{2\,\beta_L(\alpha_s,\alpha_t)}{\beta_L(\alpha_t,\alpha_t)}
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

::: {.Remark #rmk:schlafli-sign}
### The opposite normalization

Much of the reflection-group literature normalizes simple roots to $\alpha_s^2 = +2$ and attaches to $M$ the **Schläfli matrix** $C_{st} = -2\cos(\pi/m_{st})$, with $C_{ss} = 2$.
Then $C = -G(M)$, and every definiteness statement below is read with the opposite sign: a spherical system has $C$ positive definite.
:::

## Classification by definiteness

::: {.Definition #def:coxeter-system-type}

Let $(W,S)$ be an irreducible Coxeter system of rank $n$ with Coxeter matrix $M$ and Gram form $G = G(M)$.
Say that $(W,S)$, or $M$, is

- **spherical** if $G$ is negative definite;

- **euclidean** if $G$ is negative semidefinite and $\ker G$ has rank $1$;

- **hyperbolic** if $G$ is nondegenerate of signature $(1, n-1)$.

A Gram form of signature $(p,q)$ with $p\geq 2$ falls under none of the three.

For subdiagrams, \longref{def:elliptic-subdiagram} names the corresponding conditions **elliptic**, **parabolic**, and **hyperbolic**.
An elliptic subdiagram is one all of whose components are spherical; a parabolic subdiagram on $k$ vertices with $c$ connected components has kernel of rank $c$, hence rank $k-c$.
:::

::: {.Remark}

By Sylvester's law of inertia, invoked in the Lattice Theory section to define the signature, the numbers $n_+$ and $n_-$ of positive and negative squares in a diagonalization of $G$ over $\RR$, and the rank of $\ker G$, are independent of the basis.
The three conditions of \longref{def:coxeter-system-type} are therefore properties of the form $G$ rather than of the matrix representing it: spherical is $(n_+,n_-) = (0,n)$, euclidean is $(0,n-1)$ with a one-dimensional kernel, and hyperbolic is $(1,n-1)$.
:::

::: {.Theorem #thm:coxeter-type-and-geometry}
### The geometry of the three types

Let $(W,S)$ be an irreducible Coxeter system of rank $n$ with Gram form $G$.

1. $(W,S)$ is spherical if and only if $W$ is finite.
   In that case $W$ acts on the unit sphere of the negative definite space $(\RR^S, -G)$ as a finite reflection group whose fundamental domain is a spherical simplex [@Bou08; @Hum90].

2. $(W,S)$ is euclidean if and only if $W$ is infinite and admits a faithful action on a euclidean space $\EE^{\,n-1}$ as a discrete group generated by $n$ affine reflections, with fundamental domain a euclidean simplex [@Bou08; @Hum90].

3. If $(W,S)$ is hyperbolic, then $\RR^S$ with the form $G$ is a model of hyperbolic $(n-1)$-space in the sense of \longref{def:hyperbolic-model}, and the reflections $s_{\alpha_s}$ generate a discrete subgroup of its isometry group whose fundamental domain is the Coxeter polytope
   $$
   P \da \ts{\, [v] \in \HH^{\,n-1} \mid \beta(v,\alpha_s)\geq 0 \text{ for all } s\in S \,}
   $$
   of \longref{def:coxeter-polytope} [@Vin67; @Vin85].
:::

::: {.Remark}

Statement (3) asserts nothing about the volume of $P$: the finite-volume and compact cases are separated by the criterion of \longref{thm:coxeter-polytope-volume}.
:::

## Subdiagrams and the inheritance of signature

::: {.Definition #def:coxeter-subdiagram}

Let $\Sigma$ be the Coxeter diagram of $(W,S)$ and let $I\containedin S$.
The **subdiagram** $\Sigma_I$ is the induced diagram on $I$, with Coxeter matrix $M[I,I]$ and Gram form the principal submatrix $G[I,I]$.
The **rank** of $\Sigma_I$ is the rank of $G[I,I]$.
The subgroup
$$
W_I \da \gens{\, s \mid s\in I \,} \leq W
$$
is the **standard parabolic subgroup** determined by $I$, and $(W_I, I)$ is a Coxeter system with Coxeter matrix $M[I,I]$ [@Bou08].
:::

::: {.Remark}
### Parabolic subgroups and parabolic subdiagrams

The two uses of *parabolic* are independent.
The subgroup $W_I$ is a standard parabolic subgroup for every subset $I\containedin S$, whatever the definiteness of $G[I,I]$.
The subdiagram $\Sigma_I$ is parabolic when each of its connected components is euclidean (\longref{def:elliptic-subdiagram}), and then $(W_I, I)$ is a product of irreducible euclidean Coxeter systems, one for each component.
:::

::: {.Proposition #prop:signature-under-restriction}
### Restriction cannot increase the positive index

Let $\beta$ be a symmetric bilinear form on a finite-dimensional real vector space $V$, write $n_\pm(\beta)$ for its numbers of positive and negative squares, and let $V'\leq V$ be a subspace of codimension $c$.
Then
$$
n_+(\beta) - c \;\leq\; n_+\!\left(\ro{\beta}{V'}\right) \;\leq\; n_+(\beta)
,
$$
and the same inequalities hold for $n_-$.
:::

::: {.proof}
The integer $n_+(\beta)$ is the largest dimension of a subspace of $V$ on which $\beta$ is positive definite.
A subspace of $V'$ on which $\ro{\beta}{V'}$ is positive definite is such a subspace of $V$, which gives the upper bound.
If $P\leq V$ is positive definite of dimension $n_+(\beta)$, then $\beta$ is positive definite on $P\intersect V'$, and $\dim(P\intersect V')\geq n_+(\beta) - c$, which gives the lower bound.
Applying both to $-\beta$ gives the statement for $n_-$.
:::

::: {.Corollary #cor:subdiagram-inheritance}

Let $\Sigma$ be a Coxeter diagram on $S$ and $J\containedin I\containedin S$.

1. If $\Sigma_I$ is elliptic then so is $\Sigma_J$.
   Equivalently, a subdiagram that is not elliptic is contained in no elliptic subdiagram.

2. If the Gram form of $\Sigma$ has exactly one positive square --- in particular if $\Sigma$ is hyperbolic --- then the Gram form of every subdiagram of $\Sigma$ has at most one positive square, so every subdiagram is negative semidefinite or of signature $(1,q)$ with a possibly nontrivial kernel.
:::

::: {.proof}
For (1), the restriction of a negative definite form to a subspace is negative definite.
For (2), apply the upper bound of \longref{prop:signature-under-restriction} with $n_+(G) = 1$.
:::

::: {.Remark}

Part (1) is what makes an enumeration of the elliptic subdiagrams of a Coxeter--Vinberg diagram tractable: a subset that fails to be elliptic can be discarded together with all subsets containing it, so the search runs over the order ideal of elliptic subsets rather than over all of $2^{S}$.
:::

## The spherical and euclidean classifications

::: {.Theorem #thm:spherical-classification}
### Classification of spherical Coxeter systems

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

::: {.Remark}

Here $I_2(p)$ denotes the rank-two diagram with $m_{12} = p$, so that $I_2(3)\cong A_2$, $I_2(4)\cong B_2$ and $I_2(6)\cong G_2$; the list above records each isomorphism class once.
The root systems $B_n$ and $C_n$ of \longref{def:root-system-Bn-Cn} have the same Coxeter matrix and so contribute a single entry, the two being distinguished by their root lengths rather than by their Coxeter system.
:::

::: {.Theorem #thm:euclidean-classification}
### Classification of euclidean Coxeter systems

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

::: {.Proposition #prop:euclidean-radical}
### The radical of a euclidean diagram

Let $\Sigma$ be an irreducible euclidean diagram on the vertex set $I$, with Gram form $G[I,I]$ and simple roots $\ts{\alpha_s}_{s\in I}$.
Then $\ker G[I,I]$ is spanned by a vector
$$
\delta = \Sum_{s\in I} n_s\,\alpha_s
\qquad\text{with all } n_s > 0
,
$$
unique up to scalar, and $\delta^2 = 0$ [@Bou08; @Hum90].
:::

::: {.Remark}

The positivity of the coefficients $n_s$ is what places $\delta$ in the closure of a cone rather than merely in the kernel of a form, and is the reason a parabolic subdiagram of a hyperbolic Coxeter polytope determines an ideal point of the boundary rather than an arbitrary isotropic line; see \longref{prop:polytope-vertex-subdiagram}.
For $\tilde E_8$ the coefficients are the marks $(1,2,3,4,6,5,4,3,2)$ of the highest root of $E_8$.
:::

## Crystallographic Coxeter systems

::: {.Definition #def:crystallographic-coxeter}

A Coxeter matrix $M$ on $S$ is **crystallographic** if $m_{st}\in\ts{2,3,4,6,\infty}$ for all $s\neq t$.
:::

::: {.Theorem #thm:crystallographic-lattice}

A Coxeter matrix $M$ is crystallographic if and only if the group $W(M)$ preserves a lattice of full rank in $\RR^S$ [@Bou08; @Hum90].
:::

::: {.Example #ex:crystallographic-rescaling}
### Rescaling to an integral form

The equal-norm normalization $\alpha_s^2 = -2$ of \longref{def:coxeter-gram-form} does not itself make the form integral, and a crystallographic $M$ becomes integral only after the simple roots are rescaled.
For $m_{st} = 4$ one has $\beta(\alpha_s,\alpha_t) = 2\cos(\pi/4) = \sqrt2$; replacing $\alpha_t$ by $\alpha_t' \da \sqrt2\,\alpha_t$ gives
$$
\alpha_s^2 = -2,
\qquad
(\alpha_t')^2 = -4,
\qquad
\beta(\alpha_s,\alpha_t') = 2
,
$$
a short root and a long root in the sense of \longref{def:2elementary-roots}.
For $m_{st} = 6$ the same rescaling by $\sqrt3$ gives norms $-2$ and $-6$ with pairing $3$, which is the ratio occurring in $G_2$.
For $m_{st}\in\ts{2,3}$ the entries $0$ and $1$ are already integral, and the simply-laced diagrams need no rescaling.
:::

::: {.Definition #def:coxeter-base-field}

Let $M$ be a Coxeter matrix on $S$.
Its **base field** is the subfield
$$
K(M) \da \QQ\!\left(\, 2\cos(\pi/m_{st}) \;:\; s\neq t,\ m_{st} < \infty \,\right) \containedin \RR
,
$$
the smallest field over which the Gram form $G(M)$ is defined.
:::

::: {.Proposition #prop:coxeter-base-field-degree}

For an integer $m\geq 2$ one has $2\cos(\pi/m) = \zeta_{2m} + \zeta_{2m}\inv$ for a primitive $2m$-th root of unity $\zeta_{2m}$, so $\QQ(2\cos(\pi/m))$ is the maximal totally real subfield of $\QQ(\zeta_{2m})$ and
$$
\left[\QQ\!\left(2\cos(\pi/m)\right) : \QQ\right] = \tfrac12\,\#(\ZZ/2m\ZZ)\units
.
$$
In particular $K(M) = \QQ$ exactly when $m_{st}\in\ts{2,3,\infty}$ for all $s\neq t$.
:::

::: {.Proposition #prop:gram-form-integrality}
### When the Gram form is integral

$G(M)$ has all its entries in $\ZZ$ if and only if $m_{st}\in\ts{2,3,\infty}$ for every $s\neq t$.
Among the Coxeter matrices with every $m_{st}$ finite, these are exactly the simply-laced ones.
:::

::: {.proof}
The entries are the values of \longref{rmk:coxeter-form-values}, and an entry lies in $\ZZ$ only if it lies in $\QQ$.
By \longref{prop:coxeter-base-field-degree} the degree of $\QQ(2\cos(\pi/m))$ over $\QQ$ is $\tfrac12\#(\ZZ/2m\ZZ)^\times$, which equals $1$ exactly when $2m\in\ts{4,6}$, that is when $m\in\ts{2,3}$; the value at $m=\infty$ is $2$.
The remaining orders therefore give irrational entries, and the three admissible orders give $0$, $1$ and $2$.
:::

::: {.Example #ex:noncrystallographic-base-rings}
### The non-crystallographic spherical types

Of the spherical types of \longref{thm:spherical-classification}, those that are not crystallographic are $H_3$, $H_4$, and $I_2(p)$ for $p\notin\ts{2,3,4,6}$.

For $m = 5$,
$$
2\cos(\pi/5) = \varphi \da \frac{1+\sqrt5}{2},
\qquad
\varphi^2 = \varphi + 1
,
$$
so $H_3$ and $H_4$ both have base field $K = \QQ(\sqrt5)$, and their Gram forms have entries in the ring of integers $\ZZ[\varphi]$ of that field.
For $m = 8$ the base field is $\QQ(\sqrt{2+\sqrt2})$, of degree $4$ over $\QQ$ by \longref{prop:coxeter-base-field-degree}.
:::

::: {.Remark #rmk:galois-conjugate-gram-form}
### Galois conjugates of a Gram form

Let $M$ be a Coxeter matrix with base field $K = K(M)$, a totally real number field, and let $\sigma\in\operatorname{Gal}(K/\QQ)$.
Applying $\sigma$ entrywise to $G(M)$ produces a symmetric $K$-valued form $\sigma(G(M))$ of the same rank, with the same diagonal $-2$.
Its signature is not determined by that of $G(M)$: the signature of a symmetric form over a totally real field is not a Galois invariant, as the rank-one forms $\gens{1-\sqrt2}$ and $\gens{1+\sqrt2}$ over $\QQ(\sqrt2)$ show.
Whether every nontrivial conjugate of a hyperbolic Gram form is negative definite is a condition on $M$ that must be computed, and is the arithmeticity question recorded in the Open Problems section.
:::

## Origins

::: {.Remark}
### Attribution

Coxeter introduced the matrices and diagrams now named after him and classified the finite reflection groups, obtaining the list of \longref{thm:spherical-classification} with its two non-crystallographic exceptional types $H_3$ and $H_4$; the euclidean classification of \longref{thm:euclidean-classification} grew out of Weyl's theory of root systems and the affine reflection groups.
Both are given in Bourbaki [@Bou08] and in Humphreys [@Hum90], and the geometric and topological theory of general Coxeter groups in Davis [@Dav08].
The hyperbolic theory --- the polytope picture, the finite-volume criterion, and the algorithm of \longref{thm:vinberg-algorithm} --- is due to Vinberg [@Vin67; @Vin75; @Vin85]; Lannér classified the compact hyperbolic Coxeter simplices, and Vinberg and Kaplinskaja determined the reflection groups of the odd unimodular hyperbolic lattices $\latI_{18,1}$ and $\latI_{19,1}$ [@VK78], which are the ranks the moduli theory of this monograph meets.
:::
