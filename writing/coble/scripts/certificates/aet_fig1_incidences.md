"""Incidence transcription of AET Figure 1's subdiagrams, with the uncertainty left visible.

Source.  V. Alexeev, P. Engel, A. Thompson, *Stable pair compactification of moduli of K3
surfaces of degree 2*, arXiv:1903.09742v3 (= `AET23`), Figure 1 on p. 22 and Lemma 4.5.  The
figure is drawn by five vector PDFs in the e-print, `fig-Vinberg` (the labelled diagram) and the
four small ones; each small figure repeats the same triangle of 24 node positions with the
subdiagram's nodes black.  Read from the standalone artwork at 240 dpi
(`pdftoppm -png -r 240 fig-wD10wE7.pdf`), not from the page and not from a raster preview.

Node layout (the labels printed on the large diagram), rows top to bottom:

    12
    13  11
    14  20  10
    15  22  21   9
    16            8
    17  18  23  19   7
     0   1   2   3   4   5   6

Line conventions printed in the figure and stated in the text (§4A): no line = inner product 0,
single line = 1, doubled line = 2, dashed line = 6.

Vertex sets.  Read from the black-filled disks and checked in `read_fig1.py` (every black disk
sits on a printed node position; the 18 of `fig-wA17` are exactly the rim):

    A~17       0..17                                       18 nodes
    D~10 E~7   complement of {8, 16, 21, 22, 23}           19 nodes
    E~8^2 A~1  complement of {3, 12, 21, 22}               20 nodes
    D~16 A~1   complement of {2, 4, 20, 21, 22}            19 nodes

Incidence reading for `fig-wD10wE7`.  The bold strokes are the subdiagram's edges; the thin and
dashed ones belong to the ambient diagram, and a crossing of two strokes is not a node or an
edge.  Corrected against the standalone artwork and against the full Figure 1:

    single   12-13, 13-14, 14-15, 12-11, 11-10, 10-9, 12-20,
             0-1, 1-2, 2-3, 3-4, 4-5, 5-6, 6-7, 17-0, 0-18, 6-19
    doubled  18-21, 19-22
    dashed   21-22, 22-23, 23-21

Two components, of sizes 8 and 11, as the caption says (D~10 + E~7).  The 11-node one,
{18, 17, 0, 1, ..., 7, 19} with the ten edges 17-0, 0-1, ..., 6-7, 0-18, 6-19, is a tree with
two trivalent nodes (0 and 6) and four leaves (17, 18, 7, 19); the 8-node one is
{12, 13, 14, 15, 11, 10, 9, 20} with the seven edges 12-13, 13-14, 14-15, 12-11, 11-10, 10-9,
12-20.

Affine D10 is a *tree*, ten undirected edges on eleven vertices -- Sage prints its Dynkin
diagram directed, hence twenty arcs, which an earlier note in this file misread as needing a
cycle.  No eleventh edge is missing.

Validation.  `validate_fig1_component.py` compares each transcribed component with the Dynkin
diagram of its affine type as an edge-labelled graph, on the maintained baseline: E~7 True,
D~10 True (11 nodes, 10 undirected edges, degree sequence 3,3,2,2,2,2,2,1,1,1,1 -- the same as
the type's).

Candidate Gram data, checked against the source's Lemma 4.7.  With square -2, pairing 1 along
the 18-cycle and at (0,18), (6,19), (12,20), pairing 2 at (18,21), (21,9), (19,22), (22,15),
(20,23), (23,3) and pairing 6 at (21,22), (22,23), (23,21), `check_fig1_gram.py` reports:
symmetric, diagonal -2, rank 19 over QQ, kernel of dimension 5 -- which is exactly what "the 24
roots generate N" requires -- and every one of the seven affine components carries the Kac
marks of its type:

    A~17      [1 x 18]                        D~10     [1,1,2,2,2,2,2,2,2,1,1]
    E~7       [1,2,3,4,3,2,1,2]               E~8^(1)  [1,2,3,4,5,6,4,2,3]
    E~8^(2)   [2,4,6,5,4,3,2,1,3]             A~1      [1,1]
    D~16      [1,1,2,...,2,1,1]               A~1*     [1,1]

The first E8's solved vector is the one the article displays:
r_13 + 2r_14 + 3r_15 + 4r_16 + 5r_17 + 6r_0 + 4r_1 + 2r_2 + 3r_18.  And Lemma 4.7
(lem:N-linear-rels) holds in the presentation -- the four differences are relations, G(a1-a2)=0:

    n(D~10) - n(E~7) = 0,  n(E~8^(1)) - n(E~8^(2)) = 0,
    n(E~8^(1)) - n(A~1) = 0,  n(D~16) - n(A~1*) = 0.

So the numbered-root Gram data is no longer a blocker: it is the candidate above, validated
against the source's own Lemma 4.7 and against the Kac marks of the seven affine components.
N is kept distinct from M = N^* of Lemma 4.14 throughout; the roots are a dependent generating
family in rank 19, so the relations are vectors a in Z^24 with G a = 0.
