"""The owned operation spine below groups."""

from sage.categories.additive_groups import AdditiveGroups as SageAdditiveGroups
from sage.categories.additive_magmas import AdditiveMagmas as SageAdditiveMagmas
from sage.categories.additive_monoids import AdditiveMonoids as SageAdditiveMonoids
from sage.categories.additive_semigroups import AdditiveSemigroups as SageAdditiveSemigroups
from sage.categories.category import Category
from sage.categories.magmas import Magmas as SageMagmas
from sage.categories.monoids import Monoids as SageMonoids
from sage.categories.semigroups import Semigroups as SageSemigroups


class Magmas(Category):
    def super_categories(self):
        return [SageMagmas()]


class Semigroups(Category):
    def super_categories(self):
        return [SageSemigroups(), Magmas()]


class Monoids(Category):
    def super_categories(self):
        return [SageMonoids(), Semigroups()]


class AdditiveMagmas(Category):
    def super_categories(self):
        return [SageAdditiveMagmas()]


class AdditiveSemigroups(Category):
    def super_categories(self):
        return [SageAdditiveSemigroups(), AdditiveMagmas()]


class AdditiveMonoids(Category):
    def super_categories(self):
        return [SageAdditiveMonoids(), AdditiveSemigroups()]

    class ParentMethods:
        def monoidal_unit(self):
            return self.zero()


class AdditiveGroups(Category):
    def super_categories(self):
        return [SageAdditiveGroups(), AdditiveMonoids()]
