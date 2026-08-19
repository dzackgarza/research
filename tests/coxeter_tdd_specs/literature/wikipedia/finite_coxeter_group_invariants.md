# Invariants of the finite irreducible Coxeter groups

**Source**: https://en.wikipedia.org/wiki/Coxeter_group, section "Properties"
**Retrieved**: 2025-07-26 (transcribed from the full-article capture made by
`literature/tools/webpage_to_markdown.py`)
**Citation Key**: `wikipedia_coxeter_groups_2025`

This is the oracle table behind the bracket-notation orders and Weyl-group orders asserted in
`tests/coxeter_tdd_specs/system/test_literature_examples.py`
(`test_wikiwand_bracket_notation_examples`, `test_wikipedia_weyl_group_isomorphisms`,
`test_dynkin_diagram_invariant_recovery`). Every row is a falsifiable claim: each order and
Coxeter number is computable from Sage's `WeylGroup` / `CoxeterGroup`.

Notation: `n` is the rank, `h` the Coxeter number, `m = nh/2` the number of reflections
(equivalently the number of positive roots). The dihedral group of order `2p` is written
`D_{2p}`, following the article.

| Rank | Group | Bracket notation | Reflections m = nh/2 | Coxeter number h | Order | Group structure |
|---|---|---|---|---|---|---|
| 1 | A_1 | [ ] | 1 | 2 | 2 | S_2 |
| 2 | A_2 | [3] | 3 | 3 | 6 | S_3 ≅ D_6 |
| 3 | A_3 | [3,3] | 6 | 4 | 24 | S_4 |
| 4 | A_4 | [3,3,3] | 10 | 5 | 120 | S_5 |
| 5 | A_5 | [3,3,3,3] | 15 | 6 | 720 | S_6 |
| n | A_n | [3^{n-1}] | n(n+1)/2 | n+1 | (n+1)! | S_{n+1} |
| 2 | B_2 | [4] | 4 | 4 | 8 | C_2 ≀ S_2 ≅ D_8 |
| 3 | B_3 | [4,3] | 9 | 6 | 48 | C_2 ≀ S_3 ≅ S_4 × 2 |
| 4 | B_4 | [4,3,3] | 16 | 8 | 384 | C_2 ≀ S_4 |
| 5 | B_5 | [4,3,3,3] | 25 | 10 | 3840 | C_2 ≀ S_5 |
| n | B_n | [4,3^{n-2}] | n² | 2n | 2^n · n! | C_2 ≀ S_n |
| 4 | D_4 | [3^{1,1,1}] | 12 | 6 | 192 | C_2^3 · S_4 |
| 5 | D_5 | [3^{2,1,1}] | 20 | 8 | 1920 | C_2^4 · S_5 |
| n | D_n | [3^{n-3,1,1}] | n(n-1) | 2(n-1) | 2^{n-1} · n! | C_2^{n-1} · S_n |
| 6 | E_6 | [3^{2,2,1}] | 36 | 12 | 51840 | GO_6^-(2) ≅ PSp_4(3):2 |
| 7 | E_7 | [3^{3,2,1}] | 63 | 18 | 2903040 | GO_7(2) × 2 ≅ Sp_6(2) × 2 |
| 8 | E_8 | [3^{4,2,1}] | 120 | 30 | 696729600 | 2 · GO_8^+(2) |
| 4 | F_4 | [3,4,3] | 24 | 12 | 1152 | GO_4^+(3) |
| 2 | G_2 | [6] | 6 | 6 | 12 | D_12 |
| 2 | I_2(5) = H_2 | [5] | 5 | 5 | 10 | D_10 |
| 3 | H_3 | [3,5] | 15 | 10 | 120 | 2 × A_5 |
| 4 | H_4 | [3,3,5] | 60 | 30 | 14400 | 2 · (A_5 × A_5) : 2 |
| 2 | I_2(p) | [p] | p | p | 2p | D_{2p} |

The order of a reducible group is the product of the orders of its irreducible components.

B_n and C_n give the same Coxeter group: the directed Dynkin diagrams differ, the undirected
Coxeter graphs agree. This is why `[4,3]` (B_3) and `[3,4]` (C_3) both have order 48 in the
bracket-notation fixture.

The finite Coxeter groups that are not Weyl groups (not crystallographic) are H_3, H_4, and
those I_2(p) not isomorphic to a Weyl group; the exceptional isomorphisms are
I_2(3) ≅ A_2, I_2(4) ≅ B_2, I_2(6) ≅ G_2.
