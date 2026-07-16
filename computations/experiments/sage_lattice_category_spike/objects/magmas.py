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

from typing import TYPE_CHECKING

from sage.categories.additive_magmas import AdditiveMagmas as SageAdditiveMagmas
from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.homset import Hom
from sage.categories.magmas import Magmas as SageMagmas
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets

from ..lexicon import SageMorphism, SageParent
from .functors import CatObject, Functor
from .sets import CountabilitySubcategoryMethods
from .underlying_sets import ViaUnderlyingSet

if TYPE_CHECKING:
    from .underlying_sets import UnderlyingSet


class Magmas(CatObject, Category):
    r"""The owned category of magmas: the first structured forwarding
    owner on the multiplicative side."""

    def super_categories(self) -> list[Category]:
        return [SageMagmas()]

    if TYPE_CHECKING:

        def Countable(self) -> Category: ...
        def Uncountable(self) -> Category: ...

    SubcategoryMethods = CountabilitySubcategoryMethods

    ParentMethods = ViaUnderlyingSet


class Semigroups(CatObject, CategoryWithAxiom):
    r"""Associative magmas."""

    _base_category_class_and_axiom = (Magmas, "Associative")


class Monoids(CatObject, CategoryWithAxiom):
    r"""Unital semigroups."""

    _base_category_class_and_axiom = (Semigroups, "Unital")


class Groups(CatObject, CategoryWithAxiom):
    r"""Monoids with inverses."""

    _base_category_class_and_axiom = (Monoids, "Inverse")


class CountableMagmas(CatObject, CategoryWithAxiom):
    r"""Magmas whose underlying set is countable. (Sage silently discards
    an axiom request with no defining class, so this class must exist even
    though the countability semantics live entirely on the ``Sets()``
    side, reached through the underlying-set route.) Carries the same
    Sage-``EnumeratedSets`` ADAPTER integration as the owned ``Countable``
    sets — internal wiring only; the owned notion is countability — so
    Sage's construction machinery consumes countable structured parents
    natively."""

    _base_category_class_and_axiom = (Magmas, "Countable")

    def extra_super_categories(self) -> list[Category]:
        from sage.categories.enumerated_sets import EnumeratedSets

        return [EnumeratedSets()]


class UncountableMagmas(CatObject, CategoryWithAxiom):
    r"""Magmas whose underlying set is uncountable, by trusted placement."""

    _base_category_class_and_axiom = (Magmas, "Uncountable")


class AdditiveMagmas(CatObject, Category):
    r"""The owned category of additive magmas: the first structured
    forwarding owner on the additive side."""

    def super_categories(self) -> list[Category]:
        return [SageAdditiveMagmas()]

    if TYPE_CHECKING:

        def Countable(self) -> Category: ...
        def Uncountable(self) -> Category: ...

    SubcategoryMethods = CountabilitySubcategoryMethods

    ParentMethods = ViaUnderlyingSet


class AdditiveSemigroups(CatObject, CategoryWithAxiom):
    r"""Additively associative additive magmas."""

    _base_category_class_and_axiom = (AdditiveMagmas, "AdditiveAssociative")


class AdditiveMonoids(CatObject, CategoryWithAxiom):
    r"""Additively unital additive semigroups."""

    _base_category_class_and_axiom = (AdditiveSemigroups, "AdditiveUnital")

    if TYPE_CHECKING:
        # Sage's standard axiom, synthesized at runtime.
        def AdditiveCommutative(self) -> Category: ...


class AdditiveGroups(CatObject, CategoryWithAxiom):
    r"""Additive monoids with additive inverses."""

    _base_category_class_and_axiom = (AdditiveMonoids, "AdditiveInverse")

    if TYPE_CHECKING:
        # Sage's standard axiom, synthesized at runtime.
        def AdditiveCommutative(self) -> Category: ...


class CountableAdditiveMagmas(CatObject, CategoryWithAxiom):
    r"""Additive magmas whose underlying set is countable, carrying the
    same Sage-adapter wiring."""

    _base_category_class_and_axiom = (AdditiveMagmas, "Countable")

    def extra_super_categories(self) -> list[Category]:
        from sage.categories.enumerated_sets import EnumeratedSets

        return [EnumeratedSets()]


class UncountableAdditiveMagmas(CatObject, CategoryWithAxiom):
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
