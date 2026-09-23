"""Linear maps between represented modules."""

import logging
from functools import reduce
from inspect import Parameter, isfunction, ismethod, signature
from itertools import product

from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown
from sage.structure.element import parent as element_parent

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    CategoricalIsomorphism,
    _precomposable,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    LocalRings,
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_ring,
    _enumerated_ring_elements,
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


def _has_finite_free_framing(module) -> bool:
    r"""Whether ``module`` is framed, free and finitely generated: an endpoint of a coordinate matrix."""
    from dzack_research.preamble.categories.modules.pure.modules import (
        _coordinate_framed_free_module,
    )

    return _coordinate_framed_free_module(module, module.base_ring())


def _finite_generating_elements(module):
    r"""A finite determining family for linear maps, or no such supplied data.

    Used only by module-morphism comparison. Relations are unnecessary for
    comparing already admitted linear maps: linearity extends equality from
    a spanning family. Products of spanning families span a tensor product
    by bilinearity (Mathlib TensorProduct.ext). Adding structure preserves
    the supplied unformed module's family through its existing coercion.
    No infinite family or point sample is used to infer equality.
    """
    from dzack_research.preamble.categories.modules.pure.modules import FramedModules, TensorProductModules

    ring = module.base_ring()
    match module:
        case _ if module in FramedModules(ring) and module.module_generating_set().cardinality().is_finite():
            return iter(module.module_generators())
        case _ if module in TensorProductModules(ring) and module.tensor_factors().cardinality() == 2:
            left = _finite_generating_elements(module.tensor_factor(0))
            right = _finite_generating_elements(module.tensor_factor(1))
            if left is None or right is None:
                return None
            return (module.pure_tensor(x, y) for x, y in product(left, right))
        case _ if module.unformed_module() is not module:
            elements = _finite_generating_elements(module.unformed_module())
            return None if elements is None else map(module, elements)
        case _:
            return None


def _integral_left_solver(system, ring):
    r"""Factor one integral system once and return its exact row solver.

    The solver returns the solution ``a`` of ``a * system = target``, or
    ``None`` when the target is not an integral combination of the rows: the
    Smith form ``D = U A V`` reduces the system to ``d_i x_i = (U t)_i``,
    solvable exactly when each ``d_i`` divides its right-hand side.
    """

    from dzack_research.preamble.categories.modules.pure.modules import MatrixSpaces

    assert ring in OwnedRings(), "integral solving requires an owned coefficient ring"
    assert system.parent() in MatrixSpaces(ring), f"an integral linear system over {ring} is an element of a matrix mor over it, and {system.parent()} is not one"

    transposed = system.transpose()
    smith, left, right = transposed.smith_form()
    target_labels = left.domain().module_generating_set()
    shifted_labels = left.codomain().module_generating_set()
    width = int(smith.domain().module_generating_set().cardinality())

    def solve(target):
        target_values = tuple(ring(value) for value in target)
        assert len(target_values) == int(target_labels.cardinality()), (
            "the target has the length of this linear system"
        )
        target_vector = left.domain().linear_combination({label: target_values[position] for position, label in enumerate(target_labels) if target_values[position]})
        shifted_vector = left(target_vector)
        shifted_coefficients = left.codomain().framing_coefficients(shifted_vector)

        solution = [ring.zero()] * width
        for index, shifted_label in enumerate(shifted_labels):
            value = shifted_coefficients.get(shifted_label, ring.zero())
            divisor = smith[index, index] if index < min(int(shifted_labels.cardinality()), width) else ring.zero()
            if divisor == 0:
                if value != 0:
                    return None
                continue
            quotient, remainder = value.quo_rem(divisor)
            if remainder != 0:
                return None
            solution[index] = quotient

        normalized_solution = right.domain().linear_combination(
            {label: solution[position] for position, label in enumerate(right.domain().module_generating_set()) if solution[position]}
        )
        return right(normalized_solution)

    return solve


def _solve_left_integrally_element(system, target, ring):
    r"""Return the row-coefficient element ``a`` with ``a*system = target``, or ``None``."""

    return _integral_left_solver(system, ring)(target)


def _solve_left_integrally(system, target, ring):
    r"""Return positional coefficients ``a`` with ``a*system = target`` over a PID, or ``None``."""
    original_solution = _solve_left_integrally_element(system, target, ring)
    if original_solution is None:
        return None
    coefficients = original_solution.parent().framing_coefficients(original_solution)
    return tuple(coefficients.get(label, ring.zero()) for label in original_solution.parent().module_generating_set())


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
    r"""The linear extension of a function on a chosen module framing.

    Construction data: the images of the framing of the domain, or an exact
    elementwise map when the domain is unframed or the map is stated on
    elements; optionally a selected lift through the map; and, for a map
    ``S tensor_R f`` constructed by scalar extension along ``R -> S``, the
    morphism ``f`` and the scalar-extension functor it is the image under.
    """

    _scalar_extension_of = None
    _scalar_extension_functor = None
    _lift_function = None

    def _elementwise_linearity_derivation(self):
        r"""Return the construction-derived linearity decision, or ``None``.

        Ordinary elementwise callables do not.  Private universal-construction
        morphisms override this at their declaration, so callers cannot select
        a derivation with a string or boolean flag.
        """
        premise = getattr(self, "_direct_linearity_premise", None)
        if premise is not None:
            return premise.linearity_decision()
        return None

    def _selected_lift_derivation(self):
        r"""Return whether a supplied lift is exact by construction, or ``None``.

        A caller-supplied Python function is not evidence that ``None`` means
        an element lies outside the image.  Constructor-owned subobject maps
        override this hook when their selected lift is part of the subobject
        datum itself.
        """
        return None

    def __init__(
        self,
        parent,
        images,
        *,
        elementwise=False,
        scalar_extension_of=None,
        scalar_extension_functor=None,
        lift=None,
    ) -> None:
        from dzack_research.preamble.categories.modules.pure.modules import FramedModules

        Morphism.__init__(self, parent)
        assert (scalar_extension_of is None) == (scalar_extension_functor is None), (
            "a scalar-extension image names both the morphism and the functor it is the image under"
        )
        self._scalar_extension_of = scalar_extension_of
        self._scalar_extension_functor = scalar_extension_functor
        self._lift_function = lift
        self._direct_linearity_premise = None
        self._selected_lift_exactness = True if lift is None else Unknown
        if lift is not None:
            lift_derivation = self._selected_lift_derivation()
            if lift_derivation is False:
                raise ValueError("the selected lift is refuted by its construction data")
            if lift_derivation is True:
                self._selected_lift_exactness = True
        self._element_function = None
        self._linearity_decision = True
        domain = self.domain()
        codomain = self.codomain()
        if (
            isinstance(images, Morphism)
            and images.domain() is domain
            and images.codomain() is codomain
        ):
            source_morphism = images
            if isinstance(source_morphism, ModuleMorphism):
                self._direct_linearity_premise = source_morphism
            images = lambda element: source_morphism(element)
            elementwise = True
        if elementwise or domain not in FramedModules(domain.base_ring()):
            if not callable(images):
                raise TypeError("a morphism from an unframed module must be supplied as an exact element map")
            self._element_function = images
            self._generator_image = None
            self._generator_morphism = None
            derivation = self._elementwise_linearity_derivation()
            match derivation:
                case None:
                    self._linearity_decision = self._verify_elementwise_linearity_when_decidable()
                case False:
                    raise ValueError("the supplied elementwise map is not module-linear")
                case _:
                    self._linearity_decision = derivation
            self._refute_invalid_selected_lift_when_decidable()
            return
        labels = self.domain().module_generating_set()
        set_mor = Sets().Mor(labels, self.codomain())
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
            self._generator_morphism = set_mor(self._generator_image)
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
            self._generator_morphism = set_mor(self._generator_image)
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
            self._generator_morphism = set_mor(self._generator_image)
        elif callable(images):
            self._generator_images = indexed_family(
                labels,
                images,
                name="Generator images",
            )
            self._generator_image = self._generator_images.value
            self._generator_morphism = set_mor(self._generator_image)
        else:
            raise TypeError("a module morphism is specified on the domain framing")
        self._linearity_decision = self._check_selected_domain_relations()
        self._refute_invalid_selected_lift_when_decidable()

    def _refute_invalid_selected_lift_when_decidable(self) -> None:
        r"""Reject witnessed section-equation failures of a selected lift.

        This is a refutation pass, not a proof that an arbitrary lift callback
        is exact.  On a represented finite codomain every returned candidate is
        checked; otherwise zero is still a sound probe.  A callback that passes
        these checks remains unresolved unless its constructor supplies a lift
        derivation.
        """
        custom = self._lift_function
        if custom is None:
            return
        codomain = self.codomain()
        ring = codomain.base_ring()
        targets = None
        try:
            finite_codomain = codomain.is_finite() is True
        except (AttributeError, NotImplementedError):
            finite_codomain = False
        if finite_codomain:
            from dzack_research.preamble.categories.modules.pure.modules import Modules

            if codomain in EnumeratedSets() or codomain in Modules(ring).FinitelyPresented().Torsion():
                targets = tuple(codomain)
        if targets is None:
            probes = [codomain.zero()]
            generators = _finite_generating_elements(codomain)
            if generators is not None:
                probes.extend(generators)
            targets = tuple(probes)
        for target in targets:
            candidate = custom(target)
            if candidate is None:
                continue
            candidate = self.domain()(candidate)
            section_equation = self(candidate) == target
            if section_equation is False:
                raise ValueError("the selected lift does not satisfy the section equation")

    def linearity_decision(self):
        r"""Return ``True`` when linearity is established, otherwise ``Unknown``.

        Generator-image maps are linear extensions after their source relations
        are checked.  Elementwise maps are either decided in an effective
        regime, derived by a named universal construction, or retain the
        unresolved hypothesis explicitly.
        """
        return self._linearity_decision

    def _require_established_linearity(self, operation: str) -> None:
        r"""Require the linearity premise consumed by a linear-algebra conclusion."""
        if self.linearity_decision() is not True:
            raise ValueError(
                f"{operation} requires established module-linearity; this map retains an unresolved linearity hypothesis"
            )

    def _verify_elementwise_linearity_when_decidable(self):
        r"""Check an elementwise callable exactly in represented decidable regimes.

        A Python callable does not carry a proof of linearity.  When the source
        module is finite and enumerable, additivity is decidable by exhaustive
        verification, and the scalars an additive map commutes with form a
        subring, so a ring generating set decides scalar-linearity over all of
        ``R``.  Over ``ZZ`` that generating set is empty: every additive-group
        map is automatically ``ZZ``-linear.  Outside such regimes the callable
        retains an ``Unknown`` linearity hypothesis; a DEBUG diagnostic records
        that no exhaustive verification was available.

        A map given by images of a framing is not reached here at all.  Its
        linear extension is linear by construction, and the relations of the
        chosen presentation are what has to be checked instead.
        """
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        function = self._element_function
        if function is None:
            return True

        domain = self.domain()
        codomain = self.codomain()
        source_elements = self._finite_source_elements_for_verification()
        if source_elements is not None:
            return self._verify_elementwise_on_finite_source(source_elements)

        ring = domain.base_ring()
        match domain:
            case _ if domain.is_finite() is not True:
                self._check_elementwise_zero()
                self._refute_elementwise_linearity_on_selected_generators()
                _LOGGER.debug(
                    "Elementwise module morphism %s -> %s accepted without exhaustive linearity verification; the source is not represented as finite",
                    domain,
                    codomain,
                )
                return Unknown
            case _ if domain in EnumeratedSets() or domain in Modules(ring).FinitelyPresented().Torsion():
                return self._verify_elementwise_on_finite_source(tuple(domain))
            case _:
                self._check_elementwise_zero()
                _LOGGER.debug(
                    "Elementwise module morphism %s -> %s accepted without exhaustive linearity verification; finite source has no represented enumeration",
                    domain,
                    codomain,
                )
                return Unknown

    def _refute_elementwise_linearity_on_selected_generators(self) -> None:
        r"""Reject witnessed law failures without promoting finite probes to a proof.

        A finite framing does not decide an arbitrary callable on an infinite
        module.  It does, however, supply sound counterexamples when additivity
        already fails on two selected generators, or scalar-linearity fails on
        a represented ring generator and one selected module generator.  Passing
        these probes leaves the decision ``Unknown``.
        """
        generators = _finite_generating_elements(self.domain())
        if generators is None:
            return
        generators = tuple(generators)
        function = self._element_function
        for left in generators:
            for right in generators:
                additive = function(left + right) == function(left) + function(right)
                if additive is False:
                    raise ValueError("the supplied elementwise map is not additive")

        scalars = _scalar_linearity_generating_scalars(self.domain().base_ring())
        if scalars is None:
            return
        for scalar in scalars:
            for generator in generators:
                scalar_linear = (
                    function(self.domain().scalar_multiple(scalar, generator))
                    == self.codomain().scalar_multiple(scalar, function(generator))
                )
                if scalar_linear is False:
                    raise ValueError("the supplied elementwise map is not scalar-linear")

    def _finite_source_elements_for_verification(self):
        r"""Enumerate a finitely generated module over a finite ring via its framing.

        Distinct scalar combinations of the framing of a free module are
        distinct elements; over a quotient of a free module they can coincide
        and are listed once.
        """
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FramedFreeModules,
        )
        from dzack_research.preamble.categories.modules.pure.modules import FramedModules

        domain = self.domain()
        ring = domain.base_ring()
        if domain not in FramedModules(ring):
            return None
        label_set = domain.module_generating_set()
        if not label_set.cardinality().is_finite():
            return None
        labels = tuple(label_set)
        if not labels:
            return (domain.zero(),)
        scalars = _enumerated_ring_elements(ring)
        if scalars is None:
            return None
        combinations = (
            domain.linear_combination({label: coefficient for label, coefficient in zip(labels, coefficients, strict=True) if coefficient != 0})
            for coefficients in product(scalars, repeat=len(labels))
        )
        match domain:
            case _ if domain in FramedFreeModules(ring):
                return tuple(combinations)
            case _:
                elements = []
                for element in combinations:
                    duplicate = False
                    for previous in elements:
                        equal = element == previous
                        if equal is True:
                            duplicate = True
                            break
                        if equal is not False:
                            return None
                    if not duplicate:
                        elements.append(element)
                return tuple(elements)

    def _verify_elementwise_on_finite_source(self, source_elements):
        function = self._element_function
        domain = self.domain()
        codomain = self.codomain()
        ring = domain.base_ring()
        zero = domain.zero()

        decision = True
        zero_holds = function(zero) == codomain.zero()
        if zero_holds is False:
            raise ValueError("an elementwise module morphism must send zero to zero")
        if zero_holds is not True:
            decision = Unknown
        for left in source_elements:
            for right in source_elements:
                additive = function(left + right) == function(left) + function(right)
                if additive is False:
                    raise ValueError("the supplied elementwise map is not additive")
                if additive is not True:
                    decision = Unknown

        from sage.rings.integer_ring import ZZ as SageZZ

        if _engine_ring(ring) is SageZZ:
            return decision

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
            return Unknown
        for scalar in scalars:
            for element in source_elements:
                scalar_linear = (
                    function(domain.scalar_multiple(scalar, element))
                    == codomain.scalar_multiple(scalar, function(element))
                )
                if scalar_linear is False:
                    raise ValueError("the supplied elementwise map is not scalar-linear")
                if scalar_linear is not True:
                    decision = Unknown
        return decision

    def _check_elementwise_zero(self):
        r"""A linear map sends zero to zero."""
        zero_holds = self._element_function(self.domain().zero()) == self.codomain().zero()
        if zero_holds is False:
            raise ValueError("an elementwise module morphism must send zero to zero")
        return True if zero_holds is True else Unknown

    def _check_selected_domain_relations(self):
        if self._element_function is not None:
            return self._linearity_decision
        domain = self.domain()
        rows = domain._selected_presentation_rows()
        if rows is None:
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                FramedFreeModules,
            )

            if domain in FramedFreeModules(domain.base_ring()):
                return True
            return Unknown
        zero = self.codomain().zero()
        labels = domain.module_generating_set()
        decision = True
        for row in rows:
            relation_image = self._linear_combination_of_generator_images({label: coefficient for label, coefficient in zip(labels, row, strict=True) if coefficient})
            relation_holds = relation_image == zero
            if relation_holds is False:
                raise ValueError("the selected module-generator images do not kill the domain relations")
            if relation_holds is not True:
                decision = Unknown
        return decision

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
        r"""Return the pointwise sum in ``Hom_R(M, N)``.

        ``other`` is read in this Mor module by its element constructor: a
        linear map with the same endpoints, or a scalar of an endomorphism
        ring, which is that multiple of the identity.
        """
        parent = self.parent()
        summand = parent(other)
        from dzack_research.preamble.categories.group.additive_mors import _scalar_identity_coefficient

        left, right = _scalar_identity_coefficient(self), _scalar_identity_coefficient(summand)
        if left is not None and right is not None:
            return parent._scalar_identity(left + right)
        return _PointwiseSumModuleMorphism(parent, self, summand)

    def __neg__(self):
        parent = self.parent()
        from dzack_research.preamble.categories.group.additive_mors import _scalar_identity_coefficient

        scalar = _scalar_identity_coefficient(self)
        if scalar is not None:
            return parent._scalar_identity(-scalar)
        return _PointwiseNegationModuleMorphism(parent, self)

    def __sub__(self, other):
        r"""Return the pointwise difference in ``Hom_R(M, N)``."""
        return self + (-self.parent()(other))

    def _richcmp_(self, other, op):
        r"""Compare admitted linear maps on an available finite spanning family.

        A missing finite family or undecided value comparison remains Unknown;
        neither failed normalization nor a finite sample disproves equality.
        """
        from sage.structure.richcmp import op_EQ, op_NE

        if op not in (op_EQ, op_NE):
            return NotImplemented
        if not isinstance(other, ModuleMorphism) or other.parent() is not self.parent():
            return op == op_NE
        if self is other:
            return op == op_EQ
        from sage.misc.unknown import Unknown

        from dzack_research.preamble.categories.group.additive_mors import _scalar_identity_coefficient

        left, right = _scalar_identity_coefficient(self), _scalar_identity_coefficient(other)
        if left is not None and right is not None and (left == right) is True:
            return op == op_EQ
        elements = _finite_generating_elements(self.domain())
        if elements is None:
            return Unknown
        comparisons = tuple(self(element) == other(element) for element in elements)
        established_linear = (
            self.linearity_decision() is True
            and other.linearity_decision() is True
        )
        match (
            any(answer is False for answer in comparisons),
            all(answer is True for answer in comparisons),
            established_linear,
        ):
            case (True, _, _):
                equal = False
            case (_, True, True):
                equal = True
            case _:
                equal = Unknown
        return equal if op == op_EQ else (Unknown if equal is Unknown else not equal)

    def __rmul__(self, actor):
        # A specialized right operand such as ModuleEmbedding gets reflected
        # multiplication before Python tries the less-specialized left
        # ModuleMorphism.__mul__.  In that case the operation is composition,
        # not scalar multiplication.  Delegate to the left morphism so the
        # ordinary endpoint check and composition constructor remain the one
        # owner of the operation.
        from dzack_research.preamble.categories.modules.pure.modules import (
            LinearMorModules,
        )

        match element_parent(actor) in LinearMorModules(self.domain().base_ring()):
            case True:
                return actor.__mul__(self)
            case False:
                return self.parent().scalar_multiple(actor, self)

    def _lmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _rmul_(self, scalar):
        return self._lmul_(scalar)

    def _acted_upon_(self, actor, self_on_left):
        r"""Use the canonical pointwise scalar action of the Mor module."""
        _ = self_on_left
        match actor:
            case _ if actor in self.parent().base_ring():
                return self.parent().scalar_multiple(actor, self)
            case _:
                return None

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

    def internal_mor_map(
        self,
        target_map,
        *,
        source_internal_mor=None,
        target_internal_mor=None,
    ):
        r"""Return the internal-Mor map induced by pre- and postcomposition."""
        from dzack_research.preamble.categories.modules.internal_mor import (
            _internal_mor_morphism,
        )

        return _internal_mor_morphism(
            self,
            target_map,
            source_internal_mor=source_internal_mor,
            target_internal_mor=target_internal_mor,
        )

    def stack(self, other):
        r"""Return ``(self,other)`` into the biproduct of the codomains."""
        assert other.domain() is self.domain(), "stacking module maps requires one common domain"

        from dzack_research.preamble.categories.modules.pure.modules import Modules

        target = Modules(self.codomain().base_ring()).biproduct(
            (self.codomain(), other.codomain())
        )
        return target.to_product(self, other)

    def scalar_extension_of(self):
        r"""Return ``f`` when this morphism was constructed as ``S tensor_R f``, else ``None``."""
        return self._scalar_extension_of

    def scalar_extension_functor(self):
        r"""Return the functor ``S tensor_R -`` this morphism is the image under, else ``None``."""
        return self._scalar_extension_functor

    def _flat_scalar_extension_ring(self):
        r"""Return ``S`` when this morphism is ``S tensor_R f`` along a flat ``R -> S``, else ``None``.

        A localization is flat over its source, and the adic completion of a
        Noetherian ring is flat over it; those are the scalar extensions whose
        images retain their preimage.
        """
        from dzack_research.preamble.categories.rings.commutative_algebra import (
            AdicCompletions,
        )

        functor = self._scalar_extension_functor
        if functor is None:
            return None
        extended_ring = _owned_ring(functor.ring_map().codomain())
        match extended_ring:
            case _ if extended_ring in AdicCompletions():
                assert extended_ring.is_flat_over_source(), (
                    "the completion a completed morphism retains is flat over its Noetherian source"
                )
                return extended_ring
            case _ if extended_ring in LocalizationRings():
                return extended_ring
            case _:
                return None

    @cached_method
    def kernel(self):
        r"""Return ``ker(self)`` as a subobject of the domain.

        Scalar extension along a flat ring map ``R -> S`` is exact, so
        ``ker(S tensor f) = S tensor ker(f)`` with the extended inclusion.  A
        map between localizations of modules along one localization of a
        local ring descends to their numerators by clearing denominators.
        Otherwise a representation of an endpoint computes the kernel.
        """
        self._require_established_linearity("kernel construction")
        from dzack_research.preamble.categories.modules.localizations import (
            LocalizedModules,
        )
        from dzack_research.preamble.categories.modules.pure.modules import (
            ModuleSubobjects,
        )
        from dzack_research.preamble.categories.rings.commutative_algebra import (
            AdicCompletions,
        )

        domain = self.domain()
        codomain = self.codomain()
        extended_ring = self._flat_scalar_extension_ring()
        match extended_ring:
            case None:
                pass
            case _ if extended_ring in AdicCompletions():
                source_morphism = self._scalar_extension_of
                extension = self._scalar_extension_functor
                assert extension(source_morphism.domain()) is domain, (
                    "the completed morphism domain is the retained scalar-extension image of its source"
                )
                source_kernel = source_morphism.kernel()
                extension(source_kernel)
                completed_inclusion = extension(source_kernel.inclusion())
                assert completed_inclusion.codomain() is domain, (
                    "the completed source-kernel inclusion lands in the completed domain"
                )
                return completed_inclusion.image()
            case _:
                localization_functor = self._scalar_extension_functor
                source_kernel = self._scalar_extension_of.kernel()
                localized_kernel = localization_functor(source_kernel)
                localized_inclusion = localization_functor(source_kernel.inclusion())
                assert localized_inclusion.codomain() is domain, (
                    "the localized kernel inclusion lands in the localized domain"
                )
                assert localized_kernel in ModuleSubobjects(domain.base_ring()), (
                    "localization preserves the source-kernel subobject"
                )
                assert localized_kernel.inclusion() is localized_inclusion, (
                    "the localized kernel carries the localized inclusion"
                )
                return localized_kernel

        ring = domain.base_ring()
        match domain:
            case _ if (
                ring in LocalRings()
                and domain in LocalizedModules(ring)
                and codomain in LocalizedModules(ring)
                and codomain.localization_functor() is domain.localization_functor()
                and _has_finite_free_framing(domain.numerator_module())
            ):
                functor = domain.localization_functor()
                source_domain = domain.numerator_module()
                source_codomain = codomain.numerator_module()
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
                assert localized_inclusion.codomain() is domain, (
                    "the descended local kernel inclusion returns to the local domain"
                )
                return localized_kernel

        represented = NotImplemented
        for owner in (domain, codomain):
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
        self._require_established_linearity("image construction")
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
        reconstruct a preimage in the original domain.  A finite torsion
        domain is searched.  An element outside the image is rejected with
        ``ValueError``.
        """
        self._require_established_linearity("preimage computation")
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        domain = self.domain()
        codomain = self.codomain()
        element = element if element.parent() is codomain else codomain(element)
        if element == codomain.zero():
            return domain.zero()
        match domain:
            case _ if _has_finite_free_framing(domain):
                pass
            case _:
                assert domain in Modules(domain.base_ring()).FinitelyPresented().Torsion() and domain.cardinality().is_finite(), (
                    "represented preimages require a finitely framed free domain or a finite torsion domain"
                )
                found = next((candidate for candidate in domain.elements() if self(candidate) == element), None)
                if found is None:
                    raise ValueError("the selected element does not lie in the represented image")
                return found
        if self.is_surjective() and codomain.is_free():
            return self.section()(element)

        image = self.image()
        image_element = image.inclusion().lift(element)
        coefficients = image.framing_coefficients(image_element)
        domain_labels = domain.module_generating_set()
        assert all(label in domain_labels for label in coefficients), (
            "the represented image framing records the source-generator labels"
        )
        return domain.linear_combination({label: coefficient for label, coefficient in coefficients.items() if coefficient})

    def is_injective(self) -> bool:
        r"""Return whether ``ker(self)=0`` when the kernel is computable."""
        self._require_established_linearity("injectivity")
        return self.kernel().is_zero()

    def is_surjective(self) -> bool:
        r"""Return whether ``coker(self)=0`` when the cokernel is computable."""
        self._require_established_linearity("surjectivity")
        return self.cokernel().is_zero()

    def residue_morphism(self):
        r"""Return ``f tensor_R k`` for a morphism of finite modules over a local ring."""

        ring = self.domain().base_ring()
        assert self.codomain().base_ring() is ring, "a residue morphism requires one common base ring"
        assert ring in LocalRings(), "reduction modulo the maximal ideal requires a local ring"
        assert self.domain().is_finitely_generated() and self.codomain().is_finitely_generated(), (
            "Nakayama's lemma is stated for finitely generated source and target"
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
        assert self.is_injective(), "saturation is defined for a monomorphism"
        quotient = self.cokernel()
        projection = quotient.torsion_free_quotient_projection()
        composite = projection * quotient.presentation_projection()
        return composite.kernel()

    def index(self):
        r"""Return the cardinality of the cokernel."""
        return self.cokernel().cardinality()

    def _preimage_or_none(self, element):
        r"""Return the preimage of ``element`` under this injective map, or ``None`` outside the image.

        Protected contract of module morphisms.  Its callers are :meth:`lift`,
        :meth:`is_in_image` and :meth:`factor_through`.  A lift selected at
        construction is such a function: it returns the preimage of an
        element of the image and ``None`` for any other element.  Otherwise
        the coordinates of ``element`` are solved against the images of the
        domain framing over the base ring.
        """
        custom = self._lift_function
        if custom is not None:
            candidate = custom(element)
            if candidate is None:
                if self._selected_lift_exactness is True:
                    return None
                raise ValueError(
                    "the selected lift returned no candidate, but its exactness is unresolved"
                )
            candidate = self.domain()(candidate)
            target = element if element.parent() is self.codomain() else self.codomain()(element)
            section_equation = self(candidate) == target
            if section_equation is False:
                raise ValueError("the selected lift does not satisfy the section equation on this element")
            if section_equation is not True:
                raise ValueError("the selected lift section equation is undecidable on this element")
            return candidate
        self._require_established_linearity("represented preimage computation")
        ring = self.domain().base_ring()
        assert _has_finite_free_framing(self.domain()), f"a lift is solved for the coefficients of a framing, and {self.domain()} has none"
        if not _has_finite_free_framing(self.codomain()):
            return self._preimage_through_the_extension_framing(element)
        if element.parent() is not self.codomain():
            element = self.codomain()(element)
        codomain_labels = tuple(self.codomain().module_generating_set())
        coefficients = self.codomain().framing_coefficients(element)
        target = [coefficients[label] if label in coefficients else self.codomain().base_ring().zero() for label in codomain_labels]
        coordinate_map = self.domain().module_category().Mor(
            self.domain(), self.codomain()
        )(self)
        solution = _solve_left_integrally(
            coordinate_map.transpose(),
            target,
            ring,
        )
        if solution is None:
            return None
        return self.domain().linear_combination({label: coefficient for label, coefficient in zip(self.domain().module_generating_set(), solution, strict=True) if coefficient})

    def lift(self, element):
        r"""Return the unique preimage of ``element``; an element outside the image is rejected with ``ValueError``."""
        preimage = self._preimage_or_none(element)
        if preimage is None:
            raise ValueError(f"{element} is not in the image of {self}")
        return preimage

    def is_in_image(self, element) -> bool:
        r"""Return whether ``element`` has a preimage under this injective map."""
        return self._preimage_or_none(element) is not None

    def has_selected_lift(self) -> bool:
        r"""Return whether this map carries a selected lift callback."""
        return self._lift_function is not None

    def selected_lift_exactness_decision(self):
        r"""Return whether absence reported by the selected lift is construction-derived."""
        return self._selected_lift_exactness

    def factor_through(self, target_embedding):
        r"""Return the unique factor through a represented module embedding.

        For ``f:A -> X`` and a monomorphism ``j:B -> X`` this constructs the
        commuting-triangle map ``A -> B`` exactly when every selected generator
        image of ``f`` lies in ``j(B)``; otherwise ``ValueError`` states that
        ``f`` does not factor.  The source map need not itself be a
        monomorphism; uniqueness comes from ``j``.
        """
        factor = self.factor_through_or_none(target_embedding)
        if factor is None:
            raise ValueError("the morphism image is not contained in the target subobject")
        return factor

    def factor_through_or_none(self, target_embedding):
        r"""Return the unique represented factor, or None when containment fails."""
        self._require_established_linearity("factorization through a module subobject")
        assert target_embedding.codomain() is self.codomain(), (
            "module factorization through a subobject requires one common codomain"
        )
        source = self.domain()
        target = target_embedding.domain()
        generator_images = {
            label: self(source.module_generator(label))
            for label in source.module_generating_set()
        }
        match target:
            case _ if _has_finite_free_framing(target):
                preimages = {
                    label: target_embedding._preimage_or_none(image)
                    for label, image in generator_images.items()
                }
                if any(preimage is None for preimage in preimages.values()):
                    return None
            case _:
                preimages = {
                    label: target_embedding.preimage(image)
                    for label, image in generator_images.items()
                }
        return source.module_category().Mor(source, target)(preimages)

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
        self._require_established_linearity("lifting to selected presentations")
        from dzack_research.preamble.categories.modules.pure.modules import (
            ModulesWithChosenFinitePresentation,
        )

        source = self.domain()
        target = self.codomain()
        ring = source.base_ring()
        assert source in ModulesWithChosenFinitePresentation(ring) and target in ModulesWithChosenFinitePresentation(ring), (
            "a selected-presentation morphism requires presented source and target"
        )

        source_presentation = source.presentation()
        target_presentation = target.presentation()
        source_cover = source_presentation.codomain()
        target_cover = target_presentation.codomain()

        def lift_target(element):
            return target_cover.linear_combination(target.framing_coefficients(element))

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

    def _preimage_through_the_extension_framing(self, element):
        r"""Return the preimage of ``element`` in a restriction of scalars to ``R``, or ``None``.

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
        return cleared_span._preimage_or_none(cleared(target_coordinates))

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
        r"""Extend this represented linear map along ``ring_map : R -> S``.

        The scalar-extension functor owns both object and morphism transport;
        this method is the module-morphism entry to that same action.
        """
        ring = self.domain().base_ring()
        assert self.codomain().base_ring() is ring and ring_map.domain() is ring, (
            "module-morphism base change requires one source scalar ring"
        )
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return Modules(ring).scalar_extension(ring_map)(self)

    def adic_completion(self, ideal, *, precision=20):
        r"""Return ``self tensor_R R_hat`` using one shared completion parent.

        The endpoint objects are the same completed modules returned by their
        module constructors; the scalar-extension functor adopts those exact
        images before transporting this morphism.
        """
        ring = self.domain().base_ring()
        assert self.codomain().base_ring() is ring, "adic completion of a module morphism requires one scalar ring"
        assert ideal.ring() is ring, "the completion ideal belongs to the morphism scalar ring"
        completion = ring.adic_completion(ideal, precision=precision)
        return self.base_change_to_completion(completion)

    def base_change_to_completion(self, completion):
        r"""Return ``self tensor_R R_hat`` for one already selected completion."""
        ring = self.domain().base_ring()
        assert self.codomain().base_ring() is ring, "adic completion of a module morphism requires one scalar ring"
        assert completion.completion_source() is ring, "the completion has the source ring of this morphism"
        source = self.domain().base_change_to_completion(completion)
        target = self.codomain().base_change_to_completion(completion)

        from dzack_research.preamble.categories.modules.pure.modules import Modules

        extension = Modules(ring).scalar_extension(completion.completion_map())
        completed = extension(self)
        assert completed.domain() is source and completed.codomain() is target, (
            "scalar extension reuses the selected completed endpoint images"
        )
        return completed

    def completion_cokernel_comparison(self, ideal, *, precision=20):
        r"""Return the isomorphism ``coker(self) tensor R_hat ~= coker(self tensor R_hat)``.

        Completion of a Noetherian ring is flat, and scalar extension is right
        exact, so completing the cokernel commutes with taking it.  Both sides
        use one selected completion parent and are presented on the same
        generators; the isomorphism carries each generator to the generator of
        the same position.  It is an isomorphism of ``Modules(R_hat)``.
        """
        ring = self.domain().base_ring()
        completion = ring.adic_completion(ideal, precision=precision)
        assert completion.is_flat_over_source(), "the comparison uses flatness of the Noetherian completion"
        completed_morphism = self.base_change_to_completion(completion)
        completed_cokernel = self.cokernel().base_change_to_completion(completion)
        cokernel_after_completion = completed_morphism.cokernel()
        left_labels = completed_cokernel.module_generating_set()
        right_labels = cokernel_after_completion.module_generating_set()
        assert left_labels.cardinality() == right_labels.cardinality(), (
            "completion preserves the selected cokernel framing cardinality"
        )

        forward = completed_cokernel.module_category().Mor(completed_cokernel, cokernel_after_completion)(
            {label: cokernel_after_completion.module_generator(right_labels[int(left_labels.ranking_map()(label))]) for label in left_labels}
        )
        inverse = cokernel_after_completion.module_category().Mor(cokernel_after_completion, completed_cokernel)(
            {label: completed_cokernel.module_generator(left_labels[int(right_labels.ranking_map()(label))]) for label in right_labels}
        )
        return completed_cokernel.module_category().Core().Mor(
            completed_cokernel,
            cokernel_after_completion,
        )(forward, inverse)

    def _is_the_identity(self) -> bool:
        r"""Return whether this morphism is its Mor object's identity."""
        if self.domain() is not self.codomain():
            return False
        module = self.domain()
        return self is module.module_category().Mor(module, module).identity()

    def __mul__(self, other):
        r"""Return ``self . other`` for a composable arrow, or ``other * self`` for a scalar."""
        match other:
            case _ if other in self.parent().base_ring():
                return self.parent().scalar_multiple(other, self)
            case _ if not _precomposable(self, other):
                return NotImplemented
            case _:
                if other.parent() is self.parent() and self.domain() is self.codomain():
                    return self.parent()._compose_endomorphisms(self, other)
                source = other.domain()
                target = self.codomain()
                # The identity is a two-sided unit.  That is a theorem, so the
                # composite is the other factor itself rather than a fresh
                # morphism that would then have to be compared with it.
                if self._is_the_identity():
                    return other
                if other is source.module_category().Mor(source, source).identity():
                    return self
                mor = source.module_category().Mor(source, target)
                # Composition of certified linear maps is linear.  Keep that
                # theorem as construction data instead of rebuilding the
                # composite from all selected generator images and rechecking
                # the source relations.
                return _CompositeModuleMorphism(mor, self, other)

    @cached_method
    def cokernel(self):
        r"""Return the selected quotient ``codomain(self) / image(self)``.

        Scalar extension is right exact, so the cokernel of a completed
        morphism is the completion of the cokernel of its preimage.
        """
        self._require_established_linearity("cokernel construction")
        from dzack_research.preamble.categories.rings.commutative_algebra import (
            AdicCompletions,
        )

        extended_ring = self._flat_scalar_extension_ring()
        match extended_ring:
            case _ if extended_ring is not None and extended_ring in AdicCompletions():
                return self._scalar_extension_functor(self._scalar_extension_of.cokernel())
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

        self._require_established_linearity("splitting an epimorphism")
        codomain = self.codomain()
        assert self.is_surjective(), "only an epimorphism has a section"
        assert _has_finite_free_framing(codomain), "independent generator lifts define a section in the selected finite basis"
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

        self._require_established_linearity("splitting a monomorphism")
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
        matrix Mor is also the coordinate-matrix object, where inversion is
        the ordinary matrix operation and may extend coefficients to the
        computed inverse's scalar ring (for example ``ZZ`` to ``QQ``).
        """
        self._require_established_linearity("module-morphism inversion")
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
                            _owned_engine_element(result_ring, backend[row, column])
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
        automorphism group the Mor packet gives the module.  This states the
        endomorphism together with the inverse it constructs, which is what
        that group's elements are.
        """
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        module = self.domain()
        assert self.codomain() is module, "an automorphism is an endomorphism"
        return Modules(module.base_ring()).Aut(module)._from_known_inverse_pair(
            self,
            self.inverse(),
        )


def _combined_linearity_decision(morphisms):
    r"""Conjoin the linearity decisions of actual morphism premises."""
    match morphisms:
        case IndexedFamily():
            size = morphisms.cardinality()
            if not size.is_finite():
                return Unknown
        case _:
            pass
    decision = True
    for morphism in morphisms:
        current = morphism.linearity_decision()
        if current is False:
            return False
        if current is not True:
            decision = Unknown
    return decision


class _PointwiseSumModuleMorphism(ModuleMorphism):
    r"""The sum of two admitted module maps, with exactly their law premises."""

    def __init__(self, parent, left, right) -> None:
        self._left_summand = left
        self._right_summand = right
        super().__init__(
            parent,
            lambda element: left(element) + right(element),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return _combined_linearity_decision((self._left_summand, self._right_summand))


class _PointwiseNegationModuleMorphism(ModuleMorphism):
    r"""The additive inverse of an admitted module map."""

    def __init__(self, parent, morphism) -> None:
        self._negated_morphism = morphism
        super().__init__(parent, lambda element: -morphism(element), elementwise=True)

    def _elementwise_linearity_derivation(self):
        return self._negated_morphism.linearity_decision()


class _PointwiseScalarMultipleModuleMorphism(ModuleMorphism):
    r"""A scalar multiple of an admitted linear map, retaining its premise."""

    def __init__(self, parent, scalar, morphism) -> None:
        self._scalar = parent.base_ring()(scalar)
        self._scaled_morphism = morphism
        super().__init__(
            parent,
            lambda element: self.codomain().scalar_multiple(
                self._scalar,
                morphism(element),
            ),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return self._scaled_morphism.linearity_decision()


class _CompositeModuleMorphism(ModuleMorphism):
    r"""Composition of two admitted module maps with their law premises."""

    def __init__(self, parent, left, right) -> None:
        self._left_factor = left
        self._right_factor = right
        super().__init__(parent, lambda element: left(right(element)), elementwise=True)

    def _elementwise_linearity_derivation(self):
        return _combined_linearity_decision((self._left_factor, self._right_factor))


class _TransportedModuleMorphism(ModuleMorphism):
    r"""The same module map viewed in another Mor parent with the same endpoints."""

    def __init__(self, parent, morphism) -> None:
        self._transported_morphism = morphism
        super().__init__(parent, lambda element: morphism(element), elementwise=True)

    def _elementwise_linearity_derivation(self):
        return self._transported_morphism.linearity_decision()


class _ScalarIdentityModuleMorphism(ModuleMorphism):
    r"""The scalar multiple of the identity, linear by the module action."""

    def __init__(self, parent, scalar) -> None:
        from dzack_research.preamble.categories.group.additive_mors import _ScalarIdentityEvaluation

        evaluation = _ScalarIdentityEvaluation(parent, scalar)
        super().__init__(parent, evaluation, elementwise=True)

    def _elementwise_linearity_derivation(self):
        return True


class _ZeroModuleMorphism(ModuleMorphism):
    r"""The zero map between two modules, linear by the zero element laws."""

    def __init__(self, parent) -> None:
        super().__init__(
            parent,
            lambda _element: self.codomain().zero(),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return True


class _ProductProjectionModuleMorphism(ModuleMorphism):
    r"""Projection from a set-created module product, linear by componentwise construction."""

    def __init__(self, parent, underlying_projection) -> None:
        self._underlying_projection = underlying_projection
        super().__init__(
            parent,
            lambda element: self.codomain()(
                underlying_projection(element.underlying_element())
            ),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return True


class _ProductFactorModuleMorphism(ModuleMorphism):
    r"""Product factor induced by a cone of linear maps, hence linear componentwise."""

    def __init__(self, parent, underlying_factor, legs) -> None:
        self._underlying_factor = underlying_factor
        self._legs = legs
        super().__init__(
            parent,
            lambda element: self.codomain()(underlying_factor(element)),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return _combined_linearity_decision(self._legs)


class _EqualizerInclusionModuleMorphism(ModuleMorphism):
    r"""The inclusion of a set-created equalizer with inherited module operations."""

    def __init__(self, parent, underlying_inclusion, parallel_maps) -> None:
        self._underlying_inclusion = underlying_inclusion
        self._parallel_maps = parallel_maps
        super().__init__(
            parent,
            lambda element: self.codomain()(
                underlying_inclusion(element.underlying_element())
            ),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return _combined_linearity_decision(self._parallel_maps)


class _EqualizerFactorModuleMorphism(ModuleMorphism):
    r"""The unique linear factor through an equalizer inclusion."""

    def __init__(self, parent, source_leg, inclusion=None) -> None:
        self._source_leg = source_leg
        self._equalizer_inclusion = inclusion

        def factor(element):
            image = source_leg(element)
            match inclusion:
                case None:
                    return self.codomain()(image)
                case _:
                    return inclusion.lift(image)

        super().__init__(parent, factor, elementwise=True)

    def _elementwise_linearity_derivation(self):
        dependencies = [self._source_leg]
        match self._equalizer_inclusion:
            case None:
                pass
            case inclusion:
                dependencies.append(inclusion)
        return _combined_linearity_decision(dependencies)


class FramingMorphism(ModuleMorphism):
    r"""The selected framing epimorphism from a free module."""

    def __init__(self, parent, generator_morphism) -> None:
        codomain = parent.codomain()
        if parent.domain() is not codomain.framing_source():
            raise ValueError("a framing morphism has the module's selected free source")
        if generator_morphism is not codomain.module_generator_morphism():
            raise ValueError("a framing morphism realizes the module's selected generator map")
        super().__init__(parent, generator_morphism)

    def lift(self, element):
        r"""Lift through the selected framing using its constructor-owned coefficients."""
        target = self.codomain()(element)
        candidate = self.domain().linear_combination(
            self.codomain().framing_coefficients(target)
        )
        if self(candidate) != target:
            raise ValueError("the selected framing coefficients do not lift this element")
        return candidate

    def is_surjective(self) -> bool:
        r"""True: the codomain's framing coefficients supply a preimage in the selected free source."""
        return True


class ModuleEmbedding(ModuleMorphism):
    r"""An admitted injective module morphism."""

    def _injectivity_derivation(self):
        r"""Return a construction-derived injectivity decision, or ``None``."""
        return None

    def __init__(self, parent, images, **options) -> None:
        ModuleMorphism.__init__(self, parent, images, **options)
        if self.linearity_decision() is not True:
            raise ValueError("linearity is not established for this proposed module embedding")
        decision = self._injectivity_derivation()
        if decision is None:
            decision = ModuleMorphism.is_injective(self)
        if decision is False:
            raise ValueError("the supplied module morphism is not injective")
        if decision is not True:
            raise ValueError("injectivity is not established for this module morphism")
        self._injectivity_decision = True

    def is_injective(self) -> bool:
        return self._injectivity_decision


class _SubobjectInclusionModuleMorphism(ModuleEmbedding):
    r"""The inclusion carried by an already-constructed module subobject."""

    def _elementwise_linearity_derivation(self):
        return True

    def _injectivity_derivation(self):
        return True


def _module_subobject_inclusion(parent, images, *, lift=None):
    r"""Admit the inclusion carried by an already-constructed module subobject."""
    return _SubobjectInclusionModuleMorphism(parent, images, lift=lift)


class _TransportedModuleEmbedding(ModuleEmbedding):
    r"""An existing admitted embedding viewed in another Mono parent."""

    def __init__(self, parent, embedding, *, lift=None) -> None:
        self._transported_embedding = embedding
        self._transported_lift_is_exact = (
            lift is None
            and embedding.has_selected_lift()
            and embedding.selected_lift_exactness_decision() is True
        )
        super().__init__(
            parent,
            lambda element: embedding(element),
            elementwise=True,
            lift=(embedding._lift_function if lift is None else lift),
        )

    def _elementwise_linearity_derivation(self):
        return self._transported_embedding.linearity_decision()

    def _injectivity_derivation(self):
        return True

    def _selected_lift_derivation(self):
        return True if self._transported_lift_is_exact else None


class _ModuleMorphismProposedAsEmbedding(ModuleEmbedding):
    r"""A known linear map submitted to the Mono owner for injectivity admission."""

    def __init__(self, parent, morphism, *, lift=None) -> None:
        self._proposed_morphism = morphism
        super().__init__(
            parent,
            lambda element: morphism(element),
            elementwise=True,
            lift=lift,
        )

    def _elementwise_linearity_derivation(self):
        return self._proposed_morphism.linearity_decision()


class ModuleEmbeddingMor(CategoricalMor):
    r"""The declared monomorphisms between two modules over one scalar ring."""

    Element = ModuleEmbedding

    def __init__(self, mor_family, domain, codomain) -> None:
        modules = domain.module_category()
        assert domain in modules and codomain in modules, (
            "a module embedding Mor requires two modules over one scalar ring"
        )
        CategoricalMor.__init__(self, mor_family, domain, codomain)

    def _element_constructor_(self, images, *, lift=None):
        if isinstance(images, ModuleEmbedding):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the module embedding has the wrong endpoints")
            if images.parent() is self:
                return images
            return _TransportedModuleEmbedding(self, images, lift=lift)
        if isinstance(images, ModuleMorphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the module morphism has the wrong embedding endpoints")
            return _ModuleMorphismProposedAsEmbedding(self, images, lift=lift)
        return self.element_class(
            self,
            images,
            lift=lift,
        )

    def _subobject_inclusion(self, images, *, lift=None):
        r"""Construct the inclusion carried by an owned module-subobject datum."""
        return _module_subobject_inclusion(self, images, lift=lift)

    def base_ring(self):
        return self.domain().base_ring()

    def scalar_multiple(self, scalar, morphism):
        r"""Scale an embedding in the underlying linear Mor.

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
        return [packet.Mors().Of(source, target), *inherited]

    def _repr_(self):
        return f"Emb({self.domain()}, {self.codomain()})"


def _initialize_module_mor_parent(
    parent,
    mor_family,
    domain,
    codomain,
    *,
    full_internal_mor=False,
) -> None:
    r"""Install the common enriched ``R``-module Mor parent semantics.

    This is implementation reuse only.  Structured Mor categories such as
    ``Hom_{R[G]}`` must not subclass ``Hom_R`` as Python classes merely because
    they have ``Hom_R`` as a categorical supercategory.
    """
    modules = mor_family.base_category()
    ring = modules.base_ring()
    assert domain in modules and codomain in modules, (
        f"a Mor of {modules} has two of its objects as endpoints; got {domain} and {codomain}"
    )
    placement = domain.module_category()._mor_parent_placement(
        domain,
        codomain,
        full_internal_mor=full_internal_mor,
    )
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _SelectedFinitePresentationModules,
        _fix_selected_module_presentation,
    )
    from dzack_research.preamble.categories.modules.pure.modules import (
        MatrixSpaces,
        _fix_selected_module_framing,
        _matrix_unit,
    )

    # Fix all chosen data before the mixed Sage Mor is initialized and then
    # refined into its owned enrichment.  The generator-map callables below are
    # representations of those fixed data and are evaluated only after the
    # parent exists; no accessor can choose another framing or presentation.
    match placement:
        case _ if ring in OwnedRings().Commutative() and placement.is_subcategory(MatrixSpaces(ring)):
            # ``Hom_R(F_R(S), F_R(T))`` is free on the matrix units ``T x S``.
            labels = codomain.module_generating_set().product_with(domain.module_generating_set())
            _fix_selected_module_framing(
                parent,
                ring,
                labels,
                lambda label: _matrix_unit(parent, label),
                ring._fresh_free_module_on(labels),
            )
        case _ if placement.is_subcategory(_SelectedFinitePresentationModules(ring)):
            # ``Hom_R(M, N)`` between presented modules is presented by the
            # model its endpoints determine (see ``internal_mor``).
            from dzack_research.preamble.categories.modules.internal_mor import (
                __internal_mor_model_data_from_endpoints,
            )

            model, _inclusion, relation_matrix, presentation = __internal_mor_model_data_from_endpoints(
                domain,
                codomain,
            )
            _fix_selected_module_framing(
                parent,
                ring,
                model.module_generating_set(),
                lambda label: parent._morphism_from_internal_model(model.module_generator(label)),
                model.framing_source(),
            )
            _fix_selected_module_presentation(
                parent,
                ring,
                relation_matrix,
                presentation,
            )

    CategoricalMor.__init__(
        parent,
        mor_family,
        domain,
        codomain,
        category=placement,
        base=ring.ring_center(),
    )

    if domain is codomain:
        from dzack_research.preamble.categories.algebras.algebras import _algebra_from_native_ring

        # Construct composition in this exact parent; asking the Mor factory
        # for these same endpoints while it is still constructing would
        # recursively allocate another copy before it can be cached.
        _algebra_from_native_ring(
            parent,
            parent._compose_endomorphisms,
            _ModuleMorCommonMethods.identity(parent),
            lambda scalar, arrow: _ModuleMorCommonMethods._owned_scalar_multiple(parent, scalar, arrow),
        )


class _ModuleMorCommonMethods:
    r"""Python implementation shared by module-enriched Mor parents.

    This is not a mathematical Mor category.  Concrete Mor parents remain
    distinct categories and use this class only to share ordinary module-Mor
    operations.
    """

    def _element_constructor_(self, images):
        from dzack_research.preamble.categories.modules.pure.modules import MatrixSpaces

        if (
            self in MatrixSpaces(self.base_ring())
            and isinstance(images, (tuple, list))
            and len(images) == self.nrows()
            and all(isinstance(row, (tuple, list)) for row in images)
        ):
            return self.from_rows(images)
        if isinstance(images, ModuleMorphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the morphism has the wrong Mor source or target")
            if images.parent() is self:
                return images
            if images.linearity_decision() is not True:
                return _TransportedModuleMorphism(self, images)
            if not self.domain().is_framed_module():
                return _TransportedModuleMorphism(self, images)
            images = {label: images(self.domain().module_generator(label)) for label in self.domain().module_generating_set()}
        elif isinstance(images, Morphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the morphism has the wrong Mor source or target")
            return self.elementwise(lambda element: images(element))
        base_ring = self.base_ring()
        if self.domain() is self.codomain() and (images in base_ring or images in _engine_ring(base_ring)):
            scalar = base_ring(images)
            return self.scalar_multiple(scalar, self.identity())
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            _SelectedFinitePresentationModules,
        )

        if self in _SelectedFinitePresentationModules(base_ring) and images in self._internal_mor_model():
            return self._morphism_from_internal_model(self._internal_mor_model()(images))
        return self.element_class(self, images)

    def is_projective(self):
        r"""Answer ``Unknown`` for a Mor module with neither a matrix nor a presented model.

        A matrix space is free on its matrix units and a Mor between modules
        with chosen finite presentations is decided from its presented model;
        both answer through their placement.  The Mor modules reaching this
        method have neither, and projectivity is not decided for them.
        """
        from sage.misc.unknown import Unknown

        return Unknown

    def _apply_pointwise_scalar(self, scalar, element):
        return self.codomain().scalar_multiple(self.base_ring()(scalar), element)

    def _scalar_identity(self, scalar):
        return _ScalarIdentityModuleMorphism(self, scalar)

    def _compose_endomorphisms(self, left, right):
        r"""Compose endomorphisms while retaining both module-linearity premises."""
        from dzack_research.preamble.categories.group.additive_mors import (
            _scalar_identity_coefficient,
        )

        left_scalar = _scalar_identity_coefficient(left)
        right_scalar = _scalar_identity_coefficient(right)
        if left_scalar is not None and right_scalar is not None:
            return self._scalar_identity(left_scalar * right_scalar)
        return _CompositeModuleMorphism(self, left, right)

    def _owned_scalar_multiple(self, scalar, morphism):
        r"""Realize the pointwise action defining this Mor's scalar enrichment."""
        if morphism.parent() is not self:
            morphism = self(morphism)
        scalar = self.base_ring()(scalar)
        from dzack_research.preamble.categories.group.additive_mors import _scalar_identity_coefficient

        coefficient = _scalar_identity_coefficient(morphism)
        if coefficient is not None:
            return self._scalar_identity(scalar * coefficient)
        return _PointwiseScalarMultipleModuleMorphism(self, scalar, morphism)

    def elementwise(self, function):
        r"""Construct a declared linear map from its action on arbitrary elements.

        Exact verification is performed when the represented source/scalar
        underlying sets make it decidable (notably finite ones).  Otherwise the
        callable is retained with ``Unknown`` linearity and a DEBUG diagnostic
        records that no decision procedure was available.  For finitely
        generated/presented objects, prefer the
        generator-assignment constructor when possible: its linear extension
        is linear by construction and presentation relations are checked.
        """
        if not callable(function):
            raise TypeError("an elementwise module map must be callable")
        return self.element_class(
            self,
            function,
            elementwise=True,
        )

    def _product_projection(self, underlying_projection):
        r"""Admit the projection created by the underlying-set module product."""
        return _ProductProjectionModuleMorphism(self, underlying_projection)

    def _product_factor(self, underlying_factor, legs):
        r"""Admit the factor induced by a cone into a componentwise module product."""
        return _ProductFactorModuleMorphism(self, underlying_factor, legs)

    def _equalizer_inclusion(self, underlying_inclusion, parallel_maps):
        r"""Admit the inclusion created by the underlying-set equalizer."""
        return _EqualizerInclusionModuleMorphism(
            self,
            underlying_inclusion,
            parallel_maps,
        )

    def _equalizer_factor(self, source_leg, *, inclusion=None):
        r"""Admit the universal factor through a represented module equalizer."""
        return _EqualizerFactorModuleMorphism(
            self,
            source_leg,
            inclusion=inclusion,
        )

    def zero(self):
        if self.domain() is self.codomain():
            return self._scalar_identity(self.base_ring().zero())
        return _ZeroModuleMorphism(self)

    @cached_method
    def identity(self):
        r"""Return the identity of this endomorphism Mor.

        A Mor object has one identity.  Returning a fresh morphism on each call
        makes it incomparable with itself, since module-morphism equality is
        not decidable without a chosen finite presentation of the source.
        """
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism Mor")
        return self._scalar_identity(self.base_ring().one())

    def one(self):
        r"""Return the multiplicative unit when this is an endomorphism ring."""
        return self.identity()


class _AuxiliaryLinearModuleMor(_ModuleMorCommonMethods, CategoricalMor):
    r"""Private linear-Mor parent used while realizing an internal Mor module.

    This parent represents a linear arrow space needed by an algorithm.  It is
    deliberately placed only in ``LinearMorModules(R)`` and therefore cannot
    recursively demand another internal-Mor module presentation.
    """

    Element = ModuleMorphism

    def __init__(self, domain, codomain) -> None:
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        modules = Modules(_owned_ring(domain.base_ring()))
        _initialize_module_mor_parent(
            self,
            modules.MorCategory(),
            domain,
            codomain,
            full_internal_mor=False,
        )

    def __call__(self, images):
        return self._element_constructor_(images)


def _auxiliary_linear_module_mor(domain, codomain):
    return _AuxiliaryLinearModuleMor(domain, codomain)


class ModuleMor(_ModuleMorCommonMethods, CategoricalMor):
    Element = ModuleMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        _initialize_module_mor_parent(
            self,
            mor_family,
            domain,
            codomain,
            full_internal_mor=True,
        )

    def __call__(self, images):
        r"""Construct a module morphism without Sage coercion discovery."""
        return self._element_constructor_(images)

    def presentation_matrix(self):
        r"""Return the relation rows of the presented model of this Mor module."""
        from dzack_research.preamble.categories.modules.internal_mor import (
            __internal_mor_model_data,
        )

        _model, _inclusion, relation_matrix, _presentation = __internal_mor_model_data(self)
        return relation_matrix

    def presentation(self):
        r"""Return the presentation of the presented model of this Mor module."""
        from dzack_research.preamble.categories.modules.internal_mor import (
            __internal_mor_model_data,
        )

        _model, _inclusion, _relation_matrix, presentation = __internal_mor_model_data(self)
        return presentation

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
        return f"Mor({self.domain()}, {self.codomain()})"


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

    def _injectivity_derivation(self):
        return True

    def is_in_image(self, element) -> bool:
        r"""Return whether ``element`` is supported on the smaller framing."""
        if element.parent() is not self.codomain():
            return False
        source_labels = self.domain().module_generating_set()
        return all(
            label in source_labels
            for label in self.codomain().framing_coefficients(element).index_set()
        )

    def lift(self, element):
        r"""Return the unique element of the smaller free module mapping here."""
        assert self.is_in_image(element), f"{element} is not in the image of {self}"
        return self.domain().linear_combination(self.codomain().framing_coefficients(element))


def _framing_morphism(codomain) -> FramingMorphism:
    domain = codomain.framing_source()
    mor = domain.module_category().Mor(domain, codomain)
    framing = FramingMorphism(mor, codomain.module_generator_morphism())
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


class _FramedTensorBilinearEvaluationMorphism(TensorProductModuleMorphism):
    r"""Conditional classifier of a two-variable evaluation on framed factors.

    The selected tensor framing determines the only possible linear extension
    from the values on pairs of factor generators, and ordinary module-Mor
    admission still rejects any selected tensor relation that those values do
    not kill.  A Python callable, however, does not establish that its values
    on arbitrary factor elements agree with that bilinear extension.  Retain
    that bilinearity premise as ``Unknown`` instead of promoting agreement on
    the selected framing to a proof.
    """

    def __init__(self, parent, evaluation) -> None:
        self._bilinear_evaluation = evaluation
        source = parent.domain()
        left = source.tensor_factor(0)
        right = source.tensor_factor(1)

        def generator_image(pair):
            value = evaluation(
                left.module_generator(pair.component(0)),
                right.module_generator(pair.component(1)),
            )
            match element_parent(value) is parent.codomain():
                case True:
                    return value
                case False:
                    return parent.codomain()(value)

        super().__init__(parent, generator_image)
        self._linearity_decision = Unknown

    def __call__(self, *arguments):
        match len(arguments):
            case 2:
                left, right = arguments
                value = self._bilinear_evaluation(
                    self.left_module()(left),
                    self.right_module()(right),
                )
                match element_parent(value) is self.codomain():
                    case True:
                        return value
                    case False:
                        return self.codomain()(value)
            case _:
                return super().__call__(*arguments)



class ModuleAutomorphism(CategoricalIsomorphism):
    r"""An invertible module endomorphism, as an element of ``Aut_R(M)``."""

    def as_morphism(self):
        return self.forward()

    def order(self):
        forward = self.forward()
        linear = forward.domain().module_category().Mor(
            forward.domain(), forward.codomain()
        )(forward)
        from dzack_research.preamble.categories.modules.pure.modules import MatrixSpaces

        assert linear.parent() in MatrixSpaces(linear.parent().base_ring()), (
            "represented automorphism order currently requires a finite framed-free module"
        )
        return linear.multiplicative_order()

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
        r"""The group law ``(g, g^{-1}) (h, h^{-1}) = (gh, h^{-1} g^{-1})``, or ``g . f`` for a module map ``f``."""
        match other:
            case _ if element_parent(other) is self.parent():
                return self.parent()._from_known_inverse_pair(
                    self.forward() * other.forward(),
                    other._inverse * self._inverse,
                )
            case _:
                return self.forward() * other


class _ConstructedModuleAutomorphism(ModuleAutomorphism):
    r"""An automorphism whose inverse equations follow from its construction."""

    def __init__(self, parent, forward, inverse) -> None:
        Morphism.__init__(self, parent)
        match (forward.domain() is self.domain(), forward.codomain() is self.codomain()):
            case (True, True):
                pass
            case _:
                raise ValueError("the forward module map has the wrong endpoints")
        match (inverse.domain() is self.codomain(), inverse.codomain() is self.domain()):
            case (True, True):
                pass
            case _:
                raise ValueError("the inverse module map has the wrong endpoints")
        self._forward = forward
        self._inverse = inverse


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


class ModuleAutomorphismGroup(CategoricalMor):
    r"""The unit group of ``End_R(M)``, retaining its actual module maps.

    The inherited Mor containment distinguishes group elements from the
    categorical objects constructed on them. Both retain their construction
    placement; an invertible underlying endomorphism still enters the group
    through its constructor rather than becoming a group element by inspection.
    """

    Element = ModuleAutomorphism

    def __init__(self, mor_family, module) -> None:
        self._base_ring = _owned_ring(module.base_ring())
        CategoricalMor.__init__(
            self,
            mor_family,
            module,
            module,
            category=ModuleAutomorphismGroups(self._base_ring),
        )

    def base_ring(self):
        return self._base_ring

    def _from_known_inverse_pair(self, forward, inverse):
        module = self.domain()
        mor = module.module_category().Mor(module, module)
        forward = mor(forward)
        inverse = mor(inverse)
        return _ConstructedModuleAutomorphism(self, forward, inverse)

    def __call__(self, datum):
        r"""Construct an automorphism-group element rather than preserving a bare Iso arrow."""
        return self._element_constructor_(datum)

    def _element_constructor_(self, datum):
        if isinstance(datum, ModuleAutomorphism):
            if datum.parent() is self:
                return datum
            datum = datum.as_morphism()
        if isinstance(datum, CategoricalIsomorphism):
            module = self.domain()
            mor = module.module_category().Mor(module, module)
            return self.element_class(
                self,
                mor(datum.forward()),
                mor(datum.inverse()),
            )
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

    def is_finite(self):
        r"""A finite module has finitely many automorphisms; otherwise this is not decided here.

        An infinite module can have a finite automorphism group (``Aut_Z(Z)``
        has two elements), so finiteness of the module is sufficient and not
        necessary.
        """
        match self.module().is_finite():
            case True:
                return True
            case _:
                return Unknown

    def super_categories(self):
        packet = self.base_category().category_packet()
        module = self.domain()
        supers = [
            packet.Mors().Of(module, module),
            packet.Monos().Of(module, module),
            packet.Epis().Of(module, module),
        ]
        if self.aut_family() is not None:
            supers.append(packet.Ends().Of(module))
        return supers

    def _repr_(self):
        return f"Aut_{self.base_category()}({self.module()})"


class TensorProductModuleMor(ModuleMor):
    r"""The ordinary module Mor with tensor-domain bilinear constructor syntax."""

    Element = TensorProductModuleMorphism

    @staticmethod
    def _is_two_argument_callable(function) -> bool:
        r"""Whether ``function`` is a Python function of exactly two required positional arguments."""
        match function:
            case _ if isfunction(function) or ismethod(function):
                required = tuple(
                    parameter
                    for parameter in signature(function).parameters.values()
                    if parameter.kind in (Parameter.POSITIONAL_ONLY, Parameter.POSITIONAL_OR_KEYWORD)
                    and parameter.default is Parameter.empty
                )
                return len(required) == 2
            case _:
                return False

    def _element_constructor_(self, images):
        from dzack_research.preamble.categories.modules.pure.modules import FramedModules

        if self.domain() not in FramedModules(self.domain().base_ring()):
            if self._is_two_argument_callable(images):
                return self.domain().from_bilinear_map(self.codomain(), images)
            return super()._element_constructor_(images)
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
                return value if element_parent(value) is self.codomain() else self.codomain()(value)

            images = generator_image
        elif self._is_two_argument_callable(images):
            return self._from_bilinear_evaluation(images)
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
                return value if element_parent(value) is self.codomain() else self.codomain()(value)

            images = generator_image

        return super()._element_constructor_(images)

    def _from_bilinear_evaluation(self, evaluation):
        r"""Classify a stated bilinear evaluation without proving it from a framing sample."""
        match callable(evaluation):
            case True:
                return _FramedTensorBilinearEvaluationMorphism(self, evaluation)
            case False:
                raise TypeError("a bilinear evaluation must be callable")
