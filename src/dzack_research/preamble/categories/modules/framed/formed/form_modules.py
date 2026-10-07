r"""Modules equipped with exact bilinear or quadratic forms."""

from collections.abc import Iterable

from sage.categories.category_with_axiom import all_axioms
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.structure.richcmp import op_EQ

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
    MonoCategoryConstruction,
    _category_mor_parent,
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
    _base_change_element,
    _base_change_scalar,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FramedFreeModules,
    _module_subobject_spanning,
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
    ModuleMorphismMethods,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    _relation_images,
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
    MatrixSpaces,
    Modules,
    ModulesWithChosenFinitePresentation,
    TensorProductModules,
    VectorSpaces,
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
from dzack_research.preamble.tensors.tensor import tensor
from dzack_research.preamble.validation import validator

for _form_axiom in ("Symmetric", "Nondegenerate", "Unimodular", "Even"):
    if _form_axiom not in all_axioms:
        all_axioms.add(_form_axiom)


def _is_bilinear_form(form) -> bool:

    return _form_is_bilinear(form)


def _is_quadratic_form(form) -> bool:

    return _form_is_quadratic(form)


def _has_finite_framing(module) -> bool:
    ring = module.base_ring()
    return (
        module.has_selected_module_resolution()
        and module.module_generating_set().cardinality().is_finite()
    )


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
        except (TypeError, ValueError, NotImplementedError) as error:
            raise TypeError(
                f"the form value ring {value} does not carry the required represented {ring}-module structure"
            ) from error
    raise TypeError(
        f"the form on {formed_module} takes values in {value}, which is neither an "
        f"{ring}-module nor a ring receiving a map from {ring}, so it cannot serve as a value module"
    )


def _value_as_module_element(formed_module, value):
    represented = _represented_value_module(formed_module)
    if represented is formed_module.value_module():
        return represented(value)
    extension = represented.module_over_extension()
    unit_label = extension.module_generating_set()[0]
    return represented.wrap(
        extension.linear_combination(
            {unit_label: formed_module.value_module()(value)}
        )
    )


def _value_from_module_element(formed_module, element):
    represented = _represented_value_module(formed_module)
    if represented is formed_module.value_module():
        return represented(element)

    extension = represented.module_over_extension()
    restricted_element = represented(element)
    coordinates = extension.framing_morphism().lift(restricted_element.underlying_element())
    unit_label = extension.module_generating_set()[0]
    return formed_module.value_module()(coordinates(unit_label))


def _mapped_value(domain, codomain, value_morphism, value):
    r"""Return ``h(v)`` for a form value ``v`` of ``domain`` and the value map ``h``."""
    return _value_from_module_element(
        codomain, value_morphism(_value_as_module_element(domain, value))
    )


def _form_square_commutes(domain, codomain, module_morphism, value_morphism) -> bool:
    r"""Whether ``h(b_M(x, y)) = b_N(f(x), f(y))`` for the pair ``(f, h)`` from ``M`` to ``N``.

    When both forms are bilinear and ring-valued, ``h`` is the identity and
    ``f`` is a map of framed free modules of finite rank, the square is the
    tensor equation ``f^* G_N = G_M``: the Gram tensor of ``N`` pulled back
    along ``f`` is the Gram tensor of ``M``, and :meth:`Tensor.pullback` owns
    that contraction (``OWN-24``).  Otherwise no Gram tensor states the
    square, and it is decided on generators: a bilinear form is determined by
    its values on pairs of module generators, and a quadratic form ``q`` by
    ``q(s)`` and ``q(s + t)`` on generators.
    """
    source_form = domain.form()
    target_form = codomain.form()
    values = value_morphism.domain()
    match _is_bilinear_form(source_form), _is_quadratic_form(source_form):
        case True, _ if not _is_bilinear_form(target_form):
            raise TypeError(
                f"{domain} has a bilinear form, so a morphism out of it must land in a "
                f"module with a bilinear form, but {codomain} has form {target_form}"
            )
        case _, True if not _is_quadratic_form(target_form):
            raise TypeError(
                f"{domain} has a quadratic form, so a morphism out of it must land in a "
                f"module with a quadratic form, but {codomain} has form {target_form}"
            )
        case True, _ if (
            source_form.codomain() in OwnedRings()
            and value_morphism is values.module_category().Mor(values, values).identity()
            and domain.module_category().Mor(domain, codomain) in MatrixSpaces(domain.base_ring())
        ):
            return codomain.gram_tensor().pullback(module_morphism).is_equal_tensor(
                domain.gram_tensor()
            )
        case True, _:
            source_generators = tuple(domain.module_generators())
            return all(
                _mapped_value(domain, codomain, value_morphism, domain.b(left, right))
                == codomain.b(module_morphism(left), module_morphism(right))
                for left in source_generators
                for right in source_generators
            )
        case _, True:
            source_generators = tuple(domain.module_generators())
            probes = source_generators + tuple(
                left + right
                for index, left in enumerate(source_generators)
                for right in source_generators[index + 1 :]
            )
            return all(
                _mapped_value(domain, codomain, value_morphism, domain.norm(element))
                == codomain.norm(module_morphism(element))
                for element in probes
            )
    raise TypeError(
        f"a morphism of formed modules requires a bilinear or quadratic form on its domain, "
        f"but {domain} has form {source_form}"
    )


class FormedModuleMorphism:
    r"""A morphism of formed modules in one coefficient-ring fiber.

    The datum is a pair ``(f,h)`` with a module map on the underlying modules
    and a module map on the value objects that preserves the forms,
    ``h(b(x,y)) = b'(f(x),f(y))``.  Construction states this equation and does
    not compute it (``OWN-22``); :meth:`preserves_forms` computes it when asked.
    The form is preserved exactly, and the morphism is an isometry onto its
    image, exactly when ``h`` is the identity; :meth:`preserves_form_exactly`
    asks that.
    """

    def __init__(self, parent, module_morphism, value_morphism) -> None:
        domain = parent.domain()
        codomain = parent.codomain()
        if module_morphism.domain() is not domain:
            raise ValueError(
                f"a morphism of formed modules {domain} -> {codomain} needs a module map "
                f"with domain {domain}, but {module_morphism} has domain {module_morphism.domain()}"
            )
        if module_morphism.codomain() is not codomain:
            raise ValueError(
                f"a morphism of formed modules {domain} -> {codomain} needs a module map "
                f"with codomain {codomain}, but {module_morphism} has codomain {module_morphism.codomain()}"
            )
        source_values = _represented_value_module(domain)
        target_values = _represented_value_module(codomain)
        if value_morphism.domain() is not source_values:
            raise ValueError(
                f"the value map {value_morphism} must start at the value module {source_values} of "
                f"{self.domain()}, but starts at {value_morphism.domain()}"
            )
        if value_morphism.codomain() is not target_values:
            raise ValueError(
                f"the value map {value_morphism} must end at the value module {target_values} of "
                f"{self.codomain()}, but ends at {value_morphism.codomain()}"
            )
        self._value_morphism = value_morphism
        super().__init__(parent, module_morphism)

    def value_morphism(self):
        return self._value_morphism

    def preserves_form_exactly(self) -> bool:
        r"""Return whether the value-object map is the identity."""
        value_morphism = self.value_morphism()
        values = value_morphism.domain()
        if value_morphism.codomain() is not values:
            return False
        # A Mor object has one identity, so this is object identity. Comparing
        # morphisms extensionally would require extra finite-presentation data.
        return value_morphism is values.module_category().Mor(values, values).identity()

    def map_value(self, value):
        return _mapped_value(self.domain(), self.codomain(), self.value_morphism(), value)

    def preserves_forms(self) -> bool:
        r"""Return whether ``h(b(x,y)) = b'(f(x),f(y))`` on the module generators.

        The caller's diagnostic of ``OWN-22``: construction does not compute
        it, and its answer is an untrusted computation.
        """
        return _form_square_commutes(
            self.domain(), self.codomain(), self, self.value_morphism()
        )

    @validator
    def validate_form_preservation(self) -> None:
        r"""Raise ``ValueError`` unless ``h(b(x,y)) = b'(f(x),f(y))`` (``OWN-22``)."""
        if not self.preserves_forms():
            raise ValueError(
                f"({self}, {self.value_morphism()}) is not a morphism of formed modules "
                f"{self.domain()} -> {self.codomain()}: the value map applied to the source form "
                f"is not the target form pulled back along the module map"
            )

    def __eq__(self, other) -> bool:
        r"""A formed morphism is the pair ``(f,h)``; both components decide."""
        if not isinstance(other, FormedModuleMorphism):
            return False
        if self is other:
            return True
        if self.parent() is not other.parent():
            return False
        module_equal = ModuleMorphismMethods._richcmp_(self, other, op_EQ)
        return module_equal and self.value_morphism() == other.value_morphism()

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None

    def __mul__(self, other):
        if not isinstance(other, FormedModuleMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            raise ValueError(
                f"cannot compose {self} after {other}: the codomain {other.codomain()} of {other} "
                f"is not the domain {self.domain()} of {self}"
            )
        source = other.domain()
        target = self.codomain()
        modules = source.module_category()
        module_composite = modules.Mor(source, target)(
            modules.Mor(self.domain(), target)(self)
            * modules.Mor(source, self.domain())(other)
        )
        return FormModules(source.base_ring()).Mor(source, target)(
            (
                module_composite,
                self.value_morphism() * other.value_morphism(),
            )
        )


class FormEmbedding:
    r"""A form-preserving morphism whose module map is a monomorphism."""

    def __init__(
        self,
        parent,
        module_morphism,
        value_morphism,
        *,
        quadratic: bool | None = None,
    ) -> None:
        super().__init__(parent, module_morphism, value_morphism)
        if quadratic is None:
            domain = parent.domain()
            quadratic = domain in QuadraticFormModules(domain.base_ring())
        self._quadratic = bool(quadratic)

    def is_quadratic(self) -> bool:
        return self._quadratic

    @validator
    def validate_injectivity(self) -> None:
        r"""Raise ``ValueError`` unless the module map is known to be injective (``OWN-22``)."""
        domain = self.domain()
        codomain = self.codomain()
        injective = domain.module_category().Mor(domain, codomain)(self).is_injective()
        if injective is not True:
            raise ValueError(
                f"{self} is not a form-preserving embedding {domain} -> {codomain}: "
                f"its module map is not known to be injective (is_injective returned {injective})"
            )

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
            raise TypeError(
                f"the orthogonal complement of {self} is computed only for a finitely generated free "
                f"formed domain, but {source} is in {source.category()}"
            )
        if target not in FreeFormModules(target.base_ring()).FinitelyGenerated():
            raise TypeError(
                f"the orthogonal complement of {self} is computed only in a finitely generated free "
                f"formed module, but {target} is in {target.category()}"
            )
        if source.value_module() is not source.base_ring():
            raise TypeError(
                f"the orthogonal complement of {self} is computed only for forms valued in the base ring "
                f"{source.base_ring()}, but the form on {source} takes values in {source.value_module()}"
            )
        if target.value_module() is not target.base_ring():
            raise TypeError(
                f"the orthogonal complement of {self} is computed only for forms valued in the base ring "
                f"{target.base_ring()}, but the form on {target} takes values in {target.value_module()}"
            )
        if source.base_ring() is not target.base_ring():
            raise TypeError(
                f"the orthogonal complement of {self} needs source and target over one base ring, "
                f"but {source} is over {source.base_ring()} and {target} is over {target.base_ring()}"
            )

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


class FormEmbeddingMor(CategoricalMor):
    r"""The form-preserving monomorphisms between two formed modules."""

    ElementMethods = FormEmbedding

    def __init__(self, mor_family, domain, codomain) -> None:
        ring = domain.base_ring()
        formed = FormModules(ring)
        if codomain.base_ring() is not ring or domain not in formed or codomain not in formed:
            raise TypeError(
                f"form-preserving embeddings {domain} -> {codomain} need two modules with forms over one "
                f"base ring {ring}, but they lie in {domain.category()} and {codomain.category()}"
            )
        CategoricalMor.__init__(self, mor_family, domain, codomain)

    def _element_constructor_(self, images, *, quadratic: bool | None = None, check=False):
        domain = self.domain()
        codomain = self.codomain()
        if isinstance(images, FormEmbedding):
            if images.domain() is not domain or images.codomain() is not codomain:
                raise ValueError(
                    f"{images} is an embedding {images.domain()} -> {images.codomain()}, "
                    f"not an element of {self}"
                )
            if images.parent() is self:
                return images
            images = domain.module_category().Mor(domain, codomain)(images)

        if quadratic is None:
            ring = domain.base_ring()
            quadratic = domain in QuadraticFormModules(ring)
        values = _represented_value_module(domain)
        if _represented_value_module(codomain) is not values:
            raise TypeError(
                f"a form-preserving embedding {domain} -> {codomain} needs both forms valued in one module, "
                f"but they take values in {values} and {_represented_value_module(codomain)}"
            )
        module_morphism = domain.module_category().Mor(domain, codomain)(images)
        embedding = self.element_class(
            self,
            module_morphism,
            values.module_category().Mor(values, values).identity(),
            quadratic=quadratic,
        )
        embedding.validate_form_preservation(check=check)
        embedding.validate_injectivity(check=check)
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
        return [packet.Mors().Of(source, target), *inherited]

    def _repr_(self):
        return f"Emb_Form({self.domain()}, {self.codomain()})"


class FormedModuleMor(CategoricalMor):
    ElementMethods = FormedModuleMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        if domain.base_ring() != codomain.base_ring():
            raise ValueError(
                f"morphisms of formed modules {domain} -> {codomain} need one base ring, but {domain} is "
                f"over {domain.base_ring()} and {codomain} is over {codomain.base_ring()}"
            )
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, datum, *, check=False):

        explicit_pair = (
            isinstance(datum, tuple)
            and len(datum) == 2
            and all(isinstance(part, Morphism) for part in datum)
        )
        if (
            not explicit_pair
            and not isinstance(datum, FormedModuleMorphism)
            and not isinstance(datum, ModuleMorphismMethods)
        ):
            domain = self.domain()
            codomain = self.codomain()
            datum = domain.module_category().Mor(domain, codomain)(datum)

        if isinstance(datum, FormedModuleMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError(
                    f"{datum} is a morphism {datum.domain()} -> {datum.codomain()}, not an element of {self}"
                )
            if datum.parent() is self:
                return datum
            module_mor = self.domain().module_category().Mor(self.domain(), self.codomain())
            datum = (module_mor(datum), datum.value_morphism())
        elif isinstance(datum, ModuleMorphismMethods):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError(
                    f"the module map {datum} is {datum.domain()} -> {datum.codomain()}, so it does not give "
                    f"an element of {self}"
                )
            source_values = _represented_value_module(self.domain())
            target_values = _represented_value_module(self.codomain())
            if source_values is not target_values:
                raise TypeError(
                    f"the module map {datum} alone does not determine a morphism of formed modules in {self}: "
                    f"the forms take values in different modules {source_values} and {target_values}, "
                    "so a value map must also be given"
                )
            datum = (datum, source_values.module_category().Mor(source_values, target_values).identity())
        module_morphism, value_morphism = datum
        morphism = self.element_class(self, module_morphism, value_morphism)
        morphism.validate_form_preservation(check=check)
        return morphism

    def preserves_forms(self, module_morphism) -> bool:
        r"""Whether the module map ``f: M -> N`` preserves the forms: ``b_N(f(x), f(y)) = b_M(x, y)``.

        These are the module maps that underlie the elements of this Mor
        object whose value map is the identity, so the answer says whether
        ``self(f)`` exists.  Both forms take values in one module.
        """
        domain = self.domain()
        codomain = self.codomain()
        assert module_morphism.domain() is domain and module_morphism.codomain() is codomain, (
            f"{self} preserves forms along module maps {domain} -> {codomain}, but {module_morphism} is "
            f"{module_morphism.domain()} -> {module_morphism.codomain()}"
        )
        values = _represented_value_module(domain)
        assert _represented_value_module(codomain) is values, (
            f"the forms of {domain} and {codomain} take values in {values} and "
            f"{_represented_value_module(codomain)}, so a module map alone does not compare them"
        )
        return _form_square_commutes(
            domain,
            codomain,
            module_morphism,
            values.module_category().Mor(values, values).identity(),
        )

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

class FormedModuleMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self):
        return FormedModuleMor


class FormedModuleMonoCategoryConstruction(MonoCategoryConstruction):
    r"""The form-preserving monomorphisms of formed modules."""

    def fixed_category_class(self):
        return FormEmbeddingMor


class FiberedFormedModuleMorphism:
    r"""A formed-module morphism over a coefficient-ring map ``g:S1 -> S2``.

    The actual linear data live in the target fiber, exactly as required by
    the Grothendieck/fibered-category formulation:

    ``module_morphism : S2 tensor_S1 L1 -> L2`` and
    ``value_morphism  : S2 tensor_S1 W1 -> W2``.

    The represented scalar-extension computation currently materializes this for the
    scalar-valued finite-free formed objects supported by ``FormModules(R)``'s
    ``base_change`` method.  Unsupported scalar extensions fail at object
    construction rather than being represented by a semilinear fiction.
    """

    def __init__(self, parent, module_morphism, value_morphism) -> None:
        domain = parent.domain()
        codomain = parent.codomain()
        changed = parent.base_changed_domain()
        if module_morphism.domain() is not changed:
            raise ValueError(
                f"a morphism of formed modules over {parent.ring_map()} needs a module map out of the "
                f"scalar extension {changed} of {domain}, but {module_morphism} starts at "
                f"{module_morphism.domain()}"
            )
        if module_morphism.codomain() is not codomain:
            raise ValueError(
                f"a morphism of formed modules into {codomain} needs a module map with that "
                f"codomain, but {module_morphism} ends at {module_morphism.codomain()}"
            )
        source_values = _represented_value_module(changed)
        target_values = _represented_value_module(codomain)
        if value_morphism.domain() is not source_values:
            raise ValueError(
                f"the value map {value_morphism} must start at the value module {source_values} of the "
                f"scalar extension {changed}, but starts at {value_morphism.domain()}"
            )
        if value_morphism.codomain() is not target_values:
            raise ValueError(
                f"the value map {value_morphism} must end at the value module {target_values} of "
                f"{codomain}, but ends at {value_morphism.codomain()}"
            )
        self._value_morphism = value_morphism
        module_mor = parent.module_mor()
        compatible = module_mor.base_change_adjunction(
            parent.ring_map()
        ).mor_set_isomorphism_forward(
            module_morphism,
            domain,
        )
        super().__init__(parent, parent.ring_map(), compatible)

    def ring_map(self):
        return self.parent().ring_map()

    def base_changed_domain(self):
        return self.parent().base_changed_domain()

    def value_morphism(self):
        return self._value_morphism

    def map_value(self, value):
        changed = self.base_changed_domain()
        source_element = _value_as_module_element(changed, value)
        return _value_from_module_element(
            self.codomain(), self.value_morphism()(source_element)
        )

    def preserves_forms(self) -> bool:
        r"""Return whether ``h(b(x,y)) = b'(f(x),f(y))`` on generators of the scalar extension.

        The caller's diagnostic of ``OWN-22``: construction does not compute
        it, and its answer is an untrusted computation.
        """
        return _form_square_commutes(
            self.base_changed_domain(),
            self.codomain(),
            self.linearization(),
            self.value_morphism(),
        )

    @validator
    def validate_form_preservation(self) -> None:
        r"""Raise ``ValueError`` unless ``h(b(x,y)) = b'(f(x),f(y))`` on the scalar extension (``OWN-22``)."""
        if not self.preserves_forms():
            raise ValueError(
                f"({self.linearization()}, {self.value_morphism()}) is not a morphism of formed modules "
                f"{self.base_changed_domain()} -> {self.codomain()} over {self.ring_map()}: the value map "
                f"applied to the source form is not the target form pulled back along the module map"
            )

    def __mul__(self, other):
        if not isinstance(other, FiberedFormedModuleMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            raise ValueError(
                f"cannot compose {self} after {other}: the codomain {other.codomain()} of {other} "
                f"is not the domain {self.domain()} of {self}"
            )
        composite_ring_map = self.ring_map() * other.ring_map()
        mor = other.domain().fibered_formed_mor(
            self.codomain(), composite_ring_map
        )

        direct_changed = mor.base_changed_domain()
        middle_changed = self.base_changed_domain()
        module_semilinear = (
            self.parent().module_mor()(self)
            * other.parent().module_mor()(other)
        )
        module_map = module_semilinear.linearization()
        if module_map.domain() is not direct_changed:
            raise ValueError(
                f"composing {self} after {other}: the linearized module map starts at "
                f"{module_map.domain()}, not at the scalar extension {direct_changed} of {other.domain()} "
                f"along {composite_ring_map}"
            )

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
        return mor((module_map, value_map))


class FiberedFormedModuleMor(CategoricalMor):
    ElementMethods = FiberedFormedModuleMorphism

    def __init__(self, domain, codomain, ring_map) -> None:

        target_ring = _base_change_codomain(domain, ring_map)
        if target_ring != codomain.base_ring():
            raise ValueError(
                f"the ring map {ring_map} sends {domain.base_ring()} to {target_ring}, "
                f"not to the base ring {codomain.base_ring()} of {codomain}"
            )
        from dzack_research.preamble.categories.modules.fibered_modules import (
            ModulesOverCommutativeRings,
        )

        self._ring_map = ring_map
        self._module_mor = ModulesOverCommutativeRings().Mor(domain, codomain)
        self._base_changed_domain = self._module_mor.extended_domain(ring_map)
        # The endpoints sit over different base rings; the Mor is filed under
        # the Mor category of the source fibre.
        CategoricalMor.__init__(
            self,
            FormModules(domain.base_ring()).MorCategory(),
            domain,
            codomain,
        )

    def ring_map(self):
        return self._ring_map

    def base_changed_domain(self):
        return self._base_changed_domain

    def module_mor(self):
        r"""Return the underlying Mor in the varying-ring module category."""
        return self._module_mor

    def super_categories(self):
        r"""The lower arrow theory is the varying-ring semilinear module Mor."""
        return [self.module_mor()]

    def _element_constructor_(self, datum, *, check=False):
        module_morphism, value_morphism = datum
        morphism = self.element_class(self, module_morphism, value_morphism)
        morphism.validate_form_preservation(check=check)
        return morphism

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"{self} has no identity: its domain {self.domain()} differs from its codomain {self.codomain()}"
            )
        if not self.ring_map().is_identity():
            raise ValueError(
                f"{self} has no identity: it lies over the ring map {self.ring_map()}, "
                "which is not the identity"
            )

        changed = self.base_changed_domain()
        module_map = self.module_mor().identity().linearization()
        if module_map.domain() is not changed:
            raise ValueError(
                f"the identity of {self} linearizes to a module map starting at {module_map.domain()}, "
                f"not at the scalar extension {changed} of {self.domain()} along {self.ring_map()}"
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


class PairingObjects(OwnedCategoryOverBaseRing):
    r"""Module objects carrying one represented pairing ``X tensor_R Y -> W``."""

    @classmethod
    def _repr_object_names(cls):
        return "pairing-bearing module objects"

    def super_categories(self):
        r"""Paired modules are slice objects and formed modules are modules; both are sets."""
        return [OwnedSets()]

    def an_object(self):
        return PairedModules(self.base_ring()).an_object()

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def pairing(self, left, right):
            r"""Evaluate this object's selected pairing on ``(left,right)``."""
            return self._pairing_value(left, right)

        def left_module(self):
            r"""Return the left module of the selected pairing."""
            return self._pairing_left_module()

        def right_module(self):
            r"""Return the right module of the selected pairing."""
            return self._pairing_right_module()

        def value_module(self):
            r"""Return the value module of the selected pairing."""
            return self._pairing_value_module()

        def is_base_ring_valued(self) -> bool:
            r"""Return whether this finite framed pairing takes values in its base ring."""
            match self.left_module() is self.right_module() and self.left_module() is self:
                case True:
                    pass
                case False:
                    raise TypeError(
                        f"base-ring-valuedness here is defined for a formed module pairing itself, but {self} pairs {self.left_module()} and {self.right_module()}"
                    )
            match self.module_rank().is_finite():
                case True:
                    ring = self.base_ring()
                    generators = tuple(self.module_generators())
                    return all(
                        self.b(left, right) in ring
                        for left in generators
                        for right in generators
                    )
                case False:
                    raise ValueError(
                        f"cannot decide whether the form on {self} is base-ring-valued from a finite framing: the module has infinite rank"
                    )

        @cached_method
        def left_curry(self):
            r"""Return ``X -> Hom_R(Y,W)``, ``x |-> (y |-> b(x,y))``."""
            left = self.left_module()
            right = self.right_module()
            values = _represented_value_module(self)
            internal_mor = right.module_category().Mor(right, values)
            return left.module_category().Mor(
                left, internal_mor
            )._from_constructed_element_map(
                lambda left_element: internal_mor._from_constructed_element_map(
                    lambda right_element: _value_as_module_element(
                        self,
                        self.pairing(left_element, right_element),
                    )
                )
            )

        @cached_method
        def right_curry(self):
            r"""Return ``Y -> Hom_R(X,W)``, ``y |-> (x |-> b(x,y))``."""
            left = self.left_module()
            right = self.right_module()
            values = _represented_value_module(self)
            internal_mor = left.module_category().Mor(left, values)
            return right.module_category().Mor(
                right, internal_mor
            )._from_constructed_element_map(
                lambda right_element: internal_mor._from_constructed_element_map(
                    lambda left_element: _value_as_module_element(
                        self,
                        self.pairing(left_element, right_element),
                    )
                )
            )

        @cached_method
        def left_radical(self):
            r"""Return ``ker(X -> Hom_R(Y,W))`` for the selected pairing."""
            return self.left_curry().kernel()

        @cached_method
        def right_radical(self):
            r"""Return ``ker(Y -> Hom_R(X,W))`` for the selected pairing."""
            return self.right_curry().kernel()


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
        return [
            Modules(self.base_ring()).SliceOver(self.base()),
            PairingObjects(self.base_ring()),
        ]

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
        assert pairing.parent().mor_category().is_subcategory(Modules(ring)), (
            f"a pairing in {self} is a morphism of {Modules(ring)}; {pairing} is not one: "
            f"it lies in {pairing.parent()}"
        )
        assert pairing.domain() in TensorProductModules(ring), (
            f"a pairing in {self} is a morphism out of a tensor product of {ring}-modules, "
            f"but {pairing} has domain {pairing.domain()} in {pairing.domain().category()}"
        )
        return _object_of(self, arrow=pairing)

    class ParentMethods:
        def _pairing_value(self, left, right):
            return self.arrow()(self.arrow().domain().pure_tensor(left, right))

        def _pairing_left_module(self):
            return self.arrow().domain().tensor_factor(0)

        def _pairing_right_module(self):
            return self.arrow().domain().tensor_factor(1)

        def _pairing_value_module(self):
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
        if _has_finite_framing(form.module()):
            changed_values = form.coordinate_values().map(
                lambda value: _base_change_scalar(ring_map, value),
                name="Base-changed bilinear coordinate values",
            )
            return FormModules(target_ring)(
                changed.bilinear_forms(target_ring)(changed_values)
            )

        def changed_bilinear_value(left, right):
            left_coordinates = changed(left).to_vector()
            right_coordinates = changed(right).to_vector()
            result = target_ring.zero()
            for left_label in left_coordinates.support().domain():
                source_left = source.module_generator(left_label)
                for right_label in right_coordinates.support().domain():
                    source_right = source.module_generator(right_label)
                    result += (
                        left_coordinates(left_label)
                        * right_coordinates(right_label)
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
        raise TypeError(
            f"base change along {ring_map} is defined for bilinear and quadratic forms, "
            f"but the form {form} on {self} is neither"
        )

    source_form = self.form()
    if source_form.has_selected_bilinear_lift():
        changed_lift_values = source_form.lift_coordinate_values().map(
            lambda value: _base_change_scalar(ring_map, value),
            name="Base-changed quadratic-lift coordinate values",
        )
        return FormModules(target_ring)(
            changed.quadratic_forms(target_ring)(changed_lift_values)
        )

    def changed_quadratic_value(element):
        coordinates = changed(element).to_vector()
        result = target_ring.zero()
        for left_label in coordinates.support().domain():
            source_left = source.module_generator(left_label)
            result += (
                coordinates(left_label)**2
                * _base_change_scalar(ring_map, form(source_left))
            )
            left_rank = source_labels.ranking_map()(left_label)
            for right_label in coordinates.support().domain():
                if source_labels.ranking_map()(right_label) <= left_rank:
                    continue
                source_right = source.module_generator(right_label)
                result += (
                    coordinates(left_label)
                    * coordinates(right_label)
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
        return [
            Modules(self.base_ring()),
            PairingObjects(self.base_ring()),
        ]

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
    ):
        r"""Equip the module classified by ``form`` with that selected form."""
        module = form.module()
        if module.base_ring() is not self.base_ring():
            raise ValueError(
                f"{self} is over {self.base_ring()}, but the form {form} is on {module}, "
                f"which is over {module.base_ring()}"
            )
        return _form_module(
            form,
            _extra_categories=_extra_categories,
            _extra_construction_data=_extra_construction_data,
            _subobject_ambient=_subobject_ambient,
            _subobject_generator_images=_subobject_generator_images,
            _subobject_lift=_subobject_lift,
            _subobject_inclusion_factory=_subobject_inclusion_factory,
        )

    _MorCategory = FormedModuleMorCategoryConstruction
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
            r"""The selected form read on this module.

            This module is built on the framing of the unformed module, so a
            bilinear form with values in a ring on a finite framing reads here
            with the same Gram tensor.  Otherwise its arguments coerce to the
            unformed module.
            """
            form = self.form()
            module = self.unformed_module()
            if form.module() is self:
                return form
            if (
                _is_bilinear_form(form)
                and form.codomain() in OwnedRings()
                and _has_finite_framing(module)
            ):
                return self.bilinear_forms(self.value_module())(form.gram_tensor())
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
            coordinates = self._framing_lift(self(element))
            return self.unformed_module().linear_combination(
                {label: coordinates(label) for label in coordinates.support().domain()}
            )

        def _element_from_unformed_module(self, element):
            r"""The element of this module with the coefficients ``element`` has in :meth:`unformed_module`."""
            coordinates = self.unformed_module().framing_morphism().lift(element)
            return self.linear_combination(
                {label: coordinates(label) for label in coordinates.support().domain()}
            )

        def _pairing_value(self, left, right):
            return self.b(left, right)

        def _pairing_left_module(self):
            return self

        def _pairing_right_module(self):
            return self

        def _pairing_value_module(self):
            return self.form().codomain()

        def is_nondegenerate(self) -> bool:
            r"""Return whether both radicals of this form are zero."""
            match self in FormModules(self.base_ring()).Nondegenerate():
                case True:
                    return True
                case False:
                    return self.left_curry().is_injective() and self.right_curry().is_injective()

        def Mor(self, codomain, category=None):
            if category is None and codomain in FormModules(self.base_ring()):
                return FormModules(self.base_ring()).Mor(self, codomain)
            return _category_mor_parent(category, self, codomain)

        def Mono(self, codomain):
            r"""Return the form-preserving monomorphisms into ``codomain``."""
            return FormModules(self.base_ring()).Mono(self, codomain)

        def formed_mor(self, module_morphism, value_morphism):
            r"""Construct the general fixed-fiber formed morphism ``(f,h)``."""
            return self.Mor(module_morphism.codomain())(
                (module_morphism, value_morphism)
            )

        def fibered_formed_mor(self, codomain, ring_map):
            r"""Return formed morphisms from this module to ``codomain`` over ``ring_map``."""
            return FiberedFormedModuleMor(self, codomain, ring_map)

        def _Hom_(self, codomain, category=None):
            ring = self.base_ring()
            formed = FormModules(ring)
            if codomain in formed and (category is None or category.is_subcategory(formed)):
                return FormModules(ring).Mor(self, codomain)

            return self.module_category().Mor(self, codomain)

        def b(self, left, right):
            r"""Evaluate the (polar) bilinear form on two elements of this module.

            On a finite framing with values in a ring, ``b(x, y)`` is one
            contraction ``G(x, y) = sum_{i,j} G_{ij} x^i y^j`` of the Gram
            tensor with the coordinate vectors of ``x`` and ``y`` (`OWN-24`).
            """
            if left not in self or right not in self:
                raise TypeError(
                    f"the form on {self} pairs two of its elements, but {left} or {right} is not in {self}"
                )
            form = self.form()
            match _is_quadratic_form(form):
                case False if form.codomain() in OwnedRings() and _has_finite_framing(self):
                    # This module is constructed on the framing of the form's
                    # module, so its coordinates are the Gram tensor's indices.
                    framing = self.framing_morphism()
                    values = form.codomain()
                    return form.gram_tensor().contract(
                        tensor.vector(values, tuple(framing.lift(left))),
                        tensor.vector(values, tuple(framing.lift(right))),
                    )
                case is_quadratic:
                    module = form.module()
                    if module is not self:
                        left, right = module(left), module(right)
                    return form.b(left, right) if is_quadratic else form(left, right)

        def norm(self, element):
            r"""Return ``q(x)`` for a quadratic form, else ``b(x, x)``."""
            if element not in self:
                raise TypeError(
                    f"the norm on {self} is defined on its elements, but {element} is not in {self}"
                )
            form = self.form()
            if form.module() is not self:
                element = self.unformed_module()(element)
            if _is_quadratic_form(form):
                return form(element)
            return form(element, element)

        def q(self, element):
            r"""Return the selected quadratic/norm value of ``element``."""
            return self.norm(element)

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
            r"""This module with the form scaled by ``scalar``: Gram tensor ``m G`` when it has one."""
            form = self._formed_form()
            if _is_bilinear_form(form):
                if form.codomain() in OwnedRings() and _has_finite_framing(form.module()):
                    return FormModules(self.base_ring())(
                        self.bilinear_forms(self.value_module())(scalar * form.gram_tensor())
                    )
                if _has_finite_framing(form.module()):
                    values = form.coordinate_values().map(
                        lambda value: scalar * value,
                        name="Twisted bilinear coordinate values",
                    )
                    return FormModules(self.base_ring())(
                        self.bilinear_forms(self.value_module())(values)
                    )
                return FormModules(self.base_ring())(
                    self.bilinear_forms(self.value_module())(
                        lambda left, right: scalar * form(left, right)
                    )
                )
            source_form = self.form()
            if source_form.has_selected_bilinear_lift():
                values = source_form.lift_coordinate_values().map(
                    lambda value: scalar * value,
                    name="Twisted quadratic-lift coordinate values",
                )
                return FormModules(self.base_ring())(
                    self.quadratic_forms(self.value_module())(values)
                )
            return FormModules(self.base_ring())(
                self.quadratic_map(
                    self.value_module(),
                    lambda element: scalar * form(element),
                )
            )

        base_change = _formed_module_base_change
    class ElementMethods:
        @cached_method
        def b(self, other):
            r"""Return the polar bilinear value ``b(self, other)``."""
            return self.parent().b(self, other)

        @cached_method
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
            r"""Return this category with the axiom that both radicals of the form are zero."""
            return self._with_axiom("Nondegenerate")

        def Unimodular(self):
            r"""Return this category with the axiom that the correlation of the form is an isomorphism."""
            return self._with_axiom("Unimodular")

    class Nondegenerate(CategoryWithAxiom):
        r"""Form modules whose left and right radicals are zero."""

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

    _MorCategory = FormedModuleMorCategoryConstruction

    class ParentMethods:
        def algebraic_correlation_morphism(self):
            r"""Return ``b^flat : M -> Hom_R(M,R)`` for this scalar-valued bilinear form."""
            injective = self in FormModules(self.base_ring()).Nondegenerate()
            return _algebraic_correlation_morphism(self, injective=injective)

        @cached_method
        def scale_submodule(self):
            r"""Return the submodule or fractional ideal generated by all pairing values."""
            ring = self.base_ring()
            values = self.value_module()
            match values is ring, values is ring.fraction_field():
                case True, _:
                    assert self.module_rank().is_finite(), (
                        f"the scale ideal of {self} is computed from a finite Gram matrix, "
                        f"but {self} has rank {self.module_rank()}"
                    )
                    gram = self.gram_tensor()
                    rank = int(self.module_rank())
                    return ring.ideal(
                        *(gram[row, column] for row in range(rank) for column in range(rank))
                    )
                case False, True:
                    assert self.module_rank().is_finite(), (
                        f"the scale fractional ideal of {self} is computed from a finite Gram matrix, "
                        f"but {self} has rank {self.module_rank()}"
                    )
                    gram = self.gram_tensor()
                    rank = int(self.module_rank())
                    return ring.fractional_ideal(
                        *(gram[row, column] for row in range(rank) for column in range(rank))
                    )
                case False, False:
                    match values in Modules(ring):
                        case True:
                            return self.form().image()
                        case False:
                            raise TypeError(
                                f"the scale of {self} is a submodule of its value module, but {values} "
                                f"is not represented as a {ring}-module"
                            )

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
            def signature_pair(self):
                r"""Return the Sylvester inertia pair of a finite symmetric form."""
                assert self.module_rank().is_finite(), (
                    f"the signature of {self} is computed here only at finite rank, "
                    f"but it has rank {self.module_rank()}"
                )
                assert self.value_module() in OwnedRings(), (
                    f"the signature of {self} needs scalar values in an ordered ring, "
                    f"but its values lie in {self.value_module()}"
                )
                from dzack_research.preamble.categories._lattice import (
                    _signature_pair_of_gram,
                )

                return _signature_pair_of_gram(self.gram_tensor())

            def signature(self):
                r"""Return the Sylvester inertia pair of this symmetric form."""
                return self.signature_pair()

            def definiteness(self):
                r"""Return the sign type of this finite-rank symmetric form."""
                rank = int(self.module_rank())
                signature = self.signature_pair()
                positive = int(signature.first())
                negative = int(signature.second())
                zero = rank - positive - negative
                match (positive, negative, zero):
                    case (0, 0, _):
                        return "zero"
                    case (_, 0, 0):
                        return "positive_definite"
                    case (0, _, 0):
                        return "negative_definite"
                    case (_, 0, _):
                        return "positive_semidefinite"
                    case (0, _, _):
                        return "negative_semidefinite"
                    case _:
                        return "indefinite"

            def to_quadratic_module(self):
                r"""Return ``q(v)=b(v,v)/2`` when this symmetric form is even.

                Over rings where ``2`` is not a unit this is genuinely extra
                structure: the quotient must lie back in the coefficient ring.
                The represented construction is checked on a finite framing; the
                cross terms need no further divisibility test because symmetry
                contributes them with the factor ``2`` in ``b(v,v)``.
                """
                assert self.module_rank().is_finite(), (
                    f"the quadratic form q(v)=b(v,v)/2 of {self} is computed only for finite rank, "
                    f"but {self} has rank {self.module_rank()}"
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
                            f"{self} has no quadratic form q(v)=b(v,v)/2: the form is not even, "
                            f"since the value {value} is not divisible by 2 in {ring}"
                        )
                    return quotient

                def half_norm(element):
                    element = self(element)
                    return half(self.b(element, element))

                for generator in unformed.module_generators():
                    half_norm(generator)

                return unformed.equip_quadratic_form(ring, half_norm)

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
                _extra_categories=(),
            ):
                r"""Equip ``module`` with the bilinear form represented by ``gram``.

                The value object is explicit.  Descent is checked on both arguments:
                every chosen relation must pair to zero with every chosen generator.
                """
                if module not in Modules(self.base_ring()).FinitelyPresented().Torsion():
                    raise ValueError(
                        f"a torsion bilinear form in {self} is defined on a finitely presented torsion "
                        f"{self.base_ring()}-module, but {module} is in {module.category()}"
                    )

                rank = int(module.module_generating_set().cardinality())
                values = _coerced_gram(value_module, gram, rank)
                relations = _relation_images(module)
                if not _bilinear_descends(relations, values, value_module):
                    raise ValueError(
                        f"the Gram matrix {values} does not define a bilinear form on {module}: some relation "
                        f"of {module} does not pair to zero in {value_module} with every generator"
                    )
                formed = FormModules(module.base_ring())(
                    module.bilinear_forms(value_module)(values),
                    _extra_categories=(self, *tuple(_extra_categories)),
                    _subobject_ambient=_subobject_ambient,
                    _subobject_generator_images=_subobject_generator_images,
                    _subobject_lift=_subobject_lift,
                    _subobject_inclusion_factory=_subobject_inclusion_factory,
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
                    raise ValueError(
                        f"the cokernel form of {morphism} in {self} needs its codomain over {self.base_ring()}, "
                        f"but {cover} is over {cover.base_ring()}"
                    )
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

                def primary_decomposition(self, *args, **kwargs):
                    return self.primary_components(*args, **kwargs)


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
                        raise ValueError(f"{self} is not metabolic: it has no Lagrangian submodule")
                    return lagrangians[0]

                def restricted_form(self, subobject):
                    if subobject.inclusion().codomain() is not self:
                        raise ValueError(
                            f"the form of {self} restricts only to a submodule of {self}, but {subobject} "
                            f"is included into {subobject.inclusion().codomain()}"
                        )
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
                            f"the form on {self} is degenerate: some nonzero element pairs to zero with every "
                            f"generator, so it does not identify {self} with its Pontryagin dual"
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

    _MorCategory = FormedModuleMorCategoryConstruction

    class ParentMethods:
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
                f"the polar bilinear form b(x,y)=q(x+y)-q(x)-q(y) of {self} is computed here only for "
                f"forms valued in {self.base_ring()}, but q takes values in {self.value_module()}"
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
                _extra_categories=(),
            ):
                r"""Equip ``module`` with ``q(x)=x^T gram x`` valued in ``value_module``.

                For every relation ``r`` we check both ``q(r)=0`` and vanishing of the
                polar value ``q(x+r)-q(x)-q(r)`` against every generator.  These are
                exactly the conditions for the quadratic map to descend to the quotient.
                """
                if module not in Modules(self.base_ring()).FinitelyPresented().Torsion():
                    raise ValueError(
                        f"a torsion quadratic form in {self} is defined on a finitely presented torsion "
                        f"{self.base_ring()}-module, but {module} is in {module.category()}"
                    )

                rank = int(module.module_generating_set().cardinality())
                values = _coerced_gram(value_module, gram, rank)
                if any(values[i][j] != values[j][i] for i in range(rank) for j in range(rank)):
                    raise ValueError(
                        f"the Gram matrix {values} of a quadratic form on {module} must be symmetric, but it is not"
                    )
                relations = _relation_images(module)
                if not _quadratic_descends(relations, values, value_module):
                    raise ValueError(
                        f"the Gram matrix {values} does not define a quadratic form on {module}: for some "
                        f"relation r, q(r) or the polar value of r with a generator is nonzero in {value_module}"
                    )
                formed = FormModules(module.base_ring())(
                    module.quadratic_forms(value_module)(values),
                    _extra_categories=(self, *tuple(_extra_categories)),
                    _subobject_ambient=_subobject_ambient,
                    _subobject_generator_images=_subobject_generator_images,
                    _subobject_lift=_subobject_lift,
                    _subobject_inclusion_factory=_subobject_inclusion_factory,
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
                    raise ValueError(
                        f"the cokernel form of {morphism} in {self} needs its codomain over {self.base_ring()}, "
                        f"but {cover} is over {cover.base_ring()}"
                    )
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

                def primary_decomposition(self, *args, **kwargs):
                    return self.primary_components(*args, **kwargs)


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
                        raise ValueError(f"{self} is not metabolic: it has no Lagrangian submodule")
                    return lagrangians[0]

                def restricted_form(self, subobject):
                    if subobject.inclusion().codomain() is not self:
                        raise ValueError(
                            f"the form of {self} restricts only to a submodule of {self}, but {subobject} "
                            f"is included into {subobject.inclusion().codomain()}"
                        )
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
                    if (
                        value_module not in FractionFieldQuotients(self.base_ring())
                        or value_module.modulus() != 2
                    ):
                        raise TypeError(
                            f"the polarization of {self} is computed only for quadratic forms valued in QQ/2ZZ, "
                            f"but q takes values in {value_module}"
                        )

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

    @classmethod
    def _repr_object_names(cls):
        return "free form modules"

    def super_categories(self):

        return [FormModules(self.base_ring()), FramedFreeModules(self.base_ring())]

    class ParentMethods:
        base_change = _formed_module_base_change

        @cached_method
        def correlation_morphism(self):
            r"""Return the algebraic correlation ``M -> Hom_R(M,R)``."""
            injective = self in FormModules(self.base_ring()).Nondegenerate()
            return _algebraic_correlation_morphism(self, injective=injective)

        def is_unimodular(self) -> bool:
            r"""Return whether the algebraic correlation is an isomorphism."""
            injective = self in FormModules(self.base_ring()).Nondegenerate()
            correlation = _algebraic_correlation_morphism(
                self, injective=injective
            )
            return correlation.is_injective() and correlation.is_surjective()

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
                    raise ValueError(
                        f"a Gram matrix of {self} is taken on elements of {self}, but {basis} contains "
                        "an element of another module"
                    )
                size = len(selected)
                return self.value_module().matrix_space(size, size).from_rows(
                    tuple(tuple(self.b(left, right) for right in selected) for left in selected)
                )

            @cached_method
            def dual_module(self):

                return self.base_ring().free_module(self.module_generating_set())

            @cached_method
            def radical(self):
                r"""Return the left radical ``ker(M -> Hom_R(M,W))``."""
                return self.left_radical()

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
                    f"the determinant of the form on {self} needs values in a ring, "
                    f"but it takes values in {self.value_module()}, in {self.value_module().category()}"
                )
                return self.gram_matrix().determinant()

def _form_module(
    form,
    *,
    _extra_categories=(),
    _extra_construction_data=None,
    _subobject_ambient=None,
    _subobject_generator_images=None,
    _subobject_lift=None,
    _subobject_inclusion_factory=None,
):
    r"""Equip the exact represented module carrying ``form`` with that form.

    The module owner chooses the realization of the stronger object.  The
    formed layer supplies only its selected form and, for a subobject, the
    retained inclusion datum.  A distinct structured parent still represents
    each choice of form, but this owner does not rebuild the module's framing
    or presentation.
    """

    if not (_is_bilinear_form(form) or _is_quadratic_form(form)):
        raise TypeError(
            f"a module with a form is built from a bilinear or quadratic form, but {form} is neither"
        )
    module = form.module()
    base_ring = module.base_ring()
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
        has_finite_scalar_gram = form.codomain() in OwnedRings() and _has_finite_framing(module)
        if has_finite_scalar_gram and form.gram_tensor().is_symmetric():
            categories.append(BilinearFormModules(base_ring).Symmetric())
    else:
        categories.append(QuadraticFormModules(base_ring))
    categories.extend(tuple(_extra_categories))
    construction_data = dict(_extra_construction_data or {})
    construction_data["source_form"] = form
    match (_subobject_ambient, _subobject_inclusion_factory):
        case (None, None):
            pass
        case _:
            from dzack_research.preamble.categories.modules.pure.modules import ModuleSubobjects

            categories.append(ModuleSubobjects(base_ring))
            match _subobject_ambient:
                case None:
                    pass
                case ambient:
                    categories.append(Modules(base_ring).Subobjects(ambient))
            construction_data.update(
                subobject_ambient=_subobject_ambient,
                subobject_generator_images=_subobject_generator_images,
                subobject_lift=_subobject_lift,
                subobject_inclusion_factory=_subobject_inclusion_factory,
            )
    return module._module_with_structure(tuple(categories), construction_data)


@cached_function(key=lambda module, basis: (id(module), basis))
def _form_subobject_spanning(module, basis):
    r"""Return the canonical formed subobject on a finite span basis."""

    subobject = _module_subobject_spanning(module, basis)
    construction = subobject.module_subobject_construction()
    restricted = module._formed_form().pullback(subobject.inclusion())

    return FormModules(module.base_ring())(
        restricted,
        _subobject_ambient=construction.ambient_module(),
        _subobject_generator_images=construction.generator_images(),
        _subobject_lift=construction.selected_lift(),
        _subobject_inclusion_factory=construction.inclusion_factory(),
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
        or (isinstance(datum, Iterable) and not isinstance(datum, (str, bytes)))
    )
    form = (
        module.quadratic_forms(value_module)(datum)
        if coordinate_datum
        else module.quadratic_map(value_module, datum)
    )
    return FormModules(module.base_ring())(form)
