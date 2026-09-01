"""Free modules with their canonical framing."""

from itertools import count

from sage.combinat.free_module import CombinatorialFreeModule
from sage.misc.cachefunc import cached_function, cached_method
from sage.modules.free_module import (
    FreeModuleFactory_with_standard_basis as _SageFreeModuleFactory,
)
from sage.modules.free_module import FreeModule_generic
from sage.rings.integer import Integer
from sage.structure.parent import Parent
from sage.categories.sets_cat import Sets
from sage.structure.element import Element, ModuleElement
from sage.structure.richcmp import op_EQ, op_NE
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
    owned_ring_view,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import refine


class _SparseFreeModuleElement(ModuleElement):
    """Finite-support coordinates in the owned free module ``R^(I)``."""

    def __init__(self, parent, coefficients) -> None:
        ModuleElement.__init__(self, parent)
        ring = parent.base_ring()
        self._coefficients = {
            label: ring(coefficient)
            for label, coefficient in coefficients.items()
            if ring(coefficient) != ring.zero()
        }

    def monomial_coefficients(self):
        return dict(self._coefficients)

    def _add_(self, other):
        ring = self.parent().base_ring()
        coefficients = dict(self._coefficients)
        for label, coefficient in other._coefficients.items():
            value = coefficients.get(label, ring.zero()) + coefficient
            if value == ring.zero():
                coefficients.pop(label, None)
            else:
                coefficients[label] = value
        return self.parent()._element_constructor_(coefficients)

    def _neg_(self):
        return self.parent()._element_constructor_(
            {label: -coefficient for label, coefficient in self._coefficients.items()}
        )

    def _lmul_(self, scalar):
        return self.parent()._raw_scalar_multiple(scalar, self)

    _rmul_ = _lmul_

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = (
            isinstance(other, _SparseFreeModuleElement)
            and other.parent() is self.parent()
            and other._coefficients == self._coefficients
        )
        return equal if op == op_EQ else not equal

    def _repr_(self):
        if not self._coefficients:
            return "0"
        return " + ".join(
            f"{coefficient}*B[{label!r}]"
            for label, coefficient in self._coefficients.items()
        )


class _SparseFreeModuleParent(Parent):
    """Owned finite-support carrier for the free module on arbitrary labels."""

    Element = _SparseFreeModuleElement

    def __init__(self, ring, labels) -> None:
        from sage.categories.category import Category
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
            FinitelyGeneratedFreeModules,
        )

        self._preamble_base_ring = ring
        self._preamble_module_generating_set = labels
        self._preamble_module_generator_function = self._basis_element
        categories = [FramedFreeModules(ring)]
        if labels.cardinality() in SageZZ:
            categories.append(FinitelyGeneratedFreeModules(ring))
        Parent.__init__(self, base=ring, category=Category.join(tuple(categories)))
        refine(self, categories)

        from dzack_research.preamble.categories.modules.pure.modules import Modules
        from dzack_research.preamble.categories.rings import ring_morphism

        endomorphisms = Modules(ring).End(self)
        self._preamble_scalar_action_morphism = ring_morphism(
            ring,
            endomorphisms,
            lambda scalar: endomorphisms.elementwise(
                lambda element: self._raw_scalar_multiple(scalar, element),
                verify_linearity=False,
            ),
        )
        from dzack_research.preamble.categories.modules.pure.modules import (
            register_module_scalar_action,
        )

        register_module_scalar_action(self)

    def _basis_element(self, label):
        if label not in self._preamble_module_generating_set:
            raise ValueError(f"{label!r} is not a module-generator label")
        return self.element_class(self, {label: self.base_ring().one()})

    def _element_constructor_(self, value):
        if isinstance(value, self.element_class) and value.parent() is self:
            return value
        if isinstance(value, dict):
            return self.element_class(self, value)
        if isinstance(value, (tuple, list)):
            labels = tuple(self.module_generating_set())
            if len(value) != len(labels):
                raise ValueError("coordinate tuple has the wrong length")
            return self.element_class(
                self,
                {
                    label: coefficient
                    for label, coefficient in zip(labels, value, strict=True)
                    if coefficient != 0
                },
            )
        raise TypeError(f"{value!r} does not describe an element of {self}")

    def zero(self):
        return self.element_class(self, {})

    def an_element(self):
        try:
            label = next(iter(self.module_generating_set()))
        except StopIteration:
            return self.zero()
        return self._basis_element(label)

    def _raw_scalar_multiple(self, scalar, element):
        scalar = self.base_ring()(scalar)
        element = self._element_constructor_(element)
        return self.element_class(
            self,
            {
                label: scalar * coefficient
                for label, coefficient in element._coefficients.items()
            },
        )

    def rank(self):
        return self.module_generating_set().cardinality()

    def is_finite_rank(self):
        return self.rank() in SageZZ

    def _repr_(self):
        return f"Free module on {self.module_generating_set()} over {self.base_ring()}"


class FramedFreeModules(OwnedCategoryOverBaseRing):
    r"""Free modules equipped with the canonical basis map."""

    @classmethod
    def _repr_object_names(cls):
        return "framed free modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules
        from dzack_research.preamble.categories.modules.pure.free_modules import FreeModules

        return [FreeModules(self.base_ring()), FramedModules(self.base_ring())]

    class ParentMethods:
        def base_ring(self):
            selected = self.__dict__.get("_preamble_base_ring")
            if selected is not None:
                return selected
            return owned_ring_view(self.base())

        @cached_method
        def module_generating_set(self):
            selected = self.__dict__.get("_preamble_module_generating_set")
            if selected is not None:
                return selected
            match self:
                case CombinatorialFreeModule():
                    return self.basis().keys()
                case FreeModule_generic():
                    return finite_ordered_set(range(int(self.rank())))
                case _:
                    assert False, (
                        f"{type(self).__name__} does not expose its basis through the active free-module adapter"
                    )

        def module_generator(self, label):
            selected_function = self.__dict__.get("_preamble_module_generator_function")
            if selected_function is not None:
                return selected_function(label)
            selected_values = self.__dict__.get("_preamble_module_generator_values")
            if selected_values is not None:
                if label not in self.module_generating_set():
                    raise ValueError(f"{label!r} is not a module-generator label")
                return selected_values[label]
            match self:
                case CombinatorialFreeModule():
                    return self.monomial(label)
                case FreeModule_generic():
                    labels = self.module_generating_set()
                    return self.gen(labels.position(label))
                case _:
                    assert False, (
                        f"{type(self).__name__} does not expose basis elements through the active free-module adapter"
                    )

        @cached_method
        def module_generators(self):
            return FreeModuleGeneratorSet(self)

        def framing_morphism(self):
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                framing_morphism,
            )

            return framing_morphism(self, self, self.module_generator)

        def is_torsion_free(self) -> bool:
            return True

        def base_change(self, ring_map):
            r"""Return ``S tensor_R M`` along the specified ring map ``R -> S``."""
            from dzack_research.preamble.categories.modules.base_change import (
                base_change_codomain,
            )

            target_ring = base_change_codomain(self, ring_map)
            return FreshFreeModuleOn(target_ring, self.module_generating_set())


class FreeModuleGeneratorSet(Parent):
    r"""The image of the canonical basis map of a free module."""

    def __init__(self, module) -> None:
        self._module = module
        Parent.__init__(self, category=Sets())

    def __iter__(self):
        return (
            self._module.module_generator(label)
            for label in self._module.module_generating_set()
        )

    def __contains__(self, element) -> bool:
        match element:
            case Element() if element.parent() is self._module:
                pass
            case _:
                return False
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_coefficients,
        )

        coefficients = module_coefficients(element)
        return len(coefficients) == 1 and next(iter(coefficients.values())) == self._module.base_ring().one()

    def cardinality(self):
        return self._module.module_generating_set().cardinality()

    def __getitem__(self, index):
        labels = self._module.module_generating_set()
        return self._module.module_generator(labels[index])

    def position(self, element) -> int:
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_coefficients,
        )

        coefficients = module_coefficients(element)
        if element not in self:
            raise ValueError(f"{element} is not a canonical module generator")
        label = next(iter(coefficients))
        return self._module.module_generating_set().position(label)

    def _repr_(self):
        size = self.cardinality()
        finite = size in SageZZ
        if not finite:
            return f"Canonical generators of {self._module}"
        return "{" + ", ".join(repr(generator) for generator in self) + "}"


def refine_free_module(module: Parent, base_ring=None):
    r"""Place a native Sage free module in the owned module hierarchy."""
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        FinitelyGeneratedFreeModules,
    )

    ring = owned_ring_view(module.base_ring() if base_ring is None else base_ring)
    module._preamble_base_ring = ring
    categories = [FramedFreeModules(ring)]
    match module:
        case FreeModule_generic():
            finite = True
        case CombinatorialFreeModule():
            finite = module.basis().keys().cardinality() in SageZZ
        case _:
            finite = False
    if finite:
        categories.append(FinitelyGeneratedFreeModules(ring))
    return refine(module, categories)


@cached_function
def _owned_finite_free_module(base_ring, rank):
    r"""Return the owned rank-``rank`` module without mutating Sage's factory object."""
    ring = owned_ring_view(base_ring)
    engine = engine_ring(ring)
    module = _SageFreeModuleFactory.create_object(
        None,
        (engine, int(rank), False, None),
    )
    return refine_free_module(module, ring)


def FreeModule(base_ring, rank_or_index_set):
    r"""Return the free module on a finite rank or an arbitrary index set."""
    ring = owned_ring_view(base_ring)
    engine = engine_ring(ring)
    if isinstance(rank_or_index_set, (int, Integer)):
        if rank_or_index_set < 0:
            raise ValueError("the rank of a free module is nonnegative")
        return _owned_finite_free_module(ring, rank_or_index_set)
    if isinstance(rank_or_index_set, (tuple, list)):
        rank_or_index_set = finite_ordered_set(rank_or_index_set)
    try:
        module = CombinatorialFreeModule(engine, rank_or_index_set)
    except (TypeError, ValueError):
        return _SparseFreeModuleParent(ring, rank_or_index_set)
    return refine_free_module(module, ring)


def FreeModuleOn(base_ring, module_generating_set):
    r"""Return \(F_R(S)\), retaining the actual labels in ``S``."""
    ring = owned_ring_view(base_ring)
    if isinstance(module_generating_set, (int, Integer)):
        module_generating_set = finite_ordered_set(range(int(module_generating_set)))
    elif isinstance(module_generating_set, (tuple, list)):
        module_generating_set = finite_ordered_set(module_generating_set)
    try:
        module = CombinatorialFreeModule(engine_ring(ring), module_generating_set)
    except (TypeError, ValueError):
        return _SparseFreeModuleParent(ring, module_generating_set)
    module._preamble_module_generating_set = module_generating_set
    return refine_free_module(module, ring)


_fresh_free_module_counter = count()


def FreshFreeModuleOn(base_ring, module_generating_set):
    r"""Return a new free-module parent on the specified basis labels.

    ``CombinatorialFreeModule`` is a ``UniqueRepresentation`` keyed by its
    basis and print parameters.  That canonicalization is inappropriate when
    the free module is being used as the carrier of a newly selected
    structure: two different actions or forms on isomorphic free modules must
    remain different structured objects.  A private construction prefix makes
    the Sage parent identity-distinct; the visible prefix is reset immediately
    afterwards, so the token is not mathematical data or public notation.
    """
    ring = owned_ring_view(base_ring)
    if isinstance(module_generating_set, (int, Integer)):
        module_generating_set = finite_ordered_set(range(int(module_generating_set)))
    elif isinstance(module_generating_set, (tuple, list)):
        module_generating_set = finite_ordered_set(module_generating_set)
    construction_prefix = f"_preamble_fresh_{next(_fresh_free_module_counter)}"
    try:
        module = CombinatorialFreeModule(
            engine_ring(ring),
            module_generating_set,
            prefix=construction_prefix,
        )
    except (TypeError, ValueError):
        return _SparseFreeModuleParent(ring, module_generating_set)
    module.print_options(prefix="B")
    module._preamble_module_generating_set = module_generating_set
    return refine_free_module(module, ring)
