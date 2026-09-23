def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope


def test_evaluation_at_a_point_augments_the_polynomial_algebra() -> None:
    session = _session()
    QQ = session["QQ"]
    Algebras = session["Algebras"]
    AugmentedAlgebras = session["AugmentedAlgebras"]

    polynomials = QQ.free_module(["x"]).symmetric_algebra()
    label = next(iter(polynomials.algebra_generating_set()))
    at_zero = polynomials.Mor(QQ)({label: QQ(0)})
    at_one = polynomials.Mor(QQ)({label: QQ(1)})

    augmented_at_zero = AugmentedAlgebras(QQ)(at_zero)
    augmented_at_one = AugmentedAlgebras(QQ)(at_one)

    assert AugmentedAlgebras(QQ).is_subcategory(Algebras(QQ))
    assert polynomials not in AugmentedAlgebras(QQ)
    assert augmented_at_zero in AugmentedAlgebras(QQ)
    assert augmented_at_one in AugmentedAlgebras(QQ)
    assert augmented_at_zero is not polynomials
    assert augmented_at_zero is not augmented_at_one
    assert augmented_at_zero.unformed_module() is polynomials
    assert augmented_at_one.unformed_module() is polynomials
    assert augmented_at_zero.multiplication() is polynomials.multiplication_morphism()
    assert augmented_at_one.multiplication() is polynomials.multiplication_morphism()
    assert augmented_at_zero.augmentation().domain() is augmented_at_zero
    assert augmented_at_zero.augmentation().codomain() is QQ
    assert augmented_at_zero.augmentation()(
        augmented_at_zero.algebra_generator(label)
    ) == QQ(0)
    assert augmented_at_one.augmentation()(
        augmented_at_one.algebra_generator(label)
    ) == QQ(1)


def test_an_algebra_morphism_to_another_algebra_is_not_an_augmentation() -> None:
    session = _session()
    QQ = session["QQ"]
    AugmentedAlgebras = session["AugmentedAlgebras"]

    source = QQ.free_module(["x"]).symmetric_algebra()
    target = QQ.free_module(["y"]).symmetric_algebra()
    source_label = next(iter(source.algebra_generating_set()))
    target_label = next(iter(target.algebra_generating_set()))
    morphism = source.Mor(target)({source_label: target.algebra_generator(target_label)})

    try:
        AugmentedAlgebras(QQ)(morphism)
    except TypeError as error:
        assert "morphism to" in str(error)
    else:
        raise AssertionError("expected a TypeError")


def test_unframed_algebra_retains_its_selected_augmentation_without_generator_copy() -> None:
    session = _session()
    QQ = session["QQ"]
    Algebras = session["Algebras"]
    AugmentedAlgebras = session["AugmentedAlgebras"]
    GeneralModules = session["GeneralModules"]
    Modules = session["Modules"]
    Set = session["Set"]

    module = GeneralModules(QQ).from_operations(
        Set(QQ),
        addition=lambda left, right: QQ(left + right),
        zero=QQ.zero(),
        negation=lambda value: QQ(-value),
        scalar_action=lambda scalar, value: QQ(scalar * value),
    )
    tensor = Modules(QQ).tensor_product((module, module))
    multiplication = tensor.from_bilinear_map(
        module,
        lambda left, right: module(
            left.underlying_element() * right.underlying_element()
        ),
    )
    algebra = Algebras(QQ).Associative().Unital()(
        module,
        multiplication,
        module(QQ.one()),
    )
    underlying = algebra.module_category().Mor(algebra, QQ).elementwise(
        lambda element: QQ(module(element).underlying_element())
    )
    augmentation = Algebras(QQ).Associative().Unital().Mor(algebra, QQ)(underlying)
    augmented = AugmentedAlgebras(QQ)(augmentation)

    assert augmented.unformed_module() is algebra
    assert augmented.multiplication() is algebra.multiplication_morphism()
    assert augmented.augmentation().domain() is augmented
    assert augmented.augmentation().codomain() is QQ
    assert augmented.augmentation()(augmented(algebra(module(QQ(5))))) == QQ(5)
