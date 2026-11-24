# Marked Coble covers and the period map {#sec-marked-coble-period}

A marked Coble cover is a Coble cover together with a marking of its $K3$ double cover, and its period is a point of the period domain $\bD(T_\Co)$ of @def:gamma-co-groups (@rmk:marked-coble-covers-after-huybrechts).
The question settled here is whether the period determines such a cover up to an isomorphism compatible with the involution and the marking (research#800), and it does not: @prop:marked-coble-period-not-injective exhibits two marked covers on one cover, with equal periods and with markings that differ on one of the eleven classes of [@DK13, §3], that no isomorphism identifies.
research#802 asks for the same thing as an equivalence between the marked Coble covers and the period domain minus the $(-2)$-arrangement, and @prop:phi-marked-is-not-the-period-domain decides it: the period map there is essentially surjective and faithful and not full, so the equivalence fails; @rmk:phi-marked-what-is-decided states the exact form decided.

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

Write $\mcM^{\varphi}_\Co$ for the groupoid whose objects are the marked Coble covers of @def:marked-coble-cover(1) and whose morphisms are the isomorphisms of @def:marked-coble-cover(4). research#802 asks for this object to be the period domain minus the $(-2)$-arrangement. What the two computations below give is the isotropy of $\mcM^{\varphi}_\Co$ and the interaction of the marking with the involution and the period, and with them the decision of that statement.

::: {.lemma #lem:phi-marked-objects-and-automorphisms title="A $\varphi$-marked Coble cover: the involution is determined by the marking, and every object is rigid"}

Let $(X,\iota,\varphi)$ be a marked Coble cover of @def:marked-coble-cover(1) and let
$$\Gamma_\rho\definedas\theset{\gamma\in\Orth(\lkt)\mid\gamma\rho\gamma^{-1}=\rho}$$
be the centraliser of $\rho$ in $\Orth(\lkt)$. Then:

1. *The involution is determined by the marking.* $\iota^*=\varphi^{-1}\circ\rho\circ\varphi$, and this is the only involution of $X$ with that action on $H^2(X,\bZ)$: if $\iota_1^*=\iota_2^*$ then $(\iota_2^{-1}\iota_1)^*=\id$, so $\iota_2^{-1}\iota_1=\id$ [@PS24, Lemma 19.2.4].
2. *The involution is not an automorphism of the marked object.* $\iota$ is a nontrivial automorphism of $X$, and it fails the marking condition of @def:marked-coble-cover(4): $\varphi\circ\iota^*=\rho\circ\varphi\neq\varphi$, since $\rho=-\id$ on $T_\Co$ and $T_\Co\neq0$. So the isotropy of a $\varphi$-marked object does not contain $\iota$, in contrast with that of a labelled object, whose isotropy contains $\theset{\id,\iota}$ (@rmk:coble-labelled-versus-unlabelled(1)).
3. *Rigidity.* $\Aut(X,\iota,\varphi)=\theset{\id}$: an automorphism $f$ with $\varphi\circ f^*=\varphi$ has $f^*=\id$ because $\varphi$ is an isomorphism, and then $f=\id$ [@PS24, Lemma 19.2.4]. Two isomorphisms between the same pair of objects coincide whenever both exist, $g^{-1}f$ being an automorphism of the source. So $\mcM^{\varphi}_\Co$ is a discrete groupoid: every set of morphisms between two objects is empty or a singleton.
4. *The markings of one cover, and the period.* For a fixed $(X,\iota)$ the markings $\varphi$ with $\varphi\iota^*\varphi^{-1}=\rho$ form a torsor under $\Gamma_\rho$, acting by $\varphi\mapsto\gamma\circ\varphi$. Since $\rho$ is $+\id$ on $S_\Co$ and $-\id$ on $T_\Co$, an element of $\Gamma_\rho$ preserves each summand, $\gamma=\gamma_S\perp\gamma_T$, and the pairs occurring are those with $\gamma_T\circ\gamma_\Co=\gamma_\Co\circ\gamma_S$ for the gluing isometry $\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co}$ of the paragraph above. The period of $\gamma\circ\varphi$ is
$$\qty(\gamma\circ\varphi)_\bC\qty(H^{2,0}(X))=\gamma_{\bC}\qty(\pi)=\gamma_{T,\bC}(\pi),\qquad \pi\definedas\varphi_\bC\qty(H^{2,0}(X)),$$
because $\pi\subseteq T_\Co\tensor\bC$: $\iota$ is nonsymplectic, so $\iota^*\omega=-\omega$ for a holomorphic $2$-form, and $-\omega$ lies in the $(-1)$-eigenspace of $\iota^*$, which $\varphi_\bC$ carries to the $(-1)$-eigenspace of $\rho$ (@def:marked-coble-cover(1)). So the period depends on the marking only through $\gamma_T$, and two markings of one surface $(X,\iota)$ have the same period exactly when they differ by an element of $\Gamma_\rho$ whose $T_\Co$-component lies in $\Stab_{\Orth(T_\Co)}(\pi)$, a finite group (@lem:period-stabiliser-finite).
:::

::: {.proof}

1. is the defining equation of @def:marked-coble-cover(1) read for $\iota^*$, and the uniqueness the cited injection.
2. is $\varphi\circ\iota^*\circ\varphi^{-1}=\rho$ rearranged, with $\rho\neq\id$ on $T_\Co$ by @prop:coble-period-domain(2).
3. is the computation displayed, with the injection $g\mapsto g^*$ of [@PS24, Lemma 19.2.4] applied twice: once to $f$ and once to a quotient $g^{-1}f$ of two isomorphisms with the same source.
4. $(\gamma\circ\varphi)\iota^*(\gamma\circ\varphi)^{-1}=\gamma\rho\gamma^{-1}=\rho$ shows that $\Gamma_\rho$ acts on markings, and $\gamma\circ\varphi=\varphi$ gives $\gamma=\id$, so the action is free; for two markings of one $(X,\iota)$ the element $\gamma=\varphi'\circ\varphi^{-1}$ satisfies $\gamma\rho\gamma^{-1}=\rho$, so the action is transitive. The projection $\gamma\mapsto(\gamma_S,\gamma_T)$ is injective because $\gamma$ preserves each eigenspace lattice of $\rho$ and $S_\Co\oplus T_\Co$ spans $\lkt$ rationally; an isometry of $\lkt$ preserving both summands is the same thing as a pair of isometries of $S_\Co$ and $T_\Co$ preserving the gluing subgroup $h$ of @def:gluing-datum-of-a-pair, which is the graph of an isometry $A_{S_\Co}\iso A_{T_\Co}(-1)$ — the graph of $\gamma_\Co$ in the display above — that is the condition displayed. The period computation is $\gamma\circ\varphi$ applied to a holomorphic form, and $\gamma_\bC(\pi)=\gamma_{T,\bC}(\pi)$ because $\pi$ lies in the second summand. The last sentence is that computation together with $\Stab_{\Orth(T_\Co)}(\pi)$ being finite (@lem:period-stabiliser-finite, whose hypothesis holds at the signature $(2,9)$ of $T_\Co$, @prop:coble-period-domain(2)) intersected with the image of $\Gamma_\rho$.

:::

::: {.proposition #prop:phi-marked-is-not-the-period-domain title="The period map of the $\varphi$-marked Coble covers is essentially surjective and faithful, and not full: it is not an equivalence onto the period domain"}

Let $\bD\definedas\bD(T_\Co)^+$, let $Z$ be the $(-2)$-arrangement of @prop:the-coble-locus-in-the-period-domain and $U\definedas\bD\sm Z$, and let
$$\mathcal P_\Co\colon\mcM^{\varphi}_\Co\too U,\qquad (X,\iota,\varphi)\longmapsto\varphi_\bC\qty(H^{2,0}(X)),$$
be the period map of @def:marked-coble-cover(3). Then:

1. *It is essentially surjective.* For $\pi\in U$ there are $X$, an isometry $\varphi\colon H^2(X,\bZ)\isoto\lkt$ with $\varphi_\bC\qty(H^{2,0}(X))=\pi$, and an involution $\iota$ with $\iota^*=\varphi^{-1}\rho\varphi$ whose fixed locus is one smooth rational curve and whose quotient is a Coble surface of @def:coble-moduli-functor (@thm:coble-period-surjectivity). So $(X,\iota,\varphi)$ is an object of $\mcM^{\varphi}_\Co$ with period $\pi$.
2. *It is faithful.* Both sides have at most one morphism between two objects: on the target $U$ is a set, and on the source this is @lem:phi-marked-objects-and-automorphisms(3).
3. *It is not full.* By @prop:marked-coble-period-not-injective there are two objects with the same period and no isomorphism between them, while the target has the identity of that period as its only endomorphism.
4. *Consequently it is not an equivalence, and research#802's marked clause is refuted in the form the volume can state it:* a marked Coble cover is **not** determined up to isomorphism by its period, and the period map is not an equivalence onto the period domain minus the arrangement. The counterexample is the pair of @prop:marked-coble-period-not-injective; in the notation of @lem:phi-marked-objects-and-automorphisms(4) its two markings differ by $s_{\varphi([E_0])}\perp\id_{T_\Co}\in\Gamma_\rho$, whose $T_\Co$-component is the identity, so the two lie in one $\Gamma_\rho$-orbit and have the same period, and no isomorphism exists.
:::

::: {.proof}

1. is @thm:coble-period-surjectivity with $\sigma=\rho$ (@def:marked-coble-cover(1)), its clauses (1)--(3) being exactly the remaining conditions of @def:marked-coble-cover(1) on the quotient, and $\varphi_\CC\qty(H^{2,0}(X))=\pi$ the definition of the period.
2. is @lem:phi-marked-objects-and-automorphisms(3) on the source and the discreteness of a set on the target.
3. is @prop:marked-coble-period-not-injective: its two objects have equal periods by its own display, and are not isomorphic in the sense of @def:marked-coble-cover(4), which is the notion of morphism of the source; a functor that is an equivalence is full, and fullness at that pair would produce such an isomorphism.
4. An equivalence is full, faithful and essentially surjective; (1)--(3) give the first two and deny the third.

:::

::: {.remark #rmk:phi-marked-what-is-decided title="The exact statement decided about the $\varphi$-marked covers, and the neighbouring ones that are not decided"}

1. *Decided.* The statement is: the period map $\mathcal P_\Co\colon\mcM^{\varphi}_\Co\to\bD(T_\Co)^+\sm Z$ is an equivalence, that is, every period off $Z$ occurs and a marked Coble cover is determined up to isomorphism by its period. It is false: it is essentially surjective and faithful, and not full (@prop:phi-marked-is-not-the-period-domain).
   The period lands in the full period domain $\Omega$ of both components (@thm:coble-period-surjectivity(5)), of which $\bD(T_\Co)^+$ is one; the counterexample's two objects have one and the same period point, so the choice of component does not enter the refutation.
2. *No weaker reading is at stake.* A groupoid whose automorphism groups are all trivial is equivalent to its set of isomorphism classes, the inclusion of a skeleton being an equivalence, so an equivalence of bare groupoids between $\mcM^{\varphi}_\Co$ and the points of $U$ would assert only that two sets have the same cardinality, and a set-theoretic comparison of the period locus is not the statement research#802 makes. The content of that statement is the period, and it is decided in (1). A version in families would need marked Coble covers over a base, which @def:marked-coble-cover does not define, and nothing here decides such a version.
3. *What the counterexample shows to be missing.* @rmk:marked-coble-period-scope(1)--(2) records which datum the period cannot see — the class in $S_\Co$, on which $\iota$ acts trivially — and that the two marked covers of the counterexample do not carry the same chamber. Whether equal period together with equal chamber forces an isomorphism is a different statement, and it is not decided here.
4. *What is not used and not claimed.* The eleven-class-labelled stack $\mcM^{\mathrm{lab}}_\Co$ is a different object, whose isotropy contains $\theset{\id,\iota}$ at every object where a $\varphi$-marked object has isotropy $\theset{\id}$ (@lem:phi-marked-objects-and-automorphisms(2)--(3)); nothing here is inferred from it, and nothing here is inferred from the unmarked statement @prop:no-identification-with-the-period-domain(3), nor does either imply the other.
:::
