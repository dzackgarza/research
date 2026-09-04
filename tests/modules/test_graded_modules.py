from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.semirings.non_negative_integer_semiring import NN


def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope


def test_graded_modules_are_parameterized_by_a_monoid() -> None:
    session = _session()
    QQ = session["QQ"]
    ZZ = session["ZZ"]
    Modules = session["Modules"]
    GradedModules = session["GradedModules"]
    GradedAlgebras = session["GradedAlgebras"]
    NonNegativeReals = session["NonNegativeReals"]
    UnitInterval = session["UnitInterval"]

    integers = GradedModules(QQ)
    naturals = GradedModules(QQ, NN)

    assert integers is GradedModules(QQ, ZZ)
    assert integers is GradedModules(QQ, SageZZ)
    assert integers is not naturals
    assert integers.grading_monoid() is SageZZ
    assert naturals.grading_monoid() is NN
    assert integers.is_subcategory(Modules(QQ))
    assert naturals.is_subcategory(Modules(QQ))
    assert GradedAlgebras(QQ).is_subcategory(integers)
    assert GradedAlgebras(QQ, NN).is_subcategory(naturals)
    assert GradedAlgebras(QQ, NonNegativeReals).is_subcategory(
        GradedModules(QQ, NonNegativeReals)
    )
    assert GradedModules(QQ, UnitInterval).grading_monoid() is UnitInterval
    assert GradedModules(QQ, UnitInterval) is not GradedModules(QQ, NonNegativeReals)


def test_grading_monoid_must_be_a_monoid() -> None:
    session = _session()
    QQ = session["QQ"]
    GradedModules = session["GradedModules"]
    Sets = session["Sets"]

    try:
        GradedModules(QQ, Sets())
    except TypeError as error:
        assert "not a monoid" in str(error)
    else:
        raise AssertionError("expected a TypeError")


def test_a_graded_free_algebra_is_a_graded_module() -> None:
    session = _session()
    QQ = session["QQ"]
    GradedModules = session["GradedModules"]
    SymmetricAlgebraOn = session["SymmetricAlgebraOn"]

    algebra = SymmetricAlgebraOn(QQ, ["x"])
    assert algebra in GradedModules(QQ)
    assert algebra.graded_piece(algebra.grading_monoid().monoidal_unit()) is QQ
