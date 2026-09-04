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


__all__ = ["OwnedHomset"]
