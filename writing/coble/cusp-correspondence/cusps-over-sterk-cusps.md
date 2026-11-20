# The cusps of $D(T_\Co)/R$ over Sterk's cusps {#sec-cusps-over-sterk-cusps}

This section proves statement B2 of the plan for $F_\Co$ [research#786, Part I §5; research#789]: the $0$- and the $1$-cusps of $D(T_\Co)/R$ are the $\gent$-orbits of pairs $(\ell,\alpha)$, an isotropic line or plane $\ell$ of $\ten$ together with a $(-2)$-vector $\alpha$ perpendicular to it, and they fibre over Sterk's cusps of $F_{\En,2}$ by forgetting $\alpha$. The fibre over Sterk's cusp $[e_k]$ is the set of $\Stab_{\gent}(e_k)$-orbits of $(-2)$-vectors perpendicular to $e_k$, where the stabilizer is that of the isotropic *line* $\ZZ e_k$. The smallest case of that computation, Sterk's cusp $2$, is carried out here: the $(-2)$-vectors perpendicular to its representative form a single $\Orth(K_2)$-orbit. Every statement below names its group, and none of the counts is a count for $F_\Co$ or $F_{\Co,2}$.

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
the Coble lattice of [@DK13, (3.6) and Prop. 3.2]; the identification of $\generators{e+f}$ with $\generators{2}$ uses $(e+f)^2 = 2\,e\cdot f = 2$. Let
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
If $v\in T_\Co$ is primitive in $T_\Co$, it is primitive in $\ten$.
:::

::: {.proof}
Suppose $v = mw$ with $w\in\ten$ and $m>1$. Since $v\in T_\Co = \delta^{\perp\ten}$, $0 = v\cdot\delta = m\,(w\cdot\delta)$, hence $w\cdot\delta = 0$ and $w\in\delta^{\perp\ten} = T_\Co$. So $v$ is not primitive in $T_\Co$.
:::

Consequently a primitive isotropic line or plane of $T_\Co$ is a primitive isotropic line or plane of $\ten$. This, and $R\leq\gent$, is what makes the forgetful map on cusps below well defined; a $\gent$-orbit of lines or planes of $\ten$ need not however preserve $\delta^{\perp}=T_\Co$, and none of the arguments below uses such a statement.

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
The target is right: $(\gamma^{-1}\delta)\cdot e_k = \delta\cdot(\gamma e_k) = 0$ because $\gamma e_k\in T_\Co = \delta^{\perp}$, and $\delta^2 = -2$. The map is invariant under left multiplication by $R = \Stab_{\gent}(\delta)$, because $(r\gamma)^{-1}\delta = \gamma^{-1}r^{-1}\delta = \gamma^{-1}\delta$; and it is equivariant for right multiplication by $s\in\Stab_{\gent}(e_k)$, with $s e_k = \pm e_k$, acting on $L_k$ by $\alpha\mapsto s^{-1}\alpha$, which preserves $L_k$ because $(s^{-1}\alpha)\cdot e_k = \alpha\cdot(s e_k) = \pm\alpha\cdot e_k = 0$. It is surjective: for $\alpha\in L_k$, transitivity of $\gent$ on the $(-2)$-vectors of $\ten$ [@Ste91, 2.10] gives $\gamma\in\gent$ with $\gamma\alpha = \delta$, and then $\gamma e_k\perp\delta$ and $\Psi_k(\gamma) = \gamma^{-1}\delta = \alpha$. It is injective on $R$-orbits: if $\gamma^{-1}\delta = \gamma'^{-1}\delta$ then $\gamma'\gamma^{-1}\delta = \delta$, so $\gamma'\gamma^{-1}\in R$ and $\gamma'$ lies in the $R$-orbit of $\gamma$. Hence $\Psi_k$ induces a bijection
$$
R\backslash\tilde Y_k/\Stab_{\gent}(e_k)\ \cong\ \Stab_{\gent}(e_k)\backslash L_k,
$$
and the left-hand side is $R\backslash\mathcal Y_k$, the fibre.

$(3)$ The $0$-cusps of $F_{\En,2}$ are the $\gent$-orbits of primitive isotropic lines, and Sterk's five representatives exhaust them [@Ste91, (4.2.3)], so the cusp set of $F_{\En,2}$ is the disjoint union of the five orbits and (2) applies over each. For the second bijection, send the $R$-orbit of $\ell$ to the $\gent$-orbit of $(\ell,\delta)$, and the $\gent$-orbit of $(\ell,\alpha)$ to the $R$-orbit of $\gamma\ell$, where $\gamma\in\gent$ is any element with $\gamma\alpha = \delta$; that $\gamma\ell\subset T_\Co$ and that its $R$-orbit does not depend on $\gamma$ are the computations of (2), and the two assignments are inverse by construction.
:::

::: {.theorem #thm:b2-one-cusps title="B2 for $1$-cusps"}
The same statement with "line" replaced by "plane": the $1$-cusps of $D(T_\Co)/R$ are the $\gent$-orbits of pairs $(\Pi,\alpha)$ in which $\Pi\subset\ten$ is a primitive isotropic plane and $\alpha\in\ten$ is a $(-2)$-vector with $\alpha\perp\Pi$; the fibre over Sterk's $1$-cusp $[\Pi]$ is the set of $\Stab_{\gent}(\Pi)$-orbits of $(-2)$-vectors $\alpha\perp\Pi$, the stabilizer being taken in the plane $[\Pi]$.

For such a $\Pi$ the quotient $\Pi^{\perp\ten}/\Pi$ is negative definite, so there are finitely many $(-2)$-classes in $\Pi^{\perp\ten}/\Pi$; that the fibre itself is finite is @lem:one-cusp-fibre-finite.
:::

::: {.proof}
Every step of the proof of @thm:b2-zero-cusps uses only that $\ell$ is a primitive isotropic subspace of $\ten$ and that a primitive isotropic subspace of $T_\Co$ is one of $\ten$ (@lem:primitivity-tco-in-ten), so it applies verbatim to primitive isotropic planes. The identification of the $1$-cusps of $F_{\En,2}$ with the $\gent$-orbits of primitive isotropic planes is [@AEGS25, Def. 2.9]; Sterk's nine $1$-cusps are [@Ste91, §4.3]. The quotient $\Pi^{\perp}/\Pi$ has signature $(0,8)$, because $\Pi$ is a maximal isotropic plane in a lattice of signature $(2,10)$, so a negative definite integral lattice has finitely many vectors of a given norm --- finitely many $(-2)$-classes, but not yet finitely many orbits on their lifts; the lifts are controlled by @lem:one-cusp-fibre-finite below.
:::

::: {.lemma #lem:one-cusp-fibre-finite title="The fibre over a $1$-cusp is finite"}
Let $\Pi\subset\ten$ be a primitive isotropic plane with a basis $u,v$ of isotropic vectors, and let $\alpha\in\ten$ have $\alpha^2 = -2$ and $\alpha\perp\Pi$. For $z\in u^{\perp\ten}$ the Eichler transvection
$$
E_{u,z}(x) \definedas x+(x,u)z-(x,z)u-\tfrac{z^2}{2}(x,u)u
$$
lies in $\gent$, fixes $\Pi$ setwise, and acts on $\Pi^{\perp\ten}$ by $x\mapsto x-(x,z)u$. The set of values $(\alpha,z)$, $z\in u^{\perp\ten}$, is an ideal $d_u\ZZ$ with $d_u\mid 2$, so the $\Stab_{\gent}(\Pi)$-orbit of $\alpha$ contains $\alpha+2u$; symmetrically it contains $\alpha+2v$. Hence that orbit contains $\alpha+2\Pi$ and $\Stab_{\gent}(\Pi)$ has at most four orbits on the lifts $\alpha+\Pi$, so the fibre over any $1$-cusp is finite.
:::

::: {.proof}
*Integrality and membership in $\gent$.* The vector $E_{u,z}(x)-x = (x,u)z-(x,z)u-\tfrac{z^2}{2}(x,u)u$ lies in $\ten$ for $x\in\ten$ because all three coefficients are integers, and $E_{u,z}(y)-y\in\ten$ for $y\in\ten^\vee$ for the same reason with $(y,u),(y,z)\in\ZZ$; so $E_{u,z}$ acts trivially on $A_{\ten}$ and lies in $\ker\rho_{\ten}\subseteq\gent$. The transformation is the Eichler transvection of [@GHS08, §3.1, Lemma 3.1 and the integrality assertion after (10)], of which the $E$ of @lem:ze-translates-in-gent is the case $u = e'$, $z = e$; the computation is `computations/reports/coble_789-one-cusp-finiteness.py`.

*It preserves $\Pi$.* $E_{u,z}(u) = u+(u,u)z-(u,z)u-\tfrac{z^2}{2}(u,u)u = u$ because $u^2 = 0$ and $z\cdot u = 0$, and $E_{u,z}(v) = v-(v,z)u\in\Pi$.

*It translates.* For $x\in\Pi^{\perp}$ one has $(x,u) = 0$, so $E_{u,z}(x) = x-(x,z)u$.

*The ideal.* Since $\alpha,z\in\ten$ the value $(\alpha,z)$ is an integer; the set of them is a subgroup of $\ZZ$, say $d_u\ZZ$. Because $\alpha\in\Pi^{\perp}\subset u^{\perp}$ one has $(\alpha,\alpha) = -2\in d_u\ZZ$, so $d_u\mid 2$. Hence $2u\in d_u\ZZ\cdot u$ and the orbit contains $\alpha+2u$; the same argument with $v$ in place of $u$ gives $\alpha+2v$.

*Finiteness.* The orbit of $\alpha$ therefore contains $\alpha+2\Pi$, so the orbits on the lifts of a $(-2)$-class are a quotient of $\Pi/2\Pi\cong(\ZZ/2)^2$ and number at most four. The $(-2)$-classes of $\Pi^{\perp}/\Pi$ are finite because that lattice is negative definite. So the fibre is finite.
:::

::: {.lemma #lem:one-cusp-over-cusp-one-empty title="The four $1$-cusps over Sterk's cusp $1$ have empty fibre"}
Let $[\Pi]$ be one of the four $1$-cusps of $F_{\En,2}$ whose closure contains Sterk's $0$-cusp $1$. Then $\Pi^{\perp\ten}/\Pi\cong E_8(2)$, every vector of which has square divisible by $4$; hence no $(-2)$-vector of $\ten$ is perpendicular to $\Pi$, and the fibre of the $1$-cusp map of @thm:b2-one-cusps over $[\Pi]$ is empty.
:::

::: {.proof}
Sterk computes the four one-dimensional boundary components whose closure contains the $0$-cusp $e$ [@Ste91, 4.3.5]: "These four classes are not distinguished by the isomorphism type of $F^{\perp}/F$ ... In all cases we even find the same isomorphism type, namely $E_8(-2)$" [@Ste91, 4.3.5], and the four types are listed in [@Ste91, 4.3.16]. In the notation of this page $E_8(-2)$ is $E_8(2)$. Its Gram matrix is $-2C(E_8)$, with diagonal entries $-4$ and off-diagonal entries $0$ or $2$, so for $x = \sum x_i\alpha_i$ one has $x^2 = -4\sum x_i^2+4\sum_{i<j,\ \alpha_i\cdot\alpha_j = 2}x_ix_j$, a multiple of $4$; in particular $-2$ does not occur. Since $\Pi$ is isotropic, the class of a vector $\alpha\perp\Pi$ in $\Pi^{\perp}/\Pi$ has square $\alpha^2$, so an $\alpha$ with $\alpha^2 = -2$ cannot exist. The fibre, which is the set of $\Stab_{\gent}(\Pi)$-orbits of such $\alpha$ (@thm:b2-one-cusps), is therefore empty. The case $\Pi = \langle e,e'\rangle$ of the type $\{1,2\}$ is checked directly in `computations/reports/coble_789-one-cusp-empty.py`: $\Pi^{\perp\ten} = \langle e,e'\rangle\oplus E_8(2)$.
:::

::: {.lemma #lem:divisibility-decides-one-cusp title="Divisibility of a $(-2)$-class in $\Pi^{\perp\ten}/\Pi$ decides its lifts"}
Let $\Pi\subset\ten$ be a primitive isotropic plane, $L_0 \definedas \Pi^{\perp\ten}/\Pi$, let $r\in L_0$ have $r^2 = -2$, and let $\alpha\in\Pi^{\perp\ten}$ be a lift of $r$ with $\alpha^2 = -2$. For $w\in\Pi$ put $d_w\ZZ \definedas \{(\alpha,z) : z\in w^{\perp\ten}\}$. Then:

1. $d_w$ divides $\mathrm{div}_{L_0}(r) \definedas \gcd\{(\alpha,z) : z\in\Pi^{\perp\ten}\}$;
2. if $\mathrm{div}_{L_0}(r) = 1$ then $\Stab_{\gent}(\Pi)$ is transitive on the lifts of $r$, so the lift contributes exactly one point to the fibre of @thm:b2-one-cusps over $[\Pi]$.
:::

::: {.proof}
$1$. Since $\Pi\subset\Pi^{\perp}$ one has $\Pi^{\perp}\subset w^{\perp}$, so the set of values over $w^{\perp}$ contains the set over $\Pi^{\perp}$ and its gcd divides that one. The values over $\Pi^{\perp}$ depend only on the class, because $(\alpha,p) = 0$ for $p\in\Pi$ as $\alpha\perp\Pi$; their gcd is $\mathrm{div}_{L_0}(r)$.

$2$. By $1$ and the hypothesis $d_w = 1$ for every $w\in\Pi$, so for each such $w$ there is $z\in w^{\perp}$ with $(\alpha,z) = 1$; the transvection $E_{w,z}$ of @lem:one-cusp-fibre-finite lies in $\gent$, preserves $\Pi$ setwise and sends $\alpha$ to $\alpha-w$. Every vector of $\Pi$ is isotropic, so taking $w$ to run over a basis $u,v$ of $\Pi$ shows that $\alpha-u$ and $\alpha-v$ lie in the orbit, hence $\alpha-p$ lies in the orbit for every $p\in\Pi$. Any other lift of $r$ is $\alpha-p$ for some $p\in\Pi$. Hence one orbit.
:::

::: {.theorem #lem:five-one-cusps-nonempty title="The exact fibre over each of the other five $1$-cusps: $16$ points"}
Let $[\Pi]$ be one of Sterk's five further $1$-cusps, of types $\{2,4,5\}$, $\{4,5\}$, $\{3,5\}$, $\{3,4\}$ and $\{5,5\}$ [@Ste91, 4.3.17]. Then:

1. $\Pi$ is primitive in $\ten$, and for a choice of a complementary basis the Gram matrix $G_0$ of $L_0 = \Pi^{\perp\ten}/\Pi$ is exact: its determinant is $64$, and $L_0$ has exactly $16$ vectors of square $-2$;
2. every one of those $16$ classes has $\mathrm{div}_{L_0}$ equal to $1$, certified by an explicit $z\in\Pi^{\perp}$ with $(\alpha,z) = 1$;
3. hence, by @lem:divisibility-decides-one-cusp, each class contributes exactly one orbit, and the fibre of the $1$-cusp map of @thm:b2-one-cusps over $[\Pi]$ has exactly $16$ points.
:::

::: {.proof}
The computation is `computations/reports/coble_789-one-cusp-divisibility.py`, whose transcript is printed beside it.

$1$. For each of the five planes the run checks that $\{u,v\}$ has Smith form $[1,1]$, so $\Pi$ is primitive in $\ten$; takes a basis $K$ of the kernel of the two functionals $(\cdot,u),(\cdot,v)$, which is $\Pi^{\perp}$; expresses $u,v$ in that basis with integer coordinates $C$; and exhibits a complement $R$ with $\det(C;R) = \pm1$. That determinant is the certificate that $R$ together with $u,v$ is a basis of $\Pi^{\perp}$, so $G_0 = R\,G_{\Pi^{\perp}}\,R^{\mathsf T}$ is the Gram matrix of $L_0$ and not of a finite-index sublattice. The run records $\det G_0 = 64$.

The sixteen vectors of square $-2$ are then found exhaustively and without a short-vector library call: with $A = -G_0$ positive definite and $A = L\,D\,L^{\mathsf T}$ its exact rational $LDL^{\mathsf T}$ decomposition (the run checks $L\,D\,L^{\mathsf T} = A$), one has $x^{\mathsf T}Ax = \sum_k D_k\bigl(\sum_{j\ge k}L_{jk}x_j\bigr)^2$, the $k$-th summand depends only on $x_k,\dots,x_7$, and the enumeration runs from $x_7$ down to $x_0$ pruning on the exact rational partial sum against $2$. Every branch is decided by exact rational comparisons, and the run reports $16$ in each case.

$2$. For each of the sixteen classes the run lifts the class to an integral $\alpha$ with $\alpha\perp\Pi$ and $\alpha^2 = -2$, and solves the congruence $(\alpha,z) = 1$ over $z\in\Pi^{\perp}$ by extended gcd on the coefficients of a basis of $\Pi^{\perp}$; the solution is verified, not searched. It reports $\mathrm{div} = 1$ for all sixteen classes of all five planes.

$3$ is @lem:divisibility-decides-one-cusp(2) applied to the sixteen classes. The sixteen classes are distinct in $L_0$, and the class of a lift is $\Stab_{\gent}(\Pi)$-invariant, so distinct classes give distinct orbits; hence exactly $16$.
:::

## The fibre over Sterk's cusp $2$: the smallest case

At Sterk's cusp $2$ the stabilizer is the whole orthogonal group of the cusp lattice, so the fibre is decided without any information about the other cusps. Cusp $1$ is the other extreme: it carries no $(-2)$-vector at all.

::: {.proposition #prop:fibre-cusp-one-empty title="The fibre over Sterk's cusp $1$ is empty"}
At Sterk's cusp $1$, with representative $e_1 = e$, one has $K_1 = e_1^{\perp\ten}/\ZZ e_1\cong U(2)\oplus E_8(2)$, every vector of which has square divisible by $4$. In particular $K_1$ contains no $(-2)$-vector, and the fibre of $\Phi_0$ over Sterk's cusp $1$ is empty.
:::

::: {.proof}
$e^{\perp\ten} = \generators{e}\oplus U(2)\oplus E_8(2)$, so $K_1\cong U(2)\oplus E_8(2)$; this is [@Ste91, 4.3.4], whose statement is $e^{\perp}/\ZZ e\cong\mathbf H(2)\oplus E_8(-2)$. Both summands are twice an even lattice, so every square in $K_1$ lies in $4\ZZ$, and $-2\notin4\ZZ$.
:::

::: {.theorem #thm:ou-e8-transitive title="$\Orth(U\oplus E_8(2))$ is transitive on the $(-2)$-vectors"}
Let $K = U\oplus E_8(2)$. Then $\Orth(K)$ acts transitively on $\{x\in K : x^2 = -2\}$.
:::

::: {.proof}
By [@Ste91, 4.3.6], $K$ is the cusp lattice $K_2 = (e')^{\perp\ten}/\ZZ e'$ of Sterk's cusp $2$, and $\Orth(K) = \{\pm1\}\cdot W_{e'}$, where $W_{e'}$ is the subgroup generated by the reflections of $\Orth(K)$.

*A fundamental chamber of $W_{e'}$.* Take the chamber certified by the complete Vinberg search of `computations/reports/coble_TEn-chambers-run.txt`, section `K(L_2)`, which lists in the basis $e,f,\alpha_1,\dots,\alpha_8$ of $K$ the ten walls
$$
\alpha_1,\dots,\alpha_8,\qquad -e+f,\qquad \bar\alpha_8-2f,
$$
where $\bar\alpha_8 \definedas -(2\alpha_1+3\alpha_2+4\alpha_3+6\alpha_4+5\alpha_5+4\alpha_6+3\alpha_7+2\alpha_8)$ is Sterk's doubled fundamental weight, of square $-4$ and with $\bar\alpha_8\cdot\alpha_8 = 2$; there the wall Gram matrix has diagonal $(-4,\dots,-4,-2,-4)$ and off-diagonal entries $0$ and $2$, so the dihedral angles are $\pi/2$, $\pi/3$ or $\pi/4$, all submultiples of $\pi$. That the search is complete --- that these ten walls bound a chamber and not a proper sub-polytope --- is the line `unrestricted certified search on this cusp: complete=True walls=10 ideal=2 finite=8` of `computations/reports/coble_sterk-reflection-subgroups-run.txt`. Sterk's printed ten roots at cusp $2$ are the same list except for the tenth wall, which he prints as $\alpha_9 = \bar\alpha_8+2f = -\omega_8+2f$ [@Ste91, 4.3.6], $\bar\alpha_8$ being the doubled fundamental weight $2\omega_8$: the record's `his walls among the walls of the certified chamber: 9 of 10 (his walls not among them: labels [9])` compares wall vectors, and $-\omega_8+2f$ and $-2f-\omega_8$ differ by $4f$. The argument below uses the certified chamber, and does not rely on the printed one.

By Vinberg's theorem [@Vin85, §1, no. 1], a Coxeter polytope $P$ is a fundamental polytope for the group generated by the reflections in its walls, the polytopes $\gamma P$, $\gamma\in W_{e'}$, tessellate the hyperbolic space $\mathbf H$ attached to $K$, and every mirror of a reflection of $W_{e'}$ is a wall of that tessellation.

*Every $(-2)$-vector is a wall translate.* Let $x\in K$ with $x^2 = -2$ and let $s_x$ be the reflection in $x$. Since $s_x\in\Orth(K) = \{\pm1\}W_{e'}$ and $\pm1$ acts trivially on $\mathbf H$, the isometry of $\mathbf H$ induced by $s_x$ lies in the image of $W_{e'}$; it is the reflection of $\mathbf H$ with fixed hyperplane $x^{\perp}\cap\mathbf H$. By Vinberg's theorem that hyperplane is a wall of the tessellation, so $x^{\perp} = w(r_i^{\perp})$ for some $w\in W_{e'}$ and some $i\in\{1,\dots,10\}$, that is $x = \pm w(r_i)$, $r_i$ being the $i$-th wall root. Of the ten wall roots only $-e+f$ has square $-2$; the other nine have square $-4$. Hence every $(-2)$-vector of $K$ lies in the $W_{e'}$-orbit of $\pm(e-f)$, and $\Orth(K)$ is transitive.
:::

::: {.proposition #prop:isometry-k-roots title="An explicit isometry of $U\oplus E_8(2)$ carrying $e-f$ to $e+f+\alpha_1$"}
In the basis $e,f,\alpha_1,\dots,\alpha_8$ of $K=U\oplus E_8(2)$ with Gram matrix $G = \begin{pmatrix}0&1\\1&0\end{pmatrix}\oplus(-2)C(E_8)$ the matrix
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
satisfies $N^{\mathsf T}GN = G$, $\det N = -1$ and $N(e-f) = e+f+\alpha_1$. Hence $e-f$ and $e+f+\alpha_1$ lie in one $\Orth(K)$-orbit, and the two orbits of @thm:ou-e8-transitive cannot be separated by the invariants that separate these two vectors.
:::

::: {.proof}
The products $N^{\mathsf T}GN$ and $N(e-f)$ are computed in exact integer arithmetic in `computations/reports/coble_789-transvection-and-isometry.py`, whose transcript `-run.txt` prints `N^T G_K N = G_K: True`, `det N = -1` and `N(e-f) = e+f+a_1: True`. The computation serves @thm:ou-e8-transitive as a certificate for this one pair, not as its proof; the proof of transitivity is the chamber argument there.
:::

::: {.lemma #lem:ze-translates-in-gent title="The $\ZZ e'$-translates of $\delta$ are realised by $\gent$"}
Let $E\colon\ten\to\ten$ be the Eichler transvection
$$
E(x) \definedas x+(x,e')\,e-(x,e)\,e' .
$$
Then $E\in\gent$, $E(e') = e'$, $E(\delta) = \delta+e'$ and $E^k(\delta) = \delta+k e'$ for every $k\in\ZZ$.
:::

::: {.proof}
*Integrality.* On the basis $e,f,e',f',\alpha_1,\dots,\alpha_8$ of $\ten$ one has $E(e) = e$, $E(f) = f-e'$, $E(e') = e'$, $E(f') = f'+2e$ and $E(\alpha_i) = \alpha_i$, all integral. This is the case $\eta = e'$, $a = e$ of the Eichler transformation of [@GHS08, §3.1, Lemma 3.1 and the integrality assertion after (10)], as quoted in @lem:cusp-root-lift-independence; the computation is `computations/reports/coble_789-transvection-and-isometry.py`.

*Isometry.* Expanding $(E x,E y)$ for $x,y\in\ten$ with $e^2 = (e')^2 = e\cdot e' = 0$ (the sum $U\oplus U(2)\oplus E_8(2)$ is orthogonal, so $e$ and $e'$ are perpendicular), the correction terms cancel in pairs: $(Ex,Ey)-(x,y) = (x,e)(y,e')-(y,e)(x,e')+(x,e')(e,y)-(x,e)(e',y)$, and this vanishes because $(e,y) = (y,e)$ and $(e',y) = (y,e')$.

*The translates.* $(\delta,e') = 0$ and $(\delta,e) = -1$, so $E(\delta) = \delta+e'$; $E$ is linear and fixes $e'$, so $E^k(\delta) = \delta+k e'$ for $k\geq 0$, and $E^{-1}$ gives the negative multiples.

*Membership in $\gent$.* For $y$ in the dual lattice $\ten^\vee = U\oplus\tfrac12U(2)\oplus\tfrac12E_8(2)$ one has $E(y)-y = (y,e')e-(y,e)e'$, and both pairings are integers: $(y,e')$ because the $U(2)$-component of $y$ is half-integral and pairs integrally with $e'$, and $(y,e)$ because the $U$-component is integral and the other summands are orthogonal to $e$. Hence $E(y)-y\in\ten$ and $E$ acts trivially on $A_{\ten} = \ten^\vee/\ten$. So $E\in\ker\rho_{\ten}\subseteq\gent$, the last inclusion because $\gent = \rho^{-1}(M)$ is the preimage of the summand-preserving subgroup of $\Orth(A_{\ten},q)$ [@AEGS25, Def. 2.6; @Ste91, Prop. 2.7].
:::

::: {.corollary #cor:fibre-cusp-two title="The fibre over Sterk's cusp $2$ is a single point"}
The fibre of $\Phi_0$ over Sterk's cusp $2$ is a single point, represented by the pair $(\ZZ e',\,\delta)$: by the $(-2)$-vector $\delta = e-f$ of $\ten$, and by the primitive isotropic line $\ZZ e'$ of $T_\Co$ that the pair carries. (The vector $\delta$ itself is not a vector of $T_\Co$: $\delta^2 = -2\neq0$.)
:::

::: {.proof}
By @thm:b2-zero-cusps(2) the fibre is the set of $\Stab_{\gent}(e')$-orbits of $(-2)$-vectors $\alpha\perp e'$. Let $\alpha$ be one, and let $\bar\alpha$ be its image in $K_2 = (e')^{\perp\ten}/\ZZ e'$. The image of $\Stab_{\gent}(e')$ in $\Orth(K_2)$ is all of $\Orth(K_2)$ [@Ste91, 4.3.6], and $\Orth(K_2)$ is transitive on the $(-2)$-vectors of $K_2$ (@thm:ou-e8-transitive), so some $g\in\Stab_{\gent}(e')$ has $g\bar\alpha = \bar\delta$, that is $g\alpha = \delta+k e'$ for some $k\in\ZZ$. By @lem:ze-translates-in-gent the transvection $E$ lies in $\Stab_{\gent}(e')$ and $E^{-k}(g\alpha) = \delta$. Hence every $(-2)$-vector perpendicular to $e'$ is $\Stab_{\gent}(e')$-equivalent to $\delta$, and the fibre is a single point.
:::

## The other fibres, and the four $0$-cusps

::: {.proposition #prop:fibres-three-four-five title="The fibres over Sterk's cusps $3$, $4$ and $5$ are nonempty"}
At Sterk's cusps $3$, $4$ and $5$ the cusp lattice is $K_k\cong U\oplus E_8(2)$ as well [@Ste91, 4.3.4], and each carries a $(-2)$-vector perpendicular to its representative, as follows; the vectors are the white nodes of [@AEGS25, Figs.~7--8], and the coordinates are those of the record `computations/reports/coble_enriques-white-root-facets-run.txt` in the basis $(e,f,e',f',\alpha_1,\dots,\alpha_8)$ of $\ten$.
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
The subgroup $R$ has exactly four orbits on the primitive isotropic lines of $T_\Co$, of discriminant-class sizes $2$, $135$, $270$ and $120$. Hence $D(T_\Co)/R$ has exactly four $0$-cusps.
:::

::: {.proof}
Every primitive vector of $T_\Co$ has divisibility $2$ (@lem:divisibilityAlwaysTwoTco), so $v\mapsto[v/2]$ maps the primitive isotropic vectors of $T_\Co$ to the $527$ nonzero isotropic classes of $A_{T_\Co}$, and the map is a bijection from the $\ker\bar\rho$-orbits of primitive isotropic vectors onto those classes [@thm:coble-zero-cusp-count(1)]. For a subgroup $\Gamma$ with $\ker\bar\rho\subseteq\Gamma\subseteq\Orth(T_\Co)$ the $\Gamma$-orbits on primitive isotropic vectors correspond to the $\bar\rho(\Gamma)$-orbits on the classes, because the fibre over a class is a single $\ker\bar\rho$-orbit [@thm:coble-zero-cusp-count, proof, paragraph "Intermediate groups"]. Here $R = \bar\rho^{-1}(P)$ [@prop:gamma-co-images(3)], so $\bar\rho(R) = P$, and $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ has exactly four orbits on the $527$ nonzero isotropic classes, of sizes $2$, $135$, $270$ and $120$ [@prop:coble-cong-point-stabilizer(2)]. A count of $0$-cusps names its group [@def:gamma-co-groups], and this is the count for $R$.
:::

::: {.theorem #thm:orbit-per-cusp title="Which $R$-orbit lies over which Sterk cusp"}
Let $\eta_2 = e'$, $\eta_3 = e'+f'+y_3$, $\eta_4 = 2e'+f'+y_4$, $\eta_5 = 2h+y_4$ with $h = e+f$, $y_3$ of square $-4$ and $y_4$ of square $-8$ be Sterk's representatives of his cusps $2$, $3$, $4$, $5$ [@Ste91, (4.2.3)], and put $[\eta_k]\definedas[\eta_k/2]\in A_{T_\Co}$. Then $[\eta_k]$ lies in the $P$-orbit of @prop:coble-cong-point-stabilizer(2) of size
$$
\begin{array}{c|cccc}
k & 2 & 3 & 4 & 5\\ \hline
\text{size of the }P\text{-orbit of }[\eta_k] & 2 & 120 & 270 & 135
\end{array}
$$
Because $v\mapsto[v/2]$ is a bijection from the $R$-orbits on primitive isotropic lines of $T_\Co$ onto the $P$-orbits on the $527$ nonzero isotropic classes [@thm:coble-zero-cusp-count(1), with $\bar\rho(R) = P$ by @prop:gamma-co-images(3)], the $R$-orbit lying over Sterk's cusp $k$ is the orbit of $[\eta_k]$, and the four $R$-orbits of @thm:four-r-orbits are exactly the four cusps' orbits.
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
the last line because $\eta_5/2 = h+y_4/2$ and $h\in T_\Co$. Each total $q$ is $0$ modulo $2\ZZ$, as it must be for an isotropic vector. The three nonzero classes of $A_{U(2)}$ are $u_1,u_2,u_3$ with $q$-values $0,0,1$, and the $E_8(2)$-classes of value $0$ and $1$ are the sets $E_0$ of size $135$ and $E_1$ of size $120$ [@prop:coble-cong-point-stabilizer(2), proof]. So $[\eta_2] = (u_1\text{ or }u_2,\,0)$ lies in $\{u_1,u_2\}$ of size $2$; $[\eta_3] = (u_3,\,E_1)$ in the orbit of size $120$; $[\eta_4] = (u_1\text{ or }u_2,\,E_0)$ in the orbit of size $270$; and $[\eta_5] = (0,\,E_0)$ in the orbit of size $135$. The computation is `computations/reports/coble_789-cusp-classes.py`, whose transcript `-run.txt` prints, for each $k$, the components and the orbit.
:::

::: {.theorem #thm:cusp-fibres-four title="The $0$-cusps of $D(T_\Co)/R$ lie one over each of Sterk's cusps $2,3,4,5$"}
The map $\Phi_0$ of @thm:b2-zero-cusps has empty fibre over Sterk's cusp $1$ (@prop:fibre-cusp-one-empty) and exactly one point over each of Sterk's cusps $2$, $3$, $4$, $5$. Hence the four $0$-cusps of $D(T_\Co)/R$ are in bijection with Sterk's cusps $2,3,4,5$, one over each.
:::

::: {.proof}
The fibres of $\Phi_0$ partition the $0$-cusps of $D(T_\Co)/R$: $\Phi_0$ is well defined by @thm:b2-zero-cusps(1), and the cusp set of $F_{\En,2}$ is the disjoint union of the five orbits of Sterk's representatives. The fibre over cusp $1$ is empty (@prop:fibre-cusp-one-empty). For $k = 2,3,4,5$ the representative $\eta_k$ is a primitive isotropic vector of $T_\Co$, so its $R$-orbit is a $0$-cusp of $D(T_\Co)/R$ lying over cusp $k$; by @thm:orbit-per-cusp the four classes $[\eta_k]$ lie in four distinct $P$-orbits, hence the four $R$-orbits are distinct, and by @thm:four-r-orbits there are exactly four of them. So each of the four fibres over $2,3,4,5$ contains exactly one of the four $R$-orbits.
:::

::: {.theorem #thm:cusp-diagram-tco title="The cusp diagram of $D(T_\Co)/R$"}
1. *$0$-cusps.* There are four, written $0_2$, $0_3$, $0_4$, $0_5$, lying one over each of Sterk's $0$-cusps $2$, $3$, $4$, $5$, and none over cusp $1$ (@thm:cusp-fibres-four).
2. *$1$-cusps.* A $1$-cusp of $D(T_\Co)/R$ lies over exactly one of Sterk's nine $1$-cusps, whose type is a subset $T\subset\{1,2,3,4,5\}$ [@AEGS25, Not. 3.1]. There are none over the four types $\{1,2\}$, $\{1,3\}$, $\{1,4\}$, $\{1,5\}$ (@lem:one-cusp-over-cusp-one-empty), and exactly $16$ over each of the five types $\{2,4,5\}$, $\{4,5\}$, $\{3,5\}$, $\{3,4\}$, $\{5,5\}$ (@lem:five-one-cusps-nonempty); $80$ in all.
3. *Incidence.* For $k\in\{2,3,4,5\}$ the $0$-cusp $0_k$ lies in the closure of a $1$-cusp over $T$ exactly when $k\in T$. Hence $0_2$ is incident to the $16$ $1$-cusps over $\{2,4,5\}$; $0_3$ to the $32$ over $\{3,5\}$ and $\{3,4\}$; $0_4$ to the $48$ over $\{2,4,5\}$, $\{4,5\}$ and $\{3,4\}$; and $0_5$ to the $64$ over $\{2,4,5\}$, $\{4,5\}$, $\{3,5\}$ and $\{5,5\}$. There are $160$ incidence edges.
:::

::: {.proof}
$1$ is @thm:cusp-fibres-four, and $2$ is @thm:b2-one-cusps with @lem:one-cusp-over-cusp-one-empty and @lem:five-one-cusps-nonempty.

*Necessity in $3$.* The Baily--Borel incidence is containment of boundary components: a $0$-cusp $[\ell]$ lies in the closure of a $1$-cusp $[\Pi]$ exactly when some representatives satisfy $\ell\subset\Pi$ [@AEGS25, Def. 2.9 and §3.1], and the type of $[\Pi]$ is by definition [@AEGS25, Not. 3.1] the set of labels of the $0$-cusps in its closure. If $[\ell]_R$ is incident to $[\Pi]_R$, the forgetful maps of @thm:b2-zero-cusps and @thm:b2-one-cusps carry the inclusion to $\ell\subset\Pi$ in $\ten$, so the label $k$ of $[\ell]_{\gent}$ lies in $T$. Since $0_k$ exists only for $k\neq1$, this excludes cusp $1$.

*Sufficiency in $3$.* Let $\Pi'$ be a primitive isotropic plane of $T_\Co$ representing a $1$-cusp of $D(T_\Co)/R$ over $T$, and let $k\in T$ with $k\neq1$. By [@AEGS25, Not. 3.1] the label $k$ is the label of some primitive isotropic line $\ell\subset\Pi$ of $\ten$; conjugating by an element of $\gent$ gives $\ell\subset\Pi'$, and $\ell\subset T_\Co$ because $\Pi'\subset T_\Co$. So the $R$-orbit of $\ell$ is a $0$-cusp of $D(T_\Co)/R$ over $k$, hence is $0_k$ by @thm:cusp-fibres-four, and it is incident to $[\Pi']_R$ because $\ell\subset\Pi'$.

*The edge count.* The types containing $k$ are those listed, each carrying $16$ $1$-cusps by $2$; summing over $k$ gives $16(3+2+2+2+1) = 160$.
:::

::: {.remark #rmk:certified-versus-printed-chamber title="The certified cusp-$2$ chamber and Sterk's printed roots"}
The ten walls of the certified chamber of @thm:ou-e8-transitive are $\alpha_1,\dots,\alpha_8$, $-e+f$ and $\bar\alpha_8-2f$ in the coordinates of `computations/reports/coble_TEn-chambers-run.txt`. Sterk prints the last of them as $\alpha_9 = \bar\alpha_8+2f$ [@Ste91, 4.3.6], a different vector: the two differ by $4f$, and the record `computations/reports/coble_sterk-reflection-subgroups-run.txt` reports that nine of his ten printed roots are walls of the certified chamber. The count of $(-2)$-walls is one in both cases, since $-2f-\omega_8$ has square $-4$; what the printed set cannot be used for is the chamber-translate principle, which needs a fundamental chamber and is therefore applied above to the certified one. The identification of Sterk's ten printed roots with the white nodes of [@AEGS25, Figs.~7--8] is unaffected: it concerns the simple $(-2)$- and $(-4)$-roots at each cusp, and the white node at cusp $2$ is $e-f$ in both lists.
:::

::: {.remark #rmk:cusp-fibre-what-remains title="Which input decides which fibre"}
The fibre over Sterk's $0$-cusp $2$ is decided directly: the image of $\Stab_{\gent}(e')$ is the full orthogonal group of the cusp lattice [@Ste91, 4.3.6], that group is transitive on the $(-2)$-vectors (@thm:ou-e8-transitive), and the $\ZZ e'$-translates are absorbed by the transvections of @lem:ze-translates-in-gent. At Sterk's $0$-cusps $3$, $4$, $5$ the same argument does not apply, because the stabilizer image is the group generated by the printed reflections and the symmetries of their diagram, $\{\pm1\}W_k\rtimes S_k$ [@Ste91, 4.3.7--4.3.9], and $W_k$ is a proper subgroup of $W(K_k)$ of index $240$, $270$, $34\,560$ (@thm:sterk-reflection-subgroup-index); what decides those three fibres is the count of four $R$-orbits (@thm:four-r-orbits) together with @prop:fibres-three-four-five. The five $1$-cusp fibres are decided by @lem:five-one-cusps-nonempty, whose input is the explicit transvection computation of `computations/reports/coble_789-one-cusp-fibres.py` rather than any statement about the cusp stabilizer images.
:::
