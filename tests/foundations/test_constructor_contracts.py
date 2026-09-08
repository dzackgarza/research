from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.owned_category import construction_contract
from sage.rings.integer_ring import ZZ as SageZZ


def test_module_constructor_contract_discovers_its_base_ring() -> None:
    integers = _own_ring(SageZZ)
    contract = construction_contract(Modules(integers))

    base_parameters = contract.named("base_ring")
    assert base_parameters
    assert any(parameter.required for parameter in base_parameters)
    assert any(
        parameter.provider.__qualname__.endswith("Modules.ParentMethods")
        for parameter in base_parameters
    )
    assert contract.is_open()


def test_algebra_constructor_contract_separates_multiplication_from_module_data() -> None:
    integers = _own_ring(SageZZ)
    contract = construction_contract(Algebras(integers))

    required = contract.required_names()
    assert "multiplication_source_module" in required
    assert "source_multiplication" in required
    assert "algebra_base_ring" in required
    assert "algebra_is_commutative" in required
    assert "base_ring" in required
    assert "source_algebra_unit" in contract.optional_names()


def test_constructor_contract_retains_the_open_cooperative_boundary() -> None:
    integers = _own_ring(SageZZ)
    contract = construction_contract(Algebras(integers))

    providers = {provider.__qualname__ for provider in contract.variadic_providers}
    assert any(name.endswith("Algebras.ParentMethods") for name in providers)
    assert any(name.endswith("Modules.ParentMethods") for name in providers)
    assert contract.opaque_providers == ()
