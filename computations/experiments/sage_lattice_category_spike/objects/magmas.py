r"""The multiplicative and additive operation spines.

Both spines are built from Sage's standard axioms — ``Semigroups`` is
``Magmas().Associative()``, ``Monoids`` adds ``Unital``, ``Groups`` adds
``Inverse``, with the exact additive parallel — and both roots are the
first structured forwarding owners: generic set behavior is defined here,
once, by composition through the underlying-set functor
(``X.cardinality() == U(X).cardinality()``), never re-declared by any
descendant. The route to ``Sets()`` is a faithful functor, not a
subcategory inclusion: ``UnderlyingSetFunctor`` is a first-class element
of ``Fun(root, Sets())`` whose object action is the ``UnderlyingSet``
facade and whose morphism action reads the same mapping as a set map.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from sage.categories.additive_magmas import AdditiveMagmas as SageAdditiveMagmas
from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.homset import Hom
from sage.categories.magmas import Magmas as SageMagmas
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets

from ..lexicon import SageMorphism, SageParent
from .functors import Functor
from .sets import CountabilitySubcategoryMethods

if TYPE_CHECKING:
    from .cardinals import Cardinal
    from .underlying_sets import UnderlyingSet


class _ViaUnderlyingSet:
    r"""The forwarding owner's parent methods: every generic set behavior
    of a structured parent is the corresponding behavior of its underlying
    set. Installed at the two operation roots and nowhere below."""

    def underlying_set(self) -> UnderlyingSet:
        r"""The set ``U(X)`` underlying this structured parent: the same
        elements with the operations forgotten — the single functorial
        obligation everything else rolls up through."""
        from .underlying_sets import UnderlyingSet

        # Runtime Sage copies these methods onto structured parent classes,
        # so ``self`` is a Parent there.
        return UnderlyingSet(cast("SageParent", self))

    def cardinality(self) -> Cardinal:
        return self.underlying_set().cardinality()

    def is_finite(self) -> bool:
        return self.underlying_set().is_finite()

    def is_infinite(self) -> bool:
        return not self.underlying_set().is_finite()

    def is_countable(self) -> bool:
        return self.underlying_set().is_countable()

    def is_uncountable(self) -> bool:
        return self.underlying_set().is_uncountable()

    def index(self, element: object) -> int:
        return self.underlying_set().index(element)


class Magmas(Category):
    r"""The owned category of magmas: the first structured forwarding
    owner on the multiplicative side."""

    def super_categories(self) -> list[Category]:
        return [SageMagmas()]

    if TYPE_CHECKING:

        def Countable(self) -> Category: ...
        def Uncountable(self) -> Category: ...

    SubcategoryMethods = CountabilitySubcategoryMethods

    ParentMethods = _ViaUnderlyingSet


class Semigroups(CategoryWithAxiom):
    r"""Associative magmas."""

    _base_category_class_and_axiom = (Magmas, "Associative")


class Monoids(CategoryWithAxiom):
    r"""Unital semigroups."""

    _base_category_class_and_axiom = (Semigroups, "Unital")


class Groups(CategoryWithAxiom):
    r"""Monoids with inverses."""

    _base_category_class_and_axiom = (Monoids, "Inverse")


class CountableMagmas(CategoryWithAxiom):
    r"""Magmas whose underlying set is countable. (Sage silently discards
    an axiom request with no defining class, so this class must exist even
    though the countability semantics live entirely on the ``Sets()``
    side, reached through the underlying-set route.)"""

    _base_category_class_and_axiom = (Magmas, "Countable")


class UncountableMagmas(CategoryWithAxiom):
    r"""Magmas whose underlying set is uncountable, by trusted placement."""

    _base_category_class_and_axiom = (Magmas, "Uncountable")


class AdditiveMagmas(Category):
    r"""The owned category of additive magmas: the first structured
    forwarding owner on the additive side."""

    def super_categories(self) -> list[Category]:
        return [SageAdditiveMagmas()]

    if TYPE_CHECKING:

        def Countable(self) -> Category: ...
        def Uncountable(self) -> Category: ...

    SubcategoryMethods = CountabilitySubcategoryMethods

    ParentMethods = _ViaUnderlyingSet


class AdditiveSemigroups(CategoryWithAxiom):
    r"""Additively associative additive magmas."""

    _base_category_class_and_axiom = (AdditiveMagmas, "AdditiveAssociative")


class AdditiveMonoids(CategoryWithAxiom):
    r"""Additively unital additive semigroups."""

    _base_category_class_and_axiom = (AdditiveSemigroups, "AdditiveUnital")


class AdditiveGroups(CategoryWithAxiom):
    r"""Additive monoids with additive inverses."""

    _base_category_class_and_axiom = (AdditiveMonoids, "AdditiveInverse")


class CountableAdditiveMagmas(CategoryWithAxiom):
    r"""Additive magmas whose underlying set is countable."""

    _base_category_class_and_axiom = (AdditiveMagmas, "Countable")


class UncountableAdditiveMagmas(CategoryWithAxiom):
    r"""Additive magmas whose underlying set is uncountable, by trusted
    placement."""

    _base_category_class_and_axiom = (AdditiveMagmas, "Uncountable")


class UnderlyingSetFunctor(Functor):
    r"""The structure-forgetting functor from an operation root to the
    owned ``Sets()``: faithful (its ``Sets``-valued faithfulness is exactly
    concreteness), preserving elements on objects and mappings on
    morphisms."""

    _faithful = True

    def __init__(self, domain_category: Category) -> None:
        from .sets import Sets

        Functor.__init__(self, domain_category, Sets())

    def _apply_functor(self, structured: SageParent) -> UnderlyingSet:
        from .underlying_sets import UnderlyingSet

        return UnderlyingSet(structured)

    def _apply_functor_to_morphism(self, morphism: SageMorphism) -> SetMorphism:
        from .underlying_sets import UnderlyingSet

        domain = UnderlyingSet(morphism.domain())
        codomain = UnderlyingSet(morphism.codomain())
        return SetMorphism(Hom(domain, codomain, SageSets()), morphism)


if not TYPE_CHECKING:
    # Sage's class-resolution shortcut for the axiom spine; runtime-only.
    Magmas.Associative = Semigroups
    Semigroups.Unital = Monoids
    Monoids.Inverse = Groups
    Magmas.Countable = CountableMagmas
    Magmas.Uncountable = UncountableMagmas
    AdditiveMagmas.AdditiveAssociative = AdditiveSemigroups
    AdditiveSemigroups.AdditiveUnital = AdditiveMonoids
    AdditiveMonoids.AdditiveInverse = AdditiveGroups
    AdditiveMagmas.Countable = CountableAdditiveMagmas
    AdditiveMagmas.Uncountable = UncountableAdditiveMagmas
