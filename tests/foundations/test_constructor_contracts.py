from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import FiniteOrderedSets
from dzack_research.preamble.owned_category import (
    _construction_contract,
    _mor_construction_contract,
)


def test_module_constructor_contract_discovers_its_base_ring() -> None:
    integers = _own_ring(SageZZ)
    contract = _construction_contract(Modules(integers))

    base_parameters = contract.named("base_ring")
    assert base_parameters
    assert any(parameter.required for parameter in base_parameters)
    assert any(
        parameter.provider.__qualname__.endswith("Modules.ParentMethods")
        for parameter in base_parameters
    )
    assert contract.is_open()
    assert contract.has_refinement_hooks()
    assert any(
        provider.__qualname__.endswith("Modules.ParentMethods")
        for provider in contract.hook_providers
    )


def test_algebra_constructor_contract_separates_multiplication_from_module_data() -> None:
    integers = _own_ring(SageZZ)
    contract = _construction_contract(Algebras(integers))

    assert contract.named("unformed_module")
    assert contract.named("multiplication")
    assert contract.named("_engine_product")
    assert "base_ring" in contract.required_names()
    assert not contract.named("multiplication_source_module")
    assert not contract.named("source_multiplication")
    unit_contract = _construction_contract(Algebras(integers).Unital())
    assert unit_contract.named("unit")
    assert unit_contract.named("_engine_unit")


def test_constructor_contract_retains_the_open_cooperative_boundary() -> None:
    integers = _own_ring(SageZZ)
    contract = _construction_contract(Algebras(integers))

    providers = {provider.__qualname__ for provider in contract.variadic_providers}
    assert any(name.endswith("Algebras.ParentMethods") for name in providers)
    assert any(name.endswith("Modules.ParentMethods") for name in providers)
    assert contract.opaque_providers == ()


def test_constructor_contract_retains_adoption_and_refinement_hooks() -> None:
    integers = _own_ring(SageZZ)
    contract = _construction_contract(Algebras(integers))

    hook_names = {provider.__qualname__ for provider in contract.hook_providers}
    assert any(name.endswith("Modules.ParentMethods") for name in hook_names)


def test_mor_constructor_contract_retains_family_and_endpoints() -> None:
    integers = _own_ring(SageZZ)
    modules = Modules(integers)
    module = modules.an_object()
    contract = _mor_construction_contract(modules, module, module)

    required = contract.required_names()
    assert "domain" in required
    assert "codomain" in required
    assert any(name in required for name in ("mor_family", "family"))
    assert contract.owner.domain_object() is module
    assert contract.owner.codomain_object() is module


def test_specialized_constructor_can_derive_general_constructor_data() -> None:
    contract = _construction_contract(FiniteOrderedSets())

    assert contract.named("index_set")
    assert "index_set" in contract.derived_names()
    assert "element_at" in contract.derived_names()
    assert "index_of" in contract.derived_names()
    assert contract.required_names() == frozenset({"elements"})
    contract.validate({"elements": ("a", "b")})
