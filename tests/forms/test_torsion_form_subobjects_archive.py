r"""Archive reconciliation for generic finite torsion forms and their subobjects."""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    FractionFieldQuotients,
    TorsionBilinearFormModules,
    TorsionQuadraticFormModules,
)


def _matrix(ring, rows):
    rows = tuple(tuple(row) for row in rows)
    columns = 0 if not rows else len(rows[0])
    return ring.matrix_space(len(rows), columns).from_rows(rows)




def test_archive_bilinear_isotropic_subobjects_retain_form_and_inclusion() -> None:
    values = FractionFieldQuotients(ZZ)(1)
    form = TorsionBilinearFormModules(ZZ).from_relations_and_gram(
        _matrix(ZZ, [[2, 0], [0, 2]]),
        _matrix(QQ, [[0, QQ(1) / 2], [QQ(1) / 2, 0]]),
        values,
    )
    maximal = form.maximal_isotropic_subobjects()

    assert maximal.cardinality() == 3
    for subobject in maximal:
        assert subobject.ambient_module() is form
        assert subobject.cardinality() == 2
        assert form.form_vanishes_on(
            subobject.inclusion()(element) for element in subobject.elements()
        )


def test_archive_quadratic_isotropic_subobjects_are_not_bare_subsets() -> None:
    values = FractionFieldQuotients(ZZ)(2)
    form = TorsionQuadraticFormModules(ZZ).from_relations_and_gram(
        _matrix(ZZ, [[2, 0], [0, 2]]),
        _matrix(QQ, [[0, QQ(1) / 2], [QQ(1) / 2, 0]]),
        values,
    )
    maximal = form.maximal_isotropic_subobjects()

    assert maximal.cardinality() == 2
    for subobject in maximal:
        assert subobject.ambient_module() is form
        assert subobject.cardinality() == 2
        for element in subobject.elements():
            assert subobject.q(element) == subobject.value_module().zero()
