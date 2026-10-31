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
dashed ones belong to the ambient diagram.  Read off the standalone artwork:

    single (bold)   12-13, 13-14, 14-15, 12-11, 11-10, 10-9, 12-20,
                    0-1, 1-2, 2-3, 3-4, 4-5, 5-6, 0-17, 6-7, 17-18
    doubled         15-22, 9-21, 18-22, 19-21     (all with a white node at one end)
    dashed          22-21, 22-23, 21-23

Two components come out, of sizes 8 and 11, which agrees with the caption's D~10 + E~7 (11 + 8).
The 8-node one is {12, 13, 14, 15, 11, 10, 9, 20} with 7 bold edges.

Validation through the maintained API (`validate_fig1_component.py`).  The 8-node component
above is asked whether it is the Dynkin diagram of `CartanType(["E", 7, 1])`, compared as an
edge-labelled graph: the answer is True.  So the reading of that component is confirmed by the
library, arms (3, 3, 1) included -- my first guess that affine E7 should have arms (2, 3, 2)
was wrong, and the record corrected it by running the check rather than by re-reading the
picture.

The 11-node component is *not* isomorphic to `CartanType(["D", 10, 1])`: as read it has 10
edges where the affine D10 diagram has 11, so exactly one incidence is unread.  The candidates
are edges among {18, 19, 23} and the bottom chain, which the drawing renders close together;
they are left open rather than guessed, and the component is not used.

Status.  Two of the four subdiagrams now stand on a validated structure -- A~17 as an 18-cycle
(and its null vector proved null in CoxeterRim.lean) and the E7 half of D~10 E~7 by the
isomorphism above.  The remaining source transcription is one incidence in the D10 component,
plus the whole of the E~8^2 A~1 and D~16 A~1 components, whose figures have not been read yet.
The vertex sets of all four are validated and in use.

## The candidate Gram data, checked against the source's own Lemma 4.7

A full candidate was supplied for the 24 roots: square -2; pairing 1 along the 18-cycle
0..17 and at (0,18), (6,19), (12,20); pairing 2 at (18,21), (21,9), (19,22), (22,15), (20,23),
(23,3); pairing 6 at (21,22), (22,23), (23,21); zero elsewhere. `check_fig1_gram.py` runs it
against Table 1 of Sec. 4C and the Kac marks of the affine types, on the maintained baseline:

    Gram symmetric, diagonal -2, rank 19 over QQ, kernel of dimension 5

which is exactly what "the 24 roots generate N" requires. Then, component by component, the
induced block must have the Kac marks of its type as its null vector:

    A~17      marks [1 x 18]                          OK
    E~7       [1,2,3,4,3,2,1,2]                       OK
    E~8^(1)   [1,2,3,4,5,6,4,2,3]                     OK  <- the source's displayed vector
    E~8^(2)   [2,4,6,5,4,3,2,1,3]                     OK
    A~1       [1,1]                                   OK
    D~16      [1,1,2,...,2,1,1]                       OK
    A~1*      [1,1]                                   OK
    D~10      no null vector: the induced block is nondegenerate

The first E8 is the decisive one: the solved null vector is `[1,2,3,4,5,6,4,2,3]` on the chain
13,14,15,16,17,0,1,2,18, which is the vector the article displays as
n(E~8^(1)) = r_13 + 2r_14 + 3r_15 + 4r_16 + 5r_17 + 6r_0 + 4r_1 + 2r_2 + 3r_18.  Six of the
seven components are therefore validated by the candidate.

The D10 component is not: as the candidate stands its vertices {18, 17, 0, ..., 7, 19} carry
only ten edges (a tree), so the block is nondegenerate and has no null vector, and a search over
every single additional pairing-1 edge inside that block repairs nothing -- the failure is
structural, not a missing edge. That matches the independent visual reading recorded above,
which also came out one edge short there. So the remaining source question is the internal
incidence of D10 (its two arms and where 17, 18, 19 attach), and it is the only thing standing
between this candidate and a complete 24-root Gram matrix. Lemma 4.7's coincidence
n(D10) = n(E7) is the check that will confirm the repair, and it cannot run until then.
