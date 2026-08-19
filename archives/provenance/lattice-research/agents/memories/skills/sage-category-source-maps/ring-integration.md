# SageMath Ring Construction Entry Points

Here is a structured map of all major ring construction entry points in SageMath,
organized by type.

* * *

## 1. Base ring singletons

These are globally unique instances, constructed once at import time in
`src/sage/all.py`:

| Object | Class | File |
| --- | --- | --- |
| `ZZ` | `IntegerRing_class` | `src/sage/rings/integer_ring.pyx` |
| `QQ` | `RationalField` | `src/sage/rings/rational_field.py` |
| `AA` | `AlgebraicRealField` | `src/sage/rings/qqbar.py` |
| `QQbar` | `AlgebraicField` | `src/sage/rings/qqbar.py` |
| `RR` | `RealField_class` | `src/sage/rings/real_mpfr.pyx` |
| `RDF` | `RealDoubleField_class` | `src/sage/rings/real_double.pyx` |
| `CC` | `ComplexField_class` | `src/sage/rings/complex_mpfr.pyx` |
| `CDF` | `ComplexDoubleField_class` | `src/sage/rings/complex_double.pyx` |
| `RLF`, `CLF` | `RealLazyField_class`, `ComplexLazyField_class` | `src/sage/rings/real_lazy.pyx` |
| `RBF` | `RealBallField` | `src/sage/rings/real_arb.pyx` |
| `CBF` | `ComplexBallField` | `src/sage/rings/complex_arb.pyx` |
| `RIF` | `RealIntervalField_class` | `src/sage/rings/real_mpfi.pyx` |
| `CIF` | `ComplexIntervalField_class` | `src/sage/rings/complex_interval_field.py` |

`ZZ` is constructed directly as `ZZ = IntegerRing_class()` at module level.
[1](#38-0)

`QQ` is a `Singleton` subclass of `NumberField`. Its `construction()` returns
`(FractionField, ZZ)`, making it the canonical fraction field of `ZZ` in the pushout
machinery. [2](#38-1)

`QQbar` and `AA` are `Singleton` subclasses of `AlgebraicField_common`.
`QQbar.construction()` returns `(AlgebraicClosureFunctor, QQ)`. [3](#38-2)

* * *

## 2. Abstract base classes (`sage.rings.abc`)

`src/sage/rings/abc.pyx` defines abstract base classes used for `isinstance` dispatch
throughout the codebase (e.g., in `PolynomialRing` constructor dispatch).
Key ones: `AlgebraicField_common`, `AlgebraicField`, `AlgebraicRealField`,
`IntegerModRing`, `pAdicRing`, `pAdicField`. [4](#38-3)

* * *

## 3. Modular and finite rings

**`IntegerModRing` / `Zmod` / `Integers`** —
`src/sage/rings/finite_rings/integer_mod_ring.py`

`IntegerModRing_generic` extends `QuotientRing_generic`. Its `__init__` calls
`QuotientRing_generic.__init__(self, ZZ, ZZ.ideal(order), ...)`. [5](#38-4)

**`GF` / `FiniteField`** — `src/sage/rings/finite_rings/finite_field_constructor.py`

`FiniteFieldFactory` is a `UniqueFactory`. `create_object` dispatches to four
implementations based on order and characteristic:
- `FiniteField_prime_modn` — prime fields (`modn`)
- `FiniteField_givaro` — small extension fields via Zech logs (order < 65536)
- `FiniteField_ntl_gf2e` — char-2 extensions via NTL
- `FiniteField_pari_ffelt` — general extension fields via PARI [6](#38-5)

* * *

## 4. Number fields

**`NumberField`** — `src/sage/rings/number_field/number_field.py`

`NumberFieldFactory.create_object` dispatches to:
- `NumberField_quadratic` — degree-2 absolute fields
- `NumberField_absolute` — general absolute fields
- `NumberField_relative` — relative extensions [7](#38-6)

`NumberField_generic.construction()` returns `(AlgebraicExtensionFunctor, QQ)`, encoding
the tower of relative polynomials.
[8](#38-7)

Convenience constructors in the same file: `QuadraticField`, `CyclotomicField`,
`NumberFieldTower`.

**`number_field_elements_from_algebraics`** — `src/sage/rings/qqbar.py` — converts
`AA`/`QQbar` elements back to a concrete number field.
[9](#38-8)

* * *

## 5. p-adic rings and fields

All entry points are in **`src/sage/rings/padics/factory.py`**, exported via
`src/sage/rings/padics/all.py`:

```
Qp, QpCR, QpFP, QpLC, QpLF, QpER   — p-adic fields
Zp, ZpCR, ZpCA, ZpFM, ZpFP, ZpLC, ZpLF, ZpER  — p-adic rings
Qq, QqCR, QqFP   — unramified extensions of Qp
Zq, ZqCR, ZqCA, ZqFM, ZqFP  — unramified extensions of Zp
pAdicExtension   — general (ramified/unramified) extensions
WittVectorRing   — Witt vectors (src/sage/rings/padics/witt_vector_ring.py)
```

`Zp_class` and `Qp_class` are `UniqueFactory` subclasses.
`create_object` dispatches to leaf classes in
`src/sage/rings/padics/padic_base_leaves.py` (`pAdicRingCappedRelative`,
`pAdicRingCappedAbsolute`, `pAdicRingFixedMod`, `pAdicRingFloatingPoint`,
`pAdicRingLattice`, `pAdicRingRelaxed`). [10](#38-9)

Extensions live in `src/sage/rings/padics/padic_extension_leaves.py` and
`relative_extension_leaves.py`.

`QQ.completion(p, prec)` routes to `Qp(p, prec)` for finite `p` and `RealField(prec)`
for `p = Infinity`. [11](#38-10)

* * *

## 6. Polynomial rings

**`PolynomialRing`** — `src/sage/rings/polynomial/polynomial_ring_constructor.py`

The main factory function.
Dispatches via `_single_variate` and `_multi_variate`. For univariate rings,
`_single_variate` checks the base ring type and selects a specialized class:

| Base ring | Class | |---|---|---| | `IntegerModRing` (prime) |
`PolynomialRing_dense_mod_p` | | `IntegerModRing` (composite) |
`PolynomialRing_dense_mod_n` | | `FiniteField` | `PolynomialRing_dense_finite_field` | |
`pAdicFieldCappedRelative` | `PolynomialRing_dense_padic_field_capped_relative` | |
`CompleteDiscreteValuationRing` | `PolynomialRing_cdvr` | | `Field` |
`PolynomialRing_field` | | `IntegralDomain` | `PolynomialRing_integral_domain` | |
generic | `PolynomialRing_commutative` | [12](#38-11)

For multivariate rings, the default is `MPolynomialRing_libsingular` (Singular backend)
when available. [13](#38-12)

Concrete univariate implementations: `src/sage/rings/polynomial/polynomial_ring.py`
Multivariate (libsingular): `src/sage/rings/polynomial/multi_polynomial_libsingular.pyx`
Multivariate (generic): `src/sage/rings/polynomial/multi_polynomial_ring.py`

**Other polynomial-type rings:**
- `LaurentPolynomialRing` — `src/sage/rings/polynomial/laurent_polynomial_ring.py`
- `OrePolynomialRing` / `SkewPolynomialRing` —
  `src/sage/rings/polynomial/ore_polynomial_ring.py`, `skew_polynomial_ring.py`
- `PolynomialQuotientRing` — `src/sage/rings/polynomial/polynomial_quotient_ring.py`
- `BooleanPolynomialRing` — `src/sage/rings/polynomial/pbori/`
- `InfinitePolynomialRing` — `src/sage/rings/polynomial/infinite_polynomial_ring.py`

* * *

## 7. Series rings

| Constructor | File |
| --- | --- |
| `PowerSeriesRing` | `src/sage/rings/power_series_ring.py` |
| `LaurentSeriesRing` | `src/sage/rings/laurent_series_ring.py` |
| `MultiPowerSeriesRing` | `src/sage/rings/multi_power_series_ring.py` |
| `PuiseuxSeriesRing` | `src/sage/rings/puiseux_series_ring.py` |
| `LazyPowerSeriesRing`, `LazyLaurentSeriesRing` | `src/sage/rings/lazy_series_ring.py` |
| `LazyDirichletSeriesRing` | `src/sage/rings/lazy_series_ring.py` |
| `TateAlgebra` | `src/sage/rings/tate_algebra.py` |
| `AsymptoticRing` | `src/sage/rings/asymptotic/asymptotic_ring.py` |

* * *

## 8. Fraction fields, localizations, quotients

**`FractionField(R)`** — `src/sage/rings/fraction_field.py` — delegates to
`R.fraction_field()`. `FractionField_generic` is the base class.
[14](#38-13)

**`Localization(R, extra_units)`** — `src/sage/rings/localization.py` — inverts a tuple
of elements in an integral domain, embedding into the fraction field.
[15](#38-14)

**`QuotientRing(R, I)`** — `src/sage/rings/quotient_ring.py`

* * *

## 9. Function fields

`src/sage/rings/function_field/` — full directory:
- `FunctionField` constructor — `function_field.py`
- `FunctionField_rational` — rational function fields
- `FunctionField_polymod` — algebraic extensions
- Submodules for ideals, orders, places, divisors, Jacobians, Drinfeld modules

* * *

## 10. Ring extensions

**`RingExtension`** — `src/sage/rings/ring_extension.pyx` — wraps a ring homomorphism
`f: R → S` to present `S` as an `R`-algebra with explicit base.

* * *

## 11. Valuations

`src/sage/rings/valuation/` — standalone valuation framework:
- `valuation.py` — abstract `Valuation` base
- `gauss_valuation.py`, `augmented_valuation.py`, `inductive_valuation.py`
- `padic_valuation.py` — p-adic valuations on number fields and polynomial rings
- `valuations_catalog.py` — entry point

* * *

## 12. The pushout / coercion framework

**`src/sage/categories/pushout.py`** — the central file for ring construction functors.
Every ring that participates in coercion must implement `construction()` returning
`(ConstructionFunctor, simpler_ring)`.

Key functor classes and their ranks (lower rank = applied first in pushout):

| Functor | Rank | File |
| --- | --- | --- |
| `AlgebraicExtensionFunctor` | 3 | `pushout.py` |
| `CompletionFunctor` | 4 | `pushout.py` |
| `FractionField` | 5 | `pushout.py` |
| `QuotientFunctor` | 7 | `pushout.py` |
| `PolynomialFunctor` / `MultiPolynomialFunctor` | 9 | `pushout.py` |
| `MatrixFunctor` | 10 | `pushout.py` |
| `AlgebraicClosureFunctor` | 3 | `pushout.py` |

The `pushout(R, S)` function finds a common parent by walking the construction towers of
`R` and `S` and merging functors by rank.
[17](#38-16)

If you define a new ring type, you must implement `construction()` and a matching
`ConstructionFunctor` with a `merge()` method to participate in automatic coercion.
The `_apply_functor` method on the functor is what actually builds the ring.
[18](#38-17)

* * *

## 13. Residue fields

**`ResidueField`** — `src/sage/rings/finite_rings/residue_field.py` — residue fields of
prime ideals in number rings and polynomial rings.
Also produced by `AlgebraicExtensionFunctor` when applied to a residue field context.

* * *

## Summary: what to hook into

To promote your custom ring category without rewriting math:

1. **Implement `construction()`** on your ring returning a custom `ConstructionFunctor`
   — this makes your ring participate in pushout/coercion automatically.
2. **Override `fraction_field()`** if your ring has a natural fraction field different
   from the generic one.
3. **Override `completion(p, prec)`** if your ring has completions.
4. **Register coercions** via `_coerce_map_from_` or `_populate_coercion_lists_`.
5. **The `PolynomialRing` constructor** is the main place to hook if you want `R[x]` to
   return your custom polynomial ring — add a branch in `_single_variate` or
   `_multi_variate` checking `isinstance(base_ring, YourRingClass)`.

* * *

## References

### [1] ZZ construction

**File:** `src/sage/rings/integer_ring.pyx` (L1595-1596)
```python
ZZ = IntegerRing_class()
Z = ZZ
```

### [2] QQ construction and completion

**File:** `src/sage/rings/rational_field.py` (L307-322, L324-341)
```python
    def construction(self):
        from sage.categories.pushout import FractionField
        from . import integer_ring
        return FractionField(), integer_ring.ZZ

    def completion(self, p, prec, extras={}):
        if p == Infinity:
            from sage.rings.real_field import create_RealField
            return create_RealField(prec, **extras)
        else:
            from sage.rings.padics.factory import Qp
            return Qp(p, prec, **extras)
```

### [3] QQbar construction

**File:** `src/sage/rings/qqbar.py` (L1779-1790)
```python
    def construction(self):
        from sage.categories.pushout import AlgebraicClosureFunctor
        from sage.rings.rational_field import QQ
        return (AlgebraicClosureFunctor(), QQ)
```

### [4] Abstract base classes

**File:** `src/sage/rings/abc.pyx` (L91-112)
```python
    EXAMPLES::
        sage: import sage.rings.abc
        sage: isinstance(QQbar, sage.rings.abc.AlgebraicField_common)
        True
        sage: isinstance(AA, sage.rings.abc.AlgebraicField_common)
        True
```

### [5] IntegerModRing as quotient

**File:** `src/sage/rings/finite_rings/integer_mod_ring.py` (L429-484)
```python
    quotient_ring.QuotientRing_generic.__init__(self, ZZ, ZZ.ideal(order),
                                                names=('x',),
                                                category=category)
```

### [6] FiniteField dispatch

**File:** `src/sage/rings/finite_rings/finite_field_constructor.py` (L849-879)
```python
        if implementation == 'modn':
            from .finite_field_prime_modn import FiniteField_prime_modn
            K = FiniteField_prime_modn(order, check=False, modulus=modulus)
        # ... dispatches to givaro, ntl_gf2e, pari_ffelt
```

### [7] NumberField dispatch

**File:** `src/sage/rings/number_field/number_field.py` (L668-691)
```python
        if isinstance(base, NumberField_generic):
            from sage.rings.number_field.number_field_rel import NumberField_relative
            return NumberField_relative(...)
        if polynomial.degree() == 2:
            return NumberField_quadratic(...)
        else:
            return NumberField_absolute(...)
```

### [8] NumberField construction

**File:** `src/sage/rings/number_field/number_field.py` (L1521-1588)
```python
    def construction(self):
        from sage.categories.pushout import AlgebraicExtensionFunctor
        return (AlgebraicExtensionFunctor(polys, names, ...), QQ)
```

### [9] number_field_elements_from_algebraics

**File:** `src/sage/rings/qqbar.py` (L2495-2530)
```python
def number_field_elements_from_algebraics(numbers, minimal=False,
                                          same_field=False, ...):
    r"""
    Given a sequence of elements of either AA or QQbar, computes a
    number field containing all of these elements...
    """
```

### [10] p-adic factory dispatch

**File:** `src/sage/rings/padics/factory.py` (L2031-2051)
```python
        if type == 'capped-rel':
            return pAdicRingCappedRelative(...)
        elif type == 'fixed-mod':
            return pAdicRingFixedMod(...)
        # ... etc
```

### [11] QQ.completion dispatch

**File:** `src/sage/rings/rational_field.py` (L324-341)
```python
    def completion(self, p, prec, extras={}):
        if p == Infinity:
            return create_RealField(prec, **extras)
        else:
            return Qp(p, prec, **extras)
```

### [12] PolynomialRing dispatch

**File:** `src/sage/rings/polynomial/polynomial_ring_constructor.py` (L820-864)
```python
    if isinstance(base_ring, sage.rings.abc.IntegerModRing):
        if base_ring.is_field():
            specialized = polynomial_ring.PolynomialRing_dense_mod_p
    elif isinstance(base_ring, FiniteField):
        specialized = polynomial_ring.PolynomialRing_dense_finite_field
    # ... generic fallbacks
```

### [13] Multivariate polynomial implementation

**File:** `src/sage/rings/polynomial/polynomial_ring_constructor.py` (L447-451)
```python
        sage: R = PolynomialRing(ZZ, 'x,y', implementation='generic')
        sage: S = PolynomialRing(ZZ, 'x,y')  # libsingular by default
```

### [14] FractionField

**File:** `src/sage/rings/fraction_field.py` (L98-143)
```python
def FractionField(R, names=None):
    if R not in Rings():
        raise TypeError("R must be a ring")
    if not R.is_integral_domain():
        raise TypeError("R must be an integral domain")
    return R.fraction_field()
```

### [15] Localization

**File:** `src/sage/rings/localization.py` (L564-715)
```python
class Localization(Parent, UniqueRepresentation):
    r"""
    The localization generalizes the construction of the field of fractions...
    """
    def __init__(self, base_ring, extra_units, ...):
        # ... implementation
```

### [16] Functor ranks

**File:** `src/sage/categories/pushout.py` (L44-127)
```python
class ConstructionFunctor(Functor):
    """
    Base class for construction functors with merge() and rank attributes.
    """
    rank = None  # lower rank = applied first
```

### [17] pushout algorithm

**File:** `src/sage/categories/pushout.py` (L4003-4046)
```python
def pushout(R, S):
    r"""
    Given a pair of objects R and S, try to construct a
    reasonable object Y and return maps such that
    canonically R <- Y -> S.
    """
```

### [18] _apply_functor pattern

**File:** `src/doc/en/thematic_tutorials/coercion_and_categories.rst` (L1305-1320)
```python
    sage: class MyFracFunctor(ConstructionFunctor):
    ....:     rank = 5
    ....:     def _apply_functor(self, R):
    ....:         return MyFrac(R,*self.args,**self.kwds)
    ....:     def merge(self, other):
    ....:         if isinstance(other, (type(self), FractionField)):
    ....:             return self
```
