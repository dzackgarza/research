"""The root system of a definite lattice, and roots that generate the root sublattice of another lattice.

A root of a lattice `L` is a primitive `r` with `b(r, r) != 0` such that the
reflection `s_r` is in `O(L)`; `Phi(L)` is the set of roots.

Definite `L`: `Phi(L)` is finite and the preamble lattice object lists its
reflective roots; `root_system` gives them as irreducible components, each with
its type and a base.

Other `L`: `small_roots` searches the vectors with coordinates in `{-1, 0, 1}`
and at most three nonzero coordinates for roots. When the roots found generate
`L`, they generate `Z Phi(L)`, and `generating_roots` chooses among them a basis
of `L` when the greedy choice gives one. When they do not generate `L`,
`Z Phi(L)` is not decided, and a proof by hand gives the `root_span` block.
"""

from fractions import Fraction
from itertools import combinations, product

from dzack_research.preamble.rings import session_ring_objects

from latticedb import root_systems
from latticedb.model import GramTensor, Vector

_SESSION_RINGS = session_ring_objects()
ZZ = _SESSION_RINGS["ZZ"]

type Component = tuple[str, Fraction, tuple[Vector, ...]]
"""An irreducible component of a root system: its type, its scale, and its simple roots in the numbering of the type."""


def simple_roots(positive: list[Vector]) -> list[Vector]:
    """Return the base of the positive system `positive` of a reduced root system.

    `positive` holds, of each pair `r`, `-r`, the root whose first nonzero
    coordinate is positive. That is the positive system of the lexicographic
    order on the coordinates, a total order that addition respects. Its base is
    the set of positive roots that are not a sum of two positive roots.
    """
    sums = {tuple(a + b for a, b in zip(r, s, strict=True)) for r, s in combinations(positive, 2)}
    return [r for r in positive if r not in sums]


def irreducible_components(formed, base: list[Vector]) -> list[list[Vector]]:
    """Return the classes of the base under the relation that `b(r, s) != 0` generates."""
    components: list[list[Vector]] = []
    for r in base:
        root = formed(r)
        linked = [
            component
            for component in components
            if any(root.b(formed(s)) != 0 for s in component)
        ]
        components = [component for component in components if component not in linked]
        components.append([*(s for component in linked for s in component), r])
    return components


def _numbering(gram: tuple[tuple[Fraction, ...], ...], expected: tuple[tuple[int, ...], ...], chosen: tuple[int, ...]) -> tuple[int, ...] | None:
    """Return an order `p` of the indices with `gram[p[i]][p[j]] == expected[i][j]`, that starts with `chosen`; `None` when there is none."""
    position = len(chosen)
    if position == len(expected):
        return chosen
    for index in range(len(expected)):
        if index in chosen or gram[index][index] != expected[position][position]:
            continue
        if all(gram[index][chosen[other]] == expected[position][other] for other in range(position)):
            numbering = _numbering(gram, expected, (*chosen, index))
            if numbering is not None:
                return numbering
    return None


def typed_component(formed, base: list[Vector]) -> Component:
    """Return the type, the scale and the simple roots, in the numbering of the type, of an irreducible component with the given base.

    The types are tried in the order `A`, `B`, ..., `G`, so a component of rank 3 with the Gram matrix of `D3 = A3` has type `A3`.
    """
    norms = [formed(r).q() for r in base]
    scale = min(norms, key=abs) / formed.value_module()(2)
    gram = tuple(
        tuple(formed(r).b(formed(s)) / scale for s in base)
        for r in base
    )
    for letter in "ABCDEFG":
        root_type = f"{letter}{len(base)}"
        if root_systems.is_type(root_type):
            numbering = _numbering(gram, root_systems.simple_root_gram(root_type), ())
            if numbering is not None:
                return (
                    root_type,
                    Fraction(int(scale.numerator()), int(scale.denominator())),
                    tuple(base[index] for index in numbering),
                )
    raise AssertionError(f"no type for the base {base}")


def _components(formed, positive: list[Vector]) -> tuple[Component, ...]:
    """Return the irreducible components of the root system with the positive system `positive`, the greatest rank first."""
    base = simple_roots(positive)
    components = [
        typed_component(formed, component)
        for component in irreducible_components(formed, base)
    ]
    return tuple(sorted(components, key=lambda component: (-len(component[2]), component[0], component[2])))


def root_system(formed, positive_roots: dict[Vector, Fraction]) -> tuple[Component, ...]:
    """Return `Phi(L)` for a definite lattice as its irreducible components, the greatest rank first."""
    return _components(formed, list(positive_roots))


def norm_two_types(formed, positive_roots: dict[Vector, Fraction]) -> tuple[str, ...]:
    """Return the ADE type of `Phi_{{2}}(L)`, or of `Phi_{{-2}}(L)` for a negative definite `L`, as the types of its components, the greatest rank first.

    `positive_roots` contains one vector from each pair `r,-r` of reflective roots. The roots
    with `|b(r, r)| = 2` of an integer-valued lattice form a simply laced root
    system (Witt), so each component has type `A`, `D` or `E` at scale `1`
    or `-1`.
    """
    positive = [r for r, norm in positive_roots.items() if abs(norm) == 2]
    types = []
    for root_type, scale, _ in _components(formed, positive):
        assert root_type[0] in "ADE" and abs(scale) == 1, f"the roots of norm 2 form a component of type {root_type} at scale {scale}"
        types.append(root_type)
    return tuple(types)


def small_roots(gram_tensor: GramTensor, lattice) -> list[Vector]:
    """Return the roots with coordinates in `{-1, 0, 1}`, at most three of them nonzero and the first of those equal to 1."""
    rank = len(gram_tensor)
    roots = []
    for size in range(1, min(rank, 3) + 1):
        for support in combinations(range(rank), size):
            for signs in product((1, -1), repeat=size - 1):
                coefficients = dict(zip(support, (1, *signs), strict=True))
                r = tuple(coefficients.get(index, 0) for index in range(rank))
                if lattice(r).is_root():
                    roots.append(r)
    return roots


def generating_roots(roots: list[Vector], rank: int) -> list[Vector]:
    """Return a basis of `L` that is a sublist of `roots` when the greedy choice gives one, and otherwise a sublist that generates `L`. `roots` must generate `L`.

    The greedy choice takes a root when the roots taken, with it, are a basis
    of a primitive sublattice. The other choice takes a root when it is not in
    the sublattice that the roots taken generate.
    """
    ambient = ZZ.free_module(rank)
    basis: list[Vector] = []
    for r in roots:
        candidate = ambient.subobject_on(tuple(ambient(vector) for vector in (*basis, r)))
        if int(candidate.module_rank()) == len(basis) + 1 and candidate.is_primitive():
            basis.append(r)
    if len(basis) == rank:
        return basis
    taken: list[Vector] = []
    for r in roots:
        span = ambient.subobject_on(tuple(ambient(vector) for vector in taken))
        if ambient(r) not in span:
            taken.append(r)
    return taken
