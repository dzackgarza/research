# Normative spec checks for category refinement gaps.
#
# These assertions intentionally encode current failures of the wrapped Sage
# implementations against the local module-category spec in
# category_specs/modules/__init__.py and modules/subcategories/.

import logging
import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parents[4]))

from category_specs.modules import Modules
from category_specs.rings import Rings

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

QQ = Rings().Constructors().QQ()
MQQ = Modules(QQ).Constructors()

# ---------------------------------------------------------------------------
# QuotientModuleWithBasis should refine to quotient / generating-set surfaces
# ---------------------------------------------------------------------------

X = MQQ.CombinatorialFreeModule(range(3), prefix='x')
x = X.basis()
Y = MQQ.quotient_module(
    X,
    X.submodule([x[0] - x[1], x[1] - x[2]], already_echelonized=True),
    already_echelonized=True,
)

logger.warning(
    "Spec mismatch: modules-with-basis quotients should lie in Modules(QQ).Quotients(), "
    "but the wrapped Sage quotient currently does not refine into that subcategory."
)
assert Y in Modules(QQ).Quotients()

logger.warning(
    "Spec mismatch: quotient refinement should compose under axiom chaining, so a modules-with-basis "
    "quotient should lie in Modules(QQ).Quotients().WithOrderedGeneratingSet(), but the current "
    "wrapped Sage quotient does not."
)
assert Y in Modules(QQ).Quotients().WithOrderedGeneratingSet()
