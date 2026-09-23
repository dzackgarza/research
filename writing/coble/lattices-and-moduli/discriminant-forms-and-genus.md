# Discriminant forms and the genus

::: {.Remark}

The Lattice Theory section introduced the dual lattice $L\dual$, the
discriminant group $A_L \da L\dual/L$, and the discriminant quadratic form
$q_L: A_L \to \QQ/2\ZZ$ of an even lattice.
We now develop the theory these constructions specialize: the general
correspondence between symmetric bilinear forms and quadratic forms, its
torsion-valued counterpart, the resulting structure on $A_L$, the properties of
the dual lattice, and the classification of lattices up to genus.
Throughout, $(L, \beta_L)$ denotes a lattice in the sense of the Lattice Theory
section, with $L_\QQ \da L\tensor_\ZZ \QQ$ and $\beta_{L_\QQ}$ the $\QQ$-linear
extension of $\beta_L$.
:::

## Quadratic forms and the polarization identity

::: {.Definition #def:coble-quadratic-form}

A **quadratic form** on a $\ZZ$-module $L$ is a map of sets $q: L \to \QQ$ such
that $q(\lambda v) = \lambda^2 q(v)$ for all $v\in L$ and all $\lambda\in\ZZ$,
and whose **polar form** $\beta_q$ is a symmetric bilinear form on $L$:
$$
\begin{aligned}
\beta_q: L \tensor_\ZZ L &\to \QQ \\
(v, w) &\mapsto \beta_q(v, w) \da q(v+w) - q(v) - q(w)
.
\end{aligned}
$$
We say $q$ is **integral** if $q(L) \containedin \ZZ$, and we call the pair
$(L, q)$ a **quadratic $\ZZ$-module**.
:::

::: {.Remark}

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

::: {.Lemma #lem:coble-bilinear-quadratic-correspondence}

Every $\QQ$-valued symmetric bilinear module $(L, \beta)$ determines a
$\QQ$-valued quadratic module $(L, q_\beta)$ by
$$
q_\beta(v) \da \beta(v, v)
,
$$
and $q_\beta$ depends only on the symmetric part of $\beta$.
Conversely, every $\QQ$-valued quadratic module $(L, q)$ determines a symmetric
bilinear module $(L, \beta_q)$ via its polar form from [the quadratic-form definition](#def:coble-quadratic-form).
:::

::: {.Lemma #lem:coble-even-lattice-bijection}

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
[the bilinear/quadratic correspondence lemma](#lem:coble-bilinear-quadratic-correspondence), so this bijection is a distinct
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

::: {.Definition #def:coble-torsion-forms}

A **torsion bilinear form** is a pair $(G, \beta)$ where $G$ is a finitely
generated torsion $\ZZ$-module and
$$
\beta: G \tensor_\ZZ G \to \QQ/\ZZ
$$
is a symmetric bilinear form.
A **torsion quadratic form** is a pair $(G, q)$ where $G$ is a finitely
generated torsion $\ZZ$-module and $q: G \to \QQ/\ZZ$ is a quadratic form,
i.e. $q(\lambda x) = \lambda^2 q(x)$ for all $x\in G$ and $\lambda\in\ZZ$, whose
polar form is a torsion bilinear form.
:::

::: {.Remark}

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
natural surjection $\QQ/2\ZZ\surjects\QQ/\ZZ$, not under any
multiplication-by-$2$ isomorphism.
:::

## The discriminant bilinear and quadratic forms

::: {.Definition #def:coble-discriminant-forms}

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
$\QQ/2\ZZ\surjects\QQ/\ZZ$.
The **orthogonal group** $\Orth(A_L)$ is the group of automorphisms of $A_L$
preserving $q_L$.
The **length** $\ell(L)$ of $L$ is the minimal number of generators of the
abelian group $A_L$.
:::

::: {.Remark}

Both $b_L$ and $q_L$ are well defined: replacing a lift $x$ by $x + m$ with
$m\in L$ changes $\beta(x, y)$ by $\beta(m, y)\in\ZZ$ (so $b_L$ is well defined
modulo $\ZZ$) and changes $\beta(x, x)$ by
$\beta(2x, m) + \beta(m, m)\in 2\ZZ$ (so $q_L$ is well defined modulo $2\ZZ$),
since $\beta(L\dual, L)\containedin\ZZ$ and $L$ is even.
These forms are Nikulin's discriminant forms [@Nik80].
:::

::: {.Proposition #prop:discriminant-nondegenerate}

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

::: {.Proposition #prop:dual-properties}

Let $L$ and $M$ be nondegenerate lattices.
The dual lattice $L\dual = \Hom_\ZZ(L, \ZZ)$ satisfies the following.

1.  Duality commutes with orthogonal direct sums:
    $(L\oplus M)\dual = L\dual \oplus M\dual$.

2.  If $L$ has Gram matrix $G_\beta$ in a basis $B_L$, then the dual basis is
    $B_{L\dual} = (B_L^t)\inv$, and the Gram matrix of the dual form is
    $G_{\beta\dual} = G_\beta\inv$.

3.  The discriminant of the dual satisfies
    $\operatorname{disc}(L\dual) = 1/\operatorname{disc}(L)$.

4.  The dual of a twist is $(L(m))\dual = L\dual(1/m)$, where $L(m)$ is the
    twist of $L$ by $m$ from the Lattice Theory section.
:::

::: {.Remark}

Property (2) is the source of (3), since
$\operatorname{disc}(L\dual) = \det(G_\beta\inv) = 1/\det(G_\beta)
= 1/\operatorname{disc}(L)$.
Property (1) is compatible with the direct-sum decomposition
$A_{L\oplus M} = A_L\oplus A_M$ of discriminant groups recalled in the Lattice
Theory section.
:::

## Geometric identification of the dual lattice

::: {.Theorem #thm:dual-geometric-identification}

For a nondegenerate integral lattice $(L, \beta_L)$, the dual lattice is
identified with a $\ZZ$-submodule of $L_\QQ = L\tensor_\ZZ\QQ$ via
$$
L\dual \;\cong\; \ts{ v\in L_\QQ \mid \beta_{L_\QQ}(v, L) \containedin \ZZ }
,
$$
where a functional $\varphi\in L\dual$ corresponds to the unique vector
$v_\varphi\in L_\QQ$ such that $\varphi(w) = \beta_{L_\QQ}(v_\varphi, w)$ for all
$w\in L$.
Under this identification one has the chain of inclusions
$$
L \containedin L\dual \containedin L_\QQ
.
$$
:::

::: {.proof}

Nondegeneracy of $\beta_L$ makes the $\QQ$-linear extension
$L_\QQ \to \Hom_\QQ(L_\QQ, \QQ)$, $v\mapsto \beta_{L_\QQ}(v, \cdot)$, an
isomorphism, so each $\varphi\in L\dual \containedin \Hom_\QQ(L_\QQ, \QQ)$ has a
unique preimage $v_\varphi\in L_\QQ$.
The condition $\varphi(L)\containedin\ZZ$ translates to
$\beta_{L_\QQ}(v_\varphi, L)\containedin\ZZ$, giving the stated image.
The inclusion $L\containedin L\dual$ is the map $\iota$ of the Lattice Theory
section, and $L\dual\containedin L_\QQ$ holds because the pairing takes rational
values.
:::

## The genus, class group, and class number

::: {.Definition #def:coble-genus}

Two lattices $L_1, L_2$ belong to the same **genus** if
$L_{1, \ZZ_p} \cong L_{2, \ZZ_p}$ for every prime $p$, where
$L_{i, \ZZ_p} \da L_i\tensor_\ZZ \ZZ_p$, and $L_{1, \RR}\cong L_{2, \RR}$.
Lattices in the same genus share the same rank, signature, and determinant, but
need not be isometric over $\ZZ$.
The **class group** $\operatorname{cl}(L)$ is the set of isometry classes of
lattices in the genus of $L$, and the **class number** is the cardinality
$\abs{\operatorname{cl}(L)}$.
:::

::: {.Remark}

For indefinite even lattices $L$ of rank $\geq 3$ the class number is $1$, so
that the genus determines the isometry class; this is Eichler's theorem on the
spinor genus of indefinite forms (see [@CS10] for a general reference).
For definite lattices the situation is reversed: class number $1$ is
comparatively rare.
:::

::: {.Proposition #prop:scattone-bound}

If $\rank(L) > 16 + \ell(L)$, where $\ell(L)$ is the length of
[the discriminant-form definition](#def:coble-discriminant-forms), then the class number satisfies
$\abs{\operatorname{cl}(L)} \geq 2$.
:::

::: {.proof}

This is the bound of [@Sca87].
:::

## Local invariants and the Jordan decomposition

::: {.Definition #def:scale-norm-volume}
### Scale, norm, and volume

Let $(L, \beta_L)$ be a lattice.
Its **scale** is the ideal generated by all pairings and its **norm** the ideal
generated by all squares,
$$
\mathfrak{s}(L) \da \gcd\ts{\beta_L(x, y) \mid x, y\in L}\,\ZZ,
\qquad
\mathfrak{n}(L) \da \gcd\ts{\beta_L(x, x) \mid x\in L}\,\ZZ
,
$$
and its **volume** is the index ideal
$\mathfrak{v}(L)\da\abs{\det G_L}\,\ZZ = \abs{A_L}\,\ZZ$.
One has $\mathfrak{n}(L)\containedin\mathfrak{s}(L)$, and $L$ is integral exactly
when $\mathfrak{s}(L)\containedin\ZZ$.
Under the twist of the Lattice Theory section,
$\mathfrak{s}(L(m)) = m\,\mathfrak{s}(L)$,
$\mathfrak{n}(L(m)) = m\,\mathfrak{n}(L)$ and
$\mathfrak{v}(L(m)) = m^{r}\,\mathfrak{v}(L)$ for $r = \rank(L)$.
:::

::: {.Definition #def:modular-lattice}
### Modular lattices

A lattice $L$ is **$m$-modular** if $m L\dual = L$; equivalently, $L$ is similar
to its dual.
A unimodular lattice is the case $m = 1$, and $L(m)$ is $m$-modular whenever $L$
is unimodular.
:::

::: {.Theorem #thm:jordan-decomposition}
### Jordan decomposition

Let $L$ be a nondegenerate lattice and $p$ a prime.
Then $L_{\ZZ_p} = L\tensor_\ZZ\ZZ_p$ admits an orthogonal decomposition
$$
L_{\ZZ_p} = L_1 \operatorname{\perp} L_2 \operatorname{\perp}\cdots\operatorname{\perp} L_k
,
$$
in which each $L_i$ is $p^{s_i}$-modular and $s_1 < s_2 < \cdots < s_k$.
Such a decomposition exists and is unique up to isometry, and the scales
$p^{s_i}$ and the ranks $\rank(L_i)$ are invariants of $L$ at $p$.
:::

::: {.Remark}

The Jordan invariants at every prime are exactly the data compared in
[the genus definition](#def:coble-genus): two lattices lie in the same genus precisely when they have
isometric Jordan decompositions at every prime and the same signature.
For a $2$-elementary lattice only the primes $2$ and the archimedean place carry
information, and the Jordan decomposition at $2$ is assembled from the rank-two
$2$-adic lattices $V_k$ and $U_k$ from [Nikulin's $V_k,U_k$ definition](#def:nikulin-Vk-Uk) together with
rank-one summands.
:::

## The mass formula as a class-number criterion

::: {.Definition #def:mass}
### The mass of a genus

Let $L$ be a positive definite lattice and let $L^{(1)}, \ldots, L^{(h)}$ be
representatives of the isometry classes in the genus of $L$, so that
$h = \abs{\operatorname{cl}(L)}$ in the notation of [the genus definition](#def:coble-genus).
The **mass** of the genus is
$$
m(L) \da \Sum_{i=1}^{h} \frac{1}{\abs{\Orth(L^{(i)})}}
.
$$
:::

::: {.Remark}
### The Smith--Minkowski--Siegel formula and its use

The mass is computable from local data alone: the Smith--Minkowski--Siegel mass
formula expresses $m(L)$ as a product of an archimedean factor and one $p$-adic
factor for each prime, each factor read off from the Jordan decomposition of
[the Jordan-decomposition theorem](#thm:jordan-decomposition); the explicit unimodular cases are tabulated in
[@CS10 Ch. 16].
Since each summand of [the mass definition](#def:mass) is positive, the formula gives a criterion
for class number one:
$$
m(L) = \frac{1}{\abs{\Orth(L)}}
\quad\Longleftrightarrow\quad
\abs{\operatorname{cl}(L)} = 1
.
$$
This is how the uniqueness of $E_8$ in rank $8$ is certified, the mass of the
genus of even unimodular lattices of rank $8$ being $1/\abs{\Orth(E_8)}$, and it
is the definite counterpart of the indefinite criterion recorded above.
:::

## Surjectivity onto the discriminant group

::: {.Theorem #thm:two-elementary-surjectivity}
### $\Orth(H)\to\Orth(A_H, q_H)$ is surjective for indefinite $2$-elementary $H$

Let $H$ be an indefinite even $2$-elementary lattice.
Then the natural homomorphism
$$
\Orth(H)\too\Orth(A_H, q_H)
$$
onto the isometry group of the discriminant form is surjective.
:::

::: {.proof}

This is [@Nik80]; see [@Ale22 §4] for the statement in this form.
:::

::: {.Remark}

Surjectivity is what makes the finite quadratic space $A_H$ a faithful shadow of
$\Orth(H)$, and it enters at three separate points below: it lifts an isometry of
one eigenlattice of an involution to an isometry of $\lkt$; it is the standing
hypothesis of the orbit algorithms of [@Daw22]; and it is what allows an orbit
question about primitive vectors of $H$ to be posed in $A_H$ at all.
It applies to $S_\Co$, $T_\Co$, $S_\En$, $T_\En$ and $T_\dP$, all of which are
indefinite even $2$-elementary.
:::

## Invariants that do not classify

::: {.Theorem #thm:milgram}
### Milgram's formula

Let $L$ be a nondegenerate even lattice with discriminant form
$q_L\colon A_L\to\QQ/2\ZZ$ and signature $(n_+, n_-)$.
Then
$$
\Sum_{\lambda\in A_L} e\!\left(\tfrac{1}{2}q_L(\lambda)\right)
= \sqrt{\abs{A_L}}\;
e\!\left(\frac{n_+ - n_-}{8}\right),
\qquad
e(z)\da e^{2\pi i z}
.
$$
In particular the discriminant form determines the index $n_+ - n_-$ modulo $8$.
:::

::: {.proof}

This is the Gauss-sum formula of [@MH73 Appendix 4].
:::

::: {.Remark}
### What each invariant determines

Milgram's formula is a constraint linking the two halves of the classifying data
of [the genus definition](#def:coble-genus); it is an invariant of the discriminant form alone.
It is an invariant of the discriminant form, so two even lattices with the same
discriminant form give the same Gauss sum whether or not they are isometric, and
it recovers the index only modulo $8$, whereas the pair $(n_+, n_-)$ is what the
genus needs.

Two weaker invariants are sometimes offered in place of the discriminant form and
do not classify.
The **Arf invariant** is defined for a quadratic form valued in $\bF_2$; the
reduction $q_L\bmod\ZZ$ of a discriminant form loses the $\QQ/2\ZZ$-valued
information that distinguishes, for example, $\gens{2}$ from $\gens{-2}$, so
lattices agreeing in Arf invariant need not be isometric.
The **Brown invariant**, valued in $\ZZ/8\ZZ$, is the bordism-theoretic shadow of
the index, and it records exactly what Milgram's formula supplies, namely
$n_+ - n_-$ modulo $8$.
For an even lattice the classifying data are the signature $(n_+, n_-)\in\ZZ^2$
together with the discriminant form $(A_L, q_L)$, which determine the genus
[@Nik80], and for the indefinite lattices of rank at least three considered here
the genus determines the isometry class.
:::

::: {.Remark}
### The consequence for complementary lattices

If $S\containedin\Lambda$ is primitive in an even unimodular $\Lambda$ with
complement $T = S^{\perp\Lambda}$, then $q_T\cong -q_S$ by
[the embedding-gluing description](#rmk:embedding-gluing-data), and applying [Milgram's formula](#thm:milgram) to both sides
gives the congruence
$$
\sign(S) + \sign(T)\equiv 0 \pmod 8
.
$$
This congruence follows from $q_T\cong -q_S$:
verifying the isometry of discriminant forms is a normal-form comparison of the
pairs $(A_S, q_S)$ and $(A_T, -q_T)$, and a matching Gauss sum is one numerical
shadow of that comparison.
:::

## Finiteness of orbits of vectors of fixed norm

::: {.Theorem #thm:finiteness-fixed-norm-orbits}
### Finitely many orbits in each norm

Let $L$ be an integral lattice and $n\in\ZZ$.
The set
$$
S_n \da \ts{ v\in L \mid v^2 = n }
$$
of representations of $n$ by $L$ decomposes into finitely many $\Orth(L)$-orbits.
:::

::: {.Remark}
### Why the statement is needed and where it comes from

For a definite lattice the statement is trivial, $S_n$ itself being finite.
The content is the indefinite case, where $S_n$ is typically infinite: it is the
assertion that the integral points of the affine quadric $\ts{v^2 = n}$ fall into
finitely many orbits under the arithmetic group $\Orth(L)$, and it belongs to the
classical theory of representations of an integer by an indefinite quadratic
form, where the mass-formula count of representations by the classes of a genus
is replaced by a count of orbits.

Finiteness is what makes the enumeration of cusps a well-posed finite problem:
it guarantees that the $0$-cusps and $1$-cusps of a Baily--Borel compactification
are finite in number before any of them is exhibited, and that an orbit
computation can terminate.
Under the hypothesis $U^{\oplus 2}\containedin L$ the Eichler criterion
([the Eichler criterion](#thm:eichler-criterion)) makes it effective, bounding the number of
$\widetilde{\SO}^+(L)$-orbits in $S_n$ by $\abs{A_L}$; without that hypothesis
finiteness still holds but a bound has to come from elsewhere.
:::
