r"""Modules equipped with exact bilinear or quadratic forms."""

from dzack_research.preamble.categories.abstract_categories.objects import OwnedParameterizedCategory
from sage.categories.homset import Homset
from sage.categories.modules import Modules as SageModules
from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.cachefunc import cached_function, cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.parent import Parent

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.sets.set_categories import Sets as OwnedSets
from dzack_research.preamble.refine import refine



def _normalize_value_module(value_module):
    r"""Normalize a scalar-ring value object without imposing Sage-category membership."""
    if value_module in OwnedRings() or callable(getattr(value_module, "module_category", None)):
        return value_module
    try:
        return _owned_ring(value_module)
    except TypeError:
        return value_module



def _is_bilinear_form(form) -> bool:
    from dzack_research.preamble.categories.forms.forms import is_bilinear_form

    return is_bilinear_form(form)


def _is_quadratic_form(form) -> bool:
    from dzack_research.preamble.categories.forms.forms import is_quadratic_form

    return is_quadratic_form(form)


from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)


class FormMorphism(ModuleMorphism):
    r"""A linear morphism verified to preserve the equipped forms exactly."""

    def __init__(self, parent, images) -> None:
        if isinstance(images, ModuleMorphism):
            images = lambda element, morphism=images: morphism(element)
            elementwise = True
        else:
            elementwise = False
        ModuleMorphism.__init__(
            self,
            parent,
            images,
            elementwise=elementwise,
            verify_linearity=not elementwise,
        )
        source = self.domain()
        target = self.codomain()
        generators = tuple(source.module_generators())
        source_form = source.form()
        target_form = target.form()
        if _is_quadratic_form(source_form):
            if not _is_quadratic_form(target_form):
                raise TypeError("a quadratic form morphism requires quadratic endpoints")
            probes = generators + tuple(
                left + right
                for index, left in enumerate(generators)
                for right in generators[index + 1 :]
            )
            if any(source.q(element) != target.q(self(element)) for element in probes):
                raise ValueError("the stated morphism does not preserve the quadratic form")
        elif _is_bilinear_form(source_form):
            if not _is_bilinear_form(target_form):
                raise TypeError("a bilinear form morphism requires bilinear endpoints")
            if any(
                source.b(left, right) != target.b(self(left), self(right))
                for left in generators
                for right in generators
            ):
                raise ValueError("the stated morphism does not preserve the bilinear form")
        else:
            raise TypeError("a strict form morphism requires bilinear or quadratic forms")


class StrictFormHomset(CategoricalHomset):
    r"""The strict form-preserving Hom set on fixed formed endpoints."""

    Element = FormMorphism

    def __init__(self, domain, codomain) -> None:
        CategoricalHomset.__init__(
            self,
            HomCategoryConstruction(FormModules(domain.base_ring())),
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        if isinstance(images, FormMorphism) and images.parent() is self:
            return images
        return self.element_class(self, images)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a strict form endomorphism Hom set")
        return self(lambda element: element)


def strict_form_homset(domain, codomain):
    if domain.base_ring() != codomain.base_ring():
        raise ValueError("strict form morphisms require one base ring")
    return StrictFormHomset(domain, codomain)


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
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    if quadratic is None:
        ring = domain.base_ring()
        quadratic = domain in QuadraticFormModules(ring)
    return FormEmbedding(
        module_homset(domain, codomain),
        images,
        quadratic=quadratic,
    )


def _represented_value_module(formed_module):
    r"""Return the actual module object underlying a form's public value object.

    A scalar-valued form publicly takes values in the ring ``R``.  When ``R``
    is already carrying its canonical self-module structure it is returned
    directly; otherwise :func:`ring_as_module` supplies the canonical rank-one
    realization over itself.  Genuine module-valued forms are unchanged.
    """
    from dzack_research.preamble.categories.modules.pure.modules import Modules
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import ring_as_module

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
        {0: formed_module.base_ring()(value)}
    )


def _value_from_module_element(formed_module, element):
    represented = _represented_value_module(formed_module)
    if represented is formed_module.value_module():
        return represented(element)
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_coefficients,
    )

    coefficients = module_coefficients(element, represented)
    ring = formed_module.base_ring()
    labels = represented.module_generating_set()
    unit_label = labels.unrank(0)
    return ring(coefficients.get(unit_label, ring.zero()))


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
        source_form = self.domain().form()
        target_form = self.codomain().form()
        source_generators = tuple(self.domain().module_generators())
        if _is_bilinear_form(source_form):
            if not _is_bilinear_form(target_form):
                raise TypeError("bilinear formed modules map to bilinear formed modules")
            commutes = all(
                self.map_value(source_form(left, right))
                == target_form(
                    self.module_morphism()(left), self.module_morphism()(right)
                )
                for left in source_generators
                for right in source_generators
            )
        elif _is_quadratic_form(source_form):
            if not _is_quadratic_form(target_form):
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


class FormedModuleHomset(CategoricalHomset):
    Element = FormedModuleMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        if domain.base_ring() != codomain.base_ring():
            raise ValueError("fixed-fiber formed morphisms require one base ring")
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, datum):
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

        explicit_pair = (
            isinstance(datum, tuple)
            and len(datum) == 2
            and all(isinstance(part, Morphism) for part in datum)
        )
        if (
            not explicit_pair
            and not isinstance(datum, FormedModuleMorphism)
            and not isinstance(datum, ModuleMorphism)
        ):
            datum = module_homset(self.domain(), self.codomain())(datum)

        if isinstance(datum, FormedModuleMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the formed morphism has the wrong endpoints")
            if datum.parent() is self:
                return datum
            datum = (datum.module_morphism(), datum.value_morphism())
        elif isinstance(datum, ModuleMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the underlying module morphism has the wrong endpoints")
            source_values = _represented_value_module(self.domain())
            target_values = _represented_value_module(self.codomain())
            if source_values is not target_values:
                raise TypeError(
                    "a bare module morphism determines a formed morphism only "
                    "when the value module is unchanged"
                )
            datum = (datum, module_homset(source_values, target_values).identity())
        module_morphism, value_morphism = datum
        return self.element_class(self, module_morphism, value_morphism)

    def identity(self):
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

        values = _represented_value_module(self.domain())
        return self(
            (
                module_homset(self.domain(), self.domain()).identity(),
                module_homset(values, values).identity(),
            )
        )


class FormedModuleHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return FormedModuleHomset


def formed_module_homset(domain, codomain) -> FormedModuleHomset:
    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError("fixed-fiber formed morphisms require one base ring")
    category = FormModules(ring)
    if domain not in category or codomain not in category:
        raise TypeError("formed Hom endpoints must lie in one formed-module category")
    return category.Mor(domain, codomain)


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
    target_ring = changed_module.base_ring()
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
        changed = self.base_changed_domain()
        source_form = changed.form()
        target_form = self.codomain().form()
        generators = tuple(changed.module_generators())
        if _is_bilinear_form(source_form):
            if not _is_bilinear_form(target_form):
                raise TypeError("bilinear formed modules map to bilinear formed modules")
            commutes = all(
                self.map_value(source_form(left, right))
                == target_form(
                    self.module_morphism()(left), self.module_morphism()(right)
                )
                for left in generators
                for right in generators
            )
        elif _is_quadratic_form(source_form):
            if not _is_quadratic_form(target_form):
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
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

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


class FiberedFormedModuleHomset(CategoricalHomset):
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
        # The endpoints sit over different base rings, so the Hom lives in the
        # total category of the formed-module fibration, not in one fibre.
        CategoricalHomset.__init__(
            self,
            HomCategoryConstruction(FormedModules(domain.value_module())),
            domain,
            codomain,
        )

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
        if not self.ring_map().is_identity():
            raise ValueError("the fibered identity must lie over the identity ring map")
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

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


class PairedModules(OwnedParameterizedCategory):
    r"""Pairings \(X\otimes_R Y\to W\).

    An object is classified by an element of
    \(\operatorname{Hom}_R(X\otimes_R Y,W)\).  The diagonal \(X=Y\) is
    :class:`FormedModules`.
    """

    @staticmethod
    def __classcall__(cls, value_module):
        return OwnedParameterizedCategory.__classcall__(
            cls, _normalize_value_module(value_module)
        )

    @classmethod
    def _repr_object_names(cls):
        return "paired modules"

    def super_categories(self):
        return [OwnedSets()]

    def _call_(self, pairing):
        codomain = _normalize_value_module(pairing.codomain())
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


class FormedModules(OwnedParameterizedCategory):
    r"""Modules equipped with a bilinear form \(M\otimes_R M\to W\).

    This is the diagonal of :class:`PairedModules`: a pairing of a module
    with itself.
    """

    @staticmethod
    def __classcall__(cls, value_module):
        return OwnedParameterizedCategory.__classcall__(
            cls, _normalize_value_module(value_module)
        )

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

    class ElementMethods:
        def b(self, other):
            r"""Return the bilinear value ``b(self, other)``."""
            return self.parent().b(self, other)

        def q(self):
            r"""Return the quadratic value ``q(self)=b(self,self)``."""
            return self.parent().q(self)


class FormModules(OwnedCategoryOverBaseRing):
    r"""Modules over ``R`` equipped with a form."""

    @classmethod
    def _repr_object_names(cls):
        return "form modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    _HomCategory = FormedModuleHomCategoryConstruction

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

        def Mor(self, codomain, category=None):
            if category is None and codomain in FormModules(self.base_ring()):
                return strict_form_homset(self, codomain)
            from sage.categories.homset import Hom as SageHom
            return SageHom(self, codomain, category)

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

        def _Hom_(self, codomain, category=None):
            ring = self.base_ring()
            formed = FormModules(ring)
            if codomain in formed and (category is None or category.is_subcategory(formed)):
                return formed_module_homset(self, codomain)
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

            return module_homset(self, codomain)

        def b(self, left, right):
            r"""Evaluate the (polar) bilinear form on two elements of this module."""
            if left not in self or right not in self:
                raise TypeError("a form pairs two elements of one formed module")
            form = self.form()
            if _is_quadratic_form(form):
                return form.b(left, right)
            return form(left, right)

        def norm(self, element):
            r"""Return ``q(x)`` for a quadratic form, else ``b(x, x)``."""
            if element not in self:
                raise TypeError("the norm is defined on elements of this formed module")
            form = self.form()
            if _is_quadratic_form(form):
                return form(element)
            return form(element, element)

        def gram_tensor(self):
            r"""Return the scalar Gram as its intrinsic type-``(0,2)`` tensor."""
            form = self.form()
            return form.gram_tensor()

        def twist(self, scalar):
            from dzack_research.preamble.categories.forms.forms import (
                BilinearForms,
                QuadraticForms,
                QuadraticMap,
            )

            form = self.form()
            if _is_bilinear_form(form):
                try:
                    values = form.coordinate_values().map(
                        lambda value: scalar * value,
                        name="Twisted bilinear coordinate values",
                    )
                except TypeError:
                    return FormModule(
                        BilinearForms(self, self.value_module())(
                            lambda left, right: scalar * form(left, right)
                        )
                    )
                return FormModule(BilinearForms(self, self.value_module())(values))
            try:
                values = form.lift_coordinate_values().map(
                    lambda value: scalar * value,
                    name="Twisted quadratic-lift coordinate values",
                )
            except TypeError:
                return FormModule(
                    QuadraticMap(
                        self,
                        self.value_module(),
                        lambda element: scalar * form(element),
                    )
                )
            return FormModule(QuadraticForms(self, self.value_module())(values))

        def base_change(self, ring_map):
            r"""Base-change a scalar-valued finite free form along ``R -> S``."""
            from dzack_research.preamble.categories.forms.forms import (
                BilinearForms,
                QuadraticForms,
                QuadraticMap,
            )
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModuleOn
            from dzack_research.preamble.categories.modules.base_change import (
                base_change_codomain,
                base_change_scalar,
            )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_coefficients,
            )

            assert self.value_module() is self.base_ring()
            target_ring = base_change_codomain(self, ring_map)
            source = self
            source_labels = source.module_generating_set()
            changed = FreeModuleOn(target_ring, source_labels)
            form = self.form()

            if _is_bilinear_form(form):
                try:
                    changed_values = form.coordinate_values().map(
                        lambda value: base_change_scalar(ring_map, value),
                        name="Base-changed bilinear coordinate values",
                    )
                except TypeError:
                    changed_values = None
                if changed_values is not None:
                    return FormModule(BilinearForms(changed, target_ring)(changed_values))

                def changed_bilinear_value(left, right):
                    left_coefficients = module_coefficients(left, changed)
                    right_coefficients = module_coefficients(right, changed)
                    result = target_ring.zero()
                    for left_label, left_coefficient in left_coefficients.items():
                        source_left = source.module_generator(left_label)
                        for right_label, right_coefficient in right_coefficients.items():
                            source_right = source.module_generator(right_label)
                            result += (
                                left_coefficient
                                * right_coefficient
                                * base_change_scalar(
                                    ring_map,
                                    form(source_left, source_right),
                                )
                            )
                    return result

                return FormModule(
                    BilinearForms(changed, target_ring)(changed_bilinear_value)
                )

            if not _is_quadratic_form(form):
                raise TypeError(f"{form} is not a bilinear or quadratic form")

            try:
                changed_lift_values = form.lift_coordinate_values().map(
                    lambda value: base_change_scalar(ring_map, value),
                    name="Base-changed quadratic-lift coordinate values",
                )
            except TypeError:
                changed_lift_values = None
            if changed_lift_values is not None:
                return FormModule(QuadraticForms(changed, target_ring)(changed_lift_values))

            def changed_quadratic_value(element):
                coefficients = module_coefficients(element, changed)
                result = target_ring.zero()
                for left_label, left_coefficient in coefficients.items():
                    source_left = source.module_generator(left_label)
                    result += (
                        left_coefficient**2
                        * base_change_scalar(ring_map, form(source_left))
                    )
                    left_rank = source_labels.rank(left_label)
                    for right_label, right_coefficient in coefficients.items():
                        if source_labels.rank(right_label) <= left_rank:
                            continue
                        source_right = source.module_generator(right_label)
                        result += (
                            left_coefficient
                            * right_coefficient
                            * base_change_scalar(
                                ring_map,
                                form.b(source_left, source_right),
                            )
                        )
                return target_ring(result)

            return FormModule(
                QuadraticMap(changed, target_ring, changed_quadratic_value)
            )


    class ElementMethods:
        def b(self, other):
            r"""Return the polar bilinear value ``b(self, other)``."""
            return self.parent().b(self, other)

        def q(self):
            r"""Return the represented quadratic/norm value of this element."""
            return self.parent().norm(self)


class BilinearFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "modules with a bilinear form"

    def super_categories(self):
        return [FormModules(self.base_ring())]

    _HomCategory = FormedModuleHomCategoryConstruction


class SymmetricBilinearFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "modules with a symmetric bilinear form"

    def super_categories(self):
        return [BilinearFormModules(self.base_ring())]

    _HomCategory = FormedModuleHomCategoryConstruction

    class ParentMethods:
        def algebraic_correlation_morphism(self):
            from dzack_research.preamble.categories.modules.hodge import (
                AlgebraicCorrelationMorphism,
            )

            return AlgebraicCorrelationMorphism(self)

        def correlation_isomorphism(self):
            from dzack_research.preamble.categories.modules.hodge import (
                CorrelationIsomorphism,
            )

            return CorrelationIsomorphism(self)

        def hodge_discriminant(self, volume):
            from dzack_research.preamble.categories.modules.hodge import HodgeDiscriminant

            return HodgeDiscriminant(self, volume)

        def hodge_star(self, volume, degree):
            from dzack_research.preamble.categories.modules.hodge import HodgeStar

            return HodgeStar(self, volume, degree)

        def hodge_star_over_fraction_field(self, volume, degree):
            from dzack_research.preamble.categories.modules.hodge import (
                HodgeStarOverFractionField,
            )

            return HodgeStarOverFractionField(self, volume, degree)

        def multivector_hodge_star(self, volume, degree):
            from dzack_research.preamble.categories.modules.hodge import (
                MultivectorHodgeStar,
            )

            return MultivectorHodgeStar(self, volume, degree)


class QuadraticFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "modules with a quadratic form"

    def super_categories(self):
        return [FormModules(self.base_ring())]

    _HomCategory = FormedModuleHomCategoryConstruction

    class ParentMethods:
        def q(self, element):
            r"""Evaluate the equipped quadratic form on ``element``."""
            if element not in self:
                raise TypeError("the quadratic form is defined on this module")
            return self.form()(element)


class FinitelyPresentedFormModules(OwnedCategoryOverBaseRing):
    class ParentMethods:
        Mor = FormModules.ParentMethods.Mor
        base_change = FormModules.ParentMethods.base_change

    @classmethod
    def _repr_object_names(cls):
        return "finitely presented form modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import FinitelyPresentedModules

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
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules

        return [FormModules(self.base_ring()), FramedFreeModules(self.base_ring())]

    class ParentMethods:
        Mor = FormModules.ParentMethods.Mor
        base_change = FormModules.ParentMethods.base_change

        def subobject_on(self, module_generating_set):
            r"""Return the span equipped with the pulled-back form."""
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                _span_basis_elements,
            )

            basis = _span_basis_elements(self, module_generating_set)
            return _form_subobject_spanning(self, basis)


class FinitelyGeneratedFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "finitely generated form modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import FinitelyGeneratedModules

        return [FormModules(self.base_ring()), FinitelyGeneratedModules(self.base_ring())]


class FinitelyGeneratedFreeFormModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "finitely generated free form modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import FinitelyGeneratedFreeModules

        return [
            FreeFormModules(self.base_ring()),
            FinitelyGeneratedFormModules(self.base_ring()),
            FinitelyGeneratedFreeModules(self.base_ring()),
        ]

    class ParentMethods:
        Mor = FormModules.ParentMethods.Mor
        base_change = FormModules.ParentMethods.base_change

        @cached_method
        def dual_module(self):
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import BasedFreeModule

            return BasedFreeModule(self.base_ring(), self.module_generating_set())

        @cached_method
        def correlation_morphism(self):
            if self.value_module() is not self.base_ring():
                raise TypeError("the correlation morphism to the dual requires a scalar-valued form")
            dual = self.dual_module()
            images = {}
            for label in self.module_generating_set():
                source_generator = self.module_generator(label)
                images[label] = dual.linear_combination(
                    {
                        dual_label: coefficient
                        for dual_label in dual.module_generating_set()
                        if (
                            coefficient := self.b(
                                source_generator,
                                self.module_generator(dual_label),
                            )
                        )
                    }
                )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

            return module_homset(self, dual)(images)

        def determinant(self):
            r"""Return the determinant of the selected scalar-valued form."""
            assert self.value_module() is self.base_ring()
            return self.correlation_morphism().matrix().determinant()

        def is_nondegenerate(self) -> bool:
            assert self.value_module() is self.base_ring()
            from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring

            ring = _engine_ring(self.base_ring())
            assert ring.is_integral_domain()
            return self.determinant() != 0

        def is_unimodular(self) -> bool:
            r"""Return whether the correlation morphism is an isomorphism."""
            assert self.value_module() is self.base_ring()
            return bool(self.determinant().is_unit())

        def scale_submodule(self):
            assert self.value_module() is self.base_ring()
            from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring

            return _engine_ring(self.base_ring()).ideal(self.gram_tensor().list())


def FormModule(form):
    r"""Return the same represented module construction equipped with ``form``.

    The result remains a module object; it is not a wrapper around an
    ``underlying`` module.  A distinct represented parent is used so that two
    different selected forms on isomorphic modules remain distinct structured
    objects.
    """
    from dzack_research.preamble.categories.modules.pure.modules import FinitelyGeneratedFreeModules
    from dzack_research.preamble.categories.modules.pure.modules import FinitelyPresentedModules
    from dzack_research.preamble.categories.modules.pure.modules import ModulesWithChosenFinitePresentation
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FreshFreeModuleOn,
    )

    if not (_is_bilinear_form(form) or _is_quadratic_form(form)):
        raise TypeError("a formed module is classified by a bilinear or quadratic form")
    module = form.module()
    base_ring = module.base_ring()
    labels = module.module_generating_set()
    from dzack_research.preamble.categories.sets.cardinals import cardinal
    assert cardinal(labels.cardinality()).is_finite()
    if module in FramedFreeModules(base_ring):
        formed = FreshFreeModuleOn(base_ring, labels)
    elif module in ModulesWithChosenFinitePresentation(base_ring):
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
    if _is_bilinear_form(form):
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


@cached_function(key=lambda module, basis: (id(module), basis))
def _form_subobject_spanning(module, basis):
    r"""Return the canonical formed subobject on a finite span basis."""
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FreeModuleOn,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_embedding,
    )
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        _finalize_module_subobject,
    )

    labels = OwnedSets.Δ[int(basis.cardinality()) - 1]
    free_source = FreeModuleOn(module.base_ring(), labels)
    preliminary = module_embedding(
        free_source,
        module,
        lambda label: basis.unrank(int(label)),
    )
    source = FormModule(module.form().pullback(preliminary))
    inclusion = form_embedding(
        source,
        module,
        lambda label: basis.unrank(int(label)),
    )
    return _finalize_module_subobject(
        module,
        basis,
        source,
        inclusion=inclusion,
    )


def BilinearForm(module, value_module, datum):
    r"""Return ``module`` equipped with the stated bilinear form."""
    from dzack_research.preamble.categories.forms.forms import BilinearForms

    return FormModule(BilinearForms(module, value_module)(datum))


def QuadraticForm(module, value_module, datum):
    r"""Return ``module`` equipped with the stated quadratic form."""
    from dzack_research.preamble.categories.forms.forms import QuadraticForms, QuadraticMap
    from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily

    coordinate_datum = (
        isinstance(datum, IndexedFamily)
        or hasattr(datum, "rows")
        or (
            isinstance(datum, (tuple, list))
            and all(isinstance(row, (tuple, list)) for row in datum)
        )
    )
    form = (
        QuadraticForms(module, value_module)(datum)
        if coordinate_datum
        else QuadraticMap(module, value_module, datum)
    )
    return FormModule(form)


def _formed_module_from_pairing(pairing):
    r"""Specialize a pairing \(M\otimes_R M\to W\) to a formed module."""
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FramedFreeModules,
    )

    if not _is_bilinear_form(pairing):
        raise TypeError("the diagonal of PairedModules is a bilinear form")
    module = pairing.module()
    ring = module.base_ring()
    if module in FramedFreeModules(ring):
        try:
            from dzack_research.preamble.categories.sets.cardinals import cardinal
            finite = cardinal(module.module_generating_set().cardinality()).is_finite()
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
