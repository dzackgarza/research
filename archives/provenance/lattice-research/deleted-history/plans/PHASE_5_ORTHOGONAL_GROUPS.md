# Phase 5: Orthogonal Groups, Roots, Weyl, Eichler, and Coxeter

Build the full group-theoretic layer on top of the lattice hierarchy:
orthogonal groups with explicit element construction routed through hom
spaces, stabilizers, centralizers, kernel of discriminant action, isotropic
orbit enumeration, involution eigenlattices. Root systems, reflections,
Weyl groups, Eichler transvections. Coxeter diagrams with subdiagram posets
and automorphisms. After this phase, the entire spec surface from
`tests/lattice_spec/*.sage` and `tests/sage_spec/*.sage` becomes runnable.

**Depends on:** Phase 4 (the meet-based lattice, rational-lattice, and
discriminant objects built on `ModulesWithForms`). Orthogonal group
elements are endomorphisms `L.Hom(L)` supplied by the Phase 2/3 category
and wrapper machinery. Stabilizers and eigenlattices use `span`, `perp`,
and inclusion/cokernel semantics from Phases 2-4.

**Supersedes:** PHASE_1 Step 12, plus the extended group-theoretic spec
surface from all spec files.

**Style guide:** `plans/LATTICE_STYLE_GUIDE.md`.
Core style constraints: matrices are NOT hom elements (route through
`O(L).__call__` or `from_matrix`), stabilizers live on the group
(not on the lattice), reflections are constructed from root elements,
intersection via `&`, enumeration via `__iter__`.


## Files

```
src/lattices/
    groups/
        orthogonal.py             # LatticeOrthogonalGroup and subgroups
        roots.py                  # Root systems, reflections, Weyl groups
        eichler.py                # Eichler transvections and Eichler group
        coxeter.py                # Coxeter diagrams, subdiagram posets
    predicates.py                 # Centralized predicate classes (see style guide)
```


## Implementation Steps


### Step 5.0: Centralized Predicates

**File:** `predicates.py`

Every subgroup, subobject, and ConditionSet is built from predicates
defined once here and composed at call sites. No inline matrix equations
elsewhere in the codebase.

```python
class IsometryPredicate:
    """f preserves the bilinear form: M^T G M == G."""
    def __init__(self, gram_matrix: Matrix):
        self._G = gram_matrix

    def __call__(self, f: Morphism) -> bool:
        M = f.to_matrix()
        return M.T * self._G * M == self._G

class CentralizerPredicate:
    """f commutes with g: f * g == g * f."""
    def __init__(self, g: Morphism):
        self._g = g

    def __call__(self, f: Morphism) -> bool:
        return f * self._g == self._g * f

class StabilizerPredicate:
    """f fixes element v: f(v) == v."""
    def __init__(self, v):
        self._v = v

    def __call__(self, f: Morphism) -> bool:
        return f(self._v) == self._v

class LinePredicate:
    """f preserves the line <v>: f(v) in {v, -v}."""
    def __init__(self, v):
        self._v = v

    def __call__(self, f: Morphism) -> bool:
        return f(self._v) == self._v or f(self._v) == -self._v

class DiscriminantKernelPredicate:
    """f acts trivially on A_L: each discriminant class is fixed."""
    def __init__(self, lattice):
        self._A_L = lattice.discriminant_group()

    def __call__(self, f: Morphism) -> bool:
        for g in self._A_L.gens():
            if f(g.lift()).discriminant_class() != g:
                return False
        return True
```

**Rule:** Any method checking "is `f` an isometry" calls
`IsometryPredicate(G)(f)`. The equation `M^T G M == G` appears exactly
once: inside `IsometryPredicate.__call__`. Composition of predicates
(intersection, union) is done by constructing `ConditionSet` objects and
using their native `&` and `|` operators -- not by hand-rolling conjunction
classes. See Step 5.2.


### Step 5.1: LatticeOrthogonalGroup

**File:** `groups/orthogonal.py`

A `LatticeOrthogonalGroup` is the group `O(L)` of isometries of `L`.
Its elements are the endomorphisms of the lattice object in
`L.End()` that satisfy the isometry predicate. It is a genuine Sage
`Parent` whose elements are morphisms, not matrices.

```python
class LatticeOrthogonalGroup(Parent):
    """O(L) = {f in End(L) : f is an isometry}.

    Elements are LatticeMorphisms, not matrices. Construction
    from matrices goes through from_matrix, which
    constructs the morphism and validates isometry.
    """

    def __init__(self, lattice):
        self._lattice = lattice
        ...

    def lattice(self):
        return self._lattice

    def __call__(self, arg):
        """Thin dispatcher: accepts matrix or morphism."""
        ...

    def from_matrix(self, M):
        """Construct isometry from matrix representation.

        Validates that M preserves the bilinear form.
        """
        f = self._lattice.End().from_matrix(M)
        assert f.is_isometry(), "Matrix does not define an isometry"
        return f

    def from_dict(self, mapping):
        """Construct isometry from generator-image dict."""
        f = self._lattice.End().from_dict(mapping)
        assert f.is_isometry()
        return f

    def identity(self):
        return self._lattice.End().identity()

    def gens(self):
        """Generators of O(L). Backend delegation."""
        ...

    def __contains__(self, f):
        """f in O(L) iff f is a morphism L -> L that preserves the form."""
        if not isinstance(f, Morphism):
            return False  # Matrices are not in O(L)
        return (f.domain() == self._lattice
                and f.codomain() == self._lattice
                and f.is_isometry())

    def __iter__(self):
        """Enumerate all isometries. Finite for definite lattices."""
        ...

    def order(self):
        """Group order. Finite for definite lattices."""
        ...

    def is_isomorphic_to(self, group):
        """Abstract group isomorphism."""
        ...
```

**Key design: matrices are NOT in `O(L)`.** This is asserted repeatedly
in the specs:
```python
swap = matrix(ZZ, [[0,1],[1,0]])
assert swap not in O_U2          # A matrix is not a hom
assert O_U2(swap) in O_U2        # __call__ dispatches
assert O_U2.from_matrix(swap) in O_U2
```


### Step 5.2: Orthogonal Subgroups

**File:** `groups/orthogonal.py`

Subgroups of `O(L)` share the same universe (`GL_n(ZZ)`) but add
predicates on top of the isometry predicate. All predicates come from
`predicates.py` -- no inline conditions here.

```python
class LatticeOrthogonalSubgroup(LatticeOrthogonalGroup):
    """A subgroup of O(L) defined by a ConditionSet.

    Stores a ConditionSet over the same universe as O(L). Membership,
    intersection (&), and union (|) all delegate to the native
    ConditionSet operators -- no hand-rolled predicate conjunction.
    """

    def __init__(self, ambient_group, condition_set):
        self._ambient = ambient_group
        self._condition_set = condition_set  # ConditionSet object

    def __contains__(self, f):
        if not isinstance(f, Morphism):
            return False
        return f in self._condition_set

    def __and__(self, other):
        # ConditionSet & ConditionSet via native operator
        return LatticeOrthogonalSubgroup(
            self._ambient,
            self._condition_set & other._condition_set
        )

    def __or__(self, other):
        # ConditionSet | ConditionSet via native operator
        return LatticeOrthogonalSubgroup(
            self._ambient,
            self._condition_set | other._condition_set
        )
```

**Standard subgroup constructors** on `LatticeOrthogonalGroup`. Each
creates a fresh `ConditionSet(universe, predicate)` and intersects with
`self._condition_set` using native `ConditionSet &`:

```python
def centralizer(self, g):
    new_cs = ConditionSet(self._universe, CentralizerPredicate(g))
    return LatticeOrthogonalSubgroup(self, self._condition_set & new_cs)

def stabilizer(self, arg):
    if arg in self._lattice:  # Element stabilizer
        new_cs = ConditionSet(self._universe, StabilizerPredicate(arg))
    else:  # Submodule: setwise, each generator must be fixed
        cs = ConditionSet(self._universe, StabilizerPredicate(arg.gens()[0]))
        for v in arg.gens()[1:]:
            cs = cs & ConditionSet(self._universe, StabilizerPredicate(v))
        new_cs = cs
    return LatticeOrthogonalSubgroup(self, self._condition_set & new_cs)

def stabilizer_of_isotropic_line(self, v):
    new_cs = ConditionSet(self._universe, LinePredicate(v))
    return LatticeOrthogonalSubgroup(self, self._condition_set & new_cs)

def kernel_of_discriminant_action(self):
    new_cs = ConditionSet(
        self._universe, DiscriminantKernelPredicate(self._lattice)
    )
    return LatticeOrthogonalSubgroup(self, self._condition_set & new_cs)

def special_orthogonal_subgroup(self):
    det_one_cs = ConditionSet(
        self._universe, lambda f: f.to_matrix().det() == 1
    )
    return LatticeOrthogonalSubgroup(self, self._condition_set & det_one_cs)
```

**Stabilizer semantics.** Dispatch based on argument type:
- `stabilizer(v)` for element: `f(v) == v` via `StabilizerPredicate`
- `stabilizer(S)` for submodule: setwise, each generator fixed

From the specs:
```python
assert minus_I2 not in U.O().stabilizer(e)      # -e != e: StabilizerPredicate fails
assert minus_I2 in U.O().stabilizer(e.span())   # -I permutes generators of <e>: LinePredicate

combined = O_U.centralizer(f_neg) & O_U.stabilizer(e)
# predicate = IsometryPredicate(G_U) & CentralizerPredicate(f_neg) & StabilizerPredicate(e)
assert O_U.identity() in combined   # identity satisfies all three
assert f_neg not in combined        # f_neg(e) = -e, fails StabilizerPredicate
```


### Step 5.3: Isotropic Orbits

**File:** `groups/orthogonal.py` (methods on `LatticeOrthogonalGroup`)

```python
def isotropic_line_orbits(self):
    """Orbits of primitive isotropic vectors under self, up to sign."""
    ...

def isotropic_plane_orbits(self):
    """Orbits of isotropic 2-planes."""
    ...

def isotropic_flag_orbits(self, dim):
    """Orbits of isotropic flags of given dimension."""
    ...

def isotropic_lines_are_equivalent(self, v, w):
    """Whether <v> and <w> are in the same orbit."""
    ...
```

The specs assert orbit-splitting between `O(L)` and `SO(L)`:
```python
assert len(O_U.isotropic_line_orbits()) == 1
assert len(SO_U.isotropic_line_orbits()) == 2
assert O_U.isotropic_lines_are_equivalent(e, f)
assert not SO_U.isotropic_lines_are_equivalent(e, f)
```


### Step 5.4: Involution Eigenlattices

**File:** `groups/orthogonal.py` (methods on `Lattice`)

For an involution `g in O(L)` (meaning `g^2 == id`), the eigenlattices
are:
- `L.invariant_sublattice(g)` = `{v in L : g(v) == v}` = `L^g`
- `L.coinvariant_sublattice(g)` = `{v in L : g(v) == -v}` = `L_g`

These methods live on `Lattice` (they produce sublattices) but take a
group element as argument.

```python
def invariant_sublattice(self, g):
    """L^g = ker(g - id) with restricted form."""
    return (g - self.End().identity()).kernel()

def coinvariant_sublattice(self, g):
    """L_g = ker(g + id) with restricted form."""
    return (g + self.End().identity()).kernel()
```

From the specs:
```python
F = G.from_matrix(swap)
assert U.invariant_sublattice(F) == U.span([e + f])
assert U.coinvariant_sublattice(F) == U.span([e - f])
assert U.coinvariant_sublattice(F) == U.invariant_sublattice(F).perp()
```


### Step 5.5: Roots and Reflections

**File:** `groups/roots.py`

A root of `L` is a vector `v in L` with `v * v == -2` (or `v * v == 2`
depending on convention; the specs use `v * v == -2` for the hyperbolic
plane, where `e - f` has norm `-2`). The reflection in `v` is:

    s_v(w) = w - (2 * (v * w) / (v * v)) * v

This is always an integral isometry when `v` is a root.

**On `LatticeElement`:**
```python
def is_root(self):
    """v is a root iff v * v in {-2, 2} (convention: norm +/- 2)."""
    return abs(self * self) == 2

def reflection(self):
    """The reflection s_v in O(L).

    s_v(w) = w - (2 * beta(v, w) / beta(v, v)) * v
    """
    assert self.is_root()
    L = self.parent()
    images = {}
    for g in L.gens():
        images[g] = g - (2 * (self * g) / (self * self)) * self
    return L.O().from_dict(images)
```

**On `Lattice`:**
```python
def roots(self):
    """The set of roots {v in L : v * v in {-2, 2}}."""
    ...

def root_sublattice(self):
    """Sublattice spanned by the root system."""
    return self.span(self.roots())
```

From the specs:
```python
v = e - f
assert v * v == -2
assert v.is_root()
assert U.roots() == {v, -v}

s_v = v.reflection()
assert s_v(e) == f and s_v(f) == e
assert s_v(v) == -v
assert s_v in U.O()
assert s_v * s_v == U.O().identity()

R_U = U.root_sublattice()
assert R_U == Lattice.root_lattice("A1")
```


### Step 5.6: Weyl Groups

**File:** `groups/roots.py`

The Weyl group `W(L)` is the subgroup of `O(L)` generated by reflections
in the roots of `L`.

```python
class WeylGroup(LatticeOrthogonalSubgroup):
    """W(L) = <s_v : v is a root of L>."""

    def gens(self):
        """Simple reflections generating W."""
        ...

    def simple_reflections(self):
        """A choice of simple roots and their reflections."""
        ...

    def coxeter_diagram(self):
        """The Coxeter/Dynkin diagram of W."""
        ...

    def is_isomorphic_to(self, group):
        ...
```

**On `Lattice`:**
```python
def W(self):
    """Alias for self.weyl_group()."""
    return self.weyl_group()

def weyl_group(self):
    return WeylGroup(self)
```

From the specs:
```python
assert U.W() == U.weyl_group()
assert U.W().gens() == {s_v}
assert U.W().is_isomorphic_to(CyclicGroup(2))
assert s_v in U.W()
```

**LatticeMorphism extensions for reflections:**
```python
def is_reflection(self):
    """Whether this isometry is a reflection in some root."""
    ...

def reflection_decomposition(self):
    """Express as a product of reflections."""
    ...

def as_word_in_generators(self):
    """Express in terms of the generators of O(L)."""
    ...

def as_word_in_reflections(self):
    """Express as a product of reflections in roots."""
    ...

def is_involution(self):
    return self * self == self.parent().identity()

def order(self):
    """Multiplicative order in O(L)."""
    ...
```


### Step 5.7: Eichler Transvections

**File:** `groups/eichler.py`

An Eichler transvection is defined for an isotropic vector `e` and a
vector `r` in `e.perp()`:

    t_{e,r}(w) = w - (r * w) * e + (e * w) * r - (r * r / 2) * (e * w) * e

This is always an isometry when `e` is isotropic and `r in e.perp()`.

```python
def eichler_transvection(e, r):
    """Eichler transvection t_{e,r}.

    e must be isotropic, r must be in e.perp().
    """
    assert e.is_isotropic()
    assert e * r == 0  # r in e.perp()
    L = e.parent()
    images = {}
    for g in L.gens():
        images[g] = (g
            - (r * g) * e
            + (e * g) * r
            - QQ(r * r, 2) * (e * g) * e)
    return L.O().from_dict(images)
```

**Eichler group `E(L)`:** The subgroup of `O(L)` generated by all Eichler
transvections.

```python
class EichlerGroup(LatticeOrthogonalSubgroup):
    """E(L) = <t_{e,r} : e isotropic, r in e.perp()>."""

    def gens(self):
        """Generating Eichler transvections."""
        ...

    def is_trivial(self):
        ...

    def is_subgroup(self, other):
        ...
```

**On `Lattice`:**
```python
def E(self):
    """Alias for self.eichler_group()."""
    return self.eichler_group()

def eichler_group(self):
    return EichlerGroup(self)
```

From the specs:
```python
# U has no room for nontrivial Eichler transvections
assert U.E().is_trivial()
assert U.E().is_subgroup(U.W())

# U + A_1 does
L_eich = Lattice.from_string("U + A_1")
e0, f0, r = tuple(L_eich.gens())
t_er = eichler_transvection(e0, r)
assert t_er in L_eich.O()
assert t_er in L_eich.E()
assert t_er.inverse() == eichler_transvection(e0, -r)

# Eichler transvection is a product of two reflections
assert t_er == (r + e0).reflection() * r.reflection()

# Multiplicativity in the second argument
L_eich2 = Lattice.from_string("U + A_1 + A_1")
e2, f2, r1, r2 = tuple(L_eich2.gens())
t1 = eichler_transvection(e2, r1)
t2 = eichler_transvection(e2, r2)
t12 = eichler_transvection(e2, r1 + r2)
assert t1 * t2 == t12
```


### Step 5.8: Coxeter Diagrams and Subdiagram Posets

**File:** `groups/coxeter.py`

A Coxeter diagram encodes the angles between the hyperplanes orthogonal
to simple roots. For a root lattice, this is the Dynkin diagram.

```python
class CoxeterDiagram(Parent):
    """Weighted graph encoding Coxeter relations.

    Nodes correspond to simple roots. Edge weight between nodes
    i,j encodes the angle between root hyperplanes.
    """

    def __init__(self, lattice_or_cartan_type):
        ...

    def nodes(self):
        ...

    def edges(self):
        ...

    def adjacency_matrix(self, weighted=True):
        ...

    def is_connected(self):
        ...

    def subdiagram(self, node_subset):
        """Induced subdiagram on given nodes."""
        ...

    def subdiagram_poset(self):
        """Poset of all subdiagrams ordered by inclusion."""
        ...

    def Aut(self):
        """Weight-preserving graph automorphisms."""
        ...
```

From the specs:
```python
L = Lattice.A(4)
G = L.coxeter_diagram()
P = G.subdiagram_poset()
assert P in Posets

G.<n1, n2, n3, n4> = L.coxeter_diagram()
Aut_G = G.Aut()
assert Aut_G.is_isomorphic_to(ZZ/2)  # A_4 has mirror symmetry

# Subdiagram ordering
assert G.subdiagram({0}) <= G.subdiagram({0,1})
assert G.subdiagram({0,1}) <= G.subdiagram({0,1,2})
assert G.subdiagram({0,1,2}).is_connected()
assert not G.subdiagram({0,2,3}).is_connected()
```

**Root system as an object:**
```python
class RootSystem(Parent):
    """The root system Phi of a lattice.

    Objects are roots (lattice elements with norm +/- 2).
    """

    def span(self):
        """The root sublattice."""
        ...

    def simple_roots(self):
        ...

    def inclusion(self):
        """Inclusion morphism root_sublattice -> L."""
        ...
```

From the specs:
```python
assert L.root_system().inclusion().index() == 1  # Root lattice
assert L.O() == L.W()  # For A_n, O(L) = W(L)
```


### Step 5.9: Kernel of Discriminant Action

**File:** `groups/orthogonal.py`

The map `O(L) -> O(A_L)` sends each isometry of `L` to its induced action
on the discriminant group. The kernel is `O^+(L)`.

```python
def kernel_of_discriminant_action(self):
    """ker(O(L) -> O(A_L)).

    An isometry f is in the kernel iff the induced action
    on the discriminant group is trivial.
    """
    A_L = self._lattice.discriminant_group()
    def in_kernel(f):
        # f acts on A_L via: g_bar -> pi(f(g.lift()))
        # In kernel iff this action is identity
        for g in A_L.gens():
            lifted = g.lift()
            image = f(lifted)  # In L* via extension
            if image.discriminant_class() != g:
                return False
        return True
    return LatticeOrthogonalSubgroup(self, in_kernel)
```

This also works on subgroups: if `G <= O(L)`, then
`G.kernel_of_discriminant_action()` is `ker(G -> O(A_L))`.

From the specs:
```python
centralizer_A2 = A2.O().centralizer(minus_A2)
assert minus_A2 not in centralizer_A2.kernel_of_discriminant_action()
assert A2.O().identity() in centralizer_A2.kernel_of_discriminant_action()
```


## Explicitly Out of Scope for Phase 5

- **Coble geometry pipeline** (sextic -> surface -> K3 cover) -- separate
  geometric module
- **Overlattices, maximal even overlattice, glue construction** -- deferred
- **Parabolic/elliptic subdiagram classification** -- TODOs in spec
- **Folding symmetries and orbit subdiagrams** -- partially specced, TODO
- **Coxeter angle matrix in exact arithmetic** (`QQ[pi]`) -- TODO in spec
- **Enumeration of hom spaces to find generators** -- deferred
- **General indefinite isometry algorithms** (`todo_general_indefinite_isometry_spec.py`)
- **p-adic completions and local theory** -- Phase 0 stubs only


## Functional Checkpoint

Run in a Sage session after completing Phase 5:

```python
import src.sage_patches
from src.lattices.lattices import Lattice
from src.lattices.groups.eichler import eichler_transvection

U = Lattice.U()
e, f = tuple(U.gens())

# ------------------------------------------------------------------
# Orthogonal group construction and containment
# ------------------------------------------------------------------

I2 = identity_matrix(ZZ, 2)
swap = matrix(ZZ, [[0, 1], [1, 0]])
minus_I2 = -I2

O_U = U.O()
assert O_U == U.orthogonal_group()

# Matrices are NOT in O(L)
assert swap not in O_U
assert minus_I2 not in O_U

# Constructed morphisms ARE in O(L)
f_swap = O_U.from_matrix(swap)
assert f_swap in O_U
f_neg = O_U(minus_I2)
assert f_neg in O_U

# ------------------------------------------------------------------
# Explicit group enumeration
# ------------------------------------------------------------------

assert set(O_U) == {O_U(I2), O_U(swap), O_U(minus_I2), O_U(-swap)}
assert O_U.is_isomorphic_to(CyclicPermutationGroup([2, 2]))

# ------------------------------------------------------------------
# Evaluation on elements
# ------------------------------------------------------------------

assert f_swap(e) == f and f_swap(f) == e
assert f_neg(e) == -e and f_neg(f) == -f

# ------------------------------------------------------------------
# Involutions and order
# ------------------------------------------------------------------

assert f_swap.is_involution() and f_swap.order() == 2
assert f_neg.is_involution() and f_neg.order() == 2

# ------------------------------------------------------------------
# Stabilizers
# ------------------------------------------------------------------

assert set(O_U.stabilizer(e)) == {O_U(I2)}
assert f_neg not in O_U.stabilizer(e)  # -e != e
assert f_neg in O_U.stabilizer(e.span())  # -I preserves <e>

# ------------------------------------------------------------------
# Centralizers
# ------------------------------------------------------------------

centralizer_neg = O_U.centralizer(f_neg)
assert f_neg in centralizer_neg
assert O_U.identity() in centralizer_neg

# ------------------------------------------------------------------
# Isotropic orbits
# ------------------------------------------------------------------

SO_U = O_U.special_orthogonal_subgroup()
assert len(O_U.isotropic_line_orbits()) == 1
assert len(SO_U.isotropic_line_orbits()) == 2
assert O_U.isotropic_lines_are_equivalent(e, f)
assert not SO_U.isotropic_lines_are_equivalent(e, f)

# ------------------------------------------------------------------
# Intersection via &
# ------------------------------------------------------------------

combined = O_U.centralizer(f_neg) & O_U.stabilizer(e)
assert O_U.identity() in combined
assert f_neg not in combined

# ------------------------------------------------------------------
# Involution eigenlattices
# ------------------------------------------------------------------

assert U.invariant_sublattice(f_swap) == U.span([e + f])
assert U.coinvariant_sublattice(f_swap) == U.span([e - f])
assert U.coinvariant_sublattice(f_swap) == U.invariant_sublattice(f_swap).perp()

# ------------------------------------------------------------------
# Roots and reflections
# ------------------------------------------------------------------

v = e - f
assert v * v == -2
assert v.is_root()
assert U.roots() == {v, -v}

s_v = v.reflection()
assert s_v(e) == f and s_v(f) == e
assert s_v(v) == -v
assert s_v in O_U
assert s_v * s_v == O_U.identity()
assert s_v.is_reflection()
assert s_v.reflection_decomposition() == [s_v]

# ------------------------------------------------------------------
# Root sublattice
# ------------------------------------------------------------------

R_U = U.root_sublattice()
assert R_U == Lattice.root_lattice("A1")
assert R_U == U.span([v])
assert R_U.rank() == 1
assert R_U.is_primitive()
assert R_U.perp() == U.span([e + f])

# ------------------------------------------------------------------
# Weyl group
# ------------------------------------------------------------------

assert U.W() == U.weyl_group()
assert U.W().gens() == {s_v}
assert U.W().is_isomorphic_to(CyclicGroup(2))
assert s_v in U.W()

# ------------------------------------------------------------------
# Coxeter diagrams
# ------------------------------------------------------------------

assert Lattice.root_lattice("A1").coxeter_diagram() == DynkinDiagram("A1")
assert Lattice.root_lattice("D4").coxeter_diagram() == DynkinDiagram("D4")
assert Lattice.root_lattice("E8").coxeter_diagram() == DynkinDiagram("E8")
assert U.W().coxeter_diagram() == DynkinDiagram("A1")

A4 = Lattice.A(4)
G = A4.coxeter_diagram()
P = G.subdiagram_poset()
assert P in Posets
Aut_G = G.Aut()
assert Aut_G.is_isomorphic_to(ZZ/2)

# ------------------------------------------------------------------
# Eichler transvections
# ------------------------------------------------------------------

assert U.E().is_trivial()
assert U.E().is_subgroup(U.W())

L_eich = Lattice.from_string("U + A_1")
e0, f0, r = tuple(L_eich.gens())
assert e0.is_isotropic()
assert r * r == -2
assert e0 * r == 0  # r in e0.perp()

t_er = eichler_transvection(e0, r)
# Verify defining formula on each basis vector
for bv in tuple(L_eich.gens()):
    expected = (bv
        - (r * bv) * e0
        + (e0 * bv) * r
        - QQ(r * r, 2) * (e0 * bv) * e0)
    assert t_er(bv) == expected

assert t_er in L_eich.O()
assert t_er in L_eich.E()
assert t_er.inverse() == eichler_transvection(e0, -r)

# Eichler transvection = product of two reflections
assert t_er == (r + e0).reflection() * r.reflection()

# Multiplicativity in second argument
L_eich2 = Lattice.from_string("U + A_1 + A_1")
e2, f2, r1, r2 = tuple(L_eich2.gens())
t1 = eichler_transvection(e2, r1)
t2 = eichler_transvection(e2, r2)
t12 = eichler_transvection(e2, r1 + r2)
assert t1 * t2 == t12

# ------------------------------------------------------------------
# Kernel of discriminant action
# ------------------------------------------------------------------

U2 = Lattice.U().twist(2)
O_U2 = U2.O()
ker = O_U2.kernel_of_discriminant_action()
assert O_U2.identity() in ker

# ------------------------------------------------------------------
# A_2 eigenlattice and centralizer tests
# ------------------------------------------------------------------

A2 = Lattice.from_gram(IntegralLattice("A2").gram_matrix())
minus_A2 = A2.O()(- identity_matrix(ZZ, 2))
assert A2.invariant_sublattice(minus_A2).rank() == 0
assert A2.coinvariant_sublattice(minus_A2).rank() == A2.rank()

centralizer_A2 = A2.O().centralizer(minus_A2)
assert minus_A2 in centralizer_A2
assert A2.O().identity() in centralizer_A2.kernel_of_discriminant_action()
assert minus_A2 not in centralizer_A2.kernel_of_discriminant_action()

# ------------------------------------------------------------------
# O(U(2)) explicit enumeration
# ------------------------------------------------------------------

assert set(O_U2) == {O_U2(I2), O_U2(swap), O_U2(minus_I2), O_U2(-swap)}
assert O_U2.is_isomorphic_to(CyclicPermutationGroup([2, 2]))
```


## Risks

| Risk | Mitigation |
|------|-----------|
| Orthogonal group enumeration is expensive for high-rank lattices | Only enumerate for definite lattices; indefinite O(L) is infinite, provide generators only |
| Root-finding for indefinite lattices is nontrivial | Delegate to Sage's root enumeration; for hyperbolic lattices use explicit norm equations |
| Eichler transvection formula involves `r*r/2` which must be integral | Assert `r*r` is even (automatic when `r` is a root with norm -2) |
| Coxeter diagram construction from non-root-lattices | Only define for lattices where `L == L.root_sublattice()` or provide the root system explicitly |
| `kernel_of_discriminant_action` requires extending isometries to the dual | Use the inclusion `L -> L*` to lift: for `f in O(L)`, define `f*` on `L*` by `f*(phi) = phi . f^{-1}` |
| Stabilizer/centralizer predicates make enumeration lazy but slow | For finite groups, materialize the full group first then filter; for infinite groups use generators + membership test |
