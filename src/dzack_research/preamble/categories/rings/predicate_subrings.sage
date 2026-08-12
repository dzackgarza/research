r"""Subrings cut out of an ambient ring by a membership predicate.

The centre \(Z(R)=\{z\in R:zr=rz\text{ for all }r\}\) is the shape of all of
them, as are the centralizer of an element, the fixed ring of a group of
automorphisms, and the integral closure of a subring.  None of these can be
handed over as generators and relations: for a free construction on two
letters the centre is a theorem, and for a ring given by a multiplication
table it is a computation that does not finish.  What is always available is
*containment* -- deciding \(z\in Z(R)\) -- so the subring is specified by the
predicate that decides it, together with the inclusion recording it as a
subobject of the ambient ring.

Nothing is enumerated and nothing is closed.  A generating set, a basis over
the ambient ring's base, finiteness and Noetherianity are questions such a
subring is entitled not to know: each is a theorem or an expensive
computation, and an operation needing one asks for it at the point of use.

This is the ring-side companion of ``predicate_subgroups.sage``, and the two
say the same thing about two structures.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Callable

if TYPE_CHECKING:
    from sage.categories.category import Category
    from sage_lattice_category_spike.lexicon import Element
    from sage.rings.ring import Ring

from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.categories.sets_cat import Sets
from sage.structure.parent import Parent


class PredicateSubring(Parent):
    r"""The subring \(\{z\in R: P(z)\}\) of an ambient ring \(R\)."""

    def __init__(
        self,
        ambient_ring: "Ring",
        predicate: "Callable",
        description: str,
        category: "Category",
    ) -> None:
        assert ambient_ring in SageRings(), (
            f"{ambient_ring} is not a ring, so it has no subrings"
        )
        # Stored before ``Parent.__init__`` so identity is answerable while
        # Sage's caches hash this object during construction.
        self._ambient_ring = ambient_ring
        self._predicate = predicate
        self._description = description
        # The category is the caller's to state and not the predicate's to
        # imply: a subring of a noncommutative ring may be commutative and
        # may not -- the centre always is, the centralizer of one element
        # need not be -- and nothing in a membership test says which.
        Parent.__init__(self, category=category)

    def ambient_ring(self) -> "Ring":
        r"""Return \(R\), the ring this is a subring of."""
        return self._ambient_ring

    def defining_predicate(self) -> "Callable":
        r"""Return \(P\), the predicate deciding membership."""
        return self._predicate

    def __contains__(self, element: "Element") -> bool:
        r"""Return whether \(z\in R\) and \(P(z)\) -- the one always-available operation."""
        return element in self._ambient_ring and bool(self._predicate(element))

    def _element_constructor_(self, element: "Element") -> "Element":
        assert element in self, f"{element} does not satisfy {self._description}"
        return element

    def one(self) -> "Element":
        identity = self._ambient_ring.one()
        assert identity in self, (
            f"{self._description} does not contain 1, so it is not a subring"
        )
        return identity

    def zero(self) -> "Element":
        zero = self._ambient_ring.zero()
        assert zero in self, (
            f"{self._description} does not contain 0, so it is not a subring"
        )
        return zero

    def inclusion(self) -> SetMorphism:
        r"""Return the inclusion \(S\hookrightarrow R\) recording the subobject."""
        return SetMorphism(
            Hom(self, self._ambient_ring, Sets()),
            lambda element: element,
        )

    def __hash__(self) -> int:
        return hash((type(self), self._ambient_ring, self._description))

    def __eq__(self, other: object) -> bool:
        return (
            type(other) is type(self)
            and self._ambient_ring == other._ambient_ring
            and self._description == other._description
        )

    def _repr_(self) -> str:
        return f"{{z in {self._ambient_ring} : {self._description}}}"
