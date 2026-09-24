"""Mathematical nouns for category-theoretic dependent types."""

from typing import Any


# An object of a mathematically specified category C.  The category is often a
# runtime parameter (for example the codomain D of a functor F : C -> D), so
# Python cannot currently express the dependent type C.ObjectType here.
type ObjectOfCategory = Any


__all__ = ["ObjectOfCategory"]
