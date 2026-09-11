r"""Archive reconciliation for technical Sage-interoperation vocabulary.

This archive module was declaration-only.  The live module keeps the same
Sage implementation classes and the same two union aliases; the test records
the runtime class identities, while the inventory metadata records the whole
declaration surface.
"""

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.combinat.root_system.cartan_matrix import CartanMatrix
from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.groups.matrix_gps.isometries import GroupOfIsometries
from sage.modules.free_quadratic_module_integer_symmetric import (
    FreeQuadraticModule_integer_symmetric,
)
from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
from sage.quadratic_forms.genera.genus import (
    Genus_Symbol_p_adic_ring,
    GenusSymbol_global_ring,
)
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from dzack_research.preamble.lexicon.interop import (
    SageCartanMatrix,
    SageCategory,
    SageDiscriminantForm,
    SageElement,
    SageGenus,
    SageIsometryGroup,
    SageLattice,
    SageLocalGenusSymbol,
    SageMorphism,
    SageParent,
    SageQmodnZ,
    SageQuadraticForm,
    SageUniqueRepresentation,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/lexicon/interop.py",
    "live_owner": "src/dzack_research/preamble/lexicon/interop.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_sage_interop_nouns_keep_exact_runtime_classes() -> None:
    assert SageCartanMatrix is CartanMatrix
    assert SageCategory is Category
    assert SageDiscriminantForm is TorsionQuadraticModule
    assert SageElement is Element
    assert SageGenus is GenusSymbol_global_ring
    assert SageIsometryGroup is GroupOfIsometries
    assert SageLattice is FreeQuadraticModule_integer_symmetric
    assert SageLocalGenusSymbol is Genus_Symbol_p_adic_ring
    assert SageMorphism is Morphism
    assert SageParent is Parent
    assert SageQmodnZ is QmodnZ
    assert SageQuadraticForm is QuadraticForm
    assert SageUniqueRepresentation is UniqueRepresentation
