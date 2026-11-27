"""Axiom registration, subcategory selectors, and named shortcuts for Rings."""

from __future__ import annotations

from sage.categories.homset import End as SageEnd
from sage.categories.homset import Hom as SageHom
from sage.misc.cachefunc import cached_method


class _RingSubcategorySelectors:
    r"""Mixin providing ``SubcategoryMethods`` axiom and functorial selectors."""

    @cached_method
    def Commutative(self):
        return self._with_axiom("Commutative")

    @cached_method
    def Division(self):
        return self._with_axiom("Division")

    @cached_method
    def Finite(self):
        return self._with_axiom("Finite")

    @cached_method
    def Topological(self):
        return self._with_axiom("Topological")

    @cached_method
    def WithValuation(self):
        return self._with_axiom("WithValuation")

    @cached_method
    def Characteristic(self, p):
        from .constructions import _CharacteristicRings

        return _CharacteristicRings(self, p)

    @cached_method
    def KrullDimension(self, n):
        from .constructions import _KrullDimension

        return _KrullDimension(self, n)

    @cached_method
    def Polynomial(self):
        return self._with_axiom("Polynomial")

    @cached_method
    def PowerSeries(self):
        return self._with_axiom("PowerSeries")

    @cached_method
    def LaurentSeries(self):
        return self._with_axiom("LaurentSeries")

    @cached_method
    def PuiseuxSeries(self):
        return self._with_axiom("PuiseuxSeries")

    @cached_method
    def Subquotients(self):
        from .constructions import _Subquotients

        return _Subquotients.category_of(self)

    @cached_method
    def Subobjects(self):
        from .constructions import _Subobjects

        return _Subobjects.category_of(self)

    @cached_method
    def Quotients(self):
        from .constructions import _Quotients

        return _Quotients.category_of(self)

    @cached_method
    def RingsUnder(self, structure_ring):
        from .constructions import _RingsUnder

        return _RingsUnder.category_of(self, structure_ring)

    @cached_method
    def RingsOver(self, structure_ring):
        from .constructions import _RingsOver

        return _RingsOver.category_of(self, structure_ring)

    @cached_method
    def AlgebrasOver(self, structure_ring):
        from ..algebras import Algebras

        return Algebras(structure_ring)

    @cached_method
    def PolynomialRings(self):
        return self.Polynomial()

    @cached_method
    def PolynomialRingsOver(self, structure_ring):
        return self.Polynomial().RingsUnder(structure_ring)

    @cached_method
    def PolynomialOver(self, structure_ring):
        return self.PolynomialRingsOver(structure_ring)

    @cached_method
    def PowerSeriesRings(self):
        return self.PowerSeries()

    @cached_method
    def PowerSeriesRingsOver(self, structure_ring):
        return self.PowerSeries().RingsUnder(structure_ring)

    @cached_method
    def PowerSeriesOver(self, structure_ring):
        return self.PowerSeriesRingsOver(structure_ring)

    @cached_method
    def LaurentSeriesRings(self):
        return self.LaurentSeries()

    @cached_method
    def LaurentSeriesRingsOver(self, structure_ring):
        return self.LaurentSeries().RingsUnder(structure_ring)

    @cached_method
    def LaurentSeriesOver(self, structure_ring):
        return self.LaurentSeriesRingsOver(structure_ring)

    @cached_method
    def PuiseuxSeriesRings(self):
        return self.PuiseuxSeries()

    @cached_method
    def PuiseuxSeriesRingsOver(self, structure_ring):
        return self.PuiseuxSeries().RingsUnder(structure_ring)

    @cached_method
    def PuiseuxSeriesOver(self, structure_ring):
        return self.PuiseuxSeriesRingsOver(structure_ring)

    @cached_method
    def QuotientRingsOf(self, structure_ring):
        return self.Quotients().RingsUnder(structure_ring)

    @cached_method
    def QuotientsOf(self, structure_ring):
        return self.QuotientRingsOf(structure_ring)

    @cached_method
    def SubringsOf(self, structure_ring):
        return self.Subobjects().RingsOver(structure_ring)


class _RingNamedShortcuts:
    r"""Mixin providing named category accessor shortcuts on ``Rings``."""

    def Hom(self, domain, codomain):
        from .homsets import RingHomsets

        return RingHomsets.from_sage_homset(SageHom(domain, codomain, category=self))

    def End(self, ring):
        from .homsets import _Endsets

        return _Endsets.from_sage_endset(SageEnd(ring, category=self))

    @cached_method
    def NamedRings(self):
        from .specialized import _NamedRings

        return _NamedRings()

    @cached_method
    def CommutativeRings(self):
        from .specialized import _CommutativeRings

        return _CommutativeRings()

    @cached_method
    def DivisionRings(self):
        from .specialized import _DivisionRings

        return _DivisionRings()

    @cached_method
    def FiniteRings(self):
        from .specialized import _FiniteRings

        return _FiniteRings()

    @cached_method
    def IntegralDomains(self):
        return self.Commutative().IntegralDomains()

    @cached_method
    def Fields(self):
        return self.Commutative().Field()

    @cached_method
    def ReducedRings(self):
        return self.Commutative().Reduced()

    @cached_method
    def NoetherianRings(self):
        from .specialized import _NoetherianRings

        return _NoetherianRings()

    @cached_method
    def GcdDomains(self):
        from .specialized import _GcdDomains

        return _GcdDomains()

    @cached_method
    def UniqueFactorizationDomains(self):
        from .specialized import _UniqueFactorizationDomains

        return _UniqueFactorizationDomains()

    @cached_method
    def PrincipalIdealDomains(self):
        from .specialized import _PrincipalIdealDomains

        return _PrincipalIdealDomains()

    @cached_method
    def EuclideanDomains(self):
        from .specialized import _EuclideanDomains

        return _EuclideanDomains()

    @cached_method
    def DedekindDomains(self):
        from .specialized import _DedekindDomains

        return _DedekindDomains()

    @cached_method
    def ValuedRings(self):
        from .specialized import _ValuedRings

        return _ValuedRings()

    @cached_method
    def DiscreteValuationRings(self):
        from .specialized import _DiscreteValuationRings

        return _DiscreteValuationRings()

    @cached_method
    def DiscreteValuationFields(self):
        from .specialized import _DiscreteValuationFields

        return _DiscreteValuationFields()

    @cached_method
    def CompleteRings(self):
        from .specialized import _CompleteRings

        return _CompleteRings()

    @cached_method
    def CompleteDiscreteValuationRings(self):
        from .specialized import _CompleteDiscreteValuationRings

        return _CompleteDiscreteValuationRings()

    @cached_method
    def CompleteDiscreteValuationFields(self):
        from .specialized import _CompleteDiscreteValuationFields

        return _CompleteDiscreteValuationFields()

    @cached_method
    def LocalRings(self):
        from .specialized import _LocalRings

        return _LocalRings()

    @cached_method
    def FiniteFields(self):
        return self.Fields().Finite()

    @cached_method
    def NumberFields(self):
        return self.Fields().NumberFields()

    @cached_method
    def AlgebraicallyClosedFields(self):
        return self.Fields().AlgebraicallyClosed()

    @cached_method
    def LocalFields(self):
        return self.Fields().LocalFields()

    @cached_method
    def GlobalFields(self):
        return self.Fields().GlobalFields()

    @cached_method
    def ArchimedeanGlobalFields(self):
        return self.GlobalFields().Archimedean()

    @cached_method
    def NonArchimedeanGlobalFields(self):
        return self.GlobalFields().NonArchimedean()

    @cached_method
    def QuadraticNumberFields(self):
        return self.NumberFields().Quadratic()

    @cached_method
    def CyclotomicFields(self):
        return self.NumberFields().Cyclotomic()

    @cached_method
    def QuotientFields(self):
        from .specialized import _QuotientFields

        return _QuotientFields()

    @cached_method
    def ZZ(self):
        from .specialized import _ZZ

        return _ZZ()

    @cached_method
    def QQ(self):
        return self.Fields().QQ()

    @cached_method
    def QQbar(self):
        from .specialized import _QQbar

        return _QQbar()

    @cached_method
    def AA(self):
        from .specialized import _AA

        return _AA()

    @cached_method
    def RealFields(self):
        from .specialized import _RealFields

        return _RealFields()

    @cached_method
    def ComplexFields(self):
        from .specialized import _ComplexFields

        return _ComplexFields()

    @cached_method
    def IntegerModRings(self):
        from .specialized import _IntegerModRings

        return _IntegerModRings()

    @cached_method
    def Zp(self):
        from .specialized import _Zp

        return _Zp()

    @cached_method
    def Qp(self):
        from .specialized import _Qp

        return _Qp()

    @cached_method
    def PolynomialRing(self, base_ring=None):
        from .specialized import _PolynomialRings

        category = _PolynomialRings()
        if base_ring is None:
            return category
        return category.RingsUnder(base_ring)

    @cached_method
    def MatrixRing(self, base_ring, n):
        from .matrix_algebras import _MatrixAlgebras

        return _MatrixAlgebras(base_ring, n, n)

    @cached_method
    def PowerSeriesRing(self, base_ring=None):
        from .specialized import _PowerSeriesRings

        category = _PowerSeriesRings()
        if base_ring is None:
            return category
        return category.RingsUnder(base_ring)

    @cached_method
    def LaurentSeriesRing(self, base_ring=None):
        from .specialized import _LaurentSeriesRings

        category = _LaurentSeriesRings()
        if base_ring is None:
            return category
        return category.RingsUnder(base_ring)

    @cached_method
    def PuiseuxSeriesRing(self, base_ring=None):
        from .specialized import _PuiseuxSeriesRings

        category = _PuiseuxSeriesRings()
        if base_ring is None:
            return category
        return category.RingsUnder(base_ring)
