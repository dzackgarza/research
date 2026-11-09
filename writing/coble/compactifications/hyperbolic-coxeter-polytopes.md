# Hyperbolic Coxeter polytopes and finite covolume {#sec-hyperbolic-coxeter-polytopes}

::: {.notation}

Throughout, $L$ is a hyperbolic lattice of signature $(1,n)$, $C_L^+$ is a fixed component of its positive cone, and $\HH^n_L$ is the associated hyperbolic $n$-space of @def:hyperbolic-model.
Roots are negative-definite directions, so a mirror $H_v = v^{\perp}\intersect\HH^n_L$ is nonempty exactly when $v^2 < 0$.
:::

## The Tits cone

::: {.definition #def:tits-cone}

Let $(W,S)$ be a Coxeter system with Gram form $G$ on $V \definedas \RR^S$ and simple roots $\theset{\alpha_s}_{s\in S}$, and let $W$ act on the dual space $V^*$ by the contragredient of its action on $V$.
The **closed fundamental chamber** is
$$
\oC \definedas \theset{\, f\in V^* \mid f(\alpha_s)\geq 0 \text{ for all } s\in S \,}
,
$$
and the **Tits cone** of $(W,S)$ is
$$
U \definedas \Union_{w\in W} w\!\left(\oC\right) \iscontainedin V^*
.
$$
When $G$ is nondegenerate it identifies $V$ with $V^*$, and $\oC$ becomes the cone $\theset{v\in V \mid \beta(v,\alpha_s)\geq 0}$ over the closure of a Weyl chamber in the sense of @def:weyl-chamber.
:::

::: {.theorem #thm:tits-cone title="Properties of the Tits cone"}

Let $(W,S)$, $\oC$ and $U$ be as in @def:tits-cone, and for $f\in \oC$ write $I(f) \definedas \theset{s\in S \mid f(\alpha_s) = 0}$.

1. $U$ is a convex cone, and $\oC$ is a strict fundamental domain for the action of $W$ on $U$: every $W$-orbit in $U$ meets $\oC$ in exactly one point.

2. The stabilizer of $f\in\oC$ in $W$ is the standard parabolic subgroup $W_{I(f)}$ of @def:coxeter-subdiagram.

3. A point $f\in\oC$ lies in the interior of $U$ if and only if $W_{I(f)}$ is finite, that is, if and only if the subdiagram $\Sigma_{I(f)}$ is elliptic.

4. $W$ acts properly discontinuously on the interior of $U$.
:::

::: {.proof}

Parts (1) and (2) are [@Hum90, §5.13, Theorem]; the four parts together are [@Bou08; @Hum90].
:::

::: {.proposition #prop:tits-cone-spherical title="The Tits cone of a spherical system"}

Let $(W,S)$ be an irreducible Coxeter system with Tits cone $U$.
Then $(W,S)$ is spherical if and only if $U = V^*$.
:::

::: {.proof}

By @thm:coxeter-type-and-geometry(1), $(W,S)$ is spherical if and only if $W$ is finite, and $W$ is finite if and only if $U = V^*$ [@Hum90, §5.13, Exercise, and §6.4].
:::

::: {.proposition #prop:euclidean-affine-hyperplane title="The affine action of a euclidean system"}

Let $(W,S)$ be an irreducible euclidean Coxeter system, and let $\ker G = \RR\delta$ as in @prop:euclidean-radical.
Then $W$ stabilizes the affine hyperplane $E \definedas \theset{f\in V^* \mid f(\delta) = 1}$ and acts on it faithfully.
For the euclidean structure on $E$ induced by $G$, each $s\in S$ acts on $E$ as the orthogonal reflection in the affine hyperplane $E\intersect\theset{f \mid f(\alpha_s) = 0}$ [@Hum90, §6.5].
:::

::: {.proof}

This is [@Hum90, §6.5], where the vector $\lambda$ spanning the radical is $\delta$.
:::

## Vertices of a Coxeter polytope

::: {.notation}

Let $P\iscontainedin\HH^n_L$ be a Coxeter polytope (@def:coxeter-polytope) with walls $H_s = \alpha_s^{\perp}$ indexed by a finite set $S$, and Coxeter--Vinberg diagram $\Sigma$.
For $I\iscontainedin S$ write
$$
A_I \definedas \spanof_\RR\theset{\, \alpha_s \mid s\in I \,} \iscontainedin L_\RR
.
$$
The Gram matrix $G[I,I]$ is the Gram matrix of a spanning set of $A_I$, so its rank equals the rank of $\restrictionof{\beta_L}{A_I}$; that common value is the rank of $\Sigma_I$ in the sense of @def:coxeter-subdiagram.
:::

::: {.proposition #prop:polytope-vertex-subdiagram title="Vertices and subdiagrams"}

Let $I\iscontainedin S$.

1. If $\Sigma_I$ is elliptic of rank $n$, then $\dim A_I = n$, the orthogonal complement $A_I^{\perp L_\RR}$ is a line spanned by a vector of positive norm, and
   $$
   \Intersect_{s\in I} H_s
   $$
   is a single point of $\HH^n_L$, an **ordinary vertex** of $P$ when it lies in $\overline{P}$.

2. If $\Sigma_I$ is parabolic of rank $n-1$, then $\dim A_I = n$, the form $\restrictionof{\beta_L}{A_I}$ is negative semidefinite with radical a line $\RR\eta$ spanned by an isotropic vector $\eta$, one has $A_I^{\perp L_\RR} = \RR\eta$, and
   $$
   \Intersect_{s\in I}\overline{H_s}
   $$
   meets the closure of $\HH^n_L$ in the single boundary point $[\eta]\in\del\HH^n_L$, an **ideal vertex** of $P$ when it lies in $\overline P$.
   In this case the negative-definite lattice $\eta^{\perp L}/\eta$ has rank $n-1$, and the stabilizer of $[\eta]$ in $W$ is $W_I$, acting on $(\eta^{\perp L}/\eta)\tensor_\ZZ\RR \cong \EE^{\,n-1}$ as the euclidean reflection group with diagram $\Sigma_I$.
:::

::: {.proof}
Suppose first that $\Sigma_I$ is elliptic of rank $n$.
Then $G[I,I]$ is negative definite of rank $n$, so the $\alpha_s$ with $s\in I$ are linearly independent and $\dim A_I = n$.
Since $\restrictionof{\beta_L}{A_I}$ is nondegenerate, $L_\RR = A_I\perp A_I^{\perp}$, so $A_I^{\perp}$ is a line of signature $(1,0)$, spanned by a vector $v$ with $v^2 > 0$.
Now $\Intersect_{s\in I}H_s$ is the image of $A_I^\perp$ in $\HH^n_L$, a single point.

Suppose instead that $\Sigma_I$ is parabolic of rank $n-1$.
Each connected component of $\Sigma_I$ has a one-dimensional kernel by @def:elliptic-subdiagram, so $\restrictionof{\beta_L}{A_I}$ is negative semidefinite and degenerate.
Its radical is $A_I\intersect A_I^{\perp}$, a totally isotropic subspace of $L_\RR$, hence of dimension at most $\min(n_+,n_-) = 1$; being nonzero it is a line $\RR\eta$ with $\eta^2 = 0$.
Then $\dim A_I = \rank(\restrictionof{\beta_L}{A_I}) + 1 = n$, so $\dim A_I^{\perp} = (n+1) - n = 1$, and $\RR\eta\iscontainedin A_I^\perp$ forces $A_I^{\perp} = \RR\eta$.
The intersection $\Intersect_{s\in I}\overline{H_s}$ is the image of $A_I^\perp$ in $\PP(L_\RR)$, the single point $[\eta]$, which lies on $\del\HH^n_L$ because $\eta$ is isotropic.
Since $\eta$ is isotropic and $L$ has signature $(1,n)$, the form induced on $\eta^{\perp}/\eta$ is negative definite of rank $n-1$; and $A_I\iscontainedin\eta^{\perp}$, with $A_I/\RR\eta$ of dimension $n-1$, so $W_I$ acts on $\eta^{\perp}/\eta$ as the reflection group of $\Sigma_I$, which is euclidean by @def:coxeter-system-type.
:::

::: {.corollary #cor:ideal-vertices-are-parabolic}

Sending an ideal vertex $[\eta]$ of $P$ to the set $I$ of all walls of $P$ through $[\eta]$ is a bijection from the ideal vertices of $P$ onto a set of parabolic subdiagrams of $\Sigma$ of rank $n-1$, and each such $\Sigma_I$ is maximal among the parabolic subdiagrams of $\Sigma$, in the sense of @def:parabolic-subdiagram.
:::

::: {.proof}
Let $[\eta]$ be an ideal vertex and $I$ the set of walls through it, so $A_I \iscontainedin \eta^{\perp}$ and $\Sigma_I$ is parabolic of rank $n-1$ by @prop:polytope-vertex-subdiagram.
Suppose $\Sigma_J$ is parabolic with $J\containing I$.
Writing $r\leq 1$ for the dimension of the radical of $\restrictionof{\beta_L}{A_J}$, one has $\dim A_J - r = \rank(\restrictionof{\beta_L}{A_J})\leq n_-(L_\RR) = n$, so $\dim A_J\leq n+1$; and $\dim A_J = n+1$ would make $A_J = L_\RR$, whose form is nondegenerate of signature $(1,n)$ rather than negative semidefinite.
Hence $\dim A_J\leq n = \dim A_I$, so $A_J = A_I$ and every wall indexed by $J$ contains $A_I^{\perp} = \RR\eta$, that is, passes through $[\eta]$.
By the choice of $I$ this gives $J = I$.
:::

## Covolume, compactness, and finite volume

::: {.definition #def:covolume}

Let $\Gamma\leq\Isom(\HH^n_L)$ be a discrete subgroup.
Its **covolume** is the hyperbolic volume $\vol(\HH^n_L/\Gamma)$ of the quotient orbifold.
If $\Gamma$ is generated by the reflections in the walls of a Coxeter polytope $P$, then $P$ is a strict fundamental domain and $\vol(\HH^n_L/\Gamma) = \vol(P)$.
:::

::: {.theorem #thm:coxeter-polytope-volume title="Finite volume and compactness"}

Let $P\iscontainedin\HH^n_L$ be a Coxeter polytope with finitely many walls and Coxeter--Vinberg diagram $\Sigma$.

1. $\vol(P) < \infty$ if and only if, in the projective model of @def:hyperbolic-model, the closure of $P$ is the convex hull of finitely many points of $\overline{\HH^n_L}$ --- equivalently, of the ordinary and ideal vertices supplied by @prop:polytope-vertex-subdiagram.

2. $P$ is compact if and only if $\vol(P)<\infty$ and $P$ has no ideal vertex; equivalently, if and only if the closure of $P$ in the projective model is the convex hull of finitely many ordinary vertices.
   By @cor:ideal-vertices-are-parabolic this is the condition that no parabolic subdiagram of $\Sigma$ of rank $n-1$ is cut out by a set of walls meeting in $\overline{P}$.

3. $P$ has infinite volume if and only if its closure in the projective model has a vertex outside $\overline{\HH^n_L}$ [@Vin67; @Vin85].
:::

::: {.proof}

This is [@Vin67; @Vin85].
:::

::: {.corollary #cor:coxeter-simplex-volume title="The simplex case"}

Suppose $\abs{S} = n+1$ and $P$ is a simplex, so that its $n+1$ vertices are cut out by the $n+1$ maximal proper subdiagrams $\Sigma_{S\sm\theset{s}}$, $s\in S$.
Then

1. $P$ is compact if and only if every $\Sigma_{S\sm\theset{s}}$ is elliptic;

2. $\vol(P) < \infty$ if and only if every $\Sigma_{S\sm\theset{s}}$ is elliptic or parabolic, the ideal vertices being those $s$ for which $\Sigma_{S\sm\theset{s}}$ is parabolic;

3. $\vol(P) = \infty$ if and only if some $\Sigma_{S\sm\theset{s}}$ is hyperbolic.
:::

::: {.proof}

Since $P$ is a simplex, the $\alpha_s$ for $s\in S$ form a basis of $L_\RR$, and the closure of $P$ in the projective model is the convex hull of the $n+1$ points $v_s$, where $v_s$ spans the line $A_{S\sm\theset{s}}^{\perp}$.
So $A_{S\sm\theset{s}} = v_s^{\perp}$, and $\Sigma_{S\sm\theset{s}}$ has the Gram form $\restrictionof{\beta_L}{v_s^\perp}$.
As $L_\RR$ has signature $(1,n)$, @thm:sylvester gives: $v_s^2 > 0$ exactly when $v_s^{\perp}$ is negative definite, that is $\Sigma_{S\sm\theset{s}}$ is elliptic; $v_s^2 < 0$ exactly when $v_s^{\perp}$ is nondegenerate of signature $(1,n-1)$, that is $\Sigma_{S\sm\theset{s}}$ is hyperbolic; and $v_s^2 = 0$ exactly when $v_s^{\perp}$ is degenerate, with radical $\RR v_s$.

By @thm:coxeter-polytope-volume(2), $P$ is compact exactly when every $v_s$ lies in $\HH^n_L$, which is (1).
By @thm:coxeter-polytope-volume(3), $\vol(P) = \infty$ exactly when some $v_s$ lies outside $\overline{\HH^n_L}$, which is (3).
By @thm:coxeter-polytope-volume(1), $\vol(P) < \infty$ exactly when every $v_s^2\geq 0$, and then the ideal vertices are the $v_s$ with $v_s^2 = 0$.
The walls through such an ideal vertex $v_s$ are those indexed by $S\sm\theset{s}$, because $v_s\perp\alpha_s$ would make $v_s$ orthogonal to a basis of $L_\RR$.
So $\Sigma_{S\sm\theset{s}}$ is parabolic by @cor:ideal-vertices-are-parabolic; conversely a parabolic $\Sigma_{S\sm\theset{s}}$ has degenerate Gram form, so $v_s^2 = 0$.
This is (2).
:::

::: {.theorem #thm:compact-coxeter-simplices title="Compact hyperbolic Coxeter simplices"}

A compact Coxeter simplex in $\HH^n$, in the sense of @cor:coxeter-simplex-volume(1), exists only for $n\in\theset{2,3,4}$ [@Hum90, §6.9].
In $\HH^2$ the compact Coxeter simplices are the triangles of @ex:hyperbolic-triangle-groups with $p,q,r$ all finite and $\tfrac1p + \tfrac1q + \tfrac1r < 1$, and there are infinitely many.
Up to isomorphism of Coxeter diagrams there are nine compact Coxeter simplices in $\HH^3$ and five in $\HH^4$.
:::

::: {.proof}

The compact hyperbolic Coxeter groups of [@Hum90, §6.8] are those of an irreducible Coxeter system with nondegenerate form $B$, not positive definite, such that the diagram with any one vertex removed is positive definite; under $G = -2B$ this is the condition of @cor:coxeter-simplex-volume(1).
That they exist only in ranks $3$, $4$ and $5$ is [@Hum90, §6.9].

In rank $3$, @cor:coxeter-simplex-volume(1) requires each rank-two subdiagram to be elliptic, that is each $m_{st}$ finite, and @ex:hyperbolic-triangle-groups gives the hyperbolic condition $\tfrac1p + \tfrac1q + \tfrac1r < 1$; the triples $(2,3,r)$ for $r\geq 7$ give infinitely many.

In ranks $4$ and $5$ every edge of the connected diagram lies in a connected subdiagram on three vertices, which is elliptic and hence $A_3$, $B_3$ or $H_3$ by @thm:spherical-classification, so every $m_{st}\in\theset{2,3,4,5}$.
An enumeration of the Coxeter matrices of ranks $4$ and $5$ with entries in $\theset{2,3,4,5}$, keeping those with connected diagram, Schläfli matrix of signature $(n-1,1)$ and every diagram with one vertex removed positive definite, computed with floating-point eigenvalues and reduced modulo permutations of $S$, gives $9$ classes in rank $4$ and $5$ classes in rank $5$.
:::

::: {.example #ex:hyperbolic-triangle-groups title="Triangle groups"}

Let $2\leq p\leq q\leq r\leq\infty$ and let $\Sigma$ be the rank-three diagram with $m_{12} = p$, $m_{13} = q$, $m_{23} = r$.
A Coxeter polytope realizing $\Sigma$ is a triangle with angles $\pi/p$, $\pi/q$, $\pi/r$, an angle $0$ being read as an ideal vertex, and the type of $\Sigma$ is decided by the angle sum:
$$
\frac1p + \frac1q + \frac1r
\;\begin{cases}
> 1 & \text{spherical, and the triangle lies in } S^2;\\
= 1 & \text{euclidean, and the triangle lies in } \EE^2;\\
< 1 & \text{hyperbolic, and the triangle lies in } \HH^2.
\end{cases}
$$
In the hyperbolic case the triangle has area $\pi\left(1 - \tfrac1p - \tfrac1q - \tfrac1r\right)$ by the Gauss--Bonnet theorem, so every hyperbolic triangle group has finite covolume; it is cocompact exactly when $p,q,r$ are all finite, and each entry equal to $\infty$ contributes one ideal vertex.
The spherical solutions are $(2,2,r)$, $(2,3,3)$, $(2,3,4)$ and $(2,3,5)$, which are the rank-three entries $I_2(r)\times A_1$, $A_3$, $B_3$ and $H_3$ of @thm:spherical-classification; the euclidean solutions are $(2,3,6)$, $(2,4,4)$ and $(3,3,3)$, which are $\tilde G_2$, $\tilde C_2$ and $\tilde A_2$.
:::

::: {.corollary #cor:coxeter-polytope-acute title="Coxeter polytopes are acute-angled"}

Every dihedral angle of a Coxeter polytope in $\EE^n$, $S^n$ or $\HH^n$ is at most $\pi/2$.
:::

::: {.proof}

By @def:coxeter-polytope each dihedral angle is $\pi/m$ for an integer $m\geq 2$.
:::

## The cusps of the quotient

::: {.proposition #prop:cusp-cross-section title="The stabilizer of an ideal vertex"}

Let $P$ be a finite-volume Coxeter polytope with reflection group $W$, let $[\eta]$ be an ideal vertex of $P$, and let $I$ be the set of walls of $P$ through $[\eta]$.
Then the stabilizer of $[\eta]$ in $W$ is $W_I$, and $W_I$ acts on $(\eta^{\perp L}/\eta)\tensor_\ZZ\RR\cong\EE^{\,n-1}$ as a euclidean reflection group with a compact fundamental domain.
:::

::: {.proof}

By @cor:ideal-vertices-are-parabolic, $\Sigma_I$ is parabolic of rank $n-1$, and by @prop:polytope-vertex-subdiagram(2) the stabilizer of $[\eta]$ is $W_I$, acting on $\EE^{\,n-1}$ as the euclidean reflection group with diagram $\Sigma_I$.
By @prop:parabolic-subdiagram-product, $W_I$ is the direct product of the irreducible euclidean Coxeter systems $(W_{I_j}, I_j)$ of the components $\Sigma_{I_j}$ of $\Sigma_I$.
By @thm:coxeter-type-and-geometry(2), each $W_{I_j}$ acts on a euclidean space of dimension $\abs{I_j} - 1$ with a euclidean simplex as fundamental domain.
These dimensions add up to $\sum_j(\abs{I_j}-1) = \rank\Sigma_I = n-1$, so the product of these simplices is a compact fundamental domain for $W_I$ on $\EE^{\,n-1}$.
:::
