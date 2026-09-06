r"""Modules equipped as localizations of modules over the source ring."""

from sage.categories.category import Category
from sage.misc.unknown import Unknown
from sage.structure.element import ModuleElement
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    _SelectedFinitePresentationModules,
    _presentation_rows,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
    MatrixSpace,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedModules,
    FinitelyPresentedModules,
    FramedModules,
    ModuleSubobjects,
    Modules,
    ModulesWithChosenFinitePresentation,
    register_module_scalar_action,
)
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism
from dzack_research.preamble.categories.sets.set_categories import Sets


class LocalizedModules(OwnedCategoryOverBaseRing):
    r"""Modules represented as ``S^{-1}M`` for a chosen localization ``S^{-1}R``."""

    def an_object(self):
        r"""``S^{-1}(R^2)`` for ``S^{-1}R`` this category's ring."""
        from dzack_research.preamble.categories.functors.module_localization import (
            ModuleLocalizationFunctor,
        )
        from dzack_research.preamble.categories.rings.commutative_algebra import LocalizationRings
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import BasedFreeModule
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        localization_ring = self.base_ring()
        assert localization_ring in LocalizationRings(), (
            f"{localization_ring} is not a represented localization, so no module "
            "over it is a localization of a module over its source"
        )
        source = BasedFreeModule(
            localization_ring.localization_source(), finite_ordinal_set(2)
        )
        return ModuleLocalizationFunctor(localization_ring)(source)

    def super_categories(self):

        return [Modules(self.base_ring())]

    class ElementMethods(ModuleElement):
        r"""A represented fraction ``m/s`` in ``S^{-1}M``."""

        def __init__(self, parent, numerator, denominator) -> None:
            ModuleElement.__init__(self, parent)
            self._numerator = numerator
            self._denominator = denominator

        def numerator(self):
            return self._numerator

        def denominator(self):
            return self._denominator

        def _add_(self, other):
            parent = self.parent()
            source = parent.localization_source_module()
            numerator = (
                source.scalar_multiple(other.denominator(), self.numerator())
                + source.scalar_multiple(self.denominator(), other.numerator())
            )
            return parent.fraction(
                numerator,
                self.denominator() * other.denominator(),
                _trusted_denominator=True,
            )

        def _neg_(self):
            return self.parent().fraction(
                -self.numerator(),
                self.denominator(),
                _trusted_denominator=True,
            )

        def _lmul_(self, scalar):
            return self.parent().scalar_multiple(scalar, self)

        def _rmul_(self, scalar):
            return self.parent().scalar_multiple(scalar, self)

        def _acted_upon_(self, actor, self_on_left):
            try:
                scalar = self.parent().base_ring()(actor)
            except (TypeError, ValueError):
                return None
            return self.parent().scalar_multiple(scalar, self)

        def equality_status(self, other):
            r"""Return ``True``, ``False``, or ``Unknown`` for fraction equality."""
            if other.parent() is not self.parent():
                return False
            return self.parent()._fraction_equality_status(self, other)

        def _richcmp_(self, other, op):
            if op not in (op_EQ, op_NE):
                return NotImplemented
            status = self.equality_status(other)
            if status is Unknown:
                raise NotImplementedError(
                    "equality of these localization fractions is not decidable from the represented data"
                )
            return bool(status) if op == op_EQ else not bool(status)

        def _repr_(self):
            if self.denominator() == self.parent().source_ring().one():
                return repr(self.numerator())
            return f"({self.numerator()})/({self.denominator()})"

    class ParentMethods:
        def __init__(
            self,
            source_module,
            localization_ring,
            localization_functor,
            **rest,
        ) -> None:
            self._source_module = source_module
            self._preamble_localization_ring = localization_ring
            self._preamble_localization_submonoid = localization_ring.localization_submonoid()
            self._preamble_localization_functor = localization_functor
            source_ring = localization_ring.localization_source()
            framed_source = source_module in FramedModules(source_ring)
            super().__init__(base_ring=localization_ring, **rest)
            if framed_source:
                # Localization chooses no new framing: after the generic framed
                # initializer has run, carry the source generators to their
                # images in S^{-1}M.
                self._preamble_module_generating_set = (
                    source_module.module_generating_set()
                )
                self._preamble_module_generator_function = lambda label: self.fraction(
                    source_module.module_generator(label)
                )
                self._preamble_module_coefficient_function = self._framing_coefficients
            self._preamble_scalar_action_morphism = self._build_scalar_action_morphism()

        def _framing_coefficients(self, element):
            r"""Return coefficients of a localization fraction in the source framing."""

            element = self(element)
            source_coefficients = module_coefficients(
                element.numerator(),
                self.localization_source_module(),
            )
            localization_map = self.localization_ring().localization_map()
            denominator = localization_map(element.denominator())
            denominator_inverse = denominator.inverse_of_unit()
            return {
                label: localization_map(coefficient) * denominator_inverse
                for label, coefficient in source_coefficients.items()
                if coefficient != self.source_ring().zero()
            }

        def base_ring(self):
            return self.localization_ring()

        def base(self):
            return self.base_ring()

        def source_ring(self):
            return self.localization_ring().localization_source()

        def _valid_denominator(self, denominator) -> bool:
            source = self.source_ring()
            denominator = source(denominator)
            try:
                image = self.localization_ring().localization_map()(denominator)
                return bool(image.is_unit())
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                try:
                    return denominator in self.localization_submonoid()
                except NotImplementedError:
                    return False

        def fraction(self, numerator, denominator=None, *, _trusted_denominator=False):
            source_module = self.localization_source_module()
            numerator = source_module(numerator)
            source = self.source_ring()
            denominator = source.one() if denominator is None else source(denominator)
            if not _trusted_denominator and not self._valid_denominator(denominator):
                raise ValueError(
                    f"{denominator} is not represented as invertible in {self.localization_ring()}"
                )
            return self.element_class(self, numerator, denominator)

        def _element_constructor_(self, value):
            if value.parent() is self:
                return value
            if isinstance(value, tuple) and len(value) == 2:
                return self.fraction(value[0], value[1])
            return self.fraction(value)

        def zero(self):
            return self.fraction(self.localization_source_module().zero())

        def _fraction_equality_status(self, left, right):
            source = self.localization_source_module()
            cross_difference = (
                source.scalar_multiple(right.denominator(), left.numerator())
                - source.scalar_multiple(left.denominator(), right.numerator())
            )
            if cross_difference == source.zero():
                return True

            torsion_free = getattr(source, "is_torsion_free", None)
            if torsion_free is not None:
                try:
                    if torsion_free() is True:
                        return False
                except (NotImplementedError, TypeError, ValueError):
                    pass

            # For a presented module, d/1 vanishes after localization exactly
            # when Ann_R(d) meets the localization submonoid.  The cyclic
            # submodule R*d represents Ann_R(d) through the existing scalar-
            # action kernel, so no second presentation backend is needed here.
            try:
                if source in _SelectedFinitePresentationModules(self.source_ring()):
                    annihilator = source.subobject_on((cross_difference,)).annihilator()
                    structure = self.localization_submonoid().structure_data()

                    if structure.get("kind") == "prime_complement":
                        prime = structure.get("prime_ideal")
                        if prime is not None:
                            return any(
                                not prime.contains_ambient_element(generator)
                                for generator in annihilator.ideal_generators()
                            )

                    generators = tuple(
                        self.localization_submonoid().monoid_generators()
                    )
                    if not generators:
                        return False
                    product = self.source_ring().one()
                    for generator in generators:
                        product *= generator

                    # If S=<s_1,...,s_r> and p=prod s_i, then
                    # Ann(d) meets S iff p lies in radical(Ann(d)): an
                    # annihilating monomial divides a sufficiently large
                    # power of p, and p^N itself is an S-witness conversely.
                    try:
                        return annihilator.radical().contains_ambient_element(product)
                    except (AttributeError, NotImplementedError, TypeError, ValueError):
                        # A direct annihilator witness is still exact even when
                        # the represented ideal backend has no radical operation.
                        if annihilator.contains_ambient_element(product):
                            return True
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                pass

            # If M is finite and S has finitely many selected generators, the
            # orbit of the cross-difference under S is finite.  Search that orbit
            # exactly for an element killed by some denominator witness.
            try:
                if source.is_finite() is True:
                    generators = tuple(self.localization_submonoid().monoid_generators())
                    pending = [cross_difference]
                    seen = []
                    while pending:
                        current = pending.pop()
                        if current == source.zero():
                            return True
                        if any(current == old for old in seen):
                            continue
                        seen.append(current)
                        for generator in generators:
                            pending.append(source.scalar_multiple(generator, current))
                    return False
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                pass
            return Unknown

        def _raw_localized_scalar_multiple(self, scalar, element):
            element = self(element)
            numerator, denominator = self.localization_ring().localization_fraction_data(scalar)
            source = self.localization_source_module()
            return self.fraction(
                source.scalar_multiple(numerator, element.numerator()),
                denominator * element.denominator(),
                _trusted_denominator=True,
            )

        def _build_scalar_action_morphism(self):

            endomorphisms = Modules(self.base_ring()).End(self)
            return ring_morphism(
                self.base_ring(),
                endomorphisms,
                lambda scalar: endomorphisms.elementwise(
                    lambda element: self._raw_localized_scalar_multiple(scalar, element),
                    verify_linearity=False,
                ),
            )

        def _ring_morphism_defining_module_action(self):
            return self._preamble_scalar_action_morphism

        def is_finite(self):
            answer = self.localization_source_module().is_finite()
            return answer if answer is Unknown else bool(answer)

        def is_zero(self):
            r"""Decide whether this localization is zero from finite generators or a finite source."""
            source = self.localization_source_module()

            # A finitely generated module localizes to zero exactly when its
            # chosen finite generating family does.  Fraction equality carries
            # the denominator witness, so this also covers infinite presented
            # modules such as R/(f) localized at f.
            try:
                if source in FinitelyGeneratedModules(self.source_ring()):
                    statuses = tuple(
                        self.fraction(source.module_generator(label)).equality_status(
                            self.zero()
                        )
                        for label in source.module_generating_set()
                    )
                    if any(status is False for status in statuses):
                        return False
                    if all(status is True for status in statuses):
                        return True
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                pass

            if self.is_finite() is not True:
                return Unknown
            try:
                for element in source:
                    status = self.fraction(element).equality_status(self.zero())
                    if status is Unknown:
                        return Unknown
                    if status is False:
                        return False
                return True
            except (NotImplementedError, TypeError, ValueError):
                return Unknown

        def _repr_(self):
            return (
                f"{self.localization_source_module()} localized along "
                f"{self.localization_ring().localization_map()}"
            )
        def localization_source_module(self):
            source = self.__dict__.get("_source_module")
            if source is not None:
                return source
            return self.localization_functor().chosen_preimage(self)

        def localization_ring(self):
            return self._preamble_localization_ring

        def localization_submonoid(self):
            return self._preamble_localization_submonoid

        def localization_functor(self):
            return self._preamble_localization_functor

        def localization_unit(self):
            return self.localization_functor().unit(
                self.localization_source_module(),
                localized=self,
            )

        def restriction_to(self, target_ring):
            r"""Return ``S^{-1}M -> T^{-1}M`` over the ring restriction ``S^{-1}R -> T^{-1}R``.

            Both localizations are built on the same source module and keep its
            framing, so the restriction carries a generator to the generator of
            the same name: as fractions it is ``m/s`` to ``m/s``.  It is
            ``S^{-1}R``-linear into the restriction of scalars of ``T^{-1}M``,
            which is where a map between modules over different rings lives.

            This is the sheaf restriction of ``M~`` along ``D(g) <= D(f)``, and
            at a prime it is the map from a section to its germ in the stalk.
            """

            source_module = self.localization_source_module()
            target = target_ring.localize_module(source_module)
            restriction = self.localization_ring().restriction_to(target_ring)
            restricted = target.restrict_scalars(restriction)
            return module_homset(self, restricted)(
                lambda label: restricted(target.module_generator(label))
            )

        def localization_prime_point(self):
            point = self.__dict__.get("_preamble_localization_prime_point")
            if point is None:
                raise ValueError("this localization was not selected at a prime point")
            return point






__all__ = [
    "LocalizedModule",
    "LocalizedModules",
]


def LocalizedModule(
    source_module,
    localization_ring,
    localization_functor,
    *,
    subobject_ambient=None,
    subobject_generator_images=None,
    subobject_lift=None,
    subobject_inclusion_factory=None,
    subobject_verify_linearity=True,
    extra_categories=(),
    extra_construction_data=None,
):
    r"""Return ``S^{-1}M``, placed by what the source module already is.

    A localized module is a subobject when the construction selects an
    inclusion, and is framed, finitely generated, or finitely presented exactly
    when its source is: localization is exact, so a presentation of ``M`` maps
    to a presentation of ``S^{-1}M`` under ``R -> S^{-1}R``.
    """
    placement = [LocalizedModules(localization_ring), *tuple(extra_categories)]
    data = {
        "source_module": source_module,
        "localization_ring": localization_ring,
        "localization_functor": localization_functor,
    }
    if extra_construction_data is not None:
        data.update(extra_construction_data)

    if subobject_inclusion_factory is not None or (
        subobject_ambient is not None and subobject_generator_images is not None
    ):
        placement.append(ModuleSubobjects(localization_ring))
        data.update(
            subobject_ambient=subobject_ambient,
            subobject_generator_images=subobject_generator_images,
            subobject_lift=subobject_lift,
            subobject_inclusion_factory=subobject_inclusion_factory,
            subobject_verify_linearity=subobject_verify_linearity,
        )

    source_ring = localization_ring.localization_source()
    if source_module in FramedModules(source_ring):
        placement.append(FramedModules(localization_ring))
        if source_module in FinitelyGeneratedModules(source_ring):
            placement.append(FinitelyGeneratedModules(localization_ring))
        if source_module in ModulesWithChosenFinitePresentation(source_ring):
            data.update(
                _transported_presentation(source_module, localization_ring)
            )
            placement.extend(
                [
                    FinitelyPresentedModules(localization_ring),
                    ModulesWithChosenFinitePresentation(localization_ring),
                    _SelectedFinitePresentationModules(localization_ring),
                ]
            )

    return object_of(Category.join(placement), **data)


def _transported_presentation(source_module, localization_ring):
    r"""Return the presentation of ``S^{-1}M`` induced by one of ``M``.

    Localization is exact, so applying ``R -> S^{-1}R`` to the relation rows of
    a presentation of ``M`` presents ``S^{-1}M`` on the images of the same
    generators.
    """
    source_ring = localization_ring.localization_source()
    relation_rows = _presentation_rows(source_module)
    if source_module in _SelectedFinitePresentationModules(source_ring):
        relation_labels = source_module.presentation().domain().module_generating_set()
    else:
        relation_labels = Sets.Δ[len(relation_rows) - 1]
    generator_labels = source_module.module_generating_set()
    localization_map = localization_ring.localization_map()
    transported_rows = tuple(
        tuple(localization_map(coefficient) for coefficient in row)
        for row in relation_rows
    )
    relation_matrix = MatrixSpace(
        localization_ring,
        len(transported_rows),
        int(generator_labels.cardinality()),
    ).from_rows(transported_rows)
    free_relations = BasedFreeModule(localization_ring, relation_labels)
    free_generators = BasedFreeModule(localization_ring, generator_labels)
    images = {
        relation_label: free_generators.linear_combination(
            {
                generator_label: coefficient
                for generator_label, coefficient in zip(
                    generator_labels,
                    row,
                    strict=True,
                )
                if coefficient != localization_ring.zero()
            }
        )
        for relation_label, row in zip(relation_labels, transported_rows, strict=True)
    }
    return {
        "relation_matrix": relation_matrix,
        "presentation": module_homset(free_relations, free_generators)(images),
    }
