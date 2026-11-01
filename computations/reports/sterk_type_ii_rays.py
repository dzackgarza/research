"""The Type II ray counts of the five Enriques semifans, at the owner's semantic query.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/sterk_type_ii_rays.py

What is counted, and with which call.  A Type II ray is an orbit of *maximal
componentwise-affine* subdiagrams of geometric rank eight.  The query is
CoxeterDiagrams.maximal_componentwise_affine_subdiagrams(max_form_rank=8) of
sage-extensions 2a1babbbc530430f1836707d6f2a4e8ad7a458ee, whose family is every
nonempty subdiagram all of whose connected components are affine -- a single affine
component included -- with maximality decided over that whole family *before* any
cap, and whose form_rank() is the geometric rank, vertices minus nullity.  A cap is
not an equality, so the results are filtered to form_rank() == 8 afterwards; a
maximal union of rank 7 is excluded by that filter rather than by the cap.  max_rank
is the owner's vertex-count cap and is not passed here at all.

Two families, as in the Type III run, and neither is transported by position: the
reconstruction's Gram in the a_i order of sterk_cusp_diagrams.sage, and
Sterk.diagrams()["Sterk_k"] with the manuscript's r_i.  The transport is the
angle-labelled isomorphism, re-decided on the signed Gram, and the painstakingly
checked statement -- that both families give the same sets, element for element
under that transport -- is asserted rather than assumed.  The action is the
labelled automorphism group of the diagram.
"""
import sys

from sage.all import Graph, QQ, ZZ

from sage_extensions.all import CoxeterDiagrams, Lattices, Sterk

SOURCE = '/repo/computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage'
MANUSCRIPT = [4, 2, 3, 4, 5]      # 900-five-cusps.md, Type II, Coxeter compactification
FORM_RANK = 8                     # geometric rank of a Type II ray: vertices minus components


def load_definitions(path):
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
    vertices = tuple(diagram.index_set())
    graph = Graph(loops=False, multiedges=False)
    graph.add_vertices(vertices)
    norms = {vertex: int(diagram.root(vertex).q()) for vertex in vertices}
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


def maintained_signed_gram(diagram):
    gram = diagram.root_gram_tensor()
    n = int(diagram.cardinality())
    return [[int(gram[i, j]) for j in range(n)] for i in range(n)]


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


def preserves_signed_gram(matrix, signed, phi, position):
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


def ray_sets(diagram):
    """Maximal componentwise-affine subdiagrams of geometric rank exactly eight."""
    everything = list(diagram.maximal_componentwise_affine_subdiagrams(max_form_rank=FORM_RANK))
    ranks = [int(subdiagram.form_rank()) for subdiagram in everything]
    rays = [frozenset(subdiagram.index_set()) for subdiagram in everything
            if int(subdiagram.form_rank()) == FORM_RANK]
    return everything, ranks, rays


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

        phi, ambiguity = transport(angle_graph(range(n), M), maintained_angle_graph(maintained), name)
        signed = maintained_signed_gram(maintained)
        position = {vertex: index for index, vertex in enumerate(maintained.index_set())}
        script_graph, script_partition = angle_graph(range(n), M)
        action_script = script_graph.automorphism_group(
            partition=script_partition, edge_labels=True, algorithm='sage')
        candidates = [{v: phi[g(v)] for v in range(n)} for g in action_script]
        passing = [candidate for candidate in candidates
                   if preserves_signed_gram(M, signed, candidate, position)]
        assert passing, '%s: no transport preserves the signed Gram' % name
        phi = passing[0]

        everything_r, ranks_r, rays_r = ray_sets(maintained)
        everything_s, ranks_s, rays_s = ray_sets(script)

        transported = {frozenset(phi[int(vertex)] for vertex in candidate) for candidate in rays_s}
        assert transported == set(rays_r), \
            '%s: the two families disagree on the rank-eight maximal unions' % name
        assert sorted(ranks_r) == sorted(ranks_s), (name, ranks_r, ranks_s)

        graph, partition = maintained_angle_graph(maintained)
        action = graph.automorphism_group(partition=partition, edge_labels=True, algorithm='sage')
        reps = orbits(action, rays_r)

        shapes = {}
        for rank in ranks_r:
            shapes[rank] = shapes.get(rank, 0) + 1
        print('=' * 74)
        print('%-4s %-26s %2d roots  transport: %d of %d signed  |Aut| = %d'
              % (number, name, n, len(passing), ambiguity, action.order()))
        print('   maximal componentwise-affine (owner): %d, by geometric rank %s'
              % (len(everything_r), sorted(shapes.items())))
        print('   of those, rank exactly %d: %2d  ->  orbits %d   (manuscript %d)%s'
              % (FORM_RANK, len(rays_r), len(reps), MANUSCRIPT[number - 1],
                 '' if len(reps) == MANUSCRIPT[number - 1] else '  *** MISMATCH'))
        for representative in reps:
            ordered = sorted(representative, key=lambda vertex: int(str(vertex)[1:]))
            print('      orbit: %s' % ordered)
        sys.stdout.flush()


main()
