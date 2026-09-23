---
title: The fundamental chamber as a polyhedral cone
unit: method
status: reusable
tags:
  - vinberg
  - hyperbolic-geometry
  - polytopes
  - method
---

# The fundamental chamber as a polyhedral cone

**Provenance.** `notes/computations/fundamental-chamber-as-root-halfspace-cone.md`, landed 2026-08-20 from the cone cells of `archives/notebooks/Coble Lattice Invariants.ipynb` and the prototype `computations/scripts/components/coxeter-vinberg/Vinberg_L_2_1.py`.

\longref{thm:coxeter-type-and-geometry} presents the fundamental chamber of a hyperbolic Coxeter system by its half-spaces inside $\HH^{n}$, and \longref{thm:coxeter-polytope-volume} decides its volume from its ordinary and ideal vertices.
This page records the same object as a polyhedral cone in $L_\RR$, in the coordinates a polyhedral solver takes, and the form the volume criterion assumes when the input is that cone.

## The half-space presentation in coordinates

::: {.Construction #cons:chamber-cone}
### The chamber of a root set

Let $L$ be a hyperbolic lattice with bilinear form $\beta_L$ and Gram matrix $G$ in a chosen basis, and let $R = \ts{r_1,\dots,r_k}\subset L$ be a set of roots.
The cone they bound is
$$
C \da \ts{\, x\in L_\RR \;:\; \beta_L(r_i, x)\geq 0 \ \textfor i = 1,\dots,k \,}
\containedin L_\RR ,
$$
and $C\intersect\HH^n_L$ is the polytope $P$ of \longref{thm:coxeter-type-and-geometry}(3).
In coordinates the linear functional $\beta_L(r,-)$ is the row $r^{\mathsf T}G$, so the inequality defining the wall of $r$ is given by that row and not by the coordinate row of $r$.
:::

::: {.Remark}
### The cone has apex the origin

Every hyperplane $\beta_L(r_i,-) = 0$ passes through $0$, so $C$ is a cone with apex the origin.
When $C$ is pointed its vertex set as a polyhedron is $\ts{0}$, a point of the light cone and not of $\HH^n_L$, and it says nothing about $P$.
The vertices of $P$ that \longref{prop:polytope-vertex-subdiagram} describes appear in the cone as its extremal rays, and a criterion applied to $C$ must be stated in terms of those rays and of its lineality space.
:::

::: {.Proposition #prop:chamber-cone-criterion}
### The volume criterion on the cone

Let $L$ have signature $(1,n)$, let $C_L^+$ be the chosen component of the positive cone, and let $C$ be as in \longref{cons:chamber-cone}.
Then $\vol(C\intersect\HH^n_L) < \infty$ if and only if

1. every extremal ray generator $v$ of $C$ satisfies $v^2 \geq 0$;

2. all extremal ray generators lie in one half, that is, their pairings against a fixed timelike vector share a sign; and

3. the lineality space of $C$ is trivial.

Under these conditions $C \containedin \overline{C_L^+}$ and the closure of $C\intersect\HH^n_L$ in the projective model is the convex hull of the points determined by the extremal rays, which is criterion (1) of \longref{thm:coxeter-polytope-volume}.
The rays with $v^2 > 0$ are the ordinary vertices and the rays with $v^2 = 0$ the ideal vertices of \longref{prop:polytope-vertex-subdiagram}, so by \longref{thm:coxeter-polytope-volume}(2) the polytope is compact exactly when no extremal ray is isotropic.
:::

::: {.Remark}
### Why each hypothesis is separate

A cone containing a line meets both components of the positive cone, so (3) does not follow from (1).
A cone whose extremal rays are isotropic and timelike but distributed between the two components of $C_L$ is not contained in $\overline{C_L^+}$, which is (2).
Applied to the recorded runs, \longref{prop:chamber-cone-criterion} is what identifies the count reported as *vertices at infinity* in [the CoxIter results](coxiter-results-for-cusp-lattices.md) with the isotropic extremal rays of the cone, and the *non-cocompact with finite covolume* verdict recorded there with the presence of at least one of them.
:::

## Integral data of the chamber

::: {.Construction #cons:chamber-integral-data}
### Rays, facets, and integral points

From the presentation of \longref{cons:chamber-cone} one reads off:

- the extremal rays and the facets, with the incidence between them, the facets being the walls indexed by $R$;

- a primitive integral generator of each ray, obtained by clearing denominators by their least common multiple and dividing by the greatest common divisor of the resulting entries;

- the Hilbert basis of the monoid $C\intersect L$, that is, its unique minimal generating set as a monoid, together with generators for its integral points.

The last two are the data of the chamber as a subset of $L$, and are what a computation inside $C\intersect L$ requires.
:::

::: {.Remark}
### The recorded specimen

These cells were run over the $22$ roots of $\Phi_{(18,2,0)}$ in $U(2)\oplus E_8^{\oplus 2}$ ([root vectors and folded Sterk diagrams](root-vectors-and-folded-sterk-diagrams.md)) and over their restriction to the rank-$10$ invariant sublattice of the block-exchange involution.
The chamber there is full-dimensional, closed and non-compact, with the ray and integral-point data extracted through a Normaliz backend, and containment was checked by sampling $x\in C$ and testing $\beta_L(r_i,x)\geq 0$ for every root.
:::

## An exact invariant for a pair of walls

::: {.Definition #def:bond-invariant}
### The bond invariant of two roots

For roots $v,w$ of an integral lattice $L$ with $v^2, w^2 \neq 0$, set
$$
t(v,w) \da \frac{4\,\beta_L(v,w)^2}{v^2\, w^2} = 4\,g_{vw}^2 ,
$$
where $g_{vw}$ is the normalized pairing of \longref{def:coxeter-vinberg-diagram}.
For a bond of Coxeter exponent $m$ one has $t = 4\cos^2(\pi/m)$, so
$$
m = 2,\ 3,\ 4,\ 6,\ \infty
\quad\longleftrightarrow\quad
t = 0,\ 1,\ 2,\ 3,\ 4 ,
$$
and $t > 4$ is the ultraparallel case, with $t = 4\cosh^2 d$ for $d$ the distance between the mirrors (\longref{def:hyperbolic-model}).
:::

::: {.Remark}
### The bond invariant is exact and independent of the norms

For simple roots normalized to $\alpha_s^2 = -2$ the normalized pairing is already the halved Gram entry, $g_{st} = G(M)_{st}/2$.
The diagrams of this monograph mix norms $-2$ and $-4$ (\longref{def:2elementary-roots}), where $g_{vw}$ involves $\sqrt{v^2w^2}$ and is irrational already for $\beta_L(v,w) = \pm1$.
Its square $t(v,w)$ requires no square root: $\beta_L(v,w)$, $v^2$ and $w^2$ are integers, so $t\in\QQ$, and every bond of a Coxeter--Vinberg diagram of an integral lattice is decided by exact rational arithmetic.
The value $t = 4\cos^2(\pi/5) = (3+\sqrt5)/2$ is irrational, so a bond of exponent $5$ occurs between no two roots of an integral lattice, and the diagrams recorded here carry labels $2, 3, 4$ and $\infty$.
:::

::: {.Warning}
### Squares and isotropy are integer questions

The form on $L$ takes integer values, so equality of vectors, vanishing of $\beta_L(v,w)$, the value of $v^2$ and the isotropy of a ray generator are decided exactly.
A numerical tolerance applied to any of them can only lose information.
:::

## A simple system is not a root orbit

::: {.Remark}
### What closure under reflections produces

Closing a set of roots under the reflections in the roots it already holds produces the $W(L)$-orbit of the seed, hence a subset of the root system of $L$.
A simple system (\longref{def:weyl-chamber}) is a set of roots whose mirrors are the walls of a single chamber, and the two coincide only when $W(L)$ is finite.
Vinberg's algorithm produces a simple system by admitting a candidate root only when it pairs non-negatively with every accepted root (\longref{thm:vinberg-algorithm}), so the cone $C$ shrinks as roots are accepted, while closure under reflections makes the root set grow.
For an infinite reflection group the orbit is infinite and the simple system is finite.
:::

Related: [reflection groups and Vinberg](../compactifications/reflection-groups-and-vinberg.md), [hyperbolic Coxeter polytopes](../compactifications/hyperbolic-coxeter-polytopes.md), [CoxIter results for cusp lattices](coxiter-results-for-cusp-lattices.md), [Sterk root counts and computed chambers](sterk-root-counts-and-computed-chambers.md), [lattice and diagram conventions](../reference-tables/lattice-and-diagram-conventions.md).
