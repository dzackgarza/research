# Coxeter systems and their classification

::: {.notation title="Sign convention"}

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
Each $\alpha_s$ has norm $-2$ and is therefore a short root in the sense of @def:2elementary-roots; the reflections $s_{\alpha_s}$ of @def:reflection preserve $G(M)$, and $s\mapsto s_{\alpha_s}$ extends to an injective homomorphism $W(M)\to \Orth(\RR^S, G(M))$ [@Bou08, Ch. V §4 no. 3, Prop. 3, and no. 4, Cor. 2 of Th. 1; @Hum90, §5.3, Proposition, and §5.4, Corollary]. These sources use the form $B_M(\alpha_s,\alpha_t)=-\cos(\pi/m_{st})$, so $G(M)=-2B_M$, and their reflection $\sigma_s(x)=x-2B_M(\alpha_s,x)\alpha_s$ is the reflection $s_{\alpha_s}(x)=x+\beta(x,\alpha_s)\alpha_s$.
:::

::: {.proposition #prop:coxeter-normalized-pairing title="Normalized pairings of a Coxeter matrix"}

Let $M$ be a Coxeter matrix on $S$ and $s\neq t$ in $S$.
The normalized pairing of @def:coxeter-vinberg-diagram of the simple roots $\alpha_s,\alpha_t$ of @def:coxeter-gram-form is
$$
g_{st} = \frac{\beta(\alpha_s,\alpha_t)}{\sqrt{\alpha_s^2\,\alpha_t^2}}
= \frac{G(M)_{st}}{2}
= \cos\!\left(\frac{\pi}{m_{st}}\right)
,
$$
read as $g_{st} = 1$ when $m_{st} = \infty$.
In particular $g_{st}\leq 1$.
:::

::: {.proof}

By @def:coxeter-gram-form, $\alpha_s^2 = \alpha_t^2 = -2$, so $\sqrt{\alpha_s^2\,\alpha_t^2} = 2$, and $\beta(\alpha_s,\alpha_t) = G(M)_{st}$ is $2\cos(\pi/m_{st})$ for $m_{st} < \infty$ and $2$ for $m_{st} = \infty$.
:::

::: {.example #ex:coxeter-form-values title="The values at small orders"}

The entries $2\cos(\pi/m)$ of @def:coxeter-gram-form at the orders $m\leq 6$ and $m = \infty$ are
$$
\begin{array}{c|cccccc}
m & 2 & 3 & 4 & 5 & 6 & \infty \\\hline
2\cos(\pi/m) & 0 & 1 & \sqrt2 & \dfrac{1+\sqrt5}{2} & \sqrt3 & 2
\end{array}
$$
:::

::: {.notation title="The opposite normalization"}

Much of the reflection-group literature normalizes simple roots to $\alpha_s^2 = +2$ and attaches to $M$ the **Schläfli matrix** $C_{st} = -2\cos(\pi/m_{st})$, with $C_{ss} = 2$.
Then $C = -G(M)$, and the definiteness conditions of @def:coxeter-system-type are read with the opposite sign: a spherical system has $C$ positive definite.
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

::: {.proposition #prop:coxeter-type-signature title="The three types by signature"}

Let $(W,S)$ be an irreducible Coxeter system of rank $n$ with Gram form $G$, and let $\operatorname{sig}(\RR^S, G) = (p,q,r)$ be the signature of @def:signature.
Then $(W,S)$ is spherical if and only if $(p,q,r) = (0,n,0)$, euclidean if and only if $(p,q,r) = (0,n-1,1)$, and hyperbolic if and only if $(p,q,r) = (1,n-1,0)$.
:::

::: {.proof}

By @thm:sylvester, $p+q+r = n$.
The form $G$ is negative definite exactly when $q = n$.
It is negative semidefinite exactly when $p = 0$, and then $\ker G$ has rank $1$ exactly when $r = 1$, that is $q = n-1$.
It is nondegenerate of signature $(1,n-1)$ exactly when $r = 0$, $p = 1$ and $q = n-1$.
:::

::: {.theorem #thm:coxeter-type-and-geometry title="The geometry of the three types"}

Let $(W,S)$ be an irreducible Coxeter system of rank $n$ with Gram form $G$.

1. $(W,S)$ is spherical if and only if $W$ is finite.
   In that case $W$ acts on the unit sphere of the negative definite space $(\RR^S, -G)$ as a finite reflection group whose fundamental domain is a spherical simplex [@Bou08, Ch. V §4 no. 8, Th. 2 and Prop. 9].

2. $(W,S)$ is euclidean if and only if $W$ is infinite and admits a faithful action on a euclidean space $\EE^{\,n-1}$ as a discrete group generated by $n$ affine reflections, with fundamental domain a euclidean simplex [@Bou08, Ch. V §4 no. 9, Lemma 2 and Props. 10 and 11].

3. If $(W,S)$ is hyperbolic, then $\RR^S$ with the form $G$ is a model of hyperbolic $(n-1)$-space in the sense of @def:hyperbolic-model, and the reflections $s_{\alpha_s}$ generate a discrete subgroup of its isometry group whose fundamental domain is the Coxeter polytope
   $$
   P \definedas \theset{\, [v] \in \HH^{\,n-1} \mid \beta(v,\alpha_s)\geq 0 \text{ for all } s\in S \,}
   $$
   of @def:coxeter-polytope and [@Vin67; @Vin85].
:::

::: {.proof}

All three are [@Bou08, Ch. V §4; @Hum90, §§6.4, 6.5 and 6.8], with $G = -2B$ for $B$ the sources' invariant form, so that definite for $B$ is the corresponding definite sign for $G$.

In (1) the sphere of the sources is that of $(\RR^S,2B)$, which is $(\RR^S,-G)$; rescaling a metric by a positive constant preserves the sphere, the reflections and their fundamental domain. The closed cone $\overline{C}_0$ on which every $B(\alpha_s,-)$ is nonnegative is a fundamental domain [@Bou08, Ch. V §4 no. 8, Prop. 9]. It is a simplicial cone because the $\alpha_s$ form a basis, so it meets the sphere in a spherical simplex.
In (2) the euclidean space is the affine hyperplane $A$ of [@Bou08, Ch. V §4 no. 9, Prop. 10]. Its translation space is dual to $\RR^S/\ker G$, and $G$ identifies it with $\RR^S/\ker G$, of dimension $n-1$. The affine reflections are the restrictions of the contragredient reflections of the $s_{\alpha_s}$ to $A$, and discreteness is properness of the action.
In (3) the hyperboloid inside the nondegenerate space $(\RR^S,G)$ is the model of $\HH^{n-1}$ of @def:hyperbolic-model, and $P$ is the chamber of @def:coxeter-polytope.
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
is the **standard parabolic subgroup** determined by $I$, and $(W_I, I)$ is a Coxeter system with Coxeter matrix $M[I,I]$ [@Bou08, Ch. IV §1 no. 8, Th. 2; @Hum90, §5.5, Theorem].
:::

::: {.notation title="Parabolic subgroups and parabolic subdiagrams"}

The subgroup $W_I$ is a standard parabolic subgroup for every subset $I\iscontainedin S$, whatever the definiteness of $G[I,I]$.
The subdiagram $\Sigma_I$ is parabolic when each of its connected components is euclidean (@def:elliptic-subdiagram).
:::

::: {.proposition #prop:parabolic-subdiagram-product title="The Coxeter system of a parabolic subdiagram"}

Let $\Sigma_I$ be a parabolic subdiagram with connected components $\Sigma_{I_1},\dots,\Sigma_{I_r}$.
Then $W_I$ is the direct product of the standard parabolic subgroups $W_{I_1},\dots,W_{I_r}$, and each $(W_{I_j}, I_j)$ is an irreducible euclidean Coxeter system.
:::

::: {.proof}

By @def:coxeter-subdiagram, $(W_I, I)$ is a Coxeter system with Coxeter diagram $\Sigma_I$.
For any Coxeter system, $W$ is the direct product of the standard parabolic subgroups of the connected components of its Coxeter diagram, and each of these is an irreducible Coxeter system [@Hum90, §6.1, Proposition].
Each $\Sigma_{I_j}$ is euclidean because $\Sigma_I$ is parabolic.
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
and diagrams from distinct entries of this list are not isomorphic [@Bou08, Ch. VI §4 no. 1, Th. 1; @Hum90, §2.7, Theorem].
:::

::: {.proof}

By definition, $(W,S)$ is spherical exactly when $B=-\tfrac12G$ is positive definite. The connected Coxeter graphs with $B$ positive definite are those of [@Hum90, §2.4, Figure 1, and §2.7, Theorem]. In [@Bou08, Ch. VI §4 no. 1, Ths. 1 and 2] the same list is the list of connected Coxeter graphs with $W$ finite, and $W$ is finite exactly when $B$ is positive definite [@Bou08, Ch. V §4 no. 8, Th. 2].

The cited statements classify the connected Coxeter graphs whose form $B$ is positive definite, and $G = -2B$.
:::

::: {.notation title="The diagrams $I_2(p)$"}

$I_2(p)$ denotes the rank-two diagram with $m_{12} = p$, so that $I_2(3)\cong A_2$, $I_2(4)\cong B_2$ and $I_2(6)\cong G_2$.
:::

::: {.proposition #prop:bn-cn-coxeter-system title="$B_n$ and $C_n$ have one Coxeter system"}

The root systems $B_n$ and $C_n$ of @def:root-system-Bn-Cn are distinct crystallographic root systems with the same Weyl group, the Coxeter group of type $B_n$ [@Hum90, §2.9].
:::

::: {.proof}

This is [@Hum90, §2.9].
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
each of rank $n+1$ [@Bou08, Ch. VI §4 no. 2, Th. 4; @Hum90, §2.5, Figure 2].
The diagram $\tilde A_1$ has two vertices joined by a bond with $m_{12} = \infty$, and $\tilde A_n$ for $n\geq 2$ is the cycle on $n+1$ vertices with all bonds $m_{ij} = 3$.
:::

::: {.proof}

This is the classification of the connected Coxeter graphs with $B$ positive semidefinite and degenerate [@Bou08, Ch. VI §4 no. 2, Th. 4; @Hum90, §2.5, Figure 2, §2.7, Theorem, and §6.5]. The graph that Bourbaki calls $\tilde B_2$ is $\tilde C_2$ here. For a connected graph with $B$ positive semidefinite and degenerate, $\ker B$ has rank $1$ [@Hum90, §2.6, Proposition (a)], so these are the euclidean diagrams.
:::

::: {.proposition #prop:euclidean-radical title="The radical of a euclidean diagram"}

Let $\Sigma$ be an irreducible euclidean diagram on the vertex set $I$, with Gram form $G[I,I]$ and simple roots $\theset{\alpha_s}_{s\in I}$.
Then $\ker G[I,I]$ is spanned by a vector
$$
\delta = \Sum_{s\in I} n_s\,\alpha_s
\qquad\text{with all } n_s > 0
,
$$
unique up to scalar, and $\delta^2 = 0$ [@Bou08, Ch. V §4 no. 9, Lemma 2; @Hum90, §2.6, Proposition (a)].
:::

::: {.proof}

That $\ker G[I,I]$ is one-dimensional and spanned by a vector of strictly positive coordinates is [@Bou08, Ch. V §4 no. 9, Lemma 2] and [@Hum90, §2.6, Proposition (a)]; the cited statement is for the positive semidefinite form $B$, and $G = -2B$ has the same kernel.
Uniqueness up to scalar is the one-dimensionality, and $\delta^2 = \beta(\delta,\delta) = 0$ because $\delta$ lies in the kernel of the form.
:::

::: {.example #ex:affine-e8-radical title="The radical of $\tilde E_8$"}

Number the vertices of $\tilde E_8$ as $\alpha_0,\alpha_1,\dots,\alpha_8$, with $\alpha_1,\dots,\alpha_8$ the simple roots of $E_8$ in Bourbaki numbering and $\alpha_0$ the added vertex, joined to $\alpha_8$.
The kernel of the Gram form $G[I,I]$ is spanned by
$$
\delta = \alpha_0 + 2\alpha_1 + 3\alpha_2 + 4\alpha_3 + 6\alpha_4 + 5\alpha_5 + 4\alpha_6 + 3\alpha_7 + 2\alpha_8
,
$$
whose coefficients at $\alpha_1,\dots,\alpha_8$ are those of the highest root of $E_8$.
:::

## Crystallographic Coxeter systems

::: {.definition #def:crystallographic-coxeter}

A Coxeter matrix $M$ on $S$ is **crystallographic** if $m_{st}\in\theset{2,3,4,6,\infty}$ for all $s\neq t$.
:::

::: {.theorem #thm:crystallographic-lattice}

Let $M$ be a Coxeter matrix on $S$, and let $W(M)$ act on $\RR^S$ by the reflections $s_{\alpha_s}$ of @def:coxeter-gram-form.
If the Coxeter diagram $\Sigma(M)$ contains no circuit, then $W(M)$ preserves a lattice of full rank in $\RR^S$ if and only if $M$ is crystallographic.
In general, $W(M)$ preserves a lattice of full rank in $\RR^S$ if and only if $M$ is crystallographic and every circuit in $\Sigma(M)$ has an even number of edges labelled $4$ and an even number of edges labelled $6$ [@Hum90, §6.6, Proposition].
:::

::: {.proof}

This is [@Hum90, §6.6, Proposition], stated there for the geometric representation with form $B$; the reflections of @def:coxeter-gram-form are those of $B$, since $G = -2B$.
:::

::: {.example #ex:crystallographic-rescaling title="Rescaling to an integral form"}

For a crystallographic $M$ with some $m_{st}\in\theset{4,6}$, the Gram form $G(M)$ is not integral by @prop:gram-form-integrality, and rescaling simple roots makes the pairings integral.
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
Its **field of definition** is the subfield
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
The entries are the values $2\cos(\pi/m_{st})$ of @def:coxeter-gram-form (@ex:coxeter-form-values), and an entry lies in $\ZZ$ only if it lies in $\QQ$.
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

::: {.example #ex:galois-conjugate-gram-form title="Galois conjugates of a Gram form"}

Let $M$ be a Coxeter matrix with base field $K = K(M)$, a totally real number field, and let $\sigma\in\gal(K/\QQ)$.
Applying $\sigma$ entrywise to $G(M)$ produces a symmetric $K$-valued form $\sigma(G(M))$ with the same diagonal $-2$.
It has the same rank as $G(M)$, because $\sigma$ maps each minor of $G(M)$ to the corresponding minor of $\sigma(G(M))$ and maps only $0$ to $0$.
Its signature can differ from that of $G(M)$.
Let $M$ be the rank-three Coxeter matrix with $m_{12} = 2$, $m_{13} = 3$, $m_{23} = 8$, so that, with $c \definedas 2\cos(\pi/8) = \sqrt{2+\sqrt2}$,
$$
G(M) = \begin{pmatrix} -2 & 0 & 1 \\ 0 & -2 & c \\ 1 & c & -2 \end{pmatrix},
\qquad
\det G(M) = 2c^2 - 6 = 2\sqrt2 - 2 > 0
.
$$
The base field is $K = \QQ(\sqrt{2+\sqrt2})$, which contains $\sqrt2 = c^2 - 2$, and there is $\sigma\in\gal(K/\QQ)$ with $\sigma(c) = \sqrt{2-\sqrt2}$, so $\sigma(\sqrt2) = -\sqrt2$.
Both forms are nondegenerate, and on the span of the first two basis vectors both restrict to $\operatorname{diag}(-2,-2)$, so each has a negative definite subspace of dimension $2$.
By @thm:sylvester each form has an orthogonal basis, in which its Gram matrix is $\operatorname{diag}(d_1,d_2,d_3)$, and $d_1d_2d_3$ differs from the determinant in the original basis by the square of a nonzero real number, so it has the same sign.
Since $\det G(M) > 0$ and at least two of the $d_i$ are negative, exactly two are, and $G(M)$ has signature $(1,2)$; it is hyperbolic in the sense of @def:coxeter-system-type.
Since $\det\sigma(G(M)) = 2\sigma(c)^2 - 6 = -2 - 2\sqrt2 < 0$, all three $d_i$ are negative, and $\sigma(G(M))$ is negative definite (@def:definiteness).
:::
