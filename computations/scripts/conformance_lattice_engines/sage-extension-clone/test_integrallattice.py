"""Tests for sage.modules.free_quadratic_module_integer_symmetric.IntegralLattice"""

import pytest
from sage.all import vector
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

TEST_TARGET = IntegralLattice


@pytest.mark.timeout(10)
def test_construction_root_lattice_a2():
    """Tests constructor from root lattice A2"""
    lat = IntegralLattice("A2")
    assert lat.rank() == 2


@pytest.mark.timeout(10)
def test_construction_root_lattice_e8():
    """Tests constructor from root lattice E8"""
    lat = IntegralLattice("E8")
    assert lat.rank() == 8


@pytest.mark.timeout(10)
def test_gram_matrix():
    """.gram_matrix() -> Matrix
    
    Inner product matrix of the lattice.
    """
    lat = IntegralLattice("A2")
    g = lat.gram_matrix()
    assert g.nrows() == 2


@pytest.mark.timeout(10)
def test_basis():
    """.basis() -> list[Vector]
    
    Distinguished basis vectors.
    """
    lat = IntegralLattice("A2")
    basis = lat.basis()
    assert len(basis) == 2


@pytest.mark.timeout(10)
def test_rank():
    """.rank() -> Integer
    
    Rank (dimension) of lattice.
    """
    lat = IntegralLattice("E8")
    assert lat.rank() == 8


@pytest.mark.timeout(10)
def test_signature():
    """.signature() -> Integer
    
    Signature = (# positive eigenvalues) - (# negative eigenvalues) of Gram matrix.
    """
    lat = IntegralLattice("A2")
    sig = lat.signature()
    assert sig is not None


@pytest.mark.timeout(10)
def test_is_even():
    """.is_even() -> bool
    
    True if all vector norms are even.
    """
    lat = IntegralLattice("A2")
    result = lat.is_even()
    assert isinstance(result, bool)


@pytest.mark.timeout(10)
def test_dual_lattice():
    """.dual_lattice() -> FreeQuadraticModule
    
    Dual lattice L^∨ = {x ∈ L ⊗ ℚ : (x, l) ∈ ℤ for all l ∈ L}.
    """
    lat = IntegralLattice("A2")
    dual = lat.dual_lattice()
    assert dual is not None


@pytest.mark.timeout(10)
def test_discriminant_group():
    """.discriminant_group(s: int = 0) -> FiniteQuadraticModule
    
    Discriminant group L^∨/L (or s-primary part if s > 0).
    """
    lat = IntegralLattice("A2")
    dg = lat.discriminant_group()
    assert dg is not None


@pytest.mark.timeout(10)
def test_lll():
    """.lll() -> IntegralLattice
    
    Returns LLL-reduced lattice (variant/alias).
    """
    lat = IntegralLattice("A2")
    lll = lat.lll()
    assert lll is not None


@pytest.mark.timeout(10)
def test_minimum():
    """.minimum() -> Rational
    
    Returns minimum nonzero norm in lattice.
    """
    lat = IntegralLattice("A2")
    minimum = lat.minimum()
    assert minimum is not None


@pytest.mark.timeout(10)
def test_maximum():
    """.maximum() -> Integer
    
    Maximum norm: max{x² | x ∈ L \\ {0}}.
    """
    lat = IntegralLattice("A2")
    maximum = lat.maximum()
    assert maximum is not None


@pytest.mark.timeout(10)
def test_short_vectors():
    """.short_vectors(n: Integer) -> list[list[Vector]]
    
    Returns short vectors of length < n. Returns list L where L[k] is vectors of norm k.
    """
    lat = IntegralLattice("A2")
    vecs = lat.short_vectors(5)
    assert len(vecs) > 0


@pytest.mark.timeout(10)
def test_sublattice():
    """.sublattice(basis: list[Vector]) -> IntegralLattice
    
    Sublattice spanned by basis elements.
    """
    lat = IntegralLattice("A2")
    sub = lat.sublattice([vector([1, 0])])
    assert sub.rank() == 1


@pytest.mark.timeout(10)
def test_direct_sum():
    """.direct_sum(M: FreeQuadraticModule) -> IntegralLattice
    
    Direct sum with another lattice.
    """
    l1 = IntegralLattice("A2")
    l2 = IntegralLattice("A2")
    ds = l1.direct_sum(l2)
    assert ds.rank() == 4


@pytest.mark.timeout(10)
def test_twist():
    """.twist(s: int, discard_basis: bool = False) -> IntegralLattice
    
    Lattice with inner product scaled by s.
    """
    lat = IntegralLattice("A2")
    twisted = lat.twist(2)
    assert twisted is not None


@pytest.mark.timeout(10)
def test_automorphisms():
    """.automorphisms(gens: list | None = None, is_finite: bool | None = None) -> MatrixGroup
    
    Requires definite (positive or negative) form. Returns orthogonal group of isometries. For indefinite lattices, pass explicit `gens` parameter or raises NotImplementedError.
    """
    lat = IntegralLattice("A2")
    autos = lat.automorphisms()
    assert autos is not None


@pytest.mark.timeout(10)
def test_orthogonal_group():
    """.orthogonal_group() -> MatrixGroup
    
    Returns group of orthogonal automorphisms.
    """
    lat = IntegralLattice("A2")
    og = lat.orthogonal_group()
    assert og is not None


@pytest.mark.timeout(10)
def test_orthogonal_complement():
    """.orthogonal_complement(M: FreeQuadraticModule) -> FreeQuadraticModule
    
    Returns orthogonal complement of submodule M (for sublattices in ambient space).
    """
    lat = IntegralLattice("A2")
    # orthogonal_complement requires a submodule M as argument
    sub = lat.sublattice([vector([1, 0])])
    oc = lat.orthogonal_complement(sub)
    assert oc is not None


@pytest.mark.timeout(10)
def test_overlattice():
    """.overlattice(gens: list[Vector] | Matrix) -> IntegralLattice
    
    Returns lattice spanned by this lattice and given generators. Result must be integral.
    """
    lat = IntegralLattice("A2")
    # overlattice requires generators that result in an integral lattice
    ol = lat.overlattice(lat.basis_matrix() * 2)
    assert ol is not None


@pytest.mark.timeout(10)
def test_maximal_overlattice():
    """.maximal_overlattice(p: int | None = None) -> IntegralLattice
    
    Maximal even integral overlattice (or p-maximal if p given).
    """
    lat = IntegralLattice("A2")
    mol = lat.maximal_overlattice()
    assert mol is not None


@pytest.mark.timeout(10)
def test_genus():
    """.genus() -> Genus
    
    Returns the genus symbol of the integral lattice.
    """
    lat = IntegralLattice("A2")
    genus = lat.genus()
    assert genus is not None


@pytest.mark.timeout(10)
def test_enumerate_short_vectors():
    """.enumerate_short_vectors() -> Iterator[Vector]
    
    Iterates over all short vectors in the lattice.
    """
    lat = IntegralLattice("A2")
    it = lat.enumerate_short_vectors()
    vecs = [next(it) for _ in range(5)]
    assert len(vecs) == 5


@pytest.mark.timeout(10)
def test_signature_pair():
    """.signature_pair() -> tuple[Integer, Integer]
    
    Signature tuple (n_+, n_-): number of positive and negative eigenvalues.
    """
    lat = IntegralLattice("A2")
    assert lat.signature_pair() == (2, 0)


@pytest.mark.timeout(10)
def test_determinant():
    """.determinant() -> Integer
    
    Determinant of Gram matrix.
    """
    lat = IntegralLattice("A2")
    # A2 det is 3
    assert lat.determinant() == 3


@pytest.mark.timeout(10)
def test_basis_matrix():
    """Tests .basis_matrix()"""
    lat = IntegralLattice("A2")
    m = lat.basis_matrix()
    assert m.nrows() == 2


@pytest.mark.timeout(10)
def test_inner_product_matrix():
    """Tests .inner_product_matrix()"""
    lat = IntegralLattice("A2")
    ipm = lat.inner_product_matrix()
    assert ipm.nrows() == 2


@pytest.mark.timeout(10)
def test_quadratic_form():
    """Tests .quadratic_form()"""
    lat = IntegralLattice("A2")
    q = lat.quadratic_form()
    assert q.dim() == 2


@pytest.mark.timeout(10)
def test_gen():
    """Tests .gen()"""
    lat = IntegralLattice("A2")
    assert lat.gen(0) is not None


@pytest.mark.timeout(10)
def test_gens():
    """Tests .gens()"""
    lat = IntegralLattice("A2")
    assert len(lat.gens()) == 2


@pytest.mark.timeout(10)
def test_ngens():
    """Tests .ngens()"""
    lat = IntegralLattice("A2")
    assert lat.ngens() == 2


@pytest.mark.timeout(10)
def test_coordinates():
    """Tests .coordinates()"""
    lat = IntegralLattice("A2")
    b = lat.basis()
    v = b[0] + b[1]
    c = lat.coordinates(v)
    assert c == [1, 1]


@pytest.mark.timeout(10)
def test_coordinate_vector():
    """Tests .coordinate_vector()"""
    lat = IntegralLattice("A2")
    b = lat.basis()
    v = b[0] + b[1]
    cv = lat.coordinate_vector(v)
    assert list(cv) == [1, 1]


@pytest.mark.timeout(10)
def test_base_ring():
    """Tests .base_ring()"""
    lat = IntegralLattice("A2")
    assert lat.base_ring() == ZZ


@pytest.mark.timeout(10)
def test_dimension():
    """Tests .dimension()"""
    lat = IntegralLattice("A2")
    assert lat.dimension() == 2


@pytest.mark.timeout(10)
def test_is_finite():
    """Tests .is_finite()"""
    lat = IntegralLattice("A2")
    assert not lat.is_finite()


@pytest.mark.timeout(10)
def test_is_exact():
    """Tests .is_exact()"""
    lat = IntegralLattice("A2")
    assert lat.is_exact()


@pytest.mark.timeout(10)
def test_intersection():
    """Tests .intersection()"""
    lat = IntegralLattice("A2")
    assert lat.intersection(lat) == lat


@pytest.mark.timeout(10)
def test_saturation():
    """Tests .saturation()"""
    lat = IntegralLattice("A2")
    sub = lat.sublattice([lat.gen(0)])
    assert sub.saturation() == sub


@pytest.mark.timeout(10)
def test_span():
    """Tests .span()"""
    lat = IntegralLattice("A2")
    s = lat.span([lat.gen(0)])
    assert s.rank() == 1


@pytest.mark.timeout(10)
def test_zero_submodule():
    """Tests .zero_submodule()"""
    lat = IntegralLattice("A2")
    z = lat.zero_submodule()
    assert z.rank() == 0


@pytest.mark.timeout(10)
def test_zero():
    """Tests .zero()"""
    lat = IntegralLattice("A2")
    assert lat.zero() in lat


@pytest.mark.timeout(10)
def test_random_element():
    """Tests .random_element()"""
    lat = IntegralLattice("A2")
    assert lat.random_element() in lat


@pytest.mark.timeout(10)
def test_some_elements():
    """Tests .some_elements()"""
    lat = IntegralLattice("A2")
    assert len(list(lat.some_elements())) > 0


@pytest.mark.timeout(10)
def test_relations():
    """Tests .relations()"""
    lat = IntegralLattice("A2")
    assert lat.relations().rank() == 0


@pytest.mark.timeout(10)
def test_relations_matrix():
    """Tests .relations_matrix()"""
    lat = IntegralLattice("A2")
    assert lat.relations_matrix().nrows() == 0


@pytest.mark.timeout(10)
def test_Hom():
    """Tests .Hom()"""
    lat = IntegralLattice("A2")
    H = lat.Hom(lat)
    assert H is not None


@pytest.mark.timeout(10)
def test_has_coerce_map_from():
    """Tests .has_coerce_map_from()"""
    lat = IntegralLattice("A2")
    sub = lat.sublattice([lat.gen(0)])
    assert lat.has_coerce_map_from(sub)


@pytest.mark.timeout(10)
def test_tensor():
    """Tests .tensor()"""
    lat = IntegralLattice("A2")
    t = lat.tensor(lat)
    assert t is not None


@pytest.mark.timeout(10)
def test_ambient():
    """Tests .ambient()"""
    lat = IntegralLattice("A2")
    assert lat.ambient() is not None


@pytest.mark.timeout(10)
def test_ambient_module():
    """Tests .ambient_module()"""
    lat = IntegralLattice("A2")
    assert lat.ambient_module() is not None


@pytest.mark.timeout(10)
def test_vector_space():
    """Tests .vector_space()"""
    lat = IntegralLattice("A2")
    assert lat.vector_space() is not None


@pytest.mark.timeout(10)
def test_discriminant():
    """Tests .discriminant()"""
    # A2 discriminant is 3
    lat = IntegralLattice("A2")
    assert lat.discriminant() == 3


@pytest.mark.timeout(10)
def test_linear_combination_of_basis():
    """Tests .linear_combination_of_basis()"""
    lat = IntegralLattice("A2")
    v = lat.linear_combination_of_basis([2, 3])
    assert v in lat


@pytest.mark.timeout(10)
def test_CartesianProduct():
    """Tests .CartesianProduct()"""
    assert IntegralLattice.CartesianProduct is not None


@pytest.mark.timeout(10)
def test_Element():
    """Tests .Element()"""
    lat = IntegralLattice("A2")
    assert lat.Element is not None


@pytest.mark.timeout(10)
def test_addition_table():
    """Tests .addition_table()"""
    lat = IntegralLattice("A2")
    lat.addition_table()


@pytest.mark.timeout(10)
def test_algebra():
    """Tests .algebra()"""
    lat = IntegralLattice("A2")
    lat.algebra(ZZ)


@pytest.mark.timeout(10)
def test_LLL():
    """.LLL() -> IntegralLattice
    
    LLL-reduced basis of this lattice.
    """
    lat = IntegralLattice("A2")
    assert lat.LLL() is not None


@pytest.mark.timeout(10)
def test_ambient_vector_space():
    """Tests .ambient_vector_space()"""
    lat = IntegralLattice("A2")
    assert lat.ambient_vector_space() is not None


@pytest.mark.timeout(10)
def test_an_element():
    """Tests .an_element()"""
    lat = IntegralLattice("A2")
    assert lat.an_element() in lat


@pytest.mark.timeout(10)
def test_annihilator():
    """Tests .annihilator()"""
    lat = IntegralLattice("A2")
    assert lat.annihilator(lat.sublattice([lat.gen(0)])) is not None


@pytest.mark.timeout(10)
def test_annihilator_basis():
    """Tests .annihilator_basis()"""
    lat = IntegralLattice("A2")
    lat.annihilator_basis(lat.sublattice([lat.gen(0)]))


@pytest.mark.timeout(10)
def test_are_linearly_dependent():
    """Tests .are_linearly_dependent()"""
    lat = IntegralLattice("A2")
    assert lat.are_linearly_dependent([lat.gen(0), lat.gen(0)]) is True


@pytest.mark.timeout(10)
def test_base():
    """Tests .base()"""
    lat = IntegralLattice("A2")
    assert lat.base() == ZZ


@pytest.mark.timeout(10)
def test_base_extend():
    """Tests .base_extend()"""
    from sage.all import QQ
    lat = IntegralLattice("A2")
    assert lat.base_extend(QQ) is not None


@pytest.mark.timeout(10)
def test_base_field():
    """Tests .base_field()"""
    from sage.all import QQ
    lat = IntegralLattice("A2")
    assert lat.base_field() == QQ


@pytest.mark.timeout(10)
def test_cardinality():
    """Tests .cardinality()"""
    from sage.rings.infinity import Infinity
    lat = IntegralLattice("A2")
    assert lat.cardinality() == Infinity


@pytest.mark.timeout(10)
def test_cartesian_product():
    """Tests .cartesian_product()"""
    lat = IntegralLattice("A2")
    assert lat.cartesian_product(lat) is not None


@pytest.mark.timeout(10)
def test_categories():
    """Tests .categories()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.categories(), list)


@pytest.mark.timeout(10)
def test_category():
    """Tests .category()"""
    lat = IntegralLattice("A2")
    assert lat.category() is not None


@pytest.mark.timeout(10)
def test_change_ring():
    """Tests .change_ring()"""
    from sage.all import QQ
    lat = IntegralLattice("A2")
    assert lat.change_ring(QQ) is not None


@pytest.mark.timeout(10)
def test_codimension():
    """Tests .codimension()"""
    lat = IntegralLattice("A2")
    assert lat.codimension() >= 0


@pytest.mark.timeout(10)
def test_coerce():
    """Tests .coerce()"""
    lat = IntegralLattice("A2")
    v = lat.gen(0)
    assert lat.coerce(v) == v


@pytest.mark.timeout(10)
def test_coerce_embedding():
    """Tests .coerce_embedding()"""
    lat = IntegralLattice("A2")
    lat.coerce_embedding()


@pytest.mark.timeout(10)
def test_coerce_map_from():
    """Tests .coerce_map_from()"""
    lat = IntegralLattice("A2")
    sub = lat.sublattice([lat.gen(0)])
    assert lat.coerce_map_from(sub) is not None


@pytest.mark.timeout(10)
def test_construction():
    """Tests .construction()"""
    lat = IntegralLattice("A2")
    assert lat.construction() is not None


@pytest.mark.timeout(10)
def test_convert_map_from():
    """Tests .convert_map_from()"""
    lat = IntegralLattice("A2")
    assert lat.convert_map_from(ZZ) is not None


@pytest.mark.timeout(10)
def test_coordinate_module():
    """Tests .coordinate_module()"""
    lat = IntegralLattice("A2")
    assert lat.coordinate_module(lat.sublattice([lat.gen(0)])) is not None


@pytest.mark.timeout(10)
def test_coordinate_ring():
    """Tests .coordinate_ring()"""
    lat = IntegralLattice("A2")
    assert lat.coordinate_ring() == ZZ


@pytest.mark.timeout(10)
def test_degree():
    """Tests .degree()"""
    lat = IntegralLattice("A2")
    assert lat.degree() >= 2


@pytest.mark.timeout(10)
def test_denominator():
    """Tests .denominator()"""
    lat = IntegralLattice("A2")
    assert lat.denominator() == 1


@pytest.mark.timeout(10)
def test_dense_module():
    """Tests .dense_module()"""
    lat = IntegralLattice("A2")
    assert lat.dense_module() is not None


@pytest.mark.timeout(10)
def test_echelon_coordinate_vector():
    """Tests .echelon_coordinate_vector()"""
    lat = IntegralLattice("A2")
    v = lat.gen(0)
    assert lat.echelon_coordinate_vector(v) is not None


@pytest.mark.timeout(10)
def test_echelon_coordinates():
    """Tests .echelon_coordinates()"""
    lat = IntegralLattice("A2")
    v = lat.gen(0)
    assert lat.echelon_coordinates(v) is not None


@pytest.mark.timeout(10)
def test_echelon_form():
    """Tests .echelon_form()"""
    lat = IntegralLattice("A2")
    assert lat.echelon_form(lat.basis()) is not None


@pytest.mark.timeout(10)
def test_echelon_to_user_matrix():
    """Tests .echelon_to_user_matrix()"""
    lat = IntegralLattice("A2")
    assert lat.echelon_to_user_matrix() is not None


@pytest.mark.timeout(10)
def test_echelonized_basis():
    """Tests .echelonized_basis()"""
    lat = IntegralLattice("A2")
    assert lat.echelonized_basis() is not None


@pytest.mark.timeout(10)
def test_echelonized_basis_matrix():
    """Tests .echelonized_basis_matrix()"""
    lat = IntegralLattice("A2")
    assert lat.echelonized_basis_matrix() is not None


@pytest.mark.timeout(10)
def test_element_class():
    """Tests .element_class()"""
    lat = IntegralLattice("A2")
    assert lat.element_class is not None


@pytest.mark.timeout(10)
def test_endomorphism_ring():
    """Tests .endomorphism_ring()"""
    lat = IntegralLattice("A2")
    assert lat.endomorphism_ring() is not None


@pytest.mark.timeout(10)
def test_enumerate_close_vectors():
    """.enumerate_close_vectors(target: Vector) -> Iterator[Vector]
    
    Iterates over lattice vectors close to target vector.
    """
    lat = IntegralLattice("A2")
    # This might take time or need specific setup, but checking it exists/callable
    assert hasattr(lat, "enumerate_close_vectors")


@pytest.mark.timeout(10)
def test_free_module():
    """Tests .free_module()"""
    lat = IntegralLattice("A2")
    assert lat.free_module() is not None


@pytest.mark.timeout(10)
def test_free_resolution():
    """Tests .free_resolution()"""
    lat = IntegralLattice("A2")
    lat.free_resolution()


@pytest.mark.timeout(10)
def test_from_vector():
    """Tests .from_vector()"""
    lat = IntegralLattice("A2")
    v = lat.basis_matrix()[0]
    assert lat.from_vector(v) in lat


@pytest.mark.timeout(10)
def test_gens_dict():
    """Tests .gens_dict()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.gens_dict(), dict)


@pytest.mark.timeout(10)
def test_gens_dict_recursive():
    """Tests .gens_dict_recursive()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.gens_dict_recursive(), dict)


@pytest.mark.timeout(10)
def test_get_action():
    """Tests .get_action()"""
    lat = IntegralLattice("A2")
    assert lat.get_action(ZZ) is not None


@pytest.mark.timeout(10)
def test_graded_free_resolution():
    """Tests .graded_free_resolution()"""
    lat = IntegralLattice("A2")
    lat.graded_free_resolution()


@pytest.mark.timeout(10)
def test_has_user_basis():
    """Tests .has_user_basis()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.has_user_basis(), bool)


@pytest.mark.timeout(10)
def test_hom():
    """Tests .hom()"""
    lat = IntegralLattice("A2")
    assert lat.hom([lat.gen(0), lat.gen(1)]) is not None


@pytest.mark.timeout(10)
def test_index_in():
    """Tests .index_in()"""
    lat = IntegralLattice("A2")
    assert lat.index_in(lat) == 1


@pytest.mark.timeout(10)
def test_index_in_saturation():
    """Tests .index_in_saturation()"""
    lat = IntegralLattice("A2")
    assert lat.index_in_saturation() == 1


@pytest.mark.timeout(10)
def test_inject_variables():
    """Tests .inject_variables()"""
    lat = IntegralLattice("A2")
    lat.inject_variables()


@pytest.mark.timeout(10)
def test_invariant_module():
    """Tests .invariant_module()"""
    lat = IntegralLattice("A2")
    lat.invariant_module(lat.sublattice([lat.gen(0)]))


@pytest.mark.timeout(10)
def test_is_ambient():
    """Tests .is_ambient()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.is_ambient(), bool)


@pytest.mark.timeout(10)
def test_is_dense():
    """Tests .is_dense()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.is_dense(), bool)


@pytest.mark.timeout(10)
def test_is_empty():
    """Tests .is_empty()"""
    lat = IntegralLattice("A2")
    assert not lat.is_empty()


@pytest.mark.timeout(10)
def test_is_full():
    """Tests .is_full()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.is_full(), bool)


@pytest.mark.timeout(10)
def test_is_parent_of():
    """Tests .is_parent_of()"""
    lat = IntegralLattice("A2")
    v = lat.gen(0)
    assert lat.is_parent_of(v)


@pytest.mark.timeout(10)
def test_is_primitive():
    """Tests .is_primitive()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.is_primitive(lat.sublattice([lat.gen(0)])), bool)


@pytest.mark.timeout(10)
def test_is_sparse():
    """Tests .is_sparse()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.is_sparse(), bool)


@pytest.mark.timeout(10)
def test_is_submodule():
    """Tests .is_submodule()"""
    lat = IntegralLattice("A2")
    assert lat.is_submodule(lat)


@pytest.mark.timeout(10)
def test_latex_name():
    """Tests .latex_name()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.latex_name(), str)


@pytest.mark.timeout(10)
def test_latex_variable_names():
    """Tests .latex_variable_names()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.latex_variable_names(), list)


@pytest.mark.timeout(10)
def test_lift():
    """Tests .lift()"""
    lat = IntegralLattice("A2")
    v = lat.gen(0)
    assert lat.lift(v) == v


@pytest.mark.timeout(10)
def test_linear_combination():
    """Tests .linear_combination()"""
    lat = IntegralLattice("A2")
    # Checking for existence/callability
    assert hasattr(lat, "linear_combination")


@pytest.mark.timeout(10)
def test_matrix():
    """Tests .matrix()"""
    lat = IntegralLattice("A2")
    assert lat.matrix() is not None


@pytest.mark.timeout(10)
def test_max():
    """.max() -> Rational
    
    Returns maximum norm (for bounded cases).
    """
    lat = IntegralLattice("A2")
    assert lat.max() is not None


@pytest.mark.timeout(10)
def test_min():
    """.min() -> Rational
    
    Returns minimum norm (alias for `minimum()`).
    """
    lat = IntegralLattice("A2")
    assert lat.min() is not None


@pytest.mark.timeout(10)
def test_module_morphism():
    """Tests .module_morphism()"""
    lat = IntegralLattice("A2")
    lat.module_morphism(lat.hom([lat.gen(0), lat.gen(1)]))


@pytest.mark.timeout(10)
def test_monomial():
    """Tests .monomial()"""
    lat = IntegralLattice("A2")
    lat.monomial(0)


@pytest.mark.timeout(10)
def test_monomial_or_zero_if_none():
    """Tests .monomial_or_zero_if_none()"""
    lat = IntegralLattice("A2")
    lat.monomial_or_zero_if_none(0)


@pytest.mark.timeout(10)
def test_nonembedded_free_module():
    """Tests .nonembedded_free_module()"""
    lat = IntegralLattice("A2")
    assert lat.nonembedded_free_module() is not None


@pytest.mark.timeout(10)
def test_objgen():
    """Tests .objgen()"""
    lat = IntegralLattice("A2")
    assert len(lat.objgen()) == 2


@pytest.mark.timeout(10)
def test_objgens():
    """Tests .objgens()"""
    lat = IntegralLattice("A2")
    assert len(lat.objgens()) == 2


@pytest.mark.timeout(10)
def test_parent():
    """Tests .parent()"""
    lat = IntegralLattice("A2")
    assert lat.parent() is not None


@pytest.mark.timeout(10)
def test_pseudoHom():
    """Tests .pseudoHom()"""
    lat = IntegralLattice("A2")
    lat.pseudoHom(lat)


@pytest.mark.timeout(10)
def test_pseudohom():
    """Tests .pseudohom()"""
    lat = IntegralLattice("A2")
    lat.pseudohom(lat)


@pytest.mark.timeout(10)
def test_quotient():
    """Tests .quotient()"""
    lat = IntegralLattice("A2")
    assert lat.quotient(lat.sublattice([lat.gen(0)])) is not None


@pytest.mark.timeout(10)
def test_quotient_module():
    """Tests .quotient_module()"""
    lat = IntegralLattice("A2")
    assert lat.quotient_module(lat.sublattice([lat.gen(0)])) is not None


@pytest.mark.timeout(10)
def test_retract():
    """Tests .retract()"""
    lat = IntegralLattice("A2")
    v = lat.gen(0)
    assert lat.retract(v) == v


@pytest.mark.timeout(10)
def test_scale():
    """Tests .scale()"""
    lat = IntegralLattice("A2")
    assert lat.scale(2) is not None


@pytest.mark.timeout(10)
def test_span_of_basis():
    """Tests .span_of_basis()"""
    lat = IntegralLattice("A2")
    assert lat.span_of_basis([lat.gen(0)]) is not None


@pytest.mark.timeout(10)
def test_sparse_module():
    """Tests .sparse_module()"""
    lat = IntegralLattice("A2")
    assert lat.sparse_module() is not None


@pytest.mark.timeout(10)
def test_submodule():
    """Tests .submodule()"""
    lat = IntegralLattice("A2")
    assert lat.submodule([lat.gen(0)]) is not None


@pytest.mark.timeout(10)
def test_submodule_with_basis():
    """Tests .submodule_with_basis()"""
    lat = IntegralLattice("A2")
    assert lat.submodule_with_basis([lat.gen(0)]) is not None


@pytest.mark.timeout(10)
def test_sum():
    """Tests .sum()"""
    lat = IntegralLattice("A2")
    assert lat.sum([lat.sublattice([lat.gen(0)])]) is not None


@pytest.mark.timeout(10)
def test_sum_of_monomials():
    """Tests .sum_of_monomials()"""
    lat = IntegralLattice("A2")
    lat.sum_of_monomials([lat.gen(0)])


@pytest.mark.timeout(10)
def test_sum_of_terms():
    """Tests .sum_of_terms()"""
    lat = IntegralLattice("A2")
    lat.sum_of_terms([(ZZ(1), 0)])


@pytest.mark.timeout(10)
def test_summation():
    """Tests .summation()"""
    lat = IntegralLattice("A2")
    lat.summation(lat.gen(0), lat.gen(0))


@pytest.mark.timeout(10)
def test_summation_from_element_class_add():
    """Tests .summation_from_element_class_add()"""
    lat = IntegralLattice("A2")
    lat.summation_from_element_class_add(lat.gen(0), lat.gen(0))


@pytest.mark.timeout(10)
def test_tensor_product():
    """.tensor_product(other: IntegralLattice, discard_basis: bool = False) -> IntegralLattice
    
    Tensor product of two lattices.
    """
    lat = IntegralLattice("A2")
    assert lat.tensor_product(lat) is not None


@pytest.mark.timeout(10)
def test_tensor_square():
    """Tests .tensor_square()"""
    lat = IntegralLattice("A2")
    assert lat.tensor_square() is not None


@pytest.mark.timeout(10)
def test_term():
    """Tests .term()"""
    lat = IntegralLattice("A2")
    lat.term(ZZ(1), 0)


@pytest.mark.timeout(10)
def test_twisted_invariant_module():
    """Tests .twisted_invariant_module()"""
    lat = IntegralLattice("A2")
    lat.twisted_invariant_module()


@pytest.mark.timeout(10)
def test_user_to_echelon_matrix():
    """Tests .user_to_echelon_matrix()"""
    lat = IntegralLattice("A2")
    assert lat.user_to_echelon_matrix() is not None


@pytest.mark.timeout(10)
def test_uses_ambient_inner_product():
    """Tests .uses_ambient_inner_product()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.uses_ambient_inner_product(), bool)


@pytest.mark.timeout(10)
def test_variable_name():
    """Tests .variable_name()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.variable_name(), str)


@pytest.mark.timeout(10)
def test_variable_names():
    """Tests .variable_names()"""
    lat = IntegralLattice("A2")
    assert isinstance(lat.variable_names(), tuple)


@pytest.mark.timeout(10)
def test_vector_space_span():
    """Tests .vector_space_span()"""
    lat = IntegralLattice("A2")
    assert lat.vector_space_span(lat.basis()) is not None


@pytest.mark.timeout(10)
def test_vector_space_span_of_basis():
    """Tests .vector_space_span_of_basis()"""
    lat = IntegralLattice("A2")
    assert lat.vector_space_span_of_basis([lat.gen(0)]) is not None


@pytest.mark.timeout(10)
def test_zero_vector():
    """Tests .zero_vector()"""
    lat = IntegralLattice("A2")
    assert lat.zero_vector() == lat.zero()
