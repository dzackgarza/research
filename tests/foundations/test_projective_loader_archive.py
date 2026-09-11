r"""Retire the archived projective-framework notebook loader.

The archived framework package executed ``Projective_Scheme_Framework.ipynb``
into a mutable namespace before its scenarios ran.  The framework mathematics
is now implemented by ordinary preamble modules and exported from the closed
session surface, so no notebook execution or cached notebook namespace is part
of the live contract.
"""

from dzack_research.preamble.all import (
    ADELogPair,
    CompleteLinearSystems,
    CyclicCoverAlgebra,
    ProductProjectiveSpaces,
    ProjectiveSpaces,
)


ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/tests/framework/__init__.py",
        "live_owner": "src/dzack_research/preamble/all.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/framework/projective_framework_loader.py",
        "live_owner": "src/dzack_research/preamble/all.py",
        "disposition": "reconciled-live-owner",
    },
)


def test_projective_framework_constructions_are_direct_public_imports() -> None:
    for constructor in (
        ProjectiveSpaces,
        ProductProjectiveSpaces,
        CompleteLinearSystems,
        CyclicCoverAlgebra,
        ADELogPair,
    ):
        assert callable(constructor)
