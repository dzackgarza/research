from sage.all import SR
import pytest

from dzack_research.preamble.all import (
    ZZ,
    Cardinalities,
    Lattices,
    Modules,
    QuadraticField,
    signature_pair,
    signature_pairs,
)
from dzack_research.preamble.categories.sets import NN, finite_ordered_set
from dzack_research.preamble.tensors import Tensor, tensor


def _framing_vector(lattice, element):
    coefficients = lattice.framing_coefficients(element)
    zero = lattice.base_ring().zero()
    return tensor.vector(
        lattice.base_ring(),
        [
            coefficients.get(label, zero)
            for label in lattice.module_generating_set()
        ],
    )


def test_lattice_framing_coordinates_feed_an_owned_vector_tensor() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    element = lattice.basis_vector(0)
    coefficients = lattice.framing_coefficients(element)
    coordinates = _framing_vector(lattice, element)

    assert coefficients == {lattice.module_generating_set()[0]: ZZ.one()}
    assert Tensor in coordinates.__class__.__mro__
    assert coordinates.tensor_valence() == (NN**2)((1, 0))
    _shape = coordinates.tensor_shape()
    assert _shape.cardinality() == 1
    assert _shape[0] == 2
    assert coordinates == tensor.vector(ZZ, [1, 0])


def test_lattice_pairing_is_exactly_gram_tensor_contraction() -> None:
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()
    left = 2 * e + 3 * f
    right = -e + 4 * f

    expected = lattice.gram_tensor().contract(_framing_vector(lattice, left), _framing_vector(lattice, right))
    assert lattice.b(left, right) == expected
    assert left.b(right) == expected


def test_gram_tensor_contracts_a_lattice_vector_to_its_dual_covector() -> None:
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()
    vector_value = _framing_vector(lattice, 2 * e + 3 * f)
    covector = lattice.gram_tensor() * vector_value

    assert covector.tensor_valence() == (NN**2)((0, 1))
    assert covector == tensor.covector(ZZ, [3, 2])
    assert covector * _framing_vector(lattice, e) == lattice.b(e, 2 * e + 3 * f)
    assert covector * _framing_vector(lattice, f) == lattice.b(f, 2 * e + 3 * f)


def test_a_lattice_is_free_on_formal_symbols_in_sr_by_default() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    generating_set = lattice.module_generating_set()
    e0 = SR.var("e_0")
    e1 = SR.var("e_1")

    assert generating_set.cardinality() == 2
    assert e0 in generating_set
    assert e1 in generating_set
    assert e0 in SR
    assert lattice.basis_vector(0) == lattice.module_generator(e0)
    try:
        lattice.module_generator(0)
    except ValueError as error:
        assert "not a framing-generator label" in str(error)
    else:
        raise AssertionError("module_generator must evaluate framing labels, not positions")
    assert lattice.module_generator(e0) == lattice.framing_morphism()(
        lattice.framing_source().module_generator(e0)
    )
    assert lattice.module_generator(e0) * lattice.module_generator(e1) == 0
    assert lattice.module_generator(e0) * lattice.module_generator(e0) == 1
    assert repr(lattice.basis_vector(0)) == "e_0"
    displayed = repr(lattice.module_generators())
    assert displayed.startswith("Module generators: [")
    assert "e_0" in displayed and "e_1" in displayed
    assert "Lattice" not in displayed


def test_a_lattice_may_be_free_on_a_chosen_generating_set() -> None:
    hermite = finite_ordered_set((SR.var("H0"), SR.var("H1"), SR.var("H2")))
    lattice = Lattices(ZZ)(ZZ**3, module_generators=hermite)
    h0 = SR.var("H0")
    h2 = SR.var("H2")

    assert lattice.module_generating_set() == hermite
    assert lattice.module_generator(h0) * lattice.module_generator(h0) == 1
    assert lattice.module_generator(h0) * lattice.module_generator(h2) == 0
    assert repr(lattice.module_generator(h0)) == "H0"
    assert repr(lattice((1, 0, 1))) == "H0 + H2"


def test_the_free_module_on_a_named_index_set_keeps_those_generators() -> None:
    names = finite_ordered_set((SR.var("phi"), SR.var("psi")))
    lattice = Lattices(ZZ)(ZZ**names)

    assert lattice.module_generating_set() == names
    assert repr(lattice.module_generator(SR.var("phi"))) == "phi"


def test_countable_identity_form_is_free_on_formal_symbols() -> None:
    lattice = Lattices(ZZ)(ZZ**NN)
    e0 = SR.var("e_0")
    e3 = SR.var("e_3")

    assert lattice.module_rank() == lattice.module_generating_set().cardinality()
    assert e0 in lattice.module_generating_set()
    assert e3 in lattice.module_generating_set()
    assert repr(lattice({e0: 1, e3: 1})) == "e_0 + e_3"
    assert lattice.module_generator(e0) * lattice.module_generator(e3) == 0


def test_named_hyperbolic_plane_is_free_on_those_symbols() -> None:
    plane = Lattices(ZZ)("U", names=("e", "f"))
    e = SR.var("e")
    f = SR.var("f")

    assert e in plane.module_generating_set()
    assert f in plane.module_generating_set()
    assert plane.module_generator(e) * plane.module_generator(f) == 1
    assert plane.module_generator(e) * plane.module_generator(e) == 0
    assert repr(plane.module_generator(e)) == "e"


def test_named_catalogue_uses_owned_gram_tensors() -> None:
    from sage.combinat.root_system.cartan_type import CartanType
    from sage.structure.element import Matrix

    plane = Lattices(ZZ)("U")
    e, f = plane.basis_vector(0), plane.basis_vector(1)
    a2 = Lattices(ZZ)("A2")
    a2_from_type = Lattices(ZZ)(["A", 2])
    a2_from_cartan = Lattices(ZZ)(CartanType(["A", 2]))
    euclidean = Lattices(ZZ)(2)

    assert e * e == 0
    assert e * f == 1
    assert a2.basis_vector(0) * a2.basis_vector(0) == -2
    assert a2.basis_vector(0) * a2.basis_vector(1) == 1
    assert a2.gram_tensor() == a2_from_type.gram_tensor()
    assert a2.gram_tensor() == a2_from_cartan.gram_tensor()
    assert euclidean.basis_vector(0) * euclidean.basis_vector(0) == 1
    assert euclidean.basis_vector(0) * euclidean.basis_vector(1) == 0
    for lattice in (plane, a2, euclidean):
        gram_tensor = lattice.gram_tensor()
        assert gram_tensor.tensor_valence() == (NN**2)((0, 2))
        assert Tensor in gram_tensor.__class__.__mro__
        assert Matrix not in gram_tensor.__class__.__mro__


def test_lattices_over_an_order_do_not_sniff_cartan_type() -> None:
    field = QuadraticField(2, "a")
    order = field.order_generated_by(field.primitive_element())
    lattice = Lattices(order)(order**2)
    even_lattice = lattice.twist(2)
    e, f = lattice.basis_vector(0), lattice.basis_vector(1)

    assert e * e == 1
    assert e * f == 0
    assert f * f == 1
    assert not lattice.is_even()
    assert even_lattice.is_even()


def test_signature_pair_uses_the_public_cardinal_product_parent() -> None:
    pair = signature_pair(1, 2)

    # ``pair`` is itself an object/Parent of Card x Card; ``category()`` is
    # its mathematical owner.  Sage ``parent()`` on a Parent exposes runtime
    # class infrastructure and is not the categorical parent of an element.
    assert pair.category() is signature_pairs()


def test_signature_pair_uses_the_fraction_field() -> None:
    from dzack_research.preamble.all import tensor

    plane = Lattices(ZZ)("U")
    assert plane.signature_pair() == signature_pair(1, 1)

    field = QuadraticField(2, "a")
    a = field.primitive_element()
    order = field.order_generated_by(a)
    gram = tensor(order, (), (2, 2), [[2, a], [a, 2]])
    lattice = Lattices(order)(gram)
    try:
        lattice.signature_pair()
    except TypeError as error:
        assert "Frac" in str(error)
    else:
        raise AssertionError("a number-field Gram must not report a Q-signature")


def test_lorentz_correction_indexes_the_formal_symbol() -> None:
    category = Lattices(ZZ)
    lattice = category((ZZ**NN).diagonal_gram({0: -1}))
    e0 = lattice.basis_vector(0)
    e1 = lattice.basis_vector(1)

    assert e0 * e0 == -1
    assert e1 * e1 == 1
    assert e0 * e1 == 0


def test_twist_rescales_the_form_at_every_rank() -> None:
    from sage.rings.infinity import Infinity

    finite = Lattices(ZZ)(ZZ**2).twist(3)
    e0, e1 = finite.basis_vector(0), finite.basis_vector(1)
    assert e0 * e0 == 3
    assert e0 * e1 == 0
    assert e1 * e1 == 3

    infinite = Lattices(ZZ)(ZZ**NN).twist(2)
    f0, f1 = infinite.basis_vector(0), infinite.basis_vector(1)
    f3 = infinite.basis_vector(3)
    support = f0 + f3
    assert infinite.module_rank() == Infinity
    assert infinite.module_rank() in Cardinalities()
    assert infinite.module_generating_set().cardinality() in Cardinalities()
    assert f0 * f0 == 2
    assert f0 * f1 == 0
    assert f1 * f1 == 2
    assert support * support == 4

    hyperbolic = Lattices(ZZ)("U").twist(2)
    u0, u1 = hyperbolic.basis_vector(0), hyperbolic.basis_vector(1)
    assert u0 * u0 == 0
    assert u0 * u1 == 2

    lorentz = Lattices(ZZ)((ZZ**NN).diagonal_gram({0: -1})).twist(2)
    n0, n1 = lorentz.basis_vector(0), lorentz.basis_vector(1)
    assert n0 * n0 == -2
    assert n1 * n1 == 2
    assert n0 * n1 == 0


def test_colimit_lattice_constructs_before_undecidable_property_refinement() -> None:
    from sage.rings.infinity import Infinity

    category = Lattices(ZZ)
    colimit = category.colimit(lambda rank: category(ZZ**rank))
    e0 = colimit.basis_vector(0)
    e3 = colimit.basis_vector(3)
    support = e0 + e3

    assert colimit.module_rank() == Infinity
    assert e0 * e0 == 1
    assert e0 * e3 == 0
    assert support * support == 2
    with pytest.raises(AssertionError, match="exact signature"):
        colimit.signature_pair()
    with pytest.raises(AssertionError, match="kernel construction"):
        colimit.is_nondegenerate()
    with pytest.raises(AssertionError, match="kernel construction"):
        colimit.is_unimodular()


def test_infinite_rank_form_predicates_and_finite_support_operations() -> None:
    from sage.rings.infinity import Infinity

    infinite = Lattices(ZZ)(ZZ**NN)
    e0 = infinite.basis_vector(0)
    e3 = infinite.basis_vector(3)
    support = e0 + e3

    assert infinite.is_nondegenerate()
    assert infinite.is_positive_definite()
    assert not infinite.is_negative_definite()
    # The full dual is R^N, not the restricted finite-support dual.
    # Sending every basis vector to 1 is outside the correlation image.
    assert infinite.gram_tensor().is_unimodular() is False
    with pytest.raises(AssertionError, match="cokernel construction"):
        infinite.is_unimodular()
    assert infinite.unformed_module() is ZZ**NN
    assert not infinite.is_even()
    assert e0.div() == 1
    assert support.div() == 1
    assert e0.is_root()
    assert not (2 * e0 + infinite.basis_vector(1)).is_root()
    assert infinite.identity_morphism()(e0) == e0

    doubled = infinite.twist(2)
    assert doubled.module_rank() == Infinity
    assert doubled.is_even()
    assert doubled.gram_tensor().is_unimodular() is False
    with pytest.raises(AssertionError, match="cokernel construction"):
        doubled.is_unimodular()
    assert doubled.basis_vector(0).div() == 2
    assert not (2 * doubled.basis_vector(0) + doubled.basis_vector(1)).is_root()

    plane = Lattices(ZZ)("U")
    assert plane.is_even()
    assert plane.is_unimodular()
    u0 = plane.basis_vector(0)
    assert u0.div() == 1
    assert plane.reflection(u0 + plane.basis_vector(1))(u0) == -plane.basis_vector(1)


def test_a_lattice_is_one_object_per_module_and_gram() -> None:
    from dzack_research.preamble.tensors import tensor

    gram = tensor(ZZ, (), (2, 2), [[0, 1], [1, 0]])

    assert Lattices(ZZ)(gram) is Lattices(ZZ)(gram)
    assert Lattices(ZZ)("U") is Lattices(ZZ)("U")


def test_distinct_sublattices_are_distinct_objects_at_equal_gram() -> None:
    ambient = Lattices(ZZ)(ZZ**2)
    e0, e1 = ambient.module_generators()

    first = ambient.subobject_on((e0,))
    second = ambient.subobject_on((e1,))
    subobjects = Modules(ZZ).Subobjects(ambient)

    assert first.category().is_subcategory(subobjects)
    assert second.category().is_subcategory(subobjects)
    assert subobjects.as_slice_object(first).arrow() is first.inclusion()
    assert subobjects.as_slice_object(second).arrow() is second.inclusion()
    assert first.gram_tensor() == second.gram_tensor()
    assert first is not second
    assert first is ambient.subobject_on((e0,))
    assert first == first.ambient_module().subobject_on((e0,))
    assert second == second.ambient_module().subobject_on((e1,))


def test_colimit_does_not_infer_signature_from_early_stages():
    category = Lattices(ZZ)

    def stage(n):
        module = ZZ.free_module(n)
        return category(module.diagonal_gram({8: -1} if n > 8 else {}))

    lattice = category.colimit(stage)
    with pytest.raises(AssertionError, match="exact signature"):
        lattice.signature_pair()
    assert lattice.basis_vector(8).q() == -1
    assert lattice.basis_vector(0).q() == 1
    assert "rank" in repr(lattice)


def test_lattice_equipping_keeps_the_exact_module_even_with_positional_framing():
    module = ZZ.free_module(3)
    lattice = Lattices(ZZ)(module)
    assert lattice.unformed_module() is module
    assert lattice.module_generating_set() is module.module_generating_set()
