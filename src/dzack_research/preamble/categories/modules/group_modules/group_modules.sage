r"""Finite-group representations on finitely generated free modules."""

from typing import Any

from sage.categories.category import Category
from sage.matrix.matrix0 import Matrix
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp


class GroupModules(Category):
    r"""The category of \(R[G]\)-modules for the specified \(R\) and \(G\)."""

    def __init__(self, base_ring: Any, group: Any) -> None:
        assert group.is_finite(), "this category currently requires a finite group"
        self._base_ring = base_ring
        self._group = group
        Category.__init__(self)

    def base_ring(self) -> Any:
        return self._base_ring

    def acting_group(self) -> Any:
        return self._group

    def _repr_object_names(self) -> str:
        return f"{self._base_ring}[{self._group}]-modules"

    def super_categories(self) -> list:
        return [FinitelyGeneratedFreeModules(self._base_ring)]

    class ParentMethods:
        def forget_action(self: Any) -> Any:
            return self._module

        def action(self: Any) -> GroupAction:
            return self._action

        def group(self: Any) -> Any:
            return self._action.domain()

        def action_of(self: Any, element: Any) -> ModuleAutomorphism:
            return self._action(element)

        def action_matrix(self: Any, element: Any) -> Matrix:
            return self.action_of(element).matrix()

        def Hom(self: Any, codomain: Any) -> Any:
            return group_module_homset(self, codomain)

        def act(self: Any, element: Any, vector_: Any) -> Any:
            return self.action_of(element)(vector_)

        def is_invariant(self: Any, vector_: Any) -> bool:
            return all(
                self.act(element, vector_) == vector_
                for element in self.group()
            )

        def subobject_on(self: Any, generators: Any) -> Any:
            return _group_subobject(self, generators)

        def hom(self: Any, images: Any, codomain: Any = None) -> Any:
            match images:
                case dict() if images:
                    target = next(iter(images.values())).parent()
                    assignment = images
                case dict():
                    assert codomain is not None, (
                        "an empty assignment requires its codomain"
                    )
                    target = codomain
                    assignment = images
                case _:
                    images = tuple(images)
                    assert len(images) == self.rank(), (
                        "the number of images does not match the chosen basis"
                    )
                    if images:
                        target = images[0].parent()
                    else:
                        assert codomain is not None, (
                            "an empty assignment requires its codomain"
                        )
                        target = codomain
                    assignment = dict(
                        zip(self.generating_set(), images)
                    )
            assert target.group() is self.group(), (
                "an equivariant map uses the same acting group on both sides"
            )
            return self.Hom(target)(assignment)

        @cached_method
        def isotypic_decomposition(self: Any) -> Any:
            return _isotypic_decomposition(self)

        def isotypic_component(self: Any, character: Any) -> Any:
            return self.isotypic_decomposition().summand(character)

        def multiplicity_space(self: Any, character: Any) -> Any:
            component = self.isotypic_component(character)
            degree = ZZ(character(self.group().one()))
            assert component.rank() % degree == 0, (
                "the component rank is not divisible by the character degree"
            )
            return BasedFreeModule(
                _isotypic_field(self),
                Sets.Δ[component.rank() // degree - 1],
            )

        def invariants(self: Any) -> Any:
            return _group_subobject(self, _invariant_generators(self))

        def module_coinvariants(self: Any) -> Any:
            return _module_coinvariants(self)


class GroupModuleHomset(ModuleHomset):
    r"""The homset of equivariant maps between two modules for one \(G\)."""

    def __init__(self, domain: Any, codomain: Any) -> None:
        assert codomain in GroupModules(domain.base_ring(), domain.group()), (
            "the codomain is not a module for the stated ring and group"
        )
        assert domain.group() is codomain.group(), (
            "an equivariant homset has one specified acting group"
        )
        ModuleHomset.__init__(
            self,
            domain,
            codomain,
            GroupModules(domain.base_ring(), domain.group()),
        )

    def _element_constructor_(self, images: Any) -> ModuleMorphism:
        match images:
            case ModuleMorphism():
                assert images.parent() is self, (
                    "an existing equivariant morphism belongs to its own homset"
                )
                return images
            case _:
                morphism = ModuleMorphism(self, images)
        for group_element in self.domain().group():
            for label in self.domain().generating_set():
                generator = self.domain().generator(label)
                assert morphism(
                    self.domain().act(group_element, generator)
                ) == self.codomain().act(
                    group_element,
                    morphism(generator),
                ), "the proposed map is not equivariant"
        return morphism

    def _repr_(self) -> str:
        return (
            f"Hom_{self.domain().group()}("
            f"{self.domain()}, {self.codomain()})"
        )


def group_module_homset(domain: Any, codomain: Any) -> GroupModuleHomset:
    r"""Return the canonical equivariant homset of two \(G\)-modules."""
    cache = domain.__dict__.setdefault("_group_module_homsets", {})
    homset = cache.get(codomain)
    if homset is None:
        homset = GroupModuleHomset(domain, codomain)
        cache[codomain] = homset
    return homset


class GroupModuleElement(ModuleElement):
    r"""An element of an \(R[G]\)-module and its image after forgetting \(G\)."""

    def __init__(self, parent: Any, element: Any) -> None:
        ModuleElement.__init__(self, parent)
        assert element.parent() is parent.forget_action(), (
            f"{element} is not an element of {parent.forget_action()}"
        )
        self._underlying = element

    def forget_action(self) -> Any:
        return self._underlying

    def coefficients(self) -> dict:
        return _coefficients(self._underlying)

    def _coordinates(self) -> Any:
        return _coordinate_vector(self._underlying)

    def _add_(self, other: Any) -> "GroupModuleElement":
        return self.parent()._over(self._underlying + other._underlying)

    def _sub_(self, other: Any) -> "GroupModuleElement":
        return self.parent()._over(self._underlying - other._underlying)

    def _neg_(self) -> "GroupModuleElement":
        return self.parent()._over(-self._underlying)

    def _lmul_(self, factor: Any) -> "GroupModuleElement":
        return self.parent()._over(factor * self._underlying)

    _rmul_ = _lmul_

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._underlying, other._underlying, op)

    def __hash__(self) -> int:
        return hash((id(self.parent()), self._underlying))

    def _repr_(self) -> str:
        return repr(self._underlying)


class GroupModule(Parent):
    r"""A finite free module \(M\) with a specified action \(G\to Aut_R(M)\)."""

    Element = GroupModuleElement

    def __init__(self, module: Any, action: GroupAction) -> None:
        assert module in FinitelyGeneratedFreeModules(module.base_ring()), (
            "an R[G]-module is constructed from an actual finite framed free module"
        )
        assert isinstance(action, GroupAction) and action.module() is module, (
            "the action must be a morphism into the supplied module's Aut homset"
        )
        self._module = module
        Parent.__init__(
            self,
            base=module.base_ring(),
            category=GroupModules(module.base_ring(), action.domain()),
        )
        refine(self, GroupModules(module.base_ring(), action.domain()))
        source = module.framing_morphism().domain()
        self._framing_morphism = framing_morphism(
            source,
            self,
            {
                label: self._over(module.generator(label))
                for label in module.generating_set()
            },
        )
        automorphisms = self.Aut()
        values = {
            element: automorphisms(
                {
                    label: self._over(
                        action(element)(module.generator(label))
                    )
                    for label in module.generating_set()
                }
            )
            for element in action.domain()
        }
        self._action = group_action_homset(action.domain(), self)(values)

    def framing_morphism(self) -> FramingMorphism:
        return self._framing_morphism

    def forget_action(self) -> Any:
        return self._module

    def monomial(self, label: Any) -> GroupModuleElement:
        return self.generator(label)

    def rank(self) -> Any:
        return self._module.rank()

    def linear_combination(self, coefficients: Any) -> GroupModuleElement:
        return self._over(self._module.linear_combination(coefficients))

    def zero(self) -> GroupModuleElement:
        return self._over(self._module.zero())

    def _over(self, element: Any) -> GroupModuleElement:
        return self.element_class(self, element)

    def _element_constructor_(self, element: Any) -> GroupModuleElement:
        assert isinstance(element, GroupModuleElement) and element.parent() is self, (
            f"{element} is not an element of {self}"
        )
        return element

    def __contains__(self, element: Any) -> bool:
        return (
            isinstance(element, GroupModuleElement)
            and element.parent() is self
        )

    def _repr_(self) -> str:
        return f"{self._module} with an action of {self.group()}"


def _invariant_generators(module: Any) -> list:
    constraints = matrix(
        module.base_ring(),
        [
            row
            for element in module.group()
            for row in (
                module.action_matrix(element)
                - identity_matrix(module.base_ring(), module.rank())
            ).rows()
        ],
    )
    return [
        module.linear_combination(row)
        for row in constraints.right_kernel().basis()
    ]


def _module_coinvariants(module: Any) -> Any:
    relations = _independent_generators(
        module,
        [
        module.act(group_element, generator) - generator
        for group_element in module.group()
        for generator in module.gens()
        ],
    )
    relation_module = BasedFreeModule(
        module.base_ring(),
        finite_ordered_set(tuple(relations)),
    )
    presentation = (
        relation_module.Hom(module)(
            {relation: relation for relation in relation_module.generating_set()}
        )
        if relations
        else relation_module.Hom(module).zero()
    )
    return FinitelyPresentedModule(presentation)


def _isotypic_field(module: Any) -> Any:
    return QQ if module.base_ring() is ZZ else module.base_ring()


def _isotypic_generators(module: Any, character: Any) -> list:
    group = module.group()
    field = _isotypic_field(module)
    degree = field(character(group.one()))
    terms = [
        field(character(element.inverse()))
        * matrix(field, module.action_matrix(element))
        for element in group
    ]
    projector = (degree / field(group.order())) * sum(
        terms,
        matrix(field, module.rank(), module.rank()),
    )
    assert projector * projector == projector, (
        "the chosen coefficient field does not split this representation exactly"
    )
    rows = projector.image().basis_matrix()
    if rows.nrows() == 0:
        return []
    if module.base_ring() is ZZ:
        rows = matrix(ZZ, rows * rows.denominator()).saturation()
    return [module.linear_combination(row) for row in rows.rows()]


def _restricted_action_automorphisms(
    module: Any,
    submodule: Any,
    generators: list,
) -> list:
    if not generators:
        return [submodule.Aut().one() for _ in module.group().gens()]
    field = (
        module.base_ring().fraction_field()
        if module.base_ring() is ZZ
        else module.base_ring()
    )
    inclusion_matrix = matrix(
        field,
        [_coordinate_vector(generator) for generator in generators],
    )
    restricted = []
    for group_element in module.group().gens():
        images = matrix(
            field,
            [
                _coordinate_vector(module.act(group_element, generator))
                for generator in generators
            ],
        )
        coefficients = (
            inclusion_matrix.transpose()
            .solve_right(images.transpose())
            .transpose()
        )
        assert coefficients * inclusion_matrix == images, (
            "the proposed submodule is not stable under the action"
        )
        assert all(
            entry in submodule.base_ring() for entry in coefficients.list()
        ), "the restricted action is not defined over the base ring"
        restricted.append(
            submodule.Aut()(
                {
                    label: submodule.linear_combination(row)
                    for label, row in zip(
                        submodule.generating_set(),
                        coefficients.rows(),
                    )
                }
            )
        )
    return restricted


def _equivariant_hom(domain: Any, codomain: Any, images: Any) -> Any:
    match images:
        case dict():
            assignment = images
        case _:
            images = tuple(images)
            assert len(images) == domain.ngens(), (
                "the number of images does not match the framing set"
            )
            assignment = dict(
                zip(domain.generating_set(), images)
            )
    return domain.Hom(codomain)(assignment)


def _group_subobject(module: Any, generators: Any) -> Any:
    generators = tuple(generators)
    assert all(generator.parent() is module for generator in generators), (
        "a subobject is generated by elements of this group module"
    )
    generators = _independent_generators(module, generators)
    labels = finite_ordered_set(tuple(generators))
    free = BasedFreeModule(
        module.base_ring(),
        labels,
    )
    restricted = _restricted_action_automorphisms(module, free, generators)
    action = GroupAction.from_generators(module.group(), free, restricted)
    submodule = GroupModule(free, action)
    return Subobject(
        _equivariant_hom(
            submodule,
            module,
            tuple(labels),
        )
    )


def _isotypic_decomposition(module: Any) -> Any:
    group = module.group()
    characteristic = module.base_ring().characteristic()
    assert characteristic == 0 or group.order() % characteristic != 0, (
        "Maschke's hypothesis fails for this coefficient ring"
    )
    characters = tuple(group.irreducible_characters())
    component_generators = tuple(
        tuple(_isotypic_generators(module, character))
        for character in characters
    )
    components = tuple(
        _group_subobject(module, generators)
        for generators in component_generators
    )
    all_generators = [
        generator
        for generators in component_generators
        for generator in generators
    ]
    included_sum = _group_subobject(module, all_generators)
    return DirectSum(
        included_sum,
        components,
        finite_ordered_set(characters),
    )
