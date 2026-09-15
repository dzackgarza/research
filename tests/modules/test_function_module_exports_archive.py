r"""Owner-routed public access to the restored function modules."""

from sage.all import RR

from dzack_research.preamble.categories.modules import FunctionModules


def test_function_module_archive_exports_use_one_owner() -> None:
    owner = FunctionModules(RR)
    smooth = owner.smooth()
    l2 = owner.square_integrable()

    assert smooth in owner
    assert l2 in owner
    assert owner.of("C^infty", "RR") is smooth
    assert owner.of("L^2", "RR") is l2
