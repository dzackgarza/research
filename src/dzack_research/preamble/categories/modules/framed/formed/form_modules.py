r"""Modules equipped with exact bilinear or quadratic forms."""

from sage.categories.category_with_axiom import all_axioms
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
    MonoCategoryConstruction,
    _category_homset,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.forms.forms import (
    _is_bilinear_form as _form_is_bilinear,
    _is_quadratic_form as _form_is_quadratic,
)
from dzack_research.preamble.categories.modules.base_change import (
    _base_change_codomain,
    _base_change_scalar,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FramedFreeModules,
    _module_subobject_constructor_data,
    _span_basis_elements,
)
from dzack_research.preamble.categories.modules.hodge import (
    _algebraic_correlation_morphism,
    _correlation_isomorphism,
    _hodge_discriminant,
    _hodge_star,
    _hodge_star_over_fraction_field,
    _multivector_hodge_star,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    _presentation_matrix,
)
from dzack_research.preamble.categories.modules.framed.formed.torsion_form_modules import (
    CokernelTorsionFormModules,
    TorsionBilinearFormIsoCategoryConstruction,
    TorsionFormTwistFunctor,
    TorsionQuadraticFormIsoCategoryConstruction,
    _bilinear_descends,
    _coerced_gram,
    _forms_are_isomorphic,
    _invariant_factor_form_isomorphism,
    _p_adic_jordan_decomposition,
    _p_adic_jordan_form,
    _p_adic_jordan_module_generators,
    _quadratic_descends,
    _regenerate_form_on_generators,
    _representative_gram,
    _torsion_form_all_subobjects,
    _torsion_form_automorphism_group,
    _torsion_form_element_action,
    _torsion_form_isotropic_subobjects,
    _torsion_form_lagrangian_subobjects,
    _torsion_form_maximal_isotropic_subobjects,
    _torsion_form_orthogonal_subobject,
    _torsion_form_primary_part,
    _torsion_form_subobject_on,
    _torsion_form_subobject_orbits,
    _torsion_form_subquotient,
)
from dzack_research.preamble.categories.modules.framed.fraction_field_quotients import (
    FractionFieldQuotients,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    ModulesWithChosenFinitePresentation,
    TensorProductModules,
    VectorSpaces,
    _refine_finitely_presented_torsion_module,
    _torsion_module_presented_by_matrix,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import Sets as OwnedSets
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom

for _form_axiom in ("Symmetric", "Nondegenerate", "Unimodular", "Even"):
    if _form_axiom not in all_axioms:
        all_axioms.add(_form_axiom)


def _is_bilinear_form(form) -> bool:

    return _form_is_bilinear(form)


def _is_quadratic_form(form) -> bool:

    return _form_is_quadratic(form)


@cached_function(key=lambda formed_module: id(formed_module))
def _represented_value_module(formed_module):
    r"""Return the actual module object underlying a form's public value object.

    A scalar-valued form publicly takes values in the ring ``R``.  When ``R``
    is already carrying its canonical self-module structure it is returned
    directly; otherwise ``R.regular_module()`` supplies the canonical rank-one
    realization over itself.  Genuine module-valued forms are unchanged.
    """

    value = formed_module.value_module()
    ring = formed_module.base_ring()
    if value is ring:
        return ring.regular_module()
    if value in Modules(ring):
        return value
    if value in OwnedRings():
        try:
            scalar_map = OwnedRings().Mor(ring, value)(lambda scalar: value(scalar))
            return value.regular_module().restrict_scalars(scalar_map)
        except (TypeError, ValueError, NotImplementedError):
            pass
    raise TypeError(
        f"the form value object {value} has no represented {ring}-module structure"
    )


def _value_as_module_element(formed_module, value):
    represented = _represented_value_module(formed_module)
    if represented is formed_module.value_module():
        return represented(value)
    extension = getattr(represented, "module_over_extension", lambda: None)()
    if extension is not None:
        unit_label = extension.module_generating_set()[0]
        return represented.wrap(
            extension.linear_combination(
                {unit_label: formed_module.value_module()(value)}
            )
        )
    return represented.linear_combination(
        {0: formed_module.base_ring()(value)}
    )


def _value_from_module_element(formed_module, element):
    represented = _represented_value_module(formed_module)
    if represented is formed_module.value_module():
        return represented(element)

    extension = getattr(represented, "module_over_extension", lambda: None)()
    if extension is not None:
        restricted_element = represented(element)
        coefficients = extension.framing_coefficients(restricted_element.underlying_element())
        unit_label = extension.module_generating_set()[0]
        value_ring = formed_module.value_module()
        return value_ring(coefficients.get(unit_label, value_ring.zero()))

    coefficients = represented.framing_coefficients(element)
    ring = formed_module.base_ring()
    labels = represented.module_generating_set()
    unit_label = labels[0]
    return ring(coefficients.get(unit_label, ring.zero()))


class FormedModuleMorphism(Morphism):
    r"""A morphism of formed modules in one coefficient-ring fiber.

    The datum is a pair ``(f,h)`` with a module map on the underlying modules
    and a module map on the value objects, satisfying the form square.  The
    form is preserved exactly, and the morphism is an isometry onto its image,
    exactly when ``h`` is the identity; :meth:`preserves_form_exactly` asks that.
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

    def preserves_form_exactly(self) -> bool:
        r"""Return whether the value-object map is the identity."""
        value_morphism = self.value_morphism()
        values = value_morphism.domain()
        if value_morphism.codomain() is not values:
            return False
        # A Hom object has one identity, so this is object identity. Comparing
        # morphisms extensionally would require extra finite-presentation data.
        return value_morphism is values.module_category().Mor(values, values).identity()

    def is_injective(self) -> bool:
        r"""Return whether the underlying module map is injective."""
        domain = self.domain()

        if domain in Modules(domain.base_ring()).FinitelyPresented().Torsion():
            images = []
            for element in domain.elements():
                image = self.module_morphism()(element)
                if any(image == previous for previous in images):
                    return False
                images.append(image)
            return True

        return self.module_morphism().is_injective()

    def map_value(self, value):
        source_element = _value_as_module_element(self.domain(), value)
        return _value_from_module_element(
            self.codomain(), self.value_morphism()(source_element)
        )

    def _check_form_square(self) -> None:
        domain = self.domain()
        source_values = _represented_value_module(domain)
        if (
            domain is self.codomain()
            and self.module_morphism() is domain.module_category().Mor(domain, domain).identity()
            and self.value_morphism() is source_values.module_category().Mor(source_values, source_values).identity()
        ):
            return
        source_form = self.domain().form()
        target_form = self.codomain().form()
        source_generators = tuple(self.domain().module_generators())
        if _is_bilinear_form(source_form):
            if not _is_bilinear_form(target_form):
                raise TypeError("bilinear formed modules map to bilinear formed modules")
            commutes = all(
                self.map_value(self.domain().b(left, right))
                == self.codomain().b(
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
                self.map_value(self.domain().norm(element))
                == self.codomain().norm(self.module_morphism()(element))
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

    def __eq__(self, other) -> bool:
        r"""A formed morphism is the pair ``(f,h)``; both components decide."""
        if not isinstance(other, FormedModuleMorphism):
            return False
        if self is other:
            return True
        if self.parent() is not other.parent():
            return False
        return (
            self.module_morphism() == other.module_morphism()
            and self.value_morphism() == other.value_morphism()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self.parent()), id(self.module_morphism())))

    def __mul__(self, other):
        if not isinstance(other, FormedModuleMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            raise ValueError("formed morphisms are not composable")
        return FormModules(other.domain().base_ring()).Mor(other.domain(), self.codomain())(
            (
                self.module_morphism() * other.module_morphism(),
                self.value_morphism() * other.value_morphism(),
            )
        )


class FormEmbedding(FormedModuleMorphism):
    r"""A form-preserving morphism whose module map is a monomorphism."""

    def __init__(self, parent, module_morphism, value_morphism, *, quadratic: bool) -> None:
        FormedModuleMorphism.__init__(self, parent, module_morphism, value_morphism)
        self._quadratic = bool(quadratic)

    def is_quadratic(self) -> bool:
        return self._quadratic

    def lift(self, element):
        r"""Return the unique preimage through this formed monomorphism.

        The form carries no additional lifting datum: lift through the
        underlying module monomorphism whose construction owns the selected
        preimage operation.
        """
        return self.module_morphism().lift(element)

    @cached_method
    def orthogonal_complement(self):
        r"""Return the orthogonal complement of this embedded formed submodule.

        For ``i:S -> M`` this is the kernel of the pairing morphism
        ``M -> S^vee``, ``x |-> (s |-> b_M(x,i(s)))``.  The kernel computation
        belongs to the module-morphism owner; its image in ``M`` is then
        equipped with the restricted form by ``M.subobject_on``.
        """
        source = self.domain()
        target = self.codomain()
        if source not in FreeFormModules(source.base_ring()).FinitelyGenerated():
            raise TypeError("orthogonal complements currently require a finite free formed source")
        if target not in FreeFormModules(target.base_ring()).FinitelyGenerated():
            raise TypeError("orthogonal complements currently require a finite free formed target")
        if source.value_module() is not source.base_ring():
            raise TypeError("orthogonal complements currently require scalar-valued forms")
        if target.value_module() is not target.base_ring():
            raise TypeError("orthogonal complements currently require scalar-valued forms")
        if source.base_ring() is not target.base_ring():
            raise TypeError("an orthogonal complement is taken in one coefficient ring")

        dual = source.dual_module()
        images = {}
        source_labels = tuple(source.module_generating_set())
        for target_label in target.module_generating_set():
            target_generator = target.module_generator(target_label)
            images[target_label] = dual.linear_combination(
                {
                    source_label: coefficient
                    for source_label in source_labels
                    if (
                        coefficient := target.b(
                            target_generator,
                            self(source.module_generator(source_label)),
                        )
                    )
                }
            )
        pairing = target.module_category().Mor(target, dual)(images)
        kernel = pairing.kernel()
        kernel_inclusion = kernel.inclusion()
        return target.subobject_on(
            tuple(kernel_inclusion(generator) for generator in kernel.module_generators())
        )


class FormEmbeddingHomset(CategoricalHomset):
    r"""The form-preserving monomorphisms between two formed modules."""

    Element = FormEmbedding

    def __init__(self, hom_family, domain, codomain) -> None:
        ring = domain.base_ring()
        formed = FormModules(ring)
        if codomain.base_ring() is not ring or domain not in formed or codomain not in formed:
            raise TypeError("a form embedding requires two formed modules over one scalar ring")
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    def _element_constructor_(self, images, *, quadratic: bool | None = None):
        if isinstance(images, FormEmbedding):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the form embedding has the wrong endpoints")
            if images.parent() is self:
                return images
            images = images.module_morphism()

        domain = self.domain()
        codomain = self.codomain()
        if quadratic is None:
            ring = domain.base_ring()
            quadratic = domain in QuadraticFormModules(ring)
        values = _represented_value_module(domain)
        if _represented_value_module(codomain) is not values:
            raise TypeError("a form embedding keeps the value module")
        module_morphism = domain.module_category().Mor(domain, codomain)(images)
        embedding = self.element_class(
            self,
            module_morphism,
            values.module_category().Mor(values, values).identity(),
            quadratic=quadratic,
        )
        injective = embedding.is_injective()
        if injective is not True:
            raise ValueError("a form embedding requires an injective underlying module map")
        return embedding

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
        return f"Emb_Form({self.domain()}, {self.codomain()})"


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
            domain = self.domain()
            codomain = self.codomain()
            datum = domain.module_category().Mor(domain, codomain)(datum)

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
            datum = (datum, source_values.module_category().Mor(source_values, target_values).identity())
        module_morphism, value_morphism = datum
        return self.element_class(self, module_morphism, value_morphism)

    @cached_method
    def identity(self):

        domain = self.domain()
        values = _represented_value_module(domain)
        return self(
            (
                domain.module_category().Mor(domain, domain).identity(),
                values.module_category().Mor(values, values).identity(),
            )
        )

class FormedModuleHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return FormedModuleHomset


class FormedModuleMonoCategoryConstruction(MonoCategoryConstruction):
    r"""The form-preserving monomorphisms of formed modules."""

    def fixed_category_class(self):
        return FormEmbeddingHomset


def _base_change_element(module, changed_module, ring_map, element):
    r"""Transport one represented framed-module element along ``ring_map``.

    This is the elementwise form of the scalar-extension unit on the selected
    presentation.  It is used only to compose morphisms in different scalar
    fibers; the public scalar-extension object remains ``changed_module``.
    """

    coefficients = module.framing_coefficients(element)
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
    scalar-valued finite-free formed objects supported by ``FormModules(R)``'s
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
                self.map_value(changed.b(left, right))
                == self.codomain().b(
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
                self.map_value(changed.norm(element))
                == self.codomain().norm(self.module_morphism()(element))
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
        homset = other.domain().fibered_formed_homset(
            self.codomain(), composite_ring_map
        )

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
        module_map = direct_changed.module_category().Mor(direct_changed, self.codomain())(module_images)

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
        value_map = direct_values.module_category().Mor(direct_values, target_values)(value_images)
        return homset((module_map, value_map))


class FiberedFormedModuleHomset(CategoricalHomset):
    Element = FiberedFormedModuleMorphism

    def __init__(self, domain, codomain, ring_map) -> None:

        target_ring = _base_change_codomain(domain, ring_map)
        if target_ring != codomain.base_ring():
            raise ValueError("the coefficient map does not land at the target base ring")
        self._ring_map = ring_map
        self._base_changed_domain = domain.base_change(ring_map)
        # The endpoints sit over different base rings; the Hom is filed under
        # the Hom category of the source fibre.
        CategoricalHomset.__init__(
            self,
            FormModules(domain.base_ring()).HomCategory(),
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

        changed = self.base_changed_domain()
        module_map = changed.module_category().Mor(changed, self.domain())(
            {
                label: self.domain().module_generator(label)
                for label in self.domain().module_generating_set()
            }
        )
        source_values = _represented_value_module(changed)
        target_values = _represented_value_module(self.domain())
        value_map = source_values.module_category().Mor(source_values, target_values)(
            {
                label: target_values.module_generator(label)
                for label in source_values.module_generating_set()
            }
        )
        return self((module_map, value_map))


def _value_module_of(value_object):
    r"""The module a pairing takes values in; a ring names its regular module."""
    if value_object in OwnedRings():
        return value_object.regular_module()
    return value_object


class PairedModules(OwnedParameterizedCategory):
    r"""Pairings \(X\otimes_R Y\to W\), the comma category of the tensor functor over ``W``.

    An object is a morphism ``X (x) Y -> W`` of ``Modules(R)``, so its
    underlying arrow is an object of the slice ``Modules(R)/W``.  A ring
    given as the parameter names its regular module.  Equipping ``X`` with
    a pairing ``X (x) X -> W`` is :class:`FormModules`.
    """

    @staticmethod
    def __classcall__(cls, value_module):
        return OwnedParameterizedCategory.__classcall__(cls, _value_module_of(value_module))

    @classmethod
    def _repr_object_names(cls):
        return "paired modules"

    def parameter_category(self):
        return Modules(self.base_ring())

    def base_ring(self):
        return self.base().base_ring()

    def super_categories(self):
        return [Modules(self.base_ring()).SliceOver(self.base())]

    def an_object(self):
        r"""``R (x) R -> W`` sending the pure tensor of the units to a chosen element of ``W``."""
        ring = self.base_ring()
        regular = ring.regular_module()
        square = Modules(ring).tensor_product((regular, regular))
        value = self.base()
        return self(
            square.module_category().Mor(square, value)(
                {label: value.an_element() for label in square.module_generating_set()}
            )
        )

    def _call_(self, pairing):
        r"""The pairing classified by a morphism out of a represented tensor product.

        A ring-valued pairing ``X x Y -> R`` arrives as the form object of
        ``X.pairings_with(Y, R)``; its arrow into the regular module ``R`` is
        built here from its values on the tensor generators.
        """
        ring = self.base_ring()
        value = self.base()
        assert _value_module_of(pairing.codomain()) is value, (
            f"a pairing in {self} takes values in {value}, not {pairing.codomain()}"
        )
        if pairing.codomain() is not value:
            square = Modules(ring).tensor_product((pairing.left_module(), pairing.right_module()))
            left, right = square.tensor_factor(0), square.tensor_factor(1)
            pairing = square.module_category().Mor(square, value)(
                lambda pair: value(
                    (pairing(left.module_generator(pair.component(0)), right.module_generator(pair.component(1))),)
                )
            )
        assert pairing.parent().homset_category().is_subcategory(Modules(ring)), (
            f"a pairing in {self} is a morphism of {Modules(ring)}; {pairing} is not one, "
            "so its tensor-product domain is not represented"
        )
        assert pairing.domain() in TensorProductModules(ring), (
            f"a pairing is classified on a tensor product; {pairing.domain()} is not one"
        )
        return _object_of(self, arrow=pairing)

    class ParentMethods:
        def pairing(self, left, right):
            r"""Evaluate the pairing on a pair of elements."""
            return self.arrow()(self.arrow().domain().pure_tensor(left, right))

        def left_module(self):
            return self.arrow().domain().tensor_factor(0)

        def right_module(self):
            return self.arrow().domain().tensor_factor(1)

        def value_module(self):
            return self.arrow().codomain()

        def _repr_(self) -> str:
            return (
                f"Pairing {self.left_module()} ⊗ {self.right_module()} "
                f"-> {self.value_module()}"
            )


def _formed_module_base_change(self, ring_map):
    r"""Base-change a scalar-valued finite free form along ``R -> S``."""

    assert self.value_module() is self.base_ring()
    target_ring = _base_change_codomain(self, ring_map)
    source = self
    source_labels = source.module_generating_set()
    changed = target_ring.free_module(source_labels)
    form = self._formed_form()

    if _is_bilinear_form(form):
        try:
            changed_values = form.coordinate_values().map(
                lambda value: _base_change_scalar(ring_map, value),
                name="Base-changed bilinear coordinate values",
            )
        except TypeError:
            changed_values = None
        if changed_values is not None:
            return FormModules(target_ring)(
                changed.bilinear_forms(target_ring)(changed_values)
            )

        def changed_bilinear_value(left, right):
            left_coefficients = changed.framing_coefficients(left)
            right_coefficients = changed.framing_coefficients(right)
            result = target_ring.zero()
            for left_label, left_coefficient in left_coefficients.items():
                source_left = source.module_generator(left_label)
                for right_label, right_coefficient in right_coefficients.items():
                    source_right = source.module_generator(right_label)
                    result += (
                        left_coefficient
                        * right_coefficient
                        * _base_change_scalar(
                            ring_map,
                            form(source_left, source_right),
                        )
                    )
            return result

        return FormModules(target_ring)(
            changed.bilinear_forms(target_ring)(changed_bilinear_value)
        )

    if not _is_quadratic_form(form):
        raise TypeError(f"{form} is not a bilinear or quadratic form")

    try:
        changed_lift_values = form.lift_coordinate_values().map(
            lambda value: _base_change_scalar(ring_map, value),
            name="Base-changed quadratic-lift coordinate values",
        )
    except TypeError:
        changed_lift_values = None
    if changed_lift_values is not None:
        return FormModules(target_ring)(
            changed.quadratic_forms(target_ring)(changed_lift_values)
        )

    def changed_quadratic_value(element):
        coefficients = changed.framing_coefficients(element)
        result = target_ring.zero()
        for left_label, left_coefficient in coefficients.items():
            source_left = source.module_generator(left_label)
            result += (
                left_coefficient**2
                * _base_change_scalar(ring_map, form(source_left))
            )
            left_rank = source_labels.ranking_map()(left_label)
            for right_label, right_coefficient in coefficients.items():
                if source_labels.ranking_map()(right_label) <= left_rank:
                    continue
                source_right = source.module_generator(right_label)
                result += (
                    left_coefficient
                    * right_coefficient
                    * _base_change_scalar(
                        ring_map,
                        form.b(source_left, source_right),
                    )
                )
        return target_ring(result)

    return FormModules(target_ring)(
        changed.quadratic_map(target_ring, changed_quadratic_value)
    )


class FormModules(OwnedCategoryOverBaseRing):
    r"""Modules over ``R`` equipped with a form.

    ``FormModules(R)(b)`` for a form ``b`` stated on ``M`` is the one entry:
    the formed module is built on the data of ``M``, retains ``M`` as its
    datum and answers ``unformed_module()`` with it, and elements pass
    between the two by coercion, ``F(m)`` and ``M(f)``.
    """

    def an_object(self):
        r"""The hyperbolic plane U."""
        from dzack_research.preamble.categories.lattices import Lattices

        return Lattices(self.base_ring())("U")

    @classmethod
    def _repr_object_names(cls):
        return "form modules"

    def super_categories(self):

        return [Modules(self.base_ring())]

    def _call_(
        self,
        form,
        *,
        _extra_categories=(),
        _extra_construction_data=None,
        _subobject_ambient=None,
        _subobject_generator_images=None,
        _subobject_lift=None,
        _subobject_inclusion_factory=None,
        _subobject_verify_linearity=True,
    ):
        r"""Equip the module classified by ``form`` with that selected form."""
        module = form.module()
        if module.base_ring() is not self.base_ring():
            raise ValueError("a formed module belongs to the scalar ring of its selected form")
        return _form_module(
            form,
            _extra_categories=_extra_categories,
            _extra_construction_data=_extra_construction_data,
            _subobject_ambient=_subobject_ambient,
            _subobject_generator_images=_subobject_generator_images,
            _subobject_lift=_subobject_lift,
            _subobject_inclusion_factory=_subobject_inclusion_factory,
            _subobject_verify_linearity=_subobject_verify_linearity,
        )

    _HomCategory = FormedModuleHomCategoryConstruction
    _MonoCategory = FormedModuleMonoCategoryConstruction

    class ParentMethods:
        def __init__(self, source_form, **rest) -> None:
            r"""The form determines its module; the two are not independent data."""
            self._preamble_form = source_form
            super().__init__(**rest)

        def form(self):
            r"""Return the selected form datum, stated on the unformed module."""
            return self._preamble_form

        @cached_method
        def _formed_form(self):
            r"""The selected form read on this module: its arguments coerce to the unformed module."""
            form = self.form()
            module = self.unformed_module()
            if form.module() is self:
                return form
            if _is_quadratic_form(form):
                return self.quadratic_map(
                    self.value_module(),
                    lambda element: form(module(element)),
                )
            return self.bilinear_forms(self.value_module())(
                lambda left, right: form(module(left), module(right))
            )

        def unformed_module(self):
            r"""Return the module the form was stated on: the datum this module is built on."""
            return self.form().module()

        def _element_of_unformed_module(self, element):
            r"""The element of :meth:`unformed_module` with the coefficients ``element`` has here.

            A formed module is built on the framing of the module its form was
            stated on: the same generating set and, for a presented module,
            the same presentation.  So an element reads there with the same
            coefficients.
            """
            return self.unformed_module().linear_combination(
                self.framing_coefficients(element)
            )

        def _element_from_unformed_module(self, element):
            r"""The element of this module with the coefficients ``element`` has in :meth:`unformed_module`."""
            return self.linear_combination(
                self.unformed_module().framing_coefficients(element)
            )

        def pairing(self, left, right):
            return self.b(left, right)

        def left_module(self):
            return self

        def right_module(self):
            return self

        def value_module(self):
            return self.form().codomain()

        def Mor(self, codomain, category=None):
            if category is None and codomain in FormModules(self.base_ring()):
                return FormModules(self.base_ring()).Mor(self, codomain)
            return _category_homset(category, self, codomain)

        def Mono(self, codomain):
            r"""Return the form-preserving monomorphisms into ``codomain``."""
            return FormModules(self.base_ring()).Mono(self, codomain)

        def formed_hom(self, module_morphism, value_morphism):
            r"""Construct the general fixed-fiber formed morphism ``(f,h)``."""
            return self.Mor(module_morphism.codomain())(
                (module_morphism, value_morphism)
            )

        def fibered_formed_homset(self, codomain, ring_map):
            r"""Return formed morphisms from this module to ``codomain`` over ``ring_map``."""
            return FiberedFormedModuleHomset(self, codomain, ring_map)

        def fibered_formed_hom(self, codomain, ring_map, module_morphism, value_morphism):
            r"""Construct a formed morphism over a coefficient-ring map."""
            return self.fibered_formed_homset(codomain, ring_map)(
                (module_morphism, value_morphism)
            )

        def _Hom_(self, codomain, category=None):
            ring = self.base_ring()
            formed = FormModules(ring)
            if codomain in formed and (category is None or category.is_subcategory(formed)):
                return FormModules(ring).Mor(self, codomain)

            return self.module_category().Mor(self, codomain)

        def b(self, left, right):
            r"""Evaluate the (polar) bilinear form on two elements of this module."""
            if left not in self or right not in self:
                raise TypeError("a form pairs two elements of one formed module")
            form = self.form()
            if form.module() is not self:
                module = self.unformed_module()
                left, right = module(left), module(right)
            if _is_quadratic_form(form):
                return form.b(left, right)
            return form(left, right)

        def norm(self, element):
            r"""Return ``q(x)`` for a quadratic form, else ``b(x, x)``."""
            if element not in self:
                raise TypeError("the norm is defined on elements of this formed module")
            form = self.form()
            if form.module() is not self:
                element = self.unformed_module()(element)
            if _is_quadratic_form(form):
                return form(element)
            return form(element, element)

        def gram_tensor(self):
            r"""Return the scalar Gram as its intrinsic type-``(0,2)`` tensor."""
            form = self.form()
            return form.gram_tensor()

        def raise_index(self, tensor, slot=0):
            r"""Raise one lower tensor index using this formed module.

            The tensor owns the contraction algorithm.  This method is the
            formed-module-facing spelling of that same construction and does
            not introduce a second index-raising implementation.
            """
            return tensor.raise_index(self, slot)

        def raise_index_over_fraction_field(self, tensor, slot=0):
            r"""Raise one lower index after the canonical fraction-field extension.

            This is useful when the inverse Gram tensor is not integral.  Both
            the form and tensor are changed along the same canonical map
            ``R -> Frac(R)`` before the ordinary index-raising operation is
            applied.
            """
            ring_map = self.base_ring().fraction_field_map()
            changed_form = self.base_change(ring_map)
            changed_tensor = tensor.change_ring(changed_form.base_ring())
            return changed_tensor.raise_index(changed_form, slot)

        def lower_index(self, tensor, slot=0):
            r"""Lower one upper tensor index using this formed module."""
            return tensor.lower_index(self, slot)

        def twist(self, scalar):

            form = self._formed_form()
            if _is_bilinear_form(form):
                try:
                    values = form.coordinate_values().map(
                        lambda value: scalar * value,
                        name="Twisted bilinear coordinate values",
                    )
                except TypeError:
                    return FormModules(self.base_ring())(
                        self.bilinear_forms(self.value_module())(
                            lambda left, right: scalar * form(left, right)
                        )
                    )
                return FormModules(self.base_ring())(
                    self.bilinear_forms(self.value_module())(values)
                )
            try:
                values = form.lift_coordinate_values().map(
                    lambda value: scalar * value,
                    name="Twisted quadratic-lift coordinate values",
                )
            except TypeError:
                return FormModules(self.base_ring())(
                    self.quadratic_map(
                        self.value_module(),
                        lambda element: scalar * form(element),
                    )
                )
            return FormModules(self.base_ring())(
                self.quadratic_forms(self.value_module())(values)
            )

        base_change = _formed_module_base_change
    class ElementMethods:
        def b(self, other):
            r"""Return the polar bilinear value ``b(self, other)``."""
            return self.parent().b(self, other)

        def q(self):
            r"""Return the represented quadratic/norm value of this element."""
            return self.parent().norm(self)

        def is_isotropic(self) -> bool:
            r"""Return whether this element has zero represented norm."""
            return bool(self.q() == self.parent().value_module().zero())

        def is_orthogonal_to(self, other) -> bool:
            r"""Return whether the polar/bilinear value ``b(self, other)`` is zero."""
            return bool(self.b(other) == self.parent().value_module().zero())

        def represents(self, value) -> bool:
            r"""Return whether this element has represented norm ``value``.

            This is the elementwise statement ``q(self)=value``.  It does not
            answer the distinct existential question whether the whole formed
            module represents a selected value.
            """
            parent = self.parent()
            return bool(self.q() == parent.value_module()(value))

    class SubcategoryMethods:
        def Nondegenerate(self):
            r"""Return this category with the axiom that the correlation of the form has zero kernel."""
            return self._with_axiom("Nondegenerate")

        def Unimodular(self):
            r"""Return this category with the axiom that the correlation of the form is an isomorphism."""
            return self._with_axiom("Unimodular")

    class Nondegenerate(CategoryWithAxiom):
        r"""Form modules whose correlation morphism has zero kernel."""

        _certifying_predicate = "is_nondegenerate"

        def an_object(self):
            r"""The hyperbolic plane U, whose form is unimodular."""
            from dzack_research.preamble.categories.lattices import Lattices

            return Lattices(self.base_ring())("U")

    class Unimodular(CategoryWithAxiom):
        r"""Form modules whose correlation morphism is an isomorphism."""

        _certifying_predicate = "is_unimodular"

        def an_object(self):
            r"""The hyperbolic plane U."""
            from dzack_research.preamble.categories.lattices import Lattices

            return Lattices(self.base_ring())("U")

        def extra_super_categories(self):
            return [FormModules(self.base_ring()).Nondegenerate()]

    class FinitelyPresented(CategoryWithAxiom):
        r"""Form modules admitting a finite presentation."""

        def an_object(self):
            r"""The discriminant group of U."""
            from dzack_research.preamble.categories.lattices import Lattices

            return Lattices(self.base_ring())("U").discriminant_group()

        class ParentMethods:
            base_change = _formed_module_base_change


class BilinearFormModules(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The hyperbolic plane U, with its bilinear form."""
        from dzack_research.preamble.categories.lattices import Lattices

        return Lattices(self.base_ring())("U")

    @classmethod
    def _repr_object_names(cls):
        return "modules with a bilinear form"

    def super_categories(self):
        return [FormModules(self.base_ring())]

    _HomCategory = FormedModuleHomCategoryConstruction

    class ParentMethods:
        def q(self, vector):
            r"""Return the quadratic form \(q(v)=b(v,v)\) of the bilinear form.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: I2 = Lattices(ZZ)(ZZ^2)
                sage: I2.q(I2.module_generator(0))
                1
                sage: A2 = Lattices(ZZ)("A2")
                sage: A2.q(A2.module_generator(0))
                -2
            """
            return self.b(vector, vector)

    class SubcategoryMethods:
        def Symmetric(self):
            r"""Return this category with the axiom that the bilinear form is symmetric."""
            return self._with_axiom("Symmetric")

        def Even(self):
            r"""Return this category with the axiom that ``b(x, x)`` lies in ``2W`` for every ``x``."""
            return self._with_axiom("Even")

    class Symmetric(CategoryWithAxiom):
        r"""Modules with a symmetric bilinear form."""

        def an_object(self):
            r"""The hyperbolic plane U, whose form is symmetric."""
            from dzack_research.preamble.categories.lattices import Lattices

            return Lattices(self.base_ring())("U")

        class ParentMethods:
            def to_quadratic_module(self):
                r"""Return ``q(v)=b(v,v)/2`` when this symmetric form is even.

                Over rings where ``2`` is not a unit this is genuinely extra
                structure: the quotient must lie back in the coefficient ring.
                The represented construction is checked on a finite framing; the
                cross terms need no further divisibility test because symmetry
                contributes them with the factor ``2`` in ``b(v,v)``.
                """
                assert self.module_rank().is_finite(), (
                    "conversion of an even bilinear form to a quadratic form requires a finite framing"
                )
                ring = self.base_ring()
                two = ring(2)
                zero = ring.zero()
                unformed = self.unformed_module()

                def half(value):
                    value = ring(value)
                    quotient, remainder = value.quo_rem(two)
                    if remainder != zero:
                        raise ValueError(
                            "the symmetric bilinear form is not even over its coefficient ring"
                        )
                    return quotient

                def half_norm(element):
                    element = self(element)
                    return half(self.b(element, element))

                for generator in unformed.module_generators():
                    half_norm(generator)

                return unformed.equip_quadratic_form(ring, half_norm)

            def algebraic_correlation_morphism(self):

                return _algebraic_correlation_morphism(self)

            def correlation_isomorphism(self):

                return _correlation_isomorphism(self)

            def hodge_discriminant(self, volume):

                return _hodge_discriminant(self, volume)

            def hodge_star(self, volume, degree):

                return _hodge_star(self, volume, degree)

            def hodge_star_over_fraction_field(self, volume, degree):

                return _hodge_star_over_fraction_field(self, volume, degree)

            def multivector_hodge_star(self, volume, degree):

                return _multivector_hodge_star(self, volume, degree)

    class Even(CategoryWithAxiom):
        r"""Modules with a bilinear form satisfying ``b(x, x) in 2W`` for every ``x``."""

        _certifying_predicate = "is_even"

        def an_object(self):
            r"""The hyperbolic plane U, on which every square is even."""
            from dzack_research.preamble.categories.lattices import Lattices

            return Lattices(self.base_ring())("U")

    class FinitelyPresented(CategoryWithAxiom):
        r"""Finitely presented modules with a bilinear form."""

        def an_object(self):
            r"""The discriminant group of U."""
            from dzack_research.preamble.categories.lattices import Lattices

            return Lattices(self.base_ring())("U").discriminant_group()

        class Torsion(CategoryWithAxiom):
            r"""Finitely presented torsion modules with a bilinear form."""

            def an_object(self):
                r"""The discriminant group of U, a torsion module with a form."""
                from dzack_research.preamble.categories.lattices import Lattices

                return Lattices(self.base_ring())("U").discriminant_group()

            _IsoCategory = TorsionBilinearFormIsoCategoryConstruction

            def from_module(
                self,
                module,
                gram,
                value_module,
                *,
                _subobject_ambient=None,
                _subobject_generator_images=None,
                _subobject_lift=None,
                _subobject_inclusion_factory=None,
                _subobject_verify_linearity=True,
                _extra_categories=(),
            ):
                r"""Equip ``module`` with the bilinear form represented by ``gram``.

                The value object is explicit.  Descent is checked on both arguments:
                every chosen relation must pair to zero with every chosen generator.
                """
                if module not in Modules(self.base_ring()).FinitelyPresented().Torsion():
                    module = _refine_finitely_presented_torsion_module(module)

                rank = int(module.module_generating_set().cardinality())
                values = _coerced_gram(value_module, gram, rank)
                relations = _presentation_matrix(module)
                if not _bilinear_descends(relations, values, value_module):
                    raise ValueError("the bilinear form does not descend through the selected relations")
                formed = FormModules(module.base_ring())(
                    module.bilinear_forms(value_module)(values),
                    _extra_categories=(self, *tuple(_extra_categories)),
                    _subobject_ambient=_subobject_ambient,
                    _subobject_generator_images=_subobject_generator_images,
                    _subobject_lift=_subobject_lift,
                    _subobject_inclusion_factory=_subobject_inclusion_factory,
                    _subobject_verify_linearity=_subobject_verify_linearity,
                )
                return formed

            def from_relations_and_gram(self, relations, gram, value_module, module_generating_set=None):
                r"""Construct a torsion bilinear form from presentation and Gram data."""

                module = _torsion_module_presented_by_matrix(relations, module_generating_set)
                return self.from_module(module, gram, value_module)

            def cokernel(self, morphism):
                r"""Return the quotient-valued bilinear form on the literal finite cokernel of ``morphism``."""
                cover = morphism.codomain()
                if cover.base_ring() is not self.base_ring():
                    raise ValueError("the cokernel form must stay over the selected base ring")
                module = morphism.cokernel()
                values = FractionFieldQuotients(self.base_ring())(1)
                generators = tuple(cover.module_generators())
                gram = tuple(
                    tuple(values(cover.b(left, right)) for right in generators)
                    for left in generators
                )
                return self.from_module(
                    module,
                    gram,
                    values,
                    _extra_categories=(CokernelTorsionFormModules(self.base_ring()),),
                )

            @cached_method
            def twist_functor(self, scalar):
                r"""Return the endofunctor ``(A,b) |-> (A, scalar*b)`` of this category."""
                return TorsionFormTwistFunctor(self, scalar, quadratic=False)

            class ParentMethods:
                @cached_method
                def scale_submodule(self):
                    r"""Return the submodule of the value module generated by pairing values."""
                    return self.form().image()

                def subobject_generated_by(self, generators):
                    r"""Return the span as a bilinear-form-bearing subobject."""
                    return _torsion_form_subobject_on(self, generators, quadratic=False)

                def primary_part(self, prime):
                    r"""Return the ``prime``-primary bilinear-form-bearing subobject."""
                    return _torsion_form_primary_part(self, prime, quadratic=False)

                @cached_method
                def isotropic_subobjects(self):
                    r"""Return all subobjects on which the bilinear form vanishes."""
                    return _torsion_form_isotropic_subobjects(self, quadratic=False)

                @cached_method
                def maximal_isotropic_subobjects(self):
                    r"""Return the bilinear-isotropic subobjects maximal by inclusion."""
                    return _torsion_form_maximal_isotropic_subobjects(self, quadratic=False)

                def form_vanishes_on(self, elements) -> bool:
                    elements = tuple(elements)
                    return all(self.b(left, right) == self.value_module().zero() for left in elements for right in elements)


                def gram_matrix(self):
                    r"""Return canonical rational representatives of the finite-form Gram values."""
                    representative = _representative_gram(self, quadratic=False)
                    rows, columns = map(int, representative.tensor_shape())
                    return representative.base_ring().matrix_space(rows, columns).from_rows(
                        tuple(
                            tuple(representative[row, column] for column in range(columns))
                            for row in range(rows)
                        )
                    )

                @cached_method(key=lambda self, generators: tuple(id(generator) for generator in generators))
                def reframing_isometry(self, generators):
                    r"""Return the explicit isometry to this form on the selected generating family."""
                    return _regenerate_form_on_generators(
                        self, tuple(generators), quadratic=False
                    )

                def regenerate(self, generators):
                    r"""Return this finite form written on the selected generating family."""
                    return self.reframing_isometry(generators).codomain()

                @cached_method
                def primary_components(self):
                    r"""Return the prime-indexed family of primary form-bearing subobjects."""
                    primes = finite_ordered_set(
                        tuple(
                            sorted(
                                {
                                    prime
                                    for invariant in self.invariant_factors()
                                    for prime in abs(invariant).prime_divisors()
                                }
                            )
                        )
                    )
                    return indexed_family(
                        primes,
                        lambda prime: self.primary_part(prime),
                        name=f"Primary components of {self}",
                    )

                primary_decomposition = primary_components


                @cached_method
                def subobjects(self):
                    r"""Return all form-bearing subobjects of this finite form."""
                    return _torsion_form_all_subobjects(self, quadratic=False)

                def orbit(self, element, group=None):
                    r"""Return the orbit of ``element`` under ``group`` or the full orthogonal group."""
                    acting = self.automorphism_group() if group is None else group
                    return acting.orbit(self(element))

                @cached_method
                def orbits(self, group=None):
                    r"""Return the orbit partition of the finite underlying module."""
                    acting = self.automorphism_group() if group is None else group
                    action = _torsion_form_element_action(self, acting)
                    return finite_ordered_set(
                        tuple(orbit.points() for orbit in action.orbits())
                    )

                def orbits_on_subobjects(self, group=None):
                    r"""Return the orthogonal-group orbits on all form-bearing subobjects."""
                    acting = self.automorphism_group() if group is None else group
                    return _torsion_form_subobject_orbits(
                        self, self.subobjects(), acting
                    )

                def orbits_on_isotropic_subobjects(self, group=None):
                    r"""Return the orthogonal-group orbits on isotropic subobjects."""
                    acting = self.automorphism_group() if group is None else group
                    return _torsion_form_subobject_orbits(
                        self, self.isotropic_subobjects(), acting
                    )

                def is_anisotropic(self) -> bool:
                    zero = self.zero()
                    return all(
                        not self.form_vanishes_on((element,))
                        for element in self.elements()
                        if element != zero
                    )

                def orthogonal_subobject(self, subobject):
                    return _torsion_form_orthogonal_subobject(
                        self, subobject, quadratic=False
                    )

                @cached_method
                def lagrangian_subobjects(self):
                    return _torsion_form_lagrangian_subobjects(self, quadratic=False)

                def is_metabolic(self) -> bool:
                    return self.lagrangian_subobjects().cardinality() != 0

                def metabolizer(self):
                    lagrangians = self.lagrangian_subobjects()
                    if lagrangians.cardinality() == 0:
                        raise ValueError("this finite form has no metabolizer")
                    return lagrangians[0]

                def restricted_form(self, subobject):
                    if subobject.inclusion().codomain() is not self:
                        raise ValueError("the restricted form requires a subobject of this form")
                    return subobject

                def subquotient_form(self, subobject, over):
                    return _torsion_form_subquotient(
                        self, subobject, over, quadratic=False
                    )

                def orthogonal_quotient(self, subobject):
                    perpendicular = self.orthogonal_subobject(subobject)
                    return self.subquotient_form(subobject, perpendicular)

                @cached_method
                def invariant_factor_form(self):
                    r"""Return the form-preserving isomorphism to invariant-factor framing."""
                    return _invariant_factor_form_isomorphism(self, quadratic=False)

                def p_adic_jordan_decomposition(self):
                    r"""Return the chosen Jordan generators indexed by their prime."""
                    return _p_adic_jordan_decomposition(self, quadratic=False)

                def p_adic_jordan_module_generators(self):
                    r"""Return the chosen prime-by-prime Jordan generating family."""
                    return _p_adic_jordan_module_generators(self, quadratic=False)

                def p_adic_jordan_form(self):
                    r"""Return the explicit isometry to this form in Jordan framing."""
                    return _p_adic_jordan_form(self, quadratic=False)

                normal_form = p_adic_jordan_form

                def normal_form_isometry(self):
                    r"""Return the normal-form-to-original morphism."""
                    return self.normal_form().inverse()

                def twist(self, scalar):
                    r"""Return the same finite module equipped with ``scalar*b``."""
                    return TorsionBilinearFormModules(self.base_ring()).twist_functor(scalar)(self)

                def is_isomorphic(self, other) -> bool:
                    r"""Decide isometry of represented finite symmetric bilinear forms."""
                    if other not in TorsionBilinearFormModules(self.base_ring()):
                        return False
                    return _forms_are_isomorphic(self, other, quadratic=False)

                is_isometric_to = is_isomorphic

                def is_anti_isometric(self, other) -> bool:
                    r"""Return whether ``(self,b)`` is isometric to ``(other,-b)``."""
                    if other not in TorsionBilinearFormModules(self.base_ring()):
                        return False
                    return self.is_isomorphic(other.twist(-1))

                def pontryagin_dual_identification(self):
                    r"""Return ``A -> Hom(A,K/R)``, ``x |-> b(x,-)``, for perfect ``b``."""
                    from sage.categories.morphism import SetMorphism



                    zero = self.zero()
                    generators = tuple(self.module_generators())
                    if any(
                        element != zero
                        and all(self.b(element, generator) == self.value_module().zero() for generator in generators)
                        for element in self.elements()
                    ):
                        raise ValueError(
                            "the pairing does not identify this module with its Pontryagin dual because it is degenerate"
                        )
                    characters = self.module_category().Mor(self, self.value_module())

                    def character(element):
                        element = self(element)
                        return characters(
                            {
                                label: self.b(element, self.module_generator(label))
                                for label in self.module_generating_set()
                            }
                        )

                    return SetMorphism(OwnedSets().Mor(self, characters), character)

                @cached_method
                def automorphism_group(self):
                    r"""Return ``O(A,b)`` as a finite owned group of live automorphisms."""
                    return _torsion_form_automorphism_group(self, quadratic=False)

                def orthogonal_group(self):
                    return self.automorphism_group()

                def O(self):  # noqa: E743 - standard mathematical notation O(A,b)
                    return self.automorphism_group()


class QuadraticFormModules(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The discriminant group of U, which carries a quadratic form."""
        from dzack_research.preamble.categories.lattices import Lattices

        return Lattices(self.base_ring())("U").discriminant_group()

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
            return self.norm(element)

        def associated_bilinear_module(self):
            r"""Return the bilinear module polarized from this quadratic form.

            The result is a distinct formed object on the same unformed
            module.  Its form is

            ``b_q(x,y)=q(x+y)-q(x)-q(y)``.

            This generic construction keeps the same scalar value ring.  A
            discriminant quadratic form valued in ``K/2R`` polarizes into a
            different quotient ``K/R`` and is handled by its specialized
            discriminant-form owner instead.
            """
            assert self.value_module() is self.base_ring(), (
                "generic quadratic-form polarization requires scalar-ring values; "
                "changed quotient values belong to the specialized quadratic-form owner"
            )
            unformed = self.unformed_module()
            return unformed.equip_bilinear_form(
                self.value_module(),
                lambda left, right: (
                    self.norm(self(left) + self(right))
                    - self.norm(self(left))
                    - self.norm(self(right))
                ),
            )

    class FinitelyPresented(CategoryWithAxiom):
        r"""Finitely presented modules with a quadratic form."""

        def an_object(self):
            r"""The discriminant group of U."""
            from dzack_research.preamble.categories.lattices import Lattices

            return Lattices(self.base_ring())("U").discriminant_group()

        class Torsion(CategoryWithAxiom):
            r"""Finitely presented torsion modules with a quadratic form."""

            def an_object(self):
                r"""The discriminant group of U."""
                from dzack_research.preamble.categories.lattices import Lattices

                return Lattices(self.base_ring())("U").discriminant_group()

            _IsoCategory = TorsionQuadraticFormIsoCategoryConstruction

            def from_module(
                self,
                module,
                gram,
                value_module,
                *,
                _subobject_ambient=None,
                _subobject_generator_images=None,
                _subobject_lift=None,
                _subobject_inclusion_factory=None,
                _subobject_verify_linearity=True,
                _extra_categories=(),
            ):
                r"""Equip ``module`` with ``q(x)=x^T gram x`` valued in ``value_module``.

                For every relation ``r`` we check both ``q(r)=0`` and vanishing of the
                polar value ``q(x+r)-q(x)-q(r)`` against every generator.  These are
                exactly the conditions for the quadratic map to descend to the quotient.
                """
                if module not in Modules(self.base_ring()).FinitelyPresented().Torsion():
                    module = _refine_finitely_presented_torsion_module(module)

                rank = int(module.module_generating_set().cardinality())
                values = _coerced_gram(value_module, gram, rank)
                if any(values[i][j] != values[j][i] for i in range(rank) for j in range(rank)):
                    raise ValueError("the chosen bilinear lift of a quadratic form must be symmetric")
                relations = _presentation_matrix(module)
                if not _quadratic_descends(relations, values, value_module):
                    raise ValueError("the quadratic form does not descend through the selected relations")
                formed = FormModules(module.base_ring())(
                    module.quadratic_forms(value_module)(values),
                    _extra_categories=(self, *tuple(_extra_categories)),
                    _subobject_ambient=_subobject_ambient,
                    _subobject_generator_images=_subobject_generator_images,
                    _subobject_lift=_subobject_lift,
                    _subobject_inclusion_factory=_subobject_inclusion_factory,
                    _subobject_verify_linearity=_subobject_verify_linearity,
                )
                return formed

            def from_relations_and_gram(self, relations, gram, value_module, module_generating_set=None):
                r"""Construct a torsion quadratic form from presentation and Gram data."""

                module = _torsion_module_presented_by_matrix(relations, module_generating_set)
                return self.from_module(module, gram, value_module)

            def cokernel(self, morphism):
                r"""Return the quotient-valued quadratic form on the literal finite cokernel of ``morphism``."""
                cover = morphism.codomain()
                if cover.base_ring() is not self.base_ring():
                    raise ValueError("the cokernel form must stay over the selected base ring")
                module = morphism.cokernel()
                values = FractionFieldQuotients(self.base_ring())(2)
                generators = tuple(cover.module_generators())
                gram = tuple(
                    tuple(values(cover.b(left, right)) for right in generators)
                    for left in generators
                )
                return self.from_module(
                    module,
                    gram,
                    values,
                    _extra_categories=(CokernelTorsionFormModules(self.base_ring()),),
                )

            @cached_method
            def twist_functor(self, scalar):
                r"""Return the endofunctor ``(A,q) |-> (A, scalar*q)`` of this category."""
                return TorsionFormTwistFunctor(self, scalar, quadratic=True)

            class ParentMethods:
                @cached_method
                def scale_submodule(self):
                    r"""Return the submodule of the value module generated by quadratic values."""
                    values = tuple(self.q(element) for element in self.elements())
                    return self.value_module().subobject_on(values)

                def subobject_generated_by(self, generators):
                    r"""Return the span as a quadratic-form-bearing subobject."""
                    return _torsion_form_subobject_on(self, generators, quadratic=True)

                def primary_part(self, prime):
                    r"""Return the ``prime``-primary quadratic-form-bearing subobject."""
                    return _torsion_form_primary_part(self, prime, quadratic=True)

                @cached_method
                def isotropic_subobjects(self):
                    r"""Return all subobjects on which the quadratic form vanishes."""
                    return _torsion_form_isotropic_subobjects(self, quadratic=True)

                @cached_method
                def maximal_isotropic_subobjects(self):
                    r"""Return the quadratic-isotropic subobjects maximal by inclusion."""
                    return _torsion_form_maximal_isotropic_subobjects(self, quadratic=True)

                def form_vanishes_on(self, elements) -> bool:
                    return all(self.q(element) == self.value_module().zero() for element in elements)


                def gram_matrix(self):
                    r"""Return canonical rational representatives of the finite-form Gram values."""
                    representative = _representative_gram(self, quadratic=True)
                    rows, columns = map(int, representative.tensor_shape())
                    return representative.base_ring().matrix_space(rows, columns).from_rows(
                        tuple(
                            tuple(representative[row, column] for column in range(columns))
                            for row in range(rows)
                        )
                    )

                @cached_method(key=lambda self, generators: tuple(id(generator) for generator in generators))
                def reframing_isometry(self, generators):
                    r"""Return the explicit isometry to this form on the selected generating family."""
                    return _regenerate_form_on_generators(
                        self, tuple(generators), quadratic=True
                    )

                def regenerate(self, generators):
                    r"""Return this finite form written on the selected generating family."""
                    return self.reframing_isometry(generators).codomain()

                @cached_method
                def primary_components(self):
                    r"""Return the prime-indexed family of primary form-bearing subobjects."""
                    primes = finite_ordered_set(
                        tuple(
                            sorted(
                                {
                                    prime
                                    for invariant in self.invariant_factors()
                                    for prime in abs(invariant).prime_divisors()
                                }
                            )
                        )
                    )
                    return indexed_family(
                        primes,
                        lambda prime: self.primary_part(prime),
                        name=f"Primary components of {self}",
                    )

                primary_decomposition = primary_components


                @cached_method
                def subobjects(self):
                    r"""Return all form-bearing subobjects of this finite form."""
                    return _torsion_form_all_subobjects(self, quadratic=True)

                def orbit(self, element, group=None):
                    r"""Return the orbit of ``element`` under ``group`` or the full orthogonal group."""
                    acting = self.automorphism_group() if group is None else group
                    return acting.orbit(self(element))

                @cached_method
                def orbits(self, group=None):
                    r"""Return the orbit partition of the finite underlying module."""
                    acting = self.automorphism_group() if group is None else group
                    action = _torsion_form_element_action(self, acting)
                    return finite_ordered_set(
                        tuple(orbit.points() for orbit in action.orbits())
                    )

                def orbits_on_subobjects(self, group=None):
                    r"""Return the orthogonal-group orbits on all form-bearing subobjects."""
                    acting = self.automorphism_group() if group is None else group
                    return _torsion_form_subobject_orbits(
                        self, self.subobjects(), acting
                    )

                def orbits_on_isotropic_subobjects(self, group=None):
                    r"""Return the orthogonal-group orbits on isotropic subobjects."""
                    acting = self.automorphism_group() if group is None else group
                    return _torsion_form_subobject_orbits(
                        self, self.isotropic_subobjects(), acting
                    )

                def is_anisotropic(self) -> bool:
                    zero = self.zero()
                    return all(
                        not self.form_vanishes_on((element,))
                        for element in self.elements()
                        if element != zero
                    )

                def orthogonal_subobject(self, subobject):
                    return _torsion_form_orthogonal_subobject(
                        self, subobject, quadratic=True
                    )

                @cached_method
                def lagrangian_subobjects(self):
                    return _torsion_form_lagrangian_subobjects(self, quadratic=True)

                def is_metabolic(self) -> bool:
                    return self.lagrangian_subobjects().cardinality() != 0

                def metabolizer(self):
                    lagrangians = self.lagrangian_subobjects()
                    if lagrangians.cardinality() == 0:
                        raise ValueError("this finite form has no metabolizer")
                    return lagrangians[0]

                def restricted_form(self, subobject):
                    if subobject.inclusion().codomain() is not self:
                        raise ValueError("the restricted form requires a subobject of this form")
                    return subobject

                def subquotient_form(self, subobject, over):
                    return _torsion_form_subquotient(
                        self, subobject, over, quadratic=True
                    )

                def orthogonal_quotient(self, subobject):
                    perpendicular = self.orthogonal_subobject(subobject)
                    return self.subquotient_form(subobject, perpendicular)

                @cached_method
                def invariant_factor_form(self):
                    r"""Return the quadratic-form isomorphism to invariant-factor framing."""
                    return _invariant_factor_form_isomorphism(self, quadratic=True)

                def p_adic_jordan_decomposition(self):
                    r"""Return the chosen quadratic Jordan generators indexed by prime."""
                    return _p_adic_jordan_decomposition(self, quadratic=True)

                def p_adic_jordan_module_generators(self):
                    r"""Return the chosen prime-by-prime quadratic Jordan generators."""
                    return _p_adic_jordan_module_generators(self, quadratic=True)

                def p_adic_jordan_form(self):
                    r"""Return the explicit isometry to this quadratic form in Jordan framing."""
                    return _p_adic_jordan_form(self, quadratic=True)

                normal_form = p_adic_jordan_form

                def normal_form_isometry(self):
                    r"""Return the normal-form-to-original morphism."""
                    return self.normal_form().inverse()

                def twist(self, scalar):
                    r"""Return the same finite module equipped with ``scalar*q``."""
                    return TorsionQuadraticFormModules(self.base_ring()).twist_functor(scalar)(self)

                def is_isomorphic(self, other) -> bool:
                    r"""Decide isometry of represented finite quadratic forms."""
                    if other not in TorsionQuadraticFormModules(self.base_ring()):
                        return False
                    return _forms_are_isomorphic(self, other, quadratic=True)

                is_isometric_to = is_isomorphic

                def is_anti_isometric(self, other) -> bool:
                    r"""Return whether ``(self,q)`` is isometric to ``(other,-q)``."""
                    if other not in TorsionQuadraticFormModules(self.base_ring()):
                        return False
                    return self.is_isomorphic(other.twist(-1))

                @cached_method
                def automorphism_group(self):
                    r"""Return ``O(A,q)`` as a finite owned group of live automorphisms."""
                    return _torsion_form_automorphism_group(self, quadratic=True)

                def orthogonal_group(self):
                    return self.automorphism_group()

                def O(self):  # noqa: E743 - standard mathematical notation O(A,q)
                    return self.automorphism_group()

                def associated_bilinear_form(self):
                    r"""Polarize ``q:A->QQ/2ZZ`` to ``b_q:A^2->QQ/ZZ``.

                    If ``q(x)=x^T G x`` modulo ``2ZZ``, then
                    ``b_q(x,y)=x^T G y`` modulo ``ZZ``.  The halving of the ordinary
                    polar value is well defined precisely because changing a lift in
                    ``QQ/2ZZ`` by ``2ZZ`` changes its half by ``ZZ``.
                    """
                    value_module = self.value_module()
                    if not hasattr(value_module, "modulus") or value_module.modulus() != 2:
                        raise TypeError("this polarization currently requires a QQ/2ZZ-valued quadratic form")

                    bilinear_values = FractionFieldQuotients(self.base_ring())(1)
                    quadratic_form = self.form()
                    module = self.unformed_module()

                    associated = FormModules(module.base_ring())(
                        module.bilinear_forms(bilinear_values)(
                            lambda left, right: bilinear_values(
                                value_module.lift(
                                    quadratic_form.lift_pairing(left, right)
                                )
                            )
                        ),
                        _extra_categories=(TorsionBilinearFormModules(self.base_ring()),),
                    )
                    return associated


SymmetricBilinearFormModules = BilinearFormModules.Symmetric
TorsionBilinearFormModules = BilinearFormModules.FinitelyPresented.Torsion
TorsionQuadraticFormModules = QuadraticFormModules.FinitelyPresented.Torsion


class FreeFormModules(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The hyperbolic plane U, free and carrying a form."""
        from dzack_research.preamble.categories.lattices import Lattices

        return Lattices(self.base_ring())("U")

    def additional_condition(self):
        r"""None: a free form module is exactly a form module that is framed free."""
        return None

    @classmethod
    def _repr_object_names(cls):
        return "free form modules"

    def super_categories(self):

        return [FormModules(self.base_ring()), FramedFreeModules(self.base_ring())]

    class ParentMethods:
        base_change = _formed_module_base_change

        def subobject_on(self, module_generating_set):
            r"""Return the span equipped with the pulled-back form."""

            basis = _span_basis_elements(self, module_generating_set)
            return _form_subobject_spanning(self, basis)

    class FinitelyGenerated(CategoryWithAxiom):
        r"""Form modules framed by a finite basis."""

        def an_object(self):
            r"""The hyperbolic plane U."""
            from dzack_research.preamble.categories.lattices import Lattices

            return Lattices(self.base_ring())("U")

        class ParentMethods:
            base_change = _formed_module_base_change

            def gram_matrix(self, basis=None):
                r"""Return the coordinate matrix of the selected finite free form."""
                selected = tuple(self.module_generators()) if basis is None else tuple(basis)
                if any(vector.parent() is not self for vector in selected):
                    raise ValueError("a Gram matrix basis consists of vectors of this formed module")
                size = len(selected)
                return self.value_module().matrix_space(size, size).from_rows(
                    tuple(tuple(self.b(left, right) for right in selected) for left in selected)
                )

            @cached_method
            def dual_module(self):

                return self.base_ring().free_module(self.module_generating_set())

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

                return self.module_category().Mor(self, dual)(images)

            @cached_method
            def radical(self):
                r"""Return ``rad(M)=ker(M -> M^vee)`` as an actual module subobject.

                This is the radical of the represented scalar-valued bilinear
                form.  It is defined by the correlation morphism, so the kernel
                construction remains authoritative and no second Gram-kernel
                computation is introduced here.
                """
                if self.value_module() is not self.base_ring():
                    raise TypeError("the radical via correlation requires a scalar-valued form")
                return self.correlation_morphism().kernel()

            @cached_method
            def radical_quotient(self):
                r"""Return ``M/rad(M)`` equipped with the descended form.

                The underlying module is the literal cokernel of the radical
                inclusion.  Since the radical pairs trivially with all of ``M``,
                the selected form descends through that cokernel with unchanged
                values; the returned formed module is built from that descended
                form rather than from an isomorphic quotient presentation.
                """
                radical = self.radical()
                inclusion = radical.inclusion()
                value_module = self.value_module()
                value_identity = value_module.module_category().Mor(value_module, value_module).identity()
                descended = self._formed_form().descend_along(inclusion, value_identity)
                return FormModules(descended.module().base_ring())(descended)

            def determinant(self):
                r"""Return the Gram determinant of a form with values in a ring containing ``R``."""
                assert self.value_module() in OwnedRings(), (
                    "the determinant of a form is defined for ring-valued forms"
                )
                return self.gram_matrix().determinant()

            def is_nondegenerate(self) -> bool:
                r"""Whether the Gram determinant is nonzero, for values in an integral domain."""
                value = self.value_module()
                assert value in OwnedRings() and _engine_ring(value).is_integral_domain(), (
                    "nondegeneracy by the Gram determinant needs values in an integral domain"
                )
                return self.determinant() != 0

            def is_unimodular(self) -> bool:
                r"""Return whether the correlation morphism is an isomorphism."""
                assert self.value_module() is self.base_ring()
                return bool(self.determinant().is_unit())

            def scale_submodule(self):
                assert self.value_module() is self.base_ring()

                return _engine_ring(self.base_ring()).ideal(self.gram_tensor().list())


def _form_module(
    form,
    *,
    _extra_categories=(),
    _extra_construction_data=None,
    _subobject_ambient=None,
    _subobject_generator_images=None,
    _subobject_lift=None,
    _subobject_inclusion_factory=None,
    _subobject_verify_linearity=True,
):
    r"""Return the same represented module construction equipped with ``form``.

    The result remains a module object; it is not a wrapper around an
    ``underlying`` module.  A distinct represented parent is used so that two
    different selected forms on isomorphic modules remain distinct structured
    objects.
    """

    if not (_is_bilinear_form(form) or _is_quadratic_form(form)):
        raise TypeError("a formed module is classified by a bilinear or quadratic form")
    module = form.module()
    base_ring = module.base_ring()
    labels = module.module_generating_set()
    categories = [FormModules(base_ring)]
    if module in VectorSpaces(base_ring):
        categories.append(VectorSpaces(base_ring))
    is_free = module in FramedFreeModules(base_ring)
    is_presented = module in ModulesWithChosenFinitePresentation(base_ring)
    if is_free:
        categories.append(FreeFormModules(base_ring))
    if is_presented:
        categories.append(FormModules(base_ring).FinitelyPresented())
    if module in FramedFreeModules(base_ring).FinitelyGenerated():
        categories.append(FreeFormModules(base_ring).FinitelyGenerated())
    if _is_bilinear_form(form):
        categories.append(BilinearFormModules(base_ring))
        try:
            symmetric = form.gram_tensor().is_symmetric()
        except TypeError:
            symmetric = False
        if symmetric:
            categories.append(BilinearFormModules(base_ring).Symmetric())
    else:
        categories.append(QuadraticFormModules(base_ring))
    categories.extend(tuple(_extra_categories))
    construction_data = dict(_extra_construction_data or {})
    construction_data["source_form"] = form
    common = {
        "_subobject_ambient": _subobject_ambient,
        "_subobject_generator_images": _subobject_generator_images,
        "_subobject_lift": _subobject_lift,
        "_subobject_inclusion_factory": _subobject_inclusion_factory,
        "_subobject_verify_linearity": _subobject_verify_linearity,
        "_extra_categories": tuple(categories),
        "_extra_construction_data": construction_data,
    }
    if is_free:
        return base_ring._fresh_free_module_on(labels, **common)
    if is_presented:
        from sage.categories.category import Category
        from dzack_research.preamble.categories.modules.pure.modules import ModuleSubobjects

        if _subobject_ambient is not None or _subobject_inclusion_factory is not None:
            categories.append(ModuleSubobjects(base_ring))
            if _subobject_ambient is not None:
                categories.append(Modules(base_ring).Subobjects(_subobject_ambient))
            construction_data.update(
                subobject_ambient=_subobject_ambient,
                subobject_generator_images=_subobject_generator_images,
                subobject_lift=_subobject_lift,
                subobject_inclusion_factory=_subobject_inclusion_factory,
                subobject_verify_linearity=_subobject_verify_linearity,
            )
        return ModulesWithChosenFinitePresentation(base_ring)(
            module.presentation(), category=Category.join(categories), **construction_data
        )
    raise TypeError(
        "the active formed-module constructor requires a framed free or chosen finitely presented module"
    )


@cached_function(key=lambda module, basis: (id(module), basis))
def _form_subobject_spanning(module, basis):
    r"""Return the canonical formed subobject on a finite span basis."""

    labels, embedded, lift = _module_subobject_constructor_data(module, basis)
    free_source = module.base_ring().free_module(labels)
    preliminary = free_source.Mono(module)(embedded)

    def inclusion_factory(source):
        return source.Mono(module)(embedded)

    return FormModules(module.base_ring())(
        module._formed_form().pullback(preliminary),
        _subobject_ambient=module,
        _subobject_generator_images=embedded,
        _subobject_lift=lift,
        _subobject_inclusion_factory=inclusion_factory,
    )


def _bilinear_form(module, value_module, datum):
    r"""Return ``module`` equipped with the stated bilinear form."""

    return FormModules(module.base_ring())(
        module.bilinear_forms(value_module)(datum)
    )


def _quadratic_form(module, value_module, datum):
    r"""Return ``module`` equipped with the stated quadratic form."""

    coordinate_datum = (
        isinstance(datum, IndexedFamily)
        or hasattr(datum, "rows")
        or (
            isinstance(datum, (tuple, list))
            and all(isinstance(row, (tuple, list)) for row in datum)
        )
    )
    form = (
        module.quadratic_forms(value_module)(datum)
        if coordinate_datum
        else module.quadratic_map(value_module, datum)
    )
    return FormModules(module.base_ring())(form)
