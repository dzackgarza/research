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

A **semitoroidal compactification** $\semitorcpt{\FG}$ replaces the fans of a toroidal compactification (@def:toroidal-compactification) with $\Gamma$-admissible **semifans** $\mcf_I$ [@Loo02, Def. 6.1; @AE23, Def. 5.11].

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
Then $\overline F$ is a semitoroidal compactification (@def:semitoroidal-compactification), for some semifan $\mcf_I$, if and only if it sits between some toroidal and the Baily--Borel compactification, that is if there is a fan $\torfan$ and a tower
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

::: {.definition #def:generalized-coxeter-semifan}

Let $\eta$ be a $0$-cusp with Coxeter diagram $G(\Gamma_\eta)$ (@def:coxeter-matrix), reflection group $W$ and fundamental chamber $\mathfrak{C}$.
Partition the vertices of $G(\Gamma_\eta)$, that is the simple roots, into $\Phi = \Phi^{\relevant} \sqcup \Phi^{\irrelevant}$, the **relevant** and the **irrelevant roots**.
Let $W^{\irrelevant} \subseteq W$ be the subgroup generated by the reflections in the irrelevant roots.

The **generalized Coxeter semifan** $\mcf_{\mathrm{gen}}$ has, modulo $W$, the unique maximal cone $\Union_{h \in W^{\irrelevant}} h(\mathfrak{C})$; its other cones are the faces of $\mathfrak{C}$ and their $W$-translates [@AE22, Def. 9.1].
Its maximal cones are the unions of Weyl chambers (@def:weyl-chamber) $g\big(\Union_{h \in W^{\irrelevant}} h(\mathfrak{C})\big)$ for $g \in W$.
:::

::: {.proposition #prop:generalized-coxeter-semifan-is-fan title="When a generalized Coxeter semifan is a fan"}

The generalized Coxeter semifan $\mcf_{\mathrm{gen}}$ of @def:generalized-coxeter-semifan is a fan if and only if $W$ has finite covolume and $W^{\irrelevant}$ is finite, that is, the irrelevant roots span an elliptic subdiagram [@AE22, Rem. 9.11].
:::

::: {.proof}

This is [@AE22, Rem. 9.11].
:::

::: {.theorem #thm:degree-two-k3-semifan title="The ramification semifan for degree-two K3 surfaces"}

Let $F_2$ be the moduli space of degree-two polarized K3 surfaces $(X,L)$. The covering involution of $X\to\PP^2$ has ramification divisor $R\in|3L|$. The normalization of the KSBA compactification (@def:ksba-compactification) of pairs $(X,\eps R)$ is a semitoroidal compactification (@def:semitoroidal-compactification) of $F_2$. Its semifan is coarsened by the Coxeter fan of the hyperbolic lattice $N=U\oplus E_8(-1)^2\oplus A_1(-1)$: equivalently, the Coxeter fan refines the ramification semifan [@AET23, Thm. 1.2].
:::

::: {.proof}

The normalization and refinement are [@AET23, Thm. 1.2]. The morphism from the Coxeter toroidal compactification (@def:toroidal-compactification) to this semitoroidal compactification follows from @prop:semifan-refinement-morphism.
:::

![Schematic reflection chamber with an ideal vertex.](/rendered/F2HyperbolicReflection.jpg){#fig-k3-ideal-reflection-chamber}

## KSBA compactifications

::: {.definition #def:ksba-compactification}

A pair $(X, D = \Sum b_j D_j)$ is **KSBA-stable** [@KS88; @Ale96] if:

1. $X$ is a projective demi-normal variety;

2. $0 < b_j \le 1$;

3. the pair $(X, D)$ has **semi log canonical (slc)** singularities;

4. $K_X + D$ is ample and $\QQ$-Cartier.

For K-trivial varieties (like K3 or Enriques surfaces (@def:enriques-surface)), one uses pairs $(X, \eps R)$ for $0 < \eps \ll 1$ and a polarizing divisor $R$. On a slc K3 limit with trivial dualizing sheaf, the divisor $R$ must be ample and avoid the log canonical centers; then small $\eps>0$ preserves the slc condition and makes $K_X+\eps R$ ample [@AE23, §6].
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

If $R$ is recognizable, then the normalization of the KSBA compactification (@def:ksba-compactification) $\oF^R$ is isomorphic to a semitoroidal compactification (@def:semitoroidal-compactification) $\overline{F_S}^{\mcf_R}$, defined by a specific semifan $\mcf_R$ [@AE23, Thm. 9.1].
:::

::: {.proof}

This is [@AE23, Thm. 9.1].
:::

::: {.example #ex:recognizable-divisors}

Two basic examples of recognizable divisors:

1. The **rational curve divisor** $R_{\rcop} = \Sum R_i$ (the sum of all smooth rational curves in $|L|$).

2. The **ramification divisor** $R_\iota$ of a nonsymplectic involution.
:::

::: {.example #ex:elliptic-k3-divisor-fans title="Two polarizing divisors on elliptic K3 surfaces"}

Let $F$ parameterize elliptic K3 surfaces with section $s$ and singular fibers $f_1,\ldots,f_{24}$, counted with multiplicity. For the polarizing divisor $R=s+m\sum_i f_i$ with $m\ge1$, the normalization of the stable-pair compactification is toroidal. Its fan subdivides each Coxeter chamber into nine chambers, so it refines the Coxeter fan [@ABE22, Intro., Thm. 1.2]. For the image of the trisection of nonzero $2$-torsion points after contracting the section, the normalization is toroidal for a fan whose chamber is the union of four Coxeter chambers [@ABE22, Intro., Thm. 1.1 and §3]. Thus these two geometric divisors give opposite directions of comparison with the same Coxeter fan.
:::

::: {.question #qst:recognizable-semifan title="The semifan of a recognizable divisor"}

Describe the semifan $\mcf_R$ of @thm:recognizable-semitoroidal for a recognizable divisor $R$, and in particular for the rational curve divisor $R_{\rcop}$ of @ex:recognizable-divisors.
:::
