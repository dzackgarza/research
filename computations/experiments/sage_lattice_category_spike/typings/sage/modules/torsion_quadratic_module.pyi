# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Iterable

from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.groups.fqf_orthogonal import FqfOrthogonalGroup
from sage.modules.fg_pid.fgp_element import FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module import FreeModule_generic
from sage.quadratic_forms.genera.genus import GenusSymbol_global_ring
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import Element, Matrix

class TorsionQuadraticModule(FGP_Module_class):
    # The two moduli are the value modules the form takes values in: b lands
    # in QQ/(modulus)ZZ and q in QQ/(modulus_qf)ZZ. Sage keeps them private,
    # so a reach for them is a private-usage finding by design
    # (pyrightconfig.json reportPrivateUsage), not an untyped hole.
    _modulus: Rational
    _modulus_qf: Rational
    def __init__(
        self,
        V: FreeModule_generic,
        W: FreeModule_generic,
        gens: Iterable[FGP_Element] | None = ...,
        modulus: Rational | Integer | None = ...,
        modulus_qf: Rational | Integer | None = ...,
        check: bool = ...,
    ) -> None: ...
    def gram_matrix_quadratic(self) -> Matrix: ...
    def gram_matrix_bilinear(self) -> Matrix: ...
    def value_module(self) -> QmodnZ: ...
    def value_module_qf(self) -> QmodnZ: ...
    def normal_form(self, partial: bool = ...) -> TorsionQuadraticModule: ...
    def brown_invariant(self) -> Integer: ...
    def genus(self, signature_pair: tuple[int, int]) -> GenusSymbol_global_ring: ...
    # Whether some lattice of this signature has this discriminant form. The
    # pair is the lexicon's SignaturePair, whose entries are Integer.
    def is_genus(
        self,
        signature_pair: tuple[int | Integer, int | Integer],
        even: bool = ...,
    ) -> bool: ...
    def twist(self, s: object) -> TorsionQuadraticModule: ...
    def primary_part(self, p: object) -> TorsionQuadraticModule: ...
    def orthogonal_group(
        self,
        gens: Iterable[Matrix] | None = ...,
        check: bool = ...,
    ) -> FqfOrthogonalGroup: ...
    # The complement of a submodule, or of a family of its elements.
    def orthogonal_submodule_to(
        self,
        S: Iterable[Element] | TorsionQuadraticModule,
    ) -> TorsionQuadraticModule: ...
    def submodule_with_gens(self, gens: Iterable[FGP_Element]) -> TorsionQuadraticModule: ...
    def all_submodules(self) -> list[TorsionQuadraticModule]: ...

def TorsionQuadraticForm(q: Matrix) -> TorsionQuadraticModule: ...
def _brown_indecomposable(q: Matrix, p: Integer) -> Integer: ...
