"""Dependency-light runtime foundation for owned Hom-set parents."""

from sage.categories.homset import Homset


class OwnedHomset(Homset):
    r"""A Hom-set whose elements enter through its owned constructor directly.

    Sage's ``Homset`` remains the runtime parent required by ``Morphism``.
    Mathematical inputs are not sent through Sage coercion discovery: each
    concrete Hom-set owns the interpretation implemented by
    ``_element_constructor_``.
    """

    def __call__(self, *args, **kwargs):
        return self._element_constructor_(*args, **kwargs)

    def identity_at(self, obj):
        if obj is not self.domain() or obj is not self.codomain():
            raise ValueError("this Hom parent does not represent endomorphisms of the stated object")
        return self.identity()

    def morphisms_agree(self, left, right) -> bool:
        r"""Decide equality by the Hom parent's represented equality law."""
        if left.parent() is not self or right.parent() is not self:
            return False
        if left is right:
            return True
        try:
            return bool(left == right)
        except NotImplementedError as error:
            raise NotImplementedError(
                f"equality in {self} has no represented decision procedure"
            ) from error


__all__ = ["OwnedHomset"]
