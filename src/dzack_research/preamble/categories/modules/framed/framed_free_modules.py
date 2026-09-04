"""Free modules with their canonical framing."""

from itertools import islice

from sage.categories.category import Category
from sage.combinat.free_module import CombinatorialFreeModule
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.modules.free_module import FreeModule as _SageFreeModule
from sage.modules.free_module import FreeModule_generic
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_element,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_image,
    finite_ordered_set,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
)
from dzack_research.preamble.refine import refine


class FreeModuleBaseRings(Category):
    r"""Rings equipped with the selected free-module exponent construction."""

    def super_categories(self):
        return [OwnedRings()]

    class ParentMethods:
        def _fresh_free_module_on(self, labels):
            return FreshFreeModuleOn(self.base_ring(), labels)

        def __pow__(self, exponent):
            return FreeModule(self, exponent)


def _scalar_action_morphism(module, scalar_multiple):
    r"""Return ``rho_M : R -> End_R(M)`` from the parent's private scalar crossing."""
    from dzack_research.preamble.categories.modules.pure.modules import Modules
    from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism

    ring = module.base_ring()
    endomorphisms = Modules(ring).End(module)
    return ring_morphism(
        ring,
        endomorphisms,
        lambda scalar: endomorphisms.elementwise(
            lambda element: scalar_multiple(scalar, element),
            verify_linearity=False,
        ),
    )


def _finitely_generated_free_placement(ring, module_generating_set):
    r"""Return the owned categories of ``R^(S)``: finitely generated exactly when ``S`` is finite."""
    from dzack_research.preamble.categories.sets.cardinals import cardinal

    categories = [FramedFreeModules(ring)]
    if cardinal(module_generating_set.cardinality()).is_finite():
        categories.append(FinitelyGeneratedFreeModules(ring))
    return categories


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

    def __rmul__(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def __mul__(self, other):
        if (
            isinstance(other, _SparseFreeModuleElement)
            and other.parent() is self.parent()
            and hasattr(self.parent(), "multiplication_morphism")
        ):
            return self._mul_(other)
        try:
            return self.parent().scalar_multiple(other, self)
        except (TypeError, ValueError):
            return NotImplemented

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = (
            isinstance(other, _SparseFreeModuleElement)
            and other.parent() is self.parent()
            and other._coefficients == self._coefficients
        )
        return equal if op == op_EQ else not equal

    def __hash__(self):
        return hash((id(self.parent()), frozenset(self._coefficients.items())))

    def _repr_(self):
        if not self._coefficients:
            return "0"
        return " + ".join(
            f"{coefficient}*B[{label!r}]"
            for label, coefficient in self._coefficients.items()
        )


class _SparseFreeModuleParent(Parent):
    """The owned free module on arbitrary labels over a ring with no Sage engine for it."""

    Element = _SparseFreeModuleElement

    def __init__(self, ring, labels) -> None:
        self._preamble_base_ring = ring
        self._preamble_module_generating_set = labels
        self._preamble_free_module_constructor = lambda new_labels: FreshFreeModuleOn(
            ring,
            new_labels,
        )
        self._preamble_module_generator_function = self._basis_element
        self._preamble_module_coefficient_function = (
            lambda element: self._element_constructor_(element).monomial_coefficients()
        )
        categories = _finitely_generated_free_placement(ring, labels)
        Parent.__init__(self, base=ring, category=Category.join(tuple(categories)))
        refine(self, categories)
        self._preamble_scalar_action_morphism = _scalar_action_morphism(
            self,
            self._raw_scalar_multiple,
        )
        from dzack_research.preamble.categories.modules.pure.modules import (
            register_module_scalar_action,
        )

        register_module_scalar_action(self)

    def _basis_element(self, label):
        labels = self._preamble_module_generating_set
        if label not in labels:
            raise ValueError(f"{label!r} is not a module-generator label")
        return self.element_class(self, {labels(label): self.base_ring().one()})

    def _element_constructor_(self, value):
        if isinstance(value, _SparseFreeModuleElement) and value.parent() is self:
            return value
        if isinstance(value, dict):
            return self.element_class(self, value)
        if isinstance(value, (tuple, list)):
            labels = self.module_generating_set()
            if not hasattr(labels, "unrank"):
                raise TypeError(
                    "coordinate sequence syntax requires an ordered enumerated framing"
                )
            from dzack_research.preamble.categories.sets.cardinals import cardinal

            cardinality = cardinal(labels.cardinality())
            if cardinality.is_finite() and len(value) != int(cardinality.finite_value()):
                raise ValueError("coordinate tuple has the wrong length")
            coefficients = {}
            for position, coefficient in enumerate(value):
                try:
                    label = labels.unrank(position)
                except (IndexError, StopIteration) as error:
                    raise ValueError(
                        "coordinate tuple exceeds the displayed generating set"
                    ) from error
                if coefficient != 0:
                    coefficients[label] = coefficient
            return self.element_class(self, coefficients)
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
        ring = self.base_ring()

        def product(coefficient):
            try:
                return ring._from_engine_element(
                    _engine_element(ring, scalar) * _engine_element(ring, coefficient)
                )
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                return scalar * coefficient

        return self.element_class(
            self,
            {
                label: product(coefficient)
                for label, coefficient in element._coefficients.items()
            },
        )

    def _repr_(self):
        return f"Free module on {self.module_generating_set()} over {self.base_ring()}"


class FramedFreeModules(OwnedCategoryOverBaseRing):
    r"""Free modules equipped with the canonical basis map."""

    @classmethod
    def _repr_object_names(cls):
        return "framed free modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import (
            FramedModules,
            FreeModules,
        )

        return [FreeModules(self.base_ring()), FramedModules(self.base_ring())]

    class ParentMethods:
        def _represented_cokernel_of_morphism(self, morphism):
            if morphism.codomain() is not self:
                return NotImplemented
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
                FinitelyPresentedModule,
            )

            return FinitelyPresentedModule(morphism)

        def _Hom_(self, codomain, category=None):
            from dzack_research.preamble.categories.modules.pure.modules import Modules

            if category is not None and not category.is_subcategory(Modules(self.base_ring())):
                raise TypeError("this is not a module homset category")
            if not hasattr(codomain, "module_generating_set"):
                raise TypeError("the parent-level module Hom constructor requires a framed target")
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )

            return module_homset(self, codomain)

        def subobject_on(self, module_generating_set):
            r"""Return the submodule spanned by the specified elements."""
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                module_subobject_on,
            )

            return module_subobject_on(self, module_generating_set)

        def base_ring(self):
            selected = self.__dict__.get("_preamble_base_ring")
            if selected is not None:
                return selected
            return _owned_ring(self.base())

        def module_generating_set(self):
            labels = self.__dict__.get("_preamble_module_generating_set")
            assert labels is not None, f"{self} declares no module generating set"
            return labels

        def module_generator(self, label):
            selected_function = self.__dict__.get("_preamble_module_generator_function")
            if selected_function is not None:
                return selected_function(label)
            if label not in self.module_generating_set():
                raise ValueError(f"{label!r} is not a module-generator label")
            return self._preamble_module_generator_values[label]

        @cached_method
        def module_generators(self):
            from dzack_research.preamble.categories.sets.indexed_families import indexed_family

            return indexed_family(
                self.module_generating_set(),
                self.module_generator,
                name="Free-module generator family",
            )

        def framing_morphism(self):
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                framing_morphism,
            )

            return framing_morphism(self, self, self.module_generator)

        def _free_biproduct_with(self, other, labels):
            r"""Return the free biproduct realization when both factors are free."""
            if not hasattr(other, "_free_biproduct_with"):
                return NotImplemented
            return FreeModuleOn(self.base_ring(), labels)

        def rank(self):
            cardinality = self.module_generating_set().cardinality()
            try:
                finite_rank = int(cardinality)
            except (TypeError, ValueError, OverflowError):
                return cardinality
            from sage.rings.integer_ring import ZZ as SageZZ
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

            return _own_ring(SageZZ)(finite_rank)

        def is_finite_rank(self) -> bool:
            return self.rank() in SageZZ

        def is_torsion_free(self) -> bool:
            return True

        def cardinality(self):
            r"""Return ``|R^(S)|``: ``|R|^|S|`` for finite ``S``, else ``max(|R|, |S|)`` by finite support."""
            from dzack_research.preamble.categories.sets.cardinals import Cardinalities, cardinal

            scalars = cardinal(self.base_ring().cardinality())
            labels = cardinal(self.module_generating_set().cardinality())
            if labels.is_finite():
                return scalars**labels
            if scalars == Cardinalities().one():
                return Cardinalities().one()
            return Cardinalities().supremum(scalars, labels)

        def base_change(self, ring_map):
            r"""Return ``S tensor_R M`` along the specified ring map ``R -> S``."""
            from dzack_research.preamble.categories.modules.base_change import (
                base_change_codomain,
            )

            target_ring = base_change_codomain(self, ring_map)
            return FreshFreeModuleOn(target_ring, self.module_generating_set())



def _element_from_row(module, row):
    return module.linear_combination(
        {
            label: coefficient
            for label, coefficient in zip(
                module.module_generating_set(), row, strict=True
            )
            if coefficient
        }
    )


def _known_finite_generator_family(module_generating_set):
    r"""Normalize one explicitly finite spanning family without guessing finiteness."""
    from dzack_research.preamble.categories.sets.cardinals import cardinal

    if isinstance(module_generating_set, (tuple, list, range)):
        return finite_ordered_set(module_generating_set)
    try:
        size = cardinal(module_generating_set.cardinality())
        finite = size.is_finite()
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        finite = False
    if not finite:
        raise TypeError(
            "subobject generators must be a known finite owned set/family or explicit finite literal"
        )
    return module_generating_set


def _span_basis_elements(module, module_generating_set):
    r"""Return the canonical span basis using only the finite union of supports."""
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_coefficients,
    )
    from dzack_research.preamble.categories.rings.ring_foundation import (
        PrincipalIdealDomains,
        _engine_element,
    )

    ring = module.base_ring()
    if ring not in PrincipalIdealDomains():
        raise NotImplementedError(
            "the active finite submodule basis engine currently requires a principal ideal domain"
        )
    if module not in FramedFreeModules(ring):
        raise NotImplementedError(
            "the active submodule basis engine requires a framed free ambient module"
        )

    generators = _known_finite_generator_family(module_generating_set)
    ambient_labels = module.module_generating_set()
    if not hasattr(ambient_labels, "rank") or not hasattr(ambient_labels, "unrank"):
        raise TypeError("submodule basis reduction requires a ranked ambient framing")

    # Determine the finite coordinate window from the supplied finite supports.
    support_by_rank = {}
    for candidate in generators:
        element = candidate if candidate.parent() is module else module(candidate)
        for label in module_coefficients(element, module):
            support_by_rank[int(ambient_labels.rank(label))] = label

    # Private finite backend serialization.  Only the finite support window is
    # materialized; the ambient framing itself is never enumerated.
    support_ranks = sorted(support_by_rank)
    engine = _engine_ring(ring)
    free = _SageFreeModule(engine, len(support_ranks))
    engine_rows = []
    for candidate in generators:
        element = candidate if candidate.parent() is module else module(candidate)
        coefficients = module_coefficients(element, module)
        engine_rows.append(
            [
                _engine_element(
                    ring,
                    coefficients.get(support_by_rank[rank], ring.zero()),
                )
                for rank in support_ranks
            ]
        )
    basis = (
        free.zero_submodule().basis_matrix()
        if not engine_rows
        else free.submodule(engine_rows).basis_matrix()
    )
    positions = Sets.Δ[basis.nrows() - 1]

    def basis_element(position):
        row = basis.row(int(position))
        return module.linear_combination(
            {
                support_by_rank[rank]: ring._from_engine_element(row[column])
                for column, rank in enumerate(support_ranks)
                if row[column]
            }
        )

    return finite_ordered_image(
        positions,
        basis_element,
        name=f"Canonical span basis in {module}",
    )


def module_subobject_on(module, module_generating_set):
    r"""Return the submodule spanned by one explicitly finite family.

    The finite PID backend is restricted to the union of supports of the input
    elements.  In particular, a finitely generated submodule of an infinitely
    generated free module never causes enumeration of the ambient framing.
    """
    basis = _span_basis_elements(module, module_generating_set)
    return _module_subobject_spanning(module, basis)


@cached_function(key=lambda module, basis: (id(module), basis))
def _module_subobject_spanning(module, basis):
    r"""Return the subobject on its canonical owned finite span basis.

    Ambient identity is part of the subobject type.  Do not use Sage's generic
    cached-function key here: equal free-module parents need not be identical
    mathematical endpoints.
    """

    ring = module.base_ring()
    if module not in FramedFreeModules(ring):
        raise NotImplementedError(
            "the active submodule basis engine constructs subobjects of framed free modules"
        )
    labels = Sets.Δ[int(basis.cardinality()) - 1]
    source = FreshFreeModuleOn(ring, labels)
    return _finalize_module_subobject(module, basis, source)


def _finalize_module_subobject(module, basis, source, *, inclusion=None):
    r"""Install the common inclusion and finite-support lift on a chosen source.

    ``source`` is selected by the mathematical owner of the ambient structured
    module.  Generic module subobjects use an ordinary free source; formed
    modules and lattices choose sources carrying the pulled-back structure in
    their own defining modules.
    """
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_embedding,
    )

    ring = module.base_ring()
    labels = source.module_generating_set()

    def embedded(label):
        return basis.unrank(int(label))

    if inclusion is None:
        inclusion = module_embedding(source, module, embedded)
    elif inclusion.domain() is not source or inclusion.codomain() is not module:
        raise ValueError("the selected subobject inclusion has the wrong endpoints")

    # A finite subobject of an infinitely framed free module still has a
    # finite-support membership problem.  Install that exact lift rather than
    # routing through the generic finite-ambient coordinate solver.

    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        _solve_left_integrally,
        module_coefficients,
    )

    ambient_labels = module.module_generating_set()
    support_by_rank = {}
    for basis_element in basis:
        for ambient_label in module_coefficients(basis_element, module):
            support_by_rank[int(ambient_labels.rank(ambient_label))] = ambient_label
    support_positions = Sets.Δ[len(support_by_rank) - 1]

    def support_rank(position):
        requested = int(position)
        for offset, rank in enumerate(sorted(support_by_rank)):
            if offset == requested:
                return rank
        raise IndexError(position)

    support_labels = finite_ordered_image(
        support_positions,
        lambda position: support_by_rank[support_rank(position)],
        name=f"Finite support of {source} in {module}",
    )
    source_rank = int(basis.cardinality())
    support_rank_count = int(support_labels.cardinality())
    if source_rank:
        coordinate_matrix = MatrixSpace(
            ring,
            source_rank,
            support_rank_count,
        ).from_rows(
            tuple(
                tuple(
                    module_coefficients(basis.unrank(i), module).get(
                        support_labels.unrank(j),
                        ring.zero(),
                    )
                    for j in range(support_rank_count)
                )
                for i in range(source_rank)
            )
        )
    else:
        coordinate_matrix = None

    def lift_from_finite_support(element):
        element = element if element.parent() is module else module(element)
        coefficients = module_coefficients(element, module)
        if any(label not in support_labels for label in coefficients):
            raise ValueError("the element has support outside this subobject")
        if source_rank == 0:
            if coefficients:
                raise ValueError("the nonzero element is not in the zero subobject")
            return source.zero()
        solution = _solve_left_integrally(
            coordinate_matrix,
            (
                coefficients.get(support_labels.unrank(j), ring.zero())
                for j in range(support_rank_count)
            ),
            ring,
        )
        return source.linear_combination(
            {
                labels.unrank(i): coefficient
                for i, coefficient in enumerate(solution)
                if coefficient
            }
        )

    inclusion._preamble_lift = lift_from_finite_support
    source._preamble_inclusion = inclusion
    from dzack_research.preamble.categories.modules.pure.modules import ModuleSubobjects

    source = refine(source, ModuleSubobjects(ring))
    return source



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

    def _generator_label(self, element):
        r"""Return the label of ``element`` when it is a canonical generator, else ``None``."""
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_coefficients,
        )

        if element not in self._module:
            return None
        coefficients = module_coefficients(self._module(element), self._module)
        if len(coefficients) != 1:
            return None
        label, coefficient = next(iter(coefficients.items()))
        return label if coefficient == self._module.base_ring().one() else None

    def __contains__(self, element) -> bool:
        return self._generator_label(element) is not None

    def cardinality(self):
        return self._module.module_generating_set().cardinality()

    def __getitem__(self, index):
        labels = self._module.module_generating_set()
        return self._module.module_generator(labels[index])

    def position(self, element) -> int:
        label = self._generator_label(element)
        if label is None:
            raise ValueError(f"{element} is not a canonical module generator")
        return self._module.module_generating_set().position(label)

    def _repr_(self):
        size = self.cardinality()
        if size in SageZZ and size > 12:
            return f"Set of {size} module generators of {self._module}"
        return "{" + ", ".join(repr(generator) for generator in self) + "}"


def _module_generating_set(labels):
    if isinstance(labels, (int, Integer)):
        return finite_ordered_set(range(int(labels)))
    if isinstance(labels, (tuple, list, range)):
        return finite_ordered_set(labels)
    return labels


@cached_function
def _owned_finite_free_module(ring, rank):
    r"""Return the owned rank-``rank`` free module over ``ring``."""
    return _SparseFreeModuleParent(
        ring,
        finite_ordered_set(range(int(rank))),
    )


@cached_function
def _owned_free_module_on(ring, module_generating_set):
    r"""Return the owned free module ``F_R(S)`` on the stated labels."""
    return _SparseFreeModuleParent(ring, module_generating_set)


def FreeModule(base_ring, rank_or_index_set):
    r"""Return the free module on a finite rank or an arbitrary index set."""
    from dzack_research.preamble.categories.rings.ring_foundation import OwnedRings

    ring = base_ring
    if ring not in OwnedRings():
        raise TypeError("FreeModule expects a preamble ring")
    if isinstance(rank_or_index_set, (int, Integer)):
        if rank_or_index_set < 0:
            raise ValueError("the rank of a free module is nonnegative")
        return _owned_finite_free_module(ring, rank_or_index_set)
    return _owned_free_module_on(ring, _module_generating_set(rank_or_index_set))


def MatrixSpace(base_ring, nrows, ncols=None):
    r"""Return ``Hom_R(F_R([n]), F_R([m]))`` for ``m=nrows``, ``n=ncols``."""
    ring = _owned_ring(base_ring)
    from sage.rings.integer_ring import ZZ as SageZZ
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
    from dzack_research.preamble.categories.modules.pure.modules import _refine_matrix_hom
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    integers = _own_ring(SageZZ)

    def dimension(value):
        if isinstance(value, int):
            result = value
        elif getattr(value, "parent", lambda: None)() is integers:
            result = int(value)
        else:
            raise TypeError("a matrix dimension is a nonnegative preamble integer")
        if result < 0:
            raise ValueError("matrix dimensions are nonnegative")
        return result

    nrows = dimension(nrows)
    ncols = nrows if ncols is None else dimension(ncols)
    source = FreeModule(ring, ncols)
    target = FreeModule(ring, nrows)
    return _refine_matrix_hom(module_homset(source, target))


def matrix_change_ring(matrix, ring):
    r"""Return the same finite coordinate matrix over ``ring``."""
    target = MatrixSpace(ring, matrix.parent().nrows(), matrix.parent().ncols())
    return target.from_rows(
        (
            ring(matrix.matrix_entry(row_label, column_label))
            for column_label in matrix.parent().column_index_set()
        )
        for row_label in matrix.parent().row_index_set()
    )


def FreeModuleOn(base_ring, module_generating_set):
    r"""Return \(F_R(S)\), retaining the actual labels in ``S``."""
    from dzack_research.preamble.categories.rings.ring_foundation import OwnedRings

    if base_ring not in OwnedRings():
        raise TypeError("FreeModuleOn expects a preamble ring")
    return _owned_free_module_on(
        base_ring,
        _module_generating_set(module_generating_set),
    )


def FreshFreeModuleOn(base_ring, module_generating_set):
    r"""Return a new free-module parent on the specified basis labels.

    Two different actions or forms on isomorphic free modules must remain
    different structured objects, so the owned parent is not interned; the
    engine underneath may be shared, since it holds no owned data.
    """
    from dzack_research.preamble.categories.rings.ring_foundation import OwnedRings

    ring = base_ring
    if ring not in OwnedRings():
        raise TypeError("FreshFreeModuleOn expects a preamble ring")
    labels = _module_generating_set(module_generating_set)
    return _SparseFreeModuleParent(ring, labels)


def BasedFreeModule(base_ring, rank_or_labels):
    r"""Return the selected based free module on a rank or explicit labels."""
    if isinstance(rank_or_labels, (int, Integer)):
        return FreeModule(base_ring, rank_or_labels)
    return FreeModuleOn(base_ring, rank_or_labels)


@cached_function
def ring_as_module(ring):
    r"""Return the canonical free rank-one module of a ring over itself."""
    result = _owned_ring(ring)
    if result in FinitelyGeneratedFreeModules(result):
        return result
    return BasedFreeModule(result, 1)
