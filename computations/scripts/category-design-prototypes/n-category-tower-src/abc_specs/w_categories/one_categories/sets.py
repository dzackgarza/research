# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/one_categories/sets.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Set ABCs.

Defines:
1. _SetCategory_ABC: The Category of Sets (Objects=Sets, Morphisms=Functions).
2. CategoryABCs.SetObject: An Object in the Category of Sets (A Set X).

Per user directive: Separation of Category vs Object logic.
"""

from __future__ import annotations

from src.local_typing import *

from src._types import BoolProof, CategoryABCs, SageType, SympyType


class _SetCategory_ABC(CategoryABCs.Nontrivial_TwoCategory, ABC):
    """
    The Category of Sets (Set).

    - Objects: Sets (instances of CategoryABCs.SetObject).
    - Morphisms: Functions.
    - Structure: Complete, Cocomplete, Cartesian Closed.
    """

    @final
    @abstractmethod
    def empty_set(self) -> CategoryABCs.SetObject:
        """Return the initial object ∅."""
        ...

    @final
    @abstractmethod
    def singleton_set(self, x: CategoryABCs.SetObject) -> CategoryABCs.SetObject:
        """Return a terminal object {x} (or specific singleton)."""
        ...

    # Standard constructions (product, coproduct) are inherited from _CatW_ABC
    # but specific return types should be CategoryABCs.SetObject.


class _SetObject_ABC(CategoryABCs.Object_In_A_1_Cat, ABC):
    """
    An Object in the Category of Sets (A Set X).

    Also viewed as a discrete category (0-category) where:
    - Objects: Elements x ∈ X.
    - Morphisms: Identities only.
    """

    @final
    @abstractmethod
    def to_python_set(self) -> set[Any]:
        ...

    @final
    @abstractmethod
    def to_sympy_set(self) -> SympyType.Set:
        ...

    @final
    @abstractmethod
    def to_sage_set(self) -> SageType.Set:
        ...

    # === Cardinality & Elements ===

    @final
    @abstractmethod
    def cardinality(self) -> SageType.Cardinality:
        """Return the cardinality of the set (|X|)."""
        ...

    @final
    @abstractmethod
    def contains(self, x: CategoryABCs.SetObject) -> bool:
        """Check if element x is in the set (x ∈ X)."""
        ...

    @final
    @abstractmethod
    def an_element(self) -> CategoryABCs.SetObject:
        """Return an arbitrary element. Raises if empty."""
        ...

    # === Set Operations ===

    @final
    @abstractmethod
    def union(self, other: CategoryABCs.SetObject) -> CategoryABCs.SetObject:
        """Return X ∪ Y."""
        ...

    @final
    @abstractmethod
    def intersection(self, other: CategoryABCs.SetObject) -> CategoryABCs.SetObject:
        """Return X ∩ Y."""
        ...

    @final
    @abstractmethod
    def difference(self, other: CategoryABCs.SetObject) -> CategoryABCs.SetObject:
        """Return X ∖ Y."""
        ...

    @final
    @abstractmethod
    def symmetric_difference(self, other: CategoryABCs.SetObject) -> CategoryABCs.SetObject:
        """Return X △ Y."""
        ...

    @final
    @abstractmethod
    def cartesian_product(self, other: CategoryABCs.SetObject) -> CategoryABCs.SetObject:
        """Return X × Y."""
        ...

    @final
    @abstractmethod
    def disjoint_union(self, other: CategoryABCs.SetObject) -> CategoryABCs.SetObject:
        """Return X ⊔ Y."""
        ...

    @final
    @abstractmethod
    def power_set(self) -> CategoryABCs.SetObject:
        """Return P(X)."""
        ...

    # === Predicates ===

    @final
    @abstractmethod
    def is_finite(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_infinite(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_countable(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_countably_infinite(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_uncountable(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_empty(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_singleton(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_subset_of(self, other: CategoryABCs.SetObject) -> BoolProof: ...

    @final
    @abstractmethod
    def is_proper_subset_of(self, other: CategoryABCs.SetObject) -> BoolProof: ...

    @final
    @abstractmethod
    def is_superset_of(self, other: CategoryABCs.SetObject) -> BoolProof: ...

    @final
    @abstractmethod
    def is_proper_superset_of(self, other: CategoryABCs.SetObject) -> BoolProof: ...

    @final
    @abstractmethod
    def is_disjoint_from(self, other: CategoryABCs.SetObject) -> BoolProof: ...

    @final
    @abstractmethod
    def is_contained_in(self, other: CategoryABCs.SetObject) -> BoolProof:
        """Alias for is_subset_of."""
        ...

    @final
    @abstractmethod
    def contains_subset(self, other: CategoryABCs.SetObject) -> BoolProof:
        """Check if self contains other as a subset (other ⊆ self)."""
        ...

    @final
    @abstractmethod
    def properly_contains_subset(self, other: CategoryABCs.SetObject) -> BoolProof:
        """Check if self properly contains other (other ⊂ self)."""
        ...

    # === Functional ===

    @final
    @abstractmethod
    def map(self, f: CategoryABCs.SetObject) -> CategoryABCs.SetObject: ...

    @final
    @abstractmethod
    def image(self, f: CategoryABCs.SetObject) -> CategoryABCs.SetObject:
        """Alias for map(f). Returns {f(x) | x ∈ X}."""
        return self.map(f)

    @final
    @abstractmethod
    def preimage(
        self, f: CategoryABCs.SetObject, codomain_subset: CategoryABCs.SetObject
    ) -> CategoryABCs.SetObject:
        """
        Return the preimage set {x ∈ X | f(x) ∈ codomain_subset}.
        f can be a function or morphism defined on X.
        """
        ...

    @final
    @abstractmethod
    def filter(self, predicate: CategoryABCs.SetObject) -> CategoryABCs.SetObject: ...

    @final
    @abstractmethod
    def defining_predicate(self) -> CategoryABCs.SetObject | None:
        """
        If this set is defined as {x ∈ Base | P(x)}, return P.
        Returns None if not applicable (e.g. extensionally defined).
        """
        ...

    @final
    @abstractmethod
    def base_set(self) -> CategoryABCs.SetObject | None:
        """
        If this set is defined as {x ∈ Base | P(x)}, return Base.
        Returns None if not applicable.
        """
        ...

    @final
    @abstractmethod
    def simplify(self) -> CategoryABCs.SetObject:
        """
        Return a simplified representation of the set if possible.
        E.g. Intersection(A, A) -> A.
        """
        ...

    @final
    @abstractmethod
    def complement(self, universe: CategoryABCs.SetObject) -> CategoryABCs.SetObject:
        """
        Return the absolute complement of X with respect to universe.
        Equivalent to universe.difference(self).
        """
        ...

    @final
    @abstractmethod
    def reduce(
        self,
        f: Callable[[CategoryABCs.SetObject, CategoryABCs.SetObject], CategoryABCs.SetObject],
        initial: CategoryABCs.SetObject | None = None,
    ) -> CategoryABCs.SetObject: ...

    @final
    @abstractmethod
    def forall(self, predicate: Callable[[CategoryABCs.SetObject], bool]) -> BoolProof: ...

    @final
    @abstractmethod
    def exists(self, predicate: Callable[[CategoryABCs.SetObject], bool]) -> BoolProof: ...

    # === Relations ===

    @overload
    @abstractmethod
    def quotient_by_relation(
        self, relation: Callable[[CategoryABCs.SetObject], CategoryABCs.SetObject]
    ) -> CategoryABCs.SetObject: ...

    @overload
    @abstractmethod
    def quotient_by_relation(
        self, relation: Callable[[CategoryABCs.SetObject, CategoryABCs.SetObject], bool]
    ) -> CategoryABCs.SetObject: ...

    @final
    @abstractmethod
    def quotient_by_relation(
        self,
        relation: (
            CategoryABCs.SetObject
            | Callable[[CategoryABCs.SetObject, CategoryABCs.SetObject], bool]
            | Callable[[CategoryABCs.SetObject], CategoryABCs.SetObject]
        ),
    ) -> CategoryABCs.SetObject:
        """
        Return the quotient set X/~.

        The 'relation' can be specified in three ways:
        1. A set of pairs R ⊆ X × X, where (a, b) ∈ R implies a ~ b.
        2. A callable `(a, b) -> bool` that returns True if a ~ b.
        3. A callable `(a) -> class_id` that maps each element to its equivalence class identifier.

        The result is a new set where each element is an equivalence class (itself a SetObject).
        """
        ...

    @final
    @abstractmethod
    def partitions(self) -> Iterable[CategoryABCs.SetObject]: ...

    @final
    @abstractmethod
    def partitions_of_size(self, k: int) -> Iterable[CategoryABCs.SetObject]:
        """Yield partitions into exactly k non-empty subsets."""
        ...

    @final
    @abstractmethod
    def subsets_of_size(self, k: int) -> Iterable[CategoryABCs.SetObject]:
        """Yield subsets of cardinality k."""
        ...

    # === Iteration ===

    @final
    @abstractmethod
    def __iter__(self) -> Iterator[CategoryABCs.SetObject]: ...


_ = _SetCategory_ABC
_ = _SetObject_ABC
