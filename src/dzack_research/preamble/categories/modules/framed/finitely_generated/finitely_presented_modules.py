"""Finitely presented modules with a selected finite presentation.

A presented module is an owned parent.  Over a PID with a Smith form its
engine is Sage's FGP module over the engine ring; over another Sage ring it
holds a Sage free cover and relation submodule; over a ring with no Sage
engine it holds the owned free cover alone and cannot decide equality.  The
engine is read through the selected-presentation backend method ``_smith_engine``
and every Smith-form computation is an explicit crossing into it.
"""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.misc.misc_c import prod
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import ModuleElement
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    ArrowCategory,
    Isomorphism,
)
from dzack_research.preamble.categories.abstract_categories.constructions import TensorProduct
from dzack_research.preamble.categories.modules.base_change import base_change_scalar
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    framing_morphism,
    module_coefficients,
    module_embedding,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    BiproductModules,
    FreeResolution,
    Modules,
    ModuleSubobjects,
    ModulesWithChosenFinitePresentation,
    VectorSpaces,
    _biproduct_label,
    _engine_matrix,
    _refine_matrix_hom,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    LocalRings,
    OwnedCategoryOverBaseRing,
    OwnedFields,
    OwnedIntegralDomains,
    PrincipalIdealDomains,
    _engine_element,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.cardinals import Cardinalities, cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_filter,
    finite_ordered_image,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import CoproductOfFamily, Sets
from dzack_research.preamble.owned_category import object_of


def _free_cover_owner(module):
    r"""Return a selected free cover owning fresh free-module construction."""
    presentation = getattr(module, "presentation", None)
    if presentation is not None:
        try:
            return presentation().codomain()
        except AttributeError, TypeError, ValueError:
            pass
    return module


def _matrix_space_like(module, nrows, ncols):
    r"""Return one finite matrix Hom using ``module``'s selected free cover."""
    owner = _free_cover_owner(module)
    source = owner._fresh_free_module_on(Sets.Δ[int(ncols) - 1])
    target = owner._fresh_free_module_on(Sets.Δ[int(nrows) - 1])

    return module_homset(source, target)


class _SelectedFinitePresentationModules(OwnedCategoryOverBaseRing):
    r"""Implementation refinement for modules with a selected finite presentation."""

    @classmethod
    def _repr_object_names(cls):
        return "modules with a represented selected finite-presentation backend"

    def super_categories(self):
        return [ModulesWithChosenFinitePresentation(self.base_ring())]

    class ParentMethods:
        def __init__(
            self,
            relation_matrix,
            presentation,
            cokernel_morphism=None,
            **rest,
        ) -> None:
            self._preamble_relation_matrix = relation_matrix
            self._preamble_presentation = presentation
            self._preamble_cokernel_morphism = cokernel_morphism
            super().__init__(**rest)

        def base_ring(self):
            return self._preamble_base_ring

        def _same_selected_presentation_as(self, other):
            r"""Return whether ``other`` represents this selected cokernel."""
            try:
                same_ring = other.base_ring() is self.base_ring()
                same_presentation = other.presentation() == self.presentation()
            except AttributeError, TypeError, ValueError:
                return False
            return bool(same_ring and same_presentation)

        def _same_presentation_module(
            self,
            labels,
            *,
            _extra_categories=(),
            _extra_construction_data=None,
        ):
            r"""Return a fresh module carrying this chosen finite presentation."""
            if labels != self.module_generating_set():
                raise ValueError("the requested framing differs from the selected presentation")
            return FinitelyPresentedModule(
                self.presentation(),
                _extra_categories=tuple(_extra_categories),
                _extra_construction_data=_extra_construction_data,
            )

        def _presented_biproduct_with(self, other, labels, factors):
            r"""Return the finite-presentation realization of ``self direct_sum other``."""
            try:
                left_relations = _presentation_rows(self)
                right_relations = _presentation_rows(other)
            except AttributeError, NotImplementedError, TypeError, ValueError:
                return NotImplemented
            size = labels.cardinality()
            if not size.is_finite():
                return NotImplemented
            width = int(size.finite_value())
            ring = self.base_ring()
            left_labels = self.module_generating_set()
            right_labels = other.module_generating_set()
            rows = []
            for relation in left_relations:
                row = [ring.zero()] * width
                for position, coefficient in enumerate(relation):
                    if coefficient:
                        left_label = left_labels.unrank(position)
                        row[labels.rank(_biproduct_label(labels, 0, left_label))] = coefficient
                rows.append(row)
            for relation in right_relations:
                row = [ring.zero()] * width
                for position, coefficient in enumerate(relation):
                    if coefficient:
                        right_label = right_labels.unrank(position)
                        row[labels.rank(_biproduct_label(labels, 1, right_label))] = coefficient
                rows.append(row)
            relations = _matrix_space_like(self, len(rows), width).from_rows(tuple(tuple(row) for row in rows))
            presentation = _presentation_from_relation_rows(
                ring,
                labels,
                Sets.Δ[len(rows) - 1],
                relations,
            )
            return FinitelyPresentedModule(
                presentation,
                _biproduct_factors=factors,
            )

        @cached_method
        def cokernel_projection(self):
            r"""Return the canonical quotient map when this object is a selected cokernel."""
            morphism = self._preamble_cokernel_morphism
            if morphism is None:
                raise ValueError("this finitely presented module was not constructed as a cokernel")
            return module_homset(morphism.codomain(), self)({label: self.module_generator(label) for label in morphism.codomain().module_generating_set()})

        def tensor_product(self, other):

            return TensorProduct(self, other)

        @cached_method
        def free_resolution(self):
            r"""Return the selected length-one free resolution over the represented PID."""

            ring = self.base_ring()
            degree_zero = self.presentation().codomain()
            relation_matrix = _engine_matrix(self.presentation_matrix()).row_module().basis_matrix()
            relation_labels = Sets.Δ[int(relation_matrix.nrows()) - 1]
            degree_one = degree_zero._fresh_free_module_on(relation_labels)
            zero = degree_zero._fresh_free_module_on(Sets.Δ[-1])
            target_labels = degree_zero.module_generating_set()

            def image(label):
                row = relation_matrix.row(int(relation_labels.rank(label)))
                return degree_zero.linear_combination(
                    {target_label: ring._from_engine_element(coefficient) for target_label, coefficient in zip(target_labels, row, strict=True) if coefficient}
                )

            return FreeResolution(
                self,
                degree_zero,
                degree_one,
                module_embedding(degree_one, degree_zero, image),
                self.presentation_projection(),
                zero,
            )

        def presentation(self):
            r"""Return the selected relation morphism ``F_1 -> F_0``."""
            return self._preamble_presentation

        def presentation_matrix(self):
            r"""Return its relation rows in the selected target framing."""
            return self._preamble_relation_matrix

        def _selected_presentation_rows(self):
            return _matrix_coordinate_rows(self.presentation_matrix())

        def _selected_module_coefficients(self, element):
            coordinates = self._framing_coordinates(element)
            return {label: self.base_ring()(coordinates[label]) for label in self.module_generating_set() if coordinates[label] != 0}

        def _represented_kernel_of_morphism(self, morphism):
            if self not in (morphism.domain(), morphism.codomain()):
                return NotImplemented
            if morphism.codomain() is self and morphism.domain() is self.presentation().codomain() and morphism == self.presentation_projection():
                return self.presentation().image()
            if morphism.domain()._selected_presentation_rows() is None or morphism.codomain()._selected_presentation_rows() is None:
                return NotImplemented
            if self.base_ring() in PrincipalIdealDomains():
                return _pid_presentation_kernel(morphism)
            return _singular_presentation_kernel(morphism)

        def _represented_cokernel_of_morphism(self, morphism):
            if morphism.codomain() is not self:
                return NotImplemented
            return FinitelyPresentedModule(morphism, _cokernel_morphism=morphism)

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
            return FinitelyPresentedModule(
                presentation,
                _extra_categories=extra_categories,
                _extra_construction_data=extra_construction_data,
            )

        def subobject_on(self, module_generators):
            r"""Return the submodule generated by one finite family as an exact image."""

            if hasattr(module_generators, "index_set") and callable(getattr(module_generators, "value", None)):
                labels = module_generators.index_set()
                size = labels.cardinality()
                if not size.is_finite():
                    raise TypeError("subobject generators must be a finite indexed family")
                generator = module_generators.value
            else:
                generators = finite_ordered_set(module_generators)
                labels = Sets.Δ[int(generators.cardinality()) - 1]

                def generator(label):
                    return generators.unrank(int(label))

            source = self.presentation().codomain()._fresh_free_module_on(labels)
            spanning = module_homset(source, self)(lambda label: self(generator(label)))

            if self.base_ring() in LocalRings():
                spans_all = spanning.is_surjective_by_nakayama()
            else:
                try:
                    spans_all = spanning.is_surjective()
                except NotImplementedError:
                    spans_all = False
            if spans_all:

                def lift_from_ambient(image, element):
                    element = element if element.parent() is self else self(element)
                    return image.linear_combination(module_coefficients(element, self))

                return FinitelyPresentedModule(
                    self.presentation(),
                    _subobject_ambient=self,
                    _subobject_generator_images=lambda label: self.module_generator(label),
                    _subobject_lift=lift_from_ambient,
                )

            kernel = spanning.kernel()
            return FinitelyPresentedModule(
                kernel.inclusion(),
                _subobject_ambient=self,
                _subobject_generator_images=lambda label: spanning(source.module_generator(label)),
            )

        submodule = subobject_on

        def fitting_ideal(self, index):
            r"""Return ``Fitt_index(M)`` from the selected finite presentation."""

            index = int(index)
            if index < 0:
                raise ValueError("a Fitting-ideal index is nonnegative")
            ring = self.base_ring()

            # Fitting ideals commute with arbitrary base change, hence in
            # particular with localization.  A LocalizedModule remembers its
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
                    source = self.localization_source_module()
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
            return ring.ideal(*(tuple(ring._from_engine_element(_engine_ring(ring)(minor)) for minor in minors) or (ring.zero(),)))

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
                return ring.ideal(*(tuple(ring._from_engine_element(_engine_ring(ring)(entry)) for entry in entries) or (ring.zero(),)))

            raise NotImplementedError("annihilator of this general finite presentation requires a commutative-algebra backend")

        def support(self):
            r"""Return ``Supp(M)=V(Fitt_0(M))`` in ``Spec(R)``."""
            return self.base_ring().spectrum().V(self.fitting_ideal(0))

        def minimal_module_generators(self):
            r"""Return a minimal selected generating set over a local base ring.

            By Nakayama, a set of generators is minimal exactly when its image
            is a basis of ``M/mM``.  The residue module owns the represented
            choice of a basis subfamily of its selected generators.
            """
            ring = self.base_ring()
            if ring not in LocalRings():
                raise TypeError("minimal generators via Nakayama require a represented local base ring")
            residue_module = self.residue_module()
            basis_labels = residue_module.basis_generator_labels()
            return finite_ordered_image(
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
            return SageZZ(int(self.number_of_module_generators()) - relation_matrix.rank())

        def _represented_vector_space_basis_generator_labels(self):
            r"""Choose a basis subfamily of the selected generators over a field."""
            if self.base_ring() not in OwnedFields():
                return NotImplemented
            relation_matrix = _engine_matrix(self.presentation_matrix())
            pivot_columns = frozenset(relation_matrix.echelon_form().pivots())
            labels = self.module_generating_set()
            positions = finite_ordered_filter(
                Sets.Δ[int(self.number_of_module_generators()) - 1],
                lambda position: int(position) not in pivot_columns,
                name="Vector-space basis generator positions",
            )
            return finite_ordered_image(
                positions,
                lambda position: labels.unrank(int(position)),
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

        def module_generating_set(self):
            return self._preamble_module_generating_set

        def number_of_module_generators(self):
            return self.module_generating_set().cardinality()

        def module_generator(self, label):
            custom = self.__dict__.get("_preamble_module_generator_function")
            if custom is not None:
                return custom(label)
            labels = self.module_generating_set()
            position = labels.rank(label)
            if position is None:
                raise ValueError(f"{label!r} is not a module-generator label")
            return self._cover_generator(position)

        @cached_method
        def module_generators(self):
            r"""Return the indexed family of selected framing images."""

            return indexed_family(
                self.module_generating_set(),
                self.module_generator,
                name="Presented-module generator family",
            )

        def framing_morphism(self):

            source = self.presentation().codomain()
            return framing_morphism(source, self, self.module_generator)

        def _from_coordinates(self, coordinates):
            r"""Return the element with these coordinates in the chosen framing.

            Protected contract: the internal Hom model installed by
            ``module_morphisms`` reads its elements back through this name.
            """
            custom = self.__dict__.get("_preamble_module_from_coordinates_function")
            if custom is not None:
                return custom(coordinates)
            return self.linear_combination(dict(zip(self.module_generating_set(), coordinates, strict=True)))

        def _smith_engine(self):
            r"""Sage's FGP module over the engine ring, or ``None``.

            This is the only accessor of the Smith engine.  Protected contract:
            the discriminant-module, internal-Hom and algebra-presentation
            modules cross here for Smith-form data and convert every result
            back to an owned object before returning it.
            """
            engine = self.__dict__.get("_preamble_pid_engine")
            if engine is None:
                # An internal Hom is presented by its endpoint-determined
                # model, whose Smith engine is built on first use.
                factory = self.__dict__.get("_preamble_pid_engine_factory")
                if factory is not None:
                    engine = self._preamble_pid_engine = factory()
            return engine

        def _framing_coordinates(self, element):
            r"""Coordinates of ``element`` as an indexed family on the chosen framing.

            Protected contract: ``module_coefficients`` in ``module_morphisms``
            reads the coordinates of an element of a presented module here.
            """
            custom = self.__dict__.get("_preamble_module_coordinate_function")
            if custom is not None:
                ring = self.base_ring()
                labels = self.module_generating_set()
                coordinates = tuple(custom(element))
                owned = tuple(
                    coordinate if getattr(coordinate, "parent", lambda: None)() is ring else ring._from_engine_element(_engine_ring(ring)(coordinate))
                    for coordinate in coordinates
                )
                if len(owned) != int(labels.cardinality()):
                    raise ValueError("the selected coordinate function has the wrong finite length")

                return indexed_family(
                    labels,
                    lambda label: owned[int(labels.rank(label))],
                    name=f"Framing coordinates of {element}",
                )
            return self._cover_coordinates(element)

        @cached_method
        def _selected_presentation_smith_backend(self):
            r"""Privately reduce the selected relation matrix over a PID.

            The input is the selected presentation morphism itself, so the
            returned basis changes refer to the selected relation and target
            framings.  This is backend state local to the presenting module;
            callers receive owned invariants or an owned presentation witness.
            """

            ring = self.base_ring()
            if ring not in PrincipalIdealDomains():
                raise NotImplementedError("selected-presentation Smith reduction is represented here over a PID")
            backend_relation_matrix = _engine_matrix(self.presentation_matrix())
            try:
                return backend_relation_matrix.smith_form()
            except (AttributeError, NotImplementedError) as error:
                raise NotImplementedError(f"the selected exact backend does not compute Smith form over {ring}") from error

        @cached_method
        def _invariants_with_units(self):
            r"""Read the diagonal presentation, retaining unit and free coordinates."""
            normalization = self.invariant_factor_presentation()
            diagonal = normalization.codomain().arrow()
            ring = self.base_ring()
            target_rank = int(diagonal.codomain().module_generating_set().cardinality())
            diagonal_rank = min(diagonal.parent().nrows(), diagonal.parent().ncols())
            return tuple(diagonal[position, position] if position < diagonal_rank else ring.zero() for position in range(target_rank))

        def rank(self):
            r"""Return the rank of the free summand over a PID."""

            if self.base_ring() not in PrincipalIdealDomains():
                raise NotImplementedError("rank from invariant factors is represented here over a PID")
            return cardinal(sum(1 for invariant in self._invariants_with_units() if invariant == 0))

        def is_torsion(self):
            r"""Read torsion off the invariant factors over a PID, else take the generic fibre."""
            if self.base_ring() not in PrincipalIdealDomains():
                return super().is_torsion()
            return self.rank() == 0

        def is_torsion_free(self):
            r"""Over a PID ``M`` is torsion-free exactly when no invariant factor is a nonzero non-unit."""
            if self.base_ring() not in PrincipalIdealDomains():
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
            if self.base_ring() not in PrincipalIdealDomains():
                inherited = getattr(super(), "is_zero", None)
                if inherited is None:
                    raise NotImplementedError("zero testing from selected invariant factors is represented here over a PID")
                return inherited()
            return all(invariant.is_unit() for invariant in self._invariants_with_units())

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
            assert ring in PrincipalIdealDomains(), (
                f"the cardinality of a module presented over {ring} is read from an "
                "invariant-factor decomposition, which a principal ideal domain supplies"
            )
            cyclic_orders = tuple(
                ring.quotient_ring(ring.ideal(invariant)).cardinality()
                for invariant in self._invariants_with_units()
                if invariant != 0 and not invariant.is_unit()
            )
            return ring.cardinality() ** self.rank() * prod(cyclic_orders, Cardinalities().one())

        @cached_method
        def invariant_factor_presentation(self):
            r"""Normalize the selected presentation through the PID structure theorem.

            For the selected arrow ``p : F_1 -> F_0`` this returns an
            isomorphism in ``Arr(R-Mod)`` from ``p`` to a diagonal presentation
            ``d : F'_1 -> F'_0``.  The two vertical isomorphisms are the source
            and target basis changes.  Thus no chosen relation framing is lost.
            """

            ring = self.base_ring()
            if ring not in PrincipalIdealDomains():
                raise NotImplementedError("invariant-factor presentation normalization is guaranteed here over a PID")
            presentation = self.presentation()
            diagonal_backend, row_change_backend, column_change_backend = self._selected_presentation_smith_backend()

            source_labels = finite_ordered_set(range(int(presentation.domain().module_generating_set().cardinality())))
            target_labels = finite_ordered_set(range(int(presentation.codomain().module_generating_set().cardinality())))
            free_owner = presentation.codomain()
            normalized_source = free_owner._fresh_free_module_on(source_labels)
            normalized_target = free_owner._fresh_free_module_on(target_labels)

            def owned_matrix_morphism(domain, codomain, backend_matrix):
                homset = _refine_matrix_hom(module_homset(domain, codomain))
                rows = [[ring._from_engine_element(backend_matrix[row, column]) for column in range(int(backend_matrix.ncols()))] for row in range(int(backend_matrix.nrows()))]
                return homset.from_rows(rows)

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

            arrows = ArrowCategory(Modules(ring))
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
            return Isomorphism(forward, inverse)

        @cached_method
        def invariant_factors(self):
            r"""Return the indexed family of non-unit invariant factors."""

            invariants = self._invariants_with_units()
            positions = Sets.Δ[len(invariants) - 1]
            retained = finite_ordered_filter(
                positions,
                lambda position: not invariants[int(position)].is_unit(),
            )
            reduced_positions = Sets.Δ[int(retained.cardinality()) - 1]
            return finite_indexed_family(
                reduced_positions,
                lambda position: invariants[int(retained.unrank(int(position)))],
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
            if ring not in PrincipalIdealDomains():
                raise NotImplementedError(
                    "finite-free trivialization from invariant factors is represented here over a PID"
                )
            if not self.is_torsion_free():
                raise ValueError(
                    "a finitely presented PID module with torsion is not finite free"
                )

            normalization = self.invariant_factor_form()
            normalized = normalization.codomain()
            labels = normalized.module_generating_set()
            free = self.presentation().codomain()._fresh_free_module_on(labels)
            normalized_to_free = module_homset(normalized, free)(
                {label: free.module_generator(label) for label in labels}
            )
            free_to_normalized = module_homset(free, normalized)(
                {label: normalized.module_generator(label) for label in labels}
            )
            return Isomorphism(normalized_to_free, free_to_normalized) * normalization

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
            try:
                point_parent = point.parent()
            except AttributeError:
                point = spectrum(point)
            else:
                if point_parent is not spectrum:
                    point = spectrum(point)
            from dzack_research.preamble.categories.functors.module_localization import (
                module_localization_functor,
            )

            trivialization = self.finite_free_trivialization()
            localization = module_localization_functor(point.local_ring())
            return Isomorphism(
                localization(trivialization.forward()),
                localization(trivialization.inverse()),
            )

        def presentation_projection(self):
            r"""Return the selected quotient map ``F_0 -> M``."""

            source = self.presentation().codomain()
            return module_homset(source, self)({label: self.module_generator(label) for label in source.module_generating_set()})

        def torsion_free_quotient_projection(self):
            r"""Return ``M -> M/Tor(M)`` from invariant-factor coordinates."""
            normalization = self.invariant_factor_form()
            normalized = normalization.codomain()
            invariants = self._invariants_with_units()

            positions = Sets.Δ[len(invariants) - 1]
            retained_positions = finite_ordered_filter(
                positions,
                lambda position: not invariants[int(position)].is_unit(),
            )
            free_positions = finite_ordered_filter(
                positions,
                lambda position: invariants[int(position)] == self.base_ring().zero(),
            )
            target = self.presentation().codomain()._fresh_free_module_on(free_positions)
            normalized_projection = module_homset(normalized, target)(
                {
                    label: (
                        target.module_generator(retained_positions.unrank(int(label)))
                        if retained_positions.unrank(int(label)) in free_positions
                        else target.zero()
                    )
                    for label in normalized.module_generating_set()
                }
            )
            return normalized_projection * normalization.forward()

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
            if self._smith_engine() is None:
                return f"Finitely presented module on {self.number_of_module_generators()} module generators over {self.base_ring()}"
            return (
                f"Finitely presented module on {self.number_of_module_generators()} module generators over {self.base_ring()} with invariant factors {self.invariant_factors()}"
            )

        def base_change(self, ring_map):
            r"""Transport the selected finite presentation along ``R -> S``."""

            presentation = self.presentation()
            source = presentation.domain().base_change(ring_map)
            target = presentation.codomain().base_change(ring_map)
            relation_labels = source.module_generating_set()
            images = {
                relation_label: sum(
                    (
                        target.scalar_multiple(
                            base_change_scalar(ring_map, coefficient),
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
            return FinitelyPresentedModule(module_homset(source, target)(images))


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
    full_normalized = FinitelyPresentedModule(diagonal_presentation)
    invariants = module._invariants_with_units()

    invariant_positions = Sets.Δ[len(invariants) - 1]
    retained_positions = finite_ordered_filter(
        invariant_positions,
        lambda position: not invariants[int(position)].is_unit(),
    )

    ring = module.base_ring()
    free_owner = module.presentation().codomain()
    reduced_labels = Sets.Δ[int(retained_positions.cardinality()) - 1]
    reduced_target = free_owner._fresh_free_module_on(reduced_labels)
    relation_labels = finite_ordered_filter(
        reduced_labels,
        lambda reduced_position: invariants[int(retained_positions.unrank(int(reduced_position)))] != ring.zero(),
    )
    reduced_source = free_owner._fresh_free_module_on(relation_labels)
    reduced_presentation = module_homset(reduced_source, reduced_target)(
        {
            reduced_position: reduced_target.scalar_multiple(
                invariants[int(retained_positions.unrank(int(reduced_position)))],
                reduced_target.module_generator(reduced_position),
            )
            for reduced_position in relation_labels
        }
    )
    reduced = FinitelyPresentedModule(reduced_presentation)

    full_labels = full_normalized.module_generating_set()
    full_to_reduced = module_homset(full_normalized, reduced)(
        {
            full_label: (reduced.module_generator(retained_positions.rank(retained_positions(position))) if position in retained_positions else reduced.zero())
            for position, full_label in enumerate(full_labels)
        }
    )
    reduced_to_full = module_homset(reduced, full_normalized)(
        {
            reduced_label: full_normalized.module_generator(full_labels.unrank(int(retained_positions.unrank(int(reduced_label)))))
            for reduced_label in reduced.module_generating_set()
        }
    )
    reduced_iso = Isomorphism(full_to_reduced, reduced_to_full)

    target_forward = presentation_iso.forward().right()
    target_inverse = presentation_iso.inverse().right()
    full_projection = full_normalized.presentation_projection()
    original_projection = module.presentation_projection()
    original_to_full = module_homset(module, full_normalized)(
        {label: full_projection(target_forward(module.presentation().codomain().module_generator(label))) for label in module.module_generating_set()}
    )
    full_to_original = module_homset(full_normalized, module)(
        {label: original_projection(target_inverse(diagonal_presentation.codomain().module_generator(label))) for label in full_normalized.module_generating_set()}
    )
    presentation_cokernel_iso = Isomorphism(
        original_to_full,
        full_to_original,
    )
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
        equal = isinstance(other, _GeneralPresentedElement) and other.parent() is self.parent() and self.parent()._relation_contains(self._lift - other._lift)
        return equal if op == op_EQ else not equal

    def __hash__(self):
        parent = self.parent()
        smith_engine = parent._smith_engine()
        if smith_engine is None:
            raise TypeError("hashing a presented-module class requires a represented canonical quotient key")
        key = tuple(parent._to_smith_engine_element(self).vector())
        return hash((id(parent), key))

    def additive_order(self):
        r"""Return the additive order when the selected Smith model is finite."""
        parent = self.parent()
        engine = parent._smith_engine()
        if engine is None or not parent.is_torsion():
            raise NotImplementedError("additive order requires a represented finite torsion presentation")
        order = parent._to_smith_engine_element(self).additive_order()
        return parent.base_ring()._from_engine_element(SageZZ(order))

    def _repr_(self):
        return repr(self._lift)


class _GeneralPresentedModule:
    r"""A presented module over a ring with no Smith engine.

    ``free_module`` is the cover and ``relation_submodule`` the relation
    module inside it: Sage objects over the engine ring when the base ring
    has a Sage engine, else the owned free cover and ``None``.  Both are
    private; the category states the mathematics.
    """

    def __eq__(self, other):
        r"""Compare the underlying represented modules, not extra equipment.

        Two ideals are equal when they are the same submodule of the ring,
        whatever presentations were selected for them; that is the ideal
        category's equality, routed to here because an ideal is placed in
        both categories and equality is decided in one place.
        """
        from dzack_research.preamble.categories.rings.commutative_ideals import CommutativeIdeals

        ideals = CommutativeIdeals(self.base_ring())
        if self in ideals and other in ideals:
            return self._engine_ideal() == other._engine_ideal()
        return self._same_selected_presentation_as(other)

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((self.base_ring(), self.presentation()))

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
            module_generator_function=lambda label: self._cover_generator(int(module_generating_set.rank(label))),
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
            return self(self._free_module.module_generator(labels.unrank(position)))
        return self(self._free_module.gen(position))

    def _cover_coordinates(self, element):
        r"""Coordinates of a representative as an indexed family on the cover basis."""
        lift = self(element)._representative()
        labels = self.module_generating_set()

        if self._relation_submodule is None:
            coefficients = module_coefficients(lift, self._free_module)
            zero = self.base_ring().zero()
            return indexed_family(
                labels,
                lambda label: coefficients.get(label, zero),
                name=f"Cover coordinates of {element}",
            )
        native = self._free_module.coordinate_vector(lift)
        ring = self.base_ring()
        return indexed_family(
            labels,
            lambda label: ring._from_engine_element(native[int(labels.rank(label))]),
            name=f"Cover coordinates of {element}",
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
        rank = int(self._free_module.rank())
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

    def _relation_contains(self, vector) -> bool:
        if vector == self._free_module.zero():
            return True
        if self._relation_submodule is None:
            raise NotImplementedError(f"equality in a presented module over {self.base_ring()} has no computation engine that decides membership in the relation module")
        lifted_backend = self._lifted_relation_backend()
        if lifted_backend is None:
            return vector in self._relation_submodule

        lifted_free, lifted_submodule = lifted_backend
        base_ring = self.base_ring()
        presentation_ring = base_ring._exact_coefficient_presentation_ring()

        def lift_backend_coefficient(coefficient):
            owned_coefficient = base_ring._from_engine_element(coefficient)
            lifted_owned = base_ring._lift_coefficient_to_presentation(owned_coefficient)
            return _engine_element(presentation_ring, lifted_owned)

        lifted = lifted_free(tuple(lift_backend_coefficient(coefficient) for coefficient in tuple(vector)))
        native_contains = lifted in lifted_submodule
        presentation_engine = _engine_ring(presentation_ring)
        flattening = getattr(presentation_engine, "flattening_morphism", None)
        if flattening is None:
            return native_contains
        try:
            flatten = flattening()
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return native_contains
        flattened_ring = flatten.codomain()
        if flattened_ring is presentation_engine:
            return native_contains

        # Sage's generic submodule membership over a nested polynomial ring can
        # return False even for one of the displayed generators.  Flattening
        # P = R[t][x_1,...,x_n] to the canonically isomorphic polynomial ring
        # R[t,x_1,...,x_n] routes the same module-membership question to the
        # Singular-backed multivariate implementation.
        from sage.modules.free_module import FreeModule as SageFreeModule

        flattened_free = SageFreeModule(flattened_ring, int(lifted_free.rank()))
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

    def __call__(self, value):
        r"""Construct a quotient element without Sage coercion discovery."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        if isinstance(value, _GeneralPresentedElement):
            if value.parent() is self:
                return value
            value = value._representative()
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
        self._preamble_pid_engine = engine
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

    def _to_smith_engine_element(self, element):
        r"""Cross an owned quotient element into the private FGP workspace."""
        owned = self(element)
        coordinates = self._cover_coordinates(owned)
        backend = self._preamble_pid_engine
        labels = self.module_generating_set()
        return backend(backend.V()(tuple(_engine_element(self.base_ring(), coordinates[label]) for label in labels)))

    def _from_smith_engine_element(self, element):
        r"""Cross one private FGP element back to an owned quotient element."""
        backend = self._preamble_pid_engine
        lift = backend(element).lift()
        ring = self.base_ring()
        coordinates = tuple(ring._from_engine_element(coefficient) for coefficient in tuple(lift))
        return self._from_coordinates(coordinates)


class _PresentedModuleObjects(OwnedCategoryOverBaseRing):
    r"""The private quotient realization of a selected presentation."""

    @classmethod
    def _repr_object_names(cls):
        return "represented quotient modules with selected finite presentation"

    def super_categories(self):
        return [_SelectedFinitePresentationModules(self.base_ring())]

    ElementMethods = _GeneralPresentedElement

    class ParentMethods(_PresentedModule):
        pass


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
    subobject_verify_linearity=True,
    biproduct_factors=None,
    extra_categories=(),
    extra_construction_data=None,
):
    r"""Build a represented quotient through the category constructor chain."""
    categories = [_PresentedModuleObjects(base_ring)]
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
        data.update(
            subobject_ambient=subobject_ambient,
            subobject_generator_images=subobject_generator_images,
            subobject_lift=subobject_lift,
            subobject_inclusion_factory=subobject_inclusion_factory,
            subobject_verify_linearity=subobject_verify_linearity,
        )
    if biproduct_factors is not None:
        categories.append(BiproductModules(base_ring))
        data["biproduct_factors"] = biproduct_factors
    categories.extend(extra_categories)
    if extra_construction_data is not None:
        data.update(extra_construction_data)
    return object_of(Category.join(tuple(categories)), **data)


def _presentation_matrix(module):
    r"""Materialize the selected finite relation family as one matrix Hom element.

    The chosen-presentation category owns only the mathematical datum.  A
    concrete presented-module backend may already store its matrix; otherwise
    (notably for a finite free module) the matrix is synthesized from the
    selected relation rows only at this finite coordinate boundary.
    """
    ring = module.base_ring()
    if module not in ModulesWithChosenFinitePresentation(ring):
        raise TypeError("a presentation matrix requires selected finite presentation data")

    if module in _SelectedFinitePresentationModules(ring):
        return module.presentation_matrix()

    rows = module._selected_presentation_rows()
    if rows is None:
        raise TypeError("the selected finite presentation has no represented relation rows")
    rows = tuple(tuple(row) for row in rows)
    return _matrix_space_like(
        module,
        len(rows),
        int(module.module_generating_set().cardinality()),
    ).from_rows(rows)


def _matrix_coordinate_rows(matrix):
    r"""Return finite coordinate rows of one matrix Hom element."""
    parent = matrix.parent()
    return tuple(tuple(matrix.matrix_entry(row_label, column_label) for column_label in parent.column_index_set()) for row_label in parent.row_index_set())


def _presentation_rows(module):
    r"""Return the selected finite relation rows without forcing matrix realization."""
    if module not in ModulesWithChosenFinitePresentation(module.base_ring()):
        raise TypeError("relation rows require selected finite presentation data")
    rows = module._selected_presentation_rows()
    if rows is None:
        raise TypeError("the selected finite presentation has no represented relation rows")
    return tuple(tuple(row) for row in rows)


def _relation_element(module, row):
    return sum(
        (module.scalar_multiple(coefficient, module.module_generator(label)) for label, coefficient in zip(module.module_generating_set(), row, strict=True) if coefficient),
        module.zero(),
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
        raise ValueError("a kernel presentation requires one coefficient ring")
    if ring not in PrincipalIdealDomains():
        raise TypeError("the PID presented-kernel backend requires a principal ideal domain")

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
            coefficients = module_coefficients(
                morphism(domain.module_generator(source_label)),
                codomain,
            )
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
        kernel_pairs = augmented.right_kernel().basis_matrix().rows()
        projected = [free_cover(tuple(row[position] for position in range(source_rank))) for row in kernel_pairs if any(row[position] != 0 for position in range(source_rank))]
        preimage = free_cover.submodule(projected) if projected else free_cover.zero_submodule()

    basis_rows = tuple(tuple(row) for row in preimage.basis_matrix().rows())
    kernel_count = len(basis_rows)
    kernel_labels = Sets.Δ[kernel_count - 1]

    relation_coordinate_rows = []
    for row in source_relations.rows():
        source_relation = free_cover(tuple(row))
        try:
            coordinates = preimage.coordinate_vector(source_relation)
        except (ArithmeticError, ValueError) as error:
            raise ArithmeticError("a represented module morphism did not carry a source relation into the target relations") from error
        relation_coordinate_rows.append(tuple(ring._from_engine_element(engine(coefficient)) for coefficient in coordinates))

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
                source_label: ring._from_engine_element(engine(coefficient))
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
        coefficients = module_coefficients(element, domain)
        representative = free_cover(
            tuple(
                _engine_element(
                    ring,
                    coefficients.get(label, ring.zero()),
                )
                for label in source_labels
            )
        )
        try:
            coordinates = preimage.coordinate_vector(representative)
        except (ArithmeticError, ValueError) as error:
            raise ValueError("the element does not lie in the represented kernel") from error
        return kernel.linear_combination({label: ring._from_engine_element(engine(coordinates[int(label)])) for label in kernel_labels if coordinates[int(label)] != 0})

    return FinitelyPresentedModule(
        presentation,
        _subobject_ambient=domain,
        _subobject_generator_images=generator_images,
        _subobject_lift=lift_from_domain,
    )


def _singular_presentation_kernel(morphism):
    r"""Return ``ker(morphism)`` for polynomial-presentation coefficient rings.

    Let ``A=P/I`` with ``P`` a polynomial ring over a field, and let

    ``f : A^n/D -> A^m/Q``.

    Lifting to ``P``, a vector ``x`` represents a kernel element exactly when

    ``F x - Q^t y - I z = 0``

    for some ``y,z``.  Singular syzygies of that augmented matrix therefore
    generate the kernel lifts.  A second syzygy computation against the source
    relations ``D`` gives an exact finite presentation of the kernel itself.

    This is a private computation crossing.  The returned object is the owned
    finitely presented module equipped with its actual inclusion into the
    domain; no Singular module escapes into the public API.
    """
    from sage.libs.singular.function_factory import ff
    from sage.matrix.constructor import matrix
    from sage.matrix.special import identity_matrix
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    domain = morphism.domain()
    codomain = morphism.codomain()
    ring = _owned_ring(domain.base_ring())
    if _owned_ring(codomain.base_ring()) is not ring:
        raise ValueError("a kernel presentation requires one coefficient ring")

    coefficient_presentation = ring._exact_coefficient_presentation_ring()
    presentation_ring = _engine_ring(coefficient_presentation)
    coefficient_relations = ring._exact_coefficient_presentation_relations()

    def backend_coefficient_relation(relation):
        return _engine_element(coefficient_presentation, relation)

    def lift_scalar(value):
        lifted = ring._lift_coefficient_to_presentation(value)
        return _engine_element(coefficient_presentation, lifted)

    def descend_scalar(value):
        lifted = coefficient_presentation._from_engine_element(presentation_ring(value))
        return ring._descend_coefficient_from_presentation(lifted)

    try:
        coefficient_field = presentation_ring.base_ring()
        field_coefficients = bool(coefficient_field.is_field())
    except AttributeError, NotImplementedError:
        field_coefficients = False
    if not field_coefficients:
        raise NotImplementedError("the general presented-kernel backend currently uses Singular over a polynomial ring over a field")

    # Singular's syz entry point requires a multivariate polynomial parent,
    # even in one variable.  Cross only this backend representation.
    if presentation_ring.ngens() == 1 and "multi_polynomial" not in type(presentation_ring).__module__:
        singular_ring = PolynomialRing(
            coefficient_field,
            1,
            presentation_ring.variable_names(),
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

    def singular_syzygies(columns_matrix):
        total_columns = columns_matrix.ncols()
        if total_columns == 0:
            return matrix(singular_ring, 0, 0, [])
        result = ff.syz(columns_matrix)
        rows = [tuple(row) for row in result]
        return matrix(
            singular_ring,
            len(rows),
            total_columns,
            [entry for row in rows for entry in row],
        )

    if m == 0:
        kernel_lifts = [tuple(singular_ring.one() if i == j else singular_ring.zero() for i in range(n)) for j in range(n)]
    else:
        coordinate_columns = []
        for source_label in source_labels:
            image = morphism(domain.module_generator(source_label))
            coefficients = module_coefficients(image, codomain)
            coordinate_columns.append(tuple(to_singular(lift_scalar(coefficients.get(label, ring.zero()))) for label in target_labels))
        f_matrix = matrix(
            singular_ring,
            m,
            n,
            [coordinate_columns[column][row] for row in range(m) for column in range(n)],
        )
        augmented = f_matrix
        if target_relations.nrows():
            lifted_target_relations = matrix(
                singular_ring,
                target_relations.nrows(),
                m,
                [to_singular(lift_scalar(entry)) for row in _matrix_coordinate_rows(target_relations) for entry in row],
            )
            augmented = augmented.augment(-lifted_target_relations.transpose())
        for relation in coefficient_relations:
            augmented = augmented.augment(-to_singular(backend_coefficient_relation(relation)) * identity_matrix(singular_ring, m))
        first_syzygies = singular_syzygies(augmented)
        kernel_lifts = [tuple(row[position] for position in range(n)) for row in first_syzygies.rows()]

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

    relation_augmented = kernel_columns
    if source_relations.nrows():
        lifted_source_relations = matrix(
            singular_ring,
            source_relations.nrows(),
            n,
            [to_singular(lift_scalar(entry)) for row in _matrix_coordinate_rows(source_relations) for entry in row],
        )
        relation_augmented = relation_augmented.augment(-lifted_source_relations.transpose())
    for relation in coefficient_relations:
        relation_augmented = relation_augmented.augment(-to_singular(backend_coefficient_relation(relation)) * identity_matrix(singular_ring, n))

    if n == 0:
        kernel_relation_rows = []
    else:
        second_syzygies = singular_syzygies(relation_augmented)
        kernel_relation_rows = [
            tuple(from_singular(row[position]) for position in range(kernel_count))
            for row in second_syzygies.rows()
            if any(row[position] != 0 for position in range(kernel_count))
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

    kernel_generator_matrix = matrix(
        singular_ring,
        kernel_count,
        n,
        [entry for row in kernel_lifts for entry in row],
    )
    lifted_source_relation_rows = matrix(
        singular_ring,
        source_relations.nrows(),
        n,
        [to_singular(lift_scalar(entry)) for row in source_relations.rows() for entry in row],
    )

    def lift_from_domain(kernel, element):
        if element.parent() is not domain:
            element = domain(element)
        if kernel_count == 0:
            if element == domain.zero():
                return kernel.zero()
            raise ValueError("the element does not lie in the represented kernel")
        coefficients = module_coefficients(element, domain)
        requested = matrix(
            singular_ring,
            1,
            n,
            [to_singular(lift_scalar(coefficients.get(label, ring.zero()))) for label in source_labels],
        )
        spanning = kernel_generator_matrix
        if source_relations.nrows():
            spanning = spanning.stack(lifted_source_relation_rows)
        for relation in coefficient_relations:
            spanning = spanning.stack(to_singular(backend_coefficient_relation(relation)) * identity_matrix(singular_ring, n))
        try:
            lifted = matrix(
                singular_ring,
                ff.lift(
                    spanning.transpose(),
                    requested.transpose(),
                ),
            )
        except RuntimeError as error:
            raise ValueError("the element does not lie in the represented kernel") from error
        return kernel.linear_combination({label: from_singular(lifted[position, 0]) for position, label in enumerate(kernel_labels) if lifted[position, 0] != 0})

    return FinitelyPresentedModule(
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
    target = free_owner._fresh_free_module_on(labels)
    source = free_owner._fresh_free_module_on(relation_labels)
    images = {label: _relation_element(target, row) for label, row in zip(source.module_generating_set(), _matrix_coordinate_rows(relations), strict=True)}
    return module_homset(source, target)(images)


def FinitelyPresentedModule(
    presentation,
    *,
    _cokernel_morphism=None,
    _extra_categories=(),
    _extra_construction_data=None,
    _subobject_ambient=None,
    _subobject_generator_images=None,
    _subobject_lift=None,
    _subobject_inclusion_factory=None,
    _subobject_verify_linearity=True,
    _biproduct_factors=None,
):
    r"""Return ``coker(presentation)`` in ``R-Mod`` with its selected module presentation."""
    # The cokernel here is taken in the module category.  A stricter structured
    # morphism (lattice/form/equivariant/etc.) must first be read as its
    # underlying R-linear arrow; otherwise later presentation constructions
    # incorrectly inherit the stricter Hom object.

    presentation = module_homset(presentation.domain(), presentation.codomain())(presentation)
    codomain = presentation.codomain()
    base_ring = codomain.base_ring()
    engine = _engine_ring(base_ring)

    labels = codomain.module_generating_set()
    existing = _presentation_matrix(codomain)

    added_rows = []
    for source_label in presentation.domain().module_generating_set():
        image = presentation(presentation.domain().module_generator(source_label))
        coefficients = module_coefficients(image, codomain)
        added_rows.append(tuple(coefficients.get(label, base_ring.zero()) for label in labels))
    from itertools import chain

    existing_rows = _matrix_coordinate_rows(existing)
    existing_count = len(existing_rows)
    width = int(labels.cardinality())
    relations_matrix = _matrix_space_like(
        codomain,
        existing_count + len(added_rows),
        width,
    ).from_rows(chain(existing_rows, added_rows))
    relations = relations_matrix
    if existing_count == 0:
        selected_presentation = presentation
    else:
        existing_labels = codomain.presentation().domain().module_generating_set() if codomain in _SelectedFinitePresentationModules(base_ring) else Sets.Δ[existing_count - 1]
        added_labels = presentation.domain().module_generating_set()
        relation_labels = CoproductOfFamily(
            Sets.Δ[1],
            lambda index: existing_labels if int(index) == 0 else added_labels,
        )
        selected_presentation = _presentation_from_relation_rows(
            base_ring,
            labels,
            relation_labels,
            relations,
        )

    from sage.categories.rings import Rings as SageRings

    pid_backend = False
    if engine in SageRings():
        from sage.modules.free_module import FreeModule as SageFreeModule

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
            subobject_verify_linearity=_subobject_verify_linearity,
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
            subobject_verify_linearity=_subobject_verify_linearity,
            biproduct_factors=_biproduct_factors,
            extra_categories=_extra_categories,
            extra_construction_data=_extra_construction_data,
        )
    else:
        # The base ring has no Sage computation ring behind it, so the
        # cover is the owned free module and the presentation is the only
        # datum; equality of elements is not decided here.
        quotient = _new_presented_module(
            free_module=_free_cover_owner(codomain)._fresh_free_module_on(labels),
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
            subobject_verify_linearity=_subobject_verify_linearity,
            biproduct_factors=_biproduct_factors,
            extra_categories=_extra_categories,
            extra_construction_data=_extra_construction_data,
        )

    return quotient


__all__ = [
    "FinitelyPresentedModule",
    "_presentation_matrix",
]
