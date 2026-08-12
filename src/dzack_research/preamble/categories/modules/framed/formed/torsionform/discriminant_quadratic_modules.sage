r"""Discriminant quadratic modules.

A sibling of :mod:`discriminant_bilinear_modules`, not a refinement of it.  A
quadratic torsion module's data is $q$; $b_q$ is derived from it by
polarization, which is a functor and not an inclusion -- distinct $q$ can share
a $b$ (Peters--Sterk Sec. 12.5 [PS24]), so an object cannot be both.

Objects use the shared formed-module representation and are distinguished by
membership in :class:`DiscriminantQuadraticModules`.  Sage's
``TorsionQuadraticModule`` carries $b$ and $q$ together and is not refined into
this category.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.lexicon import Module

from sage.rings.integer_ring import ZZ as SageZZ
if TYPE_CHECKING:
    from dzack_research.preamble.categories.forms.forms import BilinearFormMorphism
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from sage.categories.morphism import Morphism
    from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism

from typing import Self, TYPE_CHECKING

from sage.categories.category import Category
from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.matrix.matrix0 import Matrix
from sage.rings.rational_field import QQ as SageQQ

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet


class DiscriminantQuadraticModules(Category):
    r"""Category of discriminant quadratic modules.

    Its objects carry $q:A\to\mathbb Q/2\mathbb Z$; the polarization
    $b_q:A\times A\to\mathbb Q/\mathbb Z$ is reachable through
    :meth:`~DiscriminantQuadraticModules.ParentMethods.associated_bilinear_form`,
    which lands in the sibling category.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "discriminant quadratic modules"

    def super_categories(self) -> list:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import QuadraticFormModules
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import TorsionModulesWithForm
        return [TorsionModulesWithForm(), QuadraticFormModules()]

    def from_module(self, module: "Module", gram: Matrix) -> "FormModule":
        r"""Return the torsion form on ``module`` with Gram matrix ``gram``.

        The construction the category is for: a finitely presented torsion
        module -- a group with a chosen generating set, living in this universe
        rather than converted into it -- and the matrix of the form with
        respect to that generating set.  Nothing else is needed and nothing
        else is consulted.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import FinitelyPresentedTorsionModules
        from dzack_research.preamble.categories.forms.forms import QuadraticForm
        from dzack_research.preamble.refine import refine
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import subdivide_form_gram_matrix
        assert module in FinitelyPresentedTorsionModules(), (
            "a discriminant form requires a finitely presented torsion module"
        )
        relations = module.relation_matrix()._sage_matrix().change_ring(SageZZ)
        assert all(entry in SageZZ for entry in (relations * gram).list()), (
            "the polarization is not defined on the classes: some relation "
            "does not pair integrally with the module_generators"
        )
        assert all(
            (norm := row * gram * row) in SageZZ and norm % 2 == 0
            for row in relations.rows()
        ), "q is not defined on the classes: some relation has norm outside 2Z"
        form = QuadraticForm(module, QmodnZ(2), gram)
        refine(form, self)
        subdivide_form_gram_matrix(form)
        return form

    def from_relations_and_gram(self, relations: Matrix, gram: Matrix) -> "FormModule":
        r"""Return the torsion quadratic form $(G,q)$ built from data alone.

        The independent construction, and the one every other route ends
        at: a finitely presented torsion module -- a chosen generating set
        and the relations among it -- together with the matrix of q
        with respect to that generating set.  Nothing here refers to a
        morphism, a lattice, or a cover, because a torsion form does not
        have any; it exists exactly as a lattice given by a Gram matrix
        exists.

        The assertions are the category's axioms: $b$ has to descend, and every
        relation has to have even norm, which is what a $q$ into $\\mathbb
        Q/2\\mathbb Z$ asks of the presentation.
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
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
        from dzack_research.preamble.categories.forms.forms import QuadraticForm
        from dzack_research.preamble.categories.forms.forms import QuadraticForms
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import TorsionModule
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import cokernel_categories
        from dzack_research.preamble.refine import refine
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import subdivide_form_gram_matrix
        assert isinstance(morphism, FormMorphism), (
            "a cokernel form is constructed from a form morphism"
        )
        module = TorsionModule(morphism)
        gram = morphism.codomain().form().gram_matrix()
        quadratic_form = QuadraticForms(
            morphism.codomain().forget_form(),
            QmodnZ(2),
        )(gram)
        # The hypothesis of the quadratic refinement is that L is even: then
        # q(y + x) = q(y) + 2b(y,x) + q(x) reduces to q(y) in K/2R, so q
        # descends.  That is the branch this method is reached through --
        # discriminant_group picks this category when is_even() -- so the
        # hypothesis is stated where it decides something, and the theorem is
        # not re-proved here for each generator.
        assert morphism.domain().is_even(), (
            "the discriminant quadratic form is the even case; an odd lattice "
            "carries b alone -- use discriminant_bilinear_form"
        )
        form = QuadraticForm(module, QmodnZ(2), gram)
        refine(form, [self] + cokernel_categories(morphism))
        subdivide_form_gram_matrix(form)
        return form

    class ParentMethods:
        r"""Methods available on discriminant quadratic modules."""

        def regenerate(self: Self, module_generators: "OrderedSet") -> "FormModule":
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
            return DiscriminantQuadraticModules().from_module(module, gram)

        def form_vanishes_on(self: Self, elements: "OrderedSet") -> bool:
            r"""Return whether $q$ is zero on every element of ``elements``.

            The quadratic condition, and it is the stronger one: $q(x)=0$
            throughout a subgroup forces $b_q$ to vanish on it too, since
            $q(x+y)=q(x)+q(y)+2b_q(x,y)$ leaves $2b_q(x,y)=0$ in
            $\mathbb Q/2\mathbb Z$ and so $b_q(x,y)=0$ in
            $\mathbb Q/\mathbb Z$.  The converse fails, which is why the
            sibling category answers this for itself.
            """
            return all(element.q() == 0 for element in elements)

        def associated_quadratic_form(self: Self) -> "QuadraticFormMorphism":
            r"""Return this form: it is already the quadratic one."""
            return self

        def associated_bilinear_form(self: Self) -> "BilinearFormMorphism":
            r"""Return $b_q$, the polarization -- an object of the sibling category.

            Always defined, and it forgets: distinct $q$ on the same group can
            polarize to isometric $b$ (Peters--Sterk Sec. 12.5).
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_bilinear_modules import DiscriminantBilinearModules
            return DiscriminantBilinearModules().from_module(
                self.forget_form(),
                self.form().polar_form().gram_matrix(),
            )

        def _form_matrix_latex_label(self: Self) -> str:
            r"""Return the LaTeX label for the quadratic Gram matrix."""
            return "G_{q_{A_L}}"

        def _form_matrix_latex_codomain(self: Self) -> str:
            r"""Return the LaTeX codomain for the quadratic Gram matrix entries."""
            return "\\mathbb{Q}/2\\mathbb{Z}"

        def invariant_factor_form(self: Self) -> "FormModule":
            r"""Return $q$ on module_generators from the invariant factor decomposition.

            The change merges factors across summands -- $A_{A_2\oplus A_3}$ lands
            on one generator as $\mathbb Z/12$ rather than on two as
            $\mathbb Z/3\oplus\mathbb Z/4$ -- so no decomposition of $L$ survives
            it, which is why it cannot be :meth:`discriminant_group`.
            """
            return self.regenerate(self.smith_form_module_generators())

        def normal_form(self: Self) -> "FormModule":
            r"""Return $q$ on $p$-adic Jordan module_generators -- a different object.

            For $p$ odd the blocks are those of Peters--Sterk Prop. 9.4.1; at $p=2$
            the reduced normal form of Cor. C.3.2 applies, which is where the
            quadratic side has a uniqueness statement the bilinear side lacks.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import p_adic_jordan_module_generators
            return self.regenerate(p_adic_jordan_module_generators(self))


    class ElementMethods:
        r"""Methods available on elements of discriminant quadratic modules."""

        def q(self: Self) -> "Element":
            r"""Return $q(\bar x)\in\mathbb Q/2\mathbb Z$.

            The same pairing the bilinear form reads modulo $\mathbb Z$, read
            here modulo $2\mathbb Z$ instead -- Nikulin's convention, and the
            reason $q$ and $b$ differ only in their value module.
            """
            return self.parent().form()(self.forget_form())

        def __pow__(self: Self, exponent: "Integer", modulus: "Integer" = None) -> "Element":
            r"""``x ^ 2`` -> $q(x)$."""
            assert exponent == 2, f"exponent {exponent} not supported"
            return self.q()

        def is_characteristic(self: Self) -> bool:
            r"""Return whether $q(x)=b(x,v^*)$ modulo $\mathbb Z$ for every $x$."""
            return all(
                x.q().lift() - x.b(self).lift() in SageZZ
                for x in self.parent()
            )
