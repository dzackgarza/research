"""Free algebra constructions on a chosen set of generators."""


from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
)
from dzack_research.preamble.categories.algebras.finitely_presented_algebras import _tensor_algebra_from_module_presentation
from dzack_research.preamble.categories.algebras.free_algebras import (
    GradedFreeAlgebras,
    SymmetricAlgebras,
    _symmetric_algebra_on,
    _tensor_algebra_on,
    _native_free_algebra,
    _finite_labels,
    _variable_names,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.algebras.sparse_free_algebras import (
    _sparse_symmetric_algebra_of,
    _sparse_tensor_algebra_of,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import _presentation_matrix
from dzack_research.preamble.categories.modules.pure.modules import ModulesWithChosenFinitePresentation
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
)
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets
def _has_represented_finite_framing(module) -> bool:
    r"""Return whether the selected framing is finite construction data."""
    ring = module.base_ring()

    return module in ModulesWithChosenFinitePresentation(ring)

def _tensor_algebra_of(module):
    r"""Return \(T_R(M)\), including the linear relations of ``M``."""
    if not _has_represented_finite_framing(module):

        return _sparse_tensor_algebra_of(module)

    base = module.base_ring()
    # The presenting tensor algebra is free on the source of M's framing;
    # only its quotient by M's relations has M as its degree-one module.
    generating = module if module in FramedFreeModules(base) else module.framing_source()
    presentation_ring = _tensor_algebra_on(
        base,
        module.module_generating_set(),
        source_module=generating,
    )
    return _tensor_algebra_from_module_presentation(presentation_ring, module)


def _symmetric_algebra_of(module):
    r"""Return \(\operatorname{Sym}_R(M)\) with ``M``'s linear relations."""
    if not _has_represented_finite_framing(module):

        return _sparse_symmetric_algebra_of(module)

    base = module.base_ring()
    labels = _finite_labels(module.module_generating_set())
    relation_matrix = _presentation_matrix(module)
    if relation_matrix.nrows() == 0 or not any(
        relation_matrix[row, column] != base.zero()
        for row in range(relation_matrix.nrows())
        for column in range(relation_matrix.ncols())
    ):
        return _symmetric_algebra_on(base, labels, source_module=module)

    # Sage's univariate quotient constructor only accepts monic defining
    # polynomials.  A one-variable symmetric algebra with a torsion relation
    # such as ``2*x`` is instead represented by Sage's one-variable
    # *multivariate* polynomial parent, whose ideal reduction is exact over ZZ.
    if len(labels) == 1:
        presentation_engine = base.polynomial_ring(1, names=_variable_names(labels))

        presentation_ring = _native_free_algebra(
            _engine_ring(presentation_engine), module.framing_source(), "symmetric",
        )
    else:
        presentation_ring = _symmetric_algebra_on(
            base,
            labels,
            source_module=module.framing_source(),
        )


    engine = _engine_ring(presentation_ring)
    relation_indices = Sets.Δ[relation_matrix.nrows() - 1]

    def relation_value(index):
        row_position = int(index)
        backend = engine.zero()
        for position in range(relation_matrix.ncols()):
            coefficient = relation_matrix[row_position, position]
            if coefficient:
                backend += _engine_element(base, coefficient) * engine.gen(position)
        return presentation_ring._from_engine_element(backend)

    relations = indexed_family(
        relation_indices,
        relation_value,
        name="Symmetric-algebra defining relations",
    )
    return (presentation_ring).quotient_by_relations(relations,
        _extra_categories=(
            GradedFreeAlgebras(base),
            SymmetricAlgebras(base),
            Algebras(base).Associative().Unital().Commutative(),
            GradedAlgebras(base),
        ),
        _generating_module=module,
    )
