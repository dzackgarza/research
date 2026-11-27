# Tests for Sets().Constructors().ImageSubobject()
# Assertions sourced from sage.sets.image_set.ImageSubobject doctests.

import sys
sys.path.insert(0, '/home/dzack/research/plans')
sys.path.insert(0, '/home/dzack/research')
from category_specs.sets import Sets
from sage.all import ZZ, QQ, EnumeratedSets

NS = Sets().Constructors()

# ---------------------------------------------------------------------------
# Basic image: even integers as image of x -> 2x on ZZ  (_element_constructor_)
# ---------------------------------------------------------------------------

def double(x):
    return 2 * x

def half(x):
    return x // 2

I = NS.ImageSubobject(double, ZZ, inverse=half)

assert 6 in I
assert 7 not in I

# Constructing an element: I(y) finds x such that double(x) == y
assert I(8/2) == 4
assert I(8/2).parent() == ZZ

# ---------------------------------------------------------------------------
# Equality of ImageSubobject objects  (__eq__ doctest)
# ---------------------------------------------------------------------------

I2 = NS.ImageSubobject(double, ZZ)
I3 = NS.ImageSubobject(double, ZZ)
assert I2 == I3

I_QQ = NS.ImageSubobject(double, QQ)
assert I2 != I_QQ

# ---------------------------------------------------------------------------
# Iteration: image of a finite enumerated set  (enumerated subobject)
# ---------------------------------------------------------------------------

dom = NS.FiniteEnumeratedSet([1, 2, 3, 4])
Im_finite = NS.ImageSubobject(double, dom)
assert sorted(Im_finite) == [2, 4, 6, 8]
assert Im_finite.cardinality() == 4
