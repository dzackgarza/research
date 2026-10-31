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
