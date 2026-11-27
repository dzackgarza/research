# Tests for Sets().Constructors().Family()
# Assertions sourced from sage.sets.family.Family doctests.

import sys
sys.path.insert(0, '/home/dzack/research/plans')
sys.path.insert(0, '/home/dzack/research')
from category_specs.sets import Sets
from sage.all import ZZ

NS = Sets().Constructors()

# ---------------------------------------------------------------------------
# List input: family indexed by {0,...,len-1}  (Family function docstring)
# ---------------------------------------------------------------------------

f = NS.Family([1, 2, 3])
assert list(f) == [1, 2, 3]
assert len(f) == 3

f_tuple = NS.Family((1, 2, 3))
assert list(f_tuple) == [1, 2, 3]

# ---------------------------------------------------------------------------
# Dictionary input  (Family function docstring)
# ---------------------------------------------------------------------------

fd = NS.Family({3: 'a', 4: 'b', 7: 'd'})
assert fd[7] == 'd'
assert len(fd) == 3
assert list(fd) == ['a', 'b', 'd']
assert fd.keys() == [3, 4, 7]
assert 'b' in fd
assert 'e' not in fd

# ---------------------------------------------------------------------------
# Index set + function  (Family function docstring)
# ---------------------------------------------------------------------------

ff = NS.Family([3, 4, 7], lambda i: 2 * i)
assert ff[7] == 14
assert list(ff) == [6, 8, 14]
assert len(ff) == 3

# ---------------------------------------------------------------------------
# Lazy family  (Family function docstring)
# ---------------------------------------------------------------------------

fl = NS.Family([3, 4, 7], lambda i: 2 * i, lazy=True)
assert fl[7] == 14
assert list(fl) == [6, 8, 14]

# ---------------------------------------------------------------------------
# Infinite lazy family: ZZ mapped by 2*i  (Family function docstring)
# ---------------------------------------------------------------------------

f_inf = NS.Family(ZZ, lambda i: 2 * i, lazy=True)
assert f_inf[1] == 2
assert f_inf[-5] == -10

it = iter(f_inf)
assert list(next(it) for _ in range(5)) == [0, 2, -2, 4, -4]

# ---------------------------------------------------------------------------
# hidden_keys  (Family function docstring)
# ---------------------------------------------------------------------------

fh = NS.Family([3, 4, 7], lambda i: 2 * i, hidden_keys=[2])
assert fh[7] == 14
assert fh[2] == 4          # hidden key accessed directly
assert fh.keys() == [3, 4, 7]
assert fh.hidden_keys() == [2]
assert list(fh) == [6, 8, 14]

# ---------------------------------------------------------------------------
# Generator expression  (Family function docstring)
# ---------------------------------------------------------------------------

f_gen = NS.Family(2 * i + 1 for i in [1, 2, 3])
assert list(f_gen) == [3, 5, 7]
