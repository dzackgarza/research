# Repo-scoped stubs; see lexicon/README.md.
from sage.groups.additive_abelian.qmodnz_element import QmodnZ_Element
from sage.rings.rational import Rational
from sage.structure.parent import Parent

class QmodnZ(Parent):
    n: Rational
    def __init__(self, n: object = ...) -> None: ...
    def __call__(self, x: object) -> QmodnZ_Element: ...
    def zero(self) -> QmodnZ_Element: ...
