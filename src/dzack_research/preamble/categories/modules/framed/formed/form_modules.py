r"""Modules equipped with exact bilinear or quadratic forms."""

from sage.categories.category_types import Category_over_base
from sage.categories.homset import Homset
from sage.categories.modules import Modules as SageModules
from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.parent import Parent

from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing, engine_ring
from dzack_research.preamble.refine import refine


from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)


class FormMorphism(ModuleMorphism):
    r"""A linear morphism verified to preserve the equipped forms."""


class FormEmbedding(FormMorphism):
    r"""A form-preserving morphism declared to be a monomorphism."""

    def __init__(self, parent, images, *, quadratic: bool) -> None:
        FormMorphism.__init__(self, parent, images)
        self._quadratic = bool(quadratic)
        source = self.domain()
        target = self.codomain()
        generators = tuple(source.module_generators())
        if self._quadratic:
            probes = generators + tuple(
                left + right
                for index, left in enumerate(generators)
                for right in generators[index + 1 :]
            )
            if any(source.q(element) != target.q(self(element)) for element in probes):
                raise ValueError("the stated embedding does not preserve the quadratic form")
        elif any(
            source.b(left, right) != target.b(self(left), self(right))
            for left in generators
            for right in generators
        ):
            raise ValueError("the stated embedding does not preserve the bilinear form")

    def is_injective(self) -> bool:
        return True

    def is_quadratic(self) -> bool:
        return self._quadratic


def form_embedding(domain, codomain, images, *, quadratic: bool | None = None) -> FormEmbedding:
    r"""Construct a form-preserving monomorphism on a chosen framing.

    The underlying module homset checks linearity and the selected relations.
    The embedding specialization checks preservation of ``b`` or ``q`` on the
    finite framing.  This works for both represented :class:`FormModule`
    objects and discriminant-form objects, which intentionally have their own
    structured-category realization rather than being wrappers around one.
    """
    from dzack_research.preamble.categories.modules import module_homset

    if quadratic is None:
        from dzack_research.preamble.categories.modules.framed.formed.discriminant_modules import (
            DiscriminantQuadraticModules,
        )

        ring = domain.base_ring()
        quadratic = bool(
            domain in QuadraticFormModules(ring)
            or domain in DiscriminantQuadraticModules(ring)
        )
    return FormEmbedding(
        module_homset(domain, codomain),
        images,
        quadratic=quadratic,
    )


def _represented_value_module(formed_module):
    r"""Return the actual module object underlying a form's public value object.

    A scalar-valued form publicly takes values in the ring ``R``.  The ring
    facade is not itself forced into ``Modules(R)`` merely for implementation
    convenience; its canonical value-module realization is the rank-one
    module ``R`` over itself.  Genuine module-valued forms are returned
    unchanged.
    """
    from dzack_research.preamble.categories.modules import Modules, ring_as_module

    value = formed_module.value_module()
    ring = formed_module.base_ring()
    if value is ring:
        return ring_as_module(ring)
    if value in Modules(ring):
        return value
    raise TypeError(
        f"the form value object {value} has no represented {ring}-module structure"
    )


def _value_as_module_element(formed_module, value):
    represented = _represented_value_module(formed_module)
    if represented is formed_module.value_module():
        return represented(value)
    return represented.linear_combination(
        {0: engine_ring(formed_module.base_ring())(value)}
    )


def _value_from_module_element(formed_module, element):
    represented = _represented_value_module(formed_module)
    if represented is formed_module.value_module():
        return represented(element)
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_coefficients,
    )

    coefficients = module_coefficients(element, represented)
    ring = engine_ring(formed_module.base_ring())
    return ring(coefficients.get(0, ring.zero()))


class FormedModuleMorphism(Morphism):
    r"""A morphism of formed modules in one coefficient-ring fiber.

    The datum is a pair ``(f,h)`` with a module map on the underlying modules
    and a module map on the value objects, satisfying the form square.  The
    stricter :class:`FormMorphism` remains the separate notion where ``h`` is
    the identity and the form is preserved exactly.
    """

    def __init__(self, parent, module_morphism, value_morphism) -> None:
        Morphism.__init__(self, parent)
        if module_morphism.domain() is not self.domain():
            raise ValueError("the underlying module map has the wrong domain")
        if module_morphism.codomain() is not self.codomain():
            raise ValueError("the underlying module map has the wrong codomain")
        source_values = _represented_value_module(self.domain())
        target_values = _represented_value_module(self.codomain())
        if value_morphism.domain() is not source_values:
            raise ValueError("the value-module map has the wrong domain")
        if value_morphism.codomain() is not target_values:
            raise ValueError("the value-module map has the wrong codomain")
        self._module_morphism = module_morphism
        self._value_morphism = value_morphism
        self._check_form_square()

    def module_morphism(self):
        return self._module_morphism

    def value_morphism(self):
        return self._value_morphism

    def map_value(self, value):
        source_element = _value_as_module_element(self.domain(), value)
        return _value_from_module_element(
            self.codomain(), self.value_morphism()(source_element)
        )

    def _check_form_square(self) -> None:
        from dzack_research.preamble.categories.forms import (
            BilinearFormMorphism,
            QuadraticFormMorphism,
        )

        source_form = self.domain().form()
        target_form = self.codomain().form()
        source_generators = tuple(self.domain().module_generators())
        if isinstance(source_form, BilinearFormMorphism):
            if not isinstance(target_form, BilinearFormMorphism):
                raise TypeError("bilinear formed modules map to bilinear formed modules")
            commutes = all(
                self.map_value(source_form(left, right))
                == target_form(
                    self.module_morphism()(left), self.module_morphism()(right)
                )
                for left in source_generators
                for right in source_generators
            )
        elif isinstance(source_form, QuadraticFormMorphism):
            if not isinstance(target_form, QuadraticFormMorphism):
                raise TypeError("quadratic formed modules map to quadratic formed modules")
            probes = source_generators + tuple(
                left + right
                for index, left in enumerate(source_generators)
                for right in source_generators[index + 1 :]
            )
            commutes = all(
                self.map_value(source_form(element))
                == target_form(self.module_morphism()(element))
                for element in probes
            )
        else:
            raise TypeError("a formed morphism requires bilinear or quadratic forms")
        if not commutes:
            raise ValueError("the module and value maps do not commute with the form")

    def __call__(self, element):
        return self.module_morphism()(element)

    def _call_(self, element):
        return self.module_morphism()(element)

    def __mul__(self, other):
        if not isinstance(other, FormedModuleMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            raise ValueError("formed morphisms are not composable")
        return formed_module_homset(other.domain(), self.codomain())(
            (
                self.module_morphism() * other.module_morphism(),
                self.value_morphism() * other.value_morphism(),
            )
        )


class FormedModuleHomset(Homset):
    Element = FormedModuleMorphism

    def __init__(self, domain, codomain) -> None:
        if domain.base_ring() != codomain.base_ring():
            raise ValueError("fixed-fiber formed morphisms require one base ring")
        Homset.__init__(
            self,
            domain,
            codomain,
            category=SageModules(engine_ring(domain.base_ring())),
        )

    def _element_constructor_(self, datum):
        module_morphism, value_morphism = datum
        return self.element_class(self, module_morphism, value_morphism)

    def identity(self):
        from dzack_research.preamble.categories.modules import module_homset

        values = _represented_value_module(self.domain())
        return self(
            (
                module_homset(self.domain(), self.domain()).identity(),
                module_homset(values, values).identity(),
            )
        )


def formed_module_homset(domain, codomain) -> FormedModuleHomset:
    return FormedModuleHomset(domain, codomain)


def _base_change_element(module, changed_module, ring_map, element):
    r"""Transport one represented framed-module element along ``ring_map``.

    This is the elementwise form of the scalar-extension unit on the selected
    presentation.  It is used only to compose morphisms in different scalar
    fibers; the public scalar-extension object remains ``changed_module``.
    """
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_coefficients,
    )

    coefficients = module_coefficients(element, module)
    target_ring = engine_ring(changed_module.base_ring())
    return changed_module.linear_combination(
        {
            label: target_ring(ring_map(coefficient))
            for label, coefficient in coefficients.items()
        }
    )


class FiberedFormedModuleMorphism(Morphism):
    r"""A formed-module morphism over a coefficient-ring map ``g:S1 -> S2``.

    The actual linear data live in the target fiber, exactly as required by
    the Grothendieck/fibered-category formulation:

    ``module_morphism : S2 tensor_S1 L1 -> L2`` and
    ``value_morphism  : S2 tensor_S1 W1 -> W2``.

    The active scalar-extension backend currently materializes this for the
    scalar-valued finite-free formed objects supported by ``FormModule``'s
    ``base_change`` method.  Unsupported scalar extensions fail at object
    construction rather than being represented by a semilinear fiction.
    """

    def __init__(self, parent, module_morphism, value_morphism) -> None:
        Morphism.__init__(self, parent)
        changed = parent.base_changed_domain()
        if module_morphism.domain() is not changed:
            raise ValueError("the module map must start at the base-changed source")
        if module_morphism.codomain() is not self.codomain():
            raise ValueError("the module map has the wrong target formed module")
        source_values = _represented_value_module(changed)
        target_values = _represented_value_module(self.codomain())
        if value_morphism.domain() is not source_values:
            raise ValueError("the value map must start at the base-changed source value module")
        if value_morphism.codomain() is not target_values:
            raise ValueError("the value map has the wrong target value module")
        self._module_morphism = module_morphism
        self._value_morphism = value_morphism
        self._check_form_square()

    def ring_map(self):
        return self.parent().ring_map()

    def base_changed_domain(self):
        return self.parent().base_changed_domain()

    def module_morphism(self):
        return self._module_morphism

    def value_morphism(self):
        return self._value_morphism

    def map_value(self, value):
        changed = self.base_changed_domain()
        source_element = _value_as_module_element(changed, value)
        return _value_from_module_element(
            self.codomain(), self.value_morphism()(source_element)
        )

    def _check_form_square(self) -> None:
        from dzack_research.preamble.categories.forms import (
            BilinearFormMorphism,
            QuadraticFormMorphism,
        )

        changed = self.base_changed_domain()
        source_form = changed.form()
        target_form = self.codomain().form()
        generators = tuple(changed.module_generators())
        if isinstance(source_form, BilinearFormMorphism):
            if not isinstance(target_form, BilinearFormMorphism):
                raise TypeError("bilinear formed modules map to bilinear formed modules")
            commutes = all(
                self.map_value(source_form(left, right))
                == target_form(
                    self.module_morphism()(left), self.module_morphism()(right)
                )
                for left in generators
                for right in generators
            )
        elif isinstance(source_form, QuadraticFormMorphism):
            if not isinstance(target_form, QuadraticFormMorphism):
                raise TypeError("quadratic formed modules map to quadratic formed modules")
            probes = generators + tuple(
                left + right
                for index, left in enumerate(generators)
                for right in generators[index + 1 :]
            )
            commutes = all(
                self.map_value(source_form(element))
                == target_form(self.module_morphism()(element))
                for element in probes
            )
        else:
            raise TypeError("a fibered formed morphism requires a bilinear or quadratic form")
        if not commutes:
            raise ValueError("the base-changed module and value maps do not commute with the form")

    def _call_(self, element):
        r"""Apply the equivalent semilinear map to an element of the original source."""
        changed_element = _base_change_element(
            self.domain(),
            self.base_changed_domain(),
            self.ring_map(),
            element,
        )
        return self.module_morphism()(changed_element)

    def __call__(self, element):
        return self._call_(element)

    def __mul__(self, other):
        if not isinstance(other, FiberedFormedModuleMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            raise ValueError("fibered formed morphisms are not composable")
        composite_ring_map = self.ring_map() * other.ring_map()
        homset = fibered_formed_module_homset(
            other.domain(), self.codomain(), composite_ring_map
        )
        from dzack_research.preamble.categories.modules import module_homset

        direct_changed = homset.base_changed_domain()
        middle_changed = self.base_changed_domain()

        module_images = {}
        for label in other.domain().module_generating_set():
            other_source_generator = other.base_changed_domain().module_generator(label)
            middle_element = other.module_morphism()(other_source_generator)
            lifted_middle = _base_change_element(
                self.domain(), middle_changed, self.ring_map(), middle_element
            )
            module_images[label] = self.module_morphism()(lifted_middle)
        module_map = module_homset(direct_changed, self.codomain())(module_images)

        other_values = _represented_value_module(other.base_changed_domain())
        middle_values = _represented_value_module(self.domain())
        lifted_middle_values = _represented_value_module(middle_changed)
        direct_values = _represented_value_module(direct_changed)
        target_values = _represented_value_module(self.codomain())
        value_images = {}
        for label in direct_values.module_generating_set():
            # All currently materialized cross-fiber value objects are the
            # rank-one scalar module, but retain the generic framed spelling.
            source_value = other_values.module_generator(label)
            middle_value = other.value_morphism()(source_value)
            lifted_value = _base_change_element(
                middle_values,
                lifted_middle_values,
                self.ring_map(),
                middle_value,
            )
            value_images[label] = self.value_morphism()(lifted_value)
        value_map = module_homset(direct_values, target_values)(value_images)
        return homset((module_map, value_map))


class FiberedFormedModuleHomset(Homset):
    Element = FiberedFormedModuleMorphism

    def __init__(self, domain, codomain, ring_map) -> None:
        from dzack_research.preamble.categories.modules.base_change import (
            base_change_codomain,
        )

        target_ring = base_change_codomain(domain, ring_map)
        if target_ring != codomain.base_ring():
            raise ValueError("the coefficient map does not land at the target base ring")
        self._ring_map = ring_map
        self._base_changed_domain = domain.base_change(ring_map)
        Homset.__init__(self, domain, codomain, category=Sets())

    def ring_map(self):
        return self._ring_map

    def base_changed_domain(self):
        return self._base_changed_domain

    def _element_constructor_(self, datum):
        module_morphism, value_morphism = datum
        return self.element_class(self, module_morphism, value_morphism)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism homset")
        if not hasattr(self.ring_map(), "is_identity") or not self.ring_map().is_identity():
            raise ValueError("the fibered identity must lie over the identity ring map")
        from dzack_research.preamble.categories.modules import module_homset

        changed = self.base_changed_domain()
        module_map = module_homset(changed, self.domain())(
            {
                label: self.domain().module_generator(label)
                for label in self.domain().module_generating_set()
            }
        )
        source_values = _represented_value_module(changed)
        target_values = _represented_value_module(self.domain())
        value_map = module_homset(source_values, target_values)(
            {
                label: target_values.module_generator(label)
                for label in source_values.module_generating_set()
            }
        )
        return self((module_map, value_map))


def fibered_formed_module_homset(domain, codomain, ring_map) -> FiberedFormedModuleHomset:
    r"""Return formed morphisms ``domain -> codomain`` lying over ``ring_map``."""
    return FiberedFormedModuleHomset(domain, codomain, ring_map)


class PairedModules(Category_over_base):
    r"""Pairings \(X\otimes_R Y\to W\).

    An object is classified by an element of
    \(\operatorname{Hom}_R(X\otimes_R Y,W)\).  The diagonal \(X=Y\) is
    :class:`FormedModules`.
    """

    @staticmethod
    def __classcall__(cls, value_module):
        from sage.categories.rings import Rings as SageRings
        from dzack_research.preamble.categories.rings import owned_ring_view

        if value_module in SageRings():
            value_module = owned_ring_view(value_module)
        return Category_over_base.__classcall__(cls, value_module)

    @classmethod
    def _repr_object_names(cls):
        return "paired modules"

    def super_categories(self):
        return [Sets()]

    def _call_(self, pairing):
        from sage.categories.rings import Rings as SageRings
        from dzack_research.preamble.categories.rings import owned_ring_view

        codomain = pairing.codomain()
        if codomain in SageRings():
            codomain = owned_ring_view(codomain)
        if codomain is not self.base():
            raise TypeError(
                f"a pairing in {self} takes values in {self.base()}, not {pairing.codomain()}"
            )
        if pairing.left_module() is pairing.right_module():
            return _formed_module_from_pairing(pairing)
        return _heterogeneous_pairing(pairing)

    class ParentMethods:
        def pairing(self, left, right):
            r"""Evaluate the pairing on a pair of elements."""
            return self._pairing(left, right)

        def left_module(self):
            return self._pairing.left_module()

        def right_module(self):
            return self._pairing.right_module()

        def value_module(self):
            return self._pairing.codomain()


class FormedModules(Category_over_base):
    r"""Modules equipped with a bilinear form \(M\otimes_R M\to W\).

    This is the diagonal of :class:`PairedModules`: a pairing of a module
    with itself.
    """

    @staticmethod
    def __classcall__(cls, value_module):
        from sage.categories.rings import Rings as SageRings
        from dzack_research.preamble.categories.rings import owned_ring_view

        if value_module in SageRings():
            value_module = owned_ring_view(value_module)
        return Category_over_base.__classcall__(cls, value_module)

    @classmethod
    def _repr_object_names(cls):
        return "formed modules"

    def super_categories(self):
        return [PairedModules(self.base())]

    class ParentMethods:
        def b(self, left, right):
            return self.pairing(left, right)

        def q(self, element):
            return self.b(element, element)


class FormModules(OwnedCategoryOverBaseRing):
    r"""Modules over ``R`` equipped with a form."""

    @classmethod
    def _repr_object_names(cls):
        return "form modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def form(self):
            return self._form

        def unformed_module(self):
            r"""Return the module used to equip this represented formed object."""
            return self._preamble_unformed_module

        def forget_form_morphism(self):
            r"""Return the canonical module identification from the formed copy."""
            return self._preamble_forget_form_morphism

        def equip_form_morphism(self):
            r"""Return the inverse canonical module identification into the formed copy."""
            return self._preamble_equip_form_morphism

        def value_module(self):
            return self.form().codomain()

        def formed_hom(self, module_morphism, value_morphism):
            r"""Construct the general fixed-fiber formed morphism ``(f,h)``."""
            return formed_module_homset(self, module_morphism.codomain())(
                (module_morphism, value_morphism)
            )

        def fibered_formed_hom(self, codomain, ring_map, module_morphism, value_morphism):
            r"""Construct a formed morphism over a coefficient-ring map."""
            return fibered_formed_module_homset(self, codomain, ring_map)(
                (module_morphism, value_morphism)
            )

        def b(self, left, right):
            if left.parent() is not self or right.parent() is not self:
                raise TypeError("a form pairs two elements of one formed module")
            form = self.form()
            from dzack_research.preamble.categories.forms import QuadraticFormMorphism

            if isinstance(form, QuadraticFormMorphism):
                return form.b(left, right)
            return form(left, right)

        def gram_tensor(self):
            r"""Return the scalar Gram as its intrinsic type-``(0,2)`` tensor."""
            from dzack_research.preamble.categories.forms import QuadraticFormMorphism

            form = self.form()
            return (
                form.lift_form().gram_tensor()
                if isinstance(form, QuadraticFormMorphism)
                else form.gram_tensor()
            )

        def twist(self, scalar):
            from dzack_research.preamble.categories.forms import (
                BilinearFormMorphism,
                BilinearForms,
                QuadraticForms,
            )

            form = self.form()
            if isinstance(form, BilinearFormMorphism):
                if form._gram is not None:
                    scaled = [
                        [scalar * value for value in row]
                        for row in form.values_matrix()
                    ]
                    return FormModule(BilinearForms(self, self.value_module())(scaled))
                return FormModule(
                    BilinearForms(self, self.value_module())(
                        lambda left, right: scalar * form(left, right)
                    )
                )
            if form._lift is not None:
                scaled = [
                    [scalar * value for value in row]
                    for row in form.lift_form().values_matrix()
                ]
                return FormModule(QuadraticForms(self, self.value_module())(scaled))
            return FormModule(
                QuadraticForms(self, self.value_module())(
                    lambda element: scalar * form(element)
                )
            )

        def base_change(self, ring_map):
            r"""Base-change a scalar-valued finite free form along ``R -> S``."""
            from dzack_research.preamble.categories.forms import (
                BilinearFormMorphism,
                BilinearForms,
                QuadraticFormMorphism,
                QuadraticForms,
            )
            from dzack_research.preamble.categories.modules import FreeModuleOn
            from dzack_research.preamble.categories.modules.base_change import (
                base_change_codomain,
                base_change_scalar,
            )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_coefficients,
            )

            assert self.value_module() is self.base_ring()
            target_ring = base_change_codomain(self, ring_map)
            changed = FreeModuleOn(target_ring, self.module_generating_set())
            source_generators = tuple(self.module_generators())
            form = self.form()
            if isinstance(form, BilinearFormMorphism):
                values = [
                    [
                        base_change_scalar(ring_map, form(left, right))
                        for right in source_generators
                    ]
                    for left in source_generators
                ]
                return FormModule(BilinearForms(changed, target_ring)(values))
            if not isinstance(form, QuadraticFormMorphism):
                raise TypeError(f"{form} is not a bilinear or quadratic form")
            diagonal = tuple(
                base_change_scalar(ring_map, form(generator))
                for generator in source_generators
            )
            polar = tuple(
                tuple(
                    base_change_scalar(ring_map, form.b(left, right))
                    for right in source_generators
                )
                for left in source_generators
            )
            labels = tuple(changed.module_generating_set())

            def changed_quadratic_value(element):
                coefficients = module_coefficients(element)
                values = tuple(coefficients.get(label, target_ring.zero()) for label in labels)
                return target_ring(
                    sum(
                        (values[i] ** 2) * diagonal[i]
                        for i in range(len(values))
                    )
                    + sum(
                        values[i] * values[j] * polar[i][j]
                        for i in range(len(values))
                        for j in range(i + 1, len(values))
                    )
                )

            return FormModule(
                QuadraticForms(changed, target_ring)(changed_quadratic_value)
            )

        def hom(self, images, codomain=None):
            from dzack_research.preamble.categories.forms import QuadraticFormMorphism
            from dzack_research.preamble.categories.modules import module_homset

            if codomain is None:
                if isinstance(images, dict) and images:
                    codomain = next(iter(images.values())).parent()
                elif isinstance(images, (tuple, list)) and images:
                    codomain = images[0].parent()
                else:
                    raise TypeError("the codomain is required when it cannot be read from images")
            homset = module_homset(self, codomain)
            morphism = homset(images)
            if codomain not in FormModules(codomain.base_ring()):
                return morphism
            if self.value_module() is not codomain.value_module():
                raise TypeError("form-preserving maps require the same value module")
            source_form = self.form()
            target_form = codomain.form()
            generators = tuple(self.module_generators())
            if isinstance(source_form, QuadraticFormMorphism):
                if not isinstance(target_form, QuadraticFormMorphism):
                    raise TypeError("a quadratic formed module maps to another quadratic formed module")
                probes = generators + tuple(
                    left + right
                    for i, left in enumerate(generators)
                    for right in generators[i + 1 :]
                )
                preserves = all(
                    source_form(element) == target_form(morphism(element))
                    for element in probes
                )
            else:
                if isinstance(target_form, QuadraticFormMorphism):
                    raise TypeError("a bilinear formed module maps to another bilinear formed module")
                preserves = all(
                    source_form(left, right)
                    == target_form(morphism(left), morphism(right))
                    for left in generators
                    for right in generators
                )
            if not preserves:
                raise ValueError("the stated module morphism does not preserve the form")
            return FormMorphism(homset, images)

    class ElementMethods:
        def b(self, other):
            return self.parent().b(self, other)

        def norm(self):
            from dzack_research.preamble.categories.forms import QuadraticFormMorphism

            form = self.parent().form()
            if isinstance(form, QuadraticFormMorphism):
                return form(self)
            return form(self, self)

        def is_isotropic(self) -> bool:
            return self.norm() == self.parent().value_module().zero()

        def is_orthogonal_to(self, other) -> bool:
            return self.b(other) == self.parent().value_module().zero()

        def represents(self, value) -> bool:
            return self.norm() == self.parent().value_module()(value)


class BilinearFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "modules with a bilinear form"

    def super_categories(self):
        return [FormModules(self.base_ring())]


class SymmetricBilinearFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "modules with a symmetric bilinear form"

    def super_categories(self):
        return [BilinearFormModules(self.base_ring())]


class QuadraticFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "modules with a quadratic form"

    def super_categories(self):
        return [FormModules(self.base_ring())]

    class ParentMethods:
        def q(self, element):
            r"""Evaluate the equipped quadratic form on ``element``."""
            if element.parent() is not self:
                raise TypeError("the quadratic form is defined on this module")
            return self.form()(element)

    class ElementMethods:
        def q(self):
            return self.norm()


class FinitelyPresentedFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "finitely presented form modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules import FinitelyPresentedModules

        return [FormModules(self.base_ring()), FinitelyPresentedModules(self.base_ring())]


class FinitelyPresentedBilinearFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "finitely presented modules with a bilinear form"

    def super_categories(self):
        return [
            FinitelyPresentedFormModules(self.base_ring()),
            BilinearFormModules(self.base_ring()),
        ]


class FinitelyPresentedQuadraticFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "finitely presented modules with a quadratic form"

    def super_categories(self):
        return [
            FinitelyPresentedFormModules(self.base_ring()),
            QuadraticFormModules(self.base_ring()),
        ]


class FreeFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "free form modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules import FramedFreeModules

        return [FormModules(self.base_ring()), FramedFreeModules(self.base_ring())]


class FinitelyGeneratedFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "finitely generated form modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules import FinitelyGeneratedModules

        return [FormModules(self.base_ring()), FinitelyGeneratedModules(self.base_ring())]


class FinitelyGeneratedFreeFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "finitely generated free form modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules import FinitelyGeneratedFreeModules

        return [
            FreeFormModules(self.base_ring()),
            FinitelyGeneratedFormModules(self.base_ring()),
            FinitelyGeneratedFreeModules(self.base_ring()),
        ]

    class ParentMethods:
        @cached_method
        def dual_module(self):
            from dzack_research.preamble.categories.modules import BasedFreeModule

            return BasedFreeModule(self.base_ring(), self.module_generating_set())

        @cached_method
        def correlation_morphism(self):
            if self.value_module() is not self.base_ring():
                raise TypeError("the correlation morphism to the dual requires a scalar-valued form")
            dual = self.dual_module()
            rows = self.gram_tensor().rows()
            images = {
                label: dual.linear_combination(
                    {
                        dual_label: coefficient
                        for dual_label, coefficient in zip(
                            dual.module_generating_set(),
                            row,
                            strict=True,
                        )
                        if coefficient != 0
                    }
                )
                for label, row in zip(
                    self.module_generating_set(),
                    rows,
                    strict=True,
                )
            }
            from dzack_research.preamble.categories.modules import module_homset

            return module_homset(self, dual)(images)

        def is_nondegenerate(self) -> bool:
            assert self.value_module() is self.base_ring()
            from dzack_research.preamble.categories.rings import engine_ring

            ring = engine_ring(self.base_ring())
            assert ring.is_integral_domain()
            determinant = self.gram_tensor().det()
            return determinant != 0

        def is_unimodular(self) -> bool:
            r"""Return whether the correlation morphism is an isomorphism."""
            assert self.value_module() is self.base_ring()
            return bool(self.gram_tensor().det().is_unit())

        def scale_submodule(self):
            assert self.value_module() is self.base_ring()
            from dzack_research.preamble.categories.rings import engine_ring

            return engine_ring(self.base_ring()).ideal(self.gram_tensor().list())


def FormModule(form):
    r"""Return the same represented module construction equipped with ``form``.

    The result remains a module object; it is not a wrapper around an
    ``underlying`` module.  A distinct represented parent is used so that two
    different selected forms on isomorphic modules remain distinct structured
    objects.
    """
    from dzack_research.preamble.categories.forms import (
        BilinearFormMorphism,
        QuadraticFormMorphism,
    )
    from dzack_research.preamble.categories.modules import (
        FinitelyGeneratedFreeModules,
        FinitelyPresentedModule,
        FinitelyPresentedModules,
        FramedFreeModules,
        ModulesWithChosenFinitePresentation,
        module_homset,
    )
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FreshFreeModuleOn,
    )

    if not isinstance(form, (BilinearFormMorphism, QuadraticFormMorphism)):
        raise TypeError("a formed module is classified by a bilinear or quadratic form")
    module = form.module()
    base_ring = module.base_ring()
    labels = module.module_generating_set()
    assert labels.cardinality() in SageZZ
    if module in FramedFreeModules(base_ring):
        formed = FreshFreeModuleOn(base_ring, labels)
    elif (
        module in FinitelyPresentedModules(base_ring)
        and module in ModulesWithChosenFinitePresentation(base_ring)
    ):
        formed = FinitelyPresentedModule(module.presentation())
    else:
        raise TypeError(
            "the active formed-module constructor requires a finite free or chosen finitely presented module"
        )
    forget_form = module_homset(formed, module)(
        {label: module.module_generator(label) for label in labels}
    )
    equip_form = module_homset(module, formed)(
        {label: formed.module_generator(label) for label in labels}
    )
    formed._form = form.pullback(forget_form)
    formed._pairing = formed._form
    formed._preamble_unformed_module = module
    formed._preamble_forget_form_morphism = forget_form
    formed._preamble_equip_form_morphism = equip_form

    categories = [FormModules(base_ring)]
    if formed in FramedFreeModules(base_ring):
        categories.append(FreeFormModules(base_ring))
    if formed in FinitelyPresentedModules(base_ring):
        categories.append(FinitelyPresentedFormModules(base_ring))
    if isinstance(form, BilinearFormMorphism):
        categories.append(BilinearFormModules(base_ring))
        categories.append(FormedModules(formed._form.codomain()))
        if formed in FinitelyPresentedModules(base_ring):
            categories.append(FinitelyPresentedBilinearFormModules(base_ring))
        try:
            symmetric = form.gram_tensor().is_symmetric()
        except TypeError:
            symmetric = False
        if symmetric:
            categories.append(SymmetricBilinearFormModules(base_ring))
    else:
        categories.append(QuadraticFormModules(base_ring))
        if formed in FinitelyPresentedModules(base_ring):
            categories.append(FinitelyPresentedQuadraticFormModules(base_ring))
    if formed in FinitelyGeneratedFreeModules(base_ring):
        categories.extend(
            [
                FinitelyGeneratedFormModules(base_ring),
                FinitelyGeneratedFreeFormModules(base_ring),
            ]
        )
    return refine(formed, categories)


def _formed_module_from_pairing(pairing):
    r"""Specialize a pairing \(M\otimes_R M\to W\) to a formed module."""
    from dzack_research.preamble.categories.forms.forms import BilinearFormMorphism
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FramedFreeModules,
    )

    if not isinstance(pairing, BilinearFormMorphism):
        raise TypeError("the diagonal of PairedModules is a bilinear form")
    module = pairing.module()
    ring = module.base_ring()
    if module in FramedFreeModules(ring):
        try:
            finite = module.module_generating_set().cardinality() in SageZZ
        except AttributeError:
            finite = False
        if finite:
            return FormModule(pairing)
    module._form = pairing
    module._pairing = pairing
    return refine(
        module,
        [
            FormModules(ring),
            FormedModules(pairing.codomain()),
            BilinearFormModules(ring),
        ],
    )


class _HeterogeneousPairing(Parent):
    r"""A pairing \(X\otimes_R Y\to W\) with \(X\neq Y\)."""

    def __init__(self, pairing) -> None:
        self._pairing = pairing
        category = PairedModules(pairing.codomain())
        Parent.__init__(self, category=category)
        refine(self, [category])

    def _repr_(self) -> str:
        return (
            f"Pairing {self.left_module()} ⊗ {self.right_module()} "
            f"-> {self.value_module()}"
        )


def _heterogeneous_pairing(pairing):
    return _HeterogeneousPairing(pairing)


def is_form_morphism(morphism) -> bool:
    return isinstance(morphism, FormMorphism)
