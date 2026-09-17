"""Free modules with their canonical framing."""

from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.misc.repr import repr_lincomb
from sage.modules.free_module import FreeModule as _SageFreeModule
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import ModuleElement
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.modules.base_change import _base_change_codomain
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    _presented_module_from_morphism,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    _solve_left_integrally,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    BiproductModules,
    FramedModules,
    FreeResolution,
    Modules,
    ModuleSubobjects,
    ModulesWithChosenFinitePresentation,
    VectorSpaces,
    _refine_matrix_hom,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    IntegralDomains,
    OwnedCategoryOverBaseRing,
    OwnedFields,
    OwnedRings,
    PrincipalIdealDomains,
    _engine_element,
    _engine_numeral,
    _engine_ring,
    _own_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.cardinals import (
    Cardinalities,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import EnumeratedSets, Sets
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom


def _finitely_generated_free_placement(ring, module_generating_set):
    r"""Return the owned categories of ``R^(S)``: finitely generated exactly when ``S`` is finite."""

    categories = [_SparseFramedFreeModules(ring)]
    if ring in OwnedFields():
        categories.append(VectorSpaces(ring))
    assert module_generating_set in Sets(), (
        "a free module is constructed on an owned set of labels"
    )
    if module_generating_set.cardinality().is_finite():
        categories.append(FramedFreeModules(ring).FinitelyGenerated())
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

    def __iter__(self):
        r"""Iterate coordinates when the selected framing is finite and ordered."""
        labels = self.parent().module_generating_set()
        match (labels in EnumeratedSets(), labels.cardinality().is_finite()):
            case (True, True):
                zero = self.parent().base_ring().zero()
                return (self._coefficients.get(label, zero) for label in labels)
            case _:
                raise TypeError(
                    "coordinate iteration requires a finite ordered module framing"
                )

    def underlying_set_element(self):
        r"""Recover ``s`` when this is the canonical free generator ``[s]``.

        This is the inverse of the unit ``S -> U(F_R(S))`` on its image.  A
        general linear combination has no distinguished underlying element of
        ``S`` and therefore refuses rather than selecting one support label.
        """
        if len(self._coefficients) != 1:
            raise ValueError(
                "only a canonical free generator has one underlying framing element"
            )
        label, coefficient = next(iter(self._coefficients.items()))
        if coefficient != self.parent().base_ring().one():
            raise ValueError(
                "only a canonical free generator has one underlying framing element"
            )
        return label

    def _add_(self, other):
        ring = self.parent().base_ring()
        coefficients = dict(self._coefficients)
        for label, coefficient in other._coefficients.items():
            value = coefficients.get(label, ring.zero()) + coefficient
            if value == ring.zero():
                coefficients.pop(label, None)
            else:
                coefficients[label] = value
        return self.parent().element_class(self.parent(), coefficients)

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
        r"""Multiply in the algebra this free module underlies, else scale on the right."""
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        module = self.parent()
        ring = module.base_ring()
        match other:
            case _ if element_parent(other) is module and module in Algebras(ring):
                return self._mul_(other)
            case _ if other in ring:
                return module.scalar_multiple(other, self)
            case _:
                return NotImplemented

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = other._coefficients == self._coefficients
        return equal if op == op_EQ else not equal

    def __hash__(self):
        return hash((id(self.parent()), frozenset(self._coefficients.items())))

    def _repr_(self):
        return repr_lincomb(
            self._coefficients.items(),
            repr_monomial=lambda label: f"[{label}]",
            strip_one=True,
        )

    def _latex_(self):
        return repr_lincomb(
            self._coefficients.items(),
            repr_monomial=lambda label: rf"\left[{latex(label)}\right]",
            is_latex=True,
            strip_one=True,
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
        # The free module ``F_R(S)`` is constructed on the set ``S``: that set
        # is this level's datum, and the framing it declares is the identity
        # of ``F_R(S)`` read on its basis.
        self._module_generating_set = module_generating_set
        super().__init__(
            base_ring=ring,
            module_generating_set=module_generating_set,
            module_generator_function=self._basis_element,
            framing_source=self,
            **rest,
        )

    def _basis_element(self, label):
        labels = self._module_generating_set
        assert label in labels, f"{label!r} is not a module-generator label"
        return self.element_class(self, {labels(label): self.base_ring().one()})

    def module_generating_set(self):
        r"""Return the set ``S`` this free module ``F_R(S)`` is constructed on."""
        return self._module_generating_set

    def module_generator(self, label):
        r"""Return the sparse basis element selected by this identity framing."""
        return self._basis_element(label)

    @cached_method
    def module_generators(self):
        r"""Return the image of the sparse free-basis unit as an owned set."""
        return Sets().image_set(
            self.module_generator_morphism(),
            self.module_generating_set(),
            is_injective=True,
            inverse=lambda generator: self(generator).underlying_set_element(),
        )

    def __call__(self, value):
        r"""Construct a free-module element through the owned coordinate syntax."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        labels = self.module_generating_set()
        ring = self.base_ring()
        source = element_parent(value)
        match value:
            case _ if source is self:
                return value
            case _ if isinstance(source, Parent) and self._built_on_the_same_data(source):
                return self._element_on_the_same_data(source, value)
            case dict():
                coefficients = {}
                for label, coefficient in value.items():
                    if label not in labels:
                        raise ValueError(f"{label!r} is not a module-generator label")
                    selected_label = labels(label)
                    coefficient = ring(coefficient)
                    coefficients[selected_label] = (
                        coefficients.get(selected_label, ring.zero()) + coefficient
                    )
                return self.element_class(self, coefficients)
            case tuple() | list():
                if labels not in EnumeratedSets():
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
                    labels[position]: coefficient
                    for position, coefficient in enumerate(value)
                    if coefficient != 0
                }
                return self.element_class(self, coefficients)
            # Sequence inputs are coordinate syntax, never candidate scalars.
            # Only after the structured ingress cases may a free module ask
            # whether the input is a scalar of its base ring.
            case _ if value in ring and ring(value) == ring.zero():
                return self.zero()
            case _ if value in ring and labels.cardinality() == cardinal(1):
                return self.element_class(self, {labels[0]: ring(value)})
            case _ if value in labels:
                # A label is its basis element: the unit ``S -> F(S)`` of the
                # free-forgetful adjunction, as in Sage's
                # ``CombinatorialFreeModule._element_constructor_``.
                return self._basis_element(value)
            case _:
                raise TypeError(f"{value!r} does not describe an element of {self}")

    def zero(self):
        return self.element_class(self, {})

    def an_element(self):
        labels = self.module_generating_set()
        if labels.cardinality() == cardinal(0):
            return self.zero()
        return self._basis_element(labels.an_element())

    def _raw_scalar_multiple(self, scalar, element):
        ring = self.base_ring()
        scalar = ring(scalar)
        element = self._element_constructor_(element)
        return self.element_class(
            self,
            {
                label: scalar * coefficient
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

        return [Modules(self.base_ring()).Free(), FramedModules(self.base_ring())]

    class ParentMethods:
        def _fresh_free_module_on(self, labels, **options):
            r"""Return a new free module on ``labels`` over this module's ring.

            Protected contract of framed free modules: constructions that build
            sibling free modules (covers, relation modules, matrix units) ask
            the free module they start from, so the new module is over the same
            ring.
            """
            return _fresh_free_module_on(self.base_ring(), labels, **options)

        def _represented_cokernel_of_morphism(self, morphism):
            if morphism.codomain() is not self:
                return NotImplemented
            return _presented_module_from_morphism(morphism, _cokernel_morphism=morphism)

        def _represented_annihilator_ideal(self):
            r"""Return the kernel ideal of the scalar action on a free module."""
            ring = self.base_ring()
            generator = ring.one() if self.module_rank() == 0 else ring.zero()
            return ring.ideal(generator)

        def _Hom_(self, codomain, category=None):

            if category is not None and not category.is_subcategory(Modules(self.base_ring())):
                raise TypeError("this is not a module homset category")
            if not hasattr(codomain, "module_generating_set"):
                raise TypeError("the parent-level module Hom constructor requires a framed target")

            return self.module_category().Mor(self, codomain)

        def subobject_on(self, module_generating_set):
            r"""Return the submodule spanned by the specified elements."""

            return _module_subobject_on(self, module_generating_set)

        def whole_subobject(self):
            r"""Return this free module as the full subobject of itself.

            The selected framing is already a basis, so this construction does
            not ask a backend to row-reduce it.  That distinction is essential
            over exact local PIDs, where echelon normalization can divide by a
            nonunit even though the whole-span basis is already known.
            """

            return _module_subobject_spanning(self, self.module_generators())

        def diagonal_gram(self, exceptions, default=1):
            r"""Return the diagonal type-``(0,2)`` tensor in this selected basis."""
            from dzack_research.preamble.categories._lattice import _diagonal_gram

            return _diagonal_gram(self, exceptions, default)

        def _free_biproduct_over(
            self,
            labels,
            factors,
            *,
            extra_categories=(),
            extra_construction_data=None,
        ):
            r"""Return the free biproduct realization when every factor is framed free."""
            free = FramedFreeModules(self.base_ring())
            if not all(factor in free for factor in factors):
                return NotImplemented
            return self.base_ring()._fresh_free_module_on(
                labels,
                _biproduct_factors=factors,
                _extra_categories=extra_categories,
                _extra_construction_data=extra_construction_data,
            )

        def module_rank(self):
            r"""Return the cardinality of the module generating set.

            A rank can be infinite -- \(R^{(\mathbb N)}\) has rank
            \(\aleph_0\) -- so the answer is a cardinal, not a natural
            number.  The cardinality is the generating set's own, which is
            where the doctrine puts it.
            """

            return self.module_generating_set().cardinality()

        def is_torsion_free(self) -> bool:
            r"""A free module over a domain is torsion-free.

            A basis element is killed only by a scalar killing its coefficient,
            and a domain has none nonzero.  Off a domain there is no fraction
            field and hence no torsion submodule to be zero, so the question is
            not asked rather than answered ``True``.
            """
            assert self.base_ring() in IntegralDomains(), (
                f"torsion-freeness of a module over {self.base_ring()} needs an integral-domain base"
            )
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

        def base_change(self, ring_map, *, _extra_construction_data=None):
            r"""Return ``S tensor_R M`` along the specified ring map ``R -> S``."""

            target_ring = _base_change_codomain(self, ring_map)
            return target_ring._fresh_free_module_on(
                self.module_generating_set(),
                _extra_construction_data=_extra_construction_data,
            )

        @cached_method
        def vector_space(self):
            r"""Return ``M tensor_R Frac(R)`` along the canonical fraction-field map.

            This is the archived ``vector_space`` construction: rationalization
            is scalar extension, not a separately presented copy.  Structured
            refinements such as formed modules inherit this method and dispatch
            through their own ``base_change``, so the carried structure is
            transported by the same canonical ring map.
            """
            return self.base_change(self.base_ring().fraction_field_map())

    class FinitelyGenerated(CategoryWithAxiom):
        r"""Free modules framed by a finite basis."""

        def an_object(self):
            r"""The free module of rank one."""
            return self.base_ring().free_module(1)

        def extra_super_categories(self):
            return [ModulesWithChosenFinitePresentation(self.base_ring())]

        def kernel_arrow_functor(self):
            r"""Return the kernel functor on the finite-free arrow category."""
            from dzack_research.preamble.categories.functors.linear_constructions import (
                _kernel_arrow_functor,
            )

            return _kernel_arrow_functor(self.base_ring())

        class ParentMethods:
            def _represented_vector_space_dimension(self):
                return self.module_rank()

            def _represented_vector_space_basis_generator_labels(self):
                return self.module_generating_set()

            def is_zero(self) -> bool:
                r"""Return whether this finite free module is the zero module.

                A finite free module is zero exactly when every vector in its
                chosen basis is the additive identity; this also handles the zero
                coefficient ring without replacing the basis by a rank heuristic.
                """
                return all(generator == self.zero() for generator in self.module_generators())

            def _selected_presentation_rows(self):
                return ()

            def fitting_ideal(self, index):
                r"""Return ``Fitt_i(R^n)``: zero below the rank, the unit ideal from it on.

                A free module is presented by no relations, so its relation matrix
                has no rows and the ideal of its ``(n - i)``-minors is zero while a
                minor of positive size is asked for and the unit ideal once none
                is.  The general minor computation has no matrix to read here, so
                the same formula is stated directly.
                """
                ring = self.base_ring()
                rank = int(self.number_of_module_generators())
                return ring.ideal(ring.one() if int(index) >= rank else ring.zero())

            def _represented_kernel_of_morphism(self, morphism):
                if morphism.domain() is not self:
                    return NotImplemented
                try:
                    codomain_is_zero = morphism.codomain().is_zero()
                except NotImplementedError:
                    codomain_is_zero = False
                if codomain_is_zero:
                    return self.whole_subobject()
                try:
                    coordinate_matrix = morphism.matrix()
                    coordinate_generators = coordinate_matrix._kernel_spanning_family()
                except (AttributeError, NotImplementedError):
                    return NotImplemented

                source_labels = tuple(self.module_generating_set())
                coordinate_domain = coordinate_matrix.domain()
                coordinate_labels = tuple(coordinate_domain.module_generating_set())
                if len(source_labels) != len(coordinate_labels):
                    raise ArithmeticError(
                        "the coordinate kernel changed the source framing rank"
                    )

                def transport(coordinate_vector):
                    coefficients = coordinate_domain.framing_coefficients(coordinate_vector)
                    return self.linear_combination(
                        {
                            source_label: coefficients[coordinate_label]
                            for source_label, coordinate_label in zip(
                                source_labels, coordinate_labels, strict=True
                            )
                            if coordinate_label in coefficients
                        }
                    )

                generators = finite_indexed_family(
                    coordinate_generators.index_set(),
                    lambda index: transport(coordinate_generators[index]),
                    name=f"Kernel spanning family in {self}",
                )
                return self.subobject_on(generators)

            def _same_presentation_module(
                self,
                labels,
                *,
                _extra_categories=(),
                _extra_construction_data=None,
            ):
                return self._fresh_free_module_on(
                    labels,
                    _extra_categories=tuple(_extra_categories),
                    _extra_construction_data=_extra_construction_data,
                )

            def free_resolution(self, steps=None):
                r"""A free module is its own resolution, in degree zero alone.

                The number of steps a caller is willing to compute does not enter:
                the identity already resolves a free module, so the same resolution
                answers however far it is asked to go.
                """
                _ = steps
                return self._identity_resolution()

            @cached_method
            def _identity_resolution(self):
                zero = self._fresh_free_module_on(finite_ordered_set(()))
                degrees = Sets.Δ[0]
                return FreeResolution(
                    self,
                    degrees,
                    indexed_family(degrees, lambda degree: self, name="Free resolution terms"),
                    indexed_family(
                        Sets.Δ[-1],
                        lambda degree: None,
                        name="Free resolution differentials",
                    ),
                    self.module_category().Mor(self, self).identity(),
                    zero,
                )

            @cached_method
            def dual_module(self):
                return self._fresh_free_module_on(self.module_generating_set())


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
    return _object_of(Cat().meet(tuple(categories)), **data)



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

    match module_generating_set:
        case tuple() | list() | range():
            return finite_ordered_set(module_generating_set)
        case _:
            assert (
                module_generating_set in Sets()
                and module_generating_set.cardinality().is_finite()
            ), "subobject generators are a finite owned set or an explicit finite family"
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
        for label in module.framing_coefficients(element):
            if not any(label == known for known in support):
                support.append(label)
    return finite_ordered_set(support)


def _span_basis_elements(module, module_generating_set):
    r"""Return the canonical span basis using only the finite union of supports."""

    ring = module.base_ring()
    assert ring in PrincipalIdealDomains(), (
        "the represented finite submodule basis is computed over a principal ideal domain"
    )
    assert module in FramedFreeModules(ring), (
        "the represented submodule basis is computed in a framed free ambient module"
    )

    generators = _known_finite_generator_family(module_generating_set)
    if int(generators.cardinality()) == 1:
        generator = next(iter(generators))
        generator = generator if generator.parent() is module else module(generator)
        if generator != module.zero():
            # Over a PID, hence an integral domain, one nonzero vector is
            # automatically a basis of the cyclic submodule it generates.
            # Retain that mathematical basis instead of echelon-normalizing it;
            # p-adic backends otherwise divide through nonunit pivots.
            return finite_ordered_set((generator,))
    support_labels = _finite_support_labels(module, generators)

    # Private finite backend serialization.  Only the finite support window is
    # materialized; the ambient framing itself is never enumerated.
    engine = _engine_ring(ring)
    support_count = int(support_labels.cardinality())
    free = _SageFreeModule(engine, support_count)
    engine_rows = []
    for candidate in generators:
        element = candidate if candidate.parent() is module else module(candidate)
        coefficients = module.framing_coefficients(element)
        engine_rows.append(
            [
                _engine_element(
                    ring,
                    coefficients.get(support_labels[position], ring.zero()),
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
                support_labels[column]: ring._from_engine_element(row[column])
                for column in range(support_count)
                if row[column]
            }
        )

    return FiniteOrderedSets().from_indexed(
        positions,
        basis_element,
        name=f"Canonical span basis in {module}",
    )


def _module_subobject_on(module, module_generating_set):
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
    assert module in FramedFreeModules(ring), (
        "the represented submodule basis constructs subobjects of framed free modules"
    )
    labels = Sets.Δ[int(basis.cardinality()) - 1]

    def embedded(label):
        return basis[int(label)]

    support_labels = _finite_support_labels(module, basis)
    source_rank = int(basis.cardinality())
    support_rank_count = int(support_labels.cardinality())
    if source_rank:
        coordinate_matrix = ring.matrix_space(source_rank, support_rank_count).from_rows(
            tuple(
                tuple(
                    module.framing_coefficients(basis[i]).get(
                        support_labels[j],
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
        r"""The preimage of ``element`` in the span, or ``None`` when ``element`` is outside it."""
        element = element if element.parent() is module else module(element)
        coefficients = module.framing_coefficients(element)
        if any(label not in support_labels for label in coefficients):
            return None
        if source_rank == 0:
            return None if coefficients else source.zero()
        solution = _solve_left_integrally(
            coordinate_matrix,
            (
                coefficients.get(support_labels[j], ring.zero())
                for j in range(support_rank_count)
            ),
            ring,
        )
        if solution is None:
            return None
        return source.linear_combination(
            {
                labels[i]: coefficient
                for i, coefficient in enumerate(solution)
                if coefficient
            }
        )

    return labels, embedded, lift_from_finite_support




def _module_generating_set(labels):
    r"""Read the labels a free module is constructed on.

    A rank ``n`` names the ordinal ``{0, ..., n-1}``; an explicit finite
    family of labels names the ordered set of them; an owned set is its own
    label set.
    """
    integers = _own_ring(SageZZ)
    match labels:
        case int() | Integer():
            rank = int(labels)
        case _ if element_parent(labels) is integers:
            rank = int(labels)
        case tuple() | list() | range():
            return finite_ordered_set(labels)
        case _:
            assert labels in Sets(), (
                "a free module is constructed on a rank or an owned set of labels"
            )
            return labels
    assert rank >= 0, "the rank of a free module is nonnegative"
    return Sets.Δ[rank - 1]


@cached_function
def _owned_free_module_on(ring, module_generating_set):
    r"""Return the owned free module ``F_R(S)`` on the stated labels."""
    return _new_sparse_free_module(ring, module_generating_set)


def _matrix_space(base_ring, nrows, ncols=None):
    r"""Return ``Hom_R(F_R([n]), F_R([m]))`` for ``m=nrows``, ``n=ncols``."""
    ring = _owned_ring(base_ring)
    integers = _own_ring(SageZZ)

    def dimension(value):
        result = int(integers(value))
        assert result >= 0, "matrix dimensions are nonnegative"
        return result

    nrows = dimension(nrows)
    ncols = nrows if ncols is None else dimension(ncols)
    source = ring.free_module(ncols)
    target = ring.free_module(nrows)
    return _refine_matrix_hom(source.module_category().Mor(source, target))


def _fresh_free_module_on(
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
        raise TypeError("fresh free-module construction expects a preamble ring")
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
