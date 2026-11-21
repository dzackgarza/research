# Marked Coble covers and the period map {#sec-marked-coble-period}

A marked Coble cover is a Coble cover together with a marking of its $K3$ double cover, and its period is a point of the period domain $\bD(T_\Co)$ of @def:gamma-co-groups (@rmk:marked-coble-covers-after-huybrechts).
The question settled here is whether the period determines such a cover up to an isomorphism compatible with the involution and the marking (research#800), and it does not: @prop:marked-coble-period-not-injective exhibits two marked covers on one cover, with equal periods and with markings that differ on one of the eleven classes of [@DK13, §3], that no isomorphism identifies.

::: {.definition #def:marked-coble-cover title="Marked Coble covers, their periods and their isomorphisms"}

1. A **marked Coble cover** is a triple $(X,\iota,\varphi)$ with $X$ a $K3$ surface, $\iota$ a nonsymplectic involution whose quotient is a Coble surface of @def:coble-moduli-functor, and $\varphi\colon H^2(X,\bZ)\isoto\lkt$ an isometry with
$$
\varphi\circ\iota^*\circ\varphi^{-1} = \rho,
$$
where $\rho\in\Orth(\lkt)$ is $+\id$ on $S_\Co = \generators{2}\oplus\generators{-2}^{\oplus10}$ and $-\id$ on $T_\Co$; this is the notion of @rmk:marked-coble-covers-after-huybrechts, whose $\rho$ is written $I_\Co$ below.
2. For the classical Coble cover of [@DK13, §3], that is for the double cover $X\to S$ of the blowup $S$ of $\PP^2$ at the ten nodes of an irreducible plane sextic branched along the proper transform of the sextic, the invariant lattice $H^2(X,\bZ)^\iota$ is $S_\Co$, spanned by the classes $e_0 = f^*H$ and $e_i = f^*E_i$ of the pullbacks of a line and of the $i$-th exceptional curve, and its orthogonal complement is $T_\Co$, with $\iota$ acting by $+\id$ on $S_\Co$ and by $-\id$ on $T_\Co$ (@prop:coble-cover-marking).
   The eleven classes are those of pairwise orthogonal divisors of squares $2,-2,\dots,-2$ [@DK13, §3], hence of type $(1,1)$; a holomorphic $2$-form is orthogonal to $H^{1,1}(X)$, so $H^{2,0}(X)\subseteq T_\Co\tensor_\bZ\bC$.
3. The **period** of $(X,\iota,\varphi)$ is the point $\varphi_\bC(H^{2,0}(X))$ of the period domain $\bD(T_\Co)$ of @def:type-iv-period-domain, the value of the period map $\mathcal P_\Co$ of @rmk:marked-coble-covers-after-huybrechts.
4. An **isomorphism** of marked Coble covers $(X,\iota,\varphi)\to(X',\iota',\varphi')$ is a biholomorphic map $f\colon X\to X'$ with $f\circ\iota\circ f^{-1} = \iota'$ and $\varphi\circ f^* = \varphi'$.

:::

By (2) and @prop:coble-cover-marking the lattice $S_\Co\perp T_\Co$ has finite index in $\lkt$, its gluing subgroup is the graph of the anti-isometry $\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co}$ with $q_{T_\Co}\circ\gamma_\Co = -q_{S_\Co}$, and both discriminant groups are $2$-elementary of order $2^{11}$ (@prop:theta-co-exists, @prop:coble-period-domain(2)).
An isometry of $S_\Co$ acting trivially on $A_{S_\Co}$ therefore extends to $\lkt$ as $+\id$ on $T_\Co$, and an isometry of $T_\Co$ acting trivially on $A_{T_\Co}$ extends as $+\id$ on $S_\Co$ (@thm:automorphism-lifting-criterion).
The first is how @prop:theta-co-exists produces $\theta_\Co$ from $-\id_{S_\Co}$, whose action on $A_{S_\Co}$ is trivial because that group is $2$-elementary; the same half is used below.

::: {.proposition #prop:marked-coble-period-not-injective title="The period does not determine a marked Coble cover"}

There are marked Coble covers $(X,\iota,\varphi)$ and $(X,\iota,\varphi')$ on one Coble cover, with
$$
\varphi'([E_0]) = -\varphi([E_0]),\qquad \varphi'([E_i]) = \varphi([E_i]) \quad (i = 1,\dots,10),
$$
and with $\varphi'_\bC(H^{2,0}(X)) = \varphi_\bC(H^{2,0}(X))$ as points of $\bD(T_\Co)$, that are not isomorphic in the sense of @def:marked-coble-cover(4).

:::

::: {.proof}

*The isometry.*
Let $(X,\iota,\varphi)$ be a marked Coble cover of the classical kind, @def:marked-coble-cover(2), and put $c\definedas\varphi([E_0])\in S_\Co$, a class of square $2$.
Let $s_c\in\Orth(S_\Co)$ be the reflection in $c$.
For $x\in S_\Co^\#$ one has $s_c(x) = x-(x,c)c$, and $(x,c)\in\bZ$, so $s_c(x)\in x+S_\Co$: the reflection acts trivially on $A_{S_\Co}$.
Hence $s_c\perp\id_{T_\Co}$ preserves the gluing subgroup, and it extends to an isometry $g\in\Orth(\lkt)$ with $\restrictionof{g}{S_\Co} = s_c$ and $\restrictionof{g}{T_\Co} = \id_{T_\Co}$ (@thm:automorphism-lifting-criterion).
The isometry $g$ preserves each of the two summands $S_\Co$ and $T_\Co$, so it commutes with $I_\Co$, which is $+\id$ on the first and $-\id$ on the second.

*The second marking.*
Put $\varphi'\definedas g\circ\varphi$.
It is an isometry $H^2(X,\bZ)\isoto\lkt$, and it conjugates $\iota^*$ to $g\circ I_\Co\circ g^{-1} = I_\Co$.
Its period is $\varphi'_\bC(\omega_X) = g_\bC(\varphi_\bC(\omega_X)) = \varphi_\bC(\omega_X)$ for a holomorphic $2$-form $\omega_X$, because $g$ is the identity on $T_\Co\tensor_\bZ\bC$ and $\varphi_\bC(\omega_X)$ lies there by @def:marked-coble-cover(2).
On the eleven classes, $\varphi'([E_0]) = s_c(c) = -c = -\varphi([E_0])$, while $\varphi'([E_i]) = \varphi([E_i])$ for $i\ge1$, because $(e_i,c) = 0$: the classes $e_0,\dots,e_{10}$ are pairwise orthogonal [@DK13, §3].
In particular $\varphi'\neq\varphi$.

*No isomorphism.*
Let $f\colon X\to X$ be biholomorphic with $f\circ\iota\circ f^{-1} = \iota$ and $\varphi\circ f^* = \varphi'$.
Then $\varphi\circ f^* = g\circ\varphi$, so $f^* = \varphi^{-1}\circ g\circ\varphi = G$, an involution of $H^2(X,\bZ)$ acting as the reflection in the class $[E_0]$ on $\varphi^{-1}(S_\Co)$ and as the identity on $\varphi^{-1}(T_\Co)$.
The class $[E_0]$ is that of the curve $E_0 = f^{-1}(\tilde L)$, where $\tilde L$ is the proper transform of a line meeting $C$ in six points away from its nodes [@DK13, §3]: the double cover restricted to $\tilde L\cong\PP^1$ is branched at the six points of $\tilde L\intersect\tilde C$, since $\tilde C\cdot H = 6$, so $E_0$ is a smooth connected curve of genus $2$, of square $2$.
Let $A$ be an ample class on $X$.
An ample class pairs positively with every curve of a smooth projective surface [@Huy16, Ch. 8, §1, Theorem 1.2], hence with every nonzero effective divisor, which is a sum of curves; applied to the ample class $f^*(A)$ this gives $f^*(A)\cdot[E_0]>0$.
On the other hand $f^*(A)\cdot[E_0] = A\cdot f_*([E_0]) = A\cdot G^{-1}([E_0]) = -A\cdot[E_0]<0$, since $G([E_0]) = -[E_0]$ and $G^{-1} = G$.
This is a contradiction, so no such $f$ exists.

:::

::: {.remark #rmk:marked-coble-period-scope title="Which datum the counterexample shows to be missing"}

1. The two marked covers differ by the reflection in $c = \varphi([E_0])$, which the period cannot see: $c$ lies in the invariant lattice $S_\Co$, on which $\iota$ acts trivially and on which the period therefore gives no information.
   The failure is the standard one for marked $K3$ surfaces, whose period map is generically and not globally injective [@Huy16, Ch. 7, §2, Prop. 2.2; Ch. 7, §5, Cor. 5.1]; what a Coble cover adds is the eleven classes, and the counterexample moves the class of $E_0$, the only one of the eleven of positive square.
2. It also keeps the chamber out of the marked datum: the reflection $s_c$ reverses the sign of the pairing with $c$, so it exchanges the two components of the positive cone of $\Pic(X)\tensor\RR$ and cannot preserve the chamber of $X$.
   The two marked covers therefore do not carry the same chamber, and whether marked Coble covers with equal periods and equal chambers of positive roots are isomorphic is a different statement, not decided here.

:::
