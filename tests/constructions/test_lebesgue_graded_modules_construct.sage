r"""The Hölder-graded direct sum of Lebesgue spaces is a Lebesgue graded module."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_pointwise_lebesgue_algebra_has_the_lebesgue_graded_module_placement() -> None:
    module = GradedLebesgueAlgebra

    assert module in LebesgueGradedModules(RR)
    assert module.graded_piece(QQ(1) / 2) is Lp(2)
    assert module.graded_piece(1) is Lp(1)
    assert module.graded_piece(0) is Lp(oo)
    assert module.integration_of_degree_one().domain() is Lp(1)
