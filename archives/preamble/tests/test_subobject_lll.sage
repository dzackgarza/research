r"""LLL reduction, where it is defined: ``DefiniteLattices.Subobjects``.

Reduction rewrites a framing, so its home is a submodule of a definite lattice
together with its inclusion, and the target has to be $I_{n,0}$ or $I_{0,n}$ --
the rows of the inclusion are vectors to compare only when the ambient form is
the standard one.
"""


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject


def _ensure_preamble() -> None:
    # Not ``IntegralLattice``: that name is Sage's own until the preamble
    # rebinds it, so guarding on it would leave the lattices unrefined.
    if "Lattices" in globals():
        return
    from pathlib import Path
    import dzack_research

    from dzack_research.preamble.install import install_preamble
    install_preamble(globals())
def _standard(n: int, negative: bool = False) -> "FormModule":
    r"""Return $I_{n,0}$, or $I_{0,n}$ when ``negative``."""
    gram = matrix(ZZ, n, n, lambda i, j: (0 if i != j else (-1 if negative else 1)))
    return IntegralLattice(gram)


def _skew_submodule(negative: bool = False) -> "Subobject":
    r"""Return a finite-index submodule of $I_{4,0}$ on long, skew generators."""
    _ensure_preamble()
    ambient = _standard(4r, negative)
    e = ambient.module_generators()
    return ambient.subobject_on([
        9 * e[0] + 13 * e[1],
        4 * e[1] + 11 * e[2],
        7 * e[2] + 5 * e[3],
        6 * e[3],
    ])


def test_the_reduced_framing_is_the_one_reduction_defines() -> None:
    r"""The rows come back LLL reduced, so they are the reduced rows."""
    submodule = _skew_submodule()

    original = submodule.embedding().matrix()
    reduced = submodule.LLL().embedding().matrix()

    assert reduced.rows() == original.LLL().rows(), (
        "the inclusion's rows are the LLL reduction of the rows it had"
    )


def test_reduction_keeps_the_submodule_and_shortens_its_generators() -> None:
    r"""A change of framing: the same submodule, on shorter generators."""
    submodule = _skew_submodule()
    reduced = submodule.LLL()

    assert reduced.index() == submodule.index(), (
        "a reduced framing generates the same submodule"
    )
    assert sum(reduced.gram_matrix().diagonal()) < sum(
        submodule.gram_matrix().diagonal()
    ), "the reduced generators are shorter"


def test_reduction_agrees_on_the_negative_definite_target() -> None:
    r"""$S$ and $S(-1)$ have the same short vectors, so the same framing."""
    assert _skew_submodule(negative=True).LLL().gram_matrix() == -(
        _skew_submodule().LLL().gram_matrix()
    ), "the negative definite convention reduces the same way"
