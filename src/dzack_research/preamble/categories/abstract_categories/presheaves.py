r"""Presheaves: the functor categories ``[C^op, D]``, and the Yoneda embedding.

The category of presheaves on ``C`` with values in ``D`` is

.. MATH::

    \mathrm{Presh}(C, D) := [C^{\mathrm{op}}, D],

the functor category the tree already owns, reached from ``C`` by
``C.presheaves(D)`` (``D = Sets()`` when omitted).  No new category class is
introduced: ``C.presheaves(D)`` is ``Cat().Mor(C.opposite(), D)``, so a
presheaf is an object of a functor category and its morphisms are natural
transformations.  The value category is a parameter because that is what the
later passage to sheaves of modules, of algebras, and to stacks changes.

The construction is a bifunctor ``Cat^op x Cat -> Cat``.  ``Cat`` is not an
object of itself here, so the bifunctor is stated on ``Cat`` by its two
actions: on objects, ``Cat().presheaves(C, D)``; on morphisms
``F: C' -> C`` and ``G: D -> D'``, ``Cat().presheaf_transport(F, G)`` is the
functor ``[C^op, D] -> [C'^op, D']``, ``P |-> G o P o F^op`` on objects and
``eta |-> G eta F^op`` on natural transformations.

The Yoneda embedding ``y: C -> Presh(C)`` sends ``X`` to the representable
presheaf ``Mor_C(-, X)`` and ``h: X -> Y`` to postcomposition with ``h``
(Mac Lane, *Categories for the Working Mathematician*, III.2; nLab,
*Yoneda embedding*).  It is what distinguishes ``[C^op, Set]`` from a category
of maps: its objects are functors, and ``y`` is a functor into it.
"""

from __future__ import annotations

from sage.categories.category import Category
from sage.categories.map import Map
from sage.structure.parent import Parent

from dzack_research.preamble.categories.functors.core import (
    Functor,
    NaturalTransformation,
)


class _OppositeFunctor(Functor):
    r"""``F^op: C^op -> D^op``, the functor ``F`` read on the opposite categories."""

    def __init__(self, functor: Functor) -> None:
        self._functor = functor
        super().__init__(functor.domain().opposite(), functor.codomain().opposite())

    def original(self) -> Functor:
        return self._functor

    def _apply_object(self, obj: Parent) -> Parent:
        return self.codomain()(self.original()(obj.underlying_object()))

    def _apply_morphism(self, morphism: Map) -> Map:
        # An arrow op(A) -> op(B) of C^op is an arrow B -> A of C; its image
        # is F(B) -> F(A), read as the arrow op(F(A)) -> op(F(B)) of D^op.
        return self.codomain().Mor(self(morphism.domain()), self(morphism.codomain()))(
            self.original()(morphism.underlying_arrow())
        )

    def _repr_(self) -> str:
        return f"({self.original()})^op"


class _RepresentablePresheaf(Functor):
    r"""``Mor_C(-, X): C^op -> Set`` for one object ``X`` of ``C``."""

    def __init__(self, category: Category, representing_object: Parent) -> None:
        from dzack_research.preamble.categories.sets.set_categories import Sets

        assert representing_object in category, (
            "a representable presheaf is represented by an object of its category"
        )
        self._category = category
        self._representing_object = representing_object
        super().__init__(category.opposite(), Sets())

    def representing_object(self) -> Parent:
        return self._representing_object

    def _apply_object(self, obj: Parent) -> Parent:
        return self._category.Mor(obj.underlying_object(), self.representing_object())

    def _apply_morphism(self, morphism: Map) -> Map:
        r"""Precomposition: an arrow ``u: B -> A`` of ``C`` gives ``g |-> g o u``."""
        from dzack_research.preamble.categories.sets.set_categories import Sets

        precompose = morphism.underlying_arrow()
        return Sets().Mor(self(morphism.domain()), self(morphism.codomain()))(
            lambda arrow: arrow * precompose
        )

    def _repr_(self) -> str:
        return f"Mor_{self._category}(-, {self.representing_object()})"


class _YonedaEmbedding(Functor):
    r"""``y: C -> [C^op, Set]``, ``X |-> Mor_C(-, X)``."""

    _faithful = True

    def __init__(self, category: Category) -> None:
        self._category = category
        super().__init__(category, category.presheaves())

    def _apply_object(self, obj: Parent) -> Parent:
        return self.codomain().object(_RepresentablePresheaf(self._category, obj))

    def _apply_morphism(self, morphism: Map) -> Map:
        r"""Postcomposition with ``h: X -> Y``, natural in the argument."""
        from dzack_research.preamble.categories.sets.set_categories import Sets

        source = self(morphism.domain())
        target = self(morphism.codomain())
        source_presheaf = source.arrow().functor()
        target_presheaf = target.arrow().functor()

        def component(obj):
            return Sets().Mor(source_presheaf(obj), target_presheaf(obj))(
                lambda arrow: morphism * arrow
            )

        return self.codomain().Mor(source, target)(
            NaturalTransformation(source_presheaf, target_presheaf, component)
        )

    def _repr_(self) -> str:
        return f"Yoneda embedding of {self._category}"


class _PresheafTransport(Functor):
    r"""``[C^op, D] -> [C'^op, D']`` along ``F: C' -> C`` and ``G: D -> D'``.

    This is the action of the presheaf bifunctor on a pair of arrows of
    ``Cat``: contravariant in the site through precomposition with ``F^op``,
    covariant in the values through postcomposition with ``G``.
    """

    def __init__(self, site_functor: Functor, value_functor: Functor) -> None:
        self._site_functor = site_functor
        self._value_functor = value_functor
        self._opposite_site_functor = _OppositeFunctor(site_functor)
        super().__init__(
            site_functor.codomain().presheaves(value_functor.domain()),
            site_functor.domain().presheaves(value_functor.codomain()),
        )

    def site_functor(self) -> Functor:
        return self._site_functor

    def value_functor(self) -> Functor:
        return self._value_functor

    def _transport_presheaf(self, presheaf: Functor) -> Functor:
        return self._opposite_site_functor.then(presheaf).then(self.value_functor())

    def _apply_object(self, obj: Parent) -> Parent:
        return self.codomain().object(self._transport_presheaf(obj.arrow().functor()))

    def _apply_morphism(self, morphism: Map) -> Map:
        transformation = morphism.transformation()
        source = self._transport_presheaf(transformation.source())
        target = self._transport_presheaf(transformation.target())
        opposite_site = self._opposite_site_functor
        value = self.value_functor()

        def component(obj):
            return value(transformation.component(opposite_site(obj)))

        return self.codomain().Mor(self(morphism.domain()), self(morphism.codomain()))(
            NaturalTransformation(source, target, component)
        )

    def _repr_(self) -> str:
        return f"Presh({self.site_functor()}, {self.value_functor()})"


__all__: list[str] = []
