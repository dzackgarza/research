r"""Archive reconciliation for general algebra vocabulary.

The archive module was declaration-only.  The live lexicon keeps the same
Sage implementation classes and the same ``BaseRing = Ring`` semantic alias,
while centralizing their public import surface through ``preamble.lexicon``.
"""

from sage.rings.ring import Ring
from sage.structure.element import Element, Matrix, ModuleElement, RingElement

from dzack_research.preamble.lexicon import (
    BaseRing,
)
from dzack_research.preamble.lexicon import (
    Element as PublicElement,
)
from dzack_research.preamble.lexicon import (
    Matrix as PublicMatrix,
)
from dzack_research.preamble.lexicon import (
    ModuleElement as PublicModuleElement,
)
from dzack_research.preamble.lexicon import (
    RingElement as PublicRingElement,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/lexicon/algebra.py",
    "live_owner": "src/dzack_research/preamble/lexicon/__init__.py",
    "owner_overrides": {
        "BaseRing": "src/dzack_research/preamble/lexicon/algebra.py",
        "Element": "src/dzack_research/preamble/lexicon/__init__.py",
        "Matrix": "src/dzack_research/preamble/lexicon/__init__.py",
        "ModuleElement": "src/dzack_research/preamble/lexicon/__init__.py",
        "RingElement": "src/dzack_research/preamble/lexicon/__init__.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_archived_algebra_nouns_are_the_live_semantic_classes() -> None:
    assert BaseRing is Ring
    assert PublicElement is Element
    assert PublicMatrix is Matrix
    assert PublicModuleElement is ModuleElement
    assert PublicRingElement is RingElement
