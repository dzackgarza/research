r"""Root lattices, whose isometries are read off the root system.

A root lattice is built from a Cartan matrix, so the root system is what it was
presented by and not something to be recovered from it later.  Recording the
type once, where the lattice is built, is what puts the lattice in this
category -- and the category is what makes $O(L)$ answer from $W(R)$ and the
Dynkin diagram instead of from a search over the Gram matrix.
"""

from typing import Self, TYPE_CHECKING

from sage.categories.category import Category
from sage.combinat.root_system.weyl_group import WeylGroup

from dzack_research.preamble.categories.sets.cardinals import Cardinal

if TYPE_CHECKING:
    from sage.combinat.root_system.cartan_type import CartanType
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from dzack_research.preamble.lexicon import RingElement
    from dzack_research.preamble.lexicon import OrderedSet
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphismGroup


def refine_root_lattice(lattice: "FormModule", cartan_type: "CartanType") -> "FormModule":
    r"""Record that ``lattice`` is the root lattice of ``cartan_type``.

    The one crossing.  A presentation is used once, here, where the Cartan
    matrix becomes a Gram matrix; from then on the type is the lattice's own
    and nothing downstream hunts for vectors of square $\pm 2$ to guess it
    back.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.refine import refine
    lattice._cartan_type = cartan_type
    refine(lattice, RootLattices())
    return lattice


class RootLattices(Category):
    r"""Integral lattices presented by the Cartan matrix of a root system.

    Both signs are here.  The root system's own convention makes $A_n$ positive
    definite and this project's makes it negative definite, and the two
    lattices differ by a twist that leaves every isometry alone -- so which one
    a session holds is not a question this category has to ask.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "root lattices"

    def super_categories(self) -> list:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
        return [IntegralLattices()]

    class ParentMethods:
        # Recorded by ``refine_root_lattice`` when the Cartan matrix becomes
        # the Gram matrix; annotation only, so nothing is bound on the class.
        _cartan_type: "CartanType"

        def cartan_type(self: Self) -> "CartanType":
            r"""Return the root system this lattice is the root lattice of."""
            return self._cartan_type

        def twist(self: Self, scale: "RingElement", names: "OrderedSet" = None) -> "FormModule":
            r"""Return $L(n)$, still a root lattice when $n$ is a unit.

            $L(-1)$ is the same root system read with the other sign, which is
            the twist the catalogue applies to every named root lattice.  A
            twist by anything else is not a root lattice -- $E_8(2)$ has no
            vector of square $\pm2$ -- and comes back as the plain integral
            lattice it is.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
            result = IntegralLattices.ParentMethods.twist(self, scale, names)
            if scale in (1, -1):
                refine_root_lattice(result, self.cartan_type())
            return result

        def Aut(self: Self) -> "ModuleAutomorphismGroup":
            r"""Return $O(L)$, the same group, refined into the root-lattice node.

            One object reached one way: this is ``IntegralLattices``' $O(L)$,
            built there and cached there, with one more category on it.  What
            the refinement changes is which algorithm answers -- see
            :meth:`RootLatticeIsometries.ParentMethods.cardinality`.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
            from dzack_research.preamble.refine import refine
            return refine(
                IntegralLattices.ParentMethods.Aut(self),
                RootLatticeIsometries(),
            )

        orthogonal_group = Aut
        automorphisms = Aut


class RootLatticeIsometries(Category):
    r"""$O(L)$ for a root lattice $L$."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "root lattice isometries"

    def super_categories(self) -> list:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_isometries import LatticeIsometries
        return [LatticeIsometries()]

    class ParentMethods:
        if TYPE_CHECKING:
            # $O(L)$ is a homset; ``domain`` is the lattice it acts on.
            def domain(self) -> "FormModule": ...

        def cardinality(self: Self) -> "Cardinal":
            r"""Return $|O(L)|=|W(R)|\cdot|\Gamma(R)|$.

            $O(L)=W(R)\rtimes\Gamma(R)$: the Weyl group, generated by the
            reflections in the roots, is normal in $O(L)$, and the quotient is
            $\Gamma(R)$, the automorphism group of the Dynkin diagram, acting
            by permuting the simple roots (Humphreys sec. 2.11 [Hum90];
            Conway--Sloane ch. 4 [CS10]).  So the order is a product of two
            numbers the root system knows, and neither of them is asked of the
            Gram matrix.

            **Simply laced only**, which is what this category ever holds: the
            lattice constructor names root systems by ``([ADE])(\d+)``.  The
            identity is false in general, because a root system and its root
            lattice come apart once there are two root lengths -- $Q(F_4)$ *is*
            the $D_4$ lattice, so $|O(Q(F_4))|=1152$, while
            $|W(F_4)|\cdot|\Gamma(F_4)|=1152\cdot2=2304$.  A lattice does not
            see which of its isometries the diagram called a length swap.

            The general $O(L)$ is cut out of $GL_n(\mathbb Z)$ by $MGM^t=G$ and
            found by searching short vectors, which is what
            ``group_generators`` still does here and everywhere else.  Nothing
            in that search knows that this $G$ is a Cartan matrix; this
            category is where that is known.
            """
            cartan_type = self.domain().cartan_type()
            weyl_group = WeylGroup(cartan_type, implementation="permutation")
            diagram_automorphisms = cartan_type.dynkin_diagram().automorphism_group(
                edge_labels=True
            )
            return Cardinal(weyl_group.order() * diagram_automorphisms.order())
