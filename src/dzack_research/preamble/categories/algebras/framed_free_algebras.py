"""Free algebra constructions on a chosen set of generators."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.algebras import (
    CommutativeAlgebras,
    refine_algebra,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    FreeAlgebraOn,
    FreeAlgebras,
    GradedFreeAlgebras,
    PolynomialRing,
    SymmetricAlgebraOn,
    SymmetricAlgebras,
    TensorAlgebraOn,
    TensorAlgebras,
    _finite_labels,
    _variable_names,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSet,
    finite_ordered_set,
)
from dzack_research.preamble.refine import refine


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



def _has_represented_finite_framing(module) -> bool:
    r"""Return whether the selected framing is finite construction data."""
    ring = module.base_ring()
    from dzack_research.preamble.categories.modules.pure.modules import (
        FinitelyGeneratedFreeModules,
    )
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        ModulesWithChosenFinitePresentation,
    )

    return (
        module in FinitelyGeneratedFreeModules(ring)
        or module in ModulesWithChosenFinitePresentation(ring)
    )

def TensorAlgebraOf(module):
    r"""Return \(T_R(M)\), including the linear relations of ``M``."""
    if not _has_represented_finite_framing(module):
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
    if not _has_represented_finite_framing(module):
        from dzack_research.preamble.categories.algebras.sparse_free_algebras import (
            SparseSymmetricAlgebraOf,
        )

        return SparseSymmetricAlgebraOf(module)
    from dzack_research.preamble.categories.algebras.free_algebras import (
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
    relation_matrix = _presentation_matrix(module)
    if relation_matrix.nrows() == 0 or not any(
        any(row) for row in relation_matrix.rows()
    ):
        algebra = SymmetricAlgebraOn(base, labels)
        algebra._preamble_free_algebra_source_module = module
        return algebra

    # Sage's univariate quotient constructor only accepts monic defining
    # polynomials.  A one-variable symmetric algebra with a torsion relation
    # such as ``2*x`` is instead represented by Sage's one-variable
    # *multivariate* polynomial parent, whose ideal reduction is exact over ZZ.
    if len(labels) == 1:
        presentation_engine = PolynomialRing(
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

    from dzack_research.preamble.categories.sets.set_categories import Sets
    from dzack_research.preamble.categories.sets.indexed_families import indexed_family

    engine = _engine_ring(presentation_ring)
    relation_indices = Sets.Δ[relation_matrix.nrows() - 1]

    def relation_value(index):
        row_position = int(index)
        backend = engine.zero()
        for position in range(relation_matrix.tensor_shape()[1]):
            coefficient = relation_matrix[row_position, position]
            if coefficient:
                backend += _engine_element(base, coefficient) * engine.gen(position)
        return presentation_ring._from_engine_element(backend)

    relations = indexed_family(
        relation_indices,
        relation_value,
        name="Symmetric-algebra defining relations",
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
