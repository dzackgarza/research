r"""Internal Hom modules for the exact finitely presented module backend."""

from sage.modules.fg_pid.fgp_morphism import FGP_Homset, FGP_Morphism

from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
    owned_ring_view,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    EndCategoryConstruction,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import refine


class LinearHomModules(OwnedCategoryOverBaseRing):
    r"""Represented Hom parents closed under pointwise ``R``-linear operations.

    This is the enrichment shared by the full module Hom and by structured
    linear sub-Homs such as equivariant, graded, and cochain maps.  It does not
    claim that the parent contains *all* ``R``-linear maps with its endpoints.
    """

    @classmethod
    def _repr_object_names(cls):
        return "linear Hom modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def source_module(self):
            return self.domain()

        def target_module(self):
            return self.codomain()

        def scalar_multiple(self, scalar, morphism):
            r"""Return the pointwise scalar multiple in this linear Hom."""
            if morphism.parent() is not self:
                morphism = self(morphism)
            scalar = engine_ring(self.base_ring())(scalar)
            return self.elementwise(
                lambda element: self.codomain().scalar_multiple(
                    scalar,
                    morphism(element),
                )
            )

        def as_morphism(self, element):
            return self(element)

        def from_morphism(self, morphism):
            return self(morphism)

        def evaluation(self, map_element, source_element):
            return self(map_element)(source_element)


class LinearEndCategoryConstruction(EndCategoryConstruction):
    r"""Endomorphism rings for categories enriched in ``R``-modules.

    ``End_C(M)`` is the same parent as ``Hom_C(M,M)``.  The End construction
    only records that equal-endpoint Hom as an End object and adds the ring
    structure supplied by pointwise addition and composition.
    """

    def Of(self, obj, codomain=None):
        if codomain is not None and codomain is not obj:
            raise ValueError("an endomorphism category has equal endpoints")
        if obj not in self.base_category():
            raise TypeError("the endomorphism object must lie in the base category")
        endomorphisms = super().Of(obj)
        endomorphisms.attach_end_family(self)
        from dzack_research.preamble.categories.rings import OwnedRings

        refine(endomorphisms, OwnedRings())
        return endomorphisms

    def __contains__(self, candidate) -> bool:
        return hasattr(candidate, "end_family") and candidate.end_family() is self


class InternalHomModules(OwnedCategoryOverBaseRing):
    r"""The canonical full enriched Hom modules ``Hom_R(M,N)``.

    Objects in this category are the actual categorical Hom-sets between
    ``R``-modules.  Their elements are the actual module morphisms.  A finite
    presentation, when computable, is additional structure on this same Hom
    parent rather than a second representation.
    """

    @classmethod
    def _repr_object_names(cls):
        return "internal Hom modules"

    def super_categories(self):
        return [LinearHomModules(self.base_ring())]

    class ParentMethods:
        def inclusion_into_generator_maps(self):
            r"""Return the kernel inclusion into the module of generator assignments."""
            inclusion = self.__dict__.get("_preamble_internal_hom_inclusion")
            if inclusion is None:
                raise NotImplementedError(
                    "this Hom module has no computed finite-presentation inclusion"
                )
            return inclusion


def _native_fgp_morphism(morphism):
    r"""Cross one owned module map to Sage's exact FGP kernel engine."""
    domain = morphism.domain()
    codomain = morphism.codomain()
    optimized, _change = domain.optimized()
    smith_generators = domain.smith_form_gens()
    lifted_images = [morphism(generator).lift() for generator in smith_generators]
    native_linear = optimized.V().hom(lifted_images, codomain.V())
    return FGP_Morphism(FGP_Homset(domain, codomain), native_linear)


def InternalHom(source, target):
    r"""Return the enriched Hom object ``source.Hom(target)``.

    The categorical Hom-set is always the mathematical carrier.  For a
    selected presentation ``F1 -> F0 -> source``, this function additionally
    computes the finite presentation
    ``ker(Hom(F0,target) -> Hom(F1,target))`` and installs that presentation on
    the same Hom parent.  The temporary quotient module is only a computational
    model for the presentation and never escapes as a second Hom object.
    """
    ring = owned_ring_view(source.base_ring())
    if owned_ring_view(target.base_ring()) != ring:
        raise ValueError("an internal Hom requires one common base ring")

    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    homset = module_homset(source, target)
    if homset.__dict__.get("_preamble_internal_hom_model") is not None:
        return homset

    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModules,
    )
    from dzack_research.preamble.categories.modules.framed.framed_modules import (
        FramedModules,
    )

    if (
        source not in FinitelyPresentedModules(ring)
        or target not in FinitelyPresentedModules(ring)
        or source not in FramedModules(ring)
        or target not in FramedModules(ring)
    ):
        return homset

    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        BasedFreeModule,
    )
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModule,
        _presentation_from_relation_rows,
        _presentation_matrix,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_embedding,
    )
    from dzack_research.preamble.categories.abstract_categories import TensorProduct

    source_labels = tuple(source.module_generating_set())
    target_labels = tuple(target.module_generating_set())
    source_relations = _presentation_matrix(source)
    relation_labels = finite_ordered_set(range(source_relations.nrows()))
    generator_free_module = BasedFreeModule(ring, finite_ordered_set(source_labels))
    relation_free_module = BasedFreeModule(ring, relation_labels)

    generator_assignments = TensorProduct(generator_free_module, target)
    relation_assignments = TensorProduct(relation_free_module, target)
    images = {}
    for source_position, source_label in enumerate(source_labels):
        for target_label in target_labels:
            images[(source_label, target_label)] = relation_assignments.linear_combination(
                {
                    (relation_label, target_label): source_relations[relation_label, source_position]
                    for relation_label in relation_labels
                    if source_relations[relation_label, source_position]
                }
            )
    relation_evaluation = module_homset(
        generator_assignments,
        relation_assignments,
    )(images)
    from sage.modules.fg_pid.fgp_module import FGP_Module_class

    if isinstance(generator_assignments, FGP_Module_class) and isinstance(
        relation_assignments, FGP_Module_class
    ):
        kernel = _native_fgp_morphism(relation_evaluation).kernel()
        kernel_relations = kernel._relative_matrix().change_ring(engine_ring(ring))
        kernel_labels = finite_ordered_set(range(int(kernel.V().rank())))
        kernel_relation_labels = finite_ordered_set(range(kernel_relations.nrows()))
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
    homset._install_internal_hom_model(model, inclusion)
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        ModulesWithChosenFinitePresentation,
    )

    return refine(
        homset,
        [
            InternalHomModules(ring),
            ModulesWithChosenFinitePresentation(ring),
        ],
    )


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

    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    return module_homset(source_internal_hom, target_internal_hom)(
        {
            label: target_map
            * source_internal_hom.module_generator(label)
            * source_map
            for label in source_internal_hom.module_generating_set()
        }
    )


__all__ = [
    "InternalHom",
    "InternalHomModules",
    "LinearEndCategoryConstruction",
    "LinearHomModules",
    "internal_hom_morphism",
]
