# Expensive Computations Reference

Notes on computational cost, grounded in benchmarks.

## Discriminant Groups

**Discriminant group computation is not expensive.** Benchmarks in Sage on
research-relevant lattices:

| Lattice | rank | A_L | `discriminant_group()` |
|---|---|---|---|
| U(2) ⊕ E8² | 18 | (ℤ/2)² | ~0.106s |
| K3(2) = U(2)³ ⊕ E8(2)² | 22 | (ℤ/2)²² | ~0.144s |

Both are sub-second. Compute the full group freely; no need to substitute `det(G)` as a
cardinality proxy unless profiling reveals an actual bottleneck in a specific script.
