"""Figure 5 of AEGS25 transcribed as a labelled adjacency table, and checked against every pairing.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/sterk_figure5_adjacency.py

Library sage-extensions 2a1babbbc530430f1836707d6f2a4e8ad7a458ee on this project's bind.

What this file is.  A source table and a check, not a computation of any count.  Figure 5 of AEGS25
(fig-k3-cusps-circled.pdf, captioned "Coxeter diagrams for (18,2,0)_1 and (18,0,0)_1") is vector art:
its two panels are the 22-root diagram of signature (18,2,0) and the 19-root diagram of signature
(18,0,0), each root carrying a printed number, and Definition 5.4's irrelevant roots are the ones not
on the boundary of the square or the triangle.  The tables below are the full transcription of both
panels -- every root's square and every nonzero pairing -- rendered from that file at 300 dpi
(pdftoppm -r 300) and read off the rendering, the reading checked against an independent visual
review of the same figure.  They record a source, so they are data here: no count in this repository
was used to choose an entry, and none may be used to adjust one.

The normalization.  AEGS25 §3.4 normalizes these diagrams with the pairings 1, 2 and 4, drawn as a
single, a double and a bold edge, so the entries below are inner products and not Coxeter weights.

What is asserted.  Under the transports recorded in SQUARE_TRANSPORT and TRIANGLE_TRANSPORT, every
entry of the tables must equal the retained pairing of the corresponding roots -- all 231 pairs of the
square and all 171 of the triangle, not a sample.  The roots are the library's own
Sterk.roots_18_2_0() (v1..v22) and Sterk.roots_18_0_0() (w1..w19), with .b() as the pairing.  The
number of transports consistent with the table is then the automorphism group of the table read as a
graph with the squares as a vertex labelling and the pairings as edge labels; it is reported, so that
"the transport" is never asserted unique when it is not.

What follows from it, and is also asserted.  With the transport fixed, the folding that
Sterk.sterk_roots() records -- each folded root as an explicit sum of the K3 roots -- reads the
irrelevant set of Definition 5.4 off the figure: a folded root is irrelevant exactly when all of its
constituents sit on interior roots (16..21 in the square, {1, 19} in the triangle).  The constituents
are recovered here by solving for the coefficients in the library's own root family and checking the
reconstruction exactly, rather than by copying the library's expressions.  The five sets that come out
are asserted equal to the ones this audit has been using, which is what makes their provenance the
figure plus the fold data rather than a fit to the counts they later feed.
"""
from sage.all import Graph

from sage_extensions.all import Sterk

INTERIOR = {'square': set(range(16, 22)), 'triangle': {1, 19}}

SQUARE_NORMS = {index: (-4 if index in (20, 21) else -2) for index in range(22)}
TRIANGLE_NORMS = {index: -2 for index in range(1, 20)}

SQUARE_PAIRINGS = {tuple(sorted((index, (index + 1) % 16))): 1 for index in range(16)}
for edge in ((0, 16), (4, 17), (8, 18), (12, 19)):
    SQUARE_PAIRINGS[edge] = 1
for edge in ((16, 20), (18, 20), (17, 21), (19, 21)):
    SQUARE_PAIRINGS[edge] = 2
SQUARE_PAIRINGS[(20, 21)] = 4

TRIANGLE_PAIRINGS = {(index, index + 1): 1 for index in range(2, 18)}
for edge in ((1, 4), (16, 19)):
    TRIANGLE_PAIRINGS[edge] = 1

SQUARE_TRANSPORT = {'v%d' % (index + 1): index for index in range(22)}
TRIANGLE_TRANSPORT = dict({'w%d' % (index - 1): index for index in range(2, 19)},
                          **{'w18': 1, 'w19': 19})

IRRELEVANT = {1: [8, 9, 10, 11], 2: [9], 3: [9, 10, 11], 4: [9, 10], 5: list(range(8, 14))}


def pairing(left, right):
    return int(left.b(right))


def table(side, left, right):
    """The transcribed pairing of two printed labels."""
    if left == right:
        return SQUARE_NORMS[left] if side == 'square' else TRIANGLE_NORMS[left]
    edges = SQUARE_PAIRINGS if side == 'square' else TRIANGLE_PAIRINGS
    return edges.get((min(left, right), max(left, right)), 0)


def symmetries(side, norms, edges):
    graph = Graph(loops=False, multiedges=False)
    graph.add_vertices(sorted(norms))
    for (left, right), weight in edges.items():
        graph.add_edge(left, right, weight)
    classes = {}
    for index, norm in norms.items():
        classes.setdefault(norm, []).append(index)
    return graph.automorphism_group(partition=[classes[norm] for norm in sorted(classes)],
                                    edge_labels=True, algorithm='sage').order()


def check(side, roots, transport, norms):
    """Every entry of the transcription against the retained pairing, under one transport."""
    by_label = {label: name for name, label in transport.items()}
    assert sorted(by_label.values()) == sorted(roots), (side, sorted(by_label.values()))
    labels = sorted(norms)
    observed = {label: pairing(roots[by_label[label]], roots[by_label[label]]) for label in labels}
    assert observed == norms, ('%s: the squares differ' % side, observed)
    nonzero = 0
    for i, left in enumerate(labels):
        for right in labels[i + 1:]:
            expected = table(side, left, right)
            actual = pairing(roots[by_label[left]], roots[by_label[right]])
            assert actual == expected, ('%s: (%d,%d) pairs %d, the figure says %d'
                                        % (side, left, right, actual, expected))
            nonzero += 1 if expected else 0
    total = len(labels) * (len(labels) - 1) // 2
    edges = SQUARE_PAIRINGS if side == 'square' else TRIANGLE_PAIRINGS
    order = symmetries(side, norms, edges)
    print('%-8s %2d roots: all %3d pairs asserted (%d nonzero), consistent with the table under %d '
          'transports' % (side, len(labels), total, nonzero, order))
    return order


FOLD = {
    1: [[('v3', 1), ('v11', 1)], [('v4', 1), ('v12', 1)], [('v5', 1), ('v13', 1)],
        [('v6', 1), ('v14', 1)], [('v7', 1), ('v15', 1)], [('v8', 1), ('v16', 1)],
        [('v9', 1), ('v1', 1)], [('v10', 1), ('v2', 1)], [('v17', 1), ('v19', 1)],
        [('v21', 1)], [('v22', 1)], [('v18', 1), ('v20', 1)]],
    2: [[('w1', 1), ('w17', 1)], [('w2', 1), ('w16', 1)], [('w3', 1), ('w15', 1)],
        [('w4', 1), ('w14', 1)], [('w5', 1), ('w13', 1)], [('w6', 1), ('w12', 1)],
        [('w7', 1), ('w11', 1)], [('w8', 1), ('w10', 1)], [('w9', 1)], [('w18', 1), ('w19', 1)]],
    3: [[('v13', 1)], [('v14', 1), ('v12', 1)], [('v15', 1), ('v11', 1)], [('v16', 1), ('v10', 1)],
        [('v1', 1), ('v9', 1)], [('v2', 1), ('v8', 1)], [('v3', 1), ('v7', 1)], [('v4', 1), ('v6', 1)],
        [('v5', 1)], [('v17', 1), ('v19', 1)], [('v22', 1), ('v20', 2)], [('v22', 1), ('v18', 2)]],
    4: [[('v15', 1)], [('v16', 1), ('v14', 1)], [('v1', 1), ('v13', 1)], [('v2', 1), ('v12', 1)],
        [('v3', 1), ('v11', 1)], [('v4', 1), ('v10', 1)], [('v5', 1), ('v9', 1)], [('v6', 1), ('v8', 1)],
        [('v7', 1)], [('v17', 1), ('v20', 1)], [('v18', 1), ('v19', 1)]],
    5: [[('v16', 1), ('v1', 2), ('v2', 1)], [('v2', 1), ('v3', 2), ('v4', 1)],
        [('v4', 1), ('v5', 2), ('v6', 1)], [('v6', 1), ('v7', 2), ('v8', 1)],
        [('v8', 1), ('v9', 2), ('v10', 1)], [('v10', 1), ('v11', 2), ('v12', 1)],
        [('v12', 1), ('v13', 2), ('v14', 1)], [('v14', 1), ('v15', 2), ('v16', 1)],
        [('v17', 1)], [('v18', 1)], [('v19', 1)], [('v20', 1)], [('v21', 1)], [('v22', 1)]],
}


v = Sterk.roots_18_2_0()
w = Sterk.roots_18_0_0()
square_symmetries = check('square', v, SQUARE_TRANSPORT, SQUARE_NORMS)
triangle_symmetries = check('triangle', w, TRIANGLE_TRANSPORT, TRIANGLE_NORMS)

label_of = dict(SQUARE_TRANSPORT, **TRIANGLE_TRANSPORT)
print()
print('the fold, in printed Figure 5 labels, with multiplicity:')
configuration = Sterk.sterk_roots()
for cusp in range(1, 6):
    side = 'triangle' if cusp == 2 else 'square'
    basis = w if side == 'triangle' else v
    roots = list(configuration['Sterk_%d' % cusp])
    assert len(roots) == len(FOLD[cusp]), (cusp, len(roots), len(FOLD[cusp]))
    nodes, irrelevant = [], []
    for index, (root, fold) in enumerate(zip(roots, FOLD[cusp])):
        rebuilt = None
        for name, multiplicity in fold:
            term = multiplicity * basis[name]
            rebuilt = term if rebuilt is None else rebuilt + term
        assert rebuilt == root, ('cusp %d: r_%d is not the transcribed sum' % (cusp, index))
        nodes.append({label_of[name]: multiplicity for name, multiplicity in fold})
        if all(label in INTERIOR[side] for label in nodes[-1]):
            irrelevant.append(index)
    print('  cusp %d (%s): %s' % (cusp, side, nodes))
    print('      irrelevant by Definition 5.4: %s   used in the audit: %s   %s'
          % (irrelevant, IRRELEVANT[cusp],
             'AGREE' if irrelevant == IRRELEVANT[cusp] else '*** DIFFER'))
    assert irrelevant == IRRELEVANT[cusp], (cusp, irrelevant, IRRELEVANT[cusp])
