r"""Parabolic subgroups of primitive isotropic subobjects, and their Levi data.

Let ``iota: I -> L`` be a primitive totally isotropic subobject of a lattice.
Its parabolic subgroup is the stabilizer

``P_I = Stab_{O(L)}(I) = {g in O(L) : g(iota(I)) = iota(I)}``.

Every ``g`` in ``P_I`` preserves ``I^perp`` as well, so it restricts along
``iota`` and descends to the isotropic reduction, giving two group morphisms
out of ``P_I``.  Writing ``K_I = I^perp/I``,

``1 -> U_I -> P_I -> M_I -> 1``,   ``M_I <= GL(I) x O(K_I)``,

where ``U_I`` is the common kernel: the isometries acting as the identity on
``I`` and on ``K_I``.  Membership in ``U_I`` is decided from that definition,
without constructing the quotient: ``g`` acts trivially on ``I^perp/I``
exactly when ``(g - 1)(I^perp)`` lies in ``iota(I)``.

For ``rank(I) = 1`` the ``O(L)``-orbit of ``I`` is a cusp, ``P_I`` is that
cusp's arithmetic stabilizer, and ``K_I = v^perp/v`` is the lattice whose
reflection group acts on the cusp's fundamental domain.  This is the object in
which the Sterk simple-root counts are compared: one count is taken under the
full reflection group ``W(K_I)`` of ``K_I``, the other under a reflection
subgroup of it, and the two group actions are what differ.

The Levi target ``GL(I) x O(K_I)`` is delivered here by its two components
separately.  ``levi_restriction`` lands in ``GL(I)``, the module
automorphisms of ``I``: the form ``I`` inherits is identically zero, so its
isometry group is all of ``GL(I)`` and nothing smaller is being asserted.
``levi_quotient_action`` lands in the module automorphisms of the represented
cokernel ``I^perp/I``.  Whether that automorphism is an isometry of the
induced form is the statement ``O(K_I)`` makes, and stating it needs the
projection ``I^perp ->> K_I`` that the owned ``isotropic_reduction`` does not
return; see ``isotropic_quotient_projection`` below.
"""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_embedding,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import ModuleSubobjects
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.refine import refine


class PrimitiveIsotropicSubobjects(OwnedCategoryOverBaseRing):
    r"""Primitive totally isotropic subobjects of a lattice over ``R``.

    Membership states two facts about the chosen monomorphism ``iota``: the
    form of the codomain restricts to zero along it, and its cokernel is
    torsion free.  Both are checked at admission by ``primitive_isotropic``.
    """

    @classmethod
    def _repr_object_names(cls):
        return "primitive totally isotropic subobjects"

    def an_object(self):
        r"""The isotropic line spanned by the first generator of ``U``."""
        from dzack_research.preamble.categories.lattices import Lattices

        plane = Lattices(self.base_ring())("U")
        return primitive_isotropic(plane, (plane.module_generators()[0],))

    def super_categories(self):
        return [ModuleSubobjects(self.base_ring())]

    class ParentMethods:
        def is_totally_isotropic(self) -> bool:
            r"""Return whether the codomain's form restricts to zero along the inclusion."""
            lattice = self.ambient_module()
            zero = lattice.base_ring().zero()
            embedded = self.embedded_module_generators()
            labels = self.module_generating_set()
            return all(
                lattice.b(embedded[left], embedded[right]) == zero
                for left in labels
                for right in labels
            )

        def ambient_lattice(self):
            r"""Return the lattice this isotropic subobject sits in."""
            return self.inclusion().codomain()

        @cached_method
        def isotropic_perpendicular(self):
            r"""Return ``I^perp`` as a subobject of the same lattice.

            The subobject is totally isotropic, so ``I <= I^perp``: this is
            the flag whose successive quotient is the isotropic reduction.
            """
            return self.inclusion().orthogonal_complement()

        @cached_method
        def into_perpendicular(self):
            r"""Return ``I -> I^perp``, the inclusion factored through its own perpendicular."""
            perpendicular = self.isotropic_perpendicular()
            lift = perpendicular.inclusion().lift
            inclusion = self.inclusion()
            return module_embedding(
                self,
                perpendicular,
                {
                    label: lift(inclusion(self.module_generator(label)))
                    for label in self.module_generating_set()
                },
            )

        @cached_method
        def isotropic_quotient(self):
            r"""Return the represented module ``I^perp/I``.

            This is the underlying module of ``self.isotropic_reduction()``,
            which is the same quotient carrying the form ``I^perp`` induces
            on it.  The two ranks are asserted to agree.
            """
            quotient = self.into_perpendicular().cokernel()
            assert quotient.rank() == self.isotropic_reduction().rank(), (
                "the represented cokernel of I -> I^perp and the owned isotropic "
                "reduction I^perp/I must have the same rank"
            )
            return quotient

        def isotropic_quotient_projection(self):
            r"""Return the projection ``I^perp ->> I^perp/I``.

            The owned ``isotropic_reduction`` returns the quotient lattice
            ``K_I`` but not this map, so the descent of a parabolic element is
            expressed here on the represented cokernel.
            """
            return self.isotropic_quotient().presentation_projection()

        def stabilizes(self, automorphism) -> bool:
            r"""Return whether ``automorphism`` carries this subobject onto itself.

            Both ``g`` and ``g^{-1}`` are asked to send the selected
            generators into the image, so the answer is the set equality
            ``g(I) = I`` and not the inclusion ``g(I) <= I``.
            """
            inclusion = self.inclusion()
            inverse = ~automorphism
            embedded = self.embedded_module_generators()
            return all(
                inclusion.is_in_image(automorphism(embedded[label]))
                and inclusion.is_in_image(inverse(embedded[label]))
                for label in self.module_generating_set()
            )

        @cached_method
        def parabolic_subgroup(self):
            r"""Return ``P_I = Stab_{O(L)}(I)`` as a predicate subgroup of ``O(L)``."""
            from dzack_research.preamble.categories.group.predicate_subgroups import (
                predicate_subgroup,
            )

            return predicate_subgroup(
                self.ambient_lattice().Aut(),
                self.stabilizes,
                f"g maps {self} onto itself",
            )

        def levi_restriction(self, automorphism):
            r"""Return ``g|_I`` in ``GL(I)`` for ``g`` in the parabolic subgroup."""
            assert self.stabilizes(automorphism), (
                "the restriction along iota is defined for an isometry stabilizing "
                "this isotropic subobject"
            )
            inclusion = self.inclusion()
            return module_homset(self, self)(
                {
                    label: inclusion.lift(
                        automorphism(inclusion(self.module_generator(label)))
                    )
                    for label in self.module_generating_set()
                }
            )

        def levi_quotient_action(self, automorphism):
            r"""Return the descent of ``g`` to ``I^perp/I`` for ``g`` in ``P_I``."""
            assert self.stabilizes(automorphism), (
                "the descent to I^perp/I is defined for an isometry stabilizing "
                "this isotropic subobject"
            )
            perpendicular = self.isotropic_perpendicular()
            perpendicular_inclusion = perpendicular.inclusion()
            projection = self.isotropic_quotient_projection()
            quotient = self.isotropic_quotient()
            return module_homset(quotient, quotient)(
                {
                    label: projection(
                        perpendicular_inclusion.lift(
                            automorphism(
                                perpendicular_inclusion(
                                    perpendicular.module_generator(label)
                                )
                            )
                        )
                    )
                    for label in perpendicular.module_generating_set()
                }
            )

        def acts_trivially_on_isotropic_reduction(self, automorphism) -> bool:
            r"""Return whether ``(g - 1)(I^perp)`` lies in ``iota(I)``.

            This is the definition of acting as the identity on ``I^perp/I``,
            decided on ``I^perp`` itself, so no quotient is constructed.
            """
            inclusion = self.inclusion()
            perpendicular = self.isotropic_perpendicular()
            perpendicular_inclusion = perpendicular.inclusion()
            return all(
                inclusion.is_in_image(automorphism(embedded) - embedded)
                for embedded in (
                    perpendicular_inclusion(perpendicular.module_generator(label))
                    for label in perpendicular.module_generating_set()
                )
            )

        @cached_method
        def unipotent_radical(self):
            r"""Return ``U_I``, the kernel of ``P_I -> GL(I) x O(I^perp/I)``."""
            from dzack_research.preamble.categories.group.predicate_subgroups import (
                predicate_subgroup,
            )

            inclusion = self.inclusion()
            embedded = self.embedded_module_generators()
            labels = self.module_generating_set()

            def is_unipotent(automorphism) -> bool:
                if not self.stabilizes(automorphism):
                    return False
                if any(
                    automorphism(embedded[label]) != embedded[label]
                    for label in labels
                ):
                    return False
                return self.acts_trivially_on_isotropic_reduction(automorphism)

            assert inclusion.codomain() is self.ambient_lattice(), (
                "the unipotent radical is cut out inside the orthogonal group of "
                "the lattice this subobject includes into"
            )
            return predicate_subgroup(
                self.ambient_lattice().Aut(),
                is_unipotent,
                f"g acts as the identity on {self} and on its isotropic reduction",
            )

        def eichler_transvection(self, orthogonal_vector):
            r"""Return the Eichler transvection ``E_{f,x}`` of this isotropic line.

            For the selected generator ``f`` of a rank-one isotropic subobject
            and ``x`` in ``f^perp``,

            ``E_{f,x}(y) = y + b(y,x) f - (q(x)/2) b(y,f) f - b(y,f) x``.

            The framing supplies ``f``: the transvection depends on the chosen
            generator and not only on the line, since ``E_{-f,x} = E_{f,-x}``.
            The coefficient ``q(x)/2`` is integral because ``x`` lies in an
            even lattice, which is asserted.

            ``E_{f,x}`` fixes ``f`` and satisfies ``(E_{f,x} - 1)(f^perp) <=
            Z f``, so it lies in ``unipotent_radical()``.  The assignment
            ``x -> E_{f,x}`` is a group morphism from ``(f^perp, +)`` killing
            ``f``, hence a morphism from ``f^perp/f``.
            """
            lattice = self.ambient_lattice()
            ring = lattice.base_ring()
            assert int(self.rank()) == 1, (
                "an Eichler transvection is attached to a rank-one isotropic subobject"
            )
            assert lattice.is_even(), (
                "the Eichler transvection's coefficient q(x)/2 is integral on an "
                "even lattice; this lattice is not even"
            )
            isotropic_vector = self.embedded_module_generators()[
                self.module_generating_set()[0]
            ]
            assert (
                lattice.b(isotropic_vector, orthogonal_vector) == ring.zero()
            ), "an Eichler transvection takes a vector orthogonal to its isotropic vector"
            square = lattice.q(orthogonal_vector)
            half_square = square // ring(2)
            assert ring(2) * half_square == square, (
                "q(x) is odd here, so E_{f,x} would not preserve the lattice"
            )

            def image(label):
                source = lattice.module_generator(label)
                against_x = lattice.b(source, orthogonal_vector)
                against_f = lattice.b(source, isotropic_vector)
                return (
                    source
                    + lattice.scalar_multiple(
                        against_x - half_square * against_f, isotropic_vector
                    )
                    - lattice.scalar_multiple(against_f, orthogonal_vector)
                )

            return lattice.Aut()(
                {label: image(label) for label in lattice.module_generating_set()}
            )

        def unipotent_group_generators(self):
            r"""Return the Eichler transvections on a framing of ``f^perp``.

            For a rank-one isotropic subobject these generate ``U_I``: the
            unipotent radical is the image of the morphism ``f^perp/f ->
            O(L)``, and the selected generators of ``f^perp`` generate that
            quotient.
            """
            from dzack_research.preamble.categories.sets.indexed_families import (
                finite_indexed_family,
            )

            perpendicular = self.isotropic_perpendicular()
            perpendicular_inclusion = perpendicular.inclusion()
            return finite_indexed_family(
                perpendicular.module_generating_set(),
                lambda label: self.eichler_transvection(
                    perpendicular_inclusion(perpendicular.module_generator(label))
                ),
                name=f"Eichler transvections of {self}",
            )

        def is_equivalent_to(self, other) -> bool:
            r"""Return whether ``O(L)`` carries this isotropic subobject to ``other``.

            The decision is the exact indefinite backend's; where its
            hypotheses do not hold, that backend states the absence rather
            than searching the group.
            """
            return self.transporter_witness_to(other) is not None

        def transporter_witness_to(self, other):
            r"""Return one ``g`` in ``O(L)`` with ``g(I) = other``, or ``None``.

            The full transporter is the coset ``g P_I``, which is infinite
            whenever ``P_I`` is; one witness together with
            ``parabolic_subgroup`` presents it.
            """
            assert other.ambient_lattice() is self.ambient_lattice(), (
                "an isotropic transporter compares two subobjects of one lattice"
            )
            return self.ambient_lattice().Aut().isotropic_equivalence_witness(
                self, other
            )


def primitive_isotropic(lattice, module_generating_set):
    r"""Return the primitive totally isotropic subobject spanned by the stated elements.

    Both admission conditions are decided before the subobject is refined, so
    a refused span leaves no wrongly placed object behind in the subobject
    cache.
    """
    subobject = lattice.subobject_on(module_generating_set)
    assert subobject.is_primitive(), (
        "a primitive isotropic subobject has torsion-free cokernel; the stated "
        "span is not saturated in its lattice"
    )
    zero = lattice.base_ring().zero()
    embedded = subobject.embedded_module_generators()
    labels = subobject.module_generating_set()
    assert all(
        lattice.b(embedded[left], embedded[right]) == zero
        for left in labels
        for right in labels
    ), "the stated span is not totally isotropic for the lattice form"
    return refine(subobject, PrimitiveIsotropicSubobjects(lattice.base_ring()))


__all__ = ["PrimitiveIsotropicSubobjects", "primitive_isotropic"]
