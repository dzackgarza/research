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

            custom = self.__dict__.get("_preamble_module_coordinate_function")
            if custom is not None:
                return tensor.vector(
                    engine_ring(self.base_ring()),
                    tuple(custom(element)),
                )

            if not isinstance(self, FGP_Module_class):
                lift = element.lift() if hasattr(element, "lift") else element
                return self.V().coordinate_vector(lift)

            coordinates = FGP_Module_class.coordinate_vector(self, element, reduce=False)
            engine = engine_ring(self.base_ring())
            if not reduce or engine is not SageZZ:
                return coordinates
            invariants = self.invariants()
            return tensor.vector(
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
            if not isinstance(self, FGP_Module_class):
                raise NotImplementedError(
                    "torsion detection is currently computed from PID invariant factors"
                )
            engine = engine_ring(self.base_ring())
            if engine.is_field():
                return self.is_zero()
            return self.rank() == 0

        def is_torsion_free(self):
            if not isinstance(self, FGP_Module_class):
                raise NotImplementedError(
                    "torsion-freeness is currently computed from PID invariant factors"
                )
            return all(
                invariant == 0 or invariant.is_unit()
                for invariant in self.invariants(include_ones=True)
            )

        def is_zero(self):
            if not isinstance(self, FGP_Module_class):
                raise NotImplementedError(
                    "zero detection is currently computed from PID invariant factors"
                )
            return all(
                invariant.is_unit()
                for invariant in self.invariants(include_ones=True)
            )

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
            inverse_right = right**-1
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
            inverse_right = (right**-1).change_ring(engine)
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
                        base_change_scalar(ring_map, coefficient)
                        * target.module_generator(module_label)
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
    relations = tensor.matrix(engine, existing.stack(added))
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
        if relations.nrows() == 0
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
