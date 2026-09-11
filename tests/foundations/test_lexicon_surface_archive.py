r"""Archive reconciliation for the aggregate mathematical lexicon surface.

The archived module was deliberately only a re-export boundary: each noun had
one defining lexicon module and the aggregate imported it unchanged.  The live
surface preserves those object identities and adds ``MatrixData`` without
changing any archived noun.
"""

import dzack_research.preamble.lexicon as lexicon
from dzack_research.preamble.lexicon import algebra, foundations, geometry, interop

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/lexicon/__init__.py",
        "live_owner": "src/dzack_research/preamble/lexicon/__init__.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/lexicon/foundations.py",
        "live_owner": "src/dzack_research/preamble/lexicon/foundations.py",
        "owner_overrides": {
            "RealApproximation": "src/dzack_research/preamble/rings/real.py",
            "RealNumber": "src/dzack_research/preamble/rings/real.py",
        },
        "disposition": "reconciled-live-owner",
    },
)


def test_archived_lexicon_nouns_are_the_defining_module_objects() -> None:
    defining = {
        "BaseRing": algebra.BaseRing,
        "Element": algebra.Element,
        "Matrix": algebra.Matrix,
        "ModuleElement": algebra.ModuleElement,
        "RingElement": algebra.RingElement,
        "CartanType": foundations.CartanType,
        "GramMatrix": foundations.GramMatrix,
        "Integer": foundations.Integer,
        "LatticeName": foundations.LatticeName,
        "OrderedSet": foundations.OrderedSet,
        "Rational": foundations.Rational,
        "RealApproximation": foundations.RealApproximation,
        "RealNumber": foundations.RealNumber,
        "SignaturePair": foundations.SignaturePair,
        "SymbolicExpression": foundations.SymbolicExpression,
        "CoxeterMatrix": geometry.CoxeterMatrix,
        "Graph": geometry.Graph,
        "Polyhedron": geometry.Polyhedron,
        "SageCategory": interop.SageCategory,
        "SageElement": interop.SageElement,
        "SageMorphism": interop.SageMorphism,
        "SageParent": interop.SageParent,
        "SageUniqueRepresentation": interop.SageUniqueRepresentation,
    }

    for name, defining_object in defining.items():
        assert getattr(lexicon, name) is defining_object
        assert name in lexicon.__all__


def test_live_lexicon_extension_does_not_replace_the_archived_surface() -> None:
    assert lexicon.MatrixData is foundations.MatrixData
    assert "MatrixData" in lexicon.__all__
