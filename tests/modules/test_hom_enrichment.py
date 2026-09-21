from dzack_research.preamble.all import (
    QQ,
    ZZ,
    FinitelyPresentedModules,
    InternalHomModules,
    Modules,
    ProjectiveModules,
)
from dzack_research.preamble.categories.sets import NN, finite_ordered_set


def test_module_hom_is_the_internal_hom_module() -> None:
    source = ZZ.free_module(finite_ordered_set(("e",)))
    target = ZZ.free_module(finite_ordered_set(("f",)))

    categorical_hom = source.Mor(target)
    direct_hom = source.module_category().Mor(source, target)
    internal_hom = source.module_category().Mor(source, target)

    assert categorical_hom is direct_hom
    assert direct_hom is internal_hom
    assert internal_hom in Modules(ZZ)
    assert internal_hom in InternalHomModules(ZZ)
    assert internal_hom in FinitelyPresentedModules(ZZ)
    assert internal_hom in ProjectiveModules(ZZ)
    assert internal_hom.is_projective() is True

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
    algebra = QQ.free_module(("x",)).symmetric_algebra()
    modules = Modules(QQ)

    categorical = modules.Mor(algebra, algebra)
    internal = modules.Mor(algebra, algebra)

    assert categorical is internal
    assert categorical is modules.HomCategory().Of(algebra, algebra)
    assert categorical in Modules(QQ)
    assert categorical.base_category() is modules

    identity = categorical.identity()
    x = algebra.algebra_generator("x")
    assert identity(x + 1) == x + 1
    assert (QQ(2) * identity)(x) == 2 * x


def test_internal_hom_on_infinite_framings_does_not_force_a_finite_model() -> None:
    source = ZZ.free_module(NN)
    target = ZZ.free_module(NN)

    internal = source.module_category().Mor(source, target)

    assert internal is source.module_category().Mor(source, target)
    construction = internal.internal_hom_construction()
    assert construction.source_module() is source
    assert construction.target_module() is target
    assert internal.__dict__.get("_preamble_internal_hom_model") is None

    evaluated = []

    def image(label):
        evaluated.append(label)
        return target.module_generator(label)

    identity = internal(image)
    assert evaluated == []
    e1000 = source.module_generator(NN(1000))
    assert identity(e1000) == target.module_generator(NN(1000))
    assert evaluated == [NN(1000)]


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
    hom = source.module_category().Mor(source, target)
    construction = hom.internal_hom_construction()
    assert construction.source_module() is source
    assert construction.target_module() is target
    assert hom.__dict__.get("_preamble_internal_hom_model") is not None
    framing = hom.framing_morphism()
    assert hom.framing_source() is hom.internal_hom_model().framing_source()
    assert hom.presentation().codomain() is hom.framing_source()
    assert hom.framing_morphism() is framing
    assert framing.domain() is hom.framing_source()
    assert framing.codomain() is hom
    morphism = hom({"x": target.module_generator("y")})

    kernel = morphism.kernel()
    inclusion = kernel.inclusion()
    invariant_factors = kernel.invariant_factors()
    assert invariant_factors.cardinality() == 1
    assert invariant_factors[0] == ZZ(2)

    two_x = source.scalar_multiple(ZZ(2), source.module_generator("x"))
    assert inclusion.has_selected_lift()
    lifted = inclusion.lift(two_x)
    assert inclusion(lifted) == two_x


def test_matrix_internal_hom_retains_its_free_framing_source() -> None:
    source = ZZ.free_module(2)
    target = ZZ.free_module(3)
    hom = source.module_category().Mor(source, target)

    framing = hom.framing_morphism()
    framing_source = hom.framing_source()
    assert framing_source.module_generating_set() is hom.module_generating_set()
    assert hom.framing_morphism() is framing
    assert framing.domain() is framing_source
    assert framing.codomain() is hom
    for label in hom.module_generating_set():
        assert hom.module_generator(label) == framing(
            framing_source.module_generator(label)
        )

    first_label = next(iter(hom.module_generating_set()))
    morphism = hom.module_generator(first_label)
    source_label = next(iter(source.module_generating_set()))
    source_generator = source.module_generator(source_label)
    doubled = hom.scalar_multiple(ZZ(2), morphism)
    assert doubled(source_generator) == target.scalar_multiple(
        ZZ(2), morphism(source_generator)
    )
