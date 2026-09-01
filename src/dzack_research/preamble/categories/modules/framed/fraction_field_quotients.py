r"""Fraction-field quotients ``K / a`` as modules over the base ring."""

from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.sets.non_negative_integers import NonNegativeIntegers

from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
    owned_ring_view,
)
from dzack_research.preamble.refine import hook_post_init, refine


class FractionFieldQuotients(OwnedCategoryOverBaseRing):
    r"""Modules ``Frac(R) / a`` for a fractional ideal ``a`` of ``R``.

    The active computation adapter currently specializes this construction to
    ``R = ZZ``, where Sage's :class:`QmodnZ` implements ``QQ / n ZZ``.
    """

    @classmethod
    def _repr_object_names(cls):
        return "fraction-field quotients"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.framed.framed_modules import (
            FramedModules,
        )

        return [FramedModules(self.base_ring())]

    class ParentMethods:
        def base_ring(self):
            return owned_ring_view(self.base())

        def fraction_field(self):
            return self.base_ring().fraction_field()

        def modulus(self):
            r"""Return a generator of the fractional ideal being quotiented out."""
            return self._fraction_field_modulus

        def lift(self, element):
            r"""Return a representative of ``element`` in the fraction field."""
            if element.parent() is not self:
                raise ValueError(f"{element} is not an element of {self}")
            return self.fraction_field()(element.lift())

        def divisibility_chain(self, index):
            r"""Return the chosen cofinal divisibility chain element ``d_index``."""
            if engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError(
                    "the active divisibility chain is the factorial chain over ZZ"
                )
            return SageZZ(index + 1).factorial()

        @cached_method
        def module_generating_set(self):
            return NonNegativeIntegers()

        def module_generator(self, label):
            labels = self.module_generating_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not a module-generator label")
            denominator = self.divisibility_chain(label)
            return self(SageQQ.one() / denominator)

        def framing_morphism(self):
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                FreeModuleOn,
            )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                framing_morphism,
            )

            source = FreeModuleOn(self.base_ring(), self.module_generating_set())
            return framing_morphism(source, self, self.module_generator)

        def projection_from_fraction_field(self):
            r"""Return the native quotient map ``Frac(R) -> Frac(R) / a``."""
            return self.coerce_map_from(engine_ring(self.fraction_field()))


def refine_fraction_field_quotient(quotient):
    r"""Adopt a native ``QQ / n ZZ`` parent into the owned module hierarchy."""
    if not isinstance(quotient, QmodnZ):
        raise TypeError("the active fraction-field quotient adapter expects Sage QmodnZ")
    quotient._fraction_field_modulus = quotient.n
    base_ring = owned_ring_view(SageZZ)
    categories = [FractionFieldQuotients(base_ring)]
    if not quotient.n.is_zero():
        from dzack_research.preamble.categories.modules.pure.torsion_modules import (
            TorsionModules,
        )

        categories.append(TorsionModules(base_ring))
    return refine(quotient, categories)


def FractionFieldQuotient(base_ring, modulus=1):
    r"""Return ``Frac(base_ring) / modulus*base_ring`` when natively supported."""
    if engine_ring(base_ring) is not SageZZ:
        raise NotImplementedError(
            "the active native fraction-field quotient engine currently implements QQ / n ZZ"
        )
    return refine_fraction_field_quotient(QmodnZ(modulus))


def _finish_qmodnz_initialization(quotient) -> None:
    refine_fraction_field_quotient(quotient)


hook_post_init(
    QmodnZ,
    FractionFieldQuotients(SageZZ),
    after=_finish_qmodnz_initialization,
)


__all__ = [
    "FractionFieldQuotient",
    "FractionFieldQuotients",
    "refine_fraction_field_quotient",
]
