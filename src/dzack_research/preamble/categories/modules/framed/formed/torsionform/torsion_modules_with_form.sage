r"""Finite torsion modules equipped with a bilinear or quadratic form."""


from sage.rings.rational_field import QQ as SageQQ
from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
from dzack_research.preamble.lexicon import Element
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from sage.categories.modules import Module
    from dzack_research.preamble.lexicon import ModuleElement

from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormHomset
from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
    from sage.categories.morphism import Morphism

from sage.categories.category import Category
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from typing import Protocol, TYPE_CHECKING

from dzack_research.preamble.categories.sets.cardinals import Cardinal
from dzack_research.preamble.lexicon import GramMatrix
from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import MorphismMatrix

from sage.arith.misc import factor
from sage.misc.latex import latex as _latex_fn

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import Matrix, OrderedSet

    # An ideal of ZZ, which is what an annihilator is. No lexicon noun names
    # it yet, so the stub tree's own class is what the signatures below say.
    from sage.rings.ideal import Ideal_pid

    from collections.abc import Iterator

    from sage.rings.ring import Ring

    class TorsionFormParent(Protocol):
        r"""What a finite torsion module with a form offers."""

        _over: "Module"

        def form(self) -> "FormMorphism": ...
        def forget_form(self) -> "Module": ...
        def presentation(self) -> "ModuleMorphism": ...
        def module_generator(self, label: "Element") -> "Element": ...
        def module_generators(self) -> tuple: ...
        def module_generating_set(self) -> "OrderedSet": ...
        def smith_form_module_generators(self) -> "OrderedSet": ...
        def invariants(self) -> tuple: ...
        def cardinality(self) -> "Cardinal": ...
        def annihilator(self) -> "Ideal_pid": ...
        def zero(self) -> "Element": ...
        def regenerate(self, module_generators: "OrderedSet") -> "FormModule": ...
        def form_vanishes_on(self, elements: "OrderedSet") -> bool: ...
        def subobject_generated_by(self, elements: "OrderedSet") -> Subobject: ...
        def primary_decomposition(self) -> dict: ...
        def _isotropic_subgroups(self) -> "Iterator[frozenset]": ...
        def gram_matrix(self) -> GramMatrix: ...
        def _form_matrix_latex_label(self) -> str: ...
        def _form_matrix_latex_codomain(self) -> str: ...
        def __iter__(self) -> "Iterator[Element]": ...

    class TorsionFormElement(Protocol):
        r"""What an element of such a module offers."""

        def parent(self) -> "TorsionFormParent": ...
        def forget_form(self) -> "ModuleElement": ...

    class CokernelFormParent(Protocol):
        r"""What a form on a cokernel offers: the map it came from."""

        _presentation: "ModuleMorphism"

        def presentation(self) -> "ModuleMorphism": ...
        def cover(self) -> "Module": ...
        def module_generator(self, label: "Element") -> "Element": ...
        def projection(self) -> "FormMorphism": ...


class TorsionModulesWithForm(OwnedCategoryOverBaseRing):
    r"""Category of finite torsion modules equipped with a form."""

    @staticmethod
    def __classcall_private__(
        cls: type["TorsionModulesWithForm"],
        base_ring: "Ring | None" = None,
    ) -> "TorsionModulesWithForm":
        # Over the engine's integers, which is what the modules of this
        # category carry: the owned ring is the session's name for it, and a
        # category built over one while its objects carry the other has no
        # members at all.
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: "TorsionModulesWithForm"
        match base_ring:
            case None:
                category = super().__classcall__(cls, SageZZ)
                return category
            case _ if engine_ring(base_ring) is SageZZ:
                category = super().__classcall__(cls, SageZZ)
                return category
            case _:
                assert False, (
                    "finite torsion-form algorithms here are over ZZ"
                )

    @classmethod
    def _repr_object_names(cls) -> str:
        return "torsion modules with form"

    def super_categories(self) -> list:
        r"""Return finite abelian groups equipped with a form.

        An element of $(G,b)$ is an element of the finite abelian group $G$.
        The object keeps additive notation because its group law is module
        addition.  Forgetting the form removes only $b$ and returns the same
        finite-presentation structure on the underlying module.

        Nor a category with its own pairing: $b(a,a')$ and the norm are what it
        is to have a form at all, so they come from :class:`FormModules` here
        exactly as they do for a lattice or for $L^\vee$.  What is added below
        is what being *torsion* adds, which is finiteness and everything that
        follows from it.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FinitelyGeneratedFormModules
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import FinitelyPresentedTorsionModules
        return [
            FinitelyGeneratedFormModules(self.base_ring()),
            FinitelyPresentedTorsionModules(self.base_ring()),
        ]

    class ParentMethods:
        r"""Methods shared by bilinear and quadratic discriminant modules."""

        def gram_matrix(self: "TorsionFormParent") -> GramMatrix:
            r"""Return the form's matrix with its entries read in the value module.

            The form stores representatives -- rationals -- because $\mathbb
            Q/n\mathbb Z$ has no matrix space to hold the entries themselves.
            This reduces each into the value module and takes the canonical
            representative back, so the same object is displayed the same way
            however it was built.  Which matrix it is, is the form's business:
            $b$'s matrix for a bilinear module, $q$'s upper-triangular one for
            a quadratic module.
            """
            form = self.form()
            target = form.value_module()
            reduced = GramMatrix(matrix(
                SageQQ,
                [
                    [target(entry).lift() for entry in row]
                    for row in form.gram_matrix().rows()
                ],
            ))
            reduced.subdivide(*form.gram_matrix().subdivisions())
            return reduced

        def relation_matrix(self: "TorsionFormParent") -> MorphismMatrix:
            r"""Return :meth:`presentation`'s matrix, one row per relation."""
            return self.forget_form().relation_matrix()

        def presentation(self: "TorsionFormParent") -> "ModuleMorphism":
            r"""Return $p$, the morphism this object is the cokernel of.

            Every object here has one, because every finitely presented module
            does.  What $p$ *is* varies -- a lattice's correlation, a
            finite-index map of lattices, or a morphism synthesized from a
            group and a matrix -- and that is what the refinements below are
            about; that there is one is not.
            """
            return self.forget_form().presentation()

        def invariants(self: "TorsionFormParent") -> tuple:
            r"""Return the invariant factors of the underlying module."""
            return tuple(self.forget_form().invariants())

        def cardinality(self: "TorsionFormParent") -> "Cardinal":
            r"""Return \(|A|\), which a form does not change."""
            return self.forget_form().cardinality()

        def annihilator(self: "TorsionFormParent") -> "Ideal_pid":
            r"""Return $\operatorname{Ann}(A)\subseteq\mathbb Z$, which is nonzero here.

            The ideal, not its generator: callers ask it for ``gen()``.
            """
            annihilator: "Ideal_pid" = self.forget_form().annihilator()
            return annihilator

        def smith_form_module_generators(self: "TorsionFormParent") -> "OrderedSet":
            r"""Return generators realizing the invariant factor decomposition.

            The form is not written in them -- they are a different generating
            set, and a form written in one is a different object from the same
            form written in another, which is what ``regenerate`` builds.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            return finite_ordered_set(
                tuple(
                    self._over(generator)
                    for generator in self.forget_form().smith_form_module_generators()
                )
            )

        def __iter__(self: "TorsionFormParent") -> "Iterator[Element]":
            r"""Iterate over the elements, of which there are finitely many."""
            return map(self._over, self.forget_form())


        def primary_part(self: "TorsionFormParent", p: "Integer") -> Subobject:
            r"""Return $A_p\hookrightarrow A$ as a subobject: the inclusion is the data.

            A presentation does not say which combinations of its generators
            have $p$-power order, and no bounded family of extra relations
            makes it say so, so $A_p$ is not cut out of one.  It is read off
            the primary decomposition: the invariant factor decomposition
            $A\cong\bigoplus\mathbb Z/d_i$ has generators $g_i$ of order $d_i$,
            and $(d_i/p^{v_p(d_i)})g_i$ generates the $p$-primary summand of
            that factor.  There is one per $d_i$ divisible by $p$ and they are
            independent, so they generate $A_p$ minimally -- which matters
            downstream, because a form written on a dependent generating set
            has a rank of its own that is not the group's.

            The inclusion comes with them.  Passing to the invariant factor
            decomposition is a change of basis, and $g_i$ is its $i$-th row
            already expressed in $A$'s own generating set, so composing with it
            is what makes the images above elements of $A$ rather than of a
            decomposition standing apart from it.
            """

            def primary_generator(
                generator: "ModuleElement",
            ) -> tuple["ModuleElement", ...]:
                order = generator.order()
                primary = p ** order.valuation(p)
                assert primary >= 1
                match primary:
                    case 1:
                        return ()
                    case value if value > 1:
                        return ((order // value) * generator,)
                    case _:
                        assert False, "a prime power is 1 or larger than 1"

            generators = tuple(
                primary_element
                for generator in self.smith_form_module_generators()
                for primary_element in primary_generator(generator)
            )
            return self.subobject_generated_by(generators)

        def subobject_generated_by(
            self: "TorsionFormParent",
            module_generators: "OrderedSet",
        ) -> Subobject:
            r"""Return $\langle S\rangle\hookrightarrow A$ as a subobject.

            The inclusion is the data, and it comes for free: ``regenerate``
            writes the form on the elements handed to it, so its object is
            already the subgroup they generate and its generating set is
            already made of $A$'s own elements.  What is left is to say that
            each of them is itself, which is the morphism.
            """
            regenerated = self.regenerate(module_generators)
            return Subobject(
                regenerated.Hom(self)(
                    {
                        label: label
                        for label in regenerated.module_generating_set()
                    }
                )
            )

        # ---- isotropic subobjects ----

        def isotropic_subobjects(self: "TorsionFormParent") -> "Iterator[Subobject]":
            r"""Iterate over the subobjects of $A$ the form vanishes on.

            Exhaustible because $A$ is finite, and searched rather than
            listed: an isotropic subgroup is generated by isotropic elements
            and every subgroup of one is again isotropic, so the isotropic
            subgroups are exactly what is reached from $0$ by repeatedly
            adjoining an element and keeping the result when the form still
            vanishes.  Each is reached along some chain, so none is missed,
            and each is reported once.

            Which form has to vanish is the refinements' business -- $q$ for a
            quadratic module and $b$ for a bilinear one -- and is asked of
            :meth:`form_vanishes_on`.
            """
            for _, module_generators in self._isotropic_subgroups():
                yield self.subobject_generated_by(module_generators)

        def maximal_isotropic_subobjects(
            self: "TorsionFormParent",
        ) -> "Iterator[Subobject]":
            r"""Iterate over the isotropic subobjects contained in no other.

            Maximal means maximal among the isotropic subgroups, which is a
            statement about the whole family, so the family is what it is
            decided against.  Containment is read off the subgroups as sets of
            elements, before any of them is built into an object.
            """
            subgroups = list(self._isotropic_subgroups())
            for elements, module_generators in subgroups:
                if any(elements < larger for larger, _ in subgroups):
                    continue
                yield self.subobject_generated_by(module_generators)

        def _isotropic_subgroups(
            self: "TorsionFormParent",
        ) -> "Iterator[tuple[frozenset, tuple]]":
            r"""Iterate over the isotropic subgroups as (elements, generators).

            The elements are what maximality is decided on and what the form
            is tested on; the generators are the chain that reached them, and
            they are carried along because the subgroup is wanted on a small
            generating set and not on all of itself.
            """
            zero = self.zero()
            trivial = frozenset((zero,))
            yield trivial, ()

            # Only an element whose own cyclic subgroup is isotropic can lie
            # in an isotropic subgroup, so those are the only extensions
            # worth attempting.
            extending = tuple(
                element
                for element in self
                if element != zero
                and self.form_vanishes_on(_subgroup_generated(trivial, element))
            )
            # A Python set, spelled as one: a brace literal here is the
            # preparser's finite Set of the session's universe, which is a
            # different object and does not accumulate.
            seen = set([trivial])
            frontier = [(trivial, ())]
            while frontier:
                elements, module_generators = frontier.pop()
                for element in extending:
                    if element in elements:
                        continue
                    larger = _subgroup_generated(elements, element)
                    if larger in seen or not self.form_vanishes_on(larger):
                        continue
                    seen.add(larger)
                    reached: tuple[frozenset, tuple] = (
                        larger,
                        module_generators + (element,),
                    )
                    frontier.append(reached)
                    yield reached

        def is_anisotropic(self: "TorsionFormParent") -> bool:
            r"""Return whether the only isotropic element is $0$.

            The definition (Nik80 §1.6 [Nik80]): a form is anisotropic when no
            nonzero element is isotropic.  Which vanishing is asked -- $q$ for
            a quadratic module, $b$ on the pair for a bilinear one -- is
            :meth:`form_vanishes_on`'s business, asked element by element,
            and the search is exhaustible because $A$ is finite.
            """
            zero = self.zero()
            return all(
                not self.form_vanishes_on((element,))
                for element in self
                if element != zero
            )

        def orthogonal_subobject(self: "TorsionFormParent", subobject: Subobject) -> Subobject:
            r"""Return $S^{\perp}=\{x\in A: b(x,S)=0\}\hookrightarrow A$.

            Computed from the pairing, on the data that determines it: $b$ is
            bilinear, so $b(x,S)=0$ is decided on the generators of $S$, read
            in $A$ through the subobject's inclusion.  The perpendicular is a
            subgroup, and it comes back as one: a subobject with its own
            inclusion, generated by a chain of elements none of which the
            previous ones span.
            """
            embedding = subobject.embedding()
            assert embedding.codomain() is self, (
                "the orthogonal is taken of a subobject of this module"
            )
            images = tuple(
                embedding(generator)
                for generator in embedding.domain().module_generators()
            )
            module_generators: tuple = ()
            span = frozenset((self.zero(),))
            for element in self:
                if element in span or not all(
                    element.b(image) == 0 for image in images
                ):
                    continue
                module_generators = module_generators + (element,)
                span = _subgroup_generated(span, element)
            return self.subobject_generated_by(module_generators)

        def lagrangian_subobjects(self: "TorsionFormParent") -> "Iterator[Subobject]":
            r"""Iterate over the isotropic subobjects with $S=S^{\perp}$.

            Nikulin's condition for the glued overlattice to be unimodular
            (Nik80 §1.4, [Nik80]): $S$ isotropic and equal to its own
            perpendicular.  Equality is a statement about the two subgroups
            of $A$, so it is decided on their elements seen in $A$.
            """
            for subobject in self.isotropic_subobjects():
                perpendicular = self.orthogonal_subobject(subobject)
                if _subobject_elements(subobject) == _subobject_elements(
                    perpendicular
                ):
                    yield subobject

        def is_metabolic(self: "TorsionFormParent") -> bool:
            r"""Return whether the form admits a lagrangian subobject."""
            return any(True for _ in self.lagrangian_subobjects())

        def metabolizer(self: "TorsionFormParent") -> Subobject:
            r"""Return a metabolizer: a chosen lagrangian subobject.

            *A* metabolizer -- lagrangian subobjects need not be unique -- and
            its existence is the hypothesis, stated rather than searched
            around: an anisotropic form has none.
            """
            for subobject in self.lagrangian_subobjects():
                return subobject
            assert False, (
                "the form is not metabolic: it has no lagrangian subobject"
            )

        def restricted_form(self: "TorsionFormParent", subobject: Subobject) -> "FormModule":
            r"""Return the form pulled back along $\iota: S\hookrightarrow A$.

            The pullback along a monomorphism is the restriction, and the
            subobject already carries it: :meth:`subobject_generated_by`
            writes this form on the generators of $S$, so the restricted form
            *is* the inclusion's domain, handed back under the name the
            construction goes by.
            """
            embedding = subobject.embedding()
            assert embedding.codomain() is self, (
                "the restricted form is the pullback along a subobject of "
                "this module"
            )
            return embedding.domain()

        def subquotient_form(
            self: "TorsionFormParent",
            subobject: Subobject,
            over: Subobject,
        ) -> "FormModule":
            r"""Return $K/H$ with the induced form, for $H\subseteq K\subseteq H^{\perp}$.

            Nikulin's subquotient (Nik80 §1.4, [Nik80]): $H$ isotropic makes
            the form descend to the classes, and $K\subseteq H^{\perp}$ is
            what makes the descended pairing well defined.  Both hypotheses
            are stated on the subobjects' elements; the object is then the
            cokernel of the arrow $H\to K$ the two inclusions induce, with
            the form of $K$ read on the classes -- the same construction every
            torsion form here is born from.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import TorsionModule
            embedding = subobject.embedding()
            larger = over.embedding()
            assert embedding.codomain() is self and larger.codomain() is self, (
                "a subquotient is taken of two subobjects of this module"
            )
            small = _subobject_elements(subobject)
            assert small <= _subobject_elements(over), (
                "the subquotient K/H requires H contained in K"
            )
            assert self.form_vanishes_on(tuple(small)), (
                "the subquotient form descends along an isotropic subobject"
            )
            perpendicular = _subobject_elements(
                self.orthogonal_subobject(subobject)
            )
            assert _subobject_elements(over) <= perpendicular, (
                "the subquotient form requires K contained in the "
                "perpendicular of H"
            )
            domain = embedding.domain()
            codomain = larger.domain()
            inclusion = domain.Hom(codomain)(
                {
                    label: larger.lift(embedding(generator))
                    for label, generator in zip(
                        domain.module_generating_set(),
                        domain.module_generators(),
                    )
                }
            )
            category = _discriminant_category_of(self)
            return category.from_module(
                TorsionModule(inclusion),
                _symmetric_representative_matrix(codomain.form()),
            )

        def orthogonal_quotient(self: "TorsionFormParent", subobject: Subobject) -> "FormModule":
            r"""Return $S^{\perp}/S$ with the induced form (Nik80 Prop 1.4.1)."""
            return self.subquotient_form(
                subobject, self.orthogonal_subobject(subobject)
            )

        def normal_form_isometry(self: "TorsionFormParent") -> "FormMorphism":
            r"""Return the isometry ``normal_form() -> self`` witnessing the normal form.

            The normal form is this form regenerated on the $p$-adic Jordan
            generators, which are elements of this object, so the witness
            sends each generator to itself -- the morphism the engine's
            ``return_isometry`` flag would hand back as a matrix, spelled in
            the homset it lives in.  It is an isomorphism, so it carries the
            passage in either direction.
            """
            normal = self.normal_form()
            return normal.Hom(self)(
                {label: label for label in normal.module_generating_set()}
            )

        def is_p_elementary(self: "TorsionFormParent", p: "Integer") -> bool:
            r"""Return whether the underlying group is elementary abelian of exponent $p$."""
            elementary: bool = self.forget_form().is_p_elementary(p)
            return elementary

        def primary_decomposition(self: "TorsionFormParent") -> dict:
            r"""Return the underlying group's primary decomposition."""
            decomposition: dict = self.forget_form().primary_decomposition()
            return decomposition

        def _latex_(self: "TorsionFormParent") -> str:
            r"""Return multi-line LaTeX for the torsion module and its form."""
            invs = self.invariants()
            n = self.gram_matrix().nrows()

            fp_latex = str(_latex_fn(self.forget_form()))
            inv_str = _format_invariant_factor_latex(invs)
            prim_str = _format_primary_decomp_latex(invs)
            gram_latex = _form_gram_matrix_latex(self)
            label = self._form_matrix_latex_label()

            line1 = (
                f"A_L = {fp_latex} \\in \\mathbb{{Z}}\\text{{-Mod}} \\quad "
                "\\text{(Finite presentation)} \\\\"
            )
            line2 = (
                f"A_L \\cong {inv_str} \\in \\mathbb{{Z}}\\text{{-Mod}} \\quad "
                "\\text{(Invariant factor decomposition)} \\\\"
            )
            line3 = (
                f"A_L \\cong {prim_str} \\in \\mathbb{{Z}}\\text{{-Mod}} \\quad "
                "\\text{(Primary decomposition)} \\\\"
            )
            line4 = (
                f"{label} = {gram_latex} \\in "
                f"\\mathrm{{Mat}}_{{{n}}}({self._form_matrix_latex_codomain()})"
            )

            return (
                "\\begin{gathered}\n"
                + "\n".join([line1, line2, line3, line4])
                + "\n\\end{gathered}"
            )

        def _form_matrix_latex_label(self: "TorsionFormParent") -> str:
            r"""Return the LaTeX label for this form's Gram matrix."""
            return "G_{A_L}"

        def _form_matrix_latex_codomain(self: "TorsionFormParent") -> str:
            r"""Return the LaTeX codomain for this form's Gram matrix entries."""
            return "\\mathbb{Q}/\\mathbb{Z}"

    class ElementMethods:
        r"""What torsion adds to being an element of a module with a form.

        Which is one thing.  Addition and the $\mathbb Z$ action are
        $\mathbb Z\text{-Mod}$'s and are not a group's operation under another
        name; pairing and norm are :class:`FormModules`'s, since they are what
        having a form means and not what having a *torsion* one means.  Both
        arrive with membership.

        What is left is that the annihilator of an element is a nonzero ideal,
        so it has a generator -- a question that has no answer in a free form
        module, which is why it is stated here and not above.
        """

        def order(self: "TorsionFormElement") -> "Integer":
            r"""Return the generator of $\operatorname{Ann}(a)$, asked of $U(a)$.

            A module question, and one the form has no part in, so it is put to
            the element's image under the fibration's projection.
            """
            order: "Integer" = self.forget_form().order()
            return order


class CokernelForms(Category):
    r"""Torsion forms constructed as $\operatorname{coker}(f)$ for $f:L\to M$ of finite index.

    A construction, not a kind of object.  A torsion form is $(G,b)$ -- a
    finite torsion module and a form on it -- and is as primitive as a lattice
    $(L,b)$ is; nothing about it requires a morphism.  Taking the cokernel of a
    finite-index morphism of lattices is *one way* to obtain one, and the
    objects that arise that way carry more than the general ones do: the
    morphism itself, the lattice it maps into, and the projection from that
    lattice onto the classes.

    Finite index is the whole hypothesis.  It is what makes the cokernel
    torsion, and it is $\det f\ne 0$, which is where the construction is
    gated.  The morphism need not be a correlation: any $f:L\to M$ of finite
    index between lattices whose form descends gives a torsion form here, and
    the discriminant forms are the further special case $f=c$.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "cokernel torsion forms"

    def super_categories(self) -> list:
        return [TorsionModulesWithForm()]

    class ParentMethods:
        r"""What a lattice presentation adds, which is a cover and little else.

        Not the presentation itself -- every torsion form has one of those.
        What is special here is that $p$ maps between lattices, so its codomain
        is a lattice whose classes these are and which there is a projection
        from.  Every form method belongs to the torsion form this object
        already is; nothing below computes with a form.
        """

        def cover(self: "CokernelFormParent") -> "Module":
            r"""Return $M=\operatorname{codom} f$, whose classes these are."""
            return self.presentation().codomain()

        def projection(self: "CokernelFormParent") -> "FormMorphism":
            r"""Return $\pi:M\to G$, sending $M$'s $i$-th generator to this object's.

            Available because there is a cover to project from.  A torsion form
            built from a group and a matrix has no such morphism, which is the
            point of the refinement.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _module_morphism
            cover = self.cover()
            return _module_morphism(
                cover,
                self,
                {
                    label: self.module_generator(label)
                    for label in cover.module_generating_set()
                },
            )

    class ElementMethods:
        r"""What an element of a cokernel form adds: a lift into the cover."""

        def coset_representative(self: "TorsionFormElement") -> "ModuleElement":
            r"""Return a lift of this class in the cover: a section of $\pi$.

            A class is a coset, and the cover is where its representatives
            live, so the answer is an element of :meth:`~CokernelForms.ParentMethods.cover`
            projecting back to this one -- asked of the projection morphism,
            whose ``lift`` is the section.
            """
            return self.parent().projection().lift(self)


class DiscriminantForms(Category):
    r"""The cokernels whose morphism is a correlation: $A_L=\operatorname{coker}(c:L\to L^\vee)$.

    A refinement, not a kind of object.  A torsion bilinear form is a finite
    torsion module with a form and nothing else -- $(G,b)$ for whatever $G$ and
    $b$, exactly as a lattice is $(L,b)$ -- and the ones that happen to be
    discriminant forms of a lattice are a special class of those.  What is
    special is a fact about the *presentation*: its domain is a lattice, so
    there is an $L$ to ask about, and $\pi$ has $L^\vee$ for its domain.

    So the two methods below live here and nowhere else.  A form written on
    invariant factor generators or on $p$-adic Jordan generators is presented
    by a morphism synthesized from that generating set, whose domain is a free
    module carrying a $\mathbb Q$-valued form; it is a perfectly good torsion
    form, it has a presentation, and it has no source lattice.  Before this
    split it answered ``source_lattice`` with that synthesized module.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "discriminant forms"

    def super_categories(self) -> list:
        return [CokernelForms()]

    class ParentMethods:
        r"""Methods available on the discriminant form of a lattice."""

        def correlation(self: "CokernelFormParent") -> "FormMorphism":
            r"""Return $c: L\to L^\vee$: the presentation, under its own name."""
            return self.presentation()

        def source_lattice(self: "CokernelFormParent") -> "FormModule":
            r"""Return the lattice $L$ this is the discriminant form of."""
            return self.presentation().domain()

        def overlattice_from_isotropic_subobject(
            self: "CokernelFormParent", subobject: Subobject
        ) -> "FormMorphism":
            r"""Return $L\hookrightarrow L'$ for the overlattice glued along $S$.

            Nikulin Prop. 1.4.1 (Nik80, Zotero TTY9FFJS): the integral
            overlattices of $L$ -- even ones when $L$ is even -- correspond to
            the isotropic subgroups $S\le A_L$, with $L'$ the preimage of $S$
            under $L^\vee\to A_L$.  This object carries the source lattice, so
            the construction lives here; the answer is the inclusion
            *morphism*, whose index and codomain are then the arrow's own
            questions.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum
            lattice = self.source_lattice()
            embedding = subobject.embedding()
            assert embedding.codomain() is self, (
                "the glued overlattice is named by a subobject of this "
                "discriminant form"
            )
            assert self.form_vanishes_on(
                tuple(
                    embedding(element) for element in embedding.domain()
                )
            ), "overlattice glue requires an isotropic subobject (Nik80 1.4.1)"
            overlattice = lattice.glue(
                *(
                    embedding(generator)
                    for generator in embedding.domain().module_generators()
                )
            )
            # The generating set glue chose is its rows in L's own framing, so
            # inverting them writes L's generators in the overlattice's -- the
            # matrix of the inclusion, integral exactly because L sits inside
            # what was glued from it.
            coordinates = matrix(
                SageQQ,
                [list(row) for row in overlattice.module_generating_set()],
            ).inverse()
            assert all(entry in SageZZ for entry in coordinates.list()), (
                f"{overlattice} was glued from {lattice} and does not contain it"
            )
            coordinates = coordinates.change_ring(SageZZ)
            return lattice.Hom(overlattice)(
                [
                    zipsum(row, overlattice.module_generators(), overlattice.zero())
                    for row in coordinates.rows()
                ]
            )

        def discriminant_form_of_overlattice(
            self: "CokernelFormParent", subobject: Subobject
        ) -> "FormModule":
            r"""Return $A_{L'}$ for the overlattice glued along $S$: $S^{\perp}/S$.

            Nikulin Prop. 1.4.1's other half (Nik80, Zotero TTY9FFJS): the
            discriminant form of the glued lattice is the subquotient
            $S^{\perp}/S$ of this one, so it is computed as one.
            """
            return self.orthogonal_quotient(subobject)


def cokernel_categories(morphism: "Morphism") -> list:
    r"""Return the refinements ``morphism`` earns for its cokernel.

    Two independent questions, asked in order.  Is this the cokernel of a
    morphism of lattices at all -- which is what :class:`CokernelForms` is
    about, and which a synthesized presentation on some other generating set is
    not?  And if so, is that morphism the domain's own correlation, which is
    what makes the cokernel a discriminant form rather than one of the many
    other torsion forms a finite-index $f:L\to M$ produces?
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
    domain = morphism.domain()
    if domain not in IntegralLattices():
        return []
    if morphism is domain.correlation():
        return [CokernelForms(), DiscriminantForms()]
    return [CokernelForms()]



def _subgroup_generated(subgroup: frozenset, element: "Element") -> frozenset:
    r"""Return $H+\langle a\rangle$ for a subgroup $H$ and an element $a$.

    Every coset of $\langle a\rangle$ met by the sum is $H+ka$ for some
    $k<\operatorname{ord}(a)$, so this is the whole of it and closure under
    addition needs no iterating to a fixed point.
    """
    return frozenset(
        member + multiple * element
        for member in subgroup
        for multiple in range(element.order())
    )


def _subobject_elements(subobject: "Module") -> frozenset:
    r"""Return the subobject's elements seen in the ambient module.

    Containment and equality of subobjects of one $A$ are statements about
    their images, so the images are what is compared -- the domain's own
    elements are elements of a different parent.
    """
    embedding = subobject.embedding()
    return frozenset(embedding(element) for element in subobject)


def _discriminant_category_of(form: "Module") -> Category:
    r"""Return the discriminant category ``form`` carries its form in.

    Which form a torsion module carries -- $q$ or $b$ -- is a fact about the
    object, read off its placement; constructions that produce another object
    of the same kind (subquotients, twists) ask here rather than take a flag.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_bilinear_modules import DiscriminantBilinearModules
    from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_quadratic_modules import DiscriminantQuadraticModules
    if form in DiscriminantQuadraticModules():
        return DiscriminantQuadraticModules()
    return DiscriminantBilinearModules()


# The one sanctioned crossing to Sage's torsion-quadratic engine: these are
# scratch modules built from the owned form's own matrix of representatives,
# consumed for normal forms and orthogonal groups and discarded; the private
# ``_modulus`` read mirrors the presentation trick Sage itself uses to state
# the bilinear (modulus_qf = modulus) case.
def _engine_torsion_module(form: "Module", quadratic: bool) -> "Parent":
    r"""Return Sage's torsion quadratic module carrying ``form``'s pairings.

    Built from the symmetric matrix of representatives on this object's own
    generators, so the engine's cover basis corresponds to them one to one --
    which is what lets engine answers cross back as combinations of this
    object's module generators.  For the bilinear case the module is
    re-presented at the bilinear modulus, Sage's own spelling of "the form is
    $b$ alone".
    """
    from sage.modules.torsion_quadratic_module import (
        TorsionQuadraticForm as _SageTorsionForm,
        TorsionQuadraticModule as _SageTorsionModule,
    )

    match quadratic:
        case True:
            gram = matrix(SageQQ, form.form().polar_form().gram_matrix())
        case False:
            gram = matrix(SageQQ, form.gram_matrix())
    engine = _SageTorsionForm(gram)
    assert Cardinal(engine.cardinality()) == form.cardinality(), (
        "the engine's torsion module must carry the whole group: a relation "
        "the denominators do not see was dropped"
    )
    if not quadratic:
        engine = _SageTorsionModule(
            engine.V(),
            engine.W(),
            modulus=engine._modulus,
            modulus_qf=engine._modulus,
        )
    return engine


def _engine_normal_form_key(form: "Module", quadratic: bool) -> tuple:
    r"""Return the engine's complete isometry invariant for ``form``.

    Sage's stated contract: two torsion quadratic modules are isomorphic
    exactly when they share their value modules and their normal form, so the
    key is the triple (modulus, invariants, normal-form Gram).
    """
    engine = _engine_torsion_module(form, quadratic)
    normal = engine.normal_form()
    gram = matrix(SageQQ, normal.gram_matrix_quadratic())
    gram.set_immutable()
    return (
        SageQQ(engine._modulus),
        SageQQ(engine._modulus_qf),
        tuple(normal.invariants()),
        gram,
    )


class TorsionFormAutomorphismGroup(FormHomset):
    r"""$O(A)$: the automorphisms of a finite torsion form, in its category.

    FOUNDATIONS Def 26.2: the orthogonal group of a discriminant form *is*
    $\operatorname{Aut}$ in its category -- a homset whose elements are the
    category's own form-preserving morphisms, with matrices derived views
    only (Remark 26.5: the matrix-subgroup description is invalid outside the
    homocyclic case, so no matrix group is built).  Generator data, order and
    enumeration are the engine's, translated back so every element crossing
    the boundary is a morphism of this homset.
    """

    def __init__(self, form: "Module", quadratic: bool) -> None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.refine import refine
        from sage.categories.groups import Groups as SageGroups
        FormHomset.__init__(self, form, form, form.category())
        # Aut in formed modules is a group; a finite form has a finite one.
        refine(self, [SageGroups().Finite()])
        self._engine_module = _engine_torsion_module(form, quadratic)
        self._engine_group = self._engine_module.orthogonal_group()

    def one(self) -> "FormMorphism":
        return self(
            {
                label: self.domain().module_generator(label)
                for label in self.domain().module_generating_set()
            }
        )

    def _from_engine(self, engine_automorphism: "Element") -> "FormMorphism":
        r"""Return the engine's automorphism as a morphism of this homset.

        The engine's cover basis corresponds to this object's generators
        (see :func:`_engine_torsion_module`), so the image of each generator
        is read off the engine's own right action and re-expressed as a
        combination of the owned generators.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.utilities import zipsum
        form = self.domain()
        cover = self._engine_module.V()
        generators = tuple(form.module_generators())
        images = {}
        for label, basis_vector in zip(
            form.module_generating_set(), cover.basis()
        ):
            image = self._engine_module(basis_vector) * engine_automorphism
            coordinates = cover.coordinates(image.lift())
            images[label] = zipsum(
                tuple(SageZZ(coordinate) for coordinate in coordinates),
                generators,
                form.zero(),
            )
        return self(images)

    def group_generators(self) -> "OrderedSet":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.sets.sets import finite_ordered_set
        stored = self.__dict__.get("_group_generators")
        if stored is None:
            stored = finite_ordered_set(
                tuple(
                    self._from_engine(generator)
                    for generator in self._engine_group.gens()
                )
            )
            self._group_generators = stored
        return stored

    def cardinality(self) -> "Cardinal":
        return Cardinal(self._engine_group.order())

    def order(self) -> "Cardinal":
        r"""Return $|O(A)|$.  The order of a group is its cardinality."""
        return self.cardinality()

    def is_finite(self) -> bool:
        return True

    def __iter__(self) -> "Iterator":
        for element in self._engine_group:
            yield self._from_engine(element)

    def _repr_(self) -> str:
        return f"Orthogonal group of {self.domain()}"


def _torsion_form_automorphism_group(
    form: "Module", quadratic: bool
) -> TorsionFormAutomorphismGroup:
    r"""Return the cached $O(A)$ of ``form``.

    Cached because a group is an object, not a value: its elements carry it
    as their parent, and two calls answering with two objects would make
    composition across them undefined.
    """
    cached = form.__dict__.get("_preamble_automorphism_group")
    if cached is None:
        cached = TorsionFormAutomorphismGroup(form, quadratic)
        form._preamble_automorphism_group = cached
    return cached


def _coordinates_in_module_generators(
    element: "Element",
    module_generating_set: "OrderedSet",
) -> "OrderedSet":
    r"""Return this element's coordinates in the requested generating set.

    One branch: an element answers what its coefficients are, and a presented
    module answers it as a free one does.  The case that read the private
    coordinate vector of a presented element instead returned coordinates in
    *that* element's own generating set, never the requested one, and agreed
    only when the two happened to coincide.
    """
    assert isinstance(element, Element), (
        f"{element} is not an element, so it has no coordinates"
    )
    coefficients = element.coefficients()
    return tuple(
        coefficients.get(generator, 0) for generator in module_generating_set
    )


# ---- shared construction: a torsion form is a cokernel ----

def regenerating_data(form: "FormMorphism", module_generators: "OrderedSet") -> tuple:
    r"""Return the relations and Gram matrix of ``form`` on ``module_generators``.

    The data of a torsion form, which is all a torsion form is: a presentation
    of the group on the new generating set, and the matrix of the form with
    respect to it.  No morphism is invented to hold them -- the object built
    from this pair is a torsion form in its own right, and whether it is also
    anyone's cokernel is a separate question with, here, the answer no.

    Both are read off this object's own data.  Its Gram matrix is part of what
    it is -- the form *with respect to its chosen module_generators* -- so the new one
    is $RGR^{\mathsf T}$ for $R$ the new module_generators' coordinates, which is a
    change of generating set and not a pairing computed behind the form's back.
    """
    module_generators = list(module_generators)
    assert all(generator.parent() is form for generator in module_generators), (
        "a generating set for this object is made of its own elements; "
        "elements of another module reach it through a morphism"
    )
    underlying_set = tuple(form.forget_form().module_generating_set())
    # Shaped, not inferred: the zero subobject is generated by nothing, and a
    # coordinate matrix read off an empty list of rows has no width to
    # multiply the Gram matrix by unless it is told the one it has.
    rows = matrix(
        SageQQ,
        len(module_generators),
        len(underlying_set),
        [
            coordinate
            for generator in module_generators
            for coordinate in _coordinates_in_module_generators(
                generator, underlying_set
            )
        ],
    )
    # The symmetric matrix the object is built on, whichever form it carries:
    # for a bilinear one its own, for a quadratic one its lift -- read off the
    # polarization, whose matrix records the lift (Def 25.4's inverse
    # bilinearization through the x2 value-module isomorphism).
    gram = _symmetric_representative_matrix(form.form())
    return relations_among(form, module_generators), rows * gram * rows.transpose()


def _symmetric_representative_matrix(morphism: "FormMorphism") -> "Matrix":
    r"""Return the symmetric matrix of representatives a torsion form is built on.

    For a bilinear form this is its own Gram matrix; for a quadratic form it
    is the diagonal lift -- the matrix of $b_q$ read back through the
    $\times 2$ isomorphism (Def 25.4), which is what the polarization's Gram
    matrix records.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
    match morphism:
        case QuadraticFormMorphism():
            return morphism.polar_form().gram_matrix()
        case _:
            return morphism.gram_matrix()


def relations_among(form: "FormMorphism", module_generators: "OrderedSet") -> "Matrix":
    r"""Return the relations among ``module_generators``: the kernel of $\mathbb Z^m\to A$.

    A column slice of a morphism matrix is a raw array again -- reading entries
    is where the wrapper stops -- so what comes back is one, and the consumer
    (``from_relations``) wraps it into the presentation it is the matrix of.
    """
    module_generators = list(module_generators)
    known = form.forget_form().relation_matrix()
    width = known.ncols()
    underlying_set = tuple(form.forget_form().module_generating_set())
    lifts = matrix(
        SageZZ,
        len(module_generators),
        width,
        [
            list(_coordinates_in_module_generators(generator, underlying_set))
            for generator in module_generators
        ],
    )
    kernel = MorphismMatrix(lifts).stack(known)._left_kernel_matrix()
    return kernel[:, : lifts.nrows()]


def p_adic_jordan_module_generators(
    form: "FormMorphism",
) -> list["ModuleElement"]:
    r"""Return lifts of generators putting ``form`` in $p$-adic Jordan normal form.

    Sage's reduction is the engine and works on a realization, so one is built
    from this object's own relations and Gram, run, and discarded; only the
    generators it chooses come back, as coordinates in $L^\vee$.  Nothing is
    told a value group it does not have -- an even $L$ gives the scratch module
    a $q$ and the reduction normalizes $q$; an odd one gives it $b$ alone.

    The even case serves the bilinear side too: Peters--Sterk Prop. 11.2.3 puts
    normal forms for symmetric and quadratic torsion forms on the same group in
    bijection, and $b_q$ is the polarization on the same generators.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.utilities import zipsum
    from sage.quadratic_forms.genera.normal_form import _normalize, p_adic_normal_form
    from sage.rings.padics.factory import Zp

    generators: list["Element"] = []
    exponent = form.annihilator().gen()
    for p in exponent.prime_divisors():
        # The primary decomposition is where the reduction can run: it is one
        # generator per $p$-primary cyclic factor, so the form written on it
        # has the rank the group has.
        embedding = form.primary_part(p).embedding()
        component = embedding.domain()
        engine = _p_adic_engine_matrix(component)

        # Degenerate directions are split off, normalized around, and put back.
        rank = engine.rank()
        match rank == engine.ncols():
            case True:
                split = engine.parent().identity_matrix()
            case False:
                integral = (engine * engine.denominator()).change_ring(SageZZ)
                split = integral.hermite_form(transformation=True)[1]
        degenerate, nondegenerate = split[rank:, :], split[:rank, :]
        engine = nondegenerate * engine * nondegenerate.transpose()

        precision = exponent.valuation(p) + 5
        padics = Zp(p, type="fixed-mod", prec=precision)
        # The reduction is written for p-adic lattices, so it runs on the
        # inverse form and the transformation is carried back.
        transform = p_adic_normal_form(
            engine.inverse(), p, precision=precision + 5
        )[1]
        transform = transform.change_ring(SageZZ).inverse().transpose()
        transform = transform.change_ring(padics).change_ring(SageZZ)
        scaled = (
            transform
            * engine
            * transform.transpose()
            * p ** engine.denominator().valuation(p)
        )
        transform = (
            _normalize(scaled.change_ring(padics), normal_odd=False)[1].change_ring(SageZZ)
            * transform
        )
        # Over $\mathbb Z$ before a row of it is read as coordinates: the
        # splitting is carried in the engine's rational matrix space, and a
        # coordinate vector in a torsion $\mathbb Z$-module is integral.  The
        # entries are integers already, so this asks for them as such and
        # fails loudly if the reduction ever produced otherwise.
        transform = (transform * nondegenerate).stack(degenerate).change_ring(SageZZ)

        # A row of the transformation is a combination of the component's
        # generators, so it is that element's coordinate vector; the embedding
        # carries it back into the whole group.
        generators.extend(
            embedding(
                zipsum(
            row,
            component.module_generators(),
            component.zero(),
        )
            )
            for row in transform.rows()
        )
    return generators


def _p_adic_engine_matrix(form: "FormMorphism") -> "Matrix":
    r"""Return the matrix of representatives the $p$-adic reduction reads.

    A raw array, and no morphism's matrix either: it is scratch input for
    Sage's reduction, which reads it with the raw surface -- denominators,
    a matrix space, a Hermite transformation -- and hands back a rational
    matrix of its own.

    Not a Gram matrix of anything: the reduction wants rational numbers, and
    these are chosen representatives of the form's values, scaled by the
    modulus so that the whole matrix lands in $[0,1)$.  The diagonal is the
    form's norm -- $q$ where there is one, $b(x,x)$ where there is not -- and
    that is where the two categories differ, because $q$ is read modulo
    $2\mathbb Z$ before scaling and $b(x,x)$ modulo $\mathbb Z$.
    """
    generators = tuple(
        form.module_generator(label)
        for label in form.module_generating_set()
    )
    size = len(generators)
    modulus = form.value_module().n

    def entry(i: int, left: "Element", j: int, right: "Element") -> "Element":
        match i == j:
            case True:
                return left.norm().lift() / modulus
            case False:
                return left.b(right).lift() / modulus

    return matrix(
        SageQQ,
        [
            [
                entry(i, left, j, right)
                for j, right in enumerate(generators)
            ]
            for i, left in enumerate(generators)
        ],
    )


def _format_cyclic_group_latex(orders: tuple[int, ...]) -> str:
    r"""Format cyclic group orders as ``C_n^m``."""
    if not orders:
        return "0"
    from collections import Counter

    counts = Counter(orders)

    def cyclic_factor(n: int, multiplicity: int) -> str:
        assert multiplicity >= 1
        match multiplicity:
            case 1:
                return f"C_{{{n}}}"
            case _ if multiplicity > 1:
                return f"C_{{{n}}}^{{{multiplicity}}}"
            case _:
                assert False, "a multiplicity is 1 or larger than 1"

    return " \\oplus ".join(
        cyclic_factor(n, counts[n])
        for n in sorted(counts)
    )


def _format_invariant_factor_latex(invariants: tuple[int, ...]) -> str:
    r"""Format invariant factors as ``C_n^m``."""
    return _format_cyclic_group_latex(invariants)


def _format_primary_decomp_latex(invariants: tuple[int, ...]) -> str:
    r"""Format the primary decomposition implied by invariant factors."""
    if not invariants:
        return "0"
    return _format_cyclic_group_latex(
        tuple(
            int(p) ** int(e)
            for n in invariants
            for p, e in factor(n)
        )
    )


def _form_gram_matrix_latex(module: "Module") -> str:
    r"""Return LaTeX for a form Gram matrix."""
    import re

    if not module.invariants():
        return "()"
    gram_str = str(_latex_fn(module.gram_matrix()))
    zero_dots = globals().get("_zero_dots", lambda: False)
    if zero_dots():
        gram_str = re.sub(r"\b0\b", lambda m: r"\cdot", gram_str)
    return gram_str


def subdivide_form_gram_matrix(module: "Module") -> None:
    r"""Partition ``module``'s Gram matrix once and replace ``gram_matrix``."""
    raw = module.gram_matrix()
    cuts = _form_gram_matrix_cuts(module, raw)
    match cuts:
        case []:
            G = raw
        case [_, *_]:
            G = raw.parent()(raw)
            G.subdivide(cuts, cuts)
    module.gram_matrix = lambda: G


def _form_gram_matrix_cuts(module: "Module", raw: "GramMatrix") -> list[int]:
    r"""Return the block cuts of ``module``'s form Gram matrix.

    The discriminant functor carries $L=\bigoplus L_i$ to $A=\bigoplus A_{L_i}$,
    so when the correlation's domain is decomposed its cuts are $A$'s -- and
    they have to be transported rather than recomputed, because a unimodular
    summand contributes a block of zeroes that reading the matrix alone would
    split into singletons.  A form on other generators has a synthesized domain
    carrying no decomposition, and there the matrix is all there is.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.forms.gram_matrices import _matrix_connected_component_cuts
    if raw.nrows() == 0:
        return []
    # Only a cokernel of a lattice morphism has a decomposition to transport:
    # the discriminant functor carries L = (+) L_i to A = (+) A_{L_i}, and a
    # unimodular summand contributes a block of zeroes that reading the matrix
    # alone would split into singletons.  A form on some other generating set
    # has no such morphism, and there the matrix is all there is.
    if module.category().is_subcategory(CokernelForms()):
        transported: list[int] = list(
            module.presentation().domain().gram_matrix().subdivisions()[0]
        )
        if transported and max(transported) < raw.nrows():
            return transported
    component_cuts: list[int] = _matrix_connected_component_cuts(raw)
    return component_cuts
