# CoxIter inputs and runs

CoxIter (Rafael Guglielmetti) reads a Coxeter graph and reports the spherical
and euclidean subgraphs, the f-vector of the corresponding polytope, and
covolume information. This directory holds the diagram inputs given to it and
the transcripts of the runs.

## Inputs

`*.coxiter` files, one Coxeter graph each:

- `E6.coxiter` — the $E_6$ diagram.
- `9-9-1_1.coxiter`, `10-8-0_1.coxiter`, `10-10-0_1.coxiter` — diagrams named
  by the Nikulin invariants $(r, a, \delta)$ of the two-elementary lattice they
  belong to.
- `Sterk2.coxiter` — the Sterk 2 cusp diagram.
- `F2.coxiter`, `F4.coxiter` — two larger rank-$24$ diagrams.
- `k4.coxiter`, `5cycle.coxiter` — the complete graph on four vertices and the
  five-cycle, both with every bond $3$; small specimens.

## Input format, as observed in these files

The first line is either a bare vertex count (`6`) or `dimension d`. An
optional `vertices labels: ...` line names the vertices. Every later line is a
triple `i j m`: an edge between vertices `i` and `j` carrying the Coxeter
exponent `m`. Pairs not listed carry the default bond.

The weights `0`, `1` and `?` also occur (`F2.coxiter`, `F4.coxiter`). What
CoxIter means by each is **not** recorded here and must be read off CoxIter's
own documentation before any reader is written; do not guess. The exponents
that do appear with a checkable meaning are confirmed by the run transcripts:
`8 9 4` in `9-9-1_1.coxiter` is reported as `G2 ; 8 9 (4)` in
`logs/9-9-1_1.txt`.

## Runs

`logs/*.txt` are the CoxIter transcripts for the three $(r, a, \delta)$-named
inputs. Each lists the connected spherical graphs by rank, then the euclidean
ones, then the products with their Weyl-group orders, and closes with the
f-vector, the number of vertices at infinity, and the Euler characteristic.
For `10-8-0_1` the f-vector is $(10, 45, 120, 210, 252, 210, 120, 45, 10, 1)$
with two vertices at infinity and Euler characteristic $0$.

## What the preamble owns, and what it does not

The subdiagram enumeration, the ellipticity and parabolicity predicates, the
diagram automorphism group and the orbits are owned on the lattice side
(`preamble/.../coxeter_diagrams.sage`,
`preamble/.../vinberg_invariants.sage`), so CoxIter is a cross-check here, not
the source of those notions.

Reading a `.coxiter` file into a diagram is **not** owned. The archived
notebook `archives/notebooks/Maximal Elliptic Subdiagram Class.ipynb` has a
reader (`CoxeterDiagram.init_from_coxiter_file`) that keeps every line of three
integers and builds a weighted graph, then attaches root squares as self-loops.
That reader silently drops any line it does not recognise, so it cannot be
lifted as-is: the weights above must be settled first.
