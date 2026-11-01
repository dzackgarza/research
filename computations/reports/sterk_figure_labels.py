"""The label map between Sterk's script and the manuscript's figure numbering.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/sterk_figure_labels.py

Two labelled diagrams are compared per cusp, each read from its own source and
neither transported by position or by count:

  (script)  the reconstruction in computations/scripts/sterk-enriques-cusps/
            sterk_cusp_diagrams.sage, whose Gram supplies a_i (1-based) with
            norm b(a_i, a_i) in {-2,-4} and Coxeter weight m_ij read off
            cos^2 = b_ij^2 / (b_ii b_jj): 1/4 -> 3, 1/2 -> 4, 3/4 -> 6, 1 -> infinity;
  (figure)  the tikz object in the pandoc configuration, figures/objects/coxeter/
            sterk-cusp-{1,3,4,5}.tikz, parsed for its \\coxeterroots (colour, where
            white is norm -2 and black norm -4), \\coxeterchain and \\coxeteredges.
            Its vertex i is root i of the ordered family, labelled r_i.

The isomorphism is searched as an isomorphism of edge-labelled graphs refined by
the norm partition (Graph.canonical_label with partition=, edge_labels=True,
algorithm="sage": this image's default Bliss backend segfaults).  It is not
unique, and the residual ambiguity is reported rather than resolved: the
isomorphisms of a pair of isomorphic graphs form a coset of the automorphism
group of either, of the size reported as |Aut|.

Cusp 2's object, vinberg-10-8-0.tikz, is drawn with the Vinberg macros rather
than the boolean ones and states its own vertex order instead of an edge list;
it is taken from the library family it names, Sterk.sterk_roots()["Sterk_2"],
composed with the permutation that object publishes.

Finally each of the manuscript's displayed subdiagram vertex sets is sent through
the map and classified by the owner's diagram predicates, so that the chapter's
"4 Type III rays, corresponding to the four elliptic subdiagrams displayed above"
can be read against the computed subdiagrams rather than against its own numbers.
"""
import os
import re
import shutil
import sys

from sage.all import Graph, QQ, ZZ

from sage_extensions.all import CoxeterDiagrams, Lattices

SOURCE = '/repo/computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage'
COXETER_OBJECTS = os.environ.get(
    'PANDOC_COXETER_OBJECTS', os.path.expanduser('~/.pandoc/figures/objects/coxeter'))


# ------------------------------------------------------------ the script side

def load_definitions(path):
    """Execute the reconstruction script with its module-level reports disabled.

    Its four report functions are slow (exact eigenvalues of every vertex subset)
    and their output is kept in computations/reports/sterk-cusp-diagrams-run.txt,
    so only the definitions are wanted here.  Anything else about the file is
    executed unchanged.
    """
    text = open(path).read()
    for call in ('report', 'primitivity_report', 'qrank_report', 'rank_condition_report'):
        target = '\n%s()\n' % call
        assert text.count(target) == 1, (call, text.count(target))
        text = text.replace(target, '\npass  # %s() disabled: its output is in the -run.txt\n' % call)
    namespace = {'__name__': 'sterk_cusp_diagrams'}
    exec('from sage.all import *', namespace)   # what sage's loader seeds for a .sage file
    exec(compile(text, path, 'exec'), namespace)
    return namespace


def coxeter_weight(cos2):
    table = {QQ(0): 2, QQ(1) / 4: 3, QQ(1) / 2: 4, QQ(3) / 4: 6, QQ(1): 'infinity'}
    if cos2 not in table:
        raise ValueError('the Gram gives cos^2 = %s, which is not a Coxeter weight' % cos2)
    return table[cos2]


def script_diagram(M, edge_label):
    n = M.nrows()
    norms = [int(M[i, i]) for i in range(n)]
    weights = {}
    for i in range(n):
        for j in range(i + 1, n):
            if M[i, j]:
                weights[(i, j)] = coxeter_weight(edge_label(M, i, j))
    return norms, weights


# ------------------------------------------------------------ the figure side

def argument(text, open_at):
    """The contents of the balanced brace group opening at ``open_at``, and its close."""
    depth, k = 0, open_at
    while k < len(text):
        if text[k] == '{':
            depth += 1
        elif text[k] == '}':
            depth -= 1
            if depth == 0:
                return text[open_at + 1:k], k
        k += 1
    raise ValueError('unbalanced braces from %d' % open_at)


def brace_split(text):
    parts, depth, current = [], 0, ''
    for ch in text:
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
        if ch == ',' and depth == 0:
            parts.append(current.strip())
            current = ''
        else:
            current += ch
    if current.strip():
        parts.append(current.strip())
    return parts


def macros(text, name):
    """Every occurrence of ``\\name{a}{b}..`` as a tuple of its arguments."""
    out = []
    for match in re.finditer(r'\\' + name + r'(?![a-zA-Z])', text):
        i, args = match.end(), []
        while True:
            while i < len(text) and text[i] in ' \t\n':
                i += 1
            if i < len(text) and text[i] == '{':
                value, i = argument(text, i)
                args.append(value)
                i += 1
            else:
                break
        out.append(tuple(args))
    return out


def weight_of(word):
    return 'infinity' if word == 'infinity' else int(word)


def figure_diagram(path):
    text = open(path).read()
    colour_norm = {'black': -4, 'white': -2}
    roots = macros(text, 'coxeterroots')
    assert len(roots) == 1, 'expected one \\coxeterroots in %s' % path
    norms = {}
    for entry in brace_split(roots[0][0]):
        fields = entry.split('/')
        norms[int(fields[0])] = colour_norm[fields[1]]
    assert sorted(norms) == list(range(len(norms))), (path, sorted(norms))
    weights = {}
    for weight, first, last in macros(text, 'coxeterchain'):
        for i in range(int(first), int(last)):
            weights[(i, i + 1)] = weight_of(weight)
    for weight, pairs in macros(text, 'coxeteredges'):
        for pair in brace_split(pairs):
            left, right = (int(x) for x in pair.split('/'))
            weights[(min(left, right), max(left, right))] = weight_of(weight)
    return [norms[i] for i in range(len(norms))], weights


# ------------------------------------------------------------------ the map

def labelled_graph(norms, weights):
    n = len(norms)
    G = Graph(loops=False, multiedges=False)
    G.add_vertices(range(n))
    for (i, j), m in sorted(weights.items()):
        G.add_edge(i, j, m)
    classes = {}
    for i in range(n):
        classes.setdefault(norms[i], []).append(i)
    return G, [classes[key] for key in sorted(classes)]


def canonical(G, partition):
    H, d = G.canonical_label(partition=partition, edge_labels=True,
                             certificate=True, algorithm='sage')
    return H, d


def transporter(source, target, names):
    """All isomorphisms source -> target, as dicts, with the automorphism used."""
    (Gs, ps), (Gt, pt) = source, target
    Hs, ds = canonical(Gs, ps)
    Ht, dt = canonical(Gt, pt)
    assert Hs == Ht, '%s: the two labelled diagrams are not isomorphic' % names
    dt_inverse = {canonical_vertex: vertex for vertex, canonical_vertex in dt.items()}
    phi = {vertex: dt_inverse[canonical] for vertex, canonical in ds.items()}
    aut = Gs.automorphism_group(partition=ps, edge_labels=True, algorithm='sage')
    maps = [{v: phi[g(v)] for v in Gs.vertices()} for g in aut]
    for candidate in maps:
        assert sorted(candidate.values()) == list(range(Gs.num_verts()))
    return phi, maps


CUSPS_FILE = '/repo/writing/dissertation/sections/3-part-main-theorem/7-chapter/900-five-cusps.md'


def displayed_sets(path):
    """The displayed subdiagram vertex sets, per cusp, read from the manuscript itself.

    Each cusp subsection draws its subdiagrams as ``\\pic[... subdiagram={...}]``
    over a pinned object, so the sets are the text's own and are not copied here.
    """
    text = open(path).read()
    sections = re.split(r'^#### Cusp (\d+)\s*$', text, flags=re.M)
    assert len(sections) == 11, len(sections)
    found = {}
    for number, body in zip(sections[1::2], sections[2::2]):
        sets = []
        for argument_text in re.findall(r'subdiagram=\{([0-9,\s]*)\}', body):
            sets.append([int(entry) for entry in argument_text.split(',')])
        found[int(number)] = sets
    return found


OBJECTS = {1: 'sterk-cusp-1.tikz', 2: 'vinberg-10-8-0.tikz',
           3: 'sterk-cusp-3.tikz', 4: 'sterk-cusp-4.tikz', 5: 'sterk-cusp-5.tikz'}


def figure_sterk_2():
    """vinberg-10-8-0.tikz, read from the library family that object names.

    Its header publishes the order: root i of Sterk_2 is its vertex
    1, 3, 4, 5, 6, 7, 8, 9, 10, 2 for i = 0..9.  That permutation is applied,
    so the returned diagram is indexed by the manuscript's vertex numbers.  The
    norms and the Coxeter entries are the library diagram's own.
    """
    from sage_extensions.all import Sterk

    roots = tuple(Sterk.sterk_roots()['Sterk_2'])
    n = len(roots)
    diagram = CoxeterDiagrams().from_roots({i: roots[i] for i in range(n)})
    norms = [int(roots[i].q()) for i in range(n)]
    published = [0, 2, 3, 4, 5, 6, 7, 8, 9, 1]      # library root i -> object vertex, 0-based
    assert len(published) == n and sorted(published) == list(range(n))
    object_norms, object_weights = {}, {}
    for i in range(n):
        object_norms[published[i]] = norms[i]
        for j in range(i + 1, n):
            entry = diagram.coxeter_entry(i, j)
            if entry.is_countably_infinite():
                weight = 'infinity'
            elif int(entry) != 2:
                weight = int(entry)
            else:
                continue
            left, right = published[i], published[j]
            object_weights[(min(left, right), max(left, right))] = weight
    order = sorted(object_norms)
    return [object_norms[v] for v in order], object_weights


def main():
    definitions = load_definitions(SOURCE)
    table = displayed_sets(CUSPS_FILE)
    print('displayed sets read from the manuscript: %s' % table)
    gram_of = definitions['gram_of']
    edge_label = definitions['edge_label']
    cusps = definitions['CUSPS']

    for number, (name, build) in enumerate(cusps, start=1):
        M = gram_of(build())
        n = M.nrows()
        script_side = script_diagram(M, edge_label)
        if number == 2:
            figure_side = figure_sterk_2()
        else:
            figure_side = figure_diagram(os.path.join(COXETER_OBJECTS, OBJECTS[number]))
        assert len(figure_side[0]) == n, (number, len(figure_side[0]), n)
        # the two sides agree on what a vertex is before any map is searched
        assert sorted(script_side[0]) == sorted(figure_side[0]), \
            ('%s: norm multisets differ' % name, sorted(script_side[0]), sorted(figure_side[0]))
        assert sorted(script_side[1].values(), key=str) == \
            sorted(figure_side[1].values(), key=str), \
            ('%s: weight multisets differ' % name,
             sorted(script_side[1].values(), key=str),
             sorted(figure_side[1].values(), key=str))
        Gs, ps = labelled_graph(*script_side)
        Gf, pf = labelled_graph(*figure_side)
        phi, maps = transporter((Gs, ps), (Gf, pf), name)
        # phi: script a-index (0-based, a_{i+1}) -> manuscript vertex
        print('=' * 70)
        print('%-30s  |Aut| = %d, so the map is determined up to %d relabellings'
              % (name, len(maps), len(maps)))
        print('   script a_{i+1} -> manuscript vertex %d..%d'
              % (min(phi.values()), max(phi.values())))
        print('   one representative: %s'
              % [phi[i] for i in range(n)])
        if len({tuple(sorted(m.items())) for m in maps}) != len(maps):
            raise AssertionError('%s: the transporter is not a coset' % name)
        L = Lattices(ZZ)([list(r) for r in M.rows()])
        D = CoxeterDiagrams().from_roots({i: L.basis_vector(i) for i in range(n)})
        offset = 1 if number == 2 else 0      # cusp 2's object numbers its vertices from 1
        for displayed in table[number]:
            wanted = [i for i in range(n) if phi[i] + offset in set(displayed)]
            if not wanted:
                print('      displayed %s: no script vertex maps into it' % displayed)
                continue
            sub = D.induced_subdiagram(wanted)
            inertia = (sub.positive_inertia_index(), sub.negative_inertia_index(),
                       sub.zero_inertia_index())
            rank = inertia[0] + inertia[1]
            if inertia[1] == 0 and inertia[2] == 0:
                kind = 'elliptic'
            elif inertia[1] == 0:
                kind = 'negative semidefinite, %d null direction(s)' % inertia[2]
            else:
                kind = 'indefinite'
            print('      displayed %-44s -> a%-38s %2d nodes, rank %d, (n+,n-,n0)=%s  %s'
                  % (displayed, [i + 1 for i in sorted(wanted)], len(wanted), rank,
                     inertia, kind))
        if os.environ.get('STERK_REPS'):
            # The Type II rays are the orbits of the maximal parabolic subdiagrams
            # (rank 8: nine nodes for an affine component, by Vinberg's convention).
            # The enumeration is the reconstruction script's own, which is what the
            # accepted Type II counts were computed from; the orbits are taken under
            # the same labelled action as everywhere else.
            found = [frozenset(vertex for component in components for vertex in component)
                     for _, components in definitions['maximal_parabolic_subdiagrams'](M, 8)]
            action = Gs.automorphism_group(partition=ps, edge_labels=True, algorithm='sage')
            reps, remaining = [], list(found)
            while remaining:
                representative = remaining[0]
                reps.append(representative)
                orbit = {frozenset(g(v) for v in representative) for g in action}
                remaining = [other for other in remaining if other not in orbit]
            print('   maximal parabolic subdiagrams %d -> %d orbits; representatives'
                  % (len(found), len(reps)))
            for position, representative in enumerate(reps, start=1):
                vertices = sorted(representative)
                print('      orbit %d: a%s = manuscript %s'
                      % (position, [v + 1 for v in vertices],
                         sorted(phi[v] + offset for v in vertices)))
            for displayed in table[number]:
                wanted = frozenset(i for i in range(n) if phi[i] + offset in set(displayed))
                covering = [position for position, representative in enumerate(reps, start=1)
                            if wanted in {frozenset(g(v) for v in representative) for g in action}]
                print('      displayed %-44s covers orbit %s'
                      % (displayed, covering if covering else 'none'))
        sys.stdout.flush()


main()
