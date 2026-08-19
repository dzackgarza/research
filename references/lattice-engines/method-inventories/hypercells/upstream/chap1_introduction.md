# Chapter 1 — Introduction

> Source: https://www.hypercells.net/HyperCells/doc/chap1_mj.html

HyperCells is a package that allows constructing primitive cells and supercells of hyperbolic lattices based on triangle groups and quotients with normal subgroups.

## References

- P. M. Lenggenhager, J. Maciejko, and T. Bzdušek, *Non-Abelian hyperbolic band theory from supercells*, Phys. Rev. Lett. (accepted), arXiv:2305.04945 (2023) [LMB23]
- P. M. Lenggenhager, *Emerging avenues in band theory: multigap topology and hyperbolic lattices*, PhD thesis, ETH Zurich (2023) [Len23]
- P. M. Lenggenhager, J. Maciejko, and T. Bzdušek, *HyperCells: A GAP package for constructing primitive cells and supercells of hyperbolic lattices*, https://github.com/HyperCells/HyperCells (2023)
- M. Conder, *Quotients of triangle groups acting on surfaces of genus 2 to 101* (2007) [Con07]

## 1.1 Example

A typical workflow starts by setting up the (proper) triangle group, here Δ⁺(2,8,8):

```gap
gap> tg := ProperTriangleGroup( [ 2, 8, 8 ] );
ProperTriangleGroup(2, 8, 8)
```

Next, specify a unit cell via quotient of Δ⁺ with a translation group Γ ◁ Δ⁺:

```gap
gap> ListTGQuotients( [ 2, 8, 8 ] );
[ [ 2, 6 ], [ 3, 10 ], [ 3, 11 ], [ 5, 12 ], [ 5, 13 ], [ 9, 19 ], ... ]
```

Select a quotient (T2.6):

```gap
gap> q := TGQuotient( [ 2, 6 ] );
TGQuotient([ 2, 6 ], [ 2, 8, 8 ], 8, 2, Action reflexible [m,n],
    [ x^2, x * y * z, x * z * y, y^3 * z^-1 ])
```

Construct the cell graph:

```gap
gap> cg := TGCellGraph( tg, q, 3 : simplify := 0 );
```

Derive a tessellation model graph ({8,8} tessellation):

```gap
gap> model := TessellationModelGraph( cg, true : simplify := 0 );
TGCellModelGraph(
    TGCell( ProperTriangleGroup(2, 8, 8), [ x^2, x*y*z, x*z*y, y^3*z^-1 ] ),
    center = 3,
    type = [ "TESS", [ 8, 8 ], [ "VEF", [ [ 3 ], [ 1 ], [ 2 ] ] ] ],
    vertices = [ [ 3, 1 ] ],
    edges = [ [ 1, 1, [ 1, [ 1, 1, 5 ] ], g1 ], [ 1, 1, [ 1, [ 2, 4, 8 ] ], g4 ],
        [ 1, 1, [ 1, [ 3, 2, 6 ] ], g2 ], [ 1, 1, [ 1, [ 4, 3, 7 ] ], g3 ] ],
    faces = [ [ [ 1, -1 ], [ 2, -1 ], [ 4, 1 ], [ 3, -1 ], [ 1, 1 ], [ 2, 1 ],
        [ 4, -1 ], [ 3, 1 ] ] ]
)
```

Extend to a supercell (T3.11):

```gap
gap> sc := TGCellSymmetric( tg, TGQuotient( [ 3, 11 ] ), 3 );
TGCell( ProperTriangleGroup(2, 8, 8), [ x^2, x*y*z, x*z*y, y^-8 ] )

gap> scmodel := TGSuperCellModelGraph( model, sc : simplify := 0 );
TGSuperCellModelGraph(
    primitive cell = TGCell( ProperTriangleGroup(2, 8, 8),
        [ x^2, x*y*z, x*z*y, y^3*z^-1 ] ),
    supercell = TGCell( ProperTriangleGroup(2, 8, 8),
        [ x^2, x*y*z, x*z*y, y^-8 ] ),
    cell embedding = TGCellEmbedding(
        primitive cell = TGCellTranslationGroup( < g1, g2, g3, g4 |
            g2*g1^-1*g4^-1*g3*g2^-1*g1*g4*g3^-1 > ),
        supercell = TGCellTranslationGroup( < g1, g2, g3, g4, g5, g6 |
            g6*g4*g2*g1*g3*g5*g3^-1*g2^-1*g6^-1*g5^-1*g1^-1*g4^-1 > ),
        transversal = [ <identity ...>, (x^-1*y^-1)^4*x^-1 ],
        embedding = [ g1, g2, g3, g4, g5, g6 ] -> [ g1^-1*g4^-1, ... ]
    ),
    center = 3,
    ...
)
```

## 1.2 Simplify extension (optional)

The HyperCells package has an integrated word simplification procedure. Two methods:

1. **BruteForce** (default) — checks all words up to `simplify` length
2. **KnuthBendix** — uses the Knuth-Bendix completion algorithm (requires `kbmag` package v1.5.10+)

To extend kbmag beyond 127 generators (up to 65535), edit `defs.h` in the kbmag standalone directory:

```c
// Change from:
#define MAXGEN MAXCHAR
typedef char gen;

// To:
#define MAXGEN MAXUSHORT
typedef unsigned short gen;
```

Then recompile kbmag with `make clean` and `make`.

Example using Knuth-Bendix:

```gap
gap> scmodel := TGSuperCellModelGraph( model, sc : simplify := 4*3,
>       simplifyMethod := "KnuthBendix");
```

The option `simplify` specifies the maximal length of rewriting rules. If smaller than twice the number of generators, it defaults to twice the number of generators.
