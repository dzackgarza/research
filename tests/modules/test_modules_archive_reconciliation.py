r"""Archive reconciliation for the base module and vector-space categories."""

from dzack_research.preamble.all import QQ, ZZ, Modules, VectorSpaces

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/pure/modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/pure/modules.py",
    "disposition": "reconciled-live-owner",
}


def test_module_scalar_multiplication_is_evaluation_of_its_scalar_action() -> None:
    module = Modules(ZZ).an_object()
    generator = module.module_generator(0)
    action = module.scalar_action()

    assert action.domain() is ZZ
    assert module.scalar_multiple(ZZ(3), generator) == action(ZZ(3))(generator)


def test_modules_over_a_field_are_objects_of_the_vector_space_category() -> None:
    module = Modules(QQ).an_object()
    vectors = VectorSpaces(QQ)

    assert vectors.is_subcategory(Modules(QQ))
    assert module in Modules(QQ)
    assert module in vectors
