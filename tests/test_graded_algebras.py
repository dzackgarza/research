
def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope


def test_graded_algebras_are_parameterized_by_a_monoid() -> None:
    session = _session()
    QQ = session["QQ"]
    ZZ = session["ZZ"]
    NN = session["NN"]
    Algebras = session["Algebras"]
    GradedAlgebras = session["GradedAlgebras"]
    GradedFreeAlgebras = session["GradedFreeAlgebras"]

    integers = GradedAlgebras(QQ)
    naturals = GradedAlgebras(QQ, NN)

    assert integers is GradedAlgebras(QQ, ZZ)
    assert integers is not naturals
    assert integers.grading_monoid() is ZZ
    assert naturals.grading_monoid() is NN
    assert integers.is_subcategory(Algebras(QQ))
    assert naturals.is_subcategory(Algebras(QQ))
    assert GradedFreeAlgebras(QQ).is_subcategory(integers)
    assert not GradedFreeAlgebras(QQ).is_subcategory(naturals)
    assert GradedAlgebras(QQ, session["NonNegativeReals"]) is not naturals
    assert GradedAlgebras(QQ, session["NonNegativeReals"]).grading_monoid() is session[
        "NonNegativeReals"
    ]


def test_a_graded_free_algebra_is_an_algebra_over_its_unit_graded_piece() -> None:
    session = _session()
    QQ = session["QQ"]
    Algebras = session["Algebras"]
    AugmentedAlgebras = session["AugmentedAlgebras"]
    GradedAlgebras = session["GradedAlgebras"]
    GradedAugmentedAlgebras = session["GradedAugmentedAlgebras"]
    GradedFreeAlgebras = session["GradedFreeAlgebras"]
    SymmetricAlgebraOn = session["SymmetricAlgebraOn"]

    algebra = SymmetricAlgebraOn(QQ, ["x"])
    monoid = algebra.grading_monoid()
    unit_piece = algebra.graded_piece(monoid.monoidal_unit())
    label = next(iter(algebra.algebra_generating_set()))
    inclusion = algebra.algebra_structure_morphism()
    augmentation = algebra.Hom(unit_piece)({label: unit_piece.zero()})

    assert unit_piece is QQ
    assert monoid.monoidal_unit() == monoid.zero()
    assert algebra in Algebras(unit_piece)
    assert inclusion.domain() is unit_piece
    assert inclusion.codomain() is algebra
    assert augmentation.domain() is algebra
    assert augmentation.codomain() is unit_piece
    assert augmentation(inclusion(QQ(4))) == QQ(4)
    assert augmentation(algebra.algebra_generator(label)) == QQ(0)

    combined = AugmentedAlgebras(unit_piece)(augmentation)
    to_ground = combined.ground_ring_augmentation()
    assert combined in AugmentedAlgebras(unit_piece)
    assert combined in GradedAlgebras(QQ)
    assert combined in GradedAugmentedAlgebras(QQ)
    assert combined in GradedFreeAlgebras(QQ)
    assert combined.augmentation()(combined.algebra_generator(label)) == QQ(0)
    assert to_ground.domain() is combined
    assert to_ground.codomain() is unit_piece
    assert to_ground(combined.algebra_generator(label)) == QQ(0)
    assert to_ground(combined(QQ(4))) == QQ(4)


def test_grading_monoid_must_be_a_monoid() -> None:
    session = _session()
    QQ = session["QQ"]
    GradedAlgebras = session["GradedAlgebras"]
    Sets = session["Sets"]

    try:
        GradedAlgebras(QQ, Sets())
    except TypeError as error:
        assert "not a monoid" in str(error)
    else:
        raise AssertionError("expected a TypeError")


def test_graded_algebra_homs_preserve_degree_but_augmentation_remains_ungraded() -> None:
    session = _session()
    QQ = session["QQ"]
    Algebras = session["Algebras"]
    GradedAlgebras = session["GradedAlgebras"]
    GradedAlgebraMorphism = session["GradedAlgebraMorphism"]
    GradedModules = session["GradedModules"]
    SymmetricAlgebraOn = session["SymmetricAlgebraOn"]
    graded_algebra_homset = session["graded_algebra_homset"]

    source = SymmetricAlgebraOn(QQ, ["x"])
    target = SymmetricAlgebraOn(QQ, ["t"])
    x = source.algebra_generator("x")
    t = target.algebra_generator("t")

    ordinary_homset = source.Hom(target)
    assert ordinary_homset is Algebras(QQ).Hom(source, target)
    homset = GradedAlgebras(QQ).Hom(source, target)
    assert homset is graded_algebra_homset(source, target)
    assert Algebras(QQ).Hom(source, target) in homset.super_categories()
    assert GradedModules(QQ).Hom(source, target) in homset.super_categories()
    assert isinstance(homset({"x": t}), GradedAlgebraMorphism)
    graded = homset({"x": t})
    assert isinstance(graded, GradedAlgebraMorphism)
    assert graded(x) == t

    try:
        graded_algebra_homset(source, target)({"x": t**2})
    except ValueError as error:
        assert "preserve degree" in str(error)
    else:
        raise AssertionError("expected a degree-preservation error")

    augmentation = source.Hom(QQ)({"x": QQ.zero()})
    assert not isinstance(augmentation, GradedAlgebraMorphism)
    assert augmentation(x) == QQ.zero()
