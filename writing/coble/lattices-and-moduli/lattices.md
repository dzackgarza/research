# Period domain embeddings and normalization {#sec-lattices}

::: {.notation title="The lattices of this chapter"}

$$
\begin{aligned}
    \lkt &= (22, 0, 0)_3 = U^3 \oplus E_8^2 = \latII_{3, 19} &
    E_{10} &= (10, 0, 0)_1 = U \oplus E_8 = \latII_{1, 9} \\
    S_\En &= \EnriquesInvariants_1 = E_{10}(2) &
    T_\En &= (12, 10, 0)_2 = U \oplus E_{10}(2) \\
    S_\Co &= (11, 11, 1)_1 = \generators{-2} \oplus E_{10}(2) &
    T_\Co &= (11,11,1)_2 = \generators{2} \oplus E_{10}(2) \\
    \sdp &= (2,2,0)_1 = U(2) &
    \tdp &= (20, 2, 0)_2 = U \oplus U(2) \oplus E_8^2
\end{aligned}
$$

:::

::: {.lemma #lem:primitive_embedding_eta}

Writing

$$
\begin{aligned}
T_\Co = \generators{2} \oplus E_{10}(2) &= \generators{h, e', f',\alpha_1,\cdots, \alpha_8} \\
T_\En = U \oplus E_{10}(2) &= \generators{\tilde e,\tilde f,\tilde e',\tilde f',\tilde \alpha_1,\cdots,\tilde \alpha_8},
\end{aligned}
$$

there is an embedding of lattices $T_\Co \injects T_\En$:

$$
\begin{aligned}
\eta: \generators{2} \oplus E_{10}(2) &\to U \oplus E_{10}(2) \\
(h, x) &\mapsto (\tilde e + \tilde f, x)
\end{aligned}
$$

which sends the basis vector $h$ of $\generators{2}$ to $\tilde e+\tilde f\in U$ and is the identity on the $E_{10}(2)$ summand.
Since $\coker \eta$ is torsionfree, $\eta$ is a primitive embedding.
:::

::: {.proof}

The map is well defined and isometric: $h$ has square $2$ and $\tilde e+\tilde f$ has square $2$, since $\tilde e,\tilde f$ are the isotropic basis of $U$ with $\tilde e\cdot\tilde f=1$; and $\eta$ is the identity on $E_{10}(2)$, which is an orthogonal summand of both sides.
So $\eta$ is a morphism of lattices of $\mathbf{Lat}_{\bZ}$, and it is injective because it is injective on each summand.

For primitivity, $\eta(T_{\Co})=\bZ(\tilde e+\tilde f)\oplus E_{10}(2)$, so
$$
T_\En/\eta(T_\Co)\;\cong\;U/\bZ(\tilde e+\tilde f).
$$
The homomorphism $U\to\bZ$, $a\tilde e+b\tilde f\mapsto a-b$, is surjective with kernel $\bZ(\tilde e+\tilde f)$, so $\coker\eta\cong\bZ$ is torsion-free, and $\eta$ is primitive by @prop:primitive-characterization.
:::

::: {.lemma #lem:sequence_of_embeddings}

There is a sequence of primitive embeddings

$$
T_{\Co} \injects \ten \injects \tdp \injects \lkt
$$

which is unique up to $\Orth(\lkt)$.
In particular, this yields an embedding

$$
\begin{aligned}
\generators{2} \oplus U(2) \oplus E_8(2) &\injects U \oplus U(2) \oplus E_8^2 \\
(h,x,y) & \mapsto (\tilde e + \tilde f, x, y, y)
\end{aligned}
$$

and thus an embedding $\fco \injects \fttz$.
The three matrices, in the standard basis of the marking of @thm:theta-co-coordinates, are @thm:chain-matrices.
:::

::: {.proof}

The displayed map is isometric on each summand: on $\generators{2}$ as in @lem:primitive_embedding_eta, on $U(2)$ as the identity, and on $E_8(2)$ because $(y,y)^2 = 2y^2$ in $E_8\oplus E_8$.
Its cokernel is $U/\bZ(\tilde e+\tilde f)\oplus(E_8\oplus E_8)/\theset{(y,y)}$.
The first summand is $\bZ$ by @lem:primitive_embedding_eta, and $(a,b)\mapsto a-b$ identifies the second with $E_8$.
The cokernel is torsion-free, so the map is primitive by @prop:primitive-characterization.
The embedding $\fco\injects\fttz$ is the one that @lem:locally_closed_embedding_BB induces.

For uniqueness, by [@AEGS25 Lem. 2.4, printed p. 586] it suffices to show uniqueness of $\sen \injects S_{\Co}$, i.e.

$$
E_{10}(2) \injects \generators{-2}\oplus E_{10}(2)
,
$$

or equivalently by untwisting,

$$
E_{10} \injects \generators{-1}\oplus E_{10}
.
$$

This embedding is unique because $E_{10} = U \oplus E_8$ is unimodular.
For a primitive embedding $\iota\colon E_{10}\injects L$, @prop:unimodular-splits gives $L\isoto E_{10}\perp E_{10}^{\perp L}$.
By @cons:embedding-gluing-data, its gluing datum is the graph of an isometry between a subgroup of $A_{E_{10}}$ and a subgroup of $A_{E_{10}^{\perp L}}$; since $A_{E_{10}}=0$, the datum is trivial and the embedding is determined by the isometry class of the complement.
Similarly, by [@Nik80 Cor. 1.5.2, printed p. 111, Thm. 3.6.3, printed p. 144], the homomorphism $\Orth(\lkt)\to \Orth(T_\Co)$ is surjective.
:::

::: {.lemma #lem:locally_closed_embedding_BB}

The embeddings of lattices $\eta: T_\Co\injects T_\En$ (resp. $T_{\Co} \injects \tdp$) induce locally closed embeddings $\fco \injects \fen$ (resp. $\fco \injects \fttz$) which extend to morphisms on the Baily--Borel compactifications.
:::

::: {.proof}

This follows from [@KK72 §5, Thm.2].
:::

::: {.definition #def:gamma-co-groups title="The groups of the Coble lattice"}
$T_\Co$ is the lattice $N$ of [@DK13, (3.6)], $N = \generators{2}\oplus E(2)$ with $E(2) = U(2)\oplus E_8(2)$; in the notation of @lem:primitive_embedding_eta it is $\generators{h}\oplus E_{10}(2)$. Let $\delta\definedas\tilde e-\tilde f$, a $(-2)$-vector of $T_\En$ with $\delta^{\perp T_\En} = \eta(T_\Co)$; then $T_\En = (T_\Co\perp\ZZ\delta)_H$ is the overlattice glued along $H = \generators{(h/2,\,\delta/2)}$ (@lem:primitive_embedding_eta, @def:gluing-datum-of-a-pair).

Three groups act on $\bD(T_\En)$: the stable group $\Gamma_\En\definedas\widetilde\Orth^+(T_\En) = \Orth^+(T_\En)\intersect\discriminantkernel{T_\En}$; the group $\Gamma^K_\En\definedas\Orth(T_\En)$, which is the group that [@AEGS25, Def. 2.6, printed p. 587] writes $\Gamma_\En$; and $\gent = \rho^{-1}(M)$, with $M$ the summand-preserving subgroup of $\Orth(A_{T_\En},q)$ [@AEGS25, Def. 2.6, printed p. 587; @Ste91, Prop. 2.7, printed p. 6].

1. $\Gamma_\Co\leq\Orth(T_\Co)$ is the monodromy group of the family of unpolarized Coble surfaces: the image of the monodromy representation (@def:transport-and-monodromy) of the local system of lattices with fibre $T_\Co$ (@def:local-system-of-lattices) of that family; the family, with its objects, its base and its local system, is @def:coble-family-unpolarized, and the base is its labelled base, item 3. of that definition, over which the eleven classes are global sections (@lem:d2-local-system(2)); the unlabelled base 2. carries the same family and a larger group, and base 1. is a coarse space with no family (@lem:d2-local-system(5), @rmk:d2-what-is-open(1)). The family of unpolarized Enriques surfaces, whose local system of lattices has fibre $T_\En$ and monodromy group $\Gamma_\En$, induces this family and its local system *of lattices*, in the sense that $T_\Co=\delta^{\perp\ten}$ is cut out of $T_\En$ (@prop:gamma-co-images); that it induces the family itself, that is that the two bases are identified, is not proved by anything read (@rmk:d2-what-is-open(2)). Put $\fco\definedas\bD(T_\Co)/\Gamma_\Co$.
2. $\Gamma^{\mathrm{un}}_\Co\definedas\Orth(T_\Co)$, with $F^{\mathrm{un}}_\Co\definedas\bD(T_\Co)/\Orth(T_\Co)$: the moduli space $M_\Co$ of Coble surfaces is isomorphic to an open subset of $\bD(N)/\Orth(N)$ [@DK13, Prop. 3.2, p. 513].
3. The stable group
$$
\widetilde\Orth^+(T_\Co) = \Orth^+(T_\Co)\intersect\ker\bar\rho,
$$
$\bar\rho$ being the discriminant representation of $T_\Co$ and $\ker\bar\rho$ the group $\ker\bigl(\Orth(L)\to\Orth(A_L)\bigr)$ of [@DK13, (2.1)].
4. For $\Gamma$ one of $\Gamma_\En$, $\Gamma^K_\En$, $\gent$, the restricted stabilizer
$$
R_\Gamma\definedas \text{the image of } \Stab_{\Gamma}(\delta) \text{ in } \Orth(\delta^{\perp T_\En}) = \Orth(T_\Co).
$$
5. $\Gamma_{\Co,2}\leq\Orth(T_\Co)$ is the monodromy group of the VHS of the degree-$2$ Coble family: the image of the monodromy representation (@def:transport-and-monodromy) of the local system of lattices with fibre $T_\Co$ (@def:local-system-of-lattices) of the family of Coble surfaces carrying a degree-$2$ numerical polarization (@def:coble-polarization-classes); the family, with its objects, its base and its period map, is @def:coble-family-degree-two. It is defined by the family and is not a lattice group. Put $F_{\Co,2}\definedas\bD(T_\Co)/\Gamma_{\Co,2}$. The group $R_{\gent} = \bar\rho^{-1}(P)$ of (4) and @prop:gamma-co-images(3) is the restricted Enriques stabilizer; the comparison of $\Gamma_{\Co,2}$ with it is @thm:coble-monodromy-versus-enriques, and the arithmetic group that contains $\Gamma_{\Co,2}$ is $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co) = \Gamma^{\mathrm{dir}}_{\Co,2} = \Gamma^{\mathrm{Hdg}}_{\Co,2}$ (@thm:coble-monodromy-versus-enriques(4)).

A statement about a quotient of $\bD(T_\Co)$ names the group it uses; in particular every count of cusps names its group.
:::

::: {.remark #conj:gamma-co-stable title="The stable-group equality, and its status"}

The equality
$$
\Gamma_\Co=\widetilde\Orth^+(T_\Co)
$$
was the stable-group conjecture of this chapter. It is a theorem on the base that @def:coble-family-unpolarized assigns to $\Gamma_\Co$: on the labelled base, $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable). On the unlabelled base the group is strictly larger (@cor:gamma-co-inclusions(2)), and on the coarse space there is no family at all; the tautological local system of that quotient has monodromy $\Orth^+(T_\Co)$, which is not $\Gamma_\Co$ (@thm:gamma-co-is-full). Statements elsewhere in the book that were conditional on this equality therefore hold on the labelled base, and statements about the other two bases name their group.
:::

::: {.remark #rmk:gamma-co-nodal-pair-proposal title="The $(-4)$-reflection: what is computed, and the three inputs that are missing"}

The lattice half of a refutation of @conj:gamma-co-stable is computed and stands, and by @thm:gamma-co-is-stable its hypothesis does not hold on the labelled base: if the nodal-pair element $w_\delta w_{\delta'}$ were a monodromy element of the family, then its action on $T_\Co$ would be the reflection $s_e$ in the class $e=\delta-\delta'$ of square $-4$ (`computations/reports/smwo_direct-period.md`, Theorem E, and the re-derivation in `computations/reports/coble_658-nodal-pair-refutation-probe-run.txt`), and every such reflection is an integral isometry of $T_\Co$ lying in $\Orth^+(T_\Co)$ and outside $\discriminantkernel{T_\Co}$ (@prop:gamma-co-reflective-set(3)). If that element is in $\Gamma_\Co$, then $\Gamma_\Co\not\subseteq\widetilde\Orth^+(T_\Co)$, the $\Gamma_\Co$ form of @prop:gamma-co-strong-lifting fails, and the cusp counts of $\fco$ are not those of the stable quotient.

Three inputs are missing, and none of them is a proved statement of this book:

1. the local monodromy of a degeneration acquiring two ordinary nodes at once as the product of the two commuting Picard--Lefschetz reflections: no printed statement in `tmp/sources` supplies it, and the record's citation of `.ultramath/smw0o7jbf/m5/A20-direct-period-theorem.md` §6.1(b) points outside main;
2. that the one-node family is a family of Coble surfaces *in the moduli space whose monodromy is $\Gamma_\Co$*. The members themselves are not the difficulty: a one-node member is a singular Coble quotient in the book's sense, a K3 with one $A_1$ point quotiented by an involution that fixes that point and is otherwise free in codimension one (@def:singular-coble), and its resolution is the resolved Coble surface of @def:resolved-coble, "the object traditionally called a classical Coble surface". What is missing is the moduli identification: [@DK13, Prop. 3.2, printed p. 513] is about the *classical* ten-node construction --- "In this note we will restrict ourselves to these classical examples", printed p. 513 --- so it places that construction in $\bD(N)/\Orth(N)$ and says nothing about whether the one-node members lie in the same open subset;
3. that the monodromy of the family over that base is contained in $\Gamma_\Co$, which is functorial once 2 holds and is not otherwise known.

There is a reason, not only a gap, behind the second of these, and it points at where a witness would have to live. In the classical model of [@DK13, §3, printed p. 513] the Coble surface is the blow-up of $\PP^2$ at the ten nodes of a sextic, the double cover $X$ carries the divisors $E_0,\dots,E_{10}$, and their classes $e_0,\dots,e_{10}$ generate $M_X\cong\generators{2}\oplus\generators{-2}^{\oplus10}$, with $T_\Co = M_X^\perp$ (@prop:coble-transcendental). A class of $M_X$ is orthogonal to $T_\Co$, so its reflection acts as the identity on $T_\Co$. That does not settle the question, and the reason is worth stating, because the first reading of it is wrong: the classes $e_0,\dots,e_{10}$ are algebraic on every member, so they are not vanishing classes. A vanishing class must be orthogonal to $\Pic(\widehat X_b)$, hence lies in $T_\Co$ --- which is why the discriminant of the period map is described by classes of $T_\Co$ (@prop:monodromy-contains-root-reflections), not by the $e_i$. What the computation above says is therefore only that the $M_X$-part of the monodromy is invisible on $T_\Co$; it does not say that a $(-4)$-class of $T_\Co$ fails to arise, and a witness for $\Gamma_\Co\not\subseteq\widetilde\Orth^+(T_\Co)$ is neither produced nor excluded by it.

On the tautological reading of base 1 the conclusion of this paragraph is unconditional (@thm:gamma-co-is-full), because $\Gamma^{\mathrm{taut}}_\Co=\Orth^+(T_\Co)$ contains $s_e$ for every primitive $e$ of square $-4$; the three inputs below are what a proof needs for a base whose monodromy is not already the full group. What would settle that case is a loop of the Coble moduli, or a degeneration of it, whose monodromy is computed to be $s_e$; no such computation exists in this repository on main.

The question can be put without either model, and then it is a question about divisors. The period domain is $\bD(T_\Co)$ and the Picard rank of a member jumps exactly on the Heegner divisors $\delta^\perp$ of $T_\Co$. The local monodromy of a loop around such a divisor is the reflection $s_\delta$, and that identification is an input, not a result of this book: @prop:monodromy-contains-root-reflections takes it as its hypothesis ("suppose that for every class $\delta$ of square $-2$ the meridian of $\delta^\perp$ [is $s_\delta$]"), and the only statement of the phenomenon here is @cons:lefschetz-periods, a construction with no printed source. Everything below is conditional on it. By @prop:gamma-co-reflective-set, $s_\delta$ lies in $\widetilde\Orth^+(T_\Co)$ exactly when $\delta^2 = -2$: for $\delta^2 = -4$ it lies in $\Orth^+$ and outside the discriminant kernel, and for $\delta^2 = 2$ or $4$ it lies outside $\Orth^+$ altogether. Two hypotheses make that an equivalence, and neither is proved here; where each stands is worth stating, because they are not equally close.

*(PL)* is cited, not assumed: [@Voi07, Thm. 3.16, printed p. 78] states the Picard--Lefschetz formula $T(\alpha)=\alpha+\epsilon_n\langle\alpha,\delta\rangle\delta$, which for a surface is the reflection in the vanishing class $\delta$. The unipotent Kulikov transform $T=\exp(N)$ of a semistable degeneration (Alexeev--Engel, arXiv:2208.10383v2, §6) is a different statement and is not what this step uses.

*(MG)* is where the work is, and it splits cleanly into a part that follows from the published statement and a part that does not. [@DK13, Prop. 3.2, printed p. 513] gives exactly one thing about the image: $\mathcal M_{Co}$ is isomorphic to an open subset of $\bD(N)/\Orth(N)$ with $N=T_\Co$, the isomorphism being the period map, hence open and injective (Torelli). It says nothing about the complement.


The two-way form that (PL) and (MG) would give is superseded by @thm:gamma-co-is-full below, which needs neither: what remains of it is the one direction that the theorem does not cover --- a met divisor of square $-4$ would give an element outside $\widetilde\Orth^+(T_\Co)$ even if the moduli identification failed. Neither model decides this from what is printed. [@DK13, Prop. 3.2, printed p. 513] says that the moduli space is an open subset of $\bD(N)/\Orth(N)$ with $N=T_\Co$, which constrains no Heegner divisor; the sentence after it says that the quotient of the $(-2)$-Heegner divisor of the Enriques period domain is birationally the same moduli space, which places it inside one. The two are consistent because both are birational statements about a $9$-dimensional space; what they do not say is which Heegner divisors of $T_\Co$ its boundary meets. That is the question item 1e reduces to.
:::

::: {.lemma #lem:orbifold-monodromy-of-a-quotient title="Monodromy of the tautological local system of a quotient orbifold"}

Let $\widetilde U$ be a connected topological space, let $\Gamma$ be a group acting on it, and let $T$ be a $\Gamma$-module. Put $U\definedas\widetilde U/\Gamma$ with the quotient orbifold structure, and let
$$\bT\definedas(\widetilde U\times T)/\Gamma$$
be the quotient of the trivial local system by the diagonal action. Then $\bT$ is a local system on the orbifold $U$ with fibre $T$, and its monodromy representation is
$$\pi_1^{\mathrm{orb}}(U,\tilde x)\too\Aut(T),\qquad (g,[\widetilde\gamma])\longmapsto g,$$
where an orbifold loop based at $x=[\tilde x]$ is a pair $(g,\widetilde\gamma)$ with $g\in\Gamma$ and $\widetilde\gamma$ a path in $\widetilde U$ from $\tilde x$ to $g\tilde x$. Its image is $\Gamma$ and its kernel is $\pi_1(\widetilde U,\tilde x)$; in particular
$$1\too\pi_1(\widetilde U,\tilde x)\too\pi_1^{\mathrm{orb}}(U,\tilde x)\too\Gamma\too1$$
is exact.
:::

::: {.proof}

The quotient map $\widetilde U\times T\to\bT$ is a $\Gamma$-covering, so $\bT$ is a local system on the orbifold $U$. Its pullback to $\widetilde U$ is the trivial local system $\widetilde U\times T$: transport along $\widetilde\gamma$ in the trivial system is the identity of $T$, and at the endpoint $g\tilde x$ the fibre is identified with the fibre at $\tilde x$ by $g$, so transport along the orbifold loop $(g,\widetilde\gamma)$ is $g$. Homotopic orbifold paths have equal transport (@prop:transport-homotopy-invariant), so the assignment is well defined, and it is a homomorphism because the product of orbifold loops is $(g,\widetilde\gamma)(h,\widetilde\delta)=(gh,\widetilde\gamma*(g\widetilde\delta))$ and transport is functorial. It is onto, the constant path at $\tilde x$ from $\tilde x$ to $g\tilde x$ representing $g$, and its kernel is the set of pairs $(1,\widetilde\gamma)$, that is $\pi_1(\widetilde U,\tilde x)$.
:::

::: {.theorem #thm:gamma-co-is-full title="G1 on the universal-family reading: the tautological local system has monodromy $\Orth^+(T_\Co)$"}

Let $B$ be base 1 of @def:coble-family-unpolarized, the coarse space $\mcm_\Co$ of Coble surfaces, read with the orbifold structure for which the period map
$$\per\colon B\too\bD(T_\Co)/\Orth(T_\Co)$$
is an isomorphism of orbifolds onto an open substack of $\bD(T_\Co)/\Orth(T_\Co)$; the map is that of [@DK13, Prop. 3.2, printed p. 513], whose coarse form is @lem:d2a-period-map, and this is the reading under which the tautological local system is a local system of lattices with fibre $T_\Co$; it is the universal-family reading of G1, and it is not the local system of D2a, whose base carries a family of its own (@def:coble-family-unpolarized, @lem:d2-local-system). Let $\bT$ be that local system, the pullback of the tautological local system of the quotient along $\per$ (@def:coble-family-unpolarized), and let
$$\rho\colon\pi_1^{\mathrm{orb}}(B)\to\Orth(T_\Co)$$
be its monodromy representation (@def:transport-and-monodromy), whose image we write $\Gamma^{\mathrm{taut}}_\Co$. Then
$$\Gamma^{\mathrm{taut}}_\Co=\Orth^+(T_\Co).$$
This is the monodromy of the tautological local system and is not $\Gamma_\Co$ of @def:gamma-co-groups(1): the geometric family has its own local system over the labelled base, and its monodromy lies in $\widetilde\Orth^+(T_\Co)$ (@lem:coble-family-labelled-monodromy), a proper subgroup of $\Orth^+(T_\Co)$ (@cor:gamma-co-inclusions(3)).
:::

::: {.proof}

*First inclusion: $\Gamma^{\mathrm{taut}}_\Co\subseteq\Orth^+(T_\Co)$.* The base $B$ is connected, so the period map is single-valued and its image lies in one of the two connected components of $\bD(T_\Co)$; write $\bD^+$ for that component (@prop:lifted-period-map). Transport is an isometry (@prop:local-system-of-lattices-monodromy), so every $\rho(\gamma)$ preserves $\bD^+$ (@cor:vhs-monodromy-stabilizes-component). The lattice $T_\Co$ carries the weight-$2$ Hodge structure of its K3 double cover; a holomorphic $2$-form is anti-invariant under the non-symplectic involution, so $h^{2,0}=1$, and the signature is $(2,9)$ (@prop:coble-transcendental), hence $h^{1,1}=9>0$. So the case $h^{m,m}>0$ of @thm:period-domain-component-stabilizer applies with $m=1$ and $\epsilon=1$, and
$$\Stab_{\Orth(T_\Co)}(\bD^+)=\Theta_\bR(T_\Co)=\Orth^+(T_\Co)$$
by @conv:spinor-positive-subgroup. Hence $\Gamma^{\mathrm{taut}}_\Co\subseteq\Orth^+(T_\Co)$.

*Second inclusion: $\Orth^+(T_\Co)\subseteq\Gamma^{\mathrm{taut}}_\Co$.* The quotient $\bD^+/\Gamma$ is an orbifold and not a manifold --- it is singular along the image of every fixed locus of codimension $\ge2$ [@Dim92, Ch. 4, Rem. (1.2)] --- so the argument is made on the smooth domain $\bD^+$. Put $\Gamma\definedas\Orth^+(T_\Co)$ and let $U\subseteq\bD^+/\Gamma$ be the image of the period map. By the choice of the orbifold structure, $B\to U$ is an isomorphism of orbifolds. Let $\widetilde U\subseteq\bD^+$ be the inverse image of $U$. The domain $\bD^+$ is a bounded symmetric domain, hence connected, and $\widetilde U$ is the complement in it of a proper closed analytic subset $Z$. It is connected: if $\bD^+\sm Z=A\sqcup B$ with $A,B$ nonempty open, take $a\in A$, $b\in B$ and a path $\gamma$ in $\bD^+$ from $a$ to $b$; at the first point $t$ with $\gamma(t)\notin A$ one has $\gamma(t)\in Z$, and a ball $V\ni\gamma(t)$ has $V\sm Z$ connected --- a ball minus a proper analytic subset is connected --- and meeting both $A$ and $B$, a contradiction. So $\widetilde U$ is connected.

Concretely, the complement of $\widetilde U$ is a $\Gamma$-invariant union of Heegner hyperplanes $\delta^\perp$ and lower strata; by the van Kampen--Zariski theorem [@Dim92, Ch. 4, §3] $\pi_1(\widetilde U)$ is generated by the meridians of those hyperplanes, and, where the degeneration is a Lefschetz degeneration with vanishing class $\delta$, each such meridian acts on $T_\Co$ as the reflection $s_\delta$ [@Voi07, Thm. 3.16, printed p. 78] --- the identification of the meridian with a Lefschetz loop is the hypothesis of @prop:monodromy-contains-root-reflections, and it is not needed for the two inclusions. The purity statement --- a regular open subscheme whose complement has codimension $\ge2$ has the same fundamental group --- is SGA1, Exposé X, Corollaire 3.3, printed p. 213, and is cited only in its étale form; the topological statement used here is the connectedness of $\bD^+\sm Z$ proved above.

By its definition in D2a, the local system $\bT$ with its Hodge filtration is the pullback of the tautological local system $(\bD^+\times T_\Co)/\Gamma$ along the period map --- that is what it means for the period map to classify the variation (@prop:lifted-period-map(3)) --- so over $\widetilde U$ it is $(\widetilde U\times T_\Co)/\Gamma$. By @lem:orbifold-monodromy-of-a-quotient its monodromy representation is the projection
$$\pi_1^{\mathrm{orb}}(U,\tilde x)\too\Gamma,\qquad (g,[\widetilde\gamma])\longmapsto g,$$
which is onto. Hence $\Gamma\subseteq\Gamma^{\mathrm{taut}}_\Co$, and the two inclusions give $\Gamma^{\mathrm{taut}}_\Co=\Orth^+(T_\Co)$.
:::


::: {.lemma #lem:gamma-co-labelled-index title="The labelled cover and the index $10!$"}

Let $B\to\bar B$ be the cover of @lem:d2-labelling-cover, with the local system $\bT$ of @lem:d2-local-system and the monodromy groups
$$\Gamma_\Co(B)=\rho\qty{\pi_1(B,s)},\qquad \Gamma_\Co(\bar B)=\rho\qty{\pi_1(\bar B,s)}$$
of @lem:d2-local-system(4),(5), the base point of $B$ lying over that of $\bar B$. Then
$$[\Gamma_\Co(\bar B):\Gamma_\Co(B)]=10!=3\,628\,800 .$$
:::

::: {.proof}

$B\to\bar B$ is a principal $S_{10}$-bundle (@lem:d2-labelling-cover), so
$$1\too\pi_1(B,s)\too\pi_1(\bar B,s)\too S_{10}\too1$$
is exact; this is the statement of @lem:d2-local-system(5) that $\pi_1(B,s)$ is normal in $\pi_1(\bar B,s)$ with quotient $S_{10}$. The deck transformation $\sigma\in S_{10}$ permutes the ten labels, and its monodromy is the permutation of the classes $\varepsilon_1,\dots,\varepsilon_{10}$ of @lem:d2-local-system(2); a permutation of the labels acts faithfully on $A_M$ [@YZZ25, Lemma 6.7], so the action on the labels factors through the monodromy and the map
$$\Gamma_\Co(\bar B)\too\pi_1(\bar B,s)/\pi_1(B,s)=S_{10}$$
is well defined and onto. Its kernel is the image of $\pi_1(B,s)$, namely $\Gamma_\Co(B)$: an element of $\Gamma_\Co(\bar B)$ acts trivially on the labels exactly when it is the monodromy of a loop that lifts to $B$. Hence $\Gamma_\Co(\bar B)/\Gamma_\Co(B)\cong S_{10}$ and the index is $\abs{S_{10}}=10!$.
:::

::: {.theorem #thm:gamma-co-is-stable title="G1: the monodromy group of the unpolarized Coble family is $\widetilde\Orth^+(T_\Co)$"}

Let $V$ be the variety of labelled sextics of @not:d2-plane-sextic-base, whose quotient $B=V/\PGL_3$ is the labelled base of @def:coble-family-unpolarized, item 3., let $\bT$ be the local system of lattices of @lem:d2-local-system, of fibre $T_\Co$, and let
$$\rho\colon\pi_1(V,s)\too\Orth(T_\Co)$$
be its monodromy representation, whose image is $\Gamma_\Co$ (@def:gamma-co-groups(1)). Then
$$\Gamma_\Co=\widetilde\Orth^+(T_\Co).$$
The image of $\Gamma_\Co$ in $\Aut\qty(\bD(T_\Co)^+)=\Orth^+(T_\Co)/\theset{\pm\id}$ is the image of the stable subgroup, and $\fco=\bD(T_\Co)/\Gamma_\Co$ has the same coarse space as $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$. In particular $-\id_{T_\Co}\in\Gamma_\Co$: it lies in $\Orth^+(T_\Co)$ because the positive index is $2$ (@lem:minus-identity-spinor-norm) and in $\ker\bar\rho$ because $A_{T_\Co}\cong(\ZZ/2)^{11}$ (@prop:coble-discriminant-group), so it lies in $\widetilde\Orth^+(T_\Co)$.
:::

::: {.proof}

*First inclusion: $\Gamma_\Co\subseteq\widetilde\Orth^+(T_\Co)$.* This is @lem:coble-family-labelled-monodromy; here is the same argument with the two halves named. The eleven classes $\varepsilon_0,\dots,\varepsilon_{10}$ are values of global sections of $\bV$ (@lem:d2-local-system(2)), so every $\rho(\gamma)$ fixes them and acts trivially on $M=\generators{2}\oplus\generators{-2}^{\oplus10}$ and hence on $A_M$. By @lem:coble-discriminant-actions-conjugate its discriminant action on $T_\Co$ is conjugate to its action on $A_M$, so it is trivial and $\rho(\gamma)\in\discriminantkernel{T_\Co}$; and $\rho(\gamma)\in\Orth^+(T_\Co)$ by @lem:monodromy-is-spinor-positive. Hence $\rho(\gamma)\in\widetilde\Orth^+(T_\Co)$.

*Second inclusion: $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_\Co$ up to $\pm\id$.* Put $\Gamma\definedas\widetilde\Orth^+(T_\Co)$. Because the eleven classes are flat, the family is $M$-polarized with a fixed marking of $M$, and its period map is
$$\per_M\colon V\too\bD(T_\Co)/\Gamma .$$
The moduli space of $M$-polarized K3 surfaces is constructed as $\bD(N)/\Orth(N)^*$ with $N=M^{\perp\Lkt}=T_\Co$ [@DK13, §3], and $\Orth(N)^*=\ker\bigl(\Orth(N)\to\Orth(A_N)\bigr)=\widetilde\Orth(T_\Co)$; the periods of the family lie in one component, so the quotient is by $\Gamma=\widetilde\Orth(T_\Co)\intersect\Orth^+(T_\Co)$. By the Torelli theorem for algebraic K3 surfaces [@PS71], which is the theorem [@DK13, §3] invokes to construct that moduli space and which identifies the moduli of $M$-polarized K3 surfaces with $\bD(N)/\Orth(N)^*$, the period map $\per_M$ is injective; it is holomorphic and open (@prop:lifted-period-map(4)). Let $U$ be its image and $D_U\subseteq\bD(T_\Co)$ its inverse image, which is $\Gamma$-invariant. The lift
$$\widetilde\per_M\colon\widetilde V\too D_U$$
is a homeomorphism onto $D_U$, being a lift of the homeomorphism $V\too U$ between the universal covers (@prop:lifted-period-map(4)); in particular $D_U$ is connected. So $D_U\too U$ is a covering with deck group $\Gamma/\theset{\pm\id}$, and $\pi_1(V,s)\too\Gamma/\theset{\pm\id}$ is onto.

*The monodromy is that projection.* The period map is equivariant (@eq-period-map-equivariance): $\widetilde\per_M(\gamma\tilde b)=\rho(\gamma)\widetilde\per_M(\tilde b)$. A path in $\widetilde V$ from $\tilde b$ to $\gamma\tilde b$ projects to a loop of $V$ whose lift to $D_U$ runs from $\widetilde\per_M(\tilde b)$ to $\rho(\gamma)\widetilde\per_M(\tilde b)$; so $\rho(\gamma)$ is the deck transformation of $D_U\too U$ carrying one to the other, and every deck transformation arises from such a path. Hence $\rho\qty{\pi_1(V,s)}\cdot\theset{\pm\id}=\Gamma$, which is the display up to the sign $\pm\id$; the sign is removed in the second proof.

*Second proof, from D2a's own cover and no period map.* By @lem:coble-family-labelled-monodromy, $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$. By @lem:gamma-co-labelled-index, $[\Gamma_\Co(\bar B):\Gamma_\Co(B)]=10!$, and by @thm:gamma-co-sextic-group, $\Gamma_\Co(\bar B)=\Gamma_{10A_1}$ and $[\Gamma_{10A_1}:\widetilde\Orth^+(T_\Co)]=10!$. Since $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{10A_1}$, the multiplicativity of the index gives
$$[\widetilde\Orth^+(T_\Co):\Gamma_\Co(B)]=\frac{[\Gamma_{10A_1}:\Gamma_\Co(B)]}{[\Gamma_{10A_1}:\widetilde\Orth^+(T_\Co)]}=\frac{10!}{10!}=1,$$
so $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$. This proof uses only the principal $S_{10}$-bundle of @lem:d2-labelling-cover, the flatness of the eleven classes (@lem:d2-local-system(2)) and the sextic-base theorem; no period map and no Torelli theorem enters.
:::

::: {.proposition #prop:gamma-co-geometric-bound title="The discriminant image on each base"}

Let $\Gamma_\Co$ be the monodromy group of the family of @def:coble-family-unpolarized.

1. On the labelled base $B$, $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$, so $\bar\rho(\Gamma_\Co)=\theset{1}$ (@thm:gamma-co-is-stable).
2. On the unlabelled base $\bar B$, $\bar\rho(\Gamma_\Co(\bar B))\subseteq\Theta\definedas\gamma\,\bar\rho_M(\mathfrak S_{10})\,\gamma^{-1}$, where $\gamma\colon A_M\to A_N(-1)$ is the gluing isometry of @lem:coble-discriminant-actions-conjugate and $\mathfrak S_{10}$ permutes $e_1,\dots,e_{10}$ and fixes $e_0$. The group $\Theta$ is isomorphic to $\mathfrak S_{10}$, of order $10!$, and is a proper subgroup of $\Orth(q_{T_\Co})$ of index $2^{13}\cdot3\cdot17\cdot31=12\,951\,552$.
3. On the coarse space $M_\Co$ there is no family (@rmk:d2-what-is-open(1)); the tautological local system of the quotient has monodromy $\Orth^+(T_\Co)$ (@thm:gamma-co-is-full), which is not $\Gamma_\Co$.
:::

::: {.proof}

(1) is @thm:gamma-co-is-stable. For (2), a point of $\bar B$ is a sextic together with its ten nodes as a set (@not:d2-plane-sextic-base), so the class $e_0=f^*H$ of the pullback of a line is the value of a global section of $\bV|_{\bar B}$, while the ten classes $e_1,\dots,e_{10}$ are permuted. A monodromy operator therefore fixes $e_0$ and acts on $M$ by an element of $\mathfrak S_{10}$, and @lem:coble-discriminant-actions-conjugate gives $\bar\rho(\Gamma_\Co(\bar B))\subseteq\gamma\bar\rho_M(\mathfrak S_{10})\gamma^{-1}$. That $\Theta\cong\mathfrak S_{10}$, and its index, is the computation of the same paragraph: the classes $[e_i/2]$, $i\ge1$, are permuted among themselves and $[e_0/2]$ is fixed, so $\mathfrak S_{10}\to\Orth(q_M)$ is injective, $|\Theta|=10!$, and $[\Orth(q_{T_\Co}):\Theta]=\abs{\Orth(q_{T_\Co})}/10!=2^{13}\cdot3\cdot17\cdot31$ by @prop:coble-discriminant-group. (3) is @thm:gamma-co-is-full and @rmk:d2-what-is-open(1).
:::

::: {.theorem #thm:gamma-co-sextic-group title="The sextic base: $\Gamma_{10A_1}=\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)$, and the two indices"}

Let $T=10A_1$, so that $P=\generators{H}\oplus L$ with $L=A_1^{\oplus10}$ and $Q=P^{\perp\Lkt}=T_\Co$ (@thm:occult-period-map-sextics, @lem:ten-a1-permutation-forces-strictness), and let $\Gamma_{10A_1}\le\Orth(T_\Co)$ be the group of [@YZZ25, §3.1] for that type: the image of $\Orth(\Lkt,\Delta,H)\to\Orth(Q)$, restricted to the subgroup preserving the component $\bD(Q)$. Let $\Theta\le\Orth(q_{T_\Co})$ be the image of the permutations of $e_1,\dots,e_{10}$ fixing $e_0$ (@prop:gamma-co-geometric-bound(2)). Then:

0. The unlabelled base $\bar B$ of @def:coble-family-unpolarized is the moduli space $\mathcal M_T$ of sextics of type $T$, and the local system $\bT$ of @lem:d2-local-system is the local system of that family; hence $\Gamma_\Co(\bar B)=\Gamma_{10A_1}$.
1. $\Theta\cong\mathfrak S_{10}$ and $|\Theta|=10!=3\,628\,800$.
2. $\Gamma_{10A_1}=\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)$.
3. $[\Gamma_{10A_1}:\widetilde\Orth^+(T_\Co)]=|\Theta|=10!$ and
$$[\Orth^+(T_\Co):\Gamma_{10A_1}]=\frac{\abs{\Orth(q_{T_\Co})}}{10!}=2^{13}\cdot3\cdot17\cdot31=12\,951\,552 .$$
4. $\widetilde\Orth^+(T_\Co)\subsetneq\Gamma_{10A_1}\subsetneq\Orth^+(T_\Co)$; on the family of @def:coble-family-unpolarized the inclusion $\Gamma_\Co=\Gamma_\Co(B)\subseteq\Gamma_\Co(\bar B)=\Gamma_{10A_1}$ of @lem:d2-local-system(5) has index $10!$ (@lem:gamma-co-labelled-index).
:::

::: {.proof}

(0). A point of $\bar B$ is an irreducible plane sextic with its ten nodes as a set (@not:d2-plane-sextic-base), which is the datum of a sextic of type $T=10A_1$; and the family of @lem:d2-unpolarised-family(3), quotiented by the labelling, is the family of K3 resolutions of the double covers branched along those sextics, which is the family of [@YZZ25, §2.3]. By [@YZZ25, Thm. 3.4] the period map is an isomorphism $\mathcal M_T\cong\Gamma_T\backslash(\bD_T-\mathcal H_T)$, so the monodromy of the local system on $\mathcal M_T$ is $\Gamma_T=\Gamma_{10A_1}$; over the orbifold points this is [@YZZ25, Prop. 6.6].

(1) is @prop:gamma-co-geometric-bound(2).

(2), *the inclusion $\subseteq$.* By [@YZZ25, §3.1] an element of $\Orth(\Lkt,\Delta,H)$ preserves $H$ and the set $\Delta=\theset{r_1,\dots,r_{10}}$ of the ten classes of the resolution. Hence its restriction to $P$ lies in $\Orth(P,H,\Delta)$, which is $\operatorname{Aut}(\Delta)\cong\mathfrak S_{10}$ and acts on $A_P\cong\ZZ/2\times(\ZZ/2)^{10}$ by permuting the ten generators $[r_i/2]$ and fixing $[H/2]$ [@YZZ25, Lemma 6.7]. By @lem:coble-discriminant-actions-conjugate the discriminant action on $Q=T_\Co$ is $\gamma\bar\rho_P(\psi)\gamma^{-1}$ for $\psi$ the restriction to $P$, so it lies in $\Theta$. That gives the inclusion into $\bar\rho^{-1}(\Theta)$; the inclusion into $\Orth^+(T_\Co)$ is the restriction to the component in the definition of $\Gamma_{10A_1}$ [@YZZ25, §3.1].

(2), *the inclusion $\supseteq$.* Let $\varphi\in\Orth^+(T_\Co)$ with $\bar\rho(\varphi)\in\Theta$. By [@YZZ25, Lemma 6.7] the map $\Orth(P,H,\Delta)\to\Orth(A_P)$ has image $\gamma^{-1}\Theta\gamma$, so there is $\psi\in\Orth(P,H,\Delta)$ with $\bar\rho_P(\psi)=\gamma^{-1}\bar\rho(\varphi)\gamma$; equivalently $\bar\rho(\varphi)=\gamma\bar\rho_P(\psi)\gamma^{-1}$, which by @lem:coble-discriminant-actions-conjugate is the condition that the pair $(\psi,\varphi)$ preserve the gluing subgroup of $P\oplus Q$ in $\Lkt$. By Nikulin's criterion [@Nik80, Cor. 1.5.2], which is @thm:automorphism-lifting-criterion, the pair then extends to an isometry $g\in\Orth(\Lkt)$ with $g|_P=\psi$ and $g|_Q=\varphi$. Since $\psi$ preserves $H$ and permutes $\Delta$, so does $g$; hence $\varphi$ is the restriction of an element of $\Orth(\Lkt,\Delta,H)$, and $\varphi\in\Gamma_{10A_1}$ because the restriction map $\Orth(\Lkt,H,\Delta)\to\Gamma_{10A_1}$ is an isomorphism [@YZZ25, Prop. 6.5(ii)].

(3). By @thm:two-elementary-surjectivity the map $\bar\rho\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is onto, its hypotheses being that $T_\Co$ is even, indefinite and $2$-elementary, which it is: $T_\Co=\generators{2}\oplus E_{10}(2)$ of signature $(2,9)$ (@prop:coble-period-domain(2)). The kernel $\ker\bar\rho$ contains the reflection $s_\zeta$ in a primitive vector $\zeta$ of square $2$, and $s_\zeta\notin\Orth^+(T_\Co)$ (@prop:gamma-co-reflective-set(2)); so of the two cosets of $\ker\bar\rho$ over a class $g\in\Orth(q_{T_\Co})$ one lies in $\Orth^+$, and $\bar\rho$ maps $\Orth^+(T_\Co)$ onto $\Orth(q_{T_\Co})$. Hence $\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)\to\Theta$ is onto with kernel $\Orth^+(T_\Co)\intersect\ker\bar\rho=\widetilde\Orth^+(T_\Co)$, so the first index is $|\Theta|=10!$, and the second is $|\Orth(q_{T_\Co})|/10!$ with $|\Orth(q_{T_\Co})|$ from @prop:coble-discriminant-group.

(4). Both indices in (3) exceed $1$. The last clause is @lem:gamma-co-labelled-index, which gives the index of $\Gamma_\Co(B)$ in $\Gamma_\Co(\bar B)=\Gamma_{10A_1}$ from the $S_{10}$-cover, with @lem:d2-local-system(5) for the containment; it does not use the labelled-base theorem.
:::

::: {.corollary #cor:gamma-co-inclusions title="What G1 decides for the stable group"}

1. *The labelled base, the base of $\Gamma_\Co$* (@def:coble-family-unpolarized). $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable): the forward and the reverse inclusion both hold, so @conj:gamma-co-stable is true on this base, and $\fco$ has the coarse space of $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$. Every count stated for the stable quotient is therefore a count for $\fco$: $527$ $0$-cusps (@thm:coble-zero-cusp-count(2)) and $189\,720$ $1$-cusps (@thm:plane-fibre(3)).
2. *The unlabelled base.* $\Gamma_\Co(\bar B)=\Gamma_{10A_1}=\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)$ (@thm:gamma-co-sextic-group), so
$$\widetilde\Orth^+(T_\Co)\subsetneq\Gamma_{10A_1}\subsetneq\Orth^+(T_\Co),\qquad[\Gamma_{10A_1}:\widetilde\Orth^+(T_\Co)]=10!,\qquad[\Orth^+(T_\Co):\Gamma_{10A_1}]=12\,951\,552 .$$
The inclusion $\Gamma_\Co\subseteq\Gamma_\Co(\bar B)$ is @lem:d2-local-system(5), and its index is $10!$ by @thm:gamma-co-sextic-group(4).
3. *The coarse space.* There is no family (@rmk:d2-what-is-open(1)); the tautological local system has monodromy $\Gamma^{\mathrm{taut}}_\Co=\Orth^+(T_\Co)$ (@thm:gamma-co-is-full), and
$$[\Orth^+(T_\Co):\widetilde\Orth^+(T_\Co)]=\abs{\Orth(q_{T_\Co})}=2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31=46\,998\,591\,897\,600$$
by @thm:two-elementary-surjectivity and @prop:coble-discriminant-group.
:::

::: {.remark #rmk:gamma-co-d2a title="The three bases, and which group each gives"}

@def:coble-family-unpolarized has one family and three bases. On the labelled base $B$, the base that @def:gamma-co-groups(1) assigns to $\Gamma_\Co$, the group is $\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable). On the unlabelled base $\bar B$ the same family has the larger group $\Gamma_{10A_1}=\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)$, which contains $\widetilde\Orth^+(T_\Co)$ with index $10!$ and is contained in $\Orth^+(T_\Co)$ with index $12\,951\,552$ (@thm:gamma-co-sextic-group); the inclusion $\Gamma_\Co\subseteq\Gamma_\Co(\bar B)$ has index $10!$. On the coarse space $M_\Co$ there is no family; the tautological local system of the quotient is a different object, with group $\Orth^+(T_\Co)$ (@thm:gamma-co-is-full).

So the answer to G1 depends on the base, and the base is part of D2a; on the labelled base it is the stable group. What remains open is the index of $\Gamma_\Co$ in $\Gamma_{10A_1}$, that is the comparison of bases 2 and 3 (@qst:sextic-group-comparison), and the sign $-\id\in\Gamma_\Co$, which does not affect $\fco$.
:::

::: {.remark #rmk:gamma-co-status title="What is established about $\Gamma_\Co$"}

On the labelled base of D2a, $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable): the forward inclusion is @lem:coble-family-labelled-monodromy, and the reverse inclusion is the period-map argument of the theorem. So @conj:gamma-co-stable holds on the base the definition names, and $\fco=\bD(T_\Co)/\Gamma_\Co$ has the coarse space of $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$; every cusp count for the stable quotient is a count for $\fco$ (@cor:gamma-co-inclusions(1)).

Two further things are settled by the equality itself. The sign: $-\id_{T_\Co}\in\widetilde\Orth^+(T_\Co)$ (@lem:minus-identity-spinor-norm, @prop:coble-discriminant-group), so $-\id\in\Gamma_\Co$, and on the labelled base a loop does carry it. The index: $\Gamma_\Co\subseteq\Gamma_\Co(\bar B)=\Gamma_{10A_1}$ has index $10!$ (@thm:gamma-co-sextic-group(4)), so the comparison of bases 2 and 3 is settled as well. What is not a statement about $\Gamma_\Co$ is the coarse quotient: its tautological group is $\Orth^+(T_\Co)$ (@thm:gamma-co-is-full).
:::

::: {.lemma #lem:gluing-discriminant-identification title="The gluing identification $\kappa\colon A_{E_{10}(2)}\isoto A_{T_\En}$"}

With $T_\Co = \generators{h}\perp E_{10}(2)$, $T_\En = U\perp E_{10}(2)$, $\delta$ and $H = \generators{(h/2,\delta/2)}$ as in @def:gamma-co-groups, put $S\definedas T_\Co\perp\ZZ\delta$, so that $T_\En = S_H$ and $A_{T_\En} = H^{\perp}/H$ carries the quadratic form induced by $q_S$ (@thm:nikulin-gluing); the map $\kappa$ below is the quotient $A_{E_{10}(2)}\isoto H^{\perp}/H$ and is not the inclusion $\kappa_h$ of that theorem.
Write $A_S = A_{T_\Co}\oplus A_{\ZZ\delta} = \generators{[h/2]}\perp A_{E_{10}(2)}\perp\generators{[\delta/2]}$. Then:

1. $H^{\perp} = \theset{a[h/2] + y + a[\delta/2]\ \mid\ a\in\{0,1\},\ y\in A_{E_{10}(2)}}$ and $[(a,y,a)] = [(0,y,0)]$ for these elements, so that
$$
\kappa\colon A_{E_{10}(2)}\too H^{\perp}/H = A_{T_\En},\qquad y\longmapsto[(0,y,0)],
$$
is a bijection.
2. $\kappa$ is an isometry of quadratic forms: $q_{T_\En}(\kappa(y)) = q_{E_{10}(2)}(y)$ for every $y\in A_{E_{10}(2)}$.
3. $\kappa$ carries the summands $A_{U(2)}$ and $A_{E_8(2)}$ of $A_{E_{10}(2)}$ onto the summands of the same names in $A_{T_\En} = A_{U(2)}\perp A_{E_8(2)}$; hence it conjugates the summand-preserving group $M\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})\leq\Orth(A_{T_\En},q)$ to the same product in $\Orth(q_{E_{10}(2)})$, which is the group $P$ of @def:congruence-group under the restriction isomorphism $\Orth(q_{T_\Co})\iso\Orth(q_{E_{10}(2)})$ of @lem:coble-discriminant-blocks(3).
4. Let $\varphi\in\Orth(T_\Co)$ fix $[h/2]$, so that $\varphi\oplus\id_{\ZZ\delta}$ preserves $H$ and extends to an isometry $g$ of $T_\En$ with $\restrictionof{g}{T_\Co} = \varphi$ (@thm:automorphism-lifting-criterion). Then
$$
\kappa^{-1}\,\bar\rho_{T_\En}(g)\,\kappa = \restrictionof{\bar\rho_{T_\Co}(\varphi)}{A_{E_{10}(2)}} ;
$$
in particular $g\in\discriminantkernel{T_\En}$ exactly when $\bar\rho_{T_\Co}(\varphi)$ acts trivially on $A_{E_{10}(2)}$, and, since $\bar\rho_{T_\Co}(\varphi)$ fixes $[h/2]$ and $A_{T_\Co} = \generators{[h/2]}\perp A_{E_{10}(2)}$, exactly when $\bar\rho_{T_\Co}(\varphi) = \id$.
:::

::: {.proof}

*The gluing data.* $S$ is even, and $H$ has order $2$ and is isotropic: the element $(h/2,\delta/2)$ has
$$
q_S = q_{T_\Co}(h/2) + q_{\ZZ\delta}(\delta/2) = \tfrac12 - \tfrac12 = 0 \pmod{2\ZZ},
$$
and its pairing with itself is $0$ in $\QQ/\ZZ$ for the same reason. So $A_{T_\En} = H^{\perp}/H$ with $q_{T_\En}$ induced by $\restrictionof{q_S}{H^{\perp}}$ (@thm:nikulin-gluing). On the two generators $q(h/2) = h^2/4 = \tfrac12$ and $q(\delta/2) = \delta^2/4 = -\tfrac12$, so $b(h/2,h/2) = h^2/4 = \tfrac12$ and $b(\delta/2,\delta/2) = \delta^2/4 = -\tfrac12$ in $\QQ/\ZZ$.

*(1)* An element $z = a[h/2] + y + c[\delta/2]$, with $a,c\in\{0,1\}$ and $y\in A_{E_{10}(2)}$, lies in $H^{\perp}$ exactly when
$$
b\bigl(z,(h/2,\delta/2)\bigr) = a\,b(h/2,h/2) + b(y,h/2) + c\,b(\delta/2,\delta/2) = \tfrac{a-c}{2}
$$
vanishes in $\QQ/\ZZ$, that is exactly when $a = c$; the middle term vanishes because $b(A_{E_{10}(2)},[h/2]) = 0$, $T_\Co = \generators{h}\perp E_{10}(2)$ being an orthogonal sum. This is the set displayed in (1). For such a $z$ one has $z - a(h/2,\delta/2) = (0,y,0)$ with $a(h/2,\delta/2)\in H$, so $[z] = [(0,y,0)]$, and every class of $H^{\perp}/H$ is of this form. The map is injective on these representatives: if $(0,y,0)\in H$, then $y$ is the $A_{E_{10}(2)}$-coordinate of $0$ or of $(h/2,\delta/2)$, and in both cases $y = 0$. Hence $\kappa$ is a bijection.

*(2)* $q_{T_\En}(\kappa(y)) = q_S(0,y,0) = q_{T_\Co}(y) = q_{E_{10}(2)}(y)$, the middle term because $q_{T_\En}$ is induced by $q_S$ on $H^{\perp}$ and $(0,y,0)\in H^{\perp}$, the last because $T_\Co = \generators{h}\perp E_{10}(2)$ is an orthogonal sum.

*(3)* Since $U$ is unimodular, $T_\En^* = U\oplus U(2)^*\oplus E_8(2)^*$, so the classes modulo $T_\En$ of $U(2)^*$ and of $E_8(2)^*$ are the two summands of $A_{T_\En} = A_{U(2)}\perp A_{E_8(2)}$. For $y\in A_{U(2)}$ or $y\in A_{E_8(2)}$ one has $y\in E_{10}(2)^* = U(2)^*\oplus E_8(2)^*\subseteq T_\Co^*\cap T_\En^*$, the $U(2)^*\oplus E_8(2)^*$ summand being common to $T_\Co^* = \generators{h/2}\oplus E_{10}(2)^*$ and to $T_\En^* = U\oplus E_{10}(2)^*$, and the class of $y$ modulo $T_\En$ is $\kappa(y) = [(0,y,0)]$; so $\kappa$ maps the two summands of $A_{E_{10}(2)}$ onto those of $A_{T_\En}$ and conjugates $\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ to the same product. For the last clause, $A_{T_\Co} = \generators{[h/2]}\perp A^0$ with $A^0 = A_{E_{10}(2)}$, so restriction is an isomorphism $\Orth(q_{T_\Co})\iso\Orth(q_{A^0})$, and it carries the stabilizer $P$ of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ to $\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ (@lem:coble-discriminant-blocks(3), (4)).

*(4)* Let $y\in A_{E_{10}(2)}$, represented by the functional that is $y$ on $E_{10}(2)$ and vanishes on $\generators{h}$ and on $\delta$. That representative lies in $E_{10}(2)^* = U(2)^*\oplus E_8(2)^*$, which is a summand of $T_\Co^* = \generators{h/2}\oplus E_{10}(2)^*$ and of $T_\En^* = U\oplus E_{10}(2)^*$; so $y$ may be read indifferently as a class of $A_{T_\Co}$ or of $A_{T_\En}$. The discriminant action of $g$ is $[x]\mapsto[g(x)]$ on $T_\En^*$. Since $g$ restricts to $\varphi$ on $T_\Co$ and fixes $\delta$, the functionals $g(y)$ and $\bar\rho_{T_\Co}(\varphi)(y)$ agree on $T_\Co$ and both vanish on $\delta$, hence are equal; note also that $\bar\rho_{T_\Co}(\varphi)$ preserves $A_{E_{10}(2)} = [h/2]^{\perp}$, because it fixes $[h/2]$. So
$$
\bar\rho_{T_\En}(g)(\kappa(y)) = [g(y)] = [\bar\rho_{T_\Co}(\varphi)(y)] = \kappa\bigl(\bar\rho_{T_\Co}(\varphi)(y)\bigr),
$$
which is the displayed identity. Its last clause is then immediate, and $\bar\rho_{T_\Co}(\varphi)$ acts on the direct sum $A_{T_\Co} = \generators{[h/2]}\perp A_{E_{10}(2)}$ as the identity on the first summand by hypothesis.
:::

::: {.proposition #prop:gamma-co-images title="The three restricted stabilizers"}
With $\delta$, $H$ and $R_\Gamma$ as in @def:gamma-co-groups, and $\bar\rho$ the discriminant representation of $T_\Co$:

1. $R_{\Gamma_\En} = \widetilde\Orth^+(T_\Co)$.
2. $R_{\Gamma^K_\En}$ is the stabilizer in $\Orth(T_\Co)$ of the class $[h/2]$ of $A_{T_\Co}$, and that stabilizer is all of $\Orth(T_\Co)$, because $[h/2]$ is the characteristic class of $q_{T_\Co}$:
$$
R_{\Gamma^K_\En} = \theset{\varphi\in\Orth(T_\Co)\ \mid\ \bar\rho(\varphi)(h/2) = h/2} = \Orth(T_\Co).
$$
3. $R_{\gent} = \bar\rho^{-1}(P)$, where $P\leq\Orth(q_{T_\Co})$ is the stabilizer of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ of the proof. It is a subgroup of $\Orth(T_\Co)$ of index $[\Orth(q_{T_\Co}) : P] = 2^7\cdot17\cdot31 = 67\,456$ (Step 6 of the proof), and it contains $\ker\bar\rho$.
:::

::: {.proof}

*Step 0: the two lattices and the gluing.* $T_\Co = \generators{h}\perp U(2)\perp E_8(2)$ and $T_\En = U\perp U(2)\perp E_8(2)$, and $\delta = \tilde e-\tilde f$ has $\delta^2 = -2$ and $\delta^{\perp T_\En} = \eta(T_\Co)$ (@lem:primitive_embedding_eta). By Nikulin's gluing theorem (@thm:nikulin-gluing, which is [@Nik80, Prop. 1.5.1, printed p. 111]) an even overlattice of $T_\Co\perp\generators{\delta}$ is the same thing as an isotropic subgroup $H\subseteq A_{T_\Co}\oplus A_{\generators{\delta}}$, and $A_{(T_\Co\perp\generators{\delta})_H} = H^{\perp}/H$ as quadratic forms, the form on the quotient being the one induced by $q_{T_\Co}\oplus q_{\generators{\delta}}$ on $H^{\perp}$; here $H = \generators{(h/2,\delta/2)}$. Isotropy of this $H$ is the single congruence
$$
q_{T_\Co}(h/2)+q_{\generators{\delta}}(\delta/2) = \tfrac12-\tfrac12\equiv 0 \pmod{2\bZ},
$$
and it is what makes $T_\En$ an *even* lattice rather than merely an overlattice glued along a subgroup of order $2$. Since $\abs{H} = 2$,
$$
\abs{A_{T_\En}} = \abs{A_{T_\Co}}\cdot\abs{A_{\generators{\delta}}}/\abs{H}^2 = 2^{11}\cdot 2/4 = 2^{10},
$$
as the invariant $a = 10$ of $T_\En = (12,10,0)_2$ requires.

*Step 1: the discriminant form of $T_\Co$, and its characteristic class.* On the orthogonal decomposition $A_{T_\Co} = \generators{h/2}\perp A_{U(2)}\perp A_{E_8(2)}$, which is orthogonal because $T_\Co = \generators{h}\perp E_{10}(2)$ is, the values of $q$ are these:

- $q(h/2) = h^2/4 = 1/2$, and $b(h/2,h/2) = 1/2$;
- on $A_{U(2)}$, with the classes of $e'/2$ and $f'/2$ for the isotropic basis $e',f'$ of $U(2)$, $(e',f') = 2$: $q(e'/2) = q(f'/2) = 0$ and $q((e'+f')/2) = (e'+f')^2/4 = 1$, so $q\bmod1$ vanishes on this block and its two nonzero values are $0$ and $1$, both integers;
- on $A_{E_8(2)}$, with the classes of $\alpha_i/2$ for a basis $\alpha_i$ of $E_8$: $q(y/2) = y^2/2\in\bZ$ for every $y\in E_8$, so $q\bmod1$ vanishes here too, and $q$ on this block is the quadratic form $y\mapsto y^2/2\bmod 2\bZ$ of $E_8/2E_8$.

That $q$ takes values in $\tfrac12\bZ/2\bZ\cong\bZ/4$ and that the class $w$ below exists and is unique are Nikulin's statements for every even $2$-elementary lattice, and are why the argument needs $2$-elementarity: if $L$ is even and $2$-elementary then $2x\in L$ for $x\in L^*$, hence $q(x) = x^2$ lies in $\tfrac12\bZ/2\bZ$; $x\mapsto q(x)\bmod1$ is therefore a linear function $A_L\to\tfrac12\bZ/\bZ$, and since $b$ is nondegenerate there is a *unique* $w$ with $b(w,x)\equiv q(x)\pmod1$ for all $x$, the characteristic element of $q$; it is additive over orthogonal sums, $w_{q_1\oplus q_2} = w_{q_1}\oplus w_{q_2}$, and it is $0$ exactly when $q$ is $\bZ$-valued [@Nik80, §3.9, printed pp. 149--150]. Applied to $q_{T_\Co} = q_{\generators{h/2}}\oplus q_{E_{10}(2)}$ this gives $w = [h/2]$ in one line: $q(h/2) = h^2/4 = 1/2 = b(h/2,h/2)$ makes $[h/2]$ the characteristic element of the first summand, and $q_{E_{10}(2)}$ is $\bZ$-valued, $q(y/2) = y^2/2\in\bZ$ for $y\in E_{10}$, so its characteristic element is $0$. Hence for every isometry $\sigma$ of $(A_{T_\Co},q)$ and every $x$,
$$
b(\sigma(h/2),x) = b(h/2,\sigma^{-1}x)\equiv q(\sigma^{-1}x) = q(x)\equiv b(h/2,x)\pmod1,
$$
and nondegeneracy of $b$ gives $\sigma(h/2) = h/2$: every isometry of $q_{T_\Co}$ fixes $[h/2]$. This is the case $k = [h/2]$ of @lem:coble-discriminant-blocks(3), which proves the same thing for every form of the shape $\bZ k\perp A^0$; the argument is repeated here because (1) and (3) both use it, and because the vanishing of $q\bmod1$ has to be checked on the two blocks separately, with a different reason in each.

*Step 2: which isometries of $T_\Co$ lift over $\delta$.* Let $g\in\Orth(T_\En)$ fix $\delta$. Then $g$ preserves $\delta^{\perp T_\En} = \eta(T_\Co)$, so after scalar extension $g = \varphi\oplus\id_{\generators{\delta}}$ with $\varphi = \restrictionof{g}{T_\Co}$; in particular the restriction map $\Stab_{\Orth(T_\En)}(\delta)\to\Orth(T_\Co)$ is injective. And $\varphi\oplus\id$ preserves the overlattice $T_\En$ exactly when $(\bar\rho(\varphi)\oplus\id)(H) = H$ (@thm:automorphism-lifting-criterion, which is [@Nik80, Cor. 1.5.2, printed p. 111] applied to the gluing datum of @def:gluing-datum-of-a-pair). The elements of $H$ are $0$ and $(h/2,\delta/2)$, and the second coordinate of $(\bar\rho(\varphi)\oplus\id)(h/2,\delta/2)$ is $\delta/2\neq0$, so the condition is $\bar\rho(\varphi)(h/2) = h/2$. Conversely that condition makes $\varphi\oplus\id$ preserve $H$, hence extend to an isometry of $T_\En$, which fixes $\delta$. So $\varphi$ extends to an isometry of $T_\En$ fixing $\delta$, uniquely, exactly when it fixes $[h/2]$; on discriminant groups, $\varphi\oplus\id$ acts by $\bar\rho(\varphi)$ on $A_{E_{10}(2)}$, which $\kappa$ identifies with the whole of $A_{T_\En}$ (@lem:gluing-discriminant-identification(4)).

*Step 3: part (2).* By Step 1 every isometry of $q_{T_\Co}$ fixes $[h/2]$, and by @thm:two-elementary-surjectivity ([@Nik80, Thm. 3.6.3, printed p. 144]) the map $\bar\rho\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is onto, its hypotheses being exactly that $T_\Co$ is even, indefinite and $2$-elementary, which the table gives; $T_\Co$ is moreover the case $a = t_{(+)}+t_{(-)}$ of the proof of the theorem, $11 = 2+9$, where Nikulin reduces to the orthogonal summand $u_+^{(2)}(2)$ or $\upsilon_+^{(2)}(2)$ that $q_{T_\Co}$ has in its $U(2)$ block [@Nik80, Thm. 3.6.3, printed p. 145]. So every $\varphi\in\Orth(T_\Co)$ satisfies the condition of Step 2, and
$$
\Stab_{\Orth(T_\En)}(\delta) = \theset{\varphi\oplus\id_{\generators{\delta}}\mid\varphi\in\Orth(T_\Co)}\;\cong\;\Orth(T_\Co),
$$
the restriction map being the inverse. That is (2), and with it: every isometry of $T_\Co$ extends to an isometry of $T_\En$ fixing $\delta$.

*Step 4: part (1).* Let $g = \varphi\oplus\id$ fix $\delta$. By @lem:gluing-discriminant-identification(4), $g\in\discriminantkernel{T_\En}$ exactly when $\bar\rho(\varphi)$ acts trivially on $A_{E_{10}(2)}$; since $\bar\rho(\varphi)$ fixes $[h/2]$ (Step 1) and $A_{T_\Co} = \generators{h/2}\oplus A_{E_{10}(2)}$, that holds exactly when $\bar\rho(\varphi) = \id$. For the sign, recall that $\Orth^+(L) = \Theta_\bR(L) = \ker\spinornorm_\bR$ is the kernel of the real spinor norm [@def:lattice-spinor-kernels], and that $g = \varphi\perp\id_{\generators{\delta}}$ is an orthogonal sum. The spinor norm is multiplicative on an orthogonal sum,
$$
\spinornorm_\bR(\varphi\perp\psi) = \spinornorm_\bR(\varphi)\,\spinornorm_\bR(\psi),
$$
because a reflection $s_w$ with $w\in T_\Co\tensor\bR$ acts on $T_\En\tensor\bR$ as the reflection in the same vector, with the same value $\spinornorm_\bR(s_w) = [-\tfrac12w^2]$ [@def:spinor-norm], and $\varphi\perp\psi = (\varphi\perp\id)(\id\perp\psi)$. So $\spinornorm_\bR(g) = \spinornorm_\bR(\varphi)\cdot\spinornorm_\bR(\id) = \spinornorm_\bR(\varphi)$, and $g\in\Orth^+(T_\En)$ exactly when $\varphi\in\Orth^+(T_\Co)$.

The sign is not read off positive definite subspaces, and the tempting argument that it is, is false: $\delta^2<0$ does not place every maximal positive definite subspace of $T_\En\tensor_\bR$ inside $\delta^{\perp}$, since $\eta(h)$ and $e'+f'+\delta$ span a positive definite plane --- of the maximal dimension $2$ --- with $(\eta(h),e'+f'+\delta) = 0$ and $(e'+f'+\delta,\delta) = -2$. What is true is the spinor statement above, and it is what the proof uses. So restriction carries $\Stab_{\Gamma_\En}(\delta)$ into $\widetilde\Orth^+(T_\Co)$; conversely, for $\varphi\in\widetilde\Orth^+(T_\Co)$ the element $\varphi\oplus\id$ lies in $\Stab_{\Gamma_\En}(\delta)$ by the two characterizations just proved. That is (1).

*Step 5: part (3).* By @prop:sterk-group-identification(2), $\gent = \rho^{-1}(M)$ with $M = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ the subgroup of $\Orth(A_{T_\En},q)$ preserving the decomposition, the identification of $\gent$ with the group of [@AEGS25, Def. 2.6, printed p. 587] being @prop:sterk-group-identification(1) and the description by the two summands being [@Ste91, Prop. 2.7, printed p. 6]. So $g = \varphi\oplus\id$ fixing $\delta$ lies in $\gent$ exactly when $\bar\rho(\varphi)$ preserves $A_{U(2)}$ and $A_{E_8(2)}$, the summands of $A_{T_\En}$ being $\kappa$ of the summands of $A_{E_{10}(2)}$ (@lem:gluing-discriminant-identification(3)). Every $\sigma\in\Orth(q_{T_\Co})$ fixes $w = [h/2]$ (Step 1), hence preserves $w^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$, of dimension $10$; so restriction $\Orth(q_{T_\Co})\to\Orth(w^{\perp},q|_{w^{\perp}})$ is defined, and it is injective because an isometry fixing $w^{\perp}$ pointwise fixes $w$ too, $A_{T_\Co} = \generators{w}\oplus w^{\perp}$. The condition is therefore $\bar\rho(\varphi)\in P$, where $P$ is the stabilizer in $\Orth(q_{T_\Co})$ of the decomposition $w^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$, and $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ by @lem:coble-discriminant-blocks(4). So $R_{\gent} = \bar\rho^{-1}(P)$, and it contains $\ker\bar\rho$.

*Step 6: the index.* Because $\bar\rho$ is onto (Step 3), $[\Orth(T_\Co):R_{\gent}] = [\Orth(q_{T_\Co}):P]$, and by orbit--stabilizer the latter is the number of elements in the orbit of the decomposition $D\colon w^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$. Let $N$ be the number of decompositions of $w^{\perp}$ into a $2$-dimensional summand isometric to $A_{U(2)}$ and an $8$-dimensional one isometric to $A_{E_8(2)}$; the orbit lies in that set, so $[\Orth(q_{T_\Co}):P]\leq N$. The two are computed separately, and they agree.

*(i) $N = 67\,456$.* On $w^{\perp}$ the form $q$ is $\bZ$-valued (Step 1), so $(w^{\perp},q)$ is a quadratic space over $\bF_2$, and it is of plus type: $528$ of its classes have $q = 0$, the zero class included, and $496$ have $q = 1$ (@lem:coble-discriminant-blocks(2), whose count $3\cdot136+1\cdot120 = 528$ is this one). A $2$-dimensional subspace of $w^{\perp}$ is isometric to $A_{U(2)}$ exactly when it is spanned by classes $a,b$ with $q(a) = q(b) = 0$ and $b(a,b) = 1/2$, for then $q(a+b) = 1$ and $b$ is nondegenerate on the span. There are $527$ choices for $a$; for fixed $a$ the classes with $b(a,b) = 1/2$ form an affine hyperplane of order $2^9 = 512$, and the translation $b\mapsto b+a$ preserves it and sends $q(b)$ to $q(b)+q(a)+b(a,b) = q(b)+1$, so exactly $256$ of them have $q(b) = 0$; each subspace is counted twice, through its two classes of value $0$. Hence
$$
N = \frac{527\cdot 256}{2} = 527\cdot 128 = 2^7\cdot17\cdot31 = 67\,456 .
$$
The orthogonal complement of such a subspace is a plus space of dimension $8$, that is $A_{E_8(2)}$ up to isometry, so every such subspace is one of the decompositions counted by $N$.

*(ii) $\abs{\Orth(q_{T_\Co})}/\abs{P} = 2^7\cdot17\cdot31$.* Here $\Orth(q_{T_\Co})\cong\Orth(w^{\perp},q)$ is the orthogonal group of a hyperbolic space of dimension $10$, and $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$. The restriction is an isomorphism, not only an injection: an isometry of $w^{\perp}$ extends by $w\mapsto w$, and that is an isometry because $\generators{w}\perp w^{\perp} = A_{T_\Co}$. Both orders are counts of ordered hyperbolic bases, an isometry of a hyperbolic space being determined by, and determining, the image of one fixed hyperbolic basis, and in dimension $2m$ the first hyperbolic pair can be chosen in $(2^{2m-1}+2^{m-1}-1)\cdot2^{2m-2}$ ways. This gives $\abs{\Orth(q_{U(2)})} = 2$, then $\abs{\Orth(q_{E_8(2)})} = 2\cdot(9\cdot4)\cdot(35\cdot16)\cdot(135\cdot64) = 348\,364\,800$, then $\abs{P} = 2\cdot 348\,364\,800 = 696\,729\,600 = \abs{W(E_8)}$ and $\abs{\Orth(q_{T_\Co})} = 527\cdot256\cdot 348\,364\,800 = 46\,998\,591\,897\,600 = 2^{21}3^55^27\cdot17\cdot31$, so that
$$
\frac{\abs{\Orth(q_{T_\Co})}}{\abs{P}} = 2^7\cdot17\cdot31 = 67\,456 .
$$
Both computations are in `computations/reports/coble_788-gamma-co-images-index-run.txt`, which also verifies the quadratic-form relation on all $2^{22}$ pairs, the characteristic class on all $2048$ classes, the plus type of $w^{\perp}$ and the type of the $67\,456$ complements. Since the orbit has $67\,456$ elements and the set it lies in has $67\,456$ elements, the orbit is that whole set and
$$
[\Orth(T_\Co):R_{\gent}] = [\Orth(q_{T_\Co}):P] = 2^7\cdot17\cdot31 = 67\,456 .
$$
The number is published, and the two orders are the two in the source: [@Ste91, Rem. 2.12, printed p. 8] computes $[\Orth(L_-):\Gamma] = (2^{21}3^55^27\cdot17\cdot31)/(2\cdot2^{13}3^55^27) = 2^7\cdot17\cdot31$, and $[\Orth(L_-):\Gamma] = [\Orth(q_{T_\Co}):P]$ because $\kappa$ identifies $A_{T_\En}$ with $A_{E_{10}(2)}$ and carries $M$ to $P$ (@lem:gluing-discriminant-identification(2), (3), with the restriction $\Orth(q_{T_\Co})\iso\Orth(q_{E_{10}(2)})$ of @lem:coble-discriminant-blocks(3)), the lattice $L_-$ of the source being $T_\En$ summand by summand (@prop:sterk-group-identification(1)), and $\Gamma$ is $\gent$, whose discriminant image is $M = P$. The same number is the index in $\Orth^+$: the vector $\zeta\definedas h$ is primitive of square $2$, so $s_\zeta\in\ker\bar\rho\subseteq R_{\gent}$ and $s_\zeta\notin\Orth^+(T_\Co)$ (@prop:gamma-co-reflective-set(2), which proves both halves for a primitive vector of square $2$). The first holds because $s_\zeta(x^*) - x^* = -b(x^*,\zeta)\zeta$ lies in $T_\Co$ for every $x^*\in T_\Co^*$, a reflection in a vector of square $2$ being discriminant-trivial; the second because $\spinornorm_\bR(s_\zeta) = [-\tfrac12\zeta^2] = [-1]$ is not the identity (@prop:gamma-co-reflective-set(2), @def:spinor-norm). Hence $R_{\gent}\cdot\Orth^+(T_\Co) = \Orth(T_\Co)$, and
$$
[\Orth^+(T_\Co):R_{\gent}\intersect\Orth^+(T_\Co)] = [\Orth(T_\Co):R_{\gent}] = 67\,456 .
$$
:::

::: {.remark #rmk:gamma-co-images-inputs title="What each step of @prop:gamma-co-images needs, and where it stands"}

Each step of the proof above rests on a statement that the step itself does not prove. The eleven such statements are listed below with the step that uses each and with its status; *proved* means proved on this page, and the numbered source is the numbered statement that supplies the mathematical content, with its section. The list is the check that no step carries more than it says.

1. *$T_\Co$ is even, of signature $(2,9)$ and $2$-elementary with $a = 11$.* Needed in Step 1 (for $q$ to take values in $\tfrac12\bZ/2\bZ$), Step 0 ($\abs{A_{T_\Co}} = 2^{11}$) and Step 3 (the three hypotheses of Nikulin's theorem). Status: proved --- @prop:theta-co-exists with the table of the notation block at the head of this chapter; the isometry class is [@DK13, (3.6), printed p. 513] and [@Nik80, Thm. 3.6.2, printed p. 144].
2. *$H = \generators{(h/2,\delta/2)}$ is isotropic.* Needed in Step 0: otherwise $(T_\Co\perp\generators{\delta})_H$ is not even and Nikulin's gluing theorem does not apply to it. Status: proved --- the one congruence displayed in Step 0.
3. *$[h/2]$ is the characteristic class of $q_{T_\Co}$, i.e. $b(h/2,x)\equiv q(x)\pmod1$ for all $x$.* Needed in Step 2, where the lifting condition becomes automatic, and hence in (2). Status: published --- [@Nik80, §3.9, printed pp. 149--150] proves existence and uniqueness of the characteristic element of an even $2$-elementary form and its additivity over orthogonal sums; Step 1 identifies it with $[h/2]$ on the two summands, and @lem:coble-discriminant-blocks(3) proves the same thing in the shape $k\perp A^0$.
4. *$b$ is nondegenerate on $A_{T_\Co}$.* Needed in Step 1 for the uniqueness of the characteristic class, and so for the passage from (2) to (3). Status: published --- the discriminant form of a nondegenerate lattice is nondegenerate [@Nik80, §1.3, printed p. 109].
5. *$\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is onto.* Needed in Step 3 and in Step 6, and it is what turns "every isometry of the discriminant form" into "every isometry of the lattice". Status: published --- [@Nik80, Thm. 3.6.3, printed p. 144] = @thm:two-elementary-surjectivity, the hypotheses being verified in Step 3.
6. *$\gent$ is the group of [@AEGS25, Def. 2.6, printed p. 587], and that group is the set of isometries of $T_\En$ whose discriminant action preserves the two summands $A_{U(2)}$, $A_{E_8(2)}$.* Needed in Step 5: without it $R_{\gent}$ is the image of a group that has not been identified with the group of the published degree-two family. Status: page proof --- @prop:sterk-group-identification(1), (2), resting on [@AEGS25, Defs. 2.6--2.7, printed p. 587] and [@Ste91, Prop. 2.7, printed p. 6]. This is the step that identifies the group of the published degree-two Enriques family; it is a statement about an arithmetic group, and the monodromy group $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5) is a different group, no inclusion between it and $R_{\gent}$ being asserted here.
7. *$\Orth^+$ is the kernel of the real spinor norm, and the spinor norm is multiplicative on an orthogonal sum, so $\spinornorm_\bR(\varphi\perp\id) = \spinornorm_\bR(\varphi)$.* Needed in Step 4 for the sign. It cannot be replaced by an argument about positive definite subspaces: $\delta^2<0$ does not put every maximal positive definite subspace of $T_\En\tensor\bR$ inside $\delta^{\perp}$, since $\eta(h)$ and $e'+f'+\delta$ span one with $(e'+f'+\delta,\delta) = -2$. Status: definition plus the reflection formula of @def:spinor-norm, and multiplicativity is what the exact sequence of @def:lattice-spinor-kernels asserts.
8. *The restriction $\Stab_{\Orth(T_\En)}(\delta)\to\Orth(T_\Co)$ is injective.* Needed for an equality, not only an inclusion, in (2) and (3): an isometry fixing $\delta$ and acting trivially on $\delta^{\perp T_\En}$ is the identity. Status: proved --- Step 2, where the scalar extension of $g$ is $\varphi\oplus\id$.
9. *The line stabilizer $\Stab_{\gent}(\ZZ\delta)$ and the vector stabilizer $\Stab_{\gent}(\delta)$ have the same image in $\Orth(T_\Co)$.* Needed only if the statement is read with the root fixed up to sign, which is how the stabilizer of a root class is usually written; with $\delta$ fixed as a vector, as in (2) and (3), it is not needed. Status: page proof --- the proof of @lem:coble-monodromy-in-stabilizer: if $\rho(\gamma)\delta = -\delta$ then $s_\delta\rho(\gamma)$ fixes $\delta$, and $s_\delta$ acts as the identity on $\delta^{\perp T_\En}$.
10. *$w^{\perp} = [h/2]^{\perp}$ is of plus type, and $[h/2]$ generates a direct summand of $A_{T_\Co}$.* Needed in Step 6, both for the count of the $527$ classes and for reading $\Orth(q_{T_\Co})\to\Orth(w^{\perp},q)$ as an isomorphism. Status: proved --- Step 1 and @lem:coble-discriminant-blocks(2), (3).
11. *The gluing identification $\kappa\colon A_{E_{10}(2)}\isoto A_{T_\En}$ is defined and is an isometry, it carries the two summands of $A_{E_{10}(2)}$ to those of $A_{T_\En}$, and $\varphi\oplus\id$ acts on $A_{T_\En}$ by $\bar\rho(\varphi)$.* Needed in Steps 2, 4, 5 and 6: it is what makes "$A_{E_{10}(2)}$" and "$A_{T_\En}$" the same object, hence what turns the vanishing of the discriminant action of $g$ into a condition on $\bar\rho(\varphi)$, and what transfers Sterk's group $M$ and its index to $P$. Status: proved --- @lem:gluing-discriminant-identification(1)--(4), which proves the bijectivity, the isometry, the two summands and the action formula from the gluing datum of @def:gamma-co-groups.

*The statements that the issue names.* The issue names four of Nikulin's; the proof uses three of them, and the fourth is read and recorded below as not needed. A fifth, Proposition 1.5.1, is the gluing theorem that Step 0 rests on. Proposition 1.5.1 is on the page as @thm:nikulin-gluing; Corollary 1.5.2 is the automorphism-lifting criterion used in Steps 2 and 5 and in @lem:gluing-discriminant-identification(4), on the page as @thm:automorphism-lifting-criterion; Theorem 3.6.2 is item 1 (the isometry class of an even $2$-elementary lattice by its invariants); Theorem 3.6.3 is item 5. The fourth of the issue's, **Theorem 1.14.4** of [@Nik80, §1.14], is **not used** by the proof, and it is recorded here so that its absence is a statement and not an omission. It is the analogue of Witt's theorem: for an even lattice $M$ of signature $(t_{(+)},t_{(-)})$ and an even unimodular lattice $L$ of signature $(l_{(+)},l_{(-)})$, there is a *unique* primitive embedding $M\into L$ provided (1) $l_{(+)}-t_{(+)}>0$ and $l_{(-)}-t_{(-)}>0$, (2) $l_{(+)}-t_{(+)} + l_{(-)}-t_{(-)}\geq 2 + \ell(A_{M_p})$ for every $p\neq2$, and (3) if that difference equals $\ell(A_{M_2})$ then $q_M\cong u_+^{(2)}(2)\oplus q'$ or $q_M\cong v_+^{(2)}(2)\oplus q'$. [@AEGS25, Lemma 2.4, printed p. 586], on the page as @lem:enriques-embedding-chain, invokes it for the uniqueness of the embedding $U(2)\oplus E_8(2)\into L$ of the Enriques theory, into the even unimodular lattice $(3,19)$: the three conditions hold there, $(1)$ as $3-1 = 2>0$ and $19-9 = 10>0$, $(2)$ as $12\geq 2+0$ for odd $p$, and $(3)$ is vacuous because $12\neq\ell(A_{M_2}) = 10$. The uniqueness that @prop:gamma-co-images(2) asserts is *not* an instance of it and does not need it: there the embedding $\eta$ is given, and uniqueness is injectivity of the restriction $\Stab_{\Orth(T_\En)}(\delta)\to\Orth(T_\Co)$ (item 8), while existence is Corollary 1.5.2. An embedding-uniqueness theorem about $M\into L$ with $L$ unimodular says nothing about which isometries of a fixed $\delta^{\perp}$ lift, which is what the proposition is about.

Two consequences are worth separating from the proposition. First, (2) is stronger than an existence statement for extensions: the extension of $\varphi\in\Orth(T_\Co)$ is not merely some isometry of $T_\En$ fixing a chosen root whose orthogonal complement is $T_\Co$, it is $\varphi\oplus\id_{\generators{\delta}}$, so the extension is a homomorphism and $\Stab_{\Orth(T_\En)}(\delta)$ is its graph. Second, the number in (3) is a lattice index: it says nothing about the degree of $\bD(T_\Co)/\Gamma_{\Co,2}\to\bD(T_\Co)/\Orth(T_\Co)$, which is a statement about the monodromy group and is left open by @qst:coble-monodromy-equality.
:::

::: {.lemma #lem:coble-family-identification title="The family identification (F) from the universal family over the Heegner divisor"}

In the situation of @lem:coble-monodromy-in-stabilizer, assume

(U) the degree-$2$ Coble family over $\Delta$ and its marking are defined: the family is the restriction to $\Delta$ of the universal family of K3 surfaces with the Enriques involution over the moduli stack of degree-$2$ numerically polarized Enriques surfaces, whose coarse space is $F_{\En,2}$ [@AEGS25, introduction, printed p. 583, printed p. 612, and Defs. 2.5--2.7, printed p. 587]; $\Gamma_{\Co,2}$ is its monodromy group on the local system with fibre $T_\Co$ (@def:gamma-co-groups(5)); and on every fibre the covering involution has invariant lattice $S_\Co$, spanned by the classes of $E_0,\dots,E_{10}$ [@DK13, §3, printed p. 513].

Then (F) holds: the local system with fibre $T_\Co$ is the $\delta^{\perp}$-part of the restriction to $\Delta$ of the local system with fibre $T_\En$.

(U) is **not available in this book**: no definition of the degree-$2$ Coble family, or of its marking, is given here, and supplying them is D2 of research#786. The ambient half is AEGS's universal family of Enriques surfaces over the moduli stack, quoted in the proof; the Coble half is the quotient over $\Delta$, which is what the missing definition has to make into a moduli functor.
:::

::: {.proof}

*The ambient family.* [@AEGS25, printed p. 612] constructs it: "Consider the universal family $(X,\epsilon R)\to F(2,2,0)$ of KSBA-stable pairs over the compactified moduli stack. ... the pullback of the universal family $(X_B,\epsilon R_B)\to B$ is a family whose general fiber is a pair $(X,\epsilon R)$ of an Enriques K3 surface ... Taking the quotient gives a family $(Z,\epsilon R_Z)\to B$ over a compact base, extending the universal family of Enriques surfaces ... By Lemma 2.8, the normalization $B^\nu$ of $B$ is a compactification of $F_{\En,2}$ admitting a universal family of pairs. So we have a classifying morphism $B^\nu\to F_{\En,2}$." Over the preimage of $\Delta$ the K3 fibres are nodal, and their quotients are the Coble surfaces [@AEGS25, the paragraph after Def. 2.7, printed p. 587]. That is the family of the lemma at the level of the finite cover $B^\nu$; read on the moduli stack, of which $F_{\En,2}$ is the coarse space, it is the universal family, and $\Gamma_{\Co,2}$ is the monodromy of that family.

*The fibre marking.* On a fibre the covering involution has invariant lattice $M_X = S_\Co$, spanned by the classes of $E_0,\dots,E_{10}$, and anti-invariant lattice $N_X = T_\Co$ [@DK13, (3.6), printed p. 513; @prop:coble-cover-marking].

*The covering involution is the reflection twist.* With that marking the involution acts on $H^2(X_b)\cong\lkt$ as $I_\Co = -\theta_\Co$ [@prop:coble-cover-marking]. The reflection twist $w_\alpha I_\En$ of @cons:reflection-twist has the same two eigenspaces, $S_\En\oplus\Z\alpha = S_\Co$ and $\alpha^{\perp T_\En} = T_\Co$ [@prop:coble-eigenspaces, @prop:coble-transcendental]. Two involutions of $L_{K3}$ with the same $(\pm1)$-eigenspaces coincide, so the covering involution is $w_\alpha I_\En$ on every fibre, and, the classes $e_0,\dots,e_{10}$ being canonical sections, as a family.

*Conclusion.* The local system with fibre $T_\Co$ of the Coble family is the anti-invariant local system $L_{K3}^{I_\Co=-1}$ of that involution, whose fibre is $\alpha^{\perp T_\En} = \delta^{\perp T_\En}$ [@prop:coble-eigenspaces]. That is (F).
:::

::: {.remark #rmk:coble-family-identification-status title="Where the two halves of the identification come from"}
The ambient family is [@AEGS25, printed p. 612], at the level recorded in @rmk:coble-universal-family-level; the fibre marking is [@DK13, §3, printed p. 513] and @prop:coble-cover-marking. Neither is a definition of the degree-$2$ Coble family as a moduli functor, which is (U) and is D2 of research#786. The one thing neither paper writes as a single statement is the pair for $\Delta$: [@AEGS25, printed p. 587] identifies the *points* of $\Delta$ with the Coble quotients and [@DK13, printed p. 513] describes the covers fibre by fibre. The rank of the period lattice, $11$ [@DK13, (3.6), printed p. 513], is the rank of the classical family, which is what makes the identification the right one.
:::

::: {.remark #rmk:coble-universal-family-level title="At which level the universal family over $F_{\En,2}$ exists"}
[@AEGS25, introduction, printed p. 583] announces "a description of $F_{\En,2}$ and its universal family", and the body states the level at which the family is constructed: "Consider the universal family $(X,\epsilon R)\to F(2,2,0)$ of KSBA-stable pairs over the compactified moduli stack. ... By Lemma 2.8, the normalization $B^\nu$ of $B$ is a compactification of $F_{\En,2}$ admitting a universal family of pairs. So we have a classifying morphism $B^\nu\to F_{\En,2}$" [@AEGS25, printed p. 612]. The same paper says that $F_{\En,2}$ itself is coarse: "the complement of the discriminant divisor in $F_{\En,2}=D(T_\En)/\Gamma_{\En,2}$ is the coarse moduli space of Enriques surfaces with a numerical polarization of degree 2" [@AEGS25, printed p. 587].

So the universal family exists over the moduli stack, of which $F_{\En,2}$ is the coarse space, and over the finite cover $B^\nu$; it is not a family over $F_{\En,2}$ as a scheme, and what the paper gives over $F_{\En,2}$ is the classifying morphism $B^\nu\to F_{\En,2}$. The family of @lem:coble-family-identification is therefore the restriction of the universal family at the level of the stack, equivalently of the finite cover $B^\nu$; it is not a family over the coarse space $F_{\En,2}$, and $\Gamma_{\Co,2}$ is the monodromy of the family at that level (@def:gamma-co-groups(5)).
:::

::: {.lemma #lem:coble-monodromy-in-stabilizer title="The monodromy of the degree-$2$ Coble family lies in the stabilizer of $\delta$"}

Let $\Delta\subset F_{\En,2} = \bD(T_\En)/\gent$ be the discriminant divisor, the image of $\alpha^{\perp}\subset\bD(T_\En)$ [@AEGS25, Def. 2.7 and the paragraph after it, printed p. 587], whose points parameterize quotients of nodal K3 surfaces by an involution fixing a node, these quotients being rational Coble surfaces with a $(1,1)/4$-singularity. Let $\delta$ be the $(-2)$-vector of [@DK13, the sentence after Prop. 3.2, printed p. 513] --- a representative of the class $\alpha$ of [@AEGS25, printed p. 587] --- and let $T_\Co = N_X = M_X^{\perp}$ be the transcendental lattice of the K3 double cover $X$ of a Coble surface [@DK13, (3.6), printed p. 513], which is $\delta^{\perp T_\En}$. Let $\Gamma_{\Co,2}$ be the monodromy group of @def:gamma-co-groups(5) for the K3 covers over $\Delta$, and assume

(F) the local system with fibre $T_\Co$ of that family is the $\delta^{\perp}$-part of the restriction to $\Delta$ of the local system with fibre $T_\En$.

The identification of the points of $\Delta$ with the Coble quotients is [@AEGS25, printed p. 587]; (F) is the family-level statement, and it is @lem:coble-family-identification under its hypothesis (U), which is D2 of research#786. Under (F),
$$\Gamma_{\Co,2}\subseteq R_{\gent}.$$
:::

::: {.proof}

*The periods lie in $\delta^{\perp}$ and fill it.* For a fibre $X_b$ of the family over $\Delta$ the period $[\omega_b]$ lies in $\bD(T_\Co)$, because $T_\Co = M_X^{\perp}$ is the transcendental lattice of $X_b$ [@DK13, (3.6), printed p. 513]. Since $T_\Co = \delta^{\perp T_\En}$ [@DK13, the sentence after Prop. 3.2, printed p. 513], one has $[\omega_b]\in\bD(\delta^{\perp})\subset\bD(T_\En)$. The image of the marked period map is the preimage of $\Delta$, and $\Delta$ is by definition the image of $\alpha^{\perp}$ in $\bD(T_\En)/\Gamma_\En$ [@AEGS25, Def. 2.7, printed p. 587]; that preimage is a union of components of $\bD(\delta^{\perp})$, hence open in it. This is where the definition of $\Delta$ as a period divisor is used, and no Torelli theorem is invoked.

*The monodromy preserves the line $\ZZ\delta$.* Transport is an isometry of $T_\En$, and the period map is equivariant, $\Phi(\gamma\tilde b) = \rho(\gamma)\Phi(\tilde b)$ (@eq-period-map-equivariance), so $\rho(\gamma)$ carries the image $\Phi(\widetilde\Delta)$ of the period map to itself. Its image is open in $\bD(T_\Co)$ by the previous paragraph. For an isometry $g$ one has $g\,\bD(\delta^{\perp}) = \bD((g\delta)^{\perp})$; the two closed analytic hypersurfaces $\bD(\delta^{\perp})$ and $\bD((\rho(\gamma)\delta)^{\perp})$ of $\bD(T_\En)$ meet in the nonempty open subset $\Phi(\widetilde\Delta)$, hence coincide, so $(\rho(\gamma)\delta)^{\perp} = \delta^{\perp}$ and $\rho(\gamma)\delta = \pm\delta$.

*The image lies in $R_{\gent}$.* Hence $\rho(\gamma)$ lies in the line stabilizer $\Stab_{\gent}(\ZZ\delta)$, and its restriction to $\delta^{\perp} = T_\Co$ is the image of an element of that stabilizer. The line stabilizer and the vector stabilizer have the same image in $\Orth(T_\Co)$: if $\rho(\gamma)\delta = -\delta$ then $s_\delta\rho(\gamma)$ fixes $\delta$, and $s_\delta$ acts as the identity on $\delta^{\perp}$; and $s_\delta\in\ker\rho_{T_\En}\subseteq\gent$, because $\delta$ lies in the unimodular summand $U$ of $T_\En$ and $s_\delta$ therefore acts trivially on $A_{T_\En}$. So the image of $\Stab_{\gent}(\ZZ\delta)$ is the image of $\Stab_{\gent}(\delta)$, which is $R_{\gent}$ (@def:gamma-co-groups(4), @prop:gamma-co-images(3)).
:::

::: {.theorem #thm:coble-monodromy-versus-enriques title="The monodromy of the degree-$2$ Coble family against the Enriques stabilizer"}

Let $\Gamma_{\Co,2}$ be the monodromy group of @def:gamma-co-groups(5), and let
$$
R\definedas R_{\gent} = \bar\rho^{-1}(P)\leq\Orth(T_\Co)
$$
be the image of $\Stab_{\gent}(\delta)$ in $\Orth(T_\Co)$, with $P$ the stabilizer of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ (@prop:gamma-co-images(3)). Let $\zeta\in T_\Co$ be a primitive vector of square $2$ and $s_\zeta$ its reflection (@prop:gamma-co-reflective-set).

1. $\Gamma_{\Co,2}\subseteq\Orth^+(T_\Co)$.
2. $s_\zeta\in\ker\bar\rho\subseteq R$ and $s_\zeta\notin\Orth^+(T_\Co)$ (@prop:gamma-co-reflective-set(2)). Hence $R\not\subseteq\Orth^+(T_\Co)$,
$$
R = (R\intersect\Orth^+(T_\Co))\sqcup s_\zeta\,(R\intersect\Orth^+(T_\Co)),
\qquad
[R:R\intersect\Orth^+(T_\Co)] = 2,
\qquad
[\Orth(T_\Co):R\intersect\Orth^+(T_\Co)] = 134\,912.
$$
3. $\Gamma_{\Co,2}\neq R$: the equality $\Gamma_{\Co,2} = R_{\gent}$ is false.
4. $\Gamma_{\Co,2}\subseteq R\intersect\Orth^+(T_\Co) = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co) = \Gamma^{\mathrm{dir}}_{\Co,2} = \Gamma^{\mathrm{Hdg}}_{\Co,2}$: the second inclusion is @lem:coble-monodromy-in-stabilizer, conditional on (U) of @lem:coble-family-identification, the first is (1), and the equalities are @prop:direct-eq-heegner. For the degree-$2$ Coble data of @prop:one-node-family the reverse inclusion holds as well, so there the orbifold monodromy group equals $R\intersect\Orth^+(T_\Co)$ (@prob:B25, @thm:sign-is-isotropy), the loop monodromy over the coarse moduli space being its quotient by $\theset{\pm\id}$ (@thm:no-loop-carries-the-sign).
:::

::: {.proof}

For (1). @lem:monodromy-is-spinor-positive proves, for the monodromy group of a family of Coble surfaces whose periods lie in one component of $\bD(T_\Co)$, the containment $\Gamma_\Co\subseteq\Orth^+(T_\Co)=\Theta_\bR(T_\Co)$; its proof uses only that the period map of the family is single-valued on a connected base and carries the periods into one component, and it applies verbatim to the degree-$2$ family, whose local system of lattices is again the $T_\Co$ local system of a family of Coble surfaces. Equivalently, the periods lie in a connected component of the period domain and $\rho(\gamma)$ preserves it (@eq-period-map-equivariance, @cor:vhs-monodromy-stabilizes-component).

For (2). $\zeta$ is primitive of square $2$, so $s_\zeta$ is an integral isometry lying in $\ker\bar\rho$ and outside $\Orth^+(T_\Co)$: this is @prop:gamma-co-reflective-set(2), whose proof computes $\spinornorm_\bR(s_\zeta) = [-\tfrac12\zeta^2] = [-1]$. Since $\ker\bar\rho\subseteq\bar\rho^{-1}(P) = R$ (@prop:gamma-co-images(3)), $s_\zeta\in R$. A subgroup of index two is the kernel of a homomorphism onto $\ZZ/2$, so $R\intersect\Orth^+(T_\Co)$ has index two in $R$ and the nontrivial coset is $s_\zeta(R\intersect\Orth^+(T_\Co))$. The index $[\Orth(T_\Co):R] = 67\,456$ is @prop:gamma-co-images(3), and $134\,912 = 2\cdot 67\,456$.

For (3). By (1) every element of $\Gamma_{\Co,2}$ lies in $\Orth^+(T_\Co)$, and by (2) $s_\zeta\in R$ does not; hence $\Gamma_{\Co,2}\neq R$.

For (4). The inclusion $\Gamma_{\Co,2}\subseteq R_{\gent}$ is @lem:coble-monodromy-in-stabilizer, conditional on its input (F), and $\Gamma_{\Co,2}\subseteq\Orth^+(T_\Co)$ is (1); the equalities of the chain are @prop:direct-eq-heegner. For the family of @prop:one-node-family the monodromy preserves the quadruple $(S_\Co,S_{\mathrm{dP}},H,\alpha)$ (@cor:construction-monodromy), so its image lies in $\Gamma^{\mathrm{dir}}_{\Co,2} = R_{\gent}\intersect\Orth^+(T_\Co)$, and the reverse inclusion there is @prob:B25 with @thm:sign-is-isotropy.
:::

::: {.question #qst:coble-monodromy-equality title="Is the monodromy of the degree-$2$ Coble family the whole arithmetic model?"}

Is $\Gamma_{\Co,2} = R_{\gent}\intersect\Orth^+(T_\Co)$? The inclusion $\Gamma_{\Co,2}\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$ is @thm:coble-monodromy-versus-enriques(4), from @lem:coble-monodromy-in-stabilizer, conditional on (U) of @lem:coble-family-identification; (U) and (F) are D2 of research#786. The reverse inclusion is the assertion that every congruence isometry of $T_\Co$ in $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ is realised by monodromy; by @lem:coble-monodromy-reverse-reduction it is equivalent to $\bar\rho(\Gamma_{\Co,2}) = P$ and $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$. It holds for the degree-$2$ Coble data of the direct construction, where it is @prob:B25, whose proof rests on the period computation of @prob:B24 and not on a printed theorem; no printed statement supplies it for the degree-$2$ Coble family of @lem:coble-monodromy-in-stabilizer, and it is the degree-$2$ analogue of the reverse inclusion of @conj:gamma-co-stable. The equality $R_{\gent} = \Gamma_{\Co,2}$ of research#779 is false either way (@thm:coble-monodromy-versus-enriques(3)).
:::

::: {.lemma #lem:coble-monodromy-reverse-reduction title="The reverse inclusion splits into a discriminant surjectivity and the stable group"}

Let $\Gamma_{\Co,2}$ be the monodromy group of @def:gamma-co-groups(5), so that $\Gamma_{\Co,2}\subseteq\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(1)), and let $R_{\gent} = \bar\rho^{-1}(P)$ (@prop:gamma-co-images(3)). Then
$$\Gamma_{\Co,2} = R_{\gent}\intersect\Orth^+(T_\Co)$$
if and only if both

1. $\bar\rho(\Gamma_{\Co,2}) = P$, and
2. $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$.
:::

::: {.proof}
Since $R_{\gent} = \bar\rho^{-1}(P)$ and $\widetilde\Orth^+(T_\Co) = \ker\bar\rho\intersect\Orth^+(T_\Co)$, the group $R_{\gent}\intersect\Orth^+(T_\Co)$ is the preimage in $\Orth^+(T_\Co)$ of $P$.

If (1) and (2) hold and $g\in R_{\gent}\intersect\Orth^+(T_\Co)$, choose $\gamma\in\Gamma_{\Co,2}$ with $\bar\rho(\gamma) = \bar\rho(g)$, which (1) permits; then $g\gamma^{-1}\in\Orth^+(T_\Co)$ and $\bar\rho(g\gamma^{-1}) = \id$, so $g\gamma^{-1}\in\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$ by (2), and $g\in\Gamma_{\Co,2}$.

Conversely, if $\Gamma_{\Co,2} = R_{\gent}\intersect\Orth^+(T_\Co)$, then (2) holds because $\widetilde\Orth^+(T_\Co)\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$, and (1) holds because $\bar\rho$ carries $R_{\gent}\intersect\Orth^+(T_\Co)$ onto $P$: $\bar\rho$ is onto (@thm:two-elementary-surjectivity), and if $x\in\bar\rho^{-1}(g)$ lies outside $\Orth^+(T_\Co)$ then $-x$ lies in it and $\bar\rho(-x) = \bar\rho(x)$, because $-1$ acts trivially on the $2$-elementary group $A_{T_\Co}$.
:::

::: {.remark #rmk:coble-monodromy-reverse-status title="Where the two halves of the reverse inclusion stand"}
(2) is the reverse inclusion of @conj:gamma-co-stable with $\Gamma_{\Co,2}$ in place of $\Gamma_\Co$: every stable isometry is realised by monodromy. It would follow from $W(T_\Co) = \widetilde\Orth^+(T_\Co)$ together with $W(T_\Co)\subseteq\Gamma_{\Co,2}$, the containment that @prop:monodromy-contains-root-reflections derives from the meridian hypothesis (@rmk:gamma-co-nodal-pair-proposal); the index $[\widetilde\Orth^+(T_\Co):W(T_\Co)]$ is @qst:gamma-co-reflection-index and is not known.

(1) needs monodromy elements whose discriminant action is nontrivial, and the Picard--Lefschetz reflections do not supply them: a reflection in a vector of square $-2$ acts trivially on $A_{T_\Co}$, while the reflection in a $(-4)$-class acts nontrivially (@prop:gamma-co-reflective-set(2),(3)) and arises as the product of two commuting nodal reflections (@rmk:gamma-co-nodal-pair-proposal). Whether such products generate $P$ is not known. For the degree-$2$ Coble data of @prop:one-node-family both (1) and (2) hold (@prob:B25); for the family of @lem:coble-monodromy-in-stabilizer neither is supplied by a printed source.
:::

::: {.remark #rmk:coble-monodromy-counts title="The index and the cusp counts after the correction"}
The index of the arithmetic model of the monodromy group is $[\Orth(T_\Co):R_{\gent}\intersect\Orth^+(T_\Co)] = 134\,912$, twice the $67\,456$ of @prop:gamma-co-images(3), and the degree of $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)\to\bD(T_\Co)/(R_{\gent}\intersect\Orth^+(T_\Co))$ is $\abs{W(E_8)} = 696\,729\,600$ (@thm:gamma-co-2-comparison(3), halved).

The cusp counts are unchanged. Since $\ker\bar\rho\subseteq R_{\gent}$, @thm:cusp-lifting(4) applies with $\Gamma = R_{\gent}$: parts 1--3 of that theorem hold with $\Gamma\intersect\Orth^+(T_\Co)$ in place of $\Gamma$, and the finite images $H$ and $H^+$ agree because the hypothesis $\ker\rho\subseteq\Gamma$ of its last sentence is met. Hence $R_{\gent}$ and $R_{\gent}\intersect\Orth^+(T_\Co)$ have the same orbits on the primitive isotropic vectors, on the primitive isotropic planes and on the flags. Two witnesses of the kind that proof uses lie in $\ker\bar\rho$ and outside $\Orth^+(T_\Co)$: the reflection $s_\zeta$ in the square-$2$ vector $\zeta$ fixes the primitive isotropic vector $e'$ of the $U(2)$ summand, and $\tau\definedas\id_{\generators{h}}\oplus(-\id_{U(2)})\oplus\id_{E_8(2)}$ fixes the primitive isotropic plane $\generators{e',\,2h+y}$ for $y = \alpha+\beta$ with $\alpha,\beta$ orthogonal roots of $E_8(2)$; both are integral involutions acting trivially on $A_{T_\Co}$, and $\spinornorm_\bR(\tau) = [(-1)^1] = [-1]$ by @lem:minus-identity-spinor-norm, $\tau$ being $-\id$ on the rank-two summand $U(2)$ of positive index one (@prop:gamma-co-reflective-set(2) for $s_\zeta$); `computations/reports/coble_779-monodromy-vs-enriques-run.txt` checks the two isometries, the plane and the triviality of both actions on $A_{T_\Co}$. Hence the four $0$-cusps of @prop:coble-cong-point-stabilizer(3) and the seven $1$-cusps of @thm:plane-fibre(3) are counts for $R_{\gent}\intersect\Orth^+(T_\Co)$ as well as for $R_{\gent}$, and they are counts for $F_{\Co,2}$ exactly when @qst:coble-monodromy-equality holds.
:::

::: {.remark #rmk:gamma-co-counts title="The cusp counts name their group"}
The quotient $F^{\mathrm{un}}_\Co = \bD(T_\Co)/\Orth(T_\Co)$ has one $0$-cusp, $\Orth^+(T_\Co)$ being transitive on the primitive isotropic vectors (@thm:unpolarized-cusps), computed by the $\Orth(T_\Co)$ rows of run 43556671111 (@rmk:coble-plane-incidence-rows), and one $1$-cusp, by @thm:plane-transitivity-tco, certified by the same rows. The stable quotient $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ has $527$ $0$-cusps (@thm:coble-zero-cusp-count(2)) and $189\,720$ $1$-cusps, one fibre of eight over each of the $23\,715$ liftable classes (@thm:plane-fibre(3)). The subgroup $R_{\gent} = \bar\rho^{-1}(P)$ has four orbits of primitive isotropic vectors (@prop:coble-cong-point-stabilizer(3)) and seven orbits of primitive isotropic planes, proved by the integral decorated-plane lifting and finite $G_\Co$-orbit calculation of @cor:coble-heegner-integral-plane-descent and independently reproduced by that run's row (@thm:plane-fibre(3), @rmk:coble-plane-incidence-rows); by @rmk:coble-monodromy-counts the same orbits are those of $R_{\gent}\intersect\Orth^+(T_\Co)$, so $\bD(T_\Co)/(R_{\gent}\intersect\Orth^+(T_\Co))$ has four $0$-cusps and seven $1$-cusps, and $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$ has these counts exactly when @qst:coble-monodromy-equality holds; the subgroup-orbit operation, which would count these for a prescribed subgroup rather than for $\Orth(T_\Co)$, is sage-extensions#286, and no count on this page is read off it. Each of these counts is a count of lattice orbits and not only of finite ones: every group named in this paragraph contains $\widetilde\Orth^+(T_\Co)$, so by @thm:coble-integral-lifting-fibre(1), (2) the fibre over one finite datum is a single orbit and contributes one.

The cusp counts of $\fco$ are the counts for the stable subgroup: $\fco=\bD(T_\Co)/\Gamma_\Co$ has the coarse space of $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable), hence $527$ $0$-cusps (@thm:coble-zero-cusp-count(2)) and $189\,720$ $1$-cusps (@thm:plane-fibre(3)). The one $0$-cusp and one $1$-cusp of $F^{\mathrm{un}}_\Co=\bD(T_\Co)/\Orth(T_\Co)$ are the counts of the tautological local system over the coarse space (@thm:gamma-co-is-full), which is not $\Gamma_\Co$, and those of the unlabelled base are the counts for $\Gamma_{10A_1}$, which are not computed on this page.

[@DK13, Prop. 3.2, p. 513] gives the moduli space as an open subset of the quotient by $\Orth(N)$, and the sentence after it states that the quotient of the $(-2)$-Heegner divisor by $\Orth(U\oplus E(2))$ is birational to that moduli space. By @thm:normalization for $\Gamma = \Gamma^K_\En$ the normalization of that second quotient is $\bD(T_\Co)/R_{\Gamma^K_\En}$, and $R_{\Gamma^K_\En} = \Orth(T_\Co)$ by @prop:gamma-co-images(2), in agreement with the first.
:::

::: {.theorem #thm:normalization}

Let $\Gamma$ be one of $\Gamma_\En = \widetilde\Orth^+(T_\En)$, $\Gamma^K_\En = \Orth(T_\En)$, $\gent$, and let $R_\Gamma$ be the restricted stabilizer of @def:gamma-co-groups, identified in @prop:gamma-co-images. Write $F^{\Gamma}_\Co\definedas\bD(T_\Co)/R_\Gamma$. Then the map induced by the embedding $\eta$ of @lem:primitive_embedding_eta,
$$
f^{\Gamma}\colon F^{\Gamma}_\Co = \bD(T_\Co)/R_\Gamma \too \bD(\ten)/\Gamma,
$$
is defined and finite, its image is the Heegner divisor $\mch_{-2}/\Gamma$, and $f^{\Gamma}$ is birational; hence $F^{\Gamma}_\Co$ is the normalization of that divisor.
:::

::: {.proof}

That $f^{\Gamma}$ is defined is @prop:gamma-co-images: restriction carries $\Stab_{\Gamma}(\delta)$ onto $R_\Gamma$, so the containment required by the descent criterion (@rmk:descent-of-an-equivariant-inclusion) holds, with equality. The target is the period quotient $\bD(\ten)/\Gamma$ and not the complement $(\bD(\ten)\sm\mch_{-2})/\Gamma$ of @sec-moduli-construction: every period of $T_\Co$ is orthogonal to $\delta = \tilde e-\tilde f$, a vector of square $-2$, so the image of $f^{\Gamma}$ lies in the Heegner divisor $\mch_{-2}/\Gamma$ and does not meet its complement. Nothing below uses more about $R_\Gamma$ than that it is this image, so the argument runs for each $\Gamma$. It has three steps: finiteness of the fibres, properness, and generic injectivity.

Fibres.
For $x = [\omega]\in\bD(T_\En)$ let $T(x)$ be the smallest primitive sublattice of $T_\En$ whose complexification contains $\omega$, namely $T(x)\definedas\bigl(T_\En\intersect\omega^{\perp_{T_\En\tensor_\ZZ\CC}}\bigr)^{\perp T_\En}$.
For a primitive sublattice $M\leq T_\En$ of signature $(2,\ast)$ one has $x\in\bD(M)$ if and only if $T(x)\iscontainedin M$.

Fix $y\in\bD(\ten)/\Gamma$ and a lift $\tilde y\in\bD(T_\En)$.
A point of $\inverseof{f^{\Gamma}}(y)$ is a $R_\Gamma$-orbit of a point $x = g\tilde y$ with $g\in\Gamma$ and $x\in\bD(T_\Co)$.
Writing $M'\definedas \inverseof{g}(T_\Co)$, that last condition says $T(\tilde y)\iscontainedin M'$.
Now $M'^{\perp T_\En} = \inverseof{g}(\ZZ\delta) = \ZZ v$ with $v^2 = -2$, and $v\perp T(\tilde y)$.
The space $T(\tilde y)\tensor_\ZZ\RR$ contains a positive definite plane and $T_\En$ has signature $(2,10)$, so $T(\tilde y)^{\perp T_\En}$ is negative definite and contains only finitely many vectors of square $-2$.
Each such $v$ determines $M' = v^{\perp T_\En}$, so only finitely many $M'$ occur.
For a fixed $M'$ the elements $g$ with $\inverseof{g}(T_\Co) = M'$ form one coset of $\Stab_{\Gamma}(\delta)$, whose restrictions to $T_\Co$ all lie in $R_\Gamma$ by @prop:gamma-co-images; the corresponding points $x$ therefore form a single $R_\Gamma$-orbit.
Hence $\inverseof{f^{\Gamma}}(y)$ is finite, of cardinality at most half the number of $(-2)$-vectors of $T(\tilde y)^{\perp T_\En}$.

Properness and finiteness.
By @lem:locally_closed_embedding_BB, the map $f^{\Gamma}$ extends to a morphism $\bar f^{\Gamma}\colon\overline{F^{\Gamma}_\Co}^{\operatorname{BB}}\to \overline{\bD(\ten)/\Gamma}^{\operatorname{BB}}$ of projective varieties, which is therefore proper.
A boundary component of $\overline{F^{\Gamma}_\Co}^{\operatorname{BB}}$ is indexed by a primitive isotropic sublattice $I\leq T_\Co$ of rank $1$ or $2$, and the saturation of $I$ in $T_\En$ is again primitive isotropic of the same rank.
So $\bar f^{\Gamma}$ carries boundary to boundary, giving $\inverseof{\bar f^{\Gamma}}(\bD(\ten)/\Gamma) = F^{\Gamma}_\Co$, and $f^{\Gamma}$ is proper because properness is stable under base change.
A proper morphism with finite fibres is finite ([@stacks-02LS]), so $f^{\Gamma}$ is finite.
Let $Z\definedas f^{\Gamma}(F^{\Gamma}_\Co)$, which is closed because a finite morphism is closed.

Generic injectivity.
A proper primitive sublattice $S\subsetneq T_\Co$ of signature $(2,\ast)$ cuts out a proper closed analytic subset $\bD(S)\subsetneq\bD(T_\Co)$, and there are countably many such $S$.
So the set of $x\in\bD(T_\Co)$ with $T(x) = T_\Co$ is the complement of countably many proper closed analytic subsets, hence dense.
For such an $x$ the fibre computation allows only $M' = T_\Co$: one has $T_\Co = T(x)\iscontainedin M'$ with both primitive of rank $11$.
The fibre through $x$ is therefore a single point.
The locus where a finite morphism of irreducible varieties has more than its generic number of preimages is a proper closed subset, and a dense set is not contained in one, so $f^{\Gamma}$ has degree $1$ and is birational.

Finally $F^{\Gamma}_\Co$ is normal, being the quotient of a bounded symmetric domain by a properly discontinuous group of automorphisms.
A finite birational morphism from a normal variety onto a reduced irreducible variety is its normalization, so $F^{\Gamma}_\Co$ is the normalization of $Z$.
:::

::: {.remark #rmk:normalization-enriques-analogue title="The Enriques case"}

For Enriques surfaces, $\fentwo$ is the normalization of a closed subvariety of $\fttz$ [@AEGS25 Lem. 2.8, printed p. 587].
:::

::: {.proposition #prop:sterk-group-identification title="The discriminant image of $\gent$"}

Let $\rho\colon\Orth(\ten)\to\Orth(A_{\ten}, q_{\ten})$ be the discriminant representation and $K = \ker\rho$.
Identify $\ten = U\oplus U(2)\oplus E_8(2)$ with the lattice $L_- = \mathbf H\oplus\mathbf H(2)\oplus E_8(-2)$ of [@Ste91, §2] summand by summand, and let $e', f'$ be the isotropic basis of $U(2)$, with $(e', f') = 2$.

1. $\gent$ is the group $\Gamma$ of [@Ste91, §2], and $\gent = \theset{g\in\Orth(\ten) \st \rho(g)\text{ preserves the summands } A_{U(2)} \text{ and } A_{E_8(2)} \text{ of } A_{\ten}}$.
2. $\rho(\gent) = M\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$, and $\gent = \rho^{-1}(M)$; in particular $K\subseteq\gent$.
3. $\gent$ is a proper subgroup of $\Stab_{\Orth(\ten)}\bigl([(e'+f')/2]\bigr)$.
:::

::: {.proof}

(1) The group $\Gamma$ of [@Ste91, §2] is the image in $\Orth(L_-)$ of the isometries of the K3 lattice that commute with the Enriques involution and fix the polarization vector, and $\gent$ is the image in $\Orth(\ten)$ of the same group [@AEGS25 Def. 2.6, printed p. 587].
The description by the two summands is [@Ste91, Prop. 2.7, printed p. 6].

(2) Because $U$ is unimodular, $A_{\ten} = A_{U(2)}\perp A_{E_8(2)}$, and an isometry of $q_{\ten}$ preserves both summands exactly when it is a pair of isometries of the summands.
So (1) says $\gent = \rho^{-1}(M)$.
The lattice $\ten$ is even, indefinite and $2$-elementary, so $\rho$ is surjective (@thm:two-elementary-surjectivity), and $\rho(\gent) = M$.

(3) The three nonzero classes of $A_{U(2)}$ are $[e'/2]$, $[f'/2]$ and $[(e'+f')/2]$, with $q$-values $0$, $0$ and $(e'+f')^2/4 = 1$.
So every element of $\Orth(q_{U(2)})$ fixes $[(e'+f')/2]$, and $\gent$ stabilizes it by (2).
Since $f'\in\ten$, the classes $[(e'+f')/2]$ and $[(e'-f')/2]$ are equal.
The isometry $\psi\in\Orth(L_-)$ of [@Ste91, Rem. 2.8, printed p. 7] stabilizes $\tfrac12(e'-f')+L_-$ and is not in $\Gamma$.
:::

::: {.proposition #prop:gamma-en-two-index title="The index of $\gent$"}

With $\rho$, $K$ and $M$ as in @prop:sterk-group-identification,
$$
[\Orth(\ten) : \gent] \;=\; [\Orth(A_{\ten},q_{\ten}) : M] \;=\; 2^7\cdot 17\cdot 31 \;=\; 67\,456 .
$$
:::

::: {.proof}

By @prop:sterk-group-identification, $\gent = \rho^{-1}(M)$ and $\rho$ is surjective, so $\rho$ induces a bijection $\Orth(\ten)/\gent\to\Orth(A_{\ten},q_{\ten})/M$.
Because $U$ is unimodular, $A_{\ten} = A_{E_{10}(2)}$, so $\abs{\Orth(A_{\ten},q_{\ten})} = 2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31$ by @prop:coble-discriminant-group.
By @prop:gamma-en-two-gluing, $M = \rho(\gent)$ is the $\gamma$-transport of the image of $\Stab_{\Orth(\sen)}(h)$ in $\Orth(q_{\sen})$, which has order $\abs{W(E_8)} = 2^{14}\cdot3^5\cdot5^2\cdot7$ by @thm:coble-heegner-finite-orbits(1).
The quotient of the two orders is $2^7\cdot17\cdot31$.
This is the index computed in [@Ste91, Rem. 2.12, printed p. 8].
:::

::: {.proposition #prop:ten-plane-classes title="The two classes of primitive isotropic planes of $\ten$"}

Write $e,f$ for the isotropic basis of $U$ and $e',f'$ for that of $U(2)$, with $(e,f) = 1$ and $(e',f') = 2$.
Identify the summand $E_8(2)$ with $E_8 = \theset{y_0\in\ZZ^8\cup(\ZZ^8+s) \st \textstyle\sum_i y_{0,i}\in2\ZZ}$, $s = \tfrac12(1,\dots,1)$ [@CS10, Ch. 4, §8.1], so that $y\leftrightarrow y_0$ and $(y,y') = -2\,y_0\cdot y_0'$.
Let $\alpha\in E_8(2)$ correspond to $2e_1$, and put $z\definedas 2e+2f+\alpha$.
For a primitive totally isotropic plane $\varPi\subseteq\ten$ let $D(\varPi)\leq A_{\ten}$ be the image of $\varPi_\QQ\cap\ten^*$, as in @not:isotropic-reduction-setup.

1. $\varPi_1 = \generators{e,e'}$ and $\varPi_2 = \generators{z,e'}$ are primitive totally isotropic planes.
   Every primitive totally isotropic plane $\varPi$ is $\Orth(\ten)$-equivalent to exactly one of them, and to $\varPi_1$ exactly when it contains a vector of divisibility one.
2. If $\varPi$ contains a vector of divisibility one, then $D(\varPi)$ has order $2$, its nonzero element is $[v/2]$ for every primitive $v\in\varPi$ of divisibility two, and $\varPi^\perp/\varPi\cong E_8(2)$.
3. If $\varPi$ contains no vector of divisibility one, then $D(\varPi)$ has order $4$, its three nonzero elements are the classes $[p/2]$ of the primitive $p\in\varPi$, and $\varPi^\perp/\varPi\cong D_8^*(2)$, where $D_8^*$ carries the negative of the Euclidean form.
:::

::: {.proof}

(1) The vectors $e$, $e'$ and $z$ are isotropic and pairwise orthogonal: $(2e+2f)^2 = 8$ and $\alpha^2 = -2\cdot4 = -8$.
The vector $\alpha/2$ corresponds to $e_1\notin E_8$, so $z$ is primitive in $U\oplus E_8(2)$, and $e'$ is primitive in $U(2)$; a span of primitive vectors of two orthogonal summands is primitive in their sum, so $\varPi_2$ is primitive, and so is $\varPi_1$.
The vector $e$ has divisibility one.
For a primitive $az+be'\in\varPi_2$, the ideal $(az+be',\ten)$ contains $(az+be',f) = 2a$ and $(az+be',f') = 2b$, and it lies in $2\ZZ$ because $(z,\ten)$ and $(e',\ten)$ do; so $az+be'$ has divisibility two.
By [@Ste91, Prop. 4.6, printed p. 29] there are exactly two $\Orth(\ten)$-classes of primitive isotropic planes, and divisibility is invariant under $\Orth(\ten)$, so $\varPi_1$ and $\varPi_2$ represent the two classes.

(2), (3): the subgroup $D(\varPi)$.
$A_{\ten}$ has exponent two, so $2\ten^*\subseteq\ten$, and primitivity of $\varPi$ gives $\varPi_\QQ\cap\ten^*\subseteq\tfrac12(\varPi_\QQ\cap\ten) = \tfrac12\varPi$.
A vector $p/2$ with $p\in\varPi$ lies in $\ten^*$ exactly when $(p,\ten)\subseteq 2\ZZ$, and $[p/2] = 0$ exactly when $p\in 2\varPi$.
So $D(\varPi)$ is the image of $\theset{p\in\varPi \st (p,\ten)\subseteq 2\ZZ}$ in $\varPi/2\varPi$.
If $\varPi$ contains a vector of divisibility one, then by (1) it is the image of $\varPi_1$ under an isometry, so it has a basis $u, v$ with $\operatorname{div}(u) = 1$ and $\operatorname{div}(v) = 2$.
Then $(au+bv,\ten)\subseteq 2\ZZ$ exactly when $a$ is even, so $D(\varPi) = \theset{0,[v/2]}$; a primitive $au+bv$ with $a$ even has $b$ odd and the class $[v/2]$.
If $\varPi$ contains no vector of divisibility one, then every $p\in\varPi$ has $(p,\ten)\subseteq 2\ZZ$, so $D(\varPi) = \varPi/2\varPi$ has order $4$, and its nonzero elements are the classes of the primitive vectors.

(2), (3): the quotients.
An isometry carrying $\varPi$ to $\varPi'$ induces an isometry $\varPi^\perp/\varPi\to\varPi'^\perp/\varPi'$, so by (1) it suffices to compute the quotients for $\varPi_1$ and $\varPi_2$.
Write $x = ae+bf+ce'+df'+y$ with $y\in E_8(2)$.
Then $(x,e) = b$ and $(x,e') = 2d$, so $\varPi_1^\perp = \ZZ e\oplus\ZZ e'\oplus E_8(2)$ and $\varPi_1^\perp/\varPi_1\cong E_8(2)$.

For $\varPi_2$, one has $(y,\alpha) = -4y_{0,1}$, so $x$ is orthogonal to $e'$ exactly when $d = 0$, and orthogonal to $z$ exactly when $2a+2b-4y_{0,1} = 0$, that is $a+b = 2y_{0,1}$.
So $\varPi_2^\perp = \ZZ e'\oplus W$ with $W = \theset{ae+bf+y \st a+b = 2y_{0,1}}$, and $z\in W$, so $\varPi_2^\perp/\varPi_2 = W/\ZZ z$.
For $x = ae+bf+y\in W$ put $u\definedas a - y_{0,1}$, so that $a = y_{0,1}+u$ and $b = y_{0,1}-u$, and define the linear map
$$
\pi\colon W\too\QQ^8,\qquad ae+bf+y\longmapsto(u, y_{0,2},\dots,y_{0,8}).
$$
Then $x^2 = 2ab + y^2 = 2(y_{0,1}^2-u^2) - 2\abs{y_0}^2 = -2\abs{\pi(x)}^2$, so $(x,x') = -2\,\pi(x)\cdot\pi(x')$.
If $\pi(x) = 0$, then $y_0 = y_{0,1}e_1\in E_8$ forces $y_{0,1} = 2k$ with $k\in\ZZ$, so $a = b = 2k$, $y = k\alpha$ and $x = kz$; hence $\ker\pi = \ZZ z$.
The image of $\pi$ is $\ZZ^8\cup(\ZZ^8+s)$.
It is contained in this set, because $u$ and $y_{0,1}$ are both integers or both in $\ZZ+\tfrac12$.
For $(u,y')\in\ZZ^8\cup(\ZZ^8+s)$ choose $y_{0,1}$ in $\ZZ$ or in $\ZZ+\tfrac12$, matching $u$, with $y_{0,1}+\sum_j y'_j$ even; then $y_0 = (y_{0,1},y')\in E_8$, the numbers $a = y_{0,1}+u$ and $b = y_{0,1}-u$ are integers, and $\pi(ae+bf+y) = (u,y')$.
The set $\ZZ^8\cup(\ZZ^8+s)$ is $D_8^*$ [@CS10, Ch. 4, §7.1], so $\pi$ induces an isometry $\varPi_2^\perp/\varPi_2\cong D_8^*(2)$.

There is also a direct obstruction to a third, trivial-discriminant stratum, independent of the classification in (1). Reduce $N=U\perp U(2)\perp E_8(2)$ modulo $2N$. The alternating form induced by its integral pairing is supported entirely on $U/2U$, where it is nondegenerate of dimension two. For a primitive totally isotropic plane $\varPi$, primitivity gives an injection $\varPi/2\varPi\injects N/2N$. Its image is isotropic for the mod-two pairing, so its projection onto $U/2U$ has dimension at most one. Consequently a nonzero class of $\varPi/2\varPi$ has zero $U/2U$-projection. Choose a primitive lift $p\in\varPi$ of that nonzero parity class (any nonzero element of $\F_2^2$ lifts to a primitive vector of $\ZZ^2$). Its $U$-coordinates are even, while all pairings in the other two summands are even, so $(p,N)\subseteq2\ZZ$ and $p/2\in N^*$. The class $[p/2]\in A_N$ is nonzero: otherwise $p\in2N$, and primitivity of $\varPi$ would give $p\in2\varPi$, contrary to its nonzero parity class. In particular $D(\varPi)$ is **never trivial**: the zero-dimensional finite discriminant stratum cannot lift to a primitive isotropic plane. The other two strata are realized by $\varPi_1$ and $\varPi_2$, and all their finite subgroups are realized by the transitivity and surjectivity arguments of @thm:enriques-degree-two-arithmetic(2).
:::

::: {.lemma #lem:half-vector-eichler title="Eichler transvections along a vector of divisibility two"}

Let $A = A_{\ten}$ with its discriminant quadratic form $q$ of @def:discriminant.
Then $q([x/2]) = x^2/4\bmod 2$, so $(A, q)$ is a quadratic space over $\F_2$, with polar form $\beta_q([x/2],[y/2]) = (x,y)/2\bmod 2$.
Let $d\in A$ be isotropic and nonzero, and for $c\in d^\perp$ define
$$
T_{d,c}(a)\definedas a+\beta_q(a,d)\,c+\bigl(\beta_q(a,c)+q(c)\,\beta_q(a,d)\bigr)\,d .
$$
Let $\eta\in\ten$ be a primitive isotropic vector of divisibility two with $[\eta/2] = d$.

1. For $w\in\ten^*$ with $(w,\eta) = 0$, the Eichler--Siegel transvection $E_{\eta,w}$ of @def:eichler-siegel lies in $\Orth(\ten)$, fixes $\eta$, maps every primitive totally isotropic plane that contains $\eta$ onto itself, and satisfies $\rho(E_{\eta,w}) = T_{d,[w]}$.
2. Every $c\in d^\perp$ is $[w]$ for some $w\in\ten^*$ with $(w,\eta) = 0$.
3. $c\mapsto T_{d,c}$ is a homomorphism $d^\perp\to\Orth(A,q)$ with kernel $\generators{d}$; its image $U_d$ has order $2^8$.
4. Each $T_{d,c}$ fixes $d$ and acts trivially on $d^\perp/\generators{d}$.
   If $D\ni d$ is an isotropic subgroup, then $T_{d,c}$ acts trivially on $D^\perp/D$, and trivially on $D$ when $c\in D^\perp$.
:::

::: {.proof}

Squares of vectors of $\ten^* = U\oplus\tfrac12U(2)\oplus\tfrac12E_8(2)$ are integers: $(ae'+bf')^2/4 = ab$, and $y^2/4 = -\abs{y_0}^2/2\in\ZZ$ for $y\in E_8(2)$ in the coordinates of @prop:ten-plane-classes.
For $x/2\in\ten^*$ and $t\in\ten$ one has $(x+2t)^2/4 = x^2/4+(x,t)+t^2$ with $(x,t)+t^2\in2\ZZ$, so $q([x/2]) = x^2/4\bmod 2$ is well defined, and $\beta_q$ is its polar form because $(x+y)^2/4 = x^2/4+y^2/4+(x,y)/2$.

(1) For $x\in\ten$ one has $(\eta,x)\in2\ZZ$ and $2w\in\ten$, so $(\eta,x)w\in\ten$; also $(w,x)\in\ZZ$ and $\tfrac12 w^2(\eta,x)\in\ZZ$.
So the formula of @def:eichler-siegel maps $\ten$ into $\ten$.
$E_{\eta,w}$ is an isometry of $\ten_\QQ$, so $E_{\eta,w}(\ten)$ has the discriminant of $\ten$ and $E_{\eta,w}(\ten) = \ten$.
For $p\perp\eta$ the formula reads $E_{\eta,w}(p) = p-(w,p)\eta$; so $E_{\eta,w}$ fixes $\eta$ and maps a totally isotropic plane $\varPi\ni\eta$ into itself, and onto itself because $E_{\eta,w}|_\varPi$ is unipotent.
For the discriminant action let $x'\in\ten^*$ represent $a\in A$.
Then $(\eta,x')\equiv\beta_q(a,d)$, $2(w,x')\equiv\beta_q(a,[w])$ and $w^2\equiv q([w])$ modulo $2$.
The formula gives
$$
E_{\eta,w}(x') = x' + (\eta,x')\,w - \bigl(2(w,x')+w^2(\eta,x')\bigr)\tfrac{\eta}{2} .
$$
The two coefficients are integers, $2w\in\ten$ and $\eta\in\ten$, so modulo $\ten$ only their residues modulo $2$ matter, and $A$ has exponent two.
So $\rho(E_{\eta,w})(a) = T_{d,[w]}(a)$.

(2) Let $c = [w_0]$ with $w_0\in\ten^*$.
Then $\beta_q(c,d) = (w_0,\eta)\bmod 2 = 0$, so $(w_0,\eta)\in2\ZZ = (\ten,\eta)$, and there is $t\in\ten$ with $(t,\eta) = -(w_0,\eta)$.
Then $w = w_0+t$ has $(w,\eta) = 0$ and $[w] = c$.

(3) Put $b = T_{d,c'}(a)$.
Since $\beta_q(c',d) = \beta_q(d,d) = 0$, one has $\beta_q(b,d) = \beta_q(a,d)$ and $\beta_q(b,c) = \beta_q(a,c)+\beta_q(a,d)\beta_q(c,c')$.
Substituting, and using $q(c+c') = q(c)+q(c')+\beta_q(c,c')$, gives $T_{d,c}T_{d,c'} = T_{d,c+c'}$.
$T_{d,0} = \id$, and $T_{d,d}(a) = a+\beta_q(a,d)d+\beta_q(a,d)d = a$.
Conversely, if $T_{d,c} = \id$, choose $a$ with $\beta_q(a,d) = 1$, which exists because $\beta_q$ is nondegenerate; then $c = (\beta_q(a,c)+q(c))d\in\generators{d}$.
By (1) and (2) every $T_{d,c}$ is the image of an isometry of $\ten$, so it lies in $\Orth(A,q)$.
$d^\perp$ has order $2^9$, so $U_d$ has order $2^8$.

(4) For $a\in d^\perp$ the formula reads $T_{d,c}(a) = a+\beta_q(a,c)d$, and $T_{d,c}(d) = d$.
If $D\ni d$, then $D^\perp\subseteq d^\perp$, so $T_{d,c}$ acts trivially on $D^\perp/D$.
For $a\in D$ one has $T_{d,c}(a) = a+\beta_q(a,c)d$, which is $a$ when $c\in D^\perp$.
:::

::: {.lemma #lem:ten-base-stabilizers title="The stabilizers of $\ZZ e$, $\ZZ e'$ and $\generators{e,e'}$"}

With the notation of @prop:ten-plane-classes and @lem:half-vector-eichler, put $d_1 = [e'/2]$ and $F_1 = \Stab_{\Orth(A,q)}(d_1)$.
Then $\abs{F_1} = 89\,181\,388\,800$, and
$$
\rho\bigl(\Stab_{\Orth(\ten)}(\ZZ e)\bigr) = \Orth(A,q),\qquad
\rho\bigl(\Stab_{\Orth(\ten)}(\ZZ e')\bigr) = \rho\bigl(\Stab_{\Orth(\ten)}(\varPi_1)\bigr) = F_1 .
$$
:::

::: {.proof}

*The line $\ZZ e$.* The isometries $\id_U\oplus g$ with $g\in\Orth(\sen)$, $\sen = U(2)\oplus E_8(2)$, fix $e$, and they act on $A = A_{\sen}$ through $g$.
$\sen$ is even, indefinite and $2$-elementary, so $\Orth(\sen)\to\Orth(A,q)$ is surjective (@thm:two-elementary-surjectivity).

*The order of $F_1$.* $A = A_{U(2)}\perp A_{E_8(2)}$ is the group $A^0$ of @lem:coble-discriminant-blocks, and $\Orth(A,q)$ is transitive on its $527$ nonzero isotropic elements (@lem:coble-discriminant-blocks(2)).
So $\abs{F_1} = 2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31/527 = 89\,181\,388\,800$.

*The line $\ZZ e'$ and the plane $\varPi_1$.*
An isometry that stabilizes $\ZZ e'$ fixes $[\pm e'/2] = d_1$, and an isometry that stabilizes $\varPi_1$ fixes the nonzero element $d_1$ of $D(\varPi_1)$ (@prop:ten-plane-classes(2)).
So both images lie in $F_1$.
Let $S_0\leq\Orth(\ten)$ be the group generated by the isometries $\id_{U\oplus U(2)}\oplus w$ with $w\in\Orth(E_8(2)) = W(E_8)$ and the transvections $E_{e',w}$ of @lem:half-vector-eichler(1).
Each generator fixes $e'$ and stabilizes $\varPi_1$, so $\rho(S_0)$ lies in both images.

Let $L = \rho\bigl(\theset{\id\oplus w \st w\in W(E_8)}\bigr)$.
In the coordinates of @prop:ten-plane-classes, $A_{E_8(2)} = \tfrac12E_8(2)/E_8(2)$ is $E_8/2E_8$, and $\id\oplus w$ acts as the identity on $A_{U(2)}$ and as the reduction $\bar w$ of $w$ on $E_8/2E_8$.
By @lem:weyl-E8-mod-two, $w\mapsto\bar w$ has kernel $\theset{\pm\id}$, so $\abs{L} = \abs{W(E_8)}/2 = 348\,364\,800$.

The group $U_{d_1}$ of @lem:half-vector-eichler lies in $\rho(S_0)$ by @lem:half-vector-eichler(1) and (2), and it has order $2^8$.
Since $d_1^\perp = \generators{d_1}\perp A_{E_8(2)}$, the quotient $d_1^\perp/\generators{d_1}$ is $A_{E_8(2)}$, on which $\id\oplus w$ acts by $\bar w$ and $U_{d_1}$ acts trivially (@lem:half-vector-eichler(4)).
So $L\cap U_{d_1} = 1$, and $\rho(S_0)\supseteq L\,U_{d_1}$ has at least $348\,364\,800\cdot 2^8 = 89\,181\,388\,800 = \abs{F_1}$ elements.
Hence $\rho(S_0) = F_1$, and both images equal $F_1$.
:::

::: {.lemma #lem:line-stabilizer-image title="The stabilizer of a primitive isotropic line maps onto the stabilizer of its class"}

For a primitive isotropic $v\in\ten$ let $c(\ZZ v) = [v/\operatorname{div}(v)]\in A_{\ten}$; it does not depend on the sign of $v$, because $A_{\ten}$ has exponent two.
Let $\Gamma\leq\Orth(\ten)$ contain $K$, and put $H = \rho(\Gamma)$.
Then
$$
\rho\bigl(\Stab_{\Orth(\ten)}(\ZZ v)\bigr) = \Stab_{\Orth(A,q)}\bigl(c(\ZZ v)\bigr),
\qquad
\rho\bigl(\Stab_{\Gamma}(\ZZ v)\bigr) = \Stab_{H}\bigl(c(\ZZ v)\bigr).
$$
:::

::: {.proof}

For $g\in\Orth(\ten)$ one has $c(g\ZZ v) = \rho(g)\,c(\ZZ v)$, because $g$ preserves divisibility.
By [@Ste91, Prop. 4.5, printed p. 28] there is $g\in\Orth(\ten)$ with $g\ZZ v_0 = \ZZ v$ for $v_0 = e$ or $v_0 = e'$.
Conjugation by $g$ carries $\Stab_{\Orth(\ten)}(\ZZ v_0)$ to $\Stab_{\Orth(\ten)}(\ZZ v)$, and conjugation by $\rho(g)$ carries the stabilizer of $c(\ZZ v_0)$ to the stabilizer of $c(\ZZ v)$.
The first equality holds for $v_0$ by @lem:ten-base-stabilizers, because $c(\ZZ e) = 0$ and $c(\ZZ e') = d_1$.

For the second, the inclusion $\subseteq$ is clear.
Let $h\in\Stab_H(c(\ZZ v))$.
By the first equality $h = \rho(s)$ with $s\in\Stab_{\Orth(\ten)}(\ZZ v)$, and $h = \rho(\gamma)$ with $\gamma\in\Gamma$.
Then $s\gamma^{-1}\in K\subseteq\Gamma$, so $s\in\Stab_\Gamma(\ZZ v)$.
:::

::: {.theorem #thm:sterk-line-fibres title="Primitive isotropic lines up to a discriminant preimage"}

Let $\Gamma\leq\Orth(\ten)$ contain $K$, and put $H = \rho(\Gamma)$.
Two primitive isotropic lines $\ell,\ell'\subseteq\ten$ are $\Gamma$-equivalent if and only if $c(\ell')\in H\,c(\ell)$.
:::

::: {.proof}

If $\ell' = \gamma\ell$ with $\gamma\in\Gamma$, then $c(\ell') = \rho(\gamma)c(\ell)$.
Conversely let $c(\ell') = h\,c(\ell)$ with $h\in H$.
The class $c(\ell)$ is $0$ exactly when $\operatorname{div}(\ell) = 1$, so $\ell$ and $\ell'$ have the same divisibility, and by [@Ste91, Prop. 4.5, printed p. 28] there is $g\in\Orth(\ten)$ with $g\ell = \ell'$.
Then $h^{-1}\rho(g)$ fixes $c(\ell)$, so by @lem:line-stabilizer-image $h^{-1}\rho(g) = \rho(s)$ with $s\in\Stab_{\Orth(\ten)}(\ell)$.
The element $\gamma = gs^{-1}$ carries $\ell$ to $\ell'$ and has $\rho(\gamma) = h$, so $\gamma\in\rho^{-1}(H) = \Gamma$.
:::

::: {.theorem #thm:enriques-integral-plane-stabilizers title="The stabilizers of primitive isotropic planes of $\ten$"}

For every primitive totally isotropic plane $\varPi\subseteq\ten$,
$$
\rho\bigl(\Stab_{\Orth(\ten)}(\varPi)\bigr) = \Stab_{\Orth(A,q)}\bigl(D(\varPi)\bigr).
$$
Let $\Gamma\leq\Orth(\ten)$ contain $K$, put $H = \rho(\Gamma)$ and $\Gamma^+ = \Gamma\cap\Orth^+(\ten)$.
Then:

1. $\rho(\Stab_\Gamma(\varPi)) = \rho(\Stab_{\Gamma^+}(\varPi)) = \Stab_H(D(\varPi))$;
2. two primitive totally isotropic planes $\varPi,\varPi'$ are $\Gamma$-equivalent if and only if $D(\varPi')\in H\,D(\varPi)$.
:::

::: {.proof}

For $g\in\Orth(\ten)$ one has $D(g\varPi) = \rho(g)D(\varPi)$, so, as in the proof of @lem:line-stabilizer-image, it suffices by @prop:ten-plane-classes(1) to prove the first equality for $\varPi_1$ and $\varPi_2$.
For $\varPi_1$ it is @lem:ten-base-stabilizers, since $D(\varPi_1) = \generators{d_1}$.

Let $D = D(\varPi_2) = \theset{0, d_1, d_2, d_1+d_2}$ with $d_1 = [e'/2]$ and $d_2 = [z/2]$, let $F = \Stab_{\Orth(A,q)}(D)$ and $S = \rho(\Stab_{\Orth(\ten)}(\varPi_2))\subseteq F$.

*The order of $F$.* The group $A$ is $A^0$ of @lem:coble-discriminant-blocks, so $A_{T_\Co} = \ZZ k\perp A$, and restriction is an isomorphism $\Orth(q_{A_{T_\Co}})\to\Orth(A,q)$ (@lem:coble-discriminant-blocks(3)).
The isotropic subgroups of order $4$ of $A_{T_\Co}$ lie in $k^\perp = A$ (proof of @prop:coble-planecusp-finite(2)), so they are the isotropic subgroups of order $4$ of $A$.
By @prop:coble-planecusp-finite(4), $\abs F = 1\,981\,808\,640 = 6\cdot 40\,320\cdot 2^{13}$.

Consider the homomorphism $\Phi\colon S\to\GL(D)\times\Orth(D^\perp/D)$.

*The Levi part.* Let $R$ be the set of the following vectors of $\varPi_2^\perp$, in the coordinates of @prop:ten-plane-classes: $r = y$ with $y_0 = \pm e_i\pm e_j$ and $2\leq i<j\leq 8$; and $r = 2ue+y$ with $u = \pm1$ and $y_0 = ue_1\pm e_j$, $2\leq j\leq 8$.
Each $r$ has $r^2 = -4$, $(r,\ten)\subseteq2\ZZ$ and $(r,e') = (r,z) = 0$, so the reflection $s_r(x) = x+\tfrac12(x,r)\,r$ lies in $\Orth(\ten)$ and fixes $\varPi_2$ pointwise.
So $s_r\in\Stab_{\Orth(\ten)}(\varPi_2)$, and $\rho(s_r)$ acts trivially on $D\subseteq\tfrac12\varPi_2/\varPi_2$.
The map $\pi$ of @prop:ten-plane-classes sends $R$ bijectively onto the $112$ roots $\pm e_i\pm e_j$ of $D_8$, and since $(x,r) = -2\,\pi(x)\cdot\pi(r)$, the vector $\pi(s_r x)$ is the Euclidean reflection of $\pi(x)$ in $\pi(r)$.
So the $s_r$ induce $W(D_8)$ on $\varPi_2^\perp/\varPi_2\cong D_8^*(2)$.
The discriminant group of $D_8^*(2)$ is $\tfrac12D_8/D_8^*$, which multiplication by $2$ identifies with $D_8/2D_8^*$; and $2D_8^*$ is the set of integral vectors whose coordinates all have the same parity.
Sign changes act trivially on $D_8/2D_8^*$, since $x-\varepsilon x$ has even coordinates.
The kernel of $S_8\to\Aut(D_8/2D_8^*)$ is normal in $S_8$ and contains neither the transposition $(1\,2)$ nor the $3$-cycle $(1\,2\,3)$, because they move $e_1+e_3$ and $e_1+e_4$, respectively, by $e_2-e_1\notin2D_8^*$; so it is trivial.
Hence the $s_r$ induce a group of order $8! = 40\,320$ on the discriminant group of $\varPi_2^\perp/\varPi_2$.
By @cor:isotropic-reduction-stabilizer(2), the isomorphism $\varphi_{\varPi_2}$ of @thm:isotropic-reduction-discriminant intertwines this action with the action of $\rho(s_r)$ on $D^\perp/D$.
So $\Phi(S)\supseteq 1\times\bar R$ with $\abs{\bar R} = 40\,320$.

*The action on $D$.* By @lem:half-vector-eichler(1), $g_1 = E_{z,f'/2}$ and $g_2 = E_{e',y_s/2}$, with $y_s\in E_8(2)$ corresponding to $s$, lie in $\Stab_{\Orth(\ten)}(\varPi_2)$, and by @lem:half-vector-eichler(4) they act trivially on $D^\perp/D$.
One has $g_1(e') = e'-\tfrac12(f',e')z = e'-z$, and $g_2(z) = z-\tfrac12(y_s,\alpha)e' = z+e'$ because $(y_s,\alpha) = -2\,s\cdot2e_1 = -2$.
So $\rho(g_1)$ fixes $d_2$ and sends $d_1$ to $d_1+d_2$, and $\rho(g_2)$ fixes $d_1$ and sends $d_2$ to $d_1+d_2$; these two transvections generate $\GL(D)\cong\GL_2(\F_2)$.
So $\Phi(S)\supseteq\GL(D)\times 1$, and $\abs{\Phi(S)}\geq 6\cdot40\,320$.

*The kernel of $\Phi$.* For $i = 1,2$ let $U_i = \theset{T_{d_i,c} \st c\in D^\perp}$.
By @lem:half-vector-eichler, with $\eta = e'$ and $\eta = z$, these lie in $\ker\Phi$, and $\abs{U_i} = \abs{D^\perp}/2 = 2^7$.
Let $T_{d_1,c} = T_{d_2,c'}$, and choose $a$ with $\beta_q(a,d_1) = 1$ and $\beta_q(a,d_2) = 0$.
Evaluating both sides at $a$ gives $c+(\beta_q(a,c)+q(c))d_1 = \beta_q(a,c')d_2$, so $c\in D$, and $T_{d_1,c}\in\theset{\id, T_{d_1,d_2}}$.
So $\abs{U_1\cap U_2}\leq2$, the set $U_1U_2$ has at least $2^{13}$ elements, and $\abs{\ker\Phi}\geq2^{13}$.

Hence $\abs S\geq 6\cdot40\,320\cdot2^{13} = \abs F$, and $S = F$.

(1) Let $h\in\Stab_H(D(\varPi))$.
By the first equality $h = \rho(s)$ with $s\in\Stab_{\Orth(\ten)}(\varPi)$, and $h = \rho(\gamma)$ with $\gamma\in\Gamma$; then $s\gamma^{-1}\in K\subseteq\Gamma$, so $s\in\Stab_\Gamma(\varPi)$.
The proof of @thm:enriques-spinor-orbit-agreement gives $k\in K\setminus\Orth^+(\ten)$ with $k\varPi = \varPi$.
Then $s$ or $sk$ lies in $\Stab_{\Gamma^+}(\varPi)$, and both have image $h$.

(2) If $\varPi' = \gamma\varPi$ with $\gamma\in\Gamma$, then $D(\varPi') = \rho(\gamma)D(\varPi)$.
Conversely let $D(\varPi') = h\,D(\varPi)$ with $h\in H$.
The two subgroups have the same order, so by @prop:ten-plane-classes the planes lie in one $\Orth(\ten)$-class, and $g\varPi = \varPi'$ for some $g\in\Orth(\ten)$.
Then $h^{-1}\rho(g)$ stabilizes $D(\varPi)$, so $h^{-1}\rho(g) = \rho(s)$ with $s\in\Stab_{\Orth(\ten)}(\varPi)$, and $\gamma = gs^{-1}\in\rho^{-1}(H) = \Gamma$ carries $\varPi$ to $\varPi'$.
:::

::: {.theorem #thm:enriques-degree-two-arithmetic title="The cusps of $\fentwo$"}

Let $M = \rho(\gent)$ as in @prop:sterk-group-identification.
Use the four $M$-orbits $A$, $B$, $C$, $D$ of nonzero isotropic elements of $A_{\ten}$ and the five $M$-orbits $AAA$, $ABC$, $ACC$, $ADD$, $CCD$ of isotropic subgroups of order $4$ of @ex:gco-finite-orbits, with $[e'/2]$, $[f'/2]$, $[(e'+f')/2]$ in place of $[u_0/2]$, $[w_0/2]$, $[h/2]$.

1. The primitive isotropic lines of $\ten$ form five $\gent$-orbits, the orbits of the vectors of [@Ste91, Prop. 4.2.3, printed p. 16]:

   | type | representative | class $c(\ZZ v)$ | $M$-orbit of the class |
   | :--- | :--- | :--- | :--- |
   | $1$ | $e$ | $0$ | $\theset{0}$ |
   | $2$ | $e'$ | $[e'/2]$ | $B$ |
   | $3$ | $e'+f'+\omega$ | $[(e'+f')/2]+[\omega/2]$ | $D$ |
   | $4$ | $e'+2f'+\alpha$ | $[e'/2]+[\alpha/2]$ | $C$ |
   | $5$ | $z = 2e+2f+\alpha$ | $[\alpha/2]$ | $A$ |

   Here $\alpha$ and $z$ are as in @prop:ten-plane-classes, and $\omega\in E_8(2)$ has $\omega^2 = -4$.
2. The primitive totally isotropic planes of $\ten$ form nine $\gent$-orbits.
   Four contain a vector of divisibility one; for them $D(\varPi) = \generators{c}$ with $c$ in $B$, $D$, $C$ or $A$.
   Five contain no vector of divisibility one; for them $D(\varPi)$ lies in $ABC$, $ACC$, $ADD$, $CCD$ or $AAA$.
3. Label a plane by the types of the primitive isotropic vectors it contains, as in [@Ste91, §4.3.15].
   The labels of the nine orbits of item 2 are, in the order listed there, $\theset{1,2}$, $\theset{1,3}$, $\theset{1,4}$, $\theset{1,5}$ and $\theset{2,4,5}$, $\theset{4,5}$, $\theset{3,5}$, $\theset{3,4}$, $\theset{5,5}$.
   A plane orbit is incident to a line orbit of type $t$ exactly when $t$ occurs in its label.
   For a primitive isotropic $v$, the planes containing $v$ correspond to the isotropic lines of $v^\perp/\ZZ v$, and their $\Stab_{\gent}(v)$-orbits correspond to the parabolic subdiagrams of rank $8$, modulo symmetry, of the Vinberg diagram of the reflection subgroup of the image of $\Stab_{\gent}(v)$ in $\Orth(v^\perp/\ZZ v)$ [@Ste91, §4.3.1--4.3.3].
   The subdiagram of each plane orbit at a vector of each type in its label is:

   | label | type $1$ | type $2$ | type $3$ | type $4$ | type $5$ |
   | :--- | :--- | :--- | :--- | :--- | :--- |
   | $\theset{1,2}$ | $\tilde E_8$ | $\tilde E_8$ | | | |
   | $\theset{1,3}$ | $\tilde E_7\oplus\tilde A_1$ | | $\tilde E_7\oplus\tilde A_1$ | | |
   | $\theset{1,4}$ | $\tilde D_8$ | | | $\tilde D_8$ | |
   | $\theset{1,5}$ | $\tilde A_7\oplus\tilde A_1$ | | | | $\tilde A_7\oplus\tilde A_1$ |
   | $\theset{2,4,5}$ | | $\tilde B_8$ | | $\tilde B_8$ | $\tilde C_8$ |
   | $\theset{4,5}$ | | | | $\tilde B_4\oplus\tilde B_4$ | $\tilde C_4\oplus\tilde C_4$ |
   | $\theset{3,5}$ | | | $\tilde B_6\oplus\tilde C_2$ | | $\tilde C_6\oplus\tilde C_2$ |
   | $\theset{3,4}$ | | | $\tilde C_8$ | $\tilde C_8$ | |
   | $\theset{5,5}$ | | | | | $\tilde B_3\oplus\tilde B_3\oplus\tilde C_2$ |
4. For a plane $\varPi$ with label $\lambda$, the intersection of the image of $\Stab_{\gent}(\varPi)$ in $\GL(\varPi)$ with $\SL(\varPi)$ is $\Gamma^1(2)$ for $\lambda = \theset{1,t}$ [@Ste91, §4.3.16]; it is $\Gamma(2)$ for $\theset{2,4,5}$, $\Gamma^1(2)$ for $\theset{4,5}$, $\theset{3,5}$ and $\theset{3,4}$, and $\SL_2(\ZZ)$ for $\theset{5,5}$ [@Ste91, §4.3.17, printed p. 27, and the proof of Prop. 4.7, printed p. 29].
5. The orbits of $\gent^+ = \gent\cap\Orth^+(\ten)$ on lines and on planes are the orbits of $\gent$.

So the Baily--Borel compactification of $\fentwo$ has five $0$-dimensional and nine $1$-dimensional boundary components, with the incidence of item 3 [@Ste91, §4.2, §4.4].
:::

::: {.proof}

$\gent = \rho^{-1}(M)$ contains $K$ (@prop:sterk-group-identification).

(1) Each representative is primitive and isotropic: $(e'+f')^2 = 4 = -\omega^2$, $(e'+2f')^2 = 8 = -\alpha^2$, and $z$ is treated in @prop:ten-plane-classes(1).
The last four pair evenly with $\ten$, and each pairs to $2$ with $e$ or $f'$, so they have divisibility two, and their classes are the displayed ones.
The class $[\omega/2]$ has $q = -1\equiv1$, and $[\alpha/2]$ has $q = -2\equiv0$ and is nonzero because $\alpha/2\notin\ten$.
So the five classes lie in the five $M$-orbits $\theset{0}$, $B$, $D$, $C$, $A$, which are all the $M$-orbits of isotropic elements.
By @thm:sterk-line-fibres the $\gent$-orbits of lines correspond to these $M$-orbits.

(2) By @thm:enriques-integral-plane-stabilizers(2), the $\gent$-orbits of planes correspond to the $M$-orbits of the subgroups $D(\varPi)$.
For a plane with a vector of divisibility one, $D(\varPi)$ has order $2$ and is generated by a nonzero isotropic element (@prop:ten-plane-classes(2)).
$\Orth(A,q)$ is transitive on the nonzero isotropic elements (@lem:coble-discriminant-blocks(2)), $\rho$ is surjective and $D(g\varPi_1) = \rho(g)D(\varPi_1)$, so every subgroup $\generators{c}$ with $c$ nonzero isotropic occurs; these form four $M$-orbits.
For a plane without such a vector, $D(\varPi)$ is isotropic of order $4$ (@prop:ten-plane-classes(3)).
$\Orth(A,q)$ is transitive on these subgroups (@prop:coble-planecusp-finite(2) and the identification in the proof of @thm:enriques-integral-plane-stabilizers), so every one occurs, and they form five $M$-orbits.
Subgroups of different orders are not $M$-equivalent, so there are nine orbits.

(3) A primitive $v\in\varPi$ of divisibility one has class $0$ and type $1$, and one of divisibility two has class $[v/2]\in D(\varPi)\setminus0$.
For a plane with a vector of divisibility one, every primitive vector of divisibility two has the class $c$ (@prop:ten-plane-classes(2)), and such vectors exist, for example $e'\in\varPi_1$.
For a plane without one, the classes of the primitive vectors are the three nonzero elements of $D(\varPi)$ (@prop:ten-plane-classes(3)).
By item 1 the type of a vector is read off from the $M$-orbit of its class, which gives the labels.
A $0$-dimensional boundary component lies in the closure of a $1$-dimensional one exactly when the line is $\gent$-equivalent to a line in the plane [@Ste91, §4.4].
The diagrams at the vectors of types $1$ to $5$ are those of [@Ste91, Figs. 5, 7, 9, 11, 13]; there are $4$, $2$, $3$, $4$ and $5$ of them, the number of labels that contain each type.
The plane orbits are matched across types in [@Ste91, §4.3.6--4.3.9].
The $\tilde E_8$ class at $e'$ is the class of $\ZZ e\oplus\ZZ e'$, the $\tilde E_8$ class at $e$ (§4.3.6), so its label is $\theset{1,2}$.
The $\tilde E_7\oplus\tilde A_1$ class at type $3$ and the $\tilde D_8$ class at type $4$ are the classes of the same diagrams at $e$, and the $\tilde C_8$ class at type $4$ is the $\tilde C_8$ class at type $3$ (§4.3.7, §4.3.8).
At type $5$, the classes $\tilde A_7\oplus\tilde A_1$, $\tilde C_8$, $\tilde C_6\oplus\tilde C_2$ and $\tilde C_4\oplus\tilde C_4$ are the classes $\tilde A_7\oplus\tilde A_1$ at type $1$, $\tilde B_8$ at type $2$, $\tilde B_6\oplus\tilde C_2$ at type $3$ and $\tilde B_4\oplus\tilde B_4$ at type $4$ (§4.3.9).
So the $\tilde A_7\oplus\tilde A_1$ class contains vectors of types $1$ and $5$, and its label is $\theset{1,5}$.
The four classes at $e$ are distinct, and the $\theset{1,2}$ class is the $\tilde E_8$ class, so the example "$\tilde A_7\oplus\tilde A_1\leftrightarrow\theset{1,2}$" of [@Ste91, §4.3.15] contradicts §4.3.6 and §4.3.9.
The remaining diagram at type $4$, $\tilde B_8$, belongs to the one remaining label containing $4$, which is $\theset{2,4,5}$; the remaining diagram at type $5$, $\tilde B_3\oplus\tilde B_3\oplus\tilde C_2$, belongs to $\theset{5,5}$.

(4) The nine labels are pairwise distinct.
The planes of [@Ste91, §4.3.16] are the planes $\ZZ e\oplus\ZZ v$ with $v$ of type $2$, $3$, $4$ or $5$, of labels $\theset{1,t}$, and the planes of [@Ste91, §4.3.17] have the five labels without $1$; the groups are computed there.

(5) This is @thm:enriques-spinor-orbit-agreement, items 1 and 2.
:::

::: {.lemma #lem:spinor-orbit-agreement title="When the orbits of a subgroup and of its spinor-positive half agree"}

Let $L$ be a lattice for which $\Orth^+(L)$ of @def:lattice-spinor-kernels has index two in $\Orth(L)$, let $\Gamma\leq\Orth(L)$ satisfy $\Gamma\not\subseteq\Orth^+(L)$, put $\Gamma^+=\Gamma\intersect\Orth^+(L)$, and let $X$ be a $\Gamma$-set.
Then $\Gamma$ and $\Gamma^+$ have the same orbits on $X$ if and only if $\Stab_\Gamma(x)\not\subseteq\Orth^+(L)$ for every $x\in X$.
:::

::: {.proof}

Since $[\Gamma:\Gamma^+]=2$, the complement $\Gamma\setminus\Gamma^+$ is a coset of $\Gamma^+$, so a product of two elements of $\Gamma\setminus\Gamma^+$ lies in $\Gamma^+$, and a product of one element of each lies in $\Gamma\setminus\Gamma^+$.

Suppose first that $\Stab_\Gamma(x)\subseteq\Orth^+(L)$ for some $x$, and choose $\gamma\in\Gamma\setminus\Gamma^+$.
If $\gamma x=\gamma' x$ with $\gamma'\in\Gamma^+$, then $\gamma'^{-1}\gamma\in\Stab_\Gamma(x)\subseteq\Orth^+(L)$, contradicting $\gamma'^{-1}\gamma\in\Gamma\setminus\Gamma^+$.
Hence $\gamma x$ lies in the $\Gamma$-orbit of $x$ but not in its $\Gamma^+$-orbit, and the orbit sets differ.

Conversely suppose $\Stab_\Gamma(x)\not\subseteq\Orth^+(L)$ for every $x$, and let $y=\gamma x$ with $\gamma\in\Gamma$.
If $\gamma\in\Gamma^+$ then $y\in\Gamma^+x$.
If not, choose $\tau\in\Stab_\Gamma(x)\setminus\Orth^+(L)$; then $\gamma\tau\in\Gamma^+$ and $\gamma\tau x=\gamma x=y$, so again $y\in\Gamma^+x$.
Every $\Gamma$-orbit is therefore a single $\Gamma^+$-orbit.
:::

::: {.theorem #thm:enriques-spinor-orbit-agreement title="Spinor agreement for every polarization family of $\ten$: isotropic lines, isotropic planes and flags"}

Let $N=\ten=U\oplus U(2)\oplus E_8(2)$ with signature $(2,10)$, let $\rho$ be its quadratic discriminant representation and $\widetilde\Orth(N)=\ker\rho$ its discriminant kernel, and let $\Gamma\leq\Orth(N)$ be a subgroup with $\widetilde\Orth(N)\subseteq\Gamma$.
Every preimage $\rho^{-1}(M)$ with $M\leq\Orth(A_\ten,q_\ten)$ is of this form.
Put $\Gamma^+=\Gamma\intersect\Orth^+(N)$.
Then $\Gamma$ and $\Gamma^+$ have the same orbits on

1. the primitive isotropic lines of $N$;
2. the primitive isotropic planes of $N$;
3. the flags $\ell\subset P$ consisting of a primitive isotropic line contained in a primitive isotropic plane.

For the lines the same holds for primitive isotropic vectors: $-\id_N$ lies in $\ker\rho$ and in $\Orth^+(N)$, being level two because $A_\ten$ is annihilated by $2$ and spinor-positive by @lem:minus-identity-spinor-norm at positive index two, so $-\id_N\in\Gamma\intersect\Gamma^+$ and the two generators of a line lie in one orbit of both groups.
:::

::: {.proof}

*Notation.*
Write $e,f$ for the hyperbolic basis of the summand $U$, $e',f'$ for that of $U(2)$, and $r_1,r_2$ for two orthogonal roots of the summand $E_8(2)$ — the roots corresponding to $e_1-e_2$ and $e_1+e_2$ in the coordinates of @prop:ten-plane-classes, of square $-4$ — with $\alpha\definedas r_1+r_2$ and $z\definedas 2e+2f+\alpha$.
Put
$$
\tau\definedas\id_U\oplus(-\id_{U(2)})\oplus\id_{E_8(2)} ,
$$
the $\tau_0$ of @lem:enriques-level-two-transvections.
By @lem:enriques-level-two-transvections, $\alpha^2=-8$, $z$ is primitive isotropic of divisibility two, and
$$
\sigma_U\definedas-\id_U\oplus\id\oplus\id,\qquad E_1\definedas E_{f,e'},\qquad E_2\definedas E_{f',e},\qquad E_3\definedas E_{f',z}
$$
are integral isometries of $N$ lying in $\ker\rho$; together with $\tau$ they satisfy $\spinornorm_\bR(\sigma_U)=\spinornorm_\bR(\tau)=-1$ and $\spinornorm_\bR(E_i)=1$.
In particular $\Gamma$ is not contained in $\Orth^+(N)$, since $\sigma_U\in\ker\rho\subseteq\Gamma$ and $\sigma_U\notin\Orth^+(N)$.

*The objects the two witnesses stabilize.*
$\tau(e)=e$, $\tau(e')=-e'$ and $\tau(z)=z$; so $\tau$ fixes the lines $\ZZ e$, $\ZZ e'$, $\ZZ z$ and stabilizes the two planes
$$
P_1\definedas\generators{e,e'},\qquad P_2\definedas\generators{z,e'}
$$
setwise.
Likewise $\sigma_U(e)=-e$ and $\sigma_U(e')=e'$, so $\sigma_U$ fixes $\ZZ e$ and stabilizes $P_1$.

*Transport.*
$\ker\rho$ is normal in $\Orth(N)$, being the kernel of a homomorphism, and $\spinornorm_\bR(gkg^{-1})=\spinornorm_\bR(g)\spinornorm_\bR(k)\spinornorm_\bR(g)^{-1}=\spinornorm_\bR(k)$.
So for $g\in\Orth(N)$ the conjugate $gkg^{-1}$ of a witness $k$ is again a witness, and it stabilizes the objects $k$ stabilizes, transported by $g$; it lies in $\Gamma$ because $\ker\rho\subseteq\Gamma$.

*The primitive isotropic lines.*
By [@Ste91, 4.5] the primitive isotropic vectors of $L_-\cong\ten$ form exactly two $\Orth$-orbits, represented by $e$ on the vectors of divisibility one and by $e'$ on those of divisibility two, and $-\id_N$ carries $v$ to $-v$; so the same holds for primitive isotropic *lines*.
Let $\ell$ be such a line.
If $\operatorname{div}(\ell)=1$, choose $g\in\Orth(N)$ with $g\ZZ e=\ell$ and put $k\definedas g\sigma_Ug^{-1}$; if $\operatorname{div}(\ell)=2$, choose $g$ with $g\ZZ e'=\ell$ and put $k\definedas g\tau g^{-1}$.
In both cases $k\in\ker\rho\setminus\Orth^+(N)$, $k\ell=\ell$, and $k\in\Gamma$.

*The primitive isotropic planes.*
By @prop:ten-plane-classes(1), $P_1 = \varPi_1$ and $P_2 = \varPi_2$ represent the two $\Orth(N)$-classes of primitive totally isotropic planes.
For a plane $P$ choose $g$ with $gP_1=P$ or with $gP_2=P$, and put $k\definedas g\sigma_Ug^{-1}$ in the first case and $k\definedas g\tau g^{-1}$ in the second; then $k\in\ker\rho\setminus\Orth^+(N)$ and $k$ stabilizes $P$.

*Conclusion.*
The hypotheses of @lem:spinor-orbit-agreement are met: $\Orth^+(\ten)$ has index two in $\Orth(\ten)$, because $\spinornorm_\bR$ is a homomorphism from $\Orth(\ten)$ to $\{\pm1\}$ with kernel $\Orth^+(\ten)$ and it is onto, $\sigma_U$ being an integral isometry of $\ten$ with $\spinornorm_\bR(\sigma_U)=-1$; and at every primitive isotropic line and at every primitive isotropic plane the stabilizer inside $\Gamma$ meets $\Gamma\setminus\Orth^+(\ten)$.
Items 1 and 2 follow on those two sets.
Item 3 is @thm:enriques-flag-witnesses, which produces such a $k$ for every flag, after which the same lemma gives item 3.
:::

::: {.lemma #lem:congruence-two-transitivity title="Level-two transitivity on the three parity classes, and the shear that leaves them"}

Let
$$
A\definedas\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
B\definedas\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad
\mu\definedas\begin{pmatrix}1&0\\1&1\end{pmatrix},
$$
let $\Gamma(2)\definedas\ker\qty(\SL_2(\bZ)\too\SL_2(\bF_2))$ act on $\bZ^2$ and on $\PP^1(\bZ)$, and let $\Lambda\definedas\generators{A,B,-\id}$.
Then $\Lambda\leq\Gamma(2)$, and for a primitive $(a,c)\in\bZ^2$:

1. there is $\lambda\in\Lambda$ with $\lambda(a,c)$ equal to $\pm(1,0)$ if $a$ is odd and $c$ even, to $\pm(0,1)$ if $a$ is even and $c$ odd, and to $\pm(1,1)$ if $a$ and $c$ are both odd;
2. every element of $\Gamma(2)$ is congruent to the identity modulo $2$ and therefore preserves the class of a vector modulo $2$ and sign, so the $\Gamma(2)$-orbits on $\PP^1(\bZ)$ are exactly the three classes $[1:0]$, $[0:1]$, $[1:1]$, and each of them is a single $\Lambda$-orbit of primitive vectors;
3. $\mu$ is not congruent to the identity modulo $2$; it carries $[1:0]$ to $[1:1]$, and fixes $[0:1]$; and every element of $\generators{\Lambda,\mu}$ preserves the parity of the first coordinate, so that $\generators{\Lambda,\mu}$ has exactly two orbits on $\PP^1(\bZ)$, the primitive lines $[a:c]$ with $a$ odd and those with $a$ even.

:::

::: {.proof}

*The three moves.*
$A^k$ and $B^k$ lie in $\Lambda$ for every $k\in\bZ$ and act by
$$
A^k\colon(a,c)\mapsto(a+2kc,\,c),\qquad
B^k\colon(a,c)\mapsto(a,\,c+2ka),
$$
while $-\id$ acts by $(a,c)\mapsto(-a,-c)$.
All three carry primitive vectors to primitive vectors, because $\gcd(a+2kc,c)=\gcd(a,c)$ and $\gcd(a,c+2ka)=\gcd(a,c)$; and all three preserve the parity type of the pair, that is each of the three alternatives of item 1.

*Odd--odd.*
Let $a$ and $c$ be odd.
Choose $k$ with $\abs{a+2kc}\leq\abs{c}$ and apply $A^k$, or symmetrically choose $k$ with $\abs{c+2ka}\leq\abs{a}$ and apply $B^k$.
Both entries remain odd, so neither can become $0$, and the maximum of the absolute values strictly decreases.
Iterating, we reach a pair on which no move reduces the maximum; such a pair has $\abs a=\abs c$, and primitivity forces $\abs a=\abs c=1$.
So the terminal pair is one of $(1,1)$, $(1,-1)$, $(-1,1)$, $(-1,-1)$.
Of these, $(-1,-1)=-\id(1,1)$ and $(-1,1)=-\id(1,-1)$ are reached from $(1,1)$ and $(1,-1)$ by $-\id$, and $B(1,-1)=(1,-1+2)=(1,1)$; so all four lie in the $\Lambda$-orbit of $(1,1)$, and no sign is left unaccounted for.

*Odd--even.*
Let $a$ be odd and $c$ even.
Reducing the larger absolute value by a multiple of twice the smaller keeps $a$ odd and $c$ even, and strictly decreases the maximum until no move reduces it; then either $\abs a=\abs c$, which the parities forbid, or an entry is $0$, which cannot be $a$.
So $c=0$ and $\abs a=1$ by primitivity, the terminal pair is $\pm(1,0)$, and $-\id$ settles the sign.

*Even--odd.*
Symmetrically, a primitive pair with $a$ even and $c$ odd is carried to $\pm(0,1)$.

*Item 2.*
Every element of $\Gamma(2)$ is congruent to the identity modulo $2$, hence acts trivially on $\bF_2^2$ and preserves the class of every vector; and by item 1 each class is a single $\Lambda$-orbit, with $\Lambda\leq\Gamma(2)$.
So no $\Gamma(2)$-orbit is a union of two classes, and the $\Gamma(2)$-orbits on primitive vectors are exactly the three classes.
Passing to lines changes nothing, since $-\id$ acts trivially on $\PP^1(\bZ)$; and the three classes are distinct because they are distinct modulo $2$.

*Item 3.*
$\mu\equiv\begin{pmatrix}1&0\\1&1\end{pmatrix}\not\equiv\id\pmod 2$, and $\mu(a,c)=(a,\,a+c)$.
For $a$ odd the second coordinate changes parity, so $\mu[1:0]=[1:1]$ and $\mu[1:1]=[1:0]$; for $a$ even $\mu$ fixes the vector $(0,c)$.
Hence $\mu$ preserves the parity of the first coordinate, and so do $A$, $B$ and $-\id$, so every element of $\generators{\Lambda,\mu}$ does.
Within the odd part $\Lambda$ is transitive on $[1:0]$ and on $[1:1]$ by item 2 and $\mu$ exchanges them, and within the even part $\Lambda$ is transitive on $[0:1]$; hence these two sets are exactly the orbits.

:::

::: {.lemma #lem:unipotent-spinor-trivial title="The normalized real spinor norm is trivial on unipotent isometries"}

Let $N$ be a nondegenerate lattice and $g\in\Orth(N_\bR)$ unipotent. Then $\spinornorm_\bR(g)=1$.
:::

::: {.proof}

Put $V\definedas N\otimes_\bZ\bR$; unipotence says that $n\definedas g-\id$ is nilpotent.
Then
$$
\nu\definedas\log g\definedas\sum_{k\geq1}\frac{(-1)^{k+1}}{k}n^k
$$
is a finite sum, hence a nilpotent endomorphism of $V$ with $\exp(\nu)=g$; both statements are the formal identities for a nilpotent endomorphism evaluated in the finite-dimensional commutative algebra $\bR[n]$.

*All real powers of $g$ are isometries.*
Put $g^t\definedas\exp(t\nu)=\sum_{k\geq0}t^k\nu^k/k!$, again a finite sum.
For integral $t$ this is the $t$-th power of $g$ and hence an isometry, so for fixed $x,y\in V$ the function $t\mapsto\beta(g^tx,g^ty)-\beta(x,y)$ is a polynomial in $t$ vanishing on $\bZ$, hence identically zero.
Thus $g^t\in\Orth(V)$ for every real $t$; and $g^sg^t$ and $g^{s+t}$ agree for integral $s,t$, so their difference, again a polynomial in $(s,t)$, vanishes identically.
Hence $t\mapsto g^t$ is a homomorphism $(\bR,+)\to\Orth(V)$ carrying $1$ to $g$.

*Conclusion.*
The composite $\chi\colon t\mapsto\spinornorm_\bR(g^t)$ is a homomorphism from $(\bR,+)$ into $\bR^\times/(\bR^\times)^2$, a group of exponent two, and $t=2\cdot(t/2)$ gives $\chi(t)=\chi(t/2)^2=1$.
Therefore $\spinornorm_\bR(g)=\chi(1)=1$.
:::

::: {.lemma #lem:enriques-level-two-transvections title="The level-two transvections of $\ten$: images, plane actions and spinor signs"}

Let $N=\ten=U\oplus U(2)\oplus E_8(2)$, with $e,f$ the hyperbolic basis of $U$, $e',f'$ that of $U(2)$, and $r_1,r_2$ two orthogonal roots of the summand $E_8(2)$ — the roots corresponding to $e_1-e_2$ and $e_1+e_2$ in the coordinates of @prop:ten-plane-classes; the summand is negative definite, so its norms lie in $4\bZ$ and its inner products in $2\bZ$.
Put $\alpha\definedas r_1+r_2$ and $z\definedas 2e+2f+\alpha$.
Then $\alpha^2=-8$, the vector $z$ is primitive isotropic of divisibility $2$, and $\beta(x,\alpha)\in2\bZ$ for every $x\in N$.

Write $E_{a,w}$ in the notation of @def:eichler-siegel — $a$ the isotropic vector, $w$ the vector orthogonal to it — so that
$$
E_{a,w}(x)=x+\beta(x,a)w-\beta(x,w)a
$$
when $w$ is isotropic as well, and put
$$
\sigma_U\definedas-\id_U\oplus\id\oplus\id,\qquad
\tau_0\definedas\id\oplus(-\id_{U(2)})\oplus\id,\qquad
E_1\definedas E_{f,e'},\qquad
E_2\definedas E_{f',e},\qquad
E_3\definedas E_{f',z}.
$$
Then:

1. These five are integral isometries of $N$, with the images
$$
\begin{aligned}
E_1&\colon e\mapsto e+e',\quad e'\mapsto e',\quad f\mapsto f,\quad f'\mapsto f'-2f,\\
E_2&\colon e\mapsto e,\quad e'\mapsto e'+2e,\quad f\mapsto f-f',\quad f'\mapsto f',\\
E_3&\colon e\mapsto e-2f',\quad f\mapsto f-2f',\quad e'\mapsto e'+2z,\quad f'\mapsto f',\quad x\mapsto x-\beta(x,\alpha)f',
\end{aligned}
$$
the last line for $x$ in the summand $E_8(2)$, on which $E_1$ and $E_2$ act identically; and the inverses
$$
E_1^{-1}=E_{f,-e'},\qquad E_2^{-1}=E_{f',-e},\qquad E_3^{-1}=E_{f',-z}
$$
are again integral isometries.
2. All five lie in $\widetilde\Orth(N)=\ker\rho$.
3. $\spinornorm_\bR(\sigma_U)=\spinornorm_\bR(\tau_0)=-1$, and $\spinornorm_\bR(E_1)=\spinornorm_\bR(E_2)=\spinornorm_\bR(E_3)=1$.
4. $E_1$, $E_1^2$ and $E_2$ stabilize $P_1=\generators{e,e'}$; $E_1$ and $E_3$ stabilize $P_2=\generators{z,e'}$; $\sigma_U$ stabilizes $P_1$; $\tau_0$ stabilizes both. For a primitive $v=ae+ce'$ of $P_1$ the divisibility is $\gcd(a,2c)$, and every primitive vector of $P_2$ has divisibility $2$.

:::

::: {.proof}

*The vector $z$.*
$r_1^2=r_2^2=-4$ and $\beta(r_1,r_2)=0$, so $\alpha^2=-8$.
Since $(2e+2f)^2=4\beta(e,f)+4\beta(f,e)=8$, we get $z^2=8-8=0$.
The pairings of $z$ are $\beta(z,e)=\beta(z,f)=2$, $\beta(z,e')=\beta(z,f')=0$ and $\beta(z,x)=\beta(\alpha,x)\in2\bZ$ for $x$ in the summand $E_8(2)$, whose bilinear form takes its values in $2\bZ$; so $(\ten,z)=2\bZ$.
If $z=my$ with $y\in N$ and $m\geq2$, comparing the $U$-components gives $m\mid2$, so $m=2$ and $\alpha/2\in E_8(2)$; but $\alpha^2/4=-2$ while every norm of that summand lies in $4\bZ$.
Hence $z$ is primitive.
Finally $\beta(x,\alpha)=0$ for $x\in U\perp U(2)$, and $\beta(x,\alpha)\in2\bZ$ for $x\in E_8(2)$.

*Integrality and the images.*
Each of the pairs $(a,w)=(f,e')$, $(f',e)$, $(f',z)$ consists of isotropic vectors with $\beta(a,w)=0$, so @def:eichler-siegel applies with the simplified formula displayed above.
Substituting the basis vectors, using $\beta(e,f)=1$, $\beta(e',f')=2$ and $\beta(e,e')=\beta(e,f')=\beta(e',f)=\beta(f,f')=0$:
$$
E_1\colon e\mapsto e+\beta(e,f)e'=e+e',\quad e'\mapsto e',\quad f\mapsto f,\quad f'\mapsto f'+\beta(f',f)e'-\beta(f',e')f=f'-2f,
$$
$$
E_2\colon e\mapsto e,\quad e'\mapsto e'+2e,\quad f\mapsto f+\beta(f,f')e-\beta(f,e)f'=f-f',\quad f'\mapsto f',
$$
$$
E_3\colon e\mapsto e-\beta(e,z)f'=e-2f',\quad f\mapsto f-2f',\quad e'\mapsto e'+2z,\quad f'\mapsto f',\quad x\mapsto x-\beta(x,\alpha)f'.
$$
Every image is an integral vector, and the basis vectors have integral images, so each $E_i$ is an integral isometry of $N$; the three displayed inverses are integral by the same computation, and $E_{a,w}E_{a,-w}=\id$ because the two shears cancel.
$\sigma_U$ and $\tau_0$ are evidently integral isometries.

*The discriminant kernel, on a full generating set.*
$U$ is unimodular, $E_8$ is unimodular, so
$$
N^\#=U\oplus\tfrac12U(2)\oplus\tfrac12E_8(2),\qquad A_\ten=N^\#/N ,
$$
and $A_\ten$ is generated by the classes of $e'/2$, $f'/2$ and $x/2$ for $x$ in a $\bZ$-basis of $E_8(2)$.
Each $E_i$ preserves $N$ and hence $N^\#$, since an isometry carries $\theset{y\in N_\QQ \st \beta(y,N)\subseteq\bZ}$ to itself; so its action on $A_\ten$ is read off on that generating set:
$$
\begin{array}{c|ccc}
 & e'/2 & f'/2 & x/2\\ \hline
E_1 & e'/2 & f'/2-f & x/2\\
E_2 & e'/2+e & f'/2 & x/2\\
E_3 & e'/2+z & f'/2 & x/2-\tfrac12\beta(x,\alpha)f'
\end{array}
$$
Every entry differs from the class in the left column by an element of $N$: $f$ and $z$ lie in $N$, and $\tfrac12\beta(x,\alpha)\in\bZ$ because the bilinear form of the summand $E_8(2)$ takes its values in $2\bZ$.
So all three act trivially on $A_\ten$, that is, lie in $\ker\rho$.
$\sigma_U$ and $\tau_0$ act by $-\id$ on one summand and identically on the others, and $-\id$ is the identity on a group annihilated by $2$; so they lie in $\ker\rho$ as well.

*Spinor signs.*
For $t\in\bR$ put
$$
\sigma^{(1)}_t(x)=x+t\qty[\beta(x,f)e'-\beta(x,e')f],\quad
\sigma^{(2)}_t(x)=x+t\qty[\beta(x,f')e-\beta(x,e)f'],\quad
\sigma^{(3)}_t(x)=x+t\qty[\beta(x,f')z-\beta(x,z)f'],
$$
each of the form $x\mapsto x+t\qty[\beta(x,a)w-\beta(x,w)a]$ with $a,w$ isotropic and $\beta(a,w)=0$.
The coefficient of $t$ in $\beta(\sigma_tx,\sigma_ty)$ is
$\beta(x,a)\beta(w,y)-\beta(x,w)\beta(a,y)+\beta(y,a)\beta(x,w)-\beta(y,w)\beta(x,a)$, which vanishes by cancellation, and the coefficient of $t^2$ is
$\beta(x,a)\beta(y,a)\beta(w,w)-\beta(x,a)\beta(y,w)\beta(w,a)-\beta(x,w)\beta(y,a)\beta(a,w)+\beta(x,w)\beta(y,w)\beta(a,a)$, which vanishes because $a$ and $w$ are isotropic and orthogonal.
So $\sigma^{(i)}_t\in\Orth(N_\bR)$ for every $t$, and $\sigma^{(i)}_s\sigma^{(i)}_t=\sigma^{(i)}_{s+t}$ because $\sigma^{(i)}_t$ fixes both $a$ and $w$ and preserves the two pairings $\beta(\cdot,a)$, $\beta(\cdot,w)$.
Thus $\sigma^{(i)}_1=E_i$ lies in a one-parameter subgroup of $\Orth(N_\bR)$, and $t\mapsto\spinornorm_\bR(\sigma^{(i)}_t)$ is a homomorphism from $(\bR,+)$ to a group of exponent two, hence trivial; so $\spinornorm_\bR(E_i)=1$, which is also the statement of @lem:unipotent-spinor-trivial.
For the two sign changes, @lem:minus-identity-spinor-norm gives $\spinornorm_\bR(-\id_U)=[(-1)^1]$ and $\spinornorm_\bR(-\id_{U(2)})=[(-1)^1]$, the summands having positive index one, and the spinor norm of an orthogonal sum is the product of the spinor norms of its summands, since a reflection of a summand is the corresponding reflection of the sum; so both have spinor norm $-1$.

*The planes.*
From the displayed images: $E_1(e)=e+e'$ and $E_1(e')=e'$ give $E_1^2(e)=e+2e'$, and $E_2(e')=e'+2e$; all three stabilize $P_1$.
Next $E_1(z)=z+\beta(z,f)e'=z+2e'$ and $E_1(e')=e'$, so $E_1$ stabilizes $P_2$, and $E_3(z)=z$, $E_3(e')=e'+2z$ do the same.
The divisibility of $v=ae+ce'\in P_1$ is read off from $\beta(v,f)=a$, $\beta(v,f')=2c$ and the vanishing of the other pairings, so it is $\gcd(a,2c)$; and for $v=az+be'$ of $P_2$ the values are $\beta(v,e)=\beta(v,f)=2a$, $\beta(v,f')=2b$, $\beta(v,e')=0$ and $\beta(v,x)=a\beta(\alpha,x)\in2\bZ$, so the divisibility is $2$ because $\gcd(a,b)=1$.

:::

::: {.theorem #thm:enriques-flag-witnesses title="Flag stabilizers of $\ten$: every primitive line in either plane class has a spinor-negative level-two stabilizer"}

Let $N=\ten=U\oplus U(2)\oplus E_8(2)$, and let $\Gamma\leq\Orth(N)$ contain $\ker\rho$.
With $\sigma_U$, $\tau_0$, $E_1$, $E_2$, $E_3$ as in @lem:enriques-level-two-transvections, put
$$
P_1\definedas\generators{e,e'},\qquad P_2\definedas\generators{z,e'},\qquad \theta\definedas E_1\tau_0 .
$$
The two planes represent the two $\Orth(N)$-classes of primitive isotropic planes ([@Ste91, 4.6]), and in the coordinates $[a:c]$ of $\ZZ(ae+ce')$ and of $\ZZ(az+ce')$ the elements act by
$$
\begin{array}{ll}
\sigma_U|_{P_1}\colon[a:c]\mapsto[a:-c],&\qquad \tau_0|_{P_2}\colon[a:c]\mapsto[a:-c],\\[2pt]
E_1|_{P_1}\colon[a:c]\mapsto[a:a+c],&\qquad E_2|_{P_1}\colon[a:c]\mapsto[a+2c:c],\\[2pt]
E_1|_{P_2}\colon[a:c]\mapsto[a:c+2a],&\qquad E_3|_{P_2}\colon[a:c]\mapsto[a+2c:c],
\end{array}
$$
while $E_1^2$ acts on $P_1$ by $[a:c]\mapsto[a:2a+c]$. Then:

1. $\theta$ stabilizes $P_2$, lies in $\ker\rho$, and fixes the *vector* $z+e'$; its spinor norm is $-1$.
2. For every primitive isotropic line $\ell\subset P_1$ there is $k\in\ker\rho\cap\Gamma$ with $\spinornorm_\bR(k)=-1$, $k(P_1)=P_1$ and $k(\ell)=\ell$.
3. For every primitive isotropic line $\ell\subset P_2$ there is such a $k$.
4. For every flag $\ell\subset P$, with $\ell$ a primitive isotropic line in a primitive isotropic plane, there is such a $k$ with $k(\ell)=\ell$ and $k(P)=P$.

:::

::: {.proof}

*The witnesses at the base lines.*
$\sigma_U$ negates $e$ and fixes $e'$, so it fixes $\ZZ e$ and stabilizes $P_1$; $\tau_0$ fixes $e$, negates $e'$ and fixes $z$, so it fixes $\ZZ e'$, $\ZZ z$ and stabilizes both $P_1$ and $P_2$.
For the product, $\tau_0(z+e')=z-e'$ and $E_1(z-e')=(z+2e')-e'=z+e'$, using $E_1(z)=z+2e'$ and $E_1(e')=e'$; so $\theta$ fixes the vector $z+e'$, and both factors stabilizing $P_2$, it stabilizes $P_2$.
By @lem:enriques-level-two-transvections all of these lie in $\ker\rho$, and $\spinornorm_\bR(\sigma_U)=\spinornorm_\bR(\tau_0)=-1$ while $\spinornorm_\bR(E_1)=1$, so $\spinornorm_\bR(\theta)=-1$.
A conjugate $gkg^{-1}$ of a witness has $\spinornorm_\bR(gkg^{-1})=\spinornorm_\bR(k)$ and lies in $\ker\rho$, which is normal in $\Orth(N)$.

*The lines of $P_1$.*
The subgroup generated by $E_1$ and $E_2$ stabilizes $P_1$ and acts on it by the shears
$$
E_1\mapsto\mu=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad E_1^2\mapsto\mu^2=B=\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad E_2\mapsto A=\begin{pmatrix}1&2\\0&1\end{pmatrix},
$$
and $-\id_N\in\ker\rho$ acts by $-I$.
By part 3 of @lem:congruence-two-transitivity the group generated by these matrices is transitive on the primitive lines of $P_1$ with first coordinate odd, and on those with first coordinate even; and those two sets are exactly the two divisibility classes of $P_1$ computed in @lem:enriques-level-two-transvections.
So a primitive line $\ell\subset P_1$ of divisibility one is $g\ZZ e$ for some $g\in\generators{E_1,E_2}$, and $g\sigma_Ug^{-1}$ is a witness for it; a line of divisibility two is $g\ZZ e'$ for some such $g$, and $g\tau_0g^{-1}$ is a witness.

*The lines of $P_2$.*
The subgroup generated by $E_1$ and $E_3$, together with $-\id_N$, stabilizes $P_2$ and acts on it by
$$
E_1\mapsto B=\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad E_3\mapsto A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad -\id_N\mapsto-I .
$$
By parts 1 and 2 of @lem:congruence-two-transitivity this group preserves the class modulo $2$ of a primitive vector of $P_2$ and is transitive on the primitive vectors of each of the three classes.
The base lines are $\ZZ z$ and $\ZZ e'$, both fixed by $\tau_0$, and $\ZZ(z+e')$, fixed by $\theta$; the three have pairwise distinct classes, since $z\equiv(1,0)$, $e'\equiv(0,1)$ and $z+e'\equiv(1,1)$ modulo $2$.
So every primitive line of $P_2$ is the image of one of these three under an element of the group, and the corresponding conjugate is a witness for it.

*Every flag.*
Let $\ell\subset P$ be a flag.
By [@Ste91, 4.6] there are exactly two $\Orth(N)$-classes of primitive isotropic planes, represented by $P_1$ and $P_2$ (@prop:ten-plane-classes(1)), so there is $g\in\Orth(N)$ with $gP_1=P$ or with $gP_2=P$.
Then $g^{-1}\ell$ is a primitive isotropic line of that representative plane, hence has a witness $k$ by the two paragraphs above, and $gkg^{-1}\in\ker\rho$ has spinor norm $-1$ and fixes $P$ and $\ell$.
Since every witness lies in $\ker\rho\subseteq\Gamma$, the stabilizer inside $\Gamma$ of each of these objects meets $\Gamma\setminus\Orth^+(N)$.

:::

::: {.corollary #cor:enriques-preimage-vs-positive title="The spinor-positive half of a discriminant preimage"}

Let $N = \ten$, let $M\leq\Orth(A_\ten,q_\ten)$ and $\Gamma=\rho^{-1}(M)$, so that $\rho(\Gamma)=M$ by @thm:two-elementary-surjectivity; put $\Gamma^+=\Gamma\intersect\Orth^+(N)$, and let $\tau_0$ be as in @lem:enriques-level-two-transvections.

1. $\Gamma = \Gamma^+\sqcup\Gamma^+\tau_0$, so $\Gamma^+$ has index two in $\Gamma$, and $\rho(\Gamma^+)=\rho(\Gamma)=M$.
2. $\Gamma$ and $\Gamma^+$ have the same orbits on primitive isotropic lines, on primitive isotropic planes and on flags.
   On a $\Gamma$-set $X$ their orbits agree exactly when $\Stab_\Gamma(x)$ meets $\Gamma\setminus\Orth^+(N)$ for every $x\in X$.
:::

::: {.proof}

(1) $\tau_0\in\widetilde\Orth(N)\subseteq\Gamma$ is spinor-negative (@lem:enriques-level-two-transvections), so for $g\in\Gamma$ one has $g\tau_0\in\Gamma$ with $\rho(g\tau_0)=\rho(g)$ and $\spinornorm_\bR(g\tau_0)=-\spinornorm_\bR(g)$.
So exactly one of $g$ and $g\tau_0$ lies in $\Gamma^+$, which gives $\Gamma=\Gamma^+\sqcup\Gamma^+\tau_0$ and $\rho(\Gamma^+)=\rho(\Gamma)$.

(2) The first sentence is @thm:enriques-spinor-orbit-agreement, with @thm:enriques-flag-witnesses for the flags, and the second is @lem:spinor-orbit-agreement.
:::

::: {.lemma #lem:gamma-transport-identity title="The gluing anti-isometry for $\gent$"}

Write $A_{\sen} = A_{U(2)}\oplus A_{E_8(2)}$ and $A_{\ten} = A_U\oplus A_{U(2)}\oplus A_{E_8(2)}$ for the two discriminant groups, summand by summand, with $A_U = 0$ because $U$ is unimodular.
Under the identification of the common summands the two forms agree, $q_{\ten} = q_{\sen}$; both take values in $\ZZ/2\ZZ$, where $-1 = 1$, so $q_{\ten}\circ\gamma = -q_{\sen}$ holds for $\gamma = \id$.
Consequently
$$
\rho_{\ten}(\gent) \;=\; \rho_{\sen}\bigl(\Stab_{\Orth(\sen)}(h)\bigr) \;\leq\; \Orth(A_{\ten}, q_{\ten}),
$$
and that group is generated by the discriminant images of the reflection in $u_0-w_0$ and the eight reflections in the simple roots of $E_8(2)$ — all nine of which are isometries of $\ten$ itself, since $U(2)$ and $E_8(2)$ are summands of $\ten = U\oplus U(2)\oplus E_8(2)$.
Any other admissible anti-isometry gives a preimage conjugate to $\gent$ in $\Orth(\ten)$.

:::

::: {.proof}

The discriminant groups of $U(2)$ and of $E_8(2)$ are the same in the two lattices, because both lattices contain those summands isometrically; $U$ contributes nothing. So the canonical identification is an isometry of quadratic spaces, and $\gamma = \id$ is an anti-isometry because negating a $\ZZ/2\ZZ$-valued form changes nothing.
The generators act on the discriminant through their own summands and trivially on the other, so the images of the nine isometries of $\ten$ are the nine generators of the group in @thm:coble-heegner-finite-orbits' first item and equal the $\gamma$-transport of @prop:gamma-en-two-gluing's image.
Two admissible anti-isometries differ by $\tau\in\Orth(A_{\ten},q_{\ten})$, since both satisfy $q_{\ten}(\gamma x) = -q_{\sen}(x)$; by the surjectivity of the discriminant representation (@thm:two-elementary-surjectivity) $\tau = \rho_{\ten}(s)$ for some isometry $s$ of $\ten$, and then
$$
\rho_{\ten}^{-1}(\tau M\tau^{-1}) = s\,\rho_{\ten}^{-1}(M)\,s^{-1},
$$
so the two preimages are conjugate in $\Orth(\ten)$.

:::

::: {.remark #rmk:gamma-en-two-fibres title="What the index does and does not give for the cusps"}

The $0$-cusps of $\fentwo$ are the $\gent$-orbits of primitive isotropic $v\in\ten$.
$[\Gamma^K_\En : \gent]$ being a finite index of an infinite arithmetic group, and equal to the index of $\rho(\gent)$ in the finite orthogonal group, is what lets a discriminant computation say anything here at all; it is not itself a count of orbits, and two further facts are needed.

*Surjectivity of the divisibility map.*
A primitive isotropic $v$ with $\operatorname{div}(v) = 2$ satisfies $v^2 = 0$, so $v/2\in\ten^*$ has $q_{\ten}([v/2]) = 0$ and $[v/2]\neq 0$; and $\operatorname{div}(v)=1$ gives the class $0$.
By [@AEGS25 §3.2] $\Orth(\ten)$ has exactly two orbits on primitive isotropic vectors, $\operatorname{div}=1$ and $\operatorname{div}=2$ — reproduced as a lattice computation by `T_En.cusps(1)`, which returns the two $0$-cusps of $F_{(10,10,0)}$ (record `computations/reports/coble_gammaEn2-cusps-lattice.md`) — and $\Orth(A_{\ten},q_{\ten})$ is transitive on the $527$ nonzero isotropic classes, which `coble_gammaEn2-card-run.txt` reports as one orbit before passing to a subgroup.

The lattice call counts *lines*, and the passage to vectors is a separate step rather than the same statement: a $0$-cusp is a primitive isotropic rank-one subobject $\ZZ v$, not the vector $v$, and $\theset{v,-v}$ are two generators of one line.
The two counts agree because $-\id_{\ten}\in\Orth(\ten)$ sends $v$ to $-v$, so a line's $\Orth(\ten)$-orbit is the image of a single vector orbit and the map $\text{vector orbits}\to\text{line orbits}$ is bijective: it is onto by definition of the action on subobjects, and injective because the two generators of a line lie in one vector orbit.
The same argument makes the class $[v/\operatorname{div}(v)]$ an invariant of the line, since $v$ and $-v$ have the same class in $A_{\ten}$. So the image of the $\operatorname{div}=2$ class is a single $\Orth(q)$-orbit, and it is nonempty: every one of the $527$ classes is $[v/2]$ for some primitive isotropic $v$ with $\operatorname{div}(v)=2$. The divisibility map is therefore surjective onto the classes, and $\gent$-orbits map onto $\rho(\gent)$-orbits.

*What is not proved by equivariance alone, and what is.*
Surjectivity on point sets does not make the map on orbits injective, and the correct criterion is not transitivity of the kernel.
Let $X$ be a $\Gamma^K_\En$-orbit of primitive isotropic lines, $x\in X$, $H = \Stab_{\Gamma^K_\En}(x)$, $c = \varphi(x)$ its class, $M_c = \Stab_M(c)$ for $M = \rho(\gent)$, and $\Gamma_c = \Stab_{\Gamma^K_\En}(c)$, $\gent_c = \rho^{-1}(M_c)$.
The $\gent$-orbits on $X$ are the double cosets $\gent\backslash\Gamma^K_\En/H$, the orbit of $gx$ has size $[\gent : \gent\cap gHg^{-1}]$, and the $\gent$-orbits lying over one $M$-orbit of classes are the double cosets $\gent_c\backslash\Gamma_c/H$.
There is exactly one of those --- that is, the finite count below is exact on that class --- if and only if
$$
\Gamma_c = \gent_c\cdot H
\quad\Longleftrightarrow\quad
\rho(\Gamma_c) = M_c\cdot\rho(H)
\quad\Longleftrightarrow\quad
\Stab_{\rho(\Gamma^K_\En)}(c) = M_c\cdot\rho(H),
$$
the middle equality being the image of the first under $\rho$ and the last a rewriting of it; the criterion is stated in $\rho(\Gamma^K_\En)$, and replacing that group by all of $\Orth(q_{\ten})$ uses the surjectivity of the discriminant representation (@thm:two-elementary-surjectivity), not the definition.
It holds in particular when $\rho(H) = \Stab_{\rho(\Gamma^K_\En)}(c)$: when the discriminant image of the stabilizer of the chosen line is the *whole* stabilizer of its class in the image group.
Transitivity of the kernel $K = \ker\rho$ on the fibre is **sufficient** for a single $\gent$-orbit there: $K\subseteq\gent_c$ by @prop:gamma-en-two-index, so $K$ transitive gives $\Gamma_c = K\cdot H$, whence $\rho(\Gamma_c) = \rho(H)$, and the criterion holds because $M_c\subseteq\rho(\Gamma_c)$. It is **not necessary**, and the obstruction is exactly the lifting of $M_c$: $\gent_c/K\cong M_c$ acts on the set of $K$-orbits in the fibre, the fibre is one $\gent_c$-orbit exactly when that action is transitive, and $M_c$ may permute several $K$-orbits cyclically. That is why the criterion is stated with $\rho(H)$ and not with $K$, and why $K$-transitivity is a sufficient but not a necessary condition.
What the criterion needs is the image of $\Stab_{\Orth(\ten)}(x)$: by @lem:line-stabilizer-image that image *is* the stabilizer of the class — $M_c$ at the $\gent$ level — so the criterion holds with equality and the finite count $5 = 1+4$ is the number of $0$-cusps of $\fentwo$, not merely a count of $\rho(\gent)$-orbits on classes. The computational route through `computations/reports/coble_gammaEn2-cusps-lattice.py` (the stabilizer generators that `T_En.cusps(1)` retains, for both lines) remains as an independent check of the lemma; it is not the proof of it.

**A bounded rank-4 search, as evidence only.**
The enumeration that produced those lines asks a decidable finite question and should be read at exactly its scope. For any lattice $L$ of rank $r$ with basis $B$ of a totally isotropic plane $\varPi$ (a $2\times r$ integer matrix) one has $\varPi^*/\varPi = R^{\mathrm{sat}}/R$ where $R$ is the row space of $BG$ in $\ZZ^r$; and $\varPi$ is primitive in $L$ exactly when that product computed for $B$ alone is $1$.
The script `computations/reports/coble_gammaEn2-plane-strata.py` runs this with $r = 4$, in the rank-$4$ summand $U\oplus U(2)$ **of** $T_\En$ — not in $T_\En$ itself, whose rank is 12, where the basis would be $2\times 12$ and the E_8(2)-components would matter. It then enumerates all primitive totally isotropic **presentations** with entries in $[-3,3]$: bases of planes, not the planes themselves, so the pairwise count double-counts planes with different bases of the same plane and is not a count of planes.
This is hence *bounded evidence in the rank-$4$ summand only*: it exhibits planes of order $2$ ($1040$ presentations), it finds none of order $1$ or $4$ in that box, and it proves nothing about nonexistence — not there, and still less in $T_\En$, where no reduction to the summand has been proved. The plane $\varPi = \langle e,e'\rangle$ displayed above is the genuine order-$2$ exhibit.
**What is open.** Order-$1$ and order-$4$, the reduction from the summand to $T_\En$, the availability of a primitive $w\in\varPi\cap U(2)$ on which a halving argument could rest, and the integrality of the next half each remain unproved. The nine published $1$-cusps are not assessed by this search in either direction, and no sum over the finite strata is asserted here as an arithmetic count.
No conclusion about cusps is drawn from that bounded search: the published nine $1$-cusps remain the source target, and liftability of order-$1$ and order-$4$ stays open rather than being negated.

:::

::: {.remark #rmk:descent-of-an-equivariant-inclusion title="What the stabilizer statement has to supply"}

The stabilizer step of @thm:normalization is one instance of a criterion for descending a map to a pair of quotients, and the criterion has a weak form and a strong one that are worth separating.
Let $f\colon A\injects B$ be an inclusion of sets, with groups $G_A$ and $G_B$ acting on $A$ and on $B$.
A map of orbit sets $\bar f\colon G_A\backslash A\too G_B\backslash B$ is well defined as soon as $f$ carries orbits into orbits: for every $x\in A$ and every $g_A\in G_A$ there must be some $g_B\in G_B$, allowed to depend on both $x$ and $g_A$, with $g_B f(x) = f(g_A x)$.
That is all a set-theoretic descent needs, and it is strictly weaker than an equivariance statement.
The strong form is a uniform assignment, for instance a homomorphism $G_A\too G_B$ with $f\circ g_A = g_B\circ f$ for all $g_A$ at once.
It is not necessary for $\bar f$ to exist, but it is what the geometric statements here use: it makes $f$ equivariant rather than merely orbit-compatible, it is what identifies quotients rather than just producing a map between them, and it is what any comparison of stabilizers or of orbit decompositions has to stand on.
For the case at hand, $A = \bD(T_\Co)$ with $G_A = R_\Gamma$ of @def:gamma-co-groups and $B = \bD(T_\En)$ with $G_B = \Gamma$, and what @prop:gamma-co-images supplies is the strong form, with equality: restriction of $\Stab_{\Gamma}(\delta)$ to $T_\Co$ is exactly $R_\Gamma$, so $g_A\mapsto g_A\oplus\id_{\ZZ\delta}$ is a genuine homomorphism and $f^{\Gamma}$ is $G_A$-equivariant, not merely orbit-compatible.
On the stabilizer of the sublattice $T_\Co$ the kernel of restriction is $\{1, s_\delta\}$, where $s_\delta$ is the reflection in the $(-2)$-vector $\delta = \tilde e - \tilde f$, which fixes $T_\Co$ pointwise and negates $\delta$. On $\Stab_\Gamma(\delta)$ restriction is injective, and the equivariant assignment is its inverse, the extension that fixes $\delta$.
Equality of the images does not give injectivity of $\bar f$: two $G_A$-orbits may still be carried into one $G_B$-orbit, and it is the point of $\bD(T_\Co)$ lying on a second translate $\inverseof{g}(T_\Co)$ that the fibre count has to control.
:::
