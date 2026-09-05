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
    _engine_numeral,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_image,
    finite_ordered_set,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    BiproductModules,
    FinitelyGeneratedFreeModules,
    VectorSpaces,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    FinitelyPresentedModule,
)
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.modules.base_change import base_change_codomain
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    _solve_left_integrally,
    framing_morphism,
    module_coefficients,
    module_embedding,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    FreeModules,
    ModuleSubobjects,
    Modules,
    _refine_matrix_hom,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedFields,
    PrincipalIdealDomains,
    _own_ring,
)
from dzack_research.preamble.categories.sets.cardinals import (
    Cardinalities,
)
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def _finitely_generated_free_placement(ring, module_generating_set):
    r"""Return the owned categories of ``R^(S)``: finitely generated exactly when ``S`` is finite."""

    categories = [_SparseFramedFreeModules(ring)]
    if ring in OwnedFields():
        categories.append(VectorSpaces(ring))
    if module_generating_set.cardinality().is_finite():
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


class _SparseFreeModuleParent:
    """Construction methods for the owned free module on arbitrary labels."""

    def __init__(
        self,
        base_ring,
        module_generating_set,
        **rest,
    ) -> None:
        ring = _owned_ring(base_ring)
        labels = module_generating_set
        self._preamble_free_module_constructor = lambda new_labels, **options: FreshFreeModuleOn(
            ring,
            new_labels,
            **options,
        )
        super().__init__(
            base_ring=ring,
            module_generating_set=labels,
            module_generator_function=self._basis_element,
            **rest,
        )

    def _basis_element(self, label):
        labels = self._preamble_module_generating_set
        if label not in labels:
            raise ValueError(f"{label!r} is not a module-generator label")
        return self.element_class(self, {labels(label): self.base_ring().one()})

    def __call__(self, value):
        r"""Construct a free-module element through the owned coordinate syntax."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        if isinstance(value, _SparseFreeModuleElement) and value.parent() is self:
            return value
        if isinstance(value, dict):
            labels = self.module_generating_set()
            ring = self.base_ring()
            coefficients = {}
            for label, coefficient in value.items():
                if label not in labels:
                    raise ValueError(f"{label!r} is not a module-generator label")
                selected_label = labels(label) if callable(labels) else label
                coefficient = ring(coefficient)
                coefficients[selected_label] = (
                    coefficients.get(selected_label, ring.zero()) + coefficient
                )
            return self.element_class(self, coefficients)
        labels = self.module_generating_set()

        if isinstance(value, (tuple, list)):
            if not hasattr(labels, "unrank"):
                raise TypeError(
                    "coordinate sequence syntax requires an ordered enumerated framing"
                )
            cardinality = labels.cardinality()
            if not cardinality.is_finite():
                raise TypeError(
                    "coordinate sequence syntax requires a finite framing; "
                    "use label-keyed finite support for an infinite free module"
                )
            if len(value) != int(cardinality.finite_value()):
                raise ValueError("coordinate tuple has the wrong length")
            coefficients = {
                labels.unrank(position): coefficient
                for position, coefficient in enumerate(value)
                if coefficient != 0
            }
            return self.element_class(self, coefficients)
        if labels.cardinality().is_finite() and int(labels.cardinality().finite_value()) == 1:
            try:
                scalar = self.base_ring()(value)
            except (TypeError, ValueError):
                pass
            else:
                return self.element_class(
                    self,
                    {labels.unrank(0): scalar} if scalar != self.base_ring().zero() else {},
                )
        if value in labels:
            # A label is its basis element: the unit ``S -> F(S)`` of the
            # free-forgetful adjunction, as in Sage's
            # ``CombinatorialFreeModule._element_constructor_``.
            return self._basis_element(value)
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

    def _selected_module_coefficients(self, element):
        return self._element_constructor_(element).monomial_coefficients()

    def _repr_(self):
        return f"Free module on {self.module_generating_set()} over {self.base_ring()}"


class FramedFreeModules(OwnedCategoryOverBaseRing):
    r"""Free modules equipped with the canonical basis map."""

    def an_object(self):
        r"""The hyperbolic plane U, framed by its standard basis."""
        from dzack_research.preamble.categories.lattices import Lattices

        return Lattices(self.base_ring())("U")

    @classmethod
    def _repr_object_names(cls):
        return "framed free modules"

    def super_categories(self):

        return [FreeModules(self.base_ring()), FramedModules(self.base_ring())]

    class ParentMethods:
        def _fresh_free_module_on(self, labels, **options):
            constructor = self.__dict__.get("_preamble_free_module_constructor")
            if constructor is None:
                raise NotImplementedError(
                    "this free module has no selected fresh-parent constructor"
                )
            return constructor(labels, **options)

        def _represented_cokernel_of_morphism(self, morphism):
            if morphism.codomain() is not self:
                return NotImplemented
            return FinitelyPresentedModule(morphism, _cokernel_morphism=morphism)

        def _represented_annihilator_ideal(self):
            r"""Return the kernel ideal of the scalar action on a free module."""
            ring = self.base_ring()
            generator = ring.one() if self.rank() == 0 else ring.zero()
            return ring.ideal(generator)

        def _Hom_(self, codomain, category=None):

            if category is not None and not category.is_subcategory(Modules(self.base_ring())):
                raise TypeError("this is not a module homset category")
            if not hasattr(codomain, "module_generating_set"):
                raise TypeError("the parent-level module Hom constructor requires a framed target")

            return module_homset(self, codomain)

        def subobject_on(self, module_generating_set):
            r"""Return the submodule spanned by the specified elements."""

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

            return indexed_family(
                self.module_generating_set(),
                self.module_generator,
                name="Free-module generator family",
            )

        def framing_morphism(self):

            return framing_morphism(self, self, self.module_generator)

        def _free_biproduct_with(self, other, labels, factors):
            r"""Return the free biproduct realization when both factors are framed free."""
            if other not in FramedFreeModules(self.base_ring()):
                return NotImplemented
            return FreshFreeModuleOn(
                self.base_ring(),
                labels,
                _biproduct_factors=factors,
            )

        def rank(self):
            r"""Return the cardinality of the module generating set.

            A rank can be infinite -- \(R^{(\mathbb N)}\) has rank
            \(\aleph_0\) -- so the answer is a cardinal, not a natural
            number.  The cardinality is the generating set's own, which is
            where the doctrine puts it.
            """

            return self.module_generating_set().cardinality()

        def is_finite_rank(self) -> bool:
            return self.rank().is_finite()

        def is_torsion_free(self) -> bool:
            return True

        def cardinality(self):
            r"""Return ``|R^(S)|``: ``|R|^|S|`` for finite ``S``, else ``max(|R|, |S|)`` by finite support."""

            if self.base_ring() is self:
                # A ring as the rank-one free module over itself: its
                # underlying set is the ring's, which the ring level answers.
                return super().cardinality()
            scalars = self.base_ring().cardinality()
            labels = self.module_generating_set().cardinality()
            if labels.is_finite():
                return scalars**labels
            if scalars == Cardinalities().one():
                return Cardinalities().one()
            return Cardinalities().supremum(scalars, labels)

        def is_finite(self) -> bool:
            r"""Return whether the underlying free module is finite."""
            return self.cardinality().is_finite()

        def base_change(self, ring_map):
            r"""Return ``S tensor_R M`` along the specified ring map ``R -> S``."""

            target_ring = base_change_codomain(self, ring_map)
            return FreshFreeModuleOn(target_ring, self.module_generating_set())


class _SparseFramedFreeModules(OwnedCategoryOverBaseRing):
    r"""The private sparse-coordinate realization of a framed free module."""

    @classmethod
    def _repr_object_names(cls):
        return "sparse represented framed free modules"

    def super_categories(self):
        return [FramedFreeModules(self.base_ring())]

    ElementMethods = _SparseFreeModuleElement

    class ParentMethods(_SparseFreeModuleParent):
        pass


def _new_sparse_free_module(
    ring,
    labels,
    *,
    subobject_ambient=None,
    subobject_generator_images=None,
    subobject_lift=None,
    subobject_inclusion_factory=None,
    subobject_verify_linearity=True,
    biproduct_factors=None,
    extra_categories=(),
    extra_construction_data=None,
):
    r"""Build a sparse free module through the category constructor chain."""
    categories = _finitely_generated_free_placement(ring, labels)
    data = {
        "base_ring": ring,
        "module_generating_set": labels,
    }
    if subobject_ambient is not None or subobject_inclusion_factory is not None:
        categories.append(ModuleSubobjects(ring))
        data.update(
            subobject_ambient=subobject_ambient,
            subobject_generator_images=subobject_generator_images,
            subobject_lift=subobject_lift,
            subobject_inclusion_factory=subobject_inclusion_factory,
            subobject_verify_linearity=subobject_verify_linearity,
        )
    if biproduct_factors is not None:
        categories.append(BiproductModules(ring))
        data["biproduct_factors"] = biproduct_factors
    categories.extend(extra_categories)
    if extra_construction_data is not None:
        data.update(extra_construction_data)
    return object_of(Category.join(tuple(categories)), **data)



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

    if isinstance(module_generating_set, (tuple, list, range)):
        return finite_ordered_set(module_generating_set)
    try:
        size = module_generating_set.cardinality()
        finite = size.is_finite()
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        finite = False
    if not finite:
        raise TypeError(
            "subobject generators must be a known finite owned set/family or explicit finite literal"
        )
    return module_generating_set


def _finite_support_labels(module, elements):
    r"""Return the finite union of supports without ranking the ambient framing.

    This is a private finite-coordinate boundary.  The ambient framing may be
    infinite and need not admit a ranking map; only labels that actually occur
    in the supplied finite family are retained.
    """
    support = []
    for candidate in elements:
        element = candidate if candidate.parent() is module else module(candidate)
        for label in module_coefficients(element, module):
            if not any(label == known for known in support):
                support.append(label)
    return finite_ordered_set(support)


def _span_basis_elements(module, module_generating_set):
    r"""Return the canonical span basis using only the finite union of supports."""

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
    support_labels = _finite_support_labels(module, generators)

    # Private finite backend serialization.  Only the finite support window is
    # materialized; the ambient framing itself is never enumerated.
    engine = _engine_ring(ring)
    support_count = int(support_labels.cardinality())
    free = _SageFreeModule(engine, support_count)
    engine_rows = []
    for candidate in generators:
        element = candidate if candidate.parent() is module else module(candidate)
        coefficients = module_coefficients(element, module)
        engine_rows.append(
            [
                _engine_element(
                    ring,
                    coefficients.get(support_labels.unrank(position), ring.zero()),
                )
                for position in range(support_count)
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
                support_labels.unrank(column): ring._from_engine_element(row[column])
                for column in range(support_count)
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


@cached_function(key=lambda module, basis: (id(module), tuple(basis)))
def _module_subobject_spanning(module, basis):
    r"""Return the subobject on its canonical owned finite span basis.

    Ambient identity is part of the subobject type.  Do not use Sage's generic
    cached-function key here: equal free-module parents need not be identical
    mathematical endpoints.
    """

    return _module_subobject_spanning_with_structure(module, basis)


def _module_subobject_spanning_with_structure(
    module,
    basis,
    *,
    extra_categories=(),
    extra_construction_data=None,
):
    r"""Construct a span, optionally in additional structural categories."""
    ring = module.base_ring()
    labels, embedded, lift_from_finite_support = _module_subobject_constructor_data(
        module,
        basis,
    )
    return _new_sparse_free_module(
        ring,
        labels,
        subobject_ambient=module,
        subobject_generator_images=embedded,
        subobject_lift=lift_from_finite_support,
        extra_categories=extra_categories,
        extra_construction_data=extra_construction_data,
    )


def _module_subobject_constructor_data(module, basis):
    r"""Return labels, generator images, and lift data for a finite span."""

    ring = module.base_ring()
    if module not in FramedFreeModules(ring):
        raise NotImplementedError(
            "the active submodule basis engine constructs subobjects of framed free modules"
        )
    labels = Sets.Δ[int(basis.cardinality()) - 1]

    def embedded(label):
        return basis.unrank(int(label))

    support_labels = _finite_support_labels(module, basis)
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

    def lift_from_finite_support(source, element):
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

    return labels, embedded, lift_from_finite_support



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
    integers = _own_ring(SageZZ)
    parent = getattr(labels, "parent", lambda: None)()
    if isinstance(labels, (int, Integer)) or parent is integers:
        rank = int(_engine_numeral(SageZZ, labels))
        if rank < 0:
            raise ValueError("the rank of a free module is nonnegative")
        return Sets.Δ[rank - 1]
    if isinstance(labels, (tuple, list, range)):
        return finite_ordered_set(labels)
    return labels


@cached_function
def _owned_free_module_on(ring, module_generating_set):
    r"""Return the owned free module ``F_R(S)`` on the stated labels."""
    return _new_sparse_free_module(ring, module_generating_set)


def FreeModule(base_ring, rank_or_index_set):
    r"""Return the free module on a finite rank or an arbitrary index set."""

    ring = base_ring
    if ring not in OwnedRings():
        raise TypeError("FreeModule expects a preamble ring")
    return _owned_free_module_on(ring, _module_generating_set(rank_or_index_set))


def MatrixSpace(base_ring, nrows, ncols=None):
    r"""Return ``Hom_R(F_R([n]), F_R([m]))`` for ``m=nrows``, ``n=ncols``."""
    ring = _owned_ring(base_ring)
    from sage.rings.integer_ring import ZZ as SageZZ

    integers = _own_ring(SageZZ)

    def dimension(value):
        if isinstance(value, int):
            result = value
        elif value in integers:
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

    if base_ring not in OwnedRings():
        raise TypeError("FreeModuleOn expects a preamble ring")
    return _owned_free_module_on(
        base_ring,
        _module_generating_set(module_generating_set),
    )


def FreshFreeModuleOn(
    base_ring,
    module_generating_set,
    *,
    _subobject_ambient=None,
    _subobject_generator_images=None,
    _subobject_lift=None,
    _subobject_inclusion_factory=None,
    _subobject_verify_linearity=True,
    _biproduct_factors=None,
    _extra_categories=(),
    _extra_construction_data=None,
):
    r"""Return a new free-module parent on the specified basis labels.

    Two different actions or forms on isomorphic free modules must remain
    different structured objects, so the owned parent is not interned; the
    engine underneath may be shared, since it holds no owned data.
    """

    ring = base_ring
    if ring not in OwnedRings():
        raise TypeError("FreshFreeModuleOn expects a preamble ring")
    labels = _module_generating_set(module_generating_set)
    return _new_sparse_free_module(
        ring,
        labels,
        subobject_ambient=_subobject_ambient,
        subobject_generator_images=_subobject_generator_images,
        subobject_lift=_subobject_lift,
        subobject_inclusion_factory=_subobject_inclusion_factory,
        subobject_verify_linearity=_subobject_verify_linearity,
        biproduct_factors=_biproduct_factors,
        extra_categories=_extra_categories,
        extra_construction_data=_extra_construction_data,
    )


def BasedFreeModule(base_ring, rank_or_labels):
    r"""Return the selected based free module on a rank or explicit labels."""
    return FreeModule(base_ring, rank_or_labels)


@cached_function
def ring_as_module(ring):
    r"""Return the canonical free rank-one module of a ring over itself."""
    result = _owned_ring(ring)
    if result in FinitelyGeneratedFreeModules(result):
        return result
    return BasedFreeModule(result, 1)
