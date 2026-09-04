# Folding of simply-laced Coxeter–Dynkin diagrams

**Source**: https://en.wikipedia.org/wiki/Coxeter%E2%80%93Dynkin_diagram, section "Geometric folding" **Retrieved**: 2025-07-26 (transcribed 2026-08-20 from the full-article capture made by `literature/tools/webpage_to_markdown.py`) **Citation Key**: `wikipedia_coxeter_dynkin_2025` **Revision**: oldid 1290398091 (last edited 14 May 2025), permanent link https://en.wikipedia.org/w/index.php?title=Coxeter%E2%80%93Dynkin_diagram&oldid=1290398091

**Status in this repository**: **not owned.** `coxeter_diagrams.sage` computes the diagram automorphism group (`CoxeterDiagrams.ParentMethods.Aut`, and `elliptic_subdiagram_orbits` over it), which is the input a folding needs, but there is no quotient construction: given a diagram and an element of its `Aut`, nothing returns the folded diagram.
The table below is the oracle such a construction would be checked against.

## What folding is

A simply-laced Coxeter–Dynkin diagram — finite, affine, or hyperbolic — that carries a diagram symmetry can be quotiented by that symmetry, giving a new, generally multiply-laced diagram.
Geometrically this is an orthogonal projection of the corresponding uniform polytope or tessellation.

In the $D_4 \to G_2$ folding, the edge of $G_2$ points from the class of the three outer nodes (valence 1) to the class of the central node (valence 3). $E_8$ folds into two copies of $H_4$, the second scaled by the golden ratio $\tau$.

Notably: **every finite simply-laced diagram folds to $I_2(h)$**, where $h$ is the Coxeter number.
That folding is the projection to the Coxeter plane.

## Finite types

$\varphi_A : A_\Gamma \to A_{\Gamma'}$

| $\Gamma$ | $\Gamma'$ | folding description |
| --- | --- | --- |
| $I_2(h)$ | $\Gamma(h)$ | dihedral folding |
| $B_n$ | $A_{2n}$ | $(I, s_n)$ |
| $B_n$ | $D_{n+1}$, $A_{2n-1}$ | $(A_3, \pm\varepsilon)$ |
| $F_4$ | $E_6$ | $(A_3, \pm\varepsilon)$ |
| $H_4$ | $E_8$ | $(A_4, \pm\varepsilon)$ |
| $H_3$ | $D_6$ |  |
| $H_2$ | $A_4$ |  |
| $G_2$ | $A_5$ | $(A_5, \pm\varepsilon)$ |
| $G_2$ | $D_4$ | $(D_4, \pm\varepsilon)$ |

## Affine types

$\varphi : A_{\Gamma^{+}} \to A_{\Gamma'^{+}}$

| $\Gamma$ | $\Gamma'$ | folding description |
| --- | --- | --- |
| $\tilde A_{n-1}$ | $\tilde A_{kn-1}$ | locally trivial |
| $\tilde B_n$ | $\tilde D_{2n+1}$ | $(I, s_n)$ |
| $\tilde B_n$ | $\tilde D_{n+1}$, $\tilde D_{2n}$ | $(A_3, \pm\varepsilon)$ |
| $\tilde C_n$ | $\tilde B_{n+1}$, $\tilde C_{2n}$ | $(A_3, \pm\varepsilon)$ |
| $\tilde C_n$ | $\tilde C_{2n+1}$ | $(I, s_n)$ |
| $\tilde C_n$ | $\tilde A_{2n+1}$ | $(I, s_n)$ and $(I, s_0)$ |
| $\tilde C_n$ | $\tilde A_{2n}$ | $(A_3, \varepsilon)$ and $(I, s_0)$ |
| $\tilde C_n$ | $\tilde A_{2n-1}$ | $(A_3, \varepsilon)$ and $(A_3, \varepsilon')$ |
| $\tilde C_n$ | $\tilde D_{n+2}$ | $(A_3, -\varepsilon)$ and $(A_3, -\varepsilon')$ |
| $\tilde C_2$ | $\tilde D_5$ | $(I, s_1)$ |
| $\tilde F_4$ | $\tilde E_6$, $\tilde E_7$ | $(A_3, \pm\varepsilon)$ |
| $\tilde G_2$ | $\tilde D_6$, $\tilde E_7$ | $(A_5, \pm\varepsilon)$ |
| $\tilde G_2$ | $\tilde B_3$, $\tilde F_4$ | $(B_3, \pm\varepsilon)$ |
| $\tilde G_2$ | $\tilde D_4$, $\tilde E_6$ | $(D_4, \pm\varepsilon)$ |

The source's layout groups several $\Gamma'$ rows under one $\Gamma$ entry; the rows are unrolled above, and the folding-description column is the source's own notation for the symmetry being quotiented by.
Hyperbolic foldings exist too, and the source shows them only as a figure — no table, so none is transcribed here.
