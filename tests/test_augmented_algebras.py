def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope


def test_evaluation_at_a_point_augments_the_polynomial_algebra() -> None:
    session = _session()
    QQ = session["QQ"]
    Algebras = session["Algebras"]
    AugmentedAlgebras = session["AugmentedAlgebras"]
    SymmetricAlgebraOn = session["SymmetricAlgebraOn"]

    polynomials = SymmetricAlgebraOn(QQ, ["x"])
    label = next(iter(polynomials.algebra_generating_set()))
    at_zero = polynomials.Hom(QQ)({label: QQ(0)})
    at_one = polynomials.Hom(QQ)({label: QQ(1)})

    augmented_at_zero = AugmentedAlgebras(QQ)(at_zero)
    augmented_at_one = AugmentedAlgebras(QQ)(at_one)

    assert AugmentedAlgebras(QQ).is_subcategory(Algebras(QQ))
    assert polynomials not in AugmentedAlgebras(QQ)
    assert augmented_at_zero in AugmentedAlgebras(QQ)
    assert augmented_at_one in AugmentedAlgebras(QQ)
    assert augmented_at_zero is not polynomials
    assert augmented_at_zero is not augmented_at_one
    assert augmented_at_zero is AugmentedAlgebras(QQ)(
        polynomials.Hom(QQ)({label: QQ(0)})
    )
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
    SymmetricAlgebraOn = session["SymmetricAlgebraOn"]

    source = SymmetricAlgebraOn(QQ, ["x"])
    target = SymmetricAlgebraOn(QQ, ["y"])
    source_label = next(iter(source.algebra_generating_set()))
    target_label = next(iter(target.algebra_generating_set()))
    morphism = source.Hom(target)({source_label: target.algebra_generator(target_label)})

    try:
        AugmentedAlgebras(QQ)(morphism)
    except TypeError as error:
        assert "morphism to" in str(error)
    else:
        raise AssertionError("expected a TypeError")
