r"""Discriminant bilinear modules."""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import ModuleElement
    from sage.categories.modules import Module

from sage.rings.integer_ring import ZZ as SageZZ
if TYPE_CHECKING:
    from dzack_research.preamble.categories.forms.forms import BilinearFormMorphism
    from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from sage.categories.morphism import Morphism
    from sage.rings.integer import Integer
    from sage.structure.element import Element

from typing import Protocol, TYPE_CHECKING

from dzack_research.preamble.owned_category_bases import Category_over_base_ring
from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.matrix.matrix0 import Matrix

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    class DiscriminantBilinearParent(Protocol):
        r"""What an object of this category offers."""

        def form(self) -> "BilinearFormMorphism": ...
        def smith_form_module_generators(self) -> "OrderedSet": ...
        def regenerate(self, module_generators: "OrderedSet") -> "FormModule": ...

    class DiscriminantBilinearElement(Protocol):
        r"""What an element of such an object offers."""

        def parent(self) -> "DiscriminantBilinearParent": ...
        def underlying_element(self) -> "ModuleElement": ...
        def norm(self) -> "Element": ...
        def b(self, other: "Element") -> "Element": ...


class DiscriminantBilinearModules(Category_over_base_ring):
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
            TorsionModulesWithForm(self.base_ring()),
            SymmetricBilinearFormModules(self.base_ring()),
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
        assert module in FinitelyPresentedTorsionModules(SageZZ), (
            "a discriminant form requires a finitely presented torsion module"
        )
        assert gram.is_symmetric(), (
            "a discriminant bilinear form is symmetric"
        )
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import _presentation_matrix

        relations = _presentation_matrix(module).change_ring(SageZZ)
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
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import _torsion_module_presented_by_matrix
        module = _torsion_module_presented_by_matrix(relations)
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
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import TorsionModule
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import cokernel_categories
        from dzack_research.preamble.refine import refine
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import subdivide_form_gram_matrix
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
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import _torsion_module_presented_by_matrix
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import regenerating_data
            module_generators = tuple(module_generators)
            relations, gram = regenerating_data(self, module_generators)
            module = _torsion_module_presented_by_matrix(
                relations,
                finite_ordered_set(module_generators),
            )
            return DiscriminantBilinearModules(self.base_ring()).from_module(module, gram)

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
            :meth:`~DiscriminantQuadraticModules.ObjectType.associated_bilinear_form`,
            which polarizes $q$ and needs nothing else.

            So the passage is defined exactly on a discriminant form -- a
            bilinear module carrying its source lattice -- and only when that
            lattice is even.  A bare bilinear torsion module's stored Gram
            entries are defined only mod $1$; they are not data of the form,
            and reading them as $q$-values in $\mathbb Q/2\mathbb Z$ would
            fabricate a refinement the object does not determine.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import DiscriminantForms
            assert self in DiscriminantForms(self.base_ring()), (
                "b does not determine q: a bare bilinear torsion module's "
                "representative entries are defined only mod 1, so the "
                "quadratic refinement is reachable only through a source "
                "lattice (Def 25.4)"
            )
            lattice = self.source_lattice()
            assert lattice.is_even(), (
                "the quadratic refinement q: A_L -> Q/2Z exists exactly when "
                f"the source lattice is even; {lattice} is odd"
            )
            # The refinement is the quadratic cokernel of the same
            # correlation: the construction goes back through the lattice,
            # never through this object's mod-1 representative entries.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_quadratic_modules import DiscriminantQuadraticModules
            return DiscriminantQuadraticModules(self.base_ring()).cokernel(self.correlation())

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

        def is_isomorphic(self: "DiscriminantBilinearParent", other: "DiscriminantBilinearParent") -> bool:
            r"""Return whether the two finite symmetric bilinear forms are isometric.

            The category answers its own isomorphism question -- the bilinear
            one, which quadratic isomorphism strictly refines (Nik80 Prop
            1.8.2 gives isomorphic bilinear forms under non-isomorphic $q$;
            Zotero TTY9FFJS).  Decided behind the boundary by the engine's
            normal form at the bilinear modulus, its complete invariant for
            the pairing alone; the owned $p$-adic normal form is *a* normal
            form, not *the* one, at $p=2$, which is why the decision is not a
            comparison of that object.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import _engine_normal_form_key
            assert other in DiscriminantBilinearModules(self.base_ring()), (
                "bilinear isometry is decided between bilinear torsion forms; "
                "polarize a quadratic form first"
            )
            return bool(
                _engine_normal_form_key(self, quadratic=False)
                == _engine_normal_form_key(other, quadratic=False)
            )

        def automorphism_group(self: "DiscriminantBilinearParent") -> Parent:
            r"""Return $O(A,b):=\operatorname{Aut}$ in this category.

            The bilinear orthogonal group, which contains $O(A,q)$ of any
            quadratic refinement -- the two separate already on rank-one
            2-adic forms (MM09, Zotero ACX7WF7L).  Elements are this homset's
            own form-preserving morphisms; generator data is the engine's, at
            the bilinear modulus.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import _torsion_form_automorphism_group
            return _torsion_form_automorphism_group(self)

        def twist(self: "DiscriminantBilinearParent", scalar: "Integer") -> "FormModule":
            r"""Return $(A, s\cdot b)$: the same group, the pairing rescaled.

            Restated here the way :meth:`regenerate` is, so the twist stays a
            bilinear torsion form: this category's own constructor writes the
            rescaled pairing on the same presented group (MM09's negation
            rules, Zotero ACX7WF7L, are the $s=-1$ case).
            """
            return DiscriminantBilinearModules(self.base_ring()).from_module(
                self,
                scalar * self.form().gram_matrix(),
            )

        def pontryagin_dual_identification(self: "DiscriminantBilinearParent") -> "Morphism":
            r"""Return $A\to\operatorname{Hom}(A, K/R)$, $x\mapsto b(x,-)$.

            Pontryagin duality identifies a finite abelian group with its
            character group, and a *nondegenerate* torsion bilinear form
            realizes the identification through $b$: $x\mapsto b(x,-)$ is
            injective exactly when the form is nondegenerate, and an
            injective map of a finite group into a group of the same order
            is an isomorphism.  Nondegeneracy is therefore asserted -- on a
            degenerate form the map is not the identification it names.

            Each character is an honest module morphism into the value
            module, declared by its values on the module generators; the
            identification itself is the set morphism sending an element to
            its character.  The dual vocabulary names its functor
            (``pontryagin_dual_identification``), never a bare ``dual``.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from sage.categories.homset import Hom as sage_hom
            from sage.categories.morphism import SetMorphism
            from sage.categories.sets_cat import Sets as SageSets

            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

            zero = self.zero()
            assert all(
                any(
                    element.b(self.module_generator(label)) != 0
                    for label in self.module_generating_set()
                )
                for element in self
                if element != zero
            ), (
                "the Pontryagin identification along b exists exactly on "
                "nondegenerate torsion bilinear forms; this form has a "
                "nonzero element pairing to zero with everything"
            )
            characters = module_homset(self, self.value_module())

            def character(element: "ModuleElement") -> "Morphism":
                element = self(element)
                return characters(
                    dict(
                        (label, element.b(self.module_generator(label)))
                        for label in self.module_generating_set()
                    )
                )

            return SetMorphism(sage_hom(self, characters, SageSets()), character)


    class ElementMethods:
        r"""Methods available on elements of discriminant bilinear modules.

        An element is a coset $\bar x = x + f(L)$; $b(\bar x,\bar y)$ is the
        pairing of any two lifts, read in $\mathbb Q/\mathbb Z$ because moving
        a lift by $f(\ell)$ shifts it by $b(\ell', \ell)\in\mathbb Z$.  That is
        already what a form module's element does, so there is nothing to add.
        """
