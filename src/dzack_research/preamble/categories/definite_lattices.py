r"""Exact algorithms for finite definite integral lattices."""

from __future__ import annotations

from dataclasses import dataclass

from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.qqbar import AA
from sage.rings.rational_field import QQ
from dzack_research.preamble.tensors import tensor
from dzack_research.preamble.tensors.tensor import _engine_component_matrix


def _definite_sign(lattice):
    if not lattice.is_finite_rank():
        raise TypeError("definiteness algorithms here require finite rank")
    positive, negative = lattice.signature_pair()
    rank = lattice.rank()
    if positive == rank and negative == 0:
        return SageZZ.one()
    if negative == rank and positive == 0:
        return -SageZZ.one()
    raise ValueError("this algorithm requires a positive- or negative-definite lattice")


def _positive_gram(lattice):
    r"""Return the sign and positive Gram tensor used by definite engines."""
    sign = _definite_sign(lattice)
    return sign, sign * lattice.gram_tensor().change_ring(SageZZ)


def _element_from_coordinates(lattice, coordinates):
    return lattice.linear_combination({label: coefficient for label, coefficient in zip(lattice.module_generating_set(), coordinates, strict=True) if coefficient})


@dataclass(frozen=True)
class LatticeReduction:
    original: object
    reduced: object
    isometry: object
    change_of_basis_tensor: object


def lll_reduction(lattice):
    _sign, positive_gram = _positive_gram(lattice)
    engine_gram = _engine_component_matrix(positive_gram)
    backend_rows = engine_gram.LLL_gram()
    basis_map = tensor.matrix(SageZZ, backend_rows).dual_tensor()
    return _reduction_from_transformation(lattice, basis_map)


def _reduction_from_transformation(lattice, basis_map):
    if basis_map.tensor_valence() != (1, 1):
        raise TypeError("a lattice reframing is a type-(1,1) tensor")
    reduced_gram = lattice.gram_tensor().pullback(basis_map)
    from dzack_research.preamble.categories.lattices import Lattices

    reduced = Lattices(lattice.base_ring())(reduced_gram)
    original_generators = tuple(lattice.module_generators())
    images = tuple(
        sum(
            (
                basis_map[row, column] * original_generators[row]
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
            lattice, tensor.matrix.identity(SageZZ, rank)
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
    backend_rows = tensor.matrix(
        SageZZ,
        [[backend_transformation[row, column] for column in range(rank)] for row in range(rank)],
    )
    return _reduction_from_transformation(lattice, backend_rows.dual_tensor())


def hkz_reduction(lattice):
    return bkz_reduction(lattice, block_size=int(lattice.rank()))


def minimum(lattice):
    sign, positive_gram = _positive_gram(lattice)
    backend = IntegralLattice(_engine_component_matrix(positive_gram))
    return sign * SageZZ(backend.minimum())


def vectors_of_square(lattice, square):
    sign, positive_gram = _positive_gram(lattice)
    square = SageZZ(square)
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
    square = SageZZ(square)
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
    from dzack_research.preamble.categories.lattices import Lattices
    from dzack_research.preamble.categories.modules.subobjects import ModuleSubobjects
    from dzack_research.preamble.categories.root_lattices import refine_root_lattice
    from dzack_research.preamble.categories.sets import finite_ordered_set
    from dzack_research.preamble.refine import refine

    labels = finite_ordered_set(range(len(ordered)))
    source = Lattices(lattice.base_ring())(
        [[left.b(right) for right in ordered] for left in ordered],
        module_generators=labels,
    )
    inclusion = source.Emb(lattice)({label: root for label, root in zip(labels, ordered, strict=True)})
    source._preamble_inclusion = inclusion
    refine(source, ModuleSubobjects(lattice.base_ring()))
    if lattice.is_negative_definite():
        refine_root_lattice(source, recognized)
    return source


def vectors_of_square_and_divisibility(lattice, square, divisibility):
    divisibility = SageZZ(divisibility)
    return tuple(vector for vector in vectors_of_square(lattice, square) if vector.div() == divisibility)


def shortest_vectors(lattice):
    target = minimum(lattice)
    return vectors_of_square(lattice, target)


def _target_coordinates(lattice, target):
    if getattr(target, "parent", lambda: None)() is lattice:
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_coefficients,
        )

        coefficients = module_coefficients(target, lattice)
        target = [coefficients.get(label, lattice.base_ring().zero()) for label in lattice.module_generating_set()]
    point = tensor.vector(QQ, target)
    if len(point) != lattice.rank():
        raise ValueError("a closest-vector target has one coordinate per lattice generator")
    return point


def closest_vector(lattice, target):
    r"""Return the exact closest lattice vector to a rational target."""
    from itertools import product

    from sage.functions.other import ceil, floor, sqrt
    point = _target_coordinates(lattice, target)
    _sign, gram = _positive_gram(lattice)
    gram = gram.change_ring(QQ)
    rank = gram.tensor_shape()[0]
    if rank == 0:
        return lattice.zero()

    def distance_squared(coordinates):
        delta = tensor.vector(QQ, coordinates) - point
        return gram.contract(delta, delta)

    best_coordinates = tuple(SageZZ(entry.round()) for entry in point)
    best_distance = distance_squared(best_coordinates)
    dual_gram = gram.dual_tensor()
    coordinate_ranges = []
    for index in range(rank):
        radius = sqrt(best_distance * dual_gram[index, index])
        lower = SageZZ(floor(point[index] - radius)) - 1
        upper = SageZZ(ceil(point[index] + radius)) + 1
        coordinate_ranges.append(range(lower, upper + 1))
    for raw_coordinates in product(*coordinate_ranges):
        candidate = tuple(SageZZ(entry) for entry in raw_coordinates)
        distance = distance_squared(candidate)
        if distance < best_distance or (distance == best_distance and candidate < best_coordinates):
            best_coordinates = candidate
            best_distance = distance
    return _element_from_coordinates(lattice, best_coordinates)


def babai(lattice, target):
    r"""Return Babai's LLL nearest-plane approximation."""
    point = _target_coordinates(lattice, target)
    _sign, gram = _positive_gram(lattice)
    rank = gram.tensor_shape()[0]
    if rank == 0:
        return lattice.zero()
    engine_gram = _engine_component_matrix(gram)
    backend_rows = engine_gram.LLL_gram().change_ring(QQ)
    basis_map = tensor.matrix(QQ, backend_rows).dual_tensor()
    reduced_coordinates = basis_map.inverse_tensor() * point
    rounded = tensor.vector(QQ, (SageZZ(entry.round()) for entry in reduced_coordinates))
    return _element_from_coordinates(lattice, basis_map * rounded)


def voronoi_cell(lattice, bound=None):
    r"""Return the rational Voronoi cell in the chosen lattice coordinates."""
    from sage.geometry.polyhedron.constructor import Polyhedron
    _sign, gram = _positive_gram(lattice)
    rank = gram.tensor_shape()[0]
    if rank == 0:
        return Polyhedron(vertices=[[]], base_ring=QQ)
    gram_q = gram.change_ring(QQ)
    engine_gram = _engine_component_matrix(gram)

    def cell_from_bound(radius):
        _count, _largest, raw_coordinates = engine_gram.__pari__().qfminim(SageZZ(radius), None)
        coordinates = tensor.matrix(SageZZ, raw_coordinates)
        inequalities = []
        for column_index in range(coordinates.tensor_shape()[1]):
            column = tensor.vector(
                QQ,
                [coordinates[row_index, column_index] for row_index in range(rank)],
            )
            for signed in (column, -column):
                covector = gram_q * signed
                square = covector * signed
                inequalities.append(
                    [square / 2, *(-entry for entry in covector.components())]
                )
        return Polyhedron(ieqs=inequalities, base_ring=QQ)

    if bound is not None:
        return cell_from_bound(bound)
    radius = SageZZ(max(gram[index, index] for index in range(rank)) + 1)
    for _attempt in range(16):
        cell = cell_from_bound(radius)
        if cell.is_compact():
            return cell
        radius *= 2
    raise RuntimeError(f"failed to close the Voronoi cell within square bound {radius}")


def voronoi_relevant_vectors(lattice):
    r"""Return the vectors defining facets of the Voronoi cell."""
    cell = voronoi_cell(lattice)
    _sign, gram = _positive_gram(lattice)
    rank = gram.tensor_shape()[0]
    dual_gram = gram.change_ring(QQ).dual_tensor()
    relevant = []
    for inequality in cell.inequalities():
        coefficients = tuple(inequality.A())
        covector = tensor(QQ, (), (rank,), coefficients)
        vector_coordinates = -(dual_gram * covector)
        if all(coordinate in SageZZ for coordinate in vector_coordinates):
            candidate = _element_from_coordinates(lattice, (SageZZ(coordinate) for coordinate in vector_coordinates))
            if candidate != lattice.zero() and candidate not in relevant:
                relevant.append(candidate)
    return tuple(relevant)


def successive_minima(lattice):
    r"""Return the exact symbolic successive lengths."""
    from sage.symbolic.ring import SR

    _sign, gram = _positive_gram(lattice)
    rank = gram.tensor_shape()[0]
    if rank == 0:
        return tuple()
    engine_gram = _engine_component_matrix(gram)
    transformation = engine_gram.LLL_gram()
    reduced = transformation * engine_gram * transformation.transpose()
    bound = max(reduced.diagonal())
    _count, _largest, raw_coordinates = engine_gram.__pari__().qfminim(bound, None)
    coordinate_array = tensor.matrix(SageZZ, raw_coordinates)
    coordinates = tuple(
        tensor.vector(
            SageZZ,
            [coordinate_array[row, column] for row in range(rank)],
        )
        for column in range(coordinate_array.tensor_shape()[1])
    )
    candidates = sorted(
        tuple(coordinates) + tuple(-column for column in coordinates),
        key=lambda column: (gram.contract(column, column), tuple(column)),
    )
    independent = []
    for column in candidates:
        row_array = tensor.matrix(
            SageZZ,
            [tuple(vector) for vector in independent + [column]],
        )
        if row_array.rank() > len(independent):
            independent.append(column)
            if len(independent) == rank:
                break
    if len(independent) != rank:
        raise RuntimeError("short-vector enumeration did not span the lattice space")
    return tuple(SR(gram.contract(column, column)).sqrt() for column in independent)


def gaussian_heuristic(lattice, *, exact_form=False):
    from sage.functions.gamma import gamma
    from sage.symbolic.constants import e, pi
    from sage.symbolic.ring import SR

    _sign, gram = _positive_gram(lattice)
    rank = gram.tensor_shape()[0]
    if rank == 0:
        raise ValueError("the zero lattice has no expected shortest length")
    exponent = QQ.one() / rank
    determinant_sqrt = SR(gram.det()).sqrt()
    if exact_form:
        return (determinant_sqrt * gamma(1 + QQ(rank) / 2)) ** exponent / pi.sqrt()
    return determinant_sqrt**exponent * (rank / (2 * pi * e)).sqrt()


def hadamard_ratio(lattice):
    from sage.misc.misc_c import prod
    from sage.symbolic.ring import SR

    _sign, gram = _positive_gram(lattice)
    rank = gram.tensor_shape()[0]
    if rank == 0:
        raise ValueError("the zero lattice has no framing ratio")
    product_of_norms = prod(SR(gram[index, index]).sqrt() for index in range(rank))
    return (SR(gram.det()).sqrt() / product_of_norms) ** (QQ.one() / rank)


def contact_polytope(lattice):
    from sage.geometry.polyhedron.constructor import Polyhedron

    return Polyhedron(
        vertices=[_coordinate_tuple(lattice, vector) for vector in shortest_vectors(lattice)],
        base_ring=QQ,
    )


def _coordinate_tuple(lattice, element):
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_coefficients,
    )

    coefficients = module_coefficients(element, lattice)
    return tuple(coefficients.get(label, lattice.base_ring().zero()) for label in lattice.module_generating_set())


def covering_radius(lattice):
    from sage.symbolic.ring import SR

    _sign, gram = _positive_gram(lattice)
    gram_q = gram.change_ring(QQ)
    squared = max(
        gram_q.contract(
            tensor.vector(QQ, vertex),
            tensor.vector(QQ, vertex),
        )
        for vertex in voronoi_cell(lattice).vertices_list()
    )
    return SR(squared).sqrt()


def center_density(lattice):
    from sage.symbolic.ring import SR

    _sign, gram = _positive_gram(lattice)
    rank = gram.tensor_shape()[0]
    if rank == 0:
        raise ValueError("the zero lattice has no sphere packing")
    return packing_radius(lattice) ** rank / SR(gram.det()).sqrt()


def packing_density(lattice):
    from sage.functions.gamma import gamma
    from sage.symbolic.constants import pi

    rank = int(lattice.rank())
    return pi ** (QQ(rank) / 2) / gamma(1 + QQ(rank) / 2) * center_density(lattice)


def theta_series(lattice, precision=20, variable="q"):
    _sign, positive_gram = _positive_gram(lattice)
    quadratic_form = QuadraticForm(
        SageZZ,
        2 * _engine_component_matrix(positive_gram),
    )
    return quadratic_form.theta_series(int(precision), var_str=variable)


def hermite_invariant(lattice):
    sign, positive_gram = _positive_gram(lattice)
    rank = int(lattice.rank())
    metric_minimum = SageZZ(sign * minimum(lattice))
    determinant = abs(SageZZ(positive_gram.det()))
    return AA(metric_minimum) / AA(determinant) ** (AA.one() / rank)


def packing_radius(lattice):
    sign = _definite_sign(lattice)
    metric_minimum = AA(sign * minimum(lattice))
    return metric_minimum.sqrt() / 2


def kissing_number(lattice):
    return SageZZ(len(shortest_vectors(lattice)))


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
