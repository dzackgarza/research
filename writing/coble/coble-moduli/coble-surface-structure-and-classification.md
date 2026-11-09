---
unit: reference
status: source-backed
tags:
  - coble
  - classification
  - automorphisms
  - halphen
---

# Structure and classification facts for Coble surfaces

## Negative curves

::: {.proposition #prop:coble-negative-curve-norms title="Norms of smooth rational negative curves"}

Let $S$ be a terminal Coble surface of K3 type with anti-bicanonical curve $C$.
Every smooth rational curve $E \iscontainedin S$ with $E^2 < 0$ satisfies
$$
E^2 \in \theset{-1,\, -2,\, -4},
$$
and if $E^2 = -4$ then $E$ is an irreducible component of $C$ [@DK25, Lem. 9.1.2].
:::

::: {.proof}

Adjunction on the smooth rational curve $E$ gives $E^2 = -2 - E\cdot K_S$.
Since $C\sim -2K_S$, this is $E^2 = -2 + \tfrac12\,E\cdot C$.
If $E$ is not a component of $C$, then $E\cdot C\geq 0$, and $E\cdot C = -2E\cdot K_S$ is even.
The values $E\cdot C = 0$ and $E\cdot C = 2$ give $E^2 = -2$ and $E^2 = -1$, and $E\cdot C\geq 4$ gives $E^2\geq 0$, which is excluded.
If $E$ is a component of $C$, then $E$ is a boundary component and $E^2 = -4$ by @def:coble-surface.
:::

## Automorphisms

::: {.theorem #thm:coble-aut-lattice title="Coble's theorem, lattice form"}

Let $S$ be the blowup of $\PP^2$ at the ten nodes of an irreducible rational plane sextic whose singular points are ordinary nodes, and let $M_S \definedas K_S^{\perp\, \Pic(S)}$.
The Cremona equivalence class of such a sextic is the union of finitely many projective equivalence classes.
Then $\Aut(S)$ is isomorphic to a subgroup of finite index in $\Orth(M_S)$.
For a general such sextic, this subgroup is isomorphic to the congruence subgroup of level $2$ of $\Orth(M_S)/\theset{\pm1}$, and $\Orth(M_S)/\theset{\pm1}$ is isomorphic to the Weyl group $W(E_{10})$ [@DZ99, Introduction].
:::

::: {.proposition #prop:coble-negative-curves-finite title="Finiteness of negative curves modulo automorphisms"}

Let $S$ be the blowup of $\PP^2$ at the ten nodes of an irreducible plane sextic.
Then the set of smooth rational curves on $S$ with negative self-intersection is finite modulo $\Aut(S)$.
This finiteness fails for a general blowup of $\PP^2$ at $9$ or more points [@DZ99, Introduction].
:::

::: {.question #qst:coble-negative-curves-finite title="Rational surfaces with finitely many negative curves modulo automorphisms"}

Which rational surfaces have only finitely many smooth rational curves of negative self-intersection modulo their automorphism group?
In particular, does every Coble surface of rational type in the sense of @def:coble-elliptic-rational-type contain only finitely many smooth rational curves of negative self-intersection [@DZ99, Introduction]?
:::

## The Coble-Mukai lattice

::: {.definition #def:coble-mukai-lattice title="Coble-Mukai lattice"}

Let $S$ be a terminal Coble surface of K3 type with boundary components $C_1,\ldots,C_n$, and let $\beta_i\in\Pic(S)$ be the class of $C_i$.
Let $\widetilde{\Pic}(S)$ be the $\ZZ$-submodule of $\Pic(S)_\QQ$ spanned by $\Pic(S)$ and $\tfrac12\beta_1,\ldots,\tfrac12\beta_n$.
The **Coble-Mukai lattice** of $S$ is
$$
\CM(S) \definedas \theset{x\in\widetilde{\Pic}(S) \suchthat x\cdot\beta_i = 0 \text{ for } i = 1,\ldots,n}
,
$$
with the restriction of the intersection form of $\Pic(S)_\QQ$ [@DK25, §9.2].
:::

::: {.proposition #prop:coble-mukai-lattice title="The Coble-Mukai lattice is the Enriques lattice"}

Let $S$ be a terminal Coble surface of K3 type with $n$ boundary components.

1. The form on $\CM(S)$ takes integer values [@DK25, §9.2].
2. The quotient $\widetilde{\Pic}(S)/\Pic(S)$ is an $\mathbb{F}_2$-vector space of dimension at most $n-1$.
3. $\CM(S)$ has rank $10$ and signature $(1,9)$.
4. $\Aut(S)$ permutes the curves $C_1,\ldots,C_n$ and so acts on $\CM(S)$ [@DK25, §9.2].
5. If $n = 1$, then $\CM(S) = K_S^{\perp\,\Pic(S)}$, and it is isomorphic to the Enriques lattice $E_{10}$ [@DK25, §9.2].
6. Over $\CC$, $\CM(S)$ is isomorphic to $E_{10}$ for every $n$ [@DK25, Thm. 9.2.14].

:::

::: {.proof}

(1) Let $x, x'\in\CM(S)$, and write $x = y + \tfrac12\Sum_i r_i\beta_i$ and $x' = y' + \tfrac12\Sum_i r'_i\beta_i$ with $y, y'\in\Pic(S)$ and $r_i, r'_i\in\ZZ$.
By @prop:coble-boundary-intersections, $\beta_i\cdot\beta_j = -4\delta_{ij}$.
Since $x\cdot\beta_i = x'\cdot\beta_i = 0$,
$$
y\cdot y' = x\cdot x' + \tfrac14\Sum_i r_i r'_i\,\beta_i^2 = x\cdot x' - \Sum_i r_i r'_i
,
$$
so $x\cdot x' = y\cdot y' + \Sum_i r_i r'_i\in\ZZ$.

(2) The quotient is spanned by the classes of $\tfrac12\beta_1,\ldots,\tfrac12\beta_n$, and $2\cdot\tfrac12\beta_i = \beta_i\in\Pic(S)$, so it is an $\mathbb{F}_2$-vector space.
Since $C\sim -2K_S$, $\Sum_i\tfrac12\beta_i = \tfrac12[C] = -K_S\in\Pic(S)$, so the $n$ spanning classes satisfy a nontrivial relation.

(3) By @prop:terminal-coble-basic-rational and @prop:blowup-geometric-basis, $\Pic(S)\cong\latI_{1,9+n}$, of rank $10+n$ and signature $(1, 9+n)$.
$\CM(S)\tensor\QQ$ is the orthogonal complement in $\Pic(S)_\QQ$ of the span of $\beta_1,\ldots,\beta_n$.
By @prop:coble-boundary-intersections, that span is negative definite of rank $n$.
So its orthogonal complement has rank $10$ and signature $(1,9)$.

:::

::: {.question #qst:coble-mukai-naturality title="Is the Coble--Mukai lattice the natural home for the group action?"}

Is $\CM(S)$ rather than $S_{\Co}$ the natural home for the action of $\Gamma_{\Co}$, and how are the two related?
:::

## The Dolgachev-Zhang classification

::: {.definition #def:coble-elliptic-rational-type title="Elliptic and rational types"}

Let $X$ be a Coble surface, let $E$ be a $(-1)$-curve on $X$ with blowdown $\pi\colon X\to Y$, and assume that $p_a(-2K_X + 2E) = 1$.
Write $\abs{-2K_X + 2E} = \abs{M} + P$, where $\abs{M}$ is the mobile part and $P$ is the fixed part.
Then $X$ is of **elliptic type with respect to $E$** if $p_a(M) = 1$, and of **rational type with respect to $E$** if $p_a(M) = 0$ [@DZ99, 2.1].
A Coble surface is of **elliptic type** if it is of Halphen type or of Jacobian type, and of **rational type** if it is not of elliptic type [@DZ99, 2.9].
:::

::: {.theorem #thm:coble-elliptic-type-classification title="Coble surfaces of elliptic type"}

A Coble surface of elliptic type admits a birational morphism onto a surface $Y$ such that $\abs{-K_Y}$ has exactly one member and a general member of the mobile part of $\abs{-2K_Y}$ is a smooth elliptic curve.
It is obtained in one of two ways:

- **Halphen type**: as a blowup of singular points, and their infinitely near points, of a non-multiple fibre of a minimal rational elliptic surface with one multiple fibre, of multiplicity $2$;

- **Jacobian type**: as a blowdown of some disjoint sections, and possibly of components of one fibre, of a non-minimal rational elliptic surface with a section.

A Coble surface of elliptic type admits a birational morphism onto $\PP^2$ [@DZ99, Introduction].
:::

::: {.theorem #thm:dz-k3-type-criterion title="K3 type criterion"}

Let $X$ be a Coble surface with $M^2 = 0$, for $M$ as in @def:coble-elliptic-rational-type.

- If $X$ is of Halphen type, obtained from a minimal Halphen surface $Y_m$ of index $2$ by one blowup of a singular point on its non-multiple fibre $F$, then $X$ is of K3 type if and only if $F$ has type $I_n$, $\II$, $\III$ or $\IV$.

- If $X$ is of Jacobian type, obtained from a minimal Jacobian rational elliptic surface by blowing up a singular point of one fibre $F$ and at least one singular point, with its infinitely near points, of another fibre $F_1$, then $X$ is of K3 type if and only if each of $F$ and $F_1$ has type $I_n$, $\II$, $\III$ or $\IV$.

[@DZ99, Thm. 6.5]
:::

::: {.lemma #lem:dz-k3-type-double-cover title="K3 type and the double cover"}

For a Coble surface $X$ the following are equivalent:

1. $\abs{-2K_X}$ contains a reduced divisor;

2. there is a double cover $\tilde X \to X$ with $\tilde X$ a K3 surface with at most ordinary double points.

[@DZ99, Lem. 6.2]
:::

## Rational log Enriques surfaces of index 2

::: {.definition #def:rational-log-enriques title="Rational log Enriques surface of index 2"}

A **rational log Enriques surface of index $2$** is a normal rational surface $\bar X$ with at worst quotient singularities such that $\OO(-2K_{\bar X}) \cong \OO_{\bar X}$ [@DZ99, §6].
:::

::: {.theorem #thm:coble-log-enriques-resolution title="Terminal Coble surfaces are resolutions of log Enriques surfaces"}

1. The minimal resolution $X$ of a rational log Enriques surface of index $2$ is a Coble surface with $h^0(-2K_X) = 1$. The unique member $D\in\abs{-2K_X}$ is reduced, and each connected component of $D$ is either a single $(-4)$-curve or a linear chain with dual graph
$$
(-3) - (-2) - \cdots - (-2) - (-3)
.
$$
Conversely, a Coble surface with these properties is the minimal resolution of a rational log Enriques surface of index $2$.
2. A Coble surface is terminal if and only if it has exactly one anti-bicanonical divisor $D$, and $D$ is reduced and a disjoint union of $(-4)$-curves.
3. The minimal resolution of a rational normal surface with at worst singularities of type $\tfrac14(1,1)$ is a terminal Coble surface, and conversely.

[@DZ99, Prop. 6.4]
A terminal Coble surface is the minimal resolution of a maximum rational log Enriques surface of index $2$ [@DZ99, Introduction].
:::

## Dolgachev-Kondo geometry of the degree 2 polarization

::: {.proposition #prop:coble-degree-two-branch-geometry title="The branch geometry of a degree 2 polarization"}

Let $S$ be a Coble surface with no $(-2)$-curves, and let $h = [F_1 + F_2] \in \Pic(S)$ be a polarization of degree $2$.
Then $\abs{2h}$ defines a morphism $\phi_h\colon S \to \PP^4$ whose image $\mathsf{D}$ is a $4$-nodal quartic del Pezzo surface.
Let $\sigma$ be its deck transformation, and let $C \in \abs{-2K_S}$ be the anti-bicanonical curve.

1. $\Fix(\sigma)$ is the union of a smooth curve $\bar W$ of genus $4$ and three isolated points.
2. $\phi_h(C) = \theset{q}$ is a singular point of $\mathsf{D}$, and the other three singular points of $\mathsf{D}$ are the images of the isolated fixed points.
3. $\bar W$ meets $C$ in two points.
4. $W \definedas \phi_h(\bar W)$ has $p_a(W) = 5$ and a double point at $q$, and it is the complete intersection of a net of quadrics.

So a Coble surface is obtained as a degeneration of an Enriques surface when the branch curve $W$ of $\phi_h$ passes through a singular point of $\mathsf{D}$ [@DK13, §8].
:::

::: {.proposition #prop:cuspidal-quintics-enriques title="Cuspidal quintics and Enriques surfaces"}

Let $\mcm_{\cusp}$ be the moduli space of cuspidal plane quintics, the GIT quotient of the projective space of cuspidal plane quintics by $\PGL_3$.
Then $\mcm_{\cusp}$ is a rational variety, birationally isomorphic to the moduli space $\mcm_{\En}$ of Enriques surfaces [@DK13, §4].
The locus $\mcm'_{5,\cusp}$ of @thm:coble-moduli-rational is a rational variety of dimension $9$ [@DK13, Thm. 4.1].
:::

Related: [The research program for $F_{\Co,n}$, $2 \leq n \leq 10$](#sec-coble-families-research-program), [Moduli of index 2 Halphen and rational elliptic surfaces](#sec-halphen-index-2-moduli-program), [The Coble cusp correspondence and the morphism chain](#sec-cusp-correspondence-morphism-chain).
