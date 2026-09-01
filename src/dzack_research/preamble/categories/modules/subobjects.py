r"""Submodules represented by their chosen inclusion morphisms."""

from sage.misc.cachefunc import cached_function

from sage.modules.free_module import FreeModule as SageFreeModule

from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import refine


class ModuleSubobjects(OwnedCategoryOverBaseRing):
    r"""Modules carrying a chosen monomorphism into another module."""

    @classmethod
    def _repr_object_names(cls):
        return "module subobjects"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def inclusion(self):
            r"""Return the chosen monomorphism representing this subobject."""
            return self._preamble_inclusion

        def embedded_module_generators(self):
            r"""Return the images of the selected module generators."""
            return finite_ordered_set(
                self.inclusion()(module_generator)
                for module_generator in self.module_generators()
            )

        def is_primitive(self) -> bool:
            return self.inclusion().is_primitive()

        is_saturated = is_primitive

        def index(self):
            return self.inclusion().index()

        def orthogonal_complement(self):
            r"""Return the orthogonal complement by deferring to the inclusion."""
            return self.inclusion().orthogonal_complement()

        def sum(self, other):
            r"""Return the join of two subobjects of the same codomain."""
            if self.inclusion().codomain() is not other.inclusion().codomain():
                raise ValueError("a subobject sum requires one common codomain")
            codomain = self.inclusion().codomain()
            return codomain.subobject_on(
                tuple(self.embedded_module_generators())
                + tuple(other.embedded_module_generators())
            )

        def intersection(self, other):
            r"""Return the meet of two subobjects of the same finite free module."""
            if self.inclusion().codomain() is not other.inclusion().codomain():
                raise ValueError("a subobject intersection requires one common codomain")
            codomain = self.inclusion().codomain()
            # The meet is carried by the left half of the left kernel of the
            # induced map (i_self, -i_other) into the direct sum.
            left = self.inclusion().tensor().dual_tensor()
            right = other.inclusion().tensor().dual_tensor()
            kernel = left.stack(-right).left_kernel_tensor()
            left_coefficients = kernel.restricted_to_lower_indices(
                range(left.upper_ranks()[0])
            )
            return codomain.subobject_on(
                _element_from_row(codomain, row)
                for row in (left_coefficients * left).rows()
            )

        def saturation(self):
            r"""Return the primitive closure by deferring to the inclusion."""
            return self.inclusion().saturation()

        def isotropic_reduction(self):
            r"""Return ``S^perp/S`` for an isotropic lattice subobject ``S``."""
            codomain = self.inclusion().codomain()
            from dzack_research.preamble.categories.lattices import Lattices

            if codomain not in Lattices(codomain.base_ring()):
                raise NotImplementedError(
                    "the active descended-form construction currently implements lattice isotropic reduction"
                )
            if any(
                left.b(right) != codomain.base_ring().zero()
                for left in self.module_generators()
                for right in self.module_generators()
            ):
                raise ValueError("isotropic reduction requires an isotropic subobject")

            perpendicular = self.inclusion().orthogonal_complement()
            perpendicular_inclusion = perpendicular.inclusion()
            lifted_images = {
                label: perpendicular_inclusion.lift(
                    self.inclusion()(self.module_generator(label))
                )
                for label in self.module_generating_set()
            }
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
                module_coefficients,
            )

            quotient = module_homset(self, perpendicular)(lifted_images).cokernel()
            if not quotient.is_torsion_free():
                raise ValueError(
                    "the isotropic quotient is not free over the base ring; the selected isotropic subobject is not primitive in its orthogonal complement"
                )
            quotient_module_generators = tuple(quotient.smith_form_module_generators())
            lifts = tuple(
                perpendicular.linear_combination(module_coefficients(module_generator))
                for module_generator in quotient_module_generators
            )
            labels = finite_ordered_set(range(len(lifts)))
            if not lifts:
                return Lattices(codomain.base_ring())(0)
            gram = [
                tuple(left.b(right) for right in lifts)
                for left in lifts
            ]
            return Lattices(codomain.base_ring())(
                gram,
                module_generators=labels,
            )



def _element_from_row(module, row):
    return module.linear_combination(
        {
            label: coefficient
            for label, coefficient in zip(
                module.module_generating_set(), row, strict=True
            )
            if coefficient
        }
    )


def _span_basis_rows(module, module_generating_set):
    from sage.categories.principal_ideal_domains import PrincipalIdealDomains
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_coefficients,
    )

    ring = engine_ring(module.base_ring())
    if ring not in PrincipalIdealDomains():
        raise NotImplementedError(
            "the active finite submodule basis engine currently requires a principal ideal domain"
        )
    labels = tuple(module.module_generating_set())
    rows = []
    for module_generator in module_generating_set:
        element = module_generator if module_generator.parent() is module else module(module_generator)
        coefficients = module_coefficients(element, module)
        rows.append(
            [
                coefficients[label]
                if label in coefficients
                else module.base_ring().zero()
                for label in labels
            ]
        )
    free = SageFreeModule(ring, len(labels))
    if not rows:
        return free.zero_submodule().basis_matrix().rows()
    return free.submodule(rows).basis_matrix().rows()


def module_subobject_on(module, module_generating_set):
    r"""Return the submodule spanned by the specified elements, with its inclusion.

    A subobject of $B$ is the pair $(S, f: S \hookrightarrow B)$, and both
    halves are determined by $B$ together with the submodule the elements
    span.  The span basis is canonical, so it is the datum the subobject is
    constructed on and two calls naming one submodule return one object,
    whichever generating set each was given.
    """
    rows = tuple(tuple(row) for row in _span_basis_rows(module, module_generating_set))
    return _module_subobject_spanning(module, rows)


@cached_function
def _module_subobject_spanning(module, rows):
    r"""Return the subobject of ``module`` on its canonical span basis ``rows``."""
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        FinitelyGeneratedFreeModules,
    )
    from dzack_research.preamble.categories.modules import FreeModuleOn
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_embedding,
    )

    ring = module.base_ring()
    if module not in FinitelyGeneratedFreeModules(ring):
        raise NotImplementedError(
            "the active submodule basis engine constructs subobjects of finite free modules"
        )
    labels = finite_ordered_set(range(len(rows)))

    from dzack_research.preamble.categories.lattices import Lattices
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
        FormModule,
        FormModules,
    )

    match module:
        case _ if module in Lattices(ring):
            if rows:
                from dzack_research.preamble.tensors import tensor

                embedded = tuple(
                    _element_from_row(module, row)
                    for row in rows
                )
                gram = tensor(
                    ring,
                    (),
                    (len(embedded), len(embedded)),
                    [
                        [module.b(left, right) for right in embedded]
                        for left in embedded
                    ],
                )
                source = Lattices(ring)(
                    gram,
                    module_generators=labels,
                )
            else:
                source = Lattices(ring)(0)
        case _ if module in FormModules(ring):
            free_source = FreeModuleOn(ring, labels)
            preliminary = module_embedding(
                free_source,
                module,
                {
                    label: _element_from_row(module, row)
                    for label, row in zip(labels, rows, strict=True)
                },
            )
            source = FormModule(module.form().pullback(preliminary))
        case _:
            source = FreeModuleOn(ring, labels)

    inclusion = module_embedding(
        source,
        module,
        {
            label: _element_from_row(module, row)
            for label, row in zip(labels, rows, strict=True)
        },
    )
    source._preamble_inclusion = inclusion
    return refine(source, ModuleSubobjects(ring))


__all__ = ["ModuleSubobjects", "module_subobject_on"]
