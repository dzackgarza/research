# Normative spec checks for method-surface gaps.
#
# These assertions intentionally record where existing Sage-backed objects do
# not satisfy the ABC surface declared in plans/category_specs/modules/__init__.py
# and modules/subcategories/.

import logging
import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parents[4]))

from category_specs.modules import Modules
from category_specs.rings import Rings

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

ZZ = Rings().Constructors().ZZ()
MZZ = Modules(ZZ).Constructors()

# ---------------------------------------------------------------------------
# FGP quotient modules: required surface in FinitelyPresentedModulesOverPID
# ---------------------------------------------------------------------------

V = MZZ.span([[1, 2, 5], [2, 2, 2]])
W = V.span([V.gen(0)])
Q = MZZ.quotient_of_free_modules(V, W)

logger.warning(
    "Spec mismatch: FinitelyPresentedModulesOverPID requires free_part(), "
    "but the current Sage FGP quotient object still raises NotImplementedError."
)
Q.free_part()

logger.warning(
    "Spec mismatch: FinitelyPresentedModulesOverPID requires torsion_part(), "
    "but the current Sage FGP quotient object still raises NotImplementedError."
)
Q.torsion_part()

logger.warning(
    "Spec mismatch: FinitelyPresentedModulesOverPID requires element_from_vector(...), "
    "but the current Sage FGP quotient object still raises NotImplementedError."
)
Q.element_from_vector([0])

logger.warning(
    "Spec mismatch: FinitelyPresentedModulesOverPID types optimized() as an R-module object, "
    "but the current Sage FGP quotient object returns a plain tuple."
)
assert Q.optimized() in Modules(ZZ)

# ---------------------------------------------------------------------------
# Ring objects as modules: required surface in _RingObjectsAsModules
# ---------------------------------------------------------------------------

S = MZZ.polynomial_ring_as_module(name='x')

logger.warning(
    "Spec mismatch: _RingObjectsAsModules requires module_generators(), "
    "but the wrapped Sage polynomial ring still raises NotImplementedError."
)
S.module_generators()
