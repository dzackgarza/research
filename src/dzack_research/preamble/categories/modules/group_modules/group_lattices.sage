r"""Lattices with a $G$-action: $\mathbb Z[(L,b)]$-modules.

The same thing as an $R[G]$-module, with one condition: $\rho$ lands in $O(L)$
rather than $\operatorname{GL}(L)$ -- which is $\operatorname{Aut}$ in the
category of form modules, so it is not an extra check bolted on but where the
homomorphism goes.

Everything computed here is computed on the module.  The isotypic
decomposition is a statement about $R[G]$-modules and knows nothing about
forms, so the action is handed to the module layer, the components come back
as submodules, and the lattice equips them with the restriction of $b$.  What
the form contributes is not a different computation but two facts about the
answer: the components are mutually orthogonal, so $L_G$ is expressible as
$(L^G)^{\perp}$, and each of them is a lattice rather than a bare module.
"""

from typing import Any

from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.matrix.matrix0 import Matrix
from sage.structure.parent import Parent


class GroupLattices(Category):
    r"""Category of $\mathbb Z[(L,b)]$-modules: a lattice and a $G$-action by isometries.

    Over lattices, not among them.  Two actions on one $L$ are two objects, so
    the action cannot be attached to $L$; and $L$ is not rebuilt to carry one,
    because $\rho$ lands in $O(L)$ -- the automorphism homset of $L$ in the form
    modules -- so its values are isometries of $L$ itself and everything they
    produce is already where it belongs.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattices with a group action"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        r"""What the action adds, all of it about $L$."""

        def forget_action(self: Any) -> Any:
            r"""Return $L$: restriction of scalars along $\mathbb Z\to\mathbb Z[G]$."""
            return self._lattice

        def group(self: Any) -> Any:
            r"""Return $G$."""
            return self._group

        def action_of(self: Any, element: Any) -> Any:
            r"""Return $\rho(g)\in O(L)$, an isometry of $L$."""
            return self._isometries[element]

        def act(self: Any, element: Any, x: Any) -> Any:
            r"""Return $g\cdot x$, for $x$ an element of $L$."""
            return self.action_of(element)(x)

        def is_invariant(self: Any, x: Any) -> bool:
            r"""Return whether $gx=x$ for every $g$."""
            return all(self.act(g, x) == x for g in self.group())

        @cached_method
        def module_representation(self: Any) -> Any:
            r"""Return $\rho$ as a $\mathbb Z[G]$-module: the action, form forgotten.

            Where the isotypic work happens.  A decomposition into isotypic
            components is a statement about modules over a group algebra and
            uses nothing about $b$, so it is asked there, of an object with no
            form to be distracted by.
            """
            module = BasedFreeModule(
                ZZ, standard_framing_set(self.forget_action().rank())
            )
            generator_images = [
                module.Aut()(
                    [
                        module.linear_combination(_coordinate_vector(
                            self.action_of(generator)(basis)
                        ))
                        for basis in self.forget_action().gens()
                    ]
                )
                for generator in self.group().gens()
            ]
            return GroupModule(
                module,
                GroupAction.from_generators(self.group(), module, generator_images),
            )

        def isotypic_decomposition(self: Any) -> Any:
            r"""Return the decomposition of the underlying $\mathbb Z[G]$-module."""
            return self.module_representation().isotypic_decomposition()

        def isotypic_lattice(self: Any, character: Any) -> Any:
            r"""Return the $\chi$-component of $L$, with the restricted form.

            The module computation, equipped: the component is a submodule of
            $\mathbb Z^n$, its generators are read back as elements of $L$, and
            ``subobject_on`` gives them the Gram matrix $b$ restricts to.  That
            restriction may be degenerate -- nothing about being an isotypic
            component prevents it.
            """
            component = self.isotypic_decomposition().component(character)
            return self._equip(component)

        @cached_method
        def invariant_lattice(self: Any) -> Any:
            r"""Return $L^G\hookrightarrow L$: the trivial isotypic component, equipped.

            $\{v: gv=v\ \forall g\}$, which is the $\chi=1$ component of the
            $\mathbb Z[G]$-module and not a separate construction.  Saturated,
            because $nv$ being fixed makes $v$ fixed.
            """
            return self._equip(self.module_representation().invariants())

        @cached_method
        def coinvariant_lattice(self: Any) -> Any:
            r"""Return the formed coinvariants $(L^G)^{\perp L}\hookrightarrow L$.

            This compatibility name remains for the lattice-facing API.
            """
            return self.formed_coinvariants()

        @cached_method
        def formed_coinvariants(self: Any) -> Any:
            r"""Return $(L^G)^{\perp L}\hookrightarrow L$.

            The orthogonal complement is the definition here, so this remains
            computable without choosing a splitting field.  When a semisimple
            decomposition is available, it is the lattice-side realization
            of the nontrivial isotypic summands, with any finite-index glue
            retained in the inclusion.

            $L^G\oplus L_G\subseteq L$ has finite index and is generally
            proper; the quotient is the glue.
            """
            return self.invariant_lattice().embedding().orthogonal_complement()

        def _equip(self: Any, submodule: Any) -> Any:
            r"""Return ``submodule``'s generators as a sublattice of $L$.

            The one step between the two layers: a submodule of $\mathbb Z^n$
            comes back with coordinates, those name elements of $L$, and the
            subobject built on them carries the form.
            """
            lattice = self.forget_action()
            return lattice.subobject_on(
                [
                    lattice.linear_combination(generator._coordinates())
                    for generator in submodule.embedded_gens()
                ]
            )


class GroupLattice(Parent):
    r"""A lattice equipped with an action of a finite group by isometries.

    Holds $L$, $G$ and $\rho$, and nothing else: $\rho$ takes its values in
    $O(L)$, so every element it moves is an element of $L$ and every sublattice
    it produces includes into $L$.  There is no second copy of $L$ here for
    them to live in instead.
    """

    def __init__(self, lattice: Any, group: Any, generator_images: Any) -> None:
        Parent.__init__(self, base=ZZ, category=Sets())
        self._lattice = lattice
        self._group = group
        self._isometries = self._isometries_from(generator_images)
        refine(self, GroupLattices())

    def _isometries_from(self, generator_images: Any) -> dict:
        r"""Return $\rho$ on all of $G$, as elements of $O(L)$.

        Two conditions, neither checked by hand: that each image is an isometry
        is membership in $O(L)$, which the automorphism homset asserts; and
        that the assignment extends to a homomorphism is the module layer's
        word closure, which is where a map out of a group is assembled from its
        values on generators.
        """
        isometry_group = self._lattice.Aut()
        isometries = [
            image if hasattr(image, "domain") else isometry_group(image)
            for image in generator_images
        ]
        module = BasedFreeModule(
            ZZ, standard_framing_set(self._lattice.rank())
        )
        generator_images = [
            module.Aut()(
                [
                    module.linear_combination(_coordinate_vector(image(basis)))
                    for basis in self._lattice.gens()
                ]
            )
            for image in isometries
        ]
        action = GroupAction.from_generators(self._group, module, generator_images)
        return {
            element: isometry_group(
                {
                    basis: self._lattice.linear_combination(
                        _coordinate_vector(action(element)(module_basis))
                    )
                    for basis, module_basis in zip(
                        self._lattice.gens(), module.gens()
                    )
                }
            )
            for element in self._group
        }

    def _repr_(self) -> str:
        return f"{self._lattice} with an action of {self._group}"


def group_lattice(lattice: Any, group: Any, generator_images: Any) -> GroupLattice:
    r"""Return ``lattice`` equipped with the $G$-action ``generator_images`` generates."""
    return GroupLattice(lattice, group, generator_images)
