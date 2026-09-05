r"""Internal Hom modules for the exact finitely presented module backend."""

from sage.misc.cachefunc import cached_function
from sage.modules.fg_pid.fgp_morphism import FGP_Homset, FGP_Morphism

from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    InternalHomModules,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.abstract_categories.constructions import TensorProduct
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    FinitelyPresentedModule,
    _SelectedFinitePresentationModules,
    _presentation_from_relation_rows,
    _presentation_matrix,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
    MatrixSpace,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_embedding,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    ModulesWithChosenFinitePresentation,
    _represented_finite_presentation,
    _tensor_pair,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


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


@cached_function(key=lambda homset: id(homset))
def _internal_hom_model_data(homset):
    r"""Compute the endpoint-determined finite presentation of one Hom parent.

    The Hom parent receives its structural categories when it is constructed.
    This helper only realizes that already-determined presentation lazily; it
    never mutates the Hom parent's category or installs provenance on it.
    """
    source = homset.domain()
    target = homset.codomain()
    ring = _owned_ring(source.base_ring())
    if (
        not _represented_finite_presentation(source)
        or not _represented_finite_presentation(target)
    ):
        raise NotImplementedError(
            "this Hom module has no endpoint-determined finite presentation"
        )

    source_labels = source.module_generating_set()
    target_labels = target.module_generating_set()
    source_relations = _presentation_matrix(source)
    relation_labels = Sets.Δ[source_relations.nrows() - 1]
    generator_free_module = BasedFreeModule(ring, source_labels)
    relation_free_module = BasedFreeModule(ring, relation_labels)

    generator_assignments = TensorProduct(generator_free_module, target)
    relation_assignments = TensorProduct(relation_free_module, target)
    relation_assignment_labels = relation_assignments.module_generating_set()

    def relation_image(pair):
        source_label = pair.component(0)
        target_label = pair.component(1)
        source_position = int(source_labels.rank(source_label))
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

    relation_evaluation = module_homset(
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
        kernel_relations = MatrixSpace(
            ring,
            engine_kernel_relations.nrows(),
            engine_kernel_relations.ncols(),
        ).from_rows(
            tuple(
                tuple(ring._from_engine_element(engine_ring(entry)) for entry in row)
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
        model = FinitelyPresentedModule(kernel_presentation)
        inclusion = module_embedding(
            model,
            generator_assignments,
            {
                label: generator_assignments(
                    kernel(kernel.V().gen(position)).lift()
                )
                for position, label in enumerate(model.module_generating_set())
            },
        )
    else:
        model = relation_evaluation.kernel()
        inclusion = model.inclusion()

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


def InternalHom(source, target):
    r"""Return the canonical enriched Hom object ``source.Hom(target)``."""
    ring = _owned_ring(source.base_ring())
    if _owned_ring(target.base_ring()) != ring:
        raise ValueError("an internal Hom requires one common base ring")
    return module_homset(source, target)


def internal_hom_morphism(source_internal_hom, target_internal_hom, source_map, target_map):
    r"""Return the map on internal Homs induced by pre- and postcomposition.

    ``source_map`` runs from the new source to the old source and
    ``target_map`` from the old target to the new target, so the result is
    ``h |-> target_map * h * source_map``.
    """
    if source_map.codomain() is not source_internal_hom.source_module():
        raise ValueError("precomposition has the wrong codomain")
    if target_map.domain() is not source_internal_hom.target_module():
        raise ValueError("postcomposition has the wrong domain")
    if target_internal_hom.source_module() is not source_map.domain():
        raise ValueError("the target internal Hom has the wrong source")
    if target_internal_hom.target_module() is not target_map.codomain():
        raise ValueError("the target internal Hom has the wrong target")


    return module_homset(source_internal_hom, target_internal_hom).elementwise(
        lambda morphism: target_map * morphism * source_map
    )


__all__ = [
    "InternalHom",
    "InternalHomModules",
    "internal_hom_morphism",
]
