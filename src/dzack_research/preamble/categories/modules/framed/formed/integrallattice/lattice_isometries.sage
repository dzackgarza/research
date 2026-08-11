r"""Isometries of integral lattices."""

from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Iterable

from sage_lattice_category_spike.lexicon import MorphismMatrix
if TYPE_CHECKING:
    from sage_lattice_category_spike.lexicon import Element
    from sage_lattice_category_spike.lexicon import Group
    from sage_lattice_category_spike.lexicon import Lattice

if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
    from sage.groups.matrix_gps.finitely_generated import MatrixGroup
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphism
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphismGroup
    from sage.categories.morphism import Morphism
    from dzack_research.preamble.categories.sets.sets import Set

from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormAutomorphismGroup
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import FiniteAutomorphismSubgroup
from typing import Self, TYPE_CHECKING

from sage.misc.cachefunc import cached_method

from sage_lattice_category_spike.objects.cardinals import Cardinal
from sage_lattice_category_spike.objects.morphism_matrices import matrix_group
from sage.categories.category import Category
from sage.categories.groups import Groups as SageGroups
from sage.quadratic_forms.quadratic_form import QuadraticForm as SageQuadraticForm
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import OrderedSet


def _definite_isometry_group_generator_matrices(lattice: "Lattice") -> tuple:
    r"""Return matrices generating \(O(L)\), for a definite \(L\).

    \(O(L)=\{M:MGM^t=G\}\) is a condition on the Gram matrix and on nothing
    else, so this is a call to the engine's algorithm with a matrix -- the way
    :meth:`IntegralLattices.ParentMethods.genus` is -- and not a passage into
    the engine's lattice objects.  The algorithm is Plesken--Souvignier, which
    the engine reaches through the quadratic form \(2G\); the doubling is the
    passage from the bilinear form to the quadratic one, and the sign is the
    lattice's, since \(O(L)=O(L(-1))\) and the algorithm wants the positive
    definite representative.

    A row of each matrix is the image of a framing label, which is the
    convention the whole preamble reads a morphism matrix in.  The engine's
    quadratic forms act on columns, hence the transpose -- and nothing rests
    on getting that right silently: a morphism is built from these matrices
    below, and its constructor rejects a map that does not preserve the form.

    Definite is the hypothesis and not a preference.  For an indefinite
    lattice no generating set is in hand: the engine has no algorithm, and
    :mod:`predicate_subgroups` exists because computing one for a common
    indefinite lattice runs for days.  That \(O(L)\) is nevertheless finitely
    generated is Borel and Harish-Chandra's theorem, which is why the group is
    placed in the finitely generated node without being asked to exhibit
    anything.
    """
    positive, negative = lattice.signature_pair()
    assert positive + negative == lattice.rank() and 0 in (positive, negative), (
        f"{lattice} is not definite, so no generating set of O(L) is in hand. "
        "Name a subgroup by its generators, or cut one out by a membership "
        "predicate"
    )
    gram = matrix(SageZZ, lattice.gram_matrix())
    quadratic_form = SageQuadraticForm(SageZZ, -2 * gram if positive == 0 else 2 * gram)
    # Over the integers, which the engine's quadratic forms do not say: an
    # isometry of an integral lattice permutes the lattice, so its matrix in
    # an integral framing has integral entries, and reading it over the
    # rationals would make the images rational combinations of generators.
    return tuple(
        generator.matrix().transpose().change_ring(SageZZ)
        for generator in quadratic_form.automorphism_group().gens()
    )


class LatticeIsometries(Category):
    r"""Invertible lattice homomorphisms.

    A group, as an object: the parents here are \(O(L)\) and its subgroups --
    an isometry homset is an endset, and composition of isometries is the
    group law.  So the owned group node is a super category rather than a
    declaration made again at each construction, and the words a group
    answers -- ``number_of_group_generators``, ``is_finitely_generated`` --
    reach these objects because they are groups and not because anything was
    written on them here.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattice isometries"

    def super_categories(self) -> list:
        r"""Return the homomorphism node and the finitely generated group node.

        Finitely generated and not merely a group: every object here has a
        finite generating set.  A subgroup was named by one, and \(O(L)\) has
        one by Borel and Harish-Chandra.  Not finitely *presented*, which
        \(O(L)\) itself carries and its subgroups do not: a finitely generated
        subgroup of a finitely presented group need not be finitely presented.

        Stating it here is also what orders the methods.  The finitely
        generated node answers ``group_generators`` by reading Sage's
        ``gens``, which these groups do not have -- they compute their
        generators from the Gram matrix -- and a category that this one
        declares as a super category is a category this one's methods
        precede.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_homomorphisms import LatticeHomomorphisms
        from dzack_research.preamble.categories.group.groups import OwnedFinitelyGeneratedGroups
        return [LatticeHomomorphisms(), OwnedFinitelyGeneratedGroups()]

    class ParentMethods:
        def is_countable(self: Self) -> bool:
            r"""Whether the isometries admit an enumeration.

            Read off finiteness, which this category already decides: a
            finite group is enumerated by listing it.  An indefinite lattice
            has an infinite isometry group, and countability of that is not
            settled here -- it is left to whatever decides it.
            """
            return bool(self.is_finite())

        def is_uncountable(self: Self) -> bool:
            r"""Whether the isometries are beyond every enumeration."""
            return not self.is_countable()

        def __call__(self: Self, images: "dict | FormMorphism") -> "Morphism":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_homomorphisms import LatticeHomomorphisms
            from dzack_research.preamble.refine import refine
            if isinstance(images, FormMorphism):
                # A homset is a parent and its morphisms are its elements, so
                # being handed one is a parent constructing an element it
                # already has.  Coercion discovery and ``an_element`` both ask
                # for exactly this; declaring it again through framing labels
                # would only rebuild what was passed in.
                assert images.domain() is self.domain(), (
                    f"{images} is not an isometry of {self.domain()}"
                )
                return images
            morphism = LatticeHomomorphisms.ParentMethods.__call__(
                self,
                images,
            )
            determinant = morphism.matrix().det()
            assert determinant in (1, -1), (
                f"an integral isometry has unit determinant, got {determinant}"
            )
            return refine(morphism, LatticeIsometries())

        def one(self: Self) -> "ModuleAutomorphism":
            return self(
                {
                    label: self.domain().module_generator(label)
                    for label in self.domain().module_generating_set()
                }
            )

        def an_element(self: Self) -> "ModuleAutomorphism":
            r"""Return the identity.

            Sage's generic ``_an_element_`` probes with ``self(0)``,
            ``self(1)`` and so on, which for an isometry group means
            declaring a lattice morphism from an integer.  A group has a
            distinguished element and this is it.
            """
            return self.one()

        def subgroup_on(self: Self, group_generators: "Set") -> "ModuleAutomorphismGroup":
            r"""Return the subgroup generated by a *set* of isometries."""
            assert all(generator in self for generator in group_generators), (
                "each subgroup generator must belong to this isometry group"
            )
            return LatticeIsometrySubgroup(self, group_generators)

        def _isometry_on_rows(self: Self, rows: "Iterable") -> "ModuleAutomorphism":
            r"""Return the isometry sending each framing label to a row's combination.

            The one place a matrix becomes an element of this group.  A row is
            read against the module generators, so what crosses back from the
            engine is a morphism of this lattice and never a matrix a caller
            would have to interpret.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum
            lattice = self.domain()
            return self(
                {
                    label: zipsum(row, lattice.module_generators(), lattice.zero())
                    for label, row in zip(lattice.module_generating_set(), rows)
                }
            )

        def group_generators(self: Self) -> TotallyOrderedFiniteSet:
            r"""Return \(S\) with \(\langle S\rangle\) this group.

            One question with two sources and one answer.  A subgroup was
            named by its generators and holds them; the full \(O(L)\) was not,
            so its generators are the ones the engine computes from the Gram
            matrix -- and once computed they are held the same way, which is
            what makes ``has_computed_group_generators`` true of both.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            stored = self.__dict__.get("_group_generators")
            if stored is None:
                stored = finite_ordered_set(
                    tuple(
                        self._isometry_on_rows(entries.rows())
                        for entries in
                        _definite_isometry_group_generator_matrices(self.domain())
                    )
                )
                self._group_generators = stored
            return stored

        @cached_method
        def _matrix_group(self: Self) -> "MatrixGroup":
            r"""Return this group as a GAP-backed matrix group.  The private model.

            \(O(L)\) is cut out of \(GL_n(R)\) by \(MGM^t=G\), so it and every
            subgroup of it is a matrix group on its generators' matrices.
            Deciding order, finiteness and enumeration from generators is
            Schreier--Sims and coset enumeration -- mature algorithms this
            repo calls and never restates.  Every method below defers here and
            translates the answers back into this group's own elements.
            """
            return matrix_group(
                generator.matrix() for generator in self.group_generators()
            )

        @cached_method
        def presented_group(self: Self) -> "FinitelyPresentedGroup":
            r"""Return this group as generators and relations.

            The finitely presented node's obligation, answered here: the words
            read off it -- ``presenting_free_group``, ``defining_relations``
            -- are that node's and are not restated here.

            A presentation is what coset enumeration produces, and the
            algorithm wants a permutation action to enumerate over, so the
            matrix group is realised as one first.  Both steps are the
            engine's.  Producing one at all needs the group enumerated, which
            is the definite case -- the same hypothesis
            :func:`_definite_isometry_group_generator_matrices` states, and
            for the same reason.  That \(O(L)\) *has* a finite presentation
            regardless is Borel and Harish-Chandra's theorem.

            Cached on the group and not on the lattice: a presentation is this
            group's own fact, and the lattice whose isometries it is is not
            where its computations belong.
            """
            return (
                self._matrix_group()
                .as_permutation_group()
                .as_finitely_presented_group()
            )

        def is_finite(self: Self) -> bool:
            r"""Return whether this group is finite, as decided by GAP."""
            return bool(self._matrix_group().is_finite())

        def cardinality(self: Self) -> "Cardinal":
            r"""Return \(|G|\), as computed by GAP."""
            return Cardinal(self._matrix_group().order())

        def order(self: Self) -> "Cardinal":
            r"""Return \(|G|\).  The order of a group is its cardinality."""
            return self.cardinality()

        def __iter__(self: Self):
            r"""Enumerate this group's elements, which a finite group has."""
            assert self.is_finite(), (
                f"{self} is infinite, so it cannot be enumerated"
            )
            for element in self._matrix_group():
                yield self._isometry_on_rows(element.matrix().rows())

    class MorphismMethods:
        def to_matrix(self: Self) -> "MorphismMatrix":
            return self.matrix()

        def is_identity(self: Self) -> bool:
            return self.matrix().is_one()

        def is_involution(self: Self) -> bool:
            return (self * self).is_identity()

        def __mul__(self: Self, other: object) -> "Element":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
            assert (
                isinstance(other, FormMorphism)
                and other.parent() is self.parent()
            ), "composition is internal to one isometry group"
            return self.parent()(
                {
                    label: self(other(other.domain().module_generator(label)))
                    for label in other.domain().module_generating_set()
                }
            )

        def inverse(self: Self) -> "ModuleAutomorphism":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum
            inverse_matrix = self.matrix().inverse().change_ring(SageZZ)
            return self.parent()(
                {
                    label: zipsum(
            row,
            self.domain().module_generators(),
            self.domain().zero(),
        )
                    for label, row in zip(
                        self.domain().module_generating_set(),
                        inverse_matrix.rows(),
                    )
                }
            )

        def cyclic_subgroup(self: Self) -> "Group":
            r"""Return \(\langle f\rangle\le O(L)\), the subgroup this generates.

            A group in its own right, and the \(G\) of the construction that
            names elements and takes what they generate; the action of that
            \(G\) on \(L\) is its own ``inclusion()``.  It is not the abstract \(C_n\):
            a caller who means an abstract group and a possibly unfaithful
            \(\rho\) constructs both, and hands \(\rho\) to ``with_action``.
            """
            return self.parent().subgroup_on({self})

        def _libgap_(self: Self) -> "GapElement":
            r"""Return this isometry inside its group's GAP model.

            A character is a function on a group, and when that group is a
            literal subgroup of \(O(L)\) its elements are these isometries;
            declaring where they sit in GAP is what makes GAP's characters
            functions on them rather than on a parallel set of matrices a
            caller would have to translate for.  This is the conversion
            protocol ``ClassFunction`` evaluates through.
            """
            return self.parent()._defining_matrix_group()(self.matrix()).gap()

        gap = _libgap_


class LatticeIsometrySubgroup(FiniteAutomorphismSubgroup, FormAutomorphismGroup):
    r"""The subgroup of \(O(L)\) generated by a set of isometries.

    Generated, not finite.  An isometry of an indefinite lattice can have
    infinite order, and finite-order isometries can generate an infinite
    group -- two reflections whose product has infinite order generate an
    infinite dihedral group.  So the generating set is what this object
    knows, finite generation is what it carries, and finiteness is a
    question put to GAP, never a constructor invariant.
    """

    def __init__(self, supergroup: "Group", group_generators: "Set") -> None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_homomorphisms import LatticeHomomorphisms
        from dzack_research.preamble.categories.sets.sets import finite_ordered_set
        from dzack_research.preamble.refine import refine
        lattice = supergroup.domain()
        assert supergroup.codomain() is lattice, (
            "an isometry group is an endomorphism homset"
        )
        FormAutomorphismGroup.__init__(self, lattice)
        # A subgroup of \(O(L)\) is a group, and that is the whole placement.
        # Not ``Groups().Finite()``: refining into the finite subcategory
        # asserts a theorem, and one that is generally hard -- it needs
        # \(O(L)\) computed, or a definiteness hypothesis.  Cardinality is
        # not a reason to reach for it, being total on sets already.
        #
        # Finitely generated is the one axiom the constructor does witness:
        # the generating set is the argument.  The isometry node carries the
        # group vocabulary and the engine's own node carries the axiom, so
        # the placement is what makes this object answer as a group.
        refine(
            self,
            [
                LatticeHomomorphisms(),
                LatticeIsometries(),
                SageGroups().FinitelyGenerated(),
            ],
        )
        assert group_generators, "a generated subgroup needs a generator"
        assert all(
            generator.parent() is supergroup for generator in group_generators
        ), "each subgroup generator must belong to the stated isometry group"
        self._group_generators = finite_ordered_set(
            [
                self(
                    {
                        label: generator(lattice.module_generator(label))
                        for label in lattice.module_generating_set()
                    }
                )
                for generator in group_generators
            ]
        )

    def __contains__(self, element: "Element") -> bool:
        r"""Return whether ``element`` lies in this subgroup.

        Membership is the one operation always available on a group carved
        out of \(GL_n(R)\) by a condition, so it is decided directly rather
        than by searching an enumeration.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
        return (
            isinstance(element, FormMorphism)
            and element.domain() is self.domain()
            # ``matrix`` converts through ``MorphismMatrix._matrix_``, the
            # owned protocol.  Asking the group directly would let Sage's
            # containment swallow the failed conversion and answer False for
            # an element that is present.
            and matrix(element.matrix()) in self._matrix_group()
        )

    def _repr_(self) -> str:
        return (
            f"Subgroup of O({self.domain()}) generated by "
            f"{self._group_generators.cardinality()} isometries"
        )
