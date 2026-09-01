"""Free algebra constructions on a chosen set of generators."""

from sage.algebras.free_algebra import FreeAlgebra as _SageFreeAlgebra
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.algebras import (
    CommutativeAlgebras,
    refine_algebra,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    FreeAlgebras,
    GradedFreeAlgebras,
    SymmetricAlgebras,
    TensorAlgebras,
)
from dzack_research.preamble.categories.rings import engine_ring, owned_ring_view
from dzack_research.preamble.categories.rings.rings import (
    PolynomialRing as _OwnedPolynomialRing,
)
from dzack_research.preamble.categories.sets import FiniteOrderedSet, finite_ordered_set
from dzack_research.preamble.refine import refine


def _finite_labels(labels) -> FiniteOrderedSet:
    if isinstance(labels, FiniteOrderedSet):
        return labels
    if isinstance(labels, int):
        return finite_ordered_set(range(labels))
    return finite_ordered_set(labels)


def _variable_names(labels: FiniteOrderedSet) -> tuple[str, ...]:
    names = []
    used: set[str] = set()
    for index, label in enumerate(labels):
        candidate = str(label)
        if not candidate.isidentifier() or candidate in used:
            candidate = f"x{index}"
        while candidate in used:
            candidate = f"x{index}_{len(used)}"
        names.append(candidate)
        used.add(candidate)
    return tuple(names)


def FreeAlgebraOn(base_ring, algebra_generating_set):
    r"""Return the free commutative algebra ``R[S] = Sym(F_R(S))``."""
    return SymmetricAlgebraOn(base_ring, algebra_generating_set)


def SymmetricAlgebraOn(base_ring, algebra_generating_set):
    labels = _finite_labels(algebra_generating_set)
    base = owned_ring_view(base_ring)
    algebra = _OwnedPolynomialRing(base, _variable_names(labels))
    return refine_algebra(
        algebra,
        base,
        labels,
        FreeAlgebras(base),
        GradedFreeAlgebras(base),
        SymmetricAlgebras(base),
    )


def TensorAlgebraOn(base_ring, algebra_generating_set):
    labels = _finite_labels(algebra_generating_set)
    base = owned_ring_view(base_ring)
    names = _variable_names(labels)
    algebra = _SageFreeAlgebra(engine_ring(base), len(labels), names=names)
    return refine_algebra(
        algebra,
        base,
        labels,
        FreeAlgebras(base),
        GradedFreeAlgebras(base),
        TensorAlgebras(base),
    )


def AlternatingAlgebraOn(base_ring, algebra_generating_set):
    from dzack_research.preamble.categories.algebras.power_algebras import (
        AlternatingAlgebraOn as _alternating_algebra_on,
    )

    return _alternating_algebra_on(base_ring, algebra_generating_set)


def DividedPowerAlgebraOn(base_ring, algebra_generating_set):
    from dzack_research.preamble.categories.algebras.power_algebras import (
        DividedPowerAlgebraOn as _divided_power_algebra_on,
    )

    return _divided_power_algebra_on(base_ring, algebra_generating_set)


def polynomial_ring(base_ring, names):
    r"""Return the symmetric algebra using standard polynomial-ring syntax."""
    if isinstance(names, str):
        labels = tuple(part.strip() for part in names.split(","))
    elif isinstance(names, int):
        labels = tuple(f"x{i}" for i in range(names))
    else:
        labels = tuple(names)
    return SymmetricAlgebraOn(base_ring, labels)


def TensorAlgebraOf(module):
    r"""Return \(T_R(M)\), including the linear relations of ``M``."""
    if module.module_generating_set().cardinality() not in SageZZ:
        from dzack_research.preamble.categories.algebras.sparse_free_algebras import (
            SparseTensorAlgebraOf,
        )

        return SparseTensorAlgebraOf(module)
    from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
        _tensor_algebra_from_module_presentation,
    )
    from dzack_research.preamble.categories.algebras.graded_algebras import (
        GradedAlgebras,
    )

    base = module.base_ring()
    presentation_ring = TensorAlgebraOn(base, module.module_generating_set())
    algebra = _tensor_algebra_from_module_presentation(presentation_ring, module)
    algebra._preamble_free_algebra_source_module = module
    if algebra is presentation_ring:
        return algebra
    return refine(
        algebra,
        [
            GradedFreeAlgebras(base),
            TensorAlgebras(base),
            GradedAlgebras(base),
        ],
    )


def SymmetricAlgebraOf(module):
    r"""Return \(\operatorname{Sym}_R(M)\) with ``M``'s linear relations."""
    if module.module_generating_set().cardinality() not in SageZZ:
        from dzack_research.preamble.categories.algebras.sparse_free_algebras import (
            SparseSymmetricAlgebraOf,
        )

        return SparseSymmetricAlgebraOf(module)
    from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
        FinitelyPresentedAlgebra,
    )
    from dzack_research.preamble.categories.algebras.graded_algebras import (
        GradedAlgebras,
    )
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _presentation_matrix,
    )

    base = module.base_ring()
    labels = _finite_labels(module.module_generating_set())
    relation_rows = tuple(_presentation_matrix(module).rows())
    if not relation_rows or not any(any(row) for row in relation_rows):
        algebra = SymmetricAlgebraOn(base, labels)
        algebra._preamble_free_algebra_source_module = module
        return algebra

    # Sage's univariate quotient constructor only accepts monic defining
    # polynomials.  A one-variable symmetric algebra with a torsion relation
    # such as ``2*x`` is instead represented by Sage's one-variable
    # *multivariate* polynomial parent, whose ideal reduction is exact over ZZ.
    if len(labels) == 1:
        presentation_engine = _OwnedPolynomialRing(
            base,
            1,
            names=_variable_names(labels),
        )
        presentation_ring = refine_algebra(
            presentation_engine,
            base,
            labels,
            FreeAlgebras(base),
            GradedFreeAlgebras(base),
            SymmetricAlgebras(base),
        )
    else:
        presentation_ring = SymmetricAlgebraOn(base, labels)

    engine = engine_ring(presentation_ring)
    generators = tuple(engine.gens())
    relations = tuple(
        sum(
            (
                coefficient * generator
                for coefficient, generator in zip(row, generators, strict=True)
                if coefficient
            ),
            engine.zero(),
        )
        for row in relation_rows
    )
    algebra = FinitelyPresentedAlgebra(presentation_ring, relations)
    algebra._preamble_free_algebra_source_module = module
    return refine(
        algebra,
        [
            GradedFreeAlgebras(base),
            SymmetricAlgebras(base),
            CommutativeAlgebras(base),
            GradedAlgebras(base),
        ],
    )


def AlternatingAlgebraOf(module):
    from dzack_research.preamble.categories.algebras.power_algebras import (
        AlternatingAlgebraOf as _alternating_algebra_of,
    )

    return _alternating_algebra_of(module)


def DividedPowerAlgebraOf(module):
    from dzack_research.preamble.categories.algebras.power_algebras import (
        DividedPowerAlgebraOf as _divided_power_algebra_of,
    )

    return _divided_power_algebra_of(module)
