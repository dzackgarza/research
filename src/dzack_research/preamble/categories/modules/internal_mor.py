r"""Internal Mor modules for the exact finitely presented module backend.

``Hom_R(M, N)`` for ``M`` with a chosen finite presentation ``F_1 -> F_0 ->
M -> 0`` is the kernel of the evaluation ``N^{gens(M)} -> N^{rels(M)}`` of
relations on generator assignments.  Its endpoints determine it, so the
presented model is computed from the Mor module itself and nothing about its
construction is recorded beside it.
"""

from sage.misc.cachefunc import cached_function
from sage.modules.fg_pid.fgp_morphism import FGP_Homset, FGP_Morphism

from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    _SelectedFinitePresentationModules,
    _presentation_from_relation_rows,
    _presentation_matrix,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    _combined_linearity_decision,
    _module_subobject_inclusion,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    _represented_finite_presentation,
    _tensor_pair,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


class _InternalMorFunctorialMorphism(ModuleMorphism):
    r"""Pre/postcomposition on an internal Mor with its actual linear premises."""

    def __init__(self, parent, source_map, target_map) -> None:
        self._source_map = source_map
        self._target_map = target_map
        super().__init__(
            parent,
            lambda morphism: target_map * morphism * source_map,
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return _combined_linearity_decision((self._source_map, self._target_map))


def _native_fgp_morphism(morphism):
    r"""Cross one owned module map to Sage's exact FGP kernel engine.

    Both endpoints are owned presented modules; their Smith engines are read
    through the presenting category's protected accessor.
    """
    domain = morphism.domain()
    codomain = morphism.codomain()
    domain_engine = domain._smith_engine()
    codomain_engine = codomain._smith_engine()
    optimized, _change = domain_engine.optimized()
    smith_generators = domain_engine.smith_form_gens()
    lifted_images = [
        codomain._to_smith_engine_element(
            morphism(domain._from_smith_engine_element(generator))
        ).lift()
        for generator in smith_generators
    ]
    native_linear = optimized.V().hom(lifted_images, codomain_engine.V())
    return FGP_Morphism(FGP_Homset(domain_engine, codomain_engine), native_linear)


@cached_function(key=lambda source, target: (id(source), id(target)))
def _internal_mor_model_data_from_endpoints(source, target):
    r"""Compute the endpoint-determined finite presentation of ``Hom_R(source,target)``.

    This datum depends only on the two selected endpoint presentations.  In
    particular, it is fixed before the represented Mor parent is constructed;
    realizing the parent later cannot select another presentation.
    """
    ring = _owned_ring(source.base_ring())
    assert _represented_finite_presentation(source) and _represented_finite_presentation(target), (
        f"cannot compute Hom_{ring}({source}, {target}): this algorithm needs both modules to be "
        f"finitely presented with a chosen finite presentation, but {source} is in {source.category()} "
        f"and {target} is in {target.category()}"
    )

    source_labels = source.module_generating_set()
    target.module_generating_set()
    source_relations = _presentation_matrix(source)
    relation_labels = Sets.Δ[source_relations.nrows() - 1]
    generator_free_module = ring.free_module(source_labels)
    relation_free_module = ring.free_module(relation_labels)

    modules = Modules(ring)
    generator_assignments = modules.tensor_product((generator_free_module, target))
    relation_assignments = modules.tensor_product((relation_free_module, target))
    relation_assignment_labels = relation_assignments.module_generating_set()

    def relation_image(pair):
        source_label = pair.component(0)
        target_label = pair.component(1)
        source_position = int(source_labels.ranking_map()(source_label))
        return relation_assignments.linear_combination(
            {
                _tensor_pair(
                    relation_assignment_labels,
                    relation_label,
                    target_label,
                ): source_relations[relation_label, source_position]
                for relation_label in relation_labels
                if source_relations[relation_label, source_position]
            }
        )

    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        _auxiliary_linear_module_mor,
    )

    relation_evaluation = _auxiliary_linear_module_mor(
        generator_assignments,
        relation_assignments,
    )(relation_image)
    if (
        generator_assignments in _SelectedFinitePresentationModules(ring)
        and relation_assignments in _SelectedFinitePresentationModules(ring)
        and generator_assignments._smith_engine() is not None
        and relation_assignments._smith_engine() is not None
    ):
        kernel = _native_fgp_morphism(relation_evaluation).kernel()
        engine_ring = _engine_ring(ring)
        engine_kernel_relations = kernel._relative_matrix().change_ring(engine_ring)
        kernel_relations = ring.matrix_space(engine_kernel_relations.nrows(), engine_kernel_relations.ncols()).from_rows(
            tuple(
                tuple(_owned_engine_element(ring, engine_ring(entry)) for entry in row)
                for row in engine_kernel_relations.rows()
            )
        )
        kernel_labels = Sets.Δ[int(kernel.V().rank()) - 1]
        kernel_relation_labels = Sets.Δ[engine_kernel_relations.nrows() - 1]
        kernel_presentation = _presentation_from_relation_rows(
            ring,
            kernel_labels,
            kernel_relation_labels,
            kernel_relations,
        )
        model = kernel_presentation.cokernel()
        inclusion = _module_subobject_inclusion(
            _auxiliary_linear_module_mor(model, generator_assignments),
            {
                label: generator_assignments(
                    kernel(kernel.V().gen(position)).lift()
                )
                for position, label in enumerate(model.module_generating_set())
            },
        )
    else:
        model = relation_evaluation.kernel()
        construction = model.module_subobject_construction()
        ambient = construction.ambient_module()
        images = construction.generator_images()
        assert ambient is not None and images is not None, (
            f"cannot compute Hom_{ring}({source}, {target}) as a kernel: the kernel {model} was "
            "returned without its inclusion into the module of generator assignments"
        )
        lift = construction.selected_lift()
        inclusion = _module_subobject_inclusion(
            _auxiliary_linear_module_mor(model, ambient),
            images,
            lift=(None if lift is None else lambda element: lift(model, element)),
        )

    relation_matrix = _presentation_matrix(model)
    presentation = (
        model.presentation()
        if model in _SelectedFinitePresentationModules(model.base_ring())
        else _presentation_from_relation_rows(
            model.base_ring(),
            model.module_generating_set(),
            Sets.Δ[relation_matrix.nrows() - 1],
            relation_matrix,
        )
    )
    return model, inclusion, relation_matrix, presentation


def _internal_mor_model_data(mor):
    r"""Return the endpoint-fixed selected presentation data of this Mor parent."""
    return _internal_mor_model_data_from_endpoints(mor.domain(), mor.codomain())


def _internal_mor_morphism(
    source_map,
    target_map,
    *,
    source_internal_mor=None,
    target_internal_mor=None,
):
    r"""Return the internal-Mor map induced by pre- and postcomposition."""
    if source_internal_mor is None:
        source = source_map.codomain()
        source_internal_mor = source.module_category().Mor(
            source,
            target_map.domain(),
        )
    if target_internal_mor is None:
        source = source_map.domain()
        target_internal_mor = source.module_category().Mor(
            source,
            target_map.codomain(),
        )
    if source_map.codomain() is not source_internal_mor.source_module():
        raise ValueError(
            f"cannot precompose with {source_map}: its codomain {source_map.codomain()} is not the "
            f"source {source_internal_mor.source_module()} of {source_internal_mor}"
        )
    if target_map.domain() is not source_internal_mor.target_module():
        raise ValueError(
            f"cannot postcompose with {target_map}: its domain {target_map.domain()} is not the "
            f"target {source_internal_mor.target_module()} of {source_internal_mor}"
        )
    if target_internal_mor.source_module() is not source_map.domain():
        raise ValueError(
            f"{target_internal_mor} is not Hom({source_map.domain()}, {target_map.codomain()}): its "
            f"source is {target_internal_mor.source_module()}, not the domain of {source_map}"
        )
    if target_internal_mor.target_module() is not target_map.codomain():
        raise ValueError(
            f"{target_internal_mor} is not Hom({source_map.domain()}, {target_map.codomain()}): its "
            f"target is {target_internal_mor.target_module()}, not the codomain of {target_map}"
        )

    return _InternalMorFunctorialMorphism(
        source_internal_mor.module_category().Mor(
            source_internal_mor,
            target_internal_mor,
        ),
        source_map,
        target_map,
    )


__all__ = [
    "_internal_mor_model_data",
]
