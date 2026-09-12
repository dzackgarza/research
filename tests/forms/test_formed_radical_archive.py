r"""Archive reconciliation for radicals of finite free formed modules."""

from dzack_research.preamble.all import QQ, BilinearForm, FreeModule


def test_radical_is_the_kernel_of_the_correlation_and_keeps_its_inclusion() -> None:
    module = FreeModule(QQ, 2)
    formed = BilinearForm(module, QQ, [[1, 0], [0, 0]])
    first, second = tuple(formed.module_generators())

    radical = formed.radical()
    inclusion = radical.inclusion()

    assert inclusion.codomain() is formed
    assert radical.module_rank() == 1
    assert inclusion(radical.module_generators()[0]) == second
    assert formed.b(inclusion(radical.module_generators()[0]), first) == 0
    assert formed.b(inclusion(radical.module_generators()[0]), second) == 0


def test_radical_quotient_is_the_actual_cokernel_with_the_descended_form() -> None:
    module = FreeModule(QQ, 2)
    formed = BilinearForm(module, QQ, [[1, 0], [0, 0]])
    radical = formed.radical()
    quotient = formed.radical_quotient()
    underlying_quotient = radical.inclusion().cokernel()

    assert quotient.unformed_module() is underlying_quotient
    assert quotient.module_rank() == 1
    generator = quotient.module_generators()[0]
    assert quotient.b(generator, generator) == 1
    assert quotient.is_nondegenerate()


def test_nondegenerate_form_has_zero_radical_and_unchanged_rank_after_quotient() -> None:
    module = FreeModule(QQ, 2)
    formed = BilinearForm(module, QQ, [[0, 1], [1, 0]])

    assert formed.radical().module_rank() == 0
    quotient = formed.radical_quotient()
    assert quotient.module_rank() == 2
    assert quotient.is_nondegenerate()
