from sage.all import SR

from dzack_research.preamble.all import diagonal_gram, Lattices, QuadraticField, Set, ZZ
from dzack_research.preamble.categories.sets import NN, finite_ordered_set
from dzack_research.preamble.tensors import Tensor, tensor


def test_lattice_element_to_vector_is_the_preamble_vector_tensor() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    coordinates = lattice.module_generator(0).to_vector()
    expected = tensor.vector(ZZ, [1, 0])

    assert Tensor in coordinates.__class__.__mro__
    assert coordinates.tensor_valence() == (1, 0)
    assert coordinates.tensor_shape() == (2,)
    assert coordinates == expected


def test_lattice_pairing_is_exactly_gram_tensor_contraction() -> None:
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()
    left = 2 * e + 3 * f
    right = -e + 4 * f

    expected = lattice.gram_tensor().contract(left.to_vector(), right.to_vector())
    assert lattice.b(left, right) == expected
    assert left.b(right) == expected


def test_gram_tensor_contracts_a_lattice_vector_to_its_dual_covector() -> None:
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()
    vector_value = (2 * e + 3 * f).to_vector()
    covector = lattice.gram_tensor() * vector_value

    assert covector.tensor_valence() == (0, 1)
    assert covector.components() == [3, 2]
    assert covector * e.to_vector() == lattice.b(e, 2 * e + 3 * f)
    assert covector * f.to_vector() == lattice.b(f, 2 * e + 3 * f)


def test_a_lattice_is_free_on_formal_symbols_in_sr_by_default() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    generating_set = lattice.module_generating_set()
    e0 = SR.var("e_0")
    e1 = SR.var("e_1")

    assert generating_set.cardinality() == 2
    assert e0 in generating_set
    assert e1 in generating_set
    assert e0 in SR
    assert lattice.module_generator(0) == lattice.module_generator(e0)
    assert lattice.module_generator(e0) * lattice.module_generator(e1) == 0
    assert lattice.module_generator(e0) * lattice.module_generator(e0) == 1
    assert repr(lattice.module_generator(0)) == "e_0"


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

    assert lattice.rank() == lattice.module_generating_set().cardinality()
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
    e, f = plane.module_generator(0), plane.module_generator(1)
    a2 = Lattices(ZZ)("A2")
    a2_from_type = Lattices(ZZ)(["A", 2])
    a2_from_cartan = Lattices(ZZ)(CartanType(["A", 2]))
    euclidean = Lattices(ZZ)(2)

    assert e * e == 0
    assert e * f == 1
    assert a2.module_generator(0) * a2.module_generator(0) == -2
    assert a2.module_generator(0) * a2.module_generator(1) == 1
    assert a2.gram_tensor() == a2_from_type.gram_tensor()
    assert a2.gram_tensor() == a2_from_cartan.gram_tensor()
    assert euclidean.module_generator(0) * euclidean.module_generator(0) == 1
    assert euclidean.module_generator(0) * euclidean.module_generator(1) == 0
    for lattice in (plane, a2, euclidean):
        gram_tensor = lattice.gram_tensor()
        assert gram_tensor.tensor_valence() == (0, 2)
        assert Tensor in gram_tensor.__class__.__mro__
        assert Matrix not in gram_tensor.__class__.__mro__


def test_lattices_over_an_order_do_not_sniff_cartan_type() -> None:
    field = QuadraticField(2, "a")
    order = field.order_generated_by(field.primitive_element())
    lattice = Lattices(order)(order**2)
    even_lattice = lattice.twist(2)
    e, f = lattice.module_generator(0), lattice.module_generator(1)

    assert e * e == 1
    assert e * f == 0
    assert f * f == 1
    assert not lattice.is_even()
    assert even_lattice.is_even()


def test_signature_pair_uses_the_fraction_field() -> None:
    from dzack_research.preamble.all import tensor

    plane = Lattices(ZZ)("U")
    assert plane.signature_pair() == (1, 1)

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
    lattice = category(diagonal_gram(ZZ**NN, {0: -1}))
    e0 = lattice.module_generator(0)
    e1 = lattice.module_generator(1)

    assert e0 * e0 == -1
    assert e1 * e1 == 1
    assert e0 * e1 == 0


def test_twist_rescales_the_form_at_every_rank() -> None:
    from sage.rings.infinity import Infinity

    finite = Lattices(ZZ)(ZZ**2).twist(3)
    e0, e1 = finite.module_generator(0), finite.module_generator(1)
    assert e0 * e0 == 3
    assert e0 * e1 == 0
    assert e1 * e1 == 3

    infinite = Lattices(ZZ)(ZZ**NN).twist(2)
    f0, f1 = infinite.module_generator(0), infinite.module_generator(1)
    f3 = infinite.module_generator(3)
    support = f0 + f3
    assert infinite.rank() == Infinity
    assert f0 * f0 == 2
    assert f0 * f1 == 0
    assert f1 * f1 == 2
    assert support * support == 4

    hyperbolic = Lattices(ZZ)("U").twist(2)
    u0, u1 = hyperbolic.module_generator(0), hyperbolic.module_generator(1)
    assert u0 * u0 == 0
    assert u0 * u1 == 2

    lorentz = Lattices(ZZ)(diagonal_gram(ZZ**NN, {0: -1})).twist(2)
    n0, n1 = lorentz.module_generator(0), lorentz.module_generator(1)
    assert n0 * n0 == -2
    assert n1 * n1 == 2
    assert n0 * n1 == 0


def test_infinite_rank_form_predicates_and_finite_support_operations() -> None:
    from sage.rings.infinity import Infinity

    infinite = Lattices(ZZ)(ZZ**NN)
    e0 = infinite.module_generator(0)
    e3 = infinite.module_generator(3)
    support = e0 + e3

    assert infinite.is_nondegenerate()
    assert infinite.is_unimodular()
    assert not infinite.is_even()
    assert e0.div() == 1
    assert support.div() == 1
    assert e0.is_root()
    assert not (2 * e0 + infinite.module_generator(1)).is_root()
    assert infinite.identity_morphism()(e0) == e0

    doubled = infinite.twist(2)
    assert doubled.rank() == Infinity
    assert doubled.is_even()
    assert not doubled.is_unimodular()
    assert doubled.module_generator(0).div() == 2
    assert not (2 * doubled.module_generator(0) + doubled.module_generator(1)).is_root()

    plane = Lattices(ZZ)("U")
    assert plane.is_even()
    assert plane.is_unimodular()
    u0 = plane.module_generator(0)
    assert u0.div() == 1
    assert plane.reflection(u0 + plane.module_generator(1))(u0) == -plane.module_generator(1)


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

    assert first.gram_tensor() == second.gram_tensor()
    assert first is not second
    assert first is ambient.subobject_on((e0,))
    assert first == first.ambient_module().subobject_on((e0,))
    assert second == second.ambient_module().subobject_on((e1,))
