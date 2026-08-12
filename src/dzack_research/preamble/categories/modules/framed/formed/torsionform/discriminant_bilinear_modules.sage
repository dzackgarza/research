r"""Discriminant bilinear modules."""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Module

from sage.rings.integer_ring import ZZ as SageZZ
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from sage.categories.morphism import Morphism
    from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism

from typing import Protocol, TYPE_CHECKING

from sage.categories.category import Category
from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.matrix.matrix0 import Matrix

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    class DiscriminantBilinearParent(Protocol):
        r"""What an object of this category offers."""

        def forget_form(self) -> "Module": ...
        def form(self) -> "BilinearFormMorphism": ...
        def smith_form_module_generators(self) -> "OrderedSet": ...
        def regenerate(self, module_generators: "OrderedSet") -> "FormModule": ...

    class DiscriminantBilinearElement(Protocol):
        r"""What an element of such an object offers."""

        def parent(self) -> "DiscriminantBilinearParent": ...
        def forget_form(self) -> "Element": ...
        def q(self) -> "Element": ...
        def b(self, other: "Element") -> "Element": ...


class DiscriminantBilinearModules(Category):
    r"""Category of discriminant bilinear modules.

    The category's ``gram_matrix`` is the bilinear Gram matrix. Quadratic
    discriminant modules expose their associated bilinear form through
    :meth:`associated_bilinear_form`.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "discriminant bilinear modules"

    def super_categories(self) -> list:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import SymmetricBilinearFormModules
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import TorsionModulesWithForm
        return [
            TorsionModulesWithForm(),
            SymmetricBilinearFormModules(),
        ]

    def from_module(self, module: "Module", gram: Matrix) -> "FormModule":
        r"""Return the torsion form on ``module`` with Gram matrix ``gram``.

        The construction the category is for: a finitely presented torsion
        module -- a group with a chosen generating set, living in this universe
        rather than converted into it -- and the matrix of the form with
        respect to that generating set.  Nothing else is needed and nothing
        else is consulted.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.forms.forms import BilinearForm
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import FinitelyPresentedTorsionModules
        from dzack_research.preamble.refine import refine
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import subdivide_form_gram_matrix
        assert module in FinitelyPresentedTorsionModules(), (
            "a discriminant form requires a finitely presented torsion module"
        )
        assert gram.is_symmetric(), (
            "a discriminant bilinear form is symmetric"
        )
        relations = module.relation_matrix()._sage_matrix().change_ring(SageZZ)
        assert all(entry in SageZZ for entry in (relations * gram).list()), (
            "b is not defined on the classes: some relation does not pair "
            "integrally with the module_generators"
        )
        form = BilinearForm(module, QmodnZ(1), gram)
        refine(form, self)
        subdivide_form_gram_matrix(form)
        return form

    def from_relations_and_gram(self, relations: Matrix, gram: Matrix) -> "FormModule":
        r"""Return the torsion bilinear form $(G,b)$ built from data alone.

        The independent construction, and the one every other route ends
        at: a finitely presented torsion module -- a chosen generating set
        and the relations among it -- together with the matrix of b
        with respect to that generating set.  Nothing here refers to a
        morphism, a lattice, or a cover, because a torsion form does not
        have any; it exists exactly as a lattice given by a Gram matrix
        exists.

        The assertions are the category's axioms, read on the relations: $b$ descends to the
        classes exactly when a relation pairs integrally with every generator.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import FinitelyPresentedTorsionModules
        module = FinitelyPresentedTorsionModules().from_relations(relations)
        return self.from_module(module, gram)

    def cokernel(self, morphism: "Morphism") -> "FormModule":
        r"""Return $\operatorname{coker} f$ for $f$ of finite index, as an object here.

        No second morphism appears: $f$ *is* the presentation, so it is handed
        to the module as such, and the refinements are about what $f$ happens
        to be -- a map of lattices, or a correlation -- rather than about extra
        data being carried alongside.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.forms.forms import BilinearForm
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import TorsionModule
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import cokernel_categories
        from dzack_research.preamble.refine import refine
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import subdivide_form_gram_matrix
        assert isinstance(morphism, FormMorphism), (
            "a cokernel form is constructed from a form morphism"
        )
        module = TorsionModule(morphism)
        gram = morphism.codomain().form().gram_matrix()
        # No check that the form descends.  For an R-lattice L, the
        # discriminant group A_L = L^v/L carries an induced K/R-valued
        # bilinear form -- that is a theorem, and b(L, L^v) subset R is the
        # definition of L^v, not a property of this particular L.  The check
        # that stood here re-derived it for every pair of generators, on the
        # path that renders a lattice.
        form = BilinearForm(module, QmodnZ(1), gram)
        refine(form, [self] + cokernel_categories(morphism))
        subdivide_form_gram_matrix(form)
        return form

    class ParentMethods:
        r"""Methods available on discriminant bilinear modules."""

        def regenerate(self: "DiscriminantBilinearParent", module_generators: "OrderedSet") -> "FormModule":
            r"""Return this form on the generating set ``module_generators``.

            A different generating set is a different object of this category,
            so this is a construction and not a view: the same pairings, read
            on a new set, presented by the morphism that set induces.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import FinitelyPresentedTorsionModules
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import regenerating_data
            module_generators = tuple(module_generators)
            relations, gram = regenerating_data(self, module_generators)
            module = FinitelyPresentedTorsionModules().from_relations(
                relations,
                finite_ordered_set(module_generators),
            )
            return DiscriminantBilinearModules().from_module(module, gram)

        def form_vanishes_on(self: "DiscriminantBilinearParent", elements: "OrderedSet") -> bool:
            r"""Return whether $b$ is zero on every pair drawn from ``elements``.

            A pairing takes two arguments, so vanishing is a statement about
            pairs and not about norms: $b(x,x)=0$ for every $x$ in a subgroup
            leaves $b(x,y)$ two-torsion rather than zero, and
            $(\mathbb Z/2)^2$ with $b(x,y)=1/2$ off the diagonal is a group
            where every element is its own zero and the form does not vanish.
            """
            return all(
                left.b(right) == 0
                for left in elements
                for right in elements
            )

        def associated_quadratic_form(self: "DiscriminantBilinearParent") -> "QuadraticFormMorphism":
            r"""Return the discriminant quadratic form on the same group.

            $b$ does not determine $q$: the refinement
            $q:A_L\to\mathbb Q/2\mathbb Z$ exists exactly when $L$ is even,
            because moving a lift by $\ell\in L$ shifts $b(\tilde x,\tilde x)$
            by $b(\ell,\ell)$, which lies in $2\mathbb Z$ only then.  So this
            passage goes back through the lattice, unlike
            :meth:`~DiscriminantQuadraticModules.ParentMethods.associated_bilinear_form`,
            which polarizes $q$ and needs nothing else.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_quadratic_modules import DiscriminantQuadraticModules
            return DiscriminantQuadraticModules().from_module(
                self.forget_form(),
                self.form().polar_form().gram_matrix(),
            )

        def _form_matrix_latex_label(self: "DiscriminantBilinearParent") -> str:
            r"""Return the LaTeX label for the bilinear Gram matrix."""
            return "G_{b_{A_L}}"

        def invariant_factor_form(self: "DiscriminantBilinearParent") -> "FormModule":
            r"""Return $b$ on module_generators from the invariant factor decomposition.

            The same cokernel of the same $c$, so the same $b$; what changes is the
            generating set, and with it the object.  The change merges factors
            across summands -- $A_{A_2\oplus A_3}$ lands on one generator as
            $\mathbb Z/12$ rather than on two as $\mathbb Z/3\oplus\mathbb Z/4$ --
            so no decomposition of $L$ survives it.
            """
            return self.regenerate(self.smith_form_module_generators())

        def normal_form(self: "DiscriminantBilinearParent") -> "FormModule":
            r"""Return $b$ on $p$-adic Jordan module_generators -- again a different object.

            The module_generators are the Jordan ones prime by prime, cutting out their own
            orthogonal blocks (Peters--Sterk Def. 11.2.2, Prop. 11.2.3 [PS24]).  For
            odd $p$ they are unique: Prop. 11.1.3 makes the discriminant-form map a
            bijection onto $p$-primary symmetric torsion forms of that length, and
            the blocks are the $\oplus^{r-1}\langle p^{-k}\rangle\oplus\langle
            \epsilon p^{-k}\rangle$ of Prop. 9.4.1.  At $p=2$ existence holds but
            uniqueness does not -- the isometries I--IV of Sec. 11.2 still relate
            distinct normal forms, and the reduced normal form that settles them
            (Cor. C.3.2) is built from the Gauss-sum index invariants of App. C.2,
            which are defined from $q$ and have no $b$ analogue.  So this is *a*
            normal form, not *the* one.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import p_adic_jordan_module_generators
            return self.regenerate(p_adic_jordan_module_generators(self))


    class ElementMethods:
        r"""Methods available on elements of discriminant bilinear modules.

        An element is a coset $\bar x = x + f(L)$; $b(\bar x,\bar y)$ is the
        pairing of any two lifts, read in $\mathbb Q/\mathbb Z$ because moving
        a lift by $f(\ell)$ shifts it by $b(\ell', \ell)\in\mathbb Z$.  That is
        already what a form module's element does, so there is nothing to add.
        """
