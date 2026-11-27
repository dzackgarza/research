# Tests for Sets().NamedSets().RealSet()
# Assertions sourced from sage.sets.real_set.RealSet doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.sets import Sets
from sage.all import oo

NS = Sets().NamedSets()

# ---------------------------------------------------------------------------
# Open interval from two numbers  (class docstring)
# ---------------------------------------------------------------------------

I01 = NS.RealSet(0, 1)
assert 0.5 in I01
assert 0 not in I01    # open at 0
assert 1 not in I01    # open at 1

# Endpoints are sorted: RealSet(1, 0) == RealSet(0, 1)
assert NS.RealSet(1, 0) == NS.RealSet(0, 1)

# ---------------------------------------------------------------------------
# Union of intervals  (class docstring)
# ---------------------------------------------------------------------------

I_union = NS.RealSet((0, 1), [2, 3])
assert 0.5 in I_union
assert 2 in I_union    # closed at 2
assert 1.5 not in I_union

# Overlapping intervals are merged: (1,3) ∪ (0,2) = (0,3)
I_merged = NS.RealSet((1, 3), (0, 2))
assert I_merged == NS.RealSet(0, 3)

# ---------------------------------------------------------------------------
# Unbounded interval  (class docstring)
# ---------------------------------------------------------------------------

I_real_line = NS.RealSet(-oo, oo)
assert 1e100 in I_real_line
assert -1e100 in I_real_line

# ---------------------------------------------------------------------------
# Specialized constructors  (class docstring)
# ---------------------------------------------------------------------------

I_oc = NS.RealSet.open_closed(0, 1)
assert 0 not in I_oc
assert 1 in I_oc
assert 0.5 in I_oc

I_co = NS.RealSet.closed_open(0, 1)
assert 0 in I_co
assert 1 not in I_co
assert 0.5 in I_co

I_pt = NS.RealSet.point(NS.RealSet)  # skip — no plain numeric point easily accessible
# Use built-in RealSet.point for the assertion, directly
from sage.sets.real_set import RealSet as SageRealSet
assert NS.RealSet.point(1) == SageRealSet.point(1)
assert 1 in NS.RealSet.point(1)
assert 2 not in NS.RealSet.point(1)

I_below = NS.RealSet.unbounded_below_open(0)
assert -999 in I_below
assert 0 not in I_below

I_above = NS.RealSet.unbounded_above_closed(1)
assert 1 in I_above
assert 0.999 not in I_above
assert 1e99 in I_above

# ---------------------------------------------------------------------------
# Set-theoretic operations  (Set_base mixin via RealSet)
# ---------------------------------------------------------------------------

A = NS.RealSet(0, 3)
B = NS.RealSet(1, 4)
assert NS.RealSet(0, 4) == A.union(B)
assert NS.RealSet(1, 3) == A.intersection(B)

# Complement
C = NS.RealSet([1, 2])
D = NS.RealSet([1, 3])
diff = D.difference(C)
assert 2.5 in diff
assert 1.5 not in diff

# ---------------------------------------------------------------------------
# Cardinality / is_finite  (module docstring derived)
# ---------------------------------------------------------------------------

assert NS.RealSet.point(1).is_finite() is True
assert NS.RealSet(0, 1).is_finite() is False
