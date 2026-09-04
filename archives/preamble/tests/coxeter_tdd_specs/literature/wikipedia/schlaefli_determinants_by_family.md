# Schläfli determinants of the extended diagram series

**Source**: https://en.wikipedia.org/wiki/Coxeter%E2%80%93Dynkin_diagram, sections "Schläfli matrix", "Rank 2 Coxeter groups", "Very-extended Coxeter diagrams" **Retrieved**: 2025-07-26 (transcribed from the full-article capture made by `literature/tools/webpage_to_markdown.py`) **Citation Key**: `wikipedia_coxeter_dynkin_2025` **Revision**: oldid 1290398091 (last edited 14 May 2025), permanent link https://en.wikipedia.org/w/index.php?title=Coxeter%E2%80%93Dynkin_diagram&oldid=1290398091

All matrices and determinants here are in the literature convention `C_ij = -2 cos(π/p_ij)`. This project's Gram matrix is `B = -C` (`literature/PROJECT_CONVENTIONS.md`); `det B = (-1)^n det C`, so the determinants below transfer unchanged in even rank and with a sign flip in odd rank.

The determinant of the Schläfli matrix is called the **Schläflian**.

## Rank 2

For the rank-2 diagram `[p]`,

```
C = [[2, -2cos(π/p)], [-2cos(π/p), 2]],   det C = 4 - 4cos²(π/p) = 4 sin²(π/p).
```

| p | Group | Schläfli matrix | det C |
| --- | --- | --- | --- |
| 2 | I_2(2) = A_1 × A_1 | [[2,0],[0,2]] | 4 |
| 3 | I_2(3) = A_2 | [[2,-1],[-1,2]] | 3 |
| 4 | I_2(4) = B_2 | [[2,-√2],[-√2,2]] | 2 |
| 5 | I_2(5) = H_2 | [[2,-φ],[-φ,2]] | (5-√5)/2 |
| 6 | I_2(6) = G_2 | [[2,-√3],[-√3,2]] | 1 |
| ∞ | I_2(∞) | [[2,-2],[-2,2]] | 0 |

In rank 2, and only in rank 2, the sign of the Schläflian settles the type outright, because the determinant is the product of the two eigenvalues: positive → finite, zero → affine, negative → hyperbolic.
In higher rank the classification is by the signature; a zero Schläflian still detects a nontrivial radical in every rank.

## Determinant by rank, per family

The extension process (adjoining a node) walks a family from finite through affine (extended) to hyperbolic (over-extended) and Lorentzian (very-extended).
The Schläflian as a function of the rank names where each transition happens.

| Family | Bracket notation | det C |
| --- | --- | --- |
| A_1^n | [2^{n-1}] | 2^n (finite for all n) |
| A_n | [3^{n-1}] | n + 1 (finite for all n) |
| B_n | [4,3^{n-2}] | 2 (finite for all n) |
| D_n | [3^{n-3,1,1}] | 4 (finite for all n) |
| E_n | [3^{n-3,2,1}] | 9 - n |
| — | [3^{n-4,3,1}] | 2(8 - n) |
| — | [3^{n-4,2,2}] | 3(7 - n) |
| F_n | [3,4,3^{n-3}] | 5 - n |
| G_n | [6,3^{n-2}] | 3 - n |

Transitions in the exceptional series:

- E_n: finite for E_3 (= A_2 × A_1), E_4 (= A_4), E_5 (= D_5), E_6, E_7, E_8; affine at E_9 = Ẽ_8 (det 0); hyperbolic at E_10 (det -1). E_11 is the very-extended member.

- [3^{n-4,3,1}]: finite for n = 4..7, affine at n = 8 (Ẽ_7), hyperbolic beyond.

- [3^{n-4,2,2}]: finite for n = 4..6, affine at n = 7 (Ẽ_6), hyperbolic beyond.

- F_n: finite for F_3 (= B_3) and F_4; affine at F_5 = F̃_4; hyperbolic at F_6.

- G_n: finite for G_2; affine at G_3 = G̃_2; hyperbolic at G_4.

## Hyperbolic subdivision

A connected diagram is **hyperbolic** when it is neither finite nor affine while every proper connected subdiagram is finite or affine.
It is **compact** (Lannér) when every proper subgroup is finite, and **paracompact** (Koszul, quasi-Lannér) when every proper subgroup is finite or affine.
