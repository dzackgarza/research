r"""Exact algorithms for finite definite integral lattices."""

from __future__ import annotations

from dataclasses import dataclass

from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.qqbar import AA
from sage.rings.rational_field import QQ as SageQQ
from dzack_research.preamble.tensors.tensor import tensor
from dzack_research.preamble.tensors.tensor import _engine_component_matrix
from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_coefficients
from dzack_research.preamble.categories.modules.pure.modules import (
    MatrixSpaces,
)
from dzack_research.preamble.categories.rings.commutative_algebra import PowerSeriesRing
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
)
from dzack_research.preamble.categories.schemes.polytopes import ConvexPolytope
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.rings.real import RR


def _definite_sign(lattice):
    if not lattice.is_finite_rank():
        raise TypeError("definiteness algorithms here require finite rank")
    _signature = lattice.signature_pair()
    positive, negative = _signature.first(), _signature.second()
    rank = lattice.rank()
    ring = lattice.base_ring()
    if positive == rank and negative == 0:
        return ring.one()
    if negative == rank and positive == 0:
        return -ring.one()
    raise ValueError("this algorithm requires a positive- or negative-definite lattice")


def _positive_gram(lattice):
    r"""Return the sign and positive Gram tensor used by definite engines."""
    sign = _definite_sign(lattice)
    return sign, sign * lattice.gram_tensor()


def _element_from_coordinates(lattice, coordinates):
    ring = lattice.base_ring()

    def owned(coefficient):
        if getattr(coefficient, "parent", lambda: None)() is ring:
            return coefficient
        return ring._from_engine_element(coefficient)

    return lattice.linear_combination(
        {
            label: owned(coefficient)
            for label, coefficient in zip(
                lattice.module_generating_set(), coordinates, strict=True
            )
            if coefficient
        }
    )


@dataclass(frozen=True)
class LatticeReduction:
    original: object
    reduced: object
    isometry: object
    change_of_basis_matrix: object


def lll_reduction(lattice):
    _sign, positive_gram = _positive_gram(lattice)
    engine_gram = _engine_component_matrix(positive_gram)
    backend_rows = engine_gram.LLL_gram()
    return _reduction_from_backend_rows(lattice, backend_rows)


def _reduction_from_backend_rows(lattice, backend_rows):

    ring = lattice.base_ring()
    rank = int(lattice.rank())
    # Definite-lattice engines return basis vectors as rows.  The live linear
    # map acts on coordinate columns, hence the transpose here.
    basis_map = MatrixSpace(ring, rank, rank).from_rows(
        tuple(
            tuple(
                ring._from_engine_element(backend_rows[column, row])
                for column in range(rank)
            )
            for row in range(rank)
        )
    )
    return _reduction_from_transformation(lattice, basis_map)


def _reduction_from_transformation(lattice, basis_map):

    if basis_map.parent() not in MatrixSpaces(lattice.base_ring()):
        raise TypeError("a lattice reframing is an owned matrix-Hom morphism")
    reduced_gram = lattice.gram_tensor().pullback(basis_map)
    reduced = lattice.lattice_category()(reduced_gram)
    original_generators = tuple(lattice.module_generators())
    images = tuple(
        sum(
            (
                lattice.scalar_multiple(
                    basis_map[row, column], original_generators[row]
                )
                for row in range(len(original_generators))
                if basis_map[row, column]
            ),
            lattice.zero(),
        )
        for column in range(len(original_generators))
    )
    isometry = reduced.Isom(lattice)(images)
    reduced._preamble_lll_isometry = isometry
    reduced._preamble_lll_change_of_basis = basis_map
    return LatticeReduction(lattice, reduced, isometry, basis_map)


def bkz_reduction(lattice, block_size=20):
    r"""Return a BKZ-reframed copy with its exact integral isometry witness."""
    from fpylll import BKZ, GSO, LLL, IntegerMatrix

    _sign, positive_gram = _positive_gram(lattice)
    rank = positive_gram.tensor_shape()[0]
    if rank <= 1:

        return _reduction_from_transformation(
            lattice, MatrixSpace(lattice.base_ring(), rank, rank).identity_matrix()
        )
    block_size = min(max(2, int(block_size)), rank)
    backend_gram = IntegerMatrix.from_matrix(_engine_component_matrix(positive_gram))
    backend_transformation = IntegerMatrix.identity(rank)
    gso = GSO.Mat(
        backend_gram,
        U=backend_transformation,
        gram=True,
        update=True,
    )
    lll = LLL.Reduction(gso)
    lll()
    BKZ.Reduction(gso, lll, BKZ.Param(block_size=block_size))()
    from sage.matrix.constructor import matrix as sage_matrix

    backend_rows = sage_matrix(
        SageZZ,
        rank,
        rank,
        [
            backend_transformation[row, column]
            for row in range(rank)
            for column in range(rank)
        ],
    )
    return _reduction_from_backend_rows(lattice, backend_rows)


def hkz_reduction(lattice):
    return bkz_reduction(lattice, block_size=int(lattice.rank()))


def minimum(lattice):
    sign, positive_gram = _positive_gram(lattice)
    backend = IntegralLattice(_engine_component_matrix(positive_gram))
    minimum_value = lattice.base_ring()._from_engine_element(
        SageZZ(backend.minimum())
    )
    return sign * minimum_value


def vectors_of_square(lattice, square):
    sign, positive_gram = _positive_gram(lattice)
    square = lattice.base_ring()(square)
    target = sign * square
    if target < 0:
        return tuple()
    backend = IntegralLattice(_engine_component_matrix(positive_gram))
    lists = backend.short_vectors(int(target) + 1)
    if int(target) >= len(lists):
        return tuple()
    return tuple(_element_from_coordinates(lattice, coordinates) for coordinates in lists[int(target)])


def roots(lattice):
    sign = _definite_sign(lattice)
    return vectors_of_square(lattice, 2 * sign)


def roots_of_square(lattice, square):
    square = lattice.base_ring()(square)
    if square == 0:
        return tuple()
    return tuple(vector for vector in vectors_of_square(lattice, square) if vector.is_root())


def root_sublattice(lattice):
    r"""Return the formed subobject generated by all square-two roots."""
    from sage.combinat.root_system.cartan_type import CartanType
    from sage.graphs.graph import Graph

    root_vectors = tuple(roots(lattice))
    if not root_vectors:
        return lattice.subobject_on(())
    coordinates = {root: _coordinate_tuple(lattice, root) for root in root_vectors}
    zero = (SageZZ.zero(),) * int(lattice.rank())
    positive = tuple(root for root in root_vectors if coordinates[root] > zero)
    positive_coordinates = {coordinates[root] for root in positive}
    simple = tuple(
        candidate
        for candidate in positive
        if not any(
            tuple(left - right for left, right in zip(coordinates[candidate], coordinates[other], strict=True)) in positive_coordinates
            for other in positive
            if other is not candidate
        )
    )
    graph = Graph(multiedges=False, loops=False)
    graph.add_vertices(range(len(simple)))
    graph.add_edges((left, right) for left in range(len(simple)) for right in range(left + 1, len(simple)) if simple[left].b(simple[right]) != 0)
    ordered = []
    component_types = []
    for component in graph.connected_components(sort=True):
        size = len(component)
        candidates = [CartanType(["A", size])]
        if size >= 4:
            candidates.append(CartanType(["D", size]))
        if size in (6, 7, 8):
            candidates.append(CartanType(["E", size]))
        component_graph = graph.subgraph(component)
        for candidate_type in candidates:
            standard = Graph(
                candidate_type.dynkin_diagram().to_undirected(),
                multiedges=False,
            )
            isomorphic, certificate = component_graph.is_isomorphic(standard, certificate=True)
            if isomorphic:
                break
        else:
            raise RuntimeError("a simply-laced finite root component must have ADE type")
        by_label = {certificate[vertex]: vertex for vertex in component}
        ordered.extend(simple[by_label[label]] for label in candidate_type.index_set())
        component_types.append(candidate_type)

    recognized = component_types[0] if len(component_types) == 1 else CartanType(component_types)

    if lattice.is_negative_definite():
        return lattice._root_subobject_on(ordered, recognized)
    return lattice.subobject_on(ordered)


def vectors_of_square_and_divisibility(lattice, square, divisibility):
    divisibility = lattice.base_ring()(divisibility)
    return tuple(vector for vector in vectors_of_square(lattice, square) if vector.div() == divisibility)


def shortest_vectors(lattice):
    target = minimum(lattice)
    return vectors_of_square(lattice, target)


def _target_coordinates(lattice, target):
    if getattr(target, "parent", lambda: None)() is lattice:

        coefficients = module_coefficients(target, lattice)
        target = [
            coefficients.get(label, lattice.base_ring().zero())
            for label in lattice.module_generating_set()
        ]
    rationals = lattice.base_ring().fraction_field()
    point = tensor.vector(rationals, target)
    if point.tensor_shape()[0] != int(lattice.rank()):
        raise ValueError("a closest-vector target has one coordinate per lattice generator")
    return point


def closest_vector(lattice, target):
    r"""Return the exact closest lattice vector to a rational target."""
    from itertools import product
    from sage.functions.other import ceil, floor, sqrt

    point = _target_coordinates(lattice, target)
    rationals = point.base_ring()
    _sign, gram = _positive_gram(lattice)
    gram = gram.change_ring(rationals)
    rank = gram.tensor_shape()[0]
    if rank == 0:
        return lattice.zero()

    def distance_squared(coordinates):
        delta = tensor.vector(rationals, coordinates) - point
        return gram.contract(delta, delta)

    best_coordinates = tuple(
        lattice.base_ring()(
            int(_engine_element(rationals, entry).round())
        )
        for entry in point
    )
    best_distance = distance_squared(best_coordinates)
    dual_gram = gram.dual_tensor()
    coordinate_ranges = []
    for index in range(rank):
        radius = sqrt(
            _engine_element(
                rationals, best_distance * dual_gram[index, index]
            )
        )
        center = _engine_element(rationals, point[index])
        lower = int(floor(center - radius)) - 1
        upper = int(ceil(center + radius)) + 1
        coordinate_ranges.append(range(lower, upper + 1))
    for raw_coordinates in product(*coordinate_ranges):
        candidate = tuple(lattice.base_ring()(entry) for entry in raw_coordinates)
        distance = distance_squared(candidate)
        if distance < best_distance or (
            distance == best_distance
            and tuple(int(x) for x in candidate)
            < tuple(int(x) for x in best_coordinates)
        ):
            best_coordinates = candidate
            best_distance = distance
    return _element_from_coordinates(lattice, best_coordinates)


def babai(lattice, target):
    r"""Return Babai's LLL nearest-plane approximation."""
    point = _target_coordinates(lattice, target)
    rank = int(lattice.rank())
    if rank == 0:
        return lattice.zero()
    _sign, gram = _positive_gram(lattice)
    from sage.modules.free_module_element import vector as sage_vector

    rationals = point.base_ring()
    backend_rows = _engine_component_matrix(gram).LLL_gram().change_ring(SageQQ)
    basis_map = backend_rows.transpose()
    point_backend = sage_vector(
        SageQQ,
        [_engine_element(rationals, entry) for entry in point],
    )
    reduced_coordinates = basis_map.inverse() * point_backend
    rounded = sage_vector(SageQQ, [entry.round() for entry in reduced_coordinates])
    original = basis_map * rounded
    return _element_from_coordinates(lattice, tuple(original))


def voronoi_cell(lattice, bound=None):
    r"""Return the owned rational Voronoi cell in lattice coordinates."""
    from sage.geometry.polyhedron.constructor import Polyhedron

    _sign, gram = _positive_gram(lattice)
    rank = gram.tensor_shape()[0]
    rationals = lattice.base_ring().fraction_field()
    if rank == 0:
        return ConvexPolytope(
            Polyhedron(vertices=[[]], base_ring=SageQQ)
        )
    gram_q = gram.change_ring(rationals)
    engine_gram = _engine_component_matrix(gram)

    def cell_from_bound(radius):
        backend_radius = SageZZ(int(radius))
        _count, _largest, raw_coordinates = engine_gram.__pari__().qfminim(
            backend_radius, None
        )
        coordinates = raw_coordinates
        inequalities = []
        for column_index in range(coordinates.ncols()):
            column = tensor.vector(
                rationals,
                [
                    rationals._from_engine_element(
                        SageQQ(coordinates[row_index, column_index])
                    )
                    for row_index in range(rank)
                ],
            )
            for signed in (column, -column):
                covector = gram_q * signed
                square = covector * signed
                owned_entries = [
                    square / rationals(2),
                    *(-entry for entry in covector.components()),
                ]
                inequalities.append(
                    [_engine_element(rationals, entry) for entry in owned_entries]
                )
        return ConvexPolytope(
            Polyhedron(ieqs=inequalities, base_ring=SageQQ)
        )

    if bound is not None:
        return cell_from_bound(bound)
    radius = max(int(gram[index, index]) for index in range(rank)) + 1
    for _attempt in range(16):
        cell = cell_from_bound(radius)
        if cell._engine_polyhedron().is_compact():
            return cell
        radius *= 2
    raise RuntimeError(
        f"failed to close the Voronoi cell within square bound {radius}"
    )


def voronoi_relevant_vectors(lattice):
    r"""Return the vectors defining facets of the Voronoi cell."""
    cell = voronoi_cell(lattice)
    _sign, gram = _positive_gram(lattice)
    rank = gram.tensor_shape()[0]
    rationals = lattice.base_ring().fraction_field()
    dual_gram = gram.change_ring(rationals).dual_tensor()
    relevant = []
    for inequality in cell._engine_polyhedron().inequalities():
        coefficients = tuple(
            rationals._from_engine_element(SageQQ(entry))
            for entry in inequality.A()
        )
        covector = tensor(rationals, (), (rank,), coefficients)
        vector_coordinates = -(dual_gram * covector)
        try:
            integral = tuple(
                lattice.base_ring()(coordinate)
                for coordinate in vector_coordinates
            )
        except (TypeError, ValueError):
            continue
        candidate = _element_from_coordinates(lattice, integral)
        if candidate != lattice.zero() and candidate not in relevant:
            relevant.append(candidate)
    return tuple(relevant)


def successive_minima(lattice):
    r"""Return the family of exact successive lengths, as owned real numbers."""
    from sage.matrix.constructor import matrix as sage_matrix

    _sign, gram = _positive_gram(lattice)

    rank = gram.tensor_shape()[0]
    if rank == 0:
        return finite_family((), name="Successive minima")
    engine_gram = _engine_component_matrix(gram)
    transformation = engine_gram.LLL_gram()
    reduced = transformation * engine_gram * transformation.transpose()
    bound = max(reduced.diagonal())
    _count, _largest, raw_coordinates = engine_gram.__pari__().qfminim(bound, None)
    coordinate_array = raw_coordinates
    if coordinate_array.nrows() != rank:
        coordinate_array = coordinate_array.transpose()
    ring = lattice.base_ring()
    coordinates = tuple(
        tensor.vector(
            ring,
            [
                ring._from_engine_element(
                    SageZZ(coordinate_array[row, column])
                )
                for row in range(rank)
            ],
        )
        for column in range(coordinate_array.ncols())
    )
    candidates = sorted(
        tuple(coordinates) + tuple(-column for column in coordinates),
        key=lambda column: (
            int(gram.contract(column, column)),
            tuple(int(entry) for entry in column),
        ),
    )
    independent = []
    for column in candidates:
        trial = independent + [column]
        backend_rows = sage_matrix(
            SageZZ,
            len(trial),
            rank,
            [
                _engine_element(ring, coefficient)
                for row in trial
                for coefficient in row
            ],
        )
        if backend_rows.rank() > len(independent):
            independent.append(column)
            if len(independent) == rank:
                break
    if len(independent) != rank:
        raise RuntimeError("short-vector enumeration did not span the lattice space")

    return finite_family(
        tuple(
            RR(_engine_element(ring, gram.contract(column, column))).sqrt()
            for column in independent
        ),
        name="Successive minima",
    )


def gaussian_heuristic(lattice, *, exact_form=False):
    r"""Return the Gaussian-heuristic shortest-vector radius of ``lattice``.

    The radius ``r`` is defined by ``vol(B_n(r)) = covol(lattice)``.  For a
    Gram matrix ``G`` this is

    ``r = (sqrt(abs(det(G))) / V_n)^(1/n)``,

    where ``V_n = pi^(n/2) / Gamma(n/2 + 1)`` is the volume of the Euclidean
    unit ball.  ``exact_form=True`` keeps this symbolic expression; otherwise
    the result is returned in the owned real field.
    """
    from sage.functions.gamma import gamma
    from sage.symbolic.constants import pi
    from sage.symbolic.ring import SR

    _definite_sign(lattice)
    rank = int(lattice.rank())
    if rank == 0:
        raise ValueError("the zero lattice has no Gaussian-heuristic radius")
    ring = lattice.base_ring()
    covolume = SR(_engine_element(ring, abs(lattice.determinant()))).sqrt()
    dimension = SageQQ(rank)
    unit_ball_volume = pi ** (dimension / 2) / gamma(dimension / 2 + 1)
    expression = (covolume / unit_ball_volume) ** (SageQQ.one() / rank)
    if exact_form:
        return expression
    return RR._from_engine_expression(expression)


def hadamard_ratio(lattice):
    from sage.misc.misc_c import prod
    from sage.symbolic.ring import SR

    _sign, gram = _positive_gram(lattice)
    rank = int(gram.tensor_shape()[0])
    if rank == 0:
        raise ValueError("the zero lattice has no framing ratio")
    ring = lattice.base_ring()
    product_of_norms = prod(
        SR(_engine_element(ring, gram[index, index])).sqrt()
        for index in range(rank)
    )
    determinant = abs(lattice.determinant())
    expression = (
        SR(_engine_element(ring, determinant)).sqrt() / product_of_norms
    ) ** (SageQQ.one() / rank)
    return RR(expression)


def contact_polytope(lattice):
    from sage.geometry.polyhedron.constructor import Polyhedron

    rationals = lattice.base_ring().fraction_field()
    vertices = [
        [
            _engine_element(rationals, rationals(coordinate))
            for coordinate in _coordinate_tuple(lattice, vector)
        ]
        for vector in shortest_vectors(lattice)
    ]
    return ConvexPolytope(
        Polyhedron(vertices=vertices, base_ring=SageQQ)
    )


def _coordinate_tuple(lattice, element):

    coefficients = module_coefficients(element, lattice)
    return tuple(coefficients.get(label, lattice.base_ring().zero()) for label in lattice.module_generating_set())


def covering_radius(lattice):

    _sign, gram = _positive_gram(lattice)
    rationals = lattice.base_ring().fraction_field()
    gram_q = gram.change_ring(rationals)
    cell = voronoi_cell(lattice)
    squared = max(
        gram_q.contract(
            tensor.vector(
                rationals,
                [
                    rationals._from_engine_element(SageQQ(coordinate))
                    for coordinate in vertex
                ],
            ),
            tensor.vector(
                rationals,
                [
                    rationals._from_engine_element(SageQQ(coordinate))
                    for coordinate in vertex
                ],
            ),
        )
        for vertex in cell._engine_polyhedron().vertices_list()
    )
    return RR(_engine_element(rationals, squared)).sqrt()


def center_density(lattice):

    _sign, gram = _positive_gram(lattice)
    rank = int(gram.tensor_shape()[0])
    if rank == 0:
        raise ValueError("the zero lattice has no sphere packing")
    determinant_length = RR(
        _engine_element(lattice.base_ring(), abs(lattice.determinant()))
    ).sqrt()
    return packing_radius(lattice) ** rank / determinant_length


def packing_density(lattice):
    from sage.functions.gamma import gamma
    from sage.symbolic.constants import pi

    rank = int(lattice.rank())
    factor = pi ** (SageQQ(rank) / 2) / gamma(1 + SageQQ(rank) / 2)
    return RR._from_engine_expression(factor) * center_density(lattice)


def theta_series(lattice, precision=20, variable="q"):

    _sign, positive_gram = _positive_gram(lattice)
    quadratic_form = QuadraticForm(
        SageZZ,
        2 * _engine_component_matrix(positive_gram),
    )
    backend_series = quadratic_form.theta_series(
        int(precision), var_str=variable
    )
    series_ring = PowerSeriesRing(lattice.base_ring(), variable)
    engine = _engine_ring(series_ring)
    return series_ring._from_engine_element(engine(backend_series))


def hermite_invariant(lattice):

    sign, _positive_gram_tensor = _positive_gram(lattice)
    rank = int(lattice.rank())
    ring = lattice.base_ring()
    metric_minimum = _engine_element(ring, sign * minimum(lattice))
    determinant = _engine_element(ring, abs(lattice.determinant()))
    from sage.symbolic.ring import SR

    value = SR(metric_minimum) / SR(determinant) ** (SageQQ.one() / rank)
    return RR._from_engine_expression(value)


def packing_radius(lattice):

    sign = _definite_sign(lattice)
    metric_minimum = sign * minimum(lattice)
    return RR(_engine_element(lattice.base_ring(), metric_minimum)).sqrt() / 2


def kissing_number(lattice):
    return lattice.base_ring()(len(shortest_vectors(lattice)))


__all__ = [
    "LatticeReduction",
    "babai",
    "bkz_reduction",
    "center_density",
    "closest_vector",
    "contact_polytope",
    "covering_radius",
    "gaussian_heuristic",
    "hadamard_ratio",
    "hermite_invariant",
    "hkz_reduction",
    "kissing_number",
    "lll_reduction",
    "minimum",
    "packing_density",
    "packing_radius",
    "root_sublattice",
    "roots",
    "roots_of_square",
    "shortest_vectors",
    "successive_minima",
    "theta_series",
    "vectors_of_square_and_divisibility",
    "vectors_of_square",
    "voronoi_cell",
    "voronoi_relevant_vectors",
]
