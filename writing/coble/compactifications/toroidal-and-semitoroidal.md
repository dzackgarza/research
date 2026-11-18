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

::: {.theorem #thm:semifan-recognizable-divisor title="The semifan of a recognizable divisor is the generalized Coxeter semifan"}

Let $R$ be a recognizable polarizing divisor for $F_S$ (@def:recognizable-divisor) and let $\eta$ be a $0$-cusp. Put $\bar T=\eta^\perp/\eta$, denote by $C\subset\bar T_\RR$ the positive cone, by $\Gamma_\eta$ the Coxeter diagram of $\bar T$ with vertex set $V=V(\Gamma_\eta)$ and reflection group $W=W(\Gamma_\eta)$, and by $\mathfrak C$ its fundamental chamber. Write $H_v^+=\{x\in\bar T_\RR : x\cdot v\ge 0\}$. Assume

- **(T)** the combinatorial type of the KSBA-stable limit of a degeneration of monodromy invariant $\lambda\in\bar T\cap C$ depends only on $\lambda$, and the loci on which it is locally constant are the cones of a semifan $\mcf_{R,\eta}$ whose semitoroidal compactification normalizes the KSBA compactification;
- **(W)** $\mcf_{R,\eta}$ is invariant under $W$, every wall of it is a mirror $r^\perp$ of a root $r\in V$, uniformly along the mirror: there is a subset $J\subseteq V$ such that two chambers of the Coxeter complex whose common facet lies in $r^\perp$ lie in a common cone of $\mcf_{R,\eta}$ if and only if $r\in J$.

Let $J$ be the set of (W), put $I=V-J$ and $W_J=\langle w_j\mid j\in J\rangle$, and let $L=\Union_{h\in W_J}h(\mathfrak C)$. Then:

1. the maximal cones of $\mcf_{R,\eta}$ are the $W$-translates of $L$, and its remaining cones are the images $g(F)$ with $g\in W$ and $F$ a face of $\mathfrak C$ which is not of the form $\mathfrak C\cap\bigcap_{j\in J'}r_j^\perp$ for any $J'\subseteq J$; equivalently, $\mcf_{R,\eta}$ is the coarsening of the Coxeter semifan obtained by deleting the faces $\bigl(\bigcap_{j\in J'}\alpha_j^\perp\bigr)\cap\mathfrak C$ for $J'\subseteq J$;
2. $L=\bigcap_{i\in I}\bigcap_{h\in W_J}H^+_{h(r_i)}$ is convex and locally finite, its stabilizer in $W$ is $W_J$, and its support is the rational closure of $C$;
3. two Type II or Type III cones of the Coxeter semifan, that is, two cones cut out by a maximal parabolic or an elliptic subdiagram, lie in one cone of $\mcf_{R,\eta}$ exactly when their relevant contents agree, so the cones of $\mcf_{R,\eta}$ are indexed by the combinatorial types of the KSBA-stable limits;
4. $\mcf_{R,\eta}$ is a fan if and only if $J$ spans an elliptic subdiagram, that is, if and only if $W_J$ is finite;
5. $\mcf_{R,\eta}$ is invariant under $\Stab_\Gamma(\eta)$, hence $\Gamma$-admissible for the monodromy group $\Gamma$ of $F_S$.
:::

::: {.proof}

Hypothesis (T) is [@AE22, Prop. 8.1 and its proof, printed p. 41], which states it for the two-elementary lattices of [@AE22, Fig. 1, printed p. 5] with $g\ge2$ and $S\ne(10,8,0)$ and at every $0$-cusp of $F_S$; the proof derives the statement from the cone-by-cone determination [@AE23, Thm. 9.3 and Def. 8.12], the path independence of the limit being [@AE23, Cor. 8.13], so (T) is available for a recognizable $R$ on any $F_S$ exactly as far as that determination is. The semifan $\mcf_{R,\eta}$ is invariant under the image of $\Stab_\Gamma(\eta)$ in $\Orth(\bar T)$, because an element of $\Gamma$ fixing $\eta$ carries a degeneration of monodromy $\lambda$ to one of monodromy $g\lambda$ whose stable limit is the same, so it is $\Gamma$-admissible.

*Step 1: the relation on chambers.* Two neighbouring chambers of the Coxeter complex share exactly one facet, and that facet lies in exactly one mirror $r^\perp$. By (W) the facet is a wall of $\mcf_{R,\eta}$ exactly when $r\in I$, and by (T) the two chambers lie in one cone of $\mcf_{R,\eta}$, equivalently have the same combinatorial type, exactly when the facet is not a wall. So the two chambers are merged exactly when $r\in J$.

*Step 2: the maximal cones.* A cone of $\mcf_{R,\eta}$ is a union of chambers closed under the relation of Step 1, and a maximal cone is a connected component of that relation, since a further merge would have to cross a facet in a mirror of $I$, which is a wall. The reflections $w_j$, $j\in J$, generate $W_J$; the orbit $W_J\mathfrak C$ is connected for this relation, because a facet of $h(\mathfrak C)$ in $h(r_j)^\perp$ is shared with $hw_j(\mathfrak C)$, and it is closed under it, for the same reason. Hence the maximal cones are the closures of the sets $\Union_{h\in W_J}h(\mathfrak C^\circ)$, which are $L=\Union_{h\in W_J}h(\mathfrak C)$ and its $W$-translates. This is [@AE22, Def. 9.1 and Def. 9.3, printed p. 53], and the description of the coarsening as the deletion of the faces spanned by irrelevant roots is [@AEGS25, §5.2, printed p. 610].

*Step 3: the properties.* Assertions (2), (3) and (4) are [@AET23, Prop. 4.17, printed pp. 26--27] and [@AET23, Cor. 4.18, printed p. 27], in whose notation $I$ is the set of active and $J$ the set of inactive mirrors; the identification of the relevant content with the combinatorial type is [@AET23, Thm. 7.5, printed p. 48] together with [@AET23, Prop. 7.6, printed p. 49], and the fan criterion is [@AE22, Rem. 9.11, printed p. 57] and [@AET23, Rem. 4.19, printed p. 27]. Assertion (5) is the first paragraph.
:::

::: {.example #ex:recognizable-divisors}

Two basic examples of recognizable divisors:

1. The **rational curve divisor** $R_{\rcop} = \Sum R_i$ (the sum of all smooth rational curves in $|L|$).

2. The **ramification divisor** $R_\iota$ of a nonsymplectic involution.
:::

::: {.corollary #cor:semifan-computed-cases title="The hypothesis, and the split, in the computed cases"}

Hypotheses (T) and (W) of @thm:semifan-recognizable-divisor hold, with the following $I$ and $J$, for the ramification divisor $R_\iota$ of a nonsymplectic involution, in three families:

1. **Two-elementary lattices with $g\ge2$, $S\ne(10,8,0)$.** (T) is [@AE22, Prop. 8.1, printed p. 41]. For the lattice $\bar T_1=(10+\bar k,10-\bar k,\bar\delta)$ the set $I$ is the $2\bar k$ vertices on the $I_{2\bar k}$ cycle and $J$ every other vertex, "in particular all the black vertices"; for a lattice $\bar T_{\bar g}$ reached by a chain of mirror moves, $I$ consists of the vertices inherited from $\Gamma(\bar T_1)$ and $J$ of the rest [@AE22, Def. 9.5, printed p. 54]. (W) is [@AE22, Def. 9.5, printed p. 54] together with [@AE22, Thm. 9.10, printed p. 56], which dominates $\overline F_S^{\mcf_{R,\eta}}$ by the semitoroidal compactifications for the Coxeter semifans of $W_2$ and of $W_r$.
2. **Degree-two K3 surfaces.** $I=\{0,\dots,17\}$ and $J=\{18,\dots,23\}$ for the twenty-four roots of $\bar T=H\oplus E_8^2\oplus A_1$ [@AET23, printed p. 27]. (T) is [@AET23, Thm. 7.5, printed p. 48] with [@AET23, Thm. 8.2, printed p. 50], and (W) is [@AET23, Thm. 1.2, printed p. 3]: "the Coxeter fan refines this semifan".
3. **Enriques surfaces of degree two.** A folded root lies in $J$ exactly when it is the folding of a root off the boundary of the square, resp. the triangle [@AEGS25, Def. 5.4 and Lemma 5.5, printed p. 611]. (T) is [@AEGS25, Thm. 5.9, printed p. 611], whose proof excludes a strict coarsening of the collection on the ground that it would merge a codimension-one cone carrying a one-parameter family of non-maximal pairs [@AEGS25, printed p. 612].
:::

::: {.proof}

In each case the cited statement identifies the semitoroidal compactification for the displayed semifan with the normalization of the stable-pair compactification, and the displayed split is the one the cited definition uses: (1) [@AE22, Def. 9.5, printed p. 54] and [@AE22, Thm. 9.10, printed p. 56]; (2) [@AET23, §4D, printed p. 27] with [@AET23, Thm. 8.2, printed p. 50]; (3) [@AEGS25, Lemma 5.5 and Thm. 5.9, printed p. 611]. Hypothesis (W) is then the coarsening statement in each of the three sources, and (T) is the corresponding cone-by-cone determination of the stable limits.
:::

::: {.remark #rmk:semifan-not-a-fan}

Part (4) of @thm:semifan-recognizable-divisor is what "the coarsest subdivision" leaves out. The semifan is a fan only when the irrelevant roots span an elliptic subdiagram, which [@AE22, Rem. 9.11, printed p. 57] records as happening "in rather few cases" among the two-elementary cusps, and which holds at $\fentwo$ at the $0$-cusps $2$ and $4$ and fails at $1$, $3$ and $5$ [@AEGS25, Lemma 5.6, printed p. 611]. So the semifan of a recognizable divisor is in general not a fan, and no description of it as the coarsest fan above $\{C^+\}$ can exist.
:::

::: {.example #ex:elliptic-k3-divisor-fans title="Two polarizing divisors on elliptic K3 surfaces"}

Let $F$ parameterize elliptic K3 surfaces with section $s$ and singular fibers $f_1,\ldots,f_{24}$, counted with multiplicity. For the polarizing divisor $R=s+m\sum_i f_i$ with $m\ge1$, the normalization of the stable-pair compactification is toroidal. Its fan subdivides each Coxeter chamber into nine chambers, so it refines the Coxeter fan [@ABE22, Intro., Thm. 1.2]. For the image of the trisection of nonzero $2$-torsion points after contracting the section, the normalization is toroidal for a fan whose chamber is the union of four Coxeter chambers [@ABE22, Intro., Thm. 1.1 and §3]. Thus these two geometric divisors give opposite directions of comparison with the same Coxeter fan.
:::

::: {.question #qst:recognizable-semifan title="The semifan of the rational-curve divisor"}

Let $R_{\rcop}$ be the rational-curve divisor of @ex:recognizable-divisors on $F_{2d}$. Is hypothesis (W) of @thm:semifan-recognizable-divisor satisfied at each $0$-cusp, that is, does $\mcf_{R_{\rcop}}$ coarsen the Coxeter semifan, and if so, which split $I\sqcup J$ does it induce --- equivalently, across which mirrors of the Coxeter diagram does the combinatorial type of the KSBA-stable limits of the pairs $(X,\eps R_{\rcop})$ stay constant?

Neither source that computes a semifan computes this one: [@AET23] determines the stable limits of the pairs $(X,\eps R)$ for $R$ the ramification divisor in $|3L|$, and [@AE22] those of $(X,\eps C_g)$ for the fixed curve, so in both the divisor is $R_\iota$ and not $R_{\rcop}$. The answers are therefore recorded for no $d$ in the sources read, and by @thm:semifan-recognizable-divisor the open input is the type function $\bS_{R_{\rcop}}$ at the $0$-cusps and nothing further.
:::
