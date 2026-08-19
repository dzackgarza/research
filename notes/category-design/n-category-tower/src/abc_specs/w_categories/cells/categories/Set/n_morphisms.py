# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cells/categories/Set/n_morphisms.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.


from src.local_typing import *
from src._types import *

# Elements

class _SetElement_ABC(ABC): ...

# Objects
class _Set_As_ZeroMorphism_ABC(ABC): ...

# Plain Morphisms
class _SetMorphism_As_ZeroMorphism_ABC(ABC): ...

class _SetMorphism_As_OneMorphism_ABC(ABC): 
    def apply_to_element(self, element: Any) -> Any: ...

# Endomorphisms

class _SetEndoMorphism_As_ZeroMorphism_ABC(ABC): ...

class _SetEndoMorphism_As_OneMorphism_ABC(ABC): ...

# Automorphisms

class _SetAutoMorphism_As_ZeroMorphism_ABC(ABC): ...

class _SetAutoMorphism_As_OneMorphism_ABC(ABC): ...

class SetObject:
    mn1 = _SetElement_ABC
    m0 = _Set_As_ZeroMorphism_ABC
    m1 = None
    m2 = None

class SetMorphism:
    mn1 = None # Morphisms have no elements.
    # 0-cells
    m0 = _SetMorphism_As_ZeroMorphism_ABC
    m0_endo = _SetMorphism_As_ZeroMorphism_ABC
    m0_auto = _SetMorphism_As_ZeroMorphism_ABC
    # 1-cells
    m1 = _SetMorphism_As_OneMorphism_ABC
    m1_endo = _SetMorphism_As_OneMorphism_ABC
    m1_auto = _SetMorphism_As_OneMorphism_ABC
    # 2-cells
    m2 = None
    m2_endo = None
    m2_auto = None

