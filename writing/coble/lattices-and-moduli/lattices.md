# Period domain embeddings and normalization {#sec-lattices}

::: {#not:lattices-of-chapter .notation title="The lattices of this chapter" defines="$\lkt$; $E_{10}$; $S_\En$; $T_\En$; $S_\Co$; $T_\Co$; $\sdp$; $\tdp$"}

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

The map is well defined and isometric: $h$ has square $2$ and $\tilde e+\tilde f$ has square $2$, since $\tilde e,\tilde f$ are the isotropic (@def:orthogonal-complement) basis of $U$ with $\tilde e\cdot\tilde f=1$; and $\eta$ is the identity on $E_{10}(2)$, which is an orthogonal summand of both sides.
So $\eta$ is a morphism of lattices of $\mathbf{Lat}_{\bZ}$, and it is injective (@def:injective-map) because it is injective on each summand.

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
The three matrices, in the standard basis of the marking of @thm:theta-co-coordinates, are displayed later in the book.
:::

::: {.proof}

The displayed map is isometric on each summand: on $\generators{2}$ as in @lem:primitive_embedding_eta, on $U(2)$ as the identity, and on $E_8(2)$ because $(y,y)^2 = 2y^2$ in $E_8\oplus E_8$.
Its cokernel is $U/\bZ(\tilde e+\tilde f)\oplus(E_8\oplus E_8)/\theset{(y,y)}$.
The first summand is $\bZ$ by @lem:primitive_embedding_eta, and $(a,b)\mapsto a-b$ identifies the second with $E_8$.
The cokernel is torsion-free, so the map is primitive by @prop:primitive-characterization.
The embedding $\fco\injects\fttz$ is the one that @lem:locally_closed_embedding_BB induces.

For uniqueness, by [@AEGS25 Lem. 2.4] it suffices to show uniqueness of $\sen \injects S_{\Co}$, i.e.

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
Similarly, by [@Nik80 Cor. 1.5.2, Thm. 3.6.3], the homomorphism $\Orth(\lkt)\to \Orth(T_\Co)$ is surjective.
:::

::: {.lemma #lem:locally_closed_embedding_BB}

The embeddings of lattices $\eta: T_\Co\injects T_\En$ (resp. $T_{\Co} \injects \tdp$) induce locally closed (@def:locally-closed-subset) embeddings $\fco \injects \fen$ (resp. $\fco \injects \fttz$) which extend to morphisms on the Baily--Borel compactifications.
:::

::: {.proof}

This follows from [@KK72 §5, Thm.2].
:::

::: {.definition #def:gamma-co-groups title="The groups of the Coble lattice" defines="$\delta$; $\Gamma_\En$; $\Gamma^K_\En$; $\gent$; $\Gamma_\Co$; $\fco$; $\Gamma^{\mathrm{un}}_\Co$; $F^{\mathrm{un}}_\Co$; $\widetilde\Orth^+(T_\Co)$; $R_\Gamma$; $\Gamma_{\Co,2}$; $F_{\Co,2}$"}
$T_\Co$ is the lattice $N$ of [@DK13, (3.6)], $N = \generators{2}\oplus E(2)$ with $E(2) = U(2)\oplus E_8(2)$; in the notation of @lem:primitive_embedding_eta it is $\generators{h}\oplus E_{10}(2)$. Let $\delta\definedas\tilde e-\tilde f$, a $(-2)$-vector of $T_\En$ with $\delta^{\perp T_\En} = \eta(T_\Co)$; then $T_\En = (T_\Co\perp\ZZ\delta)_H$ is the overlattice glued along $H = \generators{(h/2,\,\delta/2)}$ (@lem:primitive_embedding_eta, @def:gluing-datum-of-a-pair).

Three groups act on $\bD(T_\En)$: the stable group $\Gamma_\En\definedas\widetilde\Orth^+(T_\En) = \Orth^+(T_\En)\intersect\discriminantkernel{T_\En}$; the group $\Gamma^K_\En\definedas\Orth(T_\En)$, which is the group that [@AEGS25, Def. 2.6] writes $\Gamma_\En$; and $\gent = \rho^{-1}(M)$, with $M$ the summand-preserving subgroup of $\Orth(A_{T_\En},q)$ [@AEGS25, Def. 2.6; @Ste91, Prop. 2.7].

1. $\Gamma_\Co\leq\Orth(T_\Co)$ is the monodromy group of the variation of Hodge structure on the universal family over the moduli stack $\mcM_\Co$ of Coble surfaces (@def:coble-moduli-functor, @lem:coble-moduli-functor-stack): the image of the monodromy representation (@def:transport-and-monodromy) of the local system of lattices with fibre $T_\Co$ (@def:local-system-of-lattices) of that variation under $\pi_1(\mcM_\Co)$. A monodromy group is a property of the VHS on the universal family over the stack; it is not the monodromy of a chosen family, and no chosen family replaces it. A parameter space $B'$ carrying a family, with its map to $\mcM_\Co$, pulls the system back, and the monodromy of the pulled-back system is the image of $\pi_1(B')$ under the composite (@lem:coble-family-base-change); that image is $\Gamma_\Co$ exactly when the map sees all of $\pi_1(\mcM_\Co)$, which is a theorem and not the definition. The presentation used for the computations of this section is @def:coble-family-unpolarized: its labelled base $B$ carries the family and the local system of @lem:d2-unpolarised-family and @lem:d2-local-system, over which the eleven classes are global sections (@lem:d2-local-system(2)); write
$$\Gamma_\Co(B)\definedas\rho\qty{\pi_1(B,s)}$$
for the monodromy of that presentation, and $\Gamma_\Co(\bar B)$ for that of the unlabelled base, which carries the same family and a larger group, base 1. being a coarse space with no family (@lem:d2-local-system(4), @rmk:d2-what-is-open(1)). The two groups are compared by the map $\pi_1(B)\to\pi_1(\mcM_\Co)$ induced by the presentation, and identifying them is research#797, item 6. Put $\fco\definedas\bD(T_\Co)/\Gamma_\Co$.
2. $\Gamma^{\mathrm{un}}_\Co\definedas\Orth(T_\Co)$, with $F^{\mathrm{un}}_\Co\definedas\bD(T_\Co)/\Orth(T_\Co)$: the moduli space $M_\Co$ of Coble surfaces is isomorphic to an open subset of $\bD(N)/\Orth(N)$ [@DK13, Prop. 3.2].
3. The stable group
$$
\widetilde\Orth^+(T_\Co) = \Orth^+(T_\Co)\intersect\ker\bar\rho,
$$
$\bar\rho$ being the discriminant representation (@def:discriminant-rep) of $T_\Co$ and $\ker\bar\rho$ the group $\ker\bigl(\Orth(L)\to\Orth(A_L)\bigr)$ of [@DK13, (2.1)].
4. For $\Gamma$ one of $\Gamma_\En$, $\Gamma^K_\En$, $\gent$, the restricted stabilizer (@def:group-orbit)
$$
R_\Gamma\definedas \text{the image of } \Stab_{\Gamma}(\delta) \text{ in } \Orth(\delta^{\perp T_\En}) = \Orth(T_\Co).
$$
5. $\Gamma_{\Co,2}\leq\Orth(T_\Co)$ is the monodromy group of the VHS of the degree-$2$ Coble family: the image of the monodromy representation (@def:transport-and-monodromy) of the local system of lattices with fibre $T_\Co$ (@def:local-system-of-lattices) of the family of Coble surfaces carrying a degree-$2$ numerical polarization (@def:coble-polarization-classes); the family, with its objects, its base and its period map, is @def:coble-family-degree-two. It is defined by the family and is not a lattice group. Put $F_{\Co,2}\definedas\bD(T_\Co)/\Gamma_{\Co,2}$.

A statement about a quotient of $\bD(T_\Co)$ names the group it uses; in particular every count of cusps names its group.
:::

::: {.remark #rmk:gamma-co-groups-comparisons title="How the groups of the Coble problem compare"}

The family of unpolarized Enriques surfaces (@def:enriques-surface), whose local system of lattices has fibre $T_\En$ and monodromy group $\Gamma_\En$, induces the family of @def:gamma-co-groups(1) and its local system *of lattices*, in the sense that $T_\Co=\delta^{\perp\ten}$ is cut out of $T_\En$ (@prop:gamma-co-images); that it induces the family itself, that is that the two bases are identified, is not proved by anything read (@rmk:d2-what-is-open(2)). What is proved about the labelled group is $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)); identifying it with the group of @def:gamma-co-groups(1) is research#797, item 6.

The group $R_{\gent} = \bar\rho^{-1}(P)$ of @def:gamma-co-groups(4) and @prop:gamma-co-images(3) is the restricted Enriques stabilizer; the comparison of $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5) with it is @thm:coble-monodromy-versus-enriques, and the arithmetic group (@def:arithmetic-group) that contains $\Gamma_{\Co,2}$ is $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co) = \Gamma^{\mathrm{dir}}_{\Co,2} = \Gamma^{\mathrm{Hdg}}_{\Co,2}$ (@thm:coble-monodromy-versus-enriques(4)).
:::

::: {.remark #conj:gamma-co-stable title="The stable-group equality, and its status"}

The equality
$$\Gamma_\Co=\widetilde\Orth^+(T_\Co)$$
is the stable-group conjecture of this chapter, and it is research#780. It is proved in one direction on each base: $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)), and the identification $\Gamma_\Co=\Gamma_\Co(B)$ is research#797, item 6 (@def:gamma-co-groups(1), @thm:gamma-co-is-stable(2)), so no inclusion for $\Gamma_\Co$ itself is asserted here. The reverse inclusion is open; the three routes attempted and the step at which each fails are @rmk:d2-routes-for-the-equality. On the unlabelled base the group $\Gamma_\Co(\bar B)$ is not contained in $\widetilde\Orth^+(T_\Co)$: it contains $\Gamma_\Co(B)$ with index $10!$ and its discriminant image is $\Theta\neq\theset{1}$ (@lem:relabelling-discriminant-action(3), @cor:gamma-co-inclusions(2)). On the coarse space there is no family at all: the tautological local system of that quotient has monodromy $\Orth^+(T_\Co)$, which is not $\Gamma_\Co$ (@thm:gamma-co-is-full).
:::

::: {.remark #rmk:gamma-co-nodal-pair-proposal title="The $(-4)$-reflection: what is computed, and the three inputs that are missing"}

The lattice half of a refutation of @conj:gamma-co-stable is computed and stands, and by @thm:gamma-co-is-stable its hypothesis does not hold on the labelled base: if the nodal-pair element $w_\delta w_{\delta'}$ were a monodromy element of the family, then its action on $T_\Co$ would be the reflection $s_e$ in the class $e=\delta-\delta'$ of square $-4$ (`computations/reports/smwo_direct-period.md`, Theorem E, and the re-derivation in `computations/reports/coble_658-nodal-pair-refutation-probe-run.txt`), and every such reflection is an integral isometry of $T_\Co$ lying in $\Orth^+(T_\Co)$ and outside $\discriminantkernel{T_\Co}$ (@prop:gamma-co-reflective-set(3)). If that element is in $\Gamma_\Co$, then $\Gamma_\Co\not\subseteq\widetilde\Orth^+(T_\Co)$, the $\Gamma_\Co$ form of @prop:gamma-co-strong-lifting fails, and the cusp counts of $\fco$ are not those of the stable quotient.

Three inputs are missing, and none of them is a proved statement of this book:

1. the local monodromy of a degeneration acquiring two ordinary nodes at once as the product of the two commuting Picard--Lefschetz reflections: no printed statement in `tmp/sources` supplies it, and the record's citation of `.ultramath/smw0o7jbf/m5/A20-direct-period-theorem.md` §6.1(b) points outside main;
2. that the one-node family is a family of Coble surfaces *in the moduli space whose monodromy is $\Gamma_\Co$*. The members themselves are not the difficulty: a one-node member is a singular Coble quotient in the book's sense, a K3 with one $A_1$ point quotiented by an involution that fixes that point and is otherwise free in codimension one, and its resolution is the resolved Coble surface of @def:resolved-coble, "the object traditionally called a classical Coble surface". What is missing is the moduli identification: [@DK13, Prop. 3.2] is about the *classical* ten-node construction --- "In this note we will restrict ourselves to these classical examples" --- so it places that construction in $\bD(N)/\Orth(N)$ and says nothing about whether the one-node members lie in the same open subset;
3. that the monodromy of the family over that base is contained in $\Gamma_\Co$, which is functorial once 2 holds and is not otherwise known.

There is a reason, not only a gap, behind the second of these, and it points at where a witness would have to live. In the classical model of [@DK13, §3] the Coble surface is the blow-up of $\PP^2$ at the ten nodes of a sextic, the double cover $X$ carries the divisors $E_0,\dots,E_{10}$, and their classes $e_0,\dots,e_{10}$ generate $M_X\cong\generators{2}\oplus\generators{-2}^{\oplus10}$, with $T_\Co = M_X^\perp$ (@prop:coble-transcendental). A class of $M_X$ is orthogonal to $T_\Co$, so its reflection acts as the identity on $T_\Co$. That does not settle the question, and the reason is worth stating, because the first reading of it is wrong: the classes $e_0,\dots,e_{10}$ are algebraic on every member, so they are not vanishing classes. A vanishing class must be orthogonal to $\Pic(\widehat X_b)$, hence lies in $T_\Co$ --- which is why the discriminant of the period map is described by classes of $T_\Co$ (@prop:monodromy-contains-root-reflections), not by the $e_i$. What the computation above says is therefore only that the $M_X$-part of the monodromy is invisible on $T_\Co$; it does not say that a $(-4)$-class of $T_\Co$ fails to arise, and a witness for $\Gamma_\Co\not\subseteq\widetilde\Orth^+(T_\Co)$ is neither produced nor excluded by it.

On the tautological reading of base 1 the conclusion of this paragraph is unconditional (@thm:gamma-co-is-full), because $\Gamma^{\mathrm{taut}}_\Co=\Orth^+(T_\Co)$ contains $s_e$ for every primitive $e$ of square $-4$; the three inputs below are what a proof needs for a base whose monodromy is not already the full group. What would settle that case is a loop of the Coble moduli, or a degeneration of it, whose monodromy is computed to be $s_e$; no such computation exists in this repository on main.

The question can be put without either model, and then it is a question about divisors. The period domain is $\bD(T_\Co)$ and the Picard rank of a member jumps exactly on the Heegner divisors $\delta^\perp$ of $T_\Co$. The local monodromy of a loop around such a divisor is the reflection $s_\delta$, and that identification is an input, not a result of this book: @prop:monodromy-contains-root-reflections takes it as its hypothesis ("suppose that for every class $\delta$ of square $-2$ the meridian of $\delta^\perp$ [is $s_\delta$]"), and the only statement of the phenomenon here is @cons:lefschetz-periods, a construction with no printed source. Everything below is conditional on it. By @prop:gamma-co-reflective-set, $s_\delta$ lies in $\widetilde\Orth^+(T_\Co)$ exactly when $\delta^2 = -2$: for $\delta^2 = -4$ it lies in $\Orth^+$ and outside the discriminant kernel, and for $\delta^2 = 2$ or $4$ it lies outside $\Orth^+$ altogether. Two hypotheses make that an equivalence, and neither is proved here; where each stands is worth stating, because they are not equally close.

*(PL)* is cited, not assumed: [@Voi07, Thm. 3.16] states the Picard--Lefschetz formula $T(\alpha)=\alpha+\epsilon_n\langle\alpha,\delta\rangle\delta$, which for a surface is the reflection in the vanishing class $\delta$. The unipotent Kulikov transform $T=\exp(N)$ of a semistable degeneration (Alexeev--Engel, arXiv:2208.10383v2, §6) is a different statement and is not what this step uses.

*(MG)* is where the work is, and it splits cleanly into a part that follows from the published statement and a part that does not. [@DK13, Prop. 3.2] gives exactly one thing about the image: $\mathcal M_{Co}$ is isomorphic to an open subset of $\bD(N)/\Orth(N)$ with $N=T_\Co$, the isomorphism being the period map, hence open and injective (Torelli). It says nothing about the complement.


The two-way form that (PL) and (MG) would give is superseded by @thm:gamma-co-is-full below, which needs neither: what remains of it is the one direction that the theorem does not cover --- a met divisor of square $-4$ would give an element outside $\widetilde\Orth^+(T_\Co)$ even if the moduli identification failed. Neither model decides this from what is printed. [@DK13, Prop. 3.2] says that the moduli space is an open subset of $\bD(N)/\Orth(N)$ with $N=T_\Co$, which constrains no Heegner divisor; the sentence after it says that the quotient of the $(-2)$-Heegner divisor of the Enriques period domain is birationally the same moduli space, which places it inside one. The two are consistent because both are birational statements about a $9$-dimensional space; what they do not say is which Heegner divisors of $T_\Co$ its boundary meets. That is the question item 1e reduces to.
:::

::: {.lemma #lem:orbifold-monodromy-of-a-quotient title="Monodromy of the tautological local system of a quotient orbifold"}

Let $\widetilde U$ be a connected manifold and let $\Gamma$ be a group (@def:group) acting on it properly discontinuously with finite stabilizers (@def:group-orbit), so that $U\definedas\widetilde U/\Gamma$ has the quotient orbifold structure (@def:orbifold-quotient-structure). Let $\varphi\colon\Gamma\to\Aut(T)$ (@def:endomorphism-monoid) be a homomorphism to the automorphism group of an abelian group $T$ --- a $\Gamma$-module structure on $T$ --- and let
$$\bT\definedas(\widetilde U\times T)/\Gamma$$
be the local system on $U$ whose pullback to the chart is the trivial local system $\widetilde U\times T$ with the equivariant structure $g\cdot(\tilde u,t)\definedas(g\tilde u,\varphi(g)t)$, so that its pullback along a map $f\colon W\to U$ from a topological space is $(f^{-1}\widetilde U\times T)/\Gamma$, where $f^{-1}\widetilde U=W\times_U\widetilde U$ is the pulled-back $\Gamma$-torsor; this is the only property of $\bT$ used below. Fix $\tilde x\in\widetilde U$ and put $x\definedas[\tilde x]$. Then:

1. an orbifold loop of $U$ at $x$ is represented by a pair $(g,\widetilde\gamma)$ with $g\in\Gamma$ and $\widetilde\gamma$ a path (@def:path-connectedness) in $\widetilde U$ from $\tilde x$ to $g\tilde x$; its group element is $\psi(g,\widetilde\gamma)\definedas g$, and the assignment $\lambda\mapsto\psi(\lambda)^{-1}$ is a surjective homomorphism $\pi_1^{\mathrm{orb}}(U,\tilde x)\to\Gamma$ --- that is, $\psi$ is an anti-homomorphism for the product convention of @def:transport-and-monodromy --- with kernel (@def:kernel-cokernel) $\pi_1(\widetilde U,\tilde x)$, so that
$$1\too\pi_1(\widetilde U,\tilde x)\too\pi_1^{\mathrm{orb}}(U,\tilde x)\too\Gamma\too1$$
is exact (@def:exact-complex);

2. the monodromy representation (@def:transport-and-monodromy) of $\bT$ is
$$\rho=\varphi\circ\psi^{-1}\colon\pi_1^{\mathrm{orb}}(U,\tilde x)\too\Aut(T),$$
where $\psi^{-1}$ is the map $\lambda\mapsto\psi(\lambda)^{-1}$, a homomorphism because $\psi$ is an anti-homomorphism; hence
$$\im\rho=\varphi(\Gamma),\qquad \ker\rho=\theset{\lambda\st\psi(\lambda)\in\ker\varphi},$$
and
$$1\too\pi_1(\widetilde U,\tilde x)\too\ker\rho\too\ker\varphi\too1$$
is exact. In particular, if $\varphi$ is injective --- as for a subgroup $\Gamma\subseteq\Aut(T)$ in its defining action --- then $\rho$ has image $\Gamma$ and kernel $\pi_1(\widetilde U,\tilde x)$, and $\psi^{-1}$ identifies $\pi_1^{\mathrm{orb}}(U,\tilde x)/\pi_1(\widetilde U,\tilde x)$ with $\Gamma$.
:::

::: {.proof}

*The covering and the loop model.* The chart $p\colon\widetilde U\to U$ presents $U$ as the quotient stack $[\widetilde U/\Gamma]$ (Noohi, *Foundations of topological stacks I*, arXiv:math/0503247, Definition 3.3 and Proposition 3.4), is representable (Noohi, Lemma 6.3), and is a $\Gamma$-torsor, $\widetilde U\times_U\widetilde U\cong\Gamma\times\widetilde U$: its deck transformations are the elements of $\Gamma$. Since $\Gamma$ is discrete and acts properly discontinuously with finite stabilizers, $p$ is a covering map of topological stacks (Noohi, Definition 4.5 and Example 4.6(1), Definition 18.10), so $U$ is a topological stack (Noohi, Definition 13.8 and Example 13.1(6)) and is connected, being the image of $\widetilde U$; $\widetilde U$, being a manifold, is locally path connected and semilocally $1$-connected, so $U$ is too (Noohi, Definition 18.2); $\Gamma$ acts transitively on each fibre $\Gamma\tilde x$, so the covering is regular, its subgroup $p_*\pi_1(\widetilde U,\tilde x)$ is normal, and the deck transformations of a covering with normal subgroup $H$ are the automorphisms of the $\pi_1$-set $\pi_1^{\mathrm{orb}}(U,\tilde x)/H$, that is $\pi_1^{\mathrm{orb}}(U,\tilde x)/H$ (Noohi's Theorem 18.19, with Corollary 18.20 for the correspondence); so the deck group $\Gamma$ is $\pi_1^{\mathrm{orb}}(U,\tilde x)/p_*\pi_1(\widetilde U,\tilde x)$. This is the exact sequence of clause 1, and it gives the loop model: a loop $\lambda$ at $x$ is represented by its image $g\in\Gamma$ and the lift $\widetilde\gamma$ of $\lambda$, cut open at the base point, to a path from $\tilde x$ (Noohi, Proposition 18.18 and Lemma 18.12), whose end point is $g\tilde x$; a homotopy of loops lifts to a homotopy of these paths with $g$ constant, so the pair depends only on the class of the loop.

*The pullback along a loop, and the transport.* Let $\lambda$ be a loop at $x$ with pair $(g,\widetilde\gamma)$, and let $P\definedas\lambda^{-1}\widetilde U$ be the pullback of the chart, a $\Gamma$-torsor on $S^1$; over the interval it is trivialised by $\widetilde\gamma$, so $P|_I\cong I\times\Gamma$ and the two ends are identified by $(0,h)\sim(1,hg^{-1})$, because $(0,h)$ represents $(0,h\tilde x)$ and $(1,h')$ represents $(1,h'g\tilde x)$. Then $\lambda^{-1}\bT=(P\times T)/\Gamma$: over $I$ this is the trivial local system $I\times T$, the trivialisation being $(s,t)\mapsto[(s,\widetilde\gamma(s),t)]$, and the two ends are identified by $(0,t)\sim(1,\varphi(g)t)$, because $(0,\tilde x)=(1,\tilde x)$ and $(1,g\tilde x,\varphi(g)t)=(1,\tilde x,t)$. This is a local system on the space $S^1$; transport around $S^1$, referred to the base point through the trivialisation at $0$, is multiplication by $\varphi(g)^{-1}$ (@def:transport-and-monodromy, @lem:local-system-on-interval). The computation uses the definition of $\bT$ by its pullbacks and ordinary transport on the space $S^1$.

*$\rho$ is a homomorphism, and $\psi$ is an anti-homomorphism.* For composable loops $\lambda=(g,\widetilde\gamma)$ and $\mu=(h,\widetilde\delta)$, the composite $\lambda\mu$ --- that is $\mu$ followed by $\lambda$ in the convention of @def:transport-and-monodromy --- lifts from $\tilde x$ by $\widetilde\delta$ followed by the translate by $h$ of $\widetilde\gamma$, and ends at $hg\tilde x$; so $\psi(\lambda\mu)=hg=\psi(\mu)\psi(\lambda)$, $\psi$ is an anti-homomorphism, and
$$\rho(\lambda\mu)=\varphi(hg)^{-1}=\varphi(g)^{-1}\varphi(h)^{-1}=\rho(\lambda)\rho(\mu).$$
So $\rho=\varphi\circ\psi^{-1}$ is a homomorphism, and it is well defined on $\pi_1^{\mathrm{orb}}(U,\tilde x)$ because the pair depends only on the class of the loop.

*Surjectivity, and the kernel of $\psi$.* For $g\in\Gamma$ there is a path $\widetilde\gamma$ from $\tilde x$ to $g\tilde x$, because $\widetilde U$ is a connected manifold and hence path connected, and the pair $(g,\widetilde\gamma)$ is an orbifold loop at $x$ with $\psi(g,\widetilde\gamma)=g$; so $\psi$ is onto. The kernel of $\psi$ consists of the loops whose pair has group element $1$: these are the pairs $(1,\widetilde\gamma)$ with $\widetilde\gamma$ a path from $\tilde x$ to $\tilde x$, that is the loops of $\widetilde U$ at $\tilde x$, and two of them are equal in $\pi_1^{\mathrm{orb}}(U,\tilde x)$ exactly when the loops of $\widetilde U$ are homotopic, because a homotopy of pairs with group element $1$ is a homotopy of the paths. Hence $\ker\psi=p_*\pi_1(\widetilde U,\tilde x)$, which is $\pi_1(\widetilde U,\tilde x)$ by Noohi's Proposition 18.15, and the first sequence is exact.

*The image and the kernel of $\rho$.* From $\rho=\varphi\circ\psi^{-1}$ the image is $\varphi(\Gamma)$. A loop lies in $\ker\rho$ exactly when $\psi(\lambda)\in\ker\varphi$, so $\ker\rho$ is the preimage of $\ker\varphi$; the map $\ker\rho\to\ker\varphi$, $\lambda\mapsto\psi(\lambda)$, is onto because $\psi$ is onto, and its kernel is $\ker\psi=\pi_1(\widetilde U,\tilde x)$, so the second sequence is exact. If $\varphi$ is injective, $\ker\rho=\ker\psi=\pi_1(\widetilde U,\tilde x)$, and $\psi^{-1}$ induces an isomorphism $\pi_1^{\mathrm{orb}}(U,\tilde x)/\pi_1(\widetilde U,\tilde x)\iso\Gamma$.
:::

::: {.remark #rmk:orbifold-monodromy-depends-on-the-equivariant-structure title="The monodromy of a quotient is $\varphi(\Gamma)$ and not $\Gamma$"}

The image in @lem:orbifold-monodromy-of-a-quotient is $\varphi(\Gamma)$: the local system $\bT=(\widetilde U\times T)/\Gamma$ depends on the $\Gamma$-module structure and not on the quotient $U$ alone. Take $\widetilde U$ a point, $T=\ZZ$, and $\Gamma=C_2$ acting trivially on both; the point is a manifold and the action is properly discontinuous with stabilizer $C_2$, so the hypotheses of the lemma hold, and $U=[*/C_2]$ is the orbifold point with isotropy $C_2$; $\bT$ is the constant local system with fibre $\ZZ$, $\rho$ is trivial, and $\im\rho=1$ while $\ker\rho=C_2$, which is clause 2 for the trivial $\varphi$. The assertion that the image is $\Gamma$ for every $\Gamma$-module is false for this example; research#806 records the correction. The applications in this book take $\varphi$ to be the defining action of a subgroup of $\Aut(T)$, which is injective, and for those the image is $\Gamma$.
:::

::: {.theorem #thm:gamma-co-is-full title="G1 on the universal-family reading: the tautological local system has monodromy $\Orth^+(T_\Co)$"}

Let $M_\Co$ be base 1 of @def:coble-family-unpolarized, the coarse space of Coble surfaces, read with the orbifold structure for which the period map
$$\per\colon M_\Co\too\bD(T_\Co)/\Orth(T_\Co)$$
is an isomorphism of orbifolds onto an open substack of $\bD(T_\Co)/\Orth(T_\Co)$; the map is that of [@DK13, Prop. 3.2], whose coarse form is @lem:d2a-period-map, and this is the reading under which the tautological local system is a local system of lattices with fibre $T_\Co$; it is the universal-family reading of G1, and it is not the local system of D2a, whose base carries a family of its own (@def:coble-family-unpolarized, @lem:d2-local-system). Let $\bT$ be that local system, the pullback of the tautological local system of the quotient along $\per$, and let
$$\rho\colon\pi_1^{\mathrm{orb}}(M_\Co)\to\Orth(T_\Co)$$
be its monodromy representation (@def:transport-and-monodromy), whose image we write $\Gamma^{\mathrm{taut}}_\Co$. Then
$$\Gamma^{\mathrm{taut}}_\Co=\Orth^+(T_\Co).$$
This is the monodromy of the tautological local system and is not $\Gamma_\Co$ of @def:gamma-co-groups(1): the geometric family has its own local system over the labelled base, and its monodromy lies in $\widetilde\Orth^+(T_\Co)$ (@lem:coble-family-labelled-monodromy).
:::

::: {.proof}

*First inclusion: $\Gamma^{\mathrm{taut}}_\Co\subseteq\Orth^+(T_\Co)$.* The base $M_\Co$ is connected, so the period map is single-valued and its image lies in one of the two connected components of $\bD(T_\Co)$; write $\bD^+$ for that component (@prop:lifted-period-map). Transport is an isometry (@prop:local-system-of-lattices-monodromy), so every $\rho(\gamma)$ preserves $\bD^+$ (@cor:vhs-monodromy-stabilizes-component). The lattice $T_\Co$ carries the weight-$2$ Hodge structure of its K3 double cover; a holomorphic $2$-form is anti-invariant under the non-symplectic involution, so $h^{2,0}=1$, and the signature is $(2,9)$ (@prop:coble-transcendental), hence $h^{1,1}=9>0$. So the case $h^{m,m}>0$ of @thm:period-domain-component-stabilizer applies with $m=1$ and $\epsilon=1$, and
$$\Stab_{\Orth(T_\Co)}(\bD^+)=\Theta_\bR(T_\Co)=\Orth^+(T_\Co)$$
by @conv:spinor-positive-subgroup. Hence $\Gamma^{\mathrm{taut}}_\Co\subseteq\Orth^+(T_\Co)$.

*Second inclusion: $\Orth^+(T_\Co)\subseteq\Gamma^{\mathrm{taut}}_\Co$.* The quotient $\bD^+/\Gamma$ is an orbifold and not a manifold --- it is singular along the image of every fixed locus of codimension $\ge2$ [@Dim92, Ch. 4, Rem. (1.2)] --- so the argument is made on the smooth domain $\bD^+$. Put $\Gamma\definedas\Orth^+(T_\Co)$ and let $U\subseteq\bD^+/\Gamma$ be the image of the period map. By the choice of the orbifold structure, $M_\Co\to U$ is an isomorphism of orbifolds. Let $\widetilde U\subseteq\bD^+$ be the inverse image of $U$. The domain $\bD^+$ is a bounded symmetric domain, hence connected. The image $U$ of the period map is nonempty, and it is open by the hypothesis that $\per$ is an isomorphism of orbifolds onto an open substack; so $\widetilde U$ is a nonempty $\Gamma$-invariant open subset of $\bD^+$ and its complement $Z$ is a proper closed analytic subset (@def:closed-analytic-subset). It is connected: if $\bD^+\sm Z=A\sqcup B$ with $A,B$ nonempty open, take $a\in A$, $b\in B$ and a path (@def:path-connectedness) $\gamma$ in $\bD^+$ from $a$ to $b$; at the first point $t$ with $\gamma(t)\notin A$ one has $\gamma(t)\in Z$, and a ball $V\ni\gamma(t)$ has $V\sm Z$ connected --- a ball minus a proper analytic subset (@def:closed-analytic-subset) is connected --- and meeting both $A$ and $B$, a contradiction. So $\widetilde U$ is connected.

By its definition in D2a, the local system $\bT$ with its Hodge filtration is the pullback of the tautological local system $(\bD^+\times T_\Co)/\Gamma$ along the period map --- that is what it means for the period map to classify the variation (@prop:lifted-period-map(3)) --- so over $\widetilde U$ it is $(\widetilde U\times T_\Co)/\Gamma$. In that quotient $\Gamma=\Orth^+(T_\Co)$ acts on $T_\Co$ through its defining action, which is injective, so by @lem:orbifold-monodromy-of-a-quotient(2) its monodromy representation is
$$\pi_1^{\mathrm{orb}}(U,\tilde x)\too\Aut(T_\Co),\qquad (g,[\widetilde\gamma])\longmapsto\varphi(g)^{-1},$$
with image $\varphi(\Gamma)=\Gamma$, where $\varphi\colon\Gamma\injects\Aut(T_\Co)$ is the defining inclusion; in particular it is onto. Hence $\Gamma\subseteq\Gamma^{\mathrm{taut}}_\Co$, and the two inclusions give $\Gamma^{\mathrm{taut}}_\Co=\Orth^+(T_\Co)$.
:::


::: {.lemma #lem:gamma-co-labelled-index title="The labelled cover and the index $10!$"}

Let $B=V/\PGL_3$ and $\bar B=[V/(\SL_3\times S_{10})]$ be the labelled and unlabelled bases of @not:d2-plane-sextic-base, with the local system $\bT$ of @lem:d2-local-system and the monodromy groups
$$\Gamma_\Co(B)=\rho\qty{\pi_1(B,s)},\qquad \Gamma_\Co(\bar B)=\rho\qty{\pi_1(\bar B,s)}$$
of @lem:d2-labelled-base-monodromy and @lem:d2-local-system(4), the base point of $B$ lying over that of $\bar B$. Then
1. $\Gamma_\Co(B)=\Gamma_\Co(\bar B)\cap\ker\bar\rho$.
2. $[\Gamma_\Co(\bar B):\Gamma_\Co(B)]=\abs{\bar\rho\qty{\Gamma_\Co(\bar B)}}$, and $\bar\rho(\Gamma_\Co(\bar B))=\Theta$; so this index is $\abs{\Theta}=10!=3\,628\,800$ (@prop:gamma-co-geometric-bound(2), @lem:relabelling-discriminant-action(3)).
:::

::: {.proof}

The map $B\to\bar B$ is a principal $S_{10}$-bundle of stacks (@lem:d2-labelling-cover), so $\pi_1(B,s)$ is the kernel of the surjection $\pi_1(\bar B,s)\to S_{10}$; the classes $\varepsilon_i$ are permuted by the elements of $S_{10}$ and fixed by no other generator (@lem:d2-local-system(4)).

*First inclusion.* A loop of $\pi_1(B,s)$ acts trivially on the labels; hence it fixes each of the classes $\varepsilon_1,\dots,\varepsilon_{10}$ of @lem:d2-local-system(2), and it fixes $\varepsilon_0$ on every base. Its monodromy therefore acts trivially on $M$ and on $A_M$, hence, by @lem:coble-discriminant-actions-conjugate, trivially on $A_{T_\Co}$. So $\Gamma_\Co(B)\subseteq\Gamma_\Co(\bar B)\cap\ker\bar\rho$.

*Second inclusion.* Let $\gamma\in\pi_1(\bar B,s)$ with $\rho(\gamma)\in\ker\bar\rho$. Its monodromy acts trivially on $A_{T_\Co}$, hence, by @lem:coble-discriminant-actions-conjugate, trivially on $A_M$. The action of the label permutations on $A_M$ is faithful: $[h/2],[e_1/2],\dots,[e_{10}/2]$ is a $\ZZ/2$-basis of $A_M$, and a permutation $\sigma$ carries $[e_i/2]$ to $[e_{\sigma(i)}/2]$ and fixes $[h/2]$, so distinct permutations give distinct matrices (the same statement is [@YZZ25, Lemma 6.7 and its proof]). Hence $\gamma$ acts trivially on the labels, that is $\gamma\in\pi_1(B,s)$. Hence $\Gamma_\Co(\bar B)\cap\ker\bar\rho\subseteq\Gamma_\Co(B)$.

*The index.* The map $\bar\rho$ carries $\Gamma_\Co(\bar B)$ onto its image, with kernel $\Gamma_\Co(\bar B)\cap\ker\bar\rho=\Gamma_\Co(B)$ by the two inclusions, so
$$[\Gamma_\Co(\bar B):\Gamma_\Co(B)]=\abs{\bar\rho\qty{\Gamma_\Co(\bar B)}}.$$
That image is a subgroup of $\Theta$ (@prop:gamma-co-geometric-bound(2)) and it is $\Theta$: the relabelling arrows act on $T_\Co$ by the discriminant classes $\gamma\bar\rho_M(\sigma)\gamma^{-1}$ over all $\sigma\in\mathfrak S_{10}$, and that is $\Theta$ (@lem:relabelling-discriminant-action(3)); equivalently the label permutations are all realized by the monodromy of the unlabelled family. So the index is $\abs{\Theta}=10!$.
:::

::: {.lemma #lem:d2-monodromy-in-discriminant-kernel title="The forward inclusion from the lattice-polarized period theorem, and why the reverse is out of its reach"}

Let $M=\generators{2}\oplus\generators{-2}^{\oplus10}$ be the second summand $S_\Co$ of $\lkt$ and $N=M^{\perp\lkt}=T_\Co$ (@prop:coble-period-domain(2), [@DK13, (3.6)]). Then:

1. The monodromy group of the labelled base of @def:coble-family-unpolarized satisfies
$$\Gamma_\Co(B)\subseteq \Orth(N)^*\cap\Orth^+(N)=\widetilde\Orth^+(T_\Co),$$
where $\Orth(N)^*$ is the kernel of $\Orth(N)\to\Orth(A_N)$; this is [@Dol96, Prop. 3.3], whose hypotheses are those checked in the proof, applied through the marked period bijection of [@Dol96, Cor. 3.2].
2. The reverse inclusion is not available from that theorem, and no statement about the quotient $\bD(N)/\Orth(N)^*$ is: $-\id$ acts trivially on $\bD(N)$, so it lies in the kernel of the action of $\Orth(N)^*$ on the period domain, and the quotient determines a monodromy group only modulo $\{\pm\id\}$.
:::

::: {.proof}

1. The base $B$ of @def:coble-family-unpolarized(3) is the moduli space of $M$-polarized K3 surfaces *with the marking of $M$ fixed*: a point is a labelled ten-nodal sextic, the double cover $X_b$ is a K3 surface whose classes $e_0,\dots,e_{10}$ of @prop:coble-period-domain(1) are the labelled ones, and they generate $M$ primitively (@lem:d2-local-system(2)), so the pair $(X_b,M\subset H^2(X_b,\ZZ))$ is an $M$-polarized K3 surface with its polarization marked, and $B$ is the moduli of those by @lem:d2a-family-is-yzz.

By [@Dol96, Cor. 3.2] the period map is a bijection between marked ample $M$-polarized K3 surfaces and the open period domain, and by [@Dol96, Prop. 3.3] the group by which the marked period domain is quotiented to give that moduli space is $\Gamma_M=\Orth(N)^*$, where $\Gamma(M)$ is the pointwise stabilizer (@def:pointwise-stabilizer-of-sublattice) of $M$ in $\Orth(\lkt)$ and $\Gamma_M$ its image in $\Orth(N)$. So the monodromy group $\Gamma_\Co(B)$ of the presentation is contained in $\Orth(N)^*$.

The hypothesis of [@Dol96, Cor. 3.2] is ampleness with respect to the polarization, that is the period point avoiding the hyperplanes of $(-2)$-vectors of $N$; the general member of the family has $\Pic(X_b)=M$ (@prop:coble-period-domain(1), @lem:d2-local-system(2)), so its period lies in that open set. The further containment in $\Orth^+(N)$ is @lem:monodromy-is-spinor-positive, the periods being single-valued on the connected base $B$ (@lem:d2-incidence-connected(3)).

2. $\bD(N)$ is a domain of *lines*: a point is the line $H^{2,0}(X_b)\subset N\otimes\CC$ (@prop:coble-period-domain(1)). The isometry $-\id_N$ fixes every line, so it acts trivially on $\bD(N)$, and likewise on the domain of oriented positive $2$-planes used in [@Dol96]. Hence $\Orth(N)^*$ and $\Orth(N)^*/\{\pm\id\}$ have the same orbits (@def:group-orbit) and give the same quotient, and the deck group of the marked period domain over the moduli space is $\Orth(N)^*/\{\pm\id\}$. A monodromy group read off that quotient is therefore determined only modulo $\{\pm\id\}$, which is the statement of 2.
:::


::: {.lemma #lem:d2-arrangement-classes title="The classes $\gamma$ that cut the discriminant, and which of them can carry monodromy"}

Let $\Lambda_1=H^{\perp\Lambda}$, with $\Lambda_1\supseteq L\oplus Q$, $L=A_1^{\oplus10}$ and $Q=T_\Co$ (@lem:ten-a1-permutation-forces-strictness), and let $r\in\Lambda_1$ be a root, $r^2=-2$, $r\notin L$, written $r=t+s$ with $t\in L_\QQ$ and $s\in Q_\QQ$, with $\gamma\definedas2s$ as in @lem:d2-vanishing-reflections(2). Then:

1. *(Classification.)* The classes $\gamma$ that occur are exactly the vectors $\gamma\in Q$ for which there are $\lambda\in L$ and a root as above with
$$\lambda^2+\gamma^2=-8,\qquad \gamma=2s,\ \lambda=2t,\quad \bigl([\lambda/2],[\gamma/2]\bigr)\in H_0=\Lambda_1/(L\oplus Q).$$
Writing $\lambda=\sum_i n_i\ell_i$ gives $\gamma^2=-8+2\sum_i n_i^2$; so the squares that can occur are $-8,-6,-4,-2,0,2,4,\dots$, and each of them does occur for a suitable $\lambda$ ($\gamma^2=-2$ for $\lambda=\ell_1+\ell_2+\ell_3$, $\gamma^2=0$ for $\lambda=2\ell_1$, and so on), subject to the gluing condition.
2. *(Which can matter.)* A member of the family has $H=f^*\OO_{\PP^2}(1)$ for the double cover $f\colon X_b\to S_b\to\PP^2$ (@lem:d2-unpolarised-family(1)); this $H$ is nef and **not** ample, because $H\cdot\ell_i=0$ for the ten classes $\ell_i$ contracted by $f$, which are nonzero. So an earlier form of this clause was wrong: the negative definiteness of the orthogonal complement of an ample class does not apply, and the classes $\ell_i$ are effective algebraic classes orthogonal to $H$. In particular the components of $\calH_T$ with $\gamma^2\ge0$ are *not* excluded from the family by the Hodge index theorem, and no such exclusion is available.

3. *(What the meridians generate.)* So the components that can carry monodromy of the family are those with $\gamma^2\in\{-2,-4,-6,-8\}$. For $\gamma^2=-2$ the meridian is the reflection $s_\gamma$ (@lem:d2-vanishing-reflections(3), [@Voi07, Thm. 3.16]). For $\gamma^2\le-4$, if a loop of the family encircles that component its monodromy lies in $\widetilde\Orth^+(T_\Co)$, since $\Gamma_\Co\subseteq\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)) and it is a monodromy operator; in particular it is *not* the reflection $s_\gamma$, which for $\gamma^2=-4$ lies outside $\ker\bar\rho$ (@prop:gamma-co-reflective-set(3)). Consequently
$$W(T_\Co)\subseteq\generators{\text{meridians}}\subseteq\Gamma_\Co\subseteq\widetilde\Orth^+(T_\Co),$$
and no meridian of the family produces an element outside the stable group.
:::

::: {.proof}

1. That $2s\in Q$ and $\lambda=2t\in L$ hold, and that the class of the pair lies in $H_0$, is the lattice description of $\Lambda_1\supseteq L\oplus Q$: $\Lambda_1/(L\oplus Q)$ is the gluing subgroup, an elementary abelian $2$-group, so $2r\in L\oplus Q$. Then $4r^2=4(-2)=\lambda^2+\gamma^2$ is the displayed relation. Substituting $\lambda=\sum_in_i\ell_i$, whose square is $-2\sum_i n_i^2$ because the $\ell_i$ are orthogonal of square $-2$, gives $\gamma^2=-8+2\sum_in_i^2$; the values $0,1,2,3,4,\dots$ of $\sum_in_i^2$ give the listed squares, the corresponding $\lambda$ are as named, and each pair has to satisfy the gluing condition, which is what selects the subset that actually occurs.

2. A member of the family has $H=f^*\OO_{\PP^2}(1)$ for the double cover $f\colon X_b\to S_b\to\PP^2$ (@lem:d2-unpolarised-family(1)); this $H$ is nef and **not** ample, since $H\cdot\ell_i=0$ for the ten classes $\ell_i$ contracted by $f$ and those classes are nonzero. So the negative definiteness of the orthogonal complement of an ample class [@Huy05, Ch. 3] does not apply to $H^{\perp}$, and an algebraic class orthogonal to $H$ need not be excluded: the classes $\ell_i$ themselves are effective, algebraic and orthogonal to $H$. Hence the components of $\calH_T$ with $\gamma^2\ge0$ are *not* excluded from the family by the Hodge index theorem, and an earlier form of this clause, which drew that exclusion, was wrong.

3. The first containment is @lem:d2-vanishing-reflections(3)-(4) and the last is @thm:gamma-co-is-stable(1); the middle one is by definition, the monodromy group being generated by the monodromy of loops. For $\gamma^2=-4$, $s_\gamma\in\Orth^+(T_\Co)$ and $s_\gamma\notin\ker\bar\rho$ by @prop:gamma-co-reflective-set(3), so $s_\gamma\notin\widetilde\Orth^+(T_\Co)$; a monodromy operator lies in $\widetilde\Orth^+(T_\Co)$, hence cannot be $s_\gamma$.
:::

::: {.lemma #lem:d2-vanishing-reflections title="The square-$(-2)$ vectors of $T_\Co$, and the hyperplanes of the discriminant"}

Let $T_\Co=\generators{h}\oplus E_{10}(2)$ with $h^2=2$ (@def:gamma-co-groups), let $W(T_\Co)=\generators{s_v : v\in T_\Co,\ v^2=-2}$ be the short-root reflection group of @prop:gamma-co-reflective-set(1), and let $\Lambda_1=H^{\perp\Lambda}$ with $H$ the polarization class, so that $\Lambda_1\supseteq L\oplus Q$ with $L=A_1^{\oplus10}$ and $Q=T_\Co$ (@lem:ten-a1-permutation-forces-strictness). Then:

1. The vectors of square $-2$ in $T_\Co$ are exactly the vectors $ah+v$ with $a$ **odd** and $v\in E_{10}(2)$ of square $-2(a^2+1)$. In particular the coefficient of $h$ is not $\pm1$ in general, and there are infinitely many $h$-degrees among them. Each of them has divisibility $2$ and its reflection lies in $\widetilde\Orth^+(T_\Co)$ (@prop:gamma-co-reflective-set(1)).
2. The base is **not** identified with $\bD(Q)-\calH_T$: what @lem:d2a-family-is-yzz gives is that $B$ is the labelled moduli space of the family, and @lem:d2a-period-map gives its classifying map into $\bD(T_\Co)/\Gamma_\Co$, which is all that is used below; the components of $\calH_T$ are the divisors along which a member degenerates, and it is the meridian of such a divisor *in the base* that carries the local monodromy. Let $\calH_T$ be then the discriminant arrangement of @YZZ25, §3.3, the union of $r^{\perp}$ for the roots $r$ with $r^2=-2$, $r\perp H$, $r\notin L$. Every component of $\calH_T$ is of the form $\gamma^{\perp}$ for a vector $\gamma\in Q$ of square $4(-2-t^2)$ with $t\in L_\QQ$ of square $t^2\in 2\ZZ$, and conversely each $\delta\in Q$ with $\delta^2=-2$ contributes the component $\delta^{\perp}$. So the $(-2)$-arrangement is *contained* in $\calH_T$, and the containment is **strict**: for an isotropic $e\in U(2)\subset E_{10}(2)$ the vector $r=\ell_1+e$ has $r^2=-2+0+0=-2$, is orthogonal to $H$, and is not in $L$, so it is one of the roots defining $\calH_T$, while its hyperplane $r^{\perp}\cap\bD(Q)$ is $e^{\perp}$, the hyperplane of an *isotropic* class of $Q$ and not of a $(-2)$-class. Hence no description of the monodromy by the reflections $s_\delta$ alone can be complete.
3. For a component $\delta^{\perp}$ with $\delta^2=-2$ of the kind in 1, the local monodromy of the loop about it is the reflection $s_\delta$: this is the Picard--Lefschetz formula of [@Voi07, Thm. 3.16], $T(\alpha)=\alpha-\langle\alpha,\delta\rangle\delta$ for a surface, applied to the degeneration of @lem:d2-monodromy-in-discriminant-kernel whose vanishing class (@def:coble-marking-dictionary) is $\delta$. For the other components of 2 nothing of the kind is asserted.
4. Consequently, what the meridian argument gives is the containment
$$W(T_\Co)\subseteq\Gamma_\Co\subseteq\widetilde\Orth^+(T_\Co),$$
and no identification of $\Gamma_\Co$ with either of the two groups is asserted.
:::

::: {.proof}

1. Write $x=ah+v$ with $a\in\ZZ$ and $v\in E_{10}(2)$; then $x^2=2a^2+v^2$, and squares in $E_{10}(2)=U(2)\oplus E_8(2)$ are multiples of $4$ (in $U(2)$, with $e^2=f^2=0$ and $e\cdot f=2$, one has $(ae+bf)^2=4ab$; $E_8(2)$ is twice an even form). So $x^2=-2$ gives $2a^2\equiv-2\pmod 4$, that is $a$ odd, and then $v^2=-2-2a^2=-2(a^2+1)$. Conversely, for $a$ odd and $d\definedas-(a^2+1)/2\in\ZZ$, the vector $v=e+df\in U(2)$ has $v^2=4d=-2(a^2+1)$, so $ah+v$ has square $-2$; thus *every* odd $a$ occurs. Concretely $3h+e-5f$ has square $18-20=-2$, with $v^2=-20$: the earlier description by $\pm h+v$ with $v^2=-4$ was wrong, and it is the case $a=\pm1$ only. Divisibility $2$ is @lem:divisibilityAlwaysTwoTco, and the reflection of a square-$(-2)$ vector is in $\widetilde\Orth^+(T_\Co)$ by @prop:gamma-co-reflective-set(1).

2. Let $r\in\Lambda_1$ with $r^2=-2$ and $r\notin L$, and write $r=t+s$ with $t\in L_\QQ$ and $s\in Q_\QQ$. Since $L$ is primitive in $\Lambda$ and $\Lambda_1\cap L_\QQ=L$, we have $s\neq0$. For $q\in Q$ one has $(s,q)=(r,q)\in\ZZ$, so $s\in Q^*$; $Q=T_\Co$ is $2$-elementary, so $2s=:\gamma\in Q$ and $\gamma\neq0$.
A line $[\omega]\in\bD(Q)$ satisfies $(\omega,r)=(\omega,s)$ because $\omega\perp L_\QQ$, so $r^{\perp}\cap\bD(Q)=\gamma^{\perp}\cap\bD(Q)$: each component of $\calH_T$ is a hyperplane $\gamma^{\perp}$ with $\gamma\in Q$. Its square is $\gamma^2=4s^2=4(r^2-t^2)=4(-2-t^2)$, with $t^2\in2\ZZ$. For $t=0$ one has $r=s\in Q$ of square $-2$ and $\gamma=2r$ of square $-8$, which is the component $\delta^{\perp}$ for $\delta=r$; so every $\delta\in Q$ of square $-2$ contributes a component. For $t^2=-2$ one gets $\gamma^2=0$, an isotropic class, and such a component is not of the form $\delta^{\perp}$ with $\delta^2=-2$.

*The strictness is realized.* Take $t=\ell_1$, of square $-2$, and $s=e$, the isotropic vector of $U(2)\subset E_{10}(2)$ with $e^2=0$ and $e\cdot f=2$: then $r=\ell_1+e$ lies in $L+Q\subseteq\Lambda_1$, has $r^2=\ell_1^2+e^2+2(\ell_1,e)=-2+0+0=-2$, is orthogonal to $H$ (both summands are), and is not in $L$; and its $Q$-component is $s=e$, whose hyperplane is the one of the isotropic class $\gamma=2e$. So $\calH_T$ strictly contains the $(-2)$-arrangement.

3. The vanishing class of the nodal degeneration of @lem:d2-monodromy-in-discriminant-kernel has square $-2$ and lies in $Q$; the local monodromy is the reflection in it by [@Voi07, Thm. 3.16], whose hypotheses are those of a Lefschetz degeneration of surfaces, the central fibre being a K3 with one ordinary double point.

4. The containment $W(T_\Co)\subseteq\Gamma_\Co$ follows from 3 and @lem:d2-monodromy-in-discriminant-kernel; the second is @thm:gamma-co-is-stable(1). Part 2 shows that the arrangement which the meridian argument can use is $\calH_T$, which contains the $(-2)$-arrangement and possibly more, so no equality of $\Gamma_\Co$ with $W(T_\Co)$ follows: that would need every component of $\calH_T$ to be a $(-2)$-hyperplane, which part 2 leaves open.
:::



::: {.theorem #thm:gamma-co-is-stable title="G1: what is proved about the monodromy group, and the exact statement that remains"}

Let $H$ be the labelled base $B=V/\PGL_3$ of @def:coble-family-unpolarized(3), let $s\in H$, and let
$$\rho\colon\pi_1(H,s)\too\Orth(T_\Co)$$
be the monodromy representation of the local system $\bT$ of @lem:d2-local-system on the fibre at $s$, so that $\Gamma_\Co(B)=\rho\qty{\pi_1(H,s)}$ is the monodromy of that presentation of $\mcM_\Co$ (@def:gamma-co-groups(1)). Then:

1. $\Gamma_\Co(B)\cong\pi_1(H,s)/\ker\rho$ is a subgroup of $\widetilde\Orth^+(T_\Co)$. This is proved.
2. *Neither* equality is proved: neither $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$ nor $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$. For the first, a proof must supply an explicit, well-defined map $\pi_1(H,s)\to\widetilde\Orth^+(T_\Co)$ — equivalently a map on $\pi_1(H,s)/\ker\rho$ — which is surjective; no such map is exhibited below, and the two inclusions that would give it are stated as what is missing, not assumed. The second additionally needs $\Gamma_\Co=\Gamma_\Co(B)$, the identification of the stack's group with that of the presentation, which is research#797, item 6. Under @def:gamma-co-groups(1), research#780 asks for the equality for $\Gamma_\Co$ and therefore needs both.
:::

::: {.proof}

1. This is @lem:coble-family-labelled-monodromy; here is the same argument with the two halves named. The eleven classes $\varepsilon_0,\dots,\varepsilon_{10}$ are values of global sections of $\bV$ (@lem:d2-local-system(2)), so every $\rho(\gamma)$ fixes them and acts trivially on $M=\generators{2}\oplus\generators{-2}^{\oplus10}$ and hence on $A_M$. By @lem:coble-discriminant-actions-conjugate its discriminant action on $T_\Co$ is conjugate to its action on $A_M$, so it is trivial and $\rho(\gamma)\in\discriminantkernel{T_\Co}$; and $\rho(\gamma)\in\Orth^+(T_\Co)$ by @lem:monodromy-is-spinor-positive. Hence $\rho(\gamma)\in\widetilde\Orth^+(T_\Co)$. The isomorphism $\Gamma_\Co(B)\cong\pi_1(H,s)/\ker\rho$ is the first isomorphism theorem, $\rho$ being a homomorphism of groups.

2.
:::

::: {.remark #rmk:gamma-co-is-stable-context title="Why the reverse inclusion is open"}

The failure of the reverse inclusion is not a gap in one argument but the failure of three routes, recorded with the step that fails in @rmk:d2-routes-for-the-equality: the sextic-base orbifold route stops at $P\Gamma_T$ (@rmk:gamma-co-orbifold-obstruction), the reflection route stops because the discriminant arrangement is strictly larger than the $(-2)$-arrangement (@lem:d2-arrangement-classes), and the Enriques-side route is withdrawn because it relates $\Gamma_\Co$ to nothing: the description of the Coble family as the restriction of the Enriques family is a statement about *which* family it is, and identifying the monodromy of that restriction with a stabilizer requires exactly the map that the theorem asks for.
:::


::: {.remark #rmk:d2-marked-moduli-and-the-sign title="The marked moduli of Coble K3 covers, and what the generic stabilizer does to the count"}

This records the state of the route through the marked period domain, in the three steps it decomposes into, with the step that resists.

*(a1) Surjectivity.* By [@Dol96, Thm. 3.1] the period map of marked pseudo-ample $M$-polarized K3 surfaces is surjective onto the period domain $\bD(N)$, $N=M^{\perp\diamond}=T_\Co$; the hypotheses are that $M=\generators{2}\oplus\generators{-2}^{\oplus10}$ is primitive, even and of signature $(1,10)$, which is @prop:coble-is-the-ten-nodal-sextic-type. So every period in $\bD(T_\Co)$ is realized by an $M$-polarized K3.

*(a2) Injectivity.* For marked objects the period map is injective ([@Dol96, Cor. 3.2], from the global Torelli theorem). The involution needs no separate classification argument: under a marking that fixes $M$ pointwise, the covering involution acts on $M$ as $+1$ — $M=f^*\Pic(S)$ — and on $T_\Co$ as $-\id$ (@prop:coble-transcendental, [@DK13, §3]), and the two blocks determine the isometry of $\Lambda_{\mathrm{K3}}$ because $\Lambda\otimes\QQ=M\oplus T_\Co$. So the marked object determines the involution, and a Hodge isometry of the markings is one commuting with it.

*(a3) Reconstruction, and this is where the route resists.* That every marked $M$-polarized K3 with $\Pic=M$ is the K3 double cover of a Coble surface with its ten labels is *not* in the sources read: [@DK13, Prop. 3.2] places the classical Coble construction in an open subset of $\bD(N)/\Orth(N)$, one direction only, and neither [@YZZ25, Thm. 3.4] nor [@Dol96, Thm. 3.1] identifies the $M$-polarized K3s with the Coble covers. What the volume does prove is the converse, that the Coble family is a family of $M$-polarized K3s (@lem:d2-local-system), and the fibre identification with the family of type $10A_1$ (@lem:d2a-family-is-yzz).

*The generic stabilizer.* (c) of the route is @prop:gamma-co-images(1): the isometries of $T_\Co$ extending to $\Lambda_{\mathrm{K3}}$, commuting with the involution and fixing $M$ pointwise are $\Orth(N)^*=\widetilde\Orth(T_\Co)$, and intersecting with $\Orth^+$ gives $\widetilde\Orth^+(T_\Co)$ (@def:gamma-co-groups(3)). Since $-\id_{T_\Co}$ is one of them — it is $\restrictionof{\iota^*}{T_\Co}$ — and it acts trivially on $\bD(T_\Co)$, the quotient stack $(\bD(T_\Co)-Z)/G$ has **generic stabilizer $\{\pm\id\}\cong\{1,\iota\}$**: it is a $\ZZ/2$-gerbe over the base of the Coble-surface family, the gerbe class being the covering involution. Equivalently, the moduli stack of Coble K3 covers has generic stabilizer $\ZZ/2$ while the labelled base $B$ of @def:coble-family-unpolarized is a space (@lem:d2-plane-sextic-freeness(3)).

*What that does to the count.* If (a) held, then the marking cover of $B$ would be $\bD(T_\Co)-Z$ with deck group a subgroup of $G$, and $\Gamma_\Co$ would be the image of $\pi_1(B)$ under the period-quotient. The size of that image cannot be read off from $G$ alone, because $\pi_1(\bD(T_\Co)-Z)$ is not trivial: it is generated by the meridians of the arrangement $Z$, and those acts as the reflections $s_\delta$ (@lem:d2-vanishing-reflections(3)). So the order count that would give $\abs{\Gamma_\Co}=\abs{\widetilde\Orth^+(T_\Co)}$ from $\abs{G}=\abs{\widetilde\Orth(T_\Co)}=2\abs{\widetilde\Orth^+(T_\Co)}$ is not available: the kernel of $\pi_1(B)\to G$ is not known, and it is here — not in the equality of $G$ with the stabilizer, which is (c) and is proved — that the argument stops.
:::

::: {.remark #rmk:d2-routes-for-the-equality title="The three routes to the reverse inclusion, and the step at which each fails"}

The reverse inclusion $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_\Co$ of @thm:gamma-co-is-stable(2) has been attempted by three routes. Each is recorded here with the exact step that fails, so that the next attempt does not repeat it.

*1. The sextic base and the orbifold period theorem.* [@YZZ25, Thm. 3.4] gives $\mcm_T\cong\Gamma_T\backslash(\bD_T-\calH_T)$ and [@YZZ25, Prop. 6.6] with [@YZZ25, Prop. 6.5] upgrades it to the orbifold $P\Gamma_T\backslash(\bD_T-\calH_T)$, with $P\Gamma_T=\Gamma_T/\{\pm\id\}$ [@YZZ25, §6.1]. Since $-\id$ acts trivially on $\bD_T$ and as $-\id$ on the fibre $Q_F=T_\Co$, the lattice local system does not descend across that comparison, so the theorem identifies the period map and not the monodromy group; this is @rmk:gamma-co-orbifold-obstruction and it is where this route stops.

*2. Picard--Lefschetz reflections.* Each nodal degeneration gives the reflection $s_\delta$ in a vanishing class $\delta$ of square $-2$ (@lem:d2-vanishing-reflections), so $W(T_\Co)\subseteq\Gamma_\Co$. But the discriminant arrangement of the family is strictly larger than the $(-2)$-arrangement: for an isotropic $e$ the vector $\ell_1+e$ is a root whose hyperplane is $e^{\perp}$ (@lem:d2-arrangement-classes), the meridian of a component with $\gamma^2\le-4$ is not a reflection, and the components with $\gamma^2\ge0$ are not excluded by the Hodge index theorem, $H$ being nef and not ample (@lem:d2-arrangement-classes(2)). So this route gives the containment $W(T_\Co)\subseteq\Gamma_\Co\subseteq\widetilde\Orth^+(T_\Co)$ and cannot close it.

*3. The Enriques side.* The Coble locus is the $(-2)$-Heegner divisor of the Enriques period domain, so the Coble family is the Enriques family restricted to that divisor. It was proposed to read $\Gamma_\Co$ as the image of $\Stab_{\Gamma_\En}(\ZZ\delta)$ and then to use $R_{\Gamma_\En}=\widetilde\Orth^+(T_\Co)$ (@prop:gamma-co-images(1)). That is withdrawn, and the reason is worth stating exactly: a loop of the Coble base does not give an element of $\Stab_{\Gamma_\En}(\ZZ\delta)$ unless one already knows that the Coble base *is* the divisor modulo that stabilizer, which is a statement about the base and not a consequence of the restriction; and to relate the monodromy of the restricted family to the stabilizer one needs a map $\pi_1(H,s)\to\Stab_{\Gamma_\En}(\ZZ\delta)$, which loops around divisors do not supply. Relating $\Gamma_\Co$ to $T_\Co$'s isometries is precisely the theorem, so no step may assume it.

*What a proof must do.* By @thm:gamma-co-is-stable(2), it must exhibit an explicit, well-defined map $\pi_1(H,s)\to\widetilde\Orth^+(T_\Co)$, equivalently $\pi_1(H,s)/\ker\rho\to\widetilde\Orth^+(T_\Co)$, and show it onto. The natural candidate is the comparison of the base with a quotient of the period domain, and the precise obstruction there is that the identification of $H$ with $(\bD(T_\Co)-Z)/G$ for an explicit $G$ is *equivalent* to the equality: the deck group of $\bD(T_\Co)-Z\to H$ is by definition $\Gamma_\Co/(\Gamma_\Co\cap\{\pm\id\})$, so naming $G=\widetilde\Orth^+(T_\Co)$ as the group of that quotient assumes what is to be proved.
:::

::: {.remark #rmk:gamma-co-orbifold-obstruction title="Why the orbifold theorem of the source does not give $\Gamma_\Co(\bar B)=\Gamma_{10A_1}$"}

The period theorem of [@YZZ25, Thm. 3.4] is an isomorphism of \emph{coarse} spaces $\mcm_T\cong\Gamma_T\backslash(\bD_T-\calH_T)$. Its orbifold refinement, [@YZZ25, Thm. 1.1] together with [@YZZ25, Prop. 6.6] and the criterion [@YZZ25, Prop. 6.5], is an isomorphism of $\mcm_T$ with
$$P\Gamma_T\backslash(\bD_T-\calH_T),\qquad P\Gamma_T=\Gamma_T/\{\pm\id\},$$
the group used in [@YZZ25, §6.1]. Those two quotients are \emph{not} the same orbifold, and [@YZZ25, §6.1] says so: $-\id$ acts trivially on $\bD_T$, hence lies in every point stabilizer of $\Gamma_T\backslash(\bD_T-\calH_T)$ and in none of $P\Gamma_T\backslash(\bD_T-\calH_T)$.

The lattice local system cannot be carried across that comparison. Its fibre is $Q_F=T_\Co$, on which $-\id$ acts as $-\id$ (@prop:coble-discriminant-group), so an orbifold local system with fibre $Q_F$ does not descend to the $P\Gamma_T$-quotient, and the monodromy group of a local system is read on the orbifold whose stabilizers act on its fibre. Consequently the orbifold statement of the source identifies the period map, not the monodromy group of $\bT$, and $\Gamma_\Co(\bar B)=\Gamma_{10A_1}$ does not follow from it.

What would settle it is one of two inputs, neither of which is in this book or in the sources read: a loop of the labelled base carrying $-\id_{T_\Co}$ (@qst:gamma-co-sign-is-realised), or a statement in the lattice-polarized K3 literature that the monodromy group of the moduli of $M$-polarized K3 surfaces, for $M=\generators{2}\oplus\generators{-2}^{\oplus10}$ with its $A_1^{10}$ marking, is the discriminant kernel $\widetilde\Orth(T_\Co)$; the second implies the first, since $-\id$ lies in that kernel.
:::

::: {.question #qst:gamma-co-sign-is-realised title="The sign of the monodromy on the labelled base, and the stable-group equality it does not settle"}

Is there a loop of $B=V/\PGL_3$ whose monodromy on $T_\Co$ is $-\id$? The answer is yes: @prop:sign-is-a-loop-of-the-labelled-base exhibits one, so $-\id\in\Gamma_\Co(B)$, and $-\id$ is not an element that loops miss. That does *not* give $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$, which is @thm:gamma-co-is-stable(2): the sign is necessary for the equality and not sufficient (@rmk:the-sign-is-a-loop-not-a-missing-sign(2)), and the equality itself is @conj:gamma-co-stable. Nor does the sign give $\Gamma_\Co(\bar B)=\Gamma_{10A_1}$: by @thm:gamma-co-sextic-group(4) that identity is equivalent to $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$ and not to the sign. What the sign does give is that $\Gamma_\Co(B)$ is an index-two or larger subgroup of $\widetilde\Orth^+(T_\Co)$ containing $-W(T_\Co)$, with the bound of @rmk:the-sign-is-a-loop-not-a-missing-sign(3); every count stated for the stable quotient is a count for $\fco$ only under the equality.
:::
:::

::: {.proposition #prop:sign-is-a-loop-of-the-labelled-base title="A loop of the labelled base carries $-\id_{T_\Co}$"}

Let $W(T_\Co)$ be the group generated by the reflections $s_v$ in the $(-2)$-vectors $v$ of $T_\Co$ (@prop:gamma-co-reflective-set(1)), let $B=V/\PGL_3$ be the labelled base of @def:coble-family-unpolarized(3), and let $\Gamma_\Co(B)=\rho\qty{\pi_1(B,s)}$ (@def:gamma-co-groups(1)). Then
$$
W(T_\Co)\subseteq\Gamma_\Co(B),\qquad\text{and hence}\qquad -\id_{T_\Co}\in\Gamma_\Co(B),
$$
the second containment being @thm:coble-block-sign-in-w. Consequently the question @qst:gamma-co-sign-is-realised is answered positively: the sign is the monodromy of a loop of $B$, and it is not an element that loops miss.
:::

::: {.proof}

The discriminant arrangement of the family has components $\delta^{\perp}$ for $\delta$ a $(-2)$-vector of $T_\Co$ (@lem:d2-vanishing-reflections(2)), and these are divisors in the base: what the meridian of such a divisor carries is the local monodromy of the family over the base, and that monodromy is the reflection $s_\delta$ (@lem:d2-vanishing-reflections(3), by the Picard--Lefschetz formula of [@Voi07, Thm. 3.16]). A meridian of a divisor of $B$ is a loop of $B$, so $s_\delta\in\rho\qty{\pi_1(B,s)}=\Gamma_\Co(B)$ for every $(-2)$-vector $\delta$, which is the first containment. That $-\id_{T_\Co}\in W(T_\Co)$ is @thm:coble-block-sign-in-w, whose record is `computations/reports/coble_663-rel-lemma-c.py` with its `-run.txt` and its assertions in the `.json` beside them.
:::

::: {.remark #rmk:the-sign-is-a-loop-not-a-missing-sign title="What the loop carrying the sign does and does not settle"}

1. The closing sentence of @prop:coble-monodromy-is-the-marking-group(4) reads that no loop carries $\iota$, so that the image of $\pi_1(B)$ is an index-two subgroup and the two readings differ by exactly $\{\pm\id\}$. For the labelled base the first half is denied by @prop:sign-is-a-loop-of-the-labelled-base: the loop group already contains the sign, and the two readings do not differ by it. What @thm:no-loop-carries-the-sign establishes is a statement about the coarse space of the direct construction, not about $B$; the transfer between the two was recorded as unproved at the place where the sentence is written.
2. Nor does a loop carrying $-\id$ give the equality $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$: the sentence of @qst:gamma-co-sign-is-realised that reads the question as equivalent to that equality is an implication in one direction only, since the sign is necessary for the equality and not sufficient. The equality is @conj:gamma-co-stable and nothing here proves it.
3. What the sign does give is the finiteness of the index and a bound on it. With $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)) and $W(T_\Co)\subseteq\Gamma_\Co(B)$,
$$
[\widetilde\Orth^+(T_\Co):\Gamma_\Co(B)]\ \leq\ [\widetilde\Orth^+(T_\Co):W(T_\Co)],
$$
and the right-hand side is finite because $W(T_\Co)$ has finite index in $\Orth(T_\Co)$ (@thm:coble-block-sign-in-w). Its value is @qst:gamma-co-reflection-index and is not known; the index of the loop group in $\widetilde\Orth^+$ is therefore a finite number bounded by the reflection index, not the number $2$ that the sign was taken to produce.
:::

::: {.remark #rmk:no-loop-carries-the-sign-is-another-base title="Why a loop of $B$ may carry the sign while no loop of the direct construction's coarse space does"}

@thm:no-loop-carries-the-sign states that the monodromy of $T_\Co$ over the coarse moduli space $\mathfrak M$ of the direct construction, the space of @prob:B24, is $\Gamma^{\mathrm{dir}}_{\Co,2}/\{\pm\id\}$, so that no loop of $\mathfrak M$ carries $\iota$; @prop:sign-is-a-loop-of-the-labelled-base states that a loop of $B=V/\PGL_3$ does. Neither statement is withdrawn, and the two are consistent for two reasons.

1. They are about different bases. $\mathfrak M$ is the coarse space of the direct construction, whose objects are labelled Coble data with their $(H,\alpha)$; $B$ is the labelled base of @def:coble-family-unpolarized. No page identifies them, and the morphism between them is not written down.

2. $-\id$ acts trivially on the period domain: $[\omega]=[-\omega]$ in $\bP(T_\Co\otimes\CC)$, which is the sentence of the proof of @thm:no-loop-carries-the-sign. The period map therefore cannot separate $-\id$ from $\id$, and a loop that carries $-\id$ on the local system leaves every period fixed. This is why the sign can be a loop of $B$ on the local system and simultaneously the identity of the quotient taken at $\mathfrak M$: the quotient by $\{\pm\id\}$ is exactly the identification of the two.

The index is then a question about $W(T_\Co)$, not about the sign. Since
$$W(T_\Co)\subseteq\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co),$$
one has
$$[\widetilde\Orth^+(T_\Co):\Gamma_\Co(B)]\ \leq\ [\widetilde\Orth^+(T_\Co):W(T_\Co)]\ =\ \frac{[\Orth(T_\Co):W(T_\Co)]}{2\,\abs{\Orth(q_{T_\Co})}},$$
the denominator being $[\Orth(T_\Co):\widetilde\Orth^+(T_\Co)] = 2\abs{\Orth(q_{T_\Co})} = 93\,997\,183\,795\,200$ (@def:gamma-co-groups(3), @thm:two-elementary-surjectivity, @thm:gamma-co-sextic-group(3)). The numerator is finite (@thm:coble-block-sign-in-w) and is **not computed on the page**: the record of that theorem, `computations/reports/coble_663-rel-lemma-c.py` with its `-run.txt`, decides membership of $-\id$ in the group generated by the $1641$ distinct reflections of the diagonal model by a closure computation in the $2$-adic layers of $\Gamma(2)$; it does not compute the index $[\Orth(T_\Co):W(T_\Co)]$. Whether the inclusion $W\subseteq\Gamma_\Co(B)$ is an equality is the question that meridians alone do not settle, and it is the same defect the retired meridian criterion carried.
:::

::: {.proposition #prop:gamma-co-geometric-bound title="The discriminant image on each base"}

Let $\Gamma_\Co(B)$ and $\Gamma_\Co(\bar B)$ be the monodromy groups of the labelled and unlabelled bases of @def:coble-family-unpolarized, and $\Gamma_\Co$ that of the moduli stack (@def:gamma-co-groups(1)).

1. On the labelled base $B$, $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$, so $\bar\rho(\Gamma_\Co(B))=\theset{1}$ (@thm:gamma-co-is-stable(1)); the equality $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$ is @qst:gamma-co-sign-is-realised and is not proved.
2. On the unlabelled base $\bar B$, $\bar\rho(\Gamma_\Co(\bar B))\subseteq\Theta\definedas\gamma\,\bar\rho_M(\mathfrak S_{10})\,\gamma^{-1}$, where $\gamma\colon A_M\to A_N(-1)$ is the gluing isometry of @lem:coble-discriminant-actions-conjugate and $\mathfrak S_{10}$ permutes $e_1,\dots,e_{10}$ and fixes $e_0$. The group $\Theta$ is isomorphic to $\mathfrak S_{10}$, of order $10!$, and is a proper subgroup of $\Orth(q_{T_\Co})$ of index $2^{13}\cdot3\cdot17\cdot31=12\,951\,552$.
:::

::: {.proof}

(1) is @thm:gamma-co-is-stable. For (2), a point of $\bar B$ is a sextic together with its ten nodes as a set (@not:d2-plane-sextic-base), so the class $e_0=f^*H$ of the pullback of a line is the value of a global section of $\bV|_{\bar B}$, while the ten classes $e_1,\dots,e_{10}$ are permuted. A monodromy operator therefore fixes $e_0$ and acts on $M$ by an element of $\mathfrak S_{10}$, and @lem:coble-discriminant-actions-conjugate gives $\bar\rho(\Gamma_\Co(\bar B))\subseteq\gamma\bar\rho_M(\mathfrak S_{10})\gamma^{-1}$. That $\Theta\cong\mathfrak S_{10}$, and its index, is the computation of the same paragraph: the classes $[e_i/2]$, $i\ge1$, are permuted among themselves and $[e_0/2]$ is fixed, so $\mathfrak S_{10}\to\Orth(q_M)$ is injective (@def:injective-map), $|\Theta|=10!$, and $[\Orth(q_{T_\Co}):\Theta]=\abs{\Orth(q_{T_\Co})}/10!=2^{13}\cdot3\cdot17\cdot31$ by @prop:coble-discriminant-group.
:::

::: {.remark #rmk:gamma-co-coarse-space title="The coarse space carries no family"}

On the coarse space $M_\Co$ there is no family (@rmk:d2-what-is-open(1)); the tautological local system of the quotient has monodromy $\Orth^+(T_\Co)$ (@thm:gamma-co-is-full), which is not $\Gamma_\Co(B)$.
:::

::: {.lemma #lem:d2a-family-is-yzz title="The D2a family is the family $X_F$ of Yu--Zheng--Zhong"}

Let $\bar B$ be the unlabelled base of @def:coble-family-unpolarized(2), let $\mcx\to\mcs\to\bar B$ be the family of @lem:d2-unpolarised-family(3), and let $\bT$ be the local system of @lem:d2-local-system. Let $T=10A_1$, let $\mcv_T$ be the space of sextics of type $T$ and $\mcm_T=\mcv_T/\PGL_3$ [@YZZ25, §2.1], and let $Q_F=P_F^{\perp\Lambda_F}$ be the local system of [@YZZ25, §3.1]. Then the family $\mcx\to\mcs\to\bar B$ and the family $X_F\to\mcv_T$ of [@YZZ25, §2.3] have the same base up to labelling, the same fibres, and stalkwise the same lattice with the same generators; the local system $\bT$ has stalk (@def:stalk) $Q_F$ and the generating classes $H_F,\ell_1,\dots,\ell_{10}$ of [@YZZ25, §3.1]. What is *not* asserted is an identification of the two as equivariant local systems over the orbifold points; that is @rmk:gamma-co-orbifold-obstruction, and it is what the next theorem would need.
:::

::: {.proof}

*The bases.* A point of $\bar B$ is an irreducible plane sextic with its ten nodes as a set (@not:d2-plane-sextic-base), that is a sextic of the irreducible type $T=10A_1$; a sextic of type $T$ determines its singular set, so forgetting the labelling is a surjection $V\to\mcv_T$ whose fibres are the $10!$ orderings of the nodes, and quotienting by $S_{10}$ and $\PGL_3$ identifies $\bar B$ with $\mcm_T$.

*The fibres.* For a sextic $Z$ of type $T$, [@YZZ25, §2.3] defines $X_F$ as the minimal resolution (@def:minimal-resolution-of-surface-singularity) of the double cover of $\PP^2$ branched along $Z$. The fibre of @lem:d2-unpolarised-family(1) is the double cover of $\Bl_{p_1,\dots,p_{10}}\PP^2$ branched along the proper transform (@def:strict-transform) $C_b$ of $Z$. At a node of $Z$ the double cover has local equation $z^2=xy$, an $A_1$ singularity; blowing up the node replaces it by the exceptional curve, along which the proper transform of $Z$ is smooth of self-intersection $-4$, and the double cover branched along it is smooth there, the exceptional curve lifting to a $(-2)$-curve. That is the minimal resolution of the $A_1$ point, and the minimal resolution is unique, so the two constructions give the same K3 surface with the same covering involution and the same proper transform of $Z$.

*The local systems.* [@YZZ25, §3.1] puts $P_F=\generators{H_F}\oplus L_F$, with $L_F=A_1^{\oplus10}$ generated by the classes of the ten exceptional curves of the resolution and $H_F$ the class of the pullback of a line, and $Q_F=P_F^{\perp\Lambda_F}$. The span $\bM$ of @lem:d2-local-system(2) is generated by the class $\varepsilon_0$ of the pullback of a line and the classes $\varepsilon_1,\dots,\varepsilon_{10}$ of the ten exceptional curves, and $\bT=\bM^{\perp}$. By the identification of the fibres the two generating sets are the same classes of $H^2(X_F)$, so $P_F=\bM$ and $Q_F=\bT$.

The proof stops at the stalk, and that is all that is used. Two remarks on why the remaining comparisons are not needed for what this book proves.

*The labelled base has no isotropy to compare.* $\PGL_3$ acts freely on $V$ and $B=V/\PGL_3$ is a space (@lem:d2-plane-sextic-freeness(2)--(3)); on $B$ the local system $\bT$ is an ordinary local system of lattices, its monodromy is $\rho(\pi_1(B,s))$, and there is no stabilizer (@def:group-orbit) acting on a fibre to identify. Every statement this book makes about $\Gamma_\Co$ is a statement about $B$ (@def:coble-family-unpolarized(3), @lem:d2a-family-is-yzz).

*On the unlabelled base the comparison is not made, and nothing below needs it.* At a sextic carrying a projectivity that permutes its nodes, the image of that projectivity is an orbifold point of $\bar B$, and comparing the two families there would require the isotropy actions on the stalk to agree — the comparison that @rmk:gamma-co-orbifold-obstruction shows is obstructed.
:::

::: {.theorem #thm:gamma-co-sextic-group title="The sextic base: $\Gamma_{10A_1}=\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)$, and the two indices"}

Let $T=10A_1$, so that $P=\generators{H}\oplus L$ with $L=A_1^{\oplus10}$ and $Q=P^{\perp\Lkt}=T_\Co$ (@thm:occult-period-map-sextics, @lem:ten-a1-permutation-forces-strictness), and let $\Gamma_{10A_1}\le\Orth(T_\Co)$ be the group of [@YZZ25, §3.1] for that type: the image of $\Orth(\Lkt,\Delta,H)\to\Orth(Q)$, restricted to the subgroup preserving the component $\bD(Q)$. Let $\Theta\le\Orth(q_{T_\Co})$ be the image of the permutations of $e_1,\dots,e_{10}$ fixing $e_0$ (@prop:gamma-co-geometric-bound(2)). Then:

0. The unlabelled base $\bar B$ of @def:coble-family-unpolarized is the moduli stack of sextics of irreducible type $T=10A_1$, with coarse space $\mathcal M_T$, and the stalk (@def:stalk) of the local system $\bT$ of @lem:d2-local-system is the lattice $Q_F$ of [@YZZ25, §3.1] (@lem:d2a-family-is-yzz). The *group* identity $\Gamma_\Co(\bar B)=\Gamma_{10A_1}$ is **not** a consequence of this, for the reason recorded in @rmk:gamma-co-orbifold-obstruction; what holds is $\Gamma_\Co(\bar B)\subseteq\Gamma_{10A_1}$ (@prop:gamma-co-geometric-bound(2)), with the index of $\Gamma_\Co$ in $\Gamma_\Co(\bar B)$ equal to $\abs{\bar\rho(\Gamma_\Co(\bar B))}$ (@lem:gamma-co-labelled-index).
1. $\Theta\cong\mathfrak S_{10}$ and $|\Theta|=10!=3\,628\,800$.
2. $\Gamma_{10A_1}=\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)$.
3. $[\Gamma_{10A_1}:\widetilde\Orth^+(T_\Co)]=|\Theta|=10!$ and
$$[\Orth^+(T_\Co):\Gamma_{10A_1}]=\frac{\abs{\Orth(q_{T_\Co})}}{10!}=2^{13}\cdot3\cdot17\cdot31=12\,951\,552 .$$
4. $\widetilde\Orth^+(T_\Co)\subsetneq\Gamma_{10A_1}\subsetneq\Orth^+(T_\Co)$; on the family of @def:coble-family-unpolarized one has $\Gamma_\Co=\Gamma_\Co(B)\subseteq\Gamma_\Co(\bar B)\subseteq\Gamma_{10A_1}$ (@lem:d2-local-system(4), @prop:gamma-co-geometric-bound(2)), and $[\Gamma_\Co(\bar B):\Gamma_\Co(B)]=10!$ (@lem:gamma-co-labelled-index(2)). Since $\Gamma_\Co(\bar B)\subseteq\Gamma_{10A_1}$ with both discriminant images equal to $\Theta$, the identity $\Gamma_\Co(\bar B)=\Gamma_{10A_1}$ is equivalent to $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$, which is @qst:gamma-co-sign-is-realised and is *not* proved; clause (0) records why it is not a consequence of the identification of the stalk.
:::

::: {.proof}

(0). A point of $\bar B$ is an irreducible plane sextic with its ten nodes as a set (@not:d2-plane-sextic-base), which is the datum of a sextic of the irreducible type $T=10A_1$ in the sense of [@YZZ25, §2.1]; reducible sextics with ten nodes form a different type and are not points of $\bar B$. By @lem:d2a-family-is-yzz the two families have the same base, the same fibres and stalkwise the same lattice.

*What the period theorem does give.* By [@YZZ25, Thm. 3.4] the period map induces an isomorphism $\mathcal M_T\cong\Gamma_T\backslash(\bD_T-\mathcal H_T)$ of *coarse spaces*, and by [@YZZ25, Prop. 6.6] with [@YZZ25, Prop. 6.5] the period map preserves orbifold structures on the quotient $P\Gamma_T\backslash(\bD_T-\mathcal H_T)$ of [@YZZ25, Thm. 1.1].

*What it does not give, and why.* $P\Gamma_T=\Gamma_T/\{\pm\id\}$, and [@YZZ25, §6.1] states that $P\Gamma_T\backslash(\bD_T-\mathcal H_T)$ is a *different orbifold* from $\Gamma_T\backslash(\bD_T-\mathcal H_T)$: $-\id$ acts trivially on $\bD_T$, so it lies in every point stabilizer (@def:group-orbit) of the second and in none of the first. The lattice local system cannot be carried across that comparison either, because $-\id$ acts on the fibre $Q_F=T_\Co$ as $-\id$ (@prop:coble-discriminant-group) and not as the identity; an orbifold local system with fibre $Q_F$ therefore does not descend to $P\Gamma_T\backslash(\bD_T-\mathcal H_T)$. So the cited orbifold statement is a statement about the *period*, and it does not identify the monodromy group of $\bT$ with $\Gamma_T$. This is the one step of the labelled-base determination that is not available from the sources at hand, and it is recorded as @qst:gamma-co-sign-is-realised.

(1) is @prop:gamma-co-geometric-bound(2).

(2), *the inclusion $\subseteq$.* By [@YZZ25, §3.1] an element of $\Orth(\Lkt,\Delta,H)$ preserves $H$ and the set $\Delta=\theset{r_1,\dots,r_{10}}$ of the ten classes of the resolution. Hence its restriction to $P$ lies in $\Orth(P,H,\Delta)$, which is $\operatorname{Aut}(\Delta)\cong\mathfrak S_{10}$ and acts on $A_P\cong\ZZ/2\times(\ZZ/2)^{10}$ by permuting the ten generators $[r_i/2]$ and fixing $[H/2]$ [@YZZ25, Lemma 6.7]. By @lem:coble-discriminant-actions-conjugate the discriminant action on $Q=T_\Co$ is $\gamma\bar\rho_P(\psi)\gamma^{-1}$ for $\psi$ the restriction to $P$, so it lies in $\Theta$. That gives the inclusion into $\bar\rho^{-1}(\Theta)$; the inclusion into $\Orth^+(T_\Co)$ is the restriction to the component in the definition of $\Gamma_{10A_1}$ [@YZZ25, §3.1].

(2), *the inclusion $\supseteq$.* Let $\varphi\in\Orth^+(T_\Co)$ with $\bar\rho(\varphi)\in\Theta$. By [@YZZ25, Lemma 6.7] the map $\Orth(P,H,\Delta)\to\Orth(A_P)$ has image $\gamma^{-1}\Theta\gamma$, so there is $\psi\in\Orth(P,H,\Delta)$ with $\bar\rho_P(\psi)=\gamma^{-1}\bar\rho(\varphi)\gamma$; equivalently $\bar\rho(\varphi)=\gamma\bar\rho_P(\psi)\gamma^{-1}$, which by @lem:coble-discriminant-actions-conjugate is the condition that the pair $(\psi,\varphi)$ preserve the gluing subgroup of $P\oplus Q$ in $\Lkt$. By Nikulin's criterion [@Nik80, Cor. 1.5.2], which is @thm:automorphism-lifting-criterion, the pair then extends to an isometry $g\in\Orth(\Lkt)$ with $g|_P=\psi$ and $g|_Q=\varphi$. Since $\psi$ preserves $H$ and permutes $\Delta$, so does $g$; hence $\varphi$ is the restriction of an element of $\Orth(\Lkt,\Delta,H)$, and $\varphi\in\Gamma_{10A_1}$ because the restriction map $\Orth(\Lkt,H,\Delta)\to\Gamma_{10A_1}$ is an isomorphism: condition (ii) of [@YZZ25, Prop. 6.5], which holds for the irreducible nodal type $10A_1$ by [@YZZ25, Prop. 6.6].

(3). By @thm:two-elementary-surjectivity the map $\bar\rho\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is onto, its hypotheses being that $T_\Co$ is even, indefinite and $2$-elementary, which it is: $T_\Co=\generators{2}\oplus E_{10}(2)$ of signature $(2,9)$ (@prop:coble-period-domain(2)). The kernel $\ker\bar\rho$ contains the reflection $s_\zeta$ in a primitive vector $\zeta$ of square $2$, and $s_\zeta\notin\Orth^+(T_\Co)$ (@prop:gamma-co-reflective-set(2)); so of the two cosets of $\ker\bar\rho$ over a class $g\in\Orth(q_{T_\Co})$ one lies in $\Orth^+$, and $\bar\rho$ maps $\Orth^+(T_\Co)$ onto $\Orth(q_{T_\Co})$. Hence $\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)\to\Theta$ is onto with kernel $\Orth^+(T_\Co)\intersect\ker\bar\rho=\widetilde\Orth^+(T_\Co)$, so the first index is $|\Theta|=10!$, and the second is $|\Orth(q_{T_\Co})|/10!$ with $|\Orth(q_{T_\Co})|$ from @prop:coble-discriminant-group.

(4). Both indices in (3) exceed $1$. The last clause is @lem:gamma-co-labelled-index(2): the index of $\Gamma_\Co(B)$ in $\Gamma_\Co(\bar B)$ is $\abs{\bar\rho(\Gamma_\Co(\bar B))}$, read off the $S_{10}$-cover, and it is $\abs{\Theta}=10!$ because the relabelling arrows realize every element of $\Theta$ (@lem:relabelling-discriminant-action(3)); the containment $\Gamma_\Co(\bar B)\subseteq\Gamma_{10A_1}$ is the inclusion into $\bar\rho^{-1}(\Theta)$ with @thm:gamma-co-sextic-group(2). With $\bar\rho(\Gamma_\Co(\bar B))=\bar\rho(\Gamma_{10A_1})=\Theta$, the identity $\Gamma_\Co(\bar B)=\Gamma_{10A_1}$ is equivalent to $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$, and that is not proved, which is clause (0); the argument does not use the labelled-base theorem.
:::

::: {.corollary #cor:gamma-co-inclusions title="What G1 decides for the stable group"}

1. *The labelled base, the base of $\Gamma_\Co$* (@def:coble-family-unpolarized). What is proved is $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)); the identification $\Gamma_\Co=\Gamma_\Co(B)$ is research#797, item 6 (@def:gamma-co-groups(1)), so no inclusion for $\Gamma_\Co$ itself follows. The equality $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$, and with it @conj:gamma-co-stable on this base, is not proved: containing $-\id_{T_\Co}$ is necessary for it (@thm:gamma-co-is-stable(2)) and not sufficient (@rmk:the-sign-is-a-loop-not-a-missing-sign(2)), and where $\Gamma_\Co(B)$ sits inside $\widetilde\Orth^+(T_\Co)$ is @qst:gamma-co-sign-is-realised.
2. *The unlabelled base.* $\Gamma_\Co(\bar B)\subseteq\Gamma_{10A_1}=\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)$ (@thm:gamma-co-sextic-group(2), @prop:gamma-co-geometric-bound(2)), so
$$\widetilde\Orth^+(T_\Co)\subsetneq\Gamma_{10A_1}\subsetneq\Orth^+(T_\Co),\qquad[\Gamma_{10A_1}:\widetilde\Orth^+(T_\Co)]=10!,\qquad[\Orth^+(T_\Co):\Gamma_{10A_1}]=12\,951\,552 .$$
The inclusion $\Gamma_\Co(B)\subseteq\Gamma_\Co(\bar B)$ is @lem:d2-local-system(4), and $[\Gamma_\Co(\bar B):\Gamma_\Co(B)]=10!$ by @thm:gamma-co-sextic-group(4) with @lem:gamma-co-labelled-index(2). For $\Gamma_\Co$ itself the same inclusion is conditional on $\Gamma_\Co=\Gamma_\Co(B)$, which is research#797, item 6.
3. *The coarse space.* There is no family (@rmk:d2-what-is-open(1)); the tautological local system has monodromy $\Gamma^{\mathrm{taut}}_\Co=\Orth^+(T_\Co)$ (@thm:gamma-co-is-full), and
$$[\Orth^+(T_\Co):\widetilde\Orth^+(T_\Co)]=\abs{\Orth(q_{T_\Co})}=2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31=46\,998\,591\,897\,600$$
by @thm:two-elementary-surjectivity and @prop:coble-discriminant-group.
:::

::: {.remark #rmk:gamma-co-stable-quotient-counts title="Which quotient the stable counts describe"}

Accordingly the counts stated for the stable quotient --- $527$ $0$-cusps (@thm:coble-zero-cusp-count(2)) and $189\,720$ $1$-cusps (@thm:plane-fibre(3)) --- are counts for $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$, and are counts for $\fco$ only under that hypothesis.
:::

::: {.remark #rmk:gamma-co-d2a title="The three bases, and which group each gives"}

@def:coble-family-unpolarized has one family and three bases. On the labelled base $B$, the presentation that @def:gamma-co-groups(1) names, the group $\Gamma_\Co(B)$ is contained in $\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)), and the equality is @qst:gamma-co-sign-is-realised. On the unlabelled base $\bar B$ the group $\Gamma_\Co(\bar B)$ contains $\Gamma_\Co(B)$ with index $10!$ and is contained in $\Gamma_{10A_1}=\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)$, which contains $\widetilde\Orth^+(T_\Co)$ with index $10!$ and is contained in $\Orth^+(T_\Co)$ with index $12\,951\,552$ (@lem:gamma-co-labelled-index, @thm:gamma-co-sextic-group); whether $\Gamma_\Co(\bar B)$ is all of $\Gamma_{10A_1}$ is the equality $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$ again, and it is open (@thm:gamma-co-sextic-group(4)). On the coarse space $M_\Co$ there is no family; the tautological local system of the quotient is a different object, with group $\Orth^+(T_\Co)$ (@thm:gamma-co-is-full).

So the answer to G1 depends on the base, and the base is part of D2a; on the labelled base the group is $\Gamma_\Co(B)$, contained in $\widetilde\Orth^+(T_\Co)$ with the equality open. What is proved about the first two bases is $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{10A_1}$ (@thm:gamma-co-is-stable(1), @thm:gamma-co-sextic-group(3)); an inclusion for $\Gamma_\Co$ follows from that one exactly when $\Gamma_\Co=\Gamma_\Co(B)$, which is research#797, item 6 and is not proved; where in that chain the geometric group lies is @qst:gamma-co-sign-is-realised and the two equalities there are @conj:gamma-co-stable; and the index of $\Gamma_\Co(B)$ in $\Gamma_\Co(\bar B)$ is $\abs{\bar\rho(\Gamma_\Co(\bar B))}=10!$ (@lem:gamma-co-labelled-index).
:::

::: {.remark #rmk:gamma-co-status title="What is established about $\Gamma_\Co$, and what is open"}

Established, unconditionally, for the labelled base $H=B$ of @def:coble-family-unpolarized(3): $\Gamma_\Co(B)=\rho(\pi_1(H,s))$ (@lem:d2-labelled-base-monodromy), with $\Gamma_\Co(B)\cong\pi_1(H,s)/\ker\rho$ and $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1), three independent proofs of the inclusion); $\Gamma_\Co(B)=\Gamma_\Co(\bar B)\cap\ker\bar\rho$ with index $\abs{\bar\rho(\Gamma_\Co(\bar B))}=10!$ (@lem:gamma-co-labelled-index), so the unlabelled base is not contained in $\widetilde\Orth^+(T_\Co)$ (@lem:relabelling-discriminant-action(3)); $\Gamma_\Co(\bar B)\subseteq\Gamma_{10A_1}$, with $[\Gamma_{10A_1}:\widetilde\Orth^+(T_\Co)]=10!$ and $[\Orth^+(T_\Co):\Gamma_{10A_1}]=12\,951\,552$ (@thm:gamma-co-sextic-group); $W(T_\Co)\subseteq\Gamma_\Co(B)$ (@lem:d2-vanishing-reflections); and $-\id_{T_\Co}\in\Gamma_\Co(B)$, since $-\id_{T_\Co}\in W(T_\Co)$ (@thm:coble-block-sign-in-w) and $W(T_\Co)\subseteq\Gamma_\Co(B)$ (@lem:d2-vanishing-reflections(4)), a loop of the labelled base carrying the sign (@prop:sign-is-a-loop-of-the-labelled-base, reconciled with @thm:no-loop-carries-the-sign at @rmk:where-the-sign-is-a-loop). The earlier reading of the last clause, that $\Gamma_\Co\cap\{\pm\id\}$ is undetermined, is withdrawn. No statement here is made about $\Gamma_\Co$ itself: the identification $\Gamma_\Co=\Gamma_\Co(B)$ is research#797, item 6 (@def:gamma-co-groups(1)).

Open: the equality $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$, which is research#780 itself (@thm:gamma-co-is-stable(2)). Until it is settled the cusp counts of the stable quotient are *not* proved to be counts for $\fco$: $527$ $0$-cusps (@thm:coble-zero-cusp-count(2)) and $189\,720$ $1$-cusps (@thm:plane-fibre(3)) are counts for $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$, and are counts for $\fco$ only under the equality. The three routes and the step at which each fails are @rmk:d2-routes-for-the-equality, and the arithmetic index $\abs{\Orth(q_{T_\Co})}$ of @prop:coble-discriminant-group does not decide it.
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
vanishes in $\QQ/\ZZ$, that is exactly when $a = c$; the middle term vanishes because $b(A_{E_{10}(2)},[h/2]) = 0$, $T_\Co = \generators{h}\perp E_{10}(2)$ being an orthogonal sum. This is the set displayed in (1). For such a $z$ one has $z - a(h/2,\delta/2) = (0,y,0)$ with $a(h/2,\delta/2)\in H$, so $[z] = [(0,y,0)]$, and every class of $H^{\perp}/H$ is of this form. The map is injective (@def:injective-map) on these representatives: if $(0,y,0)\in H$, then $y$ is the $A_{E_{10}(2)}$-coordinate of $0$ or of $(h/2,\delta/2)$, and in both cases $y = 0$. Hence $\kappa$ is a bijection.

*(2)* $q_{T_\En}(\kappa(y)) = q_S(0,y,0) = q_{T_\Co}(y) = q_{E_{10}(2)}(y)$, the middle term because $q_{T_\En}$ is induced by $q_S$ on $H^{\perp}$ and $(0,y,0)\in H^{\perp}$, the last because $T_\Co = \generators{h}\perp E_{10}(2)$ is an orthogonal sum.

*(3)* Since $U$ is unimodular, $T_\En^* = U\oplus U(2)^*\oplus E_8(2)^*$, so the classes modulo $T_\En$ of $U(2)^*$ and of $E_8(2)^*$ are the two summands of $A_{T_\En} = A_{U(2)}\perp A_{E_8(2)}$. For $y\in A_{U(2)}$ or $y\in A_{E_8(2)}$ one has $y\in E_{10}(2)^* = U(2)^*\oplus E_8(2)^*\subseteq T_\Co^*\cap T_\En^*$, the $U(2)^*\oplus E_8(2)^*$ summand being common to $T_\Co^* = \generators{h/2}\oplus E_{10}(2)^*$ and to $T_\En^* = U\oplus E_{10}(2)^*$, and the class of $y$ modulo $T_\En$ is $\kappa(y) = [(0,y,0)]$; so $\kappa$ maps the two summands of $A_{E_{10}(2)}$ onto those of $A_{T_\En}$ and conjugates $\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ to the same product. For the last clause, $A_{T_\Co} = \generators{[h/2]}\perp A^0$ with $A^0 = A_{E_{10}(2)}$, so restriction is an isomorphism $\Orth(q_{T_\Co})\iso\Orth(q_{A^0})$, and it carries the stabilizer (@def:group-orbit) $P$ of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ to $\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ (@lem:coble-discriminant-blocks(3), (4)).

*(4)* Let $y\in A_{E_{10}(2)}$, represented by the functional that is $y$ on $E_{10}(2)$ and vanishes on $\generators{h}$ and on $\delta$. That representative lies in $E_{10}(2)^* = U(2)^*\oplus E_8(2)^*$, which is a summand of $T_\Co^* = \generators{h/2}\oplus E_{10}(2)^*$ and of $T_\En^* = U\oplus E_{10}(2)^*$; so $y$ may be read indifferently as a class of $A_{T_\Co}$ or of $A_{T_\En}$. The discriminant action of $g$ is $[x]\mapsto[g(x)]$ on $T_\En^*$. Since $g$ restricts to $\varphi$ on $T_\Co$ and fixes $\delta$, the functionals $g(y)$ and $\bar\rho_{T_\Co}(\varphi)(y)$ agree on $T_\Co$ and both vanish on $\delta$, hence are equal; note also that $\bar\rho_{T_\Co}(\varphi)$ preserves $A_{E_{10}(2)} = [h/2]^{\perp}$, because it fixes $[h/2]$. So
$$
\bar\rho_{T_\En}(g)(\kappa(y)) = [g(y)] = [\bar\rho_{T_\Co}(\varphi)(y)] = \kappa\bigl(\bar\rho_{T_\Co}(\varphi)(y)\bigr),
$$
which is the displayed identity. Its last clause is then immediate, and $\bar\rho_{T_\Co}(\varphi)$ acts on the direct sum $A_{T_\Co} = \generators{[h/2]}\perp A_{E_{10}(2)}$ as the identity on the first summand by hypothesis.
:::

::: {.proposition #prop:gamma-co-images title="The three restricted stabilizers"}
With $\delta$, $H$ and $R_\Gamma$ as in @def:gamma-co-groups, and $\bar\rho$ the discriminant representation (@def:discriminant-rep) of $T_\Co$:

1. $R_{\Gamma_\En} = \widetilde\Orth^+(T_\Co)$.
2. $R_{\Gamma^K_\En}$ is the stabilizer (@def:group-orbit) in $\Orth(T_\Co)$ of the class $[h/2]$ of $A_{T_\Co}$, and that stabilizer is all of $\Orth(T_\Co)$, because $[h/2]$ is the characteristic class of $q_{T_\Co}$:
$$
R_{\Gamma^K_\En} = \theset{\varphi\in\Orth(T_\Co)\ \mid\ \bar\rho(\varphi)(h/2) = h/2} = \Orth(T_\Co).
$$
3. $R_{\gent} = \bar\rho^{-1}(P)$, where $P\leq\Orth(q_{T_\Co})$ is the stabilizer of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ of the proof. It is a subgroup of $\Orth(T_\Co)$ of index $[\Orth(q_{T_\Co}) : P] = 2^7\cdot17\cdot31 = 67\,456$ (Step 6 of the proof), and it contains $\ker\bar\rho$.
:::

::: {.proof}

*Step 0: the two lattices and the gluing.* $T_\Co = \generators{h}\perp U(2)\perp E_8(2)$ and $T_\En = U\perp U(2)\perp E_8(2)$, and $\delta = \tilde e-\tilde f$ has $\delta^2 = -2$ and $\delta^{\perp T_\En} = \eta(T_\Co)$ (@lem:primitive_embedding_eta). By Nikulin's gluing theorem (@thm:nikulin-gluing, which is [@Nik80, Prop. 1.5.1]) an even overlattice of $T_\Co\perp\generators{\delta}$ is the same thing as an isotropic subgroup $H\subseteq A_{T_\Co}\oplus A_{\generators{\delta}}$, and $A_{(T_\Co\perp\generators{\delta})_H} = H^{\perp}/H$ as quadratic forms, the form on the quotient being the one induced by $q_{T_\Co}\oplus q_{\generators{\delta}}$ on $H^{\perp}$; here $H = \generators{(h/2,\delta/2)}$. Isotropy of this $H$ is the single congruence
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
- on $A_{U(2)}$, with the classes of $e'/2$ and $f'/2$ for the isotropic basis (@def:isotropic-basis-hyperbolic-plane) $e',f'$ of $U(2)$, $(e',f') = 2$: $q(e'/2) = q(f'/2) = 0$ and $q((e'+f')/2) = (e'+f')^2/4 = 1$, so $q\bmod1$ vanishes on this block and its two nonzero values are $0$ and $1$, both integers;
- on $A_{E_8(2)}$, with the classes of $\alpha_i/2$ for a basis $\alpha_i$ of $E_8$: $q(y/2) = y^2/2\in\bZ$ for every $y\in E_8$, so $q\bmod1$ vanishes here too, and $q$ on this block is the quadratic form $y\mapsto y^2/2\bmod 2\bZ$ of $E_8/2E_8$.

That $q$ takes values in $\tfrac12\bZ/2\bZ\cong\bZ/4$ and that the class $w$ below exists and is unique are Nikulin's statements for every even $2$-elementary lattice, and are why the argument needs $2$-elementarity: if $L$ is even and $2$-elementary then $2x\in L$ for $x\in L^*$, hence $q(x) = x^2$ lies in $\tfrac12\bZ/2\bZ$; $x\mapsto q(x)\bmod1$ is therefore a linear function $A_L\to\tfrac12\bZ/\bZ$, and since $b$ is nondegenerate there is a *unique* $w$ with $b(w,x)\equiv q(x)\pmod1$ for all $x$, the characteristic element of $q$; it is additive over orthogonal sums, $w_{q_1\oplus q_2} = w_{q_1}\oplus w_{q_2}$, and it is $0$ exactly when $q$ is $\bZ$-valued [@Nik80, §3.9--150]. Applied to $q_{T_\Co} = q_{\generators{h/2}}\oplus q_{E_{10}(2)}$ this gives $w = [h/2]$ in one line: $q(h/2) = h^2/4 = 1/2 = b(h/2,h/2)$ makes $[h/2]$ the characteristic element of the first summand, and $q_{E_{10}(2)}$ is $\bZ$-valued, $q(y/2) = y^2/2\in\bZ$ for $y\in E_{10}$, so its characteristic element is $0$. Hence for every isometry $\sigma$ of $(A_{T_\Co},q)$ and every $x$,
$$
b(\sigma(h/2),x) = b(h/2,\sigma^{-1}x)\equiv q(\sigma^{-1}x) = q(x)\equiv b(h/2,x)\pmod1,
$$
and nondegeneracy of $b$ gives $\sigma(h/2) = h/2$: every isometry of $q_{T_\Co}$ fixes $[h/2]$. This is the case $k = [h/2]$ of @lem:coble-discriminant-blocks(3), which proves the same thing for every form of the shape $\bZ k\perp A^0$; the argument is repeated here because (1) and (3) both use it, and because the vanishing of $q\bmod1$ has to be checked on the two blocks separately, with a different reason in each.

*Step 2: which isometries of $T_\Co$ lift over $\delta$.* Let $g\in\Orth(T_\En)$ fix $\delta$. Then $g$ preserves $\delta^{\perp T_\En} = \eta(T_\Co)$, so after scalar extension $g = \varphi\oplus\id_{\generators{\delta}}$ with $\varphi = \restrictionof{g}{T_\Co}$; in particular the restriction map $\Stab_{\Orth(T_\En)}(\delta)\to\Orth(T_\Co)$ is injective (@def:injective-map). And $\varphi\oplus\id$ preserves the overlattice $T_\En$ exactly when $(\bar\rho(\varphi)\oplus\id)(H) = H$ (@thm:automorphism-lifting-criterion, which is [@Nik80, Cor. 1.5.2] applied to the gluing datum of @def:gluing-datum-of-a-pair). The elements of $H$ are $0$ and $(h/2,\delta/2)$, and the second coordinate of $(\bar\rho(\varphi)\oplus\id)(h/2,\delta/2)$ is $\delta/2\neq0$, so the condition is $\bar\rho(\varphi)(h/2) = h/2$. Conversely that condition makes $\varphi\oplus\id$ preserve $H$, hence extend to an isometry of $T_\En$, which fixes $\delta$. So $\varphi$ extends to an isometry of $T_\En$ fixing $\delta$, uniquely, exactly when it fixes $[h/2]$; on discriminant groups, $\varphi\oplus\id$ acts by $\bar\rho(\varphi)$ on $A_{E_{10}(2)}$, which $\kappa$ identifies with the whole of $A_{T_\En}$ (@lem:gluing-discriminant-identification(4)).

*Step 3: part (2).* By Step 1 every isometry of $q_{T_\Co}$ fixes $[h/2]$, and by @thm:two-elementary-surjectivity ([@Nik80, Thm. 3.6.3]) the map $\bar\rho\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is onto, its hypotheses being exactly that $T_\Co$ is even, indefinite and $2$-elementary, which the table gives; $T_\Co$ is moreover the case $a = t_{(+)}+t_{(-)}$ of the proof of the theorem, $11 = 2+9$, where Nikulin reduces to the orthogonal summand $u_+^{(2)}(2)$ or $\upsilon_+^{(2)}(2)$ that $q_{T_\Co}$ has in its $U(2)$ block [@Nik80, Thm. 3.6.3]. So every $\varphi\in\Orth(T_\Co)$ satisfies the condition of Step 2, and
$$
\Stab_{\Orth(T_\En)}(\delta) = \theset{\varphi\oplus\id_{\generators{\delta}}\mid\varphi\in\Orth(T_\Co)}\;\cong\;\Orth(T_\Co),
$$
the restriction map being the inverse. That is (2), and with it: every isometry of $T_\Co$ extends to an isometry of $T_\En$ fixing $\delta$.

*Step 4: part (1).* Let $g = \varphi\oplus\id$ fix $\delta$. By @lem:gluing-discriminant-identification(4), $g\in\discriminantkernel{T_\En}$ exactly when $\bar\rho(\varphi)$ acts trivially on $A_{E_{10}(2)}$; since $\bar\rho(\varphi)$ fixes $[h/2]$ (Step 1) and $A_{T_\Co} = \generators{h/2}\oplus A_{E_{10}(2)}$, that holds exactly when $\bar\rho(\varphi) = \id$. For the sign, recall that $\Orth^+(L) = \Theta_\bR(L) = \ker\spinornorm_\bR$ is the kernel of the real spinor norm [@def:lattice-spinor-kernels], and that $g = \varphi\perp\id_{\generators{\delta}}$ is an orthogonal sum. The spinor norm is multiplicative on an orthogonal sum,
$$
\spinornorm_\bR(\varphi\perp\psi) = \spinornorm_\bR(\varphi)\,\spinornorm_\bR(\psi),
$$
because a reflection $s_w$ with $w\in T_\Co\tensor\bR$ acts on $T_\En\tensor\bR$ as the reflection in the same vector, with the same value $\spinornorm_\bR(s_w) = [-\tfrac12w^2]$ [@def:spinor-norm], and $\varphi\perp\psi = (\varphi\perp\id)(\id\perp\psi)$. So $\spinornorm_\bR(g) = \spinornorm_\bR(\varphi)\cdot\spinornorm_\bR(\id) = \spinornorm_\bR(\varphi)$, and $g\in\Orth^+(T_\En)$ exactly when $\varphi\in\Orth^+(T_\Co)$.

The sign is not read off positive definite subspaces, and the tempting argument that it is, is false: $\delta^2<0$ does not place every maximal positive definite subspace (@def:maximal-positive-definite-subspace) of $T_\En\tensor_\bR$ inside $\delta^{\perp}$, since $\eta(h)$ and $e'+f'+\delta$ span a positive definite plane --- of the maximal dimension $2$ --- with $(\eta(h),e'+f'+\delta) = 0$ and $(e'+f'+\delta,\delta) = -2$. What is true is the spinor statement above, and it is what the proof uses. So restriction carries $\Stab_{\Gamma_\En}(\delta)$ into $\widetilde\Orth^+(T_\Co)$; conversely, for $\varphi\in\widetilde\Orth^+(T_\Co)$ the element $\varphi\oplus\id$ lies in $\Stab_{\Gamma_\En}(\delta)$ by the two characterizations just proved. That is (1).

*Step 5: part (3).* By @prop:sterk-group-identification(2), $\gent = \rho^{-1}(M)$ with $M = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ the subgroup of $\Orth(A_{T_\En},q)$ preserving the decomposition, the identification of $\gent$ with the group of [@AEGS25, Def. 2.6] being @prop:sterk-group-identification(1) and the description by the two summands being [@Ste91, Prop. 2.7]. So $g = \varphi\oplus\id$ fixing $\delta$ lies in $\gent$ exactly when $\bar\rho(\varphi)$ preserves $A_{U(2)}$ and $A_{E_8(2)}$, the summands of $A_{T_\En}$ being $\kappa$ of the summands of $A_{E_{10}(2)}$ (@lem:gluing-discriminant-identification(3)). Every $\sigma\in\Orth(q_{T_\Co})$ fixes $w = [h/2]$ (Step 1), hence preserves $w^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$, of dimension $10$; so restriction $\Orth(q_{T_\Co})\to\Orth(w^{\perp},q|_{w^{\perp}})$ is defined, and it is injective because an isometry fixing $w^{\perp}$ pointwise fixes $w$ too, $A_{T_\Co} = \generators{w}\oplus w^{\perp}$. The condition is therefore $\bar\rho(\varphi)\in P$, where $P$ is the stabilizer in $\Orth(q_{T_\Co})$ of the decomposition $w^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$, and $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ by @lem:coble-discriminant-blocks(4). So $R_{\gent} = \bar\rho^{-1}(P)$, and it contains $\ker\bar\rho$.

*Step 6: the index.* Because $\bar\rho$ is onto (Step 3), $[\Orth(T_\Co):R_{\gent}] = [\Orth(q_{T_\Co}):P]$, and by orbit--stabilizer the latter is the number of elements in the orbit (@def:group-orbit) of the decomposition $D\colon w^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$. Let $N$ be the number of decompositions of $w^{\perp}$ into a $2$-dimensional summand isometric to $A_{U(2)}$ and an $8$-dimensional one isometric to $A_{E_8(2)}$; the orbit lies in that set, so $[\Orth(q_{T_\Co}):P]\leq N$. The two are computed separately, and they agree.

*(i) $N = 67\,456$.* On $w^{\perp}$ the form $q$ is $\bZ$-valued (Step 1), so $(w^{\perp},q)$ is a quadratic space over $\bF_2$, and it is of plus type: $528$ of its classes have $q = 0$, the zero class included, and $496$ have $q = 1$ (@lem:coble-discriminant-blocks(2), whose count $3\cdot136+1\cdot120 = 528$ is this one). A $2$-dimensional subspace of $w^{\perp}$ is isometric to $A_{U(2)}$ exactly when it is spanned by classes $a,b$ with $q(a) = q(b) = 0$ and $b(a,b) = 1/2$, for then $q(a+b) = 1$ and $b$ is nondegenerate on the span. There are $527$ choices for $a$; for fixed $a$ the classes with $b(a,b) = 1/2$ form an affine hyperplane of order $2^9 = 512$, and the translation $b\mapsto b+a$ preserves it and sends $q(b)$ to $q(b)+q(a)+b(a,b) = q(b)+1$, so exactly $256$ of them have $q(b) = 0$; each subspace is counted twice, through its two classes of value $0$. Hence
$$
N = \frac{527\cdot 256}{2} = 527\cdot 128 = 2^7\cdot17\cdot31 = 67\,456 .
$$
The orthogonal complement of such a subspace is a plus space of dimension $8$, that is $A_{E_8(2)}$ up to isometry, so every such subspace is one of the decompositions counted by $N$.

*(ii) $\abs{\Orth(q_{T_\Co})}/\abs{P} = 2^7\cdot17\cdot31$.* Here $\Orth(q_{T_\Co})\cong\Orth(w^{\perp},q)$ is the orthogonal group of a hyperbolic space of dimension $10$, and $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$. The restriction is an isomorphism, not only an injection: an isometry of $w^{\perp}$ extends by $w\mapsto w$, and that is an isometry because $\generators{w}\perp w^{\perp} = A_{T_\Co}$. Both orders are counts of ordered hyperbolic bases, an isometry of a hyperbolic space being determined by, and determining, the image of one fixed hyperbolic basis, and in dimension $2m$ the first hyperbolic pair (@def:isotropic-basis-hyperbolic-plane) can be chosen in $(2^{2m-1}+2^{m-1}-1)\cdot2^{2m-2}$ ways. This gives $\abs{\Orth(q_{U(2)})} = 2$, then $\abs{\Orth(q_{E_8(2)})} = 2\cdot(9\cdot4)\cdot(35\cdot16)\cdot(135\cdot64) = 348\,364\,800$, then $\abs{P} = 2\cdot 348\,364\,800 = 696\,729\,600 = \abs{W(E_8)}$ and $\abs{\Orth(q_{T_\Co})} = 527\cdot256\cdot 348\,364\,800 = 46\,998\,591\,897\,600 = 2^{21}3^55^27\cdot17\cdot31$, so that
$$
\frac{\abs{\Orth(q_{T_\Co})}}{\abs{P}} = 2^7\cdot17\cdot31 = 67\,456 .
$$
Both computations are in `computations/reports/coble_788-gamma-co-images-index-run.txt`, which also verifies the quadratic-form relation on all $2^{22}$ pairs, the characteristic class on all $2048$ classes, the plus type of $w^{\perp}$ and the type of the $67\,456$ complements. Since the orbit has $67\,456$ elements and the set it lies in has $67\,456$ elements, the orbit is that whole set and
$$
[\Orth(T_\Co):R_{\gent}] = [\Orth(q_{T_\Co}):P] = 2^7\cdot17\cdot31 = 67\,456 .
$$
The number is published, and the two orders are the two in the source: [@Ste91, Rem. 2.12] computes $[\Orth(L_-):\Gamma] = (2^{21}3^55^27\cdot17\cdot31)/(2\cdot2^{13}3^55^27) = 2^7\cdot17\cdot31$, and $[\Orth(L_-):\Gamma] = [\Orth(q_{T_\Co}):P]$ because $\kappa$ identifies $A_{T_\En}$ with $A_{E_{10}(2)}$ and carries $M$ to $P$ (@lem:gluing-discriminant-identification(2), (3), with the restriction $\Orth(q_{T_\Co})\iso\Orth(q_{E_{10}(2)})$ of @lem:coble-discriminant-blocks(3)), the lattice $L_-$ of the source being $T_\En$ summand by summand (@prop:sterk-group-identification(1)), and $\Gamma$ is $\gent$, whose discriminant image is $M = P$. The same number is the index in $\Orth^+$: the vector $\zeta\definedas h$ is primitive of square $2$, so $s_\zeta\in\ker\bar\rho\subseteq R_{\gent}$ and $s_\zeta\notin\Orth^+(T_\Co)$ (@prop:gamma-co-reflective-set(2), which proves both halves for a primitive vector of square $2$). The first holds because $s_\zeta(x^*) - x^* = -b(x^*,\zeta)\zeta$ lies in $T_\Co$ for every $x^*\in T_\Co^*$, a reflection in a vector of square $2$ being discriminant-trivial; the second because $\spinornorm_\bR(s_\zeta) = [-\tfrac12\zeta^2] = [-1]$ is not the identity (@prop:gamma-co-reflective-set(2), @def:spinor-norm). Hence $R_{\gent}\cdot\Orth^+(T_\Co) = \Orth(T_\Co)$, and
$$
[\Orth^+(T_\Co):R_{\gent}\intersect\Orth^+(T_\Co)] = [\Orth(T_\Co):R_{\gent}] = 67\,456 .
$$
:::

::: {.remark #rmk:gamma-co-images-inputs title="What each step of @prop:gamma-co-images needs, and where it stands"}

Each step of the proof above rests on a statement that the step itself does not prove. The eleven such statements are listed below with the step that uses each and with its status; *proved* means proved on this page, and the numbered source is the numbered statement that supplies the mathematical content, with its section. The list is the check that no step carries more than it says.

1. *$T_\Co$ is even, of signature $(2,9)$ and $2$-elementary with $a = 11$.* Needed in Step 1 (for $q$ to take values in $\tfrac12\bZ/2\bZ$), Step 0 ($\abs{A_{T_\Co}} = 2^{11}$) and Step 3 (the three hypotheses of Nikulin's theorem). Status: proved --- @prop:theta-co-exists with the table of the notation block at the head of this chapter; the isometry class is [@DK13, (3.6)] and [@Nik80, Thm. 3.6.2].
2. *$H = \generators{(h/2,\delta/2)}$ is isotropic.* Needed in Step 0: otherwise $(T_\Co\perp\generators{\delta})_H$ is not even and Nikulin's gluing theorem does not apply to it. Status: proved --- the one congruence displayed in Step 0.
3. *$[h/2]$ is the characteristic class of $q_{T_\Co}$, i.e. $b(h/2,x)\equiv q(x)\pmod1$ for all $x$.* Needed in Step 2, where the lifting condition becomes automatic, and hence in (2). Status: published --- [@Nik80, §3.9--150] proves existence and uniqueness of the characteristic element of an even $2$-elementary form and its additivity over orthogonal sums; Step 1 identifies it with $[h/2]$ on the two summands, and @lem:coble-discriminant-blocks(3) proves the same thing in the shape $k\perp A^0$.
4. *$b$ is nondegenerate on $A_{T_\Co}$.* Needed in Step 1 for the uniqueness of the characteristic class, and so for the passage from (2) to (3). Status: published --- the discriminant form of a nondegenerate lattice is nondegenerate [@Nik80, §1.3].
5. *$\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is onto.* Needed in Step 3 and in Step 6, and it is what turns "every isometry of the discriminant form" into "every isometry of the lattice". Status: published --- [@Nik80, Thm. 3.6.3] = @thm:two-elementary-surjectivity, the hypotheses being verified in Step 3.
6. *$\gent$ is the group of [@AEGS25, Def. 2.6], and that group is the set of isometries of $T_\En$ whose discriminant action preserves the two summands $A_{U(2)}$, $A_{E_8(2)}$.* Needed in Step 5: without it $R_{\gent}$ is the image of a group that has not been identified with the group of the published degree-two family. Status: page proof --- @prop:sterk-group-identification(1), (2), resting on [@AEGS25, Defs. 2.6--2.7] and [@Ste91, Prop. 2.7]. This is the step that identifies the group of the published degree-two Enriques family; it is a statement about an arithmetic group, and the monodromy group $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5) is a different group, no inclusion between it and $R_{\gent}$ being asserted here.
7. *$\Orth^+$ is the kernel of the real spinor norm, and the spinor norm is multiplicative on an orthogonal sum, so $\spinornorm_\bR(\varphi\perp\id) = \spinornorm_\bR(\varphi)$.* Needed in Step 4 for the sign. It cannot be replaced by an argument about positive definite subspaces: $\delta^2<0$ does not put every maximal positive definite subspace of $T_\En\tensor\bR$ inside $\delta^{\perp}$, since $\eta(h)$ and $e'+f'+\delta$ span one with $(e'+f'+\delta,\delta) = -2$. Status: definition plus the reflection formula of @def:spinor-norm, and multiplicativity is what the exact sequence of @def:lattice-spinor-kernels asserts.
8. *The restriction $\Stab_{\Orth(T_\En)}(\delta)\to\Orth(T_\Co)$ is injective.* Needed for an equality, not only an inclusion, in (2) and (3): an isometry fixing $\delta$ and acting trivially on $\delta^{\perp T_\En}$ is the identity. Status: proved --- Step 2, where the scalar extension of $g$ is $\varphi\oplus\id$.
9. *The line stabilizer $\Stab_{\gent}(\ZZ\delta)$ and the vector stabilizer $\Stab_{\gent}(\delta)$ have the same image in $\Orth(T_\Co)$.* Needed only if the statement is read with the root fixed up to sign, which is how the stabilizer of a root class is usually written; with $\delta$ fixed as a vector, as in (2) and (3), it is not needed. Status: page proof --- the proof of @lem:coble-monodromy-in-stabilizer: if $\rho(\gamma)\delta = -\delta$ then $s_\delta\rho(\gamma)$ fixes $\delta$, and $s_\delta$ acts as the identity on $\delta^{\perp T_\En}$.
10. *$w^{\perp} = [h/2]^{\perp}$ is of plus type, and $[h/2]$ generates a direct summand of $A_{T_\Co}$.* Needed in Step 6, both for the count of the $527$ classes and for reading $\Orth(q_{T_\Co})\to\Orth(w^{\perp},q)$ as an isomorphism. Status: proved --- Step 1 and @lem:coble-discriminant-blocks(2), (3).
11. *The gluing identification $\kappa\colon A_{E_{10}(2)}\isoto A_{T_\En}$ is defined and is an isometry, it carries the two summands of $A_{E_{10}(2)}$ to those of $A_{T_\En}$, and $\varphi\oplus\id$ acts on $A_{T_\En}$ by $\bar\rho(\varphi)$.* Needed in Steps 2, 4, 5 and 6: it is what makes "$A_{E_{10}(2)}$" and "$A_{T_\En}$" the same object, hence what turns the vanishing of the discriminant action of $g$ into a condition on $\bar\rho(\varphi)$, and what transfers Sterk's group $M$ and its index to $P$. Status: proved --- @lem:gluing-discriminant-identification(1)--(4), which proves the bijectivity, the isometry, the two summands and the action formula from the gluing datum of @def:gamma-co-groups.

*The statements that the issue names.* The issue names four of Nikulin's; the proof uses three of them, and the fourth is read and recorded below as not needed. A fifth, Proposition 1.5.1, is the gluing theorem that Step 0 rests on. Proposition 1.5.1 is on the page as @thm:nikulin-gluing; Corollary 1.5.2 is the automorphism-lifting criterion used in Steps 2 and 5 and in @lem:gluing-discriminant-identification(4), on the page as @thm:automorphism-lifting-criterion; Theorem 3.6.2 is item 1 (the isometry class of an even $2$-elementary lattice by its invariants); Theorem 3.6.3 is item 5. The fourth of the issue's, **Theorem 1.14.4** of [@Nik80, §1.14], is **not used** by the proof, and it is recorded here so that its absence is a statement and not an omission. It is the analogue of Witt's theorem: for an even lattice $M$ of signature $(t_{(+)},t_{(-)})$ and an even unimodular lattice $L$ of signature $(l_{(+)},l_{(-)})$, there is a *unique* primitive embedding $M\into L$ provided (1) $l_{(+)}-t_{(+)}>0$ and $l_{(-)}-t_{(-)}>0$, (2) $l_{(+)}-t_{(+)} + l_{(-)}-t_{(-)}\geq 2 + \ell(A_{M_p})$ for every $p\neq2$, and (3) if that difference equals $\ell(A_{M_2})$ then $q_M\cong u_+^{(2)}(2)\oplus q'$ or $q_M\cong v_+^{(2)}(2)\oplus q'$. [@AEGS25, Lemma 2.4], on the page as @lem:enriques-embedding-chain, invokes it for the uniqueness of the embedding $U(2)\oplus E_8(2)\into L$ of the Enriques theory, into the even unimodular lattice $(3,19)$: the three conditions hold there, $(1)$ as $3-1 = 2>0$ and $19-9 = 10>0$, $(2)$ as $12\geq 2+0$ for odd $p$, and $(3)$ is vacuous because $12\neq\ell(A_{M_2}) = 10$. The uniqueness that @prop:gamma-co-images(2) asserts is *not* an instance of it and does not need it: there the embedding $\eta$ is given, and uniqueness is injectivity of the restriction $\Stab_{\Orth(T_\En)}(\delta)\to\Orth(T_\Co)$ (item 8), while existence is Corollary 1.5.2. An embedding-uniqueness theorem about $M\into L$ with $L$ unimodular says nothing about which isometries of a fixed $\delta^{\perp}$ lift, which is what the proposition is about.

Two consequences are worth separating from the proposition. First, (2) is stronger than an existence statement for extensions: the extension of $\varphi\in\Orth(T_\Co)$ is not merely some isometry of $T_\En$ fixing a chosen root whose orthogonal complement is $T_\Co$, it is $\varphi\oplus\id_{\generators{\delta}}$, so the extension is a homomorphism and $\Stab_{\Orth(T_\En)}(\delta)$ is its graph. Second, the number in (3) is a lattice index: it says nothing about the degree of $\bD(T_\Co)/\Gamma_{\Co,2}\to\bD(T_\Co)/\Orth(T_\Co)$, which is a statement about the monodromy group and is open: @qst:coble-monodromy-equality, which would have named the group, is false (@prop:coble-monodromy-equality-false).
:::

::: {.lemma #lem:coble-family-identification title="The family identification (F) from the universal family over the Heegner divisor"}

In the situation of @lem:coble-monodromy-in-stabilizer, assume

(U) the degree-$2$ Coble family over $\Delta$ and its marking are defined: the family is the restriction to $\Delta$ of the universal family (@def:classifying-object) of K3 surfaces with the Enriques involution over the moduli stack of degree-$2$ numerically polarized Enriques surfaces, whose coarse space is $F_{\En,2}$ [@AEGS25, introduction, and Defs. 2.5--2.7]; $\Gamma_{\Co,2}$ is its monodromy group on the local system with fibre $T_\Co$ (@def:gamma-co-groups); and on every fibre the covering involution has invariant lattice $S_\Co$, spanned by the classes of $E_0,\dots,E_{10}$ [@DK13, §3].

Then (F) holds: the local system with fibre $T_\Co$ is the $\delta^{\perp}$-part of the restriction to $\Delta$ of the local system with fibre $T_\En$.

:::

::: {.proof}

*The ambient family.* [@AEGS25] constructs it: "Consider the universal family $(X,\epsilon R)\to F(2,2,0)$ of KSBA-stable pairs (@def:ksba-compactification) over the compactified moduli stack. ... the pullback of the universal family $(X_B,\epsilon R_B)\to B$ is a family whose general fiber is a pair $(X,\epsilon R)$ of an Enriques K3 surface ... Taking the quotient gives a family $(Z,\epsilon R_Z)\to B$ over a compact base, extending the universal family of Enriques surfaces ... By Lemma 2.8, the normalization $B^\nu$ of $B$ is a compactification of $F_{\En,2}$ admitting a universal family of pairs. So we have a classifying morphism $B^\nu\to F_{\En,2}$." Over the preimage of $\Delta$ the K3 fibres are nodal, and their quotients are the Coble surfaces [@AEGS25, the paragraph after Def. 2.7]. That is the family of the lemma at the level of the finite cover $B^\nu$; read on the moduli stack, of which $F_{\En,2}$ is the coarse space, it is the universal family, and $\Gamma_{\Co,2}$ is the monodromy of that family.

*The fibre marking.* On a fibre the covering involution has invariant lattice $M_X = S_\Co$, spanned by the classes of $E_0,\dots,E_{10}$, and anti-invariant lattice $N_X = T_\Co$ [@DK13, (3.6); @prop:coble-cover-marking].

*The covering involution is the reflection twist.* With that marking the involution acts on $H^2(X_b)\cong\lkt$ as $I_\Co = -\theta_\Co$ [@prop:coble-cover-marking]. The reflection twist $w_\alpha I_\En$ of @cons:reflection-twist has the same two eigenspaces, $S_\En\oplus\Z\alpha = S_\Co$ and $\alpha^{\perp T_\En} = T_\Co$ [@prop:coble-eigenspaces, @prop:coble-transcendental]. Two involutions of $L_{K3}$ with the same $(\pm1)$-eigenspaces coincide, so the covering involution is $w_\alpha I_\En$ on every fibre, and, the classes $e_0,\dots,e_{10}$ being canonical sections, as a family.

*Conclusion.* The local system with fibre $T_\Co$ of the Coble family is the anti-invariant local system $L_{K3}^{I_\Co=-1}$ of that involution, whose fibre is $\alpha^{\perp T_\En} = \delta^{\perp T_\En}$ [@prop:coble-eigenspaces]. That is (F).
:::

::: {.remark #rmk:coble-family-identification-status title="Where the two halves of the identification come from"}
The ambient family is [@AEGS25], at the level recorded in @rmk:coble-universal-family-level; the fibre marking is [@DK13, §3] and @prop:coble-cover-marking. The degree-$2$ Coble family as a moduli functor is @def:coble-family-degree-two. The one thing neither paper writes as a single statement is the pair for $\Delta$: [@AEGS25] identifies the *points* of $\Delta$ with the Coble quotients and [@DK13] describes the covers fibre by fibre. The rank of the period lattice, $11$ [@DK13, (3.6)], is the rank of the classical family, which is what makes the identification the right one. The identification of the points of $\Delta$ with the Coble quotients is [@AEGS25]; (F), the family-level statement used by @lem:coble-monodromy-in-stabilizer, is @lem:coble-family-identification under its hypothesis (U).

Hypothesis (U) of @lem:coble-family-identification has three parts, and the book supplies two of them. The degree-$2$ Coble family and its local system with fibre $T_\Co$ are @def:coble-family-degree-two, with $\Gamma_{\Co,2}$ its monodromy group (@def:gamma-co-groups(5)); on every fibre the covering involution has invariant lattice $S_\Co$, spanned by $e_0,\dots,e_{10}$ (@prop:coble-cover-marking). The third part asks for a comparison of stacks, and two statements are involved. (i) The monodromy containment $\Gamma_{\Co,2}\subseteq R_{\gent}\cap\Orth^+(T_\Co)$ needs no such comparison. On the K3 covers of an object of @def:coble-family-degree-two, $\alpha = f^*(-K_S)$ and $\tilde h$ are global sections, so the monodromy preserves $S_\En = \alpha^{\perp S_\Co}$ and its orthogonal complement, a local system with fibre $T_\En$ that contains $\delta = \alpha$ with $\delta^{\perp T_\En} = T_\Co$ (@prop:coble-eigenspaces). The monodromy therefore fixes $\delta$. Membership in $\gent$ is not yet proved: it requires that an isometry of $S_\En$ fixing $\tilde h$ induce on $A_{T_\En}$ an element of $\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ (@prop:sterk-group-identification(2)). This statement is over $\CC$, since it concerns a topological local system. (ii) The identification of the stack of @def:coble-family-degree-two with the restriction to $\Delta$ of the stack of [@AEGS25] is a different statement. The period-domain identification $\bD(\delta^{\perp}) = \bD(T_\Co)$ (@thm:coble-heegner-line-unique) identifies points, so it gives at most a statement about coarse spaces, and over $\CC$ that statement is birational (@prop:coble-moduli-heegner-divisor). A statement about stacks needs both stacks to be equivalent to an orbifold quotient $[\bD(T_\Co)/\Gamma]$ for an explicit $\Gamma$. For $\Gamma = R_{\gent}$ this fails on the Coble side (@lem:d2b-forgets-to-d2a(3)). Over $\operatorname{Spec}\ZZ[1/N]$ there are no periods, and the comparison must go through the moduli functors. The statements to prove are in research#787.
:::

::: {.remark #rmk:coble-universal-family-level title="At which level the universal family over $F_{\En,2}$ exists"}
[@AEGS25, introduction] announces "a description of $F_{\En,2}$ and its universal family", and the body states the level at which the family is constructed: "Consider the universal family $(X,\epsilon R)\to F(2,2,0)$ of KSBA-stable pairs over the compactified moduli stack. ... By Lemma 2.8, the normalization $B^\nu$ of $B$ is a compactification of $F_{\En,2}$ admitting a universal family of pairs. So we have a classifying morphism $B^\nu\to F_{\En,2}$" [@AEGS25]. The same paper says that $F_{\En,2}$ itself is coarse: "the complement of the discriminant divisor in $F_{\En,2}=D(T_\En)/\Gamma_{\En,2}$ is the coarse moduli space of Enriques surfaces with a numerical polarization of degree 2" [@AEGS25].

So the universal family exists over the moduli stack, of which $F_{\En,2}$ is the coarse space, and over the finite cover $B^\nu$; it is not a family over $F_{\En,2}$ as a scheme, and what the paper gives over $F_{\En,2}$ is the classifying morphism $B^\nu\to F_{\En,2}$. The family of @lem:coble-family-identification is therefore the restriction of the universal family at the level of the stack, equivalently of the finite cover $B^\nu$; it is not a family over the coarse space $F_{\En,2}$, and $\Gamma_{\Co,2}$ is the monodromy of the family at that level (@def:gamma-co-groups).
:::

::: {.lemma #lem:coble-monodromy-in-stabilizer title="The monodromy of the degree-$2$ Coble family lies in the stabilizer of $\delta$"}

Let $\Delta\subset F_{\En,2} = \bD(T_\En)/\gent$ be the discriminant divisor, the image of $\alpha^{\perp}\subset\bD(T_\En)$ [@AEGS25, Def. 2.7 and the paragraph after it], whose points parameterize quotients of nodal K3 surfaces (@def:nodal-k3-surface) by an involution fixing a node, these quotients being rational Coble surfaces with a $(1,1)/4$-singularity. Let $\delta$ be the $(-2)$-vector of [@DK13, the sentence after Prop. 3.2] --- a representative of the class $\alpha$ of [@AEGS25] --- and let $T_\Co = N_X = M_X^{\perp}$ be the transcendental lattice of the K3 double cover $X$ of a Coble surface [@DK13, (3.6)], which is $\delta^{\perp T_\En}$. Let $\Gamma_{\Co,2}$ be the monodromy group of @def:gamma-co-groups(5) for the K3 covers over $\Delta$, and assume

(F) the local system with fibre $T_\Co$ of that family is the $\delta^{\perp}$-part of the restriction to $\Delta$ of the local system with fibre $T_\En$.

Under (F),
$$\Gamma_{\Co,2}\subseteq R_{\gent}.$$
:::

::: {.proof}

*The periods lie in $\delta^{\perp}$ and fill it.* For a fibre $X_b$ of the family over $\Delta$ the period $[\omega_b]$ lies in $\bD(T_\Co)$, because $T_\Co = M_X^{\perp}$ is the transcendental lattice of $X_b$ [@DK13, (3.6)]. Since $T_\Co = \delta^{\perp T_\En}$ [@DK13, the sentence after Prop. 3.2], one has $[\omega_b]\in\bD(\delta^{\perp})\subset\bD(T_\En)$. The image of the marked period map is the preimage of $\Delta$, and $\Delta$ is by definition the image of $\alpha^{\perp}$ in $\bD(T_\En)/\Gamma_\En$ [@AEGS25, Def. 2.7]; that preimage is a union of components of $\bD(\delta^{\perp})$, hence open in it. This is where the definition of $\Delta$ as a period divisor is used, and no Torelli theorem is invoked.

*The monodromy preserves the line $\ZZ\delta$.* Transport is an isometry of $T_\En$, and the period map is equivariant, $\Phi(\gamma\tilde b) = \rho(\gamma)\Phi(\tilde b)$ (@eq-period-map-equivariance), so $\rho(\gamma)$ carries the image $\Phi(\widetilde\Delta)$ of the period map to itself. Its image is open in $\bD(T_\Co)$ by the previous paragraph. For an isometry $g$ one has $g\,\bD(\delta^{\perp}) = \bD((g\delta)^{\perp})$; the two closed analytic hypersurfaces $\bD(\delta^{\perp})$ and $\bD((\rho(\gamma)\delta)^{\perp})$ of $\bD(T_\En)$ meet in the nonempty open subset $\Phi(\widetilde\Delta)$, hence coincide, so $(\rho(\gamma)\delta)^{\perp} = \delta^{\perp}$ and $\rho(\gamma)\delta = \pm\delta$.

*The image lies in $R_{\gent}$.* Hence $\rho(\gamma)$ lies in the line stabilizer (@def:group-orbit) $\Stab_{\gent}(\ZZ\delta)$, and its restriction to $\delta^{\perp} = T_\Co$ is the image of an element of that stabilizer. The line stabilizer and the vector stabilizer have the same image in $\Orth(T_\Co)$: if $\rho(\gamma)\delta = -\delta$ then $s_\delta\rho(\gamma)$ fixes $\delta$, and $s_\delta$ acts as the identity on $\delta^{\perp}$; and $s_\delta\in\ker\rho_{T_\En}\subseteq\gent$, because $\delta$ lies in the unimodular summand $U$ of $T_\En$ and $s_\delta$ therefore acts trivially on $A_{T_\En}$. So the image of $\Stab_{\gent}(\ZZ\delta)$ is the image of $\Stab_{\gent}(\delta)$, which is $R_{\gent}$ (@def:gamma-co-groups, @prop:gamma-co-images(3)).
:::

::: {.theorem #thm:coble-monodromy-versus-enriques title="The monodromy of the degree-$2$ Coble family against the Enriques stabilizer"}

Let $\Gamma_{\Co,2}$ be the monodromy group of @def:gamma-co-groups(5), and let
$$
R\definedas R_{\gent} = \bar\rho^{-1}(P)\leq\Orth(T_\Co)
$$
be the image of $\Stab_{\gent}(\delta)$ in $\Orth(T_\Co)$, with $P$ the stabilizer (@def:group-orbit) of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ (@prop:gamma-co-images(3)). Let $\zeta\in T_\Co$ be a primitive vector of square $2$ and $s_\zeta$ its reflection (@prop:gamma-co-reflective-set).

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

Is $\Gamma_{\Co,2} = R_{\gent}\intersect\Orth^+(T_\Co)$? The inclusion $\Gamma_{\Co,2}\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$ is @thm:coble-monodromy-versus-enriques(4), from @lem:coble-monodromy-in-stabilizer, conditional on (U) of @lem:coble-family-identification; (U) and (F) are D2 of research#786. The reverse inclusion is the assertion that every congruence isometry of $T_\Co$ in $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ is realised by monodromy; by @lem:coble-monodromy-reverse-reduction it is equivalent to $\bar\rho(\Gamma_{\Co,2}) = P$ and $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$. It holds for the degree-$2$ Coble data of the direct construction, where it is @prob:B25, whose proof rests on the period computation of @prob:B24 and not on a printed theorem; no printed statement supplies it for the degree-$2$ Coble family of @lem:coble-monodromy-in-stabilizer, and it is the degree-$2$ analogue of the reverse inclusion of @conj:gamma-co-stable. The equality $R_{\gent} = \Gamma_{\Co,2}$ of research#779 is false either way (@thm:coble-monodromy-versus-enriques(3)). The equality asked here is false as well, and not merely unproved: @prop:coble-monodromy-equality-false proves $\Gamma_{\Co,2}\neq R_{\gent}\intersect\Orth^+(T_\Co)$ from the index of $\Gamma_{10A_1}$, so the reverse inclusion fails and no orbit count of $R_{\gent}$ is a count for $F_{\Co,2}$ by this route.
:::

::: {.proposition #prop:coble-monodromy-equality-false title="The monodromy of the degree-$2$ family is not the restricted stabilizer: the question is answered in the negative"}

Let $P\leq\Orth(q_{T_\Co})$ and $R_{\gent}=\bar\rho^{-1}(P)$ be as in @prop:gamma-co-images(3), let $\Theta\cong\mathfrak S_{10}$ and $\Gamma_{10A_1}=\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)$ be as in @thm:gamma-co-sextic-group(1)--(2), and let $\Gamma_{\Co,2}$ be the monodromy group of @def:gamma-co-groups(5). Then

1. $\Gamma_{\Co,2}\subseteq\Gamma_{10A_1}$, and no hypothesis on (U) of @lem:coble-family-identification is used for this.
2. The group $R_{\gent}\intersect\Orth^+(T_\Co)$ is **not** contained in $\Gamma_{10A_1}$: the two indices in $\Orth^+(T_\Co)$ are
$$
[\Orth^+(T_\Co):R_{\gent}\intersect\Orth^+(T_\Co)]=2^7\cdot17\cdot31=67\,456,
\qquad
[\Orth^+(T_\Co):\Gamma_{10A_1}]=2^{13}\cdot3\cdot17\cdot31=12\,951\,552 .
$$
3. Hence $\Gamma_{\Co,2}\neq R_{\gent}\intersect\Orth^+(T_\Co)$: the equality of @qst:coble-monodromy-equality is false, and it is the reverse inclusion that fails. No count of orbits of $R_{\gent}$ is a count for $F_{\Co,2}$ by that route.
4. Under (U) of @lem:coble-family-identification, so that $\Gamma_{\Co,2}\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(4)),
$$
[R_{\gent}\intersect\Orth^+(T_\Co):\Gamma_{\Co,2}]\ \geq\ \abs{P}/\abs{\Theta}\ =\ 192,
\qquad
[R_{\gent}:\Gamma_{\Co,2}]\ \geq\ 384,
$$
with equality in the first display exactly when $\Theta\subseteq P$ and $\Gamma_{\Co,2}=\Orth^+(T_\Co)\intersect\bar\rho^{-1}(P\intersect\Theta)$.
:::

::: {.proof}

1. This is @prop:d2b-index-exact(3): a family of degree-$2$ polarized Coble surfaces forgets to an unpolarized family (@lem:d2b-forgets-to-d2a(1)), and the underlying family is the pullback of the universal one along a morphism to $\bar B$ (@lem:d2b-forgets-to-d2a(2)), so $\Gamma_{\Co,2}\subseteq\Gamma_\Co(\bar B)$; and $\Gamma_\Co(\bar B)\subseteq\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)=\Gamma_{10A_1}$, the two halves being @lem:monodromy-is-spinor-positive and @prop:gamma-co-geometric-bound(2). Neither step uses (U).

2. The preimage in $\Orth^+(T_\Co)$ of $P$ is $R_{\gent}\intersect\Orth^+(T_\Co)$, and $\bar\rho$ carries $\Orth^+(T_\Co)$ onto $\Orth(q_{T_\Co})$ (the argument of @prop:d2b-index-exact(1)), so its index is $[\Orth(q_{T_\Co}):P]=2^7\cdot17\cdot31$, the number of @prop:gamma-co-images(3). The second index is @thm:gamma-co-sextic-group(3). For subgroups of a group of finite index, $A\subseteq B$ forces $[G:B]\leq[G:A]$; since $12\,951\,552>67\,456$, the group $R_{\gent}\intersect\Orth^+(T_\Co)$ is not contained in $\Gamma_{10A_1}$.

3. If the equality held, then $R_{\gent}\intersect\Orth^+(T_\Co)=\Gamma_{\Co,2}\subseteq\Gamma_{10A_1}$ by 1, against 2.

4. By (U) and @thm:coble-monodromy-versus-enriques(4), $\Gamma_{\Co,2}\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$, and by 1 it also lies in $\Gamma_{10A_1}$; hence
$$
\Gamma_{\Co,2}\subseteq\Orth^+(T_\Co)\intersect\bar\rho^{-1}(P\intersect\Theta).
$$
Both groups are preimages in $\Orth^+(T_\Co)$ of subgroups of $\Orth(q_{T_\Co})$, so the index of the right-hand one in $R_{\gent}\intersect\Orth^+(T_\Co)$ is $[P:P\intersect\Theta]=\abs{P\Theta}/\abs{\Theta}\geq\abs{P}/\abs{\Theta}=696\,729\,600/3\,628\,800=192$, and $[R_{\gent}:\Gamma_{\Co,2}]=2\,[R_{\gent}\intersect\Orth^+(T_\Co):\Gamma_{\Co,2}]$ is twice that by @thm:coble-monodromy-versus-enriques(2). The first display is an equality exactly when $\abs{P\Theta}=\abs{P}$, that is $\Theta\subseteq P$, and $\Gamma_{\Co,2}$ is the intermediate group displayed. The four numbers are computed from the two orders in `computations/reports/coble_797-index-of-gamma-co-2.py`, recorded in the `-run.txt` beside it.
:::

::: {.remark #rmk:two-groups-named-gamma-co-2 title="Two groups carry the name $\Gamma_{\Co,2}$, and the equality holds for only one of them"}

@prop:coble-monodromy-equality-false is a statement about the group of @def:gamma-co-groups(5): the monodromy of the local system of lattices with fibre $T_\Co$ of the family of Coble surfaces carrying a degree-$2$ numerical polarization. A second group carries the same name up to a superscript and is not that group: $\Gamma^{\mathrm{geom}}_{\Co,2}$ of @def:geometric-monodromy, the image of the orbifold monodromy representation of the connected *direct* moduli stack of polarized Coble data. For the second, @thm:sign-is-isotropy proves $\Gamma^{\mathrm{geom}}_{\Co,2}=\Gamma^{\mathrm{dir}}_{\Co,2}$, and @prop:direct-eq-heegner identifies $\Gamma^{\mathrm{dir}}_{\Co,2}$ with $R_{\gent}\intersect\Orth^+(T_\Co)$; @cor:g3-g4-decided(1) records the consequence $G_1=G_2=G_3$.

The two cannot be the same group on the present page. $\Gamma_{\Co,2}\subseteq\Gamma_\Co(\bar B)\subseteq\Gamma_{10A_1}$ (@prop:d2b-index-exact(3)), whereas $R_{\gent}\intersect\Orth^+(T_\Co)$ is not contained in $\Gamma_{10A_1}$ (@prop:coble-monodromy-equality-false(2)), and $|P|=192\cdot10!$ is the factor between them. So a statement that identifies the orbifold monodromy group of the direct stack with $R_{\gent}\intersect\Orth^+(T_\Co)$ is a statement about $\Gamma^{\mathrm{geom}}_{\Co,2}$, and it is false of $\Gamma_{\Co,2}$ as defined in @def:gamma-co-groups(5). That is the reading to give the last sentence of @thm:coble-monodromy-versus-enriques(4) and clause (1) of @cor:g3-g4-decided: each is true of the direct group and is not a statement about the degree-$2$ family of @def:coble-family-degree-two. No page proves that the two definitions agree, and until one does, a count, an index or an equality must name which of the two it means. This is a flag and not a repair: the lines belong to research#760 and research#720, and nothing here decides which group those pages intend.
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

The cusp counts are unchanged. Since $\ker\bar\rho\subseteq R_{\gent}$, @thm:cusp-lifting(4) applies with $\Gamma = R_{\gent}$: parts 1--3 of that theorem hold with $\Gamma\intersect\Orth^+(T_\Co)$ in place of $\Gamma$, and the finite images $H$ and $H^+$ agree because the hypothesis $\ker\rho\subseteq\Gamma$ of its last sentence is met. Hence $R_{\gent}$ and $R_{\gent}\intersect\Orth^+(T_\Co)$ have the same orbits on the primitive isotropic vectors, on the primitive isotropic planes and on the flags. Two witnesses of the kind that proof uses lie in $\ker\bar\rho$ and outside $\Orth^+(T_\Co)$: the reflection $s_\zeta$ in the square-$2$ vector $\zeta$ fixes the primitive isotropic vector $e'$ of the $U(2)$ summand, and $\tau\definedas\id_{\generators{h}}\oplus(-\id_{U(2)})\oplus\id_{E_8(2)}$ fixes the primitive isotropic plane $\generators{e',\,2h+y}$ for $y = \alpha+\beta$ with $\alpha,\beta$ orthogonal roots of $E_8(2)$; both are integral involutions acting trivially on $A_{T_\Co}$, and $\spinornorm_\bR(\tau) = [(-1)^1] = [-1]$ by @lem:minus-identity-spinor-norm, $\tau$ being $-\id$ on the rank-two summand $U(2)$ of positive index one (@prop:gamma-co-reflective-set(2) for $s_\zeta$); `computations/reports/coble_779-monodromy-vs-enriques-run.txt` checks the two isometries, the plane and the triviality of both actions on $A_{T_\Co}$. Hence the four $0$-cusps of @prop:coble-cong-point-stabilizer(3) and the seven $1$-cusps of @thm:plane-fibre(3) are counts for $R_{\gent}\intersect\Orth^+(T_\Co)$ as well as for $R_{\gent}$, and they are not counts for $F_{\Co,2}$: that would need @qst:coble-monodromy-equality, and the equality is false (@prop:coble-monodromy-equality-false).
:::

::: {.remark #rmk:gamma-co-counts title="The cusp counts name their group"}
The quotient $F^{\mathrm{un}}_\Co = \bD(T_\Co)/\Orth(T_\Co)$ has one $0$-cusp, $\Orth^+(T_\Co)$ being transitive on the primitive isotropic vectors (@thm:unpolarized-cusps), computed by the $\Orth(T_\Co)$ rows of run 43556671111 (@rmk:coble-plane-incidence-rows), and one $1$-cusp, by @thm:plane-transitivity-tco, certified by the same rows. The stable quotient $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ has $527$ $0$-cusps (@thm:coble-zero-cusp-count(2)) and $189\,720$ $1$-cusps, one fibre of eight over each of the $23\,715$ liftable classes (@thm:plane-fibre(3)). The subgroup $R_{\gent} = \bar\rho^{-1}(P)$ has four orbits of primitive isotropic vectors (@thm:four-r-orbits, one over each of Sterk's cusps $2,3,4,5$ by @thm:orbit-per-cusp), hence $D(T_\Co)/R_{\gent}$ has four $0$-cusps (@thm:cusp-fibres-four), and of primitive isotropic planes it has $7$, none over the four $1$-cusp types containing $1$ and distributed over the five others as @thm:one-cusp-multiplicities gives: one over $\{2,4,5\}$, one over $\{4,5\}$, two over $\{3,5\}$, one over $\{3,4\}$ and two over $\{5,5\}$; the incidence is $0_k\rightsquigarrow T$ exactly when $k\in T$, with degrees $1,3,3,6$ at $0_2,0_3,0_4,0_5$ and $13$ edges (@thm:cusp-diagram-tco); these are counts for $R_{\gent}$, and not for $\Gamma_{\Co,2}$ (@prop:coble-monodromy-equality-false). It also has seven orbits of primitive isotropic planes, proved by the integral decorated-plane lifting and finite $G_\Co$-orbit calculation of @cor:coble-heegner-integral-plane-descent and independently reproduced by that run's row (@thm:plane-fibre(3), @rmk:coble-plane-incidence-rows); by @rmk:coble-monodromy-counts the same orbits are those of $R_{\gent}\intersect\Orth^+(T_\Co)$, so $\bD(T_\Co)/(R_{\gent}\intersect\Orth^+(T_\Co))$ has four $0$-cusps and seven $1$-cusps, and $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$ does not have these counts (@prop:coble-monodromy-equality-false); the subgroup-orbit operation, which would count these for a prescribed subgroup rather than for $\Orth(T_\Co)$, is sage-extensions#286, and no count on this page is read off it. Each of these counts is a count of lattice orbits and not only of finite ones: every group named in this paragraph contains $\widetilde\Orth^+(T_\Co)$, so by @thm:coble-integral-lifting-fibre(1), (2) the fibre over one finite datum is a single orbit and contributes one.

The cusp counts of $\fco$ are the counts for the stable subgroup: $\fco=\bD(T_\Co)/\Gamma_\Co$ has the coarse space of $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable), hence $527$ $0$-cusps (@thm:coble-zero-cusp-count(2)) and $189\,720$ $1$-cusps (@thm:plane-fibre(3)). The one $0$-cusp and one $1$-cusp of $F^{\mathrm{un}}_\Co=\bD(T_\Co)/\Orth(T_\Co)$ are the counts of the tautological local system over the coarse space (@thm:gamma-co-is-full), which is not $\Gamma_\Co$, and those of the unlabelled base are the counts for $\Gamma_{10A_1}$, which are not computed on this page.

[@DK13, Prop. 3.2] gives the moduli space as an open subset of the quotient by $\Orth(N)$, and the sentence after it states that the quotient of the $(-2)$-Heegner divisor by $\Orth(U\oplus E(2))$ is birational to that moduli space. By @thm:normalization for $\Gamma = \Gamma^K_\En$ the normalization of that second quotient is $\bD(T_\Co)/R_{\Gamma^K_\En}$, and $R_{\Gamma^K_\En} = \Orth(T_\Co)$ by @prop:gamma-co-images(2), in agreement with the first.
:::

::: {.theorem #thm:normalization}

Let $\Gamma$ be one of $\Gamma_\En = \widetilde\Orth^+(T_\En)$, $\Gamma^K_\En = \Orth(T_\En)$, $\gent$, and let $R_\Gamma$ be the restricted stabilizer (@def:group-orbit) of @def:gamma-co-groups, identified in @prop:gamma-co-images. Write $F^{\Gamma}_\Co\definedas\bD(T_\Co)/R_\Gamma$. Then the map induced by the embedding $\eta$ of @lem:primitive_embedding_eta,
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
A proper primitive sublattice $S\subsetneq T_\Co$ of signature $(2,\ast)$ cuts out a proper closed analytic subset (@def:closed-analytic-subset) $\bD(S)\subsetneq\bD(T_\Co)$, and there are countably many such $S$.
So the set of $x\in\bD(T_\Co)$ with $T(x) = T_\Co$ is the complement of countably many proper closed analytic subsets, hence dense.
For such an $x$ the fibre computation allows only $M' = T_\Co$: one has $T_\Co = T(x)\iscontainedin M'$ with both primitive of rank $11$.
The fibre through $x$ is therefore a single point.
The locus where a finite morphism of irreducible varieties has more than its generic number of preimages is a proper closed subset (@def:closed-subset), and a dense set is not contained in one, so $f^{\Gamma}$ has degree (@def:graded-object) $1$ and is birational.

Finally $F^{\Gamma}_\Co$ is normal, being the quotient of a bounded symmetric domain by a properly discontinuous group of automorphisms.
A finite birational morphism from a normal variety onto a reduced irreducible variety is its normalization, so $F^{\Gamma}_\Co$ is the normalization of $Z$.
:::

::: {.remark #rmk:normalization-enriques-analogue title="The Enriques case"}

For Enriques surfaces, $\fentwo$ is the normalization of a closed subvariety of $\fttz$ [@AEGS25 Lem. 2.8].
:::

::: {.proposition #prop:sterk-group-identification title="The discriminant image of $\gent$"}

Let $\rho\colon\Orth(\ten)\to\Orth(A_{\ten}, q_{\ten})$ be the discriminant representation (@def:discriminant-rep) and $K = \ker\rho$.
Identify $\ten = U\oplus U(2)\oplus E_8(2)$ with the lattice $L_- = \mathbf H\oplus\mathbf H(2)\oplus E_8(-2)$ of [@Ste91, 1.3] summand by summand, and let $e', f'$ be the isotropic (@def:orthogonal-complement) basis (@def:based-module) of $U(2)$, with $(e', f') = 2$.

1. $\gent$ is the group (@def:group) $\Gamma$ of [@Ste91, §2, Prop. 2.7], and $\gent = \theset{g\in\Orth(\ten) \st \rho(g)\text{ preserves the summands } A_{U(2)} \text{ and } A_{E_8(2)} \text{ of } A_{\ten}}$.
2. $\rho(\gent) = M\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$, and $\gent = \rho^{-1}(M)$; in particular $K\subseteq\gent$.
3. $\gent$ is a proper subgroup of $\Stab_{\Orth(\ten)}\bigl([(e'+f')/2]\bigr)$.
:::

::: {.proof}

(1) The group $\Gamma$ of [@Ste91, Prop. 2.7] is the image in $\Orth(L_-)$ of the isometries of the K3 lattice that commute with the Enriques involution (@def:enriques-surface) and fix the polarization vector (@def:polarization-vector), and $\gent$ is the image in $\Orth(\ten)$ of the same group [@AEGS25 Def. 2.6].
The description by the two summands is [@Ste91, Prop. 2.7].

(2) Because $U$ is unimodular, $A_{\ten} = A_{U(2)}\perp A_{E_8(2)}$, and an isometry of $q_{\ten}$ preserves both summands exactly when it is a pair of isometries of the summands.
So (1) says $\gent = \rho^{-1}(M)$.
The lattice $\ten$ is even (@def:form-axioms), indefinite (@def:definiteness) and $2$-elementary, so $\rho$ is surjective (@thm:two-elementary-surjectivity), and $\rho(\gent) = M$.

(3) The three nonzero classes of $A_{U(2)}$ are $[e'/2]$, $[f'/2]$ and $[(e'+f')/2]$, with $q$-values $0$, $0$ and $(e'+f')^2/4 = 1$.
So every element of $\Orth(q_{U(2)})$ fixes $[(e'+f')/2]$, and $\gent$ stabilizes it by (2).
Since $f'\in\ten$, the classes $[(e'+f')/2]$ and $[(e'-f')/2]$ are equal.
The isometry $\psi\in\Orth(L_-)$ of [@Ste91, Rem. 2.8] stabilizes $\tfrac12(e'-f')+L_-$ and is not in $\Gamma$.
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
This is the index computed in [@Ste91, Rem. 2.12].
:::

::: {.proposition #prop:ten-plane-classes title="The two classes of primitive isotropic planes of $\ten$"}

Write $e,f$ for the isotropic basis (@def:isotropic-basis-hyperbolic-plane) (@def:based-module) of $U$ and $e',f'$ for that of $U(2)$, with $(e,f) = 1$ and $(e',f') = 2$.
Identify the summand $E_8(2)$ with $E_8 = \theset{y_0\in\ZZ^8\cup(\ZZ^8+s) \st \textstyle\sum_i y_{0,i}\in2\ZZ}$, $s = \tfrac12(1,\dots,1)$ [@CS10, Ch. 4, §8.1], so that $y\leftrightarrow y_0$ and $(y,y') = -2\,y_0\cdot y_0'$.
Let $\alpha\in E_8(2)$ correspond to $2e_1$, and put $z\definedas 2e+2f+\alpha$.
For a primitive totally isotropic plane $\varPi\subseteq\ten$ let $D(\varPi)\leq A_{\ten}$ be the image of $\varPi_\QQ\cap\ten^*$, as in @not:isotropic-reduction-setup.

1. $\varPi_1 = \generators{e,e'}$ and $\varPi_2 = \generators{z,e'}$ are primitive totally isotropic planes.
   Every primitive totally isotropic plane $\varPi$ is $\Orth(\ten)$-equivalent to exactly one of them, and to $\varPi_1$ exactly when it contains a vector of divisibility (@def:lattice-divisibility) one.
2. If $\varPi$ contains a vector of divisibility one, then $D(\varPi)$ has order $2$, its nonzero element is $[v/2]$ for every primitive $v\in\varPi$ of divisibility two, and $\varPi^\perp/\varPi\cong E_8(2)$.
3. If $\varPi$ contains no vector of divisibility one, then $D(\varPi)$ has order $4$, its three nonzero elements are the classes $[p/2]$ of the primitive $p\in\varPi$, and $\varPi^\perp/\varPi\cong D_8^*(2)$, where $D_8^*$ carries the negative of the Euclidean form.
:::

::: {.proof}

(1) The vectors $e$, $e'$ and $z$ are isotropic and pairwise orthogonal: $(2e+2f)^2 = 8$ and $\alpha^2 = -2\cdot4 = -8$.
The vector $\alpha/2$ corresponds to $e_1\notin E_8$, so $z$ is primitive in $U\oplus E_8(2)$, and $e'$ is primitive in $U(2)$; a span of primitive vectors of two orthogonal summands is primitive in their sum, so $\varPi_2$ is primitive, and so is $\varPi_1$.
The vector $e$ has divisibility one.
For a primitive $az+be'\in\varPi_2$, the ideal $(az+be',\ten)$ contains $(az+be',f) = 2a$ and $(az+be',f') = 2b$, and it lies in $2\ZZ$ because $(z,\ten)$ and $(e',\ten)$ do; so $az+be'$ has divisibility two.
By [@Ste91, Prop. 4.6] there are exactly two $\Orth(\ten)$-classes of primitive isotropic planes, and divisibility is invariant under $\Orth(\ten)$, so $\varPi_1$ and $\varPi_2$ represent the two classes.

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

There is also a direct obstruction to a third, trivial-discriminant stratum, independent of the classification in (1). Reduce $N=U\perp U(2)\perp E_8(2)$ modulo $2N$. The alternating form induced by its integral pairing is supported entirely on $U/2U$, where it is nondegenerate of dimension two. For a primitive totally isotropic plane $\varPi$, primitivity gives an injection $\varPi/2\varPi\injects N/2N$. Its image is isotropic for the mod-two pairing, so its projection onto $U/2U$ has dimension at most one. Consequently a nonzero class of $\varPi/2\varPi$ has zero $U/2U$-projection. Choose a primitive lift $p\in\varPi$ of that nonzero parity class (any nonzero element of $\F_2^2$ lifts to a primitive vector of $\ZZ^2$). Its $U$-coordinates are even, while all pairings in the other two summands are even, so $(p,N)\subseteq2\ZZ$ and $p/2\in N^*$. The class $[p/2]\in A_N$ is nonzero: otherwise $p\in2N$, and primitivity of $\varPi$ would give $p\in2\varPi$, contrary to its nonzero parity class. In particular $D(\varPi)$ is **never trivial**: the zero-dimensional finite discriminant stratum cannot lift to a primitive isotropic plane. The other two strata are realized by $\varPi_1$ and $\varPi_2$, and all their finite subgroups are realized by the transitivity and surjectivity arguments of the cusp theorem (2).
:::

::: {.lemma #lem:half-vector-eichler title="Eichler transvections along a vector of divisibility two"}

Let $A = A_{\ten}$ with its discriminant quadratic form (@def:discquad) $q$ of @def:discriminant.
Then $q([x/2]) = x^2/4\bmod 2$, so $(A, q)$ is a quadratic space over $\F_2$, with polar form $\beta_q([x/2],[y/2]) = (x,y)/2\bmod 2$.
Let $d\in A$ be isotropic and nonzero, and for $c\in d^\perp$ define
$$
T_{d,c}(a)\definedas a+\beta_q(a,d)\,c+\bigl(\beta_q(a,c)+q(c)\,\beta_q(a,d)\bigr)\,d .
$$
Let $\eta\in\ten$ be a primitive isotropic vector (@def:isotropic-subspace) of divisibility (@def:lattice-divisibility) two with $[\eta/2] = d$.

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

For $g\in\Orth(\ten)$ one has $c(g\ZZ v) = \rho(g)\,c(\ZZ v)$, because $g$ preserves divisibility (@def:lattice-divisibility).
By [@Ste91, Prop. 4.5] there is $g\in\Orth(\ten)$ with $g\ZZ v_0 = \ZZ v$ for $v_0 = e$ or $v_0 = e'$.
Conjugation by $g$ carries $\Stab_{\Orth(\ten)}(\ZZ v_0)$ to $\Stab_{\Orth(\ten)}(\ZZ v)$, and conjugation by $\rho(g)$ carries the stabilizer (@def:group-orbit) of $c(\ZZ v_0)$ to the stabilizer of $c(\ZZ v)$.
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
The class $c(\ell)$ is $0$ exactly when $\operatorname{div}(\ell) = 1$, so $\ell$ and $\ell'$ have the same divisibility (@def:lattice-divisibility), and by [@Ste91, Prop. 4.5] there is $g\in\Orth(\ten)$ with $g\ell = \ell'$.
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

1. The primitive isotropic lines of $\ten$ form five $\gent$-orbits, the orbits (@def:group-orbit) of the vectors of [@Ste91, Prop. 4.2.3]:

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
3. Label a plane by the types of the primitive isotropic vectors (@def:isotropic-subspace) it contains, as in [@Ste91, §4.3.15].
   The labels of the nine orbits of item 2 are, in the order listed there, $\theset{1,2}$, $\theset{1,3}$, $\theset{1,4}$, $\theset{1,5}$ and $\theset{2,4,5}$, $\theset{4,5}$, $\theset{3,5}$, $\theset{3,4}$, $\theset{5,5}$.
   A plane orbit is incident to a line orbit of type $t$ exactly when $t$ occurs in its label.
   For a primitive isotropic $v$, the planes containing $v$ correspond to the isotropic lines of $v^\perp/\ZZ v$, and their $\Stab_{\gent}(v)$-orbits correspond to the parabolic subdiagrams (@def:elliptic-subdiagram) of rank $8$, modulo symmetry, of the Vinberg diagram of the reflection subgroup of the image of $\Stab_{\gent}(v)$ in $\Orth(v^\perp/\ZZ v)$ [@Ste91, §4.3.1--4.3.3].
   The subdiagram (@def:coxeter-subdiagram) of each plane orbit at a vector of each type in its label is:

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
4. For a plane $\varPi$ with label $\lambda$, the intersection of the image of $\Stab_{\gent}(\varPi)$ in $\GL(\varPi)$ with $\SL(\varPi)$ is $\Gamma^1(2)$ for $\lambda = \theset{1,t}$ [@Ste91, §4.3.16]; it is $\Gamma(2)$ for $\theset{2,4,5}$, $\Gamma^1(2)$ for $\theset{4,5}$, $\theset{3,5}$ and $\theset{3,4}$, and $\SL_2(\ZZ)$ for $\theset{5,5}$ [@Ste91, §4.3.17, and the proof of Prop. 4.7].
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

Let $L$ be a lattice for which $\Orth^+(L)$ of @def:lattice-spinor-kernels has index (@def:index) two in $\Orth(L)$, let $\Gamma\leq\Orth(L)$ satisfy $\Gamma\not\subseteq\Orth^+(L)$, put $\Gamma^+=\Gamma\intersect\Orth^+(L)$, and let $X$ be a $\Gamma$-set.
Then $\Gamma$ and $\Gamma^+$ have the same orbits (@def:group-orbit) on $X$ if and only if $\Stab_\Gamma(x)\not\subseteq\Orth^+(L)$ for every $x\in X$.
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

Let $N=\ten=U\oplus U(2)\oplus E_8(2)$ with signature $(2,10)$, let $\rho$ be its quadratic discriminant representation (@def:discriminant-rep) and $\widetilde\Orth(N)=\ker\rho$ its discriminant kernel (@def:mm-integral-spinor-data), and let $\Gamma\leq\Orth(N)$ be a subgroup with $\widetilde\Orth(N)\subseteq\Gamma$.
Every preimage $\rho^{-1}(M)$ with $M\leq\Orth(A_\ten,q_\ten)$ is of this form.
Put $\Gamma^+=\Gamma\intersect\Orth^+(N)$.
Then $\Gamma$ and $\Gamma^+$ have the same orbits (@def:group-orbit) on

1. the primitive isotropic lines of $N$;
2. the primitive isotropic planes of $N$;
3. the flags $\ell\subset P$ consisting of a primitive isotropic line contained in a primitive isotropic plane.

For the lines the same holds for primitive isotropic vectors (@def:isotropic-subspace): $-\id_N$ lies in $\ker\rho$ and in $\Orth^+(N)$, being level two because $A_\ten$ is annihilated by $2$ and spinor-positive by @lem:minus-identity-spinor-norm at positive index (@def:maximal-positive-definite-subspace) two, so $-\id_N\in\Gamma\intersect\Gamma^+$ and the two generators of a line lie in one orbit of both groups.
:::

::: {.proof}

*Notation.*
Write $e,f$ for the hyperbolic basis of the summand $U$, $e',f'$ for that of $U(2)$, and $r_1,r_2$ for two orthogonal roots of the summand $E_8(2)$ — the roots corresponding to $e_1-e_2$ and $e_1+e_2$ in the coordinates of @prop:ten-plane-classes, of square $-4$ — with $\alpha\definedas r_1+r_2$ and $z\definedas 2e+2f+\alpha$.
Put
$$
\tau\definedas\id_U\oplus(-\id_{U(2)})\oplus\id_{E_8(2)} ,
$$
the $\tau_0$ of @lem:enriques-level-two-transvections.
By @lem:enriques-level-two-transvections, $\alpha^2=-8$, $z$ is primitive isotropic of divisibility (@def:lattice-divisibility) two, and
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
The hypotheses of @lem:spinor-orbit-agreement are met: $\Orth^+(\ten)$ has index two in $\Orth(\ten)$, because $\spinornorm_\bR$ is a homomorphism from $\Orth(\ten)$ to $\{\pm1\}$ with kernel $\Orth^+(\ten)$ and it is onto, $\sigma_U$ being an integral isometry of $\ten$ with $\spinornorm_\bR(\sigma_U)=-1$; and at every primitive isotropic line and at every primitive isotropic plane the stabilizer (@def:group-orbit) inside $\Gamma$ meets $\Gamma\setminus\Orth^+(\ten)$.
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
Then $\Lambda\leq\Gamma(2)$, and for a primitive (@def:primitive-embedding) $(a,c)\in\bZ^2$:

1. there is $\lambda\in\Lambda$ with $\lambda(a,c)$ equal to $\pm(1,0)$ if $a$ is odd and $c$ even (@def:form-axioms), to $\pm(0,1)$ if $a$ is even and $c$ odd, and to $\pm(1,1)$ if $a$ and $c$ are both odd;
2. every element of $\Gamma(2)$ is congruent to the identity modulo $2$ and therefore preserves the class of a vector modulo $2$ and sign, so the $\Gamma(2)$-orbits on $\PP^1(\bZ)$ are exactly the three classes $[1:0]$, $[0:1]$, $[1:1]$, and each of them is a single $\Lambda$-orbit of primitive vectors;
3. $\mu$ is not congruent to the identity modulo $2$; it carries $[1:0]$ to $[1:1]$, and fixes $[0:1]$; and every element of $\generators{\Lambda,\mu}$ preserves the parity of the first coordinate, so that $\generators{\Lambda,\mu}$ has exactly two orbits (@def:group-orbit) on $\PP^1(\bZ)$, the primitive lines $[a:c]$ with $a$ odd and those with $a$ even.

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
So the terminal pair (@def:mmp-singularities) is one of $(1,1)$, $(1,-1)$, $(-1,1)$, $(-1,-1)$.
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
Within the odd part (@def:even-odd-part-reflection-group) $\Lambda$ is transitive on $[1:0]$ and on $[1:1]$ by item 2 and $\mu$ exchanges them, and within the even part (@def:even-odd-part-reflection-group) $\Lambda$ is transitive on $[0:1]$; hence these two sets are exactly the orbits.

:::

::: {.lemma #lem:unipotent-spinor-trivial title="The normalized real spinor norm is trivial on unipotent isometries"}

Let $N$ be a nondegenerate (@def:polarization) lattice and $g\in\Orth(N_\bR)$ unipotent. Then $\spinornorm_\bR(g)=1$.
:::

::: {.proof}

Put $V\definedas N\otimes_\bZ\bR$; unipotence says that $n\definedas g-\id$ is nilpotent.
Then
$$
\nu\definedas\log g\definedas\sum_{k\geq1}\frac{(-1)^{k+1}}{k}n^k
$$
is a finite sum, hence a nilpotent endomorphism of $V$ with $\exp(\nu)=g$; both statements are the formal identities for a nilpotent endomorphism evaluated in the finite-dimensional commutative (@def:operation-axioms) algebra $\bR[n]$.

*All real powers of $g$ are isometries.*
Put $g^t\definedas\exp(t\nu)=\sum_{k\geq0}t^k\nu^k/k!$, again a finite sum.
For integral $t$ this is the $t$-th power of $g$ and hence an isometry, so for fixed $x,y\in V$ the function $t\mapsto\beta(g^tx,g^ty)-\beta(x,y)$ is a polynomial in $t$ vanishing on $\bZ$, hence identically zero.
Thus $g^t\in\Orth(V)$ for every real $t$; and $g^sg^t$ and $g^{s+t}$ agree for integral $s,t$, so their difference, again a polynomial in $(s,t)$, vanishes identically.
Hence $t\mapsto g^t$ is a homomorphism $(\bR,+)\to\Orth(V)$ carrying $1$ to $g$.

*Conclusion.*
The composite $\chi\colon t\mapsto\spinornorm_\bR(g^t)$ is a homomorphism from $(\bR,+)$ into $\bR^\times/(\bR^\times)^2$, a group (@def:group) of exponent two, and $t=2\cdot(t/2)$ gives $\chi(t)=\chi(t/2)^2=1$.
Therefore $\spinornorm_\bR(g)=\chi(1)=1$.
:::

::: {.lemma #lem:enriques-level-two-transvections title="The level-two transvections of $\ten$: images, plane actions and spinor signs"}

Let $N=\ten=U\oplus U(2)\oplus E_8(2)$, with $e,f$ the hyperbolic basis of $U$, $e',f'$ that of $U(2)$, and $r_1,r_2$ two orthogonal roots of the summand $E_8(2)$ — the roots corresponding to $e_1-e_2$ and $e_1+e_2$ in the coordinates of @prop:ten-plane-classes; the summand is negative definite (@def:definiteness), so its norms (@def:lattice-basic-invariants) lie in $4\bZ$ and its inner products in $2\bZ$.
Put $\alpha\definedas r_1+r_2$ and $z\definedas 2e+2f+\alpha$.
Then $\alpha^2=-8$, the vector $z$ is primitive isotropic of divisibility (@def:lattice-divisibility) $2$, and $\beta(x,\alpha)\in2\bZ$ for every $x\in N$.

Write $E_{a,w}$ in the notation of @def:eichler-siegel — $a$ the isotropic vector (@def:isotropic-subspace), $w$ the vector orthogonal to it — so that
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

*The discriminant kernel (@def:mm-integral-spinor-data), on a full generating set.*
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
For the two sign changes, @lem:minus-identity-spinor-norm gives $\spinornorm_\bR(-\id_U)=[(-1)^1]$ and $\spinornorm_\bR(-\id_{U(2)})=[(-1)^1]$, the summands having positive index (@def:maximal-positive-definite-subspace) one, and the spinor norm of an orthogonal sum (@def:orthogonal-sum) is the product of the spinor norms of its summands, since a reflection of a summand is the corresponding reflection of the sum; so both have spinor norm $-1$.

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

1. $\theta$ stabilizes $P_2$, lies in $\ker\rho$, and fixes the *vector* $z+e'$; its spinor norm (@def:lattice-basic-invariants) is $-1$.
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
By part 3 of @lem:congruence-two-transitivity the group generated by these matrices is transitive on the primitive lines of $P_1$ with first coordinate odd, and on those with first coordinate even; and those two sets are exactly the two divisibility (@def:lattice-divisibility) classes of $P_1$ computed in @lem:enriques-level-two-transvections.
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
Since every witness lies in $\ker\rho\subseteq\Gamma$, the stabilizer (@def:group-orbit) inside $\Gamma$ of each of these objects meets $\Gamma\setminus\Orth^+(N)$.

:::

::: {.corollary #cor:enriques-preimage-vs-positive title="The spinor-positive half of a discriminant preimage"}

Let $N = \ten$, let $M\leq\Orth(A_\ten,q_\ten)$ and $\Gamma=\rho^{-1}(M)$, so that $\rho(\Gamma)=M$ by @thm:two-elementary-surjectivity; put $\Gamma^+=\Gamma\intersect\Orth^+(N)$, and let $\tau_0$ be as in @lem:enriques-level-two-transvections.

1. $\Gamma = \Gamma^+\sqcup\Gamma^+\tau_0$, so $\Gamma^+$ has index two in $\Gamma$, and $\rho(\Gamma^+)=\rho(\Gamma)=M$.
2. $\Gamma$ and $\Gamma^+$ have the same orbits (@def:group-orbit) on primitive isotropic lines, on primitive isotropic planes and on flags.
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
Two admissible anti-isometries differ by $\tau\in\Orth(A_{\ten},q_{\ten})$, since both satisfy $q_{\ten}(\gamma x) = -q_{\sen}(x)$; by the surjectivity of the discriminant representation (@def:discriminant-rep) (@thm:two-elementary-surjectivity) $\tau = \rho_{\ten}(s)$ for some isometry $s$ of $\ten$, and then
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
