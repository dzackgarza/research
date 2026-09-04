r"""``A.Mor(B)`` is one interned category, at every level of the graph.

`ARC-07` says a category and a pair of endpoints determine exactly one Hom
object, and that object is a category.  Formed modules violated both halves:
``A.Mor(A)`` built a fresh Hom on every call and returned a different class
from ``FormModules(R).Mor(A, A)``, so a composite and an identity never shared
a parent and no isometry could be verified.  Schemes returned Sage's own Homset,
which is not a category at all.

Each specimen below is small enough to check by hand, and the claim is the same
for all of them.
"""

import pytest

from dzack_research.preamble.all import (
    AffineSpace,
    FreeModule,
    Lattices,
    QQ,
    Sets,
    ZZ,
)
from dzack_research.preamble.categories.abstract_categories.cat import Cat


def _specimens():
    r"""Return one small object from each level that owns a ``Mor``."""
    return {
        "a finite ordinal": Sets.Δ[2],
        "the integers": ZZ,
        "a free module": FreeModule(ZZ, 2),
        "the hyperbolic plane": Lattices(ZZ)("U"),
        "a discriminant form": Lattices(ZZ)("A2").discriminant_bilinear_form(),
        "an affine plane": AffineSpace(2, QQ),
        "a polynomial algebra": QQ["x"],
    }


# The specimen names, in the order the dict declares them; pytest iterates any
# iterable, so no Python container has to be built to parametrize over them.
_SPECIMEN_NAMES = _specimens()


@pytest.mark.parametrize("description", _SPECIMEN_NAMES)
def test_an_objects_mor_is_a_category(description) -> None:
    obj = _specimens()[description]

    assert obj.Mor(obj) in Cat()


@pytest.mark.parametrize("description", _SPECIMEN_NAMES)
def test_an_objects_mor_is_interned(description) -> None:
    obj = _specimens()[description]

    assert obj.Mor(obj) is obj.Mor(obj)


@pytest.mark.parametrize("description", _SPECIMEN_NAMES)
def test_the_identity_belongs_to_that_one_mor(description) -> None:
    obj = _specimens()[description]
    endomorphisms = obj.Mor(obj)

    assert endomorphisms.identity().parent() is endomorphisms


@pytest.mark.parametrize("description", _SPECIMEN_NAMES)
def test_the_identity_is_a_two_sided_unit_its_own_hom_can_confirm(description) -> None:
    r"""``id . id = id``.

    Morphism equality is undecidable in general, so a Hom whose composition
    builds a fresh morphism each time cannot confirm its own unit law.  That is
    not a weaker test: it is what made every formed-module isometry fail.
    """
    obj = _specimens()[description]
    endomorphisms = obj.Mor(obj)
    identity = endomorphisms.identity()
    composite = identity * identity

    assert composite.parent() is endomorphisms
    assert composite == identity
