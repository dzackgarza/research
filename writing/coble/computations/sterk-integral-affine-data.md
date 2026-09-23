---
title: Integral-affine edge-length data for the Sterk cusps
unit: computation
status: partial
tags:
  - integral-affine
  - sterk
  - dlt-models
---

# Integral-affine edge-length data for the Sterk cusps

**Provenance.** `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/computational-research/canonical/notebooks/Sterk IAS Plotting.ipynb`. This is the only place in the corpus with concrete integral-affine output.
Absent from the dissertation, which treats integral-affine structures theoretically without tabulating edge lengths.

## Edge-length vectors and polygon symmetry

For each cusp, $\ell$ is the ordered vector of integral-affine edge lengths of the boundary polygon $P$, obtained by solving $\Sum_i \ell_i v_i = 0$ over the ordered primitive boundary directions $v_i \in \ZZ^2$.

| Cusp | $\ell$ | $\Aut(P)$ | Generator |
| --- | --- | --- | --- |
| Sterk 1 | $(1,2,1,2,1,0,1,2,1,2,1,2,1,0,1,2,6,6,6,6)$ | $C_2$ | $\begin{psmallmatrix}-1&0\\0&-1\end{psmallmatrix}$ |
| Sterk 2 | $(4,1,2,1,2,1,2,1,2,0,2,1,2,1,2,1,2,1,4)$ | $C_2$ | $\begin{psmallmatrix}-1&0\\0&1\end{psmallmatrix}$ |
| Sterk 3 | $(2,2,2,2,2,2,2,4,2,4,2,2,2,2,2,2,24,6,30,6)$ | $C_2$ | $\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$ |

Sterk 4 and Sterk 5 were never plotted.

## Boundary direction vectors

- For $(18,2,0)$: 16 primitive directions running from $(1,-1)$ around to $(1,-2)$, plus 4 surgery directions.

- For $(18,0,0)$: 17 directions, including $(-1,4), (-2,5), (-2,3), (-2,1), (-2,-1), (-2,-3), (-2,-5), (-1,-4)$.

$(18,0,0)$ is the lattice to which the Coble cusps are claimed to correspond, so this direction list is the natural starting point for the Coble integral-affine structure; see [[cusp-correspondence-morphism-chain]].

::: {.Remark}
### Recorded defect: a failing rank assertion

Four consecutive "project-up" cells fail as saved, on `assert all_As.rank() == 10` while the printed rank is 11. This is an unresolved discrepancy, not a transient error, and it blocks the Sterk 4 and Sterk 5 plots.
Whoever resumes this work should treat the rank-10 expectation itself as the thing under test: the $+1$-eigenspace ranks recorded in [[root-vectors-and-folded-sterk-diagrams]] are 12, 12, 12, 14, and the passage from those to a rank-10 image is the step that is failing.
:::

## The plotting procedure

::: {.Construction}
### From directions to a polygon with symmetry

1. Fix the ordered primitive boundary directions $v_i \in \ZZ^2$.

2. Solve $\Sum \ell_i v_i = 0$ by `A.right_kernel()`, then rescale for evenness and divisibility.

3. Walk the polygon by $p_{i+1} = p_i + \ell_i v_i$.

4. Place surgery triangles: `edge_len = gcd(v)`, base offset $|\lfloor \text{edge\_len}/2\rfloor - \lfloor \text{surg\_size}/2\rfloor|$.

5. Recentre at the centroid and call `restricted_automorphism_group(output="matrix")` to obtain $\Aut(P)$.
:::

Related: [[computational-toolchain-and-recipe]], [[coxiter-results-for-cusp-lattices]].
