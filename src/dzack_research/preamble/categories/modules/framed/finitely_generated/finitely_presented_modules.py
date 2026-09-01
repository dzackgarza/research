"""Finitely presented modules with a selected finite presentation."""

from sage.categories.principal_ideal_domains import PrincipalIdealDomains
from sage.categories.modules import Modules as SageModules
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
    owned_ring_view,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import refine
from dzack_research.preamble.tensors import tensor


class FinitelyPresentedModules(OwnedCategoryOverBaseRing):
    r"""Modules admitting a finite presentation."""

    @classmethod
    def _repr_object_names(cls):
        return "finitely presented modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.finitely_generated.finitely_generated_modules import (
            FinitelyGeneratedModules,
        )

        return [FinitelyGeneratedModules(self.base_ring())]

    class ParentMethods:
        def is_finitely_presented(self) -> bool:
            return True

        def cokernel_projection(self):
            r"""Return the canonical quotient map when this object is a selected cokernel."""
            projection = getattr(self, "_preamble_cokernel_projection", None)
            if projection is None:
                raise ValueError("this finitely presented module was not constructed as a cokernel")
            return projection

        def tensor_product(self, other):
            r"""Return the categorical tensor product over the common base ring."""
            from dzack_research.preamble.categories.abstract_categories import (
                TensorProduct,
            )

            return TensorProduct(self, other)

class ModulesWithChosenFinitePresentation(OwnedCategoryOverBaseRing):
    r"""Finitely presented modules carrying a selected relation morphism."""

    @classmethod
    def _repr_object_names(cls):
        return "modules with a chosen finite presentation"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.framed.framed_modules import (
            FramedModules,
        )

        return [
            FinitelyPresentedModules(self.base_ring()),
            FramedModules(self.base_ring()),
        ]

    class ParentMethods:
        def base_ring(self):
            return self._preamble_base_ring

        def presentation(self):
            r"""Return the selected relation morphism ``F_1 -> F_0``."""
            return self._preamble_presentation

        def presentation_matrix(self):
            r"""Return its relation rows in the selected target framing."""
            return self._preamble_relation_matrix

        def fitting_ideal(self, index):
            r"""Return ``Fitt_index(M)`` from the selected finite presentation."""
            from dzack_research.preamble.tensors.tensor import _engine_component_matrix

            index = int(index)
            if index < 0:
                raise ValueError("a Fitting-ideal index is nonnegative")
            ring = self.base_ring()
            n = int(self.number_of_module_generators())
            minor_size = n - index
            if minor_size <= 0:
                return ring.ideal(ring.one())
            matrix = _engine_component_matrix(self.presentation_matrix())
            if minor_size > min(matrix.nrows(), matrix.ncols()):
                return ring.ideal(ring.zero())
            minors = tuple(matrix.minors(minor_size))
            return ring.ideal(*(minors or (ring.zero(),)))

        def annihilator(self):
            r"""Return ``Ann_R(M)`` in exact currently represented regimes."""
            ring = self.base_ring()
            if isinstance(self, FGP_Module_class):
                invariants = tuple(self.invariants(include_ones=True))
                if not invariants or all(invariant.is_unit() for invariant in invariants):
                    return ring.ideal(ring.one())
                if any(invariant == 0 for invariant in invariants):
                    return ring.ideal(ring.zero())
                nonunits = tuple(
                    invariant for invariant in invariants if not invariant.is_unit()
                )
                return ring.ideal(nonunits[-1])

            if int(self.number_of_module_generators()) == 1:
                from dzack_research.preamble.tensors.tensor import _engine_component_matrix

                matrix = _engine_component_matrix(self.presentation_matrix())
                entries = tuple(matrix[row, 0] for row in range(matrix.nrows()))
                return ring.ideal(*(entries or (ring.zero(),)))

            raise NotImplementedError(
                "annihilator of this general finite presentation requires a commutative-algebra backend"
            )

        def support(self):
            r"""Return ``Supp(M)=V(Fitt_0(M))`` in ``Spec(R)``."""
            return self.base_ring().spectrum().V(self.fitting_ideal(0))

        def minimal_module_generators(self):
            r"""Return a minimal selected generating set over a local base ring.

            By Nakayama, a set of generators is minimal exactly when its image
            is a basis of ``M/mM``.  The selected presentation gives
            ``M/mM = k^n / row(relations mod m)``; non-pivot standard basis
            classes therefore give a basis of the quotient.
            """
            from sage.matrix.constructor import matrix

            from dzack_research.preamble.categories.rings import (
                LocalRings,
                engine_element,
                engine_ring,
            )
            from dzack_research.preamble.categories.sets import finite_ordered_set
            ring = self.base_ring()
            if ring not in LocalRings():
                raise TypeError(
                    "minimal generators via Nakayama require a represented local base ring"
                )
            relation_rows = tuple(self.presentation_matrix().rows())
            residue = ring.residue_field()
            residue_engine = engine_ring(residue)
            residue_map = ring.residue_map()
            specialized = matrix(
                residue_engine,
                len(relation_rows),
                int(self.number_of_module_generators()),
                [
                    engine_element(residue, residue_map(coefficient))
                    for row in relation_rows
                    for coefficient in row
                ],
            )
            pivot_columns = frozenset(specialized.echelon_form().pivots())
            labels = tuple(self.module_generating_set())
            return finite_ordered_set(
                self.module_generator(label)
                for position, label in enumerate(labels)
                if position not in pivot_columns
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
            try:
                position = labels.position(label)
            except AttributeError:
                position = labels.rank(label)
            if position is None:
                raise ValueError(f"{label!r} is not a module-generator label")
            return self(self.V().gen(position))

        def module_generators(self):
            r"""Return the selected generator images, indexed by the framing.

            This is deliberately a tuple rather than a set.  A quotient may
            send two distinct framing labels to the same element, or send a
            selected generator to zero.  Those occurrences remain distinct
            pieces of framing data even though their images are equal as
            module elements.
            """
            return tuple(
                self.module_generator(label) for label in self.module_generating_set()
            )

        def framing_morphism(self):
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
                BasedFreeModule,
            )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                framing_morphism,
            )

            source = BasedFreeModule(self.base_ring(), self.module_generating_set())
            return framing_morphism(source, self, self.module_generator)

        def _from_coordinates(self, coordinates):
            custom = self.__dict__.get("_preamble_module_from_coordinates_function")
            if custom is not None:
                return custom(coordinates)
            return self(self.V()(tuple(coordinates)))

        def coordinate_vector(self, element, reduce=False):
            r"""Return optimized quotient coordinates, reducing over the native ``ZZ`` engine.

            Sage's ``FGP_Module`` implementation only performs its canonical
            residue reduction when ``base_ring() is ZZ``.  The public base
            ring here is the owned facade of ``ZZ``, so delegating the
            ``reduce=True`` branch verbatim makes quotient equality forget its
            relations.  Compute the unreduced optimized coordinates with
            Sage, then perform exactly the same reduction against the native
            coefficient engine.
            """
            from sage.modules.fg_pid.fgp_module import FGP_Module_class
            from sage.rings.integer_ring import ZZ as SageZZ

            from dzack_research.preamble.tensors.tensor import _engine_vector

            # This implements Sage's FGP coordinate protocol, so every branch
            # returns the engine vector Sage's own code consumes.
            custom = self.__dict__.get("_preamble_module_coordinate_function")
            if custom is not None:
                return _engine_vector(
                    engine_ring(self.base_ring()),
                    tuple(custom(element)),
                )

            if not isinstance(self, FGP_Module_class):
                lift = element.lift() if hasattr(element, "lift") else element
                if getattr(lift, "parent", lambda: None)() is self.V():
                    return _engine_vector(
                        engine_ring(self.base_ring()),
                        tuple(lift),
                    )
                return self.V().coordinate_vector(lift)

            coordinates = FGP_Module_class.coordinate_vector(self, element, reduce=False)
            engine = engine_ring(self.base_ring())
            if not reduce or engine is not SageZZ:
                return coordinates
            invariants = self.invariants()
            return _engine_vector(
                engine,
                [
                    coordinates[index]
                    if invariant == 0
                    else coordinates[index] % invariant
                    for index, invariant in enumerate(invariants)
                ],
            )

        def rank(self):
            r"""Return the rank of the free summand."""
            engine = engine_ring(self.base_ring())
            if engine.is_field():
                from dzack_research.preamble.tensors.tensor import (
                    _engine_component_matrix,
                )

                relations = _engine_component_matrix(self.presentation_matrix())
                return self.number_of_module_generators() - relations.rank()
            if not isinstance(self, FGP_Module_class):
                raise NotImplementedError(
                    "free-summand rank is currently computed from PID invariant factors"
                )
            return sum(
                1
                for invariant in self.invariants(include_ones=True)
                if invariant == 0
            )

        def is_torsion(self):
            engine = engine_ring(self.base_ring())
            if engine.is_field():
                return self.is_zero()
            if not isinstance(self, FGP_Module_class):
                raise NotImplementedError(
                    "torsion detection is currently computed from PID invariant factors"
                )
            return self.rank() == 0

        def is_torsion_free(self):
            if engine_ring(self.base_ring()).is_field():
                return True
            if not isinstance(self, FGP_Module_class):
                raise NotImplementedError(
                    "torsion-freeness is currently computed from PID invariant factors"
                )
            return all(
                invariant == 0 or invariant.is_unit()
                for invariant in self.invariants(include_ones=True)
            )

        def is_zero(self):
            if engine_ring(self.base_ring()).is_field():
                return self.rank() == 0
            if not isinstance(self, FGP_Module_class):
                raise NotImplementedError(
                    "zero detection is currently computed from PID invariant factors"
                )
            return all(
                invariant.is_unit()
                for invariant in self.invariants(include_ones=True)
            )

        def dimension(self):
            r"""Return vector-space dimension when the base ring is a field."""
            if not engine_ring(self.base_ring()).is_field():
                raise TypeError("dimension is defined here for modules over a field")
            return self.rank()

        def invariant_factors(self):
            return tuple(
                invariant
                for invariant in self.invariants(include_ones=True)
                if not invariant.is_unit()
            )

        def smith_form_module_generators(self):
            r"""Return the invariant-factor generators, realized inside ``self``.

            These are *not* the selected framing of ``self``.  If ``R`` is the
            selected relation matrix and ``D = U R V`` is a Smith form, the
            rows of ``V^-1`` give the generators of the Smith-normalized framed
            module expressed as elements of this quotient.  Unit invariant
            factors are omitted, so this set can be strictly smaller than the
            selected framing retained by a literal cokernel.

            Use :meth:`invariant_factor_form` when the normalized framed object
            and the explicit isomorphism to it are wanted.
            """
            if not isinstance(self, FGP_Module_class):
                raise NotImplementedError(
                    "Smith generators require a PID presentation backend"
                )
            _smith, _left, engine_right = self._smith_form()
            right = tensor.matrix(engine_ring(self.base_ring()), engine_right)
            inverse_right = right.inverse_tensor()
            basis = tensor.matrix(
                engine_ring(self.base_ring()),
                self.V().basis_matrix(),
            )
            lifted_rows = inverse_right * basis
            invariants = tuple(self.invariants(include_ones=True))
            return finite_ordered_set(
                self(lifted_rows.row(position))
                for position, invariant in enumerate(invariants)
                if not invariant.is_unit()
            )

        def invariant_factor_form(self):
            r"""Return ``self -> M_if`` as an explicit framed-module isomorphism.

            ``self`` keeps its selected presentation exactly.  In particular,
            a cokernel keeps the framing inherited from the codomain even when
            some of those generators become zero or redundant.  ``M_if`` is a
            *different* framed module: its selected generators are the
            non-unit Smith factors only, so zero summands disappear.

            If ``D = U R V`` is the Smith decomposition of the selected
            relation matrix, right multiplication by ``V`` carries the
            original presentation to Smith coordinates.  After deleting the
            unit factors this still induces an isomorphism because those
            coordinates are already zero in the quotient.  The inverse uses
            the corresponding rows of ``V^-1`` and therefore records an actual
            chosen lift of every normalized generator back to ``self``.

            The Smith decomposition is algorithmic and choice-bearing; this
            method therefore returns the isomorphism, rather than silently
            replacing ``self`` by an isomorphic normal form.
            """
            if not isinstance(self, FGP_Module_class):
                raise NotImplementedError(
                    "invariant-factor form requires a PID presentation backend"
                )

            from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
                Isomorphism,
            )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )

            engine = engine_ring(self.base_ring())
            _smith, _left, engine_right = self._smith_form()
            right = tensor.matrix(engine, engine_right)
            inverse_right = right.inverse_tensor().change_ring(engine)
            invariants = tuple(self.invariants(include_ones=True))
            retained_positions = tuple(
                position
                for position, invariant in enumerate(invariants)
                if not invariant.is_unit()
            )

            normalized_labels = finite_ordered_set(range(len(retained_positions)))
            relation_rows = []
            relation_labels = []
            for normalized_position, smith_position in enumerate(retained_positions):
                invariant = engine(invariants[smith_position])
                if invariant == 0:
                    continue
                row = [engine.zero()] * len(retained_positions)
                row[normalized_position] = invariant
                relation_rows.append(row)
                relation_labels.append(normalized_position)
            relations = tensor.matrix(
                engine,
                len(relation_rows),
                len(retained_positions),
                [entry for row in relation_rows for entry in row],
            )
            normalized_presentation = _presentation_from_relation_rows(
                self.base_ring(),
                normalized_labels,
                finite_ordered_set(relation_labels),
                relations,
            )
            normalized = FinitelyPresentedModule(normalized_presentation)

            normalized_generators = tuple(normalized.module_generators())
            forward_images = {}
            for source_position, source_label in enumerate(self.module_generating_set()):
                forward_images[source_label] = sum(
                    (
                        engine(right[source_position, smith_position])
                        * normalized_generators[normalized_position]
                        for normalized_position, smith_position in enumerate(retained_positions)
                        if right[source_position, smith_position]
                    ),
                    normalized.zero(),
                )
            forward = module_homset(self, normalized)(forward_images)

            original_generators = tuple(self.module_generators())
            inverse_images = {}
            for normalized_position, normalized_label in enumerate(normalized.module_generating_set()):
                smith_position = retained_positions[normalized_position]
                inverse_images[normalized_label] = sum(
                    (
                        engine(inverse_right[smith_position, original_position])
                        * original_generator
                        for original_position, original_generator in enumerate(original_generators)
                        if inverse_right[smith_position, original_position]
                    ),
                    self.zero(),
                )
            inverse = module_homset(normalized, self)(inverse_images)
            return Isomorphism(forward, inverse)

        def presentation_projection(self):
            r"""Return the selected quotient map ``F_0 -> M``."""
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )

            source = self.presentation().codomain()
            return module_homset(source, self)(
                {
                    label: self.module_generator(label)
                    for label in source.module_generating_set()
                }
            )

        def torsion_free_quotient_projection(self):
            r"""Return ``M -> M/Tor(M)`` in Smith coordinates."""
            if not isinstance(self, FGP_Module_class):
                raise NotImplementedError(
                    "torsion-free quotient is currently computed from PID invariant factors"
                )
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
                BasedFreeModule,
            )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )
            from dzack_research.preamble.categories.sets import finite_ordered_set

            invariants = tuple(self.invariants(include_ones=True))
            free_positions = finite_ordered_set(
                position
                for position, invariant in enumerate(invariants)
                if invariant == 0
            )
            target = BasedFreeModule(self.base_ring(), free_positions)
            _smith, _left, engine_right = self._smith_form()
            right = tensor.matrix(engine_ring(self.base_ring()), engine_right)
            images = {}
            for source_position, label in enumerate(self.module_generating_set()):
                images[label] = target.linear_combination(
                    {
                        position: right[source_position, position]
                        for position in free_positions
                        if right[source_position, position]
                    }
                )
            return module_homset(self, target)(images)

        def torsion_free_quotient(self):
            r"""Return ``M/Tor(M)``."""
            return self.torsion_free_quotient_projection().codomain()

        def exponent(self):
            r"""Return the exponent of a finite torsion ``ZZ``-module."""
            if not isinstance(self, FGP_Module_class):
                raise TypeError(
                    "the exponent is implemented on the PID presentation backend"
                )
            from sage.rings.integer_ring import ZZ as SageZZ

            if engine_ring(self.base_ring()) is not SageZZ:
                raise TypeError("the exponent here is the exponent of an abelian group")
            if not self.is_torsion():
                return SageZZ.zero()
            factors = tuple(abs(x) for x in self.invariants() if abs(x) > 1)
            return factors[-1] if factors else SageZZ.one()

        def _repr_(self):
            if not isinstance(self, FGP_Module_class):
                return (
                    f"Finitely presented module on "
                    f"{self.number_of_module_generators()} module generators over "
                    f"{self.base_ring()}"
                )
            return (
                f"Finitely presented module on "
                f"{self.number_of_module_generators()} module generators over "
                f"{self.base_ring()} with invariants {self.invariants()}"
            )

        def base_change(self, ring_map):
            r"""Transport the selected finite presentation along ``R -> S``."""
            from dzack_research.preamble.categories.modules.base_change import (
                base_change_codomain,
                base_change_scalar,
            )
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
                BasedFreeModule,
            )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )

            target_ring = base_change_codomain(self, ring_map)
            target = BasedFreeModule(target_ring, self.module_generating_set())
            relation_labels = self.presentation().domain().module_generating_set()
            source = BasedFreeModule(target_ring, relation_labels)
            images = {
                relation_label: sum(
                    (
                        target.scalar_multiple(
                            base_change_scalar(ring_map, coefficient),
                            target.module_generator(module_label),
                        )
                        for module_label, coefficient in zip(
                            target.module_generating_set(), row, strict=True
                        )
                        if coefficient
                    ),
                    target.zero(),
                )
                for relation_label, row in zip(
                    relation_labels,
                    self.presentation_matrix().rows(),
                    strict=True,
                )
            }
            return FinitelyPresentedModule(module_homset(source, target)(images))


class _GeneralPresentedElement(ModuleElement):
    r"""An element of a finitely presented module over a general ring.

    The representative lies in the selected free cover.  Equality is exact:
    two representatives define the same quotient element exactly when their
    difference lies in the selected relation submodule.
    """

    def __init__(self, parent, lift) -> None:
        ModuleElement.__init__(self, parent)
        self._lift = parent.V()(lift)

    def lift(self):
        return self._lift

    def _add_(self, other):
        return self.parent().element_class(self.parent(), self._lift + other._lift)

    def _neg_(self):
        return self.parent().element_class(self.parent(), -self._lift)

    def _lmul_(self, scalar):
        return self.parent().element_class(self.parent(), scalar * self._lift)

    _rmul_ = _lmul_

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = (
            isinstance(other, _GeneralPresentedElement)
            and other.parent() is self.parent()
            and self.parent()._relation_contains(self._lift - other._lift)
        )
        return equal if op == op_EQ else not equal

    def _repr_(self):
        return repr(self._lift)


class _GeneralPresentedModule(Parent):
    Element = _GeneralPresentedElement

    def __init__(
        self,
        free_module,
        relation_submodule,
        *,
        base_ring,
        module_generating_set,
        relation_matrix,
        presentation,
    ) -> None:
        self._free_module = free_module
        self._relation_submodule = relation_submodule
        self._preamble_base_ring = base_ring
        self._preamble_module_generating_set = module_generating_set
        self._preamble_relation_matrix = relation_matrix
        self._preamble_presentation = presentation
        self._lifted_relation_free_module = None
        self._lifted_relation_submodule = None
        Parent.__init__(
            self,
            base=base_ring,
            category=SageModules(engine_ring(base_ring)),
        )

    def V(self):
        return self._free_module

    def W(self):
        return self._relation_submodule

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
        try:
            coefficient_base = base_ring.base_ring()
        except AttributeError:
            return None
        if coefficient_base is None:
            return None

        from dzack_research.preamble.categories.algebras import (
            AlgebrasWithChosenFinitePresentation,
        )

        if base_ring not in AlgebrasWithChosenFinitePresentation(coefficient_base):
            return None

        from sage.modules.free_module import FreeModule as SageFreeModule

        presentation_ring = base_ring.presentation_ring()
        presentation_engine = engine_ring(presentation_ring)
        rank = int(self.V().rank())
        lifted_free = SageFreeModule(presentation_engine, rank)

        def lift_scalar(value):
            return presentation_engine(
                base_ring.lift_to_presentation(engine_ring(base_ring)(value))
            )

        rows = [
            lifted_free(tuple(lift_scalar(coefficient) for coefficient in row))
            for row in self.presentation_matrix().rows()
        ]
        for algebra_relation in base_ring.relations():
            relation = presentation_engine(algebra_relation)
            for position in range(rank):
                coordinates = [presentation_engine.zero()] * rank
                coordinates[position] = relation
                rows.append(lifted_free(coordinates))

        lifted_submodule = (
            lifted_free.submodule(rows)
            if rows
            else lifted_free.zero_submodule()
        )
        self._lifted_relation_free_module = lifted_free
        self._lifted_relation_submodule = lifted_submodule
        return lifted_free, lifted_submodule

    def _relation_contains(self, vector) -> bool:
        lifted_backend = self._lifted_relation_backend()
        if lifted_backend is None:
            return vector in self.W()

        lifted_free, lifted_submodule = lifted_backend
        base_ring = self.base_ring()
        presentation_engine = engine_ring(base_ring.presentation_ring())
        lifted = lifted_free(
            tuple(
                presentation_engine(
                    base_ring.lift_to_presentation(engine_ring(base_ring)(coefficient))
                )
                for coefficient in tuple(vector)
            )
        )
        return lifted in lifted_submodule

    def _element_constructor_(self, value):
        if isinstance(value, _GeneralPresentedElement):
            if value.parent() is self:
                return value
            value = value.lift()
        return self.element_class(self, value)

    def zero(self):
        return self.element_class(self, self.V().zero())

    def an_element(self):
        if self.V().rank() == 0:
            return self.zero()
        return self(self.V().gen(0))


class _PresentedModule(FGP_Module_class):
    r"""Native Sage quotient arithmetic carrying one selected presentation."""

    _preamble_base_ring = None
    _preamble_module_generating_set = None
    _preamble_relation_matrix = None
    _preamble_presentation = None

    def __init__(
        self,
        free_module,
        relation_submodule,
        *,
        base_ring,
        module_generating_set,
        relation_matrix,
        presentation,
    ) -> None:
        FGP_Module_class.__init__(self, free_module, relation_submodule)
        self._preamble_base_ring = base_ring
        self._preamble_module_generating_set = module_generating_set
        self._preamble_relation_matrix = relation_matrix
        self._preamble_presentation = presentation

    def _relative_matrix(self):
        r"""Return the backend relation matrix over Sage's computation ring.

        The public ``base_ring()`` is the owned ring parent.  Sage's FGP Smith
        algorithms, however, must remain over the native PID: internally they
        invoke the ring's ideal implementation while diagonalizing.  Crossing
        back to the engine here keeps that backend protocol from being routed
        through the preamble's mathematical ideal objects.
        """
        return self._V.coordinate_module(self._W).basis_matrix().change_ring(
            engine_ring(self._preamble_base_ring)
        )


def _presentation_matrix(module):
    r"""Return relation rows in ``module``'s selected module-generating set."""
    if module in ModulesWithChosenFinitePresentation(module.base_ring()):
        return module.presentation_matrix()

    try:
        if module.is_finitely_presented() and hasattr(module, "presentation_matrix"):
            return module.presentation_matrix()
    except (AttributeError, NotImplementedError):
        pass

    from dzack_research.preamble.categories.modules.restricted_scalars import (
        RestrictedScalarsModules,
    )

    if module in RestrictedScalarsModules(module.base_ring()):
        try:
            return module.presentation_matrix()
        except NotImplementedError:
            pass

    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        FinitelyGeneratedFreeModules,
    )

    if module not in FinitelyGeneratedFreeModules(module.base_ring()):
        raise TypeError(
            "a finite presentation requires a finitely presented or finite free target module"
        )
    return tensor.matrix(
        engine_ring(module.base_ring()),
        0,
        int(module.module_generating_set().cardinality()),
    )


def _relation_element(module, row):
    return sum(
        (
            coefficient * module.module_generator(label)
            for label, coefficient in zip(
                module.module_generating_set(), row, strict=True
            )
            if coefficient
        ),
        module.zero(),
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

    from dzack_research.preamble.categories.algebras import (
        AlgebrasWithChosenFinitePresentation,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_coefficients,
        module_embedding,
    )
    from dzack_research.preamble.categories.modules.subobjects import ModuleSubobjects

    domain = morphism.domain()
    codomain = morphism.codomain()
    ring = owned_ring_view(domain.base_ring())
    if owned_ring_view(codomain.base_ring()) is not ring:
        raise ValueError("a kernel presentation requires one coefficient ring")

    engine = engine_ring(ring)
    coefficient_base = ring.base_ring()
    if ring in AlgebrasWithChosenFinitePresentation(coefficient_base):
        presentation_ring = engine_ring(ring.presentation_ring())
        algebra_relations = tuple(presentation_ring(relation) for relation in ring.relations())

        def lift_scalar(value):
            return presentation_ring(
                ring.lift_to_presentation(engine(value))
            )

        def descend_scalar(value):
            return engine(presentation_ring(value))

    else:
        presentation_ring = engine
        algebra_relations = ()

        def lift_scalar(value):
            return presentation_ring(value)

        def descend_scalar(value):
            return engine(value)

    try:
        coefficient_field = presentation_ring.base_ring()
        field_coefficients = bool(coefficient_field.is_field())
    except (AttributeError, NotImplementedError):
        field_coefficients = False
    if not field_coefficients:
        raise NotImplementedError(
            "the general presented-kernel backend currently uses Singular over a polynomial ring over a field"
        )

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
        kernel_lifts = [
            tuple(
                singular_ring.one() if i == j else singular_ring.zero()
                for i in range(n)
            )
            for j in range(n)
        ]
    else:
        coordinate_columns = []
        for source_label in source_labels:
            image = morphism(domain.module_generator(source_label))
            coefficients = module_coefficients(image, codomain)
            coordinate_columns.append(
                tuple(
                    to_singular(lift_scalar(coefficients.get(label, engine.zero())))
                    for label in target_labels
                )
            )
        f_matrix = matrix(
            singular_ring,
            m,
            n,
            [
                coordinate_columns[column][row]
                for row in range(m)
                for column in range(n)
            ],
        )
        augmented = f_matrix
        if target_relations.nrows():
            lifted_target_relations = matrix(
                singular_ring,
                target_relations.nrows(),
                m,
                [
                    to_singular(lift_scalar(entry))
                    for row in target_relations.rows()
                    for entry in row
                ],
            )
            augmented = augmented.augment(-lifted_target_relations.transpose())
        for relation in algebra_relations:
            augmented = augmented.augment(
                -to_singular(relation) * identity_matrix(singular_ring, m)
            )
        first_syzygies = singular_syzygies(augmented)
        kernel_lifts = [
            tuple(row[position] for position in range(n))
            for row in first_syzygies.rows()
        ]

    kernel_count = len(kernel_lifts)
    kernel_labels = finite_ordered_set(range(kernel_count))
    if kernel_count:
        kernel_columns = matrix(
            singular_ring,
            n,
            kernel_count,
            [
                kernel_lifts[column][row]
                for row in range(n)
                for column in range(kernel_count)
            ],
        )
    else:
        kernel_columns = matrix(singular_ring, n, 0, [])

    relation_augmented = kernel_columns
    if source_relations.nrows():
        lifted_source_relations = matrix(
            singular_ring,
            source_relations.nrows(),
            n,
            [
                to_singular(lift_scalar(entry))
                for row in source_relations.rows()
                for entry in row
            ],
        )
        relation_augmented = relation_augmented.augment(
            -lifted_source_relations.transpose()
        )
    for relation in algebra_relations:
        relation_augmented = relation_augmented.augment(
            -to_singular(relation) * identity_matrix(singular_ring, n)
        )

    if n == 0:
        kernel_relation_rows = []
    else:
        second_syzygies = singular_syzygies(relation_augmented)
        kernel_relation_rows = [
            tuple(from_singular(row[position]) for position in range(kernel_count))
            for row in second_syzygies.rows()
            if any(row[position] != 0 for position in range(kernel_count))
        ]
    relation_labels = finite_ordered_set(range(len(kernel_relation_rows)))
    relation_matrix = matrix(
        engine,
        len(kernel_relation_rows),
        kernel_count,
        [entry for row in kernel_relation_rows for entry in row],
    )
    presentation = _presentation_from_relation_rows(
        ring,
        kernel_labels,
        relation_labels,
        relation_matrix,
    )
    kernel = FinitelyPresentedModule(presentation)
    inclusion = module_embedding(
        kernel,
        domain,
        {
            label: domain.linear_combination(
                {
                    source_label: from_singular(kernel_lifts[int(label)][position])
                    for position, source_label in enumerate(source_labels)
                    if kernel_lifts[int(label)][position] != 0
                }
            )
            for label in kernel_labels
        },
    )

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
        [
            to_singular(lift_scalar(entry))
            for row in source_relations.rows()
            for entry in row
        ],
    )

    def lift_from_domain(element):
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
            [
                to_singular(
                    lift_scalar(coefficients.get(label, engine.zero()))
                )
                for label in source_labels
            ],
        )
        spanning = kernel_generator_matrix
        if source_relations.nrows():
            spanning = spanning.stack(lifted_source_relation_rows)
        for relation in algebra_relations:
            spanning = spanning.stack(
                to_singular(relation) * identity_matrix(singular_ring, n)
            )
        try:
            lifted = matrix(
                singular_ring,
                ff.lift(
                    spanning.transpose(),
                    requested.transpose(),
                ),
            )
        except RuntimeError as error:
            raise ValueError(
                "the element does not lie in the represented kernel"
            ) from error
        return kernel.linear_combination(
            {
                label: from_singular(lifted[position, 0])
                for position, label in enumerate(kernel_labels)
                if lifted[position, 0] != 0
            }
        )

    inclusion._preamble_lift = lift_from_domain
    kernel._preamble_inclusion = inclusion
    refine(kernel, ModuleSubobjects(ring))
    return kernel


def _presentation_from_relation_rows(
    base_ring,
    labels,
    relation_labels,
    relations,
):
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        BasedFreeModule,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    target = BasedFreeModule(base_ring, labels)
    source = BasedFreeModule(base_ring, relation_labels)
    images = {
        label: _relation_element(target, row)
        for label, row in zip(
            source.module_generating_set(), relations.rows(), strict=True
        )
    }
    return module_homset(source, target)(images)


def FinitelyPresentedModule(presentation):
    r"""Return ``coker(presentation)`` and retain the selected presentation."""
    codomain = presentation.codomain()
    base_ring = owned_ring_view(codomain.base_ring())
    engine = engine_ring(base_ring)

    labels = codomain.module_generating_set()
    existing = _presentation_matrix(codomain)
    added = presentation.tensor().dual_tensor().change_ring(engine)
    relations = existing.change_ring(engine).stack(added)
    if codomain in ModulesWithChosenFinitePresentation(base_ring):
        existing_labels = tuple(
            codomain.presentation().domain().module_generating_set()
        )
        added_labels = tuple(presentation.domain().module_generating_set())
        relation_labels = finite_ordered_set(
            [("existing relation", label) for label in existing_labels]
            + [("cokernel relation", label) for label in added_labels]
        )
        selected_presentation = _presentation_from_relation_rows(
            base_ring,
            labels,
            relation_labels,
            relations,
        )
    else:
        selected_presentation = presentation

    from sage.modules.free_module import FreeModule as SageFreeModule

    free = SageFreeModule(engine, int(labels.cardinality()))
    relation_submodule = (
        free.zero_submodule()
        if relations.upper_ranks()[0] == 0
        else free.submodule([free(row) for row in relations.rows()])
    )
    pid_backend = (
        engine in PrincipalIdealDomains()
        and hasattr(free.basis_matrix(), "_clear_denom")
    )
    if pid_backend:
        quotient = _PresentedModule(
            free,
            relation_submodule,
            base_ring=base_ring,
            module_generating_set=labels,
            relation_matrix=relations,
            presentation=selected_presentation,
        )
    else:
        quotient = _GeneralPresentedModule(
            free,
            relation_submodule,
            base_ring=base_ring,
            module_generating_set=labels,
            relation_matrix=relations,
            presentation=selected_presentation,
        )

    refine(
        quotient,
        [
            FinitelyPresentedModules(base_ring),
            ModulesWithChosenFinitePresentation(base_ring),
        ],
    )

    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import (
        FinitelyPresentedTorsionModules,
    )

    if pid_backend and quotient.is_torsion():
        refine(quotient, FinitelyPresentedTorsionModules(base_ring))
    return quotient


__all__ = [
    "FinitelyPresentedModule",
    "FinitelyPresentedModules",
    "ModulesWithChosenFinitePresentation",
    "_presentation_matrix",
]
