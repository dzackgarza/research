r"""Set constructions: images, exponentials, powersets, and finite subsets."""

from collections.abc import Callable, Iterable

from sage.categories.category import Category
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.combinat.subset import Subsets as SageSubsets
from sage.misc.cachefunc import cached_function
from sage.rings.integer_ring import ZZ
from sage.sets.condition_set import ConditionSet as SageConditionSet
from sage.sets.image_set import ImageSet as SageImageSet
from sage.sets.set import Set as SageSet
from sage.structure.element import Element
from sage.structure.parent import Parent

from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.owned_sets import Sets as OwnedSets


def Set(source):
    r"""Return ``source`` as a Sage set object."""
    return source if source in OwnedSets() or source in SageSets() else SageSet(source)


def ConditionSet(universe, predicate):
    r"""Return the subset of ``universe`` cut out by ``predicate``."""
    return SageConditionSet(universe, predicate)


def ImageSet(map_, domain_subset, *, category=None, is_injective=None, inverse=None):
    r"""Return the image of ``domain_subset`` under ``map_``."""
    return SageImageSet(
        map_,
        domain_subset,
        category=category,
        is_injective=is_injective,
        inverse=inverse,
    )


class SetInjection(SetMorphism):
    r"""A set morphism supplied with the assertion that it is injective."""

    def is_injective(self) -> bool:
        return True


class SetSurjection(SetMorphism):
    r"""A set morphism supplied with the assertion that it is surjective."""

    def is_surjective(self) -> bool:
        return True


def set_injection(domain, codomain, function):
    return SetInjection(Hom(domain, codomain, OwnedSets()), function)


def set_surjection(domain, codomain, function):
    return SetSurjection(Hom(domain, codomain, OwnedSets()), function)


class SetInclusion(SetMorphism):
    r"""A represented subobject inclusion \(A\hookrightarrow X\)."""

    def __init__(
        self,
        domain,
        codomain,
        characteristic_morphism=None,
        finite_members=None,
    ) -> None:
        parent = Hom(domain, codomain, OwnedSets())
        SetMorphism.__init__(self, parent, lambda member: codomain(member))
        self._characteristic_morphism = characteristic_morphism
        self._finite_members = finite_members

    def inclusion(self):
        return self

    def is_injective(self) -> bool:
        return True

    def factor_through(self, target_inclusion):
        r"""Return the canonical map of subset objects when this subset is contained."""
        if target_inclusion.codomain() is not self.codomain():
            raise ValueError("subset factorization requires one common base set")
        if not self <= target_inclusion:
            raise ValueError("the first subset is not contained in the second")
        return SetMorphism(
            Hom(self.domain(), target_inclusion.domain(), OwnedSets()),
            lambda member: target_inclusion.domain()(self(member)),
        )

    def underlying_set(self):
        return self.domain()

    def characteristic_morphism(self):
        if self._characteristic_morphism is None:
            raise NotImplementedError(
                "this subobject has no represented decidable characteristic morphism"
            )
        return self._characteristic_morphism

    def __contains__(self, member) -> bool:
        if member not in self.codomain():
            return False
        if self._finite_members is not None:
            return member in self._finite_members
        characteristic = self.characteristic_morphism()
        return characteristic(member) == characteristic.codomain()(1)

    def __iter__(self):
        return iter(self.domain())

    def cardinality(self):
        if self._finite_members is not None:
            return cardinal(len(self._finite_members))
        return cardinal(self.domain().cardinality())

    def __len__(self) -> int:
        size = self.cardinality()
        if not size.is_finite():
            raise TypeError("length is defined only for finite subsets")
        return int(size)

    def _check_common_base(self, other) -> None:
        if self.codomain() is not other.codomain():
            raise ValueError("subset operations require one common base set")

    def __le__(self, other) -> bool:
        self._check_common_base(other)
        if self._finite_members is not None:
            return all(member in other for member in self._finite_members)
        base = self.codomain()
        if base in FiniteEnumeratedSets():
            return all(member not in self or member in other for member in base)
        raise NotImplementedError(
            "this subset relation has no represented decision procedure"
        )

    def union(self, other):
        self._check_common_base(other)
        return PowerSet(self.codomain()).from_predicate(
            lambda member: member in self or member in other
        )

    def intersection(self, other):
        self._check_common_base(other)
        return PowerSet(self.codomain()).from_predicate(
            lambda member: member in self and member in other
        )

    def difference(self, other):
        self._check_common_base(other)
        return PowerSet(self.codomain()).from_predicate(
            lambda member: member in self and member not in other
        )

    def symmetric_difference(self, other):
        self._check_common_base(other)
        return PowerSet(self.codomain()).from_predicate(
            lambda member: (member in self) != (member in other)
        )

    def complement(self):
        return PowerSet(self.codomain()).from_predicate(lambda member: member not in self)

    def __or__(self, other):
        return self.union(other)

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other not in PowerSet(self.codomain()):
            return False
        if self._finite_members is not None and other._finite_members is not None:
            return len(self._finite_members) == len(other._finite_members) and all(
                member in other for member in self._finite_members
            )
        if self.codomain() in FiniteEnumeratedSets():
            return all((member in self) == (member in other) for member in self.codomain())
        return self._characteristic_morphism is other._characteristic_morphism

    def __ne__(self, other) -> bool:
        return not self == other

    def _repr_(self) -> str:
        return f"Subobject of {self.codomain()} defined by {self.domain()}"


class PowerSetParent(Parent):
    r"""The power object \(P(X)\), represented by subobjects of ``X``."""

    def __init__(self, base_set) -> None:
        if base_set not in SageSets():
            raise TypeError("a power set is formed from a set")
        self._base_set = base_set
        Parent.__init__(self, category=SageSets())

    def base_set(self):
        return self._base_set

    def truth_values(self):
        from dzack_research.preamble.categories.sets.owned_sets import Sets

        return Sets.Δ[1]

    def characteristic_homset(self):
        return Hom(self.base_set(), self.truth_values(), SageSets())

    characteristic_hom_category = characteristic_homset

    def _subset_from_predicate(self, predicate: Callable):
        truth_values = self.truth_values()
        characteristic = SetMorphism(
            self.characteristic_homset(),
            lambda member: truth_values(ZZ.one() if predicate(member) else ZZ.zero()),
        )
        domain = ConditionSet(self.base_set(), predicate)
        return SetInclusion(domain, self.base_set(), characteristic)

    def from_predicate(self, predicate: Callable):
        return self._subset_from_predicate(predicate)

    def from_characteristic_morphism(self, characteristic_morphism):
        if characteristic_morphism.parent() is not self.characteristic_homset():
            raise ValueError("a characteristic morphism must lie in Hom(X, Δ[1])")
        truth = self.truth_values()(1)

        def predicate(member):
            return characteristic_morphism(member) == truth

        domain = ConditionSet(self.base_set(), predicate)
        return SetInclusion(domain, self.base_set(), characteristic_morphism)

    def _from_finite_members(self, members):
        normalized = []
        for member in members:
            if member not in self.base_set():
                raise ValueError(f"{member!r} is not in {self.base_set()}")
            if member not in normalized:
                normalized.append(member)
        frozen = tuple(normalized)
        truth_values = self.truth_values()
        characteristic = SetMorphism(
            self.characteristic_homset(),
            lambda member: truth_values(ZZ.one() if member in frozen else ZZ.zero()),
        )
        domain = ConditionSet(self.base_set(), lambda member: member in frozen)
        return SetInclusion(domain, self.base_set(), characteristic, frozen)

    def _element_constructor_(self, candidate):
        if isinstance(candidate, SetInclusion):
            if candidate.codomain() is not self.base_set():
                raise ValueError("the subobject has a different base set")
            return candidate
        if candidate is self.base_set():
            return self.from_predicate(lambda _member: True)
        if candidate in SageSets() and candidate in FiniteEnumeratedSets():
            return self._from_finite_members(candidate)
        if isinstance(candidate, Iterable):
            return self._from_finite_members(candidate)
        raise TypeError(f"{candidate!r} does not present a subset of {self.base_set()}")

    def __contains__(self, candidate) -> bool:
        if isinstance(candidate, SetInclusion):
            return candidate.codomain() is self.base_set()
        if candidate is self.base_set():
            return True
        if candidate in SageSets() and candidate in FiniteEnumeratedSets():
            return all(member in self.base_set() for member in candidate)
        if isinstance(candidate, Iterable):
            return all(member in self.base_set() for member in candidate)
        return False

    def top(self):
        return self(self.base_set())

    def bottom(self):
        return self(())

    def inverse_image_morphism(self, morphism):
        if morphism.codomain() is not self.base_set():
            raise ValueError("inverse image requires the morphism codomain to be the base set")
        target = PowerSet(morphism.domain())
        return SetMorphism(
            Hom(self, target, OwnedSets()),
            lambda subset: target.from_predicate(lambda member: morphism(member) in subset),
        )

    def direct_image_morphism(self, morphism):
        if morphism.domain() is not self.base_set():
            raise ValueError("direct image requires the morphism domain to be the base set")
        target = PowerSet(morphism.codomain())

        def direct_image(subset):
            size = subset.cardinality()
            if not size.is_finite():
                image_domain = ImageSet(morphism, subset.domain())
                return SetInclusion(image_domain, morphism.codomain())
            return target(tuple(morphism(member) for member in subset))

        return SetMorphism(Hom(self, target, OwnedSets()), direct_image)

    def __iter__(self):
        if self.base_set() not in FiniteEnumeratedSets():
            raise TypeError("only a finite power set has a chosen enumeration")
        return (self(subset) for subset in SageSubsets(self.base_set()))

    def cardinality(self):
        return cardinal(2) ** cardinal(self.base_set().cardinality())

    def cardinality_comparison(self):
        from dzack_research.preamble.categories.sets.cardinals import Cardinalities

        size = self.cardinality()
        return Cardinalities().hom(size, size).identity()

    def _repr_(self) -> str:
        return f"Power set of {self.base_set()}"


@cached_function
def PowerSet(base_set):
    return PowerSetParent(base_set)


class FunctionSet(Parent):
    r"""The exponential \(Y^X=\operatorname{Hom}_{Set}(X,Y)\)."""

    def __init__(self, codomain, exponent) -> None:
        if codomain not in SageSets() or exponent not in SageSets():
            raise TypeError("an exponential requires two sets")
        self._codomain = codomain
        self._exponent = exponent
        Parent.__init__(self, category=SageSets())

    def base(self):
        return self._codomain

    def exponent(self):
        return self._exponent

    def homset(self):
        return Hom(self.exponent(), self.base(), SageSets())

    def _element_constructor_(self, definition):
        if definition in self.homset():
            return definition
        return SetMorphism(self.homset(), definition)

    def __contains__(self, function) -> bool:
        return function in self.homset()

    def cardinality(self):
        return cardinal(self.base().cardinality()) ** cardinal(self.exponent().cardinality())

    def _repr_(self) -> str:
        return f"{self.base()}^{self.exponent()}"


@cached_function
def ExponentialOfSets(codomain, exponent):
    return FunctionSet(codomain, exponent)


class FixedCardinalitySubsets(Parent):
    r"""The set \([X]^k\) of subsets of a fixed finite cardinality."""

    def __init__(self, source, subset_cardinality) -> None:
        self._source = source
        self._subset_cardinality = ZZ(subset_cardinality)
        if self._subset_cardinality < 0:
            raise ValueError("a subset cardinality is nonnegative")
        Parent.__init__(self, category=SageSets())

    def source(self):
        return self._source

    def subset_cardinality(self):
        return self._subset_cardinality

    def power_set(self):
        return PowerSet(self.source())

    def _element_constructor_(self, members):
        subset = self.power_set()(members)
        if subset.cardinality() != cardinal(self.subset_cardinality()):
            raise ValueError(
                f"a member of {self} has cardinality {self.subset_cardinality()}"
            )
        return subset

    def __contains__(self, candidate) -> bool:
        if candidate not in self.power_set():
            return False
        return self.power_set()(candidate).cardinality() == cardinal(
            self.subset_cardinality()
        )

    def __iter__(self):
        if self.source() not in FiniteEnumeratedSets():
            raise TypeError(
                "the current enumeration of fixed-cardinality subsets requires a finite source"
            )
        return (
            self(tuple(subset))
            for subset in SageSubsets(self.source(), self.subset_cardinality())
        )

    def cardinality(self):
        from sage.arith.misc import binomial

        source_size = cardinal(self.source().cardinality())
        if self.subset_cardinality() == 0:
            return cardinal(1)
        if source_size.is_finite():
            return cardinal(binomial(source_size.finite_value(), self.subset_cardinality()))
        return source_size

    def _repr_(self) -> str:
        return f"Subsets of {self.source()} of cardinality {self.subset_cardinality()}"


@cached_function
def SubsetsOfSize(source, subset_cardinality):
    return FixedCardinalitySubsets(source, subset_cardinality)


class FiniteSubsetsParent(Parent):
    r"""The set \(P_{fin}(X)\) of finite subsets of ``X``."""

    def __init__(self, source) -> None:
        self._source = source
        Parent.__init__(self, category=SageSets())

    def source(self):
        return self._source

    def power_set(self):
        return PowerSet(self.source())

    def _element_constructor_(self, members):
        subset = self.power_set()(members)
        if not subset.cardinality().is_finite():
            raise ValueError("a member of the finite powerset must be finite")
        return subset

    def __contains__(self, candidate) -> bool:
        if candidate not in self.power_set():
            return False
        return self.power_set()(candidate).cardinality().is_finite()

    def __iter__(self):
        if self.source() not in FiniteEnumeratedSets():
            raise TypeError(
                "the current enumeration of finite subsets requires a finite source"
            )
        return (self(tuple(subset)) for subset in SageSubsets(self.source()))

    def cardinality(self):
        source_size = cardinal(self.source().cardinality())
        if source_size.is_finite():
            return cardinal(2) ** source_size
        return source_size

    def _repr_(self) -> str:
        return f"Finite subsets of {self.source()}"


@cached_function
def FiniteSubsets(source):
    return FiniteSubsetsParent(source)


__all__ = [
    "ConditionSet",
    "ExponentialOfSets",
    "FiniteSubsets",
    "FixedCardinalitySubsets",
    "FunctionSet",
    "ImageSet",
    "PowerSet",
    "PowerSetParent",
    "Set",
    "SetInclusion",
    "SetInjection",
    "SetSurjection",
    "set_injection",
    "set_surjection",
    "SubsetsOfSize",
]


class CartesianProductsOfSets(Category):
    r"""Dependent products of families of sets."""

    def super_categories(self):
        return [SageSets()]


class CoproductsOfSets(Category):
    r"""Dependent coproducts (disjoint unions) of families of sets."""

    def super_categories(self):
        return [SageSets()]


DisjointUnionsOfSets = CoproductsOfSets


class CartesianProductElement(Element):
    r"""A section ``i |-> x_i`` of a family of sets."""

    def __init__(self, parent, components) -> None:
        Element.__init__(self, parent)
        self._components = components

    def component(self, index):
        normalized = self.parent().index_set()(index)
        value = self._components(normalized)
        return self.parent().factor(normalized)(value)

    def __getitem__(self, index):
        return self.component(index)

    def _repr_(self) -> str:
        index_set = self.parent().index_set()
        try:
            return "(" + ", ".join(
                repr(self.component(index)) for index in index_set
            ) + ")"
        except TypeError:
            return f"Section of {self.parent()}"

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if not isinstance(other, CartesianProductElement) or other.parent() is not self.parent():
            return False
        index_set = self.parent().index_set()
        try:
            return all(self.component(index) == other.component(index) for index in index_set)
        except TypeError:
            return False

    def __ne__(self, other) -> bool:
        return not self == other


class CartesianProductOfFamilyParent(Parent):
    Element = CartesianProductElement

    def __init__(self, index_set, family) -> None:
        if index_set not in SageSets():
            raise TypeError("the index object of a product family must be a set")
        self._index_set = index_set
        self._family = family
        Parent.__init__(self, category=CartesianProductsOfSets())

    def index_set(self):
        return self._index_set

    def family(self):
        return self._family

    def factor(self, index):
        normalized = self.index_set()(index)
        factor = self.family()(normalized)
        if factor not in SageSets():
            raise TypeError("every factor of a set product must be a set")
        return factor

    def _element_constructor_(self, components):
        if isinstance(components, CartesianProductElement):
            if components.parent() is self:
                return components
            raise ValueError("the section belongs to a different product")
        if callable(components):
            component_function = components
        else:
            index_values = tuple(self.index_set())
            values = tuple(components)
            if len(index_values) != len(values):
                raise ValueError("a product element needs one component per factor")
            assignment = dict(zip(index_values, values, strict=True))
            component_function = assignment.__getitem__
        result = self.element_class(self, component_function)
        # Construction checks each represented component when the index set is enumerable.
        try:
            for index in self.index_set():
                result.component(index)
        except TypeError:
            pass
        return result

    def projection(self, index):
        normalized = self.index_set()(index)
        return SetMorphism(
            Hom(self, self.factor(normalized), SageSets()),
            lambda element: element.component(normalized),
        )

    def from_maps(self, source, maps):
        r"""Return the unique map into the product with the stated components."""
        return SetMorphism(
            Hom(source, self, OwnedSets()),
            lambda element: self(lambda index: maps(index)(element)),
        )

    def cardinality(self):
        from dzack_research.preamble.categories.sets.cardinals import Cardinalities, cardinal

        return Cardinalities().indexed_product(
            self.index_set(), lambda index: cardinal(self.factor(index).cardinality())
        )

    def __iter__(self):
        from itertools import product

        index_values = tuple(self.index_set())
        factors = tuple(self.factor(index) for index in index_values)
        return (
            self(values)
            for values in product(*(tuple(factor) for factor in factors))
        )

    def _repr_(self) -> str:
        return f"Product of the family over {self.index_set()}"


@cached_function
def CartesianProductOfFamily(index_set, family):
    return CartesianProductOfFamilyParent(index_set, family)


@cached_function
def _cartesian_product_of_tuple(factors):
    from dzack_research.preamble.categories.sets.owned_sets import Sets

    index_set = Sets.Δ[len(factors) - 1]
    return CartesianProductOfFamilyParent(
        index_set, lambda index: factors[int(index)]
    )


def CartesianProductOfSets(*factors):
    return _cartesian_product_of_tuple(tuple(factors))


def cartesian_product_of(factors):
    return CartesianProductOfSets(*tuple(factors))


def CartesianProductMorphism(source, target, component_morphisms):
    r"""Return the componentwise map between two dependent products."""
    if source.index_set() != target.index_set():
        raise ValueError("componentwise product maps require one index set")
    return SetMorphism(
        Hom(source, target, OwnedSets()),
        lambda element: target(
            lambda index: component_morphisms(index)(element.component(index))
        ),
    )


class CoproductElement(Element):
    r"""An element of a dependent sum, carrying its summand index."""

    def __init__(self, parent, index, value) -> None:
        Element.__init__(self, parent)
        normalized = parent.index_set()(index)
        self._index = normalized
        self._value = parent.cofactor(normalized)(value)

    def summand_index(self):
        return self._index

    def summand_element(self):
        return self._value

    def _repr_(self) -> str:
        return f"ι_{self.summand_index()}({self.summand_element()})"

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, CoproductElement)
            and other.parent() is self.parent()
            and other.summand_index() == self.summand_index()
            and other.summand_element() == self.summand_element()
        )

    def __ne__(self, other) -> bool:
        return not self == other


class CoproductOfFamilyParent(Parent):
    Element = CoproductElement

    def __init__(self, index_set, family) -> None:
        if index_set not in SageSets():
            raise TypeError("the index object of a coproduct family must be a set")
        self._index_set = index_set
        self._family = family
        Parent.__init__(self, category=CoproductsOfSets())

    def index_set(self):
        return self._index_set

    def family(self):
        return self._family

    def cofactor(self, index):
        normalized = self.index_set()(index)
        cofactor = self.family()(normalized)
        if cofactor not in SageSets():
            raise TypeError("every cofactor of a set coproduct must be a set")
        return cofactor

    def _element_constructor_(self, datum, value=None):
        if isinstance(datum, CoproductElement):
            if datum.parent() is self:
                return datum
            raise ValueError("the element belongs to a different coproduct")
        if value is None:
            index, value = datum
        else:
            index = datum
        return self.element_class(self, index, value)

    def injection(self, index):
        normalized = self.index_set()(index)
        return SetMorphism(
            Hom(self.cofactor(normalized), self, SageSets()),
            lambda element: self(normalized, element),
        )

    def from_maps(self, target, maps):
        r"""Return the unique map out of the coproduct extending the stated maps."""
        return SetMorphism(
            Hom(self, target, OwnedSets()),
            lambda element: maps(element.summand_index())(element.summand_element()),
        )

    def cardinality(self):
        from dzack_research.preamble.categories.sets.cardinals import Cardinalities, cardinal

        return Cardinalities().indexed_sum(
            self.index_set(), lambda index: cardinal(self.cofactor(index).cardinality())
        )

    def __iter__(self):
        return (
            self(index, element)
            for index in self.index_set()
            for element in self.cofactor(index)
        )

    def _repr_(self) -> str:
        return f"Coproduct of the family over {self.index_set()}"


@cached_function
def CoproductOfFamily(index_set, family):
    return CoproductOfFamilyParent(index_set, family)


@cached_function
def _coproduct_of_tuple(cofactors):
    from dzack_research.preamble.categories.sets.owned_sets import Sets

    index_set = Sets.Δ[len(cofactors) - 1]
    return CoproductOfFamilyParent(
        index_set, lambda index: cofactors[int(index)]
    )


def CoproductOfSets(*cofactors):
    return _coproduct_of_tuple(tuple(cofactors))


def CoproductMorphism(source, target, component_morphisms):
    r"""Return the componentwise map between two dependent coproducts."""
    if source.index_set() != target.index_set():
        raise ValueError("componentwise coproduct maps require one index set")
    return SetMorphism(
        Hom(source, target, OwnedSets()),
        lambda element: target(
            element.summand_index(),
            component_morphisms(element.summand_index())(element.summand_element()),
        ),
    )


ObjectSetsOfDiscreteCategories = SageSets
ExponentialsOfSets = FunctionSet
PowerSets = PowerSetParent
FinitePowerSets = FiniteSubsetsParent


__all__.extend(
    [
        "CartesianProductMorphism",
        "CartesianProductOfFamily",
        "CartesianProductOfSets",
        "CartesianProductsOfSets",
        "CoproductMorphism",
        "CoproductOfFamily",
        "CoproductOfSets",
        "CoproductsOfSets",
        "DisjointUnionsOfSets",
        "FinitePowerSets",
        "ObjectSetsOfDiscreteCategories",
        "PowerSets",
        "cartesian_product_of",
    ]
)
