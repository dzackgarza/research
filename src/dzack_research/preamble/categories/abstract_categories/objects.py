"""Dependency-light bases for the owned mathematical category graph."""

from sage.categories.category import Category
from dzack_research.preamble.owned_category_bases import Category as OwnedCategoryBase
from sage.misc.abstract_method import abstract_method
from sage.structure.parent import Parent
from dzack_research.preamble.owned_category import OwnedParent
from sage.misc.constant_function import ConstantFunction
from sage.structure.category_object import CategoryObject
from sage.structure.parent import Parent


def membership_by_definition(category, candidate) -> bool:
    r"""Whether ``category``'s own definition puts ``candidate`` in it.

    ``False`` unless the category states, through ``additional_condition``,
    that it imposes no condition over its supercategories.  When it does, its
    objects are exactly the objects lying in every one of them, and that is
    the whole question.

    A free function because an owned category that replaces
    ``OwnedCategory.__contains__`` -- ``OwnedCategoryOverBaseRing`` does, and
    every category over a ring reaches membership through it -- has to reach
    the same statement.  One spelling, read wherever the question is asked.
    """
    if category.additional_condition() is not None:
        return False
    return all(
        candidate in super_category for super_category in category.super_categories()
    )


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
    def an_object(self):
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

    def additional_condition(self):
        r"""Return the condition this category imposes over its supercategories.

        ``self`` when it imposes one and ``None`` when it does not, which is
        the shape of Sage's ``Category.additional_structure`` and is read the
        same way.  ``None`` is a mathematical statement, not an omission: the
        category is the intersection of its supercategories, so its objects
        are exactly the objects lying in every one of them, and what it adds
        is operations and theorems rather than a further requirement.

        ``FreeFormModules(R)`` is the model case.  A free form module is
        exactly a module that is both a form module and framed free, and
        those two are its declared supercategories, so nothing further is
        being asked of an object and the two memberships decide it.
        ``VectorSpaces(K)`` is the degenerate case of the same statement: its
        one supercategory is ``Modules(K)`` and over a field there is no
        further condition at all.

        The default is ``self``, because a category normally does state
        something of its own -- a chosen datum, an axiom, a property -- and a
        category that has not said otherwise has not been examined.
        """
        return self

    def __contains__(self, candidate) -> bool:
        r"""Whether ``candidate`` is an object of this category.

        Placement decides it, which is Sage's rule and the one every category
        with a condition of its own needs: an object acquires a chosen datum
        or an axiom by being built or refined into the category that states
        it, and no examination of the object afterwards can recover a choice
        nobody made.

        A category that imposes no condition of its own is not decided that
        way.  Nothing has to be *placed* in the intersection of two categories
        to be in it, and requiring that is what left ``U`` outside
        ``FreeFormModules(R)`` while it was in both ``FormModules(R)`` and
        ``FramedFreeModules(R)``, and left a free module over a field outside
        ``VectorSpaces(K)``.  Such a category answers by its definition.
        """
        return super().__contains__(candidate) or membership_by_definition(self, candidate)


class OwnedParameterizedCategory(OwnedCategory):
    r"""An owned category parameterized by one object of a stated category.

    ``parameter_category`` is the statement.  ``Subgroups`` is parameterized
    by a group, ``GSets`` by a group, ``DifferentialGradedModules`` by a
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
    def parameter_category(self):
        r"""Return the category this family's parameter ranges over."""

    def __init__(self, parameter) -> None:
        declared = self.parameter_category
        if declared is not NotImplemented:
            ranges_over = declared()
            assert parameter in ranges_over, (
                f"{type(self).__name__} is parameterized by an object of "
                f"{ranges_over}, and {parameter} is not one"
            )
        self._owned_parameter = parameter
        super().__init__()

    def parameter(self):
        return self._owned_parameter

    def base(self):
        return self.parameter()


class Objects(OwnedCategory):
    r"""The root of the owned mathematical category graph.

    This category carries no mathematical supercategory. Sage's own
    ``Objects``/``Sets`` categories remain runtime substrate only and are not
    semantic ancestors of owned categories.
    """

    def an_object(self):
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

        def __call__(self, *arguments, **options):
            r"""Construct an element of this object, without coercion discovery.

            The values an owned object accepts are themselves owned, and Sage's
            coercion graph has never heard of them: asked for a conversion map
            it tries to build a Hom in its own ``Sets``, finds the domain absent
            and raises, before this object's own constructor is ever reached.
            The crossing into owned data happens in ``_element_constructor_``,
            which is the one boundary that admits foreign values.
            """
            return self._element_constructor_(*arguments, **options)

    def super_categories(self):
        return []

    @classmethod
    def _repr_object_names(cls):
        return "represented mathematical objects"


__all__ = [
    "Objects",
    "OwnedCategory",
    "OwnedParameterizedCategory",
]
