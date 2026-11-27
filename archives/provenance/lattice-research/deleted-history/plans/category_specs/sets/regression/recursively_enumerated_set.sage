# Tests for Sets().NamedSets().RecursivelyEnumeratedSet()
# Assertions sourced from sage.sets.recursively_enumerated_set module doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.sets import Sets
from sage.all import FiniteEnumeratedSets

NS = Sets().NamedSets()

# ---------------------------------------------------------------------------
# No-structure set: linear combinations of 2 and 3  (module docstring)
# ---------------------------------------------------------------------------

succ = lambda a: [a + 2, a + 3]
C = NS.RecursivelyEnumeratedSet([0], succ)

it_bfs = C.breadth_first_search_iterator()
assert [next(it_bfs) for _ in range(10)] == [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]

it_dfs = C.depth_first_search_iterator()
assert [next(it_dfs) for _ in range(10)] == [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# ---------------------------------------------------------------------------
# Forest structure: binary words  (module docstring)
# ---------------------------------------------------------------------------

seeds = ['']
succ_words = lambda w: [w + 'a', w + 'b']
W = NS.RecursivelyEnumeratedSet(seeds, succ_words, structure='forest')

it_depth = W.depth_first_search_iterator()
assert [next(it_depth) for _ in range(6)] == ['', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa']

it_breadth = W.breadth_first_search_iterator()
assert [next(it_breadth) for _ in range(6)] == ['', 'a', 'b', 'aa', 'ab', 'ba']

# ---------------------------------------------------------------------------
# Finite forest with category  (module docstring)
# ---------------------------------------------------------------------------

S = NS.RecursivelyEnumeratedSet(
    [''],
    lambda x: [x + letter for letter in ['a', 'b', 'c']] if len(x) < 2 else [],
    structure='forest',
    enumeration='depth',
    category=FiniteEnumeratedSets())
assert S.list() == ['', 'a', 'aa', 'ab', 'ac', 'b', 'ba', 'bb', 'bc', 'c', 'ca', 'cb', 'cc']

# ---------------------------------------------------------------------------
# Graded structure  (module docstring — permutohedron)
# ---------------------------------------------------------------------------

from sage.misc.call import attrcall
from sage.combinat.permutation import Permutation

succ_perm = attrcall("permutohedron_succ")
seed_perm = [Permutation([1, 2, 3, 4, 5])]
R = NS.RecursivelyEnumeratedSet(seed_perm, succ_perm, structure='graded')

it_breadth_perm = R.breadth_first_search_iterator()
assert [next(it_breadth_perm) for _ in range(5)] == [
    [1, 2, 3, 4, 5],
    [2, 1, 3, 4, 5],
    [1, 3, 2, 4, 5],
    [1, 2, 4, 3, 5],
    [1, 2, 3, 5, 4]]

assert sorted(R.graded_component(0)) == [[1, 2, 3, 4, 5]]
assert sorted(R.graded_component(10)) == [[5, 4, 3, 2, 1]]

# ---------------------------------------------------------------------------
# Symmetric structure: lattice points  (module docstring)
# ---------------------------------------------------------------------------

succ_sym = lambda a: [(a[0]-1, a[1]), (a[0], a[1]-1), (a[0]+1, a[1]), (a[0], a[1]+1)]
Csym = NS.RecursivelyEnumeratedSet([(0, 0)], succ_sym, structure='symmetric', enumeration='depth')

it_depth_sym = iter(Csym)
assert [next(it_depth_sym) for _ in range(10)] == [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9)]

assert sorted(Csym.graded_component(0)) == [(0, 0)]
assert sorted(Csym.graded_component(1)) == [(-1, 0), (0, -1), (0, 1), (1, 0)]
