from collections.abc import Callable
from typing import TypeVar

from sage.categories.groups import Groups
from sage.categories.homset import Hom
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.categories.rings import Rings
from sage.categories.sets_cat import Sets
from sage.groups.finitely_presented import (
    FinitelyPresentedGroup,
    FinitelyPresentedGroupElement,
)
from sage.groups.matrix_gps.finitely_generated import (
    FinitelyGeneratedMatrixGroup_generic,
)
from sage.groups.matrix_gps.group_element import MatrixGroupElement_base
from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
from sage.modules.free_module import FreeModule, FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.sets.condition_set import ConditionSet
from sage.sets.image_set import ImageSubobject
from sage.sets.set import Set, Set_object_enumerated
from sage.structure.element import Element
from sage.structure.parent import Parent


_DomainElement = TypeVar("_DomainElement")
_MiddleElement = TypeVar("_MiddleElement")
_CodomainElement = TypeVar("_CodomainElement")


def parent_and_homset_preserve_elements(
    domain: Parent[_DomainElement],
    codomain: Parent[_CodomainElement],
    element: _DomainElement,
) -> None:
    element_parent: Parent[_DomainElement] = domain
    constructed_element: _DomainElement = element_parent(element)
    method_homset = domain.Hom(codomain)
    method_domain: Parent[_DomainElement] = method_homset.domain()
    method_codomain: Parent[_CodomainElement] = method_homset.codomain()
    function_homset = Hom(domain, codomain)
    function_domain: Parent[_DomainElement] = function_homset.domain()
    function_codomain: Parent[_CodomainElement] = function_homset.codomain()
    image: _CodomainElement = function_homset.an_element()(constructed_element)


def morphism_composition_preserves_domain_and_codomain_types(
    left: Morphism[_MiddleElement, _CodomainElement],
    right: Morphism[_DomainElement, _MiddleElement],
    element: _DomainElement,
) -> _CodomainElement:
    composite: Morphism[_DomainElement, _CodomainElement] = left * right
    return composite(element)


def arbitrary_set_members_remain_typed(
    pairs: list[tuple[int, int]],
    predicate: Callable[[tuple[int, int]], bool],
) -> tuple[int, int]:
    finite: Set_object_enumerated[tuple[int, int]] = Set(pairs)
    subset: ConditionSet[tuple[int, int]] = ConditionSet(finite, predicate)
    mathematical_set: Sets.ParentMethods[tuple[int, int]] = subset
    return mathematical_set.an_element()


def image_sets_preserve_map_domain_and_codomain_types(
    defining_map: Map[_DomainElement, _CodomainElement],
    domain: Parent[_DomainElement],
) -> Parent[_CodomainElement] | None:
    image: ImageSubobject[_DomainElement, _CodomainElement] = ImageSubobject(
        defining_map,
        domain,
    )
    return image.ambient()


def concrete_group_parents_preserve_elements(
    permutation_group: PermutationGroup_generic,
    matrix_group: FinitelyGeneratedMatrixGroup_generic,
    presented_group: FinitelyPresentedGroup,
) -> None:
    permutation: PermutationGroupElement = permutation_group.one()
    permutation_parent: PermutationGroup_generic = permutation.parent()
    matrix_element: MatrixGroupElement_base = matrix_group.one()
    matrix_parent: Groups.ParentMethods[MatrixGroupElement_base] = matrix_element.parent()
    presented_element: FinitelyPresentedGroupElement = presented_group.one()
    presented_parent: FinitelyPresentedGroup = presented_element.parent()


def integer_modules_preserve_scalars() -> None:
    module: FreeModule_generic[Integer] = FreeModule(ZZ, 2)
    scalar_ring: Rings.ParentMethods[Integer] = module.base_ring()
    zero: FreeModuleElement[Integer] = module.zero()
    zero_parent: FreeModule_generic[Integer] = zero.parent()
    negation: Morphism[
        FreeModuleElement[Integer],
        FreeModuleElement[Integer],
    ] = module.module_morphism(function=lambda x: -x, codomain=module)
    image: FreeModuleElement[Integer] = negation(zero)
