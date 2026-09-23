r"""Maps and ideal extensions attached to represented adic completions."""
import pytest

from dzack_research.preamble.all import (
    QQ,
    ArtinianRings,
    CompleteLocalRings,
)
from dzack_research.preamble.categories.algebras.algebras import Algebras




def test_nilpotent_adic_completion_keeps_the_source_but_not_a_truncation_artifact() -> None:
    dual = (QQ.free_module(("e",)).symmetric_algebra()).quotient_by_relations(("e^2",),
    )
    e = dual.algebra_generator("e")
    ideal = dual.ideal(e)
    completion = dual.adic_completion(ideal, precision=3)
    e_hat = completion.completion_map()(e)

    assert ideal.power(2) == dual.ideal(dual.zero())
    assert completion.completion_map_kernel() == dual.ideal(dual.zero())
    assert completion.is_adically_separated()
    assert e_hat != completion.zero()
    assert (e_hat**2).is_zero()


def test_idempotent_adic_completion_is_nonseparated_and_kills_the_stable_ideal() -> None:
    product = (QQ.free_module(("e",)).symmetric_algebra()).quotient_by_relations(("e^2-e",),
    )
    e = product.algebra_generator("e")
    ideal = product.ideal(e)
    completion = product.adic_completion(ideal, precision=3)

    assert ideal.power(2) == ideal
    assert completion.completion_map_kernel() == ideal
    assert not completion.is_adically_separated()
    assert not completion.is_completion_map_injective()
    assert completion.completion_map()(e) == completion.zero()
    assert completion in CompleteLocalRings()
    assert completion.maximal_ideal() == completion.extended_ideal()


def test_nonmaximal_adic_completion_is_complete_but_not_declared_local() -> None:
    plane = QQ.polynomial_ring(("x", "y"))
    x = plane.algebra_generator("x")
    completion = plane.adic_completion(plane.ideal(x))

    assert completion not in CompleteLocalRings()
    with pytest.raises(TypeError, match="not maximal"):
        completion.residue_map()
    assert completion.extended_ideal().ring() is completion




def test_artin_name_requires_finite_length() -> None:
    line = QQ.polynomial_ring(("x",))
    x = line.algebra_generator("x")
    line_completion = line.adic_completion(line.ideal(x))
    assert line_completion.adic_artin_truncation(3) in ArtinianRings()

    plane = QQ.polynomial_ring(("x", "y"))
    x = plane.algebra_generator("x")
    nonmaximal = plane.adic_completion(plane.ideal(x))
    with pytest.raises(ValueError, match="finite length"):
        nonmaximal.adic_artin_truncation(3)




def test_compatible_ring_map_induces_a_continuous_map_of_completions() -> None:
    line = QQ.polynomial_ring(("x",))
    x = line.algebra_generator("x")
    completion = line.adic_completion(line.ideal(x))
    square = Algebras(line.base_ring()).Associative().Unital().Mor(line, line)({"x": x**2})
    induced = completion.induced_map(square, completion)
    identity = completion.induced_map(
        Algebras(line.base_ring()).Associative().Unital().Mor(line, line).identity(),
        completion,
    )
    x_hat = completion.completion_map()(x)

    assert induced.domain() is completion
    assert induced.codomain() is completion
    assert identity.is_identity()
    assert induced(x_hat) == x_hat**2
    assert induced(induced(x_hat)) == x_hat**4

    incompatible = Algebras(line.base_ring()).Associative().Unital().Mor(line, line)({"x": line.one()})
    with pytest.raises(ValueError, match="does not map into"):
        completion.induced_map(incompatible, completion)
