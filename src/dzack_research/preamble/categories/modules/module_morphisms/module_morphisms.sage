r"""Native homsets and morphisms for the owned module categories.

A map from a framed module is declared by a set morphism from its generating
set to the underlying set of the codomain.  Its parent is the canonical homset
of the named domain and codomain.  Construction checks every relation of a
presented domain, so membership in a homset is parenthood and nothing else.
"""

from typing import Any

from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism, SetMorphism
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement, vector
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.sets import Sets
from sage_lattice_category_spike.objects.underlying_sets import UnderlyingSet


class ModuleHomset(Homset):
    r"""The homset \(\operatorname{Hom}_R(M,N)\) of two framed modules."""

    def __init__(self, domain: Any, codomain: Any, category: Any) -> None:
        assert domain.base_ring() == codomain.base_ring(), (
            "module morphisms require the same base ring"
        )
        Homset.__init__(
            self,
            domain,
            codomain,
            category=category,
            base=domain.base_ring(),
            check=False,
        )

    def _element_constructor_(self, images: Any) -> "ModuleMorphism":
        return ModuleMorphism(self, images)

    def zero(self) -> "ModuleMorphism":
        return ModuleMorphism(
            self,
            SetMorphism(
                Hom(
                    self.domain().generating_set(),
                    UnderlyingSet(self.codomain()),
                    Sets(),
                ),
                lambda element_of_S: self.codomain().zero(),
            ),
        )

    def identity(self) -> "ModuleMorphism":
        assert self.domain() is self.codomain(), (
            "an identity belongs to an endomorphism homset"
        )
        return ModuleMorphism(
            self,
            self.domain().generator_morphism(),
        )

    def __contains__(self, morphism: Any) -> bool:
        return (
            isinstance(morphism, ModuleMorphism)
            and morphism.parent() is self
        )

    def _repr_(self) -> str:
        return f"Hom({self.domain()}, {self.codomain()})"


def module_homset(domain: Any, codomain: Any) -> ModuleHomset:
    r"""Return the canonical module homset after forgetting extra structure."""
    cache = domain.__dict__.setdefault("_module_homsets", {})
    homset = cache.get(codomain)
    if homset is None:
        homset = ModuleHomset(
            domain,
            codomain,
            Modules(domain.base_ring()),
        )
        cache[codomain] = homset
    return homset


def _module_morphism(domain: Any, codomain: Any, images: Any) -> "ModuleMorphism":
    r"""Construct a module morphism through its canonical homset."""
    return module_homset(domain, codomain)(images)


def _underlying_module(module: Any) -> Any:
    match module:
        case FormModule():
            return module.forget_form()
        case Parent():
            return module
        case _:
            raise TypeError(f"{module!r} is not a module parent")


def _coordinate_vector(element: Any) -> FreeModuleElement:
    r"""Return finite coordinates in the element's declared framing."""
    match element:
        case FormModuleElement():
            return _coordinate_vector(element.forget_form())
        case GroupModuleElement():
            return _coordinate_vector(element.forget_action())
        case BasedFreeModuleElement():
            return element._coordinates()
        case FinitelyPresentedModuleElement():
            return vector(element._lift())
        case _:
            raise TypeError(
                f"{element} has no finite ordered framing in which a matrix "
                "coordinate vector is defined"
            )


def _coefficients(element: Any) -> dict:
    r"""Return the finite coefficient function of a framed-module element."""
    match element:
        case FormModuleElement():
            return _coefficients(element.forget_form())
        case GroupModuleElement():
            return _coefficients(element.forget_action())
        case FreeModuleOnSetElement() | BasedFreeModuleElement():
            return element.coefficients()
        case FinitelyPresentedModuleElement():
            return {
                element_of_S: coefficient
                for element_of_S, coefficient in zip(
                    element.parent().generating_set(), element._lift()
                )
                if coefficient != 0
            }
        case _:
            raise TypeError(
                f"{element} is not an element of an owned framed module"
            )


def _is_torsion(module: Any) -> bool:
    module = _underlying_module(module)
    return isinstance(module, FinitelyPresentedModule) and module.is_torsion()


def _independent_generators(module: Any, generators: Any) -> list:
    r"""Return a basis of the submodule spanned by finite input."""
    generators = list(generators)
    if not generators:
        return []
    rows = matrix(module.base_ring(), [_coordinate_vector(g) for g in generators])
    match module.base_ring() is ZZ:
        case True:
            independent = rows.hermite_form(include_zero_rows=False).rows()
        case False:
            independent = tuple(
                row for row in rows.echelon_form().rows() if not row.is_zero()
            )
    return [module.linear_combination(row) for row in independent]


class ModuleMorphism(Morphism):
    r"""The linear extension of a morphism \(S\to U(N)\)."""

    def __init__(self, parent: ModuleHomset, images: Any) -> None:
        Morphism.__init__(self, parent)
        generating_set = self._domain_generating_set()
        set_homset = Hom(
            generating_set,
            UnderlyingSet(parent.codomain()),
            Sets(),
        )
        match images:
            case SetMorphism():
                assert images.parent() is set_homset, (
                    "the generator morphism must belong to "
                    f"{set_homset}, got {images.parent()}"
                )
                generator_morphism = images
            case dict():
                assert generating_set in Sets().Finite(), (
                    "a dictionary specifies a morphism only for a finite "
                    "generating set; use a set morphism on the generating set"
                )
                assert set(images) == set(generating_set), (
                    "the assignment must name exactly every element of the "
                    "generating set"
                )
                values = dict(images)
                assert all(
                    image.parent() is parent.codomain()
                    for image in values.values()
                ), "every specified generator image must belong to the codomain"
                generator_morphism = SetMorphism(
                    set_homset,
                    values.__getitem__,
                )
            case _ if callable(images):
                generator_morphism = SetMorphism(set_homset, images)
            case _:
                raise TypeError(
                    "a module morphism is the linear extension of a set "
                    "morphism from the domain's generating set"
                )
        self._generator_morphism = generator_morphism
        self._check_relations()

    def _domain_generating_set(self) -> Any:
        return self.domain().generating_set()

    def _check_relations(self) -> None:
        domain = _underlying_module(self.domain())
        if domain not in FinitelyPresentedModules(domain.base_ring()):
            return
        generating_set = tuple(domain.generating_set())
        zero = self.codomain().zero()
        assert all(
            sum(
                (
                    coefficient
                    * self.generator_morphism()(element_of_S)
                    for coefficient, element_of_S in zip(
                        relation,
                        generating_set,
                    )
                ),
                zero,
            )
            == zero
            for relation in domain.relation_matrix().rows()
        ), "the assignment does not kill every relation"

    def generator_morphism(self) -> SetMorphism:
        r"""Return the set morphism whose linear extension is this morphism."""
        return self._generator_morphism

    def images(self) -> tuple:
        generating_set = self.domain().generating_set()
        assert generating_set in Sets().Finite(), (
            "listing all images requires a finite framing set"
        )
        return tuple(
            self.generator_morphism()(element_of_S)
            for element_of_S in generating_set
        )

    def matrix(self) -> Matrix:
        r"""Return the matrix in the finite ordered framings."""
        domain_labels = self.domain().generating_set()
        codomain_labels = self.codomain().generating_set()
        assert (
            domain_labels in Sets().Finite()
            and codomain_labels in Sets().Finite()
        ), "a matrix requires finite ordered framings"
        images = self.images()
        if not images:
            return matrix(self.codomain().base_ring(), 0, len(codomain_labels))
        return matrix([_coordinate_vector(image) for image in images])

    def _call_(self, element: Any) -> Any:
        assert element.parent() is self.domain(), (
            f"{element} is not an element of {self.domain()}"
        )
        return sum(
            (
                coefficient
                * self.generator_morphism()(element_of_S)
                for element_of_S, coefficient in _coefficients(element).items()
            ),
            self.codomain().zero(),
        )

    def lift(self, element: Any) -> Any:
        assert element.parent() is self.codomain(), (
            f"{element} is not an element of {self.codomain()}"
        )
        system = self.matrix()
        relations = self._codomain_relations()
        coefficients = _solve_left_integrally(
            system.stack(relations) if relations.nrows() else system,
            _coordinate_vector(element),
        )
        preimage = self.domain().linear_combination(
            coefficients[: system.nrows()]
        )
        assert self(preimage) == element, (
            f"{element} is not in the image of this morphism"
        )
        return preimage

    def kernel(self) -> Any:
        assert not _is_torsion(self.domain()), (
            "this kernel construction requires a free domain"
        )
        basis = self.matrix().left_kernel_matrix().rows()
        return self.domain().subobject_on(
            [self.domain().linear_combination(row) for row in basis]
        )

    def cokernel(self) -> Any:
        return TorsionModule(self)

    def image(self) -> Any:
        return self.codomain().subobject_on(list(self.images()))

    def is_injective(self) -> bool:
        r"""Return whether this morphism is a monomorphism."""
        domain = self.domain()
        if _is_torsion(domain):
            zero = domain.zero()
            return all(
                element == zero or self(element) != self.codomain().zero()
                for element in domain
            )
        assert domain in FramedFreeModules(domain.base_ring()), (
            "injectivity is implemented for free and finite torsion domains"
        )
        return self.matrix().rank() == domain.rank()

    def index(self) -> Any:
        codomain = _underlying_module(self.codomain())
        image = self.matrix()
        width = len(tuple(codomain.generating_set()))
        if isinstance(codomain, FinitelyPresentedModule):
            relations = codomain.relation_matrix()
            rows = relations.stack(image) if image.nrows() else relations
            basis = rows.hermite_form(include_zero_rows=False)
            assert basis.nrows() == width, (
                "the image does not have finite index in the codomain"
            )
            return abs(basis.det())
        if codomain.base_ring() is ZZ:
            basis = image.hermite_form(include_zero_rows=False)
            assert basis.nrows() == width, (
                "the image does not have finite index in the codomain"
            )
            return abs(basis.det())
        assert image.rank() == width, (
            "the image does not have finite index in the codomain"
        )
        return ZZ.one()

    def orthogonal_complement(self) -> Any:
        codomain = self.codomain()
        assert not _is_torsion(codomain), (
            "orthogonal complement is defined here in a free codomain"
        )
        pairing = matrix(codomain.gram_matrix()) * self.matrix().transpose()
        return codomain.subobject_on(
            [
                codomain.linear_combination(row)
                for row in pairing.left_kernel().basis()
            ]
        )

    def _codomain_relations(self) -> Matrix:
        codomain = _underlying_module(self.codomain())
        match codomain:
            case FinitelyPresentedModule():
                return codomain.relation_matrix()
            case _:
                return matrix(
                    ZZ,
                    0,
                    len(tuple(self.codomain().generating_set())),
                )

    def _repr_type(self) -> str:
        return "Module"

    def _repr_defn(self) -> str:
        generating_set = self.domain().generating_set()
        if generating_set not in Sets().Finite():
            return "the linear extension of a generator morphism"
        return "\n".join(
            f"{element_of_S!r} |--> "
            f"{self.generator_morphism()(element_of_S)}"
            for element_of_S in generating_set
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ModuleMorphism) or self.parent() is not other.parent():
            return False
        generating_set = self.domain().generating_set()
        assert generating_set in Sets().Finite(), (
            "equality of maps on a nonenumerable framing needs an explicit theorem"
        )
        return self.images() == other.images()

    def __hash__(self) -> int:
        generating_set = self.domain().generating_set()
        assert generating_set in Sets().Finite(), (
            "a morphism on a nonenumerable framing is not hashable"
        )
        return hash((id(self.parent()), self.images()))


class FramingMorphism(ModuleMorphism):
    r"""A declared epimorphism \(F_R(S)\twoheadrightarrow M\).

    Surjectivity is part of the construction datum.  It is not replaced by an
    enumeration algorithm, since \(S\) may be a membership-only set.
    """

    def __init__(self, parent: ModuleHomset, images: Any) -> None:
        assert parent.domain() in FramedFreeModules(
            parent.domain().base_ring()
        ), "the source of a framing is a free module on a specified set"
        ModuleMorphism.__init__(self, parent, images)

    def _domain_generating_set(self) -> Any:
        return self.domain().generator_morphism().domain()

    def is_surjective(self) -> bool:
        return True


def framing_morphism(
    domain: Any,
    codomain: Any,
    images: Any,
) -> FramingMorphism:
    r"""Construct the declared framing epimorphism in its canonical homset."""
    return FramingMorphism(module_homset(domain, codomain), images)


class ModuleAutomorphism(ModuleMorphism):
    r"""An invertible endomorphism of a finitely generated free module."""

    def __init__(self, parent: "ModuleAutomorphismGroup", images: Any) -> None:
        ModuleMorphism.__init__(self, parent, images)
        assert self.domain() is self.codomain(), (
            "an automorphism is an endomorphism"
        )
        determinant = self.matrix().det()
        assert determinant.is_unit(), (
            f"the determinant {determinant} is not a unit"
        )

    def __mul__(self, other: Any) -> "ModuleAutomorphism":
        assert (
            isinstance(other, ModuleAutomorphism)
            and other.parent() is self.parent()
        ), "composition here is internal to one automorphism group"
        return self.parent()(
            SetMorphism(
                Hom(
                    self.domain().generating_set(),
                    UnderlyingSet(self.codomain()),
                    Sets(),
                ),
                lambda element_of_S: self(
                    other.generator_morphism()(element_of_S)
                ),
            )
        )

    def inverse(self) -> "ModuleAutomorphism":
        inverse_matrix = self.matrix().inverse()
        images = [
            self.domain().linear_combination(row)
            for row in inverse_matrix.rows()
        ]
        return self.parent()(
            dict(zip(self.domain().generating_set(), images))
        )

    def cyclic_subgroup(self) -> "ModuleAutomorphismGroup":
        return self.parent().subgroup([self])


class ModuleAutomorphismGroup(ModuleHomset):
    r"""The automorphism homset, or a finite subgroup with the same objects."""

    Element = ModuleAutomorphism

    def __init__(self, module: Any, generators: Any = None) -> None:
        ModuleHomset.__init__(
            self,
            module,
            module,
            Modules(module.base_ring()),
        )
        self._generators = None
        self._elements = None
        if generators is not None:
            supplied = tuple(generators)
            assert supplied, "a generated subgroup needs at least one generator"
            assert all(
                isinstance(generator, ModuleAutomorphism)
                for generator in supplied
            ), "subgroup generators must be module automorphisms"
            self._generators = tuple(
                self(generator.generator_morphism())
                for generator in supplied
            )
            self._elements = self._close()

    def _element_constructor_(self, images: Any) -> ModuleAutomorphism:
        return ModuleAutomorphism(self, images)

    def module(self) -> Any:
        return self.domain()

    def one(self) -> ModuleAutomorphism:
        return self(self.module().generator_morphism())

    def subgroup(self, generators: Any) -> "ModuleAutomorphismGroup":
        generators = tuple(generators)
        assert all(generator in self for generator in generators), (
            "each subgroup generator must belong to this automorphism group"
        )
        return ModuleAutomorphismGroup(self.module(), generators)

    def gens(self) -> tuple:
        return () if self._generators is None else self._generators

    def is_finite(self) -> bool:
        return self._elements is not None

    def order(self) -> int:
        assert self._elements is not None, (
            "the full automorphism homset is not an enumerated finite group"
        )
        return len(self._elements)

    def __iter__(self):
        assert self._elements is not None, (
            "the full automorphism homset is not enumerable"
        )
        return iter(self._elements)

    def __contains__(self, element: Any) -> bool:
        return (
            isinstance(element, ModuleAutomorphism)
            and element.parent() is self
        )

    def irreducible_characters(self) -> tuple:
        assert self.is_finite() and len(self._generators) == 1, (
            "the implemented character table is for a finite cyclic subgroup"
        )
        return tuple(
            _AutomorphismCharacter(self, index)
            for index in range(self.order())
        )

    def trivial_character(self) -> Any:
        return self.irreducible_characters()[0]

    def _close(self) -> tuple:
        identity = self.one()
        elements = {identity}
        frontier = [identity]
        steps = 0
        while frontier:
            current = frontier.pop()
            for generator in self._generators:
                for factor in (generator, generator.inverse()):
                    candidate = current * factor
                    if candidate in elements:
                        continue
                    elements.add(candidate)
                    frontier.append(candidate)
                    steps += 1
                    assert steps <= 100000, (
                        "the proposed subgroup has not closed after 100000 elements"
                    )
        return tuple(elements)

    def _repr_(self) -> str:
        if self.is_finite():
            return f"Subgroup of Aut({self.module()}) of order {self.order()}"
        return f"Aut({self.module()})"


class _AutomorphismCharacter:
    r"""A character of a cyclic subgroup, evaluated on its actual elements."""

    def __init__(self, group: ModuleAutomorphismGroup, index: int) -> None:
        self._group = group
        self._index = index
        generator = group.gens()[0]
        current = group.one()
        self._powers = {}
        for power in range(group.order()):
            self._powers[current] = power
            current = current * generator

    def __call__(self, element: Any) -> Any:
        assert element in self._powers, (
            "the element is outside this character's group"
        )
        power = self._powers[element]
        order = self._group.order()
        if order <= 2:
            return QQ.one() if self._index == 0 or power == 0 else QQ(-1)
        return CyclotomicField(order).gen() ** (self._index * power)

    def degree(self) -> int:
        return 1

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, _AutomorphismCharacter)
            and self._group is other._group
            and self._index == other._index
        )

    def __hash__(self) -> int:
        return hash((id(self._group), self._index))


class GroupActionHomset(Homset):
    r"""Homomorphisms from a group to the automorphisms of one module."""

    def __init__(self, group: Any, module: Any) -> None:
        self._module = module
        Homset.__init__(
            self,
            group,
            module.Aut(),
            category=Groups(),
            check=False,
        )

    def module(self) -> Any:
        return self._module

    def _element_constructor_(self, values: dict) -> "GroupAction":
        return GroupAction(self, values)

    def __contains__(self, action: Any) -> bool:
        return (
            isinstance(action, GroupAction)
            and action.parent() is self
        )


def group_action_homset(group: Any, module: Any) -> GroupActionHomset:
    r"""Return the canonical homset \(G\to\operatorname{Aut}_R(M)\)."""
    cache = module.__dict__.setdefault("_group_action_homsets", {})
    homset = cache.get(group)
    if homset is None:
        homset = GroupActionHomset(group, module)
        cache[group] = homset
    return homset


class GroupAction(Morphism):
    r"""A homomorphism \(G\to\operatorname{Aut}_R(M)\)."""

    def __init__(self, parent: GroupActionHomset, values: dict) -> None:
        Morphism.__init__(self, parent)
        group = parent.domain()
        automorphisms = parent.codomain()
        assert group.is_finite(), "this constructor requires a finite group"
        assert set(values) == set(group), (
            "the action must name the image of every group element"
        )
        assert all(value.parent() is automorphisms for value in values.values()), (
            "every value must be an element of the stated automorphism homset"
        )
        assert values[group.one()] == automorphisms.one(), (
            "the identity must map to the identity automorphism"
        )
        assert all(
            values[left * right] == values[left] * values[right]
            for left in group
            for right in group
        ), "the supplied function is not a group homomorphism"
        self._values = dict(values)

    @classmethod
    def from_generators(
        cls, group: Any, module: Any, generator_images: Any
    ) -> "GroupAction":
        parent = group_action_homset(group, module)
        generators = tuple(group.gens())
        images = tuple(generator_images)
        assert len(images) == len(generators), (
            f"{group} has {len(generators)} generators, got {len(images)} images"
        )
        assert all(image.parent() is module.Aut() for image in images), (
            "the generator images must belong to Aut(M)"
        )
        values = {group.one(): module.Aut().one()}
        frontier = [group.one()]
        while frontier:
            current = frontier.pop()
            for generator, image in zip(generators, images, strict=True):
                product = current * generator
                candidate = values[current] * image
                match product in values:
                    case True:
                        assert values[product] == candidate, (
                            "the images do not respect the relations of the group"
                        )
                    case False:
                        values[product] = candidate
                        frontier.append(product)
        return parent(values)

    def module(self) -> Any:
        return self.parent().module()

    def _call_(self, element: Any) -> ModuleAutomorphism:
        return self._values[element]

    def values(self) -> dict:
        return dict(self._values)


def _solve_left_integrally(system: Matrix, target: Any) -> Any:
    r"""Return an integral solution of \(aS=t\), or fail."""
    smith, left, right = system.transpose().smith_form()
    shifted = left * vector(ZZ, target)
    width = smith.ncols()
    solution = [ZZ.zero()] * width
    for index, value in enumerate(shifted):
        divisor = smith[index, index] if index < width else ZZ.zero()
        assert divisor != 0 or value == 0, (
            f"no solution: row {index} is zero but asks for {value}"
        )
        if divisor != 0:
            assert value % divisor == 0, (
                f"no integral solution: row {index} asks for {value}/{divisor}"
            )
            solution[index] = value // divisor
    return right * vector(ZZ, solution)
