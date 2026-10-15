r"""Filtered modules, mixed Hodge structures and pure Hodge structures.

The definitions are Deligne's (*Théorie de Hodge II*, Publ. Math. IHES 40
(1971)).  Let ``R`` be a subring of the real numbers such that ``R tensor QQ``
is a field (``ZZ``, ``QQ`` or ``RR``; Deligne II (2.3.1)).

- A *mixed Hodge structure* over ``R`` is a finitely generated ``R``-module
  ``V``, an increasing filtration ``W`` (the weight filtration) of
  ``V tensor_R QQ`` and a decreasing filtration ``F`` (the Hodge filtration)
  of ``V tensor_R CC``, such that ``F`` induces on each ``Gr^W_n tensor CC``
  a Hodge structure of weight ``n`` (II (2.3.1)).
- A *Hodge structure of weight* ``n`` is a mixed Hodge structure with
  ``Gr^W_m = 0`` for ``m != n``.  Equivalently ``V tensor CC`` is the direct
  sum of ``V^{p,q} = F^p cap conj(F^q)`` over ``p + q = n``, with
  ``conj(V^{p,q}) = V^{q,p}`` (II (2.1.1), (2.1.10)).
- A *polarization* of a Hodge structure of weight ``n`` is an ``R``-bilinear
  ``Q: V tensor V -> R(-n)`` that is ``(-1)^n``-symmetric and satisfies the
  Hodge–Riemann relations (II (2.1.15)).

Morphisms are ``R``-linear maps whose scalar extensions preserve ``W`` and
``F``; such morphisms are strictly compatible with both filtrations
(II (2.3.5)), which makes the categories abelian.
"""

from sage.categories.category import Category
from sage.categories.category_with_axiom import all_axioms

from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _owned_integers,
)
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom

# ``Polarizable`` is the property that a pure Hodge structure admits a
# polarization; the chosen polarization is the data of
# :class:`PolarizedHodgeStructures`.
if "Polarizable" not in all_axioms:
    all_axioms.add("Polarizable")


class FilteredModules(OwnedCategoryOverBaseRing):
    r"""Modules over ``R`` with a finite decreasing filtration by submodules.

    An object is ``(M, F^•)`` with ``F^p M`` a submodule of ``M``,
    ``F^{p+1} M subseteq F^p M``, ``F^p M = M`` for ``p << 0`` and
    ``F^p M = 0`` for ``p >> 0``.  An increasing filtration ``W_•`` is the
    decreasing filtration ``W^{-n} := W_n`` (Deligne II (1.1.2)).  A morphism
    is an ``R``-linear map ``f`` with ``f(F^p M) subseteq F^p N``.
    """

    def _repr_object_names(self) -> str:
        return f"filtered modules over {self.base()}"

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def filtration_stage(self, p):
            r"""The inclusion ``F^p M -> M``, an arrow of ``Modules(R)``."""
            assert False, "filtration_stage on FilteredModules(R): not implemented"

        def graded_piece(self, p):
            r"""``Gr_F^p M = F^p M / F^{p+1} M``, an object of ``Modules(R)``."""
            assert False, "graded_piece on FilteredModules(R): not implemented"


class MixedHodgeStructures(OwnedCategoryOverBaseRing):
    r"""Mixed Hodge structures over ``R`` (Deligne II (2.3.1)).

    The underlying ``R``-module ``V`` is finitely generated, so the
    supercategory is ``Modules(R).FinitelyGenerated()``.  The filtrations live
    on ``V tensor QQ`` and ``V tensor CC``, not on ``V``, so
    :class:`FilteredModules` is not a supercategory; each filtration is a
    value in ``FilteredModules`` of the extended base.
    """

    def _repr_object_names(self) -> str:
        return f"mixed Hodge structures over {self.base()}"

    def super_categories(self):
        return [Modules(self.base_ring()).FinitelyGenerated()]

    def _call_(self, module, weight_filtration, hodge_filtration):
        r"""The mixed Hodge structure ``(V, W, F)``.

        ``weight_filtration`` is an object of ``FilteredModules(R tensor QQ)``
        on ``V tensor QQ`` in the reindexed form ``W^{-n} = W_n``;
        ``hodge_filtration`` is an object of ``FilteredModules(CC)`` on
        ``V tensor CC``.
        """
        assert False, "construction on MixedHodgeStructures(R): not implemented"

    def weight_graded_functor(self, weight):
        r"""``Gr^W_n: MixedHodgeStructures(R) -> HodgeStructures(R, n)``.

        Exact, since morphisms are strictly compatible with ``W``
        (Deligne II (2.3.5)).
        """
        assert False, "weight_graded_functor on MixedHodgeStructures(R): not implemented"

    class ParentMethods:
        def weight_filtration(self):
            r"""``W`` on ``V tensor QQ``, an object of ``FilteredModules(R tensor QQ)``."""
            assert False, "weight_filtration on MixedHodgeStructures(R): not implemented"

        def hodge_filtration(self):
            r"""``F`` on ``V tensor CC``, an object of ``FilteredModules(CC)``."""
            assert False, "hodge_filtration on MixedHodgeStructures(R): not implemented"

        def weight_graded_piece(self, weight):
            r"""``Gr^W_n V``, an object of ``HodgeStructures(R, n)``."""
            assert False, "weight_graded_piece on MixedHodgeStructures(R): not implemented"

        def hodge_number(self, p, q):
            r"""``h^{p,q} = dim_CC Gr_F^p Gr^W_{p+q} (V tensor CC)``, a natural number."""
            assert False, "hodge_number on MixedHodgeStructures(R): not implemented"


class HodgeStructures(OwnedCategoryOverBaseRing):
    r"""Hodge structures of weight ``n`` over ``R`` (Deligne II (2.1.1)).

    The full subcategory of ``MixedHodgeStructures(R)`` with ``Gr^W_m = 0`` for
    ``m != n``.  The condition depends on the integer ``n``, so it is a
    parameter of the category and not a parameterless axiom.
    """

    @staticmethod
    def __classcall__(cls, base_ring, weight):
        return OwnedCategoryOverBaseRing.__classcall__(
            cls, base_ring, _owned_integers()(weight)
        )

    def __init__(self, base_ring, weight) -> None:
        self._weight = weight
        super().__init__(base_ring)

    def weight(self):
        r"""The weight ``n``, an element of ``ZZ``."""
        return self._weight

    def _repr_object_names(self) -> str:
        return f"Hodge structures of weight {self.weight()} over {self.base()}"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self.weight())

    def super_categories(self):
        return [MixedHodgeStructures(self.base_ring())]

    class SubcategoryMethods:
        def Polarizable(self) -> Category:
            r"""Hodge structures that admit a polarization (Deligne II (2.1.15))."""
            return self._with_axiom("Polarizable")

    class ParentMethods:
        def hodge_decomposition(self):
            r"""``V tensor CC = ⊕_{p+q=n} V^{p,q}``, an object of ``GradedModules(CC, ZZ)``.

            The piece of degree ``p`` is ``V^{p,n-p} = F^p cap conj(F^{n-p})``.
            """
            assert False, "hodge_decomposition on HodgeStructures(R, n): not implemented"

        def weil_operator(self):
            r"""``C`` acting by ``i^{p-q}`` on ``V^{p,q}``, an endomorphism of ``V tensor RR``."""
            assert False, "weil_operator on HodgeStructures(R, n): not implemented"

    class Polarizable(CategoryWithAxiom):
        r"""Polarizable Hodge structures of weight ``n``.

        Full: a morphism of Hodge structures between polarizable ones is a
        morphism here; a chosen polarization is the data of
        :class:`PolarizedHodgeStructures`.
        """


HodgeStructures.__dict__["Polarizable"]._base_category_class_and_axiom = (
    HodgeStructures,
    "Polarizable",
)


class PolarizedHodgeStructures(OwnedCategoryOverBaseRing):
    r"""Hodge structures of weight ``n`` with a chosen polarization.

    An object is ``(V, Q)`` with ``Q: V tensor V -> R(-n)`` ``(-1)^n``-symmetric,
    ``Q(V^{p,q}, V^{p',q'}) = 0`` unless ``p = q'``, and
    ``Q(Cx, conj(x)) > 0`` for ``x != 0`` (Deligne II (2.1.15)).  A morphism
    preserves ``Q``, so this data subcategory is not full.
    """

    @staticmethod
    def __classcall__(cls, base_ring, weight):
        return OwnedCategoryOverBaseRing.__classcall__(
            cls, base_ring, _owned_integers()(weight)
        )

    def __init__(self, base_ring, weight) -> None:
        self._weight = weight
        super().__init__(base_ring)

    def weight(self):
        r"""The weight ``n``, an element of ``ZZ``."""
        return self._weight

    def _repr_object_names(self) -> str:
        return f"polarized Hodge structures of weight {self.weight()} over {self.base()}"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self.weight())

    def super_categories(self):
        return [HodgeStructures(self.base_ring(), self.weight()).Polarizable()]

    class ParentMethods:
        def polarization(self):
            r"""The chosen ``Q: V tensor V -> R(-n)``, an arrow of ``Modules(R)``."""
            assert False, "polarization on PolarizedHodgeStructures(R, n): not implemented"
