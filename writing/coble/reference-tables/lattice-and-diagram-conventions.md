---
title: Lattice length table and Coxeter-Vinberg diagram conventions
unit: reference
status: reference
tags:
  - lattices
  - discriminant-forms
  - coxeter-vinberg
  - conventions
---

# Lattice length table and Coxeter-Vinberg diagram conventions

**Provenance.** `/home/dzack/gitclones/diss/000-writing/.archive/source_material/thesis-appendix-tables-figures.md`, sections A.1.3, A.2.1, A.2.2, A.4. That file cites its own sources as `1.8_Discriminant_Bilinear_Quadratic_Forms.tex`, `1.30.2_Coxeter-Vinberg_Diagrams.tex` and `1.28_Root_lattices_and_labeling_Conventions.tex`, all in the same archive.
None of these tables appear in the dissertation.

This project defines the length $\ell(L)$ in `content_pandoc/sections/Lattices_and_Moduli/Discriminant_Forms_and_Genus.md` but tabulates no values.

## Length table

$\ell(L)$ is the minimal number of generators of the discriminant group $A_L$.

| $L$ | $A_L$ | $\ell(L)$ |
| --- | --- | --- |
| $A_n$ | $C_{n+1}$ | 1 |
| $D_{2n}$ | $C_2^2$ | 2 |
| $D_{2n+1}$ | $C_4$ | 1 |
| $E_6$ | $C_3$ | 1 |
| $E_7$ | $C_2$ | 1 |
| $E_8$ | $0$ | 0 |
| $E_8(2)$ | $C_2^8$ | 8 |
| $\gens{n}$ | $C_n$ | 1 |
| $U$ | $0$ | 0 |
| $U(2)$ | $C_2^2$ | 2 |
| $E_{10}(2)$ | $C_2^{10}$ | 10 |
| $I_{p,q}(2)$ | $C_2^{p+q}$ | $p+q$ |
| $V$ | $C_3$ | 1 |
| $V(2)$ | $C_2\times C_6$ | 2 |
| $L_{2d}$ | $C_{2d}$ | 1 |
| $L_{K3}$ | $0$ | 0 |

::: {.Remark}
### The row that matters here

$A_{E_{10}(2)} = C_2^{10}$ with $\ell = 10$ is the datum behind $A_{T_{\Co}} \cong (\ZZ/2)^{11}$, since $T_{\Co} = \gens{2}\oplus E_{10}(2)$ contributes one further $C_2$.
This is the only place the corpus records that value explicitly.
:::

## Coxeter-Vinberg diagram conventions

| Description | Notation | $m_{ij}$ | $\angle(H_i,H_j)$ | $w_{ij}$ |
| --- | --- | --- | --- | --- |
| No edge | $H_i \perp H_j$ | 2 | $\pi/2$ | $0$ |
| Simple edge | $H_i \pitchfork H_j$ | 3 | $\pi/3$ | $1/2$ |
| Double edge | $H_i \pitchfork H_j$ | 4 | $\pi/4$ | $\sqrt2/2$ |
| Triple edge | $H_i \pitchfork H_j$ | 5 | $\pi/5$ | $(1+\sqrt5)/4$ |
| 4-fold edge | $H_i \pitchfork H_j$ | 6 | $\pi/6$ | $\sqrt3/2$ |
| Labelled simple edge | $H_i \pitchfork H_j$ | $m_{ij}\geq 7$ | $\pi/m_{ij}$ | $\cos(\pi/m_{ij})$ |
| Thick edge | $H_i \parallel H_j$ | $\infty$ | undefined | $1$ |
| Dotted edge | $H_i$ ultraparallel $H_j$ | 0 | $\infty$ | $\cosh\rho(H_i,H_j)$ |
| White vertex | $h_i^2 = -2$ | - | - | 2 |
| Black vertex | $h_i^2 = -4$ | - | - | 4 |

### Valid node-edge configurations

$|h_1 h_2| = \sqrt{h_1^2 h_2^2}\, w_{12}$ with $w_{12}$ from the table above.

| Configuration | $h_1^2$ | $h_2^2$ | $\abs{h_1 h_2}$ |
| --- | --- | --- | --- |
| white, white, no edge | $-2$ | $-2$ | 0 |
| white, white, simple | $-2$ | $-2$ | 1 |
| white, white, thick | $-2$ | $-2$ | 2 |
| white, white, dotted | $-2$ | $-2$ | $>2$ |
| white, black, no edge | $-2$ | $-4$ | 0 |
| white, black, double | $-2$ | $-4$ | 2 |
| white, black, dotted | $-2$ | $-4$ | $>2$ |
| black, black, no edge | $-4$ | $-4$ | 0 |
| black, black, simple | $-4$ | $-4$ | 2 |
| black, black, thick | $-4$ | $-4$ | 4 |
| black, black, dotted | $-4$ | $-4$ | $>4$ |

This project's `content_pandoc/sections/Compactifications/Reflection_Groups_and_Vinberg.md` describes dotted edges in prose only; the tables above are the corresponding numerical conventions, and are what the reconstruction formula
$$
\langle v_i, v_j\rangle = \sqrt{v_i^2 v_j^2}\,\cos\!\left(\frac{\pi}{m_{ij}+2}\right)
$$
of [[root-vectors-and-folded-sterk-diagrams]] depends on.

## Cusp type classification

|  | Type II | Type III |
| --- | --- | --- |
| Boundary strata | 1-cusps, curves $C_i$ | 0-cusps, points $p_j$ |
| Sublattice type | isotropic lines in $I^1(L)$ | isotropic planes in $I^2(L)$ |
| Subdiagram type | maximal parabolic | maximal elliptic |

## $E_8$ Gram matrix

In the negative-definite convention,
$$
G_{E_8} = \begin{pmatrix}
-2&0&1&0&0&0&0&0\\
0&-2&0&1&0&0&0&0\\
1&0&-2&1&0&0&0&0\\
0&1&1&-2&1&0&0&0\\
0&0&0&1&-2&1&0&0\\
0&0&0&0&1&-2&1&0\\
0&0&0&0&0&1&-2&1\\
0&0&0&0&0&0&1&-2
\end{pmatrix},
\qquad
G_{E_8}^{-1} = \begin{pmatrix}
-4&-5&-7&-10&-8&-6&-4&-2\\
-5&-8&-10&-15&-12&-9&-6&-3\\
-7&-10&-14&-20&-16&-12&-8&-4\\
-10&-15&-20&-30&-24&-18&-12&-6\\
-8&-12&-16&-24&-20&-15&-10&-5\\
-6&-9&-12&-18&-15&-12&-8&-4\\
-4&-6&-8&-12&-10&-8&-6&-3\\
-2&-3&-4&-6&-5&-4&-3&-2
\end{pmatrix}.
$$
The rows of $G_{E_8}^{-1}$ are the highest-root expansions used in the folded Sterk 3 rank check.

::: {.Remark}
### Not carried over

The source file also holds a Niemeier lattice table, a mass formula table, and a table of unimodular lattices by dimension.
These are standard and available in Conway-Sloane; they are noted here rather than reproduced.
The source file is internally corrupted in that region: rows $n = 6\ldots9$ of the mass-formula table are orphaned after the following section, and the label A.1.3 is used twice.
Its figure section lists captions only, with all images dead `cdn.mathpix.com` links.
:::

## Discriminant group cardinalities and orders

**Provenance for this section.** `/home/dzack/gitclones/diss/000-writing/.archive/source_material/past_writing/.archive/thesis-outline-p0.md` and `-p1.md`. Stated there without derivation and marked `audited: false`. Recorded because these are tedious to recompute, not because the source is authoritative: re-derive before relying on them.

Writing $A_L = I^0(A_L) \amalg I^1(A_L)$ with $I^i = \{x : q_L(x)\equiv i \bmod 2\ZZ\}$:

| $L$ | $\#A_L$ | $\#I^0$ | $\#I^1$ |
| --- | --- | --- | --- |
| $U(2)$ | 4 | 3 | 1 |
| $E_8(2)$ | 256 | 136 | 120 |
| $E_{10}(2)$ | 1024 | 528 | 496 |

Orders of the relevant orthogonal groups:
$$
\#\Orth(A_{E_{10}(2)}) = 2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31,
\qquad
\#\Orth(E_8(2)) = 2^{14}\cdot3^5\cdot5^2\cdot7,
\qquad
\#\Orth(A_{E_8(2)}) = 2^{13}\cdot3^5\cdot5^2\cdot7 .
$$
The covering $F_{\En,2}\to F_{K3,\En}$ is recorded as finite of degree $2^7\cdot17\cdot31$.

::: {.Remark}
### Why these belong in this project

$A_{T_{\Co}} \cong (\ZZ/2)^{11}$, since $T_{\Co} = \gens{2}\oplus E_{10}(2)$ adds one $C_2$ to $A_{E_{10}(2)} = C_2^{10}$.
The isotropic split of $A_{E_{10}(2)}$ above is the base case for reducing the $\Gamma_{\Co}$-orbit problem to a finite computation in $A_{T_{\Co}}$, which is the method recorded in [[cusp-correspondence-morphism-chain]]. The group orders bound the index computations in that reduction.
:::

Related: [[root-vectors-and-folded-sterk-diagrams]], [[coxiter-results-for-cusp-lattices]], [[coble-lattice-isotropic-candidates]].
