r"""Root lattices, whose isometries are read off the root system.

A root lattice is built from a Cartan matrix, so the root system is what it was
presented by and not something to be recovered from it later.  Recording the
type once, where the lattice is built, is what puts the lattice in this
category -- and the category is what makes $O(L)$ answer from $W(R)$ and the
Dynkin diagram instead of from a search over the Gram matrix.
"""

from typing import Protocol, Self, TYPE_CHECKING

from sage.categories.category import Category
from sage.combinat.root_system.weyl_group import WeylGroup

from dzack_research.preamble.categories.sets.cardinals import Cardinal

if TYPE_CHECKING:
    from sage.combinat.root_system.cartan_type import CartanType
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormedElement
    from dzack_research.preamble.lexicon import ModuleElement
    from dzack_research.preamble.lexicon import RingElement
    from dzack_research.preamble.lexicon import OrderedSet
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphismGroup
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

    class RootLatticeElement(FormedElement, Protocol):
        r"""What an element of a root lattice offers."""


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

        def simple_roots(self: Self) -> "OrderedSet":
            r"""Return the simple roots: the framing generators, under their name.

            ``refine_root_lattice`` is the statement that the Cartan matrix
            became the Gram matrix, so the module generators *are* a simple
            system for the root system this lattice presents.  No choice is
            made here -- the choice was made once, at construction, and this
            is its name.
            """
            return self.module_generators()

        def simple_reflections(self: Self) -> "tuple[ModuleMorphism, ...]":
            r"""Return $(s_{\alpha_1},\dots,s_{\alpha_n})$, the reflections in
            the simple roots, as elements of $\mathrm{Aut}(L)$.

            Each $s_\alpha(x)=x-\dfrac{2\,b(x,\alpha)}{q(\alpha)}\,\alpha$ is
            built by :meth:`IntegralLattices.ParentMethods.reflection` from
            its images on the framing, with the form -- never a matrix
            assembled entrywise -- so each is an isometry by construction and
            an involution by the mathematics.
            """
            return tuple(self.reflection(root) for root in self.simple_roots())

        def fundamental_weights(self: Self) -> "OrderedSet":
            r"""Return $(\omega_1,\dots,\omega_n)\subset L^\vee$, defined by
            $\langle\alpha_i^\vee,\omega_j\rangle=\delta_{ij}$.

            The defining pairing is against the *coroots*, not the roots.
            This category holds the simply laced types, where
            $q(\alpha)=2\varepsilon$ with $\varepsilon=\pm1$ the convention
            sign, so $\alpha^\vee=\varepsilon\,\alpha$ and the weights are the
            dual generators up to that one sign:
            $\omega_j=\varepsilon\,e_j^\vee$.  Like the dual generators
            (:meth:`IntegralLattices.ParentMethods.dual_basis`) they are
            elements of $L^\vee$ -- for a simply laced root system the weight
            lattice *is* the dual of the root lattice.
            """
            norm = self.simple_roots()[0].norm()
            assert norm in (2, -2), (
                f"the simply laced normalization has q(alpha) = ±2; "
                f"this framing has q(alpha) = {norm}"
            )
            duals = self.dual_basis()
            if norm == 2:
                return duals
            return tuple(-weight for weight in duals)

    class ElementMethods:
        r"""The root-system vocabulary of a vector of a root lattice.

        Everything here reads the framing as the simple system, which is what
        membership in this category records.
        """

        def is_root(self: "RootLatticeElement") -> bool:
            r"""Return whether $x$ is a root.

            In a simply laced root lattice the root system is exactly the set
            of vectors of the simple roots' square (CS10 ch. 4 tabulates the
            root lattices this way): norm $-2$ in this project's sign and
            $+2$ after ``twist(-1)``.  Asked of the norm, in the framing's own
            regime, with no enumeration.
            """
            return bool(self.norm() == self.parent().simple_roots()[0].norm())

        def is_positive_root(self: "RootLatticeElement") -> bool:
            r"""Return whether $x$ is a positive root of the simple system.

            A root is positive when its coefficients over the simple roots
            are all nonnegative; every root is positive or negative, never
            mixed, which is the dichotomy the simple system grants.
            """
            return bool(
                self.is_root()
                and all(entry >= 0 for entry in self._coordinates())
            )

        def is_negative_root(self: "RootLatticeElement") -> bool:
            r"""Return whether $-x$ is a positive root."""
            return bool((-self).is_positive_root())

        def height(self: "RootLatticeElement") -> "RingElement":
            r"""Return $\operatorname{ht}(x)=\sum_i c_i$ for $x=\sum_i c_i\,\alpha_i$.

            The coefficient sum over the simple roots.  The framing is the
            simple system, so the sum is read off the coordinates and the
            simple roots have height $1$.
            """
            return sum(self._coordinates())

        def coroot(self: "RootLatticeElement") -> "ModuleElement":
            r"""Return $\alpha^\vee=\dfrac{2}{q(\alpha)}\,\alpha$, transported to $L^\vee$.

            $L$ and $L^\vee$ share no containing space here, so the classical
            $2\alpha/(\alpha,\alpha)$ is read through the correlation: the
            coroot is $\dfrac{2}{q(\alpha)}\,c(\alpha)$, the element of
            $L^\vee$ pairing each $x\in L$ to
            $\dfrac{2\,b(x,\alpha)}{q(\alpha)}$ -- so
            $\langle\alpha,\alpha^\vee\rangle=2$ always.  Defined for
            anisotropic $\alpha$; integrality of the result is exactly the
            root condition, the same one :meth:`reflection` asserts, and the
            division asserts it.
            """
            norm = self.norm()
            assert norm != 0, (
                f"the coroot is defined for an anisotropic vector; "
                f"q(v)=0 for v={self}"
            )
            return (self.parent().correlation()(self) * 2) / norm


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
