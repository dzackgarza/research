from dzack_research.preamble.all import FreeModule, Lattices, Modules, QQ, ZZ, module_embedding
from dzack_research.preamble.categories.rational_integral_stabilizers import (
    finite_commensurability_quotient,
)


def _standard_reference():
    line = Lattices(QQ)([[1]])
    restriction = Modules(QQ).restriction_of_scalars(
        ZZ.Mor(QQ)(lambda element: QQ(element))
    )
    space = restriction(line)
    e0 = line.module_generator(0)
    reference = module_embedding(
        FreeModule(ZZ, 1),
        space,
        {0: space.wrap(e0)},
    )
    negation = line.Aut()({0: -e0})
    group = line.Aut()
    return line, space, reference, negation, group


def test_stable_reference_lattice_produces_the_actual_finite_quotient_action() -> None:
    _line, _space, reference, negation, group = _standard_reference()
    quotient_data = finite_commensurability_quotient(group, reference, ZZ(3))
    quotient = quotient_data.quotient_module()
    projection = quotient_data.quotient_projection()

    assert quotient.cardinality() == 3
    assert projection.domain() is reference.domain()
    assert projection.codomain() is quotient
    induced = quotient_data.quotient_automorphism(negation)
    generator = reference.domain().module_generator(0)
    assert induced(projection(generator)) == -projection(generator)
    assert induced(induced(projection(generator))) == projection(generator)
    assert quotient_data.quotient_module() is quotient
    assert quotient_data.quotient_projection() is projection
    action = quotient_data.action_functor()
    assert action.underlying_object() is quotient
    assert action.group() is quotient_data.reference_stabilizer()
    assert negation in quotient_data.reference_stabilizer()
    assert quotient_data.action_functor() is action


def test_intermediate_lattice_maps_to_its_actual_subobject_modulo_dM() -> None:
    line, space, reference, _negation, group = _standard_reference()
    e0 = line.module_generator(0)
    intermediate = module_embedding(
        FreeModule(ZZ, 1),
        space,
        {0: space.wrap(line.scalar_multiple(QQ(2), e0))},
    )
    quotient_data = finite_commensurability_quotient(group, reference, ZZ(4))
    image = quotient_data.intermediate_image(intermediate)

    assert image.inclusion().codomain() is quotient_data.quotient_module()
    assert image.cardinality() == 2


def test_commensurability_modulus_must_be_positive() -> None:
    _line, _space, reference, _negation, group = _standard_reference()
    try:
        finite_commensurability_quotient(group, reference, ZZ(0))
    except ValueError as error:
        assert "positive" in str(error)
    else:
        raise AssertionError("a nonpositive modulus defined M/dM")


def test_only_the_reference_stabilizer_acts_on_the_finite_quotient() -> None:
    plane = Lattices(QQ)("U")
    restriction = Modules(QQ).restriction_of_scalars(
        ZZ.Mor(QQ)(lambda element: QQ(element))
    )
    space = restriction(plane)
    e0, e1 = plane.module_generators()
    reference = module_embedding(
        FreeModule(ZZ, 2),
        space,
        {0: space.wrap(e0), 1: space.wrap(e1)},
    )
    scaling = plane.Aut()(
        {
            0: plane.scalar_multiple(QQ(2), e0),
            1: plane.scalar_multiple(QQ(1) / 2, e1),
        }
    )
    quotient_data = finite_commensurability_quotient(
        plane.Aut(),
        reference,
        ZZ(2),
    )

    assert scaling not in quotient_data.reference_stabilizer()
    try:
        quotient_data.quotient_automorphism(scaling)
    except ValueError as error:
        assert "does not stabilize" in str(error)
    else:
        raise AssertionError("an isometry outside G_M acted on M/dM")
