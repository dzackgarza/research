# Hyperbolic Coxeter polytopes and finite covolume

::: {.Remark}
### Orientation

Vinberg's algorithm (\longref{thm:vinberg-algorithm}) returns a set of simple roots and terminates when they bound a chamber of finite volume.
The condition it tests is a condition on the vertices of that chamber, and those vertices are read off the Coxeter--Vinberg diagram.

Throughout, $L$ is a hyperbolic lattice of signature $(1,n)$, $C_L^+$ is a fixed component of its positive cone, and $\HH^n_L$ is the associated hyperbolic $n$-space of \longref{def:hyperbolic-model}.
Roots are negative-definite directions, so a mirror $H_v = v^{\perp}\cap\HH^n_L$ is nonempty exactly when $v^2 < 0$.
:::

## The Tits cone

::: {.Definition #def:tits-cone}

Let $(W,S)$ be a Coxeter system with Gram form $G$ on $V \da \RR^S$ and simple roots $\ts{\alpha_s}_{s\in S}$, and let $W$ act on the dual space $V^*$ by the contragredient of its action on $V$.
The **closed fundamental chamber** is
$$
\overline{C} \da \ts{\, f\in V^* \mid f(\alpha_s)\geq 0 \text{ for all } s\in S \,}
,
$$
and the **Tits cone** of $(W,S)$ is
$$
U \da \Union_{w\in W} w\!\left(\overline{C}\right) \containedin V^*
.
$$
When $G$ is nondegenerate it identifies $V$ with $V^*$, and $\overline C$ becomes the cone $\ts{v\in V \mid \beta(v,\alpha_s)\geq 0}$ over the closure of a Weyl chamber in the sense of \longref{def:weyl-chamber}.
:::

::: {.Theorem #thm:tits-cone}
### Properties of the Tits cone

Let $(W,S)$, $\overline C$ and $U$ be as in \longref{def:tits-cone}, and for $f\in \overline C$ write $I(f) \da \ts{s\in S \mid f(\alpha_s) = 0}$.

1. $U$ is a convex cone, and $\overline{C}$ is a strict fundamental domain for the action of $W$ on $U$: every $W$-orbit in $U$ meets $\overline{C}$ in exactly one point.

2. The stabilizer of $f\in\overline{C}$ in $W$ is the standard parabolic subgroup $W_{I(f)}$ of \longref{def:coxeter-subdiagram}.

3. A point $f\in\overline{C}$ lies in the interior of $U$ if and only if $W_{I(f)}$ is finite, that is, if and only if the subdiagram $\Sigma_{I(f)}$ is elliptic.

4. $W$ acts properly discontinuously on the interior of $U$.

These are theorems of Tits, recorded in [@Bou08; @Hum90].
:::

::: {.Remark}

For a spherical Coxeter system $U = V^*$.
For an irreducible euclidean one, with $\ker G = \RR\delta$ as in \longref{prop:euclidean-radical}, $U$ is the open half-space $\ts{f \mid f(\delta) > 0}$ together with the origin, and the affine reflection group of \longref{thm:coxeter-type-and-geometry}(2) is its action on the hyperplane $f(\delta) = 1$.

For a hyperbolic Coxeter system, part (3) says which points of the chamber have finite stabilizer, and \longref{prop:polytope-vertex-subdiagram} identifies those on the boundary of the cone: an ordinary vertex of the polytope lies in the interior of $U$, and an ideal vertex does not, its stabilizer being an infinite euclidean reflection group.
:::

## Vertices of a Coxeter polytope

::: {.Notation}

Let $P\containedin\HH^n_L$ be a Coxeter polytope (\longref{def:coxeter-polytope}) with walls $H_s = \alpha_s^{\perp}$ indexed by a finite set $S$, and Coxeter--Vinberg diagram $\Sigma$.
For $I\containedin S$ write
$$
A_I \da \spanof_\RR\ts{\, \alpha_s \mid s\in I \,} \containedin L_\RR
.
$$
The Gram matrix $G[I,I]$ is the Gram matrix of a spanning set of $A_I$, so its rank equals the rank of $\ro{\beta_L}{A_I}$; that common value is the rank of $\Sigma_I$ in the sense of \longref{def:coxeter-subdiagram}.
:::

::: {.Proposition #prop:polytope-vertex-subdiagram}
### Vertices and subdiagrams

Let $I\containedin S$.

1. If $\Sigma_I$ is elliptic of rank $n$, then $\dim A_I = n$, the orthogonal complement $A_I^{\perp L_\RR}$ is a line spanned by a vector of positive norm, and
   $$
   \Intersect_{s\in I} H_s
   $$
   is a single point of $\HH^n_L$, an **ordinary vertex** of $P$ when it lies in $\overline{P}$.

2. If $\Sigma_I$ is parabolic of rank $n-1$, then $\dim A_I = n$, the form $\ro{\beta_L}{A_I}$ is negative semidefinite with radical a line $\RR\eta$ spanned by an isotropic vector $\eta$, one has $A_I^{\perp L_\RR} = \RR\eta$, and
   $$
   \Intersect_{s\in I}\overline{H_s}
   $$
   meets the closure of $\HH^n_L$ in the single boundary point $[\eta]\in\partial\HH^n_L$, an **ideal vertex** of $P$ when it lies in $\overline P$.
   In this case the negative-definite lattice $\eta^{\perp L}/\eta$ has rank $n-1$, and the stabilizer of $[\eta]$ in $W$ is $W_I$, acting on $(\eta^{\perp L}/\eta)\tensor\RR \cong \EE^{\,n-1}$ as the euclidean reflection group with diagram $\Sigma_I$.
:::

::: {.proof}
Suppose first that $\Sigma_I$ is elliptic of rank $n$.
Then $G[I,I]$ is negative definite of rank $n$, so the $\alpha_s$ with $s\in I$ are linearly independent and $\dim A_I = n$.
Since $\ro{\beta_L}{A_I}$ is nondegenerate, $L_\RR = A_I\perp A_I^{\perp}$, so $A_I^{\perp}$ is a line of signature $(1,0)$, spanned by a vector $v$ with $v^2 > 0$.
Now $\Intersect_{s\in I}H_s$ is the image of $A_I^\perp$ in $\HH^n_L$, a single point.

Suppose instead that $\Sigma_I$ is parabolic of rank $n-1$.
Each connected component of $\Sigma_I$ has a one-dimensional kernel by \longref{def:elliptic-subdiagram}, so $\ro{\beta_L}{A_I}$ is negative semidefinite and degenerate.
Its radical is $A_I\intersect A_I^{\perp}$, a totally isotropic subspace of $L_\RR$, hence of dimension at most $\min(n_+,n_-) = 1$; being nonzero it is a line $\RR\eta$ with $\eta^2 = 0$.
Then $\dim A_I = \rank(\ro{\beta_L}{A_I}) + 1 = n$, so $\dim A_I^{\perp} = (n+1) - n = 1$, and $\RR\eta\containedin A_I^\perp$ forces $A_I^{\perp} = \RR\eta$.
The intersection $\Intersect_{s\in I}\overline{H_s}$ is the image of $A_I^\perp$ in $\PP(L_\RR)$, the single point $[\eta]$, which lies on $\partial\HH^n_L$ because $\eta$ is isotropic.
Since $\eta$ is isotropic and $L$ has signature $(1,n)$, the form induced on $\eta^{\perp}/\eta$ is negative definite of rank $n-1$; and $A_I\containedin\eta^{\perp}$, with $A_I/\RR\eta$ of dimension $n-1$, so $W_I$ acts on $\eta^{\perp}/\eta$ as the reflection group of $\Sigma_I$, which is euclidean by \longref{def:coxeter-system-type}.
:::

::: {.Corollary #cor:ideal-vertices-are-parabolic}

Sending an ideal vertex $[\eta]$ of $P$ to the set $I$ of all walls of $P$ through $[\eta]$ is a bijection from the ideal vertices of $P$ onto a set of parabolic subdiagrams of $\Sigma$ of rank $n-1$, and each such $\Sigma_I$ is maximal among the parabolic subdiagrams of $\Sigma$, in the sense of \longref{def:parabolic-subdiagram}.
:::

::: {.proof}
Let $[\eta]$ be an ideal vertex and $I$ the set of walls through it, so $A_I \containedin \eta^{\perp}$ and $\Sigma_I$ is parabolic of rank $n-1$ by \longref{prop:polytope-vertex-subdiagram}.
Suppose $\Sigma_J$ is parabolic with $J\supseteq I$.
Writing $r\leq 1$ for the dimension of the radical of $\ro{\beta_L}{A_J}$, one has $\dim A_J - r = \rank(\ro{\beta_L}{A_J})\leq n_-(L_\RR) = n$, so $\dim A_J\leq n+1$; and $\dim A_J = n+1$ would make $A_J = L_\RR$, whose form is nondegenerate of signature $(1,n)$ rather than negative semidefinite.
Hence $\dim A_J\leq n = \dim A_I$, so $A_J = A_I$ and every wall indexed by $J$ contains $A_I^{\perp} = \RR\eta$, that is, passes through $[\eta]$.
By the choice of $I$ this gives $J = I$.
:::

::: {.Remark}
### The boundary lattice of an ideal vertex

The lattice $\eta^{\perp L}/\eta$ produced at an ideal vertex by \longref{prop:polytope-vertex-subdiagram} is the quotient appearing in the mirror moves of \longref{def:mirror-move}, and its rank drops by two from that of $L$.
Reading the same construction one level up, at a $0$-cusp $[I]$ of a Baily--Borel compactification, the hyperbolic lattice on which the reflection group acts is $\overline{T}_I = I^{\perp T}/I$, and the isotropic lines of $\overline T_I$ are the rank-two isotropic sublattices of $T$ containing $I$; \longref{def:parabolic-subdiagram} records these as the $1$-cusps adjacent to $[I]$.
:::

## Covolume, compactness, and finite volume

::: {.Definition #def:covolume}

Let $\Gamma\leq\Isom(\HH^n_L)$ be a discrete subgroup.
Its **covolume** is the hyperbolic volume $\vol(\HH^n_L/\Gamma)$ of the quotient orbifold.
If $\Gamma$ is generated by the reflections in the walls of a Coxeter polytope $P$, then $P$ is a strict fundamental domain and $\vol(\HH^n_L/\Gamma) = \vol(P)$.
:::

::: {.Theorem #thm:coxeter-polytope-volume}
### Finite volume and compactness

Let $P\containedin\HH^n_L$ be a Coxeter polytope with finitely many walls and Coxeter--Vinberg diagram $\Sigma$.

1. $\vol(P) < \infty$ if and only if, in the projective model of \longref{def:hyperbolic-model}, the closure of $P$ is the convex hull of finitely many points of $\overline{\HH^n_L}$ --- equivalently, of the ordinary and ideal vertices supplied by \longref{prop:polytope-vertex-subdiagram}.

2. $P$ is compact if and only if $\vol(P)<\infty$ and $P$ has no ideal vertex; equivalently, if and only if the closure of $P$ in the projective model is the convex hull of finitely many ordinary vertices.
   By \longref{cor:ideal-vertices-are-parabolic} this is the condition that no parabolic subdiagram of $\Sigma$ of rank $n-1$ is cut out by a set of walls meeting in $\overline{P}$.

3. $P$ has infinite volume if and only if its closure in the projective model has a vertex outside $\overline{\HH^n_L}$.

These are Vinberg's criteria [@Vin67; @Vin85].
:::

::: {.Remark}

Criterion (1) is the condition Vinberg's algorithm tests at each stage (\longref{thm:vinberg-algorithm}, step 4), and \longref{prop:polytope-vertex-subdiagram} converts it into a statement about the subdiagrams of $\Sigma$: the algorithm terminates when every vertex of the cone bounded by the accepted roots is accounted for by an elliptic subdiagram of rank $n$ or a parabolic subdiagram of rank $n-1$.
:::

::: {.Corollary #cor:coxeter-simplex-volume}
### The simplex case

Suppose $\abs{S} = n+1$ and $P$ is a simplex, so that its $n+1$ vertices are cut out by the $n+1$ maximal proper subdiagrams $\Sigma_{S\sm\ts{s}}$, $s\in S$.
Then

1. $P$ is compact if and only if every $\Sigma_{S\sm\ts{s}}$ is elliptic;

2. $\vol(P) < \infty$ if and only if every $\Sigma_{S\sm\ts{s}}$ is elliptic or parabolic, the ideal vertices being those $s$ for which $\Sigma_{S\sm\ts{s}}$ is parabolic;

3. $\vol(P) = \infty$ if and only if some $\Sigma_{S\sm\ts{s}}$ is hyperbolic.
:::

::: {.Remark}
### Lannér's classification

The compact hyperbolic Coxeter simplices of \longref{cor:coxeter-simplex-volume}(1) were classified by Lannér.
In $\HH^2$ they are the triangles of \longref{ex:hyperbolic-triangle-groups} with $p,q,r$ all finite, of which there are infinitely many; in $\HH^3$ there are nine and in $\HH^4$ there are five.
:::

::: {.Example #ex:hyperbolic-triangle-groups}
### Triangle groups

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
The spherical solutions are $(2,2,r)$, $(2,3,3)$, $(2,3,4)$ and $(2,3,5)$, which are the rank-three entries $I_2(r)\times A_1$, $A_3$, $B_3$ and $H_3$ of \longref{thm:spherical-classification}; the euclidean solutions are $(2,3,6)$, $(2,4,4)$ and $(3,3,3)$, which are $\tilde G_2$, $\tilde C_2$ and $\tilde A_2$.
:::

::: {.Remark}
### Dihedral angles and the angle sum

Every dihedral angle of a Coxeter polytope is $\pi/m$ with $m\geq 2$ by \longref{def:coxeter-polytope}, hence at most $\pi/2$, in each of the three geometries: a Coxeter polytope is acute-angled.
What separates the three cases in \longref{ex:hyperbolic-triangle-groups} is the angle *sum* compared with the euclidean value $\pi$, and in higher rank the definiteness of the Gram form (\longref{def:coxeter-system-type}).
:::

## The cusps of the quotient

::: {.Remark}
### Ends of the quotient orbifold

Let $\Gamma$ be generated by the reflections in the walls of a finite-volume Coxeter polytope $P$.
Since $P$ is a strict fundamental domain, the quotient orbifold $\HH^n_L/\Gamma$ is homeomorphic to $P$, and its ends --- its **cusps** --- are the ideal vertices of $P$.
By \longref{prop:polytope-vertex-subdiagram} the cross-section of the cusp at $[\eta]$ is the euclidean orbifold $\EE^{\,n-1}/W_I$, where $\Sigma_I$ is the parabolic subdiagram of rank $n-1$ cutting out $[\eta]$; it is compact because $W_I$ is a euclidean reflection group of full rank, and its volume is finite, which is why an ideal vertex contributes finitely to $\vol(P)$.
A vertex lying outside $\overline{\HH^n_L}$ contributes an end of infinite volume.
:::

::: {.Remark}
### Invariants computed from the diagram

The data separating these cases --- the dimension, the number of vertices at infinity, the $f$-vector of the polytope, the covolume through the Euler characteristic in even dimension, and the growth series of the Coxeter system --- are computed from the Coxeter--Vinberg diagram alone by Guglielmetti's implementation of Vinberg's criteria [@Gug15].
The runs recorded for the lattices of this monograph are collected in the Computations section.
:::
