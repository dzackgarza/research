r"""Finitely presented torsion modules.

A finite torsion $\mathbb Z$-module with a chosen generating set and a chosen
presentation morphism $p:\mathbb Z^n\to\mathbb Z^m$.  Finite presentation is
a property of the module.  The selected $p$ is additional data.  A relation
is a generator of $p$'s domain.  The relation matrix is $p$ in the two
selected generating sets.

The selected $p$ also determines which constructions apply.  When $p$ is a
morphism of lattices, its codomain maps onto the cokernel.  When $p$ is a
correlation, the cokernel is the discriminant group.  Its induced form makes
it a discriminant form.  These facts refine the resulting object.

An element is a coordinate vector in the chosen generators, taken modulo the
lattice the relations span.  Two are equal when their difference lies in it,
which is decided by reducing against the Hermite form -- the same reduction
that gives each class a canonical representative to print and hash.
"""


from sage.rings.integer_ring import ZZ as SageZZ
from typing import Protocol, TYPE_CHECKING
from dzack_research.preamble.utilities import zipsum
if TYPE_CHECKING:
    from sage.categories.groups import Group

from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
from dzack_research.preamble.categories.sets.sets import finite_ordered_set
from sage.misc.misc_c import prod
from sage.modules.free_module_element import vector
from sage.structure.element import ModuleElement as SageModuleElement
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

from dzack_research.preamble.categories.rings.rings import ℤ
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from collections.abc import Iterable
from typing import Self, TYPE_CHECKING

from sage.matrix.matrix0 import Matrix
from sage.categories.category import Category
from sage.categories.groups import Groups
from sage.matrix.special import diagonal_matrix
from sage.misc.cachefunc import cached_method
from sage.structure.parent import Parent

from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import (
    row_normal_form,
)
from dzack_research.preamble.categories.sets.owned_sets import Sets

if TYPE_CHECKING:
    from collections.abc import Iterator

    from sage.rings.ideal import Ideal_pid
    from sage.rings.ring import Ring
    from dzack_research.preamble.lexicon import Element
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet
    from sage.structure.element import Vector


def _is_additive(group: "Group") -> bool:
    r"""Return whether ``group`` is written additively, asked of its category."""
    from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups

    additive: bool = group.category().is_subcategory(CommutativeAdditiveGroups())
    return additive


if TYPE_CHECKING:
    class TorsionModuleParent(Protocol):
        r"""What a parent placed in ``FinitelyPresentedTorsionModules(R)``
        supplies: the presentation, the generating set and its size, the zero,
        the coordinate route in, the invariant factors, and the exponent."""

        def relation_matrix(self) -> Matrix: ...
        def number_of_module_generators(self) -> int: ...
        def module_generators(self) -> "OrderedSet": ...
        def zero(self) -> "Element": ...
        def invariants(self) -> tuple: ...
        def exponent(self) -> "Integer": ...
        def annihilator(self) -> "Ideal_pid": ...
        def presenting_free_group(self) -> "Group": ...
        def _from_coordinates(self, coordinates: "Vector") -> "Element": ...

    class TorsionModuleElement(Protocol):
        r"""What an element of a torsion module supplies."""

        def parent(self) -> "TorsionModuleParent": ...
        def is_zero(self) -> bool: ...


class FinitelyPresentedTorsionModules(OwnedCategoryOverBaseRing):
    r"""Finitely presented torsion modules with a chosen generating set over a base ring $R$."""

    @staticmethod
    def __classcall_private__(
        cls: type["FinitelyPresentedTorsionModules"], base_ring: "Ring"
    ) -> "FinitelyPresentedTorsionModules":
        # Local: at module level this closes an import cycle; the ring module
        # is built by the time this category is constructed.
        from dzack_research.preamble.categories.rings.rings import engine_ring

        # Over the engine's integers, which is what the modules of this
        # category carry: the owned ring is the session's name for it, and a
        # category built over one while its objects carry the other has no
        # members at all.
        over_the_integers: "FinitelyPresentedTorsionModules"
        match base_ring:
            case _ if engine_ring(base_ring) is SageZZ:
                over_the_integers = super().__classcall__(cls, SageZZ)
                return over_the_integers
            case _:
                assert False, (
                    "this finite-presentation implementation is over ZZ"
                )

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely presented torsion modules"

    def super_categories(self) -> list:
        # Local: at module level these close an import cycle; both categories
        # are built by the time supercategories are asked for.
        from dzack_research.preamble.categories.modules.pure.torsion_modules import TorsionModules
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModules
        from dzack_research.preamble.categories.group.groups import OwnedFiniteAbelianGroups
        from dzack_research.preamble.categories.group.finitely_presented_groups import GroupsWithChosenFinitePresentation

        return [
            TorsionModules(self.base_ring()),
            FinitelyPresentedModules(self.base_ring()),
            OwnedFiniteAbelianGroups(),
            GroupsWithChosenFinitePresentation(),
        ]

    def direct_sum_of_cyclics(self, orders: "OrderedSet") -> FinitelyPresentedModule:
        r"""Return $\bigoplus_i\mathbb Z/d_i$ on one generator per summand.

        The orders are taken as given and not normalized: $[2,3]$ builds a
        module on *two* generators, not $\mathbb Z/6$ on one.  Those two are
        isomorphic and are not equal, and which one this is matters to
        everything written on the generating set afterwards.
        """
        orders = [d for d in orders]
        assert all(d > 1 for d in orders), (
            f"each summand needs an order greater than 1, got {orders}"
        )
        return self.from_relations(
            diagonal_matrix(SageZZ, orders)
        )

    def from_abelian_group(self, group: "Group") -> FinitelyPresentedModule:
        r"""Return ``group`` as an object of this category, on its own generators.

        The generating set is the one the group already has.  Nothing is
        normalized: $C_2\times C_3$ arrives with two generators and stays with
        two, even though its invariant factor decomposition is the cyclic group
        of order 6 on one.  They are isomorphic and not equal, and a form
        written on two generators cannot be transported to one without choosing
        an isomorphism nobody asked for.

        What has to be *discovered* is the relations, since a group hands over
        generators and their orders but not what combinations of them vanish.
        The relation lattice contains $\operatorname{diag}(\text{orders})$, so
        it is found inside the finite group $\mathbb Z^n/\operatorname{diag}$
        by asking which of its elements the generators kill.
        """
        assert group.is_finite(), f"{group} is not finite, so it is not torsion"
        # Commutativity is an axiom for some parents and a computation for
        # others -- a permutation group is not in Groups().Commutative() even
        # when it is abelian -- so both are accepted and neither is assumed.
        assert (
            _is_additive(group)
            or group.category().is_subcategory(Groups().Commutative())
            or group.is_abelian()
        ), f"{group} is not abelian, so it is not a torsion Z-module"
        generators = tuple(group.group_generators())
        if not generators:
            return self.from_relations(
                matrix(SageZZ, 0, 0),
                Sets.Δ[-1],
            )
        orders = [generator.order() for generator in generators]
        size = prod(orders)
        assert size <= 10 ** 6, (
            f"{group}'s generators have orders {orders}, whose product {size} "
            "is too large to search for relations; build the module from a "
            "presentation instead"
        )

        combine, identity = self._group_arithmetic(group)
        from sage.misc.mrange import cartesian_product_iterator

        found = [
            vector(SageZZ, exponents)
            for exponents in cartesian_product_iterator([range(d) for d in orders])
            if combine(generators, exponents) == identity
        ]
        relations = matrix(SageZZ, found).stack(diagonal_matrix(SageZZ, orders))
        # Square again: the relation lattice has full rank, so its Hermite form
        # has one nonzero row per generator and the rest are padding.
        reduced = row_normal_form(relations, include_zero_rows=True)
        return self.from_relations(
            reduced[: len(orders), :],
            finite_ordered_set(generators),
        )

    def _group_arithmetic(self, group: "Group") -> tuple:
        r"""Return how to form $\sum a_ig_i$ in ``group``, and its identity.

        Sage writes finite abelian groups both ways -- ``AbelianGroup``
        multiplicatively, ``AdditiveAbelianGroup`` additively -- and a
        combination of generators means the same thing in either.  Which
        notation is in use is a fact about the group's category, not about
        which methods it happens to answer to.
        """
        if _is_additive(group):
            identity = group.zero()
            return (
                lambda gens, exps: zipsum(
                    exps,
                    gens,
                    identity,
                    term=lambda a, g: a * g,
                ),
                identity,
            )
        identity = group.one()
        return (
            lambda gens, exps: prod(
                (g ** a for a, g in zip(exps, gens)), identity
            ),
            identity,
        )

    def from_relations(
        self,
        relations: "Matrix",
        module_generating_set: "OrderedSet" = None,
    ) -> FinitelyPresentedModule:
        r"""Return the module presented by ``relations``, as a morphism.

        The matrix is turned into the morphism it is the matrix of, because
        that is what a presentation is; nothing downstream sees the matrix
        except the linear algebra.
        """
        # Local: at module level these close an import cycle; the free module
        # and morphism modules are built by the time one is presented.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _module_morphism

        relations = relations.change_ring(SageZZ)
        domain = BasedFreeModule(ℤ, Sets.Δ[relations.nrows() - 1])
        match module_generating_set:
            case None:
                module_generating_set = Sets.Δ[relations.ncols() - 1]
            case Parent() | Iterable():
                module_generating_set = finite_ordered_set(module_generating_set)
                assert module_generating_set.cardinality() == relations.ncols(), (
                    "the generating set and presentation have different widths"
                )
            case _:
                assert False, (
                    "a generating set is a finite set or finite iterable"
                )
        codomain = BasedFreeModule(ℤ, module_generating_set)
        return TorsionModule(
            _module_morphism(
                domain,
                codomain,
                dict(
                    zip(
                        domain.module_generating_set(),
                        (codomain._from_coordinates(row) for row in relations.rows()),
                    )
                )
            )
        )


    class ElementMethods(SageModuleElement):
        r"""What torsion adds to being a module element, which is one thing.

        The base is the *layout*, not the methods: an owned class takes its
        instance layout from its first base, and the first base here is this
        provider.  Without it the class is laid out on whichever branch Sage's
        linearization put first -- for a discriminant group that is the group
        branch, which ends at ``Element`` -- and then Sage's
        ``RightModuleAction._act_``, which casts to ``ModuleElement``
        unchecked and calls ``_lmul_`` through that class's method table,
        jumps through a table with no such slot.  These elements are added and
        scaled, so ``ModuleElement`` is the layout they must have.


        Addition, negation and the action of $\mathbb Z$ are structure -- they
        are exactly the structure of $\mathbb Z\text{-Mod}$, which this
        category is under, so they arrive with membership and are not restated
        here.  Restating them on a subcategory would assert that torsion
        modules add something to them, which they do not: they are the same
        operations they are in any module, free or not.

        (Sage still wants the arithmetic itself on the element class, because
        its coercion model dispatches ``_add_`` and ``_lmul_`` there.  That is
        where a representation says how to add coordinate vectors; it is not
        where the operations belong.)

        What torsion does add is that the annihilator of an element is a
        nonzero ideal, so it has a generator.
        """

        def additive_order(self: "TorsionModuleElement") -> "Integer":
            r"""Return the generator of $\operatorname{Ann}(a)\subseteq\mathbb Z$.

            The least $k\ge 1$ with $ka=0$, which exists because this module is
            torsion -- in a free module the same ideal is zero and there is
            nothing to return.  It agrees numerically with the element's order
            in the underlying group, and is not that statement.
            """
            parent = self.parent()
            if self == parent.zero():
                return 1
            exponent = parent.exponent()
            multiple = 1
            while multiple <= exponent:
                if (multiple * self).is_zero():
                    return multiple
                multiple += 1
            assert False, (
                "an element of a finite torsion module has finite order"
            )

    class ParentMethods:
        r"""What a torsion module is asked, none of which involves a form."""

        def _latex_(self: "TorsionModuleParent") -> str:
            r"""Return the chosen module presentation in additive notation.

            Commutativity is part of the category of modules.  Thus the
            displayed relations are the rows of the presentation matrix.
            The presentation of the underlying group retains its commutator
            relators.
            """
            from dzack_research.preamble.categories.group.finitely_presented_groups import (
                _fp_format_presentation_latex,
            )

            generators = tuple(
                f"e_{{{index}}}"
                for index in range(1, self.number_of_module_generators() + 1)
            )

            def relation(row: "Vector") -> str:
                terms: list[str] = []
                for coefficient, generator in zip(row, generators):
                    coefficient = int(coefficient)
                    if coefficient == 0:
                        continue
                    magnitude = abs(coefficient)
                    term = (
                        generator
                        if magnitude == 1
                        else f"{magnitude}{generator}"
                    )
                    if not terms:
                        terms.append(f"-{term}" if coefficient < 0 else term)
                    else:
                        terms.append(
                            f" {'-' if coefficient < 0 else '+'} {term}"
                        )
                return f"{''.join(terms) if terms else '0'}=0"

            relations = tuple(
                relation(row) for row in self.relation_matrix().rows()
            )
            presentation: str = _fp_format_presentation_latex(
                generators,
                relations,
                subscript="\\mathbb{Z}",
            )
            return presentation

        def is_abelian(self: "TorsionModuleParent") -> bool:
            r"""Return ``True`` because module addition is commutative."""
            return True

        def group_generators(self: "TorsionModuleParent") -> "OrderedSet":
            r"""Return the module generators as additive group generators."""
            zero = self.zero()
            return finite_ordered_set(
                tuple(
                    generator
                    for generator in self.module_generators()
                    if generator != zero
                )
            )

        @cached_method
        def presenting_free_group(self: "TorsionModuleParent") -> "Group":
            r"""Return the free group on the chosen module generators."""
            from sage.groups.free_group import FreeGroup

            size = self.number_of_module_generators()
            match size:
                case 0:
                    return FreeGroup(0, "e")
                case _:
                    return FreeGroup([f"e{i + 1}" for i in range(size)])

        @cached_method
        def defining_relations(self: "TorsionModuleParent") -> "OrderedSet":
            r"""Return commutativity and module relations as group words."""
            free = self.presenting_free_group()
            generators = free.gens()
            words = [
                generators[i]
                * generators[j]
                * (generators[i] ^ -1)
                * (generators[j] ^ -1)
                for i in range(len(generators))
                for j in range(i + 1, len(generators))
            ]
            words.extend(
                prod(
                    (
                        generators[column] ^ int(row[column])
                        for column in range(len(generators))
                    ),
                    free.one(),
                )
                for row in self.relation_matrix().rows()
            )
            return finite_ordered_set(words)

        def is_p_elementary(self: "TorsionModuleParent", p: "Integer") -> bool:
            r"""Return whether $pA=0$, so that $A$ is a vector space over $\mathbb F_p$.

            The definition, asked of the module: $p$ kills $A$ exactly when it
            lies in $\operatorname{Ann}(A)$, and the annihilator is an ideal
            this module already has.  The route through an abelian group and
            then a permutation representation of it put two questions to a
            proxy twice removed -- and being killed by $p$ is not a statement
            about a permutation representation.
            """
            assert p.is_prime(), f"p must be prime, got {p}"
            return p in self.annihilator()

        def primary_decomposition(self: "TorsionModuleParent") -> dict:
            r"""Return the primary decomposition as $\{p: \text{orders}\}$.

            An invariant of the isomorphism class, read off the invariant
            factors: $\mathbb Z/d\cong\bigoplus_p\mathbb Z/p^{v_p(d)}$.
            """
            prime_powers = tuple(
                (prime, prime ** exponent)
                for factor_ in self.invariants()
                for prime, exponent in factor_.factor()
            )
            return {
                prime: tuple(
                    power
                    for term_prime, power in prime_powers
                    if term_prime == prime
                )
                for prime in sorted({prime for prime, _ in prime_powers})
            }

        def __iter__(self: "TorsionModuleParent") -> "Iterator[Element]":
            from sage.misc.mrange import cartesian_product_iterator

            reduced = row_normal_form(self.relation_matrix())
            bounds = [reduced[i, i] for i in range(self.number_of_module_generators())]
            for point in cartesian_product_iterator(
                [range(bound) for bound in bounds]
            ):
                yield self._from_coordinates(point)

        def annihilator(self: "TorsionModuleParent") -> "Ideal_pid":
            r"""Return the annihilator ideal \(\operatorname{Ann}(M)\subseteq R\).

            An ideal, not the exponent generating it: the consumer at
            ``torsion_modules_with_form`` asks it for ``.gen()``.
            """
            annihilator: "Ideal_pid" = SageZZ.ideal(self.exponent())
            return annihilator


def TorsionModule(presentation: "ModuleMorphism") -> FinitelyPresentedModule:
    r"""Return the cokernel of ``presentation``, refined as torsion."""
    module = FinitelyPresentedModule(presentation)
    assert module in FinitelyPresentedTorsionModules(module.base_ring()), (
        "the presentation does not have torsion cokernel"
    )
    return module
