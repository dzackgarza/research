# The cusps of $D(T_\Co)/R$ over Sterk's cusps {#sec-cusps-over-sterk-cusps}

This section proves statement B2 of the plan for $F_\Co$ [research#786, Part I §5; research#789]: the $0$- and the $1$-cusps of $D(T_\Co)/R$ are the $\gent$-orbits of pairs $(\ell,\alpha)$, an isotropic line or plane $\ell$ of $\ten$ together with a $(-2)$-vector $\alpha$ perpendicular to it, and they fibre over Sterk's cusps of $F_{\En,2}$ by forgetting $\alpha$. The fibre over Sterk's cusp $[e_k]$ is the set of $\Stab_{\gent}(e_k)$-orbits of $(-2)$-vectors perpendicular to $e_k$, where the stabilizer is that of the isotropic *line* $\ZZ e_k$. The smallest case of that computation, Sterk's cusp $2$, is carried out here: the $(-2)$-vectors perpendicular to its representative form a single $\Orth(K_{\eta_2})$-orbit. Every statement below names its group, and none of the counts is a count for $F_\Co$ or $F_{\Co,2}$: the group of this page is $R = \bar\rho^{-1}(P)$, of index $67\,456$ in $\Orth(T_\Co)$, whereas $\fco$ is $\bD(T_\Co)/\Gamma_\Co$, only $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ is proved on the labelled presentation, and both that equality and $\Gamma_\Co=\Gamma_\Co(B)$ are open (@thm:gamma-co-is-stable(1),(2), @conj:gamma-co-stable, research#797, item 6); the counts $527$ and $189\,720$ are those of the stable quotient $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ (@thm:coble-zero-cusp-count(2), @thm:coble-plane-orbit-counts(2)), and for $\fco$ they hold only under the equality. The passage from the counts below to $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$ would be @qst:coble-monodromy-equality, whose forward inclusion is @thm:coble-monodromy-versus-enriques(4), conditional on (U) of @lem:coble-family-identification; that equality is false (@prop:coble-monodromy-equality-false), so the counts below are not asserted for $F_{\Co,2}$.

## Setting

Let $L = \latII_{3,19} = U^{\oplus3}\oplus E_8^{\oplus2}$ be the K3 lattice and
$$
\ten = U\oplus U(2)\oplus E_8(2)\cong(12,10,0)_2
$$
the lattice of [@AEGS25, Def. 2.3], with basis $e,f,e',f',\alpha_1,\dots,\alpha_8$: $e\cdot f = 1$, $e'\cdot f' = 2$, and $\alpha_1,\dots,\alpha_8$ the simple roots of the summand $E_8(2)$, of square $-4$. Put
$$
\delta \definedas e - f,\qquad \delta^2 = -2,\qquad
T_\Co \definedas \delta^{\perp\ten} = \generators{e+f}\oplus U(2)\oplus E_8(2)\cong\generators{2}\oplus E(2),
$$
the Coble lattice of [@DK13, (3.6) and Prop. 3.2]; the identification of $\generators{e+f}$ with $\generators{2}$ uses $(e+f)^2 = 2\,e\cdot f = 2$.

The boundary lattices are those of @prop:sterk-cusp-quotients and @thm:coble-cusp-admissibility: for a primitive isotropic line $I = \ZZ e$ of $\ten$ and a primitive isotropic plane $J$ of $\ten$,
$$
K_I \definedas e^{\perp\ten}/\ZZ e, \qquad K_J \definedas J^{\perp\ten}/J,
$$
and for Sterk's representatives $K_{\eta_k} \definedas \eta_k^{\perp\ten}/\ZZ\eta_k$. A quotient of a plane is also written $\Pi^{\perp\ten}/\Pi$; $L_0$ below is $K_\Pi$.

Let
$$
\gent = \Gamma_{\En,2}\leq\Orth(\ten)
$$
be the image of $\{g\in\Orth(L) : g\Ien = \Ien g,\ g(h) = h\}$, $h$ the degree-$2$ polarization [@AEGS25, Def. 2.6]; this is the group $\Gamma$ of [@Ste91, Prop. 2.7], characterised there as the set of isometries of $\ten$ whose induced map on $A_{\ten} = A_{U(2)}\oplus A_{E_8(2)}$ respects the two summands. Let
$$
R \definedas R_{\gent} = \text{the image of } \Stab_{\gent}(\delta) \text{ in } \Orth(\delta^{\perp\ten}) = \Orth(T_\Co)
$$
[@def:gamma-co-groups(4)]; equivalently $R = \bar\rho^{-1}(P)$, where $\bar\rho\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is the discriminant representation and $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ the stabilizer of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$, so that
$$
[\Orth(T_\Co):R] = \abs{\Orth(q_{T_\Co})}/\abs{P} = 2^7\cdot17\cdot31 = 67\,456
$$
[@prop:gamma-co-images(3), @thm:gamma-co-2-comparison(3)].

The boundary components of a type IV quotient $D(\Lambda)/\Gamma$ are described as follows: a $0$-cusp is a $\Gamma$-orbit of primitive isotropic lines of $\Lambda$, a $1$-cusp a $\Gamma$-orbit of primitive isotropic planes [@AEGS25, Def. 2.9]. Sterk's five $0$-cusps of $F_{\En,2} = D(\ten)/\gent$ are represented by
$$
e,\qquad e',\qquad e'+f'+y_3,\qquad 2e'+f'+y_4,\qquad 2e+2f+y_4,
$$
with $y_3 = -(2\alpha_1+3\alpha_2+4\alpha_3+6\alpha_4+5\alpha_5+4\alpha_6+3\alpha_7+2\alpha_8)$ of square $-4$ and $y_4 = -(4\alpha_1+5\alpha_2+7\alpha_3+10\alpha_4+8\alpha_5+6\alpha_6+4\alpha_7+2\alpha_8)$ of square $-8$ [@Ste91, (4.2.3)], and are numbered $1,\dots,5$ in that order; the numbering and the vectors are those of @ex:sterk-isotropic-divisibilities. Throughout, $\Stab_{\gent}(e_k)$ denotes the stabilizer in $\gent$ of the line $\ZZ e_k$.

## Primitivity

::: {.lemma #lem:primitivity-tco-in-ten title="A vector primitive in $T_\Co$ is primitive in $\ten$"}
If $v\in T_\Co$ is primitive (@def:primitive-embedding) in $T_\Co$, it is primitive in $\ten$.
:::

::: {.proof}
Suppose $v = mw$ with $w\in\ten$ and $m>1$. Since $v\in T_\Co = \delta^{\perp\ten}$, $0 = v\cdot\delta = m\,(w\cdot\delta)$, hence $w\cdot\delta = 0$ and $w\in\delta^{\perp\ten} = T_\Co$. So $v$ is not primitive in $T_\Co$.
:::

Consequently a primitive isotropic line or plane of $T_\Co$ is a primitive isotropic line or plane of $\ten$. This, and $R\leq\gent$, is what makes the forgetful map on cusps below well defined; a $\gent$-orbit of lines or planes of $\ten$ need not however preserve $\delta^{\perp}=T_\Co$, and none of the arguments below uses such a statement.

## The correspondence

::: {.theorem #thm:b2-zero-cusps title="B2 for $0$-cusps: the $0$-cusps of $D(T_\Co)/R$ are the $\gent$-orbits of pairs $(\ell,\alpha)$"}
Let $\mathcal P_0$ be the set of pairs $(\ell,\alpha)$ in which $\ell\subset\ten$ is a primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) line and $\alpha\in\ten$ is a $(-2)$-vector with $\alpha\perp\ell$, and let $\gent$ act on $\mathcal P_0$ by $g(\ell,\alpha) = (g\ell,g\alpha)$. Then:

1. The forgetful map $\ell\mapsto\ell$ induces a well defined map of cusp sets
$$
\Phi_0\colon\{0\text{-cusps of }D(T_\Co)/R\}\longrightarrow\{0\text{-cusps of }F_{\En,2}\},
$$
sending the $R$-orbit of a primitive isotropic line $\ell\subset T_\Co$ to the $\gent$-orbit of $\ell$.
2. For Sterk's representative $e_k$ of the $k$-th $0$-cusp, the fibre $\Phi_0^{-1}([e_k])$ is canonically in bijection with the set of $\Stab_{\gent}(e_k)$-orbits of $(-2)$-vectors $\alpha\in\ten$ perpendicular to $e_k$.
3. Consequently there is a bijection
$$
\{0\text{-cusps of }D(T_\Co)/R\}\ \longleftrightarrow\ \gent\backslash\mathcal P_0,
$$
and, choosing one representative $e_k$ per Sterk cusp, a bijection onto the disjoint union
$$
\coprod_{k=1}^{5}\ \Stab_{\gent}(e_k)\backslash\{\alpha\in\ten : \alpha^2 = -2,\ \alpha\perp e_k\}.
$$
:::

::: {.proof}
$(1)$ A primitive isotropic line of $T_\Co$ is a primitive isotropic line of $\ten$ (@lem:primitivity-tco-in-ten), and $R\leq\gent$, so the $\gent$-orbit of $\ell$ depends only on the $R$-orbit of $\ell$.

$(2)$ Let $\mathcal Y_k$ be the set of primitive isotropic lines $\ell\subset T_\Co$ with $[\ell]_{\gent} = [e_k]_{\gent}$, so that the fibre is the set $R\backslash\mathcal Y_k$ of $R$-orbits; and let $\tilde Y_k = \{\gamma\in\gent : \gamma e_k\perp\delta\}$, so that $\gamma\mapsto\gamma e_k$ is a surjection $\tilde Y_k\to\mathcal Y_k$ whose fibres are the cosets of $\Stab_{\gent}(e_k)$. Define
$$
\Psi_k\colon\tilde Y_k\longrightarrow L_k\definedas\{\alpha\in\ten : \alpha^2 = -2,\ \alpha\perp e_k\},\qquad \gamma\longmapsto \gamma^{-1}\delta .
$$
The target (@def:globular-boundary) is right: $(\gamma^{-1}\delta)\cdot e_k = \delta\cdot(\gamma e_k) = 0$ because $\gamma e_k\in T_\Co = \delta^{\perp}$, and $\delta^2 = -2$. The map is invariant under left multiplication by $R = \Stab_{\gent}(\delta)$, because $(r\gamma)^{-1}\delta = \gamma^{-1}r^{-1}\delta = \gamma^{-1}\delta$; and it is equivariant for right multiplication by $s\in\Stab_{\gent}(e_k)$, with $s e_k = \pm e_k$, acting on $L_k$ by $\alpha\mapsto s^{-1}\alpha$, which preserves $L_k$ because $(s^{-1}\alpha)\cdot e_k = \alpha\cdot(s e_k) = \pm\alpha\cdot e_k = 0$. It is surjective: for $\alpha\in L_k$, transitivity of $\gent$ on the $(-2)$-vectors of $\ten$ [@Ste91, 2.10] gives $\gamma\in\gent$ with $\gamma\alpha = \delta$, and then $\gamma e_k\perp\delta$ and $\Psi_k(\gamma) = \gamma^{-1}\delta = \alpha$. It is injective (@def:injective-map) on $R$-orbits: if $\gamma^{-1}\delta = \gamma'^{-1}\delta$ then $\gamma'\gamma^{-1}\delta = \delta$, so $\gamma'\gamma^{-1}\in R$ and $\gamma'$ lies in the $R$-orbit of $\gamma$. Hence $\Psi_k$ induces a bijection
$$
R\backslash\tilde Y_k/\Stab_{\gent}(e_k)\ \cong\ \Stab_{\gent}(e_k)\backslash L_k,
$$
and the left-hand side is $R\backslash\mathcal Y_k$, the fibre.

$(3)$ The $0$-cusps of $F_{\En,2}$ are the $\gent$-orbits of primitive isotropic lines, and Sterk's five representatives exhaust them [@Ste91, (4.2.3)], so the cusp set of $F_{\En,2}$ is the disjoint union of the five orbits (@def:group-orbit) and (2) applies over each. For the second bijection, send the $R$-orbit of $\ell$ to the $\gent$-orbit of $(\ell,\delta)$, and the $\gent$-orbit of $(\ell,\alpha)$ to the $R$-orbit of $\gamma\ell$, where $\gamma\in\gent$ is any element with $\gamma\alpha = \delta$; that $\gamma\ell\subset T_\Co$ and that its $R$-orbit does not depend on $\gamma$ are the computations of (2), and the two assignments are inverse by construction.
:::

::: {.theorem #thm:b2-one-cusps title="B2 for $1$-cusps"}
The same statement with "line" replaced by "plane": the $1$-cusps of $D(T_\Co)/R$ are the $\gent$-orbits of pairs $(\Pi,\alpha)$ in which $\Pi\subset\ten$ is a primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) plane and $\alpha\in\ten$ is a $(-2)$-vector with $\alpha\perp\Pi$; the fibre over Sterk's $1$-cusp $[\Pi]$ is the set of $\Stab_{\gent}(\Pi)$-orbits of $(-2)$-vectors $\alpha\perp\Pi$, the stabilizer (@def:group-orbit) being taken in the plane $[\Pi]$.

For such a $\Pi$ the quotient $\Pi^{\perp\ten}/\Pi$ is negative definite (@def:definiteness), so there are finitely many $(-2)$-classes in $\Pi^{\perp\ten}/\Pi$; that the fibre itself is finite is @lem:one-cusp-fibre-finite.
:::

::: {.proof}
Every step of the proof of @thm:b2-zero-cusps uses only that $\ell$ is a primitive isotropic subspace (@def:isotropic-subspace) of $\ten$ and that a primitive isotropic subspace of $T_\Co$ is one of $\ten$ (@lem:primitivity-tco-in-ten), so it applies verbatim to primitive isotropic planes. The identification of the $1$-cusps of $F_{\En,2}$ with the $\gent$-orbits of primitive isotropic planes is [@AEGS25, Def. 2.9]; Sterk's nine $1$-cusps are [@Ste91, §4.3]. The quotient $\Pi^{\perp}/\Pi$ has signature (@def:signature) $(0,8)$, because $\Pi$ is a maximal isotropic plane in a lattice of signature $(2,10)$, so a negative definite integral lattice has finitely many vectors of a given norm (@def:lattice-basic-invariants) --- finitely many $(-2)$-classes, but not yet finitely many orbits (@def:group-orbit) on their lifts; the lifts are controlled by @lem:one-cusp-fibre-finite below.
:::

::: {.lemma #lem:one-cusp-fibre-finite title="The fibre over a $1$-cusp is finite"}
Let $\Pi\subset\ten$ be a primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) plane with a basis (@def:based-module) $u,v$ of isotropic vectors (@def:isotropic-subspace), and let $\alpha\in\ten$ have $\alpha^2 = -2$ and $\alpha\perp\Pi$. For $z\in u^{\perp\ten}$ the Eichler transvection
$$
E_{u,z}(x) \definedas x+(x,u)z-(x,z)u-\tfrac{z^2}{2}(x,u)u
$$
lies in $\gent$, fixes $\Pi$ setwise, and acts on $\Pi^{\perp\ten}$ by $x\mapsto x-(x,z)u$. The set of values $(\alpha,z)$, $z\in u^{\perp\ten}$, is an ideal $d_u\ZZ$ with $d_u\mid 2$, so the $\Stab_{\gent}(\Pi)$-orbit of $\alpha$ contains $\alpha+2u$; symmetrically it contains $\alpha+2v$. Hence that orbit (@def:group-orbit) contains $\alpha+2\Pi$ and $\Stab_{\gent}(\Pi)$ has at most four orbits on the lifts $\alpha+\Pi$, so the fibre over any $1$-cusp is finite.
:::

::: {.proof}
*Integrality and membership in $\gent$.* The vector $E_{u,z}(x)-x = (x,u)z-(x,z)u-\tfrac{z^2}{2}(x,u)u$ lies in $\ten$ for $x\in\ten$ because all three coefficients are integers, and $E_{u,z}(y)-y\in\ten$ for $y\in\ten^\vee$ for the same reason with $(y,u),(y,z)\in\ZZ$; so $E_{u,z}$ acts trivially on $A_{\ten}$ and lies in $\ker\rho_{\ten}\subseteq\gent$. The transformation is the Eichler transvection of [@GHS08, §3.1, Lemma 3.1 and the integrality assertion after (10)], of which the $E$ of @lem:ze-translates-in-gent is the case $u = e'$, $z = e$; the computation is `computations/reports/coble_789-one-cusp-finiteness.py`.

*It preserves $\Pi$.* $E_{u,z}(u) = u+(u,u)z-(u,z)u-\tfrac{z^2}{2}(u,u)u = u$ because $u^2 = 0$ and $z\cdot u = 0$, and $E_{u,z}(v) = v-(v,z)u\in\Pi$.

*It translates.* For $x\in\Pi^{\perp}$ one has $(x,u) = 0$, so $E_{u,z}(x) = x-(x,z)u$.

*The ideal.* Since $\alpha,z\in\ten$ the value $(\alpha,z)$ is an integer; the set of them is a subgroup of $\ZZ$, say $d_u\ZZ$. Because $\alpha\in\Pi^{\perp}\subset u^{\perp}$ one has $(\alpha,\alpha) = -2\in d_u\ZZ$, so $d_u\mid 2$. Hence $2u\in d_u\ZZ\cdot u$ and the orbit contains $\alpha+2u$; the same argument with $v$ in place of $u$ gives $\alpha+2v$.

*Finiteness.* The orbit of $\alpha$ therefore contains $\alpha+2\Pi$, so the orbits on the lifts of a $(-2)$-class are a quotient of $\Pi/2\Pi\cong(\ZZ/2)^2$ and number at most four. The $(-2)$-classes of $\Pi^{\perp}/\Pi$ are finite because that lattice is negative definite (@def:definiteness). So the fibre is finite.
:::

::: {.lemma #lem:one-cusp-over-cusp-one-empty title="The four $1$-cusps over Sterk's cusp $1$ have empty fibre"}
Let $[\Pi]$ be one of the four $1$-cusps of $F_{\En,2}$ whose closure contains Sterk's $0$-cusp $1$. Then $\Pi^{\perp\ten}/\Pi\cong E_8(2)$, every vector of which has square divisible by $4$; hence no $(-2)$-vector of $\ten$ is perpendicular to $\Pi$, and the fibre of the $1$-cusp map of @thm:b2-one-cusps over $[\Pi]$ is empty.
:::

::: {.proof}
In the marked form this is @thm:coble-cusp-admissibility(3), whose four $1$-cusps carrying no marking are exactly these; the unmarked statement below is what the $1$-cusp map of @thm:b2-one-cusps needs. Sterk computes the four one-dimensional boundary components (@def:coble-surface) whose closure contains the $0$-cusp $e$ [@Ste91, 4.3.5]: "These four classes are not distinguished by the isomorphism (@def:isomorphism-of-objects) type of $F^{\perp}/F$ ... In all cases we even (@def:form-axioms) find the same isomorphism type, namely $E_8(-2)$" [@Ste91, 4.3.5], and the four types are listed in [@Ste91, 4.3.16]. In the notation of this page $E_8(-2)$ is $E_8(2)$. Its Gram matrix is $-2C(E_8)$, with diagonal (@def:polarization-functors) entries $-4$ and off-diagonal entries $0$ or $2$, so for $x = \sum x_i\alpha_i$ one has $x^2 = -4\sum x_i^2+4\sum_{i<j,\ \alpha_i\cdot\alpha_j = 2}x_ix_j$, a multiple of $4$; in particular $-2$ does not occur. Since $\Pi$ is isotropic (@def:orthogonal-complement), the class of a vector $\alpha\perp\Pi$ in $\Pi^{\perp}/\Pi$ has square $\alpha^2$, so an $\alpha$ with $\alpha^2 = -2$ cannot exist. The fibre, which is the set of $\Stab_{\gent}(\Pi)$-orbits of such $\alpha$ (@thm:b2-one-cusps), is therefore empty. The case $\Pi = \langle e,e'\rangle$ of the type $\{1,2\}$ is checked directly in `computations/reports/coble_789-one-cusp-empty.py`: $\Pi^{\perp\ten} = \langle e,e'\rangle\oplus E_8(2)$.
:::

::: {.lemma #lem:minus-id-in-gent title="$-\id_{T_\En}$ lies in $\gent$ and identifies a lift with its negative"}
The isometry $-\id_{T_\En}$ lies in $\gent$; it fixes every primitive isotropic subspace of $\ten$ and sends $\alpha$ to $-\alpha$. Hence, for a primitive isotropic plane $\Pi$, the lifts of the class $r\in\Pi^{\perp\ten}/\Pi$ and of the class $-r$ lie in one $\Stab_{\gent}(\Pi)$-orbit, and the fibre of @thm:b2-one-cusps over $[\Pi]$ is a set of orbits on the antipodal pairs $\{\pm\bar\alpha\}$, of which there are at most eight.
:::

::: {.proof}
$\gent$ is the set of $g\in\Orth(\ten)$ whose induced map on $A_{\ten}$ preserves the decomposition $A_{U(2)}\oplus A_{E_8(2)}$ [@AEGS25, Def. 2.6; @Ste91, Prop. 2.7]. The group $A_{\ten}$ is $2$-torsion, so $-\id$ acts trivially on it, hence preserves the decomposition; so $-\id\in\gent$. It is scalar, so it fixes every subspace of $\ten$, in particular $\Pi$; and it sends a vector to its negative. So a lift of $r$ and a lift of $-r$ differ by an element of $\Stab_{\gent}(\Pi)$, and the map from the fibre to the set of pairs $\{\bar\alpha,-\bar\alpha\}$ is well defined. Since $\Pi$ is primitive, $\Pi^{\perp}/\Pi$ is torsion free, so $r\neq -r$ for a class with $r^2 = -2$; the pairs are two-element sets, and there are at most eight of them.
:::

::: {.lemma #lem:k-pi-orthogonal-lines title="The sixteen classes of $K_\Pi$ are eight orthogonal lines, and $\Orth(K_\Pi)$ permutes them transitively"}
Let $\Pi$ be a primitive isotropic plane of $\ten$ of one of the five types with nonempty fibre. Then the sixteen vectors of square $-2$ in $K_\Pi = \Pi^{\perp\ten}/\Pi$ are eight antipodal pairs whose representatives $l_1,\dots,l_8$ are pairwise orthogonal, they span a sublattice $\generators{-2}^{\oplus8}$ of index $2$, and
$$
K_\Pi = \generators{l_1,\dots,l_8} + \ZZ\cdot\tfrac12(l_1+\cdots+l_8).
$$
Consequently the image of $\Orth(K_\Pi)$ in the signed permutations of the eight lines is all of $\{\pm1\}^8\rtimes\mathfrak{S}_8$, so it permutes the eight pairs as the full symmetric group and is transitive on them.
:::

::: {.proof}
The computation is `computations/reports/coble_789-kpi-gluing.py`, whose transcript is printed beside it. For each of the five planes it reuses the exact quotient of @lem:five-one-cusps-nonempty (unimodular complement, exact Gram matrix $G_0$ with $\det G_0 = 64$, exhaustive enumeration of the sixteen vectors of square $-2$ by rational $LDL^{\mathsf T}$ pruning), checks that the eight representatives are pairwise orthogonal and have determinant $2$, so that they span a sublattice $A$ of index $2$ with $A\cong\generators{-2}^{\oplus8}$. A vector $w\in K_\Pi$ outside $A$ has half-integral coordinates in the basis $l_j$, by the index; the run computes them and finds all eight half-integral in every one of the five cases, so the gluing class in $A^{*}/A\cong(\ZZ/2)^8$ is the all-ones vector, which is the displayed identity.

For the last sentence: an isometry of $K_\Pi$ permutes its sixteen vectors of square $-2$, hence preserves $A$ and induces a signed permutation $l_i\mapsto\varepsilon_i l_{\sigma(i)}$ of the eight lines. Every signed permutation preserves the overlattice: writing $v = \tfrac12(l_1+\cdots+l_8)$ for the gluing vector, one has
$$
g(v)-v = \tfrac12\textstyle\sum_{i}(\varepsilon_i-1)\,l_{\sigma(i)} = -\sum_{i:\varepsilon_i=-1} l_{\sigma(i)}\in A,
$$
because $(\varepsilon_i-1)/2$ is $0$ or $-1$. So $g(v)\in K_\Pi$ for every sign pattern and every permutation, the image of $\Orth(K_\Pi)$ in the signed permutations is all of $\{\pm1\}^8\rtimes\mathfrak{S}_8$, and its image in $\mathfrak{S}_8$ is onto.
:::

::: {.lemma #lem:reflections-fix-the-pairs title="Reflections act trivially on the eight pairs"}
Let $\Pi$ be a primitive isotropic plane and $\alpha\in\Pi^{\perp\ten}$ a $(-2)$-vector. Then the reflection $s_\alpha$ permutes the sixteen vectors of square $-2$ of $K_\Pi$, and it fixes each of the eight antipodal pairs. Consequently no product of reflections in $(-2)$-vectors perpendicular to $\Pi$ moves a pair, and the orbits of $\Stab_{\gent}(\Pi)$ on the eight pairs are the orbits of its image modulo the reflection subgroup.
:::

::: {.proof}
$s_\alpha$ fixes $\alpha^{\perp}$ pointwise and sends $\alpha$ to $-\alpha$; it preserves $\Pi$ because $\alpha\perp\Pi$. On $K_\Pi$ it therefore fixes the class of $\alpha$ up to sign and fixes every class orthogonal to $\alpha$. By @lem:k-pi-orthogonal-lines the sixteen vectors of square $-2$ are eight antipodal pairs with pairwise orthogonal representatives $l_1,\dots,l_8$, so $s_\alpha$, for $\alpha$ in the line $\ZZ l_i$, fixes $l_j$ for $j\neq i$ and sends $l_i$ to $-l_i$: it fixes all eight pairs. A product of such reflections fixes all eight pairs as well.
:::

::: {.lemma #lem:divisibility-decides-one-cusp title="Divisibility of a $(-2)$-class in $\Pi^{\perp\ten}/\Pi$ decides its lifts"}
Let $\Pi\subset\ten$ be a primitive isotropic plane, $L_0 \definedas \Pi^{\perp\ten}/\Pi$, let $r\in L_0$ have $r^2 = -2$, and let $\alpha\in\Pi^{\perp\ten}$ be a lift of $r$ with $\alpha^2 = -2$. For $w\in\Pi$ put $d_w\ZZ \definedas \{(\alpha,z) : z\in w^{\perp\ten}\}$. Then:

1. $d_w$ divides $\mathrm{div}_{L_0}(r) \definedas \gcd\{(\alpha,z) : z\in\Pi^{\perp\ten}\}$;
2. if $\mathrm{div}_{L_0}(r) = 1$ then $\Stab_{\gent}(\Pi)$ is transitive on the lifts of $r$, so the lift contributes exactly one point to the fibre of @thm:b2-one-cusps over $[\Pi]$.
:::

::: {.proof}
$1$. Since $\Pi\subset\Pi^{\perp}$ one has $\Pi^{\perp}\subset w^{\perp}$, so the set of values over $w^{\perp}$ contains the set over $\Pi^{\perp}$ and its gcd divides that one. The values over $\Pi^{\perp}$ depend only on the class, because $(\alpha,p) = 0$ for $p\in\Pi$ as $\alpha\perp\Pi$; their gcd is $\mathrm{div}_{L_0}(r)$.

$2$. By $1$ and the hypothesis $d_w = 1$ for every $w\in\Pi$, so for each such $w$ there is $z\in w^{\perp}$ with $(\alpha,z) = 1$; the transvection $E_{w,z}$ of @lem:one-cusp-fibre-finite lies in $\gent$, preserves $\Pi$ setwise and sends $\alpha$ to $\alpha-w$. Every vector of $\Pi$ is isotropic, so taking $w$ to run over a basis $u,v$ of $\Pi$ shows that $\alpha-u$ and $\alpha-v$ lie in the orbit (@def:group-orbit), hence $\alpha-p$ lies in the orbit for every $p\in\Pi$. Any other lift of $r$ is $\alpha-p$ for some $p\in\Pi$. Hence one orbit.
:::

::: {.theorem #lem:five-one-cusps-nonempty title="The five remaining $1$-cusps: nonempty fibres, at most eight points each, seven in all"}
Let $[\Pi]$ be one of Sterk's five further $1$-cusps, of types $\{2,4,5\}$, $\{4,5\}$, $\{3,5\}$, $\{3,4\}$ and $\{5,5\}$ [@Ste91, 4.3.17]. Then:

1. $\Pi$ is primitive in $\ten$, and for a choice of a complementary basis the Gram matrix $G_0$ of $L_0 = \Pi^{\perp\ten}/\Pi$ is exact: its determinant is $64$, and $L_0$ has exactly $16$ vectors of square $-2$;
2. every one of those $16$ classes has $\mathrm{div}_{L_0}$ equal to $1$, certified by an explicit $z\in\Pi^{\perp}$ with $(\alpha,z) = 1$; this is the count of $16$ classes of square $-2$ that @thm:coble-cusp-admissibility(3) records at each of the five types, and it is a statement about $K_\Pi$, not about the number of $1$-cusps of $D(T_\Co)/R$;
3. hence, by @lem:divisibility-decides-one-cusp, all lifts of any one class form a single $\Stab_{\gent}(\Pi)$-orbit, so the fibre of @thm:b2-one-cusps over $[\Pi]$ is the set of orbits on the eight antipodal pairs (@lem:minus-id-in-gent) and has at most $8$ points;
4. the total number of $1$-cusps of $D(T_\Co)/R$ over the five types is $7$, not the number of pairs: the $R$-orbits on the primitive isotropic planes of $T_\Co$ number $7$ (@cor:coble-heegner-integral-plane-descent, which applies to $R$ because $\ker\bar\rho\subseteq R$; @thm:cusp-lifting(4)). So the five fibres are nonempty sets of at most $8$ points with total $7$, that is either $(3,1,1,1,1)$ or $(2,2,1,1,1)$ in some order.
:::

::: {.proof}
$1$ and $2$ are `computations/reports/coble_789-one-cusp-divisibility.py`, whose transcript is printed beside it: for each of the five planes the run checks that $\{u,v\}$ has Smith form $[1,1]$, so $\Pi$ is primitive in $\ten$; takes a basis $K$ of the kernel of the two functionals $(\cdot,u),(\cdot,v)$, which is $\Pi^{\perp}$; expresses $u,v$ in that basis with integer coordinates $C$; exhibits a complement $R_0$ with $\det(C;R_0) = \pm1$, the certificate that $R_0$ together with $u,v$ is a basis of $\Pi^{\perp}$, so that $G_0 = R_0\,G_{\Pi^{\perp}}\,R_0^{\mathsf T}$ is the Gram matrix of $L_0$ and not of a finite-index sublattice; finds the sixteen vectors of square $-2$ by an exact rational $LDL^{\mathsf T}$ pruning, with no short-vector library call; and lifts each to an integral $\alpha$ with $\alpha\perp\Pi$, $\alpha^2 = -2$, solving $(\alpha,z) = 1$ by extended gcd.

$3$ is @lem:divisibility-decides-one-cusp(2), which gives one orbit per class, together with @lem:minus-id-in-gent, which identifies the classes $r$ and $-r$; the sixteen classes therefore fall into at most eight orbits, one for each antipodal pair.

$4$ is @cor:coble-heegner-integral-plane-descent as used at the count of primitive isotropic plane orbits of $R$; the five types are those with nonempty fibre by $1$--$3$ and @lem:one-cusp-over-cusp-one-empty, and they partition the seven. $5$: a computation of the orbits on the pairs would be a computation of the image of $\Stab_{\gent}(\Pi)$ in $\Orth(L_0)$, which neither the present record nor any other on the page performs.
:::

::: {.remark #rmk:five-one-cusps-which-split title="Which split of the seven $1$-cusps holds"}

In @lem:five-one-cusps-nonempty(4), which of the two holds is decided by @thm:one-cusp-multiplicities(5): the double fibre is over $\{3,5\}$, the multiplicities being $1,1,2,1,2$ on $(\{2,4,5\},\{4,5\},\{3,5\},\{3,4\},\{5,5\})$, read off the seven plane orbits of `computations/reports/coble_gco_plane-orbits-run.txt` through the label dictionary of @thm:orbit-per-cusp.
:::

## The fibre over Sterk's cusp $2$: the smallest case

At Sterk's cusp $2$ the stabilizer is the whole orthogonal group of the cusp lattice, so the fibre is decided without any information about the other cusps. Cusp $1$ is the other extreme: it carries no $(-2)$-vector at all.

::: {.proposition #prop:fibre-cusp-one-empty title="The fibre over Sterk's cusp $1$ is empty"}
At Sterk's cusp $1$, with representative $\eta_1 = e$, one has $K_{\eta_1} = e^{\perp\ten}/\ZZ e\cong U(2)\oplus E_8(2)$, every vector of which has square divisible by $4$. In particular $K_{\eta_1}$ contains no $(-2)$-vector, and the fibre of $\Phi_0$ over Sterk's cusp $1$ is empty.
:::

::: {.proof}
$e^{\perp\ten} = \generators{e}\oplus U(2)\oplus E_8(2)$, so $K_{\eta_1}\cong U(2)\oplus E_8(2)$; this is [@Ste91, 4.3.4], whose statement is $e^{\perp}/\ZZ e\cong\mathbf H(2)\oplus E_8(-2)$. Both summands are twice an even lattice (@def:even-lattice), so every square in $K_1$ lies in $4\ZZ$, and $-2\notin4\ZZ$.
:::

::: {.theorem #thm:ou-e8-transitive title="$\Orth(U\oplus E_8(2))$ is transitive on the $(-2)$-vectors"}
Let $K_{\eta_2} = U\oplus E_8(2)$ be the boundary lattice of Sterk's cusp $2$ (@prop:sterk-cusp-quotients). Then $\Orth(K_{\eta_2})$ acts transitively on $\{x\in K_{\eta_2} : x^2 = -2\}$.
:::

::: {.proof}
By [@Ste91, 4.3.6], $K_{\eta_2} = (e')^{\perp\ten}/\ZZ e'$ is the boundary lattice of Sterk's cusp $2$, and $\Orth(K_{\eta_2}) = \{\pm1\}\cdot W_{e'}$, where $W_{e'}$ is the subgroup generated by the reflections of $\Orth(K)$.

*A fundamental chamber (@def:coble-polarization-classes) of $W_{e'}$.* Take the chamber certified by the complete Vinberg search of `computations/reports/coble_TEn-chambers-run.txt`, section `K(L_2)`, which lists in the basis (@def:based-module) $e,f,\alpha_1,\dots,\alpha_8$ of $K$ the ten walls (@not:coxeter-polytope-faces)
$$
\alpha_1,\dots,\alpha_8,\qquad -e+f,\qquad \bar\alpha_8-2f,
$$
where $\bar\alpha_8 \definedas -(2\alpha_1+3\alpha_2+4\alpha_3+6\alpha_4+5\alpha_5+4\alpha_6+3\alpha_7+2\alpha_8)$ is Sterk's doubled fundamental weight (@def:coroot-weight), of square $-4$ and with $\bar\alpha_8\cdot\alpha_8 = 2$; there the wall Gram matrix has diagonal (@def:polarization-functors) $(-4,\dots,-4,-2,-4)$ and off-diagonal entries $0$ and $2$, so the dihedral angles are $\pi/2$, $\pi/3$ or $\pi/4$, all submultiples of $\pi$. That the search is complete --- that these ten walls bound a chamber and not a proper sub-polytope --- is the line `unrestricted certified search on this cusp: complete=True walls=10 ideal=2 finite=8` of `computations/reports/coble_sterk-reflection-subgroups-run.txt`. Sterk's printed ten roots at cusp $2$ are the same list except for the tenth wall, which he prints as $\alpha_9 = \bar\alpha_8+2f = -\omega_8+2f$ [@Ste91, 4.3.6], $\bar\alpha_8$ being the doubled fundamental weight $2\omega_8$: the record's `his walls among the walls of the certified chamber: 9 of 10 (his walls not among them: labels [9])` compares wall vectors, and $-\omega_8+2f$ and $-2f-\omega_8$ differ by $4f$. The argument below uses the certified chamber, and does not rely on the printed one.

By Vinberg's theorem [@Vin85, §1, no. 1], a Coxeter polytope (@def:coxeter-polytope) $P$ is a fundamental polytope for the group (@def:group) generated by the reflections in its walls, the polytopes $\gamma P$, $\gamma\in W_{e'}$, tessellate the hyperbolic (@def:definiteness) space $\mathbf H$ attached to $K$, and every mirror (@not:hyperbolic-polytope-setting) of a reflection of $W_{e'}$ is a wall of that tessellation.

*Every $(-2)$-vector is a wall translate.* Let $x\in K$ with $x^2 = -2$ and let $s_x$ be the reflection in $x$. Since $s_x\in\Orth(K) = \{\pm1\}W_{e'}$ and $\pm1$ acts trivially on $\mathbf H$, the isometry of $\mathbf H$ induced by $s_x$ lies in the image of $W_{e'}$; it is the reflection of $\mathbf H$ with fixed hyperplane $x^{\perp}\cap\mathbf H$. By Vinberg's theorem that hyperplane is a wall of the tessellation, so $x^{\perp} = w(r_i^{\perp})$ for some $w\in W_{e'}$ and some $i\in\{1,\dots,10\}$, that is $x = \pm w(r_i)$, $r_i$ being the $i$-th wall root. Of the ten wall roots only $-e+f$ has square $-2$; the other nine have square $-4$. Hence every $(-2)$-vector of $K$ lies in the $W_{e'}$-orbit of $\pm(e-f)$, and $\Orth(K)$ is transitive.
:::

::: {.proposition #prop:isometry-k-roots title="An explicit isometry of $U\oplus E_8(2)$ sending $e-f$ to $e+f+\alpha_1$"}
In the basis (@def:based-module) $e,f,\alpha_1,\dots,\alpha_8$ of $K=U\oplus E_8(2)$ with Gram matrix $G = \begin{pmatrix}0&1\\1&0\end{pmatrix}\oplus(-2)C(E_8)$ the matrix
$$
N = \begin{pmatrix}
2&1&-4&0&2&0&0&0&0&0\\
1&0&0&0&0&0&0&0&0&0\\
1&0&-1&0&0&0&0&0&0&0\\
0&0&0&-1&0&0&0&0&0&0\\
0&0&0&0&-1&0&0&0&0&0\\
0&0&0&0&0&-1&0&0&0&0\\
0&0&0&0&0&0&-1&0&0&0\\
0&0&0&0&0&0&0&-1&0&0\\
0&0&0&0&0&0&0&0&-1&0\\
0&0&0&0&0&0&0&0&0&-1
\end{pmatrix}
$$
satisfies $N^{\mathsf T}GN = G$, $\det N = -1$ and $N(e-f) = e+f+\alpha_1$. Hence $e-f$ and $e+f+\alpha_1$ lie in one $\Orth(K)$-orbit, and the two orbits (@def:group-orbit) of @thm:ou-e8-transitive cannot be separated by the invariants that separate these two vectors.
:::

::: {.proof}
The products $N^{\mathsf T}GN$ and $N(e-f)$ are computed in exact (@def:exact-complex) integer arithmetic in `computations/reports/coble_789-transvection-and-isometry.py`, whose transcript `-run.txt` prints `N^T G_K N = G_K: True`, `det N = -1` and `N(e-f) = e+f+a_1: True`. The computation serves @thm:ou-e8-transitive as a certificate for this one pair, not as its proof; the proof of transitivity is the chamber (@def:coble-polarization-classes) argument there.
:::

::: {.lemma #lem:ze-translates-in-gent title="The $\ZZ e'$-translates of $\delta$ are realised by $\gent$"}
Let $E\colon\ten\to\ten$ be the Eichler transvection
$$
E(x) \definedas x+(x,e')\,e-(x,e)\,e' .
$$
Then $E\in\gent$, $E(e') = e'$, $E(\delta) = \delta+e'$ and $E^k(\delta) = \delta+k e'$ for every $k\in\ZZ$.
:::

::: {.proof}
*Integrality.* On the basis (@def:based-module) $e,f,e',f',\alpha_1,\dots,\alpha_8$ of $\ten$ one has $E(e) = e$, $E(f) = f-e'$, $E(e') = e'$, $E(f') = f'+2e$ and $E(\alpha_i) = \alpha_i$, all integral. This is the case $\eta = e'$, $a = e$ of the Eichler transformation of [@GHS08, §3.1, Lemma 3.1 and the integrality assertion after (10)], as quoted in @lem:cusp-root-lift-independence; the computation is `computations/reports/coble_789-transvection-and-isometry.py`.

*Isometry.* Expanding $(E x,E y)$ for $x,y\in\ten$ with $e^2 = (e')^2 = e\cdot e' = 0$ (the sum $U\oplus U(2)\oplus E_8(2)$ is orthogonal, so $e$ and $e'$ are perpendicular), the correction terms cancel in pairs: $(Ex,Ey)-(x,y) = (x,e)(y,e')-(y,e)(x,e')+(x,e')(e,y)-(x,e)(e',y)$, and this vanishes because $(e,y) = (y,e)$ and $(e',y) = (y,e')$.

*The translates.* $(\delta,e') = 0$ and $(\delta,e) = -1$, so $E(\delta) = \delta+e'$; $E$ is linear and fixes $e'$, so $E^k(\delta) = \delta+k e'$ for $k\geq 0$, and $E^{-1}$ gives the negative multiples.

*Membership in $\gent$.* For $y$ in the dual lattice $\ten^\vee = U\oplus\tfrac12U(2)\oplus\tfrac12E_8(2)$ one has $E(y)-y = (y,e')e-(y,e)e'$, and both pairings are integers: $(y,e')$ because the $U(2)$-component of $y$ is half-integral and pairs integrally with $e'$, and $(y,e)$ because the $U$-component is integral and the other summands are orthogonal to $e$. Hence $E(y)-y\in\ten$ and $E$ acts trivially on $A_{\ten} = \ten^\vee/\ten$. So $E\in\ker\rho_{\ten}\subseteq\gent$, the last inclusion because $\gent = \rho^{-1}(M)$ is the preimage of the summand-preserving subgroup of $\Orth(A_{\ten},q)$ [@AEGS25, Def. 2.6; @Ste91, Prop. 2.7].
:::

::: {.corollary #cor:fibre-cusp-two title="The fibre over Sterk's cusp $2$ is a single point"}
The fibre of $\Phi_0$ over Sterk's cusp $2$ is a single point, represented by the pair $(\ZZ e',\,\delta)$: by the $(-2)$-vector $\delta = e-f$ of $\ten$, and by the primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) line $\ZZ e'$ of $T_\Co$ that the pair carries. (The vector $\delta$ itself is not a vector of $T_\Co$: $\delta^2 = -2\neq0$.)
:::

::: {.proof}
By @thm:b2-zero-cusps(2) the fibre is the set of $\Stab_{\gent}(e')$-orbits of $(-2)$-vectors $\alpha\perp e'$. Let $\alpha$ be one, and let $\bar\alpha$ be its image in $K_{\eta_2} = (e')^{\perp\ten}/\ZZ e'$. The image of $\Stab_{\gent}(e')$ in $\Orth(K_{\eta_2})$ is all of $\Orth(K_{\eta_2})$ [@Ste91, 4.3.6], and $\Orth(K_{\eta_2})$ is transitive on the $(-2)$-vectors of $K_{\eta_2}$ (@thm:ou-e8-transitive), so some $g\in\Stab_{\gent}(e')$ has $g\bar\alpha = \bar\delta$, that is $g\alpha = \delta+k e'$ for some $k\in\ZZ$. By @lem:ze-translates-in-gent the transvection $E$ lies in $\Stab_{\gent}(e')$ and $E^{-k}(g\alpha) = \delta$. Hence every $(-2)$-vector perpendicular to $e'$ is $\Stab_{\gent}(e')$-equivalent to $\delta$, and the fibre is a single point.
:::

## The other fibres, and the four $0$-cusps

::: {.proposition #prop:fibres-three-four-five title="The fibres over Sterk's cusps $3$, $4$ and $5$ are nonempty"}
At Sterk's cusps $3$, $4$ and $5$ the boundary lattice $K_{\eta_k} = \eta_k^{\perp\ten}/\ZZ\eta_k$ of @prop:sterk-cusp-quotients is $K_{\eta_k}\cong U\oplus E_8(2)$ as well [@Ste91, 4.3.4], and each has a $(-2)$-vector perpendicular to its representative, as follows; the vectors are the white nodes of [@AEGS25, Figs.~7--8], and the coordinates are those of the record `computations/reports/coble_enriques-white-root-facets-run.txt` in the basis $(e,f,e',f',\alpha_1,\dots,\alpha_8)$ of $\ten$.
$$
\begin{array}{c|c|c}
\text{cusp} & \text{representative} & \text{a }(-2)\text{-vector perpendicular to it}\\ \hline
3 & e'+f'+y_3 & -(e-f),\quad e+f-f'+\alpha_8\\
4 & 2e'+f'+y_4 & -(e-f),\quad e+f-e'+\alpha_1\\
5 & 2e+2f+y_4 & -(e-f),\quad e+f+2e'+3f'-2\alpha_1+\alpha_3,\quad e+f+3e'+3f'-2\alpha_1+\alpha_2+2\alpha_3+2\alpha_4+\alpha_5,\quad e+f+3e'+4f'-2\alpha_1+2\alpha_2+3\alpha_3+4\alpha_4+3\alpha_5+2\alpha_6+\alpha_7
\end{array}
$$
Hence each of the three fibres is nonempty.
:::

::: {.proof}
At cusp $3$ the representative is $e'+f'+y_3$ and the record's cusp-$3$ section prints the two white roots as $\delta = [-1,1,0,\dots,0] = -(e-f)$ and $[1,1,0,-1,0,\dots,0,1] = e+f-f'+\alpha_8$, each certified to have square $-2$ and to be orthogonal to the representative. At cusp $4$ the representative is $2e'+f'+y_4$ and the record's cusp-$4$ section prints the white roots as $[1,1,-1,0,1,0,\dots,0] = e+f-e'+\alpha_1$ and $[-1,1,0,\dots,0] = -(e-f)$. At cusp $5$ the representative is $2e+2f+y_4$ and the record prints the four white roots $[1,1,2,3,-2,0,1,0,\dots,0]$, $[1,1,3,3,-2,1,2,2,1,0,0,0]$, $[-1,1,0,\dots,0]$ and $[1,1,3,4,-2,2,3,4,3,2,1,0]$, which are the displayed vectors. The identification of the white nodes of AEGS's Figures 7--8 with the simple $(-2)$-roots of Sterk's diagrams is @prop:facet-angles-aegs.
:::

::: {.theorem #thm:four-r-orbits title="$R$ has exactly four orbits on the primitive isotropic lines of $T_\Co$"}
The subgroup $R$ has exactly four orbits (@def:group-orbit) on the primitive isotropic lines of $T_\Co$, of discriminant-class sizes $2$, $135$, $270$ and $120$. Hence $D(T_\Co)/R$ has exactly four $0$-cusps.
:::

::: {.proof}
Every primitive vector of $T_\Co$ has divisibility $2$ (@lem:divisibilityAlwaysTwoTco), so $v\mapsto[v/2]$ maps the primitive isotropic vectors (@def:isotropic-subspace) of $T_\Co$ to the $527$ nonzero isotropic classes of $A_{T_\Co}$, and the map is a bijection from the $\ker\bar\rho$-orbits of primitive isotropic vectors onto those classes [@thm:coble-zero-cusp-count(1)]. For a subgroup $\Gamma$ with $\ker\bar\rho\subseteq\Gamma\subseteq\Orth(T_\Co)$ the $\Gamma$-orbits on primitive isotropic vectors correspond to the $\bar\rho(\Gamma)$-orbits on the classes, because the fibre over a class is a single $\ker\bar\rho$-orbit [@thm:coble-zero-cusp-count, proof, paragraph "Intermediate groups"]. Here $R = \bar\rho^{-1}(P)$ [@prop:gamma-co-images(3)], so $\bar\rho(R) = P$, and $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ has exactly four orbits on the $527$ nonzero isotropic classes, of sizes $2$, $135$, $270$ and $120$ [@prop:coble-cong-point-stabilizer(2)]. A count of $0$-cusps names its group [@def:gamma-co-groups], and this is the count for $R$.
:::

::: {.theorem #thm:orbit-per-cusp title="Which $R$-orbit lies over which Sterk cusp"}
Let $\eta_2 = e'$, $\eta_3 = e'+f'+y_3$, $\eta_4 = 2e'+f'+y_4$, $\eta_5 = 2h+y_4$ with $h = e+f$, $y_3$ of square $-4$ and $y_4$ of square $-8$ be Sterk's representatives of his cusps $2$, $3$, $4$, $5$ [@Ste91, (4.2.3)], and put $[\eta_k]\definedas[\eta_k/2]\in A_{T_\Co}$. Then $[\eta_k]$ lies in the $P$-orbit of @prop:coble-cong-point-stabilizer(2) of size
$$
\begin{array}{c|cccc}
k & 2 & 3 & 4 & 5\\ \hline
\text{size of the }P\text{-orbit of }[\eta_k] & 2 & 120 & 270 & 135
\end{array}
$$
Because $v\mapsto[v/2]$ is a bijection from the $R$-orbits on primitive isotropic lines of $T_\Co$ onto the $P$-orbits on the $527$ nonzero isotropic classes [@thm:coble-zero-cusp-count(1), with $\bar\rho(R) = P$ by @prop:gamma-co-images(3)], the $R$-orbit lying over Sterk's cusp $k$ is the orbit (@def:group-orbit) of $[\eta_k]$, and the four $R$-orbits of @thm:four-r-orbits are exactly the four cusps' orbits.
:::

::: {.proof}
Write $T_\Co = \generators{h}\oplus U(2)\oplus E_8(2)$ [@DK13, (3.6)], so that $A_{T_\Co} = A_{\generators{2}}\oplus A_{U(2)}\oplus A_{E_8(2)}$. For $k = 2,3,4,5$ the vector $\eta_k$ lies in $T_\Co$, is primitive and isotropic, and its half has the following components, with the $q$-value of each:
$$
\begin{array}{c|c|c|c|c}
k & \text{component in } U(2) & q & \text{component in } E_8(2) & q\\ \hline
2 & e'/2 & 0 & 0 & 0\\
3 & (e'+f')/2 & 1 & y_3/2 & -1\\
4 & e'+f'/2 & 2 & y_4/2 & -2\\
5 & 0 & 0 & y_4/2 & -2
\end{array}
$$
the last line because $\eta_5/2 = h+y_4/2$ and $h\in T_\Co$. Each total $q$ is $0$ modulo $2\ZZ$, as it must be for an isotropic vector (@def:isotropic-subspace). The three nonzero classes of $A_{U(2)}$ are $u_1,u_2,u_3$ with $q$-values $0,0,1$, and the $E_8(2)$-classes of value $0$ and $1$ are the sets $E_0$ of size $135$ and $E_1$ of size $120$ [@prop:coble-cong-point-stabilizer(2), proof]. So $[\eta_2] = (u_1\text{ or }u_2,\,0)$ lies in $\{u_1,u_2\}$ of size $2$; $[\eta_3] = (u_3,\,E_1)$ in the orbit of size $120$; $[\eta_4] = (u_1\text{ or }u_2,\,E_0)$ in the orbit of size $270$; and $[\eta_5] = (0,\,E_0)$ in the orbit of size $135$. The computation is `computations/reports/coble_789-cusp-classes.py`, whose transcript `-run.txt` prints, for each $k$, the components and the orbit.
:::

::: {.theorem #thm:cusp-fibres-four title="The $0$-cusps of $D(T_\Co)/R$ lie one over each of Sterk's cusps $2,3,4,5$"}
The map $\Phi_0$ of @thm:b2-zero-cusps has empty fibre over Sterk's cusp $1$ (@prop:fibre-cusp-one-empty) and exactly one point over each of Sterk's cusps $2$, $3$, $4$, $5$. Hence the four $0$-cusps of $D(T_\Co)/R$ are in bijection with Sterk's cusps $2,3,4,5$, one over each.
:::

::: {.proof}
The fibres of $\Phi_0$ partition the $0$-cusps of $D(T_\Co)/R$: $\Phi_0$ is well defined by @thm:b2-zero-cusps(1), and the cusp set of $F_{\En,2}$ is the disjoint union of the five orbits (@def:group-orbit) of Sterk's representatives. The fibre over cusp $1$ is empty (@prop:fibre-cusp-one-empty). For $k = 2,3,4,5$ the representative $\eta_k$ is a primitive isotropic vector (@def:isotropic-subspace) of $T_\Co$, so its $R$-orbit is a $0$-cusp of $D(T_\Co)/R$ lying over cusp $k$; by @thm:orbit-per-cusp the four classes $[\eta_k]$ lie in four distinct $P$-orbits, hence the four $R$-orbits are distinct, and by @thm:four-r-orbits there are exactly four of them. So each of the four fibres over $2,3,4,5$ contains exactly one of the four $R$-orbits.
:::

::: {.lemma #lem:cusp-incidence-rule title="Incidence of the cusps of $D(T_\Co)/R$"}
For $k\in\{2,3,4,5\}$ let $0_k$ be the $0$-cusp of $D(T_\Co)/R$ over Sterk's $0$-cusp $k$ (@thm:cusp-fibres-four). Then $0_k$ lies in the closure of a $1$-cusp of $D(T_\Co)/R$ over Sterk's $1$-cusp of type $T$ [@AEGS25, Not. 3.1] exactly when $k\in T$.
:::

::: {.proof}
*Necessity.* The Baily--Borel incidence is containment of boundary components: a $0$-cusp $[\ell]$ lies in the closure of a $1$-cusp $[\Pi]$ exactly when some representatives satisfy $\ell\subset\Pi$ [@AEGS25, Def. 2.9 and §3.1], and the type of $[\Pi]$ is by definition [@AEGS25, Not. 3.1] the set of labels of the $0$-cusps in its closure. If $[\ell]_R$ is incident to $[\Pi]_R$, the forgetful maps of @thm:b2-zero-cusps and @thm:b2-one-cusps carry the inclusion to $\ell\subset\Pi$ in $\ten$, so the label $k$ of $[\ell]_{\gent}$ lies in $T$. Since $0_k$ exists only for $k\neq1$, this excludes cusp $1$.

*Sufficiency.* Let $\Pi'$ be a primitive isotropic plane of $T_\Co$ representing a $1$-cusp of $D(T_\Co)/R$ over $T$, and let $k\in T$ with $k\neq1$. By [@AEGS25, Not. 3.1] the label $k$ is the label of some primitive isotropic line $\ell\subset\Pi$ of $\ten$; conjugating by an element of $\gent$ gives $\ell\subset\Pi'$, and $\ell\subset T_\Co$ because $\Pi'\subset T_\Co$. So the $R$-orbit of $\ell$ is a $0$-cusp of $D(T_\Co)/R$ over $k$, hence is $0_k$ by @thm:cusp-fibres-four, and it is incident to $[\Pi']_R$ because $\ell\subset\Pi'$.
:::

::: {.theorem #thm:one-cusp-multiplicities title="The number of $1$-cusps of $D(T_\Co)/R$ over each Sterk type"}
Let $m_T$ be the number of $1$-cusps of $D(T_\Co)/R$ lying over Sterk's $1$-cusp of type $T\subset\{1,2,3,4,5\}$ [@AEGS25, Not. 3.1]. Then

1. $m_T = 0$ for the four types containing $1$ (@lem:one-cusp-over-cusp-one-empty), and $m_T\geq1$ for the five others (@lem:five-one-cusps-nonempty(3));
2. $\sum_T m_T = 7$ and $\sum_T m_T\,\abs{T\cap\{2,3,4,5\}} = 13$;
3. consequently $m_{\{2,4,5\}} = 1$, $m_{\{5,5\}} = 2$, and exactly one of $m_{\{4,5\}}$, $m_{\{3,5\}}$, $m_{\{3,4\}}$ equals $2$ while the other two equal $1$. In particular every nonempty fibre is a set of one or two points;
4. the degrees of the four $0$-cusps are therefore $0_2$ of degree $1$ and
$$
(0_3,0_4,0_5) =
\begin{cases}
(3,4,5) & \text{if } m_{\{3,4\}} = 2,\\
(2,4,6) & \text{if } m_{\{4,5\}} = 2,\\
(3,3,6) & \text{if } m_{\{3,5\}} = 2,
\end{cases}
$$
with $13$ incidence edges in each case;
5. the third case occurs, by the computation of `computations/reports/coble_789-one-cusp-multiplicities.py` recorded at $5$ below: $m_{\{3,5\}} = 2$, $m_{\{3,4\}} = m_{\{4,5\}} = 1$. So the multiplicities are $(1,1,2,1,2)$ for the types $(\{2,4,5\},\{4,5\},\{3,5\},\{3,4\},\{5,5\})$, and the degrees of the four $0$-cusps are $1,3,3,6$ for $0_2,0_3,0_4,0_5$, with $13$ incidence edges.
:::

::: {.proof}
$1$ is @lem:one-cusp-over-cusp-one-empty and @lem:five-one-cusps-nonempty(3).

$2$. The left sum counts the $1$-cusps of $D(T_\Co)/R$, that is the $R$-orbits on the primitive isotropic planes of $T_\Co$, and these number $7$ [@thm:coble-integral-lifting-fibre(4)(b)]. The right sum counts the pairs (a $1$-cusp, a $0$-cusp of $D(T_\Co)/R$ in its closure), by the incidence of @lem:cusp-incidence-rule and [@AEGS25, Not. 3.1], which makes the $0$-cusps in the closure exactly the labels in $T$ intersected with $\{2,3,4,5\}$, since the $0$-cusps of $D(T_\Co)/R$ are $0_2$, $0_3$, $0_4$, $0_5$ (@thm:cusp-fibres-four) and there is none over $1$. Those pairs are the $R$-orbits of flags (a primitive isotropic line in a primitive isotropic plane) of $T_\Co$, and these number $13$: the flag orbits and the edges of $R_{\gent}$ are both $13$ [@thm:coble-integral-lifting-fibre(4)(b) and @prop:coble-flag-orbits-and-edges(3)].

$3$. Put $e_T \definedas m_T - 1\geq0$ on the five types with nonempty fibre; by $2$, $\sum e_T = 7-5 = 2$ and $\sum e_T\abs{T\cap\{2,3,4,5\}} = 13-10 = 3$. The five weights are $3,2,2,2,1$ for $T = \{2,4,5\},\{4,5\},\{3,5\},\{3,4\},\{5,5\}$. Two units of excess with total weight $3$ must sit one on a type of weight $2$ and one on the type of weight $1$: a single type carrying both units would contribute twice its weight, which is even and not $3$, and two units on two types of weight $2$ contribute $4$. So $e_{\{5,5\}} = 1$, $e_{\{2,4,5\}} = 0$, and exactly one of the three remaining $e$'s equals $1$. Since each $m_T$ is the cardinality of the fibre over $T$ (@thm:b2-one-cusps), each nonempty fibre has one or two points.

$4$ is the incidence rule of @lem:cusp-incidence-rule read with the multiplicities of $3$: the degree of $0_k$ is $\sum_{T\ni k}m_T$, and the three possibilities for the middle weights give the three triples displayed; the total is $\sum_T m_T\abs{T\cap\{2,3,4,5\}} = 13$ in each case by $2$.

$5$. The record `computations/reports/coble_gco_plane-orbits-run.txt` prints, for each of the seven $R$-orbits of primitive isotropic planes of $T_\Co$, the class data of @prop:coble-flag-orbits-and-edges: the $H$-orbits of the nonzero classes of $J(\Pi)$ under their discriminant-orbit sizes, $(2,135,270)$, $(135)$, $(120,135)$, $(135)$, $(120,135)$, $(120,270)$, $(135,270)$, and the flag counts $3,1,2,1,2,2,2$. By @prop:coble-flag-orbits-and-edges(1) the primitive lines of a plane fall into the nonzero classes of $J(\Pi)$, and by (2), applied with $\Gamma = R$, an $R$-orbit of lines of $T_\Co$ is determined by the $H$-orbit of its class, $H = \bar\rho(R) = P$; so the $0$-cusps of $D(T_\Co)/R$ in the closure of the $1$-cusp are the $H$-orbits of those classes, one for each distinct size in the list. By @thm:orbit-per-cusp the $P$-orbit of $[\eta_k/2]$ has size $2$, $120$, $270$, $135$ for $k = 2,3,4,5$, so the size list is the set of Sterk labels of the plane, that is its type [@AEGS25, Not. 3.1]. The sizes are pairwise distinct in each plane, so the number of $0$-cusps through the $1$-cusp equals its flag count, which is the equality case of @prop:coble-flag-orbits-and-edges(3) and reproduces the $13$ edges. The seven planes are therefore of types $\{2,4,5\}$, $\{5\}$, $\{3,5\}$, $\{5\}$, $\{3,5\}$, $\{3,4\}$, $\{4,5\}$, where $\{5\}$ is Sterk's $\{5,5\}$. So $m$ is $1,1,2,1,2$ on $(\{2,4,5\},\{4,5\},\{3,5\},\{3,4\},\{5,5\})$, which is the third alternative of $3$ and $4$. The type $\{5,5\}$ is the label set $\{5\}$: the two plane orbits of that label set each meet $0_5$ once, which is the degree $2$ that $0_5$ gains from them. The computation is `computations/reports/coble_789-one-cusp-multiplicities.py`, which reads that record, checks that the sizes are pairwise distinct and that their number is the flag count plane by plane, and checks the totals $7$ and $13$.
:::

::: {.theorem #thm:cusp-diagram-tco title="The cusp diagram of $D(T_\Co)/R$"}
1. *$0$-cusps.* There are four, written $0_2$, $0_3$, $0_4$, $0_5$, lying one over each of Sterk's $0$-cusps $2$, $3$, $4$, $5$, and none over cusp $1$ (@thm:cusp-fibres-four); in the marked form the same four are the marked $0$-cusps of @thm:coble-cusp-admissibility(2).
2. *$1$-cusps.* A $1$-cusp of $D(T_\Co)/R$ lies over exactly one of Sterk's nine $1$-cusps, whose type is a subset $T\subset\{1,2,3,4,5\}$ in the notation of [@AEGS25, Not. 3.1] and [@Ste91, §4.3.15], as the volume uses it at @thm:coble-cusp-admissibility(3). There are none over the four types $\{1,2\}$, $\{1,3\}$, $\{1,4\}$, $\{1,5\}$ (@lem:one-cusp-over-cusp-one-empty), and $7$ in all over the five types $\{2,4,5\}$, $\{4,5\}$, $\{3,5\}$, $\{3,4\}$, $\{5,5\}$: the fibre over $\{2,4,5\}$ is a single point, that over $\{5,5\}$ has two points, and exactly one of the fibres over $\{4,5\}$, $\{3,5\}$, $\{3,4\}$ has two points while the other two are single points (@thm:one-cusp-multiplicities).
3. *Incidence.* For $k\in\{2,3,4,5\}$ the $0$-cusp $0_k$ lies in the closure of a $1$-cusp over $T$ exactly when $k\in T$ (@lem:cusp-incidence-rule). Consequently $0_2$ meets only the $1$-cusps over $\{2,4,5\}$, $0_3$ those over $\{3,5\}$ and $\{3,4\}$, $0_4$ those over $\{2,4,5\}$, $\{4,5\}$ and $\{3,4\}$, and $0_5$ those over $\{2,4,5\}$, $\{4,5\}$, $\{3,5\}$ and $\{5,5\}$.
4. The number of incidence edges is $\sum_T m_T\,\#(T\cap\{2,3,4,5\}) = 13$, and the degrees of $0_2$, $0_3$, $0_4$, $0_5$ are $1$, $3$, $3$, $6$ (@thm:one-cusp-multiplicities(5), where the multiplicities are proved from the discriminant counts $7$ and $13$ of @thm:coble-integral-lifting-fibre(4)(b) and the plane-orbit record, read through @prop:coble-flag-orbits-and-edges and @thm:orbit-per-cusp).
:::

::: {.proof}
$1$ is @thm:cusp-fibres-four, and $2$ is @thm:b2-one-cusps with @lem:one-cusp-over-cusp-one-empty and @lem:five-one-cusps-nonempty.

$3$ is @lem:cusp-incidence-rule.

$4$ is the incidence rule read with the multiplicities of @thm:one-cusp-multiplicities(5): the degree of $0_k$ is $\sum_{T\ni k}m_T$, which gives $1$, $3$, $3$, $6$, and the total is $13$ by @thm:one-cusp-multiplicities(2). Those multiplicities are proved on the discriminant route: the $R$-orbits on primitive isotropic planes and on flags number $7$ and $13$ (@thm:coble-integral-lifting-fibre(4)(b)); a plane's type is the set of $H$-orbits of the nonzero classes of $J(\Pi)$, one per distinct discriminant-orbit size (@prop:coble-flag-orbits-and-edges(1), (2)); those sizes are the labels $2,3,4,5$ by @thm:orbit-per-cusp; and the seven plane orbits of the record split $1,1,2,1,2$ over the five types.

The separate computation of the stabilizer's orbits is a consistency check and not a proof step: it returns upper bounds $(1,4,2,2,3)$ from the library's `setwise_stabilizer` generator family, which is incomplete at three of the five types, as @rmk:plane-stabilizer-orbit-attempt records. Those bounds are consistent with the five values $1,1,2,1,2$ and do not sharpen them.
:::

::: {.remark #rmk:plane-stabilizer-orbit-attempt title="The library's plane-stabilizer family, and the orbits it gives"}
The computation the $1$-cusp route needs — the image of $\Stab_{\gent}(\Pi)$ in $\Orth(K_\Pi)$ and its orbits on the eight pairs — was run with the library's own call: `TEn.Aut().setwise_stabilizer` on the plane $\Pi$ of each of the five types, in `NamedLattices.TEn`, the generators then filtered to those of $\gent$ by their discriminant action (AEGS Def. 2.6, Sterk Prop. 2.7). The computation is `computations/reports/coble_789-plane-stabilizer-orbits.py`, whose transcript is printed beside it; every generator retained is verified to be an isometry, to preserve $A_{U(2)}$ and to carry $\Pi$ to itself.

The orbits it returns on the eight antipodal pairs are, for the types $(\{2,4,5\},\{4,5\},\{3,5\},\{3,4\},\{5,5\})$, the tuple $(1,4,2,2,3)$. A subgroup's orbits refine the whole stabilizer's, so these are UPPER BOUNDS for the five fibres, obtained from a generator family that is not complete: the independently computed values of @thm:one-cusp-multiplicities are $(1,1,2,1,2)$. The two agree at $\{2,4,5\}$ and $\{3,5\}$ and disagree at $\{4,5\}$, $\{3,4\}$ and $\{5,5\}$, so the family the library returns generates a proper subgroup of the stabilizer there: it is not certified complete, which is the same deficit that `vector_stabilizer_generators` is documented with for the vector case.

Consequently the multiplicities remain those of the discriminant route, and the $1$-cusp side of the diagram is not derived from the cusp stabilizer. The request for a certified-complete plane-stabilizer family is written out in `computations/reports/coble_789-sage-extensions-request.md`, with this run as the witness; the connected GitHub connection is read-only for issues, so it is recorded there rather than posted.
:::

::: {.remark #rmk:certified-versus-printed-chamber title="The certified cusp-$2$ chamber and Sterk's printed roots"}
The ten walls of the certified chamber of @thm:ou-e8-transitive are $\alpha_1,\dots,\alpha_8$, $-e+f$ and $\bar\alpha_8-2f$ in the coordinates of `computations/reports/coble_TEn-chambers-run.txt`. Sterk prints the last of them as $\alpha_9 = \bar\alpha_8+2f$ [@Ste91, 4.3.6], a different vector: the two differ by $4f$, and the record `computations/reports/coble_sterk-reflection-subgroups-run.txt` reports that nine of his ten printed roots are walls of the certified chamber. The count of $(-2)$-walls is one in both cases, since $-2f-\omega_8$ has square $-4$; what the printed set cannot be used for is the chamber-translate principle, which needs a fundamental chamber and is therefore applied above to the certified one. The identification of Sterk's ten printed roots with the white nodes of [@AEGS25, Figs.~7--8] is unaffected: it concerns the simple $(-2)$- and $(-4)$-roots at each cusp, and the white node at cusp $2$ is $e-f$ in both lists.
:::

::: {.remark #rmk:cusp-fibre-what-remains title="Which input decides which fibre"}
The fibre over Sterk's $0$-cusp $2$ is decided directly: the image of $\Stab_{\gent}(e')$ is the full orthogonal group of the cusp lattice [@Ste91, 4.3.6], that group is transitive on the $(-2)$-vectors (@thm:ou-e8-transitive), and the $\ZZ e'$-translates are absorbed by the transvections of @lem:ze-translates-in-gent. At Sterk's $0$-cusps $3$, $4$, $5$ the same argument does not apply, because the stabilizer image is the group generated by the printed reflections and the symmetries of their diagram, $\{\pm1\}W_k\rtimes S_k$ [@Ste91, 4.3.7--4.3.9], and $W_k$ is a proper subgroup of $W(K_k)$ of index $240$, $270$, $34\,560$ (@thm:sterk-reflection-subgroup-index); what decides those three fibres is the count of four $R$-orbits (@thm:four-r-orbits) together with @prop:fibres-three-four-five. The five $1$-cusp fibres are decided in two steps, and neither is a computation of the image of $\Stab_{\gent}(\Pi)$ in $\Orth(K_\Pi)$. What the published cusp groups give at a $1$-cusp is a subgroup of $\GL(\Pi)$: the intersection of the image of $\Stab_{\gent}(\Pi)$ in $\GL(\Pi)$ with $\SL(\Pi)$ is $\Gamma(2)$ for the type $\{2,4,5\}$ and $\Gamma^1(2)$ for $\{4,5\}$, $\{3,5\}$ and $\{3,4\}$ [@Ste91, §4.3.16--4.3.17], as the volume's count of plane orbits records. That group acts on $\Pi$, not on $K_\Pi$, so it does not act on the sixteen classes of square $-2$; the action of the stabilizer on those classes is a further datum. By @lem:reflections-fix-the-pairs the reflections inside $\Stab_{\gent}(\Pi)$ --- the ones @thm:coble-cusp-admissibility(1) certifies to lie in $\gent$ --- fix all eight pairs, so the orbits on the pairs are those of the image modulo the reflection subgroup, and no page of the volume states generators for that image; what reaches the pairs is the $P$-action on $A_{T_\Co}$ of @prop:coble-flag-orbits-and-edges, which is why the multiplicities are computed there and not here. First @lem:five-one-cusps-nonempty, from the divisibility computation of `computations/reports/coble_789-one-cusp-divisibility.py`, gives one orbit per $(-2)$-class and hence at most eight per fibre (@lem:minus-id-in-gent); then @thm:one-cusp-multiplicities fixes the five multiplicities from the counts $7$ and $13$ of @thm:coble-integral-lifting-fibre(4)(b) and the plane-orbit record `computations/reports/coble_gco_plane-orbits-run.txt`, read through @prop:coble-flag-orbits-and-edges and the label dictionary of @thm:orbit-per-cusp. So the multiplicities are computed by the volume's discriminant route and attributed to the types here, not computed from the cusp stabilizer; the outcome agrees with the B2 bound of eight and with the total $7$.
:::
