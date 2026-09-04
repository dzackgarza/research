r"""Finite Coxeter diagrams, optionally rooted in an integral lattice."""

from sage.categories.category import Category
from sage.combinat.root_system.cartan_type import CartanType
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.graphs.graph import Graph
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ
from sage.structure.parent import Parent

from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.tensors.tensor import tensor


def _coxeter_entry(q1, q2, pairing):
    q1 = SageZZ(q1)
    q2 = SageZZ(q2)
    pairing = SageZZ(pairing)
    if q1 == 0 or q2 == 0:
        raise ValueError("a Coxeter root has nonzero square")
    if pairing == 0:
        return SageZZ(2)
    four_cos_squared = QQ(4 * pairing**2) / QQ(q1 * q2)
    if four_cos_squared == 1:
        return SageZZ(3)
    if four_cos_squared == 2:
        return SageZZ(4)
    if four_cos_squared == 3:
        return SageZZ(6)
    if four_cos_squared >= 4:
        return Infinity
    raise ValueError(f"the root pair does not determine a crystallographic Coxeter angle: 4 cos^2(pi/m) = {four_cos_squared}")


class CoxeterDiagrams(Category):
    @classmethod
    def _repr_object_names(cls):
        return "Coxeter diagrams"

    def super_categories(self):
        return [Sets()]

    def __contains__(self, candidate) -> bool:
        return isinstance(candidate, CoxeterDiagram)

    def from_coxeter_matrix(self, coxeter_matrix, names=None, positions=None):
        if isinstance(coxeter_matrix, (list, tuple)):
            entries = tuple(tuple(row) for row in coxeter_matrix)
            coxeter_matrix = CoxeterMatrix(entries, index_set=tuple(range(len(entries))))
        return CoxeterDiagram(coxeter_matrix, names=names, positions=positions)

    def from_cartan_type(self, cartan_type, names=None, *, rooted=False, positions=None):
        cartan_type = CartanType(cartan_type)
        if not rooted:
            return CoxeterDiagram(CoxeterMatrix(cartan_type), names=names, positions=positions)
        from dzack_research.preamble.categories.lattices import Lattices
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        lattice = Lattices(_own_ring(SageZZ))(cartan_type)
        return self.from_roots(tuple(lattice.module_generators()), names=names, positions=positions)

    def from_roots(self, roots, names=None, index_set=None, positions=None):
        roots = tuple(roots)
        if not roots:
            raise ValueError("a rooted Coxeter diagram needs at least one root")
        ambient = roots[0].parent()
        if any(root.parent() is not ambient for root in roots):
            raise ValueError("all diagram roots must belong to one lattice")
        if index_set is None:
            index_set = range(len(roots))
        index_set = finite_ordered_set(index_set)
        if index_set.cardinality() != len(roots):
            raise ValueError("the index set must have one vertex per root")
        gram = tensor(
            ambient.base_ring(),
            (),
            (len(roots), len(roots)),
            [[left.b(right) for right in roots] for left in roots],
        )
        entries = [[SageZZ.one() if i == j else _coxeter_entry(gram[i, i], gram[j, j], gram[i, j]) for j in range(len(roots))] for i in range(len(roots))]
        return CoxeterDiagram(
            CoxeterMatrix(entries, index_set=tuple(index_set)),
            names=names,
            roots=roots,
            root_gram=gram,
            positions=positions,
        )


class CoxeterDiagram(Parent):
    def __init__(
        self,
        coxeter_matrix,
        names=None,
        roots=None,
        root_gram=None,
        positions=None,
    ) -> None:
        self._coxeter_matrix = CoxeterMatrix(coxeter_matrix)
        self._index_set = finite_ordered_set(tuple(self._coxeter_matrix.index_set()))
        if names is None:
            names = tuple(f"s_{index}" for index in self._index_set)
        elif isinstance(names, str):
            names = tuple(part.strip() for part in names.split(","))
        else:
            names = tuple(names)
        if len(names) != len(self._index_set):
            raise ValueError("a Coxeter diagram needs one name per vertex")
        self._names = names
        self._roots = None if roots is None else tuple(roots)
        self._root_gram = root_gram
        if positions is None:
            self._preferred_positions = None
        else:
            if set(positions) != set(self._index_set):
                raise ValueError("positions need one coordinate pair for every vertex")
            if any(len(coordinates) != 2 for coordinates in positions.values()):
                raise ValueError("every diagram position must be a coordinate pair")
            self._preferred_positions = {vertex: (coordinates[0], coordinates[1]) for vertex, coordinates in positions.items()}
        self._computed_positions = None
        Parent.__init__(self, category=CoxeterDiagrams())

    def index_set(self):
        return self._index_set

    def cardinality(self):
        return self._index_set.cardinality()

    def vertex_names(self):
        return self._names

    def coxeter_matrix(self):
        return self._coxeter_matrix

    def coxeter_entry(self, left, right):
        entry = self._coxeter_matrix[left, right]
        return Infinity if entry == -1 else entry

    def is_rooted(self) -> bool:
        return self._roots is not None

    def roots(self):
        if self._roots is None:
            raise ValueError("this Coxeter diagram has no selected root realization")
        return self._roots

    def root_gram_tensor(self):
        if self._root_gram is None:
            raise ValueError("this Coxeter diagram has no selected root realization")
        return self._root_gram

    def preferred_positions(self):
        r"""Return stored presentation coordinates, or a computed graph layout."""
        if self._preferred_positions is not None:
            return dict(self._preferred_positions)
        if self._computed_positions is None:
            layout = self.graph().layout()
            self._computed_positions = {vertex: (coordinates[0], coordinates[1]) for vertex, coordinates in layout.items()}
        return dict(self._computed_positions)

    def graph(self):
        graph = Graph(multiedges=False, loops=False)
        graph.add_vertices(tuple(self.index_set()))
        vertices = tuple(self.index_set())
        for i, left in enumerate(vertices):
            for j in range(i + 1, len(vertices)):
                right = vertices[j]
                m = self.coxeter_entry(left, right)
                if m != 2:
                    graph.add_edge(left, right, m)
        return graph

    def connected_components(self):
        return tuple(self.induced_subdiagram(component) for component in self.graph().connected_components(sort=False))

    def is_connected(self) -> bool:
        return self.graph().is_connected()

    def induced_subdiagram(self, vertices):
        vertices = tuple(vertices)
        if any(vertex not in self.index_set() for vertex in vertices):
            raise ValueError("an induced subdiagram uses vertices of this diagram")
        matrix_ = self.coxeter_matrix()
        entries = [[matrix_[left, right] for right in vertices] for left in vertices]
        names = tuple(self._names[self.index_set().position(vertex)] for vertex in vertices)
        preferred_positions = None if self._preferred_positions is None else {vertex: self._preferred_positions[vertex] for vertex in vertices}
        if self.is_rooted():
            positions = tuple(self.index_set().position(vertex) for vertex in vertices)
            roots = tuple(self._roots[position] for position in positions)
            gram = tensor(
                self._root_gram.base_ring(),
                (),
                (len(positions), len(positions)),
                [
                    [self._root_gram[i, j] for j in positions]
                    for i in positions
                ],
            )
        else:
            roots = None
            gram = None
        return CoxeterDiagram(
            CoxeterMatrix(entries, index_set=vertices),
            names=names,
            roots=roots,
            root_gram=gram,
            positions=preferred_positions,
        )

    def schlafli_tensor(self):
        r"""Return the normalized reflection Gram tensor ``S_ii=1``."""
        from sage.all import AA, cos, pi

        vertices = tuple(self.index_set())
        values = []
        for left in vertices:
            row = []
            for right in vertices:
                if left == right:
                    row.append(AA.one())
                    continue
                m = self.coxeter_entry(left, right)
                if m == Infinity:
                    row.append(-AA.one())
                else:
                    row.append(-AA(cos(pi / m)))
            values.append(row)
        return tensor(AA, (), (len(vertices), len(vertices)), values)

    def signature_pair(self):
        from dzack_research.preamble.tensors.tensor import _engine_component_matrix

        eigenvalues = _engine_component_matrix(self.schlafli_tensor()).eigenvalues()
        positive = sum(1 for value in eigenvalues if value > 0)
        negative = sum(1 for value in eigenvalues if value < 0)
        zero = len(eigenvalues) - positive - negative
        return (SageZZ(positive), SageZZ(negative), SageZZ(zero))

    def is_elliptic(self) -> bool:
        positive, negative, zero = self.signature_pair()
        return negative == 0 and zero == 0

    def is_parabolic(self) -> bool:
        positive, negative, zero = self.signature_pair()
        return negative == 0 and zero == 1

    def is_hyperbolic(self) -> bool:
        _positive, negative, _zero = self.signature_pair()
        return negative == 1

    def elliptic_subdiagrams(self, *, connected=False):
        from itertools import combinations

        vertices = tuple(self.index_set())
        result = []
        for size in range(len(vertices) + 1):
            for subset in combinations(vertices, size):
                if not subset:
                    continue
                diagram = self.induced_subdiagram(subset)
                if diagram.is_elliptic() and (not connected or diagram.is_connected()):
                    result.append(diagram)
        return tuple(result)

    def parabolic_subdiagrams(self, *, connected=False):
        from itertools import combinations

        vertices = tuple(self.index_set())
        result = []
        for size in range(1, len(vertices) + 1):
            for subset in combinations(vertices, size):
                diagram = self.induced_subdiagram(subset)
                if diagram.is_parabolic() and (not connected or diagram.is_connected()):
                    result.append(diagram)
        return tuple(result)

    def _repr_(self):
        rooted = "rooted " if self.is_rooted() else ""
        return f"{rooted}Coxeter diagram on {self.cardinality()} vertices"


__all__ = ["CoxeterDiagram", "CoxeterDiagrams"]
