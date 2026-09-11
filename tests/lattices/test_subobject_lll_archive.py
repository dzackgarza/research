from dzack_research.preamble.all import Lattices, ZZ

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/test_subobject_lll.sage",
    "live_owner": "src/dzack_research/preamble/categories/definite_lattices.py",
    "owner_overrides": {
        "test_the_reduced_framing_is_the_one_reduction_defines": "src/dzack_research/preamble/categories/lattices.py",
        "test_reduction_keeps_the_submodule_and_shortens_its_generators": "src/dzack_research/preamble/categories/lattices.py",
        "test_reduction_agrees_on_the_negative_definite_target": "src/dzack_research/preamble/categories/lattices.py",
    },
    "disposition": "reconciled-live-owner",
}


def _skew_subobject(*, negative=False):
    sign = -1 if negative else 1
    ambient = Lattices(ZZ)(
        [[sign if i == j else 0 for j in range(4)] for i in range(4)]
    )
    e = ambient.module_generators()
    return ambient.subobject_on(
        (
            9 * e[0] + 13 * e[1],
            4 * e[1] + 11 * e[2],
            7 * e[2] + 5 * e[3],
            6 * e[3],
        )
    )


def test_lll_reframes_the_same_lattice_subobject_in_the_same_ambient() -> None:
    subobject = _skew_subobject()
    reduction = subobject.lll_reduction()
    reduced = reduction.reduced

    assert reduced.ambient_lattice() is subobject.ambient_lattice()
    assert reduction.isometry.domain() is reduced
    assert reduction.isometry.codomain() is subobject
    reduced.inclusion().factor_through(subobject.inclusion())
    subobject.inclusion().factor_through(reduced.inclusion())
    assert reduced.index() == subobject.index()


def test_subobject_lll_keeps_the_exact_reduced_ambient_framing() -> None:
    subobject = _skew_subobject()
    reduction = subobject.lll_reduction()
    reduced = reduction.reduced
    old_inclusion = subobject.inclusion()
    reduced_inclusion = reduced.inclusion()

    for generator in reduced.module_generators():
        assert reduced_inclusion(generator) == old_inclusion(
            reduction.isometry(generator)
        )


def test_negative_definite_subobject_uses_the_same_lll_reframing() -> None:
    positive = _skew_subobject()
    negative = _skew_subobject(negative=True)

    assert negative.LLL().gram_matrix() == -positive.LLL().gram_matrix()
