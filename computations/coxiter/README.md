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
- `Sterk2.coxiter` — the Sterk 2 cusp diagram (Sterk Fig. 6, p. 21), ten vertices. It predates the
  batch that produced the four below and is not checked against a reconstruction.
- `Sterk1.coxiter`, `Sterk3.coxiter`, `Sterk4.coxiter`, `Sterk5.coxiter` — the other four Sterk cusp
  diagrams, from Sterk's Figs 4, 8, 10 and 12 on pp. 19, 22, 23 and 24. Each carries Sterk's own
  vertex labels, and each is checked against the reconstruction of the roots he prints beside the
  figure: `../reports/coble_sterk3-coxiter-input.py` for Fig. 8 and
  `../reports/coble_sterk-cusp-coxiter-inputs.py` for Figs 4, 10 and 12. Both derive the Gram matrix
  of the diagram's roots, turn each pairing into a Coxeter weight exactly, and check that the file
  carries exactly that diagram and that CoxIter's Gram matrix for it is the normalised Gram of those
  roots. No Sterk input here rests on a plate alone.
- `F2.coxiter`, `F4.coxiter` — two larger rank-$24$ diagrams.
- `k4.coxiter`, `5cycle.coxiter` — the complete graph on four vertices and the
  five-cycle, both with every bond $3$; small specimens.

## Input format

Transcribed from CoxIter's own documentation, "Using CoxIter", section *Encoding a Coxeter graph*
(<https://rgugliel.github.io/CoxIter/page_cox_iter.html>), read 2026-11-07 against the binary in the
rootfs (`/usr/local/bin/coxiter`, version 1.3):

- First line, mandatory: `d, n` — `d` the number of vertices and `n` the dimension. The dimension is
  optional; without it CoxIter infers it from the maximal spherical and euclidean subgraphs, and that
  inference needs the polytope to have at least one vertex. The four Sterk inputs of this batch write
  it — `12 9`, `12 9`, `11 9`, `14 9` for cusps 1, 3, 4, 5 — and `E6.coxiter` writes the bare count
  `6`.

  The other inputs begin `dimension N`. That is not a form the documentation gives, and it does not
  declare the dimension: measured on all five, CoxIter takes `N` as the vertex count, reports
  `Dimension: ?`, and guesses. `dimension 10` gives 10 vertices and guessed dimension 9
  (`10-10-0_1`, `10-8-0_1`, `Sterk2`), `dimension 9` gives 9 vertices and guessed 8 (`9-9-1_1`), and
  `dimension 24` gives 24 vertices and guessed **18** (`F2`). The first four guesses are the dimension
  those runs are meant to work in, so they stand; `F2`'s is not, and its first line should carry the
  dimension as the second token once that dimension is known. It is not guessed here.
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

## The five Sterk cusps

One input and one transcript per cusp, all five in dimension 9, all five non-cocompact with finite
covolume and Euler characteristic 0. The vertex counts are Sterk's, and each agrees with the node
count of its plate read at 300 dpi (Figs 4, 6, 8, 10, 12 on pp. 19, 21, 22, 23, 24).

| Cusp | Input | Vertices | Dimension | Finite covolume | Vertices at $\infty$ | Field | $f$-vector | Transcript |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sterk 1 | `Sterk1.coxiter` | 12 | 9 | yes | 9 | $\QQ$ | $(23, 114, 288, 462, 504, 378, 192, 63, 12, 1)$ | `logs/Sterk1.txt` |
| Sterk 2 | `Sterk2.coxiter` | 10 | 9 (guessed) | yes | 2 | $\QQ[\sqrt2]$ | $(10, 45, 120, 210, 252, 210, 120, 45, 10, 1)$ | `logs/Sterk2.txt` |
| Sterk 3 | `Sterk3.coxiter` | 12 | 9 | yes | 4 | $\QQ[\sqrt2]$ | $(33, 164, 398, 602, 616, 434, 208, 65, 12, 1)$ | `logs/Sterk3.txt` |
| Sterk 4 | `Sterk4.coxiter` | 11 | 9 | yes | 5 | $\QQ[\sqrt2]$ | $(26, 125, 300, 450, 460, 330, 165, 55, 11, 1)$ | `logs/Sterk4.txt` |
| Sterk 5 | `Sterk5.coxiter` | 14 | 9 | yes | 13 | $\QQ[\sqrt2]$ | $(115, 600, 1352, 1768, 1508, 875, 346, 90, 14, 1)$ | `logs/Sterk5.txt` |

The dimension is the one declared in each input's first line, except for `Sterk2.coxiter`, whose
`dimension 10` first line leaves it to be guessed (9, see the format section). These are the rows of
`@sec-coxiter-results-for-cusp-lattices`; `../reports/coble_sterk-cusp-coxiter-inputs.py` compares
them against the runs for cusps 1, 4 and 5 and reports a disagreement rather than reconciling it.

## Runs

`logs/*.txt` are the CoxIter transcripts. Those for the three $(r, a, \delta)$-named inputs list the
connected spherical graphs by rank, then the euclidean ones, then the products with their Weyl-group
orders, and close with the f-vector, the number of vertices at infinity, and the Euler
characteristic. For `10-8-0_1` the f-vector is $(10, 45, 120, 210, 252, 210, 120, 45, 10, 1)$
with two vertices at infinity and Euler characteristic $0$.

The `Signature (numerically)` line of every Sterk transcript is **not** the "Signature line" column of
the cusp table in the writing. It reads 10,2,0 (Sterk 1), 9,1,0 (Sterk 2), 10,2,0 (Sterk 3),
10,1,0 (Sterk 4) and 13,1,0 (Sterk 5), while that column's 9,1,2; 9,1,0; 9,1,2; 9,1,1; 9,1,4 are the
inertia of the sign-flipped Gram of each diagram's roots, as
`../reports/coble_sterk-cusp-signatures-run.txt` reproduces it at all five cusps. The two agree only
at cusp 2, by coincidence. Cite the Gram matrix or the column, not that line; and whatever is
disputed about the signature of the third cusp in `logs/Sterk3.txt` is settled by the matrix printed
beside it, rank 10 with inertia $(9,1,2)$, not by the line.

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
