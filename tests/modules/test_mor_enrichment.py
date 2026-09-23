from dzack_research.preamble.all import (
    QQ,
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set








def test_general_presented_kernel_uses_polynomial_syzygies_and_has_exact_lift() -> None:
    polynomial = QQ.free_module(("x", "y")).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    algebra = (polynomial).quotient_by_relations([x * y])
    xbar = algebra.algebra_generator("x")
    ybar = algebra.algebra_generator("y")

    zero = algebra.free_module(finite_ordered_set(()))
    source_free = algebra.free_module(finite_ordered_set(("u", "v")))
    target_free = algebra.free_module(finite_ordered_set(("w",)))
    source = zero.module_category().Mor(zero, source_free)({}).cokernel()
    target = zero.module_category().Mor(zero, target_free)({}).cokernel()
    morphism = source.module_category().Mor(source, target)(
        {
            "u": target.scalar_multiple(ybar, target.module_generator("w")),
            "v": target.scalar_multiple(xbar, target.module_generator("w")),
        }
    )

    kernel = morphism.kernel()
    inclusion = kernel.inclusion()
    source_labels = source.module_generating_set()
    kernel_images = {
        tuple(
            source.framing_coefficients(inclusion(generator)).get(label, algebra.zero())
            for label in source_labels
        )
        for generator in kernel.module_generators()
    }

    assert kernel_images == {(algebra.zero(), ybar), (xbar, algebra.zero())}
    assert kernel.presentation_matrix().nrows() == 2
    element = source.linear_combination({"u": xbar, "v": -ybar})
    assert inclusion.has_selected_lift()
    lifted = inclusion.lift(element)
    assert inclusion(lifted) == element


def test_coordinate_axes_multiplication_kernel_retains_its_nonfree_presentation() -> None:
    polynomial = QQ.free_module(("x", "y")).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    algebra = polynomial.quotient_by_relations([x * y])
    xbar = algebra.algebra_generator("x")
    ybar = algebra.algebra_generator("y")

    zero = algebra.free_module(finite_ordered_set(()))
    free = algebra.free_module(finite_ordered_set(("e",)))
    line = zero.module_category().Mor(zero, free)({}).cokernel()
    generator = line.module_generator("e")
    multiplication_by_x = line.Mor(line)(
        {"e": line.scalar_multiple(xbar, generator)}
    )

    kernel = multiplication_by_x.kernel()
    inclusion = kernel.inclusion()
    assert int(kernel.module_generating_set().cardinality()) == 1
    kernel_label = next(iter(kernel.module_generating_set()))
    kernel_generator = kernel.module_generator(kernel_label)
    image = inclusion(kernel_generator)
    assert line.framing_coefficients(image).get("e", algebra.zero()) == ybar
    assert kernel.scalar_multiple(xbar, kernel_generator) == kernel.zero()
    assert kernel_generator != kernel.zero()

    presentation = kernel.presentation()
    assert int(presentation.domain().module_generating_set().cardinality()) == 1
    relation_label = next(iter(presentation.domain().module_generating_set()))
    relation = presentation(presentation.domain().module_generator(relation_label))
    assert relation != presentation.codomain().zero()
    assert presentation.codomain().framing_coefficients(relation).get(
        kernel_label, algebra.zero()
    ) == xbar

    lifted = inclusion.lift(line.scalar_multiple(ybar, generator))
    assert inclusion(lifted) == line.scalar_multiple(ybar, generator)


def test_presented_pid_kernel_is_an_owned_subobject_with_exact_lift() -> None:
    source_free = ZZ.free_module(finite_ordered_set(("x",)))
    source_relations = ZZ.free_module(finite_ordered_set(("r4",)))
    source = source_relations.module_category().Mor(source_relations, source_free)(
            {"r4": 4 * source_free.module_generator("x")}
        ).cokernel()
    target_free = ZZ.free_module(finite_ordered_set(("y",)))
    target_relations = ZZ.free_module(finite_ordered_set(("r2",)))
    target = target_relations.module_category().Mor(target_relations, target_free)(
            {"r2": 2 * target_free.module_generator("y")}
        ).cokernel()
    mor = source.module_category().Mor(source, target)
    construction = mor.internal_mor_construction()
    assert construction.source_module() is source
    assert construction.target_module() is target
    framing = mor.framing_morphism()
    assert mor.presentation().codomain() is mor.framing_source()
    assert mor.framing_morphism() is framing
    assert framing.domain() is mor.framing_source()
    assert framing.codomain() is mor
    morphism = mor({"x": target.module_generator("y")})

    kernel = morphism.kernel()
    inclusion = kernel.inclusion()
    invariant_factors = kernel.invariant_factors()
    assert invariant_factors.cardinality() == 1
    assert invariant_factors[0] == ZZ(2)

    two_x = source.scalar_multiple(ZZ(2), source.module_generator("x"))
    assert inclusion.has_selected_lift()
    lifted = inclusion.lift(two_x)
    assert inclusion(lifted) == two_x


