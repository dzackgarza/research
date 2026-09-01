r"""Realized elements of (G_K=\operatorname{Aut}_K(\bar K))."""

from typing import TYPE_CHECKING, cast

from sage.categories.morphism import Morphism
from sage.rings.integer_ring import ZZ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.group.profinite.field_morphisms import (
    ExactFieldMorphism,
    field_generators,
)

if TYPE_CHECKING:
    from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
        AbsoluteGaloisGroup,
    )


class AbsoluteGaloisGroupElement(Morphism):
    r"""A coherent, progressively realized automorphism of the chosen closure.

    A global exact map may be supplied directly.  A lift from a finite
    quotient instead starts with one exact finite coordinate; additional
    coordinates can be installed only after their compatibility is checked.
    """

    def __init__(
        self,
        parent,
        *,
        exact_action: ExactFieldMorphism | None = None,
        coordinates=(),
        frobenius_exponent=None,
    ) -> None:
        Morphism.__init__(self, parent)
        self._exact_action = exact_action
        self._coordinates = list(coordinates)
        self._frobenius_exponent = (
            None if frobenius_exponent is None else ZZ(frobenius_exponent)
        )
        if self._exact_action is None and self._frobenius_exponent is None:
            raise TypeError(
                "an absolute Galois element requires a globally exact action"
            )

    def as_morphism(self):
        return self

    def exact_action(self):
        return self._exact_action

    def realized_stages(self) -> tuple:
        return tuple(stage for stage, _coordinate in self._coordinates)

    def restriction_coordinate(self, stage):
        for known_stage, coordinate in self._coordinates:
            if known_stage is stage:
                return coordinate
            if (
                known_stage.field() is stage.field()
                and known_stage.embedding() == stage.embedding()
            ):
                return coordinate
        return None

    def extend_coordinate(self, restriction_map, coordinate) -> None:
        r"""Install a higher finite coordinate after checking compatibility."""
        stage = restriction_map.extension()
        coordinate = restriction_map.codomain()(coordinate)
        for old_stage, old_coordinate in self._coordinates:
            if old_stage is stage:
                if old_coordinate != coordinate:
                    raise ValueError(
                        "the new coordinate contradicts the realized coordinate"
                    )
                return
        if restriction_map(self) != coordinate:
            raise ValueError("the new coordinate contradicts the global automorphism")
        self._coordinates.append((stage, coordinate))

    def frobenius_exponent(self):
        return self._frobenius_exponent

    def is_globally_evaluable(self) -> bool:
        return self._frobenius_exponent is not None or self._exact_action is not None

    def __call__(self, element):
        r"""Evaluate without forcing a finite-stage element through the closure facade."""
        return self._call_(element)

    def _call_(self, element):
        if self._frobenius_exponent is not None:
            return self.parent()._finite_frobenius_image(
                element, self._frobenius_exponent
            )
        if self._exact_action is not None:
            return self._exact_action(element)
        raise NotImplementedError("this automorphism has no global exact action")

    def fixes_base_field(self) -> bool:
        parent = cast("AbsoluteGaloisGroup", self.parent())
        embedding = parent.base_embedding()
        try:
            return all(
                self(embedding(generator)) == embedding(generator)
                for generator in field_generators(parent.base_field())
            )
        except NotImplementedError:
            return False

    def restrict(self, stage):
        return self.parent().restriction_map(stage)(self)

    def __mul__(self, other):
        if isinstance(other, AbsoluteGaloisGroupElement):
            if other.parent() is not self.parent():
                return NotImplemented
            return self.parent()._compose_elements(self, other)
        return Morphism.__mul__(self, other)

    def __invert__(self):
        return self.inverse()

    def inverse(self):
        return self.parent()._inverse_element(self)

    def __pow__(self, exponent):
        exponent = ZZ(exponent)
        if self._frobenius_exponent is not None:
            return FrobeniusElement(self.parent(), exponent * self._frobenius_exponent)
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = self.parent().one()
        factor = self
        while exponent:
            if exponent & 1:
                result = result * factor
            factor = factor * factor
            exponent >>= 1
        return result

    def conjugacy_class(self):
        return ElementConjugacyClass(self.parent(), self)

    def __eq__(self, other) -> bool:
        if (
            not isinstance(other, AbsoluteGaloisGroupElement)
            or other.parent() is not self.parent()
        ):
            return False
        if (
            self._frobenius_exponent is not None
            or other._frobenius_exponent is not None
        ):
            return self._frobenius_exponent == other._frobenius_exponent
        if self._exact_action is not None and other._exact_action is not None:
            return self._exact_action == other._exact_action
        return False

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        datum: tuple[object, ...]
        if self._frobenius_exponent is not None:
            datum = ("frobenius", self._frobenius_exponent)
        elif self._exact_action is not None:
            datum = ("exact", self._exact_action)
        else:
            datum = ("unrealized",)
        return hash((id(self.parent()), datum))

    def _repr_(self) -> str:
        if self._frobenius_exponent is not None:
            parent = cast("AbsoluteGaloisGroup", self.parent())
            q = parent.base_field_order()
            return f"q-Frobenius^{self._frobenius_exponent} (q={q})"
        if self._exact_action is not None:
            return f"Element of {self.parent()} represented by {self._exact_action}"
        fields = ", ".join(str(stage.field()) for stage, _ in self._coordinates)
        return f"Element of {self.parent()} realized on {fields}"


class FrobeniusElement(AbsoluteGaloisGroupElement):
    r"""An integral power of the canonical (q)-Frobenius."""

    def __init__(self, parent, exponent=1) -> None:
        super().__init__(parent, frobenius_exponent=ZZ(exponent))


class ElementConjugacyClass(SageObject):
    r"""The conjugacy class of a represented global automorphism."""

    def __init__(self, ambient, representative) -> None:
        self._ambient = ambient
        self._representative = representative

    def ambient(self):
        return self._ambient

    def representative(self):
        return self._representative

    def __contains__(self, element) -> bool:
        if self._ambient.is_abelian() is not True:
            raise NotImplementedError(
                "conjugacy membership is not decided for this absolute Galois group"
            )
        if element not in self._ambient:
            return False
        return element == self._representative

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if not isinstance(other, ElementConjugacyClass):
            return False
        if other._ambient is not self._ambient:
            return False
        if self._ambient.is_abelian() is not True:
            raise NotImplementedError(
                "conjugacy-class equality is not decided for this absolute Galois group"
            )
        return other._representative == self._representative

    def __hash__(self) -> int:
        if self._ambient.is_abelian() is not True:
            raise TypeError(
                "undecided absolute-Galois conjugacy classes are not hashable"
            )
        return hash((id(self._ambient), self._representative))

    def _repr_(self) -> str:
        return f"Conjugacy class of {self._representative} in {self._ambient}"


__all__ = [
    "AbsoluteGaloisGroupElement",
    "ElementConjugacyClass",
    "FrobeniusElement",
]
