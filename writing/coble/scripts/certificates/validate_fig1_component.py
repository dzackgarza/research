"""Validate a transcribed component of AET Figure 1 against the affine Dynkin diagram.

Run on the shared development image:

    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/validate_fig1_component.py

What it does: takes a candidate component as a set of Fig. 1 node labels plus the incidences
read off the artwork, and asks whether the resulting graph is the Dynkin diagram of the affine
Cartan type the caption names -- `CartanType(shape).dynkin_diagram()`, compared as an
edge-labelled graph.  This is the maintained object; nothing here re-derives the diagram.

The two candidates tested are the two readings of `fig-wD10wE7`'s 8-node component:
  (a) bold 12-20 included,  fork at 12  -> arms (3, 3, 1)
  (b) as read with node 13 as the fork  -> arms (2, 3, 1) / (2, 3, 2) depending on which
      of 12-11 and 12-20 is counted in which arm.
"""
import sys

from sage.all import Graph
from sage.combinat.root_system.cartan_type import CartanType

print("python", sys.version.split()[0])

shape = CartanType(["E", 7, 1])
D = shape.dynkin_diagram()
print("affine E7 diagram:", D.order(), "nodes,", D.size(), "edges")
print(D)

# the transcription, as read off the standalone artwork
read_edges = [(12, 13), (13, 14), (14, 15), (12, 11), (11, 10), (10, 9), (12, 20)]
nodes = (12, 13, 14, 15, 11, 10, 9, 20)

G = Graph({v: [] for v in nodes})
for a, b in read_edges:
    G.add_edge(a, b)
G.relabel({v: i for i, v in enumerate(nodes)})
print("\ntranscribed component:", G.order(), "nodes,", G.size(), "edges; degree sequence",
      sorted(G.degree(), reverse=True))
H = Graph({v: D.neighbors(v) for v in D})
print("target degree sequence:", sorted(D.degree(), reverse=True))
print("isomorphic to the affine E7 diagram:", G.is_isomorphic(H))

# and the same check for the 11-node component as read, which is one edge short of unicyclic
read_D = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 17), (6, 7), (17, 18), (19, 7)]
nodes_D = (0, 1, 2, 3, 4, 5, 6, 7, 17, 18, 19)
GD = Graph({v: [] for v in nodes_D})
for a, b in read_D:
    GD.add_edge(a, b)
GD.relabel({v: i for i, v in enumerate(nodes_D)})
shapeD = CartanType(["D", 10, 1])
DD = shapeD.dynkin_diagram()
HD = Graph({v: DD.neighbors(v) for v in DD})
print("\ndecimal-D transcription:", GD.order(), "nodes,", GD.size(), "edges; degree sequence",
      sorted(GD.degree(), reverse=True))
print("affine D10 target:", DD.order(), "nodes,", DD.size(), "edges; degree sequence",
      sorted(DD.degree(), reverse=True))
print("isomorphic to the affine D10 diagram:", GD.is_isomorphic(HD))
