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
- `Sterk3.coxiter` — the Sterk 3 cusp diagram (Sterk Fig. 8, p. 22), twelve vertices
  $\alpha_1,\dots,\alpha_7,\alpha_9,\dots,\alpha_{13}$. Its vertices and weights are derived from
  the reconstruction of Sterk's root vectors by
  `../reports/coble_sterk3-coxiter-input.py`, whose run checks that this file carries exactly that
  diagram and that CoxIter's Gram matrix for it is the normalised Gram of those roots.
- `F2.coxiter`, `F4.coxiter` — two larger rank-$24$ diagrams.
- `k4.coxiter`, `5cycle.coxiter` — the complete graph on four vertices and the
  five-cycle, both with every bond $3$; small specimens.

## Input format

Transcribed from CoxIter's own documentation, "Using CoxIter", section *Encoding a Coxeter graph*
(<https://rgugliel.github.io/CoxIter/page_cox_iter.html>), read 2026-11-07 against the binary in the
rootfs (`/usr/local/bin/coxiter`, version 1.3):

- First line, mandatory: `d, n` — `d` the number of vertices and `n` the dimension. The dimension is
  optional; without it CoxIter infers it from the maximal spherical and euclidean subgraphs, and that
  inference needs the polytope to have at least one vertex. `E6.coxiter` writes the bare count `6`
  and `F2.coxiter` writes `dimension 24`; both are read, and `Sterk3.coxiter` writes the documented
  `12 9`.
- Second line, optional: `vertices labels: label1 label2 ...`. Without it the vertices are `1..d`.
  A label may carry letters, digits, `-` and `_`, but no space.
- Every later line: `v1 v2 weight`. Only one line per edge is needed, and weight `2` (no bond) may be
  omitted. **Weight `0` is the weight infinity and weight `1` is a dotted edge** — the documented
  meaning, so no longer a thing to be read off before a reader is written. A dotted edge leaves the
  corresponding Gram entry as a free parameter: the docs' Example 2 prints it as a symbol `l_i_j`
  ("weight of the dotted line between hyperplanes 2 and 4") and adds the variables to the Gram
  matrix. `Sterk3.coxiter` uses `0` for the one $\infty$-bond of Sterk's Fig. 8.

`F4.coxiter` line 31 reads `21 22 ?`. `?` is not a weight CoxIter documents: measured on a
three-vertex test file, it prints `Unread line (incorrect format): #2 3 ?#2` and drops the line, so
that bond is missing from every run of that input. The intended weight is not recoverable from the
file and is not guessed here.

CoxIter reads the graph on **standard input**: `./coxiter < file.coxiter`, as its own usage string
puts it, or with `-i file.coxiter`. A bare path argument does not work — it reports
`Error while reading graph: EMPTY_FILE`.

## Runs

`logs/*.txt` are the CoxIter transcripts. Those for the three $(r, a, \delta)$-named inputs list the
connected spherical graphs by rank, then the euclidean ones, then the products with their Weyl-group
orders, and close with the f-vector, the number of vertices at infinity, and the Euler
characteristic. For `10-8-0_1` the f-vector is $(10, 45, 120, 210, 252, 210, 120, 45, 10, 1)$
with two vertices at infinity and Euler characteristic $0$.

`logs/Sterk3.txt` is the transcript for `Sterk3.coxiter`: 12 vertices, dimension 9, field
$\QQ[\sqrt2]$, not cocompact, **finite covolume yes**, f-vector
$(33, 164, 398, 602, 616, 434, 208, 65, 12, 1)$, 4 vertices at infinity. Its `Signature
(numerically)` line reads `10,2,0` and is *not* the inertia of the Gram matrix CoxIter prints
alongside it: that matrix has rank 10 and inertia $(9,1,2)$, which is the sign flip of the
reconstruction's $(1,9,2)$, as `../reports/coble_sterk3-coxiter-input.py` checks entry by entry.
Cite the matrix, not that line.

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
lifted as-is: the weights have to be settled first, and with the format above
they now are for `0`, `1` and `2`.
