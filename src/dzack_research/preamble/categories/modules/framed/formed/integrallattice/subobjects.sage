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

from dzack_research.preamble.categories.rings.rings import ℤ
from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
    from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import MorphismMatrix

from sage.misc.misc_c import prod
from typing import Protocol, TYPE_CHECKING

from sage.categories.category import Category

from dzack_research.preamble.categories.sets.owned_sets import Sets

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    from dzack_research.preamble.lexicon import Element

    class SubobjectParent(Protocol):
        r"""What an object of this category offers.

        A subobject *is* its inclusion, so what this names is the ambient
        object's own surface plus the arrow.  Structural rather than a class:
        the subobject is an object of the ambient category, whatever class
        that category builds its objects from.
        """

        _form: "FormMorphism"
        _module: "Module"

        def embedding(self) -> "ModuleMorphism": ...
        def embedding_codomain(self) -> "Module": ...
        def ambient(self) -> "Module": ...
        def gram_matrix(self) -> "MorphismMatrix": ...
        def module_generators(self) -> tuple: ...
        def is_countable(self) -> bool: ...
        def is_primitive(self) -> bool: ...
        def embedded_module_generators(self) -> "OrderedSet": ...


class Subobjects(Category):
    r"""Modules carrying a chosen monomorphism into an ambient module."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "subobjects"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        # Sage's subquotient interface, in the nouns this preamble already
        # has.  A subobject *is* its inclusion, so the ambient object, the
        # lift and the retraction are all read off that one morphism rather
        # than stored again.
        def _form_morphism(self: "SubobjectParent") -> "FormMorphism":
            return self._form

        def forget_form(self: "SubobjectParent") -> "Module":
            return self._module

        def ambient(self: "SubobjectParent") -> "Module":
            r"""Return $B$, the object this one is a subobject of."""
            return self.embedding_codomain()

        def lift(self: "SubobjectParent", element: "Element") -> "Element":
            r"""Return $\iota(x)$, the element seen in the ambient object."""
            return self.embedding()(element)

        def retract(self: "SubobjectParent", element: "Element") -> "Element":
            r"""Return the $x$ with $\iota(x)$ the given ambient element."""
            return self.embedding().lift(element)

        def is_countable(self: "SubobjectParent") -> bool:
            r"""A subobject is countable exactly when its ambient is.

            It injects into the ambient, so it is no larger; and the
            countability is read off the object it sits in rather than
            recomputed from a presentation.
            """
            return bool(self.ambient().is_countable())

        def is_uncountable(self: "SubobjectParent") -> bool:
            r"""Whether this subobject is beyond every enumeration."""
            return not self.is_countable()

        def index(self: "SubobjectParent") -> "Integer":
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
            index: "Integer" = self.embedding().index()
            return index

        def is_primitive(self: "SubobjectParent") -> bool:
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
            primitive: bool = self.embedding().cokernel().is_torsion_free()
            return primitive

        is_saturated = is_primitive

        def saturation(self: "SubobjectParent") -> "SubobjectParent":
            r"""Return the primitive closure $S^{\mathrm{sat}}\subseteq M$.

            $S^{\mathrm{sat}}/S=\operatorname{tors}(M/S)$, so
            $S^{\mathrm{sat}}$ is the kernel of
            $M\twoheadrightarrow M/S\twoheadrightarrow(M/S)/\mathrm{tors}$.
            That composite is built from morphisms that already exist and its
            kernel is taken by the morphism, so no call site clears
            denominators or saturates a row lattice by hand.

            Taken in the underlying module.  Torsion is a module property and
            the form takes no part in deciding it, so the composite is a map
            of modules -- asking $M$ itself for it would look for a
            form-preserving map, and $(M/S)/\mathrm{tors}$ carries no form to
            preserve.  The kernel comes back as combinations of $M$'s own
            generators, on which $M$ re-imposes its structure.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
            from dzack_research.preamble.utilities import zipsum
            inclusion = self.embedding()
            ambient = inclusion.codomain()
            quotient = inclusion.cokernel()
            projection = quotient.torsion_free_quotient()
            torsion_free = ambient.forget_form().hom(
                {
                    label: projection(quotient.module_generator(label))
                    for label in ambient.module_generating_set()
                }
            )
            saturation: "SubobjectParent" = ambient.subobject_on(
                [
                    zipsum(
                        _coordinate_vector(generator),
                        ambient.module_generators(),
                        ambient.zero(),
                    )
                    for generator
                    in torsion_free.kernel().embedded_module_generators()
                ]
            )
            return saturation

        def index_in_saturation(self: "SubobjectParent") -> "Integer":
            r"""Return $[S^{\mathrm{sat}}:S]$, an index every subobject has.

            $S^{\mathrm{sat}}/S=\operatorname{tors}(M/S)$ -- the identity
            :meth:`saturation` is built from -- and a finitely generated
            torsion module is finite.  So this is a number for every $S$,
            unlike $[M:S]$, which is infinite as soon as $S$ has smaller rank
            than $M$; the two are the same only when $S$ is already of finite
            index.

            The torsion of $M/S$ is what the invariant factors of $M/S$ that
            are not zero multiply to.  That decomposition is the presented
            module's own, asked of it, and not a normal form computed here.
            """
            index: "Integer" = prod(
                invariant
                for invariant in self.embedding().cokernel().invariants()
                if invariant != 0
            )
            return index

        def sum(self: "SubobjectParent", other: "SubobjectParent") -> "SubobjectParent":
            r"""Return $S+T\subseteq B$, the join in the subobject lattice.

            The smallest subobject containing both, which is the span of both
            images: the ambient is handed every embedded generator of each and
            builds the subobject on them the way it builds every subobject.
            """
            assert self.embedding_codomain() == other.embedding_codomain(), (
                "the subobject sum lives in one common codomain; "
                f"left={self.embedding_codomain()}, right={other.embedding_codomain()}"
            )
            joined: "SubobjectParent" = self.ambient().subobject_on(
                list(self.embedded_module_generators())
                + list(other.embedded_module_generators())
            )
            return joined

        def intersection(self: "SubobjectParent", other: "SubobjectParent") -> "SubobjectParent":
            r"""Return $S\cap T\subseteq B$, the meet in the subobject lattice.

            An element of the intersection is $xA=-yB$ for $(x,y)$ in the
            kernel of the stacked embedding rows, so the meet is the image of
            that kernel under the first block -- the same kernel construction
            :meth:`saturation` routes through, never a rational span cleared
            by hand.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
            from dzack_research.preamble.utilities import zipsum
            assert self.embedding_codomain() == other.embedding_codomain(), (
                "the subobject intersection lives in one common codomain; "
                f"left={self.embedding_codomain()}, right={other.embedding_codomain()}"
            )
            ambient = self.ambient()
            left_rows = matrix(
                SageZZ,
                [
                    _coordinate_vector(image)
                    for image in self.embedded_module_generators()
                ],
            )
            right_rows = matrix(
                SageZZ,
                [
                    _coordinate_vector(image)
                    for image in other.embedded_module_generators()
                ],
            )
            stacked = left_rows.stack(right_rows)
            kernel_rows = stacked.left_kernel().basis_matrix()
            met_rows = kernel_rows.matrix_from_columns(
                range(left_rows.nrows())
            ) * left_rows
            met: "SubobjectParent" = ambient.subobject_on(
                [
                    zipsum(row, ambient.module_generators(), ambient.zero())
                    for row in met_rows.rows()
                ]
            )
            return met

        def embedded_module_generators(self: "SubobjectParent") -> "OrderedSet":
            r"""Return the images $\iota(e_i)$ of this subobject's generators.

            Not ``module_generators``: those are the abstract $e_i$ this
            module has as an object of the ambient category, and their
            coordinates have length ``rank``.  These are their images in the
            embedding's codomain, whose coordinates have that module's rank.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            return finite_ordered_set(
                tuple(
                    self.embedding()(generator)
                    for generator in self.module_generators()
                )
            )

        def isotropic_reduction(self: "SubobjectParent") -> "Module":
            r"""Return $S^{\perp}/S$ for an isotropic subobject of a formed module."""
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            from dzack_research.preamble.utilities import zipsum
            assert self.gram_matrix().is_zero(), (
                "isotropic reduction requires the form to vanish on the subobject"
            )
            codomain = self.embedding_codomain()
            perpendicular = self.embedding().orthogonal_complement()
            inclusion = perpendicular.embedding()
            relations = matrix(
                SageZZ,
                [
                    _coordinate_vector(
                        inclusion.lift(image)
                    )
                    for image in self.embedded_module_generators()
                ],
            )
            lifts = _free_quotient_lifts(perpendicular, relations)
            generators = tuple(
                zipsum(
                    lift,
                    perpendicular.module_generators(),
                    perpendicular.zero(),
                )
                for lift in lifts
            )
            gram = matrix(
                SageZZ,
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


def _free_quotient_lifts(module: "Module", relations: "MorphismMatrix") -> list:
    r"""Return coordinates in ``module``'s framing of its quotient's generators.

    The quotient by the submodule the rows of ``relations`` generate is the
    cokernel of the morphism they are the matrix of, and its invariant-factor
    generators are already written in ``module``'s coordinates -- the
    presented module carries the free module's generating set.  So the lift
    is the generator's coordinate vector, and no separate lifting map is
    needed.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
    rows = matrix(SageZZ, relations).rows()
    free = BasedFreeModule(ℤ, module.module_generating_set())
    domain = BasedFreeModule(ℤ, len(rows))
    presentation = module_homset(domain, free)(
        dict(
            zip(
                domain.module_generating_set(),
                (free._from_coordinates(row) for row in rows),
            )
        )
    )
    return [
        _coordinate_vector(generator)
        for generator in presentation.cokernel().smith_form_module_generators()
    ]


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
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
    from dzack_research.preamble.categories.abstract_categories.slice_categories import Slice
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.definite_lattices import DefiniteLattices
    from dzack_research.preamble.refine import refine
    assert isinstance(embedding, (ModuleMorphism, FormMorphism)), (
        "a module subobject is represented by a module or form morphism"
    )
    domain = embedding.domain()
    domain_category = domain.category()
    codomain = embedding.codomain()
    match ("_form" in domain.__dict__, "_form" in codomain.__dict__):
        case (True, _):
            form = domain.__dict__["_form"]
            underlying_module = domain.__dict__["_module"]
        case (False, True):
            form = codomain.form().pullback(embedding)
            underlying_module = domain
        case (False, False):
            form = None
            underlying_module = None
    subobject = Slice(embedding, is_mono=True)
    # The form is attached *before* refinement: admission into a category is
    # allowed to interrogate the candidate -- obligations, certifying
    # predicates, even its repr -- and a formed subobject that cannot answer
    # ``form()`` yet would be refused for the wrong reason.
    match form:
        case None:
            pass
        case _:
            subobject._form = form
            subobject._module = underlying_module
    categories = [domain_category, subobject.category(), Subobjects()]
    # A submodule of a definite lattice is where reduction is defined, so the
    # axiom is joined here rather than asserted at each call site.
    if embedding.codomain() in DefiniteLattices():
        categories.append(DefiniteLattices().Subobjects())
    subobject = refine(subobject, categories)
    return subobject
