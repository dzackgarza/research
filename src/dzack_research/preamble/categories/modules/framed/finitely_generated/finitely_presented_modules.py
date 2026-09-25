"""Finitely presented modules with a selected finite presentation.

A presented module is an owned parent.  Over a PID with a Smith form its
engine is Sage's FGP module over the engine ring; over another Sage ring it
holds a Sage free cover and relation submodule; over a ring with no Sage
engine it holds the owned free cover alone and cannot decide equality.  The
engine is read through the selected-presentation backend method ``_smith_engine``
and every Smith-form computation is an explicit crossing into it.
"""

from sage.misc.cachefunc import cached_method
from sage.misc.misc_c import prod
from sage.misc.repr import repr_lincomb
from sage.misc.unknown import Unknown
from sage.all import PolynomialRing as _SagePolynomialRing
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import ModuleElement
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.objects import (
    _fix_selected_resolution,
)
from dzack_research.preamble.categories.modules.base_change import _base_change_scalar
from dzack_research.preamble.categories.modules.pure.modules import (
    BiproductModules,
    FreeResolution,
    Modules,
    ModuleSubobjects,
    ModulesWithChosenFinitePresentation,
    VectorSpaces,
    _biproduct_label,
    _engine_matrix,
    _require_matrix_mor,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    LocalRings,
    OwnedCategoryOverBaseRing,
    OwnedFields,
    OwnedIntegralDomains,
    PrincipalIdealDomains,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.cardinals import Cardinalities, cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    SetInclusion,
    Sets,
)
from dzack_research.preamble.owned_category import _object_of


def _canonical_pid_associate(ring, element):
    r"""Return the selected canonical associate of a PID scalar when available.

    Invariant factors classify cyclic summands by principal ideals, so replacing
    ``d`` by a unit multiple must not change their public representative.  Sage's
    exact PID engines already choose a canonical associate (positive over
    ``ZZ``, monic over polynomial PIDs); cross that choice back through the ring
    owner rather than reimplementing a ring-specific sign/unit convention.

    Engine adapter (``OWN-06``): its caller is the invariant-factor reading of
    a presented module over a PID; it asks the computation element for Sage's
    ``canonical_associate``, which an engine PID either implements or does
    not, and raises the associate through the owned ring.
    """
    element = ring(element)
    if element == ring.zero():
        return element
    if ring in LocalizationRings():
        source = ring.localization_source()
        if source in PrincipalIdealDomains():
            # A denominator in the localization submonoid is a unit, so
            # (a/s) and a generate the same principal ideal in S^{-1}R.
            # Canonicalize in the source PID rather than in the localization's
            # fraction-field engine, where every nonzero scalar is a unit.
            return ring.localization_map()(
                _canonical_pid_associate(source, element.numerator())
            )
    backend = _engine_element(ring, element)
    canonical_associate = getattr(backend, "canonical_associate", None)
    if canonical_associate is None:
        return element
    canonical, unit = canonical_associate()
    owned_canonical = _owned_engine_element(ring, canonical)
    owned_unit = _owned_engine_element(ring, unit)
    if not owned_unit.is_unit() or owned_canonical * owned_unit != element:
        return element
    return owned_canonical


def _finite_generating_family(module_generators):
    r"""Read a finite generating family: an indexed family, or finitely many elements indexed by position.

    The ingress of the subobject constructions: an ``IndexedFamily`` is not an
    object of an owned category, so a family given as one is recognized by its
    class, and any other finite collection is indexed by the ordinal of its
    positions.
    """
    if isinstance(module_generators, IndexedFamily):
        assert module_generators.index_set().cardinality().is_finite(), (
            f"cannot form a finitely generated submodule from {module_generators}: "
            "it is indexed by an infinite set"
        )
        return module_generators
    generators = finite_ordered_set(module_generators)
    positions = Sets.Δ[int(generators.cardinality()) - 1]
    return finite_indexed_family(
        positions,
        lambda position: generators[int(position)],
        name="Generating family",
    )


def _cover_free_module(module, labels):
    r"""Return a new free module on ``labels`` over the ring of ``module``.

    The covers, relation modules and normalized presentations a presented
    module builds are free modules over its own ring.
    """
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        _fresh_free_module_on,
    )

    return _fresh_free_module_on(_owned_ring(module.base_ring()), labels)


def _matrix_space_like(module, nrows, ncols):
    r"""Return ``Hom_R(R^ncols, R^nrows)`` on fresh free modules over the ring of ``module``."""
    source = _cover_free_module(module, Sets.Δ[int(ncols) - 1])
    target = _cover_free_module(module, Sets.Δ[int(nrows) - 1])

    return source.module_category().Mor(source, target)


class _SelectedModulePresentationBackend:
    r"""Coordinate/backend data derived from one selected module resolution."""

    def __init__(self, base_ring, relation_matrix, presentation, cokernel_morphism=None) -> None:
        if presentation.domain().base_ring() is not base_ring or presentation.codomain().base_ring() is not base_ring:
            raise ValueError(
                f"the relation map {presentation} must be a map of free {base_ring}-modules, "
                f"but its domain and codomain are over {presentation.domain().base_ring()} "
                f"and {presentation.codomain().base_ring()}"
            )
        if not presentation.domain().module_generating_set().cardinality().is_finite():
            raise ValueError(
                f"the module presented by {presentation} is not finitely presented: "
                "it has infinitely many relations"
            )
        if not presentation.codomain().module_generating_set().cardinality().is_finite():
            raise ValueError(
                f"the module presented by {presentation} is not finitely presented: "
                "it has infinitely many generators"
            )
        rows = relation_matrix.parent().row_index_set().cardinality()
        columns = relation_matrix.parent().column_index_set().cardinality()
        if rows != presentation.domain().module_generating_set().cardinality():
            raise ValueError(
                f"the relation matrix of {presentation} has {rows} rows, but there are "
                f"{presentation.domain().module_generating_set().cardinality()} relations"
            )
        if columns != presentation.codomain().module_generating_set().cardinality():
            raise ValueError(
                f"the relation matrix of {presentation} has {columns} columns, but there are "
                f"{presentation.codomain().module_generating_set().cardinality()} generators"
            )
        target_labels = presentation.codomain().module_generating_set()
        for relation_label, row in zip(
            presentation.domain().module_generating_set(),
            _matrix_coordinate_rows(relation_matrix),
            strict=True,
        ):
            represented = presentation.codomain().linear_combination(
                {
                    target_label: coefficient
                    for target_label, coefficient in zip(target_labels, row, strict=True)
                    if coefficient
                }
            )
            if presentation(presentation.domain().module_generator(relation_label)) != represented:
                raise ValueError(
                    f"the relation matrix does not agree with {presentation}: relation "
                    f"{relation_label!r} maps to {presentation(presentation.domain().module_generator(relation_label))}, "
                    f"but its matrix row gives {represented}"
                )
        self._relation_matrix = relation_matrix
        self._cokernel_morphism = cokernel_morphism

    def relation_matrix(self):
        return self._relation_matrix

    def cokernel_morphism(self):
        return self._cokernel_morphism


def _fix_selected_module_presentation(module, base_ring, relation_matrix, presentation, cokernel_morphism=None) -> None:
    r"""Promote the selected module resolution to the chosen finite presentation.

    The relation matrix and optional source cokernel morphism are retained only
    as computational backend data.  The mathematical presentation itself is
    the truncation-one resolution stored by ``Objects`` relative to ``R-Mod``.
    """
    if module._selected_module_presentation is not None:
        raise ValueError(f"{module} already has chosen generators and relations; they are fixed once")
    degree_zero = module.selected_module_resolution()
    match degree_zero.truncation():
        case 0:
            pass
        case _:
            raise ValueError(
                f"{module} already carries a selected module resolution through degree "
                f"{degree_zero.truncation()}; its finite presentation cannot be fixed a second time"
            )
    match degree_zero.level(0) is presentation.codomain():
        case False:
            raise ValueError(
                f"the relation map of {module} must land in its selected degree-zero free module "
                f"{degree_zero.level(0)}, but it lands in {presentation.codomain()}"
            )
        case True:
            pass
    resolution_category = Modules(base_ring).FinitelyPresented().resolution_category()

    def selected_resolution():
        return resolution_category.selected_presentation(
            module,
            presentation,
            degree_zero.augmentation(),
            generating_set=degree_zero.generating_set(),
            generator_morphism=degree_zero.generator_morphism(),
        )

    _fix_selected_resolution(
        module,
        Modules(base_ring),
        selected_resolution,
        replace=True,
    )
    module._selected_module_presentation = _SelectedModulePresentationBackend(
        base_ring,
        relation_matrix,
        presentation,
        cokernel_morphism,
    )


def _fix_lazy_selected_module_presentation(module, base_ring, realization_factory) -> None:
    r"""Fix one endpoint-determined finite presentation without realizing it.

    The factory is selected during construction but is not evaluated until the
    chosen module resolution is first read.  It returns the relation matrix,
    relation morphism, generating set and generator morphism of that fixed
    presentation.  Thus the mathematical choice is made before exposure while
    its computational model remains lazy.
    """
    match module._selected_module_presentation:
        case None:
            pass
        case _:
            raise ValueError(
                f"{module} already has chosen generators and relations; they are fixed once"
            )
    match callable(realization_factory):
        case True:
            pass
        case False:
            raise TypeError(
                f"a lazy selected presentation needs a zero-argument construction, "
                f"but {realization_factory!r} is not callable"
            )

    resolution_category = Modules(base_ring).FinitelyPresented().resolution_category()

    def selected_resolution():
        relation_matrix, presentation, generating_set, generator_morphism = realization_factory()
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            _framing_morphism,
        )

        backend = _SelectedModulePresentationBackend(
            base_ring,
            relation_matrix,
            presentation,
        )
        augmentation = _framing_morphism(
            module,
            presentation.codomain(),
            generator_morphism,
        )
        resolution = resolution_category.selected_presentation(
            module,
            presentation,
            augmentation,
            generating_set=generating_set,
            generator_morphism=generator_morphism,
        )
        module._selected_module_presentation = backend
        return resolution

    _fix_selected_resolution(
        module,
        Modules(base_ring),
        selected_resolution,
    )


class _SelectedFinitePresentationModules(OwnedCategoryOverBaseRing):
    r"""Implementation refinement for modules with a selected finite presentation."""

    @classmethod
    def _repr_object_names(cls):
        return "modules with a represented selected finite-presentation backend"

    def super_categories(self):
        return [ModulesWithChosenFinitePresentation(self.base_ring())]

    class ParentMethods:
        def _smith_engine(self):
            r"""The optional native FGP realization of these selected data.

            A selected presentation alone is not an FGP workspace.  Its
            private quotient engine overrides this native-boundary accessor
            when that workspace was actually constructed; no mathematical
            property is inferred from its absence.
            """
            return None

        def _smith_representative(self, element):
            r"""Read the selected reduced representative in the same quotient.

            Protected presented-module computation used by quotient-word
            normalization at the module and algebra-presentation adapters.
            The supplied and returned elements belong to this exact module;
            only its own Smith engine chooses the coordinate representative.
            """
            smith = self._smith_engine()
            assert smith is not None, (
                f"cannot reduce {element} to its Smith normal form representative: "
                f"{self} has no Smith normal form, which needs a principal ideal domain base, here {self.base_ring()}"
            )
            coordinates = smith.coordinate_vector(self._to_smith_engine_element(element), reduce=False)
            ring = _engine_ring(self.base_ring())
            reduced = tuple(
                coordinate if invariant == 0 else ring.ideal(invariant).reduce(coordinate)
                for coordinate, invariant in zip(coordinates, smith.invariants(), strict=True)
            )
            if not reduced:
                return self.zero()
            return self._from_smith_engine_element(smith.linear_combination_of_smith_form_gens(reduced))

        # The selected presentation is fixed before this refinement is exposed.
        _selected_module_presentation = None

        def __init__(
            self,
            relation_matrix,
            presentation,
            cokernel_morphism=None,
            **rest,
        ) -> None:
            super().__init__(**rest)
            _fix_selected_module_presentation(
                self,
                presentation.codomain().base_ring(),
                relation_matrix,
                presentation,
                cokernel_morphism,
            )

        def _same_selected_presentation_as(self, other):
            r"""Return whether ``other`` is a module with the same selected presentation over this ring."""
            match other:
                case _ if other in _SelectedFinitePresentationModules(self.base_ring()):
                    return bool(other.presentation() == self.presentation())
                case _:
                    return False

        def __eq__(self, other):
            r"""Compare the underlying represented modules, not extra equipment.

            A selected finite presentation determines the represented cokernel,
            so refinements such as localization or a chosen subobject inclusion
            do not create a new underlying module.  Ideals retain their stronger
            extensional equality as submodules of the ambient ring.
            """
            from dzack_research.preamble.categories.rings.commutative_ideals import (
                CommutativeIdeals,
            )

            ideals = CommutativeIdeals(self.base_ring())
            if self in ideals and other in ideals:
                return self._engine_ideal() == other._engine_ideal()
            return self._same_selected_presentation_as(other)

        def __ne__(self, other):
            return not self == other

        def __hash__(self):
            return hash((self.base_ring(), self.presentation()))

        def _same_presentation_module(
            self,
            labels,
            *,
            _extra_categories=(),
            _extra_construction_data=None,
        ):
            r"""Return a fresh module carrying this chosen finite presentation."""
            if labels != self.module_generating_set():
                raise ValueError(
                    f"cannot rebuild {self} on generators {labels}: its chosen generators are "
                    f"{self.module_generating_set()}"
                )
            return _presented_module_from_morphism(
                self.presentation(),
                _extra_categories=tuple(_extra_categories),
                _extra_construction_data=_extra_construction_data,
            )

        def _presented_biproduct_over(
            self,
            labels,
            factors,
            *,
            extra_categories=(),
            extra_construction_data=None,
        ):
            r"""Return the finite-presentation realization of $\bigoplus_{i \in I} M_i$.

            A relation of one factor is a relation of the biproduct, read at
            that factor's own block of generators; over the index set those
            blocks are disjoint, so the relation rows are their union.
            """
            ring = self.base_ring()
            if not all(
                factor in ModulesWithChosenFinitePresentation(ring)
                and factor._selected_presentation_rows() is not None
                for factor in factors
            ):
                return NotImplemented
            relations_of = {
                index: _presentation_rows(factors.value(index))
                for index in factors.index_set()
            }
            size = labels.cardinality()
            if not size.is_finite():
                return NotImplemented
            width = int(size.finite_value())
            ring = self.base_ring()
            rows = []
            for index in factors.index_set():
                factor_labels = factors.value(index).module_generating_set()
                for relation in relations_of[index]:
                    row = [ring.zero()] * width
                    for position, coefficient in enumerate(relation):
                        if coefficient:
                            label = _biproduct_label(labels, index, factor_labels[position])
                            row[labels.ranking_map()(label)] = coefficient
                    rows.append(row)
            relations = _matrix_space_like(self, len(rows), width).from_rows(tuple(tuple(row) for row in rows))
            presentation = _presentation_from_relation_rows(
                ring,
                labels,
                Sets.Δ[len(rows) - 1],
                relations,
            )
            return _presented_module_from_morphism(
                presentation,
                _biproduct_factors=factors,
                _extra_categories=extra_categories,
                _extra_construction_data=extra_construction_data,
            )

        def cokernel_morphism(self):
            r"""Return the morphism ``rho: F -> G`` of which this module is the cokernel.

            A module constructed as ``coker(rho)`` retains ``rho`` as its
            datum; the quotient map ``G -> coker(rho)`` is
            :meth:`cokernel_projection`.  Dually, a kernel subgroup answers
            ``kernel_morphism()``.
            """
            selected = self._selected_module_presentation
            assert selected is not None, (
                f"{self} has no cokernel morphism: it was not constructed from generators and relations"
            )
            morphism = selected.cokernel_morphism()
            assert morphism is not None, (
                f"{self} was not constructed as the cokernel of a morphism"
            )
            return morphism

        @cached_method
        def cokernel_projection(self):
            r"""Return the canonical quotient map when this object is a selected cokernel."""
            morphism = self.cokernel_morphism()
            source = morphism.codomain()
            return source.module_category().Mor(source, self)(
                {label: self.module_generator(label) for label in source.module_generating_set()}
            )

        def free_resolution(self, steps=None):
            r"""Return a free resolution of the selected presentation.

            Over a principal ideal domain the relation submodule is free, so
            one step suffices and the resolution is the length-one complex
            ``0 -> F_1 -> F_0 -> M -> 0`` built from an independent set of
            relations.

            Over any other base the syzygies of the chosen presentation are the
            next relations, and the resolution continues by resolving them: the
            kernel of a differential is a finitely presented submodule of its
            domain, and its own free cover composed with that inclusion is the
            next differential.  The tower stops on its own where the syzygies
            vanish, and ``is_exact`` then holds; where they do not, ``steps``
            says how far to compute, because a resolution over a general ring
            need not be finite and no bound may be assumed.
            """

            ring = self.base_ring()
            if ring in PrincipalIdealDomains():
                return self._relation_submodule_resolution()
            assert steps is not None, (
                f"a free resolution over {ring} is not known to be finite, so the "
                "number of steps to compute must be supplied"
            )
            return self._syzygy_resolution(int(steps))

        def _selected_diagonal_relation_scalars(self):
            r"""Return the selected diagonal relation scalars, or ``None``.

            A presentation with independent diagonal relations already exhibits
            the relation submodule as ``a_i e_i`` in the selected framing.
            This datum is usable even when a private Sage free-submodule engine
            cannot normalize nonunit pivots over an exact local PID.
            """
            ring = self.base_ring()
            presentation = self.presentation()
            source_labels = tuple(presentation.domain().module_generating_set())
            target_labels = tuple(presentation.codomain().module_generating_set())
            rows = tuple(_matrix_coordinate_rows(self.presentation_matrix()))
            if len(rows) != len(source_labels) or len(source_labels) > len(target_labels):
                return None
            if not all(
                coefficient != ring.zero()
                if column == row
                else coefficient == ring.zero()
                for row, relation_row in enumerate(rows)
                for column, coefficient in enumerate(relation_row)
            ):
                return None
            return tuple(
                rows[position][position] if position < len(rows) else ring.zero()
                for position in range(len(target_labels))
            )

        @cached_method
        def _relation_submodule_resolution(self):
            r"""Resolve over a PID, where the relation submodule is already free.

            When the selected presentation already exhibits independent diagonal
            relations, it is itself the relation inclusion.  This matters for
            exact local PIDs such as ``Z_p``: Sage's generic row-module echelon
            routine normalizes a nonunit pivot by dividing through it, which
            leaves the ring even though no basis change is mathematically needed.
            """

            ring = self.base_ring()
            presentation = self.presentation()
            degree_zero = presentation.codomain()
            zero = _cover_free_module(self, Sets.Δ[-1])
            if self._selected_diagonal_relation_scalars() is not None:
                return _resolution_over_degrees(
                    self,
                    {0: degree_zero, 1: presentation.domain()},
                    {1: presentation},
                    self.presentation_projection(),
                    zero,
                )

            target_labels = degree_zero.module_generating_set()
            relation_matrix = _engine_matrix(self.presentation_matrix()).row_module().basis_matrix()
            relation_labels = Sets.Δ[int(relation_matrix.nrows()) - 1]
            degree_one = _cover_free_module(self, relation_labels)

            def image(label):
                row = relation_matrix.row(int(relation_labels.ranking_map()(label)))
                return degree_zero.linear_combination(
                    {target_label: _owned_engine_element(ring, coefficient) for target_label, coefficient in zip(target_labels, row, strict=True) if coefficient}
                )

            return _resolution_over_degrees(
                self,
                {0: degree_zero, 1: degree_one},
                {1: degree_one.Mono(degree_zero)(image)},
                self.presentation_projection(),
                zero,
            )

        @cached_method
        def _syzygy_resolution(self, steps):
            r"""Resolve by iterated syzygies, stopping early where they vanish."""

            assert steps >= 1, (
                f"cannot compute {steps} steps of a free resolution of {self}: at least one step is needed"
            )
            degree_zero = self.presentation().codomain()
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import _fresh_free_module_on
            zero = _fresh_free_module_on(degree_zero.base_ring(), Sets.Δ[-1])
            terms = {0: degree_zero}
            differentials = {}
            differential = self.presentation()
            for degree in range(1, steps + 1):
                terms[degree] = differential.domain()
                differentials[degree] = differential
                syzygies = differential.kernel()
                if int(syzygies.number_of_module_generators()) == 0:
                    break
                differential = syzygies.inclusion() * syzygies.presentation_projection()
            return _resolution_over_degrees(
                self,
                terms,
                differentials,
                self.presentation_projection(),
                zero,
            )

        def presentation(self):
            r"""Return the selected relation morphism ``F_1 -> F_0``."""
            selected = self.selected_module_resolution()
            match selected.truncation():
                case 1:
                    return selected.differential(1)
                case _:
                    raise TypeError(
                        f"{self} has no selected relation map F_1 -> F_0: its chosen module resolution "
                        f"is truncated in degree {selected.truncation()}"
                    )

        def presentation_matrix(self):
            r"""Return its relation rows in the selected target framing."""
            selected = self._selected_module_presentation
            assert selected is not None, (
                f"{self} has no relation matrix: it was not constructed from generators and relations"
            )
            return selected.relation_matrix()

        def _selected_presentation_rows(self):
            r"""Return relation rows to represented module-construction adapters.

            Protected presented-module contract under OWN-05--07. Permitted
            callers are module, group-module and module-morphism constructors
            that rebuild owned kernels, quotients, direct constructions, or
            scalar changes from the selected finite presentation. The returned
            rows are owned scalar data, not a Smith-engine object.
            """
            return _matrix_coordinate_rows(self.presentation_matrix())

        def _represented_kernel_of_morphism(self, morphism):
            if self not in (morphism.domain(), morphism.codomain()):
                return NotImplemented
            if morphism.codomain() is self and morphism.domain() is self.presentation().codomain() and morphism == self.presentation_projection():
                return self.presentation().image()
            return _selected_presentation_kernel(morphism)

        def _represented_cokernel_of_morphism(self, morphism):
            if morphism.codomain() is not self:
                return NotImplemented
            return _presented_module_from_morphism(morphism, _cokernel_morphism=morphism)

        def _presented_module_from_relation_rows(
            self,
            labels,
            rows,
            *,
            extra_categories=(),
            extra_construction_data=None,
        ):

            rows = tuple(tuple(row) for row in rows)
            relations = _matrix_space_like(
                self,
                len(rows),
                int(labels.cardinality()),
            ).from_rows(rows)
            presentation = _presentation_from_relation_rows(
                self.base_ring(),
                labels,
                Sets.Δ[len(rows) - 1],
                relations,
            )
            return _presented_module_from_morphism(
                presentation,
                _extra_categories=extra_categories,
                _extra_construction_data=extra_construction_data,
            )

        def whole_subobject(self):
            r"""Return this selected presentation as the full subobject of itself."""

            def lift_from_ambient(image, element):
                element = element if element.parent() is self else self(element)
                return image.linear_combination(self.framing_coefficients(element))

            return _presented_module_from_morphism(
                self.presentation(),
                _subobject_ambient=self,
                _subobject_generator_images=lambda label: self.module_generator(label),
                _subobject_lift=lift_from_ambient,
            )

        def subobject_on(self, module_generators):
            r"""Return the submodule generated by one finite family as an exact image."""

            ring = self.base_ring()
            zero_module = (
                self.is_zero()
                if ring in LocalizationRings() or ring in OwnedFields() or ring in PrincipalIdealDomains()
                else False
            )
            if zero_module:
                return self.whole_subobject()

            family = _finite_generating_family(module_generators)
            labels = family.index_set()
            generator = family.value

            source = _cover_free_module(self, labels)
            spanning = source.module_category().Mor(source, self)(lambda label: self(generator(label)))

            if self.base_ring() in OwnedFields():
                spans_all = spanning.is_surjective()
            elif self.base_ring() in LocalRings():
                spans_all = spanning.is_surjective_by_nakayama()
            else:
                spans_all = False
            if spans_all:
                return self.whole_subobject()

            kernel = spanning.kernel()
            return _presented_module_from_morphism(
                kernel.inclusion(),
                _subobject_ambient=self,
                _subobject_generator_images=lambda label: spanning(source.module_generator(label)),
            )

        submodule = subobject_on

        def fitting_ideal(self, index):
            r"""Return ``Fitt_index(M)`` from the selected finite presentation."""

            index = int(index)
            if index < 0:
                raise ValueError(f"the Fitting ideal Fitt_{index}({self}) is undefined: the index must be nonnegative")
            ring = self.base_ring()

            # Fitting ideals commute with arbitrary base change, hence in
            # particular with localization.  A localized module remembers its
            # source presentation, so use that theorem directly instead of
            # demanding a second matrix-minor engine over S^{-1}R.  Concretely,
            # every presentation minor maps to the corresponding minor of the
            # transported presentation, and therefore
            # Fitt_i(S^{-1}M) = S^{-1}Fitt_i(M).
            if ring in LocalizationRings():
                from dzack_research.preamble.categories.modules.localizations import (
                    LocalizedModules,
                )

                if self in LocalizedModules(ring):
                    source = self.numerator_module()
                    source_ring = ring.localization_source()
                    if source in _SelectedFinitePresentationModules(source_ring):
                        return source.fitting_ideal(index).extension_to_localization(ring)

            n = int(self.number_of_module_generators())
            minor_size = n - index
            if minor_size <= 0:
                return ring.ideal(ring.one())
            matrix = _engine_matrix(self.presentation_matrix())
            if minor_size > min(matrix.nrows(), matrix.ncols()):
                return ring.ideal(ring.zero())
            minors = tuple(matrix.minors(minor_size))
            return ring.ideal(*(tuple(_owned_engine_element(ring, _engine_ring(ring)(minor)) for minor in minors) or (ring.zero(),)))

        def _represented_annihilator_ideal(self):
            r"""Represent the scalar-action kernel in exact presentation regimes."""
            ring = self.base_ring()
            if ring in PrincipalIdealDomains():
                # M is R^r together with the cyclic quotients R/(d_i), and the
                # invariant factors divide one another in order.  A scalar kills
                # the sum exactly when it kills every summand, so a free summand
                # leaves the annihilator zero and otherwise the last invariant
                # factor generates it.  This reads the selected presentation, so
                # it covers every PID whose Smith form the backend computes,
                # rather than only the integers.
                invariants = self._invariants_with_units()
                if any(invariant == 0 for invariant in invariants):
                    return ring.ideal(ring.zero())
                nonunits = tuple(invariant for invariant in invariants if not invariant.is_unit())
                if not nonunits:
                    return ring.ideal(ring.one())
                return ring.ideal(nonunits[-1])

            if int(self.number_of_module_generators()) == 1:
                matrix = _engine_matrix(self.presentation_matrix())
                entries = tuple(matrix[row, 0] for row in range(matrix.nrows()))
                return ring.ideal(*(tuple(_owned_engine_element(ring, _engine_ring(ring)(entry)) for entry in entries) or (ring.zero(),)))

            # A scalar kills M exactly when it kills each chosen generator, so
            # Ann(M) is the intersection of the ideals Ann(e_j).  Each of those
            # is the kernel of the map R -> M sending 1 to e_j, which is the
            # kernel the module already computes, so no second commutative-
            # algebra backend enters here: whatever presents a kernel over this
            # ring presents the annihilator too.
            labels = tuple(self.module_generating_set())
            assert labels, (
                f"cannot intersect annihilators of generators of {self}: it has no generators, "
                "so it is zero and its annihilator is the unit ideal"
            )
            annihilator = self.annihilator_of(self.module_generator(labels[0]))
            for label in labels[1:]:
                annihilator = annihilator.intersection(
                    self.annihilator_of(self.module_generator(label))
                )
            return annihilator

        def annihilator_of(self, element):
            r"""Return ``Ann_R(m) = ker(R -> M, r |-> r m)`` as an ideal of ``R``.

            For ``M = coker(A)`` presented on generators and ``v`` the
            coordinates of ``m``, this is the transporter ``(Im(A) :_R v)``:
            the scalars carrying ``v`` into the relations.  Stating it as the
            kernel of multiplication by ``m`` computes it with the presentation
            algorithm the module already owns, and gives every element of the
            module its annihilator rather than only the module its own.
            """
            ring = self.base_ring()
            coordinate = finite_ordered_set(("r",))
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import _fresh_free_module_on
            line = _fresh_free_module_on(self.presentation().codomain().base_ring(), coordinate)
            multiplication = line.module_category().Mor(line, self)({"r": self(element)})
            kernel = multiplication.kernel()
            inclusion = kernel.inclusion()
            scalars = tuple(
                line.framing_coefficients(inclusion(kernel.module_generator(kernel_label))).get(coordinate("r"), ring.zero())
                for kernel_label in kernel.module_generating_set()
            )
            return ring.ideal(*(scalars or (ring.zero(),)))

        def support(self):
            r"""Return ``Supp(M)=V(Fitt_0(M))`` in ``Spec(R)``."""
            return self.base_ring().spectrum().V(self.fitting_ideal(0))

        def finite_length_at_closed_point(self, point):
            r"""Return ``length_{R_p}(M_p)`` when ``M`` is supported only at ``p``.

            In the represented polynomial-over-a-field regime, Singular's
            ``vdim`` computes the base-field dimension of the quotient of the
            selected free cover by the selected relation module. If the support
            is the single closed point ``p``, every composition factor is
            ``kappa(p)``, so dividing by ``[kappa(p):k]`` gives the local
            composition length.
            """
            from sage.categories.fields import Fields as SageFields
            from sage.libs.singular.function import singular_function

            if self.is_zero():
                return _own_ring(SageZZ).zero()
            ring = self.base_ring()
            spectrum = ring.spectrum()
            point = point if element_parent(point) is spectrum else spectrum(point)
            assert point.ideal().is_maximal(), (
                f"cannot take the length of {self} at {point}: it is not a closed point of {spectrum}"
            )
            assert self.fitting_ideal(0).radical() == point.ideal(), (
                f"cannot take the length of {self} at {point}: the length is finite only when the "
                f"support of {self} is exactly this point"
            )
            # Engine adapter (``OWN-06``): Singular's ``std``/``vdim`` over a
            # multivariate polynomial ring over a field.
            engine = _engine_ring(ring)
            assert engine.base_ring() in SageFields() and "multi_polynomial" in type(engine).__module__, (
                f"cannot compute the length of {self} at {point}: this is implemented only over a "
                f"polynomial ring over a field, and the base ring is {ring}"
            )
            relations = _engine_matrix(self.presentation_matrix()).transpose()
            standard_basis = singular_function("std")(relations, ring=engine)
            vector_dimension = int(
                singular_function("vdim")(standard_basis, ring=engine)
            )
            assert vector_dimension >= 0, (
                f"{self} has infinite dimension over the coefficient field of {ring}, "
                f"so it is not supported only at {point}"
            )
            residue_degree = int(point.residue_degree())
            assert residue_degree > 0 and vector_dimension % residue_degree == 0, (
                f"{self} has dimension {vector_dimension} over the coefficient field, which is not a "
                f"multiple of the residue degree {residue_degree} of {point}; a module supported "
                "only at a point p has dimension a multiple of [kappa(p):k]"
            )
            return _own_ring(SageZZ)(vector_dimension // residue_degree)

        def minimal_module_generators(self):
            r"""Return a minimal selected generating set over a local base ring.

            By Nakayama, a set of generators is minimal exactly when its image
            is a basis of ``M/mM``.  The residue module owns the represented
            choice of a basis subfamily of its selected generators.
            """
            ring = self.base_ring()
            if ring not in LocalRings():
                raise TypeError(
                    f"cannot find minimal generators of {self}: Nakayama's lemma needs a local base "
                    f"ring, and {ring} is not known to be local"
                )
            residue_module = self.residue_module()
            basis_labels = residue_module.basis_generator_labels()
            return FiniteOrderedSets().from_indexed(
                basis_labels,
                self.module_generator,
                name="Minimal selected module generators",
            )

        def _represented_vector_space_dimension(self):
            r"""Compute dimension from the selected presentation over a field."""
            if self.base_ring() not in OwnedFields():
                return NotImplemented
            from sage.rings.integer_ring import ZZ as SageZZ

            relation_matrix = _engine_matrix(self.presentation_matrix())
            return _owned_engine_element(
                SageZZ,
                SageZZ(
                    int(self.number_of_module_generators())
                    - relation_matrix.rank()
                ),
            )

        def _represented_vector_space_basis_generator_labels(self):
            r"""Choose a basis subfamily of the selected generators over a field."""
            if self.base_ring() not in OwnedFields():
                return NotImplemented
            relation_matrix = _engine_matrix(self.presentation_matrix())
            pivot_columns = frozenset(relation_matrix.echelon_form().pivots())
            labels = self.module_generating_set()
            positions = finite_ordered_set(
                Sets.Δ[int(self.number_of_module_generators()) - 1]
            ).filtered(
                lambda position: int(position) not in pivot_columns,
                name="Vector-space basis generator positions",
            )
            return FiniteOrderedSets().from_indexed(
                positions,
                lambda position: labels[int(position)],
                name="Vector-space basis generator labels",
            )

        def annihilator_support(self):
            r"""Return ``V(Ann(M))`` when the annihilator is represented."""
            return self.base_ring().spectrum().V(self.annihilator())

        def fiber_dimension_at_least(self, dimension):
            r"""Return the closed locus where ``dim_{kappa(p)} M(p) >= dimension``."""
            dimension = int(dimension)
            spectrum = self.base_ring().spectrum()
            if dimension <= 0:
                return spectrum.V(self.base_ring().ideal(self.base_ring().zero()))
            return spectrum.V(self.fitting_ideal(dimension - 1))

        def rank_stratum(self, rank):
            r"""Return ``{p : dim_{kappa(p)} M(p) = rank}`` inside ``Spec(R)``.

            ``M_p`` is generated by at most ``i`` elements exactly when
            ``Fitt_i(M)`` is not contained in ``p`` (Eisenbud, *Commutative
            Algebra*, Prop. 20.6), so the fibre has dimension exactly ``d`` on
            ``V(Fitt_{d-1}(M))`` off ``V(Fitt_d(M))``.  The stratum is
            therefore locally closed, and as ``d`` ranges over the possible
            ranks the strata partition the spectrum.  This is the
            stratification the rank function induces; the closed union of the
            strata above ``d`` is ``fiber_dimension_at_least``.
            """
            rank = int(rank)
            spectrum = self.base_ring().spectrum()
            at_least = self.fiber_dimension_at_least(rank)
            above = self.fiber_dimension_at_least(rank + 1)
            return SetInclusion(
                spectrum.condition_set(lambda point: point in at_least and point not in above),
                spectrum,
            )

        def local_freeness_locus(self):
            r"""Return ``{p : M_p is free}`` inside ``Spec(R)``.

            A finitely presented module is free at ``p`` of rank ``d`` exactly
            when ``Fitt_d(M)_p = R_p`` and ``Fitt_{d-1}(M)_p = 0`` (Eisenbud,
            *Commutative Algebra*, Prop. 20.8).  The first condition says that
            ``d`` is the fibre dimension at ``p``, which fixes ``d``.  The
            second is a vanishing of a localized finitely generated ideal, and
            such an ideal localizes to zero exactly off the support of its
            annihilator, so it says ``Ann(Fitt_{d-1}(M))`` is not contained in
            ``p``.  Both are containments in ``p``, which is what the point
            answers, and each is an open condition, so the locus is open.

            At a point where the fibre vanishes the module is zero and hence
            free, which is the empty case of the same statement: ``Fitt_{-1}``
            is the zero ideal and localizes to zero everywhere.
            """
            spectrum = self.base_ring().spectrum()
            return SetInclusion(
                spectrum.condition_set(self._is_free_at_point),
                spectrum,
            )

        def local_free_trivialization_at(self, point):
            r"""Return an explicit free trivialization of ``M_p`` when ``p`` lies in the free locus.

            The residue fibre chooses a basis among the selected generators.
            Nakayama makes the corresponding map from a free module onto
            ``M_p``.  At a point of the Fitting-theoretic free locus the source
            rank is exactly the local rank, so the resulting surjection between
            free modules of that rank is an isomorphism; its inverse is the
            common module-morphism inverse construction.
            """
            spectrum = self.base_ring().spectrum()
            if point.parent() is not spectrum:
                point = spectrum(point)
            if not self._is_free_at_point(point):
                raise ValueError(f"{self} is not free at {point}, so its localization there has no basis")

            localized = self.localize_at_prime(point)
            selected_labels = localized.residue_module().basis_generator_labels()
            labels = FiniteOrderedSets().from_indexed(
                selected_labels,
                lambda label: label,
                name="Local free basis labels",
            )
            free = _cover_free_module(localized, labels)
            forward = free.module_category().Mor(free, localized)(
                lambda label: localized.module_generator(label)
            )
            return free.module_category().Core().Mor(free, localized)(
                forward,
                forward.inverse(),
            )

        def _is_free_at_point(self, point) -> bool:
            r"""Decide freeness of ``M_p`` from the Fitting ideals at ``point``."""
            ring = self.base_ring()
            rank = int(self.fiber_dimension(point))
            if rank == 0:
                return True
            annihilator = ring.ideal(ring.zero()).colon(self.fitting_ideal(rank - 1))
            return any(
                not point.ideal().contains_ambient_element(generator)
                for generator in annihilator.ideal_generators()
            )

        @cached_method
        def _selected_presentation_smith_backend(self):
            r"""Privately reduce the selected relation matrix over a PID.

            The input is the selected presentation morphism itself, so the
            returned basis changes refer to the selected relation and target
            framings.  This is backend state local to the presenting module;
            callers receive owned invariants or an owned presentation witness.
            """

            ring = self.base_ring()
            assert ring in PrincipalIdealDomains(), (
                f"cannot compute the Smith normal form of the relation matrix of {self}: "
                f"the base ring {ring} must be a principal ideal domain"
            )
            if ring in LocalizationRings():
                from dzack_research.preamble.categories.modules.localizations import (
                    LocalizedModules,
                )

                if self in LocalizedModules(ring):
                    source = self.numerator_module()
                    source_ring = ring.localization_source()
                    if (
                        source in _SelectedFinitePresentationModules(source_ring)
                        and source_ring in PrincipalIdealDomains()
                    ):
                        # The selected presentation of S^{-1}M is obtained by
                        # applying R -> S^{-1}R coefficientwise to the selected
                        # presentation of M.  Localize its unimodular Smith
                        # basis changes as well; reducing the same matrix in the
                        # fraction-field engine can introduce inverses of
                        # nonunits of S^{-1}R and therefore does not describe
                        # module automorphisms over the localization.
                        return source._selected_presentation_smith_backend()
            backend_relation_matrix = _engine_matrix(self.presentation_matrix())
            return backend_relation_matrix.smith_form()

        @cached_method
        def _invariants_with_units(self):
            r"""Read the diagonal presentation, retaining unit and free coordinates."""
            normalization = self.invariant_factor_presentation()
            diagonal = normalization.codomain().arrow()
            ring = self.base_ring()
            source = diagonal.domain()
            target = diagonal.codomain()
            source_labels = tuple(source.module_generating_set())
            target_labels = tuple(target.module_generating_set())
            diagonal_rank = min(len(source_labels), len(target_labels))
            invariants = []
            for position, target_label in enumerate(target_labels):
                if position >= diagonal_rank:
                    invariants.append(ring.zero())
                    continue
                image = diagonal(source.module_generator(source_labels[position]))
                coefficients = target.framing_coefficients(image)
                invariants.append(
                    _canonical_pid_associate(
                        ring,
                        coefficients.get(target_label, ring.zero()),
                    )
                )
            return tuple(invariants)

        def module_rank(self):
            r"""Return the rank of the free summand over a PID."""

            ring = self.base_ring()
            if ring in OwnedFields():
                return cardinal(self._represented_vector_space_dimension())
            assert ring in PrincipalIdealDomains(), (
                f"cannot compute the rank of {self} from invariant factors: "
                f"the base ring {ring} must be a principal ideal domain or a field"
            )
            return cardinal(sum(1 for invariant in self._invariants_with_units() if invariant == 0))

        def is_torsion(self):
            r"""Read torsion off the invariant factors over a PID, else take the generic fibre."""
            if self.base_ring() not in PrincipalIdealDomains():
                return super().is_torsion()
            return self.module_rank() == 0

        def is_torsion_free(self):
            r"""Over a PID ``M`` is torsion-free exactly when no invariant factor is a nonzero non-unit."""
            ring = self.base_ring()
            if ring in OwnedFields():
                return True
            if ring not in PrincipalIdealDomains():
                return super().is_torsion_free()
            return all(invariant == 0 or invariant.is_unit() for invariant in self._invariants_with_units())

        def is_free(self) -> bool:
            r"""Over a PID a finitely generated module is free exactly when it is torsion-free.

            This is the structure theorem: the decomposition has no cyclic
            torsion summand exactly when no invariant factor is a nonzero
            non-unit, and what is left is a sum of copies of ``R``.  So a
            presented module answers here rather than inheriting the default
            for a module with no known basis.
            """
            if self.base_ring() not in PrincipalIdealDomains():
                return super().is_free()
            return self.is_torsion_free()

        def is_zero(self):
            r"""Decide ``M = 0``.

            Over a principal ideal domain ``M`` vanishes exactly when every
            invariant factor is a unit, and over a field when its dimension is
            zero.  A localization answers through the localization of its
            numerator module.  Over any other ring ``M = coker(F_1 -> F_0)``
            vanishes exactly when every chosen generator is zero, which is
            relation membership in the free cover; that answer is ``Unknown``
            where the ring decides no such membership.
            """
            ring = self.base_ring()
            match ring:
                case _ if ring in LocalizationRings():
                    return super().is_zero()
                case _ if ring in OwnedFields():
                    return self.module_rank() == 0
                case _ if ring in PrincipalIdealDomains():
                    return all(invariant.is_unit() for invariant in self._invariants_with_units())
                case _:
                    zero = self.zero()
                    statuses = tuple(
                        self.module_generator(label) == zero
                        for label in self.module_generating_set()
                    )
                    if any(status is False for status in statuses):
                        return False
                    if all(status is True for status in statuses):
                        return True
                    return Unknown

        def cardinality(self):
            r"""Return ``|M|`` from the base cardinal and the invariant-factor decomposition.

            Over a principal ideal domain ``M`` is ``R^r`` together with the
            cyclic quotients ``R/(d_i)`` of its nonzero non-unit invariant
            factors, and the underlying set of a direct sum is the product of
            the underlying sets.  So ``|M| = |R|^r * prod_i |R/(d_i)|``, with
            every factor read from the base ring rather than assumed to be the
            integers.  The vector-space and free cases are the same formula
            with no nonzero non-unit invariant factor.
            """

            ring = self.base_ring()
            if ring in OwnedFields():
                return ring.cardinality() ** self.module_rank()
            assert ring in PrincipalIdealDomains(), (
                f"the cardinality of a module presented over {ring} is read from an "
                "invariant-factor decomposition, which a principal ideal domain supplies"
            )
            cyclic_orders = tuple(
                ring.quotient_ring(ring.ideal(invariant)).cardinality()
                for invariant in self._invariants_with_units()
                if invariant != 0 and not invariant.is_unit()
            )
            return ring.cardinality() ** self.module_rank() * prod(cyclic_orders, Cardinalities().one())

        @cached_method
        def invariant_factor_presentation(self):
            r"""Normalize the selected presentation through the PID structure theorem.

            For the selected arrow ``p : F_1 -> F_0`` this returns an
            isomorphism in ``Arr(R-Mod)`` from ``p`` to a diagonal presentation
            ``d : F'_1 -> F'_0``.  The two vertical isomorphisms are the source
            and target basis changes.  Thus no chosen relation framing is lost.
            """

            ring = self.base_ring()
            assert ring in PrincipalIdealDomains(), (
                f"cannot compute the invariant factor form of {self}: "
                f"the base ring {ring} must be a principal ideal domain"
            )
            presentation = self.presentation()
            relation_rows = tuple(_matrix_coordinate_rows(self.presentation_matrix()))
            diagonal = all(
                row_index == column_index or coefficient == ring.zero()
                for row_index, row in enumerate(relation_rows)
                for column_index, coefficient in enumerate(row)
            )
            diagonal_entries = tuple(
                _canonical_pid_associate(ring, relation_rows[position][position])
                for position in range(
                    min(
                        len(relation_rows),
                        len(relation_rows[0]) if relation_rows else 0,
                    )
                )
            )
            already_invariant = diagonal and all(
                right == ring.zero()
                or (left != ring.zero() and left.divides(right))
                for left, right in zip(
                    diagonal_entries,
                    diagonal_entries[1:],
                    strict=False,
                )
            )
            if already_invariant:
                arrows = Modules(ring).ArrowCategory()
                original_object = arrows(presentation)
                identity = arrows.Mor(original_object, original_object).identity()
                return arrows.Core().Mor(original_object, original_object)(identity, identity)

            diagonal_backend, row_change_backend, column_change_backend = self._selected_presentation_smith_backend()

            source_labels = finite_ordered_set(range(int(presentation.domain().module_generating_set().cardinality())))
            target_labels = finite_ordered_set(range(int(presentation.codomain().module_generating_set().cardinality())))
            normalized_source = _cover_free_module(self, source_labels)
            normalized_target = _cover_free_module(self, target_labels)

            def owned_matrix_morphism(domain, codomain, backend_matrix):
                mor = _require_matrix_mor(domain.module_category().Mor(domain, codomain))
                source_labels = tuple(domain.module_generating_set())
                target_labels = tuple(codomain.module_generating_set())
                if int(backend_matrix.ncols()) != len(source_labels) or int(backend_matrix.nrows()) != len(target_labels):
                    raise ArithmeticError(
                        f"invariant factor form of {self}: a change-of-basis matrix is "
                        f"{backend_matrix.nrows()} x {backend_matrix.ncols()}, but the map "
                        f"{domain} -> {codomain} needs {len(target_labels)} x {len(source_labels)}"
                    )
                return mor(
                    {
                        source_label: codomain.linear_combination(
                            {
                                target_label: _owned_engine_element(ring, backend_matrix[row, column])
                                for row, target_label in enumerate(target_labels)
                                if backend_matrix[row, column]
                            }
                        )
                        for column, source_label in enumerate(source_labels)
                    }
                )

            # The stored relation matrix is the transpose of the presentation
            # morphism matrix.  If U R V = D, then V^t A U^t = D^t.
            normalized_presentation = owned_matrix_morphism(
                normalized_source,
                normalized_target,
                diagonal_backend.transpose(),
            )
            source_forward = owned_matrix_morphism(
                presentation.domain(),
                normalized_source,
                (~row_change_backend).transpose(),
            )
            source_inverse = owned_matrix_morphism(
                normalized_source,
                presentation.domain(),
                row_change_backend.transpose(),
            )
            target_forward = owned_matrix_morphism(
                presentation.codomain(),
                normalized_target,
                column_change_backend.transpose(),
            )
            target_inverse = owned_matrix_morphism(
                normalized_target,
                presentation.codomain(),
                (~column_change_backend).transpose(),
            )

            arrows = Modules(ring).ArrowCategory()
            original_object = arrows(presentation)
            normalized_object = arrows(normalized_presentation)
            forward = arrows.Mor(original_object, normalized_object)(
                source_forward,
                target_forward,
            )
            inverse = arrows.Mor(normalized_object, original_object)(
                source_inverse,
                target_inverse,
            )
            return arrows.Core().Mor(original_object, normalized_object)(forward, inverse)

        @cached_method
        def hermite_form(self):
            r"""Return the isomorphism onto the row-normalized presentation.

            Hermite normalization changes only the chosen generators of the
            relation submodule.  It therefore keeps the quotient's selected
            module framing fixed, unlike Smith normalization, which also
            changes the target basis.  Over a PID the private matrix engine's
            row-module basis is the canonical independent row normal form;
            over a field it is the usual echelon basis.
            """

            ring = self.base_ring()
            assert ring in PrincipalIdealDomains(), (
                f"cannot compute the Hermite form of the relations of {self}: "
                f"the base ring {ring} must be a principal ideal domain"
            )
            backend = _engine_matrix(self.presentation_matrix()).row_module().basis_matrix()
            labels = self.module_generating_set()
            rows = tuple(
                tuple(
                    _owned_engine_element(ring, backend[row, column])
                    for column in range(int(backend.ncols()))
                )
                for row in range(int(backend.nrows()))
            )
            normalized = self._presented_module_from_relation_rows(labels, rows)
            forward = self.module_category().Mor(self, normalized)(
                {
                    label: normalized.module_generator(label)
                    for label in labels
                }
            )
            inverse = normalized.module_category().Mor(normalized, self)(
                {
                    label: self.module_generator(label)
                    for label in labels
                }
            )
            return self.module_category().Core().Mor(self, normalized)(forward, inverse)

        @cached_method
        def invariant_factors(self):
            r"""Return the indexed family of non-unit invariant factors."""

            invariants = self._invariants_with_units()
            positions = finite_ordered_set(Sets.Δ[len(invariants) - 1])
            retained = positions.filtered(
                lambda position: not invariants[int(position)].is_unit(),
            )
            reduced_positions = Sets.Δ[int(retained.cardinality()) - 1]
            return finite_indexed_family(
                reduced_positions,
                lambda position: invariants[int(retained[int(position)])],
                name="Invariant-factor family",
            )

        @cached_method
        def smith_form_module_generators(self):
            r"""Return the invariant-factor framing realized inside ``self``."""

            normalization = _module_invariant_factor_form(self)
            normalized = normalization.codomain()
            labels = normalized.module_generating_set()
            return finite_indexed_family(
                labels,
                lambda label: normalization.inverse()(normalized.module_generator(label)),
                name="Smith framing family",
            )

        @cached_method
        def invariant_factor_form(self):
            r"""Return ``self -> M_if`` with only non-unit invariant factors."""
            return _module_invariant_factor_form(self)

        @cached_method
        def finite_free_trivialization(self):
            r"""Return an explicit isomorphism ``self ~= R^r`` in the torsion-free PID regime.

            The invariant-factor isomorphism first removes coordinates killed
            by unit diagonal entries.  When the module is torsion-free, every
            remaining invariant factor is zero, so that normalized quotient has
            no relations at all.  Identify its selected generators with a fresh
            finite free module on the same labels and compose the two verified
            isomorphisms.
            """

            ring = self.base_ring()
            assert ring in PrincipalIdealDomains(), (
                f"cannot construct an isomorphism {self} ~= R^r from invariant factors: "
                f"the base ring {ring} must be a principal ideal domain"
            )
            if not self.is_torsion_free():
                raise ValueError(
                    f"{self} is not free: it has nonzero torsion over {ring}"
                )

            normalization = self.invariant_factor_form()
            normalized = normalization.codomain()
            labels = normalized.module_generating_set()
            free = _cover_free_module(self, labels)
            normalized_to_free = normalized.module_category().Mor(normalized, free)(
                {label: free.module_generator(label) for label in labels}
            )
            free_to_normalized = free.module_category().Mor(free, normalized)(
                {label: normalized.module_generator(label) for label in labels}
            )
            return (
                normalized.module_category()
                .Core()
                .Mor(normalized, free)(normalized_to_free, free_to_normalized)
                * normalization
            )

        def is_projective(self) -> bool:
            r"""Decide finite projectivity of the selected presentation.

            Over a principal ideal domain the structure theorem decides it and
            supplies the witness: a torsion-free finitely generated module is
            free, and ``finite_free_trivialization`` produces that isomorphism,
            so the answer arrives with the free module it names.

            Over any other integral domain the presentation still answers.  A
            finitely presented module is projective exactly when every Fitting
            ideal is generated by an idempotent, and where the only idempotents
            are zero and one that says the module has a single rank ``r``, with
            ``Fitt_{r-1}(M) = 0`` and ``Fitt_r(M) = R``.  The Fitting ideals
            commute with base change, which is why this one condition is
            equivalent to freeness of every localization.  Nothing here reads a
            placement, so a presented module answers the question rather than
            being declared projective in advance.
            """

            if self.is_zero():
                return True

            ring = self.base_ring()
            if ring in PrincipalIdealDomains():
                if not self.is_torsion_free():
                    return False
                self.finite_free_trivialization()
                return True

            assert ring in OwnedIntegralDomains(), (
                f"deciding projectivity by Fitting ideals needs the idempotents of {ring} "
                "to be trivial, which an integral domain assures"
            )
            unit_ideal = ring.ideal(ring.one())
            zero_ideal = ring.ideal(ring.zero())
            generator_count = int(self.number_of_module_generators())
            return any(
                self.fitting_ideal(rank) == unit_ideal
                and (rank == 0 or self.fitting_ideal(rank - 1) == zero_ideal)
                for rank in range(generator_count + 1)
            )

        def is_locally_free(self) -> bool:
            r"""Decide finite local freeness in the represented PID regime."""

            return self.is_projective()

        def local_free_trivialization(self, point):
            r"""Localize the global PID free trivialization at ``point``."""

            ring = self.base_ring()
            spectrum = ring.spectrum()
            point = point if element_parent(point) is spectrum else spectrum(point)
            trivialization = self.finite_free_trivialization()
            localization = point.local_ring().localization_functor()
            localized_forward = localization(trivialization.forward())
            localized_inverse = localization(trivialization.inverse())
            return localized_forward.domain().module_category().Core().Mor(
                localized_forward.domain(),
                localized_forward.codomain(),
            )(localized_forward, localized_inverse)

        def presentation_projection(self):
            r"""Return the selected quotient map ``F_0 -> M``."""
            selected = self.selected_module_resolution()
            match selected.truncation():
                case 1:
                    return selected.augmentation()
                case _:
                    raise TypeError(
                        f"{self} has no selected finite-presentation projection: its chosen module "
                        f"resolution is truncated in degree {selected.truncation()}"
                    )

        def torsion_free_quotient_projection(self):
            r"""Return ``M -> M/Tor(M)`` from invariant-factor coordinates."""
            normalization = self.invariant_factor_form()
            normalized = normalization.codomain()
            invariants = self._invariants_with_units()

            positions = finite_ordered_set(Sets.Δ[len(invariants) - 1])
            retained_positions = positions.filtered(
                lambda position: not invariants[int(position)].is_unit(),
            )
            free_positions = positions.filtered(
                lambda position: invariants[int(position)] == self.base_ring().zero(),
            )
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import _fresh_free_module_on
            target = _fresh_free_module_on(self.presentation().codomain().base_ring(), free_positions)
            normalized_projection = normalized.module_category().Mor(normalized, target)(
                {
                    label: (
                        target.module_generator(retained_positions[int(label)])
                        if retained_positions[int(label)] in free_positions
                        else target.zero()
                    )
                    for label in normalized.module_generating_set()
                }
            )
            return normalized_projection * normalization.forward()

        def torsion_submodule(self):
            r"""Return Tor(M) from the invariant-factor quotient over a PID."""
            if self.base_ring() not in PrincipalIdealDomains():
                return super().torsion_submodule()
            return self.torsion_free_quotient_projection().kernel()

        def torsion_free_quotient(self):
            r"""Return ``M/Tor(M)``."""
            return self.torsion_free_quotient_projection().codomain()

        def exponent(self):
            r"""Return the generator of ``Ann_R(M)`` over a principal ideal domain.

            The scalars killing ``M`` form an ideal, and over a principal ideal
            domain that ideal has one generator ``e``: a scalar kills ``M``
            exactly when ``e`` divides it, which is what an exponent says.  So
            the exponent is read from the annihilator rather than from the
            integers in particular, and the two degenerate readings come out
            right on their own.  A module with no nonzero annihilator, any
            nonzero free module among them, has ``e = 0``, and ``e`` is a unit
            exactly when ``Ann(M) = R``, that is exactly when ``M`` is zero.
            """

            ring = self.base_ring()
            assert ring in PrincipalIdealDomains(), (
                f"an exponent is one generator of the annihilator, which {ring} "
                "need not supply; a principal ideal domain does"
            )
            (generator,) = self.annihilator().ideal_generators()
            return generator

        def _repr_(self):
            described = f"Finitely presented module on {self.number_of_module_generators()} module generators over {self.base_ring()}"
            match self.base_ring():
                case ring if ring is _own_ring(SageZZ):
                    # Over the integers the invariant factors classify the module.
                    return f"{described} with invariant factors {self.invariant_factors()}"
                case _:
                    return described

        def base_change(self, ring_map, *, _extra_construction_data=None):
            r"""Transport the selected finite presentation along ``R -> S``."""

            presentation = self.presentation()
            source = presentation.domain().base_change(ring_map)
            target = presentation.codomain().base_change(ring_map)
            relation_labels = source.module_generating_set()
            images = {
                relation_label: sum(
                    (
                        target.scalar_multiple(
                            _base_change_scalar(ring_map, coefficient),
                            target.module_generator(module_label),
                        )
                        for module_label, coefficient in zip(target.module_generating_set(), row, strict=True)
                        if coefficient
                    ),
                    target.zero(),
                )
                for relation_label, row in zip(
                    relation_labels,
                    _presentation_rows(self),
                    strict=True,
                )
            }
            return _presented_module_from_morphism(
                source.module_category().Mor(source, target)(images),
                _extra_construction_data=_extra_construction_data,
            )



def _module_invariant_factor_form(module):
    r"""Return the invariant-factor isomorphism of the underlying presented module.

    This function deliberately bypasses category-method redispatch.  Structured
    refinements (formed/discriminant/equivariant/etc.) call it when they need
    the underlying module normalization and then transport their additional
    structure along the returned isomorphism.
    """
    r"""Return ``self -> M_if`` with only non-unit invariant factors.

    The selected presentation first normalizes by an isomorphism in
    ``Arr(R-Mod)``.  Its diagonal cokernel still remembers the full
    target framing, including coordinates killed by unit diagonal
    entries.  This second, canonical cokernel step deletes exactly
    those zero classes and retains every non-unit factor, including
    zero factors representing free summands.
    """
    presentation_iso = module.invariant_factor_presentation()
    diagonal_presentation = presentation_iso.codomain().arrow()
    full_normalized = diagonal_presentation.cokernel()
    invariants = module._invariants_with_units()

    invariant_positions = finite_ordered_set(Sets.Δ[len(invariants) - 1])
    retained_positions = invariant_positions.filtered(
        lambda position: not invariants[int(position)].is_unit(),
    )

    ring = module.base_ring()
    reduced_labels = finite_ordered_set(
        Sets.Δ[int(retained_positions.cardinality()) - 1]
    )
    reduced_target = _cover_free_module(module, reduced_labels)
    relation_labels = reduced_labels.filtered(
        lambda reduced_position: invariants[int(retained_positions[int(reduced_position)])] != ring.zero(),
    )
    reduced_source = _cover_free_module(module, relation_labels)
    reduced_presentation = reduced_source.module_category().Mor(reduced_source, reduced_target)(
        {
            reduced_position: reduced_target.scalar_multiple(
                invariants[int(retained_positions[int(reduced_position)])],
                reduced_target.module_generator(reduced_position),
            )
            for reduced_position in relation_labels
        }
    )
    reduced = reduced_presentation.cokernel()

    full_labels = full_normalized.module_generating_set()
    full_to_reduced = full_normalized.module_category().Mor(full_normalized, reduced)(
        {
            full_label: (reduced.module_generator(retained_positions.ranking_map()(retained_positions(position))) if position in retained_positions else reduced.zero())
            for position, full_label in enumerate(full_labels)
        }
    )
    reduced_to_full = reduced.module_category().Mor(reduced, full_normalized)(
        {
            reduced_label: full_normalized.module_generator(full_labels[int(retained_positions[int(reduced_label)])])
            for reduced_label in reduced.module_generating_set()
        }
    )
    reduced_iso = full_normalized.module_category().Core().Mor(
        full_normalized,
        reduced,
    )(full_to_reduced, reduced_to_full)

    target_forward = presentation_iso.forward().right()
    target_inverse = presentation_iso.inverse().right()
    full_projection = full_normalized.presentation_projection()
    original_projection = module.presentation_projection()
    original_to_full = module.module_category().Mor(module, full_normalized)(
        {label: full_projection(target_forward(module.presentation().codomain().module_generator(label))) for label in module.module_generating_set()}
    )
    full_to_original = full_normalized.module_category().Mor(full_normalized, module)(
        {label: original_projection(target_inverse(diagonal_presentation.codomain().module_generator(label))) for label in full_normalized.module_generating_set()}
    )
    presentation_cokernel_iso = module.module_category().Core().Mor(
        module,
        full_normalized,
    )(original_to_full, full_to_original)
    return reduced_iso * presentation_cokernel_iso


class _GeneralPresentedElement(ModuleElement):
    r"""An element of a finitely presented module over a general ring.

    The representative lies in the selected free cover.  Equality is exact:
    two representatives define the same quotient element exactly when their
    difference lies in the selected relation submodule.
    """

    def __init__(self, parent, lift) -> None:
        ModuleElement.__init__(self, parent)
        self._lift = parent._free_module(lift)

    def _representative(self):
        r"""Return the private representative in the selected cover."""
        return self._lift

    def _add_(self, other):
        return self.parent().element_class(self.parent(), self._lift + other._lift)

    def _neg_(self):
        return self.parent().element_class(self.parent(), -self._lift)

    def _lmul_(self, scalar):
        parent = self.parent()
        return parent.element_class(
            parent,
            parent._scale_representative(scalar, self._lift),
        )

    _rmul_ = _lmul_

    def __rmul__(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        if not isinstance(other, _GeneralPresentedElement) or other.parent() is not self.parent():
            return op == op_NE
        equal = self.parent()._relation_contains(self._lift - other._lift)
        return equal if op == op_EQ else (Unknown if equal is Unknown else not equal)

    def __hash__(self):
        parent = self.parent()
        smith_engine = parent._smith_engine()
        if smith_engine is None:
            raise TypeError(
                f"cannot hash {self}: an element of {parent} has a canonical representative only "
                f"over a principal ideal domain, and the base ring is {parent.base_ring()}"
            )
        key = tuple(parent._to_smith_engine_element(self).vector())
        return hash((id(parent), key))

    def additive_order(self):
        r"""Return the additive order when the selected Smith model is finite."""
        parent = self.parent()
        engine = parent._smith_engine()
        assert engine is not None and parent.is_torsion(), (
            f"cannot compute the additive order of {self}: {parent} must be a torsion module "
            "over a principal ideal domain"
        )
        order = parent._to_smith_engine_element(self).additive_order()
        return _owned_engine_element(parent.base_ring(), SageZZ(order))

    def _repr_(self):
        parent = self.parent()
        coordinates = parent._cover_coordinates(self)
        terms = [
            (label, coefficient)
            for label in parent.module_generating_set()
            if (coefficient := coordinates.value(label)) != parent.base_ring().zero()
        ]
        if not terms:
            return "0"
        return repr_lincomb(
            terms,
            repr_monomial=lambda label: f"[{label}]",
            strip_one=True,
        )


class _GeneralPresentedModule:
    r"""A presented module over a ring with no Smith engine.

    ``free_module`` is the cover and ``relation_submodule`` the relation
    module inside it: Sage objects over the engine ring when the base ring
    has a Sage engine, else the owned free cover and ``None``.  Both are
    private; the category states the mathematics.
    """

    def __init__(
        self,
        free_module,
        relation_submodule,
        *,
        base_ring,
        module_generating_set,
        relation_matrix,
        presentation,
        cokernel_morphism=None,
        **rest,
    ) -> None:
        self._free_module = free_module
        self._relation_submodule = relation_submodule
        self._lifted_relation_free_module = None
        self._lifted_relation_submodule = None
        super().__init__(
            base_ring=base_ring,
            module_generating_set=module_generating_set,
            module_generator_function=lambda label: self._cover_generator(int(module_generating_set.ranking_map()(label))),
            framing_source=presentation.codomain(),
            relation_matrix=relation_matrix,
            presentation=presentation,
            cokernel_morphism=cokernel_morphism,
            **rest,
        )

    def _scale_representative(self, scalar, representative):
        r"""Scale a private cover representative by an owned scalar."""
        scalar = self.base_ring()(scalar)
        if self._relation_submodule is None:
            return self._free_module.scalar_multiple(scalar, representative)
        return _engine_element(self.base_ring(), scalar) * representative

    def _cover_generator(self, position):
        r"""The class of the ``position``-th cover basis vector."""
        if self._relation_submodule is None:
            labels = self._free_module.module_generating_set()
            return self(self._free_module.module_generator(labels[position]))
        return self(self._free_module.gen(position))

    def _cover_coordinates(self, element):
        r"""Coordinates of a representative as an indexed family on the cover basis."""
        lift = self(element)._representative()
        labels = self.module_generating_set()

        if self._relation_submodule is None:
            coefficients = self._free_module.framing_coefficients(lift)
            zero = self.base_ring().zero()
            return indexed_family(
                labels,
                lambda label: coefficients.get(label, zero),
                name="Cover coordinates",
            )
        ring = self.base_ring()
        return indexed_family(
            labels,
            lambda label: _owned_engine_element(
                ring,
                lift[int(labels.ranking_map()(label))],
            ),
            name="Cover coordinates",
        )

    def _selected_module_coefficients(self, element):
        r"""Return the coefficients of the selected cover representative of ``element``."""
        coordinates = self._cover_coordinates(element)
        zero = self.base_ring().zero()
        return {
            label: coordinates[label]
            for label in self.module_generating_set()
            if coordinates[label] != zero
        }

    def _from_coordinates(self, coordinates):
        r"""Return the class of the cover element with these framing coordinates.

        ``coordinates`` are listed in the order of the finite framing.
        """
        return self.linear_combination(
            dict(zip(self.module_generating_set(), coordinates, strict=True))
        )

    def _lifted_relation_backend(self):
        r"""Return an exact presentation-ring submodule for quotient-algebra scalars.

        If the coefficient ring is itself ``A = P/I`` with a selected finite
        commutative presentation, equality in a presented ``A``-module must be
        tested after lifting to ``P``.  The relation module in ``P^n`` is
        generated by the lifted module-relation rows together with ``I e_j``
        for every free coordinate ``e_j``.  This avoids relying on Sage's
        generic submodule-membership implementation over quotient rings, which
        can fail even on a displayed generator of the submodule.
        """
        if self._lifted_relation_submodule is not None:
            return (
                self._lifted_relation_free_module,
                self._lifted_relation_submodule,
            )

        base_ring = self.base_ring()
        if not base_ring._has_selected_exact_coefficient_presentation():
            return None

        from sage.modules.free_module import FreeModule as SageFreeModule

        presentation_ring = base_ring._exact_coefficient_presentation_ring()
        presentation_engine = _engine_ring(presentation_ring)
        rank = int(self.module_generating_set().cardinality())
        lifted_free = SageFreeModule(presentation_engine, rank)

        def lift_scalar(value):
            lifted = base_ring._lift_coefficient_to_presentation(value)
            return _engine_element(presentation_ring, lifted)

        rows = [lifted_free(tuple(lift_scalar(coefficient) for coefficient in row)) for row in _presentation_rows(self)]
        for algebra_relation in base_ring._exact_coefficient_presentation_relations():
            relation = _engine_element(presentation_ring, algebra_relation)
            for position in range(rank):
                coordinates = [presentation_engine.zero()] * rank
                coordinates[position] = relation
                rows.append(lifted_free(coordinates))

        lifted_submodule = lifted_free.submodule(rows) if rows else lifted_free.zero_submodule()
        self._lifted_relation_free_module = lifted_free
        self._lifted_relation_submodule = lifted_submodule
        return lifted_free, lifted_submodule

    def _singular_polynomial_relation_contains(self, vector):
        r"""Decide direct polynomial relation membership through Singular.

        Sage's generic free-submodule membership over a polynomial ring uses
        the ambient fraction-field span, so, for example, it reports
        ``e in <x e>`` over ``QQ[x,y]``.  Singular's module ``lift`` asks the
        actual polynomial-module membership question.

        Engine adapter (``OWN-06``): its caller is :meth:`_relation_contains`;
        it returns ``NotImplemented`` for a computation ring that is not a
        polynomial ring over a field, and otherwise the membership of the
        cover vector in the relation submodule.
        """
        from sage.categories.fields import Fields as SageFields
        from sage.matrix.constructor import matrix

        engine = _engine_ring(self.base_ring())
        if "polynomial" not in type(engine).__module__ or engine.base_ring() not in SageFields():
            return NotImplemented
        coefficient_field = engine.base_ring()

        if engine.ngens() == 1 and "multi_polynomial" not in type(engine).__module__:
            singular_ring = _SagePolynomialRing(
                coefficient_field,
                engine.variable_names(),
                implementation="singular",
            )
            to_singular = engine.hom([singular_ring.gen(0)], singular_ring)
        else:
            singular_ring = engine
            to_singular = singular_ring

        width = int(self.module_generating_set().cardinality())
        rows = tuple(_presentation_rows(self))
        if not rows:
            return False
        relations = matrix(
            singular_ring,
            len(rows),
            width,
            [to_singular(_engine_element(self.base_ring(), coefficient)) for row in rows for coefficient in row],
        ).transpose()
        requested = matrix(
            singular_ring,
            width,
            1,
            [to_singular(coefficient) for coefficient in tuple(vector)],
        )
        return _singular_module_lift(relations, requested) is not None

    def _relation_contains(self, vector) -> bool:
        if vector == self._free_module.zero():
            return True
        if self._relation_submodule is None:
            diagonal = self._selected_diagonal_relation_scalars()
            ring = self.base_ring()
            if diagonal is not None and ring in PrincipalIdealDomains():
                labels = tuple(self.module_generating_set())
                coefficients = self._free_module.framing_coefficients(vector)
                return all(
                    coefficients.get(label, ring.zero()) == ring.zero()
                    if scalar == ring.zero()
                    else coefficients.get(label, ring.zero()) in ring.ideal(scalar)
                    for label, scalar in zip(labels, diagonal, strict=True)
                )
            return Unknown
        lifted_backend = self._lifted_relation_backend()
        if lifted_backend is None:
            polynomial_contains = self._singular_polynomial_relation_contains(vector)
            if polynomial_contains is not NotImplemented:
                return polynomial_contains
            return vector in self._relation_submodule

        lifted_free, lifted_submodule = lifted_backend
        base_ring = self.base_ring()
        presentation_ring = base_ring._exact_coefficient_presentation_ring()

        def lift_backend_coefficient(coefficient):
            owned_coefficient = _owned_engine_element(base_ring, coefficient)
            lifted_owned = base_ring._lift_coefficient_to_presentation(owned_coefficient)
            return _engine_element(presentation_ring, lifted_owned)

        lifted = lifted_free(tuple(lift_backend_coefficient(coefficient) for coefficient in tuple(vector)))
        return _flattened_submodule_membership(
            _engine_ring(presentation_ring),
            lifted,
            lifted_submodule,
        )

    def __call__(self, value):
        r"""Construct a quotient element without Sage coercion discovery."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        if isinstance(value, _GeneralPresentedElement):
            if value.parent() is self:
                return value
            value = value._representative()
        match element_parent(value):
            case Parent() as source if source is not self and self._built_on_the_same_data(source):
                return self._element_on_the_same_data(source, value)
        return self.element_class(self, value)

    def zero(self):
        return self.element_class(self, self._free_module.zero())

    def an_element(self):
        return self(self._free_module.an_element())


class _PresentedModule(_GeneralPresentedModule):
    r"""An owned presented module with an optional private Sage Smith engine.

    The mathematical object and its elements are the same owned quotient
    model used for general presentations.  Sage's FGP module is private state
    used only by Smith-form algorithms.
    """

    def __init__(
        self,
        engine=None,
        *,
        free_module,
        relation_submodule,
        base_ring,
        module_generating_set,
        relation_matrix,
        presentation,
        cokernel_morphism=None,
        **rest,
    ) -> None:
        self._pid_engine = engine
        super().__init__(
            free_module,
            relation_submodule,
            base_ring=base_ring,
            module_generating_set=module_generating_set,
            relation_matrix=relation_matrix,
            presentation=presentation,
            cokernel_morphism=cokernel_morphism,
            **rest,
        )

    def _smith_engine(self):
        r"""Sage's FGP module over the engine ring, or ``None``.

        This is the only accessor of the Smith engine.  Protected contract of
        the presented-module realization: the discriminant-module,
        internal-Mor and algebra-presentation adapters cross here for
        Smith-form data and convert every result back to an owned object
        before returning it.
        """
        return self._pid_engine

    def _to_smith_engine_element(self, element):
        r"""Cross an owned quotient element into the private FGP workspace.

        This is the lowering side of the protected Smith contract documented
        by ``_smith_engine``; only the named discriminant, internal-Mor and
        algebra-presentation adapters may use the raw result.
        """
        owned = self(element)
        coordinates = self._cover_coordinates(owned)
        backend = self._pid_engine
        labels = self.module_generating_set()
        return backend(backend.V()(tuple(_engine_element(self.base_ring(), coordinates[label]) for label in labels)))

    def _from_smith_engine_element(self, element):
        r"""Cross one private FGP element back to an owned quotient element.

        This is the raising side of the protected Smith contract documented by
        ``_smith_engine``. The private FGP element is consumed here and an
        element of this owned module is returned.
        """
        backend = self._pid_engine
        lift = backend(element).lift()
        ring = self.base_ring()
        coordinates = tuple(_owned_engine_element(ring, coefficient) for coefficient in tuple(lift))
        return self._from_coordinates(coordinates)


def _new_presented_module(
    *,
    free_module,
    relation_submodule,
    base_ring,
    module_generating_set,
    relation_matrix,
    presentation,
    engine=None,
    cokernel_morphism=None,
    subobject_ambient=None,
    subobject_generator_images=None,
    subobject_lift=None,
    subobject_inclusion_factory=None,
    biproduct_factors=None,
    extra_categories=(),
    extra_construction_data=None,
):
    r"""Build a represented quotient through the category constructor chain."""
    categories = [_SelectedFinitePresentationModules(base_ring)]
    if base_ring in OwnedFields():
        categories.append(VectorSpaces(base_ring))
    data = {
        "engine": engine,
        "free_module": free_module,
        "relation_submodule": relation_submodule,
        "base_ring": base_ring,
        "module_generating_set": module_generating_set,
        "relation_matrix": relation_matrix,
        "presentation": presentation,
        "cokernel_morphism": cokernel_morphism,
    }
    if subobject_ambient is not None or subobject_inclusion_factory is not None:
        categories.append(ModuleSubobjects(base_ring))
        if subobject_ambient is not None:
            categories.append(Modules(base_ring).Subobjects(subobject_ambient))
        data.update(
            subobject_ambient=subobject_ambient,
            subobject_generator_images=subobject_generator_images,
            subobject_lift=subobject_lift,
            subobject_inclusion_factory=subobject_inclusion_factory,
        )
    if biproduct_factors is not None:
        categories.append(BiproductModules(base_ring))
        data["biproduct_factors"] = biproduct_factors
    categories.extend(extra_categories)
    if extra_construction_data is not None:
        data.update(extra_construction_data)
    return _object_of(
        Cat().meet(tuple(categories)),
        _engine=(
            _SelectedFinitePresentationModules(base_ring),
            _PresentedModule,
            _GeneralPresentedElement,
        ),
        **data,
    )


def _resolution_over_degrees(module, terms, differentials, augmentation, zero):
    r"""Assemble a free resolution from its terms and differentials by degree.

    The degrees carrying a term are the ordinals up to the largest one built,
    and the degrees carrying a differential are those among them that have one,
    which are the nonzero degrees the construction reached.  Both are owned
    ordered sets, and the terms and differentials are families over them.
    """

    degrees = finite_ordered_set(Sets.Δ[max(terms)])
    carrying = degrees.filtered(
        lambda degree: int(degree) in differentials,
    )
    return FreeResolution(
        module,
        degrees,
        indexed_family(
            degrees,
            lambda degree: terms[int(degree)],
            name="Free resolution terms",
        ),
        indexed_family(
            carrying,
            lambda degree: differentials[int(degree)],
            name="Free resolution differentials",
        ),
        augmentation,
        zero,
    )


def _presentation_matrix(module):
    r"""Materialize the selected finite relation family as one matrix Mor element.

    The chosen-presentation category owns only the mathematical datum.  A
    concrete presented-module backend may already store its matrix; otherwise
    (notably for a finite free module) the matrix is synthesized from the
    selected relation rows only at this finite coordinate boundary.
    """
    ring = module.base_ring()
    if module not in ModulesWithChosenFinitePresentation(ring):
        raise TypeError(
            f"{module} has no relation matrix: it is not a module with chosen finitely many "
            f"generators and relations, but is in {module.category()}"
        )

    if module in _SelectedFinitePresentationModules(ring):
        return module.presentation_matrix()

    rows = module._selected_presentation_rows()
    if rows is None:
        raise TypeError(f"{module} is finitely presented, but its relations are not known explicitly")
    rows = tuple(tuple(row) for row in rows)
    return _matrix_space_like(
        module,
        len(rows),
        int(module.module_generating_set().cardinality()),
    ).from_rows(rows)


def _matrix_coordinate_rows(matrix):
    r"""Return finite coordinate rows of one matrix Mor element."""
    parent = matrix.parent()
    return tuple(tuple(matrix.matrix_entry(row_label, column_label) for column_label in parent.column_index_set()) for row_label in parent.row_index_set())


def _presentation_rows(module):
    r"""Return the selected finite relation rows without forcing matrix realization."""
    if module not in ModulesWithChosenFinitePresentation(module.base_ring()):
        raise TypeError(
            f"{module} has no relations: it is not a module with chosen finitely many "
            f"generators and relations, but is in {module.category()}"
        )
    rows = module._selected_presentation_rows()
    if rows is None:
        raise TypeError(f"{module} is finitely presented, but its relations are not known explicitly")
    return tuple(tuple(row) for row in rows)


def _relation_element(module, row):
    return sum(
        (module.scalar_multiple(coefficient, module.module_generator(label)) for label, coefficient in zip(module.module_generating_set(), row, strict=True) if coefficient),
        module.zero(),
    )



def _selected_presentation_kernel(morphism):
    r"""Compute a kernel from the selected finite presentations of both endpoints.

    The zero map has the whole domain for kernel.  Over a principal ideal
    domain the preimage of the target relations is free; over a polynomial
    ring over the integers, or a quotient of one with a chosen presentation,
    CAP computes the kernel presentation; over a polynomial ring over a field,
    or a quotient of one, Singular does.
    """
    from dzack_research.preamble.categories.algebras.algebras import (
        AlgebrasWithChosenFinitePresentation,
    )
    from dzack_research.preamble.categories.algebras.free_algebras import (
        SymmetricAlgebras,
    )

    domain = morphism.domain()
    codomain = morphism.codomain()
    ring = domain.base_ring()
    assert codomain.base_ring() is ring, (
        f"cannot compute the kernel of {morphism}: its domain is over {ring} and its codomain "
        f"over {codomain.base_ring()}, but a module morphism has one base ring"
    )
    selected = ModulesWithChosenFinitePresentation(ring)
    if domain not in selected or codomain not in selected:
        return NotImplemented
    if domain._selected_presentation_rows() is None or codomain._selected_presentation_rows() is None:
        return NotImplemented
    labels = domain.module_generating_set()
    if labels.cardinality().is_finite() and all(
        morphism(domain.module_generator(label)) == codomain.zero()
        for label in labels
    ):
        return domain.whole_subobject()
    integers = _own_ring(SageZZ)
    match ring:
        case _ if ring in PrincipalIdealDomains():
            return _pid_presentation_kernel(morphism)
        case _ if ring in SymmetricAlgebras(integers) or ring in AlgebrasWithChosenFinitePresentation(integers):
            return _cap_presentation_kernel(morphism)
        case _:
            return _singular_presentation_kernel(morphism)


def _cap_presentation_kernel(morphism):
    r"""Return ``ker(morphism)`` through CAP over a polynomial ring over ``ZZ``.

    ``ModulePresentationsForCAP`` owns the categorical kernel computation.
    The private adapter crosses only selected relation, morphism, kernel and
    lift matrices; the returned object is the ordinary owned finitely
    presented module with its actual inclusion into ``morphism.domain()``.
    """
    from sage_categories.engines.presented_modules import kernel_presentation

    domain = morphism.domain()
    codomain = morphism.codomain()
    ring = _owned_ring(domain.base_ring())
    if _owned_ring(codomain.base_ring()) is not ring:
        raise ValueError(
            f"cannot compute the kernel of {morphism}: its domain is over {ring} and its codomain "
            f"over {codomain.base_ring()}, but a module morphism has one base ring"
        )
    variable_names = tuple(ring.variable_names())
    assert variable_names and ring.base_ring() is _own_ring(SageZZ), (
        f"cannot compute the kernel of {morphism} with this algorithm: it needs a polynomial "
        f"ring over ZZ, and the base ring is {ring}"
    )

    source_labels = tuple(domain.module_generating_set())
    target_labels = tuple(codomain.module_generating_set())
    source_relations = tuple(_matrix_coordinate_rows(_presentation_matrix(domain)))
    target_relations = tuple(_matrix_coordinate_rows(_presentation_matrix(codomain)))
    morphism_rows = tuple(
        tuple(
            codomain.framing_coefficients(morphism(domain.module_generator(source_label))).get(target_label, ring.zero())
            for target_label in target_labels
        )
        for source_label in source_labels
    )
    native = kernel_presentation(
        variable_names=variable_names,
        owned_ring=ring,
        source_rank=len(source_labels),
        target_rank=len(target_labels),
        source_relation_rows=source_relations,
        target_relation_rows=target_relations,
        morphism_rows=morphism_rows,
    )
    inclusion_rows = native.inclusion_rows()
    kernel_count = len(inclusion_rows)
    kernel_labels = Sets.Δ[kernel_count - 1]
    relation_rows = native.relation_rows()
    relation_labels = Sets.Δ[len(relation_rows) - 1]
    relation_matrix = _matrix_space_like(
        domain, len(relation_rows), kernel_count
    ).from_rows(relation_rows)
    presentation = _presentation_from_relation_rows(
        ring, kernel_labels, relation_labels, relation_matrix
    )
    generator_images = {
        label: domain.linear_combination(
            {
                source_label: coefficient
                for source_label, coefficient in zip(
                    source_labels, inclusion_rows[int(label)], strict=True
                )
                if coefficient
            }
        )
        for label in kernel_labels
    }

    def lift_from_domain(kernel, element):
        if element.parent() is not domain:
            element = domain(element)
        if morphism(element) != codomain.zero():
            return None
        coordinates = domain.framing_coefficients(element)
        source_row = tuple(
            coordinates.get(label, ring.zero()) for label in source_labels
        )
        lifted = native.lift_row(source_row)
        return kernel.linear_combination(
            {
                label: lifted[int(label)]
                for label in kernel_labels
                if lifted[int(label)] != ring.zero()
            }
        )

    return _presented_module_from_morphism(
        presentation,
        _subobject_ambient=domain,
        _subobject_generator_images=generator_images,
        _subobject_lift=lift_from_domain,
    )

def _pid_presentation_kernel(morphism):
    r"""Return ``ker(morphism)`` from selected finite presentations over a PID.

    Write the selected presentations as ``M = R^n/P`` and ``N = R^m/Q``
    and let ``F : R^n -> R^m`` be the selected lift of ``morphism``.  The
    preimage ``S = {x in R^n : F(x) in Q}`` is a free submodule of ``R^n``.
    A basis of ``S`` gives a free cover of the kernel, while the source
    relation rows ``P <= S`` give its relations.  Thus
    ``ker(morphism) = S/P``.

    Matrix and native free-module operations below are private PID backend
    computations; the returned module and inclusion are owned objects.
    """
    from sage.matrix.constructor import matrix
    from sage.modules.free_module import FreeModule as SageFreeModule

    domain = morphism.domain()
    codomain = morphism.codomain()
    ring = _owned_ring(domain.base_ring())
    if _owned_ring(codomain.base_ring()) is not ring:
        raise ValueError(
            f"cannot compute the kernel of {morphism}: its domain is over {ring} and its codomain "
            f"over {codomain.base_ring()}, but a module morphism has one base ring"
        )
    if ring not in PrincipalIdealDomains():
        raise TypeError(
            f"cannot compute the kernel of {morphism} with this algorithm: the base ring {ring} "
            "must be a principal ideal domain"
        )

    engine = _engine_ring(ring)
    source_labels = tuple(domain.module_generating_set())
    target_labels = tuple(codomain.module_generating_set())
    source_relations = _engine_matrix(_presentation_matrix(domain))
    target_relations = _engine_matrix(_presentation_matrix(codomain))
    source_rank = len(source_labels)
    target_rank = len(target_labels)

    lift_entries = []
    for target_label in target_labels:
        for source_label in source_labels:
            coefficients = codomain.framing_coefficients(morphism(domain.module_generator(source_label)))
            lift_entries.append(
                _engine_element(
                    ring,
                    coefficients.get(target_label, ring.zero()),
                )
            )
    lift_matrix = matrix(
        engine,
        target_rank,
        source_rank,
        lift_entries,
    )
    augmented = lift_matrix.augment(-target_relations.transpose())
    free_cover = SageFreeModule(engine, source_rank)

    if source_rank == 0:
        preimage = free_cover.zero_submodule()
    else:
        diagonal, _left_change, right_change = augmented.smith_form()
        diagonal_rank = min(int(augmented.nrows()), int(augmented.ncols()))
        kernel_columns = tuple(
            column
            for column in range(int(augmented.ncols()))
            if column >= diagonal_rank or diagonal[column, column] == 0
        )
        # If D = U A V is the Smith form of the augmented matrix A, then
        # A(V e_j) = 0 exactly for the zero diagonal coordinates of D.
        # Since V is invertible, those columns of V are a basis of ker(A).
        kernel_pairs = tuple(
            tuple(
                right_change[row, column]
                for row in range(int(right_change.nrows()))
            )
            for column in kernel_columns
        )
        projected = [free_cover(tuple(row[position] for position in range(source_rank))) for row in kernel_pairs if any(row[position] != 0 for position in range(source_rank))]
        preimage = free_cover.submodule(projected) if projected else free_cover.zero_submodule()

    basis_rows = tuple(tuple(row) for row in preimage.basis_matrix().rows())
    kernel_count = len(basis_rows)
    kernel_labels = Sets.Δ[kernel_count - 1]

    relation_coordinate_rows = []
    for row in source_relations.rows():
        source_relation = free_cover(tuple(row))
        # A module morphism carries each source relation into the target
        # relations, so every relation row lies in the preimage.
        assert source_relation in preimage, (
            f"{morphism} is not well defined: the relation {source_relation} of its domain "
            "does not map into the relations of its codomain"
        )
        coordinates = preimage.coordinate_vector(source_relation)
        relation_coordinate_rows.append(tuple(_owned_engine_element(ring, engine(coefficient)) for coefficient in coordinates))

    relation_labels = Sets.Δ[len(relation_coordinate_rows) - 1]
    relation_matrix = _matrix_space_like(
        domain,
        len(relation_coordinate_rows),
        kernel_count,
    ).from_rows(tuple(relation_coordinate_rows))
    presentation = _presentation_from_relation_rows(
        ring,
        kernel_labels,
        relation_labels,
        relation_matrix,
    )
    generator_images = {
        label: domain.linear_combination(
            {
                source_label: _owned_engine_element(ring, engine(coefficient))
                for source_label, coefficient in zip(
                    source_labels,
                    basis_rows[int(label)],
                    strict=True,
                )
                if coefficient
            }
        )
        for label in kernel_labels
    }

    def lift_from_domain(kernel, element):
        if element.parent() is not domain:
            element = domain(element)
        coefficients = domain.framing_coefficients(element)
        representative = free_cover(
            tuple(
                _engine_element(
                    ring,
                    coefficients.get(label, ring.zero()),
                )
                for label in source_labels
            )
        )
        if representative not in preimage:
            return None
        coordinates = preimage.coordinate_vector(representative)
        return kernel.linear_combination({label: _owned_engine_element(ring, engine(coordinates[int(label)])) for label in kernel_labels if coordinates[int(label)] != 0})

    return _presented_module_from_morphism(
        presentation,
        _subobject_ambient=domain,
        _subobject_generator_images=generator_images,
        _subobject_lift=lift_from_domain,
    )


def _singular_module_lift(generators, column):
    r"""Express a column in a polynomial submodule, or return ``None``.

    Native Singular adapter.  As in Sage's
    ``modules/submodule.py:_groebner_basis_contains``, reduce the column by
    a standard basis before asking for its coefficients.  A nonzero normal
    form is nonmembership; an engine exception is never interpreted as it.
    """
    from sage.libs.singular.function_factory import ff
    from sage.matrix.constructor import matrix

    ring = generators.base_ring()
    standard = ff.std(generators, ring=ring)
    remainder = matrix(ff.reduce(column, standard, ring=ring))
    if not remainder.is_zero():
        return None
    return ff.lift(generators, column, ring=ring)


def _flattened_submodule_membership(presentation_engine, lifted, lifted_submodule):
    r"""Decide ``lifted in lifted_submodule`` over a polynomial ring, flattening nested variables.

    Engine adapter (``OWN-06``).  Its caller is relation membership of a
    module over a quotient of a polynomial ring.  Sage's generic submodule
    membership over a nested polynomial ring ``R[t][x_1,...,x_n]`` can return
    ``False`` even for a displayed generator; flattening to the canonically
    isomorphic ``R[t,x_1,...,x_n]`` asks the Singular-backed multivariate
    implementation instead.  A computation ring with no flattening morphism is
    asked directly.
    """
    from sage.modules.free_module import FreeModule as SageFreeModule

    flattening = getattr(presentation_engine, "flattening_morphism", None)
    if flattening is None:
        return lifted in lifted_submodule
    flatten = flattening()
    flattened_ring = flatten.codomain()
    if flattened_ring is presentation_engine:
        return lifted in lifted_submodule
    flattened_free = SageFreeModule(flattened_ring, int(lifted.parent().rank()))
    flattened = flattened_free(tuple(flatten(coefficient) for coefficient in tuple(lifted)))
    flattened_relations = flattened_free.submodule(
        tuple(
            flattened_free(
                tuple(flatten(coefficient) for coefficient in tuple(relation))
            )
            for relation in lifted_submodule.gens()
        )
    )
    return flattened in flattened_relations


def _singular_presentation_kernel(morphism):
    r"""Return ``ker(morphism)`` for polynomial-presentation coefficient rings.

    Let ``A=P/I`` with ``P`` a polynomial ring over a field, and let

    ``f : A^n/D -> A^m/Q``.

    Lifting to ``P``, a vector ``x`` represents a kernel element exactly when

    ``F x \in \operatorname{im}(Q^t,I)``.

    Singular's maintained ``homolog.lib::mor_kernel(A,M,N)`` computes the
    presentation of ``ker(A':coker(M)->coker(N))``.  Its internal first
    ``modulo(A,N)`` is also the kernel-lift module, but ``mor_kernel`` exposes
    only the resulting presentation.  This adapter therefore calls ``modulo``
    once separately to recover exactly those generator lifts for the owned
    inclusion; it does not reconstruct the presentation algorithm.

    This is a private computation crossing.  The returned object is the owned
    finitely presented module equipped with its actual inclusion into the
    domain; no Singular module escapes into the public API.
    """
    from sage.libs.singular.function_factory import ff
    from sage.matrix.constructor import matrix
    from sage.modules.free_module import FreeModule as SageFreeModule
    from sage.structure.sequence import Sequence

    domain = morphism.domain()
    codomain = morphism.codomain()
    ring = _owned_ring(domain.base_ring())
    if _owned_ring(codomain.base_ring()) is not ring:
        raise ValueError(
            f"cannot compute the kernel of {morphism}: its domain is over {ring} and its codomain "
            f"over {codomain.base_ring()}, but a module morphism has one base ring"
        )

    coefficient_presentation = ring._exact_coefficient_presentation_ring()
    presentation_ring = _engine_ring(coefficient_presentation)
    coefficient_relations = ring._exact_coefficient_presentation_relations()

    def backend_coefficient_relation(relation):
        return _engine_element(coefficient_presentation, relation)

    def lift_scalar(value):
        lifted = ring._lift_coefficient_to_presentation(value)
        return _engine_element(coefficient_presentation, lifted)

    def descend_scalar(value):
        lifted = _owned_engine_element(coefficient_presentation, presentation_ring(value))
        return ring._descend_coefficient_from_presentation(lifted)

    from sage.categories.fields import Fields as SageFields

    coefficient_field = presentation_ring.base_ring()
    assert coefficient_field in SageFields(), (
        f"cannot compute the kernel of {morphism} with this algorithm: {ring} must be a "
        f"quotient of a polynomial ring over a field, and here the coefficients are {coefficient_field}"
    )

    # Singular's syz entry point requires a multivariate polynomial parent,
    # even in one variable.  Cross only this backend representation.
    if presentation_ring.ngens() == 1 and "multi_polynomial" not in type(presentation_ring).__module__:
        singular_ring = _SagePolynomialRing(
            coefficient_field,
            presentation_ring.variable_names(),
            implementation="singular",
        )
    else:
        singular_ring = presentation_ring

    def to_singular(value):
        return singular_ring(presentation_ring(value))

    def from_singular(value):
        return descend_scalar(presentation_ring(value))

    source_labels = tuple(domain.module_generating_set())
    target_labels = tuple(codomain.module_generating_set())
    source_relations = _presentation_matrix(domain)
    target_relations = _presentation_matrix(codomain)
    n = len(source_labels)
    m = len(target_labels)
    assert n > 0 and m > 0, (
        f"cannot compute the kernel of {morphism} with this algorithm: its domain has {n} "
        f"generators and its codomain {m}, and both must be nonzero"
    )

    def singular_relation_module(relations, width):
        free = SageFreeModule(singular_ring, width)
        vectors = [
            free(tuple(to_singular(lift_scalar(entry)) for entry in row))
            for row in _matrix_coordinate_rows(relations)
        ]
        for relation in coefficient_relations:
            coefficient = to_singular(backend_coefficient_relation(relation))
            for position in range(width):
                vectors.append(
                    free(
                        tuple(
                            coefficient if index == position else singular_ring.zero()
                            for index in range(width)
                        )
                    )
                )
        if not vectors:
            vectors.append(free.zero())
        return Sequence(vectors, universe=free, check=False, immutable=True)

    def singular_module_matrix(module_vectors, width):
        vectors = tuple(module_vectors)
        return matrix(
            singular_ring,
            width,
            len(vectors),
            [
                vectors[column][row]
                for row in range(width)
                for column in range(len(vectors))
            ],
        )

    coordinate_columns = []
    for source_label in source_labels:
        image = morphism(domain.module_generator(source_label))
        coefficients = codomain.framing_coefficients(image)
        coordinate_columns.append(tuple(to_singular(lift_scalar(coefficients.get(label, ring.zero()))) for label in target_labels))
    f_matrix = matrix(
        singular_ring,
        m,
        n,
        [coordinate_columns[column][row] for row in range(m) for column in range(n)],
    )
    source_relation_module = singular_relation_module(source_relations, n)
    target_relation_module = singular_relation_module(target_relations, m)
    # ``mor_kernel`` internally computes the same ``modulo(f_matrix, N)``
    # before quotienting by the source relations.  Repeat only that first
    # maintained operation so the owned kernel can retain the corresponding
    # generator lifts and hence its actual inclusion into ``domain``.  The
    # presentation itself comes exclusively from ``mor_kernel`` below.
    kernel_lifts = tuple(
        ff.modulo(
            f_matrix,
            target_relation_module,
            ring=singular_ring,
        )
    )
    kernel_presentation = ff.homolog__lib.mor_kernel(
        f_matrix,
        source_relation_module,
        target_relation_module,
        ring=singular_ring,
    )

    kernel_count = len(kernel_lifts)
    kernel_labels = Sets.Δ[kernel_count - 1]
    if kernel_count:
        kernel_columns = matrix(
            singular_ring,
            n,
            kernel_count,
            [kernel_lifts[column][row] for row in range(n) for column in range(kernel_count)],
        )
    else:
        kernel_columns = matrix(singular_ring, n, 0, [])

    kernel_relation_rows = [
        tuple(from_singular(entry) for entry in vector)
        for vector in kernel_presentation
        if any(entry != 0 for entry in vector)
    ]
    relation_labels = Sets.Δ[len(kernel_relation_rows) - 1]
    relation_matrix = _matrix_space_like(
        domain,
        len(kernel_relation_rows),
        kernel_count,
    ).from_rows(tuple(kernel_relation_rows))
    presentation = _presentation_from_relation_rows(
        ring,
        kernel_labels,
        relation_labels,
        relation_matrix,
    )
    generator_images = {
        label: domain.linear_combination(
            {source_label: from_singular(kernel_lifts[int(label)][position]) for position, source_label in enumerate(source_labels) if kernel_lifts[int(label)][position] != 0}
        )
        for label in kernel_labels
    }

    def lift_from_domain(kernel, element):
        if element.parent() is not domain:
            element = domain(element)
        if kernel_count == 0:
            return kernel.zero() if element == domain.zero() else None
        coefficients = domain.framing_coefficients(element)
        requested = matrix(
            singular_ring,
            1,
            n,
            [to_singular(lift_scalar(coefficients.get(label, ring.zero()))) for label in source_labels],
        )
        spanning = kernel_columns.augment(
            singular_module_matrix(source_relation_module, n)
        )
        coefficients_in_spanning = _singular_module_lift(spanning, requested.transpose())
        if coefficients_in_spanning is None:
            return None
        lifted = matrix(singular_ring, coefficients_in_spanning)
        return kernel.linear_combination({label: from_singular(lifted[position, 0]) for position, label in enumerate(kernel_labels) if lifted[position, 0] != 0})

    return _presented_module_from_morphism(
        presentation,
        _subobject_ambient=domain,
        _subobject_generator_images=generator_images,
        _subobject_lift=lift_from_domain,
    )


def _presentation_from_relation_rows(
    base_ring,
    labels,
    relation_labels,
    relations,
):

    free_owner = relations.domain()
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import _fresh_free_module_on
    target = _fresh_free_module_on(free_owner.base_ring(), labels)
    source = _fresh_free_module_on(free_owner.base_ring(), relation_labels)
    images = {label: _relation_element(target, row) for label, row in zip(source.module_generating_set(), _matrix_coordinate_rows(relations), strict=True)}
    return source.module_category().Mor(source, target)(images)


def _presented_module_from_morphism(
    presentation,
    *,
    _cokernel_morphism=None,
    _extra_categories=(),
    _extra_construction_data=None,
    _subobject_ambient=None,
    _subobject_generator_images=None,
    _subobject_lift=None,
    _subobject_inclusion_factory=None,
    _biproduct_factors=None,
    _require_torsion=False,
):
    r"""Return ``coker(presentation)`` in ``R-Mod`` with its selected module presentation."""
    # The cokernel here is taken in the module category.  A stricter structured
    # morphism (lattice/form/equivariant/etc.) must first be read as its
    # underlying R-linear arrow; otherwise later presentation constructions
    # incorrectly inherit the stricter Mor object.

    presentation_source = presentation.domain()
    presentation_target = presentation.codomain()
    presentation = presentation_source.module_category().Mor(
        presentation_source,
        presentation_target,
    )(presentation)
    codomain = presentation.codomain()
    base_ring = codomain.base_ring()
    assert presentation.domain().has_selected_module_resolution(), (
        f"cannot form the cokernel of {presentation}: its domain must be a {base_ring}-module "
        f"with chosen generators, but it is in {presentation.domain().category()}"
    )
    assert presentation.domain().module_generating_set().cardinality().is_finite(), (
        f"cannot form the cokernel of {presentation}: its domain must be finitely generated, "
        f"but its generators are indexed by {presentation.domain().module_generating_set()}"
    )
    assert codomain in ModulesWithChosenFinitePresentation(base_ring), (
        f"cannot form the cokernel of {presentation}: its codomain {codomain} must be finitely "
        f"presented with chosen generators and relations, but it is in {codomain.category()}"
    )
    engine = _engine_ring(base_ring)

    labels = codomain.module_generating_set()
    existing = _presentation_matrix(codomain)

    added_rows = []
    label_ranking = labels.ranking_map()
    width = int(labels.cardinality())
    for source_label in presentation.domain().module_generating_set():
        image = presentation(presentation.domain().module_generator(source_label))
        coefficients = codomain.framing_coefficients(image)
        row = [base_ring.zero()] * width
        for label, coefficient in coefficients.items():
            row[int(label_ranking(label))] = coefficient
        added_rows.append(tuple(row))
    from itertools import chain

    existing_rows = _matrix_coordinate_rows(existing)
    existing_count = len(existing_rows)
    relations_matrix = _matrix_space_like(
        codomain,
        existing_count + len(added_rows),
        width,
    ).from_rows(chain(existing_rows, added_rows))
    relations = relations_matrix

    torsion_decision = Unknown
    match base_ring in PrincipalIdealDomains():
        case True:
            fraction_field_map = base_ring.fraction_field_map()
            field = fraction_field_map.codomain()
            generic_relations = field.matrix_space(
                relations_matrix.nrows(),
                relations_matrix.ncols(),
            ).from_rows(
                tuple(
                    tuple(fraction_field_map(coefficient) for coefficient in row)
                    for row in _matrix_coordinate_rows(relations_matrix)
                )
            )
            torsion_decision = int(_engine_matrix(generic_relations).rank()) == width
        case False:
            pass
    match (_require_torsion, torsion_decision):
        case (True, True):
            pass
        case (True, False):
            raise ValueError(
                f"the cokernel of {presentation} is not a torsion {base_ring}-module: it has a nonzero free summand"
            )
        case (True, _):
            raise AssertionError(
                f"cannot decide whether the cokernel of {presentation} is a torsion {base_ring}-module: "
                "the rank of its relation matrix over the fraction field could not be computed"
            )
        case _:
            pass
    match torsion_decision is True:
        case True:
            _extra_categories = (
                *_extra_categories,
                Modules(base_ring).FinitelyPresented().Torsion(),
            )
        case False:
            pass
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FramedFreeModules,
    )

    # When every selected relation is zero, the chosen generators themselves
    # are a basis: coker(0 : R^J -> R^I) = R^I.  Keep the selected quotient
    # and its presentation, while declaring that basis at the module owner.
    # In particular a free functor must retain this exact module, not replace
    # it by its framing source merely to acquire a Free placement.
    match all(
        coefficient == base_ring.zero()
        for row in chain(existing_rows, added_rows)
        for coefficient in row
    ):
        case True:
            _extra_categories = (*_extra_categories, FramedFreeModules(base_ring).FinitelyGenerated())

    if (
        existing_count == 0
        and presentation.domain() in FramedFreeModules(base_ring)
        and codomain in FramedFreeModules(base_ring)
    ):
        selected_presentation = presentation
    else:
        existing_labels = codomain.presentation().domain().module_generating_set() if codomain in _SelectedFinitePresentationModules(base_ring) else Sets.Δ[existing_count - 1]
        added_labels = presentation.domain().module_generating_set()
        relation_labels = Sets().coproduct(
            indexed_family(
                Sets.Δ[1],
                lambda index: existing_labels if int(index) == 0 else added_labels,
            )
        )
        selected_presentation = _presentation_from_relation_rows(
            base_ring,
            labels,
            relation_labels,
            relations,
        )

    # A presentation written directly over a localization is still a finite
    # presentation over the source ring after clearing one unit denominator
    # per relation row.  Build that source presentation first and then apply
    # exact module localization.  This avoids using a fraction-field engine as
    # though it were the local ring itself (which would make nonunits in the
    # maximal ideal invertible and corrupt cokernels/equality).
    if base_ring in LocalizationRings():
        from dzack_research.preamble.categories.modules.localizations import _localized_module

        source_ring = base_ring.localization_source()
        local_rows = tuple(_matrix_coordinate_rows(relations))
        source_rows = []
        for row in local_rows:
            fractions = tuple(base_ring.localization_fraction_data(coefficient) for coefficient in row)
            denominators = tuple(denominator for _numerator, denominator in fractions)
            cleared = []
            for position, (numerator, _denominator) in enumerate(fractions):
                multiplier = source_ring.one()
                for other_position, denominator in enumerate(denominators):
                    if other_position != position:
                        multiplier *= denominator
                cleared.append(numerator * multiplier)
            source_rows.append(tuple(cleared))

        source_relation_labels = Sets.Δ[len(source_rows) - 1]
        source_relations = source_ring._fresh_free_module_on(source_relation_labels)
        source_generators = source_ring._fresh_free_module_on(labels)
        source_presentation = source_relations.module_category().Mor(source_relations, source_generators)(
            {
                relation_label: source_generators.linear_combination(
                    {
                        label: coefficient
                        for label, coefficient in zip(labels, row, strict=True)
                        if coefficient != source_ring.zero()
                    }
                )
                for relation_label, row in zip(source_relation_labels, source_rows, strict=True)
            }
        )
        source_quotient = source_presentation.cokernel()
        localization = base_ring.localization_functor()
        local_extra_categories = list(_extra_categories)
        local_extra_data = dict(_extra_construction_data or {})
        local_extra_data["cokernel_morphism"] = _cokernel_morphism
        if _biproduct_factors is not None:
            local_extra_categories.append(BiproductModules(base_ring))
            local_extra_data["biproduct_factors"] = _biproduct_factors

        localized = _localized_module(
            source_quotient,
            base_ring,
            localization,
            selected_presentation_data={
                "relation_matrix": relations_matrix,
                "presentation": selected_presentation,
            },
            subobject_ambient=_subobject_ambient,
            subobject_generator_images=_subobject_generator_images,
            subobject_lift=_subobject_lift,
            subobject_inclusion_factory=_subobject_inclusion_factory,
            extra_categories=tuple(local_extra_categories),
            extra_construction_data=local_extra_data,
        )
        return localization.adopt_object_image(source_quotient, localized)

    from sage.categories.rings import Rings as SageRings

    pid_backend = False
    if engine in SageRings():
        from sage.modules.free_module import FreeModule as SageFreeModule

        from dzack_research.preamble.categories.rings.commutative_algebra import (
            AdicCompletions,
        )

        match base_ring:
            case _ if base_ring in AdicCompletions():
                # A capped-precision adic engine advertises PID linear algebra,
                # but Sage's free-submodule echelon constructor divides by a
                # nonunit pivot and leaves the ring.  The presentation is exact
                # owned data, so the owned free cover and the relation matrix
                # are retained instead.
                free = selected_presentation.codomain()
                relation_submodule = None
            case _:
                free = SageFreeModule(engine, int(labels.cardinality()))
                backend_rows = [free(tuple(_engine_element(base_ring, coefficient) for coefficient in row)) for row in _matrix_coordinate_rows(relations)]
                relation_submodule = free.zero_submodule() if not backend_rows else free.submodule(backend_rows)
        # Sage's FGP implementation calls ``_clear_denom`` internally in
        # its Smith/optimization algorithms.  The live Smith-form surface of
        # this project is the integral ``ZZ`` specialization; other Sage rings
        # use the general finite-presentation parent below rather than being
        # admitted to FGP by probing an incidental matrix method.
        pid_backend = engine is SageZZ
    if pid_backend:
        from sage.modules.fg_pid.fgp_module import FGP_Module

        quotient = _new_presented_module(
            engine=FGP_Module(free, relation_submodule, check=False),
            free_module=free,
            relation_submodule=relation_submodule,
            base_ring=base_ring,
            module_generating_set=labels,
            relation_matrix=relations,
            presentation=selected_presentation,
            cokernel_morphism=_cokernel_morphism,
            subobject_ambient=_subobject_ambient,
            subobject_generator_images=_subobject_generator_images,
            subobject_lift=_subobject_lift,
            subobject_inclusion_factory=_subobject_inclusion_factory,
            biproduct_factors=_biproduct_factors,
            extra_categories=_extra_categories,
            extra_construction_data=_extra_construction_data,
        )
    elif engine in SageRings():
        quotient = _new_presented_module(
            free_module=free,
            relation_submodule=relation_submodule,
            base_ring=base_ring,
            module_generating_set=labels,
            relation_matrix=relations,
            presentation=selected_presentation,
            cokernel_morphism=_cokernel_morphism,
            subobject_ambient=_subobject_ambient,
            subobject_generator_images=_subobject_generator_images,
            subobject_lift=_subobject_lift,
            subobject_inclusion_factory=_subobject_inclusion_factory,
            biproduct_factors=_biproduct_factors,
            extra_categories=_extra_categories,
            extra_construction_data=_extra_construction_data,
        )
    else:
        # The base ring has no Sage computation ring behind it, so the
        # cover is the owned free module and the presentation is the only
        # datum; equality of elements is not decided here.
        quotient = _new_presented_module(
            free_module=_cover_free_module(codomain, labels),
            relation_submodule=None,
            base_ring=base_ring,
            module_generating_set=labels,
            relation_matrix=relations,
            presentation=selected_presentation,
            cokernel_morphism=_cokernel_morphism,
            subobject_ambient=_subobject_ambient,
            subobject_generator_images=_subobject_generator_images,
            subobject_lift=_subobject_lift,
            subobject_inclusion_factory=_subobject_inclusion_factory,
            biproduct_factors=_biproduct_factors,
            extra_categories=_extra_categories,
            extra_construction_data=_extra_construction_data,
        )

    return quotient


__all__ = [
    "_presentation_matrix",
]
