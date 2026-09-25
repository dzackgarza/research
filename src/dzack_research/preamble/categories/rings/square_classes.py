r"""The square-class group \(R^\times/(R^\times)^2\) of a commutative ring.

For a commutative ring \(R\) the squaring map \(u\mapsto u^2\) is an
endomorphism of the abelian group \(R^\times\), and its cokernel is the
square-class group \(R^\times/(R^\times)^2\).  Every element has order
dividing two, since \([u]^2=[u^2]\) is trivial.  A class \([u]\) is named by
any representative unit, and \([u]=[v]\) exactly when \(uv\) is a square:
\(uv=(u/v)\,v^2\), so \(uv\) is a square iff \(u/v\) is.  Deciding equality
is therefore deciding squareness in \(R\), which the ring element answers.

It is the codomain of the spinor norm
\(\mathrm{sn}_K\colon O(L\otimes K)\to K^\times/(K^\times)^2\)
[GHS08, §1], and a ring morphism \(\varphi\colon R\to S\) induces
\([u]\mapsto[\varphi(u)]\): it sends units to units and squares to squares.
"""

from sage.categories.morphism import SetMorphism
from sage.misc.latex import latex
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import MultiplicativeGroupElement

from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.groups import AbelianGroups, OwnedGroups
from dzack_research.preamble.categories.rings.ring_foundation import (
    CommutativeRings,
    _own_ring,
)
from dzack_research.preamble.owned_category import _object_of


class SquareClass(MultiplicativeGroupElement):
    r"""The class \([u]\in R^\times/(R^\times)^2\) of a unit \(u\) of \(R\)."""

    def __init__(self, parent, representative) -> None:
        MultiplicativeGroupElement.__init__(self, parent)
        self._representative = representative

    def representative(self):
        r"""Return the unit this class was named by; any other representative differs by a square."""
        return self._representative

    def _mul_(self, other):
        r"""\([u][v]=[uv]\)."""
        return self.parent()(self._representative * other._representative)

    def __invert__(self):
        r"""\([u]^{-1}=[u^{-1}]=[u\cdot u^{-2}]=[u]\): every class is its own inverse."""
        return self

    def is_one(self) -> bool:
        r"""Whether \([u]\) is trivial, that is whether \(u\) is a square."""
        return bool(self._representative.is_square())

    def order(self):
        r"""The order of \([u]\): one when \(u\) is a square, two otherwise."""
        integers = _own_ring(SageZZ)
        return integers.one() if self.is_one() else integers(2)

    multiplicative_order = order

    def __eq__(self, other):
        r"""\([u]=[v]\) exactly when \(uv\) is a square."""
        return other in self.parent() and bool(
            (self._representative * other._representative).is_square()
        )

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        r"""Constant on the group: a class has no canonical representative over a general ring."""
        return hash(id(self.parent()))

    def _repr_(self):
        return f"[{self._representative}]"

    def _latex_(self):
        return rf"\left[{latex(self._representative)}\right]"


class _SquareClassGroup:
    r"""The cokernel \(R^\times/(R^\times)^2\) of squaring on \(R^\times\), at ``AbelianGroups()``.

    The ring is the defining datum; the group law is the ring's
    multiplication on representatives.
    """

    def __init__(self, ring, **rest) -> None:
        self._ring = ring
        super().__init__(**rest)

    def ring(self):
        r"""Return \(R\)."""
        return self._ring

    def unit_group(self):
        r"""Return \(R^\times\), of which this group is the quotient by the squares."""
        return self._ring.unit_group()

    def projection(self):
        r"""Return the quotient map \(R^\times\to R^\times/(R^\times)^2\), \(u\mapsto[u]\)."""
        units = self.unit_group()
        return SetMorphism(units.Mor(self), lambda unit: self(unit))

    def __call__(self, datum):
        return self._element_constructor_(datum)

    def _element_constructor_(self, datum):
        r"""Return a class of this group, or the class \([u]\) of a unit \(u\) of \(R\)."""
        if datum in self:
            return datum
        unit = self._ring(datum)
        assert unit.is_unit(), (
            f"{datum} has no class in {self}: a square class is the class of a unit, "
            f"and {unit} is not a unit of {self._ring}"
        )
        return self.element_class(self, unit)

    def __contains__(self, datum) -> bool:
        return isinstance(datum, SquareClass) and datum.parent() is self

    def one(self):
        return self.element_class(self, self._ring.one())

    def _repr_(self):
        return f"{self._ring}^× / ({self._ring}^×)^2"

    def _latex_(self):
        ring = latex(self._ring)
        return rf"{ring}^\times/({ring}^\times)^2"


def _square_class_group(ring):
    r"""Return \(R^\times/(R^\times)^2\) for the owned commutative ring ``ring``.

    The ring's ``square_class_group`` is the one entry; it retains the group.
    """
    assert ring in CommutativeRings(), (
        f"the square-class group R^×/(R^×)^2 is the quotient of R^× by the subgroup of "
        f"squares, which is a subgroup when R is commutative; {ring} is not known to be "
        f"a commutative ring"
    )
    return _object_of(
        AbelianGroups(),
        _engine=(OwnedGroups(), _SquareClassGroup, SquareClass),
        ring=ring,
    )


class SquareClassGroupFunctor(Functor):
    r"""\(R\mapsto R^\times/(R^\times)^2\) and \(\varphi\mapsto([u]\mapsto[\varphi(u)])\).

    A ring morphism sends a unit to a unit and a square to a square, so the
    induced map on classes is well defined, and it is multiplicative because
    \(\varphi\) is.  The images are abelian groups of exponent dividing two.
    """

    def __init__(self) -> None:
        super().__init__(CommutativeRings(), OwnedGroups())

    def _apply_object(self, ring):
        return ring.square_class_group()

    def _apply_morphism(self, morphism):
        source = self.object_image(morphism.domain())
        target = self.object_image(morphism.codomain())
        return SetMorphism(
            source.Mor(target),
            lambda square_class: target(morphism(square_class.representative())),
        )

    def _repr_(self):
        return "Square-class group functor CRing -> Grp"


__all__ = ["SquareClass", "SquareClassGroupFunctor"]
