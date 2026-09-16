"""Linear maps between represented modules."""

import logging
from functools import reduce
from itertools import product

from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_attribute import lazy_attribute
from sage.structure.element import parent as element_parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoricalIsomorphism,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalRings,
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    EnumeratedSets,
    Sets,
)

_LOGGER = logging.getLogger(__name__)


class ModuleCompletionMorphismConstruction(SageObject):
    r"""The selected source morphism and completion defining a completed map."""

    def __init__(self, source_morphism, completion) -> None:
        self._source_morphism = source_morphism
        self._completion = completion

    def source_morphism(self):
        return self._source_morphism

    def completion(self):
        return self._completion

    def image_of(self, image):
        r"""Return ``image`` with this completion construction established at birth."""
        if not isinstance(image, ModuleMorphism):
            raise TypeError("a completed module-morphism construction produces a module morphism")
        parent = image.parent()
        source = image.domain()
        if source.is_framed_module():
            return parent.element_class(
                parent,
                lambda label: image(source.module_generator(label)),
                completion_construction=self,
            )
        return parent.element_class(
            parent,
            lambda element: image(element),
            elementwise=True,
            verify_linearity=False,
            completion_construction=self,
        )


class ModuleLocalizationMorphismConstruction(SageObject):
    r"""The selected source morphism and localization functor defining a localized map."""

    def __init__(self, source_morphism, localization_functor) -> None:
        self._source_morphism = source_morphism
        self._localization_functor = localization_functor

    def source_morphism(self):
        return self._source_morphism

    def localization_functor(self):
        return self._localization_functor

    def image_of(self, image):
        r"""Return ``image`` with this localization construction established at birth."""
        if not isinstance(image, ModuleMorphism):
            raise TypeError("a localized module-morphism construction produces a module morphism")
        existing = image.localization_construction()
        if existing is self:
            return image
        if existing is not None:
            if (
                existing.source_morphism() is not self.source_morphism()
                or existing.localization_functor() is not self.localization_functor()
            ):
                raise ValueError(
                    "this morphism already carries a different localization construction"
                )
            return image
        parent = image.parent()
        source = image.domain()
        if source.is_framed_module():
            return parent.element_class(
                parent,
                lambda label: image(source.module_generator(label)),
                localization_construction=self,
            )
        return parent.element_class(
            parent,
            lambda element: image(element),
            elementwise=True,
            verify_linearity=False,
            localization_construction=self,
        )


class ModuleCokernelCompletionComparison(SageObject):
    r"""The finite-module comparison ``coker(f)^ ~= coker(f^)``."""

    def __init__(
        self,
        source_morphism,
        completion,
        completed_morphism,
        completed_cokernel,
        cokernel_after_completion,
        forward,
        inverse,
    ) -> None:
        self._source_morphism = source_morphism
        self._completion = completion
        self._completed_morphism = completed_morphism
        self._completed_cokernel = completed_cokernel
        self._cokernel_after_completion = cokernel_after_completion
        self._forward = forward
        self._inverse = inverse

    def source_morphism(self):
        return self._source_morphism

    def completion_ring(self):
        return self._completion

    def completed_morphism(self):
        return self._completed_morphism

    def completed_cokernel(self):
        return self._completed_cokernel

    def cokernel_after_completion(self):
        return self._cokernel_after_completion

    def forward(self):
        return self._forward

    isomorphism = forward

    def inverse(self):
        return self._inverse

    def _repr_(self):
        return f"Completion of coker({self.source_morphism()}) ~= coker({self.completed_morphism()})"


def _has_finite_free_framing(module) -> bool:
    r"""Return whether ``module`` represents a finite free module with framing."""
    if not bool(getattr(module, "is_free", lambda: False)()):
        return False
    labels = getattr(module, "module_generating_set", lambda: None)()
    if labels is None:
        return False

    return labels.cardinality().is_finite()


def _integral_left_solver(system, ring):
    r"""Factor one integral system once and return its exact row solver."""

    from dzack_research.preamble.categories.modules.pure.modules import MatrixSpaces

    assert ring in OwnedRings(), "integral solving requires an owned coefficient ring"
    assert system.parent() in MatrixSpaces(ring), f"an integral linear system over {ring} is an element of a matrix homset over it, and {system.parent()} is not one"

    transposed = system.transpose()
    smith, left, right = transposed.smith_form()
    target_labels = left.domain().module_generating_set()
    shifted_labels = left.codomain().module_generating_set()
    width = int(smith.domain().module_generating_set().cardinality())

    def solve(target):
        target_values = tuple(ring(value) for value in target)
        if len(target_values) != int(target_labels.cardinality()):
            raise ValueError("the target has the wrong length for this linear system")
        target_vector = left.domain().linear_combination({label: target_values[position] for position, label in enumerate(target_labels) if target_values[position]})
        shifted_vector = left(target_vector)
        shifted_coefficients = left.codomain().framing_coefficients(shifted_vector)

        solution = [ring.zero()] * width
        for index, shifted_label in enumerate(shifted_labels):
            value = shifted_coefficients.get(shifted_label, ring.zero())
            divisor = smith[index, index] if index < min(int(shifted_labels.cardinality()), width) else ring.zero()
            if divisor == 0:
                if value != 0:
                    raise ValueError("the element is not in the image of this morphism")
                continue
            quotient, remainder = value.quo_rem(divisor)
            if remainder != 0:
                raise ValueError("the element is not in the image over the base ring")
            solution[index] = quotient

        normalized_solution = right.domain().linear_combination(
            {label: solution[position] for position, label in enumerate(right.domain().module_generating_set()) if solution[position]}
        )
        return right(normalized_solution)

    return solve


def _solve_left_integrally_element(system, target, ring):
    r"""Return the row-coefficient element ``a`` with ``a*system = target``."""

    return _integral_left_solver(system, ring)(target)


def _solve_left_integrally(system, target, ring):
    r"""Return positional coefficients ``a`` with ``a*system = target`` over a PID."""
    original_solution = _solve_left_integrally_element(system, target, ring)
    coefficients = original_solution.parent().framing_coefficients(original_solution)
    return tuple(coefficients.get(label, ring.zero()) for label in original_solution.parent().module_generating_set())


def _enumerated_ring_elements(ring):
    r"""Return every element of a finite enumerable ring, or ``None``."""
    engine = _engine_ring(ring)
    try:
        if not bool(engine.is_finite()):
            return None
        return tuple(ring._from_engine_element(engine(scalar)) for scalar in engine)
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        return None


def _scalar_linearity_generating_scalars(ring):
    r"""Return scalars whose linearity decides linearity over all of ``ring``.

    Let ``f`` be additive.  The scalars ``r`` with ``f(rx)=rf(x)`` for every
    ``x`` contain ``1`` and are closed under sums, negatives and products, so
    they form a subring of ``R``.  Checking a generating set of ``R`` as a ring
    therefore decides scalar-linearity over the whole of ``R``, and additivity
    already supplies the image of ``ZZ``.

    A finite ring is its own generating set.  A framed algebra over a finite
    ring is generated by that ring together with its chosen algebra generators,
    which is what decides an infinite ring such as ``GF(q)[x]``.  Returns
    ``None`` where neither presentation is represented.
    """
    from dzack_research.preamble.categories.algebras.algebras import FramedAlgebras

    elements = _enumerated_ring_elements(ring)
    if elements is not None:
        return elements

    base = ring.base_ring()
    if base is ring or ring not in FramedAlgebras(base):
        return None
    base_elements = _enumerated_ring_elements(base)
    if base_elements is None:
        return None
    labels = ring.algebra_generating_set()
    if not labels.cardinality().is_finite():
        return None
    return tuple(ring(scalar) for scalar in base_elements) + tuple(ring.algebra_generator(label) for label in labels)


class ModuleMorphism(Morphism):
    r"""The linear extension of a function on a chosen module framing."""

    _localization_construction = None
    _completion_construction = None
    _lift_function = None

    def __init__(
        self,
        parent,
        images,
        *,
        elementwise=False,
        verify_linearity=True,
        localization_construction=None,
        completion_construction=None,
        lift=None,
    ) -> None:
        Morphism.__init__(self, parent)
        self._localization_construction = localization_construction
        self._completion_construction = completion_construction
        self._lift_function = lift
        self._element_function = None
        framed_domain = bool(self.domain().is_framed_module())
        if elementwise or not framed_domain:
            if not callable(images):
                raise TypeError("a morphism from an unframed module must be supplied as an exact element map")
            self._element_function = images
            self._generator_image = None
            self._generator_morphism = None
            if verify_linearity:
                self._verify_elementwise_linearity_when_decidable()
            return
        labels = self.domain().module_generating_set()
        set_homset = Sets().Mor(labels, self.codomain())
        if isinstance(images, SetMorphism):
            if images.domain() is not labels or images.codomain() is not self.codomain():
                raise ValueError("the generator map has the wrong framing or codomain")
            self._generator_images = indexed_family(
                labels,
                images,
                name="Generator images",
            )
            self._generator_image = self._generator_images.value
            self._generator_morphism = images
        elif isinstance(images, IndexedFamily):
            source_indices = images.index_set()

            def image_at(label):
                return images[source_indices(label)]

            self._generator_images = indexed_family(
                labels,
                image_at,
                name="Generator images",
            )
            self._generator_image = self._generator_images.value
            self._generator_morphism = set_homset(self._generator_image)
        elif isinstance(images, dict):
            size = labels.cardinality()
            if not size.is_finite():
                raise TypeError("dictionary generator-image syntax requires a finite framing; use a callable or indexed family for an infinite framing")
            if labels in EnumeratedSets():
                ranking = labels.ranking_map()
                missing_value = object()
                normalized_values = [missing_value] * int(size.finite_value())
                for label, value in images.items():
                    normalized_label = labels(label)
                    normalized_values[int(ranking(normalized_label))] = value
                missing = [
                    label
                    for position, label in enumerate(labels)
                    if normalized_values[position] is missing_value
                ]
                if missing:
                    raise ValueError(f"generator assignment omits {missing}")
                self._generator_images = indexed_family(
                    labels,
                    lambda label: normalized_values[int(ranking(label))],
                    name="Generator images",
                )
            else:
                normalized_images = {}
                for label, value in images.items():
                    normalized_label = labels(label)
                    normalized_images[normalized_label] = value
                missing = [label for label in labels if label not in normalized_images]
                if missing:
                    raise ValueError(f"generator assignment omits {missing}")
                self._generator_images = indexed_family(
                    labels,
                    normalized_images.__getitem__,
                    name="Generator images",
                )
            self._generator_image = self._generator_images.value
            self._generator_morphism = set_homset(self._generator_image)
        elif isinstance(images, (tuple, list)):
            values = tuple(images)
            size = labels.cardinality()
            if not size.is_finite():
                raise TypeError("sequence generator-image syntax requires a finite framing; use a callable or indexed family for an infinite framing")
            if len(values) != int(size.finite_value()):
                raise ValueError("the number of generator images must equal the framing size")
            if labels not in EnumeratedSets():
                raise TypeError("sequence generator-image syntax requires a ranked framing")
            self._generator_images = indexed_family(
                labels,
                lambda label: values[int(labels.ranking_map()(label))],
                name="Generator images",
            )
            self._generator_image = self._generator_images.value
            self._generator_morphism = set_homset(self._generator_image)
        elif callable(images):
            self._generator_images = indexed_family(
                labels,
                images,
                name="Generator images",
            )
            self._generator_image = self._generator_images.value
            self._generator_morphism = set_homset(self._generator_image)
        else:
            raise TypeError("a module morphism is specified on the domain framing")
        self._check_selected_domain_relations()

    def _verify_elementwise_linearity_when_decidable(self) -> None:
        r"""Check an elementwise callable exactly in represented decidable regimes.

        A Python callable does not carry a proof of linearity.  When the source
        module is finite and enumerable, additivity is decidable by exhaustive
        verification, and the scalars an additive map commutes with form a
        subring, so a ring generating set decides scalar-linearity over all of
        ``R``.  Over ``ZZ`` that generating set is empty: every additive-group
        map is automatically ``ZZ``-linear.  Outside such regimes the callable
        is a declared linear map; a DEBUG diagnostic records that no exhaustive
        verification was available.

        A map given by images of a framing is not reached here at all.  Its
        linear extension is linear by construction, and the relations of the
        chosen presentation are what has to be checked instead.
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
                "Elementwise module morphism %s -> %s accepted without exhaustive linearity verification; the source is not represented as finite",
                domain,
                codomain,
            )
            return

        try:
            source_elements = tuple(domain)
        except (AttributeError, TypeError):
            self._check_elementwise_zero_when_possible()
            _LOGGER.debug(
                "Elementwise module morphism %s -> %s accepted without exhaustive linearity verification; finite source has no represented enumeration",
                domain,
                codomain,
            )
            return

        self._verify_elementwise_on_finite_source(source_elements)

    def _finite_source_elements_for_verification(self):
        r"""Enumerate a finitely generated module over a finite ring via its framing."""
        domain = self.domain()
        ring = domain.base_ring()

        generating_set = getattr(domain, "module_generating_set", None)
        if not callable(generating_set):
            return None
        try:
            label_set = generating_set()

            if not label_set.cardinality().is_finite():
                return None
            labels = tuple(label_set)
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return None
        if not labels:
            return (domain.zero(),)
        scalars = _enumerated_ring_elements(ring)
        if scalars is None:
            return None
        elements = []
        seen = set()
        for coefficients in product(scalars, repeat=len(labels)):
            element = domain.linear_combination({label: coefficient for label, coefficient in zip(labels, coefficients, strict=True) if coefficient != 0})
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

        def evaluate(element):
            try:
                return function(element)
            except (TypeError, ValueError) as error:
                raise ValueError("the supplied elementwise map is not additive on the represented module") from error

        if evaluate(zero) != codomain.zero():
            raise ValueError("an elementwise module morphism must send zero to zero")
        for left in source_elements:
            for right in source_elements:
                if evaluate(left + right) != evaluate(left) + evaluate(right):
                    raise ValueError("the supplied elementwise map is not additive")

        from sage.rings.integer_ring import ZZ as SageZZ

        if _engine_ring(ring) is SageZZ:
            return

        scalars = _scalar_linearity_generating_scalars(ring)
        if scalars is None:
            _LOGGER.debug(
                "Elementwise map %s -> %s is exhaustively additive on its finite source, "
                "but %s has no represented ring generating set, so scalar-linearity was "
                "not exhaustively verified",
                domain,
                codomain,
                ring,
            )
            return
        for scalar in scalars:
            for element in source_elements:
                if evaluate(domain.scalar_multiple(scalar, element)) != codomain.scalar_multiple(scalar, evaluate(element)):
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
            relation_image = self._linear_combination_of_generator_images({label: coefficient for label, coefficient in zip(labels, row, strict=True) if coefficient})
            if relation_image != zero:
                raise ValueError("the selected module-generator images do not kill the domain relations")

    def module_generator_morphism(self):
        assert self._generator_morphism is not None, (
            "module_generator_morphism requires a selected module generating map on the domain"
        )
        return self._generator_morphism

    def module_generator_images(self):
        assert self._generator_morphism is not None and self._generator_images is not None, (
            "module_generator_images requires a selected module generating map on the domain"
        )
        return self._generator_images

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

    def _richcmp_(self, other, op):
        r"""Decide equality from the source's chosen finite presentation.

        Two linear maps agree exactly when they agree on a generating set, so
        this is decidable when the source carries a chosen finite presentation
        and not otherwise.
        """
        from sage.structure.richcmp import op_EQ, op_NE

        if op not in (op_EQ, op_NE):
            return NotImplemented
        if not isinstance(other, ModuleMorphism) or other.parent() is not self.parent():
            return op == op_NE
        if self is other:
            return op == op_EQ
        from sage.misc.unknown import Unknown

        domain = self.domain()
        if domain._selected_presentation_rows() is None:
            return Unknown
        equal = all(self(domain.module_generator(label)) == other(domain.module_generator(label)) for label in domain.module_generating_set())
        return equal if op == op_EQ else (Unknown if equal is Unknown else not equal)

    def __rmul__(self, actor):
        # A specialized right operand such as ModuleEmbedding gets reflected
        # multiplication before Python tries the less-specialized left
        # ModuleMorphism.__mul__.  In that case the operation is composition,
        # not scalar multiplication.  Delegate to the left morphism so the
        # ordinary endpoint check and composition constructor remain the one
        # owner of the operation.
        from dzack_research.preamble.categories.modules.pure.modules import (
            LinearHomModules,
        )

        match element_parent(actor) in LinearHomModules(self.domain().base_ring()):
            case True:
                return actor.__mul__(self)
            case False:
                return self.parent().scalar_multiple(actor, self)

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
        coefficients = self.domain().framing_coefficients(element)
        return self._linear_combination_of_generator_images(coefficients)

    def matrix(self):
        r"""Return the canonical coordinate matrix of this finite free map.

        Coordinates live in the canonical matrix Hom
        ``Hom_R(F_R([n]), F_R([m]))``.  A map whose endpoints already are
        those canonical free modules is literally that matrix element; an
        arbitrary framed map is transported only at this coordinate-view
        boundary.
        """

        assert _has_finite_free_framing(self.domain()) and _has_finite_free_framing(self.codomain()), (
            "a coordinate matrix requires finitely generated framed free endpoints"
        )
        domain_labels = tuple(self.domain().module_generating_set())
        codomain_labels = tuple(self.codomain().module_generating_set())
        coordinate_parent = self.domain().base_ring().matrix_space(len(codomain_labels), len(domain_labels))
        if self.parent() is coordinate_parent:
            return self
        columns = {
            domain_label: self.codomain().framing_coefficients(self(self.domain().module_generator(domain_label)))
            for domain_label in domain_labels
        }
        zero = self.codomain().base_ring().zero()
        return coordinate_parent.from_rows(
            tuple(
                tuple(
                    columns[domain_label].get(codomain_label, zero)
                    for domain_label in domain_labels
                )
                for codomain_label in codomain_labels
            )
        )

    def alternating_extension(self):
        r"""Extend this linear map through the exterior-algebra universal property."""
        from dzack_research.preamble.categories.algebras.power_algebras import (
            _alternating_extension,
        )

        return _alternating_extension(self)

    def tensor_product_map(self, other, *, source=None, target=None):
        r"""Return the induced map ``self tensor other`` on selected tensor products."""
        from dzack_research.preamble.categories.modules.tensor_products import (
            _tensor_product_morphism,
        )

        return _tensor_product_morphism(
            self,
            other,
            source=source,
            target=target,
        )

    def biproduct_map(self, other, *, source=None, target=None):
        r"""Return the induced map ``self direct-sum other`` on selected biproducts."""
        from dzack_research.preamble.categories.modules.pure.modules import (
            _biproduct_morphism,
        )

        return _biproduct_morphism(
            self,
            other,
            source=source,
            target=target,
        )

    def internal_hom_map(
        self,
        target_map,
        *,
        source_internal_hom=None,
        target_internal_hom=None,
    ):
        r"""Return the internal-Hom map induced by pre- and postcomposition."""
        from dzack_research.preamble.categories.modules.internal_hom import (
            _internal_hom_morphism,
        )

        return _internal_hom_morphism(
            self,
            target_map,
            source_internal_hom=source_internal_hom,
            target_internal_hom=target_internal_hom,
        )

    def stack(self, other):
        r"""Return ``(self,other)`` into the biproduct of the codomains."""
        if not isinstance(other, ModuleMorphism) or other.domain() is not self.domain():
            raise ValueError("stacking module maps requires one common domain")

        from dzack_research.preamble.categories.modules.pure.modules import Modules

        target = Modules(self.codomain().base_ring()).biproduct(
            (self.codomain(), other.codomain())
        )
        return target.to_product(self, other)

    def localization_construction(self):
        r"""Return the selected localization datum defining this transported map."""
        return self._localization_construction

    def completion_construction(self):
        r"""Return the selected completion datum defining this transported map, if any."""
        return self._completion_construction

    @cached_method
    def kernel(self):
        r"""Return ``ker(self)`` as a subobject of the domain."""
        completion_datum = self.completion_construction()
        if completion_datum is not None:
            completion_source = completion_datum.source_morphism()
            completion = completion_datum.completion()
            if not completion.is_flat_over_source():
                raise ArithmeticError("the retained completion map was expected to be flat over its Noetherian source")
            from dzack_research.preamble.categories.modules.pure.modules import Modules

            source_kernel = completion_source.kernel()
            extension = Modules(completion_source.domain().base_ring()).scalar_extension(completion.completion_map())
            if extension(completion_source.domain()) is not self.domain():
                raise ArithmeticError(
                    "the completed morphism domain is not the retained scalar-extension image of its source"
                )
            extension(source_kernel)
            completed_inclusion = extension(source_kernel.inclusion())
            if completed_inclusion.codomain() is not self.domain():
                raise ArithmeticError("the completed source-kernel inclusion has the wrong ambient module")
            return completed_inclusion.image()

        localization_construction = self.localization_construction()
        if localization_construction is not None:
            from dzack_research.preamble.categories.modules.pure.modules import (
                ModuleSubobjects,
            )

            source_morphism = localization_construction.source_morphism()
            localization_functor = localization_construction.localization_functor()
            source_kernel = source_morphism.kernel()
            localized_kernel = localization_functor(source_kernel)
            localized_inclusion = localization_functor(source_kernel.inclusion())
            if localized_inclusion.codomain() is not self.domain():
                raise ArithmeticError("localized kernel inclusion does not land in the cached localized domain")
            if localized_kernel not in ModuleSubobjects(self.domain().base_ring()):
                raise ArithmeticError("localization did not preserve the represented source-kernel subobject")
            if localized_kernel.inclusion() is not localized_inclusion:
                raise ArithmeticError("localized kernel inclusion is not the inclusion carried by the transported subobject")
            return localized_kernel

        ring = self.domain().base_ring()
        if ring in LocalRings():
            from dzack_research.preamble.categories.modules.localizations import (
                LocalizedModules,
            )

            domain = self.domain()
            codomain = self.codomain()
            if domain in LocalizedModules(ring) and codomain in LocalizedModules(ring):
                functor = domain.localization_functor()
                if codomain.localization_functor() is functor:
                    source_domain = domain.localization_source_module()
                    source_codomain = codomain.localization_source_module()
                    labels = tuple(source_domain.module_generating_set())
                    images = tuple(self(domain.module_generator(label)) for label in labels)
                    denominators = tuple(image.denominator() for image in images)

                    source_images = {}
                    for position, (label, image) in enumerate(zip(labels, images, strict=True)):
                        multiplier = source_domain.base_ring().one()
                        for other_position, denominator in enumerate(denominators):
                            if other_position != position:
                                multiplier *= denominator
                        source_images[label] = source_codomain.scalar_multiple(
                            multiplier,
                            image.numerator(),
                        )

                    source_morphism = source_domain.module_category().Mor(source_domain, source_codomain)(source_images)
                    source_kernel = source_morphism.kernel()
                    localized_kernel = functor(source_kernel)
                    localized_inclusion = functor(source_kernel.inclusion())
                    if localized_inclusion.codomain() is not domain:
                        raise ArithmeticError("the descended local kernel inclusion does not return to the direct local domain")
                    return localized_kernel

        represented = NotImplemented
        for owner in (self.domain(), self.codomain()):
            represented = owner._represented_kernel_of_morphism(self)
            if represented is not NotImplemented:
                return represented
        assert represented is not NotImplemented, (
            "kernel construction requires a represented finite-free or general polynomial-presentation backend"
        )
        return represented

    def subobject_image_adjunction(self):
        r"""Return ``f_* ⊣ f^{-1}`` on fixed-ambient module subobjects."""
        from dzack_research.preamble.categories.functors.subobject_images import (
            _SubobjectImageAdjunction,
        )

        return _SubobjectImageAdjunction(self)

    def image(self):
        r"""Return ``im(self)`` as a subobject of the codomain."""
        labels = self.domain().module_generating_set()
        assert labels.cardinality().is_finite(), (
            "the represented image-subobject backend requires a finite domain framing"
        )
        return self.codomain().subobject_on(
            finite_indexed_family(
                labels,
                lambda label: self(self.domain().module_generator(label)),
                name="Image spanning family",
            )
        )

    def preimage(self, element):
        r"""Return one preimage of ``element`` when it lies in the represented image.

        Resolution lifting repeatedly needs a preimage under a map whose
        domain is finite free.  If the map is onto its free codomain, use the
        existing projective section.  Otherwise the represented image is
        generated by the images of the domain's selected generators, with the
        same labels; lifting into that image therefore gives coefficients that
        reconstruct a preimage in the original domain.
        """
        domain = self.domain()
        codomain = self.codomain()
        element = element if element.parent() is codomain else codomain(element)
        if element == codomain.zero():
            return domain.zero()
        if not _has_finite_free_framing(domain):
            elements = getattr(domain, "elements", None)
            assert callable(elements) and domain.cardinality().is_finite(), (
                "represented preimages require a finitely framed free domain or an enumerable finite domain"
            )
            for candidate in elements():
                if self(candidate) == element:
                    return candidate
            raise ValueError("the selected element does not lie in the represented image")
        if self.is_surjective() and bool(getattr(codomain, "is_free", lambda: False)()):
            return self.section()(element)

        image = self.image()
        image_element = image.inclusion().lift(element)
        coefficients = image.framing_coefficients(image_element)
        domain_labels = domain.module_generating_set()
        if any(label not in domain_labels for label in coefficients):
            raise ArithmeticError("the represented image framing no longer records the source-generator labels")
        return domain.linear_combination({label: coefficient for label, coefficient in coefficients.items() if coefficient})

    def is_injective(self) -> bool:
        r"""Return whether ``ker(self)=0`` when the kernel is computable."""
        return self.kernel().is_zero()

    def is_surjective(self) -> bool:
        r"""Return whether ``coker(self)=0`` when the cokernel is computable."""
        return self.cokernel().is_zero()

    def residue_morphism(self):
        r"""Return ``f tensor_R k`` for a morphism of finite modules over a local ring."""

        ring = self.domain().base_ring()
        if self.codomain().base_ring() is not ring:
            raise ValueError("a residue morphism requires one common base ring")
        if ring not in LocalRings():
            raise TypeError("reduction modulo the maximal ideal requires a represented local ring")
        if not self.domain().is_finitely_generated() or not self.codomain().is_finitely_generated():
            raise TypeError("the active Nakayama interface requires finitely generated source and target")
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
        custom = self._lift_function
        if custom is not None:
            return custom(element)
        ring = self.domain().base_ring()
        assert _has_finite_free_framing(self.domain()), f"a lift is solved for the coefficients of a framing, and {self.domain()} has none"
        if not _has_finite_free_framing(self.codomain()):
            return self._lift_through_the_extension_framing(element)
        if element.parent() is not self.codomain():
            element = self.codomain()(element)
        codomain_labels = tuple(self.codomain().module_generating_set())
        coefficients = self.codomain().framing_coefficients(element)
        target = [coefficients[label] if label in coefficients else self.codomain().base_ring().zero() for label in codomain_labels]
        solution = _solve_left_integrally(
            self.matrix().transpose(),
            target,
            ring,
        )
        return self.domain().linear_combination({label: coefficient for label, coefficient in zip(self.domain().module_generating_set(), solution, strict=True) if coefficient})

    def has_selected_lift(self) -> bool:
        r"""Return whether construction supplied an exact lift through this map."""
        return self._lift_function is not None

    def factor_through(self, target_embedding):
        r"""Return the unique factor through a represented module embedding.

        For ``f:A -> X`` and a monomorphism ``j:B -> X`` this constructs the
        commuting-triangle map ``A -> B`` exactly when every selected generator
        image of ``f`` lies in ``j(B)``.  The source map need not itself be a
        monomorphism; uniqueness comes from ``j``.
        """
        if target_embedding.codomain() is not self.codomain():
            raise ValueError("module factorization through a subobject requires one common codomain")
        source = self.domain()
        target = target_embedding.domain()
        images = {}
        for label in source.module_generating_set():
            image = self(source.module_generator(label))
            try:
                images[label] = (
                    target_embedding.lift(image)
                    if _has_finite_free_framing(target_embedding.domain())
                    else target_embedding.preimage(image)
                )
            except (TypeError, ValueError) as error:
                raise ValueError("the morphism image is not contained in the target subobject") from error
        return source.module_category().Mor(source, target)(images)

    @cached_method
    def selected_presentation_morphism(self):
        r"""Lift this map to a commuting square of selected presentations.

        For ``f : M -> N`` with selected presentations ``p : F_1 -> F_0``
        and ``q : G_1 -> G_0``, first lift each image of a selected generator of
        ``M`` to the chosen free cover ``G_0``.  This gives ``b : F_0 -> G_0``
        with ``pi_N b = f pi_M``.  Consequently ``b p`` lands in ``ker(pi_N)``;
        the selected presentation identifies that kernel with ``im(q)``, so
        lifting the images of the relation generators through ``q`` gives
        ``a : F_1 -> G_1`` and the commuting square ``q a = b p``.
        """
        from dzack_research.preamble.categories.modules.pure.modules import (
            ModulesWithChosenFinitePresentation,
        )

        source = self.domain()
        target = self.codomain()
        ring = source.base_ring()
        if source not in ModulesWithChosenFinitePresentation(ring) or target not in ModulesWithChosenFinitePresentation(ring):
            raise TypeError("a selected-presentation morphism requires presented source and target")

        source_presentation = source.presentation()
        target_presentation = target.presentation()
        source_cover = source_presentation.codomain()
        target_cover = target_presentation.codomain()

        def lift_target(element):
            coordinates = target._framing_coordinates(element)
            return target_cover.linear_combination({label: coordinates[label] for label in target.module_generating_set() if coordinates[label]})

        cover_map = source_cover.module_category().Mor(source_cover, target_cover)({label: lift_target(self(source.module_generator(label))) for label in source_cover.module_generating_set()})
        relation_source = source_presentation.domain()
        relation_target = target_presentation.domain()
        relation_map = relation_source.module_category().Mor(relation_source, relation_target)(
            {
                label: target_presentation.lift(cover_map(source_presentation(source_presentation.domain().module_generator(label))))
                for label in source_presentation.domain().module_generating_set()
            }
        )

        category = ModulesWithChosenFinitePresentation(ring).presentation_category()
        return category.Mor(source.presentation_object(), target.presentation_object())(
            relation_map,
            cover_map,
        )

    def _lift_through_the_extension_framing(self, element):
        r"""Return the preimage of ``element`` in a restriction of scalars to ``R``.

        ``Res_f(W)`` along ``f: R -> Frac(R)`` is divisible, so it is not
        finitely generated over ``R`` and carries no framing of its own to
        solve coordinates against.  The image of this morphism is still the
        ``R``-span of the finitely many images of the domain framing, and
        that span is read in the ``Frac(R)``-framing ``W`` does carry: one
        common denominator carries the generator images and the target into
        the free ``R``-module on that framing, without changing which
        ``R``-combinations of the images the target is.  The coordinate lift
        decides there, which is the rational solve of the linear system
        followed by the integrality of its solution.
        """
        from dzack_research.preamble.categories.modules.pure.modules import (
            FinitelyGeneratedModules,
            FramedModules,
            RestrictedScalarsModules,
        )

        domain, codomain = self.domain(), self.codomain()
        ring = domain.base_ring()
        assert codomain in RestrictedScalarsModules(ring), f"an unframed lift is stated here for a restriction of scalars, and {codomain} is not one"
        fractions = codomain.extension_ring()
        assert fractions is ring.fraction_field(), (
            f"the integrality test reads denominators in {ring}, so the restricted scalars must be its fraction field; {codomain} restricts {fractions}"
        )
        extension = codomain.module_over_extension()
        assert extension in FramedModules(fractions) and extension in FinitelyGeneratedModules(fractions), (
            f"the span is read in a finite framing of {extension} over {fractions}, and it has none"
        )

        if element.parent() is not codomain:
            element = codomain(element)

        image_coordinates = {
            label: extension.framing_coefficients(self(domain.module_generator(label)).underlying_element())
            for label in domain.module_generating_set()
        }
        target_coordinates = extension.framing_coefficients(element.underlying_element())
        denominator = reduce(
            lambda current, coefficient: current.lcm(coefficient.denominator()),
            tuple(coefficient for coordinates in (*image_coordinates.values(), target_coordinates) for coefficient in coordinates.values()),
            ring.one(),
        )
        scale = codomain.ring_map()(denominator)
        cleared_module = ring._fresh_free_module_on(extension.module_generating_set())

        def cleared(coordinates):
            return cleared_module.linear_combination({label: ring(scale * coefficient) for label, coefficient in coordinates.items()})

        cleared_span = domain.module_category().Mor(domain, cleared_module)({label: cleared(coordinates) for label, coordinates in image_coordinates.items()})
        return cleared_span.lift(cleared(target_coordinates))

    def is_in_image(self, element) -> bool:
        r"""Return whether ``element`` has a preimage when the lift is decidable."""
        try:
            self.lift(element)
        except (TypeError, ValueError):
            return False
        return True

    def orthogonal_complement(self):
        r"""Return ``im(self)^perp`` when the codomain carries a scalar-valued pairing."""
        codomain = self.codomain()
        ring = codomain.base_ring()
        if codomain.value_module() is not ring:
            raise TypeError("this orthogonal-complement construction requires a scalar-valued form")

        source_generators = tuple(self.domain().module_generators())
        labels = Sets.Δ[len(source_generators) - 1]
        target = codomain._fresh_free_module_on(labels)
        pairing_map = codomain.module_category().Mor(codomain, target)(
            {
                label: target.linear_combination(
                    {
                        labels[position]: coefficient
                        for position, source_generator in enumerate(source_generators)
                        if (
                            coefficient := codomain.b(
                                codomain.module_generator(label),
                                self(source_generator),
                            )
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

    def tor_map(self, other, degree=0, *, argument=1, lift=None):
        r"""Return the map on ``Tor_degree`` induced by this module morphism.

        With ``argument=1``, ``self`` acts on the first Tor variable and
        ``other`` is fixed.  With ``argument=2``, ``other`` is the fixed first
        variable and ``self`` acts on the second.
        """
        from dzack_research.preamble.categories.modules.derived_functors import _tor_map

        return _tor_map(self, other, degree=degree, argument=argument, lift=lift)

    def ext_map(self, other, degree=0, *, argument=1, lift=None):
        r"""Return the map on ``Ext^degree`` induced by this module morphism.

        With ``argument=1`` this is contravariant in ``self``; with
        ``argument=2`` the first module ``other`` is fixed and the induced map
        is covariant in ``self``.
        """
        from dzack_research.preamble.categories.modules.derived_functors import _ext_map

        return _ext_map(self, other, degree=degree, argument=argument, lift=lift)

    def divided_square(self):
        r"""Return ``Gamma^2(self)`` on the divided squares of the endpoints."""
        from dzack_research.preamble.categories.modules.powers import (
            _divided_square_morphism,
        )

        return _divided_square_morphism(self)

    def symmetric_power(self, degree):
        r"""Return ``Sym^degree(self)``."""
        from dzack_research.preamble.categories.modules.powers import (
            _symmetric_power_morphism,
        )

        return _symmetric_power_morphism(self, degree)

    def exterior_power(self, degree):
        r"""Return ``Lambda^degree(self)``."""
        from dzack_research.preamble.categories.modules.powers import (
            _alternating_power_morphism,
        )

        return _alternating_power_morphism(self, degree)

    def divided_power(self, degree):
        r"""Return ``Gamma^degree(self)``."""
        from dzack_research.preamble.categories.modules.powers import (
            _divided_power_morphism,
        )

        return _divided_power_morphism(self, degree)

    def base_change(self, ring_map):
        r"""Extend this represented linear map along ``ring_map : R -> S``."""
        ring = self.domain().base_ring()
        if self.codomain().base_ring() is not ring or ring_map.domain() is not ring:
            raise ValueError("module-morphism base change requires one source scalar ring")
        source_base_change = getattr(self.domain(), "base_change", None)
        target_base_change = getattr(self.codomain(), "base_change", None)
        assert callable(source_base_change) and callable(target_base_change), (
            "base change of this module morphism requires represented endpoint base-change constructions"
        )
        source = source_base_change(ring_map)
        target = target_base_change(ring_map)

        return source.module_category().Mor(source, target)(
            {
                label: target.linear_combination(
                    {
                        target_label: ring_map(coefficient)
                        for target_label, coefficient in self.codomain().framing_coefficients(self(self.domain().module_generator(label))).items()
                        if coefficient
                    }
                )
                for label in self.domain().module_generating_set()
            }
        )

    def adic_completion(self, ideal, *, precision=20):
        r"""Return ``self tensor_R R_hat`` using one shared completion parent.

        The endpoint objects are the same completed modules returned by their
        module constructors; the scalar-extension functor adopts those exact
        images before transporting this morphism.
        """
        ring = self.domain().base_ring()
        if self.codomain().base_ring() is not ring:
            raise ValueError("adic completion of a module morphism requires one scalar ring")
        if ideal.ring() is not ring:
            raise ValueError("the completion ideal belongs to the morphism scalar ring")
        completion = ring.adic_completion(ideal, precision=precision)
        return self.base_change_to_completion(completion)

    def base_change_to_completion(self, completion):
        r"""Return ``self tensor_R R_hat`` for one already selected completion."""
        ring = self.domain().base_ring()
        if self.codomain().base_ring() is not ring:
            raise ValueError("adic completion of a module morphism requires one scalar ring")
        if completion.completion_source() is not ring:
            raise ValueError("the completion has the wrong source ring for this morphism")
        source = self.domain().base_change_to_completion(completion)
        target = self.codomain().base_change_to_completion(completion)

        from dzack_research.preamble.categories.modules.pure.modules import Modules

        extension = Modules(ring).scalar_extension(completion.completion_map())
        completed = extension(self)
        if completed.domain() is not source or completed.codomain() is not target:
            raise ArithmeticError(
                "scalar extension did not reuse the selected completed endpoint images"
            )
        return completed

    def completion_cokernel_comparison(self, ideal, *, precision=20):
        r"""Return the canonical ``coker(self)^ ~= coker(self^)`` comparison.

        The source ring is required to be in the represented Noetherian
        regime, where completion is flat.  Both sides use one selected
        completion parent; the comparison maps are induced by the retained
        finite presentations, not by dimensions or invariant factors.
        """
        ring = self.domain().base_ring()
        completion = ring.adic_completion(ideal, precision=precision)
        if not completion.is_flat_over_source():
            raise ArithmeticError("cokernel/completion comparison requires flat Noetherian completion")
        completed_morphism = self.base_change_to_completion(completion)
        source_cokernel = self.cokernel()
        completed_cokernel = source_cokernel.base_change_to_completion(completion)
        cokernel_after_completion = completed_morphism.cokernel()
        left_labels = completed_cokernel.module_generating_set()
        right_labels = cokernel_after_completion.module_generating_set()
        if left_labels.cardinality() != right_labels.cardinality():
            raise ArithmeticError("completion changed the selected cokernel framing cardinality")

        forward = completed_cokernel.module_category().Mor(completed_cokernel, cokernel_after_completion)(
            {label: cokernel_after_completion.module_generator(right_labels[int(left_labels.ranking_map()(label))]) for label in left_labels}
        )
        inverse = cokernel_after_completion.module_category().Mor(cokernel_after_completion, completed_cokernel)(
            {label: completed_cokernel.module_generator(left_labels[int(right_labels.ranking_map()(label))]) for label in right_labels}
        )
        return ModuleCokernelCompletionComparison(
            self,
            completion,
            completed_morphism,
            completed_cokernel,
            cokernel_after_completion,
            forward,
            inverse,
        )

    def _is_the_identity(self) -> bool:
        r"""Return whether this morphism is its Hom object's identity."""
        if self.domain() is not self.codomain():
            return False
        module = self.domain()
        return self is module.module_category().Mor(module, module).identity()

    def __mul__(self, other):
        if isinstance(other, ModuleMorphism):
            if other.codomain() is not self.domain():
                return NotImplemented
            # The identity is a two-sided unit.  That is a theorem, so the
            # composite is the other factor itself rather than a fresh morphism
            # that would then have to be compared with it.
            if self._is_the_identity():
                return other
            if other._is_the_identity():
                return self
            source = other.domain()
            target = self.codomain()
            homset = source.module_category().Mor(source, target)
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
        completion_datum = self.completion_construction()
        if completion_datum is not None:
            completion_source = completion_datum.source_morphism()
            completion = completion_datum.completion()
            source_cokernel = completion_source.cokernel()
            from dzack_research.preamble.categories.modules.pure.modules import Modules

            extension = Modules(completion_source.domain().base_ring()).scalar_extension(completion.completion_map())
            return extension(source_cokernel)
        quotient = self.codomain()._represented_cokernel_of_morphism(self)
        if quotient is NotImplemented:
            quotient = self.domain()._represented_cokernel_of_morphism(self)
        assert quotient is not NotImplemented, (
            "cokernel construction requires a represented quotient-module backend on one endpoint owner"
        )
        return quotient

    @cached_method
    def cokernel_projection(self):
        r"""Return the quotient map ``q : B -> coker(self)``.

        The cokernel is presented on the generators of the codomain, with the
        images of this morphism added as relations.  So the quotient map sends
        each generator to the generator of the same name, and no second model
        of the quotient is built to state it.
        """
        quotient = self.cokernel()
        codomain = self.codomain()
        return codomain.module_category().Mor(codomain, quotient)(lambda label: quotient.module_generator(label))

    def section(self):
        r"""Return ``s`` with ``self . s`` the identity, for an epimorphism onto a free module.

        A section chooses one preimage of each generator of the codomain.
        Those choices assemble into a morphism exactly when the codomain is
        free on those generators, since then there is no relation for them to
        respect: this is projectivity of a free module, and the construction
        exhibits the splitting rather than asserting that one exists.
        """

        codomain = self.codomain()
        assert self.is_surjective(), "only an epimorphism has a section"
        assert codomain.is_free(), f"a section chooses a preimage of each generator, and {codomain} must be free for those choices to respect no relation"
        return codomain.module_category().Mor(codomain, self.domain())(
            lambda label: self.lift(codomain.module_generator(label))
        )

    def retraction(self):
        r"""Return ``r`` with ``r . self`` the identity, for a split monomorphism.

        Splitting ``i : A -> B`` is the same as splitting the quotient
        ``q : B -> B/i(A)``.  Given a section ``s`` of ``q``, each ``b``
        differs from ``s(q(b))`` by an element of ``i(A)``, and ``i`` is
        injective, so ``r(b) = i^{-1}(b - s(q(b)))`` is well defined and
        restricts to the identity on ``A``.  The section exists when the
        cokernel is free, which over a principal ideal domain is exactly when
        this monomorphism splits.
        """

        assert self.is_injective(), "only a monomorphism has a retraction"
        quotient_map = self.cokernel_projection()
        splitting = quotient_map.section()
        codomain = self.codomain()

        def image(label):
            generator = codomain.module_generator(label)
            return self.lift(generator - splitting(quotient_map(generator)))

        return codomain.module_category().Mor(codomain, self.domain())(image)

    def inverse(self):
        r"""Return the two-sided inverse, with coordinate inversion on matrix objects.

        A general module morphism must be an isomorphism.  The canonical
        matrix Hom is also the coordinate-matrix object, where inversion is
        the ordinary matrix operation and may extend coefficients to the
        backend inverse's scalar ring (for example ``ZZ`` to ``QQ``).
        """
        if _has_finite_free_framing(self.domain()) and _has_finite_free_framing(self.codomain()):
            domain_labels = tuple(self.domain().module_generating_set())
            codomain_labels = tuple(self.codomain().module_generating_set())
            coordinate_parent = self.domain().base_ring().matrix_space(len(codomain_labels), len(domain_labels))
            if self.parent() is coordinate_parent:
                if len(domain_labels) != len(codomain_labels):
                    raise ValueError("a matrix inverse requires a square matrix")
                from dzack_research.preamble.categories.modules.pure.modules import (
                    _engine_matrix,
                )
                from dzack_research.preamble.categories.rings.ring_foundation import (
                    _own_ring,
                )

                backend = _engine_matrix(self).inverse()
                result_ring = _own_ring(backend.base_ring())
                target = result_ring.matrix_space(backend.nrows(), backend.ncols())
                return target.from_rows(
                    tuple(
                        tuple(
                            result_ring._from_engine_element(backend[row, column])
                            for column in range(backend.ncols())
                        )
                        for row in range(backend.nrows())
                    )
                )

        assert self.is_injective(), "only a bijection has a two-sided inverse"
        assert self.is_surjective(), "only a bijection has a two-sided inverse"
        codomain = self.codomain()
        inverse_image = self.lift if _has_finite_free_framing(self.domain()) else self.preimage
        return codomain.module_category().Mor(codomain, self.domain())(
            lambda label: inverse_image(codomain.module_generator(label))
        )

    def as_automorphism(self):
        r"""Return this invertible endomorphism as an element of ``Aut_R(M)``.

        An automorphism is not a kind of morphism; it is an element of the
        automorphism group the Hom packet gives the module.  This states the
        endomorphism together with the inverse it constructs, which is what
        that group's elements are.
        """
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            CategoricalIsomorphism,
        )
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        module = self.domain()
        assert self.codomain() is module, "an automorphism is an endomorphism"
        # The inverse was constructed as one, so the pair is mutually inverse by
        # construction and is not re-derived here.
        return Modules(module.base_ring()).Aut(module)(CategoricalIsomorphism(self.parent(), self, self.inverse(), verify=False))


class FramingMorphism(ModuleMorphism):
    r"""A declared surjective linear map from a free framed module."""

    def is_surjective(self) -> bool:
        return True


class ModuleEmbedding(ModuleMorphism):
    r"""A module morphism declared to be a monomorphism."""

    def is_injective(self) -> bool:
        return True


class ModuleEmbeddingHomset(CategoricalHomset):
    r"""The declared monomorphisms between two modules over one scalar ring."""

    Element = ModuleEmbedding

    def __init__(self, hom_family, domain, codomain) -> None:
        modules = domain.module_category()
        if domain not in modules or codomain not in modules:
            raise TypeError("a module embedding Hom requires two modules over one scalar ring")
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    def _element_constructor_(self, images, *, verify_linearity=True, lift=None):
        if isinstance(images, ModuleEmbedding):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the module embedding has the wrong endpoints")
            if images.parent() is self:
                return images
            source = self.domain()
            if source.is_framed_module():
                images = lambda label: images(source.module_generator(label))
            else:
                return self.element_class(
                    self,
                    lambda element: images(element),
                    elementwise=True,
                    verify_linearity=False,
                    lift=lift,
                )
        return self.element_class(
            self,
            images,
            verify_linearity=verify_linearity,
            lift=lift,
        )

    def base_ring(self):
        return self.domain().base_ring()

    def scalar_multiple(self, scalar, morphism):
        r"""Scale an embedding in the underlying linear Hom.

        A scalar multiple of an injective map need not remain injective, so
        this operation deliberately returns through ``Mor_R`` rather than the
        Mono parent.
        """
        source = self.domain()
        target = self.codomain()
        return source.module_category().Mor(source, target).scalar_multiple(
            scalar,
            morphism,
        )

    def super_categories(self):
        packet = self.base_category().category_packet()
        source = self.domain()
        target = self.codomain()
        inherited = [
            superpacket.Monos().Of(source, target)
            for superpacket in packet.super_packets()
            if source in superpacket.C() and target in superpacket.C()
        ]
        return [packet.Homs().Of(source, target), *inherited]

    def _repr_(self):
        return f"Emb({self.domain()}, {self.codomain()})"


def _model_smith_engine(homset):
    r"""The Smith engine of the presented model of ``homset``, when the model has one."""
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _SelectedFinitePresentationModules,
    )

    model = homset.internal_hom_model()
    if model not in _SelectedFinitePresentationModules(model.base_ring()):
        return None
    return model._smith_engine()


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
    modules = hom_family.base_category()
    ring = modules.base_ring()
    assert domain in modules and codomain in modules, (
        f"a Hom of {modules} has two of its objects as endpoints; got {domain} and {codomain}"
    )
    parent._preamble_base_ring = ring if ring in OwnedRings().Commutative() else ring.ring_center()
    parent._preamble_algebra_base_ring = parent._preamble_base_ring
    placement = domain.module_category()._hom_parent_placement(
        domain,
        codomain,
        full_internal_hom=full_internal_hom,
    )
    from dzack_research.preamble.categories.modules.pure.modules import (
        MatrixSpaces,
        _matrix_coefficients,
        _matrix_unit,
        _represented_finite_presentation,
    )

    if ring in OwnedRings().Commutative() and placement.is_subcategory(MatrixSpaces(ring)):
        labels = codomain.module_generating_set().product_with(domain.module_generating_set())
        parent._preamble_module_generating_set = labels
        parent._preamble_module_generator_function = lambda label: _matrix_unit(parent, label)
        parent._preamble_module_coefficient_function = lambda morphism: _matrix_coefficients(
            parent,
            morphism,
        )
        # A matrix space is a finitely generated free module, so Hom objects
        # between matrix spaces are matrix spaces too: it supplies the fresh
        # free-module constructor that placement asks a free module for.
        parent._preamble_free_module_constructor = ring._fresh_free_module_on
    elif ring in OwnedRings().Commutative() and full_internal_hom and _represented_finite_presentation(domain) and _represented_finite_presentation(codomain):
        # Hom(M, N) between presented modules is presented by its
        # endpoint-determined model (see ``internal_hom``); the presented-module
        # protocol reads these hooks, each of which reaches the model lazily.
        parent._preamble_module_generator_function = lambda label: parent._morphism_from_internal_model(parent.internal_hom_model().module_generator(label))
        parent._preamble_module_coordinate_function = lambda morphism: tuple(
            parent.internal_hom_model()._framing_coordinates(parent._internal_model_from_morphism(parent(morphism)))
        )
        parent._preamble_module_from_coordinates_function = lambda coordinates: parent._morphism_from_internal_model(parent.internal_hom_model()._from_coordinates(coordinates))
        parent._preamble_pid_engine_factory = lambda: _model_smith_engine(parent)
    CategoricalHomset.__init__(
        parent,
        hom_family,
        domain,
        codomain,
        category=placement,
    )

    if ring in OwnedRings().Commutative() and placement.is_subcategory(MatrixSpaces(ring)):
        framing_source = ring._fresh_free_module_on(labels)
        parent._preamble_framing_morphism = _framing_morphism(
            framing_source,
            parent,
            parent._preamble_module_generator_function,
        )

    if ring in OwnedRings().Commutative() and full_internal_hom:
        from dzack_research.preamble.categories.modules.internal_hom import (
            InternalHomConstruction,
        )

        construction = InternalHomConstruction(domain, codomain, ring)
        parent._preamble_internal_hom_construction = construction
        if (
            not placement.is_subcategory(MatrixSpaces(ring))
            and _represented_finite_presentation(domain)
            and _represented_finite_presentation(codomain)
        ):
            model, inclusion, relation_matrix, presentation = construction.model_data(parent)
            parent._preamble_internal_hom_model = model
            parent._preamble_internal_hom_inclusion = inclusion
            parent._preamble_module_generating_set = model.module_generating_set()
            parent._preamble_relation_matrix = relation_matrix
            parent._preamble_presentation = presentation
            parent._preamble_framing_morphism = _framing_morphism(
                model.framing_source(),
                parent,
                parent._preamble_module_generator_function,
            )


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
            if not self.domain().is_framed_module():
                return self.elementwise(lambda element: images(element))
            images = {label: images(self.domain().module_generator(label)) for label in self.domain().module_generating_set()}
        elif isinstance(images, Morphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the morphism has the wrong Hom source or target")
            return self.elementwise(lambda element: images(element))
        base_ring = self.base_ring()
        if self.domain() is self.codomain() and (images in base_ring or images in _engine_ring(base_ring)):
            scalar = base_ring(images)
            return self.scalar_multiple(scalar, self.identity())
        model = self.__dict__.get("_preamble_internal_hom_model")
        if model is not None and images in model:
            return self._morphism_from_internal_model(model(images))
        return self.element_class(self, images)

    def base_ring(self):
        return self._preamble_base_ring

    def is_projective(self) -> bool:
        r"""Return whether this represented Hom has a selected finite-free model.

        Matrix Hom objects install their free-module constructor before category
        refinement, so projectivity is a theorem of the retained representation
        rather than a category label used to certify itself.  General internal
        Homs without that model make no projectivity claim here.
        """
        return callable(self.__dict__.get("_preamble_free_module_constructor"))

    def scalar_multiple(self, scalar, morphism):
        return self._owned_scalar_multiple(scalar, morphism)

    def _owned_scalar_multiple(self, scalar, morphism):
        r"""Realize the pointwise action defining this Hom's scalar enrichment."""
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
        underlying sets make it decidable (notably finite ones).  Otherwise the
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

    @cached_method
    def identity(self):
        r"""Return the identity of this endomorphism Hom.

        A Hom object has one identity.  Returning a fresh morphism on each call
        makes it incomparable with itself, since module-morphism equality is
        not decidable without a chosen finite presentation of the source.
        """
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism homset")
        return self.elementwise(
            lambda element: element,
            verify_linearity=False,
        )

    def one(self):
        r"""Return the multiplicative unit when this is an endomorphism ring."""
        return self.identity()


class _AuxiliaryLinearModuleHomset(_ModuleHomsetCommonMethods, CategoricalHomset):
    r"""Private linear-Hom parent used while realizing an internal Hom module.

    This parent represents a linear arrow space needed by an algorithm.  It is
    deliberately placed only in ``LinearHomModules(R)`` and therefore cannot
    recursively demand another internal-Hom module presentation.
    """

    Element = ModuleMorphism

    def __init__(self, domain, codomain) -> None:
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        modules = Modules(_owned_ring(domain.base_ring()))
        _initialize_module_hom_parent(
            self,
            modules.HomCategory(),
            domain,
            codomain,
            full_internal_hom=False,
        )

    def __call__(self, images):
        return self._element_constructor_(images)


def _auxiliary_linear_module_homset(domain, codomain):
    return _AuxiliaryLinearModuleHomset(domain, codomain)


class ModuleHomset(_ModuleHomsetCommonMethods, CategoricalHomset):
    Element = ModuleMorphism

    # The presented-module protocol reads the chosen presentation as data.  A
    # matrix space stores it at construction; any other Hom between presented
    # modules is presented by its endpoint-determined model, reached here on
    # first use.
    @lazy_attribute
    def _preamble_module_generating_set(self):
        return self.internal_hom_model().module_generating_set()

    @lazy_attribute
    def _preamble_relation_matrix(self):
        _model, _inclusion, relation_matrix, _presentation = self._internal_hom_model_data()
        return relation_matrix

    @lazy_attribute
    def _preamble_presentation(self):
        _model, _inclusion, _relation_matrix, presentation = self._internal_hom_model_data()
        return presentation

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

    def internal_hom_construction(self):
        r"""Return the endpoint-determined construction fixed when this Hom parent was created."""
        construction = self.__dict__.get("_preamble_internal_hom_construction")
        assert construction is not None, f"{self} has no internal-Hom construction datum"
        return construction

    def _internal_hom_model_data(self):
        return self.internal_hom_construction().model_data(self)

    def module_generating_set(self):
        selected = self.__dict__.get("_preamble_module_generating_set")
        if selected is not None:
            return selected
        model, _inclusion, _relations, _presentation = self._internal_hom_model_data()
        return model.module_generating_set()

    def module_generator(self, label):
        generator_function = self.__dict__.get("_preamble_module_generator_function")
        if generator_function is not None:
            labels = self.module_generating_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not a module-generator label")
            return generator_function(labels(label))
        model = self.internal_hom_model()
        if label not in model.module_generating_set():
            raise ValueError(f"{label!r} is not an internal-Hom generator label")
        return self._morphism_from_internal_model(model.module_generator(label))

    def presentation_matrix(self):
        stored = self.__dict__.get("_preamble_relation_matrix")
        if stored is not None:
            return stored
        _model, _inclusion, relation_matrix, _presentation = self._internal_hom_model_data()
        return relation_matrix

    def presentation(self):
        stored = self.__dict__.get("_preamble_presentation")
        if stored is not None:
            return stored
        _model, _inclusion, _relation_matrix, presentation = self._internal_hom_model_data()
        return presentation

    def _selected_presentation_rows(self):
        stored = self.__dict__.get("_preamble_relation_matrix")
        if stored is not None:
            return tuple(stored.rows())
        if "_preamble_free_module_constructor" in self.__dict__:
            # A matrix space is free: no relations.
            return ()
        from dzack_research.preamble.categories.modules.pure.modules import (
            _represented_finite_presentation,
        )

        if (
            self.__dict__.get("_preamble_internal_hom_construction") is None
            or not _represented_finite_presentation(self.domain())
            or not _represented_finite_presentation(self.codomain())
        ):
            return None
        return tuple(self.presentation_matrix().rows())

    def _selected_module_coefficients(self, morphism):
        coefficient_function = self.__dict__.get("_preamble_module_coefficient_function")
        if coefficient_function is not None:
            return coefficient_function(morphism)
        model = self.__dict__.get("_preamble_internal_hom_model")
        if model is None:
            from dzack_research.preamble.categories.modules.pure.modules import (
                _represented_finite_presentation,
            )

            if (
                self.__dict__.get("_preamble_internal_hom_construction") is None
                or not _represented_finite_presentation(self.domain())
                or not _represented_finite_presentation(self.codomain())
            ):
                return None
            model = self.internal_hom_model()
        return model.framing_coefficients(self._internal_model_from_morphism(self(morphism)))

    def internal_hom_model(self):
        model = self.__dict__.get("_preamble_internal_hom_model")
        if model is not None:
            return model
        model, inclusion, relation_matrix, presentation = self._internal_hom_model_data()
        self._preamble_internal_hom_model = model
        self._preamble_internal_hom_inclusion = inclusion
        self._preamble_relation_matrix = relation_matrix
        self._preamble_presentation = presentation
        return model

    def inclusion_into_generator_maps(self):
        inclusion = self.__dict__.get("_preamble_internal_hom_inclusion")
        if inclusion is not None:
            return inclusion
        self.internal_hom_model()
        return self._preamble_internal_hom_inclusion

    def _morphism_from_internal_model(self, model_element):
        assignment_space = self.inclusion_into_generator_maps().codomain()
        assignment = self.inclusion_into_generator_maps()(model_element)
        coefficients = assignment_space.framing_coefficients(assignment)
        assignment_labels = assignment_space.module_generating_set()
        return self(
            {
                source_label: self.codomain().linear_combination(
                    {
                        target_label: coefficients[pair]
                        for target_label in self.codomain().module_generating_set()
                        if (pair := assignment_labels(lambda index: source_label if int(index) == 0 else target_label)) in coefficients
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
            for target_label, coefficient in self.codomain().framing_coefficients(image).items():
                coefficients[power_labels(lambda index: source_label if int(index) == 0 else target_label)] = coefficient
        assignment = power.linear_combination(coefficients)
        inclusion = self.inclusion_into_generator_maps()
        if inclusion.has_selected_lift():
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


class SubFramingMorphism(ModuleEmbedding):
    r"""The free module functor applied to an injection of framings.

    An injection of framing sets is split, and the free functor is a left
    adjoint that carries the splitting, so this is a split monomorphism and
    both membership in its image and the lift are decided on labels: an
    element of the larger free module comes from the smaller one exactly when
    it is supported on the smaller framing, and its preimage has the same
    coefficients.

    That is what the class buys over the general route below, which builds the
    matrix of images and solves a linear system.  The smaller framing may be
    infinite, as the degree-two piece of an algebra on countably many
    generators is, and then no matrix exists to solve against.
    """

    def is_in_image(self, element) -> bool:
        r"""Return whether ``element`` is supported on the smaller framing."""
        if element.parent() is not self.codomain():
            return False
        source_labels = self.domain().module_generating_set()
        return all(label in source_labels for label in self.codomain().framing_coefficients(element))

    def lift(self, element):
        r"""Return the unique element of the smaller free module mapping here."""
        assert self.is_in_image(element), f"{element} is not in the image of {self}"
        return self.domain().linear_combination(self.codomain().framing_coefficients(element))


def _framing_morphism(domain, codomain, images) -> FramingMorphism:
    homset = domain.module_category().Mor(domain, codomain)
    framing = FramingMorphism(homset, images)
    return framing


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

        from dzack_research.preamble.categories.modules.pure.modules import Modules

        source = Modules(morphism.domain().base_ring()).tensor_product(
            (morphism.domain(), morphism.domain())
        )
        induced = source.module_category().Mor(source, self.domain())(
            lambda pair: self.domain().pure_tensor(
                morphism(morphism.domain().module_generator(pair.component(0))),
                morphism(morphism.domain().module_generator(pair.component(1))),
            )
        )
        return source.module_category().Mor(source, self.codomain())(self * induced)

    def polar_form(self):
        if self.left_module() is not self.right_module():
            raise TypeError("polar form syntax requires a diagonal bilinear form")
        return self.parent().scalar_multiple(self.domain().base_ring()(2), self)



class ModuleAutomorphism(CategoricalIsomorphism):
    r"""An invertible module endomorphism, as an element of ``Aut_R(M)``."""

    def as_morphism(self):
        return self.forward()

    def matrix(self):
        return self.forward().matrix()

    def order(self):
        return self.matrix().multiplicative_order()

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, ModuleAutomorphism) or other.parent() is not self.parent():
            return False
        return self.forward() == other.forward()

    def __ne__(self, other):
        equal = self == other
        from sage.misc.unknown import Unknown

        return Unknown if equal is Unknown else not equal

    def __hash__(self):
        return hash(id(self.parent()))

    def inverse(self):
        return self.parent()._from_known_inverse_pair(self._inverse, self.forward())

    __invert__ = inverse

    def __mul__(self, other):
        if isinstance(other, ModuleAutomorphism):
            if other.parent() is not self.parent():
                return NotImplemented
            return self.parent()._from_known_inverse_pair(
                self.forward() * other.forward(),
                other._inverse * self._inverse,
            )
        if isinstance(other, ModuleMorphism):
            return self.forward() * other
        return NotImplemented


class ModuleAutomorphismGroups(OwnedCategoryOverBaseRing):
    r"""The groups ``Aut_R(M)`` of invertible module endomorphisms."""

    @classmethod
    def _repr_object_names(cls):
        return "module automorphism groups"

    def super_categories(self):
        from dzack_research.preamble.categories.group.groups import OwnedGroups

        return [OwnedGroups()]

    class ParentMethods:
        @cached_method
        def identity(self):
            module = self.domain()
            identity = module.module_category().Mor(module, module).identity()
            return self._from_known_inverse_pair(identity, identity)

        one = identity
        identity_automorphism = identity


class ModuleAutomorphismGroup(CategoricalHomset):
    r"""The unit group of ``End_R(M)``, retaining its actual module maps."""

    Element = ModuleAutomorphism

    def __init__(self, hom_family, module) -> None:
        self._preamble_base_ring = _owned_ring(module.base_ring())
        CategoricalHomset.__init__(
            self,
            hom_family,
            module,
            module,
            category=ModuleAutomorphismGroups(self._preamble_base_ring),
        )

    def base_ring(self):
        return self._preamble_base_ring

    def _from_known_inverse_pair(self, forward, inverse):
        module = self.domain()
        homset = module.module_category().Mor(module, module)
        forward = homset(forward)
        inverse = homset(inverse)
        return self.element_class(self, forward, inverse, verify=False)

    def __call__(self, datum):
        r"""Construct an automorphism-group element rather than preserving a bare Iso arrow."""
        if isinstance(datum, ModuleAutomorphism) and datum.parent() is self:
            return datum
        return self._element_constructor_(datum)

    def _element_constructor_(self, datum):
        if isinstance(datum, ModuleAutomorphism):
            if datum.parent() is self:
                return datum
            datum = datum.as_morphism()
        if isinstance(datum, CategoricalIsomorphism):
            return self._from_known_inverse_pair(datum.forward(), datum.inverse())
        module = self.domain()
        forward = module.module_category().Mor(module, module)(datum)
        return self._from_known_inverse_pair(forward, forward.inverse())

    @cached_method
    def identity(self):
        module = self.domain()
        identity = module.module_category().Mor(module, module).identity()
        return self._from_known_inverse_pair(identity, identity)

    one = identity
    identity_automorphism = identity

    def module(self):
        return self.domain()

    def __contains__(self, candidate):
        return isinstance(candidate, ModuleAutomorphism) and candidate.parent() is self

    def is_finite(self):
        try:
            return bool(self.module().is_finite())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            from sage.misc.unknown import Unknown

            return Unknown

    def super_categories(self):
        packet = self.base_category().category_packet()
        module = self.domain()
        supers = [
            packet.Homs().Of(module, module),
            packet.Monos().Of(module, module),
            packet.Epis().Of(module, module),
        ]
        if self.aut_family() is not None:
            supers.append(packet.Ends().Of(module))
        return supers

    def _repr_(self):
        return f"Aut_{self.base_category()}({self.module()})"


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

        if isinstance(images, IndexedFamily):
            source_indices = images.index_set()
            raw_family = images

            def generator_image(pair):
                source_pair = source_indices(lambda index: pair.component(index))
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
        elif isinstance(images, (tuple, list)) and all(isinstance(row, (tuple, list)) for row in images):
            left_size = left_labels.cardinality()
            right_size = right_labels.cardinality()
            if not left_size.is_finite() or not right_size.is_finite():
                raise TypeError("coordinate-array pairing syntax requires finite framings")
            if len(images) != int(left_size.finite_value()) or any(len(row) != int(right_size.finite_value()) for row in images):
                raise ValueError("the pairing coordinate array has the wrong shape")
            by_position = {(i, j): images[i][j] for i in range(len(images)) for j in range(len(images[i]))}

            def generator_image(pair):
                value = by_position[
                    int(left_labels.ranking_map()(pair.component(0))),
                    int(right_labels.ranking_map()(pair.component(1))),
                ]
                return value if getattr(value, "parent", lambda: None)() is self.codomain() else self.codomain()(value)

            images = generator_image

        return super()._element_constructor_(images)
