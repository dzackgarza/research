r"""Exact algorithms for finite definite integral lattices."""

from __future__ import annotations

from dataclasses import dataclass

from sage.matrix.constructor import matrix as engine_matrix
from sage.modules.free_module_element import vector as engine_vector
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.element import parent as element_parent

from dzack_research.preamble.categories.modules.pure.modules import (
    MatrixSpaces,
    ModuleSubobjects,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
)
from dzack_research.preamble.categories.schemes.polytopes import ConvexPolytopes
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.rings.real import RR
from dzack_research.preamble.tensors.tensor import _engine_component_matrix, tensor


def _definite_sign(lattice):
    if not lattice.module_rank().is_finite():
        raise TypeError("definiteness algorithms here require finite rank")
    _signature = lattice.signature_pair()
    positive, negative = _signature.first(), _signature.second()
    rank = lattice.module_rank()
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
        if element_parent(coefficient) is ring:
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


def _lll_reduction(lattice):
    _sign, positive_gram = _positive_gram(lattice)
    engine_gram = _engine_component_matrix(positive_gram)
    backend_rows = engine_gram.LLL_gram()
    return _reduction_from_backend_rows(lattice, backend_rows)


def _reduction_from_backend_rows(lattice, backend_rows):

    ring = lattice.base_ring()
    rank = int(lattice.module_rank())
    # Definite-lattice engines return basis vectors as rows.  The live linear
    # map acts on coordinate columns, hence the transpose here.
    basis_map = ring.matrix_space(rank, rank).from_rows(
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
    reduced_gram = lattice.gram_tensor().pullback(basis_map)
    if lattice in ModuleSubobjects(lattice.base_ring()):
        from dzack_research.preamble.categories.lattices import (
            _lattice_subobject_spanning,
        )

        ambient = lattice.ambient_lattice()
        old_inclusion = lattice.inclusion()
        embedded_reduced_basis = finite_ordered_set(
            tuple(old_inclusion(image) for image in images)
        )
        reduced = _lattice_subobject_spanning(
            ambient,
            embedded_reduced_basis,
        )
        if reduced.gram_tensor() != reduced_gram:
            raise ArithmeticError(
                "the reduced subobject framing does not have the pulled-back Gram form"
            )
    else:
        reduced = lattice.lattice_category()(reduced_gram)
    isometry = reduced.Isom(lattice)(images)
    return LatticeReduction(lattice, reduced, isometry, basis_map)


def _bkz_reduction(lattice, block_size=20):
    r"""Return a BKZ-reframed copy with its exact integral isometry witness."""
    from fpylll import BKZ, GSO, LLL, IntegerMatrix

    _sign, positive_gram = _positive_gram(lattice)
    rank = positive_gram.tensor_shape()[0]
    if rank <= 1:

        return _reduction_from_transformation(
            lattice, lattice.base_ring().matrix_space(rank, rank).identity_matrix()
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


def _hkz_reduction(lattice):
    return lattice.bkz_reduction(block_size=int(lattice.module_rank()))


def _minimum(lattice):
    sign, positive_gram = _positive_gram(lattice)
    backend = IntegralLattice(_engine_component_matrix(positive_gram))
    minimum_value = lattice.base_ring()._from_engine_element(
        SageZZ(backend.minimum())
    )
    return sign * minimum_value


def _vectors_of_square(lattice, square):
    sign, positive_gram = _positive_gram(lattice)
    square = lattice.base_ring()(square)
    target = sign * square
    if target < 0:
        return finite_ordered_set(())
    backend = IntegralLattice(_engine_component_matrix(positive_gram))
    lists = backend.short_vectors(int(target) + 1)
    if int(target) >= len(lists):
        return finite_ordered_set(())
    return finite_ordered_set(tuple(
        _element_from_coordinates(lattice, coordinates)
        for coordinates in lists[int(target)]
    ))


def _roots(lattice):
    sign = _definite_sign(lattice)
    return lattice.vectors_of_square(2 * sign)


def _roots_of_square(lattice, square):
    square = lattice.base_ring()(square)
    if square == 0:
        return finite_ordered_set(())
    return finite_ordered_set(tuple(
        vector for vector in lattice.vectors_of_square(square) if vector.is_root()
    ))


def _root_sublattice(lattice):
    r"""Return the formed subobject generated by all square-two roots."""
    from sage.combinat.root_system.cartan_type import CartanType
    from sage.graphs.graph import Graph

    root_vectors = tuple(lattice.roots())
    if not root_vectors:
        return lattice.subobject_on(())
    coordinates = {root: _coordinate_tuple(lattice, root) for root in root_vectors}
    zero = (SageZZ.zero(),) * int(lattice.module_rank())
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


def _vectors_of_square_and_divisibility(lattice, square, divisibility):
    divisibility = lattice.base_ring()(divisibility)
    return finite_ordered_set(tuple(
        vector
        for vector in lattice.vectors_of_square(square)
        if vector.div() == divisibility
    ))


def _shortest_vectors(lattice):
    target = lattice.minimum()
    return lattice.vectors_of_square(target)


def _target_coordinates(lattice, target):
    if element_parent(target) is lattice:

        coefficients = lattice.framing_coefficients(target)
        target = [
            coefficients.get(label, lattice.base_ring().zero())
            for label in lattice.module_generating_set()
        ]
    rationals = lattice.base_ring().fraction_field()
    point = tensor.vector(rationals, target)
    if point.tensor_shape()[0] != int(lattice.module_rank()):
        raise ValueError("a closest-vector target has one coordinate per lattice generator")
    return point


def _closest_vector(lattice, target):
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


def _close_vectors(lattice, target, square_bound):
    r"""Return the lattice vectors within the stated quadratic bound of ``target``.

    The target is a point of ``L tensor QQ`` in the selected lattice frame.
    For a positive-definite lattice this returns the ``x in L`` with
    ``q(x-target) <= square_bound``; for a negative-definite lattice the same
    statement uses the lattice's own negative form, so ``square_bound`` is
    negative and ``q(x-target) >= square_bound``.  The values of the returned
    indexed family are the exact signed squares ``q(x-target)`` in the
    fraction field of the base ring.

    PARI's ``qfcvp`` supplies the finite candidate set for the positive metric
    ``sign*q``.  Because its radius interface passes through a floating bound,
    every candidate is filtered again against the exact rational quadratic
    form before it crosses back into the owned lattice.
    """
    point = _target_coordinates(lattice, target)
    sign, positive_gram = _positive_gram(lattice)
    ring = lattice.base_ring()
    rationals = ring.fraction_field()
    bound = rationals(square_bound)
    positive_bound = rationals(sign) * bound
    if positive_bound < rationals.zero():
        raise ValueError(
            "a close-vector bound has the sign of the definite lattice form"
        )

    engine_gram = _engine_component_matrix(positive_gram)
    engine_point = engine_vector(
        SageQQ,
        tuple(_engine_element(rationals, coordinate) for coordinate in point),
    )
    _count, _largest, raw_coordinates = engine_gram.__pari__().qfcvp(
        engine_point.__pari__().Col(),
        _engine_element(rationals, positive_bound) + SageQQ(1) / 2,
    )
    positive_gram_q = engine_gram.change_ring(SageQQ)
    candidates = {}
    for column in engine_matrix(SageQQ, raw_coordinates).columns():
        displacement = column - engine_point
        positive_square = displacement * positive_gram_q * displacement
        if positive_square > _engine_element(rationals, positive_bound):
            continue
        coordinates = tuple(ring(int(entry)) for entry in column)
        vector = _element_from_coordinates(lattice, coordinates)
        signed_square = rationals._from_engine_element(
            SageQQ(_engine_element(ring, sign)) * positive_square
        )
        candidates[tuple(vector.to_tuple())] = (vector, signed_square)

    vectors = finite_ordered_set(
        tuple(vector for vector, _square in candidates.values())
    )
    by_coordinates = {
        coordinates: square for coordinates, (_vector, square) in candidates.items()
    }
    return finite_indexed_family(
        vectors,
        lambda vector: by_coordinates[tuple(vector.to_tuple())],
        name=f"Vectors of {lattice} close to {point}",
    )


def _babai(lattice, target):
    r"""Return Babai's LLL nearest-plane approximation."""
    point = _target_coordinates(lattice, target)
    rank = int(lattice.module_rank())
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


def _voronoi_region(lattice, bound=None):
    r"""The Voronoi region of ``lattice`` as Sage's exact rational polyhedron.

    Private engine adapter (``OWN-06``) behind :func:`_voronoi_cell`,
    :func:`_voronoi_facets`, :func:`_voronoi_relevant_vectors` and
    :func:`_covering_radius`.  The region is
    ``{x : b(x,v) <= q(v)/2 for every v}`` over the vectors ``v`` of
    positive square at most the bound (PARI ``qfminim``), in the positive
    form of the definite lattice.  With no stated bound the square bound is
    doubled until the region is bounded; the Voronoi cell is then that
    region, since the facets of the cell are cut out by vectors of bounded
    square.
    """
    from sage.geometry.polyhedron.constructor import Polyhedron

    _sign, gram = _positive_gram(lattice)
    rank = gram.tensor_shape()[0]
    rationals = lattice.base_ring().fraction_field()
    if rank == 0:
        return Polyhedron(vertices=[[]], base_ring=SageQQ)
    gram_q = gram.change_ring(rationals)
    engine_gram = _engine_component_matrix(gram)

    def region_from_bound(radius):
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
        return Polyhedron(ieqs=inequalities, base_ring=SageQQ)

    match bound:
        case None:
            pass
        case _:
            return region_from_bound(bound)
    radius = max(int(gram[index, index]) for index in range(rank)) + 1
    for _attempt in range(16):
        region = region_from_bound(radius)
        if region.is_compact():
            return region
        radius *= 2
    raise RuntimeError(
        f"failed to close the Voronoi cell within square bound {radius}"
    )


def _voronoi_cell(lattice, bound=None):
    r"""Return the Voronoi cell of ``lattice``: a convex polytope in ``L tensor QQ``.

    The cell is built by ``ConvexPolytopes()`` on the vertices of the region,
    with ``lattice`` as its ambient coordinate lattice.  Its facets and their
    relevant vectors are :func:`_voronoi_facets`.
    """
    region = _voronoi_region(lattice, bound=bound)
    match int(lattice.module_rank()):
        case 0:
            return ConvexPolytopes()(region.vertices_list())
        case _:
            return ConvexPolytopes()(region.vertices_list(), lattice=lattice)


def _relevant_vector_of_inequality(lattice, inequality):
    r"""The lattice vector ``v`` with ``b(x,v) <= q(v)/2`` equal to one region inequality, or ``None``.

    An inequality ``c + a(x) >= 0`` of the region has ``a = -b(-,v)`` in the
    positive form, so ``v = -G^{-1} a``; it is a lattice vector exactly when
    those coordinates lie in the base ring.
    """
    _sign, gram = _positive_gram(lattice)
    rank = gram.tensor_shape()[0]
    ring = lattice.base_ring()
    rationals = ring.fraction_field()
    dual_gram = gram.change_ring(rationals).dual_tensor()
    coefficients = tuple(
        rationals._from_engine_element(SageQQ(entry)) for entry in inequality.A()
    )
    covector = tensor(rationals, (), (rank,), coefficients)
    vector_coordinates = tuple(-(dual_gram * covector))
    match all(coordinate in ring for coordinate in vector_coordinates):
        case False:
            return None
    return _element_from_coordinates(
        lattice, tuple(ring(coordinate) for coordinate in vector_coordinates)
    )


def _voronoi_relevant_vectors(lattice):
    r"""Return the Voronoi-relevant vectors: the vectors whose inequalities are facets of the cell."""
    relevant = []
    for inequality in _voronoi_region(lattice).inequalities():
        candidate = _relevant_vector_of_inequality(lattice, inequality)
        if candidate is not None and candidate != lattice.zero() and candidate not in relevant:
            relevant.append(candidate)
    return finite_ordered_set(tuple(relevant))


def _voronoi_facets(lattice):
    r"""Return the facets of the Voronoi cell, indexed by their relevant vectors.

    The facet at the relevant vector ``v`` is the convex polytope on which
    ``b(x,v) = q(v)/2``; ``v`` and ``-v`` index opposite facets, and the
    stabilizer of the facet at ``v`` in ``O(L)`` is the point stabilizer of
    ``v``.
    """
    facets = {}
    for face in _voronoi_region(lattice).facets():
        inequalities = tuple(
            inequality
            for inequality in face.ambient_Hrepresentation()
            if inequality.is_inequality()
        )
        if len(inequalities) != 1:
            raise ArithmeticError(
                "a Voronoi facet must have one ambient supporting inequality"
            )
        relevant_vector = _relevant_vector_of_inequality(lattice, inequalities[0])
        if relevant_vector is None or relevant_vector == lattice.zero():
            raise ArithmeticError("a Voronoi facet has a nonzero relevant lattice vector")
        facets[relevant_vector] = ConvexPolytopes()(
            face.as_polyhedron().vertices_list(), lattice=lattice
        )
    return finite_indexed_family(
        finite_ordered_set(tuple(facets)),
        lambda vector: facets[vector],
        name=f"Voronoi facets of {lattice}",
    )


def _successive_minima(lattice):
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


def _gaussian_heuristic(lattice, *, exact_form=False):
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
    rank = int(lattice.module_rank())
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


def _hadamard_ratio(lattice):
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


def _contact_polytope(lattice):
    from sage.geometry.polyhedron.constructor import Polyhedron

    rationals = lattice.base_ring().fraction_field()
    vertices = [
        [
            _engine_element(rationals, rationals(coordinate))
            for coordinate in _coordinate_tuple(lattice, vector)
        ]
        for vector in lattice.shortest_vectors()
    ]
    return ConvexPolytopes()(
        Polyhedron(vertices=vertices, base_ring=SageQQ)
    )


def _coordinate_tuple(lattice, element):

    coefficients = lattice.framing_coefficients(element)
    return tuple(coefficients.get(label, lattice.base_ring().zero()) for label in lattice.module_generating_set())


def _covering_radius(lattice):

    _sign, gram = _positive_gram(lattice)
    rationals = lattice.base_ring().fraction_field()
    gram_q = gram.change_ring(rationals)
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
        for vertex in _voronoi_region(lattice).vertices_list()
    )
    return RR(_engine_element(rationals, squared)).sqrt()


def _center_density(lattice):

    _sign, gram = _positive_gram(lattice)
    rank = int(gram.tensor_shape()[0])
    if rank == 0:
        raise ValueError("the zero lattice has no sphere packing")
    determinant_length = RR(
        _engine_element(lattice.base_ring(), abs(lattice.determinant()))
    ).sqrt()
    return lattice.packing_radius() ** rank / determinant_length


def _packing_density(lattice):
    from sage.functions.gamma import gamma
    from sage.symbolic.constants import pi

    rank = int(lattice.module_rank())
    factor = pi ** (SageQQ(rank) / 2) / gamma(1 + SageQQ(rank) / 2)
    return RR._from_engine_expression(factor) * lattice.center_density()


def _theta_series(lattice, precision=20, variable="q"):

    _sign, positive_gram = _positive_gram(lattice)
    quadratic_form = QuadraticForm(
        SageZZ,
        2 * _engine_component_matrix(positive_gram),
    )
    backend_series = quadratic_form.theta_series(
        int(precision), var_str=variable
    )
    series_ring = lattice.base_ring().power_series_ring(variable)
    engine = _engine_ring(series_ring)
    return series_ring._from_engine_element(engine(backend_series))


def _hermite_invariant(lattice):

    sign, _positive_gram_tensor = _positive_gram(lattice)
    rank = int(lattice.module_rank())
    ring = lattice.base_ring()
    metric_minimum = _engine_element(ring, sign * lattice.minimum())
    determinant = _engine_element(ring, abs(lattice.determinant()))
    from sage.symbolic.ring import SR

    value = SR(metric_minimum) / SR(determinant) ** (SageQQ.one() / rank)
    return RR._from_engine_expression(value)


def _packing_radius(lattice):

    sign = _definite_sign(lattice)
    metric_minimum = sign * lattice.minimum()
    return RR(_engine_element(lattice.base_ring(), metric_minimum)).sqrt() / 2


def _kissing_number(lattice):
    return lattice.base_ring()(len(lattice.shortest_vectors()))


__all__ = [
    "LatticeReduction",
]
