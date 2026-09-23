"""Archive reconciliation for the exterior algebra universal extension."""


from dzack_research.preamble.all import ZZ, Algebras, BilinearMap
from dzack_research.preamble.categories.sets import finite_ordered_set


def _dual_numbers():
    module = ZZ.free_module(finite_ordered_set(("1", "e")))
    one = module.module_generator("1")
    epsilon = module.module_generator("e")
    multiplication = BilinearMap(
        module,
        module,
        module,
        {
            ("1", "1"): one,
            ("1", "e"): epsilon,
            ("e", "1"): epsilon,
            ("e", "e"): module.zero(),
        },
    )
    return Algebras(ZZ)(multiplication)


def test_exterior_universal_map_targets_an_ordinary_algebra() -> None:
    source_module = ZZ.free_module(finite_ordered_set(("x",)))
    target = _dual_numbers()
    epsilon = target.module_generator("e")
    linear = source_module.module_category().Mor(source_module, target)({"x": epsilon})

    extension = linear.alternating_extension()
    exterior = source_module.exterior_algebra()
    x = exterior.algebra_generator("x")

    assert extension.domain() is exterior
    assert extension.codomain() is target
    assert extension(x) == epsilon
    assert extension(x * x) == target.zero()
    assert extension(exterior.one() + 3 * x) == target.one() + 3 * epsilon


