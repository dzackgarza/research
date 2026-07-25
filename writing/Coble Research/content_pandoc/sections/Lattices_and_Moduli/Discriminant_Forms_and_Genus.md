# Discriminant forms and the genus

::: {.remark}

The Lattice Theory section introduced the dual lattice $L\dual$, the
discriminant group $A_L \da L\dual/L$, and the discriminant quadratic form
$q_L: A_L \to \QQ/2\ZZ$ of an even lattice.
We now develop the theory these constructions specialize: the general
correspondence between symmetric bilinear forms and quadratic forms, its
torsion-valued counterpart, the resulting structure on $A_L$, the properties of
the dual lattice, and the classification of lattices up to genus.
Throughout, $(L, \beta_L)$ denotes a lattice in the sense of the Lattice Theory
section, with $L_\QQ \da L\otimes_\ZZ \QQ$ and $\beta_{L_\QQ}$ the $\QQ$-linear
extension of $\beta_L$.
:::

## Quadratic forms and the polarization identity

::: {.definition ref="def:quadratic-form"}

A **quadratic form** on a $\ZZ$-module $L$ is a map of sets $q: L \to \QQ$ such
that $q(\lambda v) = \lambda^2 q(v)$ for all $v\in L$ and all $\lambda\in\ZZ$,
and whose **polar form** $\beta_q$ is a symmetric bilinear form on $L$:
$$
\begin{aligned}
\beta_q: L \otimes_\ZZ L &\to \QQ \\
(v, w) &\mapsto \beta_q(v, w) \da q(v+w) - q(v) - q(w)
.
\end{aligned}
$$
We say $q$ is **integral** if $q(L) \subseteq \ZZ$, and we call the pair
$(L, q)$ a **quadratic $\ZZ$-module**.
:::

::: {.remark}

Setting $w = v$ in the polar form and using homogeneity gives
$$
\beta_q(v, v) = q(2v) - 2q(v) = 4q(v) - 2q(v) = 2q(v)
,
$$
so that $q(v) = \tfrac{1}{2}\beta_q(v, v)$.
The polar form is thus always **even**, meaning $\beta_q(v, v)\in 2\ZZ$ whenever
$q$ is integral.
This identity is the source of the bijection recorded below.
:::

## The correspondence between bilinear and quadratic forms

::: {.lemma ref="lem:bilinear-quadratic-correspondence"}

Every $\QQ$-valued symmetric bilinear module $(L, \beta)$ determines a
$\QQ$-valued quadratic module $(L, q_\beta)$ by
$$
q_\beta(v) \da \beta(v, v)
,
$$
and $q_\beta$ depends only on the symmetric part of $\beta$.
Conversely, every $\QQ$-valued quadratic module $(L, q)$ determines a symmetric
bilinear module $(L, \beta_q)$ via its polar form of \cref{def:quadratic-form}.
:::

::: {.lemma ref="lem:even-lattice-bijection"}

There is a bijection between even symmetric integral bilinear forms on $L$ and
integral quadratic forms on $L$:
$$
\ts{ \beta\in \Sym^2_\ZZ(L\dual) \mid \beta \text{ is even} }
\quad\longleftrightarrow\quad
\Quad_\ZZ(L)
,
$$
under which a bilinear form $\beta$ is sent to
$q(v) \da \tfrac{1}{2}\beta(v, v)$, and a quadratic form $q$ is sent to its
polar form $\beta_q$.
Note that this forward map $\beta\mapsto\tfrac{1}{2}\beta(v,v)$ differs by the
factor $\tfrac{1}{2}$ from the map $\beta\mapsto q_\beta(v) = \beta(v,v)$ of
\cref{lem:bilinear-quadratic-correspondence}, so this bijection is a distinct
construction rather than a restriction of that lemma; only the backward
(polar-form) direction is shared.
Concretely, the polar form of any integral quadratic form is an even
symmetric integral bilinear form, and conversely every even symmetric integral
bilinear form $\beta$ is the polar form of the integral quadratic form
$q(v) \da \tfrac{1}{2}\beta(v, v)$.
:::

::: {.proof}

If $q$ is integral then $\beta_q(v, v) = 2q(v)\in 2\ZZ$, so $\beta_q$ is even
and integral.
Conversely, if $\beta$ is even and integral then
$q(v) \da \tfrac{1}{2}\beta(v, v)$ takes values in $\ZZ$, and its polar form
recovers $\beta$:
$$
\beta_q(v, w)
= q(v + w) - q(v) - q(w)
= \tfrac{1}{2}\left( \beta(v + w, v + w) - \beta(v, v) - \beta(w, w) \right)
= \beta(v, w)
,
$$
using symmetry of $\beta$.
The two assignments are mutually inverse.
:::

## Torsion bilinear and quadratic forms

::: {.definition ref="def:torsion-forms"}

A **torsion bilinear form** is a pair $(G, \beta)$ where $G$ is a finitely
generated torsion $\ZZ$-module and
$$
\beta: G \otimes_\ZZ G \to \QQ/\ZZ
$$
is a symmetric bilinear form.
A **torsion quadratic form** is a pair $(G, q)$ where $G$ is a finitely
generated torsion $\ZZ$-module and $q: G \to \QQ/\ZZ$ is a quadratic form,
i.e. $q(\lambda x) = \lambda^2 q(x)$ for all $x\in G$ and $\lambda\in\ZZ$, whose
polar form is a torsion bilinear form.
:::

::: {.remark}

The discriminant group $A_L$ of the Lattice Theory section is a finite, hence
finitely generated torsion, $\ZZ$-module, so its associated forms are instances
of this notion.
We record the discriminant data as two separate forms: the discriminant
quadratic form $q_L\colon A_L\to\QQ/2\ZZ$ (matching the $\QQ/2\ZZ$ normalization
of the Lattice Theory section) and the discriminant bilinear form
$b_L\colon A_L\times A_L\to\QQ/\ZZ$.
These share the numerator $\beta(\tilde x,\tilde y)$ read modulo different
lattices; the diagonal $q_L(\bar x) = \beta(\tilde x,\tilde x)\bmod 2\ZZ$
reduces to $b_L(\bar x,\bar x) = \beta(\tilde x,\tilde x)\bmod\ZZ$ under the
natural surjection $\QQ/2\ZZ\twoheadrightarrow\QQ/\ZZ$, not under any
multiplication-by-$2$ isomorphism.
:::

## The discriminant bilinear and quadratic forms

::: {.definition ref="def:discriminant-forms"}

Let $(L, \beta_L)$ be a nondegenerate even lattice with discriminant group
$A_L = L\dual/L$, and let $\beta$ also denote the $\QQ$-valued extension of the
form to $L\dual$.
The **discriminant bilinear form** of $L$ is the torsion bilinear form
$$
\begin{aligned}
b_L: A_L \times A_L &\to \QQ/\ZZ \\
(\bar x, \bar y) &\mapsto \beta(x, y) \bmod \ZZ
,
\end{aligned}
$$
computed on any lifts $x, y\in L\dual$ of $\bar x, \bar y$.
Its associated **discriminant quadratic form** is
$$
q_L(\bar x) \da \beta(x, x) \bmod 2\ZZ \in \QQ/2\ZZ
,
$$
for any lift $x$ of $\bar x$; this is the $\QQ/2\ZZ$-valued form $q_L$ recalled
from the Lattice Theory section.
Reducing modulo $\ZZ$ recovers the diagonal of $b_L$, i.e.
$q_L(\bar x)\bmod\ZZ = b_L(\bar x,\bar x)$, via the surjection
$\QQ/2\ZZ\twoheadrightarrow\QQ/\ZZ$.
The **orthogonal group** $\Orth(A_L)$ is the group of automorphisms of $A_L$
preserving $q_L$.
The **length** $\ell(L)$ of $L$ is the minimal number of generators of the
abelian group $A_L$.
:::

::: {.remark}

Both $b_L$ and $q_L$ are well defined: replacing a lift $x$ by $x + m$ with
$m\in L$ changes $\beta(x, y)$ by $\beta(m, y)\in\ZZ$ (so $b_L$ is well defined
modulo $\ZZ$) and changes $\beta(x, x)$ by
$\beta(2x, m) + \beta(m, m)\in 2\ZZ$ (so $q_L$ is well defined modulo $2\ZZ$),
since $\beta(L\dual, L)\subseteq\ZZ$ and $L$ is even.
These forms are Nikulin's discriminant forms [@Nik80].
:::

::: {.proposition ref="prop:discriminant-nondegenerate"}

The discriminant forms $b_L$ and $q_L$ of a nondegenerate lattice $L$ are
themselves nondegenerate, meaning that $b_L(\bar x, \,\cdot\,) = 0$ in
$\Hom(A_L, \QQ/\ZZ)$ implies $\bar x = 0$.
For any $\bar x, \bar y\in A_L$ the $\QQ/\ZZ$-valued bilinear form is recovered
from the $\QQ/2\ZZ$-valued quadratic form by
$$
b_L(\bar x, \bar y)
= \tfrac{1}{2}\left( q_L(\bar x + \bar y) - q_L(\bar x) - q_L(\bar y) \right)
,
$$
where the bracketed difference lies in $\QQ/2\ZZ$ and equals
$2\beta(\tilde x, \tilde y)\bmod 2\ZZ$; halving this even representative yields a
well-defined element $\beta(\tilde x, \tilde y)\bmod\ZZ$ of $\QQ/\ZZ$.
:::

::: {.proof}

Nondegeneracy is the statement that the induced map
$A_L \to \Hom(A_L, \QQ/\ZZ)$ is an isomorphism; this holds because $A_L$ is
finite and the pairing $b_L$ is the pairing induced by the perfect pairing
$L\dual/L \times L\dual/L \to \QQ/\ZZ$ coming from a nondegenerate $\beta_L$.
The polarization identity is the reduction modulo $\ZZ$ of the identity
$\beta(x, y) = \tfrac{1}{2}(\beta(x + y, x + y) - \beta(x, x) - \beta(y, y))$ on
lifts.
:::

## Properties of the dual lattice

::: {.proposition ref="prop:dual-properties"}

Let $L$ and $M$ be nondegenerate lattices.
The dual lattice $L\dual = \Hom_\ZZ(L, \ZZ)$ satisfies the following.

1.  Duality commutes with orthogonal direct sums:
    $(L\oplus M)\dual = L\dual \oplus M\dual$.

2.  If $L$ has Gram matrix $G_\beta$ in a basis $B_L$, then the dual basis is
    $B_{L\dual} = (B_L^t)^{-1}$, and the Gram matrix of the dual form is
    $G_{\beta\dual} = G_\beta^{-1}$.

3.  The discriminant of the dual satisfies
    $\operatorname{disc}(L\dual) = 1/\operatorname{disc}(L)$.

4.  The dual of a twist is $(L(m))\dual = L\dual(1/m)$, where $L(m)$ is the
    twist of $L$ by $m$ from the Lattice Theory section.
:::

::: {.remark}

Property (2) is the source of (3), since
$\operatorname{disc}(L\dual) = \det(G_\beta^{-1}) = 1/\det(G_\beta)
= 1/\operatorname{disc}(L)$.
Property (1) is compatible with the direct-sum decomposition
$A_{L\oplus M} = A_L\oplus A_M$ of discriminant groups recalled in the Lattice
Theory section.
:::

## Geometric identification of the dual lattice

::: {.theorem ref="thm:dual-geometric-identification"}

For a nondegenerate integral lattice $(L, \beta_L)$, the dual lattice is
identified with a $\ZZ$-submodule of $L_\QQ = L\otimes_\ZZ\QQ$ via
$$
L\dual \;\cong\; \ts{ v\in L_\QQ \mid \beta_{L_\QQ}(v, L) \subseteq \ZZ }
,
$$
where a functional $\varphi\in L\dual$ corresponds to the unique vector
$v_\varphi\in L_\QQ$ such that $\varphi(w) = \beta_{L_\QQ}(v_\varphi, w)$ for all
$w\in L$.
Under this identification one has the chain of inclusions
$$
L \subseteq L\dual \subseteq L_\QQ
.
$$
:::

::: {.proof}

Nondegeneracy of $\beta_L$ makes the $\QQ$-linear extension
$L_\QQ \to \Hom_\QQ(L_\QQ, \QQ)$, $v\mapsto \beta_{L_\QQ}(v, \cdot)$, an
isomorphism, so each $\varphi\in L\dual \subseteq \Hom_\QQ(L_\QQ, \QQ)$ has a
unique preimage $v_\varphi\in L_\QQ$.
The condition $\varphi(L)\subseteq\ZZ$ translates to
$\beta_{L_\QQ}(v_\varphi, L)\subseteq\ZZ$, giving the stated image.
The inclusion $L\subseteq L\dual$ is the map $\iota$ of the Lattice Theory
section, and $L\dual\subseteq L_\QQ$ holds because the pairing takes rational
values.
:::

## The genus, class group, and class number

::: {.definition ref="def:genus"}

Two lattices $L_1, L_2$ belong to the same **genus** if
$L_{1, \ZZ_p} \cong L_{2, \ZZ_p}$ for every prime $p$, where
$L_{i, \ZZ_p} \da L_i\otimes_\ZZ \ZZ_p$, and $L_{1, \RR}\cong L_{2, \RR}$.
Lattices in the same genus share the same rank, signature, and determinant, but
need not be isometric over $\ZZ$.
The **class group** $\operatorname{cl}(L)$ is the set of isometry classes of
lattices in the genus of $L$, and the **class number** is the cardinality
$\abs{\operatorname{cl}(L)}$.
:::

::: {.remark}

For indefinite even lattices $L$ of rank $\geq 3$ the class number is $1$, so
that the genus determines the isometry class; this is Eichler's theorem on the
spinor genus of indefinite forms (see [@CS10] for a general reference).
For definite lattices the situation is reversed: class number $1$ is
comparatively rare.
:::

::: {.proposition ref="prop:scattone-bound"}

If $\operatorname{rank}(L) > 16 + \ell(L)$, where $\ell(L)$ is the length of
\cref{def:discriminant-forms}, then the class number satisfies
$\abs{\operatorname{cl}(L)} \geq 2$.
:::

::: {.proof}

This is the bound of [@Sca87].
:::
