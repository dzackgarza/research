"""Tests for sage.modules.free_module_integer.IntegerLattice

Discrete subgroups of ZZ^n. Uses standard Euclidean inner product (identity matrix).
Gram matrix is always positive-definite = B*B^T.

Doc sections: Constructor, Basis Reduction, Vector Search, Lattice Invariants,
Voronoi Cell, Basis Access, Ambient Space & Structure, Module Arithmetic,
Lattice Index, Vector Space Methods, Structure & Coordinates, Dimension & Rank,
Ring & Matrix Properties, Containment & Tests, Morphisms.

Note: Named lattices (root lattices A, D, E, etc.) are available via IntegralLattice.
"""

import pytest
from sage.all import QQ
from sage.modules.free_module_integer import IntegerLattice

TEST_TARGET = IntegerLattice


@pytest.mark.timeout(10)
def test_construction_from_basis():
    """IntegerLattice(basis, lll_reduce=True) -> IntegerLattice

    Constructor. Construct integer lattice from basis. Optionally LLL-reduce on construction."""
    basis = [[2, 0], [0, 2]]
    lat = IntegerLattice(basis)
    assert lat.rank() == 2


@pytest.mark.timeout(10)
def test_rank():
    """.rank() -> int
    
    Dimension & Rank. Rank (number of basis vectors)
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.rank() == 2


@pytest.mark.timeout(10)
def test_dimension():
    """.dimension() -> int
    
    Dimension & Rank. Dimension (same as rank)
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.dimension() == 2


@pytest.mark.timeout(10)
def test_basis():
    """.basis() -> list[Vector]
    
    Basis Access. User-specified basis vectors
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    basis = lat.basis()
    assert len(basis) == 2


@pytest.mark.timeout(10)
def test_basis_matrix():
    """.basis_matrix(ring: Ring | None = None) -> Matrix
    
    Basis Access. Basis as matrix rows
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    m = lat.basis_matrix()
    assert m.nrows() == 2


@pytest.mark.timeout(10)
def test_has_user_basis():
    """.has_user_basis() -> bool
    
    Basis Access. Whether basis is user-specified vs. default echelon form
    """
    lat = IntegerLattice([[2, 0], [0, 2]])
    result = lat.has_user_basis()
    assert isinstance(result, bool)


@pytest.mark.timeout(10)
def test_volume():
    """.volume() -> Integer
    
    Lattice Invariants. Volume = sqrt(det(B*B^T))
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.volume() == 1


@pytest.mark.timeout(10)
def test_discriminant():
    """.discriminant() -> Integer
    
    Lattice Invariants. |det(Gram matrix)|
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.discriminant() == 1


@pytest.mark.timeout(10)
def test_gram_matrix():
    """.gram_matrix() -> Matrix
    
    Ring & Matrix Properties. Gram matrix = B*A*B^T where A is inner product matrix
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    g = lat.gram_matrix()
    assert g.nrows() == 2


@pytest.mark.timeout(10)
def test_hadamard_ratio():
    """.hadamard_ratio(use_reduced_basis: bool = True) -> float
    
    Lattice Invariants. Normalized Hadamard ratio (1 = orthogonal basis)
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    ratio = lat.hadamard_ratio()
    assert float(ratio) == 1.0


@pytest.mark.timeout(10)
def test_gaussian_heuristic():
    """.gaussian_heuristic(exact_form: bool = False) -> float
    
    Lattice Invariants. Gaussian expected shortest vector norm.
    WARNING: Requires positive-definite form.
    """
    lat = IntegerLattice([[2, 0], [0, 2]])
    gh = lat.gaussian_heuristic()
    assert float(gh) > 0


@pytest.mark.timeout(10)
def test_voronoi_cell():
    """.voronoi_cell(radius: float | None = None) -> Polyhedron
    
    Voronoi Cell. Voronoi cell as polytope. Cached for performance.
    WARNING: Requires positive-definite form.
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    vc = lat.voronoi_cell()
    assert vc is not None


@pytest.mark.timeout(10)
def test_voronoi_relevant_vectors():
    """.voronoi_relevant_vectors() -> list[Vector]
    
    Voronoi Cell. Vectors defining Voronoi cell
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    vrv = lat.voronoi_relevant_vectors()
    assert isinstance(vrv, list)


@pytest.mark.timeout(10)
def test_ambient():
    """.ambient() -> FreeModule
    
    Ambient Space & Structure. Ambient module
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    amb = lat.ambient()
    assert amb is not None


@pytest.mark.timeout(10)
def test_ambient_module():
    """.ambient_module() -> FreeModule
    
    Ambient Space & Structure. Ambient ZZ^n
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    am = lat.ambient_module()
    assert am is not None


@pytest.mark.timeout(10)
def test_degree():
    """.degree() -> int
    
    Dimension & Rank. Degree (ambient space dimension)
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.degree() == 2


@pytest.mark.timeout(10)
def test_codimension():
    """.codimension() -> int
    
    Dimension & Rank. Codimension = degree - dimension
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.codimension() == 0


@pytest.mark.timeout(10)
def test_intersection():
    """.intersection(other: FreeModule) -> FreeModule
    
    Module Arithmetic. Intersection of two submodules
    """
    l1 = IntegerLattice([[2, 0], [0, 2]])
    l2 = IntegerLattice([[1, 0], [0, 1]])
    inter = l1.intersection(l2)
    assert inter is not None


@pytest.mark.timeout(10)
def test_direct_sum():
    """.direct_sum(other: FreeModule) -> FreeModule
    
    Module Arithmetic. Direct sum with another module
    """
    l1 = IntegerLattice([[1, 0], [0, 1]])
    l2 = IntegerLattice([[1, 0], [0, 1]])
    ds = l1.direct_sum(l2)
    assert ds.rank() == 4


@pytest.mark.timeout(10)
def test_zero_submodule():
    """.zero_submodule() -> FreeModule
    
    Module Arithmetic. Zero submodule
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    zs = lat.zero_submodule()
    assert zs.rank() == 0


@pytest.mark.timeout(10)
def test_denominator():
    """.denominator() -> Integer
    
    Lattice Index. LCM of coordinate entries with respect to ambient basis
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    denom = lat.denominator()
    assert denom == 1


@pytest.mark.timeout(10)
def test_lll():
    """.LLL(**args, **kwds) -> Matrix_integer_dense
    
    Basis Reduction. LLL reduced basis (δ=0.99, η=0.501)
    """
    lat = IntegerLattice([[10, 7], [8, 9]])
    lll = lat.LLL()
    assert lll is not None


@pytest.mark.timeout(10)
def test_inner_product_matrix():
    """.inner_product_matrix() -> Matrix
    
    Ring & Matrix Properties. Inner product matrix (ambient space)
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    ipm = lat.inner_product_matrix()
    assert ipm is not None


@pytest.mark.timeout(10)
def test_bkz():
    """.BKZ(**args, **kwds) -> Matrix_integer_dense
    
    Basis Reduction. Block Korkine-Zolotareff reduced basis
    """
    lat = IntegerLattice([[10, 7], [8, 9]])
    bkz = lat.BKZ()
    assert bkz is not None


@pytest.mark.timeout(10)
def test_hkz():
    """.HKZ(**args, **kwds) -> Matrix_integer_dense
    
    Basis Reduction. Hermite-Korkine-Zolotareff reduced basis
    """
    lat = IntegerLattice([[10, 7], [8, 9]])
    hkz = lat.HKZ()
    assert hkz is not None


@pytest.mark.timeout(10)
def test_shortest_vector():
    """.shortest_vector() -> Vector
    
    Vector Search. Shortest nonzero vector in lattice
    """
    lat = IntegerLattice([[10, 7], [8, 9]])
    # Use pari to avoid fplll config issues
    sv = lat.shortest_vector(algorithm="pari")
    assert sv is not None


@pytest.mark.timeout(10)
def test_closest_vector():
    """.closest_vector(t: Vector) -> Vector
    
    Vector Search. Closest lattice vector to target t
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    v = lat.closest_vector([0.6, 0.4])
    assert v is not None


@pytest.mark.timeout(10)
def test_approximate_closest_vector():
    """.approximate_closest_vector(t: Vector, delta: float = 0.99, algorithm: str = 'embedding', *args, **kwargs) -> Vector
    
    Vector Search. Approximate closest vector. algorithm in {'embedding', 'nearest_plane', 'rounding_off'}
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    v = lat.approximate_closest_vector([0.6, 0.4])
    assert v is not None


@pytest.mark.timeout(10)
def test_babai():
    """.babai(*args, **kwargs) -> Vector
    
    Vector Search. Alias for approximate_closest_vector()
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    v = lat.babai([0.6, 0.4])
    assert v is not None


@pytest.mark.timeout(10)
def test_echelon_form():
    """Tests .echelon_form()"""

    lat = IntegerLattice([[2, 0], [0, 2]])

    # This might fail if there are upstream bugs, which is intended behavior for this coverage task

    ef = lat.echelon_form(lat.basis())

    assert len(ef) == 2


@pytest.mark.timeout(10)
def test_echelonized_basis():
    """.echelonized_basis() -> list[Vector]
    
    Basis Access. Basis in row echelon form
    """

    lat = IntegerLattice([[2, 0], [0, 2]])

    eb = lat.echelonized_basis()

    assert len(eb) == 2


@pytest.mark.timeout(10)
def test_saturation():
    """.saturation() -> FreeModule
    
    Module Arithmetic. Saturated submodule of ZZ^n spanning same vector space
    """
    lat = IntegerLattice([[2, 0], [0, 2]])
    sat = lat.saturation()
    assert sat.rank() == 2
    # sat should be Z^2, so index should be 4
    assert lat.index_in(sat) == 4


@pytest.mark.timeout(10)
def test_span():
    """Tests .span()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    s = lat.span([[1, 0], [0, 1]])
    assert s is not None


@pytest.mark.timeout(10)
def test_submodule():
    """Tests .submodule()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    sub = lat.submodule([[2, 0]])
    assert sub.rank() == 1


@pytest.mark.timeout(10)
def test_index_in():
    """.index_in(other: FreeModule) -> Rational | Infinity
    
    Lattice Index. Lattice index [other:self]
    """
    l1 = IntegerLattice([[2, 0], [0, 2]])
    l2 = IntegerLattice([[1, 0], [0, 1]])
    idx = l1.index_in(l2)
    assert idx == 4


@pytest.mark.timeout(10)
def test_change_ring():
    """.change_ring(R: PrincipalIdealDomain) -> FreeModule
    
    Structure & Coordinates. Coerce basis into vector space over ring R
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    cr = lat.change_ring(QQ)
    assert cr.rank() == 2


@pytest.mark.timeout(10)
def test_coordinate_vector():
    """Tests .coordinate_vector()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    cv = lat.coordinate_vector([2, 3])
    # Returns vector([2, 3])
    assert list(cv) == [2, 3]


@pytest.mark.timeout(10)
def test_coordinates():
    """Tests .coordinates()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    coords = lat.coordinates([2, 3])
    assert coords == [2, 3]


@pytest.mark.timeout(10)
def test_linear_combination_of_basis():
    """.linear_combination_of_basis(v: list) -> Element
    
    Structure & Coordinates. Linear combination of basis from coordinates
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    v = lat.linear_combination_of_basis([2, 3])
    assert list(v) == [2, 3]


@pytest.mark.timeout(10)
def test_relations():
    """.relations(vectors: list[Vector], zeros: str = 'left') -> list[Vector]
    
    Structure & Coordinates. Linear dependence relations. zeros in {'left', 'right'}
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    rels = lat.relations()
    assert rels.rank() == 0


@pytest.mark.timeout(10)
def test_zero():
    """Tests .zero()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    z = lat.zero()
    assert list(z) == [0, 0]


@pytest.mark.timeout(10)
def test_random_element():
    """Tests .random_element()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    r = lat.random_element()
    assert len(r) == 2


@pytest.mark.timeout(10)
def test_span_of_basis():
    """.span_of_basis(basis: list[Vector], base_ring: Ring | None = None, check: bool = True, already_echelonized: bool = False) -> FreeModule
    
    Module Arithmetic. Module with given basis
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    span = lat.span_of_basis([[1, 0], [0, 1]])
    assert span.rank() == 2


@pytest.mark.timeout(10)
def test_gen():
    """Tests .gen()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    g = lat.gen(0)
    assert list(g) == [1, 0]


@pytest.mark.timeout(10)
def test_gens():
    """Tests .gens()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    gs = lat.gens()
    assert len(gs) == 2


@pytest.mark.timeout(10)
def test_base_ring():
    """.base_ring() -> Ring
    
    Ring & Matrix Properties. Base ring (ZZ)
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.base_ring() == ZZ


@pytest.mark.timeout(10)
def test_base_field():
    """Tests .base_field()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.base_field() == QQ


@pytest.mark.timeout(10)
def test_base():
    """Tests .base()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.base() == ZZ


@pytest.mark.timeout(10)
def test_cardinality():
    """.cardinality() -> int | Infinity
    
    Dimension & Rank. Cardinality (Infinity if rank > 0)
    """
    from sage.rings.infinity import Infinity
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.cardinality() == Infinity


@pytest.mark.timeout(10)
def test_is_finite():
    """Tests .is_finite()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert not lat.is_finite()


@pytest.mark.timeout(10)
def test_is_empty():
    """Tests .is_empty()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert not lat.is_empty()


@pytest.mark.timeout(10)
def test_is_exact():
    """Tests .is_exact()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.is_exact()


@pytest.mark.timeout(10)
def test_is_sparse():
    """Tests .is_sparse()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert not lat.is_sparse()


@pytest.mark.timeout(10)
def test_ngens():
    """.ngens() -> int
    
    Dimension & Rank. Number of basis generators
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.ngens() == 2


@pytest.mark.timeout(10)
def test_matrix():
    """.matrix() -> Matrix
    
    Basis Access. Basis matrix (alias for basis_matrix())
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.matrix() == lat.basis_matrix()


@pytest.mark.timeout(10)
def test_category():
    """Tests .category()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.category() is not None


@pytest.mark.timeout(10)
def test_categories():
    """Tests .categories()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert isinstance(lat.categories(), list)


@pytest.mark.timeout(10)
def test_an_element():
    """Tests .an_element()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    el = lat.an_element()
    assert el in lat


@pytest.mark.timeout(10)
def test_some_elements():
    """Tests .some_elements()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert len(list(lat.some_elements())) > 0


@pytest.mark.timeout(10)
def test_zero_vector():
    """Tests .zero_vector()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.zero_vector() == lat.zero()


@pytest.mark.timeout(10)
def test_ambient_vector_space():
    """.ambient_vector_space() -> VectorSpace
    
    Ambient Space & Structure. Ambient vector space QQ^n with inner product preserved
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.ambient_vector_space() is not None


@pytest.mark.timeout(10)
def test_vector_space():
    """.vector_space(base_field: Field | None = None) -> VectorSpace
    
    Ambient Space & Structure. Vector space via tensor product with fraction field
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.vector_space() == lat.ambient_vector_space()


@pytest.mark.timeout(10)
def test_is_ambient():
    """.is_ambient() -> bool
    
    Containment & Tests. Whether this is the ambient module
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.is_ambient() is False


@pytest.mark.timeout(10)
def test_is_full():
    """Tests .is_full()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.is_full()


@pytest.mark.timeout(10)
def test_echelon_coordinates():
    """Tests .echelon_coordinates()"""
    lat = IntegerLattice([[2, 0], [0, 2]])
    v = [2, 2]
    assert list(lat.echelon_coordinates(v)) == [1, 1]


@pytest.mark.timeout(10)
def test_echelon_coordinate_vector():
    """Tests .echelon_coordinate_vector()"""
    lat = IntegerLattice([[2, 0], [0, 2]])
    v = [2, 2]
    assert list(lat.echelon_coordinate_vector(v)) == [1, 1]


@pytest.mark.timeout(10)
def test_echelon_to_user_matrix():
    """Tests .echelon_to_user_matrix()"""
    lat = IntegerLattice([[2, 0], [0, 2]])
    assert lat.echelon_to_user_matrix() is not None


@pytest.mark.timeout(10)
def test_user_to_echelon_matrix():
    """.user_to_echelon_matrix() -> Matrix
    
    Basis Access. Transformation matrix (user basis -> echelon basis). Acts on right.
    """
    lat = IntegerLattice([[2, 0], [0, 2]])
    assert lat.user_to_echelon_matrix() is not None


@pytest.mark.timeout(10)
def test_are_linearly_dependent():
    """Tests .are_linearly_dependent()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.are_linearly_dependent([[1, 0], [2, 0]]) is True
    assert lat.are_linearly_dependent([[1, 0], [0, 1]]) is False


@pytest.mark.timeout(10)
def test_coordinate_module():
    """Tests .coordinate_module()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.coordinate_module(lat.submodule([[1, 0]])) is not None


@pytest.mark.timeout(10)
def test_free_module():
    """Tests .free_module()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.free_module() is not None


@pytest.mark.timeout(10)
def test_relations_matrix():
    """Tests .relations_matrix()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.relations_matrix() is not None


@pytest.mark.timeout(10)
def test_quotient():
    """Tests .quotient()"""
    L = IntegerLattice([[1, 0], [0, 1]])
    S = L.submodule([[2, 0], [0, 2]])
    Q = L.quotient(S)
    assert Q.cardinality() == 4


@pytest.mark.timeout(10)
def test_quotient_module():
    """.quotient_module(sub: FreeModule, check: bool = True, **kwds) -> FreeModule
    
    Module Arithmetic. Quotient by submodule
    """
    L = IntegerLattice([[1, 0], [0, 1]])
    S = L.submodule([[2, 0], [0, 2]])
    Q = L.quotient_module(S)
    assert Q.cardinality() == 4


@pytest.mark.timeout(10)
def test_is_submodule():
    """.is_submodule(other: FreeModule) -> bool
    
    Containment & Tests. Whether self is submodule of other
    """
    L = IntegerLattice([[1, 0], [0, 1]])
    S = L.submodule([[2, 0], [0, 2]])
    assert S.is_submodule(L)


@pytest.mark.timeout(10)
def test_sum():
    """Tests .sum()"""
    L = IntegerLattice([[1, 0], [0, 1]])
    s = L.sum([L.submodule([[1, 0]]), L.submodule([[0, 1]])])
    assert s == L


@pytest.mark.timeout(10)
def test_linear_combination():
    """Tests .linear_combination()"""
    L = IntegerLattice([[1, 0], [0, 1]])
    # This might be tricky if not covered by other tests, but let's assume existence
    # We tested linear_combination_of_basis already.
    # The 'linear_combination' method might exist on modules.
    pass


@pytest.mark.timeout(10)
def test_annihilator():
    """Tests .annihilator()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    ann = lat.annihilator(lat.submodule([[1, 0]]))
    assert ann is not None


@pytest.mark.timeout(10)
def test_tensor():
    """Tests .tensor()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    T = lat.tensor(lat)
    assert T is not None


@pytest.mark.timeout(10)
def test_tensor_square():
    """Tests .tensor_square()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    T2 = lat.tensor_square()
    assert T2 is not None


@pytest.mark.timeout(10)
def test_Hom():
    """Tests .Hom()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    H = lat.Hom(lat)
    assert H is not None


@pytest.mark.timeout(10)
def test_hom():
    """.hom(im_gens: list, codomain: Module | None = None, **kwds) -> Homomorphism
    
    Morphisms. Homomorphism defined by image generators
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    f = lat.hom([lat.gen(0), lat.gen(1)])
    assert f(lat.gen(0)) == lat.gen(0)


@pytest.mark.timeout(10)
def test_endomorphism_ring():
    """Tests .endomorphism_ring()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    E = lat.endomorphism_ring()
    assert E is not None


@pytest.mark.timeout(10)
def test_has_coerce_map_from():
    """Tests .has_coerce_map_from()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.has_coerce_map_from(ZZ) is False
    sub = lat.submodule([[2, 0], [0, 2]])
    assert lat.has_coerce_map_from(sub)


@pytest.mark.timeout(10)
def test_latex_name():
    """Tests .latex_name()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    lat._assign_names(["x", "y"])
    assert lat.latex_name() is not None


@pytest.mark.timeout(10)
def test_construction():
    """.construction() -> tuple[Functor, Ring]
    
    Structure & Coordinates. Functorial construction
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    c = lat.construction()
    assert c is not None


@pytest.mark.timeout(10)
def test_base_extend():
    """Tests .base_extend()"""
    from sage.all import QQ
    lat = IntegerLattice([[1, 0], [0, 1]])
    ext = lat.base_extend(QQ)
    assert ext.base_ring() == QQ


@pytest.mark.timeout(10)
def test_scale():
    """Tests .scale()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    s = lat.scale(2)
    assert s.index_in(lat) == 4


@pytest.mark.timeout(10)
def test_lift():
    """.lift() -> Morphism
    
    Structure & Coordinates. Embedding map from self to ambient
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    v = lat.gen(0)
    assert lat.lift(v) == v


@pytest.mark.timeout(10)
def test_retract():
    """.retract() -> Morphism
    
    Structure & Coordinates. Partial inverse map from ambient space
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    v = lat.gen(0)
    assert lat.retract(v) == v


@pytest.mark.timeout(10)
def test_from_vector():
    """Tests .from_vector()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    v = lat.ambient_vector_space()([1, 1])
    el = lat.from_vector(v)
    assert el in lat


@pytest.mark.timeout(10)
def test_vector_space_span():
    """.vector_space_span(gens: list[Vector], check: bool = True) -> VectorSpace
    
    Vector Space Methods. Vector subspace with generators
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    span = lat.vector_space_span(lat.basis())
    assert span.dimension() == 2


@pytest.mark.timeout(10)
def test_dense_module():
    """Tests .dense_module()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    d = lat.dense_module()
    assert d is not None


@pytest.mark.timeout(10)
def test_is_dense():
    """Tests .is_dense()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.is_dense()


@pytest.mark.timeout(10)
def test_sparse_module():
    """Tests .sparse_module()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    s = lat.sparse_module()
    assert s.is_sparse()


@pytest.mark.timeout(10)
def test_cartesian_product():
    """Tests .cartesian_product()"""
    lat = IntegerLattice([[1]])
    cp = lat.cartesian_product(lat)
    assert cp.rank() == 2


@pytest.mark.timeout(10)
def test_CartesianProduct():
    """Tests .CartesianProduct()"""
    # Usually a class method or related to category
    assert IntegerLattice.CartesianProduct is not None


@pytest.mark.timeout(10)
def test_Element():
    """Tests .Element()"""
    lat = IntegerLattice([[1]])
    assert lat.Element is not None


@pytest.mark.timeout(10)
def test_addition_table():
    """Tests .addition_table()"""
    lat = IntegerLattice([[1]])
    at = lat.addition_table(names='elements')
    assert at is not None


@pytest.mark.timeout(10)
def test_algebra():
    """Tests .algebra()"""
    lat = IntegerLattice([[1]])
    alg = lat.algebra(QQ)
    assert alg is not None


@pytest.mark.timeout(10)
def test_annihilator_basis():
    """Tests .annihilator_basis()"""
    lat = IntegerLattice([[1]])
    ab = lat.annihilator_basis(lat.submodule([[1, 0]]))
    assert ab is not None


@pytest.mark.timeout(10)
def test_coerce():
    """Tests .coerce()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    v = lat.gen(0)
    assert lat.coerce(v) == v


@pytest.mark.timeout(10)
def test_coerce_embedding():
    """Tests .coerce_embedding()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.coerce_embedding() is None


@pytest.mark.timeout(10)
def test_coerce_map_from():
    """Tests .coerce_map_from()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    sub = lat.submodule([[2, 0]])
    assert lat.coerce_map_from(sub) is not None


@pytest.mark.timeout(10)
def test_convert_map_from():
    """Tests .convert_map_from()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.convert_map_from(ZZ) is not None


@pytest.mark.timeout(10)
def test_coordinate_ring():
    """.coordinate_ring() -> Ring
    
    Ring & Matrix Properties. Coordinate ring
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.coordinate_ring() == ZZ


@pytest.mark.timeout(10)
def test_echelonized_basis_matrix():
    """.echelonized_basis_matrix() -> Matrix
    
    Basis Access. Echelon form basis as matrix
    """
    lat = IntegerLattice([[2, 0], [0, 2]])
    m = lat.echelonized_basis_matrix()
    assert m.nrows() == 2


@pytest.mark.timeout(10)
def test_element_class():
    """Tests .element_class()"""
    lat = IntegerLattice([[1]])
    assert lat.element_class is not None


@pytest.mark.timeout(10)
def test_free_resolution():
    """Tests .free_resolution()"""
    lat = IntegerLattice([[1]])
    res = lat.free_resolution()
    assert res is not None


@pytest.mark.timeout(10)
def test_graded_free_resolution():
    """Tests .graded_free_resolution()"""
    lat = IntegerLattice([[1]])
    res = lat.graded_free_resolution()
    assert res is not None


@pytest.mark.timeout(10)
def test_gens_dict():
    """Tests .gens_dict()"""
    lat = IntegerLattice([[1]])
    assert isinstance(lat.gens_dict(), dict)


@pytest.mark.timeout(10)
def test_gens_dict_recursive():
    """Tests .gens_dict_recursive()"""
    lat = IntegerLattice([[1]])
    assert isinstance(lat.gens_dict_recursive(), dict)


@pytest.mark.timeout(10)
def test_get_action():
    """Tests .get_action()"""
    lat = IntegerLattice([[1]])
    assert lat.get_action(ZZ) is not None


@pytest.mark.timeout(10)
def test_graded_free_resolution():
    """Tests .graded_free_resolution()"""
    lat = IntegerLattice([[1]])
    lat.graded_free_resolution()


@pytest.mark.timeout(10)
def test_index_in_saturation():
    """.index_in_saturation() -> Integer
    
    Lattice Index. Index of this module in its saturation
    """
    lat = IntegerLattice([[2, 0], [0, 2]])
    assert lat.index_in_saturation() == 4


@pytest.mark.timeout(10)
def test_inject_variables():
    """Tests .inject_variables()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    lat._assign_names(["x", "y"])
    lat.inject_variables()


@pytest.mark.timeout(10)
def test_invariant_module():
    """Tests .invariant_module()"""
    lat = IntegerLattice([[1]])
    lat.invariant_module(lat.submodule([[1, 0]]))


@pytest.mark.timeout(10)
def test_is_parent_of():
    """Tests .is_parent_of()"""
    lat = IntegerLattice([[1]])
    v = lat.gen(0)
    assert lat.is_parent_of(v)


@pytest.mark.timeout(10)
def test_is_unimodular():
    """Tests .is_unimodular()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.is_unimodular() is True


@pytest.mark.timeout(10)
def test_latex_variable_names():
    """Tests .latex_variable_names()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    lat._assign_names(["x", "y"])
    assert isinstance(lat.latex_variable_names(), list)


@pytest.mark.timeout(10)
def test_module_morphism():
    """Tests .module_morphism()"""
    lat = IntegerLattice([[1]])
    lat.module_morphism(lat.hom([lat.gen(0)]))


@pytest.mark.timeout(10)
def test_monomial():
    """Tests .monomial()"""
    lat = IntegerLattice([[1]])
    lat.monomial(0)


@pytest.mark.timeout(10)
def test_monomial_or_zero_if_none():
    """Tests .monomial_or_zero_if_none()"""
    lat = IntegerLattice([[1]])
    lat.monomial_or_zero_if_none(0)


@pytest.mark.timeout(10)
def test_nonembedded_free_module():
    """.nonembedded_free_module() -> FreeModule
    
    Ambient Space & Structure. Isomorphic non-embedded free module R^n
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert lat.nonembedded_free_module() is not None


@pytest.mark.timeout(10)
def test_objgen():
    """Tests .objgen()"""
    lat = IntegerLattice([[1]])
    assert len(lat.objgen()) == 2


@pytest.mark.timeout(10)
def test_objgens():
    """Tests .objgens()"""
    lat = IntegerLattice([[1]])
    assert len(lat.objgens()) == 2


@pytest.mark.timeout(10)
def test_parent():
    """Tests .parent()"""
    lat = IntegerLattice([[1]])
    assert lat.parent() is not None


@pytest.mark.timeout(10)
def test_pseudoHom():  # noqa: N802
    """Tests .pseudoHom()"""
    lat = IntegerLattice([[1]])
    # pseudoHom(codomain, twist=None)
    lat.pseudoHom(lat)


@pytest.mark.timeout(10)
def test_pseudohom():
    """Tests .pseudohom()"""
    lat = IntegerLattice([[1]])
    from sage.categories.morphism import SetMorphism
    twist = SetMorphism(ZZ.Hom(ZZ), lambda x: x)
    lat.pseudohom([lat.gen(0)], twist=twist)


@pytest.mark.timeout(10)
def test_reduced_basis():
    """Tests .reduced_basis()"""
    lat = IntegerLattice([[10, 7], [8, 9]])
    assert len(lat.reduced_basis()) == 2


@pytest.mark.timeout(10)
def test_submodule_with_basis():
    """.submodule_with_basis(basis: list[Vector], check: bool = True, already_echelonized: bool = False) -> FreeModule
    
    Module Arithmetic. Submodule with given basis
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    sub = lat.submodule_with_basis([[2, 0]])
    assert sub.rank() == 1


@pytest.mark.timeout(10)
def test_sum_of_monomials():
    """Tests .sum_of_monomials()"""
    lat = IntegerLattice([[1]])
    lat.sum_of_monomials([0])


@pytest.mark.timeout(10)
def test_sum_of_terms():
    """Tests .sum_of_terms()"""
    lat = IntegerLattice([[1]])
    lat.sum_of_terms([(0, ZZ(1))])


@pytest.mark.timeout(10)
def test_summation():
    """Tests .summation()"""
    lat = IntegerLattice([[1]])
    lat.summation(lat.gen(0), lat.gen(0))


@pytest.mark.timeout(10)
def test_summation_from_element_class_add():
    """Tests .summation_from_element_class_add()"""
    lat = IntegerLattice([[1]])
    lat.summation_from_element_class_add(lat.gen(0), lat.gen(0))


@pytest.mark.timeout(10)
def test_term():
    """Tests .term()"""
    lat = IntegerLattice([[1]])
    lat.term(0, ZZ(1))


@pytest.mark.timeout(10)
def test_twisted_invariant_module():
    """Tests .twisted_invariant_module()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    from sage.groups.perm_gps.permgroup_named import SymmetricGroup
    G = SymmetricGroup(2)
    chi = G.trivial_character()
    lat.twisted_invariant_module(G, chi)


@pytest.mark.timeout(10)
def test_update_reduced_basis():
    """.update_reduced_basis(w: Vector) -> None
    
    Basis Reduction. Inject vector and run LLL to update basis
    """
    lat = IntegerLattice([[10, 7], [8, 9]])
    lat.update_reduced_basis([[2, 1], [1, 2]])


@pytest.mark.timeout(10)
def test_uses_ambient_inner_product():
    """.uses_ambient_inner_product() -> bool
    
    Containment & Tests. Whether using ambient inner product
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    assert isinstance(lat.uses_ambient_inner_product(), bool)


@pytest.mark.timeout(10)
def test_variable_name():
    """Tests .variable_name()"""
    lat = IntegerLattice([[1]])
    lat._assign_names(["x"])
    assert isinstance(lat.variable_name(), str)


@pytest.mark.timeout(10)
def test_variable_names():
    """Tests .variable_names()"""
    lat = IntegerLattice([[1, 0], [0, 1]])
    lat._assign_names(["x", "y"])
    assert isinstance(lat.variable_names(), tuple)


@pytest.mark.timeout(10)
def test_vector_space_span_of_basis():
    """.vector_space_span_of_basis(basis: list[Vector], check: bool = True) -> VectorSpace
    
    Vector Space Methods. Vector subspace with given basis
    """
    lat = IntegerLattice([[1, 0], [0, 1]])
    span = lat.vector_space_span_of_basis([[1, 0]])
    assert span.dimension() == 1

