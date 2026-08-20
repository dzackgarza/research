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
    from sage.categories.modules import Module

from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ as SageZZ
if TYPE_CHECKING:
    from dzack_research.preamble.categories.forms.forms import BilinearFormMorphism
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from sage.categories.morphism import Morphism
    from sage.rings.integer import Integer
    from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism

from typing import Protocol, TYPE_CHECKING

from dzack_research.preamble.owned_category_bases import Category
from sage.groups.additive_abelian.qmodnz import QmodnZ

# The one sanctioned crossing to Sage's private per-block Brown engine
# (ruled in by the spike's sage_patches note, absorbed here): the per-block
# Brown invariant has no public Sage surface, and this import site IS the
# boundary -- no wrapper module stands between.
from sage.modules.torsion_quadratic_module import _brown_indecomposable
from sage.matrix.matrix0 import Matrix
from sage.rings.rational_field import QQ as SageQQ

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    from collections.abc import Iterator

    class DiscriminantQuadraticParent(Protocol):
        r"""What an object of this category offers."""

        def form(self) -> "QuadraticFormMorphism": ...
        def smith_form_module_generators(self) -> "OrderedSet": ...
        def regenerate(self, module_generators: "OrderedSet") -> "FormModule": ...

        # A discriminant module is finite, so listing it is how it is searched.
        def __iter__(self) -> "Iterator[DiscriminantQuadraticElement]": ...

    class DiscriminantQuadraticElement(Protocol):
        r"""What an element of such an object offers."""

        def parent(self) -> "DiscriminantQuadraticParent": ...
        def underlying_element(self) -> "Element": ...
        def q(self) -> "Element": ...
        def b(self, other: "Element") -> "Element": ...


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
        return [TorsionModulesWithForm(SageZZ), QuadraticFormModules(SageZZ)]

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
        assert module in FinitelyPresentedTorsionModules(SageZZ), (
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
        module = FinitelyPresentedTorsionModules(SageZZ).from_relations(relations)
        return self.from_module(module, gram)

    def cokernel(self, morphism: "Morphism") -> "FormModule":
        r"""Return $\operatorname{coker} f$ for $f$ of finite index, as an object here.

        No second morphism appears: $f$ *is* the presentation, so it is handed
        to the module as such, and the refinements are about what $f$ happens
        to be -- a map of lattices, or a correlation -- rather than about extra
        data being carried alongside.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import is_form_morphism
        from dzack_research.preamble.categories.forms.forms import QuadraticForm
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import TorsionModule
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import cokernel_categories
        from dzack_research.preamble.refine import refine
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import subdivide_form_gram_matrix
        assert is_form_morphism(morphism), (
            "a cokernel form is constructed from a form morphism"
        )
        module = TorsionModule(morphism)
        gram = morphism.codomain().form().gram_matrix()
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

        def regenerate(self: "DiscriminantQuadraticParent", module_generators: "OrderedSet") -> "FormModule":
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
            module = FinitelyPresentedTorsionModules(SageZZ).from_relations(
                relations,
                finite_ordered_set(module_generators),
            )
            return DiscriminantQuadraticModules().from_module(module, gram)

        def form_vanishes_on(self: "DiscriminantQuadraticParent", elements: "OrderedSet") -> bool:
            r"""Return whether $q$ is zero on every element of ``elements``.

            The quadratic condition, and it is the stronger one: $q(x)=0$
            throughout a subgroup forces $b_q$ to vanish on it too, since
            $q(x+y)=q(x)+q(y)+2b_q(x,y)$ leaves $2b_q(x,y)=0$ in
            $\mathbb Q/2\mathbb Z$ and so $b_q(x,y)=0$ in
            $\mathbb Q/\mathbb Z$.  The converse fails, which is why the
            sibling category answers this for itself.
            """
            return all(element.q() == 0 for element in elements)

        def associated_quadratic_form(self: "DiscriminantQuadraticParent") -> "DiscriminantQuadraticParent":
            r"""Return this form: it is already the quadratic one."""
            return self

        def associated_bilinear_form(self: "DiscriminantQuadraticParent") -> "BilinearFormMorphism":
            r"""Return $b_q$, the polarization -- an object of the sibling category.

            Always defined, and it forgets: distinct $q$ on the same group can
            polarize to isometric $b$ (Peters--Sterk Sec. 12.5).
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_bilinear_modules import DiscriminantBilinearModules
            return DiscriminantBilinearModules().from_module(
                self,
                self.form().polar_form().gram_matrix(),
            )

        def _form_matrix_latex_label(self: "DiscriminantQuadraticParent") -> str:
            r"""Return the LaTeX label for the quadratic Gram matrix."""
            return "G_{q_{A_L}}"

        def _form_matrix_latex_codomain(self: "DiscriminantQuadraticParent") -> str:
            r"""Return the LaTeX codomain for the quadratic Gram matrix entries."""
            return "\\mathbb{Q}/2\\mathbb{Z}"

        def invariant_factor_form(self: "DiscriminantQuadraticParent") -> "FormModule":
            r"""Return $q$ on module_generators from the invariant factor decomposition.

            The change merges factors across summands -- $A_{A_2\oplus A_3}$ lands
            on one generator as $\mathbb Z/12$ rather than on two as
            $\mathbb Z/3\oplus\mathbb Z/4$ -- so no decomposition of $L$ survives
            it, which is why it cannot be :meth:`discriminant_group`.
            """
            return self.regenerate(self.smith_form_module_generators())

        def normal_form(self: "DiscriminantQuadraticParent") -> "FormModule":
            r"""Return $q$ on $p$-adic Jordan module_generators -- a different object.

            For $p$ odd the blocks are those of Peters--Sterk Prop. 9.4.1; at $p=2$
            the reduced normal form of Cor. C.3.2 applies, which is where the
            quadratic side has a uniqueness statement the bilinear side lacks.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import p_adic_jordan_module_generators
            return self.regenerate(p_adic_jordan_module_generators(self))

        def brown_invariant(self: "DiscriminantQuadraticParent") -> "Element":
            r"""Return $\operatorname{Br}(q)\in\mathbb Z/8$.

            The definition is the argument of the normalized Gauss sum of the
            finite quadratic form: $\gamma_q(1)=\exp(\pi i\operatorname{Br}(q)/4)$
            (MM09 Thm 5.1, Zotero ACX7WF7L) -- a property of $(A,q)$ alone.
            That $\operatorname{Br}(q_L)$ equals the signature of an even
            lattice mod $8$ is *Milgram's theorem* (Nik80 Thm 1.3.3, Zotero
            TTY9FFJS), a theorem about lattices and never the definition.

            Computed over the orthogonal splitting $q=\bigoplus_p q_p$ into
            primary parts (Nik80 Prop 1.2.2), each written in $p$-adic Jordan
            form; the value of each indecomposable block is Shimada's table,
            delegated to Sage's per-block engine behind this boundary.
            """
            from sage.quadratic_forms.genera.normal_form import collect_small_blocks
            from sage.rings.finite_rings.integer_mod_ring import IntegerModRing

            brown = IntegerModRing(8).zero()
            for p in self.annihilator().gen().prime_divisors():
                normal = self.primary_part(p).normal_form()
                generators = tuple(normal.module_generators())
                # The symmetric matrix of canonical representatives: q on the
                # diagonal read in Q/2Z, b off it read in Q/Z -- the entries
                # the per-block table is written in.
                reduced = matrix(
                    SageQQ,
                    [
                        [
                            left.q().lift() if i == j else left.b(right).lift()
                            for j, right in enumerate(generators)
                        ]
                        for i, left in enumerate(generators)
                    ],
                )
                for block in collect_small_blocks(reduced):
                    brown += _brown_indecomposable(block, p)
            return brown

        def is_isomorphic(self: "DiscriminantQuadraticParent", other: "DiscriminantQuadraticParent") -> bool:
            r"""Return whether the two finite quadratic forms are isometric.

            The category answers its own isomorphism question: both objects
            carry $q$, and the decision is normal-form comparison behind the
            boundary -- the engine's stated contract is that torsion quadratic
            modules are isomorphic exactly when they share value modules and
            normal form.  Finiteness is what makes this decidable at all.
            That quadratic isomorphism refines bilinear refines group
            isomorphism is then a theorem (MM09, Zotero ACX7WF7L), not an API
            flag.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import _engine_normal_form_key
            assert other in DiscriminantQuadraticModules(), (
                "quadratic isometry is decided between quadratic torsion "
                "forms; ask the bilinear category about polarizations"
            )
            return bool(
                _engine_normal_form_key(self, quadratic=True)
                == _engine_normal_form_key(other, quadratic=True)
            )

        def automorphism_group(self: "DiscriminantQuadraticParent") -> Parent:
            r"""Return $O(A,q):=\operatorname{Aut}_{\mathbf{DiscQuad}}(A,q)$.

            FOUNDATIONS Def 26.2: a value of the generic automorphism
            construction in this category, not a separate primitive.  The
            elements are this homset's own form-preserving morphisms;
            generator data and order are the engine's, translated back
            (Remark 26.5 rules out the matrix-subgroup description outside
            the homocyclic case, so no matrix group is built).
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import _torsion_form_automorphism_group
            return _torsion_form_automorphism_group(self, quadratic=True)

        def twist(self: "DiscriminantQuadraticParent", scalar: "Integer") -> "FormModule":
            r"""Return $(A, s\cdot q)$: the same group, the form rescaled.

            Restated here the way :meth:`regenerate` is, so the twist of a
            quadratic torsion form is constructed *as one*: the general
            notion rescales the form morphism (MM09, Zotero ACX7WF7L, whose
            negation rules are the $s=-1$ case), and this category's own
            constructor is what writes the rescaled form on the same
            presented group.
            """
            return DiscriminantQuadraticModules().from_module(
                self,
                scalar * self.form().polar_form().gram_matrix(),
            )

        def is_anti_isometric(
            self: "DiscriminantQuadraticParent",
            other: "DiscriminantQuadraticParent",
        ) -> bool:
            r"""Return whether some group isomorphism $f:A_1\to A_2$ has
            $q_2(f(x))=-q_1(x)$.

            An anti-isometry *is* an isometry onto the $(-1)$-twist of the
            codomain, so the question is spelled through the owned twist and
            the category's own isometry decision -- no new primitive.  This
            is the relation Nikulin's complement-pair theory runs on
            (Nik80, Zotero TTY9FFJS, Cor 1.6.2: the discriminant quadratic
            forms of a primitive complement pair in an even unimodular
            lattice are anti-isometric).
            """
            return bool(self.is_isomorphic(other.twist(-1)))


    class ElementMethods:
        r"""Methods available on elements of discriminant quadratic modules."""

        def q(self: "DiscriminantQuadraticElement") -> "Element":
            r"""Return $q(\bar x)\in\mathbb Q/2\mathbb Z$.

            The same pairing the bilinear form reads modulo $\mathbb Z$, read
            here modulo $2\mathbb Z$ instead -- Nikulin's convention, and the
            reason $q$ and $b$ differ only in their value module.
            """
            return self.parent().form()(self.underlying_element())

        def __pow__(
            self: "DiscriminantQuadraticElement",
            exponent: "Integer",
            modulus: "Integer | None" = None,
        ) -> "Element":
            r"""``x ^ 2`` -> $q(x)$."""
            assert exponent == 2, f"exponent {exponent} not supported"
            return self.q()

        def is_characteristic(self: "DiscriminantQuadraticElement") -> bool:
            r"""Return whether $q(x)=b(x,v^*)$ modulo $\mathbb Z$ for every $x$."""
            return all(
                x.q().lift() - x.b(self).lift() in SageZZ
                for x in self.parent()
            )
