"""Linear maps between represented modules."""

import logging
import operator
from itertools import product

from sage.categories.action import Action
from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_element,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.set_categories import (
    CartesianProductOfSets,
    Sets,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    coordinate_family as _coordinate_family,  # noqa: F401 -- compatibility import for powers.py
    coordinate_family_from_function as _coordinate_family_from_function,  # noqa: F401
    coordinate_pair as _coordinate_pair,  # noqa: F401
    finite_framing as _finite_framing,  # noqa: F401
)
from dzack_research.preamble.refine import refine


_LOGGER = logging.getLogger(__name__)


def _has_finite_free_framing(module) -> bool:
    r"""Return whether ``module`` represents a finite free module with framing."""
    if not bool(getattr(module, "is_free", lambda: False)()):
        return False
    labels = getattr(module, "module_generating_set", lambda: None)()
    if labels is None:
        return False
    from dzack_research.preamble.categories.sets.cardinals import cardinal

    return cardinal(labels.cardinality()).is_finite()


def _solve_left_integrally_element(system, target, ring):
    r"""Return the row-coefficient element ``a`` with ``a*system = target``."""
    from dzack_research.preamble.categories.rings.ring_foundation import OwnedRings

    if ring not in OwnedRings():
        raise TypeError("integral solving requires an owned coefficient ring")

    try:
        matrix_parent = system.parent()
    except AttributeError:
        matrix_parent = None
    if matrix_parent is not None and callable(getattr(matrix_parent, "matrix_shape", None)):
        matrix_system = system
    else:
        raise TypeError("an integral linear system is an owned matrix Hom element")

    transposed = matrix_system.transpose()
    smith, left, right = transposed.smith_form()

    target_labels = left.domain().module_generating_set()
    target_values = tuple(ring(value) for value in target)
    if len(target_values) != int(target_labels.cardinality()):
        raise ValueError("the target has the wrong length for this linear system")
    target_vector = left.domain().linear_combination(
        {
            label: target_values[position]
            for position, label in enumerate(target_labels)
            if target_values[position]
        }
    )
    shifted_vector = left(target_vector)
    shifted_coefficients = module_coefficients(
        shifted_vector, left.codomain()
    )
    shifted_labels = left.codomain().module_generating_set()

    source_labels = smith.domain().module_generating_set()
    width = int(source_labels.cardinality())
    solution = [ring.zero()] * width
    for index, shifted_label in enumerate(shifted_labels):
        value = shifted_coefficients.get(shifted_label, ring.zero())
        divisor = (
            smith[index, index]
            if index < min(int(shifted_labels.cardinality()), width)
            else ring.zero()
        )
        if divisor == 0:
            if value != 0:
                raise ValueError("the element is not in the image of this morphism")
            continue
        quotient, remainder = value.quo_rem(divisor)
        if remainder != 0:
            raise ValueError("the element is not in the image over the base ring")
        solution[index] = quotient

    normalized_solution = right.domain().linear_combination(
        {
            label: solution[position]
            for position, label in enumerate(right.domain().module_generating_set())
            if solution[position]
        }
    )
    return right(normalized_solution)


def _solve_left_integrally(system, target, ring):
    r"""Return positional coefficients ``a`` with ``a*system = target`` over a PID."""
    original_solution = _solve_left_integrally_element(system, target, ring)
    coefficients = module_coefficients(original_solution, original_solution.parent())
    return tuple(
        coefficients.get(label, ring.zero())
        for label in original_solution.parent().module_generating_set()
    )


def module_coefficients(element, module=None) -> dict:
    r"""Return coefficients in the selected framing of the stated module.

    ``module`` is normally ``element.parent()``.  It is explicit at facade
    boundaries such as number-field orders, whose Sage elements retain the
    number field as their concrete parent even when regarded as elements of
    the order.
    """
    if module is None:
        module = element.parent()
    coefficient_function = module.__dict__.get("_preamble_module_coefficient_function")
    if coefficient_function is not None:
        # The selected framing owns its coefficient map.  This takes
        # precedence over any representation-specific realization such as a
        # localization fraction model.
        return {
            label: module.base_ring()(coefficient)
            for label, coefficient in coefficient_function(element).items()
            if coefficient != 0
        }

    coordinate_function = module.__dict__.get("_preamble_module_coordinate_function")
    if coordinate_function is not None:
        labels = module.module_generating_set()
        coordinates = iter(coordinate_function(element))
        result = {}
        for label in labels:
            try:
                coefficient = next(coordinates)
            except StopIteration as error:
                raise ValueError(
                    "the selected module-coordinate function returned too few coordinates"
                ) from error
            coefficient = module.base_ring()(coefficient)
            if coefficient != 0:
                result[label] = coefficient
        try:
            next(coordinates)
        except StopIteration:
            return result
        raise ValueError(
            "the selected module-coordinate function returned too many coordinates"
        )
    selected = module._selected_module_coefficients(element)
    if selected is not None:
        return selected
    from dzack_research.preamble.categories.rings.ring_foundation import OwnedOrders

    if module in OwnedOrders():
        labels = module.module_generating_set()
        engine = _engine_ring(module)
        backend_element = _engine_element(module, element)
        coordinates = iter(
            (SageZZ(backend_element),)
            if engine is SageZZ
            else engine.coordinates(backend_element)
        )
        result = {}
        base = module.base_ring()
        base_engine = _engine_ring(base)
        for label in labels:
            try:
                coefficient = next(coordinates)
            except StopIteration as error:
                raise ValueError("the order coordinate backend returned too few coordinates") from error
            if coefficient != 0:
                result[label] = base._from_engine_element(base_engine(coefficient))
        try:
            next(coordinates)
        except StopIteration:
            return result
        raise ValueError("the order coordinate backend returned too many coordinates")
    # An element that stores its own finite support in the framing.
    return dict(element.monomial_coefficients())


class ModuleMorphism(Morphism):
    r"""The linear extension of a function on a chosen module framing."""

    def __init__(
        self,
        parent,
        images,
        *,
        elementwise=False,
        verify_linearity=True,
    ) -> None:
        Morphism.__init__(self, parent)
        self._element_function = None
        framed_domain = bool(self.domain().is_framed())
        if elementwise or not framed_domain:
            if not callable(images):
                raise TypeError(
                    "a morphism from an unframed module must be supplied as an exact element map"
                )
            self._element_function = images
            self._generator_image = None
            self._generator_morphism = None
            if verify_linearity:
                self._verify_elementwise_linearity_when_decidable()
            return
        labels = self.domain().module_generating_set()
        set_homset = Sets().hom(labels, self.codomain())
        if isinstance(images, SetMorphism):
            self._generator_image = images._call_
            self._generator_morphism = images
        elif isinstance(images, dict):
            from sage.rings.infinity import Infinity

            assert labels.cardinality() != Infinity
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(f"generator assignment omits {missing}")
            self._generator_image = images.__getitem__
            self._generator_morphism = SetMorphism(set_homset, images.__getitem__)
        elif isinstance(images, (tuple, list)):
            from sage.rings.infinity import Infinity

            assert labels.cardinality() != Infinity
            values = tuple(images)
            labels_tuple = tuple(labels)
            if len(values) != len(labels_tuple):
                raise ValueError("the number of generator images must equal the framing size")
            assignment = dict(zip(labels_tuple, values, strict=True))
            self._generator_image = assignment.__getitem__
            self._generator_morphism = SetMorphism(set_homset, assignment.__getitem__)
        elif callable(images):
            self._generator_image = images
            self._generator_morphism = SetMorphism(set_homset, images)
        else:
            raise TypeError("a module morphism is specified on the domain framing")
        self._check_selected_domain_relations()

    def _verify_elementwise_linearity_when_decidable(self) -> None:
        r"""Check an elementwise callable exactly in represented decidable regimes.

        A Python callable does not carry a proof of linearity.  When both the
        scalar ring and the source module are finite and enumerable, linearity
        is decidable by exhaustive verification.  Over ``ZZ`` a finite source
        only needs exhaustive additivity, since every additive-group map is
        automatically ``ZZ``-linear.  Outside such regimes the callable is a
        declared linear map; a DEBUG diagnostic records that no exhaustive
        verification was available.
        """
        function = self._element_function
        if function is None:
            return

        domain = self.domain()
        codomain = self.codomain()
        source_elements = self._finite_source_elements_for_verification()
        if source_elements is not None:
            self._verify_elementwise_on_finite_source(source_elements)
            return

        try:
            source_finite = bool(domain.is_finite())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            source_finite = False

        if not source_finite:
            self._check_elementwise_zero_when_possible()
            _LOGGER.debug(
                "Elementwise module morphism %s -> %s accepted without exhaustive "
                "linearity verification; source carrier is not represented as finite",
                domain,
                codomain,
            )
            return

        try:
            source_elements = tuple(domain)
        except (AttributeError, TypeError):
            self._check_elementwise_zero_when_possible()
            _LOGGER.debug(
                "Elementwise module morphism %s -> %s accepted without exhaustive "
                "linearity verification; finite source has no represented enumeration",
                domain,
                codomain,
            )
            return

        self._verify_elementwise_on_finite_source(source_elements)

    def _finite_source_elements_for_verification(self):
        r"""Enumerate a finitely generated module over a finite ring via its framing."""
        domain = self.domain()
        ring = domain.base_ring()
        from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring

        if not domain.is_framed():
            return None
        try:
            labels = tuple(domain.module_generating_set())
        except (AttributeError, TypeError):
            return None
        engine = _engine_ring(ring)
        try:
            if not bool(engine.is_finite()):
                return None
            scalars = tuple(
                ring._from_engine_element(engine(scalar))
                for scalar in engine
            )
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return None
        elements = []
        seen = set()
        for coefficients in product(scalars, repeat=len(labels)):
            element = domain.linear_combination(
                {
                    label: coefficient
                    for label, coefficient in zip(labels, coefficients, strict=True)
                    if coefficient != 0
                }
            )
            try:
                key = element
                if key in seen:
                    continue
                seen.add(key)
            except TypeError:
                if any(element == previous for previous in elements):
                    continue
            elements.append(element)
        return tuple(elements)

    def _verify_elementwise_on_finite_source(self, source_elements) -> None:
        function = self._element_function
        domain = self.domain()
        codomain = self.codomain()
        ring = domain.base_ring()
        zero = domain.zero()
        if function(zero) != codomain.zero():
            raise ValueError("an elementwise module morphism must send zero to zero")
        for left in source_elements:
            for right in source_elements:
                if function(left + right) != function(left) + function(right):
                    raise ValueError("the supplied elementwise map is not additive")

        from sage.rings.integer_ring import ZZ as SageZZ

        from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring

        if _engine_ring(ring) is SageZZ:
            return

        try:
            scalar_finite = bool(ring.is_finite())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            scalar_finite = False
        if not scalar_finite:
            _LOGGER.debug(
                "Elementwise map %s -> %s is exhaustively additive on its finite source, "
                "but scalar-linearity over infinite %s was not exhaustively verified",
                domain,
                codomain,
                ring,
            )
            return
        try:
            engine = _engine_ring(ring)
            scalars = tuple(
                ring._from_engine_element(engine(scalar))
                for scalar in engine
            )
        except TypeError:
            _LOGGER.debug(
                "Elementwise map %s -> %s is exhaustively additive, but finite scalar "
                "ring %s has no represented enumeration",
                domain,
                codomain,
                ring,
            )
            return
        for scalar in scalars:
            for element in source_elements:
                if function(domain.scalar_multiple(scalar, element)) != codomain.scalar_multiple(
                    scalar, function(element)
                ):
                    raise ValueError("the supplied elementwise map is not scalar-linear")

    def _check_elementwise_zero_when_possible(self) -> None:
        try:
            source_zero = self.domain().zero()
            target_zero = self.codomain().zero()
            image = self._element_function(source_zero)
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return
        if image != target_zero:
            raise ValueError("an elementwise module morphism must send zero to zero")

    def _check_selected_domain_relations(self) -> None:
        if self._element_function is not None:
            return
        domain = self.domain()
        rows = domain._selected_presentation_rows()
        if rows is None:
            return
        zero = self.codomain().zero()
        labels = domain.module_generating_set()
        for row in rows:
            relation_image = self._linear_combination_of_generator_images(
                {
                    label: coefficient
                    for label, coefficient in zip(labels, row, strict=True)
                    if coefficient
                }
            )
            if relation_image != zero:
                raise ValueError(
                    "the selected module-generator images do not kill the domain relations"
                )

    def module_generator_morphism(self):
        if self._generator_morphism is None:
            raise NotImplementedError(
                "an unframed morphism has no selected generator map"
            )
        return self._generator_morphism

    def __add__(self, other):
        if not isinstance(other, ModuleMorphism):
            return NotImplemented
        if other.domain() is not self.domain() or other.codomain() is not self.codomain():
            return NotImplemented
        parent = self.parent()
        return parent.elementwise(
            lambda element: self(element) + other(element),
            verify_linearity=False,
        )

    def __neg__(self):
        parent = self.parent()
        return parent.elementwise(
            lambda element: -self(element),
            verify_linearity=False,
        )

    def __sub__(self, other):
        if not isinstance(other, ModuleMorphism):
            return NotImplemented
        return self + (-other)

    def morphisms_agree(self, other) -> bool:
        r"""Decide equality from this source module's selected finite framing."""
        if not isinstance(other, ModuleMorphism):
            return False
        if self.domain() is not other.domain() or self.codomain() is not other.codomain():
            return False
        if self is other:
            return True
        from dzack_research.preamble.categories.sets.cardinals import cardinal

        domain = self.domain()
        generating_set = getattr(domain, "module_generating_set", None)
        if not callable(generating_set):
            raise NotImplementedError(
                "equality of morphisms without a selected module framing is not decidable"
            )
        labels = generating_set()
        try:
            finite = cardinal(labels.cardinality()).is_finite()
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            finite = False
        if not finite:
            raise NotImplementedError(
                "equality of morphisms from an infinite framing is not decidable"
            )
        return all(
            self(domain.module_generator(label))
            == other(domain.module_generator(label))
            for label in labels
        )

    def _richcmp_(self, other, op):
        from sage.structure.richcmp import op_EQ, op_NE

        if op not in (op_EQ, op_NE):
            return NotImplemented
        if not isinstance(other, ModuleMorphism) or other.parent() is not self.parent():
            return op == op_NE
        equal = self.morphisms_agree(other)
        return equal if op == op_EQ else not equal

    def __rmul__(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _lmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _rmul_(self, scalar):
        return self._lmul_(scalar)

    def _acted_upon_(self, actor, self_on_left):
        r"""Use the canonical pointwise scalar action of the Hom module."""
        try:
            scalar = self.parent().base_ring()(actor)
        except (TypeError, ValueError):
            return None
        return self.parent().scalar_multiple(scalar, self)

    def _linear_combination_of_generator_images(self, coefficients):
        r"""Evaluate a linear combination through the codomain module interface.

        Owned ring facades deliberately do not require Sage's coercion model
        to identify native coefficient elements with the facade parent.  Raw
        ``scalar * element`` therefore bypasses the module abstraction.  The
        linear extension is intrinsic: apply the codomain's represented scalar
        action directly to each selected generator image and add the results.
        No codomain framing is involved.
        """
        codomain = self.codomain()
        ring = codomain.base_ring()
        return sum(
            (
                codomain.scalar_multiple(
                    ring(source_coefficient),
                    self._generator_image(source_label),
                )
                for source_label, source_coefficient in coefficients.items()
            ),
            codomain.zero(),
        )

    def _call_(self, element):
        if element.parent() is not self.domain():
            element = self.domain()(element)
        if self._element_function is not None:
            image = self._element_function(element)
            return image if image.parent() is self.codomain() else self.codomain()(image)
        coefficients = module_coefficients(element, self.domain())
        return self._linear_combination_of_generator_images(coefficients)

    def matrix(self):
        r"""Return the underlying free-module morphism under the matrix-Hom identification.

        If this already lies in the full module Hom, it is returned literally.
        A stricter structured morphism (for example a lattice isometry) is
        first regarded as the corresponding element of the full ``R``-module
        Hom with the same endpoints.
        """

        ring = self.domain().base_ring()
        if not (
            _has_finite_free_framing(self.domain())
            and _has_finite_free_framing(self.codomain())
        ):
            raise NotImplementedError(
                "a coordinate matrix requires finitely generated framed free endpoints"
            )
        homset = module_homset(self.domain(), self.codomain())
        if not callable(getattr(homset, "matrix_shape", None)):
            raise ArithmeticError("the full finite-free Hom did not acquire matrix structure")
        return self if self.parent() is homset else homset(self)

    def stack(self, other):
        r"""Return ``(self,other)`` into the biproduct of the codomains."""
        if not isinstance(other, ModuleMorphism) or other.domain() is not self.domain():
            raise ValueError("stacking module maps requires one common domain")
        from dzack_research.preamble.categories.abstract_categories.constructions import Biproduct

        target = Biproduct(self.codomain(), other.codomain())
        return target.to_product(self, other)

    @cached_method
    def kernel(self):
        r"""Return ``ker(self)`` as a subobject of the domain."""
        source_morphism = getattr(
            self,
            "_preamble_localization_source_morphism",
            None,
        )
        localization_functor = getattr(
            self,
            "_preamble_localization_functor",
            None,
        )
        if source_morphism is not None and localization_functor is not None:
            source_kernel = source_morphism.kernel()
            localized_kernel = localization_functor(source_kernel)
            localized_inclusion = localization_functor(source_kernel.inclusion())
            if localized_inclusion.codomain() is not self.domain():
                raise ArithmeticError(
                    "localized kernel inclusion does not land in the cached localized domain"
                )
            return localized_kernel._as_module_subobject(localized_inclusion)

        for owner in (self.domain(), self.codomain()):
            represented = owner._represented_kernel_of_morphism(self)
            if represented is not NotImplemented:
                return represented
        raise NotImplementedError(
            "this kernel has no represented finite-free or general polynomial-presentation backend"
        )

    def image(self):
        r"""Return ``im(self)`` as a subobject of the codomain."""
        from sage.rings.infinity import Infinity

        assert self.domain().rank() != Infinity
        from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family

        labels = self.domain().module_generating_set()
        return self.codomain().subobject_on(
            finite_indexed_family(
                labels,
                lambda label: self(self.domain().module_generator(label)),
                name="Image spanning family",
            )
        )

    def is_injective(self) -> bool:
        r"""Return whether ``ker(self)=0`` when the kernel is computable."""
        return self.kernel().rank() == 0

    def is_surjective(self) -> bool:
        r"""Return whether ``coker(self)=0`` when the cokernel is computable."""
        return self.cokernel().is_zero()

    def residue_morphism(self):
        r"""Return ``f tensor_R k`` for a morphism of finite modules over a local ring."""
        from dzack_research.preamble.categories.rings.ring_foundation import LocalRings

        ring = self.domain().base_ring()
        if self.codomain().base_ring() is not ring:
            raise ValueError("a residue morphism requires one common base ring")
        if ring not in LocalRings():
            raise TypeError("reduction modulo the maximal ideal requires a represented local ring")
        if not (
            bool(getattr(self.domain(), "is_finitely_generated", lambda: False)())
            and bool(getattr(self.codomain(), "is_finitely_generated", lambda: False)())
        ):
            raise TypeError(
                "the active Nakayama interface requires finitely generated source and target"
            )
        return self.base_change(ring.residue_map())

    reduction_mod_maximal_ideal = residue_morphism

    def is_surjective_mod_maximal_ideal(self) -> bool:
        r"""Return whether ``f tensor_R k`` is surjective."""
        return self.residue_morphism().is_surjective()

    def is_surjective_by_nakayama(self) -> bool:
        r"""Use Nakayama: a map onto a finite local module is surjective iff its residue map is."""
        return self.is_surjective_mod_maximal_ideal()

    def is_primitive(self) -> bool:
        r"""Return whether this monomorphism has torsion-free cokernel."""
        if not self.is_injective():
            return False
        return self.cokernel().is_torsion_free()

    is_saturated = is_primitive

    def saturation(self):
        r"""Return the saturation of the image of an injective morphism.

        For ``i:S -> M`` this is the kernel of
        ``M -> M/S -> (M/S)/Tor(M/S)``.
        """
        if not self.is_injective():
            raise ValueError("saturation is defined here for a monomorphism")
        quotient = self.cokernel()
        projection = quotient.torsion_free_quotient_projection()
        composite = projection * quotient.presentation_projection()
        return composite.kernel()

    def index(self):
        r"""Return the cardinality of the cokernel."""
        return self.cokernel().cardinality()

    def lift(self, element):
        r"""Return the unique preimage of ``element`` for an injective free map."""
        custom = self.__dict__.get("_preamble_lift")
        if custom is not None:
            return custom(element)
        ring = self.domain().base_ring()
        if not (
            _has_finite_free_framing(self.domain())
            and _has_finite_free_framing(self.codomain())
        ):
            raise NotImplementedError(
                "the coordinate lift requires finite free framed endpoints"
            )
        if element.parent() is not self.codomain():
            element = self.codomain()(element)
        codomain_labels = tuple(self.codomain().module_generating_set())
        coefficients = module_coefficients(element, self.codomain())
        target = [
            coefficients[label]
            if label in coefficients
            else self.codomain().base_ring().zero()
            for label in codomain_labels
        ]
        solution = _solve_left_integrally(
            self.matrix().transpose(),
            target,
            ring,
        )
        return self.domain().linear_combination(
            {
                label: coefficient
                for label, coefficient in zip(
                    self.domain().module_generating_set(), solution, strict=True
                )
                if coefficient
            }
        )

    def is_in_image(self, element) -> bool:
        r"""Return whether ``element`` has a preimage when the lift is decidable."""
        try:
            self.lift(element)
        except (TypeError, ValueError):
            return False
        return True

    def orthogonal_complement(self):
        r"""Return ``im(self)^perp`` inside the formed codomain."""
        codomain = self.codomain()
        ring = codomain.base_ring()
        if not callable(getattr(codomain, "b", None)):
            raise TypeError("orthogonal complement requires a formed codomain")
        value_module = getattr(codomain, "value_module", None)
        if value_module is not None and value_module() is not ring:
            raise TypeError("this orthogonal-complement construction requires a scalar-valued form")

        from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

        source_generators = tuple(self.domain().module_generators())
        target_labels = finite_ordered_set(range(len(source_generators)))
        target = ring._fresh_free_module_on(target_labels)
        pairing_map = module_homset(codomain, target)(
            {
                label: target.linear_combination(
                    {
                        position: codomain.b(
                            codomain.module_generator(label),
                            self(source_generator),
                        )
                        for position, source_generator in enumerate(source_generators)
                        if codomain.b(
                            codomain.module_generator(label),
                            self(source_generator),
                        )
                        != ring.zero()
                    }
                )
                for label in codomain.module_generating_set()
            }
        )
        return pairing_map.kernel()

    def then(self, other):
        r"""Return ``other ∘ self``."""
        if other.domain() is not self.codomain():
            raise ValueError("the first codomain must equal the second domain")
        return other * self

    def base_change(self, ring_map):
        r"""Extend this represented linear map along ``ring_map : R -> S``."""
        ring = self.domain().base_ring()
        if self.codomain().base_ring() is not ring or ring_map.domain() is not ring:
            raise ValueError("module-morphism base change requires one source scalar ring")
        try:
            source = self.domain().base_change(ring_map)
            target = self.codomain().base_change(ring_map)
        except AttributeError as error:
            raise NotImplementedError(
                "base change of this module morphism requires represented endpoint base changes"
            ) from error

        return module_homset(source, target)(
            {
                label: target.linear_combination(
                    {
                        target_label: ring_map(coefficient)
                        for target_label, coefficient in module_coefficients(
                            self(self.domain().module_generator(label)),
                            self.codomain(),
                        ).items()
                        if coefficient
                    }
                )
                for label in self.domain().module_generating_set()
            }
        )

    def __mul__(self, other):
        if isinstance(other, ModuleMorphism):
            if other.codomain() is not self.domain():
                return NotImplemented
            homset = module_homset(other.domain(), self.codomain())
            # Composition of certified linear maps is linear.  Keep that theorem
            # as construction data instead of rebuilding the composite from all
            # selected generator images and rechecking the source relations.
            return homset.elementwise(
                lambda element: self(other(element)),
                verify_linearity=False,
            )
        try:
            return self.parent().scalar_multiple(other, self)
        except (TypeError, ValueError):
            return NotImplemented

    @cached_method
    def cokernel(self):
        r"""Return the selected quotient ``codomain(self) / image(self)``."""
        quotient = self.codomain()._represented_cokernel_of_morphism(self)
        if quotient is NotImplemented:
            quotient = self.domain()._represented_cokernel_of_morphism(self)
        if quotient is NotImplemented:
            raise NotImplementedError(
                "this cokernel has no represented quotient-module backend"
            )
        projection = module_homset(self.codomain(), quotient)(
            {
                label: quotient.module_generator(label)
                for label in self.codomain().module_generating_set()
            }
        )
        quotient._preamble_cokernel_morphism = self
        quotient._preamble_cokernel_projection = projection
        return quotient


class FramingMorphism(ModuleMorphism):
    r"""A declared surjective linear map from a free framed module."""

    def is_surjective(self) -> bool:
        return True


class ModuleEmbedding(ModuleMorphism):
    r"""A module morphism declared to be a monomorphism."""

    def is_injective(self) -> bool:
        return True

    def factor_through(self, target_embedding):
        r"""Return the unique factor through ``target_embedding`` when it exists.

        For inclusions ``i:A -> X`` and ``j:B -> X`` this constructs the
        commuting-triangle map ``A -> B`` exactly when ``i(A) <= j(B)``.
        """
        if target_embedding.codomain() is not self.codomain():
            raise ValueError("subobject factorization requires one common codomain")
        images = {}
        for label in self.domain().module_generating_set():
            image = self(self.domain().module_generator(label))
            try:
                images[label] = target_embedding.lift(image)
            except (TypeError, ValueError) as error:
                raise ValueError("the first subobject is not contained in the second") from error
        return module_homset(self.domain(), target_embedding.domain())(images)


class _ModuleHomScalarAction(Action):
    r"""The pointwise scalar action of the base ring on a module Hom object."""

    def __init__(self, scalar_parent, homset, is_left) -> None:
        self._homset = homset
        Action.__init__(self, scalar_parent, homset, is_left, operator.mul)

    def _act_(self, scalar, morphism):
        return self._homset.scalar_multiple(scalar, morphism)


def _initialize_module_hom_parent(
    parent,
    hom_family,
    domain,
    codomain,
    *,
    full_internal_hom=False,
) -> None:
    r"""Install the common enriched ``R``-module Hom parent semantics.

    This is implementation reuse only.  Structured Hom categories such as
    ``Hom_{R[G]}`` must not subclass ``Hom_R`` as Python classes merely because
    they have ``Hom_R`` as a categorical supercategory.
    """
    if domain.base_ring() != codomain.base_ring():
        raise ValueError("module morphisms require a common base ring")
    from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring

    parent._preamble_base_ring = _owned_ring(domain.base_ring())
    CategoricalHomset.__init__(
        parent,
        hom_family,
        domain,
        codomain,
    )
    domain.module_category()._refine_hom_parent(
        parent,
        full_internal_hom=full_internal_hom,
    )
    scalar_parent = parent._preamble_base_ring
    parent.register_action(_ModuleHomScalarAction(scalar_parent, parent, True))
    parent.register_action(_ModuleHomScalarAction(scalar_parent, parent, False))


class _ModuleHomsetCommonMethods:
    r"""Python implementation shared by module-enriched Hom parents.

    This is not a mathematical Hom category.  Concrete Hom parents remain
    distinct categories and use this class only to share ordinary module-Hom
    operations.
    """

    def _element_constructor_(self, images):

        if (
            callable(getattr(self, "from_rows", None))
            and isinstance(images, (tuple, list))
            and len(images) == self.nrows()
            and all(isinstance(row, (tuple, list)) for row in images)
        ):
            return self.from_rows(images)
        if isinstance(images, ModuleMorphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the morphism has the wrong Hom source or target")
            if images.parent() is self:
                return images
            if not self.domain().is_framed():
                return self.elementwise(lambda element: images(element))
            images = {
                label: images(self.domain().module_generator(label))
                for label in self.domain().module_generating_set()
            }
        elif isinstance(images, Morphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the morphism has the wrong Hom source or target")
            return self.elementwise(lambda element: images(element))
        model = self.__dict__.get("_preamble_internal_hom_model")
        if model is not None and images in model:
            return self._morphism_from_internal_model(model(images))
        return self.element_class(self, images)

    def base_ring(self):
        return self._preamble_base_ring

    def scalar_multiple(self, scalar, morphism):
        if morphism.parent() is not self:
            morphism = self(morphism)
        scalar = self.base_ring()(scalar)
        return self.elementwise(
            lambda element: self.codomain().scalar_multiple(
                scalar,
                morphism(element),
            ),
            verify_linearity=False,
        )

    def elementwise(self, function, *, verify_linearity=True):
        r"""Construct a declared linear map from its action on arbitrary elements.

        Exact verification is performed when the represented source/scalar
        carriers make it decidable (notably finite carriers).  Otherwise the
        callable is accepted as the defining elementwise realization and a
        DEBUG diagnostic records that its linearity was not mechanically
        certified.  For finitely generated/presented objects, prefer the
        generator-assignment constructor when possible: its linear extension
        is linear by construction and presentation relations are checked.
        """
        if not callable(function):
            raise TypeError("an elementwise module map must be callable")
        return self.element_class(
            self,
            function,
            elementwise=True,
            verify_linearity=verify_linearity,
        )

    def source_module(self):
        return self.domain()

    def target_module(self):
        return self.codomain()

    def evaluation(self, morphism, source_element):
        return self(morphism)(source_element)

    def morphisms_agree(self, left, right) -> bool:
        r"""Decide equality through the module Hom's selected framing data."""
        if left.parent() is not self or right.parent() is not self:
            return False
        return bool(left == right)

    def as_morphism(self, element):
        r"""Compatibility spelling: Hom elements already are morphisms."""
        return self(element)

    def from_morphism(self, morphism):
        r"""Compatibility spelling: the morphism is already a Hom element."""
        return self(morphism)

    def zero(self):
        return self.elementwise(
            lambda _element: self.codomain().zero(),
            verify_linearity=False,
        )

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism homset")
        if not callable(getattr(self.domain(), "module_generating_set", None)):
            return self.elementwise(
                lambda element: element,
                verify_linearity=False,
            )
        labels = self.domain().module_generating_set()
        try:
            from dzack_research.preamble.categories.sets.cardinals import cardinal
            finite = cardinal(labels.cardinality()).is_finite()
        except AttributeError:
            finite = False
        if finite:
            return self(
                {
                    label: self.domain().module_generator(label)
                    for label in labels
                }
            )
        return self.elementwise(
            lambda element: element,
            verify_linearity=False,
        )

    def one(self):
        r"""Return the multiplicative unit when this is an endomorphism ring."""
        return self.identity()



class ModuleHomset(_ModuleHomsetCommonMethods, CategoricalHomset):
    Element = ModuleMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        _initialize_module_hom_parent(
            self,
            hom_family,
            domain,
            codomain,
            full_internal_hom=True,
        )

    def __call__(self, images):
        r"""Construct a module morphism without Sage coercion discovery."""
        return self._element_constructor_(images)










    def internal_hom_model(self):
        model = self.__dict__.get("_preamble_internal_hom_model")
        if model is None:
            raise NotImplementedError("this Hom module has no computed finite presentation")
        return model

    def inclusion_into_generator_maps(self):
        inclusion = self.__dict__.get("_preamble_internal_hom_inclusion")
        if inclusion is None:
            raise NotImplementedError("this Hom module has no computed generator-assignment inclusion")
        return inclusion

    def _morphism_from_internal_model(self, model_element):
        assignment_space = self.inclusion_into_generator_maps().codomain()
        assignment = self.inclusion_into_generator_maps()(model_element)
        coefficients = module_coefficients(assignment, assignment_space)
        assignment_labels = assignment_space.module_generating_set()
        return self(
            {
                source_label: self.codomain().linear_combination(
                    {
                        target_label: coefficients[pair]
                        for target_label in self.codomain().module_generating_set()
                        if (
                            pair := assignment_labels(
                                lambda index: source_label
                                if int(index) == 0
                                else target_label
                            )
                        ) in coefficients
                    }
                )
                for source_label in self.domain().module_generating_set()
            }
        )

    def _internal_model_from_morphism(self, morphism):
        model = self.internal_hom_model()
        power = self.inclusion_into_generator_maps().codomain()
        power_labels = power.module_generating_set()
        coefficients = {}
        for source_label in self.domain().module_generating_set():
            image = morphism(self.domain().module_generator(source_label))
            for target_label, coefficient in module_coefficients(
                image,
                self.codomain(),
            ).items():
                coefficients[
                    power_labels(
                        lambda index: source_label
                        if int(index) == 0
                        else target_label
                    )
                ] = coefficient
        assignment = power.linear_combination(coefficients)
        inclusion = self.inclusion_into_generator_maps()
        custom_lift = inclusion.__dict__.get("_preamble_lift")
        if custom_lift is not None:
            return inclusion.lift(assignment)
        return model(assignment)


    def linear_combination(self, coefficients):
        result = self.zero()
        for label, coefficient in coefficients.items():
            if coefficient:
                result = result + self.scalar_multiple(
                    coefficient,
                    self.module_generator(label),
                )
        return result



    def _repr_(self):
        return f"Hom({self.domain()}, {self.codomain()})"


def module_homset(domain, codomain) -> ModuleHomset:
    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError("module morphisms require a common base ring")
    if codomain.module_category() is not domain.module_category():
        raise ValueError("module morphisms require one owned module category")
    return domain.module_category().Hom(domain, codomain)


def framing_morphism(domain, codomain, images) -> FramingMorphism:
    homset = module_homset(domain, codomain)
    framing = FramingMorphism(homset, images)
    return framing


def module_embedding(
    domain,
    codomain,
    images,
    *,
    verify_linearity=True,
) -> ModuleEmbedding:
    r"""Construct a declared module monomorphism on a chosen framing."""
    return ModuleEmbedding(
        module_homset(domain, codomain),
        images,
        verify_linearity=verify_linearity,
    )



class TensorProductModuleMorphism(ModuleMorphism):
    r"""A linear map out of a chosen tensor product, hence a bilinear map."""

    def left_module(self):
        return self.domain().tensor_factor(0)

    def right_module(self):
        return self.domain().tensor_factor(1)

    def module(self):
        if self.left_module() is not self.right_module():
            raise TypeError("a pairing of distinct modules is not a bilinear form on one module")
        return self.left_module()

    def __call__(self, *arguments):
        if len(arguments) == 1:
            return self._call_(arguments[0])
        if len(arguments) == 2:
            return self._call_(self.domain().pure_tensor(*arguments))
        raise TypeError("a tensor-product morphism takes one tensor or two factor elements")

    def coordinate_values(self):
        from dzack_research.preamble.categories.sets.indexed_families import indexed_family

        labels = self.domain().module_generating_set()
        return indexed_family(
            labels,
            lambda pair: self(
                self.left_module().module_generator(pair.component(0)),
                self.right_module().module_generator(pair.component(1)),
            ),
            name="Bilinear coordinate values",
        )

    def _gram_entry(self, left_label, right_label):
        return self(
            self.left_module().module_generator(left_label),
            self.right_module().module_generator(right_label),
        )

    def norm(self, element):
        if self.left_module() is not self.right_module():
            raise TypeError("a norm requires a diagonal bilinear form")
        return self(element, element)

    def pullback(self, morphism):
        if self.left_module() is not self.right_module():
            raise TypeError("this pullback syntax is for a diagonal bilinear form")
        if morphism.codomain() is not self.left_module():
            raise ValueError("the pullback map must land in the form's module")
        from dzack_research.preamble.categories.abstract_categories.constructions import TensorProduct

        source = TensorProduct(morphism.domain(), morphism.domain())
        induced = module_homset(source, self.domain())(
            lambda pair: self.domain().pure_tensor(
                morphism(
                    morphism.domain().module_generator(pair.component(0))
                ),
                morphism(
                    morphism.domain().module_generator(pair.component(1))
                ),
            )
        )
        return module_homset(source, self.codomain())(self * induced)

    def polar_form(self):
        if self.left_module() is not self.right_module():
            raise TypeError("polar form syntax requires a diagonal bilinear form")
        return self.parent().scalar_multiple(self.domain().base_ring()(2), self)



class TensorProductModuleHomset(ModuleHomset):
    r"""The ordinary module Hom with tensor-domain bilinear constructor syntax."""

    Element = TensorProductModuleMorphism

    @staticmethod
    def _is_two_argument_callable(function) -> bool:
        if not callable(function):
            return False
        try:
            from inspect import signature

            parameters = signature(function)
            parameters.bind(None, None)
        except (TypeError, ValueError):
            return False
        try:
            parameters.bind(None)
        except TypeError:
            return True
        return False

    def _element_constructor_(self, images):
        left = self.domain().tensor_factor(0)
        right = self.domain().tensor_factor(1)
        left_labels = left.module_generating_set()
        right_labels = right.module_generating_set()

        from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily

        if isinstance(images, IndexedFamily):
            source_indices = images.index_set()
            raw_family = images

            def generator_image(pair):
                source_pair = source_indices(
                    lambda index: pair.component(index)
                )
                value = raw_family[source_pair]
                return value if getattr(value, "parent", lambda: None)() is self.codomain() else self.codomain()(value)

            images = generator_image
        elif self._is_two_argument_callable(images):
            raw = images

            def generator_image(pair):
                value = raw(
                    left.module_generator(pair.component(0)),
                    right.module_generator(pair.component(1)),
                )
                return value if getattr(value, "parent", lambda: None)() is self.codomain() else self.codomain()(value)

            images = generator_image
        elif (
            isinstance(images, (tuple, list))
            and all(isinstance(row, (tuple, list)) for row in images)
        ):
            from dzack_research.preamble.categories.sets.cardinals import cardinal

            left_size = cardinal(left_labels.cardinality())
            right_size = cardinal(right_labels.cardinality())
            if not left_size.is_finite() or not right_size.is_finite():
                raise TypeError("coordinate-array pairing syntax requires finite framings")
            if len(images) != int(left_size.finite_value()) or any(
                len(row) != int(right_size.finite_value()) for row in images
            ):
                raise ValueError("the pairing coordinate array has the wrong shape")
            by_position = {
                (i, j): images[i][j]
                for i in range(len(images))
                for j in range(len(images[i]))
            }

            def generator_image(pair):
                value = by_position[
                    int(left_labels.rank(pair.component(0))),
                    int(right_labels.rank(pair.component(1))),
                ]
                return value if getattr(value, "parent", lambda: None)() is self.codomain() else self.codomain()(value)

            images = generator_image

        return super()._element_constructor_(images)
