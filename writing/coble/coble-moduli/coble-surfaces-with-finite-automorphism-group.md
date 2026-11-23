---
unit: reference
status: source-backed
tags:
  - coble
  - classification
  - automorphisms
  - roots
---

# Coble surfaces with finite automorphism group {#sec-coble-finite-automorphism}

Kondō classifies the Coble surfaces whose automorphism group is finite in characteristic $p\neq 2$: there are exactly nine of them up to isomorphism, and the nine are distinguished by the dual graph of their effective irreducible roots [@Kon21, Theorem 1.1].
This is the Coble analogue of the classification of complex Enriques surfaces with finite automorphism group by Nikulin and Kondō, and it replaces the Enriques lattice $\Num(Y)\iso E_{10}$ and the $(-2)$-curves on $Y$ by the Coble--Mukai lattice $\CM(S)$ of @def:coble-mukai-lattice and by effective irreducible roots.
Two things should be separated from the start: the classification is a statement about surfaces, not about plane models, and its finiteness input is the automorphism group of a single surface, not the monodromy of any family (@rmk:kondo-what-the-classification-does-not-decide).

## The classified objects

::: {.definition #def:strong-coble-surface title="Coble surface in the strong sense"}

Let $S$ be a smooth projective rational surface over a field $k$ with $\abs{-K_S}=\varnothing$.
Then $S$ is a **strong Coble surface** with boundary components $B_1,\ldots,B_n$ if
$$
\abs{-2K_S} = \theset{B_1+\cdots+B_n},
$$
where each $B_i$ is a nonsingular rational curve and $B_i\intersect B_j=\varnothing$ for $i\neq j$ [@Kon21, §1].
:::

::: {.proposition #prop:strong-coble-is-terminal-coble title="The classified objects are exactly the terminal Coble surfaces of K3 type"}

Let $S$ be a smooth projective rational surface with $\abs{-K_S}=\varnothing$ and $\abs{-2K_S}\neq\varnothing$.
Then $S$ is a strong Coble surface with $n$ boundary components in the sense of @def:strong-coble-surface if and only if it is a terminal Coble surface of K3 type with $n$ boundary components in the sense of @def:coble-surface.
In that case $B_i^2=-4$, $K_S\cdot B_i=2$, $K_S^2=-n$, $\rho(S)=10+n$, $n\le 10$, and there is a double cover $\pi\colon X\too S$ branched along $B_1+\cdots+B_n$ with $X$ a K3 surface [@Kon21, §1, §3; @DK25, Cor. 9.1.5, Prop. 6.4; @prop:terminal-coble-basic-rational].
:::

::: {.proof}

*From strong to terminal.* By hypothesis $\abs{-2K_S}$ has the single member $D=B_1+\cdots+B_n$, which is reduced because the $B_i$ are distinct prime divisors and they are pairwise disjoint.
Intersecting $D\sim-2K_S$ with $B_i$ gives $-2K_S\cdot B_i=B_i^2$, that is $B_i\cdot K_S=-\tfrac12B_i^2$; adjunction on the smooth rational curve $B_i$ gives $-2=B_i^2+B_i\cdot K_S$, and the two together give $B_i^2=-4$ and $B_i\cdot K_S=2$.
So $D$ is the only member of $\abs{-2K_S}$ and is a disjoint union of $(-4)$-curves, which is the terminal K3-type condition of @def:coble-surface.

*From terminal to strong.* Conversely, if $\abs{-2K_S}=\theset{D}$ with $D$ reduced and a disjoint union of smooth rational $(-4)$-curves, then naming the components $B_1,\ldots,B_n$ gives the strong Coble data, by the same numbering.

The numerical invariants and the bound are those of @prop:terminal-coble-basic-rational, and the double cover is [@Kon21, §1].

:::

The passage between the two vocabularies matters for reading Theorem 1.1: the hypothesis is *strong*, so a Coble surface whose anti-bicanonical member is non-reduced, or which has several anti-bicanonical members, is outside the classification however many or few automorphisms it has.
An object of the complex Coble stack $\mcM_\Co$ of @def:coble-moduli-functor has a single smooth anti-bicanonical curve, hence is strong and is classified by @thm:kondo-finite-aut-classification when its automorphism group is finite.

## The Coble--Mukai lattice and effective irreducible roots

::: {.proposition #prop:kondo-coble-mukai-is-e10 title="When the Coble--Mukai lattice is the Enriques lattice"}

Let $S$ be a strong Coble surface with $n$ boundary components.

1. If $n=1$ or $n=2$, then $\CM(S)\iso E_{10}$ [@Kon21, Proposition 3.1(1)].
2. If $k=\CC$, then $\CM(S)\iso E_{10}$ for every $n$ [@Kon21, Proposition 3.1(2)].

For $n=1$ the lattice $\CM(S)$ is $K_S^{\perp}$ inside $\Pic(S)$ [@Kon21, Proposition 3.1, proof], and it is the home of the classes of the $(-2)$-curves, which are disjoint from the boundary.
:::

::: {.definition #def:effective-irreducible-root title="Effective roots and irreducible effective roots"}

Let $S$ be a strong Coble surface.
An effective class $\alpha\in\CM(S)$ with $\alpha^2=-2$ is an **effective root**, and $\alpha$ is **irreducible** if $\abs{\alpha-\beta}=\varnothing$ for every other effective root $\beta$ [@Kon21, §3].
Since $\abs{-2K_S}=\theset{B_1+\cdots+B_n}$, the curves of negative self-intersection on $S$ are the boundary components and the $(-2)$- and $(-1)$-curves, so an effective irreducible root is either the class of a $(-2)$-curve or the class of a $(-1)$-curve boosted by half of two boundary components (@lem:effective-root-dichotomy).
The **dual graph** of a set of effective irreducible roots has that set as its vertex set and joins two vertices by a single edge when their intersection number is $1$, by $m$ lines when it is $m$ [@Kon21, §2].
:::

::: {.lemma #lem:effective-root-dichotomy title="The two kinds of effective irreducible root, and their intersection numbers"}

Let $S$ be a strong Coble surface with boundary components $B_1,\ldots,B_n$ and boundary classes $\beta_i$.

1. An effective irreducible root is either the class of a $(-2)$-curve on $S$, or has the form $2e+\tfrac12\beta_j+\tfrac12\beta_k$ where $E$ is a $(-1)$-curve meeting the two distinct boundary components $B_j$ and $B_k$ [@Kon21, Lemma 3.2].
   The second kind is called a $(-1)$-**root**.
2. For $(-1)$-roots $\alpha=2e+\tfrac12\beta_1+\tfrac12\beta_2$ and $\alpha'=2e'+\tfrac12\beta_1'+\tfrac12\beta_2'$,
$$
\alpha\cdot\alpha' = 4E\cdot E'+4-\abs{\theset{B_1,B_2,B_1',B_2'}},
$$
so $\alpha\cdot\alpha'=1$ if and only if $E$ and $E'$ are disjoint and the two roots share exactly one boundary component [@Kon21, Lemma 3.3(1)].
3. A $(-1)$-root meets a $(-2)$-root in an even number, since a $(-2)$-curve is disjoint from the boundary [@Kon21, Lemma 3.3(2)].
:::

::: {.proof}

(1) and (2) are [@Kon21, Lemma 3.2, Lemma 3.3] verbatim; since distinct boundary components are disjoint, $\tfrac12\beta_j\cdot\tfrac12\beta_k=0$ when $j\neq k$, while $\tfrac12\beta_j\cdot\tfrac12\beta_j=-1$. Thus the four half-boundary classes contribute $4$ minus the number of distinct boundary components.
For (3): $\alpha\cdot C=2e\cdot C$ for a $(-2)$-root $C$ as soon as $C$ is disjoint from the boundary, and $E\cdot C\in\ZZ$.

:::

::: {.definition #def:coble-r-invariant title="The $R$-invariant of a strong Coble surface"}

Let $S$ be a strong Coble surface with boundary components $B_1,\dots,B_n$, let $\pi\colon X\too S$ be the double cover branched along $\sum_iB_i$ with covering involution $\sigma$, put $L^+=\pi^*\CM(S)$ and let $L^-$ be the orthogonal complement of $L^+$ in $\Pic(X)$; the $(-2)$-curves $\tilde B_i$ with $\pi^*(B_i)=2\tilde B_i$ lie in $L^-$ [@Kon21, §3].
Put
$$
h^\pm = \theset{\delta^\pm\in L^\pm : \exists\delta^\mp\in L^\mp,\ (\delta^\pm)^2=-4,\ \tfrac12(\delta^+ + \delta^-)\in\Pic(X)}
$$
and let $\langle h^-\rangle=K(2)$ be the sublattice of $L^-$ generated by $h^-$, where $K$ is a root lattice.
The assignment $\gamma(\delta^-\bmod2)=\delta^+\bmod2$ is a homomorphism
$$
\gamma\colon K/2K\iso K(2)/2K(2)\too L^+/2L^+\iso\CM(S)/2\CM(S),
$$
its kernel $H$ is isotropic for the form $q_{K/2K}(x)=\tfrac12\langle x,x\rangle\bmod2\ZZ$, and the overlattice
$$
K_H = \theset{x\in K\tensor\QQ : 2x\in H}
$$
contains $K$ with index $\abs{H}$.
The pair $(K,H)$ is the $R$-**invariant** of $S$ [@Kon21, §3].
:::

A $(-2)$-curve $C$ contributes $\delta^\pm=\tilde C^+\pm\tilde C^-$, and a $(-1)$-root $2e+\tfrac12\beta_i+\tfrac12\beta_j$ contributes $\delta^+=2\tilde E+\tilde B_i+\tilde B_j$ and $\delta^-=\tilde B_i\pm\tilde B_j$, so both kinds of effective irreducible root are visible in $h^\pm$ [@Kon21, §3].
Two differences from the Enriques case are recorded in [@Kon21, §3] and matter below: the overlattice $K_H$ may contain $(-1)$-vectors, and it does as soon as $n\ge2$, the $(-1)$-vectors being $\tfrac12(\tilde B_i+\tilde B_j)$; and $\CM(S)$ need not be $E_{10}$, so the $R$-invariant is not a refinement of a single lattice statement (@lem:kondo-possible-characteristics(1)).

::: {.corollary #cor:one-boundary-coble-roots-are-curves title="With one boundary component every effective irreducible root is a curve"}

Let $S$ be a strong Coble surface with $n=1$ boundary component $B_1$.
Then $S$ carries no $(-1)$-root, and every effective irreducible root of $S$ is the class of a $(-2)$-curve.
Consequently, for a strong Coble surface with $n=1$ and finitely many effective irreducible roots, the vertices of the dual graph are all smooth rational curves on $S$.
:::

::: {.proof}

A $(-1)$-root meets two *different* boundary components by @lem:effective-root-dichotomy(1), and there is one boundary component. The last sentence restates @lem:effective-root-dichotomy(1): a $(-2)$-root is a $(-2)$-curve.

:::

## The nef cone, and the criterion for finiteness

::: {.definition #def:coble-mukai-nef-domain title="The domain $D(S)$ and the reflection group $W(S)$"}

Let $S$ be a strong Coble surface, let $\overline{\CM(S)}^+$ be the closure in $\CM(S)\otimes\RR$ of the component of $\theset{x^2>0}$ containing a nef class, and let $W(S)\subset\Orth(\CM(S))$ be generated by the reflections $s_\alpha\colon x\mapsto x+\langle x,\alpha\rangle\alpha$ in the effective irreducible roots.
Then
$$
D(S) = \theset{x\in\overline{\CM(S)}^+: x\cdot\alpha\ge0\text{ for every effective irreducible root }\alpha}
$$
is preserved by $\Aut(S)$ [@Kon21, §3].
:::

::: {.proposition #prop:coble-mukai-nef-and-completeness title="The nef cone is a fundamental domain, and a finite-index set of roots is all of them"}

Let $S$ be a strong Coble surface.

1. For $x\in\overline{\CM(S)}^+\intersect\CM(S)$, the class $x$ is nef if and only if $x\in D(S)$; the intersection of the nef cone of $S$ with $\overline{\CM(S)}^+$ is a fundamental domain for $W(S)$ [@Kon21, Proposition 3.4].
2. If $W(S)$ has finite index in $\Orth(\CM(S))$, then $\Aut(S)$ is finite [@Kon21, Proposition 3.5].
3. Conversely, let $\Aut(S)$ be finite and let $\Gamma=\theset{\alpha_1,\ldots,\alpha_s}$ be a set of pairwise different effective irreducible roots whose reflection group $W(\Gamma)$ has finite index in $\Orth(\CM(S))$. Then $\alpha_1,\ldots,\alpha_s$ are the only effective irreducible roots on $S$ [@Kon21, Proposition 3.7].
:::

::: {.proof}

(1) and (2) are [@Kon21, Proposition 3.4, Proposition 3.5]. (3) is [@Kon21, Proposition 3.7], proved as the corresponding statement for Enriques surfaces in Kondō's 1986 paper (Proposition 1.10 there, as cited at [@Kon21, Proposition 3.7]), and it uses the finiteness of $\Aut(S)$ to transport a root outside $\Gamma$ into one inside it by an automorphism.

:::

Clause 3 is what makes a displayed set of roots an answer rather than a lower bound: it is the step that converts "these $k$ roots generate a finite-index reflection group" into "these are all the effective irreducible roots".
Clause 2 is the corresponding conversion in the other direction, and it is the only place where finiteness of $\Aut(S)$ enters the existence half of the classification.

## Genus one fibrations, extremality, and special bi-sections

::: {.proposition #prop:coble-fibration-dictionary title="Genus one fibrations, their Halphen models, and special bi-sections"}

Let $S$ be a strong Coble surface with boundary components $B_1,\dots,B_n$.

1. The genus one fibrations $p\colon S\too\PP^1$ correspond bijectively to the primitive isotropic vectors of $D(S)\intersect\CM(S)$; the class of a fibre is such a vector, and conversely a primitive isotropic $f$ gives a fibration whose pullback to the covering K3 surface is nef and isotropic [@Kon21, Lemma 3.11].
2. Every genus one fibration on $S$ is obtained from a Halphen surface of index $2$ by blowing up all singular points, and their infinitely near points, of one reduced singular fibre, or from a Halphen surface of index $1$ by doing this to two reduced singular fibres [@Kon21, Proposition 3.8].
3. If $F$ is blown up from a fibre of type $\II$, $\III$, $\IV$ or $\mathrm{I}_n$, then its inverse image on the covering K3 surface is of type $\IV$, $\mathrm{I}_0^*$, $\IV^*$ or $\mathrm{I}_{2n}$ respectively [@Kon21, Lemma 3.9].
4. An effective irreducible root $r$ with $r\cdot F=2$ for a general fibre $F$ is a **special bi-section**, and the fibration is then **special**; if $\Aut(S)$ is finite, the Jacobian fibration of the minimal model of $p$ is extremal [@Kon21, Proposition 3.10]; and if $S$ has an effective irreducible root, then $S$ has a special genus one fibration [@Kon21, Lemma 3.13].
:::

::: {.proof}

(1)--(3) are the cited numbered statements. For (4): special bi-sections are defined in [@Kon21, §1, §3]; extremality is [@Kon21, Proposition 3.10]; and the existence of a special fibration from a root is [@Kon21, Lemma 3.13], whose proof separates $n=1,2$, where $\CM(S)\iso E_{10}$ and Cossec's theorem for Enriques surfaces [@Kon21, Proposition 3.12] transfers, from $n\ge3$, where the bi-section of the Halphen model is examined case by case.

:::

The mechanism of [@Kon21, Lemma 3.13] deserves naming, since the classification is an induction on it: a $(-1)$-curve $E$ meeting two boundary components $B,B'$ gives the $(-1)$-root $2e+\tfrac12\beta+\tfrac12\beta'$ [@Kon21, Lemma 3.2]. Its other case is conditional, not an unrestricted fibration construction. It starts with $n\ge3$, a fibration $p$ with Halphen model $H$, and the proper transform $E$ of a bi-section such that $E$ meets one boundary component $B$ with multiplicity $2$. Then $H$ has index $2$, and every boundary component lies in the fibre $F$ of $p$ containing $B$. There are a second boundary component $B'$ and a $(-1)$-curve $E_1$ with $E_1\cdot B=E_1\cdot B'=1$; moreover $2E+B$ is nef and isotropic. Thus $e+\tfrac12\beta$ is a primitive isotropic class in $D(S)\cap\CM(S)$, so [@Kon21, Lemma 3.11] gives a new fibration, of which $2e_1+\tfrac12\beta+\tfrac12\beta'$ is a special bi-section [@Kon21, Lemma 3.13].
The two kinds of root of @lem:effective-root-dichotomy are exactly the two ways a fibration can change.

## The mechanism of the classification

::: {.lemma #lem:kondo-finite-aut-engine title="The engine: five moves from finiteness of $\Aut(S)$ to a complete graph of roots"}

Let $S$ be a strong Coble surface in characteristic $p\neq2$ with $\Aut(S)$ finite.
Then:

1. every genus one fibration on $S$ has extremal Jacobian [@Kon21, Proposition 3.10]; each of the extremal fibrations of [@Kon21, §2, Table 3] that [@Kon21, §6] allows has a reducible fibre, whose vertices are represented by $(-1)$- and $(-2)$-roots [@Kon21, Remark 3.14], so $S$ carries an effective irreducible root;
2. some genus one fibration on $S$ is special;
3. let $\Gamma$ be the graph of effective irreducible roots obtained from a special fibration by iterating (2) on the new fibrations produced by a special bi-section; then $W(\Gamma)$ has finite index in $\Orth(\CM(S))$ if and only if every connected parabolic subdiagram of $\Gamma$ is a component of a parabolic subdiagram of $\Gamma$ of rank $\rank\CM(S)-2=8$, and in that case $\Gamma$ is the whole set of effective irreducible roots.

Consequently the induction leaves only finitely many possible dual graphs, classified in @thm:kondo-possible-dual-graphs. Passing from those graphs to finitely many isomorphism classes of surfaces requires the characteristic and boundary restrictions of [@Kon21, §6] and the uniqueness arguments of [@Kon21, §7], not the graph finiteness alone.
:::

::: {.proof}

(1) is [@Kon21, Proposition 3.10], together with the reading of [@Kon21, §2, Table 3] and [@Kon21, §6]: the extremal fibration has a reducible fibre, and its components are roots.

(2) is [@Kon21, Lemma 3.13] applied to the root of (1).

(3) The graph $\Gamma$ is a finite set of $(-2)$-vectors in the even lattice $\CM(S)$ of signature $(1,9)$, with no $m$-tuple lines for $m\ge3$, so Vinberg's criterion [@Kon21, Theorem 2.3] applies verbatim and gives the stated equivalence. For a lattice of signature $(1,n)$ the maximal parabolic rank is $n-1$; here $n=9$, hence the threshold is $\rank\CM(S)-2=8$.
The non-degeneracy hypothesis of that criterion is automatic here: the roots of the reducible fibres of an extremal fibration together with a special bi-section generate $\CM(S)\tensor\QQ$, so the cone $K(\Gamma)$ is strictly convex [@Kon21, Remark 3.6]. With the finite index in hand, $\Gamma$ is complete by @prop:coble-mukai-nef-and-completeness(3).

The graph-finiteness sentence is [@Kon21, Theorem 5.1, §5]: the finite-index condition constrains the graph alone, with $\rank\CM(S)=10$ bounding the possible parabolic configurations. The subsequent deduction of the surface classification is [@Kon21, Theorem 1.1, §6, §7].

:::

The two directions are used asymmetrically in [@Kon21]: the existence half (§5) is (1)--(3) applied to an unknown surface, and the identification half (§4, §6) is the same statements applied to the nine exhibited graphs, where clause 3 of @prop:coble-mukai-nef-and-completeness supplies completeness and clause 2 of @prop:coble-mukai-nef-and-completeness supplies finiteness of the automorphism group.

::: {.theorem #thm:kondo-possible-dual-graphs title="The possible dual graphs of effective irreducible roots"}

Assume $\operatorname{char}(k)\neq2$ and let $S$ be an Enriques or a strong Coble surface with finite automorphism group.
Then the dual graph of all effective irreducible roots on $S$ is of type $\mathrm{I}$, $\mathrm{II}$, ..., $\mathrm{VII}$, $\mathrm{MI}$ or $\mathrm{MII}$ [@Kon21, Theorem 5.1].
:::

::: {.proof}

The proof is the induction of @lem:kondo-finite-aut-engine over the types of the singular fibres of a special fibration, ordered as in [@Kon21, §5, (4.4)--(4.28)], and it uses three lemmas: a reducible multiple fibre is of type $\tilde A_m$, and is of type $\mathrm{I}_n$ when it consists of $(-2)$-curves [@Kon21, Lemma 5.3]; a diagram of type $D_4$ can be realized only by $(-2)$-curves, because the intersection of a $(-2)$-root with a $(-1)$-root is even [@Kon21, Lemma 5.4]; and a special bi-section meets only the simple components of a fibre of type $\II^*$, $\III^*$, $\IV^*$ or $\mathrm{I}_n^*$ [@Kon21, Lemma 5.5].
The steps [@Kon21, §5, (4.18), (4.23.2), (4.24.3), (4.24.4), (4.26)] are the ones where the cited 1986 proof used automorphisms of a complex K3 surface; they are replaced by the arguments producing $\Gamma_{\mathrm{MII}}$, $\Gamma_{\mathrm{MI}}$ and the two exclusions by extremal rational elliptic surfaces, and the two remaining multiple-fibre configurations are excluded by Martin's Lemma 10.12, as cited at [@Kon21, §5].
:::

## The classification

::: {.theorem #thm:kondo-finite-aut-classification title="Coble surfaces with finite automorphism group in characteristic $p\neq2$"}

Let $S$ be a strong Coble surface over an algebraically closed field of characteristic $p\neq2$, with finite automorphism group.
Then $S$ is isomorphic to exactly one of the nine surfaces of the table below, and each row is realized by such a surface [@Kon21, Theorem 1.1].
Here $n$ is the number of boundary components, $k$ is the number of effective irreducible roots — Kondō's letter, which the ground-field symbol of @def:strong-coble-surface must not be confused with — the two middle columns count the roots by kind, and the last-but-one column is the $R$-invariant of @def:coble-r-invariant.
:::

| type | $p$ | $n$ | $k$ | $(-2)$-roots | $(-1)$-roots | $\Aut(S)$ | $R$-invariant | source |
|---|---|---|---|---|---|---|---|---|
| $\mathrm{I}$ | any $p\neq2$ | $1$ | $12$ | $12$ | $0$ | $\mathrm{D}_8$ | $(E_8\oplus A_1,\theset{0})$ | [@Kon21, Example 4.3, Proposition 4.4; §6, case (1)] |
| $\mathrm{I}$ | any $p\neq2$ | $2$ | $12$ | $10$ | $2$ | $\mathrm{D}_8$ | $(E_8\oplus A_1^{\oplus2},\ZZ/2\ZZ)$ | [@Kon21, Example 4.1, Proposition 4.2; §6, case (1)] |
| $\mathrm{II}$ | any $p\neq2$ | $1$ | $12$ | $12$ | $0$ | $S_4$ | $(D_9,\theset{0})$ | [@Kon21, Example 4.5, Proposition 4.6; §6, case (2)] |
| $\mathrm{V}$ | $3$ | $2$ | $20$ | $16$ | $4$ | $S_4\times\ZZ/2\ZZ$ | $(E_7\oplus A_2\oplus A_1^{\oplus2},(\ZZ/2\ZZ)^2)$ | [@Kon21, Example 4.7, Proposition 4.8; §6, case (4)] |
| $\mathrm{VI}$ | $3$ | $5$ | $20$ | $10$ | $10$ | $S_5$ | $(E_6\oplus D_5,\ZZ/2\ZZ)$ | [@Kon21, Example 4.9, Proposition 4.11; §6, case (5)] |
| $\mathrm{VI}$ | $5$ | $1$ | $20$ | $20$ | $0$ | $S_5$ | $(E_6\oplus A_4,\theset{0})$ | [@Kon21, Example 4.12, Proposition 4.13; §6, case (5)] |
| $\mathrm{VII}$ | $5$ | $1$ | $20$ | $20$ | $0$ | $S_5$ | $(A_9\oplus A_1,\ZZ/2\ZZ)$ | [@Kon21, Example 4.15, Proposition 4.16; §6, case (6)] |
| $\mathrm{MI}$ | $3$ | $2$ | $40$ | $30$ | $10$ | $\Aut(S_6)$ | $(A_5^{\oplus2}\oplus A_1^{\oplus2},(\ZZ/2\ZZ)^3)$ | [@Kon21, Example 4.17, Proposition 4.19] |
| $\mathrm{MII}$ | $3$ | $8$ | $40$ | $24$ | $16$ | $(S_4\times S_4)\cdot\ZZ/2\ZZ$ | $(D_8\oplus A_2^{\oplus2},(\ZZ/2\ZZ)^2)$ | [@Kon21, Example 4.20, Proposition 4.22] |

The $(-2)$/$(-1)$ split in the table is the one computed in [@Kon21, §6]: case (1) fixes all twelve vertices of $\Gamma_{\mathrm{I}}$ as $(-2)$-curves when $n=1$ and ten of them when $n=2$; case (2) gives twelve $(-2)$-curves; case (4) sixteen $(-2)$-curves and the four $(-1)$-roots of the subdiagram (C) of [@Kon21, Figure 4]; case (5) ten $(-2)$-curves from the ten nodes and ten $(-1)$-roots for $n=5$, and twenty $(-2)$-curves for $n=1$; case (6) twenty $(-2)$-curves; cases (7) and (8) are described in @lem:kondo-possible-characteristics below.

::: {.corollary #cor:kondo-finite-aut-over-c title="Over the complex numbers there are exactly three"}

Let $S$ be a strong Coble surface over $\CC$ with finite automorphism group.
Then $S$ is isomorphic to one of: the type $\mathrm{I}$ surface with one boundary component (@prop:kondo-type-i-one-boundary), the type $\mathrm{I}$ surface with two boundary components, and the type $\mathrm{II}$ surface with one boundary component.
Each has twelve effective irreducible roots, and no other strong Coble surface over $\CC$ has finitely many automorphisms.
:::

::: {.proof}

The three rows of @thm:kondo-finite-aut-classification whose characteristic column reads "any $p\neq2$" are exactly these, and each is realized over $\CC$ by the construction of the cited examples, whose equations have coefficients in $\ZZ[1/2]$ [@Kon21, Example 4.1, Example 4.3, Example 4.5]. The remaining six rows have $p=3$ or $p=5$ forced, by @lem:kondo-possible-characteristics.

:::

::: {.corollary #cor:kondo-finite-aut-locus-finite title="Finiteness of the object, and the count of roots"}

Let $p\neq2$. The strong Coble surfaces over an algebraically closed field of characteristic $p$ with finite automorphism group form at most nine isomorphism classes, so in the moduli of Coble surfaces the strong objects with finite automorphism group are finitely many points, not a positive-dimensional family.
The number of effective irreducible roots of such a surface is $12$, $20$ or $40$, and it is $12$ for the three complex ones.
A Coble surface that is not strong is not covered by [@Kon21, Theorem 1.1], so no claim is made about its automorphism group: the finiteness here is a statement about the strong locus, which is what @prop:strong-coble-is-terminal-coble identifies.
:::

::: {.proof}

Finiteness is @thm:kondo-finite-aut-classification, which gives existence *and* uniqueness per row ("each type is unique"). The counts are the column $k$; its values are $12$, $20$, $40$.

:::

This is where the strong hypothesis of @prop:strong-coble-is-terminal-coble does real work, and it is the sharpest form of the comparison with the unnodal objects, where $\Aut(S)$ contains $W_{10}(2)$ and is infinite: among the *strong* Coble surfaces in characteristic $p\neq2$, finite automorphism group is the property of nine isolated objects.
It is not an open condition on the moduli of Coble surfaces, and the converse is not claimed: a Coble surface whose anti-bicanonical member is non-reduced lies outside [@Kon21, Theorem 1.1], so whether it can have finite automorphism group is not decided by the classification.

## Characteristic and number of boundary components

::: {.lemma #lem:kondo-possible-characteristics title="Which characteristics and how many boundary components"}

Let $S$ be a strong Coble surface over an algebraically closed field of characteristic $p\neq2$ whose dual graph of effective irreducible roots is of one of the types of @thm:kondo-possible-dual-graphs.

1. For types $\mathrm{I},\ldots,\mathrm{VII}$ the lattice $\CM(S)$ is $E_{10}$; for types $\mathrm{MI}$ and $\mathrm{MII}$ its determinant is $-2^l$ for some $l\ge0$ [@Kon21, Lemma 6.1].
2. The characteristic and the number of boundary components are then as follows [@Kon21, §6, cases (1)--(8)]:

| type | $p$ | $n$ | the restriction that decides it |
|---|---|---|---|
| $\mathrm{I}$ | any $p\neq2$ | $1$ or $2$ | an $\tilde E_8$ subdiagram comes from $(\II^*)$, $(\II^*,\II)$, $(\II^*,\mathrm{I}_1)$ or $(\II^*,\mathrm{I}_1,\mathrm{I}_1)$ |
| $\mathrm{II}$ | any $p\neq2$ | $1$ | $\tilde D_8$ gives $(\mathrm{I}_4^*,\mathrm{I}_1,\mathrm{I}_1,\mathrm{I}_1)$ with the singular points of one or two $\mathrm{I}_1$ fibres blown up; $\tilde D_5+\tilde A_3$ gives $(\mathrm{I}_1^*,\mathrm{I}_4,\mathrm{I}_1)$ with the singular point(s) of one or two of its $\mathrm{I}_4$ and $\mathrm{I}_1$ fibres blown up; comparing the two models gives $n=1$ |
| $\mathrm{III}$, $\mathrm{IV}$ | none | — | $\tilde D_4+\tilde D_4$ comes from $(\mathrm{I}_0^*,\mathrm{I}_0^*)$ with no blow-up, so the type is empty |
| $\mathrm{V}$ | $3$ | $2$ | the first two fibrations give $n=2$; comparing $\tilde E_6+\tilde A_2$ in arbitrary characteristic with its characteristic-$3$ quasi-elliptic form leaves only $p=3$, with two fibres of type $\II$ blown up |
| $\mathrm{VI}$ | $3$ or $5$ | $5$ if $p=3$, $1$ if $p=5$ | for $p\neq3$ the two indicated fibrations give $n=1$, after which Kondō's row-specific $R$-invariant and discriminant calculation gives $p=5$; for $p=3$ the alternative fibrations and the further $\tilde A_5+\tilde A_2+\tilde A_1$ and $\tilde D_5+\tilde A_3$ subdiagrams give $n=5$ |
| $\mathrm{VII}$ | $5$ | $1$ | the subdiagrams give $n\in\theset{1,2}$; an $A_9$ of $(-2)$-curves forces the covering K3 surface to be supersingular in characteristic $5$, and $(\mathrm{I}_5,\mathrm{I}_5,\II)$ then excludes $n=2$ |
| $\mathrm{MI}$ | $3$ | $2$ | the four maximal parabolic subdiagrams give $n=6$ for $p\neq3$ and $n=2$ for $p=3$; $n=6$ is excluded by a $\tilde A_3+\tilde A_3+\tilde A_1+\tilde A_1$ subdiagram whose two $\tilde A_1$'s are of different kinds |
| $\mathrm{MII}$ | $3$ | $8$ | $p=3$ and $n\in\theset{2,8}$; $n=2$ is excluded by counting the $(-2)$-roots of a quasi-elliptic fibration $(\IV,\IV,\IV,\IV)$ |
:::

::: {.proof}

(1) is [@Kon21, Lemma 6.1]: for types $\mathrm{I}$--$\mathrm{VII}$ the argument passes to the Enriques surface of the same type, whose $(-2)$-curves generate $E_{10}$ by the Enriques reducibility lemma of Cossec--Dolgachev--Liedtke, and for $\mathrm{MI}$, $\mathrm{MII}$ a parabolic subdiagram of type $\tilde A_7+\tilde A_1$ or $\tilde A_3+\tilde A_3+\tilde A_1+\tilde A_1$ together with a bi-section generates a finite-index sublattice of determinant $\pm2^j$.
(2) is [@Kon21, §6, cases (1)--(8)]; in each case a parabolic subdiagram of the graph is read as a genus one fibration of the surface by @prop:coble-fibration-dictionary(2)--(3), the Halphen model of @prop:coble-fibration-dictionary(2) says which fibres are blown up, and $n$ is the number of boundary components produced; then [@Kon21, Lemma 5.4] and @lem:effective-root-dichotomy determine which vertices are $(-2)$-curves, and that in turn excludes the remaining possibilities.

:::

The characteristic restrictions in @lem:kondo-possible-characteristics are separate rowwise fibration arguments; no global determinant-divisibility test is invoked.

::: {.remark #rmk:kondo-det-k-and-characteristic title="The rowwise characteristic restrictions"}

For type $\mathrm V$, the fibrations attached to $\tilde D_6+\tilde A_1+\tilde A_1$ and $\tilde E_7+\tilde A_1$ first give $n\in\theset{2,4}$ and $n\in\theset{1,2,3}$, hence $n=2$. The subdiagram $\tilde E_6+\tilde A_2$ then leaves only the characteristic-$3$ quasi-elliptic alternative: blowing up two fibres of type $\II$ produces the required two boundary components. Thus $p=3$ [@Kon21, §6, case (4)].

For type $\mathrm{VI}$ with $p\neq3$, the fibrations attached to $\tilde E_6+\tilde A_2$ and $\tilde A_4+\tilde A_4$ give $n=1$. The graph then determines the $R$-invariant $(E_6\oplus A_4,\theset{0})$; Kondō's discriminant calculation for this particular invariant, using $\abs{\det A_4}=5$ together with [@Kon21, Proposition 3.16, Lemma 2.1], identifies $X$ as a supersingular K3 surface in characteristic $5$. If instead $p=3$, the first fibration is replaced by quasi-elliptic $(\IV^*,\IV)$ or elliptic $(\IV^*,\mathrm{I}_3)$; the further subdiagrams $\tilde A_5+\tilde A_2+\tilde A_1$ and $\tilde D_5+\tilde A_3$ exclude the latter and force $n=5$ [@Kon21, §6, case (5)].

For type $\mathrm{VII}$, the three listed parabolic subdiagrams first give $n\in\theset{1,2}$. The $15$-vertex single-edge subdiagram consists entirely of $(-2)$-curves: the alternative that all its vertices are $(-1)$-roots is incompatible with $n\le2$. Its $A_9$ component in $K$ then gives, by Kondō's row-specific application of [@Kon21, Proposition 3.16, Lemma 2.1], a supersingular cover in characteristic $5$. In that characteristic the $\tilde A_4+\tilde A_4$ fibration is $(\mathrm{I}_5,\mathrm{I}_5,\II)$, which excludes $n=2$ and leaves the unique $n=1$ row [@Kon21, §6, case (6)].

For type $\mathrm{MI}$, the four maximal parabolic subdiagrams give $n=6$ if $p\neq3$ and $n=2$ if $p=3$. Under $n=6$, the first fibration makes all triads $(-2)$-curves, all duads $(-1)$-roots, and all synthemes $(-2)$-curves (after interchanging duads and synthemes if necessary). In the fibration $(\mathrm{I}_4,\mathrm{I}_4,\mathrm{I}_2,\mathrm{I}_2)$ attached to $\tilde A_3+\tilde A_3+\tilde A_1+\tilde A_1$, one $\mathrm{I}_2$ fibre is blown up and the other is not; but one $\tilde A_1$ consists of a duad and a syntheme, while the other consists of triads. These root-kind assignments are incompatible, so $p=3$ and $n=2$ [@Kon21, §6, case (7); @Kon21, Lemma 4.18].

For type $\mathrm{MII}$, the maximal parabolic subdiagrams force $p=3$ and $n\in\theset{2,8}$. If $n=2$, the quasi-elliptic fibration $(\IV,\IV,\IV,\IV)$ would make all forty vertices $(-2)$-curves, whereas the blown-up $\mathrm{I}_2$ fibre in $(\mathrm{I}_4,\mathrm{I}_4,\mathrm{I}_2,\mathrm{I}_2)$ supplies a $(-1)$-root. Thus $n=8$ [@Kon21, §6, case (8); @Kon21, Lemma 4.21]. Types $\mathrm I$ and $\mathrm{II}$ instead have examples in every characteristic $p\neq2$, and types $\mathrm{III}$ and $\mathrm{IV}$ are empty by their fibration configurations [@Kon21, §6, cases (1)--(4)].
:::

::: {.remark #rmk:kondo-supersingular-covers title="Picard number of the cover, and two grades of support for the supersingularity claims"}

Write $\pi\colon X\too S$ for the double cover, $\sigma$ for the covering involution, $L^+=\pi^*\CM(S)$ and $L^-=(L^+)^\perp$ inside $\Pic(X)$.
Then $\rank L^+=10$ and $\Pic(X)\tensor\QQ=L^+\tensor\QQ\oplus L^-\tensor\QQ$, so
$$
\rho(X)=10+\rank L^- .
$$
The root lattice $K$ of the $R$-invariant satisfies $K(2)\subseteq L^-$ [@Kon21, §3] and the $n$ boundary components contribute the $n$ independent $(-2)$-curves $\tilde B_i$, so $\rank L^-\ge\max(\rank K,n)$, and $\rho(X)=22$ is equivalent to $\rank L^-=12$.

For $\mathrm{MI}$ and $\mathrm{MII}$ the cover is identified: the Fermat quartic surface [@Kon21, Example 4.17] and $\operatorname{Kum}(E\times E)$ for the supersingular elliptic curve [@Kon21, Example 4.20], both supersingular of Artin invariant $1$, and indeed $\rank K=12$ in both rows.
For $\mathrm V$, both rows of type $\mathrm{VI}$, and $\mathrm{VII}$, the $R$-invariants give the following separate lower bounds:

| type | $\rank K$ | $\rho(X)=10+\rank L^-\ge$ | source |
|---|---|---|---|
| $\mathrm V$, $n=2$ | $11$ | $21$ | [@Kon21, Proposition 4.8] |
| $\mathrm{VI}$, $n=5$ | $11$ | $21$ | [@Kon21, Proposition 4.11] |
| $\mathrm{VI}$, $n=1$ | $10$ | $20$ | [@Kon21, Proposition 4.13] |
| $\mathrm{VII}$, $n=1$ | $10$ | $20$ | [@Kon21, Proposition 4.16] |

The assertion of [@Kon21, §1] that these covers are supersingular needs $\rank L^-=12$, which is not read off from the $R$-invariant, and no computation of $\rank L^-$ appears in the extracted text.
Nothing below depends on it: the classification, the characteristics and the counts do not use supersingularity, except at [@Kon21, §6, case (6)] where it is used to exclude $n=2$ for type $\mathrm{VII}$.
:::

::: {.proof}

$\pi^*$ is injective with $\pi_*\pi^*=2$, so $\pi^*\CM(S)$ has rank $10$ and is nondegenerate; hence $\Pic(X)\tensor\QQ$ is the direct sum of $L^+\tensor\QQ$ and its orthogonal complement, and ranks add.
$K(2)\subseteq L^-$ is [@Kon21, §3], where $\langle h^-\rangle=K(2)$ is the sublattice of $L^-$ generated by the vectors of square $-4$ paired with a vector of $L^+$; $\pi^*(B_i)=2\tilde B_i$ with $\tilde B_i^2=-2$ and $\tilde B_i\in L^-$ [@Kon21, §3], and distinct boundary components are disjoint, so the $\tilde B_i$ are independent.
The identifications of $X$ for $\mathrm{MI}$ and $\mathrm{MII}$ and their Artin invariant are [@Kon21, Example 4.17, Example 4.20].

:::

## Uniqueness, and two counts that check it

::: {.proposition #prop:kondo-uniqueness title="Uniqueness of each type"}

Each of the nine rows of @thm:kondo-finite-aut-classification contains one isomorphism class [@Kon21, §7].
:::

::: {.proof}

For $n=1$, that is types $\mathrm{I}$, $\mathrm{II}$, $\mathrm{VI}$ and $\mathrm{VII}$, uniqueness is [@Kon21, §7], citing Martin's Propositions 3.4, 4.3, 8.5 and 9.4, which classify Enriques surfaces of the corresponding type in characteristic $\neq2$; the passage to the Coble surface is licensed because the $R$-invariant and the graph agree.
For type $\mathrm{I}$ with $n=2$ the construction of [@Kon21, Example 4.1] is reversed to produce the same divisors on $\PP^1\times\PP^1$; Martin's argument does not apply directly because it uses a fibration of type $(\III^*,\mathrm{I}_2)$, whereas here the corresponding fibration is $(\III^*,\III)$.
For type $\mathrm{V}$ with $n=2$ the divisors are recovered as in the previous case; for type $\mathrm{VI}$ with $n=5$ the surface is recovered from the unique Jacobian rational elliptic fibration of type $(\mathrm{I}_6,\mathrm{I}_3,\III)$ [@Kon21, Remark 4.10]; for type $\mathrm{MI}$ the count below; for type $\mathrm{MII}$ from the uniqueness of the supersingular elliptic curve.

:::

::: {.proposition #prop:kondo-type-mi-count title="The count in the type $\mathrm{MI}$ uniqueness argument"}

On the Fermat quartic surface in characteristic $3$ there are $112$ lines, each disjoint from $81$ others, and
$$
\frac{112\cdot81}{2}=4536=2^3\cdot3^4\cdot 7
$$
pairs of skew lines.
The stabilizer of a pair of skew lines is $\Aut(S)\times\ZZ/2\ZZ$, of order $2\cdot1440=2^6\cdot3^2\cdot5=2880$, the extra $\ZZ/2\ZZ$ being generated by the covering involution, and
$$
4536\cdot2880 = 13\,063\,680 = 2^9\cdot3^6\cdot5\cdot7 = \abs{\mathrm{PGU}_4(\FF_9)},
$$
which acts on the set of pairs of skew lines; so the action is transitive and the type $\mathrm{MI}$ surface is unique [@Kon21, §7].
:::

::: {.proof}

The numbers are those of [@Kon21, §7], including $\abs{\mathrm{Aut}(S)}=\abs{\Aut(S_6)}=1440$ [@Kon21, Proposition 4.19] and $\abs{\mathrm{PGU}_4(\FF_9)}=2^9\cdot3^6\cdot5\cdot7$.
The arithmetic is exact: $112\cdot81/2=56\cdot81=4536$; $4536\cdot2880=13\,063\,680$; and $2^9\cdot3^6\cdot5\cdot7=512\cdot729\cdot35=13\,063\,680$.
The factor $2$ is the covering involution, which acts on the pair of skew lines cutting out the branch divisor, as $\pi^*(B_i)=2\tilde B_i$ records.

:::

A second, independent check on the same row is [@Kon21, Example 4.17]: the order of $\Aut(\Gamma_{\mathrm{MI}})$ is $\abs{\Aut(S_6)}=1440$ and $\Aut(S)$ injects into it, so the two groups have order $1440$ and are equal.
That inclusion is a statement about one surface; it says nothing about the configuration of forty roots on any other surface, and nothing about monodromy.

## The one-boundary type I surface

::: {.proposition #prop:kondo-type-i-one-boundary title="The type $\mathrm{I}$ pencil on $\PP^1\times\PP^1$, and its three Coble members"}

Let $k$ be algebraically closed of characteristic $p\neq2$, let $\phi$ be the involution $(u_0:u_1,v_0:v_1)\mapsto(u_0:-u_1,v_0:-v_1)$ of $\PP^1\times\PP^1$, and let $L_1,L_2$ be the curves $u_0=\pm u_1$ of bidegree $(1,0)$ and $L_3,L_4$ the curves $v_0=\pm v_1$ of bidegree $(0,1)$. For $\alpha\in k$ let $C_\alpha$ be the curve of bidegree $(2,2)$
$$
(2u_0^2-u_1^2)(v_0^2-v_1^2)=\qty(2\alpha v_0^2+(1-2\alpha)v_1^2)(u_0^2-u_1^2).
$$
The total branch divisor has bidegree
$$
[C_\alpha]+[L_1]+[L_2]+[L_3]+[L_4]=(2,2)+2(1,0)+2(0,1)=(4,4).
$$
Let $X\too\PP^1\times\PP^1$ be the minimal resolution of the double cover branched along $C_\alpha+\sum_iL_i$, and let $\sigma$ be the lift of $\phi$ [@Kon21, Example 4.1].

1. The fixed points of $\phi$ are the four points $(1:0,1:0)$, $(1:0,0:1)$, $(0:1,1:0)$, $(0:1,0:1)$, and none of them lies on any $L_i$.
2. A fixed point of $\phi$ lies on $C_\alpha$ for exactly three values of $\alpha$: at $\alpha=1$ the two points $(1:0,1:0)$ and $(0:1,0:1)$, at $\alpha=\tfrac12$ the point $(0:1,1:0)$, at $\alpha=\tfrac32$ the point $(1:0,0:1)$.
   For all other $\alpha$ the involution $\sigma$ is fixed-point free and $S=X/\langle\sigma\rangle$ is an Enriques surface of type $\mathrm{I}$ [@Kon21, Example 4.1].
3. At $\alpha=1$, $C_1=2Q_1Q_2$ with $Q_\pm\colon u_1v_0\mp u_0v_1=0$, and $\sigma$ has two fixed curves; $S=X/\langle\sigma\rangle$ is the type $\mathrm{I}$ strong Coble surface with two boundary components and twelve effective irreducible roots, ten $(-2)$-curves and two $(-1)$-roots, with dual graph $\Gamma_{\mathrm{I}}$, $\Aut(S)\iso\mathrm{D}_8$ and $R$-invariant $(E_8\oplus A_1^{\oplus2},\ZZ/2\ZZ)$ [@Kon21, Example 4.1, Proposition 4.2].
4. At $\alpha=\tfrac12$ and $\alpha=\tfrac32$ the singularity of $C_\alpha$ at the fixed point is an ordinary node, with local equation $u^2+w^2=0$ in the coordinates $u=u_0/u_1$, $w=v_1/v_0$ at $(0:1,1:0)$ and $A^2+B^2=0$ in $A=u_1/u_0$, $B=v_0/v_1$ at $(1:0,0:1)$; $\sigma$ has one fixed curve; $S$ is the type $\mathrm{I}$ strong Coble surface with one boundary component, twelve $(-2)$-curves, $\Aut(S)\iso\mathrm{D}_8$ and $R$-invariant $(E_8\oplus A_1,\theset{0})$ [@Kon21, Example 4.3, Proposition 4.4].
   By the uniqueness clause of @thm:kondo-finite-aut-classification the two surfaces are isomorphic.
:::

::: {.proof}

(1) is immediate from the action of $\phi$; none of the four points satisfies $u_0=\pm u_1$ or $v_0=\pm v_1$, both of which need both coordinates nonzero.

(2) Evaluating the defining equation of $C_\alpha$ at the four fixed points gives $2=2\alpha$, $-2=1-2\alpha$, $-1=-2\alpha$ and $1=2\alpha-1$, that is $\alpha=1$, $\alpha=\tfrac32$, $\alpha=\tfrac12$ and $\alpha=1$, so the values are as listed and no other $\alpha$ puts a fixed point on $C_\alpha$. Since the branch divisor is $C_\alpha+\sum L_i$ and $\sigma$ fixes a curve exactly over the fixed points of $\phi$ lying on the branch divisor, $\sigma$ is fixed point free away from those three values, and $X/\langle\sigma\rangle$ is an Enriques surface.

(3) is [@Kon21, Example 4.1, Proposition 4.2], with the splitting $C_1=2Q_1Q_2$ checked by expansion: $(2u_0^2-u_1^2)(v_0^2-v_1^2)-(2v_0^2-v_1^2)(u_0^2-u_1^2)=2(u_1^2v_0^2-u_0^2v_1^2)=2Q_1Q_2$.

(4) Substituting $u_0=u$, $u_1=1$, $v_0=1$, $v_1=w$ at $\alpha=\tfrac12$ gives $-2u^2w^2+u^2+w^2$, whose lowest-degree part is $u^2+w^2$: a nondegenerate quadratic form if and only if $p\neq2$, so the point is an ordinary node and not a cusp. At $\alpha=\tfrac32$ the same substitution with $u_0=1$, $u_1=A$, $v_0=B$, $v_1=1$ gives $2A^2B^2-A^2-B^2$, whose quadratic term is $-(A^2+B^2)$, the same shape. The identification of the surfaces is [@Kon21, Example 4.3, Proposition 4.4].

:::

Two remarks on @prop:kondo-type-i-one-boundary.

First, the hypothesis $p\neq2$ is not a convenience in the construction: by (4) the local equation of the branch curve at the fixed point is $u^2+w^2=0$, which in characteristic $2$ is the double line $(u+w)^2=0$, so the double cover is inseparable there and no Coble surface arises.
This is the local shadow of the global statement of [@Kon21, §1] that the canonical covering of a Coble surface in characteristic $2$ is inseparable, which is why the classification assumes $p\neq2$.

Second, the two one-boundary members of the pencil, at $\alpha=\tfrac12$ and $\alpha=\tfrac32$, are not related by a symmetry of the pencil visible in [@Kon21, Example 4.1]; their isomorphism is an instance of the uniqueness clause of @thm:kondo-finite-aut-classification, and it can be read as saying that the type $\mathrm{I}$ surface with one boundary component admits two inequivalent $\PP^1\times\PP^1$ models of this shape.

::: {.proposition #prop:type-i-e8-summand title="The $E_8$ configuration on the one-boundary surface is a unimodular summand of the Coble--Mukai lattice"}

Let $S$ be the surface of @prop:kondo-type-i-one-boundary(4), over $\CC$.

1. $\CM(S)\iso E_{10}$ and $\CM(S)=K_S^{\perp}$, and the twelve $(-2)$-curve classes span $\CM(S)\tensor\QQ$.
2. The graph $\Gamma_{\mathrm{I}}$ contains a parabolic subdiagram $\tilde E_8$ [@Kon21, §6, case (1)], and since all twelve vertices are $(-2)$-curves, deleting the extending vertex of that $\tilde E_8$ leaves eight of them whose dual graph is $E_8$.
3. Those eight classes span a primitive unimodular sublattice $E_8\subset\CM(S)$ whose orthogonal complement is the hyperbolic plane $U$:
$$
\CM(S) = E_8\oplus U .
$$
:::

::: {.proof}

(1) $\CM(S)\iso E_{10}$ and $\CM(S)=K_S^{\perp}$ are @prop:kondo-coble-mukai-is-e10 for $n=1$. The twelve classes span $\CM(S)\tensor\QQ$ because $\Gamma_{\mathrm{I}}$ satisfies the criterion of [@Kon21, Theorem 2.3] — this is the assertion of [@Kon21, Example 4.3] that the dual graph satisfies the condition — so $W(\Gamma_{\mathrm{I}})$ has finite index in $\Orth(\CM(S))$ by that theorem, and a reflection group of finite index cannot fix a nonzero vector, so the roots generate $\CM(S)\tensor\QQ$.

(2) The parabolic subdiagram of type $\tilde E_8$ is [@Kon21, §6, case (1)]. Its nine vertices are $(-2)$-curves by @cor:one-boundary-coble-roots-are-curves, and the affine diagram $\tilde E_8$ is the Dynkin diagram $E_8$ with one vertex attached to the vertex adjacent to the branch node; deleting that vertex leaves $E_8$.

(3) $E_8$ is unimodular, so its image in the unimodular lattice $\CM(S)$ is primitive: a primitive vector of a unimodular lattice with unimodular orthogonal complement spans a direct summand, and here $A_{E_8}=0$ gives $\CM(S)=E_8\oplus E_8^{\perp}$. The complement is even, unimodular and of signature $(1,1)$ — the signature is $(1,9)-(0,8)$ — and the even unimodular lattice of signature $(1,1)$ is $U$ [@thm:indefinite-unimodular-classification; @def:enriques-lattice].

:::

::: {.corollary #cor:type-i-one-boundary-not-classical title="The one-boundary type I surface has no presentation by ten distinct nodes"}

Over $\CC$, let $S$ be the surface of @prop:kondo-type-i-one-boundary(4).
Then $S$ is a strong Coble surface with one boundary component, so by @thm:coble-smooth-antibicanonical-is-a-plane-blowup it is $\Bl_{p_1,\dots,p_{10}}\PP^2$ for ten points, possibly infinitely near, its anti-bicanonical curve is $C=6H-2\sum_iE_i$, and its image $Z$ is an irreducible plane sextic with $\delta(Z)=10$.
By @prop:type-i-e8-summand it contains eight $(-2)$-curves with dual graph $E_8$, so by @prop:coble-e8-configuration-excludes-ten-distinct-centres $S$ has no ten pairwise disjoint $(-1)$-curves and no birational morphism to $\PP^2$ with ten distinct centres.
In particular the ten points of the plane model are not ten distinct points at which $Z$ has an ordinary node.
:::

::: {.proof}

The first sentence is @prop:strong-coble-is-terminal-coble and @thm:coble-smooth-antibicanonical-is-a-plane-blowup(2)--(3).
The eight $(-2)$-curves are @prop:type-i-e8-summand(2), and the E8 configuration is of $(-2)$-curves as @prop:coble-e8-configuration-excludes-ten-distinct-centres requires.
That proposition gives the absence of ten pairwise disjoint $(-1)$-curves; the exceptional curves of a morphism with ten distinct centres are ten pairwise disjoint $(-1)$-curves, so no such morphism exists, and by @thm:coble-smooth-antibicanonical-is-a-plane-blowup(4) a plane model whose ten centres are distinct would have $Z$ with exactly ten ordinary nodes.

:::

::: {.remark #rmk:kondo-what-the-classification-does-not-decide title="What the classification does not decide"}

Three statements are outside @thm:kondo-finite-aut-classification, and none of them follows from it.

1. *Isomorphism with any other non-classical object.* The one-boundary type $\mathrm{I}$ surface is non-classical by @cor:type-i-one-boundary-not-classical, and so are the surfaces $S_{Z_8}$ and $S_{Z_{64}}$ of @ex:coble-sextics-with-an-a15-point. The corollary does not assert non-classicality of the two-boundary type $\mathrm{I}$ surface. Sharing the property "non-classical" is not an isomorphism, and no comparison between the twelve-root configuration of @prop:kondo-type-i-one-boundary(4) and the configurations of those two surfaces is made here or in [@Kon21]. What the example gives the complex theory is a second, independent supply of objects with an $E_8$ configuration of $(-2)$-curves, hence a second family of plane models whose ten centres cannot be ten distinct nodes.
2. *A presentation by ten distinct centres.* The contrary is proved: @cor:type-i-one-boundary-not-classical.
3. *Monodromy.* Finiteness of $\Aut(S)$ at the nine surfaces is isotropy data at nine objects. The monodromy of a local system on a moduli stack is a property of a family over a base, computed from loops, and it is not a function of the automorphism group of a single fibre; @thm:kondo-finite-aut-classification constructs no family and no base, so it yields no statement about the monodromy groups $\Gamma_\Co$ and $\Gamma_{\Co,2}$ of the Coble families, and none about which lattice group the stack's monodromy is. In particular the nine surfaces do not supply a computation of the monodromy of $\mcM_\Co$ over $\CC$; the finite-isotropy locus being nine points is compatible with a monodromy group that is large on the complement.

:::

Related: [Constructions of the moduli space](#sec-moduli-construction), [The research program for $F_{\Co,n}$](#sec-coble-families-research-program), [The Coble cusp correspondence and the morphism chain](#sec-cusp-correspondence-morphism-chain).
