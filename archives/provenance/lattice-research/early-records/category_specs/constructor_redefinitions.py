"""Install top-level Sage constructor redefinitions for category refinement."""

from __future__ import annotations

from collections.abc import Callable
from importlib import import_module
from typing import TYPE_CHECKING, Any, cast

from sage.modules.free_module import FreeModule as _SageFreeModule
from sage.modules.free_module import VectorSpace as _SageVectorSpace
from sage.structure.parent import Parent as SageParent

if TYPE_CHECKING:
    from .types import (
        Category,
        CategoryObject,
        Integer,
        Matrix,
        Polynomial,
        RMod,
        Ring,
        RingElement,
        RModule,
    )

type SageConstructor = Callable[..., object]

_INSTALLED = False


def _sage_constructor(module_name: str, attr_name: str) -> SageConstructor:
    module = import_module(module_name)
    return cast(SageConstructor, getattr(module, attr_name))


def _refine_as_parent(parent: object, categories: "Category | list[Category]") -> SageParent:
    from .utils import refine_category

    return refine_category(cast(SageParent, parent), categories, test=False)


def _category_list(*categories: object) -> "list[Category]":
    return [cast("Category", category) for category in categories]


def _modules_over(base_ring: "Ring") -> "RMod":
    from .modules import Modules

    return cast("RMod", Modules(cast("CategoryObject", base_ring)))


def _module_axiom(base_ring: "Ring", *axioms: str) -> "Category":
    from .utils import with_axiom

    category = cast("Category", _modules_over(base_ring))
    for axiom in axioms:
        category = cast("Category", with_axiom(category, axiom))
    return category


def _ring_axiom(*axioms: str) -> "Category":
    from .rings import Rings
    from .utils import with_axiom

    category = cast("Category", Rings())
    for axiom in axioms:
        category = cast("Category", with_axiom(category, axiom))
    return category


def _ring_axiom_under(axiom: str, base_ring: "Ring") -> "Category":
    rings_under = cast(SageConstructor, getattr(_ring_axiom(axiom), "RingsUnder"))
    return cast("Category", rings_under(base_ring))


_SageCombinatorialFreeModule = _sage_constructor(
    "sage.combinat.free_module", "CombinatorialFreeModule"
)
_SageFreeModuleConstructor = _sage_constructor("sage.modules.free_module", "FreeModule")
_SageMatrixSpace = _sage_constructor("sage.matrix.matrix_space", "MatrixSpace")
_SageGF = _sage_constructor("sage.rings.finite_rings.finite_field_constructor", "GF")
_SageFiniteField = _sage_constructor(
    "sage.rings.finite_rings.finite_field_constructor", "FiniteField"
)
_SageIntegerModRing = _sage_constructor(
    "sage.rings.finite_rings.integer_mod_ring", "IntegerModRing"
)
_SageQuadraticField = _sage_constructor(
    "sage.rings.number_field.number_field", "QuadraticField"
)
_SageZp = _sage_constructor("sage.rings.padics.factory", "Zp")
_SageLaurentPolynomialRing = _sage_constructor(
    "sage.rings.polynomial.laurent_polynomial_ring", "LaurentPolynomialRing"
)
_SagePolynomialRing = _sage_constructor(
    "sage.rings.polynomial.polynomial_ring_constructor", "PolynomialRing"
)
_SagePowerSeriesRing = _sage_constructor(
    "sage.rings.power_series_ring", "PowerSeriesRing"
)


def FreeModule(
    base_ring: "Ring",
    rank: "Integer",
    sparse: bool = False,
    *,
    inner_product_matrix: "Matrix | None" = None,
) -> "RModule":
    M = cast(
        "RModule",
        _SageFreeModuleConstructor(base_ring, rank, sparse, inner_product_matrix),
    )
    return cast(
        "RModule",
        _refine_as_parent(
            M,
            [_module_axiom(base_ring, "Free", "FinitelyPresented", "FiniteRank")],
        ),
    )


def VectorSpace(
    base_ring: "Ring",
    dimension: "Integer",
    sparse: bool = False,
    *,
    inner_product_matrix: "Matrix | None" = None,
) -> "RModule":
    M = cast(
        "RModule",
        _SageFreeModuleConstructor(base_ring, dimension, sparse, inner_product_matrix),
    )
    return cast(
        "RModule",
        _refine_as_parent(
            M,
            [
                _module_axiom(base_ring, "Free", "FinitelyPresented", "FiniteRank"),
                _module_axiom(base_ring, "OverField"),
            ],
        ),
    )


def MatrixSpace(
    base_ring: "Ring",
    nrows: "Integer",
    ncols: "Integer | None" = None,
    sparse: bool = False,
    implementation: str | type[Any] | None = None,
) -> "RModule":
    if ncols is None:
        ncols = nrows
    M = cast(
        "RModule",
        _SageMatrixSpace(
            base_ring,
            nrows,
            ncols,
            sparse=sparse,
            implementation=implementation,
        ),
    )
    return cast(
        "RModule",
        _refine_as_parent(
            M,
            [_module_axiom(base_ring, "Free", "FinitelyPresented", "FiniteRank")],
        ),
    )


def CombinatorialFreeModule(
    base_ring: "Ring",
    basis_keys: Any = None,
    element_class: type[Any] | None = None,
    category: Any | None = None,
    prefix: str | None = None,
    names: str | tuple[str, ...] | None = None,
) -> "RModule":
    M = cast(
        "RModule",
        _SageCombinatorialFreeModule(
            base_ring,
            basis_keys,
            element_class=element_class,
            category=category,
            prefix=prefix,
            names=names,
        ),
    )
    return cast(
        "RModule",
        _refine_as_parent(
            M,
            [
                _module_axiom(base_ring, "Free"),
                _module_axiom(base_ring, "WithBasis"),
                _module_axiom(base_ring, "WithOrderedGeneratingSet"),
            ],
        ),
    )


def GF(
    order: "Integer",
    name: str | None = None,
    modulus: "Polynomial | str | None" = None,
    names: str | None = None,
    impl: str | None = None,
    proof: bool | None = None,
    check_prime: bool = True,
    check_irreducible: bool = True,
    prefix: str | None = None,
    repr: str | None = None,
    elem_cache: bool | None = None,
) -> "Ring":
    from .rings import Rings
    from .rings.subcategories.finite_field import _FiniteFields

    constructor_keywords: dict[str, object] = {
        "check_prime": check_prime,
        "check_irreducible": check_irreducible,
    }
    if name is not None:
        constructor_keywords["name"] = name
    if modulus is not None:
        constructor_keywords["modulus"] = modulus
    if names is not None:
        constructor_keywords["names"] = names
    if impl is not None:
        constructor_keywords["impl"] = impl
    if proof is not None:
        constructor_keywords["proof"] = proof
    if prefix is not None:
        constructor_keywords["prefix"] = prefix
    if repr is not None:
        constructor_keywords["repr"] = repr
    if elem_cache is not None:
        constructor_keywords["elem_cache"] = elem_cache

    R = cast(
        "Ring",
        _SageGF(
            order,
            **constructor_keywords,
        ),
    )
    return cast("Ring", _refine_as_parent(R, _category_list(Rings(), _FiniteFields())))


def FiniteField(
    order: "Integer",
    name: str | None = None,
    modulus: "Polynomial | str | None" = None,
    names: str | None = None,
    impl: str | None = None,
    proof: bool | None = None,
    check_prime: bool = True,
    check_irreducible: bool = True,
    prefix: str | None = None,
    repr: str | None = None,
    elem_cache: bool | None = None,
) -> "Ring":
    from .rings import Rings
    from .rings.subcategories.finite_field import _FiniteFields

    constructor_keywords: dict[str, object] = {
        "check_prime": check_prime,
        "check_irreducible": check_irreducible,
    }
    if name is not None:
        constructor_keywords["name"] = name
    if modulus is not None:
        constructor_keywords["modulus"] = modulus
    if names is not None:
        constructor_keywords["names"] = names
    if impl is not None:
        constructor_keywords["impl"] = impl
    if proof is not None:
        constructor_keywords["proof"] = proof
    if prefix is not None:
        constructor_keywords["prefix"] = prefix
    if repr is not None:
        constructor_keywords["repr"] = repr
    if elem_cache is not None:
        constructor_keywords["elem_cache"] = elem_cache

    R = cast(
        "Ring",
        _SageFiniteField(
            order,
            **constructor_keywords,
        ),
    )
    return cast("Ring", _refine_as_parent(R, _category_list(Rings(), _FiniteFields())))


def IntegerModRing(
    order: "Integer" = cast("Integer", 0),
    is_field: bool = False,
    category: Any | None = None,
) -> "Ring":
    from .rings import Rings
    from .rings.subcategories.integer_mod_ring import _IntegerModRings
    from .utils import with_axiom

    R = cast("Ring", _SageIntegerModRing(order, is_field=is_field, category=category))
    return cast(
        "Ring",
        _refine_as_parent(
            R,
            _category_list(
                Rings(),
                _IntegerModRings(),
                with_axiom(ModulesZZ(), "FinitelyPresented"),
            ),
        ),
    )


def Zp(
    p: "Integer",
    prec: "Integer | None" = None,
    type: str = "capped-rel",
    print_mode: str | None = None,
    names: str | None = None,
) -> "Ring":
    from .rings import Rings
    from .rings.subcategories.p_adic_integer_ring import _Zp

    R = cast(
        "Ring",
        _SageZp(
            p,
            prec=prec,
            type=type,
            print_mode=print_mode,
            names=names,
        ),
    )
    return cast("Ring", _refine_as_parent(R, _category_list(Rings(), _Zp())))


def PolynomialRing(
    base_ring: "Ring",
    name: str | tuple[str, ...] | None = None,
    *,
    n: "Integer | None" = None,
    names: str | tuple[str, ...] | None = None,
    sparse: bool | None = None,
    order: str = "degrevlex",
    implementation: str | None = None,
) -> "Ring":
    from sage.categories.fields import Fields


    if names is None and name is not None:
        names = name
    if isinstance(names, tuple):
        return cast(
            "Ring",
            _SagePolynomialRing(
                base_ring,
                names,
                sparse=sparse,
                order=order,
                implementation=implementation,
            ),
        )
    if names is None:
        raise TypeError("PolynomialRing expects a variable name")
    R = cast(
        "Ring",
        _SagePolynomialRing(
            base_ring,
            names,
            sparse=sparse,
            order=order,
            implementation=implementation,
        ),
    )
    if base_ring not in Fields():
        return cast("Ring", R)
    return cast(
        "Ring",
        _refine_as_parent(
            R,
            [_ring_axiom_under("Polynomial", cast("Ring", R.base_ring()))],
        ),
    )


def LaurentPolynomialRing(
    base_ring: "Ring",
    name: str,
    sparse: bool = False,
) -> "Ring":
    R = cast("Ring", _SageLaurentPolynomialRing(base_ring, name, sparse=sparse))
    return cast(
        "Ring",
        _refine_as_parent(
            R,
            [_ring_axiom_under("LaurentSeries", cast("Ring", R.base_ring()))],
        ),
    )


def PowerSeriesRing(
    base_ring: "Ring",
    name: str,
    *,
    sparse: bool = False,
    default_prec: "Integer | None" = None,
    implementation: str | None = None,
) -> "Ring":
    R = cast(
        "Ring",
        _SagePowerSeriesRing(
            base_ring,
            name,
            sparse=sparse,
            default_prec=default_prec,
            implementation=implementation,
        ),
    )
    return cast(
        "Ring",
        _refine_as_parent(
            R,
            [_ring_axiom_under("PowerSeries", cast("Ring", R.base_ring()))],
        ),
    )


def QuadraticField(
    D: "RingElement | Integer",
    name: str = "a",
    check: bool = True,
    embedding: bool | "RingElement" = True,
    latex_name: str = "sqrt",
) -> "Ring":
    from sage.categories.dedekind_domains import DedekindDomains

    from .rings import Rings
    from .rings.subcategories.quadratic_number_field import _QuadraticNumberFields

    R = cast(
        "Ring",
        _SageQuadraticField(
            D,
            name=name,
            check=check,
            embedding=embedding,
            latex_name=latex_name,
        ),
    )
    refined = _refine_as_parent(
        R,
        _category_list(Rings(), _QuadraticNumberFields()),
    )
    ring_of_integers = cast(SageConstructor, getattr(refined, "ring_of_integers"))
    _refine_as_parent(ring_of_integers(), [cast("Category", DedekindDomains())])
    return cast("Ring", refined)


def ModulesZZ() -> "Category":
    from sage.all import ZZ

    from .modules import Modules

    return cast("Category", Modules(ZZ))


def install_constructor_redefinitions() -> None:
    global _INSTALLED
    if _INSTALLED:
        return

    import sage.all as sage_all
    import sage.combinat.free_module as combinat_free_module
    import sage.modules.free_module as free_module_module
    import sage.rings.finite_rings.finite_field_constructor as finite_field_module
    import sage.rings.finite_rings.integer_mod_ring as integer_mod_ring_module
    import sage.rings.number_field.number_field as number_field_module
    import sage.rings.padics.factory as padic_factory_module
    import sage.rings.polynomial.laurent_polynomial_ring as laurent_poly_module
    import sage.rings.polynomial.polynomial_ring_constructor as poly_module
    import sage.rings.power_series_ring as power_series_module

    setattr(free_module_module, "FreeModule", FreeModule)
    setattr(free_module_module, "VectorSpace", VectorSpace)
    setattr(combinat_free_module, "CombinatorialFreeModule", CombinatorialFreeModule)
    setattr(finite_field_module, "GF", GF)
    setattr(finite_field_module, "FiniteField", FiniteField)
    setattr(integer_mod_ring_module, "IntegerModRing", IntegerModRing)
    setattr(padic_factory_module, "Zp", Zp)
    setattr(poly_module, "PolynomialRing", PolynomialRing)
    setattr(laurent_poly_module, "LaurentPolynomialRing", LaurentPolynomialRing)
    setattr(power_series_module, "PowerSeriesRing", PowerSeriesRing)
    setattr(number_field_module, "QuadraticField", QuadraticField)

    setattr(sage_all, "FreeModule", FreeModule)
    setattr(sage_all, "VectorSpace", VectorSpace)
    setattr(sage_all, "CombinatorialFreeModule", CombinatorialFreeModule)
    setattr(sage_all, "MatrixSpace", MatrixSpace)
    setattr(sage_all, "GF", GF)
    setattr(sage_all, "FiniteField", FiniteField)
    setattr(sage_all, "IntegerModRing", IntegerModRing)
    setattr(sage_all, "Zp", Zp)
    setattr(sage_all, "PolynomialRing", PolynomialRing)
    setattr(sage_all, "LaurentPolynomialRing", LaurentPolynomialRing)
    setattr(sage_all, "PowerSeriesRing", PowerSeriesRing)
    setattr(sage_all, "QuadraticField", QuadraticField)

    _INSTALLED = True
