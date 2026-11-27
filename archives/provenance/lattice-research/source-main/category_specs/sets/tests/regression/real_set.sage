# Tests for Sets().Constructors().RealSet(...)
# Assertions sourced from sage.sets.real_set.RealSet doctests.

import sys
sys.path.insert(0, '/home/dzack/research/plans')
sys.path.insert(0, '/home/dzack/research')
from category_specs.sets import Sets
from sage.all import oo
from sage.sets.real_set import RealSet as SageRealSet

NS = Sets().Constructors()

open_01 = SageRealSet.open(0, 1).get_interval(0)
open_03 = SageRealSet.open(0, 3).get_interval(0)
open_04 = SageRealSet.open(0, 4).get_interval(0)
open_13 = SageRealSet.open(1, 3).get_interval(0)
open_14 = SageRealSet.open(1, 4).get_interval(0)
open_23 = SageRealSet.open(2, 3).get_interval(0)
closed_12 = SageRealSet.closed(1, 2).get_interval(0)
closed_13 = SageRealSet.closed(1, 3).get_interval(0)
real_line = SageRealSet.real_line().get_interval(0)

# ---------------------------------------------------------------------------
# Open interval from two numbers  (class docstring)
# ---------------------------------------------------------------------------

I01 = NS.RealSet(intervals=[open_01])
assert 0.5 in I01
assert 0 not in I01    # open at 0
assert 1 not in I01    # open at 1

# Endpoints are sorted: RealSet(1, 0) == RealSet(0, 1)
assert NS.RealSet(intervals=[SageRealSet.open(1, 0).get_interval(0)]) == NS.RealSet(intervals=[open_01])

# ---------------------------------------------------------------------------
# Union of intervals  (class docstring)
# ---------------------------------------------------------------------------

I_union = NS.RealSet(intervals=[open_01, open_23])
assert 0.5 in I_union
assert 2 not in I_union    # open at 2
assert 1.5 not in I_union

# Overlapping intervals are merged: (0,3) ∪ (1,4) = (0,4)
I_merged = NS.RealSet(intervals=[open_03, open_14])
assert I_merged == NS.RealSet(intervals=[open_04])

# ---------------------------------------------------------------------------
# Unbounded interval  (class docstring)
# ---------------------------------------------------------------------------

I_real_line = NS.RealSet(intervals=[real_line])
assert 1e100 in I_real_line
assert -1e100 in I_real_line

# ---------------------------------------------------------------------------
# Specialized constructors  (class docstring)
# ---------------------------------------------------------------------------

I_oc = NS.open_closed(lower=0, upper=1)
assert 0 not in I_oc
assert 1 in I_oc
assert 0.5 in I_oc

I_co = NS.closed_open(lower=0, upper=1)
assert 0 in I_co
assert 1 not in I_co
assert 0.5 in I_co

assert 1 in NS.point(point=1)
assert 2 not in NS.point(point=1)

I_below = NS.unbounded_below_open(bound=0)
assert -999 in I_below
assert 0 not in I_below

I_above = NS.unbounded_above_closed(bound=1)
assert 1 in I_above
assert 0.999 not in I_above
assert 1e99 in I_above

# ---------------------------------------------------------------------------
# Set-theoretic operations  (Set_base mixin via RealSet)
# ---------------------------------------------------------------------------

A = NS.RealSet(intervals=[open_03])
B = NS.RealSet(intervals=[open_14])
assert NS.RealSet(intervals=[open_04]) == A.union(B)
assert NS.RealSet(intervals=[open_13]) == A.intersection(B)

# Complement
C = NS.RealSet(intervals=[closed_12])
D = NS.RealSet(intervals=[closed_13])
diff = D.difference(C)
assert 2.5 in diff
assert 1.5 not in diff

# ---------------------------------------------------------------------------
# Cardinality / is_finite  (module docstring derived)
# ---------------------------------------------------------------------------

assert NS.point(point=1).is_finite() is True
assert NS.RealSet(intervals=[open_01]).is_finite() is False
