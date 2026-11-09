---
unit: computation
status: computed
tags:
  - roots
  - folding
  - coxeter-diagrams
  - sterk
notes: |-
  Provenance: the archived "Lattices and Coxeter Diagrams DZG" notebook, rank-check reports, and root-correspondence tables A.3.2a/b in the archived thesis tables and figures. These sources agree.
  Provenance: an author annotation in the archived Enriques appendix, attached to a hand-drawn reproduction of Scattone's Figure 6.3.1.
---

# Explicit root vectors and the folded Sterk diagrams {#sec-root-vectors-and-folded-sterk-diagrams}

## Coordinates

::: {.notation title="Coordinates on $L_{20,2,0}$"}

Work in $L_{20,2,0} = U \oplus U(2) \oplus E_8 \oplus E_8$, with $e,f$ the $U$ basis, $e',f'$ the $U(2)$ basis, $\alpha_i$ and $\tilde\alpha_i$ the simple roots of the two $E_8$ summands, and $w_i, \tilde w_i$ the bases of the dual lattices $E_8^\# = E_8$ dual to them.
:::

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

Under $\tilde\eta$ the Coble $0$-cusp maps to the $0$-cusp $(18,0,0)_1 = U\oplus E_8^{\oplus2}$ (@lem:cusp_map_dP).

## The folded diagrams

Folding is performed by summing a root with its image under the relevant involution, $s = v + \sigma(v)$.

::: {.construction title="Sterk 1: 12 nodes, all of norm -4"}

The involution is $v_k\leftrightarrow v_{k+8}$ for $1\le k\le 8$, $v_{17}\leftrightarrow v_{19}$, $v_{18}\leftrightarrow v_{20}$, with $v_{21}$ and $v_{22}$ fixed; it preserves the products of @prop:eighteen-two-zero-vinberg-diagram.
The nodes are $s^1_k = v_k + v_{k+8}$ for $1\le k\le 8$, $s^1_9 = v_{17}+v_{19}$, $s^1_{10} = v_{18}+v_{20}$, $s^1_{11} = v_{21}$ and $s^1_{12} = v_{22}$.
Their Gram matrix has rank $10$.
:::

::: {.construction title="Sterk 2: 10 nodes, norms $(-4^{\times 8}, -2, -4)$"}

$s^2_k = w_k + w_{18-k}$, together with $s^2_9 = w_9$ and $s^2_{10} = w_{18}+w_{19}$.
:::

::: {.construction title="Sterk 3: 12 nodes, norms $(-2,-4,-4,-4,-4,-4,-4,-4,-2,-4,-4,-4)$"}

This case is reflection-twisted rather than a plain permutation.
Set
$$
w_\alpha(x) = x + \tfrac12\inner{v_{22}}{x}\, v_{22},
\qquad
I(x) = x + w_\alpha(x),
$$
so that $s^3_{11} = I(v_{20})$ and $s^3_{12} = I(v_{18})$.
:::

::: {.construction title="Sterk 4: 11 nodes, norms $(-2,-4,-4,-4,-4,-4,-4,-4,-2,-4,-4)$"}

$s^4_{12} = v_{22}+v_{21}$ is invariant under the involution.
It has square $v_{21}^2 + v_{22}^2 + 2(v_{21},v_{22}) = -4-4+8 = 0$ (@prop:eighteen-two-zero-vinberg-diagram), so it is not a root and is dropped.
:::

::: {.construction title="Sterk 5: 14 nodes, norms $(-4^{\times 8}, -2,-2,-2,-2, -4,-4)$"}

$s^5_k = v_{2k-2} + 2 v_{2k-1} + v_{2k}$.
:::

::: {.example #ex:folded-sterk-norm-multisets title="Squares of the folded nodes"}

For $j = 1,\dots,5$, the multiset of squares of the nodes of the folded Sterk $j$ diagram above is the multiset of squares of the roots of the diagram of $W_{\eta_j}$ in @prop:sterk-reflection-subgroup-diagrams:

| Diagram | Nodes | Squares |
| --- | --- | --- |
| Sterk 1 | 12 | $12\times(-4)$ |
| Sterk 2 | 10 | $9\times(-4)$, $1\times(-2)$ |
| Sterk 3 | 12 | $10\times(-4)$, $2\times(-2)$ |
| Sterk 4 | 11 | $9\times(-4)$, $2\times(-2)$ |
| Sterk 5 | 14 | $10\times(-4)$, $4\times(-2)$ |
:::

## Eigenspace ranks of the Sterk involution

On the 22-dimensional root space, the $+1$-eigenspace ranks are 12, 12, 12, 14 for Sterk 1, 3, 4, 5 respectively.

## Rank checks

::: {.example #ex:gram-ranks-of-root-systems title="Ranks of Gram matrices"}

| Root set | Squares | Rank of the Gram matrix |
| --- | --- | --- |
| $v_1,\dots,v_{22}$ of $\Phi_{(18,2,0)}$ | $(-2^{\times20}, -4, -4)$ | 18 |
| roots of Sterk's diagram of $W_{\eta_j}$, $j = 1,2,3,4$ [@Ste91, §§4.3.5--4.3.8] | as in @ex:folded-sterk-norm-multisets | 10 |

The Gram matrix of $v_1,\dots,v_{22}$ is the one given by the products in the proof of @prop:eighteen-two-zero-vinberg-diagram.
The vectors $v_1,\dots,v_{22}$ span a sublattice of rank $18$ of $U(2)\oplus E_8^{\oplus2}$.
:::

## Comparison with the published $(18,2,0)$ diagram

::: {.proposition #prop:eighteen-two-zero-vinberg-diagram title="The 22 roots give the Vinberg diagram of $(18,2,0)$"}

Put $\epsilon_i = -1$ for $i\in\theset{2,10,17,19,21,22}$ and $\epsilon_i = 1$ otherwise.
Then $(\epsilon_i v_i,\epsilon_j v_j)\geq 0$ for all $i\neq j$, and the Coxeter diagram of $\epsilon_1v_1,\ldots,\epsilon_{22}v_{22}$ is the diagram of the lattice $(18,2,0)$ in [@AE22, Fig. 4].
:::

::: {.proof}

The nonzero products $(v_i,v_j)$ with $i<j$ are as follows.

| Value | Pairs $\theset{i,j}$ |
| --- | --- |
| $1$ | $\theset{1,16}$, $\theset{3,4}$, $\theset{4,5}$, $\theset{5,6}$, $\theset{5,18}$, $\theset{6,7}$, $\theset{7,8}$, $\theset{8,9}$, $\theset{11,12}$, $\theset{12,13}$, $\theset{13,14}$, $\theset{13,20}$, $\theset{14,15}$, $\theset{15,16}$ |
| $-1$ | $\theset{1,2}$, $\theset{1,17}$, $\theset{2,3}$, $\theset{9,10}$, $\theset{9,19}$, $\theset{10,11}$ |
| $2$ | $\theset{17,21}$, $\theset{19,21}$ |
| $-2$ | $\theset{18,22}$, $\theset{20,22}$ |
| $4$ | $\theset{21,22}$ |

Each pair with a negative product contains exactly one index $i$ with $\epsilon_i = -1$, and each pair with a positive product contains zero or two such indices, so the signs $\epsilon_i$ make every product nonnegative.
With the conventions of [@AE22, Sec. 3A], two $(-2)$-roots with product $1$ are joined by a single edge, a $(-2)$-root and a $(-4)$-root with product $2$ by a double edge, and the two $(-4)$-roots $v_{21}, v_{22}$ with product $4$ by a thick edge.
The diagram is therefore the $16$-cycle
$$
v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_{10}, v_{11}, v_{12}, v_{13}, v_{14}, v_{15}, v_{16},
$$
the four vertices $v_{17}, v_{18}, v_{19}, v_{20}$ joined by single edges to $v_1, v_5, v_9, v_{13}$, and the two black vertices $v_{21}, v_{22}$ joined to each other by a thick edge, with $v_{21}$ joined by double edges to $v_{17}, v_{19}$ and $v_{22}$ to $v_{18}, v_{20}$.
This is the $(18,2,0)$ diagram of [@AE22, Fig. 4], with $v_1, v_5, v_9, v_{13}$ the four corners of its square.
:::

The Coxeter diagram of [@AET23, Fig. 1] has $24$ nodes and describes a fundamental chamber of $W(N)$ for $N = U\oplus E_8^{\oplus 2}\oplus A_1$, of rank $19$ and type $(19,1,1)$ [@AET23, §4].

::: {.proposition #prop:aegs-toroidal-cusps title="Toroidal cusps of the stable-pair compactification"}

The normalization of $\ofentwo$ is semitoroidal for the semifans $\mathfrak F^k$, $k = 1,\dots,5$, of [@AEGS25, §5.2].
It is toroidal over the $0$-cusps $2$ and $4$, over the $1$-cusps adjacent to them and over the $1$-cusp $35$, and strictly semitoroidal over the remaining cusps [@AEGS25, Thm. 5.9].
:::

Related: [CoxIter results for cusp lattices](#sec-coxiter-results-for-cusp-lattices), [computational toolchain and recipe](#sec-computational-toolchain-and-recipe), [lattice and diagram conventions](#sec-lattice-and-diagram-conventions), [cusp-correspondence morphism chain](#sec-cusp-correspondence-morphism-chain).
