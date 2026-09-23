---
title: Explicit root vectors and the folded Sterk diagrams
unit: computation
status: computed
tags:
  - roots
  - folding
  - coxeter-diagrams
  - sterk
---

# Explicit root vectors and the folded Sterk diagrams

**Provenance.** `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/computational-research/canonical/notebooks/Lattices and Coxeter Diagrams DZG.ipynb`, `.../reports/rank-checks/*.rtf`, and the root correspondence tables A.3.2a/b of `/home/dzack/gitclones/diss/000-writing/.archive/source_material/thesis-appendix-tables-figures.md`. The two sources agree.
Absent from the dissertation, which states only the generic fact that roots have norm $-2$ or $-4$ with divisibility 2.

::: {.Remark}
## Why this is the highest-value computational note for this project

`content_pandoc/sections/Open_Problems/Open_Problems.md` poses, as an open conjecture, the horizontal folding involution $\theta$ with $\lkt^\theta \cong T_{\Co}$ and $\lkt^{-\theta}\cong S_{\Co}$, and explicitly demands the $22\times22$ matrix of $\theta$ and the horizontal folding of the $(18,0,0)_1$ diagram.
Those are stated in exactly the coordinates tabulated below.
:::

## Ambient lattice and notation

Work in $L_{20,2,0} = U \oplus U(2) \oplus E_8 \oplus E_8$, with $e,f$ the $U$ basis, $e',f'$ the $U(2)$ basis, $\alpha_i$ and $\tilde\alpha_i$ the simple roots of the two $E_8$ summands, and $w_i, \tilde w_i$ the corresponding dual weights.

## The $(18,2,0)_1$ diagram: 22 roots

$\Phi_{(18,2,0)}$, in $U(2)\oplus E_8^{\oplus2}$.
Norms are $-2$ for $v_1 \ldots v_{20}$ and $-4$ for $v_{21}, v_{22}$.

| Node | Root | Node | Root |
| --- | --- | --- | --- |
| $v_1$ | $\tilde\alpha_8$ | $v_{12}$ | $\tilde\alpha_3$ |
| $v_2$ | $e'+f'+w_1+\tilde w_8$ | $v_{13}$ | $\tilde\alpha_4$ |
| $v_3$ | $\alpha_1$ | $v_{14}$ | $\tilde\alpha_5$ |
| $v_4$ | $\alpha_3$ | $v_{15}$ | $\tilde\alpha_6$ |
| $v_5$ | $\alpha_4$ | $v_{16}$ | $\tilde\alpha_7$ |
| $v_6$ | $\alpha_5$ | $v_{17}$ | $e'+\tilde w_8$ |
| $v_7$ | $\alpha_6$ | $v_{18}$ | $\alpha_2$ |
| $v_8$ | $\alpha_7$ | $v_{19}$ | $e'+w_8$ |
| $v_9$ | $\alpha_8$ | $v_{20}$ | $\tilde\alpha_2$ |
| $v_{10}$ | $e'+f'+w_8+\tilde w_1$ | $v_{21}$ | $f'-e'$ |
| $v_{11}$ | $\tilde\alpha_1$ | $v_{22}$ | $5e'+3f'+2w_2+2\tilde w_2$ |

## The $(18,0,0)_1$ diagram: 19 roots

$\Phi_{(18,0,0)}$, in $U \oplus E_8^{\oplus2}$.
All 19 roots have norm $-2$.

| Node | Root | Node | Root |
| --- | --- | --- | --- |
| $w_1$ | $\alpha_1$ | $w_{11}$ | $\tilde\alpha_8$ |
| $w_2$ | $\alpha_3$ | $w_{12}$ | $\tilde\alpha_7$ |
| $w_3$ | $\alpha_4$ | $w_{13}$ | $\tilde\alpha_6$ |
| $w_4$ | $\alpha_5$ | $w_{14}$ | $\tilde\alpha_5$ |
| $w_5$ | $\alpha_6$ | $w_{15}$ | $\tilde\alpha_4$ |
| $w_6$ | $\alpha_7$ | $w_{16}$ | $\tilde\alpha_3$ |
| $w_7$ | $\alpha_8$ | $w_{17}$ | $\tilde\alpha_1$ |
| $w_8$ | $w_8+e$ | $w_{18}$ | $\alpha_2$ |
| $w_9$ | $f-e$ | $w_{19}$ | $\tilde\alpha_2$ |
| $w_{10}$ | $\tilde w_8+e$ |  |  |

$(18,0,0)_1 = U\oplus E_8^{\oplus2}$ is the lattice to which the Coble cusps are claimed to correspond under $\tilde\eta$; see [the cusp-correspondence morphism chain](../coble-moduli/cusp-correspondence-morphism-chain.md).

## The folded diagrams

Folding is performed by summing a root with its image under the relevant involution, $s = v + \sigma(v)$.

::: {.Construction}
### Sterk 1: 12 nodes, all of norm -4

$s^1_k = v_k + v_{k+8}$, together with $s^1_{10} = v_{21}$ and $s^1_{11} = v_{22}$.
:::

::: {.Construction}
### Sterk 2: 10 nodes, norms $(-4^{\times 8}, -2, -4)$

$s^2_k = w_k + w_{18-k}$, together with $s^2_9 = w_9$ and $s^2_{10} = w_{18}+w_{19}$.
:::

::: {.Construction}
### Sterk 3: 12 nodes, norms $(-2,-4,-4,-4,-4,-4,-4,-4,-2,-4,-4,-4)$

This case is reflection-twisted rather than a plain permutation.
Set
$$
w_\alpha(x) = x + \tfrac12\inner{v_{22}}{x}\, v_{22},
\qquad
I(x) = x + w_\alpha(x),
$$
so that $s^3_{11} = I(v_{20})$ and $s^3_{12} = I(v_{18})$.
:::

::: {.Construction}
### Sterk 4: 11 nodes, norms $(-2,-4,-4,-4,-4,-4,-4,-4,-2,-4,-4)$

The notebook records a genuine subtlety here: $s^4_{12} = v_{22}+v_{21}$ is invariant under the involution but **is not a root**, and is therefore dropped.
This is why Sterk 4 has 11 nodes rather than 12.
:::

::: {.Construction}
### Sterk 5: 14 nodes, norms $(-4^{\times 8}, -2,-2,-2,-2, -4,-4)$

$s^5_k = v_{2k-2} + 2 v_{2k-1} + v_{2k}$.
:::

::: {.Remark}
### Independent verification against Sterk's published basis

Each folded diagram is cross-checked against Sterk's own published root basis (in terms of $\alpha'_i, e, f, e', f', w'_i$), producing the same norm multisets in permuted order.
This is an independent confirmation that the folding construction reproduces Sterk's diagrams, and is the strongest surviving validation in the corpus.
:::

## Eigenspace ranks of the Sterk involution

On the 22-dimensional root space, the $+1$-eigenspace ranks are 12, 12, 12, 14 for Sterk 1, 3, 4, 5 respectively (Sterk 2 not recorded).
The induced root-image matrices have shape $(20,12)$ or $(20,14)$ and are asserted to have rank 10.

## Rank checks

The Gram matrix is reconstructed from a Coxeter diagram by
$$
\inner{v_i}{v_j} = \sqrt{v_i^2\, v_j^2}\,\cos\!\left(\frac{\pi}{m_{ij}+2}\right),
$$
with $\infty$-labelled edges handled as $\sqrt{v_i^2 v_j^2}$.

| Case | Norms | Asserted rank |
| --- | --- | --- |
| Coxeter $(18,2,0)$, 22 roots | $(-2^{\times20}, -4, -4)$ | 18 |
| Coxeter Sterk 3, 12 roots | $(-4,-4,-4,-4,-2,-4,-4,-2,-4,-4,-4,-4)$ | 10 |
| Folded Sterk 3 | full Gram of $U(2)\oplus E_8\oplus E_8$ in Bourbaki basis, folded along the diagonal symmetry | - |

## An unresolved discrepancy in the $(18,2,0)$ diagram

**Provenance for this section.** An author annotation in `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/enriques-research/canonical/my_enriques_notes/900_appendix.tex`, attached to a hand-drawn reproduction of Scattone's Figure 6.3.1:

> Note: this is slightly different to $(18,2,0)$ in AET19, very mysterious!

::: {.Question}
### Do Scattone and AET19 give the same diagram?

Scattone's Figure 6.3.1 is the Coxeter diagram of the full reflection group of $\gens{-4}\oplus U \oplus E_8^{\oplus2}$, reached through his $F_4$ boundary computation.
AET19 gives a Coxeter diagram for the lattice with invariants $(18,2,0)$.
These should be the same diagram, and the author recorded that they are not, without resolving how they differ or which is right.
:::

This is the only unresolved research observation found in that whole source tree, and it bears directly on the table of 22 roots above, which is written in the $(18,2,0)$ presentation.
Anything derived from $\Phi_{(18,2,0)}$, including the folded Sterk diagrams and the $\theta$ matrix the open problems demand, inherits whatever the discrepancy is.
Settling it is a prerequisite, not a footnote.

::: {.Remark}
### A related contradiction, resolved

Two blocks of the same archived outline disagree about which 0-cusps of $\fentwo$ carry toroidal rather than strictly semitoroidal compactifications: one says cusps 2 and 4, the other says cusps 2 and 3. The dissertation settles it as **cusps 2 and 4**, together with the adjacent 1-cusps and 1-cusp 35, citing AEGS Thm.
5.9. This matters here because the Coble 0-cusp is claimed to be Sterk cusp 2, which is toroidal under either reading; see [the cusp-correspondence morphism chain](../coble-moduli/cusp-correspondence-morphism-chain.md).
:::

Related: [CoxIter results for cusp lattices](coxiter-results-for-cusp-lattices.md), [computational toolchain and recipe](computational-toolchain-and-recipe.md), [lattice and diagram conventions](../reference-tables/lattice-and-diagram-conventions.md), [cusp-correspondence morphism chain](../coble-moduli/cusp-correspondence-morphism-chain.md).
