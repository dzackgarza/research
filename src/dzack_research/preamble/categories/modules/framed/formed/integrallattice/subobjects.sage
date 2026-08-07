r"""The module-level subobject category.

A subobject of \(B\) is a module \(S\) carrying a chosen monomorphism
\(\iota:S\hookrightarrow B\).  It is not a wrapper around \(S\), and \(S\) is
not a subset of \(B\): \(S\) is an object of the ambient category like any
other, and this category *mixes in* what the arrow gives it.  Generators,
rank, zero, form, Gram matrix, group, and action are answered by the ambient
category and are never re-declared here.

The abstract ``SubobjectCategory`` (``slice_categories.sage``) supplies
``embedding()`` for a subobject in any \(\mathbf{C}\).  What this file adds
needs cosets, hence an abelian ambient category -- see
:meth:`Subobjects.ParentMethods.index`.
"""

from typing import Self, TYPE_CHECKING

from sage.categories.category import Category

from sage_lattice_category_spike.objects.sets import Sets

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import OrderedSet


class Subobjects(Category):
    r"""Modules carrying a chosen monomorphism into an ambient module."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "subobjects"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        def index(self: Self) -> "Integer":
            r"""Return $[B:S]$, the cardinality of $\operatorname{coker}(\iota)$.

            Sited here and not on the abstract subobject category: an index
            counts the cosets $x+S$, and $x+S=y+S$ is only a statement once
            $x-y\in S$ is one.  That needs the ambient object to be an
            abelian group under the subobject -- an abelian ambient
            category, of which modules are the case this file is about.  A
            subobject of a bare set, of a monoid, or of a scheme has no
            index, which is why the slice category declares none.

            The computation belongs to the arrow: ``ModuleMorphism.index``.
            """
            return self.embedding().index()

        def is_primitive(self: Self) -> bool:
            r"""Return whether this subobject is primitive (saturated) in its codomain.

            The definition, and the single place it is computed: $S\subseteq M$
            is primitive exactly when $M/S$ is torsion free.  Every other
            statement of primitivity in the repo -- an element's, a
            sublattice's -- routes here rather than restating a numerical
            equivalent that happens to hold over $\mathbb Z$ in some
            generating set.

            Torsion free is not free: over a general $R$ the two differ, and
            the definition is the former.
            """
            return self.embedding().cokernel().is_torsion_free()

        is_saturated = is_primitive

        def saturation(self: Self) -> "Subobject":
            r"""Return the primitive closure $S^{\mathrm{sat}}\subseteq M$.

            $S^{\mathrm{sat}}/S=\operatorname{tors}(M/S)$, so
            $S^{\mathrm{sat}}$ is the kernel of
            $M\twoheadrightarrow M/S\twoheadrightarrow(M/S)/\mathrm{tors}$.
            That composite is built from morphisms that already exist and its
            kernel is taken by the morphism, so no call site clears
            denominators or saturates a row lattice by hand.
            """
            inclusion = self.embedding()
            ambient = inclusion.codomain()
            quotient = inclusion.cokernel()
            projection = quotient.torsion_free_quotient()
            return ambient.hom(
                {
                    label: projection(quotient.module_generator(label))
                    for label in ambient.module_generating_set()
                }
            ).kernel()

        def embedded_module_generators(self: Self) -> "OrderedSet":
            r"""Return the images $\iota(e_i)$ of this subobject's generators.

            Not ``module_generators``: those are the abstract $e_i$ this
            module has as an object of the ambient category, and their
            coordinates have length ``rank``.  These are their images in the
            embedding's codomain, whose coordinates have that module's rank.
            """
            return finite_ordered_set(
                tuple(
                    self.embedding()(generator)
                    for generator in self.module_generators()
                )
            )

        def isotropic_reduction(self: Self) -> "Module":
            r"""Return $S^{\perp}/S$ for an isotropic subobject of a formed module."""
            assert self.gram_matrix().is_zero(), (
                "isotropic reduction requires the form to vanish on the subobject"
            )
            codomain = self.embedding_codomain()
            perpendicular = self.embedding().orthogonal_complement()
            inclusion = perpendicular.embedding()
            relations = matrix(
                ZZ,
                [
                    _coordinate_vector(
                        inclusion.lift(image)
                    )
                    for image in self.embedded_module_generators()
                ],
            )
            lifts = _free_quotient_lifts(perpendicular.rank(), relations)
            generators = tuple(
                zipsum(
                    lift,
                    perpendicular.module_generators(),
                    perpendicular.zero(),
                )
                for lift in lifts
            )
            gram = matrix(
                ZZ,
                [
                    [
                        left.b(right)
                        for right in generators
                    ]
                    for left in generators
                ],
            )
            return codomain._sub_form_module(
                gram,
                finite_ordered_set(generators),
            )


def _free_quotient_lifts(rank: "Integer", relations: "MorphismMatrix") -> list:
    from sage.modules.free_module import FreeModule as _sage_free_module

    free = _sage_free_module(ZZ, rank)
    quotient = free / free.submodule(matrix(ZZ, relations).rows())
    return [generator.lift() for generator in quotient.gens()]


def Subobject(embedding: "ModuleMorphism") -> "Module":
    r"""Return $\iota$'s domain, refined into the subobject categories.

    The subobject *is* the domain.  ``Slice`` stores the arrow on it and
    refines it into ``SubObject(codomain)``, the ambient-parameterized slice
    category; the module-level ``Subobjects`` is joined on top for the
    coset-dependent methods.  Nothing wraps the module, so it keeps every
    method its own category gives it.

    The second refine is passed the object's *whole* category and not
    ``Subobjects()`` alone: ``refine`` rebuilds the class from the category
    it is handed, so handing it the leaf alone would drop the module's own
    methods.
    """
    assert isinstance(embedding, (ModuleMorphism, FormMorphism)), (
        "a module subobject is represented by a module or form morphism"
    )
    subobject = Slice(embedding, is_mono=True)
    return refine(subobject, [subobject.category(), Subobjects()])
