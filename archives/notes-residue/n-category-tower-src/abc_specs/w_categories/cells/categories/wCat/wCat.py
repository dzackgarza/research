# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cells/categories/wCat/wCat.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.


from __future__ import annotations
from src.local_typing import *
from src._types import *

from .n_morphisms.category import Category

# src/abc_specs/w_categories/cells/categories/wCat/n_morphisms/w_category.py
from src.abc_specs.w_categories.cells.categories.wCat.n_morphisms.category import Morphism_Collection

class UnrulyCategory:
    objects: type[Any]

class InitialCategory(UnrulyCategory): ...
class TerminalCategory(UnrulyCategory): ...

@dataclass
class RulyCategory(UnrulyCategory):
    elements: type[Any] | None
    objects: type[Any]
    hom_category_class: type[Hom_C_xy_Category]
    """
    Derived notions:
    - C.one_morphisms() = hom_category_class.zero_morphisms()
    - C.two_morphisms() = hom_category_class.().hom_category_class()
    - C.n_morphisms(n) = C.n_morphisms(n-1).hom_category_class()
    """
    
class Hom_C_xy_Category(UnrulyCategory): 
    elements = None
    objects: type[Any] # Morphisms in C
    endomorphism_mixin: type[Any] # Endomorphisms in C
    automorphism_mixin: type[Any] # Automorphisms in C
    hom_category_class: type[Hom_C_xy_Category | InitialCategory | TerminalCategory]

class wCat_Morphism_Collection(Morphism_Collection):
    from .n_morphisms.functor import Functor
    from .n_morphisms.natural_transformation import NaturalTransformation
    from .hom_categories.hom_wcat import Fun, Fun_xy
    from .hom_categories.end_wcat import EndoFun, EndoFun_x
    from .hom_categories.aut_wcat import AutoFun, AutoFun_x

    # (-1)-Morphisms
    mn1 = None

    # 0-Morphisms: Categories

    class m0(Category.m0): 
        @override
        def amb(self) -> wCat: ...

    m0_endo = None
    m0_auto = None

    m1 = Functor.m1
    m1_endo = Functor.m1_endo
    m1_auto = Functor.m1_auto

    m2 = NaturalTransformation.m2
    m2_endo = NaturalTransformation.m2_endo
    m2_auto = NaturalTransformation.m2_auto

    hom_c = Fun
    hom_c_xy = Fun_xy

    end_c = EndoFun
    end_c_x = EndoFun_x

    aut_c = AutoFun
    aut_c_x = AutoFun_x

class wCat(Category.m0):

    @override
    @abstractmethod
    @final
    def amb(self) -> None:  # type: ignore[todo-fix-later]
        return None

    @override
    @abstractmethod
    @final
    def _n_morphism_classes(self) -> type[wCat_Morphism_Collection]: ...



wCategory = wCat_Morphism_Collection.m0

wFunctor = wCat_Morphism_Collection.m1
wEndoFunctor = wCat_Morphism_Collection.m1_endo
wAutoFunctor = wCat_Morphism_Collection.m1_auto

wNaturalTransformation = wCat_Morphism_Collection.m2
wEndoNaturalTransformation = wCat_Morphism_Collection.m2_endo
wAutoNaturalTransformation = wCat_Morphism_Collection.m2_auto

wFun = wCat_Morphism_Collection.hom_c
wFun_xy = wCat_Morphism_Collection.hom_c_xy

wEndoFun = wCat_Morphism_Collection.end_c
wEndoFun_x = wCat_Morphism_Collection.end_c_x

wAutoFun = wCat_Morphism_Collection.aut_c
wAutoFun_x = wCat_Morphism_Collection.aut_c_x