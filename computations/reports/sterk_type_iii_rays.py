"""The Type III ray counts of the five Enriques semifans, at the owner, on both families.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-main/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/sterk_type_iii_rays.py

Two root families are compared, and neither is transported by position or count:

  (script)  computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage,
            the reconstruction from Sterk's closed-form root vectors in
            L_- = H + H(2) + E8(-2), whose Gram in the a_i order of that file is
            degenerate of rank 10 and Schlaefli signature (9,1);
  (library) Sterk.diagrams()["Sterk_k"], the maintained rooted diagram, whose
            vertices are the dissertation's r_0..r_{n-1}.

The two are matched as angle-labelled graphs -- vertices carry their root norm,
edges their Coxeter weight, the sign of a pairing dropped as a Coxeter diagram
drops it -- and then the retained transport is *re*-checked on the signed Gram: every
entry b(a_i, a_j) must equal b(r_phi(i), r_phi(j)), signs and magnitudes, not only
the norm and the Coxeter order.  The angle labelling cannot see that: b and -b give
one Coxeter weight, and so do 2 and 4 between roots of unequal length, so a map that
preserves norms and weights need not preserve a single signed pairing.  The signed
check is what makes the transport a lattice-isometry statement rather than a
diagram statement, and the number of coset elements that pass it is reported.

The subdiagrams are the owner's: CoxeterDiagrams.maximal_elliptic_subdiagrams()
decides ellipticity and maximality on vertex sets (sage-extensions
6ce8cdeb2b6d579c766f30f41811f482d333ae3c).  Maximal elliptic subdiagrams occur
in several ranks; a Type III *ray* needs elliptic rank 9, since v^perp/Zv has
rank 10 and signature (1,9) and the cone dimension is the ambient rank minus the
elliptic rank (AET, Thm 4.3), so rank 9 is selected here and rank 7 or 8 is not
counted.  The action is the diagram's labelled automorphism group.
"""
import os
import sys

from sage.all import Graph, QQ, ZZ

from sage_extensions.all import CoxeterDiagrams, Lattices, Sterk

SOURCE = '/repo/computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage'
MANUSCRIPT = [4, 8, 15, 12, 17]     # 900-five-cusps.md, Type III, Coxeter compactification


def load_definitions(path):
    """Execute the reconstruction with its module-level reports disabled.

    They take minutes (exact eigenvalues of every vertex subset) and their output
    is kept in computations/reports/sterk-cusp-diagrams-run.txt; the definitions
    are executed unchanged.
    """
    text = open(path).read()
    for call in ('report', 'primitivity_report', 'qrank_report', 'rank_condition_report'):
        target = '\n%s()\n' % call
        assert text.count(target) == 1, (call, text.count(target))
        text = text.replace(target, '\npass  # %s() disabled: its output is in the -run.txt\n' % call)
    namespace = {'__name__': 'sterk_cusp_diagrams'}
    exec('from sage.all import *', namespace)
    exec(compile(text, path, 'exec'), namespace)
    return namespace


def coxeter_weight(cos2):
    table = {QQ(0): 2, QQ(1) / 4: 3, QQ(1) / 2: 4, QQ(3) / 4: 6, QQ(1): 'infinity'}
    if cos2 not in table:
        raise ValueError('cos^2 = %s is not a Coxeter weight' % cos2)
    return table[cos2]


def angle_graph(index_set, gram):
    """The angle-labelled graph: vertices partitioned by root norm, edges by weight."""
    vertices = tuple(index_set)
    n = len(vertices)
    graph = Graph(loops=False, multiedges=False)
    graph.add_vertices(vertices)
    norms = {vertex: int(gram[i, i]) for i, vertex in enumerate(vertices)}
    for i, left in enumerate(vertices):
        for j in range(i + 1, n):
            if gram[i, j]:
                cos2 = QQ(gram[i, j]) ** 2 / (QQ(gram[i, i]) * QQ(gram[j, j]))
                graph.add_edge(left, vertices[j], coxeter_weight(cos2))
    classes = {}
    for vertex in vertices:
        classes.setdefault(norms[vertex], []).append(vertex)
    return graph, [classes[key] for key in sorted(classes)]


def maintained_angle_graph(diagram):
    """The same angle labelling, read off the maintained rooted diagram itself.

    Its retained root Gram is returned in owned scalars, which do not coerce into
    QQ; the root squares and the Coxeter entries are the diagram's public accessors
    and carry exactly the two data an angle-labelled graph has.
    """
    vertices = tuple(diagram.index_set())
    graph = Graph(loops=False, multiedges=False)
    graph.add_vertices(vertices)
    norms = {}
    for vertex in vertices:
        norms[vertex] = int(diagram.root(vertex).q())
    for i, left in enumerate(vertices):
        for right in vertices[i + 1:]:
            entry = diagram.coxeter_entry(left, right)
            if entry.is_countably_infinite():
                graph.add_edge(left, right, 'infinity')
            elif int(entry) != 2:
                graph.add_edge(left, right, int(entry))
    classes = {}
    for vertex in vertices:
        classes.setdefault(norms[vertex], []).append(vertex)
    return graph, [classes[key] for key in sorted(classes)]


def canonical(graph, partition):
    return graph.canonical_label(partition=partition, edge_labels=True,
                                 certificate=True, algorithm='sage')


def transport(source, target, label):
    (Gs, ps), (Gt, pt) = source, target
    Hs, ds = canonical(Gs, ps)
    Ht, dt = canonical(Gt, pt)
    assert Hs == Ht, '%s: the two angle-labelled diagrams are not isomorphic' % label
    dt_inverse = {canonical_vertex: vertex for vertex, canonical_vertex in dt.items()}
    phi = {vertex: dt_inverse[canonical_vertex] for vertex, canonical_vertex in ds.items()}
    aut = Gs.automorphism_group(partition=ps, edge_labels=True, algorithm='sage')
    return phi, aut.order()


def maintained_signed_gram(diagram):
    """The maintained diagram's root Gram, signed, over ZZ.

    The retained tensor's entries are owned scalars, which do not coerce into QQ but
    do convert to ZZ; the row order is ``diagram.index_set()``.
    """
    gram = diagram.root_gram_tensor()
    n = int(diagram.cardinality())
    return [[int(gram[i, j]) for j in range(n)] for i in range(n)]


def preserves_signed_gram(matrix, signed, phi, position):
    """Whether ``phi`` carries every signed pairing of ``matrix`` to the maintained one.

    ``phi`` maps a script index to a maintained vertex label, ``position`` that label to
    its index in the maintained Gram.
    """
    n = matrix.nrows()
    return all(matrix[i, j] == signed[position[phi[i]]][position[phi[j]]]
               for i in range(n) for j in range(n))


def orbits(action, sets):
    remaining, reps = list(sets), []
    while remaining:
        representative = remaining[0]
        reps.append(representative)
        orbit = {frozenset(g(vertex) for vertex in representative) for g in action}
        remaining = [other for other in remaining if other not in orbit]
    return reps


def main():
    definitions = load_definitions(SOURCE)
    gram_of = definitions['gram_of']
    library = Sterk.diagrams()

    for number, (name, build) in enumerate(definitions['CUSPS'], start=1):
        M = gram_of(build())
        n = M.nrows()
        L = Lattices(ZZ)([list(row) for row in M.rows()])
        script = CoxeterDiagrams().from_roots({i: L.basis_vector(i) for i in range(n)})
        maintained = library['Sterk_%d' % number]
        assert int(maintained.cardinality()) == n, (name, n, int(maintained.cardinality()))

        phi, ambiguity = transport(
            angle_graph(range(n), M),
            maintained_angle_graph(maintained),
            name)
        assert len(set(phi.values())) == n

        # The angle labelling is blind to signs and to the magnitude 2 versus 4 between
        # roots of unequal length, so the transport is re-decided on the signed Gram.
        signed = maintained_signed_gram(maintained)
        position = {vertex: index for index, vertex in enumerate(maintained.index_set())}
        assert sorted(position) == sorted(set(phi.values()))
        script_graph, script_partition = angle_graph(range(n), M)
        script_action = script_graph.automorphism_group(
            partition=script_partition, edge_labels=True, algorithm='sage')
        candidates = [{v: phi[g(v)] for v in range(n)} for g in script_action]
        passing = [candidate for candidate in candidates
                   if preserves_signed_gram(M, signed, candidate, position)]
        assert passing, ('%s: no element of the transport coset preserves the signed Gram' % name)
        phi = passing[0]

        script_sets = [frozenset(int(vertex) for vertex in diagram.index_set())
                       for diagram in script.maximal_elliptic_subdiagrams(connected=False)]
        maintained_sets = [frozenset(diagram.index_set())
                           for diagram in maintained.maximal_elliptic_subdiagrams(connected=False)]
        assert len(script_sets) == len(maintained_sets), (name, len(script_sets), len(maintained_sets))
        # Every coset representative carries the script's sets onto the same maintained
        # sets, the owner's enumeration being invariant under the diagram's symmetries.
        transported = {frozenset(phi[int(vertex)] for vertex in candidate)
                       for candidate in script_sets}
        assert transported == set(maintained_sets), \
            '%s: the owner\'s maximal elliptic sets are not carried by the signed transport' % name

        diagram_of = {}
        for candidate in maintained_sets:
            diagram_of[candidate] = None
        rank_of = {}
        for diagram in maintained.maximal_elliptic_subdiagrams(connected=False):
            candidate = frozenset(diagram.index_set())
            rank_of[candidate] = (diagram.positive_inertia_index(),
                                  diagram.negative_inertia_index(),
                                  diagram.zero_inertia_index())
        shapes = {}
        for candidate, inertia in rank_of.items():
            assert inertia[1] == 0 and inertia[2] == 0, (name, candidate, inertia)
            shapes[inertia[0]] = shapes.get(inertia[0], 0) + 1
        rays = [candidate for candidate in maintained_sets if rank_of[candidate][0] == 9]

        graph, partition = maintained_angle_graph(maintained)
        action = graph.automorphism_group(partition=partition, edge_labels=True, algorithm='sage')
        reps = orbits(action, rays)

        print('=' * 72)
        print('%-4s %-26s %2d roots  rank(v^perp/Zv)=%2d  elliptic rank 9 needed'
              % (number, name, n, M.rank()))
        print('   maximal elliptic subdiagrams: %d, by elliptic rank %s'
              % (len(maintained_sets), sorted(shapes.items())))
        print('   rank 9: %d subdiagrams, |Aut| = %d, orbits %2d  (manuscript %2d)%s'
              % (len(rays), action.order(), len(reps), MANUSCRIPT[number - 1],
                 '' if len(reps) == MANUSCRIPT[number - 1] else '  *** MISMATCH'))
        print('   transport a_{i+1} -> library vertex: %d of the %d angle-preserving maps '
              'preserve every signed pairing' % (len(passing), ambiguity))
        print('   a signed transport, determined up to %d relabellings:' % len(passing))
        print('      %s' % [phi[i] for i in range(n)])
        for representative in reps:
            ordered = sorted(representative, key=lambda vertex: int(str(vertex)[1:]))
            print('      orbits: %s' % ordered)
        sys.stdout.flush()


main()
