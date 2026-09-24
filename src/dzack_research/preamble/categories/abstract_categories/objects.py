"""Dependency-light bases for the owned mathematical category graph."""

from typing import Any

from sage.categories.category import Category
from sage.categories.category_with_axiom import all_axioms
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.structure.parent import Parent

# The marker every owned category base carries, axiom categories included.
# Re-exported so the Mor packet can recognize one without reaching past this
# module into the bases it is built from.
from dzack_research.preamble.owned_category import (  # noqa: F401
    OwnedCategoryMixin,
    OwnedParent,
)
from dzack_research.preamble.owned_category_bases import (
    Category as OwnedCategoryBase,
    CategoryWithAxiom,
)


if "Framed" not in all_axioms:
    all_axioms.add("Framed")


class _SelectedFraming:
    r"""One category-relative chosen epimorphism from a selected free source."""

    def __init__(
        self,
        owner,
        target,
        source,
        generating_set,
        generator_morphism,
        framing_morphism_factory,
    ) -> None:
        if generator_morphism.domain() is not generating_set:
            raise ValueError("a framing generator morphism starts at its selected generating set")
        if generator_morphism.codomain() is not target:
            raise ValueError("a framing generator morphism lands in the framed object")
        self._owner = owner
        self._target = target
        self._source = source
        self._generating_set = generating_set
        self._generator_morphism = generator_morphism
        self._framing_morphism_factory = framing_morphism_factory
        self._framing_morphism = None

    def owner(self):
        return self._owner

    def source(self):
        return self._source

    def framing_generating_set(self):
        return self._generating_set

    def generator_morphism(self):
        return self._generator_morphism

    def framing_morphism(self):
        selected = self._framing_morphism
        if selected is None:
            selected = self._framing_morphism_factory()
            if selected.domain() is not self.source() or selected.codomain() is not self._target:
                raise ValueError("the selected framing epimorphism has the wrong endpoints")
            self._framing_morphism = selected
        return selected


def _fix_selected_framing(
    target,
    owner,
    source,
    generating_set,
    generator_morphism,
    framing_morphism_factory,
):
    r"""Fix one ``Framed`` datum for ``target`` in the stated ambient category."""
    selected_by_owner = target._selected_framing_registry()
    if owner in selected_by_owner:
        raise ValueError(f"{target} already has a selected framing in {owner}")
    selected = _SelectedFraming(
        owner,
        target,
        source,
        generating_set,
        generator_morphism,
        framing_morphism_factory,
    )
    selected_by_owner[owner] = selected
    return selected


class OwnedCategory(OwnedCategoryBase):
    r"""Base class for categories belonging to the owned mathematical graph.

    Over :class:`owned_category_bases.Category`, which ties this category's
    ``ParentMethods`` / ``ElementMethods`` / ``MorphismMethods`` into the
    named classes as real bases.  Sage's own builder passes
    ``prepend_cls_bases=False``, so only a copy of the container's
    ``__dict__`` reaches the MRO -- a copy carries no bases, so it cannot
    carry ``Parent``, so it cannot carry fields or a constructor.  That, and
    nothing else, is why a level would otherwise need a hand-written parent
    class beside its category.
    """

    @abstract_method
    def an_object(self) -> Parent:
        r"""Return one object of this category.

        A witness that the category is inhabited, and the datum every construction
        parameterized by a category needs: where ``C`` takes an object of ``D``,
        ``C(D.an_object())`` builds one without the caller knowing anything else
        about ``D``.

        Distinct from ``an_element``, which every parent carries and which produces
        an element *of that object*.  This produces an object *of this category*.

        Sage's ``Category.example`` is not this operation: it looks for a template
        module under ``sage.categories.examples`` and returns the ``NotImplemented``
        singleton when it finds none, so it answers for Sage's graph and is silent
        where it should be loud.

        A contract on every owned category, not a default: exhibiting an inhabitant
        is per-category mathematics, and a category that cannot is a gap in that
        category.
        """

class OwnedParameterizedCategory(OwnedCategory):
    r"""An owned category parameterized by one object of a stated category.

    ``parameter_category`` is the statement.  ``Subgroups`` is parameterized
    by a group, ``GObjects(G, Sets())`` by a group, ``DifferentialGradedModules`` by a
    differential graded algebra, ``GradedAlgebraModules`` by a graded algebra,
    ``PredicateSubgroups`` by a whole category.  Each of those is a different
    structure, and a family that does not say which one it wants can only
    report a wrong argument from wherever inside the first operation happened
    to need it -- ``this API expects a preamble group``, ``no attribute
    'grading_monoid'`` -- naming nothing about what was wanted.

    Stating it does two things.  A wrong parameter is refused at the boundary,
    against the category it should have been in, and a member of the family
    becomes constructible without knowing anything else about it: it is
    ``type(C)(C.parameter_category().an_object())``, which is what lets a
    survey of the owned graph reach a parameterized family at all instead of
    carrying a hand-written table of specimens.

    A family that has not stated it says so by name, through Sage's optional
    abstract-method protocol, and construction proceeds unchecked until it
    does.
    """

    @abstract_method(optional=True)
    def parameter_category(self) -> Category:
        r"""Return the category this family's parameter ranges over."""

    def __init__(self, parameter: Parent) -> None:
        # Stored before it is checked: a family over a base-relative category
        # (Cox rings over the toric schemes of the scheme's own base) states
        # its parameter category in terms of the parameter.
        self._owned_parameter = parameter
        declared = self.parameter_category
        if declared is not NotImplemented:
            ranges_over = declared()
            assert parameter in ranges_over, (
                f"{type(self).__name__} is parameterized by an object of "
                f"{ranges_over}, and {parameter} is not one"
            )
        super().__init__()

    def parameter(self) -> Parent:
        return self._owned_parameter

    def base(self) -> Parent:
        return self.parameter()


class Objects(OwnedCategory):
    r"""The root of the owned mathematical category graph.

    This category carries no mathematical supercategory. Sage's own
    ``Objects``/``Sets`` categories remain runtime substrate only and are not
    semantic ancestors of owned categories.
    """

    def an_object(self) -> Parent:
        r"""The set 2, which is an object like any other.

        The root has no structure to exhibit, so its witness is whatever the
        first level above it builds: two distinct elements, so that a map out
        of the witness is not forced.
        """
        from dzack_research.preamble.categories.sets.set_categories import Sets

        return Sets().an_object()

    class ParentMethods(OwnedParent, Parent):
        r"""The owned root of every object chain.

        Every owned object is an object, so the host runtime initialization
        belongs here and nowhere above.  A level declares its own datum and
        threads into this one with a cooperative ``super().__init__(**rest)``.
        """

        @cached_method
        def _selected_framing_registry(self):
            return {}

        def __call__(self, *arguments, **options):
            r"""Construct an element of this object, without coercion discovery.

            The values an owned object accepts are themselves owned, and Sage's
            coercion graph has never heard of them: asked for a conversion map
            it tries to build a Mor in its own ``Sets``, finds the domain absent
            and raises, before this object's own constructor is ever reached.
            The crossing into owned data happens in ``_element_constructor_``,
            which is the one boundary that admits foreign values.
            """
            return self._element_constructor_(*arguments, **options)

    class Framed(CategoryWithAxiom):
        r"""Objects carrying one chosen generating epimorphism from a free object.

        This is the single data contract for selected 1-framings.  A framing is
        relative to an ambient category: the same represented parent may carry
        its module framing and a different algebra framing.  Both are instances
        of this one contract, keyed by the category whose free functor supplies
        the source; neither specialization owns a second framing data model.
        """

        def an_object(self):
            r"""A rank-one free integer module with its canonical framing."""
            from sage.rings.integer_ring import ZZ as SageZZ

            from dzack_research.preamble.categories.rings.ring_foundation import (
                _own_ring,
            )

            return _own_ring(SageZZ).free_module(1)

        class ParentMethods:
            def selected_framing(self, owner):
                r"""Return the constructor-owned 1-framing in ``owner``."""
                selected = self._selected_framing_registry().get(owner)
                assert selected is not None, (
                    f"{self} was constructed without selected framing data in {owner}"
                )
                return selected

            def selected_framing_source(self, owner):
                r"""Return the exact selected free source in ``owner``."""
                return self.selected_framing(owner).source()

            def selected_framing_generating_set(self, owner):
                r"""Return the set indexing the selected free source in ``owner``."""
                return self.selected_framing(owner).framing_generating_set()

            def selected_framing_generator_morphism(self, owner):
                r"""Return the selected map from framing labels into this object."""
                return self.selected_framing(owner).generator_morphism()

            def selected_framing_generator(self, owner, label):
                r"""Return the image of one selected free generator."""
                labels = self.selected_framing_generating_set(owner)
                if label not in labels:
                    raise ValueError(f"{label!r} is not a framing-generator label")
                return self.selected_framing_generator_morphism(owner)(labels(label))

            @cached_method
            def selected_framing_generators(self, owner, *, name):
                r"""Return the selected generator family ``s |-> x_s``."""
                from dzack_research.preamble.categories.sets.indexed_families import (
                    indexed_family,
                )

                return indexed_family(
                    self.selected_framing_generating_set(owner),
                    lambda label: self.selected_framing_generator(owner, label),
                    name=name,
                )

            def selected_framing_generator_count(self, owner):
                return self.selected_framing_generating_set(owner).cardinality()

            def selected_framing_morphism(self, owner):
                r"""Return the selected generating epimorphism in ``owner``."""
                return self.selected_framing(owner).framing_morphism()

            def is_framed(self) -> bool:
                return True

    def super_categories(self):
        return []

    @classmethod
    def _repr_object_names(cls):
        return "represented mathematical objects"


__all__ = [
    "Objects",
    "OwnedCategory",
    "OwnedParameterizedCategory",
    "_fix_selected_framing",
]
