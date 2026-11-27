# Current gaps

## Literature / citation gaps

### Task 1.1 sextic constructions — VALIDATED (EXTENDS literature)

**Status**: VALIDATED — The repo's three Task 1.1 examples are confirmed independent
constructions from Thas (1994), but now validated against Pieroni (2026). Pieroni
provides theoretical framework explaining why 10-nodal sextics are rare (28-dimensional
space vs 30 conditions).
Repo provides computational examples that Pieroni's theory predicts should be special.
See `notes/thas_vs_task1_1_comparison.md` and `notes/literature_connections.md`.

**Connection**: EXTENDS — Pieroni (2026) lines 752-759, 1225-1280 provide theoretical
justification. Repo's parametric construction via resultants provides concrete
realizations.

**Remaining gap**: Could still be connected to Coble (1917) or Coolidge (1931) primary
sources (both blocked on institutional access).

### J. Thas uniqueness primary source — BLOCKED

**Status**: BLOCKED — The underlying `J. Thas` primary source behind the stronger
uniqueness wording remains unresolved.
Only accessible via Dolgachev's archived 2016 MPI abstract (secondary source).

**Gap**: C. Thas (1994) provides weaker existence/construction claim.
Stronger uniqueness claim requires J. Thas primary source.

**Next action**: Requires author contact or institutional access to
unpublished/conference sources.

### Coolidge stronger theorem wording — BLOCKED

**Status**: BLOCKED — Coolidge has been directly inspected for the classical
nine-/ten-node discussion, but the stronger all-ten-from-any-nine theorem wording quoted
via MathOverflow needs cleaner primary-text extraction.

**Gap**: MathOverflow paraphrase of "Theorem 28, p. 392" not yet isolated from primary
text.

**Next action**: Requires better OCR extraction or page-image confirmation from Coolidge
(1931).

## Computation-to-literature interface gaps — RESOLVED (2026-03-31)

**Status**: All computational work validated against literature (Pieroni 2026,
Huybrechts K3). See `notes/literature_connections.md` for complete analysis.

**Key findings**:
- Task 1.1 (Sextic constructions): EXTENDS — Pieroni provides theoretical framework,
  repo provides computational examples
- Task 3.2 (Isotropic planes): CONTEXT — Pieroni E₁₀ = Num(X) provides lattice
  structure. Note: Theorem 46 concerns geometric isotropic sequences (E_i·E_j = 1 -
  δ_ij), not lattice-theoretic isotropic vectors (v² = 0)
- Task 5.1 (Involutions): EXTENDS — Pieroni Theorem 72 classifies ALL involutions as
  Bertini lifts, repo constructs explicit example
- Lattice structure: MATCHES — Pieroni's E₁₀ = Num(X) aligns with repo's S_Co structure
- NO CONTRADICTIONS found between literature and computational work

**Documentation**:
- Task 1.1: `notes/task1_1_birationality_note.md`,
  `notes/task1_1_exact_coordinate_note.md`
- Literature connections: `notes/literature_connections.md` (264 lines)
- Acquired papers: 5 sources locally (21,613 total lines)

## Computational gaps

### Task 3.2 orbit uniqueness — CONJECTURE (computational complexity)

**Status**: CONJECTURE — The orbit uniqueness claim for 15 primitive isotropic planes
remains computationally unverified due to computational complexity.

**Attempts**: 6 failed attempts (5 GAP, 1 Sage native) - all timeout or return empty.
Root cause: A_T has order 2048, O(q_T) is large, orbit computation is genuinely hard.

**What is verified**:
- Enumeration: 27 isotropic planes found, 15 primitive ✓
- J⊥/J structure: J⊥/J ≅ A₁^⊕7 confirmed for all 15 planes ✓
- Orbit uniqueness: CONJECTURE (not computationally verified)

**Theoretical support**:
- Nikulin Prop 1.5.2: surjectivity O(T) → O(q_T) implies single orbit
- Pieroni (2026): E₁₀ = Num(X) provides lattice structure alignment (lines 146, 483-493)
  Note: Theorem 46 concerns geometric isotropic sequences, not lattice-theoretic
  isotropic vectors

**Software research** (2026-03-31): Investigated alternative approaches including Dawes
(2022) algorithms, Sage native functionality, Magma, and PARI/GP. Conclusion:
computational complexity is fundamental, not tool-specific.
See `notes/task3_2_gap_difficulty.md` for complete analysis.

**Next action**: Accept as CONJECTURE with strong theoretical support.
See `notes/task3_2_gap_difficulty.md` and `notes/task3_2_gap_difficulty.md` for complete
analysis.

## Genuine mathematical / implementation gaps

- The old Task 5.1 involution construction failed, but the current exact script now
  replaces it with a verified glued-model route: primitive `S_Co \hookrightarrow Λ_K3`,
  true orthogonal complement, and a sign involution that is integral and satisfies
  `θ ∈ O(Λ_K3)` on that explicit ambient lattice model.
- The remaining Task 5.1 gap is no longer raw existence of `θ`; it is to keep longer
  prose and literature-facing claims consistent with
  `notes/task5_1_exact_involution_note.md` without overclaiming beyond the verified
  glued model.
- `notes/task5_1_route_reset.md` remains canonical for the route order: primitive
  embedding and orthogonal complement first, involution only afterward; CARAT remains
  auxiliary only on finite positive-definite subproblems.
- Lean formalization remains secondary until the literature spine and blocked
  computations are stabilized.

## Computational bugs (resolved 2026-03-30)

**Task 1.2 T_Co Gram matrix bug**: FIXED (commit 160422c). Changed embedding
construction in `task1_2_gram_matrices_fixed.sage` to use single coordinates instead of
pairs. T_Co Gram diagonal now correct `[2, 2, -2, -2, -2, -2, -2, -2, -2, -2, -2]` with
determinant -2048.

**Task 1.3 T_Co embedding**: NOT A BUG. Discriminant form verification confirmed
computed T_Co has correct discriminant form.
Non-diagonal Gram matrix is different basis representation of same lattice.

## Immediate next targets

- None — all immediate literature and computation-to-literature interface gaps are now
  documented.
