---
unit: method
status: reusable
tags:
  - sagemath
  - coxiter
  - vinberg
  - method
notes: |-
  Provenance: originally the archived computational-research Sage-script and notebook tree, which has since been trashed. Nothing of this appears in the dissertation.
  Current location: most files survive in the research tree; reusable modules are in the computations scripts collection, notebooks in the notebook archive, and the empty vinal, AlVin, and VinbergsAlgorithmNF directories remain unvendored.
---

# Toolchain and recipe for a hyperbolic 2-elementary lattice {#sec-computational-toolchain-and-recipe}



## The recipe

::: {.construction title="Seven steps, from a lattice to its cusps and integral-affine data"}

1. **Build the lattice** from $U$, $U(2)$, $E_8$, $E_8(2)$, $\generators{\pm2}$ blocks.
   Confirm 2-elementarity and read off $(r,a,\delta)$, computing $\delta$ by the diagonal test on the discriminant quadratic form.

2. **Find the roots** by Vinberg's algorithm, or write them down by hand and verify with `root_intersection_matrix`, which asserts that the Gram matrix is symmetric with diagonal contained in $\{-2,-4\}$.
   The polyhedral presentation of the resulting chamber, and the test deciding whether the accepted roots bound a finite-volume hyperbolic polyhedron, are in [fundamental chamber polyhedra](#sec-fundamental-chamber-polyhedra).

3. **Run CoxIter** on the diagram for the $f$-vector, a finite-covolume certificate, the count of vertices at infinity, and the growth series.

4. **Fold along an explicit involution.** Realize $\sigma$ either as a permutation of root labels or as a product of reflections; assert $\sigma^2 = \id$; take $s = v + \sigma(v)$, or $x + w_\alpha(x)$ in the reflection-twisted cases.
   The rank of the $+1$-eigenspace is the number of independent edge-length parameters.
   Check that each $s$ is actually a root: see the Sterk 4 case in [root vectors and folded Sterk diagrams](#sec-root-vectors-and-folded-sterk-diagrams), where an invariant vector is not a root and must be dropped.

5. **Enumerate maximal elliptic subdiagrams up to symmetry.** All vertex subsets, filtered to connected with definite Gram; maximal under inclusion via `Poset(subgraphs, subset).maximal_elements()`; then `Aut(Gamma).orbit(vertices, action="OnSets")`, canonicalizing each orbit as a sorted tuple of tuples in a set; label the representative by `M.is_similar(M_type)` against `get_all_rank_n_types(n)`, joining components with direct sums.
   The definiteness tests that decide each type, and the monotonicity that prunes the subset search, are in [lattice algorithms by signature](#sec-lattice-algorithms-by-signature).

6. **Enumerate isotropic orbits** with the function `vector_orbit_representatives` of `sage-indefinite-port`, using $\div(v)$ and $v^\perp/v$ as separating invariants, matched against the table of $2$-elementary lattices keyed by $(r,a,\delta)$ [@Nik79b].
   The algorithm this invokes, its hypotheses, and the Tits building it computes are in [isotropic orbits and Tits buildings](#sec-isotropic-orbits-and-tits-buildings).

7. **Build the integral-affine structure** by the polygon-walking procedure in [Sterk integral-affine data](#sec-sterk-integral-affine-data).
:::

## The reusable modules

| Path (relative to `sage-scripts/`) | What it provides |
| --- | --- |
| `init.sage` | The environment: $\ZZ$, $U$, $U(2)$, $A_n/D_n/E_n$ to rank 20 and their twists, $E_{10}$, $E_{10}(2)$; the lattices $\sdp, \tdp, \sen, \ten, T_{\Co}, S_{\Co}, L_{\Nik}^{\pm}$; a `two_elementary_lattices` registry keyed by $(r,a,\delta)$; the three K3 involutions $\Idp, \Ien, I_{\Nik}$ as lattice homomorphisms on $U^3\oplus E_8^{\oplus2}$; `get_isotrop_type`; `root_intersection_matrix`; node-position data for all five Sterk diagrams; Sterk's five isotropic vectors with divisibility and isometry assertions; a `vinberg_algorithm` method delegating to `vinal` |
| Isometry utility module | A complete catalogue of Coxeter and Dynkin Gram matrices and graphs: $A_n, A_n(2), B_n, B_n(2), C_n, C_n(2), D_n, D_n(2), E_{6,7,8}$ and twists, $G_2, G_2(2), F_4, H_3, H_3(2), H_4$, plus all affine types and their 2-twists; `get_all_rank_n_types(n)`, `get_coxeter_label_connected`, `is_lanner`. This is the lookup table behind the subdiagram type labels |
| Coxeter graph module | A `CoxeterGraph(Graph)` class: matrix-graph conversion, `is_elliptic_matrix` / `is_parabolic_matrix`, connected-subgraph enumeration, ADE type labelling, colour conventions for $-2$ and $-4$ nodes |
| `hyperbolic_diagrams.sage` | Poincare-disc and upper-half-plane figure generation |

Related: [CoxIter results for cusp lattices](#sec-coxiter-results-for-cusp-lattices), [root vectors and folded Sterk diagrams](#sec-root-vectors-and-folded-sterk-diagrams), [Coble lattice isotropic candidates](#sec-coble-lattice-isotropic-candidates), [Sterk integral-affine data](#sec-sterk-integral-affine-data), [lattice algorithms by signature](#sec-lattice-algorithms-by-signature), [fundamental chamber polyhedra](#sec-fundamental-chamber-polyhedra), [isotropic orbits and Tits buildings](#sec-isotropic-orbits-and-tits-buildings).
