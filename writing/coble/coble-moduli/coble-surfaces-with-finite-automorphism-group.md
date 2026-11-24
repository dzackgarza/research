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

Let $S$ be a smooth projective rational surface over an algebraically closed field $k$ of characteristic $p$, with $\abs{-K_S}=\varnothing$ and $\abs{-2K_S}\neq\varnothing$.
Then $S$ is a strong Coble surface with $n$ boundary components in the sense of @def:strong-coble-surface if and only if it is a terminal Coble surface of K3 type with $n$ boundary components in the sense of @def:coble-surface.
In that case $B_i^2=-4$, $K_S\cdot B_i=2$, $K_S^2=-n$, $\rho(S)=10+n$ and $n\le 10$ [@Kon21, §3; @DK25, §9.1, Corollary 9.1.5; @prop:terminal-coble-basic-rational].
Let $\pi\colon X\too S$ be the canonical double cover defined by $\OO_S(-K_S)$.
If $p\neq2$, then $\pi$ is separable, branched along $B_1+\cdots+B_n$, and $X$ is smooth and is a K3 surface [@DK25, Proposition 9.1.1 and the $p\neq2$ case of its proof; @KK21, Introduction].
If $p=2$, then $\pi$ is a purely inseparable $\mu_2$-cover, and $X$ is K3-like: $\omega_X\iso\OO_X$ and $H^1(X,\OO_X)=0$.
Let $A$ be the conductrix, defined by $(\eta)=-\sum_{i=1}^nB_i+2A$.
If $A=0$, then $X$ has some singular point, all its singularities are rational double points, and its minimal nonsingular model is a supersingular K3 surface; the K3 surface is that resolution, not the cover $X$.
If $A\neq0$, then $X$ is a rational surface, $A^2=-2$, and its isolated singularities are $4-n$ rational double points of type $A_1$ [@KK21, Introduction, Theorem 1.1, Theorem 3.1, Theorem 3.6, Proposition 3.17, Corollary 3.18].
:::

::: {.proof}

*From strong to terminal.* By hypothesis $\abs{-2K_S}$ has the single member $D=B_1+\cdots+B_n$, which is reduced because the $B_i$ are distinct prime divisors and they are pairwise disjoint.
Intersecting $D\sim-2K_S$ with $B_i$ gives $-2K_S\cdot B_i=B_i^2$, that is $B_i\cdot K_S=-\tfrac12B_i^2$; adjunction on the smooth rational curve $B_i$ gives $-2=B_i^2+B_i\cdot K_S$, and the two together give $B_i^2=-4$ and $B_i\cdot K_S=2$.
So $D$ is the only member of $\abs{-2K_S}$ and is a disjoint union of $(-4)$-curves, which is the terminal K3-type condition of @def:coble-surface.

*From terminal to strong.* Conversely, if $\abs{-2K_S}=\theset{D}$ with $D$ reduced and a disjoint union of smooth rational $(-4)$-curves, then naming the components $B_1,\ldots,B_n$ gives the strong Coble data, by the same numbering.

The numerical invariants and the bound are those of @prop:terminal-coble-basic-rational. The separable smooth K3 cover for $p\neq2$ is [@Kon21, §1; @DK25, Proposition 9.1.1, the $p\neq2$ case of its proof; @KK21, Introduction], and the characteristic-$2$ statements are [@KK21, Introduction, Theorem 1.1, Theorem 3.1, Theorem 3.6, Proposition 3.17, Corollary 3.18].

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

::: {.definition #def:coble-r-invariant title="The $R$-invariant in characteristic $p\neq2$"}

Let $S$ be a strong Coble surface over an algebraically closed field $k$ of characteristic $p\neq2$, with boundary components $B_1,\dots,B_n$. Let $\pi\colon X\too S$ be the **separable** double cover branched along $\sum_iB_i$, with its nontrivial covering involution $\sigma$, and put $L^+=\pi^*\CM(S)$ and let $L^-$ be the orthogonal complement of $L^+$ in $\Pic(X)$; the $(-2)$-curves $\tilde B_i$ with $\pi^*(B_i)=2\tilde B_i$ lie in $L^-$ [@Kon21, §3].
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
K_H = \theset{x\in \tfrac12 K : [2x]_{2K}\in H}
$$
contains $K$ with index $\abs{H}$.
The pair $(K,H)$ is the $R$-**invariant** of $S$ [@Kon21, §3].

The isomorphism $K_H/K\iso H$ sends $x+K$ to $[2x]_{2K}$: its kernel is zero, and $v/2$ lifts every $[v]\in H$. The form on $K_H$ is the rational extension of the form on $K$. Isotropy for $q_{K/2K}$ alone does not imply integrality of its bilinear pairing: for the orthogonal basis $e_1,e_2,e_3$ of $A_1^{\oplus3}$ of square $-2$, the subgroup generated by $[e_1+e_2]$ and $[e_2+e_3]$ is isotropic, whereas the two half-sums pair to $-1/2$. For the geometric kernel $H$, $K_H(2)$ embeds in $L^-$: if a class $[\delta^-]$ of $K(2)/2K(2)$ lies in $H$, a compatible $\delta^+\in L^+$ with $(\delta^++\delta^-)/2\in\Pic(X)$ may be taken in $2L^+$, by adding the half-sum relations for the generators of $K(2)$. Thus $\delta^-/2\in\Pic(X)\cap(L^-)_{\QQ}=L^-$. This assertion concerns the scaled pairing, not integrality of the unscaled pairing for an arbitrary isotropic subgroup.
:::

The hypothesis $p\neq2$ is essential to this K3-cover formulation. In characteristic $2$ the canonical cover is instead a **purely inseparable $\mu_2$-cover**, which can be singular and need not be a K3 surface [@KK21, Introduction, Theorem 1.1]. On function fields its extension $k(S)\subseteq k(X)$ is purely inseparable of degree $2$: every $z\in k(X)$ satisfies $z^2\in k(S)$. If $\tau\in\Aut_{k(S)}(k(X))$, then
$$
(\tau(z)-z)^2=\tau(z^2)-z^2=0.
$$
Since $k(X)$ is a field, $\tau(z)=z$ for every $z$, whence $\tau=\id$. Thus **there is no nontrivial geometric deck involution** in characteristic $2$; the infinitesimal group scheme $\mu_2$ is not an order-two automorphism on geometric points, since $\mu_2(k)=\{1\}$. The source [@Kon21, §3], which assumes characteristic different from $2$, therefore does **not** define the displayed $R$-invariant through a covering involution on an arbitrary characteristic-two Coble surface. A characteristic-two analogue would require a separate definition and proof involving the $\mu_2$ action and the potentially singular cover. This does not change @def:strong-coble-surface or the characteristic-two canonical-cover theorem of @prop:strong-coble-is-terminal-coble.

Under the hypotheses of @def:coble-r-invariant, a $(-2)$-curve $C$ contributes $\delta^\pm=\tilde C^+\pm\tilde C^-$, and a $(-1)$-root $2e+\tfrac12\beta_i+\tfrac12\beta_j$ contributes $\delta^+=2\tilde E+\tilde B_i+\tilde B_j$ and $\delta^-=\tilde B_i\pm\tilde B_j$, so both kinds of effective irreducible root are visible in $h^\pm$ [@Kon21, §3].
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

1. The genus one fibrations $p\colon S\too\PP^1$ correspond bijectively to the primitive isotropic vectors of $D(S)\intersect\CM(S)$ by taking the primitive generator $f$ of the fibre ray. For an actual general fibre $F$, [@Kon21, Lemma 3.11] gives that $[F]$ is isotropic in $D(S)\intersect\CM(S)$, not that $[F]$ is primitive; conversely a primitive isotropic $f$ gives a fibration whose pullback to the covering K3 surface is nef and isotropic. In the index-two Halphen case $[F]=2f$ with $f$ primitive [@DK25, Proposition 9.1.4, Example 9.1.7]. Thus the condition $r\cdot F=2$ in (4) says $r\cdot f=1$ when $[F]=2f$, and $r\cdot f=2$ when $[F]=f$.
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
3. let $\Gamma$ be the graph of effective irreducible roots obtained from a special fibration by iterating (2) on the new fibrations produced by a special bi-section, and assume that $\Gamma$ has no $m$-tuple lines with $m\ge3$; then $W(\Gamma)$ has finite index in $\Orth(\CM(S))$ if and only if every connected parabolic subdiagram of $\Gamma$ is a component of a parabolic subdiagram of $\Gamma$ of rank $\rank\CM(S)-2=8$, and in that case $\Gamma$ is the whole set of effective irreducible roots.

Consequently the induction leaves only finitely many possible dual graphs, classified in @thm:kondo-possible-dual-graphs. Passing from those graphs to finitely many isomorphism classes of surfaces requires the characteristic and boundary restrictions of [@Kon21, §6] and the uniqueness arguments of [@Kon21, §7], not the graph finiteness alone.
:::

::: {.proof}

(1) is [@Kon21, Proposition 3.10], together with the reading of [@Kon21, §2, Table 3] and [@Kon21, §6]: the extremal fibration has a reducible fibre, and its components are roots.

(2) is [@Kon21, Lemma 3.13] applied to the root of (1).

(3) The graph $\Gamma$ is a finite set of $(-2)$-vectors in the even lattice $\CM(S)$ of signature $(1,9)$. Vinberg's criterion [@Kon21, Theorem 2.3] requires that set to be finite, $\Gamma$ to be non-degenerate, and the absence of $m$-tuple lines assumed in the statement, and it then gives the stated equivalence. For a lattice of signature $(1,n)$ the maximal parabolic rank is $n-1$; here $n=9$, hence the threshold is $\rank\CM(S)-2=8$.
The non-degeneracy hypothesis of that criterion is automatic here: the roots of the reducible fibres of an extremal fibration together with a special bi-section generate $\CM(S)\tensor\QQ$, so the cone $K(\Gamma)$ is strictly convex [@Kon21, Remark 3.6]. Moreover $W(\Gamma)\subseteq W(S)$, so finite index of $W(\Gamma)$ implies finite index of $W(S)$, to which @prop:coble-mukai-nef-and-completeness(2) applies. With the finite index in hand, $\Gamma$ is complete by @prop:coble-mukai-nef-and-completeness(3).

The graph-finiteness sentence is [@Kon21, Theorem 5.1, §5]: the finite-index condition constrains the graph alone, with $\rank\CM(S)=10$ bounding the possible parabolic configurations. The subsequent deduction of the surface classification is [@Kon21, Theorem 1.1, §6, §7].

:::

The two directions are used asymmetrically in [@Kon21]: the existence half (§5) is (1)--(3) applied to an unknown surface, while the identification of the examples (§4) requires a finite-index check on each displayed graph before @prop:coble-mukai-nef-and-completeness can supply finiteness and completeness. The graphwise input, including the two rows for which Kondō's example does not repeat that check, is @lem:kondo-exhibited-graph-finiteness below. Section 6 instead determines characteristic and boundary number from parabolic fibrations; it supplies no Vinberg verification.

::: {.theorem #thm:kondo-possible-dual-graphs title="The possible dual graphs of effective irreducible roots"}

Assume $\operatorname{char}(k)\neq2$ and let $S$ be an Enriques or a strong Coble surface with finite automorphism group.
Then the dual graph of all effective irreducible roots on $S$ is of type $\mathrm{I}$, $\mathrm{II}$, ..., $\mathrm{VII}$, $\mathrm{MI}$ or $\mathrm{MII}$ [@Kon21, Theorem 5.1].
:::

::: {.proof}

The proof is the induction of @lem:kondo-finite-aut-engine over the types of the singular fibres of a special fibration, ordered as in [@Kon21, §5, (4.4)--(4.28)], and it uses three lemmas: a reducible multiple fibre is of type $\tilde A_m$, and is of type $\mathrm{I}_n$ when it consists of $(-2)$-curves [@Kon21, Lemma 5.3]; a diagram of type $D_4$ can be realized only by $(-2)$-curves, because the intersection of a $(-2)$-root with a $(-1)$-root is even [@Kon21, Lemma 5.4]; and a special bi-section meets only the simple components of a fibre of type $\II^*$, $\III^*$, $\IV^*$ or $\mathrm{I}_n^*$ [@Kon21, Lemma 5.5].
The steps [@Kon21, §5, (4.18), (4.23.2), (4.24.3), (4.24.4), (4.26)] are the ones where the cited 1986 proof used automorphisms of a complex K3 surface; they are replaced by the arguments producing $\Gamma_{\mathrm{MII}}$, $\Gamma_{\mathrm{MI}}$ and the two exclusions by extremal rational elliptic surfaces, and the two remaining multiple-fibre configurations are excluded by Martin's Lemma 10.12, as cited at [@Kon21, §5].
:::

## The classification

::: {.lemma #lem:kondo-exhibited-graph-finiteness title="Finite automorphism groups from the exhibited root graphs"}
Let $S$ be one of the strong Coble surfaces exhibited in [@Kon21, Example 4.1, Example 4.3, Example 4.5, Example 4.7, Example 4.9, Example 4.12, Example 4.15, Example 4.17, Example 4.20], and let $\Gamma$ be its displayed graph of effective irreducible roots.
Then $W(\Gamma)$ has finite index in $\Orth(\CM(S))$, $\Aut(S)$ is finite, and $\Gamma$ is the complete graph of effective irreducible roots on $S$.
This conclusion uses Kondō's Theorem 2.3 and Propositions 3.5 and 3.7, not a row of Theorem 1.1 or Table 2.
:::

::: {.proof}

The Coble--Mukai lattice has signature $(1,9)$ [@KK21, Introduction]. Vinberg's criterion [@Kon21, Theorem 2.3] therefore applies to a finite set $\Delta$ of $(-2)$-vectors precisely when $\Gamma$ is non-degenerate, contains no $m$-tuple lines with $m\ge3$, and every connected parabolic subdiagram of $\Gamma$ is a connected component of a parabolic subdiagram of rank $n-1=8$; then $W(\Gamma)$ has finite index in $\Orth(\CM(S))$.
Here $\Delta$ has $12$, $20$ or $40$ elements in the cited examples. Figures 2--6 have only single and double lines, and the definitions of the remaining two graphs likewise give only these two multiplicities [@Kon21, Figures 2--6, Example 4.17, Example 4.20], so no $m$-tuple line with $m\ge3$ occurs.
For the graph types of Examples 4.1, 4.5, 4.7, 4.9 and 4.15, non-degeneracy is part of Kondō's graphwise assertion quoted below, whose fibration basis is [@Kon21, Remark 3.6]: the reducible fibres of an extremal genus-one fibration together with a special bi-section generate $\CM(S)\tensor\QQ$, hence $K(\Gamma)$ is strictly convex. For $\mathrm{MI}$ and $\mathrm{MII}$, [@Kon21, Lemma 4.18, Lemma 4.21] say explicitly that every maximal parabolic diagram defines a special genus-one fibration, so the same remark applies without assuming that the displayed roots are already complete. The two transferred cases are handled below by graph and lattice identification, not by assuming completeness.

The maximal-parabolic condition is checked graph by graph, not inferred from Table 2:

| graph | Vinberg's rank-$8$ condition and its source |
|---|---|
| $\Gamma_{\mathrm I}$ | [@Kon21, Example 4.1] states that the complete graph satisfies Theorem 2.3. The rank-$8$ completions recorded in [@Kon21, §6, case (1)] are $\tilde E_8$, $\tilde E_7+\tilde A_1$ and $\tilde A_7+\tilde A_1$, of ranks $8$, $7+1$ and $7+1$. Example 4.3 uses this same abstract graph for the one-boundary surface. |
| $\Gamma_{\mathrm{II}}$ | [@Kon21, Example 4.5] states the condition; [@Kon21, §6, case (2)] records $\tilde D_8$ and $\tilde D_5+\tilde A_3$, of ranks $8$ and $5+3$. |
| $\Gamma_{\mathrm V}$ | [@Kon21, Example 4.7] states the condition; [@Kon21, §6, case (4)] records $\tilde D_6+\tilde A_1+\tilde A_1$, $\tilde E_7+\tilde A_1$ and $\tilde E_6+\tilde A_2$, of ranks $6+1+1$, $7+1$ and $6+2$. |
| $\Gamma_{\mathrm{VI}}$ | [@Kon21, Example 4.9] states the condition; [@Kon21, §6, case (5)] records $\tilde E_6+\tilde A_2$, $\tilde A_4+\tilde A_4$, $\tilde A_5+\tilde A_2+\tilde A_1$ and $\tilde D_5+\tilde A_3$, of ranks $6+2$, $4+4$, $5+2+1$ and $5+3$. Example 4.12 uses this same abstract graph in characteristic $5$. |
| $\Gamma_{\mathrm{VII}}$ | [@Kon21, Example 4.15] states the condition; [@Kon21, §6, case (6)] records $\tilde A_4+\tilde A_4$, $\tilde A_8$ and $\tilde A_5+\tilde A_2+\tilde A_1$, of ranks $4+4$, $8$ and $5+2+1$. |
| $\Gamma_{\mathrm{MI}}$ | [@Kon21, Lemma 4.18] proves directly that every connected parabolic subdiagram is a component of one of its maximal diagrams; their component-rank multisets are $\{5,2,1\}$, $\{4,4\}$, $\{3,3,1,1\}$ and $\{2,2,2,2\}$, each summing to $8$. |
| $\Gamma_{\mathrm{MII}}$ | [@Kon21, Lemma 4.21] proves the same statement, with component-rank multisets $\{7,1\}$, $\{5,2,1\}$, $\{3,3,1,1\}$ and $\{2,2,2,2\}$. |

For the one-boundary type $\mathrm I$ example and the characteristic-$5$ type $\mathrm{VI}$ example, the two transfers asserted in the table are legitimate: the graphs are respectively the same abstract $\Gamma_{\mathrm I}$ and $\Gamma_{\mathrm{VI}}$, and the ambient lattice is $E_{10}$ for each one-boundary surface by [@Kon21, Proposition 3.1(1)], as it is for the type $\mathrm I$--$\mathrm{VII}$ companion graphs by [@Kon21, Lemma 6.1]. Vinberg's criterion therefore transfers together with the abstract graph and the ambient $E_{10}$. So every exhibited graph satisfies the complete hypothesis of that criterion and $W(\Gamma)$ has finite index.
Since $W(\Gamma)\subseteq W(S)$, $W(S)$ has finite index in $\Orth(\CM(S))$ as well, and $\Aut(S)$ is finite by [@Kon21, Proposition 3.5]. Only with this finiteness established does [@Kon21, Proposition 3.7] apply, proving that the displayed $\Gamma$ is the whole set of effective irreducible roots. No finiteness assertion is made for any other strong or terminal Coble surface.

:::

::: {.theorem #thm:kondo-finite-aut-classification title="Coble surfaces with finite automorphism group in characteristic $p\neq2$"}

Let $S$ be a strong Coble surface over an algebraically closed field of characteristic $p\neq2$, with finite automorphism group.
Then $S$ is isomorphic to exactly one of the nine surfaces of the table below. Each row is realized by such a surface: existence and finiteness are @lem:kondo-exhibited-graph-finiteness, proved above independently of Table 2, and classification and uniqueness are [@Kon21, Theorem 1.1].
Here $n$ is the number of boundary components, $k$ is the number of effective irreducible roots — Kondō's letter, which the ground-field symbol of @def:strong-coble-surface must not be confused with — the two middle columns count the roots by kind, and the last-but-one column is the $R$-invariant of @def:coble-r-invariant.
:::

| type | $p$ | $n$ | $k$ | $(-2)$-roots | $(-1)$-roots | $\Aut(S)$ | $R$-invariant | source |
|---|---|---|---|---|---|---|---|---|
| $\mathrm{I}$ | any $p\neq2$ | $1$ | $12$ | $12$ | $0$ | $\mathrm{D}_8$ | $(E_8\oplus A_1,\theset{0})$ | [@Kon21, Example 4.3, Proposition 4.4; §6, case (1)] |
| $\mathrm{I}$ | any $p\neq2$ | $2$ | $12$ | $10$ | $2$ | $\mathrm{D}_8$ | $(E_8\oplus A_1^{\oplus2},\ZZ/2\ZZ)$ | [@Kon21, Example 4.1, Proposition 4.2; §6, case (1)] |
| $\mathrm{II}$ | any $p\neq2$ | $1$ | $12$ | $12$ | $0$ | $S_4$ | $(D_9,\theset{0})$ | [@Kon21, Example 4.5, Proposition 4.6; §6, case (2)] |
| $\mathrm{V}$ | $3$ | $2$ | $20$ | $16$ | $4$ | $S_4\times\ZZ/2\ZZ$ | $(E_7\oplus A_2\oplus A_1^{\oplus2},(\ZZ/2\ZZ)^2)$ | [@Kon21, Example 4.7, Proposition 4.8; §6, case (4)] |
| $\mathrm{VI}$ | $3$ | $5$ | $20$ | $10$ | $10$ | $S_5$ | $(E_6\oplus D_5,\ZZ/2\ZZ)$ | [@Kon21, Example 4.9, Proposition 4.11; §6, case (5)] |
| $\mathrm{VI}$ | $5$ | $1$ | for $p\neq3$ the two fibrations give $n=1$ and the graph gives $K=E_6\oplus A_4$; the anti-invariant lattice argument in @rmk:kondo-supersingular-covers forces $p=5$ |
| $\mathrm{VII}$ | $5$ | $1$ | the fibrations give $n\in\theset{1,2}$; the anti-invariant lattice argument in @rmk:kondo-supersingular-covers forces $p=5$ in both cases; the $(\mathrm{I}_5,\mathrm{I}_5,\II)$ fibration then excludes $n=2$ |
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
| $\mathrm{II}$ | any $p\neq2$ | $1$ | $\tilde D_8$ gives $(\mathrm{I}_4^*,\mathrm{I}_1,\mathrm{I}_1)$, with Euler contribution $10+1+1=12$, by [@Kon21, §2, Table 3]; the singular points of one or two $\mathrm{I}_1$ fibres are blown up. Also $\tilde D_5+\tilde A_3$ gives $(\mathrm{I}_1^*,\mathrm{I}_4,\mathrm{I}_1)$ with the singular point(s) of one or two of its $\mathrm{I}_4$ and $\mathrm{I}_1$ fibres blown up. The first model allows $n\in\theset{1,2}$ and the second $n\in\theset{1,4,5}$, so comparing them gives $n=1$ [@Kon21, Proposition 3.8; §6, case (2)] |
| $\mathrm{III}$, $\mathrm{IV}$ | none | — | $\tilde D_4+\tilde D_4$ comes from $(\mathrm{I}_0^*,\mathrm{I}_0^*)$ with no blow-up, so the type is empty |
| $\mathrm{V}$ | $3$ | $2$ | the first two fibrations give $n=2$; comparing $\tilde E_6+\tilde A_2$ in arbitrary characteristic with its characteristic-$3$ quasi-elliptic form leaves only $p=3$, with two fibres of type $\II$ blown up |
| $\mathrm{VI}$ | $5$ | $1$ | for $p\neq3$ the two fibrations give $n=1$ and the graph gives $K=E_6\oplus A_4$; the anti-invariant lattice argument in @rmk:kondo-supersingular-covers forces $p=5$ |
| $\mathrm{VI}$ | $3$ | $5$ | for $p=3$ the alternative fibrations and the further $\tilde A_5+\tilde A_2+\tilde A_1$ and $\tilde D_5+\tilde A_3$ subdiagrams give $n=5$ [@Kon21, §6, case (5)], which is the row $(3,5)$ of Table 2 of [@Kon21, Theorem 1.1] |
| $\mathrm{VII}$ | $5$ | $1$ | the fibrations give $n\in\theset{1,2}$; the anti-invariant lattice argument in @rmk:kondo-supersingular-covers forces $p=5$ in both cases; the $(\mathrm{I}_5,\mathrm{I}_5,\II)$ fibration then excludes $n=2$ |
| $\mathrm{MI}$ | $3$ | $2$ | the four maximal parabolic subdiagrams give $n=6$ for $p\neq3$ and $n=2$ for $p=3$; $n=6$ is excluded by a $\tilde A_3+\tilde A_3+\tilde A_1+\tilde A_1$ subdiagram whose two $\tilde A_1$'s are of different kinds |
| $\mathrm{MII}$ | $3$ | $8$ | $p=3$ and $n\in\theset{2,8}$; $n=2$ is excluded by counting the $(-2)$-roots of a quasi-elliptic fibration $(\IV,\IV,\IV,\IV)$ |
:::

::: {.proof}

(1) is [@Kon21, Lemma 6.1]: for types $\mathrm{I}$--$\mathrm{VII}$ the argument passes to the Enriques surface of the same type, whose $(-2)$-curves generate $E_{10}$ by the Enriques reducibility lemma of Cossec--Dolgachev--Liedtke, and for $\mathrm{MI}$, $\mathrm{MII}$ a parabolic subdiagram of type $\tilde A_7+\tilde A_1$ or $\tilde A_3+\tilde A_3+\tilde A_1+\tilde A_1$ together with a bi-section generates a finite-index sublattice of determinant $\pm2^j$.
(2) uses [@Kon21, §6, cases (1)--(8)]. A parabolic subdiagram determines a genus-one fibration by @prop:coble-fibration-dictionary(2)--(3); its Halphen model determines the boundary components through the singular fibres that are blown up. [@Kon21, Lemmas 3.3 and 5.4] determine the kinds of roots. The characteristic-$5$ deductions in cases (5) and (6) use the proof in @rmk:kondo-supersingular-covers, not a prior assumption of the classification in Table 2.

:::

The characteristic-five rows require the additional Picard-rank and discriminant argument in @rmk:kondo-supersingular-covers. The fibration and graph inputs are independent of the classification conclusion.

::: {.remark #rmk:kondo-det-k-and-characteristic title="The rowwise characteristic restrictions"}

For type $\mathrm V$, the fibrations attached to $\tilde D_6+\tilde A_1+\tilde A_1$ and $\tilde E_7+\tilde A_1$ first give $n\in\theset{2,4}$ and $n\in\theset{1,2,3}$, hence $n=2$. The subdiagram $\tilde E_6+\tilde A_2$ then leaves only the characteristic-$3$ quasi-elliptic alternative: blowing up two fibres of type $\II$ produces the required two boundary components. Thus $p=3$ [@Kon21, §6, case (4)].

For type $\mathrm{VI}$ with $p\neq3$, the fibrations attached to $\tilde E_6+\tilde A_2$ and $\tilde A_4+\tilde A_4$ give $n=1$, and the graph determines $K=E_6\oplus A_4$ [@Kon21, §6, case (5), p. 38]. The anti-invariant argument below proves supersingularity and $p=5$ from these inputs. If $p=3$, the alternative fibrations and further subdiagrams $\tilde A_5+\tilde A_2+\tilde A_1$ and $\tilde D_5+\tilde A_3$ give $n=5$ by the same case of the source.

For type $\mathrm{VII}$, [@Kon21, §6, case (6), p. 39] first gives $n\in\theset{1,2}$ and proves that the fifteen vertices joined by single edges represent genuine $(-2)$-curves. The proof below uses these inputs to force $p=5$ before excluding the two-boundary case; it does not use the already classified characteristic-$5$ example.

For type $\mathrm{MI}$, the four maximal parabolic subdiagrams give $n=6$ if $p\neq3$ and $n=2$ if $p=3$. Under $n=6$, the first fibration makes all triads $(-2)$-curves, all duads $(-1)$-roots, and all synthemes $(-2)$-curves (after interchanging duads and synthemes if necessary). In the fibration $(\mathrm{I}_4,\mathrm{I}_4,\mathrm{I}_2,\mathrm{I}_2)$ attached to $\tilde A_3+\tilde A_3+\tilde A_1+\tilde A_1$, one $\mathrm{I}_2$ fibre is blown up and the other is not; but one $\tilde A_1$ consists of a duad and a syntheme, while the other consists of triads. These root-kind assignments are incompatible, so $p=3$ and $n=2$ [@Kon21, §6, case (7); @Kon21, Lemma 4.18].

For type $\mathrm{MII}$, the maximal parabolic subdiagrams force $p=3$ and $n\in\theset{2,8}$. If $n=2$, the quasi-elliptic fibration $(\IV,\IV,\IV,\IV)$ would make all forty vertices $(-2)$-curves, whereas the blown-up $\mathrm{I}_2$ fibre in $(\mathrm{I}_4,\mathrm{I}_4,\mathrm{I}_2,\mathrm{I}_2)$ supplies a $(-1)$-root. Thus $n=8$ [@Kon21, §6, case (8); @Kon21, Lemma 4.21]. Types $\mathrm I$ and $\mathrm{II}$ instead have examples in every characteristic $p\neq2$, and types $\mathrm{III}$ and $\mathrm{IV}$ are empty by their fibration configurations [@Kon21, §6, cases (1)--(4)].
:::

::: {.remark #rmk:kondo-supersingular-covers title="Picard rank and the characteristic-five restrictions"}

Let $S$ be a strong Coble surface over an algebraically closed field of characteristic $p\neq2$, with $n$ boundary components, and let $\pi\colon X\to S$ be its smooth canonical K3 cover with covering involution $\sigma$. Set $P=\Pic(X)$, $P_+=P^\sigma$, $N=\ker(1+\sigma^*)$, and $b_i=\tilde B_i$. The two pull-push identities $\pi_*\pi^*=2$ and $\pi^*\pi_*=1+\sigma^*$ imply
$$
(P_+)_{\QQ}=\pi^*\Pic(S)_{\QQ},\qquad
\rank P_+=10+n .
$$
Indeed $K_S^2=-n$, and a rational surface has Picard rank $10-K_S^2$. The $b_i$ are invariant, pairwise orthogonal, of square $-2$. In Kondō's notation $L^+=\pi^*\CM(S)$ is orthogonal to the $b_i$; consequently
$$
(L^-)_{\QQ}=N_{\QQ}\perp\bigoplus_i\QQ b_i .
$$
Here $L^-$ is not the true anti-invariant lattice. The latter $N$ is negative definite by the Hodge index theorem, since it is orthogonal to the pullback of an ample divisor of $S$. It contains no vector of square $-2$: K3 Riemann--Roch makes one sign of such a vector effective, contrary to its zero intersection with that ample divisor.

For a generator $\delta^-\in h^-$ of $K(2)$, its compatible half-sum with an element of $L^+$ is integral. Pairing the half-sum with $b_i$ gives $(\delta^-,b_i)\in2\ZZ$. Thus $c_i=-(\delta^-,b_i)/2$ is integral and
$$
\eta=\delta^--\sum_i c_i b_i\in N,\qquad
\eta^2=-4+2\sum_i c_i^2.
$$
Negative definiteness and the absence of square-$-2$ vectors imply either every $c_i=0$, or $\sum_i c_i^2=2$ and $\eta=0$. In particular when $n=1$, every generator of $K(2)$ belongs to $N$, and
$$
\rho(X)\ge 11+\rank K .
$$
For arbitrary $n$, the inclusion $K(2)\subset L^-$ still gives $\rho(X)\ge10+\rank K$.

**Supersingularity and the odd-primary discriminant.** For a smooth K3 surface $\rho\ge21$ excludes characteristic zero (over $\CC$ use $h^{1,1}=20$; in general descend the surface and a finite set of independent divisor classes to a finitely generated characteristic-zero field and embed it into $\CC$). In positive characteristic the height inequality $\rho\le22-2h$ for finite height $h\ge1$ and the supersingular Tate theorem imply $\rho=22$ [@Mat23K3Mu, Lemma 8.3(2),(4)]. Artin's discriminant theorem now applies [@Kon21, Proposition 3.16]:
$$
A_P\iso(\ZZ/p)^{2\sigma_0},\qquad 1\le\sigma_0\le10.
$$
Over $\ZZ_p$, the projectors $(1\pm\sigma^*)/2$ give the integral orthogonal decomposition $P_{\ZZ_p}=(P_+)_{\ZZ_p}\perp N_{\ZZ_p}$. The invariant summand is $\pi^*\Pic(S)_{\ZZ_p}$ by the same pull-push identities, and is unimodular: the intersection lattice of a smooth rational surface is unimodular (a minimal rational surface has this property and a blow-up adds an orthogonal square-$-1$ generator); scaling its form by the unit $2$ preserves unimodularity. Hence
$$
A_{N_{\ZZ_p}}\iso(\ZZ/p)^{2\sigma_0}.
$$
If a nondegenerate integral sublattice $R\subset N$ has corank one and $p\nmid\det R$, the inverse Gram matrix of $R$ over $\ZZ_p$ gives an integral orthogonal projection onto $R_{\ZZ_p}$. Thus $N_{\ZZ_p}=R_{\ZZ_p}\perp R_{\ZZ_p}^{\perp}$, with a rank-one complement. Its discriminant group is cyclic, contradicting $2\sigma_0\ge2$. Therefore $p\mid\det R$. This argument requires no primitivity of $R$ over $\ZZ$.

**Type VI with $p\neq3$.** The preliminary deductions of [@Kon21, §6, case (5), p. 38] give $n=1$ and $K=E_6\oplus A_4$, before any assertion about $p=5$. Thus $R=K(2)\subset N$ has rank ten, giving $\rho\ge21$. The preceding argument yields $\rho=22$, $\rank N=11$, and
$$
p\mid|\det R|=2^{10}\cdot3\cdot5.
$$
Since $p\neq2,3$, necessarily $p=5$.

**Type VII.** The preliminary deductions of [@Kon21, §6, case (6), p. 39] give $n=1$ or $2$, and the fifteen vertices in the single-edge subgraph are genuine $(-2)$-curves. The abstract graph of type VII is described in [@MO15Mathieu, §1.2, pp. 6--7 and Remark 1.4]: these fifteen vertices form the line graph of the Petersen graph, and five further vertices each have intersection $0$ or $2$ with them. Only these graph incidences are used, not the Enriques-surface geometry of that source. In the realization of the Petersen graph by the two-element subsets of $\theset{1,2,3,4,5}$, with disjoint pairs adjacent, the path
$$
12,\ 34,\ 15,\ 23,\ 45,\ 13,\ 24,\ 35,\ 14,\ 25
$$
has ten distinct vertices and consecutive pairs are disjoint. Its nine edges induce a path in the line graph.

For a genuine $(-2)$-curve $C$ on $S$, adjunction gives $K_S\cdot C=0$, so $B\cdot C=-2K_S\cdot C=0$ and $C$ misses the branch. Its inverse image consists of two disjoint rational curves $C^+,C^-$: the restriction is an étale double cover of $\PP^1$, which is trivial by Riemann--Hurwitz. Then $d_C=C^+-C^-\in N$ has square $-4$. For two such curves put $a=C^+\cdot D^+$ and $b=C^+\cdot D^-$. The deck involution and the projection formula give $a+b=C\cdot D$ and $d_C\cdot d_D=2(a-b)$. Thus the nine curves corresponding to the chosen path have difference classes with squares $-4$, pairings $\pm2$ along its edges, and zero elsewhere. Choosing signs successively along the path gives $A_9(2)\subset N$ (negative definite convention).

If $n=2$, this rank-nine lattice and the rank-twelve invariant lattice give $\rho\ge21$. Hence $\rho=22$ and $\rank N=10$. Applying the corank-one obstruction to $R=A_9(2)$ gives $p\mid2^9\cdot10$, so $p=5$.

If $n=1$, all effective irreducible roots are genuine $(-2)$-curves [@Kon21, Lemma 3.2 and §6, case (6)]. For one of the five further vertices $r$, the corresponding $d_r$ has pairings $0$ or $\pm4$ with the fifteen differences. In the negative definite space $N_{\QQ}$, a pairing of absolute value $4$ between vectors of square $-4$ forces equality up to sign by Cauchy--Schwarz. Each vertex of the line graph has a single-edge neighbour, however, with difference pairing of absolute value $2$. Such equality would contradict the $0,\pm4$ pairings of $d_r$ with the entire family. Thus $d_r$ is orthogonal to the fifteen differences, and $R=A_9(2)\perp A_1(2)\subset N$ has rank ten. The rank-eleven invariant lattice gives $\rho\ge21$, whence $\rho=22$, $\rank N=11$, and $p\mid 2^{10}\cdot10\cdot2$. Again $p=5$.

With $p=5$ established in both cases, the $\tilde A_4+\tilde A_4$ subdiagram corresponds to a Halphen model with fibres $(\mathrm{I}_5,\mathrm{I}_5,\II)$ [@Kon21, §6, case (6)]. By [@Kon21, Proposition 3.8 and proof of Lemma 3.9], one reduced singular fibre is blown up in the index-two case, or two in the index-one case. Blowing up a fibre of type $\mathrm{I}_5$ yields five boundary components and blowing up one of type $\II$ yields one. The resulting possible numbers are $5,1,10,6$, none equal to $2$. Thus $n=1$.

For the characteristic-three examples of type V with $n=2$ and type VI with $n=5$, [@Kon21, Propositions 4.8 and 4.11] gives root lattices of rank eleven, so the general inequality $\rho\ge10+\rank K$ already implies supersingularity by Lemma 8.3 of [@Mat23K3Mu]. For the types MI and MII the covers are the Fermat quartic and the Kummer surface of the product of two supersingular elliptic curves, respectively, both supersingular of Artin invariant $1$ [@Kon21, Examples 4.17 and 4.20].

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
3. At $\alpha=1$, $C_1=Q_1Q_2$ with $Q_\pm\colon u_1v_0\mp u_0v_1=0$, and $\sigma$ has two fixed curves; $S=X/\langle\sigma\rangle$ is the type $\mathrm{I}$ strong Coble surface with two boundary components and twelve effective irreducible roots, ten $(-2)$-curves and two $(-1)$-roots, with dual graph $\Gamma_{\mathrm{I}}$, $\Aut(S)\iso\mathrm{D}_8$ and $R$-invariant $(E_8\oplus A_1^{\oplus2},\ZZ/2\ZZ)$ [@Kon21, Example 4.1, Proposition 4.2].
4. At $\alpha=\tfrac12$ and $\alpha=\tfrac32$ the singularity of $C_\alpha$ at the fixed point is an ordinary node, with quadratic term $u^2+w^2$ in the coordinates $u=u_0/u_1$, $w=v_1/v_0$ at $(0:1,1:0)$ and quadratic term $-(A^2+B^2)$ in $A=u_1/u_0$, $B=v_0/v_1$ at $(1:0,0:1)$; $\sigma$ has one fixed curve; $S$ is the type $\mathrm{I}$ strong Coble surface with one boundary component, twelve $(-2)$-curves, $\Aut(S)\iso\mathrm{D}_8$ and $R$-invariant $(E_8\oplus A_1,\theset{0})$ [@Kon21, Example 4.3, Proposition 4.4].
   By the uniqueness clause of @thm:kondo-finite-aut-classification the two surfaces are isomorphic.
:::

::: {.proof}

(1) is immediate from the action of $\phi$; none of the four points satisfies $u_0=\pm u_1$ or $v_0=\pm v_1$, both of which need both coordinates nonzero.

(2) Evaluating the defining equation of $C_\alpha$ at the four fixed points gives $2=2\alpha$, $-2=1-2\alpha$, $-1=-2\alpha$ and $1=2\alpha-1$, that is $\alpha=1$, $\alpha=\tfrac32$, $\alpha=\tfrac12$ and $\alpha=1$, so the values are as listed and no other $\alpha$ puts a fixed point on $C_\alpha$. Since the branch divisor is $C_\alpha+\sum L_i$ and $\sigma$ fixes a curve exactly over the fixed points of $\phi$ lying on the branch divisor, $\sigma$ is fixed point free away from those three values, and $X/\langle\sigma\rangle$ is an Enriques surface.

(3) is [@Kon21, Example 4.1, Proposition 4.2], with the splitting $C_1=Q_1Q_2$ checked by expansion: $(2u_0^2-u_1^2)(v_0^2-v_1^2)-(2v_0^2-v_1^2)(u_0^2-u_1^2)=u_1^2v_0^2-u_0^2v_1^2=Q_1Q_2$.

(4) Substituting $u_0=u$, $u_1=1$, $v_0=1$, $v_1=w$ at $\alpha=\tfrac12$ gives $-2u^2w^2+u^2+w^2$, whose lowest-degree part is $u^2+w^2$: a nondegenerate quadratic form if and only if $p\neq2$, so the point is an ordinary node and not a cusp. At $\alpha=\tfrac32$ the same substitution with $u_0=1$, $u_1=A$, $v_0=B$, $v_1=1$ gives $2A^2B^2-A^2-B^2$, whose quadratic term is $-(A^2+B^2)$, the same shape. The identification of the surfaces is [@Kon21, Example 4.3, Proposition 4.4].

:::

Two remarks on @prop:kondo-type-i-one-boundary.

First, in (4) the quadratic term of the local branch equation is nondegenerate precisely in characteristic different from $2$. In characteristic $2$ the tangent cone is the double line $(u+w)^2=0$, and the separable double-cover construction and its covering involution used in the proposition do not apply. This does not exclude characteristic-two Coble surfaces, whose canonical covers are described in @prop:strong-coble-is-terminal-coble.

Second, the one-boundary members at $\alpha=\tfrac12,\tfrac32$ are exchanged by the factor interchange $s(u,v)=(v,u)$. Write $F_\alpha$ for the left side of the branch equation minus the right side. Expansion gives
$$
F_\alpha(u,v)=(2-2\alpha)(u_0^2v_0^2+u_1^2v_1^2)+(2\alpha-3)u_0^2v_1^2+(2\alpha-1)u_1^2v_0^2,
$$
hence $F_{2-\alpha}(v,u)=-F_\alpha(u,v)$. The remaining four branch fibres are exchanged by $s$. On the double cover given by $w^2=(u_0^2-u_1^2)(v_0^2-v_1^2)F_\alpha$, in the total space of $\OO(2,2)$, the factor interchange of this line bundle followed by multiplication by $i$ with $i^2=-1$ induces $(u,v,w)\mapsto(v,u,iw)$ to the cover for $2-\alpha$. It lifts to the minimal resolutions. On the chart $u_0v_0\neq0$, the Enriques-type lift acts by $(u_1/u_0,v_1/v_0,w)\mapsto(-u_1/u_0,-v_1/v_0,-w)$: the sign exchanges the two sheets over the off-branch fixed base point $(1:0,1:0)$. The displayed isomorphism commutes with this lift on the dense chart, hence everywhere, and descends to the Coble quotients. The two models are therefore equivalent when the rulings are not labelled.

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

(1) $\CM(S)\iso E_{10}$ and $\CM(S)=K_S^{\perp}$ are @prop:kondo-coble-mukai-is-e10 for $n=1$. @lem:kondo-exhibited-graph-finiteness, whose type $\mathrm I$ input is the same graph $\Gamma_{\mathrm I}$ of [@Kon21, Example 4.1] transferred to Example 4.3, gives finite index of $W(\Gamma_{\mathrm I})$ in $\Orth(\CM(S))$. A reflection group of finite index cannot fix a nonzero vector, so the twelve root classes generate $\CM(S)\tensor\QQ$.

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
That proposition gives the absence of ten pairwise disjoint $(-1)$-curves; the exceptional curves of a morphism with ten distinct centres are ten pairwise disjoint $(-1)$-curves, so no such morphism exists. By @thm:coble-smooth-antibicanonical-is-a-plane-blowup(4), if a plane model had ten distinct centres, $Z$ would have exactly ten double points, each an ordinary node **or an ordinary cusp**. Such a model is excluded here, and in particular a presentation by ten distinct ordinary nodes is impossible.

:::

::: {.remark #rmk:kondo-what-the-classification-does-not-decide title="What the classification does not decide"}

Three statements are outside @thm:kondo-finite-aut-classification, and none of them follows from it.

1. *Isomorphism with any other non-classical object.* The one-boundary type $\mathrm{I}$ surface is non-classical by @cor:type-i-one-boundary-not-classical, and so are the surfaces $S_{Z_8}$ and $S_{Z_{64}}$ of @ex:coble-sextics-with-an-a15-point. The corollary does not assert non-classicality of the two-boundary type $\mathrm{I}$ surface. Sharing the property "non-classical" is not an isomorphism, and no comparison between the twelve-root configuration of @prop:kondo-type-i-one-boundary(4) and the configurations of those two surfaces is made here or in [@Kon21]. What the example gives the complex theory is a second, independent supply of objects with an $E_8$ configuration of $(-2)$-curves, hence a second family of plane models whose ten centres cannot be ten distinct nodes.
2. *A presentation by ten distinct centres.* The contrary is proved: @cor:type-i-one-boundary-not-classical.
3. *Monodromy.* Finiteness of $\Aut(S)$ at the nine surfaces is isotropy data at nine objects. The monodromy of a local system on a moduli stack is a property of a family over a base, computed from loops, and it is not a function of the automorphism group of a single fibre; @thm:kondo-finite-aut-classification constructs no family and no base, so it yields no statement about the monodromy groups $\Gamma_\Co$ and $\Gamma_{\Co,2}$ of the Coble families, and none about which lattice group the stack's monodromy is. In particular the nine surfaces do not supply a computation of the monodromy of $\mcM_\Co$ over $\CC$; the finite-isotropy locus being nine points is compatible with a monodromy group that is large on the complement.

:::

Related: [Constructions of the moduli space](#sec-moduli-construction), [The research program for $F_{\Co,n}$](#sec-coble-families-research-program), [The Coble cusp correspondence and the morphism chain](#sec-cusp-correspondence-morphism-chain).
