from dzack_research.preamble.all import (
    BasedFreeModule,
    FinitelyPresentedAlgebra,
    FinitelyPresentedModule,
    FinitelyPresentedModules,
    InternalHom,
    InternalHomModules,
    Modules,
    ZZ,
    module_homset,
    QQ,
    SymmetricAlgebraOn,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)


def test_module_hom_is_the_internal_hom_module_not_a_second_carrier() -> None:
    source = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    target = BasedFreeModule(ZZ, finite_ordered_set(("f",)))

    categorical_hom = source.Hom(target)
    direct_hom = module_homset(source, target)
    internal_hom = InternalHom(source, target)

    assert categorical_hom is direct_hom
    assert direct_hom is internal_hom
    assert internal_hom in Modules(ZZ)
    assert internal_hom in InternalHomModules(ZZ)
    assert internal_hom in FinitelyPresentedModules(ZZ)

    f = internal_hom({"e": target.module_generator("f")})
    e = source.module_generator("e")
    target_generator = target.module_generator("f")

    assert f.parent() is internal_hom
    assert (f + f)(e) == 2 * target_generator
    assert (2 * f)(e) == 2 * target_generator
    assert (-f)(e) == -target_generator
    assert internal_hom.as_morphism(f) is f
    assert internal_hom.from_morphism(f) is f

    # A finite presentation is extra structure on the same Hom parent, and
    # its selected generators are actual module morphisms.
    generator = next(iter(internal_hom.module_generators()))
    assert generator.parent() is internal_hom
    assert generator(e) == target_generator


def test_module_hom_is_unique_even_when_objects_have_more_structure() -> None:
    algebra = SymmetricAlgebraOn(QQ, ("x",))
    modules = Modules(QQ)

    categorical = modules.Hom(algebra, algebra)
    internal = InternalHom(algebra, algebra)

    assert categorical is internal
    assert categorical is modules.HomCategory().Of(algebra, algebra)
    assert categorical in Modules(QQ)
    assert categorical.base_category() is modules

    identity = categorical.identity()
    x = algebra.algebra_generator("x")
    assert identity(x + 1) == x + 1
    assert (QQ(2) * identity)(x) == 2 * x


def test_general_presented_kernel_uses_polynomial_syzygies_and_has_exact_lift() -> None:
    polynomial = SymmetricAlgebraOn(QQ, ("x", "y"))
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    algebra = FinitelyPresentedAlgebra(polynomial, [x * y])
    xbar = algebra.algebra_generator("x")
    ybar = algebra.algebra_generator("y")

    zero = BasedFreeModule(algebra, finite_ordered_set(()))
    source_free = BasedFreeModule(algebra, finite_ordered_set(("u", "v")))
    target_free = BasedFreeModule(algebra, finite_ordered_set(("w",)))
    source = FinitelyPresentedModule(module_homset(zero, source_free)({}))
    target = FinitelyPresentedModule(module_homset(zero, target_free)({}))
    morphism = module_homset(source, target)(
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
            module_coefficients(inclusion(generator), source).get(label, algebra.zero())
            for label in source_labels
        )
        for generator in kernel.module_generators()
    }

    assert kernel_images == {(algebra.zero(), ybar), (xbar, algebra.zero())}
    assert kernel.presentation_matrix().nrows() == 2
    element = source.linear_combination({"u": xbar, "v": -ybar})
    lifted = inclusion.lift(element)
    assert inclusion(lifted) == element
