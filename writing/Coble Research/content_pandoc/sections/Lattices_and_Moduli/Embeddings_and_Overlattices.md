# Embeddings, overlattices, and gluing {#sec:embeddings-overlattices}

::: {.remark}

The basic vocabulary of lattices, primitive embeddings, orthogonal
complements, discriminant groups, and the unimodular lattices
$\latI_{p, q}$ and $\latII_{p, q}$ was fixed in \cref{sec:lattice-theory}.
We now develop the finer theory that underlies the lattice computations of
this monograph: the several equivalent characterizations of a primitive
sublattice, the classification of primitive embeddings up to isometry,
Nikulin's correspondence between overlattices and isotropic subgroups of the
discriminant form, the splitting of a unimodular sublattice off its ambient
lattice, the classification of unimodular lattices, the finiteness of the set
of primitive embeddings into an even unimodular lattice, and the behaviour of
the discriminant group under scaling.
Throughout, $S$, $T$, and $L$ denote nondegenerate lattices in the sense of
\cref{sec:lattice-theory}, $\beta$ denotes the ambient bilinear form when no
confusion can arise, and $A_L \da L\dual/L$ is the discriminant group with its
quadratic form $q_L$.
:::

## Primitive and saturated sublattices

::: {.definition title="Saturation" ref="def:saturation"}

Let $S\subseteq L$ be a sublattice.
The **saturation** of $S$ in $L$ is the sublattice
$$
\operatorname{Sat}_L(S) \da \ts{v\in L \mid nv\in S \text{ for some } n\in \ZZ\setminus\ts{0}}
.
$$
Equivalently, $\operatorname{Sat}_L(S) = S_\QQ\intersect L$, where
$S_\QQ \da S\otimes_\ZZ\QQ$ is regarded inside $L_\QQ$.
We say $S$ is **saturated** in $L$ if $S = \operatorname{Sat}_L(S)$.
:::

::: {.proposition title="Characterization of primitive sublattices" ref="prop:primitive-characterization"}

Let $S\subseteq L$ be a sublattice.
The following conditions are equivalent.

1.  The inclusion $S\injects L$ is a primitive embedding, i.e. $\coker(S\injects L)$
    is torsionfree.

2.  $S$ is saturated in $L$: $S = \operatorname{Sat}_L(S)$.

3.  $S_\QQ\intersect L = S$, where the intersection is taken in $L_\QQ$.

4.  $S$ is a direct summand of $L$ as a $\ZZ$-module, i.e. $L\cong S\oplus T$
    for some submodule $T\subseteq L$.

5.  Every $\ZZ$-basis of $S$ extends to a $\ZZ$-basis of $L$.

6.  Every $\ZZ$-linear functional $S\to\ZZ$ is the restriction of a $\ZZ$-linear
    functional $L\to\ZZ$.

7.  $S = (S^{\perp L})^{\perp L}$, the double orthogonal complement of $S$ in $L$.

A sublattice satisfying these conditions is called a **primitive sublattice**.
:::

::: {.proof}

We show $(1)\iff(2)$, $(2)\iff(3)$, $(2)\iff(4)\iff(5)\iff(6)$, and
$(2)\iff(7)$.

$(1)\iff(2)$: By definition $\coker(S\injects L) = L/S$, and $L/S$ is
torsionfree if and only if no nonzero element of $L/S$ is torsion.
An element $v + S$ is torsion in $L/S$ precisely when $nv\in S$ for some
nonzero $n\in\ZZ$, i.e. when $v\in\operatorname{Sat}_L(S)$.
Thus $L/S$ is torsionfree if and only if $\operatorname{Sat}_L(S) = S$.

$(2)\iff(3)$: This is the second description of the saturation recorded in
\cref{def:saturation}.
If $v\in S_\QQ\intersect L$, then $v = \sum_i (a_i/n) s_i$ with $s_i\in S$,
$a_i\in\ZZ$, and $n\in\ZZ\setminus\ts{0}$, so $nv\in S$ and
$v\in\operatorname{Sat}_L(S)$; conversely if $nv\in S$ then
$v = (nv)/n\in S_\QQ$, so $v\in S_\QQ\intersect L$.
Hence $\operatorname{Sat}_L(S) = S_\QQ\intersect L$, and $(2)$ and $(3)$ are the
same equation.

$(2)\Rightarrow(4)$: The quotient $L/S$ is a finitely generated $\ZZ$-module,
hence isomorphic to $\ZZ^k\oplus F$ with $F$ finite.
The torsion subgroup $F$ is exactly $\operatorname{Sat}_L(S)/S$, which vanishes
by $(2)$, so $L/S\cong\ZZ^k$ is free.
A short exact sequence $0\to S\to L\to L/S\to 0$ with $L/S$ free splits,
yielding $L\cong S\oplus T$ with $T\cong L/S$.

$(4)\Rightarrow(5)$: If $L\cong S\oplus T$, then the union of a $\ZZ$-basis of
$S$ and a $\ZZ$-basis of $T$ is a $\ZZ$-basis of $L$, so any basis of $S$
extends.

$(5)\Rightarrow(6)$: Fix a basis $e_1,\ldots,e_r$ of $S$, extended to a basis
$e_1,\ldots,e_r,e_{r+1},\ldots,e_n$ of $L$.
Given $\varphi\colon S\to\ZZ$, define $\tilde\varphi\colon L\to\ZZ$ by
$\tilde\varphi(e_i) = \varphi(e_i)$ for $i\le r$ and $\tilde\varphi(e_j) = 0$
for $j > r$; then $\tilde\varphi$ restricts to $\varphi$ on $S$.

$(6)\Rightarrow(2)$: Suppose $v\in\operatorname{Sat}_L(S)$ with $nv\in S$,
$n\ne 0$, but $v\notin S$.
Choose a $\ZZ$-basis $s_1,\ldots,s_r$ of $S$ and write $nv = \sum_i a_i s_i$
with $a_i\in\ZZ$.
Since $v\notin S$, some coefficient $a_i$ is not divisible by $n$; fix such an
$i$ and let $\varphi\colon S\to\ZZ$ be the coordinate functional dual to $s_i$,
so $\varphi(nv) = a_i$.
By $(6)$ there is $\tilde\varphi\colon L\to\ZZ$ restricting to $\varphi$, and
then $n\tilde\varphi(v) = \tilde\varphi(nv) = \varphi(nv) = a_i$, forcing
$n\mid a_i$, a contradiction.
Hence $\operatorname{Sat}_L(S) = S$.

$(2)\Rightarrow(7)$: In general $S\subseteq (S^{\perp L})^{\perp L}$ and the
right-hand side is saturated (it is cut out by the vanishing of rational linear
conditions, hence equals its own $\QQ$-span intersected with $L$).
Because $L$ is nondegenerate, $S$ and $(S^{\perp L})^{\perp L}$ have the same
$\QQ$-span, so $(S^{\perp L})^{\perp L} = S_\QQ\intersect L$.
If $S$ is saturated, this equals $S$.

$(7)\Rightarrow(2)$: If $S = (S^{\perp L})^{\perp L}$, then $S$ equals a double
orthogonal complement, which as just noted equals $S_\QQ\intersect L$; by
$(3)$ this is condition $(2)$.
:::

## Equivalence of embeddings

::: {.definition title="Equivalence of primitive embeddings" ref="def:embedding-equivalence"}

Two primitive embeddings $\iota_1\colon S\injects L_1$ and
$\iota_2\colon S\injects L_2$ are **equivalent** if there is an isometry
$f\in\operatorname{Isom}(L_1, L_2)$ with $f\circ\iota_1 = \iota_2$.
When $L_1 = L_2 = L$, two primitive embeddings
$\iota_1,\iota_2\colon S\injects L$ are **equivalent** if they are related in this
way by an element $f\in\Orth(L)$.
The set of equivalence classes of primitive embeddings of $S$ into a fixed
lattice $L$ is denoted $\operatorname{Emb}(S, L)$.
:::

::: {.remark}

Since an equivalence identifies $\iota_1(S)$ with $\iota_2(S)$ as sublattices of
$L$, describing $\operatorname{Emb}(S, L)$ amounts to classifying the
$\Orth(L)$-orbits of primitive sublattices of $L$ isometric to $S$, together
with the choice of isometry onto each such sublattice.
This is the object controlled by the gluing theory of the next subsection and
made finite, in the even unimodular case, by
\cref{prop:embedding-finiteness}.
:::

## Overlattices and gluing

::: {.definition title="Overlattice" ref="def:overlattice"}

An **overlattice** of a lattice $S$ is a lattice $L$ containing $S$ as a
finite-index sublattice, with $\ro{\beta_L}{S} = \beta_S$.
Equivalently, $L$ is a lattice with $S\subseteq L\subseteq S\dual$, where the
inclusions use the canonical map $S\injects S\dual$ of \cref{sec:lattice-theory}
and its dual; the finite quotient $L/S$ is then a subgroup of
$A_S = S\dual/S$.
:::

::: {.theorem title="Nikulin's gluing correspondence" ref="thm:nikulin-gluing"}

Let $S$ be an even lattice.
There is a bijection
$$
\ts{\text{even overlattices } L \text{ of } S}
\;\longleftrightarrow\;
\ts{\text{isotropic subgroups } H\le A_S}
$$
between the set of even overlattices of $S$ and the set of subgroups $H\le A_S$
on which the discriminant quadratic form $q_S$ vanishes identically.
The bijection sends an overlattice to the isotropic subgroup it cuts out, and
an isotropic subgroup to the overlattice it glues:
$$
\begin{aligned}
L &\longmapsto H_L \da L/S \subseteq A_S, \\
H &\longmapsto \eta^{-1}(H)\subseteq S\dual,
\end{aligned}
$$
where $\eta\colon S\dual\to A_S$ is the quotient map.
Under this correspondence,
$$
[L : S] = \abs{H}, \qquad
A_L \cong H^{\perp}/H, \qquad
\operatorname{disc} L = \frac{\operatorname{disc} S}{\abs{H}^2},
$$
where $H^{\perp}\le A_S$ is the orthogonal complement of $H$ with respect to
$q_S$.
Two even overlattices $L$, $L'$ of $S$ are isometric by an isometry restricting
to an element of $\Orth(S)$ if and only if $H_L$ and $H_{L'}$ are conjugate
under the image of $\Orth(S)$ in $\Orth(q_S)$.
:::

::: {.proof}

Any lattice $L$ intermediate between $S$ and $S\dual$ contains $S$ with finite
index, and the pairing $\beta_S$ extends to $L$ with integer values precisely
when the image $H_L = L/S\subseteq A_S$ is isotropic for $q_S$: for
$x + S, y + S\in H_L$ one has $\beta_{S_\QQ}(x, y)\in\ZZ$ if and only if the
associated bilinear form on $A_S$ vanishes on $H_L$, and evenness of $L$
requires in addition $q_S(x + S) = 0$ for all $x + S\in H_L$.
Conversely, given an isotropic $H\le A_S$, the preimage $\eta^{-1}(H)\subseteq
S\dual$ is an even overlattice of $S$ with $\eta^{-1}(H)/S = H$; the two
constructions are mutually inverse.

For the numerical statements, $[L:S] = \abs{L/S} = \abs{H}$.
Since $\operatorname{disc}$ scales by the square of the index under passage to a
finite-index sublattice, $\operatorname{disc} S = [L:S]^2\operatorname{disc} L =
\abs{H}^2\operatorname{disc} L$, giving the displayed formula.
Finally, the discriminant form of $L$ is computed on
$L\dual/L$; one has $L\dual = \eta^{-1}(H^{\perp})$ inside $S_\QQ$, whence
$A_L = L\dual/L \cong H^{\perp}/H$.

The orbit statement is immediate from the definitions: an isometry of $S$
extends to an isometry of $S\dual$ and hence acts on $A_S$ through the natural
map $\Orth(S)\to\Orth(q_S)$, carrying the overlattice attached to $H$ to the one
attached to its image.
:::

::: {.remark ref="rmk:embedding-gluing-data"}

The correspondence of \cref{thm:nikulin-gluing} is the engine behind the
classification of primitive embeddings.
A primitive embedding $S\injects L$ with orthogonal complement $T\da S^{\perp L}$
realizes $L$ as an even overlattice of the orthogonal direct sum $S\oplus T$,
whose discriminant group is $A_S\oplus A_T$ by the additivity recorded in
\cref{sec:lattice-theory}.
The corresponding isotropic subgroup $H\le A_S\oplus A_T$ is the graph of an
isometry $\gamma\colon H_S\xrightarrow{\sim} H_T$ between subgroups
$H_S\le A_S$ and $H_T\le A_T$, anti-isometric for the two discriminant forms; the
embedding is thus determined by the gluing data $(H_S, H_T, \gamma)$.
Comparing discriminants across the overlattice $L$ of $S\oplus T$ gives the
**discriminant formula**
$$
\abs{\operatorname{disc} T} = \frac{\abs{\operatorname{disc} L}\cdot\abs{H}^2}{\abs{\operatorname{disc} S}},
\qquad H\da H_L,
$$
recovering, when $L$ is unimodular, the statement that
$\abs{\operatorname{disc} T} = \abs{\operatorname{disc} S}$ and that $H_S = A_S$,
$H_T = A_T$ so that $\gamma\colon A_S\xrightarrow{\sim} A_T$ is an isometry onto
$A_T$ equipped with the negated form; see \cref{prop:embedding-finiteness}.
The framework and these formulas are due to Nikulin [@Nik80 §1.4--1.5].
:::

## Splitting of unimodular sublattices

::: {.definition title="Splitting" ref="def:lattice-split"}

Let $S\injects L$ be a primitive embedding with orthogonal complement
$T\da S^{\perp L}$.
We say $S$ **splits** $L$ if $L = S\oplus T$; equivalently, if $L$ is the
trivial index-$1$ overlattice of $S\oplus T$, i.e. the isotropic subgroup
$H_L\le A_{S\oplus T}$ of \cref{thm:nikulin-gluing} is the zero group.
:::

::: {.proposition title="Unimodular sublattices split" ref="prop:unimodular-splits"}

Let $S$ be a unimodular lattice admitting a primitive embedding into a
nondegenerate lattice $L$, and let $T\da S^{\perp L}$ be its orthogonal
complement.
Then $S$ splits $L$:
$$
L \cong S\oplus T
.
$$
Moreover, if $L$ is unimodular then $T$ is unimodular as well.
:::

::: {.proof}

First observe that $S\intersect T = \ts{0}$: any $x\in S\intersect T$ satisfies
$\beta_L(x, S) = 0$, and since $S$ is nondegenerate this forces $x = 0$.
Thus the sum $S + T$ inside $L$ is direct, giving an inclusion
$S\oplus T\subseteq L$.

We show this inclusion is an equality.
Let $x\in L$ be arbitrary and consider the functional
$\ro{\beta_L(x,\,\cdot\,)}{S}\colon S\to\ZZ$.
Since $S$ is unimodular, the canonical map $S\to S\dual$ is an isomorphism, so
there exists $s\in S$ with $\beta_L(x, y) = \beta_S(s, y)$ for all $y\in S$; that
is, $\beta_L(x - s, S) = 0$, so $x - s\in T$.
Hence $x = s + (x - s)\in S\oplus T$, and $L = S\oplus T$, which is the first
claim.

For the second claim, $L = S\oplus T$ gives
$\operatorname{disc} L = \operatorname{disc} S\cdot\operatorname{disc} T$.
When $L$ is unimodular, $\operatorname{disc} L = \pm 1$, and since $S$ is
unimodular with $\operatorname{disc} S = \pm 1$ we obtain
$\operatorname{disc} T = \pm 1$, so $T$ is unimodular.
:::

::: {.lemma title="Divisibility of isotropic vectors in unimodular lattices" ref="lem:unimodular-divisibility"}

Let $L$ be a nondegenerate unimodular lattice and let $v\in L$ be a primitive
isotropic vector.
Then there exists $w\in L$ with $\beta_L(v, w) = 1$.
In particular $\operatorname{div}_L(v) = 1$ for every primitive vector $v\in L$.
:::

::: {.proof}

Since $L$ is unimodular, the canonical map $L\to L\dual$ is an isomorphism, so
every functional in $L\dual = \Hom_\ZZ(L, \ZZ)$ has the form
$\beta_L(u,\,\cdot\,)$ for a unique $u\in L$.
Because $v$ is primitive, by \cref{prop:primitive-characterization} it extends to
a $\ZZ$-basis $e_1 = v, e_2,\ldots,e_n$ of $L$.
Let $\varphi\colon L\to\ZZ$ be the dual-basis functional with $\varphi(v) = 1$
and $\varphi(e_j) = 0$ for $j > 1$.
Writing $\varphi = \beta_L(w,\,\cdot\,)$ for the corresponding $w\in L$ and using
symmetry gives $\beta_L(v, w) = \beta_L(w, v) = \varphi(v) = 1$.
For the divisibility statement, the image $\beta_L(v, L) = \operatorname{div}_L(v)\ZZ$
contains $\beta_L(v, w) = 1$, so $\operatorname{div}_L(v) = 1$.
:::

::: {.corollary title="Hyperbolic splitting of unimodular lattices" ref="cor:hyperbolic-splitting"}

Let $L$ be a nondegenerate unimodular lattice containing a primitive isotropic
vector.
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
By \cref{lem:unimodular-divisibility} choose $w\in L$ with
$\beta_L(e, w) = 1$, and set $k\da w^2$.
The sublattice $P\da\gens{e, w}$ has Gram matrix
$\begin{bmatrix}0 & 1\\ 1 & k\end{bmatrix}$ of determinant $-1$, hence
$P$ is a rank-$2$ unimodular sublattice, and it is primitive since a unimodular
sublattice is saturated by \cref{prop:primitive-characterization}.
The isometry type of $P$ is governed by the parity of $k = w^2$: the Gram
matrix $\begin{bmatrix}0 & 1\\ 1 & k\end{bmatrix}$ gives $P\cong U$ when $k$ is
even and $P\cong\latI_{1, 1}$ (the odd rank-$2$ unimodular hyperbolic lattice)
when $k$ is odd.
We adjust $w$ within its coset to realize the parity dictated by $L$; note that
adding to $w$ any vector of $\gens{e}^{\perp L}$ preserves $\beta_L(e, w) = 1$.

If $L$ is even then $k = w^2$ is even; replacing $w$ by $w - \tfrac{k}{2}e$
(and $e\in\gens{e}^{\perp L}$ since $e^2 = 0$) leaves $\beta_L(e, w) = 1$
unchanged and makes $w^2 = 0$, so $P\cong U$.

If $L$ is odd we arrange $w^2$ to be odd, so that $P\cong\latI_{1, 1}$.
Every $x\in L$ satisfies $x - \beta_L(e, x)\,w\in\gens{e}^{\perp L}$, so
$L = \gens{e}^{\perp L} + \ZZ w$.
Were $\gens{e}^{\perp L}$ to consist entirely of even-norm vectors and $w^2$
even, every $x = y + mw$ ($y\in\gens{e}^{\perp L}$) would have
$x^2 = y^2 + 2m\,\beta_L(y, w) + m^2 w^2$ even, forcing $L$ even --- contrary to
hypothesis.
Hence either $w^2$ is already odd, or $\gens{e}^{\perp L}$ contains a vector $u$
of odd norm; in the latter case replace $w$ by $w + u$, which preserves
$\beta_L(e, w) = 1$ and gives $(w + u)^2 = w^2 + 2\beta_L(w, u) + u^2$ odd.
Either way $k = w^2$ is odd and $P\cong\latI_{1, 1}$.

Since $P$ is unimodular, \cref{prop:unimodular-splits} gives
$L\cong P\oplus P^{\perp L}$.
:::

## Classification of unimodular lattices

::: {.theorem title="Classification of indefinite unimodular lattices" ref="thm:indefinite-unimodular-classification"}

Any indefinite unimodular lattice is determined up to isometry by its rank,
index, and parity.
Explicitly, an indefinite unimodular lattice of signature $(p, q)$ is isometric
to $\latI_{p, q} = \gens{1}^{\oplus p}\oplus\gens{-1}^{\oplus q}$ if it is odd,
and to $\latII_{p, q}$ (which requires $p - q\equiv 0\pmod 8$) if it is even.
The same uniqueness by rank, index, and parity holds for definite unimodular
lattices of rank at most $8$.
:::

::: {.theorem title="Classification of small unimodular lattices" ref="thm:small-unimodular-classification"}

Let $L$ be any unimodular lattice, definite or indefinite, with
$\operatorname{rank}_\ZZ L\le 4$.
Then either

1.  $L$ is odd and $L\cong\latI_{p, q}$ for some $(p, q)$ with $p + q =
    \operatorname{rank}_\ZZ L$, or

2.  $L$ is even and $L\cong U$ or $L\cong U^{\oplus 2}$.
:::

::: {.remark}

The indefinite classification is Serre's theorem on integral quadratic forms
[@Ser73 Ch.\ V]; the uniqueness statement for definite unimodular lattices of
small rank, and the $\operatorname{rank}\le 4$ enumeration, are classical and
may be found in Milnor--Husem\"oller [@MH73 Ch.\ II] and in Conway--Sloane
[@CS10 Ch.\ 15].
The even case is especially rigid: in the range $\operatorname{rank}_\ZZ L\le 4$
the only even unimodular lattices are $U$ (rank $2$) and $U^{\oplus 2}$ (rank
$4$), there being no even unimodular lattice of odd rank and none of rank $0$
other than the zero lattice.
The constraint $p - q\equiv 0\pmod 8$ for $\latII_{p, q}$ reflects the fact that
the signature of an even unimodular lattice is divisible by $8$.
:::

## Finiteness of embeddings

::: {.proposition title="Finiteness of embeddings into even unimodular lattices" ref="prop:embedding-finiteness"}

If $S$ and $L$ are even lattices and $L$ is unimodular, then
$\operatorname{Emb}(S, L)$ is a finite set.
:::

::: {.proof}

By \cref{prop:unimodular-splits} and \cref{rmk:embedding-gluing-data}, a
primitive embedding $S\injects L$ into an even unimodular $L$ is equivalent to
the data of its orthogonal complement $T\da S^{\perp L}$ together with an
isometry
$$
\gamma\colon A_S\xrightarrow{\;\sim\;} A_T(-1),
$$
because unimodularity of $L$ forces the gluing subgroup to be the whole graph of
$\gamma$ (equivalently $H_S = A_S$, $H_T = A_T$).
Two such embeddings are equivalent in $\operatorname{Emb}(S, L)$ if and only if
the corresponding $\gamma$ differ by the action of $\Orth(q_T)$; the equivalence
class therefore depends only on the isometry class of $T$ and on a
$\Orth(q_T)$-orbit of isometries $A_S\xrightarrow{\sim} A_T(-1)$.

Each ingredient is finite.
The discriminant groups $A_S$ and $A_T$ are finite abelian groups, so the set
$\operatorname{Isom}(A_S, A_T(-1))$ of discriminant-form isometries and the
group $\Orth(q_T)$ are finite.
The isometry class of $T$ is constrained to a fixed genus in the sense of
\cref{def:genus} (its signature is $\operatorname{sign} L - \operatorname{sign} S$
and its discriminant form is $-q_S$), and a genus of lattices contains only
finitely many isometry classes; equivalently, the class group
$\operatorname{cl}(T)$ of \cref{def:genus} is finite.
A finite union of finite sets of $\Orth(q_T)$-orbits is finite, so
$\operatorname{Emb}(S, L)$ is finite.
:::

## The exact sequence for scaled lattices

::: {.proposition title="Discriminant group of a scaled lattice" ref="prop:scaled-discriminant-ses"}

Let $L$ be a lattice and $m$ a positive integer, and let $L(m)$ be the twist of
$L$ by $m$ (\cref{sec:lattice-theory}).
There is a short exact sequence of finite abelian groups
$$
0 \to L/mL \to A_{L(m)} \to A_L \to 0
.
$$
In particular, if $L$ is unimodular then $A_L = 0$ and
$A_{L(m)}\cong L/mL\cong(\ZZ/m\ZZ)^{\operatorname{rank} L}$.
:::

::: {.proof}

The underlying module of $L(m)$ is $L$, with form $\beta_{L(m)} = m\beta_L$.
Consequently the canonical map $\iota_{L(m)}\colon L(m)\to L(m)\dual$ is
$m$ times the canonical map $\iota_L\colon L\to L\dual$ after the identification
$L(m)\dual\cong L\dual$ of underlying modules.
Thus $L(m)\dual\cong L\dual$ and the image of $L(m)$ inside $L(m)\dual$ is
$m\iota_L(L)$.
The discriminant group is
$$
A_{L(m)} = L(m)\dual/L(m) \cong L\dual/mL
.
$$
The inclusion $mL\subseteq L\subseteq L\dual$ then yields the short exact
sequence
$$
0 \to L/mL \to L\dual/mL \to L\dual/L \to 0,
$$
which is the claimed sequence $0\to L/mL\to A_{L(m)}\to A_L\to 0$.
If $L$ is unimodular then $\iota_L$ is an isomorphism, so $A_L = 0$ and
$A_{L(m)}\cong L/mL\cong(\ZZ/m\ZZ)^{\operatorname{rank} L}$.
:::

::: {.proposition title="The orthogonal group exact sequence" ref="prop:orthogonal-group-ses"}

Let $L$ be a lattice.
Every isometry $f\in\Orth(L)$ extends by functoriality to an isometry of
$L\dual$ and hence induces an automorphism of the discriminant form $A_L$,
defining a group homomorphism
$$
\psi\colon\Orth(L)\to\Orth(q_L)
.
$$
Writing $\tilde\Orth(L)\da\ker\psi$ for the **stable orthogonal group** of $L$
(\cref{sec:lattice-theory}) and $\Orth^*(q_L)\da\coker\psi$, there is an exact
sequence
$$
0 \to \tilde\Orth(L) \to \Orth(L) \xrightarrow{\;\psi\;} \Orth(q_L) \to \Orth^*(q_L) \to 0
.
$$
:::

::: {.remark}

The cokernel $\Orth^*(q_L)$ measures the obstruction to lifting an automorphism
of the discriminant form $q_L$ to an isometry of $L$.
By Nikulin's surjectivity criterion, $\psi$ is surjective, i.e.
$\Orth^*(q_L) = 0$, whenever $L$ is indefinite and
$$
\ell(A_L) + 2 \le \operatorname{rank} L,
$$
where $\ell(A_L)$ is the length of \cref{def:discriminant-forms}, i.e. the
minimal number of generators of $A_L$ [@Nik80 Cor.\ 1.5.2, Thm.\ 1.14.2].
For a unimodular lattice such as $U$ or $E_8$ the discriminant group is trivial,
so $\Orth(q_L) = 0$ and $\tilde\Orth(L) = \Orth(L)$; the same triviality
underlies the surjectivity statement invoked for $\lkt$ in
\cref{lem:sequence_of_embeddings}.
:::
