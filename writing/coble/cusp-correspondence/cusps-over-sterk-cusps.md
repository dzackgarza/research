# The cusps of $D(T_\Co)/R$ over Sterk's cusps {#sec-cusps-over-sterk-cusps}

This section proves statement B2 of the plan for $F_\Co$ [research#786, Part I §5; research#789]: the $0$- and the $1$-cusps of $D(T_\Co)/R$ are the $\gent$-orbits of pairs $(\ell,\alpha)$, an isotropic line or plane $\ell$ of $\ten$ together with a $(-2)$-vector $\alpha$ perpendicular to it, and they fibre over Sterk's cusps of $F_{\En,2}$ by forgetting $\alpha$. The fibre over Sterk's cusp $[e_k]$ is the set of $\Stab_{\gent}(e_k)$-orbits of $(-2)$-vectors perpendicular to $e_k$, where the stabilizer is that of the isotropic *line* $\ZZ e_k$. The smallest case of that computation, Sterk's cusp $2$, is carried out here: the $(-2)$-vectors perpendicular to its representative form a single $\Orth(K_2)$-orbit. Every statement below names its group, and none of the counts is a count for $F_\Co$ or $F_{\Co,2}$.

## Setting

Let $L = \latII_{3,19} = U^{\oplus3}\oplus E_8^{\oplus2}$ be the K3 lattice and
$$
\ten = U\oplus U(2)\oplus E_8(2)\cong(12,10,0)_2
$$
the lattice of [@AEGS25, Def. 2.3, printed p. 586], with basis $e,f,e',f',\alpha_1,\dots,\alpha_8$: $e\cdot f = 1$, $e'\cdot f' = 2$, and $\alpha_1,\dots,\alpha_8$ the simple roots of the summand $E_8(2)$, of square $-4$. Put
$$
\delta \definedas e - f,\qquad \delta^2 = -2,\qquad
T_\Co \definedas \delta^{\perp\ten} = \generators{e+f}\oplus U(2)\oplus E_8(2)\cong\generators{2}\oplus E(2),
$$
the Coble lattice of [@DK13, (3.6) and Prop. 3.2, printed p. 513]; the identification of $\generators{e+f}$ with $\generators{2}$ uses $(e+f)^2 = 2\,e\cdot f = 2$. Let
$$
\gent = \Gamma_{\En,2}\leq\Orth(\ten)
$$
be the image of $\{g\in\Orth(L) : g\Ien = \Ien g,\ g(h) = h\}$, $h$ the degree-$2$ polarization [@AEGS25, Def. 2.6, printed p. 587]; this is the group $\Gamma$ of [@Ste91, Prop. 2.7, printed p. 7], characterised there as the set of isometries of $\ten$ whose induced map on $A_{\ten} = A_{U(2)}\oplus A_{E_8(2)}$ respects the two summands. Let
$$
R \definedas R_{\gent} = \text{the image of } \Stab_{\gent}(\delta) \text{ in } \Orth(\delta^{\perp\ten}) = \Orth(T_\Co)
$$
[@def:gamma-co-groups(4)]; equivalently $R = \bar\rho^{-1}(P)$, where $\bar\rho\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is the discriminant representation and $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ the stabilizer of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$, so that
$$
[\Orth(T_\Co):R] = \abs{\Orth(q_{T_\Co})}/\abs{P} = 2^7\cdot17\cdot31 = 67\,456
$$
[@prop:gamma-co-images(3), @thm:gamma-co-2-comparison(3)].

The boundary components of a type IV quotient $D(\Lambda)/\Gamma$ are described as follows: a $0$-cusp is a $\Gamma$-orbit of primitive isotropic lines of $\Lambda$, a $1$-cusp a $\Gamma$-orbit of primitive isotropic planes [@AEGS25, Def. 2.9, printed p. 588]. Sterk's five $0$-cusps of $F_{\En,2} = D(\ten)/\gent$ are represented by
$$
e,\qquad e',\qquad e'+f'+y_3,\qquad 2e'+f'+y_4,\qquad 2e+2f+y_4,
$$
with $y_3 = -(2\alpha_1+3\alpha_2+4\alpha_3+6\alpha_4+5\alpha_5+4\alpha_6+3\alpha_7+2\alpha_8)$ of square $-4$ and $y_4 = -(4\alpha_1+5\alpha_2+7\alpha_3+10\alpha_4+8\alpha_5+6\alpha_6+4\alpha_7+2\alpha_8)$ of square $-8$ [@Ste91, (4.2.3), printed p. 16], and are numbered $1,\dots,5$ in that order; the numbering and the vectors are those of @ex:sterk-isotropic-divisibilities. Throughout, $\Stab_{\gent}(e_k)$ denotes the stabilizer in $\gent$ of the line $\ZZ e_k$.

## Primitivity

::: {.lemma #lem:primitivity-tco-in-ten title="A vector primitive in $T_\Co$ is primitive in $\ten$"}
If $v\in T_\Co$ is primitive in $T_\Co$, it is primitive in $\ten$.
:::

::: {.proof}
Suppose $v = mw$ with $w\in\ten$ and $m>1$. Since $v\in T_\Co = \delta^{\perp\ten}$, $0 = v\cdot\delta = m\,(w\cdot\delta)$, hence $w\cdot\delta = 0$ and $w\in\delta^{\perp\ten} = T_\Co$. So $v$ is not primitive in $T_\Co$.
:::

Consequently a primitive isotropic line or plane of $T_\Co$ is a primitive isotropic line or plane of $\ten$, and a $\gent$-orbit of such objects of $\ten$ that meets $T_\Co$ consists of objects of $T_\Co$. This is what makes the forgetful map on cusps below well defined.

## The correspondence

::: {.theorem #thm:b2-zero-cusps title="B2 for $0$-cusps: the $0$-cusps of $D(T_\Co)/R$ are the $\gent$-orbits of pairs $(\ell,\alpha)$"}
Let $\mathcal P_0$ be the set of pairs $(\ell,\alpha)$ in which $\ell\subset\ten$ is a primitive isotropic line and $\alpha\in\ten$ is a $(-2)$-vector with $\alpha\perp\ell$, and let $\gent$ act on $\mathcal P_0$ by $g(\ell,\alpha) = (g\ell,g\alpha)$. Then:

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
The target is right: $(\gamma^{-1}\delta)\cdot e_k = \delta\cdot(\gamma e_k) = 0$ because $\gamma e_k\in T_\Co = \delta^{\perp}$, and $\delta^2 = -2$. The map is invariant under left multiplication by $R = \Stab_{\gent}(\delta)$, because $(r\gamma)^{-1}\delta = \gamma^{-1}r^{-1}\delta = \gamma^{-1}\delta$; and it is equivariant for right multiplication by $s\in\Stab_{\gent}(e_k)$, with $s e_k = \pm e_k$, acting on $L_k$ by $\alpha\mapsto s^{-1}\alpha$, which preserves $L_k$ because $(s^{-1}\alpha)\cdot e_k = \alpha\cdot(s e_k) = \pm\alpha\cdot e_k = 0$. It is surjective: for $\alpha\in L_k$, transitivity of $\gent$ on the $(-2)$-vectors of $\ten$ [@Ste91, 2.10, printed p. 8] gives $\gamma\in\gent$ with $\gamma\alpha = \delta$, and then $\gamma e_k\perp\delta$ and $\Psi_k(\gamma) = \gamma^{-1}\delta = \alpha$. It is injective on $R$-orbits: if $\gamma^{-1}\delta = \gamma'^{-1}\delta$ then $\gamma'\gamma^{-1}\delta = \delta$, so $\gamma'\gamma^{-1}\in R$ and $\gamma'$ lies in the $R$-orbit of $\gamma$. Hence $\Psi_k$ induces a bijection
$$
R\backslash\tilde Y_k/\Stab_{\gent}(e_k)\ \cong\ \Stab_{\gent}(e_k)\backslash L_k,
$$
and the left-hand side is $R\backslash\mathcal Y_k$, the fibre.

$(3)$ The $0$-cusps of $F_{\En,2}$ are the $\gent$-orbits of primitive isotropic lines, and Sterk's five representatives exhaust them [@Ste91, (4.2.3), printed p. 16], so the cusp set of $F_{\En,2}$ is the disjoint union of the five orbits and (2) applies over each. For the second bijection, send the $R$-orbit of $\ell$ to the $\gent$-orbit of $(\ell,\delta)$, and the $\gent$-orbit of $(\ell,\alpha)$ to the $R$-orbit of $\gamma\ell$, where $\gamma\in\gent$ is any element with $\gamma\alpha = \delta$; that $\gamma\ell\subset T_\Co$ and that its $R$-orbit does not depend on $\gamma$ are the computations of (2), and the two assignments are inverse by construction.
:::

::: {.theorem #thm:b2-one-cusps title="B2 for $1$-cusps"}
The same statement with "line" replaced by "plane": the $1$-cusps of $D(T_\Co)/R$ are the $\gent$-orbits of pairs $(\Pi,\alpha)$ in which $\Pi\subset\ten$ is a primitive isotropic plane and $\alpha\in\ten$ is a $(-2)$-vector with $\alpha\perp\Pi$; the fibre over Sterk's $1$-cusp $[\Pi]$ is the set of $\Stab_{\gent}(\Pi)$-orbits of $(-2)$-vectors $\alpha\perp\Pi$, the stabilizer being taken in the plane $[\Pi]$.

For such a $\Pi$ the quotient $\Pi^{\perp\ten}/\Pi$ is negative definite, so the set of $(-2)$-vectors perpendicular to $\Pi$ modulo $\Pi$ is finite and the fibre is a finite set.
:::

::: {.proof}
Every step of the proof of @thm:b2-zero-cusps uses only that $\ell$ is a primitive isotropic subspace of $\ten$ and that a primitive isotropic subspace of $T_\Co$ is one of $\ten$ (@lem:primitivity-tco-in-ten), so it applies verbatim to primitive isotropic planes. The identification of the $1$-cusps of $F_{\En,2}$ with the $\gent$-orbits of primitive isotropic planes is [@AEGS25, Def. 2.9, printed p. 588]; Sterk's nine $1$-cusps are [@Ste91, §4.3, printed pp. 17--25]. The quotient $\Pi^{\perp}/\Pi$ has signature $(0,8)$, because $\Pi$ is a maximal isotropic plane in a lattice of signature $(2,10)$; a negative definite integral lattice has finitely many vectors of a given norm.
:::

## The fibre over Sterk's cusp $2$: the smallest case

At Sterk's cusp $2$ the stabilizer is the whole orthogonal group of the cusp lattice, so the fibre is decided without any information about the other cusps. Cusp $1$ is the other extreme: it carries no $(-2)$-vector at all.

::: {.proposition #prop:fibre-cusp-one-empty title="The fibre over Sterk's cusp $1$ is empty"}
At Sterk's cusp $1$, with representative $e_1 = e$, one has $K_1 = e_1^{\perp\ten}/\ZZ e_1\cong U(2)\oplus E_8(2)$, every vector of which has square divisible by $4$. In particular $K_1$ contains no $(-2)$-vector, and the fibre of $\Phi_0$ over Sterk's cusp $1$ is empty.
:::

::: {.proof}
$e^{\perp\ten} = \generators{e}\oplus U(2)\oplus E_8(2)$, so $K_1\cong U(2)\oplus E_8(2)$; this is [@Ste91, 4.3.4, printed p. 19], whose statement is $e^{\perp}/\ZZ e\cong\mathbf H(2)\oplus E_8(-2)$. Both summands are twice an even lattice, so every square in $K_1$ lies in $4\ZZ$, and $-2\notin4\ZZ$.
:::

::: {.theorem #thm:ou-e8-transitive title="$\Orth(U\oplus E_8(2))$ is transitive on the $(-2)$-vectors"}
Let $K = U\oplus E_8(2)$. Then $\Orth(K)$ acts transitively on $\{x\in K : x^2 = -2\}$.
:::

::: {.proof}
By [@Ste91, 4.3.6, printed p. 21], $K$ is the cusp lattice $K_2 = (e')^{\perp\ten}/\ZZ e'$ of Sterk's cusp $2$ --- Sterk writes $H\oplus E_8(-2)$ for $U\oplus E_8(2)$ --- and
$$
\Orth(K) = \{\pm1\}\cdot W_{e'},
$$
where $W_{e'}$ is the group generated by the reflections in the ten simple roots $\alpha_1,\dots,\alpha_8$, $\alpha_9 = \omega_8+2f$, $\alpha_{10} = e-f$ displayed in Sterk's Fig. 6, $\omega_8$ being the fundamental weight of $E_8(2)$ dual to $\alpha_8$; all ten are roots of $K$, and $\alpha_9$, like $\alpha_1,\dots,\alpha_8$, has square $-4$. That diagram is a Coxeter diagram: its bonds are single or double, so its dihedral angles are $\pi/2$, $\pi/3$ or $\pi/4$, all submultiples of $\pi$. By Vinberg's theorem [@Vin85, §1, no. 1, printed pp. 31--32], a Coxeter polytope $P$ is a fundamental polytope for the group generated by the reflections in its walls, the polytopes $\gamma P$, $\gamma\in W_{e'}$, tessellate the hyperbolic space $\mathbf H$ attached to $K$, and every mirror of a reflection of $W_{e'}$ is a wall of that tessellation.

Let $x\in K$ with $x^2 = -2$ and let $s_x$ be the reflection in $x$. Since $s_x\in\Orth(K) = \{\pm1\}W_{e'}$, and $\pm1$ acts trivially on $\mathbf H$, the isometry of $\mathbf H$ induced by $s_x$ lies in the image of $W_{e'}$; it is the reflection of $\mathbf H$ with fixed hyperplane $x^{\perp}\cap\mathbf H$. By Vinberg's theorem that hyperplane is a wall of the tessellation, so $x^{\perp} = w(\alpha_i^{\perp})$ for some $w\in W_{e'}$ and some $i\in\{1,\dots,10\}$, that is $x = \pm w(\alpha_i)$. Of the ten simple roots only $\alpha_{10} = e-f$ has square $-2$; the other nine have square $-4$. Hence every $(-2)$-vector of $K$ lies in the $W_{e'}$-orbit of $\pm(e-f)$, and $\Orth(K)$ is transitive.
:::

::: {.corollary #cor:fibre-cusp-two title="The fibre over Sterk's cusp $2$ maps onto a single point"}
The fibre of $\Phi_0$ over Sterk's cusp $2$ is nonempty, and its image under $\alpha\mapsto\bar\alpha$ in $K_2$ is a single $\Orth(K_2)$-orbit: the class of $\delta = e-f$, which is perpendicular to $e'$. Indeed the image of $\Stab_{\gent}(e')$ in $\Orth(K_2)$ is all of $\Orth(K_2)$ [@Ste91, 4.3.6, printed p. 21], and $\Orth(K_2)$ is transitive on the $(-2)$-vectors of $K_2$ (@thm:ou-e8-transitive).
:::

::: {.proof}
Immediate from @thm:b2-zero-cusps(2), the two cited statements, and $\delta\perp e'$. The fibre is the set of $\Stab_{\gent}(e')$-orbits of $(-2)$-vectors $\alpha\perp e'$, and the map $\alpha\mapsto\bar\alpha\in K_2$ is $\Stab_{\gent}(e')$-equivariant and surjective onto the $(-2)$-vectors of $K_2$; a surjective equivariant map of orbit sets is surjective.
:::

::: {.remark #rmk:fibre-cusp-two-translates title="The one step from the $\Orth(K_2)$-orbit to the fibre"}
The fibre is the set of $\Stab_{\gent}(e')$-orbits on the $(-2)$-vectors $\alpha\perp e'$, and two such vectors have the same image in $K_2$ exactly when they differ by a multiple of $e'$. So the fibre is a single point exactly when $\Stab_{\gent}(e')$ acts transitively on the $\ZZ e'$-translates of a $(-2)$-vector, that is when the Eichler transvections of @lem:cusp-root-lift-independence --- which move $\delta$ to $\delta-ke'$ at the level of $\ten$ --- lie in $\gent$. Their membership in $\Orth(\ten)$ is @lem:cusp-root-lift-independence; their membership in $\gent$ is not established here, and it is the one step of the computation at cusp $2$ which this page does not carry out. The four-cusp statement below does not use it: it uses the independent count of four $R$-orbits.
:::

## The other fibres, and the four $0$-cusps

::: {.proposition #prop:fibres-three-four-five title="The fibres over Sterk's cusps $3$, $4$ and $5$ are nonempty"}
At Sterk's cusps $3$, $4$ and $5$ the cusp lattice is $K_k\cong U\oplus E_8(2)$ as well [@Ste91, 4.3.4, printed p. 19], and each carries a $(-2)$-vector perpendicular to its representative, as follows; the vectors are the white nodes of [@AEGS25, Figs.~7--8, printed pp.~594--595], and the coordinates are those of the record `computations/reports/coble_enriques-white-root-facets-run.txt` in the basis $(e,f,e',f',\alpha_1,\dots,\alpha_8)$ of $\ten$.
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

::: {.theorem #thm:cusp-fibres-four title="The $0$-cusps of $D(T_\Co)/R$ lie one over each of Sterk's cusps $2,3,4,5$"}
The map $\Phi_0$ of @thm:b2-zero-cusps has empty fibre over Sterk's cusp $1$ (@prop:fibre-cusp-one-empty) and a nonempty fibre over each of Sterk's cusps $2$, $3$, $4$, $5$ (@cor:fibre-cusp-two, @prop:fibres-three-four-five). The subgroup $R$ has exactly four orbits on the primitive isotropic lines of $T_\Co$ [@prop:coble-cong-point-stabilizer(3), the subgroup being $R = \bar\rho^{-1}(P)$ by @prop:gamma-co-images(3)], so $D(T_\Co)/R$ has exactly four $0$-cusps. Hence each of the four nonempty fibres is a single point, and the four $0$-cusps of $D(T_\Co)/R$ are in bijection with Sterk's cusps $2,3,4,5$, one over each.
:::

::: {.proof}
The fibres of $\Phi_0$ partition the $0$-cusps of $D(T_\Co)/R$: $\Phi_0$ is well defined by @thm:b2-zero-cusps(1), and the cusp set of $F_{\En,2}$ is the disjoint union of the five orbits of Sterk's representatives. One fibre is empty (@prop:fibre-cusp-one-empty) and the other four are nonempty (@cor:fibre-cusp-two, @prop:fibres-three-four-five), so they partition the four $0$-cusps of $D(T_\Co)/R$ into four nonempty parts. The count of four is not read off the fibres: it is @prop:coble-cong-point-stabilizer(3), whose proof identifies the $R$-orbits on primitive isotropic vectors with the $P$-orbits on the $527$ nonzero isotropic classes through the discriminant class $v\mapsto[v/2]$, a bijection on $K$-orbits by @thm:coble-zero-cusp-count(1).
:::

::: {.remark #rmk:cusp-fibre-what-remains title="What the computation of the fibres does and does not use"}
The fibre over cusp $2$ is computed directly, from Sterk's identification of the stabilizer with the full orthogonal group of the cusp lattice and the transitivity of that group on the $(-2)$-vectors. The same argument does not apply at cusps $3$, $4$, $5$: there Sterk computes the stabilizer image as the group generated by the reflections in the printed chamber and the symmetries of its diagram, $\{\pm1\}W_k\rtimes S_k$ [@Ste91, 4.3.7--4.3.9, printed pp. 22--24; that the whole image is generated by the reflection subgroup and the diagram symmetries is the general statement of @Ste91, 4.3.2, printed p. 17], and the reflection subgroup $W_k$ is a proper subgroup of $W(K_k)$: its index is $240$, $270$ and $34\,560$ at $k = 3,4,5$ (@thm:sterk-reflection-subgroup-index). Whether that proper subgroup is nonetheless transitive on the $(-2)$-vectors of $K_k$ is exactly the fibre computation at that cusp, and it is not carried out here. What decides those three fibres here is the count of four $R$-orbits together with the nonemptiness of @prop:fibres-three-four-five. A direct computation of the image of the stabilizer at cusps $3$, $4$, $5$ and of its orbits on the $(-2)$-vectors, which would give the three fibres independently of that count, remains; were it to return more than one orbit at any of the three cusps, @thm:coble-zero-cusp-count, and with it the count of four, would be false.
:::
