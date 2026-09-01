r"""Restriction of scalars along a specified ring morphism."""

from sage.categories.category import Category
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp

from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
    owned_ring_view,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import refine
from dzack_research.preamble.tensors import tensor


class RestrictedScalarsModules(OwnedCategoryOverBaseRing):
    r"""Modules obtained by reading an ``S``-module over ``R`` along ``R -> S``."""

    @classmethod
    def _repr_object_names(cls):
        return "restricted-scalars modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def ring_map(self):
            r"""Return the selected scalar map ``R -> S``."""
            return self._preamble_ring_map

        def module_over_extension(self):
            r"""Return the original ``S``-module before restriction of scalars."""
            return self._preamble_extension_module

        def extension_ring(self):
            return owned_ring_view(self.module_over_extension().base_ring())

        def scalar_multiple(self, scalar, element):
            if element.parent() is not self:
                element = self(element)
            extension_module = self.module_over_extension()
            return self.element_class(
                self,
                extension_module.scalar_multiple(
                    self.ring_map()(scalar),
                    element.underlying_element(),
                ),
            )

class RestrictedScalarsModuleView(Parent):
    r"""A distinct parent for the same additive group with a restricted scalar action."""

    class Element(ModuleElement):
        def __init__(self, parent, underlying_element) -> None:
            ModuleElement.__init__(self, parent)
            self._underlying_element = underlying_element

        def underlying_element(self):
            return self._underlying_element

        def _add_(self, other):
            return self.parent().element_class(
                self.parent(),
                self._underlying_element + other._underlying_element,
            )

        def _neg_(self):
            return self.parent().element_class(
                self.parent(), -self._underlying_element
            )

        def _lmul_(self, scalar):
            return self.parent().scalar_multiple(scalar, self)

        def _richcmp_(self, other, op):
            return richcmp(
                self._underlying_element,
                other._underlying_element,
                op,
            )

        def _repr_(self):
            return repr(self._underlying_element)

    def __init__(self, module, ring_map) -> None:
        self._preamble_extension_module = module
        self._preamble_ring_map = ring_map
        base_ring = owned_ring_view(ring_map.domain())
        extension_ring = owned_ring_view(module.base_ring())
        self._preamble_module_generating_set = None

        categories = [RestrictedScalarsModules(base_ring)]
        from dzack_research.preamble.categories.modules.framed.framed_modules import (
            FramedModules,
        )
        from dzack_research.preamble.categories.modules.pure.finitely_generated.finitely_generated_modules import (
            FinitelyGeneratedModules,
        )
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
            FinitelyGeneratedFreeModules,
        )
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            FinitelyPresentedModules,
        )

        if (
            module in FramedModules(extension_ring)
            and extension_ring in FramedModules(base_ring)
        ):
            scalar_labels = extension_ring.module_generating_set()
            module_labels = module.module_generating_set()
            if (
                scalar_labels.cardinality() in SageZZ
                and module_labels.cardinality() in SageZZ
            ):
                self._preamble_module_generating_set = finite_ordered_set(
                    (scalar_label, module_label)
                    for scalar_label in scalar_labels
                    for module_label in module_labels
                )
                categories.append(FramedModules(base_ring))
                if (
                    extension_ring in FinitelyGeneratedModules(base_ring)
                    and module in FinitelyGeneratedModules(extension_ring)
                ):
                    categories.append(FinitelyGeneratedModules(base_ring))
                if extension_ring in FinitelyGeneratedFreeModules(base_ring):
                    if module in FinitelyPresentedModules(extension_ring):
                        categories.append(FinitelyPresentedModules(base_ring))
                    if module in FinitelyGeneratedFreeModules(extension_ring):
                        self._preamble_module_generator_values = {
                            label: self.module_generator(label)
                            for label in self._preamble_module_generating_set
                        }
                        categories.append(FinitelyGeneratedFreeModules(base_ring))

        Parent.__init__(
            self,
            base=base_ring,
            category=Category.join(tuple(categories)),
        )
        refine(self, categories)

    def _element_constructor_(self, value):
        if isinstance(value, self.element_class) and value.parent() is self:
            return value
        if isinstance(value, RestrictedScalarsModuleView.Element):
            value = value.underlying_element()
        return self.wrap(self._preamble_extension_module(value))

    def wrap(self, underlying_element):
        r"""Read an element of the extension module in this restricted module."""
        extension_module = self._preamble_extension_module
        if getattr(underlying_element, "parent", lambda: None)() is not extension_module:
            underlying_element = extension_module(underlying_element)
        return self.element_class(self, underlying_element)

    def _coerce_map_from_(self, source):
        # Restriction of scalars is a change of structure, not a coercion of
        # mathematical objects.  Call ``wrap`` explicitly when the same
        # underlying additive-group element is to be read in this parent.
        if source is self._preamble_extension_module:
            return None
        return super()._coerce_map_from_(source)

    def __contains__(self, value) -> bool:
        if isinstance(value, self.element_class) and value.parent() is self:
            return True
        try:
            return value in self._preamble_extension_module
        except (TypeError, ValueError):
            return False

    def module_generating_set(self):
        if self._preamble_module_generating_set is None:
            raise NotImplementedError(
                "this scalar restriction has no selected finite framing"
            )
        return self._preamble_module_generating_set

    def module_generator(self, label):
        labels = self.module_generating_set()
        if label not in labels:
            raise ValueError(f"{label!r} is not a restricted-scalar module-generator label")
        scalar_label, module_label = label
        extension_ring = owned_ring_view(self._preamble_extension_module.base_ring())
        scalar = extension_ring.module_generator(scalar_label)
        module_generator = self._preamble_extension_module.module_generator(module_label)
        underlying = self._preamble_extension_module.scalar_multiple(
            scalar,
            module_generator,
        )
        return self.element_class(self, underlying)

    def module_generators(self):
        return finite_ordered_set(
            self.module_generator(label) for label in self.module_generating_set()
        )

    def framing_morphism(self):
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FreeModuleOn,
        )
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            framing_morphism,
        )

        source = FreeModuleOn(self.base_ring(), self.module_generating_set())
        return framing_morphism(source, self, self.module_generator)

    def presentation_matrix(self):
        r"""Return the induced finite presentation over the smaller ring.

        Suppose ``S`` is finite free over ``R`` on ``(s_i)`` and ``M`` is
        presented over ``S`` on ``(m_j)`` with relation rows ``(a_j)``.  The
        restricted module is generated over ``R`` by ``s_i m_j``.  For every
        selected relation and every ``s_i`` we expand ``s_i a_j`` in the
        selected ``R``-basis of ``S``.  These are exactly the restriction of
        the original ``S``-relation submodule to ``R``.
        """
        if self._preamble_module_generating_set is None:
            raise NotImplementedError(
                "this scalar restriction has no selected finite presentation"
            )
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            _presentation_matrix,
        )
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_coefficients,
        )

        extension_ring = self.extension_ring()
        extension_module = self.module_over_extension()
        scalar_labels = tuple(extension_ring.module_generating_set())
        module_labels = tuple(extension_module.module_generating_set())
        restricted_labels = tuple(self.module_generating_set())
        positions = {
            label: position for position, label in enumerate(restricted_labels)
        }
        engine = engine_ring(self.base_ring())
        relation_rows = []
        for relation in _presentation_matrix(extension_module).rows():
            for scalar_label in scalar_labels:
                scalar_generator = extension_ring.module_generator(scalar_label)
                row = [engine.zero()] * len(restricted_labels)
                for module_label, coefficient in zip(
                    module_labels, relation, strict=True
                ):
                    if not coefficient:
                        continue
                    product = extension_ring(
                        scalar_generator * extension_ring(coefficient)
                    )
                    for output_scalar_label, output_coefficient in module_coefficients(
                        product, extension_ring
                    ).items():
                        position = positions[(output_scalar_label, module_label)]
                        row[position] += engine(output_coefficient)
                if any(row):
                    relation_rows.append(row)
        return tensor.matrix(
            engine,
            len(relation_rows),
            len(restricted_labels),
            [entry for row in relation_rows for entry in row],
        )

    def zero(self):
        return self.element_class(self, self._preamble_extension_module.zero())

    def an_element(self):
        return self.element_class(self, self._preamble_extension_module.an_element())

    def _repr_(self):
        return (
            f"{self._preamble_extension_module} restricted to "
            f"{self.base_ring()} along {self._preamble_ring_map}"
        )


def restrict_scalars(module, ring_map):
    r"""Return ``Res_R^S(module)`` along the specified morphism ``R -> S``."""
    if engine_ring(ring_map.codomain()) is not engine_ring(module.base_ring()):
        raise ValueError(
            f"restriction of scalars for {module} requires a map into "
            f"{module.base_ring()}, got codomain {ring_map.codomain()}"
        )
    return RestrictedScalarsModuleView(module, ring_map)


def twist_scalar_action(module, ring_endomorphism):
    r"""Twist the scalar action of an ``R``-module along ``R -> R``.

    This is restriction of scalars along an endomorphism of the scalar ring;
    it is unrelated to ``L.twist(a)``, which rescales a lattice form while
    leaving its scalar action unchanged.
    """
    ring = engine_ring(module.base_ring())
    if (
        engine_ring(ring_endomorphism.domain()) is not ring
        or engine_ring(ring_endomorphism.codomain()) is not ring
    ):
        raise ValueError(
            "a scalar-action twist is specified by an endomorphism of the module's base ring"
        )
    return restrict_scalars(module, ring_endomorphism)


__all__ = [
    "RestrictedScalarsModuleView",
    "RestrictedScalarsModules",
    "restrict_scalars",
    "twist_scalar_action",
]
