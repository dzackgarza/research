r"""Finitely presented torsion modules.

A finite torsion $\mathbb Z$-module with a chosen generating set, presented by
a morphism $p:\mathbb Z^n\to\mathbb Z^m$ and by nothing else.  Every finitely
presented module is the cokernel of such a $p$, so this is what being finitely
presented *is*, not a mark of where the module came from -- a relation is a
generator of $p$'s domain, and the familiar relation matrix is $p$ read in the
two generating sets.

Which $p$ also settles what else is known.  When $p$ is a morphism of lattices
there is a cover to project from; when it is a correlation the cokernel is a
discriminant form; and when it is synthesized from a group and a matrix it is
none of those and the module is no worse for it.  Those are refinements of the
resulting object, not different kinds of module.

An element is a coordinate vector in the chosen generators, taken modulo the
lattice the relations span.  Two are equal when their difference lies in it,
which is decided by reducing against the Hermite form -- the same reduction
that gives each class a canonical representative to print and hash.
"""


from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
from dzack_research.preamble.utilities import zipsum
if TYPE_CHECKING:
    from sage_lattice_category_spike.lexicon import Group

from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
from dzack_research.preamble.categories.sets.sets import finite_ordered_set
from sage.misc.misc_c import prod
from sage.modules.free_module_element import vector
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

from dzack_research.preamble.categories.rings.rings import ℤ
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from collections.abc import Iterable
from typing import Self, TYPE_CHECKING

from sage.matrix.matrix0 import Matrix
from sage.categories.category import Category
from sage.categories.groups import Groups
from sage.categories.modules import Modules
from sage.matrix.special import diagonal_matrix
from sage.structure.parent import Parent

from sage_lattice_category_spike.lexicon import MorphismMatrix
from sage_lattice_category_spike.objects.sets import Sets

if TYPE_CHECKING:
    from sage.rings.ideal import Ideal_pid
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import OrderedSet


def _is_additive(group: "Group") -> bool:
    r"""Return whether ``group`` is written additively, asked of its category."""
    from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups

    return group.category().is_subcategory(CommutativeAdditiveGroups())


class FinitelyPresentedTorsionModules(OwnedCategoryOverBaseRing):
    r"""Finitely presented torsion modules with a chosen generating set over a base ring $R$."""

    @staticmethod
    def __classcall_private__(cls, base_ring=None):
        # Local: at module level this closes an import cycle; the ring module
        # is built by the time this category is constructed.
        from dzack_research.preamble.categories.rings.rings import engine_ring

        # Over the engine's integers, which is what the modules of this
        # category carry: the owned ring is the session's name for it, and a
        # category built over one while its objects carry the other has no
        # members at all.
        match base_ring:
            case None:
                return super().__classcall__(cls, SageZZ)
            case _ if engine_ring(base_ring) is SageZZ:
                return super().__classcall__(cls, SageZZ)
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

        return [
            TorsionModules(self.base_ring()),
            FinitelyPresentedModules(self.base_ring()),
        ]

    def direct_sum_of_cyclics(self, orders: "OrderedSet") -> "TorsionModule":
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
        return self.from_relations(MorphismMatrix(diagonal_matrix(SageZZ, orders)))

    def from_abelian_group(self, group: "Group") -> "TorsionModule":
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
                MorphismMatrix(matrix(SageZZ, 0, 0)),
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
        relations = MorphismMatrix(matrix(SageZZ, found).stack(diagonal_matrix(SageZZ, orders)))
        # Square again: the relation lattice has full rank, so its Hermite form
        # has one nonzero row per generator and the rest are padding.
        reduced = relations.normal_form(include_zero_rows=True)
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
        relations: "MorphismMatrix",
        module_generating_set: "OrderedSet" = None,
    ) -> "TorsionModule":
        r"""Return the module presented by ``relations``, as a morphism.

        The matrix is turned into the morphism it is the matrix of, because
        that is what a presentation is; nothing downstream sees the matrix
        except the linear algebra.
        """
        # Local: at module level these close an import cycle; the free module
        # and morphism modules are built by the time one is presented.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _module_morphism

        relations = MorphismMatrix(relations, SageZZ)
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


    class ElementMethods:
        r"""What torsion adds to being a module element, which is one thing.

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

        def order(self: Self) -> "Integer":
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

        def abelian_group(self: Self) -> "Group":
            r"""Return this module as a Sage finite abelian group."""
            from sage.groups.abelian_gps.abelian_group import AbelianGroup
            # Local: at module level this closes an import cycle; the group
            # module is built by the time a group is asked for.
            from dzack_research.preamble.categories.group.groups import own_group

            return own_group(AbelianGroup(list(self.invariants())))

        def is_p_elementary(self: Self, p: "Integer") -> bool:
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

        def primary_decomposition(self: Self) -> dict:
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

        def as_finitely_presented_group(self: Self) -> "Group":
            r"""Return this module as a finitely presented abelian group."""
            from sage.groups.free_group import FreeGroup
            from sage.misc.misc_c import prod
            # Local: at module level this closes an import cycle; the group
            # module is built by the time a group is asked for.
            from dzack_research.preamble.categories.group.groups import own_group

            relations = self.relation_matrix()
            size = relations.ncols()
            if size == 0:
                return own_group(FreeGroup(0, "e").quotient([]))

            free = FreeGroup([f"e{i + 1}" for i in range(size)])
            # A free *group*, so its generators are group generators.  The
            # module noun asks it for data it does not have -- the words
            # below are products in the group law, not linear combinations.
            generators = free.gens()
            words = [
                generators[i]
                * generators[j]
                * (generators[i] ^ -1)
                * (generators[j] ^ -1)
                for i in range(size)
                for j in range(i + 1, size)
            ]
            words.extend(
                prod(
                    (
                        generators[column] ^ int(row[column])
                        for column in range(size)
                    )
                )
                for row in relations.rows()
            )
            return own_group(free.quotient(words))

        def __iter__(self: Self):
            from sage.misc.mrange import cartesian_product_iterator

            reduced = self.relation_matrix().normal_form()
            bounds = [reduced[i, i] for i in range(self.number_of_module_generators())]
            for point in cartesian_product_iterator(
                [range(bound) for bound in bounds]
            ):
                yield self._from_coordinates(point)

        def annihilator(self: Self) -> "Ideal_pid":
            r"""Return the annihilator ideal \(\operatorname{Ann}(M)\subseteq R\).

            An ideal, not the exponent generating it: the consumer at
            ``torsion_modules_with_form`` asks it for ``.gen()``.
            """
            return SageZZ.ideal(self.exponent())


def TorsionModule(presentation: "ModuleMorphism") -> FinitelyPresentedModule:
    r"""Return the cokernel of ``presentation``, refined as torsion."""
    module = FinitelyPresentedModule(presentation)
    assert module in FinitelyPresentedTorsionModules(module.base_ring()), (
        "the presentation does not have torsion cokernel"
    )
    return module
