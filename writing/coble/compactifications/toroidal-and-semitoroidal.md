# Toroidal and semitoroidal compactifications {#sec-toroidal-and-semitoroidal}

## Toroidal compactifications

::: {.definition #def:toroidal-compactification}

A **toroidal compactification** $\torcpt{\FG}$ refines the singular cusps of the Baily--Borel compactification by choosing an admissible rational polyhedral fan $\torfan_I$ for each cusp $I$.

Locally, the boundary is modeled on toric varieties $X_{\torfan_I}$.
:::

For the degree-two K3 period space $F_2$ of dimension $19$, the Baily–Borel boundary has one $0$-cusp and four $1$-cusp curves, all incident to that point. The four curves have root-lattice labels $A_{17}$, $D_{10}\oplus E_7$, $E_8^2\oplus A_1$, and $D_{16}\oplus A_1$. Hence the boundary has codimension $18$. The toroidal fan supplies divisorial boundary above the $0$-cusp; its choice changes the compactification [@AET23, §3B–3C].

More generally, for primitive degree $2d$ polarizations, Scattone's cusp classification gives one orbit of $0$-cusps when $d$ is squarefree [@Sca87, §4]. A $0$-cusp $I$ determines the hyperbolic lattice $I^\perp/I$ and its positive cone, on whose rational closure the admissible fan is supported. The explicit Coxeter construction below concerns the degree-two lattice; uniqueness of a cusp by itself does not select a Coxeter fan.

At the degree-two cusp $I=\ZZ\delta$, the lattice $I^\perp/I$ has signature $(1,18)$ and rank $19$. In a tube realization, quotienting by the integral cusp translations turns its complex coordinates $z_i$ into torus coordinates $q_i=e^{2\pi i z_i}$. Along a one-parameter degeneration these have leading terms $q_i\sim c_i t^{\lambda_i}$; the exponent vector $\lambda\in I^\perp/I$ is the monodromy cocharacter that picks a ray in the positive cone. A fan decides which such rays have a limit in the toroidal chart [@AET23, §3C; @AE23, §5]. The logarithmic monodromy and the triple-point invariant of a Type III central fiber are related by @prop:type-iii-monodromy-triple-points.

::: {.example #ex:second-voronoi-semiabelic title="The second Voronoi compactification of $\mathcal A_g$"}

For $\mathcal A_g=\operatorname{Sp}_{2g}(\ZZ)\backslash\mathfrak H_g$, the cusp cone of maximal torus rank is the cone of positive definite symmetric quadratic forms $Q$ on $M_\RR$, with $M\simeq\ZZ^g$. A form determines periodic Voronoi and Delaunay decompositions of $M_\RR$. The relative interiors of the second Voronoi cones are the loci where their combinatorial type is constant; their closures form the fan [@AET23, Intro., p. 4].

Write $N=M^\vee$ and let $f_Q\colon M\to N_\RR$ be the symmetric map associated with an integral form $Q$. For a one-parameter degeneration with monodromy vector $Q$, Mumford's construction takes the cone over a shifted Voronoi tiling in $\RR\oplus N_\RR$, forms its infinite toric variety, and divides by the translation action of $M$. Its tropical polarized limit is the real torus with divisor
$$
(X_{\mathrm{trop}},\Theta_{\mathrm{trop}})
=\bigl(N_\RR,\,\ell+f_Q(\operatorname{Vor}Q)\bigr)/f_Q(M),
\qquad X_{\mathrm{trop}}=N_\RR/f_Q(M),
$$
where $\ell$ is the shift of the tiling. The cell decomposition of the tropical torus induced by the divisor is the dual complex of the central fiber. At each vertex of the tropical divisor, the local fan gives the normalization of a toric component of that fiber; shared cells give the gluing [@AET23, Intro., pp. 3–4].

The height projection $\RR\oplus N_\RR\to\RR$ defines a toric morphism from the infinite toric variety to $\AA^1$. Its generic fiber is a torus; after the $M$-quotient it recovers the punctured abelian family. The height-one cells describe the boundary components in the central fiber [@Mum72; @AN99, §1.8]. Dually, the theta-function construction forms a graded algebra from the polarization's piecewise-linear function and takes its $\operatorname{Proj}$; the domains where this function is linear give the Delaunay decomposition. The Voronoi and Delaunay decompositions are dual descriptions of the same degeneration, and the second Voronoi fan records when their combinatorial type changes [@AN99; @AET23, Intro., p. 4].

Alexeev's compactification by stable semiabelic pairs $(P,\Theta)$ has a main irreducible component containing $\mathcal A_g$, whose normalization is the toroidal compactification for this fan [@Ale02, Introduction]. The theta divisor is part of the boundary object, not just a numerical polarization.
:::

::: {.example #ex:nodal-elliptic-period title="A nodal elliptic period"}

In the family $E_t\colon y^2=x^3+x^2+t$, the fiber $E_0$ is the nodal cubic $y^2=x^2(x+1)$. Choose a vanishing cycle $\alpha$, a cycle $\beta$ with $\alpha\cdot\beta=1$, and normalize the holomorphic differential by $\int_\alpha\omega_t=1$. Picard–Lefschetz monodromy sends $\beta$ to $\beta+\alpha$, so the remaining period $\tau_t=\int_\beta\omega_t$ changes by an integer on continuation around $t=0$. Consequently $q_t=\exp(2\pi i\tau_t)$ is single valued. This is the rank-one torus coordinate that the toroidal construction extends across the cusp.
:::

For genus two, write $Q(x,y)=ax^2+by^2+c(x+y)^2$. The triangular reflection chamber and the cone over that chamber are schematic views of the fan. The Voronoi picture and its two hexagons show the cell decomposition that descends to the tropical torus; setting one of $a,b,c$ to zero changes the polygonal type along a wall [@AET23, Intro., pp. 3–4].

In the pictured honeycomb cellulation of the tropical torus, there are two vertices joined by three edges. The corresponding central fiber has two toric components, each with the fan of $\PP^2$, glued along three boundary curves. The Delaunay triangulation is dual to this cellulation. This describes that particular cell type; it does not assert the same component count for every positive form. When one of $a,b,c$ reaches zero, its hexagons collapse to quadrilaterals and the form reaches a wall of this three-coordinate chamber. Setting two to zero reaches a boundary ray; crossing a wall changes the Delaunay triangulation [@AN99, §1.8].

In period coordinates, a symplectic marking writes an abelian variety as $\CC^g/(\ZZ^g+\tau\ZZ^g)$ with $\tau\in\mathfrak H_g$. At a maximal-rank cusp, the unipotent translations act by $\tau\mapsto\tau+S$ for $S\in\operatorname{Sym}_g(\ZZ)$, so $q_{ij}=\exp(2\pi i\tau_{ij})$ are coordinates on the corresponding torus quotient. A one-parameter degeneration has a monodromy quadratic form $Q=(n_{ij})$; the exponents in $q_{ij}\sim c_{ij}t^{n_{ij}}$ record its cocharacter. The Voronoi construction above uses this same $Q$ [@AET23, Intro., pp. 3–4].

For example, $Q=\left(\begin{smallmatrix}2&1\\1&3\end{smallmatrix}\right)$ is positive definite and $Q(\ZZ^2)$ has index $5$ in $\ZZ^2$. The real torus $\RR^2/Q(\ZZ^2)$ carries the periodic Voronoi tiling associated with $Q$. Coning a lattice-compatible shift of that tiling at height $1$ gives the infinite toric fan; the quotient by $\ZZ^2$ produces the degeneration. The chosen tiling controls its central fiber, while $Q$ fixes the monodromy [@AET23, Intro., pp. 3–4].

![Schematic triangular reflection chamber in the hyperbolic disc.](/rendered/tesselate_disc.jpg){#fig-ppav-reflection-chamber}

![Cone over the schematic chamber tiling.](/rendered/tesselate_disc2.jpg){#fig-ppav-coned-chambers}

![Voronoi cells in the genus-two illustration.](/rendered/Vor_tess.jpg){#fig-ppav-voronoi-cells}

![Two hexagonal cells with edge lengths $a,b,c$ in the archive illustration.](/rendered/honeycomb_sidelengths.jpg){#fig-ppav-hexagons}

## Semitoroidal compactifications

::: {.definition #def:semitoroidal-compactification}

A **semitoroidal compactification** $\semitorcpt{\FG}$ replaces the fans of a toroidal compactification with $\Gamma$-admissible **semifans** $\mcf_I$ [@Loo02, Def. 6.1; @AE23, Def. 5.11].

A semifan $\mcf_I$ consists of the same data as a fan, except that its cones need only be locally polyhedral in $C_I$ rather than rational polyhedral, together with a compatibility condition at each $1$-cusp: for $I = \ZZ\delta \oplus \ZZ\lambda$ a primitive rank two isotropic lattice, the tiles of the periodic tiling of $I^{\perp}/I$ induced by the cones of $\mcf_I$ containing $\ZZ\lambda$ are of the form $B \times (H_I \otimes \RR)$ for bounded polytopes $B$, and the primitive sublattice $H_I$ is required not to depend on the choice of $\delta\in I$ [@AE23, Def. 5.11; @Loo02, Def. 6.1].
As for a fan, the cones of $\mcf_I$ are locally finite in $C_I$.
:::

::: {.proposition #prop:semifan-refinement-morphism title="Morphisms from refinements"}

Let $\mcf$ and $\mathfrak{G}$ be semifans for $\FG$ such that $\mathfrak{G}$ refines $\mcf$.
Then there is a morphism $\overline{F}^{\mathfrak{G}} \to \overline{F}^{\mcf}$ that maps strata to strata [@AE23, Thm. 5.13; @Loo02, Lem. 6.6].
:::

::: {.proof}

This is [@AE23, Thm. 5.13], which cites [@Loo02, Lem. 6.6].
:::

::: {.corollary #cor:toroidal-to-baily-borel title="The tower over the Baily--Borel compactification"}

Let $\torfan$ be a fan and $\mcf$ a semifan for $\FG$ such that $\torfan$ refines $\mcf$.
Then there are morphisms
$$
\torcpt{\FG} \too
\semitorcpt{\FG} \too
\bbcpt{\FG}
.
$$
:::

::: {.proof}

Every fan is a semifan, and the semifan $\{C_I^+\}$ defines the Baily--Borel compactification [@AE23, Ex. 5.12].
Every semifan refines $\{C_I^+\}$, because its cones lie in $C_I^+$.
Apply @prop:semifan-refinement-morphism to $\torfan$ refining $\mcf$ and to $\mcf$ refining $\{C_I^+\}$.
:::

::: {.theorem #thm:tower-semitoroidal}

Let $F$ be a type IV arithmetic quotient and $\overline F$ a normal compactification of $F$.
Then $\overline F$ is a semitoroidal compactification, for some semifan $\mcf_I$, if and only if it sits between some toroidal and the Baily--Borel compactification, that is if there is a fan $\torfan$ and a tower
$$
\torcpt{\FG} \too
\overline F \too
\bbcpt{\FG}
$$
of morphisms over $\bbcpt{\FG}$ [@AE23, Thm. 5.14].
:::

::: {.proof}

This is [@AE23, Thm. 5.14].

The forward implication follows on refining the semifan to a fan.
For the converse, the maximal cones of the semifan are the unions of the classes of maximal cones of $\torfan$ under the equivalence relation generated by sharing a codimension one face whose one-dimensional boundary stratum is contracted by $\torcpt{\FG} \to \overline F$.
:::

## Generalized Coxeter semifans

::: {.definition #def:coxeter-semifan}

Let $W\leq\Orth(L)$ be a reflection group with fundamental chamber $\mathfrak{C}$, acting on the rational closure $C_\QQ$ of a cone.
The **Coxeter semifan** $\mathcal F^{\mathrm{cox}}$ of the chamber has, modulo $W$, the cones $\mathfrak{C}$, its faces, and their $W$-translates; it is a fan if and only if $W$ has finite covolume [@AE22, Def. 3.5, printed p. 10].
:::

::: {.definition #def:generalized-coxeter-semifan}

Let $\eta$ be a $0$-cusp with Coxeter diagram $G(\Gamma_\eta)$, reflection group $W$ and fundamental chamber $\mathfrak{C}$.
Partition the vertices of $G(\Gamma_\eta)$, that is the simple roots, into $\Phi = \Phi^{\relevant} \sqcup \Phi^{\irrelevant}$, the **relevant** and the **irrelevant roots**.
Let $W^{\irrelevant} \subseteq W$ be the subgroup generated by the reflections in the irrelevant roots.

The **generalized Coxeter semifan** $\mcf_{\mathrm{gen}}$ has, modulo $W$, the unique maximal cone $\Union_{h \in W^{\irrelevant}} h(\mathfrak{C})$; its other cones are the faces of $\mathfrak{C}$ and their $W$-translates [@AE22, Def. 9.1, printed p. 53].
Its maximal cones are the unions of Weyl chambers $g\big(\Union_{h \in W^{\irrelevant}} h(\mathfrak{C})\big)$ for $g \in W$.
:::

::: {.proposition #prop:generalized-coxeter-semifan-is-fan title="When a generalized Coxeter semifan is a fan"}

The generalized Coxeter semifan $\mcf_{\mathrm{gen}}$ of @def:generalized-coxeter-semifan is a fan if and only if $W$ has finite covolume and $W^{\irrelevant}$ is finite, that is, the irrelevant roots span an elliptic subdiagram [@AE22, Rem. 9.11, printed p. 57].
:::

::: {.proof}

This is [@AE22, Rem. 9.11].
:::

::: {.theorem #thm:degree-two-k3-semifan title="The ramification semifan for degree-two K3 surfaces"}

Let $F_2$ be the moduli space of degree-two polarized K3 surfaces $(X,L)$. The covering involution of $X\to\PP^2$ has ramification divisor $R\in|3L|$. The normalization of the KSBA compactification of pairs $(X,\eps R)$ is a semitoroidal compactification of $F_2$. Its semifan is coarsened by the Coxeter fan of the hyperbolic lattice $N=U\oplus E_8(-1)^2\oplus A_1(-1)$: equivalently, the Coxeter fan refines the ramification semifan [@AET23, Thm. 1.2].
:::

::: {.proof}

The normalization and refinement are [@AET23, Thm. 1.2]. The morphism from the Coxeter toroidal compactification to this semitoroidal compactification follows from @prop:semifan-refinement-morphism.
:::

![Schematic reflection chamber with an ideal vertex.](/rendered/F2HyperbolicReflection.jpg){#fig-k3-ideal-reflection-chamber}

## KSBA compactifications

::: {.definition #def:ksba-compactification}

A pair $(X, D = \Sum b_j D_j)$ is **KSBA-stable** [@KS88; @Ale96] if:

1. $X$ is a projective demi-normal variety;

2. $0 < b_j \le 1$;

3. the pair $(X, D)$ has **semi log canonical (slc)** singularities;

4. $K_X + D$ is ample and $\QQ$-Cartier.

For K-trivial varieties (like K3 or Enriques surfaces), one uses pairs $(X, \eps R)$ for $0 < \eps \ll 1$ and a polarizing divisor $R$. On a slc K3 limit with trivial dualizing sheaf, the divisor $R$ must be ample and avoid the log canonical centers; then small $\eps>0$ preserves the slc condition and makes $K_X+\eps R$ ample [@AE23, §6].
For a choice of polarizing divisor $R$ on the K3 surfaces of an open subset $U \subseteq F$, the **KSBA compactification** $\oF^R$ is the coarse space of the closure of $U$ in the moduli stack of stable pairs $(X, \eps R)$ [@AE23, Def. 6.11].
:::

::: {.example #ex:stable-curves-as-ksba title="The curve case of KSBA stability"}

Let $C$ be a connected projective nodal curve. The pair $(C,0)$ is KSBA-stable exactly when its dualizing sheaf $\omega_C$ is ample. For an irreducible component $E$ with normalization $\widetilde E$ and $n_E$ branches of nodes on it,
$$
\deg\bigl(\omega_C|_E\bigr)=2g(\widetilde E)-2+n_E.
$$
Thus a rational component needs at least three distinguished branches and an elliptic component needs at least one. The stable curves of [@DM69] are precisely these one-dimensional stable varieties.

For a one-parameter family of smooth curves, stable reduction first makes the family semistable after finite base change. Passing to the relative minimal model contracts exceptional curves in the total space; the relative canonical model then contracts central-fiber components on which the dualizing sheaf has degree zero. In the nodal central fiber these are rational components with two distinguished branches. The final stable curve is unique after the chosen base change, although semistable models can differ [@DM69]. The ample dualizing sheaf is the part of this construction that extends to the KSBA condition $K_X+D$ ample in higher dimensions.
:::

::: {.example #ex:degree-two-k3-branch-pair title="The sextic branch pair"}

For a generic degree-two polarized K3 surface, $\pi\colon X\to\PP^2$ is a double cover branched over a plane sextic $B$. Its ramification divisor is $R=\operatorname{Fix}(\iota)\in|3L|$. The canonical bundle formula gives
$$
K_X+\eps R=\pi^*\!\left(K_{\PP^2}+\frac{1+\eps}{2}B\right).
$$
For the degenerations in the stable-pair compactification, stability of $(X,\eps R)$ is equivalent to stability of the branch pair $(Y,\frac{1+\eps}{2}B)$; the quotient surface $Y$ can degenerate along with $B$ [@AET23, Intro., p. 3]. This is Hacking's degree-six plane-curve compactification problem [@Hac04], with the ramification divisor furnishing the chosen polarization.
:::

## Looijenga compactifications

::: {.definition #def:looijenga-compactification}

Let $\mch$ be a $\Gamma$-invariant arrangement of hyperplane sections of the period domain $D$.
The **Looijenga compactification** $\overline{\Gamma\backslash D}^{\,\mch}$ is the compactification of the arrangement complement $\Gamma\backslash(D - \mch)$ determined by $\mch$ [@Loo02, Thm. 7.4].
:::

::: {.corollary #cor:looijenga-empty-arrangement title="The empty arrangement"}

If $\mch$ is empty, then the Looijenga compactification of @def:looijenga-compactification is the Baily--Borel compactification $\bbcpt{\FG}$.
:::

::: {.proof}

The hypothesis of [@Loo02, Cor. 7.5] holds vacuously for the empty arrangement, and the arrangement complement is $D$.
So the Looijenga compactification is the proj of the algebra of $\Gamma$-automorphic forms on $D$ [@Loo02, Cor. 7.5].
The automorphic line bundle on $\bbcpt{\FG}$ is ample, and the sections of its $k$-th tensor power are the $\Gamma$-automorphic forms of degree $k$ [@Loo02, Thm. 2.4].
So this proj is $\bbcpt{\FG}$.
:::

## Recognizable divisors

::: {.definition #def:recognizable-divisor}

A polarizing divisor $R$ on the generic surface in $F_S$ is **recognizable** if, for any quasipolarized Kulikov degeneration $\mcx \to \Delta$, the divisor $R$ extends unambiguously to a flat limit $R_0 \subset \mcx_0$, unique up to $\Aut^0(\tilde{\mcx}_0)$ in any other smoothing.
:::

::: {.theorem #thm:recognizable-semitoroidal}

If $R$ is recognizable, then the normalization of the KSBA compactification $\oF^R$ is isomorphic to a semitoroidal compactification $\overline{F_S}^{\mcf_R}$, defined by a specific semifan $\mcf_R$ [@AE23, Thm. 9.1].
:::

::: {.proof}

This is [@AE23, Thm. 9.1].
:::

::: {.theorem #thm:semifan-stratum title="The semifan of a recognizable divisor is the semifan of the stratum function"}

Let $R$ be a recognizable polarizing divisor for $F_S$ (@def:recognizable-divisor) and let $\eta$ be a $0$-cusp. Put $\bar T=\eta^\perp/\eta$ and let $C\subset\bar T_\RR$ be the positive cone. Then there is a well-defined function
$$
\bS_R\colon\bar T\cap C\longrightarrow\{\text{combinatorial types of KSBA-stable pairs}\}
$$
assigning to a monodromy invariant $\lambda$ the combinatorial type of the stable limit of a degeneration of $R$-polarized pairs with monodromy $\lambda$; it depends only on the projective class of $\lambda$; the loci on which it is locally constant are the cones of a semifan $\mcf_{R,\eta}$ at $\eta$; and the normalization of the KSBA compactification $\oF^R$ is the semitoroidal compactification for the collection of these semifans. Up to the action of the monodromy group, the cones of $\mcf_{R,\eta}$ are therefore exactly the sets of monodromy invariants carrying a fixed combinatorial type.
:::

::: {.proof}

The existence of $\bS_R$ and the identification of the cones are the two statements of [@AE23] quoted in the proof of [@AE22, Prop. 8.1, printed p. 41]: the cones "are determined as the (closures of) collections of monodromy invariants $\lambda\in\sigma$ for which the KSBA-stable model of a degeneration with monodromy invariant $\lambda$ has a fixed combinatorial type" ([@AE23, Thm. 9.3 with Def. 8.12]), and "recognizability ensures that any degeneration with a given monodromy invariant in the projective class of $\lambda$ has the same combinatorial type" ([@AE23, Cor. 8.13]). The identification of the normalization of the KSBA compactification with the semitoroidal compactification is [@AE23, Thm. 9.1], which is @thm:recognizable-semitoroidal.

Neither quoted statement is restricted to a class of divisors: the first speaks of "the KSBA-stable model of a degeneration", the second of recognizable divisors as such. The proposition of [@AE22] in whose proof they are quoted instantiates them at the pairs $(X,\eps C_g)$, which is why its own hypotheses carry $g\ge2$. The statements of [@AE23] used here are the ones that proof reproduces; they are cited by the printed pages of arXiv:2101.12186v3.

$\Gamma$-admissibility: an element of $\Gamma$ fixing $\eta$ carries a degeneration of monodromy $\lambda$ to one of monodromy $g\lambda$ with the same stable limit, so $\bS_R$ is invariant under $\Stab_\Gamma(\eta)$.
:::

::: {.example #ex:recognizable-divisors}

Two basic examples of recognizable divisors:

1. The **rational curve divisor** $R_{\rcop} = \Sum R_i$ (the sum of all smooth rational curves in $|L|$), recognizable for all $d$ [@AE23]. The assertion is also readable in a deposited source: [@AE23a] states that $R_{\rcop}$ "was proven to be recognizable in" [@AE23], and gives $R_{\rcop}\in|n_dL|$.

2. The **ramification divisor** $R_\iota$ of a nonsymplectic involution.

:::

::: {.lemma #lem:unigonal-restriction title="What the restriction theorem gives at the cusp with $p_*=1$"}

Let $\eta$ be the $0$-cusp of $F_{2d}$ with $p_*(\delta)=1$, so that $k=d$ (@lem:cusp-census), with boundary lattice $\bar T=\langle-2d\rangle\oplus U\oplus E_8(-1)^{\oplus2}$ and $t$ a generator of the $\langle-2d\rangle$ summand, $t^2=-2d$. Then: (i) the restriction of $\mcf_{R_{\rcop},\eta}$ to $t^\perp$ is a **fan**; (ii) $t^\perp\cap C^+$ is a union of cones of $\mcf_{R_{\rcop},\eta}$; (iii) that fan is the fan of [@ABE22, §4C, printed p. 14]; and (iv) each maximal cone of it is itself a cone of $\mcf_{R_{\rcop},\eta}$, not only a slice of a $19$-dimensional one. All four are [@AE23, Thm. 10.16, printed p. 38] with its proof.
:::

::: {.proof}

The cusp with $p_*(\delta)=1$ is the one the unigonal locus meets (@lem:unigonal-locus-cusp-support), and its boundary lattice is $\langle-2d\rangle\oplus U\oplus E_8(-1)^{\oplus2}$ with $k=d$ (@lem:cusp-lattice-p-greater-one). [@AE23, Thm. 10.16, printed p. 38] states that the restriction of $\mcf_{R_{\rcop}}$ to $\langle-2d\rangle^\perp$ is a fan and that $\langle-2d\rangle^\perp\cap C_\delta^+$ is a union of cones of $\mcf_{R_{\rcop}}$, which are (i) and (ii) for $t^\perp=\langle-2d\rangle^\perp$; its proof identifies that restriction with the fan of [@ABE22, §4C, printed p. 14], which is (iii), and shows that each of its maximal cones is a cone of $\mcf_{R_{\rcop}}$ rather than only a slice, which is (iv).
:::

::: {.lemma #lem:f2-argument-does-not-transfer title="The $F_2$ determination does not transfer to the cusps with $p_*>1$ and $k=1$"}

Let $\eta$ be a $0$-cusp of $F_{N^2}$ with $N\ge2$ whose class $\{\pm q\}$ is a unit modulo $N$, so that $p_*(\delta)>1$ and $k=d/p_*^2=1$ (@lem:cusp-census). Then: (1) the boundary lattice of $\eta$ is $\langle-2\rangle\oplus U\oplus E_8(-1)^{\oplus2}$, the lattice of the $F_2$ cusp, and its Coxeter fan is the printed fan of twenty-four $(-2)$-roots [@AET23, Def. 4.1 and Fig. 1, printed pp. 21--22]; and (2) the unigonal locus meets only the $0$-cusp with $p_*=1$ (@lem:unigonal-locus-cusp-support), so [@AE23, Thm. 10.16, printed p. 38], whose assertion is a restriction to $\langle-2d\rangle^\perp$ on the unigonal locus, yields nothing at $\eta$. Consequently the argument of @lem:f2-cusp-is-the-refinement-case **does not transfer**: no analogue of the nine-cone fan is recorded on the unigonal hyperplane of $\bar T$ at such a cusp, and no cone of $\mcf_{R_{\rcop},\eta}$ is recorded there in the sources read.
:::

::: {.proof}

Assertion (1) is @lem:cusp-lattice-p-greater-one at $k=1$ together with @lem:k-one-two-sharp's identification of the cusp family. For (2), [@AE23, Thm. 10.16, printed p. 38] restricts $\mcf_{R_{\rcop}}$ to $\langle-2d\rangle^\perp$ and identifies it with the fan of [@ABE22, §4C, printed p. 14]; its proof uses the unigonal locus, a family of elliptic K3 surfaces with $L=s+(d+1)f$, and @lem:unigonal-locus-cusp-support records from the same proof that this locus meets only the $p_*=1$ cusp. At $\eta$ the two lattices agree but the restricting family is absent, so the theorem's hypothesis does not hold there and its conclusion is unavailable — the coincidence of boundary lattices transfers nothing by itself.
:::

::: {.lemma #lem:f2-cusp-is-the-refinement-case title="At the unique $0$-cusp of $F_2$ the semifan refines the Coxeter fan along the unigonal hyperplane"}

Let $\eta$ be the unique $0$-cusp of $F_2$, with boundary lattice $\bar T=U\oplus E_8(-1)^{\oplus2}\oplus A_1(-1)$ and $t$ a generator of the $A_1(-1)$ summand, so that $t^\perp=U\oplus E_8(-1)^{\oplus2}$ is the unigonal hyperplane and a wall of the Coxeter chamber. Then the restriction of $\mcf_{R_{\rcop},\eta}$ to $t^\perp$ is the fan of [@ABE22, §4C, printed p. 14], which subdivides the chamber $P\subset t^\perp$ by the four hyperplanes $\beta_L^\perp,\gamma_L^\perp,\beta_R^\perp,\gamma_R^\perp$ into nine cones, none of the four being the mirror of a root. So at this cusp the semifan realises the **refinement** half of the dichotomy of @rmk:coarsening-is-one-half, along that wall: the nine cones are strictly finer than $P$, and by @lem:semifan-determined-on-one-chamber they are the part of the semifan's trace on $\overline{\mathfrak C}$ that lies in $t^\perp$.
:::

::: {.proof}

[@AE23, Thm. 10.16, printed p. 38] identifies the restriction of $\mcf_{R_{\rcop},\eta}$ to $t^\perp$ with the fan of [@ABE22, §4C, printed p. 14], and its proof shows that each of its maximal cones is itself a cone of $\mcf_{R_{\rcop},\eta}$ and not only a slice of a $19$-dimensional one. That fan cuts $P$ by the four hyperplanes into nine cones [@ABE22, §4C, printed p. 14]. None of the four is the mirror of a root of $\bar T$: $\gamma_L^2=-4$ and $\beta_L^2=-8$ are printed there, a vector of $\operatorname{span}(t,\gamma_L)$ is $at+k\gamma_L$ with square $-2a^2-4k^2$, which equals $-2$ only for $k=0$, that is for $t$ itself, and the same computation with $\beta_L$ gives $-2a^2-8k^2$, again only $t$. So the nine cones strictly refine $P$ along $t^\perp$, and @lem:semifan-determined-on-one-chamber places them in the semifan's trace on $\overline{\mathfrak C}$.
:::

::: {.lemma #lem:semifan-determined-on-one-chamber title="The semifan is determined on one Coxeter chamber, whatever the half of the dichotomy"}

Let $\eta$ be a $0$-cusp of $F_{2d}$ with boundary lattice $\bar T=\delta^\perp/\delta$, let $W_2(\bar T)$ be the group generated by the reflections in the $(-2)$-vectors of $\bar T$, and let $\mathfrak C$ be its fundamental chamber in the positive cone. Then $\mcf_{R_{\rcop},\eta}$ is invariant under $W_2(\bar T)$, and consequently it is **determined by its restriction to the closure of a fundamental chamber**: a cone lies in $\mcf_{R_{\rcop},\eta}$ if and only if it is a $W_2(\bar T)$-translate of a cone of $\mcf_{R_{\rcop},\eta}$ whose relative interior meets $\overline{\mathfrak C}$. By the $\Gamma$-admissibility of a semifan [@AE23, Def. 5.9 and Def. 5.11, printed pp. 13--14] finitely many such cones suffice. This holds for either half of the dichotomy of @rmk:coarsening-is-one-half: it uses only that every $(-2)$-reflection of $\bar T$ lies in the monodromy, and not that the semifan coarsens or refines the Coxeter semifan.
:::

::: {.proof}

By @lem:minus-two-reflections-lift each reflection $s_x$ in a $(-2)$-vector $x$ of $\bar T$ is realised by an isometry of $L_{2d}$ lying in $\Gamma$ and fixing the cusp, so $\mcf_{R_{\rcop},\eta}$ is invariant under it [@AE23, Def. 5.9, printed p. 13]; as the $s_x$ generate $W_2(\bar T)$, the semifan is $W_2(\bar T)$-invariant. A $W_2(\bar T)$-invariant family of cones is stable under translation by the group, so its cones are unions of $W_2(\bar T)$-orbits, and every such orbit meets $\overline{\mathfrak C}$ because $\mathfrak C$ is a fundamental chamber; hence the cones contained in a given orbit are exactly the translates of the cones of the orbit that meet $\overline{\mathfrak C}$, and the fan is determined by that trace. Finally $\Gamma$-admissibility gives finitely many $\Gamma$-orbits of cones, and $W_2(\bar T)\subseteq\Gamma_\eta$ by the same lemma, so finitely many cones of the trace represent all of them.
:::

::: {.remark #rmk:coarsening-is-one-half title="(W) is the coarsening half of the dichotomy it belongs to"}

Hypothesis **(W)** of @thm:semifan-recognizable-divisor is one half of a dichotomy: it asks that every cone of $\mathfrak M_{R,\eta}$ be a **union** of cones of the Coxeter semifan, that is, that $\mathfrak M_{R,\eta}$ coarsen it. The owner's research statement conjectures the weaker pair, that the Coble semifans are "either refinements or coarsenings of the canonical Coxeter fans" (`writing/research-statement/ResearchStatement.md:215`), and research#777 records that the refinement half is unsettled. So every statement on this page proved under (W) — @lem:wall-criterion, the conclusion of @lem:rcop-refinement-criterion that $\mcf_{R_{\rcop}}$ does not coarsen the Coxeter semifan at the $F_2$ cusp, @lem:generalized-unigonal-constraint and @lem:k-one-two-sharp — is **conditional on the coarsening half**, and none of them excludes the case in which the semifan refines the Coxeter semifan instead. The refinement half is not merely open: it is realised. At the unique $0$-cusp of $F_2$ the semifan strictly refines the Coxeter fan along the unigonal hyperplane (@lem:f2-cusp-is-the-refinement-case, from [@AE23, Thm. 10.16, printed p. 38] and [@ABE22, §4C, printed p. 14]), so the reading in which every Coble semifan coarsens the Coxeter fan is refuted at that cusp, and the owner's "either refinements or coarsenings" is the wording the results support. What does not depend on the reading: the boundary-lattice lemmas (@lem:cusp-lattice-p-greater-one, @lem:shared-one-cusp-lattice), the lifting lemma @lem:minus-two-reflections-lift, the generalized unigonal class and hyperplane @lem:generalized-unigonal-hyperplane, and the census @lem:cusp-census, which are statements about the lattices and the cusps alone.
:::

::: {.theorem #thm:semifan-recognizable-divisor title="The closed form, when the semifan coarsens the Coxeter semifan"}

Let $R$ be a recognizable polarizing divisor for $F_S$ and let $\eta$ be a $0$-cusp. Here $\Gamma$ is the group of changes of marking of the moduli problem, $\Gamma=\{\gamma\in O(L_{K3}):\gamma|_M=\mathrm{id}_M\}$ for the polarization lattice $M$ [@AE23, Cor. 2.9, printed p. 5], so for the degree-$2d$ problem, whose polarization lattice is $M=\langle 2d\rangle$, it is the isometry group of $M^\perp=L_{2d}$ and $\mathrm{Stab}_\Gamma(\eta)$ is the stabilizer of the cusp $\ZZ\delta$. Put $\bar T=\eta^\perp/\eta$ with positive cone $C$, let $\Gamma_\eta$ be the Coxeter diagram of the full reflection group $W=W(\Gamma_\eta)$ of $\bar T$, with vertex set $V$ and fundamental chamber $\mathfrak C$ (the diagram of [@AE22, §9A], whose long simple roots are the black vertices), and write $H_v^+=\{x\in\bar T_\RR:x\cdot v\ge0\}$. Assume

- **(W)** every cone of $\mcf_{R,\eta}$ is a union of cones of the Coxeter semifan $\mcf^{\mathrm{cox}}$, that is, $\mcf_{R,\eta}$ coarsens $\mcf^{\mathrm{cox}}$; and the merging is governed by the simple roots, in that there is a subset $J\subseteq V$ such that two chambers of the Coxeter complex whose common facet lies in $r^\perp$ lie in a common cone of $\mcf_{R,\eta}$ if and only if $r\in J$.

Then, with $I=V-J$, $W_J=\langle w_j\mid j\in J\rangle$ and $L=\Union_{h\in W_J}h(\mathfrak C)$:

1. the maximal cones of $\mcf_{R,\eta}$ are the $W$-translates of $L$, and its remaining cones are the images $g(F)$, $g\in W$, of the faces $F$ of $\mathfrak C$ that are not of the form $\mathfrak C\cap\bigcap_{j\in J'}r_j^\perp$ with $J'\subseteq J$; equivalently, $\mcf_{R,\eta}$ is the coarsening of $\mcf^{\mathrm{cox}}$ obtained by deleting the faces $\bigl(\bigcap_{j\in J'}\alpha_j^\perp\bigr)\cap\mathfrak C$ with $J'\subseteq J$;
2. $L=\bigcap_{i\in I}\bigcap_{h\in W_J}H^+_{h(r_i)}$ is convex and locally finite, its stabilizer in $W$ is $W_J$, and its support is the rational closure of $C$;
3. two Type II or Type III cones of $\mcf^{\mathrm{cox}}$, that is, two cones cut out by a maximal parabolic or an elliptic subdiagram, lie in one cone of $\mcf_{R,\eta}$ exactly when their relevant contents agree;
4. $\mcf_{R,\eta}$ is a fan if $W$ has finite covolume and $J$ spans an elliptic subdiagram; neither hypothesis is automatic (@rmk:semifan-not-a-fan).
:::

::: {.proof}

*Step 1: the relation on chambers.* Two neighbouring chambers of the Coxeter complex share exactly one facet, and that facet lies in exactly one mirror $r^\perp$ of a simple root. By the second clause of (W) the two chambers lie in one cone of $\mcf_{R,\eta}$ exactly when $r\in J$, and by @thm:semifan-stratum that is exactly when their combinatorial types agree.

*Step 2: the maximal cones.* By the first clause of (W) every cone of $\mcf_{R,\eta}$ is a union of cones of $\mcf^{\mathrm{cox}}$, hence a union of chambers closed under the relation of Step 1, and a maximal cone is a connected component of that relation. The reflections $w_j$, $j\in J$, generate $W_J$; the orbit $W_J\mathfrak C$ is connected for the relation, because a facet of $h(\mathfrak C)$ in $h(r_j)^\perp$ is shared with $hw_j(\mathfrak C)$, and it is closed under it, for the same reason. Hence the maximal cones are the closures of the sets $\Union_{h\in W_J}h(\mathfrak C^\circ)$, which are $L$ and its $W$-translates. This is [@AE22, Def. 9.1 and Def. 9.3, printed p. 53], and the coarsening as the deletion of the faces spanned by irrelevant roots is [@AEGS25, §5.2, printed p. 610].

*Step 3: the properties.* Assertions (2), (3) and (4) are [@AET23, Prop. 4.17, printed pp. 26--27] and [@AET23, Cor. 4.18, printed p. 27], in whose notation $I$ is the set of active and $J$ the set of inactive mirrors, with the fan criterion of [@AE22, Rem. 9.11, printed p. 57] and [@AET23, Rem. 4.19, printed p. 27]. The first clause of (W) is what makes Step 2 legitimate: without it a semifan may cut the interior of a chamber, and @prop:semifan-coarsening-fails exhibits exactly that.
:::

::: {.proposition #prop:semifan-coarsening-extension title="(W) is the extension of the universal family over the Coxeter toroidal compactification"}

Let $R$ be a recognizable polarizing divisor for $F_S$ and let $\eta$ be a $0$-cusp. Then the coarsening clause of (W) --- that every cone of $\mcf_{R,\eta}$ is a union of cones of the Coxeter semifan, equivalently that the Coxeter fan $\mcf^{\mathrm{cox}}$ refines $\mcf_{R,\eta}$ --- is equivalent to each of the following:

1. the family of stable pairs $(X,\eps R)$ extends from $F_S$ to a family of stable pairs over the toroidal compactification $\overline F^{\mcf^{\mathrm{cox}}}$;
2. there is a morphism $\overline F^{\mcf^{\mathrm{cox}}}\to\overline F^{\mcf_R}$ over the Baily--Borel compactification, and the family of item 1 is the pullback under it of the family over $\overline F^{\mcf_R}$.
:::

::: {.proof}

The family over $\overline F^{\mcf_R}$ is what the identification of @thm:semifan-stratum supplies, $\overline F^{\mcf_R}$ being the normalization of the KSBA compactification.

*Item 1 implies item 2.* A family of stable pairs over $\overline F^{\mcf^{\mathrm{cox}}}$ restricts to the universal family on $F_S$, so it and the universal family are classified by the same map to the moduli of stable pairs, which therefore extends over the boundary; that map is the required morphism, and the family is its pullback.

*The coarsening implies item 2.* A refinement of semifans gives a morphism of the semitoroidal compactifications, which is @prop:semifan-refinement-morphism [@AE23, Thm. 5.13; @Loo02, Lem. 6.6].

*Item 1 implies the coarsening.* A family of stable pairs over $\overline F^{\mcf^{\mathrm{cox}}}$ is flat, so its combinatorial type is locally constant on the base, hence constant on each boundary stratum of the toroidal compactification, the strata being connected. By @thm:semifan-stratum the cones of $\mcf_{R,\eta}$ are the loci of constant combinatorial type, so every cone of $\mcf^{\mathrm{cox}}$ lies in a cone of $\mcf_{R,\eta}$.
:::

::: {.proposition #prop:semifan-coarsening-fails title="(W) is not automatic: the rational-curve divisor on the elliptic locus"}

Let $F$ be the moduli space of elliptic K3 surfaces with section $s$ and singular fibers $f_1,\dots,f_{24}$, and let $R=s+m\sum_{i=1}^{24}f_i$ with $m\ge1$. Then the semifan of the stable-pair compactification of $F$ for the divisor $R$ is the rational-curve fan $\mcf_{\mathrm{rc}}$ of [@ABE22, §4C, printed p. 14], and $\mcf_{\mathrm{rc}}$ does not coarsen the Coxeter semifan: it subdivides each chamber of $\mcf^{\mathrm{cox}}$ by the four hyperplanes $\beta_L^\perp,\gamma_L^\perp,\beta_R^\perp,\gamma_R^\perp$ into nine cones, and none of the four is the mirror of a root.

On a surface of $F$ the rational curves of $|L|$ specialize to $s+(d+1)f$, so the rational-curve divisor of $F_{2d}$ restricts on this locus to $n_d\bigl(s+\frac{d+1}{24}\sum_i f_i\bigr)$, proportional to $R$ [@ABE22, Intro.].
:::

::: {.proof}

The semifan is $\mcf_{\mathrm{rc}}$ by [@ABE22, Intro., Thm. 1.2], which states that the normalization of the stable-pair compactification for $R$ is the toroidal compactification associated to "a subdivision of the Coxeter chamber into $9$ sub-chambers". The construction is [@ABE22, §4C, printed p. 14]: $\mcf_{\mathrm{rc}}$ is obtained "by subdividing the chamber $P$ by the hyperplanes $\beta_L^\perp$, $\gamma_L^\perp$, $\beta_R^\perp$, $\gamma_R^\perp$ into $3\cdot3=9$ maximal-dimensional subcones", where
$$
\beta_L=\alpha_3+2\alpha_2-\alpha_1,\qquad \gamma_L=\alpha_3-\alpha_1,\qquad
\beta_R=\alpha_{17}+2\alpha_{18}-\alpha_{19},\qquad \gamma_R=\alpha_{17}-\alpha_{19},
$$
and the simple roots satisfy $\alpha_i^2=-2$ and $\alpha_i\cdot\alpha_j\in\{0,1\}$ for $i\ne j$, with $\alpha_1$ pendant at $\alpha_4$ and $\alpha_2,\dots,\alpha_{18}$ a chain in the diagram of [@ABE22, Fig. 1, printed p. 12], so that $\alpha_1\cdot\alpha_2=\alpha_1\cdot\alpha_3=0$ and $\alpha_2\cdot\alpha_3=1$. Hence
$$
\gamma_L^2=-4-2\,\alpha_1\cdot\alpha_3=-4,\qquad
\beta_L^2=-12+4\,\alpha_2\cdot\alpha_3-2\,\alpha_1\cdot\alpha_3-4\,\alpha_1\cdot\alpha_2=-8,
$$
as [@ABE22, §4C, printed p. 14] prints them, and by the symmetry exchanging the two ends of the diagram $\gamma_R^2=-4$ and $\beta_R^2=-8$. The vectors $(1,2,-1)$ and $(1,-1)$ in the simple roots are primitive, and a primitive integral vector proportional to a root has square $-2$; so none of the four is a multiple of a root and their mirrors are not mirrors of roots. The four hyperplanes cut the interior of the chamber, so $\mcf_{\mathrm{rc}}$ strictly refines $\mcf^{\mathrm{cox}}$ and (W) fails.

The proportionality is [@ABE22, Intro.]: "each curve $C_i$ specializes to a sum of the section $s$ and $d+1$ singular fibers", so $R\equiv n_d\bigl(s+\frac{d+1}{24}\sum_i f_i\bigr)$, "which is proportional to $s+m\sum_{i=1}^{24}f_i$".
:::

::: {.proposition #prop:recognizability-restricts title="Recognizability passes to a sub-moduli locus"}

Let $F_{S'}\subseteq F_S$ be a locus of $S'$-polarized K3 surfaces inside the moduli of $S$-polarized ones, and let $R$ be a recognizable divisor for $F_S$. Then the restriction of $R$ to $F_{S'}$ is a recognizable divisor for $F_{S'}$.
:::

::: {.proof}

A quasipolarized Kulikov degeneration whose generic fibre lies in $F_{S'}$ is a quasipolarized Kulikov degeneration whose generic fibre lies in $F_S$, and the divisor and the surfaces are the same objects in the two readings. So the flat limit that @def:recognizable-divisor supplies for $F_S$ is the one for $F_{S'}$, and its uniqueness up to $\Aut^0(\tilde{\mcx}_0)$ is the same statement. Nothing in the definition refers to the polarization lattice beyond fixing the surfaces.
:::

::: {.remark #rmk:recognizable-gap title="What @prop:semifan-coarsening-fails does not establish, and what does"}

The divisor of @prop:semifan-coarsening-fails is ABE22's polarizing divisor $s+m\sum_{i=1}^{24}f_i$, and [@ABE22, Intro.] relates it to the rational-curve divisor of $F_{2d}$ only up to proportionality: the source computes $R\equiv n_d\bigl(s+\frac{d+1}{24}\sum_i f_i\bigr)$ for the sum of the rational curves of $|L|$ and calls the result "proportional to $s+m\sum_{i=1}^{24}f_i$". That is a relation between divisor classes, and it does not identify the two stable-pair compactifications: the pairs are $(X,\eps R_{\rcop}|_F)$ and $(X,\eps(s+m\sum_i f_i))$, their divisors differ, and a KSBA compactification of pairs depends on the divisor and not on its class alone.

That divisor lives on the elliptic locus $F\subset F_2$ and not on $F_2$: it is built from a section and a fibre class, so it needs a surface whose Picard group contains $U\oplus\langle-2\rangle$, of rank $3$, while the very general degree-two K3 surface has Picard rank $1$. The question is therefore posed for $F$, which is the space [@ABE22] write $F$, and there the divisor is positive on both curve classes of that lattice, $D\cdot f=1$ and $D\cdot s=24m-2>0$ for $m\ge1$, so the candidate is a genuine polarizing divisor wherever the question can be asked (`computations/reports/coble_679-locus-probe-run.txt`).

The proportionality itself is weaker than the sentence suggests. All fibres of a morphism are algebraically equivalent, so the $24$ singular fibres satisfy $\sum_{i=1}^{24}f_i\equiv 24f$; with $L=s+(d+1)f$ and $d=1$, ABE22's divisor is $s+24mf$ and the rational-curve divisor has the class $n_1L=24s+48f$. The two are proportional only at $m=\frac{d+1}{24}=\frac1{12}$, which is not an integer, and at the integer $m=2$, where their degrees agree ($48=24\cdot2$), the classes $s+48f$ and $s+2f$ are not proportional (`computations/reports/coble_679-proportionality-run.txt`, reproduced by `tests/engineering/test_coble_a36_acceptance.py`).

The display has exactly one coefficient at which it is true, $(d+1)/24$, and at that coefficient ABE22's divisor is $s+(d+1)f$, which is the polarization $L$ itself; the divisor their theorem is about, $s+m\sum_i f_i$ with an integer $m\ge1$, is not proportional to $R_{\rcop}$'s class. So the sentence cannot be read as relating the two compactifications under either reading, and the body text's divisor, whose compactification [@ABE22, Intro., Thm. 1.2] computes, is not the rational-curve divisor's.

So @prop:semifan-coarsening-fails does not by itself exhibit a recognizable divisor with (W) failed. What does is a separate statement of [@AE23]. By [@AE23, Prop. 10.10, printed p. 36] the rational-curve divisor restricts on the unigonal locus to $n_d\bigl(s+\frac{d+1}{24}\sum_i f_i\bigr)$, and [@AE23, Thm. 10.16, printed p. 38] identifies the restriction of its semifan to the unigonal hyperplane with the fan of [@ABE22, §4C, printed p. 14]. The identification is not through proportionality: the caveat that [@ABE22]'s own computation of the divisor models assumes $m>\tfrac13$ is absorbed there by the observation that the stratum function has the same level sets, so the fan is the same ([@AE23, Thm. 10.16 with Thm. 9.3, printed pp. 30 and 38]). That is the identification @lem:rcop-refinement-criterion uses; the proportionality sentence alone would not supply it.
:::

::: {.remark #rmk:rcop-split-computation}

Before @lem:rcop-refinement-criterion, the question of @qst:recognizable-semifan was put to the library: the script `computations/reports/coble_679-rcop-split.py` and its transcript `computations/reports/coble_679-rcop-split-run.txt`, running on `sage-extensions`.

At the $0$-cusp of $F_2$, whose boundary lattice $U\oplus E_8(-1)^{\oplus2}\oplus A_1(-1)$ the script builds, it runs Vinberg's algorithm for the fundamental chamber and its walls. The walk does not finish within $900$ seconds there, nor within $1800$ (`computations/reports/coble_679-rcop-split-run-1800.txt` is the same script under that bound), nor within $2400$ with the walk alone and a bound of its own (`computations/reports/coble_679-rcop-chamber-run.txt`), nor within $1500$ with the controlling vector $e+f$ of square $2$, which lies on every wall carried by the $E_8(-1)^{\oplus2}\oplus A_1(-1)$ blocks (`computations/reports/coble_679-rcop-chamber-controlling-vector-run.txt`), so the library yields no wall set at that cusp. That is a fact about the walk and not about the literature: the chamber there is printed, and so is the inventory of its cones, in @thm:cone-inventory-printed. What a computation of the cones needs is the stable limit of $(X,\eps R_{\rcop})$ over a cone, and that is not an operation of the library — no module of `src/sage_extensions` names a stable pair, a Kulikov model or a semifan, and the transcript carries the two expressions that raise `AttributeError`.

At the elliptic cusp of @prop:semifan-coarsening-fails the script does complete. The chamber has $19$ walls, every one of square $-2$, $18$ of their $171$ pairs meeting and $153$ orthogonal: a tree on $19$ nodes, as the diagram of [@ABE22, Fig. 1, printed p. 12] is. The squares of $\alpha_j-\alpha_i$ over the simple pairs are $-4$ and $-6$, and those of $\alpha_c+2\alpha_b-\alpha_a$ over the triples the walk admits are $-12$: never $-2$, so none of these vectors is a root, which is the check on the walk's chamber. The two walls that decide (W) are the printed $\gamma_L^\perp$ and $\beta_L^\perp$ of [@ABE22, §4C, printed p. 14], of square $-4$ and $-8$, and their evaluation is the hand one of @prop:semifan-coarsening-fails. The $F_2$ cusp is now decided without the walk, by @lem:rcop-refinement-criterion; the walk would still be needed at the $0$-cusps of $F_{2d}$ for $d\ge2$ (@qst:recognizable-semifan).
:::

::: {.remark #rmk:missing-stable-limit}

The operation that would compute the semifan at a cusp to which no restriction theorem applies, stated so that the gap is a contract and not a description. Fix a $0$-cusp $\eta$ of $F_{2d}$, a cone $\sigma$ of $\mcf^{\mathrm{cox}}$, and the rational-curve divisor $R_{\rcop}$.

- **Input:** the boundary lattice $\bar T=\eta^\perp/\eta$ with its form, the cone $\sigma$ (equivalently a monodromy invariant $\lambda$ in its relative interior), and the polarized surface $(X,L)$.
- **Output:** the combinatorial type of the KSBA stable limit of the pair $(X,\eps R_{\rcop})$ — the dual graph of the central fibre with the genera of its components, the multiplicities with which the limit divisor meets them, and the contraction that defines the stable model. This is the value of the type function of @thm:semifan-stratum.
- **Parent:** the cone of the chamber, whose methods are in `src/sage_extensions/categories/polyhedral_cones.py`, with the Kulikov model and its integral-affine structure as the intermediate the construction runs through.

The absence of the operation, and the bounds of the chamber attempts, are guarded by `tests/engineering/test_coble_a36_acceptance.py`, which fails as soon as either record changes. The operation has a prerequisite that is also unmet: its input is a monodromy invariant read against the simple roots of the chamber, and the library's Vinberg walk on $U\oplus E_8(-1)^{\oplus2}\oplus A_1(-1)$ does not reach that chamber, so an implementation needs the chamber computed, or its pairings transcribed and checked and the vectors realized in the lattice, first — and bounding the search is not a way to get it: at `max_roots = 1` the rank-19 walk still does not finish in $120$ s, while the rank-18 control returns all eighteen roots in $63$--$66$ s under the same bounds (`computations/reports/coble_679-chamber-bound-probe-run.txt`); the component dictionary is not a further gap, since [@AET23, §7A, printed pp. 46--47] gives the polytope of every ADE shape outright. The obligation itself is stated where this repository states library obligations: `computations/lattice-interface-contract/specification/test_stable_limit_workflow_interfaces.py`, a `tdd_red` contract, run explicitly with `python3 -m pytest computations/lattice-interface-contract/specification -q -o addopts=""` since the repository's `testpaths` do not reach it, that fixes the input and output of the operation, requires its constancy on a semifan cone (AET23, Theorem 7.5, printed p. 48), and requires it to reproduce the one published degeneration, the eighteen components of $(\PP^2,L+C)$ of AET23, Example 7.4, printed p. 48.

The defining maps are those of [@AET23, Thm. 7.5, printed p. 48] and [@AE22, §§8--9, printed pp. 41--57], which produce that output for the ramification divisors, and of [@ABE22, §§7B and 7G, printed pp. 25 and 34], which produce it for the elliptic one. The library has none of the three: no module of `src/sage_extensions` names a stable pair, a Kulikov model or a semifan, and @rmk:rcop-split-computation records the two expressions that raise `AttributeError`.
:::

::: {.theorem #thm:cone-inventory-printed title="The cones of the Coxeter semifan at the $F_2$ cusp, from the printed diagram"}

Let $N=U\oplus E_8(-1)^{\oplus2}\oplus A_1(-1)$ be the boundary lattice of the $0$-cusp of $F_2$ and $\Gamma$ its Coxeter diagram, with vertex set the $24$ roots $r_0,\dots,r_{23}$. Then the cones of the Coxeter semifan $\mcf^{\mathrm{cox}}$ at that cusp are described as follows, all of it printed:

1. the faces of the fundamental chamber $\mathcal K$ correspond, order-reversing, to the elliptic and maximal parabolic subdiagrams $G\subseteq\Gamma$, by $F\mapsto\{i: F\subset r_i^\perp\}$ and $G\mapsto\bigcap_{i\in G}r_i^\perp$, the chamber itself corresponding to $G=\emptyset$;
2. the Type III cones meeting the interior of the positive cone and of dimension $d>0$ correspond to the elliptic subdiagrams of rank $r=19-d$, which are the disjoint unions of Dynkin diagrams $G_i$ of ADE type with $\sum_i|G_i|=r$;
3. the Type II rays $\RR_{\ge0}v$ with $v^2=0$ correspond to the maximal parabolic subdiagrams, the disjoint unions of affine Dynkin diagrams $\widehat G_i$ with $\sum_i|G_i|=17$;
4. modulo $W(N)$ the cones are in bijection with the faces of $\mathcal K$, and modulo $O^+(N)=S_3\ltimes W(N)$ with the elliptic and maximal parabolic subdiagrams modulo $S_3$; the maximal parabolic ones number $4$ modulo $S_3$, "illustrated on the right in Fig. 1".
:::

::: {.proof}

This is [@AET23, Definition 4.2, Theorem 4.3, Lemma 4.4 and Lemma 4.5, printed p. 22], with the diagram $\Gamma$ and the four maximal parabolic subdiagrams printed in [@AET23, Fig. 1, printed p. 22]: the subdiagrams drawn there are $A_{17}$, $A_{17}^-$, $D_{10}E_7$, $E_8^2A_1$ and $D_{16}A_1$, five names for the four classes of the lemma. Two checks on that list, both internal to this chapter: each name meets the vertex count of part (3) above, $17$, $10+7$, $8+8+1$ and $16+1$ vertices respectively; and the four classes are the root-lattice labels $A_{17}$, $D_{10}\oplus E_7$, $E_8^2\oplus A_1$ and $D_{16}\oplus A_1$ of the four $1$-cusp curves of this chapter's opening paragraph, which is what the correspondence between $1$-cusps and maximal parabolic subdiagrams gives. The same lattice appears in [@AE22, §10, printed p. 57] as $T=(19,1,1)\cong N$, and its Vinberg diagram is the one printed in the second panel of [@AE22, Fig. 4, printed p. 57], attributed there to Vinberg--Kaplinskaja and to Kondo; that attribution is quoted, and neither of the two papers is deposited among the sources of this repository, so neither is cited by its own pagination.

The reading for the issue: this is the whole cone inventory at the cusp where the library's walk does not terminate, obtained from the source at no computational cost, and it is the fan that the semifan of $R_{\rcop}$ is compared against in @lem:rcop-refinement-criterion. That comparison does not go through the diagram: by @lem:rcop-refinement-criterion there is no relevant set $J\subseteq V$ for $R_{\rcop}$ at this cusp, because the semifan does not coarsen the Coxeter fan there at all.
:::

::: {.remark #rmk:cone-inventory}

The step after the chamber — the inventory of the cones the semifan would coarsen — has been attempted once, at the one cusp where the chamber is computed at all. [@ABE22, Cor. 4.3, §4A, printed p. 13] prints the counts of this fan: "In $\mcf^{\mathrm{cox}}/W$ there are $2\cdot 9+1=19$ facets and $9^2+1=82$ rays. In $\mcf^{\mathrm{cox}}/\Gamma$ there are $9+1=10$ facets and $\frac{9\cdot 10}{2}+1=46$ rays."

The chamber the library computes has $19$ walls, which is the facet count. The orbit count it returns for the family of maximal parabolic subdiagrams with one affine component is $10$; the call's own definition is the orbit set of the diagram's automorphism group $\Aut G$ acting on that family, not of the reflection group $W$, so it is neither the $82$ nor the $46$ above and no cone count is asserted here. The enumeration of maximal elliptic subdiagrams did not finish in $600$ seconds, and the run was cut by its outer bound inside the next enumeration, the script's own alarm not interrupting it; the record ends there (`computations/reports/coble_679-elliptic-cone-inventory-run.txt`).
:::

::: {.corollary #cor:semifan-computed-cases title="(W), and the split, in the computed cases"}

Hypothesis (W) of @thm:semifan-recognizable-divisor holds, with the following $I$ and $J$, for the following divisors:

1. **The divisor $C_g$ of a two-elementary K3 surface, $g\ge2$, $S\ne(10,8,0)$.** The compactification computed in [@AE22] is that of the pairs $(X,\eps C_g)$, where $C_g$ is the component of genus $g\ge2$ of the fixed locus $X^\iota$, not the whole fixed locus [@AE22, Abstract, printed p. 1]. For the lattice $\bar T_1=(10+\bar k,10-\bar k,\bar\delta)$ the set $I$ is the $2\bar k$ vertices on the $I_{2\bar k}$ cycle and $J$ every other vertex, "in particular all the black vertices"; for a lattice $\bar T_{\bar g}$ reached by a chain of mirror moves, $I$ consists of the vertices inherited from $\Gamma(\bar T_1)$ and $J$ of the rest [@AE22, Def. 9.5, printed p. 54]. (W) is [@AE22, Def. 9.5, printed p. 54] with [@AE22, Thm. 9.10, printed p. 56], which dominates $\overline F_S^{\mcf_{R,\eta}}$ by the semitoroidal compactifications for the Coxeter semifans of $W_2$ and of $W_r$.
2. **The ramification divisor of a degree-two K3 surface.** $I=\{0,\dots,17\}$ and $J=\{18,\dots,23\}$ for the twenty-four roots of $\bar T=H\oplus E_8^2\oplus A_1$ [@AET23, printed p. 27]. (W) is [@AET23, Thm. 1.2, printed p. 3], "the Coxeter fan refines this semifan", and the identification of the semifan with the normalized compactification is [@AET23, Thm. 8.2, printed p. 50].
3. **The ramification divisor of a degree-two Enriques surface.** A folded root lies in $J$ exactly when it is the folding of a root off the boundary of the square, resp. the triangle [@AEGS25, Def. 5.4 and Lemma 5.5, printed p. 611]. (W) and the identification are [@AEGS25, Thm. 5.9, printed p. 611], whose proof excludes a strict coarsening of the collection on the ground that it would merge a codimension-one cone carrying a one-parameter family of non-maximal pairs [@AEGS25, printed p. 612].
:::

::: {.proof}

In each case the cited statement identifies the semitoroidal compactification for the displayed semifan with the normalization of the stable-pair compactification, and exhibits it as a coarsening of the Coxeter fan with the displayed split: (1) [@AE22, Def. 9.5, printed p. 54] with [@AE22, Thm. 9.10, printed p. 56]; (2) [@AET23, §4D, printed p. 27] with [@AET23, Thm. 8.2, printed p. 50]; (3) [@AEGS25, Lemma 5.5 and Thm. 5.9, printed p. 611]. Each source also supplies the family and not only the comparison of fans, so (W) is decided there in the form of @prop:semifan-coarsening-extension: in (2) it is the sentence of the abstract of [@AET23], "the universal family of polarized K3 surfaces of degree 2 can be extended to a flat family of stable KSBA pairs $(X,\eps R)$ over the toroidal compactification associated to the Coxeter fan"; in (1) the domination of $\overline F_S^{\mcf_{R,\eta}}$ by the Coxeter compactifications in [@AE22, Thm. 9.10, printed p. 56]; in (3) the family over the compactified moduli stack constructed in the proof of [@AEGS25, Thm. 5.9, printed p. 612]. The second clause of (W) is the root-level declaration of relevance in each of the three definitions: the cones of each semifan are unions of Coxeter chambers, and the chambers are merged exactly across the mirrors of the irrelevant roots. Where a source states its diagram for the $(-2)$-roots alone, its coarsening is a coarsening of the full diagram too: no semifan that coarsens the $(-2)$-fan has a wall along the mirror of a long root, since such a wall would be a union of $(-2)$-facets lying in one hyperplane, and that hyperplane is then a $(-2)$-mirror.
:::

::: {.remark #rmk:semifan-not-a-fan}

The fan criterion of @thm:semifan-recognizable-divisor(4) is the joint one of [@AE22, Rem. 9.11, printed p. 57]: a semifan of this form is a fan when $W$ has finite covolume and the irrelevant roots span an elliptic subdiagram, and the first of the two is recorded there as holding "in rather few cases" among the two-elementary cusps. At $\fentwo$ the semifans are fans at the $0$-cusps $2$ and $4$ and not at $1$, $3$ and $5$, the irrelevant subgroups being infinite at the last three [@AEGS25, Lemma 5.6, printed p. 611]. So a semifan is not in general a fan, and no description of $\mcf_R$ as the coarsest fan above $\{C^+\}$ can exist.
:::

::: {.example #ex:elliptic-k3-divisor-fans title="Two polarizing divisors on elliptic K3 surfaces"}

Let $F$ parameterize elliptic K3 surfaces with section $s$ and singular fibers $f_1,\ldots,f_{24}$, counted with multiplicity. For the polarizing divisor $R=s+m\sum_i f_i$ with $m\ge1$, the normalization of the stable-pair compactification is toroidal. Its fan subdivides each Coxeter chamber into nine chambers, so it refines the Coxeter fan [@ABE22, Intro., Thm. 1.2]. For the image of the trisection of nonzero $2$-torsion points after contracting the section, the normalization is toroidal for a fan whose chamber is the union of four Coxeter chambers [@ABE22, Intro., Thm. 1.1 and §3]. Thus these two geometric divisors give opposite directions of comparison with the same Coxeter fan.
:::

::: {.remark #rmk:two-questions-are-one}

The inventory of what is *known* to be recognizable is what made the two questions of @qst:recognizable-semifan one question about a single computation. In the deposits only two classes of polarizing divisor carry a recognizability proof: the ramification divisor of a nonsymplectic involution, in its fixed-locus form [@AE22, §8A, printed p. 41; @AEH24, Thm. 3.24] and in its Enriques form [@AEGS25, Thm. 5.9, printed p. 611], and the rational-curve divisor $R_{\rcop}$ on $F_{2d}$ [@AE23, witnessed by @AE23a] (`computations/reports/coble_679-recognizability-inventory-run.txt`).

For the first class (W) is decided at every $0$-cusp of every one of the fifty two-elementary lattices with $g\ge2$, and it holds: [@AE22, Thm. 9.10, printed p. 56] identifies the normalization with the semitoroidal compactification for the collection of semifans $\mcf_{\rm ram}(T)$ of [@AE22, Def. 9.5, printed p. 54], one for each $0$-cusp, and each of those is a coarsening of the Coxeter fan by construction. In the remaining twenty-five two-elementary lattices the fixed locus has no component of genus $g\ge2$, and its components have negative square, so it is not an ample divisor and no stable pair is formed from it; there the first class supplies no divisor at all.

For the second class the answer is now known at $d=1$: by @lem:rcop-refinement-criterion hypothesis (W) fails for $R_{\rcop}$ at the unique $0$-cusp of $F_2$, so $R_{\rcop}$ is a recognizable divisor whose semifan does not coarsen the Coxeter semifan, and no split $I\sqcup J$ exists at that cusp. What remains of the computation is the cones of $\mcf_{R_{\rcop}}$ at the $0$-cusps of $F_{2d}$ for $d\ge2$ (@qst:recognizable-semifan).
:::

::: {.lemma #lem:rcop-refinement-criterion title="The rational-curve divisor does not coarsen the Coxeter semifan at the $F_2$ cusp"}

Let $d=1$ and let $\eta$ be the unique $0$-cusp of $F_2$, with boundary lattice $U\oplus E_8(-1)^{\oplus 2}\oplus A_1(-1)$, Coxeter diagram $\Gamma$ of twenty-four roots and cone inventory as printed in @thm:cone-inventory-printed. Then the rational-curve divisor $R_{\rcop}$ has a cone of $\mcf_{R_{\rcop},\eta}$ that is not a union of cones of $\mcf^{\mathrm{cox}}$, and consequently the universal family of stable pairs $(X,\eps R_{\rcop})$ does not extend over the toroidal compactification $\overline F_2^{\mcf^{\mathrm{cox}}}$ (@prop:semifan-coarsening-extension).
:::

::: {.proof}

*The cusp and the unigonal hyperplane.* A quasipolarized K3 surface of degree $2d$ is unigonal when it is elliptic with $L=s+(d+1)f$ [@AE23, Def. 10.9, printed p. 36], and on a unigonal surface the rational-curve divisor is $R_{\rcop}=n_d\bigl(s+\frac{d+1}{24}\sum_{i=1}^{24}f_i\bigr)$ [@AE23, Prop. 10.10, printed p. 36]. The $0$-cusps of $F_{2d}$ number $\lfloor (N+2)/2\rfloor$, where $d=N^2d_0$ with $d_0$ squarefree [@AE23, §10C, printed p. 37]; for $d=1$ there is exactly one, and its invariant is $\delta^*=2qNd_0=0$ with $q\in\ZZ/N\ZZ$, which for $N=1$ forces $q=0$, that is $p_*(\delta)=1$. Its boundary lattice is $\delta^\perp/\delta\cong\langle-2\rangle\oplus U\oplus E_8(-1)^{\oplus2}=N$ [@AE23, §10C, printed p. 38], with $H=U$ the hyperbolic plane and $E_8$ carrying the negative definite form of the K3 lattice; at $d=1$ the cusp has $p_*(\delta)=1$, the case in which the printed first summand $\langle-2d/p_*(\delta)\rangle$ is $\langle-2\rangle$ (@lem:cusp-lattice-p-greater-one). Write $t$ for a generator of the $A_1(-1)$ summand, so that $N=\langle t\rangle\oplus U\oplus E_8(-1)^{\oplus2}$, $t^2=-2$ and $t^\perp=U\oplus E_8(-1)^{\oplus2}$: this is the unigonal hyperplane $\langle-2d\rangle^\perp$ of [@AE23, Thm. 10.16, printed p. 38] at $d=1$.

*The cone of the semifan.* Let $\mcf_{R_{\rcop},\eta}=\mcf^{\mathrm{rc}}_\delta$ be the semifan of [@AE23, Def. 10.15, printed p. 38]. By [@AE23, Thm. 10.16, printed p. 38] the restriction of $\mcf_{R_{\rcop},\eta}$ to $t^\perp$ is a fan and $\langle-2d\rangle^\perp\cap C_\delta^+$ is a union of cones of $\mcf^{\mathrm{rc}}_\delta$; the proof of the theorem identifies that restriction with the fan of [@ABE22, §4C, printed p. 14] and shows that each of its maximal cones is itself a cone of $\mcf^{\mathrm{rc}}_\delta$, not only a slice of a $19$-dimensional cone. By [@ABE22, §4C, printed p. 14] that fan subdivides the Coxeter chamber $P\subset t^\perp$ by the hyperplanes $\beta_L^\perp,\gamma_L^\perp,\beta_R^\perp,\gamma_R^\perp$ into nine cones $\sigma_{LR}$, and $\sigma_{22}$ has facets on $\gamma_L^\perp$ and on $\beta_L^\perp$ that meet the interior of $P$. Put $h_\gamma=\sigma_{22}\cap\gamma_L^\perp$ and $h_\beta=\sigma_{22}\cap\beta_L^\perp$; both are $17$-dimensional cones in $t^\perp$.

*The cutting vectors are primitive.* In [@ABE22, §4C, printed p. 14],
$$\beta_L=\alpha_3+2\alpha_2-\alpha_1,\qquad \gamma_L=\alpha_3-\alpha_1,$$
and in the diagram of [@ABE22, Fig. 1, printed p. 12] the vertex $\alpha_1$ is pendant at $\alpha_4$ and $\alpha_2,\dots,\alpha_{18}$ is a chain, so that $\alpha_1\cdot\alpha_2=\alpha_1\cdot\alpha_3=0$ and $\alpha_2\cdot\alpha_3=1$. Hence
$$\beta_L\cdot\alpha_1=2,\qquad \beta_L\cdot\alpha_2=-3,\qquad \gamma_L\cdot\alpha_2=1,\qquad \beta_L^2=-8,\qquad \gamma_L^2=-4,$$
the three values $\beta_L\cdot\alpha_1=2$, $\beta_L^2=-8$ and $\gamma_L^2=-4$ being printed in [@ABE22, §4C, printed p. 14]. A vector pairing to $1$ with a vector of the lattice is primitive, and so is one whose pairings with $\alpha_1$ and $\alpha_2$ have gcd $1$; hence $\gamma_L$ and $\beta_L$ are primitive in $U\oplus E_8(-1)^{\oplus2}$.

*Neither facet is a mirror trace.* The walls of $\mcf^{\mathrm{cox}}$ are the mirrors of the vectors of square $-2$ [@AET23, Def. 4.1, printed p. 21], and the twenty-four simple roots of the diagram are such vectors [@AET23, §5C, printed p. 29; Fig. 1, printed p. 22]. Let $r\in N$ be one with $h_\gamma\subset r^\perp$. The span of $h_\gamma$ is $\gamma_L^\perp\cap t^\perp$, so $r$ lies in its orthogonal complement, $\operatorname{span}(t,\gamma_L)$: write $r=at+k\gamma_L$, with $a\in\ZZ$ and $k\in\ZZ$, the latter because $\gamma_L$ is primitive. Then
$$-2=r^2=-2a^2+k^2\gamma_L^2=-2a^2-4k^2,$$
so $a^2+2k^2=1$ and $k=0$: the only root whose mirror contains $h_\gamma$ is $r=\pm t$, that is the mirror $t^\perp$ itself. The same computation with $\beta_L$, whose square is $-8$, gives $a^2+4k^2=1$ and again $k=0$. So neither $h_\gamma$ nor $h_\beta$ is contained in the mirror of a root other than $t^\perp$.

A vector of square $-4$ does not cut the fan, and such vectors do exist: $\gamma_L$ itself has $\gamma_L^2=-4$, so the mirror $\gamma_L^\perp$ contains $h_\gamma$ and is not a wall of $\mcf^{\mathrm{cox}}$ [@AET23, Def. 4.1, printed p. 21]. What the computation above excludes is exactly the walls: no $(-2)$-vector other than $\pm t$ has its mirror through $h_\gamma$ or $h_\beta$.

*A union of Coxeter cones cannot have $h_\gamma$ as a facet.* Suppose that $\sigma_{22}$ were a union of cones of $\mcf^{\mathrm{cox}}_\eta$. The mirrors of $\mcf^{\mathrm{cox}}_\eta$ are locally finite and $h_\gamma$ is contained in none of them other than $t^\perp$, so a relative interior point $x$ of $h_\gamma$ that lies in the interior of $P$ lies on no mirror other than $t^\perp$. The cone of $\mcf^{\mathrm{cox}}_\eta$ whose relative interior contains $x$ is then the facet $F$ of a chamber along $t^\perp$, and $F$ is $18$-dimensional. Since $x\in\sigma_{22}$, the cone of the fan whose relative interior contains $x$ is contained in $\sigma_{22}$, so $F\subset\sigma_{22}$. But $F$ and $\sigma_{22}$ are both $18$-dimensional, so $x$ is a relative interior point of $\sigma_{22}$, whereas it lies in the facet $h_\gamma$ of $\sigma_{22}$. This is a contradiction.

So $\sigma_{22}$ is a cone of $\mcf_{R_{\rcop},\eta}$ that is not a union of cones of $\mcf^{\mathrm{cox}}_\eta$: the coarsening clause of (W) fails for $R_{\rcop}$ at $\eta$. By @prop:semifan-coarsening-extension the universal family of stable pairs $(X,\eps R_{\rcop})$ does not extend over $\overline F_2^{\mcf^{\mathrm{cox}}}$.
:::

::: {.lemma #lem:cusp-lattice-p-greater-one title="The boundary lattice at every cusp with $p_*>1$"}

Let $\eta$ be a $0$-cusp of $F_{2d}$ with $p_*(\delta_\eta)=p>1$. Write $d=N^2d_0$ with $d_0$ squarefree, let $h=\gcd(q,N)$ for the class $\{\pm q\}$ of $\eta$, put $p=N/h$ and $a=q/h$, and set $k=d/p^2=d_0h^2$. Let $g$ generate the $\langle-2d\rangle$ summand of $L_{2d}$ and let $e_1,f_1$ be the basis of the first hyperbolic plane. Then the vector
$$\delta=a g+p e_1+p d_0q^2f_1$$
is a primitive isotropic representative of $\eta$, and
$$\delta^\perp/\delta\cong\langle-2d/p_*^2\rangle\oplus U\oplus E_8(-1)^{\oplus2}=\langle-2k\rangle\oplus U\oplus E_8(-1)^{\oplus2},$$
of rank $19$ and discriminant $2k$. At $k=1$ this is the boundary lattice of the $F_2$ cusp, whose Coxeter semifan is the one printed there [@AET23, Def. 4.1 and Fig. 1, printed pp. 21--22]; for $k\ge2$ it is the boundary lattice of the unigonal cusp of $F_{2k}$, whose Coxeter diagram is not printed in the sources read here. The formula printed in [@AE23, §10C, printed p. 38] gives $\langle-2d/p_*(\delta)\rangle=\langle-2pk\rangle$ here, of discriminant $2pk$, so at $p_*>1$ the printed first summand is not the one these cusps have; at $p_*=1$ the two readings agree, and that is the case the proof of @lem:rcop-refinement-criterion uses.
:::

::: {.proof}

Write $x=A g+be_1+cf_1+W$ with $W\in H(e_2,f_2)\oplus E_8^{\oplus2}$. Then $x\cdot\delta=-2daA+p(c+d_0q^2b)$, so $x\in\delta^\perp$ exactly when $c+d_0q^2b=2pkaA$. The solutions are spanned by $u=e_1-d_0q^2f_1$ and $v=g+2pkaf_1$, together with $H(e_2,f_2)\oplus E_8^{\oplus2}$: $\delta^\perp=\langle u,v\rangle\oplus H(e_2,f_2)\oplus E_8^{\oplus2}$, of rank $2+2+16=20$. One has $\delta=av+pu$, $u^2=-2d_0q^2=-2ka^2$, $v^2=-2p^2k=-2d$ and $u\cdot v=2pka$. Choose integers $r,s$ with $as-pr=1$; then $\delta$ and $z=rv+su$ form a basis of $\langle u,v\rangle$, so $z$ generates $\langle u,v\rangle/\ZZ\delta$, and $z^2=-2dr^2+4pkars-2d_0q^2s^2=-2k(pr-as)^2=-2k$, where $ka^2=d_0q^2$. So $\delta^\perp/\delta$ is generated by $z$, the second hyperbolic plane and $E_8^{\oplus2}$, with $z^2=-2k$: it is $\langle-2k\rangle\oplus U\oplus E_8(-1)^{\oplus2}$, of discriminant $2k$. The printed first summand is $\langle-2pk\rangle$, of discriminant $2pk$.
:::

::: {.lemma #lem:generalized-unigonal-hyperplane title="The generalized unigonal class at every cusp with $p_*>1$"}

Let $\eta$ be a $0$-cusp of $F_{2d}$ with $p_*(\delta)=p>1$, with $d=N^2d_0$, $h=\gcd(q,N)$, $p=N/h$, $a=q/h$ and $k=d/p^2=d_0h^2$ as in @lem:cusp-lattice-p-greater-one, and put $u=e_1-d_0q^2f_1$. Then $u\in\delta^\perp$ and, in $\bar T=\delta^\perp/\delta=\langle-2k\rangle\oplus U\oplus E_8(-1)^{\oplus2}$ with $z$ the generator of the first summand constructed in the proof of @lem:cusp-lattice-p-greater-one, the class of $u$ is
$$\bar u=az.$$
Consequently $u^\perp$ in $\bar T$ is $z^\perp=U(e_2,f_2)\oplus E_8(-1)^{\oplus2}$, which is unimodular of rank $18$ and signature $(1,17)$ at every such cusp, and the vectors of $\bar T$ with that mirror are exactly the multiples $cz$: the hyperplane is the mirror of a $(-2)$-vector exactly when $k=1$, and of a $(-2)$- or $(-4)$-vector exactly when $k\in\{1,2\}$.
:::

::: {.proof}

One has $u\cdot\delta=p(e_1\cdot e_1)+pd_0q^2(e_1\cdot f_1)-pd_0q^2(f_1\cdot e_1)-pd_0^2q^4(f_1\cdot f_1)=pd_0q^2-pd_0q^2=0$, so $u\in\delta^\perp$. In the notation of the cited proof, $\delta=av+pu$ and $z=rv+su$ with $as-pr=1$, hence $az-r\delta=arv+asu-arv-rpu=(as-pr)u=u$, and since $z$ generates $\langle u,v\rangle/\ZZ\delta$ the class of $u$ in $\bar T$ is $az$. As $\delta^\perp=\langle u,v\rangle\oplus H(e_2,f_2)\oplus E_8^{\oplus2}$ and $z\in\langle u,v\rangle$, the orthogonal complement of $z$ in $\bar T$ contains $U(e_2,f_2)\oplus E_8(-1)^{\oplus2}$ and has rank $18=\operatorname{rank}\bar T-1$, so it equals it, and $z$ being primitive the sum $\langle z\rangle\oplus z^\perp=\bar T$ is orthogonal. A vector $v\in\bar T$ has $v^\perp=z^\perp$ exactly when $v\in(z^\perp)^\perp=\ZZ z$, that is $v=cz$, and then $v^2=-2kc^2$. This lies in $\{-2,-4\}$ exactly when $kc^2\in\{1,2\}$, and equals $-2$ exactly when $k=1$ with $c=\pm1$.
:::

::: {.lemma #lem:generalized-unigonal-constraint title="What (W) forces on the generalized unigonal hyperplane"}

Let $\eta$ be a $0$-cusp of $F_{2d}$ with $p_*(\delta)=p>1$ and $k=d/p^2$, and let $z$ be the generator of the $\langle-2k\rangle$ summand of $\bar T$ of @lem:generalized-unigonal-hyperplane, so that $z^\perp=U(e_2,f_2)\oplus E_8(-1)^{\oplus2}$. Assume
$$(\mathrm H_p)\qquad z^\perp\cap C^+\ \text{is a union of cones of }\ \mcf_{R_{\rcop},\eta},$$
the $p>1$ analogue of the last sentence of [@AE23, Thm. 10.16, printed p. 38], which is printed at $p_*=1$ only. If $k\notin\{1,2\}$ then (W) fails at $\eta$. Equivalently, under (W) the hyperplane $z^\perp$ meets $C^+$ in a set that is not a union of cones of $\mcf_{R_{\rcop},\eta}$.
:::

::: {.proof}

One has $z^2=-2k<0$, so $z^\perp$ has signature $(1,17)$ and $z^\perp\cap C^+$ is a nonempty open subset of it. By $(\mathrm H_p)$ that set is a locally finite union of closed convex cones of $\mcf_{R_{\rcop},\eta}$, each of them contained in the closure of $C^+$ and hence, being contained in $z^\perp$, of dimension at most $18$. A cone of dimension at most $17$ has empty interior in $z^\perp$, and a locally finite union of closed sets with empty interior has empty interior, so one of the cones has dimension $18$ and spans $z^\perp$. By @lem:generalized-unigonal-hyperplane the vectors of $\bar T$ whose mirror is $z^\perp$ are the multiples $cz$, of square $-2kc^2$, and $-2kc^2\in\{-2,-4\}$ requires $k\in\{1,2\}$ because $c^2\ge1$. So for $k\notin\{1,2\}$ the span $z^\perp$ is not the mirror of a vector of $\bar T$ of square $-2$ or $-4$, and @lem:wall-criterion gives the failure of (W).
:::

::: {.lemma #lem:cusp-census title="The census of $0$-cusps by $(p,a,k)$"}

Let $d=N^2d_0$ with $d_0$ squarefree, and let $\eta$ be the $0$-cusp of $F_{2d}$ of class $\{\pm q\}$, $q\in\ZZ/N\ZZ$, with $h=\gcd(q,N)$, $p=N/h$, $a=q/h$ and $k=d/p^2=d_0h^2$ as in @lem:cusp-lattice-p-greater-one. Then:
1. $p=1$ exactly for the classes with $q\equiv0\pmod N$, that is for the single class $\{0\}$; every other $0$-cusp of $F_{2d}$ has $p_*>1$. So $F_{2d}$ has $\lfloor(N+2)/2\rfloor-1$ cusps with $p_*>1$, its $\lfloor(N+2)/2\rfloor$ cusps being the classes $\{\pm q\}$ [@AE23, §10C, printed p. 37].
2. At a cusp with $p_*>1$ one has $k=d_0h^2$, so $d_0h^2\in\{1,2\}$ exactly when $(d_0,h)\in\{(1,1),(2,1)\}$: the cusps with $k\in\{1,2\}$ are exactly those of $F_{N^2}$ and of $F_{2N^2}$ whose class $\{\pm q\}$ has $\gcd(q,N)=1$, and there $k=1$ and $k=2$ respectively.
3. Consequently, if $d$ is neither a square nor twice a square, then every $0$-cusp of $F_{2d}$ with $p_*>1$ has $k\notin\{1,2\}$, and at each of them (W) forces $(\mathrm H_p)$ of @lem:generalized-unigonal-constraint to fail.
:::

::: {.proof}

$h=\gcd(q,N)$ divides $N$, so $p=N/h=1$ exactly when $h=N$, that is when $N$ divides $q$; and $k=d/p^2=N^2d_0h^2/N^2=d_0h^2$. As $d_0\ge1$ is squarefree and $h\ge1$, the product $d_0h^2$ is $1$ only for $(d_0,h)=(1,1)$ and $2$ only for $(d_0,h)=(2,1)$. The condition $h=1$ is $\gcd(q,N)=1$, and $d_0=1$, resp. $d_0=2$, is $d=N^2$, resp. $d=2N^2$. Assertion 3 is assertion 2 with the contrapositive of @lem:generalized-unigonal-constraint.
:::

::: {.lemma #lem:k-one-two-sharp title="The cusps with $k\in\{1,2\}$ are where neither criterion fires"}

Let $\eta$ be a $0$-cusp of $F_{2d}$ with $p_*(\delta)=p>1$ and $k=d/p^2\in\{1,2\}$, so that $d=N^2$ or $d=2N^2$ with $N\ge2$ and the class $\{\pm q\}$ of $\eta$ is a unit modulo $N$ (@lem:cusp-census), and let $z$ generate the $\langle-2k\rangle$ summand of $\bar T$ as in @lem:generalized-unigonal-hyperplane. Then $z^2=-2$ at $k=1$ and $z^2=-4$ at $k=2$, so $z^\perp$ **is** the mirror of a vector of $\bar T$ of square $-2$, respectively $-4$: the wall criterion @lem:wall-criterion does not refute (W) at $\eta$, and the generalized-unigonal constraint @lem:generalized-unigonal-constraint is silent there. At $k=1$ the boundary lattice is the lattice of the $F_2$ cusp, whose Coxeter fan is the printed one of twenty-four $(-2)$-roots [@AET23, Def. 4.1 and Fig. 1, printed pp. 21--22], so at those cusps (W) is a well-posed question about a printed fan; no printed source records a cone of $\mcf_{R_{\rcop},\eta}$ at them, so it is not decided.
:::

::: {.proof}

By @lem:cusp-census the cusps with $p_*>1$ and $k\in\{1,2\}$ are those with $d_0\in\{1,2\}$ and $h=1$, that is $d=N^2$ or $d=2N^2$ with $\gcd(q,N)=1$; $q\equiv0\pmod N$ would give $p=1$, so $N\ge2$. There $z^2=-2k$ is $-2$ or $-4$, so $z^\perp$ is the mirror of $z$ itself, a vector of square $-2$ or $-4$, and the hypothesis of @lem:wall-criterion fails; the hypothesis $(\mathrm H_p)$ of @lem:generalized-unigonal-constraint is not needed because its conclusion needs $k\notin\{1,2\}$. At $k=1$ the boundary lattice is $\langle-2\rangle\oplus U\oplus E_8(-1)^{\oplus2}$, the lattice of the $F_2$ cusp (@lem:cusp-lattice-p-greater-one), whose Coxeter fan is cut by the twenty-four $(-2)$-roots of [@AET23, Def. 4.1, printed p. 21].
:::

::: {.lemma #lem:k-greater-one-fan-not-prism title="The comparison fan at the $k\ge2$ cusps is not a prism"}

Let $k\ge1$, $N_k=\langle-2k\rangle\oplus U\oplus E_8(-1)^{\oplus2}$ with $g$ a generator of the first summand, $e,f$ the standard basis of $U$, and $C\subset U\oplus E_8(-1)^{\oplus2}$ the fundamental chamber of its root system. Then $r=g+(k-1)e+f$ is a $(-2)$-root of $N_k$, and its mirror $r^\perp$ meets the interior of $\RR g\times C$ while being neither $\RR g$ nor the preimage of a wall of $C$ under the projection $\RR g\times(U\oplus E_8^{\oplus2})\to U\oplus E_8^{\oplus2}$. Hence the Coxeter chamber of $N_k$ is strictly contained in a translate of $\RR g\times C$. For $k\ge2$ the lattice $N_k$ is not $N_1$ (their discriminants are $2k$ and $2$), and its comparison fan is not the product of the printed $F_2$ fan with a line: it cannot be read off the $24$-root diagram.
:::

::: {.proof}

$r^2=-2k+((k-1)e+f)^2=-2k+2(k-1)=-2$, and $r\cdot g=-2k\ne0$, so $r^\perp$ contains no line in the $g$-direction and is neither $\RR g$ nor the preimage of a hyperplane of $U\oplus E_8(-1)^{\oplus2}$. For $u$ in the interior of $C$ put $x=\frac{((k-1)e+f)\cdot u}{2k}\,g+u$; then $x$ lies in the interior of $\RR g\times C$ and $r\cdot x=-2k\cdot\frac{((k-1)e+f)\cdot u}{2k}+((k-1)e+f)\cdot u=0$, so $r^\perp$ cuts that interior. The roots of $N_k$ with zero $g$-coordinate are exactly the roots of $U\oplus E_8(-1)^{\oplus2}$, so the chamber of $N_k$ lies in a chamber of that subgroup, a translate of $\RR g\times C$, and the mixed wall shows it is strictly smaller. At $k\ge2$, $N_k$ is not isometric to $N_1$, so its fan is not the printed one, and the mixed wall shows that it is not the printed one times a line either.
:::

::: {.lemma #lem:k-not-two-reflective title="The reflective dichotomy for $N_k$"}

For $k\ge1$ put $N_k=\langle-2k\rangle\oplus U\oplus E_8(-1)^{\oplus2}$. Then $N_k$ is two-reflective in the sense of @def:reflective-lattice if and only if $k=1$: the group $W_2(N_k)$ generated by the vectors of square $-2$ has finite index in $\Orth(N_k)$ exactly for $k=1$ [@Nik79b, Prop. 0.2.1, printed p. 1402, and the equivalence on p. 1404; @AET23, §4A, printed p. 21]. Consequently, at a $0$-cusp of $F_{2d}$ with invariants $p_*(\delta)$ and $k=d/p_*^2$, the boundary lattice is two-reflective exactly when $k=1$, that is $p_*(\delta)=\sqrt d$, that is $d=N^2$ with $\gcd(q,N)=1$; in particular the unigonal cusp of $F_{2d}$ has a two-reflective boundary lattice only for $d=1$, and when $d$ is not a perfect square no cusp of $F_{2d}$ has one. At $k=1$ the reflection group is the one of the printed $24$-root diagram [@AET23, Def. 4.1 and Fig. 1, printed pp. 21--22]; for $k\ge2$ it has infinite covolume, so the comparison is against a semifan and not a fan [@AET23, Def. 3.5, printed p. 10], and at the unigonal cusp of $F_{2d}$ with $d\ge2$ the reflection group that enters the printed proof of [@AE23, Thm. 10.16, printed pp. 38--39] is that of the hyperplane $\langle-2d\rangle^\perp\cong II_{1,17}$, not that of the $19$-dimensional lattice.
:::

::: {.proof}

For $k=1$, $N_1=U\oplus(E_8(-1)^{\oplus2}\oplus A_1)$ and $W(N_1)$ has finite index in $\Orth^+(N_1)$ with quotient $S_3$ [@AET23, §4A, printed p. 21]; it is also the exception of [@Nik79b, Thm. 0.2.2, printed p. 1403]. For $k\ge2$, write $N_k=U\oplus K_0$ with $K_0=\langle-2k\rangle\oplus E_8(-1)^{\oplus2}$, negative definite of rank $17$. A vector $v=au+\beta$ of $K_0$ has square $-2ka^2-2|\beta|^2$, so $v^2=-2$ forces $ka^2+|\beta|^2=1$ and hence $a=0$: the $(-2)$-vectors of $K_0$ are its $E_8(-1)^{\oplus2}$ roots and span rank $16<17$. If $N_k$ were two-reflective, [@Nik79b, Prop. 0.2.1, printed p. 1402] would put $N_k$ in $\mathcal F_U$, and the equivalence printed on [@Nik79b, p. 1404] would make the genus of $K_0$ generated by its $(-2)$-vectors up to finite index; it is not. So $N_k$ is not two-reflective for $k\ge2$. The cusp consequence is @lem:cusp-lattice-p-greater-one with $k=d/p_*^2$: $k=1$ exactly when $d=p_*^2$, that is $d=N^2$ and $\gcd(q,N)=1$. The last clause is the proof of [@AE23, Thm. 10.16, printed pp. 38--39], whose restriction is to $\langle-2d\rangle^\perp=II_{1,17}$.
:::

::: {.lemma #lem:minus-two-reflections-lift title="Every $(-2)$-reflection of the boundary lattice is in the monodromy"}

Let $L$ be an even lattice, $\delta\in L$ primitive isotropic, $N=\delta^\perp/\delta$, and let $x\in N$ with $x^2=-2$. Then every lift $\tilde x\in\delta^\perp$ of $x$ has $\tilde x^2=-2$, and $s_{\tilde x}\colon y\mapsto y-\frac{2(y,\tilde x)}{(\tilde x,\tilde x)}\tilde x$ is an integral isometry of $L$ that fixes $\delta$, induces $s_x$ on $N$, and acts trivially on $A_L=L^*/L$. Consequently, at a $0$-cusp $\eta$ of $F_{2d}$ with boundary lattice $\bar T=\delta^\perp/\delta$, the semifan $\mcf_{R_{\rcop},\eta}$ is invariant under $W_2(\bar T)$, the group generated by the reflections in all $(-2)$-vectors of $\bar T$.
:::

::: {.proof}

Two lifts differ by $t\delta$, and $(\tilde x+t\delta)^2=\tilde x^2+2t(\tilde x\cdot\delta)+t^2\delta^2=\tilde x^2$ because $\tilde x\in\delta^\perp$ and $\delta^2=0$; the form on $N$ is induced from $\delta^\perp$, so $\tilde x^2=x^2=-2$. For $y\in L$ the product $y\cdot\tilde x$ is an integer, $L$ being even, so $s_{\tilde x}(y)=y+(y\cdot\tilde x)\tilde x$ lies in $L$; further $s_{\tilde x}(\delta)=\delta+(\delta\cdot\tilde x)\tilde x=\delta$, and $s_{\tilde x}$ is the reflection in the line spanned by $\tilde x$, so it induces the reflection $s_x$ on $N$. For $v\in L^*$ one has $v\cdot\tilde x\in\ZZ$, so $s_{\tilde x}(v)-v=(v\cdot\tilde x)\tilde x\in L$, that is, $s_{\tilde x}$ acts trivially on $A_L=L^*/L$. So $s_{\tilde x}$ lies in the group of changes of marking $\Gamma$ of [@AE23, Cor. 2.9, printed p. 5], which for the degree-$2d$ problem is the isometry group of $L_{2d}$, and it fixes the cusp $\ZZ\delta$; by the invariance of a semifan under the stabilizer of its cusp [@AE23, Def. 5.9 and Def. 5.11, printed pp. 13--14] the semifan $\mcf_{R_{\rcop},\eta}$ is invariant under $s_{\tilde x}$. Letting $x$ run over the $(-2)$-vectors of $\bar T=\delta^\perp/\delta$, the semifan is invariant under $W_2(\bar T)$.
:::

::: {.lemma #lem:wall-criterion title="A necessary condition for (W) at any $0$-cusp"}

Let $\eta$ be a $0$-cusp of $F_{2d}$ with boundary lattice $\bar T=\delta^\perp/\delta$, and let $\sigma$ be an $18$-dimensional cone of $\mcf_{R_{\rcop},\eta}$ whose span $H$ is a hyperplane of $\bar T_\RR$. If $H$ is not the mirror of a vector of $\bar T$ of square $-2$ or $-4$, then (W) fails at $\eta$. In particular, at the cusps with $d=p^2$, whose boundary lattice is that of the $F_2$ cusp (@lem:cusp-lattice-p-greater-one) and whose Coxeter fan is cut by the $24$ $(-2)$-roots [@AET23, Def. 4.1 and Fig. 1, printed pp. 21--22], (W) there implies that every $18$-dimensional cone of $\mcf_{R_{\rcop},\eta}$ spans one of those $24$ root mirrors.
:::

::: {.proof}

A cone of the Coxeter semifan of dimension $18$ is a facet of a $19$-dimensional chamber, hence is contained in the mirror of a simple root of the diagram [@AET23, Lemma 4.4, printed p. 22], and the simple roots of the diagrams used here are vectors of square $-2$ or $-4$: the $(-2)$-vectors in every diagram read here [@AET23, Def. 4.1, printed p. 21; @Nik79b, printed p. 1402], together with the $(-4)$-vectors of divisibility $2$ where the boundary lattice is $2$-elementary [@AE22, §3A, printed p. 10]. At the cusps with $k\ge2$ no diagram is printed (@lem:cusp-lattice-p-greater-one), so the criterion is applied there through the $(-2)$ part of the list, which every printed diagram contains. If $\sigma$ were a union of cones of the semifan, the cones contained in $\sigma$ would cover it. A locally finite family of closed cones of dimension at most $17$ is countable, and its union has empty interior in the $18$-dimensional space $\operatorname{span}\sigma$, so by Baire it cannot fill $\sigma$. Hence one of the cones has dimension $18$ and spans $\sigma$; being a facet of a chamber it lies in a root mirror, and that mirror is $H$. So if $H$ is no root mirror, no such cover exists and (W) fails. At the unigonal cusp of $F_{2d}$ with $d\ge3$ the hyperplane $\langle-2d\rangle^\perp$ is no mirror of a vector of square $-2$ or $-4$, which gives the failure proved above; at $d=2$ it is the mirror of the $(-4)$-vector $g$, and the facet $h_\beta$ is used there instead.
:::

::: {.lemma #lem:p-cusp-meets-unigonal title="Every $p_*>1$ cusp shares a $1$-cusp with the unigonal cusp"}

Let $\eta$ be a $0$-cusp of $F_{2d}$ with $p_*(\delta_\eta)=p>1$. Write $d=N^2d_0$ with $d_0$ squarefree, let $h=\gcd(q,N)$ for the class $\{\pm q\}$ of $\eta$, so that $p=N/h$ [@AE23, §10C, printed p. 37], and put $a=q/h$ and $k=d/p^2=d_0h^2$. Let $g$ generate the $\langle-2d\rangle$ summand of $L_{2d}$ and let $e_1,f_1$ be the basis of the first hyperbolic plane. Then
$$\delta=a g+p e_1+p d_0q^2f_1$$
is a primitive isotropic representative of $\eta$ with $p_*(\delta)=p$. The vector $e_2$ of the second hyperbolic plane is primitive isotropic with $p_*(e_2)=1$, and $\delta\cdot e_2=0$; so $J=\ZZ\delta\oplus\ZZ e_2$ is a primitive isotropic rank-two sublattice. The boundary component $F_J$ is a $1$-cusp of the Baily--Borel compactification [@AET23, §3B, printed pp. 15--16], and both $F_{\ZZ\delta}$ and $F_{\ZZ e_2}$ lie in its closure: every $0$-cusp with $p_*>1$ and the unigonal cusp of $F_{2d}$ lie on a common $1$-cusp. By the compatibility clause of [@AE23, Def. 5.11, printed p. 14] the two $0$-cusp semifans are constrained by the same $1$-cusp.
:::

::: {.proof}

With $d=N^2d_0$, $p=N/h$ and $a=q/h$ one has $k=d/p^2=d_0h^2$ and $ka^2=d_0q^2$. Hence $\delta^2=-2da^2+p^2(e_1+d_0q^2f_1)^2=-2da^2+2p^2d_0q^2=0$, and $\delta$ is primitive because the gcd of its coordinates $(a,p,pd_0q^2)=(q/h,N/h,Nd_0q^2/h)$ is $\gcd(q,N)/h=1$. The class of $\delta/p=(q/N)g+e_1+d_0q^2f_1$ in $\Delta_{2d}$ is that of $(q/N)g=2qNd_0\cdot g/(2d)$, namely $2qNd_0$, so $\delta$ represents the cusp $\{\pm q\}$ [@AE23, §10C, printed p. 37]; $\delta/p$ lies in $L^*$, while $\delta/p^2$ pairs as $1/p$ with $f_1$ and does not, so $p_*(\delta)=p$. The vector $e_2$ is primitive isotropic with $p_*(e_2)=1$, and $\delta\cdot e_2=0$ because $g,e_1,f_1$ are orthogonal to $e_2$. The plane $J$ is primitive: a combination $m\delta+ne_2$ has $g$-coordinate $ma$, so divisibility in $L$ forces $m=0$ and then $n=0$; it is isotropic because both generators are. By [@AET23, §3B, printed pp. 15--16] a primitive isotropic rank-two $J$ defines a $1$-cusp $F_J$, and $F_I\subset\overline{F_J}$ exactly when the isotropic line $I$ lies in $J$; here both $\ZZ\delta$ and $\ZZ e_2$ do. The compatibility clause of [@AE23, Def. 5.11, printed p. 14] requires, for each $1$-cusp, that the direction sublattice $H_{I,\delta}$ of the tiling induced by the $0$-cusp $\delta$ be independent of $\delta$ in $I$; applied to the two lines in $J$ it gives $H_{J,\delta}=H_{J,e_2}$.
:::

::: {.lemma #lem:unigonal-locus-cusp-support title="The unigonal locus meets only the cusp with $p_*=1$"}

Let $F_H\hookrightarrow F_{2d}$ be the unigonal locus, of elliptic K3 surfaces with $L=s+(d+1)f$ [@AE23, Def. 10.9, printed p. 36]. Then the closure of $F_H$ in the Baily--Borel compactification meets only the $0$-cusps with $p_*(\delta)=1$; by [@AE23, Thm. 10.16, printed p. 38] these form a single $\Gamma$-orbit, the unigonal cusp. Consequently, at a cusp with $p_*>1$ no degeneration of a unigonal surface occurs, the identification $R_{\rcop}=n_d\bigl(s+\frac{d+1}{24}\sum_i f_i\bigr)$ of [@AE23, Prop. 10.10, printed p. 36] is not available, and the restriction theorem [@AE23, Thm. 10.16, printed p. 38] cannot be applied there.
:::

::: {.proof}

In the proof of [@AE23, Thm. 10.16, printed pp. 38--39] the cusps met by the unigonal locus are those of a primitive isotropic $\delta\in H^\perp$, and the proof records that such a $\delta$ has invariant $\delta^*=0$ (loc. cit.), that is $p_*(\delta)=1$. All $\delta$ with $p_*(\delta)=1$ are $\Gamma$-equivalent [@AE23, Thm. 10.16, printed p. 38], so there is a single such cusp. At a cusp with $p_*>1$ the hypothesis of [@AE23, Thm. 10.16, printed p. 38] fails, and with it the identification of the restriction of $R_{\rcop}$ with ABE22's divisor on which the theorem's proof rests.
:::

::: {.lemma #lem:shared-one-cusp-lattice title="The lattice of the shared $1$-cusp"}

Let $\eta$, $q$, $h$, $p=N/h$, $a=q/h$, $k=d/p^2=d_0h^2$, $\delta$ and $J$ be as in @lem:p-cusp-meets-unigonal. Then
$$J^\perp/J\cong\langle-2k\rangle\oplus E_8(-1)^{\oplus2},$$
of rank $17$. At $k=1$ ($d=p^2$, $h=1$) this is $E_8(-1)^{\oplus2}\oplus A_1(-1)$, the maximal parabolic subdiagram $E_8^2A_1$ of the $24$-root diagram [@AET23, Lemma 4.5, printed p. 23]; for every $k$ it is the lattice in which the tiling $F_{\delta,J}$ of [@AE23, Def. 5.11, printed p. 14] lives.
:::

::: {.proof}

Write $x=A g+be_1+cf_1+de_2+ef_2+w$ with $w\in E_8^{\oplus2}$. Then $x\cdot e_2=e$, so $e=0$, and $x\cdot\delta=-2daA+p(c+d_0q^2b)$, so $c+d_0q^2b=2pkaA$. The solutions are spanned by $u=e_1-d_0q^2f_1$, $v=g+2pkaf_1$ and $e_2$, together with $E_8^{\oplus2}$: $J^\perp=\langle u,v\rangle\oplus\ZZ e_2\oplus E_8^{\oplus2}$, of rank $2+1+16=19$. One has $\delta=av+pu$, $u^2=-2d_0q^2$, $v^2=-2p^2k=-2d$ and $u\cdot v=2pka$. Choose integers $r,s$ with $as-pr=1$; then $\delta$ and $z=rv+su$ form a basis of $\langle u,v\rangle$, so $z$ generates $\langle u,v\rangle/\ZZ\delta$. Moreover $z^2=-2dr^2+4pkars-2d_0q^2s^2=-2k(pr-as)^2=-2k$, where $ka^2=d_0q^2$. So $J^\perp/J$ is generated by $z$ and $E_8^{\oplus2}$, with $z^2=-2k$: it is $\langle-2k\rangle\oplus E_8(-1)^{\oplus2}$, of rank $17$. At $k=1$, $\langle-2\rangle\oplus E_8(-1)^{\oplus2}$ is the maximal parabolic subdiagram $E_8^2A_1$ of the $24$-root diagram [@AET23, Lemma 4.5, printed p. 23].
:::

::: {.question #qst:recognizable-semifan title="The cones for the rational-curve divisor away from the unigonal locus"}

The first of the two questions this block used to carry --- whether a **recognizable** polarizing divisor can have a semifan that does not coarsen the Coxeter semifan, that is, for which hypothesis (W) of @thm:semifan-recognizable-divisor fails --- is answered affirmatively by @lem:rcop-refinement-criterion: the rational-curve divisor $R_{\rcop}$ on $F_2$ is recognizable [@AE23, Thm. 10.11, printed p. 36], and (W) fails for it at the unique $0$-cusp, so the universal family of stable pairs $(X,\eps R_{\rcop})$ does not extend over the Coxeter toroidal compactification (@prop:semifan-coarsening-extension).

What remains is the second question, for $d\ge2$: for $R_{\rcop}$ on $F_{2d}$, which is recognizable for all $d$ [@AE23; @AE23a], which split $I\sqcup J$ does $\mcf_{R_{\rcop}}$ induce at each $0$-cusp of $F_{2d}$, if (W) holds there at all --- equivalently, across which mirrors of the Coxeter diagram does the combinatorial type of the KSBA-stable limits of the pairs $(X,\eps R_{\rcop})$ stay constant?

The comparison itself is not what blocks $d\ge2$, and neither is the norm of the roots. If the Coxeter semifan at the unigonal cusp is cut by any set of vectors of square $-2$ or $-4$ --- the two norms among the vertices of the diagrams of [@AE22, §3A, printed p. 10] --- the argument of @lem:rcop-refinement-criterion repeats with the facet $h_\beta=\sigma_{22}\cap\beta_L^\perp$ in place of $h_\gamma$: a vector of $\operatorname{span}(g,\beta_L)$ is $ag+b\beta_L$ and has square $-2ka^2-8b^2$, which is at most $-8$ when $b\ne0$, so the only such vector of square $-2$ or $-4$ is $\pm g$, and that only when $k=d/p\le2$ [@ABE22, §4C, printed p. 14]. A point $q$ of $\operatorname{relint}(h_\beta)$ outside the countably many proper hyperplanes cut by the other mirrors therefore lies on no mirror except possibly $g^\perp$. Its cell is a $19$-dimensional chamber when $g$ is not one of the cutting vectors; otherwise it is an $18$-dimensional cell, open in $g^\perp$, that meets $\{\beta_L<0\}$ because $q\in\beta_L^\perp$ and $\beta_L$ is a nonzero linear form on $g^\perp$, while $\sigma_{22}$ lies in $\{\beta_L\ge0\}$ [@ABE22, (4.2), printed p. 14]. In either case the cell is not contained in the $18$-dimensional $\sigma_{22}$, which contains $q$, so (W) fails; the long root $g$ at $k=2$ is included in this and does not repair (W). What is missing is the fan itself: the only Coxeter diagram of a $0$-cusp lattice of $F_{2d}$ printed in the sources read here is that of the $F_2$ cusp [@AET23, Def. 4.1 and Fig. 1, printed pp. 21--22], which by @lem:cusp-lattice-p-greater-one is also the diagram at the cusps with $d=p^2$ ($k=1$); at the cusps with $k\ge2$ the boundary lattice is the unigonal lattice of $F_{2k}$, and no Coxeter diagram of it is recorded.

No cone of $\mcf_{R_{\rcop}}$ is recorded at those cusps, and the gap is stated where the semifan is defined: [@AE23, Intro., printed p. 3] writes that "we have no explicit description, because the structure of a hypothetical 'tropical K3-rational curves pair' $(B,R^{\mathrm{rc}}_{\mathrm{trop}})$ is unknown", and calls such a description "an interesting open question". The restriction theorem the lemma uses is available at the unigonal cusp of every $F_{2d}$ [@AE23, Thm. 10.16, printed p. 38]. Question 2 is the computation of the type function at each cone, and it needs the stable limit of the pair over a cone, which is not an operation of the library (@rmk:missing-stable-limit, @rmk:rcop-split-computation); [@AET23] computes those limits for the ramification divisor $R\in|3L|$ and [@AE22] for $(X,\eps C_g)$. The cones it would be labelled in are printed at the $F_2$ cusp (@thm:cone-inventory-printed) and at the cusps with $d=p^2$ (@lem:cusp-lattice-p-greater-one); at the other $p_*>1$ cusps no inventory of them is recorded in the sources read here. What the computation must produce is constrained by @lem:wall-criterion: if (W) holds at a cusp, every $18$-dimensional cone of $\mcf_{R_{\rcop}}$ there spans a root mirror, so an $18$-dimensional cone whose span is no root mirror refutes (W). @lem:generalized-unigonal-constraint fixes one hyperplane in advance: at a cusp with $k\notin\{1,2\}$, (W) forces $z^\perp\cap C^+$ not to be a union of cones of $\mcf_{R_{\rcop},\eta}$, so a cone of the semifan meeting that open set must cross $z^\perp$ rather than lie in it.
:::
