# Reflective Lorentzian Lattices Test Fixtures

Source: http://www.math.rwth-aachen.de/~Markus.Kirschmer/lorentz/index.html

## Data Files

- **ListN**: Genus data for signature (N,1) lattices
  - Format: `< -det, symbol, facets, cusps >`
  - facets[k] = number of (N-k)-dimensional faces of fundamental domain
  - facets[1] = number of vectors from Vinberg's algorithm

- **GramN**: Gram matrices for each lattice
  - Each line contains (N+1)×(N+1) entries of symmetric bilinear form
  - Ordering matches ListN

## Statistics

| Dimension | Lattices |
|-----------|----------|
| 3         | 203      |
| 4         | 62       |
| 5         | 81       |
| 6         | 54       |
| 7         | 78       |
| 8         | 39       |
| 9         | 50       |
| 10        | 24       |
| 11        | 27       |
| 12        | 15       |
| 13        | 17       |
| 14        | 8        |
| 15        | 10       |
| 16        | 2        |
| 17        | 5        |
| 18        | 2        |
| 19        | 3        |
| 21        | 1        |
| **Total** | **781**  |

## Completeness

- n=4,5: Complete (Walhorn, Turkalj)
- n>5: Complete under assumption det has no prime divisors >19
- n=3: Contains all strongly squarefree isotropic and anisotropic lattices

## Example Usage

```python
# Parse List3 to get genus symbols and invariants
# Cross-check against computed Gram matrix determinants
# Verify face counts match Vinberg algorithm output
```
