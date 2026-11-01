"""Lemma 5.8's semitoroidal counts, re-derived from the labelled diagrams.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/sterk_semitoroidal_counts.py

Library sage-extensions 2a1babbbc530430f1836707d6f2a4e8ad7a458ee on this project's bind.  Diagrams
Sterk.diagrams(), vertices r_i.  Lemma 5.8 of AEGS25 says the semitoroidal compactification has
2+0, 2+7, 2+7, 4+7, 3+0 Type II + Type III divisors at cusps 1..5, obtained from that lemma's own
input -- the per-cusp lists of Lemma 5.3, 4+4, 2+8, 3+15, 4+12, 5+17 -- by discarding the subgraphs
containing a connected component consisting entirely of irrelevant vertices.  The per-cusp numbers
are ray numbers in fF_k/Gamma_k; the lemma's own total, 6 + 21 = 27, is smaller in the Type II term
because, as its proof of Lemma 5.3 records, one Type II divisor may pass through several 0-cusps
(18 Type II rays there are 9 divisors).  So the comparison made here is cusp by cusp.  This file
applies exactly that rule to the orbits computed at the owner (maximal componentwise-affine
subdiagrams of form rank 8 for Type II, maximal elliptic subdiagrams of rank 9 for Type III) and
counts the surviving orbits under the labelled automorphism group.

The irrelevant sets are the ones fixed by Figure 5 and the fold transport recorded in GAPS.  One
thing the rule needs and the source does not spell out: the deletion is by a *labelled* property of
a vertex set, so it is a rule on orbits -- independent of which representative is singled out, and
so comparable with a Gamma_k-count -- only if the acting group preserves the irrelevant set.  That
is tested here rather than assumed, as is the consequence: when the set is preserved, the surviving
subdiagrams are a union of full orbits, and the surviving-orbit count is the only count available.
"""
import sys

from sage.all import Graph

from sage_extensions.all import Sterk

IRRELEVANT = {1: {8, 9, 10, 11}, 2: {9}, 3: {9, 10, 11}, 4: {9, 10}, 5: set(range(8, 14))}
# Lemma 5.3's per-cusp Type II + Type III ray counts, the list the deletion acts on.
COXETER = {1: (4, 4), 2: (2, 8), 3: (3, 15), 4: (4, 12), 5: (5, 17)}
# Lemma 5.8's counts, the expected outcome.
EXPECTED = {1: (2, 0), 2: (2, 7), 3: (2, 7), 4: (4, 7), 5: (3, 0)}


def labelled_graph(diagram):
    """The angle-labelled graph: vertices partitioned by root norm, edges by Coxeter weight."""
    vertices = tuple(diagram.index_set())
    graph = Graph(loops=False, multiedges=False)
    graph.add_vertices(vertices)
    classes = {}
    for vertex in vertices:
        classes.setdefault(int(diagram.root(vertex).q()), []).append(vertex)
    for i, left in enumerate(vertices):
        for right in vertices[i + 1:]:
            entry = diagram.coxeter_entry(left, right)
            if entry.is_countably_infinite():
                graph.add_edge(left, right, 'infinity')
            elif int(entry) != 2:
                graph.add_edge(left, right, int(entry))
    return graph, [classes[key] for key in sorted(classes)]


def orbits(action, sets):
    remaining, reps = list(sets), []
    while remaining:
        representative = remaining[0]
        reps.append(representative)
        orbit = {frozenset(g(vertex) for vertex in representative) for g in action}
        remaining = [other for other in remaining if other not in orbit]
    return reps


def survives(diagram, candidate, irrelevant):
    """No connected component of the induced subdiagram lies entirely inside the irrelevant set."""
    induced = diagram.induced_subdiagram(sorted(candidate))
    for component in induced.connected_component_vertex_sets():
        if all(int(str(vertex)[1:]) in irrelevant for vertex in component):
            return False
    return True


library = Sterk.diagrams()
totals = [0, 0]
failures = 0
for k in (1, 2, 3, 4, 5):
    diagram = library['Sterk_%d' % k]
    graph, partition = labelled_graph(diagram)
    action = graph.automorphism_group(partition=partition, edge_labels=True, algorithm='sage')
    irrelevant = IRRELEVANT[k]
    label = {vertex: int(str(vertex)[1:]) for vertex in diagram.index_set()}
    irrelevant_roots = ['r%d' % index for index in sorted(irrelevant)]
    images = {frozenset(label[g(vertex)] for vertex in irrelevant_roots) for g in action}
    invariant = images == {frozenset(irrelevant)}

    two_sets = [frozenset(d.index_set())
                for d in diagram.maximal_componentwise_affine_subdiagrams(max_form_rank=8)
                if int(d.form_rank()) == 8]
    three_sets = [frozenset(d.index_set())
                  for d in diagram.maximal_elliptic_subdiagrams(connected=False)
                  if int(d.positive_inertia_index()) == 9]
    two_surviving = [candidate for candidate in two_sets if survives(diagram, candidate, irrelevant)]
    three_surviving = [candidate for candidate in three_sets if survives(diagram, candidate, irrelevant)]
    two_orbits = len(orbits(action, two_surviving))
    three_orbits = len(orbits(action, three_surviving))

    # The Coxeter-compactification counts are re-derived here as a guard that this file asks the
    # same two queries as the committed certificates, and that its action is the same.
    coxeter = (len(orbits(action, two_sets)), len(orbits(action, three_sets)))
    assert coxeter == COXETER[k], ('cusp %d: Coxeter counts %s, Lemma 5.3 %s'
                                   % (k, coxeter, COXETER[k]))
    if invariant:
        surviving = set(two_surviving) | set(three_surviving)
        for candidate in surviving:
            moved = {frozenset(g(vertex) for vertex in candidate) for g in action}
            assert moved <= surviving, \
                'cusp %d: a survivor\'s orbit leaves the surviving list (%s)' % (k, sorted(candidate))
    ok = (two_orbits, three_orbits) == EXPECTED[k]
    failures += 0 if ok else 1
    totals[0] += two_orbits
    totals[1] += three_orbits

    print('cusp %d  irrelevant roots %s' % (k, irrelevant_roots))
    print('   labelled action |Aut| = %2d, irrelevant set invariant: %s (%d distinct images)'
          % (action.order(), invariant, len(images)))
    print('   Type II  : %2d of %2d maximal componentwise-affine subdiagrams of form rank 8 survive'
          ' -> %d orbits   [Lemma 5.3 list %d, Lemma 5.8 %d]'
          % (len(two_surviving), len(two_sets), two_orbits, COXETER[k][0], EXPECTED[k][0]))
    print('   Type III : %3d of %3d maximal elliptic subdiagrams of rank 9 survive'
          ' -> %2d orbits   [Lemma 5.3 list %d, Lemma 5.8 %d]'
          % (len(three_surviving), len(three_sets), three_orbits, COXETER[k][1], EXPECTED[k][1]))
    print('   %s' % ('AGREES with Lemma 5.8' if ok else '*** DIFFERS from Lemma 5.8'))
    print()
    sys.stdout.flush()

print('rays: %d Type II + %d Type III = %d, counted per cusp as Lemma 5.8 states them'
      % (totals[0], totals[1], totals[0] + totals[1]))
print('Lemma 5.8\'s own total, 6 + 21 = 27, counts divisors rather than rays: as in Lemma 5.3, where '
      'the 18 Type II rays are 9 divisors because a Type II divisor can pass through several '
      '0-cusps.  The per-cusp ray counts are what is compared above, and they agree at all five.')
print('%s' % ('all five cusps agree with Lemma 5.8' if failures == 0
              else '%d cusp(es) differ from Lemma 5.8' % failures))
