"""Linear maps between framed modules."""

import operator

from sage.categories.action import Action
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.sets_cat import Sets
from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.free_module import FreeModule_generic
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
)
from dzack_research.preamble.categories.rings import engine_ring
from dzack_research.preamble.tensors import tensor


def _solve_left_integrally(system, target, ring):
    r"""Return ``a`` with ``a*system = target`` over a PID, or raise.

    Smith normal form is used on the transpose so the divisibility conditions
    are conditions in the actual scalar ring rather than a rational solve
    followed by denominator inspection.
    """
    from dzack_research.preamble.tensors import Tensor, tensor

    if not isinstance(system, Tensor):
        system = tensor.matrix(ring, system)
    engine_smith, engine_left, engine_right = system.dual_tensor().smith_form()
    smith = tensor.matrix(ring, engine_smith)
    left = tensor.matrix(ring, engine_left)
    right = tensor.matrix(ring, engine_right)
    shifted = left * tensor.vector(ring, target)
    width = smith.ncols()
    solution = [ring.zero()] * width
    for index, value in enumerate(shifted):
        divisor = smith[index, index] if index < width else ring.zero()
        if divisor == 0:
            if value != 0:
                raise ValueError("the element is not in the image of this morphism")
            continue
        if not divisor.divides(value):
            raise ValueError("the element is not in the image over the base ring")
        solution[index] = ring(value / divisor)
    return right * tensor.vector(ring, solution)


def module_coefficients(element, module=None) -> dict:
    r"""Return coefficients in the selected framing of the stated module.

    ``module`` is normally ``element.parent()``.  It is explicit at facade
    boundaries such as number-field orders, whose Sage elements retain the
    number field as their concrete parent even when regarded as elements of
    the order.
    """
    if module is None:
        module = element.parent()
    coordinate_function = module.__dict__.get("_preamble_module_coordinate_function")
    if coordinate_function is not None:
        labels = tuple(module.module_generating_set())
        coordinates = tuple(coordinate_function(element))
        if len(coordinates) != len(labels):
            raise ValueError(
                "the selected module-coordinate function returned the wrong number of coordinates"
            )
        return {
            label: module.base_ring()(coefficient)
            for label, coefficient in zip(labels, coordinates, strict=True)
            if coefficient != 0
        }
    if hasattr(module, "module_over_extension") and hasattr(element, "underlying_element"):
        extension_module = module.module_over_extension()
        extension_ring = module.extension_ring()
        extension_coefficients = module_coefficients(
            element.underlying_element(),
            extension_module,
        )
        coefficients = {}
        for module_label, scalar in extension_coefficients.items():
            scalar_coefficients = module_coefficients(scalar, extension_ring)
            for scalar_label, coefficient in scalar_coefficients.items():
                coefficients[(scalar_label, module_label)] = module.base_ring()(coefficient)
        return coefficients
    if hasattr(module, "underlying_module") and hasattr(element, "underlying_element"):
        return module_coefficients(
            element.underlying_element(),
            module.underlying_module(),
        )
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        ModulesWithChosenFinitePresentation,
    )

    if module in ModulesWithChosenFinitePresentation(module.base_ring()):
        # ``FGP_Element.lift`` is the backend coordinate lift.  Keep this
        # boundary explicit: mathematically structured quotients may expose
        # separate semantic representatives without changing the engine's
        # coordinate protocol.  The covering module need not be the ambient
        # standard lattice: kernels and other exact constructions naturally
        # have a proper free submodule as their cover.  Coordinates therefore
        # belong to the selected basis of ``V()``, not to its ambient vector
        # coordinates.
        from sage.modules.fg_pid.fgp_element import FGP_Element

        coordinates = (
            module.V().coordinate_vector(FGP_Element.lift(element))
            if isinstance(element, FGP_Element)
            else module.coordinate_vector(element)
        )
        return {
            label: module.base_ring()(coefficient)
            for label, coefficient in zip(
                module.module_generating_set(),
                tuple(coordinates),
                strict=True,
            )
            if coefficient != 0
        }
    from dzack_research.preamble.categories.rings import OwnedOrders

    if module in OwnedOrders():
        labels = tuple(module.module_generating_set())
        engine = engine_ring(module)
        coordinates = (
            (SageZZ(element),)
            if engine is SageZZ
            else tuple(engine.coordinates(element))
        )
        return {
            label: coefficient
            for label, coefficient in zip(labels, coordinates, strict=True)
            if coefficient != 0
        }
    match module:
        case CombinatorialFreeModule():
            return dict(element.monomial_coefficients())
        case FreeModule_generic():
            labels = tuple(module.module_generating_set())
            return {
                label: coefficient
                for label, coefficient in zip(labels, tuple(element), strict=True)
                if coefficient != 0
            }
        case _:
            return dict(element.monomial_coefficients())


class ModuleMorphism(Morphism):
    r"""The linear extension of a function on a chosen module framing."""

    def __init__(self, parent, images, *, elementwise=False) -> None:
        Morphism.__init__(self, parent)
        self._element_function = None
        from dzack_research.preamble.categories.modules.framed.framed_modules import (
            FramedModules,
        )

        framed_domain = self.domain() in FramedModules(self.domain().base_ring())
        if elementwise or not framed_domain:
            if not callable(images):
                raise TypeError(
                    "a morphism from an unframed module must be supplied as an exact element map"
                )
            self._element_function = images
            self._generator_image = None
            self._generator_morphism = None
            return
        labels = self.domain().module_generating_set()
        set_homset = Hom(labels, self.codomain(), Sets())
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

    def _check_selected_domain_relations(self) -> None:
        if self._element_function is not None:
            return
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            ModulesWithChosenFinitePresentation,
        )

        domain = self.domain()
        if domain not in ModulesWithChosenFinitePresentation(domain.base_ring()):
            return
        zero = self.codomain().zero()
        labels = domain.module_generating_set()
        for row in domain.presentation_matrix().rows():
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
            lambda element: self(element) + other(element)
        )

    def __neg__(self):
        parent = self.parent()
        return parent.elementwise(
            lambda element: -self(element)
        )

    def __sub__(self, other):
        if not isinstance(other, ModuleMorphism):
            return NotImplemented
        return self + (-other)

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
        ``scalar * element`` therefore bypasses the module abstraction and can
        fail for number-field/order coefficients.  Expand the selected images
        in the codomain framing, multiply coefficients in the owned base ring,
        and let ``codomain.linear_combination`` perform the module action.
        """
        codomain = self.codomain()
        ring = codomain.base_ring()
        from dzack_research.preamble.categories.modules.framed.fraction_field_quotients import (
            FractionFieldQuotients,
        )

        if codomain in FractionFieldQuotients(ring):
            # K/a has a deliberately nonunique infinite framing, so expanding
            # a quotient class in that framing is neither canonical nor
            # necessary.  Its native additive group and R-action are exact.
            return sum(
                (
                    ring(source_coefficient)
                    * self._generator_image(source_label)
                    for source_label, source_coefficient in coefficients.items()
                ),
                codomain.zero(),
            )
        from dzack_research.preamble.categories.modules.framed.framed_modules import (
            FramedModules,
        )

        if codomain not in FramedModules(ring):
            return sum(
                (
                    ring(source_coefficient) * self._generator_image(source_label)
                    for source_label, source_coefficient in coefficients.items()
                ),
                codomain.zero(),
            )
        engine = engine_ring(ring)
        accumulated = {}
        for source_label, source_coefficient in coefficients.items():
            image_coefficients = module_coefficients(
                self._generator_image(source_label), codomain
            )
            for target_label, image_coefficient in image_coefficients.items():
                contribution = engine(source_coefficient) * engine(image_coefficient)
                accumulated[target_label] = (
                    accumulated.get(target_label, engine.zero()) + contribution
                )
        return codomain.linear_combination(
            {
                label: coefficient
                for label, coefficient in accumulated.items()
                if coefficient != 0
            }
        )

    def _call_(self, element):
        if element.parent() is not self.domain():
            element = self.domain()(element)
        if self._element_function is not None:
            image = self._element_function(element)
            return image if image.parent() is self.codomain() else self.codomain()(image)
        coefficients = module_coefficients(element, self.domain())
        return self._linear_combination_of_generator_images(coefficients)

    def tensor(self):
        r"""Return the type-``(1,1)`` coordinate tensor of this linear map.

        With the selected framings this is a type-``(1,1)`` tensor, so it acts
        on a coordinate vector by left contraction: ``M * v``.  Raw Sage
        matrices are reserved for private computational crossings.
        """
        if self._generator_image is None:
            raise NotImplementedError(
                "coordinate tensors require selected framings on the source and target"
            )
        domain_labels = tuple(self.domain().module_generating_set())
        codomain_labels = tuple(self.codomain().module_generating_set())
        columns = []
        for label in domain_labels:
            image = self._generator_image(label)
            coefficients = module_coefficients(image, self.codomain())
            columns.append(
                [
                    coefficients[target_label]
                    if target_label in coefficients
                    else self.codomain().base_ring().zero()
                    for target_label in codomain_labels
                ]
            )
        if not columns:
            return tensor.matrix(
                engine_ring(self.domain().base_ring()),
                len(codomain_labels),
                0,
            )
        if not codomain_labels:
            return tensor.matrix(
                engine_ring(self.domain().base_ring()),
                0,
                len(domain_labels),
            )
        rows = tuple(zip(*columns, strict=True))
        return tensor.matrix(
            engine_ring(self.domain().base_ring()),
            rows,
        )

    def matrix(self):
        r"""Return the linear-map tensor in the selected framings.

        Kept as the familiar coordinate spelling; the returned object is a
        typed tensor, not a raw Sage matrix.
        """
        return self.tensor()

    def kernel(self):
        r"""Return ``ker(self)`` as a subobject of the domain."""
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
            FinitelyGeneratedFreeModules,
        )

        ring = self.domain().base_ring()
        assert (
            self.domain() in FinitelyGeneratedFreeModules(ring)
            and self.codomain() in FinitelyGeneratedFreeModules(ring)
        )
        rows = self.tensor().dual_tensor().left_kernel().basis_matrix().rows()
        return self.domain().subobject_on(
            self.domain().linear_combination(
                {
                    label: coefficient
                    for label, coefficient in zip(
                        self.domain().module_generating_set(), row, strict=True
                    )
                    if coefficient
                }
            )
            for row in rows
        )

    def image(self):
        r"""Return ``im(self)`` as a subobject of the codomain."""
        from sage.rings.infinity import Infinity

        assert self.domain().rank() != Infinity
        return self.codomain().subobject_on(
            self(self.domain().module_generator(label))
            for label in self.domain().module_generating_set()
        )

    def is_injective(self) -> bool:
        r"""Return whether ``ker(self)=0`` when the kernel is computable."""
        return self.kernel().rank() == 0

    def is_surjective(self) -> bool:
        r"""Return whether ``coker(self)=0`` when the cokernel is computable."""
        return self.cokernel().is_zero()

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
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
            FinitelyGeneratedFreeModules,
        )

        ring = self.domain().base_ring()
        assert (
            self.domain() in FinitelyGeneratedFreeModules(ring)
            and self.codomain() in FinitelyGeneratedFreeModules(ring)
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
            self.tensor().dual_tensor(),
            target,
            engine_ring(ring),
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
        from dzack_research.preamble.categories.lattices import Lattices
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
            FormModules,
        )

        if codomain not in Lattices(ring) and codomain not in FormModules(ring):
            raise TypeError("orthogonal complement requires a formed codomain")
        if codomain not in Lattices(ring) and codomain.value_module() is not ring:
            raise TypeError("this orthogonal-complement construction requires a scalar-valued form")

        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
            BasedFreeModule,
        )
        from dzack_research.preamble.categories.sets import finite_ordered_set

        source_generators = tuple(self.domain().module_generators())
        target_labels = finite_ordered_set(range(len(source_generators)))
        target = BasedFreeModule(ring, target_labels)
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

    def __mul__(self, other):
        if isinstance(other, ModuleMorphism):
            if other.codomain() is not self.domain():
                return NotImplemented
            homset = module_homset(other.domain(), self.codomain())
            from dzack_research.preamble.categories.modules.framed.framed_modules import (
                FramedModules,
            )

            if other.domain() in FramedModules(other.domain().base_ring()):
                return homset(
                    lambda label: self(
                        other(other.domain().module_generator(label))
                    )
                )
            return homset.elementwise(lambda element: self(other(element)))
        try:
            return self.parent().scalar_multiple(other, self)
        except (TypeError, ValueError):
            return NotImplemented

    def cokernel(self):
        r"""Return the selected quotient ``codomain(self) / image(self)``."""
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            FinitelyPresentedModule,
        )

        quotient = FinitelyPresentedModule(self)
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
    from dzack_research.preamble.categories.rings import owned_ring_view

    parent._preamble_base_ring = owned_ring_view(domain.base_ring())
    CategoricalHomset.__init__(
        parent,
        hom_family,
        domain,
        codomain,
        homset_category=Sets(),
    )
    from dzack_research.preamble.categories.modules.internal_hom import (
        InternalHomModules,
        LinearHomModules,
    )
    from dzack_research.preamble.refine import refine

    placement = [LinearHomModules(parent._preamble_base_ring)]
    if full_internal_hom:
        placement.append(InternalHomModules(parent._preamble_base_ring))
    refine(parent, placement)
    scalar_parent = engine_ring(parent._preamble_base_ring)
    parent.register_action(_ModuleHomScalarAction(scalar_parent, parent, True))
    parent.register_action(_ModuleHomScalarAction(scalar_parent, parent, False))


class ModuleHomset(CategoricalHomset):
    Element = ModuleMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        _initialize_module_hom_parent(
            self,
            hom_family,
            domain,
            codomain,
            full_internal_hom=True,
        )

    def _element_constructor_(self, images):
        if isinstance(images, ModuleMorphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the morphism has the wrong Hom source or target")
            if images.parent() is self:
                return images
            from dzack_research.preamble.categories.modules.framed.framed_modules import (
                FramedModules,
            )

            if self.domain() not in FramedModules(self.base_ring()):
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
        if model is not None and (
            getattr(images, "parent", lambda: None)() is model
            or getattr(images, "parent", lambda: None)() is model.V()
        ):
            model_element = images if images.parent() is model else model(images)
            return self._morphism_from_internal_model(model_element)
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
            )
        )

    def elementwise(self, function):
        r"""Construct an exact linear map from its action on arbitrary elements.

        This is the representation used when no finite framing is selected.
        The caller is responsible for supplying an actual linear map; finite
        framed constructors continue to validate the selected generator data.
        """
        if not callable(function):
            raise TypeError("an elementwise module map must be callable")
        return self.element_class(self, function, elementwise=True)

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

    def _install_internal_hom_model(self, model, inclusion) -> None:
        self._preamble_internal_hom_model = model
        self._preamble_internal_hom_inclusion = inclusion
        self._preamble_module_generating_set = model.module_generating_set()
        self._preamble_relation_matrix = model.presentation_matrix()
        self._preamble_presentation = model.presentation()
        self._preamble_module_generator_function = (
            lambda label: self._morphism_from_internal_model(model.module_generator(label))
        )
        self._preamble_module_coordinate_function = (
            lambda morphism: tuple(
                model.coordinate_vector(self._internal_model_from_morphism(self(morphism)))
            )
        )
        self._preamble_module_from_coordinates_function = (
            lambda coordinates: self._morphism_from_internal_model(
                model._from_coordinates(coordinates)
            )
        )

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
        assignment = self.inclusion_into_generator_maps()(model_element)
        coefficients = module_coefficients(
            assignment,
            self.inclusion_into_generator_maps().codomain(),
        )
        return self(
            {
                source_label: self.codomain().linear_combination(
                    {
                        target_label: coefficients[(source_label, target_label)]
                        for target_label in self.codomain().module_generating_set()
                        if (source_label, target_label) in coefficients
                    }
                )
                for source_label in self.domain().module_generating_set()
            }
        )

    def _internal_model_from_morphism(self, morphism):
        model = self.internal_hom_model()
        power = self.inclusion_into_generator_maps().codomain()
        coefficients = {}
        for source_label in self.domain().module_generating_set():
            image = morphism(self.domain().module_generator(source_label))
            for target_label, coefficient in module_coefficients(
                image,
                self.codomain(),
            ).items():
                coefficients[(source_label, target_label)] = coefficient
        return model(power.linear_combination(coefficients))

    def zero(self):
        return self.elementwise(lambda _element: self.codomain().zero())

    def linear_combination(self, coefficients):
        result = self.zero()
        for label, coefficient in coefficients.items():
            if coefficient:
                result = result + self.scalar_multiple(
                    coefficient,
                    self.module_generator(label),
                )
        return result

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism homset")
        from dzack_research.preamble.categories.modules.framed.framed_modules import (
            FramedModules,
        )

        if self.domain() not in FramedModules(self.base_ring()):
            return self.elementwise(lambda element: element)
        labels = self.domain().module_generating_set()
        try:
            finite = labels.cardinality() in SageZZ
        except AttributeError:
            finite = False
        if finite:
            return self(
                {
                    label: self.domain().module_generator(label)
                    for label in labels
                }
            )
        return self.elementwise(lambda element: element)

    def one(self):
        r"""Return the multiplicative unit when this is an endomorphism ring."""
        return self.identity()

    def _repr_(self):
        return f"Hom({self.domain()}, {self.codomain()})"


def module_homset(domain, codomain) -> ModuleHomset:
    from dzack_research.preamble.categories.modules import Modules

    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError("module morphisms require a common base ring")
    return Modules(ring).Hom(domain, codomain)


def framing_morphism(domain, codomain, images) -> FramingMorphism:
    homset = module_homset(domain, codomain)
    framing = FramingMorphism(homset, images)
    return framing


def module_embedding(domain, codomain, images) -> ModuleEmbedding:
    r"""Construct a declared module monomorphism on a chosen framing."""
    return ModuleEmbedding(module_homset(domain, codomain), images)
